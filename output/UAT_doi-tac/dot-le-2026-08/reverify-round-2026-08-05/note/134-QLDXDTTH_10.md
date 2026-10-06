## [UAT_TGPL Doanh Nghiệp-tuần 2] row 134 — QLDXDTTH_10 — S2
Tên chức năng: 
Tác nhân: 
Mô tả: Tab "Đề xuất đào tạo" (màn Chương trình đào tạo) thiếu cột "Người đề xuất".
Điều kiện: 1. Đăng nhập tài khoản Cán bộ nghiệp vụ
2. Đơn vị của cán bộ có ít nhất 1 đề xuất đào tạo do Doanh nghiệp gửi
Dữ liệu đầu vào: Đề xuất do DN "QA UAT Kiem Thu DN" gửi ngày 03/08/2026, nội dung bắt đầu bằng QA-VERIFY-0803, trạng thái "Mới gửi".
Các bước: 1. Vào Đào tạo, tập huấn -> Chương trình đào tạo
2. Chọn tab "Đề xuất đào tạo"
3. Xem danh sách, cuộn hết thanh ngang của bảng
4. Bấm vào nội dung đề xuất để mở màn chi tiết
KQ mong đợi: Bảng đề xuất có cột "Người đề xuất" để cán bộ biết đề xuất là của doanh nghiệp / người hỗ trợ nào.
Căn cứ: FR-III-13 (UC32) §Đặc tả màn hình SCR-III-01 - Thành phần 8 (dòng 1875) liệt kê cột: Lĩnh vực, Nội dung, Người đề xuất, Trạng thái, Ngày tạo, Hành động.
KQ thực tế (l1): Không có cột "Người đề xuất". Bảng chỉ có 8 cột: Nội dung, Lĩnh vực, Thời gian mong muốn, Địa điểm mong muốn, SL dự kiến, Trạng thái, Ngày tạo, Hành động. Đã cuộn hết thanh ngang để chắc chắn không phải cột bị khuất. Màn chi tiết đề xuất cũng không hiển thị người đề xuất. Cán bộ không biết đề xuất là của ai.
Trạng thái 1: Fail | P dev fix1: dev done | Q Verify: Pass
KQ thực tế lần 2: 
Trạng thái 2:  | W dev fix2: dev done | X Verify2: Reopen
--- NOTE (Y: DEV phản hồi lần 2) ---
✅ Vẫn còn lỗi — chưa đạt.
- Đã kiểm lại trên bản dựng mới nhất của môi trường nghiệm thu, bằng hai tài khoản Cán bộ nghiệp vụ (một cấp Địa phương, một cấp Trung ương), xem cả bảng danh sách lẫn màn hình chi tiết, có cuộn hết thanh ngang của bảng.
- Phần đã hết lỗi: cột "Người đề xuất" đã được thêm vào bảng (bảng nay có 9 cột) và cũng đã có ở màn hình chi tiết. Với đề xuất do doanh nghiệp gửi bằng tài khoản trong phần mềm, cột này hiển thị đúng họ tên kèm đơn vị; chúng tôi tự tạo hai đề xuất từ hai doanh nghiệp khác nhau và bảng hiện đúng hai tên khác nhau.
- Phần còn lỗi: với đề xuất được gửi từ chuyên trang (người gửi không dùng tài khoản trong phần mềm), cột "Người đề xuất" chỉ hiện dấu gạch ngang kèm tên đơn vị, không có họ tên và cũng không có tên doanh nghiệp. Màn hình chi tiết cũng chỉ hiện dấu gạch ngang.
- Đo được: trên danh sách 16 đề xuất mà cán bộ Trung ương nhìn thấy, có 10 đề xuất để trống người đề xuất, trong đó có chính đề xuất "TKM gửi đề xuất đào tạo cán bộ nghiệp vụ quý 3/2026" ngày 23/07/2026 và "TKM đề xuất kiểm thử chức năng".
- Đã loại trừ khả năng "chỉ do dữ liệu cũ": hai đề xuất cũ nhất trong kho (ngày 11/05/2026 và 25/05/2026) vẫn hiện đầy đủ tên người đề xuất, trong khi nhóm bị trống nằm ở khoảng 23/06 đến 25/07. Như vậy yếu tố phân biệt là nguồn gửi, không phải thời điểm tạo.
- Cũng đã loại trừ nguyên nhân do vai trò và do trạng thái: hai cấp cán bộ cho kết quả như nhau, và nhóm bị trống trải đều ở cả bốn trạng thái Mới gửi, Đã tiếp nhận, Đang xử lý, Đã xử lý.
- Vì mục đích của cột là để cán bộ biết đề xuất là của doanh nghiệp hay người hỗ trợ nào, mà đúng nhóm đề xuất gửi từ chuyên trang lại không có thông tin này, nên phần sửa mới đạt một nửa.