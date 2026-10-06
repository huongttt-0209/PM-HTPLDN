# Condition table — BUG-EM-TK-007 (R3)

| Điều kiện | Thao tác | Kỳ vọng | Thực tế | Kết quả |
|---|---|---|---|---|
| Tài khoản DN `0127000002` ở `CHO_KICH_HOAT`; dùng link mới nhất `first-login-password` | Mở link và đặt mật khẩu hợp lệ | Đặt một lần thành công | UI báo `Đặt mật khẩu thành công`, chuyển về đăng nhập | PASS |
| Cùng chính xác token đã dùng | Mở lại URL | Không hiện form; báo link đã sử dụng và hướng dẫn xin link mới | Chỉ hiện alert `Link đặt mật khẩu đã được sử dụng`, có link `yêu cầu link mới` và `đăng nhập` | PASS |
| Sau lần dùng đầu | GET `/auth/first-login-password/validate` | Nhận diện lý do USED | 200, `valid=false`, `reason=USED` | PASS |
| Link đã dùng | Quan sát trang | Không tạo form/session mới hay cho submit lần hai | Không có form mật khẩu hoặc nút submit | PASS |

**Kết luận:** PASS — link một lần dùng đã được nhận diện đúng và UI hiển thị đúng ERR-PWD-04.

**Evidence:** [Thông báo link đã sử dụng](../bug-report/image/bug-em-tk-007-r3-used-link-message-2026-08-25.png) — SHA-256 `08f565cb99adbcdf1b96921460e57b1e56517c6d948a5f95ca089a9afc58f389`.
