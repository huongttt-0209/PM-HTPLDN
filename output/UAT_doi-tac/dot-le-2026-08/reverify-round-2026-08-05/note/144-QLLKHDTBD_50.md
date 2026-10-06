## [UAT_TGPL Doanh Nghiệp-tuần 2] row 144 — QLLKHDTBD_50 — S2
Tên chức năng: 
Tác nhân: 
Mô tả: Bảng danh sách Kế hoạch đào tạo thiếu cột và sai định dạng so với thiết kế
Điều kiện: 1. Đăng nhập tài khoản cán bộ (đã kiểm với Cán bộ nghiệp vụ Địa phương và Cán bộ phê duyệt Trung ương, kết quả như nhau)
2. Có sẵn ít nhất 1 kế hoạch đào tạo đã nhập ngân sách dự kiến
Dữ liệu đầu vào: Kế hoạch KH-20260803-0001 (ngân sách dự kiến 100.000.000), KH-20260803-0004; tổng 14 kế hoạch trong danh sách
Các bước: 1. Chọn menu "Đào tạo, tập huấn" -> "Kế hoạch đào tạo"
2. Xem thanh tiêu đề của bảng danh sách, cuộn ngang hết sang phải để thấy toàn bộ cột
3. Đối chiếu với thiết kế màn hình Kế hoạch đào tạo năm (SCR-III-00, Thành phần 3 — Bảng kế hoạch, srs-fr-03-dao-tao.md dòng 1767-1775)
KQ mong đợi: Bảng có đủ các cột theo thiết kế: ô tích chọn dòng, Tên kế hoạch, Năm, Thời gian, Ngân sách dự kiến, Số chương trình, Trạng thái, Người tạo, Ngày tạo, Hành động. Cột ngân sách hiển thị theo định dạng dấu chấm (ví dụ "500.000.000 đ"), rỗng thì hiển thị "—".
KQ thực tế (l1): Bảng chỉ có 8 cột: Mã kế hoạch, Tên kế hoạch, Năm, Từ ngày, Đến ngày, Ngân sách (VNĐ), Trạng thái, Hành động.
- Thiếu 4 thành phần theo thiết kế: ô tích chọn dòng (toàn trang không có ô tích nào), cột "Số chương trình", cột "Người tạo", cột "Ngày tạo".
- Cột ngân sách hiển thị số thô "100000000.00" thay vì "100.000.000 đ". Cùng kế hoạch đó, màn Chi tiết lại hiển thị đúng "100.000.000 VNĐ" nên hai màn không nhất quán.
Đã kiểm bằng 2 cách đều cho kết quả như nhau: đọc danh sách tiêu đề bảng trong mã trang (đúng 8 cột, không có cột nào bị ẩn) và nhìn ảnh chụp sau khi cuộn ngang hết sang phải.
Ảnh hưởng nghiệp vụ: thiếu cột "Người tạo" nên cán bộ phê duyệt không có cách nào biết kế hoạch do đơn vị/người nào lập để ra quyết định duyệt.
Phát hiện thêm trong lúc kiểm tra lại phiếu PDKHDTTH_04 ngày 03/08/2026, không thuộc phạm vi phiếu đó.
Trạng thái 1: Fail | P dev fix1: dev done | Q Verify: Pass
KQ thực tế lần 2: 
Trạng thái 2:  | W dev fix2: dev done | X Verify2: 
--- NOTE (Y: DEV phản hồi lần 2) ---
✅ Đã đạt — cả 5 nội dung của phiếu đều hết lỗi.

- Đã kiểm lại trên bản dựng mới nhất, màn Đào tạo, tập huấn → Kế hoạch đào tạo → Danh sách, đo bằng 2 vai trò: Cán bộ nghiệp vụ Trung ương và Cán bộ phê duyệt Trung ương. Hai vai trò cho kết quả giống nhau.
- Ô tích chọn dòng: đã có; tích ở dòng tiêu đề thì toàn bộ 14/14 dòng đang hiển thị được chọn theo.
- Cột "Người tạo": đã có, hiện đúng tên người lập kế hoạch.
- Cột "Ngày tạo": đã có, đúng dạng ngày/tháng/năm.
- Cột ngân sách: đã hiển thị đúng định dạng dấu chấm kèm đơn vị (100.000.000 đ, 1.000.000 đ, 2.000.000 đ); kế hoạch không nhập ngân sách hiện dấu "—". Không còn dòng nào ra số thô.
- Cột "Số chương trình" — nội dung còn lỗi ở lần trước — nay đã đếm đúng: đối chiếu từng dòng với dữ liệu chương trình đào tạo thực tế đều khớp (4, 2, 1, 1 cho bốn kế hoạch có chương trình; 0 cho các kế hoạch chưa có chương trình nào), cộng dồn cả bảng bằng đúng tổng số chương trình đang có.
- Đã thử tạo mới một chương trình đào tạo qua giao diện và gắn vào một kế hoạch đang hiện 0: lưu xong quay lại bảng danh sách thì kế hoạch đó chuyển thành 1 và tổng cả bảng tăng theo. Như vậy cột này cập nhật đúng cả với dữ liệu phát sinh mới, không chỉ dữ liệu cũ.
- Kết luận: nội dung phiếu phản ánh đã được khắc phục trọn vẹn; bảng danh sách Kế hoạch đào tạo hiện đủ cột và đúng định dạng.