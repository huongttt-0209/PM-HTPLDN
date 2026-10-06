#!/usr/bin/env python3
"""
sheet_auth.py — Tạo token.json 1 lần cho sheet_write.py (OAuth Desktop app).

Cần: 1 file OAuth client secret (kiểu "Desktop app") tải từ Google Cloud Console.
  Google Cloud Console > APIs & Services > Credentials > Create Credentials
    > OAuth client ID > Application type: Desktop app > Download JSON.
  (Nhớ Enable "Google Sheets API" cho project trước.)

Chạy (nên chạy trực tiếp trong terminal để mở được trình duyệt đăng nhập):
  python3 tools/sheet_auth.py --client /duong/dan/client_secret.json
  # hoặc đặt file tại tools/credentials.json rồi chạy:  python3 tools/sheet_auth.py

Sau khi đăng nhập + đồng ý → ghi tools/token.json. sheet_write.py sẽ tự dùng file này.
"""
import argparse, os, sys, warnings
warnings.filterwarnings("ignore")

SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]
HERE = os.path.dirname(os.path.abspath(__file__))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--client", default=os.path.join(HERE, "credentials.json"),
                    help="OAuth Desktop client secret JSON (default: tools/credentials.json)")
    ap.add_argument("--out", default=os.path.join(HERE, "token.json"))
    args = ap.parse_args()

    if not os.path.exists(args.client):
        print(f"❌ Không thấy client secret: {args.client}", file=sys.stderr)
        print("   Tải OAuth 'Desktop app' JSON từ Google Cloud Console rồi truyền --client.", file=sys.stderr)
        sys.exit(2)

    from google_auth_oauthlib.flow import InstalledAppFlow
    flow = InstalledAppFlow.from_client_secrets_file(args.client, SCOPES)
    creds = flow.run_local_server(port=0)  # mở trình duyệt để đăng nhập + đồng ý
    with open(args.out, "w") as f:
        f.write(creds.to_json())
    print(f"✅ Đã tạo token: {args.out}")
    print("   Giờ có thể chạy sheet_write.py (tự dùng token này).")


if __name__ == "__main__":
    main()
