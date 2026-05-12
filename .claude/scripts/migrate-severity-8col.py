#!/usr/bin/env python3
"""One-shot migration: Severity breakdown table → 8-col (Tổng + 5 sev + Closed + Open).

Touch rules (CRITICAL — preserve BA-confirm + body):
- Only modifies the Severity breakdown table block. Never touches Bug Summary Table,
  bug detail sections, observations/BA-confirm appendix, or Phụ lục.
- For Nhóm A files (6-col Severity present): replace ONLY the table lines (header +
  separator + data rows). Commentary blockquotes around the table stay intact.
- For Nhóm B files (no Severity table): insert a new Severity breakdown block right
  before `## Bug Summary Table` heading.
- For Nhóm C-safe files (Severity unknown/multi-row but BST counts are clean): same
  as Nhóm A — replace the entire table block (header + separator + ALL data rows)
  with 1-row 8-col.
- Skip Nhóm C-unsafe (count discrepancy in BST), Nhóm X (no BST), Nhóm D (already OK).

Modes:
    --dry-run (default)   Print per-file diff to stdout. No writes.
    --apply               Write changes in-place.
    --filter A|B|C-safe   Limit to a classification subset (can repeat).
    --file <path>         Limit to specific file(s) (can repeat).
    --show-diff N         Show full unified diff for first N files (default: 3 in dry-run).

Usage:
    python3 .claude/scripts/migrate-severity-8col.py output/qa-reports/round7-2026-05-06/bug-reports/
    python3 .claude/scripts/migrate-severity-8col.py --apply --filter A output/qa-reports/round7-2026-05-06/bug-reports/

Exit: 0 success, 1 if any file errored.
"""
from __future__ import annotations

import argparse
import difflib
import sys
from pathlib import Path

HOOKS_DIR = Path(__file__).resolve().parent.parent / "hooks"
sys.path.insert(0, str(HOOKS_DIR))
from bug_report_parser import parse_bug_report  # noqa: E402

SCRIPTS_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPTS_DIR))
# Reuse file-walking utilities from verifier
import importlib.util as _ilu

_spec = _ilu.spec_from_file_location("verify_bug_reports", SCRIPTS_DIR / "verify-bug-reports.py")
_verify_mod = _ilu.module_from_spec(_spec)
_spec.loader.exec_module(_verify_mod)  # type: ignore[union-attr]
collect_files = _verify_mod.collect_files
is_bug_report_file = _verify_mod.is_bug_report_file


# -----------------------------------------------------------------------------
# Table rendering
# -----------------------------------------------------------------------------


def render_8col_table(total: int, critical: int, major: int, medium: int, minor: int, trivial: int, closed: int, open_: int) -> list[str]:
    """Return lines (no trailing newlines) for the 8-col Severity table."""
    return [
        "| Tổng | Critical | Major | Medium | Minor | Trivial | Closed | Open |",
        "|------|----------|-------|--------|-------|---------|--------|------|",
        f"| {total:<4} | {critical:<8} | {major:<5} | {medium:<6} | {minor:<5} | {trivial:<7} | {closed:<6} | {open_:<4} |",
    ]


def counts_from_parse(parsed: dict) -> tuple[int, int, int, int, int, int, int, int]:
    """Extract (total, critical, major, medium, minor, trivial, closed, open) from BST counts.

    `Open` column aggregates Open + Defer + Withdrawn (active work not yet Closed).
    """
    sc = parsed["bst"]["severity_counts"]
    c = parsed["bst"]["counts"]
    return (
        c["total"],
        sc["critical"],
        sc["major"],
        sc["medium"],
        sc["minor"],
        sc["trivial"],
        c["closed"],
        c["open"] + c["defer"] + c["withdrawn"],
    )


# -----------------------------------------------------------------------------
# Block locators (operate on list of lines, no trailing \n)
# -----------------------------------------------------------------------------


def find_severity_heading_idx(lines: list[str]) -> int:
    for i, ln in enumerate(lines):
        if ln.strip().lower().startswith("### severity breakdown"):
            return i
    return -1


def find_bst_heading_idx(lines: list[str]) -> int:
    for i, ln in enumerate(lines):
        s = ln.strip().lower()
        if s.startswith("## bug summary table") or s == "## bug summary":
            return i
    return -1


def find_table_block_after(lines: list[str], start_idx: int) -> tuple[int, int] | None:
    """Find the first markdown table starting at/after start_idx.

    Returns (first_table_line_idx, one_past_last_table_line_idx) or None.
    Stops scanning if 20 non-blank non-table lines are seen first.
    """
    i = start_idx
    seen_non_blank = 0
    while i < len(lines):
        ln = lines[i].strip()
        if not ln:
            i += 1
            continue
        if ln.startswith("|") and ln.endswith("|"):
            # Found start
            start = i
            j = i
            while j < len(lines):
                lj = lines[j].rstrip()
                if lj.strip().startswith("|") and lj.strip().endswith("|"):
                    j += 1
                else:
                    break
            return (start, j)
        seen_non_blank += 1
        if seen_non_blank > 20:
            return None
        i += 1
    return None


# -----------------------------------------------------------------------------
# Migration operations
# -----------------------------------------------------------------------------


def migrate_replace_table(content: str, parsed: dict) -> tuple[str, str]:
    """Nhóm A + C-safe: replace existing Severity table block with new 8-col.

    Returns (new_content, action_description).
    """
    lines = content.split("\n")
    sev_idx = find_severity_heading_idx(lines)
    if sev_idx < 0:
        return (content, "ERROR: no '### Severity breakdown' heading found")
    block = find_table_block_after(lines, sev_idx + 1)
    if block is None:
        return (content, "ERROR: no table found after '### Severity breakdown'")
    start, end = block
    new_table = render_8col_table(*counts_from_parse(parsed))
    new_lines = lines[:start] + new_table + lines[end:]
    return ("\n".join(new_lines), f"replaced Severity table lines {start + 1}-{end} with 8-col 1-row")


SEVERITY_BLOCK_TEMPLATE = """### Severity breakdown

{table}

> **Quy tắc đếm:**
> - `Tổng` = tổng số dòng bug trong **Bug Summary Table** (kể cả Closed strikethrough).
> - 5 cột severity (Critical / Major / Medium / Minor / Trivial) tổng = `Tổng`.
> - `Closed` + `Open` = `Tổng`. `Closed` đếm Status ∈ {{Closed, ~~closed~~}}; `Open` đếm phần còn lại (Open, Reopen, Defer, Withdrawn — mọi bug chưa đóng).
> - Update bảng này **sau MỖI lần đóng/mở bug** (cùng nhịp với rename Pass- prefix)."""


def migrate_insert_table(content: str, parsed: dict) -> tuple[str, str]:
    """Nhóm B: insert new Severity table block before `## Bug Summary Table` heading.

    Returns (new_content, action_description). Ensures exactly 1 blank line before
    and 1 blank line after the inserted block (no double-blank).
    """
    lines = content.split("\n")
    bst_idx = find_bst_heading_idx(lines)
    if bst_idx < 0:
        return (content, "ERROR: no '## Bug Summary Table' heading found — cannot determine insert position")
    new_table = render_8col_table(*counts_from_parse(parsed))
    block_text = SEVERITY_BLOCK_TEMPLATE.format(table="\n".join(new_table))
    block_lines = block_text.split("\n")
    # Strip back any existing blank lines before BST heading — we'll re-add exactly 1
    insert_at = bst_idx
    while insert_at > 0 and lines[insert_at - 1].strip() == "":
        insert_at -= 1
    new_lines = (
        lines[:insert_at]
        + [""]
        + block_lines
        + [""]
        + lines[bst_idx:]
    )
    return ("\n".join(new_lines), f"inserted Severity block before line {bst_idx + 1} (BST heading)")


# -----------------------------------------------------------------------------
# Classification per file
# -----------------------------------------------------------------------------

C_SAFE_BST_CLEAN_THRESHOLDS = {
    "severity_sum_matches_total": True,
    "closed_plus_open_matches_total": True,
    "no_status_unknown": True,
    "no_severity_unknown": True,
}


def _bst_is_clean(parsed: dict) -> bool:
    """A BST is 'clean' when its rows can be summarised into the 8-col Severity
    table without losing rows: severity_sum == total, closed+open == total, no
    unknown severity or status rows."""
    cons = parsed["consistency"]
    counts = parsed["bst"]["counts"]
    sev_counts = parsed["bst"]["severity_counts"]
    return (
        cons.get("severity_sum_matches_total") is True
        and cons.get("closed_plus_open_matches_total") is True
        and counts.get("unknown", 0) == 0
        and sev_counts.get("unknown", 0) == 0
    )


def reclassify(parsed: dict) -> str:
    """Return one of: A, B, C-safe, C-unsafe, D, X.

    For Nhóm B (no Severity table), we additionally require the BST to be 'clean':
    if a BUG row has non-standard severity (e.g. `Question`) or non-standard status,
    we cannot synthesise a correct 8-col Severity table from it — the row must be
    fixed manually first. Demote such files to C-unsafe so they hit the manual queue.
    """
    cls = parsed["classification"]
    if cls in ("A", "D", "X"):
        return cls
    if cls == "B":
        return "B" if _bst_is_clean(parsed) else "C-unsafe"
    # cls == C: split based on BST cleanliness
    return "C-safe" if _bst_is_clean(parsed) else "C-unsafe"


# -----------------------------------------------------------------------------
# Per-file driver
# -----------------------------------------------------------------------------


def process_file(filepath: Path, apply: bool, want_diff: bool) -> dict:
    """Run migration on a single file. Returns result dict."""
    result = {
        "filepath": str(filepath),
        "classification": "?",
        "action": "skipped",
        "diff": None,
        "error": None,
    }
    try:
        parsed = parse_bug_report(filepath)
    except Exception as e:  # noqa: BLE001
        result["error"] = f"parse error: {e}"
        return result
    if parsed.get("error"):
        result["error"] = parsed["error"]
        return result
    cls = reclassify(parsed)
    result["classification"] = cls

    if cls == "D":
        result["action"] = "skip (already 8-col + consistent)"
        return result
    if cls == "X":
        result["action"] = "skip (no BST — Nhóm X requires manual special handling)"
        return result
    if cls == "C-unsafe":
        result["action"] = "skip (Nhóm C-unsafe — count discrepancy needs manual fix)"
        return result

    content = filepath.read_text(encoding="utf-8")
    if cls in ("A", "C-safe"):
        new_content, action = migrate_replace_table(content, parsed)
    elif cls == "B":
        new_content, action = migrate_insert_table(content, parsed)
    else:
        result["action"] = f"skip (unknown class {cls})"
        return result

    if action.startswith("ERROR"):
        result["error"] = action
        return result

    if new_content == content:
        result["action"] = f"no-op ({action})"
        return result

    result["action"] = action

    if want_diff:
        result["diff"] = "".join(
            difflib.unified_diff(
                content.splitlines(keepends=True),
                new_content.splitlines(keepends=True),
                fromfile=str(filepath) + " (current)",
                tofile=str(filepath) + " (new)",
                n=2,
            )
        )

    if apply:
        filepath.write_text(new_content, encoding="utf-8")
        result["action"] = "WROTE — " + result["action"]

    return result


# -----------------------------------------------------------------------------
# CLI
# -----------------------------------------------------------------------------


def main(argv: list[str]) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("targets", nargs="+", help="Files or folders")
    ap.add_argument("--apply", action="store_true", help="Write changes in-place (default: dry-run only)")
    ap.add_argument(
        "--filter",
        action="append",
        choices=["A", "B", "C-safe", "C-unsafe", "X", "D"],
        help="Only process files of this classification (repeatable)",
    )
    ap.add_argument("--show-diff", type=int, default=3, help="Show full diff for first N migrated files (default 3)")
    ap.add_argument("--quiet", action="store_true", help="Only show summary, no per-file lines")
    args = ap.parse_args(argv[1:])

    files = collect_files(args.targets)
    if not files:
        print("No bug-report files matched.", file=sys.stderr)
        return 1

    results: list[dict] = []
    diff_shown = 0
    error_count = 0
    for f in files:
        # Pre-classify quickly to honor --filter without full processing
        parsed_pre = parse_bug_report(f)
        cls_pre = reclassify(parsed_pre)
        if args.filter and cls_pre not in args.filter:
            results.append({"filepath": str(f), "classification": cls_pre, "action": "filtered out", "error": None})
            continue
        want_diff = diff_shown < args.show_diff and cls_pre in ("A", "B", "C-safe")
        r = process_file(f, apply=args.apply, want_diff=want_diff)
        if r.get("error"):
            error_count += 1
        if r.get("diff"):
            diff_shown += 1
            if not args.quiet:
                print(f"\n----- DIFF: {r['filepath']} [{r['classification']}] -----")
                print(r["diff"])
        results.append(r)

    # Summary
    by_cls: dict[str, list[dict]] = {}
    for r in results:
        by_cls.setdefault(r["classification"], []).append(r)

    print("\n" + "=" * 80)
    print("MIGRATION SUMMARY" + (" (DRY-RUN)" if not args.apply else " (APPLIED)"))
    print("=" * 80)
    for cls in ["A", "B", "C-safe", "C-unsafe", "D", "X", "?"]:
        if cls not in by_cls:
            continue
        rows = by_cls[cls]
        actioned = [r for r in rows if r["action"] not in ("filtered out", "no-op", "")
                    and not r["action"].startswith("skip")
                    and not r["action"].startswith("no-op")]
        errors = [r for r in rows if r.get("error")]
        skipped = [r for r in rows if r["action"].startswith("skip") or r["action"].startswith("no-op")]
        filtered = [r for r in rows if r["action"] == "filtered out"]
        print(f"  {cls:<10} {len(rows):>3} files | actioned={len(actioned)} skipped={len(skipped)} errors={len(errors)} filtered={len(filtered)}")
    print(f"\nTotal files: {len(results)}; errors: {error_count}")
    if not args.apply:
        print("\nDRY-RUN — no files were modified. Re-run with --apply to commit changes.")
    return 0 if error_count == 0 else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv))
