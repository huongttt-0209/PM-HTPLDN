# Bảng đối chiếu điều kiện — VVTDVQL_07 (row 240) — Xuất PDF BC Vụ việc theo đơn vị quản lý

**Kết luận:** Open — ERR-RPT-04 KHÔNG tái hiện (Xuất PDF thành công, HTTP 200), NHƯNG file PDF thiếu 3/4 dòng header bắt buộc (Kỳ báo cáo / Đơn vị / Ngày tạo) — sai SRS `srs-fr-11-bao-cao.md:1088`. Bản Excel cùng báo cáo có đủ 4/4.

| Điều kiện có thể đổi kết quả | Đối tác (evidence `partner-evidence/VVTDVQL_07.jpg`) | Mình test (cbnv_tw, 21/07/2026) | GAP? |
|---|---|---|:-:|
| Vai trò / tài khoản | Quản trị viên (QTHT/admin) | cbnv_tw (CB Nghiệp vụ TW — đúng Tác nhân SRS) | Không |
| Entity + trạng thái | BC Vụ việc theo đơn vị quản lý có data | BC Vụ việc theo đơn vị quản lý có data (4 đơn vị) | Không |
| Dữ liệu tiền đề | Có vụ việc phân theo đơn vị quản lý | Có vụ việc: BKHĐT 4, Cục BTTP 8, An Giang 3, Hà Nội 2 | Không |
| Input / filter | loai=vu-viec-theo-don-vi, Năm 2026, Toàn quốc | loai=vu-viec-theo-don-vi, Năm 2026, Toàn quốc, filterDacThu rỗng | Không |
| Khổ giấy / hướng (chỉ ảnh hưởng PDF) | A4 mặc định | A4 / Dọc (portrait, dạng bảng) | Không |

**Artifact real-data:** file `vvtdvql_07.pdf` (PyMuPDF: chỉ "BC VỤ VIỆC THEO ĐƠN VỊ QUẢN LÝ" → vào thẳng bảng; "Kỳ báo cáo"/"Đơn vị:"/"Ngày tạo" = MISSING cả 3), ảnh so sánh `bug-reports/bctk/image/BUG-VVTDVQL-PDF-HEADER-compare.png`. Cùng lỗi template PDF dùng chung batch7/8 (BUG-EXPORT-PDF-HEADER).
