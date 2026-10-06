# CHUẨN CHẤM — QLKTLBG_20 (Flow 04 · Giai đoạn A)

> **Giai đoạn A — chưa mở màn.** File này khoá chuẩn chấm TRƯỚC khi đo. Sau khi mở màn, CẤM đổi quan hệ
> `MATCH/DIFF/GAP` để khớp kết quả (Flow 04 luật khoá 5).

## 1. Bảng đầu

| Mục | Giá trị |
|---|---|
| Bảng / tab / dòng | Bảng đối tác 2026-08-07 · tab `bug` · **dòng 14** |
| Mã TC | **QLKTLBG_20** |
| Mô tả (đối tác) | "Xuất Excel với điều kiện lọc không có kết quả" |
| Trạng thái nguồn | Trạng thái `Fail` · Dopai `N/R` · Trạng thái dev fix `Fixed` · DEV phản hồi lần 1 (trống) |
| TKM phản hồi lần 1 | "Màn hình không có nút chức năng" |
| Env | `https://18.143.165.120.nip.io` |
| Bản dựng | Đọc ở chân/sidebar khi đo (tiền lệ tuần 2: `HTPLDN · V1.0.5`) — **bắt buộc tải lại trang rồi mới ghi** |
| Tài khoản dự kiến | `cbnv_tw_02` / `Test@1234` · OTP MailHog `http://18.143.165.120:8025` |
| Vai trò theo đặc tả | **CB NV** — `srs-fr-03-dao-tao.md:751` ("Tác nhân: CB NV / CB PD"), `:828`; quyền PRE-01 `:757` |
| Màn | Đào tạo, tập huấn → **Kho tài liệu / Bài giảng** → Danh sách (SCR-III-03) |
| URL | `https://18.143.165.120.nip.io/dao-tao/bai-giang/danh-sach` |
| SRS đã đọc | `Docs-PM-HTPLDN/…/srs-v3.5/srs-fr-03-dao-tao.md` — **2296 dòng** |
| SRS đã đọc | `Docs-PM-HTPLDN/…/srs-v3.5/srs-v3.5.md` — **7012 dòng** |
| SRS đã đọc (đối chiếu tiền lệ module khác) | `srs-fr-13-tv-nhanh.md` — **932 dòng** · `srs-fr-15-ct-htpldn.md` — **1610 dòng** |

---

## 2. Nguồn đã đọc (tự mở trong lượt này)

**SRS nguồn chuẩn DUY NHẤT — `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/`:**

| File | Đoạn đã đọc trọn | Nội dung |
|---|---|---|
| `srs-fr-03-dao-tao.md` | `:744–818` | FR-III-07 (UC26) — trọn mục, gồm bảng **Error Handling** `:805–809` |
| `srs-fr-03-dao-tao.md` | `:821–877` | FR-III-08 Tìm kiếm tài liệu (UC27) — trọn mục; **không có bảng Error Handling** |
| `srs-fr-03-dao-tao.md` | `:1941–1984` | **SCR-III-03** — trọn 6 Thành phần + Quy tắc nghiệp vụ |
| `srs-fr-03-dao-tao.md` | `:2227–2251` | §6 Tổng quan BR sử dụng |
| `srs-v3.5.md` | `:5561–5574` | Phụ lục B.2 BR-DATA (trọn bảng) |
| `srs-v3.5.md` | `:692`, `:861` | Pattern P-01 · EC-DATA-PAGE |
| `srs-fr-13-tv-nhanh.md` | `:148–157` | Bảng Error Handling — **tiền lệ module khác** về xuất Excel khi lọc rỗng |
| `srs-fr-15-ct-htpldn.md` | `:398–412` | Bảng Error Handling + AC — **tiền lệ module khác**, xử lý KHÁC module trên |

**Quét từ đồng nghĩa đã chạy trên `srs-fr-03-dao-tao.md`** (không chỉ 1 lệnh grep): `Xuất Excel` · `xuất excel` ·
`Xuất file` · `kết xuất` · `export` · `tải xuống` · `Tải về` · `xuất tệp` · `xuất danh sách` · `tiêu chí lọc` ·
`không có dữ liệu` · `danh sách rỗng` · `0 bản ghi` · `Không tìm thấy` · `Chưa có dữ liệu` · `trạng thái trống` ·
`Empty state`. Quét thêm **toàn thư mục** `srs-v3.5/` cho `không có dữ liệu` / `danh sách rỗng` / `BR-DATA-06` /
`_EXPORT`.

**Ngữ cảnh (CHỈ để biết tra chỗ nào — KHÔNG dùng làm căn cứ verdict, không mượn số dòng):**
`output/UAT_doi-tac/reverify-week-2/verify1-conlai-2026-08-03/bug-reports/dao-tao/bug-report-dao-tao.md` (URL màn +
env) · `output/UAT_doi-tac/reverify-week-2/cond/QLKTLBG_02-r2.md` (chip "Bộ lọc nâng cao (2)" mặc định).

---

## 3. Cổng bằng chứng

- **Không có bằng chứng đối tác** — ô Ảnh/video rỗng thật (đã kiểm cả link ẩn), ô "Kết quả thực tế" cũng trống.
- **Vẫn chạy tiếp** theo Flow 04 §Cổng bằng chứng: *"Thiếu bằng chứng nhưng tự tái hiện được → chạy tiếp và ghi
  điều kiện đã tái hiện."* **CẤM kết luận "không phải lỗi" chỉ vì không có bằng chứng.**
- **Vì sao tái hiện được:** 2 bước, không cần tiền đề đặc biệt, không cần ID bản ghi của đối tác. Điều kiện duy
  nhất — "tiêu chí lọc không có kết quả" — QA **tự dựng được** bằng từ khoá vô nghĩa (xem §6 T3).
- **Điều kiện tái hiện sẽ ghi vào báo cáo:** env + bản dựng · tài khoản thực dùng · URL màn · **giá trị lọc cụ
  thể đã nhập** · xác nhận màn hiện **0 bản ghi** ngay trước khi bấm Xuất Excel.
- **Neo lấy được từ bằng chứng:** không có → dùng dữ liệu QA sẵn có, **không đụng dữ liệu đối tác**.

---

## 4. BUG SCOPE LOCK

Expected đối tác (nguyên văn): **"Hệ thống xuất danh sách rỗng hoặc hiển thị thông báo không có dữ liệu"**

🔴 **Đây là mệnh đề HOẶC** — chỉ cần **một trong hai** nhánh xảy ra là vế nội dung **đạt**. Khoá điều này ngay để
vòng đo sau không chấm Fail oan khi hệ thống chọn nhánh còn lại.

| Vế | Expected đối tác (nguyên văn / tách vế) | SRS `file:dòng` | Quan hệ | Route | Đường đo |
|---|---|---|---|---|---|
| **C1** | Bước 2 "nhấn Xuất excel" **thực hiện được** — màn Kho tài liệu / Bài giảng phải có chức năng Xuất Excel (triệu chứng TKM: "Màn hình không có nút chức năng") | `srs-fr-03-dao-tao.md:1952` + `srs-v3.5.md:5570` | **MATCH** | **TEST** | Đường UI: liệt kê **innerText** + `title`/`aria-label` của mọi `button`/`a`/`[role=button]` ở vùng tiêu đề & thanh công cụ, kể cả trong menu phụ. Đối chứng độc lập: liệt kê `paths` chứa `bai-giang` ở `/api/docs-json`, lọc `export`/`excel` — **CẤM đoán đường dẫn** |
| **C2a** | Nhánh (a) của mệnh đề HOẶC: "**Hệ thống xuất danh sách rỗng**" — tệp xuất phản ánh **đúng bộ lọc đang đặt**, bộ lọc ra 0 kết quả ⇒ tệp có **0 dòng dữ liệu**, KHÔNG chứa bản ghi ngoài bộ lọc | `srs-fr-03-dao-tao.md:1952` + `srs-v3.5.md:5570` | **MATCH** | **TEST** | Đường UI: đặt bộ lọc 0-kết-quả → bấm Xuất Excel. Đối chứng độc lập: **mở tệp bằng `openpyxl`** đếm số dòng dữ liệu (tổng dòng − dòng tiêu đề) |
| **C2b** | Nhánh (b) của mệnh đề HOẶC: "**hoặc hiển thị thông báo không có dữ liệu**" — hệ thống chặn xuất / không tạo tệp mà báo cho người dùng | **IM LẶNG** cho Nhóm III (đã đọc trọn `srs-fr-03-dao-tao.md:744–818` FR-III-07, `:821–877` FR-III-08 — **FR-III-08 không có bảng Error Handling**, `:1941–1984` SCR-III-03 không có mục trạng thái rỗng / thông báo khi xuất). Dòng gần nhất đã đọc để truy phạm vi: `srs-fr-03-dao-tao.md:1952` | **GAP** | **BA** | Chỉ **đo hiện trạng** để làm rõ câu hỏi BA: bắt nguyên văn thông báo bằng `innerText` + xác nhận có/không có tệp. **Không Pass, không Reopen vế này** |

### Trích nguyên văn SRS dưới từng vế

**C1 — `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-03-dao-tao.md:1949–1952`:**

```
**Thành phần 2 — Tiêu đề + Hành động chính:**
- Tiêu đề trang: "Kho tài liệu & bài giảng"
- Nút "+ Thêm mới" (chính): mở biểu mẫu thêm bài giảng
- Nút "Xuất Excel" (phụ): xuất danh sách theo bộ lọc hiện tại, tối đa 10.000 dòng (BR-DATA-06)
```

**C1 + C2a — `srs-v3.5.md:5570`** (Phụ lục B.2, BR-DATA-06; header cột `:5563` =
`| ID | Phát biểu quy tắc | Nguồn | Áp dụng FR | Ngoại lệ | Kiểm chứng |`):

```
| BR-DATA-06 | **Export Excel:** Mọi danh sách có tính năng xuất Excel. File xuất theo bộ lọc hiện tại, không vượt quá 10,000 rows/file | Pattern IP-01 | Toàn bộ CRUD list | Báo cáo nhóm IX có xuất PDF theo khung TT 17/2025 | Test export limit |
```

→ *"File xuất **theo bộ lọc hiện tại**"* là căn cứ của **C2a**: bộ lọc ra 0 kết quả thì tệp không được chứa bản ghi
nào. Cột "Áp dụng FR" = **"Toàn bộ CRUD list"**; cột "Ngoại lệ" chỉ có *Báo cáo nhóm IX* — **không loại trừ Nhóm III**.

**C2a — `srs-fr-03-dao-tao.md:1954–1960`** (bộ lọc dùng để dựng ca 0 kết quả):

```
**Thành phần 3 — Thanh lọc và tìm kiếm:**
- Ô từ khóa: "Tìm theo tên bài giảng"
- Lọc Loại tài liệu: Tất cả / Slide / PDF / Video
- Lọc Lĩnh vực pháp luật (chọn nhiều — nguồn DANH_MUC loại LINH_VUC_PL)
- Lọc Công khai: Tất cả / Đã công khai / Chưa công khai `[STT66 UAT 2026-06-02]`
- Lọc Từ ngày / Đến ngày (theo ngày tạo)
- Nút "Tìm kiếm" (chính) · "Xóa bộ lọc" (mờ)
```

**C2b — chứng minh SRS Nhóm III IM LẶNG (đã đọc trọn, không kết luận bằng 1 lệnh grep):**

1. `srs-fr-03-dao-tao.md:805–809` — **toàn bộ** bảng Error Handling của FR-III-07 chỉ có 3 dòng, đều về tải tệp
   bài giảng, **không có dòng nào về xuất Excel / dữ liệu rỗng**:

```
| # | Điều kiện lỗi | Mã lỗi | Phản hồi hệ thống | Severity |
|---|--------------|--------|-------------------|----------|
| E1 | File vượt 20MB | ERR-BG-01 | "File tối đa 20MB" | ERROR |
| E2 | File sai định dạng | ERR-BG-02 | "Chỉ chấp nhận file Slide hoặc PDF" | ERROR |
| E3 | URL YouTube không hợp lệ | ERR-BG-03 | "URL YouTube không hợp lệ" | ERROR |
```

2. **FR-III-08 (`:821–877`) không có bảng Error Handling nào** — mục đi thẳng từ `**Postconditions:**` (`:868`)
   sang `**Acceptance Criteria:**` (`:870`). Bốn AC (`:871–874`) đều nói về hiển thị danh sách lọc, **không AC nào
   nói về xuất Excel**.
3. `srs-fr-03-dao-tao.md:1941–1984` (SCR-III-03) **không có** mục "Trạng thái rỗng" / thông báo khi xuất — trong
   khi cùng file, SCR-III-02 lại có (`:1921`, `:1922`, `:1927`) ⇒ việc thiếu ở SCR-III-03 là **khoảng trống thật**,
   không phải do quy ước viết tắt của tài liệu.

**C2b — tiền lệ ở module KHÁC chứng minh đây là quyết định BA phải chốt riêng từng màn** (dẫn để đặt câu hỏi BA
đúng trọng tâm; **KHÔNG** dùng làm chuẩn chấm cho màn này):

- `Docs-PM-HTPLDN/…/srs-v3.5/srs-fr-13-tv-nhanh.md:155`:

```
| E5 | Xuất Excel khi bộ lọc không có kết quả | INF-KHO-XL-01 | "Không có dữ liệu để xuất" — chặn xuất, không tạo tệp rỗng **[BA-07 tuần 4]** | INFO |
```

- `Docs-PM-HTPLDN/…/srs-v3.5/srs-fr-15-ct-htpldn.md:403` và AC `:409`:

```
| E1 | Không có dữ liệu để xuất | INF-XI-02-XL-01 | "Không có chương trình nào để xuất" | INFO |
- **Given** DS trống **When** nhấn "Xuất Excel" **Then** hiển thị thông báo không có dữ liệu
```

→ Hai module đã được BA chốt **rõ ràng và bằng mã thông báo riêng**; Nhóm III thì **không có gì**. Đây là căn cứ
để chấm `GAP`, không phải để mượn quy tắc của module khác áp sang.

### 🔴 Trả lời câu hỏi then chốt

> **SRS có quy định màn Kho tài liệu / Bài giảng phải có chức năng Xuất Excel không?**

**CÓ — quy định rõ, ở cấp màn hình.** `srs-fr-03-dao-tao.md:1952` liệt kê nút "Xuất Excel" là Hành động chính của
SCR-III-03 và dẫn thẳng BR-DATA-06; BR-DATA-06 (`srs-v3.5.md:5570`) phát biểu *"Mọi danh sách có tính năng xuất
Excel"*, Áp dụng FR = *"Toàn bộ CRUD list"*, ngoại lệ duy nhất là Báo cáo nhóm IX.

→ **C1: route TEST · MATCH · thiếu nút = Reopen.**

Nhưng **SRS Nhóm III KHÔNG quy định hành vi khi bộ lọc ra 0 kết quả** → **C2b là GAP → route BA**, cấm Pass và cấm
Reopen riêng vế đó.

### ⚠️ Đã cân nhắc và LOẠI khả năng "SRS im lặng cả C1"

Bảng §6 tại `srs-fr-03-dao-tao.md:2243` ghi `| BR-DATA-06 | Export Excel | FR-III-01, FR-III-05, FR-III-06,
FR-III-14 |` — **không liệt kê FR-III-07/FR-III-08**. **Không phải mệnh đề ngoại lệ**: đó là bảng mục lục tham
chiếu chéo cấp FR (cột 3 tên *"FR áp dụng (trong nhóm này)"*), không dùng từ "không áp dụng"; ngoại lệ của
BR-DATA-06 nằm ở **cột "Ngoại lệ" của chính BR** (`srs-v3.5.md:5570`) và chỉ có *Báo cáo nhóm IX*; đặc tả cấp màn
(`:1952`) nói rõ màn này CÓ nút và là căn cứ nghiệm thu (xem `:1945`). → **Không đổi quan hệ C1.** Ghi **1 dòng
candidate tài liệu** (không phải bug phần mềm): *"Bảng §6 `:2243` thiếu FR-III-07/FR-III-08 ở dòng BR-DATA-06."*

---

## 5. Đường đo tối thiểu

**Một đường UI ngắn nhất + một đối chứng độc lập. Đủ thì dừng — bấm Xuất Excel đúng 1 lần.**

### 5.1. Nhánh — nút Xuất Excel **KHÔNG tồn tại** (đúng triệu chứng TKM)

| Bước | Nội dung | Kiểm vế |
|---|---|---|
| U1 | Đăng nhập `cbnv_tw_02`, **tải lại trang**, ghi bản dựng ở sidebar | tiền đề |
| U2 | Vào Đào tạo, tập huấn → Kho tài liệu / Bài giảng; xác nhận URL `/dao-tao/bai-giang/danh-sach` | tiền đề |
| U3 | `evaluate_script` liệt kê **innerText** vùng tiêu đề + thanh công cụ, **kèm** mảng `{tag, innerText, title, ariaLabel, className}` của mọi `button`/`a`/`[role=button]` trong vùng đó (bắt nút chỉ có icon) | **C1** |
| U4 | Mở mọi menu phụ tìm được (kebab `…`, "Thao tác khác", dropdown) rồi lặp lại U3 cho nội dung menu | **C1** |
| Đối chứng độc lập | `fetch('/api/docs-json')` → liệt kê key `paths` chứa `bai-giang`; lọc tiếp path/summary chứa `export`/`excel`/`xuat`. **CẤM tự đoán đường dẫn endpoint** | **C1** |

C1 không đạt ⇒ **C2a/C2b không đo được** — ghi rõ là bị chặn bởi C1, **không** suy đoán hệ thống "sẽ" làm gì.

### 5.2. Nhánh — nút Xuất Excel **CÓ tồn tại**

| Bước | Nội dung | Kiểm vế |
|---|---|---|
| U1–U2 | như trên | tiền đề |
| U3 | Nhập ô từ khoá `"Tìm theo tên bài giảng"` = **`ZZQAKHONGTONTAI20260807`** → bấm "Tìm kiếm" | tiền đề C2 |
| U4 | **Xác nhận màn hiện 0 bản ghi** (đọc `innerText` vùng bảng + `total`/`total_count` trong phản hồi danh sách qua `list_network_requests`). Chưa xác nhận 0 thì **CẤM bấm xuất** | tiền đề C2 |
| U5 | Cài bộ bắt lớp nổi (`MutationObserver` trên `document.body`, **không lọc trùng**, đọc `innerText`) **TRƯỚC** khi bấm — vì thông báo là output bắt buộc của nhánh (b) | **C2b** |
| U6 | Bấm **Xuất Excel** (UI thật, **1 lần**) | **C1** + **C2a/C2b** |
| U7 | Ghi lại **cả hai** quan sát: (i) có/không tệp tải về; (ii) nguyên văn thông báo bắt được + số lời gọi mạng kèm theo | phân nhánh |
| Đối chứng độc lập — nhánh (a) | Nếu có tệp: **MỞ TỆP** `openpyxl.load_workbook(path, read_only=True)` → đếm **số dòng dữ liệu** (tổng dòng − dòng tiêu đề) ⇒ phải = **0** | **C2a** |
| Đối chứng độc lập — nhánh (b) | Nếu không có tệp: đối chiếu phản hồi máy chủ của chính lời gọi xuất (`list_network_requests` → mã trạng thái + thân phản hồi) với thông báo đã bắt | **C2b** |

**Lấy tệp về để mở — thử theo thứ tự, dừng khi được:** (1) kiểm `~/Downloads`; (2) nếu Chrome MCP `--isolated`
không đổ file ra đĩa → đọc nội dung **ngay trong trang**: `fetch` lại đúng URL tệp mà lời gọi tải đã dùng (lấy từ
`list_network_requests`, **không đoán**) → parse EOCD + `DecompressionStream`, chỉ trả về số dòng cần đo; (3) giữ
lại đường dẫn tệp / manifest để verdict truy lại được.

🔴 **CẤM dừng ở "tải được tệp".** HTTP 200 + binary chỉ chứng minh CREATE, không chứng minh CORRECT.

---

## 6. Tiền đề tối thiểu

| # | Tiền đề | Cách thoả |
|---|---|---|
| T1 | Tài khoản đúng vai trò **CB NV** (`srs-fr-03-dao-tao.md:751`, `:828`) | `cbnv_tw_02` / `Test@1234`, OTP MailHog. Lock account → fallback SAME role+cấp (`_03`), **ghi account thực dùng** |
| T2 | Màn Kho tài liệu / Bài giảng **truy cập được** và bảng render bình thường trước khi lọc | Vào màn, xác nhận có bảng (không cần bao nhiêu bản ghi — ca này cần 0 **sau khi lọc**) |
| T3 | **Bộ lọc chắc chắn ra 0 kết quả** | Ô từ khoá `"Tìm theo tên bài giảng"` (`:1955`) = **`ZZQAKHONGTONTAI20260807`** — chuỗi vô nghĩa, không dấu, có ngày để không đụng dữ liệu thật. **Không dùng lọc ngày** (dễ lẫn với ca khác và phụ thuộc dữ liệu). Nếu chuỗi này vô tình khớp → đổi sang `ZZQAKHONGTONTAI20260807X` và ghi lại giá trị thực dùng |
| T4 | **Xác nhận 0 bản ghi** trước khi bấm xuất | Đọc bảng + `total`/`total_count` phản hồi danh sách. **Đây là tiền đề bắt buộc** — thiếu thì phép đo không nói về ca này |
| T5 | Ghi **env + bản dựng** sau khi tải lại trang | Sidebar/chân trang |
| T6 | Không tạo dữ liệu mới | Ca này **không cần seed** — chỉ cần lọc rỗng. Nếu vì lý do nào đó phải seed, khai đủ: **đổi bản ghi nào · đổi gì · env nào** |

**Không đụng dữ liệu đối tác.**

---

## 7. Bẫy chặn FAIL oan / PASS oan

**Chặn FAIL oan:**

- **(a) 🔴 Mệnh đề HOẶC — đạt 1 trong 2 là đủ.** Expected là *"xuất danh sách rỗng **hoặc** hiển thị thông báo
  không có dữ liệu"*. Hệ thống chỉ tạo tệp rỗng mà **không** báo gì → **vẫn thoả expected**, CẤM chấm Fail. Hệ
  thống chỉ báo "không có dữ liệu" mà **không** tạo tệp → **vẫn thoả expected**, CẤM chấm Fail vì "không tải được
  tệp". Chỉ khi **không nhánh nào xảy ra** (không tệp, không thông báo, hoặc tệp chứa bản ghi ngoài bộ lọc) mới là
  không đạt.
- **(b) Nút có thể nằm trong menu phụ / là icon không nhãn.** CẤM kết luận "không có nút" bằng mắt qua ảnh chụp.
  Phải liệt kê DOM thanh công cụ: `innerText` **cộng** `title`/`aria-label`/`className` của mọi
  `button`/`a`/`[role=button]`, và mở thử menu phụ trước khi chốt C1.
- **(e) Nhầm "Tải về" ở cột Hành động với "Xuất Excel".** `srs-fr-03-dao-tao.md:1974` — *"Hành động | — | Xem trực
  tuyến · Tải về (chỉ Slide/PDF) · Sửa · Xóa"*. Ở ca này bảng rỗng nên cột Hành động **không** hiện — đừng vì thế
  mà kết luận "màn mất nút chức năng"; C1 đo ở **thanh công cụ đầu màn**, không đo ở dòng bảng.
- **(f) Tệp rỗng nhưng vẫn có dòng tiêu đề.** Tệp chỉ có header, 0 dòng dữ liệu = **đạt C2a**. CẤM chấm Fail vì
  "tệp không hoàn toàn trống byte".
- **(g) SRS Nhóm III KHÔNG quy định câu chữ thông báo cho màn này.** CẤM chấm Fail vì thông báo không trùng chữ
  *"Không có dữ liệu để xuất"* của `srs-fr-13-tv-nhanh.md:155` hay *"Không có chương trình nào để xuất"* của
  `srs-fr-15-ct-htpldn.md:403` — hai câu đó thuộc **màn khác**, và bản thân hai màn đó cũng xử lý khác nhau.
- **(h) SRS Nhóm III không quy định bộ cột tệp xuất SCR-III-03** (FR-III-07 `:744–818` và FR-III-08 `:821–877`
  không có mục "Processing — Xuất Excel", khác FR-III-01 `:180–184`). ⇒ CẤM chấm Fail vì thiếu/thừa cột, sai thứ
  tự, sai tên sheet.
- **(j) Đổi vai trò để "cho ra nút".** Nếu C1 không đạt, CẤM đăng nhập `admin` rồi kết luận Pass — vai trò của vế
  là **CB NV** (`:751`).

**Chặn PASS oan:**

- **(c) Chữ người dùng nhìn thấy đọc bằng `innerText`, KHÔNG `textContent`** — `textContent` gom cả node ẩn của
  AntD → báo "có thông báo" trong khi người dùng không thấy gì (bug ma), hoặc báo có nút trong khi nút đang ẩn.
- **(c-2) Thông báo tự tắt.** Lớp nổi AntD sống < 5s → cài `MutationObserver` trên `document.body` **TRƯỚC** khi
  bấm, **CẤM lọc trùng** (lọc trùng che double-toast), và đếm kèm số lời gọi mạng. Không bắt được bằng observer →
  dùng thân phản hồi của lời gọi xuất làm bằng chứng mạnh hơn ảnh; **không bấm lại chỉ để chụp lại**.
- **(d) Tải được tệp ≠ nội dung đúng.** Bắt buộc mở tệp đếm dòng dữ liệu. Tệp "rỗng" mà thực ra chứa **toàn bộ**
  bản ghi (bỏ qua bộ lọc) là **C2a KHÔNG đạt** — đây chính là ca PASS-oan nguy hiểm nhất của case này.
- **(d-2) Không có tệp + không có thông báo, nhưng có toast "Xuất thành công".** Không thuộc nhánh nào ⇒ **không
  đạt**, không được coi là nhánh (b).
- **(k) Trang cũ / bản dựng cũ.** Tab MCP mở lâu vẫn chạy JS cũ → **tải lại trang** trước lô đo và **ghi tên bản
  dựng**.
- **(l) Hai phép đo mâu thuẫn = CHƯA được chốt.** Ví dụ: thông báo nói "không có dữ liệu" nhưng vẫn có tệp chứa
  dòng dữ liệu → ghi cả hai, hỏi user.

---

## 8. Điểm KHÁC NHAU với QLKTLBG_19 — cấm suy verdict chéo

Hai case **cùng màn** (`/dao-tao/bai-giang/danh-sach`), **cùng câu triệu chứng TKM** ("Màn hình không có nút chức
năng"), nhưng **khác vế đo và khác cả quan hệ với SRS**. Flow 04 BƯỚC 0: *"đo từng case trên đúng màn của nó. Cấm
đo 1 case rồi suy cho các case còn lại — cùng chữ không có nghĩa cùng nguyên nhân."*

| | QLKTLBG_20 (file này) | QLKTLBG_19 |
|---|---|---|
| Điều kiện lọc | **Có** bộ lọc, cố ý cho ra **0 kết quả** | **Không đặt** bộ lọc |
| Tập dữ liệu lúc bấm | 0 bản ghi | ≥ 1 bản ghi |
| Vế nội dung | Mệnh đề **HOẶC** — tệp rỗng **hoặc** thông báo không có dữ liệu | Tệp phải chứa **toàn bộ** danh sách |
| Quan hệ với SRS | C1 MATCH · **C2a MATCH · C2b GAP** | C1 MATCH · C2 MATCH (không có GAP) |
| Route | TEST + **có nhánh phải chuyển BA** | TEST toàn bộ |
| Phép đo quyết định | Đếm dòng dữ liệu = 0, **hoặc** bắt nguyên văn thông báo | Đếm dòng dữ liệu = tổng bản ghi trên màn |
| Ca PASS-oan nguy hiểm nhất | Tệp "rỗng" thực ra chứa toàn bộ bản ghi (bỏ qua bộ lọc) | Tệp chỉ chứa trang đang xem (20 dòng) |

**Chỉ có C1 là chung** — và vẫn phải **tự quan sát lại trong từng case**, ghi riêng cho từng case. **C2 tuyệt đối
không suy chéo:** case 19 có thể xuất đúng toàn bộ danh sách mà vẫn hỏng ở ca 0-kết-quả (ví dụ bỏ qua bộ lọc khi
tập rỗng, hoặc lỗi khi tạo tệp không dòng); ngược lại, case 20 báo "không có dữ liệu" đúng cũng không nói gì về
việc case 19 có xuất đủ số dòng hay không.

---

## 9. Chốt Giai đoạn A

- **C1, C2a = MATCH → route TEST** ⇒ **phải sang Giai đoạn B** để đo (không được chốt Cần BA ngay ở Giai đoạn A).
- **C2b = GAP → route BA**, chỉ đo hiện trạng để làm rõ câu hỏi; **cấm Pass, cấm Reopen riêng vế này**.

**Câu hỏi BA đã soạn sẵn cho vế C2b** (dùng nguyên văn khi kết quả rơi vào nhánh (b)):

> **CẦN BA CONFIRM:** đối tác kỳ vọng — khi bộ lọc màn Kho tài liệu / Bài giảng không có kết quả, hệ thống *"xuất
> danh sách rỗng hoặc hiển thị thông báo không có dữ liệu"*; SRS quy định — **im lặng** cho Nhóm III: FR-III-07
> (`srs-fr-03-dao-tao.md:744–818`, bảng Error Handling `:805–809` chỉ có 3 lỗi về tải tệp), FR-III-08
> (`:821–877`, **không có bảng Error Handling**) và SCR-III-03 (`:1941–1984`) đều không nêu hành vi khi tập kết
> quả rỗng, trong khi module khác đã chốt rõ và chốt **khác nhau** (`srs-fr-13-tv-nhanh.md:155` — chặn xuất, không
> tạo tệp rỗng; `srs-fr-15-ct-htpldn.md:403` + `:409` — hiển thị thông báo); web/dev hiện tại — *(điền sau khi đo)*.
> **Mục đích câu hỏi: bổ sung điều này vào đặc tả SCR-III-03, KHÔNG phải chặn bàn giao.**

**Bảng quyết định đã cam kết TRƯỚC khi đo** (chống đổi chuẩn theo kết quả — luật khoá 5):

| Quan sát ở Giai đoạn B | Verdict logic |
|---|---|
| Không tìm thấy chức năng Xuất Excel (sau khi đã liệt kê DOM + menu phụ + `/api/docs-json`) | **Reopen** (C1 không đạt) |
| Có nút; tệp tải về, mở được, **0 dòng dữ liệu** | Nhánh (a) — mọi vế MATCH đạt ⇒ thuộc nhóm **Pass** |
| Có nút; **không tạo tệp**, hiển thị thông báo không có dữ liệu | Nhánh (b) — expected **THOẢ** (cấm Fail/Reopen), nhưng C2b là GAP ⇒ **Cần BA**; ghi `WEB HIỆN TẠI: đúng kỳ vọng đối tác` + câu hỏi BA ở trên |
| Có nút; tệp tải về nhưng **chứa bản ghi ngoài bộ lọc** (≠ 0 dòng) | **Reopen** (C2a không đạt — vi phạm *"File xuất theo bộ lọc hiện tại"*, `srs-v3.5.md:5570`) |
| Có nút; bấm ra lỗi 4xx/5xx, **không tệp và không thông báo** | **Reopen** (không nhánh nào của mệnh đề HOẶC xảy ra) |
| Vừa có thông báo "không có dữ liệu" vừa có tệp chứa dòng dữ liệu | **Chưa chốt** (hai phép mâu thuẫn) — ghi cả hai, hỏi user |
| Không dựng được bộ lọc 0-kết-quả (T3/T4 không thoả) | **Chưa chốt** — nêu rõ dữ kiện còn thiếu |
