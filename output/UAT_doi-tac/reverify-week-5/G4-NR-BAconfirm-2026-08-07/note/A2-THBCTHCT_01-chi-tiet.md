# A2 — dòng 343 — `THBCTHCT_01` — "Tổng hợp báo cáo thực hiện chương trình từ nhiều đơn vị"

> **VERDICT: `Reopen`** — chi tiết ở §10. Đo 07/08/2026 20:53→21:14 (giờ VN), bản dựng `index-BbPPdate.js`,
> tài khoản `cbnv_tw_05`. Lỗi tái hiện **2/2 lượt trên 2 đợt độc lập**.

## 1. Bối cảnh phiếu (đọc từ `do/00-sheet-7-dong-goc.txt`, khối DÒNG 343)

| Cột | Nội dung |
|---|---|
| `[D]` Mã TC | `THBCTHCT_01` |
| `[F]` Tác nhân | Cán bộ nghiệp vụ TW |
| `[H]` Điều kiện | NSD là CB nghiệp vụ cấp TW + có ≥1 báo cáo từ Bộ/Ngành hoặc Địa phương **đã gửi lên** |
| `[J]` Các bước | 1. Chọn menu "Đợt báo cáo" · 2. Chọn các báo cáo cần tổng hợp trong bảng danh sách (ô chọn) + bấm "Tổng hợp" · 3. Bấm "Lưu tổng hợp" |
| `[K]` KQ mong đợi | (K1) Lưu bản ghi báo cáo tổng hợp toàn quốc · (K2) Chuyển trạng thái các đợt báo cáo đã chọn: Đã gửi TW → Đã tổng hợp · (K3) Lưu vết thao tác · (K4) Thông báo "Đã tổng hợp báo cáo toàn quốc" |
| `[L]` KQ thực tế | **TRỐNG** |
| `[Q]` TKM phản hồi 1 | "Chưa thực hiện được do uc GKQTHCTHTPL_01 lỗi" ⇒ **đối tác chưa chạy lượt nào**, không có bằng chứng đối tác để so |
| `[R]` Trạng thái dev fix | `BA confirm` |
| `[S]` DEV phản hồi 1 | Dev tự fix theo SRS (BA không phải quyết). Căn cứ câu thông báo: `INF-XI-09-01`. **Dev đã sửa: danh sách tổng hợp trả đúng bản ghi báo cáo của từng đơn vị (trước đó gộp sai theo đợt).** |

**Phạm vi đo lượt này (user chốt):** chỉ (1) 3 bước ở `[J]` chấm theo `[K]`, và (2) hai điểm Dev khai ở `[S]`
— (S-a) câu thông báo có đúng `INF-XI-09-01` không; (S-b) danh sách tổng hợp có trả đúng bản ghi báo cáo
**của từng đơn vị** (không gộp theo đợt) không.

**Điểm treo của lượt trước (ô `[T]`, chạy 13:30–13:45 trên bản dựng CŨ `index-eWHwDgt2.js`):** trục ĐỢT
chuyển thẳng `Tạo đợt → Đã tổng hợp` (không đi qua "Đã gửi TW"), trục ĐƠN VỊ giữ "Đã nộp", trục BÁO CÁO
chuyển "Đã gửi TW → Đã tổng hợp"; đặc tả tự mâu thuẫn ⇒ lượt đó chốt `BA confirm`.

## 2. Môi trường · bản dựng · tài khoản

| Mục | Giá trị |
|---|---|
| Env | `https://18.143.165.120.nip.io` (nội bộ) |
| **Bản dựng TRƯỚC lượt đo** (đo 20:53:26 giờ VN 07/08/2026) | `index-BbPPdate.js` — `last-modified Fri, 07 Aug 2026 06:47:57 GMT` = **13:47:57 giờ VN** |
| **Bản dựng SAU lượt đo** (đo 21:14:45) | `index-BbPPdate.js` — `06:47:57 GMT` = 13:47:57 giờ VN — **TRÙNG hai đầu** (§9) |
| Tài khoản ra verdict | `cbnv_tw_05` — CB Nghiệp vụ Trung ương (`CB_NV_TW`), Cục Bổ trợ tư pháp. Đăng nhập 20:55, mã xác thực lấy ở hộp thư giả lập |
| Nhãn phiên bản trên giao diện | `HTPLDN · V1.0.10` |
| Mốc giờ đo | **20:53 → 21:14** ngày 07/08/2026 (giờ VN) |
| Tài khoản chỉ để ĐỌC, không ra verdict | `cbpd_bn_03` + `cbnv_bn_03` (dựng tiền đề) · `cbnv_dp_05` (đọc chéo bằng phiên đơn vị An Giang) · `admin` (**chỉ đọc** Nhật ký hệ thống ở §7) |

## 3. Tiền đề — lượt trước đã tiêu, phải dựng lại

**Vì sao phải dựng lại:** đợt `DOT-THBC01-UAT` mà ô `[T]` mô tả **đã bị chính lượt 13:30 tiêu hết** —
kiểm sống lúc 20:56 (`GET /api/v1/dot-bao-caos/tong-hop` bằng phiên `cbnv_tw_05`): cả hai báo cáo
`c4801d2d…` (Bộ KH&ĐT) và `df6498aa…` (Sở TP An Giang) đã ở `DA_TONG_HOP`, không tổng hợp lại được.
Cả danh sách chỉ còn **1** báo cáo `DA_GUI_TW` (Sở TP Hà Nội) ⇒ không đủ để đo vế "chọn **các** báo cáo".

**Đã tự dựng tiền đề mới** (đúng luật 5 của brief — thiếu thì tạo, không kết luận blocker), dùng đợt
`DOT-SO_BO_NAM-2026-1` (`e9909d96-1391-463b-8072-b1b56c319f8e`, kỳ **Sơ bộ năm**, biểu mẫu **21a**):

| Bước dựng | Tài khoản | Kết quả |
|---|---|---|
| Phê duyệt nội bộ báo cáo của Bộ KH&ĐT (`c19b1bc2…`) | `cbpd_bn_03` (CB Phê duyệt - Bộ ngành, Bộ KH&ĐT) — phiên riêng, cách ly | 200 · nộp `CHO_DUYET → DA_DUYET` |
| Gửi báo cáo lên Trung ương | `cbnv_bn_03` (CB Nghiệp vụ - Bộ ngành, Bộ KH&ĐT) — phiên riêng, cách ly | 200 lúc **20:58:35** · báo cáo vào danh sách tổng hợp của TW ở `DA_GUI_TW` |

> Hai tài khoản trên **chỉ dùng để dựng tiền đề**, không ra verdict. Toàn bộ 3 bước của phiếu do
> `cbnv_tw_05` bấm trên giao diện thật.

### 3.1 Trạng thái BA TRỤC **trước** khi bấm (đọc 20:59:02 bằng chính phiên `cbnv_tw_05`)

| Trục | Giá trị trước |
|---|---|
| **ĐỢT** `DOT-SO_BO_NAM-2026-1` | `TAO_DOT` · `version 1` · `daGuiTw = false` · `ngayGuiTw = null` |
| **ĐƠN VỊ** (bảng tiến độ nộp) | Bộ KH&ĐT = `DA_NOP` · Sở TP Hà Nội = `DA_NOP` · Sở TP An Giang = `CHO_DUYET` · 80 đơn vị còn lại `CHUA_NOP` |
| **BÁO CÁO** (danh sách tổng hợp của TW) | Bộ KH&ĐT `c19b1bc2…` = **`DA_GUI_TW`** · Sở TP Hà Nội `4db99158…` = **`DA_GUI_TW`** |

Danh sách tổng hợp của TW lúc này có **4 dòng**: 2 dòng của đợt `DOT-THBC01-UAT` (đã `DA_TONG_HOP`,
tồn dư của lượt 13:30) + 2 dòng `DA_GUI_TW` của đợt `DOT-SO_BO_NAM-2026-1` vừa dựng.

## 4. Đường đi thực tế của 3 bước trong phiếu

| Bước phiếu | Đã làm gì | Ghi nhận |
|---|---|---|
| **B1** "Chọn menu Đợt báo cáo" | Bấm mục **Đợt báo cáo** trên thanh menu trái → `/ct-htpldn/dot-bao-cao`, bảng 4 đợt hiện đúng | ✅ menu tồn tại, mở được |
| — | Mở chi tiết đợt `DOT-SO_BO_NAM-2026-1` → cuối màn có nút **[Tổng hợp]**. Bấm thử: hiện hộp xác nhận *"Tổng hợp báo cáo? Đợt sẽ chuyển sang Đã tổng hợp"* — **KHÔNG có ô chọn, KHÔNG có [Lưu tổng hợp]** ⇒ đây là lối tổng hợp **cả đợt**, không phải luồng của phiếu. **Đã bấm [Hủy]**, 0 yêu cầu gửi đi, tiền đề còn nguyên | ảnh 03 |
| **B2** "Chọn các báo cáo … (ô chọn) + bấm Tổng hợp" | Màn có ô chọn + nút [Tổng hợp] là **"Tổng hợp báo cáo toàn quốc"** (`/ct-htpldn/tong-hop`). Màn này **không có mục nào trên menu trái và không có nút dẫn** từ màn Đợt báo cáo hay màn Chương trình HTPLDN ⇒ phải gõ thẳng địa chỉ mới vào được (điểm này đã nêu ở phiếu THBCTHCT_02, không chấm ở đây) | ảnh 04 |
| **B3** "Bấm Lưu tổng hợp" | Tick đúng 2 dòng của đợt `DOT-SO_BO_NAM-2026-1` → nút đổi thành **[Tổng hợp (2)]** → hộp gợi ý số liệu → nhập nhận xét (xem §6.3) → **[Lưu tổng hợp]** lúc **21:04:31** | ảnh 05, 06, 07 |

## 5. Chấm từng ý của cột `[K]`

### K1 — "Lưu bản ghi báo cáo tổng hợp toàn quốc" → ✅ ĐẠT

Máy chủ trả **201** và tạo mới bản ghi:

| Trường | Giá trị |
|---|---|
| `id` | `7e7e6b7d-ec22-4e1a-b244-f95fd3a7b383` |
| `maBaoCao` | `TH-TW-1786111471109` |
| `loai` | **`TONG_HOP_TW`** |
| `dotBaoCaoId` | `e9909d96…` (đúng đợt `DOT-SO_BO_NAM-2026-1`) |
| `donViId` / `donViNopId` | `00000000-0000-4000-8000-000000000001` — Cục Bổ trợ tư pháp (cấp TW) |
| `bieuMauSuDung` | `MAU_21A` |
| `ngayTao` | `2026-08-07T14:04:31.101Z` = **21:04:31 giờ VN** |
| `soLieuTongHop` | 0·0·0·0·0·0·0·0·0·0·0·**1207**·**1308** — **trùng khít** 13 ô trên biểu lúc bấm |

Đặc tả: `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-15-ct-htpldn.md:1004`
= `| 6 | Lưu bản ghi BC tổng hợp toàn quốc (loại TONG_HOP_TW) | — |` (đã mở file đọc, không quote từ trí nhớ).

### K4 — thông báo "Đã tổng hợp báo cáo toàn quốc" → ✅ ĐẠT, đúng nguyên văn

Bộ bắt thông báo `tools/toast-capture.js` cài **trước** khi bấm, tự kiểm `soObserverDangSong = 1` (hợp lệ,
không nhân bản), không lọc trùng, đọc `innerText`:

```
SO_REQUEST = 1   → POST /api/v1/dot-bao-caos/tong-hop
SO_KHUNG   = 1   → "Đã tổng hợp báo cáo toàn quốc"
```

⇒ 1 lượt bấm = 1 yêu cầu = 1 thông báo, **không lặp**. Chuỗi hiển thị **trùng khít từng chữ** với đặc tả
`srs-fr-15-ct-htpldn.md:1032` = `| I1 | Tổng hợp thành công | INF-XI-09-01 | "Đã tổng hợp báo cáo toàn quốc" | INFO |`.

⇒ **Điểm (S-a) Dev khai — ĐÚNG.**

### K2 — "Chuyển trạng thái các đợt báo cáo đã chọn: Đã gửi TW → Đã tổng hợp" → ❌ **KHÔNG ĐẠT** (lỗi mới, nặng)

**Thân yêu cầu gửi đi chỉ có ĐÚNG 2 mã báo cáo:**
```
{"baoCaoIds":["4db99158-…" (Sở TP Hà Nội), "c19b1bc2-…" (Bộ KH&ĐT)], "soLieuTongHop":{…}}
```

**Nhưng sau khi lưu, danh sách có 5 dòng thay vì 4** — xuất hiện thêm **Sở Tư pháp An Giang** của chính
đợt đó, mang nhãn **"Đã tổng hợp"**, cột "Ngày gửi TW" để **trống (–)**:

| Dòng trên màn tổng hợp của TW | Trước (20:59) | Sau (21:05, đã tải lại toàn bộ trang) |
|---|---|---|
| Bộ KH&ĐT `c19b1bc2…` — **có chọn** | "Đã gửi TW" | "Đã tổng hợp" ✅ đúng |
| Sở TP Hà Nội `4db99158…` — **có chọn** | "Đã gửi TW" | "Đã tổng hợp" ✅ đúng |
| **Sở TP An Giang `c1b1045d…` — KHÔNG chọn** | **không có dòng nào trong danh sách**; trục đơn vị = `CHO_DUYET`; `ngayGuiTw = null` (**chưa từng gửi TW**) | **có dòng, nhãn "Đã tổng hợp"**, "Ngày gửi TW" vẫn trống ❌ **sai** |
| ĐỢT `DOT-SO_BO_NAM-2026-1` | `TAO_DOT` `v1` · `daGuiTw=false` | `DA_TONG_HOP` `v2` · `daGuiTw` vẫn `false` |
| Trục ĐƠN VỊ (bảng tiến độ nộp) | KH&ĐT `DA_NOP` · HN `DA_NOP` · **An Giang `CHO_DUYET`** | không đổi — An Giang **vẫn `CHO_DUYET`** |

Hai điểm sai độc lập nhau, đều nhìn thấy được trên màn hình cán bộ TW:
1. **Mục KHÔNG được chọn vẫn bị gán nhãn "Đã tổng hợp"** — phiếu ghi rõ chỉ "các đợt báo cáo **đã chọn**"
   mới chuyển; đặc tả `:1005` cũng vậy.
2. **Mục CHƯA gửi lên TW cũng bị hút vào danh sách và đóng dấu "Đã tổng hợp"** — trong khi đầu vào của
   chính chức năng chỉ gồm báo cáo đã gửi TW (`:993`) và danh sách chỉ gồm BC **đã gửi** (`:1000`).
   An Giang đang **chờ đơn vị mình duyệt nội bộ**, chưa gửi đi, mà đã bị tính là đã tổng hợp toàn quốc.

> **Nói chính xác cái gì hỏng (đo tiếp ở §6.1):** bản ghi báo cáo của An Giang trong dữ liệu **KHÔNG bị
> sửa** — đọc bằng phiên của chính đơn vị đó vẫn thấy `CHO_PHE_DUYET`. Cái sai nằm ở **màn tổng hợp của
> cấp TW**: nó lấy danh sách và suy trạng thái **theo ĐỢT** thay vì theo từng bản báo cáo. Hậu quả nghiệp
> vụ vẫn nguyên: cán bộ TW nhìn màn này sẽ tưởng đơn vị đã nộp và đã được tổng hợp.

⇒ Về đúng điểm Dev khai ở ô `[S]` — *"danh sách tổng hợp trả đúng bản ghi báo cáo của từng đơn vị (trước
đó gộp sai theo đợt)"*: đã **tách dòng** theo đơn vị (đạt, xem ngay dưới), nhưng **thành viên danh sách và
cột trạng thái vẫn tính theo ĐỢT** ⇒ việc "gộp theo đợt" **chưa sửa hết**, và phần chưa sửa chính là
nguyên nhân của K2.

### Điểm (S-b) Dev khai — "danh sách trả đúng bản ghi của từng đơn vị" → ✅ ĐẠT (phần đọc)

Màn "Tổng hợp báo cáo toàn quốc" có cột đầu là **"Đơn vị"**, cột thứ hai là "Mã đợt"; **cùng một mã đợt
`DOT-SO_BO_NAM-2026-1` hiện thành 2 dòng riêng** cho Bộ KH&ĐT và Sở TP Hà Nội, mỗi dòng có ngày gửi TW và
trạng thái riêng, ô chọn riêng (ảnh 04). ⇒ không còn gộp theo đợt ở phần hiển thị/chọn.

## 6. Kiểm chứng lại bằng đường khác — 2 phép thử độc lập

### 6.1 Đọc bằng phiên đăng nhập của CHÍNH đơn vị bị kéo theo (Sở TP An Giang)

Đăng nhập `cbnv_dp_05` (CB Nghiệp vụ - Địa phương, `donViId …8002-000000000006` = Sở Tư pháp An Giang),
phiên **cách ly hoàn toàn** với phiên TW, đọc lại đợt `DOT-SO_BO_NAM-2026-1` lúc 21:07:

| Trường | Giá trị |
|---|---|
| Trạng thái ĐỢT | `DA_TONG_HOP` |
| `trangThaiNop` của An Giang | **`CHO_DUYET`** — không đổi |
| Trạng thái **bản ghi báo cáo** `c1b1045d…` của An Giang | **`CHO_PHE_DUYET`** — **không đổi** |

⇒ Kết luận chính xác: **bản ghi báo cáo của An Giang KHÔNG bị sửa trong dữ liệu.** Cái sai nằm ở **màn
"Tổng hợp báo cáo toàn quốc" của cấp TW**: màn này (a) **hút cả báo cáo chưa gửi TW vào danh sách** ngay khi
đợt được đóng dấu tổng hợp, và (b) **hiển thị trạng thái theo ĐỢT chứ không theo từng bản ghi** nên gán
nhãn "Đã tổng hợp" cho cả đơn vị chưa nộp. Đây đúng là phần "gộp theo đợt" mà Dev khai đã sửa — sửa được
việc **tách dòng theo đơn vị**, chưa sửa việc **trạng thái/danh sách vẫn tính theo đợt**.

> Cột "Trạng thái" của màn này vốn **không phải** trường trạng thái của bản ghi báo cáo: trước khi tổng hợp,
> báo cáo Bộ KH&ĐT có trạng thái bản ghi là `DA_DUYET` nhưng màn TW hiển thị "Đã gửi TW". Tức cột này là giá
> trị **suy ra**, và nay nó suy từ trạng thái ĐỢT.

### 6.2 Lượt đo thứ hai — đợt khác, đơn vị ở trạng thái khác → **TÁI HIỆN**

Dựng tiền đề thứ hai trên đợt `DOT-SO_BO_6_THANG-2026-1` (`a61e07f1…`, kỳ Sơ bộ 6 tháng, biểu 21a):
`cbpd_bn_03` duyệt + `cbnv_bn_03` gửi TW báo cáo Bộ KH&ĐT (`a63bf70c…`) lúc 21:10:29. Đơn vị thứ hai của đợt
— **Sở TP An Giang (`f445b699…`) đang ở `DANG_LAP`** (đơn vị còn đang soạn, chưa trình duyệt nội bộ, chưa
gửi TW) và **không hiện trong danh sách tổng hợp**.

Chạy lại đúng 3 bước của phiếu, **chỉ tick đúng 1 dòng** (Bộ KH&ĐT). Thân yêu cầu gửi đi:
```
{"baoCaoIds":["a63bf70c-9ed0-4587-b5e2-9b9689dfa94c"], …}
```
Kết quả lúc 21:11:43 — bản ghi tổng hợp `TH-TW-1786111903529` được tạo, thông báo đúng 1 lần
"Đã tổng hợp báo cáo toàn quốc", **và danh sách nhảy từ 6 lên 7 dòng**: Sở TP An Giang của đợt
`DOT-SO_BO_6_THANG-2026-1` xuất hiện với "Ngày gửi TW" = **–** và trạng thái **"Đã tổng hợp"** (ảnh 10,
chụp sau khi tải lại toàn bộ trang). Trục đơn vị của An Giang vẫn `DANG_LAP`.

⇒ **Tái hiện 2/2 lượt, trên 2 đợt độc lập, với đơn vị ở 2 trạng thái khác nhau (`CHO_DUYET` và `DANG_LAP`).**
Không phải hiện tượng ngẫu nhiên của một bộ dữ liệu.

### 6.3 Một điểm KHÔNG phải lỗi của phần mềm — tự bắt được, khai để khỏi hiểu nhầm

Ở lượt 1, ô "Nhận xét, kiến nghị" tôi điền bằng lệnh đổ giá trị của công cụ đo → thân yêu cầu **không kèm**
`nhanXet`, bản ghi lưu `nhanXet = null`. Ở lượt 2 tôi **gõ bằng bàn phím** vào chính ô đó → `nhanXet` được
gửi và **lưu đúng nguyên văn**. ⇒ đây là **giới hạn của công cụ đo**, KHÔNG phải lỗi phần mềm. **Không log.**

## 7. K3 — "Lưu vết thao tác theo quy định" → ✅ ĐẠT

Đọc Nhật ký hệ thống bằng tài khoản `admin` (**CHỈ ĐỌC**, không ra verdict — tài khoản nghiệp vụ không có
quyền xem nhật ký, đây là phân quyền đúng). Ngày 07/08/2026 có **đúng 2 mục `TONG_HOP`**, khớp đúng 2 lượt bấm:

| Mục | `entityId` | `thoiGian` | Người thực hiện |
|---|---|---|---|
| `4b490e14…` | `7e7e6b7d…` = bản ghi lượt 1 | `14:04:31.101Z` = **21:04:31** VN | `cbnv_tw_05` · CB Nghiệp vụ - Trung ương #05 · vai trò "Cán bộ Nghiệp vụ TW" · Cục Bổ trợ tư pháp - Bộ Tư pháp |
| `1b8f82dc…` | `b23ac4e1…` = bản ghi lượt 2 | `14:11:43.523Z` = **21:11:43** VN | như trên |

`module = DOT_BAO_CAO`, `entityType = BAO_CAO_CT_HTPL`. Đối chiếu chéo: `entityId` + `thoiGian` **trùng khít**
`id` + `ngayTao` trong phản hồi 201 của chính hai lượt bấm.

Đặc tả: `srs-fr-15-ct-htpldn.md:1007` = `| 9 | Ghi nhật ký thao tác | BR-DATA-05 |`.

*Ghi nhận (không chấm):* ba trường `ipAddress`, `endpoint`, `responseCode` đều `null` — phiếu và `:1007`
không đòi, giống hệt ghi nhận của lượt 13:30.

## 8. Quote đặc tả — đã mở file đọc, xác minh từng số dòng

Nguồn: `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-15-ct-htpldn.md` (FR-XI-09, UC170).

| Dòng | Nguyên văn |
|---|---|
| `:993` | `\| 1 \| bao_cao_ids \| identifier[] \| Y \| FK → BAO_CAO_CT_HTPL, da_gui_tw = true \| — \| Checkbox chọn \|` |
| `:1000` | `\| 2 \| Hiển thị danh sách BC từ BN + ĐP đã gửi \| — \|` |
| `:1004` | `\| 6 \| Lưu bản ghi BC tổng hợp toàn quốc (loại TONG_HOP_TW) \| — \|` |
| `:1005` | `\| 7 \| Chuyển các đợt BC đã chọn sang DA_TONG_HOP \| SM-DOT-BC \|` |
| `:1007` | `\| 9 \| Ghi nhật ký thao tác \| BR-DATA-05 \|` |
| `:1010` | `- **SM-DOT-BC**: Transition DA_GUI_TW → DA_TONG_HOP → Xem Phụ lục C (file chính)` |
| `:1032` | `\| I1 \| Tổng hợp thành công \| INF-XI-09-01 \| "Đã tổng hợp báo cáo toàn quốc" \| INFO \|` |

Ba căn cứ trực tiếp cho phần KHÔNG ĐẠT: `:993` (đầu vào **chỉ** gồm báo cáo `da_gui_tw = true`), `:1000`
(danh sách **chỉ** gồm BC **đã gửi**), `:1005` (**chỉ** các mục **đã chọn** mới chuyển trạng thái).

## 9. Bản dựng SAU lượt đo

`curl` lúc **21:14:45** ngày 07/08/2026 → `index-BbPPdate.js`, `last-modified Fri, 07 Aug 2026 06:47:57 GMT`
= **13:47:57 giờ VN**. **TRÙNG** với nhãn đo trước lượt (20:53:26) ⇒ toàn bộ lượt đo nằm trọn trên **một**
bản dựng, và đúng là bản mới (lượt cũ ở ô `[T]` chạy trên `index-eWHwDgt2.js` — bản 09:11). Tab đo cũng đã
được **tải lại toàn bộ trang** trước mỗi lượt, `script[src]` đọc tại trang xác nhận đang chạy `index-BbPPdate.js`.

## 10. Tổng kết từng ý → verdict

| Ý | Nguồn | Kết quả đo |
|---|---|---|
| **K1** Lưu bản ghi tổng hợp toàn quốc | phiếu `[K]` + `:1004` | ✅ **ĐẠT** — 2/2 lượt tạo đúng bản ghi `TONG_HOP_TW`, số liệu trùng khít biểu |
| **K2** Chuyển trạng thái **các đợt báo cáo đã chọn** Đã gửi TW → Đã tổng hợp | phiếu `[K]` + `:993`, `:1000`, `:1005` | ❌ **KHÔNG ĐẠT** — mục **không chọn** và **chưa gửi TW** cũng bị gán "Đã tổng hợp". Tái hiện 2/2 lượt |
| **K3** Lưu vết thao tác | phiếu `[K]` + `:1007` | ✅ **ĐẠT** — đúng 1 mục/lượt, đúng bản ghi, đúng giờ, đúng người |
| **K4** Thông báo "Đã tổng hợp báo cáo toàn quốc" | phiếu `[K]` + `:1032` | ✅ **ĐẠT** — đúng nguyên văn, 1 yêu cầu = 1 thông báo, 2/2 lượt |
| **S-a** Câu thông báo theo `INF-XI-09-01` | ô `[S]` | ✅ **ĐÚNG như Dev khai** |
| **S-b** Danh sách trả đúng bản ghi của **từng đơn vị** | ô `[S]` | ⚠️ **ĐÚNG MỘT NỬA** — phần hiển thị/chọn đã tách theo đơn vị (đạt); nhưng **thành viên danh sách và cột trạng thái vẫn tính theo ĐỢT** nên sinh lỗi ở K2 |

### VERDICT: `Reopen`

Theo bảng chốt verdict của brief: *"việc Dev khai đã làm ở ô S mà đo ra **chưa làm / làm sai** → `Reopen`"*
và *"có ≥1 ý Reopen → tổng Reopen"*. Ở đây **cả hai điều kiện** đều thoả: một ý của cột `[K]` (K2) đo ra sai,
và điểm Dev khai đã sửa (S-b, hết gộp theo đợt) mới sửa được một nửa — phần còn lại chính là nguyên nhân
sinh lỗi. Đây **không** phải chỗ "đặc tả im lặng chờ BA": `:993`, `:1000`, `:1005` nói rõ cả ba mặt (chỉ
báo cáo đã gửi TW · chỉ mục đã chọn · danh sách chỉ gồm BC đã gửi), nên **không giữ `BA confirm`**.

> **Verdict này KHÔNG phụ thuộc câu hỏi nghiệp vụ còn treo (trục ĐỢT hay trục BÁO CÁO).** Dù sau này BA
> chốt theo hướng nào, vẫn còn một vi phạm **đặc tả nói rõ, không im lặng**: `:1000` quy định danh sách của
> màn này chỉ gồm **BC đã gửi**, `:993` quy định đầu vào chỉ gồm báo cáo `da_gui_tw = true`. Báo cáo An Giang
> có `ngayGuiTw = null`, cột "Ngày gửi TW" trên màn để trống, đơn vị còn đang `CHO_DUYET`/`DANG_LAP` —
> **chưa từng gửi lên TW** — mà vẫn nằm trong danh sách tổng hợp toàn quốc và mang nhãn "Đã tổng hợp".
> Vì vậy đây là lỗi chấm được ngay, không phải điểm chờ BA.

> **Khác gì với lượt 13:30 (ô `[T]`)?** Lượt đó tiền đề chỉ có **đúng 2 đơn vị** trong đợt và **cả hai đều
> được chọn**, nên không có đơn vị thứ ba để lộ ra việc bị kéo theo — do đó lượt đó chỉ thấy phần "đường đi
> trạng thái của ĐỢT" và xếp là điểm cần BA. Lượt này tiền đề có **đơn vị thứ ba chưa gửi TW**, nên lỗi lộ ra.
> Câu hỏi nghiệp vụ cũ (trục ĐỢT / ĐƠN VỊ / BÁO CÁO) vẫn còn nguyên giá trị nhưng **không còn là điểm chốt**
> của phiếu này nữa — đã có lỗi cụ thể chặn trước.

## 11. Dữ liệu đã thay đổi trên môi trường nội bộ (khai đủ)

| Đối tượng | Trước | Sau | Do |
|---|---|---|---|
| BC Bộ KH&ĐT `c19b1bc2…` (đợt SO_BO_NAM) | `CHO_PHE_DUYET`, chưa gửi TW | duyệt + gửi TW | **dựng tiền đề** (`cbpd_bn_03`, `cbnv_bn_03`) |
| BC Bộ KH&ĐT `a63bf70c…` (đợt SO_BO_6_THANG) | `CHO_PHE_DUYET`, chưa gửi TW | duyệt + gửi TW | **dựng tiền đề** lượt 2 |
| Đợt `DOT-SO_BO_NAM-2026-1` | `TAO_DOT` `v1` | `DA_TONG_HOP` `v2` | [Lưu tổng hợp] 21:04:31 |
| Đợt `DOT-SO_BO_6_THANG-2026-1` | `TAO_DOT` `v1` | `DA_TONG_HOP` `v2` | [Lưu tổng hợp] 21:11:43 |
| Bản ghi mới `7e7e6b7d…` `TH-TW-1786111471109` | không có | được tạo | lượt 1 |
| Bản ghi mới `b23ac4e1…` `TH-TW-1786111903529` | không có | được tạo | lượt 2 |
| BC Sở TP An Giang `c1b1045d…` và `f445b699…` | `CHO_PHE_DUYET` / `DANG_LAP` | **bản ghi KHÔNG đổi**, nhưng màn TW hiển thị "Đã tổng hợp" | chính là lỗi đang báo |

Không đụng dữ liệu của bên nghiệm thu. Không ghi thẳng cơ sở dữ liệu. Không ép trạng thái bằng đường dữ liệu.

**Hệ quả cho lô sau:** cả 3 đợt `DOT-THBC01-UAT`, `DOT-SO_BO_NAM-2026-1`, `DOT-SO_BO_6_THANG-2026-1` đã
`DA_TONG_HOP`. Còn đợt `DOT-TRON_NAM-2026-1` (`a63a3214…`, kỳ Tròn năm, biểu **CA_HAI**) ở `TAO_DOT`, có
BC Sở TP Hà Nội `1b3085b8…` đang `DANG_LAP` — muốn dựng tiền đề mới thì đi từ đó.

## 12. Ảnh bằng chứng

| # | Tệp trong `image/` | Chứng minh điều gì |
|---|---|---|
| 01 | `THBCTHCT_01-01-menu-dot-bao-cao-truoc-khi-bam.png` | Bước 1 của phiếu: menu **Đợt báo cáo** mở được; đợt `DOT-SO_BO_NAM-2026-1` đang ở "Tạo đợt" |
| 02 | `THBCTHCT_01-02-chi-tiet-dot-truoc-khi-bam-tao-dot.png` | Trạng thái **trước**: đợt ở bước 1 "Tạo đợt"; Bộ KH&ĐT "Đã nộp", An Giang "Chờ duyệt" |
| 03 | `THBCTHCT_01-03-hop-xac-nhan-tong-hop-tu-chi-tiet-dot.png` | Nút [Tổng hợp] ở màn chi tiết đợt chỉ mở hộp xác nhận cả đợt — không phải luồng của phiếu; đã bấm Hủy |
| 04 | `THBCTHCT_01-04-danh-sach-tong-hop-theo-tung-don-vi.png` | **Điểm Dev khai (S-b) phần đọc — ĐẠT**: cùng 1 mã đợt hiện thành 2 dòng riêng theo đơn vị, mỗi dòng 1 ô chọn |
| 05 | `THBCTHCT_01-05-da-tick-2-don-vi-nut-tong-hop-2.png` | Đã tick **đúng 2** dòng, nút đổi thành [Tổng hợp (2)] |
| 06 | `THBCTHCT_01-06-form-tong-hop-goi-y-so-lieu.png` | Biểu tổng hợp: "Số đơn vị 2", 13 chỉ tiêu gợi ý, nút [Lưu tổng hợp] |
| 07 | `THBCTHCT_01-07-ngay-sau-luu-tong-hop-thong-bao.png` | **Ngay sau [Lưu tổng hợp] lượt 1**: danh sách nhảy từ 4 lên **5 dòng** — An Giang (không chọn, ngày gửi TW trống) đã mang nhãn "Đã tổng hợp" |
| 08 | `THBCTHCT_01-08-luot2-form-1-don-vi-da-go-nhan-xet.png` | Lượt 2: biểu tổng hợp "Số đơn vị **1**", đã gõ nhận xét bằng bàn phím |
| 09 | `THBCTHCT_01-09-sau-tai-lai-trang-2-don-vi-bi-keo-theo.png` | **Sau khi tải lại toàn bộ trang bằng địa chỉ**: dòng An Giang của đợt `DOT-SO_BO_NAM-2026-1` (lỗi lượt 1) **vẫn còn** — không phải hiển thị tạm |
| 10 | `THBCTHCT_01-10-luot2-dong-an-giang-dang-lap-da-tong-hop.png` | **Ảnh chốt lượt 2**: dòng cuối — Sở TP An Giang / `DOT-SO_BO_6_THANG-2026-1` / Ngày gửi TW "–" / **"Đã tổng hợp"**, dù đơn vị đang `DANG_LAP` và tôi chỉ chọn 1 dòng |

Ảnh 04 chứng minh phần Dev đã sửa; ảnh 07 + 09 + 10 chứng minh phần chưa sửa.

> **Đã đối chiếu mã băm (md5) toàn bộ 10 ảnh — không có hai ảnh trùng nhau.** Một ảnh chụp "sau khi tải lại
> trang" của lượt 1 ban đầu **trùng byte** với ảnh 07 (màn hình không đổi một điểm ảnh nào), nên đã **bỏ**
> để không có hai chú thích khác nhau trỏ về cùng một ảnh; vai trò chứng minh "lỗi còn sau khi tải lại
> trang" nay do **ảnh 09** đảm nhiệm (ảnh này chụp sau một lần tải lại toàn bộ trang khác và vẫn hiện
> nguyên dòng lỗi của lượt 1).

## 13. Ngoài tiêu chí đang chấm — có gì bất thường?

1. **Màn "Tổng hợp báo cáo toàn quốc" không có lối vào** — không có mục trên menu trái, không có nút dẫn từ
   màn Đợt báo cáo hay Chương trình HTPLDN; phải gõ thẳng địa chỉ. *(Đã nêu ở phiếu THBCTHCT_02 — không mở
   trùng, chỉ nhắc.)*
2. **Hai lối "Tổng hợp" khác nhau, dễ nhầm:** nút [Tổng hợp] ở màn chi tiết đợt tổng hợp **cả đợt** ngay sau
   một hộp xác nhận (không chọn đơn vị, không nhập số liệu, không có [Lưu tổng hợp]); còn luồng của phiếu ở
   màn riêng. Hai lối cùng tên, cùng đích, khác hẳn hành vi.
3. **Câu chữ trong hộp tổng hợp gọi sai đối tượng:** *"Sau khi lưu, 2 **đợt báo cáo** được chọn sẽ chuyển
   sang trạng thái Đã tổng hợp"* — thực chất là **2 báo cáo của 2 đơn vị trong CÙNG 1 đợt**. Nhiều khả năng
   cùng gốc với lỗi ở K2 (vẫn tư duy theo đợt).
4. **Nhãn đường dẫn "Tong Hop" không dấu** trên thanh điều hướng của màn này (các màn khác đều có dấu).
5. **Chưa có đường xem lại bản ghi tổng hợp** sau khi lưu *(đã nêu ở lượt 13:30 — nhắc lại, không mở trùng)*.

Các mục 2–4 là **ghi nhận cho dev**, không chấm vào phiếu này vì nằm ngoài `[J]`/`[K]`/`[S]`.
