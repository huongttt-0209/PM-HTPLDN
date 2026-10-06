# Condition table — BUG-EM-TK-018 (R3)

| Điều kiện | Thao tác | Kỳ vọng | Thực tế | Kết quả |
|---|---|---|---|---|
| QTHT `admin`; tài khoản DN `0109998887`, entity `996cc5db-43c5-4903-b3d1-1c21adb2ece8`, số điện thoại ban đầu `0912345678`, version 127 | Sửa số điện thoại thành `0912345679` trên form tài khoản | API cập nhật thành công và sinh audit `TAI_KHOAN / UPDATE` | `PUT /api/v1/tai-khoan/{id}` trả 200, version 128; audit `0648f3de-b0d7-48c7-a137-76b3702b089d` được tạo lúc `2026-08-25T04:21:01.361Z` | PASS |
| Audit mới sau cập nhật | Gọi `GET /api/v1/audit-logs/0648f3de-b0d7-48c7-a137-76b3702b089d` | Có dữ liệu cũ và mới để đối chiếu JSON diff | `duLieuCu.dienThoai=0912345678`; `duLieuMoi.dienThoai=0912345679`; hai object đều có đủ email, họ tên, đơn vị và loại tài khoản | PASS |
| Kết thúc kiểm tra | Hoàn nguyên số điện thoại | Trả fixture về dữ liệu ban đầu | `PUT` hoàn nguyên trả 200, `dienThoai=0912345678`, version 129 | PASS |

**Kết luận:** PASS — audit của thao tác sửa tài khoản đã lưu đồng thời `duLieuCu` và `duLieuMoi`, thể hiện đúng thay đổi old → new.

**Evidence:** [Audit detail API](../bug-report/image/bug-em-tk-018-r3-audit-old-new-diff-2026-08-25.png) — SHA-256 `27c71d8ee2e57e5915a37f9ad2b52b4abec433ba2d9426925d98bb7922663de8`.
