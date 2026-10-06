#!/usr/bin/env python3
"""Ghi cột Verify (round reverify tuần 3) — Sheet 1, tab "UAT_TGPL Doanh Nghiệp-tuần 3".

Hai chế độ (theo yêu cầu reverify):
  --pass   : bug hết lỗi → CHỈ ghi Verify = "Pass". KHÔNG đụng P (Trạng thái dev fix 1) / R.
  --reopen : bug còn lỗi → P = "Reopen", Verify = "Reopen", R (DEV phản hồi lần 1) = --note (OVERWRITE).

Guard:
  1. Spreadsheet id + tab title khớp hằng số.
  2. Dò cột theo TÊN header (Mã TC / Trạng thái dev fix 1 / Verify / DEV phản hồi lần 1).
  3. D{row} (Mã TC) phải == --ma-tc, lệch -> DỪNG.
  4. In old -> new mỗi ô ghi.
  5. Đọc lại sau ghi, không khớp -> exit != 0.

  python3 sheet_verify_write.py --row 303 --ma-tc XNTGHTVV_OOS_01 --pass [--dry-run]
  python3 sheet_verify_write.py --row 7 --ma-tc PDHSVV_02 --reopen --note "..." [--dry-run]
"""
import argparse, os, sys, time, warnings
from datetime import datetime
warnings.filterwarnings("ignore")

SPREADSHEET_ID = "1OKBN2otlmdZ44THkmhtsn-_63M2Boh7zQwearwjYR3s"
TAB_NAME = "UAT_TGPL Doanh Nghiệp-tuần 3"
# --- Tab override (thêm 2026-07-27 cho đợt tuần 4) ---------------------------
# Guard gốc: TAB_NAME hardcode để không ghi nhầm tab. Đợt tuần 4 cần tab khác ->
# cho override QUA ENV `UAT_TAB` nhưng chỉ chấp nhận tên nằm trong ALLOWED_TABS
# (vẫn là hằng số hardcode). Không set env -> giữ nguyên default.
_ALLOWED_TABS = {
    "UAT_TGPL Doanh Nghiệp-tuần 1",
    "UAT_TGPL Doanh Nghiệp-tuần 2",
    "UAT_TGPL Doanh Nghiệp-tuần 3",
    "UAT_TGPL Doanh Nghiệp-tuần 4",
}
_env_tab = os.environ.get("UAT_TAB", "").strip()
if _env_tab:
    if _env_tab not in _ALLOWED_TABS:
        raise SystemExit(f"\u274c DUNG (guard): UAT_TAB={_env_tab!r} khong nam trong ALLOWED_TABS {_ALLOWED_TABS}")
    TAB_NAME = _env_tab
# -----------------------------------------------------------------------------
SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]
HERE = os.path.dirname(os.path.abspath(__file__))
LOG = os.path.join(HERE, "sheet_verify_write.log")


def col_letter(idx0):
    s = ""
    n = idx0
    while True:
        s = chr(ord("A") + n % 26) + s
        n = n // 26 - 1
        if n < 0:
            break
    return s


def get_ws():
    import gspread
    from google.oauth2.credentials import Credentials
    from google.auth.transport.requests import Request
    token = os.path.join(HERE, "token.json")
    creds = Credentials.from_authorized_user_file(token, SCOPES)
    if creds and creds.expired and creds.refresh_token:
        creds.refresh(Request())
        with open(token, "w") as f:
            f.write(creds.to_json())
    gc = gspread.authorize(creds)
    sh = gc.open_by_key(SPREADSHEET_ID)
    ws = sh.worksheet(TAB_NAME)
    return ws


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--row", type=int, required=True)
    ap.add_argument("--ma-tc", required=True)
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--pass", dest="is_pass", action="store_true")
    g.add_argument("--reopen", dest="is_reopen", action="store_true")
    ap.add_argument("--note", default="")
    ap.add_argument("--note-file", default="",
                    help="Đọc note từ file (an toàn cho note nhiều dòng — tránh vỡ quoting shell)")
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()

    if a.note_file:
        with open(a.note_file, encoding="utf-8") as f:
            a.note = f.read().strip()
    if a.is_reopen and not a.note.strip():
        sys.exit("DỪNG: --reopen bắt buộc có --note / --note-file (mô tả lỗi đang thấy).")

    ws = get_ws()
    header = ws.row_values(1)

    def find(name):
        for i, h in enumerate(header):
            if h.strip() == name:
                return i
        sys.exit(f"DỪNG: không thấy cột header '{name}'")

    ci_matc = find("Mã TC")
    ci_p = find("Trạng thái dev fix 1")
    ci_q = find("Verify")
    ci_r = find("DEV phản hồi lần 1")
    D = col_letter(ci_matc); P = col_letter(ci_p); Q = col_letter(ci_q); R = col_letter(ci_r)

    row = a.row
    got = ws.batch_get([f"{D}{row}", f"{P}{row}", f"{Q}{row}", f"{R}{row}"])
    def gv(x): return (x[0][0] if x and x[0] else "").strip()
    cur_matc, cur_p, cur_q, cur_r = gv(got[0]), gv(got[1]), gv(got[2]), gv(got[3])

    if cur_matc != a.ma_tc:
        sys.exit(f"DỪNG: {D}{row}='{cur_matc}' != --ma-tc '{a.ma_tc}'")

    writes = []  # (cell, old, new)
    if a.is_pass:
        writes.append((f"{Q}{row}", cur_q, "Pass"))
    else:  # reopen
        writes.append((f"{P}{row}", cur_p, "Reopen"))
        writes.append((f"{Q}{row}", cur_q, "Reopen"))
        writes.append((f"{R}{row}", cur_r, a.note))

    print(f"Tab: {TAB_NAME} | D={D} P={P} Verify={Q} R={R} | row {row} Mã TC='{cur_matc}' ✓")
    for cell, old, new in writes:
        print(f"  {cell}: '{old[:40]}' -> '{new[:40]}'")

    if a.dry_run:
        print("[dry-run] không ghi."); return

    body = [{"range": cell, "values": [[new]]} for cell, _, new in writes]
    for attempt in range(5):
        try:
            ws.batch_update(body, value_input_option="RAW"); break
        except Exception as e:
            if attempt == 4: raise
            w = 2 ** attempt; print(f"  APIError -> retry {w}s"); time.sleep(w)

    time.sleep(1)
    back = ws.batch_get([cell for cell, _, _ in writes])
    stamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    bad = []
    with open(LOG, "a") as f:
        f.write(f"\n=== {stamp} — row {row} {a.ma_tc} ({'PASS' if a.is_pass else 'REOPEN'}) ===\n")
        for i, (cell, old, new) in enumerate(writes):
            now = (back[i][0][0] if back[i] else "").strip()
            ok = now == new
            if not ok: bad.append(f"  {cell}: đọc lại='{now}' != '{new}'")
            f.write(f"{cell}\told='{old}'\tnew='{now}'\t{'OK' if ok else 'FAIL'}\n")
            print(f"  {'✅' if ok else '❌'} {cell} -> '{now[:40]}'")
    if bad:
        print("\n❌ Đọc lại KHÔNG khớp:"); print("\n".join(bad)); sys.exit(3)
    print(f"\n✅ Ghi xong {len(writes)} ô. Log: {LOG}")


if __name__ == "__main__":
    main()
