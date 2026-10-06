# CHUẨN CHẤM — QLKTLBG_19 (Lô G3 · khoá TRƯỚC khi đo)

> **Chưa mở màn.** File này khoá chuẩn chấm TRƯỚC khi đo. Sau khi đo, CẤM sửa quan hệ `MATCH / GAP` hay
> đổi tiêu chí Pass/Reopen để khớp kết quả quan sát được.
>
> ⚠️ Ô "Kết quả verify" của dòng này **đã có nội dung, nhưng đo trên env NỘI BỘ**. Lô G3 là lượt xác nhận
> lại trên env đối tác — **cấm chép kết luận cũ**, phải đo lại thật.

## 1. Bảng đầu

| Mục | Giá trị |
|---|---|
| Bảng / tab / dòng | Bảng đối tác · tab `bug` · **dòng 13** |
| Mã TC | **QLKTLBG_19** |
| Mô tả (đối tác) | "Xuất excel không có điều kiện lọc" |
| Trạng thái nguồn | Trạng thái `Fail` · Trạng thái dev fix `Test done` · Kết quả verify đã có (đo env **nội bộ**) |
| TKM phản hồi lần 1 | "Màn hình không có nút chức năng" |
| Env | **`https://htpldn-uat.ospgroup.vn`** (env NGHIỆM THU của đối tác) — MailHog `https://htpldn-uat.ospgroup.vn/mailhog/` |
| Bản dựng | **(để trống — đọc trên UI khi đo)**; bắt buộc tải lại trang rồi mới ghi số hiệu ở sidebar/chân trang |
| Tài khoản dự kiến | `cbnv_tw` / `Test@1234` (vai trò `CB_NV_TW`, cấp TW). OTP lấy ở MailHog của **chính env này**. Giới hạn đăng nhập 5 lượt/60 giây |
| Vai trò theo đặc tả | **CB NV** (hoặc CB PD) — `srs-fr-03-dao-tao.md:751` ("**Tác nhân:** CB NV / CB PD" — FR-III-07) và `:828` (FR-III-08); quyền PRE-01 `:757` |
| Màn | Đào tạo, tập huấn → **Kho tài liệu / Bài giảng** → Danh sách (**SCR-III-03**) |
| URL | `https://htpldn-uat.ospgroup.vn/dao-tao/bai-giang/danh-sach` — **đã có bằng chứng trên chính env đối tác** (thanh địa chỉ trong ảnh `QLKTLBG_18.jpg`, cùng màn), không phải suy đoán |
| SRS đã đọc | `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-03-dao-tao.md` — **2296 dòng** |
| SRS đã đọc | `Docs-PM-HTPLDN/…/srs-v3.5/srs-v3.5.md` — **7012 dòng** |
| SRS đã đọc (tiền lệ module khác) | `srs-fr-13-tv-nhanh.md` — **932 dòng** · `srs-fr-15-ct-htpldn.md` — **1610 dòng** |

---

## 2. Nguồn đã đọc (tự mở trong lượt này)

**SRS nguồn chuẩn DUY NHẤT — `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/`:**

| File | Đoạn đã đọc trọn | Nội dung |
|---|---|---|
| `srs-fr-03-dao-tao.md` | `:744–818` | **FR-III-07 (UC26) trọn mục**, gồm **Error Handling `:803–809`** |
| `srs-fr-03-dao-tao.md` | `:821–877` | **FR-III-08 (UC27) trọn mục** — **KHÔNG có bảng Error Handling** |
| `srs-fr-03-dao-tao.md` | `:1941–1984` | **SCR-III-03 trọn mục** — 6 Thành phần + Quy tắc nghiệp vụ |
| `srs-fr-03-dao-tao.md` | `:2227–2252` | §6 Tổng quan BR sử dụng (gồm `:2243`) |
| `srs-v3.5.md` | `:5561–5574` | Phụ lục B.2 BR-DATA (trọn bảng, gồm **BR-DATA-06 `:5570`**) |
| `srs-v3.5.md` | `:861` | EC-DATA-PAGE — ràng buộc phân trang |
| `srs-fr-13-tv-nhanh.md` | `:148–157` | Bảng Error Handling — tiền lệ module khác (xuất Excel, giới hạn 10.000 dòng) |
| `srs-fr-15-ct-htpldn.md` | `:398–412` | Bảng Error Handling + AC — tiền lệ module khác |

**Quét từ đồng nghĩa đã chạy** (nhiều lệnh, không chỉ 1 grep) trên `srs-fr-03-dao-tao.md` và **toàn thư mục**
`srs-v3.5/`: `Xuất Excel` · `xuất excel` · `Xuất file` · `kết xuất` · `export` · `xuất tệp` · `xuất danh sách` ·
`tải xuống` · `Tải về` · `toàn bộ danh sách` · `bộ lọc hiện tại` · `BR-DATA-06` · `phân trang` ·
`danh sách rỗng` · `không có dữ liệu`.

**Ngữ cảnh (CHỈ để biết tra chỗ nào — KHÔNG dùng làm căn cứ verdict, không mượn số dòng):**
`output/UAT_doi-tac/flowtest-2026-08-05/partner-evidence/QLKTLBG_18.jpg` (ảnh cùng màn — xem §3) ·
`output/UAT_doi-tac/flowtest-2026-08-05/evidence/DEV-QLKTLBG_18-nut-xuat-excel-loc-slide-V108.png` (ảnh
chụp **env nội bộ**, bản dựng `V1.0.8` — **KHÔNG** dùng cho env đối tác) ·
`output/UAT_doi-tac/bug-con-fail-doi-tac-2026-07-31.md:335`.

---

## 3. Cổng bằng chứng

- **Không có bằng chứng riêng cho QLKTLBG_19** — ô Ảnh/video của dòng 13 rỗng.
- **Có bằng chứng của case cùng màn** (`QLKTLBG_18.jpg`) — đã mở xem: thanh địa chỉ
  `htpldn-uat.ospgroup.vn/dao-tao/bai-giang/danh-sach`, bản dựng sidebar `HTPLDN · V1.0`, đồng hồ 2026-07-25,
  vai trò `CB_NV_TW`, vùng tiêu đề chỉ có **`+ Thêm mới`** và **`Làm mới`** (**không có "Xuất Excel"**), chip
  `Bộ lọc nâng cao (2)` hiện sẵn, bảng có dữ liệu nhiều loại.
  **Ảnh này dùng để định vị màn + xác nhận URL, KHÔNG dùng để kết luận verdict cho dòng 13.**
- **Vẫn chạy tiếp.** Thiếu bằng chứng riêng nhưng **tự tái hiện được**: đúng 2 bước, không cần tiền đề đặc
  biệt, không cần ID bản ghi của đối tác. Ca này còn **dễ dựng hơn** QLKTLBG_18 vì không cần đặt bộ lọc.
- **Điều kiện tái hiện sẽ ghi vào báo cáo:** env + bản dựng đọc trên UI · tài khoản thực dùng · URL màn ·
  **xác nhận đã Xóa bộ lọc** · **tổng số bản ghi màn báo** ngay trước khi bấm Xuất Excel.
- **Không đụng dữ liệu đối tác** — chỉ xem và xuất, không sửa/xóa bản ghi nào.

---

## 4. Bảng chuẩn chấm

**Expected đối tác (nguyên văn):** *"Hệ thống xuất toàn bộ danh sách hiện có trên bảng danh sách"*

🔴 **Khoá cách hiểu ngay:** *"toàn bộ danh sách hiện có trên bảng danh sách"* = **toàn bộ tập kết quả mà màn
đang liệt kê cho tài khoản đang đăng nhập**, tức tổng số bản ghi màn báo — **KHÔNG** phải "trang đang xem",
và cũng **KHÔNG** phải "mọi bản ghi trong hệ thống bất kể phân quyền đơn vị" (`:1981` — lọc theo `don_vi_id`
theo BR-AUTH-08).

| # | Điều kiện của BUG GỐC | Đặc tả nói gì (file:dòng, nguyên văn) | Phép đo quyết định | Pass khi | Reopen khi |
|---|---|---|---|---|---|
| **C1** | Bước 2 của phiếu — *"Nhấn Xuất excel"* — **thực hiện được**: màn Kho tài liệu / Bài giảng phải có chức năng Xuất Excel. Triệu chứng TKM: *"Màn hình không có nút chức năng"* | **MATCH.** `srs-fr-03-dao-tao.md:1952` — *"Nút \"Xuất Excel\" (phụ): xuất danh sách theo bộ lọc hiện tại, tối đa 10.000 dòng (BR-DATA-06)"* · `srs-v3.5.md:5570` — *"**Export Excel:** Mọi danh sách có tính năng xuất Excel…"*, Áp dụng FR = *"Toàn bộ CRUD list"* | Liệt kê DOM vùng tiêu đề + thanh công cụ: mảng `{tag, innerText, title, ariaLabel, className, disabled}` của mọi `button`/`a`/`[role=button]`; mở mọi menu phụ rồi lặp lại. Đối chứng độc lập: `paths` chứa `bai-giang` ở `/api/docs-json`, lọc `export`/`excel`/`xuat` — **CẤM đoán đường dẫn** | Màn có chức năng Xuất Excel dùng được (bấm được, sinh ra lời gọi tải tệp) | Đã liệt kê DOM + menu phụ + `/api/docs-json` mà **không có** chức năng xuất danh sách nào ở thanh công cụ |
| **C2** | Vế nội dung — khi **không đặt điều kiện lọc**, tệp phải chứa **toàn bộ** danh sách màn đang có, **không chỉ trang đang xem** | **MATCH.** `srs-fr-03-dao-tao.md:1952` — *"xuất danh sách theo bộ lọc hiện tại, **tối đa 10.000 dòng**"* (bộ lọc rỗng ⇒ tập xuất = toàn bộ danh sách) · `srs-v3.5.md:5570` — *"File xuất theo bộ lọc hiện tại, **không vượt quá 10,000 rows/file**"*. Giới hạn duy nhất đặc tả đặt ra là **10.000 dòng**, **không phải kích thước trang** | **Xóa bộ lọc** → ghi **tổng bản ghi màn báo** (đọc `innerText` vùng phân trang **và** `total`/`total_count` trong thân phản hồi danh sách) → bấm Xuất Excel 1 lần → **MỞ TỆP** bằng `openpyxl` đếm số dòng dữ liệu (tổng dòng − dòng tiêu đề) | Số dòng dữ liệu trong tệp **= tổng bản ghi màn báo** (khi tổng ≤ 10.000) | Tệp chỉ chứa **trang đang xem** (vd đúng 20 dòng trong khi tổng lớn hơn); hoặc số dòng **thiếu/thừa** so với tổng mà không có lý do thuộc đặc tả |

### Trích nguyên văn SRS dưới từng vế

**C1 — `srs-fr-03-dao-tao.md:1949–1952` (Thành phần 2 của SCR-III-03, trọn khối):**

```
**Thành phần 2 — Tiêu đề + Hành động chính:**
- Tiêu đề trang: "Kho tài liệu & bài giảng"
- Nút "+ Thêm mới" (chính): mở biểu mẫu thêm bài giảng
- Nút "Xuất Excel" (phụ): xuất danh sách theo bộ lọc hiện tại, tối đa 10.000 dòng (BR-DATA-06)
```

**C1 + C2 — `srs-v3.5.md:5570`** (Phụ lục B.2, BR-DATA-06; header cột ở `:5563`):

```
| BR-DATA-06 | **Export Excel:** Mọi danh sách có tính năng xuất Excel. File xuất theo bộ lọc hiện tại, không vượt quá 10,000 rows/file | Pattern IP-01 | Toàn bộ CRUD list | Báo cáo nhóm IX có xuất PDF theo khung TT 17/2025 | Test export limit |
```

**C2 — `srs-fr-03-dao-tao.md:1976` (phân trang — nguồn của bẫy PASS-oan chính):**

```
**Thành phần 5 — Phân trang:** mặc định 20 dòng/trang; cho phép 10/20/50/100.
```

> Đây là lý do C2 phải mở tệp đếm dòng: mặc định màn chỉ hiện 20 dòng, nên tệp 20 dòng **trông rất giống**
> tệp đúng nếu chỉ nhìn qua.

**C2 — `srs-v3.5.md:861` (EC-DATA-PAGE — khẳng định màn luôn hiển thị tổng bản ghi, tức mốc so sánh luôn có):**

```
> **EC-DATA-PAGE — Ràng buộc Pagination:** Số bản ghi/trang nằm trong khoảng [1, 100], mặc định 20. … Trang vượt trang cuối trả danh sách rỗng kèm total_count. **(S3-1)** Cho phép thay đổi số bản ghi/trang: 10, 20, 50, 100. Luôn hiển thị tổng số bản ghi ở màn danh sách.
```

**C2 phạm vi dữ liệu — `srs-fr-03-dao-tao.md:1981`:**

```
- Danh sách lọc theo đơn vị sở hữu (`don_vi_id`) theo BR-AUTH-08.
```

**C2 — bộ lọc mặc định của màn, `srs-fr-03-dao-tao.md:1954–1960`** (để biết "không có điều kiện lọc" nghĩa là
đưa tất cả các ô này về trạng thái rỗng / "Tất cả"):

```
**Thành phần 3 — Thanh lọc và tìm kiếm:**
- Ô từ khóa: "Tìm theo tên bài giảng"
- Lọc Loại tài liệu: Tất cả / Slide / PDF / Video
- Lọc Lĩnh vực pháp luật (chọn nhiều — nguồn DANH_MUC loại LINH_VUC_PL)
- Lọc Công khai: Tất cả / Đã công khai / Chưa công khai `[STT66 UAT 2026-06-02]`
- Lọc Từ ngày / Đến ngày (theo ngày tạo)
- Nút "Tìm kiếm" (chính) · "Xóa bộ lọc" (mờ)
```

### 🔴 Trả lời câu hỏi then chốt

> **SRS có quy định màn Kho tài liệu / Bài giảng phải có chức năng Xuất Excel không?**

**CÓ — quy định rõ, ở cấp màn hình** (`:1952`), dẫn thẳng BR-DATA-06 (`srs-v3.5.md:5570`) với Áp dụng FR =
*"Toàn bộ CRUD list"*, ngoại lệ duy nhất là *Báo cáo nhóm IX*. ⇒ **C1 MATCH · thiếu chức năng = Reopen.**

> **SRS có quy định tệp xuất khi KHÔNG lọc phải chứa toàn bộ danh sách không?**

**CÓ, theo cách suy trực tiếp từ câu chữ — không phải suy diễn.** Cả `:1952` lẫn `srs-v3.5.md:5570` đều đặt
**đúng một** giới hạn cho tập xuất: *"tối đa 10.000 dòng"* / *"không vượt quá 10,000 rows/file"*. Đặc tả
**không** ở đâu nói tệp xuất bị giới hạn theo kích thước trang. Bộ lọc rỗng ⇒ *"theo bộ lọc hiện tại"* = toàn
bộ danh sách. ⇒ **C2 MATCH.**

### ⚠️ Đã cân nhắc và LOẠI khả năng "SRS im lặng"

Bảng §6 tại `srs-fr-03-dao-tao.md:2243` ghi `| BR-DATA-06 | Export Excel | FR-III-01, FR-III-05, FR-III-06,
FR-III-14 |` — **không liệt kê FR-III-07/FR-III-08**. **Không phải mệnh đề ngoại lệ:** đó là bảng mục lục
tham chiếu chéo cấp FR, không dùng từ "không áp dụng"; ngoại lệ của BR-DATA-06 nằm ở **cột "Ngoại lệ" của
chính BR** (`srs-v3.5.md:5570`) và chỉ có *Báo cáo nhóm IX*; đặc tả cấp màn (`:1952`) nói rõ màn này CÓ nút
và **là căn cứ nghiệm thu** (`:1945`). → **Không đổi quan hệ C1/C2.** Ghi **1 dòng candidate tài liệu**
(không phải bug phần mềm): *"Bảng §6 `:2243` thiếu FR-III-07/FR-III-08 ở dòng BR-DATA-06."*

---

## 5. Đường đo tối thiểu

**Một đường UI ngắn nhất + một đối chứng độc lập. Bấm Xuất Excel đúng 1 lần.**

| Bước | Nội dung | Kiểm vế |
|---|---|---|
| U0 | Đăng nhập `cbnv_tw` trên `https://htpldn-uat.ospgroup.vn` (OTP MailHog cùng env), **tải lại trang**, ghi số hiệu bản dựng | tiền đề |
| U1 | (Phiếu bước 1) Chọn menu **"Đào tạo, tập huấn" → "Kho tài liệu / Bài giảng"**; xác nhận URL `…/dao-tao/bai-giang/danh-sach` | tiền đề |
| U2 | Bấm **"Xóa bộ lọc"** (`:1960`); kiểm mọi ô lọc về rỗng/"Tất cả", **mở cả khối "Bộ lọc nâng cao"** kiểm từng ô bên trong | tiền đề T2 |
| U3 | **Ghi tổng bản ghi màn báo**: `innerText` vùng phân trang + `total`/`total_count` trong thân phản hồi danh sách. Hai nguồn phải khớp. Chưa có con số này thì **CẤM bấm xuất** | tiền đề T3 |
| U4 | Liệt kê DOM vùng tiêu đề + thanh công cụ (`innerText` + `title` + `aria-label` + `className` + `disabled`); mở mọi menu phụ rồi lặp lại | **C1** |
| U5 | Cài `output/UAT_doi-tac/tools/toast-capture.js` **TRƯỚC** khi bấm | phụ trợ |
| U6 | (Phiếu bước 2) Bấm **Xuất Excel** (UI thật, **1 lần**) | **C1** |
| U7 | Ghi: có/không tệp tải về · nguyên văn thông báo bắt được · số lời gọi mạng kèm theo · mã trạng thái lời gọi xuất | **C1** |
| Đối chứng độc lập | **MỞ TỆP**: `openpyxl.load_workbook(path, read_only=True)` → đếm số dòng dữ liệu (tổng dòng − dòng tiêu đề); so với con số ghi ở U3 | **C2** |
| Đối chứng độc lập | `fetch('/api/docs-json')` → `paths` chứa `bai-giang`, lọc `export`/`excel`/`xuat`. **CẤM tự đoán đường dẫn** | **C1** |

**Lấy tệp về để mở — thử theo thứ tự, dừng khi được:** (1) kiểm `~/Downloads`; (2) nếu trình duyệt điều khiển
bằng công cụ không đổ tệp ra đĩa → đọc nội dung **ngay trong trang**: `fetch` lại **đúng** URL tệp mà lời gọi
tải đã dùng (lấy từ `list_network_requests`, **không đoán**) → parse EOCD + `DecompressionStream`, chỉ trả về
số dòng cần đo; (3) giữ lại đường dẫn tệp để verdict truy lại được.

C1 không đạt ⇒ **C2 không đo được** — ghi rõ bị chặn bởi C1, **không** suy đoán hệ thống "sẽ" làm gì.

🔴 **CẤM dừng ở "tải được tệp".** HTTP 200 + dữ liệu nhị phân chỉ chứng minh CREATE, không chứng minh CORRECT.

---

## 6. Tiền đề phải dựng

| # | Tiền đề | Vì sao bắt buộc (dòng SRS) | Cách dựng nếu thiếu |
|---|---|---|---|
| **T1** | Tài khoản vai trò **CB NV** | `:751` tác nhân FR-III-07 · `:828` tác nhân FR-III-08 · `:757` quyền "Quản lý tài liệu ĐT" | `cbnv_tw` / `Test@1234` + OTP MailHog env đối tác. Env này **chưa xác nhận có tài khoản anh em** `cbnv_tw_02/_03` → khoá lock thì **DỪNG, báo lead**, cấm đổi vai trò/cấp |
| **T2** | **Bộ lọc thật sự rỗng** trước khi bấm xuất | Đây là chữ *"không có điều kiện lọc"* của phiếu; nếu còn sót 1 ô lọc thì phép đo nói về case 18 chứ không phải case 19 | Bấm **"Xóa bộ lọc"** (`:1960`), **mở khối "Bộ lọc nâng cao" kiểm từng ô bên trong**, rồi đọc lại danh sách. Ghi ảnh chụp trạng thái thanh lọc |
| **T3** | **Biết chắc tổng bản ghi màn báo** | Không có con số này thì C2 không chấm được | `innerText` vùng phân trang + `total`/`total_count` trong thân phản hồi. Hai nguồn lệch nhau → **Chưa chốt**, ghi cả hai |
| **T4** | Tổng bản ghi **> 20** (lý tưởng) để phân biệt "toàn bộ" với "một trang" | `:1976` — mặc định 20 dòng/trang. Nếu tổng ≤ 20 thì tệp 20 dòng và tệp "toàn bộ" **trùng nhau** ⇒ phép đo **không phân biệt được** | Nếu tổng ≤ 20: (a) đổi số bản ghi/trang xuống **10** (`:1976` cho phép) rồi đo lại — khi đó tệp phải có > 10 dòng nếu tổng > 10; (b) nếu tổng vẫn ≤ 10 thì **thêm bản ghi QA** (`+ Thêm mới`, tên có dấu `QA` + ngày) cho tới khi tổng > số dòng/trang, và **khai rõ đã tạo gì**; (c) không dựng được thì ghi rõ **giới hạn của phép đo** trong nhật ký, không âm thầm bỏ qua |
| **T5** | Tổng bản ghi **≤ 10.000** | `:1952` + `srs-v3.5.md:5570` — trên ngưỡng này hành vi đúng là cắt/cảnh báo, không phải "toàn bộ" | Env UAT gần như chắc chắn dưới ngưỡng; vẫn ghi lại con số tổng để loại trừ |
| **T6** | Ghi **env + bản dựng** sau khi tải lại trang | Luật 4 BRIEF | Đọc ở sidebar/chân trang (ảnh đối tác cho thấy vị trí này hiển thị `HTPLDN · V1.0`) |

**Không đụng dữ liệu đối tác** — chỉ xem và xuất; nếu buộc phải thêm bản ghi để dựng T4 thì khai đủ:
**thêm bản ghi nào · đặt tên gì · env nào**.

---

## 7. Bẫy đã biết

**Chặn FAIL oan:**

- **(a) 🔴 Chip "Bộ lọc nâng cao (2)" hiện sẵn KHÔNG phải là bộ lọc đang áp dụng.** Ảnh đối tác cho thấy chip
  này hiện ngay khi vào màn. Con số `(2)` là **số ô lọc nâng cao có sẵn**, không có nghĩa "đang có 2 điều
  kiện lọc đang áp". **Nhưng** vẫn phải bấm "Xóa bộ lọc" + mở khối kiểm từng ô (T2) — vì ngược lại, nếu thật
  sự còn sót điều kiện thì tệp thiếu dòng sẽ bị chấm Fail oan.
- **(b) Nút có thể nằm trong menu phụ / là biểu tượng không nhãn.** CẤM kết luận "không có nút" bằng mắt qua
  ảnh chụp. Phải liệt kê `innerText` **cộng** `title`/`aria-label`/`className` của mọi
  `button`/`a`/`[role=button]`, và mở thử menu phụ trước khi chốt C1.
- **(c) 🔴 Biểu tượng ở cột "Thao tác" từng dòng ≠ nút xuất danh sách.** `:1974` — *"Hành động | — | Xem trực
  tuyến · **Tải về (chỉ Slide/PDF)** · Sửa · Xóa"*. C1 đo ở **thanh công cụ đầu màn**, không đo ở dòng bảng.
- **(d) SRS Nhóm III không quy định bộ cột tệp xuất SCR-III-03.** FR-III-07 (`:744–818`) và FR-III-08
  (`:821–877`) không có mục "Processing — Xuất Excel" (khác FR-III-01 `:180–184`, FR-III-05 `:599–605`).
  ⇒ **CẤM chấm Fail vì thiếu/thừa cột, sai thứ tự, sai tên sheet, tên tệp.**
- **(e) SRS không quy định câu chữ thông báo sau khi xuất ở màn này.** CẤM chấm Fail vì không có toast hoặc
  toast khác chữ.
- **(f) Bản ghi ngoài phạm vi đơn vị không có trong tệp.** `:1981` — danh sách lọc theo `don_vi_id`
  (BR-AUTH-08). Mốc so sánh là **tổng màn báo cho tài khoản đang đăng nhập**, không phải toàn bộ dữ liệu hệ
  thống. CẤM đối chiếu tệp với số bản ghi đếm bằng tài khoản `admin`.
- **(g) Đổi vai trò để "cho ra nút".** Nếu C1 không đạt, CẤM đăng nhập `admin` rồi kết luận Pass — vai trò
  của vế là **CB NV** (`:751`).

**Chặn PASS oan:**

- **(h) 🔴 Tệp chỉ chứa trang đang xem.** `:1976` — mặc định 20 dòng/trang. **Đây là ca PASS-oan nguy hiểm
  nhất của case này**: tệp mở được, có tiêu đề đẹp, 20 dòng dữ liệu — trông y hệt tệp đúng. Bắt buộc so với
  con số tổng ghi ở U3.
- **(i) "Tải được tệp" ≠ "nội dung đúng".** Bắt buộc mở tệp bằng `openpyxl` đếm dòng.
- **(j) Đếm nhầm dòng tiêu đề.** Số dòng dữ liệu = tổng dòng − dòng tiêu đề. Ghi cả hai con số.
- **(k) Đọc tổng bản ghi từ nguồn không tin cậy.** Phải lấy **cả hai**: chữ hiển thị vùng phân trang **và**
  `total`/`total_count` trong thân phản hồi. Lệch nhau → **Chưa chốt**, không tự chọn con số thuận lợi.
- **(l) Chữ người dùng nhìn thấy đọc bằng `innerText`, KHÔNG `textContent`.**
- **(m) Thông báo tự tắt.** Dùng `tools/toast-capture.js` cài **TRƯỚC** khi bấm, **cấm lọc trùng**, đếm kèm
  số lời gọi mạng; **không bấm lại chỉ để chụp lại**.
- **(n) 🔴 Trang cũ / bản dựng cũ / kết luận mượn từ env nội bộ.** Ô "Kết quả verify" của dòng này đã có nội
  dung nhưng **đo trên env nội bộ**; ảnh `DEV-…-V108.png` cũng là env nội bộ. **Cấm chép**. Phải tải lại
  trang và ghi bản dựng đọc trên UI của chính env đối tác.
- **(o) Hai phép đo mâu thuẫn = CHƯA được chốt.** Ghi cả hai, hỏi lead.

---

## 8. Điểm KHÁC NHAU với QLKTLBG_18 / QLKTLBG_20 — cấm suy verdict chéo

| | QLKTLBG_18 | **QLKTLBG_19** (file này) | QLKTLBG_20 |
|---|---|---|---|
| Điều kiện lọc | **Có** lọc, cho ra tập con | **Không đặt** lọc (phải chủ động Xóa bộ lọc) | **Có** lọc, cố ý **0 kết quả** |
| Tập dữ liệu lúc bấm | 0 < N < tổng | **= tổng** | 0 |
| Vế nội dung | Tệp = đúng tập lọc | **Tệp = toàn bộ danh sách** | Tệp rỗng **HOẶC** thông báo không có dữ liệu |
| Quan hệ với SRS | MATCH toàn bộ | **MATCH toàn bộ (không có GAP)** | C1/C2a MATCH · **C2b GAP → BA** |
| Ca PASS-oan nguy hiểm nhất | Tệp chứa toàn bộ (bỏ qua lọc) | **Tệp chỉ chứa trang đang xem (20 dòng)** | Tệp "rỗng" thực ra chứa toàn bộ |
| Có nhánh phải chuyển BA? | Không | **Không** | **Có** (C2b) |

**Chỉ có C1 là chung** — và vẫn phải **tự quan sát lại trong từng case**, ghi riêng cho từng case. C2 tuyệt
đối không suy chéo: hệ thống có thể xuất đúng theo bộ lọc (case 18 Pass) mà vẫn cắt tệp theo trang khi không
lọc (case 19 Fail), và ngược lại.

---

## 9. Bảng quyết định đã cam kết TRƯỚC khi đo

| Quan sát khi đo | Verdict logic |
|---|---|
| Không tìm thấy chức năng Xuất Excel (sau khi đã liệt kê DOM + menu phụ + `/api/docs-json`) | **Reopen** (C1 không đạt) |
| Có chức năng; tệp mở được; **số dòng dữ liệu = tổng bản ghi màn báo** (tổng ≤ 10.000) | **Pass** |
| Có chức năng; tệp chỉ chứa **trang đang xem** (số dòng = số dòng/trang, tổng lớn hơn) | **Reopen** (C2 không đạt) |
| Có chức năng; tệp **thiếu/thừa dòng** so với tổng, không giải thích được bằng đặc tả | **Reopen** (C2 không đạt) |
| Có chức năng; bấm ra lỗi 4xx/5xx, **không có tệp** | **Reopen** (C1 không đạt trên thực tế) |
| Tệp thiếu/thừa cột, khác thứ tự cột, tên tệp lạ, không có toast | **KHÔNG chấm Fail vì các điểm này** (SRS Nhóm III im lặng) — ghi 1 dòng candidate nếu đáng lưu ý |
| Tổng bản ghi ≤ số dòng/trang, không dựng được T4 | **Chưa chốt** hoặc Pass-có-giới-hạn **chỉ khi** đã hạ số dòng/trang xuống 10 và vẫn phân biệt được; nếu không phân biệt được thì ghi rõ giới hạn, **không Pass suông** |
| Chưa xác nhận được bộ lọc đã rỗng (T2) | **Chưa chốt** — phép đo không nói về case này |
| Hai phép đo mâu thuẫn (tổng màn báo vs `total_count` vs số dòng tệp) | **Chưa chốt** — ghi cả ba, hỏi lead |
