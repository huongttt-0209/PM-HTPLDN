# Reverify bug KTHSYCHTPL_QA01 - dòng 364

- Ngày chạy: 07/08/2026
- Môi trường: `https://18.143.165.120.nip.io`
- Cách chạy: Chrome DevTools trên cửa sổ Chrome hiển thị; toàn bộ bước đăng nhập, lấy OTP trên MailHog, mở vụ việc và đọc timeline đều thực hiện qua UI
- Dữ liệu kiểm tra: `VV-STP-AG-20260806-001`
- Đơn vị quản lý: `Sở Tư pháp An Giang`
- Verdict: **Pass**

## Điều kiện xác nhận

Hai cán bộ nghiệp vụ cùng vai trò, cùng đơn vị phải xem được đầy đủ cùng một lịch sử sự kiện của vụ việc; timeline không được lọc theo người đang đăng nhập/người đã tạo sự kiện.

## Các bước và kết quả thực tế

1. Đăng nhập bằng tài khoản `cbnv_dp_01` qua màn hình đăng nhập và nhập OTP đọc trực tiếp trên giao diện MailHog.
2. Vào `Vụ việc HTPL`, mở `VV-STP-AG-20260806-001`.
   - Vụ việc hiển thị trạng thái `Đã phân công`.
   - Khối `Phân công Người hỗ trợ / Tư vấn viên` hiển thị `Đơn vị quản lý = Sở Tư pháp An Giang`, `NHT/TVV phụ trách = QA NHT An Giang UAT2`, trạng thái phân công `Chờ xác nhận`, thời điểm `06/08/2026 13:25`.
   - `Dòng thời gian` hiển thị đủ 3 sự kiện, thứ tự mới nhất trước:
     - `Phân công` — `06/08/2026 13:25` — `CB Nghiệp vụ - Địa phương #01`
     - `Kiểm tra` — `06/08/2026 13:23` — `CB Nghiệp vụ - Địa phương #01`
     - `Tạo vụ việc` — `06/08/2026 13:20` — `CB Nghiệp vụ - Địa phương #01`
3. Đăng xuất bằng UI, đăng nhập tài khoản `cbnv_dp_02` qua UI và OTP MailHog, sau đó vào lại cùng vụ việc.
   - Tài khoản #02 thấy vụ việc trong danh sách và mở được chi tiết, xác nhận không có lỗi quyền truy cập.
   - Khối phân công vẫn hiển thị đúng `Sở Tư pháp An Giang`, `QA NHT An Giang UAT2`, `Chờ xác nhận`, `06/08/2026 13:25`.
   - Timeline của tài khoản #02 hiển thị đúng cùng 3 sự kiện, cùng thứ tự, tên sự kiện, thời điểm và tác nhân như tài khoản #01.

## Kết luận

Bug đã được fix thành công. Cán bộ nghiệp vụ #02 cùng đơn vị vẫn xem được toàn bộ lịch sử do cán bộ #01 tạo; hệ thống không còn lọc timeline theo người đang đăng nhập. Đề xuất ghi `Trạng thái dev fix = Test done`.

## Ghi chú bằng chứng

- Đã chụp ảnh toàn trang trực tiếp qua Chrome DevTools ở cả hai phiên đăng nhập; ảnh thể hiện đồng thời khối phân công và đủ ba dòng timeline.
- Không cần seed dữ liệu bằng API vì dữ liệu tiền đề đã tồn tại và dùng được.
- Không dùng API để đọc/so sánh timeline hoặc đưa ra verdict.
