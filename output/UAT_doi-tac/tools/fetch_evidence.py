#!/usr/bin/env python3
"""
fetch_evidence.py — Lấy bằng chứng đối tác gắn ở cột "Ảnh/vieo 1" (hyperlink Drive) về máy.

VÌ SAO CÓ SCRIPT NÀY (chống lặp lỗi 2026-07-10):
  Evidence đối tác nằm ở cột M dưới dạng HYPERLINK Google Drive. gspread `get_all_values()`
  CHỈ trả text hiển thị ("QLKTLBG_02.jpg") và GIẤU link → dễ tưởng "không có evidence" khi
  ngó folder local không thấy file. Script này trích link qua Sheets REST API rồi tải về, để
  bước locate evidence thành CƠ HỌC — không còn chỗ suy đoán "thiếu".

KẾT CỤC (chỉ 2):
  • Tải được file → in đường dẫn local (mở xem full-res tới khoảnh khắc lỗi rồi mới verify).
  • Cột M dòng N RỖNG (không text + không link) → in "RỖNG" + exit 3 → đây MỚI thật sự là
    không có evidence → verdict TRỐNG + hỏi user. KHÔNG được verify bằng text.

Dùng:
  python3 tools/fetch_evidence.py --row 8
  python3 tools/fetch_evidence.py --row 8 --out-dir reverify-week-2/partner-evidence
  python3 tools/fetch_evidence.py --row 8 --col-header "Ảnh/video 2"   # evidence vòng 2 (cột T)

Auth: tái dùng tools/token.json (OAuth, scope spreadsheets) — như sheet_write.py.
"""
import argparse, os, re, sys, json, warnings, urllib.parse, urllib.request
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
    # 2026-08-05: tab tổng hợp "bug" (gid=1714340219). Script này CHỈ ĐỌC (tải evidence về máy)
    # nên allowlist ở đây không mang rủi ro ghi nhầm tab — guard gốc viết cho script GHI.
    "bug",
}
_env_tab = os.environ.get("UAT_TAB", "").strip()
if _env_tab:
    if _env_tab not in _ALLOWED_TABS:
        raise SystemExit(f"\u274c DUNG (guard): UAT_TAB={_env_tab!r} khong nam trong ALLOWED_TABS {_ALLOWED_TABS}")
    TAB_NAME = _env_tab
# -----------------------------------------------------------------------------
COL_EVIDENCE_HEADER = "Ảnh/vieo 1"   # cột M (evidence vòng đầu). Vòng 2 = "Ảnh/video 2" (cột T).
COL_MATC_HEADER = "Mã TC"
SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]
HERE = os.path.dirname(os.path.abspath(__file__))


def die(msg, code=2):
    print(f"❌ {msg}", file=sys.stderr)
    sys.exit(code)


def col_letter(idx0):
    """0-based column index -> A1 letter (A, B, ... Z, AA...)."""
    s = ""
    n = idx0 + 1
    while n > 0:
        n, r = divmod(n - 1, 26)
        s = chr(65 + r) + s
    return s


def load_creds(token_path):
    from google.oauth2.credentials import Credentials
    from google.auth.transport.requests import Request
    if not os.path.exists(token_path):
        die(f"Không có token: {token_path}. Chạy tools/sheet_auth.py để tạo.")
    creds = Credentials.from_authorized_user_file(token_path, SCOPES)
    if creds and creds.expired and creds.refresh_token:
        creds.refresh(Request())
        with open(token_path, "w") as f:
            f.write(creds.to_json())
    if not creds or not creds.token:
        die("Token không hợp lệ / không refresh được.")
    return creds


def get_cell(creds, col, row):
    """Trả (formattedValue, [urls]) của ô {col}{row} — gồm cả hyperlink whole-cell lẫn link
    nhúng từng đoạn text (textFormatRuns)."""
    rng = f"{TAB_NAME}!{col}{row}"
    # Link đối tác gắn theo 3 kiểu khác nhau tuỳ ô — phải bắt CẢ 3:
    #   (a) hyperlink whole-cell (ô jpg)  (b) textFormatRuns[].format.link (link 1 đoạn text)
    #   (c) chipRuns[].chip.richLinkProperties.uri (smart chip Drive — ô webm)
    fields = "sheets.data.rowData.values(formattedValue,hyperlink,textFormatRuns,chipRuns)"
    url = (f"https://sheets.googleapis.com/v4/spreadsheets/{SPREADSHEET_ID}"
           f"?ranges={urllib.parse.quote(rng)}&includeGridData=true"
           f"&fields={urllib.parse.quote(fields)}")
    req = urllib.request.Request(url, headers={"Authorization": f"Bearer {creds.token}"})
    with urllib.request.urlopen(req, timeout=30) as r:
        data = json.load(r)
    try:
        cell = data["sheets"][0]["data"][0]["rowData"][0]["values"][0]
    except (KeyError, IndexError):
        return "", []
    text = (cell.get("formattedValue") or "").strip()
    urls = []
    if cell.get("hyperlink"):
        urls.append(cell["hyperlink"])
    for run in cell.get("textFormatRuns", []) or []:
        uri = (run.get("format", {}) or {}).get("link", {}).get("uri")
        if uri:
            urls.append(uri)
    for run in cell.get("chipRuns", []) or []:
        uri = (run.get("chip", {}) or {}).get("richLinkProperties", {}).get("uri")
        if uri:
            urls.append(uri)
    # dedup giữ thứ tự
    seen, out = set(), []
    for u in urls:
        if u not in seen:
            seen.add(u); out.append(u)
    return text, out


def drive_id(url):
    for pat in (r"/file/d/([A-Za-z0-9_-]{20,})",
                r"[?&]id=([A-Za-z0-9_-]{20,})",
                r"/d/([A-Za-z0-9_-]{20,})"):
        m = re.search(pat, url)
        if m:
            return m.group(1)
    return None


def download(url, dest):
    """Tải file Drive (hoặc URL trực tiếp) về dest. Trả (ok, note)."""
    fid = drive_id(url)
    dl = f"https://drive.google.com/uc?export=download&id={fid}" if fid else url
    req = urllib.request.Request(dl, headers={"User-Agent": "Mozilla/5.0 fetch-evidence"})
    with urllib.request.urlopen(req, timeout=60) as r:
        ctype = (r.headers.get("Content-Type") or "").lower()
        body = r.read()
    if body[:15].lstrip().lower().startswith(b"<!doctype") or b"text/html" in ctype.encode():
        # Drive interstitial (file lớn / cần confirm) — thử confirm token
        m = re.search(rb'confirm=([0-9A-Za-z_-]+)', body)
        if fid and m:
            dl2 = f"https://drive.google.com/uc?export=download&confirm={m.group(1).decode()}&id={fid}"
            req2 = urllib.request.Request(dl2, headers={"User-Agent": "Mozilla/5.0 fetch-evidence"})
            with urllib.request.urlopen(req2, timeout=120) as r2:
                body = r2.read()
        else:
            return False, "Drive trả HTML (interstitial) — có thể file lớn/không public. Kiểm tra quyền chia sẻ."
    with open(dest, "wb") as f:
        f.write(body)
    return True, f"{len(body)} bytes"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--row", type=int, required=True, help="Số dòng sheet (1-based, gồm header)")
    ap.add_argument("--col-header", default=COL_EVIDENCE_HEADER,
                    help=f'Header cột evidence (default "{COL_EVIDENCE_HEADER}")')
    ap.add_argument("--out-dir", default=os.path.join(os.getcwd(), "partner-evidence"),
                    help="Thư mục lưu (default ./partner-evidence)")
    ap.add_argument("--token", default=os.path.join(HERE, "token.json"))
    args = ap.parse_args()

    creds = load_creds(args.token)

    import gspread
    from google.oauth2.credentials import Credentials
    gc = gspread.authorize(Credentials.from_authorized_user_file(args.token, SCOPES))
    ws = gc.open_by_key(SPREADSHEET_ID).worksheet(TAB_NAME)
    header = ws.row_values(1)
    if args.col_header not in header:
        die(f"Không thấy cột '{args.col_header}'. Header: {header}")
    col = col_letter(header.index(args.col_header))
    ma_tc = ""
    if COL_MATC_HEADER in header:
        rowvals = ws.row_values(args.row)
        di = header.index(COL_MATC_HEADER)
        ma_tc = rowvals[di].strip() if di < len(rowvals) else ""

    print("─" * 60)
    print(f"Row {args.row} | Cột '{args.col_header}' ({col}{args.row}) | Mã TC: {ma_tc or '?'}")
    text, urls = get_cell(creds, col, args.row)
    print(f"Text hiển thị: {text or '(trống)'}")
    print(f"Link Drive tìm thấy: {len(urls)}")

    if not text and not urls:
        print("─" * 60)
        print("🟥 RỖNG — cột evidence không có text lẫn link. ĐÂY mới là 'không có evidence'.")
        print("   → Verdict để TRỐNG + hỏi user. KHÔNG verify bằng text.")
        sys.exit(3)

    if not urls:
        print("─" * 60)
        print(f"⚠️  Có text '{text}' nhưng KHÔNG trích được link Drive trong ô.")
        print("   → Mở sheet tay kiểm tra ô này; có thể link gắn kiểu khác. CHƯA đóng được Cổng 1.")
        sys.exit(4)

    os.makedirs(args.out_dir, exist_ok=True)
    ok_any = False
    for i, u in enumerate(urls):
        # Ô nhiều dòng (vd "TKM phản hồi lần 1" = câu chú thích + xuống dòng + tên tệp):
        # chỉ lấy ĐOẠN cuối cùng trông giống tên tệp, rồi khử ký tự phá đường dẫn.
        # (2026-08-06: không khử -> `TKM retest 31/7: ...\nX_v2.jpg` thành thư mục con "7:" -> FileNotFoundError)
        name_from_text = ""
        for line in reversed((text or "").splitlines()):
            line = line.strip()
            if re.search(r"\.(jpg|jpeg|png|gif|webm|mp4|mov)$", line, re.I):
                name_from_text = re.split(r"[\\/]", line)[-1].strip()
                break
        base = name_from_text or f"{ma_tc or ('row' + str(args.row))}-evidence-{i+1}"
        base = re.sub(r'[\x00-\x1f<>:"|?*]', "_", base).strip() or f"row{args.row}-evidence-{i+1}"
        if len(urls) > 1 and re.search(r"\.\w+$", base):
            stem, ext = os.path.splitext(base)
            base = f"{stem}-{i+1}{ext}"
        if not re.search(r"\.\w+$", base):
            base += ".jpg"
        dest = os.path.join(args.out_dir, base)
        ok, note = download(u, dest)
        if ok:
            ok_any = True
            print(f"  ✅ [{i+1}] {u[:60]}… → {dest}  ({note})")
        else:
            print(f"  ❌ [{i+1}] {u[:60]}… → {note}")
    print("─" * 60)
    if ok_any:
        print(f"📁 Đã tải về {args.out_dir}. → MỞ XEM full-res tới khoảnh khắc lỗi rồi mới verify.")
        sys.exit(0)
    sys.exit(5)


if __name__ == "__main__":
    main()
