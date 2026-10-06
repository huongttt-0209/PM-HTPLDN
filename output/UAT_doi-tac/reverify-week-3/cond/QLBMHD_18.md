# Bảng đối chiếu điều kiện — QLBMHD_18 (Xem trước DOC/DOCX không convert PDF preview)

Loại bug: **Xem trước file DOC/DOCX không chuyển đổi sang PDF preview mà mở hộp thoại tải.** Verdict phụ thuộc: đúng vai trò + đúng nút Xem trước + biểu mẫu định dạng DOC/DOCX.

| Điều kiện có thể đổi kết quả | Đối tác (evidence QLBMHD_18.webm + Excel row 111) | Mình test | GAP? |
|---|---|---|:-:|
| Vai trò | **CB Nghiệp vụ - TW** | `cbnv_tw` — CB Nghiệp vụ - Trung ương (BTP·TW), cùng vai trò | Không |
| Nút thao tác | **Xem trước** (màn Chi tiết) | Nút "Xem trước" màn Chi tiết (FE `window.open('/api/v1/bieu-maus/<id>/preview')`) | Không |
| Định dạng file | **DOCX** (partner: BM-20260713-002 "TKM test xem trước file DOC", DOCX 44.9KB) | **DOCX** — BM-20260715-001 "QA BM001 Hidden Parent 715" (`valid.docx`) | Không |

**Kết luận: 0 GAP. Tái hiện: CÓ.**

`GET /api/v1/bieu-maus/28104008-.../preview` (biểu mẫu DOCX) → **302** → `location` = `http://18.143.165.120:9000/htpldn/.../valid.docx?response-content-disposition=inline&...` → trỏ thẳng tới **file .docx THÔ** phục vụ `inline`, KHÔNG convert sang PDF. Trình duyệt không render .docx inline → hộp thoại tải về. FE không có khung xem trước in-app.

- Evidence: `../reverify-audit/QLBMHD_17/network-evidence-preview.md` (mục DOCX, reqid=1005/1006) + screenshot `../bug-reports/image/QLBMHD_17-18-19-preview-opens-rawfile.png`.

Đối chiếu SRS `srs-fr-09-bieu-mau.md:325` (Processing preview Bước 2): "Nếu doc/docx: **chuyển đổi sang PDF preview**".

→ **`Open`**: DOCX không được convert sang PDF preview → vi phạm SRS `:325`. Owner: Dev BE (thiếu convert docx→PDF). Cùng gốc bug với QLBMHD_17/19.

Chi tiết bug: `../bug-reports/Pass-bug-report-bieu-mau-batch5.md` (BUG-BM-B5-02).
