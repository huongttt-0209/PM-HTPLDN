# Condition table — BUG-EM-DN-005 (R3)

| Điều kiện | Điều kiện gốc | Thực tế reverify 2026-08-25 | GAP |
|---|---|---|---|
| Trạng thái tài khoản | `CHO_KICH_HOAT` | Tài khoản `0127000002` (`3499f94a-6075-4174-9cf2-2d92ddd13cdf`) vẫn ở `CHO_KICH_HOAT` | Không |
| Thư kích hoạt ban đầu | Có một thư sau khi Claim | MailHog có thư “Kích hoạt tài khoản doanh nghiệp HTPLDN” lúc `2026-08-24T10:53:35.885Z` | Không |
| Gửi lại lần hai | Phải phát sinh thêm thư, không báo thành công giả | MailHog có thư thứ hai “Kích hoạt tài khoản hệ thống HTPLDN (gửi lại)” lúc `2026-08-24T10:57:23.991Z` | Không |
| Token mới | Lần gửi lại phải sinh token mới | Token gửi lại `cc0c2cbf-baae-4afe-9baa-9bded7eac625`, khác token của thư đầu | Không |
| Bản ghi được cập nhật | Lần gửi lại phải tạo thay đổi phía hệ thống | `version = 2`, `ngayCapNhat = 2026-08-24T10:57:23.917Z`, trùng thời điểm thư gửi lại | Không |
| Môi trường | DEV | `https://18.143.165.120.nip.io`, UI v1.0.16; MailHog `http://18.143.165.120:8025` | Không |

**Kết luận:** PASS — tài khoản Chờ kích hoạt đã nhận được thư kích hoạt thứ hai với token mới; triệu chứng “màn hình báo gửi nhưng không có thư” không còn tái hiện.

**Ghi chú kiểm thử:** endpoint Quên mật khẩu đang bị rate-limit theo môi trường trong phiên R3, vì vậy verdict được đối chiếu trên fixture post-fix gần nhất bằng API tài khoản và MailHog trực tiếp.
