# QLBMHD_10 (row 103) — Thêm biểu mẫu công khai, file hợp lệ — kiểm "Upload file thất bại"

- **Tài khoản:** `cbnv_tw` (CB Nghiệp vụ - TW, BTP·TW).
- **Đối tác phản ánh** (env `htpldn-uat.ospgroup.vn`, ảnh `QLBMHD_10.jpg`, account CB_NV_BN): upload file `.docx` HỢP LỆ (`3.BTP_CPLQG_S7_2025_PM_L4_CONG_CT_HTPLDN.docx`) → toast **"Upload file thất bại. Vui lòng thử lại."** (từ chối file hợp lệ).

## Kết quả kiểm thử (env `18.143.165.120.nip.io`, 2026-07-20)

- Upload `valid.docx` (docx OOXML hợp lệ, <20MB) vào trường File biểu mẫu:
  - `POST /api/v1/bieu-maus/upload` → **0 toast lỗi**, upload item `ant-upload-list-item-done` (thành công), file đính kèm.
  - Evidence: [`valid-docx-attached.png`](valid-docx-attached.png).
- Submit "Thêm mới" (folder "Thư mục biểu mẫu seed", tên `QA-test-valid-docx-row104`) → tạo biểu mẫu **THÀNH CÔNG** → `/bieu-mau/danh-sach`, record xuất hiện, 0 lỗi.
  - Evidence: [`record-created-list.png`](record-created-list.png).

## Verdict

- Lỗi đối tác báo ("Upload file thất bại" với file hợp lệ) **KHÔNG tái hiện** trên build hiện tại — file `.docx` hợp lệ upload + tạo biểu mẫu thành công.
- Chuỗi "Upload file thất bại. **Vui lòng thử lại.**" (please retry) mang tính lỗi **tạm thời** (server/mạng) — có thể do sự cố nhất thời phía env đối tác lúc chụp.
- → **Reject** (đề nghị đối tác kiểm tra lại: trên build hiện tại file hợp lệ upload bình thường; nếu gặp lại, gửi kèm size/định dạng file cụ thể + thời điểm để soát lỗi tạm thời).
