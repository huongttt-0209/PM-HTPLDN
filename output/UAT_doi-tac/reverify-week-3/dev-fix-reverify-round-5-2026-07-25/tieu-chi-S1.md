# S1 — Quản trị hệ thống — Danh mục · Phân quyền · Cấu hình · Đăng ký công khai

- **Tài khoản của session:** admin / Secret@123 (QTHT) · row 186 KHÔNG cần login
- **Số case:** 7 — rows [135, 140, 148, 153, 173, 174, 186]
- **Mức seed:** Nhẹ — chủ yếu kiểm giao diện. Case 135/148 cần tạo bản ghi danh mục MỚI để test trên dữ liệu mới.

> **Nguồn tiêu chí:** khối `── CÁCH VERIFY ──` gốc do BA/dev viết, khôi phục từ giá trị `old=` trong `output/UAT_doi-tac/tools/sheet_verify_write.log`. Ô R trên sheet đã bị chế độ `--reopen` ghi đè sáng 25/07 nên KHÔNG còn tiêu chí. **Chấm PASS/FAIL đúng theo khối này, không tự nghĩ tiêu chí.**

> Bản snapshot nguyên văn P/Q/R trước round 5: `snapshot-P-Q-R-truoc-round5.md` cùng thư mục.


---

# Row 135 — QLDMCTHT_13

## TIÊU CHÍ GỐC — bắt buộc chấm theo

✅ Bug đúng (BA duyệt 24/07/2026) — 2 ý trên form Sửa danh mục tab "Chương trình hỗ trợ"; cùng gốc với QLDMCTHT_06, sửa 1 lần ở component form danh mục dùng chung.
Dev FE (1): ẩn trường "Danh mục cha" ở loại danh mục phẳng — mẫu dùng chung TPL-DM-CRUD chỉ có 5 trường (srs-fr-10-quan-tri.md:77-83), ghi chú BA :85.
Dev FE (2): giá trị ngày đang lưu khi nạp lên form Sửa phải hiển thị theo quy ước ngày/tháng/năm (DG-01 srs-v3.5.md:950; UI-06 srs-v3.5.md:575), không phải năm-tháng-ngày. Mức Minor.

── CÁCH VERIFY sau Dev fix ──
Precondition: admin (QTHT), tab "Chương trình hỗ trợ" (/quan-tri/danh-muc/CHUONG_TRINH_HT), đã có record cũ (vd CT_NGUOI_NGHEO — Thời gian bắt đầu 01/01/2020).
1) Bấm "Sửa" trên record CT_NGUOI_NGHEO → đọc nhãn các trường của form Chỉnh sửa.
2) Đọc giá trị có sẵn của ô "Thời gian bắt đầu" (không sửa gì).
3) Đổi "Thời gian kết thúc" thành 31/12/2026 → Lưu → mở lại form Sửa của chính record đó.
✅ PASS khi: (a) form Sửa KHÔNG còn trường "Danh mục cha"; (b) ngày cũ nạp lên hiện 01/01/2020; (c) sau khi lưu và mở lại, "Thời gian kết thúc" hiện 31/12/2026 — đúng ngày, đúng thứ tự ngày-tháng-năm.
❌ FAIL nếu: còn trường "Danh mục cha"; hoặc ô ngày hiện 2020-01-01 / 2026-12-31; hoặc lưu xong ngày bị lệch do đọc nhầm ngày thành tháng.
⚠️ Chỉ kiểm 2 ô ngày trong form Sửa; các cột ngày tạo/ngày cập nhật ở màn khác không thuộc phạm vi case này.

## Triệu chứng QA ghi nhận lượt trước (sáng 25/07) — CHỈ tham khảo, không phải tiêu chí

- Mở "Sửa" một chương trình hỗ trợ, chọn lại Thời gian kết thúc rồi bấm Đồng ý thì hệ thống báo "Dữ liệu không hợp lệ" và không lưu được; form vẫn mở, tải lại trang thì giá trị vừa chọn mất hẳn.
- Kèm theo là dòng nhắc ngày phải ở dạng năm-tháng-ngày, trong khi ô trên màn đang hiển thị và nhận ngày theo dạng ngày/tháng/năm.
- Ô "Thời gian bắt đầu" vẫn đang có sẵn giá trị 01/01/2020 trên form, không hề bỏ trống, nhưng hệ thống vẫn báo thiếu ngày bắt đầu.
- Lỗi lặp lại cả khi gõ tay lẫn khi chọn ngày từ lịch. Thêm mới một chương trình hỗ trợ cũng bị chặn y hệt, nên hiện không tạo mới lẫn không sửa được bản ghi nào ở mục Chương trình hỗ trợ.
- Hai điểm còn lại của phiếu đã đạt: form Sửa không còn ô "Danh mục cha", và ngày đang lưu nạp lên form đúng 01/01/2020 theo dạng ngày/tháng/năm.


---

# Row 140 — QLDMCQDVQL_12

## TIÊU CHÍ GỐC — bắt buộc chấm theo

✅ Bug đúng (BA duyệt 24/07/2026). Dev FE: bổ sung kiểm tra "còn thay đổi chưa lưu" + hộp thoại xác nhận cho panel chỉnh sửa bên phải của màn cây "Cơ quan đơn vị" — hiện panel bị đặt lại thẳng về trạng thái chưa chọn, mất dữ liệu, không hỏi. Căn cứ UI-08 (srs-v3.5.md:577) áp cho mọi form nhập liệu toàn hệ thống + §Quy tắc tương tác màn Quản lý danh mục (srs-fr-10-quan-tri.md:1622); panel chi tiết của màn cây (FR-VIII-05 — :294-302, SCR-VIII-01 :1601-1603) vẫn là form nhập liệu nên thuộc phạm vi UI-08. Mức Major (mất dữ liệu đang nhập).

── CÁCH VERIFY sau Dev fix ──
Precondition: admin (QTHT), tab "Cơ quan đơn vị" (/quan-tri/danh-muc/CO_QUAN_DON_VI) — cây đơn vị bên trái, panel chi tiết bên phải.
1) Chọn 1 đơn vị trên cây → panel phải hiện thông tin → sửa ô Địa chỉ thành "So 1 Test 140" (chưa Lưu).
2) Bấm đóng panel (X hoặc Hủy) → quan sát hộp thoại xác nhận.
3) Chọn ở lại → kiểm tra panel còn nguyên và Địa chỉ vừa gõ chưa mất.
4) Bấm đóng lại → chọn bỏ thay đổi → chọn lại chính đơn vị đó trên cây và đọc ô Địa chỉ.
5) Lặp bước 1, nhưng thay vì đóng panel thì bấm sang MỘT ĐƠN VỊ KHÁC trên cây.
✅ PASS khi: bước 2 và bước 5 đều hỏi xác nhận trước khi bỏ nội dung đang sửa; bước 3 giữ nguyên nội dung; bước 4 Địa chỉ trở về giá trị gốc (không bị lưu nhầm).
❌ FAIL nếu: panel đặt lại thẳng về "Chọn một đơn vị từ cây bên trái" mà không hỏi; hoặc bấm sang đơn vị khác làm mất dữ liệu đang sửa mà không cảnh báo; hoặc đã chọn bỏ thay đổi nhưng hệ thống vẫn lưu.
⚠️ Panel ở trạng thái chỉ xem (chưa sửa gì) thì đóng thẳng, KHÔNG hỏi — đó là đúng, không tính FAIL.

## Triệu chứng QA ghi nhận lượt trước (sáng 25/07) — CHỈ tham khảo, không phải tiêu chí

- Ở mục Cơ quan đơn vị, chọn một đơn vị trên cây rồi bấm Sửa, nhập nội dung mới vào ô Địa chỉ (hoặc sửa ô Tên đơn vị) nhưng chưa bấm Lưu.
- Bấm Hủy: hệ thống thoát khỏi chế độ chỉnh sửa ngay lập tức, không hiện hộp thoại hỏi xác nhận, nội dung vừa nhập mất hẳn.
- Đang sửa dở mà bấm chọn một đơn vị khác trên cây: khung thông tin chuyển thẳng sang đơn vị mới, cũng không có cảnh báo nào, nội dung đang nhập bị bỏ.
- Chọn lại đúng đơn vị vừa sửa thì các ô trở về giá trị cũ, xác nhận là dữ liệu đang nhập đã mất mà người dùng không được hỏi trước.
- Khung chỉnh sửa hiện chỉ có hai nút Hủy và Lưu; đã thử trên hai đơn vị khác nhau, kết quả giống nhau.


---

# Row 148 — QLDMHSDNHT_13

## TIÊU CHÍ GỐC — bắt buộc chấm theo

✅ Bug đúng (BA 24/07/2026, Cụm A). Dev FE: không hiển thị trường "Danh mục cha" trên form Sửa danh mục "Hồ sơ đề nghị hỗ trợ". FR-VIII-08 (UC106) dùng mẫu TPL-DM-CRUD, §trường riêng chỉ gồm thành phần hồ sơ bắt buộc/tùy chọn (srs-fr-10-quan-tri.md:412-427); mẫu chung 5 trường (:77-83) không khai trường cha; ghi chú BA :85 chốt trường cha chỉ áp danh mục cấu trúc cây. Backend không lưu quan hệ cha cho danh mục phẳng; dọn bản ghi phẳng đã lỡ gán cha. Cosmetic.

── CÁCH VERIFY sau Dev fix ──
Precondition: admin (QTHT), Quản trị hệ thống → Danh mục dùng chung → tab "Hồ sơ đề nghị hỗ trợ" (/quan-tri/danh-muc/HO_SO_DE_NGHI_HT); chọn 1 bản ghi hồ sơ có sẵn.
1) Bấm [Sửa] bản ghi hồ sơ đề nghị hỗ trợ đang có → đọc toàn bộ nhãn trường form Chỉnh sửa.
2) Đối chiếu với form [+ Thêm mới] cùng tab.
✅ PASS khi: (a) form Sửa KHÔNG còn trường "Danh mục cha"; (b) vẫn giữ đủ trường riêng "thành phần hồ sơ" của tab (không bị ẩn nhầm khi gỡ trường cha); (c) giá trị bản ghi nạp đúng khi mở Sửa.
❌ FAIL nếu: form Sửa còn ô "Danh mục cha" (kể cả để trống/làm mờ), HOẶC gỡ trường cha làm hỏng chức năng lưu / mất trường thành phần hồ sơ.
⚠️ Tab cấu trúc cây (Cơ quan đơn vị) giữ trường cha là đúng SRS :85.

## Triệu chứng QA ghi nhận lượt trước (sáng 25/07) — CHỈ tham khảo, không phải tiêu chí

- Mở [Sửa] một danh mục "Hồ sơ đề nghị hỗ trợ" đang có (đã thử "Đơn đề nghị hỗ trợ" và "Hồ sơ chứng minh điều kiện"): trường "Danh mục cha" đã được gỡ, nhưng khối "Thành phần bắt buộc → Thành phần 1" hiện ra hoàn toàn trống.
- Hai ô "Mã thành phần" và "Tên thành phần" có dấu * bắt buộc nhưng không nạp dữ liệu của bản ghi đang sửa; nút xóa khối "Thành phần 1" bị làm mờ, không bấm được.
- Bấm [Đồng ý] để lưu thì bị chặn, hiện lỗi "Mã thành phần là bắt buộc" và "Tên thành phần là bắt buộc" → không lưu được thay đổi trên bản ghi cũ nếu không tự nhập thêm một thành phần mới.
- Ngoài ra, cột "Loại" (Bắt buộc / Tùy chọn) hiển thị ở danh sách không có ô tương ứng trên biểu mẫu để xem hoặc chỉnh sửa.


---

# Row 153 — QLCHTHXLHS_03

## TIÊU CHÍ GỐC — bắt buộc chấm theo

✅ Bug đúng một phần (BA duyệt 24/07/2026) — 3 điểm Dev sửa; phần cấu trúc còn lại là thiết kế lại đã được chấp nhận và cập nhật vào đặc tả.
Dev FE (e): bổ sung "Số ngày bổ sung tối đa" vào bảng và cửa sổ Sửa cấu hình thời hạn — bắt buộc với mọi loại yêu cầu khác Hỏi đáp, mặc định 5 ngày làm việc, để trống với Hỏi đáp (srs-fr-10-quan-tri.md:477, :1768, :1770; tiêu chí nghiệm thu :518; báo lỗi :515).
Dev FE (f): bỏ hiển thị "Hệ số quá hạn" khỏi cả bảng lẫn cửa sổ Sửa — đây là tham số ngầm bên trong, chốt không đưa lên giao diện (:1772, :2194).
Dev FE (g, ưu tiên thấp): bổ sung lại 2 khối thông tin của thẻ SLA — khung giải thích 4 mức cảnh báo (:1762) và cảnh báo "hồ sơ mới áp cấu hình mới, hồ sơ đang xử lý giữ hạn cũ" (:1771).
Giữ nguyên (đặc tả đã cập nhật theo web): tách 2 cột mã + tên loại, 6 loại yêu cầu, gộp vùng cảnh báo, bảng chỉ đọc + nút Sửa (:1763-1769, :522-533).

── CÁCH VERIFY sau Dev fix ──
Precondition: admin (QTHT), /quan-tri/cau-hinh → thẻ "Thời hạn xử lý (SLA)".
1) Đọc tên toàn bộ cột của bảng.
2) Bấm "Sửa" ở dòng VU_VIEC → đọc danh sách trường trong cửa sổ.
3) Xóa trắng "Số ngày bổ sung tối đa" ở dòng VU_VIEC rồi bấm lưu.
4) Bấm "Sửa" ở dòng HOI_DAP → xem ô "Số ngày bổ sung tối đa".
5) Quan sát phần đầu và phần cuối của thẻ SLA (ngoài bảng).
✅ PASS khi: (a) có "Số ngày bổ sung tối đa" ở cả bảng và cửa sổ Sửa, dòng VU_VIEC hiện 5; (b) KHÔNG còn "Hệ số quá hạn" ở bảng lẫn cửa sổ Sửa; (c) bước 3 bị từ chối kèm thông báo yêu cầu nhập số nguyên dương và giá trị cũ giữ nguyên; (d) dòng HOI_DAP để trống hoặc không cho nhập ô này; (e) thấy khung giải thích 4 mức cảnh báo và cảnh báo về ảnh hưởng khi lưu.
❌ FAIL nếu: thiếu "Số ngày bổ sung tối đa"; còn hiển thị "Hệ số quá hạn"; bước 3 lưu được giá trị trống; hoặc thiếu 1 trong 2 khối thông tin.
⚠️ Bảng ở chế độ chỉ đọc và sửa qua cửa sổ là ĐÚNG đặc tả mới — không báo lỗi vì không sửa được trực tiếp trên dòng. 6 dòng loại yêu cầu (có thêm Hỏi đáp phức tạp và Hồ sơ chi trả) cũng đúng.

## Triệu chứng QA ghi nhận lượt trước (sáng 25/07) — CHỈ tham khảo, không phải tiêu chí

- Bảng cấu hình thời hạn xử lý (SLA) hiện chỉ có các cột: Loại yêu cầu, Tên loại, Thời hạn (ngày LV), Vùng cảnh báo, Email, Thông báo app, Hành động — vẫn chưa có cột Số ngày bổ sung tối đa.
- Mở cửa sổ Sửa của dòng Vụ việc hỗ trợ pháp lý thì đã có ô Số ngày bổ sung tối đa với giá trị 5, tức là dữ liệu đã có nhưng chưa được đưa ra ngoài bảng để xem nhanh.
- Khối cảnh báo về ảnh hưởng khi lưu cấu hình cũng chưa xuất hiện trên thẻ SLA; nội dung này hiện chỉ nằm bên trong cửa sổ Sửa nên người dùng chỉ thấy khi đã mở cửa sổ.
- Các điểm còn lại đã đạt: không còn Hệ số quá hạn ở cả bảng và cửa sổ Sửa; xóa trắng Số ngày bổ sung tối đa bị chặn kèm thông báo yêu cầu nhập số nguyên dương và giá trị cũ giữ nguyên; dòng Hỏi đáp pháp luật không có ô này; khung giải thích 4 mức cảnh báo hiển thị đầy đủ ở đầu thẻ.


---

# Row 173 — QLPQCN_02

## TIÊU CHÍ GỐC — bắt buộc chấm theo

✅ Loại 2 — cập nhật đặc tả; riêng điểm "không có ô chọn vai trò" thì Dev KHÔNG sửa code (BA duyệt 24/07/2026). Cách chọn vai trò hiện tại của web là ĐÚNG: màn Phân quyền chức năng đã được tái thiết kế theo Pha 5 (CHANGELOG 2026-05-08, BA + PM chốt) và đặc tả SCR-VIII-04 nay ghi "Loại màn hình: 1 vùng panel gập-mở theo module (redesign Pha 5)" (srs-fr-10-quan-tri.md:1693) với thành phần chọn vai trò là "Điều hướng chọn vai trò | select / list" (:1701) → chọn vai trò qua điều hướng từ danh sách Vai trò là hợp lệ, không bắt buộc phải có ô chọn (dropdown) trên màn; kỳ vọng "bộ chọn vai trò + ma trận 6 cột" theo tài liệu thiết kế v2.0 §4.10.4.2 đã hết hiệu lực → đề nghị đối tác cập nhật Kết quả mong đợi theo thiết kế panel-theo-module. VIỆC DUY NHẤT Dev FE phải làm ở màn này: bổ sung chức năng đưa phân quyền của vai trò về mặc định — BA chốt 24/07/2026 GIỮ thành phần này trong bản redesign và đặc tả đã ghi nhận tại :1707 ("Nút Reset | [Reset về mặc định] | click → modal xác nhận | luôn hiển thị"); web hiện chỉ có Quay lại + Lưu. Minor.

── CÁCH VERIFY sau Dev fix ──
Precondition: account admin (vai trò QTHT); Quản trị hệ thống → Tài khoản & phân quyền → danh sách Vai trò. Chọn một vai trò KHÔNG dùng cho test khác (bước 3 sẽ ghi đè phân quyền thật) và chụp lại tập quyền hiện tại trước khi bắt đầu.
1) Từ danh sách Vai trò, mở phân quyền của vai trò "Cán bộ Nghiệp vụ Địa phương" → đọc tiêu đề màn xem có nêu rõ đang phân quyền cho vai trò nào.
2) Quay lại danh sách, mở phân quyền của MỘT vai trò khác (vd "Cán bộ Phê duyệt") → so sánh tập quyền đang tích của 2 vai trò phải khác nhau (không dính dữ liệu của vai trò mở trước).
3) TẠO KHÁC BIỆT RỒI LƯU — bắt buộc, KHÔNG được bỏ: ở vai trò test, tích thêm 2-3 quyền và bỏ tích 2-3 quyền ở các nhóm khác nhau → bấm Lưu → tải lại màn, xác nhận thay đổi ĐÃ lưu → chụp màn hình tập quyền vừa lưu (gọi là ảnh A). Bỏ bước này thì "đưa về mặc định" và "tải lại trạng thái đã lưu" cho kết quả giống hệt nhau, bản cài đặt sai vẫn qua được bài kiểm tra.
4) Bấm chức năng đưa phân quyền về mặc định → quan sát có bước xác nhận không → chọn HỦY → tập quyền phải giữ nguyên đúng như ảnh A.
5) Bấm lại → chọn ĐỒNG Ý → so với ảnh A: tập quyền phải KHÁC. Bấm Lưu, tải lại màn → kết quả sau khi đưa về mặc định vẫn được giữ.
6) Lặp lại bước 3 (đổi vài quyền khác rồi Lưu) và bước 5 một lần nữa → kết quả sau khi đưa về mặc định của 2 lần phải GIỐNG NHAU (chứng tỏ có một bộ mặc định cố định, không phải hoàn tác thao tác gần nhất).
✅ PASS khi: (a) mở phân quyền từ danh sách vai trò luôn tải đúng quyền của vai trò được chọn và màn cho biết rõ đang thao tác trên vai trò nào; (b) có chức năng đưa quyền về mặc định kèm bước xác nhận; (c) chọn Hủy → không đổi; (d) chọn Đồng ý → tập quyền KHÁC ảnh A và lưu/tải lại vẫn giữ; (e) làm 2 lần cho ra cùng một kết quả.
❌ FAIL nếu: không tìm được chức năng đưa quyền về mặc định; chức năng đó áp ngay không hỏi xác nhận; mở vai trò B vẫn hiển thị tập quyền của vai trò A; hoặc sau khi Đồng ý tập quyền TRÙNG KHỚP ảnh A (dấu hiệu chỉ tải lại dữ liệu đã lưu chứ không đưa về mặc định).
⚠️ Bẫy FAIL-oan: màn KHÔNG có ô chọn (dropdown) vai trò là ĐÚNG đặc tả redesign (:1701) — đừng mark FAIL vì thiếu dropdown, cũng đừng yêu cầu Dev dựng lại ma trận 6 cột Xem/Thêm/Sửa/Xóa/Phê duyệt/Xuất.
🔴 CẦN BA CHỐT trước khi kết luận NỘI DUNG bộ mặc định đúng hay sai: SRS chỉ có DUY NHẤT một dòng nói về nút này — "[Reset về mặc định] | click → modal xác nhận" (srs-fr-10-quan-tri.md:1707) — và KHÔNG có mục xử lý nào định nghĩa "mặc định" gồm những quyền gì. §3.4.2 Ma trận phân quyền CRUD (srs-v3.5.md:1277) mới ở mức entity × vai trò với ký hiệu C/R/U/D, chưa ánh xạ xuống 218 mã quyền của màn này (srs-v3.5.md:3113). Vì vậy 6 bước trên chỉ kiểm được chức năng CÓ chạy và cho kết quả ổn định, CHƯA kiểm được bộ mặc định có đúng nội dung không. Đề nghị BA cung cấp bảng quyền mặc định theo từng vai trò ở mức mã quyền; có bảng đó mới bổ sung bước đối chiếu từng quyền.

## Triệu chứng QA ghi nhận lượt trước (sáng 25/07) — CHỈ tham khảo, không phải tiêu chí

- Màn phân quyền không cho biết đang thao tác trên vai trò nào: tiêu đề chỉ ghi "Phân quyền vai trò", đường dẫn phía trên ghi "Vai trò / Chi tiết / Quyền hạn", không hiển thị tên hay mã vai trò ở bất kỳ vị trí nào trên màn. Người dùng không có cách tự xác nhận mình đang sửa đúng vai trò trước khi bấm Lưu.
- Chức năng "Reset về mặc định" hiện chỉ bỏ các thay đổi chưa lưu, chưa khôi phục bộ quyền mặc định của vai trò: sau khi lưu một tập quyền đã bị sửa rồi bấm Reset, hệ thống trả về đúng tập vừa lưu chứ không trở lại bộ quyền gốc của vai trò, dù thông báo xác nhận ghi là khôi phục bộ quyền mặc định.
- Nút "Reset về mặc định" cũng bị làm mờ khi màn chưa có thay đổi nào, nên không dùng được để đưa vai trò về mặc định ở trạng thái bình thường.
- Phần đã đạt: mở phân quyền từ danh sách vai trò nạp đúng bộ quyền của từng vai trò (hai vai trò kiểm thử cho hai tập quyền khác nhau); nút Reset có hỏi xác nhận trước khi áp, chọn Hủy thì tập quyền giữ nguyên; bấm Lưu và tải lại màn thì kết quả được giữ.


---

# Row 174 — QLPQCN_03

## TIÊU CHÍ GỐC — bắt buộc chấm theo

✅ Loại 2 — cập nhật đặc tả; riêng điểm "cách trình bày quyền" thì Dev KHÔNG sửa code (BA duyệt 24/07/2026). Cách hiển thị hiện tại của web là ĐÚNG: theo redesign Pha 5 (CHANGELOG 2026-05-08, BA + PM chốt), đặc tả SCR-VIII-04 nay mô tả "1 vùng duy nhất — danh sách panel gập-mở, mỗi panel = 1 nhóm chức năng (module) theo module_code; render đủ 12 module (Seed 218 quyền = 213 CHUC_NANG + 5 DU_LIEU)" (srs-fr-10-quan-tri.md:1702), mỗi panel gồm block 6 quyền CRUD compact (:1703) + block quyền workflow đặc thù theo nhóm verb (:1705), và §Quy tắc tương tác chốt "render panel theo module_code, không parse prefix ma_quyen" (:1710, :1713) → trình bày quyền theo nhóm chức năng gập-mở là đúng thiết kế, không phải "thiếu cây chức năng"; kỳ vọng ma trận phân quyền theo cây chức năng của tài liệu v2.0 §4.10.4.2 đã bị bản redesign thay thế → đề nghị đối tác cập nhật Kết quả mong đợi. VIỆC DUY NHẤT Dev FE phải làm ở màn này: bổ sung chức năng đưa phân quyền về mặc định (BA chốt 24/07/2026 GIỮ, đặc tả :1707) — theo dõi và verify chi tiết tại dòng QLPQCN_02 để tránh log trùng. Minor.

── CÁCH VERIFY sau Dev fix ──
Precondition: account admin (vai trò QTHT); mở phân quyền của 1 vai trò từ danh sách Vai trò (vd "Cán bộ Nghiệp vụ Địa phương").
1) Đếm số nhóm chức năng (panel) trên màn — phải đủ 12 nhóm, đối chiếu danh sách phân bổ 218 quyền trong đặc tả (srs-v3.5.md:3113): Hỏi đáp, Đào tạo, TVV/CG, Vụ việc, Chi trả, Đánh giá, Biểu mẫu, Quản trị, Báo cáo, Tư vấn chuyên sâu, Tư vấn nhanh, Chương trình HTPL. Tên hiển thị của panel lấy từ dữ liệu (trường tên module tiếng Việt) nên KHÔNG bắt buộc trùng từng chữ với danh sách trên — đủ 12 nhóm và gọi đúng mảng nghiệp vụ là đạt.
2) Gập-mở nhóm "Báo cáo" → kiểm trong nhóm có cả phần quyền cơ bản (xem / thêm / sửa / xóa / phê duyệt-từ chối / xuất) và phần quyền nghiệp vụ riêng; mỗi quyền có tên tiếng Việt đọc hiểu được.
3) Mở thêm 2 nhóm khác (vd "Chi trả", "Đào tạo") → xác nhận cùng cấu trúc, không nhóm nào rỗng.
4) Tích thêm 1 quyền trong nhóm "Báo cáo" → Lưu → tải lại màn → kiểm quyền vừa tích còn được giữ; bỏ tích lại → Lưu để hoàn nguyên.
5) (CHỈ GHI NHẬN — không dùng để chấm PASS/FAIL) Nếu màn có ô chọn nhanh cả nhóm thì thử tích → xem các quyền trong nhóm có được chọn theo và Lưu không báo lỗi. Đặc tả SCR-VIII-04 KHÔNG quy định thành phần này (srs-fr-10-quan-tri.md:1699-1707) nên màn không có ô chọn nhanh cũng KHÔNG phải lỗi.
✅ PASS khi: màn hiển thị đủ 12 nhóm chức năng dạng gập-mở; mỗi nhóm mở ra danh sách quyền có tên rõ ràng gồm cả quyền cơ bản và quyền nghiệp vụ; tích/bỏ tích + Lưu ghi nhận đúng sau khi tải lại màn.
❌ FAIL nếu: thiếu nhóm chức năng so với 12 nhóm đặc tả; nhóm mở ra rỗng; quyền hiển thị bằng mã kỹ thuật không có tên tiếng Việt; hoặc tích quyền + Lưu xong tải lại bị mất.
⚠️ Bẫy FAIL-oan: KHÔNG mark FAIL vì màn không có cây chức năng phân cấp hoặc không có 6 cột hành động — đó là thiết kế cũ đã bị thay (:1693, :1702).
⚠️ Chức năng đưa quyền về mặc định verify ở dòng QLPQCN_02, không lặp ở đây.

## Triệu chứng QA ghi nhận lượt trước (sáng 25/07) — CHỈ tham khảo, không phải tiêu chí

- Màn phân quyền hiển thị 14 nhóm chức năng dạng gập-mở, nhưng 5 nhóm đang lấy mã kỹ thuật làm tên nhóm: BIEU_MAU, CT_HTPLDN, DOANH_NGHIEP, NGUOI_HO_TRO, TU_VAN — trong khi 9 nhóm còn lại có tên tiếng Việt (Báo cáo, Chi trả, Đánh giá, Đào tạo, Hỏi đáp pháp luật, HTPL địa phương, Quản trị hệ thống, Tư vấn viên, Vụ việc HTPL).
- Tên từng quyền bên trong các nhóm đều viết tiếng Việt KHÔNG dấu, ví dụ "Cap nhat bao cao", "Duyet bao cao", "Xem nhat ky kiem toan" — không đồng nhất với phần còn lại của phần mềm.
- Các nội dung khác đã đạt: mọi nhóm mở ra đều có danh sách quyền, gồm cả quyền cơ bản (xem/thêm/sửa/xóa/phê duyệt/xuất) và quyền nghiệp vụ riêng; tích thêm 1 quyền rồi Lưu, tải lại màn vẫn giữ đúng; ô chọn ở đầu nhóm chọn được toàn bộ quyền trong nhóm và Lưu không báo lỗi.


---

# Row 186 — QLDKTK_03

## TIÊU CHÍ GỐC — bắt buộc chấm theo

✅ Bug đúng (BA duyệt 24/07/2026) — cả 2 ý của case này đều là lỗi, verdict Open.

Ý (a) — mục Tài khoản thiếu "Tên đăng nhập": vẫn Open (BUG-QLDKTK_03). Dev FE: mục Tài khoản đăng nhập phải cho DN thấy tên đăng nhập của mình ở dạng chỉ đọc, lấy theo Mã số thuế DN đang khai và tự cập nhật khi MST thay đổi (SRS srs-fr-10-quan-tri.md:1886 — SCR-VIII-08 Nhóm 2 row 25; AC :1110–:1111; Processing bước 3 :1078 "Set username = ma_so_thue"). Mức Minor.

Ý (b) — mục Tài khoản thừa "Họ và tên người đăng ký" + "Số điện thoại": BA chốt 24/07/2026 **GỠ 2 ô này khỏi biểu mẫu đăng ký, KHÔNG bổ sung vào SRS**. Căn cứ SRS đã kiểm nguyên văn: `srs-fr-10-quan-tri.md:1885`–`:1889` (SCR-VIII-08 "Nhóm 2 — Tài khoản đăng nhập (3 trường nhập + 1 ô hiển thị readonly)" chỉ gồm Tên đăng nhập chỉ đọc / Mật khẩu / Xác nhận mật khẩu / Cam kết thông tin đúng sự thật) + `:1067`–`:1070` (FR-VIII-22 §Inputs, nhóm "Thông tin tài khoản" đúng 3 trường) + AC `:1110` bản cập nhật 24/07/2026 đếm "27 trường nhập gồm: 24 trường thông tin DN, 2 trường mật khẩu, và 1 ô cam kết" — không có 2 trường này. Tên đăng nhập gắn theo MST của DN nên luồng đăng ký không cần thu thông tin người đăng ký tách riêng. Mức Minor/Cosmetic.

── CÁCH VERIFY sau Dev fix ──
Precondition: KHÔNG cần tài khoản — biểu mẫu công khai https://18.143.165.120.nip.io/register/doanh-nghiep. Nếu đang có phiên đăng nhập thì đăng xuất hoặc mở cửa sổ ẩn danh để chắc chắn render bản công khai.
1) Mở URL trên, cuộn hết biểu mẫu, đọc nhãn từng ô trong mục "Thông tin tài khoản".
2) Đếm số ô nhập của riêng mục "Thông tin tài khoản" (không tính nút bấm).
3) Nhập Mã số thuế 10 chữ số chưa từng đăng ký (vd 0101234567) vào ô Mã số thuế ở mục Thông tin doanh nghiệp → quay lại xem mục Tài khoản.
4) Sửa Mã số thuế thành 0107654321 → xem lại giá trị tên đăng nhập (KHÔNG tải lại trang).
5) Điền đủ mọi ô bắt buộc còn lại + email chưa dùng + tích ô cam kết → bấm Đăng ký.
✅ PASS khi ĐỦ 4 điều: (i) mục Tài khoản KHÔNG còn ô "Họ và tên người đăng ký" và KHÔNG còn ô "Số điện thoại" của người đăng ký; (ii) mục Tài khoản còn đúng 4 mục — tên đăng nhập (chỉ đọc) + Mật khẩu + Xác nhận mật khẩu + ô cam kết; (iii) bước 3 tên đăng nhập hiển thị đúng 0101234567 và bước 4 tự đổi thành 0107654321 mà không cần tải lại trang; (iv) bước 5 đăng ký được chấp nhận, không có lỗi "bắt buộc" nào trỏ vào 2 ô đã gỡ.
❌ FAIL nếu: còn 1 trong 2 ô đã gỡ hiển thị trên biểu mẫu; HOẶC ô chỉ bị ẩn khỏi giao diện nhưng dữ liệu người đăng ký (hoTen / soDienThoaiTaiKhoan) vẫn nằm trong DOM và vẫn được gửi lên khi đăng ký; HOẶC vẫn không có ô tên đăng nhập chỉ đọc; HOẶC tên đăng nhập không đổi theo Mã số thuế.
⚠️ Bẫy 1 — KHÔNG nhầm sang ô "Điện thoại doanh nghiệp" ở mục Thông tin doanh nghiệp: SRS bắt buộc giữ ô này (`srs-fr-10-quan-tri.md:1057` Inputs row 15 Bắt buộc = Y; `:1875` SCR row 15) và đây chính là bug QLDKTK_08 vừa đóng 23/07/2026. Gỡ nhầm ô này, hoặc làm mất dấu bắt buộc của nó, = FAIL và làm tái phát QLDKTK_08.
⚠️ Bẫy 2 — "Người đại diện pháp luật" (`:1054`) và "Số điện thoại liên hệ" của DN (`:1057`) ở mục Thông tin doanh nghiệp là 2 trường KHÁC, phải giữ nguyên; chỉ 2 ô trong mục Tài khoản mới bị gỡ.
⚠️ Bẫy 3 — nếu bước 5 bị chặn vì "Mã số thuế đã có trong hệ thống" hoặc "Email đã được sử dụng" thì đổi MST/email khác rồi chạy lại; đó KHÔNG tính FAIL của case này.
Ảnh lỗi cũ (mục Tài khoản: có Họ tên + SĐT người đăng ký, thiếu Tên đăng nhập): image/BUG-QLDKTK_02_03_08-form-dangky-full.png

## Triệu chứng QA ghi nhận lượt trước (sáng 25/07) — CHỈ tham khảo, không phải tiêu chí

- Mục "Tài khoản đăng nhập" trên biểu mẫu đăng ký hiện chỉ có 3 thành phần: Mật khẩu, Xác nhận mật khẩu và ô cam kết — vẫn chưa có ô Tên đăng nhập ở dạng chỉ đọc.
- Do không có ô này nên khi nhập Mã số thuế (thử 0101234567 rồi đổi sang 0107654321) cũng không có chỗ nào hiển thị tên đăng nhập tương ứng để doanh nghiệp biết mình sẽ đăng nhập bằng gì.
- Phần đã đạt: hai ô "Họ và tên người đăng ký" và "Số điện thoại" của người đăng ký đã được gỡ khỏi mục Tài khoản, không còn tồn tại ẩn trong trang; ô "Điện thoại doanh nghiệp" ở mục Thông tin doanh nghiệp vẫn giữ nguyên và vẫn bắt buộc.
- Đăng ký thử với đầy đủ thông tin bắt buộc vẫn thành công bình thường, không phát sinh lỗi bắt buộc nào liên quan đến hai ô đã gỡ.
