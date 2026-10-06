# Phản hồi BA — Báo cáo thống kê (phiếu ba-confirmation-needed-bctk.md)

**Phiếu nguồn:** `ba-confirmation-needed-bctk.md` (UAT tuần 3, module Báo cáo Thống kê, 6 nhóm — 25 test case).
**Nguồn đối chiếu:**
- SRS chính: `_bmad-output/planning-artifacts/srs-v3.5/srs-fr-11-bao-cao.md`
- CSV baseline: `docs/Input/Danh sách transaction_v1.1_2026-03-27.csv` (STT 124–146 = 23 loại báo cáo thống kê)

**Ngày lập:** 23/07/2026.

---

## Ghi chú phương pháp (đọc trước)

> **Trạng thái & khuôn trình bày:** Mỗi mục trình bày theo khuôn **3 câu hỏi quyết định** — **(1)** Phần mềm đúng SRS chưa? **(2)** Đối tác yêu cầu có khác SRS không, khác gì? **(3)** Yêu cầu đó có bắt buộc cho luồng nghiệp vụ không? — rồi suy ra **Kết luận Loại 1/2/3**. Logic: phần mềm SAI SRS → Loại 1 (Dev fix); đúng SRS + đối tác khác + KHÔNG bắt buộc cho luồng → Loại 3 (đưa vào cải tiến, defer vì đợt fix đang gấp); đúng SRS + đối tác khác + BẮT BUỘC cho luồng, hoặc SRS thiếu/mâu thuẫn + cần cho luồng → Loại 2 (update SRS + Dev). Mỗi case tự mang dấu quyết định (✅) ngay tại dòng Kết luận của nó; điểm còn đánh dấu **[CHỜ CĐT]** chỉ chờ Chủ đầu tư xác nhận biểu mẫu luật định trước khi có thể nâng Loại.

- **3 cụm cùng chung một cách phân loại:**
  1. **Thẻ chỉ số tổng hợp (KPI card)** — xuyên suốt VVTTG_02, CPCTHTTDVQL_03, CPCTHTTLHDN_03, CTTDVQL_02, CTTLV_03.
  2. **Chiều/trục của biểu đồ** — CLDTBDDDR_04, LDTBDDDR_04, CGTVPL_04, CLDTBDPL_04.
  3. **Trục phụ cho biểu đồ trộn metric khác đơn vị (tiền / đếm / %)** — CPCTHTTLHDN_04, CPCTHTTTG_03.

  → 3 cụm này theo quy tắc đều là **Loại 3** (app đúng SRS + không bắt buộc luồng); chỉ nâng Loại 2 nếu CĐT xác nhận yêu cầu bắt buộc (vd biểu mẫu TT17). Riêng CLDTBDPL_04 là **Loại 2** do trùng nhãn.

**Lưu ý cách phân loại ô số tổng (đã đánh giá lại 2026-07-24):** Phải tách 2 loại ô số tổng:
- **Ô ĐẾM số bản ghi** (Tổng vụ việc / Tổng hồ sơ / Tổng chương trình): chính là trường **`tong_ban_ghi` = "Tổng số bản ghi"** mà **mẫu chung TPL-REPORT-FULL bắt buộc mọi báo cáo phải có, "Luôn"** (`srs-fr-11-bao-cao.md:57`, `:100`; mọi FR-IX đều kế thừa mẫu này) → **ô này ĐÚNG SRS, không phải app tự thêm.** (Ghi chú cũ nói "tong_ban_ghi không phải các trị tổng đặc thù" — sai ở chỗ gộp cả ô đếm; ô đếm chính là tong_ban_ghi.)
- **Ô TIỀN / dẫn xuất** (Tổng chi phí / Tổng ngân sách / Tổng DN tham gia): là tổng cộng toàn báo cáo, mà §Output đặc thù của các báo cáo này chỉ khai các trị đó **theo từng dòng** (từng đơn vị/loại DN/lĩnh vực — `:754-758`, `:833-839`, `:941-945`, `:981-984`), **chưa khai trị tổng toàn báo cáo** → ô này mới là phần chưa có trong §Output; BA chốt: chấp nhận (giữ) hay bổ sung trị tổng vào §Output.
→ Vậy 5 case ô số tổng: **VVTTG_02 = ĐÚNG SRS hoàn toàn** (chỉ có 1 ô đếm = tong_ban_ghi); 4 case còn lại (CPCTHTTDVQL_03, CPCTHTTLHDN_03, CTTDVQL_02, CTTLV_03) = **ô đếm đúng SRS (giữ) + ô tiền là phần dôi không vi phạm → Loại 3 (giữ app, đối tác cập nhật Expected, KHÔNG tự bổ sung §Output; chỉ nâng Loại 2 nếu CĐT xác nhận biểu mẫu TT17 bắt buộc có dòng Tổng cộng)**. *(Đã đối chiếu ảnh evidence 2026-07-24: mỗi case hiện đúng 2 ô — 1 ô ĐẾM (CPCTHTTDVQL_03/CPCTHTTLHDN_03: "Tổng hồ sơ"=25; CTTDVQL_02/CTTLV_03: "Tổng chương trình"=5) + 1 ô TIỀN/DẪN XUẤT (Tổng chi phí=226.308.268; Tổng ngân sách=0; Tổng DN tham gia=0).)*

---

## Nhóm 1 — DISPLAY họ Vụ việc

### SLHDVM_03 — Bảng "theo đơn vị" của BC Số lượng hỏi đáp

**(1) Phần mềm đúng SRS chưa?** **ĐÚNG.** Bảng "theo đơn vị" của BC Số lượng hỏi đáp (FR-IX-01 / UC124) theo SRS chỉ gồm 3 cột: mã đơn vị, tên đơn vị, số lượng — không có cột "Đã trả lời" hay "Tỷ lệ (%)" ở mức đơn vị (`srs-fr-11-bao-cao.md:166`). CSV gốc STT124 cũng không nhắc 2 cột này (`csv:1096`).
**(2) Đối tác yêu cầu có khác SRS không? Khác gì?** **CÓ.** Đối tác muốn thêm 2 cột "Đã trả lời" và "Tỷ lệ (%)" theo bản thiết kế riêng của họ — 2 cột này nằm ngoài §Output SRS.
**(3) Yêu cầu đó có bắt buộc cho luồng nghiệp vụ không?** **KHÔNG.** Bảng đã đủ số liệu cho luồng; 2 cột thêm chỉ là cách xem khác → đưa vào yêu cầu cải tiến (kèm bổ sung §Output FR-IX-01), không xử như lỗi. Đối tác đọc lại SRS bản 23/6 và cập nhật Kết quả mong đợi theo §Output (Đơn vị + Số lượng).
**→ Kết luận: Loại 3 — Không sửa, đề nghị đối tác đưa vào danh sách yêu cầu cải tiến; giữ nguyên SRS, đề nghị đối tác đọc lại SRS bản 23/6.** ✅ Đã chốt (2026-07-23).
> **Phản hồi gửi đối tác:** [Lý do] Bảng "theo đơn vị" của báo cáo Số lượng hỏi đáp đã hiển thị đúng ba cột như đặc tả đã thống nhất: mã đơn vị, tên đơn vị và số lượng. Hai cột "Đã trả lời" và "Tỷ lệ (%)" ở mức đơn vị nằm ngoài phạm vi đặc tả và không cần thiết để bảo đảm đủ số liệu cho nghiệp vụ. [Nhận định] Kính đề nghị Quý đối tác đưa nội dung này vào danh sách yêu cầu cải tiến.

---

### VVDHT_03 — "Chỉ số tổng hợp nhanh" các mức SLA

**(1) Phần mềm đúng SRS chưa?** **ĐÚNG.** BC Vụ việc đang hỗ trợ (FR-IX-03 / UC126) theo SRS luôn hiện 4 con số về hạn xử lý: tổng đang xử lý, bình thường, cảnh báo, quá hạn (`:257-262`). "Quá hạn nghiêm trọng" chỉ là một lựa chọn trong bộ lọc, không nằm trong dữ liệu báo cáo phải hiện (`:245`); SCR-IX-01 không có thành phần "ô số tổng" (`:1039-1054`). App đã hiện đủ mọi mức hạn ở bảng "Mức SLA" + biểu đồ cột (phản ánh "thiếu chỉ số" không tái hiện).
**(2) Đối tác yêu cầu có khác SRS không? Khác gì?** **CÓ.** Đối tác muốn mỗi mức (Sắp hết hạn / Quá hạn / Quá hạn nghiêm trọng) thành một ô số tổng riêng ở đầu màn (thẻ), thay vì trình bày bằng bảng/biểu đồ như hiện tại.
**(3) Yêu cầu đó có bắt buộc cho luồng nghiệp vụ không?** **KHÔNG.** Số liệu đã đủ, chỉ khác cách trình bày → đưa vào yêu cầu cải tiến: thêm component "Khối chỉ số" vào SCR-IX-01 (`:1039-1054`) + thêm "Quá hạn nghiêm trọng" vào §Output. Đối tác cập nhật Kết quả mong đợi (mức SLA ở bảng + biểu đồ cột là đủ theo §Output).
**→ Kết luận: Loại 3 — Không sửa, đề nghị đối tác đưa vào danh sách yêu cầu cải tiến.** ✅ Đã chốt (2026-07-23).
> **Phản hồi gửi đối tác:** [Lý do] Báo cáo Vụ việc đang hỗ trợ đã thể hiện đầy đủ các mức hạn xử lý qua bảng mức hạn xử lý và biểu đồ cột đúng như đặc tả, trong đó "Quá hạn nghiêm trọng" vốn chỉ là một lựa chọn trong bộ lọc. Việc trình bày mỗi mức thành một ô số tổng riêng chỉ là một cách hiển thị khác, không ảnh hưởng đến tính đầy đủ của số liệu và không bắt buộc cho nghiệp vụ. [Nhận định] Kính đề nghị Quý đối tác đưa nội dung này vào danh sách yêu cầu cải tiến.
---

### VVTTG_02 — Ô "Tổng vụ việc toàn kỳ" trên báo cáo Vụ việc theo thời gian

**(1) Phần mềm đúng SRS chưa?** **ĐÚNG.** BC Vụ việc theo thời gian (FR-IX-05 / UC128) ghi rõ "Kế thừa mẫu chung TPL-REPORT-FULL" (`srs-fr-11-bao-cao.md:327`); mẫu chung này (áp cho cả 23 báo cáo) có trường `tong_ban_ghi` = "Tổng số bản ghi", điều kiện "Luôn" (`:57`, `:100`). Với báo cáo vụ việc, "tổng số bản ghi" chính là tổng số vụ việc → ô "Tổng vụ việc toàn kỳ" là trường `tong_ban_ghi` mà SRS bắt buộc, không phải app tự thêm.
**(2) Đối tác yêu cầu có khác SRS không? Khác gì?** **CÓ (và trái SRS).** Kết quả mong đợi của đối tác ghi "Không có chỉ số tổng hợp riêng" và chấm Fail vì coi ô số tổng là thừa. Kỳ vọng này vừa trái SRS, vừa trái chính test case VVTTG_01 của đối tác (VVTTG_01 kỳ vọng khu vực kết quả gồm "các chỉ số tổng hợp, biểu đồ và bảng").
**(3) Yêu cầu đó có bắt buộc cho luồng nghiệp vụ không?** **KHÔNG (kỳ vọng không hợp lệ).** Phần mềm đúng đặc tả → không sửa; đề nghị đối tác sửa Kết quả mong đợi VVTTG_02 thành "có ô Tổng vụ việc toàn kỳ" cho khớp SRS (trường `tong_ban_ghi` bắt buộc của mẫu báo cáo chung).
**→ Kết luận: Loại 3 — Không sửa, đề nghị đối tác đưa vào danh sách yêu cầu cải tiến; phần mềm ĐÚNG SRS, đề nghị đối tác sửa Kết quả mong đợi.** ✅ Đã đánh giá lại (2026-07-24) dựa trên SRS + ảnh evidence VVTTG_02.jpg.
> **Phản hồi gửi đối tác:** [Lý do] Ô "Tổng vụ việc toàn kỳ" chính là chỉ tiêu "Tổng số bản ghi" mà mọi báo cáo trong hệ thống đều bắt buộc phải hiển thị, nên phần mềm đã làm đúng đặc tả. Kỳ vọng "không có chỉ số tổng hợp riêng" vừa trái với đặc tả, vừa không nhất quán với chính kịch bản kiểm thử liền trước (VVTTG_01) của Quý đối tác. [Nhận định] Kính đề nghị Quý đối tác đưa nội dung này vào danh sách yêu cầu cải tiến.

---

## Nhóm 2 — DISPLAY họ Đào tạo / CG-TVV / Đánh giá (cụm "chiều/trục biểu đồ")

> **Bản chất chung 4 case:** Bảng Mapping 23 loại BC (`srs-fr-11-bao-cao.md:1058-1082`) chỉ ghi **LOẠI biểu đồ** (Bar / Donut / Line...), KHÔNG quy định **chiều dữ liệu của trục** (đơn vị / hình thức / loại / khóa học). SCR-IX-01 item 10 cũng chỉ liệt kê loại biểu đồ, không định trục (`srs-fr-11-bao-cao.md:1050`). Vì vậy việc app chọn trục = đơn vị KHÔNG trái điều khoản nào → không phải lỗi. Đây là khoảng trống đặc tả → BA nên bổ sung 1 cột "Chiều/trục biểu đồ" vào bảng Mapping và quyết chung cho cả họ.

### CLDTBDDDR_04 — BC Lớp đào tạo đang diễn ra: trục đơn vị vs hình thức + đòi thêm biểu đồ xu hướng

**(1) Phần mềm đúng SRS chưa?** **ĐÚNG.** BC Lớp đào tạo đang diễn ra (FR-IX-06 / UC129) — bảng Mapping chỉ ghi dùng biểu đồ cột (`srs-fr-11-bao-cao.md:1065`), không quy định trục. §Output có đủ số liệu theo hình thức/đơn vị/lĩnh vực (`:374-381`), mô tả nêu cả 3 cách chia (`:355`); app vẽ trục = đơn vị, hình thức thể hiện bằng màu → không trái. Là báo cáo chụp-một-thời-điểm nên Mapping không kèm biểu đồ đường xu hướng (khác FR-IX-07 vốn có cả cột lẫn đường). Bảng: §Output `theo_don_vi[]` chỉ khai `{don_vi, ten, so_luong}` (`:379`), KHÔNG có "Số học viên" ở mức đơn vị (`so_hv` chỉ nằm trong `ds_khoa_hoc[]` — `:381`); app hiện Trực tuyến/Trực tiếp/Tổng số là superset của §Output. Pháp lý: TT 17/2025/TT-BTP Điều 3.1.b chỉ quy định cách ghi biểu mẫu luật định (Phụ lục IV), không ràng buộc trục biểu đồ trên phần mềm cũng không buộc báo cáo snapshot kèm biểu đồ xu hướng.
**(2) Đối tác yêu cầu có khác SRS không? Khác gì?** **CÓ (3 ý).** (a) muốn cột gom theo hình thức học thay vì theo đơn vị; (b) muốn thêm biểu đồ đường thể hiện xu hướng qua thời gian; (c) muốn bảng có cột "Số khóa, Số học viên" ở mức đơn vị. Cả 3 là thiết kế riêng của đối tác, ngoài §Output.
**(3) Yêu cầu đó có bắt buộc cho luồng nghiệp vụ không?** **KHÔNG (cả 3 ý).** → đưa vào yêu cầu cải tiến: (a) văn bản hoá trục = đơn vị bằng cột "Chiều/trục biểu đồ" trong Mapping (chỉ ghi rõ đặc tả, không đổi app); (b) nếu CĐT muốn xu hướng qua các kỳ → đổi Mapping UC129 có Trend + thêm `theo_ky[]` vào §Output FR-IX-06; (c) nếu muốn "Số học viên" mức đơn vị → cải tiến. Đối tác cập nhật Kết quả mong đợi cho khớp SRS.
**→ Kết luận: Loại 3 — Không sửa, đề nghị đối tác đưa vào danh sách yêu cầu cải tiến; phần mềm đúng SRS, các mong muốn của đối tác đưa vào yêu cầu cải tiến.** ✅ Đã chốt (2026-07-24).
> **Phản hồi gửi đối tác:** [Lý do] Đặc tả của báo cáo Lớp đào tạo đang diễn ra chỉ quy định dùng biểu đồ cột chứ không ràng buộc trục biểu đồ phải chia theo chiều nào, nên việc phần mềm vẽ trục theo đơn vị và phân biệt hình thức học bằng màu là hợp lệ. Các mong muốn đổi trục theo hình thức học, thêm biểu đồ đường thể hiện xu hướng và thêm cột "Số học viên" ở mức đơn vị đều nằm ngoài đặc tả và không bắt buộc cho nghiệp vụ. [Nhận định] Kính đề nghị Quý đối tác đưa nội dung này vào danh sách yêu cầu cải tiến.

---

### LDTBDDDR_04 — Biểu đồ cột xếp theo đơn vị hay theo cách học (BC Lớp đào tạo đã diễn ra)

**(1) Phần mềm đúng SRS chưa?** **ĐÚNG.** SRS chỉ yêu cầu báo cáo này (FR-IX-07 / UC130) dùng biểu đồ cột + biểu đồ đường (`srs-fr-11-bao-cao.md:1066`), KHÔNG quy định cột phải xếp theo chiều nào. Phần mềm có đủ số liệu theo đơn vị và theo cách học (`:416-422`): vẽ cột theo đơn vị, cách học (trực tuyến/trực tiếp) phân biệt bằng màu.

**(2) Đối tác yêu cầu có khác SRS không? Khác gì?** **CÓ.** Đối tác muốn mỗi cột là một **cách học** (Trực tuyến / Trực tiếp); phần mềm đang để mỗi cột là một **đơn vị**. Cùng số liệu, chỉ khác chiều xếp cột — SRS không đứng về bên nào. *(Đối tác đính kèm nhầm ảnh của báo cáo "đang diễn ra".)*

**(3) Yêu cầu đó có bắt buộc cho luồng nghiệp vụ không?** **KHÔNG.** Xếp cột theo chiều nào cũng không ảnh hưởng luồng nghiệp vụ hay tính đúng của số liệu — thuần là cách trình bày. → **Đưa vào danh sách yêu cầu cải tiến** (không fix trong đợt gấp); đối tác cập nhật Kết quả mong đợi cho khớp SRS.

**→ Kết luận: Loại 3 — Không sửa, đề nghị đối tác đưa vào danh sách yêu cầu cải tiến.** **✅ BA duyệt 2026-07-24.**
> **Phản hồi gửi đối tác:** [Lý do] Đặc tả của báo cáo Lớp đào tạo đã diễn ra chỉ yêu cầu có biểu đồ cột và biểu đồ đường, không quy định cột phải xếp theo chiều nào, nên việc phần mềm để mỗi cột là một đơn vị và phân biệt cách học bằng màu là hợp lệ. Việc đổi mỗi cột thành một cách học chỉ là khác cách trình bày, không ảnh hưởng đến số liệu hay nghiệp vụ. [Nhận định] Kính đề nghị Quý đối tác đưa nội dung này vào danh sách yêu cầu cải tiến.

---

### CGTVPL_04 — BC Số lượng CG/TVV: donut theo đơn vị vs loại; "biểu đồ cột không hiển thị" không tái hiện

**(1) Phần mềm đúng SRS chưa?** **ĐÚNG (SRS im lặng về chiều donut).** BC Số lượng chuyên gia/tư vấn viên (FR-IX-08 / UC131) — bảng Mapping ghi dùng biểu đồ tròn + biểu đồ cột (`srs-fr-11-bao-cao.md:1067`), không nói donut chia theo cách nào. §Output đã thể hiện cách chia theo loại qua các ô số tổng TVV/CG (Số tư vấn viên = 5, Số chuyên gia = 0) và bảng theo đơn vị (`:458-466`); app vẽ donut theo đơn vị, biểu đồ cột CÓ render → ý phụ "biểu đồ cột không hiển thị" KHÔNG tái hiện. Pháp lý: TT 17/2025/TT-BTP Điều 3.1.b chỉ ràng buộc biểu mẫu luật định, không ràng chiều donut.
**(2) Đối tác yêu cầu có khác SRS không? Khác gì?** **CÓ.** Đối tác muốn biểu đồ tròn chia theo LOẠI (tư vấn viên/chuyên gia); phần mềm đang chia theo đơn vị.
**(3) Yêu cầu đó có bắt buộc cho luồng nghiệp vụ không?** Về luồng thì không chặn — chiều theo loại đã có sẵn ở ô số tổng TVV/CG và bảng theo đơn vị; biểu đồ tròn vẽ theo đơn vị là phần SRS im lặng, **KHÔNG vi phạm đặc tả**. Đối tác đòi đổi donut sang chia theo LOẠI → **KHÔNG bắt buộc cho luồng nghiệp vụ** → Loại 3. Giữ nguyên phần mềm; đề nghị đối tác cập nhật Kết quả mong đợi; nếu đối tác vẫn muốn đổi chiều donut thì ghi vào yêu cầu cải tiến. **KHÔNG tự bổ sung §Output/Mapping trong đợt này.**
**→ Kết luận: Loại 3 — Không sửa, đề nghị đối tác đưa vào danh sách yêu cầu cải tiến; phần mềm đúng SRS, đề nghị đối tác cập nhật Kết quả mong đợi / đưa vào yêu cầu cải tiến. Ý phụ "biểu đồ cột không hiển thị" đóng vì KHÔNG tái hiện.** **✅ BA duyệt 2026-07-24.** (Lỗi theo lĩnh vực đã log riêng ở bug-report-bctk-batch2.md.)
> **Phản hồi gửi đối tác:** [Lý do] Đặc tả của báo cáo Số lượng chuyên gia/tư vấn viên quy định dùng biểu đồ tròn và biểu đồ cột nhưng không ràng buộc biểu đồ tròn phải chia theo tiêu chí nào; số liệu theo loại (tư vấn viên/chuyên gia) cũng đã sẵn có ở các ô số tổng và bảng theo đơn vị, nên phần mềm không vi phạm đặc tả. Việc đổi biểu đồ tròn sang chia theo loại không bắt buộc cho nghiệp vụ. [Nhận định] Kính đề nghị Quý đối tác đưa nội dung này vào danh sách yêu cầu cải tiến.

---

### CLDTBDPL_04 — BC Chất lượng đào tạo: nhãn trục đơn vị vs khóa học; "thiếu đường điểm TB" không tái hiện

**(1) Phần mềm đúng SRS chưa?** **ĐÚNG về loại biểu đồ, nhưng có khiếm khuyết trình bày (trùng nhãn).** BC Chất lượng đào tạo (FR-IX-10 / UC133) — Mapping ghi dùng biểu đồ cột + biểu đồ đường (`srs-fr-11-bao-cao.md:1069`), không nói nhãn trục ghi theo gì; §Output luôn có số liệu cả theo khóa học lẫn theo đơn vị (`:544-548`). App render đúng Bar + Line và đường "Điểm TB" CÓ hiển thị → ý phụ "thiếu đường điểm TB" KHÔNG tái hiện (xem chính ảnh đối tác đính kèm). Khiếm khuyết: mỗi cột ứng với một khóa học (4 cột = 4 khóa) nhưng nhãn trục ghi tên đơn vị nên 2 khóa cùng "Cục Bổ trợ tư pháp" bị trùng nhãn. Pháp lý: TT 17/2025/TT-BTP Điều 3.1.b buộc ghi biểu sao cho số liệu không gây hiểu nhầm — để 2 điểm khác nhau trông y hệt là lỗi trình bày.
**(2) Đối tác yêu cầu có khác SRS không? Khác gì?** **CÓ.** Đối tác muốn nhãn trục gom theo khóa học; phần mềm đang ghi theo đơn vị.
**(3) Yêu cầu đó có bắt buộc cho luồng nghiệp vụ không?** **CÓ — cần sửa để số liệu đọc không nhầm.** Trùng nhãn khiến không phân biệt được điểm của khóa nào → **đổi nhãn trục theo khóa học (mã/tên khóa): update SRS (sửa riêng ô UC133 trong bảng Mapping — KHÔNG thêm cột mới, xem Phương án xử lý bên dưới) + Dev đổi nhãn trục.** Phương án tối thiểu nếu CĐT giữ nhãn đơn vị: phải khử trùng nhãn (nối thêm tên khóa/đợt sau tên đơn vị) rồi cập nhật kết quả mong đợi — giữ nhãn đơn vị trơn không chấp nhận được về trình bày.
**→ Kết luận: Loại 2 — Cập nhật SRS rồi Dev làm theo SRS mới: đổi nhãn trục biểu đồ theo khóa học (hết trùng nhãn); ý phụ "thiếu đường điểm TB" đóng vì KHÔNG tái hiện.** **✅ BA duyệt 2026-07-24.**
> **Phương án xử lý (cập nhật SRS):** **KHÔNG thêm cột mới** vào bảng Mapping (bảng có 23 dòng, thêm cột "Chiều/trục biểu đồ" sẽ tạo 22 ô trống vì chỉ UC133 có giá trị). Chỉ sửa RIÊNG ô của UC133 "BC Chất lượng đào tạo" trong bảng Mapping — `srs-fr-11-bao-cao.md:1074`, cột "Biểu đồ" hiện = "Bar + Line" → ghi rõ **"Bar + Line — nhãn trục theo khóa học (mã/tên khóa; khử trùng khi 2 khóa cùng đơn vị)"**. Sau khi SRS cập nhật, Dev FE đổi nhãn trục biểu đồ UC133 từ tên đơn vị sang theo khóa học để hết trùng nhãn khi hai khóa cùng tên đơn vị (Cục Bổ trợ tư pháp).

---

## Nhóm 3 — DISPLAY: Chi phí / Số lượng chương trình

### CPCTHTTDVQL_03 — BC Chi phí theo đơn vị: thẻ Tổng hồ sơ + Tổng chi phí

**(1) Phần mềm đúng SRS chưa?** **Ô ĐẾM đúng, ô TIỀN chưa khai §Output.** BC Chi phí theo đơn vị (FR-IX-16 / UC139) là bảng chéo hàng đơn vị × cột (số hồ sơ, tổng chi phí, chi phí trung bình). Thẻ **"Tổng hồ sơ" = trường `tong_ban_ghi`** ("Tổng số bản ghi", "Luôn") mà mẫu chung TPL-REPORT-FULL bắt buộc (`srs-fr-11-bao-cao.md:100`); với báo cáo chi phí, bản ghi = hồ sơ đã thanh toán (Processing chung bước 4, `:82`) → **"Tổng hồ sơ" ĐÚNG SRS, không phải app tự thêm.** Thẻ **"Tổng chi phí" (tiền):** §Output FR-IX-16 (`:752-758`) chỉ khai `tong_chi_phi` theo TỪNG hàng đơn vị (`:756`), **chưa khai trị tổng tiền toàn báo cáo** — không bị cấm nhưng SRS chưa mô tả (FR-IX-15/UC138 có con số tổng thật `:720-721` nhưng là báo cáo khác). Pháp lý: TT 17/2025/TT-BTP (đã xác minh) Điều 1.2.y (HTPLDN vào chế độ báo cáo thống kê ngành Tư pháp) + Điều 3.1.b (biểu mẫu phải có "phương pháp tính") → trị tổng phải được SRS ghi rõ mới thành yêu cầu chính thức. *Cần CĐT xác nhận* biểu mẫu HTPLDN của TT17 (Phụ lục I & IV) có dòng "Tổng cộng" hay không — chưa đối chiếu được số hiệu biểu mẫu từ văn bản gốc.
**(2) Đối tác yêu cầu có khác SRS không? Khác gì?** **CÓ.** Đối tác mong màn hình không có ô số tổng riêng; phần mềm hiện 2 thẻ ở đầu màn (Tổng hồ sơ + Tổng chi phí).
**(3) Yêu cầu đó có bắt buộc cho luồng nghiệp vụ không?** Thẻ ĐẾM "Tổng hồ sơ" = `tong_ban_ghi` bắt buộc → đúng SRS, giữ nguyên. Thẻ "Tổng chi phí" (tiền) là phần dôi, §Output chưa khai nhưng **KHÔNG vi phạm đặc tả**. Đối tác đòi gỡ thẻ số tổng → **KHÔNG bắt buộc cho luồng nghiệp vụ** → Loại 3. Giữ nguyên phần mềm; đề nghị đối tác cập nhật Kết quả mong đợi; nếu đối tác vẫn muốn gỡ thẻ thì ghi vào yêu cầu cải tiến. **KHÔNG tự bổ sung §Output/Mapping trong đợt này.**
**→ Kết luận: Loại 3 — Không sửa, đề nghị đối tác đưa vào danh sách yêu cầu cải tiến; phần mềm đúng SRS, đề nghị đối tác cập nhật Kết quả mong đợi / đưa vào yêu cầu cải tiến.** **✅ BA duyệt 2026-07-24.** [Chỉ nâng Loại 2 nếu CĐT xác nhận biểu mẫu TT17 bắt buộc dòng Tổng cộng.]
> **Phản hồi gửi đối tác:** [Lý do] Thẻ "Tổng hồ sơ" chính là chỉ tiêu "Tổng số bản ghi" bắt buộc của mọi báo cáo nên đúng đặc tả; còn thẻ "Tổng chi phí" tuy đặc tả báo cáo Chi phí theo đơn vị mới mô tả chi phí theo từng đơn vị nhưng đây là phần hiển thị thêm, không vi phạm đặc tả. Yêu cầu gỡ các thẻ số tổng ở đầu màn hình không bắt buộc cho nghiệp vụ. [Nhận định] Kính đề nghị Quý đối tác đưa nội dung này vào danh sách yêu cầu cải tiến.

---

### CPCTHTTLHDN_03 — BC Chi phí theo loại hình DN: thẻ Tổng hồ sơ + Tổng chi phí

**(1) Phần mềm đúng SRS chưa?** **Ô ĐẾM đúng, ô TIỀN chưa khai §Output.** BC Chi phí theo loại hình DN (FR-IX-18 / UC141) chia chi phí theo loại DN (siêu nhỏ/nhỏ/vừa), kèm mức hỗ trợ và so trần theo Nghị định 55. Thẻ **"Tổng hồ sơ" = `tong_ban_ghi`** ("Luôn", `srs-fr-11-bao-cao.md:100`; bản ghi chi phí = hồ sơ đã thanh toán, Processing chung bước 4 `:82`) → **ĐÚNG SRS.** Thẻ **"Tổng chi phí":** §Output FR-IX-18 (`:831-839`) chỉ khai `tong_chi_phi` theo TỪNG loại hình DN (`:837`), **chưa khai trị tổng tiền toàn báo cáo** (FR-IX-15/UC138 có con số tổng thật nhưng là báo cáo khác). Pháp lý: TT 17/2025/TT-BTP (đã xác minh) Điều 1.2.y + Điều 3.1.b ("phương pháp tính"); riêng báo cáo này còn so trần chi phí theo Nghị định 55/2019 nên một con số tổng chi phí toàn báo cáo càng có ý nghĩa đối chiếu. *Cần CĐT xác nhận* số hiệu biểu mẫu HTPLDN và dòng "Tổng cộng" ở Phụ lục I/IV văn bản gốc TT17.
**(2) Đối tác yêu cầu có khác SRS không? Khác gì?** **CÓ.** Đối tác mong không có ô số tổng riêng; phần mềm hiện 2 thẻ (Tổng hồ sơ + Tổng chi phí).
**(3) Yêu cầu đó có bắt buộc cho luồng nghiệp vụ không?** Thẻ ĐẾM "Tổng hồ sơ" = `tong_ban_ghi` bắt buộc → đúng SRS, giữ nguyên. Thẻ "Tổng chi phí" (tiền) là phần dôi, §Output chưa khai nhưng **KHÔNG vi phạm đặc tả**. Đối tác đòi gỡ thẻ số tổng → **KHÔNG bắt buộc cho luồng nghiệp vụ** → Loại 3. Giữ nguyên phần mềm; đề nghị đối tác cập nhật Kết quả mong đợi; nếu đối tác vẫn muốn gỡ thẻ thì ghi vào yêu cầu cải tiến. **KHÔNG tự bổ sung §Output/Mapping trong đợt này.**
**→ Kết luận: Loại 3 — Không sửa, đề nghị đối tác đưa vào danh sách yêu cầu cải tiến; phần mềm đúng SRS, đề nghị đối tác cập nhật Kết quả mong đợi / đưa vào yêu cầu cải tiến.** **✅ BA duyệt 2026-07-24.** [Chỉ nâng Loại 2 nếu CĐT xác nhận biểu mẫu TT17 bắt buộc dòng Tổng cộng.]
> **Phản hồi gửi đối tác:** [Lý do] Thẻ "Tổng hồ sơ" là chỉ tiêu "Tổng số bản ghi" bắt buộc của mọi báo cáo nên đúng đặc tả; còn thẻ "Tổng chi phí" là phần hiển thị thêm, không vi phạm đặc tả dù đặc tả báo cáo Chi phí theo loại hình doanh nghiệp mới mô tả chi phí theo từng loại hình doanh nghiệp. Yêu cầu bỏ các ô số tổng ở đầu màn hình không bắt buộc cho nghiệp vụ. [Nhận định] Kính đề nghị Quý đối tác đưa nội dung này vào danh sách yêu cầu cải tiến.

---

### CPCTHTTLHDN_04 — BC Chi phí theo loại hình DN: biểu đồ 6 metric; "trục tung toàn bộ 0"

**(1) Phần mềm đúng SRS chưa?** **ĐÚNG (SRS không định series).** FR-IX-18 / UC141 — Mapping ghi dùng biểu đồ cột nhóm, có bộ lọc "Loại DN" (`srs-fr-11-bao-cao.md:1077`), KHÔNG nói cột gom theo nhóm nào cũng không bảo vẽ cùng lúc 6 loại số liệu; SRS chỉ mô tả cột của bảng (`:831-839`) và bảng của app thì khớp. Claim "trục tung toàn bộ 0" KHÔNG đúng: các cột tiền vẫn có giá trị rõ, chỉ Số hồ sơ và Mức hỗ trợ (%) bị nén sát 0 do vẽ chung một trục với thang tiền — là vấn đề trình bày (trộn số liệu khác đơn vị lên 1 trục), không phải lỗi dữ liệu. Pháp lý: TT 17/2025/TT-BTP Điều 3.1.b chỉ ràng buộc số liệu và "phương pháp tính", không ràng kỹ thuật vẽ biểu đồ.
**(2) Đối tác yêu cầu có khác SRS không? Khác gì?** **CÓ (2 ý).** (1) biểu đồ đang vẽ cùng lúc nhiều loại số liệu (Chênh lệch, Số hồ sơ, Trần/hồ sơ, Trần chi phí, Tổng chi phí) mà "tài liệu không yêu cầu" — đối tác mong gom cột theo loại hình DN và mức hỗ trợ; (2) báo "trục dọc toàn bộ bằng 0" (không đúng thực tế).
**(3) Yêu cầu đó có bắt buộc cho luồng nghiệp vụ không?** Không phải lỗi dữ liệu. Biểu đồ trộn nhiều metric trên một trục, chuyện chọn series và trục phụ là phần SRS im lặng, **KHÔNG vi phạm đặc tả**. Đối tác đòi thu gọn series / đổi cách vẽ trục → **KHÔNG bắt buộc cho luồng nghiệp vụ** → Loại 3. Giữ nguyên phần mềm; đề nghị đối tác cập nhật Kết quả mong đợi; nếu đối tác vẫn muốn đổi thì ghi vào yêu cầu cải tiến. **KHÔNG tự bổ sung §Output/Mapping trong đợt này.**
**→ Kết luận: Loại 3 — Không sửa, đề nghị đối tác đưa vào danh sách yêu cầu cải tiến; phần mềm đúng SRS, đề nghị đối tác cập nhật Kết quả mong đợi / đưa vào yêu cầu cải tiến. Claim "trục tung toàn bộ 0" đóng vì không đúng (chỉ metric đếm/% bị nén do trộn scale).** **✅ BA duyệt 2026-07-24.**
> **Phản hồi gửi đối tác:** [Lý do] Đặc tả của báo cáo Chi phí theo loại hình doanh nghiệp không quy định biểu đồ phải vẽ những loại số liệu nào hay chia trục ra sao, nên phần mềm không trái đặc tả. Phản ánh "trục dọc toàn bộ bằng 0" không đúng thực tế: chỉ các cột thể hiện số đếm và tỷ lệ phần trăm bị nén sát 0 do vẽ chung một trục với thang tiền. Việc thu gọn bớt số liệu hay thêm một trục phụ không bắt buộc cho nghiệp vụ. [Nhận định] Kính đề nghị Quý đối tác đưa nội dung này vào danh sách yêu cầu cải tiến.

---

### CPCTHTTTG_03 — BC Chi phí theo thời gian: "trục tung toàn bộ 0"

**(1) Phần mềm đúng SRS chưa?** **ĐÚNG.** BC Chi phí theo thời gian (FR-IX-19 / UC142) — Mapping ghi dùng biểu đồ đường diễn biến (`srs-fr-11-bao-cao.md:1078`); §Output đưa vào biểu đồ cả tổng chi phí lẫn số hồ sơ theo từng kỳ (`:869-871`) nên vẽ 2 đường là khớp SRS (SRS không quy định phải tách trục). Claim "trục tung toàn bộ 0" KHÔNG đúng: đường Tổng chi phí ở đỉnh trục, chỉ đường Số hồ sơ bị nén sát 0 do chung trục thang tiền. Đối tác chọn Kỳ = Năm nên biểu đồ chỉ 1 điểm (2026) là đúng bộ lọc (nghiệm thu "12 tháng thì 12 điểm" — `:874`). Pháp lý: TT 17/2025/TT-BTP (đã xác minh) Điều 3.3 (kỳ báo cáo sơ bộ 6 tháng / sơ bộ năm / tròn năm) → "Kỳ = Năm" 1 điểm là đúng báo cáo tròn năm; luật không quy định cách chia trục.
**(2) Đối tác yêu cầu có khác SRS không? Khác gì?** **KHÔNG khác đặc tả — chỉ là claim "số liệu ở trục dọc toàn bộ bằng 0"** (không đúng thực tế).
**(3) Yêu cầu đó có bắt buộc cho luồng nghiệp vụ không?** Không phải lỗi dữ liệu. Việc tách trục phụ cho Số hồ sơ trên biểu đồ trend là phần SRS im lặng, **KHÔNG vi phạm đặc tả**. Đối tác đòi đổi cách vẽ trục → **KHÔNG bắt buộc cho luồng nghiệp vụ** → Loại 3. Giữ nguyên phần mềm; đề nghị đối tác cập nhật Kết quả mong đợi; nếu đối tác vẫn muốn đổi thì ghi vào yêu cầu cải tiến. **KHÔNG tự bổ sung §Output/Mapping trong đợt này.** Riêng thẻ "Tổng chi phí toàn kỳ" = `tong_chi_phi_ky` đã khai §Output FR-IX-19 (`:871`) nên hợp lệ — giữ nguyên; thẻ "Tổng hồ sơ toàn kỳ" = `tong_ban_ghi` cũng có căn cứ SRS.
**→ Kết luận: Loại 3 — Không sửa, đề nghị đối tác đưa vào danh sách yêu cầu cải tiến; phần mềm đúng SRS, đề nghị đối tác cập nhật Kết quả mong đợi / đưa vào yêu cầu cải tiến. Claim "trục tung toàn bộ 0" đóng vì không đúng.** **✅ BA duyệt 2026-07-24.**
> **Phản hồi gửi đối tác:** [Lý do] Biểu đồ đường của báo cáo Chi phí theo thời gian vẽ cả tổng chi phí lẫn số hồ sơ theo từng kỳ đúng đặc tả, và việc chọn kỳ thống kê theo năm cho ra một điểm dữ liệu (năm 2026) là đúng theo bộ lọc. Phản ánh "trục dọc toàn bộ bằng 0" không đúng thực tế: chỉ đường Số hồ sơ bị nén sát 0 do dùng chung trục với thang tiền. Việc tách một trục phụ riêng cho đường Số hồ sơ không bắt buộc cho nghiệp vụ. [Nhận định] Kính đề nghị Quý đối tác đưa nội dung này vào danh sách yêu cầu cải tiến.

---

## Nhóm 4 — Họ Chương trình HTPLDN

### CTTDVQL_02 (và CTTLV_03) — Thẻ chỉ số tổng hợp mà §Output đặc thù không liệt kê

**(1) Phần mềm đúng SRS chưa?** **Ô ĐẾM đúng, ô TIỀN/dẫn xuất chưa khai §Output.** CTTDVQL_02 = BC Chương trình theo đơn vị (FR-IX-21 / UC144, bảng chéo mỗi hàng một đơn vị); CTTLV_03 = BC Chương trình theo lĩnh vực (FR-IX-22 / UC145, mỗi hàng một lĩnh vực). Thẻ **"Tổng chương trình" = `tong_ban_ghi`** ("Tổng số bản ghi", "Luôn" — `srs-fr-11-bao-cao.md:100`; bản ghi = chương trình HTPLDN đã duyệt, Processing chung bước 4 `:82`) → **ĐÚNG SRS ở cả 2 báo cáo.** Thẻ **tiền/dẫn xuất:** §Output FR-IX-21 (`:939-945`) chỉ khai `tong_ngan_sach` theo TỪNG đơn vị; §Output FR-IX-22 (`:979-984`) chỉ khai `so_dn_tham_gia` theo TỪNG lĩnh vực — **chưa khai trị tổng "Tổng ngân sách" / "Tổng DN tham gia" toàn báo cáo** (FR-IX-20/UC143 có con số tổng chương trình `:907` nhưng là báo cáo khác). Pháp lý: TT 17/2025/TT-BTP (đã xác minh) Điều 1.2.y + Điều 3.1.b ("phương pháp tính"). *Cần CĐT xác nhận* biểu mẫu HTPLDN của TT17 (Phụ lục I/IV) có dòng "Tổng cộng" hay không — chưa đối chiếu được số hiệu biểu mẫu.
**(2) Đối tác yêu cầu có khác SRS không? Khác gì?** **CÓ.** Đối tác cho rằng có ô số tổng thừa: CTTDVQL_02 hiện 2 ô (Tổng chương trình, Tổng ngân sách); CTTLV_03 hiện 2 ô (Tổng chương trình, Tổng DN tham gia).
**(3) Yêu cầu đó có bắt buộc cho luồng nghiệp vụ không?** Thẻ ĐẾM "Tổng chương trình" = `tong_ban_ghi` bắt buộc → đúng SRS ở cả 2 báo cáo, giữ nguyên. Thẻ tiền/dẫn xuất (Tổng ngân sách / Tổng DN tham gia) là phần dôi, §Output chưa khai trị tổng toàn báo cáo nhưng **KHÔNG vi phạm đặc tả**. Đối tác đòi gỡ thẻ số tổng → **KHÔNG bắt buộc cho luồng nghiệp vụ** → Loại 3. Giữ nguyên phần mềm; đề nghị đối tác cập nhật Kết quả mong đợi (CTTDVQL_02 + CTTLV_03); nếu đối tác vẫn muốn gỡ thẻ thì ghi vào yêu cầu cải tiến. **KHÔNG tự bổ sung §Output/Mapping trong đợt này.**
**→ Kết luận: Loại 3 — Không sửa, đề nghị đối tác đưa vào danh sách yêu cầu cải tiến; phần mềm đúng SRS, đề nghị đối tác cập nhật Kết quả mong đợi / đưa vào yêu cầu cải tiến.** **✅ BA duyệt 2026-07-24.** [Chỉ nâng Loại 2 nếu CĐT xác nhận biểu mẫu TT17 bắt buộc dòng Tổng cộng.]
> **Phản hồi gửi đối tác:** [Lý do] Thẻ "Tổng chương trình" ở cả hai báo cáo chính là chỉ tiêu "Tổng số bản ghi" bắt buộc của mọi báo cáo nên đúng đặc tả; còn các thẻ "Tổng ngân sách" và "Tổng doanh nghiệp tham gia" là phần hiển thị thêm, không vi phạm đặc tả dù đặc tả mới mô tả các số liệu này theo từng đơn vị hoặc từng lĩnh vực. Yêu cầu bỏ các ô số tổng không bắt buộc cho nghiệp vụ. [Nhận định] Kính đề nghị Quý đối tác đưa nội dung này vào danh sách yêu cầu cải tiến.

---

## Cụm xuyên nhóm cần BA chốt 1 lần — "Khối chỉ số tổng hợp (KPI card)"

**Các case liên quan:** VVTTG_02, CPCTHTTDVQL_03, CPCTHTTLHDN_03, CTTDVQL_02, CTTLV_03 (và gián tiếp cách trình bày ở VVDHT_03).

**Vấn đề chung *(Đã đối chiếu evidence 2026-07-24)*.** Nhiều báo cáo hiển thị ô số tổng ở đầu màn, nhưng SCR-IX-01 §Thành phần màn hình chưa có thành phần riêng cho ô số tổng (chỉ có Biểu đồ + Bảng — `srs-fr-11-bao-cao.md:1050-1051`) → khoảng trống ở tầng màn hình. Về DỮ LIỆU phải tách 2 loại ô:
- **Ô ĐẾM** (Tổng vụ việc / Tổng hồ sơ / Tổng chương trình) = trường **`tong_ban_ghi`** ("Tổng số bản ghi", "Luôn") mà **mẫu chung TPL-REPORT-FULL bắt buộc mọi báo cáo phải có** (`:57`, `:100`) → **ĐÚNG SRS, không phải app tự thêm.**
- **Ô TIỀN / dẫn xuất** (Tổng chi phí / Tổng ngân sách / Tổng DN tham gia) = tổng cộng toàn báo cáo; §Output đặc thù của các báo cáo này chỉ khai các trị đó **theo từng dòng** (đơn vị/loại DN/lĩnh vực), **chưa khai trị tổng toàn báo cáo** → phần này BA chốt: bổ sung §Output (giữ ô) hay gỡ. **Ngoại lệ:** báo cáo trend chi phí FR-IX-19 CÓ sẵn `tong_chi_phi_ky` "Luôn" (`:871`) → ô "Tổng chi phí toàn kỳ" ở CPCTHTTTG_03 hợp lệ.
→ Đồng thời bổ sung thành phần "Khối chỉ số" vào SCR-IX-01 để có chỗ đặt các ô số tổng.

**Căn cứ pháp lý & nghiệp vụ (chung cho cả cụm).**
- *Pháp lý (đã xác minh — TT 17/2025/TT-BTP, hiệu lực 01/11/2025).* Điều 1 khoản 2 điểm y xác định HTPLDN là một lĩnh vực thuộc chế độ báo cáo thống kê ngành Tư pháp; Điều 3 khoản 1 điểm b buộc mỗi biểu mẫu kèm nội dung giải thích "khái niệm, phương pháp tính, cách ghi biểu, nguồn số liệu" (Phụ lục IV). Đây là **cơ sở tham chiếu (thông lệ thống kê pháp định)** cho quy tắc "mọi trị tổng phải có phương pháp tính được đặc tả = phải khai báo trong §Output"; ràng buộc trực tiếp vẫn là **nhất quán nội bộ §Output** (thay cho lập luận cũ dựa vào `tong_ban_ghi`, đã gỡ). *Cần CĐT xác nhận:* số hiệu biểu HTPLDN của TT17 và việc các biểu đó có "dòng Tổng cộng" hay không nằm ở Phụ lục I & IV; nguồn thứ cấp trên mạng chưa đủ khẳng định (một số nơi dẫn biểu "21a/21b/21c" nhưng chưa đối chiếu được văn bản gốc). Lưu ý phân biệt: báo cáo trong module là công cụ tổng hợp nội bộ phục vụ quản lý, làm nền cho báo cáo thống kê luật định gửi Bộ; §Output đặc thù vẫn là đặc tả ràng buộc trực tiếp.
- *Nghiệp vụ.* Báo cáo thống kê hành chính theo thông lệ luôn có dòng/ô "Tổng cộng", và dashboard quản lý thường đặt thẻ chỉ số tổng hợp đầu màn để lãnh đạo nắm nhanh quy mô. Vì thế các thẻ tổng đang hiển thị là **hợp lý về nghiệp vụ, chỉ thiếu chỗ đứng trong đặc tả** — nghiêng về GIỮ + khai báo hơn là gỡ.

**Đề xuất BA (dọn 1 lần).** Theo quy tắc: thẻ ĐẾM (`tong_ban_ghi`) là đúng SRS → **giữ**; thẻ tiền/dẫn xuất là phần dôi, §Output chưa khai trị tổng toàn báo cáo nhưng **KHÔNG vi phạm đặc tả** → cả cụm là **Loại 3 — giữ nguyên app, đề nghị đối tác cập nhật Kết quả mong đợi, KHÔNG tự bổ sung §Output trong đợt này**. Chỉ nâng Loại 2 nếu CĐT xác nhận biểu mẫu luật định (vd biểu mẫu HTPLDN của TT17) bắt buộc có dòng tổng — khi đó mới update SRS + Dev ở đợt riêng. Căn cứ pháp lý TT17 ở trên vẫn giữ làm tham chiếu; không kèm khuyến nghị chủ động "GIỮ + bổ sung đặc tả 2 tầng".

---

## Nhóm 5 — Nút "In báo cáo" không hiển thị (6 case)

### SLHDVM_08 · VVDTN_08 · VVDHT_08 · VVDHTHT_08 · VVTTG_07 · CLDTBDDDR_08 — Nút "In báo cáo" không hiển thị

**(1) Phần mềm đúng SRS chưa?** **ĐÚNG.** 6 test case dùng chung màn SCR-IX-01 (FR-IX-01→06). §Thành phần màn hình SCR-IX-01 chỉ quy định 4 nút: "Làm mới" (`srs-fr-11-bao-cao.md:1042`) và "Xem báo cáo"/"Xuất Excel"/"Xuất PDF" (`:1047-1049`) — không có nút "In báo cáo" (`:1037-1054`). CSV gốc STT124 mô tả "xuất file báo cáo" nhưng không có nút "In" (`Danh sách transaction_v1.1_2026-03-27.csv:1103`). Nhu cầu in đã đáp ứng một phần: bấm Xuất PDF mở hộp thoại "Tùy chọn in báo cáo PDF" (khổ A4/A3/Letter, dọc/ngang). Pháp lý: TT 17/2025/TT-BTP (đã xác minh) Điều 3.5 cho gửi báo cáo qua 3 cách (Phần mềm / văn bản điện tử / văn bản giấy có chữ ký, đóng dấu) — không buộc phần mềm có riêng nút tên "In", chỉ cần ra được văn bản đúng thể thức (Xuất PDF rồi in là hợp lệ).
**(2) Đối tác yêu cầu có khác SRS không? Khác gì?** **CÓ.** Đối tác báo "màn hình không có nút chức năng" — mong có nút "In báo cáo" riêng, bấm vào mở bản xem trước + hộp thoại in của trình duyệt.
**(3) Yêu cầu đó có bắt buộc cho luồng nghiệp vụ không?** **KHÔNG.** Nhu cầu in đã được Xuất PDF đáp ứng (còn hợp thể thức hơn nút in trình duyệt vốn in theo DOM màn hình, dễ vỡ thể thức) → đưa vào yêu cầu cải tiến. Cập nhật Kết quả mong đợi 6 test case (bỏ yêu cầu nút "In báo cáo" riêng), hướng dẫn dùng Xuất PDF để in — đã đáp ứng phương thức "văn bản giấy" của TT17. Nếu CĐT vẫn muốn nút "In": bổ sung nút mở LẠI bản xem trước PDF rồi in (không print DOM màn hình), ghi component vào SCR-IX-01 + Dev FE — xử như cải tiến, không phải lỗi.
**→ Kết luận: Loại 3 — Không sửa, đề nghị đối tác đưa vào danh sách yêu cầu cải tiến; nhu cầu in đã đáp ứng qua Xuất PDF, nút "In báo cáo" riêng đưa vào yêu cầu cải tiến.** **✅ BA duyệt 2026-07-24.**
> **Phản hồi gửi đối tác:** [Lý do] Màn hình báo cáo chỉ quy định các nút "Làm mới", "Xem báo cáo", "Xuất Excel" và "Xuất PDF", không có nút "In báo cáo", nên phần mềm đúng đặc tả; nhu cầu in cũng đã được đáp ứng qua chức năng Xuất PDF (bảo đảm thể thức văn bản tốt hơn so với in trực tiếp từ màn hình). Một nút "In" riêng không bắt buộc cho nghiệp vụ. [Nhận định] Kính đề nghị Quý đối tác đưa nội dung này vào danh sách yêu cầu cải tiến.

---

## Nhóm 6 — Nút "Xóa bộ lọc" không hiển thị (6 case)

### SLHDVM_09 · VVDTN_09 · VVDHT_09 · VVDHTHT_09 · VVTTG_08 · CLDTBDDDR_09 — Nút "Xóa bộ lọc" không hiển thị

**(1) Phần mềm đúng SRS chưa?** **ĐÚNG.** 6 test case dùng chung màn SCR-IX-01 (FR-IX-01→06). Chức năng reset lọc CÓ tồn tại dưới tên "Làm mới" (`srs-fr-11-bao-cao.md:1042`); thanh thao tác chỉ có "Xem báo cáo"/"Xuất Excel"/"Xuất PDF" (`:1047-1049`) — SRS không có nút tên "Xóa bộ lọc". QA kiểm: nút "Làm mới" xóa hết giá trị lọc + xóa vùng kết quả, không tự tải lại. SRS không quy định giá trị mặc định cụ thể sau reset (Kỳ=Tháng, đầu tháng...); app đặt lại về trạng thái ban đầu để trống. CSV cũng không quy định tên nút reset lọc.
**(2) Đối tác yêu cầu có khác SRS không? Khác gì?** **CÓ (khác TÊN + giá trị mặc định).** Đối tác báo "màn hình không có nút chức năng" — mong nút tên "Xóa bộ lọc", reset về mặc định cụ thể (Kỳ=Tháng, Từ ngày=đầu tháng, Đến ngày=hôm nay, Đơn vị=đơn vị đang đăng nhập, còn lại="Tất cả"), và phần kết quả không tự tải lại.
**(3) Yêu cầu đó có bắt buộc cho luồng nghiệp vụ không?** **KHÔNG.** Chức năng reset đã có (khác TÊN, không thiếu chức năng) → đưa vào yêu cầu cải tiến. Cập nhật Kết quả mong đợi 6 test case ("Xóa bộ lọc" → "Làm mới", mô tả reset về trạng thái khởi tạo trống). Hai điểm CĐT có thể cân nhắc như cải tiến: (a) chuẩn hóa tên nút toàn hệ thống (màn danh sách khác dùng "Xóa bộ lọc", màn này dùng "Làm mới") → cập nhật SCR-IX-01 + Dev; (b) reset pre-fill giá trị mặc định (Kỳ=Tháng, đầu tháng, hôm nay) thay vì để trống → bổ sung SCR-IX-01 + Dev FE. Điểm đồng bộ: `srs-fr-11-bao-cao.md:1042` (Nút Làm mới) — nếu chốt đổi tên/định giá trị mặc định thì sửa dòng này.
**→ Kết luận: Loại 3 — Không sửa, đề nghị đối tác đưa vào danh sách yêu cầu cải tiến; chức năng reset đã có (nút "Làm mới"), thống nhất tên nút + giá trị mặc định đưa vào yêu cầu cải tiến.** **✅ BA duyệt 2026-07-24.**
> **Phản hồi gửi đối tác:** [Lý do] Chức năng xóa bộ lọc đã tồn tại dưới tên nút "Làm mới" theo đúng đặc tả màn hình, nên phần mềm không thiếu chức năng mà chỉ khác tên gọi và giá trị mặc định sau khi đặt lại. Việc thống nhất tên nút hay điền sẵn các giá trị mặc định không bắt buộc cho nghiệp vụ. [Nhận định] Kính đề nghị Quý đối tác đưa nội dung này vào danh sách yêu cầu cải tiến.

---

## Phụ lục — Xác minh citation của phiếu

Đã mở SRS đúng vị trí và **xác nhận toàn bộ trích dẫn của QA là chính xác**, trừ 2 điểm bổ sung sau (QA nêu thiếu, không sai):

1. **FR-IX-19 có trị tổng toàn kỳ.** §Output FR-IX-19 có `tong_chi_phi_ky` ("Tổng CP toàn kỳ", "Luôn" — dòng 871). Đây là tiền lệ cho thấy mẫu "báo cáo trend + 1 trị tổng toàn kỳ" là hợp lý để BA cân nhắc bổ sung cho FR-IX-05; nhưng nó KHÔNG tự làm thẻ "Tổng vụ việc toàn kỳ" ở VVTTG_02 thành hợp lệ, vì §Output FR-IX-05 (335-339) hiện chưa khai báo trị tổng tương ứng.
2. **Về `tong_ban_ghi` của template chung.** Trường này (`srs-fr-11-bao-cao.md:100`, TPL-REPORT-FULL, "Luôn") CHỈ là "Tổng số bản ghi" chung, KHÔNG phải trị "Tổng chi phí"/"Tổng hồ sơ"/"Tổng ngân sách" → chỉ hợp lệ hoá thẻ **ĐẾM** (Tổng vụ việc / hồ sơ / chương trình = `tong_ban_ghi`, đúng SRS, giữ). Thẻ **TIỀN/dẫn xuất** không nằm trong §Output đặc thù nhưng là phần dôi không vi phạm đặc tả → theo quy tắc là **Loại 3** (giữ app, đối tác cập nhật Expected, KHÔNG tự bổ sung §Output); chỉ nâng Loại 2 nếu CĐT xác nhận biểu mẫu luật định bắt buộc có dòng Tổng cộng.

CSV baseline: STT 124–146 (`Danh sách transaction_v1.1_2026-03-27.csv:1096+`) xác nhận đây là các chức năng báo cáo của "Cán bộ nghiệp vụ TW,BN,ĐP / Cán bộ phê duyệt TW,BN,ĐP", không có tranh chấp tác nhân/phạm vi; CSV không định nghĩa nút "In báo cáo" hay "Xóa bộ lọc" → không phủ nhận verdict Nhóm 5/6.
