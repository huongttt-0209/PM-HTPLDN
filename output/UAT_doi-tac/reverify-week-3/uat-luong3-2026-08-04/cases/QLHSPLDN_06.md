# QLHSPLDN_06 — dòng 324 (tab `UAT_TGPL Doanh Nghiệp-tuần 3`)

## Tuần

Tuần 3

## Mã TC

QLHSPLDN_06

## Mô tả

Xem

## Điều kiện

1. Đăng nhập hệ thống thành công

## Các bước thực hiện

1. Chọn menu "Doanh nghiệp"
2. Nhấn "Xem chi tiết"
3. Chọn thẻ "Hồ sơ pháp lý doanh nghiệp"
4. Nhấn "Xem"

## Kết quả mong đợi

Hệ thống mở cửa sổ chi tiết hiển thị toàn bộ thông tin của hồ sơ và danh sách tệp đính kèm (nếu có) ở chế độ chỉ đọc.

## Kết quả thực tế

Màn hình không có nút chức năng xem chi tiết

## Ảnh/vieo 1

QLHSPLDN_06.jpg

## Trạng thái 1

Fail

## Trạng thái dev fix 1

dev done

## Verify

Pass

## DEV phản hồi lần 1

Đã kiểm tra lại — lỗi đã được khắc phục, thẻ "Hồ sơ pháp lý" trong màn Chi tiết doanh nghiệp nay đã có nút xem chi tiết trên từng dòng hồ sơ. Kiểm ở đúng vai trò Cán bộ Nghiệp vụ Trung ương và đúng phạm vi Bộ Tư pháp - Trung ương như trong ảnh đối tác gửi, theo đúng 4 bước của phiếu kiểm thử.
• Cột "Hành động" của mỗi dòng hồ sơ hiện có đủ 3 nút: "Xem" (kèm biểu tượng con mắt), "Sửa" và "Xoá". Ảnh đối tác gửi chỉ có 2 nút Sửa và Xoá — nay đã bổ sung nút Xem.
• Bấm "Xem" thì hệ thống mở đúng cửa sổ "Chi tiết hồ sơ pháp lý" như mong đợi, hiển thị đầy đủ: Mã hồ sơ, Tên hồ sơ, Loại hồ sơ, Lĩnh vực pháp lý, Nguồn, Cơ quan cấp, Ngày cấp, Ngày hết hạn, Trạng thái, Mô tả, cùng mục "Tệp đính kèm" liệt kê tên tệp và dung lượng kèm hai nút Xem và Tải, và nút Đóng.
• Cửa sổ chi tiết đúng là chế độ chỉ đọc: không có ô nhập liệu nào trong cửa sổ, người dùng chỉ xem chứ không sửa được.
• Nút "Xem" dùng được thật chứ không phải bị mờ hay khoá: không bị vô hiệu hoá, bấm là mở ngay.
• Đội kiểm thử đã lưu ý một khả năng dễ gây hiểu nhầm và đã kiểm riêng: nút có thể chỉ hiện ở một số trạng thái hồ sơ nhất định. Vì môi trường kiểm thử ban đầu chỉ có hồ sơ ở trạng thái "Hiệu lực", đội kiểm thử đã tự tạo thêm hồ sơ cho hai trạng thái còn lại rồi kiểm lại. Kết quả: đã kiểm trên 6 hồ sơ thuộc đủ cả 3 trạng thái "Hiệu lực", "Hết hạn" và "Thu hồi" — cả 6 hồ sơ đều có nút Xem. Vậy nút không phụ thuộc trạng thái hồ sơ.
• Cũng đã kiểm cả hồ sơ có tệp đính kèm lẫn hồ sơ không có tệp: cả hai trường hợp đều mở được cửa sổ chi tiết bình thường.
• Đã kiểm thêm khả năng nút bị cuộn ngang che khuất: bảng có thanh cuộn ngang, nhưng cột "Hành động" là cột được ghim cố định bên phải nên luôn hiển thị, không thể bị che. Trong ảnh đối tác gửi, cột này cũng hiện đầy đủ.
• Xác nhận thêm: phản ánh của đối tác là chính xác đối với bản phần mềm tại thời điểm đó — bản đó thật sự không có nút xem chi tiết, và cũng không bấm được vào dòng để mở. Đây không phải do thao tác nhầm.
• Verify: tài khoản Cán bộ Nghiệp vụ Trung ương (cbnv_tw_04), là vai trò trùng với ảnh đối tác gửi. Doanh nghiệp dùng để kiểm tra là "Cong ty TNHH QA UAT Kiem Thu" (mã DN-HNI-0001), trong đó 2 hồ sơ trạng thái "Hết hạn" và "Thu hồi" do đội kiểm thử tự tạo để kiểm đủ các trạng thái.
