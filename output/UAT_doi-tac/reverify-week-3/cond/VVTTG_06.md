# Bảng đối chiếu điều kiện — VVTTG_06 (row 217) — Xuất PDF BC Vụ việc theo thời gian

**Verdict:** Reject — lỗi "Không thể tạo file xuất" (ERR-RPT-04) KHÔNG tái hiện; hệ thống xuất file .pdf thành công.

| Điều kiện có thể đổi kết quả | Đối tác (evidence full-res VVTTG_06.jpg) | Mình test (21/07/2026) | GAP? |
|---|---|---|:-:|
| Vai trò / tài khoản | Quản trị viên (QTHT) — góc phải màn hình | `cbnv_tw_05` (CB Nghiệp vụ TW — vai trò chuẩn ra verdict, có quyền xem + xuất BC). QTHT quyền rộng hơn, không thể là lý do đối tác lỗi mà mình pass | Không |
| Loại báo cáo | BC Vụ việc theo thời gian | BC Vụ việc theo thời gian | Không |
| Kỳ + khoảng thời gian | Năm — 01/01/2026 → 31/12/2026 | Năm — 01/01/2026 → 31/12/2026 | Không |
| Đơn vị (phạm vi) | Cục Bổ trợ tư pháp - Bộ Tư pháp (BTP-TW), donViId ...0001 | Đúng đơn vị BTP-TW (donViId ...0001 khớp URL đối tác) | Không |
| Dữ liệu tiền đề (phải có data mới bật nút Xuất) | Có data — Tổng vụ việc toàn kỳ = 1 | Có data — BTP-TW = 3 (đã Xem báo cáo ra kết quả trước khi Xuất) | Không |
| Thao tác | Xuất PDF (.pdf) → dialog chọn khổ giấy A4/hướng Dọc → Xuất file | Xuất PDF (.pdf) → dialog A4/Dọc → Xuất file | Không |

**0 GAP.** Đối tác báo lỗi cụ thể (ERR-RPT-04 khi Xuất PDF) — verify đúng điều kiện, lỗi KHÔNG tái hiện: `POST /api/v1/bao-cao/export` (formatXuat=PDF, khoGiay=A4, huongGiay=portrait) trả 200 + `content-type: application/pdf` + `content-disposition: attachment; filename="bao-cao-vu-viec-theo-thoi-gian-2026-07-21.pdf"` (body = binary file) — reqid=112.

**Lưu ý env:** đối tác test trên `htpldn-uat.ospgroup.vn`; QA verify trên `18.143.165.120.nip.io`. Lỗi không tái hiện → đề nghị đối tác kiểm tra lại.
