# Sao lưu nguyên văn dòng 124 — CNDSMLTVV_01 (trước vòng 2)

## STT

(trống)

## Tuần

Tuần 2

## Mã TC

CNDSMLTVV_01

## Tên chức năng

Cập nhật danh sách mạng lưới tư vấn viên

## Tác nhân

Cán  bộ  nghiệp  vụ 
 TW,BN,ĐP

## Mô tả

Thực hiện cập nhật danh sách các tư vấn viên đã được phê duyệt lên Cổng công khai.

## Điều kiện

1. Đăng nhập tài khoản 
2. Hồ sơ đang ở trạng thái "Đang hoạt động" và chưa được công khai

## Dữ liệu đầu vào

(trống)

## Các bước thực hiện

1. Chọn menu "Mạng lướt tư vấn viên" -> "Tư vấn viên/Chuyên gia"
2. Tích chọn các ứng viên hợp lệ
3. Nhấn "Công khai hàng loạt" và Xác nhận

## Kết quả mong đợi

- Hệ thống hiển thị cửa sổ nhập mô tả công khai (bắt buộc) áp cho các tư vấn viên đã chọn và xác nhận "Công khai {N} tư vấn viên đã chọn lên Cổng pháp luật quốc gia?"
- Lưu mô tả công khai, đặt cờ công khai, chuyển trạng thái công khai, ghi thời điểm.

## Kết quả thực tế

Hệ thống không mở cửa sổ nhập mà hiển thị thông báo "Mô tả công khai là bắt buộc trước khi đẩy lên Cổng pháp luật quốc gia"

## Ảnh/vieo 1

CNDSMLTVV_01.jpg

## Trạng thái 1

Fail

## TKM phản hồi lần 1

(trống)

## Trạng thái dev fix 1

dev done

## Verify

Pass

## DEV phản hồi lần 1

☑️ Đã kiểm tra lại — chức năng chạy đúng.
- Kiểm tra lại bằng vai trò Cán bộ Nghiệp vụ Trung ương, đúng tiền đề của phiếu: chọn các tư vấn viên đang ở trạng thái "Đang hoạt động" và chưa được công khai.
- Chọn 2 tư vấn viên rồi bấm "Công khai lên Cổng PLQG": hệ thống MỞ cửa sổ nhập như mong đợi, tiêu đề "Công khai hàng loạt lên Cổng PLQG", kèm đúng câu xác nhận "Công khai 2 tư vấn viên đã chọn lên Cổng pháp luật quốc gia?".
- Trong cửa sổ có ô "Mô tả công khai" gắn dấu bắt buộc, giới hạn 5000 ký tự.
- Nếu để trống mô tả rồi bấm "Công khai": hệ thống báo lỗi ngay tại ô nhập ("Vui lòng nhập mô tả công khai") và giữ nguyên cửa sổ, không gửi dữ liệu đi. Đây là chỗ khác với lần bên kiểm thử gặp: thông báo thiếu mô tả nay nằm trong cửa sổ nhập, không còn bắn ra ngoài màn danh sách.
- Nhập mô tả rồi bấm "Công khai": lưu thành công, thông báo "Đã công khai tư vấn viên thành công", cả 2 hồ sơ chuyển từ "Chưa công khai" sang "Công khai".
- Kiểm tra thêm ở màn chi tiết tư vấn viên: nút công khai cũng mở đúng cửa sổ nhập, có thêm phần đính kèm tệp và tự điền lại mô tả đã nhập trước đó.
- Chức năng Cập nhật danh sách mạng lưới tư vấn viên (UC46) hiện hoạt động bình thường. Đề nghị bên kiểm thử xác nhận lại trên bản mới nhất.
- Verify: tài khoản Cán bộ Nghiệp vụ Trung ương, bản dựng V1.0.5, ngày 03/08/2026.

## Kết quả thực tế lần 2

(trống)

## Ảnh/video 2

(trống)

## Trạng thái 2

(trống)

## TKM phản hồi lần 2

(trống)

## Trạng thái dev fix 2

(trống)

## Verify 2

(trống)

## DEV phản hồi lần 2

(trống)
