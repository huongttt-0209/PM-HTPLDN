# Bug Report — QTHT Batch 8 (Quản lý tài khoản người dùng — SCR-VIII-03)

| Thông tin | Giá trị |
|-----------|---------|
| **Dự án** | PM HTPLDN — Trợ giúp pháp lý Doanh nghiệp |
| **Môi trường** | https://18.143.165.120.nip.io |
| **Người test** | QA Automation (Chrome DevTools MCP) |
| **Ngày** | 2026-07-21 |
| **Loại test** | UAT re-verify (vòng đầu) — Functional / UI |
| **Round** | Reverify tuần 3 — QTHT Batch 8 |
| **Tài liệu tham chiếu** | `input/srs-update-2026-5-5/srs-fr-10-quan-tri.md` (FR-VIII-15, SCR-VIII-03); `output/UAT_doi-tac/QA_VERIFY_PROTOCOL.md` |

---

## Tổng hợp

Phát hiện các lỗi có SRS reference cụ thể trong Batch 8 (7 case: QLTKND_02·03·06·15·17·25·27). File này chỉ chứa các case verdict **Open**. Case `BA confirm` → `../../ba-confirm/qtht/ba-confirmation-needed-qtht-batch8.md`.

### Severity breakdown

| Tổng | Critical | Major | Medium | Minor | Trivial | Closed | Open |
|------|----------|-------|--------|-------|---------|--------|------|
| 3    | 0        | 0     | 3      | 0     | 0       | 2      | 1    |

## Bug Summary Table

| Bug ID | Severity | Priority | Type | TC Ref | **SRS Reference** | Title | Status |
|--------|----------|----------|------|--------|-------------------|-------|--------|
| BUG-QLTKND_02 | Medium | P2 | UI/UX | QLTKND_02 (row 165) | `SCR-VIII-03 Thành phần row 5–6 (dòng 1649–1650)` · `SM-TAIKHOAN (dòng 2030)` | Bộ lọc: Đơn vị phẳng (không cây) · Trạng thái thiếu "Tất cả" · dư state "Chờ phân quyền" | Closed |
| BUG-QLTKND_03 | Medium | P2 | UI/UX | QLTKND_03 (row 166) | `SCR-VIII-03 Thành phần row 8 (dòng 1652)` · `BA 2026-05-07 Q3` | Thanh thẻ tab trạng thái có 6 thẻ (đặc tả 4), dư thẻ "Chờ phân quyền" (state đã bỏ) — thẻ đã đúng 4, còn sai bảng màu badge cột Trạng thái | Reopen |
| BUG-QLTKND_15 | Medium | P2 | UI/UX | QLTKND_15 (row 168) | `FR-VIII-15 §Error Handling E1 ERR-TK-01 (dòng 727)` | Thêm TK trùng tên đăng nhập → 1 request nhưng hiện 2 thông báo lỗi | Closed |

---

## ~~BUG-QLTKND_02~~ [CLOSED] — Bộ lọc màn Tài khoản: Đơn vị phẳng, Trạng thái thiếu "Tất cả" và dư state "Chờ phân quyền"

> **Re-test:** 2026-07-23 01:17:08 R1 — ✅ PASS (Closed-verified). Bộ lọc Đơn vị nay render dạng cây (AntD tree, node cha "Cục Bổ trợ tư pháp" có caret mở rộng, các Bộ thụt cấp); bộ lọc Trạng thái mặc định "Tất cả" và chỉ còn 4 trạng thái (Chờ kích hoạt / Hoạt động / Tạm khóa / Vô hiệu hóa) — đã bỏ "Chờ phân quyền". Cả 3 điểm khớp KQ mong đợi.

### Mô tả

Trên màn **Quản lý tài khoản người dùng** (SCR-VIII-03, FR-VIII-15), QTHT mở thanh bộ lọc phía trên danh sách. Ba thành phần lọc sai so với đặc tả: (1) bộ lọc "Đơn vị" render **danh sách phẳng** (liệt kê các Bộ) thay vì **cây phân cấp**; (2) bộ lọc "Trạng thái" **không có lựa chọn "Tất cả"** và để **trống mặc định**; (3) bộ lọc "Trạng thái" có **5 giá trị**, dư trạng thái **"Chờ phân quyền"** (đã bị bỏ khỏi đặc tả).

### Các bước tái hiện

1. Đăng nhập `admin` (vai trò **QTHT**) → **Quản trị hệ thống → Tài khoản & phân quyền**.
2. Quan sát thanh bộ lọc: ô "Trạng thái" hiển thị placeholder "Trạng thái" (không có giá trị "Tất cả" mặc định).
3. Mở dropdown "Trạng thái" → đếm được 5 mục: Chờ kích hoạt / **Chờ phân quyền** / Hoạt động / Tạm khóa / Vô hiệu hóa (không có "Tất cả").
4. Mở dropdown "Đơn vị" → danh sách phẳng các Bộ (Bộ Công an, Bộ Công Thương, …), không có node cha/con, không mũi tên mở rộng, không thụt cấp.

### Kết quả mong đợi

- SCR-VIII-03 dòng 1649: bộ lọc Đơn vị = "select **(tree)** — cây đơn vị phân cấp".
- SCR-VIII-03 dòng 1650: bộ lọc Trạng thái = "**Tất cả** / CHO_KICH_HOAT / HOAT_DONG / TAM_KHOA / VO_HIEU_HOA" (có "Tất cả" + đúng **4** trạng thái).
- SM-TAIKHOAN (dòng 2030) + BA chốt 2026-05-07 Q3: chỉ còn **4** trạng thái, **đã bỏ CHO_PHAN_QUYEN**.

### Kết quả thực tế

- Bộ lọc Đơn vị hiển thị **phẳng** (không cây).
- Bộ lọc Trạng thái **không có "Tất cả"**, mặc định **rỗng**, và có **5** giá trị (dư "Chờ phân quyền").

### Bằng chứng

- `image/BUG-QLTKND_02-trangthai-5states.png` — dropdown Trạng thái 5 giá trị, không "Tất cả".
- `image/BUG-QLTKND_02-donvi-flat.png` — dropdown Đơn vị danh sách phẳng.
- Evidence đối tác: `partner-evidence/QLTKND_02.jpg`.

---

## BUG-QLTKND_03 [REOPEN] — Thanh thẻ tab trạng thái có 6 thẻ (đặc tả 4), dư thẻ "Chờ phân quyền"

> **Re-test:** 2026-08-03 18:27:00 R2 — ❌ REOPEN (fix một phần). **Đã hết lỗi gốc:** thanh thẻ nay đúng **4** thẻ — Tất cả 207 / Hoạt động 145 / Chờ kích hoạt 20 / Tạm khóa 2, không còn "Chờ phân quyền"; bấm từng thẻ lọc đúng (`admin` QTHT, build HTPLDN V1.0.4). Ý "thiếu thẻ Vô hiệu hóa" xác nhận **ngoài đặc tả** (`Docs-PM-HTPLDN/…/srs-fr-10-quan-tri.md:1713` chỉ liệt kê 4 thẻ; VO_HIEU_HOA lọc qua select `:1711` — chọn "Vô hiệu hóa" + bấm Tìm kiếm → 38 kết quả). **Còn lại:** ý "Chờ kích hoạt chưa có màu nhấn" **có cơ sở** — `srs-fr-10-quan-tri.md:1720` gán màu cho badge **cột Trạng thái** và 3/4 đang sai: CHO_KICH_HOAT xám `rgb(191,191,191)` (yêu cầu vàng) · TAM_KHOA hổ phách `rgb(212,136,6)` (yêu cầu đỏ) · VO_HIEU_HOA đỏ `rgb(245,34,45)` (yêu cầu đen); chỉ HOAT_DONG xanh `rgb(56,158,13)` đúng.

### Mô tả

Trên màn **Quản lý tài khoản người dùng** (SCR-VIII-03), thanh thẻ tab lọc theo trạng thái hiển thị **6 thẻ**: Tất cả / Hoạt động / Chờ kích hoạt / Tạm khóa / **Chờ phân quyền** / Vô hiệu hóa. Đặc tả chỉ quy định **4 thẻ**; thẻ "Chờ phân quyền" ứng với trạng thái đã bị bỏ.

### Các bước tái hiện

1. Đăng nhập `admin` (vai trò **QTHT**) → **Quản trị hệ thống → Tài khoản & phân quyền**.
2. Quan sát thanh thẻ tab ngay dưới tiêu đề "Tài khoản & phân quyền".
3. Đếm: Tất cả(27) / Hoạt động(19) / Chờ kích hoạt(4) / Tạm khóa / **Chờ phân quyền** / Vô hiệu hóa(4) = 6 thẻ.

### Kết quả mong đợi

- SCR-VIII-03 dòng 1652: Tab = "**Tất cả / Hoạt động / Chờ kích hoạt / Tạm khóa** (số đếm)" — đúng **4** thẻ.
- BA chốt 2026-05-07 Q3 + SM-TAIKHOAN (dòng 2030): đã bỏ trạng thái CHO_PHAN_QUYEN → không được có thẻ "Chờ phân quyền".

### Kết quả thực tế

- Thanh tab có **6** thẻ, trong đó **"Chờ phân quyền"** là trạng thái đã bỏ (không được xuất hiện) và **"Vô hiệu hóa"** không nằm trong danh sách tab của đặc tả.
- Ý phụ của đối tác "thẻ Chờ kích hoạt không có màu vàng": đặc tả không quy định màu cho **thẻ tab**, nhưng `srs-fr-10-quan-tri.md:1720` (SCR-VIII-03 item 15) quy định màu cho **badge cột Trạng thái**. Re-verify 2026-08-03 đo lại badge: 3/4 màu sai đặc tả (chi tiết ở dòng Re-test) → ý này **có cơ sở**, không còn xếp là "không tính là lỗi".

### Bằng chứng

- `image/BUG-QLTKND_03-tabs-6.png` — thanh 6 thẻ tab.
- `image/BUG-QLTKND_03-badge-mau.png` — re-verify 2026-08-03: 4 thẻ đúng, nhưng badge cột Trạng thái sai bảng màu.
- Evidence đối tác: `partner-evidence/QLTKND_03.jpg`.

---

## ~~BUG-QLTKND_15~~ [CLOSED] — Thêm tài khoản trùng tên đăng nhập: 1 request nhưng hiện 2 thông báo lỗi

> **Re-test:** 2026-07-23 01:22:04 R1 — ✅ PASS (Closed-verified). Chạy lại luồng Thêm mới với tên đăng nhập trùng `cbnv_tw` (đo bằng MutationObserver self-check observer=1, 2/2 lần): mỗi lần submit = 1 request `POST /api/v1/tai-khoan` → chỉ còn **1 khung thông báo** "Tên đăng nhập 'cbnv_tw' đã tồn tại". Không tạo bản ghi trùng. Khớp KQ mong đợi (ERR-TK-01: 1 thông báo).

### Mô tả

Trên form **Thêm tài khoản mới** (SCR-VIII-03, FR-VIII-15), khi QTHT nhập **tên đăng nhập đã tồn tại** và bấm "Thêm mới", hệ thống gửi **1 request** (`POST /api/v1/tai-khoan`) nhưng hiển thị **2 thông báo lỗi** cùng lúc: "Username đã tồn tại trong hệ thống" và "Tên đăng nhập '{username}' đã tồn tại". Đặc tả chỉ yêu cầu 1 thông báo. Không tạo bản ghi trùng (chỉ 1 POST, hệ thống từ chối) → lỗi hiển thị FE.

### Các bước tái hiện

1. Đăng nhập `admin` (vai trò **QTHT**) → **Quản trị hệ thống → Tài khoản & phân quyền → Thêm mới**.
2. Nhập Tên đăng nhập = `cbnv_tw` (đã tồn tại), Họ tên bất kỳ, Email mới hợp lệ, chọn Loại TK / Đơn vị / Vai trò.
3. Bấm "Thêm mới".
4. Đo bằng `tools/toast-capture.js` (observer=1 đã self-check): 1 request `POST /api/v1/tai-khoan` → **2 khung thông báo** (2 chữ khác nhau); toast z-index 2010 > modal 1000 (nổi trên modal). Tái hiện ≥5/5 lần.

### Kết quả mong đợi

- FR-VIII-15 §Error Handling E1 (`ERR-TK-01`, dòng 727): username trùng → **1** thông báo "Username '{username}' đã tồn tại".

### Kết quả thực tế

- 1 lần submit → **2** thông báo lỗi cho cùng 1 lần vi phạm.

### Bằng chứng

- `../../reverify-audit/QLTKND_15/toast-capture-measurement.md` — log đo (JSON: 1 request → 2 toast, z-index, self-check observer=1).
- `image/BUG-QLTKND_15-dup-username-toast.png` — form nhập username trùng `cbnv_tw` (toast tự tắt ~3s, khung chụp lỡ nhịp; toast xác nhận qua observer + evidence đối tác).
- Evidence đối tác: `partner-evidence/QLTKND_15.jpg` (hiện đúng 2 toast).
