# Re-verify UI - CBKQDTBD_OOS_01 (dòng 347)

> **Đã được thay thế ngày 2026-08-07:** Sau khi seed dữ liệu điều kiện và verify lại hoàn toàn qua Chrome UI, verdict hiện tại là **PASS**. Xem `Pass-CBKQDTBD_OOS_01-row-347.md`. Nội dung bên dưới được giữ lại làm lịch sử blocker dữ liệu ban đầu.

- Ngày chạy: 2026-08-07
- Môi trường: `https://18.143.165.120.nip.io`
- Tài khoản: `cbnv_tw_01` (bộ 01)
- Phương thức: Chrome DevTools trên cửa sổ Chrome hiển thị; OTP lấy qua giao diện MailHog hiển thị
- Kết luận: **BLOCKED - chưa đủ điều kiện kết luận Pass/Reopen**

## Phạm vi cần xác minh

Khóa học `KH-20260703-005` (`test thêm mới khóa học`), đối chiếu cột **Đơn vị** trên ba tab **Học viên**, **Kết quả**, **Công bố kết quả**:

- Hoàng Minh Đức (`hoangminhduc@gmail.com`): phải trống hoặc `-` nhất quán trên cả ba tab.
- `tester tkm`: phải hiển thị `TKM` nhất quán trên cả ba tab.

## Các bước đã thực hiện qua UI

1. Đăng nhập thành công bằng `cbnv_tw_01`; hoàn tất OTP trên giao diện ứng dụng, mã OTP được đọc trực tiếp từ giao diện MailHog.
2. Mở menu **Đào tạo, tập huấn > Khóa học**.
3. Tại tab **Tất cả**, tìm chính xác mã `KH-20260703-005`.
4. Hệ thống trả về **Không có khóa học nào phù hợp.**
5. Bấm **Làm mới** trên UI, kết quả vẫn không đổi.
6. Xóa điều kiện tìm kiếm rồi tìm theo tên `test thêm mới khóa học`; hệ thống cũng trả về **Không có khóa học nào phù hợp.**
7. Kiểm tra thêm tab **Hủy** với tên khóa học; không có kết quả.
8. Thử dataset đối chứng được nêu trong kết quả bug gốc: tìm chính xác `KH-20260509-006` ở tab **Tất cả**; hệ thống tiếp tục hiển thị **Không có khóa học nào phù hợp.**
9. Với cùng bộ lọc `KH-20260509-006`, kiểm tra riêng tab **Hoàn thành** và tab **Hủy**; cả hai tab đều không có kết quả.

## Bằng chứng

- Ảnh chụp Chrome hiển thị đã được lấy tại màn **Khóa học**, tab **Tất cả**, bộ lọc chính xác `KH-20260703-005`; bảng hiển thị **Không có khóa học nào phù hợp.**
- Ảnh chụp Chrome hiển thị thứ hai đã được lấy tại tab **Hoàn thành**, bộ lọc chính xác `KH-20260509-006`; bảng cũng hiển thị **Không có khóa học nào phù hợp.**
- URL hiển thị tại thời điểm xác nhận: `/dao-tao/khoa-hoc/danh-sach?tab=TAT_CA&keyword=KH-20260703-005&page=1`.
- URL dataset đối chứng: `/dao-tao/khoa-hoc/danh-sach?tab=HOAN_THANH&keyword=KH-20260509-006&page=1` và `/dao-tao/khoa-hoc/danh-sach?tab=DA_HUY&keyword=KH-20260509-006&page=1`.
- Header tài khoản trên màn hình: **CB Nghiệp vụ - Trung ương #01**, đơn vị **BTP · TW**.

## Lý do blocker

Dữ liệu khóa học mục tiêu và khóa học đối chứng đều không tồn tại hoặc không hiển thị cho đúng tài khoản/môi trường được chỉ định. Vì không thể mở khóa học, không thể truy cập ba tab chi tiết để đối chiếu Hoàng Minh Đức, `tester tkm` hoặc nhóm `tester 2/3/4/5`. Đây là blocker dữ liệu, không phải bằng chứng bug còn tồn tại.

## Điều kiện để chạy lại

Khôi phục/cung cấp khóa học `KH-20260703-005` hoặc `KH-20260509-006` cho `cbnv_tw_01`, hoặc cung cấp mã khóa học thay thế có đủ học viên không có đơn vị và ít nhất một học viên có đơn vị thật trên cả ba tab. Sau đó chạy lại toàn bộ đối chiếu qua UI trước khi cập nhật Google Sheet.
