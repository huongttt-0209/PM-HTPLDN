## [UAT_TGPL Doanh Nghiệp-tuần 3] row 238 — CLDTBDPL_07 — S2
Tên chức năng: 
Tác nhân: 
Mô tả: Kiểm tra chức năng Xuất PDF
Điều kiện: 1. Đăng nhập hệ thống thành công
2. Có dữ liệu thống kê
Dữ liệu đầu vào: 
Các bước: 1. Chọn menu "Báo cáo thống kê"
2. Nhập tiêu chí/điều kiện
3. Nhấn Xem báo cáo
4. Nhấn Xuất PDF
KQ mong đợi: Hệ thống tạo tệp PDF theo đúng mẫu biểu Thông tư số 17/2025/TT-BTP — khổ A4, phông chữ Times New Roman cỡ 13, đầu trang có quốc hiệu và tên cơ quan, cuối trang có ngày ký và chức danh người ký.
- Tên tệp xuất: BaoCaoDaoTao_{YYYYMMDD_HHmm}.pdf.
KQ thực tế (l1): Hệ thống hiển thị thông báo "Không thể tạo file xuất. Vui lòng thử lại.".
Trạng thái 1: Fail | P dev fix1: dev done | Q Verify: Pass
KQ thực tế lần 2: 
Trạng thái 2:  | W dev fix2: dev done | X Verify2: Reopen
--- NOTE (Y: DEV phản hồi lần 2) ---
- Không còn gặp thông báo "Forbidden" khi bấm Xuất PDF. Phần lỗi báo lần trước đã chạy được: hệ thống tạo và tải được tệp PDF về máy.
- Tuy nhiên tệp PDF tải về bị thiếu dữ liệu so với màn hình: bảng "Danh sách khóa học" trong tệp chỉ có 5 cột (Mã khóa học, Tên khóa học, Đơn vị, Số học viên, Điểm TB) — thiếu hẳn cột "Tỷ lệ đạt".
- Trên màn hình, bảng này có 6 cột và cột "Tỷ lệ đạt" hiển thị đầy đủ giá trị cho cả 5 khóa học (50%, 0%, 100%, 80%, 60%).
- Cùng báo cáo này khi Xuất Excel thì vẫn có đủ cột "Tỷ lệ đạt (%)" kèm số liệu. Như vậy chỉ riêng bản PDF bị thiếu cột.
- Đã xuất lại lần thứ hai với đúng điều kiện lọc cũ (Kỳ báo cáo Năm 2026, đơn vị Toàn quốc, khổ giấy A4 dọc mặc định): kết quả vẫn thiếu cột "Tỷ lệ đạt", không phải lỗi ngẫu nhiên một lần.
- Đề nghị bổ sung cột "Tỷ lệ đạt" vào bảng danh sách khóa học ở bản xuất PDF để khớp với màn hình và với bản Excel.