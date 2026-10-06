⚠️ Cần BA xác nhận — lỗi "Forbidden" ĐÃ HẾT và thao tác gửi lên Trung ương nay chạy trót lọt, 4/5 vế kỳ vọng đều đạt. Chỉ còn vế "chuyển trạng thái ĐỢT báo cáo" chưa chốt được, vì cùng một đợt lại hiện hai trạng thái khác nhau tùy vai trò người xem, mà đặc tả đang tự mâu thuẫn ở đúng chỗ này.

Đo ngày 07/08/2026 trên môi trường nội bộ 18.143.165.120.nip.io, bó mã giao diện index-D4Buvu4S.js — đã tải lại trang bằng địa chỉ và đọc lại tên bó mã ngay trong tab ở cả hai nhịp đo.
Tài khoản bấm gửi: cbnv_hn (Cán bộ Nghiệp vụ Địa phương — Sở Tư pháp Hà Nội), đúng vai trò và đúng cấp theo đặc tả. Tiền đề phê duyệt kết quả do cbpd_hn (Cán bộ Phê duyệt CÙNG đơn vị, đã đối chiếu trùng mã đơn vị) thực hiện. Vế phía Trung ương đo bằng tài khoản cbnv_tw đăng nhập riêng, không dùng tài khoản quản trị. Đợt đo: DOT-SO_BO_NAM-2026-1, phạm vi 83 đơn vị.

PHẦN ĐÃ ĐẠT:
- Trước khi bấm, màn Chi tiết đợt đọc được "Đã duyệt kết quả" và có nút [Gửi lên TW]. Bấm nút → hộp xác nhận "Gửi báo cáo lên TW? Sau khi gửi, báo cáo của đơn vị sẽ chuyển sang trạng thái Đã nộp" → [Đồng ý]: thao tác thành công, KHÔNG còn thông báo "Forbidden".
- Hệ thống hiện thông báo nhanh đúng nguyên văn câu đối tác kỳ vọng: "Đã gửi báo cáo lên Trung ương". Đúng 1 thông báo cho 1 lần bấm, không hiện trùng.
- Ghi nhận thời điểm gửi: mốc gửi lưu lại là 07/08/2026 03:11:24 (giờ VN), lệch khoảng một phần mười giây so với lúc bấm xác nhận. Trên màn Chi tiết đợt (vai trò Trung ương) có bảng "Tiến độ nộp theo đơn vị", trong 83 dòng chỉ đúng một dòng "Đã nộp" — Sở Tư pháp Hà Nội, cấp DP, ngày nộp 07/08/2026.
- Vào danh sách tổng hợp của cấp Trung ương: đọc bằng chính phiên của cán bộ nghiệp vụ Trung ương, có dòng khớp đủ ba yếu tố mã đợt + tên đơn vị + ngày gửi.
- Thông báo cho cán bộ nghiệp vụ Trung ương: có, trùng mốc giờ, tiêu đề "Đơn vị đã nộp BC đợt DOT-SO_BO_NAM-2026-1 lên TW".
- Lưu vết thao tác: nhật ký hệ thống có mục ứng với lần gửi, đúng tài khoản cbnv_hn, đúng mốc giờ; bước phê duyệt tiền đề cũng được ghi đúng tài khoản cbpd_hn.
- Đo trạng thái hai nhịp theo yêu cầu: ngay sau thao tác và sau khi tải lại trang bằng địa chỉ — cả hai nhịp màn của đơn vị vừa gửi đều đọc được "Đã gửi TW", thanh tiến trình nhảy sang bước 5.

PHẦN CẦN BA QUYẾT — vì sao chưa chốt hết lỗi được:
Cùng một đợt DOT-SO_BO_NAM-2026-1, sau khi gửi thành công:
- Màn của cán bộ Địa phương (người vừa gửi) đọc: "Đã gửi TW".
- Màn của cán bộ Trung ương (bên nhận) đọc: "Tạo đợt" — cả ở danh sách đợt lẫn ở Chi tiết đợt. Tab lọc "Đã gửi TW" trong danh sách đợt của Trung ương đang rỗng, không có đợt vừa gửi.
Dữ liệu nguồn cho thấy trạng thái, dấu đã-gửi và thời điểm gửi đều được ghi ở bản ghi THEO TỪNG ĐƠN VỊ, còn bản ghi ĐỢT thì không đổi.
Đặc tả đang tự mâu thuẫn đúng ở chỗ này: :937 (chức năng gửi TW) yêu cầu chuyển trạng thái ĐỢT sang "Đã gửi TW", đánh dấu đã gửi và ghi thời điểm gửi; nhưng :938 ngay sau đó lại quy định chính ba việc ấy ở cấp ĐƠN VỊ; trong khi :1368 chỉ cho mỗi đợt MỘT giá trị trạng thái, mà một đợt lại dùng chung cho 83 đơn vị (:621, :646, :1398). Ba dòng này không thể cùng đúng khi các đơn vị đang ở những bước khác nhau. Vì đặc tả mâu thuẫn, QA không được phép tự chọn bên nào là đúng, nên không chốt Pass và cũng không mở lại lỗi cho vế này.

⚠️ CẦN BA CONFIRM:
(1) Trạng thái mà người dùng nhìn thấy ở màn Chi tiết đợt phải là trạng thái CỦA ĐƠN VỊ MÌNH hay trạng thái chung CỦA ĐỢT? Hiện phần mềm đang cho cán bộ Địa phương thấy trạng thái của đơn vị, còn cán bộ Trung ương thấy trạng thái của đợt — nên hai vai trò đọc ra hai kết quả khác nhau cho cùng một đợt.
(2) Nếu chốt theo trục ĐƠN VỊ, đề nghị phát biểu lại :937 cho khớp :938 (bỏ phần chuyển trạng thái đợt), đồng thời làm rõ khi nào thì trạng thái chung của ĐỢT mới đổi — vì hiện tại đợt đứng nguyên ở "Tạo đợt" suốt cả vòng đời, kể cả khi đã có đơn vị nộp xong.
(3) Bộ lọc "Đã gửi TW" ở danh sách đợt của Trung ương nên hiểu thế nào: liệt kê đợt có ít nhất một đơn vị đã gửi, hay chỉ đợt mà toàn bộ đơn vị đã gửi?
Mục đích là làm rõ mô hình trạng thái trong đặc tả, KHÔNG chặn bàn giao — chức năng gửi lên Trung ương đã dùng được bình thường và đầy đủ.

Ghi nhận thêm, KHÔNG thuộc phạm vi phiếu và không ảnh hưởng kết luận:
- Đã truy được nguồn của chữ "Forbidden" mà phiếu mô tả: nếu dùng tài khoản CẤP TRUNG ƯƠNG để gọi chức năng gửi lên Trung ương thì hệ thống chặn với đúng chữ "Forbidden". Việc chặn là ĐÚNG đặc tả (:918, :922 quy định chỉ cán bộ nghiệp vụ Bộ/Ngành hoặc Địa phương mới được gửi), nên đây không phải lỗi. Tuy nhiên thông điệp trả về là chuỗi tiếng Anh thô kèm mã quyền chung, không phải thông điệp tiếng Việt mà đặc tả đã khai sẵn cho chức năng này (:962 "Đợt BC chưa được phê duyệt kết quả" và :963 "Chỉ đơn vị BN/ĐP mới gửi BC lên TW"). Đề nghị dev gắn đúng thông điệp đã đặc tả để người dùng hiểu vì sao bị chặn.
- Thông báo gửi cho cán bộ Trung ương chỉ nêu mã đợt, không nêu tên đơn vị đã nộp; đặc tả không quy định nội dung nên chỉ nêu để BA cân nhắc, vì một đợt có tới 83 đơn vị.
- Một lần gửi sinh 2 mục nhật ký cùng mốc giờ; đặc tả không quy định số mục nên chỉ ghi nhận.

Lưu ý về dữ liệu: bước phê duyệt kết quả là tiền đề do QA dựng để đo được phiếu này; đợt DOT-SO_BO_NAM-2026-1 hiện đang ở trạng thái đã nộp lên Trung ương do QA thao tác chứ không phải người dùng thật, có thể đưa về trạng thái cũ sau khi đối tác đọc xong. QA chủ động KHÔNG bấm nút [Tổng hợp] ở màn Trung ương vì đó là chức năng khác, ngoài phạm vi phiếu.
