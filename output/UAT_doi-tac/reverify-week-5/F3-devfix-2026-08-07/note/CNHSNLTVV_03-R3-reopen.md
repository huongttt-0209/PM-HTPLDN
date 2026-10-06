🔁 CÒN LỖI Ở ĐÂU
Lưu năng lực có đính tệp chứng chỉ nay báo thành công, nhưng tệp vừa đính không hiện tên: màn Năng lực chỉ hiện một chuỗi ký tự kỹ thuật thay cho tên tệp. Nặng hơn, từ khi hồ sơ đã có tệp chứng chỉ thì bấm [Cập nhật năng lực] lại bị chuyển sang trang báo không có quyền truy cập — hồ sơ đó không sửa năng lực được nữa. Tái hiện 3/3 hồ sơ.

VÌ SAO LÀ LỖI
srs-fr-04-chuyen-gia-tvv.md:432 — Người hỗ trợ cùng đơn vị nhấn "Cập nhật năng lực" thì form phải mở. :425-:429 chỉ cho từ chối vì 5 lý do (khác đơn vị, tệp quá cỡ, tổng quá cỡ, mã độc, hồ sơ vô hiệu hóa), không có lý do "hồ sơ đã có chứng chỉ đính tệp". :418 hồ sơ năng lực phải được cập nhật.

ĐÃ HẾT LỖI
Câu "Lỗi hệ thống, vui lòng thử lại sau." không còn: 4/4 lượt lưu có đính tệp đều báo thành công, dữ liệu vào máy chủ thật.

ĐÃ ĐO
5 lượt bấm Lưu thật trên 3 hồ sơ (Đang hoạt động · Mới đăng ký · Yêu cầu bổ sung), đủ 3 dạng: không tệp · tệp tên đặc biệt · tệp tên thường. Mỗi lượt 1 yêu cầu — 1 thông báo, không lặp.

── CÁCH VERIFY sau Dev fix ──
Precondition: tài khoản nht_qa_tw / Test@1234 — vai trò Người hỗ trợ pháp lý, đơn vị Cục Bổ trợ tư pháp -
  Bộ Tư pháp, cấp TW. Màn: Mạng lưới Tư vấn viên → Tư vấn viên / Chuyên gia → mở hồ sơ → tab "Năng lực" →
  [Cập nhật năng lực].
  Dữ liệu phải có sẵn: 3 hồ sơ cùng đơn vị với tài khoản trên, và cả 3 đều đã có sẵn phần năng lực (mở tab
   "Năng lực" thấy có Trình độ hoặc Số thẻ hành nghề, không phải toàn dấu "—") —
   (i) 1 hồ sơ Đang hoạt động ĐÃ có chứng chỉ kèm tệp từ trước, ví dụ TVV-BTP-TW-0002;
   (ii) 1 hồ sơ Mới đăng ký, dòng "Chứng chỉ chi tiết" còn là dấu "—", ví dụ TVV-BTP-TW-0037;
   (iii) 1 hồ sơ Yêu cầu bổ sung, dòng "Chứng chỉ chi tiết" còn là dấu "—", ví dụ TVV-BTP-TW-0026.
   Thiếu thì tạo bằng luồng chuẩn: Tư vấn viên / Chuyên gia → [Thêm mới] → điền hồ sơ tối thiểu → lưu.
  Cần thêm: 2 tệp PDF nhỏ (dưới 1 MB) — 1 tệp đặt tên có dấu cách, ngoặc đơn và dấu & (ví dụ
   "2K15 T3 (4.8) & CN (9.8).pdf"), 1 tệp tên chỉ có chữ/số/gạch nối. Cả 2 tệp đã có sẵn trong seed-files/.
1) Trên hồ sơ (i) — hồ sơ SẴN CÓ chứng chỉ kèm tệp: bấm [Cập nhật năng lực]. Form phải mở ra tại chỗ.
   Nếu bị chuyển sang trang báo không có quyền truy cập thì lỗi còn nguyên, ghi lại rồi đo tiếp các bước sau.
2) Trên hồ sơ (ii): mở form, KHÔNG đính tệp, chỉ sửa Trình độ + Kinh nghiệm chi tiết → [Lưu].
   Đây là lượt đối chứng, phải lưu được.
3) Trên hồ sơ (ii): mở lại form, ở khối "Thêm chứng chỉ mới" đính tệp tên có ký tự đặc biệt, nhập Ghi chú
   cập nhật = "a" → [Lưu]. Đọc nguyên văn thông báo hiện ra.
4) Lặp bước 3 trên hồ sơ (iii) với tệp tên thường.
   ⇒ tổng cộng 3 lượt bấm [Lưu]: 1 lượt không tệp + 2 lượt có tệp, cộng lượt mở form ở bước 1.
5) Sau MỖI lượt lưu: tải lại trang, mở lại tab "Năng lực", đọc dòng "Chứng chỉ chi tiết" — phải thấy TÊN TỆP
   vừa đính, không được là một chuỗi ký tự kỹ thuật.
6) Sau MỖI lượt lưu: bấm lại [Cập nhật năng lực] trên chính hồ sơ vừa lưu — form phải mở lại được, và khối
   "Chứng chỉ hiện có" phải liệt kê tệp vừa đính đúng tên, xem/tải được.
7) Đo bằng đường thứ hai: xem phản hồi máy chủ của chính lượt bấm lưu đó, đọc lại bản ghi hồ sơ qua máy chủ
   để so với những gì màn hình đang hiện, và thử mở chính tệp vừa đính qua đường đọc tệp của máy chủ.
✅ PASS khi: đủ 3/3 lượt lưu đều báo thành công, VÀ sau khi tải lại trang thì tệp vừa đính hiện ĐÚNG TÊN ở
   dòng "Chứng chỉ chi tiết" và trong khối "Chứng chỉ hiện có", VÀ mở lại được form [Cập nhật năng lực] trên
   hồ sơ đã có tệp chứng chỉ — cả hồ sơ (i) sẵn có tệp lẫn 2 hồ sơ vừa đính, VÀ phản hồi máy chủ của cả 3 lượt
   đều là thành công và tệp vừa đính đọc lại được, VÀ mỗi lượt chỉ sinh đúng 1 thông báo (đếm theo mốc giờ
   khác nhau, không đếm số phần tử).
❌ FAIL nếu: bất kỳ lượt nào báo lỗi hoặc máy chủ trả lỗi — kể cả khi chỉ hỏng ở 1 trong 2 kiểu tên tệp, hoặc
   chỉ hỏng ở 1 trong các hồ sơ. Cũng FAIL nếu báo thành công nhưng tải lại trang thì tệp không hiện đúng tên,
   hoặc hiện ra một chuỗi ký tự kỹ thuật thay cho tên tệp. Cũng FAIL nếu sau khi hồ sơ đã có tệp chứng chỉ thì
   bấm [Cập nhật năng lực] bị chuyển sang trang báo không có quyền truy cập, khiến hồ sơ đó không còn sửa
   năng lực được nữa.
⚠️ Đừng chấm Fail vì nhãn nút là "Lưu" thay vì "Đồng ý", vì form là inline thay vì hộp thoại, hay vì câu
   chữ cụ thể của thông báo THÀNH CÔNG — đặc tả srs-fr-04-chuyen-gia-tvv.md:432 không chốt những thứ đó.
   Cũng đừng chấm Fail khi hệ thống từ chối ĐÚNG theo :425-:429 (tệp quá 10MB, tổng quá 50MB, có mã độc,
   khác đơn vị, hồ sơ đã vô hiệu hóa) — đó là hành vi đúng.
⚠️ Đừng kết luận "đã fix" khi chỉ thấy lượt lưu báo thành công: lần đo 07/08 cả 4 lượt có tệp đều báo thành
   công mà vẫn chưa đạt. Phép đo quyết định là 2 việc SAU khi lưu — tệp có hiện đúng TÊN không, và có mở lại
   được form trên hồ sơ đã có tệp không. Cũng đừng kết luận từ việc bước tải tệp lên trả về thành công:
   bước đó vốn đã chạy được, chỗ hỏng nằm sau nó.
⚠️ Hồ sơ đang ở "Yêu cầu bổ sung" sau khi lưu năng lực sẽ tự chuyển sang "Đang thẩm định" — đó là hành vi
   ĐÚNG theo srs-fr-04-chuyen-gia-tvv.md:405, không phải lỗi.
⚠️ Kiểm thêm: lượt lưu hỏng (nếu còn) không được để lại tệp thừa trên hồ sơ. Cách đọc: mở tab "Hồ sơ" →
   khối "File đính kèm", đếm số tệp trước và sau lượt bấm.
