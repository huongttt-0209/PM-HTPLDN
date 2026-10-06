# Kế hoạch verify module "Báo cáo Thống kê" (Nhóm IX — FR-IX) — tuần 3

> **Vì sao chia batch:** module Báo cáo Thống kê có **87 case** đối tác báo (rows **190–276**, tab `UAT_TGPL Doanh Nghiệp-tuần 3`).
> Chạy 87 case trong 1 session → vỡ context → chất lượng verify tụt (đúng bài học postmortem 16/07: "mù" khi chạy nhiều case một lúc).
> → Chia **13 batch** theo **cụm lỗi (suffix mã TC = 1 thao tác template dùng chung) + họ báo cáo + tiền đề seed dùng chung** để mỗi session học 1 rule SRS, seed 1 lần, verify nhất quán nhiều case cùng bản chất.
> Mỗi batch **mở 1 cửa sổ Claude Code MỚI**, dán nguyên khối file `bctk/SESSION-bctk-batch{N}-prompt.md` tương ứng.
> **Chỉ có file prompt** nằm phẳng trong `bctk/`. **Bug + BA + cond + audit ghi vào FOLDER BUG TỔNG của round** (`reverify-week-3/bug-reports|cond|reverify-audit/` + `ba-confirmation-needed-bctk-batch{N}.md` ở gốc round), đặt tên file theo batch để không đụng nhau khi chạy song song.

## SRS gốc của module
`Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-11-bao-cao.md` (Nhóm IX — Báo cáo Thống kê, UC124–UC146, 23 loại báo cáo).

🔴 **Điểm mấu chốt — SHARED TEMPLATE `TPL-REPORT-FULL` (dòng 57–127) + màn dùng chung `SCR-IX-01` (dòng 1027–1090).** Cả 23 báo cáo dùng CHUNG 1 màn (SCR-IX-01) + 1 template (input/processing/output/error). Mỗi FR-IX-nn chỉ bổ sung phần **ĐẶC THÙ** (công thức, dimensions, output columns, biểu đồ). Gần như mọi cụm lỗi quy về đúng 1 clause của template/màn chung:

| Clause chuẩn | Dòng SRS | Liên quan cụm lỗi (suffix) |
|---|---|---|
| **SCR-IX-01 toolbar chỉ có 4 nút:** `Làm mới` (item 2), `Xem báo cáo` (item 7), `Xuất Excel (.xlsx)` (item 8), `Xuất PDF (.pdf)` (item 9) | 1042, 1047–1049 | **KHÔNG có nút "In báo cáo" / "Xóa bộ lọc"** → cụm _08/_09 |
| Nút Xuất Excel/PDF: điều kiện "Sau khi đã Xem báo cáo" → `click → auto-download` | 1048–1049 | Export _05/_06/_07 |
| Toast xuất file: `"Đang tạo file..." → "Xuất thành công" + auto-download` | 1054 | Export _05/_06/_07 |
| Given/When/Then Xuất Excel/PDF → tải file theo format TT17/2025 | 123–124 | Export _05/_06/_07 |
| **E6 `ERR-RPT-04` = "Không thể tạo file xuất. Vui lòng thử lại"** (Lỗi xuất file) | ~118 | Export _05/_06/_07 (đây ĐÚNG message đối tác báo) |
| E3 `INF-RPT-01` = "Không có dữ liệu báo cáo cho kỳ và đơn vị đã chọn" (empty state) | ~113, 1053 | Data _01 (no-data), tiền đề seed mọi batch |
| Biểu đồ (item 10): Line/Bar/Stacked/Donut/Radar tùy loại BC + toggle Hiện/Ẩn | 1051 | Cụm _04 (biểu đồ sai chiều/loại) |
| Bảng dữ liệu (item 11): nhóm theo chiều, cột sort, sticky header, hàng tổng | 1052 | Cụm _03 (thiếu/sai cột bảng tổng hợp) |
| **Bảng "Mapping 23 loại BC" — biểu đồ kỳ vọng từng báo cáo** | 1058–1082 | Cụm _04 — nguồn chuẩn đối chiếu biểu đồ |
| Export chèn tiêu đề + kỳ + đơn vị + ngày tạo vào header file (TT17); max 10.000 rows; timeout 30s | 1086–1090 | Export edge (E4 WRN-RPT-01, E5) |

## Map prefix mã TC → FR-IX / UC / Tên báo cáo / Biểu đồ kỳ vọng (dòng 1058–1082)

| Prefix | FR / UC | Tên báo cáo | Bộ lọc đặc thù | **Biểu đồ kỳ vọng** | Batch |
|---|---|---|---|---|:-:|
| SLHDVM | FR-IX-01 / UC124 | Số lượng hỏi đáp/vướng mắc PL | Lĩnh vực PL, Trạng thái HD | Donut + Trend | 1·5·6·7 |
| VVDTN | FR-IX-02 / UC125 | Vụ việc đã tiếp nhận | Kênh tiếp nhận, Lĩnh vực PL | Bar + Trend | 1·5·6·7 |
| VVDHT | FR-IX-03 / UC126 | Vụ việc đang hỗ trợ | NHT phụ trách, Mức SLA | Bar (snapshot) | 1·5·6·7·13 |
| VVDHTHT | FR-IX-04 / UC127 | Vụ việc đã hoàn thành | Lĩnh vực PL, Kết quả | Bar + Donut | 1·5·6·7 |
| VVTTG | FR-IX-05 / UC128 | Vụ việc theo thời gian | — | Line chart trend | 1·5·6·8·13 |
| CLDTBDDDR | FR-IX-06 / UC129 | Lớp đào tạo đang diễn ra | Hình thức, Lĩnh vực | Bar (snapshot) | 2·5·6·8 |
| LDTBDDDR | FR-IX-07 / UC130 | Lớp đào tạo đã diễn ra | Hình thức | Bar + Trend | 2·8 |
| CGTVPL | FR-IX-08 / UC131 | Số lượng CG/TVV | Loại TVV, Lĩnh vực CM, Đơn vị | Donut + Bar | 2·9 |
| DGHQHTPL | FR-IX-09 / UC132 | Đánh giá hiệu quả HTPL | Đợt đánh giá | Bar + Radar | 2·9 |
| CLDTBDPL | FR-IX-10 / UC133 | Chất lượng đào tạo | Khóa học cụ thể | Bar + Line | 2·9 |
| VVTDVQL | FR-IX-11 / UC134 | Vụ việc theo đơn vị quản lý | — | Stacked bar | 9 |
| VVTLV | FR-IX-12 / UC135 | Vụ việc theo lĩnh vực | — | Grouped bar | 3·10·13 |
| VVTLHDN | FR-IX-13 / UC136 | Vụ việc theo loại hình DN | Loại DN | Grouped bar | 3·10 |
| VVTTGCT | FR-IX-14 / UC137 | Vụ việc theo thời gian chi tiết | — | Stacked bar trend | 10 |
| CPHTCT | FR-IX-15 / UC138 | Chi phí chi trả hỗ trợ | — | Bar + Summary | 10 |
| CPCTHTTDVQL | FR-IX-16 / UC139 | Chi phí theo đơn vị | — | Bar cross-tab | 3·11 |
| CPCTHTTLHDN | FR-IX-18 / UC141 | Chi phí theo loại hình DN | Loại DN | Grouped bar | 3·11 |
| CPCTHTTTG | FR-IX-19 / UC142 | Chi phí theo thời gian | — | Line chart trend | 3·11 |
| SLCTHT | FR-IX-20 / UC143 | Số lượng CT hỗ trợ | Trạng thái CT | Bar + Trend | 3·11 |
| CTTDVQL | FR-IX-21 / UC144 | CT theo đơn vị | — | Bar cross-tab | 4·12 |
| CTTLV | FR-IX-22 / UC145 | CT theo lĩnh vực | Lĩnh vực | Bar | 4·12·13 |
| CTTTG | FR-IX-23 / UC146 | CT theo thời gian | — | Line chart trend | 12 |

> ⚠️ Map trên suy từ **thứ tự row = thứ tự FR + nội dung đối tác phản ánh**. FR-IX-17 (Chi phí theo lĩnh vực / UC140) KHÔNG có case trong lô này. **Mỗi batch BẮT BUỘC mở đúng section FR-IX-nn trong SRS xác nhận tên báo cáo + output columns trước khi verdict** (§3-Step Verify).

## 🔴 9 suffix mã TC = 9 thao tác template dùng chung (đọc từ cột "Mô tả"/"Các bước" của sheet)

| Suffix | Thao tác test | KQ mong đợi (SRS) | Đối tác phản ánh | Cụm batch |
|:-:|---|---|---|---|
| **_01** | Xem báo cáo có dữ liệu → khu vực kết quả (chỉ số + biểu đồ + bảng) | Hiển thị số liệu đúng theo đơn vị | Số liệu sai / không trùng khớp / "Không xác định" / no-data khi lọc | **DATA** (batch 13) |
| **_02** | Hiển thị "Chỉ số tổng hợp nhanh" (KPI card) | Theo từng BC — có/không có KPI riêng | KPI thừa (BC không được có nhưng vẫn hiện) | **DISPLAY** (batch 1·4) |
| **_03** | Hiển thị biểu đồ + bảng kết quả (giống thiết kế) | Đủ chỉ số/thẻ + cột bảng tổng hợp theo FR | Thiếu chỉ số/thẻ/cột, bảng không giống thiết kế | **DISPLAY** (batch 1·2·3·4) |
| **_04** | Hiển thị biểu đồ (giống thiết kế) | Đúng loại + chiều biểu đồ (bảng Mapping 1058) | Biểu đồ sai chiều (theo Đơn vị thay vì hình thức/loại/khóa), thiếu biểu đồ | **DISPLAY** (batch 1·2·3·4) |
| **_05** | Xuất Excel (.xlsx) | Xuất toàn bộ + auto-download (TT17) | "Không thể tạo file xuất. Vui lòng thử lại." | **EXPORT** (batch 8·10·11·12) |
| **_06** | Xuất Excel (.xlsx) | Xuất toàn bộ + auto-download (TT17) | "Không thể tạo file xuất. Vui lòng thử lại." | **EXPORT** (batch 7·8·9·10·11·12) |
| **_07** | Xuất PDF (.pdf) theo TT17/2025 | Tạo PDF A4, Times New Roman 13, quốc hiệu... | "Không thể tạo file xuất." (hoặc "không hiển thị nút") | **EXPORT** (batch 7·8·9·10·11) |
| **_08** | In báo cáo | Dựng bản xem trước + mở hộp thoại in trình duyệt | "Màn hình không hiển thị nút chức năng" | **BUTTON** (batch 5) |
| **_09** | Xóa bộ lọc | Reset bộ lọc về mặc định (Kỳ=Tháng, đơn vị đăng nhập...) | "Màn hình không hiển thị nút chức năng" | **BUTTON** (batch 6) |

> 🔴 **CẢNH BÁO số suffix KHÔNG đồng nhất tuyệt đối — phân cụm theo cột "Mô tả" của sheet, KHÔNG theo số suffix.** Các báo cáo có thêm/bớt bước "Chỉ số tổng hợp" nên đánh số lệch. Ngoại lệ đã phát hiện: **VVTTG_07 = In báo cáo** (không phải Xuất PDF), **VVTTG_08 = Xóa bộ lọc** (không phải In); **CTTDVQL_04 + CTTTG_04 = Xuất excel** (không phải hiển thị). Batch dưới đã gán theo **thao tác thực** — nếu tự chạy lại phân loại, luôn đọc "Mô tả"/"Các bước" của từng row.

## 13 batch (tổng 87 case)

| Batch | Cụm / chủ đề | # | Mã TC (rows) | Tiền đề seed chung | File prompt |
|:-:|---|:-:|---|---|---|
| **1** | DISPLAY — Hiển thị chỉ số/biểu đồ/bảng — họ Vụ việc nhóm 1 (_02/_03/_04) | 8 | SLHDVM_03(r190), VVDTN_04(r195), VVDHT_03(r201), VVDHT_04(r202), VVDHTHT_03(r207), VVDHTHT_04(r208), VVTTG_02(r214), VVTTG_03(r215) | Có dữ liệu VV/hỏi đáp trong kỳ+đơn vị chọn (Xem báo cáo ra data) | `SESSION-bctk-batch1-prompt.md` |
| **2** | DISPLAY — Đào tạo / CG-TVV / Đánh giá (_03/_04) | 7 | CLDTBDDDR_03(r220), CLDTBDDDR_04(r221), LDTBDDDR_04(r226), CGTVPL_04(r229), DGHQHTPL_03(r232), CLDTBDPL_03(r235), CLDTBDPL_04(r236) | Có dữ liệu lớp đào tạo / CG-TVV / đợt đánh giá | `SESSION-bctk-batch2-prompt.md` |
| **3** | DISPLAY — Vụ việc nhóm 2 + Chi phí + Số lượng CT (_03/_04) | 8 | VVTLV_03(r242), VVTLHDN_03(r245), CPCTHTTDVQL_03(r252), CPCTHTTLHDN_03(r255), CPCTHTTLHDN_04(r256), CPCTHTTTG_03(r259), SLCTHT_03(r262), SLCTHT_04(r263) | Có dữ liệu VV + chi phí chi trả + chương trình HT | `SESSION-bctk-batch3-prompt.md` |
| **4** | DISPLAY — họ Chương trình HTPLDN (_02/_03) | 4 | CTTDVQL_02(r266), CTTDVQL_03(r267), CTTLV_03(r271), CTTLV_04(r272) | Có dữ liệu chương trình HTPLDN | `SESSION-bctk-batch4-prompt.md` |
| **5** | BUTTON — Nút **In báo cáo** không hiển thị | 6 | SLHDVM_08(r193), VVDTN_08(r198), VVDHT_08(r205), VVDHTHT_08(r211), VVTTG_07(r218), CLDTBDDDR_08(r224) | Không cần data (chỉ soi toolbar) — vẫn Xem báo cáo 1 lần | `SESSION-bctk-batch5-prompt.md` |
| **6** | BUTTON — Nút **Xóa bộ lọc** không hiển thị | 6 | SLHDVM_09(r194), VVDTN_09(r199), VVDHT_09(r206), VVDHTHT_09(r212), VVTTG_08(r219), CLDTBDDDR_09(r225) | Không cần data (soi toolbar + test nút "Làm mới") | `SESSION-bctk-batch6-prompt.md` |
| **7** | EXPORT — Vụ việc nhóm 1 (Excel + PDF) | 8 | SLHDVM_06(r191), SLHDVM_07(r192), VVDTN_06(r196), VVDTN_07(r197), VVDHT_06(r203), VVDHT_07(r204), VVDHTHT_06(r209), VVDHTHT_07(r210) | Có dữ liệu để Xem báo cáo trước khi Xuất | `SESSION-bctk-batch7-prompt.md` |
| **8** | EXPORT — VV theo thời gian + Đào tạo (Excel + PDF) | 6 | VVTTG_05(r216), VVTTG_06(r217), CLDTBDDDR_06(r222), CLDTBDDDR_07(r223), LDTBDDDR_06(r227), LDTBDDDR_07(r228) | Có dữ liệu VV theo TG + lớp đào tạo | `SESSION-bctk-batch8-prompt.md` |
| **9** | EXPORT — CG/TVV + Đánh giá + Chất lượng ĐT + VV theo ĐVQL (_06/_07) | 8 | CGTVPL_06(r230), CGTVPL_07(r231), DGHQHTPL_06(r233), DGHQHTPL_07(r234), CLDTBDPL_06(r237), CLDTBDPL_07(r238), VVTDVQL_06(r239), VVTDVQL_07(r240) | Có dữ liệu tương ứng | `SESSION-bctk-batch9-prompt.md` |
| **10** | EXPORT — VV theo LV/LHDN/TGCT + Chi phí HT (_05/_06/_07) | 8 | VVTLV_05(r243), VVTLV_06(r244), VVTLHDN_05(r246), VVTLHDN_06(r247), VVTTGCT_05(r248), VVTTGCT_06(r249), CPHTCT_06(r250), CPHTCT_07(r251) | Có dữ liệu VV + chi phí | `SESSION-bctk-batch10-prompt.md` |
| **11** | EXPORT — Chi phí chi tiết + Số lượng CT (_05/_06/_07) | 8 | CPCTHTTDVQL_06(r253), CPCTHTTDVQL_07(r254), CPCTHTTLHDN_06(r257), CPCTHTTLHDN_07(r258), CPCTHTTTG_05(r260), CPCTHTTTG_06(r261), SLCTHT_06(r264), SLCTHT_07(r265) | Có dữ liệu chi phí + chương trình | `SESSION-bctk-batch11-prompt.md` |
| **12** | EXPORT — họ Chương trình (Excel + PDF) | 6 | CTTDVQL_04(r268), CTTDVQL_05(r269), CTTLV_05(r273), CTTLV_06(r274), CTTTG_04(r275), CTTTG_05(r276) | Có dữ liệu chương trình | `SESSION-bctk-batch12-prompt.md` |
| **13** | DATA — Số liệu chính xác (_01) — HARDEST, cần seed đúng + đối chiếu công thức | 4 | VVDHT_01(r200), VVTTG_01(r213), VVTLV_01(r241), CTTLV_01(r270) | Seed đúng số bản ghi biết trước, đối chiếu công thức FR | `SESSION-bctk-batch13-prompt.md` |

**Kích thước 8/7/8/4/6/6/8/6/8/8/8/6/4 = 87 — mỗi batch ≤8 case** → 1 session verify trọn không vỡ context.
Batch nhỏ tail (batch 4·13 = 4 case) CÓ THỂ gộp nếu tester quen tay, nhưng mặc định chạy riêng cho an toàn.

## 🔴 Vai trò dùng verdict — Cán bộ nghiệp vụ/phê duyệt (KHÔNG dùng admin ra verdict)

Cột "Tác nhân" của các case = **"Cán bộ nghiệp vụ TW,BN,ĐP / Cán bộ phê duyệt TW,BN,ĐP"**. TPL-REPORT-FULL processing bước 1 (dòng 79): "Kiểm tra quyền truy cập báo cáo + phạm vi theo đơn vị" (BR-AUTH-01). SCR-IX-01 item 5 (dòng 1046): dropdown đơn vị auto theo phân quyền 2-tier — **TW = "Toàn quốc"** (data rộng nhất), BN/ĐP locked theo đơn vị mình.

- **Chính: `cbnv_tw` / `Test@1234`** (Cán bộ nghiệp vụ Trung ương — phạm vi Toàn quốc → nhiều data nhất để render chỉ số/biểu đồ/bảng + có cái để Xuất). Fallback: `cbpd_tw` (cùng cấp TW).
- **admin CHỈ dùng để seed data / điều tra**, KHÔNG ra verdict (quyền QTHT không phải role của bug — báo cáo là chức năng cán bộ). Xem `input/input.md`.
- Nếu 1 case cần role BN/ĐP cụ thể (data scope hẹp) → login đúng cấp (cbnv_bn / cbnv_dp) + ghi rõ account đã dùng.

## 🔴 Cụm lỗi xuyên batch — verify chéo, nghi bug gốc chung (đừng log rời)

1. **Cụm "Xuất file thất bại — ERR-RPT-04"** — **44 case Xuất Excel/PDF xuyên batch 7·8·9·10·11·12.** Message đối tác báo ("Không thể tạo file xuất. Vui lòng thử lại.") = ĐÚNG `ERR-RPT-04` (E6, dòng ~118). Nghi **1 bug BE gốc chung** (endpoint xuất file lỗi cho MỌI loại báo cáo). 
   - **Verdict:** Xuất Excel/PDF là chức năng SRS quy định RÕ (SCR item 8/9 dòng 1048–1049 "click → auto-download"; Given/When/Then dòng 123–124). Fail = **hệ thống chặn luồng hợp lệ → `Open`** (dẫn dòng 1048–1049 + 123–124). 
   - ⚠️ **TIỀN ĐỀ BẮT BUỘC (§Nguyên tắc 4):** nút Xuất chỉ bật "Sau khi đã Xem báo cáo" (dòng 1048). Phải **seed data + Xem báo cáo ra kết quả** trước, RỒI mới Xuất. Nếu Xuất fail trên báo cáo KHÔNG có data → chưa đúng điều kiện, KHÔNG được kết luận. Nếu báo cáo CÓ data mà vẫn ERR-RPT-04 → `Open` (BE bug).
   - **GATE real-data:** mỗi case chụp toast ERR-RPT-04 (`tools/toast-capture.js`) + `list_network_requests` bắt request xuất trả 4xx/5xx. Verify KỸ 2–3 báo cáo đại diện (network payload), phần còn lại vẫn chụp ảnh + verdict riêng từng case.

2. **Cụm "Nút không hiển thị" (_08 In + _09 Xóa bộ lọc)** — **11 case batch 5·6.** SCR-IX-01 toolbar (dòng 1042–1054) **KHÔNG spec nút "In báo cáo" và KHÔNG spec nút "Xóa bộ lọc"** — chỉ có `Làm mới`, `Xem báo cáo`, `Xuất Excel`, `Xuất PDF`. 
   - **_08 In báo cáo:** đối tác kỳ vọng nút In (KQMĐ = xem trước + hộp thoại in), SRS **silent** (không có nút In) → **`BA confirm`** (expected đối tác khác SRS, để BA chốt có bổ sung chức năng In không). App KHÔNG hiện nút In là **đúng theo SRS hiện tại** → KHÔNG Open, KHÔNG Reject.
   - **_09 Xóa bộ lọc:** SRS có **"Nút Làm mới"** (item 2, dòng 1042). Đối tác kỳ vọng nút tên "Xóa bộ lọc" reset bộ lọc. **BẮT BUỘC test hành vi nút "Làm mới":** nếu "Làm mới" reset bộ lọc về mặc định (đúng KQMĐ _09) → chức năng CÓ, chỉ khác tên → **`BA confirm`** (SRS spec "Làm mới", đối tác muốn "Xóa bộ lọc"). Nếu "Làm mới" chỉ reload trang / KHÔNG reset bộ lọc → chức năng reset thật sự thiếu → cân nhắc **`Open`** (dẫn KQMĐ _09 + SCR item 2). Chụp ảnh trước/sau khi bấm "Làm mới".

3. **Cụm "Biểu đồ + bảng sai thiết kế" (Mô tả = "Kiểm tra hiển thị Biểu đồ và bảng")** — **16 case batch 1·2·3·4.** Đối tác báo biểu đồ render sai chiều (theo Đơn vị thay vì hình thức/loại/khóa), thiếu biểu đồ, hoặc bảng thiếu cột. Đối chiếu **bảng "Mapping 23 loại BC" (dòng 1058–1082)** cột "Biểu đồ kỳ vọng" + section **Output** của từng FR (bảng output columns) + SCR item 10/11 (dòng 1051–1052). App render sai loại/chiều/thiếu cột so SRS → **`Open`** (dẫn dòng mapping/output + FR). App render khác nhưng SRS mô tả chung → `BA confirm`. Chụp full-res biểu đồ + bảng, đọc trục/legend/header cột.

4. **Cụm "Chỉ số tổng hợp (KPI card) thiếu/thừa" (Mô tả = "Kiểm tra hiển thị Chỉ số tổng hợp")** — **11 case batch 1·2·3·4.** Đối chiếu section **Output** của từng FR-IX-nn. SRS liệt kê RÕ chỉ số mà app thiếu (vd DGHQHTPL: thiếu thẻ "Tổng số vụ việc đã đánh giá") → **`Open`**. Một số case KQMĐ đối tác = "Không có chỉ số tổng hợp riêng" (VVTTG_02, CTTDVQL_02, CTTLV_03) mà app LẠI hiện KPI → mở FR-IX-05/21/22 xem SRS có KPI không: SRS không có mà app hiện → `Open`/`BA confirm`; SRS có → đối tác sai kỳ vọng → `BA confirm`. Mở FR xác nhận, đừng suy đoán.

5. **Cụm "Số liệu sai" (_01)** — **4 case batch 13** (HARDEST). Cần seed đúng số bản ghi biết trước → Xem báo cáo → đối chiếu con số hiển thị vs **Công thức** trong FR-IX-nn. Số sai → `Open` (dẫn công thức). Số đúng, đối tác seed khác → `Reject`. "Không xác định"/no-data khi lọc = có thể FE filter bug hoặc thiếu seed → phân loại theo CLAUDE.md §"tab trống" (check `list_network_requests`).

## Verdict wording — mẹo nhanh (theo protocol, KHÔNG thay bảng Verdict)
- SRS §Output/§SCR quy định RÕ cột/nút/biểu đồ/định dạng mà app sai (thiếu/thừa/sai chiều/sai định dạng/chặn luồng) → thường **`Open`** (dẫn dòng template/FR/SCR/mapping).
- App làm KHÁC nhưng SRS chỉ nêu chung / không quy định (nút In không có trong SCR, đổi tên "Làm mới"↔"Xóa bộ lọc", KPI thiết kế thêm) → **`BA confirm`**.
- Đối tác báo lỗi cụ thể mà verify **KHÔNG tái hiện** (web chạy đúng) → **`Reject`** + "→ Đối tác kiểm tra lại."
- **CẤM** kết luận từ SRS suông — mọi verdict phải kèm **artifact real-data** (ảnh full-res phần tranh chấp / toast+network của chính thao tác) chạy trên data đã seed (§GATE protocol).

## 🔴 3-Step Verify TRƯỚC khi log bug (CLAUDE.md §4.4 + QA_VERIFY_PROTOCOL 3 CỔNG)
1. **Version SRS:** mặc định `srs-update-2026-5-5/`? → KHÔNG, module này dùng `srs-v3.5/srs-fr-11-bao-cao.md` (đúng đường dẫn user giao). Quote sai version = bug invalid.
2. **Quote nguyên văn dòng SRS** (mở file, format `srs-fr-11-bao-cao.md:LINE` + nội dung). KHÔNG dùng số dòng từ trí nhớ.
3. **Verify method thứ 2:** UI fail → curl/`list_network_requests` API cùng thao tác. API fail → reload UI fresh re-test.

## Output — tất cả ghi vào FOLDER BUG TỔNG của round (KHÔNG tạo folder riêng batch)
> Folder bug tổng = `output/UAT_doi-tac/reverify-week-3/bug-reports|cond|reverify-audit/` (dùng chung mọi module round 3; file có tiền tố `bctk` + số batch → không clobber khi song song).

- **Verdict → Google Sheet NGAY** sau mỗi case:
  `python3 tools/sheet_write.py --mode verify1 --row N --ma-tc <MÃ> --status <Open|Reject|BA confirm|""> --evidence <path> --condition-table <file.md> --note-file <note.txt>`
  (bug tĩnh: thêm `--static-bug "<lý do ≥10 ký tự>"`; ô TRỐNG: `--blocker-category A-F`). Lệnh chạy từ thư mục `output/UAT_doi-tac/`.
- **Bug Open** → `output/UAT_doi-tac/reverify-week-3/bug-reports/bug-report-bctk-batch{N}.md` (template `output/template/bug-report-template.md`, 6 sections; Bug ID = `BUG-<mã TC>`) + ≥1 screenshot `output/UAT_doi-tac/reverify-week-3/bug-reports/image/` (tên theo Bug ID).
- **BA confirm** → `output/UAT_doi-tac/reverify-week-3/ba-confirmation-needed-bctk-batch{N}.md`.
- **Reject / BA confirm** → evidence audit vào `output/UAT_doi-tac/reverify-week-3/reverify-audit/<mã TC>/`.
- **Bảng đối chiếu điều kiện** từng case (bug phụ thuộc role/state/data) → `output/UAT_doi-tac/reverify-week-3/cond/<mã TC>.md`. Bug tĩnh (nút thiếu cố định) không cần bảng — dùng `--static-bug`.
- **Cuối cùng (1 session, tuần tự):** merge 13 file `bug-report-bctk-batch{N}.md` → `bug-reports/Pass-bug-report-bctk.md`; merge BA → `ba-confirmation-needed-bctk.md`.

## 🔴 Chạy song song được không?
- **Tất cả 23 báo cáo dùng CHUNG 1 màn SCR-IX-01** (chỉ đổi dropdown loại BC) → verify = read-only (Xem/Xuất/soi nút), gần như KHÔNG mutate data nghiệp vụ → **an toàn chạy song song nhiều batch**.
- **Ngoại lệ cần seed:** batch 13 (_01 số liệu) cần seed data biết trước → seed record riêng tiền tố `BCTK-B13-<ngày>`, đừng đụng data batch khác. Các batch DISPLAY/EXPORT chỉ cần "có data bất kỳ trong kỳ" → tái dùng data sẵn có, không seed đè.
- An toàn nhất: chạy tuần tự, hoặc song song 2–4 batch. Export batch (7–12) độc lập hoàn toàn (chỉ khác dropdown loại BC).

## Tài khoản dùng chung
- **Chính: `cbnv_tw` / `Test@1234`** (Cán bộ nghiệp vụ TW — Toàn quốc). Fallback: `cbpd_tw`. Seed/điều tra: `admin` / `Secret@123`.
- Xem `output/UAT_doi-tac/input/input.md`. Thiếu account/data/state tạo được mà không tạo → **CẤM** ghi verdict (§Nguyên tắc 4). Tạo xong ghi lại vào `input/input.md`.

## Môi trường
- Web: `https://18.143.165.120.nip.io/login` · MailHog: `http://18.143.165.120:8025/` (xem `input/input.md`).
- Tool QA mặc định: **Chrome DevTools MCP** (`mcp__chrome-devtools__*`).
