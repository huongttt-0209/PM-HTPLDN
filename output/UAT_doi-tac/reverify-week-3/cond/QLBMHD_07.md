# Đối chiếu điều kiện — QLBMHD_07 (Upload tệp hỏng — thông báo)

Loại: **Validation upload — thông báo khi file hỏng/không hợp lệ.** Đối tác báo thông báo "sai thiết kế" (generic).

## Bảng đối chiếu điều kiện

| Điều kiện có thể đổi kết quả | Đối tác (evidence QLBMHD_07.jpg) | Mình test | GAP? |
|---|---|---|:-:|
| Vai trò người thao tác | CB Nghiệp vụ upload biểu mẫu | `cbnv_tw` — CB Nghiệp vụ, Trung ương (BTP·TW) | Không |
| Màn / trường upload | Form Thêm biểu mẫu, trường File biểu mẫu | Đúng form `/bieu-mau/them-moi`, trường File biểu mẫu | Không |
| Loại file lỗi | File hỏng đuôi .docx (`corrupt.docx`) | `corrupt.docx` — bytes rác, đuôi .docx (không phải ZIP hợp lệ) | Không |
| Cách đo thông báo | Quan sát toast UI | `toast-capture.js` observer + đếm request | Không |

**0 GAP.** Đúng vai trò + đúng trường + đúng loại file hỏng + đo toast bằng observer.

## Cổng 3 — SRS vs web (dạng bullet)

- SRS ERR-BM-04 (`srs-fr-09:345`): "File không hợp lệ hoặc bị hỏng". SRS ERR-BM-01 (`srs-fr-09:342`): "Chỉ chấp nhận file doc, docx, xls, xlsx".
- Web đo được: toast "Nội dung file không khớp định dạng. Vui lòng tải lên file gốc đúng loại đã chọn." (1 request POST upload, 1 toast, file không đính kèm).
- Đối chiếu: app chặn file không hợp lệ + báo thông báo cụ thể (đúng ý ERR-BM-04/01, chi tiết hơn), khác **cách diễn đạt**. Lỗi generic "Upload file thất bại" đối tác báo (env cũ) không tái hiện.
- Đối chứng: `valid.docx` cùng cấu trúc minimal upload OK → app từ chối `corrupt.docx` vì nội dung không hợp lệ, không phải vì minimal.

## Verdict

- Yêu cầu nghiệp vụ (chặn file hỏng + báo lỗi rõ) **đạt**; chỉ khác wording so chuỗi mẫu SRS. Không tự Open (nghiệp vụ đạt) cũng không Reject đơn thuần (còn câu hỏi wording).
- → **BA confirm**: BA quyết có bắt buộc đúng nguyên văn ERR-BM-04 không.

Evidence: [`../reverify-audit/QLBMHD_07/toast-capture.md`](../reverify-audit/QLBMHD_07/toast-capture.md).
