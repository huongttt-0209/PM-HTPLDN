# GIAI ĐOẠN B — số đo thô · `QLHSPLDN_12` (tab `bug`, dòng 294 — "Tìm kiếm hồ sơ pháp lý không có kết quả")

```
Lô:            F9 — tái xác nhận trên env NGHIỆM THU của đối tác
Flow:          flows/03-reverify-sau-dev-fix.md — NHÁNH 2 "Tái xác nhận trên môi trường khác"
Nguồn chuẩn:   chuan/QLHSPLDN_12.md (Giai đoạn A đã khoá) — làm đúng theo, không tự thêm/bớt vế
Env đo:        https://htpldn-uat.ospgroup.vn  (env nghiệm thu của đối tác)
Người đo:      agent ĐO · 2026-08-07 · phiên 14:33 → 14:36 giờ VN
```

---

## 1. Vân tay bản dựng — ĐẦU và CUỐI case

| Hạng mục | ĐẦU case — **14:33:30 VN 07/08** | CUỐI case — **14:36:37 VN 07/08** |
|---|---|---|
| Bó mã JS (máy chủ đang phát) | `assets/index-D4NhKEjr.js` | `assets/index-D4NhKEjr.js` |
| Bó mã CSS | `assets/index-DVlgOkLg.css` | `assets/index-DVlgOkLg.css` |
| `GET /` `last-modified` | `Fri, 07 Aug 2026 04:17:55 GMT` (= 11:17 VN) | `Fri, 07 Aug 2026 04:17:55 GMT` |
| `GET /` `etag` | `W/"6a755c73-428"` | `W/"6a755c73-428"` |
| Máy chủ web | `nginx` | `nginx` |
| Chuỗi chân sidebar | `HTPLDN · V1.0.10` | `HTPLDN · V1.0.10` |
| **Thẻ script đang nạp trong tab** | `/assets/index-D4NhKEjr.js` | `/assets/index-D4NhKEjr.js` |

> ✅ **Hai đầu TRÙNG KHỚP tuyệt đối** ⇒ không có deploy chen giữa case ⇒ không phải khai quan sát nào rơi
> trước/sau mốc deploy. Trùng luôn vân tay ba case `_06` / `_07` / `_11` đo trước cùng phiên.
>
> ✅ **Đã loại bẫy "tab mở lâu vẫn chạy mã cũ" mà KHÔNG cần tải lại trang:** đọc trực tiếp
> `document.querySelectorAll('script[src]')` trong tab → đúng **`/assets/index-D4NhKEjr.js`**, trùng khít bó mã máy
> chủ đang phát ở **cả hai đầu**. Tên bó mã có băm nội dung ⇒ mã đang chạy trong tab **chính là** bản dựng hiện
> hành. (Không tải lại trang để khỏi tiêu thêm lượt đăng nhập — giới hạn 5 lượt/60s.)

---

## 2. Tài khoản thực dùng + xác nhận vai trò

| Hạng mục | Giá trị |
|---|---|
| Tài khoản | **`cbnv_tw`** (đúng tài khoản chỉ định, **không** phải fallback) |
| Cách vào phiên | **Dùng lại phiên đang sống** của các case trước cùng lô — kiểm sống bằng `GET /api/v1/auth/me` → **200** ở **cả đầu và cuối** case |
| Số lượt đăng nhập phát sinh trong case này | **0** — không chạm giới hạn 5 lượt/60s |
| `hoTen` | `Cán bộ NV Trung ương` |
| `vaiTro` | `["CB_NV_TW"]` |
| `capDonVi` | `TW` |
| `donViId` | `00000000-0000-4000-8000-000000000001` (= *Cục Bổ trợ tư pháp - Bộ Tư pháp*) |
| Badge trên màn (đọc được trong ảnh) | `Cán bộ NV Trung ương · Cán bộ Nghiệp vụ Trung ương` · phạm vi `BTP · TW` |

⇒ Khớp đúng vai trò/cấp trên bằng chứng của đối tác, và đúng tác nhân `srs-fr-12:565`.
**Không dùng `admin` ở bất kỳ bước nào.**

---

## 3. Bản ghi đã đọc / đã tạo / đã đổi

| Hạng mục | Số lượng |
|---|---|
| Bản ghi **TẠO MỚI** | **0** |
| Bản ghi **SỬA / XOÁ** | **0** |
| Bản ghi chỉ **ĐỌC** | 1 DN + 4 hồ sơ pháp lý |

Case chỉ đọc ⇒ đúng nguồn chuẩn §5: **không seed gì**. Toàn case phát sinh **1 lệnh `GET` nghiệp vụ** cho phép đo
quyết định (cộng vài lệnh đếm thông báo chạy nền của khung ứng dụng).

**Doanh nghiệp đo:** **`DN-XX-0005`** — *Công ty TNHH Mẫu Test* (`1a715c55-bc31-46de-ae07-56dd4f403ce5`), đúng DN
trong bằng chứng của đối tác và đúng DN nguồn chuẩn §5 chỉ định (dùng chung phiên với `QLHSPLDN_11`).

**4 hồ sơ của DN đó — CHỈ ĐỌC:**

| # | Mã hồ sơ | Tên hồ sơ | Loại | Trạng thái |
|---|---|---|---|---|
| 1 | `HSPL-20260804-0001` | QA-HSPL-V2-0408-742199 DA SUA vong 2 | `QUYET_DINH` | `HET_HAN` |
| 2 | `HSPL-20260803-0002` | Hồ sơ pháp lý doanh nghiệp XXX | `HOP_DONG` | `HIEU_LUC` |
| 3 | `HSPL-20260803-0001` | TKM hồ sơ pháp lý số 1 | `KHAC` | `HIEU_LUC` |
| 4 | `HSPL-20260731-0002` | Ho so x - SUA CU v2 742199 | `GIAY_CN` | `HIEU_LUC` |

> 🔴 **Tuân thủ kỷ luật dữ liệu §4 brief:** `DN-XX-0005`, `HSPL-20260803-0001`, `HSPL-20260731-0002` và mọi bản ghi
> khác **không bị sửa, không bị xoá, không thêm hồ sơ nào**. Không bấm `Xem` / `Sửa` / `Xoá` trên bất kỳ hàng nào.

**Đường UI đã đi:** dùng lại tab đang mở ở thẻ **Hồ sơ pháp lý** của `DN-XX-0005` → bấm **[Xóa bộ lọc]** để trả về
nền so sánh → gõ từ khóa rác vào ô *Tìm theo mã hoặc tên hồ sơ* → bấm **[Tìm kiếm]**. Không gõ thẳng URL.

---

## 4. Số đo thô

### 4.0 — Nền so sánh (baseline TRƯỚC khi lọc) · 14:34:26 VN

Bắt buộc theo nguồn chuẩn §6 điều kiện ①: không có mốc này thì "bảng rỗng" không phân biệt được **rỗng do lọc** với
**rỗng do chưa có dữ liệu**.

| Nguồn | Số đo |
|---|---|
| **Bảng trên màn** (đếm `tr.ant-table-row`) | **4 hàng** — `HSPL-20260804-0001` · `HSPL-20260803-0002` · `HSPL-20260803-0001` · `HSPL-20260731-0002` |
| **Phản hồi máy chủ** `GET /api/v1/ho-so-phap-ly-dns?doanhNghiepId=1a715c55-…&pageSize=100` → **200** | `meta.total` = **4**, `data[]` = **4**, cùng 4 mã |
| Ô từ khóa | **trống** (độ dài 0) |
| Hai ô chọn *Loại hồ sơ* / *Trạng thái* | **chưa chọn** (đang hiện chữ gợi ý xám) |

⇒ Nền so sánh đạt: **4 ≥ 1 dòng**, và không còn bộ lọc tồn dư nào từ case `_11`.

### 4.0b — Chứng minh từ khóa THẬT SỰ không khớp bản ghi nào

Nguồn chuẩn §5 đòi "phải chứng minh nó thật sự không khớp bản ghi nào" — không được suy đoán từ chuỗi trông có vẻ vô nghĩa.

Đã lấy **nguyên thân phản hồi máy chủ của nền so sánh** (đủ 4 bản ghi, đủ mọi trường) rồi dò chuỗi
`zzqqxx-khongtontai` **không phân biệt hoa-thường** trên **toàn bộ JSON của từng bản ghi**:

| Phép dò | Kết quả |
|---|---|
| Số bản ghi chứa chuỗi (dò toàn JSON, case-insensitive) | **0 / 4** |
| Chuỗi trong `maHoSo` của 4 hàng | không có |
| Chuỗi trong `tenHoSo` của 4 hàng | không có |
| Chuỗi trong `tenDoanhNghiep` (`Công ty TNHH Mẫu Test`) | không có |

⇒ Theo `srs-fr-12:593` (keyword tìm theo **mã HS, tên DN, tên HS**), tập kết quả đúng phải là **đúng 0 dòng**.

---

### 4.1 — PHÉP ĐO QUYẾT ĐỊNH · tìm với từ khóa không khớp · 14:35:18 VN

**Thao tác bằng UI thật:** gõ `zzqqxx-khongtontai` vào ô *Tìm theo mã hoặc tên hồ sơ* → bấm nút **[Tìm kiếm]**.

**Kiểm bẫy dụng cụ TRƯỚC khi bấm** (nguồn chuẩn §4 mục 1 — vòng trước đã đo hụt vì ô bị **nối chuỗi**):

| Kiểm | Kết quả |
|---|---|
| Cách điền | **clear ô trước** (đặt `''`), rồi đặt giá trị qua **setter gốc `HTMLInputElement.prototype.value`** + phát `input` và `change` — **không** dùng `fill_form` |
| Giá trị ô sau khi điền | `"zzqqxx-khongtontai"` — **độ dài 18**, đúng bằng độ dài chuỗi đích |
| Có bị nối vào giá trị cũ không? | **Không** — so bằng `===` với chuỗi đích: **true** |
| Bộ lọc khác có tồn dư không? | **Không** — hai ô chọn vẫn ở trạng thái chưa chọn (đọc trên ảnh chụp lẫn cây a11y) |
| Có lệnh tìm nào tự bắn lúc gõ không? | **Không** — 0 request cho tới khi bấm **[Tìm kiếm]** |

**Số đo:**

| Hạng mục | Số đo |
|---|---|
| Số hàng bảng **trước** lọc | **4** |
| Số hàng bảng **sau** lọc | **0** |
| Lệnh máy chủ phát ra bởi CHÍNH cú bấm | `GET /api/v1/ho-so-phap-ly-dns?doanhNghiepId=1a715c55-…&**keyword=zzqqxx-khongtontai**&pageSize=100` |
| Kiểu lệnh | **XHR** (không phải `fetch`) — bộ đếm bọc **cả hai** nên vẫn bắt được |
| HTTP | **200** (không 4xx/5xx) |
| Tham số `keyword` gửi lên | **`zzqqxx-khongtontai`** — đúng nguyên chuỗi đã gõ, không bị cắt/nối |
| Thân phản hồi (nguyên văn) | `{"success":true,"data":[],"meta":{"page":1,"pageSize":100,"total":0,"totalPages":0}}` |
| `meta.total` máy chủ trả | **0** |
| `data[]` máy chủ trả | **rỗng** (độ dài 0) |
| Bảng ↔ phản hồi máy chủ | ✅ **trùng khít** — 0 dòng trên bảng = 0 bản ghi máy chủ trả |
| Lỗi bảng điều khiển phát sinh do case | **0** |

### 4.2 — Chuỗi chữ đọc được + so từng ký tự

Đọc bằng **`innerText`** (CẤM `textContent`), trên phần tử `.ant-empty-description` nằm trong
`tr.ant-table-placeholder` của vùng bảng.

| Hạng mục | Giá trị |
|---|---|
| **Chuỗi đọc được trên màn** | `Không tìm thấy hồ sơ pháp lý phù hợp` |
| **Chuỗi đặc tả `srs-fr-12-tv-chuyen-sau.md:701`** | `Không tìm thấy hồ sơ pháp lý phù hợp` |
| So sánh `===` (nguyên trạng, không chuẩn hoá) | **`true`** |
| **SỐ KÝ TỰ LỆCH** | **0** |
| Độ dài (điểm mã) — thực tế / đặc tả | **36 / 36** |
| So sau chuẩn hoá `NFC` | **`true`**, **0 ký tự lệch** ⇒ loại luôn khả năng lệch cách tổ hợp dấu tiếng Việt (NFC ↔ NFD) |
| Dãy điểm mã hai bên | **giống hệt từng phần tử**: `75,104,244,110,103,32,116,236,109,32,116,104,7845,121,32,104,7891,32,115,417,32,112,104,225,112,32,108,253,32,112,104,249,32,104,7907,112` |
| Khoảng trắng thừa đầu/cuối | **không có** |
| Khoảng trắng kép giữa chuỗi | **không có** |

⇒ **Khớp NGUYÊN VĂN TỪNG KÝ TỰ**, chứng minh bằng dãy điểm mã chứ không bằng mắt.

### 4.3 — Phân biệt TRẠNG THÁI CUỐI với khung trung gian (bẫy đã lộ ở `_11`)

Ở `_11`, khung *"Không tìm thấy…"* chỉ **chớp ~53 ms** rồi bị các hàng dữ liệu thay chỗ ⇒ là **khung vẽ trung gian**,
không phải trạng thái cuối. Lượt này bắt buộc phải phân biệt.

| Phép kiểm | Kết quả |
|---|---|
| `MutationObserver` cài **TRƯỚC** khi bấm, đọc `innerText`, **KHÔNG dedupe** | ghi nhận **đúng 1** nút được thêm: `TR.ant-table-placeholder` — nội dung `Không tìm thấy hồ sơ pháp lý phù hợp`, lúc `07:35:18.516Z` |
| Có nút nào thêm SAU đó thay chỗ nó không? | **Không** — không có lượt vẽ hàng dữ liệu nào tiếp theo (khác hẳn `_11`, nơi hàng dữ liệu hiện sau 53 ms) |
| Đọc lại **+4 giây** sau cú bấm | 0 hàng · câu vẫn còn |
| Đọc lại **+7 giây** sau cú bấm | 0 hàng · câu vẫn còn · `offsetParent !== null` ⇒ **đang hiển thị thật**, không phải node ẩn |
| Đọc lại **+~80 giây** (lúc đo vân tay cuối case) | 0 hàng · câu vẫn còn |
| Ảnh chụp màn (sau khi bảng đã ổn định) | thấy rõ câu trong vùng bảng rỗng |

⇒ Câu báo là **TRẠNG THÁI CUỐI ỔN ĐỊNH**, **không** phải khung chớp. Bẫy `_11` **không** tái diễn ở nhánh rỗng.

### 4.4 — Kênh hiển thị (ghi nhận, KHÔNG dùng để chấm)

| Hạng mục | Quan sát |
|---|---|
| Câu hiện ở đâu | **Dòng chữ trong vùng bảng rỗng** — `tr.ant-table-placeholder` → `.ant-empty` → `.ant-empty-description`, kèm hình minh họa trạng thái rỗng |
| Có thông báo nổi (toast/notification/alert) không | **Không** — dò `.ant-message-notice-wrapper`, `.ant-message-notice`, `.ant-notification-notice`, `[role="alert"]` → **0 phần tử** |
| Mã `INF-HSPL-01` có hiện trên giao diện không | **Không** |

⇒ Cả hai điểm này **nguồn chuẩn §6 xếp đúng vào nhóm "KHÔNG được chấm Fail vì…"**: `:701` chỉ quy định **nội dung
phản hồi + mức INFO**, **không** quy định kênh hiển thị; mã lỗi là định danh nội bộ của đặc tả, không phải chuỗi
bắt buộc hiển thị. **Ghi nhận, không chấm lỗi.**

### 4.5 — Tổng hợp lệnh máy chủ của case

| # | Điều kiện lọc | Tham số gửi lên | HTTP | `meta.total` | Số hàng bảng | Khớp? |
|---|---|---|---|---|---|---|
| 0 | *(không lọc — nền so sánh)* | `doanhNghiepId` | 200 | **4** | **4** | ✅ |
| 1 | từ khóa không khớp gì | `doanhNghiepId` + **`keyword=zzqqxx-khongtontai`** | 200 | **0** | **0** | ✅ |

Dãy **4 → 0**. **0 lệnh 4xx/5xx** trong cả case.

---

## 5. Artifact quyết định verdict

Ở `F9-uatdoitac-QLHSPLDN-2026-08-07/image/`. Mỗi ảnh **đã được mở ra đọc bằng mắt**, không kết luận bằng script.

| Ảnh | Thấy gì trong ảnh |
|---|---|
| `12-A-baseline-DN-XX-0005-4hang-o-tukhoa-trong.png` | **Nền so sánh.** Tiêu đề `Chi tiết DN #DN-XX-0005`, thẻ *Hồ sơ pháp lý* đang mở. Ô từ khóa **trống** (chỉ còn chữ gợi ý xám *"Tìm theo mã hoặc tên hồ sơ"*), hai ô chọn *Loại hồ sơ* / *Trạng thái* xám mờ chưa chọn. Bảng đếm được **4 hàng** (`HSPL-20260804-0001`, `HSPL-20260803-0002`, `HSPL-20260803-0001`, `HSPL-20260731-0002`), có ô phân trang số **1**. |
| `12-B-tukhoa-rac-0hang-cau-Khong-tim-thay-ho-so-phap-ly-phu-hop.png` | **Ảnh quyết định.** Ô từ khóa hiện đúng chuỗi **`zzqqxx-khongtontai`** kèm nút xoá ⊗ (không bị nối chuỗi); hai ô chọn **vẫn chưa chọn** ⇒ chỉ có một điều kiện lọc duy nhất là từ khóa. Hàng tiêu đề bảng vẫn còn, **thân bảng không còn hàng dữ liệu nào**, ở giữa là hình minh họa trạng thái rỗng và **dòng chữ `Không tìm thấy hồ sơ pháp lý phù hợp`** đọc rõ bằng mắt. Ô phân trang đã biến mất. Badge góc phải vẫn là `Cán bộ NV Trung ương` · `BTP · TW`. |

---

## 6. Verdict

# 📌 **Pass** — HIỆN TẠI ĐẠT

**Bám luật Flow 03 §Chốt (bảng Verdict logic), dòng "Pass":**

1. **Mọi vế đều `MATCH` và đều đạt.** Ba vế con nguồn chuẩn §2 — **C2a** chạy được thao tác tìm · **C2b** hiện đúng
   câu báo khi không ra kết quả · **C2c** đúng thẻ đang tranh chấp — đều đo được và đều đạt. Không vế nào FAIL.
   Triệu chứng đối tác báo (*"Không có trường thông tin tìm kiếm trên màn hình"*) **không tái hiện**.
2. **Đủ 5 điều kiện PASS của nguồn chuẩn §6:** ① nền so sánh **4 ≥ 1 dòng** · ② sau khi tìm bảng còn **0 dòng** ·
   ③ câu trên màn khớp **0 ký tự lệch** đọc bằng `innerText` · ④ phản hồi máy chủ `data[]` rỗng, `meta.total = 0`,
   `keyword` gửi lên đúng nguyên chuỗi đã gõ · ⑤ vân tay bản dựng **đầu = cuối**.
3. **Biến thể bắt buộc đã chạy đủ 1/1.** Nguồn chuẩn §3 chốt đúng **một** biến thể — nhánh rỗng do từ khóa, đúng
   phạm vi Bước 4 của phiếu. Không tự nâng thành nhiều biến thể (Flow 03 §Khi chưa có FAIL).
4. **Có đối chứng độc lập cho quan sát quyết định.** Đọc **phản hồi máy chủ của chính lệnh tìm đó**
   (`total = 0`, `data[]` rỗng, `keyword` khớp) rồi đối chiếu với bảng đang hiển thị — đúng phương pháp Flow 03
   §Chạy.3 ("hiển thị → đối chiếu dữ liệu nguồn"). **Không** bấm lại cùng nút làm đối chứng.
5. **Không Pass bằng quan sát tĩnh.** Không dừng ở "màn trông có vẻ trống": đã **gõ từ khóa thật, bấm nút thật**,
   bảng **đổi thật 4 → 0**, mở phản hồi máy chủ đối chiếu, và **chụp ảnh rồi mở ảnh đọc bằng mắt**.
6. **Đã loại được hai ca giả mạo mà chuẩn chấm đòi loại.** (a) *"FE tự ẩn dòng nhưng máy chủ vẫn trả dữ liệu"* —
   loại vì máy chủ trả **đúng `total = 0`**, không phải >0. (b) *"FE hiện câu rỗng cứng bất kể máy chủ trả gì"* —
   loại vì cùng màn/cùng nút, khi từ khóa khác (`202608`, đo ở `_11`) và khi không lọc, hệ thống trả **3** và **4**
   hàng dữ liệu chứ không hiện câu này ⇒ câu báo bám theo dữ liệu máy chủ, không phải chuỗi cứng.
7. **Đã loại bẫy khung chớp của `_11`.** Câu báo tồn tại ổn định ở **+4 s / +7 s / +~80 s** sau cú bấm, có
   `offsetParent !== null`, và bộ quan sát **không** ghi nhận lượt vẽ nào thay chỗ nó ⇒ đây là **trạng thái cuối**,
   không phải khung trung gian.
8. **Câu chữ khớp tuyệt đối, chứng minh bằng điểm mã.** `0` ký tự lệch cả ở dạng nguyên trạng lẫn sau chuẩn hoá
   `NFC`, 36/36 điểm mã giống hệt ⇒ không phải "đại ý giống".

**Giới hạn hiệu lực (bắt buộc ghi):** Pass này **chỉ có hiệu lực trên env `https://htpldn-uat.ospgroup.vn`**, bản
dựng `assets/index-D4NhKEjr.js` · `last-modified Fri, 07 Aug 2026 04:17:55 GMT`, đo lúc **14:33 → 14:36 giờ VN
07/08/2026**, vai trò **`CB_NV_TW`**, trên **`DN-XX-0005`** (chính DN trong bằng chứng của đối tác).

**Không viết "fix đã có tác dụng":** phiên này không có bằng chứng trạng thái trước fix trên chính env/bản dựng này
⇒ chỉ kết luận **hiện trạng ĐẠT so với SRS + expected gốc**, dùng chữ *HIỆN TẠI ĐẠT*.

**Ghi ô Drive theo mapping §7 brief:** `Trạng thái dev fix` = **`UAT done`**.
*(Chưa ghi — dừng chờ điều phối theo yêu cầu prompt.)*

---

## 7. Bug mới / candidate

**Không có bug mới, không có candidate.**

Phép đo quyết định phát sinh **1 lệnh `GET` nghiệp vụ**, HTTP **200**, **0 thông báo lỗi**, **0 lỗi bảng điều khiển**
mới. **Không dùng tới lượt xác nhận bổ sung nào** (hạn mức 1 phép/case vẫn còn nguyên).

### Ghi nhận KHÔNG thành candidate

- **Câu báo hiện dưới dạng dòng chữ trong vùng bảng rỗng, không phải thông báo nổi.** Nguồn chuẩn §6 xếp đúng mục
  này vào nhóm *"KHÔNG được chấm Fail vì…"* — `:701` chỉ quy định nội dung phản hồi + mức INFO, không quy định kênh.
  Ghi nhận cho dev biết, **không** chấm lỗi, **không** đẩy BA.
- **Không thấy mã `INF-HSPL-01` trên giao diện.** Cũng thuộc nhóm "KHÔNG được chấm Fail vì…" của nguồn chuẩn §6 —
  mã là định danh nội bộ của đặc tả.
- **Kèm câu đúng còn có hình minh họa trạng thái rỗng.** Nguồn chuẩn §6 cho phép tường minh.
- **Cảnh báo bảng điều khiển `Route path "/ticket=*" …`** (mức `warn`, của thư viện định tuyến). **Không** phải do
  case này sinh ra — có sẵn từ lúc khung ứng dụng khởi động, không do cú bấm [Tìm kiếm], không có biểu hiện nào
  trên màn/phản hồi đang đo, không chạm vế C2. Ghi nhận để khỏi bỏ sót, **không** mở candidate (không thuộc
  "sai lệch trong chính màn/phản hồi đang quan sát" của luật §8 brief).
- **Bảng có 10 cột, phải cuộn ngang mới thấy hết ở khổ 1440px.** Nguồn chuẩn §6 chốt rõ mục này thuộc phạm vi ghi
  nhận của **`QLHSPLDN_14`**, không liên quan C2.

---

## 8. Phần chưa đo được

| Phần | Lý do | Có ảnh hưởng verdict? |
|---|---|---|
| Nhánh rỗng do **bộ lọc** (chọn *Loại hồ sơ* / *Trạng thái* ra 0 kết quả) thay vì do từ khóa | Nguồn chuẩn §3 khoá **đúng 1 biến thể bắt buộc**: *"nhánh rỗng do từ khóa (đúng phạm vi Bước 4 của phiếu)"*. Chạy thêm nhánh lọc là **vượt phạm vi đã khóa** + Flow 03 cấm tự nâng số biến thể | **Không** — biến thể bắt buộc đủ 1/1 |
| Nhánh rỗng khi **kết hợp** từ khóa + bộ lọc | Như trên — ngoài phạm vi khóa. Logic VÀ đã được `QLHSPLDN_11` đo riêng và đạt | **Không** |
| Khoảng ngày không hợp lệ (`tu_ngay > den_ngay`, `ERR-HSPL-06` `:701` dòng E6) | Thuộc **`QLHSPLDN_13`** (dòng 295), case khác | **Không** |
| Nội dung tệp *Xuất Excel* khi kết quả rỗng | Thuộc **`QLHSPLDN_14`** (dòng 296), case khác. Case này **không bấm** nút đó | **Không** |
| Hành vi của vai trò khác (NHT, vai trò Doanh nghiệp ở `SCR-V.III-04`) | Ngoài vế — case chỉ đo đúng vai trò `CB_NV_TW` của đối tác. `srs-fr-07:514` còn cấm vai trò khác vào màn đó | **Không** |
| Câu báo khi DN **vốn không có hồ sơ nào** (rỗng do chưa có dữ liệu) | Nguồn chuẩn §5 chỉ rõ đo kiểu đó là **yếu** vì không phân biệt được với rỗng do lọc; đã tránh bằng cách chạy trên DN có 4 hồ sơ | **Không** |

---

## 9. Tự kiểm trước khi chốt (cổng Flow 03)

| # | Câu hỏi | Trả lời |
|---|---|---|
| 1 | Chuẩn chấm có bám đúng SRS hiện tại + expected gốc? | Có — dùng nguyên bảng vế/điều kiện đã khoá ở `chuan/QLHSPLDN_12.md`. Agent ĐO đã **tự mở lại** `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-12-tv-chuyen-sau.md` đọc dòng **701** trong chính lượt này, xác nhận E7 · `INF-HSPL-01` · câu *"Không tìm thấy hồ sơ pháp lý phù hợp"* · mức `INFO` — không bê số dòng từ báo cáo cũ |
| 2 | Có đo đúng phần còn lỗi, hay chạy lại phần đã đạt / kiểm chức năng kế bên? | Đo đúng vế C2 (nhánh **không** có kết quả). Không lặp lại vế C1 của `_11` (nhánh **có** kết quả) ngoài phần tối thiểu làm nền so sánh |
| 3 | Reopen đã có FAIL hợp lệ chưa? | **Không có FAIL nào** ⇒ luật dừng sớm không kích hoạt; phải chạy hết mọi điều kiện PASS — đã chạy hết 5/5 |
| 4 | Pass đã phủ hết vế/biến thể nguồn chuẩn yêu cầu? | Có — **1/1** biến thể bắt buộc (nguồn chuẩn §3 chỉ khóa một), đủ 5 điều kiện PASS, có đối chứng máy chủ |
| 5 | Artifact có chứa quan sát quyết định và đã mở đọc lại? | Có — 2 ảnh (nền so sánh · trạng thái rỗng có câu báo), **từng ảnh đã mở ra đọc bằng mắt**, mô tả ở §5 |
| 6 | Người ngoài phiên đo có phân biệt được phần đạt / cần BA / chưa đo? | Có — §4 số đo, §6 verdict, §7 không có bug mới, §8 phần chưa đo, tách bạch |

---

## 10. Bàn giao trạng thái trình duyệt

- Trình duyệt + phiên `cbnv_tw` **giữ sống** (`GET /api/v1/auth/me` → 200 lúc cuối case). **0 lượt đăng nhập** đã tiêu.
- Tab đang ở `https://htpldn-uat.ospgroup.vn/doanh-nghiep/1a715c55-…?tab=ho-so-pl`, đã bấm **[Xóa bộ lọc]** trả về
  nền sạch — **4 hàng**, ô từ khóa trống ⇒ case sau khỏi dính bộ lọc tồn dư (đúng vấn đề case này gặp lúc mở màn).
- Trong tab còn `window.__QA12` — bộ đếm request bọc **cả `fetch` lẫn `XMLHttpRequest`**, **trong suốt** (chỉ ghi
  lại, không đổi request/response). Mảng đã dọn rỗng. Case sau dùng lại được, hoặc tải lại trang để gỡ.
