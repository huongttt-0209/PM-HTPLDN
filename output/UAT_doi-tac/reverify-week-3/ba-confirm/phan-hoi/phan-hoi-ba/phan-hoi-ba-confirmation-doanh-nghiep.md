# Phản hồi BA — Quản lý DN được hỗ trợ (phiếu ba-confirmation-doanh-nghiep.md)

**Phiếu nguồn:** `ba-confirmation-doanh-nghiep.md` (Tuần 3, KTĐL, 2026-07-20)
**Nguồn đối chiếu:**
- `_bmad-output/planning-artifacts/srs-v3.5/srs-fr-07-doanh-nghiep.md` (FR-V.III-01/02/NEW-03; SCR-V.III-01/02/03)
- `_bmad-output/planning-artifacts/srs-v3.5/srs-v3.5.md` (quy ước dùng chung UI-08…UI-11, DG-03/06/08; BR-AUTH-08)
- `docs/Input/Danh sách transaction_v1.1_2026-03-27.csv` (UC81 Thêm, UC82 Tìm kiếm DN)

**Ngày lập:** 23/07/2026.

> **Lưu ý số dòng:** phiếu KTĐL trích theo bản `Docs-PM-HTPLDN/...`; nội dung trùng khớp file SRS trong repo nhưng số dòng lệch. Mọi trích dẫn dưới đây dùng số dòng **thực tế trong repo** đã mở kiểm.

---

### QLDNDHTPL_05 + QLDNDHTPL_06 — Form Thêm mới DN gom 2 khối thay vì 3 khối A/B/C

**(1) Phần mềm đúng SRS chưa?** **SAI** — SCR-V.III-03 §Bố cục form ghi rõ phải chia **3 khối A/B/C** (A: định danh cơ bản, B: địa chỉ + phân loại, C: thông tin bổ sung) và liệt kê đủ trường từng khối (`srs-fr-07-doanh-nghiep.md:550-586`). Ảnh `QLDNDHTPL_05.jpg` + `QLDNDHTPL_06.jpg` (cùng một ảnh) cho thấy web chỉ chia **2 khối** "Thông tin chung" + "Thông tin liên hệ", xếp trường sai khối (Email + SĐT lẽ ra Nhóm A lại ở "Thông tin liên hệ"; Loại DN + Quy mô + Ngành nghề lẽ ra Nhóm B lại ở "Thông tin chung") và **thiếu hẳn Nhóm C**. Ghi chú "(sẽ bổ sung)" chỉ thuộc bản vẽ MH-VII-03, không thuộc phần chia khối (`:609`). Bên kiểm thử nói SRS không ràng buộc cách gom khối là chưa đúng.
**(2) Đối tác yêu cầu có khác SRS không? Khác gì?** **KHÔNG** — đối tác chỉ báo "trường thông tin hiển thị không đúng theo thiết kế", tức đòi form về đúng 3 khối A/B/C như SRS đã vẽ, không thêm gì mới.
**(3) Yêu cầu đó có bắt buộc cho luồng nghiệp vụ không?** **CÓ → phải sửa.** Dev FE tổ chức lại form thành 3 khối A/B/C theo §Bố cục form, đồng thời bổ sung 11 trường Nhóm C đang thiếu (trùng gốc BUG-QLDNDHTPL_04); chỉ đổi cách nhóm/nhãn khối, không đụng ràng buộc trường. Khối C mang gốc pháp lý: #16 "DN do phụ nữ làm chủ", #17 "Số lao động nữ", #18 "Số lao động khuyết tật" (`:581-583`) — là tiêu chí xếp thứ tự ưu tiên hỗ trợ tại **NĐ 55/2019/NĐ-CP Điều 4 Khoản 4** (điểm a: DN do phụ nữ làm chủ hoặc dùng nhiều lao động nữ; điểm b: DN dùng từ 30% lao động trở lên là người khuyết tật), dùng để tính điểm ưu tiên (BR-CALC-07) khi phân công. Vì vậy khối C phải tách riêng, có nhãn rõ. (Luật gốc ghi "người khuyết tật từ 30% trở lên", không nhắc "DN xã hội" — cần CĐT xác nhận nếu test case ghi khác.) Điểm đồng bộ SRS: `srs-fr-07-doanh-nghiep.md:550-586`, `:581-583`, `:609`.
**→ Kết luận: Loại 1 — Lỗi phần mềm, Dev sửa theo SRS: tổ chức lại form Thêm mới thành 3 khối A/B/C và bổ sung 11 trường Nhóm C đang thiếu.** *(Đã đối chiếu evidence 2026-07-24)* **✅ BA duyệt 2026-07-24.**

---

### QLDNDHTPL_13 — Form Thêm mới không điền sẵn Tỉnh/TP theo đơn vị cán bộ

**(1) Phần mềm đúng SRS chưa?** **SAI một phần.** SCR-V.III-03 khối B trường #6 yêu cầu giao diện tự điền sẵn Tỉnh/TP theo đơn vị của cán bộ (BR-AUTH-08 — phân quyền theo đơn vị), sửa lại được nếu DN ở tỉnh khác (`srs-fr-07-doanh-nghiep.md:566`); FR-V.III-NEW-03 bước 2 chỉ là lớp chặn backend khi lưu qua API mà thiếu thì tự gán mặc định (`:292`), không thay việc điền sẵn trên giao diện — hai chỗ này bổ trợ nhau, không mâu thuẫn như bên kiểm thử nói. Theo BR-AUTH-08 (`srs-v3.5.md:5443`), cán bộ TW phụ trách toàn quốc nên để trống là **đúng**; cán bộ Hà Nội phải được điền sẵn "Hà Nội" nhưng web vẫn để trống → **sai**, trái dòng 566. (Bằng chứng là video `.webm` không xem trực tiếp được; chấm theo Kết quả thực tế cột L "Hệ thống không đặt mặc định theo đơn vị của cán bộ đăng nhập" + SRS. Cột L chỉ ghi câu chung, không nêu rõ tài khoản cbnv_tw/cbnv_hn — chi tiết tài khoản là suy luận theo phạm vi đơn vị.)
**(2) Đối tác yêu cầu có khác SRS không? Khác gì?** **KHÔNG** cho phần cán bộ địa phương — đối tác đòi form tự điền sẵn Tỉnh/TP, đúng với SRS. Chỉ khác ở kỳ vọng cho cán bộ TW: đối tác coi TW để trống cũng là lỗi, nhưng SRS quy định TW để trống là đúng.
**(3) Yêu cầu đó có bắt buộc cho luồng nghiệp vụ không?** **CÓ → phải sửa.** Dev FE: form Thêm mới điền sẵn Tỉnh/TP = tỉnh của đơn vị cán bộ với cán bộ BN/ĐP (chỉnh được), cán bộ TW để trống; giữ lưới an toàn backend ở bước lưu (dòng 292). Phần TW web đã đúng → phản hồi đối tác: nếu test case kỳ vọng TW cũng điền sẵn thì cập nhật Kết quả mong đợi cho khớp phạm vi toàn quốc. Điểm đồng bộ SRS: `srs-fr-07-doanh-nghiep.md:566`, `:292`; `srs-v3.5.md:5443`.
**→ Kết luận: Loại 1 — Lỗi phần mềm, Dev sửa theo SRS: form Thêm mới điền sẵn Tỉnh/TP theo đơn vị với cán bộ BN/ĐP (sửa được), cán bộ TW để trống.** *(Đã đối chiếu evidence 2026-07-24)* **✅ BA duyệt 2026-07-24.**

---

### QLDNDHTPL_17 — Danh sách DN không sắp xếp khi click tiêu đề cột

**(1) Phần mềm đúng SRS chưa?** **ĐÚNG** — SCR-V.III-01 chỉ ghi "sắp xếp mặc định: bản ghi cập nhật mới nhất lên trên" (`srs-fr-07-doanh-nghiep.md:448`); cả bảng cột (`:436-443`) lẫn quy ước chung DG-06 (`srs-v3.5.md:955`) đều không nói tới việc bấm tiêu đề cột để sắp xếp. Web đã làm đúng phần sắp xếp mặc định.
**(2) Đối tác yêu cầu có khác SRS không? Khác gì?** **CÓ** — đối tác muốn bấm tiêu đề cột để sắp xếp lần lượt tăng dần / giảm dần; đây là chức năng SRS chưa đặt ra.
**(3) Yêu cầu đó có bắt buộc cho luồng nghiệp vụ không?** **KHÔNG → yêu cầu cải tiến.** Không fix; liệt kê sắp-xếp-khi-click-cột vào danh mục yêu cầu cải tiến để BA/CĐT cân nhắc bổ sung. Phản hồi đối tác: phần mềm đúng SRS (chỉ yêu cầu sắp xếp mặc định — đã có), sắp xếp khi click tiêu đề cột là chức năng mới → đưa vào yêu cầu cải tiến, đồng thời cập nhật Kết quả mong đợi test case.
**→ Kết luận: Loại 3 — Không sửa, đề nghị đối tác đưa vào danh sách yêu cầu cải tiến: chức năng sắp xếp khi bấm tiêu đề cột (SRS chỉ đặt sắp xếp mặc định, đã có).** *(Đã đối chiếu evidence 2026-07-24 — ảnh `QLDNDHTPL_17.jpg` là màn danh sách DN; SRS chỉ đặt sắp xếp mặc định, không có bấm-cột-để-sắp-xếp.)* **✅ BA duyệt 2026-07-24.**

> **Phản hồi gửi đối tác:** [Lý do] Danh sách doanh nghiệp hiện được sắp xếp mặc định theo bản ghi cập nhật mới nhất — phần này phần mềm đã đáp ứng đúng yêu cầu. Việc bấm vào tiêu đề cột để sắp xếp tăng dần/giảm dần là chức năng chưa được đặt ra trong tài liệu nghiệp vụ. [Nhận định] Kính đề nghị Quý đối tác đưa nội dung này vào danh sách yêu cầu cải tiến.

---

### TKDNHTPL_02 — Bộ lọc / tìm kiếm danh sách DN khác thiết kế (5 ý con)

**Bối cảnh.** Cán bộ Nghiệp vụ / Phê duyệt lọc danh sách DN (UC82). Thanh bộ lọc trong SRS có 6 ô: Từ khóa, Quy mô, Tỉnh thành, Lĩnh vực KD (chọn nhiều giá trị, theo VSIC cấp 4 — mã ngành nghề), Từ ngày, Đến ngày (`srs-fr-07-doanh-nghiep.md:427-434`, Lĩnh vực KD `:430`); CSV UC82 cũng chỉ có từ khóa (tên/MST), lĩnh vực kinh doanh, khoảng thời gian — không có "Ngành nghề" riêng, không có "Đơn vị" (`Danh sách transaction_v1.1_2026-03-27.csv:689-696`). Đọc ảnh `TKDNHTPL_02.jpg` (đã đối chiếu 2026-07-24): thanh lọc gồm Tìm theo tên DN/MST · Tỉnh/Thành phố · Quy mô · **"Ngành nghề"** (một dropdown có nhãn) · **một ô select rỗng hẹp không nhãn** (ô "‹ ⌄") · Từ ngày · Đến ngày · Bộ lọc nâng cao (2). Ô "Ngành nghề" ở ý 1 và ô vô nghĩa ở ý 5 là **hai phần tử khác nhau**: ô "Ngành nghề" chính là ô lọc Lĩnh vực KD bị đặt sai nhãn, còn ô rỗng hẹp mới là ô thừa cần bỏ. Không có ô nào tên "Đơn vị" trên màn.

**(1) Phần mềm đúng SRS chưa?** **Hỗn hợp.** ý 1 **SAI**: ô lọc Lĩnh vực KD (SRS field #10, `:430`) bị đặt sai nhãn thành "Ngành nghề". ý 2 **SAI**: ô Lĩnh vực KD (chọn nhiều giá trị) thiếu mục "Tất cả" mà UI-11 bắt buộc (`srs-v3.5.md:580`). ý 3 **SAI nếu app chỉ cho chọn 1**: Lĩnh vực KD phải là multi-select theo SRS — dựa trên `linh_vuc_ids` (FR-V.III-02) và bảng nhiều–nhiều `DOANH_NGHIEP_LINH_VUC` (baseline §3.4.3.3a), danh mục theo VSIC 2025 cấp 4 (QĐ 36/2025/QĐ-TTg), khớp chuẩn ĐKKD tại **NĐ 168/2025/NĐ-CP** (một DN đăng ký nhiều ngành nghề). ý 5 **SAI**: có ô select rỗng thừa ngoài 6 ô của SRS + CSV. ý 4 **ĐÚNG**: SRS + CSV UC82 chỉ có 6 ô, không có "Đơn vị" (`:427-434`, `:689-696`).
**(2) Đối tác yêu cầu có khác SRS không? Khác gì?** **Chỉ ý 4 khác** — đối tác đòi thêm field "Đơn vị" cho người dùng cấp TW, không có trong SRS/CSV UC82. Các ý 1/2/3/5 không đòi gì mới, chỉ đòi thanh lọc về đúng 6 ô thiết kế.
**(3) Yêu cầu đó có bắt buộc cho luồng nghiệp vụ không?**
- **Ý 1 (CÓ → phải sửa):** đổi nhãn/placeholder ô "Ngành nghề" thành "Lĩnh vực KD", **KHÔNG xóa** (là 1 trong 6 ô lọc bắt buộc). **Loại 1.**
- **Ý 5 (CÓ → phải sửa):** bỏ ô select rỗng/không nhãn ("‹ ⌄") đang thừa — đây mới là "1 trường tìm kiếm không có ý nghĩa" đối tác báo, **không phải** ô "Ngành nghề". **Loại 1.**
- **Ý 2 (CÓ → phải sửa):** ô Lĩnh vực KD (multi-select) bổ sung mục "Tất cả" theo UI-11. Ô Quy mô / Tỉnh (chọn đơn) SRS không quy định default "Tất cả" → giữ theo SRS (để trống = không lọc). **Loại 1.**
- **Ý 3 (CÓ → phải sửa):** nếu app chỉ cho chọn 1 → Dev fix thành multi; nếu app đã multi → đối tác sửa Kết quả mong đợi. **Loại 1.**
- **Ý 4 (KHÔNG → yêu cầu cải tiến):** giữ theo SRS, không thêm "Đơn vị"; nếu đối tác cần thì đưa vào yêu cầu cải tiến. **Loại 3.**
- Sau khi Dev fix, cập nhật SCR-V.III-01 §filter-bar. Điểm đồng bộ SRS: `srs-fr-07-doanh-nghiep.md:427-434`, `:430`; `srs-v3.5.md:580`; `csv:689-696`.
**→ Kết luận: ý 1/2/3/5 = Loại 1 — Lỗi phần mềm, Dev sửa theo SRS: đổi nhãn ô "Ngành nghề" về "Lĩnh vực KD", bỏ ô select rỗng thừa, thêm mục "Tất cả" theo UI-11 cho ô Lĩnh vực KD, bảo đảm multi-select; ý 4 = Loại 3 — Không sửa, đề nghị đối tác đưa vào danh sách yêu cầu cải tiến: thêm field "Đơn vị" cho người dùng cấp TW (ngoài 6 ô của SRS/CSV UC82).** *(Đã đối chiếu evidence 2026-07-24 — nhãn Loại giữ nguyên; sửa lại mô tả kỹ thuật ý 5 vì ảnh cho thấy ô vô nghĩa KHÔNG phải ô "Ngành nghề".)* **✅ BA duyệt 2026-07-24.**

> **Phản hồi gửi đối tác (ý 4):** [Lý do] Thanh bộ lọc danh sách doanh nghiệp theo thiết kế hiện tại gồm 6 ô: Từ khóa, Quy mô, Tỉnh thành, Lĩnh vực kinh doanh, Từ ngày, Đến ngày — không có ô lọc theo Đơn vị; phần mềm đang giữ đúng thiết kế này. [Nhận định] Kính đề nghị Quý đối tác đưa nội dung này vào danh sách yêu cầu cải tiến.

---

### TKDNHTPL_03 — Tìm không ra kết quả: hiển thị "Trống" thay vì thông báo cụ thể

**(1) Phần mềm đúng SRS chưa?** **SAI** — FR-V.III-02 phần Xử lý lỗi, tình huống E1 "Không có kết quả" quy định dùng mã `INF-DN-TK-01` với câu "Không tìm thấy doanh nghiệp phù hợp", mức thông tin (`srs-fr-07-doanh-nghiep.md:260`). Web hiện chữ "Trống" (mặc định của ô danh sách rỗng) là không đúng câu SRS đã quy định. Bên kiểm thử nói "SRS không quy định câu chữ" là đã bỏ sót bảng Xử lý lỗi.
**(2) Đối tác yêu cầu có khác SRS không? Khác gì?** **KHÔNG** — đối tác chỉ muốn một câu thông báo rõ nghĩa thay vì màn trống chung chung, đúng cái SRS đã đặt (`INF-DN-TK-01`).
**(3) Yêu cầu đó có bắt buộc cho luồng nghiệp vụ không?** **CÓ → phải sửa.** Dev FE: khi tìm kiếm/lọc trả về 0 bản ghi, vùng kết quả hiển thị đúng `INF-DN-TK-01` "Không tìm thấy doanh nghiệp phù hợp" (thay chuỗi "Trống" mặc định). Điểm đồng bộ SRS: `srs-fr-07-doanh-nghiep.md:260`.
**→ Kết luận: Loại 1 — Lỗi phần mềm, Dev sửa theo SRS: khi tìm kiếm/lọc trả về 0 bản ghi, hiển thị đúng `INF-DN-TK-01` "Không tìm thấy doanh nghiệp phù hợp" thay chuỗi "Trống" mặc định.** *(Đã đối chiếu evidence 2026-07-24 — ảnh `TKDNHTPL_03.jpg` xác nhận màn 0 dòng hiện icon hộp rỗng + chữ "Trống"; SRS `:260` E1 → INF-DN-TK-01 "Không tìm thấy doanh nghiệp phù hợp".)* **✅ BA duyệt 2026-07-24.**
