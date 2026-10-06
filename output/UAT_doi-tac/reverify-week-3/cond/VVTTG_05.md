# Bảng đối chiếu điều kiện — VVTTG_05 (row 216) — Xuất Excel BC Vụ việc theo thời gian

**Verdict:** Reject — lỗi "Không thể tạo file xuất" (ERR-RPT-04) KHÔNG tái hiện; hệ thống xuất file .xlsx thành công.

| Điều kiện có thể đổi kết quả | Đối tác (evidence full-res VVTTG_05.jpg) | Mình test (21/07/2026) | GAP? |
|---|---|---|:-:|
| Vai trò / tài khoản | Quản trị viên (QTHT) — góc phải màn hình | `cbnv_tw_05` (CB Nghiệp vụ TW — vai trò chuẩn ra verdict, có quyền xem + xuất BC). Export là chức năng tạo file dùng chung; xuất thành công với vai trò nghiệp vụ → bao phủ. QTHT quyền rộng hơn, không thể là lý do đối tác lỗi mà mình pass | Không |
| Loại báo cáo | BC Vụ việc theo thời gian | BC Vụ việc theo thời gian | Không |
| Kỳ + khoảng thời gian | Năm — 01/01/2026 → 31/12/2026 | Năm — 01/01/2026 → 31/12/2026 | Không |
| Đơn vị (phạm vi) | Cục Bổ trợ tư pháp - Bộ Tư pháp (BTP-TW), donViId ...0001 | Đã test CẢ Toàn quốc VÀ đúng đơn vị BTP-TW (donViId ...0001 khớp URL đối tác) | Không |
| Dữ liệu tiền đề (phải có data mới bật nút Xuất) | Có data — Tổng vụ việc toàn kỳ = 1 | Có data — Toàn quốc = 6, BTP-TW = 3 (đều đã Xem báo cáo ra kết quả trước khi Xuất) | Không |
| Thao tác | Xuất Excel (.xlsx) | Xuất Excel (.xlsx) | Không |

**0 GAP.** Đối tác báo lỗi cụ thể (ERR-RPT-04 khi Xuất Excel) — verify đúng điều kiện, lỗi KHÔNG tái hiện: `POST /api/v1/bao-cao/export` (formatXuat=XLSX) trả 200 + `content-type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet` + `content-disposition: attachment; filename="bao-cao-vu-viec-theo-thoi-gian-2026-07-21.xlsx"` (body = binary file). Reproduce cả Toàn quốc (reqid=97) và đúng đơn vị BTP-TW (reqid=108).

**Lưu ý env:** đối tác test trên `htpldn-uat.ospgroup.vn`; QA verify trên env được giao `18.143.165.120.nip.io`. Lỗi không tái hiện trên env QA → khả năng lỗi transient/đã fix ở env đối tác → đề nghị đối tác kiểm tra lại.
