# NHẬT KÝ ĐO — QLKTLBG_19 (dòng 13) · Lô G3 · env nghiệm thu đối tác

> Chuẩn chấm khoá trước khi đo: [`chuan/QLKTLBG_19.md`](../chuan/QLKTLBG_19.md). Đo xong **không sửa** chuẩn.

## 1. Bảng đầu

| Mục | Giá trị |
|---|---|
| Mã TC / dòng | **QLKTLBG_19** · dòng **13** · "Xuất excel không có điều kiện lọc" |
| Env | **`https://htpldn-uat.ospgroup.vn`** (env NGHIỆM THU của đối tác) |
| **Bản dựng đọc trên UI** | **`HTPLDN · V1.0.10`** (chân khối logo sidebar) — đọc **sau** khi tải lại trang bỏ qua bộ nhớ đệm |
| Bó mã FE | `assets/index-Bd1akG3f.js` (đọc từ `script[src]` của trang sau khi tải lại) |
| Ngày giờ đo | **2026-08-07**, 16:46–16:52 giờ VN (09:46–09:52 UTC) |
| Tài khoản | **`cbnv_tw`** — `hoTen` "Cán bộ NV Trung ương", `vaiTro=["CB_NV_TW"]`, `capDonVi=TW`, `donViId=00000000-0000-4000-8000-000000000001` (Cục Bổ trợ tư pháp - BTP) — đọc thật từ `GET /api/v1/auth/me` HTTP 200 |
| Vai trò theo đặc tả | `srs-fr-03-dao-tao.md:751` — *"**Tác nhân:** CB NV / CB PD"* (FR-III-07). Tài khoản đo đúng vai trò CB NV |
| Màn | Đào tạo, tập huấn → Kho tài liệu / Bài giảng → Danh sách (**SCR-III-03**) |
| URL đạt được | `https://htpldn-uat.ospgroup.vn/dao-tao/bai-giang/danh-sach` |
| **Không đăng nhập lại** | Dùng đúng phiên sẵn có; không đăng xuất, không tốn lượt đăng nhập nào (giới hạn 5 lượt/60s) |
| Không đụng dữ liệu đối tác | Chỉ xem + xuất. **Không tạo / sửa / xoá bản ghi nào** |

## 2. B0 — Tải lại trang, đọc lại bản dựng

`navigate_page type=reload ignoreCache=true` trên `/dashboard`, rồi đọc lại trang:

- Chữ hiển thị trên UI: **`HTPLDN · V1.0.10`**
- `script[src]` duy nhất: `/assets/index-Bd1akG3f.js`

→ Bản dựng ghi trong báo cáo là số **đọc trên giao diện của chính env đối tác sau khi tải lại**, không mượn từ nguồn nào khác.

## 3. B1 — Điều hướng theo đúng bước 1 của phiếu

Bấm menu sidebar **"Đào tạo, tập huấn" → "Kho tài liệu / Bài giảng"** (sidebar đã ở trạng thái mở rộng, không cần thao tác thu gọn/mở).

- URL thực tế đạt được: **`https://htpldn-uat.ospgroup.vn/dao-tao/bai-giang/danh-sach`**
- Dải điều hướng: Trang chủ / Đào tạo, tập huấn / Kho tài liệu / Bài giảng / Danh sách
- Tiêu đề màn: **"Kho tài liệu / Bài giảng"**

## 4. B2 — Chứng minh "KHÔNG có điều kiện lọc" (chữ khoá của case)

### 4.1 Thao tác

Bấm **"Xóa bộ lọc"**, sau đó **mở khối "Bộ lọc nâng cao (2)"** kiểm từng ô bên trong.

### 4.2 Đọc trạng thái thật của mọi ô lọc (`innerText` / `value`, không dùng `textContent`)

| Ô lọc | Giá trị đọc được |
|---|---|
| Ô từ khóa "Tìm theo tên bài giảng" | `value` = **rỗng** |
| Loại tài liệu | không có `.ant-select-selection-item` → **chưa chọn** |
| Lĩnh vực pháp lý | không có `.ant-select-selection-item` → **chưa chọn** |
| Công khai | không có `.ant-select-selection-item` → **chưa chọn** |
| Từ ngày | `value` = **rỗng** |
| Đến ngày | `value` = **rỗng** |

### 4.3 🔴 Chứng cứ mạnh nhất — tham số màn thật sự gửi lên máy chủ

Lời gọi tải danh sách của màn:

```
GET /api/v1/bai-giangs?page=1&pageSize=20   → HTTP 200
```

**Chuỗi truy vấn chỉ có `page` + `pageSize`** — không có bất kỳ tham số lọc nào trong 7 tham số mà danh sách hỗ trợ
(`keyword · loaiTaiLieu · linhVucId · khoaHocId · congKhai · tuNgay · denNgay`). ⇒ Tiền đề **T2 đạt**: phép đo này
nói đúng về case "không có điều kiện lọc".

### 4.4 ⚠️ Bẫy chip "Bộ lọc nâng cao (2)" — đã kiểm, KHÔNG phải bộ lọc đang áp dụng

Chip **"Bộ lọc nâng cao (2)"** hiện sẵn ngay khi vào màn, y như trong ảnh bằng chứng của đối tác. Đã mở khối ra kiểm:
bên trong đúng **2 ô lọc** là **"Từ ngày"** và **"Đến ngày"**, **cả hai đều rỗng**. ⇒ Con số `(2)` là **số ô lọc nâng cao
có trong khung**, **không** có nghĩa "đang áp 2 điều kiện lọc". Chuỗi truy vấn ở §4.3 xác nhận điều này: không có
`tuNgay`/`denNgay` nào được gửi đi.

### 4.5 Tổng số bản ghi — lấy đủ CẢ HAI nguồn (chống bẫy k)

| Nguồn | Giá trị |
|---|---|
| Chữ hiển thị vùng phân trang (`innerText`) | **"Hiển thị 1-7 / 7 kết quả"** |
| Thân phản hồi danh sách | `meta` = `{"page":1,"pageSize":20,"total":7,"totalPages":1}` → **`total` = 7** |

**Hai nguồn khớp nhau → tổng bản ghi màn báo = 7.** Tiền đề **T3 đạt**. Cũng thoả **T5** (7 ≤ 10.000).

7 bản ghi đọc được (theo thứ tự màn): `Test ẩn file đính kèm` (PDF) · `Quản lý, thanh toán và quyết toán vốn đầu tư công`
(Video) · `Quy trình lập và quản lý kế hoạch đầu tư công…` (Video) · `Hướng dẫn lập, thẩm định và quản lý kế hoạch đầu tư
công trung hạn…` (Slide) · `Cẩm nang thực hiện nghĩa vụ thuế…` (PDF) · `Hướng dẫn kê khai, nộp thuế và sử dụng hóa đơn
điện tử…` (Slide) · `Test video 2` (Video, **Chưa công khai**).

## 5. B3 — VẾ 1: màn hình CÓ chức năng Xuất Excel hay không

**Không kết luận bằng mắt.** Đã liệt kê toàn bộ `button` / `a` / `[role=button]` trong vùng nội dung
(35 phần tử), tách theo vùng, đọc đủ `innerText` + `title` + `aria-label` + `className` + tên biểu tượng + `disabled`.

### 5.1 Vùng tiêu đề + thanh công cụ

| # | Thẻ | `innerText` | Biểu tượng | `disabled` | Vị trí |
|---|---|---|---|---|---|
| 1 | BUTTON | **Thêm mới** | `anticon-plus` | false | (1032, 80) |
| 2 | **BUTTON** | **Xuất Excel** | **`anticon-download`** | **false** | **(1161, 80)** |
| 3 | BUTTON | Làm mới | `anticon-reload` | false | (1296, 80) |
| 4 | BUTTON | *(rỗng)* | `anticon-close-circle` | false | nút xoá chữ của ô từ khoá (đang ẩn) |
| 5 | BUTTON | Bộ lọc nâng cao (2) | `anticon-up` | false | (461, 185) |
| 6 | BUTTON | Xóa bộ lọc | `anticon-clear` | false | (1144, 181) |
| 7 | BUTTON | Tìm kiếm | `anticon-search` | false | (1280, 181) |
| 8–10 | BUTTON / A | *(phân trang)* | `anticon-left` · `1` · `anticon-right` | 2 nút mũi tên `disabled` | chân bảng |

**Không có menu phụ nào ở thanh công cụ** (không có phần tử `haspopup` / `ant-dropdown-trigger` ở vùng tiêu đề) —
3 nút hành động đều phơi thẳng, không giấu trong menu.

### 5.2 ⚠️ Phân biệt với biểu tượng ở cột "Thao tác" (bẫy c)

Trong thân bảng có các nút chỉ-biểu-tượng ở cột **"Thao tác"** của **từng dòng**: `anticon-eye` (Xem trực tuyến) ·
`anticon-download` (**Tải về** — chỉ dòng Slide/PDF) · `anticon-edit` (Sửa) · `anticon-delete` (Xoá).
Đây là thao tác trên **một bài giảng**, **KHÔNG** phải chức năng xuất danh sách — khớp `srs-fr-03-dao-tao.md:1974`
(*"Hành động | — | Xem trực tuyến · Tải về (chỉ Slide/PDF) · Sửa · Xóa"*). Vế 1 chấm ở **thanh công cụ đầu màn**,
và ở đó **có** nút "Xuất Excel" riêng biệt (khác vị trí, có nhãn chữ, nằm ngoài `.ant-table`).

### 5.3 Đối chứng độc lập — hợp đồng dịch vụ

`GET /api/docs-json` (mở được, không cần đăng nhập) → đường dẫn **`/api/v1/bai-giangs/export`** **có tồn tại**,
phương thức POST, mô tả *"Xuất danh sách bài giảng ra Excel"*. **Không đoán đường dẫn** — đọc thẳng từ `paths`.

### 5.4 Ảnh đã chụp và đã mở đọc

`image/QLKTLBG_19-01-man-danh-sach-khong-loc.png` — **đã mở ảnh ra đọc**. Nhìn thấy: sidebar ghi `HTPLDN · V1.0.10`;
vùng tiêu đề "Kho tài liệu / Bài giảng" kèm **3 nút: `+ Thêm mới` (xanh) · `Xuất Excel` (viền, biểu tượng mũi tên xuống) ·
`Làm mới`**; thanh lọc 6 ô đều trống (Tìm theo tên bài giảng / Loại tài liệu / Lĩnh vực pháp lý / Công khai / Từ ngày /
Đến ngày) + `Bộ lọc nâng cao (2)` + `Xóa bộ lọc` + `Tìm kiếm`; bảng 7 dòng dữ liệu.

> **Khác biệt so với tiền đề của phiếu:** ảnh bằng chứng đối tác cùng màn (25/07/2026, bản dựng `HTPLDN · V1.0`) cho thấy
> vùng tiêu đề **chỉ có `+ Thêm mới` và `Làm mới`** — đúng như phản hồi TKM *"Màn hình không có nút chức năng"*.
> Trên bản dựng **V1.0.10** đang đo, nút **Xuất Excel** đã có mặt ở đúng vùng đó.

**⇒ VẾ 1 (C1): ĐẠT** (còn phải bấm được — xem §6).

## 6. B4 — VẾ 2: bấm nút và kiểm nội dung tệp

### 6.1 Bộ bắt thông báo

Cài **đúng `output/UAT_doi-tac/tools/toast-capture.js`** (đọc nguyên file, tiêm qua `evaluate_script`) **TRƯỚC** khi bấm.
Không tự viết bộ đo, **không lọc trùng**, đọc chữ bằng `innerText`.

**Tự kiểm số observer (bắt buộc trước khi tin số liệu):** `soObserverDangSong = 1` → **hợp lệ**, số liệu dùng được.

### 6.2 Bấm "Xuất Excel" — đúng 1 lần

| Số đo | Giá trị |
|---|---|
| Số lần bấm | **1** |
| **Số khung thông báo bắt được** | **1** |
| Nguyên văn thông báo | **"Xuất dữ liệu thành công."** |
| Bị lặp thông báo | **Không** (`BI_LAP=false`) |
| **Số request phát sinh (khác GET)** | **1** — `POST /api/v1/bai-giangs/export` |

⇒ 1 bấm = 1 lời gọi = 1 thông báo. Không gửi trùng, không hiện trùng.

### 6.3 🔴 Mã HTTP của lời gọi xuất

```
POST /api/v1/bai-giangs/export   →   HTTP 200
```

**Thân yêu cầu màn gửi đi: `{}`** (rỗng, `content-length: 2`) — xác nhận lần nữa **không đính kèm điều kiện lọc nào**.

Tiêu đề phản hồi:

| Tiêu đề | Giá trị |
|---|---|
| `content-type` | `application/vnd.openxmlformats-officedocument.spreadsheetml.sheet` |
| `content-disposition` | `attachment; filename="DanhSachBaiGiang_20260807_1649.xlsx"` |
| `content-length` | **8610** |
| **`x-export-exported`** | **7** |
| **`x-export-total`** | **7** |

> **Rủi ro R5 của khảo sát KHÔNG xảy ra.** Đã kiểm: hệ thống thật sự **không có** quyền `export_bai_giang`
> (`cbnv_tw` có 239 quyền, nhóm bài giảng chỉ `create/read/update/delete_bai_giang`), nhưng lời gọi xuất **trả 200**,
> không phải 403 — endpoint không chặn theo một quyền xuất riêng cho bài giảng. **Không đổi tài khoản để lách.**

### 6.4 MỞ TỆP RA ĐỌC NỘI DUNG (không dừng ở "tải được tệp")

Tệp **có** rơi về `~/Downloads`: `/Users/huongttt/Downloads/DanhSachBaiGiang_20260807_1649.xlsx`
· 8610 byte (**khớp đúng `content-length`**) · md5 `274e6b4e682445c206fa037c517254a6`. Đọc bằng `openpyxl`:

| Số đo | Giá trị |
|---|---|
| Số sheet | **1** |
| Tên sheet | **"Bài giảng"** |
| Tổng dòng không rỗng | **8** |
| Dòng tiêu đề | **1** |
| **Số dòng dữ liệu (8 − 1)** | **7** |

Bộ cột dòng tiêu đề: `Tên bài giảng · Loại tài liệu · Lĩnh vực · Dung lượng · Công khai · Người tạo · Ngày tạo · Mô tả`.

**Đối chiếu từng dòng với màn — đủ 7/7, không thiếu bản ghi nào:**

| # | Tên bài giảng trong tệp | Loại | Công khai |
|---|---|---|---|
| 1 | Test ẩn file đính kèm | PDF | Đã công khai |
| 2 | Quản lý, thanh toán và quyết toán vốn đầu tư công | Video | Đã công khai |
| 3 | Quy trình lập và quản lý kế hoạch đầu tư công… | Video | Đã công khai |
| 4 | Hướng dẫn lập, thẩm định và quản lý kế hoạch đầu tư công trung hạn… | Slide | Đã công khai |
| 5 | Cẩm nang thực hiện nghĩa vụ thuế… | PDF | Đã công khai |
| 6 | Hướng dẫn kê khai, nộp thuế và sử dụng hóa đơn điện tử… | Slide | Đã công khai |
| 7 | **Test video 2** | Video | **Chưa công khai** |

Đáng lưu ý: tệp **có cả bản ghi "Chưa công khai"** — đúng nghĩa "toàn bộ danh sách hiện có trên bảng danh sách",
không âm thầm cắt theo trạng thái công khai.

### 6.5 🔴 SỐ ĐO QUYẾT ĐỊNH

| Vế | Số đo | Kết quả |
|---|---|---|
| Tổng bản ghi màn báo | **7** (chữ chân bảng "Hiển thị 1-7 / 7 kết quả" **và** `meta.total=7` — hai nguồn khớp) | mốc so sánh |
| Số dòng dữ liệu trong tệp | **7** | **= tổng** ✅ |
| Máy chủ tự khai | `x-export-exported = 7` / `x-export-total = 7` | khớp ✅ |

### 6.6 Phép thử phân biệt "toàn bộ danh sách" vs "trang đang xem" (bẫy h — bẫy PASS-oan nguy hiểm nhất)

Vì tổng = **7** mà cỡ trang mặc định = **20**, riêng con số 7 **chưa** tự phân biệt được hai giả thuyết. Đã làm 3 phép thử:

**(a) Hạ cỡ trang xuống mức nhỏ nhất giao diện cho phép.** Mở danh sách chọn cỡ trang, đọc thật các lựa chọn:
**`10 / trang` · `20 / trang` · `50 / trang` · `100 / trang`** — **không có mức nào nhỏ hơn 7**
(khớp `srs-fr-03-dao-tao.md:1976` — *"mặc định 20 dòng/trang; cho phép 10/20/50/100"*). Đã chọn **10 / trang**
→ URL `…/danh-sach?page=1&pageSize=10`, màn vẫn hiện **7 dòng**, chân bảng vẫn **"Hiển thị 1-7 / 7 kết quả"**, chỉ 1 trang.
⇒ **Giao diện không thể tạo ra trạng thái "trang đang xem nhỏ hơn toàn bộ danh sách"** với khối dữ liệu hiện có
(muốn vậy phải thêm ≥4 bản ghi mới vào dữ liệu đối tác — **đã không làm**, xem §8).
Ảnh: `image/QLKTLBG_19-02-phan-trang-luc-xuat.png` — **đã mở ảnh ra đọc**: chân bảng ghi "Hiển thị 1-7 / 7 kết quả",
ô cỡ trang ghi "10 / trang", chỉ có số trang **1**, hai mũi tên chuyển trang đều mờ; 7 dòng dữ liệu hiện đủ; thanh lọc
phía trên vẫn trống.

**(b) Đọc hợp đồng của chức năng xuất.** `GET /api/docs-json` → `BaiGiangExportDto` có **đúng 7 thuộc tính**, toàn bộ là
trường lọc: `keyword · loaiTaiLieu · linhVucId · khoaHocId · congKhai · tuNgay · denNgay`. **Không có** bất kỳ trường
phân trang nào (`page` / `pageSize` / `limit` / `offset`). ⇒ Về mặt hợp đồng, chức năng xuất **không nhận** khái niệm
"trang", nên không thể cắt theo trang.

**(c) Thử ép phân trang xem chức năng xuất có nghe theo không** (phép đo phụ, không tạo/sửa dữ liệu):

| Gửi kèm | HTTP | `x-export-exported` | `x-export-total` | Kích thước tệp |
|---|---|---|---|---|
| `{}` (đúng thân màn gửi) | 200 | **7** | **7** | 8610 byte |
| `{"page":1,"pageSize":1}` | 200 | **7** | **7** | 8610 byte |
| `{"page":2,"pageSize":5}` | 200 | **7** | **7** | 8610 byte |

Ép cỡ trang xuống 1, hay đòi trang 2, tệp xuất **vẫn nguyên 7 bản ghi, vẫn đúng 8610 byte**.

⇒ **Kết luận phép thử phân biệt: tệp xuất bám theo TOÀN BỘ danh sách, chứng minh được là KHÔNG cắt theo trang đang xem.**
Bẫy (h) đã bị loại bằng bằng chứng trực tiếp, **không** bằng suy đoán.

**⇒ VẾ 2 (C2): ĐẠT.**

## 7. B5 — Console

`list_console_messages` (lọc error + warn): **0 lỗi**. Đúng **1 cảnh báo** duy nhất, không liên quan case:
*"Route path `/ticket=*` will be treated as if it were `/ticket=/*`…"* (cảnh báo cấu hình đường dẫn của thư viện
điều hướng, phát sinh ngay từ lúc nạp trang, không do thao tác xuất).

## 8. Điều KHÔNG làm (khai rõ)

- **Không tạo / sửa / xoá bản ghi nào** trên env đối tác. Riêng phương án "thêm bản ghi QA cho tới khi tổng > cỡ trang"
  ở chuẩn chấm §6 T4(b) **đã cân nhắc và KHÔNG dùng**, vì phép thử §6.6(b)+(c) đã phân biệt được dứt điểm mà không cần
  đụng dữ liệu đối tác.
- **Không đổi tài khoản, không đăng xuất, không đăng nhập lại** (giữ nguyên phiên `cbnv_tw`).
- **Không đổi vai trò để "cho ra nút"** (bẫy g) — không cần, vì vai trò CB NV đã thấy và bấm được nút.
- Bấm nút **Xuất Excel trên giao diện đúng 1 lần**; 2 lời gọi ở §6.6(c) là phép đo phụ ở tầng dịch vụ để phân biệt
  giả thuyết cắt-theo-trang, không phải bấm lại nút để chụp lại thông báo.

## 9. Đối chiếu bảng chuẩn chấm

| Vế | Nội dung | Đặc tả (mở file đọc số dòng thật) | Số đo | Kết quả |
|---|---|---|---|---|
| **C1** | Màn Kho tài liệu / Bài giảng phải có chức năng Xuất Excel và bấm được | `srs-fr-03-dao-tao.md:1952` — *"Nút \"Xuất Excel\" (phụ): xuất danh sách theo bộ lọc hiện tại, tối đa 10.000 dòng (BR-DATA-06)"* · `srs-v3.5.md:5570` — BR-DATA-06, Áp dụng FR *"Toàn bộ CRUD list"* | Có nút ở thanh công cụ (đã liệt kê DOM 35 phần tử), bấm 1 lần → `POST /api/v1/bai-giangs/export` **HTTP 200** + tệp .xlsx 8610 byte + thông báo "Xuất dữ liệu thành công." | **ĐẠT** |
| **C2** | Không đặt lọc ⇒ tệp chứa **toàn bộ** danh sách, không chỉ trang đang xem | `srs-fr-03-dao-tao.md:1952` + `srs-v3.5.md:5570` — giới hạn duy nhất là **10.000 dòng**, đặc tả không đặt giới hạn theo cỡ trang · `srs-fr-03-dao-tao.md:1976` — phân trang 10/20/50/100 | Tổng màn báo **7** (2 nguồn khớp) — tệp có **7 dòng dữ liệu** (8 dòng − 1 tiêu đề), đủ 7/7 bản ghi kể cả bản "Chưa công khai"; ép `pageSize=1` vẫn xuất 7 | **ĐẠT** |

**Câu trích đặc tả đã tự mở file xác minh số dòng** (`Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/`):

- `srs-fr-03-dao-tao.md:751` — `**Tác nhân:** CB NV / CB PD`
- `srs-fr-03-dao-tao.md:1952` — `- Nút "Xuất Excel" (phụ): xuất danh sách theo bộ lọc hiện tại, tối đa 10.000 dòng (BR-DATA-06)`
- `srs-fr-03-dao-tao.md:1976` — `**Thành phần 5 — Phân trang:** mặc định 20 dòng/trang; cho phép 10/20/50/100.`
- `srs-v3.5.md:5570` — `| BR-DATA-06 | **Export Excel:** Mọi danh sách có tính năng xuất Excel. File xuất theo bộ lọc hiện tại, không vượt quá 10,000 rows/file | … | Toàn bộ CRUD list | … |`

## 10. VERDICT

# ✅ PASS

Cả hai vế đều **ĐẠT**, đo trực tiếp trên env nghiệm thu đối tác, bản dựng **V1.0.10**:
màn hình **đã có** chức năng Xuất Excel (triệu chứng cũ *"Màn hình không có nút chức năng"* **không còn tái hiện**),
bấm ra tệp thật, và **nội dung tệp chứa đủ toàn bộ 7/7 bản ghi** của danh sách không lọc — đã qua phép thử phân biệt
cắt-theo-trang.

**Phạm vi hiệu lực:** `https://htpldn-uat.ospgroup.vn` · bản dựng **V1.0.10** (bó mã `index-Bd1akG3f.js`) ·
tài khoản `cbnv_tw` (CB_NV_TW, cấp TW) · **2026-08-07 16:46–16:52** · khối dữ liệu 7 bài giảng thuộc đơn vị TW.

## 11. Ảnh bằng chứng

| Tệp | Nội dung | Đã mở đọc |
|---|---|---|
| `image/QLKTLBG_19-01-man-danh-sach-khong-loc.png` | Màn danh sách, thanh lọc trống, 3 nút thanh công cụ gồm **Xuất Excel**, bản dựng V1.0.10 | ✅ |
| `image/QLKTLBG_19-02-phan-trang-luc-xuat.png` | Chân bảng lúc xuất: "Hiển thị 1-7 / 7 kết quả", cỡ trang 10/trang, 1 trang | ✅ |

Tệp xuất giữ lại để truy lại: `/Users/huongttt/Downloads/DanhSachBaiGiang_20260807_1649.xlsx` (md5 `274e6b4e682445c206fa037c517254a6`).

## 12. Ghi nhận NGOÀI phạm vi case (không tự thêm dòng sheet — báo lead)

1. **Bảng §6 của `srs-fr-03-dao-tao.md:2243`** liệt kê BR-DATA-06 cho `FR-III-01, FR-III-05, FR-III-06, FR-III-14`,
   **thiếu FR-III-07 / FR-III-08** trong khi đặc tả cấp màn `:1952` quy định màn này có nút Xuất Excel.
   Đây là **điểm cần chỉnh ở tài liệu**, không phải lỗi phần mềm (đã ghi sẵn trong chuẩn chấm §4).
2. **Hệ thống không tồn tại quyền `export_bai_giang`** trong bộ quyền, trong khi các danh sách khác đều có quyền xuất
   riêng (`export_vu_viec`, `export_doanh_nghiep`, `export_tu_van_vien`…). Lời gọi xuất bài giảng vẫn trả 200 —
   tức chức năng chạy được nhưng **không được kiểm soát bởi một quyền xuất riêng** như các danh sách còn lại.
   Ghi nhận để lead cân nhắc, **không thuộc phạm vi case 19**.
3. Quan sát ở khảo sát về bộ lọc **"Công khai"** (`congKhai`) thuộc phạm vi **QLKTLBG_18** — case này không đặt lọc nên
   không đo; nhường người đo case 18.
