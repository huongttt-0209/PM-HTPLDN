# Reverify UI - QLNDTVVCG_OOS_01 (row 358)

- Ngày verify: 07/08/2026
- Môi trường: `https://18.143.165.120.nip.io`
- Công cụ thực thi: Chrome DevTools trên cửa sổ Chrome hiển thị
- Phạm vi: verify lại bug, không sửa source code, không gọi API trực tiếp
- Tài khoản: `qa_tvvseed28` (mật khẩu và OTP đã ẩn)
- Dữ liệu kiểm thử: `TVCS-20260806-0003`
- Verdict: **PASS**

## Nội dung BA cần xác nhận

Khi chuyên gia từ chối nhiệm vụ, hệ thống phải:

1. Hiển thị đúng thông báo `Đã từ chối yêu cầu tư vấn`.
2. Chuyển người dùng về trang danh sách tư vấn chuyên sâu.

## Các bước đã chạy qua UI

1. Đăng nhập tài khoản chuyên gia trên giao diện web.
2. Mở OTP mới nhất của đúng người nhận qua giao diện MailHog và hoàn tất xác thực trên giao diện web.
3. Chọn menu `Tư vấn` > `Tư vấn chuyên sâu`.
4. Tại tab `Chờ xử lý`, mở bản ghi `TVCS-20260806-0003` đang ở trạng thái `Đã phân công` cho `QA TVV Seed28 Active`.
5. Nhấn `Từ chối nhiệm vụ`.
6. Nhập lý do `Rerun UI Chrome DevTools row 358 - không phù hợp chuyên môn` (59 ký tự, lớn hơn tối thiểu 10 ký tự).
7. Nhấn xác nhận `Từ chối`.

## Kết quả thực tế

- Hệ thống trả về danh sách tại URL `https://18.143.165.120.nip.io/tv-chuyen-sau/danh-sach`.
- Snapshot Chrome ngay sau thao tác hiển thị chính xác toast: `Đã từ chối yêu cầu tư vấn`.
- Bản ghi `TVCS-20260806-0003` không còn xuất hiện trong tab `Chờ xử lý` của chuyên gia; danh sách chỉ còn `TVCS-20260805-0001`.
- DevTools Network ghi nhận chính thao tác phát sinh từ UI hoàn tất thành công với HTTP 200 và dữ liệu trả về đưa yêu cầu về trạng thái tiếp nhận, bỏ chuyên gia đã từ chối.

## Bằng chứng giao diện

Các ảnh chụp màn hình đã được chụp và hiển thị trực tiếp trong phiên Chrome DevTools ở các mốc:

1. Tab `Chờ xử lý` có `TVCS-20260806-0003` trước thao tác.
2. Trang chi tiết có nút `Từ chối nhiệm vụ`.
3. Modal `Từ chối nhiệm vụ?` trước và sau khi nhập lý do.
4. Trang danh sách sau thao tác, `TVCS-20260806-0003` đã rời khỏi tab `Chờ xử lý`.

Chrome DevTools không cho lưu ảnh vào thư mục workspace do giới hạn workspace root của connector, nên bằng chứng ảnh được giữ dưới dạng ảnh hiển thị trực tiếp trong phiên QA; snapshot accessibility lưu được nguyên văn toast và URL chuyển trang.

## Kết luận

**PASS**. Hành vi sau khi chuyên gia từ chối khớp nội dung BA chốt: đúng toast `Đã từ chối yêu cầu tư vấn` và chuyển về danh sách.

> Không cập nhật Google Sheet trong bước này theo phân công của agent chính.
