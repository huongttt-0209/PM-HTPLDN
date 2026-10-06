# Bảng đối chiếu điều kiện — VVTLV_06 (row 244) — Xuất PDF BC Vụ việc theo lĩnh vực

**Verdict:** Open — lỗi "Không thể tạo file xuất" (ERR-RPT-04) KHÔNG tái hiện (file PDF tải về được), NHƯNG nội dung file PDF **thiếu 3/4 trường header bắt buộc** (Kỳ báo cáo / Đơn vị / Ngày tạo) theo SRS `srs-fr-11-bao-cao.md:1088` → BUG-EXPORT-PDF-HEADER.

| Điều kiện có thể đổi kết quả | Đối tác (evidence full-res VVTLV_06.jpg) | Mình test (21/07/2026) | GAP? |
|---|---|---|:-:|
| Vai trò / tài khoản | Quản trị viên (QTHT) — góc phải màn hình | `cbnv_tw_01` (CB Nghiệp vụ TW — vai trò chuẩn ra verdict, có quyền xem + xuất BC) | Không |
| Loại báo cáo | BC Vụ việc theo lĩnh vực | BC Vụ việc theo lĩnh vực | Không |
| Kỳ + khoảng thời gian | Năm — 01/01/2026 → 31/12/2026 | Năm — 01/01/2026 → 31/12/2026 | Không |
| Đơn vị (phạm vi) | Toàn quốc | Toàn quốc | Không |
| Dữ liệu tiền đề (phải có data mới bật nút Xuất) | Có data — đã Xem báo cáo trước | Có data — Thuế 1 + Thương mại 16 (Tổng 17), đã Xem báo cáo trước khi Xuất | Không |
| Thao tác | Xuất PDF (.pdf) | Xuất PDF (.pdf), khổ A4 + hướng Dọc (mặc định) | Không |

**0 GAP.** `POST /api/v1/bao-cao/export` (formatXuat=PDF, khoGiay=A4, huongGiay=portrait, reqid=100) trả **200** + `content-type: application/pdf` + `content-disposition: attachment; filename="bao-cao-vu-viec-theo-linh-vuc-2026-07-21.pdf"`. Toast = "Đang tạo file..." (không có ERR-RPT-04).

**Kiểm nội dung file (PyMuPDF):** file A4 (210×297mm) + font Tinos (Times New Roman-tương thích) cỡ 13 → 2/2 yêu cầu định dạng SRS đạt; số liệu đúng (Thuế 1, Thương mại 16). NHƯNG dòng đầu chỉ có tiêu đề "BC VỤ VIỆC THEO LĨNH VỰC" rồi vào thẳng bảng — **KHÔNG có** khối header Kỳ báo cáo / Đơn vị / Ngày tạo. Bản Excel cùng báo cáo (VVTLV_05.xlsx) có đủ 4 trường → chứng minh BE có sẵn dữ liệu header, lỗi ở nhánh dựng PDF. File gốc: `reverify-audit/_export-check/VVTLV_06.pdf`; ảnh render: `bug-reports/bctk/image/VVTLV_06-pdf-no-header.png`.

**Lưu ý env:** đối tác test `htpldn-uat.ospgroup.vn` (báo lỗi ERR-RPT-04 không tạo được file); QA verify `18.143.165.120.nip.io` (file tạo được nhưng thiếu header). Lỗi tạo-file của đối tác không tái hiện; lỗi thiếu-header là lỗi khác (SRS-based) → Open + chuyển dev.
