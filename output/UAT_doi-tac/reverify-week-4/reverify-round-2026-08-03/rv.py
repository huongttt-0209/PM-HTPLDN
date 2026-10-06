#!/usr/bin/env python3
"""rv.py — helper re-verify vòng 2 (đợt 03/08/2026).

Mỗi case: sinh Bảng đối chiếu điều kiện (cond/<MA>.md) rồi gọi sheet_write.py --mode reverify2.
- Pass       -> ghi X (Verify 2) = Pass. KHÔNG đụng W/Y.
- Reopen     -> ghi W (Trạng thái dev fix 2) = Reopen + X = Reopen + Y (DEV phản hồi lần 2) = note.
- BA confirm -> ghi X = BA confirm + Y = câu hỏi gửi BA. KHÔNG đụng W (lỗi gốc dev đã xử lý thật;
                chỗ vướng là kỳ vọng của đối tác chưa khớp đặc tả).

Dùng:
  python3 rv.py --ma-tc SLHDVM_06 --tab 3 --row 191 --verdict Pass \
      --evidence evidence/SLHDVM_06.log \
      --cond "Vai trò|cbnv_tw (CB_NV_TW, Toàn quốc)|cbnv_tw (CB_NV_TW, Toàn quốc)" \
      --cond "Loại báo cáo|BC Số lượng hỏi đáp/vướng mắc pháp luật|BC Số lượng hỏi đáp/vướng mắc pháp luật" \
      [--note-file note.txt]   # bắt buộc khi Reopen
"""
import argparse, os, subprocess, sys

HERE = os.path.dirname(os.path.abspath(__file__))
TOOLS = os.path.abspath(os.path.join(HERE, "..", "..", "tools"))
TABS = {"2": "UAT_TGPL Doanh Nghiệp-tuần 2", "3": "UAT_TGPL Doanh Nghiệp-tuần 3"}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--ma-tc", required=True)
    ap.add_argument("--tab", required=True, choices=["2", "3"])
    ap.add_argument("--row", required=True, type=int)
    ap.add_argument("--verdict", required=True, choices=["Pass", "Reopen", "BA confirm"])
    ap.add_argument("--evidence", required=True)
    ap.add_argument("--cond", action="append", required=True,
                    help='"Điều kiện|Bug gốc|Mình test" — GAP tự điền "Không"')
    ap.add_argument("--note-file")
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()

    ev = a.evidence if os.path.isabs(a.evidence) else os.path.join(HERE, a.evidence)
    if not os.path.exists(ev) or os.path.getsize(ev) == 0:
        sys.exit(f"❌ evidence không tồn tại/rỗng: {ev}")

    cond_path = os.path.join(HERE, "cond", f"{a.ma_tc}.md")
    lines = [f"# Bảng đối chiếu điều kiện — {a.ma_tc} (re-verify vòng 2, 03/08/2026)", "",
             "| Điều kiện | Bug gốc (vòng 2) | Mình test | GAP? |",
             "|---|---|---|---|"]
    for c in a.cond:
        parts = [p.strip() for p in c.split("|")]
        if len(parts) != 3:
            sys.exit(f"❌ --cond phải có đúng 3 phần 'Điều kiện|Bug gốc|Mình test': {c!r}")
        lines.append(f"| {parts[0]} | {parts[1]} | {parts[2]} | Không |")
    lines.append("")
    with open(cond_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))

    cmd = [sys.executable, os.path.join(TOOLS, "sheet_write.py"),
           "--mode", "reverify2", "--row", str(a.row), "--ma-tc", a.ma_tc,
           "--status", a.verdict, "--evidence", ev, "--condition-table", cond_path]
    if a.verdict != "Pass":
        if not a.note_file:
            sys.exit(f"❌ {a.verdict} bắt buộc --note-file (ghi cột 'DEV phản hồi lần 2').")
        nf = a.note_file if os.path.isabs(a.note_file) else os.path.join(HERE, a.note_file)
        cmd += ["--note-file", nf]
    if a.dry_run:
        cmd.append("--dry-run")

    env = dict(os.environ, UAT_TAB=TABS[a.tab])
    print("→", " ".join(cmd))
    sys.exit(subprocess.call(cmd, env=env, cwd=TOOLS))


if __name__ == "__main__":
    main()
