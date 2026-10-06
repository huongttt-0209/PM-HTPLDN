#!/usr/bin/env python3
"""finish.py — đóng 1 case re-verify vòng 2: dựng evidence -> ghi sheet -> cập nhật report md.

Chạy SAU khi đã thao tác trên web và (với case xuất file) đã lưu response body của
POST /bao-cao/export bằng get_network_request --responseFilePath.

VD (case Pass, có file xuất):
  python3 finish.py --ma-tc SLHDVM_07 --tab 3 --row 192 --verdict Pass \
     --title "BC Số lượng hỏi đáp — Xuất PDF" \
     --claim 'TKM retest 31/7: hệ thống hiển thị thông báo "Forbidden"' \
     --expect "Hệ thống tạo tệp PDF ... tải về máy" \
     --steps "Báo cáo thống kê -> Loại BC = ... -> Kỳ Năm -> Xem báo cáo -> Xuất PDF -> Xuất file (A4/Dọc)" \
     --obs "POST /bao-cao/export -> 200, content-type application/pdf" \
     --obs "Toast: chỉ 'Đang tạo file...', không có 'Forbidden'" \
     --file evidence/SLHDVM_07-bao-cao-hoi-dap.pdf \
     --conclusion "Không tái hiện Forbidden, file đúng nội dung -> Pass" \
     --cond "Vai trò|cbnv_tw|cbnv_tw"  ...
"""
import argparse, datetime, os, re, subprocess, sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPORT = os.path.join(HERE, "KET-QUA-REVERIFY-VONG-2.md")
ICON = {"Pass": "✅", "Reopen": "❌", "BA confirm": "⚠️"}


def read_file_summary(path):
    """Đọc nội dung file xuất (xlsx/pdf) trả về list dòng tóm tắt để nhét vào evidence."""
    out = []
    ap = path if os.path.isabs(path) else os.path.join(HERE, path)
    if not os.path.exists(ap):
        return [f"(khong doc duoc: {path} khong ton tai)"]
    size = os.path.getsize(ap)
    out.append(f"FILE: {os.path.basename(ap)} — {size} bytes")
    if ap.lower().endswith((".xlsx", ".xls")):
        import openpyxl
        wb = openpyxl.load_workbook(ap)
        for ws in wb.worksheets:
            out.append(f"  [sheet] {ws.title} ({ws.max_row}x{ws.max_column})")
            for i, row in enumerate(ws.iter_rows(values_only=True), 1):
                vals = [str(c) for c in row if c is not None and str(c).strip()]
                if vals:
                    out.append(f"    r{i}: " + " | ".join(vals))
    elif ap.lower().endswith(".pdf"):
        import fitz
        d = fitz.open(ap)
        out.append(f"  PDF {d.page_count} trang | kho giay pt: {d[0].rect} (A4 = 595x842)")
        out.append(f"  FONTS: {sorted({f[3] for p in d for f in p.get_fonts(full=True)})}")
        for i in range(d.page_count):
            out.append(f"  --- trang {i+1} ---")
            for ln in d[i].get_text().splitlines():
                if ln.strip():
                    out.append("    " + ln)
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--ma-tc", required=True)
    ap.add_argument("--tab", required=True, choices=["2", "3"])
    ap.add_argument("--row", required=True, type=int)
    ap.add_argument("--verdict", required=True, choices=["Pass", "Reopen", "BA confirm"])
    ap.add_argument("--title", required=True, help="Tên chức năng ngắn cho bảng")
    ap.add_argument("--claim", required=True, help="Lý do reopen của TKM")
    ap.add_argument("--expect", required=True, help="KQ mong đợi (rút gọn)")
    ap.add_argument("--steps", required=True)
    ap.add_argument("--obs", action="append", required=True, help="mỗi -obs 1 quan sát")
    ap.add_argument("--file", action="append", default=[], help="file xuất cần đọc nội dung")
    ap.add_argument("--conclusion", required=True)
    ap.add_argument("--note-short", required=True, help="ghi chú ≤12 từ cho Bảng 1")
    ap.add_argument("--cond", action="append", required=True)
    ap.add_argument("--note-file", help="note cột Y — bắt buộc khi Reopen")
    ap.add_argument("--why", help="Bảng 2: vì sao chưa xong (Reopen / BA confirm)")
    ap.add_argument("--todo", help="Bảng 2: cần làm gì (Reopen)")
    ap.add_argument("--who", help="Bảng 2: ai làm (Reopen)")
    ap.add_argument("--account", default="cbnv_tw / CB_NV_TW Toan quoc",
                    help="tai khoan da dung — doi khi case chay bang role khac (vd admin / QTHT)")
    ap.add_argument("--skip-sheet", action="store_true")
    a = ap.parse_args()

    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")

    # ---------- 1. evidence ----------
    ev_path = os.path.join(HERE, "evidence", f"{a.ma_tc}.log")
    L = [f"RE-VERIFY {a.ma_tc} — {now} (build HTPLDN V1.0.4, tai khoan {a.account})",
         f"Moi truong: https://htpldn-uat.ospgroup.vn  |  Cong cu: Chrome DevTools MCP (UI-driven)", "",
         f"CLAIM VONG 2 (TKM): {a.claim}",
         f"KQ MONG DOI      : {a.expect}", "",
         f"LUONG DA CHAY LAI: {a.steps}", "", "QUAN SAT:"]
    L += [f"  - {o}" for o in a.obs]
    for f in a.file:
        L += ["", "NOI DUNG FILE XUAT:"] + read_file_summary(f)
    L += ["", f"KET LUAN: {a.conclusion}", f"VERDICT : {a.verdict}"]
    with open(ev_path, "w", encoding="utf-8") as fh:
        fh.write("\n".join(L) + "\n")
    print(f"✅ evidence: {ev_path} ({os.path.getsize(ev_path)} bytes)")

    # ---------- 2. ghi sheet ----------
    if not a.skip_sheet:
        cmd = [sys.executable, os.path.join(HERE, "rv.py"), "--ma-tc", a.ma_tc, "--tab", a.tab,
               "--row", str(a.row), "--verdict", a.verdict, "--evidence", ev_path]
        for c in a.cond:
            cmd += ["--cond", c]
        if a.verdict != "Pass":
            if not a.note_file:
                sys.exit(f"❌ {a.verdict} bắt buộc --note-file")
            cmd += ["--note-file", a.note_file]
        rc = subprocess.call(cmd)
        if rc != 0:
            sys.exit(f"❌ ghi sheet THẤT BẠI (rc={rc}) — KHÔNG cập nhật report để tránh lệch.")

    # ---------- 3. cap nhat report md ----------
    txt = open(REPORT, encoding="utf-8").read()
    icon = ICON[a.verdict]

    # 3a. them dong vao Bang 1
    m = re.search(r"(\n\*\*Tiến độ:\*\*)", txt)
    tbl1 = txt[:m.start()]
    n = len(re.findall(r"^\| \d+ \| ", tbl1, re.M)) + 1
    row = (f"| {n} | {a.ma_tc} | T{a.tab} · {a.row} | {a.title} | {icon} {a.verdict} | {a.note_short} |\n")
    txt = txt[:m.start()] + row + txt[m.start():]

    # 3b. cap nhat dong Tien do
    def bump(mm):
        tot = len(re.findall(r"^\| \d+ \| ", txt.split("**Tiến độ:**")[0], re.M))
        p = len(re.findall(r"\| ✅ Pass \|", txt))
        r = len(re.findall(r"\| ❌ Reopen \|", txt))
        b = len(re.findall(r"\| ⚠️ BA confirm \|", txt))
        return f"**Tiến độ:** {tot}/54 · ✅ Pass {p} · ❌ Reopen {r} · ⚠️ BA confirm {b}"
    txt = re.sub(r"\*\*Tiến độ:\*\*[^\n]*", bump, txt, count=1)

    # 3c. Bang 2 (chi khi Reopen)
    if a.verdict != "Pass":
        b2 = "## Bảng 2 — Case chưa xong / còn lỗi\n"
        if "_(chưa có case Reopen)_" in txt:
            txt = txt.replace("_(chưa có case Reopen)_",
                              "| Mã TC | Vì sao | Cần làm gì | Ai làm |\n|---|---|---|---|")
        i = txt.index(b2) + len(b2)
        j = txt.index("\n---", i)
        txt = txt[:j] + f"\n| {a.ma_tc} | {a.why or ''} | {a.todo or ''} | {a.who or 'Dev'} |" + txt[j:]

    # 3d. chi tiet case
    obs_md = "\n".join(f"- {o}" for o in a.obs)
    files_md = " · ".join(f"[{os.path.basename(f)}]({f})" for f in a.file)
    detail = f"""
### {n}. {icon} {a.ma_tc} — {a.title} (T{a.tab} dòng {a.row})

**Claim vòng 2 (TKM):** {a.claim}
**KQ mong đợi:** {a.expect}

**Luồng đã chạy lại:** {a.steps}

**Quan sát:**
{obs_md}

**Kết luận:** {a.conclusion} → **{a.verdict}**
**Bằng chứng:** [evidence/{a.ma_tc}.log](evidence/{a.ma_tc}.log){' · ' + files_md if files_md else ''} · [bảng điều kiện](cond/{a.ma_tc}.md)
**Sheet:** tuần {a.tab} dòng {a.row} → { {'Pass': '`Verify 2` = `Pass`', 'Reopen': '`Trạng thái dev fix 2` = `Reopen` · `Verify 2` = `Reopen` · `DEV phản hồi lần 2` = mô tả lỗi', 'BA confirm': '`Verify 2` = `BA confirm` · `DEV phản hồi lần 2` = câu hỏi gửi BA (KHÔNG đụng `Trạng thái dev fix 2`)'}[a.verdict] } {icon}
"""
    txt = txt.rstrip() + "\n" + detail
    with open(REPORT, "w", encoding="utf-8") as fh:
        fh.write(txt)
    print(f"✅ report cập nhật: case #{n} {a.ma_tc} = {a.verdict}")


if __name__ == "__main__":
    main()
