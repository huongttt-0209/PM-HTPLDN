#!/usr/bin/env python3
"""Đồng bộ dòng `### Severity breakdown` theo `## Bug Summary Table` — nguyên tử, 1 lệnh.

VÌ SAO CẦN: hook `check-bug-report-severity-sync.py` (PreToolUse:Edit) đòi 2 bảng khớp nhau ở
state SAU mỗi Edit. Thêm 1 bug bằng 2 Edit riêng → state trung gian lệch → BLOCK cả hai chiều
(sửa bảng nào trước cũng bị chặn). Script này ghi bằng Bash (không trigger PreToolUse:Edit) và
ghi CẢ dòng tổng trong một lần, nên thoát được thế kẹt đó mà không cần nới hook.

KHÔNG bịa số: dòng Severity luôn được TÍNH LẠI từ các dòng thật của Bug Summary Table, và BST
phải khớp 1-1 với các heading bug entry trong file. Lệch → TỪ CHỐI ghi, in ra lệch ở đâu.
Nhờ vậy "hai bảng khớp nhau" không thể là khớp nhau ở một con số sai.

Cách dùng:
    python3 .claude/scripts/sync-bug-report-tables.py <file|thư mục>...            # chỉ kiểm (mặc định)
    python3 .claude/scripts/sync-bug-report-tables.py --write <file|thư mục>...    # ghi thật

Mã thoát: 0 = mọi file OK/đã ghi · 1 = có file lệch (chế độ kiểm) · 2 = từ chối ghi vì dữ liệu chưa nhất quán.
"""
from __future__ import annotations

import argparse
import os
import re
import sys
import tempfile
from pathlib import Path

HOOKS_DIR = Path(__file__).resolve().parent.parent / "hooks"
sys.path.insert(0, str(HOOKS_DIR))
from bug_report_parser import (  # noqa: E402
    SEVERITY_HEADING_RE,
    _find_table_after,
    _split_table_row,
    compute_consistency,
    parse_bst,
    parse_severity_table,
)

# Heading của một bug entry: h2..h4 có chứa mã BUG-…  (loại trừ heading của chính 2 bảng)
ENTRY_HEADING_RE = re.compile(r"^#{2,4}[ \t]+(?P<text>.*\bBUG-[A-Za-z0-9_.\-]+.*)$", re.MULTILINE)
BUG_ID_RE = re.compile(r"BUG-[A-Za-z0-9_.\-]+")
SKIP_PATH_PARTS = ("/image/", "/_archive/", "/screenshots/", "/img/")


def _norm_id(s: str) -> str:
    """Lấy đúng mã BUG-… trong ô, bỏ chú thích kèm theo (`~~`, `(R9)`, `**`…)."""
    found = BUG_ID_RE.search(s)
    return (found.group(0) if found else s.strip()).rstrip("~*`.,;:").upper()


def entry_ids(content: str) -> list[str]:
    """Mã bug lấy từ heading của các entry (không phải từ bảng)."""
    out = []
    for m in ENTRY_HEADING_RE.finditer(content):
        found = BUG_ID_RE.search(m.group("text"))
        if found:
            out.append(_norm_id(found.group(0)))
    return out


def wanted_values(sev_fmt: str, bst: dict) -> list[int]:
    c = bst["counts"]
    s = bst["severity_counts"]
    vals = [c["total"], s["critical"], s["major"], s["medium"], s["minor"], s["trivial"]]
    if sev_fmt == "8-col":
        vals += [c["closed"], c["open"] + c["defer"] + c["withdrawn"]]
    return vals


def build_row(header_cells: list[str], vals: list[int]) -> str:
    widths = [max(len(h), 1) for h in header_cells]
    cells = [f" {str(v):<{widths[i]}} " for i, v in enumerate(vals)]
    return "|" + "|".join(cells) + "|"


def process(path: Path, write: bool) -> tuple[str, str]:
    """Trả về (trạng thái, thông điệp). Trạng thái ∈ OK / FIXED / DIFF / REFUSE / SKIP."""
    content = path.read_text(encoding="utf-8")
    sev = parse_severity_table(content)
    bst = parse_bst(content)

    if not bst["present"]:
        return "SKIP", "không có Bug Summary Table"
    if not sev["present"]:
        return "SKIP", "không có bảng Severity breakdown (thêm tay trước đã)"
    if sev["format"] not in ("6-col", "8-col"):
        return "REFUSE", (
            f"Severity breakdown dùng định dạng lạ ({sev['format']}) — chỉ nhận đúng "
            "`Tổng|Critical|Major|Medium|Minor|Trivial[|Closed|Open]`. Sửa tiêu đề cột trước."
        )
    if sev["data_row_count"] != 1:
        return "REFUSE", f"Severity breakdown có {sev['data_row_count']} dòng dữ liệu, cần đúng 1"

    # Cổng chống "khớp nhau ở số sai": BST phải phản chiếu đúng các entry thật trong file.
    ids_bst = [_norm_id(r["bug_id"]) for r in bst["rows"]]
    ids_entry = entry_ids(content)
    only_bst = sorted(set(ids_bst) - set(ids_entry))
    only_entry = sorted(set(ids_entry) - set(ids_bst))
    dup_bst = sorted({i for i in ids_bst if ids_bst.count(i) > 1})
    if only_bst or only_entry or dup_bst:
        parts = []
        if only_bst:
            parts.append(f"có dòng bảng nhưng KHÔNG có entry: {', '.join(only_bst)}")
        if only_entry:
            parts.append(f"có entry nhưng KHÔNG có dòng bảng: {', '.join(only_entry)}")
        if dup_bst:
            parts.append(f"trùng mã trong bảng: {', '.join(dup_bst)}")
        return "REFUSE", "bảng và entry chưa khớp 1-1 → " + " · ".join(parts)

    unknown_sev = bst["severity_counts"]["unknown"]
    unknown_stat = bst["counts"]["unknown"]
    if unknown_sev or unknown_stat:
        return "REFUSE", (
            f"{unknown_sev} dòng không đọc được Severity, {unknown_stat} dòng không đọc được "
            "Status — sửa các ô đó rồi chạy lại"
        )

    offset, lines = _find_table_after(content, SEVERITY_HEADING_RE.search(content).end())
    header_cells = _split_table_row(lines[0])
    old_row = lines[2]
    vals = wanted_values(sev["format"], bst)
    new_row = build_row(header_cells, vals)

    # So SỐ chứ không so chuỗi — khác mỗi khoảng trắng canh cột thì không đụng vào file.
    keys = ["tong", "critical", "major", "medium", "minor", "trivial", "closed", "open"]
    cur = [sev["values"].get(k) for k in keys[: len(vals)]]
    if cur == vals:
        return "OK", "đã khớp"

    if not write:
        return "DIFF", f"cần đổi\n      cũ : {old_row}\n      mới: {new_row}"

    row_start = offset + len(lines[0]) + 1 + len(lines[1]) + 1
    updated = content[:row_start] + new_row + content[row_start + len(old_row):]

    # Ghi nguyên tử rồi tự kiểm lại; sai thì trả file về nguyên trạng.
    fd, tmp = tempfile.mkstemp(dir=str(path.parent), suffix=".tmp")
    with os.fdopen(fd, "w", encoding="utf-8") as fh:
        fh.write(updated)
    os.replace(tmp, path)

    check = compute_consistency(parse_severity_table(updated), parse_bst(updated))
    if check["severity_table_matches_bst"] is not True:
        path.write_text(content, encoding="utf-8")
        return "REFUSE", "ghi xong tự kiểm lại vẫn lệch → đã trả file về nguyên trạng"
    return "FIXED", f"{old_row.strip()}  →  {new_row.strip()}"


def collect(targets: list[str]) -> list[Path]:
    out: list[Path] = []
    for t in targets:
        p = Path(t)
        cands = sorted(p.rglob("*.md")) if p.is_dir() else [p]
        for c in cands:
            if any(part in str(c).replace("\\", "/") for part in SKIP_PATH_PARTS):
                continue
            out.append(c)
    return out


def main(argv: list[str]) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("targets", nargs="+", help="file .md hoặc thư mục")
    ap.add_argument("--write", action="store_true", help="ghi thật (mặc định chỉ kiểm)")
    ap.add_argument("-q", "--quiet", action="store_true", help="chỉ in file có vấn đề")
    args = ap.parse_args(argv)

    tally: dict[str, int] = {}
    worst = 0
    for path in collect(args.targets):
        try:
            status, msg = process(path, args.write)
        except Exception as exc:  # noqa: BLE001
            status, msg = "REFUSE", f"lỗi đọc/ghi: {exc}"
        tally[status] = tally.get(status, 0) + 1
        if status == "REFUSE":
            worst = max(worst, 2)
        elif status == "DIFF":
            worst = max(worst, 1)
        if args.quiet and status in ("OK", "SKIP"):
            continue
        print(f"[{status:6}] {path}\n      {msg}")

    print("\n" + " · ".join(f"{k}={v}" for k, v in sorted(tally.items())) or "không có file nào")
    return worst


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
