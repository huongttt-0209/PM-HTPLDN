## [UAT_TGPL Doanh Nghiệp-tuần 3] row 259 — CPCTHTTTG_03 — S2
Tên chức năng: 
Tác nhân: 
Mô tả: Kiểm tra hiển thị Biểu đồ và bảng tổng hợp
Điều kiện: 1. Đăng nhập hệ thống thành công
2. Có dữ liệu thống kê
Dữ liệu đầu vào: 
Các bước: 1. Chọn menu "Báo cáo thống kê"
2. Nhập tiêu chí/điều kiện hợp lệ
3. Nhấn Xem báo cáo
KQ mong đợi: - Biểu đồ đường thể hiện xu hướng chi phí
- Bảng tổng hợp: Kỳ thời gian, Tổng chi phí, Số hồ sơ
KQ thực tế (l1): - Số liệu ở trục tung của biểu đồ hiển thị toàn bộ giá trị 0
Trạng thái 1: Fail | P dev fix1: Reject | Q Verify: Reject
KQ thực tế lần 2: 
Trạng thái 2:  | W dev fix2: dev done | X Verify2: 
--- NOTE (Y: DEV phản hồi lần 2) ---
- Đã kiểm tra lại trên đúng môi trường và đúng bộ số liệu anh/chị đã chụp (Tổng chi phí toàn kỳ 226.308.268, Tổng hồ sơ toàn kỳ 25): tài khoản Cán bộ nghiệp vụ Trung ương, báo cáo "Chi phí theo thời gian" (UC142), kỳ Năm 2026 từ 01/01/2026 đến 31/12/2026, đơn vị Toàn quốc.
- Nhãn trục dọc đã đọc được bình thường. Trục bên trái là thang tiền, hiển thị lần lượt "0 · 60 triệu · 120 triệu · 180 triệu · 240 triệu", không còn ra chuỗi "000.000" như trong ảnh anh/chị gửi kèm.
- Biểu đồ nay có thêm một trục dọc riêng bên phải dành cho "Số hồ sơ" (0 · 7 · 14 · 21 · 28), nên đường Số hồ sơ nằm đúng vị trí giá trị 25 của nó, không còn bị dồn sát đáy do vẽ chung thang với số tiền.
- Bảng tổng hợp có đủ Kỳ, Từ ngày, Đến ngày, Số hồ sơ, Tổng chi phí và khớp với số liệu trên biểu đồ (Năm 2026 — 25 hồ sơ — 226.308.268 đ).
- Kết luận: nội dung anh/chị phản ánh đã được khắc phục; chức năng hiển thị biểu đồ và bảng tổng hợp của báo cáo Chi phí theo thời gian hoạt động bình thường trên bản hiện tại.