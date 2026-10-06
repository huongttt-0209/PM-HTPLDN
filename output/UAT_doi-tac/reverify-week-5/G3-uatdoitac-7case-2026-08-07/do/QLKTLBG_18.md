# NHẬT KÝ ĐO — QLKTLBG_18 (dòng 12) · Lô G3 · env nghiệm thu đối tác

> Chuẩn chấm khoá trước khi đo: [`chuan/QLKTLBG_18.md`](../chuan/QLKTLBG_18.md). Đo xong **không sửa** chuẩn.

## 1. Bảng đầu

| Mục | Giá trị |
|---|---|
| Mã TC / dòng | **QLKTLBG_18** · dòng **12** · "Xuất Excel với điều kiện lọc" |
| Env | **`https://htpldn-uat.ospgroup.vn`** (env NGHIỆM THU của đối tác) |
| **Bản dựng đọc trên UI** | **`HTPLDN · V1.0.10`** (chân khối logo sidebar) — đọc **sau** khi tải lại trang bỏ qua bộ nhớ đệm |
| Bó mã FE | `assets/index-Bd1akG3f.js` (đọc từ `script[src]` của trang sau khi tải lại) |
| Ngày giờ đo | **2026-08-07**, 17:00–17:12 giờ VN (10:00–10:12 UTC) |
| Tài khoản | **`cbnv_tw`** — `hoTen` "Cán bộ NV Trung ương", `vaiTro=["CB_NV_TW"]`, `capDonVi=TW`, `donViId=00000000-0000-4000-8000-000000000001` (Cục Bổ trợ tư pháp - BTP) — đọc thật từ `GET /api/v1/auth/me` HTTP 200 |
| Vai trò theo đặc tả | `srs-fr-03-dao-tao.md:751` — *"**Tác nhân:** CB NV / CB PD"* (FR-III-07) · `:828` (FR-III-08, cùng câu). Tài khoản đo đúng vai trò CB NV |
| Màn | Đào tạo, tập huấn → Kho tài liệu / Bài giảng → Danh sách (**SCR-III-03**) |
| URL đạt được | `https://htpldn-uat.ospgroup.vn/dao-tao/bai-giang/danh-sach` |
| **Không đăng nhập lại** | Dùng đúng phiên sẵn có; không đăng xuất, không tốn lượt đăng nhập nào (giới hạn 5 lượt/60s) |
| Không đụng dữ liệu đối tác | Chỉ xem, lọc và xuất. **Không tạo / sửa / xoá bản ghi nào** |

## 2. Mô tả ảnh bằng chứng của đối tác (đã mở ra xem trong lượt này)

`output/UAT_doi-tac/flowtest-2026-08-05/partner-evidence/QLKTLBG_18.jpg` — **đã mở đọc**, mô tả nguyên trạng:

- Thanh địa chỉ: `htpldn-uat.ospgroup.vn/dao-tao/bai-giang/danh-sach` → đúng env đối tác, đúng màn SCR-III-03.
- Sidebar ghi bản dựng **`HTPLDN · V1.0`**; đồng hồ hệ điều hành **08:51 ngày 2026-07-25**.
- Người đăng nhập: **"Cán bộ NV Trung ương · CB_NV_TW"** → đúng vai trò đặc tả.
- Vùng tiêu đề *"Kho tài liệu / Bài giảng"* chỉ có **2 nút**: **`+ Thêm mới`** (xanh) và **`Làm mới`**.
  **Không có nút "Xuất Excel"** — khớp câu TKM *"Màn hình không có nút chức năng"*.
- Thanh lọc: ô *"Tìm theo tên bài giảng"*, `Loại tài liệu`, `Lĩnh vực pháp lý`, `Công khai`, chip
  **`Bộ lọc nâng cao (2)`**, nút `Xóa bộ lọc` + `Tìm kiếm`.
- Bảng có dữ liệu (Video / PDF / Slide), các cột Dung lượng · Ngày tạo · Công khai · Thao tác (3 biểu tượng).
  Bảng đang cuộn ngang nên cột "Tên bài giảng" nằm ngoài khung hình.

**Ảnh chứng minh gì:** tại bản dựng `V1.0` ngày 25/07/2026 màn này **không** có nút Xuất Excel.
**Ảnh KHÔNG chứng minh gì:** không nói gì về bản dựng hiện tại ⇒ vẫn phải đo lại thật (đã làm ở §3–§8).

## 3. B0 — Tải lại trang, đọc lại bản dựng

`navigate_page type=reload ignoreCache=true`, rồi đọc lại trang:

- Chữ hiển thị trên UI: **`HTPLDN · V1.0.10`**
- `script[src]` duy nhất: `/assets/index-Bd1akG3f.js`
- `GET /api/v1/auth/me` → **HTTP 200**, `vaiTro=["CB_NV_TW"]`, `capDonVi="TW"` (phiên còn sống, không cần đăng nhập lại)

## 4. B1 — Điều hướng theo đúng bước 1 của phiếu

Bấm menu sidebar **"Đào tạo, tập huấn" → "Kho tài liệu / Bài giảng"**.

- **URL thực tế đạt được:** `https://htpldn-uat.ospgroup.vn/dao-tao/bai-giang/danh-sach`
- Dải điều hướng: Trang chủ / Đào tạo, tập huấn / Kho tài liệu / Bài giảng / Danh sách
- Tiêu đề màn: **"Kho tài liệu / Bài giảng"**

## 5. B2 — Mốc đối chứng: tổng bản ghi khi CHƯA lọc

| Nguồn | Giá trị |
|---|---|
| Chữ vùng phân trang (`innerText`) | **"Hiển thị 1-7 / 7 kết quả"** |
| Thân phản hồi danh sách `GET /api/v1/bai-giangs?page=1&pageSize=20` (HTTP 200) | `meta` = `{"page":1,"pageSize":20,"total":7,"totalPages":1}` → **`total` = 7** |
| Đếm tay số dòng trên bảng | **7** |

**Ba nguồn khớp → mốc chưa lọc = 7.** Chuỗi truy vấn chỉ có `page` + `pageSize`, không kèm tham số lọc nào.

7 bản ghi (đọc từ thân phản hồi): 2 PDF · 3 VIDEO · 2 SLIDE; 6 bản `congKhai=true`, 1 bản
`congKhai=false` ("Test video 2").

## 6. B3 — Nhập tiêu chí lọc trên GIAO DIỆN (không ép qua dịch vụ)

**Nhãn thật trên màn:** ô lọc thứ 2 là **"Loại tài liệu"**, các lựa chọn đọc thật trong danh sách xổ:
**`PDF` · `Slide` · `Video`** (đúng nhóm giá trị `:1956`, khác chỗ đặc tả có thêm mục "Tất cả" — xem §11).

Thao tác: chọn **Loại tài liệu = PDF** → bấm **"Tìm kiếm"**.

### 6.1 Xác nhận bộ lọc ĐÃ THỰC SỰ ÁP — 3 chiều độc lập

| Chiều | Số đo |
|---|---|
| (1) Truy vấn màn gửi lên máy chủ (`list_network_requests`) | `GET /api/v1/bai-giangs?loaiTaiLieu=PDF&page=1&pageSize=20` → **HTTP 200**. Có tham số lọc `loaiTaiLieu=PDF` |
| (2) Tổng ở chân bảng | đổi **"Hiển thị 1-7 / 7 kết quả"** → **"Hiển thị 1-2 / 2 kết quả"**; thân phản hồi `meta.total` đổi **7 → 2** |
| (3) Đếm tay số dòng trên bảng | **2** |

URL màn cũng đổi thành `…/danh-sach?loaiTaiLieu=PDF&page=1`.

### 6.2 ⚠️ Bẫy chip "Bộ lọc nâng cao (2)" — đã kiểm, KHÔNG phải bộ lọc đang áp

Chip **"Bộ lọc nâng cao (2)"** hiện sẵn ngay khi vào màn (y như ảnh đối tác). Đã mở khối ra đọc:
bên trong đúng **2 ô** — **"Từ ngày"** và **"Đến ngày"**, **cả hai `value` đều rỗng**. ⇒ Con số `(2)` là
**số ô lọc nâng cao có trong khung**, **không** có nghĩa "đang áp 2 điều kiện". Chuỗi truy vấn ở §6.1
xác nhận: không có `tuNgay` / `denNgay` nào được gửi đi.

## 7. B4 — VẾ 1: màn hình có chức năng Xuất Excel hay không

**Không kết luận bằng mắt.** Đã liệt kê toàn bộ `button` / `a` / `[role=button]` trong vùng nội dung
(**18 phần tử**), đọc đủ `innerText` + `title` + `aria-label` + `className` + tên biểu tượng + `disabled` + toạ độ.

### 7.1 Vùng tiêu đề + thanh công cụ (ngoài bảng)

| # | Thẻ | `innerText` | `title` | `aria-label` | Biểu tượng | `disabled` | Toạ độ |
|---|---|---|---|---|---|---|---|
| 1 | BUTTON | **Thêm mới** | null | null | `anticon-plus` | false | (1040, 80) |
| 2 | **BUTTON** | **Xuất Excel** | null | null | **`anticon-download`** | **false** | **(1169, 80)** |
| 3 | BUTTON | Làm mới | null | null | `anticon-reload` | false | (1304, 80) |
| 4 | BUTTON | *(rỗng)* | null | null | `anticon-close-circle` | false | nút xoá chữ của ô từ khoá (đang ẩn) |
| 5 | BUTTON | Bộ lọc nâng cao (2) | null | null | `anticon-down` | false | (1236, 145) |
| 6 | BUTTON | Xóa bộ lọc | null | null | `anticon-clear` | false | (1152, 181) |
| 7 | BUTTON | Tìm kiếm | null | null | `anticon-search` | false | (1288, 181) |
| 8–10 | BUTTON / A | *(phân trang)* | — | — | `anticon-left` · `1` · `anticon-right` | 2 mũi tên `disabled` | chân bảng |

**Không có menu phụ nào ở thanh công cụ** — truy vấn `.ant-dropdown-trigger, [aria-haspopup="menu"]`
trong vùng nội dung trả về **mảng rỗng**. 3 nút hành động đều phơi thẳng, không giấu trong menu.

### 7.2 ⚠️ Phân biệt với biểu tượng cột "Thao tác" (bẫy c)

Trong thân bảng, **mỗi dòng** có nhóm nút chỉ-biểu-tượng ở cột **"Thao tác"**: `anticon-eye` (Xem trực tuyến) ·
`anticon-download` (**Tải về** — chỉ dòng Slide/PDF) · `anticon-edit` (Sửa) · `anticon-delete` (Xoá).
Đây là thao tác trên **một bài giảng**, khớp `srs-fr-03-dao-tao.md:1974`
(*"Hành động | — | Xem trực tuyến · Tải về (chỉ Slide/PDF) · Sửa · Xóa"*). Vế 1 chấm ở **thanh công cụ đầu màn**
(nằm ngoài `.ant-table`, có nhãn chữ, toạ độ y=80), và ở đó **có** nút "Xuất Excel" riêng biệt.

### 7.3 Ảnh đã chụp và đã mở đọc

`image/QLKTLBG_18-01-man-da-ap-bo-loc.png` — **đã mở ảnh ra đọc**. Nhìn thấy: sidebar ghi `HTPLDN · V1.0.10`;
vùng tiêu đề "Kho tài liệu / Bài giảng" kèm **3 nút `+ Thêm mới` · `Xuất Excel` · `Làm mới`**; ô "Loại tài liệu"
hiển thị giá trị **PDF**, các ô lọc còn lại trống; chip `Bộ lọc nâng cao (2)`; bảng **2 dòng, cả hai nhãn PDF**;
chân bảng **"Hiển thị 1-2 / 2 kết quả"**, cỡ trang `20 / trang`, chỉ 1 trang.

**⇒ VẾ 1 (B1): ĐẠT** — triệu chứng cũ *"Màn hình không có nút chức năng"* **không còn tái hiện** trên bản dựng V1.0.10.

## 8. B5 — VẾ 2: bấm xuất và kiểm NỘI DUNG tệp

### 8.1 Bộ bắt thông báo

Cài **đúng `output/UAT_doi-tac/tools/toast-capture.js`** (đọc nguyên file, tiêm qua `evaluate_script`) **TRƯỚC** khi bấm.
Không tự viết bộ đo, **không lọc trùng**, đọc chữ bằng `innerText`.
**Tự kiểm số observer trước mỗi lần bấm:** `soObserverDangSong = 1` cả 3 lần → số liệu hợp lệ.

### 8.2 Lần đo 1 — bộ lọc **Loại tài liệu = PDF**

| Số đo | Giá trị |
|---|---|
| Số lần bấm "Xuất Excel" | **1** |
| **Số khung thông báo bắt được** | **1** |
| Nguyên văn thông báo | **"Xuất dữ liệu thành công."** |
| Bị lặp thông báo | **Không** (`BI_LAP=false`) |
| **Số request phát sinh (khác GET)** | **1** — `POST /api/v1/bai-giangs/export` |

**Mã HTTP + thân yêu cầu THẬT màn gửi đi:**

```
POST /api/v1/bai-giangs/export   →   HTTP 200
Thân yêu cầu: {"loaiTaiLieu":"PDF"}          (content-length: 21)
```

⇒ Thân yêu cầu **mang đúng tiêu chí lọc đang áp trên màn** — đây là bằng chứng "xuất theo bộ lọc hiện tại".

Tiêu đề phản hồi:

| Tiêu đề | Giá trị |
|---|---|
| `content-type` | `application/vnd.openxmlformats-officedocument.spreadsheetml.sheet` |
| `content-disposition` | `attachment; filename="DanhSachBaiGiang_20260807_1704.xlsx"` |
| `content-length` | **7340** |
| **`x-export-exported`** | **2** |
| **`x-export-total`** | **2** |

**MỞ TỆP RA ĐỌC** — tệp rơi về `~/Downloads`: `/Users/huongttt/Downloads/DanhSachBaiGiang_20260807_1704.xlsx`
· 7340 byte (**khớp đúng `content-length`**) · md5 `807f29165002ca783b533b1e50eee5dd`. Đọc bằng `openpyxl`:

| Số đo | Giá trị |
|---|---|
| Số sheet | **1** |
| Tên sheet | **"Bài giảng"** |
| Tổng dòng không rỗng | **3** |
| Dòng tiêu đề | **1** |
| **Số dòng dữ liệu (3 − 1)** | **2** |

Bộ cột dòng tiêu đề: `Tên bài giảng · Loại tài liệu · Lĩnh vực · Dung lượng · Công khai · Người tạo · Ngày tạo · Mô tả`.

**Đối chiếu TỪNG TÊN bài giảng trong tệp với TỪNG DÒNG trên bảng đã lọc — trùng khít 2/2, không thừa không thiếu:**

| # | Tên trên bảng (đã lọc PDF) | Tên trong tệp | Cột "Loại tài liệu" trong tệp |
|---|---|---|---|
| 1 | Test ẩn file đính kèm | Test ẩn file đính kèm | PDF ✅ |
| 2 | Cẩm nang thực hiện nghĩa vụ thuế đối với hộ kinh doanh và cá nhân kinh doanh | (giống hệt) | PDF ✅ |

### 8.3 Lần đo 2 — phép thử đối chứng bắt buộc, bộ lọc **Loại tài liệu = Video**

Đổi tiêu chí lọc trên giao diện sang **Video** → bấm **Tìm kiếm**.

| Chiều xác nhận | Số đo |
|---|---|
| Truy vấn màn gửi | `GET /api/v1/bai-giangs?loaiTaiLieu=VIDEO&page=1&pageSize=20` → HTTP 200 |
| Chân bảng | **"Hiển thị 1-3 / 3 kết quả"** |
| Đếm tay | **3** dòng, cả 3 nhãn "Video" |

Bấm **Xuất Excel** 1 lần: **1 request · 1 thông báo** ("Xuất dữ liệu thành công.") · `BI_LAP=false`.

```
POST /api/v1/bai-giangs/export   →   HTTP 200
Thân yêu cầu: {"loaiTaiLieu":"VIDEO"}        (content-length: 23)
content-disposition: attachment; filename="DanhSachBaiGiang_20260807_1706.xlsx"
content-length: 7664 · x-export-exported: 3 · x-export-total: 3
```

**MỞ TỆP RA ĐỌC** — `/Users/huongttt/Downloads/DanhSachBaiGiang_20260807_1706.xlsx` · 7664 byte
(khớp `content-length`) · md5 `038ef491f54396da7546448c4b279742` · 1 sheet "Bài giảng" ·
**4 dòng không rỗng − 1 tiêu đề = 3 dòng dữ liệu**, cả 3 cột "Loại tài liệu" đều **Video**:

| # | Tên trên bảng (đã lọc Video) | Trong tệp | Công khai |
|---|---|---|---|
| 1 | Quản lý, thanh toán và quyết toán vốn đầu tư công | ✅ | Đã công khai |
| 2 | Quy trình lập và quản lý kế hoạch đầu tư công theo quy định hiện hành | ✅ | Đã công khai |
| 3 | **Test video 2** | ✅ | **Chưa công khai** |

Ảnh: `image/QLKTLBG_18-03-doi-chung-loc-video.png` — **đã mở ảnh ra đọc**: ô "Loại tài liệu" hiển thị **Video**,
bảng 3 dòng đều nhãn Video (dòng 3 là "Test video 2"), chân bảng **"Hiển thị 1-3 / 3 kết quả"**, nút "Xuất Excel"
đang ở trạng thái vừa bấm (viền xanh).

### 8.4 🔴 SỐ ĐO QUYẾT ĐỊNH — hai lần lọc khác số nhau

| Lần đo | Tiêu chí lọc | Tổng chưa lọc | Tổng màn báo sau lọc | Số dòng dữ liệu trong tệp | Máy chủ tự khai | Kết luận |
|---|---|---|---|---|---|---|
| 1 | Loại tài liệu = **PDF** | 7 | **2** (chân bảng + `meta.total` + đếm tay, cả 3 khớp) | **2** | `x-export-exported=2` / `x-export-total=2` | **= tổng sau lọc, ≠ 7** ✅ |
| 2 | Loại tài liệu = **Video** | 7 | **3** (3 nguồn khớp) | **3** | `3` / `3` | **= tổng sau lọc, ≠ 7, ≠ 2** ✅ |

⇒ Hai phép đo cho **hai con số khác nhau và đều bám đúng bộ lọc** ⇒ loại được giả thuyết "trùng hợp"
và loại được ca PASS-oan nguy hiểm nhất (tệp chứa toàn bộ 7 bản ghi, bỏ qua bộ lọc).
Cũng loại được ca "tệp chỉ chứa trang đang xem": cỡ trang là 20, cả hai tập lọc đều < 20 nên
tệp không thể bị cắt theo trang; ngoài ra `BaiGiangExportDto` không có trường phân trang nào.

**⇒ VẾ 2 (B2) — với tiêu chí "Loại tài liệu": ĐẠT.**

### 8.5 Ảnh chân bảng lúc bấm xuất

`image/QLKTLBG_18-02-chan-bang-sau-loc.png` — **đã mở ảnh ra đọc**: chụp ngay sau cú bấm "Xuất Excel"
của lần đo 1. Nhìn thấy nút **"Xuất Excel"** đang ở trạng thái vừa bấm (viền xanh), ô "Loại tài liệu" = **PDF**,
bảng 2 dòng PDF, chân bảng **"Hiển thị 1-2 / 2 kết quả"**, cỡ trang `20 / trang`, 1 trang.

## 9. B6 — Console

`list_console_messages` (lọc error + warn): **0 lỗi**. Đúng **1 cảnh báo** duy nhất, không liên quan case:
*"Route path `/ticket=*` will be treated as if it were `/ticket=/*`…"* (cảnh báo cấu hình đường dẫn của thư viện
điều hướng, phát sinh từ lúc nạp trang, không do thao tác lọc/xuất).

## 10. 🔴 B7 — Kiểm ô lọc "Công khai" (thuộc phạm vi case vì `congKhai` là một tiêu chí lọc)

### 10.1 Màn hình CÓ ô lọc "Công khai"

Có. Ô lọc thứ 4 trên thanh lọc, `input#congKhai`. Danh sách xổ đọc thật có **2 lựa chọn**:
**"Công khai"** và **"Không công khai"** (đặc tả `:1958` ghi *"Tất cả / Đã công khai / Chưa công khai"* —
chênh câu chữ, xem §11).

⇒ Theo phiếu giao việc, nhánh **"Có"** áp dụng: phải thử **cả 2 giá trị** và kiểm kết quả trên bảng.

### 10.2 Dữ liệu nền (đọc từ thân phản hồi danh sách chưa lọc)

Tổng 7 bản ghi = **6 bản `congKhai=true`** + **1 bản `congKhai=false`** — bản đó là **"Test video 2"**,
badge trên bảng ghi **"Chưa công khai"**.

### 10.3 Kết quả thử 2 giá trị

| Giá trị chọn trên màn | Truy vấn màn gửi | Chân bảng | Đếm tay | Badge cột "Công khai" của mọi dòng | Đúng/Sai |
|---|---|---|---|---|---|
| **"Công khai"** | `GET /api/v1/bai-giangs?congKhai=true&page=1&pageSize=20` → 200, `meta.total` = **6** | "Hiển thị 1-6 / 6 kết quả" | 6 | tất cả **"Đã công khai"** | **Đúng** |
| **"Không công khai"** | `GET /api/v1/bai-giangs?congKhai=false&page=1&pageSize=20` → 200, `meta.total=`**6** | "Hiển thị 1-6 / 6 kết quả" | 6 | tất cả **"Đã công khai"** | 🔴 **SAI** |

Với lựa chọn **"Không công khai"**, danh sách trả về **đúng 6 bản ghi giống hệt** lựa chọn "Công khai" —
**mọi bản ghi đều đang "Đã công khai"**, còn bản ghi **duy nhất** thực sự "Chưa công khai" ("Test video 2")
**không xuất hiện**. Đã đọc `congKhai` của cả 6 bản trong thân phản hồi: **cả 6 đều `true`**.

**Kiểm chéo để loại giả thuyết "bản ghi bị ẩn khỏi màn":** cũng bản ghi "Test video 2" đó **hiện bình thường**
khi lọc Loại tài liệu = Video (§8.3) và khi không lọc (§5) ⇒ bản ghi không bị ẩn; **chỉ riêng tiêu chí
"Công khai" trả sai tập kết quả**.

### 10.4 🔴 Ảnh hưởng THẲNG tới vế "xuất Excel theo điều kiện lọc"

Giữ nguyên bộ lọc **"Không công khai"** rồi bấm **Xuất Excel** (1 lần · 1 request · 1 thông báo
"Xuất dữ liệu thành công." · `BI_LAP=false`):

```
POST /api/v1/bai-giangs/export   →   HTTP 200
Thân yêu cầu: {"congKhai":"false"}           (content-length: 20)
content-disposition: attachment; filename="DanhSachBaiGiang_20260807_1709.xlsx"
content-length: 8492 · x-export-exported: 6 · x-export-total: 6
```

**MỞ TỆP RA ĐỌC** — `/Users/huongttt/Downloads/DanhSachBaiGiang_20260807_1709.xlsx` · 8492 byte
(khớp `content-length`) · md5 `28efd26a5c96990d8def47422d222956` · 1 sheet "Bài giảng" ·
**7 dòng không rỗng − 1 tiêu đề = 6 dòng dữ liệu**:

| # | Tên bài giảng trong tệp | Cột "Công khai" trong tệp |
|---|---|---|
| 1 | Test ẩn file đính kèm | **Đã công khai** |
| 2 | Quản lý, thanh toán và quyết toán vốn đầu tư công | **Đã công khai** |
| 3 | Quy trình lập và quản lý kế hoạch đầu tư công… | **Đã công khai** |
| 4 | Hướng dẫn lập, thẩm định và quản lý kế hoạch đầu tư công trung hạn… | **Đã công khai** |
| 5 | Cẩm nang thực hiện nghĩa vụ thuế… | **Đã công khai** |
| 6 | Hướng dẫn kê khai, nộp thuế và sử dụng hóa đơn điện tử… | **Đã công khai** |
| — | *(thiếu)* **Test video 2** — bản duy nhất "Chưa công khai" | **không có trong tệp** |

**SỐ ĐO QUYẾT ĐỊNH của vế này:** điều kiện lọc đang đặt trên màn là **"Không công khai"**, tệp xuất ra
**6/6 dòng đều "Đã công khai"** — tức **0/6 dòng khớp điều kiện lọc**, và bản ghi duy nhất khớp điều kiện
thì **vắng mặt**. Đối chiếu chuẩn chấm §4 B2 (*"Reopen khi… tệp chứa dòng **không khớp** tiêu chí lọc"*)
⇒ **B2 KHÔNG ĐẠT với tiêu chí "Công khai"**.

Ảnh:
- `image/QLKTLBG_18-04-loc-khong-cong-khai-sai.png` — **đã mở ảnh ra đọc**: chụp ngay sau cú bấm
  "Xuất Excel"; ô lọc thứ 4 hiển thị **"Không công khai"**, các ô lọc khác trống, bảng **6 dòng**,
  chân bảng **"Hiển thị 1-6 / 6 kết quả"**.
- `image/QLKTLBG_18-05-cot-cong-khai-nguoc-bo-loc.png` — **đã mở ảnh ra đọc**: cùng trạng thái đó nhưng
  bảng đã cuộn ngang để lộ cột **"Công khai"** — ô lọc ghi **"Không công khai"** trong khi **cả 6 dòng**
  đều mang badge xanh **"Đã công khai"**; chân bảng "Hiển thị 1-6 / 6 kết quả".

### 10.5 Đối chiếu đặc tả cho vế này (đã mở file đọc số dòng thật)

- `srs-fr-03-dao-tao.md:844` (FR-III-08, Inputs bộ lọc, dòng 5):
  `| 5 | cong_khai | select | N | **[STT66 UAT 2026-06-02]** Lọc trạng thái công khai: Tất cả / Đã công khai (`cong_khai=1`) / Chưa công khai (`cong_khai=0`) |`
- `srs-fr-03-dao-tao.md:874` (FR-III-08, Acceptance Criteria):
  `- **[STT66 UAT 2026-06-02] Given** CB NV lọc theo trạng thái Công khai (Đã/Chưa công khai) **When** chọn **Then** danh sách lọc tương ứng; cột "Công khai" hiển thị badge cho từng bản ghi`
- `srs-fr-03-dao-tao.md:1958` (SCR-III-03, Thành phần 3):
  `- Lọc Công khai: Tất cả / Đã công khai / Chưa công khai [STT66 UAT 2026-06-02]`
- `srs-fr-03-dao-tao.md:1971` (SCR-III-03, cột 6 của bảng):
  `| Công khai | cong_khai | **Badge** "Đã công khai" / "Chưa công khai" — chỉ hiển thị, **không** bật tắt tại dòng …`
- `srs-fr-03-dao-tao.md:1952` + `srs-v3.5.md:5570` — tệp xuất phải *"theo bộ lọc hiện tại"* (trích ở §12).

⇒ Đặc tả **có** quy định rõ tiêu chí lọc này và **có** AC riêng cho nó. Không phải chỗ SRS im lặng.

### 10.6 Đã tra tracker mâu thuẫn đặc tả trước khi kết luận

`tasks/srs-contradictions.md` — **không có** entry nào về bài giảng / bộ lọc Công khai đang mở
⇒ không phải ca "chờ BA chốt", chấm theo đặc tả bình thường.

## 11. Ghi nhận PHỤ (candidate, KHÔNG dùng để chấm verdict)

1. **Câu chữ lựa chọn ô lọc "Công khai" lệch đặc tả.** Màn có 2 lựa chọn **"Công khai" / "Không công khai"**;
   đặc tả `:1958` ghi **"Tất cả / Đã công khai / Chưa công khai"**, và badge trên bảng (`:1971`) dùng đúng
   "Đã công khai" / "Chưa công khai". Ghi 1 dòng candidate, **không mở rộng case**.
2. **Ô lọc "Loại tài liệu" không có mục "Tất cả"** (chỉ PDF / Slide / Video); đặc tả `:1956` ghi
   *"Tất cả / Slide / PDF / Video"*. Trên màn, việc "bỏ lọc" làm bằng nút xoá (×) của ô hoặc nút "Xóa bộ lọc".
   Candidate, không thuộc vế đo.
3. **Nút "Làm mới" thừa so với đặc tả** `:1949–1952` (khối này chỉ liệt kê "+ Thêm mới" và "Xuất Excel").
   Đã ghi trong chuẩn chấm §4; candidate, không thuộc phạm vi phiếu.
4. **Bảng §6 tại `srs-fr-03-dao-tao.md:2243`** liệt kê BR-DATA-06 cho `FR-III-01, FR-III-05, FR-III-06, FR-III-14`,
   **thiếu FR-III-07 / FR-III-08** trong khi đặc tả cấp màn `:1952` quy định màn này có nút Xuất Excel.
   Điểm cần chỉnh ở **tài liệu**, không phải lỗi phần mềm (đã ghi sẵn trong chuẩn chấm §4).

## 12. Đối chiếu bảng chuẩn chấm

**Câu trích đặc tả — đã tự mở file xác minh số dòng** (`Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/`):

- `srs-fr-03-dao-tao.md:751` — `**Tác nhân:** CB NV / CB PD`
- `srs-fr-03-dao-tao.md:1952` — `- Nút "Xuất Excel" (phụ): xuất danh sách theo bộ lọc hiện tại, tối đa 10.000 dòng (BR-DATA-06)`
- `srs-fr-03-dao-tao.md:1976` — `**Thành phần 5 — Phân trang:** mặc định 20 dòng/trang; cho phép 10/20/50/100.`
- `srs-v3.5.md:5570` — `| BR-DATA-06 | **Export Excel:** Mọi danh sách có tính năng xuất Excel. File xuất theo bộ lọc hiện tại, không vượt quá 10,000 rows/file | Pattern IP-01 | Toàn bộ CRUD list | Báo cáo nhóm IX có xuất PDF theo khung TT 17/2025 | Test export limit |`
- `srs-fr-03-dao-tao.md:844` · `:874` · `:1958` · `:1971` — trích nguyên văn ở §10.5

| Vế | Nội dung | Số đo | Kết quả |
|---|---|---|---|
| **B1** | Màn Kho tài liệu / Bài giảng phải có chức năng Xuất Excel và bấm được | Đã liệt kê 18 phần tử DOM + kiểm menu phụ (rỗng): có nút "Xuất Excel" ở thanh công cụ (1169, 80), `disabled=false`. Bấm 3 lần trong lượt đo, **cả 3 lần đều HTTP 200** + sinh tệp .xlsx thật + 1 thông báo "Xuất dữ liệu thành công.", không lặp | **ĐẠT** |
| **B2** | Tệp xuất phải theo đúng điều kiện lọc đang áp: chỉ chứa bản ghi khớp bộ lọc, và chứa đủ mọi bản ghi khớp | **Tiêu chí "Loại tài liệu": ĐẠT** — PDF: màn 2 / tệp 2 dòng, 2/2 khớp tên · Video: màn 3 / tệp 3 dòng, 3/3 khớp tên; hai số khác nhau và đều ≠ 7.<br>🔴 **Tiêu chí "Công khai": KHÔNG ĐẠT** — lọc "Không công khai": màn 6 dòng đều "Đã công khai", tệp **6/6 dòng đều "Đã công khai"** (0/6 khớp điều kiện), thiếu bản ghi duy nhất "Chưa công khai" | **KHÔNG ĐẠT** (một phần) |

Đối chiếu **bảng quyết định đã cam kết TRƯỚC khi đo** (chuẩn chấm §9), dòng:
*"Có chức năng; tệp chứa toàn bộ danh sách / **có dòng không khớp tiêu chí lọc** → **Reopen** (B2 không đạt —
vi phạm 'theo bộ lọc hiện tại', `:1952` + `srs-v3.5.md:5570`)"*.
Cộng luật BRIEF §4.8 — **Fix một phần = Reopen**.

## 13. VERDICT

# ❌ REOPEN

**Vế đã sửa xong:** màn hình **đã có** chức năng Xuất Excel (triệu chứng cũ *"Màn hình không có nút chức năng"*
không còn tái hiện), bấm ra tệp thật, và với tiêu chí **Loại tài liệu** thì tệp bám đúng bộ lọc — đã chứng minh
bằng **hai** phép đo cho **hai** con số khác nhau (2 và 3, đều khác tổng chưa lọc 7).

**Vế còn lỗi:** với tiêu chí lọc **"Công khai"**, cả danh sách trên màn lẫn tệp Excel xuất ra **không tuân theo
điều kiện đã chọn**: chọn "Không công khai" nhưng nhận về 6 bản ghi **đều đang "Đã công khai"** (0/6 khớp),
còn bản ghi duy nhất thực sự "Chưa công khai" thì **không có mặt** — trái `srs-fr-03-dao-tao.md:874` (AC của
FR-III-08) và trái yêu cầu *"xuất danh sách theo bộ lọc hiện tại"* ở `:1952` + `srs-v3.5.md:5570`.

**Phạm vi hiệu lực:** `https://htpldn-uat.ospgroup.vn` · bản dựng **V1.0.10** (bó mã `index-Bd1akG3f.js`) ·
tài khoản `cbnv_tw` (CB_NV_TW, cấp TW) · **2026-08-07 17:00–17:12** · khối dữ liệu 7 bài giảng thuộc đơn vị TW
(6 đã công khai + 1 chưa công khai).

## 14. Ảnh bằng chứng

| Tệp | Nội dung | Đã mở đọc |
|---|---|---|
| `image/QLKTLBG_18-01-man-da-ap-bo-loc.png` | Màn đã áp bộ lọc Loại tài liệu = PDF; thanh công cụ có **Xuất Excel**; chân bảng "Hiển thị 1-2 / 2 kết quả"; bản dựng V1.0.10 | ✅ |
| `image/QLKTLBG_18-02-chan-bang-sau-loc.png` | Chân bảng ngay lúc bấm "Xuất Excel" lần 1 (lọc PDF): "Hiển thị 1-2 / 2 kết quả" | ✅ |
| `image/QLKTLBG_18-03-doi-chung-loc-video.png` | Phép thử đối chứng: lọc Video, 3 dòng, "Hiển thị 1-3 / 3 kết quả" | ✅ |
| `image/QLKTLBG_18-04-loc-khong-cong-khai-sai.png` | **Thao tác lỗi:** lọc "Không công khai" nhưng bảng ra 6 dòng, chụp ngay sau cú bấm Xuất Excel | ✅ |
| `image/QLKTLBG_18-05-cot-cong-khai-nguoc-bo-loc.png` | **Thao tác lỗi (rõ nhất):** ô lọc "Không công khai" vs cột "Công khai" của cả 6 dòng đều "Đã công khai" | ✅ |

Tệp xuất giữ lại để truy lại:
- `/Users/huongttt/Downloads/DanhSachBaiGiang_20260807_1704.xlsx` (lọc PDF, md5 `807f29165002ca783b533b1e50eee5dd`)
- `/Users/huongttt/Downloads/DanhSachBaiGiang_20260807_1706.xlsx` (lọc Video, md5 `038ef491f54396da7546448c4b279742`)
- `/Users/huongttt/Downloads/DanhSachBaiGiang_20260807_1709.xlsx` (lọc "Không công khai", md5 `28efd26a5c96990d8def47422d222956`)

## 15. Điều KHÔNG làm (khai rõ)

- **Không tạo / sửa / xoá bản ghi nào** trên env đối tác. Tiền đề T2/T3 đã đủ sẵn (7 bản ghi, đủ tương phản
  loại tài liệu và trạng thái công khai) nên **không cần thêm bài giảng QA**.
- **Không đổi tài khoản, không đăng xuất, không đăng nhập lại** (giữ nguyên phiên `cbnv_tw`, 0 lượt đăng nhập).
- **Không đổi vai trò để "cho ra nút"** (bẫy f) — không cần, vai trò CB NV đã thấy và bấm được nút.
- **Không ép bộ lọc qua dịch vụ**: mọi tiêu chí lọc đều nhập trên giao diện rồi bấm "Tìm kiếm"; các lời gọi
  đọc được đều là do màn tự phát sinh.
- Không mở rộng sang case QLKTLBG_19 / QLKTLBG_20 (khác vế đo — chuẩn chấm §8).
