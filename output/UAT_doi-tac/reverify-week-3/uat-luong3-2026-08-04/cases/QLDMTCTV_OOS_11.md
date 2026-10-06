# QLDMTCTV_OOS_11 — dòng 337 (tab `UAT_TGPL Doanh Nghiệp-tuần 3`)

## Tuần

Tuần 3

## Mã TC

QLDMTCTV_OOS_11

## Mô tả

Màn Chi tiết Tổ chức tư vấn — thiếu toàn bộ 3 tab và không có vùng tệp đính kèm

## Điều kiện

1. Đăng nhập tài khoản Cán bộ Nghiệp vụ cấp Trung ương (cbnv_tw_04), đơn vị Cục Bổ trợ tư pháp - Bộ Tư pháp.
2. Chọn menu "Mạng lưới Tư vấn viên" -> "Tổ chức tư vấn".

## Dữ liệu đầu vào

Tổ chức TC-BTP-TW-0003, trạng thái "Mới đăng ký", có 1 tệp PDF đính kèm (xác nhận được khi mở chế độ Chỉnh sửa).

## Các bước thực hiện

1. Ở thẻ "Mới đăng ký", bấm vào tên tổ chức TC-BTP-TW-0003 để mở màn Chi tiết.
2. Đếm số tab trên màn.
3. Tìm mục tệp đính kèm và nút "Xem" / "Tải xuống" của tệp.
4. Đọc đường dẫn điều hướng ở thanh trên cùng.
5. Đối chiếu: bấm "Chỉnh sửa" để xác nhận tổ chức này thực sự đang có tệp.

## Kết quả mong đợi

Màn hình SCR-IV-NEW-03 quy định màn Chi tiết là "Trang chi tiết 3 tab + 6 nút hành động ở header" (dòng 1702). Ba tab bắt buộc: "Thông tin" (dòng 1729), "Tư vấn viên liên kết" (dòng 1730), "Lịch sử" (dòng 1732). Riêng tab "Thông tin" phải hiển thị đủ 6 nhóm thông tin, trong đó có nhóm file đính kèm và "mỗi file có nút Xem mở hộp xem PDF, Tải xuống" (dòng 1729). Đường dẫn điều hướng phải là "... > [Tên tổ chức]" (dòng 1715).

## Kết quả thực tế

Màn Chi tiết KHÔNG có tab nào (đếm được 0 tab). Cả ba tab "Thông tin", "Tư vấn viên liên kết" và "Lịch sử" đều không tồn tại — người dùng không xem được danh sách tư vấn viên liên kết lẫn nhật ký thao tác của tổ chức.
Không có mục tệp đính kèm nào, cũng không có nút "Xem" hay "Tải xuống", dù tổ chức này đang có 1 tệp PDF (mở chế độ Chỉnh sửa thì thấy tệp). Muốn xem tệp phải vào chế độ Chỉnh sửa.
Bảng thông tin cũng thiếu mục "Lĩnh vực" dù tổ chức có lĩnh vực Thương mại.
Đường dẫn điều hướng hiển thị "... / Tổ chức tư vấn / Chi tiết", không kèm tên tổ chức như đặc tả.

## Ảnh/vieo 1

QLDMTCTV_OOS-man-chi-tiet-khong-co-3-tab-va-khong-co-vung-tep.png

## Trạng thái 1

Fail

## Trạng thái dev fix 1

dev done

## Verify

Pass

## DEV phản hồi lần 1

✅ Bug ĐÚNG - chuyển dev.
- Màn Chi tiết Tổ chức tư vấn hiện không có tab nào. Theo màn hình SCR-IV-NEW-03 (dòng 1702), đây phải là trang chi tiết gồm 3 tab: "Thông tin" (dòng 1729), "Tư vấn viên liên kết" (dòng 1730) và "Lịch sử" (dòng 1732).
- Hệ quả: không xem được danh sách tư vấn viên liên kết với tổ chức, cũng không xem được nhật ký thao tác của hồ sơ.
- Không có mục tệp đính kèm trên màn Chi tiết, dù tổ chức đang có tệp. Dòng 1729 quy định tab "Thông tin" phải hiển thị nhóm file đính kèm, mỗi tệp kèm nút "Xem" mở hộp xem PDF và nút "Tải xuống". Hiện phải vào chế độ Chỉnh sửa mới thấy tệp.
- Bảng thông tin còn thiếu mục "Lĩnh vực" dù tổ chức có lĩnh vực.
- Đường dẫn điều hướng hiển thị "... / Tổ chức tư vấn / Chi tiết", trong khi dòng 1715 yêu cầu kèm tên tổ chức.
- Kiểm trên tổ chức TC-BTP-TW-0003 (trạng thái Mới đăng ký, có 1 tệp PDF), tài khoản Cán bộ Nghiệp vụ Trung ương.
- Ghi chú tham chiếu: chức năng "Quản lý Tổ chức tư vấn" (FR-IV-NEW-01) trong đặc tả KHÔNG được cấp mã UC (dòng 1029 ghi "chưa có trong CSV"), nên chỉ nêu tên chức năng và số dòng, không có mã UC để dẫn.
- Lỗi do QA phát hiện thêm khi kiểm 4 phiếu QLDMTCTV_02 / _05 / _06 / _09 ngày 03/08/2026, không nằm trong phạm vi 4 phiếu đó nên mở dòng riêng để chuyển dev.
- Môi trường kiểm: bản dựng HTPLDN V1.0.5.
