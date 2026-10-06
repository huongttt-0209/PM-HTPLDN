## [UAT_TGPL Doanh Nghiệp-tuần 2] row 121 — CBKQDTBD_01 — S2
Tên chức năng: Công bố kết quả đào tạo bồi dưỡng
Tác nhân: Cán  bộ 
 TW,BN,ĐP
Mô tả: Cung cấp chức năng công bố kết quả, cập nhật kết quả vào tài khoản của học viên.
Điều kiện: 1. Đăng nhập tài khoản 
2. Khóa học ở trạng thái "Hoàn thành" và có học viên có kết quả đã được phê duyệt.
Dữ liệu đầu vào: 
Các bước: 1. Chọn menu "Đào tạo, tập huấn" -> "Khóa học"
2. Nhấn xem chi tiết khóa học
3. Chọn tab "Công bố kết quả"
4. Chọn danh sách học viên và bấm nút "Công bố"
KQ mong đợi: Hợp lệ, hệ thống hiển thị thông báo "Đã công bố kết quả cho {số lượng} học viên".
KQ thực tế (l1): Màn hình chi tiết không có tab riêng"Công bố kết quả"
Trạng thái 1: Fail | P dev fix1: dev done | Q Verify: Pass
KQ thực tế lần 2: 
Trạng thái 2:  | W dev fix2: dev done | X Verify2: Reopen
--- NOTE (Y: DEV phản hồi lần 2) ---
✅ Vẫn còn lỗi — chưa đạt.
- Đã kiểm tra lại ngày 04/08/2026 bằng tài khoản Cán bộ nghiệp vụ Trung ương (cbnv_tw), bản dựng V1.0.5, trên đúng khóa học được phản ánh: "test thêm mới khóa học" (mã KH-20260703-005), trạng thái Hoàn thành, có 2 học viên đã được phê duyệt kết quả.
- Phần đã hết lỗi: màn hình chi tiết khóa học nay đã có tab riêng "Công bố kết quả". Bấm "Công bố tất cả" rồi xác nhận thì cả 2 học viên chuyển sang "Đã công bố" kèm thời điểm công bố 04/08/2026 16:47. Bấm "Hủy công bố tất cả" thì hệ thống bắt nhập lý do tối thiểu 10 ký tự (nhập 3 ký tự bị chặn ngay tại ô nhập), nhập đủ lý do thì cả 2 học viên trở lại "Chưa công bố". Khóa học chưa ở trạng thái Hoàn thành thì hệ thống chặn công bố và báo rõ lý do.
- Phần còn lỗi: đúng bước 4 của phiếu — "Chọn danh sách học viên và bấm nút Công bố" — hiện chưa thực hiện được.
- Nút "Công bố" (và nút "Hủy" khi đã công bố) ở cột Hành động của từng học viên luôn ở trạng thái mờ, bấm không được. Rê chuột lên nút thì phần mềm tự hiện chú thích: "Công bố/hủy theo từng học viên sẽ khả dụng khi hệ thống hỗ trợ (hiện chỉ công bố cấp khóa)".
- Ô tích chọn ở từng dòng và ô "chọn tất cả" không có tác dụng: tích xong vẫn không bấm được nút nào, hệ thống chỉ công bố hoặc hủy công bố cho toàn bộ khóa học, không công bố được cho một phần danh sách học viên.
- Đã kiểm trên 3 khóa học khác nhau và ở cả hai trạng thái (chưa công bố và đã công bố) — nút của từng học viên luôn mờ, nên không phải do dữ liệu của riêng một khóa.
- Ghi nhận thêm trong cùng màn hình: sau khi hủy công bố, cột "Thời điểm công bố" vẫn giữ mốc thời gian của lần công bố trước trong khi cột trạng thái đã trở về "Chưa công bố".
- Ghi nhận thêm (kiểm lại lần hai lúc 17:07 cùng ngày): sau khi khóa học đã trải qua một lượt công bố rồi hủy công bố, bấm "Công bố tất cả" thêm lần nữa thì hệ thống từ chối và hiện thông báo "Đang có yêu cầu PUBLISH đang chờ xử lý cho khóa học này", không công bố lại được. Trên màn hình không có chỗ nào để cán bộ xem hoặc xử lý yêu cầu đang chờ đó, nên khóa học bị kẹt không công bố lại được.
- Đề nghị bổ sung thao tác công bố / hủy công bố cho từng học viên (hoặc cho nhóm học viên được tích chọn) đúng như mô tả của phiếu kiểm thử.