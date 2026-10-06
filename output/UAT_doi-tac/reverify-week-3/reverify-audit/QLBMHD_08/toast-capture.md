# QLBMHD_08 (row 101) — Upload tệp có mã độc (EICAR) — đo hành vi + thông báo

- **Tài khoản:** `cbnv_tw` (CB Nghiệp vụ - TW, BTP·TW).
- **Màn:** Form Thêm biểu mẫu (`/bieu-mau/them-moi`), trường "File biểu mẫu".
- **Chuẩn test mã độc:** chuỗi **EICAR** (`X5O!P%@AP[4\PZX54(P^)7CC)7}$EICAR-STANDARD-ANTIVIRUS-TEST-FILE!$H+H*`) — file test chuẩn công nghiệp, vô hại, MỌI antivirus đều nhận diện. Dùng thay cho "file có mã độc" là thực hành chuẩn.

## Hai bước đo

**Bước 1 — `eicar.docx` (EICAR bytes thô, đuôi .docx, KHÔNG phải ZIP hợp lệ):**
```json
{ "SO_REQUEST": 1, "SO_TOAST": 1, "chu_toast": ["Nội dung file không khớp định dạng. Vui lòng tải lên file gốc đúng loại đã chọn."] }
```
→ App chặn ở bước kiểm **định dạng** (giống corrupt.docx), CHƯA tới bước quét mã độc. Không đo được path AV bằng file này.

**Bước 2 — `valid-eicar.docx` (docx OOXML HỢP LỆ, cùng cấu trúc `valid.docx`, chèn chuỗi EICAR vào `word/document.xml`):**
- Upload: `POST /api/v1/bieu-maus/upload` → **HTTP 201 Created** (server chấp nhận + lưu).
- Toast lỗi: **0**. Upload item: `ant-upload-list-item-done` (thành công). File đính kèm OK.
- Submit "Thêm mới" (folder "Thư mục biểu mẫu seed", tên `QA-eicar-malware-test-row101`) → tạo biểu mẫu **THÀNH CÔNG**, chuyển `/bieu-mau/danh-sach`, record xuất hiện, **0 chặn / 0 message mã độc**.
- Evidence: [`eicar-accepted-list.png`](eicar-accepted-list.png) + network 201.

## Đối chiếu SRS (yêu cầu quét virus — 3 nơi)

- `srs-fr-09:314`: bước xử lý "Quét virus file đính kèm".
- `srs-fr-09:382` (Edge Case EC-02): "File chứa macro virus (doc/docx) → **Quét antivirus TRƯỚC lưu trữ** → **ERR-BM-07** nếu phát hiện mã độc".
- `srs-fr-09:652` (SCR-VII-02 Inputs #15): File đính kèm "Bắt buộc. doc/docx/xls/xlsx. Max 20MB. **Quét virus**".

→ SRS bắt buộc quét virus TRƯỚC khi lưu, chặn nếu phát hiện mã độc. Thực tế: file `.docx` hợp lệ chứa chuỗi test mã độc chuẩn EICAR được **chấp nhận, lưu (201) và tạo thành biểu mẫu** — không bị quét chặn, không có ERR-BM-07.

## Caveat (ghi trung thực)

- EICAR nằm trong `document.xml` bên trong ZIP (.docx). AV chuẩn (vd ClamAV) giải nén docx và bắt được; nếu AV của app không giải nén archive → có thể bỏ sót. Không quan sát được server-side để biết "không có AV" hay "AV không quét trong archive".
- Dù cách nào: hành vi quan sát (file test mã độc được lưu + có thể công khai lên Cổng PLQG) KHÔNG khớp yêu cầu SRS "quét virus trước lưu trữ".
- Đề nghị Dev/Security xác nhận: (1) AV có chạy trước lưu trữ không; (2) có quét nội dung bên trong archive .docx không.

## Verdict

- Lỗi đối tác báo ("thông báo mã độc sai thiết kế") KHÔNG tái hiện theo nghĩa "sai wording" — thực tế **nghiêm trọng hơn**: không có thông báo/chặn nào, file mã độc được chấp nhận.
- → **Open (BUG-QLBMHD_08)** — vi phạm yêu cầu quét virus SRS (dòng 314/382/652). Type: Security. Đề nghị Dev/Security kiểm tra pipeline quét AV.
