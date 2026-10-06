# Bảng đối chiếu điều kiện — QLNDTVVCG_08 (row 281) — REVERIFY sau dev fix

**Kết luận:** Pass — Trường "Nội dung tư vấn chi tiết" trên form Thêm TVCS **nay là Rich Text Editor** (TipTap/ProseMirror, contenteditable, có thanh công cụ định dạng), không còn là `<textarea>` thô. Đúng "KQ mong đợi" của bug gốc.

- **Mã TC:** QLNDTVVCG_08 (row 281) · **Màn:** SCR-X1-02 form Thêm (`/tv-chuyen-sau/tao-moi`).
- **Loại bug:** loại control của 1 field (phụ thuộc màn + role mở form) → lập bảng đối chiếu.

## Bảng đối chiếu điều kiện (re-test đúng điều kiện bug gốc)

| Điều kiện có thể đổi kết quả | Bug gốc (Pass-bug-report-tvcs-batchB.md) | Mình test (cbnv_tw_01 / CB_NV_TW, BTP·TW, 23/07/2026) | GAP? |
|---|---|---|:-:|
| Vai trò / tài khoản | CB_NV_TW (cbnv_tw_02), đơn vị BTP·TW | CB_NV_TW (cbnv_tw_01), đơn vị BTP·TW — cùng role + cùng đơn vị | Không |
| Màn hình | Form Thêm yêu cầu TVCS `/tv-chuyen-sau/tao-moi` (SCR-X1-02) | Form Thêm yêu cầu TVCS `/tv-chuyen-sau/tao-moi` (SCR-X1-02) | Không |
| Field kiểm tra | Accordion "Nội dung tư vấn" → "Nội dung tư vấn chi tiết" | Đúng field "Nội dung tư vấn chi tiết" | Không |
| Phép đo control | Đọc DOM: loại control (textarea vs rich text editor) | Đọc DOM `[contenteditable]` + class + thử áp định dạng thật | Không |
| Kết quả đo | `<textarea>` thô, **0 tín hiệu** rich text (không quill/ckeditor/tinymce/contenteditable) | **contenteditable div `tiptap ProseMirror`** role=textbox + toolbar 6 nút; áp Bold → `<strong>` | Không |

**0 GAP** — re-test đúng vai trò/màn/field như bug gốc; chỉ khác instance tài khoản (`_01` vs `_02`, cùng role CB_NV_TW + cùng đơn vị BTP·TW).

**Artifact real-data (chạy trên form thật, đo bằng `evaluate_script` + thao tác gõ/định dạng):**
- Field "Nội dung tư vấn chi tiết" = `<div class="tiptap ProseMirror" role="textbox" contenteditable="true">` → **là Rich Text Editor (TipTap/ProseMirror)**, không phải textarea.
- Thanh công cụ có đủ 6 nút: **In đậm · In nghiêng · Gạch chân · Danh sách · Danh sách có số · Chèn liên kết**.
- Thao tác thật: click editor → bật "In đậm" → gõ "Noi dung tu van in dam - reverify RTE" → editor tạo markup `<p><strong>Noi dung tu van in dam - reverify RTE</strong></p>` (định dạng hoạt động thực, không phải chỉ có nút).
- `<textarea>` duy nhất còn lại trên form thuộc field **"Ghi chú"** (placeholder "Ghi chú thêm (nếu có)"), KHÔNG phải field nội dung.
- Ảnh: `bug-reports/tvcs/image/bug-qlndtvvcg_08-retest-pass-richtext-editor.png`.

## Kết luận

- SRS SCR-X1-02 §Thành phần màn hình: "Nội dung TV chi tiết (Rich Text Editor, bắt buộc, max 50KB)".
- Web hiện tại **đã là Rich Text Editor** cho phép định dạng văn bản → khớp KQ mong đợi → **Pass (Closed)**.
