# Bảng đối chiếu điều kiện — VVTTGCT_05 (row 248) — Xuất Excel BC Vụ việc theo thời gian chi tiết

**Verdict:** Reject — lỗi "Không thể tạo file xuất" (ERR-RPT-04) KHÔNG tái hiện; hệ thống xuất file .xlsx thành công, nội dung đúng chuẩn TT17.

| Điều kiện có thể đổi kết quả | Đối tác (evidence full-res VVTTGCT_05.jpg) | Mình test (21/07/2026) | GAP? |
|---|---|---|:-:|
| Vai trò / tài khoản | Quản trị viên (QTHT) — góc phải màn hình | `cbnv_tw_01` (CB Nghiệp vụ TW — vai trò chuẩn ra verdict). Xuất thành công với vai trò nghiệp vụ đã bao phủ; QTHT quyền rộng hơn nên không thể là lý do đối tác lỗi mà mình pass | Không |
| Loại báo cáo | BC Vụ việc theo thời gian chi tiết | BC Vụ việc theo thời gian chi tiết | Không |
| Kỳ + khoảng thời gian | Năm — 01/01/2026 → 31/12/2026 | Năm — 01/01/2026 → 31/12/2026 | Không |
| Đơn vị (phạm vi) | Toàn quốc | Toàn quốc | Không |
| Dữ liệu tiền đề (phải có data mới bật nút Xuất) | Có data — đã Xem báo cáo ra biểu đồ stacked bar | Có data — kỳ 2026-01-01: Mới 1/Tiếp nhận 3/Đang hỗ trợ 6/Hoàn thành 5 (Tổng 17), đã Xem báo cáo trước khi Xuất | Không |
| Thao tác | Xuất Excel (.xlsx) | Xuất Excel (.xlsx) | Không |

**0 GAP.** `POST /api/v1/bao-cao/export` (formatXuat=XLSX, reqid=118) trả **200** + `content-disposition: attachment; filename="bao-cao-vu-viec-theo-tg-chi-tiet-2026-07-21.xlsx"`. Toast = "Đang tạo file...", KHÔNG phải ERR-RPT-04.

**Kiểm nội dung file (openpyxl):** header TT17 ĐỦ 4/4 (tiêu đề + Kỳ + Đơn vị: Toàn quốc + Ngày tạo: 21/07/2026) + bảng theo trạng thái khớp màn hình (2026-01-01: 1/3/6/5, Tổng 17). File gốc: `reverify-audit/_export-check/VVTTGCT_05.xlsx`.

**Lưu ý env:** đối tác test `htpldn-uat.ospgroup.vn`; QA verify `18.143.165.120.nip.io`. Lỗi không tái hiện → đề nghị đối tác kiểm tra lại.
