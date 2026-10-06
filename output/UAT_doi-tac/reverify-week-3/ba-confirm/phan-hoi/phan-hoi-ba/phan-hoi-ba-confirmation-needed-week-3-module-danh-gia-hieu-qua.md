# Phản hồi BA — Đánh giá hiệu quả (phiếu ba-confirmation-needed-week-3-module-danh-gia-hieu-qua.md)

**Phiếu nguồn:** `ba-confirmation-needed-week-3-module-danh-gia-hieu-qua.md`
**Nguồn đối chiếu:** `srs-v3.5/srs-fr-08-danh-gia.md` (SRS FR-08) + baseline `srs-v3.5.md` (quy ước UI-01…UI-11, DG-01…DG-08, Phụ lục E.H) + `Danh sách transaction_v1.1_2026-03-27.csv`
**Ngày lập:** 23/07/2026.

> **Ghi chú phương pháp.** Tôi đã tự xác minh từng citation của QA trong SRS FR-08, đồng thời tra baseline `srs-v3.5.md` cho các case QA kết luận "SRS im lặng" (nút Hủy modal, điều hướng sau lưu, thông báo kỳ rỗng, cắt bớt cột). Hai quy ước dùng chung ở baseline làm thay đổi nhận định so với QA: **UI-08** (bắt buộc hỏi xác nhận khi hủy form còn dữ liệu chưa lưu) và **H7** (bắt buộc quay về danh sách + toast sau khi thêm mới). Ngoài ra, các chuỗi thông báo/mã lỗi nằm trong bảng **Error Handling** của SRS là **đặc tả chính thức** (có mã lỗi kèm chuỗi), không phải "mô tả tham khảo"; do đó app lệch chuỗi trong bảng Error Handling được xếp **lỗi nhẹ** theo luật trọng tài #4, khác với lập luận "describe-not-prescribe" của QA.

> **Cách đọc khuôn "3 câu hỏi quyết định".** Mỗi case trả lời 3 câu: (1) Phần mềm đúng SRS chưa? (2) Đối tác yêu cầu có khác SRS không, khác gì? (3) Yêu cầu đó có bắt buộc cho luồng nghiệp vụ không? Rồi quy về Loại: **Loại 1** = app sai SRS, Dev sửa app; **Loại 2** = app đúng SRS (hoặc SRS thiếu/mâu thuẫn) nhưng yêu cầu bắt buộc cho luồng → phải xử lý/chốt; **Loại 3** = app đúng SRS, yêu cầu khác SRS nhưng không bắt buộc → xếp yêu cầu cải tiến (đợt gấp), cập nhật Expected.

---

## Phần 1 — Batch A: Lập kế hoạch và Phân công

### LKHDG_02 — Cột "Tên đợt" bị cắt bớt kèm "..."

**(1) Phần mềm đúng SRS chưa?** ĐÚNG — cắt bớt tên đợt kèm "..." là hành vi được đặc tả tại SCR-VI-01 (`srs-fr-08-danh-gia.md:820`); DG-04 chỉ bắt mở rộng/thu gọn cho nội dung dài quá 2 dòng, không áp cho cột một dòng (`srs-v3.5.md:953`). *(Đã đối chiếu evidence 2026-07-24)* Lưu ý: ảnh LKHDG_02.jpg (cùng màn với LKHDG_03.jpg) KHÔNG có cột "Tên đợt" (các cột: Mã kế hoạch / Đối tượng / Từ ngày / Đến ngày / Số vụ việc / Trạng thái / Người tạo / Ngày tạo / Hành động), nên chưa quan sát được chỗ "cắt bớt + ...". Đề nghị CĐT/đối tác xác nhận lại.
**(2) Đối tác yêu cầu có khác SRS không? Khác gì?** CÓ — đối tác muốn đọc đủ tên đợt (không cắt), ví dụ "Đợt đánh giá seed 2026" thay vì "Đợt đánh...", trong khi SRS đặc tả hiển thị cắt bớt kèm "...".
**(3) Yêu cầu đó có bắt buộc cho luồng nghiệp vụ không?** KHÔNG → yêu cầu cải tiến. Không bắt buộc sửa app; đề nghị cập nhật Expected. Cải tiến tùy chọn: thêm tooltip hiện đầy đủ tên khi rê chuột, chỉ cắt giá trị chứ không cắt tiêu đề cột.
**→ Kết luận: CHỜ ĐỐI TÁC LÀM RÕ — chưa gán Loại.** (Nếu app **thiếu hẳn cột Tên đợt** so với SCR #11 → **Loại 1** Dev bổ sung cột; nếu chỉ **cắt chữ** đúng SRS → **Loại 3**. Gán Loại sau khi đối tác trả lời.) (Note đề nghị đối tác xác nhận trên màn thật trước khi gán Loại.)

---

### LKHDG_03 — Bộ lọc danh sách (3 ý: "Tròn năm" / mục "Tất cả" / lọc Trạng thái)

**(1) Phần mềm đúng SRS chưa?**
- #1 "Tròn năm": **SAI** — SRS ghi nhãn "Tròn năm" (mã TRON_NAM, `srs-fr-08-danh-gia.md:821`) đúng thuật ngữ Thông tư 17/2025/TT-BTP (nguyên văn: kỳ báo cáo "gồm toàn bộ số liệu thực tế tính từ ngày 01 tháng 01 đến hết ngày 31 tháng 12 năm báo cáo"; ba kỳ 21a/21b là "sơ bộ 6 tháng / sơ bộ năm / tròn năm"); app hiện "Trọn năm" là sai. Nhận định ban đầu "app đúng, SRS ghi nhầm chính tả" đã bị **lật**.
- #2 mục "Tất cả": app **khác SRS** — SRS ghi mục "Tất cả" trong dropdown Lọc tần suất/Lọc đối tượng (`srs-fr-08-danh-gia.md:813-814`), app chỉ để chữ gợi ý mờ trong ô; UI-11 (`srs-v3.5.md:580`) chỉ áp ô chọn nhiều nên không bắt buộc trực tiếp, nhưng SRS đã ghi rõ mục "Tất cả".
- #3 lọc Trạng thái: app **khác SRS** — SRS quy định dropdown nằm trong thanh lọc (`srs-fr-08-danh-gia.md:815`), app làm dạng các thẻ tab.
**(2) Đối tác yêu cầu có khác SRS không? Khác gì?** KHÔNG (đối tác khớp SRS, app lệch) — #1 Expected "Tròn năm" trùng SRS; #2 muốn hiện mục "Tất cả" tường minh (trùng SRS); #3 muốn dropdown Trạng thái trong thanh lọc (trùng SRS).
**(3) Yêu cầu đó có bắt buộc cho luồng nghiệp vụ không?** #1 **CÓ** (thuật ngữ pháp định TT 17/2025) → Dev sửa app "Trọn năm" → "Tròn năm", giữ nguyên Expected; đề nghị CĐT đối chiếu biểu 21a/21b gốc trước khi chốt. #2/#3 app lệch SRS, đối tác khớp SRS → **Loại 1 (Dev sửa app theo SRS)**: #2 Dev hiện mục "Tất cả" tường minh trong dropdown Lọc tần suất/Lọc đối tượng (`srs-fr-08-danh-gia.md:813-814`), không để chữ gợi ý mờ; #3 Dev chuyển lọc Trạng thái về dropdown trong thanh lọc (`srs-fr-08-danh-gia.md:815`), không dùng tabs. *(Ghi chú: nếu BA thấy tabs hợp lý hơn thì hợp thức hóa bằng Loại 2 — cập nhật SCR #6; mặc định theo quy tắc là Loại 1.)*
**→ Kết luận: Loại 1 — Lỗi phần mềm, Dev sửa theo SRS (cả 3 ý). #1 Dev sửa app "Trọn năm"→"Tròn năm"; #2 Dev hiện mục "Tất cả" tường minh trong dropdown; #3 Dev đưa lọc Trạng thái về dropdown trong thanh lọc, bỏ tabs.** Điểm đồng bộ SRS: `srs-fr-08-danh-gia.md:813-814, 815, 821`; đối chiếu `srs-v3.5.md:580` (UI-11). **✅ BA duyệt 2026-07-24.**

---

### LKHDG_10 — Sau "Lưu nháp" không điều hướng chi tiết

**(1) Phần mềm đúng SRS chưa?** ĐÚNG — SRS phân biệt hai nút: "[Lưu nháp]" chỉ lưu (đưa đợt về LAP_KE_HOACH), còn "[Lưu & Chuyển tiêu chí]" mới mở màn chi tiết Tab 1 (`srs-fr-08-danh-gia.md:841`); đầu ra UC83 chỉ yêu cầu một thông báo nổi (`:139`) và tạo bản ghi kế hoạch LAP_KE_HOACH (`:143`). Quy ước chung **H7** (Phụ lục E.H) bắt buộc sau khi thêm mới thì quay về danh sách kèm thông báo nổi, trừ khi FR ghi ngoại lệ. Vậy "ở lại danh sách + toast" đúng cả đặc tả lẫn quy ước chung.
**(2) Đối tác yêu cầu có khác SRS không? Khác gì?** CÓ — đối tác muốn "Lưu nháp" giữ/chuyển sang màn chi tiết đợt, đi ngược quy ước H7.
**(3) Yêu cầu đó có bắt buộc cho luồng nghiệp vụ không?** KHÔNG → yêu cầu cải tiến. Luồng vào thẳng chi tiết đã có sẵn ở nút "Lưu & Chuyển tiêu chí". Không sửa app; đề nghị cập nhật Expected. Nếu vẫn muốn "Lưu nháp" điều hướng chi tiết thì là yêu cầu mới **đi ngược H7**, cần CĐT quyết trước khi ghi ngoại lệ vào FR.
**→ Kết luận: Loại 3 — Không sửa, đề nghị đối tác đưa vào danh sách yêu cầu cải tiến: giữ "Lưu nháp" ở lại danh sách kèm toast theo H7 (luồng vào chi tiết đã có sẵn ở nút "Lưu & Chuyển tiêu chí").** **✅ BA duyệt 2026-07-24.**
> **Phản hồi gửi đối tác:** Kính thưa Quý đối tác, phần mềm hiện đã tuân thủ đặc tả: nút "Lưu nháp" chỉ thực hiện lưu đợt về trạng thái Lập kế hoạch và ở lại danh sách kèm thông báo nổi theo quy ước dùng chung của hệ thống, còn thao tác đi thẳng vào màn chi tiết đã được bố trí sẵn ở nút "Lưu & Chuyển tiêu chí". Yêu cầu để "Lưu nháp" điều hướng sang màn chi tiết đi ngược quy ước dùng chung nói trên và không bắt buộc cho luồng nghiệp vụ. Kính đề nghị Quý đối tác đưa nội dung này vào danh sách yêu cầu cải tiến.

---

### LKHDG_19 — Chi tiết đợt không hiển thị "Cơ quan được đánh giá"

**(1) Phần mềm đúng SRS chưa?** **SRS mâu thuẫn nội bộ** — SCR-VI-01 #28 (thẻ "Thông tin đợt") chỉ liệt kê 5 trường Mã đợt/Tên đợt/Tần suất/Kỳ đánh giá/Đối tượng, không có "Cơ quan được đánh giá" (`srs-fr-08-danh-gia.md:849`), app đang làm đúng mô tả này; nhưng data model #16 quy định `co_quan_duoc_danh_gia_id` **bắt buộc**, trỏ tới danh mục đơn vị, thêm bởi **[CR-10]** để phân biệt với "cơ quan thực hiện đánh giá" `don_vi_id` (`srs-fr-08-danh-gia.md:1033`). Ẩn trường này làm mất luôn ý nghĩa của [CR-10]. Căn cứ Nghị định 55/2019/NĐ-CP Điều 14 (Bộ Tư pháp "tổ chức đánh giá độc lập hoạt động hỗ trợ pháp lý cho DN nhỏ và vừa") + TT 17/2025 chia biểu 21a/TP/HTPLDN ("tại cơ quan chuyên môn") và 21b/TP/HTPLDN ("tại UBND cấp tỉnh") → "Cơ quan được đánh giá" là thông tin nhận diện cốt lõi, quyết định đợt xếp vào biểu nào. Điểm/khoản cụ thể của Điều 14 cần CĐT đối chiếu bản gốc.
*(Đã đối chiếu evidence 2026-07-24)* **Đính chính:** ảnh LKHDG_19.jpg cho thấy thẻ "Thông tin kế hoạch" của app ĐÃ hiển thị "Mục tiêu" (ví dụ "TKM kiểm thử chức năng lưu nháp") cùng nhiều trường ngoài SCR #28 (Thời gian bắt đầu/kết thúc, Số vụ việc, Điểm trung bình, Ghi chú) — nhận định cũ "Mục tiêu cũng vắng" là SAI; trường duy nhất thực sự thiếu là "Cơ quan được đánh giá".
**(2) Đối tác yêu cầu có khác SRS không? Khác gì?** KHÔNG (khớp data model) — đối tác muốn thẻ chi tiết hiển thị "Cơ quan được đánh giá" đã nhập lúc tạo, tức đòi khớp trường bắt buộc `co_quan_duoc_danh_gia_id`.
**(3) Yêu cầu đó có bắt buộc cho luồng nghiệp vụ không?** CÓ → phải sửa. Chọn **Hướng 1** (khuyến nghị): thẻ chi tiết bổ sung hiển thị "Cơ quan được đánh giá"; đồng thời dọn SCR #28 (`:849`) thêm trường này và đồng bộ danh sách trường thẻ chi tiết với thực tế app (Mục tiêu/thời gian/số VV/điểm TB/ghi chú đã có). Sau khi BA chốt Hướng 1, UI hiện tại là **thiếu đúng 1 trường "Cơ quan được đánh giá"** → owner Dev FE. Hướng 2 (giữ ẩn khỏi thẻ chi tiết, dọn SCR hợp thức hóa việc chỉ dùng ở tầng dữ liệu) đi ngược bản chất đánh giá độc lập + trục phân loại biểu 21a/21b, **không khuyến nghị**.
**→ Kết luận: Loại 2 — Cập nhật SRS rồi Dev làm theo SRS mới: bổ sung trường "Cơ quan được đánh giá" vào thẻ chi tiết + dọn SCR #28, Dev FE hiển thị theo SRS mới.** **✅ BA duyệt 2026-07-24.**
> **Phương án xử lý (cập nhật SRS):** `srs-fr-08-danh-gia.md:849` (SCR-VI-01 #28 thẻ "Thông tin đợt", hiện chỉ liệt kê Mã đợt/Tên đợt/Tần suất/Kỳ đánh giá/Đối tượng) — bổ sung trường "Cơ quan được đánh giá" (đồng bộ data model #16 `co_quan_duoc_danh_gia_id` bắt buộc `[CR-10]` tại `:1033`), đồng thời dọn danh sách trường của thẻ cho khớp thực tế app (Mục tiêu/thời gian/số VV/điểm TB/ghi chú). Sau khi SRS cập nhật, Dev FE hiển thị "Cơ quan được đánh giá" trên thẻ chi tiết đợt.

---

### PCNTHDG_06 — Nút [Hủy] modal "Thêm người đánh giá" không hỏi xác nhận

**(1) Phần mềm đúng SRS chưa?** SAI — quy ước dùng chung **UI-08** bắt buộc hỏi xác nhận ("Ở lại / Rời đi") khi hủy một biểu mẫu đang nhập dở còn dữ liệu chưa lưu, áp dụng cho **mọi biểu mẫu nhập liệu trong toàn hệ thống** (`srs-v3.5.md:577`). Cửa sổ "Thêm người đánh giá" có ô bắt buộc (Người đánh giá, Vai trò) và đã nhập dở nên thuộc phạm vi UI-08; app đóng im lặng là vi phạm. (QA đóng khung "SRS im lặng" vì chỉ tra file FR-08 SCR #38/#39 — SRS **không** hề im lặng.)
**(2) Đối tác yêu cầu có khác SRS không? Khác gì?** KHÔNG — đối tác đòi hộp thoại xác nhận hủy bỏ thay đổi chưa lưu, đúng bằng UI-08.
**(3) Yêu cầu đó có bắt buộc cho luồng nghiệp vụ không?** CÓ → phải sửa. Dev FE bổ sung hộp thoại xác nhận "Ở lại / Rời đi" theo UI-08; chỉ đóng modal và bỏ dữ liệu khi người dùng xác nhận rời. Có thể ghi chú UI-08 vào SCR-VI-01 (Tab Phân công) để Dev không bỏ sót; nguồn chuẩn `srs-v3.5.md:577`.
**→ Kết luận: Loại 1 — Lỗi phần mềm, Dev sửa theo SRS: bổ sung hộp thoại xác nhận "Ở lại / Rời đi" khi hủy modal còn dữ liệu chưa lưu theo UI-08.** **✅ BA duyệt 2026-07-24.**

---

## Phần 2 — Batch B: Thực hiện, Chấm điểm, Báo cáo và Phê duyệt

### CVVDG_01 — Toast chọn vụ việc "Đã chọn vụ việc đánh giá" vs "Đã lưu {N} vụ việc"

**(1) Phần mềm đúng SRS chưa?** ĐÚNG — FR-VI-05 bước 6 "Lưu danh sách VV đánh giá" (`srs-fr-08-danh-gia.md:420`) không quy định chính xác câu chữ; quy ước chung chỉ yêu cầu "hiện thông báo nổi khi lưu thành công" (`:894`). App hiện thông báo nổi "Đã chọn vụ việc đánh giá" → đã đạt yêu cầu SRS.
**(2) Đối tác yêu cầu có khác SRS không? Khác gì?** CÓ — đối tác muốn chuỗi "Đã lưu {N} vụ việc" (có số lượng, dùng động từ "Lưu"), theo bản thiết kế riêng của đối tác, không phải SRS v3.5.
**(3) Yêu cầu đó có bắt buộc cho luồng nghiệp vụ không?** KHÔNG → yêu cầu cải tiến. Không sửa app; đề nghị cập nhật Expected. Cải tiến tùy chọn: thêm số lượng vào toast, ví dụ "Đã lưu {N} vụ việc đánh giá".
**→ Kết luận: Loại 3 — Không sửa, đề nghị đối tác đưa vào danh sách yêu cầu cải tiến: giữ toast hiện tại (đã đạt yêu cầu SRS); tùy chọn thêm số lượng vào toast, ví dụ "Đã lưu {N} vụ việc đánh giá".** **✅ BA duyệt 2026-07-24.**
> **Phản hồi gửi đối tác:** Kính thưa Quý đối tác, phần mềm đã hiển thị thông báo nổi khi lưu danh sách vụ việc đánh giá thành công, đáp ứng đúng yêu cầu của đặc tả (đặc tả chỉ quy định hiện thông báo nổi khi lưu thành công, không ấn định câu chữ cụ thể). Chuỗi "Đã lưu {N} vụ việc" mà Quý đối tác mong muốn thuộc bản thiết kế riêng, không phải đặc tả hiện hành và không bắt buộc cho luồng nghiệp vụ. Kính đề nghị Quý đối tác đưa nội dung này vào danh sách yêu cầu cải tiến.

---

### CVVDG_02 — Bảng chọn VV thiếu cột Tên DN / Ngày hoàn thành / Cảnh báo trùng đợt

**(1) Phần mềm đúng SRS chưa?** ĐÚNG — SCR #41 mô tả phần chọn vụ việc là danh sách tích chọn nhiều, **không liệt kê cột nào bắt buộc** (`srs-fr-08-danh-gia.md:872`). "Tên DN" chỉ gắn bảng chấm điểm SCR #42 (`:873`) và bảng tổng hợp báo cáo SCR #47 (`:883`); "Ngày hoàn thành" không xuất hiện ở màn hình nào của Nhóm VI; "Cảnh báo trùng đợt" là một **hành vi** (`:449`), kiểm riêng ở case CVVDG_03. App hiện 5 cột (Mã VV, Tên VV, Lĩnh vực, Trạng thái, Đã chọn?) đủ để chọn vụ việc.
**(2) Đối tác yêu cầu có khác SRS không? Khác gì?** CÓ — đối tác muốn thêm cột Tên doanh nghiệp, Ngày hoàn thành, Cảnh báo trùng đợt vào bảng chọn VV, ngoài đặc tả SCR #41.
**(3) Yêu cầu đó có bắt buộc cho luồng nghiệp vụ không?** KHÔNG → yêu cầu cải tiến. Không sửa app; đề nghị cập nhật Expected. Tùy chọn: nếu CB NV cần phân biệt VV theo doanh nghiệp, BA có thể yêu cầu bổ sung cột "Tên DN" (owner Dev FE khi đó).
**→ Kết luận: Loại 3 — Không sửa, đề nghị đối tác đưa vào danh sách yêu cầu cải tiến: giữ bảng chọn VV 5 cột theo SCR #41; thêm cột Tên DN / Ngày hoàn thành / Cảnh báo trùng đợt là cải tiến tùy chọn.** **✅ BA duyệt 2026-07-24.**
> **Phản hồi gửi đối tác:** Kính thưa Quý đối tác, phần mềm đã cung cấp bảng chọn vụ việc với đầy đủ các cột phục vụ thao tác chọn (Mã VV, Tên VV, Lĩnh vực, Trạng thái, Đã chọn), phù hợp với đặc tả màn hình này vốn không liệt kê cột nào là bắt buộc. Các cột "Tên doanh nghiệp", "Ngày hoàn thành", "Cảnh báo trùng đợt" nằm ngoài đặc tả màn hình này và không bắt buộc cho luồng nghiệp vụ. Kính đề nghị Quý đối tác đưa nội dung này vào danh sách yêu cầu cải tiến.

---

### CVVDG_04 — Message kỳ đánh giá không có VV

**(1) Phần mềm đúng SRS chưa?** SAI (lỗi nhẹ về chuỗi) — bảng Error Handling FR-VI-05 mục E1 chốt rõ: kỳ không có vụ việc nào hoàn thành thì hiện mã `WRN-DG-VV-01` với câu "Không có vụ việc nào hoàn thành trong kỳ đánh giá này" (`srs-fr-08-danh-gia.md:442`); app đang dùng câu chung "Không có vụ việc nào phù hợp". Bảng Error Handling có mã lỗi kèm chuỗi cụ thể là đặc tả chính thức → theo luật trọng tài #4, app dùng sai câu chữ là lỗi nhẹ. Hành vi xử lý kỳ rỗng (khóa nút xác nhận) đã đúng.
**(2) Đối tác yêu cầu có khác SRS không? Khác gì?** KHÔNG — đối tác đòi câu thông báo khớp SRS WRN-DG-VV-01.
**(3) Yêu cầu đó có bắt buộc cho luồng nghiệp vụ không?** CÓ → phải sửa (ưu tiên thấp, không ảnh hưởng dữ liệu/luồng). Dev FE đổi chuỗi trạng thái rỗng của bảng chọn VV thành "Không có vụ việc nào hoàn thành trong kỳ đánh giá này" theo WRN-DG-VV-01.
**→ Kết luận: Loại 1 — Lỗi phần mềm, Dev sửa theo SRS: đổi chuỗi trạng thái rỗng của bảng chọn VV thành "Không có vụ việc nào hoàn thành trong kỳ đánh giá này" theo WRN-DG-VV-01.** **✅ BA duyệt 2026-07-24.**

---

### THDG_02 — Chấm điểm: thiếu ô nhận xét từng tiêu chí; nhãn "Ghi chú" vs "Nhận xét tổng thể"

**(1) Phần mềm đúng SRS chưa?** **SRS mâu thuẫn nội bộ** (3 chỗ không khớp) — FR-VI-06 Inputs liệt kê 2 ô: nhận xét từng tiêu chí `nhan_xet` (≤1000 ký tự, `srs-fr-08-danh-gia.md:480`) và nhận xét tổng thể `nhan_xet_tong_the` (≤2000, `:481`); nhưng SCR #42 chỉ có **một** cột "Nhận xét" (`:873`), nhận xét tổng thể của đợt nằm ở Tab Báo cáo qua ô "Nhận xét chung" SCR #49 (`:885`); data model kết quả đánh giá cũng chỉ có **một** ô `nhan_xet`/vụ việc + điểm chi tiết từng tiêu chí lưu dạng JSON `chi_tiet_diem` (`:1050-1051`), không có chỗ chứa nhận xét riêng per tiêu chí. App có 1 ô "Ghi chú" — khớp số lượng với SCR #42 và data model, chỉ khác **tên nhãn**. Không có luật nào bắt nhận xét theo từng tiêu chí (điểm chi tiết đã lưu ở `chi_tiet_diem` nên vẫn minh bạch).
**(2) Đối tác yêu cầu có khác SRS không? Khác gì?** CÓ — đối tác muốn thêm ô "Nhận xét từng tiêu chí" và đổi ô nhận xét chung thành nhãn "Nhận xét tổng thể" (app đang để "Ghi chú").
**(3) Yêu cầu đó có bắt buộc cho luồng nghiệp vụ không?** CÓ (phần đổi nhãn cho khớp SCR) → phải sửa. Chọn **Hướng 2** (khuyến nghị): giữ một ô nhận xét cho mỗi dòng VV, đổi nhãn "Ghi chú" → "Nhận xét" cho khớp SCR #42; nhận xét tổng thể của đợt dùng ô "Nhận xét chung" ở Tab Báo cáo (SCR #49); dọn FR-VI-06 Inputs #4 ghi rõ `nhan_xet` là nhận xét **theo dòng VV** (không per tiêu chí) (`:480`). Hướng 1 (làm nhận xét per tiêu chí đúng FR Inputs #4) phải mở rộng data model để lưu lời văn từng tiêu chí + mở rộng màn chấm điểm — thay đổi lớn về dữ liệu/giao diện/chi phí nhập liệu, chỉ chốt khi CĐT xác định báo cáo đánh giá độc lập cần giải trình từng tiêu chí.
**→ Kết luận: Loại 2 — Cập nhật SRS rồi Dev làm theo SRS mới: giữ 1 ô nhận xét cho mỗi dòng VV, đổi nhãn "Ghi chú"→"Nhận xét" khớp SCR #42, dọn FR-VI-06 Inputs #4 (nhận xét theo dòng VV, không per tiêu chí).** **✅ BA duyệt 2026-07-24.**
> **Phương án xử lý (cập nhật SRS):** `srs-fr-08-danh-gia.md:480` (FR-VI-06 Inputs #4 `nhan_xet`, hiện chỉ "Max 1000 ký tự") — ghi rõ đây là nhận xét theo dòng vụ việc (một ô/VV, KHÔNG per tiêu chí); nhận xét tổng thể của đợt dùng ô "Nhận xét chung" ở Tab Báo cáo (SCR #49, `:885`). Sau khi SRS cập nhật, Dev FE đổi nhãn ô "Ghi chú" → "Nhận xét" cho khớp SCR #42 (`:873`), giữ nguyên số lượng ô và data model.

---

### THDG_03 — Nhập điểm vượt max: FE tự nắn im lặng, không báo lỗi

**(1) Phần mềm đúng SRS chưa?** SAI (lỗi nhẹ) — bảng Error Handling FR-VI-06 mục E1 buộc điểm vượt tối đa phải **từ chối và báo cho người dùng**, kèm mã `ERR-DG-DG-01` "Điểm phải từ 0 đến {max}" (`srs-fr-08-danh-gia.md:517`). Thực tế: phía giao diện tự sửa 15 về 10 mà không nói gì (chưa đạt phần "báo"), phía máy chủ từ chối đúng (mã `ERR-DG-SC-06`, chặn 0–max) nên dữ liệu vẫn an toàn. Theo luật trọng tài #5, thiếu thông báo là lỗi nhẹ.
**(2) Đối tác yêu cầu có khác SRS không? Khác gì?** KHÔNG — đối tác đòi báo lỗi khi vượt max, đúng E1.
**(3) Yêu cầu đó có bắt buộc cho luồng nghiệp vụ không?** CÓ → phải sửa (FE). Dev FE hiển thị thông báo khi phát hiện nhập vượt max — hoặc chặn kèm chuỗi "Điểm phải từ 0 đến {max}" theo E1, hoặc nếu vẫn nắn về max thì kèm dòng "Đã điều chỉnh về tối đa {max}". BE đã đúng, không cần sửa logic. Cải tiến tùy chọn: đồng bộ mã lỗi BE `ERR-DG-SC-06` với SRS `ERR-DG-DG-01` (hoặc cập nhật SRS ghi nhận mã thực tế) (`:517`).
**→ Kết luận: Loại 1 — Lỗi phần mềm, Dev sửa theo SRS: Dev FE hiển thị thông báo khi nhập điểm vượt max theo ERR-DG-DG-01 "Điểm phải từ 0 đến {max}" (BE đã đúng, không cần sửa logic).** **✅ BA duyệt 2026-07-24.**

---

### LBCDG_02 — Trường thông tin màn Lập báo cáo không đúng SRS

**(1) Phần mềm đúng SRS chưa?** SAI (làm sai đặc tả, không phải phạm vi để mở) — FR-VI-07 quy định các ô người dùng phải tự nhập: kinh phí hoạt động khác `kp_hoat_dong_khac`, kinh phí xã hội hóa `kp_xa_hoi_hoa`, nhận xét tổng thể `nhan_xet_tong_the`, kiến nghị `kien_nghi` (`srs-fr-08-danh-gia.md:551-554`); báo cáo tạo theo mẫu chung Nhóm VI (`:562`) với một bộ số liệu tự động điền — bảng 13 cột chính (`:569-585`, số tư vấn viên, buổi tập huấn, hội nghị, văn bản, hồ sơ theo quy mô DN, kinh phí NSNN…). App hiện chỉ có 4 ô (Tiêu đề, Nội dung, Nhận xét tổng thể, Kiến nghị) → **thiếu** 2 ô kinh phí + **thiếu** toàn bộ bộ số liệu, đồng thời **thừa** hai ô "Tiêu đề"/"Nội dung" không nằm trong Inputs. (Luật trọng tài #6: chỉ dẫn các cột do chính SRS liệt kê dòng 569–585, không suy diễn thêm TT17.) Căn cứ NĐ 55/2019 Điều 14 (tổng hợp, gửi báo cáo kết quả HTPL) + mẫu 21a/21b của TT 17/2025; chi tiết cột 21a/21b cần CĐT đối chiếu biểu gốc.
**(2) Đối tác yêu cầu có khác SRS không? Khác gì?** KHÔNG — đối tác đòi bộ trường đúng thiết kế, tức đúng FR-VI-07 (không phải các ô tự do "Tiêu đề/Nội dung").
**(3) Yêu cầu đó có bắt buộc cho luồng nghiệp vụ không?** CÓ → phải sửa, phân kỳ 2 bước:
- Bước 1 (rõ ràng, chi phí thấp): bổ sung 2 ô kinh phí nhập tay `kp_hoat_dong_khac`, `kp_xa_hoi_hoa`; bảo đảm `nhan_xet_tong_the`, `kien_nghi` đúng Inputs; rà "Tiêu đề"/"Nội dung" — ưu tiên **bỏ** nếu không có trong Inputs, chỉ **ánh xạ** về trường SRS (vd gộp "Nội dung" vào `nhan_xet_tong_the`) khi đối tác chứng minh chúng thay thế một trường chuẩn. Owner Dev FE (+ BE cho 2 ô kinh phí).
- Bước 2 (lớn hơn): hiện thực bộ số liệu tự động theo template Nhóm VI (`:569-585`), bám đúng cột biểu 21a (cơ quan chuyên môn) / 21b (UBND cấp tỉnh) tùy loại cơ quan được đánh giá và theo kỳ báo cáo khớp Tần suất đợt — khối tích hợp BE đáng kể (lấy từ nhiều module), xếp lịch riêng, chỉ khóa danh sách cột sau khi CĐT xác nhận khớp biểu gốc. Owner Dev FE + BE.
Điểm đồng bộ SRS: `srs-fr-08-danh-gia.md:551-554, 569-585`.
**→ Kết luận: Loại 1 — Lỗi phần mềm, Dev sửa theo SRS: bổ sung 2 ô kinh phí nhập tay + bộ số liệu tự động theo FR-VI-07, gỡ 2 ô "Tiêu đề"/"Nội dung" thừa ngoài Inputs (phân kỳ 2 bước).** **✅ BA duyệt 2026-07-24.**

---

### LBCDG_04 — Tên nút xuất "Xuất báo cáo" vs "Xuất XLSX"/"Xuất DOCX"

**(1) Phần mềm đúng SRS chưa?** SAI (lệch tên + số lượng nút) — SCR #53 mô tả **2 nút** riêng "[Xuất XLSX]" và "[Xuất DOCX]", xuất theo mẫu TT17/2025 (`srs-fr-08-danh-gia.md:889`); đầu ra FR-VI-07 #2 yêu cầu có cả tệp Excel (.xlsx) và Word (.docx) (`:595`). Chữ trong ngoặc vuông ở màn hình là tên nút thực tế (giống [Lưu nháp], [Trình phê duyệt]) nên là đặc tả. App chỉ có 1 nút "Xuất báo cáo" (xuất .xlsx đúng chức năng). Việc thiếu xuất Word đã tách thành lỗi riêng **BUG-LBCDG_05** (chưa xử lý); case này chỉ xét tên + số lượng nút.
**(2) Đối tác yêu cầu có khác SRS không? Khác gì?** KHÔNG — đối tác kỳ vọng nút xuất theo định dạng ("Xuất Excel"), đúng hướng SCR #53.
**(3) Yêu cầu đó có bắt buộc cho luồng nghiệp vụ không?** CÓ → phải sửa (ưu tiên thấp). Khi khôi phục xuất Word (BUG-LBCDG_05), trả về đúng cấu trúc 2 nút và đặt nhãn "Xuất XLSX" / "Xuất DOCX" theo SCR #53. Owner Dev FE, nên gộp cùng đợt fix BUG-LBCDG_05.
**→ Kết luận: Loại 1 — Lỗi phần mềm, Dev sửa theo SRS: khi khôi phục xuất Word (BUG-LBCDG_05), trả về đúng cấu trúc 2 nút và đặt nhãn "Xuất XLSX" / "Xuất DOCX" theo SCR #53.** **✅ BA duyệt 2026-07-24.**

---

### TPDBC_03 — Trình phê duyệt BC ở sai trạng thái: message khác SRS

**(1) Phần mềm đúng SRS chưa?** **SRS mâu thuẫn nội bộ**. *(Đã đối chiếu evidence 2026-07-24)* Ảnh TPDBC_03.jpg: tab Báo cáo của đợt chưa ở BAO_CAO hiển thị empty-state **"Chưa hoàn thành đánh giá"** (Số vụ việc đánh giá = 0), KHÔNG có nút Trình duyệt để bấm và KHÔNG trả 404 "Báo cáo đánh giá không tồn tại" như nhận định cũ. Chuỗi "Chưa hoàn thành đánh giá" trùng đúng SRS `ERR-DG-BC-01` "Đợt chưa hoàn thành đánh giá" tại FR-VI-07 (`srs-fr-08-danh-gia.md:606`); trong khi FR-VI-08 mục E1 lại đặt chuỗi khác cho cùng điều kiện "đợt chưa ở BAO_CAO": `ERR-DG-TR-01` "Đợt không ở trạng thái đã lập BC" (`:670`), với điều kiện tiên quyết BAO_CAO tại `:631`. App chọn chuỗi FR-VI-07 — chuỗi vốn được SRS công nhận, không phải trả sai bậy.
**(2) Đối tác yêu cầu có khác SRS không? Khác gì?** CÓ — Kết quả mong đợi (cột K) là chuỗi `ERR-DG-TR-01` "Đợt không ở trạng thái đã lập báo cáo" (FR-VI-08); app hiển thị `ERR-DG-BC-01`. Khác nhau vì SRS có 2 chuỗi cho cùng tình huống chặn.
**(3) Yêu cầu đó có bắt buộc cho luồng nghiệp vụ không?** CÓ (BA phải gỡ mâu thuẫn để nhất quán chuỗi chặn). Ưu tiên thấp (UI đã chặn, không có nút để bấm). Điểm đồng bộ SRS: gỡ mâu thuẫn `srs-fr-08-danh-gia.md:606` (ERR-DG-BC-01) ↔ `:670` (ERR-DG-TR-01).

**→ Kết luận: Loại 2 — Cập nhật SRS rồi Dev làm theo SRS mới: gỡ mâu thuẫn ERR-DG-BC-01 ↔ ERR-DG-TR-01, thống nhất một chuỗi chặn.** ✅ BA chốt 2026-07-24: dùng ERR-DG-TR-01 (Dev đổi câu app), bỏ ERR-DG-BC-01.
> **Phương án xử lý (cập nhật SRS):** gỡ mâu thuẫn hai chuỗi cho cùng điều kiện "Đợt không ở BAO_CAO" — `srs-fr-08-danh-gia.md:606` (FR-VI-07 E1 `ERR-DG-BC-01` "Đợt chưa hoàn thành đánh giá") ↔ `:670` (FR-VI-08 E1 `ERR-DG-TR-01` "Đợt không ở trạng thái đã lập BC"). Chuẩn hóa theo `ERR-DG-TR-01` (đã chốt): sửa `:606` bỏ `ERR-DG-BC-01`, thống nhất một chuỗi chặn. Sau khi SRS cập nhật, Dev đổi chuỗi empty-state tab Báo cáo sang "Đợt không ở trạng thái đã lập BC" theo `ERR-DG-TR-01`.

---

_Đã tự xác minh toàn bộ citation của phiếu trong `srs-fr-08-danh-gia.md` và tra chéo baseline `srs-v3.5.md` (UI-08, UI-11, H7, DG-04). Các mã lỗi/chuỗi dẫn trong phiếu đều khớp file gốc; điểm khác biệt nhận định so với QA nằm ở việc áp quy ước dùng chung baseline và coi bảng Error Handling là đặc tả chính thức._

_**Kiểm chứng bằng evidence UAT (Google Sheet + ảnh) — 2026-07-24.** Đã đọc nguyên văn cột Kết quả mong đợi (K) + Kết quả thực tế (L) và xem ảnh đính kèm (M) của 13 case. Ba chỗ đã sửa tại chỗ do lệch với bằng chứng: (1) **TPDBC_03** — app thực tế hiển thị "Chưa hoàn thành đánh giá" (= SRS ERR-DG-BC-01, dòng 606), KHÔNG phải "Báo cáo đánh giá không tồn tại"/ERR-VAL-BC-DG-02 như nhận định cũ; bản chất là mâu thuẫn nội bộ SRS giữa ERR-DG-BC-01 (dòng 606) và ERR-DG-TR-01 (dòng 670). (2) **LKHDG_19** — thẻ chi tiết app ĐÃ hiển thị "Mục tiêu"; nhận định cũ "Mục tiêu cũng vắng" là sai, trường thiếu duy nhất là "Cơ quan được đánh giá". (3) **LKHDG_02** — ảnh danh sách đính kèm không có cột "Tên đợt" nên chưa xác nhận được hành vi "cắt bớt + ..."; đã thêm lưu ý đề nghị đối tác/CĐT xác nhận lại. Mười case còn lại (LKHDG_03, LKHDG_10, PCNTHDG_06, CVVDG_01/_02/_04, THDG_02/_03, LBCDG_02/_04) khớp đúng Expected/Actual + ảnh, giữ nguyên kết luận. Kết luận "Tròn năm" (TT17) đúng, app "Trọn năm" sai — được ảnh CVVDG_01/THDG_02 xác nhận app đang hiển thị "Trọn năm"._
