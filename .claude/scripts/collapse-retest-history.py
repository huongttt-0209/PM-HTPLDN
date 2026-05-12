#!/usr/bin/env python3
"""Migration: collapse retest history blockquotes trong bug-report-*.md.

Mỗi bug entry chỉ giữ DUY NHẤT 1 blockquote `> **Re-(verify|test) ...` latest
theo max timestamp `YYYY-MM-DD HH:MM[:SS]`. Các blockquote cũ bị xoá toàn bộ
(kể cả continuation lines `> - ...` / `>` / `> {detail}`).

Portable cho mọi QA clone repo:
  - Shebang `#!/usr/bin/env python3` (không hardcode python path)
  - Internal refs qua `Path(__file__).resolve().parents[2]` = project root
  - Accept path arg relative-to-cwd hoặc absolute

Usage:
  python3 .claude/scripts/collapse-retest-history.py --dry-run <file_or_dir>
  python3 .claude/scripts/collapse-retest-history.py --write <file_or_dir>
  python3 .claude/scripts/collapse-retest-history.py --dry-run --recursive output/qa-reports/

Flags:
  --dry-run    Print diff preview, KHÔNG ghi file (default behavior nếu thiếu --write).
  --write      Ghi file thực tế. Tạo `.bak` backup cùng folder trước khi overwrite.
  --recursive  Recurse vào thư mục, match `**/bug-reports/**/(Pass-)?bug-report-*.md`.
  --quiet      Chỉ in summary, không in diff per-file.

Exit codes:
  0  — không có drift (hoặc --dry-run thành công với drift)
  1  — có error (invalid path, parse fail, write fail)
"""
from __future__ import annotations

import argparse
import difflib
import re
import sys
from datetime import datetime
from pathlib import Path
from typing import Iterable

TARGET_RE = re.compile(r"bug-report-[^/]+\.md$", re.IGNORECASE)
EXCLUDE_RE = re.compile(r"(^|/)(node_modules|\.git|\.bak)/")

# Bug entry boundary: `^## (~~)?(\*\*)?BUG-` h2 heading
BUG_HEADING_RE = re.compile(r"^## (?:~~)?(?:\*\*)?BUG-", re.MULTILINE)

# Retest blockquote first-line: `^> \*\*Re-(verify|test)`
RETEST_FIRST_LINE_RE = re.compile(
    r"^>\s+\*\*Re-(?:verify|test)\b", re.IGNORECASE
)

# Timestamp `YYYY-MM-DD HH:MM[:SS]` (space hoặc 'T' separator)
TIMESTAMP_RE = re.compile(
    r"(\d{4}-\d{2}-\d{2})[ T](\d{2}:\d{2}(?::\d{2})?)"
)

# Markdown image ref `![alt](path)` — extract from deleted blocks for stderr report
IMAGE_REF_RE = re.compile(r"!\[([^\]]*)\]\(([^)]+)\)")


def parse_timestamp(ts: str) -> datetime | None:
    """Parse `YYYY-MM-DD HH:MM` hoặc `YYYY-MM-DD HH:MM:SS`. Return None nếu invalid."""
    m = TIMESTAMP_RE.search(ts)
    if not m:
        return None
    date_part, time_part = m.group(1), m.group(2)
    fmt = "%Y-%m-%d %H:%M:%S" if time_part.count(":") == 2 else "%Y-%m-%d %H:%M"
    try:
        return datetime.strptime(f"{date_part} {time_part}", fmt)
    except ValueError:
        return None


def is_blockquote_line(line: str) -> bool:
    """Line thuộc blockquote group: bắt đầu `>` (có thể `> `, `>`, `> - ...`, `> > ...`)."""
    return line.startswith(">")


def find_retest_blocks(lines: list[str], start: int, end: int) -> list[tuple[int, int]]:
    """Tìm các retest block trong slice lines[start:end].

    Returns list of (block_start_idx, block_end_idx_exclusive) — indices relative to `lines`.

    Block = từ dòng `> **Re-(verify|test)` đến trước:
      - Dòng `> **Re-(verify|test)` kế tiếp, HOẶC
      - Dòng KHÔNG bắt đầu `>` (kết thúc blockquote group).
    """
    blocks: list[tuple[int, int]] = []
    i = start
    while i < end:
        if RETEST_FIRST_LINE_RE.match(lines[i]):
            block_start = i
            j = i + 1
            while j < end:
                if RETEST_FIRST_LINE_RE.match(lines[j]):
                    break
                if not is_blockquote_line(lines[j]):
                    break
                j += 1
            blocks.append((block_start, j))
            i = j
        else:
            i += 1
    return blocks


def block_timestamp(lines: list[str], block_start: int, block_end: int) -> datetime | None:
    """Parse timestamp từ dòng đầu block (Re-test/verify line)."""
    return parse_timestamp(lines[block_start])


def find_bug_boundaries(lines: list[str]) -> list[tuple[int, int]]:
    """Split file thành bug entries.

    Returns [(bug_start_line_idx, bug_end_line_idx_exclusive), ...].
    Bug start = dòng `^## (~~)?BUG-`. Bug end = dòng `## BUG-` kế tiếp hoặc EOF.
    """
    bug_starts: list[int] = []
    for i, line in enumerate(lines):
        if BUG_HEADING_RE.match(line):
            bug_starts.append(i)
    if not bug_starts:
        return []
    boundaries: list[tuple[int, int]] = []
    for k, start in enumerate(bug_starts):
        end = bug_starts[k + 1] if k + 1 < len(bug_starts) else len(lines)
        boundaries.append((start, end))
    return boundaries


def collapse_file_content(content: str) -> tuple[str, list[dict]]:
    """Collapse retest history trong content. Return (new_content, report).

    report = list of dict per-bug-with-collapse:
      {"bug_heading": str, "kept_ts": str, "dropped_count": int, "dropped_images": [str]}
    """
    lines = content.splitlines(keepends=False)
    boundaries = find_bug_boundaries(lines)
    if not boundaries:
        return content, []

    drop_indices: set[int] = set()
    report: list[dict] = []

    for bug_start, bug_end in boundaries:
        blocks = find_retest_blocks(lines, bug_start, bug_end)
        if len(blocks) <= 1:
            continue

        timestamps = [block_timestamp(lines, bs, be) for bs, be in blocks]
        if all(ts is None for ts in timestamps):
            continue

        # Pick block with max timestamp; ties → pick last (assume file order = recency).
        keep_idx = -1
        keep_ts: datetime | None = None
        for k, ts in enumerate(timestamps):
            if ts is None:
                continue
            if keep_ts is None or ts >= keep_ts:
                keep_ts = ts
                keep_idx = k

        if keep_idx < 0:
            continue

        dropped_images: list[str] = []
        dropped_count = 0
        for k, (bs, be) in enumerate(blocks):
            if k == keep_idx:
                continue
            dropped_count += 1
            for ln in range(bs, be):
                drop_indices.add(ln)
                for m in IMAGE_REF_RE.finditer(lines[ln]):
                    dropped_images.append(f"![{m.group(1)}]({m.group(2)})")

        report.append({
            "bug_heading": lines[bug_start].strip(),
            "kept_ts": keep_ts.strftime("%Y-%m-%d %H:%M:%S") if keep_ts else "?",
            "dropped_count": dropped_count,
            "dropped_images": dropped_images,
        })

    if not drop_indices:
        return content, report

    # Drop selected lines + collapse adjacent blank `>` continuation orphans.
    new_lines: list[str] = []
    for i, line in enumerate(lines):
        if i in drop_indices:
            continue
        new_lines.append(line)

    # Preserve trailing newline if original had one.
    new_content = "\n".join(new_lines)
    if content.endswith("\n") and not new_content.endswith("\n"):
        new_content += "\n"

    return new_content, report


def iter_target_files(target: Path, recursive: bool) -> Iterable[Path]:
    """Yield file paths khớp TARGET_RE."""
    if target.is_file():
        if TARGET_RE.search(target.name) and not EXCLUDE_RE.search(str(target)):
            yield target
        return
    if not target.is_dir():
        return
    if recursive:
        for p in target.rglob("*.md"):
            if TARGET_RE.search(p.name) and not EXCLUDE_RE.search(str(p)):
                yield p
    else:
        for p in target.iterdir():
            if p.is_file() and TARGET_RE.search(p.name) and not EXCLUDE_RE.search(str(p)):
                yield p


def write_with_backup(path: Path, new_content: str) -> Path:
    """Write atomic: temp file + rename. Tạo `.bak` backup trước khi overwrite."""
    backup = path.with_suffix(path.suffix + ".bak")
    backup.write_text(path.read_text(encoding="utf-8"), encoding="utf-8")
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_text(new_content, encoding="utf-8")
    tmp.replace(path)
    return backup


def print_diff(path: Path, old: str, new: str, quiet: bool) -> None:
    if quiet:
        return
    diff = difflib.unified_diff(
        old.splitlines(keepends=True),
        new.splitlines(keepends=True),
        fromfile=f"{path} (before)",
        tofile=f"{path} (after)",
        n=2,
    )
    sys.stdout.writelines(diff)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("target", help="File hoặc thư mục bug-report")
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--dry-run", action="store_true", help="Preview diff, không ghi (default)")
    mode.add_argument("--write", action="store_true", help="Ghi file + tạo .bak backup")
    parser.add_argument("--recursive", "-r", action="store_true", help="Recurse vào thư mục")
    parser.add_argument("--quiet", "-q", action="store_true", help="Chỉ in summary, không in diff")
    args = parser.parse_args(argv)

    if not args.write:
        args.dry_run = True  # default

    target = Path(args.target).resolve()
    if not target.exists():
        print(f"ERROR: path không tồn tại: {target}", file=sys.stderr)
        return 1

    files = list(iter_target_files(target, args.recursive))
    if not files:
        print(f"INFO: không tìm thấy file match `bug-report-*.md` trong {target}", file=sys.stderr)
        return 0

    total_files = 0
    total_drift = 0
    total_dropped_blocks = 0
    total_dropped_images: list[tuple[Path, str]] = []

    for f in sorted(files):
        try:
            content = f.read_text(encoding="utf-8")
        except Exception as e:  # noqa: BLE001
            print(f"ERROR read {f}: {e}", file=sys.stderr)
            continue
        total_files += 1

        new_content, report = collapse_file_content(content)
        if not report or new_content == content:
            continue

        total_drift += 1
        for r in report:
            total_dropped_blocks += r["dropped_count"]
            for img in r["dropped_images"]:
                total_dropped_images.append((f, img))

        rel = f.relative_to(Path.cwd()) if str(f).startswith(str(Path.cwd())) else f
        print(f"\n=== {rel} ===", file=sys.stderr)
        for r in report:
            print(
                f"  bug: {r['bug_heading'][:80]}",
                file=sys.stderr,
            )
            print(
                f"    kept latest: {r['kept_ts']} | dropped {r['dropped_count']} block(s)",
                file=sys.stderr,
            )
            if r["dropped_images"]:
                print(
                    f"    [WARN] images in dropped blocks (manual migrate nếu cần):",
                    file=sys.stderr,
                )
                for img in r["dropped_images"]:
                    print(f"      - {img}", file=sys.stderr)

        if args.write:
            backup = write_with_backup(f, new_content)
            print(f"  WRITE → {f.name} (.bak → {backup.name})", file=sys.stderr)
        else:
            print_diff(f, content, new_content, args.quiet)

    mode_label = "WRITE" if args.write else "DRY-RUN"
    print(
        f"\n[{mode_label}] scanned={total_files} drift={total_drift} dropped_blocks={total_dropped_blocks} dropped_images={len(total_dropped_images)}",
        file=sys.stderr,
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
