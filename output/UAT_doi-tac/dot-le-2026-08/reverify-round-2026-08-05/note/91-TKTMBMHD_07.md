## [UAT_TGPL Doanh Nghiệp-tuần 3] row 91 — TKTMBMHD_07 — S2
Tên chức năng: 
Tác nhân: 
Mô tả: Xóa bộ lọc
Điều kiện: 1. Đăng nhập tài khoản
Dữ liệu đầu vào: 
Các bước: 1. Chọn menu "Biểu mẫu" -> "Thư mục biểu mẫu"
2. Nhập/chọn tiêu chí tìm kiếm
3. Bấm nút Xóa bộ lọc
KQ mong đợi: - Xóa toàn bộ giá trị đã nhập tại các điều kiện tìm kiếm và bộ lọc (Tìm kiếm, Lọc lĩnh vực, Lọc trạng thái, Khoảng ngày tạo).
+ Đưa tab phân loại về "Tất cả".
+ Hiển thị lại danh sách mặc định (toàn bộ thư mục trong phạm vi phân quyền, sắp xếp theo ngày tạo giảm dần).
KQ thực tế (l1): Không đưa về tab "Tất cả"
Trạng thái 1: Fail | P dev fix1: dev done | Q Verify: Pass
KQ thực tế lần 2: 
Trạng thái 2:  | W dev fix2: dev done | X Verify2: Reopen
--- NOTE (Y: DEV phản hồi lần 2) ---
- Đã chạy lại luồng: Thư viện biểu mẫu > Thư mục, đặt bộ lọc rồi bấm "Xóa bộ lọc".
- Phần đã được sửa: thanh tab phân loại nay ĐÃ tự về "Tất cả", các ô Tìm kiếm, Lĩnh vực, Trạng thái và Khoảng ngày cũng đã được xóa trắng.
- Phần còn lỗi: danh sách KHÔNG trở về mặc định. Mặc định màn hình có 23 thư mục; sau khi gõ từ khóa rồi bấm "Xóa bộ lọc", danh sách vẫn chỉ hiển thị các bản ghi khớp từ khóa cũ (ví dụ gõ "test" thì còn 9 kết quả, gõ "a" kèm lĩnh vực Thuế thì còn 2 kết quả). Số đếm trên tab "Tất cả" cũng đổi theo, hiển thị "Tất cả 9" thay vì "Tất cả 23".
- Hệ quả với người dùng: ô lọc trông như đã trống nhưng danh sách vẫn đang bị lọc, dễ hiểu nhầm là hệ thống chỉ có ngần đó thư mục.
- Bấm thêm nút "Làm mới" cũng không đưa danh sách về mặc định.
- Đã thử 2 lần với 2 bộ lọc khác nhau, kết quả giống nhau.