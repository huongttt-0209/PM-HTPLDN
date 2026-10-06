# TPDBC_01 — dòng 316 (tab `UAT_TGPL Doanh Nghiệp-tuần 3`)

## Tuần

Tuần 3

## Mã TC

TPDBC_01

## Tên chức năng

Trình phê duyệt báo cáo đánh giá

## Mô tả

Cung cấp quy trình để CB Nghiệp vụ trình Lãnh đạo CQQLNN phê duyệt báo cáo đánh giá.

## Điều kiện

1. Đăng nhập tài khoản 
2. Đợt đánh giá ở trạng thái "Báo cáo".
3. Báo cáo đã được lưu

## Các bước thực hiện

1. Chọn menu "Đánh giá hiệu quả"
2. Mở Chi tiết đợt đánh giá (tab Báo cáo)
3. Nhấn "Trình phê duyệt báo cáo"

## Kết quả mong đợi

- Hệ thống hiển thị thông điệp "Đã trình phê duyệt báo cáo".
- Chuyển trạng thái đợt đánh giá từ "Báo cáo" sang "Chờ phê duyệt".
+ Gửi thông báo cho Cán bộ phê duyệt cùng đơn vị.
+ Lưu vết thao tác theo quy định.

## Kết quả thực tế

Cán bộ phê duyệt không nhận được thông báo

## Ảnh/vieo 1

TPDBC_01.webm

## Trạng thái 1

Fail

## Trạng thái dev fix 1

dev done

## Verify

Pass

## DEV phản hồi lần 1

☑️ Đã kiểm tra lại — chức năng hoạt động đúng, không còn lỗi.
- Chức năng "Trình phê duyệt báo cáo đánh giá" (UC 90) đã được QA tự chạy lại từ đầu trên bản hiện tại.
- Tiền đề đúng như phiếu: đợt đánh giá DG-20260725-0001 đang ở trạng thái "Lập báo cáo", báo cáo đã được lưu.
- Thao tác: mở Chi tiết đợt đánh giá, vào tab "Báo cáo", nhấn "Trình phê duyệt", xác nhận ở hộp thoại "Trình phê duyệt báo cáo?".
- Hệ thống hiện thông điệp "Đã trình phê duyệt" và chuyển đợt từ "Lập báo cáo" sang "Chờ phê duyệt".
- Ngay sau đó, kiểm tra ở phía Cán bộ phê duyệt cùng đơn vị (cùng cấp Trung ương với người trình): chuông thông báo có mục mới "Báo cáo đánh giá chờ phê duyệt - DG-20260725-0001", nội dung ghi rõ mã kế hoạch và tên đợt đánh giá, kèm lời nhắc đăng nhập để xem xét phê duyệt. Số thông báo chưa đọc tăng thêm 1.
- Đã kiểm tra trên hai tài khoản Cán bộ phê duyệt khác nhau cùng đơn vị, cả hai đều nhận được thông báo này.
- Kết luận: đúng như kết quả mong đợi của phiếu, hệ thống có gửi thông báo cho Cán bộ phê duyệt cùng đơn vị.
