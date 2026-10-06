# Phản hồi BA — Tư vấn theo vụ việc TVCS (phiếu ba-confirmation-needed-tvcs.md)

**Phiếu nguồn:** `ba-confirmation-needed-tvcs.md` (UAT tuần 3, 6 nhóm A–F, 12 mục cần BA)
**Nguồn đối chiếu:** SRS v3.5 `_bmad-output/planning-artifacts/srs-v3.5/srs-fr-12-tv-chuyen-sau.md` (bản chuẩn hiện hành, 1639 dòng) + baseline `srs-v3.5.md`; CSV `docs/Input/Danh sách transaction_v1.1_2026-03-27.csv`.
**Ngày lập:** 23/07/2026.

> **Lưu ý số dòng:** phiếu QA trích theo bản sao `input/srs-update-2026-5-5/` và `srs-v3.5/` (đánh số dòng lệch nhẹ). Toàn bộ trích dẫn dưới đây đã đối chiếu lại trên bản chuẩn `_bmad-output/planning-artifacts/srs-v3.5/srs-fr-12-tv-chuyen-sau.md` — **nội dung khớp**, số dòng cập nhật theo bản chuẩn.

> **Khuôn phản hồi:** mỗi mục trả lời 3 câu hỏi quyết định — (1) phần mềm đúng SRS chưa, (2) đối tác yêu cầu có khác SRS không, (3) yêu cầu đó có bắt buộc cho luồng nghiệp vụ không — rồi phân **Loại 1** (sai SRS, Dev fix theo SRS) / **Loại 2** (phải sửa, cần bổ sung/dọn SRS) / **Loại 3** (web đúng SRS, ghi nhận cải tiến).

---

## Nhóm A — Màn danh sách SCR-X1-01

### QLNDTVVCG_40 — Xuất Excel danh sách TVCS: tên tệp + tập cột chưa được đặc tả

**(1) Phần mềm đúng SRS chưa?** SRS thiếu — SCR-X1-01 chỉ ghi có nút `[Xuất Excel]`, không quy định tên tệp/tập cột (`srs-fr-12-tv-chuyen-sau.md:1090`); mô tả export duy nhất trong tài liệu (`:632`, đặt mã `HSPL-{date}-{seq}` ở `:647`) là của FR-X.1-04/UC150 (`:529`), không áp cho danh sách TVCS; baseline `srs-v3.5.md` cũng không có quy ước chung. App không sai đặc tả (xuất vẫn chạy, tải được tệp có dữ liệu).
**(2) Đối tác yêu cầu có khác SRS không? Khác gì?** CÓ — muốn tên `TVCS-danh-sach-{YYYYMMDD-HHmm}.xlsx` + đủ cột hiển thị (Doanh nghiệp, Chuyên gia, Lĩnh vực…) thêm "Nội dung tư vấn (đầy đủ)" và "Ngày hoàn thành"; app hiện xuất `noi-dung-tu-van-cs-{YYYYMMDD}.xlsx` (thiếu giờ-phút), thiếu cột DN/CG/Lĩnh vực/Tiêu đề, thừa cột Nội dung + Điểm đánh giá.
**(3) Yêu cầu đó có bắt buộc cho luồng nghiệp vụ không?** CÓ → phải sửa (đặc tả export còn khuyết) — BA bổ sung Processing "Xuất Excel danh sách TVCS" vào FR-X.1-01/SCR-X1-01 (`:1090`): tên tệp có giờ-phút, tập cột bám cột đang hiển thị (Mã tư vấn / Doanh nghiệp / Chuyên gia / Lĩnh vực / Tiêu đề / Trạng thái / Ngày bắt đầu / Ngày tạo, có thể thêm "Ngày hoàn thành"), "Nội dung tư vấn (đầy đủ)" chỉ khi người dùng chọn xuất đầy đủ, xuất theo đúng bộ lọc hiện hành; sau đó Dev thực hiện. (*Phương án thay thế:* tách "Xuất danh sách" / "Xuất chi tiết", chỉ nên chọn nếu đối tác cần bản đầy đủ thường xuyên.)
**→ Kết luận: Loại 2 — Cập nhật SRS rồi Dev làm theo SRS mới:** bổ sung Processing "Xuất Excel danh sách TVCS" vào SCR-X1-01 (tên tệp có giờ-phút, tập cột bám cột đang hiển thị) rồi Dev thực hiện. **✅ BA duyệt 2026-07-24.**
> **Phương án xử lý (cập nhật SRS):** `srs-fr-12-tv-chuyen-sau.md:1090` (SCR-X1-01, hàng nút `[Xuất Excel]`) + khối Processing FR-X.1-01 (`:125`–`163`) — thêm mục Processing "Xuất Excel danh sách TVCS": tên tệp `TVCS-danh-sach-{YYYYMMDD-HHmm}.xlsx` (có giờ-phút), tập cột bám cột đang hiển thị (Mã tư vấn / Doanh nghiệp / Chuyên gia / Lĩnh vực / Tiêu đề / Trạng thái / Ngày bắt đầu / Ngày tạo [+ Ngày hoàn thành]), "Nội dung tư vấn (đầy đủ)" chỉ khi người dùng chọn xuất đầy đủ, xuất theo đúng bộ lọc hiện hành. Sau khi SRS chốt, Dev đặt lại tên tệp + tập cột export cho khớp.

---

## Nhóm B — Form Thêm/Sửa SCR-X1-02

### QLNDTVVCG_06 — "Ngày tư vấn" không mặc định hôm nay + thiếu "Cơ quan tiếp nhận"

**(1) Phần mềm đúng SRS chưa?** ĐÚNG — `ngay_tu_van` có ô "Mặc định" = "—", SRS không yêu cầu tự điền hôm nay (`srs-fr-12-tv-chuyen-sau.md:116`); `don_vi_id` (đơn vị tiếp nhận) hệ thống tự gán = đơn vị của cán bộ đăng nhập, không phải ô nhập tay (`:118`); khối "Thông tin cơ bản" không có ô "Cơ quan tiếp nhận" (`:1142`). Web khớp cả 2 điểm.
**(2) Đối tác yêu cầu có khác SRS không? Khác gì?** CÓ — muốn form tự điền ngày hôm nay và hiển thị ô "Cơ quan tiếp nhận".
**(3) Yêu cầu đó có bắt buộc cho luồng nghiệp vụ không?** KHÔNG → yêu cầu cải tiến — hai điểm là cải tiến UX tùy chọn: (1) mặc định `ngay_tu_van` = hôm nay (nếu chốt, đổi cột "Mặc định" `:116` từ "—" sang "hôm nay"); (2) hiển thị "Cơ quan tiếp nhận" **chỉ đọc** = đơn vị CB (nếu chốt, thêm trường read-only vào Accordion `:1142`). BA chốt rồi cập nhật SRS + Expected testcase.
**→ Kết luận: Loại 3 — Không sửa, đề nghị đối tác đưa vào danh sách yêu cầu cải tiến:** mặc định ngày hôm nay + ô "Cơ quan tiếp nhận" chỉ đọc là cải tiến UX tùy chọn; BA chốt rồi mới cập nhật SRS + Expected testcase. **✅ BA duyệt 2026-07-24.**
> **Phản hồi gửi đối tác:** [Lý do] Phần mềm hiện tuân thủ đúng đặc tả: trường "Ngày tư vấn" không được quy định tự điền hôm nay, và "Cơ quan tiếp nhận" do hệ thống tự gán theo đơn vị của cán bộ đăng nhập chứ không phải ô nhập tay, nên đây không phải lỗi. Việc mặc định ngày hôm nay và hiển thị ô "Cơ quan tiếp nhận" ở dạng chỉ đọc là cải tiến trải nghiệm tùy chọn. [Nhận định] Kính đề nghị Quý đối tác đưa nội dung này vào danh sách yêu cầu cải tiến.

---

### QLNDTVVCG_08 (mục phụ) — Trường "Vụ việc liên kết (tùy chọn)" thừa so với §form spec nhưng đúng theo thực thể

*(Đã đối chiếu evidence 2026-07-24: `:1316` xác nhận FK `vu_viec_id` có thật; ô "Vụ việc liên kết (tùy chọn)" trên ảnh QLNDTVVCG_08.jpg là hợp lệ. **Lưu ý:** phiếu này chỉ xử lý sub-item "Vụ việc liên kết"; hai sub-item còn lại của testcase — "Nội dung tư vấn không phải trình soạn thảo văn bản" và "thiếu trường Tiêu đề (đang hiển thị 'Tóm tắt')" — đối chiếu evidence là **bug thật**: SRS `:1143` yêu cầu Rich Text Editor + nhãn "Tiêu đề", ảnh cho thấy web dùng textarea thường + nhãn "Tóm tắt". Hai điểm này là lỗi rõ, Dev fix theo SRS, không cần BA quyết — xem thêm QLNDTVVCG_17.)*

**(1) Phần mềm đúng SRS chưa?** SRS mâu thuẫn — §Inputs FR-X.1-01 (`srs-fr-12-tv-chuyen-sau.md:108`–`120`) và khối form (`:1142`–`1143`) không liệt kê `vu_viec_id`, nhưng bảng dữ liệu/sơ đồ TVCS lại có FK `vu_viec_id` (bỏ trống được): `:1229` (sơ đồ dữ liệu), `:1316` ("Vụ việc liên quan (nếu có)"). Ô trên form khớp ý đồ bảng dữ liệu → app không lỗi.
**(2) Đối tác yêu cầu có khác SRS không? Khác gì?** CÓ — đối tác coi ô "Vụ việc liên kết" là thừa vì không nằm trong danh sách trường mà §form spec liệt kê.
**(3) Yêu cầu đó có bắt buộc cho luồng nghiệp vụ không?** CÓ → phải sửa (đồng bộ SRS, **giữ trường**) — gắn nội dung tư vấn với vụ việc gốc giúp truy nguồn (Nghị định 55/2019/NĐ-CP Điều 10 khoản 2 điểm c); khi ERD ↔ bảng trường nhập chọi nhau, đặc tả form bám bảng dữ liệu. Bổ sung `vu_viec_id` vào §Inputs (`:108`–`120`) + Accordion §Thành phần (`:1142`–`1143`), đối chiếu `:1316`. Không gỡ trường (gỡ thì phải sửa cả ERD `:1229`/`:1316` + mất truy nguồn → không khuyến nghị).
**→ Kết luận: Loại 2 — Cập nhật SRS rồi Dev làm theo SRS mới:** giữ trường "Vụ việc liên kết", bổ sung `vu_viec_id` vào §Inputs + Accordion §Thành phần cho khớp bảng dữ liệu. **✅ BA duyệt 2026-07-24.**
> **Phương án xử lý (cập nhật SRS):** `srs-fr-12-tv-chuyen-sau.md:108`–`120` (§Inputs, bổ sung sau field #15) + `:1142` (Accordion "Thông tin cơ bản") — thêm field `vu_viec_id` (FK → VU_VIEC, tùy chọn, bỏ trống được) vào bảng Inputs và ghi ô "Vụ việc liên kết (tùy chọn)" vào Accordion, đối chiếu ERD `:1316`; giữ nguyên trường, không gỡ. Dev giữ ô "Vụ việc liên kết (tùy chọn)" hiện có trên form, không đổi code.

---

## Nhóm C — Màn Chi tiết SCR-X1-02

### QLNDTVVCG_15 — Số nhóm accordion + nhãn nhóm (SRS tự mâu thuẫn)

*(Đã đối chiếu evidence 2026-07-24: ảnh QLNDTVVCG_15.jpg cho thấy build HIỆN TẠI có **7 khối** — dư khối "Vụ việc liên kết" tách riêng; phần "7 nhóm" mà đối tác nêu **có tái hiện**, không phải build cũ. Dev FE cần gộp "Vụ việc liên kết" vào "Thông tin cơ bản" để về 6 khối.)*

**(1) Phần mềm đúng SRS chưa?** SAI + SRS mâu thuẫn — §Bố cục liệt kê **5 khối** tên ngắn (`srs-fr-12-tv-chuyen-sau.md:1133`), còn §Thành phần liệt kê **6 khối** (5 + "Công khai chuyên trang" chỉ hiện khi DA_DUYET theo BR-PUBLIC-01, `:1142`–`:1147`, hàng 8b `:1147`); cả hai đều KHÔNG có khối "Vụ việc liên kết" riêng. Build hiện đếm **7 khối** (dư "Vụ việc liên kết" tách accordion — SRS chỉ có FK `vu_viec_id` `:1316`, không phải nhóm màn hình). Nhãn: thực thể `TU_LIEU_PHAP_LY_VV` (`:1204`, `:1406`/`:1408`), FR-X.1-06 "Quản lý **tư liệu pháp lý** của vụ việc" (`:795`) → web ghi "Tư liệu pháp **luật**" là SAI; "Nhật ký", "Trạng thái công khai" cũng lệch.
**(2) Đối tác yêu cầu có khác SRS không? Khác gì?** CÓ — đối tác muốn nhãn "Tư liệu pháp lý liên kết", "Nhật ký thao tác" và tổng **5 khối**; phản ánh "7 nhóm" thì đúng build hiện tại.
**(3) Yêu cầu đó có bắt buộc cho luồng nghiệp vụ không?** CÓ → phải sửa — chốt §Thành phần (`:1144`–`:1147`) làm chuẩn: **6 nhóm** (5 cơ bản + "Công khai chuyên trang" khi DA_DUYET). Dev FE gỡ accordion "Vụ việc liên kết" riêng, gộp trường vào "Thông tin cơ bản"; sửa 3 nhãn "Tư liệu pháp luật" → "Tư liệu pháp lý liên kết", "Nhật ký" → "Nhật ký thao tác", "Trạng thái công khai" → "Công khai chuyên trang"; dọn §Bố cục `:1133` thêm nhóm Công khai cho khớp. Mong muốn "5 nhóm" của đối tác không đúng chuẩn (chuẩn 6 cho bản Đã duyệt).
**→ Kết luận: Loại 1 — Lỗi phần mềm, Dev sửa theo SRS:** Dev FE gỡ accordion "Vụ việc liên kết" riêng về 6 nhóm + sửa 3 nhãn ("Tư liệu pháp lý liên kết" / "Nhật ký thao tác" / "Công khai chuyên trang"). **✅ BA duyệt 2026-07-24.**

---

### QLNDTVVCG_17 — "Cơ quan tiếp nhận" ở Nhóm 1 + "Tiêu đề/Tóm tắt" Nhóm 2

*(Đã đối chiếu evidence 2026-07-24 — sửa kết luận cũ.)*

**(1) Phần mềm đúng SRS chưa?** SAI (nhãn) + ĐÚNG (đơn vị) — trường chính thức là `tieu_de`, "chính thức hóa từ `tom_tat`" theo chốt STT68/STT11 (`srs-fr-12-tv-chuyen-sau.md:114`; §Thành phần `:1143` ghi nhãn "Tiêu đề"), nhưng ảnh QLNDTVVCG_17.jpg (+ form Thêm QLNDTVVCG_06.jpg/_08.jpg) build **vẫn hiển thị "Tóm tắt"** → web SAI. "Cơ quan tiếp nhận": `don_vi_id` tự gán (`:118`), bảng dữ liệu mô tả `:1318` nhưng không bắt hiển thị ở màn chi tiết, khối 1 §Thành phần `:1142` không liệt kê → không hiển thị = đúng SRS.
**(2) Đối tác yêu cầu có khác SRS không? Khác gì?** CÓ — muốn nhãn "Tiêu đề" (đúng, là bug) + hiển thị ô "Cơ quan tiếp nhận" ở khối 1 (vượt SRS).
**(3) Yêu cầu đó có bắt buộc cho luồng nghiệp vụ không?** CÓ (nhãn) → phải sửa: Dev FE đổi nhãn "Tóm tắt" → **"Tiêu đề"** ở form Thêm/Sửa + màn Chi tiết (Nhóm 2) theo `:114`/`:1143`, SRS giữ nguyên. KHÔNG (Cơ quan tiếp nhận) → cải tiến tùy chọn, chốt chung QLNDTVVCG_06 điểm (2): nếu chốt thì thêm trường **chỉ đọc** vào Nhóm 1 (`:1142`).
**→ Kết luận: Loại 1 — Lỗi phần mềm, Dev sửa theo SRS** (kèm cải tiến tùy chọn gộp với _06)**:** Dev FE đổi nhãn "Tóm tắt" → "Tiêu đề" ở form Thêm/Sửa + màn Chi tiết. **✅ BA duyệt 2026-07-24.**

---

### QLNDTVVCG_22 — Modal Phân công CG: ô "Chuyên môn" trống + chú thích SLA

**(1) Phần mềm đúng SRS chưa?** ĐÚNG (banner SLA) + SRS thiếu (ô Chuyên môn) — modal Phân công phải "gợi ý TOP 5 chuyên gia… + thông tin thời hạn xử lý (2 ngày làm việc để xác nhận)" (`srs-fr-12-tv-chuyen-sau.md:1153`), dòng SLA đã hiển thị → đạt; câu "sẽ được gửi thông báo" SRS không nhắc. Ô "Chuyên môn": SRS ghi hiện "chuyên môn, SĐT, email" (`:1142`) + "chuyên môn phù hợp lĩnh vực" (`:160`) nhưng không nói lấy từ trường nào; CG mẫu có lĩnh vực nhưng trường chuyên ngành trống → hiển thị "—". Do SRS chưa định nghĩa rõ, không phải lỗi FE.
**(2) Đối tác yêu cầu có khác SRS không? Khác gì?** CÓ — muốn ô "Chuyên môn" có dữ liệu (không "—") và thêm chú thích "Chuyên gia sẽ được gửi thông báo…".
**(3) Yêu cầu đó có bắt buộc cho luồng nghiệp vụ không?** CÓ (ô Chuyên môn) → phải sửa: ghép đúng CG với vụ việc là nghĩa vụ nghiệp vụ — Nghị định 55/2019/NĐ-CP Điều 9 (đã được NĐ 18/2026/NĐ-CP sửa đổi) yêu cầu "tư vấn viên pháp luật **phù hợp** thuộc mạng lưới". BA định nghĩa mức nghiệp vụ: ô phải phản ánh lĩnh vực/chuyên môn CG, không để trống khi CG đã có dữ liệu lĩnh vực (Dev chọn trường nguồn); đảm bảo hồ sơ CG (FR-04) nhập chuyên ngành (trống = thiếu dữ liệu CG, owner quản trị/dữ liệu CG). KHÔNG (chú thích SLA) → cải tiến tùy chọn.
**→ Kết luận: Loại 2 — Cập nhật SRS rồi Dev làm theo SRS mới:** BA định nghĩa ô "Chuyên môn" phải phản ánh lĩnh vực/chuyên môn CG (không để trống khi CG đã có dữ liệu) rồi Dev chọn trường nguồn. **✅ BA duyệt 2026-07-24.**
> **Phương án xử lý (cập nhật SRS):** `srs-fr-12-tv-chuyen-sau.md:1142` (mô tả CG modal Phân công "khi chọn hiện chuyên môn, SĐT, email") + `:160` (bước "chuyên môn phù hợp lĩnh vực") — SRS phải ĐỊNH NGHĨA RÕ nguồn dữ liệu ô "Chuyên môn" trong modal Phân công CG, lấy từ hồ sơ CG (FR-04) theo quy tắc: **ưu tiên `chuyen_nganh`; nếu `chuyen_nganh` trống thì ghép tên các lĩnh vực từ `linh_vuc_ids`; nếu cả hai trống thì hiển thị "Chưa cập nhật"**. Dev chỉ map ô "Chuyên môn" theo đúng quy tắc này, KHÔNG tự quyết nguồn dữ liệu; hồ sơ CG (FR-04) bảo đảm có nhập `chuyen_nganh`/`linh_vuc_ids` (owner dữ liệu CG).

---

## Nhóm D — Workflow SM-TVCS

### QLNDTVVCG_36 — Cơ chế "duyệt hủy" record DANG_TU_VAN

**(1) Phần mềm đúng SRS chưa?** SAI + SRS thiếu luồng — SRS có guard rõ: bước 4 Hủy "Nếu đang tư vấn (DANG_TU_VAN): **phải có DN đồng ý hủy + CB Phê duyệt duyệt hủy**" (`srs-fr-12-tv-chuyen-sau.md:229`), bảng SM-TVCS chuyển `DANG_TU_VAN → HUY` ghi "**DN yêu cầu hủy + CB PD duyệt**" (`:1512`; sơ đồ `:1484`); app cho hủy thẳng sang HUY (BUG-QLNDTVVCG_36 đã ghi nhận) → SAI. Nhưng SRS mới có 7 trạng thái (`:1489`–`:1512` / bảng `:1308`), **chưa có** state trung gian "CHO_DUYET_HUY" + luồng con, và tự vênh người khởi tạo `:229` ("DN **đồng ý**", CB bấm trước) ↔ `:1512` ("DN **yêu cầu**", DN bấm trước).
**(2) Đối tác yêu cầu có khác SRS không? Khác gì?** CÓ — phản ánh hủy từ "Đang tư vấn" chuyển thẳng "Đã hủy", không qua bước "chờ duyệt hủy".
**(3) Yêu cầu đó có bắt buộc cho luồng nghiệp vụ không?** CÓ → phải sửa — hủy nội dung đang làm dở chạm quyền lợi DN (Nghị định 55/2019/NĐ-CP Điều 10 khoản 2 điểm c) nên cần DN đồng ý + một cấp phê duyệt. BA thiết kế state trung gian + Processing sub-flow + màn/nút "Duyệt hủy" cho CB PD, làm rõ mâu thuẫn người khởi tạo `:229` ↔ `:1512`, cập nhật `:222`–`232` (Processing Hủy) và `:1489`–`:1512` (SM); Dev chặn hủy trực tiếp theo SRS trước, làm đúng luồng sau khi SRS bổ sung. (*Phương án thay thế giữ 7 state + chỉ chặn nút → không có nơi lưu/hiển thị yêu cầu hủy đang chờ → không khuyến nghị.*)
**→ Kết luận: Loại 2 — Cập nhật SRS rồi Dev làm theo SRS mới:** BA thiết kế state trung gian "chờ duyệt hủy" + luồng "Duyệt hủy" cho CB PD; Dev chặn hủy trực tiếp theo SRS trước, làm đúng luồng sau khi SRS bổ sung. **✅ BA duyệt 2026-07-24.**
> **Phương án xử lý (cập nhật SRS):** SRS **đã có sẵn cổng duyệt hủy** — chuyển `DANG_TU_VAN → HUY` yêu cầu điều kiện "**DN yêu cầu hủy + CB PD duyệt**" (`:1512`). Bug là app bỏ qua cổng này, cho hủy thẳng. Chốt **giữ mô hình chuyển tiếp trực tiếp có điều kiện của SRS** (không thêm state trung gian), chỉ sửa 2 điểm để gỡ mâu thuẫn và bổ sung nhánh từ chối:
> - **Gỡ mâu thuẫn người khởi tạo** — chốt **DN là bên yêu cầu hủy** (DN muốn dừng); sửa `:229` bước 4 Processing Hủy từ "yêu cầu DN **đồng ý** hủy + CB Phê duyệt duyệt hủy" → "**DN yêu cầu hủy** + CB Phê duyệt duyệt hủy" cho khớp `:1512` ("DN yêu cầu hủy + CB PD duyệt").
> - **Bổ sung nhánh CB PD TỪ CHỐI duyệt hủy** vào Processing "Hủy yêu cầu" `:222`–`232` — theo tiền lệ `CHO_PHE_DUYET → DANG_TU_VAN` "CB PD từ chối" (BR-FLOW-04, `:1510`): nếu CB PD **từ chối** duyệt hủy thì **hồ sơ giữ nguyên `DANG_TU_VAN`** (không sang HUY), yêu cầu lý do từ chối.
>
> **KHÔNG thêm state `CHO_DUYET_HUY`** (bỏ đề xuất thêm enum entity + state trung gian ở `:115`/`:1308`/SM) — mô hình chuyển tiếp trực tiếp có điều kiện đã đủ và nhẹ hơn.
> *(Phương án tùy chọn: nếu CĐT muốn theo dõi tường minh trạng thái "chờ duyệt hủy" trên UI/báo cáo, mới thêm state `CHO_DUYET_HUY` + luồng con — không khuyến nghị mặc định.)*
>
> Dev chặn hủy trực tiếp DANG_TU_VAN → HUY khi chưa có duyệt của CB PD (BUG-QLNDTVVCG_36), thực thi đúng cổng duyệt hủy đã có sẵn trong SRS.

---

## Nhóm E — Tư liệu pháp lý, tab SCR-X1-02

### QLTLPLCVV_02 — Bảng tư liệu thiếu cột "Ngày tạo" / "Người tạo" (SRS tự mâu thuẫn)

**(1) Phần mềm đúng SRS chưa?** SRS mâu thuẫn — Outputs "Tìm kiếm tư liệu" quy định `nguoi_tao` "luôn" hiển thị (`srs-fr-12-tv-chuyen-sau.md:937`) và `ngay_tao` "luôn" hiển thị dạng dd/mm/yyyy HH:mm (`:938`), nhưng §Thành phần mô tả bảng gọn "Tên / Loại / Trạng thái / Số file / Hành động" (`:1144`), bỏ 2 cột. §Thành phần `:1144` vốn cũ và thiếu (ghi "Số file", thiếu "Lĩnh vực"/"Công khai lúc") → lấy Outputs làm chuẩn. Web hiện thiếu 2 cột.
**(2) Đối tác yêu cầu có khác SRS không? Khác gì?** CÓ — muốn bảng có cột "Ngày tạo" và "Người tạo".
**(3) Yêu cầu đó có bắt buộc cho luồng nghiệp vụ không?** CÓ → phải sửa — cột Người tạo/Ngày tạo giúp truy nguồn, nhất là khi tư liệu chia sẻ công khai lên Cổng (Nghị định 55/2019/NĐ-CP Điều 10 khoản 2 điểm a; lưu dấu vết theo Nghị định 85/2016/NĐ-CP — số điều/khoản cụ thể cần CĐT xác nhận với văn bản gốc). Chốt theo Outputs (`:937`/`:938`): bảng phải có "Người tạo" + "Ngày tạo (dd/mm/yyyy HH:mm)"; cập nhật §Thành phần `:1144` liệt kê đủ cột (Tên / Loại / Lĩnh vực / File / Trạng thái / Công khai lúc / Người tạo / Ngày tạo / Hành động); Dev FE bổ sung (Dev BE nếu API chưa trả 2 trường).
**→ Kết luận: Loại 2 — Cập nhật SRS rồi Dev làm theo SRS mới:** chốt theo Outputs, bảng tư liệu phải có cột "Người tạo" + "Ngày tạo (dd/mm/yyyy HH:mm)"; cập nhật §Thành phần rồi Dev bổ sung. **✅ BA duyệt 2026-07-24.**
> **Phương án xử lý (cập nhật SRS):** `srs-fr-12-tv-chuyen-sau.md:1144` (§Thành phần, Accordion "Tư liệu PL liên kết") — liệt kê đủ cột bảng tư liệu (Tên / Loại / Lĩnh vực / File / Trạng thái / Công khai lúc / Người tạo / Ngày tạo / Hành động), đồng bộ với Outputs "Tìm kiếm tư liệu" `:937` (`nguoi_tao` "luôn" hiển thị) + `:938` (`ngay_tao` "luôn", dd/mm/yyyy HH:mm). Dev FE bổ sung 2 cột "Người tạo" + "Ngày tạo"; Dev BE bổ sung nếu API chi tiết chưa trả 2 trường.

---

### QLTLPLCVV_03 — Nút "Thêm tư liệu" hiện ở mọi trạng thái TVCS

**(1) Phần mềm đúng SRS chưa?** ĐÚNG — §Thành phần quy định nút [+ Thêm tư liệu] **"luôn hiển thị"** (`srs-fr-12-tv-chuyen-sau.md:1144`); Quy tắc tương tác "thêm/sửa/xóa tư liệu ngay tại chỗ", không khóa theo trạng thái TVCS (`:1156`). Rule "chỉ cho vào chế độ sửa khi TIEP_NHAN/DANG_TU_VAN" (`:1152`) chỉ áp cho việc sửa các trường bản ghi TVCS (nút `[Lưu]` chỉ hiện ở 2 trạng thái đó, `:1148`), KHÔNG áp CRUD tư liệu. `:1144` và `:1152` không mâu thuẫn.
**(2) Đối tác yêu cầu có khác SRS không? Khác gì?** CÓ — muốn ẩn nút Thêm khi TVCS = DA_DUYET và HUY.
**(3) Yêu cầu đó có bắt buộc cho luồng nghiệp vụ không?** KHÔNG → yêu cầu cải tiến — web đúng SRS, kỳ vọng "ẩn ở Đã duyệt/Hủy" không có cơ sở SRS. Cải tiến đáng cân nhắc: chặn thêm tư liệu khi TVCS = HUY (cập nhật `:1144` thêm điều kiện loại trừ HUY); DA_DUYET nên giữ cho thêm. Expected testcase cập nhật theo SRS hiện hành.
**→ Kết luận: Loại 3 — Không sửa, đề nghị đối tác đưa vào danh sách yêu cầu cải tiến:** web đúng SRS (nút "luôn hiển thị"); kỳ vọng ẩn nút khi DA_DUYET/HUY không có cơ sở SRS, chỉ cân nhắc chặn khi HUY. **✅ BA duyệt 2026-07-24.**
> **Phản hồi gửi đối tác:** [Lý do] Phần mềm hiện đúng đặc tả: nút "Thêm tư liệu" được quy định "luôn hiển thị" và thao tác thêm/sửa/xóa tư liệu không bị khóa theo trạng thái vụ việc tư vấn, nên việc nút hiển thị ở mọi trạng thái không phải lỗi. Kỳ vọng ẩn nút khi trạng thái "Đã duyệt"/"Hủy" hiện chưa có cơ sở trong đặc tả. [Nhận định] Kính đề nghị Quý đối tác đưa nội dung này vào danh sách yêu cầu cải tiến.

---

### QLTLPLCVV_07 — Nút "Sửa" + cho sửa (mô tả/file) trên tư liệu "Đã công khai"

*(Đã đối chiếu evidence 2026-07-24: ảnh QLTLPLCVV_07.jpg xác nhận nút **[Sửa] hiển thị trên dòng tư liệu "Đã công khai"** — đúng phản ánh đối tác. Riêng khẳng định "BE cho sửa thật mô tả/tệp, trả thành công" chưa nhìn thấy trực tiếp trên ảnh tĩnh này, nhưng không đổi hướng xử lý.)*

**(1) Phần mềm đúng SRS chưa?** SAI — SRS khóa sửa toàn bộ khi công khai: bước 3 "nếu đang công khai (CONG_KHAI) → **không cho sửa (phải hủy công khai trước)**" (`srs-fr-12-tv-chuyen-sau.md:888`), không ngoại lệ mô tả/tệp; app lại cho sửa `moTa` + `fileDinhKemIds` trên tư liệu công khai và dùng mã `ERR-STATE-X1-06-01` — mã này **không có trong SRS** (Error Handling chỉ tới ERR-TLPL-05 / WRN-TLPL-01, `:952`–`957`), Dev tự đặt, chưa được BA/CĐT chốt.
**(2) Đối tác yêu cầu có khác SRS không? Khác gì?** CÓ (khớp SRS) — đối tác muốn ẩn nút Sửa khi "Công khai", chỉ cho sửa khi "Nháp" — chính là Kết quả mong đợi của testcase.
**(3) Yêu cầu đó có bắt buộc cho luồng nghiệp vụ không?** CÓ → phải sửa — nội dung công khai (cung cấp thông tin pháp luật, Nghị định 55/2019/NĐ-CP Điều 10 khoản 2 điểm a) không được sửa ngầm. Giữ `:888`: Dev BE chặn PATCH (kể cả `moTa`/`fileDinhKemIds`) khi `trang_thai = CONG_KHAI`, trả lỗi yêu cầu hủy công khai trước; Dev FE khóa/ẩn nút [Sửa]. Phương án "cho sửa field phụ khi công khai" chỉ khi CĐT/PM quyết chính thức (kèm cập nhật `:888` + bổ sung `ERR-STATE-X1-06-01` vào Error Handling + vẫn ghi nhật ký) → **BA khuyến nghị KHÔNG, giữ `:888`**.
**→ Kết luận: Loại 1 — Lỗi phần mềm, Dev sửa theo SRS:** giữ khóa sửa khi công khai — Dev BE chặn PATCH (kể cả mô tả/tệp) khi CONG_KHAI, Dev FE khóa/ẩn nút [Sửa]. **✅ BA duyệt 2026-07-24.**

---

## Nhóm F — Quản lý tư liệu pháp lý của vụ việc

### QLTLPLCVV_15 — Upload file mã độc (EICAR) không bị chặn

*(Đã đối chiếu evidence 2026-07-24 — sửa kết luận cũ: tệp mã độc **đã bị chặn** (upload thất bại), KHÔNG phải "nhận là sạch". Vấn đề thật là thông báo sai — hệ thống báo chung chung "Tải file thất bại" thay vì câu chuẩn ERR-TLPL-04. Đánh giá cũ ghi tệp "vẫn tải lên thành công, `trangThaiQuet = SACH`" là KHÔNG khớp evidence — đã sửa lại.)*

**(1) Phần mềm đúng SRS chưa?** SAI (câu chữ thông báo) — SRS có bước **"Quét virus"** (`srs-fr-12-tv-chuyen-sau.md:858`) + **E4 = ERR-TLPL-04** "File '{ten_file}' chứa mã độc" (`:955`); evidence (Kết quả thực tế + ảnh QLTLPLCVV_15.jpg) cho thấy tệp PDF mã độc bị **chặn** (toast "Tải file thất bại", tệp không đính kèm) nhưng thông báo không phải câu chuẩn ERR-TLPL-04 → lệch ở câu chữ, **không phải để lọt mã độc**.
**(2) Đối tác yêu cầu có khác SRS không? Khác gì?** CÓ — đối tác phản ánh hệ thống chỉ báo chung chung "Tải file thất bại", không phải câu thông báo chuẩn.
**(3) Yêu cầu đó có bắt buộc cho luồng nghiệp vụ không?** CÓ → phải sửa — chống mã độc là nghĩa vụ pháp lý: **Luật An toàn thông tin mạng 2015 (Luật 86/2015/QH13) Điều 11 khoản 1** ("có trách nhiệm thực hiện phòng ngừa, ngăn chặn phần mềm độc hại…"), Điều 3 khoản 11 định nghĩa phần mềm độc hại, khoản 2 mức cao hơn cho hệ thống quan trọng quốc gia; Nghị định 85/2016/NĐ-CP + TCVN 11930 (số điều/khoản cần CĐT xác nhận với văn bản gốc). Dev BE trả đúng `ERR-TLPL-04` "Tệp «{ten_file}» chứa mã độc" khi bước Quét virus chặn tệp, và **xác nhận việc chặn đúng do quét virus** (không phải dung lượng/định dạng); kiểm chứng bằng tệp EICAR chuẩn. Mức độ: lỗi câu chữ, không phải lỗ hổng — nhưng nếu Dev xác nhận chặn KHÔNG do quét virus (bước quét chưa chạy) → mới thành lỗ hổng bảo mật ưu tiên cao (đi ngược Điều 11 khoản 1 + Nghị định 85/2016). SRS `:858`/`:955` giữ nguyên.
**→ Kết luận: Loại 1 — Lỗi phần mềm, Dev sửa theo SRS:** Dev BE trả đúng chuỗi ERR-TLPL-04 "Tệp «{ten_file}» chứa mã độc" khi quét virus chặn tệp, và xác nhận việc chặn đúng do quét virus. **✅ BA duyệt 2026-07-24.**

---

### QLTLPLCVV_16 — Xóa tệp đính kèm không có hộp xác nhận

**(1) Phần mềm đúng SRS chưa?** ĐÚNG — "Xóa file đính kèm" gồm **6 bước** (kiểm tra quyền → file có thuộc tư liệu không → xóa khỏi kho → cập nhật liên kết → cảnh báo nếu công khai mà hết file → ghi nhật ký), **KHÔNG có bước hỏi xác nhận** (`srs-fr-12-tv-chuyen-sau.md:904`–`913`); còn "Xóa tư liệu" thì **có** xác nhận "Bạn có chắc chắn muốn xóa tư liệu '{tên}'?" (`:900`). SRS cố ý phân biệt → web (xóa file không hỏi) đúng SRS.
**(2) Đối tác yêu cầu có khác SRS không? Khác gì?** CÓ — muốn có hộp xác nhận trước khi xóa từng file đính kèm.
**(3) Yêu cầu đó có bắt buộc cho luồng nghiệp vụ không?** KHÔNG → yêu cầu cải tiến — nếu BA thấy xóa file cũng nên có xác nhận (tránh xóa nhầm), cập nhật Processing `:904`–`913` thêm bước "hiển thị xác nhận" rồi mới chuyển Dev FE; chỉ khi đó web hiện tại mới thành lỗi. Expected cập nhật theo SRS.
**→ Kết luận: Loại 3 — Không sửa, đề nghị đối tác đưa vào danh sách yêu cầu cải tiến:** web đúng SRS (xóa file không hỏi là chủ đích); nếu muốn thêm xác nhận thì BA cập nhật Processing trước, khi đó web hiện tại mới thành lỗi. **✅ BA duyệt 2026-07-24.**
> **Phản hồi gửi đối tác:** [Lý do] Phần mềm hiện đúng đặc tả: quy trình "Xóa file đính kèm" được thiết kế không có bước hỏi xác nhận (khác với "Xóa tư liệu" vốn có xác nhận), đây là sự phân biệt có chủ đích trong đặc tả nên không phải lỗi. Việc bổ sung hộp xác nhận trước khi xóa từng tệp là cải tiến nhằm tránh xóa nhầm. [Nhận định] Kính đề nghị Quý đối tác đưa nội dung này vào danh sách yêu cầu cải tiến.

---

## Ghi chú anomaly (form Sửa không hiển thị file cũ trên env nip.io)

Nằm ngoài phạm vi testcase, nhưng ảnh hưởng khả năng verify QLTLPLCVV_16 và QLTLPLCVV_07: trên env `18.143.165.120.nip.io`, endpoint chi tiết trả `files: []` dù `soFile ≥ 1` (cả tư liệu NHAP mới tạo lẫn CONG_KHAI). Theo SRS, tư liệu CONG_KHAI chắc chắn phải có ≥ 1 file (`srs-fr-12-tv-chuyen-sau.md:869` + BR-PUBLIC / E5 `:956`). Đề nghị Dev xác nhận endpoint chi tiết có trả mảng `files` không, hoặc FE nạp file qua endpoint khác — chưa log bug Open cho tới khi loại trừ khác biệt build/endpoint.
