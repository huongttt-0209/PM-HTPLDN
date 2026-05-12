# Test Cases PASS — hop-dong-tv
> **Nguồn**: result-hop-dong-tv-all.md
> **Ngày tổng hợp**: 2026-05-11
> **Phạm vi**: chỉ Result ∈ {PASS, PASS-DEVIATE, PASS-RESOLVED}

## Summary

| File test-case | Total PASS |
|----------------|------------|
| 01-TC-quan-ly-hd-tv-CRUD | 18 |
| 05-TC-tim-kiem-hd-tv | 5 |
| 06-TC-permission-matrix | 1 |
| **Tổng** | **24** |

> Note: `PASS` đã gồm các biến thể "PASS (partial)" / "PASS (qua PATCH)" / "PASS (UI surface)" / "PASS (discovery resolved SPEC-CLARIFY)" — normalize về `PASS` theo token đầu tiên. Không có dòng `PASS-DEVIATE` hoặc `PASS-RESOLVED` trong source.

---

## 01-TC-quan-ly-hd-tv-CRUD

> Source TC: `c:\HoaAG\LuatDN5\Ver3.1\output\test-cases\hop-dong-tv\01-TC-quan-ly-hd-tv-CRUD.md`
> Source report: `c:\HoaAG\LuatDN5\Ver3.1\output\execution-test\hop-dong-tv\report-01-TC-quan-ly-hd-tv-CRUD\Tcs-report\01-TC-quan-ly-hd-tv-CRUD-execution-report-2026-05-11.md`

| ID | TraceID (Mã SRS) | Tên Test Case | Pre-conditions (Tiền đề) | Test Data (Dữ liệu) | Các bước thực hiện | Kết quả mong đợi | Type (Happy/Negative/Edge) | Kết quả test (Result) | Chi tiết |
|----|------------------|---------------|--------------------------|---------------------|--------------------|------------------|----------------------------|------------------------|----------|
| TC-HDTV-001 | FR-X.3-01 / Processing step 1-8 | Tạo HĐ thành công — happy path | cb_nv_tw_01 login. TVV "Nguyễn Văn A" trạng thái HOAT_DONG. | ten="Tư vấn pháp lý DN ABC", ben_b="Nguyễn Văn A", tvv_id=TVV001, gia_tri=50_000_000, thoi_han_bat_dau=2026-06-01, thoi_han_ket_thuc=2026-12-31 | 1. Vào "Quản lý HĐ tư vấn" → click [+ Thêm hợp đồng]. 2. Nhập 6 trường bắt buộc + chọn TVV. 3. Click [Lưu]. | (1) POST `/hop-dong-tv` 201. (2) ma_hop_dong tự sinh `HDTV-20260510-001` (BR-DATA-04). (3) ben_a = "Bộ Tư pháp" (auto từ TW). (4) trạng_thái=`DANG_THUC_HIEN`. (5) Audit log INSERT (BR-DATA-05). | Happy 🔴 | PASS |  |
| TC-HDTV-002 | FR-X.3-01 / Processing Cập nhật | Sửa HĐ thành công | cb_nv_tw_01 login. HĐ HDTV-20260510-001 (DANG_THUC_HIEN). | ten="Tư vấn pháp lý DN ABC (Sửa)", noi_dung="Cập nhật phạm vi HĐ" | 1. Click Sửa trên HĐ. 2. Đổi tên + thêm nội dung + Lưu. | (1) PUT 200. (2) Tên + nội dung cập nhật. (3) Audit log UPDATE (BR-DATA-05). | Happy 🔴 | PASS |  |
| TC-HDTV-003 | FR-X.3-01 / Processing Xóa step 7 | Xóa HĐ không có VV liên kết — happy | cb_nv_tw_01 login. HĐ "Test Xóa" tồn tại, 0 VV liên kết. | — | 1. Click Xóa trên HĐ. 2. Xác nhận dialog. | (1) Soft delete `is_deleted=1` (BR-DATA-01). (2) HĐ biến mất khỏi danh sách. (3) Audit log DELETE. | Happy 🔴 | PASS |  |
| TC-HDTV-004 | FR-X.3-01 / AC#1 + BR-DATA-07 | Hiển thị danh sách HĐ — phân trang 20/page | cb_nv_tw_01 login. ≥25 HĐ thuộc TW. | — | 1. Truy cập "Quản lý HĐ tư vấn". | (1) Bảng phân trang 20/page (BR-DATA-07). (2) Cột: Mã HĐ, Tên HĐ, Bên A, Bên B, Giá trị (định dạng VND), Thời hạn BĐ, Thời hạn KT, Số VV liên kết (badge), Tiến độ TT (progress bar %). | Happy 🟡 | PASS |  |
| TC-HDTV-005 | FR-X.3-01 / Outputs#5 | Format giá trị HĐ tiền VND có separator | cb_nv_tw_01 login. HĐ giá trị 50_000_000. | — | 1. Xem cột "Giá trị" trên danh sách. | Hiển thị `50.000.000 ₫` hoặc `50,000,000 VND` (theo locale vi-VN). | Happy 🟢 | PASS |  |
| TC-HDTV-010 | FR-X.3-01 / E1 ERR-HDTV-01 | Tên HĐ trống | cb_nv_tw_01 login. | ten=""  | 1. Form thêm mới. 2. Bỏ trống tên. 3. Click [Lưu]. | (1) Inline error / toast: **"Tên hợp đồng là bắt buộc"** (ERR-HDTV-01). (2) Form giữ. (3) KHÔNG có record. | Negative 🔴 | PASS |  |
| TC-HDTV-011 | FR-X.3-01 / E2 ERR-HDTV-02 | Ngày bắt đầu > ngày kết thúc | cb_nv_tw_01 login. | thoi_han_bat_dau=2026-12-31, thoi_han_ket_thuc=2026-06-01 | 1. Form thêm mới. 2. Nhập đủ trường + ngày BD > ngày KT. 3. Lưu. | (1) Error: **"Ngày bắt đầu phải trước ngày kết thúc"** (ERR-HDTV-02). (2) KHÔNG có record. | Negative 🔴 | PASS |  |
| TC-HDTV-012 | FR-X.3-01 / E5 ERR-HDTV-05 | Giá trị HĐ ≤ 0 | cb_nv_tw_01 login. | gia_tri_hop_dong=0 | 1. Form thêm mới. 2. Nhập giá trị=0. 3. Lưu. | (1) Error: **"Giá trị hợp đồng phải lớn hơn 0"** (ERR-HDTV-05). | Negative 🔴 | PASS |  |
| TC-HDTV-013 | FR-X.3-01 / E5 ERR-HDTV-05 | Giá trị HĐ âm | cb_nv_tw_01 login. | gia_tri_hop_dong=-1000000 | 1. Form thêm mới. 2. Nhập giá trị=-1tr. 3. Lưu. | (1) Error: ERR-HDTV-05 hoặc field không cho phép âm (UI block). | Negative 🟡 | PASS |  |
| TC-HDTV-020 | FR-X.3-01 / Inputs#7-8 | Boundary: thoi_han_bat_dau == thoi_han_ket_thuc (cùng ngày) | cb_nv_tw_01 login. | thoi_han_bat_dau=2026-06-01, thoi_han_ket_thuc=2026-06-01 | 1. Tạo HĐ với 2 ngày trùng. | Tạo OK (≥ inclusive theo SRS line 86 `>= thoi_han_bat_dau`). | Edge 🟡 | PASS |  |
| TC-HDTV-022 | FR-X.3-01 / BR-DATA-04 + concurrency | Concurrent CREATE 2 tab cùng ngày → SEQ uniqueness | cb_nv_tw_01 login. Mở 2 tab SCR-X3-01. | Tab1+Tab2: cùng ngày tạo | 1. Tab1 fill form + Lưu (delay BE). 2. Tab2 fill form khác + Lưu trước khi Tab1 response. | (1) Backend race: 2 INSERT thành công. (2) Mã HĐ phải UNIQUE: `HDTV-20260510-001` + `HDTV-20260510-002` (BR-DATA-04 sequence). (3) Không có 2 mã trùng. | Edge 🟡 | PASS |  |
| TC-HDTV-024 | FR-X.3-01 / Inputs#5 (A4 merged) | tvv_id dropdown loại trừ TVV trạng_thái != HOAT_DONG (TAM_DUNG / VO_HIEU_HOA) | cb_nv_tw_01 login. TVV001 HOAT_DONG, TVV002 TAM_DUNG, TVV003 VO_HIEU_HOA. | Mở dropdown TVV | 1. Form thêm HĐ. 2. Mở dropdown chọn TVV. 3. Search "". | Dropdown chỉ list TVV001 (HOAT_DONG). TVV002+003 KHÔNG xuất hiện. (02-thu-tu-module:649 quote `lọc trang_thai=HOAT_DONG`). | Edge 🟡 | PASS |  |
| TC-HDTV-025 | FR-X.3-01 / Inputs#5 + AC#7 (A4 merged) | tvv_id chọn loai_tvv='CG' (Chuyên gia) lưu OK | cb_nv_tw_01 login. CG001 (loai_tvv='CG', HOAT_DONG). | tvv_id=CG001, ben_b="Chuyên gia A" | 1. Form thêm HĐ. 2. Dropdown TVV chọn CG001. 3. Lưu. | (1) HĐ lưu OK với tvv_id trỏ CG001. (2) AC#7 srs-fr-14:180 quote "loai_tvv='CG' lưu hợp đồng với tu_van_vien_id trỏ đến CG đó". | Edge 🟡 | PASS |  |
| TC-HDTV-030 | FR-X.3-01 / Entity trang_thai enum (Codex P0-1 patched) | Sửa `trang_thai` từ DANG_THUC_HIEN → TAM_DUNG (free-edit field) | HĐ "HDTV-test-01" trạng_thái=DANG_THUC_HIEN. | trang_thai=TAM_DUNG | 1. Form Sửa HĐ. 2. Đổi field trang_thai (dropdown/radio) sang TAM_DUNG. 3. [Lưu]. | (1) PUT 200, trang_thai=TAM_DUNG persist. (2) Audit log UPDATE. (3) **OBS**: nếu UI render action-bar nút [Tạm dừng] thay cho dropdown — log observation, KHÔNG fail (TODO UNVERIFIED). | Edge 🟡 | PASS |  |
| TC-HDTV-031 | FR-X.3-01 / Entity trang_thai enum (Codex P0-1 patched) | Sửa `trang_thai` TAM_DUNG → DANG_THUC_HIEN | HĐ "HDTV-test-01" TAM_DUNG. | trang_thai=DANG_THUC_HIEN | 1. Form Sửa. 2. Đổi field. 3. [Lưu]. | (1) Lưu OK. (2) Audit log. | Edge 🟡 | PASS |  |
| TC-HDTV-032 | FR-X.3-01 / Entity trang_thai enum (Codex P0-1 patched) | Sửa `trang_thai` → HOAN_THANH (KHÔNG có guard chính thức) | HĐ HDTV gia_tri=100tr, Σ thanh toán=70tr (chưa đủ). | trang_thai=HOAN_THANH | 1. Form Sửa. 2. Đổi trang_thai sang HOAN_THANH. 3. [Lưu]. | (1) PASS — lưu OK (CRUD thuần, KHÔNG guard Σ ≤ gia_tri trên transition trang_thai per SRS §5; ràng buộc Σ chỉ áp tại TTGD entry-level theo Processing step 4 SRS line 119). (2) Audit log. | Edge 🟡 | PASS |  |
| TC-HDTV-033 | FR-X.3-01 / Entity trang_thai enum (Codex P0-1 patched) | Sửa `trang_thai` → HUY | HĐ HDTV-test-01. | trang_thai=HUY | 1. Form Sửa. 2. Đổi field. 3. [Lưu]. | (1) trang_thai=HUY persist. (2) HĐ vẫn tồn tại (KHÔNG soft-delete). (3) Audit log. | Edge 🟡 | PASS |  |
| TC-HDTV-034 | FR-X.3-01 / Inputs#9 (A6 fill) | ghi_chu boundary text long (≥5000 ký tự?) | cb_nv_tw_01 login. | ghi_chu = 5000 ký tự | 1. Form thêm HĐ. 2. Paste ghi_chu 5000 ký tự. 3. Lưu. | (1) Lưu OK (text long không quy định max trong SRS). (2) Hoặc UI client-side limit (textarea maxlength). **SPEC-CLARIFY-HDTV-14**: SRS không quy định max length cho ghi_chu/noi_dung. | Edge 🟢 | PASS |  |

---

## 05-TC-tim-kiem-hd-tv

> Source TC: `c:\HoaAG\LuatDN5\Ver3.1\output\test-cases\hop-dong-tv\05-TC-tim-kiem-hd-tv.md`
> Source report: `c:\HoaAG\LuatDN5\Ver3.1\output\execution-test\hop-dong-tv\report-05-TC-tim-kiem-hd-tv\Tcs-report\05-TC-tim-kiem-hd-tv-execution-report-2026-05-11.md`

| ID | TraceID (Mã SRS) | Tên Test Case | Pre-conditions (Tiền đề) | Test Data (Dữ liệu) | Các bước thực hiện | Kết quả mong đợi | Type (Happy/Negative/Edge) | Kết quả test (Result) | Chi tiết |
|----|------------------|---------------|--------------------------|---------------------|--------------------|------------------|----------------------------|------------------------|----------|
| TC-HDTK-001 | FR-X.3-02 / AC#1 + Processing step 2 | Tìm theo keyword (tên HĐ) | HĐ "Tư vấn pháp lý ABC" tồn tại. | keyword="ABC" | 1. Filter-bar nhập "ABC". 2. Submit/blur. | (1) GET `/hop-dong-tv/search?keyword=ABC`. (2) Danh sách lọc HĐ matching tên/mã/bên B. (3) Phân trang 20/page (BR-DATA-07). | Happy 🔴 | PASS |  |
| TC-HDTK-011 | FR-X.3-02 / E2 INF-HDTV-TK-01 + AC#3 | Không có kết quả | cb_nv_tw_01 login. | keyword="ZZZ_NOT_EXIST" | 1. Tìm với keyword không tồn tại. | (1) Hiển thị empty state: **"Không tìm thấy hợp đồng phù hợp"** (INF-HDTV-TK-01). | Negative 🟡 | PASS |  |
| TC-HDTK-023 | FR-X.3-02 / keyword full-text 3 fields (A4 merged) | Keyword match TÊN + MÃ + BÊN B (3 fields full-text) | HĐ A tên="Tư vấn ABC", HĐ B mã="HDTV-20260101-099", HĐ C ben_b="Công ty XYZ". | keyword="ABC" / "099" / "XYZ" | 1. Test 3 lần với 3 keyword. | Mỗi keyword trả về HĐ matching theo field tương ứng (full-text trên 3 fields, business §6 quote). | Edge 🟡 | PASS |  |
| TC-HDTK-024 | FR-X.3-02 / SQL injection (A4 merged) | Keyword chứa SQL injection payload — sanitize | cb_nv_tw_01 login. | keyword="' OR 1=1 --" | 1. Filter keyword với payload injection. | (1) Sanitize: query chạy như literal text. (2) KHÔNG return all rows (SQL injection block). (3) BR-EC-13 max 200 ký tự nếu áp dụng. | Edge 🔴 | PASS |  |
| TC-HDTK-026 | FR-X.3-02 / empty keyword (A4 merged) | Keyword rỗng → trả tất cả (scope đơn vị) | cb_nv_tw_01 login. ≥30 HĐ TW. | keyword="" | 1. Filter keyword rỗng. 2. Submit. | Trả tất cả HĐ TW phân trang 20/page (BR-DATA-07). KHÔNG validate "keyword bắt buộc". | Edge 🟢 | PASS |  |

---

## 06-TC-permission-matrix

> Source TC: `c:\HoaAG\LuatDN5\Ver3.1\output\test-cases\hop-dong-tv\06-TC-permission-matrix.md`
> Source report: `c:\HoaAG\LuatDN5\Ver3.1\output\execution-test\hop-dong-tv\report-06-TC-permission-matrix\Tcs-report\06-TC-permission-matrix-execution-report-2026-05-11.md`

| ID | TraceID (Mã SRS) | Tên Test Case | Pre-conditions (Tiền đề) | Test Data (Dữ liệu) | Các bước thực hiện | Kết quả mong đợi | Type (Happy/Negative/Edge) | Kết quả test (Result) | Chi tiết |
|----|------------------|---------------|--------------------------|---------------------|--------------------|------------------|----------------------------|------------------------|----------|
| TC-PERM-001 | Permission / CB_NV_TW | CB_NV_TW thấy + CRUD HĐ scope toàn TW | cb_nv_tw_01 login. | — | 1. Truy cập HĐ TV. 2. Thấy nút [+ Thêm], [Sửa], [Xóa], [Xuất Excel]. 3. Tạo HĐ mới. | (1) Thấy đầy đủ action button. (2) Tạo HĐ thành công (don_vi_id=TW). | Happy 🔴 | PASS |  |

---

## Skipped

Các file dưới đây không có TC Result ∈ {PASS, PASS-DEVIATE, PASS-RESOLVED} — toàn bộ TC ở trạng thái BLOCKED/FAIL/OBS, đã omit khỏi báo cáo này:

- **02-TC-moc-tien-do** (9 TC, 0 PASS) — toàn bộ BLOCKED do BUG-ENV-001 token revoke khi click [+ Thêm mốc] trong Edit modal.
- **03-TC-thanh-toan-giai-doan** (11 TC, 0 PASS) — toàn bộ BLOCKED do token revoke + phụ thuộc TC-001 (chưa tạo được GĐ).
- **04-TC-lien-ket-vu-viec** (11 TC, 0 PASS) — toàn bộ BLOCKED do BUG-LVV-001 Critical (Edit modal thiếu accordion "Vụ việc liên kết").

> Source reports cho các file Skipped:
> - `c:\HoaAG\LuatDN5\Ver3.1\output\execution-test\hop-dong-tv\report-02-TC-moc-tien-do\Tcs-report\02-TC-moc-tien-do-execution-report-2026-05-11.md`
> - `c:\HoaAG\LuatDN5\Ver3.1\output\execution-test\hop-dong-tv\report-03-TC-thanh-toan-giai-doan\Tcs-report\03-TC-thanh-toan-giai-doan-execution-report-2026-05-11.md`
> - `c:\HoaAG\LuatDN5\Ver3.1\output\execution-test\hop-dong-tv\report-04-TC-lien-ket-vu-viec\Tcs-report\04-TC-lien-ket-vu-viec-execution-report-2026-05-11.md`

*Generated 2026-05-11 — filtered from result-hop-dong-tv-all.md*
