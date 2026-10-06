# Condition table — BUG-EM-TK-013 (R3)

| Điều kiện | Thao tác | Kỳ vọng | Thực tế | Kết quả |
|---|---|---|---|---|
| QTHT; `0409998821` ban đầu `HOAT_DONG` | Khóa tài khoản trên UI | Chuyển `TAM_KHOA`, thu hồi phiên | UI báo thành công; dòng tài khoản và tab hiển thị `Tạm khóa 1` | PASS |
| MailHog recipient baseline 7 thư lúc `04:13:54Z`; tài khoản đang `TAM_KHOA` | Gửi Quên mật khẩu bằng TAI_KHOAN.email (kiểm 2 lần) | Không sinh reset token/email | API 400 `ERR-PWD-02`; MailHog vẫn 7 thư lúc `04:15:44Z`, latest không đổi từ 24/08 | PASS |
| Tài khoản vẫn `TAM_KHOA` | Đăng nhập bằng mật khẩu đúng | Không được vào OTP/session | API login 401; UI báo `Tài khoản đã bị tạm khóa...` | PASS |
| Kết thúc kiểm tra | QTHT bấm Mở khóa | Trả fixture về trạng thái ban đầu | UI trở lại `Hoạt động`; tab Tạm khóa về 0 | PASS |

**Kết luận:** PASS — tài khoản bị QTHT tạm khóa không thể tự đi qua luồng reset mật khẩu hoặc đăng nhập; trạng thái không tự mở.

**Evidence:**

- [Quên mật khẩu bị chặn](../bug-report/image/bug-em-tk-013-r3-forgot-password-blocked-2026-08-25.png) — SHA-256 `745cb920262d8172b0bd4868bc61221acd6ef84f815fa249213fa88f04eb7cbc`.
- [Đăng nhập bị chặn](../bug-report/image/bug-em-tk-013-r3-locked-account-login-blocked-2026-08-25.png) — SHA-256 `a8921f26d920ea8aa59d2c8f7fded9e560a4e26d67206a8fdadda5aad0c6e2ac`.
