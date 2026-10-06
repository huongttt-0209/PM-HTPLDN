# QLBMHD_11 (row 104) — Thêm mới khi thư mục Công khai, file hợp lệ — kiểm "Chỉ chấp nhận .doc/.docx/.xls/.xlsx"

- **Tài khoản:** `cbnv_tw` (CB Nghiệp vụ - TW, BTP·TW).
- **Đối tác phản ánh** (env `htpldn-uat.ospgroup.vn`, video `QLBMHD_11.webm`): thêm biểu mẫu (bối cảnh thư mục Công khai) với file hợp lệ → báo lỗi **"Chỉ chấp nhận .doc/.docx/.xls/.xlsx"** dù file đúng định dạng.

## Kết quả kiểm thử (env `18.143.165.120.nip.io`, 2026-07-20)

- Form Thêm biểu mẫu, chọn folder "Thư mục biểu mẫu seed", đính kèm `valid.docx` (đúng định dạng .docx):
  - Trường "File biểu mẫu" nhận file OK, item `ant-upload-list-item-done`, **0 lỗi** "Chỉ chấp nhận...".
  - Submit "Thêm mới" → tạo biểu mẫu **THÀNH CÔNG** → `/bieu-mau/danh-sach`, record `QA-test-valid-docx-row104` xuất hiện.
  - Evidence: dùng chung [`../QLBMHD_10/record-created-list.png`](../QLBMHD_10/record-created-list.png) (cùng lượt tạo).
- Hint dưới trường File biểu mẫu: "Chỉ chấp nhận: .doc, .docx, .xls, .xlsx — Tối đa 20MB" — đây là **text hướng dẫn** (luôn hiển thị), KHÔNG phải lỗi validation. File `.docx` hợp lệ được nhận bình thường.

## Verdict

- Lỗi đối tác báo ("Chỉ chấp nhận .doc/.docx/.xls/.xlsx" chặn file hợp lệ) **KHÔNG tái hiện** — file `.docx` hợp lệ được nhận + tạo biểu mẫu thành công.
- → **Reject** (đề nghị đối tác kiểm tra lại; có thể ở env cũ file bị đọc sai MIME hoặc lỗi tạm thời).
