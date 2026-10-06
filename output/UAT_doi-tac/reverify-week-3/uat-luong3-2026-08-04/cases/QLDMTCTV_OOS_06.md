# QLDMTCTV_OOS_06 — dòng 332 (tab `UAT_TGPL Doanh Nghiệp-tuần 3`)

## Tuần

Tuần 3

## Mã TC

QLDMTCTV_OOS_06

## Mô tả

Danh sách Tổ chức tư vấn — thứ tự các thẻ trạng thái khác thứ tự đặc tả

## Điều kiện

1. Đăng nhập tài khoản Cán bộ Phê duyệt cấp Trung ương (cbpd_tw_04), đơn vị Cục Bổ trợ tư pháp - Bộ Tư pháp.
2. Chọn menu "Mạng lưới Tư vấn viên" -> "Tổ chức tư vấn".

## Dữ liệu đầu vào

Tài khoản Cán bộ Phê duyệt thấy đủ 6 thẻ.

## Các bước thực hiện

1. Đọc thứ tự các thẻ trạng thái từ trái sang phải.
2. Đối chiếu với thứ tự trong đặc tả màn hình.

## Kết quả mong đợi

Màn hình SCR-IV-NEW-01 xếp thứ tự các thẻ từ dòng 1625 đến 1630 là: "Đang hoạt động" -> "Tạm dừng" -> "Mới đăng ký" -> "Chờ phê duyệt" -> "Đã từ chối" -> "Vô hiệu hóa".

## Kết quả thực tế

Thứ tự trên web là: "Đang hoạt động" -> "Chờ phê duyệt" -> "Mới đăng ký" -> "Đã từ chối" -> "Tạm dừng" -> "Vô hiệu hóa".
Đủ 6 thẻ, không thiếu thẻ nào, chỉ khác vị trí sắp xếp.

## Ảnh/vieo 1

QLDMTCTV_05-cbpd-tw-04-thanh-the-co-cho-phe-duyet.png

## Trạng thái 1

Fail

## Trạng thái dev fix 1

BA confirm

## Verify

BA confirm

## DEV phản hồi lần 1

⚠️ Cần BA xác nhận.
- Đặc tả đang tự mâu thuẫn về SỐ LƯỢNG thẻ trạng thái của màn danh sách Tổ chức tư vấn.
- Phần màn hình khẳng định 6 thẻ ở ba chỗ độc lập: dòng 1610 ("Danh sách 6 tab"), dòng 1617 ("Hiển thị 6 tab") và bảng thành phần dòng 1625 đến 1630 liệt kê đủ 6 thẻ.
- Nhưng Tiêu chí chấp nhận của chính chức năng lại ghi "3 tab trạng thái" (dòng 1129).
- Thực tế phần mềm: Cán bộ Phê duyệt thấy 6 thẻ; Cán bộ Nghiệp vụ thấy 5 thẻ vì thẻ "Chờ phê duyệt" chỉ hiện với Cán bộ Phê duyệt, đúng như dòng 1628 quy định. Không vai trò nào thấy 3 thẻ.
⚠️ Câu hỏi gửi BA: số thẻ đúng là 6 hay 3? Đề nghị chốt một con số rồi sửa chỗ còn lại cho khớp, vì chừng nào dòng 1129 còn ghi "3 tab" thì mọi lượt kiểm sau vẫn báo lệch. Tổ kiểm thử nghiêng về 6 vì phần màn hình mô tả chi tiết hơn, nhất quán ở ba chỗ và khớp với phần mềm; nhưng không tự chốt vì đây là hai phần của cùng một tài liệu đã duyệt.
- Rút lại một ý so với lượt trước: ý "thứ tự các thẻ khác đặc tả" đã được rà lại và rút, vì bảng thành phần màn hình là bảng liệt kê thành phần chứ không phải bản vẽ bố cục, không đủ căn cứ coi thứ tự là ràng buộc bắt buộc. Phần mềm xếp thẻ khác thứ tự liệt kê nhưng đủ thẻ, không thiếu thẻ nào.
- Ghi chú tham chiếu: chức năng "Quản lý Tổ chức tư vấn" (FR-IV-NEW-01) trong đặc tả không được cấp mã UC (dòng 1029 ghi "chưa có trong CSV"), nên chỉ nêu tên chức năng và số dòng.
- Đã đưa vào file gửi BA: ba-confirmation-needed-luong4-to-chuc-tu-van-2026-08-03.md, mục 2.
- Kiểm bằng vai trò Cán bộ Phê duyệt Trung ương (cbpd_tw_04), bản dựng HTPLDN V1.0.5.
