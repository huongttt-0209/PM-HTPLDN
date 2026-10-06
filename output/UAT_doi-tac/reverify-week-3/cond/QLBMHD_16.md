# Bảng đối chiếu điều kiện — QLBMHD_16 (tải về không giữ nguyên tên file gốc)

Loại bug: **Tên file khi Tải về không phải tên file gốc.** Đối tác: bấm "Tải về" trong màn Chi tiết, file tải xuống mang tên khác (tên biểu mẫu) thay vì tên file gốc đã upload. Verdict phụ thuộc: đúng vai trò + đúng nút Tải về (màn Chi tiết) + biểu mẫu có file có tên gốc khác tên biểu mẫu.

| Điều kiện có thể đổi kết quả | Đối tác (từ evidence QLBMHD_16.webm + Excel row 109) | Mình test | GAP? |
|---|---|---|:-:|
| Vai trò | **CB Nghiệp vụ - TW** (CB_NV_TW, BTP·TW) | `cbnv_tw` — CB Nghiệp vụ - Trung ương (BTP·TW), cùng vai trò | Không |
| Nút thao tác | **Tải về** trong màn Chi tiết biểu mẫu | Nút "Tải về" màn Chi tiết `/bieu-mau/28104008.../` (FE `window.open('/api/v1/bieu-maus/<id>/download')`) | Không |
| Tên file gốc vs tên biểu mẫu | Tên biểu mẫu "TKM test sửa biểu mẫu" ≠ tên file gốc đã upload | Tên biểu mẫu "QA BM001 Hidden Parent 715" ≠ tên file gốc `valid.docx` (từ `duongDanFile`) — phân biệt rõ | Không |
| Định dạng file | XLSX (partner) | DOCX (`valid.docx`) — cơ chế đặt tên tải về dùng chung endpoint, không phụ thuộc định dạng | Không |

**Kết luận: 0 GAP. Tái hiện: CÓ.**

`GET /api/v1/bieu-maus/28104008-.../download` → **302**, header `location` trỏ tới presigned MinIO URL của object gốc `valid.docx` NHƯNG kèm tham số:
`response-content-disposition=attachment; filename*=UTF-8''QA%20BM001%20Hidden%20Parent%20715.docx`
→ **Tên file tải về bị ép = "QA BM001 Hidden Parent 715.docx" (TÊN BIỂU MẪU)**, KHÔNG phải tên file gốc `valid.docx`.

- Evidence: `../reverify-audit/QLBMHD_16/network-evidence-download-filename.md` (get_network_request reqid=937 — full Location header) + screenshot `../bug-reports/image/QLBMHD_16-detail-download-context.png`.

Đối chiếu SRS `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-09-bieu-mau.md`:
- `:335` Processing Tải về Bước 3: "Truyền file gốc về máy người dùng (**giữ nguyên tên file gốc**)".
- `:356` Outputs #5 `file_ten` = "Tên file gốc" (hệ thống có lưu tên gốc — đáng lẽ dùng cho tên tải về).

→ **`Open`**: BE ép `content-disposition` = tên biểu mẫu thay vì giữ tên file gốc → vi phạm SRS `:335`. Owner: Dev BE (endpoint `/download`).

Chi tiết bug: `../bug-reports/Pass-bug-report-bieu-mau-batch5.md` (BUG-BM-B5-01).
