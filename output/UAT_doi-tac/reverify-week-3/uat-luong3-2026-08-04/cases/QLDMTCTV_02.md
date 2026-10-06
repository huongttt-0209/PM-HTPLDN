# QLDMTCTV_02 — dòng 317 (tab `UAT_TGPL Doanh Nghiệp-tuần 3`)

## Tuần

Tuần 3

## Mã TC

QLDMTCTV_02

## Mô tả

Kiểm tra hiển thị Cột dữ liệu trong bảng kết quả

## Điều kiện

1. Đăng nhập tài khoản

## Các bước thực hiện

1. Chọn menu "Mạng lưới tư vấn viên" => "Tổ chức tư vấn"

## Kết quả mong đợi

- Hệ thống hiển thị các trường thông tin giống với thiết kế
- Dữ liệu hiển thị đúng định dạng và trường thông tin
- Dữ liệu hiển thị không bị tràn/đè lên nhau, đồng nhất ngôn ngữ hiển thị

## Kết quả thực tế

Thiếu ô chọn và trường STT

## Ảnh/vieo 1

QLDMTCTV_02.jpg

## Trạng thái 1

Fail

## Trạng thái dev fix 1

dev done

## Verify

Pass

## DEV phản hồi lần 1

Đã kiểm tra lại — lỗi đã được khắc phục, chức năng Quản lý Tổ chức tư vấn hiển thị đúng.
• Vào Mạng lưới Tư vấn viên > Tổ chức tư vấn, bảng danh sách nay ĐÃ CÓ ô tích chọn ở đầu mỗi dòng (kèm ô tích chọn tất cả trên hàng tiêu đề) và ĐÃ CÓ cột STT đánh số theo trang (1, 2, 3...). Đây đúng là 2 mục đối tác phản ánh còn thiếu.
• Kiểm tra thêm toàn bộ các cột còn lại của bảng: Mã tổ chức, Tên tổ chức, Loại hình, Lĩnh vực, Người đại diện, Trạng thái, Công khai, Hành động — đều hiển thị đầy đủ, đúng định dạng, không tràn chữ, không đè chữ, ngôn ngữ thống nhất tiếng Việt.
• Ô tích chọn dùng được thật, không chỉ hiển thị: chọn nhiều dòng ở thẻ "Đang hoạt động" thì hiện thanh thao tác hàng loạt kèm nút Công khai / Hủy công khai; ở thẻ "Chờ phê duyệt" (vai trò Cán bộ Phê duyệt) thì hiện nút Phê duyệt hàng loạt.
• Đã kiểm tra ở cả 3 vai trò (Quản trị viên, Cán bộ Nghiệp vụ Trung ương, Cán bộ Phê duyệt Trung ương) và ở tất cả các thẻ trạng thái, kết quả giống nhau. Với thẻ chưa có dữ liệu, đội kiểm thử đã tự tạo thêm tổ chức tư vấn để kiểm tra chứ không bỏ qua.
• Riêng thẻ "Chờ phê duyệt" chỉ hiện với vai trò Cán bộ Phê duyệt, các vai trò khác không thấy — đây là đúng thiết kế, không phải thiếu chức năng.
• Verify: tài khoản Cán bộ Nghiệp vụ Trung ương (cbnv_tw_04), đối chiếu thêm bằng tài khoản Quản trị viên và Cán bộ Phê duyệt Trung ương (cbpd_tw_04); dữ liệu kiểm thử gồm 3 tổ chức có sẵn và 1 tổ chức tự tạo (TC-BTP-TW-0001).
