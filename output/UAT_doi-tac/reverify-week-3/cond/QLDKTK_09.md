# Bảng đối chiếu điều kiện — QLDKTK_09

Loại bug: **Đăng ký tài khoản doanh nghiệp → đối tác báo "hệ thống không gửi liên kết kích hoạt đến email".** Verdict phụ thuộc: sau khi đăng ký thành công, hệ thống có phát email chứa link kích hoạt hay không.

| Điều kiện có thể đổi kết quả | Đối tác | Mình test | GAP? |
|---|---|---|:-:|
| Vai trò | Khách chưa đăng nhập (tự đăng ký DN) | Khách chưa đăng nhập (tự đăng ký DN `/register/doanh-nghiep`) | Không |
| Màn hình / thao tác | Màn "Đăng ký tài khoản doanh nghiệp" → điền đủ → Đăng ký → chờ mail kích hoạt | Cùng màn → điền đủ → Đăng ký → kiểm tra mail hệ thống phát | Không |
| Dữ liệu tiền đề (MST + email) | MST mới + email mới chưa tồn tại | MST mới `7712349980` + email mới `qa_reg_email_0721@example.com` (đều chưa tồn tại) | Không |
| Trạng thái sau đăng ký | Đăng ký thành công → TK CHO_KICH_HOAT | Đăng ký thành công (API 201) → TK `CHO_KICH_HOAT` | Không |

**Kết luận: KHÔNG tái hiện.** Trên bản kiểm thử hiện tại (2026-07-21): đăng ký DN mới → API `POST /auth/register-doanh-nghiep` trả **201** (message "Vui lòng kiểm tra email để kích hoạt tài khoản"); ngay sau đó hệ thống **CÓ phát email** "Kích hoạt tài khoản doanh nghiệp HTPLDN" tới đúng email đăng ký, trong nội dung có **liên kết kích hoạt** `.../auth/verify-email?token=470405f7-...`; mở liên kết → API `verify-email` trả **200**, tài khoản chuyển `HOAT_DONG`. Hành vi "không gửi liên kết" KHÔNG xảy ra → **Reject**. Bằng chứng: `QLDKTK_09-mailhog-activation-email-sent.png` (email + link) + network 201/200.

> Ghi chú nội bộ (không đưa vào note đối tác): kênh nhận mail của môi trường được giao khác kênh đối tác dùng; ở đây chỉ khẳng định điều SRS FR-VIII-22 §Processing bước 10 yêu cầu — HỆ THỐNG có phát email link kích hoạt — là ĐÚNG trên bản hiện tại. Việc thư tới được hộp thư người dùng cuối phụ thuộc hạ tầng nhận mail (spam/SMTP) phía đối tác, không phải lỗi ứng dụng.
