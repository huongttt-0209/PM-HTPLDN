# Bảng đối chiếu điều kiện — VVTLHDN_06 (row 247) — Xuất PDF BC Vụ việc theo loại hình DN

**Verdict:** Open — lỗi "Không thể tạo file xuất" (ERR-RPT-04) KHÔNG tái hiện (file PDF tải về được), NHƯNG nội dung file PDF **thiếu 3/4 trường header bắt buộc** (Kỳ báo cáo / Đơn vị / Ngày tạo) theo SRS `srs-fr-11-bao-cao.md:1088` → BUG-EXPORT-PDF-HEADER.

| Điều kiện có thể đổi kết quả | Đối tác (evidence full-res VVTLHDN_06.jpg) | Mình test (21/07/2026) | GAP? |
|---|---|---|:-:|
| Vai trò / tài khoản | Quản trị viên (QTHT) — góc phải màn hình | `cbnv_tw_01` (CB Nghiệp vụ TW — vai trò chuẩn ra verdict) | Không |
| Loại báo cáo | BC Vụ việc theo loại hình DN | BC Vụ việc theo loại hình DN | Không |
| Kỳ + khoảng thời gian | Năm — 01/01/2026 → 31/12/2026 | Năm — 01/01/2026 → 31/12/2026 | Không |
| Đơn vị (phạm vi) | Toàn quốc | Toàn quốc | Không |
| Bộ lọc Loại DN (đặc thù, tùy chọn) | Để trống | Để trống — khớp đối tác | Không |
| Dữ liệu tiền đề (phải có data mới bật nút Xuất) | Có data — đã Xem báo cáo trước | Có data — Nhỏ 3 + Siêu nhỏ 14 (Tổng 17), đã Xem báo cáo trước khi Xuất | Không |
| Thao tác | Xuất PDF (.pdf) | Xuất PDF (.pdf), khổ A4 + hướng Dọc (mặc định) | Không |

**0 GAP.** `POST /api/v1/bao-cao/export` (formatXuat=PDF, reqid=112) trả **200** + `content-type: application/pdf` + `content-disposition: attachment; filename="bao-cao-vu-viec-theo-loai-dn-2026-07-21.pdf"`. Toast = "Đang tạo file...".

**Kiểm nội dung file (PyMuPDF):** A4 + Tinos cỡ 13; số liệu đúng (Nhỏ 3, Siêu nhỏ 14). Dòng đầu chỉ có tiêu đề "BC VỤ VIỆC THEO LOẠI HÌNH DN" rồi vào bảng — **KHÔNG có** khối header Kỳ báo cáo / Đơn vị / Ngày tạo. Bản Excel cùng báo cáo (VVTLHDN_05.xlsx) đủ 4 trường. File gốc: `reverify-audit/_export-check/VVTLHDN_06.pdf`; ảnh render: `bug-reports/bctk/image/VVTLHDN_06-pdf-no-header.png`.

**Lưu ý env:** lỗi tạo-file của đối tác không tái hiện; lỗi thiếu-header là lỗi khác (SRS-based) → Open + chuyển dev.
