# Đối chiếu điều kiện — QLBMHD_11 (Thêm mới khi thư mục Công khai, file hợp lệ — "Chỉ chấp nhận .doc/.docx/.xls/.xlsx")

Loại: **Reject file hợp lệ.** Đối tác báo file `.docx` hợp lệ bị chặn "Chỉ chấp nhận .doc/.docx/.xls/.xlsx".

## Bảng đối chiếu điều kiện

| Điều kiện có thể đổi kết quả | Đối tác (evidence QLBMHD_11.webm) | Mình test | GAP? |
|---|---|---|:-:|
| Vai trò người thao tác | CB Nghiệp vụ thêm biểu mẫu | `cbnv_tw` — CB Nghiệp vụ, Trung ương (BTP·TW) | Không |
| Màn / trường upload | Form Thêm biểu mẫu, trường File biểu mẫu | Đúng form `/bieu-mau/them-moi`, trường File biểu mẫu | Không |
| Thư mục chứa | Thư mục (bối cảnh Công khai) | Chọn thư mục "Thư mục biểu mẫu seed" + submit tạo | Không |
| Loại file | `.docx` hợp lệ | `valid.docx` — docx OOXML hợp lệ, đúng định dạng .docx | Không |

**0 GAP** cho điều kiện "thêm biểu mẫu với file .docx hợp lệ".

## Cổng 3 — SRS vs web (dạng bullet)

- SRS: trường File biểu mẫu nhận doc/docx/xls/xlsx (`srs-fr-09:50`, `:652`). File `.docx` hợp lệ phải được chấp nhận.
- Web đo được: `valid.docx` → trường File biểu mẫu nhận OK (`ant-upload-list-item-done`), 0 lỗi "Chỉ chấp nhận..."; submit → tạo biểu mẫu THÀNH CÔNG.
- Đối chiếu: "Chỉ chấp nhận: .doc, .docx, .xls, .xlsx — Tối đa 20MB" trên web là **text hướng dẫn luôn hiển thị**, KHÔNG phải lỗi validation. File `.docx` hợp lệ được nhận + tạo bình thường → lỗi đối tác báo không tái hiện.

## Verdict

- → **Reject**: không tái hiện; file `.docx` hợp lệ được nhận + tạo biểu mẫu OK. Đề nghị đối tác kiểm lại (có thể env cũ đọc sai MIME / lỗi tạm thời).

Evidence: [`../reverify-audit/QLBMHD_11/note.md`](../reverify-audit/QLBMHD_11/note.md) + [`../reverify-audit/QLBMHD_10/record-created-list.png`](../reverify-audit/QLBMHD_10/record-created-list.png).
