# Backup cột `DEV phản hồi lần 2` — trước đợt re-verify R4

**Thời điểm trích:** 2026-07-30 21:36:16
**Sheet:** `1OKBN2otlmdZ44THkmhtsn-_63M2Boh7zQwearwjYR3s` (UAT-PM HTPLDN)

> Trích nguyên văn để phục hồi nếu verdict Reopen ghi đè mất nội dung (quyết định BA 30/07 + CÁCH VERIFY).

---

## KTDGKQHT_03 — tab `UAT_TGPL Doanh Nghiệp-tuần 2`, row 5

- `Trạng thái dev fix 1` = `dev done` · `Verify` = `Pass`
- `Trạng thái dev fix 2` = `(trống)` · `Verify 2` = `(trống)`
- `Trạng thái 2` = `(trống)` · `Kết quả thực tế lần 2` = (trống)

### DEV phản hồi lần 2 (nguyên văn)

```text
(TRỐNG)
```

---

## QLKTLBG_02 — tab `UAT_TGPL Doanh Nghiệp-tuần 2`, row 8

- `Trạng thái dev fix 1` = `dev done` · `Verify` = `Pass`
- `Trạng thái dev fix 2` = `dev done` · `Verify 2` = `Open`
- `Trạng thái 2` = `Fail` · `Kết quả thực tế lần 2` = 'Hệ thống hiển thị thiếu các trường thông tin: Ảnh xem trước, Lĩnh vực, Người tạo'

### DEV phản hồi lần 2 (nguyên văn)

```text
✅ Bug đúng (BA chốt 30/07/2026). Dev FE: bổ sung 3 cột còn thiếu vào bảng danh sách Kho tài liệu / Bài giảng — Ảnh đại diện, Lĩnh vực, Người tạo — đưa bảng về đủ 9 cột. Mức Major.

Căn cứ BA đưa:
- SCR-III-03 (srs-fr-03-dao-tao.md:1904-1910) không tự liệt kê cột nào mà ủy quyền qua dòng "UX-Spec ref" sang dac-ta-man-hinh-chuc-nang-v2.md — MH-03.3 (dòng 1625-1637), nơi liệt kê đủ 9 cột: Ảnh đại diện · Tên bài giảng · Loại tài liệu · Lĩnh vực · Dung lượng · Công khai · Người tạo · Ngày tạo · Hành động.
- Bản bàn giao HTPLDN-PTYC-CT-v2.0.docx mục 4.3.7.2.2 (bảng "Cột dữ liệu trong bảng kết quả", STT 5→13) liệt kê trùng khớp đúng 9 cột đó.
- Cả 3 trường đều có sẵn trong nhóm dữ liệu BAI_GIANG: anh_dai_dien (srs-v3.5.md:2477), linh_vuc_ids (:2482), created_by (:2486) — không phải yêu cầu phát sinh ngoài mô hình.
- Lý do bắt buộc: màn đã có bộ lọc "Lĩnh vực pháp luật" nhưng không có cột tương ứng nên lọc xong không đọc được kết quả theo tiêu chí gì; cột Người tạo cần cho phân định trách nhiệm giữa các đơn vị dùng chung kho tài liệu.
- BA đã nội hóa bảng 9 cột vào thân SCR-III-03 ngày 30/07/2026, không còn phụ thuộc dòng "UX-Spec ref".

BA chốt kèm 3 điểm phạm vi:
(a) Cột ảnh dùng nhãn "Ảnh đại diện" (đồng bộ với tên trường và với nhãn ở Bảng xem trước), KHÔNG dùng "Ảnh xem trước".
(b) Cột Công khai là nhãn trạng thái CHỈ HIỂN THỊ — không dựng công tắc bật/tắt tại dòng; thao tác công khai vẫn nằm ở biểu mẫu thêm/sửa.
(c) "Khóa học liên kết" KHÔNG đưa thành cột (một bài giảng dùng lại ở nhiều khóa, một ô cột không chứa nổi). Nút "Xuất Excel" được BA tách thành hạng mục riêng, NGOÀI phạm vi sửa lỗi này.

Đính chính phản hồi vòng 1: câu "Đã kiểm tra lại, không tái hiện được lỗi" ở lần trước không còn đúng — thiếu 3 cột là lỗi thật, xin được rút lại.

── CÁCH VERIFY sau Dev fix ──
Precondition: tài khoản cbnv_tw / Test@1234 trên https://18.143.165.120.nip.io; menu "Đào tạo, tập huấn" → "Kho tài liệu / Bài giảng"; giữ bộ lọc mặc định (không lọc gì).
1) Đọc header bảng danh sách: đếm số cột và ghi lại nhãn từng cột.
2) Chọn 1 bài giảng ĐÃ có ảnh đại diện và ĐÃ gán ít nhất 1 lĩnh vực (chưa có thì tự tạo qua [+ Thêm mới]) — đọc 3 ô của đúng dòng đó: ô cột ảnh, ô cột Lĩnh vực, ô cột Người tạo.
3) Chọn 1 bài giảng KHÔNG có ảnh đại diện và KHÔNG gán lĩnh vực — đọc lại 3 ô đó.
4) Mở bộ lọc "Lĩnh vực pháp luật", chọn 1 lĩnh vực cụ thể → bấm Tìm kiếm → đọc cột Lĩnh vực của mọi dòng trả về.
5) Bấm thẳng vào ô cột "Công khai" của 1 dòng bất kỳ.
✅ PASS khi ĐỦ 5 điều: (1) bảng có đúng 9 cột — Ảnh đại diện · Tên bài giảng · Loại tài liệu · Lĩnh vực · Dung lượng · Công khai · Người tạo · Ngày tạo · Hành động; (2) bước 2 cả 3 ô đều có dữ liệu thật — ảnh thu nhỏ hiển thị được, Lĩnh vực đúng lĩnh vực đã gán cho chính bài giảng đó, Người tạo đúng họ tên tài khoản đã tạo bản ghi; (3) bước 3 ô ảnh rơi về biểu tượng mặc định theo loại tài liệu, 2 ô còn lại hiện dấu "—" chứ không để trắng / "null" / "undefined"; (4) bước 4 mọi dòng trả về đều chứa lĩnh vực vừa lọc; (5) bước 5 ô Công khai không đổi giá trị khi bấm (là nhãn chỉ đọc).
❌ FAIL nếu: bảng vẫn 6 cột như ảnh cũ; thiếu bất kỳ cột nào trong 3 cột Ảnh đại diện / Lĩnh vực / Người tạo; cột có mặt nhưng ô rỗng ngay trên bản ghi đã có dữ liệu (bước 2); ô cột Công khai bật/tắt được tại dòng.
⚠️ Bẫy cần tránh: (a) KHÔNG báo FAIL vì thiếu cột "Khóa học liên kết" hoặc thiếu nút "Xuất Excel" — BA đã tách khỏi phạm vi lỗi này; (b) nhãn các cột khác không cần trùng từng ký tự, đúng ý nghĩa cột là đạt — riêng cột ảnh phải là "Ảnh đại diện" chứ không phải "Ảnh xem trước" (BA chốt điểm a); (c) KHÔNG kết luận đạt chỉ vì header đủ 9 nhãn — bắt buộc kiểm ô có dữ liệu ở bước 2.
Ảnh lỗi cũ: QLKTLBG_02_v2.jpg (cột "Ảnh/video 2").
```

---

## DKTGMLTVV_03 — tab `UAT_TGPL Doanh Nghiệp-tuần 2`, row 53

- `Trạng thái dev fix 1` = `dev done` · `Verify` = `Pass`
- `Trạng thái dev fix 2` = `dev done` · `Verify 2` = `Open`
- `Trạng thái 2` = `Fail` · `Kết quả thực tế lần 2` = '- Nhóm 2 — Thông tin chuyên môn: SRS quy định chỉ hiển thị các trường Trình độ chuyên môn, Chuyên ngành đào tạo, Số năm '

### DEV phản hồi lần 2 (nguyên văn)

```text
✅ Bug đúng một phần (BA chốt 30/07/2026) — 3 việc Dev phải sửa, 1 ý không phải lỗi. Chi tiết 4 mục dưới đây.

[1] ❌ Bộ trường nhóm "Nghề nghiệp" — KHÔNG phải lỗi (BA xác nhận 30/07/2026).
- BA chốt: phần mềm ĐÚNG. 11 trường đang hiển thị đều có căn cứ — 9 mục theo SCR-IV-02 nhóm 2 (srs-fr-04-chuyen-gia-tvv.md:1495-1504), cộng 2 trường Chuyên ngành / Số năm kinh nghiệm theo FR-IV-03 §Inputs (:304, :305) và §Processing bước 7 (:323).
- Nguyên nhân hai vòng ghi nhận ngược nhau: bản bàn giao .docx mô tả HAI màn hình khác nhau (mục 4.4.1.3.2 "Cán bộ thêm/sửa Tư vấn viên" — nhóm 2 có 12 trường; mục 4.4.3.2.2 "Người hỗ trợ đăng ký ứng viên" — màn riêng, nhóm 2 chỉ 3 trường), trong khi SRS gộp làm MỘT màn SCR-IV-02 dùng chung. Quý đơn vị kiểm với vai trò Người hỗ trợ nên đối chiếu mục 4.4.3.2.2 và thấy 3 trường. Cả hai vòng đều trích đúng, chỉ là trích hai mục khác nhau.
- Không rút nhóm 2 về 3 trường: làm vậy sẽ gỡ "Số thẻ hành nghề" và "Tệp thẻ hành nghề" khỏi màn Người hỗ trợ đăng ký, trong khi SCR-IV-02 mục 3.5 ghi rõ đây là thành phần bắt buộc với ứng viên loại Tư vấn viên theo Điều 20 Nghị định 77/2008/NĐ-CP — cán bộ sẽ không còn gì để thẩm định nhóm tiêu chí Pháp lý.
- BA xác nhận bản mô tả trong tài liệu bàn giao (mục 4.4.3.2.2) đang thiếu so với đặc tả, sẽ gửi lại bản cập nhật mới nhất khi bàn giao fix bug tuần. Đối tác cập nhật lại Kết quả mong đợi của test case cho khớp.

[2] ✅ Bug đúng (BA 30/07/2026) — "Chuyên ngành" và "Số năm kinh nghiệm" đang để tùy chọn.
- Dev BE/FE: đặt hai trường này là BẮT BUỘC trên luồng Người hỗ trợ đăng ký ứng viên mới (FR-IV-03 §Inputs :304 chuyen_nganh = Y, :305 so_nam_kinh_nghiem = Y; bản .docx 4.4.3.2.2 STT 9 và 10 cột Bắt buộc cũng ghi "Có" — hai nguồn khớp nhau, không có tranh chấp tài liệu). GIỮ tùy chọn trên luồng cán bộ sửa hồ sơ đã có (FR-IV-04 §Inputs :382). Mức Major — hai trường là căn cứ để cán bộ chấm nhóm tiêu chí Năng lực chuyên môn ở bước thẩm định (SCR-IV-03 mục 15); thiếu thì phải trả hồ sơ về yêu cầu bổ sung.
- Chặn kỹ thuật đã được BA gỡ trước: nhóm dữ liệu TU_VAN_VIEN vốn THIẾU HẲN trường chuyen_nganh dù 4 nơi đang dùng tới; BA đã bổ sung trường này vào SRS ngày 30/07/2026 (4 vị trí). Dev đã có chỗ lưu rồi mới đặt ràng buộc bắt buộc.

[3] ✅ Bug đúng (BA 30/07/2026) — form đang có 6 nhóm thay vì 5.
- Dev FE: GIỮ NGUYÊN hai trường "Số quyết định công bố" / "Ngày quyết định công bố" (có trong nhóm dữ liệu TU_VAN_VIEN :155, :156 và trong mẫu xuất Phụ lục 1 QĐ 1322/QĐ-BTP :2212, :2213) nhưng chuyển chúng vào Nhóm 2 "Thông tin nghề nghiệp", KHÔNG để thành nhóm thứ 6 riêng. Căn cứ: SCR-IV-02:1476 quy định 5 nhóm; bản .docx 4.4.1.3.2 đặt đúng hai trường này ở Nhóm 2, STT 21 và 22, ngay sau Chức vụ hiện tại / Nơi công tác hiện tại. Mức Cosmetic — gộp nhóm, KHÔNG gỡ trường.
- BA đã bổ sung 4 mục 3.8→3.11 vào bảng SCR-IV-02 nhóm 2 ngày 30/07/2026.

[4] ✅ Bug ĐÚNG – chuyển dev — lỗi QA phát hiện thêm khi soi cùng form này (giữ nguyên từ vòng trước):
- Trường "Tổ chức hành nghề chính" đang bị đặt BẮT BUỘC: để trống rồi bấm Lưu thì hệ thống chặn với thông báo "Tổ chức chính là bắt buộc".
- Theo đặc tả, trường này là TÙY CHỌN và ghi rõ lý do "tư vấn viên tự do để trống": SCR-IV-02 nhóm 3 mục 4.1 (srs-fr-04-chuyen-gia-tvv.md:1506), và FR-IV-03 (UC41) §Inputs #14 (dòng 307) cũng ghi to_chuc_id là không bắt buộc. Hệ quả: hiện KHÔNG đăng ký được tư vấn viên hành nghề tự do vào mạng lưới.
- BA xác nhận 30/07/2026: chốt TÙY CHỌN. Baseline srs-v3.5.md:1710 cũng ghi N kèm chú thích "optional — TVV tự do có thể NULL [CR-02]"; chỉ srs-fr-04-chuyen-gia-tvv.md:150 ghi Y và BA đã sửa Y → N ngày 30/07 — nếu không sửa thì Dev gỡ ràng buộc ở giao diện xong phần xử lý phía sau vẫn từ chối, phiếu bị mở lại.
- Bug ID: BUG-DKTGMLTVV_03

── CÁCH VERIFY sau Dev fix ──
Precondition: 2 tài khoản trên https://18.143.165.120.nip.io — nht_qa_tw / Test@1234 (Người hỗ trợ pháp lý, Cục Bổ trợ tư pháp - Bộ Tư pháp) và cbnv_tw / Test@1234 (Cán bộ Nghiệp vụ Trung ương). Màn: "Mạng lưới tư vấn viên" → "Tư vấn viên/Chuyên gia" → tab "Mới đăng ký" → [Thêm mới].
1) Login nht_qa_tw → mở form Thêm mới → đếm số nhóm (section) và đọc nhãn từng nhóm.
2) Vẫn ở form đó: tìm vị trí của "Số quyết định công bố" và "Ngày quyết định công bố" — ghi lại chúng nằm ở nhóm nào.
3) Chọn Loại = Tư vấn viên, điền đủ các trường bắt buộc khác nhưng ĐỂ TRỐNG "Chuyên ngành" và "Số năm kinh nghiệm" → bấm Lưu.
4) Điền "Chuyên ngành" = "Luật Kinh tế", "Số năm kinh nghiệm" = 5 → bấm Lưu → mở lại chính hồ sơ vừa tạo và đọc 2 trường đó.
5) Trên form Thêm mới: ĐỂ TRỐNG "Tổ chức hành nghề chính", điền đủ các trường bắt buộc còn lại → bấm Lưu.
6) Login cbnv_tw → bấm [Sửa] một hồ sơ tư vấn viên ĐÃ CÓ → xóa trống "Chuyên ngành" → bấm Lưu.
✅ PASS khi ĐỦ 5 điều: (1) bước 1 form có đúng 5 nhóm, không còn nhóm riêng cho quyết định công bố; (2) bước 2 hai trường "Số QĐ công bố" / "Ngày QĐ công bố" nằm trong nhóm "Thông tin nghề nghiệp"; (3) bước 3 hệ thống CHẶN lưu và chỉ rõ hai trường Chuyên ngành + Số năm kinh nghiệm còn thiếu; (4) bước 4 lưu thành công VÀ mở lại hồ sơ thấy đúng "Luật Kinh tế" và 5 (giá trị được ghi xuống, không mất); (5) bước 5 lưu THÀNH CÔNG với Tổ chức hành nghề chính để trống, và bước 6 cũng lưu thành công với Chuyên ngành để trống.
❌ FAIL nếu: form vẫn 6 nhóm, hoặc hai trường quyết định công bố nằm ngoài nhóm 2; bước 3 lưu lọt, hoặc chỉ chặn 1 trong 2 trường; bước 4 lưu được nhưng mở lại hồ sơ thì Chuyên ngành trống; bước 5 hoặc bước 6 bị chặn.
⚠️ Bẫy cần tránh: (a) KHÔNG báo "thừa trường" ở nhóm 2 — BA đã chốt bộ trường hiện tại là đúng, đừng đếm lại theo bản .docx cũ; (b) hai trường Chuyên ngành / Số năm kinh nghiệm chỉ bắt buộc ở luồng ĐĂNG KÝ MỚI (bước 3); nếu bắt buộc luôn ở luồng SỬA hồ sơ cũ (bước 6) thì là FAIL; (c) bước 4 bắt buộc mở lại hồ sơ để kiểm — chỉ thấy thông báo lưu thành công là chưa đủ, vì lỗi có thể nằm ở chỗ không có trường để lưu; (d) tiêu chí bước 3 là CHẶN KHI BẤM LƯU, không tính riêng việc nhãn có dấu sao hay không.
Ảnh lỗi cũ: DKTGMLTVV_03_v2.jpg (cột "Ảnh/video 2").
```

---

## QLHSTVV_03 — tab `UAT_TGPL Doanh Nghiệp-tuần 2`, row 58

- `Trạng thái dev fix 1` = `dev done` · `Verify` = `Pass`
- `Trạng thái dev fix 2` = `dev done` · `Verify 2` = `Open`
- `Trạng thái 2` = `Fail` · `Kết quả thực tế lần 2` = '- Nhóm 2 thông tin nghề nghiệp thừa trường Số quyết định (công nhận)\n- Nhóm 3 — Tổ chức thừa trường Địa bàn'

### DEV phản hồi lần 2 (nguyên văn)

```text
✅ Bug đúng một phần (BA chốt 30/07/2026) — 2 việc Dev phải sửa, 1 ý không phải lỗi. Chi tiết 3 mục dưới đây.

[1] ✅ Bug ĐÚNG – chuyển dev — mục "Địa bàn" ở nhóm Tổ chức (giữ nguyên từ vòng trước, BA xác nhận 30/07/2026):
- Ảnh anh/chị gửi cho thấy rất rõ nhóm "Tổ chức & Mạng lưới" có mục "Địa bàn". Anh/chị phản ánh đúng: theo đặc tả, tư vấn viên KHÔNG còn khái niệm địa bàn nữa, trường này đã được bỏ hẳn vì thẻ tư vấn viên có hiệu lực toàn quốc theo Nghị định 77/2008 Điều 19 (srs-fr-04-chuyen-gia-tvv.md dòng 46 và dòng 153 — đánh dấu "Bỏ field này"). Đặc tả còn ghi rõ bộ lọc "địa bàn" ở màn danh sách phải hiểu là lọc theo đơn vị công nhận, không phải theo địa bàn của tư vấn viên (dòng 233).
- BA xác nhận 30/07/2026: nguyên tắc bỏ địa bàn của Tư vấn viên còn nguyên hiệu lực ở v3.5; bản bàn giao .docx mục 4.4.11.2.2 nhóm 3 "Tổ chức" cũng chỉ có Tổ chức chủ quản và Tổ chức đối tác, không có Địa bàn. Dev gỡ dứt điểm mục "Địa bàn". Mức Major.
- Lưu ý khi kiểm lại: QA chạy đúng các bước anh/chị mô tả với cùng vai trò Cán bộ Nghiệp vụ Trung ương, thử trên 2 hồ sơ khác nhau và cả hai lần đều KHÔNG thấy mục "Địa bàn" hiện ra — nhiều khả năng lệch bản triển khai giữa hai môi trường. Vì bằng chứng của anh/chị rất rõ và đặc tả thì cấm hẳn trường này, QA vẫn chuyển dev để dev rà và gỡ dứt điểm.
- Bug ID: BUG-QLHSTVV_03

[2] ❌ Số nhóm của thẻ "Hồ sơ" — KHÔNG phải lỗi (BA xác nhận 30/07/2026).
- BA chốt: hồ sơ tư vấn viên gồm SÁU nhóm thông tin, trong đó nhóm (f) "Thông tin công khai" chỉ hiển thị với hồ sơ đã được công khai lên Cổng pháp luật quốc gia (srs-fr-04-chuyen-gia-tvv.md:1556). Bản bàn giao .docx mục 4.4.11.2.2 ghi "5 nhóm" là bản chưa theo kịp đặc tả — BA xác nhận bản SRS docx đang lỗi thời, sẽ gửi lại bản cập nhật mới nhất khi bàn giao fix bug tuần. Phần mềm hiển thị 6 nhóm là ĐÚNG, Dev không sửa ý này.
- BA chốt kèm cách hiểu tài liệu: dòng :1556 là mô tả RÚT GỌN ở cấp NHÓM, không phải danh sách đóng ở cấp trường — nên không suy ra được "mục không có trong dòng đó là mục thừa". Bằng chứng nằm trong chính nó: nhóm (b) chỉ ghi "chức vụ + nơi công tác + trình độ, chứng chỉ, số thẻ, kinh nghiệm", bỏ qua "Bằng cấp chi tiết" và "Chứng chỉ chi tiết" trong khi SCR-IV-02 mục 3.3, 3.4 quy định hai mục này có trong hồ sơ và không ai coi là thừa. BA đã ghi rõ điều này vào SCR-IV-03 ngày 30/07/2026.
- Đối tác cập nhật lại Kết quả mong đợi của test case: 6 nhóm, nhóm thứ 6 chỉ hiện với hồ sơ đã công khai.

[3] ✅ Bug đúng (BA 30/07/2026) — không tra được "Số quyết định công nhận" ở màn chi tiết.
- BA chốt: đây là trường bắt buộc nhập khi Cán bộ Phê duyệt duyệt hồ sơ (FR-IV-07 §Inputs :583, mã lỗi ERR-PD-05 ở :616) và có tên trong mẫu xuất Phụ lục 1 (:2027), nhưng KHÔNG mục nào của màn chi tiết đang hiển thị nó — đặc tả bỏ trống. Dev BE/FE: bổ sung "Số quyết định công nhận" vào THẺ THÔNG TIN CHÍNH ở đầu trang chi tiết tư vấn viên, đặt cạnh "Ngày công nhận" đã có sẵn (SCR-IV-03 mục 3, :1543); hiển thị khi hồ sơ đã qua phê duyệt, để trống ở các trạng thái trước. KHÔNG đưa vào thẻ "Hồ sơ". Mức Major.
- Lý do BA không đưa vào thẻ "Hồ sơ": thẻ đó phản chiếu hồ sơ ứng viên TỰ KHAI, còn số quyết định là KẾT QUẢ XỬ LÝ của cơ quan — trộn hai loại dữ liệu sẽ khiến người đọc tưởng ứng viên tự khai số quyết định. Số quyết định và ngày công nhận là hai vế của cùng một quyết định nên phải đứng cạnh nhau.
- BA đã bổ sung mục này vào SCR-IV-03 ngày 30/07/2026.
- Về việc Quý đơn vị báo "Số quyết định (công nhận)" là mục THỪA ở nhóm Nghề nghiệp: BA ghi nhận Quý đơn vị quan sát đúng (cả .md lẫn .docx đều không đặt mục này trong nhóm Nghề nghiệp), nhưng bản QA kiểm lại không thấy mục đó ở đâu trên màn, kể cả trên hồ sơ có số quyết định thật — chênh lệch là do lệch bản triển khai giữa hai môi trường. Sau khi Dev đưa trường về thẻ đầu trang thì điểm này tự hết.

── CÁCH VERIFY sau Dev fix ──
Precondition: cbnv_tw / Test@1234 trên https://18.143.165.120.nip.io. Cần 2 hồ sơ tư vấn viên: (A) 1 hồ sơ ĐÃ được phê duyệt/công nhận (có số quyết định công nhận thật, dạng QĐ-…/QĐ-BTP) và ĐÃ công khai; (B) 1 hồ sơ CHƯA qua phê duyệt (Mới đăng ký / Đang thẩm định). Màn: "Mạng lưới tư vấn viên" → "Tư vấn viên/Chuyên gia" → xem chi tiết.
1) Mở chi tiết hồ sơ (A) → đọc thẻ thông tin chính ở đầu trang, liệt kê các mục đang hiển thị.
2) Vẫn ở hồ sơ (A) → mở thẻ "Hồ sơ", bung hết các nhóm thu gọn → đếm số nhóm, đọc nhãn từng nhóm, và đọc hết nhãn các mục trong nhóm "Nghề nghiệp" và nhóm "Tổ chức".
3) Mở chi tiết hồ sơ (B) → đọc lại thẻ đầu trang và thẻ "Hồ sơ".
✅ PASS khi ĐỦ 4 điều: (1) thẻ đầu trang của hồ sơ (A) hiển thị "Số quyết định công nhận" với đúng số quyết định của chính hồ sơ đó, đứng cạnh "Ngày công nhận"; (2) thẻ "Hồ sơ" của (A) có 6 nhóm, trong đó có nhóm "Thông tin công khai"; (3) trong toàn bộ thẻ "Hồ sơ" của (A) KHÔNG còn mục "Địa bàn" ở nhóm Tổ chức và KHÔNG còn "Số quyết định (công nhận)" ở nhóm Nghề nghiệp; (4) hồ sơ (B) chưa qua phê duyệt thì mục "Số quyết định công nhận" ở thẻ đầu trang để trống hoặc không hiển thị, và thẻ "Hồ sơ" chỉ có 5 nhóm (chưa có nhóm Thông tin công khai).
❌ FAIL nếu: hồ sơ (A) không tra được số quyết định công nhận ở bất kỳ đâu trên màn chi tiết; số quyết định có hiển thị nhưng nằm trong thẻ "Hồ sơ" thay vì thẻ đầu trang; vẫn còn mục "Địa bàn"; hồ sơ (B) đã hiện số quyết định dù chưa được phê duyệt.
⚠️ Bẫy cần tránh: (a) KHÔNG báo FAIL vì thẻ "Hồ sơ" có 6 nhóm thay vì 5 — BA đã chốt 6 nhóm là đúng; (b) hồ sơ CHƯA công khai chỉ có 5 nhóm cũng ĐÚNG, nhóm thứ 6 vốn chỉ hiện khi đã công khai, nên phải kiểm trên hồ sơ đã công khai mới kết luận được; (c) nhãn mục không cần trùng từng ký tự, đúng ý nghĩa là đạt; (d) nếu vẫn thấy "Địa bàn", ghi kèm mã tư vấn viên cụ thể vì lần kiểm trước không tái hiện được trên môi trường QA.
Ảnh lỗi cũ: QLHSTVV_03_v2.jpg (cột "Ảnh/video 2").
```

---

## TDHSTVV_14 — tab `UAT_TGPL Doanh Nghiệp-tuần 2`, row 68

- `Trạng thái dev fix 1` = `dev done` · `Verify` = `Pass`
- `Trạng thái dev fix 2` = `dev done` · `Verify 2` = `Open`
- `Trạng thái 2` = `Fail` · `Kết quả thực tế lần 2` = 'Người hỗ trợ không nhận được thông báo kèm lý do'

### DEV phản hồi lần 2 (nguyên văn)

```text
✅ Bug đúng (BA chốt 30/07/2026). Kỳ vọng của Quý đơn vị được xác nhận: Người hỗ trợ pháp lý ĐÃ NỘP hồ sơ phải nhận được thông báo kèm lý do khi hồ sơ bị kết luận "Không đạt".

Căn cứ BA đưa:
- Bản bàn giao HTPLDN-PTYC-CT-v2.0.docx mục 4.4.5 ghi người nhận là Người hỗ trợ ở BA chỗ độc lập: 4.4.5.1 Mục đích ("gửi thông báo cho Người hỗ trợ khi có kết quả"); 4.4.5.2.1 dòng "Lý do bổ sung / từ chối"; 4.4.5.2.2 nút "Gửi kết quả thẩm định" Trường hợp 2 ("gửi thông báo kèm lý do đến Người hỗ trợ, lưu vết thao tác, hiển thị thông báo 'Đã từ chối hồ sơ'"). Kết quả mong đợi trong phiếu là bản chép nguyên văn dòng cuối.
- Vì vậy SRS FR-IV-06 chỉ nêu chủ hồ sơ là BỊ SÓT, không phải Quý đơn vị kỳ vọng ngoài đặc tả — nhận định "kỳ vọng nằm ngoài SRS" ở phản hồi trước xin được rút lại.
- Ba lý do BA nêu là bắt buộc: (a) ứng viên bị từ chối ở bước thẩm định CHƯA có tài khoản (tài khoản chỉ được cấp khi Cán bộ Phê duyệt duyệt — :2326), nên trong phần mềm không vai trò nào nhìn thấy kết quả từ chối; (b) người phải hành động sau khi bị từ chối là Người hỗ trợ, vì ứng viên không có tài khoản để sửa hồ sơ và FR-IV-03 đặt Người hỗ trợ là người nộp; (c) chiều đi đã có sẵn (FR-IV-03 §Processing bước 8: Người hỗ trợ nộp thì hệ thống báo Cán bộ Nghiệp vụ cùng đơn vị), chiều về thiếu hẳn.
- BA đã bổ sung Người hỗ trợ vào danh sách người nhận trong SRS ngày 30/07/2026 (FR-IV-06 §Processing bước 5 và 6, §Postconditions, bảng SM-TVV, Tiêu chí chấp nhận, SCR-IV-03 mục 20c).

Việc Dev phải làm — BA chốt 4 điểm:
1. Bổ sung Người hỗ trợ ĐÃ NỘP hồ sơ vào danh sách người nhận thông báo, áp cho CẢ HAI kết luận "Không đạt" VÀ "Yêu cầu bổ sung" (sửa một chỗ bỏ chỗ kia thì vòng sau sẽ log lại). GIỮ NGUYÊN thư gửi chủ hồ sơ đang chạy đúng.
2. Đi CẢ HAI kênh: thông báo trong phần mềm và thư điện tử, theo quy ước BR-NOTIF-01 (srs-v3.5.md:5591 — "in-app + email"). Ứng viên vẫn chỉ nhận thư điện tử.
3. Thông báo trong phần mềm hiển thị cho vai trò Người hỗ trợ — vai trò duy nhất có tài khoản và có việc phải làm tiếp.
4. Câu chữ thông báo sau khi bấm "Gửi KQ": kết luận "Không đạt" → thông báo phản ánh việc hồ sơ đã bị TỪ CHỐI (BA chốt dùng "Đã từ chối hồ sơ"); kết luận "Yêu cầu bổ sung" → phản ánh việc đã gửi yêu cầu bổ sung đến Người hỗ trợ. Hiện hệ thống đang hiện "Đã lưu kết quả thẩm định" cho cả hai trường hợp.
Mức Major.

Việc liên quan — BA chốt cùng ngày, NGOÀI phạm vi dòng này, ghi ra để Dev không sửa sót: ở bước PHÊ DUYỆT (FR-IV-07), người nhận thông báo khi Cán bộ Phê duyệt từ chối gồm Cán bộ Nghiệp vụ đã thẩm định + chủ hồ sơ + Người hỗ trợ đã nộp hồ sơ; và người sửa rồi nộp lại hồ sơ sau khi bị từ chối là Người hỗ trợ, không phải chủ hồ sơ.

Lỗi phụ QA phát hiện kèm, đã chuyển dev (giữ nguyên từ vòng trước): thư báo TỪ CHỐI lại mang tiêu đề trong thân thư là "✅ Phê duyệt: Hồ sơ bị từ chối" — có chữ "Phê duyệt" và dấu tích xanh, mâu thuẫn với chính nội dung bên dưới. Người nhận dễ hiểu nhầm là hồ sơ được duyệt.

Hồ sơ để dev/BA đối chiếu: TVV-BTP-TW-0021 (Cục Bổ trợ tư pháp, trạng thái Từ chối, đã lưu lý do).

── CÁCH VERIFY sau Dev fix ──
Precondition: trên https://18.143.165.120.nip.io — nht_qa_tw / Test@1234 (Người hỗ trợ pháp lý, Cục Bổ trợ tư pháp) và cbnv_tw / Test@1234 (Cán bộ Nghiệp vụ Trung ương, cùng đơn vị); hộp thư giả lập MailHog http://18.143.165.120:8025. Cần hồ sơ tư vấn viên do CHÍNH nht_qa_tw nộp, đang ở trạng thái cho phép thẩm định (Đang thẩm định / Chờ phê duyệt) — chưa có thì login nht_qa_tw tạo mới rồi nộp.
1) Login nht_qa_tw → mở màn Thông báo → ghi lại SỐ thông báo hiện có (mốc đối chiếu).
2) Login cbnv_tw → "Mạng lưới tư vấn viên" → "Tư vấn viên/Chuyên gia" → mở hồ sơ nói trên → tab "Thẩm định" → chọn kết luận "Không đạt", nhập lý do "Thiếu bản sao thẻ hành nghề" → bấm "Gửi KQ" → đọc NGAY thông báo hiện trên màn.
3) Login lại nht_qa_tw → mở màn Thông báo → so với mốc ở bước 1, mở thông báo mới nhất và đọc nội dung.
4) Mở MailHog → tìm thư gửi tới email của Người hỗ trợ và thư gửi tới email khai trên hồ sơ ứng viên → đọc tiêu đề trong thân thư và phần lý do.
5) Lặp bước 2 trên một hồ sơ khác với kết luận "Yêu cầu bổ sung" + lý do "Bổ sung bằng tốt nghiệp", rồi lặp bước 3 và bước 4.
✅ PASS khi ĐỦ 5 điều: (1) bước 2 màn hiện thông báo phản ánh việc hồ sơ đã bị từ chối (BA chốt "Đã từ chối hồ sơ"), KHÔNG còn là "Đã lưu kết quả thẩm định"; (2) bước 3 màn Thông báo của nht_qa_tw có ĐÚNG 1 thông báo mới so với mốc bước 1, nội dung nêu hồ sơ bị từ chối và CHỨA nguyên văn lý do "Thiếu bản sao thẻ hành nghề"; (3) bước 4 có thư gửi tới Người hỗ trợ kèm lý do, VÀ thư gửi chủ hồ sơ vẫn còn (không bị thay thế); (4) tiêu đề trong thân thư từ chối không còn chữ "Phê duyệt" và không còn dấu tích xanh; (5) bước 5 với kết luận "Yêu cầu bổ sung" cũng đạt đủ 4 điều trên, thông báo trên màn phản ánh việc đã gửi yêu cầu bổ sung đến Người hỗ trợ.
❌ FAIL nếu: màn Thông báo của Người hỗ trợ không tăng thêm bản ghi nào; có thông báo nhưng KHÔNG kèm lý do; chỉ có thư điện tử mà không có thông báo trong phần mềm (hoặc ngược lại); thư gửi chủ hồ sơ bị mất; kết luận "Yêu cầu bổ sung" không phát sinh thông báo cho Người hỗ trợ.
⚠️ Bẫy cần tránh: (a) phải dùng ĐÚNG Người hỗ trợ ĐÃ NỘP chính hồ sơ đó — Người hỗ trợ khác cùng đơn vị không nhận là đúng thiết kế, đừng tính FAIL; (b) ứng viên KHÔNG có tài khoản nên không kiểm được thông báo trong phần mềm của ứng viên, chỉ kiểm qua MailHog; (c) câu chữ không cần trùng từng ký tự hay dấu câu, nhưng phải nói rõ hồ sơ bị TỪ CHỐI — câu "Đã lưu kết quả thẩm định" là FAIL vì không phản ánh kết quả; (d) chỉ kiểm nhánh "Không đạt" mà bỏ nhánh "Yêu cầu bổ sung" là kiểm thiếu, BA chốt áp cho cả hai; (e) nếu thẻ "Thẩm định" vẫn mở được ở trạng thái "Yêu cầu bổ sung" và bấm "Gửi KQ" báo lỗi, đó là lỗi khác đã ghi ở vòng 1 — không dùng làm căn cứ kết luận dòng này.
Ảnh lỗi cũ: TDHSTVV_13_v2.webm (cột "Ảnh/video 2").
```

---

## TKDGHQHTPL_02 — tab `UAT_TGPL Doanh Nghiệp-tuần 1`, row 47

- `Trạng thái dev fix 1` = `dev done` · `Verify` = `Reject`
- `Trạng thái dev fix 2` = `dev done` · `Verify 2` = `Open`
- `Trạng thái 2` = `Fail` · `Kết quả thực tế lần 2` = 'Điểm đánh giá hiệu quả hỗ trợ pháp lý trung bình thang 0–100 nhưng số liệu trên màn hình hiển thị vượt quá 100'

### DEV phản hồi lần 2 (nguyên văn)

```text
✅ Bug đúng (BA chốt 30/07/2026). BA đã trả lời 2 điểm còn treo. Chỗ sửa nằm ở nghiệp vụ Đánh giá (cấu hình tiêu chí) — Dev KHÔNG sửa Dashboard.

Đã kiểm tra lại ngày 27/07/2026 bằng tài khoản cbnv_tw (Cán bộ NV Trung ương, đơn vị BTP · TW) trên chính môi trường đối tác, đúng bộ lọc trong ảnh (Cấp đơn vị "Trung ương" + Đơn vị "Cục Bổ trợ tư pháp - Bộ Tư pháp").

1) Phần đối tác phản ánh — con số vượt quá 100 thì KHÔNG còn tái hiện:
- Thẻ nay hiển thị 8.2/100, trục biểu đồ trần 100 (ảnh đối tác là 164.0/100, trục 172).
- Cùng bộ lọc, thẻ "Tỷ lệ tuân thủ thời hạn xử lý" bên cạnh vẫn là 17.4% đúng như ảnh đối tác, chứng minh vẫn là cùng tập dữ liệu chưa bị đụng vào — chỉ riêng con số điểm đổi.
- Hai cột biểu đồ cũng đổi theo đúng một hệ số: 172 thành 8.6 và 150 thành 7.5, đều chia đúng 20 lần. Đã quét thêm 33 tổ hợp bộ lọc khác nhau, không tổ hợp nào vượt quá 100.

2) Nhưng cùng thẻ đó vẫn còn sai, KHÔNG nên đóng:
- Trên đúng môi trường này, kết quả đánh giá cao nhất đang là 10,00 điểm và được hệ thống xếp loại "Xuất sắc" — tức đã đạt mức trần tuyệt đối. Vậy mà thẻ Dashboard vẫn gộp nó vào con số ghi "trên 100", làm một kết quả hoàn hảo trông như chỉ đạt khoảng một phần mười.
- Kiểm chứng bằng số học trên đúng dữ liệu này: 6 kết quả có điểm, tổng 49,30, chia 6 ra 8,216 — khớp con số 8.2 đang hiển thị. Các mức điểm lần lượt là 10,00 / 9,50 / 8,90 / 8,00 / 7,90 / 5,00, toàn bộ nằm trong khoảng 0 đến 10.
- Đối chiếu cách hệ thống tự xếp loại cũng cho thấy trần là 10: 5,00 xếp "Đạt" (tức 50%), 9,50 xếp "Xuất sắc" (95%), 8,90 và 7,90 xếp "Tốt" (89% và 79%). Đúng quy ước tại srs-fr-08-danh-gia.md dòng 874.
- Hệ quả nhìn thấy được: hai cột biểu đồ 8.6 và 7.5 bị vẽ dẹt sát đáy trên trục chạy tới 100, gần như không đọc được xu hướng.

3) Chỗ sửa nằm ở NGHIỆP VỤ ĐÁNH GIÁ, KHÔNG phải ở Dashboard — BA duyệt hướng này:
- Quy đổi con số trên Dashboard sang phần trăm: LOẠI. Dashboard sẽ hiện 86 trong khi màn chi tiết hiện 8,6 cho cùng một đợt (màn chi tiết hiển thị số thô — srs-fr-08-danh-gia.md dòng 873). Đây đúng là tình huống mà CHANGELOG-v3-to-v3.5.md đã chủ động sửa khi nâng v3 → v3.5.
- Giữ số thô và đổi mẫu số theo trần riêng từng kế hoạch: LOẠI. Mỗi kế hoạch một trần khác nhau thì không cộng trung bình chéo kế hoạch được, mà đó lại là việc chính của thẻ này.
- Ràng buộc cấu hình tiêu chí sao cho điểm tổng đạt trần đúng 100: CHỌN. Khi trần bằng 100 thì điểm thô, phần trăm và nhãn "/100" trùng nhau làm một, cả bốn quy định đang chọi nhau tự khớp. Củng cố: dữ liệu đời trước (kế hoạch KHDG-SEED-0001) đang mang điểm 80 / 60 / 90 — đã ở thang 0-100 từ đầu.

4) BA CHỐT 30/07/2026 — thay quyết định "Loại 1, ràng buộc điểm tổng 0-100" ở phiếu trước:
- Quy tắc mới BR-CALC-08 "Chuẩn thang điểm của một đợt đánh giá": trong mỗi kế hoạch đánh giá, tổng của (điểm tối đa của tiêu chí × trọng số tiêu chí ÷ 100) phải bằng 100. Hệ thống chặn lưu cấu hình tiêu chí vi phạm, kèm thông báo nêu rõ tổng hiện tại. BA đã thêm BR-CALC-08 vào srs-v3.5.md mục B.6 ngày 30/07/2026.
- Đổi giá trị mặc định của "Điểm tối đa" từ 10 thành 100 (srs-fr-08-danh-gia.md:1100) — với tổng trọng số bắt buộc 100%, mọi tiêu chí để mặc định là thỏa BR-CALC-08 ngay.
- Bổ sung ràng buộc tổng vào bảng trường tiêu chí (:191) và màn cấu hình tiêu chí (:850), đặt cạnh cảnh báo tổng trọng số đã có.
- Lỗ hổng ở mục 5 dưới đây được BR-CALC-08 bịt luôn, không cần quy tắc riêng.
- KHÔNG đụng gì ở Dashboard: srs-fr-01-dashboard.md:416, :450, :823 giữ nguyên.
- Dữ liệu đã chấm: KHÔNG quy đổi. Toàn bộ dữ liệu hiện có là dữ liệu thử nghiệm — cấu hình lại kế hoạch và chấm lại. (Điều kiện kèm: nếu tới lúc vận hành thật đã có đợt chấm xong trên thang cũ thì quy đổi theo trần của chính đợt đó — điểm mới = điểm cũ × 100 ÷ trần cũ — giữ nguyên xếp loại đã công bố và ghi việc quy đổi vào nhật ký của đợt; thuộc hạng mục di trú dữ liệu INS-06.)
- Một lập luận của QA bị BA bác, ghi lại để khỏi dùng lại: thẻ "Chất lượng đào tạo, bồi dưỡng pháp lý" hiển thị 7.3/10 KHÔNG phải bằng chứng tự tố cáo — thẻ đó đo điểm kiểm tra học viên, FR-III-05 quy định thang 0-10 là cố ý và đúng. Kết luận vẫn giữ nhờ các căn cứ còn lại.
- Ghi chú: srs-fr-01-dashboard.md dòng 410 vẫn ghi FR-I-08 có "công thức tính chờ CĐT review". Quyết định trên là quyết định của BA về ràng buộc dữ liệu, KHÔNG thay thế lần review công thức của CĐT — đề nghị gộp vào lần trình CĐT gần nhất.
Mức Major.

5) Lỗ hổng độc lập phát hiện kèm: điểm tối đa để tự do ("lớn hơn 0, số nguyên dương" — dòng 191) trong khi điểm tổng bị chặn trong khoảng 0 đến 100 (dòng 1049). Nếu cấu hình điểm tối đa 200 và chấm 150 thì điểm tổng thành 150, vi phạm chính ràng buộc đó. Đã dựng thử một kế hoạch điểm tối đa 200 trên môi trường được giao và hệ thống chấp nhận.

Phạm vi để đội phát triển không sửa nhầm: phần tính điểm và xếp loại đang chạy ĐÚNG đặc tả của nó. Thẻ Dashboard cũng đang hiển thị đúng như đặc tả mô tả. Sai lệch nằm ở chỗ cấu hình điểm tối đa của tiêu chí không bị ràng buộc để điểm tổng đạt trần 100.

Bug ID: BUG-TKDGHQ-THANG-DIEM.

── CÁCH VERIFY sau Dev fix ──
Precondition: cbnv_tw / Test@1234 trên https://18.143.165.120.nip.io. Màn A: "Đánh giá hiệu quả" → Kế hoạch đánh giá → cấu hình tiêu chí. Màn B: "Tổng quan hệ thống" với bộ lọc Cấp đơn vị "Trung ương" + Đơn vị "Cục Bổ trợ tư pháp - Bộ Tư pháp", Năm 2026, Tháng "Tất cả".
1) Tạo 1 kế hoạch đánh giá MỚI → mở màn cấu hình tiêu chí → đọc giá trị "Điểm tối đa" mà hệ thống điền sẵn cho tiêu chí đầu tiên.
2) Cấu hình 2 tiêu chí: trọng số 50% + 50%, Điểm tối đa 10 và 10 → bấm Lưu.
3) Sửa lại: trọng số 50% + 50%, Điểm tối đa 100 và 100 → bấm Lưu.
4) Sửa lại: trọng số 50% + 50%, Điểm tối đa 200 và 200 → bấm Lưu.
5) Sửa lại: trọng số 30% + 70%, Điểm tối đa 100 và 100 → bấm Lưu.
6) Với kế hoạch đã lưu ở bước 3: chấm đạt điểm tối đa cả 2 tiêu chí cho 1 đối tượng → mở màn chi tiết kết quả, đọc "Điểm tổng" và xếp loại.
7) Mở màn B → đọc thẻ "Điểm đánh giá hiệu quả hỗ trợ pháp lý" và trục Y của biểu đồ bên dưới.
✅ PASS khi ĐỦ 5 điều: (1) bước 1 "Điểm tối đa" mặc định là 100, không phải 10; (2) bước 2 và bước 4 hệ thống CHẶN lưu, thông báo nêu rõ tổng điểm tối đa có trọng số hiện tại (20 ở bước 2, 200 ở bước 4) và yêu cầu bằng 100; (3) bước 3 và bước 5 lưu THÀNH CÔNG (cả hai đều cho tổng bằng 100); (4) bước 6 "Điểm tổng" bằng 100 và được xếp loại "Xuất sắc"; (5) bước 7 thẻ vẫn ghi thang /100, trục Y biểu đồ vẫn chạy 0-100, và không con số nào trên thẻ hay biểu đồ vượt quá 100.
❌ FAIL nếu: bước 1 mặc định vẫn là 10; bước 2 hoặc bước 4 lưu lọt; bước 3 hoặc bước 5 bị chặn nhầm; bước 6 điểm tổng ra 10 hoặc 200 thay vì 100; hoặc Dev đã sửa ở Dashboard (đổi nhãn "/100", nhân/chia con số trên thẻ, đổi trần trục Y).
⚠️ Bẫy cần tránh: (a) ràng buộc là TỔNG của (điểm tối đa × trọng số ÷ 100) bằng 100, KHÔNG phải "mỗi tiêu chí phải bằng 100" — bước 5 (30%/70%, mỗi tiêu chí 100) phải lưu được, chặn nó là FAIL; (b) KHÔNG kiểm bằng kế hoạch cũ đã cấu hình từ trước — BA chốt không quy đổi dữ liệu cũ nên kế hoạch cũ vẫn để trần 10 là đúng, bắt buộc tạo kế hoạch MỚI; (c) con số trung bình trên thẻ Dashboard sẽ trộn kế hoạch trần cũ (10) và kế hoạch mới (100) nên trông thấp — đó KHÔNG phải FAIL, tiêu chí của bước 7 chỉ là nhãn/trục/không vượt 100; (d) KHÔNG báo lỗi thẻ "Chất lượng đào tạo, bồi dưỡng pháp lý" hiển thị /10 — thẻ đó đo điểm kiểm tra học viên, thang 0-10 là cố ý đúng.
Ảnh lỗi cũ: TKDGHQHTPL_02_v2.png (cột "Ảnh/video 2").
```

---

## TKDGHQHTPL_OOS_01 — tab `UAT_TGPL Doanh Nghiệp-tuần 1`, row 276

- `Trạng thái dev fix 1` = `dev done` · `Verify` = `Pass`
- `Trạng thái dev fix 2` = `(trống)` · `Verify 2` = `Pass`
- `Trạng thái 2` = `(trống)` · `Kết quả thực tế lần 2` = (trống)

### DEV phản hồi lần 2 (nguyên văn)

```text
☑️ Dòng này đã đóng ở vòng trước — mục dưới đây bổ sung QUYẾT ĐỊNH BA 30/07/2026 để chốt căn cứ đặc tả, KHÔNG mở lại dòng.

BA chốt: Loại 2 — đặc tả FR-I-08 bị SÓT điều kiện lọc, không phải phần mềm cố ý tính mọi bản ghi. Nội dung BA đã sửa vào SRS ngày 30/07/2026:
- §Processing bước 2 (srs-fr-01-dashboard.md:441) và §Outputs so_luong_danh_gia (:452): chỉ tính KẾT QUẢ ĐÁNH GIÁ ở trạng thái "Đã đánh giá", thuộc KẾ HOẠCH ĐÁNH GIÁ không ở trạng thái "Hủy". Áp cho CẢ con số trung bình LẪN cỡ mẫu — hai chỗ phải cùng một tập bản ghi, nếu không thì chú thích "Dựa trên N đánh giá" tiếp tục nói sai.
- §Preconditions (:425): "Có dữ liệu đánh giá trong kỳ" → "Có kết quả đánh giá đã chấm trong kỳ".
- Nhãn cỡ mẫu "Dựa trên N đánh giá" sau khi lọc là đúng nghĩa, không đổi câu chữ.
- BA BÁC cách QA đề xuất (đưa FR-I-08 vào phạm vi BR-RPT-01): BR-RPT-01 (srs-v3.5.md:5625) liệt kê tập trạng thái hợp lệ là DA_DUYET / HOAN_THANH / DA_CONG_BO / CONG_KHAI / DA_CHI_TRA — KHÔNG có DA_DANH_GIA, áp máy móc thì không bản ghi nào lọt. Ngoài ra Dashboard vốn nêu tập trạng thái tại TỪNG thẻ (KPI-01 lọc MOI, KPI-03 lọc 5 trạng thái đang sống, KPI-04 lọc HOAN_THANH + DA_DANH_GIA, KPI-05 DANG_DIEN_RA, KPI-06 DA_KET_THUC, KPI-07 DANG_HOAT_DONG) — nhiều thẻ cố ý đếm bản ghi chưa ở trạng thái cuối, kéo BR-RPT-01 vào Dashboard sẽ đá nhau với KPI-01 và KPI-03. BR-RPT-01 GIỮ NGUYÊN phạm vi FR-IX-01..23.
- Ghi chú: srs-fr-01-dashboard.md:410 vẫn ghi FR-I-08 có "công thức tính chờ CĐT review". Quyết định trên là quyết định của BA về điều kiện lọc, KHÔNG thay thế lần review công thức của CĐT.

Vì sao KHÔNG mở lại dòng: hành vi lọc đã đúng từ 27/07/2026 và đã được kiểm với ĐÚNG điều kiện tái hiện — dữ liệu gây lỗi vẫn còn nguyên trên môi trường khi đo (xem cột "DEV phản hồi lần 1"). Quyết định BA ở trên chỉ bổ sung CĂN CỨ ĐẶC TẢ cho hành vi đó, không phát sinh việc mới cho Dev. Dev chỉ cần bảo đảm không hồi quy khi sửa các dòng Dashboard khác.

KIỂM LẠI 30/07/2026 (sau khi BA chốt) — vẫn ĐẠT, kiểm bằng cbnv_tw trên môi trường được giao, màn "Tổng quan hệ thống", Năm 2026 / Tháng "Cả năm":
- Hai điều kiện tái hiện VẪN CÒN NGUYÊN trên môi trường, nên phép đo có giá trị kết luận: (a) 3 kết quả còn ở trạng thái "Chưa đánh giá" nhưng đã có điểm 80,00 / 60,00 / 90,00 (kế hoạch KHDG-SEED-0001); (b) kế hoạch DG-20260727-0001 ở trạng thái "Hủy" có kết quả đã chấm 100,00 điểm (thêm một kế hoạch Hủy nữa là DG-20260724-0001, không có kết quả).
- Đếm thực tế: 16 kết quả đánh giá, trong đó 11 kết quả "Đã đánh giá"; trừ 1 kết quả thuộc kế hoạch đã hủy còn 10 kết quả hợp lệ, tổng điểm 82,40.
- Số kỳ vọng tính tay: cỡ mẫu 10, trung bình 82,40 ÷ 10 = 8,24 → 8.2.
- Thẻ "Điểm đánh giá hiệu quả hỗ trợ pháp lý" hiển thị đúng 8.2/100 kèm "Dựa trên 10 đánh giá" — khớp cả cỡ mẫu lẫn giá trị trung bình. Biểu đồ chỉ còn cột 07/2026 = 8.2; ba cột cao nhất trước đây (02/2026 = 90.0, 04/2026 = 80.0, 05/2026 = 60.0) sinh từ ba bản ghi chưa chấm đã không còn.
- Đối chứng quyết định: nếu hệ thống KHÔNG lọc thì với đúng dữ liệu hiện tại phải ra cỡ mẫu 14 và trung bình 412,40 ÷ 14 = 29,46 → 29.5 — đúng bằng con số lỗi đã log ban đầu. Thẻ ra 10 và 8.2 chứng minh bộ lọc đang hoạt động, không phải do dữ liệu bẫy biến mất.

── CÁCH VERIFY (dùng khi Dev đụng lại Dashboard / nghi hồi quy) ──
Precondition: cbnv_tw / Test@1234 trên https://18.143.165.120.nip.io. BẮT BUỘC xác nhận trước 2 điều kiện tái hiện — thiếu 1 trong 2 thì mọi kết quả đo đều KHÔNG có giá trị kết luận:
 (a) trong kỳ đang xem có ít nhất 1 kết quả đánh giá còn ở trạng thái "Chưa đánh giá" nhưng ĐÃ có điểm tổng;
 (b) trong kỳ đang xem có ít nhất 1 kế hoạch đánh giá ở trạng thái "Hủy" mà kết quả của nó ĐÃ có điểm.
Thiếu thì tự dựng: tạo kế hoạch đánh giá, chấm điểm cho đối tượng rồi để nguyên kết quả ở "Chưa đánh giá" (điều kiện a); tạo kế hoạch khác, chấm điểm xong chuyển kế hoạch sang "Hủy" (điều kiện b).
1) Mở "Đánh giá hiệu quả" → danh sách kế hoạch và kết quả đánh giá → đếm chính xác 3 con số và ghi lại điểm của từng bản ghi: số kết quả "Đã đánh giá"; số kết quả "Chưa đánh giá" nhưng đã có điểm; số kết quả thuộc kế hoạch đang ở trạng thái "Hủy".
2) Tính tay số kỳ vọng: N_kỳ_vọng = (số kết quả "Đã đánh giá") trừ (số kết quả "Đã đánh giá" thuộc kế hoạch "Hủy"). TB_kỳ_vọng = tổng điểm của đúng N_kỳ_vọng bản ghi đó chia N_kỳ_vọng.
3) Mở "Tổng quan hệ thống", bộ lọc Cấp đơn vị "Trung ương" + Đơn vị "Cục Bổ trợ tư pháp - Bộ Tư pháp", Năm 2026, Tháng "Tất cả" → cuộn tới thẻ "Điểm đánh giá hiệu quả hỗ trợ pháp lý" → đọc con số điểm và dòng chú thích "Dựa trên N đánh giá".
4) Đọc giá trị từng cột trên biểu đồ bên dưới, đối chiếu riêng tháng chứa kế hoạch "Hủy" và tháng chứa bản ghi "Chưa đánh giá".
✅ PASS khi ĐỦ 3 điều: (1) N trên thẻ đúng bằng N_kỳ_vọng ở bước 2; (2) con số điểm trên thẻ đúng bằng TB_kỳ_vọng (làm tròn 1 chữ số thập phân); (3) cột của tháng có kế hoạch "Hủy" và cột của tháng có bản ghi "Chưa đánh giá" không bị các bản ghi đó đội lên — bằng trung bình của riêng các kết quả "Đã đánh giá" còn hiệu lực trong tháng đó, hoặc rỗng nếu tháng đó không còn bản ghi hợp lệ nào.
❌ FAIL nếu: N trên thẻ lớn hơn N_kỳ_vọng; con số điểm lệch khỏi TB_kỳ_vọng; cột biểu đồ của tháng có kế hoạch "Hủy" vẫn mang điểm của kế hoạch đó.
⚠️ Bẫy cần tránh: (a) mở Dashboard thấy con số "trông hợp lý" KHÔNG phải bằng chứng đã đúng — bắt buộc xác nhận 2 điều kiện tái hiện ở Precondition trước, môi trường không có dữ liệu bẫy thì mọi lần đo đều Pass giả; (b) môi trường đối tác htpldn-uat.ospgroup.vn tại 27/07 KHÔNG thỏa 2 điều kiện đó — đo ở đấy mà không kiểm trước là kiểm sai; (c) cỡ mẫu và giá trị trung bình phải cùng một tập bản ghi, N đúng nhưng trung bình lệch (hoặc ngược lại) vẫn là FAIL; (d) việc thẻ trộn nhiều thang điểm khác nhau là vấn đề KHÁC, đã nằm ở dòng TKDGHQHTPL_02 — không dùng làm căn cứ FAIL cho dòng này.
Ảnh: TKDGHQHTPL_02-r3-nipio-diem-29.5-tren-100.png (cột "Ảnh/vieo 1" — trạng thái TRƯỚC khi sửa) · TKDGHQHTPL_OOS_01-r4-nipio-30-07-diem-8.2-tren-10-danh-gia.png (bản đo lại 30/07/2026).
```

---
