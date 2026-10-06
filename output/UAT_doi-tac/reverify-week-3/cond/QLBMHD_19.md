# Bảng đối chiếu điều kiện — QLBMHD_19 (Xem trước XLS/XLSX không hiển thị bảng read-only)

Loại bug: **Xem trước file XLS/XLSX không hiển thị bảng read-only mà mở hộp thoại tải.** Verdict phụ thuộc: đúng vai trò + đúng nút Xem trước + biểu mẫu định dạng XLS/XLSX.

| Điều kiện có thể đổi kết quả | Đối tác (evidence QLBMHD_19.webm + Excel row 112) | Mình test | GAP? |
|---|---|---|:-:|
| Vai trò | **CB Nghiệp vụ - TW** | `cbnv_tw` — CB Nghiệp vụ - Trung ương (BTP·TW), cùng vai trò | Không |
| Nút thao tác | **Xem trước** (màn Chi tiết) | Nút "Xem trước" màn Chi tiết (FE `window.open('/api/v1/bieu-maus/<id>/preview')`) | Không |
| Định dạng file | **XLSX** (partner: file "Plan kiem thu.xlsx") | **XLSX** — BM-B6-valid-2 (`BM-B6-valid-2.xlsx`, id ad4258c3-...) | Không |

**Kết luận: 0 GAP. Tái hiện: CÓ.**

`GET /api/v1/bieu-maus/ad4258c3-.../preview` (biểu mẫu XLSX) → **302** → `location` = `http://18.143.165.120:9000/htpldn/.../BM-B6-valid-2.xlsx?response-content-disposition=inline&...` → trỏ thẳng tới **file .xlsx THÔ** phục vụ `inline`, KHÔNG hiển thị bảng read-only. Trình duyệt không render .xlsx inline → hộp thoại tải về. FE không có khung xem trước in-app.

- Evidence: `../reverify-audit/QLBMHD_17/network-evidence-preview.md` (mục XLSX, reqid=1008) + screenshot `../bug-reports/image/QLBMHD_17-18-19-preview-opens-rawfile.png`.

Đối chiếu SRS `srs-fr-09-bieu-mau.md:326` (Processing preview Bước 3): "Nếu xls/xlsx: **hiển thị preview dạng bảng (read-only)**".

→ **`Open`**: XLSX không được hiển thị dạng bảng read-only → vi phạm SRS `:326`. Owner: Dev BE (thiếu render xlsx→bảng). Cùng gốc bug với QLBMHD_17/18.

Chi tiết bug: `../bug-reports/Pass-bug-report-bieu-mau-batch5.md` (BUG-BM-B5-02).
