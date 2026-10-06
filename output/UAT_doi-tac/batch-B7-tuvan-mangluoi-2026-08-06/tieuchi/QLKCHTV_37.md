# Tiêu chí verify — QLKCHTV_37

```
Mã case: QLKCHTV_37 (tab `bug`, dòng 305)     Thời điểm viết: 2026-08-06 14:53
Môi trường verify: https://18.143.165.120.nip.io  (env NỘI BỘ — đối tác đo trên env nghiệm thu khác)
Bản dựng: HTPLDN · V1.0.8 · bó mã FE `assets/index-DIABnbIr.js` (+ `assets/index-DVlgOkLg.css`)
          · `GET /` last-modified `Thu, 06 Aug 2026 07:13:15 GMT` (14:13:15 giờ VN) · etag `W/"6a74340b-428"`
          Đo lúc 14:56 (curl), đọc lại trong trang 15:02 và 15:09 — không đổi.
          ⚠️ Số phiên bản vẫn `V1.0.8` như lô B6 sáng nay nhưng bó mã đã khác (B6: `index-CNwX9JjX.js`,
          last-modified 02:51:16 GMT) ⇒ env deploy lại lúc 14:13 mà KHÔNG đổi số phiên bản. Chỉ ghi
          "V1.0.8" là không truy được đã đo bản nào.
Thời gian đo: 2026-08-06 14:57 → 15:11 (giờ VN)
```

> **Khai báo hồ sơ QA nội bộ đã đọc trước khi viết mục 4** (bắt buộc theo flow 04 §Giai đoạn A):
> - `output/UAT_doi-tac/reverify-week-4/bug-reports/bug-report-UAT-tuan-4.md` — entry `BUG-QLKCHTV_37`
>   (bắt đầu dòng ~1297), đã **Closed**, dòng Re-test ghi *"2026-07-28 11:19:46 R2 — ✅ PASS"* với số đo cũ:
>   nút [Xuất Excel] + 3 thẻ tổng hợp có mặt trên `TVN-20260727-0002`, tệp tải về tên
>   `danh-gia-tv-nhanh-TVN-20260727-0002-20260728-1119.xlsx`, đọc được 6 cột.
> - `output/UAT_doi-tac/batch-B7-tuvan-mangluoi-2026-08-06/bug-report.md` (bố cục file lô B7).
>
> **Mục 4 và mục 5 dưới đây suy TỪ ĐẶC TẢ, KHÔNG lấy số đo cũ làm ngưỡng.** Số đo cũ đo trên bản dựng
> khác (28/07) và **trước** khi BA chốt khuôn tên tệp ngày 2026-08-06, nên **không có giá trị chứng minh**
> cho lượt đo này. Bản ghi `TVN-20260727-0002` của lượt cũ **bị cấm dùng lại** — lượt này tự dựng phiên mới.

---

## 1. Đối tác phản ánh

Mô tả case: **"Xuất Excel đánh giá"**. Kết quả thực tế đối tác ghi: **"Màn hình không có nút chức năng"**.
TKM retest 3/8: *"Màn hình chưa có nút chức năng"*. DEV phản hồi lần 1: *"Ghi nhận của Quý đơn vị là đúng…
đơn vị phát triển **sẽ chỉnh sửa** phần mềm theo đặc tả đã cập nhật"* (thì tương lai — dev tự nhận **chưa** sửa
tại thời điểm trả lời).

Tách vế:

| Vế | Nội dung | Trạng thái đặc tả |
|---|---|---|
| **(a)** | Màn hình **không có** nút xuất tệp đánh giá ⇒ người dùng không kết xuất được | đặc tả **nói rõ** (`:582`) — khớp kỳ vọng đối tác |
| **(b)** | Tệp xuất phải chứa đủ **6 trường**: mã phiên · điểm đánh giá · nhận xét của DN · ngày đánh giá · tên DN · mã DN | đặc tả **nói rõ** (`:582`) — khớp kỳ vọng đối tác |
| **(c)** | Tệp phải **tải được về máy** người dùng | đặc tả **nói rõ** (`:582` "[Xuat Excel]" + §H8 quy ước tệp kết xuất) |
| **(d)** | **Khuôn tên tệp** — đối tác kỳ vọng `danh-gia-tv-nhanh-{mã phiên}{YYYYMMDD-HHmm}.xlsx` | đặc tả nói rõ **NHƯNG KHÁC**: `DanhGiaTvNhanh_{ma_phien}_{YYYYMMDD_HHmm}.xlsx`. **BA ĐÃ CHỐT ngày 2026-08-06** đúng điểm này ⇒ áp quyết định có sẵn, **không** đẩy sang hỏi BA (flow 04 §Rẽ nhánh, ngoại lệ duy nhất) |

**Bằng chứng đã xem:** `partner-evidence/QLKCHTV_37.jpg` (226.886 byte, ảnh tĩnh, đã mở **full-res**
1920×1030 bằng Read tool). Đọc được trên ảnh:

- Thanh địa chỉ: `htpldn-uat.ospgroup.vn/tv-nhanh/6dc026f2-b54b-4f7d-bda9-584ca1aa6f75` ⇒ **env nghiệm thu**,
  đúng màn **chi tiết phiên tư vấn nhanh**.
- Breadcrumb *Trang chủ / Tư vấn nhanh / Chi tiết*; sidebar đang chọn mục **Tư vấn nhanh**.
- Phiên **TVN-20260511-0002**, DN *"Cty Verify Dup"*, nhãn trạng thái góc phải **"Hoàn thành"**; thanh tiến
  trình 5 bước đã tích hết: Mới → Đang tìm kiếm → Đã gợi ý → CB trả lời → **5 Hoàn thành**.
- Khối *Thông tin phiên tư vấn*: Mã phiên `TVN-20260511-0002` · **Kênh = "Thủ công"** · **MST = "—" (trống)** ·
  Ngày gửi 11/05/2026 · Ngày cập nhật 11/05/2026 · Câu hỏi *"TC-DN-002 đề nghị tư vấn chi tiết"*.
- Khối **"Đánh giá"**: Điểm đánh giá **5 sao** · Ngày đánh giá **11/05/2026** · Nhận xét *"Test TC-DGTV-001 PASS"*.
  ⇒ **đủ tiền đề** đặc tả đòi để nút phải hiện (phiên Hoàn thành + ≥1 đánh giá).
- **Trong khối Đánh giá KHÔNG có nút xuất tệp nào, cũng KHÔNG có 3 thẻ tổng hợp** (Tổng đánh giá / Điểm TB /
  Phân bố). Toàn màn chỉ có 1 nút điều hướng *"Quay lại danh sách"* ⇒ đúng triệu chứng đối tác nêu.
- Góc phải: **"Cán bộ NV Trung ương  CB_NV_TW"**, badge đơn vị **BTP · TW**.
- Sidebar chân: **"HTPLDN · V1.0"**. Đồng hồ khay hệ thống: **10:44 AM · 2026-07-20**.

**Kiểm bằng chứng có đúng case này không:** ✅ đúng. Ảnh chụp đúng màn *Tư vấn nhanh → chi tiết phiên*,
đúng khối *Đánh giá*, đúng triệu chứng *không có nút xuất tệp*, trên phiên **đã Hoàn thành + đã có đánh giá**
— khớp cả ô Mô tả, ô Điều kiện và 3 bước của case.

> ⚠️ Lệch thời điểm cần ghi rõ: ảnh chụp **20/07/2026**, còn TKM retest **03/08/2026** chỉ có chữ, không kèm
> ảnh mới. Hai lần phản ánh **không cùng bản dựng** (env nghiệm thu ngày 20/07 là `HTPLDN · V1.0`; ngày 03/08
> bản dựng env nghiệm thu là V1.0.3 theo hồ sơ lô cùng ngày). Vẫn coi là **cùng một triệu chứng** vì cả hai
> lần đều mô tả "màn hình không có nút chức năng".

## 2. Đặc tả nói gì

Nguồn: `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-13-tv-nhanh.md`
(bản chốt duy nhất theo CLAUDE.md) + `srs-v3.5.md` Phụ lục E §H8.

Quote nguyên văn (đã mở file đọc đúng dòng, không lấy từ trí nhớ):

- `srs-fr-13-tv-nhanh.md:582` — SCR-X2-03 thành phần **#10**:
  *"Danh gia (v2.1 gop tu MH-13.4) | section/column | Diem (1-5 sao) / Nhan xet DN / Ngay danh gia.
  The tong hop: Tong danh gia (COUNT) / Diem TB (AVG) / Phan bo (bar chart mini). **[Xuat Excel]** — **ten tep
  `DanhGiaTvNhanh_{ma_phien}_{YYYYMMDD_HHmm}.xlsx` theo Phu luc E §H8 `[BA chot 2026-08-06]`; tap cot: ma phien,
  diem danh gia, nhan xet cua DN, ngay danh gia, ten doanh nghiep, ma doanh nghiep. Nut CHI hien thi khi phien
  o HOAN_THANH va da co it nhat 1 danh gia — khong roi vao truong hop xuat rong [BA-03 tuan 4]** | -- |
  **hien thi trong tab Hoan thanh hoac chi tiet phien**"*
- `srs-v3.5.md:6716` — Phụ lục E **§H8** *"Tên tệp xuất thống nhất"*: *"Áp cho **tệp kết xuất dữ liệu** phần mềm
  sinh ra theo yêu cầu người dùng… **Khuôn:** `{TenTep}[_{DinhDanh}]_{YYYYMMDD_HHmm}.{đuôi}`. `{TenTep}` viết
  liền kiểu PascalCase, bỏ dấu tiếng Việt và bỏ mọi ký tự không phải chữ hoặc số (kể cả dấu gạch nối, dấu cách,
  dấu câu); dấu gạch dưới chỉ dùng để ngăn các đoạn… Phần giờ-phút bắt buộc…"*
  `[BA chốt 2026-08-06 — nâng phạm vi quyết định 2026-08-04 của Nhóm IX thành quy ước chung]`
- `srs-fr-13-tv-nhanh.md:727` — entity TU_VAN_NHANH: *"ma_phien … dùng làm `{DinhDanh}` khi xuất tệp theo
  Phụ lục E §H8 `[bổ sung 2026-08-06]`"*.
- `srs-fr-13-tv-nhanh.md:392` — FR-X.2-05 bảng Inputs hàng 3: *"nhan_xet | text (long) | **N** | — | — | DN nhập"*
  ⇒ nhận xét **không bắt buộc**.
- `srs-fr-13-tv-nhanh.md:743` — entity DANH_GIA_TV: *"nhan_xet | text (long) | **N** | | | Nhận xét từ DN"*.
- `srs-fr-13-tv-nhanh.md:380` — FR-X.2-05: *"…đây cũng là căn cứ để áp quy tắc **mỗi phiên chỉ được chấm một
  lần** bởi chính DN đã gửi câu hỏi"* ⇒ COUNT tối đa 1 đánh giá / phiên.
- `srs-fr-13-tv-nhanh.md:265` / `:577` — kênh phiên có **2 giá trị**: `TV_NHANH` / `TV_THU_CONG`
  (cột "Kênh" trên bảng danh sách).
- `srs-fr-13-tv-nhanh.md:830` / `:839` — SM-TVNHANH: `CB_TRA_LOI --(DN đánh giá)--> HOAN_THANH`.
- `srs-fr-13-tv-nhanh.md:371` — *"Tác nhân: Cổng Pháp luật quốc gia (gửi đánh giá thay DN qua API inbound).
  **Người đánh giá thực sự là Doanh nghiệp**"* ⇒ đánh giá **không** nhập từ giao diện CMS của cán bộ.

**IM LẶNG về:**

1. **Nhãn / hình thức nút** (gọi "Xuất Excel", "Tải Excel", icon…), vị trí chính xác trong khối.
2. **Định dạng trình bày bên trong tệp** (font, khổ giấy, có dòng tiêu đề lớn hay không, thứ tự cột) —
   `:582` chỉ liệt kê **tập cột phải có**, không chốt thứ tự hay kiểu trình bày.
3. **Có bắt buộc hiện nút ở CẢ hai vị trí hay không** — `:582` ghi *"tab Hoan thanh **hoac** chi tiet phien"*
   ⇒ **một trong hai** là đủ.
4. **Hành vi khi phiên có nhiều đánh giá** — `:380` đã chặn ở mức 1 đánh giá/phiên.

## 3. Precondition

- **Tài khoản:** `cbnv_tw_02` — vai trò **CB_NV_TW** (Cán bộ Nghiệp vụ Trung ương), cấp **TW**,
  mật khẩu `Test@1234`. Đúng vai trò + cấp đọc được trên ảnh đối tác (*"Cán bộ NV Trung ương · CB_NV_TW"*,
  badge **BTP · TW**). Fallback theo Rule 7 nếu login fail: `cbnv_tw_03` (cùng vai trò + cùng cấp).
- **Tài khoản phụ (chỉ để dựng tiền đề, KHÔNG ra verdict):** vai trò **DN** — `0109998887` (QA UAT Kiểm Thử DN,
  `DN-HNI-0001`, Hà Nội) / `0209888006` / `2323232323`, mật khẩu `Test@1234`.
- **Màn:** `https://18.143.165.120.nip.io` → menu **Tư vấn → Tư vấn nhanh** → mở **chi tiết phiên**
  (`/tv-nhanh/{id}`) → khối **"Đánh giá"**; và **tab "Hoàn thành"** của màn danh sách.
- **Dữ liệu tiền đề (BẮT BUỘC tự dựng mới, cấm dùng lại `TVN-20260727-0002` của lượt cũ):**
  **2 phiên tư vấn nhanh MỚI** đưa lên trạng thái **Hoàn thành**, mỗi phiên có **đúng 1 bản ghi đánh giá của
  doanh nghiệp** — 1 phiên đánh giá **có** nhận xét, 1 phiên đánh giá **không** nhận xét (mục 5).
  Đánh giá phải đi qua đường DN/Cổng PLQG theo `:371`, không nhập tay bằng tài khoản cán bộ.

## 4. Tiêu chí chấm

✅ **PASS khi ĐỦ CẢ 5 điều** dưới đây, đo trên vai trò CB Nghiệp vụ, với **từng** dạng đánh giá trong mục 5:

1. **Nút xuất tệp có mặt và thao tác được** trên phiên **Hoàn thành + đã có ≥1 đánh giá**, ở **ít nhất một**
   trong hai vị trí đặc tả cho phép (tab "Hoàn thành" của danh sách **hoặc** màn chi tiết phiên) — đo được bằng:
   nút tồn tại trong trang · `disabled` = false · `pointer-events` ≠ `none` · `opacity` = 1 · kích thước > 0 ·
   màu chữ không phải xám nhạt.
2. **Bấm thật có kết quả** — bấm bằng thao tác giao diện thật (không gọi API thay), hệ thống **chuyển được một
   tệp bảng tính về máy người dùng**. Bấm không có gì xảy ra, hoặc chỉ báo lỗi = **FAIL**.
3. **Mở tệp ra đọc được và có đủ 6 trường** theo `:582`: **mã phiên · điểm đánh giá · nhận xét của doanh nghiệp ·
   ngày đánh giá · tên doanh nghiệp · mã doanh nghiệp**. Thiếu ≥1 trường ⇒ FAIL.
4. **Dữ liệu trong tệp khớp đúng đánh giá đang hiện trên màn** — mã phiên, điểm, nhận xét, ngày đánh giá,
   tên DN, mã DN đọc trong tệp **trùng khít** giá trị hiển thị ở khối "Đánh giá" của chính phiên đó.
   Ô nhận xét của dạng "không nhận xét" phải để **trống**, không được sinh chữ `null` / `undefined` / `None`.
5. **Tên tệp đúng khuôn `DanhGiaTvNhanh_{ma_phien}_{YYYYMMDD_HHmm}.xlsx`** theo `:582` + Phụ lục E §H8
   (`srs-v3.5.md:6716`): phần tên viết liền PascalCase không dấu gạch nối, `{ma_phien}` là mã phiên thật,
   có đủ phần ngày + giờ-phút, đuôi `.xlsx`.
6. **Đối chứng bằng đường thứ hai** — sau khi đo giao diện, đọc lại bản ghi đánh giá của phiên qua máy chủ và
   so từng trường với nội dung tệp. **Hai đường mâu thuẫn ⇒ chưa được chốt.**

❌ **FAIL nếu** bất kỳ điều nào xảy ra ở **bất kỳ** dạng đánh giá nào:

- **Không có** nút xuất tệp ở cả hai vị trí, trong khi phiên đã Hoàn thành và đã có đánh giá — chính triệu chứng
  đối tác nêu ⇒ **Reopen**.
- Nút có nhưng **bị vô hiệu hoá**, hoặc bấm **không sinh ra tệp nào**.
- Tệp sinh ra nhưng **0 byte / không mở được / không phải bảng tính**.
- Tệp **thiếu ≥1 trong 6 trường**, hoặc dữ liệu **lệch** so với màn hình ⇒ fix một phần ⇒ **Reopen**.
- **Tên tệp sai khuôn** đặc tả ⇒ fix một phần ⇒ **Reopen**.

🚫 **KHÔNG được chấm Fail vì** (đặc tả im lặng — xem mục 2):

- Nhãn nút không đúng chữ "Xuất Excel", hoặc nút nằm ở vị trí khác trong khối.
- Nút chỉ hiện ở **một** trong hai vị trí (`:582` ghi "hoặc").
- Thứ tự cột trong tệp, có/không có dòng tiêu đề lớn, font chữ, độ rộng cột, tên sheet.
- Tệp có **thêm** cột ngoài 6 cột bắt buộc.
- Khuôn tên tệp **không** giống chữ đối tác ghi trong ô Kết quả mong đợi
  (`danh-gia-tv-nhanh-…`) — **BA đã chốt 2026-08-06** khuôn `DanhGiaTvNhanh_…`; chấm theo đặc tả.
- Nút **không** hiện trên phiên chưa Hoàn thành / chưa có đánh giá — `:582` quy định đúng như vậy.

**Quan sát tách riêng, KHÔNG kéo verdict của case** (đối tác không nêu trong ô Kết quả thực tế):
3 thẻ tổng hợp **Tổng đánh giá (COUNT) / Điểm TB (AVG) / Phân bố** mà `:582` cũng đòi. Thiếu ⇒ ghi nhận + báo
phiên chính để mở phiếu riêng, **không** dùng để chấm case này.

## 5. Dạng dữ liệu phải phủ — **M = 2**

| # | Dạng | Vì sao nằm trong M |
|---|---|---|
| D1 | Đánh giá **CÓ nhận xét** (chuỗi tiếng Việt **có dấu**) | Đúng dạng trong ảnh bằng chứng (nhận xét *"Test TC-DGTV-001 PASS"*); là dạng làm cột "nhận xét của DN" trong tệp có nội dung. Thêm dấu tiếng Việt để bắt lỗi mã hoá khi ghi tệp |
| D2 | Đánh giá **KHÔNG có nhận xét** (`nhan_xet` để trống) | `:392` và `:743` khai `nhan_xet` **không bắt buộc** ⇒ đây là dạng hợp lệ thứ hai của chính trường nằm trong tập cột `:582`; là dạng hay lộ lỗi ghi `null`/`undefined` vào ô Excel |

**Nguồn xác định M:** ① đặc tả `:392` (bảng Inputs FR-X.2-05 — `nhan_xet` KBB) và `:743` (entity DANH_GIA_TV) ·
② `:582` liệt kê **"nhan xet cua DN"** là một cột bắt buộc của tệp xuất ⇒ phải phủ cả 2 trạng thái của trường đó ·
③ `:380` chốt mỗi phiên chỉ 1 đánh giá ⇒ không có dạng "nhiều đánh giá / 1 phiên".
⇒ **M = 1 là không hợp lệ** cho case này vì trường quyết định nội dung cột có 2 trạng thái hợp lệ.

**Biến thể phụ phải ghi nhận (không tính vào M):** kênh phiên `TV_THU_CONG` (dạng trong ảnh đối tác) và
`TV_NHANH` (`:265`, `:577`); hai lối vào hiển thị nút (tab "Hoàn thành" · chi tiết phiên) theo `:582`.

## 6. Bảng điều kiện

| Điều kiện có thể đổi kết quả | Đối tác | Mình test lần này | GAP? |
|---|---|---|:-:|
| Vai trò / tài khoản | `CB_NV_TW` — badge *"Cán bộ NV Trung ương · CB_NV_TW"*, đơn vị **BTP · TW** | `cbnv_tw_02` — `vaiTro=["CB_NV_TW"]`, `capDonVi=TW`, `donViId=00000000-0000-4000-8000-000000000001` (Cục Bổ trợ tư pháp - Bộ Tư pháp). **Trùng khít cả vai trò lẫn cấp, không nới chiều nào.** Không dùng tài khoản quản trị để ra verdict. Tài khoản DN `0109998887` chỉ dùng để **đọc** (kiểm có lối vào đánh giá hay không), không ra verdict | **Không** |
| Entity + trạng thái | Phiên `TVN-20260511-0002` ở **Hoàn thành** (5/5 bước), kênh **Thủ công**, đã có **1 đánh giá 5 sao** ngày 11/05/2026 | **3 phiên QA tự dựng**, cả 3 ở **Hoàn thành** + **đúng 1 đánh giá**: `TVN-20260806-0001` (kênh TV Nhanh, 4 sao) · `TVN-20260806-0002` (TV Nhanh, 5 sao) · **`TVN-20260806-0003` (kênh Thủ công, 3 sao — trùng khít kênh trong ảnh đối tác)**. Kiểm thêm **nhánh ngược**: `TVN-20260729-0002` (Cán bộ trả lời, chưa đánh giá) và `TVN-20260727-0004` (Hoàn thành nhưng KHÔNG có đánh giá) → nút không hiện, đúng `:582` | **Không** |
| Dữ liệu tiền đề | 1 phiên · 1 đánh giá **có nhận xét** (*"Test TC-DGTV-001 PASS"*) · DN *"Cty Verify Dup"*, **MST trống ("—")** | 3 đánh giá QA tự dựng trên DN `DN-HNI-0001` — *"Cong ty TNHH QA UAT Kiem Thu"*, **MST `0109998887` (có giá trị)**. Đánh giá tạo qua `POST …/danh-gia/cms-proxy` — **đường DUY NHẤT phần mềm cung cấp**: vai trò DN không có menu Tư vấn nhanh và bị **403** ở `/api/v1/tu-van-nhanhs`; đường inbound `/api/v1/public/…/danh-gia` đòi mTLS mà env không cấp chứng thư. **Chênh lệch MST (đối tác trống, mình có giá trị) không đóng được** vì bản ghi DN của đối tác nằm ở env khác — nhưng cột "Mã doanh nghiệp" trong tệp lấy đúng MST, nên DN trống MST cùng lắm ra **ô trống**, không đổi kết luận về việc **có hay không có nút** (chính vế đối tác nêu) | **Không** |
| Input / filter / giá trị nhập | Không có ô lọc nào trong ảnh; thao tác = tìm nút xuất tệp trong khối "Đánh giá" ở **màn chi tiết phiên** | Kiểm **cả 2 vị trí** `:582` cho phép: **tab "Hoàn thành"** của danh sách (không có nút — đặc tả ghi "hoặc" nên hợp lệ) và **màn chi tiết phiên** (có nút). Bấm **thật** nút `[Xuất Excel]` bằng chuột trên giao diện ở cả 3 phiên, không gọi dịch vụ thay thao tác | **Không** |
| Độ phủ biến thể (N bản ghi, M dạng) | N = 1 phiên-đánh giá · M = 1 dạng (có nhận xét) | **N = 3 phiên-đánh giá · M = 2/2 dạng** (D1 có nhận xét tiếng Việt có dấu ×2 · D2 không nhận xét ×1) ⇒ **3 lượt bấm thật** + 3 lượt đối chứng qua máy chủ + 2 lượt kiểm nhánh ngược + 1 lượt kiểm tab Hoàn thành. Phủ thêm **2/2 giá trị kênh** (`TV_NHANH` · `TV_THU_CONG`) và 3 mức điểm khác nhau (3/4/5). Rộng hơn đối tác (1×1) | **Không** |

**Sửa đổi tiêu chí giữa chừng:** không có. Mục 4 và 5 giữ nguyên như lúc 14:53, trước khi mở màn tranh chấp.

**Kết quả chấm theo mục 4** (đo 14:57 → 15:11 — số đo đầy đủ: [`../ketqua-QLKCHTV_37.txt`](../ketqua-QLKCHTV_37.txt)):

| # | Tiêu chí PASS | Kết quả |
|---|---|---|
| 1 | Nút xuất tệp có mặt + thao tác được ở ≥1 vị trí `:582` cho phép | ✅ 3/3 phiên ở **màn chi tiết**: `disabled=false` · `aria-disabled=null` · `pointer-events:auto` · `opacity:1` · `cursor:pointer` · 127×32 px. Tab "Hoàn thành" không có nút — hợp lệ vì `:582` ghi "hoặc" |
| 2 | Bấm thật ra tệp bảng tính về máy | ✅ 3/3 lượt bấm chuột thật → **7008 / 6940 / 7000 byte**, chữ ký `PK\x03\x04`, MIME `…spreadsheetml.sheet`. **3 mã băm md5 khác nhau** ⇒ 3 tệp thật, không phải tệp lấy lại từ bộ nhớ đệm |
| 3 | Tệp có đủ 6 trường `:582` | ✅ **6/6** ở cả 3 tệp: Mã phiên · Điểm đánh giá · Nhận xét của doanh nghiệp · Ngày đánh giá · Tên doanh nghiệp · Mã doanh nghiệp |
| 4 | Dữ liệu trong tệp khớp màn; ô nhận xét rỗng không sinh `null` | ✅ khớp **từng ô** với khối "Đánh giá" của chính phiên đó. Dạng D2 (máy chủ lưu `nhanXet = null`) ghi ra **chuỗi rỗng**, không phải chữ `null`/`undefined` |
| 5 | Tên tệp đúng khuôn `:582` + §H8 | ✅ 3/3: `DanhGiaTvNhanh_TVN202608060001_20260806_1504.xlsx` · `…0002_20260806_1506.xlsx` · `…0003_20260806_1510.xlsx` — PascalCase, `{DinhDanh}` đã bỏ dấu gạch nối đúng §H8, đủ ngày + giờ-phút, 49/255 ký tự |
| 6 | Đối chứng đường thứ hai | ✅ gọi thẳng dịch vụ xuất tệp: **200** cả 3, tên tệp do **máy chủ** đặt trong `content-disposition` trùng khít tên giao diện dùng; đọc lại bản ghi đánh giá khớp từng trường với nội dung tệp. **Không mâu thuẫn** |

⇒ Vế **(a)**, **(b)**, **(c)** đều **hết lỗi**. Vế **(d)** (khuôn tên tệp): bản dựng theo đúng **đặc tả hiện hành**
(`DanhGiaTvNhanh_…`), khác chữ đối tác ghi trong phiếu (`danh-gia-tv-nhanh-…`) — nhưng **BA đã chốt lại khuôn này
ngày 2026-08-06** tại `srs-v3.5.md:6716` §H8, nên đây là **áp quyết định có sẵn**, không phải QA tự bác đối tác,
và **không mở câu hỏi BA**.

**Quan sát tách riêng (không kéo verdict):**
- 3 thẻ tổng hợp mà `:582` cũng đòi — **CÓ ĐỦ** ở cả 3 phiên, số khớp dữ liệu thật (1 lượt · 4.0/5 · 4★×1 ‖
  1 lượt · 5.0/5 · 5★×1 ‖ 1 lượt · 3.0/5 · 3★×1). Đối tác không nêu vế này nên chỉ ghi nhận.
- Cột "Mã doanh nghiệp" điền **mã số thuế** `0109998887`, không phải mã nội bộ `DN-HNI-0001`. `:582` chỉ ghi
  "ma doanh nghiep", không chốt lấy trường nào ⇒ đặc tả im lặng ⇒ **không chấm Fail** (đã ghi sẵn ở mục 4).
- Bấm `[Xuất Excel]` **không sinh thông báo nào** (0/3 lượt). `:582` không đòi thông báo cho thao tác này
  ⇒ không chấm lỗi; bằng chứng thay thế là tệp thật + phản hồi máy chủ.

**GAP còn lại: 0/5.**

**3 dữ kiện neo của đối tác:**
`htpldn-uat.ospgroup.vn/tv-nhanh/6dc026f2-b54b-4f7d-bda9-584ca1aa6f75` — mã phiên `TVN-20260511-0002` ·
phiên **Hoàn thành**, kênh **Thủ công**, 1 đánh giá 5 sao ngày 11/05/2026, DN *"Cty Verify Dup"* (MST trống) ·
vai trò **CB_NV_TW** (BTP · TW), env **nghiệm thu `htpldn-uat.ospgroup.vn`**, bản dựng **HTPLDN · V1.0**,
thời điểm ảnh **20/07/2026 10:44** (TKM nhắc lại 03/08/2026, không kèm ảnh mới).

> **Giới hạn hiệu lực (không phải GAP):** đối tác đo trên env nghiệm thu `htpldn-uat.ospgroup.vn`; lượt này đo
> trên env **nội bộ** `18.143.165.120.nip.io`. Verdict chỉ có hiệu lực cho env + bản dựng ghi ở đầu file,
> phải xác nhận lại khi bản dựng đó lên env nghiệm thu.
