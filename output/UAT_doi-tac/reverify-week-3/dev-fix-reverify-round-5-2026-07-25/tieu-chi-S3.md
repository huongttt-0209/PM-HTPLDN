# S3 — Tư vấn chuyên sâu · Tư liệu PL · Vụ việc · Doanh nghiệp · Địa phương Hà Nội

- **Tài khoản của session:** cbnv_tw_02 / Test@1234 · cbnv_hn / Test@1234 · cbpd_tw_01 / Test@1234 · qa_tvvseed28 / Test@1234
- **Số case:** 9 — rows [286, 290, 296, 308, 289, 307, 11, 70, 293]
- **Mức seed:** NẶNG — cần 3 hồ sơ chuyên gia, tư liệu Nháp có tệp, TVCS ở ĐANG_TƯ_VẤN, vụ việc Đang xử lý đã phân công, đợt chấm điểm cho cbnv_hn.

> **Nguồn tiêu chí:** khối `── CÁCH VERIFY ──` gốc do BA/dev viết, khôi phục từ giá trị `old=` trong `output/UAT_doi-tac/tools/sheet_verify_write.log`. Ô R trên sheet đã bị chế độ `--reopen` ghi đè sáng 25/07 nên KHÔNG còn tiêu chí. **Chấm PASS/FAIL đúng theo khối này, không tự nghĩ tiêu chí.**

> Bản snapshot nguyên văn P/Q/R trước round 5: `snapshot-P-Q-R-truoc-round5.md` cùng thư mục.


---

# Row 286 — QLNDTVVCG_22

## TIÊU CHÍ GỐC — bắt buộc chấm theo

✅ Bug đúng MỘT PHẦN (BA 24/07/2026) — Loại 2, SRS đã được bổ sung, Dev làm theo SRS mới.
- Ý 1 (ô "Chuyên môn" trống) = PHẢI SỬA. Đặc tả nay đã ĐỊNH NGHĨA RÕ nguồn dữ liệu: ô "Chuyên môn" (hiển thị khi chọn Chuyên gia ở khối Thông tin cơ bản và trong modal Phân công CG) lấy từ hồ sơ Chuyên gia (FR-04) theo quy tắc — ưu tiên chuyen_nganh; nếu chuyen_nganh trống thì ghép tên các lĩnh vực từ linh_vuc_ids; nếu cả hai trống thì hiển thị "Chưa cập nhật" (srs-fr-12-tv-chuyen-sau.md:1168, đặc tả có gắn mã [QLNDTVVCG_22]). Hiện app map thẳng vào chuyen_nganh nên hiện "—" dù chuyên gia đã có lĩnh vực. Dev BE/FE áp đúng quy tắc trên, KHÔNG tự chọn nguồn dữ liệu khác. Song song, chủ dữ liệu hồ sơ Chuyên gia bảo đảm có nhập chuyên ngành/lĩnh vực. Mức Minor.
- Ý 2 (chú thích "Chuyên gia sẽ được gửi thông báo…") = KHÔNG PHẢI LỖI. Modal đã có dòng thông tin thời hạn xử lý "2 ngày làm việc để xác nhận", đáp ứng yêu cầu đặc tả (dòng 1167); câu chú thích thêm về việc gửi thông báo là cải tiến tùy chọn, đặc tả không quy định — Dev KHÔNG cần thêm.

── CÁCH VERIFY sau Dev fix ──
Precondition: cbnv_tw (CB Nghiệp vụ TW) + 1 bản ghi TVCS ở trạng thái "Tiếp nhận". Cần 3 hồ sơ chuyên gia làm dữ liệu thử, cùng lĩnh vực với bản ghi: (A) có nhập chuyên ngành; (B) trống chuyên ngành nhưng có ≥1 lĩnh vực; (C) trống cả chuyên ngành lẫn lĩnh vực.
1) Mở Chi tiết bản ghi "Tiếp nhận" → bấm [Phân công CG] → modal mở.
2) Chọn lần lượt chuyên gia A, B, C → mỗi lần đọc giá trị ô "Chuyên môn" trong bảng thông tin chi tiết của chuyên gia.
3) Đóng modal → tại khối "Thông tin cơ bản" chọn chuyên gia B ở dropdown Chuyên gia → đọc ô "Chuyên môn".
✅ PASS khi: A hiện đúng chuyên ngành đã nhập; B hiện tên (các) lĩnh vực của chuyên gia đó thay vì để trống; C hiện đúng chữ "Chưa cập nhật"; và ô "Chuyên môn" ở khối Thông tin cơ bản (bước 3) cho ra cùng kết quả với modal.
❌ FAIL nếu: trường hợp B vẫn hiện "—"/để trống; C hiện "—" thay vì "Chưa cập nhật"; hoặc modal và khối Thông tin cơ bản hiển thị khác nhau cho cùng một chuyên gia.
⚠️ Nhãn của dropdown chọn chuyên gia vốn đã kèm sẵn tên lĩnh vực — KHÔNG được lấy nhãn dropdown thay cho ô "Chuyên môn"; phải đọc đúng ô "Chuyên môn" trong bảng thông tin chi tiết, nếu không sẽ PASS oan.
⚠️ KHÔNG đánh FAIL vì thiếu câu "Chuyên gia sẽ được gửi thông báo…" (ý 2 — BA chốt không phải lỗi).

## Triệu chứng QA ghi nhận lượt trước (sáng 25/07) — CHỈ tham khảo, không phải tiêu chí

- Cửa sổ "Phân công chuyên gia": ô "Chuyên môn" đã hiển thị đúng tên lĩnh vực của chuyên gia khi chuyên gia chưa nhập chuyên ngành — phần này đã đạt.
- Vẫn còn lỗi ở khối "Thông tin cơ bản" của màn Thêm yêu cầu tư vấn: chọn đúng chuyên gia đó thì ô "Chuyên môn" vẫn hiển thị dấu "—", trong khi cửa sổ Phân công của cùng chuyên gia hiển thị "Thương mại". Hai nơi cho kết quả khác nhau với cùng một chuyên gia.
- Màn Sửa yêu cầu tư vấn: sau khi chọn chuyên gia, hệ thống không hiển thị ô "Chuyên môn" (cũng không có số điện thoại, email) như màn Thêm mới.
- Chưa kiểm được trường hợp chuyên gia trống cả chuyên ngành lẫn lĩnh vực (kỳ vọng hiển thị "Chưa cập nhật") vì hệ thống bắt buộc chọn ít nhất 1 lĩnh vực khi tạo/sửa hồ sơ chuyên gia.


---

# Row 290 — QLNDTVVCG_40

## TIÊU CHÍ GỐC — bắt buộc chấm theo

✅ Bug đúng (BA 24/07/2026). Loại 2 — SRS đã được bổ sung, Dev làm theo SRS mới. Dev BE/FE: sửa chức năng Xuất Excel của danh sách TVCS cho khớp Processing "Xuất Excel danh sách TVCS" vừa bổ sung vào đặc tả — srs-fr-12-tv-chuyen-sau.md:155-164 (bước 4 dòng 162: tên tệp có giờ-phút + tập cột bám cột đang hiển thị; bước 5 dòng 163: cột "Nội dung tư vấn (đầy đủ)" chỉ khi người dùng chọn xuất đầy đủ; bước 2 dòng 160: xuất theo đúng bộ lọc hiện hành). Nút [Xuất Excel] của màn danh sách ở dòng 1104. Hiện app đặt tên tệp thiếu giờ-phút và tập cột lệch (thiếu Doanh nghiệp / Chuyên gia / Lĩnh vực / Tiêu đề, thừa Nội dung + Điểm đánh giá). Mức Minor.

── CÁCH VERIFY sau Dev fix ──
Precondition: cbnv_tw (CB Nghiệp vụ TW), mở màn "Quản lý Tư vấn pháp luật chuyên sâu"; danh sách phải có ≥3 bản ghi thuộc ≥2 lĩnh vực khác nhau.
1) Không đặt bộ lọc → bấm [Xuất Excel] → ghi lại TÊN TỆP tải về.
2) Mở tệp .xlsx, đọc dòng tiêu đề → liệt kê đủ tên cột theo thứ tự.
3) Đếm số dòng dữ liệu trong tệp, đối chiếu số bản ghi đang hiển thị trên lưới.
4) Đặt bộ lọc Trạng thái = "Đang tư vấn" (hoặc 1 lĩnh vực cụ thể) → bấm [Xuất Excel] lần 2 → mở tệp, đếm dòng.
✅ PASS khi: (a) tên tệp có cả ngày VÀ giờ-phút, đủ để 2 lần xuất trong cùng một ngày ra 2 tên khác nhau; (b) tệp có đủ các cột đang hiển thị trên lưới — Mã tư vấn, Doanh nghiệp, Chuyên gia, Lĩnh vực, Tiêu đề, Trạng thái, Ngày bắt đầu, Ngày tạo; (c) KHÔNG tự động kèm cột "Nội dung tư vấn (đầy đủ)" khi người dùng không chọn xuất đầy đủ; (d) tệp lần 2 chỉ chứa đúng các dòng khớp bộ lọc và ít hơn lần 1.
❌ FAIL nếu: 2 lần xuất cùng ngày cho ra trùng tên tệp; thiếu bất kỳ cột nào ở (b); vẫn kèm sẵn cột nội dung đầy đủ; hoặc tệp lần 2 vẫn ra toàn bộ bản ghi (bỏ qua bộ lọc).
⚠️ Cột "Ngày hoàn thành" chỉ bắt buộc khi cột đó ĐANG hiển thị trên lưới (SRS dòng 162) — lưới không có cột này thì tệp thiếu nó KHÔNG tính FAIL.

## Triệu chứng QA ghi nhận lượt trước (sáng 25/07) — CHỈ tham khảo, không phải tiêu chí

- Tệp xuất ra vẫn luôn kèm sẵn cột "Nội dung tư vấn (đầy đủ)" với toàn bộ nội dung tư vấn; màn danh sách không có tùy chọn nào để người dùng chọn có xuất đầy đủ hay không.
- Tên tệp tải về dạng "tv-chuyen-sau-1784921668017.xlsx": phần đuôi là một dãy số máy sinh, người dùng không đọc được ngày và giờ-phút xuất tệp.
- Cột "Ngày tạo" trong tệp lệch 1 ngày so với màn danh sách: bản ghi hiển thị "25/07/2026 02:33" trên lưới nhưng trong tệp ghi "24/7/2026".
- Các điểm đã đạt: tệp có đủ các cột Mã tư vấn, Doanh nghiệp, Chuyên gia, Lĩnh vực, Tiêu đề, Trạng thái, Ngày bắt đầu, Ngày tạo; số dòng khớp lưới; xuất theo bộ lọc lĩnh vực cho đúng 1 dòng.


---

# Row 296 — QLTLPLCVV_07

## TIÊU CHÍ GỐC — bắt buộc chấm theo

✅ Bug đúng (BA 24/07/2026). Loại 1 — Dev sửa theo SRS; BA khuyến nghị GIỮ nguyên quy định hiện hành, không mở ngoại lệ. Đặc tả khóa sửa toàn bộ khi tư liệu đang công khai: Processing "Chỉnh sửa tư liệu" bước 3 — "Kiểm tra trạng thái: nếu CONG_KHAI → từ chối sửa (phải hủy công khai trước)" (srs-fr-12-tv-chuyen-sau.md:902) — KHÔNG có ngoại lệ cho mô tả hay tệp đính kèm. Hiện app vẫn hiện nút [Sửa] trên tư liệu "Đã công khai" và cho cập nhật thật mô tả + tệp đính kèm. Dev BE: từ chối yêu cầu cập nhật tư liệu đang ở trạng thái công khai kể cả khi chỉ đổi mô tả/tệp, phản hồi nêu rõ phải hủy công khai trước. Dev FE: khóa hoặc ẩn nút [Sửa] trên dòng tư liệu "Đã công khai". Lưu ý mã lỗi ERR-STATE-X1-06-01 mà app đang dùng KHÔNG có trong bảng Xử lý lỗi của đặc tả (dòng 962-971 chỉ tới ERR-TLPL-05 và WRN-TLPL-01) — Dev không tự đặt mã ngoài đặc tả. Mức Major (nội dung đã công khai bị sửa ngầm).

── CÁCH VERIFY sau Dev fix ──
Precondition: cbnv_tw (CB Nghiệp vụ TW). Trong nhóm "Tư liệu PL liên kết" của một TVCS, cần 2 tư liệu: T1 ở trạng thái "Đã công khai" (có ≥1 tệp đính kèm) và T2 ở trạng thái "Nháp".
1) Xem dòng T1 → kiểm tra nút [Sửa] có hiện / có bấm được không.
2) Nếu vẫn vào được form sửa T1: đổi RIÊNG ô Mô tả rồi lưu → đọc phản hồi hệ thống; đóng form, mở lại T1 và đọc lại Mô tả.
3) Trên T1, thử thêm hoặc gỡ một tệp đính kèm rồi lưu → đóng form, mở lại T1 và đếm số tệp.
4) Hủy công khai T1 (đưa về "Nháp") → sửa Mô tả → lưu.
5) Trên T2 ("Nháp") → sửa Mô tả → lưu.
✅ PASS khi: bước 1 nút [Sửa] của T1 bị ẩn hoặc vô hiệu; nếu vẫn vào được form thì bước 2 và 3 đều bị hệ thống từ chối kèm thông báo nêu rõ phải hủy công khai trước, VÀ mở lại T1 thấy Mô tả cùng số tệp KHÔNG đổi so với trước; bước 4 và 5 sửa được bình thường.
❌ FAIL nếu: mở lại T1 thấy Mô tả hoặc số tệp đã thay đổi; hoặc bước 4/5 bị chặn (chặn nhầm cả tư liệu Nháp và tư liệu đã hủy công khai).
⚠️ Chỉ nhìn thông báo lỗi trên giao diện là CHƯA đủ để kết luận PASS — bắt buộc đóng form, mở lại tư liệu và đối chiếu giá trị Mô tả + số tệp trước/sau. Lỗi cũ đúng ở dạng giao diện báo lỗi nhưng dữ liệu phía sau vẫn bị ghi đè.
Ảnh lỗi cũ (nút Sửa trên tư liệu Đã công khai): partner-evidence/QLTLPLCVV_07.jpg

## Triệu chứng QA ghi nhận lượt trước (sáng 25/07) — CHỈ tham khảo, không phải tiêu chí

- Phần đã đạt: tư liệu đang ở trạng thái "Đã công khai" không còn hiển thị nút [Sửa] (chỉ còn Xem tệp / Hủy công khai / Xóa), không vào được biểu mẫu sửa.
- Còn lỗi: hủy công khai tư liệu đó (về "Nháp") rồi sửa ô "Mô tả" và bấm [Lưu] → hệ thống báo "Một hoặc nhiều file đã được gắn vào bản ghi khác" và KHÔNG lưu được.
- Làm tương tự trên một tư liệu vốn ở trạng thái "Nháp" (chưa từng công khai) → cũng báo đúng thông báo trên, không lưu được.
- Tạo mới một tư liệu khác có đính kèm 1 tệp rồi sửa mô tả → vẫn gặp lỗi giống hệt.
- Thử gỡ tệp đính kèm ra khỏi tư liệu rồi bấm [Lưu] → lưu thành công. Như vậy chỉ cần tư liệu còn giữ tệp đính kèm sẵn có thì không sửa được bất kỳ thông tin nào.
- Sau khi báo lỗi, nội dung vừa nhập ở ô "Mô tả" bị xóa trắng, người dùng phải nhập lại từ đầu.
- Đề nghị: tư liệu ở trạng thái "Nháp" (kể cả tư liệu vừa hủy công khai) phải sửa và lưu được bình thường trong khi vẫn giữ nguyên tệp đính kèm sẵn có.


---

# Row 308 — QLTLPLCVV_OOS_01

## TIÊU CHÍ GỐC — bắt buộc chấm theo

[Dev báo] Sửa tư liệu giờ lưu OK. Nhưng gỡ tệp trong form Sửa thì tệp vẫn còn — update mới chỉ re-link, chưa có logic UNLINK.
[BA chốt 24/07/2026] Phải thêm xóa thật: gỡ tệp → xóa file khỏi storage + gỡ liên kết FILE_DINH_KEM; mở lại tư liệu không còn tệp, cột "File" giảm. Nếu CÔNG_KHAI + hết tệp → cảnh báo CB NV. Căn cứ: srs-fr-12-tv-chuyen-sau.md:918-927 [GAP-X.1-02]. (Mã BA QLTLPLCVV_005_01 ↔ mã sheet QLTLPLCVV_OOS_01.)
── CÁCH VERIFY ──
Precondition: env https://18.143.165.120.nip.io; có tư liệu "Nháp" với ≥1 tệp đính kèm.
1) Regression save: mở tư liệu Nháp còn tệp → sửa Mô tả → Lưu → lưu thành công, giữ nguyên tệp (không còn báo "file đã gắn vào bản ghi khác").
2) Unlink: trong form Sửa gỡ 1 tệp → Lưu → mở lại tư liệu: tệp đó KHÔNG còn, cột "File" giảm 1.
✅ PASS: lưu-giữ-tệp OK + gỡ tệp thì tệp biến mất thật (khỏi storage + FILE_DINH_KEM).
❌ FAIL: gỡ tệp nhưng mở lại tệp vẫn còn / cột File không giảm; HOẶC còn báo "file đã gắn vào bản ghi khác" khi lưu.



---

# Row 289 — QLNDTVVCG_36

## TIÊU CHÍ GỐC — bắt buộc chấm theo

⚠️ Hành vi hủy hiện tại ĐÚNG ĐẶC TẢ — KHÔNG phải bug. Chỉ còn 1 việc dọn dẹp (BA chốt 24/07/2026).

THEO SRS (srs-fr-12-tv-chuyen-sau.md:238-244, Processing "Hủy yêu cầu"):
- Ở trạng thái ĐANG_TƯ_VẤN, CHỈ Cán bộ Phê duyệt được hủy; CB Nghiệp vụ / Chuyên gia bị chặn (:238, tag [QLNDTVVCG_36 chốt 2026-07-24]).
- Hủy chuyển TRỰC TIẾP ĐANG_TƯ_VẤN → HỦY, KHÔNG tạo trạng thái trung gian "chờ duyệt hủy" (:241).
- "Từ chối duyệt hủy" = Cán bộ Phê duyệt KHÔNG thực hiện hủy → bản ghi giữ nguyên ĐANG_TƯ_VẤN. Không cần màn duyệt hủy riêng trong app.
- Yêu cầu hủy của DN là văn bản/email NGOÀI hệ thống; hệ thống KHÔNG lưu thành cột riêng trên entity (:244).

→ Vì vậy: Kết quả thực tế (Cán bộ Phê duyệt hủy thẳng sang "Đã hủy") là ĐÚNG SRS. Kết quả mong đợi của đối tác (đòi trạng thái trung gian "chờ duyệt hủy" + luồng duyệt hủy trong app) TRÁI SRS → KHÔNG dựng thêm luồng này.

VIỆC DEV CÒN LẠI (cleanup — BA chốt 24/07/2026): gỡ phần dư đã lỡ xây cho cơ chế "DN gửi / duyệt yêu cầu hủy trong app" — theo BA là 3 cột lưu yêu-cầu-hủy + 2 endpoint (gửi / duyệt yêu cầu hủy). Căn cứ: SRS :244 nói yêu cầu hủy của DN nằm NGOÀI hệ thống, không lưu cột riêng. (Số cột/endpoint theo BA liệt kê; QA chưa mở được mã nguồn để đếm độc lập — dev đối chiếu khi gỡ.)

── CÁCH VERIFY sau khi Dev cleanup ──
Precondition: env https://18.143.165.120.nip.io; có TVCS ở trạng thái ĐANG_TƯ_VẤN.
1) Login Cán bộ Phê duyệt: mở bản ghi ĐANG_TƯ_VẤN → [Hủy yêu cầu] → nhập lý do → xác nhận → bản ghi chuyển THẲNG sang "Đã hủy" (không qua state trung gian).
2) Login Cán bộ Nghiệp vụ / Chuyên gia: nút [Hủy yêu cầu] phải bị ẩn/chặn ở bản ghi ĐANG_TƯ_VẤN.
3) Đối chiếu với dev: không còn 3 cột + 2 endpoint "yêu cầu duyệt hủy" trong hệ thống.
✅ PASS khi: (a) Cán bộ Phê duyệt hủy trực tiếp được; (b) CB NV/CG bị chặn ở ĐANG_TƯ_VẤN; (c) không còn cột/endpoint "yêu cầu duyệt hủy" dư.
❌ FAIL khi: vẫn còn cột/endpoint duyệt-hủy trong app, HOẶC CB NV/CG hủy được ở ĐANG_TƯ_VẤN.
⚠️ KHÔNG chấm FAIL vì thiếu màn "duyệt hủy" hay thiếu state "chờ duyệt hủy" — SRS KHÔNG yêu cầu các thành phần đó.



---

# Row 307 — QLDNDHTPL_OOS_01

## TIÊU CHÍ GỐC — bắt buộc chấm theo

[Dev báo] Đã fix double-toast (1 thao tác → 1 thông báo). Nhưng DN đơn vị khác vẫn hiện nút Sửa + mở được biểu mẫu chỉnh sửa, mới chỉ chặn ở bước Lưu.
[BA chốt 24/07/2026] Phải ẨN nút Sửa/Xóa theo quyền (không chỉ chặn ở Lưu): CB Phê duyệt R* → ẩn; CB Nghiệp vụ → chỉ hiện với DN thuộc đơn vị mình. Áp cả nút "Chỉnh sửa" ở màn chi tiết SCR-V.III-02. Backend vẫn kiểm quyền — ẩn nút chỉ là UX. Căn cứ: srs-fr-07-doanh-nghiep.md:443, :451 [QLDNDHTPL_005_01 chốt 2026-07-24]. (Mã BA/SRS QLDNDHTPL_005_01 ↔ mã sheet QLDNDHTPL_OOS_01.)
── CÁCH VERIFY ──
Precondition: env https://18.143.165.120.nip.io.
1) Login CB Phê duyệt (R*): mở danh sách DN → nút Sửa/Xóa phải ẩn ở mọi dòng; mở chi tiết 1 DN → nút "Chỉnh sửa" cũng ẩn.
2) Login CB Nghiệp vụ (TW): dòng DN thuộc đơn vị mình → có Sửa/Xóa; dòng DN đơn vị khác → ẩn Sửa/Xóa (không chỉ chặn ở Lưu).
3) Regression double-toast: gây 1 lỗi (vd sửa DN đơn vị khác rồi Lưu) → chỉ hiện 1 thông báo lỗi.
✅ PASS: nút Sửa/Xóa ẩn đúng theo quyền + double-toast không tái diễn.
❌ FAIL: DN đơn vị khác vẫn hiện Sửa/Xóa (dù đã chặn ở Lưu), HOẶC vẫn 2 khung thông báo cho 1 thao tác.



---

# Row 11 — CNKQHT_03

## TIÊU CHÍ GỐC — bắt buộc chấm theo

✅ Bug đúng (BA 24/07/2026) — gồm 2 lỗi cấu trúc (Loại 1) + 1 điểm cập nhật đặc tả (Loại 2).
- Loại 1, Dev sửa theo đặc tả: bước cập nhật kết quả hỗ trợ FR-V.I-15 chỉ có 3 ô nhập — Nội dung kết quả hỗ trợ, Tệp kết quả hỗ trợ (srs-fr-05-vu-viec.md:1095, file_ket_qua) và Ghi chú. App đang THIẾU ô đính kèm tệp kết quả (mất chứng cứ đầu vào của hồ sơ chi trả) và THỪA ô "Kết luận" vốn thuộc bước sau do CB nghiệp vụ thực hiện (:1150).
- Loại 2, BA chấp thuận đề nghị đối tác và đã cập nhật đặc tả: ô Nội dung kết quả hỗ trợ tối đa 10.000 ký tự (:1094) thay cho mốc 5.000 đang chạy — Dev nâng theo đặc tả mới. Mức Major (mất ô đính kèm) + Minor (giới hạn ký tự).

── CÁCH VERIFY sau Dev fix ──
Precondition: tài khoản người được phân công xử lý vụ việc (qa_tvvseed28 hoặc nht_qa_tw / Test@1234) hoặc cbnv_tw; cần 1 vụ việc đang ở trạng thái "Đang xử lý" (đã chấp nhận phân công). Mở Chi tiết vụ việc → phần Kết quả hỗ trợ → bấm [Cập nhật kết quả] để mở màn nhập.
1) Liệt kê các ô có trong màn nhập.
2) Dán 10.000 ký tự vào ô Nội dung kết quả hỗ trợ, xem bộ đếm; rồi thử 10.001 ký tự.
3) Đính kèm 1 tệp kết quả (pdf hoặc docx) rồi Lưu.
4) Thoát ra, mở lại vụ việc đó xem phần Kết quả hỗ trợ.
✅ PASS khi: màn nhập có ô đính kèm Tệp kết quả hỗ trợ và KHÔNG còn ô "Kết luận"; ô Nội dung nhận đủ 10.000 ký tự (bộ đếm lấy mốc 10.000) và chặn khi vượt; tệp đính kèm lưu thành công và mở lại vẫn thấy, tải về đúng tệp đã nộp.
❌ FAIL nếu: vẫn không có ô đính kèm; vẫn còn ô "Kết luận"; nội dung vẫn bị chặn ở 5.000 ký tự; hoặc đính kèm được nhưng sau khi lưu mở lại mất tệp.
⚠️ Ô "Kết luận cuối cùng" ở bước KHÁC (CB nghiệp vụ cập nhật kết quả cuối khi vụ việc Đã duyệt) là ĐÚNG đặc tả — chỉ chấm màn nhập kết quả hỗ trợ ở trạng thái Đang xử lý, đừng nhầm sang bước kia rồi báo FAIL.
Ảnh lỗi cũ: CNKQHT_03.jpg (ảnh UAT đối tác — màn "Cập nhật kết quả hỗ trợ": Nội dung 0/5000, có ô "Kết luận" thừa, không có ô đính kèm Tệp kết quả hỗ trợ).

## Triệu chứng QA ghi nhận lượt trước (sáng 25/07) — CHỈ tham khảo, không phải tiêu chí

- Ô đính kèm "Tệp kết quả hỗ trợ" đã được bổ sung, ô "Kết luận" đã gỡ khỏi cửa sổ nhập, nội dung nhận đủ 10.000 ký tự và chặn khi vượt mốc — các điểm này đã đạt.
- Còn lỗi: đăng nhập bằng tài khoản người được phân công xử lý vụ việc (tư vấn viên), chọn tệp kết quả thì hệ thống báo "Forbidden" và không đính kèm được tệp nào.
- Còn lỗi: đăng nhập bằng tài khoản cán bộ nghiệp vụ thì tệp đính kèm lên được và hiện trong cửa sổ nhập, bấm Xác nhận có thông báo "Đã cập nhật kết quả"; nhưng thoát ra mở lại vụ việc thì mục Kết quả hỗ trợ chỉ còn phần nội dung, tệp vừa đính kèm biến mất, không xem hay tải lại được.
- Kiểm thử ngày 25/07/2026 trên vụ việc VV-BTP-TW-20260712-004 đang ở trạng thái "Đang xử lý".


---

# Row 70 — THDG_03

## TIÊU CHÍ GỐC — bắt buộc chấm theo

✅ Bug đúng (BA duyệt 24/07/2026) — Loại 1: phần mềm sai SRS ở phần thông báo. Mức Minor. Owner Dev FE — máy chủ đã từ chối đúng, KHÔNG sửa logic kiểm tra phía máy chủ.
Dev FE: khi người dùng nhập điểm vượt điểm tối đa của tiêu chí, hệ thống phải cho người dùng BIẾT. Hiện giao diện lặng lẽ đổi giá trị về mức tối đa mà không nói gì (người dùng gõ 15, ô thành 10, không hiểu vì sao). Đặc tả yêu cầu từ chối giá trị vượt tối đa và báo cho người dùng với nội dung "Điểm phải từ 0 đến {max}". Dev chọn 1 trong 2 cách đều đạt: chặn không nhận giá trị vượt tối đa kèm thông báo đó, HOẶC vẫn nắn về tối đa nhưng phải kèm thông báo cho biết đã điều chỉnh về mức tối đa.
SRS đã kiểm nguyên văn: Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-08-danh-gia.md:517 — bảng xử lý lỗi của luồng chấm điểm, mục E1: 'Điểm vượt điểm tối đa | ERR-DG-DG-01 | "Điểm phải từ 0 đến {max}" | ERROR'.
Ghi chú (không tính vào case này): mã lỗi máy chủ đang trả là ERR-DG-SC-06 trong khi SRS ghi ERR-DG-DG-01 — BA xếp việc đồng bộ mã là cải tiến tùy chọn.

── CÁCH VERIFY sau Dev fix ──
Precondition: đăng nhập https://18.143.165.120.nip.io bằng cbnv_hn / Test@1234. Cần 1 đợt đang chấm điểm mà tài khoản này được phân công, có ≥1 vụ việc đã chọn và có tiêu chí Điểm tối đa = 10: /danh-gia/ke-hoach/danh-sach → chi tiết đợt → tab Chấm điểm.
1) Vào ô điểm của tiêu chí có điểm tối đa 10, xóa trắng rồi gõ 15, sau đó bấm ra ngoài ô.
2) Quan sát NGAY: có thông báo/dòng chữ báo lỗi nào hiện ra không, và giá trị còn lại trong ô là bao nhiêu.
3) Gõ tiếp -3 vào cùng ô đó rồi bấm ra ngoài, quan sát tương tự.
4) Gõ 8 (hợp lệ) vào ô đó, bấm ra ngoài → bấm Lưu kết quả.
5) Tải lại trang, mở lại tab Chấm điểm, đọc lại giá trị ô vừa lưu.
✅ PASS khi ĐỦ 4 điều: (i) bước 2 CÓ thông báo nhìn thấy được nói rõ khoảng điểm hợp lệ 0–10, hoặc nói rõ đã điều chỉnh về mức tối đa 10 — không còn im lặng; (ii) giá trị lưu được KHÔNG bao giờ vượt 10; (iii) bước 3 nhập số âm cũng được báo tương tự, không im lặng; (iv) bước 4-5 giá trị hợp lệ 8 lưu và hiển thị lại đúng 8, không có thông báo lỗi thừa.
❌ FAIL nếu: gõ 15 rồi rời ô mà KHÔNG có bất kỳ thông báo nào (dù giá trị đã bị nắn về 10); HOẶC có thông báo nhưng vẫn cho lưu điểm 15; HOẶC nhập giá trị hợp lệ vẫn bị báo lỗi.
⚠️ Máy chủ vốn đã từ chối điểm vượt tối đa — nếu chỉ sửa phía máy chủ mà giao diện vẫn im lặng thì case này VẪN FAIL, vì phần còn thiếu đúng là phần người dùng nhìn thấy.
⚠️ Điểm tối đa lấy theo TỪNG tiêu chí, không cố định 10 — tiêu chí có điểm tối đa khác (vd 20) thì thông báo phải nêu đúng con số của tiêu chí đó.

## Triệu chứng QA ghi nhận lượt trước (sáng 25/07) — CHỈ tham khảo, không phải tiêu chí

- Nhập điểm vượt điểm tối đa (gõ 15 vào tiêu chí có điểm tối đa 10): hệ thống đã hiện dòng chữ "Điểm phải từ 0 đến 10" ngay dưới ô và chặn không cho lưu — phần này đã đạt.
- Nhập điểm âm (gõ -3 vào cùng ô đó rồi bấm ra ngoài): ô lặng lẽ tự đổi về 0, không hiện bất kỳ thông báo hay dòng chữ báo lỗi nào, ô cũng không được tô đỏ. Người dùng không biết giá trị vừa nhập đã bị hệ thống thay đổi.
- Điểm hợp lệ (nhập 8) vẫn lưu và hiển thị lại đúng, không có thông báo lỗi thừa.
- Đề nghị: trường hợp nhập dưới 0 cần được báo cho người dùng biết giống như trường hợp vượt điểm tối đa.


---

# Row 293 — QLHSPLDN_03

## TIÊU CHÍ GỐC — bắt buộc chấm theo

✅ Bug đúng (BA duyệt 24/07/2026) — case này gồm 4 ý, cả 4 ý đều là lỗi phần mềm (Loại 1: SRS đã đúng và đủ, web lệch) nên verdict Open. Căn cứ trích từ SRS v3.5 hiện hành: Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-12-tv-chuyen-sau.md, FR-X.1-04 (UC150) §Inputs Thêm mới / Chỉnh sửa (bảng :564–:574, đúng 11 trường).

Ý 1 — BỎ trường "Số/Ký hiệu" khỏi biểu mẫu Thêm/Sửa. §Inputs 11 trường (:564–:574) không có trường này, entity HO_SO_PHAP_LY_DN 19 trường (:1399–:1417) cũng không có; tìm so_hieu/so_ky_hieu trên toàn thư mục SRS v3.5 = 0 kết quả. Người dùng nhập vào thì dữ liệu không có chỗ lưu. Yêu cầu: biểu mẫu không còn ô này (BA lưu ý: nếu sau này nghiệp vụ cần lưu số/ký hiệu văn bản thì mở yêu cầu cải tiến để bổ sung vào entity + §Inputs + §Outputs, không tự thêm ở tầng giao diện). Mức Minor.

Ý 2 — Ô văn bản dài phải mang nhãn "Mô tả", hiện đang mang nhãn "Ghi chú". §Inputs chỉ có ĐÚNG MỘT ô văn bản dài không bắt buộc, tên mo_ta — :572 nguyên văn "| 9 | mo_ta | text (long) | N | — | — | người dùng nhập |" (entity :1408 mô tả "Mô tả"). Yêu cầu: biểu mẫu có đúng một ô văn bản dài mang nhãn "Mô tả" — sửa nhãn, KHÔNG thêm ô mới để tránh sinh hai ô trùng chức năng. Mức Minor/Cosmetic.

Ý 3 — THÊM ô chọn "Lĩnh vực pháp lý" vào biểu mẫu Thêm/Sửa. §Inputs đã có sẵn :568 nguyên văn "| 5 | linh_vuc_id | identifier | N | FK -> DANH_MUC | — | người dùng chọn |" (entity :1404 "Lĩnh vực PL"). Yêu cầu: biểu mẫu cho người dùng chọn lĩnh vực pháp lý từ danh mục, không bắt buộc, giá trị chọn phải lưu lại được. Không cần sửa SRS. Mức Major.

Ý 4 — THÊM ô "Tệp đính kèm" vào biểu mẫu Thêm/Sửa. §Inputs đã có sẵn :574 nguyên văn "| 11 | file_dinh_kem | file | N | PDF/image, max 20MB | — | người dùng upload |"; §Processing Thêm mới bước 5 :604 "Upload file nếu có (max 20MB, quét virus) | EC-FILE-01". Yêu cầu: biểu mẫu cho đính kèm tệp PDF/ảnh không quá 20MB, tệp phải được lưu kèm hồ sơ; vượt dung lượng hoặc nhiễm mã độc thì từ chối kèm thông báo (SRS §Error Handling :684 ERR-HSPL-03, :685 ERR-HSPL-04). Không cần sửa SRS. Mức Major.

Phân biệt với QLHSPLDN_02 ý 2: ở case NÀY "Lĩnh vực pháp lý" là Ô NHẬP trên biểu mẫu (§Inputs đã có sẵn nên thuần Dev bổ sung); ở QLHSPLDN_02 là CỘT trên bảng danh sách. Hai chỗ khác nhau, phải làm và kiểm riêng.

Hiện trạng đã được ghi nhận 21/07/2026 (nguồn: output/UAT_doi-tac/reverify-week-3/bug-reports/qlhspldn/Pass-bug-report-qlhspldn.md:96 — đọc label biểu mẫu qua DOM): biểu mẫu có 8 ô "Tên hồ sơ · Loại hồ sơ · Số/Ký hiệu · Ngày cấp · Ngày hết hạn · Cơ quan cấp · Trạng thái · Ghi chú", không tìm thấy control upload nào. Bug ID: BUG-QLHSPLDN_03. Ô "Trạng thái dev fix 1" đang là "dev done" nên giữ nguyên; người re-verify chạy lại các bước dưới trên bản mới nhất để chốt.

── CÁCH VERIFY sau Dev fix ──
Precondition: tài khoản cbnv_hn / Test@1234 (CB Nghiệp vụ Địa phương — Sở Tư pháp Hà Nội), mã OTP lấy tại MailHog http://18.143.165.120:8025. Môi trường https://18.143.165.120.nip.io. Màn hình: menu Doanh nghiệp → DN-HNI-0001 (mã số thuế 0109998887) → Xem chi tiết → thẻ "Hồ sơ pháp lý" → nút [+ Thêm hồ sơ]. Chuẩn bị sẵn 1 tệp PDF sạch dung lượng dưới 20MB trên máy để thử đính kèm.
1) Đăng nhập cbnv_hn, mở thẻ "Hồ sơ pháp lý" của DN-HNI-0001, bấm [+ Thêm hồ sơ].
2) Kéo hết biểu mẫu từ trên xuống đáy, đọc nhãn TẤT CẢ các ô (đọc label qua DOM cho chắc, vì biểu mẫu dạng panel có thể cuộn).
3) Mở ô chọn "Lĩnh vực pháp lý", xem danh sách lĩnh vực có giá trị để chọn không, rồi chọn "Lao động".
4) Nhập Tên hồ sơ = "HS kiem thu linh vuc va tep", Loại hồ sơ = "Hợp đồng", gõ vào ô văn bản dài nội dung "Noi dung kiem thu mo ta", đính kèm tệp PDF đã chuẩn bị, rồi bấm nút lưu của biểu mẫu.
5) Mở lại đúng hồ sơ vừa tạo bằng chức năng Chỉnh sửa (hoặc Xem chi tiết) và đối chiếu 3 giá trị vừa nhập.
✅ PASS khi ĐỦ 4 điều: (i) biểu mẫu KHÔNG còn ô "Số/Ký hiệu"; (ii) biểu mẫu CÓ ô chọn "Lĩnh vực pháp lý" và bước 3 danh sách lĩnh vực có ít nhất 1 giá trị chọn được (không rỗng); (iii) biểu mẫu có ĐÚNG MỘT ô văn bản dài mang nhãn "Mô tả" — không còn ô nào nhãn "Ghi chú"; (iv) biểu mẫu có ô đính kèm tệp, bước 4 lưu thành công, và bước 5 mở lại thấy đủ 3 giá trị: lĩnh vực = Lao động, nội dung "Noi dung kiem thu mo ta" nằm trong ô "Mô tả", tên tệp PDF đã đính kèm hiển thị trong hồ sơ.
❌ FAIL nếu: vẫn còn ô "Số/Ký hiệu" hiển thị trên biểu mẫu, hoặc ô chỉ bị ẩn khỏi giao diện nhưng giá trị của nó vẫn nằm trong dữ liệu gửi lên khi lưu; HOẶC không có ô "Lĩnh vực pháp lý", hoặc có ô nhưng danh sách chọn mở ra rỗng; HOẶC ô văn bản dài vẫn mang nhãn "Ghi chú"; HOẶC không có ô đính kèm tệp; HOẶC nhập được nhưng bước 5 mở lại mất một trong ba giá trị lĩnh vực / mô tả / tệp (giao diện có ô nhưng dữ liệu không được lưu).
⚠️ Bẫy 1 — ý 2 là ĐỔI NHÃN, không phải thêm trường: nếu sau fix biểu mẫu xuất hiện đồng thời cả ô "Mô tả" và ô "Ghi chú" thì tính FAIL, vì SRS chỉ quy định một ô văn bản dài duy nhất (:572).
⚠️ Bẫy 2 — hồ sơ cũ tạo TRƯỚC khi fix không có lĩnh vực và không có tệp; mở hồ sơ cũ ra thấy trống là ĐÚNG, không tính FAIL. Bắt buộc dùng hồ sơ tạo MỚI ở bước 4 để kết luận.
⚠️ Bẫy 3 — nếu bước 4 bị chặn vì tệp vượt 20MB hoặc bị chặn do quét mã độc thì đó là ràng buộc SRS đang chạy đúng (:604, :684, :685); đổi sang tệp PDF sạch nhỏ hơn 20MB rồi làm lại, KHÔNG tính FAIL của case này.
Ảnh lỗi cũ (biểu mẫu 8 ô, thừa "Số/Ký hiệu", nhãn "Ghi chú", không có ô lĩnh vực và không có ô upload): image/BUG-QLHSPLDN_03-form-them-moi.png và image/BUG-QLHSPLDN_03-form-them-moi-bottom.png

## Triệu chứng QA ghi nhận lượt trước (sáng 25/07) — CHỈ tham khảo, không phải tiêu chí

- Biểu mẫu Thêm/Sửa hồ sơ pháp lý đã có ô "Lĩnh vực pháp lý", ô "Mô tả" và ô "Tệp đính kèm"; ô "Số/Ký hiệu" đã được gỡ.
- Tạo mới 1 hồ sơ: chọn lĩnh vực "Lao động", nhập nội dung vào ô "Mô tả", đính 1 tệp PDF sạch dưới 20MB → lưu thành công.
- Mở lại đúng hồ sơ vừa tạo bằng nút [Sửa]: lĩnh vực và mô tả hiển thị đúng, NHƯNG ô "Tệp đính kèm" TRỐNG — không hiển thị tên tệp đã đính, không có cách nào xem hoặc tải lại tệp từ hồ sơ.
- Trong khi đó bảng danh sách vẫn hiển thị cột "Có tệp đính kèm" = "Có" cho hồ sơ này, tức tệp vẫn được lưu nhưng màn hồ sơ không hiển thị lại.
- Đã thử nhiều lần, kết quả giống nhau. Sửa một trường khác rồi lưu thì tệp không bị mất, nên đây là lỗi hiển thị khi mở lại hồ sơ.
- Đề nghị: mở lại hồ sơ phải liệt kê được các tệp đã đính kèm và cho xem/tải tệp.
