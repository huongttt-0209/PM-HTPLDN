⚠️ CẦN BA XÁC NHẬN — web hiện tại ĐÚNG kỳ vọng của phiếu, chỉ còn một điểm đặc tả chưa quy định nên chưa chấm được.

ĐÃ ĐO
Env nội bộ 18.143.165.120.nip.io, bó mã index-D4Buvu4S.js, tài khoản cbnv_tw_04 (Cán bộ Nghiệp vụ Trung ương), hai hồ sơ TVCS-QLND38-UAT-01 và TVCS-QLND38-UAT-02, cả hai đang "Tiếp nhận", cùng lĩnh vực Thương mại, cùng đơn vị tài khoản đo. Đo lúc 07/08/2026 02:33-02:42 bằng thao tác thật trên giao diện.

KIỂM TRƯỚC ĐỂ KHÔNG BÁO OAN
Trước khi bấm, đã mở cửa sổ phân công của một hồ sơ Thương mại khác để chắc chắn danh sách chuyên gia không rỗng, rồi đóng lại không xác nhận. Có 2 chuyên gia đang hoạt động và cả hai đều phủ lĩnh vực Thương mại. Như vậy loại được khả năng "cửa sổ rỗng vì đơn vị không có chuyên gia".

ĐÃ HẾT LỖI
1) Mỗi dòng danh sách đều có ô chọn. Tích 2 dòng thì hiện thanh "Đã chọn 2 bản ghi" kèm nút "Phân công hàng loạt (2)" ở trạng thái bấm được.
2) Bấm nút đó thì hệ thống MỞ cửa sổ "Phân công chuyên gia" (cảnh báo thời hạn 2 ngày làm việc, ô chọn chuyên gia bắt buộc, ô ghi chú, nút Hủy và Phân công). Quét toàn trang KHÔNG còn chuỗi "chưa được hỗ trợ", và bộ bắt thông báo ghi nhận 0 khung thông báo trong 2,5 giây sau khi bấm. Đây chính là triệu chứng bên kiểm thử báo trước đây, nay không còn tái hiện.
3) Chọn chuyên gia rồi xác nhận: đúng 1 lời gọi tới máy chủ và đúng 1 thông báo "Đã phân công chuyên gia cho 2 yêu cầu", không nhân đôi.
4) Tải lại danh sách bằng địa chỉ rồi đọc lại TỪNG mã: cả 2/2 hồ sơ đều đã có chuyên gia "Chuyên gia UAT QLNDTVVCG 38" và đã rời khỏi "Tiếp nhận". Đọc lại từ máy chủ cũng cho cả 2 hồ sơ cùng trạng thái đã phân công, cùng một mã chuyên gia, thời điểm phân công cách nhau 2 phần nghìn giây, tức một thao tác duy nhất chứ không phải hai lần phân công lẻ.

VỀ ẢNH BẰNG CHỨNG CŨ
Ảnh của bên kiểm thử chụp trên môi trường nghiệm thu, bản dựng cũ hơn (chân trang ghi V1.0, tên các thẻ phân loại cũng khác). Trong ảnh đó, lời từ chối viện dẫn chính srs-fr-12 để nói không hỗ trợ hàng loạt; nhưng đặc tả srs-fr-12 lại quy định phải có nút phân công chuyên gia hàng loạt cho bản ghi Tiếp nhận, và quy định này đã có từ bản 3. Lý do "để chuyên gia khớp lĩnh vực từng yêu cầu" cũng không đứng vững vì đặc tả chỉ buộc KIỂM chuyên môn khớp lĩnh vực, không cấm thao tác theo lô. Bản đang chạy trên env đo đã làm đúng đặc tả.

CHƯA CHẤM ĐƯỢC - CẦN BA CHỐT
Phiếu kỳ vọng "áp dụng chuyên gia đã chọn cho tất cả yêu cầu được chọn đồng thời", tức một chuyên gia chung. Đặc tả chỉ nói có nút phân công hàng loạt cho bản ghi Tiếp nhận, KHÔNG nói chọn một chuyên gia chung hay chọn riêng cho từng hồ sơ trong cùng cửa sổ; khối xử lý phân công chỉ mô tả một bản ghi; module tương tự bên Chuyên gia lại dùng khuôn nhập riêng từng hồ sơ. Vì đặc tả im lặng nên không có chuẩn để chấm vế này, dù hiện trạng web đang đúng ý phiếu.
Câu hỏi cho BA: với phân công chuyên gia hàng loạt của Tư vấn chuyên sâu, cán bộ chọn MỘT chuyên gia áp cho mọi hồ sơ đã chọn, hay chọn chuyên gia RIÊNG cho từng hồ sơ trong cùng một cửa sổ? Nếu là một chuyên gia chung thì xử lý thế nào khi các hồ sơ đã chọn thuộc lĩnh vực khác nhau, trong khi bước kiểm của khối phân công buộc chuyên môn phải phù hợp lĩnh vực?
Lượt đo này cố ý chọn 2 hồ sơ CÙNG lĩnh vực để không lẫn với tình huống bị từ chối do lệch chuyên môn, nên chưa có dữ kiện cho tình huống khác lĩnh vực. Đó đúng là phần BA cần chốt trước khi bổ sung đặc tả.

HIỆN TRẠNG CỦA VẾ CẦN BA
Cửa sổ chỉ có một ô chọn chuyên gia và một ô ghi chú, không có bảng nhập riêng cho từng hồ sơ; một lời gọi duy nhất áp cho cả hai hồ sơ. Tức là web đang làm ĐÚNG kỳ vọng của phiếu. Ghi rõ để không ai đọc nhầm thành lỗi chưa xử lý.

LỖI MỚI PHÁT SINH NGOÀI DÒNG NÀY
Nhãn trạng thái trên màn danh sách lệch với bảng nhãn của đặc tả: trạng thái đã phân công hiện chữ "Phân công" trong khi đặc tả ghi "Đã phân công"; trạng thái hủy hiện chữ "Hủy" trong khi đặc tả ghi "Đã hủy". Hai trạng thái còn lại nhìn thấy trong lượt đo (Tiếp nhận, Đã duyệt) thì khớp. Đã ghi thành dòng lỗi riêng ở cuối bảng, mã QLNDTVVCG_QA01. Điểm này không kéo kết quả của dòng 288 vì phiếu không yêu cầu về câu chữ nhãn, và việc chuyển trạng thái đã được máy chủ xác nhận đúng.

DỮ LIỆU ĐÃ THAY ĐỔI TRÊN MÔI TRƯỜNG
Hai hồ sơ TVCS-QLND38-UAT-01 và TVCS-QLND38-UAT-02 đã chuyển từ "Tiếp nhận" sang đã phân công cho "Chuyên gia UAT QLNDTVVCG 38", ghi chú phân công QA-QLND38-20260807-0240. Hai hồ sơ này không dùng lại được cho lượt đo sau vì đã rời trạng thái Tiếp nhận; muốn đo lại thì tạo hồ sơ mới bằng nút Thêm yêu cầu tư vấn, hoặc dùng các hồ sơ Tiếp nhận cùng lĩnh vực Thương mại còn lại trên môi trường. Không đụng dữ liệu của đối tác.

BẰNG CHỨNG
2 dòng đã tích, thanh "Đã chọn 2 bản ghi" và nút "Phân công hàng loạt (2)": https://drive.google.com/file/d/1g6slPeM0HYr2cwJGSBQ8AoJLviPb5qKY/view?usp=drivesdk
Chụp NGAY SAU khi bấm nút hàng loạt, cửa sổ phân công mở ra - đây là ảnh đối chiếu trực tiếp với ảnh bằng chứng cũ: https://drive.google.com/file/d/1bkN7ZF4kZE3Sl7jp-WDb0W6eJhYEati-/view?usp=drivesdk
Sau khi tải lại danh sách, cả 2 hồ sơ đã có chuyên gia: https://drive.google.com/file/d/1IHJIesPwbhZCFP0HNUVFqEzpco7yB3LV/view?usp=drivesdk

GIỚI HẠN
Kết luận chỉ có hiệu lực cho env nội bộ và bó mã index-D4Buvu4S.js đã đo; bên kiểm thử đo trên môi trường nghiệm thu với bản dựng cũ hơn. Không có ảnh lỗi cũ do chính bên kiểm thử của phía này chụp, nên đây là kết luận về hiện trạng đúng so với đặc tả, không phải kết luận về việc bản sửa có tác dụng hay không. Lượt đo chỉ với 2 hồ sơ cùng lĩnh vực và cùng đơn vị; chưa đo tình huống chọn hồ sơ khác lĩnh vực, chọn lẫn dòng khác trạng thái, chọn dòng khác đơn vị, hoặc chọn số lượng lớn - các tình huống này nằm ngoài yêu cầu của phiếu.
