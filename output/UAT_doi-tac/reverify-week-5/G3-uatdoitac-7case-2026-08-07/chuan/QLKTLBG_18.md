# CHUẨN CHẤM — QLKTLBG_18 (Lô G3 · khoá TRƯỚC khi đo)

> **Chưa mở màn.** File này khoá chuẩn chấm TRƯỚC khi đo. Sau khi đo, CẤM sửa quan hệ `MATCH / GAP` hay
> đổi tiêu chí Pass/Reopen để khớp kết quả quan sát được.

## 1. Bảng đầu

| Mục | Giá trị |
|---|---|
| Bảng / tab / dòng | Bảng đối tác · tab `bug` · **dòng 12** |
| Mã TC | **QLKTLBG_18** |
| Mô tả (đối tác) | "Xuất Excel với điều kiện lọc" |
| Trạng thái nguồn | Trạng thái `Fail` · Trạng thái dev fix `Test done` · Kết quả verify **TRỐNG** |
| TKM phản hồi lần 1 | "Màn hình không có nút chức năng" |
| Env | **`https://htpldn-uat.ospgroup.vn`** (env NGHIỆM THU của đối tác) — MailHog `https://htpldn-uat.ospgroup.vn/mailhog/` |
| Bản dựng | **(để trống — đọc trên UI khi đo)**; bắt buộc tải lại trang rồi mới ghi số hiệu ở sidebar/chân trang |
| Tài khoản dự kiến | `cbnv_tw` / `Test@1234` (vai trò `CB_NV_TW`, cấp TW). OTP lấy ở MailHog của **chính env này**. Giới hạn đăng nhập 5 lượt/60 giây |
| Vai trò theo đặc tả | **CB NV** (hoặc CB PD) — `srs-fr-03-dao-tao.md:751` ("**Tác nhân:** CB NV / CB PD" — FR-III-07) và `:828` (FR-III-08); quyền PRE-01 `:757` ("có quyền \"Quản lý tài liệu ĐT\"") |
| Màn | Đào tạo, tập huấn → **Kho tài liệu / Bài giảng** → Danh sách (**SCR-III-03**) |
| URL | `https://htpldn-uat.ospgroup.vn/dao-tao/bai-giang/danh-sach` — **đã có bằng chứng trên chính env đối tác** (thanh địa chỉ trong ảnh `QLKTLBG_18.jpg`), không phải suy đoán |
| SRS đã đọc | `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-03-dao-tao.md` — **2296 dòng** |
| SRS đã đọc | `Docs-PM-HTPLDN/…/srs-v3.5/srs-v3.5.md` — **7012 dòng** |
| SRS đã đọc (tiền lệ module khác) | `srs-fr-13-tv-nhanh.md` — **932 dòng** · `srs-fr-15-ct-htpldn.md` — **1610 dòng** · `srs-fr-11-bao-cao.md` — **1295 dòng** |

---

## 2. Nguồn đã đọc (tự mở trong lượt này)

**SRS nguồn chuẩn DUY NHẤT — `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/`:**

| File | Đoạn đã đọc trọn | Nội dung |
|---|---|---|
| `srs-fr-03-dao-tao.md` | `:744–818` | **FR-III-07 (UC26) trọn mục** — Preconditions `:753–757`, Inputs, Processing, Outputs, **Error Handling `:803–809`**, AC `:811–815` |
| `srs-fr-03-dao-tao.md` | `:821–877` | **FR-III-08 (UC27) trọn mục** — Inputs bộ lọc `:836–845`, Processing `:847–853`, Outputs `:855–866`, AC `:870–874`. **Mục này KHÔNG có bảng Error Handling** |
| `srs-fr-03-dao-tao.md` | `:1941–1984` | **SCR-III-03 trọn mục** — 6 Thành phần + Quy tắc nghiệp vụ |
| `srs-fr-03-dao-tao.md` | `:2227–2252` | §6 Tổng quan BR sử dụng (gồm dòng `:2243` BR-DATA-06) |
| `srs-v3.5.md` | `:5561–5574` | Phụ lục B.2 BR-DATA (trọn bảng, gồm **BR-DATA-06 `:5570`**) |
| `srs-v3.5.md` | `:861` | EC-DATA-PAGE — ràng buộc phân trang |
| `srs-fr-13-tv-nhanh.md` | `:148–157` | Bảng Error Handling — **tiền lệ module khác** về xuất Excel khi lọc rỗng |
| `srs-fr-15-ct-htpldn.md` | `:398–412` | Bảng Error Handling + AC — **tiền lệ module khác**, xử lý KHÁC module trên |
| `srs-fr-11-bao-cao.md` | `:1281–1285` | Bản sao BR-DATA-06 trong nhóm IX (đối chiếu, không phải căn cứ cho nhóm III) |

**Quét từ đồng nghĩa đã chạy** (nhiều lệnh, không chỉ 1 grep) trên `srs-fr-03-dao-tao.md` và **toàn thư mục**
`srs-v3.5/`: `Xuất Excel` · `xuất excel` · `Xuất file` · `kết xuất` · `export` · `xuất tệp` · `xuất danh sách` ·
`tải xuống` · `Tải về` · `tiêu chí lọc` · `bộ lọc hiện tại` · `BR-DATA-06` · `danh sách rỗng` ·
`không có dữ liệu` · `tải lên` · `import` · `tệp mẫu`.

**Ngữ cảnh (CHỈ để biết tra chỗ nào — KHÔNG dùng làm căn cứ verdict, không mượn số dòng):**
`output/UAT_doi-tac/flowtest-2026-08-05/partner-evidence/QLKTLBG_18.jpg` (ảnh đối tác — xem §3) ·
`output/UAT_doi-tac/flowtest-2026-08-05/evidence/DEV-QLKTLBG_18-nut-xuat-excel-loc-slide-V108.png` (ảnh
chụp **trên env nội bộ**, bản dựng `V1.0.8` — **KHÔNG** dùng để kết luận cho env đối tác) ·
`output/UAT_doi-tac/bug-con-fail-doi-tac-2026-07-31.md:334`.

---

## 3. Cổng bằng chứng

- **CÓ bằng chứng đối tác** — `partner-evidence/QLKTLBG_18.jpg`, **đã mở ảnh ra xem**.
- **Mô tả lại nội dung ảnh (nguyên trạng, không diễn giải thêm):**
  - Thanh địa chỉ trình duyệt: `htpldn-uat.ospgroup.vn/dao-tao/bai-giang/danh-sach` → **đúng env đối tác**,
    **đúng màn** SCR-III-03. Đây là căn cứ để §1 ghi URL mà không phải đoán.
  - Sidebar góc trái ghi bản dựng **`HTPLDN · V1.0`**. Đồng hồ hệ điều hành trong ảnh: **08:51 ngày
    2026-07-25** → ảnh chụp **trước** bản dựng hiện tại của env (`Last-Modified` bó mã FE 2026-08-07).
  - Người dùng đang đăng nhập: **"Cán bộ NV Trung ương · CB_NV_TW"** → đúng vai trò đặc tả (`:751`).
  - Vùng tiêu đề *"Kho tài liệu / Bài giảng"* chỉ có **2 nút**: **`+ Thêm mới`** và **`Làm mới`**. **Không
    thấy nút "Xuất Excel"** — khớp câu TKM *"Màn hình không có nút chức năng"*.
  - Thanh lọc hiển thị: ô *"Tìm theo tên bài giảng"*, `Loại tài liệu`, `Lĩnh vực pháp lý`, `Công khai`, chip
    **`Bộ lọc nâng cao (2)`**, nút `Xóa bộ lọc` và `Tìm kiếm`.
  - Bảng có dữ liệu (Video/PDF/Slide, cột Dung lượng · Ngày tạo · Công khai · Thao tác với 3 biểu tượng).
- **Ảnh chứng minh điều gì / KHÔNG chứng minh điều gì:** ảnh chứng minh **tại bản dựng `V1.0` ngày
  2026-07-25** màn này không có nút Xuất Excel. Ảnh **KHÔNG** nói gì về bản dựng hiện tại — nên **vẫn phải
  đo lại thật**, cấm chép kết luận từ ảnh và cấm chép kết luận từ ảnh chụp env nội bộ.
- **Vì sao tái hiện được:** đúng 2 bước, không cần tiền đề đặc biệt, không cần ID bản ghi của đối tác. Điều
  kiện duy nhất — "nhập tiêu chí lọc" — QA tự dựng được (§6 T3).
- **Điều kiện tái hiện sẽ ghi vào báo cáo:** env + bản dựng đọc trên UI · tài khoản thực dùng · URL màn ·
  **giá trị lọc cụ thể đã nhập** · **tổng số bản ghi màn hiện sau khi lọc** ngay trước khi bấm Xuất Excel.
- **Không đụng dữ liệu đối tác** — chỉ lọc, không sửa/xóa bản ghi nào.

---

## 4. Bảng chuẩn chấm

**Expected đối tác (nguyên văn):** *"Hệ thống xuất danh sách bài giảng theo điều kiện lọc hiện tại ra tệp Excel."*

| # | Điều kiện của BUG GỐC | Đặc tả nói gì (file:dòng, nguyên văn) | Phép đo quyết định | Pass khi | Reopen khi |
|---|---|---|---|---|---|
| **B1** | Bước 2 của phiếu — *"…nhấn Xuất excel"* — **thực hiện được**: màn Kho tài liệu / Bài giảng phải có chức năng Xuất Excel. Triệu chứng TKM: *"Màn hình không có nút chức năng"* | **MATCH.** `srs-fr-03-dao-tao.md:1952` — *"Nút \"Xuất Excel\" (phụ): xuất danh sách theo bộ lọc hiện tại, tối đa 10.000 dòng (BR-DATA-06)"* · `srs-v3.5.md:5570` — *"**Export Excel:** Mọi danh sách có tính năng xuất Excel…"*, cột "Áp dụng FR" = *"Toàn bộ CRUD list"* | Liệt kê DOM vùng tiêu đề + thanh công cụ: mảng `{tag, innerText, title, ariaLabel, className, disabled}` của mọi `button`/`a`/`[role=button]`; mở mọi menu phụ rồi lặp lại. Đối chứng độc lập: `paths` chứa `bai-giang` ở `/api/docs-json`, lọc `export`/`excel`/`xuat` — **CẤM đoán đường dẫn** | Màn có chức năng Xuất Excel dùng được (bấm được, sinh ra lời gọi tải tệp) | Đã liệt kê DOM + menu phụ + `/api/docs-json` mà **không có** chức năng xuất danh sách nào ở thanh công cụ |
| **B2** | Vế nội dung — tệp xuất phải **theo đúng điều kiện lọc đang áp dụng**: chỉ chứa bản ghi khớp bộ lọc, và chứa **đủ** mọi bản ghi khớp (không chỉ trang đang xem) | **MATCH.** `srs-fr-03-dao-tao.md:1952` — *"xuất danh sách **theo bộ lọc hiện tại**"* · `srs-v3.5.md:5570` — *"File xuất **theo bộ lọc hiện tại**, không vượt quá 10,000 rows/file"* · `srs-fr-03-dao-tao.md:1908` (cùng nhóm, màn SCR-III-01) — *"Xuất Excel tối đa 10.000 dòng theo bộ lọc hiện tại"* | Đặt **1 bộ lọc cho ra tập con nhỏ hơn tổng** (§6 T3) → bấm Tìm kiếm → **ghi lại tổng số bản ghi màn báo** (đọc `innerText` vùng phân trang **và** `total`/`total_count` trong thân phản hồi danh sách) → bấm Xuất Excel 1 lần → **MỞ TỆP** bằng `openpyxl` đếm số dòng dữ liệu (tổng dòng − dòng tiêu đề) và soi giá trị cột tương ứng tiêu chí lọc | Số dòng dữ liệu trong tệp **=** tổng bản ghi màn báo sau khi lọc, **và** mọi dòng đều khớp tiêu chí lọc đã đặt | Tệp chứa **toàn bộ** danh sách (bỏ qua bộ lọc); hoặc tệp chỉ chứa **trang đang xem** (vd 20 dòng trong khi tổng lớn hơn); hoặc tệp chứa dòng **không khớp** tiêu chí lọc |

### Trích nguyên văn SRS dưới từng vế

**B1 — `srs-fr-03-dao-tao.md:1949–1952` (Thành phần 2 của SCR-III-03, trọn khối):**

```
**Thành phần 2 — Tiêu đề + Hành động chính:**
- Tiêu đề trang: "Kho tài liệu & bài giảng"
- Nút "+ Thêm mới" (chính): mở biểu mẫu thêm bài giảng
- Nút "Xuất Excel" (phụ): xuất danh sách theo bộ lọc hiện tại, tối đa 10.000 dòng (BR-DATA-06)
```

> Đối chiếu với ảnh đối tác: khối này liệt kê **2 nút** (Thêm mới, Xuất Excel) và **không** có "Làm mới";
> ảnh lại có "Thêm mới" + "Làm mới" mà thiếu "Xuất Excel". Nút "Làm mới" thừa so với đặc tả **không thuộc
> phạm vi phiếu này** — nếu thấy, ghi 1 dòng candidate, không mở rộng case.

**B1 + B2 — `srs-v3.5.md:5570`** (Phụ lục B.2, BR-DATA-06; header cột ở `:5563` =
`| ID | Phát biểu quy tắc | Nguồn | Áp dụng FR | Ngoại lệ | Kiểm chứng |`):

```
| BR-DATA-06 | **Export Excel:** Mọi danh sách có tính năng xuất Excel. File xuất theo bộ lọc hiện tại, không vượt quá 10,000 rows/file | Pattern IP-01 | Toàn bộ CRUD list | Báo cáo nhóm IX có xuất PDF theo khung TT 17/2025 | Test export limit |
```

**B2 — `srs-fr-03-dao-tao.md:1954–1960` (Thành phần 3 — bộ lọc dùng để dựng ca "có điều kiện lọc"):**

```
**Thành phần 3 — Thanh lọc và tìm kiếm:**
- Ô từ khóa: "Tìm theo tên bài giảng"
- Lọc Loại tài liệu: Tất cả / Slide / PDF / Video
- Lọc Lĩnh vực pháp luật (chọn nhiều — nguồn DANH_MUC loại LINH_VUC_PL)
- Lọc Công khai: Tất cả / Đã công khai / Chưa công khai `[STT66 UAT 2026-06-02]`
- Lọc Từ ngày / Đến ngày (theo ngày tạo)
- Nút "Tìm kiếm" (chính) · "Xóa bộ lọc" (mờ)
```

**B2 — `srs-fr-03-dao-tao.md:1976` (phân trang — nguồn của bẫy "tệp chỉ có 20 dòng"):**

```
**Thành phần 5 — Phân trang:** mặc định 20 dòng/trang; cho phép 10/20/50/100.
```

**B2 phạm vi dữ liệu — `srs-fr-03-dao-tao.md:1981`:**

```
- Danh sách lọc theo đơn vị sở hữu (`don_vi_id`) theo BR-AUTH-08.
```

### 🔴 Trả lời câu hỏi then chốt

> **SRS có quy định màn Kho tài liệu / Bài giảng phải có chức năng Xuất Excel không?**

**CÓ — quy định rõ, ở cấp màn hình.** `:1952` liệt kê "Xuất Excel" là Hành động chính của SCR-III-03 và dẫn
thẳng BR-DATA-06; BR-DATA-06 (`srs-v3.5.md:5570`) phát biểu *"Mọi danh sách có tính năng xuất Excel"*, Áp
dụng FR = *"Toàn bộ CRUD list"*, ngoại lệ duy nhất là *Báo cáo nhóm IX*. ⇒ **B1 MATCH · thiếu chức năng =
Reopen.**

> **SRS có quy định tệp xuất phải theo bộ lọc không?**

**CÓ — hai chỗ độc lập** cùng dùng đúng cụm *"theo bộ lọc hiện tại"* (`:1952` và `srs-v3.5.md:5570`).
⇒ **B2 MATCH.**

### ⚠️ Đã cân nhắc và LOẠI khả năng "SRS im lặng"

Bảng §6 tại `srs-fr-03-dao-tao.md:2243` ghi `| BR-DATA-06 | Export Excel | FR-III-01, FR-III-05, FR-III-06,
FR-III-14 |` — **không liệt kê FR-III-07/FR-III-08**. **Không phải mệnh đề ngoại lệ:** đó là bảng mục lục
tham chiếu chéo cấp FR (cột 3 tên *"FR áp dụng (trong nhóm này)"*), không dùng từ "không áp dụng"; ngoại lệ
của BR-DATA-06 nằm ở **cột "Ngoại lệ" của chính BR** (`srs-v3.5.md:5570`) và chỉ có *Báo cáo nhóm IX*; đặc
tả cấp màn (`:1952`) nói rõ màn này CÓ nút và **là căn cứ nghiệm thu** (`:1945` — *"Bảng cột đã nội hóa
xuống dưới — khi hai bên khác nhau thì lấy mục này làm căn cứ nghiệm thu"*). → **Không đổi quan hệ B1.**
Ghi **1 dòng candidate tài liệu** (không phải bug phần mềm): *"Bảng §6 `:2243` thiếu FR-III-07/FR-III-08 ở
dòng BR-DATA-06."*

---

## 5. Đường đo tối thiểu

**Một đường UI ngắn nhất + một đối chứng độc lập. Bấm Xuất Excel đúng 1 lần.**

| Bước | Nội dung | Kiểm vế |
|---|---|---|
| U0 | Đăng nhập `cbnv_tw` trên `https://htpldn-uat.ospgroup.vn` (OTP MailHog cùng env), **tải lại trang**, ghi số hiệu bản dựng | tiền đề |
| U1 | (Phiếu bước 1) Chọn menu **"Đào tạo, tập huấn" → "Kho tài liệu / Bài giảng"**; xác nhận URL `…/dao-tao/bai-giang/danh-sach` | tiền đề |
| U2 | **Bấm "Xóa bộ lọc"** rồi Tìm kiếm → ghi **tổng bản ghi khi không lọc** (làm mốc so sánh cho B2) | tiền đề T2 |
| U3 | Liệt kê DOM vùng tiêu đề + thanh công cụ (`innerText` + `title` + `aria-label` + `className` + `disabled`); mở mọi menu phụ rồi lặp lại | **B1** |
| U4 | (Phiếu bước 2a) **Nhập tiêu chí lọc** đã chọn ở §6 T3 → bấm **"Tìm kiếm"** | tiền đề T3 |
| U5 | **Xác nhận bộ lọc đã áp dụng**: đọc `innerText` vùng phân trang + `total`/`total_count` trong thân phản hồi danh sách. Số này phải **nhỏ hơn** mốc U2. Chưa xác nhận thì **CẤM bấm xuất** | tiền đề T4 |
| U6 | Cài `output/UAT_doi-tac/tools/toast-capture.js` **TRƯỚC** khi bấm | phụ trợ |
| U7 | (Phiếu bước 2b) Bấm **Xuất Excel** (UI thật, **1 lần**) | **B1** |
| U8 | Ghi: có/không tệp tải về · nguyên văn thông báo bắt được · số lời gọi mạng kèm theo · mã trạng thái lời gọi xuất | **B1** |
| Đối chứng độc lập | **MỞ TỆP**: `openpyxl.load_workbook(path, read_only=True)` → đếm số dòng dữ liệu (tổng dòng − dòng tiêu đề) + đọc giá trị cột tương ứng tiêu chí lọc của **mọi** dòng | **B2** |
| Đối chứng độc lập | `fetch('/api/docs-json')` → `paths` chứa `bai-giang`, lọc `export`/`excel`/`xuat`. **CẤM tự đoán đường dẫn** | **B1** |

**Lấy tệp về để mở — thử theo thứ tự, dừng khi được:** (1) kiểm `~/Downloads`; (2) nếu trình duyệt điều khiển
bằng công cụ không đổ tệp ra đĩa → đọc nội dung **ngay trong trang**: `fetch` lại **đúng** URL tệp mà lời gọi
tải đã dùng (lấy từ `list_network_requests`, **không đoán**) → parse EOCD + `DecompressionStream`, chỉ trả về
số dòng + giá trị cột cần đo; (3) giữ lại đường dẫn tệp để verdict truy lại được.

B1 không đạt ⇒ **B2 không đo được** — ghi rõ bị chặn bởi B1, **không** suy đoán hệ thống "sẽ" làm gì.

🔴 **CẤM dừng ở "tải được tệp".** HTTP 200 + dữ liệu nhị phân chỉ chứng minh CREATE, không chứng minh CORRECT.

---

## 6. Tiền đề phải dựng

| # | Tiền đề | Vì sao bắt buộc (dòng SRS) | Cách dựng nếu thiếu |
|---|---|---|---|
| **T1** | Tài khoản vai trò **CB NV** | `:751` tác nhân FR-III-07 · `:828` tác nhân FR-III-08 · `:757` quyền "Quản lý tài liệu ĐT" | `cbnv_tw` / `Test@1234` + OTP MailHog env đối tác. Env này **chưa xác nhận có tài khoản anh em** `cbnv_tw_02/_03` → khoá lock thì **DỪNG, báo lead**, cấm đổi vai trò/cấp |
| **T2** | Màn có **≥2 bản ghi** và tập khớp bộ lọc phải **nhỏ hơn tổng** | Nếu tập lọc = tổng thì không phân biệt được "xuất theo bộ lọc" với "xuất tất cả" ⇒ phép đo **không nói được gì** về B2 | Ảnh đối tác cho thấy màn có nhiều loại tài liệu (Video/PDF/Slide) → nhiều khả năng đủ. Nếu tổng ≤1 hoặc mọi bản ghi cùng một loại → **thêm 1 bài giảng QA** (`+ Thêm mới`, tên có dấu `QA` + ngày) để tạo tương phản, và **khai rõ đã tạo gì** trong nhật ký đo |
| **T3** | **Một bộ lọc có kết quả nhưng KHÔNG phải toàn bộ** | Đây chính là chữ *"điều kiện lọc"* trong phiếu | Ưu tiên **Lọc Loại tài liệu = một giá trị cụ thể** (Slide **hoặc** PDF **hoặc** Video — `:1956`) vì kiểm chứng lại trong tệp rất dễ (soi cột Loại tài liệu). **Không dùng lọc ngày** (phụ thuộc dữ liệu, khó đối chiếu). Ghi lại giá trị lọc thực dùng |
| **T4** | **Biết chắc tổng bản ghi sau khi lọc** trước khi bấm xuất | Không có con số này thì không chấm được B2 | Đọc `innerText` vùng phân trang **và** `total`/`total_count` trong thân phản hồi danh sách; hai nguồn phải khớp |
| **T5** | Bộ lọc thực sự **đã được áp dụng**, không chỉ "đã gõ vào ô" | Đặc tả có nút "Tìm kiếm" riêng (`:1960`) ⇒ gõ xong chưa chắc đã lọc | Bấm **"Tìm kiếm"** rồi mới đọc lại tổng ở U5 |
| **T6** | Ghi **env + bản dựng** sau khi tải lại trang | Luật 4 BRIEF | Đọc ở sidebar/chân trang (ảnh đối tác cho thấy vị trí này hiển thị `HTPLDN · V1.0`) |

**Không đụng dữ liệu đối tác** — chỉ lọc và xuất; nếu buộc phải thêm bản ghi để dựng T2 thì khai đủ:
**thêm bản ghi nào · đặt tên gì · env nào**.

---

## 7. Bẫy đã biết

**Chặn FAIL oan:**

- **(a) 🔴 Chip "Bộ lọc nâng cao (2)" hiện sẵn KHÔNG phải là bộ lọc đang áp dụng.** Ảnh đối tác cho thấy chip
  này hiện ngay khi vào màn. Con số `(2)` là **số ô lọc nâng cao có sẵn**, không có nghĩa "đang có 2 điều
  kiện lọc". Đừng vì thấy chip mà tưởng đã lọc — luôn bấm **"Xóa bộ lọc"** lấy mốc U2 rồi mới đặt lọc thật.
- **(b) Nút có thể nằm trong menu phụ / là biểu tượng không nhãn.** CẤM kết luận "không có nút" bằng mắt qua
  ảnh chụp. Phải liệt kê `innerText` **cộng** `title`/`aria-label`/`className` của mọi
  `button`/`a`/`[role=button]`, và mở thử menu phụ trước khi chốt B1.
- **(c) 🔴 Biểu tượng ở cột "Thao tác" từng dòng ≠ nút xuất danh sách.** `:1974` — *"Hành động | — | Xem trực
  tuyến · **Tải về (chỉ Slide/PDF)** · Sửa · Xóa"*. Ảnh đối tác cho thấy 3 biểu tượng ở cột này. **"Tải về"
  là tải tệp bài giảng của MỘT dòng**, không phải xuất danh sách. B1 đo ở **thanh công cụ đầu màn**.
- **(d) SRS Nhóm III không quy định bộ cột tệp xuất SCR-III-03.** FR-III-07 (`:744–818`) và FR-III-08
  (`:821–877`) không có mục "Processing — Xuất Excel" (khác FR-III-01 `:180–184` và FR-III-05 `:599–605`).
  ⇒ **CẤM chấm Fail vì thiếu/thừa cột, sai thứ tự cột, sai tên sheet, hay tên tệp.**
- **(e) SRS không quy định câu chữ thông báo sau khi xuất ở màn này.** CẤM chấm Fail vì không có toast, hoặc
  toast khác chữ.
- **(f) Đổi vai trò để "cho ra nút".** Nếu B1 không đạt, CẤM đăng nhập `admin` rồi kết luận Pass — vai trò
  của vế là **CB NV** (`:751`).
- **(g) Bản ghi ngoài phạm vi đơn vị không có trong tệp.** `:1981` — danh sách lọc theo `don_vi_id` (BR-AUTH-08).
  Mốc so sánh của B2 là **tổng màn báo cho tài khoản đang đăng nhập**, không phải toàn bộ dữ liệu hệ thống.

**Chặn PASS oan:**

- **(h) 🔴 "Tải được tệp" ≠ "nội dung đúng".** Bắt buộc mở tệp bằng `openpyxl`. Tệp chứa **toàn bộ** bản ghi
  (bỏ qua bộ lọc) là **B2 KHÔNG đạt** — đây là ca PASS-oan nguy hiểm nhất của case này.
- **(i) 🔴 Tệp chỉ chứa trang đang xem.** `:1976` — mặc định 20 dòng/trang. Nếu tập lọc >20 mà tệp đúng 20
  dòng thì **B2 không đạt**. Nên chủ động chọn bộ lọc cho tập **>20** nếu dữ liệu cho phép; không đủ dữ liệu
  thì ghi rõ giới hạn của phép đo trong nhật ký (không âm thầm bỏ qua).
- **(j) Đếm nhầm dòng tiêu đề.** Số dòng dữ liệu = tổng dòng − dòng tiêu đề. Ghi cả hai con số.
- **(k) Chữ người dùng nhìn thấy đọc bằng `innerText`, KHÔNG `textContent`** — `textContent` gom cả node ẩn
  → báo "có nút" trong khi nút đang ẩn.
- **(l) Thông báo tự tắt.** Dùng `tools/toast-capture.js` cài **TRƯỚC** khi bấm, **cấm lọc trùng**, đếm kèm
  số lời gọi mạng. Không bắt được → dùng **thân phản hồi** của lời gọi xuất làm bằng chứng mạnh hơn ảnh;
  **không bấm lại chỉ để chụp lại**.
- **(m) 🔴 Trang cũ / bản dựng cũ / kết luận mượn từ env nội bộ.** Ảnh `DEV-…-V108.png` là **env nội bộ**,
  bản dựng `V1.0.8` — **không** dùng làm căn cứ cho env đối tác. Phải **tải lại trang** và **ghi bản dựng**
  đọc trên UI của chính env đối tác.
- **(n) Hai phép đo mâu thuẫn = CHƯA được chốt.** Ví dụ màn báo 3 bản ghi nhưng tệp có 12 dòng → ghi cả hai,
  hỏi lead.

---

## 8. Điểm KHÁC NHAU với QLKTLBG_19 / QLKTLBG_20 — cấm suy verdict chéo

Ba case **cùng màn** (`…/dao-tao/bai-giang/danh-sach`), **cùng câu triệu chứng TKM**, nhưng **khác vế đo**.
Cấm đo 1 case rồi suy cho 2 case còn lại.

| | **QLKTLBG_18** (file này) | QLKTLBG_19 | QLKTLBG_20 |
|---|---|---|---|
| Điều kiện lọc | **Có** lọc, cho ra **tập con** | **Không đặt** lọc | **Có** lọc, cố ý **0 kết quả** |
| Tập dữ liệu lúc bấm | 0 < N < tổng | = tổng | 0 |
| Vế nội dung | Tệp = **đúng tập lọc** | Tệp = **toàn bộ** danh sách | Tệp rỗng **HOẶC** thông báo không có dữ liệu |
| Quan hệ với SRS | B1 MATCH · B2 MATCH | MATCH toàn bộ | C1/C2a MATCH · **C2b GAP → BA** |
| Ca PASS-oan nguy hiểm nhất | Tệp chứa **toàn bộ** (bỏ qua lọc) | Tệp chỉ chứa **trang đang xem** | Tệp "rỗng" thực ra chứa toàn bộ |

**Chỉ có B1 là chung** — và vẫn phải **tự quan sát lại trong từng case**, ghi riêng cho từng case. B2 tuyệt
đối không suy chéo: hệ thống có thể xuất đúng toàn bộ danh sách (case 19 Pass) mà vẫn bỏ qua bộ lọc (case 18
Fail) — đó chính là hai lỗi ngược chiều nhau.

---

## 9. Bảng quyết định đã cam kết TRƯỚC khi đo

| Quan sát khi đo | Verdict logic |
|---|---|
| Không tìm thấy chức năng Xuất Excel (sau khi đã liệt kê DOM + menu phụ + `/api/docs-json`) | **Reopen** (B1 không đạt) |
| Có chức năng; tệp mở được; **số dòng dữ liệu = tổng bản ghi màn báo sau khi lọc** và mọi dòng khớp tiêu chí | **Pass** |
| Có chức năng; tệp chứa **toàn bộ** danh sách / có dòng **không khớp** tiêu chí lọc | **Reopen** (B2 không đạt — vi phạm *"theo bộ lọc hiện tại"*, `:1952` + `srs-v3.5.md:5570`) |
| Có chức năng; tệp chỉ chứa **trang đang xem** (vd 20 dòng, tổng lớn hơn) | **Reopen** (B2 không đạt) |
| Có chức năng; bấm ra lỗi 4xx/5xx, **không có tệp** | **Reopen** (B1 không đạt trên thực tế) |
| Tệp thiếu/thừa cột, khác thứ tự cột, tên tệp lạ, không có toast | **KHÔNG chấm Fail vì các điểm này** (SRS Nhóm III im lặng) — ghi 1 dòng candidate nếu đáng lưu ý |
| Không dựng được T2/T3 (không đủ dữ liệu để tập lọc nhỏ hơn tổng) | **Chưa chốt** — nêu rõ dữ kiện còn thiếu, **CẤM Pass** |
| Hai phép đo mâu thuẫn (tổng màn báo vs số dòng trong tệp không giải thích được) | **Chưa chốt** — ghi cả hai, hỏi lead |
