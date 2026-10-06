# Bảng đối chiếu điều kiện — QLBMHD_17 (Xem trước mở hộp thoại tải file thay vì cửa sổ xem trước)

Loại bug: **"Xem trước" không mở khung xem trước mà mở hộp thoại tải file.** Verdict phụ thuộc: đúng vai trò + đúng nút Xem trước (màn Chi tiết) + biểu mẫu có file.

| Điều kiện có thể đổi kết quả | Đối tác (evidence QLBMHD_17.webm + Excel row 110) | Mình test | GAP? |
|---|---|---|:-:|
| Vai trò | **CB Nghiệp vụ - TW** | `cbnv_tw` — CB Nghiệp vụ - Trung ương (BTP·TW), cùng vai trò | Không |
| Nút thao tác | **Xem trước** (màn Chi tiết biểu mẫu) | Nút "Xem trước" màn Chi tiết `/bieu-mau/<id>/` (FE `window.open('/api/v1/bieu-maus/<id>/preview')`) | Không |
| Biểu mẫu có file | Biểu mẫu có file đính kèm | BM-20260715-001 (DOCX) + BM-B6-valid-2 (XLSX) — đều có file | Không |

**Kết luận: 0 GAP. Tái hiện: CÓ.**

FE bấm "Xem trước" → `window.open('/api/v1/bieu-maus/<id>/preview','_blank')`, KHÔNG render khung xem trước in-app (`hasModal=false`, `hasIframe=false`, `hasPdfViewer=false`). Endpoint `/preview` → **302** redirect thẳng tới **file thô** (`response-content-disposition=inline`) → trình duyệt không render inline được Office file → hiện hộp thoại tải về.

- Evidence: `../reverify-audit/QLBMHD_17/network-evidence-preview.md` + screenshot `../bug-reports/image/QLBMHD_17-18-19-preview-opens-rawfile.png`.

Đối chiếu SRS `srs-fr-09-bieu-mau.md:320-327` (Processing Xem trực tuyến): Bước 2 docx→PDF, Bước 3 xlsx→bảng read-only, Bước 4 không hỗ trợ→thông báo+tải. Hệ thống mở thẳng file thô, không xem trước, không "thông báo".

→ **`Open`**: "Xem trước" không cho xem trước trực tuyến, mở thẳng file thô (trình duyệt tải về) → vi phạm SRS `:320-327`. Owner: Dev BE (thiếu convert preview) + Dev FE (thiếu khung xem trước). Gốc chung với QLBMHD_18 (DOCX) + QLBMHD_19 (XLSX).

Chi tiết bug: `../bug-reports/Pass-bug-report-bieu-mau-batch5.md` (BUG-BM-B5-02).
