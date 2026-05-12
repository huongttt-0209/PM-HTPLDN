#!/usr/bin/env python3
"""Standalone CLI verifier for bug-report markdown files.

Uses shared parser in `.claude/hooks/bug_report_parser.py` — single source of truth.
NO file modification. Reports violations + classification per file.

Usage:
    python3 .claude/scripts/verify-bug-reports.py <folder|file>...
        # Default: human-readable summary table + counts per classification.

    python3 .claude/scripts/verify-bug-reports.py --json <folder|file>
        # JSON output (one object per file, suitable for piping to jq).

    python3 .claude/scripts/verify-bug-reports.py --csv <folder|file>
        # CSV output: filepath,classification,severity_table_format,bst_schema,total,closed,open,...

    python3 .claude/scripts/verify-bug-reports.py --queue <folder|file>
        # List files per nhóm A/B/C/D/X — drives migration workflow.

Classification (mutually exclusive):
    A — 6-col Severity present + BST consistent + all rows classifiable → SCRIPT-MIGRATE
    B — No Severity table + BST present → MANUAL: add table
    C — Severity present but wrong format/multi-row/inconsistent counts → MANUAL: check
    D — Already 8-col Severity + counts consistent → SKIP (already done)
    X — No BST or unparseable → MANUAL: special case

Exit code: 0 always (verifier is non-blocking; this is recon).
"""
from __future__ import annotations

import argparse
import csv
import json
import sys
from pathlib import Path

# Make parser importable
HOOKS_DIR = Path(__file__).resolve().parent.parent / "hooks"
sys.path.insert(0, str(HOOKS_DIR))
from bug_report_parser import parse_bug_report  # noqa: E402

# File filter — same as audit subagent
SKIP_NAME_PREFIXES = ("dev-seed-request-", "seed-request-", "non-dev-")
SKIP_NAMES = ("file_name.md",)
SKIP_PATH_PARTS = ("/image/", "/_archive/", "/screenshots/", "/img/")


def is_bug_report_file(p: Path) -> bool:
    """Filter rule: file must look like an actual bug-report MD (not evidence/seed-request)."""
    if p.suffix.lower() != ".md":
        return False
    name = p.name
    if name in SKIP_NAMES:
        return False
    for prefix in SKIP_NAME_PREFIXES:
        if name.startswith(prefix):
            return False
    if name.startswith("bug-bc-") and name.endswith("-evidence.md"):
        return False
    path_str = str(p).replace("\\", "/")
    for part in SKIP_PATH_PARTS:
        if part in path_str:
            return False
    # Must match bug-report-*.md or Pass-bug-report-*.md
    base = name
    if not (
        base.startswith("bug-report-")
        or base.startswith("Pass-bug-report-")
    ):
        return False
    return True


def collect_files(targets: list[str]) -> list[Path]:
    out: list[Path] = []
    for t in targets:
        p = Path(t)
        if p.is_file():
            out.append(p)
            continue
        if p.is_dir():
            for f in sorted(p.rglob("*.md")):
                if is_bug_report_file(f):
                    out.append(f)
            continue
        print(f"WARN: target not found: {t}", file=sys.stderr)
    # Deduplicate while preserving order
    seen = set()
    result: list[Path] = []
    for f in out:
        rp = f.resolve()
        if rp not in seen:
            seen.add(rp)
            result.append(f)
    return result


def fmt_summary_table(results: list[dict]) -> str:
    """Human-readable summary table."""
    lines = []
    lines.append(
        f"{'Module':<22} {'Filename':<55} {'Cls':<3} {'SevFmt':<8} {'BstSch':<14} "
        f"{'Tot':>3} {'Crit':>4} {'Maj':>3} {'Med':>3} {'Min':>3} {'Triv':>4} "
        f"{'Cls':>3} {'Opn':>3} {'Def':>3} {'Unk':>3} Consist"
    )
    lines.append("-" * 175)
    for r in results:
        fp = Path(r["filepath"])
        module = fp.parent.name
        filename = fp.name
        cls = r["classification"]
        sev_fmt = r["severity_table"]["format"]
        bst_sch = r["bst"]["schema"]
        c = r["bst"]["counts"]
        sc = r["bst"]["severity_counts"]
        cons = r["consistency"]
        cons_str = (
            ("S" if cons.get("severity_sum_matches_total") else "·")
            + ("O" if cons.get("closed_plus_open_matches_total") else "·")
            + ("T" if cons.get("severity_table_matches_bst") else "·")
        )
        lines.append(
            f"{module:<22} {filename[:55]:<55} {cls:<3} {sev_fmt:<8} {bst_sch:<14} "
            f"{c.get('total', 0):>3} {sc.get('critical', 0):>4} {sc.get('major', 0):>3} "
            f"{sc.get('medium', 0):>3} {sc.get('minor', 0):>3} {sc.get('trivial', 0):>4} "
            f"{c.get('closed', 0):>3} {c.get('open', 0):>3} {c.get('defer', 0):>3} {sc.get('unknown', 0):>3} {cons_str}"
        )
    # Summary footer
    counts = {"A": 0, "B": 0, "C": 0, "D": 0, "X": 0}
    for r in results:
        counts[r["classification"]] = counts.get(r["classification"], 0) + 1
    lines.append("")
    lines.append(
        f"Total: {len(results)} files | "
        f"A={counts['A']} (script-migrate) | "
        f"B={counts['B']} (no sev table) | "
        f"C={counts['C']} (manual check) | "
        f"D={counts['D']} (already 8-col OK) | "
        f"X={counts['X']} (special case)"
    )
    lines.append(
        "Consist legend: S=severity_sum==total, O=closed+open==total, T=severity_table==bst (or · if false/null)"
    )
    return "\n".join(lines)


def fmt_queue(results: list[dict]) -> str:
    """Per-classification file list for migration planning."""
    buckets: dict[str, list[dict]] = {"A": [], "B": [], "C": [], "D": [], "X": []}
    for r in results:
        buckets[r["classification"]].append(r)
    lines = []
    labels = {
        "A": "Nhóm A — SCRIPT-MIGRATE (6-col → 8-col, counts consistent)",
        "B": "Nhóm B — MANUAL: add Severity table (BST present, no table)",
        "C": "Nhóm C — MANUAL: check format/counts (multi-row, custom header, or discrepancy)",
        "D": "Nhóm D — SKIP (already 8-col with consistent counts)",
        "X": "Nhóm X — MANUAL: special (no BST or unparseable)",
    }
    for cls in ["A", "B", "C", "D", "X"]:
        lines.append(f"\n## {labels[cls]} ({len(buckets[cls])} files)\n")
        for r in buckets[cls]:
            fp = Path(r["filepath"])
            module = fp.parent.name
            c = r["bst"]["counts"]
            sc = r["bst"]["severity_counts"]
            note_bits = []
            if cls == "A":
                note_bits.append(
                    f"counts: total={c['total']} closed={c['closed']} open={c['open']} "
                    f"(C{sc['critical']}/M{sc['major']}/m{sc['medium']}/n{sc['minor']}/t{sc['trivial']})"
                )
            elif cls == "B":
                note_bits.append(f"bst={r['bst']['schema']} total={c['total']} closed={c['closed']} open={c['open']}")
            elif cls == "C":
                reasons = []
                if r["severity_table"]["format"] == "unknown":
                    reasons.append(f"sev-fmt=unknown (rows={r['severity_table']['data_row_count']})")
                if r["severity_table"]["format"] == "8-col":
                    reasons.append("sev=8-col but counts off")
                if c.get("unknown"):
                    reasons.append(f"status_unknown={c['unknown']}")
                if sc.get("unknown"):
                    reasons.append(f"severity_unknown={sc['unknown']}")
                cons = r["consistency"]
                if cons.get("severity_sum_matches_total") is False:
                    reasons.append("sev_sum!=total")
                if cons.get("closed_plus_open_matches_total") is False:
                    reasons.append("closed+open!=total")
                note_bits.append(", ".join(reasons) or "see --json for detail")
            elif cls == "D":
                note_bits.append(
                    f"counts: total={c['total']} closed={c['closed']} open={c['open']}"
                )
            elif cls == "X":
                note_bits.append(f"bst.present={r['bst']['present']} err={r['error']}")
            lines.append(f"- [{module}] {fp.name}  — {' | '.join(note_bits)}")
    return "\n".join(lines)


def fmt_csv(results: list[dict]) -> str:
    import io

    buf = io.StringIO()
    w = csv.writer(buf)
    w.writerow(
        [
            "filepath",
            "module",
            "classification",
            "severity_table_format",
            "severity_table_rows",
            "bst_schema",
            "total",
            "critical",
            "major",
            "medium",
            "minor",
            "trivial",
            "closed",
            "open",
            "defer",
            "withdrawn",
            "status_unknown",
            "severity_unknown",
            "sev_sum_match",
            "closed_open_match",
            "sev_table_match_bst",
        ]
    )
    for r in results:
        fp = Path(r["filepath"])
        c = r["bst"]["counts"]
        sc = r["bst"]["severity_counts"]
        cons = r["consistency"]
        w.writerow(
            [
                str(fp),
                fp.parent.name,
                r["classification"],
                r["severity_table"]["format"],
                r["severity_table"]["data_row_count"],
                r["bst"]["schema"],
                c.get("total", 0),
                sc.get("critical", 0),
                sc.get("major", 0),
                sc.get("medium", 0),
                sc.get("minor", 0),
                sc.get("trivial", 0),
                c.get("closed", 0),
                c.get("open", 0),
                c.get("defer", 0),
                c.get("withdrawn", 0),
                c.get("unknown", 0),
                sc.get("unknown", 0),
                cons.get("severity_sum_matches_total"),
                cons.get("closed_plus_open_matches_total"),
                cons.get("severity_table_matches_bst"),
            ]
        )
    return buf.getvalue()


def main(argv: list[str]) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("targets", nargs="+", help="Files or folders to verify")
    fmt_group = ap.add_mutually_exclusive_group()
    fmt_group.add_argument("--json", action="store_true", help="JSON output (1 line per file)")
    fmt_group.add_argument("--csv", action="store_true", help="CSV output")
    fmt_group.add_argument("--queue", action="store_true", help="Per-classification file list")
    args = ap.parse_args(argv[1:])

    files = collect_files(args.targets)
    if not files:
        print("No bug-report files matched.", file=sys.stderr)
        return 0
    results = [parse_bug_report(f) for f in files]

    if args.json:
        for r in results:
            print(json.dumps(r, ensure_ascii=False))
    elif args.csv:
        print(fmt_csv(results), end="")
    elif args.queue:
        print(fmt_queue(results))
    else:
        print(fmt_summary_table(results))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
