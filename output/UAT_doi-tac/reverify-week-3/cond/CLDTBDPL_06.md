# Bảng đối chiếu điều kiện — CLDTBDPL_06 (row 237) — Xuất Excel BC Chất lượng đào tạo

**Kết luận:** Reject — ERR-RPT-04 "Không thể tạo file xuất" KHÔNG tái hiện. Xuất Excel thành công (HTTP 200), nội dung file đúng (4/4 header + 4 khóa học khớp màn hình).

| Điều kiện có thể đổi kết quả | Đối tác (evidence `partner-evidence/CLDTBDPL_06.jpg`) | Mình test (cbnv_tw, 21/07/2026) | GAP? |
|---|---|---|:-:|
| Vai trò / tài khoản | Quản trị viên (QTHT/admin) | cbnv_tw (CB Nghiệp vụ TW — đúng Tác nhân SRS; admin quyền ⊇) | Không |
| Entity + trạng thái | BC Chất lượng đào tạo đã "Xem báo cáo" ra data | BC Chất lượng đào tạo đã "Xem báo cáo" ra data (4 khóa học) | Không |
| Dữ liệu tiền đề | Có khóa đào tạo + học viên | Có 4 khóa (AAA-KH-DP, AAA-KH-BN, KH-SEED-0001, AAA-KH-TW) | Không |
| Input / filter | loai=chat-luong-dao-tao, Kỳ Năm 2026, ĐV Toàn quốc | loai=chat-luong-dao-tao, Kỳ Năm 2026, ĐV Toàn quốc, filterDacThu rỗng | Không |

**Artifact real-data:** `reverify-audit/_export-check-batch9/cldtbdpl-excel-success-toast.png` (report có data), network `POST /api/v1/bao-cao/export` [200], file `cldtbdpl_06.xlsx` (đủ 4/4 header: `BC Chất lượng đào tạo` · `Kỳ báo cáo: Năm (từ 01/01/2026 đến 31/12/2026)` · `Đơn vị: Toàn quốc` · `Ngày tạo: 21/07/2026` + 4 dòng khóa học khớp màn hình).
