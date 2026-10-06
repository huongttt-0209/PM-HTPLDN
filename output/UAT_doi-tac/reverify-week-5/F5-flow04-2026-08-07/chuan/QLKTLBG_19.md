# CHUẨN CHẤM — QLKTLBG_19 (Flow 04 · Giai đoạn A)

> **Giai đoạn A — chưa mở màn.** File này khoá chuẩn chấm TRƯỚC khi đo. Sau khi mở màn, CẤM đổi quan hệ
> `MATCH/DIFF/GAP` để khớp kết quả (Flow 04 luật khoá 5).

## 1. Bảng đầu

| Mục | Giá trị |
|---|---|
| Bảng / tab / dòng | Bảng đối tác 2026-08-07 · tab `bug` · **dòng 13** |
| Mã TC | **QLKTLBG_19** |
| Mô tả (đối tác) | "Xuất excel không có điều kiện lọc" |
| Trạng thái nguồn | Trạng thái `Fail` · Dopai `N/R` · Trạng thái dev fix `Fixed` · DEV phản hồi lần 1 (trống) |
| TKM phản hồi lần 1 | "Màn hình không có nút chức năng" |
| Env | `https://18.143.165.120.nip.io` |
| Bản dựng | Đọc ở chân/sidebar khi đo (tiền lệ tuần 2: `HTPLDN · V1.0.5`) — **bắt buộc tải lại trang rồi mới ghi** |
| Tài khoản dự kiến | `cbnv_tw_02` / `Test@1234` · OTP MailHog `http://18.143.165.120:8025` |
| Vai trò theo đặc tả | **CB NV** — `srs-fr-03-dao-tao.md:751` ("Tác nhân: CB NV / CB PD"), `:828`; quyền PRE-01 `:757` |
| Màn | Đào tạo, tập huấn → **Kho tài liệu / Bài giảng** → Danh sách (SCR-III-03) |
| URL | `https://18.143.165.120.nip.io/dao-tao/bai-giang/danh-sach` |
| SRS đã đọc | `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-03-dao-tao.md` — **2296 dòng** |
| SRS đã đọc | `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-v3.5.md` — **7012 dòng** |

---

## 2. Nguồn đã đọc (tự mở trong lượt này)

**SRS nguồn chuẩn DUY NHẤT — `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/`:**

| File | Đoạn đã đọc trọn | Nội dung |
|---|---|---|
| `srs-fr-03-dao-tao.md` | `:744–818` | FR-III-07 Quản lý kho tài liệu, bài giảng (UC26) — trọn mục: Preconditions · Inputs · Processing · Outputs · Postconditions · Error Handling · Acceptance Criteria |
| `srs-fr-03-dao-tao.md` | `:821–877` | FR-III-08 Tìm kiếm tài liệu (UC27) — trọn mục |
| `srs-fr-03-dao-tao.md` | `:1941–1984` | **SCR-III-03 Kho tài liệu / Bài giảng** — trọn 6 Thành phần + Quy tắc nghiệp vụ |
| `srs-fr-03-dao-tao.md` | `:2227–2251` | §6 Business Rules liên quan — bảng Tổng quan BR sử dụng |
| `srs-v3.5.md` | `:5561–5574` | Phụ lục B.2 BR-DATA (trọn bảng, gồm header cột `:5563`) |
| `srs-v3.5.md` | `:692` | Pattern P-01 "Danh sách quản lý" |
| `srs-v3.5.md` | `:861` | EC-DATA-PAGE — ràng buộc phân trang / tổng số bản ghi |

**Quét từ đồng nghĩa đã chạy trên `srs-fr-03-dao-tao.md`** (không chỉ 1 lệnh grep): `Xuất Excel` · `xuất excel` ·
`Xuất file` · `kết xuất` · `export` · `tải xuống` · `Tải về` · `xuất tệp` · `xuất danh sách` · `tiêu chí lọc` ·
`không có dữ liệu` · `danh sách rỗng` · `Không tìm thấy` · `Chưa có dữ liệu` · `trạng thái trống` · `Empty state`.
Quét thêm toàn thư mục `srs-v3.5/` cho `BR-DATA-06`, `_EXPORT`, `BAI_GIANG`.

**Ngữ cảnh (CHỈ để biết tra chỗ nào — KHÔNG dùng làm căn cứ verdict, không mượn số dòng):**
`output/UAT_doi-tac/reverify-week-2/verify1-conlai-2026-08-03/bug-reports/dao-tao/bug-report-dao-tao.md` (URL màn +
env) · `output/UAT_doi-tac/reverify-week-2/cond/QLKTLBG_02-r2.md` (màn có chip "Bộ lọc nâng cao (2)" mặc định).

---

## 3. Cổng bằng chứng

- **Không có bằng chứng đối tác** cho case này — ô Ảnh/video rỗng thật (đã kiểm cả link ẩn trong ô). Ô "Kết quả
  thực tế" cũng trống.
- **Vẫn chạy tiếp** theo Flow 04 §Cổng bằng chứng: *"Thiếu bằng chứng nhưng tự tái hiện được → chạy tiếp và ghi
  điều kiện đã tái hiện."* **CẤM kết luận "không phải lỗi" chỉ vì không có bằng chứng.**
- **Vì sao tái hiện được:** các bước của đối tác chỉ có 2 bước, không cần tiền đề đặc biệt, không cần ID bản ghi
  cụ thể — (1) vào menu Đào tạo, tập huấn → Kho tài liệu / Bài giảng; (2) nhấn Xuất excel. Điều kiện "không có
  điều kiện lọc" tự dựng được bằng cách để trống toàn bộ thanh lọc.
- **Điều kiện tái hiện sẽ ghi vào báo cáo:** env + bản dựng · tài khoản thực dùng · URL màn · trạng thái thanh
  lọc lúc bấm (chụp/liệt kê) · tổng số bản ghi màn hiển thị lúc bấm.
- **Neo lấy được từ bằng chứng:** không có → dùng dữ liệu QA sẵn có trên màn, **không đụng dữ liệu đối tác**.

---

## 4. BUG SCOPE LOCK

Expected đối tác (nguyên văn): **"Hệ thống xuất toàn bộ danh sách hiện có trên bảng danh sách"**

| Vế | Expected đối tác (nguyên văn / tách vế) | SRS `file:dòng` | Quan hệ | Route | Đường đo |
|---|---|---|---|---|---|
| **C1** | Bước 2 "Nhấn Xuất excel" **thực hiện được** — màn Kho tài liệu / Bài giảng phải có chức năng Xuất Excel (triệu chứng TKM: "Màn hình không có nút chức năng") | `srs-fr-03-dao-tao.md:1952` + `srs-v3.5.md:5570` | **MATCH** | **TEST** | Đường UI: mở `/dao-tao/bai-giang/danh-sach`, liệt kê **innerText** toàn bộ thanh công cụ + nhãn ẩn (`aria-label`/`title`) của mọi `button`/`a` trong vùng tiêu đề, kể cả trong menu phụ (kebab/"…"). Đối chứng độc lập: liệt kê path đã công bố ở `/api/docs-json` có chứa `bai-giang`, lọc path/summary có `export`/`excel` |
| **C2** | "**xuất toàn bộ danh sách hiện có trên bảng danh sách**" khi **không đặt điều kiện lọc** — tệp phải chứa toàn bộ tập bản ghi của bộ lọc hiện tại (không cắt còn trang đang xem) | `srs-fr-03-dao-tao.md:1952` + `srs-v3.5.md:5570` | **MATCH** | **TEST** | Đường UI: để trống thanh lọc → bấm Xuất Excel → lấy tệp. Đối chứng độc lập: **mở tệp bằng `openpyxl`** đếm số dòng dữ liệu (trừ dòng tiêu đề) và so với **tổng số bản ghi** lấy từ phản hồi danh sách của trang (`list_network_requests` → `total`/`total_count` của lời gọi danh sách), KHÔNG so với con số tự đếm bằng mắt |

### Trích nguyên văn SRS dưới từng vế

**C1 — `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-03-dao-tao.md:1941`** (tiêu đề mục):

```
### SCR-III-03: Kho tài liệu / Bài giảng (sub-menu 4) `[v3.5 — đẩy số sub-menu do SCR-III-00 thêm mới]` `[BA chốt 2026-07-30 — QLKTLBG_02 UAT tuần 2 vòng 2: nội hóa bảng cột từ MH-03.3, bổ sung 3 cột Ảnh đại diện · Lĩnh vực · Người tạo]`
```

**C1 — `srs-fr-03-dao-tao.md:1949–1952`** (Thành phần 2 — dòng quyết định là `:1952`):

```
**Thành phần 2 — Tiêu đề + Hành động chính:**
- Tiêu đề trang: "Kho tài liệu & bài giảng"
- Nút "+ Thêm mới" (chính): mở biểu mẫu thêm bài giảng
- Nút "Xuất Excel" (phụ): xuất danh sách theo bộ lọc hiện tại, tối đa 10.000 dòng (BR-DATA-06)
```

**C1 + C2 — `srs-v3.5.md:5570`** (Phụ lục B.2, BR-DATA-06; header cột tại `:5563` là
`| ID | Phát biểu quy tắc | Nguồn | Áp dụng FR | Ngoại lệ | Kiểm chứng |`):

```
| BR-DATA-06 | **Export Excel:** Mọi danh sách có tính năng xuất Excel. File xuất theo bộ lọc hiện tại, không vượt quá 10,000 rows/file | Pattern IP-01 | Toàn bộ CRUD list | Báo cáo nhóm IX có xuất PDF theo khung TT 17/2025 | Test export limit |
```

→ Cột **"Áp dụng FR" = "Toàn bộ CRUD list"**; cột **"Ngoại lệ"** chỉ liệt kê *"Báo cáo nhóm IX có xuất PDF theo
khung TT 17/2025"* — **không có ngoại lệ nào cho Nhóm III / SCR-III-03**.

**C1 — `srs-v3.5.md:692`** (Pattern P-01, chứng cứ bổ trợ — UC26/UC27 nằm trong dải UC20-38 của nhóm III):

```
| P-01 | Danh sách quản lý (List Management) | Bảng dữ liệu + Tìm kiếm + Lọc + Phân trang (10/20/50/100 bản ghi/trang, hiển thị tổng số bản ghi) + CRUD + Xuất Excel + Chọn hàng loạt + **Tabs trạng thái** (context-sensitive batch actions per tab) | ~60% UC: II (UC10-19), III (UC20-38), IV (UC39-50), ... |
```

**C2 — `srs-v3.5.md:861`** (EC-DATA-PAGE — cơ sở để lấy "tổng số bản ghi" trên màn làm mốc so):

```
> **EC-DATA-PAGE — Ràng buộc Pagination:** Số bản ghi/trang nằm trong khoảng [1, 100], mặc định 20. ... **(S3-1)** Cho phép thay đổi số bản ghi/trang: 10, 20, 50, 100. Luôn hiển thị tổng số bản ghi ở màn danh sách.
```

**C2 — `srs-fr-03-dao-tao.md:1976`** (Thành phần 5 — phân trang của chính màn này):

```
**Thành phần 5 — Phân trang:** mặc định 20 dòng/trang; cho phép 10/20/50/100.
```

**C2 — `srs-fr-03-dao-tao.md:1981`** (Quy tắc nghiệp vụ — giới hạn "toàn bộ" theo đơn vị):

```
- Danh sách lọc theo đơn vị sở hữu (`don_vi_id`) theo BR-AUTH-08.
```

### 🔴 Trả lời câu hỏi then chốt

> **SRS có quy định màn Kho tài liệu / Bài giảng phải có chức năng Xuất Excel không?**

**CÓ — quy định rõ, ở cấp màn hình.** `srs-fr-03-dao-tao.md:1952` liệt kê nút "Xuất Excel" là **Hành động chính**
(Thành phần 2) của SCR-III-03 và dẫn thẳng BR-DATA-06. BR-DATA-06 (`srs-v3.5.md:5570`) phát biểu *"Mọi danh sách
có tính năng xuất Excel"*, **Áp dụng FR = "Toàn bộ CRUD list"**, và **ngoại lệ duy nhất là Báo cáo nhóm IX** —
không loại trừ Nhóm III.

→ **Route TEST · quan hệ MATCH · thiếu nút = Reopen.**

### ⚠️ Đã cân nhắc và LOẠI khả năng "SRS im lặng / ngược expected"

Một điểm dễ đọc nhầm thành ngoại lệ: bảng §6 "Tổng quan BR sử dụng" tại `srs-fr-03-dao-tao.md:2243` ghi

```
| BR-DATA-06 | Export Excel | FR-III-01, FR-III-05, FR-III-06, FR-III-14 |
```

tức **không liệt kê FR-III-07 / FR-III-08**. **Đây KHÔNG phải mệnh đề ngoại lệ**, vì:

1. Đó là **bảng mục lục tham chiếu chéo cấp FR**, cột thứ 3 tên là *"FR áp dụng (trong nhóm này)"* — nó không phát
   biểu quy tắc, không dùng từ "không áp dụng" / "ngoại lệ" cho FR nào.
2. Ngoại lệ của BR-DATA-06 nằm ở **cột "Ngoại lệ" của chính BR** (`srs-v3.5.md:5570`) và chỉ có một mục: *Báo cáo
   nhóm IX*. BR dạng "Áp dụng: Toàn bộ…" là **default áp dụng**; muốn loại trừ phải có dòng SRS nói rõ — **không có**.
3. Đặc tả **cấp màn hình** (`:1952`) nói rõ màn này CÓ nút Xuất Excel và dẫn đúng BR-DATA-06 → đây là căn cứ
   nghiệm thu của màn (xem thêm `:1945`: *"Bảng cột đã nội hóa xuống dưới — khi hai bên khác nhau thì lấy mục này
   làm căn cứ nghiệm thu"*).

→ **Không đổi quan hệ.** Ghi nhận riêng **1 dòng candidate tài liệu** (không phải bug phần mềm, không đổi verdict):
*"Bảng §6 `srs-fr-03-dao-tao.md:2243` thiếu FR-III-07/FR-III-08 ở dòng BR-DATA-06 trong khi SCR-III-03:1952 dẫn
BR-DATA-06 — đề nghị BA bổ sung cho khớp mục lục."*

---

## 5. Đường đo tối thiểu

**Một đường UI ngắn nhất + một đối chứng độc lập cho mỗi vế. Đủ thì dừng.**

### 5.1. Nhánh — nút Xuất Excel **KHÔNG tồn tại** (đúng triệu chứng TKM)

| Bước | Nội dung | Kiểm vế |
|---|---|---|
| U1 | Đăng nhập `cbnv_tw_02`, **tải lại trang**, ghi bản dựng ở sidebar | tiền đề |
| U2 | Vào Đào tạo, tập huấn → Kho tài liệu / Bài giảng; xác nhận URL `/dao-tao/bai-giang/danh-sach` | tiền đề |
| U3 | `evaluate_script` liệt kê **innerText** của vùng tiêu đề + thanh công cụ; **kèm** mảng `{tag, innerText, title, ariaLabel, className}` của **mọi** `button`/`a`/`[role=button]` trong vùng đó (bắt được nút chỉ có icon, không nhãn) | **C1** |
| U4 | Mở mọi menu phụ tìm được ở U3 (kebab `…`, "Thao tác khác", dropdown) rồi lặp lại U3 cho nội dung menu vừa mở | **C1** |
| Đối chứng độc lập | `fetch('/api/docs-json')` → liệt kê **key `paths`** có chứa `bai-giang`; lọc tiếp path/summary chứa `export`/`excel`/`xuat`. **CẤM tự đoán đường dẫn endpoint** — chỉ đọc danh sách đã công bố | **C1** |

**Cách đọc kết quả đối chứng:** có endpoint export nhưng UI không có nút → thiếu ở giao diện; không có cả hai →
thiếu toàn phần. Cả hai đều làm **C1 không đạt**; ghi rõ nhánh nào để dev biết chỗ sửa (mô tả yêu cầu, **không kê
đơn** cách implement).

### 5.2. Nhánh — nút Xuất Excel **CÓ tồn tại**

| Bước | Nội dung | Kiểm vế |
|---|---|---|
| U1–U2 | như trên | tiền đề |
| U3 | Xác nhận thanh lọc **rỗng** (xoá bộ lọc nếu có chip mặc định), ghi lại nguyên trạng thái lọc | tiền đề C2 |
| U4 | Ghi **tổng số bản ghi** màn hiển thị + `total`/`total_count` trong phản hồi lời gọi danh sách (`list_network_requests`) | mốc so C2 |
| U5 | Bấm **Xuất Excel** (UI thật, 1 lần) | **C1** + **C2** |
| Đối chứng độc lập | **MỞ TỆP** đọc nội dung: `openpyxl.load_workbook(path, read_only=True)` → đếm **số dòng dữ liệu** (tổng dòng − dòng tiêu đề) và đối chiếu với số ở U4 | **C2** |

**Lấy tệp về để mở — thử theo thứ tự, dừng khi được:**
1. Kiểm `~/Downloads` sau khi bấm (tiền lệ: xuất PDF có rơi về `~/Downloads`).
2. Nếu Chrome MCP `--isolated` không đổ file ra đĩa: đọc nội dung **ngay trong trang** — `fetch` lại đúng URL tệp
   mà lời gọi tải đã dùng (lấy từ `list_network_requests`, **không đoán**) → parse EOCD + `DecompressionStream`
   → chỉ trả về số dòng/ô cần đo, không dump base64.
3. Ghi lại đường dẫn tệp / manifest nội dung để verdict truy lại được.

🔴 **CẤM dừng ở "tải được tệp".** HTTP 200 + binary chỉ chứng minh CREATE, không chứng minh CORRECT.

---

## 6. Tiền đề tối thiểu

| # | Tiền đề | Cách thoả |
|---|---|---|
| T1 | Tài khoản đúng vai trò **CB NV** (`srs-fr-03-dao-tao.md:751`, `:828`) | `cbnv_tw_02` / `Test@1234`, OTP MailHog. Lock account → fallback SAME role+cấp (`_03`), **ghi account thực dùng** |
| T2 | Màn danh sách có **≥ 1 bản ghi** (để "toàn bộ danh sách" có nghĩa và đếm được) | **Ưu tiên dùng dữ liệu QA sẵn có** — tiền lệ tuần 2 màn này có 5–8 bản ghi. Chỉ khi màn = 0 bản ghi mới seed **1** bài giảng qua **luồng UI Thêm mới** (`srs-fr-03-dao-tao.md:775–785`); nếu seed phải khai: **đổi bản ghi nào · đổi gì · env nào** |
| T3 | Thanh lọc **rỗng** đúng nghĩa "không có điều kiện lọc" | Bấm "Xóa bộ lọc" (`:1960`); nếu màn vẫn hiện chip mặc định (tiền lệ "Bộ lọc nâng cao (2)") thì **ghi nguyên trạng** và vẫn so với tổng bản ghi ĐANG hiển thị (cùng bộ lọc) — xem bẫy (f) |
| T4 | Tổng bản ghi **≤ 10.000** | Đọc tổng ở U4. Nếu > 10.000 thì việc hệ thống từ chối là **đúng đặc tả** (`srs-v3.5.md:5570`), không phải lỗi |
| T5 | Ghi **env + bản dựng** sau khi tải lại trang | Sidebar/chân trang |

**Không đụng dữ liệu đối tác.** Không chạy lại vòng đời, không tạo mới nếu dữ liệu QA sẵn có còn dùng được.

---

## 7. Bẫy chặn FAIL oan / PASS oan

**Chặn FAIL oan:**

- **(b) Nút có thể nằm trong menu phụ hoặc là icon không nhãn.** CẤM kết luận "không có nút" bằng mắt qua ảnh
  chụp. Phải liệt kê DOM thanh công cụ: `innerText` **cộng** `title` / `aria-label` / `className` của mọi
  `button`/`a`/`[role=button]`, và phải mở thử menu phụ trước khi chốt C1.
- **(e) Nhầm "Tải về" ở cột Hành động với "Xuất Excel".** `srs-fr-03-dao-tao.md:1974` — *"Hành động | — | Xem trực
  tuyến · Tải về (chỉ Slide/PDF) · Sửa · Xóa (xóa mềm, có hộp xác nhận)"*. "Tải về" là tải **tệp bài giảng của
  một dòng**, KHÔNG phải xuất danh sách. Có "Tải về" ≠ có "Xuất Excel".
- **(f) Chip bộ lọc mặc định.** Màn này từng hiển thị chip "Bộ lọc nâng cao (2)" ngay khi vào. Nếu không xoá được,
  vẫn đo được: so số dòng tệp với **tổng bản ghi đang hiển thị dưới cùng bộ lọc đó**, không so với toàn bộ DB.
- **(g) Phạm vi đơn vị.** `srs-fr-03-dao-tao.md:1981` — danh sách lọc theo `don_vi_id` (BR-AUTH-08). "Toàn bộ danh
  sách" = toàn bộ trong phạm vi tài khoản, KHÔNG phải toàn bộ bản ghi hệ thống.
- **(h) Trần 10.000 dòng** (`srs-v3.5.md:5570`) — từ chối khi vượt trần là đúng đặc tả.
- **(i) SRS Nhóm III KHÔNG quy định bộ cột của tệp xuất cho SCR-III-03.** Khác với FR-III-01 (`:180–184`),
  FR-III-05 (`:599`), FR-III-06 (`:703`) là các màn khác có mục "Processing — Xuất Excel" riêng; FR-III-07
  (`:744–818`) và FR-III-08 (`:821–877`) **không có mục này**. ⇒ **CẤM chấm Fail vì thiếu/thừa cột, sai thứ tự
  cột, sai định dạng ngày, sai tên sheet.** Nếu tệp không có cột nào nhận diện được bản ghi → ghi **candidate 1
  dòng** + câu hỏi BA, không tự chấm Fail.
- **(j) Đổi vai trò để "cho ra nút".** Nếu C1 không đạt, CẤM đăng nhập `admin` rồi kết luận Pass — vai trò của vế
  là **CB NV** (`:751`). Tài khoản quản trị chỉ dùng chuẩn bị dữ liệu / điều tra.

**Chặn PASS oan:**

- **(d) Tải được tệp ≠ nội dung đúng.** Bắt buộc mở tệp bằng `openpyxl` và đếm dòng dữ liệu. Toast "Xuất thành
  công" và HTTP 200 **không** thay được việc mở tệp.
- **(i-2) Tệp chỉ chứa trang đang xem.** Nếu tổng bản ghi > số dòng/trang (mặc định 20 — `:1976`) mà tệp chỉ có
  đúng số dòng của trang hiện tại → **C2 KHÔNG đạt** (`:1952` nói "theo bộ lọc hiện tại", không nói "theo trang").
  Vì vậy tiền đề nên có **> 20 bản ghi** nếu dữ liệu cho phép; nếu ≤ 20 thì phép đo không phân biệt được
  trang-vs-toàn-bộ → **ghi rõ giới hạn này trong báo cáo**, đừng Pass như thể đã chứng minh.
- **(c) Chữ người dùng nhìn thấy đọc bằng `innerText`, KHÔNG `textContent`** — `textContent` gom cả node ẩn của
  AntD → sinh "bug ma" hoặc ngược lại báo có nút trong khi nút đang ẩn.
- **(k) Trang cũ / bản dựng cũ.** Tab MCP mở lâu vẫn chạy JS cũ → **tải lại trang** trước lô đo và **ghi tên bản
  dựng**; đã có tiền lệ Reopen oan vì bỏ bước này.
- **(l) Hai phép đo mâu thuẫn = CHƯA được chốt.** Số dòng tệp ≠ tổng bản ghi từ phản hồi danh sách → ghi cả hai,
  hỏi user, không tự chọn số nào.

---

## 8. Điểm KHÁC NHAU với QLKTLBG_20 — cấm suy verdict chéo

Hai case **cùng màn** (`/dao-tao/bai-giang/danh-sach`), **cùng câu triệu chứng TKM** ("Màn hình không có nút chức
năng"), nhưng **khác vế đo**. Flow 04 BƯỚC 0: *"đo từng case trên đúng màn của nó. Cấm đo 1 case rồi suy cho các
case còn lại — cùng chữ không có nghĩa cùng nguyên nhân."*

| | QLKTLBG_19 (file này) | QLKTLBG_20 |
|---|---|---|
| Điều kiện lọc | **Không đặt** bộ lọc | **Có** bộ lọc, cố ý cho ra **0 kết quả** |
| Tập dữ liệu lúc bấm | ≥ 1 bản ghi | 0 bản ghi |
| Vế nội dung (C2) | Tệp phải chứa **toàn bộ** danh sách | Kết quả là mệnh đề **HOẶC**: tệp rỗng **hoặc** thông báo không có dữ liệu |
| Quan hệ với SRS | C1 MATCH · C2 **MATCH** | C1 MATCH · C2a MATCH · **C2b GAP** (SRS Nhóm III im lặng về nhánh "chặn xuất + báo") |
| Route | TEST toàn bộ | TEST + **có nhánh phải chuyển BA** |
| Phép đo quyết định | Đếm dòng dữ liệu trong tệp = tổng bản ghi | Đếm dòng dữ liệu = 0 **hoặc** bắt nguyên văn thông báo |

**Chỉ có C1 là chung.** Nếu C1 không đạt ở case này thì cũng phải **tự đo C1 lại trong case 20** (cùng phiên vẫn
phải ghi quan sát riêng cho từng case) — nhưng **C2 tuyệt đối không suy chéo**: C2 của 19 đạt không nói gì về C2
của 20, và ngược lại. Trường hợp riêng của case 20 (0 kết quả) là ca biên mà C2 của case 19 chưa từng chạm tới.

---

## 9. Chốt Giai đoạn A

- Mọi vế đều **MATCH** → **route TEST**, chuyển sang Giai đoạn B để đo.
- Chưa có vế `DIFF`/`GAP` ⇒ **chưa có câu hỏi BA** cho case này (chỉ có 1 candidate tài liệu ở §4, không chặn
  verdict).
- **Chưa kết luận verdict** ở Giai đoạn A (đúng phạm vi nhiệm vụ).

**Bảng quyết định đã cam kết TRƯỚC khi đo** (chống đổi chuẩn theo kết quả — luật khoá 5):

| Quan sát ở Giai đoạn B | Verdict logic |
|---|---|
| Không tìm thấy chức năng Xuất Excel (sau khi đã liệt kê DOM + menu phụ + `/api/docs-json`) | **Reopen** (C1 không đạt) |
| Có nút; tệp mở được; số dòng dữ liệu = tổng bản ghi màn (bộ lọc rỗng) | **Pass** |
| Có nút; tệp chỉ chứa trang đang xem trong khi tổng > số dòng/trang | **Reopen** (C2 không đạt) |
| Có nút; bấm ra lỗi 4xx/5xx, không có tệp, hoặc tệp mở không được | **Reopen** (C2 không đạt) |
| Có nút; tệp có dữ liệu nhưng số dòng ≠ tổng và không giải thích được | **Chưa chốt** (hai phép mâu thuẫn) |
| Tổng bản ghi > 10.000 và hệ thống từ chối kèm hướng dẫn lọc nhỏ hơn | **Không phải lỗi** — đúng `srs-v3.5.md:5570` |
