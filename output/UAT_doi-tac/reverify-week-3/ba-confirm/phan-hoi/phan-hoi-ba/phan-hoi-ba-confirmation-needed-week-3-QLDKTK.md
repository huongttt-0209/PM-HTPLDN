# Phản hồi BA — Đăng ký tài khoản DN (phiếu ba-confirmation-needed-week-3-QLDKTK.md)

**Phiếu nguồn:** `ba-confirmation-needed-week-3-QLDKTK.md`
**Nguồn đối chiếu:** SRS v3.5 — `srs-fr-10-quan-tri.md` (FR-VIII-22 §Inputs dòng 1032–1058, SCR-VIII-08 dòng 1826–1866), `srs-fr-07-doanh-nghiep.md` (entity DOANH_NGHIEP dòng 683–718, FR-V.III-NEW-03 / SCR-V.III-03), `srs-v3.5.md` (DG-08 dòng 957); CSV baseline `Danh sách transaction_v1.1_2026-03-27.csv` (UC120 dòng 1072).
**Ngày lập:** 23/07/2026. **Kiểm chứng evidence:** 24/07/2026 — Sheet UAT `1dJat1cc68…` tab "UAT_TGPL Doanh Nghiệp" (QLDKTK_01..05, dòng 1273–1277; cột K Kết quả mong đợi, L Kết quả thực tế) + ảnh `QLDKTK_04.jpg` + video `QLDKTK_03.webm` (trích khung hình toàn form đăng ký).

> **Đính chính vị trí SRS:** Đầu bài nội bộ ghi FR-VIII-22 nằm ở `srs-fr-07-doanh-nghiep.md`. Thực tế FR-VIII-22 (DN tự đăng ký, UC120) + màn SCR-VIII-08 nằm trọn ở `srs-fr-10-quan-tri.md` (dòng 1016). `srs-fr-07` chỉ chứa form CB Nghiệp vụ tự tạo hồ sơ DN (FR-V.III-NEW-03 / SCR-V.III-03) + entity DOANH_NGHIEP. Phiếu QA trích `srs-fr-10-quan-tri.md` — **đúng file**. Toàn bộ nhận định dưới đây căn cứ SRS thật ở `srs-fr-10`.

---

### QLDKTK_03 (ý b) — Mục "Thông tin tài khoản" thêm "Họ và tên người đăng ký" + "Số điện thoại"

**(1) Phần mềm đúng SRS chưa?** [SRS thiếu] — SRS chốt cứng danh sách trường: 18 trường DN (`srs-fr-10-quan-tri.md:1037`–`:1054`) + 3 trường Tài khoản (`:1055`–`:1058`), AC đếm chặt "đúng 21 trường + 1 ô cam kết" (`:1098`); nhóm Tài khoản SCR-VIII-08 chỉ 4 ô (`:1857`–`:1861`). Web thêm 2 ô ngoài danh sách → lệch danh sách chốt, nhưng đây là nhu cầu SRS chưa lường trước: người điền form thường là kế toán/nhân sự, khác người đại diện pháp luật đã có ở ô `:1048` (DN cũng đã có ô SĐT riêng ở `:1051`; hồ sơ DN cho phép 1 email kế toán dịch vụ dùng cho nhiều DN `srs-fr-07-doanh-nghiep.md:696`).
**(2) Đối tác yêu cầu có khác SRS không? Khác gì?** [CÓ] — form thêm 2 ô bắt buộc "Họ và tên người đăng ký" + "Số điện thoại" ở nhóm Tài khoản, không có trong SRS. QA ghi "Cần BA xác nhận" (Sheet UAT L1275: *"Màn hình có trường thông tin 'Họ và tên người đăng ký', 'Số điện thoại' nhưng SRS không yêu cầu 2 trường này"*).
**(3) Yêu cầu đó có bắt buộc cho luồng nghiệp vụ không?** [CÓ → phải sửa] — hai ô này nằm ngoài danh sách trường đã chốt của biểu mẫu đăng ký, luồng đăng ký chạy đủ mà không cần chúng (tên đăng nhập = MST 10 số của DN theo Thông tư 105/2020/TT-BTC Điều 5 Khoản 2 + Khoản 3 điểm a — tài khoản gắn DN, không tự lưu người dùng). Hành động: **BỎ 2 ô này khỏi biểu mẫu.** Dev FE gỡ "Họ và tên người đăng ký" + "Số điện thoại người đăng ký" khỏi nhóm Tài khoản đăng nhập. **SRS KHÔNG sửa** — danh sách trường đã chốt (18 trường DN + 3 trường Tài khoản) không có 2 trường này, nên gỡ đi là khớp đặc tả; AC `:1098` giữ nguyên cách đếm. Không phát sinh trường mới ở entity.
**→ Kết luận: Loại 1 — Lỗi phần mềm, Dev sửa theo SRS: GỠ 2 ô "Họ và tên người đăng ký" + "Số điện thoại người đăng ký" khỏi biểu mẫu đăng ký (nằm ngoài danh sách trường đã chốt). KHÔNG bổ sung vào SRS.** **✅ BA duyệt 2026-07-24.**

> **Phản hồi gửi đối tác:** Kính thưa Quý đối tác, ghi nhận phản ánh là đúng: hai ô "Họ và tên người đăng ký" và "Số điện thoại" nằm ngoài danh sách trường đã chốt của biểu mẫu đăng ký (tên đăng nhập được gắn theo mã số thuế của doanh nghiệp, luồng đăng ký không cần hai ô này). Chủ đầu tư đã chốt **bỏ hai ô này**; đơn vị phát triển sẽ gỡ khỏi biểu mẫu để khớp đặc tả. Kính đề nghị Quý đối tác giữ nguyên Kết quả mong đợi của trường hợp kiểm thử.

---

### Phát hiện 2.1 — Thứ tự 2 nhóm bị đảo (Tài khoản trước, Doanh nghiệp sau)

**(1) Phần mềm đúng SRS chưa?** [SAI] — SCR-VIII-08 chốt thứ tự "Nhóm 1 — Thông tin doanh nghiệp" (`srs-fr-10-quan-tri.md:1838`) đứng trước, "Nhóm 2 — Tài khoản đăng nhập" (`:1857`) đứng sau; mô tả loại màn hình cũng ghi "chia 2 nhóm: Thông tin doanh nghiệp + Tài khoản" đúng thứ tự đó (`:1828`). Web xếp ngược (Tài khoản trên, DN dưới) → lệch. Lý do nghiệp vụ cần đúng thứ tự: ô "Tên đăng nhập" (readonly) tự điền theo MST khai ở phần DN; đặt Tài khoản lên trên thì ô này trống, vô nghĩa tới khi cuộn xuống nhập MST.
**(2) Đối tác yêu cầu có khác SRS không? Khác gì?** [KHÔNG] — đối tác KHÔNG ghi ý này trong ô Kết quả thực tế. Ô QLDKTK_02 chỉ nêu "thiếu Tệp đính kèm" + "Doanh thu (VNĐ) khác thiết kế (SRS tên là Doanh thu năm)"; ô QLDKTK_03 chỉ nêu "thiếu Tên đăng nhập" + "thừa 2 ô Họ tên/SĐT người đăng ký" — không ô nào nhắc thứ tự nhóm. Đây là phát hiện thêm của BA khi rà màn hình.
**(3) Yêu cầu đó có bắt buộc cho luồng nghiệp vụ không?** [CÓ → phải sửa] — web sai so với SRS, Dev FE sắp lại: khối "Thông tin doanh nghiệp" trên, "Tài khoản đăng nhập" dưới, khớp SCR-VIII-08. Không cần sửa SRS. Đồng bộ: `srs-fr-10-quan-tri.md:1838` (Nhóm 1) · `:1857` (Nhóm 2) · `:1828` (loại màn hình).
**→ Kết luận: Loại 1 — Lỗi phần mềm, Dev sửa theo SRS: sắp lại thứ tự — khối "Thông tin doanh nghiệp" trên, "Tài khoản đăng nhập" dưới, khớp SCR-VIII-08.** **✅ BA duyệt 2026-07-24.**

---

### Phát hiện 2.2a — "Tên viết tắt", "Ngày cấp ĐKKD", "Fax" + khối "Quy mô" (Số LĐ nữ, Số LĐ khuyết tật, Nữ làm chủ)

**(1) Phần mềm đúng SRS chưa?** [SRS thiếu (liệt kê)] — Cả 6 ô/khối đều là thuộc tính hợp lệ của entity DOANH_NGHIEP: `ten_viet_tat` (`srs-fr-07-doanh-nghiep.md:688`), `ngay_cap_dkkd` (`:691`), `fax` (`:697`), `so_lao_dong_nu` (`:704`), `so_lao_dong_khuyet_tat` (`:705`), `la_nu_lam_chu` (`:706`); form CB Nghiệp vụ SCR-V.III-03 đã có "Ngày cấp ĐKKD" (`srs-fr-07:474`), "Fax" (`:487`) và 3 trường ưu tiên "Phụ nữ làm chủ / Số LĐ nữ / Số LĐ khuyết tật" (`srs-fr-07:488`–`:490`). FR-VIII-22 cam kết form đăng ký khai "full thông tin entity DOANH_NGHIEP (giống Inputs FR-V.III-01)" (`srs-fr-10-quan-tri.md:1024`). Vậy web LÀM ĐÚNG cam kết đó; SRS chỉ thiếu ở bảng liệt kê 18 trường FR-VIII-22 — thiếu sót ở phần liệt kê, không phải ô thừa sai.
**(2) Đối tác yêu cầu có khác SRS không? Khác gì?** [KHÔNG] — đối tác chỉ nêu thiếu Tệp đính kèm + tên trường Doanh thu (QLDKTK_02); 6 ô/khối này là phát hiện thêm của BA. Đều là thông tin tổ chức (số liệu tổng hợp cấp DN), không phải dữ liệu định danh cá nhân, không thuộc Luật số 91/2025/QH15 — khác hẳn toggle công khai ở 2.2b. *(Danh mục nội dung Giấy chứng nhận ĐKDN theo Luật Doanh nghiệp 2020 làm căn cứ mạnh hơn — cần CĐT xác nhận với văn bản gốc.)*
**(3) Yêu cầu đó có bắt buộc cho luồng nghiệp vụ không?** [CÓ → phải sửa (bổ sung SRS)] — 3 trường ưu tiên là đầu vào quy tắc chấm điểm phân công vụ việc BR-CALC-07 (NĐ 55/2019/NĐ-CP Điều 4, `srs-v3.5.md:5520`) → rất nên thu ngay từ bước đăng ký. Hành động: giữ cả 6 trường, bổ sung `ten_viet_tat`/`ngay_cap_dkkd`/`fax`/`so_lao_dong_nu`/`so_lao_dong_khuyet_tat`/`la_nu_lam_chu` vào Inputs FR-VIII-22 (`srs-fr-10-quan-tri.md:1037`–`:1054`) + SCR-VIII-08 Nhóm 1 (`:1838`–`:1856`), tất cả để "Tùy chọn"; `so_lao_dong_nu`/`so_lao_dong_khuyet_tat` ràng buộc `≥ 0 và ≤ so_lao_dong` (CHECK entity `srs-fr-07-doanh-nghiep.md:713`–`:714`, lỗi ERR-DN-OWN-03 `srs-fr-07:394`); ghi chú 3 trường ưu tiên là đầu vào BR-CALC-07; cập nhật đếm trường AC (`:1098`), gộp chung tổng với 2 trường người liên hệ ở QLDKTK_03 khi chốt.
**→ Kết luận: Loại 2 — Cập nhật SRS rồi Dev làm theo SRS mới: bổ sung 6 trường (`ten_viet_tat`/`ngay_cap_dkkd`/`fax`/`so_lao_dong_nu`/`so_lao_dong_khuyet_tat`/`la_nu_lam_chu`) vào Inputs FR-VIII-22 + SCR-VIII-08 Nhóm 1, để "Tùy chọn".**
> **Phương án xử lý (cập nhật SRS):** `srs-fr-10-quan-tri.md:1037`–`:1054` (§Inputs FR-VIII-22, bảng thông tin DN) + `:1838`–`:1856` (SCR-VIII-08 Nhóm 1) — thêm 6 trường `ten_viet_tat` / `ngay_cap_dkkd` / `fax` / `so_lao_dong_nu` / `so_lao_dong_khuyet_tat` / `la_nu_lam_chu`, tất cả để "Tùy chọn"; 2 trường lao động `so_lao_dong_nu` và `so_lao_dong_khuyet_tat` ràng buộc `≥ 0 và ≤ so_lao_dong`; ghi chú 3 trường ưu tiên (`so_lao_dong_nu` / `so_lao_dong_khuyet_tat` / `la_nu_lam_chu`) là đầu vào quy tắc chấm điểm phân công BR-CALC-07. Cập nhật số đếm trường ở AC `:1098` (gộp chung với 2 trường "Người liên hệ tài khoản" của QLDKTK_03 nếu CĐT duyệt cùng lúc). Dev bổ sung 6 ô vào Nhóm 1 form đăng ký DN theo SRS mới. **✅ BA duyệt 2026-07-24.**

---

### Phát hiện 2.2b — Toggle "Cho phép công khai thông tin"

**(1) Phần mềm đúng SRS chưa?** [SRS thiếu/im lặng] — Rà nguyên bảng thuộc tính entity DOANH_NGHIEP (`srs-fr-07-doanh-nghiep.md:683`–`:718`) không có `cong_khai`/`cho_phep_cong_khai` (khác hẳn `la_nu_lam_chu`/`so_lao_dong_nu`/`so_lao_dong_khuyet_tat` ở 2.2a — các trường này CÓ trong entity); FR-VIII-22 và SCR-VIII-08 cũng không nhắc việc công khai; CSV không có UC/giao dịch nào cho DN đồng ý công khai hồ sơ ở bước đăng ký. SRS im lặng hoàn toàn về ý nghĩa (công khai trường nào, cho ai xem, DN rút lại thế nào) → không kết luận đúng/sai được.
**(2) Đối tác yêu cầu có khác SRS không? Khác gì?** [KHÔNG] — nút này KHÔNG do đối tác ghi trong ô Kết quả thực tế; là phát hiện thêm của BA. Đây là một nghiệp vụ MỚI, chưa được định nghĩa; phân biệt rõ với nút "Nữ làm chủ" (có căn cứ entity `la_nu_lam_chu` → thuộc 2.2a).
**(3) Yêu cầu đó có bắt buộc cho luồng nghiệp vụ không?** [KHÔNG → yêu cầu cải tiến] — đăng ký không cần công khai. Hơn nữa form còn thu "Họ tên/SĐT người đăng ký" là dữ liệu cá nhân (Luật số 91/2025/QH15, thay Nghị định 13/2023/NĐ-CP), một nút "cho phép công khai" khi chưa rõ phạm vi có thể kéo theo công khai cả dữ liệu cá nhân — sự đồng ý này chưa "được thông báo đầy đủ, cho mục đích rõ ràng" nên chưa đủ điều kiện pháp lý, gây rủi ro cho cả DN lẫn CĐT.

**✅ BA chốt 2026-07-24:** BỎ toggle "Cho phép công khai thông tin" — Dev gỡ/ẩn khỏi form đăng ký DN; KHÔNG đưa vào SRS (nghiệp vụ công khai chưa được định nghĩa). Nếu sau này CĐT muốn tính năng công khai thì đặc tả riêng — khi đó mới cần trả lời: công khai trường nào / cho ai xem / DN rút lại đồng ý thế nào. *(Số Điều/Khoản Luật 91/2025/QH15 và Nghị định 356/2025 — cần CĐT xác nhận với văn bản gốc.)*
**→ Kết luận: Loại 3 — Không đưa vào SRS, đề nghị đối tác đưa vào danh sách yêu cầu cải tiến nếu cần: nghiệp vụ công khai chưa được định nghĩa. BA đã chốt BỎ toggle "Cho phép công khai thông tin" — Dev gỡ/ẩn khỏi form đăng ký (2026-07-24).**

> **Phản hồi gửi đối tác:** [Lý do] Nút "Cho phép công khai thông tin" hiện không nằm trong đặc tả và nghiệp vụ công khai chưa được định nghĩa (công khai trường nào, cho ai xem, doanh nghiệp rút lại đồng ý thế nào); biểu mẫu còn thu thập dữ liệu cá nhân của người đăng ký nên một nút công khai chưa rõ phạm vi có thể kéo theo rủi ro pháp lý về bảo vệ dữ liệu cá nhân. Vì vậy phần mềm sẽ bỏ nút này khỏi biểu mẫu đăng ký doanh nghiệp. Kính đề nghị Quý đối tác ghi nhận việc bỏ nút này; nếu sau này cần tính năng công khai, kính đề nghị đưa vào danh sách yêu cầu cải tiến.

---

*File lập: 23/07/2026 — BA Mary phản hồi phiếu QLDKTK tuần 3.*
