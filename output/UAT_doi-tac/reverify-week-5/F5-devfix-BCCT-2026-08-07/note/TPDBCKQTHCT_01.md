✅ Vẫn còn lỗi — nhưng điểm hỏng đã DỊCH CHỖ: nay thao tác "Trình duyệt kết quả" bị hệ thống chặn hẳn, dù trên màn cả 13/13 chỉ tiêu của biểu mẫu đều đang có giá trị. Cán bộ không còn đường nào để trình báo cáo.

Đo ngày 07/08/2026 trên môi trường nội bộ 18.143.165.120.nip.io, bó mã giao diện index-D4Buvu4S.js (07/08/2026 02:23) — đã tải lại trang bằng địa chỉ và đọc lại tên bó mã ngay trong tab trước khi đo.
Tài khoản: cbnv_hn (Cán bộ Nghiệp vụ Địa phương — Sở Tư pháp Hà Nội), đúng vai trò và đúng cấp theo đặc tả. Đợt đo: DOT-SO_BO_NAM-2026-1, biểu mẫu 21a.

TRIỆU CHỨNG CŨ ĐÃ HẾT:
Ở lượt trình đi lọt được, trạng thái CÓ cập nhật đúng: màn Chi tiết đợt đọc được "Chờ duyệt kết quả", thanh tiến trình nhảy sang bước 3, và giữ nguyên sau khi tải lại trang bằng địa chỉ; báo cáo chuyển sang Chờ phê duyệt; cán bộ phê duyệt cùng đơn vị (cbpd_hn, đã đối chiếu trùng đơn vị) nhận đúng thông báo "Báo cáo đợt ... đã được trình duyệt" trùng mốc giờ; nhật ký hệ thống có mục ứng với thao tác trình. Nghĩa là mô tả cũ "có thông báo thành công nhưng trạng thái không đổi" KHÔNG còn tái hiện.

LỖI HIỆN TẠI — vì sao vẫn phải mở lại:
Trên màn Chi tiết đợt, bảng Biểu mẫu 21a có đủ 13 dòng chỉ tiêu và dòng nào cũng đang hiện giá trị: chỉ tiêu 1 đến 11 hiện sẵn số 0 kèm dấu (HT) và KHÔNG có ô để cán bộ nhập hay sửa; chỉ tiêu 12 và 13 có ô nhập, đã nhập 1207 và 1308. Tức là không có chỉ tiêu nào bỏ trống.
Bấm [Trình duyệt KQ] → xác nhận [Đồng ý] → hệ thống chặn với thông báo "Vui lòng hoàn chỉnh báo cáo trước khi trình", và liệt kê đúng 11 chỉ tiêu "còn thiếu" — trùng khít 11 chỉ tiêu duy nhất không có ô nhập trên màn. Lặp 3 lần, kết quả như nhau. Trạng thái đợt đứng nguyên ở "Đang lập báo cáo".
Đặc tả (srs-fr-15-ct-htpldn.md:802, BA chốt 06/08/2026) quy định rõ: "Ô để trống là chưa điền; giá trị 0 là đã điền (đơn vị không phát sinh hoạt động trong kỳ vẫn phải nộp)". Với 11 chỉ tiêu nói trên thì không có ô nào để trống — không tồn tại ô, và giá trị đang hiển thị là 0. Đặc tả cũng nêu số liệu là thứ hệ thống gợi ý và cán bộ được nhập/chỉnh sửa (:731, :743, :744). Hiện cả hai đường đều không đi được: cán bộ không sửa được 11 chỉ tiêu đó, còn giá trị do chính hệ thống đưa ra thì lại bị chính hệ thống từ chối. Hệ quả là điều kiện nghiệm thu tại :829 (trình báo cáo hoàn chỉnh thì đợt chuyển sang Chờ duyệt kết quả) không thể đạt được bằng thao tác trên màn.
Đã kiểm để loại trừ nguyên nhân khác: bấm [Làm mới] và xác nhận đầy đủ trên hộp thoại (nội dung hộp thoại ghi "Làm mới sẽ cập nhật các chỉ tiêu 1-11 từ hệ thống") thì không phát sinh yêu cầu nào và giá trị không đổi; lưu nháp lại rồi trình lại vẫn bị chặn y hệt. Thử trên một đợt thứ hai áp dụng cả hai biểu mẫu (DOT-TRON_NAM-2026-1) cũng bị chặn cùng cách, nên không phải sự cố của riêng một bản ghi.

ĐỀ NGHỊ VỀ MẶT NGHIỆP VỤ (không ràng buộc cách làm): cần bảo đảm một đơn vị không phát sinh hoạt động trong kỳ — tức mọi chỉ tiêu hệ thống tính ra đều bằng 0 — vẫn trình được báo cáo theo đúng :802, thay vì bị chặn vì chính những chỉ tiêu mà màn hình không cho nhập.

Ghi nhận thêm, KHÔNG thuộc phạm vi phiếu và không ảnh hưởng kết luận:
- Mã lỗi hệ thống trả về là ERR-VAL-XI-07-02, trong khi đặc tả :825 khai ERR-XI-07-01; câu chữ thông báo thì khớp đúng đặc tả.
- Trường trạng thái của bản ghi ĐỢT ở máy chủ vẫn đứng ở "Tạo đợt" kể cả sau khi trình thành công (nhãn người dùng nhìn thấy đang lấy theo trạng thái nộp của từng đơn vị). Đặc tả đang tự mâu thuẫn ở chỗ này: bảng chuyển trạng thái :1512 khai đợt chuyển sang "Đang lập BC" khi cán bộ bắt đầu lập, nhưng phần xử lý của chính chức năng lập báo cáo (:739-:747) không có bước nào đổi trạng thái đợt; thêm nữa một đợt dùng chung cho hàng chục đơn vị mà trường trạng thái đợt chỉ có một giá trị. Vì đặc tả mâu thuẫn nên QA KHÔNG chấm điểm này, chỉ nêu để BA chốt lại mô hình trạng thái.
- Dữ liệu đã lưu có 3 chỉ tiêu (số vụ việc, số doanh nghiệp được hỗ trợ, tổng chi phí) nhưng không dòng nào trên bảng 13 chỉ tiêu hiển thị các giá trị này.

Lưu ý về dữ liệu: để kiểm được vế thông báo và vế nhật ký (vốn nằm sau bước bị chặn), QA đã ép qua tiền đề bằng đường dữ liệu trên đúng đợt DOT-SO_BO_NAM-2026-1, nên đợt này hiện đang ở Chờ duyệt kết quả do QA tác động chứ không phải người dùng thật — có thể đưa về trạng thái cũ sau khi đối tác đọc xong. Kết luận của phiếu chỉ dựa trên phép đo qua giao diện.
