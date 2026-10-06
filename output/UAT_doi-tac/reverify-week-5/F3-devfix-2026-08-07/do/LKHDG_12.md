# Nhật ký đo — LKHDG_12 (dòng 126) · lô F3-devfix-2026-08-07

**Đo lúc:** 2026-08-07 02:07 → 02:12 giờ VN · **Agent:** agent ĐO (Chrome DevTools MCP)
**Chuẩn chấm áp dụng:** `output/UAT_doi-tac/reverify-week-5/F3-devfix-2026-08-07/chuan/LKHDG_12.md` (khối PASS/FAIL §6, đã khóa — không sửa)

---

## 1. Vân tay bản dựng (ghi NGAY đầu phiên, trước mọi thao tác đo)

| Hạng mục | Giá trị đo được hôm nay | Bản đã biết (BAN-DUNG.md, 06/08 18:44) | Kết |
|---|---|---|---|
| Chuỗi phiên bản chân sidebar | **`HTPLDN · V1.0.9`** | `HTPLDN · V1.0.8` | 🔼 **ĐỔI** |
| Bó mã FE (js) | **`assets/index-DsMHK7Dp.js`** | `assets/index-DIABnbIr.js` (và `index-DThrFe1_.js` ở lượt 00:32/08:50) | 🔼 **ĐỔI — không trùng bản nào trong 2 bản cũ** |
| Bó mã FE (css) | `assets/index-DVlgOkLg.css` | `assets/index-DVlgOkLg.css` | giữ nguyên |
| `GET /` last-modified | **`Thu, 06 Aug 2026 18:51:25 GMT`** (2026-08-07 01:51:25 VN) | `Thu, 06 Aug 2026 07:13:15 GMT` | 🔼 **ĐỔI** |
| `GET /` etag | **`W/"6a74d7ad-428"`** | `W/"6a74340b-428"` | 🔼 **ĐỔI** |
| Máy chủ web | `nginx/1.27.5` sau `Caddy` (`via: 1.1 Caddy`) | y hệt | giữ nguyên |
| Môi trường | `https://18.143.165.120.nip.io` — env **NỘI BỘ** | y hệt | — |

⇒ **Có bản dựng mới thật.** Cảnh báo §10.6 của chuẩn (bó mã trùng khít bản cũ ⇒ phải báo điều phối trước khi chốt) **KHÔNG kích hoạt**: bó mã `index-DsMHK7Dp.js` khác cả `index-DThrFe1_.js` lẫn `index-DIABnbIr.js`, `last-modified` mới hơn ~11,5 giờ.
⚠️ Sidebar đọc được **V1.0.9**, không phải V1.0.10 như tin nền của lô. Ghi đúng cái đo được.

**Tài khoản đo:** `cbnv_tw` / `Test@1234` — đăng nhập UI thật, mã 6 số lấy ở MailHog. Xác nhận danh tính qua `GET /api/v1/auth/me`: `vaiTro=["CB_NV_TW"]`, `donViId=00000000-0000-4000-8000-000000000001`, `capDonVi=TW`. **Không dùng `admin`.** Không cần fallback Rule 7 (đăng nhập lần đầu OK).
> Ghi chú vệ sinh phiên: khi mở trình duyệt còn phiên cũ của một tài khoản **Doanh nghiệp**; đã `POST /api/v1/auth/logout` + xoá `localStorage`/`sessionStorage` rồi mới đăng nhập lại → không lây nhiễm phạm vi dữ liệu.

---

## 2. Tiền đề đã dựng

**Không phải seed gì thêm.** Điều kiện tối thiểu của chuẩn (§3: danh sách phải có ≥2 giá trị khác nhau ở cột định lọc và `n_lọc < n_tổng`) đã thoả sẵn:

- `n_tổng = 20` đợt.
- Đợt seed vòng trước `DG-20260806-0001` **còn tồn tại**, Tần suất *Sơ bộ 6 tháng* — chính là bản ghi làm cho `n_lọc(Tròn năm) = 19 < 20`. Không mất điều kiện đo lượt 1.

**Độ phủ dạng dữ liệu M = 5/5** (theo chuẩn §7.3), N = 20 bản ghi:

| # | Dạng bắt buộc | Bản ghi minh chứng | Đạt |
|---|---|---|:-:|
| 1 | Tần suất *Sơ bộ 6 tháng* | `DG-20260806-0001` | ✅ |
| 2 | Tần suất *Tròn năm* | 19 đợt còn lại | ✅ |
| 3 | Đối tượng *Vụ việc* | `DG-20260730-0003`, … | ✅ |
| 4 | Đối tượng *Đào tạo* hoặc *Tổng hợp* | `DG-20260806-0001` (Đào tạo) · `KHDG-QAW7-02` (Tổng hợp) | ✅ |
| 5 | ≥2 giá trị Trạng thái | 7 giá trị: Lập kế hoạch · Phân công · Đang đánh giá · Thực hiện · Hủy · Đã đánh giá · Chờ phê duyệt · Hoàn thành | ✅ |

---

## 3. Các bước đo + quan sát thô (thao tác UI thật)

**Đường đi:** đăng nhập → sidebar *Đánh giá hiệu quả* → `/danh-gia/ke-hoach/danh-sach` (click sidebar, không `navigate_page`).

### Bước 1 — chưa lọc
`Hiển thị 1-20 / 20 kết quả` ⇒ **`n_tổng = 20`**.

### Bước 2 — lọc Tần suất = "Tròn năm" → [Tìm kiếm]
- URL: `…/danh-sach?tanSuat=TRON_NAM&page=1`
- Chân bảng: `Hiển thị 1-19 / 19 kết quả` ⇒ **`n_lọc¹ = 19`** ( < 20 ✔ phép đo có nghĩa)
- Cột Tần suất trên màn chỉ còn 1 giá trị: `["Tròn năm"]`
- **Tập 19 mã trên màn** (1 trang, không phải lật trang): `DG-20260730-0003, DG-20260730-0002, DG-20260730-0001, DG-20260727-0001, DG-20260725-0003, KHDG-QAW7-02, KHDG-QAW7-01, DG-20260725-0002, DG-20260725-0001, DG-20260724-0001, DG-20260723-0002, DG-20260723-0001, DG-20260722-0002, DG-20260722-0001, DG-20260720-0004, DG-20260720-0003, DG-20260720-0002, DG-20260720-0001, KHDG-SEED-0001`

### Bước 3 — [Xuất Excel] lượt 1, MỞ TỆP đếm dòng
Bộ đo thông báo cài **TRƯỚC** khi bấm; tự kiểm cho `soObserverDangSong = 1` ⇒ số liệu hợp lệ.

| Chỉ số | Giá trị |
|---|---|
| Yêu cầu phát ra | `POST /api/v1/ke-hoach-danh-gias/export?tanSuat=TRON_NAM&page=1&pageSize=20` · 200 |
| `SO_REQUEST` (không tính GET) | **1** |
| `SO_KHUNG_THONG_BAO` | **1** — `"Xuất Excel thành công"` · `khoangCachMs = null` (không có khung thứ 2 ⇒ không có dấu hiệu bất thường `SO_KHUNG > 1` + `khoangCachMs < 1ms`) |
| Kích thước tệp | **8440 byte** |
| Tiêu đề tệp (10 cột) | `Mã KH · Tên đợt · Tần suất · Đối tượng · Số vụ việc · Từ ngày · Đến ngày · Trạng thái · Người tạo · Ngày tạo` |
| **Số dòng dữ liệu** (không kể tiêu đề) | **19** |
| Tần suất trong tệp | `["Tròn năm"]` — 1 giá trị duy nhất |
| **Tập mã trong tệp** | trùng khít 19 mã ở bước 2, **đúng từng mã và đúng cả thứ tự** |

*Cách mở tệp:* bắt thân phản hồi của chính yêu cầu xuất rồi **giải nén `.xlsx` ngay trong trang** (EOCD + `DecompressionStream('deflate-raw')`), đọc `xl/worksheets/sheet1.xml` + `xl/sharedStrings.xml`. **Không** kết luận từ mã 200 hay số byte.

### Bước 4 — cột lọc KHÁC: Tần suất = "Tất cả", Trạng thái = "Hoàn thành" → [Tìm kiếm] → [Xuất Excel]
- URL sau lọc: `…/danh-sach?trangThai=HOAN_THANH&page=1` — **đã xác nhận không còn `tanSuat=`** (đúng yêu cầu chuẩn §4 ghi chú thao tác).
- Chân bảng: `Hiển thị 1-4 / 4 kết quả` ⇒ **`n_lọc² = 4`**. Cột Trạng thái trên màn: `["Hoàn thành"]`.
- **Tập 4 mã trên màn:** `DG-20260723-0002, DG-20260722-0001, DG-20260720-0001, KHDG-SEED-0001`

| Chỉ số | Giá trị |
|---|---|
| Yêu cầu phát ra | `POST /api/v1/ke-hoach-danh-gias/export?trangThai=HOAN_THANH&page=1&pageSize=20` · 200 |
| `SO_REQUEST` | **1** · `SO_KHUNG_THONG_BAO` **1** (`"Xuất Excel thành công"`) · `khoangCachMs = null` |
| Kích thước tệp | **7195 byte** — **KHÁC** lượt 1 (8440) |
| **Số dòng dữ liệu** | **4** |
| Trạng thái trong tệp | `["Hoàn thành"]` — 1 giá trị duy nhất (vòng 06/08 là 7 giá trị) |
| **Tập mã trong tệp** | `DG-20260723-0002, DG-20260722-0001, DG-20260720-0001, KHDG-SEED-0001` — **trùng khít** tập trên màn |

---

## 4. Đường đo thứ hai (gọi thẳng máy chủ bằng chính phiên đăng nhập)

`fetch(url, {credentials:'include'})` chèn trong trang — dùng bản `fetch` gốc (không đi qua lớp bọc của bộ đo) để số liệu sạch.

| Chuỗi truy vấn | `GET /api/v1/ke-hoach-danh-gias` | `POST /api/v1/ke-hoach-danh-gias/export` |
|---|---|---|
| `?trangThai=HOAN_THANH&page=1&pageSize=20` | 200 · **4** bản ghi | 200 · **7195 byte** |
| `?tanSuat=TRON_NAM&page=1&pageSize=20` | 200 · **19** bản ghi | 200 · **8439 byte** |
| `?page=1&pageSize=20` (KHÔNG lọc) | 200 · **20** bản ghi | 200 · **8559 byte** |

**Đọc kết quả:** cột `GET` biến thiên theo bộ lọc (4 / 19 / 20) **và** cột `POST …/export` nay **cũng biến thiên** (7195 / 8439 / 8559) — **3 giá trị khác nhau**. Vòng 06/08 cột export đứng yên `8519 / 8519 / 8519`. ⇒ Phần sinh tệp phía máy chủ **đã dùng tham số lọc**, đúng chỗ trước đây bỏ qua.
*(8439 ↔ 8440 lệch 1 byte giữa đường 2 và đường UI cùng bộ lọc: khác dấu thời gian nén trong `.xlsx`, không phải khác nội dung — số dòng và tập mã đã đối chiếu bằng nội dung, không bằng byte.)*
**Không có mâu thuẫn UI vs API** — hai đường cùng kết luận.

---

## 5. Bảng GAP (điều kiện PASS/FAIL không đo được)

| # | Điều kiện trong khối đã khóa | Đo được? | Ghi chú |
|---|---|:-:|---|
| 1 | Số dòng dữ liệu trong tệp = `n_lọc`, cả 2 lượt | ✅ | đã mở tệp đếm, không suy từ byte |
| 2 | Tập "Mã KH" trong tệp trùng khít tập trên màn, **so từng mã** | ✅ | so từng phần tử, cả 2 lượt |
| 3 | 2 lượt lọc khác nhau không cho 2 tệp cùng kích thước byte | ✅ | 8440 ≠ 7195 |

⇒ **BẢNG GAP TRỐNG — 0 mục.** Không rơi vào luật "có GAP ⇒ verdict ô trống".

---

## 6. Đối chiếu TỪNG gạch đầu dòng của khối PASS/FAIL đã khóa

> Khối nguồn: `chuan/LKHDG_12.md` §6 (chép từ `flowtest-kiemdinh/bug-report.md:116-123`). Không sửa, không nới.

| Gạch đầu dòng của khối khóa | Số đo | Kết |
|---|---|:-:|
| ✅ *"cả 2 lượt, số dòng dữ liệu trong tệp = đúng `n_lọc` của lượt đó"* | lượt 1: 19 = 19 · lượt 2: 4 = 4 | **THOẢ** |
| ✅ *"tập 'Mã KH' trong tệp trùng khít tập mã đang hiện trên màn (so từng mã, không chỉ so số lượng)"* | lượt 1: 19/19 mã khớp từng cái · lượt 2: 4/4 mã khớp từng cái | **THOẢ** |
| ❌ *"tệp chứa ≥1 mã không thuộc tập sau lọc"* | 0 mã lạ ở cả 2 lượt (vòng trước dư `DG-20260806-0001`) | **KHÔNG dính** |
| ❌ *"số dòng ≠ `n_lọc`"* | 19 = 19 · 4 = 4 | **KHÔNG dính** |
| ❌ *"2 lượt lọc khác nhau lại cho 2 tệp cùng kích thước byte"* | 8440 vs 7195 | **KHÔNG dính** |
| ⚠️ *"Đừng chấm Fail vì tệp thiếu cột hay vì định dạng nhãn"* | tuân thủ — tệp có 10 cột, nhãn tiếng Việt có dấu; **chỉ ghi nhận**, không dùng chấm | tuân thủ |
| ⚠️ *"Đừng kết luận 'đã fix' khi chỉ thấy đường dẫn có mang tham số lọc"* | tuân thủ — **đã mở tệp đếm dòng** + đối chứng đường 2, không chốt bằng URL/200/byte | tuân thủ |

**Bẫy chuẩn §8 đã né:** #1 URL có tham số ≠ đã fix (đã mở tệp) · #2 200/byte ≠ đúng (đã đọc nội dung) · #3 không chấm Fail vì cột/nhãn · #4 tìm cột mã theo **nội dung** chuỗi `DG-…`/`KHDG-…` chứ không theo tiêu đề · #5 so từng mã · #6 `n_lọc < n_tổng` ở cả 2 lượt · #7 không phải lật trang (19 ≤ 20/trang) · #9 đã tải lại trang + ghi bó mã FE.

---

## 7. VERDICT

# ✅ **Pass**

**Căn cứ:**
- **Đặc tả (tự mở đếm lại hôm nay 07/08):** `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-v3.5.md:5570` — BR-DATA-06: *"**Export Excel:** Mọi danh sách có tính năng xuất Excel. **File xuất theo bộ lọc hiện tại**, không vượt quá 10,000 rows/file"*, cột *Áp dụng FR* = **"Toàn bộ CRUD list"**, cột *Ngoại lệ* chỉ miễn *"Báo cáo nhóm IX có xuất PDF theo khung TT 17/2025"* ⇒ **không miễn nhóm VI**. Nút [Xuất Excel] của màn: `srs-fr-08-danh-gia.md:823`.
  🔴 Hồ sơ cũ ghi `srs-v3.5.md:5525` (**lệch −45 dòng**) và `srs-fr-08-danh-gia.md:821` (**lệch −2**) — đã tự mở file xác minh và sửa lại trong cả 2 file bug-report.
- **Vế (a)** — vế DUY NHẤT quyết định verdict theo chuẩn §1 — **đã hết lỗi**: tệp xuất đúng tập đang hiển thị, đo trên **2 cột lọc khác nhau** (Tần suất `:825`, Trạng thái `:827`), chốt bằng **nội dung tệp** và **đường đo thứ hai**.
- **Vế (b) + (c)** (thiếu cột / nhãn mã enum thô): vẫn hết lỗi, **không tái phát** — ghi nhận, **không** dùng làm căn cứ verdict (đặc tả im lặng, chuẩn §2).

**Giới hạn hiệu lực:** đo trên **env nội bộ** `18.143.165.120.nip.io` bản **V1.0.9 / `index-DsMHK7Dp.js`**. Đối tác nghiệm thu trên `htpldn-uat.ospgroup.vn` bản V1.0 ⇒ đây là **Pass tạm**, chỉ có hiệu lực cho tới khi bản dựng này lên env đối tác.

---

## 8. Lỗi phát hiện thêm ngoài phạm vi (candidate — KHÔNG dùng làm căn cứ verdict)

1. **Nhãn trạng thái của ứng dụng lệch enum đặc tả `:827`.** Danh sách chọn "Trạng thái" trên màn có 9 mục: *Tất cả · Lập kế hoạch · Phân công · Chờ duyệt PC · Thực hiện · **Đang đánh giá** · **Đã đánh giá** · **Lập báo cáo** · Chờ phê duyệt · Hoàn thành*. Ba nhãn in đậm không có trong enum đặc tả (`:827` liệt kê `LAP_KE_HOACH / PHAN_CONG / CHO_DUYET_PC / THUC_HIEN / BAO_CAO / CHO_PHE_DUYET / HOAN_THANH / HUY`); ngoài ra màn **thiếu** mục *Hủy* trong danh sách chọn dù bảng vẫn hiển thị đợt trạng thái *Hủy*. Đây là phát hiện tình cờ (đúng loại đã ghi ở chuẩn §8.8) — **đặc tả im lặng về nhãn**, ghi riêng, không đổi verdict.
2. **Nút "Bộ lọc nâng cao (2)"** trên thanh lọc không nằm trong bảng `filter-bar` của đặc tả (`:824-829` chỉ có 5 ô lọc + nút Tìm kiếm/Xóa bộ lọc). Ngoài phạm vi case, chỉ ghi nhận.
3. **Bản ghi `DG-20260806-0001` đã bị đổi tên trước khi tôi đo** — tên hiện tại kết thúc bằng `"- sua v1.0.9"`, tức đã có người/quy trình khác chỉnh sửa bản ghi này trên bản dựng V1.0.9 trước phiên đo này. Không ảnh hưởng phép đo LKHDG_12 (chỉ dùng bản ghi này làm biến thể Tần suất), nhưng **ghi lại để điều phối biết dữ liệu env không còn nguyên trạng so với vòng 06/08**.

---

## 9. Ảnh bằng chứng

| Ảnh | Đường dẫn |
|---|---|
| Lượt 1 — màn đã lọc Tần suất *Tròn năm*, chân bảng "Hiển thị 1-19 / 19 kết quả", URL `?tanSuat=TRON_NAM&page=1`, chân sidebar `HTPLDN · V1.0.9` | `output/UAT_doi-tac/flowtest-kiemdinh/image/LKHDG_12-R3-01-luot1-loc-TronNam-19ketqua-V109.png` · bản sao `output/UAT_doi-tac/reverify-bug-devfix-2026-08-06/bug-reports/image/LKHDG_12-R3-01-luot1-loc-TronNam-19ketqua-V109.png` |
| Lượt 2 — màn đã lọc Trạng thái *Hoàn thành*, chân bảng "Hiển thị 1-4 / 4 kết quả", URL `?trangThai=HOAN_THANH&page=1` | `output/UAT_doi-tac/flowtest-kiemdinh/image/LKHDG_12-R3-02-luot2-loc-HoanThanh-4ketqua-V109.png` · bản sao `output/UAT_doi-tac/reverify-bug-devfix-2026-08-06/bug-reports/image/LKHDG_12-R3-02-luot2-loc-HoanThanh-4ketqua-V109.png` |
