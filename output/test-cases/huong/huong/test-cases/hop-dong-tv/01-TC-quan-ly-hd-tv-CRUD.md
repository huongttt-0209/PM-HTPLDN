# Test Cases — FR-X.3-01 (UC159): Quản lý HĐ Tư vấn — CRUD Thông tin chung + Xuất Excel

> **SRS Ref**: FR-X.3-01, SCR-X3-01, Entity HOP_DONG_TU_VAN
> **Ngày tạo**: 2026-05-10
> **Đặc thù**: CRUD thuần, KHÔNG phê duyệt. Mã HĐ auto `HDTV-YYYYMMDD-SEQ`. Bên A auto từ đơn vị user. Xóa chặn nếu còn VV liên kết. Xuất Excel theo filter.

---

## Quy ước

- **Priority**: 🔴 P0 (critical) · 🟡 P1 (high) · 🟢 P2 (medium)
- **TraceID**: `FR-X.3-01 / {section}` — truy vết SRS
- **Pre-conditions mặc định**: User đã đăng nhập, có quyền "Quản lý HĐ tư vấn"

---

## Trường input FR-X.3-01 (Thông tin chung — Accordion 1)

| # | Field | Bắt buộc | Kiểu | Ràng buộc |
|---|-------|----------|------|-----------|
| 1 | ma_hop_dong | Y (auto) | text | `HDTV-YYYYMMDD-SEQ` (BR-DATA-04) |
| 2 | ten_hop_dong | Y | text | Không trống (E1 ERR-HDTV-01) |
| 3 | ben_a | Y (auto) | text | Auto từ `don_vi_id` user login |
| 4 | ben_b | Y | text | Nhập tay |
| 5 | tvv_id | N | identifier | FK → TU_VAN_VIEN; lọc `loai_tvv ∈ {TVV,CG}`, `trang_thai=HOAT_DONG` |
| 6 | gia_tri_hop_dong | Y | money | > 0 (E5 ERR-HDTV-05) |
| 7 | thoi_han_bat_dau | Y | date | — |
| 8 | thoi_han_ket_thuc | Y | date | ≥ thoi_han_bat_dau (E2 ERR-HDTV-02) |
| 9 | noi_dung | N | text long | — |
| 10 | ghi_chu | N | text long | — |
| 11 | file_dinh_kem[] | N | file[] | Upload nhiều file (định dạng SPEC-CLARIFY-HDTV-05) |

---

## A. CRUD HĐ — HAPPY

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|---------|---------------|----------------|-----------|-------------------|------------------|------|
| TC-HDTV-001 | FR-X.3-01 / Processing step 1-8 | Tạo HĐ thành công — happy path | cb_nv_tw_01 login. TVV "Nguyễn Văn A" trạng thái HOAT_DONG. | ten="Tư vấn pháp lý DN ABC", ben_b="Nguyễn Văn A", tvv_id=TVV001, gia_tri=50_000_000, thoi_han_bat_dau=2026-06-01, thoi_han_ket_thuc=2026-12-31 | 1. Vào "Quản lý HĐ tư vấn" → click [+ Thêm hợp đồng]. 2. Nhập 6 trường bắt buộc + chọn TVV. 3. Click [Lưu]. | (1) POST `/hop-dong-tv` 201. (2) ma_hop_dong tự sinh `HDTV-20260510-001` (BR-DATA-04). (3) ben_a = "Bộ Tư pháp" (auto từ TW). (4) trạng_thái=`DANG_THUC_HIEN`. (5) Audit log INSERT (BR-DATA-05). | Happy 🔴 |
| TC-HDTV-002 | FR-X.3-01 / Processing Cập nhật | Sửa HĐ thành công | cb_nv_tw_01 login. HĐ HDTV-20260510-001 (DANG_THUC_HIEN). | ten="Tư vấn pháp lý DN ABC (Sửa)", noi_dung="Cập nhật phạm vi HĐ" | 1. Click Sửa trên HĐ. 2. Đổi tên + thêm nội dung + Lưu. | (1) PUT 200. (2) Tên + nội dung cập nhật. (3) Audit log UPDATE (BR-DATA-05). | Happy 🔴 |
| TC-HDTV-003 | FR-X.3-01 / Processing Xóa step 7 | Xóa HĐ không có VV liên kết — happy | cb_nv_tw_01 login. HĐ "Test Xóa" tồn tại, 0 VV liên kết. | — | 1. Click Xóa trên HĐ. 2. Xác nhận dialog. | (1) Soft delete `is_deleted=1` (BR-DATA-01). (2) HĐ biến mất khỏi danh sách. (3) Audit log DELETE. | Happy 🔴 |
| TC-HDTV-004 | FR-X.3-01 / AC#1 + BR-DATA-07 | Hiển thị danh sách HĐ — phân trang 20/page | cb_nv_tw_01 login. ≥25 HĐ thuộc TW. | — | 1. Truy cập "Quản lý HĐ tư vấn". | (1) Bảng phân trang 20/page (BR-DATA-07). (2) Cột: Mã HĐ, Tên HĐ, Bên A, Bên B, Giá trị (định dạng VND), Thời hạn BĐ, Thời hạn KT, Số VV liên kết (badge), Tiến độ TT (progress bar %). | Happy 🟡 |
| TC-HDTV-005 | FR-X.3-01 / Outputs#5 | Format giá trị HĐ tiền VND có separator | cb_nv_tw_01 login. HĐ giá trị 50_000_000. | — | 1. Xem cột "Giá trị" trên danh sách. | Hiển thị `50.000.000 ₫` hoặc `50,000,000 VND` (theo locale vi-VN). | Happy 🟢 |
| TC-HDTV-006 | FR-X.3-01 / Excel Processing step 1-5 + GAP-X.3-02 | Xuất Excel danh sách HĐ | cb_nv_tw_01 login. ≥10 HĐ. | Filter rỗng (toàn TW) | 1. Click [Xuất Excel] trên toolbar. | (1) GET file `.xlsx` ≤10.000 dòng. (2) File chứa cột: Mã HĐ, Tên, Bên A, Bên B, Giá trị, Thời hạn BĐ/KT, Số VV, Tiến độ TT. (3) Audit EXPORT (BR-DATA-05). **SPEC-CLARIFY-HDTV-03**: template column chính thức cần CĐT confirm. | Happy 🟡 |

---

## B. CRUD HĐ — NEGATIVE

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|---------|---------------|----------------|-----------|-------------------|------------------|------|
| TC-HDTV-010 | FR-X.3-01 / E1 ERR-HDTV-01 | Tên HĐ trống | cb_nv_tw_01 login. | ten=""  | 1. Form thêm mới. 2. Bỏ trống tên. 3. Click [Lưu]. | (1) Inline error / toast: **"Tên hợp đồng là bắt buộc"** (ERR-HDTV-01). (2) Form giữ. (3) KHÔNG có record. | Negative 🔴 |
| TC-HDTV-011 | FR-X.3-01 / E2 ERR-HDTV-02 | Ngày bắt đầu > ngày kết thúc | cb_nv_tw_01 login. | thoi_han_bat_dau=2026-12-31, thoi_han_ket_thuc=2026-06-01 | 1. Form thêm mới. 2. Nhập đủ trường + ngày BD > ngày KT. 3. Lưu. | (1) Error: **"Ngày bắt đầu phải trước ngày kết thúc"** (ERR-HDTV-02). (2) KHÔNG có record. | Negative 🔴 |
| TC-HDTV-012 | FR-X.3-01 / E5 ERR-HDTV-05 | Giá trị HĐ ≤ 0 | cb_nv_tw_01 login. | gia_tri_hop_dong=0 | 1. Form thêm mới. 2. Nhập giá trị=0. 3. Lưu. | (1) Error: **"Giá trị hợp đồng phải lớn hơn 0"** (ERR-HDTV-05). | Negative 🔴 |
| TC-HDTV-013 | FR-X.3-01 / E5 ERR-HDTV-05 | Giá trị HĐ âm | cb_nv_tw_01 login. | gia_tri_hop_dong=-1000000 | 1. Form thêm mới. 2. Nhập giá trị=-1tr. 3. Lưu. | (1) Error: ERR-HDTV-05 hoặc field không cho phép âm (UI block). | Negative 🟡 |
| TC-HDTV-014 | FR-X.3-01 / E4 ERR-HDTV-04 | Xóa HĐ đang có VV liên kết | cb_nv_tw_01 login. HĐ "HDTV-001" liên kết 2 VV (V001, V002). | — | 1. Click Xóa HĐ. 2. Xác nhận. | (1) Reject: **"Không thể xóa hợp đồng đang có vụ việc liên kết"** (ERR-HDTV-04). (2) HĐ vẫn tồn tại. (3) KHÔNG audit DELETE. | Negative 🔴 |

---

## C. CRUD HĐ — EDGE

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|---------|---------------|----------------|-----------|-------------------|------------------|------|
| TC-HDTV-020 | FR-X.3-01 / Inputs#7-8 | Boundary: thoi_han_bat_dau == thoi_han_ket_thuc (cùng ngày) | cb_nv_tw_01 login. | thoi_han_bat_dau=2026-06-01, thoi_han_ket_thuc=2026-06-01 | 1. Tạo HĐ với 2 ngày trùng. | Tạo OK (≥ inclusive theo SRS line 86 `>= thoi_han_bat_dau`). | Edge 🟡 |
| TC-HDTV-021 | FR-X.3-01 / SCR-X3-01 row#4 | Cột "Thời hạn KT" highlight đỏ nếu ≤30 ngày | cb_nv_tw_01 login. HĐ A KT=NOW+15d, HĐ B KT=NOW+45d. | — | 1. Xem danh sách HĐ. | (1) HĐ A row "Thời hạn KT" hiển thị màu đỏ. (2) HĐ B màu mặc định. **SPEC-CLARIFY-HDTV-08**: countdown realtime hay snapshot daily? | Edge 🟡 |
| TC-HDTV-022 | FR-X.3-01 / BR-DATA-04 + concurrency | Concurrent CREATE 2 tab cùng ngày → SEQ uniqueness | cb_nv_tw_01 login. Mở 2 tab SCR-X3-01. | Tab1+Tab2: cùng ngày tạo | 1. Tab1 fill form + Lưu (delay BE). 2. Tab2 fill form khác + Lưu trước khi Tab1 response. | (1) Backend race: 2 INSERT thành công. (2) Mã HĐ phải UNIQUE: `HDTV-20260510-001` + `HDTV-20260510-002` (BR-DATA-04 sequence). (3) Không có 2 mã trùng. | Edge 🟡 |
| TC-HDTV-023 | FR-X.3-01 / Inputs#3 | ben_a auto theo cấp đơn vị user (TW vs ĐP) | cb_nv_dp_01 (Sở TP AG) login. | — | 1. Tạo HĐ mới. 2. Xem field ben_a. | ben_a hiển thị "Sở Tư pháp An Giang" (auto từ don_vi_id), không phải "Bộ Tư pháp". | Edge 🟡 |
| TC-HDTV-024 | FR-X.3-01 / Inputs#5 (A4 merged) | tvv_id dropdown loại trừ TVV trạng_thái != HOAT_DONG (TAM_DUNG / VO_HIEU_HOA) | cb_nv_tw_01 login. TVV001 HOAT_DONG, TVV002 TAM_DUNG, TVV003 VO_HIEU_HOA. | Mở dropdown TVV | 1. Form thêm HĐ. 2. Mở dropdown chọn TVV. 3. Search "". | Dropdown chỉ list TVV001 (HOAT_DONG). TVV002+003 KHÔNG xuất hiện. (02-thu-tu-module:649 quote `lọc trang_thai=HOAT_DONG`). | Edge 🟡 |
| TC-HDTV-025 | FR-X.3-01 / Inputs#5 + AC#7 (A4 merged) | tvv_id chọn loai_tvv='CG' (Chuyên gia) lưu OK | cb_nv_tw_01 login. CG001 (loai_tvv='CG', HOAT_DONG). | tvv_id=CG001, ben_b="Chuyên gia A" | 1. Form thêm HĐ. 2. Dropdown TVV chọn CG001. 3. Lưu. | (1) HĐ lưu OK với tvv_id trỏ CG001. (2) AC#7 srs-fr-14:180 quote "loai_tvv='CG' lưu hợp đồng với tu_van_vien_id trỏ đến CG đó". | Edge 🟡 |
| TC-HDTV-026 | FR-X.3-01 / Inputs#11 / SPEC-CLARIFY-HDTV-05 (A4 merged) | file_dinh_kem upload >dung lượng / sai định dạng | cb_nv_tw_01 login. | file=demo.exe (sai format), file2=20MB+ (over size?) | 1. Form thêm HĐ. 2. Upload file .exe. 3. Upload file 50MB. | (1) BE behavior **SRS Gap**: SRS không quy định format/size cho file_dinh_kem HĐ. Kỳ vọng: reject .exe (security) + reject >20MB (default theo các module khác). Mark **SPEC-CLARIFY-HDTV-05**. | Edge 🟡 |
| TC-HDTV-027 | FR-X.3-01 / BR-DATA-04 (A4 merged) | Mã HĐ format chính xác `HDTV-YYYYMMDD-NNN` | cb_nv_tw_01 login. | — | 1. Tạo HĐ mới ngày 2026-05-10. | (1) ma_hop_dong = `HDTV-20260510-001` (đúng format BR-DATA-04, prefix HDTV, ngày YYYYMMDD, SEQ 3 digit). | Edge 🟢 |
| TC-HDTV-028 | FR-X.3-01 / Excel + BR-AUTH-08 (A4 merged) | Xuất Excel chỉ scope đơn vị user | cb_nv_dp_01 (AG) login. AG có 5 HĐ. TW có 100 HĐ. | — | 1. Click [Xuất Excel]. | File .xlsx chỉ chứa 5 HĐ AG. KHÔNG có HĐ TW (BR-AUTH-08). | Edge 🟡 |
| TC-HDTV-029 | FR-X.3-01 / Excel Processing step 2 + AC#6 (Codex P1-1) | Xuất Excel với filter non-empty (TVV + khoảng ngày) | cb_nv_tw_01 login. ≥30 HĐ TW. TVV001 có 5 HĐ. Range 2026-06..09 có 8 HĐ overlap TVV001=3 HĐ. | tvv_id=TVV001, tu_ngay=2026-06-01, den_ngay=2026-09-30 | 1. Filter form: chọn TVV001 + khoảng ngày. 2. Submit (list refresh = 3 row). 3. Click [Xuất Excel]. | File .xlsx chỉ chứa **3 HĐ** match filter (TVV001 + range). KHÔNG có toàn bộ 30 HĐ TW (Processing step 2 SRS line 130 quote "Áp dụng filter hiện tại"). | Edge 🔴 |

---

## D. TRẠNG THÁI HĐ (status field, KHÔNG phải SM — per SRS §5 line 450-452)

> **SRS §5 nguyên văn:** "Nhóm X.3 không có state machine. HĐ TV chỉ CRUD thuần. Trạng thái HĐ chỉ là status field đơn giản, không theo vòng đời phê duyệt." → 4 TC dưới test field `trang_thai` như enum thông thường (free-edit trong form Sửa). Action-bar [Tạm dừng]/[Đóng HĐ]/[Hủy] là TODO UNVERIFIED của 02-thu-tu-module → KHÔNG bắt buộc test, mark OBS.

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|---------|---------------|----------------|-----------|-------------------|------------------|------|
| TC-HDTV-030 | FR-X.3-01 / Entity trang_thai enum (Codex P0-1 patched) | Sửa `trang_thai` từ DANG_THUC_HIEN → TAM_DUNG (free-edit field) | HĐ "HDTV-test-01" trạng_thái=DANG_THUC_HIEN. | trang_thai=TAM_DUNG | 1. Form Sửa HĐ. 2. Đổi field trang_thai (dropdown/radio) sang TAM_DUNG. 3. [Lưu]. | (1) PUT 200, trang_thai=TAM_DUNG persist. (2) Audit log UPDATE. (3) **OBS**: nếu UI render action-bar nút [Tạm dừng] thay cho dropdown — log observation, KHÔNG fail (TODO UNVERIFIED). | Edge 🟡 |
| TC-HDTV-031 | FR-X.3-01 / Entity trang_thai enum (Codex P0-1 patched) | Sửa `trang_thai` TAM_DUNG → DANG_THUC_HIEN | HĐ "HDTV-test-01" TAM_DUNG. | trang_thai=DANG_THUC_HIEN | 1. Form Sửa. 2. Đổi field. 3. [Lưu]. | (1) Lưu OK. (2) Audit log. | Edge 🟡 |
| TC-HDTV-032 | FR-X.3-01 / Entity trang_thai enum (Codex P0-1 patched) | Sửa `trang_thai` → HOAN_THANH (KHÔNG có guard chính thức) | HĐ HDTV gia_tri=100tr, Σ thanh toán=70tr (chưa đủ). | trang_thai=HOAN_THANH | 1. Form Sửa. 2. Đổi trang_thai sang HOAN_THANH. 3. [Lưu]. | (1) PASS — lưu OK (CRUD thuần, KHÔNG guard Σ ≤ gia_tri trên transition trang_thai per SRS §5; ràng buộc Σ chỉ áp tại TTGD entry-level theo Processing step 4 SRS line 119). (2) Audit log. | Edge 🟡 |
| TC-HDTV-033 | FR-X.3-01 / Entity trang_thai enum (Codex P0-1 patched) | Sửa `trang_thai` → HUY | HĐ HDTV-test-01. | trang_thai=HUY | 1. Form Sửa. 2. Đổi field. 3. [Lưu]. | (1) trang_thai=HUY persist. (2) HĐ vẫn tồn tại (KHÔNG soft-delete). (3) Audit log. | Edge 🟡 |
| TC-HDTV-034 | FR-X.3-01 / Inputs#9 (A6 fill) | ghi_chu boundary text long (≥5000 ký tự?) | cb_nv_tw_01 login. | ghi_chu = 5000 ký tự | 1. Form thêm HĐ. 2. Paste ghi_chu 5000 ký tự. 3. Lưu. | (1) Lưu OK (text long không quy định max trong SRS). (2) Hoặc UI client-side limit (textarea maxlength). **SPEC-CLARIFY-HDTV-14**: SRS không quy định max length cho ghi_chu/noi_dung. | Edge 🟢 |

---

## Tổng kết file 01-TC

- **Tổng số TC: 26** (6 Happy + 5 Negative + 10 Edge + 5 status field + 1 Codex Excel filter)
- **Critical TC (🔴)**: TC-HDTV-001, 002, 003, 010, 011, 012, 014, 029
- **A4 merged 2026-05-10**: TC-HDTV-024..028
- **A6 fill 2026-05-10**: TC-HDTV-030..034 (4 status field test + 1 ghi_chu entity)
- **Codex 2026-05-10 patches**: TC-HDTV-024/025 sửa `DANG_HOAT_DONG`→`HOAT_DONG` (P0-2). TC-HDTV-030..033 đổi từ "SM transition" → "status field free-edit" (P0-1, SRS §5 contradicts SM). +TC-HDTV-029 Excel filter non-empty (P1-1).
- **SPEC-CLARIFY refs**: HDTV-03 (Excel template), HDTV-05 (file format), HDTV-08 (countdown 30d), HDTV-14 (ghi_chu max length)

*Generated 2026-05-10 — Phase A step A3*
