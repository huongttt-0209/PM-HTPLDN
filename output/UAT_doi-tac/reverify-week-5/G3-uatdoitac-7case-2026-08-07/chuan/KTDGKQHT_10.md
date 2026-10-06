# CHUẨN CHẤM — KTDGKQHT_10 (Lô G3 · khoá TRƯỚC khi đo)

> **Chưa mở màn.** File này khoá chuẩn chấm TRƯỚC khi đo. Sau khi đo, CẤM sửa quan hệ `MATCH / GAP` hay
> đổi tiêu chí Pass/Reopen để khớp kết quả quan sát được.

## 1. Bảng đầu

| Mục | Giá trị |
|---|---|
| Bảng / tab / dòng | Bảng đối tác · tab `bug` · **dòng 11** |
| Mã TC | **KTDGKQHT_10** |
| Mô tả (đối tác) | "Tải lên tệp Excel Kết quả kiểm tra" |
| Trạng thái nguồn | Trạng thái `Fail` · Dopai `N/R` · Trạng thái dev fix `Test done` · Kết quả verify **TRỐNG** |
| TKM phản hồi lần 1 | "Màn hình không có nút chức năng" |
| Env | **`https://htpldn-uat.ospgroup.vn`** (env NGHIỆM THU của đối tác) — MailHog `https://htpldn-uat.ospgroup.vn/mailhog/` |
| Bản dựng | **(để trống — đọc trên UI khi đo)**; bắt buộc tải lại trang rồi mới ghi số hiệu ở sidebar/chân trang |
| Tài khoản dự kiến | `cbnv_tw` / `Test@1234` (vai trò `CB_NV_TW`, cấp TW — bộ tài khoản đã kiểm chứng trên env đối tác). OTP lấy ở MailHog của **chính env này**. Giới hạn đăng nhập 5 lượt/60 giây |
| Vai trò theo đặc tả | **CB NV** (hoặc CB PD) — `srs-fr-03-dao-tao.md:526` ("**Tác nhân:** CB NV / CB PD"); quyền PRE-01 `:534` ("có quyền \"Quản lý kết quả ĐT\"") |
| Màn | Đào tạo, tập huấn → **Khóa học** → chi tiết khóa → **Tab "Kết quả kiểm tra"** (SCR-III-02 Tab 5 — `srs-fr-03-dao-tao.md:522`, `:1924`) |
| URL | Danh sách khóa `…/dao-tao/khoa-hoc/danh-sach`, chi tiết `…/dao-tao/khoa-hoc/{id}` — **dự kiến, xác nhận khi đo** (đường dẫn suy từ báo cáo cũ env nội bộ = ngữ cảnh, chưa có bằng chứng trên env đối tác) |
| SRS đã đọc | `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-03-dao-tao.md` — **2296 dòng** |
| SRS đã đọc | `Docs-PM-HTPLDN/…/srs-v3.5/srs-v3.5.md` — **7012 dòng** |

---

## 2. Nguồn đã đọc (tự mở trong lượt này)

**SRS nguồn chuẩn DUY NHẤT — `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/`:**

| File | Đoạn đã đọc trọn | Nội dung |
|---|---|---|
| `srs-fr-03-dao-tao.md` | `:519–670` | **FR-III-05 (UC24) trọn mục** — Preconditions, Inputs, Processing Nhập thủ công, **Processing Tải mẫu** `:571–583`, **Processing Import Excel** `:585–597`, Processing Xuất Excel `:599–607`, Outputs, **Error Handling** `:631–645`, AC `:647–660`, Edge case `:662–666` |
| `srs-fr-03-dao-tao.md` | `:672–742` | FR-III-06 (UC25) — Tìm kiếm kết quả + Processing Xuất Excel + Error Handling (đọc để loại nhầm phạm vi) |
| `srs-fr-03-dao-tao.md` | `:1292–1310` | FR-III-17 (UC36) — ranh giới nhập liệu vs FR-III-05 |
| `srs-fr-03-dao-tao.md` | `:1552–1594` | FR-III-NEW-04 — gán đề kiểm tra vào khóa (tiền đề bật nút tải mẫu) |
| `srs-fr-03-dao-tao.md` | `:1912–1937` | **SCR-III-02 trọn mục** — 8 tab, đặc biệt Tab 4 `:1919–1923` và **Tab 5 `:1924–1929`** |
| `srs-fr-03-dao-tao.md` | `:2133–2161` | SM-KHOAHOC — 9 trạng thái + transition `DA_CONG_KHAI → DANG_DIEN_RA → DA_KET_THUC` |
| `srs-fr-03-dao-tao.md` | `:2227–2252` | §6 Tổng quan BR sử dụng |
| `srs-fr-03-dao-tao.md` | `:10`, `:14` | Ghi chú sửa đổi 2026-07-30 + **2026-08-04 (KTDGKQHT_05 — cơ chế "Tải mẫu → điền → tải lên")** |
| `srs-v3.5.md` | `:5561–5574` | Phụ lục B.2 BR-DATA (trọn bảng, gồm BR-DATA-06 `:5570`) |

**Quét từ đồng nghĩa đã chạy** (nhiều lệnh, không chỉ 1 grep) — trên `srs-fr-03-dao-tao.md` và **toàn thư mục** `srs-v3.5/`:
`tải lên` · `import` · `Import Excel` · `nhập từ Excel` · `tải mẫu` · `tệp mẫu` · `biểu mẫu mẫu` · `file mẫu` ·
`bản xem trước` · `xem trước` · `preview` · `bản review` · `dòng lỗi` · `dòng hợp lệ` · `số dòng` ·
`bản ghi không hợp lệ` · `đã nạp` · `báo cáo import` · `Kết quả kiểm tra` · `Xuất Excel` · `kết xuất` ·
`export` · `BR-DATA-06` · `danh sách rỗng` · `không có dữ liệu`.

**Kết quả quét đáng chú ý:** cụm `bản ghi không hợp lệ` / `đã nạp` / `số dòng hợp lệ` **không xuất hiện ở bất
kỳ file nào** trong `srs-v3.5/`. Cụm gần nhất là `srs-fr-03-dao-tao.md:593` — *"Hiển thị bản review (thành
công / lỗi) — dòng lỗi ghi rõ mã lỗi + số dòng"*. ⇒ **Câu chữ thông báo mà đối tác kỳ vọng là câu chữ của
phiếu, KHÔNG phải câu chữ đặc tả** (xem vế A3).

**Ngữ cảnh (CHỈ để biết tra chỗ nào — KHÔNG dùng làm căn cứ verdict, không mượn số dòng):**
`output/UAT_doi-tac/bug-con-fail-doi-tac-2026-07-31.md:333` (dòng tổng hợp phiếu) ·
`output/UAT_doi-tac/batch-NR-fixed-2026-08-06/BATCH-PLAN.md:38` · các báo cáo env nội bộ chứa đường dẫn
`/dao-tao/khoa-hoc/{id}`.

---

## 3. Cổng bằng chứng

- **KHÔNG có bằng chứng đối tác** — ô Ảnh/video rỗng, ô "Kết quả thực tế" cũng trống. Chỉ có 1 câu TKM
  *"Màn hình không có nút chức năng"*.
- **Vẫn chạy tiếp.** Thiếu bằng chứng nhưng **tự tái hiện được**, vì cả 4 bước trong phiếu đều là thao tác
  chuẩn trên màn công khai của phần mềm, không cần ID bản ghi riêng của đối tác.
- **Vì sao tái hiện được / rủi ro:** tái hiện được **chỉ khi dựng đủ tiền đề §6**. Đây là case **nặng tiền đề
  nhất** trong lô: nút tải mẫu/tải lên có điều kiện bật rõ ràng trong đặc tả (`:578`), nên "không thấy nút"
  khi chưa dựng đủ tiền đề **KHÔNG chứng minh được gì**.
- **Điều kiện tái hiện sẽ ghi vào báo cáo:** env + bản dựng đọc trên UI · tài khoản thực dùng · mã/tên khóa
  học + **trạng thái khóa tại thời điểm đo** · mã đề kiểm tra đang chọn · số học viên trong khóa · tên tệp
  tải lên + số dòng hợp lệ / dòng cố ý sai đã gài.
- **Neo lấy được từ bằng chứng:** không có → dùng dữ liệu QA tự dựng. **Không đụng dữ liệu đối tác.**

---

## 4. Bảng chuẩn chấm

**Expected đối tác (nguyên văn, 2 gạch đầu dòng):**
1. *"Hiển thị bản xem trước kết quả (số dòng hợp lệ, số dòng lỗi và lý do từng dòng)."*
2. *"Nạp thành công, hệ thống hiển thị thông báo \"Đã nạp {số thành công} bản ghi thành công, {số lỗi} bản ghi không hợp lệ\"."*

| # | Điều kiện của BUG GỐC | Đặc tả nói gì (file:dòng, nguyên văn) | Phép đo quyết định | Pass khi | Reopen khi |
|---|---|---|---|---|---|
| **A1** | Bước 4 của phiếu — *"Tải lên tệp Excel"* — **thực hiện được** trên Tab "Kết quả kiểm tra" của khóa ở "Đang diễn ra"/"Đã kết thúc". Triệu chứng TKM: *"Màn hình không có nút chức năng"* | **MATCH.** `srs-fr-03-dao-tao.md:524` — *"Nhập kết quả đào tạo (điểm danh + kiểm tra). 2 tab: Điểm danh và Kiểm tra. **Hỗ trợ nhập thủ công + import Excel**."* · `:589` bước 1 — *"Upload file Excel (.xlsx)"* · `:1924` (SCR-III-02 Tab 5) — *"**Hỗ trợ Import Excel qua tệp mẫu** — nút \"Tải mẫu điểm kiểm tra\" (bật sau khi chọn đề kiểm tra thuộc khóa, khóa `DANG_DIEN_RA`/`DA_KET_THUC`, có quyền…)"* | Sau khi **đã dựng đủ T2–T4** (§6): liệt kê DOM vùng công cụ Tab 5 — `innerText` **cộng** `title`/`aria-label`/`className` của mọi `button`/`a`/`[role=button]`/`input[type=file]`, mở cả menu phụ (kebab, "Thao tác khác"). Đối chứng độc lập: liệt kê `paths` chứa `ket-qua`/`khoa-hoc` ở `/api/docs-json`, lọc `import`/`upload`/`mau`/`template` — **CẤM đoán đường dẫn** | Tab 5 có đường tải tệp Excel dùng được (bấm được, mở hộp chọn tệp hoặc kéo-thả) khi khóa ở `DANG_DIEN_RA`/`DA_KET_THUC`, đã chọn đề, tài khoản CB NV | Đã dựng đủ T2–T4 mà Tab 5 **không có bất kỳ đường tải tệp nào** (DOM + menu phụ + docs-json đều không có) |
| **A2** | Vế 1 expected — sau khi tải lên, hệ thống **hiển thị bản xem trước** phân biệt **dòng hợp lệ / dòng lỗi** và nêu **lý do từng dòng lỗi** | **MATCH (nội dung).** `:593` bước 5 — *"Hiển thị bản review (thành công / lỗi) — dòng lỗi ghi rõ mã lỗi + số dòng"* · `:594` bước 6 — *"Nếu xác nhận: merge kết quả — **chỉ merge dòng hợp lệ**, dòng lỗi bỏ qua"* · `:650` (AC) — *"**Given** CB NV import Excel **When** upload file **Then** validate + import + báo cáo lỗi"*. Câu chữ mã lỗi tra ở bảng Error Handling `:635–643` (ERR-KQ-01…ERR-KQ-09) | Tải lên tệp mẫu đã gài **cố ý ≥1 dòng lỗi** (T6): đọc `innerText` của khối xem trước hiện ra **trước khi xác nhận** — kiểm 3 điều: (a) có phân nhóm thành công vs lỗi; (b) dòng lỗi chỉ được **số dòng**; (c) dòng lỗi nêu **lý do / mã lỗi**. Ghi nguyên văn | Có bước xem trước trước khi ghi, phân biệt được dòng hợp lệ vs dòng lỗi, và mỗi dòng lỗi có số dòng + lý do (mã lỗi hoặc câu chữ tương ứng bảng `:635–643`) | Nạp thẳng **không có bước xem trước**; hoặc có xem trước nhưng **không** phân biệt hợp lệ/lỗi; hoặc dòng lỗi **không** chỉ ra số dòng, hoặc **không** nêu lý do nào |
| **A3** | Vế 2 expected — sau khi xác nhận nạp, hệ thống **thông báo kết quả nạp** gồm **số bản ghi thành công** và **số bản ghi không hợp lệ** | **MATCH về yêu cầu, GAP về câu chữ.** `:595` bước 7 — *"Trả về báo cáo import"*. SRS **KHÔNG** quy định câu chữ; quét toàn thư mục `srs-v3.5/` cho `đã nạp` / `bản ghi không hợp lệ` / `số dòng hợp lệ` → **0 kết quả** | Cài `output/UAT_doi-tac/tools/toast-capture.js` **TRƯỚC** khi bấm xác nhận (cấm tự viết observer, cấm lọc trùng, cấm `textContent`); bắt nguyên văn thông báo + đếm số lời gọi mạng kèm theo; đối chiếu với thân phản hồi của chính lời gọi import (`list_network_requests`) | Sau khi nạp, hệ thống trả **báo cáo kết quả nạp có cả hai con số** (số ghi nhận được + số bị loại) — bằng lớp nổi, khối tổng kết trên màn, hoặc màn báo cáo import. **Câu chữ khác mẫu của phiếu vẫn Pass** | Nạp xong **không có báo cáo kết quả nào** (không thông báo, không khối tổng kết, thân phản hồi không có số liệu); hoặc báo cáo **chỉ có 1 trong 2 con số** trong khi tệp có cả dòng hợp lệ lẫn dòng lỗi |
| **A4** | Hệ quả bắt buộc của chữ *"Nạp thành công"* — dữ liệu **thật sự vào đúng chỗ**: chỉ dòng hợp lệ được ghi, dòng lỗi bị bỏ qua, điểm ngoài 0–10 **không** bị tự kéo về biên | **MATCH.** `:594` — *"chỉ merge dòng hợp lệ, dòng lỗi bỏ qua"* · `:597` — *"Đặc biệt **cấm tự kéo điểm về biên 0/10 khi import** — dòng có điểm ngoài khoảng phải bị báo lỗi và bỏ qua, không được lặng lẽ ghi giá trị 10."* · `:645` (ghi chú E1) · `:635` (E1 ERR-KQ-01 — *"Điểm kiểm tra phải từ 0 đến 10"*) | Sau khi nạp: **tải lại** Tab 5 → đọc bảng, đối chiếu từng học viên: điểm của dòng hợp lệ = giá trị trong tệp; học viên ở dòng lỗi **không** có điểm mới; dòng gài điểm `15` **không** thành `10`. Đối chứng độc lập: đọc thân phản hồi của lời gọi danh sách kết quả | Bảng sau khi tải lại khớp đúng: dòng hợp lệ có điểm đúng, dòng lỗi không được ghi, không có giá trị bị kéo về biên | Dòng lỗi vẫn được ghi; hoặc điểm `15` bị ghi thành `10`; hoặc điểm ghi lệch với tệp |

### Trích nguyên văn SRS dưới từng vế

**A1 — `srs-fr-03-dao-tao.md:522` (màn hình của FR-III-05):**

```
**Màn hình:** SCR-III-02 (chi tiết Khóa học — Tab 4 "Điểm danh" + Tab 5 "Kết quả kiểm tra") `[KTDGKQHT_05 chốt 2026-08-04 — sửa tham chiếu tab cũ]`
```

**A1 — `srs-fr-03-dao-tao.md:585–595` (trọn bảng Processing — Import Excel):**

```
**Processing — Import Excel `[KTDGKQHT_08 UAT 2026-07-16 — làm rõ import chịu cùng ràng buộc với nhập thủ công; KTDGKQHT_05 chốt 2026-08-04 — nhập theo tệp mẫu]`:**

| Bước | Mô tả xử lý | BR áp dụng |
|------|-------------|-----------|
| 1 | Upload file Excel (.xlsx) | — |
| 2 | Xác nhận tệp theo **đúng bộ cột của tệp mẫu** (mục "Tải mẫu"); thiếu/sai cột → ERR-KQ-02. Xác định **loại bản ghi theo loại tệp mẫu** … đọc `lich_hoc_id` / `de_kiem_tra_id` từ **metadata tệp** và bắt buộc **khớp buổi / đề đang chọn** trên màn; lệch → ERR-KQ-09 | — |
| 3 | **Kiểm tra trạng thái khóa học một lần cho cả file** theo loại import: điểm danh → PRE-03; điểm kiểm tra → PRE-04. Sai → từ chối cả file kèm ERR-KQ-06, không xử lý dòng nào | SM-KHOAHOC |
| 4 | Xác nhận từng dòng dữ liệu … | — |
| 5 | Hiển thị bản review (thành công / lỗi) — dòng lỗi ghi rõ mã lỗi + số dòng | — |
| 6 | Nếu xác nhận: merge kết quả — **chỉ merge dòng hợp lệ**, dòng lỗi bỏ qua | BR-KQ-01, BR-KQ-02 |
| 7 | Trả về báo cáo import | — |
```

**A1 tiền đề — `srs-fr-03-dao-tao.md:537` (PRE-04 — chính là "Điều kiện" ghi trong phiếu):**

```
| PRE-04 | **Nhập điểm kiểm tra:** khóa học ở `DANG_DIEN_RA` **hoặc** `DA_KET_THUC` `[BA chốt 2026-07-16 — Phương án A2]` |
```

**A1 tiền đề — `srs-fr-03-dao-tao.md:575–578` (điều kiện BẬT nút tải mẫu — quyết định "có/không có nút"):**

```
| Loại mẫu | Nút | Ngữ cảnh gắn (metadata tệp) | Điều kiện bật nút |
|----------|-----|------------------------------|-------------------|
| Mẫu điểm danh | "Tải mẫu điểm danh" (Tab 4) | Buổi học đang chọn (`lich_hoc_id`) | Đã chọn buổi + khóa `DANG_DIEN_RA` + khóa có ≥1 buổi học + có quyền nhập điểm danh |
| Mẫu điểm kiểm tra | "Tải mẫu điểm kiểm tra" (Tab 5) | Đề kiểm tra đang chọn (`de_kiem_tra_id`) | Đã chọn đề thuộc khóa + khóa `DANG_DIEN_RA`/`DA_KET_THUC` + có quyền |
```

**A2/A4 — `srs-fr-03-dao-tao.md:582` (bộ cột tệp mẫu điểm kiểm tra — dùng để dựng T5/T6):**

```
  - **Mẫu điểm kiểm tra:** `hoc_vien_id` (điền sẵn, khoá/ẩn) · Họ tên · Email · Đơn vị · **Điểm kiểm tra** (trống — điền 0–10) · Ghi chú.
```

**A2 — `srs-fr-03-dao-tao.md:635–643` (bảng Error Handling của FR-III-05, trọn 9 dòng — nguồn "lý do từng dòng"):**

```
| E1 | Điểm ngoài 0-10 | ERR-KQ-01 | "Điểm kiểm tra phải từ 0 đến 10" | ERROR |
| E2 | File format lỗi | ERR-KQ-02 | "File không đúng định dạng mẫu" | ERROR |
| E3 | Học viên không tồn tại hoặc không thuộc khóa | ERR-KQ-03 | "Không tìm thấy học viên ở dòng {N} (định danh không hợp lệ hoặc không thuộc khóa học này)" | ERROR |
| E4 | diem_danh không thuộc enum … | ERR-KQ-04 | "Giá trị điểm danh không hợp lệ" | ERROR |
| E5 | Xuất Excel vượt 10.000 dòng | ERR-KQ-05 | "Vượt giới hạn 10.000 dòng, vui lòng lọc nhỏ hơn" (BR-DATA-06) | ERROR |
| E6 | Nhập điểm danh khi khóa không ở `DANG_DIEN_RA`, hoặc nhập điểm kiểm tra khi khóa không ở `DANG_DIEN_RA`/`DA_KET_THUC` … | ERR-KQ-06 | … | ERROR |
| E7 | `lich_hoc_id` không thuộc khóa học đang thao tác | ERR-KQ-07 | "Buổi học không thuộc khóa học này" | ERROR |
| E8 | Nhập điểm kiểm tra nhưng thiếu `de_kiem_tra_id`, hoặc đề không thuộc khóa học | ERR-KQ-08 | "Vui lòng chọn đề kiểm tra thuộc khóa học này" | ERROR |
| E9 | Tệp mẫu tải lên không khớp buổi / đề đang chọn (metadata tệp lệch ngữ cảnh) | ERR-KQ-09 | "Tệp mẫu không khớp buổi học / đề kiểm tra đang chọn. Vui lòng tải mẫu đúng và thử lại" | ERROR |
```

> Dòng E3 (`:637`) là bằng chứng đặc tả **có** đòi "lý do kèm số dòng" — câu chữ chứa `{N}`.

**A4 — `srs-fr-03-dao-tao.md:597` (import không được nới lỏng ràng buộc):**

```
> **Import không được nới lỏng ràng buộc `[KTDGKQHT_08 UAT 2026-07-16]`:** import Excel là **đường nhập liệu thứ hai** vào cùng bảng dữ liệu, nên phải chịu **đúng** các ràng buộc trạng thái (PRE-03/PRE-04) và validate như nhập thủ công. Đặc biệt **cấm tự kéo điểm về biên 0/10 khi import** — dòng có điểm ngoài khoảng phải bị báo lỗi và bỏ qua, không được lặng lẽ ghi giá trị 10.
```

### 🔴 Trả lời câu hỏi then chốt

> **SRS có quy định chức năng tải lên tệp Excel Kết quả kiểm tra không? Ở màn nào, tab nào, vai trò nào,
> trạng thái khóa học nào?**

**CÓ — quy định rõ, đủ cả 4 chiều. SRS KHÔNG im lặng.**

| Chiều | Đặc tả | Dòng |
|---|---|---|
| **Có chức năng?** | *"Hỗ trợ nhập thủ công + **import Excel**"* · Processing Import Excel 7 bước · *"Hỗ trợ Import Excel qua tệp mẫu"* | `:524` · `:585–595` · `:1924` |
| **Màn / tab nào?** | SCR-III-02 (chi tiết Khóa học) — **Tab 5 "Kết quả kiểm tra"** | `:522` · `:1924` |
| **Vai trò nào?** | Tác nhân **CB NV / CB PD**; PRE-01 có quyền "Quản lý kết quả ĐT" | `:526` · `:534` |
| **Trạng thái khóa nào?** | PRE-04 — `DANG_DIEN_RA` **hoặc** `DA_KET_THUC` (đúng bằng "Điều kiện" ghi trong phiếu) | `:537` · `:1925` |

**Chỉ có MỘT khoảng trống, và là khoảng trống về CÂU CHỮ, không phải về chức năng:** đặc tả nói *"Trả về
báo cáo import"* (`:595`) mà không quy định mẫu câu. ⇒ **Vế A3 chấm theo nội dung (có đủ 2 con số), CẤM
chấm theo chữ.**

### ⚠️ Đã cân nhắc và LOẠI hai cách hiểu sai

1. **"Đặc tả chỉ có nút *Tải mẫu*, không có nút *Tải lên* → không đòi tải lên."** Loại. `:589` bước 1 ghi
   thẳng *"Upload file Excel (.xlsx)"*, `:653`/`:654` là AC cho hành vi *"tải lên tệp mẫu"*. Đặc tả **không
   đặt tên** cho nút tải lên → theo quy tắc mô tả-yêu-cầu-không-kê-đơn, chấm ở **năng lực tải tệp**, không
   chấm ở nhãn nút.
2. **"Tab 5 chỉ đọc nên không có nút."** Chỉ đúng khi khóa đã ở `CHO_DUYET_KQ` trở đi — `:1929`:
   *"**Chỉ đọc từ `CHO_DUYET_KQ`:** sau khi trình duyệt KQ, bảng chỉ đọc cho tới khi CB PD từ chối"*. ⇒ tiền
   đề T7: **chọn khóa CHƯA trình duyệt kết quả**. Nếu đo nhầm khóa đã trình duyệt thì "không có nút" là
   **đúng đặc tả**, không phải bug.

---

## 5. Đường đo tối thiểu

**Một đường UI ngắn nhất + một đối chứng độc lập. Chạy đúng 4 bước của phiếu, không đổi luồng chính.**

| Bước | Nội dung | Kiểm vế |
|---|---|---|
| U0 | Đăng nhập `cbnv_tw` trên `https://htpldn-uat.ospgroup.vn` (OTP MailHog cùng env), **tải lại trang**, ghi số hiệu bản dựng | tiền đề |
| U1 | (Phiếu bước 1) Chọn menu **"Đào tạo, tập huấn" → "Khóa học"**; ghi URL thực tế | tiền đề |
| U2 | Xác nhận/dựng khóa đúng tiền đề T2–T4 (§6). Ghi mã khóa + **trạng thái đọc trên UI** | tiền đề |
| U3 | (Phiếu bước 2) Nhấn xem chi tiết khóa học | tiền đề |
| U4 | (Phiếu bước 3) Chọn tab **"Kết quả kiểm tra"** | tiền đề |
| U5 | Liệt kê DOM vùng công cụ của tab: mảng `{tag, innerText, title, ariaLabel, className, disabled}` của mọi `button`/`a`/`[role=button]`/`input[type=file]`; mở mọi menu phụ rồi lặp lại | **A1** |
| U6 | Chọn **đề kiểm tra** trên tab (điều kiện bật nút — `:578`), lặp lại U5 để so trước/sau | **A1** |
| U7 | Bấm "Tải mẫu điểm kiểm tra" → **mở tệp bằng `openpyxl`**, đối chiếu bộ cột với `:582` | tiền đề T5 |
| U8 | Điền tệp mẫu: ≥2 dòng điểm hợp lệ (vd `7.5`, `9`) + **≥1 dòng điểm `15`** (gài ERR-KQ-01). Ghi rõ dòng nào gài | tiền đề T6 |
| U9 | Cài `tools/toast-capture.js` **TRƯỚC** khi thao tác | **A2**, **A3** |
| U10 | (Phiếu bước 4) **Tải lên tệp Excel** vừa điền — 1 lần | **A1** |
| U11 | Đọc `innerText` khối xem trước hiện ra **trước khi xác nhận**; chụp màn hình | **A2** |
| U12 | Xác nhận nạp; bắt nguyên văn thông báo + đếm lời gọi mạng | **A3** |
| U13 | **Tải lại** Tab 5, đọc bảng, đối chiếu từng học viên với tệp đã tải lên | **A4** |
| Đối chứng độc lập | `list_network_requests` → mã trạng thái + **thân phản hồi** của lời gọi import và của lời gọi danh sách kết quả sau khi tải lại | **A2·A3·A4** |
| Đối chứng độc lập | `fetch('/api/docs-json')` → `paths` chứa `ket-qua`/`khoa-hoc`, lọc `import`/`upload`/`template`/`mau`. **CẤM đoán đường dẫn** | **A1** |

A1 không đạt ⇒ **A2/A3/A4 không đo được** — ghi rõ là bị chặn bởi A1, **không** suy đoán hệ thống "sẽ" làm gì.

🔴 **CẤM dừng ở "tải lên không báo lỗi".** HTTP 200 chỉ chứng minh nhận tệp, không chứng minh ghi đúng — U13 là bắt buộc.

---

## 6. Tiền đề phải dựng

**Đây là case nặng tiền đề nhất của lô. "Không thấy nút" khi chưa đủ T2–T4 KHÔNG kết luận được gì.**

| # | Tiền đề | Vì sao bắt buộc (dòng SRS) | Cách dựng nếu thiếu |
|---|---|---|---|
| **T1** | Tài khoản vai trò **CB NV** | `:526` tác nhân · `:534` quyền "Quản lý kết quả ĐT" | `cbnv_tw` / `Test@1234` + OTP MailHog env đối tác. Env này **chưa xác nhận có tài khoản anh em** `cbnv_tw_02/_03` → khoá lock thì **DỪNG, báo lead**, cấm đổi sang vai trò/cấp khác |
| **T2** | Khóa học ở **`DANG_DIEN_RA` hoặc `DA_KET_THUC`** (đúng "Điều kiện" của phiếu) | `:537` PRE-04 · `:1925` · `:1927` (khóa chưa bắt đầu → chỉ hiện dòng "Khóa học chưa bắt đầu…") | Ưu tiên **tìm khóa có sẵn** ở 2 trạng thái này (lọc trên danh sách Khóa học). Không có → dựng theo SM-KHOAHOC `:2148–2151`: `DA_DUYET → DA_CONG_KHAI → DANG_DIEN_RA`. Dựng qua API cookie-auth thì **tra đường dẫn ở `/api/docs-json`**, cấm đoán |
| **T3** | Khóa có **≥1 học viên** trong danh sách | `:580` — tệp mẫu *"điền sẵn danh sách học viên của khóa"*; khóa 0 học viên ⇒ mẫu rỗng ⇒ không đo được "nạp {N} bản ghi" | Chọn khóa đã có học viên được duyệt. Không có → seed đăng ký + duyệt (FR-III-03/FR-III-04) rồi ghi rõ đã seed gì |
| **T4** | Khóa có **≥1 đề kiểm tra `KICH_HOAT`** gắn qua Tab 7, và **đã chọn đề** trên Tab 5 | `:578` điều kiện bật nút · `:583` metadata `de_kiem_tra_id` · `:642` ERR-KQ-08 | Vào **Tab 7 "Đề kiểm tra"** → "Thêm đề kiểm tra" (FR-III-NEW-04, `:1552–1574`) chọn đề `KICH_HOAT`. Không có đề nào `KICH_HOAT` → dựng đề ở SCR-III-04 rồi kích hoạt |
| **T5** | **Tệp Excel đúng mẫu** = tệp do **chính hệ thống sinh** ở U7 (không tự chế) | `:590` bước 2 — sai cột → ERR-KQ-02; metadata lệch → ERR-KQ-09 | Bấm "Tải mẫu điểm kiểm tra" của **đúng đề đang chọn**; mở bằng `openpyxl` đối chiếu bộ cột `:582` trước khi điền |
| **T6** | Tệp có **cả dòng hợp lệ lẫn dòng cố ý lỗi** | Không có dòng lỗi thì vế A2 ("số dòng lỗi và lý do từng dòng") và nửa sau của A3 **không đo được** | Điền ≥2 dòng điểm hợp lệ + **≥1 dòng điểm `15`** (ERR-KQ-01, `:635`). Ghi lại chính xác dòng số mấy gài gì |
| **T7** | Khóa **CHƯA** ở `CHO_DUYET_KQ`/`HOAN_THANH` | `:1929` — từ `CHO_DUYET_KQ` bảng **chỉ đọc** ⇒ không có nút là ĐÚNG đặc tả | Kiểm trạng thái khóa trên UI trước khi đo; nếu đã trình duyệt KQ thì **đổi khóa khác**, không log bug |
| **T8** | Ghi **env + bản dựng** sau khi tải lại trang | Luật 4 BRIEF | Đọc ở sidebar/chân trang |

**Nếu không dựng được T2/T3/T4 → verdict "Chưa chốt", nêu rõ dữ kiện còn thiếu. CẤM Pass (BRIEF luật 7).**
**Không đụng dữ liệu đối tác** — chỉ tạo khóa/đề/học viên mang dấu QA + ngày, và khai đầy đủ trong nhật ký đo.

---

## 7. Bẫy đã biết

**Chặn FAIL oan:**

- **(a) 🔴 Nút bị ẩn/mờ ĐÚNG đặc tả khi chưa chọn đề.** `:578` ghi rõ nút chỉ bật *"sau khi chọn đề kiểm tra
  thuộc khóa"*. Kết luận "màn hình không có nút chức năng" khi **chưa chọn đề** là FAIL oan. Bắt buộc so
  DOM **trước và sau** khi chọn đề (U5 vs U6).
- **(b) Nút chỉ có biểu tượng / nằm trong menu phụ / là `input[type=file]` ẩn.** CẤM kết luận "không có nút"
  bằng mắt qua ảnh chụp — phải liệt kê `innerText` **cộng** `title`/`aria-label`/`className` + mở menu phụ.
- **(c) Nhầm "Tải mẫu" với "Tải lên", và nhầm "Xuất Excel" với cả hai.** `:607` phân biệt rõ **tệp mẫu nhập**
  (đầu vào) với **tệp Xuất Excel kết quả** (đầu ra), *"tệp Xuất kết quả KHÔNG dùng để nhập liệu"*. Thấy nút
  "Xuất Excel" **không** chứng minh A1 đạt; thấy "Tải mẫu" cũng chưa đủ — phải có đường **đưa tệp lên**.
- **(d) Đo nhầm Tab 4 "Điểm danh".** Tab 4 và Tab 5 đều có import nhưng **khác ràng buộc** (`:536` PRE-03 chỉ
  `DANG_DIEN_RA`, đóng khi `DA_KET_THUC`). Phiếu này là **Tab 5 "Kết quả kiểm tra"**.
- **(e) Tệp QA tự chế bị từ chối ERR-KQ-02/ERR-KQ-09 → KHÔNG phải bug.** `:590` yêu cầu đúng bộ cột mẫu +
  metadata khớp đề đang chọn. Phải dùng tệp mẫu hệ thống sinh (T5).
- **(f) Câu chữ thông báo khác mẫu trong phiếu.** SRS chỉ nói *"Trả về báo cáo import"* (`:595`) — **CẤM chấm
  Fail vì thông báo không đúng chữ** *"Đã nạp {…} bản ghi thành công, {…} bản ghi không hợp lệ"*. Chấm ở
  **nội dung**: có đủ 2 con số hay không.
- **(g) Khóa đã trình duyệt kết quả → bảng chỉ đọc.** `:1929`. Đổi khóa, không log bug.
- **(h) Đổi vai trò để "cho ra nút".** Nếu A1 không đạt, CẤM đăng nhập `admin` rồi kết luận Pass — vai trò
  của vế là **CB NV** (`:526`).

**Chặn PASS oan:**

- **(i) Chữ người dùng nhìn thấy đọc bằng `innerText`, KHÔNG `textContent`** — `textContent` gom cả node ẩn
  của thư viện giao diện → báo "có thông báo"/"có nút" trong khi người dùng không thấy gì.
- **(j) Thông báo tự tắt.** Dùng `tools/toast-capture.js` cài **TRƯỚC** khi bấm, **cấm lọc trùng**, đếm kèm số
  lời gọi mạng. Không bắt được → dùng **thân phản hồi** của lời gọi import làm bằng chứng mạnh hơn ảnh;
  **không bấm lại chỉ để chụp lại** (bấm lại = nạp lần 2, làm bẩn dữ liệu).
- **(k) "Tải lên không báo lỗi" ≠ "nạp đúng".** U13 bắt buộc: tải lại Tab 5 đối chiếu từng học viên.
- **(l) Điểm `15` âm thầm thành `10`.** `:597` + `:645` cấm tuyệt đối. Đây là **ca PASS-oan nguy hiểm nhất**
  của case này — thông báo có thể báo "nạp 3 thành công, 0 lỗi" mà thực chất đã bóp méo dữ liệu.
- **(m) Xem trước hiện ra nhưng chỉ là danh sách thô.** A2 đòi **phân biệt** hợp lệ/lỗi + **số dòng** + **lý
  do**; bảng liệt kê suông không thoả.
- **(n) Trang cũ / bản dựng cũ.** Tab mở lâu vẫn chạy JS cũ → **tải lại trang** trước lô đo và **ghi bản dựng**.
- **(o) Hai phép đo mâu thuẫn = CHƯA được chốt.** Ví dụ thông báo báo "3 thành công" nhưng bảng chỉ có 2 →
  ghi cả hai, hỏi lead.

---

## 8. Bảng quyết định đã cam kết TRƯỚC khi đo

| Quan sát khi đo | Verdict logic |
|---|---|
| Đã dựng đủ T2–T4, đã chọn đề; DOM + menu phụ + `/api/docs-json` đều **không có đường tải tệp** ở Tab 5 | **Reopen** (A1 không đạt) |
| Có đường tải tệp; xem trước phân biệt hợp lệ/lỗi + số dòng + lý do; xác nhận → báo cáo có **cả 2 con số**; tải lại bảng khớp đúng, điểm `15` bị loại | **Pass** (A1·A2·A3·A4 đạt) |
| Có đường tải tệp nhưng **nạp thẳng, không có bước xem trước** | **Reopen** (A2 không đạt — `:593`) |
| Có xem trước nhưng dòng lỗi **không** nêu số dòng hoặc **không** nêu lý do | **Reopen** (A2 không đạt) |
| Nạp xong **không có báo cáo kết quả nào** (không thông báo, thân phản hồi không có số liệu) | **Reopen** (A3 không đạt — `:595`) |
| Có báo cáo đủ 2 con số nhưng **câu chữ khác** mẫu của phiếu | **Pass** vế A3 — SRS im lặng câu chữ, **cấm Reopen vì chữ** |
| Báo cáo chỉ có 1 con số trong khi tệp có cả dòng hợp lệ lẫn dòng lỗi | **Reopen** (A3 không đạt) |
| Điểm `15` bị ghi thành `10`, hoặc dòng lỗi vẫn được ghi | **Reopen** (A4 không đạt — `:597`, `:645`) |
| Tệp mẫu **đúng đề đang chọn** nhưng bị từ chối ERR-KQ-09 | **Reopen** (A1 không đạt trên thực tế — `:590` chỉ cho phép từ chối khi metadata **lệch**) |
| Không có nút vì **chưa chọn đề** / khóa **chưa bắt đầu** / khóa **đã trình duyệt KQ** | **KHÔNG phải bug** — dựng đủ tiền đề rồi đo lại (`:578`, `:1927`, `:1929`) |
| Không dựng được T2/T3/T4 (không có khóa đúng trạng thái / không có học viên / không có đề `KICH_HOAT`) | **Chưa chốt** — nêu rõ dữ kiện còn thiếu, **CẤM Pass** |
| Hai phép đo mâu thuẫn (thông báo vs bảng sau khi tải lại) | **Chưa chốt** — ghi cả hai, hỏi lead |
