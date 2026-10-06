# QLDMTCTV_06 — dòng 319 (tab `UAT_TGPL Doanh Nghiệp-tuần 3`)

## Tuần

Tuần 3

## Mã TC

QLDMTCTV_06

## Mô tả

Kiểm tra các trường thông tin trên màn hình/popup thêm mới

## Điều kiện

1. Đăng nhập tài khoản

## Các bước thực hiện

1. Chọn menu "Mạng lưới tư vấn viên" => "Tổ chức tư vấn"
2. Nhấn "Thêm mới"

## Kết quả mong đợi

Hệ thống mở biểu mẫu Thêm ở chế độ nhập liệu mới, với các trường thông tin giống với thiết kế

## Kết quả thực tế

- Thiếu trường thông tin Số QĐ công bố, Ngày QĐ công bố, Tệp đính kèm

## Ảnh/vieo 1

QLDMTCTV_06.jpg

## Trạng thái 1

Fail

## Trạng thái dev fix 1

dev done

## Verify

Pass

## DEV phản hồi lần 1

Đã kiểm tra lại — lỗi đã được khắc phục, biểu mẫu Thêm mới của chức năng Tổ chức tư vấn nay đã có đủ các trường thông tin. Kiểm ở đúng vai trò Cán bộ Nghiệp vụ Trung ương và đúng đơn vị Bộ Tư pháp - Trung ương như trong ảnh đối tác gửi. Cả 3 trường đối tác báo thiếu đều đã xuất hiện:
• "Số quyết định công bố": ĐÃ CÓ, là ô nhập chữ.
• "Ngày quyết định công bố": ĐÃ CÓ, là ô chọn ngày có biểu tượng lịch.
• "Tệp đính kèm": ĐÃ CÓ, là vùng kéo thả tệp, cho phép tối đa 10 tệp với các định dạng .pdf, .doc, .docx, .xls, .xlsx và dung lượng tối đa 20MB mỗi tệp.
• Vị trí của 3 trường này: nằm ở phần cuối biểu mẫu, ngay bên dưới ô "Lĩnh vực pháp lý" và phía trên ô "Ghi chú", được tách thành hai mục có tiêu đề là "Công bố" và "Tệp đính kèm". Các trường này hiển thị sẵn ngay khi vừa mở biểu mẫu, không cần bấm mở thêm mục nào; chỉ cần cuộn xuống cuối biểu mẫu là thấy.
• Ngoài việc hiển thị, đội kiểm thử đã kiểm tra cả việc nhập và lưu: nhập số quyết định, chọn ngày quyết định và đính kèm một tệp PDF, sau đó bấm Lưu thì hệ thống tạo tổ chức thành công. Mở lại hồ sơ vừa tạo thì cả ba thông tin đều còn nguyên, kể cả tệp đính kèm, chứng tỏ dữ liệu được lưu thật chứ không chỉ hiện trên màn hình.
• Đội kiểm thử cũng đã rà soát toàn bộ biểu mẫu và đối chiếu với thiết kế: các trường còn lại đều đầy đủ, gồm Tên tổ chức, Loại hình, Người đại diện, Chức vụ đại diện, Số Giấy ĐKHĐ Sở TP, Ngày cấp, Số lao động, Địa chỉ, Điện thoại, Email, Website, Lĩnh vực pháp lý, Ghi chú, cùng hai nút Hủy và Lưu. Không còn trường nào bị thiếu.
• Verify: tài khoản Cán bộ Nghiệp vụ Trung ương (cbnv_tw_04), là vai trò trùng với ảnh đối tác gửi. Hồ sơ dùng để kiểm tra việc lưu dữ liệu là tổ chức TC-BTP-TW-0003 do đội kiểm thử tự tạo.
