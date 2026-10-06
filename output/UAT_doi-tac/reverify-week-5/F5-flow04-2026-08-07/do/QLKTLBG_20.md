# HỒ SƠ ĐO — QLKTLBG_20 (Flow 04 · Giai đoạn B)

> Chuẩn chấm đã khoá: [`chuan/QLKTLBG_20.md`](../chuan/QLKTLBG_20.md). File này chỉ ghi phép đo.
> **Không đổi quan hệ MATCH/DIFF/GAP.** C1 `MATCH · TEST` · C2a `MATCH · TEST` · C2b `GAP · BA`.
>
> 🔴 **ĐO ĐỘC LẬP với QLKTLBG_19.** Case 19 cùng màn vừa ra Pass, nhưng vế C1 của case này đã **tự quan sát lại
> từ đầu** trong lượt đo riêng dưới đây; không mượn kết quả case 19 làm căn cứ (Flow 04 BƯỚC 0 — *cùng chữ không
> có nghĩa cùng nguyên nhân*).

---

## 1. Vân tay bản dựng (ghi đầu phiên)

| Mục | Giá trị thực đo |
|---|---|
| Env | `https://18.143.165.120.nip.io` |
| Giờ đo | **2026-08-07 02:44–02:49 giờ VN** (= 2026-08-06 19:44–19:49 GMT) |
| `last-modified` | `Thu, 06 Aug 2026 19:23:01 GMT` |
| `etag` | `W/"6a74df15-428"` |
| Bó mã FE | `/assets/index-D4Buvu4S.js` |
| Chuỗi phiên bản sidebar | `HTPLDN · V1.0.9` |

✅ **KHÔNG có deploy giữa lượt 2 và lượt này.** Cả 3 chỉ dấu (`last-modified` · `etag` · bó mã) **trùng khít**
vân tay lượt 2 (dòng 13, 02:30) ⇒ case 19 và case 20 đo trên **cùng một bản dựng**. (Vẫn đối chiếu bằng 3 chỉ
dấu chứ không bằng chuỗi `V1.0.9` trên màn — chuỗi đó đã từng lùi số dù bó mã mới hơn.)

**Đã tải lại trang** trước lô đo (chặn bẫy PASS-oan (k) — tab mở lâu vẫn chạy JS cũ): `navigate_page type=reload`
+ `ignoreCache=true` trên `/dao-tao/bai-giang/danh-sach`. Phiên đăng nhập còn hiệu lực sau khi tải lại (token
idle TTL 1800s) nên **không phải đăng nhập lại**, không tiêu lượt nào của giới hạn 5 lượt/60 giây.

---

## 2. Tài khoản thực dùng

| Mục | Giá trị |
|---|---|
| Tài khoản | **`cbnv_tw_02`** — đúng tài khoản prompt chỉ định, **không fallback**, không dùng `admin` |
| Danh tính đọc từ phiên | `CB Nghiệp vụ - Trung ương #02` (hiển thị trên thanh tiêu đề màn) |
| Định danh trong thẻ phiên | `vaiTro: ["CB_NV_TW"]` · `capDonVi: "TW"` · `donViId: 00000000-0000-4000-8000-000000000001` · `idleTtl: 1800` |
| Vai trò theo đặc tả | **CB NV** — `srs-fr-03-dao-tao.md:751`, đọc lại nguyên văn lượt này: `**Tác nhân:** CB NV / CB PD` ✅ khớp |

**KHÔNG dùng `admin` để ra verdict** (chặn bẫy (j) — "đổi vai trò cho ra nút" là PASS-oan kinh điển).

---

## 3. Màn + tiền đề

| Mục | Giá trị |
|---|---|
| URL màn (trước lọc) | `https://18.143.165.120.nip.io/dao-tao/bai-giang/danh-sach?page=1&pageSize=10` |
| URL màn (sau lọc) | `https://18.143.165.120.nip.io/dao-tao/bai-giang/danh-sach?pageSize=10&search=ZZQAKHONGTONTAI20260807&page=1` |
| Tiêu đề trang (`h1`) | `Kho tài liệu / Bài giảng` |
| **N = tổng bản ghi khi KHÔNG lọc** | **11** |
| Từ khoá lọc đã dùng | **`ZZQAKHONGTONTAI20260807`** (đúng giá trị chuẩn chấm §6 T3, không phải đổi sang biến thể `…X`) |
| **`meta.total` sau lọc** | **0** |

### 3.1. Nguồn của N = 11 — số thô trước, các chiều cộng khớp

| Chiều | Giá trị | Nguồn |
|---|---|---|
| Số thô `meta.total` | **11** | `GET /api/v1/bai-giangs?page=1&pageSize=10` (reqid=381, HTTP 200) |
| `meta.totalPages` × `pageSize` | 2 trang × 10 | cùng phản hồi — khớp với 11 bản ghi |
| Chữ trên màn | `Hiển thị 1-10 / 11 kết quả` | `innerText` của `.ant-pagination-total-text` |

→ Các chiều **cộng khớp** ⇒ N = 11 dùng được.

**Chip "Bộ lọc nâng cao (2)" KHÔNG phải bộ lọc đang áp.** Đã kiểm bằng chính tham số màn gửi lên máy chủ:
`GET /api/v1/bai-giangs?page=1&pageSize=10` — **chỉ có tham số phân trang, không có tham số lọc nào**. Con số
(2) là số ô lọc bên trong khung nâng cao. ⇒ N = 11 là tổng thật trong phạm vi tài khoản, không phải tổng đã lọc.

### 3.2. Xác nhận màn về 0 bản ghi TRƯỚC khi bấm xuất (tiền đề bắt buộc T4)

| Chiều | Giá trị | Nguồn |
|---|---|---|
| Số thô `meta.total` sau lọc | **0** | `GET /api/v1/bai-giangs?keyword=ZZQAKHONGTONTAI20260807&page=1&pageSize=10` (reqid=388, HTTP 200) |
| `meta.totalPages` | **0** | cùng phản hồi |
| Độ dài mảng `data` | **0** | cùng phản hồi |
| Số dòng bảng trên màn | **0** | `document.querySelectorAll('.ant-table-tbody tr.ant-table-row').length` |
| Chữ trạng thái rỗng (`innerText`) | **`Không có bài giảng nào phù hợp.`** | `innerText` của `.ant-table-tbody` |
| Vùng phân trang | **không hiển thị** | `.ant-pagination` không có trên màn |
| Giá trị còn trong ô từ khoá | `ZZQAKHONGTONTAI20260807` | `input[placeholder="Tìm theo tên bài giảng"].value` |

→ **T3 + T4 THOẢ.** Sáu chiều đều nói 0, không chiều nào lệch. Ảnh mốc này:
[`image/QLKTLBG_20-01-bo-loc-0-ket-qua.png`](../image/QLKTLBG_20-01-bo-loc-0-ket-qua.png).

### 3.3. 🔴 Khai báo trung thực — một lời gọi hỏng do tôi đoán sai tên tham số

Lần đầu tôi tự dựng lời gọi đối chứng với tham số `search=` (đoán theo query của địa chỉ trên trình duyệt) →
trả về `total: 11`, tưởng như bộ lọc không ăn. **Đó là lỗi của tôi, không phải của phần mềm**: tham số thật màn
gửi lên là `keyword=` (đọc từ reqid=388), còn `search=` chỉ là query của tuyến giao diện. Máy chủ bỏ qua tham số
lạ nên trả nguyên 11.

Lời gọi hỏng đó là **reqid=389** — ghi ra đây để người đọc nhật ký mạng không hiểu nhầm thành hai phép đo mâu
thuẫn. Sau khi đọc đúng tham số, mọi chiều đều nhất quán ở 0. **Không có phép đo nào mâu thuẫn.**

---

## 4. VẾ C1 — màn có chức năng Xuất Excel

> Chuẩn chấm: `MATCH · route TEST`. Neo `srs-fr-03-dao-tao.md:1952` + `srs-v3.5.md:5570`.

### 4.1. Đường UI — liệt kê DOM thanh công cụ (không kết luận bằng mắt qua ảnh)

Liệt kê **mọi** `button` / `a` / `[role=button]` trong `<main>` **trừ** vùng `.ant-table`, trả `innerText` +
`title` + `aria-label` + `className` + `disabled` + `visible` (chặn bẫy (b) — nút có thể là icon không nhãn):

| # | `innerText` | `title` / `aria-label` | `disabled` | `visible` |
|---|---|---|---|---|
| 1 | `Thêm mới` | — / — | false | true |
| 2 | **`Xuất Excel`** | — / — | **false** | **true** |
| 3 | `Làm mới` | — / — | false | true |
| 4 | *(rỗng)* | — / — | false | true — `ant-input-clear-icon` (nút xoá ô từ khoá) |
| 5 | `Bộ lọc nâng cao (2)` | — / — | false | true |
| 6 | `Xóa bộ lọc` | — / — | false | true |
| 7 | `Tìm kiếm` | — / — | false | true |
| 8–11 | *(phân trang)* | — / — | — | true |

Tổng 11 phần tử vùng thanh công cụ. Quét thêm **toàn màn** với bộ lọc regex `excel|xuất|export` trên
`innerText` + `title` + `aria-label` → đúng **1** kết quả duy nhất: nút `Xuất Excel` ở trên.

⇒ **Không cần mở menu phụ**: không tồn tại kebab `…` / "Thao tác khác" / dropdown nào ở vùng thanh công cụ, và
nút đã tìm thấy trực tiếp.

**Phân biệt với `Tải về` per-row (bẫy (e)):** nút đo được nằm ở **thanh công cụ đầu màn**, đã loại trừ vùng
`.ant-table` khỏi phép liệt kê. Bốn biểu tượng cột "Thao tác" của từng dòng (xem · tải về · sửa · xóa) thuộc
`srs-fr-03-dao-tao.md:1974` (`| Hành động | — | Xem trực tuyến · Tải về (chỉ Slide/PDF) · Sửa · Xóa (xóa mềm,
có hộp xác nhận) |`) — ở lượt đo này bảng rỗng nên chúng **không hiện**, càng không thể lẫn.

### 4.2. Đối chứng độc lập — danh mục chức năng máy chủ công bố

`GET /api/docs-json` (HTTP 200, 549 đường dẫn). Lọc đường dẫn chứa `bai-giang` → **12** kết quả; lọc tiếp
`export|excel|xuat`:

```
POST /api/v1/bai-giangs/export — summary: "Xuất danh sách bài giảng ra Excel"
```

**Không đoán đường dẫn** — đường dẫn này đọc ra từ danh mục máy chủ công bố, và chính là đường dẫn màn gọi khi
bấm nút (xem §5.3).

### 4.3. Kết luận C1

**ĐẠT.** Hai đường khớp (giao diện có nút hiển thị + máy chủ công bố chức năng xuất), **dừng, không mở đường
thứ ba**. Triệu chứng ghi trên phiếu — *"Màn hình không có nút chức năng"* — **không tái hiện** trên bản dựng đo.

---

## 5. VẾ C2 — bộ lọc ra 0 kết quả

> C2a `MATCH · TEST` (nhánh (a) *xuất danh sách rỗng*) · C2b `GAP · BA` (nhánh (b) *hiển thị thông báo*).
> Expected đối tác là **mệnh đề HOẶC** — chỉ cần một nhánh xảy ra là vế nội dung đạt.

### 5.1. Bộ bắt thông báo — cài TRƯỚC khi bấm, đã tự kiểm

Bộ bắt thuộc vế Cn (nhánh (b) chính là "hiển thị thông báo") nên **bắt buộc** cài trước thao tác.
Dùng nguyên khối [`tools/toast-capture.js`](../../../tools/toast-capture.js): `MutationObserver` trên
`document.body`, đọc bằng **`innerText`**, **không lọc trùng**, đếm kèm số lời gọi ghi.

**Tự kiểm số observer trước khi tin số liệu:** chèn node giả `NODE_TU_KIEM` → ghi nhận **đúng 1 lần**
(`soObserverDangSong = 1`, `hopLe = true`) ⇒ **số liệu hợp lệ**, không bị nhân bản.

### 5.2. Thao tác — bấm Xuất Excel trên giao diện thật, ĐÚNG 1 LẦN

Bấm bằng sự kiện click thật trên chính phần tử nút `Xuất Excel` của màn (`innerText === 'Xuất Excel'`,
`disabled === false`), **không gọi thẳng API thay cho thao tác**. Thao tác được hẹn giờ sau 2500ms rồi chụp ảnh
ngay (đảo thứ tự) để cố bắt thông báo tự tắt.

### 5.3. Ba quan sát bắt buộc

**(i) Hệ thống CÓ tạo tệp không → CÓ.**

| Mục | Giá trị |
|---|---|
| Tên tệp | `DanhSachBaiGiang_20260807_0248.xlsx` |
| Kích thước | **6 687 bytes** |
| Về đĩa lúc | `2026-08-07 02:48` giờ VN |
| Phân biệt với tệp lượt trước | Tệp case 19 là `…_0234.xlsx` (02:34, 7 636 bytes) — **khác mốc giờ, khác kích thước, khác nội dung**; không lẫn |
| Bản giữ lại | [`seed-files/QLKTLBG_20-xuat-excel-bo-loc-0-ket-qua-0248.xlsx`](../seed-files/QLKTLBG_20-xuat-excel-bo-loc-0-ket-qua-0248.xlsx) |
| `sha256` | `a88970f2f31cd207f34042c75f12c202f8569030d2f7c08d8008549c9037d795` |

**(ii) Chữ người dùng nhìn thấy (`innerText`) → `Xuất dữ liệu thành công.`**

| Mục | Giá trị |
|---|---|
| Số khung thông báo | **1** (không lặp) |
| Nguyên văn | **`Xuất dữ liệu thành công.`** |
| Loại | toast (tự tắt ~3s) |
| Số lời gọi ghi kèm theo | **1** — `POST /api/v1/bai-giangs/export` |
| Khoảng cách giữa 2 khung | không áp dụng (chỉ 1 khung) |
| Độ trễ hiện thông báo | ~155ms sau khi bấm (bấm `160050.1` → thông báo `160205.3`) |

Đây **không phải** thông báo "không có dữ liệu" ⇒ **nhánh (b) KHÔNG xảy ra**.

**(iii) Mã HTTP + thân phản hồi của chính lời gọi xuất:**

| Mục | Giá trị |
|---|---|
| Lời gọi | `POST /api/v1/bai-giangs/export` (reqid=394) |
| Mã trạng thái | **200** |
| **Thân yêu cầu** | **`{"keyword":"ZZQAKHONGTONTAI20260807"}`** ← màn **CÓ** truyền bộ lọc lên chức năng xuất |
| `content-type` phản hồi | `application/vnd.openxmlformats-officedocument.spreadsheetml.sheet` |
| `content-disposition` | `attachment; filename="DanhSachBaiGiang_20260807_0248.xlsx"` ← khớp tệp đã mở |
| `content-length` | `6687` ← khớp kích thước tệp trên đĩa |
| **`x-export-total`** | **`0`** ← máy chủ tự khai tổng bản ghi khớp bộ lọc = 0 |
| **`x-export-exported`** | **`0`** ← máy chủ tự khai số bản ghi đã xuất = 0 |

### 5.4. Đối chứng độc lập — MỞ TỆP đếm dòng (không dừng ở "tải được tệp")

`openpyxl.load_workbook(read_only=True)` trên chính tệp đã giữ lại:

| Mục | Giá trị đo |
|---|---|
| Số trang tính | 1 — tên `Bài giảng` |
| `max_row` | **1** |
| `max_column` | 8 |
| Số dòng có nội dung | **1** |
| Hàng tiêu đề | `Tên bài giảng` · `Loại tài liệu` · `Lĩnh vực` · `Dung lượng` · `Công khai` · `Người tạo` · `Ngày tạo` · `Mô tả` |
| **SỐ DÒNG DỮ LIỆU = tổng dòng − dòng tiêu đề** | **1 − 1 = 0** |

🔴 **Đã chặn ca PASS-oan nguy hiểm nhất của case này** (bẫy (d)): tệp **không** chứa bản ghi nào ngoài bộ lọc.
Nếu chức năng xuất bỏ qua bộ lọc thì tệp phải có 11 dòng dữ liệu (= N) — thực đo **0**.

### 5.5. Kết luận C2

**C2a ĐẠT** — nhánh (a) của mệnh đề HOẶC xảy ra: hệ thống **xuất danh sách rỗng**, tệp phản ánh **đúng bộ lọc
hiện tại**, đúng câu chữ *"File xuất theo bộ lọc hiện tại"* (`srs-v3.5.md:5570`) và *"xuất danh sách theo bộ
lọc hiện tại"* (`srs-fr-03-dao-tao.md:1952`).

Ba chiều số liệu độc lập đều nói **0** và **cộng khớp**: `meta.total` sau lọc = 0 · `x-export-total` /
`x-export-exported` = 0 · số dòng dữ liệu trong tệp = 0.

**C2b (GAP) KHÔNG kích hoạt.** Nhánh (b) không xảy ra (thông báo là "Xuất dữ liệu thành công.", không phải
"không có dữ liệu"), và vì mệnh đề là **HOẶC** nên nhánh (a) đã đạt là đủ. Theo bảng quyết định đã cam kết
TRƯỚC khi đo, ca này **không phát sinh câu hỏi BA** — nhánh (a) có neo SRS riêng (`srs-v3.5.md:5570`), không
phải vùng SRS im lặng.

⚠️ **Không chấm Fail vì nhánh còn lại của mệnh đề HOẶC** (bẫy (a)) — hệ thống không hiển thị thông báo "không
có dữ liệu", nhưng điều đó **không** làm vế không đạt.

---

## 6. Bẫy đã chủ động chặn

| Bẫy (chuẩn chấm §7) | Cách đã chặn |
|---|---|
| (a) Mệnh đề HOẶC — chấm Fail nhánh còn lại | Nhánh (a) đạt ⇒ vế đạt; không chấm Fail vì thiếu thông báo |
| (b) Nút là icon / nằm trong menu phụ | Liệt kê DOM đủ `innerText`+`title`+`aria-label`+`className`, không kết luận bằng mắt |
| (c) `textContent` gom node ẩn → bug ma | Toàn bộ chữ đọc bằng **`innerText`** |
| (c-2) Thông báo tự tắt | Observer cài **trước** thao tác, **không lọc trùng**, đã tự kiểm = 1 observer |
| (d) Tải được tệp ≠ nội dung đúng | **Đã mở tệp bằng `openpyxl`** đếm dòng — 0 dòng dữ liệu |
| (d-2) Không tệp + không thông báo nhưng có toast "thành công" | Không rơi vào ca này: tệp **có thật**, đã mở đọc, và `x-export-total: 0` xác nhận |
| (e) Nhầm "Tải về" per-row với "Xuất Excel" | Đã loại vùng `.ant-table` khỏi phép liệt kê; bảng rỗng nên cột Thao tác không hiện |
| (f) Tệp rỗng vẫn có dòng tiêu đề | Đếm **dòng dữ liệu** (tổng − tiêu đề), không đòi tệp trống byte |
| (h) Bộ cột tệp xuất | **Không chấm** theo bộ cột — SRS Nhóm III không quy định; chỉ ghi lại để tham khảo |
| (j) Đổi vai trò cho ra nút | Chỉ dùng `cbnv_tw_02`, **không** đụng `admin` |
| (k) Trang cũ / bản dựng cũ | Đã `reload` + `ignoreCache` trước lô đo, ghi vân tay 3 chỉ dấu |
| (l) Hai phép đo mâu thuẫn | Không có mâu thuẫn — lời gọi `search=` hỏng đã khai rõ ở §3.3 là do tôi đoán sai tham số |
| Trần 10.000 dòng · phạm vi `don_vi_id` | Không chấm — chưa chạm trần (N=11); phạm vi TW rộng là đúng `:1981` |
| Bảng §6 `:2243` thiếu FR-III-07/08 | Là mục lục tham chiếu chéo, **không** dùng đổi quan hệ C1 |

---

## 7. Ánh xạ vào BẢNG QUYẾT ĐỊNH đã khoá trước khi đo

**Bảng §1 của prompt điều phối:**

| Web hành xử thế nào khi bộ lọc ra 0 kết quả | Khớp? |
|---|---|
| **Xuất được tệp, tệp có 0 dòng dữ liệu** → Đạt qua nhánh (a), có neo SRS `srs-v3.5.md:5570` ⇒ **C2 ĐẠT, không phát sinh câu hỏi BA** | ✅ **HÀNG NÀY** |
| Chặn xuất + hiện thông báo "không có dữ liệu" ⇒ `BA confirm` | ✗ không xảy ra |
| Xuất tệp nhưng tệp chứa TOÀN BỘ danh sách ⇒ `Reopen` | ✗ đã loại: tệp 0 dòng, không phải 11 |
| Không có nút Xuất Excel ⇒ `Reopen` | ✗ đã loại: nút có, hiển thị, không vô hiệu hoá |
| Hành xử khác / hai phép đo mâu thuẫn ⇒ `Chưa chốt` | ✗ không có mâu thuẫn |

**Bảng quyết định trong chuẩn chấm §9** — khớp hàng: *"Có nút; tệp tải về, mở được, **0 dòng dữ liệu** →
Nhánh (a) — mọi vế MATCH đạt ⇒ thuộc nhóm **Pass**"*. Hai bảng **cùng kết luận**.

---

## 8. Cổng chốt verdict (Flow 04)

| # | Câu hỏi | Trả lời |
|---|---|---|
| 1 | Mỗi vế neo dòng nào của đúng SRS prompt cấp? | C1 → `srs-fr-03-dao-tao.md:1952` + `srs-v3.5.md:5570`; C2a → `srs-v3.5.md:5570`. **Đã tự mở đọc lại cả 4 dòng trong lượt này** (`:751`, `:1952`, `:1974`, `srs-v3.5.md:5570`), không mượn số dòng từ hồ sơ cũ |
| 2 | Mọi thao tác có trả lời một vế Cn / là đối chứng của vế đó? | Có. Lời gọi `search=` hỏng đã khai rõ §3.3 và **không** dùng làm căn cứ |
| 3 | Vế `DIFF/GAP` đã bị chặn Pass và có câu hỏi BA? | C2b `GAP` **không kích hoạt** — mệnh đề HOẶC đạt qua nhánh (a), nhánh này có neo SRS riêng. Đúng hàng 1 bảng §1 |
| 4 | Đã đọc đầy đủ expected, không dựa bản cắt ngắn? | Có — expected nguyên văn từ chuẩn chấm §4 |
| 5 | Điều kiện đo khớp tiền đề case? | Có — vai trò CB NV, bộ lọc ra 0 kết quả (`meta.total = 0` xác nhận trước khi bấm) |

---

## 9. VERDICT LOGIC

# ✅ Pass

- **C1 ĐẠT** — màn có chức năng Xuất Excel (giao diện + danh mục máy chủ, hai đường khớp).
- **C2 ĐẠT** qua **nhánh (a)** của mệnh đề HOẶC — xuất được tệp, tệp **0 dòng dữ liệu**, đúng bộ lọc hiện tại.
- **Không có vế nào phải chuyển BA** ở case này.

**Giá trị đề nghị ô `Trạng thái dev fix`: `Test done`.**

**Giới hạn hiệu lực:** chỉ cho môi trường `https://18.143.165.120.nip.io`, bản dựng `last-modified
19:23:01 GMT 06/08/2026` · `etag W/"6a74df15-428"` · bó mã `index-D4Buvu4S.js`, tại thời điểm đo 02:44–02:49
ngày 07/08/2026.

**Không suy đoán về tác dụng của bản sửa:** không có ảnh hiện trạng trước khi sửa ⇒ chỉ khẳng định **hiện trạng
đúng đặc tả**, không viết "bản sửa đã có tác dụng" (Flow 04 §Ca biên).

---

## 10. Artifact

| Đường dẫn | Chứng minh điều gì | Mốc giờ |
|---|---|---|
| [`image/QLKTLBG_20-01-bo-loc-0-ket-qua.png`](../image/QLKTLBG_20-01-bo-loc-0-ket-qua.png) | **Cả C1 lẫn tiền đề C2**: nút `Xuất Excel` hiện ở hàng hành động chính; ô từ khoá = `ZZQAKHONGTONTAI20260807`; bảng hiện `Không có bài giảng nào phù hợp.`; tài khoản `CB Nghiệp vụ - Trung ương #02` trên thanh tiêu đề | 2026-08-07 02:47 |
| [`seed-files/QLKTLBG_20-xuat-excel-bo-loc-0-ket-qua-0248.xlsx`](../seed-files/QLKTLBG_20-xuat-excel-bo-loc-0-ket-qua-0248.xlsx) | **Số đo quyết định C2a**: tệp xuất ra có **0 dòng dữ liệu** (chỉ 1 hàng tiêu đề). `sha256 a88970f2…9037d795` | 2026-08-07 02:48 |

**Đã mở lại ảnh xác nhận nội dung khớp mô tả.** ✅

**Ảnh chụp ngay sau khi bấm đã bị loại**: chụp trượt thông báo (thông báo hiện 155ms sau khi bấm) và **md5 trùng
khít** ảnh 01 (`d23227323b33aceba93b5222b086a8ce`) ⇒ là bản sao y hệt, không chứng minh thêm điều gì. Đã xoá để
tránh "hai ảnh trùng nhau mang hai chú thích khác nhau". **Không bấm lại chỉ để chụp lại** (chuẩn chấm §7 c-2) —
chữ thông báo đã bắt được bằng `innerText` và phản hồi máy chủ (`x-export-total: 0`) là bằng chứng mạnh hơn ảnh.

---

## 11. Bug mới / candidate / seed

**Bug mới:** không có.

**Nhật ký trình duyệt:** sạch — 0 lỗi, 0 cảnh báo trong suốt lô đo.

**Candidate (1 dòng, TÀI LIỆU — không phải bug phần mềm):** bảng tổng quan §6 tại
`srs-fr-03-dao-tao.md:2243` liệt kê BR-DATA-06 cho FR-III-01/05/06/14 mà **thiếu FR-III-07 và FR-III-08**,
trong khi đặc tả màn SCR-III-03 (`:1952`) lại dẫn thẳng BR-DATA-06 — đề nghị BA bổ sung cho khớp.
*(Đã nêu sẵn ở chuẩn chấm §4; không đổi quan hệ C1 và không chặn bàn giao.)*

**Ghi nhận trung tính, KHÔNG phải bug:** khi tập kết quả rỗng, hệ thống báo `Xuất dữ liệu thành công.` thay vì
một thông báo dạng "không có dữ liệu" như hai màn khác đã được BA chốt (`srs-fr-13-tv-nhanh.md:155` —
`INF-KHO-XL-01`; `srs-fr-15-ct-htpldn.md:403` — `INF-XI-02-XL-01`). **Không log bug** vì: (1) SRS Nhóm III
im lặng về câu chữ này — bẫy (g) cấm chấm Fail theo câu chữ của màn khác; (2) expected đối tác là mệnh đề
HOẶC và **đã thoả qua nhánh (a)**; (3) thông báo đúng sự thật — hệ thống đã xuất tệp thành công.

**Seed / mutate:** **KHÔNG có.** Không tạo, sửa, xoá bản ghi nào. Thao tác duy nhất là nhập từ khoá vào ô tìm
kiếm (không làm thay đổi dữ liệu). Toàn bộ 11 bản ghi là dữ liệu QA có sẵn; **không đụng dữ liệu đối tác**.
