# BA confirmation needed — UAT đối tác tab tuần 1, vòng 2 (`TKDGHQHTPL_02` + `TKDGHQHTPL_OOS_01`) — 2026-07-27

> **File này để làm gì:** gom các testcase mà QA **không tự chốt verdict được**, kèm đối chiếu SRS + evidence UI để BA quyết nhanh. Bug đã có SRS reference rõ nằm ở [`bug-reports/dashboard/bug-report-dashboard-r2.md`](bug-reports/dashboard/bug-report-dashboard-r2.md) — file này chỉ chứa phần cần BA/CĐT chốt.
>
> **Cả 2 TC đều thuộc Dạng B** (SRS tự mâu thuẫn / thiếu ràng buộc → QA không tự chốt được).

> **⚠️ Version SRS dùng trong file này:** `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/` — bản chốt 2026-07-25, **nguồn duy nhất** theo CLAUDE.md §Quick reference.
> Template gốc `output/template/ba-confirmation-needed-template.md` dòng 10 còn hướng dẫn cite `input/srs-update-2026-5-5/` — bản đó là bản BA trích khi viết phiếu UAT, **lệch ~+5..+14 dòng và lệch cả nội dung**. Mọi số dòng dưới đây đã mở file verify trực tiếp trên bản `Docs-PM-HTPLDN/`, KHÔNG lấy từ trí nhớ. Đề nghị BA cho phép sửa dòng 10 của template để tránh tester sau quote nhầm bản.

**Tracker liên quan:** [`tasks/srs-contradictions.md` §SRS-C-009](../../../tasks/srs-contradictions.md) · **Audit đầy đủ:** [`reverify-audit/TKDGHQHTPL_02/audit.md`](reverify-audit/TKDGHQHTPL_02/audit.md)

---

## TKDGHQHTPL_02 — Thẻ "Điểm đánh giá hiệu quả hỗ trợ pháp lý" (Tổng quan hệ thống): thang điểm dán nhãn "/100" nhưng trần thực chỉ là 10

**Bối cảnh testcase**

- Dòng Excel: **47**, mã TC `TKDGHQHTPL_02`, tab `UAT_TGPL Doanh Nghiệp-tuần 1`.
- Nội dung kiểm tra: Cán bộ nghiệp vụ Trung ương mở màn **Tổng quan hệ thống**, đọc thẻ **"Điểm đánh giá hiệu quả hỗ trợ pháp lý"**.
- Expected trong file UAT: chỉ số hiển thị phải nằm trong thang 0–100.
- Actual đối tác ghi (ảnh 21/07/2026): thẻ hiển thị **164.0/100**, trục biểu đồ chạy tới **172** — vượt trần 100.

**Kết quả verify UI hiện tại**

- Verify lại ngày **27/07/2026** qua Chrome DevTools MCP, tài khoản UAT `cbnv_tw` / `CB_NV_TW` (Cục Bổ trợ tư pháp — BTP · TW), trên **chính môi trường đối tác** `https://htpldn-uat.ospgroup.vn`, **đúng bộ lọc trong ảnh đối tác** (Cấp đơn vị "Trung ương" + Đơn vị "Cục Bổ trợ tư pháp - Bộ Tư pháp").
- **Triệu chứng ">100" KHÔNG còn tái hiện:** thẻ nay hiển thị **8.2/100**, trục trần 100. Hai cột biểu đồ đổi theo đúng một hệ số: `172 → 8.6` và `150 → 7.5`, **đều chia đúng 20 lần**. Đã quét thêm 33 tổ hợp bộ lọc, không tổ hợp nào vượt 100.
- **Neo chứng minh cùng tập dữ liệu:** thẻ "Tỷ lệ tuân thủ thời hạn xử lý" bên cạnh vẫn **17.4%** ở cả 2 lần đo, trùng khít ảnh đối tác — chỉ riêng con số điểm đổi.
- **Nhưng cùng thẻ đó vẫn còn sai:** trên chính env này, kết quả đánh giá cao nhất là **10,00 điểm** và được hệ thống xếp loại **"Xuất sắc"** — tức đã đạt trần tuyệt đối — vậy mà thẻ vẫn gộp nó vào con số dán nhãn **"/100"**, làm một kết quả hoàn hảo trông như chỉ đạt khoảng một phần mười.
- **Kiểm chứng số học:** 6 kết quả có điểm là 10,00 / 9,50 / 8,90 / 8,00 / 7,90 / 5,00 — toàn bộ nằm trong 0–10; tổng **49,30 ÷ 6 = 8,216**, khớp con số **8.2** hiển thị.
- **Đối chiếu cách hệ thống tự xếp loại cũng cho thấy trần là 10:** 5,00 → "Đạt" (50%), 9,50 → "Xuất sắc" (95%), 8,90 → "Tốt" (89%), 7,90 → "Tốt" (79%).
- **Bằng chứng tự tố cáo trong cùng 1 màn hình:** thẻ "Chất lượng đào tạo, bồi dưỡng pháp lý" ngay bên dưới hiển thị **"Điểm trung bình 7.3/10"** và **"Điểm kiểm tra trung bình 7.3/10"** — cùng độ lớn con số, nhưng một thẻ ghi trên 10 còn thẻ đánh giá ghi trên 100.
- Evidence:
  - [`bug-reports/dashboard/image/BUG-TKDGHQ-THANG-DIEM-doitac-8.2tren100.png`](bug-reports/dashboard/image/BUG-TKDGHQ-THANG-DIEM-doitac-8.2tren100.png)
  - [`bug-reports/dashboard/image/BUG-TKDGHQ-THANG-DIEM-cung-man-7.3tren10.png`](bug-reports/dashboard/image/BUG-TKDGHQ-THANG-DIEM-cung-man-7.3tren10.png)
  - [`bug-reports/dashboard/image/BUG-TKDGHQ-THANG-DIEM-anh-goc-doitac-164tren100.png`](bug-reports/dashboard/image/BUG-TKDGHQ-THANG-DIEM-anh-goc-doitac-164tren100.png)

**Điểm mâu thuẫn trong SRS v3.5**

1. Theo **FR-I-08 (Dashboard)**, chỉ số của thẻ chạy trên **thang 0–100** và lấy thẳng `diem_tong`:
   - Biểu đồ trái là *"Điểm đánh giá hiệu quả hỗ trợ pháp lý (biểu đồ cột, **thang 0-100** theo điểm tổng đánh giá `KET_QUA_DANH_GIA.diem_tong` — ràng buộc 0-100)"*.
   - Outputs `diem_hai_long_tb` cũng ghi format *"thang **0-100**"*.

   Citation:
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-01-dashboard.md:416`
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-01-dashboard.md:450`

2. Nhưng **nhóm VI (Đánh giá)** lại cho ra trần thực tế là **10**, không phải 100:
   - BR-CALC-04: *"Điểm tổng = SUM(diem_i * trong_so_i / 100)"*.
   - `diem_toi_da` mặc định **10**; ràng buộc chấm điểm là *"0 ≤ diem ≤ diem_toi_da"*. Với Σ trọng số bị ép **= 100%** thì trần của `diem_tong` chỉ là **10**.
   - Xếp loại lại tính theo **tỷ lệ phần trăm** trên trần riêng từng kế hoạch: *">=90% Xuất sắc / >=70% Tốt / >=50% Đạt / <50% Chưa đạt"* — tức trần là mốc quy chiếu, không phải con số 100 cố định.

   Citation:
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-08-danh-gia.md:1239` (BR-CALC-04)
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-08-danh-gia.md:1100` (`diem_toi_da` mặc định 10)
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-08-danh-gia.md:479` (`0 ≤ diem ≤ diem_toi_da`)
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-08-danh-gia.md:874` (xếp loại theo %)
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-08-danh-gia.md:1049` (`diem_tong` CHECK 0–100 — chỉ là khoảng giá trị hợp lệ, không phải thang chấm)

3. **Nguồn gây lệch — ghi rõ trong CHANGELOG:** khi nâng v3 → v3.5, thang của Dashboard được sửa từ 1–5 lên 0–100 **căn cứ ràng buộc lưu trữ**, không đối chiếu BR-CALC-04. CHANGELOG cũng ghi mức lệch đúng bằng **20 lần** — trùng khít hệ số ÷20 đo được ở phần verify trên, nên giải trình *"BE với FE chưa giống nhau"* của đội phát triển là **có cơ sở**.

   Citation:
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/CHANGELOG-v3-to-v3.5.md:1729`
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/CHANGELOG-v3-to-v3.5.md:1734`

4. **Chỗ đặc tả còn thiếu hẳn (không phải mâu thuẫn, mà là bỏ trống):** không dòng nào ràng buộc **tổng** của `diem_toi_da`. `:191` chỉ ghi *"> 0, số nguyên dương"*, màn cấu hình `:850` cũng chỉ ghi *"number > 0"* — trong khi **trọng số** thì đã bị ép SUM = 100%.

   Citation:
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-08-danh-gia.md:191`
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-08-danh-gia.md:850`

5. **Ghi chú thẩm quyền:** FR-I-08 hiện vẫn ghi *"**Source:** Đề xuất — **công thức tính chờ CĐT review**"* — công thức của chính thẻ này chưa được ký chính thức.

   Citation:
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-01-dashboard.md:410`

**QA đã sàng 3 hướng — chỉ còn 1 hướng sống sót**

| Hướng xử lý | `:416` thang 0-100 theo `diem_tong` | `:1049` CHECK 0-100 | `:874` xếp loại % | `CHANGELOG:1729` đối chiếu được với màn chi tiết | Cộng TB chéo kế hoạch |
|---|:-:|:-:|:-:|:-:|:-:|
| (a) Dashboard quy đổi sang % | ✗ | ✓ | ✓ | **✗** | ✓ |
| (b) Giữ số thô, mẫu số theo trần từng kế hoạch | ✗ | ✓ | ✓ | ✓ | **✗** |
| **(c) Ràng buộc cấu hình để trần luôn = 100** | ✓ | ✓ | ✓ | ✓ | ✓ |

- **(a) LOẠI.** Màn chi tiết đánh giá hiển thị cột *"Điểm tổng (tự tính = tổng điểm x trọng số / 100)"*, tức **số thô** (8,6) — `srs-fr-08-danh-gia.md:873`. Quy đổi Dashboard sang % ⇒ Dashboard **86** vs chi tiết **8,6** cho cùng một vụ. Đây đúng là tình huống `CHANGELOG:1729` đã chủ động sửa: *"Cán bộ nghiệp vụ nhìn biểu đồ Dashboard hiển thị '3.5' trong khi báo cáo chi tiết hiển thị '70' cho cùng một vụ, **không cách nào đối chiếu**"*. Hướng này tái tạo lại đúng lỗi cũ.
- **(b) LOẠI.** Mỗi kế hoạch một trần khác nhau ⇒ không cộng trung bình chéo kế hoạch được, mà đó lại là việc chính của thẻ.
- **(c) CHỌN.** Củng cố thêm: dữ liệu đời trước (kế hoạch `KHDG-SEED-0001`) đang mang điểm **80 / 60 / 90** — đã ở thang 0–100 từ trước ⇒ thang 0–100 nhiều khả năng luôn là thiết kế gốc, còn `diem_toi_da` mặc định **10** mới là chỗ lệch.

⇒ **Vị trí sửa nằm ở nhóm VI Đánh giá (cấu hình + kiểm tra `diem_toi_da`), KHÔNG phải Dashboard.** Thẻ Dashboard đang hiển thị đúng như `:416` mô tả — đề nghị đội phát triển **không** sửa ở Dashboard.

**Câu hỏi cần BA / CĐT xác nhận**

Chỉ cần trả lời có/không cho 2 câu — không cần thiết kế lại:

1. **Bổ sung ràng buộc còn thiếu:** có chốt quy tắc `Σ (diem_toi_da_i × trong_so_i / 100) = 100` cho mỗi kế hoạch đánh giá không?
   → Đây là **thêm một luật nghiệp vụ mới** (đặc tả hiện chỉ ràng buộc từng `diem_toi_da` > 0, không ràng buộc tổng) nên đội phát triển không tự quyết được.
2. **Duyệt cách xử lý dữ liệu đã có:** các kế hoạch đang cấu hình `diem_toi_da = 10` và **đã chấm xong** thì quy đổi, hay chấp nhận để lệch vĩnh viễn?
   → Việc này đụng vào kết quả đã chấm nên cần người có thẩm quyền duyệt.

**Đề xuất QA tạm thời**

- Phần lỗi hiển thị đã đủ căn cứ chuyển dev (đã log `BUG-TKDGHQ-THANG-DIEM`), nhưng **dev chưa thao tác được** cho tới khi 2 câu trên có câu trả lời → verdict đề xuất cho dòng 47: **`Open, BA confirm`**.
- Nếu BA chốt **có** cho câu 1: hướng (c) thành ràng buộc chính thức; owner sửa = **Dev BE + Dev FE nhóm VI Đánh giá** (cấu hình tiêu chí), Dashboard **giữ nguyên**. Kèm câu 2 quyết định có migration hay không.
- Nếu BA chốt **không** cho câu 1 (chấp nhận mỗi kế hoạch một trần riêng): thì `srs-fr-01-dashboard.md:416` phải sửa — thẻ Dashboard không thể vừa lấy `diem_tong` thô vừa dán nhãn "/100"; khi đó owner = **BA cập nhật đặc tả FR-I-08 trước**, rồi mới tới Dev.

**Lỗ hổng độc lập phát hiện kèm (bịt luôn nếu câu 1 được duyệt)**

`diem_toi_da` để tự do (`srs-fr-08-danh-gia.md:191`) trong khi `diem_tong` bị chặn `CHECK BETWEEN 0 AND 100` (`:1049`). Cấu hình `diem_toi_da = 200` rồi chấm 150 ⇒ `diem_tong = 150`, **vi phạm chính ràng buộc đó**. QA đã dựng thử một kế hoạch `diem_toi_da = 200` trên môi trường được giao `18.143.165.120.nip.io` — **hệ thống chấp nhận**.

---

## TKDGHQHTPL_OOS_01 — Cùng thẻ đó gộp cả kết quả CHƯA chấm và kế hoạch ĐÃ HỦY vào chỉ số

> **Phân biệt phạm vi với TC trên:** dòng 47 nói về **thang đo**; dòng này nói về **tập bản ghi đầu vào**. Tách riêng để đội phát triển không sửa gộp.

**Bối cảnh testcase**

- Dòng Excel: **276**, mã TC `TKDGHQHTPL_OOS_01` — TC do **QA mở thêm** (ngoài phạm vi case đối tác), phát sinh khi verify `TKDGHQHTPL_02`.
- Nội dung kiểm tra: Cán bộ nghiệp vụ Trung ương đọc con số trung bình + chú thích cỡ mẫu "Dựa trên N đánh giá" của cùng thẻ đó.
- Expected: chỉ số và cỡ mẫu phản ánh đúng các đánh giá **thực sự đã được chấm và còn hiệu lực** trong kỳ.

**Kết quả verify UI hiện tại**

- Thẻ hiển thị **29.5/100** kèm chú thích **"Dựa trên 14 đánh giá"**, trong khi số kết quả thực sự đã chấm chỉ có **11**.
- Đếm thừa 3 bản ghi: `14 = 11 kết quả "Đã đánh giá" + 3 kết quả vẫn ở "Chưa đánh giá" nhưng đã có sẵn điểm` (80,00 / 60,00 / 90,00). Chính 3 bản ghi chưa chấm này lại là **3 cột cao nhất** của biểu đồ (02/2026 = 90.0 · 04/2026 = 80.0 · 05/2026 = 60.0).
- Kế hoạch **`DG-20260727-0001`** ở trạng thái **"Hủy"** nhưng kết quả **100,00** của nó vẫn vào trung bình và vào cột 07/2026. Bỏ riêng bản ghi này ra thì cột 07/2026 là **8,24** thay vì **16.6** — một bản ghi của kế hoạch đã hủy làm cột này **tăng gấp đôi**.
- Kiểm chứng số học: tổng điểm của đúng 14 bản ghi được đếm là **412,40**; chia 14 được **29,457** → khớp **29.5** trên thẻ ⇒ thẻ lấy toàn bộ bản ghi có điểm, không lọc theo trạng thái kết quả và cũng không loại kế hoạch đã hủy.
- **⚠️ Tiền đề dữ liệu — quan trọng để dev không kết luận nhầm "đã sửa":** lỗi chỉ lộ ra khi trong kỳ có đồng thời (a) ≥1 kết quả còn "Chưa đánh giá" nhưng đã có điểm, và (b) ≥1 kế hoạch "Hủy" mà kết quả đã có điểm. Tại 27/07/2026, **env đối tác `htpldn-uat.ospgroup.vn` KHÔNG thoả tiền đề này** → mở Dashboard ở đó sẽ không thấy lỗi, và **đó không phải bằng chứng đã sửa**. Số liệu trên đo tại env được giao `18.143.165.120.nip.io`.
- Evidence: [`bug-reports/dashboard/image/BUG-TKDGHQ-KPI-LOC-29.5-dua-tren-14-danh-gia.png`](bug-reports/dashboard/image/BUG-TKDGHQ-KPI-LOC-29.5-dua-tren-14-danh-gia.png)

**Điểm mâu thuẫn trong SRS v3.5**

1. Theo **BR-RPT-01**, bản ghi chưa ở trạng thái cuối hợp lệ và bản ghi đã hủy **không** được tính vào số liệu thống kê:
   - *"Bản ghi `DU_THAO`, `CHO_PHE_DUYET`, `TU_CHOI`, `DA_HUY` **KHÔNG** được tính vào số liệu thống kê"*.
   - **Nhưng** cột phạm vi áp dụng của quy tắc chỉ liệt kê **`FR-IX-01..23` (nhóm Báo cáo)** — **không** gồm FR-I-08 Dashboard.

   Citation:
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-v3.5.md:5608`

2. Nhưng **FR-I-08** lại chỉ mô tả chung chung, **không** nêu điều kiện lọc trạng thái nào:
   - Processing bước 2: *"Tính điểm đánh giá hiệu quả hỗ trợ pháp lý trung bình từ **kết quả đánh giá** thuộc phạm vi"*.
   - Outputs `so_luong_danh_gia`: *"tổng số **đánh giá** trong kỳ + phạm vi đã lọc"*.
   - Preconditions: *"Có dữ liệu đánh giá trong kỳ (Nhóm VI)"*.

   Citation:
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-01-dashboard.md:441`
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-01-dashboard.md:452`
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-01-dashboard.md:425`

3. Trong khi đó nhóm VI khẳng định bản ghi chưa chấm **chưa phải** là một đánh giá đã hoàn tất, và kế hoạch hủy là **soft-delete**:
   - `KET_QUA_DANH_GIA.trang_thai` — *"CHECK IN ('CHUA_DANH_GIA','DA_DANH_GIA')"*, mặc định `'CHUA_DANH_GIA'`.
   - Chuyển trạng thái sang `HUY` có hệ quả *"Audit, soft-delete"*; trạng thái `HUY` = *"Đợt đánh giá bị hủy"*.

   Citation:
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-08-danh-gia.md:1052`
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-08-danh-gia.md:1183`
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-08-danh-gia.md:1168`

**Câu hỏi cần BA / CĐT xác nhận**

FR-I-08 (thẻ "Điểm đánh giá hiệu quả hỗ trợ pháp lý" trên màn Tổng quan hệ thống) có chịu ràng buộc BR-RPT-01 không?

1. **Hướng 1 — có, mở rộng phạm vi BR-RPT-01 sang FR-I-08:** thẻ phải loại kết quả còn "Chưa đánh giá" và kết quả thuộc kế hoạch "Hủy" ra khỏi **cả trung bình lẫn cỡ mẫu**. Đề nghị BA bổ sung `FR-I-08` vào cột phạm vi áp dụng ở `srs-v3.5.md:5608` và nêu rõ điều kiện lọc ở bước xử lý `srs-fr-01-dashboard.md:441`.
2. **Hướng 2 — không, Dashboard cố ý tính mọi bản ghi có điểm:** thì UI hiện tại **không phải lỗi**, nhưng đề nghị BA ghi rõ chủ ý này vào FR-I-08 để lần sau QA không log lại, và cân nhắc đổi nhãn chú thích cỡ mẫu cho đúng bản chất (đang ghi "Dựa trên N đánh giá" trong khi N gồm cả bản chưa chấm).

**Đề xuất QA tạm thời**

- Tạm verdict cho `TKDGHQHTPL_OOS_01`: **`Cần BA xác nhận`** — chưa chuyển dev cho tới khi BA chốt phạm vi BR-RPT-01.
- Nếu BA chọn **hướng 1**: UI hiện tại là **`Vẫn lỗi`**, owner dự kiến **Dev BE** (thêm điều kiện lọc ở truy vấn của thẻ). Bug đã log sẵn: `BUG-TKDGHQ-KPI-LOC`.
- Nếu BA chọn **hướng 2**: UI hiện tại **không phải lỗi** → QA đóng `BUG-TKDGHQ-KPI-LOC` + cập nhật lại expected; owner = **BA cập nhật FR-I-08**.
- Ghi chú chung cho cả 2 nhánh: `srs-fr-01-dashboard.md:410` đang ghi FR-I-08 có *"công thức tính chờ CĐT review"* — nên câu trả lời cho cả 2 TC trong file này nên đi kèm lần review đó.

---

## Phụ lục — điều kiện đo

| Thành phần | Giá trị |
|---|---|
| Env đối tác | `https://htpldn-uat.ospgroup.vn` — dùng cho phần verify `TKDGHQHTPL_02` |
| Env được giao | `https://18.143.165.120.nip.io` — dùng cho phần số liệu `TKDGHQHTPL_OOS_01` |
| Tài khoản | `cbnv_tw` / `Test@1234` (CB_NV_TW, Cục Bổ trợ tư pháp — BTP · TW) |
| Ngày đo | 2026-07-27 |
| Tool | Chrome DevTools MCP |

> **Dữ liệu QA tự tạo trên env được giao (đừng nhầm là dữ liệu thật, không xoá được):** kế hoạch **`DG-20260727-0001`** (`b217202c-de53-4f6b-a3f9-6ec911f2dfe0`, trạng thái `HUY`, 1 tiêu chí `diemToiDa = 200`, 1 kết quả `diemTong = 100.00`). **Không** seed bất kỳ dữ liệu nào lên env đối tác.

---

*File tạo: 2026-07-27 | QA Automation via Claude Code | theo [`output/template/ba-confirmation-needed-template.md`](../../template/ba-confirmation-needed-template.md)*
