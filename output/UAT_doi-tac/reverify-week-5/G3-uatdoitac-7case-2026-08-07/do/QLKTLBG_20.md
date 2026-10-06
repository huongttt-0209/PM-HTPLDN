# NHẬT KÝ ĐO — QLKTLBG_20 (dòng 14) · Lô G3 · env nghiệm thu đối tác

> Chuẩn chấm khoá trước khi đo: [`chuan/QLKTLBG_20.md`](../chuan/QLKTLBG_20.md). Đo xong **không sửa** chuẩn.

## 1. Bảng đầu

| Mục | Giá trị |
|---|---|
| Mã TC / dòng | **QLKTLBG_20** · dòng **14** · "Xuất Excel với điều kiện lọc không có kết quả" |
| Env | **`https://htpldn-uat.ospgroup.vn`** (env NGHIỆM THU của đối tác) |
| **Bản dựng đọc trên UI** | **`HTPLDN · V1.0.10`** (chân khối logo sidebar) — đọc **sau** khi tải lại trang bỏ qua bộ nhớ đệm |
| Bó mã FE | `assets/index-Bd1akG3f.js` (đọc từ `script[src]` của trang sau khi tải lại) |
| Ngày giờ đo | **2026-08-07**, 17:22–17:27 giờ VN (10:22–10:27 UTC) |
| Tài khoản | **`cbnv_tw`** — `hoTen` "Cán bộ NV Trung ương", `vaiTro=["CB_NV_TW"]`, `capDonVi=TW`, `donViId=00000000-0000-4000-8000-000000000001` (Cục Bổ trợ tư pháp - BTP) — đọc thật từ `GET /api/v1/auth/me` HTTP 200 |
| Vai trò theo đặc tả | `srs-fr-03-dao-tao.md:751` — *"**Tác nhân:** CB NV / CB PD"* (FR-III-07) · `:828` (FR-III-08, cùng câu). Tài khoản đo đúng vai trò CB NV |
| Màn | Đào tạo, tập huấn → Kho tài liệu / Bài giảng → Danh sách (**SCR-III-03**) |
| URL đạt được | `https://htpldn-uat.ospgroup.vn/dao-tao/bai-giang/danh-sach` |
| **Không đăng nhập lại** | Dùng đúng phiên sẵn có; không đăng xuất, không tốn lượt đăng nhập nào (giới hạn 5 lượt/60s) |
| Không đụng dữ liệu đối tác | Chỉ lọc và xuất. **Không tạo / sửa / xoá bản ghi nào** |
| Giá trị lọc thực dùng | **`ZZQAKHONGTONTAI20260807`** (đúng chuỗi chuẩn chấm §6 T3 đề nghị, không phải đổi sang biến thể) |

## 2. B0 — Tải lại trang, đọc lại bản dựng

`navigate_page type=reload ignoreCache=true`, rồi đọc lại trang:

- Chữ hiển thị trên UI: **`HTPLDN · V1.0.10`**
- `script[src]` duy nhất: `/assets/index-Bd1akG3f.js`
- `GET /api/v1/auth/me` → **HTTP 200**, `vaiTro=["CB_NV_TW"]`, `capDonVi="TW"` (phiên còn sống, không cần đăng nhập lại)

## 3. B1 — Điều hướng theo đúng bước 1 của phiếu

Bấm menu sidebar **"Đào tạo, tập huấn" → "Kho tài liệu / Bài giảng"** (nhóm menu đã ở trạng thái mở rộng sẵn).

- **URL thực tế đạt được:** `https://htpldn-uat.ospgroup.vn/dao-tao/bai-giang/danh-sach`
- Dải điều hướng: Trang chủ / Đào tạo, tập huấn / Kho tài liệu / Bài giảng / Danh sách
- Tiêu đề màn: **"Kho tài liệu / Bài giảng"**

## 4. 🔴 Sự cố tiền đề đã phát hiện và xử lý TRƯỚC khi đo (bắt buộc khai)

Phiên trình duyệt bàn giao lại từ lượt đo QLKTLBG_18 đang đứng ở URL `…/danh-sach?congKhai=false&page=1`.
Sau khi bấm sidebar, **URL và lời gọi danh sách đã sạch** (`GET /api/v1/bai-giangs?page=1&pageSize=20` → 7 bản ghi),
nhưng **ô lọc "Công khai" trên biểu mẫu vẫn còn hiển thị giá trị "Không công khai"**.

Lần bấm "Tìm kiếm" **đầu tiên** (sau khi gõ từ khoá) vì thế đã gửi lên
`GET /api/v1/bai-giangs?keyword=ZZQAKHONGTONTAI20260807&congKhai=false&page=1&pageSize=20` — tức **trộn thêm ô lọc
"Công khai"**, đúng ô mà lượt đo QLKTLBG_18 đã chứng minh là đang trả sai tập kết quả.

**Xử lý:** bấm **"Xóa bộ lọc"** → xác nhận lại toàn bộ ô lọc về rỗng và danh sách về **7** →
**gõ lại từ khoá và bấm "Tìm kiếm" lần nữa**. Mọi số đo dùng để chấm ở §6–§7 đều lấy từ lần đo **sạch** này,
chuỗi truy vấn **chỉ có `keyword`**, không có `congKhai`.

> ⚠️ **Cải chính một phép đo của chính tôi:** lần kiểm ô lọc đầu tiên tôi dùng bộ chọn `.ant-select-selection-item`
> và nhận về "không ô nào có giá trị" — **đó là âm tính giả**. Ứng dụng này dựng ô chọn bằng
> `.ant-select-content-has-value` kèm thuộc tính `title`, không dùng `.ant-select-selection-item`. Đọc lại bằng
> bộ chọn đúng thì ô "Công khai" **có** giá trị `title="Không công khai"` và **có** nút xoá (`.ant-select-clear`).
> Ghi lại đây để lượt sau không lặp lại lỗi đo này.

**Ảnh hưởng tới verdict: KHÔNG.** Vế đo của case này (tệp xuất khi bộ lọc ra 0 kết quả) được đo lại trọn vẹn
trên trạng thái sạch. Bản thân hiện tượng "ô lọc không được đặt lại khi vào lại màn" được ghi ở §10 như
**quan sát ngoài phạm vi**, không dùng để chấm dòng 14.

## 5. B2 — Mốc đối chứng: tổng bản ghi khi CHƯA lọc

| Nguồn | Giá trị |
|---|---|
| Chữ vùng phân trang (`innerText`) | **"Hiển thị 1-7 / 7 kết quả"** |
| Thân phản hồi `GET /api/v1/bai-giangs?page=1&pageSize=20` (HTTP 200) | `meta` = `{"page":1,"pageSize":20,"total":7,"totalPages":1}` → **`total` = 7** |
| Đếm tay số dòng trên bảng (DOM) | **7** |

**Ba nguồn khớp → mốc chưa lọc = 7.** Đây là con số dùng để đối chiếu ở §7.4.

7 bản ghi (đọc từ thân phản hồi): 2 PDF · 3 VIDEO · 2 SLIDE; 6 bản `congKhai=true`, 1 bản `congKhai=false` ("Test video 2").

> Mốc này được xác nhận **hai lần**: lần đầu ngay sau khi vào màn, và lần thứ hai sau khi bấm "Xóa bộ lọc"
> (`GET /api/v1/bai-giangs?page=1&pageSize=20` → lại 7 bản ghi, chân bảng lại "Hiển thị 1-7 / 7 kết quả").

## 6. B3 — Nhập tiêu chí lọc KHÔNG CÓ KẾT QUẢ trên GIAO DIỆN

**Không ép qua dịch vụ.** Gõ vào ô **"Tìm theo tên bài giảng"** (đặc tả `srs-fr-03-dao-tao.md:1955`) chuỗi
**`ZZQAKHONGTONTAI20260807`** → bấm nút **"Tìm kiếm"** (`:1960`).

**Cố ý KHÔNG dùng ô lọc "Công khai"** làm tiêu chí: lượt đo QLKTLBG_18 đã chứng minh ô này đang trả sai tập
kết quả; dùng nó sẽ trộn hai lỗi khác nhau vào cùng một verdict.

- URL màn sau khi tìm: `…/danh-sach?search=ZZQAKHONGTONTAI20260807&page=1`
- Trạng thái các ô lọc còn lại tại thời điểm bấm xuất: Loại tài liệu · Lĩnh vực pháp lý · Công khai đều ở
  chữ gợi ý (`has-value = false`); Từ ngày / Đến ngày `value` đều **rỗng**.

## 7. B4 — Chứng minh màn THẬT SỰ về 0 trước khi bấm xuất (đủ 6 chiều)

**Truy vấn thật màn gửi lên** (`list_network_requests`, reqid 415):

```
GET /api/v1/bai-giangs?keyword=ZZQAKHONGTONTAI20260807&page=1&pageSize=20   →   HTTP 200
```

⇒ Có tham số từ khoá, **không** kèm tham số lọc nào khác.

**Thân phản hồi (nguyên văn, đủ cả gói):**

```json
{"success":true,"data":[],"meta":{"page":1,"pageSize":20,"total":0,"totalPages":0}}
```

### 7.1 Bảng 6 chiều

| # | Chiều | Số đo | Đạt |
|---|---|---|---|
| 1 | Tổng bản ghi máy chủ trả về | `meta.total` = **0** | ✅ |
| 2 | Số trang | `meta.totalPages` = **0** | ✅ |
| 3 | Mảng dữ liệu trả về | `data` = **`[]`** (độ dài 0) | ✅ |
| 4 | Bảng còn dòng nào không (đếm tay DOM) | `.ant-table-tbody tr.ant-table-row` = **0 dòng**; chỉ còn **1** dòng `tr.ant-table-placeholder` | ✅ |
| 5 | Câu trạng thái rỗng hiện trên màn (nguyên văn, đọc bằng `innerText`) | **"Không có bài giảng nào phù hợp."** | ✅ |
| 6 | Vùng phân trang | `.ant-pagination` = **không tồn tại**; không còn chuỗi nào chứa "kết quả" trên màn | ✅ |

### 7.2 ⚠️ Bẫy chip "Bộ lọc nâng cao (2)" — đã kiểm, KHÔNG phải bộ lọc đang áp

Chip **"Bộ lọc nâng cao (2)"** hiện sẵn ngay khi vào màn. Hai ô bên trong là **"Từ ngày"** và **"Đến ngày"**,
`value` **cả hai đều rỗng**, và chuỗi truy vấn ở §7 xác nhận **không** có `tuNgay`/`denNgay` nào được gửi đi.
⇒ Con số `(2)` là **số ô lọc nâng cao có trong khung**, không có nghĩa "đang áp 2 điều kiện lọc".

### 7.3 Ảnh đã chụp và đã mở đọc

`image/QLKTLBG_20-01-man-loc-khong-ket-qua.png` — **đã mở ảnh ra đọc**. Nhìn thấy: sidebar ghi
`HTPLDN · V1.0.10`; dải điều hướng "Trang chủ / Đào tạo, tập huấn / Kho tài liệu / Bài giảng / Danh sách";
người đăng nhập "Cán bộ NV Trung ương · Cán bộ Nghiệp vụ Trung ương", nhãn đơn vị **BTP · TW**; vùng tiêu đề
"Kho tài liệu / Bài giảng" kèm **3 nút `+ Thêm mới` · `Xuất Excel` · `Làm mới`**; ô từ khoá chứa đúng chuỗi
**`ZZQAKHONGTONTAI20260807`** (có nút xoá ×), ba ô lọc còn lại đang là chữ gợi ý mờ ("Loại tài liệu",
"Lĩnh vực pháp lý", "Công khai") — **không ô nào mang giá trị**; chip `Bộ lọc nâng cao (2)` ở trạng thái thu gọn;
bảng chỉ còn **hàng tiêu đề cột** + đúng **một dòng chữ mờ "Không có bài giảng nào phù hợp."**;
**phía dưới bảng hoàn toàn trống — không có vùng phân trang, không có dòng "Hiển thị … kết quả"**.

## 8. B5 — Bấm xuất và kiểm NỘI DUNG tệp

### 8.1 Bộ bắt thông báo

Cài **đúng `output/UAT_doi-tac/tools/toast-capture.js`** (đọc nguyên file, tiêm nguyên khối qua `evaluate_script`)
**TRƯỚC** khi bấm. Không tự viết bộ đo, **không lọc trùng**, đọc chữ bằng `innerText`.

**Tự kiểm số observer (bắt buộc trước khi tin số liệu):** `soObserverDangSong = 1` → **hợp lệ**, số liệu dùng được.

### 8.2 Bấm "Xuất Excel" — đúng 1 lần

| Số đo | Giá trị |
|---|---|
| Số lần bấm | **1** |
| **Số khung thông báo bắt được** | **1** |
| Nguyên văn thông báo | **"Xuất dữ liệu thành công."** |
| Loại khung | toast (tự tắt ~3s) |
| Bị lặp thông báo | **Không** (`BI_LAP=false`) |
| **Số request phát sinh (khác GET)** | **1** — `POST /api/v1/bai-giangs/export` |

⇒ 1 bấm = 1 lời gọi = 1 thông báo. Không gửi trùng, không hiện trùng.

### 8.3 🔴 Mã HTTP + THÂN YÊU CẦU THẬT màn đã gửi

```
POST /api/v1/bai-giangs/export   →   HTTP 200
Thân yêu cầu: {"keyword":"ZZQAKHONGTONTAI20260807"}        (content-length: 37)
```

🔴 **Đây là bằng chứng tệp được tạo THEO BỘ LỌC HIỆN TẠI, không bỏ qua bộ lọc:** thân yêu cầu mang **đúng
từ khoá đang lọc trên màn**, không phải gói rỗng `{}` (gói rỗng chính là thân mà lượt đo QLKTLBG_19 ghi nhận
khi màn **không** đặt lọc).

Tiêu đề phản hồi:

| Tiêu đề | Giá trị |
|---|---|
| `content-type` | `application/vnd.openxmlformats-officedocument.spreadsheetml.sheet` |
| `content-disposition` | `attachment; filename="DanhSachBaiGiang_20260807_1726.xlsx"` |
| `content-length` | **6686** |
| **`x-export-exported`** | **0** |
| **`x-export-total`** | **0** |

### 8.4 MỞ TỆP RA ĐỌC NỘI DUNG (không dừng ở "tải được tệp")

Tệp **có** rơi về `~/Downloads`: `/Users/huongttt/Downloads/DanhSachBaiGiang_20260807_1726.xlsx`
· **6686 byte** (**khớp đúng `content-length`**) · md5 `da32796be8676d16386a2aef38690dba`.
Đọc bằng `openpyxl.load_workbook(path, read_only=True)`:

| Số đo | Giá trị |
|---|---|
| Số sheet | **1** |
| Tên sheet | **"Bài giảng"** |
| `ws.max_row` / `ws.max_column` | **1** / 8 |
| Tổng dòng không rỗng | **1** |
| Dòng tiêu đề | **1** |
| **Số dòng dữ liệu (1 − 1)** | **0** |

Nội dung **duy nhất** trong sheet là dòng tiêu đề:

```
Tên bài giảng · Loại tài liệu · Lĩnh vực · Dung lượng · Công khai · Người tạo · Ngày tạo · Mô tả
```

Bộ cột này trùng khít bộ cột của tệp xuất ở QLKTLBG_18 / QLKTLBG_19 ⇒ tệp vẫn là tệp xuất danh sách bình
thường, chỉ **không có bản ghi nào bên dưới**. Đúng bẫy (e) của chuẩn chấm: **tệp còn dòng tiêu đề vẫn là
"0 dòng dữ liệu"**, không được chấm Fail vì "tệp không trống hoàn toàn theo byte".

### 8.5 🔴 SỐ ĐO QUYẾT ĐỊNH — `0 vs 7`

| Vế | Số đo | Kết quả |
|---|---|---|
| Tổng bản ghi khi **chưa lọc** | **7** (chân bảng + `meta.total` + đếm tay, ba nguồn khớp) | mốc so sánh |
| Tổng bản ghi **sau khi lọc** | **0** (đủ 6 chiều ở §7.1) | tiền đề của ca đo |
| **Số dòng dữ liệu trong tệp xuất** | **0** | **= 0, KHÔNG phải 7** ✅ |
| Máy chủ tự khai | `x-export-exported = 0` / `x-export-total = 0` | khớp ✅ |

⇒ Ca PASS-oan nguy hiểm nhất mà chuẩn chấm §7 bẫy (i) cảnh báo — *tệp "rỗng" thực ra chứa toàn bộ 7 bản ghi vì
bỏ qua bộ lọc* — **đã bị loại bằng bằng chứng trực tiếp**: nếu chức năng xuất bỏ qua bộ lọc thì tệp phải có
**7** dòng dữ liệu và `content-length` phải cỡ 8610 byte (kích thước tệp 7 bản ghi đo được ở QLKTLBG_19);
thực đo là **0 dòng** và **6686 byte**.

### 8.6 Ảnh đã chụp và đã mở đọc

`image/QLKTLBG_20-02-sau-khi-bam-xuat.png` — **đã mở ảnh ra đọc**. Chụp ngay sau cú bấm "Xuất Excel".
Nhìn thấy: nút **"Xuất Excel"** đang ở trạng thái vừa bấm (viền xanh, đang giữ tiêu điểm) trong khi
`+ Thêm mới` và `Làm mới` giữ nguyên trạng thái thường; ô từ khoá vẫn giữ **`ZZQAKHONGTONTAI20260807`**;
ba ô lọc còn lại vẫn là chữ gợi ý mờ; bảng vẫn chỉ có hàng tiêu đề cột + dòng
**"Không có bài giảng nào phù hợp."**; phía dưới bảng vẫn **không có vùng phân trang**; sidebar vẫn ghi
`HTPLDN · V1.0.10`.

> **Ảnh không bắt được khung thông báo** (thông báo tự tắt ~3s và chỉ hiện sau khi máy chủ trả tệp).
> Theo bẫy (l) của chuẩn chấm, **không bấm lại chỉ để chụp lại**; bằng chứng cho vế thông báo lấy từ bộ bắt
> thông báo (§8.2) và từ thân phản hồi của chính lời gọi xuất (§8.3) — mạnh hơn ảnh.

## 9. B6 — Console

`list_console_messages` (lọc error + warn + assert): **0 lỗi**. Đúng **1 cảnh báo** duy nhất, không liên quan case:
*"Route path `/ticket=*` will be treated as if it were `/ticket=/*`…"* (cảnh báo cấu hình đường dẫn của thư viện
điều hướng, phát sinh từ lúc nạp trang, không do thao tác lọc/xuất). Trùng đúng cảnh báo đã ghi ở QLKTLBG_18/19.

## 10. Ghi nhận NGOÀI phạm vi case (không tự thêm dòng sheet — báo lead)

1. 🔴 **Ô lọc không được đặt lại khi vào lại màn bằng menu, và điều kiện "ẩn" đó được áp lại ở lần tìm kiếm kế
   tiếp.** Chi tiết đo ở §4: vào lại màn bằng sidebar thì URL và lời gọi danh sách đã sạch (7 bản ghi), nhưng ô
   "Công khai" vẫn hiển thị "Không công khai"; lần bấm "Tìm kiếm" ngay sau đó gửi kèm `congKhai=false` mà người
   dùng không chủ động chọn lại. Hệ quả nghiệp vụ: người dùng có thể tin mình đang lọc theo một tiêu chí trong
   khi hệ thống áp thêm một tiêu chí nữa — và vì tệp xuất bám theo bộ lọc hiện tại, tệp xuất cũng bị ảnh hưởng
   theo. Ghi nhận để lead quyết, **không thuộc phạm vi dòng 14**.
2. **Câu chữ lựa chọn ô lọc "Công khai" lệch đặc tả** (màn: "Công khai" / "Không công khai"; `:1958`:
   "Tất cả / Đã công khai / Chưa công khai") — đã ghi ở QLKTLBG_18 §11, nhắc lại để không rơi rụng.
3. **Bảng §6 tại `srs-fr-03-dao-tao.md:2243`** liệt kê BR-DATA-06 cho `FR-III-01, FR-III-05, FR-III-06,
   FR-III-14`, **thiếu FR-III-07 / FR-III-08** trong khi đặc tả cấp màn `:1952` quy định màn này có nút Xuất
   Excel. Điểm cần chỉnh ở **tài liệu**, không phải lỗi phần mềm (đã ghi sẵn trong chuẩn chấm §4).

## 11. Đối chiếu bảng chuẩn chấm

**Câu trích đặc tả — đã tự mở file xác minh số dòng** (`Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/`,
`srs-fr-03-dao-tao.md` **2296 dòng** · `srs-v3.5.md` **7012 dòng**):

- `srs-fr-03-dao-tao.md:751` — `**Tác nhân:** CB NV / CB PD`
- `srs-fr-03-dao-tao.md:828` — `**Tác nhân:** CB NV / CB PD`
- `srs-fr-03-dao-tao.md:1952` — `- Nút "Xuất Excel" (phụ): xuất danh sách theo bộ lọc hiện tại, tối đa 10.000 dòng (BR-DATA-06)`
- `srs-fr-03-dao-tao.md:1955` — `- Ô từ khóa: "Tìm theo tên bài giảng"`
- `srs-fr-03-dao-tao.md:1960` — `- Nút "Tìm kiếm" (chính) · "Xóa bộ lọc" (mờ)`
- `srs-v3.5.md:5570` — `| BR-DATA-06 | **Export Excel:** Mọi danh sách có tính năng xuất Excel. File xuất theo bộ lọc hiện tại, không vượt quá 10,000 rows/file | Pattern IP-01 | Toàn bộ CRUD list | Báo cáo nhóm IX có xuất PDF theo khung TT 17/2025 | Test export limit |`

| Vế | Nội dung | Đặc tả | Số đo | Kết quả |
|---|---|---|---|---|
| **D1** | Màn phải có chức năng Xuất Excel và **bấm được** (triệu chứng TKM: *"Màn hình không có nút chức năng"*) | **MATCH** — `:1952` + `srs-v3.5.md:5570` (Áp dụng FR *"Toàn bộ CRUD list"*) | Nút "Xuất Excel" có ở thanh công cụ đầu màn, `disabled=false`; bấm 1 lần → `POST /api/v1/bai-giangs/export` **HTTP 200** + sinh tệp .xlsx thật 6686 byte + 1 thông báo, không lặp | **ĐẠT** |
| **D2a** | Nhánh (a) của mệnh đề HOẶC — tệp phản ánh đúng bộ lọc đang đặt; bộ lọc ra 0 kết quả ⇒ tệp **0 dòng dữ liệu** | **MATCH** — `:1952` *"xuất danh sách **theo bộ lọc hiện tại**"* · `srs-v3.5.md:5570` *"File xuất **theo bộ lọc hiện tại**"* | Màn về 0 (đủ 6 chiều) → thân yêu cầu mang đúng từ khoá đang lọc → tệp mở được, **0 dòng dữ liệu** (chỉ còn dòng tiêu đề), `x-export-exported=0`/`x-export-total=0`. Đối chiếu **0 vs 7** | **ĐẠT** |
| **D2b** | Nhánh (b) — hiển thị thông báo không có dữ liệu / chặn xuất | **IM LẶNG cho Nhóm III → GAP → route BA** (FR-III-07 `:744–818`, FR-III-08 `:821–877`, SCR-III-03 `:1941–1984` đều không nêu) | Hệ thống **chọn nhánh (a)**: vẫn tạo tệp và báo *"Xuất dữ liệu thành công."*, không hiển thị câu "không có dữ liệu" | **Không Pass/Reopen riêng vế này** — đo hiện trạng, chuyển BA |

**Đối chiếu bảng quyết định đã cam kết TRƯỚC khi đo (chuẩn chấm §9), dòng:**
*"Có chức năng; tệp tải về, mở được, **0 dòng dữ liệu** → Nhánh (a) — mọi vế MATCH đạt ⇒ **Pass**"*.

**Bẫy (a) đã áp dụng đúng:** expected của phiếu là **mệnh đề HOẶC**. Hệ thống chỉ tạo tệp rỗng mà không báo
"không có dữ liệu" → **vẫn thoả expected**, CẤM chấm Fail vì câu chữ thông báo. Đặc tả Nhóm III cũng không quy
định câu chữ này (bẫy f).

**Không rơi vào bẫy (j)** (*không tệp + không thông báo, chỉ có toast "thành công"*): ở đây tệp **có thật**, mở
được, và có **0 dòng dữ liệu** — đúng nhánh (a).
**Không rơi vào bẫy (n)** (*hai phép đo mâu thuẫn*): thông báo, tiêu đề `x-export-*` và nội dung tệp **đều nói
cùng một điều** (0 bản ghi).

## 12. VERDICT

# ✅ PASS

Cả hai vế bắt buộc đều **ĐẠT**, đo trực tiếp trên env nghiệm thu đối tác, bản dựng **V1.0.10**:

- Màn hình **đã có** chức năng Xuất Excel và **bấm ra tệp thật** — triệu chứng cũ *"Màn hình không có nút chức
  năng"* **không còn tái hiện**.
- Với bộ lọc cho **0 kết quả** (đã chứng minh đủ 6 chiều), tệp xuất ra có **0 dòng dữ liệu** — đúng nhánh
  *"xuất danh sách rỗng"* của kỳ vọng, và chứng minh chức năng xuất **bám theo bộ lọc hiện tại** chứ không
  bỏ qua bộ lọc (thân yêu cầu mang đúng từ khoá; **0** dòng chứ không phải **7**).

**Phạm vi hiệu lực:** `https://htpldn-uat.ospgroup.vn` · bản dựng **V1.0.10** (bó mã `index-Bd1akG3f.js`) ·
tài khoản `cbnv_tw` (CB_NV_TW, cấp TW) · **2026-08-07 17:22–17:27** · khối dữ liệu 7 bài giảng thuộc đơn vị TW ·
tiêu chí lọc 0-kết-quả dựng bằng ô từ khoá "Tìm theo tên bài giảng".

## 13. Ảnh bằng chứng

| Tệp | Nội dung | Đã mở đọc |
|---|---|---|
| `image/QLKTLBG_20-01-man-loc-khong-ket-qua.png` | Màn đã áp bộ lọc 0-kết-quả: ô từ khoá `ZZQAKHONGTONTAI20260807`, bảng chỉ còn "Không có bài giảng nào phù hợp.", **không còn vùng phân trang**; thanh công cụ có **Xuất Excel**; bản dựng V1.0.10 | ✅ |
| `image/QLKTLBG_20-02-sau-khi-bam-xuat.png` | **Thao tác quyết định:** ngay sau cú bấm "Xuất Excel" (nút đang ở trạng thái vừa bấm) trong khi màn vẫn ở trạng thái 0 bản ghi | ✅ |

Tệp xuất giữ lại để truy lại: `/Users/huongttt/Downloads/DanhSachBaiGiang_20260807_1726.xlsx`
(6686 byte, md5 `da32796be8676d16386a2aef38690dba`, 1 sheet "Bài giảng", 0 dòng dữ liệu).

## 14. Điều KHÔNG làm (khai rõ)

- **Không tạo / sửa / xoá bản ghi nào** trên env đối tác. Ca này không cần seed (tiền đề T7).
- **Không đổi tài khoản, không đăng xuất, không đăng nhập lại** (giữ nguyên phiên `cbnv_tw`, 0 lượt đăng nhập).
- **Không đổi vai trò để "cho ra nút"** (bẫy h) — không cần, vai trò CB NV đã thấy và bấm được nút.
- **Không dùng ô lọc "Công khai"** làm tiêu chí lọc (đang lỗi theo QLKTLBG_18) — và đã chủ động **xoá** nó khỏi
  biểu mẫu trước khi đo (§4).
- **Không ép bộ lọc qua dịch vụ**: tiêu chí lọc gõ trên giao diện rồi bấm "Tìm kiếm"; mọi lời gọi đọc được đều
  do màn tự phát sinh.
- **Bấm nút "Xuất Excel" đúng 1 lần**; không bấm lại để chụp lại thông báo (bẫy l).
- **Không lặp lại công khảo sát liệt kê toàn bộ nút DOM** như QLKTLBG_18/19 đã làm trên đúng màn này — vế D1 ở
  case này được chứng minh bằng **thao tác thành công** (bấm → HTTP 200 → tệp thật), mạnh hơn quan sát tĩnh.
- Không mở rộng sang case QLKTLBG_18 / QLKTLBG_19 (khác vế đo — chuẩn chấm §8).

## 15. Đề nghị BA (không chặn bàn giao, KHÔNG ảnh hưởng kết quả case)

**CẦN BA CONFIRM:** đối tác kỳ vọng — khi bộ lọc màn Kho tài liệu / Bài giảng không có kết quả, hệ thống
*"xuất danh sách rỗng hoặc hiển thị thông báo không có dữ liệu"*; SRS quy định — **im lặng** cho Nhóm III:
FR-III-07 (`srs-fr-03-dao-tao.md:744–818`, bảng Error Handling `:805–809` chỉ có 3 lỗi về tải tệp bài giảng),
FR-III-08 (`:821–877`, **không có bảng Error Handling**) và SCR-III-03 (`:1941–1984`) đều không nêu hành vi khi
tập kết quả rỗng, trong khi module khác đã chốt rõ và chốt **khác nhau** (`srs-fr-13-tv-nhanh.md:155` — chặn
xuất, không tạo tệp rỗng; `srs-fr-15-ct-htpldn.md:403` + `:409` — hiển thị thông báo); **web/dev hiện tại** —
trên `https://htpldn-uat.ospgroup.vn` bản dựng **V1.0.10** (đo 07/08/2026), hệ thống **vẫn tạo tệp** với 0 dòng
dữ liệu và báo *"Xuất dữ liệu thành công."*, **không** hiển thị thông báo "không có dữ liệu".
**Mục đích câu hỏi: bổ sung điều này vào đặc tả SCR-III-03, KHÔNG phải chặn bàn giao.**
Hành vi hiện tại **đã thoả kỳ vọng của phiếu** (mệnh đề HOẶC, nhánh "xuất danh sách rỗng") ⇒ **case này Pass**.
