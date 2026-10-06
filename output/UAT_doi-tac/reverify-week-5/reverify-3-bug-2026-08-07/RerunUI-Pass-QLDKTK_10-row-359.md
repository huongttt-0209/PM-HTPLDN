# Reverify UI - QLDKTK_10 (row 359)

- Ngày verify: 07/08/2026, 22:40–22:44 (Asia/Ho_Chi_Minh)
- Môi trường: `https://18.143.165.120.nip.io` — HTPLDN v1.0.10
- Công cụ thực thi: Chrome DevTools trên cửa sổ Chrome hiển thị
- Phạm vi: verify lại bug, không sửa source code, không chạy Playwright/curl/API trực tiếp
- Doanh nghiệp thử nghiệm: `Công ty QA UI Reverify 359 20260807`
- MST đăng nhập: `9908070802`
- Email: `qa.ui.rv359.20260807.02@htpldn.test`
- Mật khẩu: `[REDACTED]`
- Verdict: **PASS**

## Nội dung cần xác nhận

Doanh nghiệp vừa đăng ký nhưng chưa kích hoạt email phải bị chặn đăng nhập, vẫn ở trang `/login`, hiển thị đúng thông báo:

`Tài khoản đang chờ kích hoạt. Vui lòng kiểm tra email kích hoạt.`

Không được hiển thị dialog đăng nhập lần đầu hoặc chuyển vào dashboard.

## Các bước đã chạy qua UI

1. Mở trực tiếp trang `/register/doanh-nghiep` trên cửa sổ Chrome hiển thị.
2. Nhập đầy đủ dữ liệu doanh nghiệp mới, MST `9908070802`, email `qa.ui.rv359.20260807.02@htpldn.test` và mật khẩu hợp lệ.
3. Chọn loại doanh nghiệp `Công ty trách nhiệm hữu hạn`, tỉnh/thành `Hà Nội`, ngành nghề chính `Thương mại và dịch vụ`, quy mô `Nhỏ`.
4. Bấm `Đăng ký`. Khi hệ thống cảnh báo dữ liệu lao động/doanh thu/vốn gợi ý `Siêu nhỏ`, bấm đúng lựa chọn `Giữ lựa chọn của tôi`.
5. Mở MailHog bằng tab Chrome hiển thị, xác nhận email mới nhất có người nhận và tiêu đề đúng. Chỉ mở xem nội dung email, **không bấm link kích hoạt**.
6. Đăng xuất phiên người dùng cũ còn lưu từ case trước bằng menu UI và xác nhận `Đồng ý`.
7. Tại `/login`, nhập MST `9908070802` và mật khẩu vừa đăng ký rồi bấm `Đăng nhập`.
8. Lặp lại thao tác đăng nhập thêm một lần để xác nhận kết quả ổn định.

## Kết quả thực tế

- MailHog hiển thị email mới nhất gửi tới `qa.ui.rv359.20260807.02@htpldn.test`, tiêu đề `Kích hoạt tài khoản doanh nghiệp HTPLDN`.
- Nội dung email xác nhận doanh nghiệp `Công ty QA UI Reverify 359 20260807` đăng ký thành công và tên đăng nhập là MST `9908070802`.
- Không có thao tác bấm hoặc mở link kích hoạt trong toàn bộ luồng.
- Cả hai lần bấm `Đăng nhập`, trình duyệt đều giữ nguyên URL `https://18.143.165.120.nip.io/login`.
- Toast hiển thị chính xác: `Tài khoản đang chờ kích hoạt. Vui lòng kiểm tra email kích hoạt.`
- Không xuất hiện dialog đăng nhập lần đầu; không chuyển vào dashboard; không tạo phiên đăng nhập cho doanh nghiệp mới.
- Console chỉ ghi nhận request đăng nhập bị từ chối HTTP 401, phù hợp với việc tài khoản chưa kích hoạt bị chặn.

## Bằng chứng giao diện

Các ảnh chụp màn hình đã được chụp và hiển thị trực tiếp trong phiên Chrome DevTools tại các mốc:

1. Toàn bộ form đăng ký đã nhập dữ liệu, mật khẩu được che.
2. Modal `Quy mô không khớp với tiêu chí NĐ39/2018` với nút `Giữ lựa chọn của tôi`.
3. MailHog hiển thị email kích hoạt đúng người nhận và doanh nghiệp, không kích hoạt liên kết.
4. Trang `/login` sau khi bấm đăng nhập, hiển thị toast chờ kích hoạt và vẫn giữ MST trên form.

Chrome DevTools connector không cho lưu ảnh trực tiếp vào thư mục workspace do giới hạn workspace root, nên bằng chứng ảnh được giữ dưới dạng ảnh hiển thị trực tiếp trong phiên QA; accessibility snapshot lưu được nguyên văn URL và toast.

## Kết luận

**PASS**. Bug `QLDKTK_10` đã được fix theo luồng UI: tài khoản doanh nghiệp chưa kích hoạt không thể đăng nhập và nhận đúng thông báo BA yêu cầu.

> Không cập nhật Google Sheet trong bước này theo phân công của agent chính.
