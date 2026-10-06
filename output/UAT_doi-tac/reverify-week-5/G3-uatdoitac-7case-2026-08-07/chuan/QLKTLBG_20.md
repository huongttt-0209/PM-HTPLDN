# CHUẨN CHẤM — QLKTLBG_20 (Lô G3 · khoá TRƯỚC khi đo)

> **Chưa mở màn.** File này khoá chuẩn chấm TRƯỚC khi đo. Sau khi đo, CẤM sửa quan hệ `MATCH / GAP` hay
> đổi tiêu chí Pass/Reopen để khớp kết quả quan sát được.
>
> ⚠️ Ô "Kết quả verify" của dòng này **đã có nội dung, nhưng đo trên env NỘI BỘ**. Lô G3 là lượt xác nhận
> lại trên env đối tác — **cấm chép kết luận cũ**, phải đo lại thật.

## 1. Bảng đầu

| Mục | Giá trị |
|---|---|
| Bảng / tab / dòng | Bảng đối tác · tab `bug` · **dòng 14** |
| Mã TC | **QLKTLBG_20** |
| Mô tả (đối tác) | "Xuất Excel với điều kiện lọc không có kết quả" |
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
| SRS đã đọc (tiền lệ module khác) | `srs-fr-13-tv-nhanh.md` — **932 dòng** · `srs-fr-15-ct-htpldn.md` — **1610 dòng** · `srs-fr-11-bao-cao.md` — **1295 dòng** |

---

## 2. Nguồn đã đọc (tự mở trong lượt này)

**SRS nguồn chuẩn DUY NHẤT — `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/`:**

| File | Đoạn đã đọc trọn | Nội dung |
|---|---|---|
| `srs-fr-03-dao-tao.md` | `:744–818` | **FR-III-07 (UC26) trọn mục**, gồm **Error Handling `:803–809`** (chỉ 3 dòng, đều về tải tệp bài giảng) |
| `srs-fr-03-dao-tao.md` | `:821–877` | **FR-III-08 (UC27) trọn mục** — **KHÔNG có bảng Error Handling**; đi thẳng từ Postconditions `:868` sang AC `:870` |
| `srs-fr-03-dao-tao.md` | `:1941–1984` | **SCR-III-03 trọn mục** — 6 Thành phần + Quy tắc nghiệp vụ |
| `srs-fr-03-dao-tao.md` | `:1912–1937` | SCR-III-02 — đối chứng: màn cùng nhóm **CÓ** mục trạng thái rỗng (`:1921`, `:1922`, `:1927`) |
| `srs-fr-03-dao-tao.md` | `:2227–2252` | §6 Tổng quan BR sử dụng (gồm `:2243`) |
| `srs-v3.5.md` | `:5561–5574` | Phụ lục B.2 BR-DATA (trọn bảng, gồm **BR-DATA-06 `:5570`**) |
| `srs-v3.5.md` | `:861` | EC-DATA-PAGE |
| `srs-fr-13-tv-nhanh.md` | `:148–157` | Bảng Error Handling — **tiền lệ module khác** về xuất Excel khi lọc rỗng |
| `srs-fr-15-ct-htpldn.md` | `:398–412` | Bảng Error Handling + AC — **tiền lệ module khác**, xử lý KHÁC module trên |

**Quét từ đồng nghĩa đã chạy** (nhiều lệnh, không chỉ 1 grep) trên `srs-fr-03-dao-tao.md` và **toàn thư mục**
`srs-v3.5/`: `Xuất Excel` · `xuất excel` · `kết xuất` · `export` · `xuất tệp` · `xuất danh sách` · `Tải về` ·
`tiêu chí lọc` · `bộ lọc hiện tại` · `BR-DATA-06` · **`danh sách rỗng`** · **`không có dữ liệu`** ·
`Không có dữ liệu để xuất` · `0 bản ghi` · `Không tìm thấy` · `Chưa có dữ liệu` · `trạng thái trống` ·
`Empty state`.

**Kết quả quét đáng chú ý:** trong toàn thư mục `srs-v3.5/`, cụm *"Không có dữ liệu để xuất"* chỉ có ở
`srs-fr-13-tv-nhanh.md:155`; cụm *"không có dữ liệu"* gắn với xuất Excel chỉ có ở `srs-fr-15-ct-htpldn.md:403`
và `:409`. **Nhóm III (`srs-fr-03-dao-tao.md`) không có dòng nào.**

**Ngữ cảnh (CHỈ để biết tra chỗ nào — KHÔNG dùng làm căn cứ verdict, không mượn số dòng):**
`output/UAT_doi-tac/flowtest-2026-08-05/partner-evidence/QLKTLBG_18.jpg` (ảnh cùng màn — xem §3) ·
`output/UAT_doi-tac/flowtest-2026-08-05/evidence/DEV-QLKTLBG_18-nut-xuat-excel-loc-slide-V108.png` (ảnh
chụp **env nội bộ**, bản dựng `V1.0.8` — **KHÔNG** dùng cho env đối tác) ·
`output/UAT_doi-tac/bug-con-fail-doi-tac-2026-07-31.md:336`.

---

## 3. Cổng bằng chứng

- **Không có bằng chứng riêng cho QLKTLBG_20** — ô Ảnh/video của dòng 14 rỗng.
- **Có bằng chứng của case cùng màn** (`QLKTLBG_18.jpg`) — đã mở xem: thanh địa chỉ
  `htpldn-uat.ospgroup.vn/dao-tao/bai-giang/danh-sach`, bản dựng sidebar `HTPLDN · V1.0`, đồng hồ 2026-07-25,
  vai trò `CB_NV_TW`, vùng tiêu đề chỉ có **`+ Thêm mới`** và **`Làm mới`** (**không có "Xuất Excel"**), chip
  `Bộ lọc nâng cao (2)` hiện sẵn.
  **Ảnh này dùng để định vị màn + xác nhận URL, KHÔNG dùng để kết luận verdict cho dòng 14.**
- **Vẫn chạy tiếp.** Thiếu bằng chứng riêng nhưng **tự tái hiện được**: 2 bước, không cần tiền đề đặc biệt,
  không cần ID bản ghi của đối tác. Điều kiện duy nhất — *"tiêu chí lọc không có kết quả"* — QA **tự dựng
  được** bằng từ khoá vô nghĩa (§6 T3).
  **CẤM kết luận "không phải lỗi" chỉ vì không có bằng chứng.**
- **Điều kiện tái hiện sẽ ghi vào báo cáo:** env + bản dựng đọc trên UI · tài khoản thực dùng · URL màn ·
  **giá trị lọc cụ thể đã nhập** · xác nhận màn hiện **0 bản ghi** ngay trước khi bấm Xuất Excel.
- **Không đụng dữ liệu đối tác** — chỉ lọc, không tạo/sửa/xóa bản ghi nào.

---

## 4. Bảng chuẩn chấm

**Expected đối tác (nguyên văn):** *"Hệ thống xuất danh sách rỗng hoặc hiển thị thông báo không có dữ liệu"*

🔴 **Đây là mệnh đề HOẶC** — chỉ cần **một trong hai** nhánh xảy ra là vế nội dung **đạt**. Khoá điều này
ngay để vòng đo sau không chấm Fail oan khi hệ thống chọn nhánh còn lại.

| # | Điều kiện của BUG GỐC | Đặc tả nói gì (file:dòng, nguyên văn) | Phép đo quyết định | Pass khi | Reopen khi |
|---|---|---|---|---|---|
| **D1** | Bước 2 của phiếu — *"…nhấn Xuất excel"* — **thực hiện được**: màn Kho tài liệu / Bài giảng phải có chức năng Xuất Excel. Triệu chứng TKM: *"Màn hình không có nút chức năng"* | **MATCH.** `srs-fr-03-dao-tao.md:1952` — *"Nút \"Xuất Excel\" (phụ): xuất danh sách theo bộ lọc hiện tại, tối đa 10.000 dòng (BR-DATA-06)"* · `srs-v3.5.md:5570` — *"**Export Excel:** Mọi danh sách có tính năng xuất Excel…"*, Áp dụng FR = *"Toàn bộ CRUD list"* | Liệt kê DOM vùng tiêu đề + thanh công cụ: mảng `{tag, innerText, title, ariaLabel, className, disabled}` của mọi `button`/`a`/`[role=button]`; mở mọi menu phụ rồi lặp lại. Đối chứng độc lập: `paths` chứa `bai-giang` ở `/api/docs-json`, lọc `export`/`excel`/`xuat` — **CẤM đoán đường dẫn** | Màn có chức năng Xuất Excel dùng được | Đã liệt kê DOM + menu phụ + `/api/docs-json` mà **không có** chức năng xuất danh sách nào ở thanh công cụ |
| **D2a** | Nhánh (a) của mệnh đề HOẶC — *"Hệ thống **xuất danh sách rỗng**"*: tệp phản ánh **đúng bộ lọc đang đặt**; bộ lọc ra 0 kết quả ⇒ tệp có **0 dòng dữ liệu**, KHÔNG chứa bản ghi ngoài bộ lọc | **MATCH.** `srs-fr-03-dao-tao.md:1952` — *"xuất danh sách **theo bộ lọc hiện tại**"* · `srs-v3.5.md:5570` — *"File xuất **theo bộ lọc hiện tại**…"*, cột "Áp dụng FR" = *"Toàn bộ CRUD list"*, cột "Ngoại lệ" chỉ có *Báo cáo nhóm IX* (**không loại trừ Nhóm III**) | Đặt bộ lọc 0-kết-quả (§6 T3) → xác nhận màn hiện 0 bản ghi (T4) → bấm Xuất Excel 1 lần → nếu có tệp thì **MỞ TỆP** bằng `openpyxl` đếm số dòng dữ liệu (tổng dòng − dòng tiêu đề) | Tệp mở được và có **0 dòng dữ liệu** (chỉ còn dòng tiêu đề, hoặc không có dòng nào) | Tệp chứa **bản ghi ngoài bộ lọc** (≠ 0 dòng dữ liệu) — vi phạm *"theo bộ lọc hiện tại"* |
| **D2b** | Nhánh (b) của mệnh đề HOẶC — *"**hoặc hiển thị thông báo không có dữ liệu**"*: hệ thống chặn xuất / không tạo tệp mà báo cho người dùng | **IM LẶNG cho Nhóm III → GAP → route BA.** Đã đọc trọn `:744–818` (FR-III-07, bảng Error Handling `:805–809` chỉ có 3 lỗi về tải tệp bài giảng), `:821–877` (FR-III-08 — **không có bảng Error Handling**), `:1941–1984` (SCR-III-03 — **không có** mục trạng thái rỗng / thông báo khi xuất). Dòng gần nhất để truy phạm vi: `:1952` | Chỉ **đo hiện trạng**: cài `output/UAT_doi-tac/tools/toast-capture.js` **TRƯỚC** khi bấm; bắt nguyên văn thông báo (`innerText`) + xác nhận có/không có tệp + đối chiếu thân phản hồi lời gọi xuất | **Không Pass riêng vế này, không Reopen riêng vế này.** Nếu hệ thống chọn nhánh (b) thì expected của đối tác **THOẢ** ⇒ không được chấm Fail; nhưng vì đặc tả im lặng nên ghi **Cần BA confirm** kèm câu hỏi đã soạn ở §9 | (không áp dụng — GAP không sinh Reopen) |

### Trích nguyên văn SRS dưới từng vế

**D1 — `srs-fr-03-dao-tao.md:1949–1952` (Thành phần 2 của SCR-III-03, trọn khối):**

```
**Thành phần 2 — Tiêu đề + Hành động chính:**
- Tiêu đề trang: "Kho tài liệu & bài giảng"
- Nút "+ Thêm mới" (chính): mở biểu mẫu thêm bài giảng
- Nút "Xuất Excel" (phụ): xuất danh sách theo bộ lọc hiện tại, tối đa 10.000 dòng (BR-DATA-06)
```

**D1 + D2a — `srs-v3.5.md:5570`** (Phụ lục B.2, BR-DATA-06; header cột ở `:5563` =
`| ID | Phát biểu quy tắc | Nguồn | Áp dụng FR | Ngoại lệ | Kiểm chứng |`):

```
| BR-DATA-06 | **Export Excel:** Mọi danh sách có tính năng xuất Excel. File xuất theo bộ lọc hiện tại, không vượt quá 10,000 rows/file | Pattern IP-01 | Toàn bộ CRUD list | Báo cáo nhóm IX có xuất PDF theo khung TT 17/2025 | Test export limit |
```

→ *"File xuất **theo bộ lọc hiện tại**"* là căn cứ của **D2a**: bộ lọc ra 0 kết quả thì tệp không được chứa
bản ghi nào.

**D2a — `srs-fr-03-dao-tao.md:1954–1960` (bộ lọc dùng để dựng ca 0 kết quả):**

```
**Thành phần 3 — Thanh lọc và tìm kiếm:**
- Ô từ khóa: "Tìm theo tên bài giảng"
- Lọc Loại tài liệu: Tất cả / Slide / PDF / Video
- Lọc Lĩnh vực pháp luật (chọn nhiều — nguồn DANH_MUC loại LINH_VUC_PL)
- Lọc Công khai: Tất cả / Đã công khai / Chưa công khai `[STT66 UAT 2026-06-02]`
- Lọc Từ ngày / Đến ngày (theo ngày tạo)
- Nút "Tìm kiếm" (chính) · "Xóa bộ lọc" (mờ)
```

**D2b — chứng minh SRS Nhóm III IM LẶNG (đã đọc trọn, không kết luận bằng 1 lệnh grep):**

1. `srs-fr-03-dao-tao.md:805–809` — **toàn bộ** bảng Error Handling của FR-III-07 chỉ có 3 dòng, đều về tải
   tệp bài giảng, **không dòng nào về xuất Excel / dữ liệu rỗng**:

```
| # | Điều kiện lỗi | Mã lỗi | Phản hồi hệ thống | Severity |
|---|--------------|--------|-------------------|----------|
| E1 | File vượt 20MB | ERR-BG-01 | "File tối đa 20MB" | ERROR |
| E2 | File sai định dạng | ERR-BG-02 | "Chỉ chấp nhận file Slide hoặc PDF" | ERROR |
| E3 | URL YouTube không hợp lệ | ERR-BG-03 | "URL YouTube không hợp lệ" | ERROR |
```

2. **FR-III-08 (`:821–877`) không có bảng Error Handling nào** — mục đi thẳng từ `**Postconditions:**`
   (`:868`) sang `**Acceptance Criteria:**` (`:870`). Bốn AC (`:871–874`) đều nói về hiển thị danh sách lọc,
   **không AC nào nói về xuất Excel**.
3. `srs-fr-03-dao-tao.md:1941–1984` (SCR-III-03) **không có** mục "Trạng thái rỗng" / thông báo khi xuất —
   trong khi **cùng file**, SCR-III-02 lại có (`:1921`, `:1922`, `:1927`) ⇒ việc thiếu ở SCR-III-03 là
   **khoảng trống thật**, không phải quy ước viết tắt của tài liệu.

**D2b — tiền lệ ở module KHÁC, chứng minh đây là quyết định BA phải chốt riêng từng màn** (dẫn để đặt câu hỏi
BA đúng trọng tâm; **KHÔNG** dùng làm chuẩn chấm cho màn này):

- `srs-fr-13-tv-nhanh.md:155`:

```
| E5 | Xuất Excel khi bộ lọc không có kết quả | INF-KHO-XL-01 | "Không có dữ liệu để xuất" — chặn xuất, không tạo tệp rỗng **[BA-07 tuần 4]** | INFO |
```

- `srs-fr-15-ct-htpldn.md:403` và AC `:409`:

```
| E1 | Không có dữ liệu để xuất | INF-XI-02-XL-01 | "Không có chương trình nào để xuất" | INFO |
- **Given** DS trống **When** nhấn "Xuất Excel" **Then** hiển thị thông báo không có dữ liệu
```

→ Hai module đã được BA chốt **rõ ràng và bằng mã thông báo riêng**, mà lại **chốt khác nhau** (một bên chặn
xuất, một bên chỉ hiển thị thông báo); Nhóm III thì **không có gì**. Đây là căn cứ để chấm `GAP`, **không
phải** để mượn quy tắc của module khác áp sang.

### 🔴 Trả lời câu hỏi then chốt

> **SRS có quy định màn Kho tài liệu / Bài giảng phải có chức năng Xuất Excel không?**

**CÓ — quy định rõ, ở cấp màn hình** (`:1952`), dẫn thẳng BR-DATA-06 (`srs-v3.5.md:5570`) với Áp dụng FR =
*"Toàn bộ CRUD list"*. ⇒ **D1 MATCH · thiếu chức năng = Reopen.**

> **SRS có quy định hành vi khi bộ lọc ra 0 kết quả không?**

**KHÔNG — Nhóm III im lặng** (chứng minh 3 bước ở trên). ⇒ **D2b là GAP → route BA**, cấm Pass và cấm Reopen
riêng vế đó. **D2a vẫn MATCH** vì nó chỉ là hệ quả của *"theo bộ lọc hiện tại"*.

### ⚠️ Đã cân nhắc và LOẠI khả năng "SRS im lặng cả D1"

Bảng §6 tại `srs-fr-03-dao-tao.md:2243` ghi `| BR-DATA-06 | Export Excel | FR-III-01, FR-III-05, FR-III-06,
FR-III-14 |` — **không liệt kê FR-III-07/FR-III-08**. **Không phải mệnh đề ngoại lệ:** đó là bảng mục lục
tham chiếu chéo cấp FR (cột 3 tên *"FR áp dụng (trong nhóm này)"*), không dùng từ "không áp dụng"; ngoại lệ
của BR-DATA-06 nằm ở **cột "Ngoại lệ" của chính BR** (`srs-v3.5.md:5570`) và chỉ có *Báo cáo nhóm IX*; đặc
tả cấp màn (`:1952`) nói rõ màn này CÓ nút và **là căn cứ nghiệm thu** (`:1945`). → **Không đổi quan hệ D1.**
Ghi **1 dòng candidate tài liệu** (không phải bug phần mềm): *"Bảng §6 `:2243` thiếu FR-III-07/FR-III-08 ở
dòng BR-DATA-06."*

---

## 5. Đường đo tối thiểu

**Một đường UI ngắn nhất + một đối chứng độc lập. Bấm Xuất Excel đúng 1 lần.**

### 5.1. Nhánh — chức năng Xuất Excel **KHÔNG tồn tại** (đúng triệu chứng TKM)

| Bước | Nội dung | Kiểm vế |
|---|---|---|
| U0 | Đăng nhập `cbnv_tw`, **tải lại trang**, ghi bản dựng | tiền đề |
| U1 | (Phiếu bước 1) Vào Đào tạo, tập huấn → Kho tài liệu / Bài giảng; xác nhận URL `…/dao-tao/bai-giang/danh-sach` | tiền đề |
| U2 | Liệt kê `innerText` vùng tiêu đề + thanh công cụ, **kèm** mảng `{tag, innerText, title, ariaLabel, className, disabled}` của mọi `button`/`a`/`[role=button]` (bắt nút chỉ có biểu tượng) | **D1** |
| U3 | Mở mọi menu phụ tìm được (kebab `…`, "Thao tác khác", dropdown) rồi lặp lại U2 cho nội dung menu | **D1** |
| Đối chứng độc lập | `fetch('/api/docs-json')` → `paths` chứa `bai-giang`; lọc tiếp path/summary chứa `export`/`excel`/`xuat`. **CẤM tự đoán đường dẫn** | **D1** |

D1 không đạt ⇒ **D2a/D2b không đo được** — ghi rõ bị chặn bởi D1, **không** suy đoán hệ thống "sẽ" làm gì.

### 5.2. Nhánh — chức năng Xuất Excel **CÓ tồn tại**

| Bước | Nội dung | Kiểm vế |
|---|---|---|
| U0–U1 | như trên | tiền đề |
| U2 | (Phiếu bước 2a) Nhập ô từ khoá *"Tìm theo tên bài giảng"* = **`ZZQAKHONGTONTAI20260807`** → bấm **"Tìm kiếm"** | tiền đề T3 |
| U3 | **Xác nhận màn hiện 0 bản ghi**: `innerText` vùng bảng + `total`/`total_count` trong thân phản hồi danh sách. Chưa xác nhận 0 thì **CẤM bấm xuất** | tiền đề T4 |
| U4 | Cài `output/UAT_doi-tac/tools/toast-capture.js` **TRƯỚC** khi bấm — vì thông báo là đầu ra bắt buộc của nhánh (b) | **D2b** |
| U5 | (Phiếu bước 2b) Bấm **Xuất Excel** (UI thật, **1 lần**) | **D1** + **D2a/D2b** |
| U6 | Ghi lại **cả hai** quan sát: (i) có/không tệp tải về; (ii) nguyên văn thông báo bắt được + số lời gọi mạng kèm theo | phân nhánh |
| Đối chứng độc lập — nhánh (a) | Nếu có tệp: **MỞ TỆP** `openpyxl.load_workbook(path, read_only=True)` → đếm **số dòng dữ liệu** (tổng dòng − dòng tiêu đề) ⇒ phải = **0** | **D2a** |
| Đối chứng độc lập — nhánh (b) | Nếu không có tệp: đối chiếu thân phản hồi + mã trạng thái của **chính lời gọi xuất** (`list_network_requests`) với thông báo đã bắt | **D2b** |

**Lấy tệp về để mở — thử theo thứ tự, dừng khi được:** (1) kiểm `~/Downloads`; (2) nếu trình duyệt điều khiển
bằng công cụ không đổ tệp ra đĩa → đọc nội dung **ngay trong trang**: `fetch` lại **đúng** URL tệp mà lời gọi
tải đã dùng (lấy từ `list_network_requests`, **không đoán**) → parse EOCD + `DecompressionStream`, chỉ trả về
số dòng cần đo; (3) giữ lại đường dẫn tệp để verdict truy lại được.

🔴 **CẤM dừng ở "tải được tệp".** HTTP 200 + dữ liệu nhị phân chỉ chứng minh CREATE, không chứng minh CORRECT.

---

## 6. Tiền đề phải dựng

| # | Tiền đề | Vì sao bắt buộc (dòng SRS) | Cách dựng nếu thiếu |
|---|---|---|---|
| **T1** | Tài khoản vai trò **CB NV** | `:751` tác nhân FR-III-07 · `:828` tác nhân FR-III-08 · `:757` quyền "Quản lý tài liệu ĐT" | `cbnv_tw` / `Test@1234` + OTP MailHog env đối tác. Env này **chưa xác nhận có tài khoản anh em** `cbnv_tw_02/_03` → khoá lock thì **DỪNG, báo lead**, cấm đổi vai trò/cấp |
| **T2** | Màn Kho tài liệu / Bài giảng **truy cập được**, bảng render bình thường trước khi lọc | Cần biết màn khỏe mạnh để phân biệt "0 kết quả do lọc" với "màn hỏng" | Vào màn, xác nhận có bảng (**không cần** bao nhiêu bản ghi — ca này cần 0 **sau khi lọc**). Ghi lại tổng trước khi lọc để đối chiếu ở bẫy (d) |
| **T3** | **Bộ lọc chắc chắn ra 0 kết quả** | Đây là chữ *"điều kiện lọc không có kết quả"* của phiếu | Ô từ khoá *"Tìm theo tên bài giảng"* (`:1955`) = **`ZZQAKHONGTONTAI20260807`** — chuỗi vô nghĩa, không dấu, có ngày để không đụng dữ liệu thật. **Không dùng lọc ngày** (dễ lẫn với ca khác và phụ thuộc dữ liệu). Nếu chuỗi này vô tình khớp → đổi sang `ZZQAKHONGTONTAI20260807X` và **ghi lại giá trị thực dùng** |
| **T4** | **Xác nhận 0 bản ghi** trước khi bấm xuất | Thiếu thì phép đo không nói về ca này | Đọc bảng + `total`/`total_count` trong thân phản hồi danh sách. Hai nguồn phải khớp |
| **T5** | Bộ lọc thật sự **đã được áp dụng** | Đặc tả có nút "Tìm kiếm" riêng (`:1960`) ⇒ gõ xong chưa chắc đã lọc | Bấm **"Tìm kiếm"** rồi mới đọc lại ở U3 |
| **T6** | Ghi **env + bản dựng** sau khi tải lại trang | Luật 4 BRIEF | Đọc ở sidebar/chân trang |
| **T7** | **Không tạo dữ liệu mới** | Ca này không cần seed | Chỉ cần lọc rỗng. Nếu vì lý do nào đó phải seed, khai đủ: **đổi bản ghi nào · đổi gì · env nào** |

**Không đụng dữ liệu đối tác.**

---

## 7. Bẫy đã biết

**Chặn FAIL oan:**

- **(a) 🔴 Mệnh đề HOẶC — đạt 1 trong 2 là đủ.** Expected là *"xuất danh sách rỗng **hoặc** hiển thị thông
  báo không có dữ liệu"*. Hệ thống chỉ tạo tệp rỗng mà **không** báo gì → **vẫn thoả expected**, CẤM chấm
  Fail. Hệ thống chỉ báo "không có dữ liệu" mà **không** tạo tệp → **vẫn thoả expected**, CẤM chấm Fail vì
  "không tải được tệp". Chỉ khi **không nhánh nào xảy ra** (không tệp, không thông báo, hoặc tệp chứa bản
  ghi ngoài bộ lọc) mới là không đạt.
- **(b) 🔴 Chip "Bộ lọc nâng cao (2)" hiện sẵn KHÔNG phải là bộ lọc đang áp dụng.** Ảnh đối tác cho thấy chip
  này hiện ngay khi vào màn; con số `(2)` là **số ô lọc nâng cao có sẵn**, không có nghĩa "đang có 2 điều
  kiện lọc". Bộ lọc 0-kết-quả của ca này phải do **QA chủ động đặt** ở T3, và phải xác nhận bằng T4.
- **(c) Nút có thể nằm trong menu phụ / là biểu tượng không nhãn.** CẤM kết luận "không có nút" bằng mắt qua
  ảnh chụp. Phải liệt kê `innerText` **cộng** `title`/`aria-label`/`className` của mọi
  `button`/`a`/`[role=button]`, và mở thử menu phụ trước khi chốt D1.
- **(d) 🔴 Bảng rỗng nên cột "Hành động" không hiện — đừng nhầm là "màn mất nút chức năng".**
  `srs-fr-03-dao-tao.md:1974` — *"Hành động | — | Xem trực tuyến · **Tải về (chỉ Slide/PDF)** · Sửa · Xóa"*.
  Cột này thuộc **từng dòng**; ca này bảng rỗng nên nó biến mất là bình thường. D1 đo ở **thanh công cụ đầu
  màn**. (Đây cũng là lý do T2 yêu cầu ghi lại trạng thái màn **trước** khi lọc.)
- **(e) Tệp rỗng nhưng vẫn có dòng tiêu đề.** Tệp chỉ có header, 0 dòng dữ liệu = **đạt D2a**. CẤM chấm Fail
  vì "tệp không hoàn toàn trống byte".
- **(f) 🔴 SRS Nhóm III KHÔNG quy định câu chữ thông báo cho màn này.** CẤM chấm Fail vì thông báo không
  trùng chữ *"Không có dữ liệu để xuất"* (`srs-fr-13-tv-nhanh.md:155`) hay *"Không có chương trình nào để
  xuất"* (`srs-fr-15-ct-htpldn.md:403`) — hai câu đó thuộc **màn khác**, và bản thân hai màn đó cũng xử lý
  **khác nhau**.
- **(g) SRS Nhóm III không quy định bộ cột tệp xuất SCR-III-03.** FR-III-07 (`:744–818`) và FR-III-08
  (`:821–877`) không có mục "Processing — Xuất Excel" (khác FR-III-01 `:180–184`, FR-III-05 `:599–605`).
  ⇒ CẤM chấm Fail vì thiếu/thừa cột, sai thứ tự, sai tên sheet.
- **(h) Đổi vai trò để "cho ra nút".** Nếu D1 không đạt, CẤM đăng nhập `admin` rồi kết luận Pass — vai trò
  của vế là **CB NV** (`:751`).

**Chặn PASS oan:**

- **(i) 🔴 "Tải được tệp" ≠ "nội dung đúng".** Bắt buộc mở tệp đếm dòng dữ liệu. Tệp "rỗng" mà thực ra chứa
  **toàn bộ** bản ghi (bỏ qua bộ lọc) là **D2a KHÔNG đạt** — **ca PASS-oan nguy hiểm nhất của case này**.
- **(j) Không có tệp + không có thông báo, nhưng có toast "Xuất thành công".** Không thuộc nhánh nào ⇒
  **không đạt**, và **không** được coi là nhánh (b).
- **(k) Chữ người dùng nhìn thấy đọc bằng `innerText`, KHÔNG `textContent`** — `textContent` gom cả node ẩn
  → báo "có thông báo" trong khi người dùng không thấy gì (bug ma), hoặc báo có nút trong khi nút đang ẩn.
- **(l) Thông báo tự tắt.** Dùng `tools/toast-capture.js` cài **TRƯỚC** khi bấm, **cấm lọc trùng** (lọc trùng
  che double-toast), đếm kèm số lời gọi mạng. Không bắt được → dùng **thân phản hồi** của lời gọi xuất làm
  bằng chứng mạnh hơn ảnh; **không bấm lại chỉ để chụp lại**.
- **(m) 🔴 Trang cũ / bản dựng cũ / kết luận mượn từ env nội bộ.** Ô "Kết quả verify" của dòng này đã có nội
  dung nhưng **đo trên env nội bộ**; ảnh `DEV-…-V108.png` cũng là env nội bộ. **Cấm chép.** Phải tải lại
  trang và ghi bản dựng đọc trên UI của chính env đối tác.
- **(n) Hai phép đo mâu thuẫn = CHƯA được chốt.** Ví dụ: thông báo nói "không có dữ liệu" nhưng vẫn có tệp
  chứa dòng dữ liệu → ghi cả hai, hỏi lead.

---

## 8. Điểm KHÁC NHAU với QLKTLBG_18 / QLKTLBG_19 — cấm suy verdict chéo

Ba case **cùng màn** (`…/dao-tao/bai-giang/danh-sach`), **cùng câu triệu chứng TKM** (*"Màn hình không có nút
chức năng"*), nhưng **khác vế đo và khác cả quan hệ với SRS**. Cấm đo 1 case rồi suy cho 2 case còn lại —
cùng chữ không có nghĩa cùng nguyên nhân.

| | QLKTLBG_18 | QLKTLBG_19 | **QLKTLBG_20** (file này) |
|---|---|---|---|
| Điều kiện lọc | **Có** lọc, cho ra tập con | **Không đặt** lọc | **Có** lọc, cố ý cho ra **0 kết quả** |
| Tập dữ liệu lúc bấm | 0 < N < tổng | = tổng | **0 bản ghi** |
| Vế nội dung | Tệp = đúng tập lọc | Tệp = toàn bộ danh sách | **Mệnh đề HOẶC** — tệp rỗng **hoặc** thông báo không có dữ liệu |
| Quan hệ với SRS | MATCH toàn bộ | MATCH toàn bộ | D1 MATCH · **D2a MATCH · D2b GAP** |
| Route | TEST toàn bộ | TEST toàn bộ | TEST + **có nhánh phải chuyển BA** |
| Phép đo quyết định | Số dòng = tổng sau khi lọc | Số dòng = tổng bản ghi màn báo | Số dòng dữ liệu = **0**, **hoặc** bắt nguyên văn thông báo |
| Ca PASS-oan nguy hiểm nhất | Tệp chứa toàn bộ (bỏ qua lọc) | Tệp chỉ chứa trang đang xem | Tệp "rỗng" thực ra chứa toàn bộ bản ghi |

**Chỉ có D1 là chung** — và vẫn phải **tự quan sát lại trong từng case**, ghi riêng cho từng case. **D2 tuyệt
đối không suy chéo:** case 19 có thể xuất đúng toàn bộ danh sách mà vẫn hỏng ở ca 0-kết-quả (ví dụ bỏ qua bộ
lọc khi tập rỗng, hoặc lỗi khi tạo tệp không dòng); ngược lại, case 20 báo "không có dữ liệu" đúng cũng không
nói gì về việc case 18/19 có xuất đủ số dòng hay không.

---

## 9. Bảng quyết định đã cam kết TRƯỚC khi đo

| Quan sát khi đo | Verdict logic |
|---|---|
| Không tìm thấy chức năng Xuất Excel (sau khi đã liệt kê DOM + menu phụ + `/api/docs-json`) | **Reopen** (D1 không đạt) |
| Có chức năng; tệp tải về, mở được, **0 dòng dữ liệu** | Nhánh (a) — mọi vế MATCH đạt ⇒ **Pass** |
| Có chức năng; **không tạo tệp**, hiển thị thông báo không có dữ liệu | Nhánh (b) — expected **THOẢ** (cấm Fail/Reopen), nhưng D2b là GAP ⇒ **Cần BA**; ghi *"web hiện tại: đúng kỳ vọng đối tác"* + câu hỏi BA ở dưới |
| Có chức năng; tệp tải về nhưng **chứa bản ghi ngoài bộ lọc** (≠ 0 dòng dữ liệu) | **Reopen** (D2a không đạt — vi phạm *"File xuất theo bộ lọc hiện tại"*, `srs-v3.5.md:5570`) |
| Có chức năng; bấm ra lỗi 4xx/5xx, **không tệp và không thông báo** | **Reopen** (không nhánh nào của mệnh đề HOẶC xảy ra) |
| Vừa có thông báo "không có dữ liệu" **vừa** có tệp chứa dòng dữ liệu | **Chưa chốt** (hai phép mâu thuẫn) — ghi cả hai, hỏi lead |
| Không dựng được bộ lọc 0-kết-quả (T3/T4 không thoả) | **Chưa chốt** — nêu rõ dữ kiện còn thiếu, **CẤM Pass** |

**Câu hỏi BA đã soạn sẵn cho vế D2b** (dùng nguyên văn khi kết quả rơi vào nhánh (b)):

> **CẦN BA CONFIRM:** đối tác kỳ vọng — khi bộ lọc màn Kho tài liệu / Bài giảng không có kết quả, hệ thống
> *"xuất danh sách rỗng hoặc hiển thị thông báo không có dữ liệu"*; SRS quy định — **im lặng** cho Nhóm III:
> FR-III-07 (`srs-fr-03-dao-tao.md:744–818`, bảng Error Handling `:805–809` chỉ có 3 lỗi về tải tệp bài
> giảng), FR-III-08 (`:821–877`, **không có bảng Error Handling**) và SCR-III-03 (`:1941–1984`) đều không nêu
> hành vi khi tập kết quả rỗng, trong khi module khác đã chốt rõ và chốt **khác nhau**
> (`srs-fr-13-tv-nhanh.md:155` — chặn xuất, không tạo tệp rỗng; `srs-fr-15-ct-htpldn.md:403` + `:409` — hiển
> thị thông báo); web/dev hiện tại — *(điền sau khi đo, kèm env + bản dựng)*.
> **Mục đích câu hỏi: bổ sung điều này vào đặc tả SCR-III-03, KHÔNG phải chặn bàn giao.**
