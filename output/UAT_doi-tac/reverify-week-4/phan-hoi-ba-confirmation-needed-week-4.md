# Phản hồi BA — 24 câu hỏi UAT tuần 4 (phiếu `ba-confirmation-needed-week-4.md`)

**Ngày lập:** 30/07/2026
**Phiếu nguồn:** `Week4/Yêu cầu/ba-confirmation-needed-week-4.md` — 24 câu hỏi (BA-01…BA-24), 24 dòng test case
**Quy trình áp dụng:** `docs/Reference/Fix bug KTĐL/QUY-TRINH-phan-tich-bug-nghiep-vu.md`
**Bản chấm chuẩn (`.md`):** `_bmad-output/planning-artifacts/srs-v3.5/` — `srs-v3.5.md`, `srs-fr-13-tv-nhanh.md`, `srs-fr-15-ct-htpldn.md`, `srs-fr-16-api.md`, `srs-fr-02-hoi-dap.md`, `CHANGELOG-v3-to-v3.5.md`
**Bản bàn giao (`.docx`):** `docs/Reference/HTPLDN-PTYC-CT-v2.0.docx` — bàn giao 10/07/2026 qua nhóm Zalo (BA xác nhận đây là bản đối tác cầm khi kiểm thử tuần 4 ngày 27/07/2026)
**CSV baseline:** `docs/Reference/Danh-sach-transaction_v1.1_2026-03-27.md` — UC154, UC155, UC156, UC178
**Sheet theo dõi:** tab `UAT_TGPL Doanh Nghiệp-tuần 4` — xem mục "Cập nhật sheet" ở cuối phiếu

---

## Tình trạng duyệt

**BA đã duyệt toàn bộ 24 mục ngày 30/07/2026.** Quyết định của từng mục đóng dấu ngay dưới phần Kết luận của mục đó.

**Sửa SRS là đợt tách biệt, chưa làm ở lượt này** — theo nguyên tắc nền 1 của quy trình: chốt trong phiếu trước, sửa SRS sau. Danh sách việc gom theo tệp ở cuối phiếu.

---

## Ghi chú phương pháp

### Kết quả đảo chiều so với tuần 3 — phải nói rõ để không áp nhầm khuôn

Tuần 2–3 có ~60 ca dạng **Loại 4A**: `.docx` mô tả thừa, `.md` cố ý không có, nên giữ nguyên phần mềm và sửa tài liệu bàn giao. Tuần 4 **ngược lại**: ở phần lớn các điểm đang tranh chấp, bản `.docx` mô tả **đầy đủ và đúng hơn** bản `.md`, và cây trọng tài chốt theo `.docx`.

Vì kết luận đảo chiều nên phải nêu bằng chứng thay vì khẳng định suông. Đã trích cả `HTPLDN-PTYC-CT-v1.0.docx` lẫn `v2.0` rồi đếm số lần xuất hiện của từng chuỗi đang tranh chấp:

| Chuỗi trong `.docx` | v1.0 | v2.0 | Có trong `.md`? |
|---|:-:|:-:|:-:|
| `kho-cau-hoi-{YYYYMMDD-HHmm}` (tên tệp xuất kho câu hỏi) | 1 | 1 | Không |
| `DanhSachChuongTrinh_` (tên tệp xuất chương trình) | 1 | 1 | Không |
| "Bạn đang thay thế…" (cảnh báo ghi đè) | 1 | 1 | Không |
| "lịch sử thẩm định" | 1 | 1 | Không |
| "Không tìm thấy phiên tư vấn phù hợp" | 1 | 1 | Không |
| "Bạn có chắc chắn muốn đánh dấu câu hỏi…" | 1 | 1 | Không |
| "Khối thông tin nhanh" | 4 | 4 | Không |

⇒ Toàn bộ đều là nội dung **có sẵn từ v1.0, giữ nguyên qua v2.0**. Đúng cơ chế đã mô tả ở nguyên tắc nền 6: bản `.docx` được vá dần từ v1.0, chỉ thêm/sửa chứ không gỡ. Điểm khác tuần 3 là **lần này nội dung đọng lại đó phần lớn còn giá trị nghiệp vụ**, nên phân định ra **hướng B** (bổ sung `.md`) chứ không phải hướng A.

**Đơn vị kiểm thử ghi nhận đúng theo tài liệu được giao ở toàn bộ 24 mục.** Không mục nào đối tác quan sát sai. Vì vậy phiếu này **không có mục nào Reject**.

### Cách phân định A hay B — không suy từ một tín hiệu

Với mỗi mục chỉ có ở `.docx`, đã tra đủ cây trọng tài (quyết định BA/CHANGELOG → mô hình dữ liệu/§Outputs → SCR ↔ Processing → CSV UC → pháp luật/CĐT) rồi mới chốt. Kết quả:

- **Hướng B (bổ sung `.md`) — 17 mục:** có ít nhất một tầng của cây trọng tài đỡ lưng (quyết định CHANGELOG đã chốt, giao dịch CSV bắt buộc, quy ước dùng chung ở baseline, hoặc ràng buộc entity).
- **Hướng A (`.docx` thừa, gỡ ở bản kế tiếp) — 3 mục:** BA-13 phần nút Lưu nháp · BA-20 điểm 4 khối thông tin nhanh · BA-23 cột liên kết Đợt báo cáo. Cả ba đều có **đối chứng cho thấy `.md` bỏ có chủ đích**, nêu trong từng mục.
- **Loại 3 (ngoài cả hai tài liệu) — 1 mục:** BA-21 vế "Lĩnh vực pháp lý". Đây là mục duy nhất đối tác đòi thêm ngoài cả `.md` lẫn `.docx`.
- **Loại 1/2 thuần (không liên quan lệch tài liệu) — 3 mục:** BA-08, BA-09, BA-22.

### Phản hồi gửi đối tác — chỉ viết khi không sửa hoặc không sửa một phần

Theo quy tắc chung của phiếu. Cụ thể ở đợt này:

- **Câu chung cho các mục chấp thuận** (17 mục hướng B + Loại 1/2): *"Ghi nhận của Quý đơn vị là đúng. Nội dung này đã được chấp thuận và cập nhật vào đặc tả; đơn vị phát triển sẽ chỉnh sửa phần mềm theo đặc tả đã cập nhật. Kính đề nghị Quý đơn vị giữ nguyên Kết quả mong đợi."* — điền cho các dòng tương ứng, **không** thay đổi trạng thái đang xử lý.
- **Phản hồi riêng** chỉ viết ở BA-07 (ý phụ không tái hiện), BA-13 (ý Lưu nháp), BA-20 (điểm 4), BA-21 (vế Lĩnh vực), BA-23.

### Khối lượng phát sinh — cần biết trước khi duyệt

23/24 dòng còn việc cho Dev. Phần lớn là sửa nhỏ ở giao diện (nhãn, câu thông báo, định dạng ngày, hộp thoại xác nhận, nút Xóa bộ lọc). Hai nhóm nặng hơn, nên xếp ưu tiên trước: **Xuất Excel kho câu hỏi** (BA-02/03/07) và **thu tập trạng thái Tư vấn nhanh về 4** (BA-09). Riêng BA-22, sau quyết định ngày 30/07 thì Dev chỉ còn lỗi 400 của giao diện tìm kiếm vụ việc — việc đổi đường dẫn chuyển sang phía tài liệu.

### Gom cụm

Bốn cụm được phân tích và chốt phương án một lần, nhưng **cập nhật sheet vẫn theo từng dòng**:

- **Cụm Xuất Excel kho câu hỏi:** BA-02 (có trong phạm vi không) · BA-03 (tên tệp, tập cột) · BA-07 (không có dữ liệu). BA-02 là câu chặn.
- **Cụm câu chữ trạng thái rỗng / bộ lọc:** BA-17 · BA-18.
- **Cụm rủi ro mất nội dung đang soạn:** BA-11 · BA-13.
- **Cụm đầu trang và dòng danh sách Chương trình:** BA-20 · BA-23 · BA-24.

---

## QLKCHTV_02 — Ba ô lọc Lĩnh vực / Nguồn / Trạng thái mặc định "Tất cả" *(BA-01)*

**(1) Phần mềm đúng `.md` chưa?** ĐÚNG. Quy ước UI-11 (`srs-v3.5.md:580`) chỉ ràng buộc ô lọc **chọn nhiều**; ba ô đang xét là chọn đơn nên không thuộc phạm vi. Thanh lọc SCR-X2-01 (`srs-fr-13-tv-nhanh.md:530`) không nói giá trị mặc định.

**(1b) Bản `.docx` có nói khác không?** CÓ. Mục **4.13.1.2.2**, bảng "Điều kiện tìm kiếm / bộ lọc", cột **Mặc định** của cả ba dòng 2 (Lĩnh vực pháp lý), 3 (Nguồn), 4 (Trạng thái) đều ghi **"Tất cả"**.

**(2) Đối tác yêu cầu khác gì?** Đòi ba ô hiển thị sẵn "Tất cả" thay vì chữ mờ gợi ý — đúng theo `.docx` họ cầm.

**(3) Có bắt buộc cho luồng nghiệp vụ không?** Không chặn luồng. Danh sách vẫn trả đủ bản ghi khi chưa chọn lọc.

**Phân định hướng:** Tín hiệu mở đầu — `.md` **có** dùng quy ước mặc định "Tất cả" cho ô lọc ở **4 nhóm khác** (`srs-fr-01-dashboard.md:742` và `:744`, `srs-fr-10-quan-tri.md:1829`, `srs-fr-09-bieu-mau.md:619`), thiếu đúng ở nhóm X.2 ⇒ nghi bị sót. Tra tiếp cây trọng tài: không tầng nào chốt ngược lại. → **Hướng B**.

| Trường | Nội dung |
|---|---|
| Bản `.docx` đối chiếu | `HTPLDN-PTYC-CT-v2.0.docx` · 10/07/2026 · nhóm Zalo |
| Trích `.docx` | Mục 4.13.1.2.2, bảng bộ lọc, dòng 2–4, cột Mặc định = "Tất cả" |
| Trích `.md` | `srs-fr-13-tv-nhanh.md:530` — mô tả thanh lọc, không nêu giá trị mặc định |
| Hướng | **B** — `.md` bị sót (quy ước đã dùng ở 4 nhóm khác) |
| Dev action | Có (Minor) |
| Doc action | BA bổ sung `.md`; `.docx` giữ nguyên |
| Sheet | Giữ xử lý |

**→ Kết luận: Loại 4B — bản gốc bị sót, bổ sung đặc tả rồi Dev làm theo. Ba ô lọc Lĩnh vực / Nguồn / Trạng thái của màn Kho câu hỏi hiển thị mặc định "Tất cả". Dev action: Có (Minor). Doc action: BA bổ sung. Sheet: Giữ xử lý.** **✅ BA duyệt 2026-07-30.**

**Phương án xử lý (cập nhật SRS):** `srs-fr-13-tv-nhanh.md:530` — thêm vào mô tả thanh lọc: ba ô Lĩnh vực / Nguồn / Trạng thái là ô chọn đơn, giá trị mặc định "Tất cả", chọn "Tất cả" tương đương không áp điều kiện lọc.

---

## QLKCHTV_12, QLKCHTV_13 — Xuất Excel kho câu hỏi có thuộc phạm vi không *(BA-02 — câu chặn của cụm)*

**(1) Phần mềm đúng `.md` chưa?** Không kết luận được theo file FR: Processing FR-X.2-01 dừng ở bước 7 (`srs-fr-13-tv-nhanh.md:111`–`:119`), thanh công cụ SCR-X2-01 chỉ khai 3 nút (`:528`), Quy tắc tương tác không có dòng nào về Xuất Excel (`:543`–`:546`). Phần mềm **đã dựng** nút này và chạy được.

**(1b) Bản `.docx` có nói khác không?** CÓ. Mục **4.13.1.2.3** mục số 6 "Xuất Excel" mô tả đầy đủ: xuất theo bộ lọc hiện tại, tối đa 10.000 dòng, ba trường hợp (có dữ liệu / vượt giới hạn / không có dữ liệu).

**(2) Đối tác yêu cầu khác gì?** Không đòi thêm gì ngoài tài liệu — họ kiểm đúng mục 4.13.1.2.3.

**(3) Có bắt buộc cho luồng nghiệp vụ không?** CÓ. Đây là một giao dịch bắt buộc của UC154.

**Phân định hướng:** Cây trọng tài chốt ngay ở **tầng 1** — CHANGELOG v3→v3.5 mục 9 (`CHANGELOG-v3-to-v3.5.md:2443`–`:2449`) ghi rõ đã chốt bổ sung Xuất Excel vào FR-X.2-01 và SCR-X2-01, kèm cả ba vị trí phải sửa. Quyết định đã chốt nhưng **chưa được áp vào file FR**. **Tầng 4** củng cố: CSV UC154 giao dịch 4 — *"Cán bộ nghiệp vụ TW,BN,ĐP xuất danh sách kho câu hỏi, tư vấn; Hệ thống kiểm tra điều kiện và thực hiện xuất file định dạng excel"*. → **Hướng B**, không có gì phải cân nhắc thêm.

**→ Kết luận: Loại 2 — SRS bị sót một quyết định đã chốt; BA cập nhật SRS rồi Dev làm theo. Chức năng Xuất Excel kho câu hỏi NẰM TRONG phạm vi; nút đang có trên hệ thống là đúng, giữ lại. Dev action: Có (theo BA-03 và BA-07). Doc action: BA áp CHANGELOG mục 9 vào file FR. Sheet: Giữ xử lý (cả row 6 và row 7).** **✅ BA duyệt 2026-07-30.**

**Phương án xử lý (cập nhật SRS):**
- `srs-fr-13-tv-nhanh.md:119` — thêm bước 8 vào Processing FR-X.2-01: xuất danh sách theo bộ lọc hiện tại, giới hạn 10.000 dòng, trả tệp tải về.
- `:528` — thanh công cụ SCR-X2-01 thêm nút `[Xuất Excel]` (thành 4 nút).
- `:546` — Quy tắc tương tác thêm một dòng cho nút Xuất Excel.
- Nội dung chi tiết của ba mục trên lấy theo BA-03 và BA-07 dưới đây.

> **Đóng câu chặn:** BA-03 và BA-07 có cơ sở trả lời.

---

## QLKCHTV_12, QLKCHTV_37 — Tên tệp và tập cột của tệp Excel xuất ra *(BA-03)*

**(1) Phần mềm đúng `.md` chưa?** `.md` im lặng hoàn toàn về tên tệp và tập cột của nhóm X.2 — hệ quả trực tiếp của BA-02. Đo thực tế: tên tệp `kho-cau-hoi-20260727.xlsx` (thiếu giờ phút), tệp có 7 cột trong khi màn hình có 12 cột.

**(1b) Bản `.docx` có nói khác không?** CÓ, và nói rất cụ thể. Mục **4.13.1.2.3** mục 6:
- Tên tệp: **`kho-cau-hoi-{YYYYMMDD-HHmm}.xlsx`** — có giờ phút.
- Tập cột: *"bao gồm toàn bộ cột đang hiển thị cộng thêm cột «Câu hỏi (đầy đủ)», «Câu trả lời (đầy đủ)» và «Ngày cập nhật» để phục vụ báo cáo"*.

Với `QLKCHTV_37` (xuất Excel khối Đánh giá của phiên tư vấn nhanh), mục **4.13.2.3.3** mục 8 cũng quy định đủ: tên tệp `danh-gia-tv-nhanh-{mã phiên}-{YYYYMMDD-HHmm}.xlsx`; cột gồm mã phiên, điểm đánh giá, nhận xét, ngày đánh giá, tên doanh nghiệp, mã doanh nghiệp; nút chỉ hiển thị khi phiên Hoàn thành và đã có ít nhất một đánh giá.

**(2) Đối tác yêu cầu khác gì?** Kỳ vọng của phiếu (`HHmm`, có "Ngày cập nhật", "Câu hỏi (đầy đủ)", "Câu trả lời (đầy đủ)") **trùng từng chữ** với `.docx`.

**(3) Có bắt buộc cho luồng nghiệp vụ không?** CÓ với phần giờ phút: xuất hai lần trong ngày thì tệp thứ hai bị trình duyệt thêm hậu tố, cán bộ dễ nhầm tệp khi đối soát báo cáo. Tập cột: cần, vì tệp hiện tại cắt mất nội dung đầy đủ nên không dùng để báo cáo được.

**Phân định hướng:** Đi theo BA-02 — đã là hướng B thì lấy luôn nội dung `.docx` làm căn cứ bổ sung. Đối chiếu thêm: hai nhóm khác của `.md` đều có mẫu tên tệp kèm giờ phút (`srs-fr-02-hoi-dap.md:151` — `HoiDap_{YYYYMMDD_HHmm}.xlsx`; `srs-fr-12-tv-chuyen-sau.md:162`). → **Hướng B**.

**→ Kết luận: Loại 4B — bổ sung đặc tả rồi Dev sửa. Chốt tên tệp `kho-cau-hoi-{YYYYMMDD-HHmm}.xlsx` và tập cột theo `.docx`; khối Đánh giá tư vấn nhanh chốt theo mục 4.13.2.3.3. Dev action: Có. Doc action: BA bổ sung. Sheet: Giữ xử lý (row 6, row 19).** **✅ BA duyệt 2026-07-30.**

**Phương án xử lý (cập nhật SRS):**
- `srs-fr-13-tv-nhanh.md:119` (bước 8 mới của FR-X.2-01) — ghi tên tệp `kho-cau-hoi-{YYYYMMDD-HHmm}.xlsx`; tập cột gồm **các cột dữ liệu của bảng danh sách** (Mã, Câu hỏi, Câu trả lời, Lĩnh vực, Từ khóa, Nguồn, Trạng thái, Công khai, Hiệu lực, Điểm TB, Ngày tạo — không lấy ô chọn và cột Hành động), **bổ sung** ba cột "Câu hỏi (đầy đủ)", "Câu trả lời (đầy đủ)", "Ngày cập nhật".
- `:574` (khối Đánh giá trong SCR-X2-03) — ghi tên tệp và 6 cột theo mục 4.13.2.3.3, kèm điều kiện hiển thị nút.

> **Chuyển kèm cho Dev (QA nêu, chưa kết luận được):** thân yêu cầu xuất đang truyền `pageSize: 20`. Dữ liệu hiện chỉ 13 bản ghi nên chưa phân biệt được tệp xuất có bị cắt theo trang hay không. Đặc tả yêu cầu xuất theo **bộ lọc**, không theo trang đang xem, giới hạn 10.000 dòng — đề nghị Dev tự kiểm điểm này.

---

## QLKCHTV_10, QLKCHTV_12 — Nhãn tiếng Việt của nguồn `IMPORT` *(BA-04)*

**(1) Phần mềm đúng `.md` chưa?** `.md` chỉ quy định **màu thẻ** cho ba giá trị nguồn (`srs-fr-13-tv-nhanh.md:532`), không quy định chữ hiển thị. Phần mềm đang Việt hoá 2/3 giá trị, riêng `IMPORT` giữ nguyên chữ tiếng Anh ở cả ba nơi (bảng danh sách, màn chi tiết, tệp Excel).

**(1b) Bản `.docx` có nói khác không?** CÓ. Mục **4.13.1.2.2** dòng 3 và dòng 14 đều ghi ba nhãn: *"Tự động"*, *"Thủ công"*, **"Nhập Excel"**.

**(2) Đối tác yêu cầu khác gì?** Đòi hiển thị "Nhập Excel" — đúng `.docx`.

**(3) Có bắt buộc không?** Không chặn luồng, nhưng đây là phần mềm tiếng Việt phục vụ cán bộ; để lẫn một nhãn tiếng Anh giữa hai nhãn đã Việt hoá là lỗi hiển thị rõ ràng (QA đã log riêng phần không nhất quán).

**Phân định hướng:** `.docx` khớp với chính tên nút "Nhập Excel" mà `.md` đã dùng ở `:528`. Không tầng nào của cây trọng tài đòi giữ chữ tiếng Anh. → **Hướng B**.

**→ Kết luận: Loại 4B — chốt nhãn hiển thị của nguồn `IMPORT` là "Nhập Excel", đồng bộ cả ba nơi (bảng danh sách, màn chi tiết, tệp Excel xuất ra). Dev action: Có (Minor, gộp `BUG-QLKCHTV_10`). Doc action: BA bổ sung nhãn vào `.md`. Sheet: Giữ xử lý (row 5, row 6).** **✅ BA duyệt 2026-07-30.**

**Phương án xử lý (cập nhật SRS):** `srs-fr-13-tv-nhanh.md:532` — bổ sung nhãn hiển thị vào cạnh quy định màu: `TU_DONG` → "Tự động", `THU_CONG` → "Thủ công", `IMPORT` → "Nhập Excel".

---

## QLKCHTV_14 — Màn chi tiết câu hỏi có hiển thị "Lịch sử thẩm định" không *(BA-05)*

**(1) Phần mềm đúng `.md` chưa?** ĐÚNG theo câu chữ hiện có: `srs-fr-13-tv-nhanh.md:545` liệt kê màn chi tiết gồm câu hỏi, câu trả lời, lĩnh vực, từ khóa, nguồn, người tạo — không có lịch sử thẩm định. Web cũng chưa hiển thị người tạo.

**(1b) Bản `.docx` có nói khác không?** CÓ. Mục **4.13.1.2.3** mục 8 "Xem": *"…hiển thị đầy đủ câu hỏi, câu trả lời (nội dung định dạng), lĩnh vực pháp lý, từ khóa, nguồn, **người tạo, thời điểm tạo và cập nhật, lịch sử thẩm định**"*.

**(2) Đối tác yêu cầu khác gì?** Đòi mục "Lịch sử thẩm định" — đúng `.docx`.

**(3) Có bắt buộc cho luồng nghiệp vụ không?** CÓ. `.md:536` đã bắt buộc: khi Từ chối thì nhập lý do (bắt buộc) và gửi thông báo cho cán bộ tạo. Nhưng hiện **không có chỗ nào tra lại lý do đó** sau khi thông báo trôi đi — cán bộ bị từ chối phải chỉnh sửa và trình lại mà không xem lại được lý do. CSV UC155 định nghĩa hai giao dịch duyệt và từ chối kèm lý do; UC154 có giao dịch "xem chi tiết kho câu hỏi". Thiếu lịch sử thẩm định là **mất vết xử lý của một luồng phê duyệt**, không phải chuyện trải nghiệm.

**Phân định hướng:** Cây trọng tài — **tầng 3** (SCR ↔ Processing): `.md` có bước xử lý duyệt/từ chối kèm lý do nhưng không có nơi hiển thị; **tầng 4** CSV UC155 xác nhận luồng thẩm định là giao dịch chính thức. Thêm nữa QA đo được máy chủ **đã trả sẵn** đủ nguyên liệu (người gửi duyệt, ngày gửi duyệt, người duyệt, ngày duyệt, ghi chú phê duyệt). → **Hướng B**.

**→ Kết luận: Loại 4B — bổ sung đặc tả rồi Dev dựng phần hiển thị. Màn chi tiết câu hỏi hiển thị "Lịch sử thẩm định" gồm các mốc: gửi duyệt (người, thời điểm) · duyệt (người, thời điểm) · từ chối (người, thời điểm, lý do bắt buộc); kèm người tạo và thời điểm tạo/cập nhật. Dev action: Có (Medium — dữ liệu máy chủ đã có sẵn). Doc action: BA bổ sung. Sheet: Giữ xử lý (row 8).** **✅ BA duyệt 2026-07-30.**

**Phương án xử lý (cập nhật SRS):**
- `srs-fr-13-tv-nhanh.md:545` — bổ sung vào mô tả chi tiết Q&A: người tạo, thời điểm tạo và cập nhật, khối "Lịch sử thẩm định" với ba loại mốc nêu trên.
- Bảng thuộc tính entity `KHO_CAU_HOI` (`:683`–`:698`) — bổ sung các trường phục vụ khối này; xử lý chung với BA-08.

---

## QLKCHTV_18 — Bật/tắt hiệu lực: có hộp thoại xác nhận không, câu chữ chuẩn là gì *(BA-06)*

**(1) Phần mềm đúng `.md` chưa?** Phần mềm đang **làm nhiều hơn** `.md`: `srs-fr-13-tv-nhanh.md:533` mô tả đây là thao tác gạt và cập nhật ngay, không nhắc hộp thoại; web lại có hộp thoại xác nhận cả hai chiều nhưng câu chữ khác kỳ vọng và không nhắc mã câu hỏi.

**(1b) Bản `.docx` có nói khác không?** CÓ. Mục **4.13.1.2.3** mục 10 "Bật/tắt hiệu lực": *"…hệ thống hiển thị cửa sổ xác nhận «Bạn có chắc chắn muốn đánh dấu câu hỏi «{mã}» là «{hết hiệu lực/có hiệu lực}»?»"*, kèm ba trường hợp xác nhận tắt / xác nhận bật / bỏ xác nhận.

**(2) Đối tác yêu cầu khác gì?** Đòi đúng câu chữ đó — đúng `.docx`.

**(3) Có bắt buộc cho luồng nghiệp vụ không?** CÓ ở mức vừa. Tắt hiệu lực làm câu hỏi **biến mất khỏi Cổng Pháp luật quốc gia và khỏi kết quả tra cứu trong phiên tư vấn** — hệ quả ra ngoài hệ thống. Quy ước chung UI-04 (`srs-v3.5.md:573`) đã đặt nguyên tắc hỏi xác nhận trước thao tác gỡ bỏ. Việc nhắc mã câu hỏi trong câu xác nhận là để cán bộ không gạt nhầm dòng.

**Phân định hướng:** Việc `.md:538` có "modal xac nhan" cho Công khai mà `:533` không có chỉ là **tín hiệu**, và tín hiệu này bị chính phần mềm bác: hệ thống đã dựng hộp thoại, đúng tinh thần UI-04 và đúng `.docx`. → **Hướng B**, chi phí gần như bằng không vì chỉ sửa câu chữ.

**→ Kết luận: Loại 4B — giữ hộp thoại xác nhận, chốt câu chữ theo `.docx`: "Bạn có chắc chắn muốn đánh dấu câu hỏi «{mã}» là «{hết hiệu lực / có hiệu lực}»?", hai nút Hủy / Đồng ý. Dev action: Có (Minor — sửa câu chữ, bổ sung mã câu hỏi). Doc action: BA bổ sung câu chuẩn vào `.md`. Sheet: Giữ xử lý (row 10).** **✅ BA duyệt 2026-07-30.**

**Phương án xử lý (cập nhật SRS):** `srs-fr-13-tv-nhanh.md:533` — sửa mô tả toggle hiệu lực: gạt công tắc mở hộp thoại xác nhận với câu chữ chuẩn nêu trên; xác nhận thì cập nhật hiệu lực và ghi nhật ký, bỏ xác nhận thì không thực hiện.

---

## QLKCHTV_13 — Xuất Excel khi bộ lọc không có kết quả *(BA-07)*

**(1) Phần mềm đúng `.md` chưa?** `.md` im lặng — hệ quả của BA-02. Đo thực tế: lọc ra 0 kết quả rồi bấm Xuất Excel thì vẫn tải về tệp chỉ có dòng tiêu đề, không có thông báo nào.

**(1b) Bản `.docx` có nói khác không?** CÓ. Mục **4.13.1.2.3** mục 6, Trường hợp 3: *"Không có dữ liệu, hệ thống thông báo «Không có dữ liệu để xuất»"* — tức **chặn kèm thông báo**, không xuất tệp rỗng.

**(2) Đối tác yêu cầu khác gì?** Đòi đúng câu đó — đúng `.docx`.

**(3) Có bắt buộc không?** CÓ ở mức vừa: tệp rỗng chỉ có tiêu đề dễ bị hiểu nhầm là "kho không có câu hỏi nào", trong khi thực tế chỉ là bộ lọc quá hẹp.

**Phân định hướng:** **Tầng 3** của cây trọng tài chốt luôn — nhóm Chương trình HTPLDN của chính `.md` đã có đúng quy tắc này: `srs-fr-15-ct-htpldn.md` E1 = *"Không có chương trình nào để xuất"* (INFO). Cùng một hành vi xuất Excel, một nhóm có quy định, nhóm X.2 thiếu ⇒ bị sót. → **Hướng B**.

**→ Kết luận: Loại 4B — chốt: bộ lọc không có kết quả thì chặn xuất và hiển thị "Không có dữ liệu để xuất". Dev action: Có (Minor). Doc action: BA bổ sung. Sheet: Giữ xử lý (row 7).** **✅ BA duyệt 2026-07-30.**

**Phương án xử lý (cập nhật SRS):** `srs-fr-13-tv-nhanh.md` — bảng Error Handling của FR-X.2-01 (`:148`–`:153`) thêm một dòng mức INFO: điều kiện "không có dữ liệu để xuất", phản hồi "Không có dữ liệu để xuất"; đặt mã theo dãy `INF-KHO-XL-01` (đã kiểm không trùng trong file).

**Phản hồi gửi đối tác — riêng ý phụ:** *"Về ý «tệp xuất ra chính là tệp cũ»: chúng tôi đã kiểm tra lại ba lần với ba phạm vi lọc khác nhau và tệp tải về khác nhau ở cả ba lần (không lọc 13 bản ghi — 8.075 byte; lọc theo lĩnh vực 6 bản ghi — 7.433 byte; lọc không có kết quả — 6.655 byte), tức hệ thống có áp dụng bộ lọc khi xuất. Kính đề nghị Quý đơn vị kiểm tra lại và gửi kèm dung lượng từng tệp nếu vẫn tái hiện. Ý chính về thông báo khi không có dữ liệu đã được chấp thuận và sẽ chỉnh sửa."*

---

## QLKCHTV_02, _04, _14, _16 — Mâu thuẫn nội bộ về entity `KHO_CAU_HOI` *(BA-08)*

**(1) Phần mềm đúng `.md` chưa?** `.md` tự mâu thuẫn nên chưa chấm được: bốn chỗ coi `NHAP` là trạng thái hợp lệ (`srs-fr-13-tv-nhanh.md:103`, `:530`, `:534`, `:536`) trong khi ràng buộc entity loại nó ra (`:690`), và bản sao entity ở file chính còn cũ hơn nữa — chỉ 3 giá trị, thiếu cả `CONG_KHAI` và 5 trường công khai (`srs-v3.5.md:2216`, khối `:2204`–`:2222`).

**(1b) Bản `.docx` có nói khác không?** `.docx` **giải được mâu thuẫn**. Mục **4.13.1.2.2** dòng 4 và dòng 15 đều ghi **5 giá trị trạng thái**: "Nháp", "Chờ duyệt", "Đã duyệt", "Đã công khai", "Hết hiệu lực". Mục **4.13.1.2.3** mục 4 có nút "Lưu nháp" tạo bản ghi trạng thái "Nháp"; mục 12 "Từ chối" chuyển "Chờ duyệt" → "Nháp".

**(2) Đối tác yêu cầu khác gì?** Không đòi gì thêm; các phiếu liên quan chấm theo tập 5 trạng thái của `.docx`.

**(3) Có bắt buộc không?** CÓ. Nếu `NHAP` không hợp lệ thì hành động Từ chối ở `:536` không có trạng thái đích — luồng thẩm định gãy.

**Phân định hướng — chốt theo cây trọng tài:**
1. **Tầng 1:** không có quyết định BA/CHANGELOG nào bỏ `NHAP`.
2. **Tầng 2 (mô hình dữ liệu):** hai bản entity lệch nhau; bản ở file FR (`:690`) **mới hơn** bản ở file chính (`:2216` — thiếu `CONG_KHAI` và 5 trường công khai vốn đã được chốt qua CR Item-01). Bản mới thắng.
3. **Tầng 3:** ba chỗ mô tả màn hình và một bước xử lý đều dùng `NHAP` — ràng buộc entity đứng một mình đối lại.
4. **Tầng 4:** CSV UC155 có giao dịch từ chối kèm lý do, cần một trạng thái để câu hỏi quay về cho cán bộ sửa.

→ `NHAP` là trạng thái hợp lệ; ràng buộc entity ở `:690` và bản sao ở `srs-v3.5.md:2216` là chỗ bị sót.

**→ Kết luận: Loại 2 — SRS tự mâu thuẫn, BA cập nhật SRS rồi Dev làm theo. `KHO_CAU_HOI` có 5 trạng thái `NHAP / CHO_DUYET / DA_DUYET / CONG_KHAI / HET_HIEU_LUC`; bản trong `srs-fr-13-tv-nhanh.md` là bản chuẩn, bản trong file chính phải đồng bộ theo. Phần mềm hiện đã chạy đúng mô hình này, việc còn lại của Dev chỉ là đổi nhãn hiển thị "Bị từ chối" thành "Nháp". Dev action: Có (Minor — đổi nhãn, `BUG-QLKCHTV_02` giữ nguyên bản chất lỗi hiển thị, owner Dev FE). Doc action: BA đồng bộ 2 nơi. Sheet: Giữ xử lý (row 2, 4, 8, 9).** **✅ BA duyệt 2026-07-30.**

**Phương án xử lý (cập nhật SRS):**
- `srs-fr-13-tv-nhanh.md:690` — ràng buộc trạng thái thêm `NHAP` (thành 5 giá trị).
- `srs-v3.5.md:2216` — đồng bộ ràng buộc trạng thái đủ 5 giá trị.
- `srs-v3.5.md:2204`–`:2222` — đồng bộ bảng thuộc tính theo bản ở file FR: bổ sung 5 trường công khai (`cong_khai`, `anh_dai_dien`, `thoi_gian_dang_tai`, `mo_ta_cong_khai`, `file_dinh_kem_cong_khai`).
- Cả hai bản entity — bổ sung trường người tạo và các trường thẩm định (người gửi duyệt / ngày gửi duyệt / người duyệt / ngày duyệt / ghi chú phê duyệt) để đỡ phần hiển thị của `:545` và của BA-05. Đây là mâu thuẫn 2 mà phiếu QA nêu: `:545` đòi hiển thị "người tạo" nhưng bảng thuộc tính không khai trường nào.
- Ghi rõ trong CHANGELOG: bản entity ở file FR là bản chuẩn của nhóm X.2.

---

## QLKCHTV_22, QLKCHTV_26 — Tư vấn nhanh có 4 hay 6 trạng thái *(BA-09)*

**(1) Phần mềm đúng `.md` chưa?** SAI — phần mềm **vượt** đặc tả. `.md` chốt 4 trạng thái ở ba nơi độc lập: máy trạng thái SM-TVNHANH (`srs-fr-13-tv-nhanh.md:791`–`:825`), ràng buộc entity `TU_VAN_NHANH` (`:713`), ô lọc trạng thái (`:579`); danh sách 3 thẻ (`:567`). Web đang có 6 nhãn trạng thái, 4 thẻ, thanh tiến trình 5 bước.

**(1b) Bản `.docx` có nói khác không?** KHÔNG — `.docx` **cùng phía với `.md`**. Mục **4.13.2.2.2** dòng 2 ghi *"4 giá trị trạng thái phiên: «Mới», «Cán bộ trả lời», «Hoàn thành», «Hết hạn»"*; bảng thẻ phân loại chỉ có 3 thẻ (Tất cả / Chờ xử lý / Hoàn thành). Đây **không phải** ca lệch tài liệu.

**(2) Đối tác yêu cầu khác gì?** Không. Đối tác chấm theo 4 trạng thái / 3 thẻ, tức theo cả hai tài liệu.

**(3) Có bắt buộc không?** CÓ. Hai trạng thái thừa là `DANG_TIM_KIEM` và `DA_GOI_Y` — chúng chỉ có nghĩa trong mô hình **hệ thống tự tìm kiếm và tự sinh gợi ý**, là mô hình đã bị bỏ. Giữ lại thì phiên có thể rơi vào trạng thái không ai chuyển tiếp được.

**Nguồn gây hiểu nhầm:** CHANGELOG mục 6 và mục 7 (`CHANGELOG-v3-to-v3.5.md:2415`–`:2432`) có nhắc `DANG_TIM_KIEM` / `DA_GOI_Y`. Nhưng đọc kỹ thì đó là **mô tả delta của bản v3 cũ**, không phải quyết định cho v3.5. Chính v3.5 đã bỏ mô hình tự gợi ý, ghi rõ ở bốn nơi: mô tả FR-X.2-02 (`:173` — *"Hệ thống không tự động tìm kiếm mặc định và không hiển thị gợi ý tự động"*), Processing bước 2 (`:197`), Điều kiện chấp nhận (`:232`), và SCR-X2-03 (`:572`). Bản `.docx` mục **4.13.2.1** cũng ghi đúng như vậy.

**→ Kết luận: Loại 2 — SRS mâu thuẫn giữa CHANGELOG cũ và bản đang hiệu lực; chốt theo bản đang hiệu lực. Tư vấn nhanh có ĐÚNG 4 trạng thái (Mới / Cán bộ trả lời / Hoàn thành / Hết hạn) và 3 thẻ (Tất cả / Chờ xử lý / Hoàn thành). Hai trạng thái "Đang tìm kiếm" và "Đã gợi ý" đang chạy trên hệ thống là tàn dư của mô hình tự gợi ý đã bị bỏ — Dev gỡ. Dev action: Có. Doc action: BA đánh dấu hai mục CHANGELOG là mô tả v3 cũ, không còn hiệu lực. Sheet: Giữ xử lý (row 11, row 14).** **✅ BA duyệt 2026-07-30.**

**Phương án xử lý (cập nhật SRS):**
- Không sửa `:713`, `:791`–`:825`, `:579`, `:567` — bốn nơi này đã đúng.
- `CHANGELOG-v3-to-v3.5.md:2415`–`:2432` — thêm ghi chú: hai trạng thái `DANG_TIM_KIEM` / `DA_GOI_Y` thuộc mô hình tự gợi ý của v3, đã bỏ ở v3.5; các delta liên quan không còn áp dụng.
- Dev: ô lọc trạng thái về 4 nhãn, danh sách về 3 thẻ, thanh tiến trình vẽ theo 4 trạng thái của SM-TVNHANH. Cần rà dữ liệu đang mang hai trạng thái cũ trước khi gỡ.

> **Lưu ý gửi kèm Dev:** đây là mục có ảnh hưởng rộng nhất Luồng 2. Nên xử lý trước các mục nhỏ của cùng luồng để tránh sửa hai lần.

---

## QLKCHTV_22 — Cột "Ngày gửi" có hiển thị giờ phút không *(BA-10)*

**(1) Phần mềm đúng `.md` chưa?** Không kết luận được từ nhóm X.2: `.md:569` liệt kê cột nhưng không nêu định dạng; quy ước UI-06 (`srs-v3.5.md:576`) chỉ ghi định dạng ngày `dd/MM/yyyy`, không nói tới cột kiểu ngày-giờ. Đo thực tế: "Ngày gửi" hiển thị `27/07/2026` trong khi "Ngày cập nhật" ngay cạnh hiển thị `27/07/2026 11:54` — không nhất quán trong cùng một bảng.

**(1b) Bản `.docx` có nói khác không?** CÓ. Mục **4.13.2.2.2** dòng 11 ghi rõ: *"Ngày gửi | Ngày – giờ | … Định dạng dd/mm/yyyy HH:mm"*; dòng 12 "Ngày cập nhật" cùng định dạng.

**(2) Đối tác yêu cầu khác gì?** Đòi có giờ phút — đúng `.docx`.

**(3) Có bắt buộc không?** CÓ ở mức vừa. Thời điểm doanh nghiệp gửi câu hỏi là mốc tính thời hạn xử lý (hệ thống tự tính số phút xử lý theo `:717`) và là mốc tính tự hết hạn 30 ngày. Hiển thị mỗi ngày thì cán bộ không đối chiếu được với số liệu thời gian xử lý.

**Phân định hướng:** **Tầng 3** — chính `.md` đã lưu dữ liệu tới giây và tự tính thời gian xử lý theo phút; hiển thị mất phần giờ là mất thông tin ở khâu trình bày. Đối chứng: nhóm Hỏi đáp quy định rõ cột kiểu ngày-giờ dùng `dd/mm/yyyy HH:mm` (`srs-fr-02-hoi-dap.md:1043`). → **Hướng B**.

**→ Kết luận: Loại 4B — chốt các cột kiểu ngày-giờ của màn danh sách Tư vấn nhanh (Ngày gửi, Ngày trả lời, Ngày cập nhật) hiển thị `dd/mm/yyyy HH:mm`. Dev action: Có (Minor, gộp `BUG-QLKCHTV_22`). Doc action: BA bổ sung. Sheet: Giữ xử lý (row 11).** **✅ BA duyệt 2026-07-30.**

**Phương án xử lý (cập nhật SRS):** `srs-fr-13-tv-nhanh.md:569` — bổ sung định dạng `dd/mm/yyyy HH:mm` cho ba cột Ngày gửi / Ngày trả lời / Ngày cập nhật của bảng Tư vấn nhanh.

---

## QLKCHTV_31 — Cảnh báo trước khi ghi đè nội dung cán bộ đang soạn *(BA-11)*

**(1) Phần mềm đúng `.md` chưa?** ĐÚNG theo câu chữ: `.md:572` và `:201` chỉ mô tả bấm [Chọn] thì chép câu trả lời vào ô soạn, không nhắc cảnh báo. Đo thực tế: ghi đè ngay, mất sạch phần cán bộ tự gõ, không hộp thoại, không thông báo.

**(1b) Bản `.docx` có nói khác không?** CÓ, đúng từng chữ kỳ vọng của phiếu. Mục **4.13.2.3.3** mục 2 "Chọn câu trả lời từ kho": *"NSD có thể bấm «Chọn» trên kết quả khác để thay thế nội dung vừa điền; hệ thống cảnh báo «Bạn đang thay thế nội dung trả lời đã soạn. Tiếp tục?» nếu ô trả lời đã có nội dung tùy chỉnh."*

**(2) Đối tác yêu cầu khác gì?** Không đòi gì ngoài tài liệu.

**(3) Có bắt buộc không?** CÓ. Đây là mất dữ liệu người dùng vừa tạo, không khôi phục được, không có bản nháp để lấy lại (xem BA-13). Quy ước chung UI-08 (`srs-v3.5.md:577`) đặt nguyên tắc không để người dùng mất nội dung chưa lưu; tình huống này cùng loại hại tuy không cùng phạm vi câu chữ.

**Phân định hướng:** Không tầng nào của cây trọng tài đòi giữ hành vi ghi đè im lặng; nguyên tắc UI-08 và rủi ro đo được đều đẩy về phía có cảnh báo. → **Hướng B**.

**→ Kết luận: Loại 4B — chốt: khi ô "Nội dung trả lời" đã có nội dung do cán bộ tự soạn mà cán bộ bấm [Chọn] ở một kết quả tra cứu khác, hệ thống hỏi xác nhận "Bạn đang thay thế nội dung trả lời đã soạn. Tiếp tục?" trước khi ghi đè. Nếu ô trống hoặc nội dung nguyên vẹn từ kho thì chép thẳng, không hỏi. Dev action: Có (Medium). Doc action: BA bổ sung. Sheet: Giữ xử lý (row 15).** **✅ BA duyệt 2026-07-30.**

**Phương án xử lý (cập nhật SRS):** `srs-fr-13-tv-nhanh.md:572` (hành vi nút [Chọn]) và `:201` (Processing bước 6) — bổ sung điều kiện hỏi xác nhận trước khi ghi đè, kèm câu chữ chuẩn.

---

## QLKCHTV_32 — Bấm mã Q&A trong kết quả tra cứu có mở cửa sổ chi tiết không *(BA-12)*

**(1) Phần mềm đúng `.md` chưa?** ĐÚNG theo câu chữ: `.md:572` liệt kê thành phần của mỗi kết quả tra cứu và hành vi duy nhất được mô tả là nút [Chọn]. Đo thực tế: mã hiển thị dạng chữ phụ màu xám, không gắn hàm xử lý bấm — chưa từng được dựng chứ không phải hỏng.

**(1b) Bản `.docx` có nói khác không?** CÓ. Mục **4.13.2.3.3** mục 3 "Xem chi tiết câu trả lời": *"NSD bấm vào mã câu trả lời trong kết quả tra cứu, hệ thống mở cửa sổ chi tiết hiển thị đầy đủ câu hỏi, câu trả lời, lĩnh vực pháp lý, từ khóa và nguồn… Cửa sổ chi tiết có nút «Đóng»"*.

**(2) Đối tác yêu cầu khác gì?** Không đòi gì ngoài tài liệu.

**(3) Có bắt buộc không?** CÓ ở mức vừa. Thẻ kết quả chỉ hiển thị **câu trả lời rút gọn** (`.md:572` ghi rõ "Cau tra loi rut gon"). Cán bộ phải đọc hết câu trả lời mới quyết định được có chọn hay không; hiện chỉ có cách bấm [Chọn] để chép vào ô soạn rồi đọc — tức phải ghi đè nội dung đang có mới xem được, chồng thêm đúng rủi ro của BA-11.

**Phân định hướng:** Lập luận trên là **tầng 3** (thành phần màn hình mâu thuẫn với bước xử lý: bắt cán bộ chọn Q&A phù hợp nhưng không cho đọc đủ để chọn). → **Hướng B**.

**→ Kết luận: Loại 4B — chốt: bấm vào mã câu hỏi trong thẻ kết quả tra cứu mở cửa sổ chi tiết chỉ-đọc gồm câu hỏi, câu trả lời đầy đủ, lĩnh vực, từ khóa, nguồn, kèm nút Đóng; không làm thay đổi nội dung đang soạn. Dev action: Có (Minor). Doc action: BA bổ sung. Sheet: Giữ xử lý (row 16).** **✅ BA duyệt 2026-07-30.**

**Phương án xử lý (cập nhật SRS):** `srs-fr-13-tv-nhanh.md:572` — bổ sung hành vi bấm mã Q&A trong khu vực tra cứu và thành phần cửa sổ chi tiết chỉ-đọc.

---

## QLKCHTV_36 — Màn trả lời Tư vấn nhanh có cần [Lưu nháp] không *(BA-13 — tách 2 ý)*

Phiếu gộp hai thứ khác nhau. Phải tách vì hai ý đi hai hướng ngược nhau.

### Ý 1 — Cảnh báo khi rời màn còn nội dung chưa gửi

**(1) Phần mềm đúng `.md` chưa?** SAI. Quy ước chung **UI-08** (`srs-v3.5.md:577`) bắt buộc: *"Hỏi xác nhận (hộp thoại «Ở lại / Rời đi») khi người dùng rời hoặc hủy một form đang nhập dở còn dữ liệu chưa lưu. **Áp cho mọi form nhập liệu toàn hệ thống**"*. Màn trả lời phiên là form nhập liệu. Hiện cán bộ soạn dở rồi rời màn là mất toàn bộ, không có cảnh báo nào.

**(1b) `.docx` có nói khác không?** Cùng phía. Mục **4.13.2.3.3** mục 7 "Quay lại" mô tả đúng cơ chế này.

**(2)(3)** Đối tác không nêu riêng ý này; đây là điểm bắt buộc theo quy ước chung, có mất dữ liệu thật.

**→ Kết luận ý 1: Loại 1 — Lỗi phần mềm, Dev sửa theo SRS: bổ sung hỏi xác nhận khi rời màn trả lời mà ô "Nội dung trả lời" còn nội dung chưa gửi, theo quy ước UI-08. KHÔNG sửa SRS. Dev action: Có (Minor).** **✅ BA duyệt 2026-07-30.**

### Ý 2 — Nút [Lưu nháp]

**(1) Phần mềm đúng `.md` chưa?** ĐÚNG, và `.md` **nói ngược lại** kỳ vọng chứ không chỉ im lặng: `:572` khai đúng hai thao tác ([Gửi trả lời] và nút phụ "Đẩy sang Nhóm II"); FR-X.2-02 (`:164`–`:238`) không có bước xử lý, đầu ra, trạng thái hay mã lỗi nào cho bản nháp; Điều kiện chấp nhận `:235` ghi *"chỉ lưu `noi_dung_tra_loi` cuối cùng"*. QA đo thêm ở tầng máy chủ: 10 đường dẫn của nhóm tư vấn nhanh, không đường nào cho bản nháp.

**(1b) Bản `.docx` có nói khác không?** CÓ. Mục **4.13.2.3.3** mục 6 "Lưu nháp".

**(2) Đối tác yêu cầu khác gì?** Đòi nút [Lưu nháp] — đúng `.docx`.

**(3) Có bắt buộc không?** KHÔNG, một khi ý 1 đã được sửa. Rủi ro mà QA lo (mất công soạn) do hai lỗ hổng cộng lại: không cảnh báo ghi đè (BA-11) và không cảnh báo rời màn (ý 1). Cả hai đều đã chốt sửa. Bản thân việc lưu nháp không phải điều kiện để hoàn thành phiên tư vấn.

**Phân định hướng — đây là chỗ `.md` bỏ có chủ đích, có đối chứng:**
1. **Tầng 1:** nhóm Hỏi đáp của chính `.md` đặc tả lưu nháp **rất kỹ** — `srs-fr-02-hoi-dap.md:1127` có cả tự lưu mỗi 60 giây, chỉ báo "Đã lưu lúc {giờ}", xử lý tranh chấp khi hai cán bộ cùng sửa. Viết chi tiết đến mức đó cho Hỏi đáp mà không viết một chữ cho Tư vấn nhanh là **lựa chọn thiết kế**, không phải sót.
2. **Tầng 2:** `.md` ghi thẳng chủ trương "chỉ lưu nội dung cuối cùng" (`:235`).
3. **Tính chất luồng:** tư vấn nhanh là trả lời ngắn dựa trên kho câu hỏi có sẵn, khác hẳn hỏi đáp chính thức phải trích dẫn văn bản và qua phê duyệt.

→ **Hướng A**.

| Trường | Nội dung |
|---|---|
| Bản `.docx` đối chiếu | `HTPLDN-PTYC-CT-v2.0.docx` · 10/07/2026 · nhóm Zalo |
| Trích `.docx` | Mục 4.13.2.3.3, mục 6 "Lưu nháp" — lưu nội dung đang soạn, trạng thái phiên không đổi |
| Trích `.md` | `srs-fr-13-tv-nhanh.md:572` (chỉ 2 thao tác) · `:235` ("chỉ lưu nội dung cuối cùng") · `srs-fr-02-hoi-dap.md:1127` (đối chứng: nhóm Hỏi đáp có, viết rất kỹ) |
| Hướng | **A** — `.docx` mô tả thừa so với bản gốc |
| Dev action | Không |
| Doc action | Bên soạn tài liệu bàn giao gỡ mục 6 "Lưu nháp" khỏi 4.13.2.3.3 ở bản kế tiếp; giữ mục 7 "Quay lại" |
| Sheet | (theo dòng — xem kết luận chung) |

**→ Kết luận ý 2: Loại 4A — phần mềm đúng bản gốc, tài liệu bàn giao mô tả thừa. Không bổ sung [Lưu nháp] cho màn trả lời Tư vấn nhanh. Dev action: Không. Doc action: cập nhật `.docx`.** **✅ BA duyệt 2026-07-30.**

**→ Kết luận chung `QLKCHTV_36`: ca lai — ý 1 Dev phải sửa, ý 2 không. Sheet: Giữ xử lý (row 18), không đặt Resolve.** **✅ BA duyệt 2026-07-30.**

**Phản hồi gửi đối tác — riêng ý 2:** *"Về nút Lưu nháp trên màn trả lời tư vấn nhanh: xác nhận bản đặc tả bàn giao đang chưa cập nhật ở điểm này. Luồng tư vấn nhanh được thiết kế là trả lời ngắn dựa trên kho câu hỏi sẵn có, chỉ lưu nội dung cuối cùng khi gửi; chức năng lưu nháp thuộc nhóm Hỏi đáp pháp luật. Bản đặc tả cập nhật sẽ được gửi lại khi bàn giao đợt sửa lỗi. Đổi lại, phần mềm sẽ bổ sung cảnh báo khi Quý đơn vị rời màn hình mà nội dung soạn dở chưa được gửi, để không mất nội dung đang nhập."*

---

## QLKCHTV_26 — Khối "Thông tin doanh nghiệp" gồm những trường nào *(BA-14)*

**(1) Phần mềm đúng `.md` chưa?** `.md:571` chỉ ghi chung một cụm "Thong tin DN", không liệt kê trường ⇒ không chấm được phần trường nào phải có. Đo thực tế: khối chỉ có 2 dòng — Tên DN (có giá trị) và MST (bỏ trống).

**(1b) Bản `.docx` có nói khác không?** CÓ, liệt kê đủ bốn trường. Mục **4.13.2.3.2**, bảng "Cột trái — Thông tin phiên tư vấn", dòng 2: *"Thông tin doanh nghiệp | Nhóm thông tin | … | **Tên doanh nghiệp, mã số thuế, thư điện tử liên hệ, người gửi câu hỏi** — lấy từ tài khoản doanh nghiệp trên Cổng Pháp luật quốc gia"* — trùng đúng kỳ vọng của phiếu.

**(2) Đối tác yêu cầu khác gì?** Không đòi gì ngoài tài liệu.

**(3) Có bắt buộc không?** CÓ. Cán bộ cần thư điện tử liên hệ và người gửi để liên hệ lại khi câu hỏi chưa rõ; đây là thông tin tối thiểu của một phiên tư vấn.

**Phân định hướng:** `.md` mô tả gộp một cụm, `.docx` liệt kê chi tiết — dạng bị sót ở mức liệt kê, không phải trái nhau. QA đo được dữ liệu thư điện tử đã có sẵn ở dịch vụ dữ liệu doanh nghiệp, chỉ chưa trả về trong khối doanh nghiệp của phiên. → **Hướng B**.

**→ Kết luận: Loại 4B — chốt khối "Thông tin doanh nghiệp" ở cột trái màn trả lời gồm 4 trường: tên doanh nghiệp, mã số thuế, thư điện tử liên hệ, người gửi câu hỏi. Dev action: Có (sửa một lần cùng `BUG-QLKCHTV_26B` — bổ sung mã số thuế, thư điện tử và người gửi vào dữ liệu trả về của phiên). Doc action: BA bổ sung. Sheet: Giữ xử lý (row 14).** **✅ BA duyệt 2026-07-30.**

**Phương án xử lý (cập nhật SRS):** `srs-fr-13-tv-nhanh.md:571` — thay cụm "Thong tin DN" bằng danh sách 4 trường nêu trên, ghi rõ nguồn dữ liệu là hồ sơ doanh nghiệp gắn với phiên.

---

## PDNDCHTV_07 — Duyệt hàng loạt có gửi thông báo cho từng cán bộ tạo không *(BA-15)*

**(1) Phần mềm đúng `.md` chưa?** SAI. `.md:536` định nghĩa hành động Duyệt gồm ba vế: đặt trạng thái `DA_DUYET`, bật hiệu lực, **và thông báo cho cán bộ nghiệp vụ**. `:537` mô tả nút Duyệt hàng loạt chỉ nói về hành vi của nút, **không định nghĩa lại** hành động Duyệt và không miễn trừ nghĩa vụ thông báo. Đo thực tế: duyệt hàng loạt 2 câu hỏi, hộp thông báo bên nhận đếm trước/sau đều 253 — chênh lệch bằng 0.

**(1b) Bản `.docx` có nói khác không?** KHÔNG — `.docx` **nói mạnh hơn cả `.md`**, đóng luôn tranh cãi. Mục **4.13.1.2.3** mục 13 "Duyệt hàng loạt", Trường hợp 1: *"…hệ thống chuyển trạng thái tất cả câu hỏi được chọn: «Chờ duyệt» → «Đã duyệt», **gửi thông báo cho từng cán bộ tạo câu hỏi tương ứng**"*.

**(2) Đối tác yêu cầu khác gì?** Không. Yêu cầu của họ khớp cả hai tài liệu.

**(3) Có bắt buộc không?** CÓ. Cán bộ tạo câu hỏi phải biết kết quả thẩm định; thiếu thông báo thì họ không biết câu hỏi đã được duyệt hay còn chờ.

**→ Kết luận: Loại 1 — Lỗi phần mềm, Dev sửa theo SRS: duyệt hàng loạt phải gửi thông báo cho từng cán bộ đã tạo câu hỏi trong lô, giống hệt duyệt đơn lẻ. Nên sửa ở tầng dùng chung để duyệt đơn lẻ, từ chối và duyệt hàng loạt cùng đi qua một chỗ. Cách hiểu của QA là đúng, `BUG-PD-THONG-BAO` giữ nguyên. Dev action: Có. Doc action: BA bổ sung một câu vào `:537` cho khỏi hỏi lại. Sheet: Giữ xử lý (row 22).** **✅ BA duyệt 2026-07-30.**

**Phương án xử lý (cập nhật SRS):** `srs-fr-13-tv-nhanh.md:537` — thêm vào mô tả nút Duyệt hàng loạt: mỗi câu hỏi trong lô áp dụng đầy đủ hành động Duyệt ở `:536`, gồm cả việc gửi thông báo cho cán bộ tạo tương ứng.

---

## QLCKCHTV_02 — "Mô tả công khai" để trống thì có tự điền bằng nội dung câu hỏi không *(BA-16)*

**(1) Phần mềm đúng `.md` chưa?** SAI về tinh thần đặc tả. `.md:106` định nghĩa `mo_ta_cong_khai` là *"mô tả hiển thị trên Cổng PLQG, **khác `cau_hoi`/`cau_tra_loi` nội bộ**"* — tức trường riêng, có mục đích riêng. Đo thực tế: bỏ trống thì hệ thống tự điền **nguyên văn nội dung câu hỏi** và lưu lại, làm trường này thành bản sao đúng thứ mà đặc tả nói phải khác.

**(1b) Bản `.docx` có nói khác không?** KHÔNG, cùng phía `.md`. Mục **4.13.6.2.2** mục 1 "Công khai": hộp thoại *"cho phép NSD bổ sung mô tả hiển thị trên chuyên trang… **nếu cần**"* — trường tùy chọn do cán bộ chủ động nhập, không có quy tắc tự điền nào.

**(2) Đối tác yêu cầu khác gì?** Không đòi thêm; họ ghi nhận nội dung công khai ra không như mong đợi.

**(3) Có bắt buộc không?** CÓ. Đây là **nội dung hiển thị ra ngoài hệ thống**, cho cộng đồng doanh nghiệp đọc trên Cổng Pháp luật quốc gia. Câu hỏi nội bộ thường viết theo văn phong hồ sơ, không phải văn phong công bố. Tự điền âm thầm khiến cán bộ tưởng đã để trống mà thực ra đã đăng nguyên văn câu hỏi nội bộ lên Cổng.

**→ Kết luận: Loại 1 — Lỗi phần mềm, Dev sửa theo SRS: bỏ quy tắc tự điền "Mô tả công khai" bằng nội dung câu hỏi. Cán bộ để trống thì lưu trống; trường vẫn là tùy chọn, không bắt buộc nhập. Hộp thoại vẫn hiển thị đúng giá trị đang lưu nếu bản ghi đã có mô tả (phần này phần mềm đang làm đúng, giữ nguyên). Dev action: Có. Doc action: BA bổ sung một câu vào `:106`. Sheet: Giữ xử lý (row 23).** **✅ BA duyệt 2026-07-30.**

**Phương án xử lý (cập nhật SRS):** `srs-fr-13-tv-nhanh.md:106` — thêm: hệ thống không tự điền giá trị mặc định cho trường này; để trống thì lưu trống.

> **[CHỜ CĐT]** Cần xác nhận với bên vận hành Cổng Pháp luật quốc gia: khi mô tả công khai trống thì Cổng hiển thị theo quy tắc nào của Cổng. Không chặn việc Dev gỡ phần tự điền, nhưng nên xác nhận trước khi công khai lô lớn.

---

## TKCHTV_02 — Câu thông báo khi tìm kiếm / lọc không khớp *(BA-17)*

**(1) Phần mềm đúng `.md` chưa?** Không chấm được từ nhóm X.2: mã `INF-TVN-TK-01` (*"Không tìm thấy câu hỏi phù hợp"*) có tồn tại nhưng cả hai chỗ khai đều thuộc FR-X.2-02 (`:225`) và FR-X.2-04 (`:349`) — khu vực tra cứu kho trong màn trả lời và chuyên trang doanh nghiệp, không phải màn danh sách quản trị. Phần mô tả màn danh sách (`:530`, `:568`) không quy định câu rỗng. Đo thực tế: cả hai màn đều dùng câu dành cho "chưa có dữ liệu" kể cả khi kho đang có dữ liệu.

**(1b) Bản `.docx` có nói khác không?** CÓ, cho **cả hai màn**, đúng từng chữ kỳ vọng của phiếu:
- Mục **4.13.1.2.3** mục 2 "Tìm kiếm", Trường hợp 1: *"bảng dữ liệu để trống và hiển thị thông báo «Không tìm thấy câu hỏi phù hợp»"*.
- Mục **4.13.2.2.3** mục 2 "Tìm kiếm", Trường hợp 1: *"…«Không tìm thấy phiên tư vấn phù hợp»"*.

**(2) Đối tác yêu cầu khác gì?** Không đòi gì ngoài tài liệu.

**(3) Có bắt buộc không?** CÓ ở mức vừa. Nói "Chưa có câu hỏi nào" trong khi kho có 14 câu hỏi là **thông tin sai** với người dùng, dễ khiến cán bộ tưởng mất dữ liệu.

**Phân định hướng:** **Tầng 1** — nhóm Hỏi đáp của chính `.md` đã có quy ước dùng chung cho đúng tình huống này, tách 5 biến thể (`srs-fr-02-hoi-dap.md:1047`), trong đó biến thể 1 dành cho "chưa có dữ liệu" và biến thể 4 cho "lọc không khớp" kèm nút [Xóa bộ lọc]. Nhóm X.2 thiếu ⇒ bị sót. → **Hướng B**, và áp theo quy ước 5 biến thể để nhất quán toàn hệ thống — quy ước này **bao trùm** câu chữ của `.docx` chứ không mâu thuẫn.

**→ Kết luận: Loại 4B — chốt: hai màn danh sách nhóm X.2 áp quy ước trạng thái rỗng của nhóm Hỏi đáp, phân biệt rõ hai tình huống. Chưa có dữ liệu → "Chưa có câu hỏi nào." / "Chưa có phiên tư vấn nào." Tìm kiếm hoặc lọc không khớp → "Không tìm thấy câu hỏi phù hợp." / "Không tìm thấy phiên tư vấn phù hợp." kèm nút [Xóa bộ lọc] (nối với BA-18). Dev action: Có (Minor). Doc action: BA bổ sung. Sheet: Giữ xử lý (row 25).** **✅ BA duyệt 2026-07-30.**

**Phương án xử lý (cập nhật SRS):** `srs-fr-13-tv-nhanh.md:530` và `:568` — bổ sung mô tả trạng thái rỗng theo quy ước ở `srs-fr-02-hoi-dap.md:1047`, nêu rõ câu chữ cho từng tình huống của từng màn.

---

## TKCHTV_03 — Màn Kho câu hỏi có nút [Xóa bộ lọc] không *(BA-18)*

**(1) Phần mềm đúng `.md` chưa?** `.md` không quy định nút này ở cả hai màn của nhóm X.2 (`:530`, `:568`). Đo thực tế: màn Tư vấn nhanh **có** nút và chạy đúng; màn Kho câu hỏi **không có**, và nút [Làm mới] không đặt lại bộ lọc — tức không có thao tác nào đưa danh sách về mặc định trong một lần bấm.

**(1b) Bản `.docx` có nói khác không?** CÓ, cho **cả hai màn**. Mục **4.13.1.2.3** mục 3 và mục **4.13.2.2.3** mục 3, cùng nội dung: *"↻ Xóa bộ lọc — hệ thống xóa toàn bộ giá trị ở các ô lọc và ô tìm kiếm, tải lại danh sách theo mặc định của thẻ hiện tại"*. `.docx` cũng tách bạch với nút "Làm mới" (giữ nguyên điều kiện lọc).

**(2) Đối tác yêu cầu khác gì?** Không đòi gì ngoài tài liệu.

**(3) Có bắt buộc không?** CÓ ở mức vừa. Màn Kho câu hỏi có tới 6 tiêu chí lọc; không có nút đặt lại thì cán bộ phải xóa tay từng ô.

**Phân định hướng:** **Tầng 1** — nút [Xóa bộ lọc] là quy ước lặp ở **7 nhóm khác** của chính `.md` (`srs-fr-02-hoi-dap.md:1033`, `srs-fr-09-bieu-mau.md:622`, `srs-fr-07-doanh-nghiep.md:434`, `srs-fr-04-chuyen-gia-tvv.md:1439`, `srs-fr-05-vu-viec.md:1646`, `srs-fr-06-chi-tra.md:1050`, `srs-fr-08-danh-gia.md:817`), và chính màn anh em cùng nhóm cũng đã dựng. Không tầng nào chốt ngược. → **Hướng B**.

**→ Kết luận: Loại 4B — chốt: thanh lọc của cả hai màn danh sách nhóm X.2 có nút [Xóa bộ lọc], hành vi đặt lại toàn bộ tiêu chí và ô tìm kiếm về mặc định của thẻ đang chọn; nút [Làm mới] giữ nguyên điều kiện lọc, chỉ tải lại dữ liệu. Dev action: Có (Minor — bổ sung cho màn Kho câu hỏi, thành phần đã có sẵn ở màn Tư vấn nhanh). Doc action: BA bổ sung. Sheet: Giữ xử lý (row 26).** **✅ BA duyệt 2026-07-30.**

**Phương án xử lý (cập nhật SRS):** `srs-fr-13-tv-nhanh.md:528` và `:566` — bổ sung nút [Xóa bộ lọc] vào thanh công cụ hai màn, phân biệt rõ với [Làm mới].

---

## KHTHCTHTPLDN_07 — Tên tệp Excel xuất từ màn Chương trình HTPLDN *(BA-19)*

**(1) Phần mềm đúng `.md` chưa?** `.md` mô tả đủ quy trình xuất Excel của nhóm XI (`srs-fr-15-ct-htpldn.md:387`–`:410`) nhưng **không quy định tên tệp**. Đo thực tế: tệp tải về là `ct-htpldn-2026-07-27.xlsx` — thiếu giờ phút.

**(1b) Bản `.docx` có nói khác không?** CÓ, đúng từng chữ kỳ vọng của phiếu. Mục **4.15.1.2.3** mục 2 "Xuất tệp danh sách": *"Đặt tên tệp **DanhSachChuongTrinh_{YYYYMMDD_HHmm}.xlsx**"*.

**(2) Đối tác yêu cầu khác gì?** Không đòi gì ngoài tài liệu.

**(3) Có bắt buộc không?** CÓ ở mức vừa, cùng lý do BA-03: xuất hai lần trong ngày thì tệp thứ hai bị trình duyệt thêm hậu tố, dễ nhầm tệp khi đối soát.

**Phân định hướng:** **Tầng 1** — `srs-fr-02-hoi-dap.md:151` đã đặt mẫu tên tệp có giờ phút cho nhóm Hỏi đáp; `srs-fr-12-tv-chuyen-sau.md:162` cũng vậy. `.docx` dùng đúng khuôn đó. → **Hướng B**.

**→ Kết luận: Loại 4B — chốt tên tệp `DanhSachChuongTrinh_{YYYYMMDD_HHmm}.xlsx`. Dev action: Có (Minor). Doc action: BA bổ sung. Sheet: Giữ xử lý (row 29).** **✅ BA duyệt 2026-07-30.**

**Phương án xử lý (cập nhật SRS):**
- `srs-fr-15-ct-htpldn.md:397` (bước 5 của Processing Xuất Excel) — bổ sung mẫu tên tệp.
- **Đồng thời cập nhật `.docx`:** mục 4.15.1.2.3 mục 2 liệt kê **9 cột**, thiếu "Lĩnh vực pháp lý" so với 10 cột mà `.md:396` quy định (phần mềm đang xuất đúng 10 cột). Đây là chỗ `.docx` thiếu so với bản gốc — bên soạn tài liệu bàn giao bổ sung ở bản kế tiếp.

> **Ưu tiên cao hơn tên tệp:** lỗi hai cột thời gian trong tệp lệch 1 ngày so với màn hình (chương trình bắt đầu 01/01/2026 vào tệp thành 31/12/2025) đã tách thành `BUG-CT-XUAT-EXCEL-SAI-NGAY` (dòng `KHTHCTHTPLDN_OOS_06`). Đây là sai dữ liệu, đề nghị Dev xử lý trước.

---

## KHTHCTHTPLDN_12 — Bố cục đầu trang Chi tiết chương trình và nhãn `CHO_PHE_DUYET` *(BA-20 — 4 điểm)*

Phiếu nêu 4 điểm; QA đã re-verify và xác nhận **cả 4 đều quan sát đúng hiện trạng**. Bản `.docx` trả lời được **cả 4**, nên không còn phải chờ tài liệu đặc tả màn hình MH-15.1 mà QA không có.

**(1) Phần mềm đúng `.md` chưa?** `.md` không mô tả đầu trang của trang chi tiết: `:1107` chỉ quy định thanh điều hướng cho **trang danh sách**; không có dòng nào về định dạng tiêu đề hay khối tóm tắt đầu trang.

**(1b) Bản `.docx` có nói khác không?** CÓ, mục **4.15.1.3.2**, bảng "Đầu trang" — bốn dòng đầu ứng đúng bốn điểm của phiếu:

| Điểm phiếu nêu | Trích `.docx` mục 4.15.1.3.2 | Hướng |
|---|---|:-:|
| 1. Thanh điều hướng kèm mã CT | Dòng 1: *"Trang chủ › Chương trình hỗ trợ pháp lý doanh nghiệp › Chi tiết **{Mã chương trình}**"* | B |
| 2. Tiêu đề dạng `{Mã}: {Tên}` | Dòng 2: *"Hiển thị dạng «{Mã chương trình}: {Tên chương trình}» kèm nhãn trạng thái hiện tại bên phải tiêu đề"* | B |
| 3. Nhãn bước "Chờ PD" | Dòng 3: thanh tiến trình 6 bước ghi đầy đủ *"Dự thảo → **Chờ phê duyệt** → Đã duyệt → Đã công bố → Đang thực hiện → Hoàn thành"* | B |
| 4. Khối thông tin nhanh | Dòng 4–7: bốn mục Ngân sách / Thời gian / Đơn vị thực hiện / Đối tượng | **A** |

**(2) Đối tác yêu cầu khác gì?** Không đòi gì ngoài tài liệu ở cả 4 điểm.

**(3) Có bắt buộc không?** Điểm 1–2: mức vừa — tiêu đề chỉ có mã chương trình khiến cán bộ phải cuộn xuống mới biết đang mở chương trình nào. Điểm 3: có — nhãn phải thống nhất, hiện chính phần mềm cũng lệch giữa hai nơi (thẻ lọc màn danh sách ghi "Chờ phê duyệt", bước 2 thanh tiến trình ghi "Chờ PD"). Điểm 4: không — cả bốn thông tin **đều đang hiển thị đầy đủ** trong phần Thông tin ngay bên dưới, chỉ khác cách bày.

**Phân định hướng từng điểm:**

- **Điểm 3 — chốt được ngay từ `.md`, không cần `.docx`.** `.md` tự mâu thuẫn: `:1120` viết tắt `[Cho PD]` trong thanh tiến trình, nhưng `:1174` — **bảng nhãn trạng thái SM-KH-CTHTPL**, tức nơi định nghĩa nhãn chuẩn — ghi `CHO_PHE_DUYET` → *"Cho phe duyet"*. Cây trọng tài **tầng 2** (bảng định nghĩa thắng chỗ viết tắt trong sơ đồ). `.docx` cùng phía. → Chốt **"Chờ phê duyệt"**. **✅ BA duyệt 2026-07-30.**
- **Điểm 1, 2 — hướng B.** `.md` không mô tả đầu trang trang chi tiết; `.docx` có, nội dung hợp lý, chi phí sửa nhỏ. Không tầng nào chốt ngược. **✅ BA duyệt 2026-07-30.**
- **Điểm 4 — hướng A.** Đây là **bố cục thuần**: `.md:1120`–`:1131` liệt kê đúng bốn thông tin này là **các trường của phần Thông tin**, không có thành phần nào tên "khối thông tin nhanh" (tra toàn thư mục `srs-v3.5/` cụm "thông tin nhanh": 0 kết quả). Thông tin không mất, chỉ không có khối tóm tắt riêng. `.md` bày theo dạng danh sách trường là cách bày đã chốt. **✅ BA duyệt 2026-07-30.**

| Trường (cho điểm 4) | Nội dung |
|---|---|
| Bản `.docx` đối chiếu | `HTPLDN-PTYC-CT-v2.0.docx` · 10/07/2026 · nhóm Zalo |
| Trích `.docx` | Mục 4.15.1.3.2, bảng Đầu trang, dòng 4–7 "Khối thông tin nhanh — Ngân sách / Thời gian / Đơn vị thực hiện / Đối tượng" |
| Trích `.md` | `srs-fr-15-ct-htpldn.md:1120`–`:1131` — bốn thông tin này là trường của phần Thông tin; không có thành phần "khối thông tin nhanh" |
| Hướng | **A** — `.docx` mô tả thừa (bố cục, thông tin không mất) |
| Dev action | Không |
| Doc action | Bên soạn tài liệu bàn giao gỡ dòng 4–7 khỏi bảng Đầu trang ở bản kế tiếp |
| Sheet | (theo dòng — xem kết luận chung) |

**→ Kết luận `KHTHCTHTPLDN_12`: ca lai.** **✅ BA duyệt 2026-07-30.**
- **Điểm 3: Loại 2 — SRS tự mâu thuẫn, chốt theo bảng nhãn trạng thái. Nhãn chuẩn của `CHO_PHE_DUYET` là "Chờ phê duyệt", áp cho cả thanh tiến trình lẫn thẻ lọc. Dev action: Có (Minor, Dev FE). Doc action: BA sửa `:1120` cho khớp `:1174`.** **✅ BA duyệt 2026-07-30.**
- **Điểm 1, 2: Loại 4B — bổ sung mô tả đầu trang vào `.md` rồi Dev chỉnh. Dev action: Có (Minor).** **✅ BA duyệt 2026-07-30.**
- **Điểm 4: Loại 4A — Dev action: Không; cập nhật `.docx`.** **✅ BA duyệt 2026-07-30.**
- **Sheet: Giữ xử lý (row 31)** — ưu tiên phần Dev.

**Phương án xử lý (cập nhật SRS):**
- `srs-fr-15-ct-htpldn.md:1120` — sửa thanh tiến trình viết đủ nhãn theo bảng `:1174`: Dự thảo → Chờ phê duyệt → Đã duyệt → Đã công bố → Đang thực hiện → Hoàn thành.
- Bổ sung vào bảng thành phần trang Chi tiết CT (trước `:1120`) hai dòng mô tả đầu trang: thanh điều hướng kết thúc bằng "Chi tiết {Mã chương trình}"; tiêu đề trang dạng "{Mã chương trình}: {Tên chương trình}" kèm nhãn trạng thái bên phải.

**Phản hồi gửi đối tác — riêng điểm 4:** *"Về khối thông tin nhanh ở đầu trang chi tiết chương trình: xác nhận bản đặc tả bàn giao đang chưa cập nhật ở điểm này. Bốn thông tin Ngân sách, Thời gian, Đơn vị thực hiện và Đối tượng đều đang hiển thị đầy đủ trong phần Thông tin của trang, chỉ không gom thành khối tóm tắt riêng ở đầu trang. Bản đặc tả cập nhật sẽ được gửi lại khi bàn giao đợt sửa lỗi. Ba điểm còn lại của phiếu (thanh điều hướng, tiêu đề trang, nhãn trạng thái) đã được chấp thuận và sẽ chỉnh sửa."*

---

## TKKHCTHTPL_01 — Thanh lọc màn Chương trình có bổ sung "Lĩnh vực pháp lý" không *(BA-21)*

Đây là **mục duy nhất của đợt này đối tác đòi thêm ngoài cả hai tài liệu**.

**(1) Phần mềm đúng `.md` chưa?** Về vế Lĩnh vực: ĐÚNG. `.md` liệt kê **tường minh** 5 dữ liệu đầu vào của chức năng tìm kiếm (`srs-fr-15-ct-htpldn.md:352`–`:356`: `keyword`, `don_vi_id`, `trang_thai`, `tu_ngay`, `den_ngay`) và 4 ô trên thanh lọc (`:1109`–`:1112`). Không mục nào là lĩnh vực.

**(1b) Bản `.docx` có nói khác không?** KHÔNG. Mục **4.15.1.2.2**, bảng bộ lọc, liệt kê đúng 5 ô: Tìm kiếm theo từ khóa, Đơn vị, Trạng thái, Từ ngày, Đến ngày. **Không có Lĩnh vực pháp lý.** Đây là điểm phân biệt: các mục khác của đợt này đối tác chấm theo `.docx`, riêng mục này họ đòi thêm ngoài cả `.docx`.

**(2) Đối tác yêu cầu khác gì?** Đòi thêm một tiêu chí lọc không có ở bất kỳ tài liệu nào.

**(3) Có bắt buộc cho luồng nghiệp vụ không?** KHÔNG. Cán bộ vẫn tìm được chương trình theo từ khóa, đơn vị, trạng thái và khoảng ngày. Đề xuất hợp lý về nghiệp vụ (lĩnh vực pháp lý là trường bắt buộc khi tạo chương trình và là chiều gom số liệu báo cáo — `:1128`; phần xử lý phía sau đã hỗ trợ sẵn tham số này, QA đo được kết quả thu hẹp từ 8 xuống 1) nhưng đó là **cải tiến**, không phải lỗi.

**→ Kết luận vế Lĩnh vực: Loại 3 — Phần mềm đúng đặc tả; phần đối tác đòi không bắt buộc. Không bổ sung ô lọc Lĩnh vực ở đợt này, đề nghị đưa vào danh sách yêu cầu cải tiến. Dev action cho riêng ý này: Không.** **✅ BA duyệt 2026-07-30.**

**→ Kết luận dòng `TKKHCTHTPL_01`: ca lai — vế "Đơn vị" của cùng phiếu là lỗi thật (`:353` liệt kê `don_vi_id` là dữ liệu đầu vào, `:1110` quy định ô chọn Đơn vị với điều kiện hiển thị "luôn hiển thị"; web thiếu), đã chấm Open và gộp `BUG-CT-LOC-THIEU-DONVI-TRANGTHAI`. Dev action: Có (cho vế Đơn vị). Sheet: Giữ xử lý (row 32).** **✅ BA duyệt 2026-07-30.**

> **Độc lập với quyết định trên:** bảng danh sách đang thiếu cột "Lĩnh vực pháp lý" mà `:1113` đã quy định (web 9/10 cột) — `BUG-CT-BANG-THIEU-COT-LINHVUC`, dòng `KHTHCTHTPLDN_OOS_05`, đang Open. Bổ sung cột này giải quyết phần lớn nhu cầu thực tế của đối tác mà không cần thêm bộ lọc, nên đề nghị Dev ưu tiên.

**Phản hồi gửi đối tác — riêng vế Lĩnh vực:** *"[Lý do] Bộ tiêu chí tìm kiếm của màn Chương trình hỗ trợ pháp lý doanh nghiệp được chốt gồm từ khóa, đơn vị chủ trì, trạng thái và khoảng thời gian; lĩnh vực pháp lý không nằm trong bộ tiêu chí này. [Nhận định] Kính đề nghị Quý đơn vị đưa nội dung này vào danh sách yêu cầu cải tiến. Phần thiếu ô lọc theo đơn vị chủ trì mà Quý đơn vị nêu cùng phiếu đã được ghi nhận là lỗi và sẽ được chỉnh sửa; cột Lĩnh vực pháp lý trên bảng danh sách cũng sẽ được bổ sung."*

---

## TKVVHTPLDN_01 — Hợp đồng đường dẫn của nhóm API tích hợp *(BA-22)*

**(1) Phần mềm đúng `.md` chưa?** LỆCH — hai bên khai hai dạng đường dẫn khác nhau; bên nào phải theo bên nào thì xử ở phần Phân định. `.md` công bố `GET /api/v1/vu-viec/search` (`srs-fr-16-api.md:665` FR-XII-08, đường dẫn ở `:671`). Bản mô tả API đã triển khai công bố `GET /api/v1/public/vu-viecs/search` — khác cả ở tiền tố `public` lẫn ở dạng số nhiều. Kiểm toàn file `srs-fr-16-api.md`: **không có lần nào** xuất hiện tiền tố `/api/v1/public`; toàn bộ 19 giao diện đều dùng dạng số ít không tiền tố.

**(1b) Bản `.docx` có nói khác không?** KHÔNG — và đây là điểm quyết định. Mục **4.16.8** (Tìm kiếm vụ việc hỗ trợ pháp lý), phần Tham chiếu, ghi đúng đường dẫn của `.md`: *"đường dẫn GET /api/v1/vu-viec/search"*. Mục **4.16.7** cũng vậy với `/api/v1/vu-viec`. ⇒ **Hai tài liệu thống nhất với nhau; chỉ phần mềm lệch.** Đây **không** phải ca lệch tài liệu bàn giao.

**(2) Đối tác yêu cầu khác gì?** Không. Họ gọi theo đường dẫn được công bố và nhận lỗi.

**(3) Có bắt buộc không?** CÓ — bắt buộc phải **thống nhất về một dạng duy nhất**, không bắt buộc phải là dạng nào. Đường dẫn là hợp đồng để bên tiêu thụ (Cổng Pháp luật quốc gia) tích hợp; để hai dạng song song thì bên tiêu thụ đọc tài liệu được giao mà gọi không tới, việc liên thông không thực hiện được.

**Phân định:** Đường dẫn chính thức của nhóm FR-XII là dạng đang chạy trên hệ thống: `/api/v1/public/{nhóm-nội-dung}s` và `/api/v1/public/{nhóm-nội-dung}s/search` (có tiền tố `public`, entity số nhiều). Phần mềm **không** phải đổi đường dẫn; hai tài liệu sửa theo. Đây là ngoại lệ có chủ đích so với nguyên tắc đã dùng ở `FR-VIII-22` (mã lỗi `ERR-REG-`, chốt 2026-05-10 — code lệch đặc tả ở định danh đã văn bản hoá thì sửa code): ở đây bên tiêu thụ chưa tích hợp nên chưa ai phụ thuộc dạng cũ, sửa tài liệu rẻ hơn đổi 19 đường dẫn đã triển khai.

**→ Kết luận: Loại 2 — dạng ĐỔI BASELINE, không phải Loại 2 thường.** Cần nói rõ vì bốn nhãn của quy trình không có ô nào khớp hẳn: đặc tả **không** tự mâu thuẫn (Loại 2 thường), `.docx` **không** lệch `.md` (Loại 4), và tuy phần mềm lệch đặc tả nhưng BA **không** bắt Dev sửa (Loại 1). Ở đây BA chọn lấy bản đã triển khai làm chuẩn hợp đồng, tức **đổi baseline** — đặc tả cập nhật theo, Dev giữ nguyên đường dẫn. Dev action: Có — nhưng cho lỗi 400 nêu dưới, KHÔNG phải cho việc đổi đường dẫn. Doc action: sửa `srs-fr-16-api.md` (19 giao diện) + `.docx` mục 4.16.x + thông báo dạng đường dẫn đúng cho đối tác. Sheet: Giữ xử lý (row 35).** **✅ BA duyệt 2026-07-30.**

**Phương án xử lý (cập nhật SRS) — đợt sửa riêng:**
- `srs-fr-16-api.md` — rà **toàn bộ 19 giao diện**, đổi đường dẫn sang dạng đã triển khai. Không sửa lẻ FR-XII-08; sửa lẻ sẽ để lại 18 giao diện lệch. Đối chiếu nguồn chuẩn là bản mô tả API đang chạy (`GET /api/docs-json`, 530 đường dẫn) chứ không gõ tay theo suy đoán.
- `.docx` mục 4.16.1 đến 4.16.19 — phần Tham chiếu của từng mục đang ghi đường dẫn dạng cũ, sửa đồng loạt cùng lượt.
- Sau khi sửa xong: **thông báo cho đối tác dạng đường dẫn chính thức**, vì họ đang cầm tài liệu ghi dạng cũ.

**Lỗi thứ hai trên cùng dòng (độc lập với việc đổi đường dẫn):** lỗi 400 *"Validation failed (uuid is expected)"* khi tìm theo từ khóa là lỗi thật — bản mô tả API đã triển khai xác nhận `/search` chỉ bắt buộc `keyword` (chuỗi, tối thiểu 2 ký tự) và **không có tham số bắt buộc nào kiểu định danh**, trong khi đường dẫn liền kề xem chi tiết thì bắt buộc một tham số kiểu định danh. `BUG-API-TIM-VUVIEC-BAO-LOI-UUID` (Major, P1, Backend) giữ nguyên. Giả thuyết để Dev truy nguyên: lời gọi `/search` bị định tuyến nhầm sang nhánh xem chi tiết theo định danh.

**Hai việc phải xử lý ở phía tài liệu:**
1. **`danh-sach-api.md` — ✅ BA chốt 2026-07-30: bỏ hẳn.** Tệp này đã bị xóa khỏi `_bmad-output/planning-artifacts/srs-v3.5/` (trạng thái đã xóa trong thư mục làm việc) và **không khôi phục**. Từ nay `srs-fr-16-api.md` là nguồn duy nhất của danh mục giao diện tích hợp. Việc phải làm: ghi mục "bỏ `danh-sach-api.md`" vào CHANGELOG; rà và gỡ mọi trích dẫn còn trỏ tới tệp này (trong đó có trích dẫn `danh-sach-api.md:67` ở phiếu QA tuần 4 — trích dẫn đó nay không còn hiệu lực).
2. `.docx` mục 4.16.x đang trỏ *"xem tài liệu kỹ thuật `srs-fr-16-api.md` §2 (kèm gói bàn giao)"* — cần xác nhận tệp này thực sự có trong gói gửi đối tác, nếu không thì bên tiêu thụ không có bản đặc tả chi tiết nào để đối chiếu.

> **[CHỜ CĐT] — chặn kiểm thử, không chặn phiếu này:** toàn bộ bề mặt `/api/v1/public/*` trên môi trường được giao trả 401 với lỗi chứng thư số phía khách; máy chủ không đòi chứng thư ở bước bắt tay nên kể cả được cấp cũng không trình lên được qua đường này. QA đã thử cạn 10 hướng. **Nhóm FR-XII sẽ không kiểm thử được ở mọi vòng UAT tiếp theo** cho tới khi bên vận hành cấp chứng thư số phía khách hoặc mở một lối truy cập dành cho kiểm thử. Đề nghị BA chuyển bên vận hành quyết sớm. Đây là hạn chế môi trường, không phải hạn chế của QA.

---

## KHTHCTHTPLDN_03 — Mô hình màn "Đợt báo cáo" và cột liên kết trên bảng danh sách *(BA-23)*

Hai câu hỏi tách rời, trả lời riêng.

### Câu 1 — Mô hình nào đang hiệu lực

**(1) Phần mềm đúng `.md` chưa?** `.md` giữ song song hai mô hình nên chưa chấm được: `:618` ghi *"tab «Đợt báo cáo» độc lập, không drill-down từ CT"* (sửa theo **STT 52 UAT 2026-05-26**); trong khi `:1101` và trọn bảng `:1143`–`:1166` vẫn mô tả Đợt báo cáo là một thẻ nằm trong trang chi tiết chương trình. Phần mềm làm theo `:618`.

**(1b) Bản `.docx` có nói khác không?** KHÔNG — `.docx` **đứng hẳn về phía `:618`** và nói rõ hơn cả `.md`:
- Mục **4.15.2.2** đặt tên màn là *"Đợt báo cáo định kỳ (danh sách đợt báo cáo toàn quốc)"*.
- Mục **4.15.1.3.2**, bảng "Thẻ nội dung", dòng 9: *"Liên kết «Đợt báo cáo định kỳ» — liên kết điều hướng sang màn hình «Đợt báo cáo định kỳ» **độc lập**…, **không phải** thẻ con thuộc một chương trình"*.
- Dòng 8 xác nhận trang chi tiết chỉ có một thẻ "Thông tin chương trình".

**Phân định:** Cây trọng tài chốt ở **tầng 1** — quyết định STT 52 UAT 2026-05-26 là quyết định mới nhất, chốt sau đè chốt trước; `.docx` và phần mềm đều đã theo. `:1101` và `:1143`–`:1166` là tàn dư của mô hình cũ chưa được gỡ.

**→ Kết luận câu 1: Loại 2 — dọn đặc tả, phần mềm đã đúng. Mô hình hiệu lực là màn "Đợt báo cáo định kỳ" độc lập theo `:618`; trang chi tiết chương trình chỉ có nội dung "Thông tin chương trình". Dev action: Không. Doc action: BA gỡ `:1101` (vế tab "Đợt báo cáo") và trọn bảng `:1143`–`:1166` khỏi SCR-XI-01.** **✅ BA duyệt 2026-07-30.**

### Câu 2 — Bảng danh sách có cột liên kết nhanh sang màn Đợt báo cáo không

**(1)** Phần mềm hiển thị cột "Số đợt BC" — **đúng** `.md:1113`.
**(1b)** `.docx` mục **4.15.1.2.2** dòng 13 mô tả cột **"Đợt báo cáo"** kiểu *Liên kết*: *"Liên kết nhanh mở màn hình «Đợt báo cáo định kỳ» độc lập… Đợt báo cáo định kỳ không gắn riêng từng chương trình."*
**(2)** Đối tác đòi cột liên kết — đúng `.docx`.
**(3)** Không bắt buộc: mục "Đợt báo cáo" đã đứng độc lập ngang hàng ở menu bên trái, cán bộ vào thẳng được.

**Phân định hướng:** **Hướng A**, và chính `.docx` tự tố cáo mình: cột đó là **liên kết nhanh từ dòng của một chương trình sang một màn hình toàn quốc không gắn với chương trình nào** — đúng câu mà `.docx` viết ngay trong ô mô tả. Đây là tàn dư của mô hình drill-down cũ, cùng gốc với `:1101` mà câu 1 vừa chốt gỡ. Giữ lại thì cán bộ bấm vào dòng chương trình A lại ra danh sách đợt báo cáo toàn quốc — gây hiểu nhầm là đã lọc theo chương trình đó. Cột đếm "Số đợt BC" theo `.md` là cách thể hiện đúng mô hình mới.

| Trường | Nội dung |
|---|---|
| Bản `.docx` đối chiếu | `HTPLDN-PTYC-CT-v2.0.docx` · 10/07/2026 · nhóm Zalo |
| Trích `.docx` | Mục 4.15.1.2.2, bảng danh sách, dòng 13 — cột "Đợt báo cáo", kiểu *Liên kết*: "Liên kết nhanh mở màn hình «Đợt báo cáo định kỳ» độc lập" |
| Trích `.md` | `srs-fr-15-ct-htpldn.md:1113` — cột thứ 9 là *"So dot BC"* (số đếm), không có cột liên kết |
| Hướng | **A** — `.docx` mô tả thừa, là tàn dư mô hình drill-down đã bỏ theo STT 52 |
| Dev action | Không |
| Doc action | Bên soạn tài liệu bàn giao đổi dòng 13 thành cột "Số đợt BC" (số đếm) ở bản kế tiếp |
| Sheet | Resolve |

**→ Kết luận `KHTHCTHTPLDN_03`: Loại 4A cho câu 2 + Loại 2 dọn đặc tả cho câu 1. Phần mềm đúng ở cả tên cột lẫn cấu trúc màn. Dev action: Không. Doc action: BA gỡ `:1101` + `:1143`–`:1166` khỏi `.md`; bên soạn tài liệu bàn giao sửa dòng 13 của `.docx`. Sheet: Resolve.** **✅ BA duyệt 2026-07-30.**

**Phản hồi gửi đối tác:** *"Xác nhận bản SRS docx đang outdate. Sẽ gửi lại bản cập nhật mới nhất khi bàn giao fix bug tuần."*

> **Không thuộc phạm vi câu hỏi này:** bảng danh sách vẫn thiếu cột "Lĩnh vực pháp lý" mà `:1113` đã quy định — `BUG-CT-BANG-THIEU-COT-LINHVUC`, dòng `KHTHCTHTPLDN_OOS_05`, đang Open, không chờ BA.

> **Khi gửi bản `.docx` mới, gửi kèm danh sách mã test case cần sửa Kết quả mong đợi** — ít nhất `KHTHCTHTPLDN_03` (cột Đợt báo cáo), `KHTHCTHTPLDN_12` (khối thông tin nhanh), `QLKCHTV_36` (nút Lưu nháp). Không gửi danh sách thì đối tác chấm bản mới bằng thước cũ.

---

## KHTHCTHTPLDN_08 — Cột "Hành động" trên dòng danh sách Chương trình *(BA-24)*

**(1) Phần mềm đúng `.md` chưa?** `.md` im lặng đúng chỗ đang tranh chấp: `:1113` chỉ ghi cột *"Hanh dong (conditional)"*, không liệt kê tập nút và không nói "conditional" theo tiêu chí gì. Bảng hành động theo trạng thái (`:1193`–`:1207`) map trạng thái → nút nhưng không nói nút nằm ở đâu. Đo thực tế: 8/8 dòng chỉ có nút Xem; trang chi tiết thì đủ nút vòng đời, đúng trạng thái và đúng vai trò.

**(1b) Bản `.docx` có nói khác không?** CÓ, và nói rất rõ vị trí. Mục **4.15.1.2.2** dòng 14: *"Hành động | Nhóm nút | Tổ hợp nút thao tác nhanh theo trạng thái chương trình: «Xem» (luôn có), «Tạm dừng» (khi Đang thực hiện), «Kích hoạt» (khi Đã duyệt hoặc Đã công bố), «Sửa» (khi Dự thảo)"*. Mục **4.15.1.2.3** mục 6 mô tả đủ hành vi từng nút, gồm cả hộp thoại nhập lý do khi Tạm dừng — trùng đúng ba ý của phiếu.

**(2) Đối tác yêu cầu khác gì?** Không đòi gì ngoài tài liệu.

**(3) Có bắt buộc không?** Mức vừa. Chức năng nghiệp vụ không thiếu (trang chi tiết đã đủ), nhưng cán bộ theo dõi nhiều chương trình phải mở từng trang chi tiết để tạm dừng hoặc kích hoạt.

**Phân định hướng:** **Tầng 3** của cây trọng tài — chữ *"conditional"* ở `:1113` chỉ có nghĩa nếu tập nút **thay đổi theo điều kiện**; nếu cột chỉ có mỗi nút Xem thì không việc gì phải ghi "conditional". Tức bản gốc đã ngầm định tập nút thay đổi theo trạng thái, chỉ thiếu phần liệt kê. `.docx` liệt kê đúng phần thiếu đó, và khớp với bảng `:1193`–`:1207` của chính `.md`. → **Hướng B**.

**→ Kết luận: Loại 4B — bổ sung đặc tả rồi Dev dựng. Cột "Hành động" trên dòng danh sách gồm: [Xem] luôn có · [Tạm dừng] khi Đang thực hiện (kèm hộp thoại nhập lý do bắt buộc) · [Kích hoạt] khi Đã duyệt hoặc Đã công bố · [Sửa] và [Xóa] khi Dự thảo. Các nút chịu cùng ràng buộc quyền và trạng thái như ở trang chi tiết; [Hoàn thành] không đưa lên dòng danh sách vì chỉ dành cho Cán bộ phê duyệt (`:264`, `:274`). Dev action: Có. Doc action: BA bổ sung. Sheet: Giữ xử lý (row 30).** **✅ BA duyệt 2026-07-30.**

**Phương án xử lý (cập nhật SRS):** `srs-fr-15-ct-htpldn.md:1113` — thay chữ *"Hanh dong (conditional)"* bằng danh sách nút và điều kiện hiển thị nêu trên, trỏ tới bảng `:1193`–`:1207` cho phần chuyển trạng thái.

**Điểm (c) phiếu nêu — bất đối xứng Sửa/Xóa ở dòng Dự thảo:** `:1211` ghi *"Sửa/Xóa CT: chỉ khi DU_THAO"*, nhưng ảnh của đối tác cho thấy dòng Dự thảo có biểu tượng xóa mà không có Sửa. Chốt quy tắc: dòng ở trạng thái Dự thảo có **cả** [Sửa] và [Xóa]; các trạng thái khác không có cả hai. Ghi vào `:1113` cùng lượt. Môi trường QA hiện không còn bản ghi Dự thảo nên chưa kiểm lại được — đề nghị Dev tự kiểm khi sửa, và **không** dùng điểm này làm căn cứ chấm lỗi riêng.

> **Ghi chú `.docx` cần sửa:** mục 4.15.1.2.2 có ghi chú chênh lệch *"prototype hiện cho hiển thị nút «Sửa» cả khi chương trình ở trạng thái «Chờ phê duyệt»"* — sai so với `:1211`. Bên soạn tài liệu bàn giao gỡ ghi chú này ở bản kế tiếp.

---

## Pha 4 — Kiểm định

Đã tự soi lại theo bốn góc, không lặp lại đề vòng phân tích:

**Góc 1 — Có ca nào đang xếp Loại 3 mà thực ra là Loại 4 không?** Chỉ còn một ca Loại 3 (BA-21 vế Lĩnh vực). Đã tra `.docx` mục 4.15.1.2.2: bảng bộ lọc liệt kê đúng 5 ô, không có Lĩnh vực ⇒ đúng là Loại 3, không phải Loại 4. Ngược lại, đã soi hết 23 ca còn lại để chắc không ca nào bị đẩy sang Loại 4 chỉ vì `.docx` "có nhắc" — ba ca BA-09, BA-15, BA-22 có `.docx` **cùng phía `.md`**, đã xếp Loại 1/Loại 2 chứ không xếp Loại 4.

**Góc 2 — Mỗi ca Loại 4 đã ghi đủ bản `.docx` nào · ngày · số mục chưa?** Có. Toàn bộ dùng chung `HTPLDN-PTYC-CT-v2.0.docx` · 10/07/2026 · nhóm Zalo; mỗi mục đều dẫn số mục cụ thể (4.13.1.2.2, 4.13.1.2.3, 4.13.2.2.2, 4.13.2.2.3, 4.13.2.3.2, 4.13.2.3.3, 4.13.6.2.2, 4.15.1.2.2, 4.15.1.2.3, 4.15.1.3.2, 4.16.8).

**Góc 3 — Hướng A/B đã tra hết cây trọng tài hay mới dừng ở tín hiệu?** Ba ca hướng A đều có đối chứng riêng chứ không chỉ dựa vào "`.md` không dùng ở đâu cả": BA-13 có đối chứng nhóm Hỏi đáp đặc tả lưu nháp rất kỹ; BA-20 điểm 4 có `:1120`–`:1131` liệt kê đúng bốn thông tin đó dưới dạng trường; BA-23 câu 2 có quyết định STT 52 và mâu thuẫn tự thân trong chính ô mô tả của `.docx`.

**Góc 4 — Ràng buộc trường và độ phủ ý con.** Rà lại các ý con của phiếu để không bỏ sót: ý phụ "tệp xuất ra là tệp cũ" của `QLKCHTV_13` (đã có phản hồi riêng — không tái hiện), ý (c) bất đối xứng Sửa/Xóa của `KHTHCTHTPLDN_08` (đã chốt quy tắc, ghi rõ chưa re-verify được), lỗi lệch ngày trong tệp Excel chương trình (đã tách dòng riêng, ưu tiên trước tên tệp), lỗi 400 của nhóm API (tách khỏi việc đổi đường dẫn).

**Điểm đã tự sửa trong lúc kiểm định:** ban đầu xếp BA-13 nguyên khối theo hướng B. Đọc lại `:235` và đối chứng `srs-fr-02-hoi-dap.md:1127` thì thấy phải tách hai ý — cảnh báo rời màn là Loại 1 theo quy ước UI-08, còn nút Lưu nháp là 4A. Giữ nguyên khối sẽ tạo việc backend không cần thiết.

**Chưa làm:** vòng soi bằng Codex (chạy chế độ chỉ đọc) như Pha 4 mục 1 yêu cầu — công cụ không sẵn trong phiên này. Nếu cần lớp kiểm định độc lập, đề nghị chạy riêng với đầu vào là bảng phân loại ở mục "Cập nhật sheet" dưới đây.

---

## Pha 5 — Cập nhật sheet

**✅ Đã ghi xong 30/07/2026** — 24 ô cột Q + 1 ô cột P, đã xác minh trên bản tải lại.

### Xác định đúng đích ghi — hai điểm suýt sai

Phiếu QA ghi *"tab `UAT_TGPL Doanh Nghiệp-tuần 4`"* và đánh số dòng 2…35. Đối chiếu thực tế khác cả hai:

1. **Không có tab riêng tên "…-tuần 4".** Tuần 4 là **một khối nằm trong** tab `UAT_TGPL Doanh Nghiệp` (`gid=799081340`) của sheet `1dJat1cc68-TNuX_ibzBK-0NcgOWvPLu6aioiEgeUa5c`. Tab này có 1.672 dòng, cột "Tuần" chia 4 khối: Tuần 1 (244 dòng) · Tuần 2 (314) · Tuần 3 (962) · **Tuần 4 (146 dòng, từ dòng 1527 đến 1672)**.
2. **Tệp có một tab nhân đôi dễ ghi nhầm:** `Bản sao của UAT_TGPL Doanh Nghiệp` (`gid=129281948`), 1.676 dòng, khối Tuần 4 nằm ở 1531–1676 — **lệch đúng 4 dòng** so với tab chính. Phân biệt bằng dữ liệu: tab chính đã có 34 dòng Tuần 4 mang trạng thái dev (33 `InProcess` + 1 `dev done`), bản sao trống hoàn toàn. **Luôn kiểm tên tab đang mở trước khi ghi, không tin mỗi `gid`.**
3. **Số dòng 2…35 trong phiếu QA là số thứ tự trong khối**, không phải dòng thật. Ghi theo số đó sẽ đè vào vùng Tuần 1.
4. Đã đối chiếu từng mã: **24/24 khớp 1-1** trong khối Tuần 4 của tab chính, không mã nào trùng sang khối tuần khác.
5. Cột đích dò theo **tên tiêu đề** (không ghi cứng chữ cái): `Trạng thái dev fix` = **cột P** · `DEV phản hồi lần 1` = **cột Q**. Hai cột vòng hai (`Trạng thái dev fix 2` = V · `DEV phản hồi lần 2` = W) **để trống**, đợt này là vòng phản hồi đầu.

### Hai ràng buộc của sheet phải biết trước khi ghi

- **Cột P có xác thực dữ liệu, chỉ nhận 6 giá trị:** `New`, `Reopent`, `InProcess`, **`Resoved`**, `Reject`, `dev done`. Giá trị "đã giải quyết" trong sheet **viết thiếu chữ l** — nhập `Resolve` bị chặn, phải nhập đúng `Resoved`. Đề nghị đơn vị quản trị sheet sửa chính tả giá trị này; trước khi sửa thì mọi lượt ghi phải theo đúng chữ sai đó.
- **Cột Mã TC vẫn là công thức**, chưa chuyển sang giá trị cố định: `=IF(G{n}<>"";"QLKCHTV_"&TEXT(COUNTIF(...);"00");"")`. Nghĩa là chèn hoặc xóa dòng sẽ **đánh số lại toàn bộ mã phía dưới**, phá vỡ mọi ánh xạ mã ↔ dòng đã ghi. Thỏa thuận "mã là duy nhất và cố định" chưa được áp vào tab này. **Đề nghị chuyển cột Mã TC sang giá trị cố định trước đợt ghi sau.**

### Bảng ghi — theo từng dòng test case, không gộp

| Dòng sheet | Số trong khối | Mã TC | Mã BA | Cột P — Trạng thái dev fix | Cột Q — DEV phản hồi lần 1 |
|:-:|:-:|---|---|---|---|
| 1527 | 2 | QLKCHTV_02 | BA-01, BA-08 | *giữ nguyên* | Câu chung |
| 1529 | 4 | QLKCHTV_04 | BA-08 | *giữ nguyên* | Câu chung |
| 1535 | 5 | QLKCHTV_10 | BA-04 | *giữ nguyên* | Câu chung |
| 1537 | 6 | QLKCHTV_12 | BA-02, BA-03, BA-04 | *giữ nguyên* | Câu chung |
| 1538 | 7 | QLKCHTV_13 | BA-02, BA-07 | *giữ nguyên* | Riêng — BA-07 |
| 1539 | 8 | QLKCHTV_14 | BA-05, BA-08 | *giữ nguyên* | Câu chung |
| 1541 | 9 | QLKCHTV_16 | BA-08 | *giữ nguyên* | Câu chung |
| 1543 | 10 | QLKCHTV_18 | BA-06 | *giữ nguyên* | Câu chung |
| 1547 | 11 | QLKCHTV_22 | BA-09, BA-10 | *giữ nguyên* | Câu chung |
| 1551 | 14 | QLKCHTV_26 | BA-09, BA-14 | *giữ nguyên* | Câu chung |
| 1556 | 15 | QLKCHTV_31 | BA-11 | *giữ nguyên* | Câu chung |
| 1557 | 16 | QLKCHTV_32 | BA-12 | *giữ nguyên* | Câu chung |
| 1561 | 18 | QLKCHTV_36 | BA-13 | *giữ nguyên* | Riêng — BA-13 |
| 1562 | 19 | QLKCHTV_37 | BA-03 | *giữ nguyên* | Câu chung |
| 1570 | 22 | PDNDCHTV_07 | BA-15 | *giữ nguyên* | Câu chung |
| 1572 | 23 | QLCKCHTV_02 | BA-16 | *giữ nguyên* | Câu chung |
| 1578 | 25 | TKCHTV_02 | BA-17 | *giữ nguyên* | Câu chung |
| 1579 | 26 | TKCHTV_03 | BA-18 | *giữ nguyên* | Câu chung |
| **1612** | 28 | KHTHCTHTPLDN_03 | BA-23 | **Resoved** | Câu chuẩn hướng A |
| 1616 | 29 | KHTHCTHTPLDN_07 | BA-19 | *giữ nguyên* | Câu chung |
| 1617 | 30 | KHTHCTHTPLDN_08 | BA-24 | *giữ nguyên* | Câu chung |
| 1621 | 31 | KHTHCTHTPLDN_12 | BA-20 | *giữ nguyên* | Riêng — BA-20 |
| 1625 | 32 | TKKHCTHTPL_01 | BA-21 | *giữ nguyên* | Riêng — BA-21 |
| 1662 | 35 | TKVVHTPLDN_01 | BA-22 | *giữ nguyên* | Câu chung |

**Chỉ 1 ô cột P phải đổi giá trị** (dòng 1612 = `Resoved`); 23 dòng còn lại giữ nguyên trạng thái đang xử lý, chỉ điền cột Q. **Không dòng nào Reject** — đối tác quan sát đúng ở cả 24 mục.

**Vẫn phải làm đúng thứ tự Pha 5 khi ghi:** số dòng ở trên chốt theo bản tải về ngày 30/07/2026 — sheet là mục tiêu di động, người kiểm thử có thể chèn/xóa dòng. **Đọc lại cột Mã TC tại đúng dòng ngay trước khi ghi**, ghi theo lô, rồi tải lại kiểm hai điều: đúng số ô đã đổi, và Mã TC tại mỗi dòng vừa ghi vẫn là mã dự kiến.

---

## Việc phải làm sau khi BA duyệt phiếu

**1. Sửa SRS — pha riêng.** BA chốt 2026-07-30 là **chưa sửa ở lượt này**, đóng dấu duyệt phiếu trước. Khi chạy đợt sửa, gom theo tệp:
- `srs-fr-13-tv-nhanh.md`: BA-01, BA-02, BA-03, BA-04, BA-05, BA-06, BA-07, BA-08, BA-10, BA-11, BA-12, BA-14, BA-15, BA-16, BA-17, BA-18
- `srs-fr-15-ct-htpldn.md`: BA-19, BA-20, BA-23, BA-24
- `srs-fr-16-api.md`: BA-22 — đổi đường dẫn **cả 19 giao diện** sang dạng đã triển khai, đối chiếu theo bản mô tả API đang chạy
- `srs-v3.5.md`: BA-08 (đồng bộ bản sao entity `KHO_CAU_HOI`)
- `CHANGELOG-v3-to-v3.5.md`: BA-02 (ghi đã áp mục 9) · BA-09 (đánh dấu mục 6, 7 là mô tả v3 cũ) · BA-22 (ghi việc bỏ hẳn `danh-sach-api.md`)

**Đề nghị chia 2 pha khi chạy:** pha 1 nhóm X.2 (`srs-fr-13` + `srs-v3.5` đồng bộ entity), dừng để BA rà; pha 2 nhóm XI và nhóm XII (`srs-fr-15` + `srs-fr-16` + CHANGELOG).

**2. Cập nhật `.docx` — việc của bên soạn tài liệu bàn giao, không phải Dev.** Ba mục gỡ (đã duyệt): nút Lưu nháp ở 4.13.2.3.3 (BA-13) · khối thông tin nhanh ở 4.15.1.3.2 dòng 4–7 (BA-20) · cột liên kết Đợt báo cáo ở 4.15.1.2.2 dòng 13 (BA-23). Ba mục sửa cho khớp: tập cột tệp xuất chương trình 9 → 10 cột (BA-19) · gỡ ghi chú chênh lệch sai về nút Sửa (BA-24) · đường dẫn ở phần Tham chiếu của 4.16.1–4.16.19 theo dạng đã triển khai (BA-22). **Ghi vào sổ nội dung đã cố ý gỡ** theo mục Phòng ngừa tái diễn của quy trình, để lượt sau không thêm lại.

**3. Gửi kèm bản `.docx` mới: danh sách mã test case cần sửa Kết quả mong đợi** — `QLKCHTV_36`, `KHTHCTHTPLDN_03`, `KHTHCTHTPLDN_12`. Kèm theo **thông báo dạng đường dẫn chính thức của nhóm giao diện tích hợp** (BA-22), vì đối tác đang cầm tài liệu ghi dạng cũ.

**4. Chuyển bên vận hành:** cấp chứng thư số phía khách cho môi trường UAT, nếu không thì nhóm FR-XII không kiểm thử được ở mọi vòng tiếp theo (BA-22).

---

*Phiếu lập 30/07/2026 theo `QUY-TRINH-phan-tich-bug-nghiep-vu.md`. Phần "Chốt" chỉ có hiệu lực khi BA đóng dấu duyệt vào từng mục.*
