# Bảng đối chiếu điều kiện — CLDTBDPL_07 (row 238) — Xuất PDF BC Chất lượng đào tạo

**Kết luận:** Open — ERR-RPT-04 KHÔNG tái hiện (Xuất PDF thành công, HTTP 200), NHƯNG file PDF thiếu 3/4 dòng header bắt buộc (Kỳ báo cáo / Đơn vị / Ngày tạo) — sai SRS `srs-fr-11-bao-cao.md:1088`. Bản Excel cùng báo cáo có đủ 4/4.

| Điều kiện có thể đổi kết quả | Đối tác (evidence `partner-evidence/CLDTBDPL_07.jpg`) | Mình test (cbnv_tw, 21/07/2026) | GAP? |
|---|---|---|:-:|
| Vai trò / tài khoản | Quản trị viên (QTHT/admin) | cbnv_tw (CB Nghiệp vụ TW — đúng Tác nhân SRS) | Không |
| Entity + trạng thái | BC Chất lượng đào tạo có data | BC Chất lượng đào tạo có data (4 khóa học) | Không |
| Dữ liệu tiền đề | Có khóa đào tạo + học viên | Có 4 khóa (AAA-KH-DP, AAA-KH-BN, KH-SEED-0001, AAA-KH-TW) | Không |
| Input / filter | loai=chat-luong-dao-tao, Năm 2026, Toàn quốc | loai=chat-luong-dao-tao, Năm 2026, Toàn quốc, filterDacThu rỗng | Không |
| Khổ giấy / hướng (chỉ ảnh hưởng PDF) | A4 mặc định | A4 / Dọc (portrait, dạng bảng) | Không |

**Artifact real-data:** file `cldtbdpl_07.pdf` (PyMuPDF: chỉ "BC CHẤT LƯỢNG ĐÀO TẠO" → vào thẳng bảng; "Kỳ báo cáo"/"Đơn vị:"/"Ngày tạo" = MISSING), ảnh so sánh `bug-reports/bctk/image/BUG-CLDTBDPL-PDF-HEADER-compare.png`. Cùng lỗi template PDF dùng chung batch7/8 (BUG-EXPORT-PDF-HEADER).
