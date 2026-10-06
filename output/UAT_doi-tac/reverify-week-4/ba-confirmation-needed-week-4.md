# BA confirmation needed — UAT đối tác tuần 4 (PM HTPLDN) — 2026-07-27

| Thông tin | Giá trị |
|-----------|---------|
| **Dự án** | Phần mềm Hỗ trợ pháp lý doanh nghiệp (PM HTPLDN) |
| **Môi trường verify** | https://18.143.165.120.nip.io |
| **Đợt** | UAT đối tác tuần 4 · vòng 1 |
| **Nguồn đặc tả đối chiếu** | `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/` |
| **Sheet** | tab `UAT_TGPL Doanh Nghiệp-tuần 4` |
| **Cập nhật** | 2026-07-27 |

> **File này để làm gì:** gom các testcase mà QA **không tự chốt verdict được** hoặc cần BA phản hồi lại đối tác, kèm đầy đủ đối chiếu SRS + evidence UI để BA quyết nhanh. KHÔNG dùng file này thay bug-report — bug có SRS reference rõ đã log ở [bug-reports/bug-report-UAT-tuan-4.md](bug-reports/bug-report-UAT-tuan-4.md).

> **2 dạng case:**
> - **Dạng A — QA đã có kết luận, cần BA phản hồi đối tác.** Bộ mục: *Bối cảnh → Đối chiếu SRS → Citation → Kết quả verify UI → Kết luận QA → Nội dung đề xuất BA phản hồi đối tác*.
> - **Dạng B — SRS tự mâu thuẫn, QA không tự chốt được.** Bộ mục: *Bối cảnh → Kết quả verify UI → Điểm mâu thuẫn trong SRS → Câu hỏi cần BA xác nhận → Đề xuất QA tạm thời*.
>
> Phân dạng trong file này: **Dạng B** — BA-02, BA-08, BA-09, BA-22, BA-23. **Dạng A** — 19 câu còn lại (riêng **BA-20** là dạng A nhưng có **1 điểm mang tính dạng B**: nhãn trạng thái `CHO_PHE_DUYET` được đặc tả ghi 2 dạng khác nhau).

> **Nguồn citation:** `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/` — **nguồn duy nhất chốt 2026-07-25** (CLAUDE.md §Quick reference). Bản `input/srs-update-2026-5-5/` lệch số dòng và lệch cả nội dung nên KHÔNG dùng để quote. Mọi số dòng dưới đây đã mở file verify, không lấy từ trí nhớ. Template [ba-confirmation-needed-template.md](../../template/ba-confirmation-needed-template.md) đã được sửa cùng ngày để trỏ đúng nguồn này ⇒ file này **không còn lệch** so với template.

> **Cách đặt tiêu đề mỗi câu hỏi (theo template):** `## <MÃ_TC> — <tiêu đề> *(BA-NN · Dạng A|B)*`. Mã BA-NN giữ nguyên vì đang được tham chiếu ở bảng đối chiếu điều kiện `cond/`, note gửi đối tác, [bug-reports/bug-report-UAT-tuan-4.md](bug-reports/bug-report-UAT-tuan-4.md) và các audit. Một mã TC có thể xuất hiện ở 2 câu hỏi khác nhau (`QLKCHTV_02` → BA-01 + BA-08 · `QLKCHTV_12` → BA-02 + BA-03 · `QLKCHTV_14` → BA-05 + BA-08 · `QLKCHTV_22` → BA-09 + BA-10 · `QLKCHTV_26` → BA-09 + BA-14) — phân biệt bằng tiêu đề và mã BA-NN, không phải bằng mã TC.

**Tình trạng:** 24 câu hỏi · 0 đã chốt · 24 đang chờ.

> **Phạm vi:** BA-01…BA-08 từ **Luồng 1 — Kho câu hỏi**; BA-09…BA-14 từ **Luồng 2 — Tư vấn nhanh**; BA-15 **Luồng 3**; BA-16 **Luồng 4**; BA-17…BA-18 **Luồng 5**; BA-19…BA-20 + **BA-23…BA-24** **Luồng 6**; BA-21 **Luồng 7**; BA-22 **Luồng 9**.

> **Bổ sung 2026-07-27 (sau audit verdict `Reject`):** BA-23 và BA-24 mở mới, BA-20 mở rộng thêm 2 câu hỏi. Nguyên nhân: audit lại 3 dòng đang mang `Reject` của tab tuần 4 cho thấy cả 3 đối tác **quan sát đúng hiện trạng**, tranh chấp nằm ở **đặc tả** — theo `QA_VERIFY_PROTOCOL.md` §Verdict thì đó là `BA confirm`, không phải `Reject`. Verdict trên sheet đã đổi `Reject` → `BA confirm` cho row 28, 30, 31. Chi tiết: [reverify-audit/audit-reject-2026-07-27/AUDIT-reject-tuan-4.md](reverify-audit/audit-reject-2026-07-27/AUDIT-reject-tuan-4.md).

| Mã | Dạng | Chủ đề | Case liên quan | Mức ảnh hưởng | Tình trạng |
|---|:-:|---|---|---|---|
| BA-01 | A | Ô lọc có mặc định "Tất cả" không | QLKCHTV_02 (row 2) | Thấp | ⏳ Chờ BA |
| BA-02 | B | Chức năng Xuất Excel Kho câu hỏi chưa được gộp vào FR | QLKCHTV_12 (row 6), QLKCHTV_13 (row 7) | **Cao** — chặn 2 case | ⏳ Chờ BA |
| BA-03 | A | Quy tắc đặt tên file + tập cột của file xuất | QLKCHTV_12 (row 6), QLKCHTV_37 (row 19) | Trung bình | ⏳ Chờ BA |
| BA-04 | A | Nhãn hiển thị tiếng Việt cho nguồn `IMPORT` | QLKCHTV_10 (row 5), QLKCHTV_12 (row 6) | Thấp | ⏳ Chờ BA |
| BA-05 | A | Màn chi tiết có phải hiển thị "Lịch sử thẩm định" | QLKCHTV_14 (row 8) | Trung bình | ⏳ Chờ BA |
| BA-06 | A | Bật/tắt hiệu lực có bắt buộc hộp thoại xác nhận | QLKCHTV_18 (row 10) | Trung bình | ⏳ Chờ BA |
| BA-07 | A | Xuất Excel khi không có dữ liệu: chặn hay xuất file rỗng | QLKCHTV_13 (row 7) | Trung bình | ⏳ Chờ BA |
| BA-08 | B | Mâu thuẫn nội bộ trong SRS về entity `KHO_CAU_HOI` | QLKCHTV_02 (row 2), QLKCHTV_04 (row 4), QLKCHTV_14 (row 8), QLKCHTV_16 (row 9) | **Cao** — ảnh hưởng cách fix | ⏳ Chờ BA |
| BA-09 | B | Mâu thuẫn nội bộ trong SRS về máy trạng thái `SM-TVNHANH` (4 hay 6 trạng thái) | QLKCHTV_22 (row 11), QLKCHTV_26 (row 14) · toàn Luồng 2 | **Cao** — ảnh hưởng cách fix | ⏳ Chờ BA |
| BA-10 | A | Cột "Ngày gửi" có cần hiển thị giờ phút không | QLKCHTV_22 (row 11) | Thấp | ⏳ Chờ BA |
| BA-11 | A | Có cảnh báo trước khi ghi đè nội dung tự soạn khi chọn Q&A khác không | QLKCHTV_31 (row 15) | Trung bình | ⏳ Chờ BA |
| BA-12 | A | Bấm mã Q&A trong kết quả tra cứu có mở cửa sổ chi tiết không | QLKCHTV_32 (row 16) | Thấp | ⏳ Chờ BA |
| BA-13 | A | Màn trả lời Tư vấn nhanh có cần [Lưu nháp] không | QLKCHTV_36 (row 18) | Trung bình | ⏳ Chờ BA |
| BA-14 | A | Khối "Thông tin DN" ở cột trái gồm những trường bắt buộc nào | QLKCHTV_26 (row 14) | Trung bình | ⏳ Chờ BA |
| BA-15 | A | Duyệt hàng loạt có phải gửi thông báo cho từng cán bộ tạo không | PDNDCHTV_07 (row 22) | Trung bình — ảnh hưởng phạm vi fix | ⏳ Chờ BA |
| BA-16 | A | Mô tả công khai để trống thì có được tự điền bằng nội dung câu hỏi không | QLCKCHTV_02 (row 23) | Thấp | ⏳ Chờ BA |
| BA-17 | A | Câu thông báo khi lọc/tìm không khớp trên màn danh sách Kho câu hỏi và Tư vấn nhanh | TKCHTV_02 (row 25) | Thấp | ⏳ Chờ BA |
| BA-18 | A | Màn Kho câu hỏi có phải có nút [Xóa bộ lọc] như Tư vấn nhanh không | TKCHTV_03 (row 26) | Thấp | ⏳ Chờ BA |
| BA-19 | A | Tên tệp Excel xuất từ màn Chương trình HTPLDN theo quy ước nào | KHTHCTHTPLDN_07 (row 29) | Thấp | ⏳ Chờ BA |
| BA-20 | A (1 điểm dạng B) | Bố cục đầu trang Chi tiết chương trình — cần bản đặc tả màn hình (UX) để đối chiếu; **+ nhãn `CHO_PHE_DUYET`: "Chờ PD" hay "Chờ phê duyệt"** | KHTHCTHTPLDN_12 (row 31) | Trung bình — 4 điểm phiếu nêu đều quan sát đúng nhưng thiếu căn cứ chấm; riêng nhãn trạng thái thì SRS ghi 2 dạng | ⏳ Chờ BA |
| BA-21 | A | Thanh lọc màn Chương trình HTPLDN có bổ sung tiêu chí Lĩnh vực pháp lý không | TKKHCTHTPL_01 (row 32) | Thấp — phần xử lý phía sau đã hỗ trợ sẵn | ⏳ Chờ BA |
| BA-22 | B | Hai tài liệu đang mô tả hai đường dẫn khác nhau cho cùng nhóm API tích hợp (FR-XII) — chốt bản nào là hợp đồng chính thức | TKVVHTPLDN_01 (row 35) | Trung bình — bên tiêu thụ đọc 2 tài liệu sẽ nhận 2 câu trả lời khác nhau | ⏳ Chờ BA |
| BA-23 | B | Màn "Đợt báo cáo": đặc tả vừa ghi tab độc lập (dòng 618) vừa ghi thẻ trong chi tiết CT (dòng 1101, 1143-1166) — chốt mô hình nào; có cần liên kết nhanh từ dòng CT không | KHTHCTHTPLDN_03 (row 28) | Trung bình — quyết cả tập cột bảng danh sách lẫn cấu trúc trang chi tiết | ⏳ Chờ BA |
| BA-24 | A | Cột "Hành động" trên dòng danh sách CT: chỉ nút Xem, hay hiển thị thêm nút theo trạng thái (Kích hoạt / Tạm dừng / Sửa) | KHTHCTHTPLDN_08 (row 30) | Trung bình — quyết phạm vi fix phía giao diện danh sách | ⏳ Chờ BA |

---

## QLKCHTV_02 — Ba ô lọc Lĩnh vực / Nguồn / Trạng thái có phải mặc định "Tất cả" không? *(BA-01 · Dạng A)*

**Bối cảnh testcase**

- Dòng Excel: row 2, mã TC `QLKCHTV_02` — ý 2 của phiếu.
- Nội dung kiểm tra: CB Nghiệp vụ Trung ương mở màn danh sách **Kho câu hỏi**, kiểm thanh lọc.
- Expected trong file UAT: ba ô lọc Lĩnh vực / Nguồn / Trạng thái hiển thị giá trị mặc định **"Tất cả"**.
- Actual đối tác ghi: ba ô lọc không hiển thị "Tất cả".

**Đối chiếu SRS v3.5**

- Quy ước giao diện UI-11 chỉ ràng buộc ô lọc **chọn nhiều** phải có mục "Tất cả"; **không** có quy định nào cho ô lọc chọn đơn.
- Ba ô lọc đang xét là ô **chọn đơn**, nên không thuộc phạm vi UI-11.
- Chữ "Tất cả" duy nhất xuất hiện ở màn này là **tên thẻ (tab)** của danh sách, không phải giá trị mặc định của ô lọc.

**Citation**

- `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-v3.5.md:580` (quy ước UI-11)
- `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-13-tv-nhanh.md:530` (SCR-X2-01 — mô tả thanh lọc Kho câu hỏi)

**Kết quả verify UI hiện tại**

- Verify lại ngày 27/07/2026 qua Chrome DevTools MCP, tài khoản UAT `cbnv_tw` (CB Nghiệp vụ - Trung ương, đơn vị BTP · TW) — đúng vai trò đối tác đã dùng.
- Mở URL `https://18.143.165.120.nip.io/tv-nhanh/kho-cau-hoi` (màn danh sách Kho câu hỏi).
- Cả 3 ô lọc đang ở trạng thái **chữ mờ gợi ý**, chưa chọn giá trị nào — tái hiện đúng như đối tác mô tả.
- Danh sách vẫn trả về đủ bản ghi khi chưa chọn lọc, tức hành vi lọc không bị sai; chỉ là cách hiển thị mặc định.
- Evidence: `bug-reports/image/BUG-QLKCHTV_02-dropdown-trangthai.png` · `bug-reports/image/BUG-QLKCHTV_02-dropdown-nguon.png`

**Kết luận QA**

- `QLKCHTV_02` ý 2: **chưa đủ căn cứ chấm là bug** theo SRS v3.5 — đặc tả im lặng cho ô lọc chọn đơn.
- Hiện tượng đối tác nêu là **có thật**, nhưng không vi phạm dòng đặc tả nào.
- Ý 1 và ý 3 của cùng case đã được chấm `Open` và log bug riêng — xem `BUG-QLKCHTV_02`.

**Nội dung đề xuất BA phản hồi đối tác**

Đề nghị BA chốt: có bổ sung yêu cầu 3 ô lọc chọn đơn này mặc định hiển thị "Tất cả" không?

- **Nếu CÓ** → mở bug giao diện mức Minor, gộp cùng `BUG-QLKCHTV_02`, đồng thời bổ sung câu quy định vào `srs-fr-13-tv-nhanh.md:530`.
- **Nếu KHÔNG** → trả lời đối tác là hành vi đúng đặc tả hiện hành, đóng ý này.
- Verdict QA đề xuất: `Cần BA xác nhận`, chưa gửi Dev cho riêng ý này.

---

## QLKCHTV_12 (và QLKCHTV_13) — Chức năng "Xuất Excel" của Kho câu hỏi chưa được gộp vào FR đang hiệu lực *(BA-02 · Dạng B)*

**Bối cảnh testcase**

- Dòng Excel: row 6, mã TC `QLKCHTV_12`; row 7, mã TC `QLKCHTV_13`.
- Nội dung kiểm tra: CB Nghiệp vụ Trung ương dùng nút **[Xuất Excel]** trên màn danh sách Kho câu hỏi.
- Expected trong file UAT: nút [Xuất Excel] tồn tại và xuất file theo bộ lọc hiện tại, có quy tắc tên file và tập cột cụ thể.
- **Đây là câu hỏi chặn — trả lời BA-02 xong mới xử lý được BA-03 và BA-07.**

**Kết quả verify UI hiện tại**

- Verify lại ngày 27/07/2026 qua Chrome DevTools MCP, tài khoản UAT `cbnv_tw` (CB Nghiệp vụ - Trung ương).
- Mở đúng màn danh sách Kho câu hỏi, URL là `https://18.143.165.120.nip.io/tv-nhanh/kho-cau-hoi`.
- Nút **[Xuất Excel]** **ĐÃ có** trên thanh công cụ và **chạy được**: `POST /api/v1/kho-cau-hois/export` → 200, tải về tệp `.xlsx`.
- Đã kiểm tệp có áp dụng bộ lọc: không lọc (13 bản ghi) = 8.075 byte · lọc Lĩnh vực (6 bản ghi) = 7.433 byte · lọc rỗng (0 bản ghi) = 6.655 byte.
- Evidence: `reverify-audit/QLKCHTV_12/files/lan1-kho-cau-hoi-20260727.xlsx` · `reverify-audit/QLKCHTV_13/files/loc-rong-kho-cau-hoi-20260727.xlsx`

**Điểm mâu thuẫn trong SRS v3.5**

1. Theo **CHANGELOG v3→v3.5**, chức năng Xuất Excel Kho câu hỏi **đã được chốt bổ sung** — mục *"9. FR-X.2-01 bổ sung chức năng Xuất Excel danh sách kho Q&A theo bộ lọc"* ghi rõ: *"§2 FR-X.2-01 Processing thêm bước 8 'Xuất Excel theo filter hiện tại — tối đa 10.000 dòng — trả file download'; §3 SCR-X2-01 toolbar thêm nút '[Xuất Excel]'; §3 SCR-X2-01 Quy tắc tương tác thêm bullet 'Nút [Xuất Excel] xuất danh sách Q&A theo filter hiện tại, tối đa 10.000 dòng, format .xlsx'"*.

   Citation:
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/CHANGELOG-v3-to-v3.5.md:2443-2449`

2. Nhưng **file FR đang hiệu lực KHÔNG chứa nội dung đó**:
   - phần Processing của FR-X.2-01 chỉ tới **bước 7**;
   - thanh công cụ SCR-X2-01 chỉ khai **3 nút**: *"+ Them cau hoi / Nhap Excel / Lam moi"* — không có [Xuất Excel];
   - phần Quy tắc tương tác **không có bullet nào** về Xuất Excel.

   Citation:
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-13-tv-nhanh.md:111-119` (Processing, hết ở bước 7)
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-13-tv-nhanh.md:528` (toolbar SCR-X2-01, 3 nút)
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-13-tv-nhanh.md:543-546` (Quy tắc tương tác)

**Câu hỏi cần BA xác nhận**

Mô tả trong CHANGELOG có phải bản đã chốt và cần gộp vào `srs-fr-13-tv-nhanh.md`, hay tính năng Xuất Excel Kho câu hỏi đã bị bỏ khỏi phạm vi?

1. **Hướng 1 — theo CHANGELOG (đã chốt, FR bị sót):** cập nhật FR cho khớp CHANGELOG. Khi đó các kỳ vọng của đối tác về tên tệp / tập cột / thông báo khi rỗng **có căn cứ** để chấm Open hoặc Pass.
2. **Hướng 2 — theo FR đang hiệu lực (đã bỏ khỏi phạm vi):** nút [Xuất Excel] đang có trên hệ thống là tính năng ngoài phạm vi, cần BA quyết giữ hay gỡ.

**Đề xuất QA tạm thời**

- Chưa gửi bug về Xuất Excel Kho câu hỏi cho Dev cho tới khi BA chốt source truth.
- Tạm verdict cho `QLKCHTV_12` (row 6) và `QLKCHTV_13` (row 7): phần liên quan Xuất Excel = `Cần BA xác nhận`. Các ý khác của 2 case này đã chấm độc lập.
- Nếu BA chọn hướng 1: BA-03 và BA-07 mới có cơ sở trả lời, owner dự kiến `Dev BE` (tập cột, tên tệp) + `Dev FE` (thông báo khi rỗng).
- Nếu BA chọn hướng 2: QA hạ toàn bộ kỳ vọng Xuất Excel của 2 case xuống ngoài phạm vi, và đề nghị BA quyết số phận nút đang có trên hệ thống.

---

## QLKCHTV_12 (và QLKCHTV_37) — Quy tắc đặt tên file và tập cột của file Excel xuất ra *(BA-03 · Dạng A)*

**Bối cảnh testcase**

- Dòng Excel: row 6, mã TC `QLKCHTV_12` — ý (a) và (b) của phiếu. Bổ sung: row 19, mã TC `QLKCHTV_37`.
- Nội dung kiểm tra: CB Nghiệp vụ Trung ương xuất Excel từ màn Kho câu hỏi, kiểm tên tệp và tập cột.
- Expected trong file UAT: tên tệp có `HHmm`; tập cột gồm cả "Ngày cập nhật", "Câu hỏi (đầy đủ)", "Câu trả lời (đầy đủ)".
- **Phụ thuộc BA-02** — nếu BA-02 chốt "đã bỏ khỏi phạm vi" thì câu hỏi này không còn cần thiết.

**Đối chiếu SRS v3.5**

- Đặc tả **im lặng hoàn toàn** về tên tệp và tập cột file xuất của Kho câu hỏi — đây là hệ quả trực tiếp của BA-02.
- Các nhóm khác **có** quy định rõ, dùng làm tham chiếu: nhóm Hỏi đáp quy định `HoiDap_{YYYYMMDD_HHmm}.xlsx`; nhóm Tư vấn chuyên sâu quy định `TVCS-danh-sach-{YYYYMMDD-HHmm}.xlsx`. Cả hai đều **có phần giờ phút**.
- Với `QLKCHTV_37`: đặc tả yêu cầu khối Đánh giá của phiên tư vấn nhanh có nút `[Xuat Excel]` nhưng **không quy định tên tệp cũng không quy định tập cột**. Đã tìm toàn bộ `srs-v3.5/` — không có quy tắc nào.

**Citation**

- `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-02-hoi-dap.md:151` (mẫu tên tệp nhóm Hỏi đáp)
- `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-12-tv-chuyen-sau.md:162` (mẫu tên tệp nhóm Tư vấn chuyên sâu)
- `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-13-tv-nhanh.md:574` (khối Đánh giá có nút Xuất Excel, không quy định tên tệp/tập cột)

**Kết quả verify UI hiện tại**

- Verify lại ngày 27/07/2026 qua Chrome DevTools MCP, tài khoản UAT `cbnv_tw`. **Đã tải tệp thật về và mở đọc nội dung**, không chỉ kiểm tệp tải được.
- Mở URL `https://18.143.165.120.nip.io/tv-nhanh/kho-cau-hoi` rồi bấm [Xuất Excel] trên thanh công cụ.
- Tên tệp do **máy chủ** đặt: `content-disposition: attachment; filename="kho-cau-hoi-20260727.xlsx"` — chỉ có ngày, **không có giờ phút**.
- Tệp có đúng **7 cột**: `Mã câu hỏi | Câu hỏi | Câu trả lời | Lĩnh vực | Nguồn | Trạng thái | Số lượt xem`.
- Màn hình có **12 cột**: `Mã | Câu hỏi | Lĩnh vực | Từ khóa | Nguồn | Trạng thái | Hiệu lực | Công khai | Lượt xem | Đánh giá | Ngày tạo | Hành động`.
- Vậy tệp xuất thiếu: **Từ khóa, Hiệu lực, Công khai, Đánh giá, Ngày tạo** — và cả **Ngày cập nhật** mà phiếu nêu.
- Với `QLKCHTV_37`: chức năng xuất Excel của khối Đánh giá **chưa được dựng ở cả giao diện lẫn máy chủ** — đã log `BUG-QLKCHTV_37`.
- Evidence: `reverify-audit/QLKCHTV_12/files/kho-cau-hoi-20260727.xlsx` · `bug-reports/image/BUG-TVN-danh-gia-thieu-xuat-excel.png`

**Bổ sung 28/07/2026 — rà toàn bộ 25 chức năng xuất tệp, câu hỏi này KHÔNG chỉ của Kho câu hỏi**

Đã đọc nội dung từng ô của cả 25 tệp xuất trên toàn ứng dụng (lượt 1: 16 chức năng · lượt 2: 9 chức năng còn lại), đối chiếu dãy cột tệp với dãy cột màn hình. Kết quả cho thấy hệ thống **đang tồn tại song song hai triết lý xuất tệp khác nhau**, và đây mới là gốc của câu hỏi:

| Nhóm | Màn | Cột màn hình → cột tệp | Căn cứ SRS |
|---|---|---|---|
| **A. Xuất theo biểu mẫu luật định** *(đặc tả có quy định — KHÔNG phải lỗi)* | Tư vấn viên / Chuyên gia | 9 → **10 cột hoàn toàn khác** (STT, Năm sinh, Thông tin liên hệ, Chức danh, Trình độ + số văn bằng, Chứng chỉ, Kinh nghiệm…) | `srs-fr-04-chuyen-gia-tvv.md:1455` — *"theo mẫu **Phụ lục 1 — QĐ 1322/QĐ-BTP ngày 01/6/2020** (10 cột cố định)"*. Tệp thực tế đúng 10 cột ⇒ **đạt** |
| | Tổ chức tư vấn | 8 → **18 cột** (thêm Số Giấy ĐKHĐ, Ngày cấp, Số QĐ công bố…) | `srs-fr-04-chuyen-gia-tvv.md:1644` — *"theo mẫu **Phụ lục 2 — QĐ 1322/QĐ-BTP**"* ⇒ **đạt** |
| **B. Xuất "bản sao màn hình"** *(đặc tả im lặng — cần BA chốt)* | Kho câu hỏi | 12 → 7, thiếu **Từ khóa · Hiệu lực · Công khai · Điểm TB · Ngày tạo** | `srs-fr-13-tv-nhanh.md` không nhắc nút [Xuất Excel], không có tập cột |
| | Chi trả chi phí | 9 → 9 nhưng **không trùng khớp**: thiếu **"Mức HT %"**, thêm **"Deadline SLA"**, đổi tên *Mã HS→Mã hồ sơ · Tên DN→Doanh nghiệp · SLA→Mức cảnh báo* | `srs-fr-06-chi-tra.md:1044` chỉ nhắc có nút [Xuất Excel], không quy định tập cột |
| | Thư viện biểu mẫu *(thêm sau lượt 2)* | 6 → **8** nhưng vẫn thiếu **"Số biểu mẫu" · "Đồng bộ"** (tệp bù bằng STT, Mô tả, Thứ tự, Ngày cập nhật) | `srs-v3.5/` không quy định tập cột cho màn này |
| | Nhật ký hệ thống *(thêm sau lượt 2)* | 8 → **15** nhưng thiếu **"Chi tiết thay đổi"** — cột mang giá trị tra cứu chính | `srs-v3.5/` không quy định tập cột cho màn này |

Điểm quan trọng: **nhóm A chứng minh việc tệp khác màn hình không mặc nhiên là lỗi** — có màn cố tình xuất theo biểu mẫu Nhà nước quy định, khác hẳn màn hình là đúng. Đây là lý do QA **không** áp quy tắc "tệp phải giống màn hình" một cách máy móc: nếu áp máy móc thì 2 màn nhóm A sẽ thành 2 bug sai.

**Cập nhật trạng thái xử lý (28/07/2026, sau khi chủ đợt UAT ra quyết định):** chủ đợt UAT đã chốt quy ước — *nơi nào đặc tả có quy định biểu mẫu thì theo biểu mẫu; nơi nào đặc tả im lặng thì tệp xuất phải có đủ các cột đang hiển thị trên giao diện*. Theo quy ước này, 4 màn nhóm B **đã được log thành bug** `BUG-XUAT-TEP-THIEU-COT-SO-VOI-MAN-HINH` (dòng sheet 48, mã `XUATTEP_OOS_13`). Câu hỏi gửi BA ở đây vì vậy chuyển từ *"có phải lỗi không"* sang ***"đề nghị chính thức hóa quy ước trên thành điều khoản trong đặc tả"*** — để dev có căn cứ văn bản khi fix, và để các màn xuất tệp về sau không phải tranh luận lại từ đầu.

*(Các màn còn lại trong 25 chức năng đã rà: dãy cột khớp màn hình, hoặc chỉ khác cách đặt tên cột — không nêu ở đây.)*

Evidence bổ sung: [bug-reports/image/R2-QUET-XUAT-TEP-noi-dung.log.txt](bug-reports/image/R2-QUET-XUAT-TEP-noi-dung.log.txt) *(16 chức năng lượt 1)* · [bug-reports/image/R2-QUET2-XUAT-TEP-noi-dung.log.txt](bug-reports/image/R2-QUET2-XUAT-TEP-noi-dung.log.txt) *(9 chức năng lượt 2, mục "ĐỐI CHIẾU CỘT")* — bản đọc từng ô của cả 25 tệp.

**Kết luận QA**

- `QLKCHTV_12` ý (a) và (b): **không chấm được** vì đặc tả im lặng — chờ BA-02 rồi BA-03.
- Tên tệp hiện tại nhận diện được nội dung và ngày xuất, chỉ **thiếu giờ phút** ⇒ xuất 2 lần trong ngày sẽ bị trình duyệt thêm hậu tố `(1)`.
- Tập cột hiện tại **hẹp hơn** màn hình 5 cột. Không kết luận đúng/sai vì không có danh sách cột bắt buộc để đối chiếu.
- Sau đợt rà 28/07: vấn đề **không riêng Kho câu hỏi** mà là **thiếu một quy tắc chung** áp cho mọi chức năng xuất tệp mà đặc tả im lặng (sau khi rà đủ 25 chức năng: **4 màn** — Kho câu hỏi, Chi trả chi phí, Thư viện biểu mẫu, Nhật ký hệ thống).

**Nội dung đề xuất BA phản hồi đối tác**

Đề nghị BA chốt 3 điểm, và chốt **cùng lúc cho cả Kho câu hỏi và Tư vấn nhanh** để hai chỗ dùng một quy ước (vì `QLKCHTV_37` dev sắp phải dựng mới):

1. Quy tắc đặt tên tệp xuất — có cần `HHmm` như 2 nhóm đã có quy định không?
2. Tập cột bắt buộc gồm những cột nào? Có gồm "Ngày cập nhật", "Câu hỏi (đầy đủ)", "Câu trả lời (đầy đủ)" như phiếu kỳ vọng không?
3. **(bổ sung 28/07)** Với những màn đặc tả **không** quy định biểu mẫu luật định, quy tắc mặc định của tệp xuất là gì — **đủ đúng bộ cột đang hiển thị trên màn hình**, hay được phép chọn một tập hẹp hơn? Nếu chốt "đủ bộ cột màn hình" thì đề nghị ghi thành một điều khoản chung bổ sung cho `BR-DATA-06` (`srs-fr-11-bao-cao.md:1276`) để không phải hỏi lại cho từng màn; khi đó Kho câu hỏi và Chi trả chi phí thành lỗi và chuyển dev.

- Verdict QA đề xuất: `Cần BA xác nhận`, owner sau khi chốt dự kiến `Dev BE`.
- **Lưu ý gửi kèm dev (QA chưa kết luận được, cần dev tự kiểm):** thân yêu cầu xuất có truyền `pageSize: 20`. Dữ liệu hiện tại chỉ 13 bản ghi nên chưa xác định được tệp xuất có bị giới hạn theo trang hay không — trong khi CHANGELOG nói giới hạn là 10.000 dòng.

---

## QLKCHTV_10 (và QLKCHTV_12) — Nhãn hiển thị tiếng Việt cho nguồn `IMPORT` *(BA-04 · Dạng A)*

**Bối cảnh testcase**

- Dòng Excel: row 5, mã TC `QLKCHTV_10`; row 6, mã TC `QLKCHTV_12`.
- Nội dung kiểm tra: CB Nghiệp vụ Trung ương xem cột "Nguồn" trên màn Kho câu hỏi sau khi nhập câu hỏi từ tệp Excel.
- Expected trong file UAT: nguồn `IMPORT` hiển thị **"Nhập Excel"**.
- Actual đối tác ghi: hiển thị nguyên chữ tiếng Anh "Import".

**Đối chiếu SRS v3.5**

- Đặc tả **chỉ quy định màu thẻ** cho 3 giá trị nguồn: *"TU_DONG (xanh duong, ...) / THU_CONG (vang, ...) / IMPORT (tim, ...)"*. Ứng dụng đang hiển thị đúng thẻ màu tím.
- Đặc tả **không quy định chữ hiển thị** cho bất kỳ giá trị nào trong 3 giá trị đó.
- ⇒ Không có căn cứ chấm chữ "Import" là sai; nhưng cũng không có căn cứ nói nó đúng.

**Citation**

- `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-13-tv-nhanh.md:532` (chỉ quy định màu thẻ nguồn)
- `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-13-tv-nhanh.md:102` và `:688` (enum `IMPORT`)

**Kết quả verify UI hiện tại**

- Verify lại ngày 27/07/2026 qua Chrome DevTools MCP, tài khoản UAT `cbnv_tw`.
- Mở URL `https://18.143.165.120.nip.io/tv-nhanh/kho-cau-hoi` (bảng danh sách) và `https://18.143.165.120.nip.io/tv-nhanh/kho-cau-hoi/{id câu hỏi}` (màn chi tiết, mở từ dòng danh sách).
- Cùng cột "Nguồn": `TU_DONG` → "Tự động", `THU_CONG` → "Thủ công", riêng `IMPORT` → giữ nguyên **"Import"**.
- Lặp lại ở **3 nơi**: bảng danh sách, màn chi tiết, và tệp Excel xuất ra.
- Evidence: `bug-reports/image/BUG-QLKCHTV_10-ketqua-nhap.png` · `bug-reports/image/BUG-QLKCHTV_14-chi-tiet-co-tu-khoa.png`

**Kết luận QA**

- Phần **không nhất quán** (2 giá trị đã Việt hoá, 1 giá trị chưa) đã chấm `Open` và log `BUG-QLKCHTV_10` — căn cứ là tính nhất quán trong cùng một cột, không cần BA.
- Phần **chữ cụ thể phải là gì** thì không chấm được, vì đặc tả không quy định chữ hiển thị ⇒ đưa vào đây.

**Nội dung đề xuất BA phản hồi đối tác**

Đề nghị BA chốt chữ hiển thị chính thức cho nguồn `IMPORT`: "Nhập Excel" (như phiếu kỳ vọng), "Nhập từ Excel", hay giữ "Import"?

- **Đề xuất của QA:** chốt một chữ tiếng Việt để đồng bộ với 2 giá trị còn lại, vì đây là phần mềm tiếng Việt phục vụ cán bộ nghiệp vụ.
- Verdict QA đề xuất: bug về tính không nhất quán = `Vẫn lỗi — owner: Dev FE`; riêng chữ cụ thể = `Cần BA xác nhận`.
- Đề nghị BA trả lời sớm để dev sửa **một lần** cho cả 3 nơi đang hiển thị.

---

## QLKCHTV_14 — Màn chi tiết câu hỏi có phải hiển thị "Lịch sử thẩm định" không? *(BA-05 · Dạng A)*

**Bối cảnh testcase**

- Dòng Excel: row 8, mã TC `QLKCHTV_14` — ý 3 của phiếu.
- Nội dung kiểm tra: CB Nghiệp vụ Trung ương mở màn chi tiết một câu hỏi trong Kho câu hỏi.
- Expected trong file UAT: màn chi tiết hiển thị mục **"Lịch sử thẩm định"**.
- Actual đối tác ghi: không có mục này.

**Đối chiếu SRS v3.5**

- Đặc tả liệt kê các trường màn chi tiết phải hiển thị: *"Chi tiet Q&A: side panel/modal hien thi day du cau hoi, cau tra loi (rich text), linh vuc, tu khoa, nguon, nguoi tao"* — **không có** lịch sử thẩm định.
- Đã tìm toàn bộ file FR nhóm X.2: **không có** mục "Lịch sử thẩm định" nào cho Kho câu hỏi.
- ⇒ Theo đặc tả hiện hành, việc không có mục này **không sai**.

**Citation**

- `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-13-tv-nhanh.md:545` (danh sách trường màn chi tiết Q&A)

**Kết quả verify UI hiện tại**

- Verify lại ngày 27/07/2026 qua Chrome DevTools MCP, tài khoản UAT `cbnv_tw`.
- Mở URL `https://18.143.165.120.nip.io/tv-nhanh/kho-cau-hoi/{id câu hỏi}` — màn chi tiết câu hỏi, mở từ dòng ở `https://18.143.165.120.nip.io/tv-nhanh/kho-cau-hoi`.
- Panel chi tiết hiển thị `Mã · Lĩnh vực · Nguồn · Trạng thái · Công khai · Hiệu lực · Lượt xem · Đánh giá TB · Ngày tạo · Ngày duyệt`, rồi tới Câu hỏi / Câu trả lời. Không có mục lịch sử thẩm định.
- **Dữ liệu đã sẵn sàng nếu BA yêu cầu dựng:** máy chủ đã trả về đủ nguyên liệu — `nguoiGuiDuyetId`, `ngayGuiDuyet`, `nguoiDuyetId`, `ngayDuyet`, `ghiChuPheDuyet`.
- Evidence: `bug-reports/image/BUG-QLKCHTV_14-chi-tiet-co-tu-khoa.png`

**Kết luận QA**

- `QLKCHTV_14` ý 3: **không phải bug** theo SRS v3.5 — đặc tả không yêu cầu mục này.
- Kỳ vọng của đối tác nhiều khả năng đến từ tài liệu thiết kế khác, không phải SRS v3.5.
- Các ý khác của case đã chấm riêng — xem `BUG-QLKCHTV_14`.

**Nội dung đề xuất BA phản hồi đối tác**

Đề nghị BA chốt: màn chi tiết có phải hiển thị lịch sử thẩm định không? Nếu có thì gồm những mốc nào (gửi duyệt / duyệt / từ chối kèm lý do)?

- **Nếu CÓ** → bổ sung vào `srs-fr-13-tv-nhanh.md:545`, mở bug giao diện mức Medium. Thuận lợi: dữ liệu máy chủ đã có sẵn, dev chỉ cần dựng phần hiển thị.
- **Nếu KHÔNG** → trả lời đối tác là ngoài phạm vi v3.5, đóng ý này.
- Verdict QA đề xuất: `Không phải bug theo SRS` cho ý 3, chưa gửi Dev.

---

## QLKCHTV_18 — Bật/tắt hiệu lực có bắt buộc hộp thoại xác nhận không, và câu chữ chuẩn là gì? *(BA-06 · Dạng A)*

**Bối cảnh testcase**

- Dòng Excel: row 10, mã TC `QLKCHTV_18`.
- Nội dung kiểm tra: CB Nghiệp vụ Trung ương gạt công tắc Hiệu lực của một câu hỏi trong Kho câu hỏi (đo cả 2 chiều bật và tắt).
- Expected trong file UAT: hộp thoại xác nhận với câu *"Bạn có chắc chắn muốn đánh dấu câu hỏi «{mã}» là «{hết hiệu lực/có hiệu lực}»?"*.
- Actual đối tác ghi: câu xác nhận không đúng như kỳ vọng.

**Đối chiếu SRS v3.5**

- Đã tìm toàn bộ `srs-v3.5/` với các biến thể *"Bạn có chắc"* / *"Ban co chac"* → **0 kết quả**. Câu kỳ vọng trong phiếu **không tồn tại trong SRS v3.5**, nhiều khả năng đến từ tài liệu thiết kế khác của bên đối tác.
- Đặc tả mô tả đây là thao tác **gạt và cập nhật ngay**: *"Toggle hieu luc | toggle | Tat -> hieu_luc = 0, an khoi Cong. Bat -> hieu_luc = 1 | **toggle -> cap nhat** | luon hien thi"* — không nhắc hộp thoại xác nhận nào.
- **Đối chứng nội bộ quan trọng:** cùng màn hình, hành động Công khai / Hủy công khai thì đặc tả **CÓ** ghi rõ *"modal xac nhan"*. Việc ghi cho hành động kia mà không ghi cho hành động này là khác biệt **có chủ ý**, không phải sót.
- ⇒ Ứng dụng đang **cẩn thận hơn** đặc tả (có hộp thoại trong khi đặc tả không đòi).

**Citation**

- `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-13-tv-nhanh.md:533` (toggle hiệu lực → cập nhật ngay)
- `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-13-tv-nhanh.md:538` (hành động Công khai — có "modal xac nhan")

**Kết quả verify UI hiện tại**

- Verify lại ngày 27/07/2026 qua Chrome DevTools MCP, tài khoản UAT `cbnv_tw` — đo nguyên văn cả 2 chiều.
- Mở URL `https://18.143.165.120.nip.io/tv-nhanh/kho-cau-hoi`, gạt công tắc Hiệu lực trên dòng danh sách.
- Tắt hiệu lực: tiêu đề **"Đánh dấu hết hiệu lực"** · nội dung **"Câu hỏi sẽ ngừng hiển thị nhưng vẫn lưu trong hệ thống. Tiếp tục?"** · nút [Hủy] / [Đồng ý].
- Bật lại: tiêu đề **"Kích hoạt hiệu lực"** · nội dung **"Câu hỏi sẽ được kích hoạt lại và hiển thị cho người dùng. Tiếp tục?"** · nút [Hủy] / [Đồng ý].
- Cả 2 hộp thoại **không nhắc mã câu hỏi**.
- Evidence: `bug-reports/image/BUG-QLKCHTV_18-dialog-het-hieu-luc.png`

**Kết luận QA**

- `QLKCHTV_18`: **không phải bug** theo SRS v3.5. Hệ thống đang làm nhiều hơn đặc tả yêu cầu, không ít hơn.
- Câu chữ đối tác kỳ vọng không có trong SRS v3.5 ⇒ không có căn cứ để chấm hệ thống sai.
- Điểm duy nhất còn tranh chấp là **có nhắc mã câu hỏi hay không** — cũng không có dòng đặc tả nào quy định.

**Nội dung đề xuất BA phản hồi đối tác**

Đề nghị BA chốt 2 điểm:

1. Bật/tắt hiệu lực có bắt buộc hộp thoại xác nhận không, hay gạt là cập nhật ngay như `:533`?
2. Nếu có, câu chữ chuẩn là gì, và có phải nhắc mã câu hỏi trong câu xác nhận không?

- Verdict QA đề xuất: `Không phải bug theo SRS / Cần BA xác nhận`, không gửi Dev.
- Nếu BA chốt là **phải nhắc mã** thì mới mở bug giao diện mức Minor; đồng thời đề nghị bổ sung câu chữ chuẩn vào `:533` để lần sau không phải hỏi lại.

---

## QLKCHTV_13 — Xuất Excel khi không có dữ liệu: chặn kèm thông báo hay vẫn xuất file rỗng? *(BA-07 · Dạng A)*

**Bối cảnh testcase**

- Dòng Excel: row 7, mã TC `QLKCHTV_13`. **Phụ thuộc BA-02.**
- Nội dung kiểm tra: CB Nghiệp vụ Trung ương lọc cho ra 0 kết quả rồi bấm [Xuất Excel] trên màn Kho câu hỏi.
- Expected trong file UAT: hệ thống chặn kèm thông báo *"Không có dữ liệu để xuất"*.
- Actual đối tác ghi: vẫn xuất tệp; và tệp xuất ra *"chính là tệp cũ đã xuất ở QLKCHTV_12"*.

**Đối chiếu SRS v3.5**

- Đặc tả **im lặng** — đã tìm toàn bộ SRS v3.5, không có cụm *"Không có dữ liệu để xuất"* hay tương đương cho Kho câu hỏi. Đây là hệ quả trực tiếp của BA-02.
- Không có dòng nào quy định hành vi khi bộ lọc trả 0 kết quả mà người dùng bấm xuất.

**Citation**

- `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-13-tv-nhanh.md:528` (toolbar SCR-X2-01 — không khai nút Xuất Excel, nên cũng không có mô tả hành vi lỗi)
- `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/CHANGELOG-v3-to-v3.5.md:2443-2449` (mô tả duy nhất về Xuất Excel — chỉ nói giới hạn 10.000 dòng, không nói trường hợp 0 dòng)

**Kết quả verify UI hiện tại**

- Verify lại ngày 27/07/2026 qua Chrome DevTools MCP, tài khoản UAT `cbnv_tw`.
- Mở URL `https://18.143.165.120.nip.io/tv-nhanh/kho-cau-hoi`, đặt bộ lọc cho ra 0 kết quả rồi bấm [Xuất Excel].
- Lọc cho ra 0 kết quả (màn hiện *"Chưa có câu hỏi nào."*) → bấm [Xuất Excel] vẫn tải về tệp `.xlsx` **chỉ có dòng tiêu đề, 0 dòng dữ liệu** (6.655 byte). Không có khung thông báo nào. `POST /api/v1/kho-cau-hois/export` → 200.
- **Ý phụ của đối tác KHÔNG tái hiện:** đã đo 3 lần với 3 phạm vi khác nhau — không lọc (13 bản ghi) = 8.075 byte · lọc Lĩnh vực (6 bản ghi) = 7.433 byte · lọc rỗng (0 bản ghi) = 6.655 byte ⇒ máy chủ **có** áp dụng bộ lọc, không trả lại tệp cũ.
- Evidence: `reverify-audit/QLKCHTV_13/files/loc-rong-kho-cau-hoi-20260727.xlsx`

**Kết luận QA**

- Ý chính (`không có thông báo khi 0 dữ liệu`): **không chấm được** vì đặc tả im lặng ⇒ chờ BA.
- Ý phụ (`tệp xuất ra là tệp cũ`): **không tái hiện**, đã chứng minh bằng 3 phép đo kích thước tệp khác nhau. Đã đề nghị đối tác kiểm lại và gửi kèm kích thước từng tệp.

**Nội dung đề xuất BA phản hồi đối tác**

Đề nghị BA chốt: khi bộ lọc không có kết quả, hệ thống nên chặn kèm thông báo, hay vẫn xuất tệp rỗng như hiện tại?

- Nếu **chặn kèm thông báo** → mở bug giao diện mức Minor, và đề nghị chốt luôn câu chữ để đồng bộ với BA-17.
- Nếu **vẫn xuất tệp rỗng** → trả lời đối tác là hành vi đúng, và đề nghị BA ghi vào đặc tả để lần sau không bị mở lại.
- Verdict QA đề xuất: `Cần BA xác nhận` cho ý chính; ý phụ đề nghị BA phản hồi đối tác là **không tái hiện**, kèm 3 số đo kích thước tệp ở trên.

---

## QLKCHTV_02 (và QLKCHTV_04, QLKCHTV_14, QLKCHTV_16) — Mâu thuẫn nội bộ trong SRS về entity `KHO_CAU_HOI` *(BA-08 · Dạng B)*

**Bối cảnh testcase**

- Dòng Excel: row 2 `QLKCHTV_02`, row 4 `QLKCHTV_04`, row 8 `QLKCHTV_14`, row 9 `QLKCHTV_16`.
- Nội dung kiểm tra: CB Nghiệp vụ Trung ương làm việc với trạng thái và các trường của câu hỏi trong Kho câu hỏi.
- Expected trong file UAT: tùy case — danh sách trạng thái đúng, màn chi tiết đủ trường, cửa sổ Sửa đủ nút.
- **Ảnh hưởng trực tiếp tới cách dev fix 4 bug đang mở.**

**Kết quả verify UI hiện tại**

- Verify lại ngày 27/07/2026 qua Chrome DevTools MCP, tài khoản UAT `cbnv_tw` (và `cbpd_tw` cho phần duyệt/từ chối).
- Mở đúng màn danh sách Kho câu hỏi và thẻ "Chờ duyệt", URL là `https://18.143.165.120.nip.io/tv-nhanh/kho-cau-hoi` và `https://18.143.165.120.nip.io/tv-nhanh/kho-cau-hoi?tab=CHO_DUYET&page=1`; màn chi tiết là `https://18.143.165.120.nip.io/tv-nhanh/kho-cau-hoi/{id câu hỏi}`.
- Ô lọc "Trạng thái" trên màn Kho câu hỏi đổ ra **5 mục**: Bị từ chối / Chờ duyệt / Đã duyệt / Công khai / Hết hiệu lực.
- Phép đo ở `PDNDCHTV_04` cho thấy mục mang nhãn **"Bị từ chối" thực chất lọc theo `NHAP`** và chạy đúng ⇒ hệ thống **có** trạng thái `NHAP`, chỉ gán sai chữ hiển thị.
- Màn chi tiết **không** hiển thị người tạo.
- Evidence: `bug-reports/image/BUG-QLKCHTV_02-dropdown-trangthai.png` · `bug-reports/image/BUG-QLKCHTV_14-chi-tiet-co-tu-khoa.png`

**Điểm mâu thuẫn trong SRS v3.5**

1. **Mâu thuẫn 1 — trạng thái `NHAP` có hợp lệ hay không.** Bốn chỗ trong SRS coi `NHAP` là trạng thái hợp lệ, hai chỗ khác lại loại nó khỏi ràng buộc entity:

   | Vị trí trong SRS | Nội dung | Có `NHAP`? |
   |---|---|:-:|
   | `srs-fr-13-tv-nhanh.md:103` (FR-X.2-01 Inputs) | `NHAP / CHO_DUYET / DA_DUYET / CONG_KHAI / HET_HIEU_LUC` | ✅ |
   | `srs-fr-13-tv-nhanh.md:530` (SCR-X2-01 thanh lọc) | `NHAP/CHO_DUYET/DA_DUYET/CONG_KHAI/HET_HIEU_LUC` | ✅ |
   | `srs-fr-13-tv-nhanh.md:534` (cửa sổ nhập Q&A) | `[Huy] [Luu nhap] [Gui duyet]` | ✅ |
   | `srs-fr-13-tv-nhanh.md:536` (hành động Từ chối) | `modal ly do bat buoc + SET NHAP + TB CB NV` | ✅ |
   | `srs-fr-13-tv-nhanh.md:690` (ràng buộc entity) | `CHECK IN ('CHO_DUYET','DA_DUYET','CONG_KHAI','HET_HIEU_LUC')` | ❌ |
   | `srs-v3.5.md:2216` (bản sao entity trong file chính) | chỉ 3 giá trị | ❌ |

   Citation:
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-13-tv-nhanh.md:103`, `:530`, `:534`, `:536`
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-13-tv-nhanh.md:690`
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-v3.5.md:2216`

2. **Mâu thuẫn 2 — trường "người tạo".** Đặc tả yêu cầu màn chi tiết hiển thị *"nguoi tao"*, nhưng bảng thuộc tính entity `KHO_CAU_HOI` **không khai trường người tạo** nào.

   Citation:
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-13-tv-nhanh.md:545` (yêu cầu hiển thị người tạo)
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-13-tv-nhanh.md:683-698` (bảng thuộc tính entity — không có trường người tạo)

3. **Mâu thuẫn 3 — hai bản entity lệch nhau.** Bảng entity trong file chính **cũ hơn** bản trong file FR: thiếu trạng thái `CONG_KHAI` và thiếu cả 5 trường công khai (`cong_khai`, `anh_dai_dien`, `thoi_gian_dang_tai`, `mo_ta_cong_khai`, `file_dinh_kem_cong_khai`).

   Citation:
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-v3.5.md:2204-2222` (bản cũ)
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-13-tv-nhanh.md:683-698` (bản mới)

**Câu hỏi cần BA xác nhận**

Entity `KHO_CAU_HOI` phải hiểu theo bản nào, và 3 điểm lệch trên xử lý thế nào?

1. **Hướng 1 — bản trong `srs-fr-13-tv-nhanh.md` là chuẩn:** `NHAP` là trạng thái hợp lệ ⇒ sửa ràng buộc ở `:690` và `srs-v3.5.md:2216`; bổ sung trường người tạo vào entity; đồng bộ `srs-v3.5.md` theo file FR. Hệ thống hiện tại phù hợp hướng này, việc còn lại chỉ là **đổi nhãn hiển thị** "Bị từ chối" → đúng nghĩa `NHAP`.
2. **Hướng 2 — bản ràng buộc entity là chuẩn:** `NHAP` không hợp lệ ⇒ phải bỏ trạng thái này khỏi 4 chỗ đang khai, và khi đó hành động Từ chối ở `:536` phải chuyển sang trạng thái khác. Đây là thay đổi lớn về luồng nghiệp vụ.

**Đề xuất QA tạm thời**

- QA đang lấy `srs-fr-13-tv-nhanh.md:683-698` làm bản chuẩn khi tra cứu entity `KHO_CAU_HOI`.
- Tạm verdict cho 4 case: đã chấm theo bản FR, các bug liên quan đã log — nhưng **cách fix** phụ thuộc câu trả lời này.
- Nếu BA chọn hướng 1: `BUG-QLKCHTV_02` là **lỗi gán sai chữ hiển thị**, owner `Dev FE`, sửa nhãn là xong.
- Nếu BA chọn hướng 2: `BUG-QLKCHTV_02` đổi bản chất thành **lỗi luồng trạng thái**, owner `Dev BE`, phạm vi rộng hơn nhiều và phải rà lại cả hành động Từ chối.

---

## QLKCHTV_22 (và QLKCHTV_26) — Mâu thuẫn nội bộ trong SRS về máy trạng thái `SM-TVNHANH`: 4 hay 6 trạng thái? *(BA-09 · Dạng B)*

**Bối cảnh testcase**

- Dòng Excel: row 11 `QLKCHTV_22`, row 14 `QLKCHTV_26` — nhưng **ảnh hưởng toàn bộ Luồng 2**.
- Nội dung kiểm tra: CB Nghiệp vụ Trung ương xem danh sách và màn trả lời phiên Tư vấn nhanh.
- Expected trong file UAT: tùy case — đủ cột, đủ thẻ, trạng thái đúng.
- **Cùng loại lỗi ghép tài liệu với BA-02.**

**Kết quả verify UI hiện tại**

- Verify lại ngày 27/07/2026 qua Chrome DevTools MCP, tài khoản UAT `cbnv_tw`.
- Mở đúng màn danh sách Tư vấn nhanh và màn trả lời, URL là `https://18.143.165.120.nip.io/tv-nhanh/danh-sach` và `https://18.143.165.120.nip.io/tv-nhanh/{id phiên}` (phiên `TVN-20260727-0001`).
- Ô lọc "Trạng thái" đổ ra **6 nhãn**: `Mới` · `Đang tìm kiếm` · `Đã gợi ý` · `CB trả lời` · `Hoàn thành` · `Hết hạn`.
- Thanh tiến trình ở màn trả lời vẽ **5 bước**: Mới → Đang tìm kiếm → Đã gợi ý → CB trả lời → Hoàn thành.
- Danh sách có **4 thẻ**.
- Evidence: `bug-reports/image/BUG-TVN-danh-sach-cot-va-hanh-dong.png` · `bug-reports/image/BUG-TVN-man-tra-loi-cot-trai.png`

**Điểm mâu thuẫn trong SRS v3.5**

1. Theo **file FR đang hiệu lực**, Tư vấn nhanh chỉ có **4 trạng thái** và **3 thẻ**:
   - máy trạng thái `SM-TVNHANH` chỉ có 4 trạng thái: `MOI` / `CB_TRA_LOI` / `HOAN_THANH` / `HET_HAN`;
   - ràng buộc entity: `CHECK IN ('MOI','CB_TRA_LOI','HOAN_THANH','HET_HAN')`;
   - danh sách chỉ **3 thẻ**: `Tat ca / Cho xu ly / Hoan thanh`;
   - ô lọc chỉ **4 nhãn** trạng thái.

   Citation:
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-13-tv-nhanh.md:791-825` (máy trạng thái SM-TVNHANH)
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-13-tv-nhanh.md:713` (ràng buộc entity)
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-13-tv-nhanh.md:567` (3 thẻ)
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-13-tv-nhanh.md:579` (4 nhãn trạng thái)

2. Nhưng **CHANGELOG lại nhắc 2 trạng thái còn lại như thứ đã có từ v3** — mô tả luồng escalate có nhắc `DANG_TIM_KIEM` / `DA_GOI_Y`, là hai trạng thái **không tồn tại ở bất kỳ đâu** trong file FR đang hiệu lực.

   Citation:
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/CHANGELOG-v3-to-v3.5.md:2415-2432`

**Câu hỏi cần BA xác nhận**

1. Tập trạng thái chính thức của Tư vấn nhanh là **4 hay 6**? Nếu là 6 thì cần bổ sung `DANG_TIM_KIEM` / `DA_GOI_Y` vào `:713`, `:791-825` và `:579`.
2. Số thẻ chính thức của danh sách là **3 hay 4**?

**Đề xuất QA tạm thời**

- **Chưa chuyển dev bất kỳ kết luận nào của Luồng 2 phụ thuộc trạng thái** cho tới khi BA chốt source truth.
- Tạm verdict: các case Luồng 2 đã chấm theo phần **không** phụ thuộc tập trạng thái (cột thiếu, nút thiếu, dữ liệu trống); phần phụ thuộc trạng thái = `Cần BA xác nhận`.
- Nếu BA chọn 4 trạng thái: 2 trạng thái đang chạy trên hệ thống là **ngoài phạm vi**, owner `Dev BE` + `BA cập nhật expected của phiếu`.
- Nếu BA chọn 6 trạng thái: hệ thống đúng, **đặc tả phải sửa** ở 4 vị trí nêu trên.
- QA **không tự suy luận** hướng nào, vì chọn sai sẽ chấm sai hàng loạt case của cả luồng.

---

## QLKCHTV_22 — Cột "Ngày gửi" ở danh sách Tư vấn nhanh có cần hiển thị giờ phút không? *(BA-10 · Dạng A)*

**Bối cảnh testcase**

- Dòng Excel: row 11, mã TC `QLKCHTV_22` — ý gốc của phiếu.
- Nội dung kiểm tra: CB Nghiệp vụ Trung ương xem cột "Ngày gửi" trên danh sách Tư vấn nhanh.
- Expected trong file UAT: cột "Ngày gửi" hiển thị kèm giờ phút.
- Actual đối tác ghi: chỉ hiển thị ngày.

**Đối chiếu SRS v3.5**

- Quy ước giao diện UI-06 chỉ ghi *"Định dạng ngày: dd/MM/yyyy"*, **không nói tới giờ**.
- Phần mô tả màn danh sách Tư vấn nhanh (SCR-X2-03) **không có bảng định dạng đầu ra** nào.
- Nhóm khác **có** quy định rõ định dạng có giờ cho cột kiểu ngày-giờ: nhóm Hỏi đáp ghi *"Cột Ngày tạo | table-column | dd/mm/yyyy HH:mm"*.
- ⇒ Không có căn cứ trực tiếp trong nhóm X.2 để chấm là lỗi.

**Citation**

- `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-v3.5.md:576` (quy ước UI-06 — định dạng ngày)
- `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-02-hoi-dap.md:1043` (nhóm Hỏi đáp — định dạng có giờ)

**Kết quả verify UI hiện tại**

- Verify lại ngày 27/07/2026 qua Chrome DevTools MCP, tài khoản UAT `cbnv_tw`.
- Mở URL `https://18.143.165.120.nip.io/tv-nhanh/danh-sach` (màn danh sách Tư vấn nhanh).
- Cột "Ngày gửi" hiển thị `27/07/2026` (chỉ ngày), trong khi cột "Ngày cập nhật" **ngay bên cạnh** lại hiển thị `27/07/2026 11:54` (có giờ) — **không nhất quán trong cùng một bảng**.
- Dữ liệu máy chủ có đủ giờ phút giây (`"ngayGui": "2026-07-27T04:54:02.624Z"`) ⇒ phần giờ bị mất ở khâu hiển thị, không phải thiếu dữ liệu.
- Evidence: `bug-reports/image/BUG-TVN-danh-sach-cot-va-hanh-dong.png`

**Kết luận QA**

- `QLKCHTV_22` ý này: **chưa đủ căn cứ chấm là bug** — đặc tả nhóm X.2 không quy định định dạng cột.
- Nhưng điểm **không nhất quán giữa 2 cột cạnh nhau** trong cùng bảng là có thật, và đó là lý do QA không phản hồi đối tác là "hành vi đúng".

**Nội dung đề xuất BA phản hồi đối tác**

Đề nghị BA chốt: cột "Ngày gửi" (và các cột ngày khác của màn này) dùng `dd/MM/yyyy` hay `dd/MM/yyyy HH:mm`?

- **Nếu CÓ giờ** → gộp vào `BUG-QLKCHTV_22` (đang mở cho phần thiếu/thừa cột), mức Minor, owner `Dev FE`.
- **Nếu CHỈ ngày** → cần chốt luôn cột "Ngày cập nhật" đang hiện giờ có phải sửa cho nhất quán không.
- Verdict QA đề xuất: `Cần BA xác nhận`.

---

## QLKCHTV_31 — Chọn Q&A khác từ kho có phải hỏi xác nhận trước khi ghi đè nội dung cán bộ đang soạn không? *(BA-11 · Dạng A)*

**Bối cảnh testcase**

- Dòng Excel: row 15, mã TC `QLKCHTV_31`.
- Nội dung kiểm tra: CB Nghiệp vụ Trung ương đang soạn nội dung trả lời phiên Tư vấn nhanh, rồi bấm `[Chọn]` ở một kết quả tra cứu kho câu hỏi.
- Expected trong file UAT: hệ thống hỏi xác nhận, câu *"Bạn đang thay thế…"*.
- Actual đối tác ghi: ghi đè ngay, mất nội dung đang soạn.

**Đối chiếu SRS v3.5**

- Đặc tả chỉ mô tả thao tác này là **sao chép nội dung**: *"Bấm [Chọn] thì chép câu trả lời vào ô soạn"*; và ở phần quy trình: *"chọn một Q&A phù hợp -> copy cau_tra_loi vào ô soạn"*, cán bộ được chỉnh sửa trước khi gửi.
- Đã tìm toàn bộ `srs-v3.5/` cụm *"Bạn đang thay thế"* mà phiếu nêu → **0 kết quả**.
- Quy ước chung UI-08 **có** yêu cầu hỏi xác nhận, nhưng phạm vi là khi người dùng **rời/hủy** biểu mẫu đang nhập dở — **không phủ** tình huống ghi đè một ô ngay trong biểu mẫu.

**Citation**

- `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-13-tv-nhanh.md:572` (bấm [Chọn] → chép câu trả lời vào ô soạn)
- `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-13-tv-nhanh.md:201` (quy trình bước 6 — copy `cau_tra_loi`)
- `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-v3.5.md:577` (quy ước UI-08 — xác nhận khi rời/hủy biểu mẫu)

**Kết quả verify UI hiện tại**

- Verify lại ngày 27/07/2026 qua Chrome DevTools MCP, tài khoản UAT `cbnv_tw` — **đo 2 lần**.
- Mở URL `https://18.143.165.120.nip.io/tv-nhanh/{id phiên}` — màn trả lời phiên `TVN-20260727-0001`, mở từ `https://18.143.165.120.nip.io/tv-nhanh/danh-sach`.
- Khi ô "Nội dung trả lời" đã có nội dung do cán bộ tự soạn, bấm `[Chọn]` ở một kết quả tra cứu khác thì hệ thống **ghi đè ngay lập tức**, mất sạch phần tự soạn.
- Đo được **0 hộp thoại xác nhận, 0 thông báo, 0 lần gọi máy chủ**.
- Lần đo thứ 2 dùng nội dung **100% tự gõ** để loại trừ phản biện *"nội dung đó vốn lấy từ kho"*.
- Evidence: `reverify-audit/QLKCHTV_31/frames/` (khung hình đo 2 lần)

**Kết luận QA**

- `QLKCHTV_31`: **chưa đủ căn cứ chấm là bug** — đặc tả mô tả thao tác là sao chép, không đòi xác nhận; câu chữ đối tác kỳ vọng không tồn tại trong SRS v3.5.
- Nhưng **rủi ro mất công soạn là thật** và đo được, nên QA không phản hồi đối tác là "hành vi đúng, đóng case".

**Nội dung đề xuất BA phản hồi đối tác**

Đề nghị BA chốt: khi cán bộ đã soạn nội dung riêng mà bấm chọn Q&A khác từ kho, hệ thống có phải hỏi xác nhận trước khi ghi đè không? Nếu có thì câu chữ chuẩn là gì?

- **Đề nghị chốt cùng lúc với BA-13** — hai câu hỏi cùng nói về rủi ro mất công soạn: hiện hệ thống **vừa** không cảnh báo ghi đè, **vừa** không có lưu nháp.
- Verdict QA đề xuất: `Cần BA xác nhận`, chưa gửi Dev.

---

## QLKCHTV_32 — Bấm vào mã Q&A trong kết quả tra cứu có mở cửa sổ chi tiết không? *(BA-12 · Dạng A)*

**Bối cảnh testcase**

- Dòng Excel: row 16, mã TC `QLKCHTV_32`.
- Nội dung kiểm tra: CB Nghiệp vụ Trung ương bấm vào mã Q&A trong thẻ kết quả tra cứu kho câu hỏi (ở màn trả lời phiên Tư vấn nhanh).
- Expected trong file UAT: mở cửa sổ chi tiết câu hỏi, có nút "Đóng".
- Actual đối tác ghi: không mở được gì.

**Đối chiếu SRS v3.5**

- Đặc tả chỉ liệt kê **thành phần hiển thị** của mỗi kết quả: mã câu hỏi, câu hỏi in đậm, câu trả lời rút gọn, lĩnh vực, từ khóa, điểm phù hợp, nút Chọn. Hành vi duy nhất được mô tả là *"bấm [Chọn] thì chép câu trả lời vào ô soạn"*.
- **Không có** câu nào về cửa sổ chi tiết trong màn tra cứu, cũng không có nút "Đóng".
- Cửa sổ chi tiết câu hỏi chỉ được đặc tả ở màn **Kho câu hỏi** — là màn khác, không phải màn đang test.

**Citation**

- `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-13-tv-nhanh.md:572` (thành phần thẻ kết quả tra cứu + hành vi nút Chọn)
- `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-13-tv-nhanh.md:545` (cửa sổ chi tiết — thuộc màn Kho câu hỏi)

**Kết quả verify UI hiện tại**

- Verify lại ngày 27/07/2026 qua Chrome DevTools MCP, tài khoản UAT `cbnv_tw`.
- Mở URL `https://18.143.165.120.nip.io/tv-nhanh/{id phiên}` — màn trả lời phiên `TVN-20260727-0001`, vùng kết quả tra cứu kho câu hỏi.
- Bấm 1 lần và bấm đúp vào mã câu hỏi: **không** mở cửa sổ nào, địa chỉ trang không đổi, không có nút "Đóng" nào.
- Kiểm cấu trúc giao diện: mã hiển thị bằng **chữ thường, kiểu chữ phụ, màu xám mờ**; con trỏ giữ dạng chữ (không phải dạng bàn tay); **không gắn hàm xử lý bấm** ⇒ không phải liên kết, tức là chưa từng được dựng chứ không phải bị lỗi.
- Evidence: `bug-reports/image/BUG-TVN-ket-qua-tra-cuu-ma-khong-bam-duoc.png` · `reverify-audit/QLKCHTV_32/`

**Kết luận QA**

- `QLKCHTV_32`: **không đủ căn cứ chấm là bug** — đặc tả không quy định hành vi bấm vào mã trong thẻ kết quả.
- Đáng chú ý: phần lớn thông tin phiếu muốn xem thì thẻ kết quả **đã hiển thị sẵn** (mã, câu hỏi, câu trả lời rút gọn, lĩnh vực, nguồn, điểm phù hợp). Thứ thực sự còn thiếu là **xem được câu trả lời đầy đủ**, vì trên thẻ nội dung bị cắt bớt.

**Nội dung đề xuất BA phản hồi đối tác**

Đề nghị BA chốt: bấm vào mã Q&A trong kết quả tra cứu có phải mở cửa sổ chi tiết không? Nếu có thì cửa sổ gồm những trường nào và có cần nút "Đóng" riêng không?

- QA gợi ý BA cân nhắc phương án nhẹ hơn: chỉ cần cho **mở rộng phần câu trả lời ngay trên thẻ** là đã giải quyết đúng nhu cầu thật (xem câu trả lời đầy đủ) mà không phải dựng thêm cửa sổ.
- Verdict QA đề xuất: `Cần BA xác nhận`.

---

## QLKCHTV_36 — Màn trả lời Tư vấn nhanh có cần nút [Lưu nháp] không? *(BA-13 · Dạng A)*

**Bối cảnh testcase**

- Dòng Excel: row 18, mã TC `QLKCHTV_36`.
- Nội dung kiểm tra: CB Nghiệp vụ Trung ương soạn nội dung trả lời rồi tìm nút [Lưu nháp] trên màn trả lời phiên Tư vấn nhanh.
- Expected trong file UAT: có nút [Lưu nháp], lưu lại nội dung đang soạn.
- Actual đối tác ghi: không có nút này.

**Đối chiếu SRS v3.5**

> Ở case này đặc tả **nói ngược lại** kỳ vọng của phiếu, không chỉ im lặng.

- Đặc tả màn trả lời chỉ khai **hai** thao tác: `[Gui tra loi]` và nút phụ "Đẩy sang Nhóm II". Không có nút nào cho bản nháp.
- FR-X.2-02 không có bước xử lý, đầu ra, trạng thái hay mã lỗi nào cho bản nháp.
- Đặc tả còn ghi rõ hệ thống *"chỉ lưu `noi_dung_tra_loi` cuối cùng"* cùng thông tin CB xử lý / thời điểm trả lời ⇒ chủ trương là **chỉ lưu bản cuối**.
- Cụm *"Luu nhap"* trong file FR Tư vấn nhanh chỉ xuất hiện **1 lần**, và đó là nút của màn **Kho câu hỏi**, không phải màn Tư vấn nhanh.
- **Đối chứng cho thấy đây là lựa chọn thiết kế, không phải sót:** nhóm Hỏi đáp **có** đặc tả lưu nháp rất chi tiết — *"Nút Lưu nháp + Auto-save | Auto-save mỗi 60 giây nếu có thay đổi (silent save, không toast — chỉ đổi indicator 'Đã lưu lúc {HH:mm:ss}')"*. Viết kỹ cho Hỏi đáp mà không viết cho Tư vấn nhanh phù hợp với tính chất luồng trả lời ngắn dựa trên kho câu hỏi có sẵn.

**Citation**

- `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-13-tv-nhanh.md:572` (chỉ 2 thao tác trên màn trả lời)
- `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-13-tv-nhanh.md:164-238` (FR-X.2-02 — không có bước nào cho bản nháp)
- `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-13-tv-nhanh.md:215` ("chỉ lưu `noi_dung_tra_loi` cuối cùng")
- `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-13-tv-nhanh.md:534` (nút Lưu nháp — thuộc màn Kho câu hỏi)
- `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-02-hoi-dap.md:1127` (nhóm Hỏi đáp — có Lưu nháp + tự lưu)

**Kết quả verify UI hiện tại**

- Verify lại ngày 27/07/2026 qua Chrome DevTools MCP, tài khoản UAT `cbnv_tw`.
- Mở URL `https://18.143.165.120.nip.io/tv-nhanh/{id phiên}` — màn trả lời phiên `TVN-20260727-0001`.
- Màn trả lời **không có** nút [Lưu nháp] — đo ở cả 2 tình huống: ô nội dung trống và ô đã có nội dung.
- Kiểm thêm tầng máy chủ: nhóm tư vấn nhanh có **10 đường dẫn**, **không đường nào** cho bản nháp ⇒ chức năng chưa tồn tại ở **cả hai tầng**, không phải nút bị ẩn theo quyền.
- Evidence: `bug-reports/image/BUG-TVN-man-tra-loi-cot-trai.png`

**Kết luận QA**

- `QLKCHTV_36`: **không phải bug** theo SRS v3.5 — đặc tả không khai chức năng này, và còn có câu chủ trương chỉ lưu bản cuối.
- Nhưng **rủi ro thực tế là có**: cán bộ soạn dở mà rời màn thì mất toàn bộ nội dung, và bấm chọn Q&A khác thì bị ghi đè không hỏi (BA-11).

**Nội dung đề xuất BA phản hồi đối tác**

Đề nghị BA chốt: màn trả lời Tư vấn nhanh có cần [Lưu nháp] không?

- **Đề nghị chốt cùng lúc với BA-11.** Nếu BA quyết **không** thêm Lưu nháp thì tối thiểu nên có cảnh báo trước khi mất nội dung đang soạn — hiện hệ thống **vừa** không lưu nháp, **vừa** không cảnh báo ghi đè, hai lỗ hổng cộng lại mới thành rủi ro thật.
- Verdict QA đề xuất: `Không phải bug theo SRS / Cần BA xác nhận`, chưa gửi Dev.

---

## QLKCHTV_26 — Khối "Thông tin DN" ở cột trái màn trả lời gồm những trường bắt buộc nào? *(BA-14 · Dạng A)*

**Bối cảnh testcase**

- Dòng Excel: row 14, mã TC `QLKCHTV_26` — **phần ý (2)** của phiếu.
- Nội dung kiểm tra: CB Nghiệp vụ Trung ương xem khối "Thông tin Doanh nghiệp" ở cột trái màn trả lời phiên Tư vấn nhanh.
- Expected trong file UAT: khối này có tên DN, mã số thuế, thư điện tử liên hệ, người gửi câu hỏi.
- Actual đối tác ghi: thiếu thông tin.

**Đối chiếu SRS v3.5**

- Đặc tả chỉ ghi chung một cụm *"Thong tin DN"* cho khối này, **không liệt kê trường cụ thể** ⇒ không có căn cứ để chấm thiếu trường nào.
- Vì vậy phải tách phiếu thành 2 phần: phần giao diện **tự công bố** trường rồi bỏ trống (chấm được), và phần trường phiếu **mong thêm** (phải hỏi BA).

**Citation**

- `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-13-tv-nhanh.md:571` (khối "Thong tin DN" — mô tả chung, không liệt kê trường)

**Kết quả verify UI hiện tại**

- Verify lại ngày 27/07/2026 qua Chrome DevTools MCP, tài khoản UAT `cbnv_tw`.
- Mở URL `https://18.143.165.120.nip.io/tv-nhanh/{id phiên}` — màn trả lời phiên `TVN-20260727-0001`, khối "Thông tin Doanh nghiệp" ở cột trái.
- Khối "Thông tin Doanh nghiệp" chỉ có **2 dòng**: `Tên DN` (có giá trị) và `MST:` (**bỏ trống**). Không có thư điện tử liên hệ, không có người gửi câu hỏi.
- Evidence: `bug-reports/image/BUG-TVN-man-tra-loi-cot-trai.png`

**Kết luận QA**

- **Phần đã chấm là lỗi, không cần BA:** nhãn "MST" đã được dựng trên giao diện nhưng máy chủ không trả `maSoThue` → đã log `BUG-QLKCHTV_26B` trong [bug-report-UAT-tuan-4.md](bug-reports/bug-report-UAT-tuan-4.md). Đây là lỗi rõ vì giao diện **tự công bố** trường rồi bỏ trống.
- **Phần cần BA chốt:** hai mục *"thư điện tử liên hệ"* và *"người gửi câu hỏi"* mà phiếu kỳ vọng — đặc tả không liệt kê nên QA không chấm.

**Nội dung đề xuất BA phản hồi đối tác**

Đề nghị BA chốt: khối "Thông tin DN" ở cột trái màn trả lời phải hiển thị những trường nào (tên DN / mã số thuế / thư điện tử / điện thoại / người gửi câu hỏi / …)?

- **Ghi chú kỹ thuật gửi kèm:** dữ liệu thư điện tử **có sẵn** ở `GET /api/v1/doanh-nghieps`, chỉ không được trả về trong khối `doanhNghiep` của `GET /api/v1/tu-van-nhanhs/{id}`. Nếu BA chốt là bắt buộc thì dev bổ sung **cùng lúc** với `maSoThue` ở `BUG-QLKCHTV_26B` — một lần sửa cho cả hai.
- Verdict QA đề xuất: `Open, BA confirm` (ý MST là bug; ý thư điện tử / người gửi chờ BA).

---

## PDNDCHTV_07 — Duyệt hàng loạt có phải gửi thông báo cho từng cán bộ tạo câu hỏi không? *(BA-15 · Dạng A)*

**Bối cảnh testcase**

- Dòng Excel: row 22, mã TC `PDNDCHTV_07`.
- Nội dung kiểm tra: CB Phê duyệt Trung ương dùng chức năng duyệt hàng loạt cho nhiều câu hỏi cùng lúc.
- Expected trong file UAT: cả lô chuyển "Đã duyệt" **và** cán bộ tạo nhận được thông báo.
- Actual đối tác ghi: cán bộ tạo không nhận thông báo.

**Đối chiếu SRS v3.5**

- Đặc tả định nghĩa **hành động Duyệt** gồm 3 vế: đặt trạng thái `DA_DUYET`, bật hiệu lực, **và thông báo cho cán bộ nghiệp vụ**.
- Đặc tả **nút Duyệt hàng loạt** thì chỉ ghi *"[Duyet hang loat] -> modal xac nhan. Khong tu choi hang loat"* — nói về hành vi của nút, **không nhắc lại** nghĩa vụ thông báo và cũng **không định nghĩa lại** hành động Duyệt.
- Duyệt hàng loạt tạo ra **đúng cùng một chuyển trạng thái** `CHO_DUYET → DA_DUYET` như duyệt đơn lẻ, chỉ khác số lượng bản ghi ⇒ QA áp dụng cùng nghĩa vụ thông báo.
- Đã rà toàn bộ quy trình xử lý FR-X.2-01 (7 bước): **không có câu nào miễn trừ** thông báo cho thao tác hàng loạt.

**Citation**

- `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-13-tv-nhanh.md:536` (hành động Duyệt — 3 vế, có "TB CB NV")
- `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-13-tv-nhanh.md:537` (nút Duyệt hàng loạt — không nhắc thông báo)
- `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-13-tv-nhanh.md:95-163` (FR-X.2-01 — không có câu miễn trừ)

**Kết quả verify UI hiện tại**

- Verify lại ngày 27/07/2026 qua Chrome DevTools MCP, tài khoản UAT `cbpd_tw` (thao tác duyệt) và `cbnv_tw` (kiểm hộp thông báo bên nhận).
- Mở URL `https://18.143.165.120.nip.io/tv-nhanh/kho-cau-hoi?tab=CHO_DUYET&page=1` (thẻ "Chờ duyệt" của màn Kho câu hỏi) để tích chọn rồi duyệt hàng loạt.
- Duyệt hàng loạt 2 câu hỏi **chạy đúng về dữ liệu**: cả 2 sang "Đã duyệt", có hiệu lực, 1 lần gọi xử lý cho cả lô.
- Nhưng cán bộ tạo nhận **0 thông báo** — đếm hộp thông báo trước/sau: **253 → 253**, chênh lệch bằng 0.
- Evidence: `bug-reports/image/BUG-PD-07-duyet-hang-loat-truoc-khi-bam.png` · `bug-reports/image/BUG-PD-THONG-BAO-can-bo-tao-khong-nhan.png` · `reverify-audit/PDNDCHTV_07/`

**Kết luận QA**

- QA **đã chấm là lỗi** → `BUG-PD-THONG-BAO` trong [bug-report-UAT-tuan-4.md](bug-reports/bug-report-UAT-tuan-4.md), vì hành động Duyệt ở `:536` ghi thẳng nghĩa vụ thông báo và thao tác hàng loạt không được miễn trừ ở đâu cả.
- Nêu rõ căn cứ ở trên để BA **phản biện được** nếu chủ trương thực tế khác.

**Nội dung đề xuất BA phản hồi đối tác**

Đề nghị BA chốt: khi cán bộ phê duyệt dùng duyệt hàng loạt, hệ thống có phải gửi thông báo cho **từng** cán bộ đã tạo câu hỏi trong lô không?

- Nếu **có** (QA đang hiểu theo hướng này): dev sửa **một lần ở tầng chung** cho cả duyệt đơn lẻ, từ chối và duyệt hàng loạt.
- Nếu **không** — tức duyệt hàng loạt được phép im lặng: QA sẽ tách `PDNDCHTV_07` ra khỏi `BUG-PD-THONG-BAO` và điều chỉnh kết luận case này. Khi đó đề nghị BA bổ sung câu miễn trừ vào `:537` để lần sau không phải hỏi lại.
- **Ghi chú:** dù BA chốt hướng nào thì phần **duyệt đơn lẻ** và **từ chối** (`PDNDCHTV_01`, `PDNDCHTV_04`) vẫn là lỗi rõ, vì `:536` ghi thẳng "TB CB NV" cho cả hai. BA-15 chỉ ảnh hưởng phạm vi của thao tác hàng loạt.
- Verdict QA đề xuất: giữ `Open`, đồng thời gửi BA để chốt phạm vi.

---

## QLCKCHTV_02 — Khi "Mô tả công khai" để trống, hệ thống có được tự điền bằng nội dung câu hỏi không? *(BA-16 · Dạng A)*

**Bối cảnh testcase**

- Dòng Excel: row 23, mã TC `QLCKCHTV_02`.
- Nội dung kiểm tra: CB Nghiệp vụ Trung ương công khai một câu hỏi ra Cổng Pháp luật quốc gia, không nhập gì vào ô "Mô tả công khai".
- Expected trong file UAT: công khai thành công với các thông tin đã khai.
- Actual đối tác ghi: nội dung công khai không như mong đợi.

**Đối chiếu SRS v3.5**

- Đặc tả mô tả `mo_ta_cong_khai` là *"mô tả hiển thị trên Cổng PLQG, **khác `cau_hoi`/`cau_tra_loi` nội bộ**"*. Cách diễn đạt này cho thấy đây là **trường riêng, có mục đích riêng**, không phải bản sao của nội dung câu hỏi.
- Đặc tả **không nêu** quy tắc tự điền mặc định khi trường này để trống.

**Citation**

- `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-13-tv-nhanh.md:106` (định nghĩa `mo_ta_cong_khai` — "khác `cau_hoi`/`cau_tra_loi` nội bộ")

**Kết quả verify UI hiện tại**

- Verify lại ngày 27/07/2026 qua Chrome DevTools MCP, tài khoản UAT `cbnv_tw`, có kiểm chéo bằng `cbpd_tw`.
- Mở URL `https://18.143.165.120.nip.io/tv-nhanh/kho-cau-hoi/{id câu hỏi}` rồi bấm [Công khai] để mở hộp thoại xác nhận.
- Ở hộp thoại xác nhận Công khai, nếu bản ghi chưa có mô tả công khai thì ô "Mô tả công khai" **tự điền sẵn nguyên văn nội dung câu hỏi**. Cán bộ bấm [Công khai] mà không sửa gì thì hệ thống **lưu bản sao nội dung câu hỏi vào trường mô tả công khai**.
- Đo cụ thể: `QA-20260727-0001` trước khi công khai có `moTaCongKhai = null`; sau khi công khai (QA **không gõ gì** vào ô đó) trường này thành đúng nguyên văn câu hỏi *"QA tuần 4: Doanh nghiệp nhỏ và vừa cần chuẩn bị hồ sơ gì để được hỗ trợ pháp lý về thuế?"*.
- **Đã kiểm để không báo nhầm:** nếu bản ghi **đã có** mô tả công khai thì hộp thoại hiển thị đúng giá trị đang lưu, **không ghi đè** (kiểm trên `QA-20260727-0005`) ⇒ đây chỉ là quy tắc điền mặc định khi trống, **không phải lỗi mất dữ liệu**.
- Evidence: `bug-reports/image/BUG-CK-modal-cong-khai-thieu-anh-va-tep.png`

**Kết luận QA**

- `QLCKCHTV_02` ý này: **không chấm là lỗi** vì chưa đủ căn cứ — đặc tả không cấm điền mặc định.
- Nhưng cần BA xác nhận vì nó quyết định **nội dung thật sự hiển thị ra Cổng Pháp luật quốc gia** — tức ảnh hưởng người dùng ngoài hệ thống, không chỉ nội bộ.

**Nội dung đề xuất BA phản hồi đối tác**

Đề nghị BA chốt: khi cán bộ để trống "Mô tả công khai", hệ thống nên xử lý theo hướng nào?

- (a) Tự điền bằng nội dung câu hỏi như hiện tại.
- (b) Để trống và Cổng PLQG tự xử lý phần hiển thị.
- (c) Bắt buộc cán bộ nhập trước khi cho công khai.
- Verdict QA đề xuất: `Cần BA xác nhận` cho ý này (các ý khác của cùng case đã chấm riêng).

---

## TKCHTV_02 — Khi tìm kiếm/lọc không khớp, màn danh sách Kho câu hỏi và Tư vấn nhanh phải hiển thị câu gì? *(BA-17 · Dạng A)*

**Bối cảnh testcase**

- Dòng Excel: row 25, mã TC `TKCHTV_02`.
- Nội dung kiểm tra: CB Nghiệp vụ Trung ương tìm một chuỗi không tồn tại trên màn danh sách Kho câu hỏi và màn danh sách Tư vấn nhanh.
- Expected trong file UAT: hiển thị *"Không tìm thấy câu hỏi phù hợp"* / *"Không tìm thấy phiên tư vấn phù hợp"*.
- Actual đối tác ghi: câu thông báo không đúng.

**Đối chiếu SRS v3.5**

- Đặc tả nhóm X.2 **có** định nghĩa câu cho tình huống tìm không ra: `INF-TVN-TK-01` = *"Không tìm thấy câu hỏi phù hợp"*. Nhưng cả hai chỗ khai mã này đều nằm ở **FR-X.2-02** (cán bộ tra cứu kho ngay trong màn trả lời phiên) và **FR-X.2-04** (doanh nghiệp tự tra trên chuyên trang) — **không phải** màn danh sách quản trị mà đối tác đang test.
- Phần mô tả **màn danh sách** thì **không** quy định câu thông báo khi rỗng.
- Nhóm Hỏi đáp đã có quy ước rất rõ cho đúng tình huống này: tách **5 biến thể**, biến thể (1) *"Chưa có hỏi đáp nào"* cho **không có dữ liệu**, biến thể (4) *"Không tìm thấy hỏi đáp phù hợp với bộ lọc. [Xóa bộ lọc]"* cho **lọc không khớp**.
- Câu đối tác mong cho Tư vấn nhanh (*"Không tìm thấy phiên tư vấn phù hợp"*) **không xuất hiện ở bất kỳ đâu trong SRS v3.5** — là chữ đối tác tự đặt.

**Citation**

- `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-13-tv-nhanh.md:225` (`INF-TVN-TK-01` trong FR-X.2-02)
- `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-13-tv-nhanh.md:349` (`INF-TVN-TK-01` trong FR-X.2-04)
- `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-13-tv-nhanh.md:530` (màn danh sách Kho câu hỏi — không quy định câu rỗng)
- `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-13-tv-nhanh.md:568` (màn danh sách Tư vấn nhanh — không quy định câu rỗng)
- `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-02-hoi-dap.md:1047` (nhóm Hỏi đáp — 5 biến thể câu thông báo)

**Kết quả verify UI hiện tại**

- Verify lại ngày 27/07/2026 qua Chrome DevTools MCP, tài khoản UAT `cbnv_tw`.
- Mở URL `https://18.143.165.120.nip.io/tv-nhanh/kho-cau-hoi` và `https://18.143.165.120.nip.io/tv-nhanh/danh-sach`, tìm một chuỗi không tồn tại trên cả hai màn.
- Cả hai màn đều đang dùng câu dành cho trường hợp *chưa có dữ liệu*, **kể cả khi kho đang có dữ liệu**:

  | Màn | Dữ liệu đang có | Tìm chuỗi vô nghĩa | Câu hiển thị |
  |---|:-:|---|---|
  | Kho câu hỏi | 14 câu hỏi | `abcdxyzqwerty` | *"Chưa có câu hỏi nào."* |
  | Tư vấn nhanh | 4 phiên | `abcdxyzqwerty` | *"Không có phiên tư vấn nhanh nào."* |

- Evidence: `bug-reports/image/BUG-TK-tim-khong-ket-qua-bao-chua-co-cau-hoi-nao.png` · `bug-reports/image/BUG-TK-tv-nhanh-tim-dung-ma-phien-ra-0.png`

**Kết luận QA**

- Hiện tượng đối tác nêu **tái hiện đúng**, nhưng câu chữ chuẩn cho màn danh sách thì đặc tả nhóm X.2 **không quy định** ⇒ phần câu chữ phải chờ BA.
- **Phần dữ liệu đã đúng** — hệ thống trả về 0 dòng, không còn hiện tượng "hiển thị toàn bộ bản ghi". Đây thuần là câu chữ.

**Nội dung đề xuất BA phản hồi đối tác**

Đề nghị BA chốt: hai màn danh sách này áp quy ước nào?

- (a) Áp quy ước 5 biến thể của nhóm Hỏi đáp (`srs-fr-02-hoi-dap.md:1047`) — phân biệt "chưa có dữ liệu" với "lọc không khớp", kèm gợi ý xóa bộ lọc. **QA nghiêng phương án này** vì nhất quán toàn hệ thống.
- (b) Dùng lại `INF-TVN-TK-01` cho cả màn danh sách, và bổ sung một mã tương ứng cho Tư vấn nhanh.
- (c) Giữ nguyên như hiện tại — khi đó đề nghị BA ghi vào đặc tả để lần sau không bị chấm là lỗi.
- **Đề nghị chốt cùng lúc với BA-07 và BA-18** — cả ba đều là câu chữ trạng thái rỗng / bộ lọc của cùng nhóm màn.
- Verdict QA đề xuất: `Open, BA confirm`.

---

## TKCHTV_03 — Màn Kho câu hỏi có bắt buộc phải có nút [Xóa bộ lọc] như màn Tư vấn nhanh không? *(BA-18 · Dạng A)*

**Bối cảnh testcase**

- Dòng Excel: row 26, mã TC `TKCHTV_03`.
- Nội dung kiểm tra: CB Nghiệp vụ Trung ương đặt bộ lọc trên màn Kho câu hỏi rồi tìm cách đưa danh sách về mặc định.
- Expected trong file UAT: có nút [Xóa bộ lọc], bấm là đặt lại toàn bộ tiêu chí.
- Actual đối tác ghi: không có nút này.

**Đối chiếu SRS v3.5**

- Đặc tả mô tả thanh lọc **cả hai màn** nhưng **không dòng nào** nhắc nút xóa bộ lọc ⇒ không có căn cứ trực tiếp trong nhóm X.2.
- Ngược lại, nút này là **quy ước lặp lại ở 7 nhóm khác** của cùng SRS v3.5 (Hỏi đáp, Biểu mẫu, Doanh nghiệp, Chuyên gia/TVV, Vụ việc, Chi trả, Đánh giá).
- Bản thân hệ thống cũng **đã dựng** nút này ở màn Tư vấn nhanh ⇒ thành phần có sẵn, chỉ là màn Kho câu hỏi không gắn.

**Citation**

- `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-13-tv-nhanh.md:530` (thanh lọc Kho câu hỏi — không nhắc nút xóa bộ lọc)
- `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-13-tv-nhanh.md:568` (thanh lọc Tư vấn nhanh — không nhắc nút xóa bộ lọc)
- `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-02-hoi-dap.md:1033` · `srs-fr-09-bieu-mau.md:622` · `srs-fr-07-doanh-nghiep.md:434` · `srs-fr-04-chuyen-gia-tvv.md:1439` · `srs-fr-05-vu-viec.md:1646` · `srs-fr-06-chi-tra.md:1050` · `srs-fr-08-danh-gia.md:817` (7 nhóm khác đều có nút [Xóa bộ lọc])

**Kết quả verify UI hiện tại**

- Verify lại ngày 27/07/2026 qua Chrome DevTools MCP, tài khoản UAT `cbnv_tw`.
- Mở URL `https://18.143.165.120.nip.io/tv-nhanh/kho-cau-hoi` và `https://18.143.165.120.nip.io/tv-nhanh/danh-sach` để đối chiếu thanh lọc hai màn.

  | Màn | Số tiêu chí lọc | Nút [Xóa bộ lọc] | [Làm mới] có đặt lại bộ lọc? |
  |---|:-:|:-:|:-:|
  | Kho câu hỏi | 6 (từ khóa, Lĩnh vực, Nguồn, Trạng thái, Từ ngày, Đến ngày) | **không có** | **không** |
  | Tư vấn nhanh | 4 (từ khóa, Trạng thái, Từ ngày, Đến ngày) | **có**, chạy đúng | — |

- Đã thử [Làm mới] trên Kho câu hỏi: trước khi bấm ô tìm kiếm là `lao động` và bảng còn 1/14 dòng; sau khi bấm **vẫn y nguyên** ⇒ hiện **không có thao tác nào** đưa danh sách về mặc định trong một lần bấm.
- Evidence: `bug-reports/image/BUG-TK-kho-cau-hoi-loc-dung-1-ket-qua.png`

**Kết luận QA**

- Hiện tượng đối tác nêu **tái hiện đúng**, nhưng đặc tả nhóm X.2 không quy định nút này nên QA không tự chấm.
- QA nghiêng hướng "phải có", vì 7 nhóm khác đều có và **màn anh em cùng nhóm cũng có**.

**Nội dung đề xuất BA phản hồi đối tác**

Đề nghị BA chốt: thanh lọc màn danh sách trong nhóm X.2 có bắt buộc kèm nút [Xóa bộ lọc] không?

- Nếu **có** (QA đang hiểu theo hướng này): dev bổ sung nút vào Kho câu hỏi, hành vi giống Tư vấn nhanh.
- Nếu **không**: QA hạ `TKCHTV_03` xuống không phải lỗi. Khi đó đề nghị BA ghi rõ ngoại lệ vào `:530` để đối tác không mở lại case này ở vòng sau.
- **Đề nghị BA xem cùng lúc với BA-17** — hai thứ này đi với nhau: quy ước ở `srs-fr-02-hoi-dap.md:1047` đặt nút [Xóa bộ lọc] **ngay trong câu thông báo** khi lọc không khớp, tức giải quyết một lượt cả hai vấn đề.
- Verdict QA đề xuất: `Open, BA confirm`.

---

## KHTHCTHTPLDN_07 — Tệp Excel xuất từ màn Chương trình HTPLDN đặt tên theo quy ước nào? *(BA-19 · Dạng A)*

**Bối cảnh testcase**

- Dòng Excel: row 29, mã TC `KHTHCTHTPLDN_07`.
- Nội dung kiểm tra: CB Nghiệp vụ Trung ương bấm [Xuất Excel] trên màn Chương trình HTPLDN.
- Expected trong file UAT: tải về tệp tên `DanhSachChuongTrinh_{YYYYMMDD_HHmm}.xlsx`.
- Actual đối tác ghi: tên tệp không đúng quy ước.

**Đối chiếu SRS v3.5**

- Đặc tả mô tả **đầy đủ** quy trình xuất Excel của nhóm này (kiểm quyền → truy vấn theo bộ lọc → giới hạn 10.000 dòng → tạo tệp với 10 cột → trả tệp) nhưng **không có dòng nào quy định tên tệp**. Đã rà toàn file, không có chuỗi `DanhSach` hay mẫu tên tệp nào.
- Quy ước mà đối tác mong đợi thì **có thật ở nhóm khác**: nhóm Hỏi đáp ghi *"| 3 | Trả về file tải về. Tên file: `HoiDap_{YYYYMMDD_HHmm}.xlsx` |"*. Đây là chỗ **duy nhất** trong SRS v3.5 có mẫu tên tệp dạng này.

**Citation**

- `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-15-ct-htpldn.md:387-410` (quy trình xuất Excel — không quy định tên tệp)
- `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-15-ct-htpldn.md:396` (bảng 10 cột bắt buộc của tệp xuất)
- `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-02-hoi-dap.md:151` (nhóm Hỏi đáp — mẫu tên tệp `HoiDap_{YYYYMMDD_HHmm}.xlsx`)

**Kết quả verify UI hiện tại**

- Verify lại ngày 27/07/2026 qua Chrome DevTools MCP, tài khoản UAT `cbnv_tw`, có kiểm chéo `cbpd_tw`.
- Mở URL `https://18.143.165.120.nip.io/ct-htpldn/danh-sach` rồi bấm [Xuất Excel].
- Bấm [Xuất Excel] → tải về tệp **`ct-htpldn-2026-07-27.xlsx`**. Tên này vẫn nhận diện được nội dung và ngày xuất, chỉ khác cách viết và **thiếu phần giờ phút** — nếu cán bộ xuất 2 lần trong ngày thì tệp thứ hai bị trình duyệt thêm hậu tố `(1)`.
- **QA đã mở tệp ra đọc nội dung** chứ không chỉ kiểm tệp tải được: **đủ 10 cột bắt buộc**, không thiếu cột nào; nhưng **hai cột thời gian bị lệch 1 ngày** so với màn hình (chương trình bắt đầu 01/01/2026 vào tệp thành 31/12/2025).
- Evidence: `bug-reports/image/BUG-CT-xuat-excel-ten-tep-va-ngay-lech.png` · `bug-reports/image/BUG-CT-xuat-excel-noi-dung-tep.log.txt`

**Kết luận QA**

- Ý tên tệp: **không đủ căn cứ chấm là bug** — đặc tả nhóm XI không quy định tên tệp.
- **Lỗi lệch ngày nặng hơn chuyện tên tệp** và QA đã tách ra thành lỗi riêng `BUG-CT-XUAT-EXCEL-SAI-NGAY` (dòng `KHTHCTHTPLDN_OOS_06` trên sheet), đề nghị BA/dev ưu tiên xử lý phần đó trước.

**Nội dung đề xuất BA phản hồi đối tác**

Đề nghị BA chốt: tên tệp Excel xuất ra ở nhóm Chương trình HTPLDN theo hướng nào?

- (a) Áp quy ước của `srs-fr-02-hoi-dap.md:151`, đổi thành `DanhSachChuongTrinh_{YYYYMMDD_HHmm}.xlsx` — thống nhất toàn hệ thống, có giờ phút nên không trùng tên trong ngày. **QA nghiêng phương án này.**
- (b) Giữ nguyên `ct-htpldn-{yyyy-mm-dd}.xlsx` — khi đó đề nghị BA ghi mẫu tên này vào `:396` để lần sau không bị chấm là lỗi.
- Verdict QA đề xuất: `Cần BA xác nhận` cho ý tên tệp; ý lệch ngày đã `Open` ở dòng riêng.

---

## KHTHCTHTPLDN_12 — Bố cục đầu trang "Chi tiết chương trình" lấy căn cứ ở đâu? Và nhãn trạng thái `CHO_PHE_DUYET` hiển thị dạng nào? *(BA-20 · Dạng A — riêng câu hỏi (c) về nhãn trạng thái mang tính dạng B: SRS ghi 2 dạng)*

**Bối cảnh testcase**

- Dòng Excel: row 31, mã TC `KHTHCTHTPLDN_12`.
- Nội dung kiểm tra: CB Nghiệp vụ Trung ương mở màn Chi tiết chương trình và đối chiếu bố cục đầu trang.
- Expected trong file UAT: thanh điều hướng kèm mã chương trình; tiêu đề dạng `{Mã chương trình}: {Tên chương trình}`; thanh tiến trình 6 bước có dấu tích xanh / bước nổi bật / bước mờ; khối thông tin nhanh (Ngân sách, Thời gian, Đơn vị, Đối tượng).
- Actual đối tác ghi: 4 điểm trên đều không đúng.

**Đối chiếu SRS v3.5** *(sửa 2026-07-27 sau audit — trước đây mục này kết luận điểm 3+4 "ủng hộ hệ thống" và chấm `Reject`; nay rút lại, xem lý do bên dưới)*

- **Cả 4 điểm phiếu nêu đều quan sát ĐÚNG hiện trạng** (re-verify live 27/07). Không điểm nào là "lỗi không có thật".
- Điểm 1 và 2 **không có căn cứ nào** trong SRS để chấm. Mức chi tiết mà phiếu yêu cầu (định dạng tiêu đề, dấu tích xanh / bước mờ) là mức của **bản đặc tả màn hình**, không phải SRS.
- Chính SRS trỏ tới tài liệu đó: *"**UX-Spec ref:** dac-ta-man-hinh-chuc-nang-v2.md -- MH-15.1"*. **Tài liệu này không có trong bộ SRS v3.5 mà QA đang dùng để đối chiếu** (`find` toàn repo: không tồn tại), nên QA không kiểm được.
- **Điểm 3 — nhãn "Chờ PD": SRS ghi HAI dạng, đây là mâu thuẫn nội bộ (tính chất dạng B).**
  - `:1120` viết thanh tiến trình dạng viết tắt `[Cho PD]`.
  - `:1174` — bảng `#### Bang nhan trang thai SM-KH-CTHTPL` — quy định **nhãn chuẩn** của trạng thái: `| CHO_PHE_DUYET | Cho phe duyet | Vang | --color-warning |`, tức dạng đầy đủ "Chờ phê duyệt" **đúng như kỳ vọng của phiếu**.
  - Web cũng tự lệch: thẻ lọc màn danh sách ghi **"Chờ phê duyệt"**, bước 2 thanh tiến trình ghi **"Chờ PD"** (cùng một phiên đo).
  - ⇒ Không thể kết luận "hệ thống làm đúng" chỉ từ `:1120`. **Khuyến nghị cũ "đề nghị dev không sửa" đã bị gỡ** vì có nguy cơ khoá sai hướng fix.
- **Điểm 4 — khối thông tin nhanh:** thông tin **không mất** (4/4 mục đang hiển thị trong phần Thông tin), nhưng "khối tóm tắt riêng ở đầu trang" là **bố cục** — cùng loại chi tiết và cùng nguồn căn cứ thiếu (MH-15.1) như điểm 1–2. Dùng "SRS không có thành phần tên đó" để Reject điểm 4 trong khi lấy đúng lý do đó để đẩy điểm 1–2 sang BA là **không nhất quán** ⇒ điểm 4 cũng chuyển BA. (`grep -rniE "thông tin nhanh|thong tin nhanh" srs-v3.5/` → **0 hit**.)

**Citation**

- `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-15-ct-htpldn.md:1096` (UX-Spec ref → `dac-ta-man-hinh-chuc-nang-v2.md` MH-15.1 — tài liệu QA không có)
- `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-15-ct-htpldn.md:1107` (thanh điều hướng — chỉ quy định cho **trang danh sách**)
- `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-15-ct-htpldn.md:1120` (thanh tiến trình — viết nguyên văn `[Cho PD]`)
- `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-15-ct-htpldn.md:1169-1174` (**bảng nhãn trạng thái SM-KH-CTHTPL — `CHO_PHE_DUYET` → nhãn "Cho phe duyet"**; nguồn mâu thuẫn với `:1120`)
- `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-15-ct-htpldn.md:1120-1131` (4 thông tin thuộc phần Thông tin: `:1124`/`:1125` thời gian · `:1126` ngân sách · `:1127` đối tượng · `:1129` đơn vị)

**Kết quả verify UI hiện tại**

- Verify lại ngày 27/07/2026 qua Chrome DevTools MCP, tài khoản UAT `cbnv_tw`, có kiểm chéo `cbpd_tw` để chắc đầu trang không đổi theo quyền.
- Mở URL `https://18.143.165.120.nip.io/ct-htpldn/3b85dc5e-f0a7-4746-a483-018e1daddfe1` (chi tiết `CT-20260721-0002`, Đang thực hiện), đối chiếu thêm 3 chương trình ở Đã duyệt / Đã công bố / Hoàn thành.

  | # | Điểm phiếu nêu | Đo thực tế | Có căn cứ trong SRS v3.5? |
  |:-:|---|---|---|
  | 1 | Thanh điều hướng thiếu {Mã chương trình} | Đúng — thanh điều hướng là "Trang chủ / Chương trình HTPLDN / Chi tiết" | **Không.** `:1107` chỉ quy định thanh điều hướng của **trang danh sách**; trang chi tiết không có dòng nào mô tả |
  | 2 | Tiêu đề thiếu {Tên chương trình} | Đúng — tiêu đề là "CT-20260721-0002" kèm nhãn trạng thái; tên chương trình hiện ở dòng ngay dưới trong phần Thông tin | **Không.** Không có dòng nào quy định định dạng tiêu đề trang chi tiết |
  | 3 | Bước 2 hiển thị viết tắt "Chờ PD" | Đúng — thanh tiến trình ghi "Chờ PD"; **cùng lúc thẻ lọc màn danh sách ghi "Chờ phê duyệt"** | **Có ở CẢ HAI dạng, mâu thuẫn nhau.** `:1120` viết *"[Du thao] -- **[Cho PD]** -- [Da duyet] -- [Cong bo] -- [Thuc hien] -- [Hoan thanh]"*; nhưng `:1174` — bảng nhãn trạng thái — quy định `CHO_PHE_DUYET` → nhãn *"Cho phe duyet"* ⇒ **cần BA chốt**, không kết luận được |
  | 4 | Thiếu khối thông tin nhanh | Không có khối tóm tắt riêng, **nhưng cả 4 thông tin đều hiển thị đầy đủ** trong phần "Thông tin" ngay bên dưới | **Không.** `:1120-1131` liệt kê 4 thông tin này là các **trường** của phần Thông tin, không có thành phần nào tên "khối thông tin nhanh" ⇒ cùng lỗ hổng căn cứ (MH-15.1) như điểm 1–2 |

- Evidence: `bug-reports/image/BUG-CT-chi-tiet-dau-trang-va-thanh-tien-trinh.png` · `reverify-audit/audit-reject-2026-07-27/AUDIT-12-chi-tiet-dau-trang-va-phan-thong-tin-day-du.png` (ảnh full-page 27/07: đầu trang + trọn phần Thông tin gồm Đối tượng thụ hưởng / Thời gian / Ngân sách)

**Kết luận QA** *(sửa 2026-07-27)*

- **Cả 4 điểm: quan sát của phiếu đúng, chưa đủ căn cứ để chấm đúng/sai ⇒ `BA confirm` cho toàn case.**
- Điểm 1 và 2: không có căn cứ để chấm vì thuộc phạm vi bản đặc tả màn hình mà QA không có.
- Điểm 3: hai dòng SRS cho hai dạng nhãn khác nhau (`:1120` vs `:1174`) và bản thân web cũng lệch giữa hai chỗ ⇒ BA chốt nhãn chuẩn.
- Điểm 4: thông tin **không mất** — điểm này chỉ hạ severity, không đủ để nói phiếu báo lỗi không có thật; căn cứ về khối tóm tắt vẫn thiếu như điểm 1–2.

**Nội dung đề xuất BA phản hồi đối tác**

- (a) Bản `dac-ta-man-hinh-chuc-nang-v2.md` (MH-15.1) có quy định thanh điều hướng kèm mã CT, tiêu đề dạng `{Mã}: {Tên}`, và **khối thông tin nhanh ở đầu trang** không? Nếu có, **đề nghị BA gửi bản đó** để QA chấm lại điểm 1, 2 và 4.
- (b) Nếu bản đặc tả màn hình không còn hiệu lực hoặc không quy định các điểm này: đề nghị BA **bổ sung mô tả đầu trang chi tiết** vào `srs-fr-15-ct-htpldn.md` và phản hồi đối tác rằng cách bày hiện tại là phương án được chốt, để đối tác không mở lại case ở vòng sau.
- (c) **Nhãn của trạng thái `CHO_PHE_DUYET` trên thanh tiến trình** lấy theo bảng nhãn trạng thái (`:1174` — "Chờ phê duyệt") hay giữ dạng viết tắt (`:1120` — "Chờ PD")? Cần chốt để thanh tiến trình và thẻ lọc trong phần mềm hiển thị thống nhất; sau khi chốt, đề nghị BA sửa dòng còn lại trong SRS cho khớp.
- Verdict QA đề xuất: `Cần BA xác nhận` cho cả 4 điểm — đã ghi **`BA confirm`** trên sheet ngày 27/07/2026 (sửa từ `Reject, BA confirm`, xem [AUDIT-reject-tuan-4.md](reverify-audit/audit-reject-2026-07-27/AUDIT-reject-tuan-4.md)), chưa gửi Dev cho ý nào. Riêng điểm 3 (nhãn trạng thái) sau khi BA chốt thì owner dự kiến `Dev FE` + `BA` (sửa dòng SRS còn lại cho khớp).

---

## TKKHCTHTPL_01 — Thanh lọc màn Chương trình HTPLDN có bổ sung tiêu chí "Lĩnh vực pháp lý" không? *(BA-21 · Dạng A)*

**Bối cảnh testcase**

- Dòng Excel: row 32, mã TC `TKKHCTHTPL_01`.
- Nội dung kiểm tra: CB Nghiệp vụ Trung ương tìm kiếm trên màn Chương trình HTPLDN theo đơn vị quản lý và theo lĩnh vực.
- Expected trong file UAT: thanh lọc có cả hai tiêu chí.
- Actual đối tác ghi: *"Thiếu trường thông tin tìm kiếm theo đơn vị quản lý, lĩnh vực"*.

**Đối chiếu SRS v3.5**

QA tách hai vế ra đo riêng vì căn cứ của chúng **khác hẳn nhau**:

| Vế | Đo thực tế | Căn cứ trong SRS v3.5 | QA xử lý |
|---|---|---|---|
| Thiếu lọc **Đơn vị** | Đúng — thanh lọc không có tiêu chí Đơn vị | **Có.** `:353` liệt kê `don_vi_id` là dữ liệu đầu vào của chức năng tìm kiếm; `:1110` quy định ô chọn **Đơn vị** trên thanh lọc, cột điều kiện hiển thị ghi *"luon hien thi"* | Chấm **Open** — gộp vào `BUG-CT-LOC-THIEU-DONVI-TRANGTHAI` |
| Thiếu lọc **Lĩnh vực** | Đúng — thanh lọc không có tiêu chí Lĩnh vực | **Không.** Bảng dữ liệu đầu vào của FR-XI-02 (`:352`–`:356`) chỉ có 5 mục: `keyword`, `don_vi_id`, `trang_thai`, `tu_ngay`, `den_ngay`. Bảng thanh lọc (`:1109`–`:1112`) cũng chỉ có 4 ô tương ứng. **Không có mục nào là lĩnh vực** | Chuyển **BA-21** |

Đặc tả liệt kê **tường minh** 5 dữ liệu đầu vào của chức năng tìm kiếm và lĩnh vực không nằm trong đó ⇒ chấm lỗi ở đây sẽ là QA **tự thêm yêu cầu ngoài đặc tả**.

**Citation**

- `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-15-ct-htpldn.md:352-356` (FR-XI-02 — 5 dữ liệu đầu vào, không có lĩnh vực)
- `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-15-ct-htpldn.md:1109-1112` (thanh lọc — 4 ô, không có lĩnh vực)
- `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-15-ct-htpldn.md:353` · `:1110` (căn cứ cho vế **Đơn vị** — đã chấm Open)
- `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-15-ct-htpldn.md:370` (kết quả tìm kiếm phải trả kèm `linh_vuc_id, ten_linh_vuc`)
- `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-15-ct-htpldn.md:1113` ("Lĩnh vực pháp lý" là một cột của bảng danh sách)
- `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-15-ct-htpldn.md:1128` (lĩnh vực là trường **bắt buộc** khi tạo chương trình + chiều gom số liệu báo cáo)

**Kết quả verify UI hiện tại**

- Verify lại ngày 27/07/2026 qua Chrome DevTools MCP, tài khoản UAT `cbnv_tw`, có kiểm chéo `cbpd_tw`.
- Mở URL `https://18.143.165.120.nip.io/ct-htpldn/danh-sach` (thanh lọc của màn Chương trình HTPLDN).
- Thanh lọc **không có** cả hai tiêu chí Đơn vị và Lĩnh vực.
- **Phần xử lý phía sau đã hỗ trợ sẵn lĩnh vực:** gọi thẳng dịch vụ dữ liệu của màn kèm tham số lĩnh vực → kết quả thu hẹp từ **8 xuống 1** chương trình đúng lĩnh vực. Đối chứng bằng một tham số **bịa** không tồn tại thì vẫn trả đủ **8** ⇒ tham số lĩnh vực **được xử lý thật**, không bị bỏ qua. Nếu BA đồng ý, phần việc còn lại chỉ là **thêm ô chọn trên giao diện**.
- **Hiện cán bộ không có đường nào tra theo lĩnh vực từ màn này** — vì cột Lĩnh vực pháp lý cũng đang thiếu trên bảng (`BUG-CT-BANG-THIEU-COT-LINHVUC`, dòng `KHTHCTHTPLDN_OOS_05`). Thiếu cả cột lẫn bộ lọc nên muốn biết lĩnh vực phải mở từng chương trình.
- Evidence: `bug-reports/image/BUG-CT-danh-sach-thieu-loc-donvi-trangthai-va-cot-linhvuc.png` · `bug-reports/image/BUG-CT-o-loc-duy-nhat-la-cong-bo.png`

**Kết luận QA**

- Vế **Đơn vị**: đã chấm `Open`, **không chờ BA** — có căn cứ trực tiếp ở `:353` và `:1110`.
- Vế **Lĩnh vực**: QA **không tự chấm là lỗi**, chuyển BA — nhưng đề xuất của đối tác là hợp lý về nghiệp vụ, dựa trên 3 dữ kiện nêu trên.

**Nội dung đề xuất BA phản hồi đối tác**

- (a) Bổ sung ô chọn **Lĩnh vực pháp lý** vào thanh lọc và cập nhật `:352`–`:356` + `:1109`–`:1112` cho khớp. **QA nghiêng phương án này** vì phần xử lý đã có sẵn và lĩnh vực là chiều gom số liệu báo cáo (`:1128`).
- (b) Giữ nguyên 4 tiêu chí như đặc tả hiện tại. Khi đó QA sẽ phản hồi đối tác rằng vế "lĩnh vực" không phải lỗi, và đề nghị **vẫn ưu tiên bổ sung cột** Lĩnh vực pháp lý vào bảng (`:1113` đã quy định) để cán bộ ít nhất nhìn thấy được.
- **Ghi chú:** dù BA chốt hướng nào cho câu hỏi này, **bộ lọc Đơn vị vẫn phải bổ sung** theo `:1110`.
- Verdict QA đề xuất: `Open, BA confirm`.

---

## TKVVHTPLDN_01 — Hợp đồng API cho hệ thống tích hợp: bản SRS hay bản mô tả API đã triển khai là bản chính thức? *(BA-22 · Dạng B)*

**Bối cảnh testcase**

- Dòng Excel: row 35, mã TC `TKVVHTPLDN_01`.
- Nội dung kiểm tra: hệ thống tích hợp bên ngoài gọi API tìm kiếm vụ việc HTPL theo từ khóa.
- Expected trong file UAT: trả về danh sách vụ việc khớp từ khóa.
- Actual đối tác ghi: nhận lỗi 400 với thông báo *"Validation failed (uuid is expected)"* — hệ thống đòi một mã định danh trong khi thao tác là tìm theo từ khóa.

**Kết quả verify UI hiện tại**

- Nhóm API này **không có màn hình nào** để verify qua giao diện: đã rà mã nguồn giao diện CMS (bundle 1.119.097 byte) → **0 lần** gọi `/api/v1/public/*`.
- **Không có URL màn hình để mở** — thay vào đó QA gọi thẳng đường dẫn của nhóm API: `GET https://18.143.165.120.nip.io/api/v1/public/vu-viecs/search?keyword=...`.
- QA **không thực thi lại được** lời gọi: toàn bộ bề mặt `/api/v1/public/*` trên môi trường được giao trả **401** với mã lỗi chứng thư số phía khách (mTLS). Đã thử cạn kiệt **10 hướng** (4 dạng URL × cách xác thực, cổng 80, 6 cổng ứng dụng trực tiếp, 5 cổng HTTPS thay thế, kiểm bắt tay TLS, mã nguồn giao diện, hồ sơ tài khoản được giao) — xem bảng cạn kiệt trong `bug-reports/image/BLOCKER-TKVVHTPLDN_01-cong-api-cong-khai-mtls.log.txt`.
- Máy chủ **không đòi chứng thư ở bước bắt tay TLS** ⇒ kể cả được cấp chứng thư cũng không trình lên được qua đường này. Tiền đề còn thiếu do **bên vận hành** cấp, QA không tự tạo được.
- **Vẫn verify được phần hợp đồng** bằng nguồn độc lập với phiếu đối tác: `GET /api/docs-json` (200, ~1,5 MB, 530 đường dẫn, không cần xác thực). Kết quả đối chiếu ghi trong `bug-reports/image/BUG-API-tim-vu-viec-400-doi-chieu-hop-dong.log.txt`.

**Điểm mâu thuẫn trong SRS v3.5**

1. **Hai tài liệu công bố hai dạng đường dẫn khác nhau cho cùng một chức năng.**

   | Nguồn | Đường dẫn công bố | Dạng |
   |---|---|---|
   | SRS v3.5 (FR-XII-08) | `GET /api/v1/vu-viec/search` | entity **số ít**, **không** có `public` |
   | Bản mô tả API đã triển khai (`GET /api/docs-json`) | `GET /api/v1/public/vu-viecs/search` | entity **số nhiều**, **có** `public` |

   Citation:
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-16-api.md:665` (FR-XII-08 — chức năng tìm kiếm vụ việc cho hệ thống tích hợp)
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-16-api.md:671` (đường dẫn dạng `/api/v1/vu-viec/search`)
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/danh-sach-api.md:67` (bản liệt kê API — cùng dạng số ít)

2. **Không thể kết luận đường dẫn SRS "không tồn tại".** QA ban đầu suy diễn rằng gọi theo đường dẫn SRS sẽ nhận 404; **đo lại thì sai**. Số liệu thật:

   | Đường dẫn thử | Mã HTTP | Mã lỗi trả về |
   |---|:-:|---|
   | `/api/v1/public/vu-viecs/search?keyword=…` | 401 | `ERR-AUTH-MTLS-01` (lỗi chứng thư) |
   | `/api/v1/vu-viec/search?keyword=test` (dạng SRS) | 401 | `ERR-AUTH-MTLS-01` (lỗi chứng thư) |
   | `/api/v1/hoi-dap/search?keyword=test` (dạng SRS) | 401 | `ERR-AUTH-MTLS-01` (lỗi chứng thư) |
   | `/api/v1/vu-viec/abc/def` (đường dẫn bịa) | 404 | `ERR-SYS-00-04-01` |
   | `/api/v1/xyz-khong-co/search` (đường dẫn bịa) | 404 | `ERR-SYS-00-04-01` |

   **Cách đọc số liệu:** đường dẫn dạng SRS trả **cùng loại lỗi chứng thư** như đường dẫn `public`, còn đường dẫn bịa trả **404**. Nếu đường dẫn SRS không được khai báo ở đâu cả thì đã phải 404 giống 2 dòng cuối ⇒ **rất có thể là đường dẫn thay thế có thật** nhưng không xuất hiện trong bản mô tả API công bố. QA không xác nhận được thêm vì bị chặn ở lớp chứng thư.

3. **Bản mô tả API đã triển khai chứng minh lời gọi của đối tác là hợp lệ** — tức lỗi 400 không do dữ liệu đối tác nhập sai:
   - tham số bắt buộc **duy nhất** của `/search` là `keyword`, kiểu chuỗi, độ dài tối thiểu 2. Cả hai giá trị đối tác gửi đều hợp lệ;
   - endpoint này **không có tham số bắt buộc nào kiểu uuid** — hai tham số kiểu uuid (`linhVucId`, `doanhNghiepId`) đều **không** bắt buộc và đối tác **không** gửi;
   - đường dẫn liền kề `/api/v1/public/vu-viecs/{id}` thì lại đòi **bắt buộc** `doanhNghiepId` kiểu uuid.

   Citation:
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-16-api.md:681` (tham số của chức năng tìm kiếm)
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-16-api.md:690` (chức năng xem chi tiết theo quyền sở hữu)

**Câu hỏi cần BA xác nhận**

1. **Bản nào là hợp đồng chính thức** để đối tác tích hợp và để QA đối chiếu: dạng `/api/v1/vu-viec/...` trong SRS, hay dạng `/api/v1/public/vu-viecs/...` trong bản mô tả API đã triển khai?
   - (a) Bản mô tả API đã triển khai là chuẩn → đề nghị BA cập nhật `srs-fr-16-api.md` và `danh-sach-api.md` cho khớp, và thông báo dạng đường dẫn đúng cho đối tác.
   - (b) SRS là chuẩn → dev phải bổ sung/đổi tên đường dẫn cho khớp SRS.
   - (c) Cả hai đều hiệu lực (một là bí danh của cái kia) → đề nghị BA ghi rõ quan hệ bí danh này vào SRS để không ai còn phải suy đoán.
2. **Môi trường UAT có kế hoạch cấp chứng thư số phía khách cho QA không?** Nếu không, nhóm API tích hợp (FR-XII) sẽ **không verify được ở mọi vòng UAT tiếp theo** — cần BA/bên vận hành quyết sớm, vì đây là hạn chế môi trường chứ không phải hạn chế kỹ năng.

**Đề xuất QA tạm thời**

- Case `TKVVHTPLDN_01` đã chấm **`Open`** theo quyết định của quản lý QA, kèm mô tả để **dev tự kiểm** — QA nói rõ trong bug entry và trong ghi chú gửi đối tác rằng số liệu lỗi lấy từ **bản ghi hình trong phiếu đối tác**, KHÔNG phải phép đo của QA.
- Bug đã log: `BUG-API-TIM-VUVIEC-BAO-LOI-UUID` (Major, P1, Backend) trong [bug-report-UAT-tuan-4.md](bug-reports/bug-report-UAT-tuan-4.md).
- **Giả thuyết nêu cho dev truy nguyên** (nêu dạng gợi ý, không kết luận thay dev): kiểm tra xem lời gọi `.../search` có bị xử lý nhầm sang nhánh xem chi tiết theo định danh không — nhánh đó đòi bắt buộc `doanhNghiepId` kiểu uuid, khớp đúng thông báo lỗi đối tác nhận được. Lỗi phát sinh ở **tầng kiểm tra dữ liệu vào**, trước khi truy vấn dữ liệu ⇒ độc lập với vai trò và trạng thái bản ghi.

---

## KHTHCTHTPLDN_03 — Màn "Đợt báo cáo" thuộc mô hình nào, và bảng danh sách CT có cần liên kết nhanh sang màn đó? *(BA-23 · Dạng B)*

**Bối cảnh testcase**

- Dòng Excel: row 28, mã TC `KHTHCTHTPLDN_03` (mở mới 2026-07-27 sau audit verdict — case này trước đó mang `Reject`).
- Nội dung kiểm tra: CB Nghiệp vụ Trung ương mở màn danh sách Chương trình HTPLDN và đối chiếu tập cột với thiết kế.
- Expected trong file UAT: bảng danh sách có cột **"Đợt báo cáo"** đóng vai trò **liên kết nhanh** mở màn "Đợt báo cáo định kỳ" độc lập.
- Actual đối tác ghi: không có cột đó, bảng hiển thị cột **"Số đợt BC"**.

**Kết quả verify UI hiện tại**

- Verify lại 2026-07-27 17:35 qua Chrome DevTools MCP, tài khoản `cbnv_tw` (CB Nghiệp vụ - Trung ương, BTP · TW), có kiểm chéo `cbpd_tw`.
- Mở URL `https://18.143.165.120.nip.io/ct-htpldn/danh-sach` (thẻ "Tất cả", 8 chương trình trải 4 trạng thái) và `https://18.143.165.120.nip.io/ct-htpldn/3b85dc5e-f0a7-4746-a483-018e1daddfe1` (chi tiết `CT-20260721-0002`).
- **Quan sát của đối tác đúng.** Đọc tiêu đề bảng bằng mã lệnh (cuộn hết chiều ngang) → đúng **9 cột**: `Mã CT · Tên chương trình · Mục tiêu · Thời gian · Ngân sách · Đơn vị · Trạng thái · Số đợt BC · Hành động`. Không có cột "Đợt báo cáo".
- Menu bên trái có mục **"Đợt báo cáo"** đứng độc lập ngang hàng với "Chương trình HTPLDN".
- **Trang chi tiết CT chỉ có 1 thẻ "Thông tin"** — không có thẻ "Đợt báo cáo".
- Đối chiếu với đặc tả: tên cột "Số đợt BC" **khớp** `:1113`; mô hình màn Đợt báo cáo **khớp** `:618` nhưng **trái** `:1101`.
- Evidence: `reverify-audit/audit-reject-2026-07-27/AUDIT-03-08-danh-sach-9-cot-va-cot-hanh-dong.png`

**Điểm mâu thuẫn trong SRS v3.5**

1. Theo **FR-XI-05a (UC165)**, màn Đợt báo cáo là **màn độc lập, không mở từ chương trình**:
   - `:618` — *"**Màn hình:** SCR-XI-01 — Quản lý CT HTPLDN (tổng hợp) (**v3.5.2: tab "Đợt báo cáo" độc lập, không drill-down từ CT**)"*.
   - Ở mô hình này bảng danh sách CT chỉ cần **số đếm** đợt — đúng như cột *"So dot BC"* mà `:1113` quy định, và đúng như phần mềm đang làm.
   - Phần mềm khớp hướng này: menu bên trái có mục "Đợt báo cáo" riêng; trang chi tiết CT chỉ có thẻ "Thông tin".

   Citation:
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-15-ct-htpldn.md:618`
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-15-ct-htpldn.md:1113` (tập 10 cột bảng danh sách — cột 9 = *"So dot BC"*, cột 4 = *"Linh vuc phap ly"*)

2. Nhưng **SCR-XI-01** lại mô tả Đợt báo cáo là **một thẻ nằm trong trang chi tiết CT**, tức vẫn mở từ chương trình:
   - `:1101` — *"**Trang chi tiet CT:** Tab "Thong tin" (form CT + bieu mau + action buttons lifecycle) + Tab "Dot bao cao" (bang dot BC + drill-down dot -> form lap BC + phe duyet + gui TW + tong hop)"*.
   - `:1143`–`:1166` — trọn bảng *"Thanh phan man hinh -- Trang Chi tiet CT: Tab "Dot bao cao""* vẫn nằm trong SCR-XI-01, chưa bị gỡ.
   - Ở mô hình này, kỳ vọng của phiếu (có đường mở nhanh từ dòng chương trình sang màn Đợt báo cáo) là **hợp lý**.

   Citation:
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-15-ct-htpldn.md:1101`
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-15-ct-htpldn.md:1143-1166`

⇒ Bản đặc tả **giữ song song hai mô hình**. Phần mềm đang làm theo `:618`. Không thể kết luận phiếu "hiểu sai" khi chính đặc tả còn hai hướng.

**Câu hỏi cần BA xác nhận**

1. **Mô hình nào đang hiệu lực** cho màn Đợt báo cáo: tab độc lập theo `:618`, hay thẻ trong trang chi tiết CT theo `:1101` + `:1143-1166`?
   - (a) Theo `:618` → đề nghị BA **gỡ** phần tab Đợt báo cáo ở `:1101` và `:1143-1166` khỏi SRS để không ai còn đối chiếu theo mô hình cũ.
   - (b) Theo `:1101` → phần mềm thiếu thẻ "Đợt báo cáo" trong trang chi tiết CT, QA sẽ mở bug riêng.
2. **Bảng danh sách CT có bổ sung liên kết nhanh sang màn "Đợt báo cáo định kỳ" không** (ví dụ bấm vào số ở cột "Số đợt BC" để mở màn Đợt báo cáo đã lọc theo chương trình)? Nếu **không** bổ sung, đề nghị BA phản hồi rõ để đối tác không mở lại case; nếu **có**, đây là yêu cầu mới cần ghi vào `:1113`.

**Đề xuất QA tạm thời**

- **Chưa gửi ý này cho Dev cho tới khi BA chốt mô hình** — nếu fix trước khi chốt thì rất dễ làm ngược lại quyết định của BA.
- Tạm verdict cho `KHTHCTHTPLDN_03`: `Cần BA xác nhận`. Verdict QA đề xuất: `Cần BA xác nhận` — đã ghi **`BA confirm`** trên sheet ngày 27/07/2026 (sửa từ `Reject`, xem [AUDIT-reject-tuan-4.md](reverify-audit/audit-reject-2026-07-27/AUDIT-reject-tuan-4.md)), chưa gửi Dev cho riêng ý này.
- **Nếu BA chọn hướng 1 (`:618` — màn độc lập):** phần mềm hiện tại **đúng** ở cả tên cột và cấu trúc màn ⇒ QA cập nhật expected của testcase; owner dự kiến `BA` (gỡ phần tab Đợt báo cáo ở `:1101` + `:1143-1166` khỏi SRS) — **không** có việc cho Dev, trừ khi BA quyết bổ sung liên kết nhanh ở câu hỏi 2 (khi đó owner `Dev FE`).
- **Nếu BA chọn hướng 2 (`:1101` — thẻ trong chi tiết CT):** phần mềm **thiếu thẻ "Đợt báo cáo"** trong trang chi tiết CT ⇒ `Vẫn lỗi`, owner dự kiến `Dev FE` (+ `Dev BE` nếu cần API lấy đợt theo chương trình); QA sẽ mở bug riêng sau khi BA chốt.
- **Độc lập với quyết định của BA:** cùng bảng này **thiếu cột "Lĩnh vực pháp lý"** mà `:1113` có liệt kê (web 9/10 cột). Dữ liệu đã có sẵn — tệp Excel xuất từ chính màn này in ra đủ Đất đai / Thuế / Lao động; `:1128` xác nhận lĩnh vực pháp lý là trường bắt buộc khi tạo CT. Đã log dòng riêng `KHTHCTHTPLDN_OOS_05`, bug `BUG-CT-BANG-THIEU-COT-LINHVUC` (đang `Open`, owner `Dev FE`). Phần này **không** chờ BA.

---

## KHTHCTHTPLDN_08 — Cột "Hành động" trên dòng danh sách CT gồm những nút nào? *(BA-24 · Dạng A)*

**Bối cảnh testcase**

- Dòng Excel: row 30, mã TC `KHTHCTHTPLDN_08` (mở mới 2026-07-27 sau audit verdict — case này trước đó mang `Reject`).
- Nội dung kiểm tra: hành động nhanh trên dòng của bảng danh sách Chương trình HTPLDN.
- Expected trong file UAT: Đang thực hiện → [Tạm dừng]; Đã duyệt / Đã công bố → [Kích hoạt]; Dự thảo → [Sửa].
- Actual đối tác ghi: không hiển thị nút nào trong số đó.

**Đối chiếu SRS v3.5**

- **Kỳ vọng của phiếu trùng với một bảng CÓ THẬT trong SRS** — `#### Bang hanh dong theo trang thai CT` (`:1193`–`:1207`), map trạng thái → nút nhưng **không quy định nút nằm ở đâu**:
  - `:1202` `DA_DUYET | [Kich hoat] | DANG_THUC_HIEN` · `:1204` `DA_CONG_BO | [Kich hoat]` → khớp ý 2 của phiếu.
  - `:1205` `DANG_THUC_HIEN | [Tam dung] | TAM_DUNG | Modal ly do` → khớp ý 1 của phiếu.
  - `:1211` *"Sua/Xoa CT: chi khi DU_THAO"* → khớp ý 3 của phiếu.
- **Cột Hành động của bảng danh sách chỉ được mô tả là *"Hanh dong (conditional)"*** (`:1113`) — không liệt kê tập nút, không nói "conditional" theo tiêu chí gì.
- Bảng thành phần **trang chi tiết** thì liệt kê rõ các nút vòng đời ở `action-bar`: `:1132` (nhóm nút khi Dự thảo), `:1136` ([Kích hoạt], nhãn nguyên văn *"Bat dau thuc hien"*), `:1138` ([Tạm dừng]).
- ⇒ SRS **im lặng đúng chỗ đang tranh chấp** (dòng danh sách vs trang chi tiết). Không có dòng nào nói các nút này **không được** nằm trên dòng.

**Citation**

- `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-15-ct-htpldn.md:1113` (cột Hành động — chỉ ghi "conditional")
- `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-15-ct-htpldn.md:1132` · `:1136` · `:1138` (nút vòng đời ở action-bar trang chi tiết)
- `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-15-ct-htpldn.md:1193-1207` (**bảng hành động theo trạng thái CT — nguồn kỳ vọng của phiếu**)
- `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-15-ct-htpldn.md:1211` (*"Sua/Xoa CT: chi khi DU_THAO"*)
- `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-15-ct-htpldn.md:264` · `:274` ([Hoàn thành] chỉ dành cho CB Phê duyệt — `ERR-XI-01-HT-01`)

**Kết quả verify UI hiện tại**

- Verify lại 2026-07-27 17:35–17:42 qua Chrome DevTools MCP, hai tài khoản `cbnv_tw` và `cbpd_tw` (đặc tả phân quyền khác nhau cho từng nút).
- Mở URL `https://18.143.165.120.nip.io/ct-htpldn/danh-sach`, rồi mở trang chi tiết của từng trạng thái từ chính dòng danh sách (`.../ct-htpldn/{id}` — 4 bản ghi ở bảng dưới).
- **Dòng danh sách:** 8/8 dòng chỉ có 1 nút `Xem chương trình <mã>` — dòng `CT-20260721-0002` (Đang thực hiện) **không** có [Tạm dừng]. ⇒ quan sát của phiếu **đúng**.
- **Trang chi tiết — đọc toàn trang gồm cả thanh cố định đáy màn hình:**

  | Trạng thái | Bản ghi | Nút thực tế | Đặc tả yêu cầu | Khớp? |
  |---|---|---|---|:-:|
  | Đã duyệt | `CT-20260725-0002` | [Công bố lên Cổng PLQG] · [Bắt đầu thực hiện] | `:1135` [Công bố] · `:1136` [Kích hoạt] | ✅ |
  | Đã công bố | `CTHTPL-SEED-0001` | [Hủy công bố] · [Bắt đầu thực hiện] | `:1137` [Hủy công bố] · `:1136` [Kích hoạt] | ✅ |
  | Đang thực hiện | `CT-20260721-0002` | [Tạm dừng] (thêm [Hoàn thành] khi đăng nhập `cbpd_tw`) | `:1138` [Tạm dừng] · `:1140` [Hoàn thành] (CB PD — `:264`/`:274`) | ✅ |
  | Hoàn thành | `CT-20260721-0003` | không có nút | không quy định (trạng thái kết thúc) | ✅ |

- **Lưu ý cho người kiểm lại:** nút nằm ở **thanh cố định đáy màn hình**, ngoài vùng nội dung chính — quét trong vùng nội dung sẽ trả về 0 nút và dễ kết luận nhầm là mất chức năng.
- Evidence: `reverify-audit/audit-reject-2026-07-27/AUDIT-03-08-danh-sach-9-cot-va-cot-hanh-dong.png` · `reverify-audit/audit-reject-2026-07-27/AUDIT-12-chi-tiet-dau-trang-va-phan-thong-tin-day-du.png` (thấy rõ [Tạm dừng] ở thanh cố định)

**Kết luận QA**

- **Chức năng nghiệp vụ không thiếu** — mọi nút vòng đời có đủ ở trang chi tiết, đúng trạng thái và đúng vai trò.
- **Nhưng không kết luận được phiếu sai:** kỳ vọng của phiếu lấy từ `:1193-1207` của chính SRS, và SRS không chốt vị trí nút ⇒ đây là bất đồng về **đặc tả**, phải để BA quyết.

**Nội dung đề xuất BA phản hồi đối tác**

- (a) Cột Hành động trên dòng danh sách **chỉ giữ nút Xem** (mọi hành động vòng đời thực hiện ở trang chi tiết) → đề nghị BA ghi rõ tập nút của cột này vào `:1113` để đối tác không mở lại case ở vòng sau.
- (b) Cột Hành động **phải hiển thị thêm nút theo trạng thái** → đây là yêu cầu bổ sung phía giao diện danh sách, QA sẽ mở bug sau khi BA chốt.
- (c) **Bất đối xứng cần chốt cùng lúc:** `:1211` gộp *"Sửa/Xóa CT: chỉ khi Dự thảo"*, nhưng dòng Dự thảo hiện có biểu tượng **xóa** mà **không có Sửa** (việc sửa thực hiện trong biểu mẫu ở trang chi tiết). Ghi nhận từ ảnh đối tác — env QA hiện không còn bản ghi Dự thảo nên **chưa re-verify được**, không dùng làm căn cứ chấm lỗi.
- Verdict QA đề xuất: `Cần BA xác nhận` — đã ghi **`BA confirm`** trên sheet ngày 27/07/2026 (sửa từ `Reject`, xem [AUDIT-reject-tuan-4.md](reverify-audit/audit-reject-2026-07-27/AUDIT-reject-tuan-4.md)), chưa gửi Dev. Nếu BA chọn phương án (b) thì owner dự kiến `Dev FE`; chọn (a) thì owner `BA` (ghi rõ tập nút vào `:1113`), không có việc cho Dev.

---

*File cập nhật sau mỗi luồng verify. BA phản hồi trực tiếp vào từng mục hoặc trả lời tập trung — QA sẽ cập nhật trạng thái ở bảng chỉ mục và điều chỉnh verdict trên sheet tuần 4 theo kết luận của BA.*
