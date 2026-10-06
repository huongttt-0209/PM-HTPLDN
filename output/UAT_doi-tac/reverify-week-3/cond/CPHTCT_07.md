# Bảng đối chiếu điều kiện — CPHTCT_07 (row 251) — Xuất PDF BC Chi phí chi trả hỗ trợ

**Verdict:** Open — lỗi "Không thể tạo file xuất" (ERR-RPT-04) KHÔNG tái hiện (file PDF tải về được), NHƯNG nội dung file PDF **thiếu khối header bắt buộc** (Kỳ báo cáo / Đơn vị: Toàn quốc / Ngày tạo) theo SRS `srs-fr-11-bao-cao.md:1088` → BUG-EXPORT-PDF-HEADER.

| Điều kiện có thể đổi kết quả | Đối tác (evidence full-res CPHTCT_07.jpg) | Mình test (21/07/2026) | GAP? |
|---|---|---|:-:|
| Vai trò / tài khoản | Quản trị viên (QTHT) — góc phải màn hình | `cbnv_tw_01` (CB Nghiệp vụ TW — vai trò chuẩn ra verdict) | Không |
| Loại báo cáo | BC Chi phí chi trả hỗ trợ | BC Chi phí chi trả hỗ trợ | Không |
| Kỳ + khoảng thời gian | Năm — 01/01/2026 → 31/12/2026 | Năm — 01/01/2026 → 31/12/2026 | Không |
| Đơn vị (phạm vi) | Toàn quốc | Toàn quốc | Không |
| Dữ liệu tiền đề (phải có data mới bật nút Xuất) | Có data — KPI Tổng chi phí 226.308.268đ / 25 hồ sơ (env đối tác) | Có data — Tổng chi phí 8.000.000đ / 1 hồ sơ (env QA), đã Xem báo cáo trước khi Xuất. Số lượng data khác env nhưng đều CÓ data → không đổi verdict export | Không |
| Thao tác | Xuất PDF (.pdf) | Xuất PDF (.pdf), khổ A4 + hướng Dọc (mặc định) | Không |

**0 GAP.** `POST /api/v1/bao-cao/export` (formatXuat=PDF, reqid=129) trả **200** + `content-type: application/pdf` + `content-disposition: attachment; filename="bao-cao-chi-phi-chi-tra-2026-07-21.pdf"`. Toast = "Đang tạo file...".

**Kiểm nội dung file (PyMuPDF):** A4 + Tinos cỡ 13; số liệu đúng (Cục Bổ trợ tư pháp: 1 HS, 8.000.000 tổng + TB). Dòng đầu chỉ có tiêu đề "BC CHI PHÍ CHI TRẢ HỖ TRỢ" rồi vào thẳng bảng — **KHÔNG có** khối header Kỳ báo cáo / Đơn vị: Toàn quốc / Ngày tạo. (Lưu ý: chữ "Đơn vị" trong file là **tên cột bảng dữ liệu**, KHÔNG phải dòng header phạm vi "Đơn vị: Toàn quốc" — khối header TT17 vẫn thiếu.) Bản Excel cùng báo cáo (CPHTCT_06.xlsx) có đủ 4 trường header. File gốc: `reverify-audit/_export-check/CPHTCT_07.pdf`; ảnh render: `bug-reports/bctk/image/CPHTCT_07-pdf-no-header.png`.

**Lưu ý env:** lỗi tạo-file của đối tác không tái hiện; lỗi thiếu-header là lỗi khác (SRS-based) → Open + chuyển dev.
