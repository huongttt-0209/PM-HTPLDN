# Re-verify bug QLDKTK_10 — dòng 359

- Môi trường: `https://18.143.165.120.nip.io` — HTPLDN v1.0.10
- Thời điểm: 07/08/2026 21:56–22:01 (Asia/Ho_Chi_Minh)
- Doanh nghiệp thử nghiệm: `Công ty QA Reverify 359 20260807`
- MST đăng nhập: `9908070801`
- Email: `qa.rv359.20260807.01@htpldn.test`
- Verdict: **PASS**

## Phạm vi bug

Reverify đúng bug OOS tại dòng 359: doanh nghiệp vừa đăng ký nhưng **chưa kích hoạt email** không được phép đăng nhập. Không dùng case gốc trùng mã TC ở dòng 169.

## Luồng đã chạy

1. Đăng ký mới tài khoản doanh nghiệp bằng dữ liệu hợp lệ.
2. API đăng ký trả `201`, trạng thái tài khoản `CHO_KICH_HOAT` và yêu cầu kiểm tra email kích hoạt.
3. Xác nhận MailHog đã nhận đúng một email kích hoạt cho địa chỉ thử nghiệm, nhưng **không mở và không bấm link kích hoạt**.
4. Tại trang đăng nhập, nhập MST và mật khẩu vừa đăng ký rồi bấm `Đăng nhập`.

## Kết quả

- Hệ thống chặn đăng nhập tại `/login`; không sinh access token và không đi vào ứng dụng.
- API `POST /api/v1/auth/login` trả `401`, mã lỗi `ERR-AUTH-LOGIN-02`.
- Thông báo hiển thị/capture từ DOM: `Tài khoản đang chờ kích hoạt. Vui lòng kiểm tra email kích hoạt.`
- Trạng thái trả ngay từ API đăng ký là `CHO_KICH_HOAT`; không có thao tác kích hoạt nào được thực hiện trong toàn bộ luồng.

## Bằng chứng

- `359-register-response.txt`: request đăng ký trả `201`; response xác nhận `CHO_KICH_HOAT`.
- `359-unactivated-login-response.txt`: request đăng nhập trả `401`.
- `image/359-after-register-login-page.png`: sau đăng ký hệ thống chuyển về màn hình đăng nhập.
- `image/359-before-unactivated-login.png`: thử đăng nhập bằng tài khoản vừa tạo, chưa kích hoạt.
- `image/359-unactivated-login-blocked.png`: vẫn ở màn hình đăng nhập sau khi bị chặn.

## Cập nhật Sheet

- Dòng: 359
- `Trạng thái dev fix`: `Test done`
- Không ghi `Kết quả verify` vì verdict Pass.
