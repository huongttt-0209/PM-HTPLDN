# QLDMTCTV_OOS_07 — dòng 333 (tab `UAT_TGPL Doanh Nghiệp-tuần 3`)

## Tuần

Tuần 3

## Mã TC

QLDMTCTV_OOS_07

## Mô tả

Danh sách Tổ chức tư vấn — màn hình rỗng chỉ hiện chữ "Trống", thiếu câu hướng dẫn theo đặc tả

## Điều kiện

1. Đăng nhập tài khoản Cán bộ Nghiệp vụ cấp Trung ương (cbnv_tw_04), đơn vị Cục Bổ trợ tư pháp - Bộ Tư pháp.
2. Chọn menu "Mạng lưới Tư vấn viên" -> "Tổ chức tư vấn".

## Dữ liệu đầu vào

Thẻ "Đã từ chối" chưa có tổ chức nào (thẻ "Tạm dừng" và "Vô hiệu hóa" cũng vậy).

## Các bước thực hiện

1. Bấm vào thẻ "Đã từ chối".
2. Đọc nội dung hiển thị ở vùng bảng khi không có bản ghi.
3. Lặp lại với thẻ "Tạm dừng" và "Vô hiệu hóa".

## Kết quả mong đợi

Màn hình SCR-IV-NEW-01 dòng 1649 quy định khi thẻ không có bản ghi thì hiển thị hình minh họa kèm câu "Chưa có tổ chức tư vấn nào trong mục này", và có nút "+ Thêm tổ chức tư vấn" ở thẻ "Mới đăng ký".

## Kết quả thực tế

Vùng bảng chỉ hiện hình minh họa kèm đúng một chữ "Trống" — là chữ mặc định của thư viện giao diện, không phải câu tiếng Việt mà đặc tả yêu cầu. Không có câu hướng dẫn nào cho người dùng.
Đã kiểm ở thẻ "Đã từ chối"; thẻ "Tạm dừng" và "Vô hiệu hóa" hiển thị y hệt.

## Ảnh/vieo 1

QLDMTCTV_OOS-man-rong-hien-chu-Trong-thay-vi-cau-huong-dan.png

## Trạng thái 1

Fail

## Trạng thái dev fix 1

dev done

## Verify

Pass

## DEV phản hồi lần 1

- Phần chữ đã sửa đúng: cả 3 thẻ rỗng (Đã từ chối, Tạm dừng, Vô hiệu hóa) nay hiện câu "Chưa có tổ chức tư vấn nào trong mục này", không còn chữ "Trống".
- Còn lại: hình minh họa ở vùng rỗng nay không còn nữa. Vùng rỗng chỉ có đúng một dòng chữ, trong khi Kết quả mong đợi của phiếu yêu cầu "hình minh họa kèm câu ...". Trước lần sửa này hình minh họa vẫn hiển thị, nên đây là điểm mới phát sinh.
- Theo màn hình SCR-IV-NEW-01 (dòng 1649), trạng thái rỗng gồm cả phần hình và phần chữ hướng dẫn, không phải chỉ một trong hai.
- Riêng nút "+ Thêm tổ chức tư vấn" ở thẻ "Mới đăng ký" chưa kiểm được lần này vì thẻ đó đang có dữ liệu nên không rơi vào trạng thái rỗng.
- Đã kiểm bằng vai trò Cán bộ Nghiệp vụ Trung ương, đơn vị Cục Bổ trợ tư pháp, ngày 04/08/2026, bản dựng V1.0.5.
