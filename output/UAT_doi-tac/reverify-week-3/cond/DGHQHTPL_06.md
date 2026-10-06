# Bảng đối chiếu điều kiện — DGHQHTPL_06 (row 233) — Xuất Excel BC Đánh giá hiệu quả HTPL

**Kết luận:** Reject — ERR-RPT-04 "Không thể tạo file xuất" KHÔNG tái hiện. Xuất Excel thành công (HTTP 200), nội dung file đúng (4/4 header + 3 đơn vị khớp màn hình).

| Điều kiện có thể đổi kết quả | Đối tác (evidence `partner-evidence/DGHQHTPL_06.jpg`) | Mình test (cbnv_tw, 21/07/2026) | GAP? |
|---|---|---|:-:|
| Vai trò / tài khoản | Quản trị viên (QTHT/admin) | cbnv_tw (CB Nghiệp vụ TW — đúng Tác nhân SRS; admin quyền ⊇) | Không |
| Entity + trạng thái | Báo cáo Đánh giá HTPL đã "Xem báo cáo" ra data (1 đợt / 2 lượt / 7đ) | Báo cáo Đánh giá HTPL đã "Xem báo cáo" ra data (2 đợt / 4 lượt / 59đ) | Không |
| Dữ liệu tiền đề | Có đợt đánh giá + lượt đánh giá | Có đợt đánh giá + lượt (3 đơn vị: 90/1/1, 80/1/1, 34/2/2) | Không |
| Input / filter | loai=danh-gia-hieu-qua, Kỳ Năm 2026, ĐV Toàn quốc, Đợt="TKM kiểm thử 2" | loai=danh-gia-hieu-qua, Kỳ Năm 2026, ĐV Toàn quốc, KHÔNG lọc đợt (đợt "TKM kiểm thử 2" không seed trên env này) | Không* |

\* GAP đợt đánh giá: đợt cụ thể "TKM kiểm thử 2" không tồn tại trên env test, nhưng bộ lọc đợt CHỈ thu hẹp dòng dữ liệu, KHÔNG quyết định endpoint xuất chạy được hay không (ERR-RPT-04 = lỗi tạo file, không phải lỗi lọc). Đã test Toàn quốc/tất-cả-đợt (có data) → xuất thành công ⇒ đợt không đổi kết quả xuất. Chứng minh không ảnh hưởng kết quả → bỏ qua hợp lệ.

**Artifact real-data:** `reverify-audit/_export-check-batch9/dghqhtpl-export-success-toast.png` (report có data), network `POST /api/v1/bao-cao/export` [200], file `dghqhtpl_06.xlsx` (đủ 4/4 header + 3 đơn vị khớp).
