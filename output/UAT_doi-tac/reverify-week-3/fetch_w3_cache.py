#!/usr/bin/env python3
"""READ-ONLY: tải 2 sheet (DRIVE tuần 3 + ĐỐI TÁC gộp) về JSON cache.
Không ghi bất cứ thứ gì lên Google Sheets. Chỉ dùng .get_all_values() +
fetch_sheet_metadata(includeGridData) để lấy hyperlink cột Ảnh/vieo 1.
"""
import os, json, warnings
warnings.filterwarnings("ignore")

HERE = "/Users/huongttt/Downloads/antigravity/PM HTPLDN/skilkk/output/UAT_doi-tac/tools"
OUT = os.path.dirname(os.path.abspath(__file__))
SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]

DRIVE_ID = "1OKBN2otlmdZ44THkmhtsn-_63M2Boh7zQwearwjYR3s"
DRIVE_TAB = "UAT_TGPL Doanh Nghiệp-tuần 3"
PARTNER_ID = "1dJat1cc68-TNuX_ibzBK-0NcgOWvPLu6aioiEgeUa5c"
PARTNER_TAB = "UAT_TGPL Doanh Nghiệp"
PARTNER_GID = 799081340


def client():
    import gspread
    from google.oauth2.credentials import Credentials
    from google.auth.transport.requests import Request
    token = os.path.join(HERE, "token.json")
    creds = Credentials.from_authorized_user_file(token, SCOPES)
    if creds and creds.expired and creds.refresh_token:
        creds.refresh(Request())
        with open(token, "w") as f:
            f.write(creds.to_json())
    return gspread.authorize(creds)


def main():
    gc = client()

    # ---------- DRIVE ----------
    sh_d = gc.open_by_key(DRIVE_ID)
    print("DRIVE tabs:", [w.title for w in sh_d.worksheets()])
    ws_d = sh_d.worksheet(DRIVE_TAB)
    drive_vals = ws_d.get_all_values()
    print(f"DRIVE '{DRIVE_TAB}' rows={len(drive_vals)} cols={len(drive_vals[0]) if drive_vals else 0}")

    # ---------- PARTNER ----------
    sh_p = gc.open_by_key(PARTNER_ID)
    print("PARTNER tabs:", [(w.title, w.id) for w in sh_p.worksheets()])
    ws_p = None
    for w in sh_p.worksheets():
        if w.id == PARTNER_GID:
            ws_p = w
            break
    if ws_p is None:
        ws_p = sh_p.worksheet(PARTNER_TAB)
    print(f"PARTNER chosen tab: {ws_p.title!r} gid={ws_p.id}")
    partner_vals = ws_p.get_all_values()
    print(f"PARTNER rows={len(partner_vals)} cols={len(partner_vals[0]) if partner_vals else 0}")

    # ---------- PARTNER hyperlinks (grid data) ----------
    # Lấy toàn bộ grid của tab đối tác, trích link từ hyperlink /
    # userEnteredFormat.textFormat.link.uri / textFormatRuns.
    hdr_p = partner_vals[0]
    ci_anh = None
    for i, h in enumerate(hdr_p):
        if h.strip().lower().startswith("ảnh/vieo 1") or h.strip().lower().startswith("ảnh/video 1"):
            ci_anh = i
            break
    print("PARTNER 'Ảnh/vieo 1' col index =", ci_anh)
    a1col = ""
    n = ci_anh if ci_anh is not None else 0
    while True:
        a1col = chr(ord("A") + n % 26) + a1col
        n = n // 26 - 1
        if n < 0:
            break
    rng = f"'{ws_p.title}'!{a1col}1:{a1col}{len(partner_vals)}"
    print("grid range:", rng)
    meta = sh_p.fetch_sheet_metadata({
        "includeGridData": "true",
        "ranges": rng,
    })
    links = {}   # "r,c" -> uri
    sheets = meta.get("sheets", [])
    if sheets:
        data = sheets[0].get("data", [])
        if data:
            r0 = data[0].get("startRow", 0)
            c0 = data[0].get("startColumn", 0)
            for _ri, row in enumerate(data[0].get("rowData", [])):
                ri = _ri + r0
                for _ci, cell in enumerate(row.get("values", []) or []):
                    ci = _ci + c0
                    uri = cell.get("hyperlink")
                    if not uri:
                        uri = (cell.get("userEnteredFormat", {})
                                   .get("textFormat", {}).get("link", {}).get("uri"))
                    if not uri:
                        for run in cell.get("textFormatRuns", []) or []:
                            u = run.get("format", {}).get("link", {}).get("uri")
                            if u:
                                uri = u
                                break
                    if uri:
                        links[f"{ri},{ci}"] = uri
    print(f"PARTNER hyperlinks found: {len(links)}")

    with open(os.path.join(OUT, "cache_w3.json"), "w") as f:
        json.dump({
            "drive_tab": DRIVE_TAB,
            "drive": drive_vals,
            "partner_tab": ws_p.title,
            "partner_gid": ws_p.id,
            "partner": partner_vals,
            "partner_links": links,
        }, f, ensure_ascii=False)
    print("cache written ->", os.path.join(OUT, "cache_w3.json"))

    print("\n=== DRIVE HEADER ===")
    for i, h in enumerate(drive_vals[0]):
        print(f"  [{i}] {h!r}")
    print("\n=== PARTNER HEADER ===")
    for i, h in enumerate(partner_vals[0]):
        print(f"  [{i}] {h!r}")


if __name__ == "__main__":
    main()
