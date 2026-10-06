# QLDMTCTV_OOS_08 — dòng 334 (tab `UAT_TGPL Doanh Nghiệp-tuần 3`)

## Tuần

Tuần 3

## Mã TC

QLDMTCTV_OOS_08

## Mô tả

Biểu mẫu Thêm mới / Chỉnh sửa Tổ chức tư vấn — không chia 6 nhóm thu gọn như đặc tả

## Điều kiện

1. Đăng nhập tài khoản Cán bộ Nghiệp vụ cấp Trung ương (cbnv_tw_04), đơn vị Cục Bổ trợ tư pháp - Bộ Tư pháp.
2. Chọn menu "Mạng lưới Tư vấn viên" -> "Tổ chức tư vấn".

## Dữ liệu đầu vào

Tổ chức TCTV-SEED-0001 dùng để mở chế độ Chỉnh sửa; chế độ Thêm mới mở từ nút "+ Thêm mới".

## Các bước thực hiện

1. Bấm "+ Thêm mới" và đọc toàn bộ biểu mẫu từ trên xuống.
2. Tìm các nhóm thu gọn / mở được trên biểu mẫu.
3. Lặp lại ở chế độ Chỉnh sửa: bấm biểu tượng Sửa trên một dòng bất kỳ.

## Kết quả mong đợi

Màn hình SCR-IV-NEW-02 dòng 1664 ghi loại màn hình là "Biểu mẫu nhập liệu (6 nhóm)"; dòng 1669 liệt kê 6 nhóm: Thông tin cơ bản, Lĩnh vực & Nhân sự, Liên hệ, Công bố, File đính kèm, Ghi chú. Các dòng 1676, 1683, 1686, 1691 ghi loại giao diện của từng nhóm là "nhóm thu gọn", riêng nhóm 1 mặc định mở.

## Kết quả thực tế

Biểu mẫu để phẳng, không có nhóm nào thu gọn hay mở ra được. Chỉ 2 trong 6 nhóm có tiêu đề mục hiển thị là "Công bố" và "Tệp đính kèm"; 4 nhóm còn lại không có tiêu đề phân tách.
Giống nhau ở cả chế độ Thêm mới và chế độ Chỉnh sửa. Không cản trở việc nhập liệu, nhưng biểu mẫu dài và khó tìm mục.

## Ảnh/vieo 1

QLDMTCTV_09-01-TCTV-SEED-0001-form-sua-tu-dau-den-muc-cong-bo.png

## Trạng thái 1

Fail

## Trạng thái dev fix 1

dev done

## Verify

Pass

## DEV phản hồi lần 1

✅ Bug ĐÚNG - chuyển dev.
- Biểu mẫu Thêm mới và Chỉnh sửa Tổ chức tư vấn đang để phẳng, không có nhóm nào thu gọn hoặc mở ra được.
- Theo màn hình SCR-IV-NEW-02 (dòng 1664 và 1669), biểu mẫu phải chia 6 nhóm: Thông tin cơ bản, Lĩnh vực & Nhân sự, Liên hệ, Công bố, File đính kèm, Ghi chú; các dòng 1676, 1683, 1686, 1691 ghi rõ loại giao diện là "nhóm thu gọn".
- Thực tế chỉ 2 trong 6 nhóm có tiêu đề mục ("Công bố" và "Tệp đính kèm"), 4 nhóm còn lại không có tiêu đề phân tách.
- Không cản trở nhập liệu, nhưng biểu mẫu dài và khó tìm mục hơn thiết kế.
- Ghi chú tham chiếu: chức năng "Quản lý Tổ chức tư vấn" (FR-IV-NEW-01) trong đặc tả KHÔNG được cấp mã UC (dòng 1029 ghi "chưa có trong CSV"), nên chỉ nêu tên chức năng và số dòng, không có mã UC để dẫn.
- Lỗi do QA phát hiện thêm khi kiểm 4 phiếu QLDMTCTV_02 / _05 / _06 / _09 ngày 03/08/2026, không nằm trong phạm vi 4 phiếu đó nên mở dòng riêng để chuyển dev.
- Môi trường kiểm: bản dựng HTPLDN V1.0.5.
