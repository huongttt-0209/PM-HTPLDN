✅ Đã hết lỗi — bảng biểu mẫu 21b có đủ cả cột "Số liệu kỳ trước" lẫn cột "Ghi chú".

Đo ngày 07/08/2026 trên môi trường nội bộ 18.143.165.120.nip.io, bó mã giao diện index-D4Buvu4S.js (07/08/2026 02:23) — đã tải lại trang bằng địa chỉ và đọc lại tên bó mã ngay trong tab trước khi đo.
Tài khoản: cbnv_hn (Cán bộ Nghiệp vụ Địa phương — Sở Tư pháp Hà Nội), đúng vai trò và đúng cấp theo đặc tả.

Phải dựng dữ liệu trước mới đo được: cả 3 đợt báo cáo đang có trên môi trường đều chỉ áp dụng biểu mẫu 21a, mà đặc tả (srs-fr-15-ct-htpldn.md:1168) quy định 21b chỉ hiển thị "khi biểu mẫu được áp dụng". Nếu đo bằng dữ liệu sẵn có rồi kết luận "thiếu 21b" thì sẽ sai, vì 21b vắng mặt trong tình huống đó là ĐÚNG đặc tả. Do đó đã nhờ tài khoản Cán bộ Nghiệp vụ Trung ương (cbnv_tw) tạo mới một đợt áp dụng CẢ HAI biểu mẫu: DOT-TRON_NAM-2026-1 "QA F5 reverify 21b - CA_HAI (LBCKQTHCT_04)", phạm vi 2 đơn vị. Đợt này là dữ liệu QA dựng để kiểm thử, có thể xóa sau khi đối tác đọc xong kết quả.

Kết quả trên màn Chi tiết đợt báo cáo:
- Màn hiển thị 2 thẻ biểu mẫu có nhãn rõ ràng: "Biểu mẫu 21a/TP/HTPLDN" và "Biểu mẫu 21b/TP/HTPLDN". Hai bảng có nội dung giống hệt nhau nên đã xác định đúng bảng 21b bằng nhãn thẻ, không xác định bằng số dòng hay nội dung.
- Bảng 21b có đúng 4 cột theo thứ tự: "Chỉ tiêu" | "Số liệu kỳ trước" | "Kỳ này" | "Ghi chú", đủ 13 dòng chỉ tiêu.
- Ở chế độ nhập, mỗi dòng chỉ tiêu của 21b có một ô Ghi chú riêng (nhãn gợi ý trong ô là "Ghi chú"), tức là ô nhập thật chứ không phải cột trang trí.
- Đã kiểm cuộn ngang: không có cột nào bị đẩy khuất ngoài khung nhìn.
- Cột "Số liệu kỳ trước" hiển thị cả khi chưa có dữ liệu kỳ trước (hiện dấu "—"), nên không rơi vào trường hợp "cột bị ẩn vì chưa có số liệu".
- Đo ở cả hai chế độ chỉ đọc và chế độ nhập, kết quả như nhau.

Ghi nhận thêm để BA xem xét, KHÔNG ảnh hưởng kết luận phiếu này: bảng 21b trên màn hiện đang dựng giống hệt 21a (13 dòng chỉ tiêu), trong khi Phụ lục D của tài liệu tổng (mục D.1.3 và D.2.2) mô tả mẫu 21b là bảng tổng hợp cấp tỉnh, mỗi dòng là một Sở/ban ngành và có thêm 2 cột định danh. Hai chỗ này thuộc hai tầng khác nhau (biểu mẫu nhập trên màn so với mẫu văn bản xuất ra), và phần đặc tả màn hình tại :1168 chỉ ghi vắn tắt "tương tự 21a" — dev đang làm đúng theo câu chữ này. Đề nghị BA ghi rõ tập cột và cấu trúc dòng của 21b vào phần đặc tả màn hình để hai bên không chấm bằng hai thước đo khác nhau. Đây là đề nghị bổ sung đặc tả, không chặn bàn giao và không thuộc phạm vi phiếu này.

Về bằng chứng gốc: ảnh LBCKQTHCT_04.jpg bị cắt mất tiêu đề thẻ nên không xác định được ảnh chụp bảng 21a hay 21b, cũng không đọc được biểu mẫu áp dụng và trạng thái của đợt. Vì vậy QA tự dựng tiền đề và đo lại theo đúng luồng phiếu mô tả.
