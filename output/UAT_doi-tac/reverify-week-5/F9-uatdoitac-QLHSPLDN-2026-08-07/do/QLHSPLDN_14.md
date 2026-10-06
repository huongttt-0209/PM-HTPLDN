# GIAI ĐOẠN B — số đo thô · `QLHSPLDN_14` (tab `bug`, dòng 296 — "Xuất Excel thành công")

```
Lô:            F9 — tái xác nhận trên env NGHIỆM THU của đối tác (case CUỐI lô)
Flow:          flows/03-reverify-sau-dev-fix.md — NHÁNH 2 "Tái xác nhận trên môi trường khác"
Nguồn chuẩn:   chuan/QLHSPLDN_14.md (Giai đoạn A đã khoá) — làm đúng theo, không tự thêm/bớt vế
Env đo:        https://htpldn-uat.ospgroup.vn  (env nghiệm thu của đối tác)
Người đo:      agent ĐO · 2026-08-07 · phiên 15:19 → 15:25 giờ VN
```

> 🔴 **KẾT QUẢ NGẮN GỌN: phép đo bắt buộc KHÔNG chạy được.** Ngay đầu case phát hiện **máy chủ đã deploy bản
> dựng MỚI lúc 15:15 VN** (giữa case `_13` và case này). Tải lại trang để lên đúng bản dựng hiện hành thì
> bản dựng mới **chặn toàn bộ màn bằng một hộp thoại bắt buộc nhập số CCCD, không có đường bỏ qua** ⇒ **không
> bấm được nút [Xuất Excel] bằng UI thật** ⇒ **không xuất được tệp** ⇒ **không mở được nội dung tệp**.
> Verdict `QLHSPLDN_14` = **Chưa chốt**. Cổng chặn CCCD là **bug mới, trái SRS** — chi tiết §7.

---

## 1. Vân tay bản dựng — ĐẦU và CUỐI case

| Hạng mục | ĐẦU case — **15:19:57 VN 07/08** | CUỐI case — **15:24:44 VN 07/08** |
|---|---|---|
| Bó mã JS **máy chủ đang phát** (`GET /`) | **`assets/index-Bd1akG3f.js`** | **`assets/index-Bd1akG3f.js`** |
| Bó mã JS **tab đang chạy** (`script[src]`) | ⚠️ **`assets/index-D4NhKEjr.js`** (bó **CŨ**, tab mở từ case trước) → sau khi tải lại: `assets/index-Bd1akG3f.js` | **`assets/index-Bd1akG3f.js`** |
| Bó mã CSS | `assets/index-DVlgOkLg.css` | `assets/index-DVlgOkLg.css` |
| `GET /` `last-modified` | **`Fri, 07 Aug 2026 08:15:32 GMT`** (= **15:15:32 VN**) | `Fri, 07 Aug 2026 08:15:32 GMT` |
| `GET /` `etag` | **`W/"6a759424-428"`** | `W/"6a759424-428"` |
| Máy chủ web | `nginx` | `nginx` |
| Chuỗi chân sidebar | `HTPLDN · V1.0.10` | `HTPLDN · V1.0.10` |

### 1.1 🔴 Có deploy chen giữa lô — bắt buộc khai

| Mốc | Bó mã | `last-modified` | `etag` |
|---|---|---|---|
| 5 case trước lô (`_06` `_07` `_11` `_12` `_13`), đo **14:14 → 15:00 VN** | `assets/index-D4NhKEjr.js` | `Fri, 07 Aug 2026 04:17:55 GMT` (= 11:17 VN) | `W/"6a755c73-428"` |
| **Case này**, đo **15:19 → 15:25 VN** | **`assets/index-Bd1akG3f.js`** | **`Fri, 07 Aug 2026 08:15:32 GMT`** (= **15:15:32 VN**) | **`W/"6a759424-428"`** |

- Case `_13` kết thúc **14:59:55 VN**; bản dựng mới lên **15:15:32 VN** ⇒ **deploy rơi vào khoảng 15:00–15:15 VN**,
  tức **SAU KHI cả 5 case trước đã đo xong**. Không có quan sát nào của 5 case đó nằm vắt qua mốc deploy
  ⇒ **số đo của 5 case trước vẫn nhất quán nội bộ, không phải đo lại vì lý do vắt mốc.**
- ⚠️ Nhưng **hiệu lực của chúng chỉ gắn với bản dựng `index-D4NhKEjr.js`, mà bản dựng đó KHÔNG còn được deploy**.
  Đây là dữ kiện điều phối cần biết trước khi ghi Drive cho cả lô.
- ⚠️ **Chuỗi sidebar `V1.0.10` KHÔNG đổi** dù bó mã đổi hẳn — đúng cảnh báo ở brief §2 ("`V1.0.x` không phải
  định danh bản dựng"). Định danh thật vẫn là bó mã + `last-modified`.
- ✅ Hai đầu case này **trùng khít nhau** (`Bd1akG3f` · `08:15:32 GMT` · `W/"6a759424-428"`) ⇒ **không có deploy
  thứ hai chen vào trong lúc đo case này**.
- ✅ **Đã loại trừ bẫy "tab mở lâu vẫn chạy mã cũ"** — và lần này bẫy đó **đã thực sự bung**: tab đang chạy bó cũ
  trong khi máy chủ phát bó mới. **Đã tải lại trang** (`reload`, `ignoreCache`) để tab nạp đúng bó mã hiện hành,
  xác nhận lại bằng `document.querySelectorAll('script[src]')`.

---

## 2. Tài khoản thực dùng + xác nhận vai trò

| Hạng mục | Giá trị |
|---|---|
| Tài khoản | **`cbnv_tw`** (đúng tài khoản chỉ định, **không** phải fallback) |
| Cách vào phiên | **Dùng lại phiên đang sống** của các case trước — kiểm `GET /api/v1/auth/me` → **200** ở **cả đầu và cuối** case. Phiên **sống sót qua 2 lần tải lại trang**, không bị đá về `/login` |
| Số lượt đăng nhập phát sinh | **0** — không chạm giới hạn 5 lượt/60s |
| `hoTen` | `Cán bộ NV Trung ương` |
| `vaiTro` | `["CB_NV_TW"]` |
| `capDonVi` | `TW` |
| `donViId` | `00000000-0000-4000-8000-000000000001` (= *Cục Bổ trợ tư pháp - Bộ Tư pháp*) |
| `authMethod` | **`LOCAL`** (= Tier 1 nội bộ) |
| `cccd` | **`null`** |
| Badge trên màn | `Cán bộ NV Trung ương · Cán bộ Nghiệp vụ Trung ương` · phạm vi `BTP · TW` |

⇒ Đúng tác nhân `srs-fr-12:565`. **Không dùng `admin` ở bất kỳ bước nào.**

---

## 3. Bản ghi đã đọc / đã tạo / đã đổi

| Hạng mục | Số lượng |
|---|---|
| Bản ghi **TẠO MỚI** | **0** |
| Bản ghi **SỬA / XOÁ** | **0** |
| Bản ghi chỉ **ĐỌC** | 1 DN + 4 hồ sơ pháp lý |
| Tệp Excel đã sinh ra | **0** |

🔴 **KHÔNG nhập số CCCD vào hộp thoại chặn.** Đó là ghi dữ liệu định danh cá nhân vào **bản ghi tài khoản mà QA
không tự tạo**, trên **env nghiệm thu của đối tác** — vi phạm kỷ luật dữ liệu brief §4.1, và số CCCD còn có thể
vướng ràng buộc duy nhất/đối chiếu VNeID. **Quyết định này để điều phối chốt, agent ĐO không tự ý ghi.**

**Doanh nghiệp đo:** `DN-XX-0005` — *Công ty TNHH Mẫu Test* (`1a715c55-bc31-46de-ae07-56dd4f403ce5`),
URL `/doanh-nghiep/1a715c55-…?tab=ho-so-pl` — đúng DN trong bằng chứng đối tác, giữ nguyên màn case `_11`/`_13`
để lại. **Không sửa, không xoá, không thêm gì.**

---

## 4. Số đo thô

### 4.0 — Nền so sánh đọc được trên bản dựng MỚI · 15:20:36 VN

| Nguồn | Số hàng | Danh sách mã |
|---|---|---|
| Bảng trên màn (`tr.ant-table-row`) | **4** | `HSPL-20260804-0001` · `HSPL-20260803-0002` · `HSPL-20260803-0001` · `HSPL-20260731-0002` |

Trùng khít nền 4 hàng mà case `_11` / `_12` / `_13` đã đo trên bản dựng cũ ⇒ **dữ liệu không đổi**, bộ lọc vẫn ở
nền sạch (ô từ khóa trống, 2 ô chọn chưa chọn). Đủ điều kiện tối thiểu của nguồn chuẩn §5 (≥2 bản ghi + tồn tại
bộ lọc cắt được tập con: `202608` → 3 hàng, `202608` + *Hiệu lực* → 2 hàng, theo số đo `_11`).

Thẻ hiển thị **10 cột** (`Mã hồ sơ` · `Tên hồ sơ` · `Loại` · `Lĩnh vực pháp lý` · `Nguồn` · `Ngày cấp` ·
`Ngày hết hạn` · `Trạng thái` · `Có tệp đính kèm` · `Hành động`) — đúng như nguồn chuẩn §2.2 đã cảnh báo.
**Không chấm gì theo bảng này** vì vế C4 chấm **tệp xuất**.

### 4.1 — Nút [Xuất Excel] · quan sát TĨNH (KHÔNG đủ để Pass)

| Hạng mục | Số đo |
|---|---|
| Nút *Xuất Excel* có mặt trong đúng vùng thẻ *Hồ sơ pháp lý DN*? | ✅ **có** — 1 nút, cùng hàng với *Tìm kiếm* / *Xóa bộ lọc*, **bên trong `<form>` bộ lọc của thẻ** |
| Vị trí | `{x:579, y:310, w:127, h:32}` |
| Có nhầm nút của màn danh sách DN (`srs-fr-07:425`) không? | ❌ **không** — đang ở `/doanh-nghiep/{id}?tab=ho-so-pl`, tiêu đề `Chi tiết DN #DN-XX-0005`, tab *Hồ sơ pháp lý* đang chọn |

🔴 **Đây là quan sát tĩnh. Nguồn chuẩn §6 ghi rõ: "Chỉ nhìn thấy nút *Xuất Excel* hiện trên thẻ ⇒ CẤM chấm Pass."**
Vì vậy dữ kiện này **KHÔNG** được dùng làm căn cứ verdict, chỉ ghi nhận. Triệu chứng đối tác báo
(*"Màn hình không có nút chức năng"*) **không tái hiện về mặt hiển thị** — nhưng **không đủ để kết luận case**.

### 4.2 — 🚫 Phép đo bắt buộc BỊ CHẶN · 15:20:40 VN

**Ngay khi trang nạp xong trên bản dựng mới, một hộp thoại phủ toàn màn bật lên và không tắt được.**

| Hạng mục | Số đo |
|---|---|
| Tiêu đề hộp thoại | **`Cập nhật thông tin bắt buộc`** |
| Nội dung nguyên văn | *"Theo quy định mới, bạn cần cung cấp số Căn cước công dân (CCCD) để tiếp tục sử dụng hệ thống. Thông tin này chỉ được yêu cầu một lần."* |
| Ô nhập | `Số CCCD` — **bắt buộc** (`required`), placeholder *"Nhập 12 chữ số CCCD"* |
| Nút trong hộp thoại | **đúng 1 nút: `Xác nhận`** |
| Có nút đóng (×)? | ❌ **không** (`.ant-modal-close` không tồn tại) |
| Bấm phím `Escape` | ❌ **không tắt** — hộp thoại còn nguyên |
| Bấm ra ngoài (mask `.ant-modal-wrap`) | ❌ **không tắt** — hộp thoại còn nguyên |
| Nút [Xuất Excel] có bấm được không? | ❌ **KHÔNG.** `document.elementFromPoint()` tại **tâm nút** trả về `DIV.ant-form-item-control-input-content` **của hộp thoại**, không phải nút ⇒ nút bị lớp phủ che, cú bấm rơi vào hộp thoại |
| Tái hiện | ✅ **tái hiện xác định** — tải lại trang lần 2 (15:24:44 VN): hộp thoại **bật lại y hệt**, vẫn không nút đóng, vẫn che nút [Xuất Excel] |

⇒ **Không thực hiện được lượt (a) "xuất khi không lọc" lẫn lượt (b) "xuất theo bộ lọc".**
⇒ **0 tệp `.xlsx` được sinh ra ⇒ không có gì để mở nội dung ra đọc.**
⇒ Toàn bộ điều kiện PASS ①②③④ của nguồn chuẩn §6 **không có số đo nào**.

### 4.3 — Vì sao KHÔNG lách bằng cách gọi thẳng đường API xuất tệp

Nguồn chuẩn §4 mục 2 + Flow 03 §Chạy.2 buộc **hành động đang tranh chấp phải chạy bằng UI thật**; API chỉ được
làm đối chứng. Vế C4 tranh chấp đúng chuyện *"bấm nút Xuất Excel trên thẻ"* ⇒ tự dựng lệnh gọi máy chủ để lấy
tệp là **thay thế thao tác UI**, không hợp lệ, và còn vi phạm brief §4.3 ("cấm đoán đường dẫn API"). Vì cú bấm
UI chưa từng chạy, cũng **không có** request nào trong `list_network_requests` để lấy đường tải tệp một cách
hợp lệ. **Không lách.**

---

## 5. Artifact quyết định

| Ảnh | Thấy gì trong ảnh |
|---|---|
| `image/14-A-ban-dung-moi-hopthoai-CCCD-chan-nut-XuatExcel.png` | Màn `Chi tiết DN #DN-XX-0005`, tab **Hồ sơ pháp lý** đang chọn, sidebar ghi `HTPLDN · V1.0.10`, badge `Cán bộ NV Trung ương` · `BTP · TW`. Toàn trang bị **phủ xám**; giữa màn là hộp thoại trắng **"Cập nhật thông tin bắt buộc"** với câu *"Theo quy định mới, bạn cần cung cấp số Căn cước công dân (CCCD) để tiếp tục sử dụng hệ thống…"*, ô đỏ dấu `*` **Số CCCD** (placeholder *"Nhập 12 chữ số CCCD"*) và **chỉ một nút `Xác nhận`** — **không có dấu × để đóng**. Hộp thoại **đè đúng lên chỗ hàng nút của thẻ**: chỉ còn thấy ló nút `Tìm kiếm` bên trái, còn `Xóa bộ lọc` và **`Xuất Excel` bị che hoàn toàn**. Bảng 4 hàng (`HSPL-20260804-0001`, `HSPL-20260803-0002`, `HSPL-20260803-0001`, `HSPL-20260731-0002`) vẫn hiện mờ phía dưới lớp phủ ⇒ dữ liệu có đủ, chỉ là **không thao tác được**. |

---

## 6. Verdict

# 📌 **Chưa chốt** — CHƯA THỂ KẾT LUẬN

**Bám luật Flow 03 §Chốt (bảng Verdict logic), dòng "Chưa chốt": *"Blocker khách quan … hoặc thiếu biến thể
quyết định để Pass"*.**

1. **Không đủ căn cứ Pass.** Nguồn chuẩn §3 khoá **2 biến thể bắt buộc** — (a) xuất khi không lọc, (b) xuất theo
   bộ lọc cắt tập con. **Chạy được 0/2.** Nguồn chuẩn §6 nói thẳng: *"Chỉ chạy lượt (a) ⇒ Chưa chốt"* — ở đây
   còn chưa chạy nổi lượt (a). Và điều kiện Pass cốt lõi là **mở nội dung tệp `.xlsx` đọc hàng tiêu đề + thân
   tệp**; **không có tệp nào** ⇒ không có gì để đọc.
2. **Không đủ căn cứ Reopen.** Luật dừng sớm đòi **cả bốn** điều kiện, trong đó có *"chạy đúng tiền đề và thao
   tác đã khoá"* và *"sai lệch không phải do env, tài khoản, dữ liệu test hoặc bản dựng"*. Thao tác đã khoá
   (bấm [Xuất Excel]) **chưa hề chạy được**, và vật cản nằm ở **lớp xác thực/hồ sơ tài khoản**, **không** thuộc
   hành vi xuất Excel. Chấm `Reopen` sẽ báo cho dev một điều sai sự thật — rằng *"Xuất Excel còn lỗi"* — trong
   khi **không có một số đo nào** về hành vi xuất Excel. **Không chấm Reopen.**
3. **Không phải Cần BA.** Cả 5 vế con của C4 đều đã được Giai đoạn A chốt `MATCH`; không có vế `DIFF/GAP` nào
   phát sinh trong lượt đo này. Vướng mắc là **chặn kỹ thuật**, không phải tranh chấp đặc tả.
4. **Tuyệt đối không Pass bằng quan sát tĩnh.** Nút *Xuất Excel* **có hiện** trên đúng thẻ (§4.1) — nhưng nguồn
   chuẩn §6 xếp đúng dữ kiện này vào ô *"CẤM chấm Pass vì"*. **Không dùng nó để chốt.**
5. **Không lấy kết quả env nội bộ ra đỡ.** Nguồn chuẩn §6: *"Lấy kết quả Pass ở env nội bộ làm căn cứ"* nằm
   trong nhóm cấm.

**Ghi ô Drive:** 🚫 **KHÔNG ghi ô nào** (đúng mapping brief §7 — `Chưa chốt` ⇒ không ghi, báo điều phối).
Ô `Trạng thái dev fix` của dòng 296 **giữ nguyên `Test done`**, ô `Kết quả verify` **giữ nguyên**.

**Giới hạn hiệu lực:** quan sát này gắn với env `https://htpldn-uat.ospgroup.vn`, bản dựng
`assets/index-Bd1akG3f.js` · `last-modified Fri, 07 Aug 2026 08:15:32 GMT`, đo **15:19 → 15:25 giờ VN
07/08/2026**, vai trò `CB_NV_TW`, trên `DN-XX-0005`.

---

## 7. Bug mới tự lộ

### 🔴 `BUG-MOI-01` (đề xuất mã sheet: `QLHSPLDN_QA01`) — Bản dựng mới bắt cán bộ nội bộ nhập CCCD mới cho dùng hệ thống, không có đường bỏ qua

**Đây là bug đã đủ căn cứ, KHÔNG phải candidate** — có SRS dẫn `file:dòng`, có artifact, có đối chứng độc lập.
Nó **tự lộ trong chính bước bắt buộc** của case (nạp màn để bấm [Xuất Excel]), **không** phải do đi dò tìm.

| Hạng mục | Nội dung |
|---|---|
| **Hiện tượng** | Sau khi tải lại trang trên bản dựng `index-Bd1akG3f.js`, hệ thống bật hộp thoại **"Cập nhật thông tin bắt buộc"** đòi **số CCCD** với câu *"để tiếp tục sử dụng hệ thống"*. Hộp thoại **không có nút đóng**, **không tắt bằng `Escape`**, **không tắt khi bấm ra ngoài**, và **che mất hàng nút của màn** ⇒ người dùng **không làm được gì** cho tới khi khai số CCCD. |
| **Xuất hiện tại** | Ngay khi nạp `/doanh-nghiep/{id}?tab=ho-so-pl` với tài khoản `cbnv_tw` (`CB_NV_TW`, cấp TW, `authMethod=LOCAL`, `cccd=null`). Tái hiện **2/2 lần** tải lại. |
| **SRS đòi ngược lại — 4 neo, đã mở file đọc đúng số dòng** | ① `srs-v3.5.md:5543` **BR-AUTH-13** — *"Cán bộ nội bộ (Quản trị Hệ thống, Cán bộ Nghiệp vụ, Cán bộ Phê duyệt) … SHALL chỉ dùng **Tier 1** … **Lý do: cán bộ nội bộ không có thông tin định danh cá nhân (CCCD/căn cước) liên kết với VNeID; cán bộ truy cập qua mạng kín chuyên dùng nội bộ nên không cần định danh công dân.**"*<br>② `srs-v3.5.md:5642` **BR-INTG-06** — *"Tier 1 (nội bộ qua mạng kín): username/password + TOTP 2FA — **không cần CCCD vì user là cán bộ nội bộ.**"*<br>③ `srs-fr-10-quan-tri.md:1734` — *"\| 24 \| form \| CCCD \| text-input \| **Không bắt buộc**, validate 12 chữ số \|"*<br>④ `srs-fr-10-quan-tri.md:2110` — *"\| cccd \| text \| **N** \| \| \| Số CCCD (**từ VNeID**) \|"* (nullable, nguồn dữ liệu là VNeID chứ không phải người dùng tự khai) |
| **Quan hệ** | **DIFF rõ ràng giữa sản phẩm và SRS** — SRS **nói tường minh** rằng cán bộ nội bộ Tier 1 **không cần** CCCD và trường CCCD **không bắt buộc**. Đây **không** phải "SRS im lặng" ⇒ **không cần BA chốt để gọi là sai.** |
| **Đối chứng độc lập** | `GET /api/v1/auth/me` → **200**, trả `vaiTro:["CB_NV_TW"]` · `capDonVi:"TW"` · `authMethod:"LOCAL"` · **`cccd:null`** ⇒ tài khoản bị chặn **đúng là** lớp "cán bộ nội bộ Tier 1" mà BR-AUTH-13 / BR-INTG-06 miễn CCCD. Kiểm chặn bằng phương pháp thứ hai: `document.elementFromPoint()` tại tâm nút [Xuất Excel] trả về phần tử **của hộp thoại** ⇒ chứng minh bị che thật, không phải cảm nhận qua ảnh. |
| **Tác động quan sát được** | Chặn **toàn bộ** thao tác trên màn đang mở ⇒ **chặn đứng phép đo bắt buộc của `QLHSPLDN_14`**. |
| **Bằng chứng** | `image/14-A-ban-dung-moi-hopthoai-CCCD-chan-nut-XuatExcel.png` |
| **Đã dùng bao nhiêu lượt xác nhận?** | **1/1** — đúng hạn mức brief §8: chỉ **tải lại trang** (thao tác đọc, **không** tạo/sửa bản ghi, **không** sinh đầu ra nghiệp vụ mới). Không mở chức năng khác, không bấm thử field/nút nào khác. |

**Giới hạn của quan sát (khai thẳng, không suy rộng):** chỉ quan sát trên **màn bắt buộc của case này**.
**Chưa** kiểm hộp thoại có bật trên mọi màn / mọi vai trò hay không — muốn kết luận phạm vi phải mở thêm màn,
mà việc đó là **exploratory**, brief §8 cấm. Câu chữ *"để tiếp tục sử dụng hệ thống"* gợi ý đây là cổng chặn
mức ứng dụng, nhưng **đó là suy đoán, không phải số đo**.

**Chưa ghi lên sheet.** Brief §7 buộc **báo điều phối trước khi thêm dòng bug mới** — đã dừng, chờ điều phối.

### Ghi nhận KHÔNG thành bug / không thành candidate

- **Bảng trên màn có 10 cột, thiếu *Doanh nghiệp* và *Cơ quan cấp*** — nguồn chuẩn §6 xếp vào nhóm
  *"KHÔNG được chấm Fail vì"*: vế C4 chấm **tệp xuất**, không chấm bảng. Ghi nhận, **không** log.
- **Nhãn nút thêm là "Thêm hồ sơ"** — đã có candidate ở `do/QLHSPLDN_06.md` §7. Theo Flow 03 §"Bug mới tự lộ"
  mục 2: **liên kết vào candidate đã có, không mở phiếu thứ hai.**

---

## 8. Phần chưa đo được

| Phần | Lý do | Ảnh hưởng verdict? |
|---|---|---|
| **Lượt (a) — xuất Excel khi KHÔNG lọc**, đọc hàng tiêu đề + số dòng + danh sách mã trong tệp | **Bị chặn** bởi hộp thoại CCCD (§4.2) — không bấm được nút bằng UI thật | 🔴 **CÓ** — đây là phép đo bắt buộc; thiếu ⇒ Chưa chốt |
| **Lượt (b) — xuất Excel THEO BỘ LỌC**, chứng minh `:662` | Như trên. Bộ lọc dự kiến đã sẵn sàng (`202608` → 3 hàng; + *Hiệu lực* → 2 hàng, theo số đo `_11`) nhưng **không bấm được nút xuất** | 🔴 **CÓ** — thiếu biến thể quyết định |
| **Hàng tiêu đề 8 cột đúng thứ tự `srs-fr-12:664`** (`mã hồ sơ` · `tên` · `DN` · `loại` · `ngày cấp` · `hết hạn` · `trạng thái` · `cơ quan cấp`) | Không có tệp để mở | 🔴 **CÓ** |
| **Ngưỡng "tối đa 10.000 dòng"** (`srs-fr-12:663`) | ⏸ **Không đo tới được trên env** — `DN-XX-0005` chỉ có **4** hồ sơ, thấp hơn ngưỡng rất nhiều; muốn kiểm phải dựng khối lượng dữ liệu lớn, **không làm trên env nghiệm thu của đối tác**. Khai theo đúng nguồn chuẩn §6.1 | ❌ **Không** — nguồn chuẩn §6.1 ghi rõ ngưỡng này **không chặn Pass**; nó **không** phải lý do Chưa chốt |
| Phạm vi hộp thoại CCCD trên các màn / vai trò khác | Mở thêm màn = exploratory, brief §8 cấm | ❌ Không |

---

## 9. Tự kiểm trước khi chốt (cổng Flow 03)

| # | Câu hỏi | Trả lời |
|---|---|---|
| 1 | Chuẩn chấm có bám đúng SRS hiện tại + expected gốc? | Có — dùng nguyên bảng vế đã khoá ở `chuan/QLHSPLDN_14.md` (C4 = `MATCH`, neo `srs-fr-12:657-665`). Không tự thêm/bớt điều kiện |
| 2 | Có đo đúng phần còn lỗi? | Đã tới đúng màn, đúng thẻ, đúng nút — nhưng **bị chặn trước khi bấm**. Không đi kiểm chức năng kế bên |
| 3 | Reopen đã có FAIL hợp lệ chưa? | **Chưa.** Thiếu 2/4 điều kiện: thao tác đã khoá chưa chạy được, và vật cản thuộc lớp tài khoản/bản dựng ⇒ **không** chấm Reopen |
| 4 | Pass đã phủ hết biến thể bắt buộc? | **Không — 0/2.** ⇒ Chưa chốt, đúng luật "thiếu biến thể quyết định" |
| 5 | Artifact có chứa quan sát quyết định và đã mở đọc lại? | Có — ảnh `14-A`, **đã mở ra đọc bằng mắt**, mô tả ở §5 |
| 6 | Người ngoài phiên đo có phân biệt được phần đạt / chưa đo / bug mới? | Có — §4 số đo, §6 verdict, §7 bug mới, §8 phần chưa đo, tách bạch |
| 7 | Có tự ý đổi dữ liệu env đối tác không? | **Không.** 0 tạo · 0 sửa · 0 xoá · 0 tệp sinh ra. **Không nhập CCCD** — để điều phối chốt |

---

## 10. Trạng thái bàn giao (case cuối lô)

| Hạng mục | Trạng thái |
|---|---|
| Trình duyệt MCP | **Còn mở**. Tab 1 `about:blank` (launcher), tab 2 = `/doanh-nghiep/1a715c55-…?tab=ho-so-pl` **đang bị hộp thoại CCCD chặn** |
| Phiên `cbnv_tw` | **Còn sống** — `GET /api/v1/auth/me` → **200** lúc 15:24:44 VN. **0 lượt đăng nhập** phát sinh trong case |
| Bản dựng đang chạy trong tab | `assets/index-Bd1akG3f.js` (**bản mới**, deploy 15:15:32 VN) |
| Dữ liệu env đối tác | **Nguyên vẹn** — 0 thay đổi |
| Drive | **Chưa ghi gì cho dòng 296** |

**Cần điều phối quyết:**
1. **Có cho phép nhập CCCD cho `cbnv_tw` không?** Không có quyết định này thì **không QA nào thao tác được**
   trên env đối tác bằng bản dựng hiện tại. (Agent ĐO **không** tự ý ghi — xem §3.)
2. **Thêm dòng bug mới `QLHSPLDN_QA01`** cho cổng chặn CCCD (brief §7 buộc xin phép trước khi thêm dòng).
3. **Lô F9 có cần đo lại 5 case đã Pass trên bản dựng mới không?** — 5 verdict đó gắn với bản dựng
   `index-D4NhKEjr.js`, **không còn được deploy** (§1.1).

---
---

# LƯỢT ĐO 2 — sau khi điều phối phê duyệt nhập CCCD · **verdict: Pass**

```
Người đo:      agent ĐO (lượt 2) · 2026-08-07 · phiên 15:34 → 15:37 giờ VN
Cơ sở tiến hành: chủ việc PHÊ DUYỆT 2 việc — (1) được nhập số CCCD kiểm thử vào `cbnv_tw`
                 để qua hộp thoại chặn và đo trọn case; (2) được thêm dòng bug mới `QLHSPLDN_QA01`
                 cho chính hộp thoại đó.
Phần §1–§10 phía trên GIỮ NGUYÊN làm dấu vết lượt tắc — không sửa một chữ.
```

## 11. 🔴 Mutation có chủ đích trên env đối tác — khai đầy đủ

| Hạng mục | Giá trị |
|---|---|
| **Hành động** | Nhập **số CCCD kiểm thử** vào hộp thoại *"Cập nhật thông tin bắt buộc"* rồi bấm **[Xác nhận]** |
| **Số đã nhập** | **`000000000001`** — 12 chữ số, chọn cố ý dạng **rõ ràng là dữ liệu thử** (11 số 0 + 1), không phải số CCCD thật của bất kỳ ai |
| **Tài khoản bị đổi** | **`cbnv_tw`** (*Cán bộ NV Trung ương*, `CB_NV_TW`, cấp `TW`, `authMethod=LOCAL`) |
| **Thời điểm** | **15:34:32 → 15:34:43 giờ VN 07/08/2026** (điền lúc 15:34:32, bấm Xác nhận ngay sau đó) |
| **Env** | **`https://htpldn-uat.ospgroup.vn`** — env **NGHIỆM THU của đối tác** |
| **Bản dựng lúc mutation** | `assets/index-Bd1akG3f.js` · `last-modified Fri, 07 Aug 2026 08:15:32 GMT` · `etag W/"6a759424-428"` |
| **Đường gọi máy chủ thực phát ra** | `PATCH /api/v1/auth/me/cccd` → **200** (đọc từ `list_network_requests`, reqid 1708 — **không đoán đường dẫn**) |
| **Thông báo hệ thống** | *"Cập nhật CCCD thành công"* (bắt bằng `MutationObserver` cài trước cú bấm, **không lọc trùng**: ghi 2 lượt thêm khung cho **cùng một** thông báo) |
| **Đối chứng độc lập sau mutation** | `GET /api/v1/auth/me` → **200**, `cccd` đổi từ **`null`** → **`"000000000001"`**; `vaiTro` / `capDonVi` / `authMethod` **không đổi** |
| **Trạng thái hộp thoại sau đó** | **Tự đóng**, `document.querySelectorAll('.ant-modal').length = 0`, **không bật lại** trong suốt phần còn lại của phiên |
| **Phạm vi ảnh hưởng** | **Chỉ trường `cccd` của chính tài khoản QA dùng để đo.** Không đụng tài khoản nào khác. **Không** đụng bản ghi nghiệp vụ nào |

> ⚠️ **Đây là thay đổi dữ liệu duy nhất trong cả case.** Cần hoàn nguyên (đưa `cccd` về `null`) thì phải làm ở
> tầng CSDL/QTHT — màn hình không cấp đường xoá. Ghi lại để đối tác/dev biết dấu vết này là của QA.

## 12. Vân tay bản dựng — ĐẦU và CUỐI lượt đo 2

| Hạng mục | ĐẦU — **15:34:09 VN** | CUỐI — **15:37:16 VN** |
|---|---|---|
| Bó mã JS đang chạy trong tab | `assets/index-Bd1akG3f.js` | `assets/index-Bd1akG3f.js` |
| `GET /` `last-modified` | `Fri, 07 Aug 2026 08:15:32 GMT` | `Fri, 07 Aug 2026 08:15:32 GMT` |
| `GET /` `etag` | `W/"6a759424-428"` | `W/"6a759424-428"` |
| Chuỗi chân sidebar | `HTPLDN · V1.0.10` | `HTPLDN · V1.0.10` |

✅ **Hai đầu trùng khít** ⇒ không có deploy chen vào giữa lượt đo. Vẫn là **bản dựng MỚI** (deploy 15:15:32 VN),
**mới hơn** bản `index-D4NhKEjr.js` mà 5 case `_06`/`_07`/`_11`/`_12`/`_13` đã đo.

## 13. Tài khoản + phạm vi dữ liệu

| Hạng mục | Giá trị |
|---|---|
| Tài khoản | **`cbnv_tw`** — `GET /api/v1/auth/me` → 200, `vaiTro:["CB_NV_TW"]`, `capDonVi:"TW"`, `authMethod:"LOCAL"` |
| Số lượt đăng nhập phát sinh | **0** — dùng lại phiên đang sống |
| Hồ sơ pháp lý **tạo / sửa / xoá** | **0 · 0 · 0** |
| Doanh nghiệp **tạo / sửa / xoá** | **0 · 0 · 0** |
| Bản ghi chỉ **đọc** | `DN-XX-0005` (`1a715c55-…3ce5`) + 4 hồ sơ pháp lý của DN đó |
| Tệp `.xlsx` sinh ra | **2** (đều là tệp tải về phía người dùng, **không** ghi gì vào hệ thống) |
| Đổi dữ liệu duy nhất | trường `cccd` của chính `cbnv_tw` — §11 |

## 14. Số đo — LƯỢT (a): xuất khi KHÔNG lọc

### 14.1 Nền trước khi bấm · 15:35:00 VN

Bộ lọc **sạch**: ô từ khóa trống, *Loại hồ sơ* chưa chọn, *Trạng thái* chưa chọn, *Từ ngày* / *Đến ngày* trống.

| Nguồn | Số hàng | Danh sách mã |
|---|---|---|
| Bảng trên màn (`tr.ant-table-row`) | **4** | `HSPL-20260804-0001` · `HSPL-20260803-0002` · `HSPL-20260803-0001` · `HSPL-20260731-0002` |

### 14.2 Cú bấm UI thật + tệp sinh ra

| Hạng mục | Số đo |
|---|---|
| Thao tác | Bấm **[Xuất Excel]** trong đúng vùng thẻ *Hồ sơ pháp lý DN* (cùng hàng *Tìm kiếm* / *Xóa bộ lọc*), tại `/doanh-nghiep/1a715c55-…?tab=ho-so-pl`, tab *Hồ sơ pháp lý* đang chọn |
| Có nhầm nút màn danh sách DN (`srs-fr-07:425`) không? | ❌ **không** |
| Đường gọi máy chủ **do chính UI phát ra** | `GET /api/v1/ho-so-phap-ly-dns/export?doanhNghiepId=1a715c55-bc31-46de-ae07-56dd4f403ce5` → **200** (reqid 1712) — **không** kèm tham số lọc nào, đúng với bộ lọc sạch |
| Kích thước tệp | **6 777 byte** |
| Kiểu MIME | `application/vnd.openxmlformats-officedocument.spreadsheetml.sheet` (= `.xlsx` thật) |
| Tên tệp tải về | `ho-so-phap-ly-dn-1786091713969.xlsx` |
| Thông báo | *"Xuất Excel thành công"* — 1 thông báo (bộ theo dõi ghi 2 lượt thêm khung cho **cùng một** thông báo, không phải nhân đôi) |
| Lệnh 4xx/5xx | **0** |

### 14.3 🔴 MỞ NỘI DUNG tệp ra đọc

Tệp được lấy từ **chính đối tượng nhị phân mà UI dựng ra** (hook `URL.createObjectURL`), parse **EOCD của zip +
`DecompressionStream('deflate-raw')`** ngay trong trang, đọc `xl/worksheets/sheet1.xml` + `xl/sharedStrings.xml`.
Chỉ trả về đúng thứ cần đo — **không** dump base64.

**Cấu trúc:** đúng **1 sheet** (`xl/worksheets/sheet1.xml`), **5 hàng** = 1 hàng tiêu đề + **4 hàng thân**.

**Hàng tiêu đề — đọc được 8 nhãn, theo thứ tự trái→phải:**

| # | Nhãn trong tệp | Trường ở `srs-fr-12:664` | Khớp |
|---|---|---|---|
| 1 | `Mã hồ sơ` | mã hồ sơ | ✅ |
| 2 | `Tên hồ sơ` | tên | ✅ |
| 3 | `Doanh nghiệp` | DN | ✅ |
| 4 | `Loại hồ sơ` | loại | ✅ |
| 5 | `Ngày cấp` | ngày cấp | ✅ |
| 6 | `Ngày hết hạn` | hết hạn | ✅ |
| 7 | `Trạng thái` | trạng thái | ✅ |
| 8 | `Cơ quan cấp` | cơ quan cấp | ✅ |

⇒ **đúng 8 trường, đúng thứ tự**, không thiếu, không thừa. Có đủ **`Doanh nghiệp`** và **`Cơ quan cấp`** — hai cột
`:664` đòi cho tệp nhưng **vắng** trên bảng 10 cột của màn. Chấm theo **8 trường + thứ tự**, **không** bắt khớp
từng ký tự nhãn (nguồn chuẩn §6 *"KHÔNG được chấm Fail vì"*).

**Thân tệp — 4 hàng, đối chiếu THEO TẬP MÃ với bảng:**

| # | Mã trong tệp | Có trên bảng? |
|---|---|---|
| 1 | `HSPL-20260804-0001` | ✅ |
| 2 | `HSPL-20260803-0002` | ✅ |
| 3 | `HSPL-20260803-0001` | ✅ |
| 4 | `HSPL-20260731-0002` | ✅ |

⇒ **4 = 4**, tập mã **trùng khít**, không lẫn mã lạ, không thiếu mã nào, **cùng thứ tự**.

**Đối chiếu GIÁ TRỊ từng bản ghi (tệp ↔ bảng):**

| Mã | Tên hồ sơ | Doanh nghiệp | Loại | Ngày cấp | Ngày hết hạn | Trạng thái | Cơ quan cấp |
|---|---|---|---|---|---|---|---|
| `HSPL-20260804-0001` | QA-HSPL-V2-0408-742199 DA SUA vong 2 ✅ | Công ty TNHH Mẫu Test | Quyết định ✅ | 05/08/2026 ✅ | 30/11/2026 ✅ | Hết hạn ✅ | Co quan cap DA SUA v2 |
| `HSPL-20260803-0002` | Hồ sơ pháp lý doanh nghiệp XXX ✅ | Công ty TNHH Mẫu Test | Hợp đồng ✅ | 12/08/2026 ✅ | 21/08/2026 ✅ | Hiệu lực ✅ | Bộ tư pháp và Cục phổ biến |
| `HSPL-20260803-0001` | TKM hồ sơ pháp lý số 1 ✅ | Công ty TNHH Mẫu Test | Khác ✅ | 03/08/2026 ✅ | 03/08/2026 ✅ | Hiệu lực ✅ | TKM |
| `HSPL-20260731-0002` | Ho so x - SUA CU v2 742199 ✅ | Công ty TNHH Mẫu Test | Giấy chứng nhận ✅ | 01/07/2026 ✅ | *(trống)* — bảng hiện `-` | Hiệu lực ✅ | *(trống)* |

Cột `Doanh nghiệp` = **`Công ty TNHH Mẫu Test`** ở cả 4 hàng — **đúng tên `DN-XX-0005`**, ⇒ tệp **không** lẫn hồ sơ
của DN khác (phạm vi `:661` đạt). Ô *Ngày hết hạn* trống ở hàng 4 khớp đúng dấu `-` trên bảng (bản ghi vốn không có
ngày hết hạn) — không phải mất dữ liệu.

## 15. Số đo — LƯỢT (b): xuất THEO BỘ LỌC (phép chứng minh `:662`)

### 15.1 Đặt bộ lọc cắt tập con · 15:36:40 VN

| Hạng mục | Số đo |
|---|---|
| Bộ lọc đặt | **Từ khóa = `202608`** *(gõ vào ô "Tìm theo mã hoặc tên hồ sơ")* **+ Trạng thái = `Hiệu lực`** *(chọn trong khung, đọc lại bằng `.ant-select-content` → hiện đúng `Hiệu lực`)* |
| Thao tác | Bấm nút **[Tìm kiếm]** thật bằng UI |
| Đường gọi máy chủ do UI phát ra | `GET /api/v1/ho-so-phap-ly-dns?doanhNghiepId=1a715c55-…&keyword=202608&trangThai=HIEU_LUC&pageSize=100` (reqid 1716) |
| Bảng sau lọc | **2 hàng** — `HSPL-20260803-0002` · `HSPL-20260803-0001` |
| Có thực sự cắt không? | ✅ **4 → 2**, tập con **thực sự nhỏ hơn** (`⊊`), khớp đúng số đo case `_11` (`202608` + *Hiệu lực* → 2 hàng) |

### 15.2 Cú bấm [Xuất Excel] lần 2 + tệp sinh ra

| Hạng mục | Số đo |
|---|---|
| Đường gọi máy chủ **do chính UI phát ra** | `GET /api/v1/ho-so-phap-ly-dns/export?doanhNghiepId=1a715c55-…&keyword=202608&trangThai=HIEU_LUC` → **200** (reqid 1717) |
| 🔴 **Ý nghĩa** | Lệnh xuất **mang theo đúng bộ lọc đang đặt trên màn** — lượt (a) **không** có tham số lọc, lượt (b) **có đủ cả hai**. Đây là bằng chứng ở **tầng máy chủ** cho `:662` |
| Kích thước tệp | **6 583 byte** (khác tệp (a) — không phải tệp cũ dùng lại) |
| Kiểu MIME | `application/vnd.openxmlformats-officedocument.spreadsheetml.sheet` |
| Tên tệp tải về | `ho-so-phap-ly-dn-1786091811215.xlsx` |
| Thông báo | *"Xuất Excel thành công"* |
| Lệnh 4xx/5xx | **0** |

### 15.3 🔴 MỞ NỘI DUNG tệp (b) ra đọc

**Hàng tiêu đề:** vẫn **đúng 8 nhãn, đúng thứ tự** — `Mã hồ sơ` · `Tên hồ sơ` · `Doanh nghiệp` · `Loại hồ sơ` ·
`Ngày cấp` · `Ngày hết hạn` · `Trạng thái` · `Cơ quan cấp`.

**Thân tệp: đúng 2 hàng.**

| # | Mã trong tệp (b) | Có trong tập đang hiển thị sau lọc? | Có trong tệp (a)? |
|---|---|---|---|
| 1 | `HSPL-20260803-0002` | ✅ | ✅ |
| 2 | `HSPL-20260803-0001` | ✅ | ✅ |

| Mã | Tên hồ sơ | Doanh nghiệp | Loại | Ngày cấp | Ngày hết hạn | Trạng thái | Cơ quan cấp |
|---|---|---|---|---|---|---|---|
| `HSPL-20260803-0002` | Hồ sơ pháp lý doanh nghiệp XXX | Công ty TNHH Mẫu Test | Hợp đồng | 12/08/2026 | 21/08/2026 | **Hiệu lực** | Bộ tư pháp và Cục phổ biến |
| `HSPL-20260803-0001` | TKM hồ sơ pháp lý số 1 | Công ty TNHH Mẫu Test | Khác | 03/08/2026 | 03/08/2026 | **Hiệu lực** | TKM |

**Kết luận vế `:662`:**
- Tập (b) = `{HSPL-20260803-0002, HSPL-20260803-0001}` **⊊** tập (a) = 4 mã ⇒ **thật sự là tập con**.
- Tập (b) **bằng đúng** tập 2 hàng đang hiển thị sau khi lọc ⇒ **không thừa, không thiếu**.
- **Không** lẫn `HSPL-20260804-0001` (từ khóa khớp `202608` nhưng trạng thái *Hết hạn*) ⇒ **cả hai chiều lọc đều
  được áp**, không phải chỉ áp từ khóa.
- **Không** lẫn `HSPL-20260731-0002` (*Hiệu lực* nhưng mã không chứa `202608`) ⇒ **từ khóa cũng được áp**.

⇒ Tệp **bám đúng bộ lọc hiện tại**, **không** phải "xuất tất cả rồi mặc kệ bộ lọc".

## 16. Đối chứng độc lập — đối chiếu bảng kiểm nguồn chuẩn §4

| # | Việc phải làm | Đã làm |
|---|---|---|
| 1 | Ghi baseline (số dòng + **danh sách mã**) trước mỗi lượt | ✅ (a) 4 mã · (b) 2 mã — §14.1, §15.1 |
| 2 | Bấm nút thật bằng UI, đúng vùng thẻ Hồ sơ pháp lý | ✅ 2 lượt, đúng màn `?tab=ho-so-pl`, không nhầm nút màn danh sách DN |
| 3 | 🔴 **Mở nội dung tệp `.xlsx`** (EOCD + `DecompressionStream`, chỉ trả thứ cần đo) | ✅ cả **2** tệp — §14.3, §15.3 |
| 4 | Đọc hàng tiêu đề, đếm cột, ghi nguyên văn nhãn theo thứ tự | ✅ 8/8 đúng thứ tự ở **cả 2** tệp |
| 5 | Đếm hàng thân + đọc cột mã toàn bộ thân, so **theo tập** | ✅ (a) 4/4 · (b) 2/2, trùng khít tập mã |
| 6 | Lượt (b) chứng minh "theo bộ lọc hiện tại": tập (b) ⊊ tập (a) **và** = tập đang hiển thị | ✅ §15.3 |
| 7 | Ghi đường gọi máy chủ sinh tệp + kích thước + kiểu MIME | ✅ reqid 1712 / 1717, 6 777 B / 6 583 B, MIME xlsx |
| 8 | Thông báo bắt bằng `MutationObserver` cài **trước** cú bấm, **không lọc trùng**, đọc `innerText` | ✅ *"Xuất Excel thành công"* cả 2 lượt |

**Đối chứng độc lập mạnh nhất (không phải bấm lại cùng nút):** hai tệp có **kích thước khác nhau**, **nội dung khác
nhau**, sinh từ **hai đường gọi máy chủ khác nhau về tham số lọc** — trong đó tham số lọc của lượt (b) đọc được ở
tầng mạng, **độc lập** với thứ mà giao diện hiển thị.

## 17. Verdict lượt đo 2

# 📌 **Pass** — ĐÃ HẾT LỖI

Đối chiếu **đủ 6 điều kiện PASS** của nguồn chuẩn §6:

| # | Điều kiện PASS | Kết quả |
|---|---|---|
| 1 | Từ chính thẻ Hồ sơ pháp lý xuất được tệp `.xlsx` (`:665`) | ✅ 2 tệp, MIME xlsx thật, mở đọc được |
| 2 | Lượt (a): tiêu đề 8 cột đúng thứ tự `:664`; thân đúng số dòng + đúng danh sách mã | ✅ 8/8 · 4 hàng · 4 mã trùng khít |
| 3 | Lượt (b): tiêu đề vẫn 8 cột đúng thứ tự; thân = đúng tập con, ⊊ (a), không lẫn ngoài bộ lọc (`:662`) | ✅ 8/8 · 2 hàng · ⊊ · không lẫn 2 mã bị lọc ra |
| 4 | Cả 2 lượt đối chiếu **theo tập mã**, không chỉ theo số lượng | ✅ §14.3, §15.3 |
| 5 | Đã khai `⏸ CHƯA KIỂM TRA` cho ngưỡng 10.000 dòng | ✅ §18 + ô ghi sheet |
| 6 | Vân tay bản dựng đầu case = cuối case | ✅ §12 |

**Không điều kiện FAIL nào chạm:** xuất được · tệp mở được · đủ 8 cột · không thừa/thiếu/đảo cột · thân khớp tập
đang hiển thị · lượt (b) không lẫn bản ghi ngoài bộ lọc · không lẫn DN khác · **0** lệnh 4xx/5xx.

**Triệu chứng gốc đối tác báo (*"Màn hình không có nút chức năng"*)** — đã **mở ảnh bằng chứng của đối tác đọc
lại** (`F4-pilot-QLHSPLDN-2026-08-07/partner-evidence/QLHSPLDN_15.jpg`): thẻ *Hồ sơ pháp lý DN* của `DN-HNI-0011`
đi thẳng từ tiêu đề + nút *Thêm hồ sơ* xuống hàng tiêu đề bảng rồi tới phân trang — **không có hàng bộ lọc, không
có nút Tìm kiếm, không có nút Xuất Excel**. Nay hàng đó đã đủ và chạy đúng ⇒ dùng `✅ ĐÃ HẾT LỖI`.

**Ghi ô Drive:** `Trạng thái dev fix` = **`UAT done`** · `Kết quả verify` = nội dung ở
[`note/note-sheet-QLHSPLDN_14.txt`](../note/note-sheet-QLHSPLDN_14.txt).

**Giới hạn hiệu lực:** env `https://htpldn-uat.ospgroup.vn`, bản dựng `assets/index-Bd1akG3f.js`
(`last-modified Fri, 07 Aug 2026 08:15:32 GMT`), đo **15:34 → 15:37 giờ VN 07/08/2026**, vai trò `CB_NV_TW`,
trên `DN-XX-0005`.

## 18. Phần chưa đo được (lượt 2)

| Phần | Lý do | Ảnh hưởng verdict? |
|---|---|---|
| **Ngưỡng "tối đa 10.000 dòng"** (`srs-fr-12:663`) | ⏸ `DN-XX-0005` chỉ có **4** hồ sơ, thấp hơn ngưỡng rất nhiều. Muốn kiểm phải dựng khối lượng dữ liệu lớn — **không** làm trên env nghiệm thu của đối tác | ❌ **Không** — nguồn chuẩn §6.1 ghi rõ ngưỡng này không chặn Pass |
| Các chiều lọc còn lại của `:662` (*Loại hồ sơ*, khoảng ngày) | Đã chứng minh `:662` bằng **2 chiều** (từ khóa + trạng thái), đủ phép chứng minh. Thêm chiều nữa là mở rộng phạm vi ngoài phiếu | ❌ Không |
| Phạm vi hộp thoại CCCD trên màn / vai trò khác | Exploratory, brief §8 cấm — đã tách thành dòng bug riêng `QLHSPLDN_QA01` | ❌ Không |

## 19. Artifact lượt 2

| Ảnh | Thấy gì |
|---|---|
| `image/14-A-ban-dung-moi-hopthoai-CCCD-chan-nut-XuatExcel.png` | *(lượt 1)* hộp thoại CCCD che nút [Xuất Excel] — giữ làm bằng chứng cho dòng bug `QLHSPLDN_QA01` |
| `image/14-B-luot-b-loc-202608-HieuLuc-2hang-da-xuat-Excel.png` | *(lượt 2)* Màn `Chi tiết DN #DN-XX-0005`, tab **Hồ sơ pháp lý**, **không còn hộp thoại chặn**. Hàng bộ lọc hiện đủ: ô từ khóa mang `202608`, khung *Trạng thái* hiện `Hiệu lực`, và **thấy rõ 3 nút [Tìm kiếm] · [Xóa bộ lọc] · [Xuất Excel]**. Bảng bên dưới còn **đúng 2 hàng** `HSPL-20260803-0002` và `HSPL-20260803-0001`, cả hai *Hiệu lực* — đúng tập con mà tệp (b) chứa |

## 20. Đã ghi Drive — xác nhận đọc lại

| Việc | Kết quả |
|---|---|
| **Dòng 296** (`Mã TC = QLHSPLDN_14`, tab `bug`, gid 1714340219) | `Trạng thái dev fix`: `Test done` → **`UAT done`** · `Kết quả verify`: ghi đè bằng note **3 602 ký tự**. Công cụ `tools/sheet_bug_verify_write.py`, guard `--expect` khớp, chạy `--dry-run` trước. **Đọc lại xác nhận** bằng `sheet_read.py --row 296` + `sheet_dump_cell.py` → `diff` với `note/note-sheet-QLHSPLDN_14.txt` **sạch 0 dòng lệch**. Ô chỉ đọc (`Trạng thái` · `Kết quả thực tế` · `TKM phản hồi lần 1` · `DEV phản hồi lần 1`) **không đụng** |
| **Dòng bug mới `QLHSPLDN_QA01`** | Thêm ở **dòng 379** bằng `tools/sheet_add_bug_row.py` (đúng công cụ sẵn có, **không** viết script mới). Bộ ô: `Mã TC` · `Tên chức năng` = *Đăng nhập / Thông tin tài khoản* · `Mô tả` · `Các bước thực hiện` · `Kết quả mong đợi` (mô tả **yêu cầu nghiệp vụ**, dẫn 4 dòng SRS đã tự mở file xác minh: `srs-v3.5.md:5543`, `:5642`, `srs-fr-10-quan-tri.md:1734`, `:2110`) · `Kết quả thực tế` · `Trạng thái` = `Fail` · `Dopai` = `bug` · `Ảnh/vieo 1` = link Drive xem được. **Đọc lại xác nhận** khớp 10/10 ô |
| Ảnh bằng chứng | `14-A-…png` đã tải lên Drive (batch `f9` thêm vào chính `tools/drive_upload_evidence.py`, chia sẻ "ai có link đều xem được") → `https://drive.google.com/file/d/1Ln7XPEEmCEDEr5anlXhbsnJkbXz8FvGN/view?usp=drivesdk` |
