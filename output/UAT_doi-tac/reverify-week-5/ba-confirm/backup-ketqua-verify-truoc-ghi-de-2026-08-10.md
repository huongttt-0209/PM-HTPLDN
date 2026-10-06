# Sao lưu cột `Kết quả verify` — TRƯỚC khi ghi đè verdict sau BA

**Ngày sao lưu:** 10/08/2026 · tab `bug`, sheet `1OKBN2otlmdZ44THkmhtsn-_63M2Boh7zQwearwjYR3s`

Ghi đè theo yêu cầu của QA (chốt 10/08/2026). File này giữ nguyên văn nội dung cũ,
**gồm cả link Drive bằng chứng**, để khôi phục được nếu cần.

---

## Dòng 32 — `QLTVV_02`

- Trạng thái dev fix lúc sao lưu: `Bug`
- Độ dài nội dung cũ: 2101 ký tự

```text
✅ Bug đúng (BA duyệt 09/08/2026 — phiếu 34 điểm tuần 5, mục 27). Dev BE: danh sách Tư vấn viên/Chuyên gia phải sắp mặc định theo NGÀY CẬP NHẬT mới nhất trước, theo quy ước dữ liệu chung DG-06 áp cho mọi màn danh sách; bản ghi chưa từng cập nhật thì lấy theo thời gian tạo để xếp chỗ. Hiện phần mềm đang sắp theo ngày tạo bản ghi nên phải sửa. Mức Minor.
LƯU Ý PHẠM VI: BA BÁC vế "ngày công nhận" trong Kết quả mong đợi của phiếu — tiêu chí đó không có căn cứ ở bất kỳ chỗ nào trong đặc tả. Đối tác được đề nghị sửa Kết quả mong đợi thành "mặc định sắp theo thời gian cập nhật mới nhất trước, 20 bản ghi mỗi trang". 4/5 vế còn lại của phiếu (tràn cột Điểm ĐG · hiển thị điểm đồng nhất · nút thao tác xuống dòng · 20 mục/trang) đã hết lỗi từ lượt đo 06/08/2026.

── CÁCH VERIFY sau Dev fix ──
Precondition: cbnv_tw / Test@1234 (Cán bộ Nghiệp vụ Trung ương). Mạng lưới tư vấn viên → Tư vấn viên/Chuyên gia, tab "Đang hoạt động". KHÔNG đụng bộ lọc, KHÔNG bấm tiêu đề cột (đang đo thứ tự MẶC ĐỊNH).
1) Mở danh sách ở trạng thái mặc định. Ghi lại thứ tự mã TVV của trang 1 (20 dòng).
2) Đọc ngày cập nhật của từng dòng trang 1 — lấy ở phản hồi của lượt tải danh sách, hoặc mở lần lượt 3 hồ sơ đầu để đối chiếu.
3) Chọn 1 hồ sơ đang nằm CUỐI trang 1, sửa một trường vô hại (ví dụ ô mô tả/ghi chú) rồi Lưu.
4) Quay lại danh sách, tải lại trang, KHÔNG đụng bộ lọc.
✅ PASS khi: (a) thứ tự trang 1 giảm dần theo ngày cập nhật — không dòng nào có ngày cập nhật MỚI HƠN dòng đứng trên nó; (b) sau bước 3, hồ sơ vừa sửa nhảy lên DÒNG ĐẦU TIÊN của danh sách; (c) mặc định vẫn đúng 20 bản ghi/trang.
❌ FAIL nếu: hồ sơ vừa sửa ở bước 3 KHÔNG nhảy lên đầu (tức vẫn sắp theo ngày tạo); hoặc thứ tự tăng dần; hoặc mặc định khác 20 dòng/trang.
⚠️ Bẫy 1 — KHÔNG chấm theo "ngày công nhận" như phiếu gốc ghi: BA đã bác vế đó. Danh sách sắp theo ngày công nhận là FAIL, không phải PASS.
⚠️ Bẫy 2 — hồ sơ chưa từng cập nhật xếp theo thời gian tạo; thấy nhóm này xen kẽ theo ngày tạo thì KHÔNG log lỗi.
⚠️ Bẫy 3 — chỉ chấm vế thứ tự sắp xếp. Bốn vế còn lại của phiếu đã đóng ở lượt 06/08, đừng mở lại.
Ảnh lỗi cũ: QLTVV_02.webm
```

---

## Dòng 35 — `DKTGMLTVV_13`

- Trạng thái dev fix lúc sao lưu: `Bug`
- Độ dài nội dung cũ: 3756 ký tự

```text
✅ Bug đúng MỘT PHẦN (BA duyệt 09/08/2026 — phiếu 34 điểm tuần 5, mục 8 · 9 · 12 · 12b). Dòng này gộp 4 vế, chỉ 1 vế là lỗi cần Dev sửa.

CẦN DEV SỬA — 1 vế (mục 12, Loại 4 hướng B): Dev FE ghép mã hồ sơ vừa sinh vào câu thông báo sau khi đăng ký thành công. Căn cứ BA đưa: bản bàn giao HTPLDN-PTYC-CT-v3.5.docx mục 4.4.3.2.3 đã ghi "…báo 'Đăng ký thành công, chờ thẩm định' kèm mã tư vấn viên vừa sinh"; bản gốc .md bị SÓT vế này chứ không phải bỏ có chủ đích (không có quyết định nào loại bỏ mã khỏi thông báo trên màn). Dữ liệu đã sẵn — máy chủ vốn trả mã TVV ngay trong phản hồi của lượt tạo. Mức Minor.

KHÔNG PHẢI LỖI — 3 vế còn lại, phần mềm đúng cả hai bản tài liệu; đối tác được đề nghị cập nhật Kết quả mong đợi:
- Loại hồ sơ "Người hỗ trợ" (mục 8): "Người hỗ trợ" là TÁC NHÂN đi đăng ký hộ, không phải loại của hồ sơ được tạo. Ô Loại chỉ có "Tư vấn viên"/"Chuyên gia" là đúng. Hồ sơ Người hỗ trợ được quản lý ở nhánh riêng Mạng lưới Tư vấn viên → Người hỗ trợ pháp lý, do Quản trị hệ thống hoặc Cán bộ Nghiệp vụ lập, căn cứ pháp lý khác hẳn (NĐ 55/2019 Điều 7 so với NĐ 77/2008 của tư vấn viên).
- Chuyển sang "trang theo dõi tiến độ" (mục 9): quy ước §H7 mức BẮT BUỘC buộc quay về trang Danh sách sau khi thêm mới thành công, và FR/SCR của màn này không có ghi chú ngoại lệ. Phần mềm không có màn nào tên "trang theo dõi tiến độ" cho luồng đăng ký tư vấn viên. Việc theo dõi tiến độ đã có sẵn ba đường: 7 tab trạng thái kèm số đếm ngay trên trang danh sách, badge trạng thái ở trang chi tiết, và thông báo trong phần mềm + thư điện tử ở từng mốc kết quả.
- Nhãn nút "Gửi đăng ký" (mục 12b): BA chốt GIỮ nhãn "Lưu". Ghi chú "BA xác nhận tên button sai" ở ô TKM phản hồi lần 1 KHÔNG có hiệu lực — chưa từng được nhập vào đặc tả, không có dấu thay đổi nào chạm tới nhãn nút của màn này. Quy ước §H4 mức BẮT BUỘC: nút lưu luôn mang nhãn "Lưu"; chuỗi "Gửi đăng ký" cho 0 kết quả ở cả .md lẫn .docx. Màn hình KHÔNG thiếu nút chức năng — bấm "Lưu" chính là hoàn tất nộp hồ sơ.

── CÁCH VERIFY sau Dev fix ──
Precondition: nht_ag_uat2 / Test@1234 (Người hỗ trợ pháp lý, Sở Tư pháp An Giang). Mạng lưới tư vấn viên → Tư vấn viên/Chuyên gia → Thêm mới.
1) Nhập đủ dữ liệu hợp lệ cho hồ sơ mới: Loại = "Tư vấn viên", chọn 2 lĩnh vực pháp luật, chọn tổ chức chủ quản. Bấm "Lưu".
2) Đọc TRỌN câu thông báo hiện ra ngay sau khi lưu. Toast tự tắt nhanh — hẹn giờ chụp ~2,5 giây sau khi bấm, hoặc đọc thẳng phản hồi của chính lượt tạo (mạnh hơn ảnh).
3) Mở tab "Mới đăng ký", tìm hồ sơ vừa tạo, đọc mã hồ sơ THẬT trên danh sách hoặc trang chi tiết.
4) Đối chiếu mã trong câu thông báo ở bước 2 với mã thật ở bước 3.
✅ PASS khi: (a) câu thông báo vừa giữ phần "Đăng ký thành công, chờ thẩm định", vừa kèm mã hồ sơ vừa sinh; (b) mã trong thông báo TRÙNG KHỚP mã thật của hồ sơ vừa tạo (dạng TVV-STP-AG-000N), không phải chỗ trống / undefined / null / mã của hồ sơ khác; (c) 7 vế đã đạt ở lượt đo 07/08 vẫn đạt: hồ sơ vào tab "Mới đăng ký", lưu đủ 2 lĩnh vực, đúng tổ chức chủ quản, đơn vị quản lý tự gán đúng theo người đăng ký, có thông báo tới Cán bộ Nghiệp vụ cùng đơn vị, có dòng nhật ký loại thao tác "Tạo mới".
❌ FAIL nếu: thông báo vẫn chỉ có "Đăng ký thành công, chờ thẩm định" mà không có mã; hoặc có chỗ dành cho mã nhưng rỗng/undefined/null; hoặc mã hiển thị khác mã thật của hồ sơ vừa tạo.
⚠️ Bẫy 1 — nút vẫn mang tên "Lưu" là ĐÚNG. KHÔNG log lại "thiếu nút Gửi đăng ký".
⚠️ Bẫy 2 — sau khi lưu hệ thống quay về trang Danh sách là ĐÚNG. KHÔNG log lại "không chuyển sang trang theo dõi tiến độ".
⚠️ Bẫy 3 — ô Loại chỉ có 2 lựa chọn Tư vấn viên/Chuyên gia là ĐÚNG. KHÔNG log lại "thiếu loại Người hỗ trợ".
⚠️ Bẫy 4 — câu chữ phần dẫn KHÔNG cần y hệt từng ký tự; đo yêu cầu là "thông báo thành công CÓ kèm mã hồ sơ vừa sinh".
Ảnh lỗi cũ: DKTGMLTVV_13.jpg
```

---

## Dòng 149 — `QLDMTCTV_12`

- Trạng thái dev fix lúc sao lưu: `Bug`
- Độ dài nội dung cũ: 3794 ký tự

```text
✅ Bug đúng (BA duyệt 08/08/2026 — phiếu 34 điểm tuần 5, mục 2). BA CHẤP THUẬN mốc 5.000 ký tự đúng bằng kỳ vọng của phiếu: bản bàn giao .docx dùng 5.000 làm khuôn mặc định cho ô văn bản nhiều dòng ở 15 chỗ, và 5.000 là mốc được dùng nhiều nhất trong đặc tả (21 lần, hơn 2.000 và 1.000). Phần mềm đang chặn ở 1.000 và CẮT ÂM THẦM phần vượt nên phải sửa. Mức Minor.
Dev FE+BE — 6 việc, áp cho CẢ HAI màn có ô này (Chi tiết Tổ chức tư vấn và Chi tiết Tư vấn viên): (1) nâng giới hạn ô Lý do thay đổi trạng thái lên 5.000 ký tự; (2) BỎ HẲN cơ chế cắt bớt — nội dung vượt mốc phải giữ nguyên thứ người dùng gõ/dán, không tự xóa phần thừa; (3) hiện bộ đếm ký tự ngay dưới ô, cập nhật khi gõ, chuyển trạng thái cảnh báo khi vượt mốc; (4) chặn nút Lưu ở CẢ HAI đầu — dưới 10 và trên 5.000 — kèm câu báo ngay tại ô; (5) câu báo phân biệt được hai đầu mốc; (6) máy chủ kiểm cùng hai mốc, khi từ chối thì trả đúng mã lỗi riêng đã khai của chức năng, không dùng mã hệ thống chung.
LƯU Ý PHẠM VI: phần đối tác báo "Màn hình không có nút chức năng" KHÔNG phải lỗi — xem bẫy 1.

── CÁCH VERIFY sau Dev fix ──
Precondition: cbnv_tw_03 / Test@1234 (Cán bộ Nghiệp vụ Trung ương — BẮT BUỘC cùng đơn vị với bản ghi, KHÔNG dùng tài khoản quản trị). Mạng lưới tư vấn viên → Tổ chức tư vấn → mở TC-TW-DEMO-001 "Công ty Luật TNHH Demo Kiểm Thử" (đơn vị Cục Bổ trợ tư pháp - Bộ Tư pháp, đang Đang hoạt động) → thẻ Thao tác → Cập nhật trạng thái.
1) Chọn Trạng thái mới = "Tạm dừng". Dán chuỗi ĐÚNG 5.000 ký tự vào ô Lý do → xác nhận lưu.
2) Mở lại bản ghi → tab "Lịch sử" → đếm độ dài chuỗi lý do vừa lưu.
3) Mở lại cửa sổ Cập nhật trạng thái, dán chuỗi 8.000 ký tự → ĐẾM số ký tự còn lại trong ô (KHÔNG bấm lưu).
4) Xóa bớt còn đúng 5.001 ký tự → đọc bộ đếm, rồi thử bấm nút xác nhận.
5) Xóa còn 9 ký tự → thử bấm nút xác nhận.
6) Gọi thẳng máy chủ lượt cập nhật trạng thái với lý do 5.001 ký tự → đọc mã lỗi trong phản hồi.
7) Lặp bước 1 và bước 4 trên màn Chi tiết Tư vấn viên (một hồ sơ TVV cùng đơn vị).
8) Hoàn nguyên bản ghi về "Đang hoạt động" sau khi đo xong.
✅ PASS khi: (a) chuỗi 5.000 ký tự lưu thành công, đọc lại ở tab Lịch sử ĐỦ 5.000 ký tự không thiếu ký tự nào; (b) dán 8.000 ký tự thì ô GIỮ NGUYÊN 8.000 — không tự cắt còn 5.000 hay 1.000; (c) bộ đếm hiện đúng dạng {n}/5000 và chuyển sang trạng thái cảnh báo khi n > 5000; (d) ở 5.001 ký tự và ở 9 ký tự đều KHÔNG lưu được VÀ có câu báo hiện ngay tại ô; (e) máy chủ từ chối chuỗi 5.001 ký tự bằng đúng mã lỗi riêng của chức năng, không phải mã hệ thống chung; (f) cả hai màn Tổ chức tư vấn và Tư vấn viên cùng hành vi.
❌ FAIL nếu: ô vẫn chặn cứng ở 1.000 ký tự; hoặc nội dung vượt mốc vẫn bị cắt mà không báo gì (đúng lỗi gốc); hoặc không có bộ đếm; hoặc lưu được chuỗi dài hơn 5.000; hoặc chỉ sửa 1 trong 2 màn.
⚠️ Bẫy 1 — KHÔNG log lại "Màn hình không có nút chức năng": ảnh bằng chứng gốc chụp bằng tài khoản Quản trị hệ thống cấp Trung ương trên bản ghi TC-STP-HN-0001 của Sở Tư pháp Hà Nội (lệch cùng lúc cả vai trò lẫn đơn vị). Nút "Cập nhật trạng thái" chỉ hiện với Cán bộ Nghiệp vụ CÙNG ĐƠN VỊ với bản ghi — thẻ Thao tác rỗng khi sai tiền đề là hệ quả phân quyền, không phải thiếu nút. Đo đúng tiền đề thì thẻ Thao tác có đủ 4 mục.
⚠️ Bẫy 2 — câu chữ báo lỗi KHÔNG cần khớp từng ký tự; đo yêu cầu là "có câu báo tại ô + chặn được nút Lưu", không bắt bẻ chính tả.
⚠️ Bẫy 3 — dropdown "Trạng thái mới" lọc theo trạng thái hiện tại là ĐÚNG (phần mềm đang làm nhiều hơn đặc tả yêu cầu và khớp phiếu). Đừng báo thiếu lựa chọn khi bản ghi Đang hoạt động chỉ hiện "Tạm dừng" + "Vô hiệu hóa".
⚠️ Bẫy 4 — cách chặn hiện tại là làm mờ nút xác nhận. Sau fix phải có THÊM câu báo tại ô; chỉ làm mờ nút mà không báo gì là chưa đạt việc (4).
Ảnh lỗi cũ: image/QLDMTCTV_12-C6-5001-ky-tu.png (thư mục output/UAT_doi-tac/reverify-week-5/F5-devfix-2026-08-07/)
```

---

## Dòng 163 — `QLDX_03`

- Trạng thái dev fix lúc sao lưu: `UAT done`
- Độ dài nội dung cũ: 0 ký tự

```text
(RỖNG)
```

---

## Dòng 288 — `QLNDTVVCG_38`

- Trạng thái dev fix lúc sao lưu: `BA confirm`
- Độ dài nội dung cũ: 5665 ký tự

```text
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

```

---

## Dòng 297 — `QLHSPLDN_15`

- Trạng thái dev fix lúc sao lưu: `UAT done`
- Độ dài nội dung cũ: 918 ký tự

```text
⚠️ CẦN BA XÁC NHẬN: Đặc tả im lặng về việc xuất Excel khi bộ lọc ra 0 bản ghi nên chưa có chuẩn để chấm.
WEB HIỆN TẠI: Lọc ra 0 bản ghi rồi bấm Xuất Excel thì hệ thống chặn xuất và báo đúng nguyên văn "Không có dữ liệu để xuất", không tạo tệp rỗng.
KỲ VỌNG ↔ SRS: Đối tác kỳ vọng đúng câu đó, còn FR-X.1-04 đặc tả khối Xuất Excel (srs-fr-12-tv-chuyen-sau.md:657-665) và bảng lỗi E1-E7 (:693-701) đều không có mã nào cho tình huống xuất khi bộ lọc rỗng, trong khi module Kho câu hỏi đã chốt mã INF-KHO-XL-01 với đúng câu này (srs-fr-13-tv-nhanh.md:155).
ĐÃ ĐO: Tài khoản cbnv_tw_02, doanh nghiệp DN-HNI-0001 thẻ Hồ sơ pháp lý; lọc từ khóa không khớp thì bảng còn 0 dòng, bấm Xuất Excel bắt được đúng 1 thông báo "Không có dữ liệu để xuất", đối chứng 0 lượt gọi máy chủ và không tệp nào được tạo.
CÂU HỎI BA: Hồ sơ pháp lý DN có áp cùng hành vi chặn xuất kèm thông báo như Kho câu hỏi không, và câu chữ chính thức là gì?
```

---

## Dòng 301 — `QLTLPLCVV_22`

- Trạng thái dev fix lúc sao lưu: `reject`
- Độ dài nội dung cũ: 3743 ký tự

```text
⚠️ Cần BA xác nhận — QA verify lại 07/08/2026, bản dựng V1.0.9, vai trò Cán bộ Nghiệp vụ Trung ương (cbnv_tw_05), trên bản ghi tư vấn chuyên sâu TVCS-20260806-0003. Phiếu gồm 2 vế: 1 vế chạy đúng như đối tác mong đợi, 1 vế phải để BA chốt vì đặc tả màn hình chưa nói tới.

WEB HIỆN TẠI — ĐÚNG KỲ VỌNG ĐỐI TÁC
- Nhóm "Tư liệu pháp lý liên kết" trong màn chi tiết Tư vấn chuyên sâu ĐÃ CÓ ô nhập từ khóa (chữ gợi ý trong ô: "Tìm theo tên hoặc mô tả tư liệu") kèm 3 bộ lọc Loại tư liệu / Lĩnh vực / Trạng thái và hai nút [Tìm kiếm] [Xóa bộ lọc]. Bảng tư liệu đủ 9 cột như đặc tả màn.
- Tìm bằng từ khóa tiếng Việt CÓ DẤU chạy đúng: nhóm đang có 2 tư liệu; gõ "Nghị định" rồi bấm [Tìm kiếm] thì bảng còn đúng 1 dòng "Nghị định 55/2019 hỗ trợ pháp lý cho doanh nghiệp nhỏ và vừa", tư liệu còn lại bị loại. Đối chứng bằng chính phản hồi máy chủ của lượt tìm đó: tổng = 1, đúng 1 mã bản ghi 0d258d7c-9498-48b3-982d-db85a13cdb96 — khớp số dòng hiện trên màn.

VÌ SAO VẪN PHẢI HỎI BA, KHÔNG CHẤM "ĐÃ HẾT LỖI"
Đặc tả CÓ yêu cầu chức năng tìm kiếm tư liệu (srs-fr-12-tv-chuyen-sau.md:942-951 — nhận từ khóa theo tên tư liệu và mô tả, lĩnh vực, loại tư liệu, trạng thái; AND logic; phân trang), và màn duy nhất chứa yêu cầu này chính là nhóm tư liệu trong màn chi tiết TVCS (:828, :1153, :1227-1229 — màn riêng SCR-X1-07 đã bị gộp vào). NHƯNG phần Thành phần màn hình của SCR-X1-02 chỉ khai cho nhóm này một bảng dữ liệu và nút [+ Thêm tư liệu] (:1171, :1198), và FR-X.1-06 không có tiêu chí chấp nhận nào cho tìm kiếm (:986-996). Tức phần dev đang làm đúng ý đối tác lại không có chỗ nào trong đặc tả màn hình quy định — QA không có căn cứ để chấm đạt hay không đạt.

CẦN BA CONFIRM: đối tác kỳ vọng nhóm "Tư liệu pháp lý liên kết" trong màn chi tiết Tư vấn chuyên sâu có ô nhập từ khóa và/hoặc bộ lọc để tìm tư liệu ngay tại đó; SRS quy định chức năng tìm kiếm tư liệu là yêu cầu bắt buộc của FR-X.1-06 (srs-fr-12-tv-chuyen-sau.md:942-951) và màn duy nhất chứa FR-X.1-06 chính là nhóm này (:828, :1153, :1227-1229), nhưng Thành phần màn hình của SCR-X1-02 chỉ khai bảng dữ liệu + nút [+ Thêm tư liệu], không khai ô tìm kiếm hay bộ lọc nào (:1171, :1198), và FR-X.1-06 không có tiêu chí chấp nhận cho tìm kiếm (:986-996); web/dev hiện tại đã có đủ ô tìm kiếm + 3 bộ lọc + nút [Tìm kiếm] [Xóa bộ lọc] và chạy đúng.
Đề nghị BA chốt: bổ sung thành phần tìm kiếm/lọc này vào SCR-X1-02 phần Thành phần màn hình (nêu rõ tìm theo trường nào, có mấy bộ lọc) và bổ sung tiêu chí chấp nhận tương ứng cho FR-X.1-06, để đặc tả khớp sản phẩm đang chạy. Mục đích là bổ sung vào đặc tả, KHÔNG phải chặn bàn giao.

ĐÃ ĐO
Đếm số ô nhập/chọn nằm trong đúng khung của nhóm tư liệu (4 ô: 1 ô từ khóa + 3 bộ lọc) và đếm số dòng bảng trước/sau khi tìm (2 → 1), rồi đối chiếu với phản hồi máy chủ của chính lượt tìm đó. Tiền đề: nhóm này ban đầu chỉ có 1 tư liệu không mang dấu tiếng Việt nên chưa phân biệt được có dấu / không dấu; QA đã thêm 1 tư liệu "Nghị định 55/2019 hỗ trợ pháp lý cho doanh nghiệp nhỏ và vừa" (loại Văn bản pháp luật, trạng thái Nháp) bằng chính nút [Thêm tư liệu] trên bản ghi TVCS-20260806-0003 của môi trường kiểm thử nội bộ; không đụng dữ liệu của đối tác.

BẰNG CHỨNG
- Nhóm tư liệu có ô tìm kiếm + 3 bộ lọc + bảng 9 cột: https://drive.google.com/file/d/1KGFgkn36R1FI1bBLr1cp84WUShXqe1tr/view?usp=drivesdk
- Gõ từ khóa có dấu "Nghị định" ra đúng 1 kết quả: https://drive.google.com/file/d/1Q2Y31zRZ55NZ_85fCf5s3f07jK0jEG70/view?usp=drivesdk

GIỚI HẠN HIỆU LỰC
Kết quả trên đo tại môi trường kiểm thử nội bộ bản dựng V1.0.9. Ảnh của đối tác chụp ở bản V1.0, tại đó nhóm tư liệu chưa có thanh lọc và bảng chỉ 7 cột — hai bản dựng khác nhau thật, nên kết luận này chỉ có hiệu lực cho bản V1.0.9 và cần đo lại sau khi bản này lên môi trường nghiệm thu.

```

---

## Dòng 302 — `QLTLPLCVV_23`

- Trạng thái dev fix lúc sao lưu: `reject`
- Độ dài nội dung cũ: 4508 ký tự

```text
⚠️ Cần BA xác nhận — QA verify lại 07/08/2026, bản dựng V1.0.9, vai trò Cán bộ Nghiệp vụ Trung ương (cbnv_tw_05), trên bản ghi tư vấn chuyên sâu TVCS-20260806-0003. Phiếu gồm 2 vế: vế tìm không dấu chạy đúng, vế còn lại phải để BA chốt vì đặc tả màn hình chưa nói tới.

WEB HIỆN TẠI — ĐÚNG KỲ VỌNG ĐỐI TÁC
- Tìm bằng từ khóa tiếng Việt KHÔNG DẤU chạy đúng: bấm [Xóa bộ lọc] cho bảng về 2 tư liệu, rồi gõ "Nghi dinh" (bỏ dấu hoàn toàn) và bấm [Tìm kiếm] thì bảng còn đúng 1 dòng là bản ghi tên viết CÓ DẤU "Nghị định 55/2019 hỗ trợ pháp lý cho doanh nghiệp nhỏ và vừa"; tư liệu còn lại bị loại. Đối chứng bằng phản hồi máy chủ của chính lượt tìm đó: tổng = 1, mã bản ghi 0d258d7c-9498-48b3-982d-db85a13cdb96 — TRÙNG KHÍT với lượt gõ có dấu ở phiếu QLTLPLCVV_22, tức bỏ dấu và có dấu cho ra cùng một kết quả.
- Nhóm "Tư liệu pháp lý liên kết" trong màn chi tiết Tư vấn chuyên sâu ĐÃ CÓ ô nhập từ khóa (chữ gợi ý trong ô: "Tìm theo tên hoặc mô tả tư liệu") kèm 3 bộ lọc Loại tư liệu / Lĩnh vực / Trạng thái và hai nút [Tìm kiếm] [Xóa bộ lọc]. Bảng tư liệu đủ 9 cột như đặc tả màn.

VÌ SAO VẪN PHẢI HỎI BA, KHÔNG CHẤM "ĐÃ HẾT LỖI"
Đặc tả CÓ yêu cầu chức năng tìm kiếm tư liệu (srs-fr-12-tv-chuyen-sau.md:942-951) và màn duy nhất chứa yêu cầu này chính là nhóm tư liệu trong màn chi tiết TVCS (:828, :1153, :1227-1229 — màn riêng SCR-X1-07 đã bị gộp vào). NHƯNG phần Thành phần màn hình của SCR-X1-02 chỉ khai cho nhóm này một bảng dữ liệu và nút [+ Thêm tư liệu] (:1171, :1198), và FR-X.1-06 không có tiêu chí chấp nhận nào cho tìm kiếm (:986-996). Phần dev đang làm đúng ý đối tác lại không có chỗ nào trong đặc tả màn hình quy định.

CẦN BA CONFIRM (1): đối tác kỳ vọng nhóm "Tư liệu pháp lý liên kết" trong màn chi tiết Tư vấn chuyên sâu có ô nhập từ khóa và/hoặc bộ lọc để tìm tư liệu ngay tại đó; SRS quy định chức năng tìm kiếm tư liệu là yêu cầu bắt buộc của FR-X.1-06 (srs-fr-12-tv-chuyen-sau.md:942-951) và màn duy nhất chứa FR-X.1-06 chính là nhóm này (:828, :1153, :1227-1229), nhưng Thành phần màn hình của SCR-X1-02 chỉ khai bảng dữ liệu + nút [+ Thêm tư liệu], không khai ô tìm kiếm hay bộ lọc nào (:1171, :1198), và FR-X.1-06 không có tiêu chí chấp nhận cho tìm kiếm (:986-996); web/dev hiện tại đã có đủ ô tìm kiếm + 3 bộ lọc + nút [Tìm kiếm] [Xóa bộ lọc] và chạy đúng.
Đề nghị BA chốt: bổ sung thành phần tìm kiếm/lọc này vào SCR-X1-02 phần Thành phần màn hình và bổ sung tiêu chí chấp nhận tương ứng cho FR-X.1-06. Mục đích là bổ sung vào đặc tả, KHÔNG phải chặn bàn giao.

CẦN BA CONFIRM (2 — riêng phiếu này, về yêu cầu không dấu): đối tác kỳ vọng tìm bằng từ khóa tiếng Việt không dấu vẫn ra bản ghi có tên viết có dấu; SRS quy định hai chỗ lệch nhau — bước xử lý của chính FR-X.1-06 ghi "Full-text search trên ten_tu_lieu + mo_ta (hỗ trợ tiếng Việt unaccent)" (srs-fr-12-tv-chuyen-sau.md:948), trong khi quy tắc BR-DATA-08 ở bản gốc file chính không nhắc chữ unaccent và chỉ áp cho FR-II-02 / FR-X.1-02 / FR-X.2-04, phần Ngoại lệ ghi "Các entity khác: search by tìm kiếm theo từ khóa" (srs-v3.5.md:5572); hai bảng tham chiếu trong FR-12 cũng chỉ gán BR-DATA-08 cho FR-X.1-02 (:1579, :1635); web/dev hiện tại đã hỗ trợ không dấu, cho ra đúng cùng một bản ghi với lượt gõ có dấu.
Đề nghị BA chốt: tìm kiếm tư liệu pháp lý (FR-X.1-06) có bắt buộc hỗ trợ tiếng Việt không dấu hay không, và đồng bộ lại phạm vi BR-DATA-08 giữa file chính với bản trích ở FR-12. Chuẩn chấm vòng này vẫn lấy :948.

ĐÃ ĐO
Đây là phép đo RIÊNG cho vế không dấu, không suy từ phiếu có dấu — hai phiếu của đối tác dùng chung một ảnh bằng chứng nên ảnh không phân biệt được hai vế. Chọn cụm hai từ "Nghi dinh" chứ không dùng một từ, vì bỏ dấu của "nghị" là "nghi" trùng tiền tố của "nghiệp" nên tìm một từ sẽ mất khả năng phân biệt. Đếm số dòng bảng trước/sau khi tìm (2 → 1) rồi đối chiếu tập mã bản ghi của hai lượt tìm có dấu và không dấu. Tiền đề dùng lại nguyên của phiếu QLTLPLCVV_22, không thêm dữ liệu mới.

BẰNG CHỨNG
- Gõ từ khóa KHÔNG DẤU "Nghi dinh" vẫn ra bản ghi tên có dấu: https://drive.google.com/file/d/1PPH3XpTzzzcdmkT5ZYICy0PSgIxuq18i/view?usp=drivesdk
- Nhóm tư liệu có ô tìm kiếm + 3 bộ lọc + bảng 9 cột: https://drive.google.com/file/d/1KGFgkn36R1FI1bBLr1cp84WUShXqe1tr/view?usp=drivesdk

GIỚI HẠN HIỆU LỰC
Kết quả trên đo tại môi trường kiểm thử nội bộ bản dựng V1.0.9. Ảnh của đối tác chụp ở bản V1.0, tại đó nhóm tư liệu chưa có thanh lọc và bảng chỉ 7 cột — hai bản dựng khác nhau thật, nên kết luận này chỉ có hiệu lực cho bản V1.0.9 và cần đo lại sau khi bản này lên môi trường nghiệm thu.

```

---

## Dòng 321 — `QLHDTVVCG_15`

- Trạng thái dev fix lúc sao lưu: `BA confirm`
- Độ dài nội dung cũ: 10066 ký tự

```text
📌 KẾT QUẢ CHUNG: CẦN BA XÁC NHẬN — bốn yêu cầu chấm được đều ĐẠT, còn hai điểm đặc tả chưa đủ căn cứ nên chưa được chấm đạt cũng không được chấm lỗi.

Phiếu này bên nghiệm thu chưa chạy lượt nào (ô Kết quả thực tế để trống, không có ảnh), nên đây là lượt chạy đầu tiên; chuẩn chấm lấy từ ô Kết quả mong đợi của phiếu đối chiếu với đặc tả.

Đo trên môi trường nội bộ https://18.143.165.120.nip.io, bó mã giao diện index-BbPPdate.js (bản lên lúc 13:47 ngày 07/08/2026), đo lúc 14:39-14:47 ngày 07/08/2026. Tài khoản Cán bộ Nghiệp vụ Trung ương cbnv_tw_03, đơn vị "Cục Bổ trợ tư pháp - Bộ Tư pháp" - đúng vai trò được phép lưu hợp đồng; không dùng tài khoản quản trị.

ĐƯỜNG VÀO THỰC TẾ (nói rõ vì bước 1 của phiếu đã hết hiệu lực)

Bước 1 của phiếu ghi "Chọn menu Hợp đồng Tư vấn". Thanh bên KHÔNG có mục đó - đúng theo quyết định nghiệp vụ ngày 11/05/2026 (bỏ menu riêng), như phản hồi của bộ phận phát triển. Đây là đường đi, không phải điểm chấm, nên không tính là lỗi. Đường thực tế: Vụ việc HTPL > tìm vụ việc VV-BTP-TW-20260804-002 > mở Chi tiết vụ việc > mở mục "HĐ tư vấn liên kết" > bấm "+ Tạo hợp đồng" > nhập thông tin > bấm nút gửi biểu mẫu.

Hợp đồng đã tạo thật bằng giao diện: HDTV-20260807-0006 - "Hợp đồng tư vấn xác lập quyền sở hữu trí tuệ và nhãn hiệu cho doanh nghiệp nhỏ và vừa", bên B là Chuyên gia UAT QLNDTVVCG 38, giá trị 250.000.000 đồng, thời gian 07/08/2026 đến 25/08/2026.

ĐÃ ĐẠT - 4 phần

1) Sinh mã hợp đồng đúng khuôn HDTV-{ngày}-{số thứ tự}. Sau khi lưu, mã HDTV-20260807-0006 hiện ở cả ba chỗ: dưới tiêu đề hợp đồng, ô "Mã hợp đồng", và cột "Mã hợp đồng" trên bảng danh sách. Kiểm lại bằng đường thứ hai: đọc lại chính bản ghi đó từ máy chủ, mã lưu trong dữ liệu cũng là HDTV-20260807-0006 - trùng khít chuỗi hiển thị. Đã kiểm riêng phần ngày: 20260807 đúng là NGÀY TẠO bản ghi, không phải ngày kết thúc hợp đồng (25/08/2026). Yêu cầu của đặc tả tại srs-fr-14-hop-dong-tv.md:81, :119 và :514.

2) Lưu bản ghi kèm ĐẦY ĐỦ ba nhóm dữ liệu con đã nhập (nhóm thứ tư là tệp đính kèm, xem phần Cần nghiệp vụ chốt điểm 2). Trước khi lưu đã nhập 1 mốc tiến độ, 1 giai đoạn thanh toán và 3 vụ việc liên kết. Sau khi lưu, mở LẠI màn chi tiết hợp đồng (tải mới từ máy chủ, không đếm trên biểu mẫu cũ) thì đếm được đúng 1 mốc tiến độ "Ban giao ho so tra cuu nhan hieu" hạn 18/08/2026, đúng 1 giai đoạn "Dot 1 - tam ung khi ky hop dong" 100.000.000 đồng ngày 15/08/2026, và đúng 3 vụ việc VV-BTP-TW-20260804-002, -003, -004. Kiểm lại bằng đường thứ hai: đọc lại bản ghi từ máy chủ, số phần tử từng nhóm là 1 - 1 - 3, khớp số đã nhập. Nhờ vậy loại được ca hay gặp "giao diện nhận dữ liệu con nhưng máy chủ chỉ lưu phần thông tin chung". Màn chi tiết còn có mục "Nhật ký hoạt động" ghi lại thao tác tạo mới - đáp ứng yêu cầu lưu vết tại :162. Yêu cầu của đặc tả tại :122, :123, :159 đến :162.

3) Gán trạng thái "Đang thực hiện". Hợp đồng vừa lưu hiện nhãn tiếng Việt "Đang thực hiện" ở thẻ dưới tiêu đề, ô Trạng thái và cột Trạng thái trên bảng danh sách; không chỗ nào lộ mã kỹ thuật ra màn hình. Kiểm lại bằng đường thứ hai: giá trị trạng thái lưu trong dữ liệu đúng là giá trị mặc định mà đặc tả quy định, nên loại được khả năng "giao diện hiển thị mặc định cứng còn dữ liệu lưu khác". Yêu cầu của đặc tả tại :396 và :464.

4) Hiển thị đúng câu thông báo "Đã lưu hợp đồng". Đã cài bộ bắt thông báo trước khi bấm lưu (thông báo loại này tự tắt sau vài giây, đọc muộn sẽ kết luận sai là "im lặng"), không lọc trùng. Kết quả: đúng MỘT thông báo tại một mốc giờ duy nhất 14:43:54, nội dung "Đã lưu hợp đồng" - trùng từng chữ câu chuẩn của đặc tả. Đếm kèm số yêu cầu gửi đi: đúng MỘT yêu cầu lưu, phản hồi thành công, đóng dấu thời gian cùng giây với thông báo. Vậy không có thông báo kép, không có lưu hai lần. Yêu cầu của đặc tả tại :173 và :187. Ghi nhận phản hồi của bộ phận phát triển là chính xác: câu này đã dùng chung cho cả tạo mới lẫn cập nhật.

CẦN NGHIỆP VỤ CHỐT - 2 điểm (chưa được chấm đạt hay lỗi)

Điểm 1: SAU KHI LƯU THÌ MÀN HÌNH ĐI ĐÂU.
- CẦN BA CONFIRM: đối tác kỳ vọng sau khi lưu hợp đồng mới thì hệ thống quay về màn danh sách hợp đồng; SRS quy định nhóm chức năng này KHÔNG có màn danh sách độc lập, sau khi lưu hệ thống đóng biểu mẫu và trả người dùng về ngữ cảnh đã mở nó, tức Chi tiết Vụ việc hoặc Chi tiết Tư vấn viên (srs-fr-14-hop-dong-tv.md:175, ghi chú "BA chốt 06/08/2026", và :187); web hiện tại: đóng biểu mẫu, ở lại màn Chi tiết vụ việc VV-BTP-TW-20260804-002 và tự nạp lại bảng "HĐ tư vấn liên kết" ngay trong màn đó, bảng đã hiện hợp đồng vừa tạo.
- Nói cách khác, phần mềm đang làm THEO PHÍA ĐẶC TẢ, khác với câu chữ trong ô Kết quả mong đợi của phiếu. Vì hai nguồn nói ngược nhau nên không được chấm đạt cũng không được chấm lỗi.
- CÂU HỎI CHO NGHIỆP VỤ: đề nghị chốt - sau khi lưu hợp đồng mới, hệ thống phải quay về một màn danh sách hợp đồng riêng (thì phải dựng thêm màn đó), hay giữ như hiện nay là trả về màn đã mở biểu mẫu? Nếu chốt giữ như hiện nay thì đề nghị sửa lại câu chữ của phiếu kiểm thử cho khớp.

Điểm 2: PHẦN MỀM TÁCH VIỆC ĐÍNH KÈM TỆP THÀNH HAI BƯỚC (phần tệp đính kèm của yêu cầu số 2).
- HÀNH VI ĐO ĐƯỢC: ở chế độ Thêm mới, mục "Tài liệu đính kèm" KHÔNG có ô chọn tệp, phần mềm hiện dòng chữ "Vui lòng lưu hợp đồng trước khi đính kèm tài liệu". Sau khi lưu, mở lại biểu mẫu ở chế độ SỬA thì ô chọn tệp XUẤT HIỆN, có vùng "Kéo thả hoặc nhấp để chọn tệp đính kèm" kèm ràng buộc ghi rõ trên màn: tối đa 10 tệp, định dạng pdf/doc/docx/xls/xlsx/jpg/png, 20MB mỗi tệp. Nghĩa là NĂNG LỰC ĐÍNH KÈM CÓ, nhưng bị tách làm hai bước - không phải "không đính kèm được".
- Nói rõ để tránh hiểu nhầm: đội kiểm thử ĐÃ chuẩn bị sẵn bộ tệp thật đúng định dạng; việc không nhập được là do phần mềm không mở chỗ nhập ở bước tạo, không phải do thiếu dữ liệu thử.
- Đối chứng độc lập: phía máy chủ, việc nạp tệp cũng buộc phải gắn với một hợp đồng ĐÃ TỒN TẠI. Vậy đây là thiết kế nhất quán của phần mềm, không phải trục trặc ngẫu nhiên.
- Lượt kiểm chế độ Sửa chỉ MỞ RA NHÌN rồi bấm Hủy, KHÔNG tải tệp lên, KHÔNG lưu - vì thao tác sửa hợp đồng thuộc một phiếu kiểm thử khác, làm bây giờ sẽ ảnh hưởng phép đo của phiếu đó. Đã xác minh bản ghi không đổi.
- Đặc tả đứng ở đâu (đã tự mở tệp đọc lại bốn chỗ): :92 bảng dữ liệu đầu vào CÓ khai trường tệp đính kèm, nhiều tệp, không bắt buộc, do người dùng tải lên; :290 bảng thành phần màn hình CÓ khai "File đính kèm" trên trang thêm/sửa. NHƯNG bước xử lý khi lưu (:122, :123) chỉ nhắc mốc tiến độ, thanh toán giai đoạn và liên kết vụ việc; mục kết quả sau xử lý (:159 đến :162) cũng chỉ liệt kê hợp đồng, mốc tiến độ, thanh toán, liên kết vụ việc và lưu vết - KHÔNG chỗ nào nhắc tệp đính kèm. Tức đặc tả CÓ trường tệp trên biểu mẫu nhưng KHÔNG phát biểu ở đâu rằng tệp phải được lưu CÙNG LÚC tạo bản ghi, trong khi ô Kết quả mong đợi của phiếu lại nói rõ "cùng toàn bộ ... tệp đính kèm đã nhập".
- Vì đặc tả im lặng nên phần này KHÔNG được chấm đạt, cũng KHÔNG được kết luận là lỗi của bộ phận phát triển.
- CÂU HỎI CHO NGHIỆP VỤ: đối tác kỳ vọng tạo hợp đồng và nạp tệp đính kèm trong cùng một lượt lưu. Đặc tả có khai trường tệp trên biểu mẫu thêm/sửa (:92, :290) nhưng bước xử lý khi lưu (:122, :123) và mục kết quả sau xử lý (:159 đến :162) không nhắc tệp đính kèm, nên không có căn cứ đòi lưu cùng lúc. Web hiện tại yêu cầu lưu hợp đồng trước rồi mới đính kèm ở chế độ Sửa. Đề nghị nghiệp vụ chốt: nạp tệp lúc tạo có bắt buộc không, hay tách hai bước là chấp nhận được - và bổ sung điều này vào đặc tả.

GHI NHẬN THÊM CHO DEV (không ảnh hưởng kết quả phiếu này)

- Nhãn nút gửi biểu mẫu đổi theo chế độ: chế độ Thêm mới là "Thêm mới", chế độ Sửa là "Lưu". Phiếu chấm theo hành vi nên không tính là lỗi; đề nghị nghiệp vụ thống nhất nhãn.
- Nhật ký hoạt động của hợp đồng hiện HAI dòng "Tạo mới" cùng mốc 14:43 cho một lần lưu, trong đó một dòng bỏ trống cột Đường dẫn và cột Mã phản hồi, dù chỉ có đúng một yêu cầu lưu được gửi đi. Đặc tả chỉ ghi chung chung là "có lưu vết", không nói một giao dịch sinh mấy dòng nhật ký, nên chỉ ghi nhận, chưa kết luận.
- Phần mềm CÓ màn chi tiết hợp đồng riêng, và đường dẫn phụ đề của màn đó có liên kết "Hợp đồng tư vấn"; bấm thử liên kết này thì hệ thống ném người dùng về màn Tổng quan chứ không mở danh sách hợp đồng nào. Trong khi đặc tả :266 và :268 nói nhóm chức năng này không còn màn/menu riêng. Ghi nhận làm dữ kiện cho câu hỏi nghiệp vụ về phạm vi màn hình, không tính là lỗi của phiếu này.

DỮ LIỆU ĐÃ THAY ĐỔI: lượt đo này TẠO MỚI 1 hợp đồng tư vấn trên môi trường nội bộ - mã HDTV-20260807-0006 lúc 14:43 ngày 07/08/2026, kèm 1 mốc tiến độ, 1 giai đoạn thanh toán và 3 liên kết tới vụ việc VV-BTP-TW-20260804-002, -003, -004 (chỉ tạo liên kết, không sửa bản thân các vụ việc). Ghi chú của hợp đồng mang dấu QA-F8-321-20260807 để phân biệt với dữ liệu của đối tác. Không sửa, không xóa bản ghi nào khác. Sau khi lượt đo này kết thúc, đội có bổ sung 1 tệp đính kèm vào chính hợp đồng đó để phục vụ các phiếu sau; việc bổ sung diễn ra SAU khi đã đo và ghi xong phần trên, nên không ảnh hưởng kết quả của phiếu này.

Ảnh bằng chứng:
- Dữ liệu đã nhập trước khi bấm lưu (nội dung, ghi chú, mốc tiến độ, giai đoạn thanh toán): https://drive.google.com/file/d/1-Ut6CKSa2OoHCX1L1he5edygARQTPfOi/view?usp=drivesdk
- Sau khi lưu: biểu mẫu đóng, màn dừng ở Chi tiết vụ việc, bảng hợp đồng liên kết đã có bản ghi mới: https://drive.google.com/file/d/1ce65-8s3aoiS__GLD7HyVOiz8WqBHHmk/view?usp=drivesdk
- Mở lại chi tiết hợp đồng đếm từng nhóm: 3 vụ việc, 1 mốc tiến độ, 1 giai đoạn thanh toán, chưa có tài liệu đính kèm: https://drive.google.com/file/d/1tbbdgTvP1J4ix0V-HTnJY80x1fB8xIH0/view?usp=drivesdk
- Chế độ Thêm mới không có ô chọn tệp, chỉ chế độ Sửa mới có: https://drive.google.com/file/d/1VMsiUnGvgaPLqAvEXnm_cYQBR0JB7OuH/view?usp=drivesdk

Do bên nghiệm thu chưa từng chạy phiếu này nên đội không có ảnh "lỗi cũ" để so sánh; vì vậy chỉ kết luận được hiện trạng hiện nay, không kết luận về tác dụng của bản sửa.

Kết quả trên chỉ có hiệu lực cho môi trường nội bộ https://18.143.165.120.nip.io ở bản dựng đã ghi tại thời điểm đo; đợt kiểm của bên nghiệm thu thực hiện trên môi trường htpldn-uat.ospgroup.vn.

```
