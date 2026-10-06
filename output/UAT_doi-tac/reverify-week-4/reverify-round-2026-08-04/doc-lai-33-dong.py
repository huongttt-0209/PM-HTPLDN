#!/usr/bin/env python3
"""Đọc lại 33 dòng vừa ghi, đối chiếu với kế hoạch + bản sao lưu trước khi ghi.

Chỉ ĐỌC, không ghi. Gọi 2 lần đọc (mỗi tab 1 lần) để không đụng quota.
Chạy: python3 reverify-week-4/reverify-round-2026-08-04/doc-lai-33-dong.py
"""
import json
import os
import sys

TOOLS = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "tools")
SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]


def get_client():
    """Dùng chung token.json với sheet_write.py — chỉ đọc, không ghi."""
    import gspread
    from google.oauth2.credentials import Credentials
    from google.auth.transport.requests import Request

    token = os.path.join(TOOLS, "token.json")
    creds = Credentials.from_authorized_user_file(token, SCOPES)
    if creds and creds.expired and creds.refresh_token:
        creds.refresh(Request())
        with open(token, "w") as f:
            f.write(creds.to_json())
    return gspread.authorize(creds)


SHEET_ID = "1OKBN2otlmdZ44THkmhtsn-_63M2Boh7zQwearwjYR3s"
T2 = "UAT_TGPL Doanh Nghiệp-tuần 2"
T3 = "UAT_TGPL Doanh Nghiệp-tuần 3"

# (tab, dòng, Mã TC, verdict mong đợi, bộ cột)  — bộ 1 = vòng 1 (P/Q/R), bộ 2 = vòng 2 (W/X/Y)
PLAN = [
    (T2, 116, "KTDGKQHT_02",       "Open",   1),
    (T2, 120, "PDKHDTTH_04",       "Reject", 1),
    (T2, 122, "DKTGMLTVV_04",      "Reject", 1),
    (T2, 123, "DKTGMLTVV_05",      "Open",   1),
    (T2, 125, "QLLSHTCTVV_03",     "Open",   1),
    (T2, 126, "QLLSHTCTVV_04",     "Open",   1),
    (T2, 127, "NHSYC_01",          "Open",   1),
    (T2, 135, "QLDXDTTH_11",       "Open",   1),
    (T2, 145, "TKHSYCHTPL_OOS_01", "Open",   1),
    (T3, 331, "QLDMTCTV_OOS_05",   "Open",   1),
    (T3, 332, "QLDMTCTV_OOS_06",   "Reject", 1),
    (T3, 339, "QLDMTCTV_OOS_13",   "Open",   1),
]
PDF_ROWS = [
    (192, "SLHDVM_07"), (197, "VVDTN_07"), (204, "VVDHT_07"), (210, "VVDHTHT_07"),
    (217, "VVTTG_06"), (223, "CLDTBDDDR_07"), (228, "LDTBDDDR_07"), (231, "CGTVPL_07"),
    (234, "DGHQHTPL_07"), (240, "VVTDVQL_07"), (244, "VVTLV_06"), (247, "VVTLHDN_06"),
    (249, "VVTTGCT_06"), (251, "CPHTCT_07"), (254, "CPCTHTTDVQL_07"), (258, "CPCTHTTLHDN_07"),
    (261, "CPCTHTTTG_06"), (265, "SLCTHT_07"), (269, "CTTDVQL_05"), (274, "CTTLV_06"),
    (276, "CTTTG_05"),
]
PLAN += [(T3, r, ma, "Reopen", 2) for r, ma in PDF_ROWS]

HDR_R1 = ("Trạng thái dev fix 1", "Verify", "DEV phản hồi lần 1")
HDR_R2 = ("Trạng thái dev fix 2", "Verify 2", "DEV phản hồi lần 2")

BACKUP = os.path.join(os.path.dirname(__file__), "..", "..",
                      "reverify-audit", "BACKUP-33-dong-truoc-baapply-2026-08-04.json")


def col_of(header_row, name):
    for i, h in enumerate(header_row):
        if h.strip() == name:
            return i
    raise SystemExit(f"❌ Không tìm thấy cột tên '{name}'")


def main():
    gc = get_client()
    sh = gc.open_by_key(SHEET_ID)
    grids = {}
    for tab in (T2, T3):
        grids[tab] = sh.worksheet(tab).get_all_values()
        print(f"📥 Đọc xong tab '{tab}' — {len(grids[tab])} dòng")

    backup = {}
    if os.path.exists(BACKUP):
        with open(BACKUP, encoding="utf-8") as f:
            raw = json.load(f)
        for tab_name, rows in raw.get("data", {}).items():
            for row_str, item in rows.items():
                backup[(tab_name, int(row_str))] = item

    ok = bad = 0
    print("\n{:<8} {:>5} {:<20} {:<8} {:<10} {:<10} {:>7}  {}".format(
        "Tab", "Dòng", "Mã TC", "Mong đợi", "Cột trạng thái", "Cột Verify", "Ghi chú", "Kết luận"))
    print("─" * 118)
    for tab, row, ma, want, band in PLAN:
        grid = grids[tab]
        hdr = grid[0]
        names = HDR_R1 if band == 1 else HDR_R2
        c_ma = col_of(hdr, "Mã TC")
        c_p, c_q, c_r = (col_of(hdr, n) for n in names)
        line = grid[row - 1]

        def cell(i):
            return line[i].strip() if i < len(line) else ""

        got_ma, got_p, got_q, got_r = cell(c_ma), cell(c_p), cell(c_q), cell(c_r)
        # Cột "Trạng thái dev fix" là Ô CỦA DEV, không phải của QA (protocol §1) — dev sửa
        # realtime nên giá trị hiện tại có thể khác lúc QA ghi. Chỉ ghi nhận, KHÔNG tính lệch.
        # Tiêu chí đạt = cột Verify (ô của QA) đúng verdict + note không rỗng + Mã TC khớp.
        problems = []
        if got_ma != ma:
            problems.append(f"Mã TC lệch: '{got_ma}'")
        if got_q != want:
            problems.append(f"{names[1]}='{got_q}' ≠ '{want}'")
        if not got_r:
            problems.append(f"{names[2]} RỖNG")
        real = problems
        tag = "✅" if not real else "❌"
        if real:
            bad += 1
        else:
            ok += 1
        old_p = backup.get((tab, row), {}).get(names[0])
        note = ""
        if got_p != want:
            note = f"ô dev = '{got_p}'" + (f" (sao lưu: '{old_p}')" if old_p and old_p != got_p else "")
        print("{:<8} {:>5} {:<20} {:<8} {:<14} {:<12} {:>7}  {} {}".format(
            "tuần 2" if tab == T2 else "tuần 3", row, ma, want,
            got_p[:14], got_q[:12], f"{len(got_r)} kt", tag, "· ".join(real) or note))

    print("─" * 118)
    print(f"KẾT QUẢ ĐỌC LẠI: {ok}/{len(PLAN)} khớp kế hoạch · {bad} lệch")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
