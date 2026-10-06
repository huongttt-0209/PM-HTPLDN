🔁 CÒN LỖI Ở ĐÂU
Công khai hàng loạt: hồ sơ bị từ chối vẫn hiện "Đã công khai tư vấn viên thành công". Bấm riêng 1 hồ sơ Tư vấn viên thiếu Số thẻ hành nghề: tải lại trang 0/1 được công khai. Bấm lô 2 hồ sơ (1 đủ điều kiện, 1 thiếu số thẻ): chỉ 1/2 được công khai, thông báo vẫn báo thành công, không nêu hồ sơ nào trượt và vì sao.

VÌ SAO LÀ LỖI
Từ chối hồ sơ thiếu số thẻ là ĐÚNG (srs-fr-04-chuyen-gia-tvv.md:1507). Cái sai là báo thành công sai sự thật: thông báo thành công chỉ được hiện khi thao tác đã có hiệu lực (srs-v3.5.md:6772), còn ca từ chối phải nêu rõ lý do (:681, :682).

ĐÃ HẾT LỖI
Cửa sổ nhập mô tả mở đúng, câu xác nhận đúng số hồ sơ đã chọn. Một hồ sơ hỏng KHÔNG còn kéo đổ cả lô: hồ sơ hợp lệ cùng lô đã công khai đủ mô tả, cờ công khai và thời gian đăng tải.

ĐÃ ĐO
3 hồ sơ x 3 dạng (Chuyên gia; TVV có số thẻ; TVV không số thẻ) x lô 1 và 2 dòng = 4 lượt bấm thật, mỗi lượt tải lại trang đếm số hồ sơ thực sự chuyển "Công khai".

── CÁCH VERIFY sau Dev fix ──
Precondition: tài khoản cbnv_tw_02 / Test@1234 — vai trò Cán bộ Nghiệp vụ Trung ương, đơn vị Cục Bổ trợ
  tư pháp - Bộ Tư pháp. Màn: Mạng lưới Tư vấn viên → Tư vấn viên / Chuyên gia → tab "Đang hoạt động".
  Dữ liệu phải có sẵn: 3 hồ sơ đang "Đang hoạt động" + "Chưa công khai", đủ 3 biến thể khác nhau —
   (i) loại Chuyên gia (CG-QLND38-UAT);
   (ii) loại Tư vấn viên CÓ Số thẻ hành nghề (TVV-BTP-TW-0016, số thẻ THN-TW-2026-016 — đã dựng sẵn 07/08);
   (iii) loại Tư vấn viên KHÔNG có Số thẻ hành nghề (TVV-SEED-0001) — biến thể quan trọng nhất.
   Hồ sơ nào đang "Công khai" thì dùng chính nút [Hủy công khai] để đưa về "Chưa công khai" trước khi đo.
1) Tích 1 hồ sơ loại (iii) → [Công khai lên Cổng PLQG] → nhập mô tả bất kỳ → xác nhận.
   Đọc NGUYÊN VĂN câu thông báo hiện ra, rồi TẢI LẠI TRANG và đọc cột "Công khai" của đúng hồ sơ đó.
2) Tích CÙNG LÚC 2 hồ sơ: 1 cái loại (ii) + 1 cái loại (iii) → nhập mô tả → xác nhận → tải lại trang →
   đếm xem MẤY TRÊN 2 hồ sơ thực sự chuyển sang "Công khai".
3) Lặp bước 2 nhưng chỉ tích riêng hồ sơ loại (ii) — để biết hồ sơ đó tự nó có công khai được không.
4) Mở màn chi tiết từng hồ sơ vừa thao tác, tab "Hồ sơ", đọc nhóm "Thông tin công khai": phải có đủ
   mô tả vừa nhập + thời gian đăng tải.
5) Đo bằng đường thứ hai: xem phản hồi máy chủ của chính lượt bấm đó — phải đọc từng hồ sơ trong danh
   sách kết quả, không chỉ nhìn trạng thái chung; rồi đọc lại bản ghi để so với màn hình.
✅ PASS khi: (a) với hồ sơ không đủ điều kiện, hệ thống báo TỪ CHỐI rõ hồ sơ nào không đạt và vì sao
   (KHÔNG được báo thành công), VÀ (b) với lô có lẫn hồ sơ hỏng, những hồ sơ hợp lệ còn lại vẫn phải
   được công khai đủ (hoặc hệ thống chặn cả lô nhưng NÓI RÕ là không hồ sơ nào được công khai), VÀ
   (c) mọi hồ sơ báo thành công đều đủ 4 kết cục sau khi tải lại: mô tả đúng nguyên văn · cờ công khai bật ·
   nhóm "Thông tin công khai" hiện ra · thời gian đăng tải bám đúng thời điểm bấm, VÀ (d) số hồ sơ chuyển
   sang "Công khai" sau khi tải lại đúng bằng số hồ sơ mà thông báo nói là đã công khai.
❌ FAIL nếu: báo thành công mà tải lại trang hồ sơ vẫn "Chưa công khai" — kể cả khi chỉ sai 1 hồ sơ trên 2;
   hoặc 1 hồ sơ hỏng vẫn kéo đổ những hồ sơ hợp lệ khác mà người dùng không được báo; hoặc người dùng
   không biết hồ sơ nào không đạt và vì sao; hoặc thời gian đăng tải trống dù cờ công khai đã bật.
⚠️ Đừng chấm Fail vì không thấy phần mềm gọi sang Cổng pháp luật quốc gia, hay vì Cổng chưa hiển thị
   ngay: đặc tả srs-fr-04-chuyen-gia-tvv.md:645 và :686 chốt mô hình KÉO — phần mềm chỉ đặt cờ, Cổng tự
   kéo định kỳ. Cũng đừng chấm Fail vì câu chữ của cửa sổ xác nhận hay nhãn nút, và đừng chấm Fail khi
   hệ thống từ chối ĐÚNG lúc bỏ trống mô tả (:682) hay khi hồ sơ không ở trạng thái cho phép (:681).
⚠️ KHÔNG được đòi hệ thống công khai được hồ sơ loại Tư vấn viên thiếu Số thẻ hành nghề: đặc tả
   srs-fr-04-chuyen-gia-tvv.md:1507 ghi "Bắt buộc nếu Loại = Tư vấn viên" nên việc máy chủ từ chối là
   ĐÚNG. Phần phải sửa là: báo thành công sai sự thật, và không cho người dùng biết hồ sơ nào không đạt.
⚠️ Đừng kết luận "đã fix" khi chỉ thấy cửa sổ nhập mô tả mở ra được — phần đó vốn đã chạy đúng từ lượt đo
   06/08. Cũng đừng kết luận từ thông báo thành công, và đừng kết luận từ trạng thái chung của phản hồi
   máy chủ — hiện nay phản hồi báo "thành công" ở vỏ ngoài trong khi bên trong có hồ sơ thất bại.
   Phép đo quyết định là: TẢI LẠI TRANG rồi ĐẾM số hồ sơ thực sự đã chuyển sang "Công khai".
⚠️ Hai phần ĐÃ ĐẠT ở bản dựng V1.0.10, đừng làm hỏng lại khi sửa tiếp: (1) một hồ sơ bị từ chối KHÔNG còn
   kéo đổ cả lô — hồ sơ hợp lệ cùng lô vẫn được công khai đủ; (2) lý do từ chối máy chủ trả về đã là câu
   nghiệp vụ đọc được, không còn lộ nguyên văn ràng buộc của cơ sở dữ liệu.
⚠️ Biến thể dễ bị bỏ sót: hồ sơ loại Tư vấn viên KHÔNG có Số thẻ hành nghề. Chỉ đo hồ sơ Chuyên gia hoặc
   hồ sơ có số thẻ thì sẽ thấy "chạy được" và bỏ lọt toàn bộ lỗi này.
⚠️ Kiểm thêm sau khi fix: lượt bấm hỏng (nếu còn) không được ghi đè mô tả công khai cũ của hồ sơ.
Ảnh lỗi lần này: image/CNDSMLTVV_01-R3-03-luot2-lo-2-ho-so-thong-bao.png +
   image/CNDSMLTVV_01-R3-08-ma-tvv-va-cot-cong-khai-day-du.png
