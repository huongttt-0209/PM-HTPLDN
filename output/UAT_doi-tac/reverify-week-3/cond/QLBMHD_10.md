# Đối chiếu điều kiện — QLBMHD_10 (Thêm biểu mẫu công khai, file hợp lệ — "Upload file thất bại")

Loại: **Reject file hợp lệ.** Đối tác báo file `.docx` hợp lệ bị "Upload file thất bại. Vui lòng thử lại.".

## Bảng đối chiếu điều kiện

| Điều kiện có thể đổi kết quả | Đối tác (evidence QLBMHD_10.jpg) | Mình test | GAP? |
|---|---|---|:-:|
| Vai trò người thao tác | CB Nghiệp vụ (CB_NV_BN) thêm biểu mẫu | `cbnv_tw` — CB Nghiệp vụ, Trung ương (BTP·TW); cùng nhóm quyền CB NV | Không |
| Màn / trường upload | Form Thêm biểu mẫu, trường File biểu mẫu | Đúng form `/bieu-mau/them-moi`, trường File biểu mẫu | Không |
| Loại file | `.docx` hợp lệ (`3.BTP_CPLQG_S7_...docx`) | `valid.docx` — docx OOXML hợp lệ, <20MB | Không |
| Kết quả quan sát | Upload + tạo biểu mẫu | Upload + submit "Thêm mới" | Không |

**0 GAP** cho điều kiện "upload file .docx hợp lệ khi thêm biểu mẫu".

## Cổng 3 — SRS vs web (dạng bullet)

- SRS: file doc/docx/xls/xlsx ≤20MB hợp lệ phải upload được + tạo biểu mẫu (`srs-fr-09` FR-VII-04, Postconditions dòng 363).
- Web đo được: `valid.docx` → upload 0 lỗi (`ant-upload-list-item-done`) → submit → tạo biểu mẫu THÀNH CÔNG (`/bieu-mau/danh-sach`, record xuất hiện).
- Đối chiếu: file `.docx` hợp lệ upload + tạo bình thường. Lỗi "Upload file thất bại" đối tác báo KHÔNG tái hiện. Chuỗi "Vui lòng thử lại" gợi lỗi tạm thời server/mạng ở env đối tác.

## Verdict

- → **Reject**: không tái hiện; file hợp lệ upload + tạo biểu mẫu OK trên build hiện tại. Đề nghị đối tác kiểm lại (kèm size/định dạng file + thời điểm nếu gặp lại).

Evidence: [`../reverify-audit/QLBMHD_10/valid-docx-attached.png`](../reverify-audit/QLBMHD_10/valid-docx-attached.png) + [`../reverify-audit/QLBMHD_10/record-created-list.png`](../reverify-audit/QLBMHD_10/record-created-list.png).
