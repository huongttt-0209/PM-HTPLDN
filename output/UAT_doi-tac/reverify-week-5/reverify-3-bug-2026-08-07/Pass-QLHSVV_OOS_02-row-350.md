# Reverify bug QLHSVV_OOS_02 - dòng 350

- Ngày chạy: 07/08/2026
- Môi trường: `https://18.143.165.120.nip.io`
- Tài khoản: bộ tài khoản 01, vai trò Cán bộ Nghiệp vụ Trung ương
- Cách chạy: Chrome DevTools trên cửa sổ Chrome hiển thị; không dùng Playwright, curl hoặc gọi API nghiệp vụ trực tiếp
- Vụ việc kiểm tra: `VV-BTP-TW-20260803-002`
- Verdict: **Pass**

## Nội dung BA cần xác nhận

1. Cột `Loại` của tài liệu phải dùng một trong 6 loại giấy tờ NĐ55, không dùng nhóm thời điểm `Yêu cầu` / `Bổ sung`.
2. Form `Thêm tài liệu` phải cho chọn loại giấy tờ.
3. Hai tệp khác nhau có thể hiển thị hai nhãn loại khác nhau.
4. Đối chiếu với 6 hạng mục trên form `Kiểm tra hồ sơ`.

## Các bước và kết quả thực tế

1. Vào `Vụ việc HTPL`, tìm mã `VV-BTP-TW-20260803-002` và mở chi tiết.
   - UI tìm thấy đúng một kết quả, trạng thái `Đã tiếp nhận`.
2. Mở nhóm `Tài liệu đính kèm`.
   - Dữ liệu ban đầu có tệp `QLHSVV_07_qa.jpg` với `Loại = Khác`.
   - Không còn hiển thị nhãn sai `Yêu cầu` hoặc `Bổ sung`.
3. Bấm `Thêm tài liệu`, mở combobox `Loại giấy tờ`.
   - UI hiển thị đúng 6 lựa chọn:
     - `Văn bản đề nghị (Mẫu 01)`
     - `Giấy chứng nhận đăng ký kinh doanh`
     - `Tờ khai quy mô doanh nghiệp`
     - `Hợp đồng tư vấn pháp luật`
     - `Văn bản tư vấn pháp luật`
     - `Khác`
4. Chọn `Văn bản đề nghị (Mẫu 01)`, đưa tệp kiểm thử `row350-van-ban-de-nghi.pdf` vào form và bấm `Tải lên` trên UI.
   - UI báo `Đã tải lên 1 tệp`.
   - Bảng tài liệu cập nhật ngay trên giao diện và hiển thị hai dòng:
     - `row350-van-ban-de-nghi.pdf` -> `Văn bản đề nghị (Mẫu 01)`
     - `QLHSVV_07_qa.jpg` -> `Khác`
   - Hai tệp có hai nhãn loại khác nhau, đúng điều kiện BA.
5. Bấm `Kiểm tra hồ sơ`.
   - Form hiển thị `Checklist Mẫu 01 NĐ55 (6 hạng mục)` gồm Văn bản đề nghị, Giấy CNĐKKD, Tờ khai quy mô DN, Hợp đồng dịch vụ TVPL và hai hạng mục Văn bản TVPL.

## Kết luận

Bug đã được fix thành công. Cột `Loại`, form thêm tài liệu và checklist đều theo nhóm giấy tờ NĐ55; hai tệp khác nhau hiển thị được hai nhãn loại khác nhau. Đề xuất ghi `Trạng thái dev fix = Test done`.

## Ghi chú môi trường

- Ảnh màn hình đã được chụp và hiển thị trực tiếp qua Chrome DevTools cho các trạng thái: danh sách vụ việc, bảng tài liệu, danh sách 6 loại giấy tờ, form kiểm tra hồ sơ và bảng hai nhãn sau upload. Chrome DevTools MCP không cho lưu ảnh vào workspace do giới hạn configured workspace roots.
- Khi thử reload sau khi đã ghi nhận đầy đủ kết quả, gateway trả HTTP 502. Sự cố phát sinh sau toast upload thành công và sau khi bảng đã hiển thị hai dòng, không làm thay đổi verdict của bug này.
