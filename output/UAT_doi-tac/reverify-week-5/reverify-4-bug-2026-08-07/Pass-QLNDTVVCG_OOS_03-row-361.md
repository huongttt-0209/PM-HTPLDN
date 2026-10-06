# Re-verify bug QLNDTVVCG_OOS_03 — dòng 361

- Môi trường: `https://18.143.165.120.nip.io` — HTPLDN v1.0.10
- Thời điểm: 07/08/2026 21:51–21:55 (Asia/Ho_Chi_Minh)
- Tài khoản phân công: `cbnv_tw_01`
- Chuyên gia nhận: `qa_tvvseed28`
- Bản ghi: `TVCS-20260805-0001`
- Verdict: **PASS**

## Căn cứ chấm

BA/SRS yêu cầu bước phân công chuyên gia gửi đủ hai kênh **in-app + email**, nội dung phải nêu yêu cầu và SLA 2 ngày làm việc.

## Luồng đã chạy

1. Ghi MailHog baseline ngay trước thao tác: `total = 1936`.
2. Dùng `cbnv_tw_01` mở bản ghi trạng thái `Tiếp nhận`, chọn `QA TVV Seed28 Active`, ghi chú `QA reverify row 361 - kiem in-app va email`, rồi xác nhận phân công.
3. Đọc MailHog ngay sau thao tác.
4. Đăng nhập đúng tài khoản `qa_tvvseed28`, mở chuông thông báo và đọc thông báo vừa sinh.

## Kết quả

- **Email đạt:** MailHog tăng `1936 → 1937` đúng thời điểm phân công `2026-08-07T14:52:51.966Z`; người nhận `qa.tvvseed28@htpldn-uat.local`; tiêu đề `Bạn được phân công tư vấn: TVCS-20260805-0001`.
- Nội dung email có mã yêu cầu, tiêu đề yêu cầu và câu `Vui lòng xác nhận nhận việc trong 2 ngày làm việc, quá hạn hệ thống sẽ tự thu hồi phân công.`
- **In-app đạt:** chuông thông báo của chính `qa_tvvseed28` có bản tin loại `PHAN_CONG`, tiêu đề `Bạn được phân công tư vấn: TVCS-20260805-0001`, nội dung bắt đầu bằng mã và yêu cầu tương ứng.
- Email OTP đăng nhập chuyên gia sinh sau đó làm tổng thư tăng tiếp lên `1938`; đã tách riêng và không dùng làm bằng chứng nghiệp vụ.

## Bằng chứng

- `image/361-before-phan-cong.png`: modal phân công đúng CG, hiển thị email và SLA 2 ngày.
- `image/361-in-app-notification.png` và `image/361-in-app-notification-panel.png`: thông báo in-app của CG có đúng mã bản ghi.
- `image/361-email-mailhog.png`: email nghiệp vụ đầy đủ tiêu đề, người nhận, nội dung và SLA.

## Cập nhật Sheet

- Dòng: 361
- `Trạng thái dev fix`: `Test done`
- Không ghi `Kết quả verify` vì verdict Pass.
