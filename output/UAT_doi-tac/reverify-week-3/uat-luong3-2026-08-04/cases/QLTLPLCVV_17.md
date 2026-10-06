# QLTLPLCVV_17 — dòng 326 (tab `UAT_TGPL Doanh Nghiệp-tuần 3`)

## Tuần

Tuần 3

## Mã TC

QLTLPLCVV_17

## Mô tả

Xem tệp trực tuyến

## Điều kiện

1. Đăng nhập hệ thống thành công

## Các bước thực hiện

1. Chọn menu "Tư vấn" => "Tư vấn chuyên sâu"
2. Nhấn "Xem chi tiết" tại bản ghi
3. Mở Nhóm 3 — Tư liệu pháp lý liên kết
4. Bấm vào tên tệp đính kèm,

## Kết quả mong đợi

Hệ thống mở trình xem trực tuyến cho định dạng hỗ trợ (PDF, hình ảnh). Định dạng không hỗ trợ xem trực tuyến, hệ thống tải tệp về máy người dùng.

## Kết quả thực tế

Hệ thống disable nút chức năng Xem

## Ảnh/vieo 1

QLTLPLCVV_17_v2.jpg

## Trạng thái 1

Fail

## Trạng thái dev fix 1

dev done

## Verify

Pass

## DEV phản hồi lần 1

Đã kiểm tra lại — lỗi đã được khắc phục, nút "Xem" tệp trong mục Tư liệu pháp lý liên kết của Tư vấn chuyên sâu nay bấm được bình thường. Kiểm ở đúng vai trò Cán bộ Nghiệp vụ Trung ương và đúng đơn vị Bộ Tư pháp - Trung ương như trong ảnh đối tác gửi, trên tư liệu đã ở trạng thái Đã công khai giống hệt ảnh.
- Nút "Xem" hiển thị bình thường, không còn bị làm mờ và không còn bị vô hiệu hóa; bấm vào có phản hồi ngay.
- Với tệp Word (đuôi .docx) giống tệp trong ảnh đối tác gửi: hệ thống tải tệp về máy, mở ra đọc được đầy đủ nội dung, không phải tệp rỗng hay tệp hỏng.
- Với tệp PDF: hệ thống mở trình xem trực tuyến và hiển thị đúng nội dung bên trong tệp.
- Với tệp hình ảnh: hệ thống mở khung xem ảnh và hiển thị đúng ảnh, đúng kích thước gốc.
- Đội kiểm thử không chỉ dừng ở chỗ "cửa sổ có mở ra" mà đã mở từng tệp đọc lại nội dung để chắc chắn tệp hiện ra thật.
- Đã kiểm thêm ở vai trò Chuyên gia được phân công phụ trách nội dung tư vấn đó: chuyên gia xem và tải được tệp bình thường ở chế độ chỉ đọc, đúng như quy định về phân quyền.
- Đã tải lại trang và kiểm lại lần cuối trên bản phần mềm đang chạy để chắc chắn kết quả không phải do trang cũ còn lưu trên trình duyệt.
