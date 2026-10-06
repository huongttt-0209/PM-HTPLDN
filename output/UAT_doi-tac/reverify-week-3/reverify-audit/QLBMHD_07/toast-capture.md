# QLBMHD_07 (row 100) — Upload tệp hỏng/không hợp lệ — đo thông báo

- **Tài khoản:** `cbnv_tw` (CB Nghiệp vụ - TW, BTP·TW).
- **Màn:** Form Thêm biểu mẫu (`/bieu-mau/them-moi`), trường "File biểu mẫu".
- **File test:** `corrupt.docx` — nội dung bytes rác, đặt đuôi `.docx` (KHÔNG phải file ZIP/OOXML hợp lệ).
- **Đo bằng:** `tools/toast-capture.js` observer (không lọc trùng, innerText, đếm request).

## Kết quả đo (2026-07-20)

```json
{ "SO_REQUEST": 1, "request": ["POST /api/v1/bieu-maus/upload"], "SO_TOAST": 1,
  "chu_toast": ["Nội dung file không khớp định dạng. Vui lòng tải lên file gốc đúng loại đã chọn."] }
```

- App gọi server (POST upload) → trả lỗi → toast **"Nội dung file không khớp định dạng. Vui lòng tải lên file gốc đúng loại đã chọn."** File KHÔNG được đính kèm.
- **Đối chứng quan trọng:** `valid.docx` cùng cấu trúc 3-part minimal LẠI upload OK (row 103) → app từ chối `corrupt.docx` vì nội dung KHÔNG phải docx hợp lệ (bytes rác), chứ không phải vì file nhỏ/minimal. Message phản ánh đúng bản chất "nội dung không khớp định dạng".

## Đối chiếu SRS

- ERR-BM-04 (`srs-fr-09:345`): "File không hợp lệ hoặc bị hỏng" (file corrupt).
- ERR-BM-01 (`srs-fr-09:342`): "Chỉ chấp nhận file doc, docx, xls, xlsx" (sai format).
- App: "Nội dung file không khớp định dạng. Vui lòng tải lên file gốc đúng loại đã chọn." — truyền tải đúng ý "file không hợp lệ / nội dung không đúng định dạng", cụ thể + hướng dẫn hơn cả 2 chuỗi SRS. Khác **cách diễn đạt**.

## So sánh với evidence đối tác

- Đối tác (env `htpldn-uat.ospgroup.vn`, ảnh `QLBMHD_07.jpg`): upload `corrupt.docx` → toast **generic "Upload file thất bại. Vui lòng thử lại."** (không cho biết file hỏng).
- Env kiểm thử (`18.143.165.120.nip.io`): thông báo CỤ THỂ "Nội dung file không khớp định dạng..." → lỗi generic đối tác báo KHÔNG còn.

## Verdict

- App chặn file không hợp lệ + báo thông báo cụ thể, hữu ích (đúng tinh thần ERR-BM-04/ERR-BM-01), chỉ khác wording so với chuỗi mẫu SRS. Lỗi "thông báo sai thiết kế (generic)" đối tác báo không tái hiện trên build hiện tại.
- → **BA confirm**: thông báo hiện tại truyền tải đúng yêu cầu, khác cách diễn đạt → BA quyết có bắt buộc đúng nguyên văn ERR-BM-04 không.
