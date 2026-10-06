# QLDMTCTV_OOS_04 — dòng 330 (tab `UAT_TGPL Doanh Nghiệp-tuần 3`)

## Tuần

Tuần 3

## Mã TC

QLDMTCTV_OOS_04

## Mô tả

Danh sách Tổ chức tư vấn — thẻ trạng thái không có bản ghi thì không hiển thị số đếm "0"

## Điều kiện

1. Đăng nhập tài khoản Cán bộ Nghiệp vụ cấp Trung ương (cbnv_tw_04), đơn vị Cục Bổ trợ tư pháp - Bộ Tư pháp.
2. Chọn menu "Mạng lưới Tư vấn viên" -> "Tổ chức tư vấn".

## Dữ liệu đầu vào

Các thẻ "Đã từ chối", "Tạm dừng", "Vô hiệu hóa" hiện chưa có tổ chức nào.

## Các bước thực hiện

1. Quan sát thanh thẻ trạng thái.
2. Đọc huy hiệu số đếm của từng thẻ.
3. Đối chiếu thẻ có bản ghi với thẻ chưa có bản ghi.

## Kết quả mong đợi

Màn hình SCR-IV-NEW-01 quy định mọi thẻ trạng thái đều thuộc loại "tab + số đếm" (dòng 1625 đến 1630), và dòng 1650 ghi rõ phần phân trang phải "hiển thị tổng mỗi tab". Vậy thẻ chưa có bản ghi vẫn phải hiển thị số 0.

## Kết quả thực tế

Các thẻ chưa có bản ghi ("Đã từ chối", "Tạm dừng", "Vô hiệu hóa") không hiển thị huy hiệu nào, kể cả số 0. Chỉ thẻ có bản ghi mới hiện số.
Hệ quả: người dùng không phân biệt được "mục này đang có 0 hồ sơ" với "phần mềm chưa làm số đếm cho thẻ này".

## Ảnh/vieo 1

QLDMTCTV_05-cbpd-tw-04-thanh-the-co-cho-phe-duyet.png

## Trạng thái 1

Fail

## Trạng thái dev fix 1

Reject

## Verify

Reject

## DEV phản hồi lần 1

- Vì đặc tả không quy định trường hợp bằng 0 nên không trích được điều khoản nào bị vi phạm ⇒ đóng dòng này, không chuyển dev và cũng không cần BA quyết.
- Đã gỡ khỏi file gửi BA (ba-confirmation-needed-luong4-to-chuc-tu-van-2026-08-03.md). Bản ghi P/Q/R trước khi sửa lưu tại reverify-audit/BACKUP-sheet-tuan3-rows-330-331-332-339-truoc-khi-sua-2026-08-03.json.
- Kiểm bằng vai trò Cán bộ Nghiệp vụ Trung ương (cbnv_tw_04) và Cán bộ Phê duyệt Trung ương (cbpd_tw_04), bản dựng HTPLDN V1.0.5.
