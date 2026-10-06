# Phản hồi phiếu DEV — hai phiếu ngày 05/08/2026

- **Phiếu nguồn:** `Week5/Yêu cầu/phan-hoi-ba-TONG-HOP-reject-va-diem-can-chot-2026-08-05.md` (45 TC Reject + 3 điểm kỹ thuật) · `Week5/Yêu cầu/phan-hoi-ba-lo-10-bug-NR-OPEN-2026-08-05.md` (lô 10 bug N/R + Open). **Ngày phản hồi:** 05–06/08/2026
- **Sổ theo dõi:** sổ KTĐL `1dJat1cc…` tab `UAT_TGPL Doanh Nghiệp` (gid 799081340), bản tải 05/08 và 06/08/2026. Cột Mã TC đã là giá trị cố định, không còn công thức; các mã trong phiếu đều duy nhất, không trùng khối tuần
- ⚠️ **ĐÍNH CHÍNH 08/08/2026 — sổ đã được đánh số lại.** Ngày 08/08 đơn vị kiểm thử sửa sổ: tổng dòng 1.640 → 1.633, riêng khối `QLHDTVVCG_` gom từ 27 xuống 21 test case và **đánh số lại từ đầu**. Đã tra lại **toàn bộ 110 ô ghi chú** theo *nội dung dòng* (Mô tả + Kết quả mong đợi), không tra theo mã: **110/110 ô nằm đúng dòng**, mã hiện tại khớp mã lúc ghi. Chỗ lệch là **mã ghi trong phiếu này** — mã của Vấn đề 3, 4, 5 viết theo bản 06/08 nên nay trỏ sang test case khác. Bảng quy đổi mã ở từng mục dưới. **Khi tra sổ, luôn tìm theo nội dung test case, không tìm theo mã.**
- **Bản `.docx` đối chiếu:** `HTPLDN-PTYC-CT-v3.5.docx` — bản bàn giao có hiệu lực, dùng cho câu (1b) ở mọi mục. **Ngày bàn giao và kênh gửi chưa được ghi nhận trong kho**; tệp trong kho sửa lần cuối 01/08/2026. Để kết luận không phụ thuộc việc đối tác cầm bản nào, hai cụm tranh chấp lớn (Vấn đề 1, 2) đã **tra chéo bản v2.0 và bản dựng từ v1.0** — ba bản nói giống hệt nhau
- **Bản chấm chuẩn:** SRS `.md` — `_bmad-output/planning-artifacts/srs-v3.5/`

**Ghi chú phương pháp:**
- Trạng thái lấy từ ô `Trạng thái` của sổ KTĐL, không lấy từ mô tả trong phiếu Dev. Trong 45 TC Dev gọi là "Reject", chỉ **32 dòng** đang `Fail`; **27 dòng** `QLHDTVVCG_01`…`_27` là `N/R` (Dev chỉ nêu 12), `QLDXDTTH_07` và `CPCTHTTLV_01` là `Đang Phát Triển`, `QLCHTHXLHS_09` đã `Pass`.
- Toàn bộ trích dẫn `file:dòng` của hai phiếu Dev đã mở kiểm lại từng dòng; các chỗ kết luận khác đề xuất của Dev đều nêu căn cứ tại chỗ.
- Cụm gộp: Vấn đề 1 (16 mã), Vấn đề 2 (16 mã), Vấn đề 3 (27 mã), Vấn đề 10 (3 mã) — phân tích một lần, cập nhật sổ theo từng dòng.


> ⚠️ **ĐÍNH CHÍNH 08/08/2026 — nguồn `.docx` của phiếu này đã sai.** Toàn bộ trích `.docx` ở các mục dưới lấy từ thư mục `_bmad-output/partner-docx-v3.5/` (nay đã đổi tên thành `_KHONG-DUNG-NUA_…`). Bộ đó sinh ra bản 23/06 ≈ v2.0, **không phải bản đối tác cầm**. Bản bàn giao có hiệu lực là **`docs/Reference/HTPLDN-PTYC-CT-v3.5.docx` ngày 01/08/2026** — đã tra thẳng tệp và đính chính từng mục bên dưới. `.docx` đã được cập nhật theo bản gốc ngày 08/08.

---

# Phần I — Phiếu 45 TC Reject

## Vấn đề 1 — Cụm A: nút "In báo cáo" trên 16 màn Báo cáo thống kê (16 TC)

**Vấn đề:** Người kiểm thử mở màn hình báo cáo, xem kết quả rồi tìm nút để in ra giấy — trên màn hình không có nút nào như vậy. Tài liệu họ được giao có mô tả nút này kèm đúng khuôn trình bày văn bản hành chính nên họ ghi lỗi. Không khép dứt điểm thì 16 phiếu này quay lại ở mọi đợt kiểm thử sau.

**Mã trong cụm (Tuần 3):** `LDTBDDDR_08` · `CGTVPL_08` · `DGHQHTPL_08` · `CLDTBDPL_08` · `VVTDVQL_08` · `VVTLV_07` · `VVTLHDN_07` · `VVTTGCT_07` · `CPHTCT_08` · `CPCTHTTDVQL_08` · `CPCTHTTLHDN_08` · `CPCTHTTTG_07` · `SLCTHT_08` · `CTTDVQL_06` · `CTTLV_07` · `CTTTG_06`. Cả 16 dòng đều `Fail`, ô Kết quả thực tế **trống**, ghi chú *"Màn hình không hiển thị nút chức năng"*.

**(1) Phần mềm đúng SRS chưa? → ĐÚNG.** Vùng hành động chỉ có ba nút, không có nút In:
- `srs-fr-11-bao-cao.md:1051` — *"Nút Xem báo cáo | button (primary) | 'Xem báo cáo' → chạy query"*
- `srs-fr-11-bao-cao.md:1052-1053` — *"Nút Xuất Excel"*, *"Nút Xuất PDF"*
- Tra toàn thư mục `srs-v3.5/`: không có chuỗi "In báo cáo" ở bất kỳ file FR nào.

**(1b) Bản `.docx` đối tác cầm có nói khác không? → CÓ** — xem bảng Loại 4 bên dưới.

**(2) Đối tác yêu cầu khác SRS ở đâu? → Đúng một nút.** Không khác gì thêm; Kết quả mong đợi là bản sao nguyên văn đoạn trong `.docx`.

**(3) Yêu cầu đó có bắt buộc cho luồng nghiệp vụ không? → KHÔNG.** Xuất Excel và Xuất PDF đã phục vụ đủ nhu cầu lưu trữ, trình ký, phát hành; in là tiện lợi thêm.

| Trường | Nội dung |
|---|---|
| Bản `.docx` đối chiếu | `HTPLDN-PTYC-CT-v3.5.docx` — xem đầu phiếu. Đã tra chéo v2.0 và bản dựng từ v1.0: giống hệt |
| Trích `.docx` | ⚠️ **Đính chính 08/08:** chuỗi dưới đây KHÔNG có trong bản 01/08 ở mục 4.11. Nhưng chức năng in **có thật**, ở **mục 3.11.2 bước 6 "Xuất tệp hoặc in báo cáo"**: *"nếu Cán bộ chọn in: dựng bản xem trước đúng định dạng Thông tư 17/2025 và gọi hộp in của trình duyệt"* — **kết luận Loại 4A vẫn đứng**, chỉ sai địa chỉ mục. Đã gỡ khỏi `.docx` ngày 08/08. *(Trích cũ, từ nguồn sai:)* Mục **4.11.1.2.3 STT 4 "In báo cáo"**: *"Điều kiện hiển thị: đã có kết quả báo cáo hiển thị trên màn hình. NSD bấm nút 'In báo cáo', hệ thống dựng bản xem trước định dạng theo Thông tư số 17/2025/TT-BTP (khổ A4, Times New Roman cỡ 13) và mở hộp thoại in của trình duyệt. NSD xác nhận trong hộp thoại in, hệ thống gửi lệnh in tới máy in đã chọn. Lưu vết thao tác in theo quy định."* Mục 4.11.2.2.3 và các mục nhóm báo cáo còn lại ghi *"hoạt động tương tự mục 4.11.1.2.3"* — đó là lý do một mong muốn lặp trên đủ 16 màn |
| Trích `.md` | **Không có.** Tra toàn thư mục `srs-v3.5/`: không có chuỗi "In báo cáo" |
| Hướng | **A** — bỏ **có chủ đích**. Tầng 1 (quyết định BA): `CHANGELOG-v3-to-v3.5.md:590`, bảng *"Thay đổi BA chốt OUT — KHÔNG áp vào v3.5"*: *"Thay đổi 8 — Bổ sung chức năng 'In báo cáo' với print preview A4 \| BA chốt 2026-05-06: không đưa vào v3.5"*. Tầng 4 (CSV): `docs/Input/Danh sách transaction_v1.1_2026-03-27.csv` — mỗi UC124–146 chỉ có 2 transaction (thống kê; xuất file excel), không có transaction in |
| Dev action | **Không** |
| Doc action | Bên soạn tài liệu bàn giao — bản `.docx` kế tiếp: gỡ STT 4 mục 4.11.1.2.3 và mọi chỗ tham chiếu tới nó |
| Sheet | **Resolve** (16 dòng) |

**→ Kết luận: Loại 4 hướng A — phần mềm đúng bản gốc, tài liệu bàn giao thừa một nút. Không bổ sung "In báo cáo" vào SRS; quyết định BA ngày 06/05/2026 giữ nguyên. Dev action: Không → Sheet: Resolve, KHÔNG Reject.**

> **Phản hồi gửi đối tác:**
> Xác nhận bản SRS docx đang thừa thành phần. Sẽ gửi lại bản cập nhật mới nhất khi bàn giao fix bug tuần.

---

## Vấn đề 2 — Cụm B: nút "Xóa bộ lọc" trên 16 màn Báo cáo thống kê (16 TC)

**Vấn đề:** Sau khi nhập một loạt điều kiện lọc, người kiểm thử tìm nút để xóa sạch và đưa các ô lọc về mặc định — màn hình chỉ có nút "Làm mới". Tài liệu bàn giao mô tả đây là hai nút khác nhau nên họ ghi lỗi cho nút còn thiếu.

**Mã trong cụm (Tuần 3):** `LDTBDDDR_09` · `CGTVPL_09` · `DGHQHTPL_09` · `CLDTBDPL_09` · `VVTDVQL_09` · `VVTLV_08` · `VVTLHDN_08` · `VVTTGCT_08` · `CPHTCT_09` · `CPCTHTTDVQL_09` · `CPCTHTTLHDN_09` · `CPCTHTTTG_08` · `SLCTHT_09` · `CTTDVQL_07` · `CTTLV_08` · `CTTTG_07`. Cả 16 dòng cùng tình trạng như cụm A.

**(1) Phần mềm đúng SRS chưa? → ĐÚNG.** Bản gốc chỉ có "Làm mới", và không định nghĩa bộ giá trị mặc định nào để mà đặt lại:
- `srs-fr-11-bao-cao.md:1046` — *"toolbar | Tiêu đề trang | label | 'Báo cáo Thống kê' + Nút Làm mới"*
- `srs-fr-11-bao-cao.md:69-71` — bảng Input chung, cột **Mặc định** của `ky_bao_cao`, `tu_ngay`, `den_ngay` đều ghi **"—"**. Riêng `don_vi_id` (`:72`) **có** mặc định theo phân quyền (*"Auto phân quyền nếu không truyền"*, màn hình `:1049` ghi *"Auto theo phân quyền 2-tier"*) — nên trong bốn ô lọc mà `.docx` đòi đặt lại, chỉ một ô có giá trị mặc định trong bản gốc
- Tra toàn `srs-fr-11-bao-cao.md`: không có chuỗi "Xóa bộ lọc".

**(1b) Bản `.docx` đối tác cầm có nói khác không? → CÓ, và tách rõ hai nút** — xem bảng Loại 4 bên dưới.

**(2) Đối tác yêu cầu khác SRS ở đâu? → Khác ba thứ.** Ngoài cái nút, `.docx` còn đặt ra **cả một bộ giá trị mặc định** mà bản gốc để trống hoàn toàn, **và** quy tắc *"khu vực kết quả không tự tải lại cho đến khi bấm 'Xem báo cáo'"*. Đây không phải chuyện tên nút.

**(3) Yêu cầu đó có bắt buộc cho luồng nghiệp vụ không? → KHÔNG.** Người dùng vẫn sửa được từng ô lọc rồi bấm "Xem báo cáo"; không có bước nghiệp vụ nào tắc.

| Trường | Nội dung |
|---|---|
| Bản `.docx` đối chiếu | `HTPLDN-PTYC-CT-v3.5.docx` — xem đầu phiếu. Đã tra chéo v2.0 và bản dựng từ v1.0: giống hệt |
| Trích `.docx` | ⚠️ **Đính chính 08/08 — kết luận Loại 4A của mục này ĐỔ.** Bản 01/08 có "Xóa bộ lọc" ở 14 chỗ nhưng **không chỗ nào thuộc nhóm Báo cáo thống kê** (chỉ ở 4.2, 4.3, 4.4, 4.5, 4.7); mục 3.11.2 và 4.11 đều không có. Tức `.docx` bàn giao **đã đúng**; đối tác lấy Kết quả mong đợi từ bản cũ họ cầm hồi 16/07. Không có Doc action. *(Trích cũ, từ nguồn sai:)* Mục **4.11.1.2.3 STT 5 "Làm mới"**: *"…truy vấn lại dữ liệu với điều kiện lọc hiện tại để cập nhật kết quả mới nhất, **giữ nguyên các điều kiện lọc** và vị trí cuộn trang."* · **STT 6 "Xóa bộ lọc"**: *"…xóa toàn bộ giá trị đã nhập trong các trường lọc và đặt lại về giá trị mặc định (Kỳ = Tháng, Từ ngày = ngày đầu tháng hiện tại, Đến ngày = ngày hiện tại, Đơn vị = đơn vị đăng nhập, các trường khác = 'Tất cả'); khu vực kết quả không tự tải lại cho đến khi NSD bấm 'Xem báo cáo'."* |
| Trích `.md` | Chỉ có "Làm mới" (`:1046`). **Không có** "Xóa bộ lọc", **không có** bộ giá trị mặc định |
| Hướng | **A.** Tín hiệu mở đầu nghiêng về "bị sót" — "Xóa bộ lọc" có ở 8 nhóm FR khác trong bản gốc. Nhưng cây trọng tài bác tín hiệu đó: tầng 3 (màn hình ↔ xử lý) — `:1045-1058` liệt kê đủ 14 thành phần và **có rà tới thanh công cụ**, ở đó chọn "Làm mới"; bảng Processing chung (`:79-88`, 10 bước) không có bước nào đặt lại bộ lọc. Bộ mặc định `.docx` đòi không tồn tại ở đâu trong bản gốc nên không thể là thứ bị chép sót. Tầng 4 (CSV): UC124–146 chỉ 2 transaction |
| Dev action | **Không** |
| Doc action | Bên soạn tài liệu bàn giao — bản `.docx` kế tiếp: gỡ STT 6 mục 4.11.1.2.3, giữ STT 5 "Làm mới" |
| Sheet | **Resolve** (16 dòng) |

**→ Kết luận: Loại 4 hướng A — phần mềm đúng bản gốc. Màn Báo cáo thống kê giữ đúng một nút "Làm mới"; không bổ sung "Xóa bộ lọc" và không bổ sung bộ giá trị mặc định vào SRS. Dev action: Không → Sheet: Resolve, KHÔNG Reject.**

> **Phản hồi gửi đối tác** *(bản đã gửi 08/08 — khác Vấn đề 1 vì bản `.docx` 01/08 vốn đã đúng ở cụm này, không có gì phải sửa)*:
> Phần mềm đang đúng đặc tả. Bản SRS docx v3.5 bàn giao ngày 01/08/2026 không còn nút "Xóa bộ lọc" ở nhóm màn hình Báo cáo thống kê; màn hình chỉ có nút "Làm mới". Kính đề nghị Quý đơn vị cập nhật Kết quả mong đợi theo bản bàn giao 01/08/2026.

---

## Vấn đề 3 — Cụm Hợp đồng tư vấn: cả khối đứng vì test case mô tả lối vào đã bị bỏ (27 TC)

**Vấn đề:** Không một test case nào của màn Hợp đồng tư vấn chạy được. Bước đầu tiên của hầu hết test case là *"Chọn menu 'Hợp đồng Tư vấn'"* — mà menu đó không tồn tại, vì hợp đồng được mở từ trong hồ sơ vụ việc hoặc hồ sơ tư vấn viên. Người kiểm thử dừng ngay ở bước 1 nên toàn bộ các bước sau không thực hiện được.

**Mã trong cụm (Tuần 4):** `QLHDTVVCG_01` … `QLHDTVVCG_27`, dòng 1555–1581, **cả 27 dòng đều `N/R`**, ô Kết quả thực tế trống. Phiếu Dev chỉ nêu 12 mã và xếp vào diện "báo Fail nhưng chức năng đã có"; 15 mã còn lại cùng tình trạng và cùng một vật cản.

> ⚠️ **Đính chính 08/08 — cụm này đã được chạy lại và đánh số lại.** Khối còn **21 test case** (`_01`…`_21`), không còn 27. Trạng thái nay: **12 `Pass` · 6 `Fail` · 3 `N/R`** — tức vật cản lối vào đã được gỡ, phần lớn cụm chạy được. Đơn vị kiểm thử đã **bỏ hẳn** test case `↻ Xóa bộ lọc` (mã cũ `_06`), **gộp** 5 test case "Biểu mẫu chi tiết — Nhóm 1…5" (mã cũ `_08`…`_12`) thành một test case "Xem chi tiết hợp đồng", và **bỏ** test case "Thêm hợp đồng thành công" (mã cũ `_15`). Vấn đề 3 coi như đã khép.
>
> **Quy đổi mã cũ → mã hiện tại:** `_07`→`_06` · `_13`→`_07` · `_14`→`_08` · `_19`→`_09` · `_20`→`_10` · `_21`→`_11` · `_22`→`_12` · `_23`→`_13` · `_24`→`_14` · `_25`→`_15` · `_26`→`_16` · `_27`→`_17`. Mã cũ `_06`, `_08`…`_12`, `_15` không còn. Mã cũ `_16`/`_17`/`_18` được viết lại tên, nay là `_19`/`_21`/`_20`.

| Nhóm mã | Số mã | Bước 1 của test case | Vào được màn hình không |
|---|:-:|---|---|
| `_02` … `_21` | 20 | *"Chọn menu 'Hợp đồng Tư vấn'"* | Không — menu không tồn tại |
| `_22` … `_27` | 6 | *"Mở Nhóm N của biểu mẫu chi tiết"* | Không — vẫn phải mở được biểu mẫu chi tiết trước |
| `_01` | 1 | *(bỏ trống)* | Chính là dòng ghi nhận thiếu menu |

**(1) Phần mềm đúng SRS chưa? → ĐÚNG.** `srs-fr-14-hop-dong-tv.md:264`: *"Round 7 BA decision (2026-05-11): Route standalone `/hop-dong-tv/danh-sach` KHÔNG phải menu/màn hình nghiệp vụ public… không xuất hiện trong sidebar/menu, và không được QA coi là luồng chính. Luồng nghiệp vụ chính vẫn truy cập HĐ tư vấn từ ngữ cảnh Vụ việc hoặc TVV."*

**(1b) Bản `.docx` đối tác cầm có nói khác không? → CÓ, do thiếu chứ không do mâu thuẫn** — xem bảng Loại 4 bên dưới.

**(2) Đối tác yêu cầu khác SRS ở đâu? → Ở lối vào, không ở chức năng.** Ghi chú của người kiểm thử tại `QLHDTVVCG_01`: *"- SRS 10/7: Hiện chưa có nguyên mẫu giao diện (prototype) cho màn hình này. - Test 20/7: Màn hình chưa có menu cho chức năng này"*. Câu đầu là trích nguyên văn `.docx` mục 4.14.1.2.1; câu sau là kết quả thao tác thật.

**(3) Yêu cầu đó có bắt buộc cho luồng nghiệp vụ không? → KHÔNG.** Hai lối vào hiện có đã phủ đủ nhu cầu; các chức năng bên trong màn hình Dev đã đối chiếu là có, chỉ chưa ai vào tới để kiểm.

| Trường | Nội dung |
|---|---|
| Bản `.docx` đối chiếu | `HTPLDN-PTYC-CT-v3.5.docx` — xem đầu phiếu |
| Trích `.docx` | Mục **4.14.1.2** trình bày "Quản lý Hợp đồng Tư vấn" như một màn hình danh sách độc lập, có thanh công cụ riêng. Mục **4.14.1.2.1**: *"Hiện chưa có nguyên mẫu giao diện (prototype) cho màn hình này. Bản mô tả trường thông tin và chức năng dưới đây được lập theo đặc tả yêu cầu phần mềm (SRS)."* Tra toàn `section-4-fr-14`: **không có chữ nào** về route ẩn hay hai lối vào |
| Trích `.md` | `srs-fr-14-hop-dong-tv.md:264` — quyết định BA 11/05/2026, đã dẫn ở câu (1) |
| Hướng | **A** — `.docx` thiếu ghi chú của quyết định 11/05/2026 nên mô tả một lối vào đã hết hiệu lực. Tầng 1 (quyết định BA) giải quyết dứt điểm, không cần tra tiếp |
| Dev action | **Không** |
| Doc action | Bên soạn tài liệu bàn giao — bản `.docx` kế tiếp: bổ sung vào đầu mục 4.14.1 ghi chú hợp đồng tư vấn không có mục menu riêng, kèm hai lối vào |
| Sheet | **Giữ `N/R`** cả 27 dòng — chưa chạy nên chưa có ghi nhận nào để Resolve hay Reject |

**→ Kết luận: Loại 4 hướng A — quyết định BA ngày 11/05/2026 giữ nguyên, phần mềm đang làm đúng. Vật cản không phải "chức năng chưa có" cũng không phải "bản dựng cũ", mà là bộ test case mô tả một lối vào đã hết hiệu lực. Dev action: Không → Sheet: giữ `N/R` cả 27 dòng; ghi phản hồi vào dòng `QLHDTVVCG_01`, dùng chung cho cả khối.**

> **Phản hồi gửi đối tác:**
> *(Bản Dev chép lên sổ ngày 07/08 là bản dưới đây, viết theo nguồn `.docx` sai — nói "bản kế tiếp sẽ ghi rõ lối vào". Ngày 08/08 đã ghi đè bằng bản đúng, vì bản 01/08 vốn đã có sẵn ghi chú hai lối vào ở đầu nhóm 4.14.)*
>
> **Bản đã gửi (08/08):**
> Phần mềm đang đúng đặc tả. Hợp đồng tư vấn không có mục menu riêng — mở từ Chi tiết Vụ việc hoặc Chi tiết Tư vấn viên. Bản SRS docx v3.5 bàn giao ngày 01/08/2026 đã ghi rõ hai lối vào này ở đầu nhóm 4.14. Kính đề nghị Quý đơn vị cập nhật bước thực hiện của cả 27 test case QLHDTVVCG_01–_27 theo bản bàn giao 01/08/2026, rồi thực hiện kiểm thử.
>
> **Bản cũ (đã bị ghi đè):**
> **[Lý do]** Hợp đồng tư vấn không có mục menu riêng — đây là thiết kế, không phải chức năng còn thiếu. Hợp đồng luôn gắn với một vụ việc hoặc một tư vấn viên nên được mở ngay trong hồ sơ đó: **Chi tiết Vụ việc → mục "Hợp đồng tư vấn liên kết"**, hoặc **Chi tiết Tư vấn viên → thẻ "Lịch sử"**. ~~Bản SRS docx kế tiếp sẽ ghi rõ lối vào này.~~
> **[Nhận định]** Kính đề nghị Quý đơn vị sửa bước 1 của cả 27 test case `QLHDTVVCG_01`–`_27` từ *"Chọn menu Hợp đồng Tư vấn"* sang một trong hai lối vào trên, rồi thực hiện kiểm thử.

---

## Vấn đề 4 — `QLHDTVVCG_15` và `QLHDTVVCG_21`: câu thông báo sau khi lưu hợp đồng

> ⚠️ **Đính chính 08/08 — mã đã đổi.** `_15` "Thêm hợp đồng thành công" đã bị **bỏ khỏi sổ**; `_21` "Sửa thành công" nay là **`QLHDTVVCG_11`**, trạng thái `Pass`. Tra sổ theo nội dung test case, không theo mã.

**Vấn đề:** Test case chờ câu *"Đã lưu hợp đồng"*, phần mềm hiện báo *"Tạo hợp đồng thành công"* khi thêm mới và *"Cập nhật hợp đồng thành công"* khi chỉnh sửa.

**(1) Phần mềm đúng SRS chưa? → Bản gốc không quy định, và không có khuôn nào đủ áp đảo để suy ra.** Nhóm X.3 không đặc tả câu thông báo (`srs-fr-14:168-172` chỉ có 5 mã lỗi). Quét toàn bộ 18 file thì bản gốc dùng **cả hai khuôn lẫn lộn**, không có luật thành văn:

| Khuôn | Ví dụ trong bản gốc |
|---|---|
| "Đã + hành động + đối tượng" | `srs-fr-04:1555` *"Đã công nhận tư vấn viên"* · `srs-fr-07:599` *"Đã tạo hồ sơ doanh nghiệp…"* · `srs-v3.5.md:6726` *"Đã công khai {ten_doi_tuong}…"* |
| "… thành công" | `srs-fr-10:1011` *"Đăng xuất thành công"* · `srs-fr-10:1327` *"Đặt mật khẩu thành công…"* · `srs-fr-11:1058` *"Xuất thành công"* · `srs-fr-09:492` *"Import thành công {N} file…"* |
| Lai hai khuôn | `srs-fr-05:1590` *"**Đã lưu thành công**"* — tiền lệ gần ca này nhất |

Nên **không thể** kết luận phần mềm sai khuôn, cũng không thể kết luận `.docx` thừa. Đây là chỗ đặc tả im lặng thật, không có trọng tài nội tại.

**(1b) → ⚠️ Đính chính 08/08: KHÔNG.** Bản 01/08 **không có** chuỗi "Đã lưu hợp đồng" ở bất kỳ đâu, nên cơ sở "chốt lấy theo `.docx`" không còn. Kết luận vẫn giữ theo quyết định BA 06/08, và **`.docx` đã được bổ sung câu này ngày 08/08 cho khớp bản gốc**. *(Trích cũ, từ nguồn sai:)* Mục **4.14.1.2.3 STT 8 "Lưu"**, Trường hợp 1: *"Hợp lệ, hệ thống hiển thị thông báo **'Đã lưu hợp đồng'** và quay về danh sách."*

**(2) Đối tác yêu cầu khác SRS ở đâu? → Ở vế "quay về danh sách", không ở câu chữ.** Câu chữ họ ghi là đúng. Riêng vế *"quay về danh sách"* chọi với quyết định BA 11/05 ở Vấn đề 3 — hợp đồng không có màn danh sách độc lập để quay về.

**(3) Yêu cầu đó có bắt buộc cho luồng nghiệp vụ không? → Không bắt buộc, nhưng nên theo.** Câu thông báo không chặn luồng; tuy vậy để mỗi màn một khuôn thì người dùng đọc thấy hệ thống chắp vá.

| Trường | Nội dung |
|---|---|
| Bản `.docx` đối chiếu | `HTPLDN-PTYC-CT-v3.5.docx` — xem đầu phiếu |
| Trích `.docx` | Mục **4.14.1.2.3 STT 8**, Trường hợp 1: *"hệ thống hiển thị thông báo 'Đã lưu hợp đồng' và quay về danh sách"* |
| Trích `.md` | Nhóm X.3 **không đặc tả** câu thông báo (`srs-fr-14:168-172` chỉ có 5 mã lỗi). Bản gốc dùng cả hai khuôn, không có luật thành văn |
| Hướng | **B — bản gốc bị sót.** Không có căn cứ nội tại để chọn khuôn, nên **BA chốt 06/08/2026 lấy theo `.docx`**: đối tác đã cầm bản đó nên test case đạt ngay, khỏi phải sửa `.docx`, và khớp tiền lệ gần nhất `srs-fr-05:1590` *"Đã lưu thành công"* |
| Dev action | **Có** — sửa câu thông báo theo khuôn |
| Doc action | Chỉ sửa vế *"và quay về danh sách"* thành *"và quay về ngữ cảnh đã mở biểu mẫu"*. **Câu chữ thông báo giữ nguyên — `.docx` đúng** |
| Sheet | **Giữ `N/R`** — chưa chạy (xem Vấn đề 3) |

**→ Kết luận: Loại 4 hướng B — bản gốc bị sót, bổ sung đặc tả rồi Dev sửa. **BA chốt 06/08/2026: lấy câu theo `.docx` — *"Đã lưu hợp đồng"*.** Kết quả mong đợi của đơn vị kiểm thử **viết đúng, không phải sửa**. Dev action: Có → Sheet: giữ `N/R`.**

### Phương án xử lý (cập nhật SRS)

- `srs-fr-14-hop-dong-tv.md:166-172` — bảng Error Handling của `FR-X.3-01` thêm một dòng mức INFO: `INF-HDTV-01` *"Đã lưu hợp đồng"*, dùng chung cho cả thêm mới lẫn chỉnh sửa đúng như `.docx` mô tả. Đã tra va chạm mã: `INF-HDTV-01/02` chưa dùng ở đâu (`INF-HDTV-TK-01` của FR tìm kiếm là mã khác).
- Ghi chú dưới bảng: vì nhóm X.3 không có màn danh sách độc lập nên "quay về ngữ cảnh đã mở biểu mẫu" là biến thể hợp lệ của Phụ lục E §H7.
- Thêm một dòng Tiêu chí chấp nhận cho hai luồng lưu.

**Đề nghị mở một mục riêng ở đợt sau — chuẩn hóa câu thông báo thành quy ước.** Bản gốc đang dùng lẫn lộn hai khuôn ở hơn 100 chỗ mà **không có luật thành văn**, nên mỗi lần tranh chấp lại phải đi đếm tiền lệ và vẫn không ra kết luận. Đưa vào Phụ lục E một dòng chốt khuôn là dứt điểm. Ngoài phạm vi hai phiếu Dev nên phiếu này không quyết.

*Phạm vi mục này chỉ là câu thông báo và vế "quay về danh sách" — đúng phần Dev đưa ra hỏi. Các ý con còn lại trong Kết quả mong đợi của `QLHDTVVCG_15` (sinh mã `HDTV-{YYYYMMDD}-{SEQ}`, tạo bản ghi kèm mốc tiến độ / thanh toán / liên kết vụ việc / tệp đính kèm, gán trạng thái "Đang thực hiện") **đều có căn cứ ở `srs-fr-14:119-123`, không tranh chấp** — chờ chạy để đo.*

---

## Vấn đề 5 — `QLHDTVVCG_22`: cửa sổ liên kết vụ việc chỉ với tới 100 vụ việc đầu

> ⚠️ **Đính chính 08/08 — mã đã đổi.** Test case "Liên kết vụ việc" nay là **`QLHDTVVCG_12`**, trạng thái `Pass`. Mã `_22` hiện không còn trong khối.

**Vấn đề:** Khi gắn vụ việc vào hợp đồng, cửa sổ chọn chỉ nạp 100 vụ việc đầu rồi lọc trong phạm vi 100 bản ghi đó. Đơn vị nào có hơn 100 vụ việc thì cán bộ không tìm được vụ việc thứ 101 trở đi — gõ đúng mã cũng không ra, và không có dấu hiệu nào báo cho người dùng biết đang bị cắt.

| Số vụ việc của đơn vị | Thao tác | Kết quả |
|---|---|---|
| 49 (dữ liệu kiểm thử hiện tại) | gõ mã vụ việc bất kỳ | Tìm được — lỗi chưa lộ |
| 120 | gõ mã của vụ việc thứ 30 | Tìm được |
| 120 | gõ mã của vụ việc thứ 105 | **Không ra kết quả**, không có cảnh báo |
| 120 | gõ tên doanh nghiệp của vụ việc thứ 10 | **Không ra kết quả** — từ khóa chưa phủ tên doanh nghiệp |

**(1) Phần mềm đúng SRS chưa? → SAI.** Bản gốc yêu cầu tìm được vụ việc theo mã **và** theo tên doanh nghiệp:
- `srs-fr-05-vu-viec.md:402` — ô `keyword`: *"Từ khóa tìm kiếm (mã hồ sơ, tên DN, HT nguồn)"*
- `srs-fr-05-vu-viec.md:667` — Processing bước 3: *"Tìm từ khóa trên **mã VV, tên DN**"*
- `srs-fr-14-hop-dong-tv.md:287` (SCR-X3-01) — *"Nút [+ Liên kết VV] -> modal multi-select. N:N"*
- `srs-fr-14-hop-dong-tv.md:526` (BR-DATA-07) — *"Mọi danh sách sử dụng phân trang. Default: 20 rows/page, **max: 100 rows/page**"*. Đây là trần **một trang**, không phải trần số bản ghi với tới được. Việc Dev chặn `pageSize` ở 100 là đúng quy tắc; cái sai là nạp đúng một trang rồi lọc trong phạm vi đó, không phân trang và không tìm phía máy chủ — nên vụ việc thứ 101 trở đi không có đường nào chạm tới.

**(1b) Bản `.docx` đối tác cầm có nói khác không? → Có thêm một vế, không mâu thuẫn.** Mục **4.14.1.2.3 STT 10**: ô tìm kiếm *"theo mã vụ việc, tên doanh nghiệp hoặc lĩnh vực"*. Vế "lĩnh vực" bản gốc không có — không bắt buộc, làm được thì tốt.

**(2) Đối tác yêu cầu khác SRS ở đâu? → Không khác.** Kết quả mong đợi trùng bản gốc ở hai vế mã vụ việc và tên doanh nghiệp.

**(3) Yêu cầu đó có bắt buộc cho luồng nghiệp vụ không? → CÓ.** Không liên kết được vụ việc thì hợp đồng tư vấn mất mối nối với hồ sơ vụ việc — hỏng luồng, không phải bất tiện.

**→ Kết luận: Loại 1 — Lỗi phần mềm, Dev sửa theo SRS: cửa sổ liên kết vụ việc phải tìm và chọn được **mọi** vụ việc trong phạm vi quyền của người dùng, không dừng ở 100 bản ghi đầu; từ khóa phải phủ **mã vụ việc và tên doanh nghiệp** theo `srs-fr-05:667`. Việc mở rộng từ khóa sang tên doanh nghiệp là đưa mã nguồn về đúng bản gốc, không phải yêu cầu mới nên không cần BA duyệt đổi giao kèo API; cách làm do Dev tự thiết kế. Không sửa SRS. Dev action: Có → Sheet: giữ `N/R` — Dev sửa trước, đơn vị kiểm thử chạy sau.**

---

## Vấn đề 6 — `QLDXDTTH_07`: xóa đề xuất đào tạo đã tiếp nhận

**Vấn đề:** Test case chờ thấy hộp xác nhận rồi thông báo từ chối *"Đề xuất đã tiếp nhận không thể xóa"*. Thực tế người dùng không thấy nút Xóa nên không có hộp xác nhận nào. Nhưng test case này chưa chạy được, vì lý do khác hẳn.

**(1) Phần mềm đúng SRS chưa? → ĐÚNG, và bản gốc có đủ cả hai vế.**
- `srs-fr-03-dao-tao.md:1076` — *"Sửa: chỉ khi MOI. **Xóa: chỉ khi MOI**, xóa mềm."* → nút chỉ hiện với đề xuất "Mới"
- `srs-fr-03-dao-tao.md:1082` — *"Error Handling: … **ERR-DX-03 'Đề xuất đã tiếp nhận không thể xóa'**"* → chốt chặn cho yêu cầu xóa gửi tới hệ thống ngoài đường giao diện
- `srs-fr-03-dao-tao.md:1086` — *"Given CB NV xóa đề xuất When đề xuất chưa tiếp nhận Then xóa mềm"*

**(1b) Bản `.docx` đối tác cầm có nói khác không? → KHÔNG — nói y hệt.** Mục **4.3.13.2.2 STT 3 "Xóa đề xuất"** ghi điều kiện hiển thị là trạng thái "Mới", kèm *"Trường hợp 2: Đề xuất đã tiếp nhận, hệ thống từ chối và hiển thị thông báo 'Đề xuất đã tiếp nhận không thể xóa'"*. Đúng hai vế mà bản gốc có ở `:1076` và `:1082`. **Không phải tranh chấp lệch tài liệu.**

**(2) Đối tác yêu cầu khác SRS ở đâu? → Ở giả định nút Xóa hiển thị.** Kết quả mong đợi chờ một hộp xác nhận rồi mới tới thông báo từ chối — tức giả định bấm được nút. Cả hai tài liệu đều đặt điều kiện hiển thị là trạng thái "Mới", nên với đề xuất đã tiếp nhận thì không có nút để bấm; `ERR-DX-03` là chốt chặn phía máy chủ, không phải bước người dùng nhìn thấy.

**(3) Yêu cầu đó có bắt buộc cho luồng nghiệp vụ không? → KHÔNG.** Ẩn nút chặn thao tác sớm hơn và an toàn hơn là cho bấm rồi báo lỗi.

**→ Kết luận: case lai.**

- **Ý chính — Loại 3:** phần mềm đúng cả bản gốc lẫn tài liệu bàn giao; đề nghị đơn vị kiểm thử cập nhật Kết quả mong đợi. Không sửa SRS, **không có Doc action** — `.docx` không sai.
- **Ý con — Loại 1, chưa xác minh:** ghi nhận của đơn vị kiểm thử *"Bản ghi không cập nhật trạng thái mặc dù Cán bộ nghiệp vụ đã phê duyệt trạng thái thành 'Đã tiếp nhận'"* — đây là vật cản khiến test case không chạy được (dòng 336, `Đang Phát Triển`, Kết quả thực tế trống; mã này nằm trong danh sách 102 test case Tuần 2 chưa chạy tại `tuan2-N_R.csv`). **Dev phải dựng lại đúng tình huống — tạo một đề xuất, cho cán bộ nghiệp vụ phê duyệt thành "Đã tiếp nhận", rồi xem trạng thái trên màn hình có đổi không. Nếu lỗi lặp lại thì đây là lỗi phần mềm, Dev phải sửa** — không xếp sang diện "quan sát về dữ liệu" rồi bỏ qua như phiếu Dev đang làm. Nếu làm lại mà không thấy lỗi thì phải trả lời kèm bằng chứng là ảnh hoặc video các bước phê duyệt và trạng thái sau đó, không kết luận suông.

**Dev action: Có — dựng lại tình huống để kiểm chứng, và sửa nếu lỗi lặp lại → Sheet: `InProcess` `[BA chốt 2026-08-06]`.** Phần tranh chấp về nút Xóa đã khép và đã phản hồi đối tác, nhưng ý con "phê duyệt xong trạng thái không đổi" Dev còn phải xử — nên dòng này để đang xử lý, không đóng.

> **Phản hồi gửi đối tác:**
> **[Lý do]** Đề xuất chỉ xóa được khi ở trạng thái "Mới"; đã tiếp nhận thì nút "Xóa" không hiển thị nên không có hộp xác nhận. Câu *"Đề xuất đã tiếp nhận không thể xóa"* là chốt chặn phía máy chủ cho yêu cầu gửi tới hệ thống ngoài đường giao diện, không phải bước người dùng nhìn thấy.
> **[Nhận định]** Kính đề nghị Quý đơn vị sửa Kết quả mong đợi `QLDXDTTH_07` thành *"Đề xuất đã tiếp nhận không hiển thị nút Xóa"*, tương tự `QLDXDTTH_05` với nút "Sửa". Riêng ghi nhận *"phê duyệt xong trạng thái không đổi"* — chúng tôi ghi nhận là lỗi và xử lý.

---

## Vấn đề 7 — `QLCHTHXLHS_09`: câu thông báo lưu cấu hình thời hạn xử lý

**Vấn đề:** Phiếu Dev đưa mã này ra hỏi BA có nên chuẩn hóa câu thông báo không. Test case này đã đạt.

**(1) Phần mềm đúng SRS chưa? → ĐÚNG, và đã được đo.** Dòng 1027, `Trạng thái` = **`Pass`**. Ô Kết quả thực tế ghi *"Hệ thống lưu thành công và hiển thị thông báo 'Đã lưu cấu hình thời hạn xử lý thành công'"* — **trùng khít Kết quả mong đợi**.

**(1b) Bản `.docx` có nói khác không? → Không đặt ra.** Không có chênh lệch nào giữa mong đợi và thực tế để mà tranh chấp.

**(2) Đối tác yêu cầu khác SRS ở đâu? → Không khác.** Ghi chú của Dev *"TC QLCHTHXLHS_07 lỗi nên test sau"* trỏ sang một dòng khác (dòng 1025), đang `Fail` với nội dung khác hẳn — thiếu trường "Số ngày bổ sung tối đa", đơn vị kiểm thử chạy lại 31/07 vẫn lỗi. Không liên quan tới `_09`.

**(3) Yêu cầu đó có bắt buộc cho luồng nghiệp vụ không? → Không đặt ra.** Không có yêu cầu nào đang treo.

**→ Kết luận: không có vấn đề — test case đã đạt, không có tranh chấp nào để BA quyết. Không mở quy ước câu thông báo vào Phụ lục E cho tình huống này vì chưa có ca lỗi thật nào đòi hỏi. Dev action: Không → Sheet: giữ nguyên `Pass`, không đụng dòng.**

---

## Vấn đề 8 — `CPCTHTTLV_01`: báo cáo chi phí theo lĩnh vực không có số liệu

**Vấn đề:** Màn hình báo cáo chi phí theo lĩnh vực chạy được nhưng không ra số nào, do môi trường kiểm thử chưa có dữ liệu chi trả nào thuộc lĩnh vực đó.

**(1) Phần mềm đúng SRS chưa? → Chưa đo được.** Dòng 1351, `Trạng thái` = **`Đang Phát Triển`**; Kết quả thực tế: *"Chưa có dữ liệu test"*; ghi chú người kiểm thử: *"Chưa có dữ liệu test - A/c thêm giữ liệu giúp e vs ạ"*. Đây là lời đề nghị bổ sung dữ liệu, không phải báo lỗi chức năng.

**(1b) Bản `.docx` có nói khác không? → Không đặt ra.** Chưa có chênh lệch nào để đối chiếu.

**(2) Đối tác yêu cầu khác SRS ở đâu? → Không khác.** Kết quả mong đợi bám đúng bản gốc.

**(3) Yêu cầu đó có bắt buộc cho luồng nghiệp vụ không? → Không đặt ra.**

**→ Kết luận: không phải lỗi phần mềm, và cũng không phải việc của phía mình. Môi trường UAT (`htpldn-uat.ospgroup.vn`) do OSP dựng và đơn vị kiểm thử chạy trên đó, nên dữ liệu kiểm thử trên môi trường này thuộc trách nhiệm OSP. Chuyển OSP bổ sung dữ liệu chi trả có gắn lĩnh vực pháp lý, rồi đơn vị kiểm thử chạy lại. Dev action: Không → Sheet: giữ nguyên `Đang Phát Triển`.**

*Áp chung cho mọi test case dừng vì "chưa có dữ liệu test": môi trường kiểm thử là của OSP, phía mình không dựng dữ liệu hộ. Chỉ nhận phần lỗi phần mềm.*

---

## Vấn đề 9 — Ba điểm Dev tự khép bằng tài liệu: xác nhận đúng

**Vấn đề:** Dev báo đã tự xử lý ba điểm dựa vào tài liệu và chỉ xin BA phản đối nếu sai. Đã kiểm lại cả ba, đều đúng.

**(1) Phần mềm đúng SRS chưa? → Cả ba điểm đều có căn cứ tài liệu rõ:**
- **Cột "Trạng thái" bảng vụ việc liên kết hiện mã thô** (`DA_TIEP_NHAN` thay vì "Đã tiếp nhận"): `srs-fr-05-vu-viec.md:1500` và `:2268` đều có sẵn bảng ánh xạ trạng thái sang tiếng Việt kèm màu. Lỗi rõ, Dev đã sửa bằng bảng ánh xạ dùng chung.
- **Tra doanh nghiệp của tài khoản theo mã số thuế thay vì theo thư điện tử:** đúng — thư điện tử được phép đổi độc lập sau khi đăng ký nên tra theo thư có thể trả nhầm doanh nghiệp khác; tên đăng nhập của doanh nghiệp là mã số thuế.
- **Tìm kiếm phải bỏ dấu:** `srs-v3.5.md:6712` (Phụ lục E §H5, BẮT BUỘC) — *"Mọi dropdown có ≥10 lựa chọn phải hỗ trợ tìm kiếm bằng cách gõ (autocomplete) với so khớp tương đối (chứa chuỗi, không phân biệt hoa thường, hỗ trợ bỏ dấu tiếng Việt)"*.

**(1b)(2)(3) → Không đặt ra.** Không có chênh lệch nào giữa Dev và tài liệu để phân xử.

**→ Kết luận: cả ba điểm khép đúng, BA không có ý kiến khác. Dev action: Không còn việc của BA → Sheet: không đụng dòng nào — các điểm này không gắn mã test case riêng đang mở.**

---

# Phần II — Lô 10 bug N/R + Open

- **Phiếu nguồn:** `Week5/Yêu cầu/phan-hoi-ba-lo-10-bug-NR-OPEN-2026-08-05.md` · bản dựng thẩm định `V1.0.8`
- **Trạng thái trên sổ KTĐL, bản tải 06/08/2026:** `QLDX_04` (dòng 1189) · `QLDX_05` (1190) · `QLDX_06` (1191) · `QLNDTVVCG_39` (1446) đều `Fail` với ô Kết quả thực tế **trống**; `TPDBCKQTHCT_02` (1616) và `THBCTHCT_05` (1621) là `N/R`.

---

## Vấn đề 10 — Cụm `QLDX_04/05/06`: đồng hồ phiên làm việc 30 phút (3 TC)

**Vấn đề:** Để máy 25 phút thì phải hiện hộp thoại báo sắp hết phiên, để tiếp đến phút 30 thì bị đưa về trang đăng nhập. Nhưng nếu lúc đăng nhập người dùng tích ô "Ghi nhớ đăng nhập" thì toàn bộ cơ chế này tắt hẳn — không cảnh báo, không tự đăng xuất, phiên mở vô thời hạn. Máy dùng chung ở cơ quan bỏ đó là người khác mở được hồ sơ. Đây nhiều khả năng cũng là lý do đơn vị kiểm thử ghi Fail cả ba mã: họ chờ 25 phút mà không thấy gì xảy ra.

| Tình huống | Mốc không thao tác | Hành vi đúng | Hành vi hiện tại |
|---|---|---|---|
| Không tích "Ghi nhớ đăng nhập" | 25 phút | Hiện hộp thoại cảnh báo | Đúng |
| Không tích | 30 phút | Tự đăng xuất, về trang đăng nhập | Đúng |
| **Có tích** | 25 phút | Hiện hộp thoại cảnh báo | **Không hiện gì** |
| **Có tích** | 30 phút | Tự đăng xuất | **Không đăng xuất, phiên mở vô hạn** |
| Có tích, đã đăng xuất, mở lại sau 12 giờ | — | Không phải nhập lại tài khoản và mật khẩu | Đúng |

**(1) Phần mềm đúng SRS chưa? → SAI ở chỗ tắt đồng hồ.** Hai quy định BẮT BUỘC, không có mệnh đề ngoại lệ nào:
- `srs-v3.5.md:4498` (SEC-03) — *"Timeout phiên đăng nhập: 30 phút không hoạt động"*
- `srs-v3.5.md:5482` (BR-AUTH-06) — *"Session CMS: 30 phút idle timeout. API token xác thực: TTL 15 phút, refresh token 24 giờ. Redirect về trang đăng nhập khi hết hạn"*
- `srs-fr-10-quan-tri.md:1884` — *"Ghi nho dang nhap | checkbox | Extend session TTL"*: nói kéo dài, không nói kéo dài **cái nào** trong ba mốc trên.

**(1b) Bản `.docx` đối tác cầm có nói khác không? → Không — còn giải nghĩa rõ hơn và bác cách hiểu hiện tại.** Mục **4.10.7.2 STT 5**: *"Khi bật, hệ thống ghi nhớ phiên đăng nhập trên máy tính/thiết bị đang dùng để lần tiếp theo vào hệ thống **không cần nhập lại tên đăng nhập và mật khẩu** trong thời gian hiệu lực."* Mục **4.10.7.4 STT 2**: hộp thoại cảnh báo hiện *"khi NSD không thao tác suốt 25 phút"* — không kèm ngoại lệ nào.

**(2) Đối tác yêu cầu khác SRS ở đâu? → Không khác.** Kết quả mong đợi của cả ba mã trùng khít bản gốc lẫn `.docx`. Ba mã khác nhau ở chi tiết: `_04` nhãn nút hiện *"Tiếp tục đăng nhập"* trong khi bản gốc ghi `[Gia han]` (`srs-fr-10:1891`) và `.docx` ghi *"Gia hạn phiên"*; `_05` hành vi gia hạn đúng Kết quả mong đợi; `_06` câu thông báo sau khi hết phiên chưa đúng.

**(3) Yêu cầu đó có bắt buộc cho luồng nghiệp vụ không? → CÓ.** Đây là hàng rào bảo mật phiên làm việc, không phải tiện lợi.

**→ Kết luận: Loại 1 — Lỗi phần mềm, Dev sửa theo SRS. Đồng hồ nghỉ 30 phút áp cho **mọi** phiên kể cả khi tích "Ghi nhớ đăng nhập"; ô đó chỉ quyết định lần đăng nhập kế tiếp có phải nhập lại tài khoản và mật khẩu hay không. Kèm theo: sửa nhãn nút (`_04`) và câu thông báo hết phiên (`_06`). Không Reject `QLDX_05` — Kết quả mong đợi viết đúng và phần mềm làm đúng vế đó, chờ bản sửa lên rồi kiểm lại. Không sửa SRS. Dev action: Có → Sheet: cả 3 dòng giữ nguyên trạng thái đang xử lý.**

*Căn cứ của kết luận là SEC-03 và BR-AUTH-06 — hai điều BẮT BUỘC, không có mệnh đề ngoại lệ nào cho phép tắt đồng hồ nghỉ. Việc "Extend session TTL" ứng với mốc làm mới 24 giờ của BR-AUTH-06 là **suy luận** từ cách `.docx` giải nghĩa ô này, không phải câu chữ trong bản gốc; nếu Dev cho rằng phải hiểu khác thì vẫn không đổi kết luận, vì bản gốc không cho tắt đồng hồ nghỉ ở bất kỳ cách hiểu nào.*

---

## Vấn đề 11 — `QLNDTVVCG_39`: phân công chuyên gia hàng loạt khi có dòng khác "Tiếp nhận"

**Vấn đề:** Cán bộ tích chọn nhiều yêu cầu tư vấn chuyên sâu rồi bấm phân công hàng loạt, trong đó có yêu cầu đã sang giai đoạn đang tư vấn. Hệ thống chặn lại. Test case lại chờ hệ thống mở cửa sổ phân công và gán chuyên gia cho tất cả.

**(1) Phần mềm đúng SRS chưa? → ĐÚNG.** `srs-fr-12-tv-chuyen-sau.md:1114` (SCR-XII-01 dòng 12): *"[Phân công CG hàng loạt] **(chỉ bản ghi TIEP_NHAN)**… nút enable theo trạng thái dòng được chọn"*.

**(1b) Bản `.docx` đối tác cầm có nói khác không? → KHÔNG — nói y hệt, còn chi tiết hơn.** Mục **4.12.1.2.3 STT 9**: *"Điều kiện hiển thị: NSD đã chọn ít nhất 1 dòng bằng ô chọn; **các dòng được chọn đều ở trạng thái 'Tiếp nhận'**. **Nếu có dòng ở trạng thái khác, hệ thống hiển thị thông báo 'Chỉ có thể phân công hàng loạt với các yêu cầu đang ở trạng thái Tiếp nhận'**. NSD bấm nút 'Phân công hàng loạt', hệ thống mở cửa sổ phân công, áp dụng chuyên gia đã chọn cho tất cả yêu cầu được chọn đồng thời."*

**(2) Đối tác yêu cầu khác SRS ở đâu? → Ở chỗ chép thiếu.** Kết quả mong đợi là **nửa sau** của đúng ô này, bỏ mất nửa đầu — trong khi cả hai vế nằm chung một ô. Không phải tranh chấp lệch tài liệu.

**(3) Yêu cầu đó có bắt buộc cho luồng nghiệp vụ không? → KHÔNG, và còn có hại.** Yêu cầu đã sang đang tư vấn nghĩa là chuyên gia đã nhận việc; ghi đè hàng loạt sẽ gạt chuyên gia đang làm dở ra khỏi hồ sơ và phá vòng đời trạng thái.

**→ Kết luận: Loại 3 — phần mềm đúng cả bản gốc lẫn tài liệu bàn giao; đề nghị đơn vị kiểm thử cập nhật Kết quả mong đợi. Không sửa SRS. Dev action: Không → Sheet: Reject.**

> **Phản hồi gửi đối tác:**
> **[Lý do]** Phân công hàng loạt chỉ áp dụng cho yêu cầu ở trạng thái "Tiếp nhận". Yêu cầu đã sang "Đang tư vấn" nghĩa là chuyên gia đã nhận việc; gán đè hàng loạt sẽ thay người đang xử lý mà không qua bước thu hồi. Điều kiện này và câu chặn tương ứng đã có tại mục 4.12.1.2.3 của SRS docx.
> **[Nhận định]** Kính đề nghị Quý đơn vị cập nhật Kết quả mong đợi thành: hệ thống không mở cửa sổ phân công và báo chỉ phân công hàng loạt được các yêu cầu ở trạng thái "Tiếp nhận".

---

## Vấn đề 12 — `TPDBCKQTHCT_02`: "báo cáo hoàn chỉnh" nghĩa là gì

**Vấn đề:** Cán bộ Sở lập báo cáo định kỳ theo biểu mẫu Thông tư 17/2025 rồi bấm trình phê duyệt. Hệ thống có cổng chặn "báo cáo chưa hoàn chỉnh", nhưng hiện chỉ kiểm tra xem phần số liệu có rỗng hoàn toàn không — nên một báo cáo mới điền 3 ô trên tổng số 13 chỉ tiêu vẫn trình lên được. Cấp trên nhận về bản không dùng được để tổng hợp, phải trả lại, mất một vòng.

| Tình huống | Số liệu đã nhập | Trình phê duyệt được? |
|---|---|---|
| Điền đủ 13 chỉ tiêu, có số dương | đầy đủ | Được |
| Điền đủ 13 chỉ tiêu, tất cả bằng 0 | đơn vị không phát sinh hoạt động trong kỳ | Được |
| Chỉ điền 3 ô, 10 chỉ tiêu bỏ trống | `{soVuViec: 3, tongChiPhi: 0, soDnDuocHoTro: 0}` — dữ liệu thật đang có trên 120 | Không |
| Không nhập ô nào | trống | Không |
| Đủ 13 chỉ tiêu, bỏ trống "Nhận xét, kiến nghị" | đầy đủ số liệu | Được |

**(1) Phần mềm đúng SRS chưa? → SRS thiếu.** Có cổng chặn nhưng không định nghĩa thế nào là hoàn chỉnh:
- `srs-fr-15-ct-htpldn.md:802` — Processing bước 2: *"Kiểm tra BC hoàn chỉnh"*
- `srs-fr-15-ct-htpldn.md:825` — *"E1 | BC chưa hoàn chỉnh | ERR-XI-07-01 | 'Vui lòng hoàn chỉnh BC trước khi trình'"*
- `srs-fr-15-ct-htpldn.md:731`, `:733` — `so_lieu` bắt buộc (Y), `nhan_xet` không bắt buộc (N).

**(1b) → CÓ, nhưng ở cổng khác.** ⚠️ **Đính chính 08/08:** chuỗi *"đầy đủ số liệu bắt buộc"* nằm ở **mục 4.15.7.2.3**, và đó là cổng chặn lúc **Lưu nháp** (`ERR-XI-06-01`), không phải lúc Trình phê duyệt. Bản 01/08 **không có** bước "Trình phê duyệt báo cáo" riêng. Kết luận Loại 2 vẫn đứng — bản gốc thiếu định nghĩa là thật, và 13 chỉ tiêu đã đối chiếu với biểu mẫu 21a gốc. *(Trích cũ, từ nguồn sai:)* Mục **4.15.x STT 2**: *"Kiểm tra báo cáo **đầy đủ số liệu bắt buộc theo biểu mẫu áp dụng**"* — tức đủ chỉ tiêu của biểu mẫu đơn vị đã chọn.

**(2) Đối tác yêu cầu khác SRS ở đâu? → Không khác, chỉ là bản gốc im lặng.** Đối chiếu biểu mẫu gốc `docs/Input/Mau_21a_So_ban_nganh.csv`: biểu 21a/TP/HTPLDN ban hành kèm TT 17/2025 đánh số cột **-1 đến -13**, tức đúng **13 chỉ tiêu**, khớp danh sách trong phiếu Dev.

**(3) Yêu cầu đó có bắt buộc cho luồng nghiệp vụ không? → CÓ.** Không có định nghĩa thì cổng chặn vô nghĩa, báo cáo trắng vẫn lọt lên cấp trên.

**→ Kết luận: Loại 2 — bổ sung định nghĩa vào SRS, Dev làm theo. "Hoàn chỉnh" = có mặt đủ các chỉ tiêu của biểu mẫu đơn vị đã chọn. Dev action: Có → Sheet: giữ nguyên `N/R`.**

**Dev action cụ thể — 4 việc:**
1. Cổng chặn khi bấm "Trình phê duyệt" kiểm **đủ chỉ tiêu của biểu mẫu tại `bieu_mau_su_dung`**: `MAU_21A` → 13 chỉ tiêu biểu 21a; `MAU_21B` → theo biểu 21b; `CA_HAI` → cả hai biểu.
2. Ô để trống tính là **chưa điền** → chặn. **Giá trị 0 tính là đã điền** → cho qua; đơn vị không phát sinh hoạt động trong kỳ vẫn phải nộp báo cáo định kỳ.
3. **"Nhận xét, kiến nghị" không tính vào điều kiện** — bỏ trống vẫn trình được.
4. Câu chặn dùng đúng mã `ERR-XI-07-01` với nội dung *"Vui lòng hoàn chỉnh báo cáo trước khi trình"* — viết đủ chữ "báo cáo", không viết tắt "BC" như bản gốc đang ghi.

### Phương án xử lý (cập nhật SRS)

- `srs-fr-15-ct-htpldn.md:802` — bước 2 viết rõ: *"Kiểm tra BC hoàn chỉnh: đủ toàn bộ chỉ tiêu của biểu mẫu tại `bieu_mau_su_dung` (MAU_21A → 13 chỉ tiêu biểu 21a; MAU_21B → theo biểu 21b; CA_HAI → cả hai biểu). Ô để trống là chưa điền; giá trị 0 là đã điền. `nhan_xet` không tính vào điều kiện này."*
- `srs-fr-15-ct-htpldn.md:825` — mã `ERR-XI-07-01` giữ nguyên, sửa nội dung thông báo từ *"Vui lòng hoàn chỉnh BC trước khi trình"* thành *"Vui lòng hoàn chỉnh báo cáo trước khi trình"* để khớp tài liệu bàn giao và Kết quả mong đợi của test case — viết tắt "BC" chỉ dùng trong đặc tả, không dùng trên giao diện.
- Bổ sung một dòng Tiêu chí chấp nhận: *"Given báo cáo còn chỉ tiêu bỏ trống When CB NV bấm Trình phê duyệt Then chặn + báo `ERR-XI-07-01`"*.
- **Đồng bộ cụm "BC hoàn chỉnh" ở 2 chỗ còn lại của chính FR-XI-07:** `srs-fr-15:782` (Mô tả) và `:829` (Tiêu chí chấp nhận hiện có) — cùng dùng cụm này mà chưa trỏ về định nghĩa mới.
- **Đồng bộ máy trạng thái — 2 bản sao:** `srs-v3.5.md:6207` và `srs-fr-15-ct-htpldn.md:1511` cùng ghi chuyển `DANG_LAP_BC → CHO_DUYET_KQ` với điều kiện **"BC đầy đủ số liệu"**. Đây là cùng một cổng chặn với `:802` nhưng gọi bằng cụm khác — sửa cả hai dòng trỏ về định nghĩa "hoàn chỉnh" mới, nếu không sẽ tồn tại hai cách hiểu.
- **Không nhầm với cổng lúc lưu:** `srs-fr-15:764` có `ERR-XI-06-01` *"Vui lòng nhập đầy đủ số liệu bắt buộc"* thuộc FR-XI-06 (lập báo cáo). Đó là kiểm lúc **lưu**, khác cổng lúc **trình phê duyệt** đang bàn ở đây; định nghĩa mới chỉ áp cho cổng trình phê duyệt.

**Điểm treo phát hiện khi rà — nợ có sẵn từ STT 52, cần dọn ở đợt riêng, không chặn phiếu này.** Quyết định STT 52 (UAT 2026-05-26) đã chuyển đợt báo cáo thành **độc lập với chương trình**; `srs-fr-15` đã áp, nhưng **baseline chưa sync** ở 3 chỗ:

| Chỗ chưa sync | Đang ghi | Đã chốt ở `srs-fr-15` |
|---|---|---|
| `srs-v3.5.md:2174`, `:2176` (entity `DOT_BAO_CAO`) | `ma_dot` = `DOT-{CT_ID}-{SEQ}`; `chuong_trinh_id` **bắt buộc** | `:623` — *"đợt báo cáo không còn gắn cứng `chuong_trinh_id`"* |
| `srs-v3.5.md:4430` (ERD) | `CHUONG_TRINH_HTPL \|\|--o{ DOT_BAO_CAO : "co_dot_bc"` | `:1307` — *"bỏ liên kết CHUONG_TRINH_HTPL ||--o{ DOT_BAO_CAO"* |
| `srs-v3.5.md:6205` và `srs-fr-15:1509` (SM, dòng tạo đợt) | guard *"CT ở DANG_THUC_HIEN/HOAN_THANH"* | `:655` — *"**BỎ kiểm tra trạng thái CT (STT 52)** — đợt BC độc lập với CT"* |

Ba chỗ này **không phải do phương án trên gây ra** — đã lệch từ 26/05. Nhưng dòng SM `srs-v3.5.md:6207` mà phương án sẽ sửa nằm **ngay dưới** dòng `:6205` đang sai, nên người áp sẽ nhìn thấy; ghi ra đây để không sửa nửa vời rồi tưởng bảng đã sạch.

**Doc action: KHÔNG có — bản `.docx` giữ nguyên.** Đây là mục duy nhất trong phiếu mà `.docx` đúng còn bản gốc thiếu, nên chỉ sửa một chiều `.md` cho khớp `.docx`. Ghi rõ để lượt sau không ai "sửa" nhầm bản `.docx`.

---

## Vấn đề 13 — `THBCTHCT_05` (phần 1): tên tệp xuất báo cáo tổng hợp

**Vấn đề:** Tệp báo cáo tổng hợp toàn quốc xuất ra phải đặt tên theo khuôn nào — bản gốc bỏ trống, tài liệu bàn giao ghi một chuỗi cụ thể, mà chuỗi đó lại khác hình thức với mọi tên tệp còn lại của hệ thống.

**(1) Phần mềm đúng SRS chưa? → SRS thiếu.** `srs-fr-15-ct-htpldn.md:1016` chỉ ghi *"File xuất | Excel (.xlsx) / Word (.docx) theo TT17"*. Tra toàn thư mục `srs-v3.5/`: không có tên tệp nào cho Nhóm XI.

**(1b) → ⚠️ Đính chính 08/08: KHÔNG.** Bản 01/08 **không đặc tả tên tệp ở bất kỳ đâu** trong cả tài liệu. Cơ sở "lấy theo `.docx`" không còn — nhưng §H8 vẫn đứng bằng lý do nội tại (16 chỗ đặt tên, 4 chỗ lệch khuôn). `.docx` đã được bổ sung tên tệp `BaoCaoTongHopCTHTPL_` ngày 08/08. *(Trích cũ, từ nguồn sai:)* Mục **4.15.x STT 7**: *"Đặt tên tệp theo định dạng `BaoCaoTongHop_CTHTPL_{YYYYMMDD_HHmm}.xlsx` hoặc `.docx`"* — Kết quả mong đợi của test case chép nguyên văn từ đây, không phải tự suy ra từ quy ước Nhóm IX như phiếu Dev phỏng đoán.

**(2) Đối tác yêu cầu khác SRS ở đâu? → Ở hình thức tên tệp.** Rà toàn bộ hai bản, phần lớn đã cùng khuôn `{TênViếtLiền}_{YYYYMMDD_HHmm}.{đuôi}` (`HoiDap_`, `DanhSachChuongTrinh_`, `BaoCaoHoiDap_`, `BaoCaoVuViec_`, `BaoCaoDaoTao_`, `BaoCaoChuyenGia_`, `BaoCaoDanhGia_`, `BaoCaoChiPhi_`, `BaoCaoChuongTrinh_`). **Bốn chỗ lệch:**

| Chỗ lệch | Tên tệp hiện tại | Lệch ở đâu |
|---|---|---|
| `.docx` mục 4.15 STT 7 | `BaoCaoTongHop_CTHTPL_{YYYYMMDD_HHmm}` | hai dấu gạch dưới |
| `srs-fr-12-tv-chuyen-sau.md:162` | `TVCS-danh-sach-{YYYYMMDD-HHmm}.xlsx` | tên gạch nối, giờ-phút dùng gạch nối |
| `srs-fr-13-tv-nhanh.md:120` | `kho-cau-hoi-{YYYYMMDD-HHmm}.xlsx` | tên gạch nối, giờ-phút dùng gạch nối |
| `srs-fr-13-tv-nhanh.md:582` | `danh-gia-tv-nhanh-{ma_phien}-{YYYYMMDD-HHmm}.xlsx` | như trên, **và** có đoạn định danh `{ma_phien}` chen giữa |

**(3) Yêu cầu đó có bắt buộc cho luồng nghiệp vụ không? → CÓ ở mức tối thiểu.** Tệp phải có tên; để bản gốc im lặng thì mỗi bên tự đặt một kiểu.

**→ Kết luận: Loại 2 — nâng quy ước tên tệp BA chốt 04/08/2026 thành quy ước dùng chung cho **mọi nhóm**, đưa vào Phụ lục E; tên tệp Nhóm XI theo đó là `BaoCaoTongHopCTHTPL_{YYYYMMDD_HHmm}.xlsx` / `.docx`. **BA chốt 06/08/2026.** Dev action: Có. **Doc action:** bên soạn tài liệu bàn giao sửa mục 4.15.x STT 7 của bản `.docx` kế tiếp. → Sheet: giữ nguyên `N/R`.**

### Phương án xử lý (cập nhật SRS)

- Thêm **§H8 vào Phụ lục E** (`srs-v3.5.md`, bảng "Quy ước 7 thành phần UI đồng nhất" → thành 8), mức **BẮT BUỘC**:

  > **H8 — Tên tệp xuất thống nhất.** Áp cho **tệp kết xuất dữ liệu** mà phần mềm sinh ra theo yêu cầu người dùng (xuất danh sách, xuất báo cáo), ở **mọi nhóm chức năng**. **Không áp** cho tệp mẫu nhập liệu tải sẵn (vd "Tải mẫu điểm danh"), tệp người dùng tải lên, và tệp đính kèm — những loại này giữ tên gốc theo quy ước riêng của từng FR.
  > Khuôn: `{TenTep}[_{DinhDanh}]_{YYYYMMDD_HHmm}.{đuôi}`. `{TenTep}` viết liền kiểu PascalCase, bỏ dấu tiếng Việt và bỏ mọi ký tự không phải chữ hoặc số (kể cả dấu gạch nối, dấu cách, dấu câu); dấu gạch dưới chỉ dùng để ngăn các đoạn. `{DinhDanh}` là đoạn tuỳ chọn khi tệp gắn với một bản ghi cụ thể — phải lấy từ một trường **đã khai trong entity** của bản ghi đó, và áp cùng quy tắc ký tự như `{TenTep}`.
  > Tổng độ dài tên tệp tối đa **255 ký tự**; vượt thì cắt bớt `{TenTep}` chứ không cắt phần thời gian. Nếu trùng tên (hai lần xuất trong cùng phút), tự thêm hậu tố `_1`, `_2` — theo đúng cách đã dùng cho tệp tải lên tại `srs-fr-02-hoi-dap.md:108`.

- **Đổi 3 tên tệp đang lệch** (nếu không đổi thì thêm §H8 xong SRS tự mâu thuẫn ngay):
  - `srs-fr-12-tv-chuyen-sau.md:162` → `TvcsDanhSach_{YYYYMMDD_HHmm}.xlsx`
  - `srs-fr-13-tv-nhanh.md:120` → `KhoCauHoi_{YYYYMMDD_HHmm}.xlsx`
  - `srs-fr-13-tv-nhanh.md:582` → `DanhGiaTvNhanh_{ma_phien}_{YYYYMMDD_HHmm}.xlsx` — ⚠️ **chốt trường định danh trước khi áp:** `ma_phien` có ở Outputs (`srs-fr-13:282`) và ở ERD baseline (`srs-v3.5.md:4146`, `text ma_phien UK`), nhưng **bảng entity `TU_VAN_NHANH` ở `srs-fr-13` §4 không khai trường này** — chỉ có `id`. Bổ sung `ma_phien` vào bảng entity cho khớp ERD, rồi mới dùng làm `{DinhDanh}`.
- `srs-fr-11-bao-cao.md:85-86` — đổi phần mô tả khuôn tên tệp thành cross-ref về `Phụ lục E §H8`, giữ lại phần riêng của Nhóm IX (`{TenBaoCao}` là tên loại báo cáo). Quyết định 04/08 không bị đảo, chỉ được nâng phạm vi. **Cùng file còn 3 chỗ nữa nhắc khuôn này, phải sửa đồng bộ:** `:123`, `:124` (Tiêu chí chấp nhận) và `:1092` (Quy tắc tương tác SCR-IX-01).
- `srs-fr-15-ct-htpldn.md:1016` — bổ sung tên tệp `BaoCaoTongHopCTHTPL_{YYYYMMDD_HHmm}` cho báo cáo tổng hợp TW.
- **Phụ lục E — sửa nhãn "7" thành "8" ở 3 chỗ:** `srs-v3.5.md:6694` (ghi chú đầu Phụ lục), `:6702` (tiêu đề mục E.H), `:6716` (câu "nếu lệch quy ước H1–H7" → H1–H8).
- `srs-fr-15-ct-htpldn.md:397` (`DanhSachChuongTrinh_`) và `srs-fr-02-hoi-dap.md:151` (`HoiDap_`) đã đúng khuôn, giữ nguyên. Mã `H8` chưa dùng ở đâu — đã tra.

---

## Vấn đề 14 — `THBCTHCT_05` (phần 2): khối ký cuối trang có in dòng chức danh không

**Vấn đề:** Cuối tệp báo cáo xuất ra có khối ký. Bản gốc yêu cầu khối ký gồm ngày ký, chức danh người ký và con dấu — nhưng hệ thống không lưu chức vụ của cán bộ ở bất kỳ đâu, nên không có gì để in vào dòng đó. Nhóm IX đã được miễn dòng này, Nhóm XI thì chưa ai nói.

**(1) Phần mềm đúng SRS chưa? → SRS tự mâu thuẫn.** `srs-v3.5.md:6674-6678` (Phụ lục D.2.4): khung chung ghi *"Footer: Ngày ký + Chức danh người ký + Con dấu"*, ngay dưới là *"**Ngoại lệ nhóm IX (Báo cáo thống kê)** `[BA chốt 2026-08-04]`: khối ký gồm ngày ký + họ tên cán bộ xuất báo cáo + chỗ trống cho con dấu…, **không có dòng chức danh** — hồ sơ tài khoản (`TAI_KHOAN`) không lưu chức vụ nên không có nguồn dữ liệu"*. Nguyên nhân nêu ra là nguyên nhân **dữ liệu**, không phải đặc thù Nhóm IX.

**(1b) → CÓ, ở mục khác.** ⚠️ **Đính chính 08/08:** vế "chức danh" nằm ở **mục 3.11.2 bước 6**, không phải 4.15. Nguyên văn bản 01/08: *"cuối trang có ngày ký và chức danh"*. **Kết luận vẫn đứng**, đã sửa `.docx` ngày 08/08. *(Trích cũ, từ nguồn sai:)* Mục **4.15.x STT 7**: *"cuối trang có ngày ký và chức danh người ký"* — chép theo Phụ lục D.2.4 bản cũ, chưa có ngoại lệ.

**(2) Đối tác yêu cầu khác SRS ở đâu? → Không khác; mâu thuẫn nằm trong chính bản gốc.** Tra toàn bộ entity: các trường chức vụ hiện có đều không phải của cán bộ — `chuc_vu_dd` / `chuc_vu_dai_dien` là chức vụ người đại diện doanh nghiệp (`srs-fr-10:1057`, `srs-v3.5.md:1663`), một trường `chuc_vu` thuộc entity `HOC_VIEN` (`srs-v3.5.md:3512`); trường `chuc_vu` của hồ sơ tư vấn viên đã bị bỏ (`srs-v3.5.md:1884`, BA chốt 2026-05-05). Lời khai của Dev đúng.

**(3) Yêu cầu đó có bắt buộc cho luồng nghiệp vụ không? → KHÔNG.** Biểu mẫu gốc `docs/Input/Mau_21a_So_ban_nganh.csv` để khối ký là ba ô ký tay: *"Người lập biểu (Ký, ghi rõ họ tên)"* · *"Người kiểm tra (Ký, ghi rõ họ tên, chức vụ)"* · *"…ngày…tháng…năm… GIÁM ĐỐC (Ký, đóng dấu, ghi rõ họ tên)"*. Chức vụ là chỗ người ký tự ghi khi ký tay, không phải trường hệ thống phải điền sẵn.

**→ Kết luận: Loại 2 — mở rộng ngoại lệ §D.2.4 từ riêng Nhóm IX sang mọi tệp xuất của phần mềm. Khối ký gồm ngày ký + họ tên cán bộ xuất báo cáo + chỗ trống cho chữ ký, chức vụ và con dấu khi in chính thức; không in sẵn dòng chức danh. Dev action: Có → Sheet: giữ nguyên `N/R`.**

**Dev action cụ thể — 4 việc:**
1. Tệp xuất của Nhóm XI in khối ký cuối trang gồm **ngày ký** và **họ tên cán bộ xuất báo cáo**, kèm khoảng trống để người ký tự ghi chữ ký, chức vụ và đóng dấu khi in chính thức.
2. **Không in sẵn dòng chức danh** dưới tên cán bộ — không có nguồn dữ liệu, in ra sẽ là dòng trống hoặc chữ giả.
3. Áp cho **cả hai định dạng** Excel và Word (`srs-fr-15:1016` cho phép cả hai), không chỉ một.
4. Giữ đủ phần khung trình bày còn lại mà Kết quả mong đợi của test case nêu: **khổ A4, phông Times New Roman cỡ 13, đầu trang có quốc hiệu và tên cơ quan**. Ba ý này bản gốc đã có sẵn tại `srs-v3.5.md:6673-6677` (§D.2.4 "Format chung theo TT 17/2025") nên không phải bổ sung đặc tả — nhưng liệt kê ra đây để Dev không chỉ làm mỗi khối ký rồi vẫn bị đơn vị kiểm thử ghi lỗi.

Bỏ phần Dev nêu trong phiếu là *"chừa sẵn chỗ in chức danh nếu sau này BA chọn (b)"* — BA đã chốt dứt điểm hướng không in chức danh, giữ nhánh dự phòng chỉ tạo mã chết và chỗ để hiểu nhầm ở lượt sau.

**Doc action:** bên soạn tài liệu bàn giao sửa mục 4.15.x STT 7, bỏ vế "chức danh người ký".

### Phương án xử lý (cập nhật SRS)

- `srs-v3.5.md:6677` — **phải sửa cùng lúc**, dòng khung chung hiện ghi *"Footer: Ngày ký + Chức danh người ký + Con dấu (nếu in chính thức)"*. Khi ngoại lệ ở dòng dưới thành "mọi tệp xuất" thì dòng này không còn ca nào áp dụng mà vẫn bắt buộc chức danh — hai dòng liền nhau chọi nhau. Viết lại thành *"Footer: Ngày ký + Họ tên cán bộ xuất + chỗ trống cho chữ ký, chức vụ và con dấu (nếu in chính thức)"*.
- `srs-v3.5.md:6678` — đổi nhãn *"Ngoại lệ nhóm IX (Báo cáo thống kê)"* thành *"Ngoại lệ chung cho mọi tệp xuất"*, ghi rõ căn cứ là hồ sơ tài khoản không lưu chức vụ và biểu mẫu gốc để trống chỗ này cho người ký tự ghi. Bổ sung `[BA chốt 2026-08-06]` bên cạnh mốc 04/08.
- `srs-v3.5.md:4669` (LEG-06) — sửa vế *"còn áp cho tệp PDF của Nhóm IX theo chốt BA 2026-08-04"* thành ngoại lệ chức danh áp cho **mọi tệp xuất theo khung hành chính**. **Không đụng cột "Áp dụng"** của dòng này — xem điểm treo bên dưới.
- `srs-fr-15-ct-htpldn.md:1016` — ghi rõ khối ký của tệp xuất Nhóm XI theo §D.2.4.

**Điểm treo phát hiện khi rà phạm vi — Nhóm VI, cần BA quyết ở đợt sau, không chặn phiếu này.** Ba chỗ trong SRS nói khác nhau về việc mẫu 21a/21b có áp cho Nhóm VI (Đánh giá hiệu quả) hay không:

| Nguồn | Nói gì | Mốc |
|---|---|---|
| `srs-v3.5.md:4669` LEG-06, cột "Áp dụng" | 21a/21b áp cho **Nhóm VI** (UC83-91), IX, XI | cũ |
| `srs-v3.5.md:6672` D.2.4 "Phạm vi áp dụng" | *"hai biểu mẫu 21a/21b thuộc **nhóm XI**"* — không nhắc Nhóm VI; bảng mapping chỉ 2 dòng, đều trỏ FR-XI-06 | `[BA chốt 2026-08-04]` |
| `srs-fr-08-danh-gia.md:1088` | `mau_bao_cao` *"ở FR-08 chỉ là **tham chiếu liên kết**"* sang nhóm XI | — |

Theo cây trọng tài tầng 1 (chốt sau đè chốt trước) thì D.2.4 thắng: cột "Áp dụng" của LEG-06 là **dấu vết cũ chưa dọn sau quyết định 04/08**. Vì vậy phương án trên **không đụng cột đó** — sửa theo hướng mở rộng sẽ đóng dấu lại một phạm vi đã bị thu hẹp.

Kèm theo, `srs-fr-08` còn tự mâu thuẫn: `:1088` nói chỉ là tham chiếu, nhưng `:900` và `:911` ghi nút xuất *"Xuất theo mẫu TT17/2025"*, trong khi Nhóm VI có xuất tệp thật (`:605` — Excel/Word). Cần một lượt riêng để chốt: tệp xuất của Nhóm VI theo mẫu nào, có khung hành chính không. Ngoài phạm vi hai phiếu Dev nên phiếu này không quyết.

*Đính chính một nhận định trung gian: Nhóm XI **không** thiếu đặc tả khung trình bày. Khung nằm ở `srs-v3.5.md` §D.2.4 "Format chung theo TT 17/2025" (A4, Times New Roman 13, quốc hiệu + tên cơ quan đầu trang, khối ký cuối trang) và `srs-fr-15:1016` trỏ tới bằng cụm "theo TT17" — đúng lối tổ chức baseline, không lặp ở file FR.*

---

## Vấn đề 15 — `THBCTHCT_01`: tổng hợp báo cáo toàn quốc

**Vấn đề:** Cán bộ Trung ương gộp báo cáo của các đơn vị thành báo cáo toàn quốc. Mã này Dev xếp vào diện *"đã có căn cứ SRS rõ ràng nên tự fix"*, không trình BA. Kiểm lại: **Dev nói đúng ở phần chính**; chỉ một ý con nhỏ là bản gốc im lặng. Nhưng test case đứng vì một lỗi khác hẳn.

**(1) Phần mềm đúng SRS chưa? → Bản gốc quy định rõ 3 trên 4 ý con.** Bóc Kết quả mong đợi ra:

| Ý con trong Kết quả mong đợi | Bản gốc có không |
|---|---|
| Lưu bản ghi báo cáo tổng hợp toàn quốc | **CÓ** — `srs-fr-15:1003` bước 6, kèm Outputs `:1015` và Postconditions `:1020` |
| Chuyển đợt báo cáo: Đã gửi TW → Đã tổng hợp | **CÓ** — `:1004` bước 7 + máy trạng thái `:1515` |
| Lưu vết thao tác | **CÓ** — `:1006` bước 9 (BR-DATA-05) |
| Thông báo *"Đã tổng hợp báo cáo toàn quốc"* | **KHÔNG** — tra toàn thư mục `srs-v3.5/`, chuỗi "Đã tổng hợp" và "tổng hợp thành công" **không tồn tại ở bất kỳ file nào** |

**(1b) → ⚠️ Đính chính 08/08: KHÔNG.** Bản 01/08 **không có** chuỗi "Đã tổng hợp báo cáo toàn quốc". Cơ sở không còn; kết luận giữ theo quyết định BA 06/08, và `.docx` đã được bổ sung câu này ngày 08/08. *(Trích cũ, từ nguồn sai:)* Mục **4.15.x STT 6** (`section-4-fr-15.md:339`): *"Trường hợp 1: Tổng hợp thành công, hệ thống hiển thị thông báo **'Đã tổng hợp báo cáo toàn quốc'**"*. Ba ý con còn lại `.docx` nói giống bản gốc.

**(2) Đối tác yêu cầu khác SRS ở đâu? → Ở câu chữ.** Bản gốc **sót** chưa viết câu thông báo cho FR-XI-09, và như phân tích ở Vấn đề 4 thì bản gốc dùng lẫn lộn hai khuôn nên không có căn cứ nội tại để chọn. **BA chốt 06/08/2026: lấy câu theo `.docx`** — *"Đã tổng hợp báo cáo toàn quốc"*, cùng nguyên tắc với Vấn đề 4.

**(3) Vì sao test case chưa chạy? → Bị một lỗi khác chặn, không liên quan tranh chấp trên.** Ghi chú của người kiểm thử tại dòng 1619: *"Chưa thực hiện được do uc GKQTHCTHTPL_01 lỗi"*. Tra `GKQTHCTHTPL_01` (dòng 1617, Tuần 4): **`Fail`**, Kết quả thực tế ghi *"Hệ thống hiển thị thông báo **Forbidden**"* — lỗi phân quyền. Mã này **không nằm trong cả hai phiếu Dev**.

**→ Kết luận: Loại 4 hướng B cho riêng ý con câu chữ — bản gốc bị sót, bổ sung đặc tả rồi Dev làm theo; **BA chốt 06/08/2026 lấy câu theo `.docx`**, nên Kết quả mong đợi của đơn vị kiểm thử **không phải sửa**. Ba ý con còn lại Dev tự fix là **đúng căn cứ**. Dev action: Có (giữ hoặc đổi câu thông báo cho khớp khuôn "Đã ...") → Sheet: giữ nguyên `N/R` (dòng 1619). **Doc action: không có** — `.docx` đúng.**

### Phương án xử lý (cập nhật SRS)

- `srs-fr-15-ct-htpldn.md` FR-XI-09 — bổ sung một dòng mức INFO vào bảng Error Handling ghi câu *"Đã tổng hợp báo cáo toàn quốc"*, theo đúng cách làm ở Vấn đề 4.

**Việc cần làm ngoài phạm vi hai phiếu Dev — `GKQTHCTHTPL_01` lỗi "Forbidden" (dòng 1617, `Fail`).** Đây là vật cản thật của `THBCTHCT_01`, và là lỗi phân quyền có Kết quả thực tế ghi nhận đàng hoàng, nhưng **không phiếu Dev nào nhắc tới**. Đề nghị đưa vào lô xử lý kế tiếp; chừng nào chưa sửa thì cả `THBCTHCT_01` lẫn các mã phía sau nó vẫn không chạy được.

*Hai mã `QLHDTVVCG_26` và `_27` (thêm/xóa giai đoạn thanh toán) cũng do Dev tự chốt, đã kiểm: bản gốc `srs-fr-14:289` có đủ inline-edit, bốn trường, kiểm tổng thanh toán ≤ giá trị hợp đồng và thanh tiến độ; `.docx` chỉ mô tả chi tiết hơn chứ **không chọi** bản gốc. Dev tự làm là chấp nhận được.*

---

# Việc cần làm sau phiếu này

**1. Cập nhật sổ KTĐL.** Xác định lại số dòng ngay trước khi ghi và kiểm lại Mã TC ngay sau khi ghi. Cột cần ghi là **`Q`** (Trạng thái dev fix) và **`R`** (DEV phản hồi lần 1) — không phải `P`, đó là ô của đơn vị kiểm thử. **Giá trị ghi lên sổ là `Resoved`** (thiếu chữ `l`) theo đúng chính tả sổ đang dùng ở 62 dòng; ghi `Resolve` sẽ thành giá trị thứ sáu mà bộ lọc của đối tác không bắt được.

| Nhóm | Số dòng | Cột `Trạng thái dev fix` | Cột `DEV phản hồi lần 1` |
|---|:-:|---|---|
| Vấn đề 1 — 16 mã cụm A | 16 | `Resoved` | câu chuẩn ở Vấn đề 1 |
| Vấn đề 2 — 16 mã cụm B | 16 | `Resoved` | câu chuẩn ở Vấn đề 2 |
| Vấn đề 11 — `QLNDTVVCG_39` (dòng 1446) | 1 | `Reject` | phản hồi ở Vấn đề 11 |
| Vấn đề 3–5 — `QLHDTVVCG_01`…`_27` | 27 | **không ghi** — giữ `N/R` | chỉ ghi vào dòng `_01` (Vấn đề 3, dùng chung cả khối). 26 dòng còn lại để trống — `_15`/`_21` nay là Loại 4B, Dev sửa nên không phản hồi |
| Vấn đề 12, 13, 14 — `TPDBCKQTHCT_02` · `THBCTHCT_05` | 2 | **không ghi** — giữ `N/R` | **không ghi** |
| Vấn đề 15 — `THBCTHCT_01` (dòng 1619) | 1 | **không ghi** — giữ `N/R` | **không ghi** — Loại 4B, Dev sửa |
| *(ngoài phạm vi)* `GKQTHCTHTPL_01` (dòng 1617) | 1 | **không ghi** — `Fail`, chuyển lô sau | **không ghi** |
| Vấn đề 10 — `QLDX_04` · `_05` · `_06` | 3 | **không ghi** — giữ trạng thái đang xử lý | **không ghi** |
| Vấn đề 6 — `QLDXDTTH_07` (dòng 336) | 1 | `InProcess` | phản hồi ở Vấn đề 6 |
| Vấn đề 8 — `CPCTHTTLV_01` (dòng 1351) | 1 | **không ghi** — giữ `Đang Phát Triển`, chuyển OSP bổ sung dữ liệu | **không ghi** |
| Vấn đề 7 — `QLCHTHXLHS_09` (dòng 1027) | 1 | **không ghi** — giữ `Pass` | **không ghi** |

**2. Danh sách gửi kèm khi bàn giao bản `.docx` mới** — test case có Kết quả mong đợi chép từ mục sẽ bị gỡ hoặc sửa, cần cập nhật trước khi chạy: 16 mã cụm A, 16 mã cụm B, `QLDXDTTH_05`, `QLDXDTTH_07`, `QLNDTVVCG_39`, `THBCTHCT_05`; riêng khối `QLHDTVVCG_01`…`_27` phải sửa **bước thực hiện** cho cả 27 mã. `_15` và `_21` **không phải sửa Kết quả mong đợi** — câu thông báo họ ghi đúng khuôn bản gốc (Vấn đề 4). Không gửi danh sách này thì đơn vị kiểm thử sẽ chấm bản mới bằng thước cũ và ghi lại đúng bấy nhiêu lỗi.

**3. Doc action gom về một mối** — bên soạn tài liệu bàn giao, không phải Dev:

| Mục `.docx` | Việc | Nguồn |
|---|---|---|
| **3.11.2** bước 6 (4 chỗ) | Gỡ chức năng in báo cáo — tên bước, mục đích, thao tác, kết quả, nhánh lỗi | Vấn đề 1 · **ĐÃ LÀM 08/08** |
| *(không có)* | Vấn đề 2 — bản 01/08 đã đúng, không có việc gì | Vấn đề 2 |
| *(không có)* | Vấn đề 3 — bản 01/08 **đã có sẵn** ghi chú hai lối vào ở đầu nhóm 4.14 | Vấn đề 3 |
| **4.14.1.2.3** | Bổ sung `+ Hiển thị thông báo "Đã lưu hợp đồng".` | Vấn đề 4 · **ĐÃ LÀM 08/08** |
| **3.11.2** khối ký | "ngày ký và chức danh" → "ngày ký và họ tên cán bộ xuất báo cáo, chừa chỗ cho chữ ký, chức vụ và con dấu" | Vấn đề 14 · **ĐÃ LÀM 08/08** |
| **4.15.11.2.3** | Bổ sung `+ Hiển thị thông báo "Đã tổng hợp báo cáo toàn quốc".` và câu tên tệp `BaoCaoTongHopCTHTPL_{YYYYMMDD_HHmm}` | Vấn đề 13, 15 · **ĐÃ LÀM 08/08** |
| **3.11.2** bước "Ghi nhật ký thao tác" | Gỡ nốt vế in còn sót: *"tạo, xem, xuất và in báo cáo"* → *"tạo, xem và xuất báo cáo"*; *"(xem / xuất Excel / xuất PDF / in)"* → *"(xem / xuất tệp bảng tính / xuất tệp in ấn)"*. Căn cứ `srs-fr-11:88` và BR-DATA-05 — bản gốc chỉ ghi "xem/xuất báo cáo" | Vấn đề 1 · **ĐÃ LÀM 08/08**, phát hiện ở lượt Codex soát lại |
| **4.14.1.2.3** bước "Chỉnh sửa hợp đồng tư vấn" | Bổ sung câu *"Đã lưu hợp đồng"* cho cả chế độ Chỉnh sửa — `srs-fr-14:173` khai `INF-HDTV-01` dùng chung *"thêm mới hoặc chỉnh sửa"*, `.docx` mới chỉ có ở bước Thêm mới | Vấn đề 4 · **ĐÃ LÀM 08/08** |
| **4.14.1.2.3** cả hai bước lưu | Bổ sung vế điều hướng: *"đóng biểu mẫu và trả người sử dụng về ngữ cảnh đã mở nó là màn hình Chi tiết Vụ việc hoặc Chi tiết Tư vấn viên"*. Doc action gốc ghi *"sửa vế 'và quay về danh sách'"* — chuỗi đó **không tồn tại** trong bản 01/08, nên thành bổ sung mới theo `srs-fr-14:175` `[BA chốt 2026-08-06]` | Vấn đề 4 · **ĐÃ LÀM 08/08** |

**4. Cập nhật SRS — pha riêng, chỉ làm sau khi BA duyệt phiếu này:** `srs-fr-14:166-172` + Tiêu chí chấp nhận (Vấn đề 4) · `srs-fr-15:802`, `:825` (Vấn đề 12) · Phụ lục E §H8 + `srs-fr-11:85-86` + `srs-fr-15:1016` (Vấn đề 13) · Phụ lục D.2.4 + LEG-06 (Vấn đề 14).

**5. Đưa bản sửa lên đúng môi trường đối tác đang kiểm thử.** Sổ KTĐL cho thấy đơn vị kiểm thử chạy trên `htpldn-uat.ospgroup.vn` và `uat.phapluat.gov.vn`, **không phải** `18.143.165.120` — 120 chỉ là môi trường Dev tự thẩm định (bản dựng `V1.0.8`). Bản sửa cụm `QLDX_04/05/06` phải lên tới UAT của OSP thì đơn vị kiểm thử mới chạy lại được. Riêng khối `QLHDTVVCG` thì bản dựng không phải điều kiện chặn — phải sửa lối vào trong test case trước (Vấn đề 3).

**6. Việc còn treo của Dev** — không cần BA: 20 bài kiểm thử tự động còn khẳng định cách tra doanh nghiệp theo thư điện tử (Vấn đề 9).
