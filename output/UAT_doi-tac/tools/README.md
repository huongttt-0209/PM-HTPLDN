# tools/ — Ghi verdict + lấy evidence verify UAT (có guard)

3 script:
- `sheet_auth.py` — tạo `token.json` **1 lần** (OAuth Desktop, mở trình duyệt đăng nhập).
- `sheet_write.py` — ghi **đúng 2 ô** (`Trạng thái dev fix 1` + `DEV phản hồi lần 1`) cho 1 dòng, có 5 guard, đọc lại xác nhận.
- `fetch_evidence.py` — tải bằng chứng đối tác gắn ở **cột M** (hyperlink jpg/png + smart-chip Drive `.webm`) về `partner-evidence/`. **Chạy TRƯỚC khi verify mỗi case** (đóng Cổng 1): `python3 tools/fetch_evidence.py --row N`. `get_all_values()` giấu link nên "không thấy file local" ≠ "không có evidence" — chỉ khi script báo **RỖNG (exit 3)** mới thật sự không có → verdict TRỐNG. Vòng 2 dùng `--col-header "Ảnh/video 2"`.

## Bước 1 — Tạo OAuth Desktop client (làm 1 lần, trên Google Cloud Console)

1. Vào https://console.cloud.google.com/ → chọn (hoặc tạo mới) 1 **Project** ở thanh trên.
2. **Enable Google Sheets API:** mở https://console.cloud.google.com/apis/library/sheets.googleapis.com → bấm **Enable** (đảm bảo đúng project vừa chọn).
3. **OAuth consent screen** (nếu chưa cấu hình): APIs & Services → OAuth consent screen → User Type **External** → điền App name + email hỗ trợ + email nhà phát triển → Save. Ở mục **Test users / Audience** → **Add users** = chính email Google của bạn (để đăng nhập không bị chặn khi app đang ở chế độ Testing).
4. **Tạo credential:** APIs & Services → **Credentials** → **Create Credentials** → **OAuth client ID** → Application type: **Desktop app** → đặt tên bất kỳ → **Create** → **Download JSON**.
5. Lưu file JSON vừa tải thành: `output/UAT_doi-tac/tools/credentials.json`

## Bước 2 — Đăng nhập tạo token (chạy trực tiếp trong terminal để mở được trình duyệt)

```
python3 "output/UAT_doi-tac/tools/sheet_auth.py"
```
Trình duyệt mở → đăng nhập Google → nếu thấy cảnh báo "unverified app" thì bấm **Advanced → Go to … (unsafe)** → **Allow**.
Xong sẽ tạo `tools/token.json`.

## Bước 3 — Ghi (agent tự chạy)

```
# thử trước (không ghi):
python3 "output/UAT_doi-tac/tools/sheet_write.py" --row 2 --ma-tc DKTGKH_07 --status "Reject" --note "..." --dry-run
# ghi thật (chỉ 2 ô, đọc lại xác nhận):
python3 "output/UAT_doi-tac/tools/sheet_write.py" --row 2 --ma-tc DKTGKH_07 --status "Reject" --note "..."
```

## Guard trong sheet_write.py
1. Spreadsheet ID + tên tab khớp hằng số hardcode.
2. Dò cột theo TÊN header (`Trạng thái dev fix 1` / `DEV phản hồi lần 1`) — sheet đổi layout vẫn đúng ô.
3. `D{row}` (Mã TC) phải == `--ma-tc`, lệch → DỪNG.
4. Chỉ set 2 ô, in old→new.
5. Đọc lại sau ghi, không khớp → báo lỗi.

> `credentials.json` và `token.json` là bí mật cá nhân — KHÔNG commit (đã đưa vào .gitignore của thư mục nếu có).
