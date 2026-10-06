# QLDMTCTV_09 — dòng 320 (tab `UAT_TGPL Doanh Nghiệp-tuần 3`)

## Tuần

Tuần 3

## Mã TC

QLDMTCTV_09

## Mô tả

Kiểm tra các trường thông tin trên màn hình/popup sửa

## Điều kiện

1. Đăng nhập tài khoản

## Các bước thực hiện

1. Chọn menu "Mạng lưới tư vấn viên" => "Tổ chức tư vấn"
2. Nhấn Sửa

## Kết quả mong đợi

- Hệ thống mở biểu mẫu ở chế độ chỉnh sửa, điền sẵn thông tin hiện có.
- Dữ liệu hiển thị đúng định dạng và trường thông tin
- Dữ liệu hiển thị không bị tràn/đè lên nhau, đồng nhất ngôn ngữ hiển thị

## Kết quả thực tế

- Thiếu trường thông tin Số QĐ công bố, Ngày QĐ công bố, Tệp đính kèm

## Ảnh/vieo 1

QLDMTCTV_09.jpg

## Trạng thái 1

Fail

## Trạng thái dev fix 1

dev done

## Verify

Pass

## DEV phản hồi lần 1

Đã kiểm tra lại — lỗi đã được khắc phục, biểu mẫu ở chế độ Sửa của chức năng Tổ chức tư vấn nay đã có đủ các trường thông tin. Kiểm ở đúng vai trò Cán bộ Nghiệp vụ Trung ương và đúng đơn vị Bộ Tư pháp - Trung ương như trong ảnh đối tác gửi. Cả 3 trường đối tác báo thiếu đều đã xuất hiện:
• "Số quyết định công bố": ĐÃ CÓ, là ô nhập chữ.
• "Ngày quyết định công bố": ĐÃ CÓ, là ô chọn ngày có biểu tượng lịch.
• "Tệp đính kèm": ĐÃ CÓ, là vùng kéo thả tệp, cho phép tối đa 10 tệp với các định dạng .pdf, .doc, .docx, .xls, .xlsx và dung lượng tối đa 20MB mỗi tệp.
• Vị trí của 3 trường này: nằm ở phần cuối biểu mẫu, ngay bên dưới ô "Lĩnh vực pháp lý" và phía trên ô "Ghi chú", được tách thành hai mục có tiêu đề là "Công bố" và "Tệp đính kèm". Chúng hiển thị sẵn ngay khi vừa bấm Sửa, không cần bấm mở thêm mục nào; chỉ cần cuộn xuống cuối biểu mẫu là thấy.
• Đội kiểm thử đã lưu ý một khả năng dễ gây hiểu nhầm và đã kiểm riêng: nếu hệ thống chỉ hiện 3 trường này khi hồ sơ đã có sẵn dữ liệu, thì hồ sơ cũ mở ra vẫn sẽ thiếu, đúng như đối tác phản ánh. Vì vậy đã mở chế độ Sửa trên nhiều hồ sơ khác nhau để đối chiếu.
• Kết quả: đã kiểm trên 4 hồ sơ thuộc 3 trạng thái khác nhau. Ba hồ sơ CHƯA từng có dữ liệu ở 3 trường này, gồm cả một hồ sơ cũ có sẵn trong hệ thống từ trước chứ không phải do đội kiểm thử tạo, là "Trung tâm Tư vấn Pháp luật Seed" (đang hoạt động), TC-BTP-TW-0002 (mới đăng ký) và TC-BTP-TW-0001 (chờ phê duyệt). Một hồ sơ ĐÃ có sẵn dữ liệu là TC-BTP-TW-0003 (mới đăng ký). Cả 4 hồ sơ đều hiển thị đầy đủ 3 trường, nên biểu mẫu Sửa không phụ thuộc vào việc hồ sơ đã có dữ liệu hay chưa, cũng không thay đổi theo trạng thái hồ sơ.
• Ngoài việc hiển thị, đã kiểm cả việc nhập và lưu ngay trên một hồ sơ vốn đang để trống cả 3 trường (TC-BTP-TW-0002): nhập số quyết định, chọn ngày quyết định và đính kèm một tệp PDF, bấm Lưu thì hệ thống báo cập nhật thành công. Tải lại trang rồi mở lại thì cả ba thông tin đều còn nguyên, kể cả tệp đính kèm với đúng tên tệp và dung lượng, chứng tỏ dữ liệu được lưu thật chứ không chỉ hiện trên màn hình.
• Về yêu cầu biểu mẫu phải điền sẵn thông tin hiện có: đã đối chiếu từng trường trên cả 4 hồ sơ, các thông tin đang có của hồ sơ đều được điền sẵn đúng, ngày hiển thị đúng dạng ngày/tháng/năm, danh mục hiển thị đúng nhãn tiếng Việt, tệp đính kèm hiển thị đúng tên và dung lượng kèm nút Xem và Xóa. Các ô để trống đều là những thông tin hồ sơ thật sự chưa có. Bố cục không bị tràn hay đè chữ, toàn bộ ngôn ngữ hiển thị là tiếng Việt.
• Đã rà soát toàn bộ biểu mẫu Sửa và đối chiếu với thiết kế: các trường còn lại đều đầy đủ, gồm Tên tổ chức, Loại hình, Người đại diện, Chức vụ đại diện, Số Giấy ĐKHĐ Sở TP, Ngày cấp, Số lao động, Địa chỉ, Điện thoại, Email, Website, Lĩnh vực pháp lý, Ghi chú, cùng hai nút Hủy và Lưu. Không còn trường nào bị thiếu.
• Verify: tài khoản Cán bộ Nghiệp vụ Trung ương (cbnv_tw_04), là vai trò trùng với ảnh đối tác gửi.
