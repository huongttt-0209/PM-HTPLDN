⚠️ Cần BA xác nhận — lỗi đối tác báo đã KHÔNG còn, nhưng còn 1 điểm đặc tả chưa quy định nên chưa chấm Pass được.

[Ghi lại để không mất dấu — vòng 2 đối tác báo: "Hệ thống không chuyển trạng thái thành «Đang lập»".]

Đo ngày 07/08/2026 trên môi trường nội bộ 18.143.165.120.nip.io, bó mã giao diện index-DsMHK7Dp.js (07/08/2026 01:51) — đã kiểm lại tên bó mã ngay trong tab đo. Bằng chứng gốc của đối tác quay trên môi trường khác và trên bản cũ V1.0 ngày 20/07; riêng khiếu nại vòng 2 không kèm file bằng chứng nào, nên QA tự dựng lại đúng luồng phiếu mô tả để đo.
Tài khoản: cbnv_hn (Cán bộ Nghiệp vụ Địa phương — Sở Tư pháp Hà Nội), đúng vai trò và đúng cấp với phiếu; dùng đơn vị này vì các đơn vị địa phương khác đã nộp/đang lập xong nên không còn trạng thái "Chưa nộp" để quan sát phép chuyển. Đợt DOT-SO_BO_NAM-2026-1, biểu mẫu 21a. Thao tác bấm bằng giao diện thật, đối chứng lại bằng dữ liệu máy chủ.

ĐẠT 3/3 điểm mà đặc tả có quy định:
1. Trạng thái nộp của đơn vị chuyển "Chưa nộp" → "Đang lập báo cáo" và GIỮ NGUYÊN sau khi tải lại trang bằng địa chỉ (đúng SRS FR-XI-06, srs-fr-15-ct-htpldn.md:746). Hệ thống đồng thời sinh bản ghi báo cáo gắn vào đơn vị. Đây chính là điểm đối tác báo hỏng ở vòng 2 — KHÔNG tái hiện được.
2. Nội dung báo cáo chi tiết lưu và đọc lại đúng từng chữ sau khi tải lại trang: nhận xét, ghi chú chỉ tiêu và 2 chỉ tiêu nhập tay đều khớp trên cả giao diện lẫn dữ liệu máy chủ (SRS :745).
3. Nhật ký thao tác ghi đủ 3 lượt (1 lượt bắt đầu lập báo cáo + 2 lượt cập nhật số liệu), đúng tài khoản, vai trò, đơn vị và mốc giờ (SRS :747).
Không có hiện tượng gửi trùng: mỗi lần bấm chỉ phát sinh đúng 1 lượt gọi. Mỗi thao tác chỉ hiện 1 thông báo (không lặp lại lỗi thông báo hiện 2 lần của tuần 4).

⚠️ CẦN BA CONFIRM: đối tác kỳ vọng khi lưu nháp thành công hệ thống hiển thị thông báo nhanh "Đã lưu nháp"; đặc tả IM LẶNG về điểm này — FR-XI-06 (srs-fr-15-ct-htpldn.md:701–770) phần Đầu ra chỉ ghi "Báo cáo CT", phần Hậu điều kiện chỉ ghi tạo bản ghi + ghi nhật ký, phần xử lý lỗi chỉ có ERR-XI-06-01, và 2 dòng Tiêu chí chấp nhận đều không nhắc thông báo; dòng mô tả thành phần màn hình :1170 liệt kê nhóm nút [Hủy] [Lưu nháp] [Trình duyệt KQ] mà không đặc tả thông báo, trong khi :1173 (Gửi lên TW) lại ghi rõ "Toast success"; cả file chỉ có 3 mã thông báo INF- (:381, :403, :1032), không mã nào thuộc FR-XI-06.
Thực tế web hiện tại ĐÚNG như kỳ vọng của đối tác: bấm [Lưu nháp] hiện đúng 1 thông báo "Đã lưu nháp thành công", bấm [Lập báo cáo] hiện "Đã bắt đầu lập báo cáo".
Câu hỏi cho BA: (a) Thao tác Lưu nháp ở FR-XI-06 có bắt buộc phản hồi thành công cho người dùng không? (b) Nếu có, câu chữ có bị ràng buộc đúng chuỗi "Đã lưu nháp" hay chỉ cần một thông báo thành công bất kỳ? (c) Nếu BA chốt là bắt buộc, đề nghị bổ sung mã INF-XI-06-* vào bảng thông báo của FR-XI-06 để các vòng sau có căn cứ chấm.
Mục đích hỏi là BỔ SUNG VÀO ĐẶC TẢ, không chặn bàn giao — hiện không còn lỗi nào chưa xử lý ở phiếu này.

Ghi nhận thêm (không thuộc phạm vi phiếu, không ảnh hưởng kết luận): thẻ "Biểu mẫu" và thẻ "Nhận xét, kiến nghị" có 2 nút [Lưu nháp] riêng biệt và không thấy nút [Hủy], trong khi :1170 mô tả một nhóm nút chung có [Hủy]; mỗi thao tác sinh 2 dòng nhật ký cùng mốc giờ (1 dòng cấp nghiệp vụ + 1 dòng cấp giao tiếp). Đặc tả không quy định các điểm này nên chỉ ghi nhận.
