⚠️ Cần BA xác nhận.
- Đối tác báo: tiêu đề trang màn Chi tiết hồ sơ chi trả không giống thiết kế (đối tác kỳ vọng tiêu đề "Chi tiết hồ sơ #{mã hồ sơ}").
- Kiểm tra lại trên màn Chi tiết hồ sơ (tài khoản CB Nghiệp vụ TW, hồ sơ CT-SEED-101, data thật): tiêu đề trang (h1) hiển thị TÊN DOANH NGHIỆP ("Công ty TNHH Seed Publishable"), không phải chuỗi "Chi tiết hồ sơ #{mã}". Hành vi này tái hiện đúng như đối tác phản ánh.
- Đối chiếu SRS SCR-V.II-02 (FR-06, UC69): component #3 "Header info" (srs-fr-06-chi-tra.md:979) liệt kê thẻ đầu trang gồm Mã hồ sơ, Tên doanh nghiệp, Quy mô, Trạng thái, SLA — nhưng KHÔNG quy định chính xác chuỗi tiêu đề trang (h1) phải là "Chi tiết hồ sơ #{mã}". App dùng tên DN làm tiêu đề, các trường bắt buộc của header đều đủ.
- Thanh tiến trình (stepper, component #4, srs-fr-06-chi-tra.md:980): hiển thị đủ 6 bước đúng thứ tự (Tiếp nhận → Kiểm tra → Đánh giá → Thẩm định → Phê duyệt → Thanh toán) — phần này ĐÚNG spec, không phải lỗi.
- Phát hiện thêm: breadcrumb (component #1, srs-fr-06-chi-tra.md:977) hiển thị "Trang chủ / Chi trả chi phí / Chi tiết" — thiếu "#{ma_ho_so}" so với SRS ("Chi tiết #{ma_ho_so}").
- Cần BA xác nhận: (1) tiêu đề trang phải theo thiết kế "Chi tiết hồ sơ #{mã}" hay dùng tên DN được chấp nhận; (2) breadcrumb có bắt buộc kèm #{ma_ho_so} không.
