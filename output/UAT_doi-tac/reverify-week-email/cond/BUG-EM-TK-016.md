# Condition table — BUG-EM-TK-016 (R3)

| Điều kiện | Thao tác | Kỳ vọng | Thực tế | Kết quả |
|---|---|---|---|---|
| QTHT; DN tự đăng ký `0108172026` ở `CHO_KICH_HOAT`; mailbox baseline 2 | Bấm Gửi lại email kích hoạt | Sinh đúng 1 thư mới | UI báo thành công; mailbox 2 → 3; thư lúc `04:16:58Z` | PASS |
| Mở thư mới nhất | Kiểm URL | Dùng `/auth/verify-email?token=...` | URL là `/auth/verify-email?token=305dc571-...` | PASS |
| Cùng nội dung thư | Kiểm hướng dẫn sau kích hoạt | Không yêu cầu đặt mật khẩu lần đầu; dùng mật khẩu đã đặt khi đăng ký | Nội dung ghi đăng nhập bằng mật khẩu đã đặt khi đăng ký | PASS |
| Cùng thư | Tìm `/auth/first-login-password` | Không được xuất hiện | Không xuất hiện | PASS |

**Kết luận:** PASS — resend activation cho DN đã sinh đúng verify-email link.

**Evidence:** [MailHog API message](../bug-report/image/bug-em-tk-016-r3-verify-email-link-2026-08-25.png) — SHA-256 `a3804d04f0fb5c4318513361cceceb7b45ad4cfd0165dd070a27d72176907368`.
