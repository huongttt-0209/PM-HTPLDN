# Đối chiếu điều kiện — QLBMHD_06 (Upload file >20MB — thông báo lỗi)

Loại: **Validation upload — thông báo khi file vượt 20MB.** Đối tác báo web hiển thị "File vượt quá 20MB (24.7 MB)" (file 24.7MB) — kiểm xem thông báo có đúng yêu cầu SRS ERR-BM-02 không.

Verify đúng vai trò đối tác (**CB Nghiệp vụ**), thao tác thật: mở form Thêm biểu mẫu → chọn file .docx ~21MB vào trường File biểu mẫu → đo toast qua observer.

## Bảng đối chiếu điều kiện

| Điều kiện có thể đổi kết quả | Đối tác (evidence QLBMHD_06) | Mình test | GAP? |
|---|---|---|:-:|
| Vai trò người thao tác | CB Nghiệp vụ upload biểu mẫu | `cbnv_tw` — CB Nghiệp vụ, Trung ương (BTP·TW) | Không |
| Màn / trường upload | Form Thêm biểu mẫu, trường File biểu mẫu (max 20MB) | Đúng form `/bieu-mau/them-moi`, trường File biểu mẫu (hint "Tối đa 20MB") | Không |
| File vượt ngưỡng | File > 20MB (đối tác dùng 24.7MB) | `big-21mb.docx` ~21.0MB (docx hợp lệ, chỉ vượt dung lượng) | Không |
| Cách đo thông báo | Quan sát toast trên UI | `toast-capture.js` observer (không lọc trùng, innerText, đếm request) | Không |

**0 GAP.** Đúng vai trò + đúng trường upload + file vượt 20MB + đo toast bằng observer.

## Cổng 3 — SRS ERR-BM-02 vs web

- SRS yêu cầu: ERR-BM-02 (`srs-fr-09:343`) — "File vượt quá giới hạn 20MB. Kích thước: {size}MB". Yêu cầu nghiệp vụ: báo file vượt ngưỡng 20MB + cho biết kích thước thực.
- Web đo được: toast **"File vượt quá 20MB (21.0 MB)"**, 1 khung, **0 request ghi** (FE chặn client-side, file không đính kèm).
- Đối chiếu: **cùng nội dung nghiệp vụ** — báo vượt 20MB + kèm kích thước thực (21.0 MB). Khác **cách diễn đạt**: bỏ chữ "giới hạn", format kích thước "(21.0 MB)" thay vì ". Kích thước: 21.0MB".

## Verdict

- Yêu cầu nghiệp vụ ERR-BM-02 (chặn file >20MB + báo kích thước) **được đáp ứng**. Sai khác chỉ ở **wording** so với chuỗi mẫu SRS.
- Theo quy tắc "describe don't prescribe": QA không tự Open (nghiệp vụ đã đạt) cũng không Reject (đối tác quan sát đúng thực tế). → **BA confirm**: BA quyết có bắt buộc đúng nguyên văn chuỗi ERR-BM-02 hay chấp nhận wording hiện tại.

Evidence: [`../reverify-audit/QLBMHD_06/toast-capture.md`](../reverify-audit/QLBMHD_06/toast-capture.md).
