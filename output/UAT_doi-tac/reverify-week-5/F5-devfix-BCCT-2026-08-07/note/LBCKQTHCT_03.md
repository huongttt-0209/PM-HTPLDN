✅ Đã hết lỗi — bảng biểu mẫu 21a có đủ cả cột "Số liệu kỳ trước" lẫn cột "Ghi chú".

Đo ngày 07/08/2026 trên môi trường nội bộ 18.143.165.120.nip.io, bó mã giao diện index-D4Buvu4S.js (07/08/2026 02:23) — đã tải lại trang bằng địa chỉ và đọc lại tên bó mã ngay trong tab trước khi đo. Lưu ý: môi trường vừa được triển khai lại lúc 02:23, khác bó mã so với đầu đợt verify, trong khi nhãn phiên bản trên giao diện vẫn là V1.0.9 nên nhãn này không phân biệt được hai bản dựng.
Tài khoản: cbnv_hn (Cán bộ Nghiệp vụ Địa phương — Sở Tư pháp Hà Nội), đúng vai trò và đúng cấp theo đặc tả.

Kết quả trên màn Chi tiết đợt báo cáo, bảng biểu mẫu 21a:
- Hàng tiêu đề đọc được đúng 4 cột theo thứ tự: "Chỉ tiêu" | "Số liệu kỳ trước" | "Kỳ này" | "Ghi chú" — khớp đủ 4 cụm mà đặc tả yêu cầu tại srs-fr-15-ct-htpldn.md:1167.
- Bảng có đúng 13 dòng chỉ tiêu, khớp mốc BA chốt ngày 06/08/2026 tại :802.
- Cột "Ghi chú" là ô nhập riêng cho từng chỉ tiêu (13 ô), lưu được và đọc lại đúng nội dung đã nhập.
- Đã kiểm cuộn ngang của bảng: không có cột nào bị đẩy khuất ngoài khung nhìn.

Kiểm chéo để loại 2 khả năng chấm oan:
- Lặp lại trên 2 đợt báo cáo khác nhau (một đợt đang lập có dữ liệu, một đợt còn trống hoàn toàn) — cả hai đều hiện đủ 4 cột.
- Cột "Số liệu kỳ trước" hiện cả khi chưa có dữ liệu kỳ trước: dữ liệu nguồn đang rỗng mà cột vẫn hiển thị kèm dấu "—", nên không rơi vào trường hợp "cột bị ẩn vì chưa có số liệu".
- Đo bằng 2 đường độc lập (đọc giao diện và đọc thẳng dữ liệu nguồn), hai đường khớp nhau.

Ghi nhận thêm, không ảnh hưởng kết luận phiếu này: đặc tả tại :1167 ràng buộc biểu mẫu 21a chỉ hiển thị "khi đợt ở trạng thái Đang lập BC", nhưng thực tế phần mềm hiển thị biểu mẫu theo trạng thái nộp của ĐƠN VỊ chứ không theo trạng thái của ĐỢT — hiện không có đợt nào trong môi trường rời khỏi trạng thái "Tạo đợt", kể cả đợt đã có đơn vị nộp xong. Điểm này được xử lý ở phiếu TPDBCKQTHCT_01, là phiếu có kết quả mong đợi nhắm thẳng vào trạng thái của đợt.

Về bằng chứng gốc: video LBCKQTHCT_03.webm quay màn biểu mẫu 21b, trong khi phiếu này soi biểu mẫu 21a; bản ghi dùng trong video (DOT-SO_BO_NAM-2026-2) hiện không còn tồn tại trên môi trường. Vì vậy QA tự dựng lại đúng luồng phiếu mô tả để đo, thay vì đối chiếu theo video.
