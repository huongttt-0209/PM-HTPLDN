## [UAT_TGPL Doanh Nghiệp-tuần 3] row 166 — QLTKND_03 — S2
Tên chức năng: 
Tác nhân: 
Mô tả: Kiểm tra Thẻ trạng thái (tab nhanh)
Điều kiện: 1. Đăng nhập tài khoản
Dữ liệu đầu vào: 
Các bước: 1. Chọn menu "Quản trị hệ thống" => "Tài khoản & Phân quyền"
KQ mong đợi: 5 thẻ tab hiển thị số lượng tài khoản theo trạng thái: "Tất cả", "Đang hoạt động", "Chờ kích hoạt", "Tạm khóa", "Vô hiệu hóa". Thẻ "Chờ kích hoạt" dùng màu nhấn (vàng) để thu hút chú ý của Quản trị hệ thống về các tài khoản chưa được người dùng kích hoạt.
KQ thực tế (l1): Màn hình hiển thị 6 thẻ tab. Thẻ "Chờ kích hoạt" không có màu nhấn
Trạng thái 1: Fail | P dev fix1: dev done | Q Verify: Pass
KQ thực tế lần 2: 
Trạng thái 2:  | W dev fix2: dev done | X Verify2: Reopen
--- NOTE (Y: DEV phản hồi lần 2) ---
- Đã kiểm tra lại thanh thẻ trạng thái ở màn Tài khoản & phân quyền: nay còn đúng 4 thẻ "Tất cả / Hoạt động / Chờ kích hoạt / Tạm khóa", không còn thẻ "Chờ phân quyền" như lần trước. Bấm lần lượt từng thẻ đều lọc ra đúng số liệu tương ứng (207 / 145 / 20 / 2). Phần này đã đạt.
- Về ý "thiếu thẻ Vô hiệu hóa": đặc tả chỉ quy định 4 thẻ nêu trên, còn tài khoản đã vô hiệu hóa được xem qua bộ lọc "Trạng thái" ngay bên dưới. Chúng tôi đã thử: chọn "Vô hiệu hóa" rồi bấm "Tìm kiếm" thì ra 38 tài khoản. Ý này xin phép khép lại.
- Về ý "Chờ kích hoạt chưa có màu nhấn": phản ánh này có cơ sở, nhưng chỗ được quy định màu là cột "Trạng thái" trong danh sách chứ không phải thẻ lọc. Kiểm tra cột đó thì màu đang lệch ở 3/4 trạng thái:
  - "Chờ kích hoạt" đang màu xám, trong khi yêu cầu là màu vàng;
  - "Tạm khóa" đang màu vàng cam, trong khi yêu cầu là màu đỏ;
  - "Vô hiệu hóa" đang màu đỏ, trong khi yêu cầu là màu đen;
  - riêng "Hoạt động" màu xanh là đúng.
- Vì vậy chúng tôi để phiếu này ở trạng thái Reopen. Phạm vi còn lại chỉ là chỉnh bảng màu cho cột "Trạng thái"; phần thẻ lọc trạng thái đã đúng, không cần sửa thêm.