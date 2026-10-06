# GIAI ĐOẠN B — số đo thô · `QLHSPLDN_13` (tab `bug`, dòng 295 — "Khoảng ngày không hợp lệ")

```
Lô:            F9 — tái xác nhận trên env NGHIỆM THU của đối tác
Flow:          flows/03-reverify-sau-dev-fix.md — NHÁNH 2 "Tái xác nhận trên môi trường khác"
Nguồn chuẩn:   chuan/QLHSPLDN_13.md (Giai đoạn A đã khoá) — làm đúng theo, không tự thêm/bớt vế
Env đo:        https://htpldn-uat.ospgroup.vn  (env nghiệm thu của đối tác)
Người đo:      agent ĐO · 2026-08-07 · phiên 14:51 → 15:00 giờ VN
```

---

## 1. Vân tay bản dựng — ĐẦU và CUỐI case

| Hạng mục | ĐẦU case — **14:51:18 VN 07/08** | CUỐI case — **14:59:55 VN 07/08** |
|---|---|---|
| Bó mã JS (máy chủ đang phát) | `assets/index-D4NhKEjr.js` | `assets/index-D4NhKEjr.js` |
| Bó mã CSS | `assets/index-DVlgOkLg.css` | `assets/index-DVlgOkLg.css` |
| `GET /` `last-modified` | `Fri, 07 Aug 2026 04:17:55 GMT` (= 11:17 VN) | `Fri, 07 Aug 2026 04:17:55 GMT` |
| `GET /` `etag` | `W/"6a755c73-428"` | `W/"6a755c73-428"` |
| Máy chủ web | `nginx` | `nginx` |
| Chuỗi chân sidebar | `HTPLDN · V1.0.10` | `HTPLDN · V1.0.10` |
| **Thẻ script đang nạp trong tab** | `/assets/index-D4NhKEjr.js` | `/assets/index-D4NhKEjr.js` |

> ✅ **Hai đầu TRÙNG KHỚP tuyệt đối** ⇒ không có deploy chen giữa case ⇒ không phải khai quan sát nào rơi
> trước/sau mốc deploy. Trùng luôn vân tay 4 case `_06` / `_07` / `_11` / `_12` đo trước cùng phiên.
>
> ✅ **Đã loại bẫy "tab mở lâu vẫn chạy mã cũ" mà KHÔNG cần tải lại trang:** đọc trực tiếp
> `document.querySelectorAll('script[src]')` trong tab → đúng **`/assets/index-D4NhKEjr.js`**, trùng khít bó mã
> máy chủ đang phát ở **cả hai đầu**. Tên bó mã có băm nội dung ⇒ mã đang chạy trong tab **chính là** bản dựng
> hiện hành.

---

## 2. Tài khoản thực dùng + xác nhận vai trò

| Hạng mục | Giá trị |
|---|---|
| Tài khoản | **`cbnv_tw`** (đúng tài khoản chỉ định, **không** phải fallback) |
| Cách vào phiên | **Dùng lại phiên đang sống** của các case trước cùng lô — `GET /api/v1/auth/me` → **200** ở **cả đầu và cuối** case |
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

Case chỉ đọc ⇒ đúng nguồn chuẩn §5: **không seed gì**. Nhánh đo là nhánh **từ chối trước khi truy vấn**, nên
toàn case **không phát sinh một lệnh nghiệp vụ nào** (chi tiết §4.5).

**Doanh nghiệp đo:** **`DN-XX-0005`** — *Công ty TNHH Mẫu Test* (`1a715c55-bc31-46de-ae07-56dd4f403ce5`), đúng DN
nguồn chuẩn §5 chỉ định, dùng chung phiên với `_11` / `_12`.

**4 hồ sơ của DN đó — CHỈ ĐỌC, không đụng:** `HSPL-20260804-0001` · `HSPL-20260803-0002` · `HSPL-20260803-0001`
· `HSPL-20260731-0002`.

> 🔴 **Tuân thủ kỷ luật dữ liệu §4 brief:** không sửa, không xoá, không thêm hồ sơ nào. Không bấm
> `Xem` / `Sửa` / `Xoá` / `Thêm hồ sơ` / `Xuất Excel` trên bất kỳ hàng nào. Chỉ chạm 2 ô ngày, nút
> **[Tìm kiếm]** và nút **[Xóa bộ lọc]**.

**Đường UI đã đi:** dùng lại tab đang mở ở thẻ **Hồ sơ pháp lý** của `DN-XX-0005` (nền sạch 4 hàng do `_12` bàn
giao) → đặt *Từ ngày* → đặt *Đến ngày* → bấm **[Tìm kiếm]** → bấm lặp → **[Xóa bộ lọc]** trả nền sạch.
Không gõ thẳng URL, không tải lại trang.

---

## 4. Số đo thô

### 4.0 — Nền so sánh trước khi đặt ngày · 14:52 VN

| Nguồn | Số đo |
|---|---|
| Bảng trên màn (`tr.ant-table-row`) | **4 hàng** — đúng 4 mã ở §3 |
| Ô từ khóa | **trống** (độ dài 0) |
| Hai ô chọn *Loại hồ sơ* / *Trạng thái* | **chưa chọn** |
| Hai ô ngày | **cả hai trống** |
| Phần tử thông báo đang sống trên màn | **0** |

⇒ Không còn bộ lọc tồn dư từ case trước (đúng yêu cầu nguồn chuẩn §5 "dọn trạng thái trước khi đo").

### 4.0b — Tự kiểm BỘ BẮT THÔNG BÁO còn sống (bắt buộc, nguồn chuẩn §4 mục 2)

Bộ bắt = `MutationObserver` trên `document.body` (`childList` + `subtree`), đọc **`innerText`** (CẤM
`textContent`), **KHÔNG lọc trùng**, ghi mọi node thoả bộ chọn thông báo kèm mốc giờ.

| Mốc tự kiểm | Cách chứng minh | Kết quả |
|---|---|---|
| Sau khi cài, trước lượt 1 | Chèn node mồi `__QA13_PROBE__` mang class `.ant-message-notice-wrapper` | ✅ bộ bắt ghi được node mồi kèm `innerText` ⇒ **CÒN SỐNG** |
| Ngay **trước** cú bấm lượt 1 | Node mồi `__QA13_PROBE2__` | ✅ **CÒN SỐNG** |
| Ngay **trước** cú bấm lượt 2 | Node mồi `__QA13_PROBE3__` | ✅ **CÒN SỐNG** |

⇒ Mọi số "0 thông báo" (nếu có) đều có nghĩa. Node mồi được **gỡ khỏi DOM ngay sau khi kiểm**, không lẫn vào số đo.

Bộ đếm lượt gọi máy chủ bọc **CẢ `fetch` LẪN `XMLHttpRequest`** — bắt buộc, vì `_12` đã chứng minh màn này gửi
bằng **XHR**; chỉ bọc `fetch` sẽ báo 0 request sai.

### 4.1 — Giá trị THẬT SỰ đặt được vào 2 ô ngày

Ô ngày là `.ant-picker` ⇒ điền bằng **clear trước → đặt qua setter gốc `HTMLInputElement.prototype.value` → phát
`input` → phát `Enter`**. **Không** dùng `fill_form` (nối chuỗi).

| Ô | Giá trị đích | **Giá trị đọc lại được trong ô** | Xác nhận độc lập bằng cây a11y |
|---|---|---|---|
| *Từ ngày* | `31/12/2026` | **`31/12/2026`** | `uid=55_8 textbox "Từ ngày" value="31/12/2026"` |
| *Đến ngày* | `01/01/2026` | **`01/01/2026`** | `uid=55_10 textbox "Đến ngày" value="01/01/2026"` |

⇒ Cặp ngày **thực sự ngược** (`tu_ngay` **31/12/2026** > `den_ngay` **01/01/2026**), đúng Bước 4 của phiếu và
đúng nhánh E6. **Không** dùng cặp bằng nhau (`:596` cho phép `tu_ngay <= den_ngay` nên bằng nhau là hợp lệ).

Giá trị được xác nhận **hai đường độc lập**: script đọc `.value` **và** cây a11y của snapshot ⇒ loại khả năng
script tự đọc lại chính thứ mình vừa ghi.

**Ghi nhận thêm khi đặt ô:** đặt **một mình** *Từ ngày* (chưa đặt *Đến ngày*) → **0 lệnh nghiệp vụ** phát sinh
(chỉ có `GET /api/v1/auth/me` chạy nền của khung ứng dụng). ⇒ Hiện tượng candidate của vòng env nội bộ
(*"đặt một mình Từ ngày thì hệ thống tự phát truy vấn"*) **KHÔNG tái hiện** trên env + bản dựng này.

### 4.2 — LƯỢT BẤM 1 (phép đo quyết định) · 14:54:04 VN

**Thao tác bằng UI thật:** bấm nút **[Tìm kiếm]** bằng **chuột thật qua CDP** (`click` theo `uid`), không phải
gọi hàm trong trang.

| Hạng mục | Số đo |
|---|---|
| **Số thông báo bắt được** | **ĐÚNG 1** (xem §4.4 chứng minh không nhân đôi) |
| **Chuỗi đọc được** (`innerText`) | **`Ngày bắt đầu phải trước ngày kết thúc`** |
| Kênh hiển thị | thanh nổi giữa đỉnh màn — `div.ant-message-notice-wrapper` › `div.ant-message-notice.ant-message-notice-error` |
| Lỗi gắn dưới ô nhập (`.ant-form-item-explain-error`) | **0** |
| **Lượt gọi máy chủ NGHIỆP VỤ do cú bấm** | **0** — không có lệnh `ho-so-phap-ly-dns` nào |
| Lệnh nền không liên quan | 1 × `GET /api/v1/thong-baos/unread-count` (XHR, 200) — bộ đếm thông báo chạy nền |
| Số hàng bảng **trước** bấm | **4** |
| Số hàng bảng **sau** bấm | **4** — **y nguyên**, đúng 4 mã cũ |
| Lệnh 4xx/5xx | **0** |

### 4.3 — So từng ký tự với đặc tả

Đặc tả (đã **tự mở file đọc lại** trong chính lượt này):
`Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-12-tv-chuyen-sau.md:700`

```
| E6 | tu_ngay > den_ngay (tìm kiếm) | ERR-HSPL-06 | "Ngày bắt đầu phải trước ngày kết thúc" | ERROR |
```

| Hạng mục | Giá trị |
|---|---|
| **Chuỗi trên màn** (`innerText`) | `Ngày bắt đầu phải trước ngày kết thúc` |
| **Chuỗi đặc tả `:700`** | `Ngày bắt đầu phải trước ngày kết thúc` |
| So `===` nguyên trạng | **`true`** |
| **SỐ KÝ TỰ LỆCH** | **0** |
| Vị trí ký tự lệch đầu tiên | **không có** (`-1`) |
| Độ dài (điểm mã) — thực tế / đặc tả | **37 / 37** |
| So sau chuẩn hoá **`NFC`** | **`true`**, **0 ký tự lệch** ⇒ loại khả năng lệch cách tổ hợp dấu tiếng Việt (NFC ↔ NFD) |
| Dãy điểm mã hai bên | **giống hệt từng phần tử**: `78,103,224,121,32,98,7855,116,32,273,7847,117,32,112,104,7843,105,32,116,114,432,7899,99,32,110,103,224,121,32,107,7871,116,32,116,104,250,99` |
| Khoảng trắng thừa đầu/cuối · khoảng trắng kép | **không có** |

⇒ **Khớp NGUYÊN VĂN TỪNG KÝ TỰ**, chứng minh bằng dãy điểm mã chứ không bằng mắt. Cũng trùng khít **từng ký tự**
với ô `Kết quả mong đợi` của phiếu đối tác.

### 4.4 — LƯỢT BẤM LẶP + loại dứt điểm ca "thông báo nhân đôi"

Đây là biến thể bắt buộc (nguồn chuẩn §3 biến thể (b)) và là điều kiện FAIL tường minh, nên được đo kỹ nhất.

**Vấn đề gặp phải:** bộ bắt ghi **2 lượt thêm** node `.ant-message-notice-wrapper` cho **cùng một** cú bấm. Nếu
đếm theo **số phần tử DOM** thì sẽ kết luận "nhân đôi" và chấm FAIL. Nguồn chuẩn §"BẪY CÔNG CỤ" đã cảnh báo đúng
chỗ này: **đếm theo mốc giờ / theo định danh node, KHÔNG theo số phần tử**.

**Đã dựng lại bộ bắt có gắn ĐỊNH DANH NODE (`WeakMap`) + theo dõi cả lượt GỠ node**, kết quả:

| Phép kiểm | Kết quả | Ý nghĩa |
|---|---|---|
| Số **node wrapper KHÁC NHAU** trong 1 cú bấm | **1** (`NODE_ID = 2` ở cả 2 lượt ghi) | 2 lượt ghi là **CÙNG MỘT node** được báo 2 lần ⇒ **KHÔNG** nhân đôi |
| Số wrapper **anh em cùng cha** `.ant-message` tại lúc thêm | **1** | Khay thông báo chỉ chứa đúng 1 thẻ |
| **Điểm danh DOM** mỗi 150 ms suốt vòng đời thông báo | **22 mẫu, mẫu nào cũng `wrappers = 1`** | Không lúc nào có 2 thông báo cùng tồn tại |
| Số lượt **GỠ** node wrapper | **1** (đúng `NODE_ID = 2`) | 1 thẻ sinh ra → 1 thẻ mất đi |
| Vòng đời thông báo | `07:55:41.579Z` → `07:55:44.913Z` = **3,33 giây** | Đúng thời lượng mặc định, tự tắt bình thường |

⇒ **KẾT LUẬN: đúng MỘT thông báo cho mỗi cú bấm, ở CẢ lượt 1 và lượt lặp.** Điều kiện FAIL "nhân đôi thông báo"
**không** xảy ra. Đây là chỗ dễ chấm oan nhất của case, đã loại bằng định danh node + điểm danh DOM chứ không
bằng cảm nhận.

**Số đo lượt bấm lặp (14:55:41 VN):** 1 thông báo · chuỗi y hệt · **0 ký tự lệch** · **0 lệnh nghiệp vụ** ·
bảng vẫn **4 hàng** đúng 4 mã cũ.

### 4.5 — Tổng hợp lượt gọi máy chủ toàn case (CHẨN ĐOÁN — không phải tiêu chí chấm)

| Lượt bấm [Tìm kiếm] | Giờ VN | Lệnh **nghiệp vụ** phát sinh | Thông báo | Hàng bảng |
|---|---|---|---|---|
| 1 (chuột thật qua CDP) | 14:54:04 | **0** | 1 · khớp 0 ký tự lệch | 4 → 4 |
| 2 (lặp — biến thể bắt buộc) | 14:55:41 | **0** | 1 · khớp 0 ký tự lệch | 4 → 4 |
| 3 (chụp ảnh) | 14:57:31 | **0** | 1 · chuỗi y hệt | 4 |
| 4 (chụp ảnh) | 14:58:08 | **0** | 1 · chuỗi y hệt | 4 |
| 5 (chụp ảnh) | 14:59:28 | **0** | 1 · chuỗi y hệt | 4 |

**Tổng: 5/5 lượt bấm → 0 lệnh `ho-so-phap-ly-dns`, 0 lệnh 4xx/5xx, mỗi lượt đúng 1 thông báo, bảng không đổi.**

> ⚠️ **Vì sao có 5 lượt bấm chứ không phải 2:** phép đo bắt buộc chỉ cần **2** (lượt 1 + lượt lặp) và **đã xong
> trọn vẹn ở 14:55:41**. Ba lượt sau **không phải biến thể đo mới**, chỉ để chụp cho được tấm ảnh mà nguồn chuẩn
> §4 liệt vào "ghi lại tối thiểu" — thông báo tự tắt sau 3,33 s trong khi độ trễ của công cụ chụp đo được là
> **> 5,8 s**, nên hai lần đầu chụp trượt. Lượt 5 hẹn giờ bấm sau 6.500 ms mới bắt kịp.
> Thao tác này **không đổi dữ liệu, không tạo đầu ra nghiệp vụ, không phát một lệnh nghiệp vụ nào** (đã chứng
> minh 5/5 ở bảng trên) nên không vi phạm kỷ luật dữ liệu env đối tác. **Tác dụng phụ có lợi:** 5 lượt cho kết
> quả giống hệt nhau ⇒ củng cố thêm mệnh đề "đúng 1 thông báo, không nhân đôi, không lần nào im lặng".
>
> **Ghi nhận thẳng (Flow 03 §Chạy.4 "không lặp thao tác chỉ để săn lại ảnh"):** ba lượt chụp là **lặp thao tác
> để lấy ảnh**, đúng thứ điều khoản đó khuyên tránh. Giữ lại ghi chú này để vòng sau cân nhắc, xem §10.

### 4.6 — Ghi nhận kèm (KHÔNG dùng để chấm)

| Hạng mục | Quan sát | Xếp loại theo nguồn chuẩn §6 |
|---|---|---|
| Kênh hiển thị là thanh nổi đỉnh màn, không phải lỗi gắn dưới ô nhập | `.ant-form-item-explain-error` = **0** | "KHÔNG được chấm Fail vì…" — SRS không quy định kênh |
| Mã `ERR-HSPL-06` không hiện trên giao diện | không thấy | "KHÔNG được chấm Fail vì…" — mã là định danh nội bộ của đặc tả |
| Ô ngày **không chặn nhập** cặp ngược (không có ô ngày nào bị làm mờ) | cho nhập rồi mới báo khi bấm | "KHÔNG được chấm Fail vì…" — SRS quy định phản hồi ở nhánh lỗi, không buộc khoá ô |
| Cảnh báo bảng điều khiển `Route path "/ticket=*" …` (mức `warn`) | có sẵn từ lúc khung ứng dụng khởi động | Không do case sinh ra — cũng đã ghi nhận ở `_12` |

---

## 5. Artifact quyết định verdict

Ở `F9-uatdoitac-QLHSPLDN-2026-08-07/image/`. Mỗi ảnh **đã được mở ra đọc bằng mắt**, không kết luận bằng script.

| Ảnh | Thấy gì trong ảnh |
|---|---|
| `13-A-cap-ngay-nguoc-31122026-01012026-bang-giu-nguyen-4-hang.png` | **Ảnh chứng minh bảng KHÔNG đổi.** Tiêu đề `Chi tiết DN #DN-XX-0005`, thẻ *Hồ sơ pháp lý* đang mở. Hai ô ngày hiện rõ **`31/12/2026`** (Từ ngày) và **`01/01/2026`** (Đến ngày) — đúng cặp ngược; ô từ khóa trống, hai ô chọn chưa chọn ⇒ cặp ngày là điều kiện lọc duy nhất. Bảng vẫn **đủ 4 hàng** đúng 4 mã cũ, còn ô phân trang số **1**. *(Ảnh chụp ngoài vòng đời 3,33 s của thanh thông báo nên không có thông báo trong khung — dùng để chứng minh bảng giữ nguyên, không dùng để kết luận về thông báo.)* |
| `13-B-thongbao-Ngay-bat-dau-phai-truoc-ngay-ket-thuc.png` | **Ảnh quyết định.** Giữa đỉnh màn có **đúng MỘT** thanh thông báo nền trắng, biểu tượng tròn đỏ dấu ✕, chữ đọc rõ **`Ngày bắt đầu phải trước ngày kết thúc`** — **không có thanh thứ hai** chồng lên. Bên dưới, hai ô ngày vẫn là **`31/12/2026`** và **`01/01/2026`**; bảng vẫn **đủ 4 hàng** (`HSPL-20260804-0001`, `HSPL-20260803-0002`, `HSPL-20260803-0001`, `HSPL-20260731-0002`) ⇒ hệ thống báo lỗi mà **không** trả danh sách theo khoảng ngày ngược. Badge góc phải `Cán bộ NV Trung ương` · `BTP · TW`. |

---

## 6. Verdict

# 📌 **Pass** — HIỆN TẠI ĐẠT

**Bám luật Flow 03 §Chốt (bảng Verdict logic), dòng "Pass":**

1. **Mọi vế đều `MATCH` và đều đạt.** Ba vế con nguồn chuẩn §2 — **C3a** thẻ có bộ lọc khoảng ngày và đặt được
   cặp ngược · **C3b** chặn và báo đúng câu · **C3c** đúng thẻ đang tranh chấp — đều đo được và đều đạt. Không
   vế nào FAIL. Triệu chứng đối tác báo (*"Không có trường thông tin tìm kiếm trên màn hình"*) **không tái hiện**.
2. **Đủ 7/7 điều kiện PASS của nguồn chuẩn §6:** ① có 2 ô ngày, đặt được cặp ngược `31/12/2026` > `01/01/2026`
   (xác nhận 2 đường độc lập) · ② mỗi lượt bấm bắt được **đúng 1** thông báo · ③ chuỗi khớp **0 ký tự lệch**,
   đọc bằng `innerText`, chứng minh bằng 37/37 điểm mã và cả sau chuẩn hoá `NFC` · ④ hệ thống **không** trả danh
   sách theo khoảng ngày ngược (bảng y nguyên 4 hàng, **0 lệnh nghiệp vụ**) · ⑤ lượt bấm lặp vẫn **đúng 1**,
   không nhân đôi · ⑥ bộ bắt thông báo tự kiểm còn sống **3 lần** · ⑦ vân tay bản dựng **đầu = cuối**.
3. **Biến thể bắt buộc đã chạy đủ 2/2** — (a) cặp ngày ngược đúng Bước 4 của phiếu · (b) lượt bấm lặp để loại ca
   nhân đôi.
4. **Không FAIL điều kiện nào ở nguồn chuẩn §6:** thẻ **có** ô ngày · thông báo **có** hiện · **0** ký tự lệch ·
   **không** nhân đôi · **không** trả danh sách theo khoảng ngược · **0** lệnh 5xx.
5. **KHÔNG Pass bằng quan sát tĩnh.** Không dừng ở "màn có 2 ô ngày": đã **đặt cặp ngày ngược thật**, **bấm nút
   thật bằng chuột qua CDP**, bắt thông báo bằng bộ quan sát cài **TRƯỚC** cú bấm, so **từng điểm mã**, và **mở
   ảnh đọc bằng mắt**.
6. **Có đối chứng độc lập cho quan sát quyết định**, đúng nghĩa Flow 03 §Chạy.3 — **không** lấy "bấm lại cùng
   nút" làm đối chứng:
   - cho mệnh đề *"đúng 1 thông báo"*: **định danh node** (`WeakMap`) + **điểm danh DOM 22 mẫu** + **nhật ký gỡ
     node** — ba đường khác nhau, cùng kết luận 1;
   - cho mệnh đề *"hệ thống từ chối tìm kiếm"*: **bộ đếm lệnh bọc cả `fetch` lẫn `XHR`** cho **0** lệnh nghiệp
     vụ, đối chiếu với **bảng giữ nguyên 4 hàng đúng 4 mã** đọc lại từ DOM;
   - cho mệnh đề *"cặp ngày đã đặt được thật"*: **cây a11y của snapshot** xác nhận `value=` độc lập với script.
7. **Đã loại đúng cái bẫy nguy hiểm nhất của case.** Bộ bắt ghi **2** lượt thêm node cho 1 cú bấm — nếu đếm theo
   số phần tử DOM sẽ chấm FAIL "nhân đôi thông báo" oan. Định danh node cho thấy đó là **cùng một node báo 2
   lần**, khay thông báo chỉ có 1 thẻ, và chỉ có 1 lượt gỡ.

**Về việc chặn ở tầng nào — KHÔNG dùng để chấm:** hệ thống chặn ngay ở **giao diện**, **0** lượt gọi máy chủ
nghiệp vụ trong cả 5 lần bấm. Đây là **chẩn đoán khai cho dev**, **không** phải tiêu chí Pass/Fail: `:700` chỉ
quy định **điều kiện lỗi → phản hồi → mức ERROR**, **không** quy định chặn ở tầng nào (đúng như prompt và nguồn
chuẩn §6 đã chốt trước).

**Giới hạn hiệu lực (bắt buộc ghi):** Pass này **chỉ có hiệu lực trên env `https://htpldn-uat.ospgroup.vn`**, bản
dựng `assets/index-D4NhKEjr.js` · `last-modified Fri, 07 Aug 2026 04:17:55 GMT`, đo lúc **14:51 → 15:00 giờ VN
07/08/2026**, vai trò **`CB_NV_TW`**, trên **`DN-XX-0005`** (chính DN trong bằng chứng của đối tác).

**Không viết "fix đã có tác dụng":** phiên này không có bằng chứng trạng thái trước fix trên chính env/bản dựng
này ⇒ chỉ kết luận **hiện trạng ĐẠT so với SRS + expected gốc**, dùng chữ *HIỆN TẠI ĐẠT*.

**Ghi ô Drive theo mapping §7 brief:** `Trạng thái dev fix` = **`UAT done`**.
*(Chưa ghi — dừng chờ điều phối theo yêu cầu prompt.)*

---

## 7. Bug mới / candidate

**Không có bug mới. Không có candidate mới.**

Toàn case: **0** lệnh nghiệp vụ, **0** lệnh 4xx/5xx, **0** lỗi bảng điều khiển mới. **Không dùng tới lượt xác
nhận bổ sung nào** (hạn mức 1 phép/case vẫn còn nguyên).

### Candidate cũ — đã có kết luận

| Candidate (từ vòng env nội bộ) | Kết quả trên env + bản dựng này |
|---|---|
| *"Đặt **một mình** ô Từ ngày (chưa đặt Đến ngày) thì hệ thống **tự phát truy vấn** mà không cần bấm Tìm kiếm"* | **KHÔNG tái hiện.** Hiện tượng tự lộ trong chính luồng bắt buộc (bước đặt ô ngày) nên đã quan sát đúng lúc: đặt xong *Từ ngày* → **0 lệnh nghiệp vụ**, bảng không đổi. Chỉ có `GET /api/v1/auth/me` chạy nền của khung ứng dụng. |

### Ghi nhận KHÔNG thành candidate

- **Thông báo hiện ở thanh nổi đỉnh màn, không phải lỗi gắn dưới ô nhập** — nguồn chuẩn §6 xếp đúng vào nhóm
  *"KHÔNG được chấm Fail vì…"*; `:700` không quy định kênh hiển thị.
- **Không thấy mã `ERR-HSPL-06` trên giao diện** — cùng nhóm trên; mã là định danh nội bộ của đặc tả.
- **Ô ngày cho nhập cặp ngược rồi mới báo khi bấm** — cùng nhóm trên; SRS quy định phản hồi ở nhánh lỗi, không
  buộc khoá ô.
- **Cảnh báo `Route path "/ticket=*" …`** (mức `warn`) — có sẵn từ lúc khung ứng dụng khởi động, không do cú bấm
  sinh ra, không chạm vế C3. Đã ghi nhận từ `_12`.
- **Chênh giữa `:596` (`tu_ngay <= den_ngay`, cho phép bằng nhau) và câu chữ `:700` (*"phải trước"*)** — nguồn
  chuẩn §7 đã chốt: phiếu chỉ đo nhánh **ngày bắt đầu SAU ngày kết thúc**, chênh này **không chạm phép đo**,
  **không** log, **không** đẩy BA.

---

## 8. Phần chưa đo được

| Phần | Lý do | Có ảnh hưởng verdict? |
|---|---|---|
| Cặp ngày **bằng nhau** (`tu_ngay = den_ngay`) | `:596` cho phép `tu_ngay <= den_ngay` ⇒ hợp lệ, **không** thuộc nhánh E6. Nguồn chuẩn §6 xếp vào "KHÔNG được chấm Fail vì…" và cấm đẩy BA | **Không** |
| Khoảng ngày ngược **kết hợp** từ khóa / bộ lọc loại · trạng thái | Nguồn chuẩn §3 khoá **đúng 2 biến thể**; thêm nữa là **vượt phạm vi đã khóa** + Flow 03 cấm tự nâng số biến thể | **Không** — biến thể bắt buộc đủ 2/2 |
| Khoảng ngày **hợp lệ** có ra kết quả đúng không | Thuộc vế C1 của **`QLHSPLDN_11`** (dòng 293), đã đo riêng và đạt | **Không** |
| Hành vi nút **Xuất Excel** khi khoảng ngày ngược | Thuộc **`QLHSPLDN_14`** (dòng 296), case khác. Case này **không bấm** nút đó | **Không** |
| Hành vi của vai trò khác (NHT, vai trò Doanh nghiệp ở `SCR-V.III-04`) | Ngoài vế — case chỉ đo đúng vai trò `CB_NV_TW` của đối tác. `srs-fr-07:514` còn cấm vai trò khác vào màn đó | **Không** |
| Chặn khoảng ngày ngược ở **tầng máy chủ** (gọi thẳng API với `tuNgay > denNgay`) | Hệ thống chặn ngay ở giao diện nên lệnh không bao giờ rời trình duyệt. Nguồn chuẩn §6 chốt rõ **tầng chặn không phải tiêu chí**; gọi thẳng API là thao tác ngoài đường UI đã khóa | **Không** |

---

## 9. Tự kiểm trước khi chốt (cổng Flow 03)

| # | Câu hỏi | Trả lời |
|---|---|---|
| 1 | Chuẩn chấm có bám đúng SRS hiện tại + expected gốc? | Có. Agent ĐO đã **tự mở lại** `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-12-tv-chuyen-sau.md` trong chính lượt này, đọc **dòng 700** (E6 · `ERR-HSPL-06` · câu *"Ngày bắt đầu phải trước ngày kết thúc"* · mức `ERROR`), **dòng 596** (`tu_ngay <= den_ngay`), **dòng 589/691** làm neo bảng — **không** bê số dòng từ báo cáo cũ. Số dòng khớp đúng nguồn chuẩn §2 |
| 2 | Có đo đúng phần còn lỗi, hay chạy lại phần đã đạt / kiểm chức năng kế bên? | Đo đúng vế C3 (nhánh **khoảng ngày ngược**). Không lặp lại vế C1 `_11` / C2 `_12` ngoài phần tối thiểu làm nền so sánh |
| 3 | Reopen đã có FAIL hợp lệ chưa; nếu có, vì sao còn chạy tiếp? | **Không có FAIL nào** ⇒ luật dừng sớm không kích hoạt; phải chạy hết mọi điều kiện PASS — đã chạy hết 7/7 |
| 4 | Pass đã phủ hết vế/biến thể nguồn chuẩn yêu cầu? | Có — **2/2** biến thể bắt buộc, đủ 7/7 điều kiện PASS, có đối chứng độc lập cho từng quan sát quyết định |
| 5 | Artifact có chứa quan sát quyết định và đã mở đọc lại? | Có — 2 ảnh, **từng ảnh đã mở ra đọc bằng mắt**, mô tả ở §5. Ảnh `13-B` chứa trực tiếp quan sát quyết định (đúng 1 thanh thông báo, đúng câu chữ, bảng vẫn 4 hàng) |
| 6 | Người ngoài phiên đo có phân biệt được phần đạt / cần BA / chưa đo? | Có — §4 số đo, §6 verdict, §7 không bug mới, §8 phần chưa đo, tách bạch |

---

## 10. Bàn giao trạng thái trình duyệt

- Trình duyệt + phiên `cbnv_tw` **giữ sống** (`GET /api/v1/auth/me` → **200** lúc cuối case). **0 lượt đăng nhập**
  đã tiêu trong cả case.
- Tab đang ở `https://htpldn-uat.ospgroup.vn/doanh-nghiep/1a715c55-…?tab=ho-so-pl`, đã bấm **[Xóa bộ lọc]** trả về
  **nền sạch**: 2 ô ngày **trống**, ô từ khóa **trống**, hai ô chọn **chưa chọn**, bảng **4 hàng** đúng 4 mã cũ
  ⇒ case sau (`QLHSPLDN_14` — Xuất Excel) khỏi dính bộ lọc tồn dư.
- Trong tab còn `window.__QA13` — bộ quan sát thông báo (có định danh node) + bộ đếm lệnh bọc **cả `fetch` lẫn
  `XMLHttpRequest`**, **trong suốt** (chỉ ghi lại, không đổi request/response). Mảng đã dọn rỗng, đồng hồ điểm
  danh đã dừng. Case sau dùng lại được, hoặc tải lại trang để gỡ. `window.__QA12` của case trước vẫn còn.
- Mọi node mồi tự kiểm (`__QA13_PROBE*`) **đã gỡ khỏi DOM**.

---

## 11. CẢI TIẾN FLOW (Flow 03 cho phép nêu khi có bằng chứng)

`CẢI TIẾN FLOW: Nguồn chuẩn §4 buộc "ghi lại tối thiểu" phải có ẢNH thông báo, trong khi Flow 03 §Chạy.4 cấm
"lặp thao tác chỉ để săn lại ảnh/toast" — hai điều khoản đá nhau khi thông báo tự tắt sau 3,33 s còn độ trễ công
cụ chụp đo được là > 5,8 s · ẢNH HƯỞNG: phải bấm thêm 3 lượt ngoài 2 lượt đo bắt buộc mới lấy được ảnh; ở case
có thao tác GHI thì 3 lượt thừa đó sẽ tạo dữ liệu rác trên env đối tác, rủi ro thật chứ không chỉ tốn công ·
CHỖ CẦN XEM LẠI: nên cho phép nguồn chuẩn chấp nhận "bản ghi bộ quan sát (innerText + định danh node + mốc giờ)
thay cho ảnh" đối với thông báo tự tắt — như chính prompt lô này đã nêu — và ghi rõ thứ tự ưu tiên để agent
không phải tự phân xử giữa hai điều khoản.`
