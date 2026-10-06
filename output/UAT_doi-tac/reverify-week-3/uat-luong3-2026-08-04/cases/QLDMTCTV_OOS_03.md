# QLDMTCTV_OOS_03 — dòng 329 (tab `UAT_TGPL Doanh Nghiệp-tuần 3`)

## Tuần

Tuần 3

## Mã TC

QLDMTCTV_OOS_03

## Mô tả

Danh sách Tổ chức tư vấn — cột "Hành động" thiếu nhóm lệnh "..." (Trình phê duyệt / Phê duyệt / Từ chối / Cập nhật trạng thái)

## Điều kiện

1. Đăng nhập tài khoản Cán bộ Nghiệp vụ cấp Trung ương (cbnv_tw_04), đơn vị Cục Bổ trợ tư pháp - Bộ Tư pháp.
2. Chọn menu "Mạng lưới Tư vấn viên" -> "Tổ chức tư vấn".

## Dữ liệu đầu vào

3 tổ chức ở thẻ "Đang hoạt động" và 2 tổ chức ở thẻ "Mới đăng ký".

## Các bước thực hiện

1. Cuộn ngang bảng sang phải tới cột "Hành động".
2. Đếm và đọc các nút đang có trên mỗi dòng.
3. Tìm nhóm lệnh dạng dấu ba chấm "..." trên dòng.

## Kết quả mong đợi

Màn hình SCR-IV-NEW-01 dòng 1646 quy định cột "Hành động" gồm 2 biểu tượng thường (Xem, Sửa) và một nhóm lệnh "..." chứa: "Trình phê duyệt", "Phê duyệt", "Từ chối", "Cập nhật trạng thái", "Xóa" — mỗi lệnh hiện theo đúng vai trò và trạng thái của dòng.

## Kết quả thực tế

Cột "Hành động" chỉ có 3 biểu tượng rời: Xem, Sửa, Xóa. Không có nhóm lệnh "..." nào.
Hệ quả: các lệnh "Trình phê duyệt" và "Cập nhật trạng thái" không thao tác được từ danh sách, phải mở màn Chi tiết của từng tổ chức mới làm được.

## Ảnh/vieo 1

QLDMTCTV_02-cuon-ngang-hien-cot-trang-thai-va-cong-khai.png

## Trạng thái 1

Fail

## Trạng thái dev fix 1

dev done

## Verify

Pass

## DEV phản hồi lần 1

- Nhóm lệnh "..." trên cột Hành động đã được bổ sung, các lệnh hiển thị đúng theo vai trò và trạng thái hồ sơ.
- Còn lại: bấm "Trình phê duyệt" (hồ sơ Mới đăng ký) và bấm "Cập nhật trạng thái" (hồ sơ Đang hoạt động) không mở hộp thoại xác nhận nào, mà chuyển thẳng sang màn Chi tiết của tổ chức; người dùng phải tự tìm và bấm nút tương ứng ở màn đó mới thực hiện được. Đây đúng là 2 lệnh mà phiếu gốc đã nêu.
- Đối chứng trong cùng nhóm lệnh: "Xóa" mở hộp thoại ngay tại danh sách; "Phê duyệt" và "Từ chối" đều mở được hộp thoại xác nhận. Chỉ 2 lệnh nêu trên là chưa thao tác được từ danh sách.
- Theo màn hình SCR-IV-NEW-01 (dòng 1646), mỗi mục trong nhóm lệnh "..." khi bấm phải thực hiện đúng lệnh đó, tức đưa ra bước xác nhận tương ứng, chứ không dừng giữa chừng.
- Đã kiểm bằng vai trò Cán bộ Nghiệp vụ Trung ương và Cán bộ Phê duyệt Trung ương, đơn vị Cục Bổ trợ tư pháp; tái hiện 2 lần ở 2 phiên đăng nhập, ngày 04/08/2026, bản dựng V1.0.5.
