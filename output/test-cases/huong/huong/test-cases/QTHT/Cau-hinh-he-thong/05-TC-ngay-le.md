# Test Cases — Quản lý Ngày lễ (FR-VIII-29)

> **SRS Ref**: FR-VIII-29 (srs-fr-10:1376-1434), Entity `NGAY_LE` (owned), tích hợp BR-CALC-03 (deadline tính ngày LV trừ ngày lễ)
> **Ngày tạo**: 2026-05-08 (BMAD A3, A4 inline merge)
> **Tài khoản chính**: `qtht_01`
> **Màn hình:** SCR-VIII-06 hoặc màn hình riêng (danh mục con — line 1382). Verify URL thực tế ở Phase B.

> **Pre-condition chung:** `qtht_01` đăng nhập, vào màn hình Quản lý Ngày lễ (URL TBD). Seed NGAY_LE 5 record VN gốc (Tết DL, Giỗ Tổ, 30/4-1/5, Quốc khánh, Tết AL).

---

## A. HAPPY PATH — CRUD

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước | Kết quả mong đợi | Type | Priority |
|----|---------|---------------|----------------|-----------|----------|------------------|------|----------|
| TC-CH-NL-001 | FR-VIII-29 AC1 | QTHT thêm ngày lễ mới — happy path | `qtht_01`. | ten="Lễ test", bat_dau=2026-08-15, ket_thuc=2026-08-15, mo_ta="test", lap_lai_hang_nam=true | 1. Click [+ Thêm ngày lễ]. 2. Fill modal. 3. Save. | **STATE**: BE POST `/api/ngay-le`. AUDIT_LOG action=CREATE (BR-DATA-05). **UI**: Toast success. Bảng refresh có row mới. **PERSIST**: GET reload thấy. | Happy | P0 |
| TC-CH-NL-002 | FR-VIII-29 input #5 default | Default `lap_lai_hang_nam = true` | `qtht_01`. | — | 1. Modal create. 2. Quan sát toggle. | **UI**: Toggle "Lặp lại hàng năm" mặc định ON (input #5 default true, line 1399). | Happy | P1 |
| TC-CH-NL-003 | FR-VIII-29 step 4 | Sửa ngày lễ — đổi tên | `qtht_01`. Có 1 ngày lễ "Lễ test". | ten="Lễ test sửa" | 1. Click ✏️ Sửa. 2. Modal load giá trị cũ. 3. Sửa tên. 4. Save. | **STATE**: BE PATCH. AUDIT_LOG UPDATE old/new. **UI**: Toast success. Bảng refresh. | Happy | P0 |
| TC-CH-NL-004 | FR-VIII-29 step 4 + BR-DATA-01 | Xóa ngày lễ — soft delete | `qtht_01`. | — | 1. Click 🗑 Xóa. 2. Confirm. | **STATE**: BE PATCH `is_deleted=1`. AUDIT_LOG DELETE. **UI**: Row biến mất khỏi bảng. **PERSIST**: GET reload không hiện. | Happy | P0 |
| TC-CH-NL-005 | FR-VIII-29 input #3 | Khoảng nhiều ngày — bat_dau != ket_thuc | `qtht_01`. | bat_dau=2026-04-30, ket_thuc=2026-05-01 | 1. Modal. 2. Save khoảng 2 ngày. | **STATE**: BE accept (input #3 ket_thuc >= bat_dau, line 1397). **UI**: Toast success. Bảng hiển thị range. | Happy | P0 |
| TC-CH-NL-006 | A6 fill A5-GAP-CH-06 + input #4 | Field mo_ta happy — lưu + hiển thị | `qtht_01`. | mo_ta="Lễ Quốc khánh — nghỉ chính thức theo Bộ luật LĐ 2019" | 1. Modal. 2. Nhập mo_ta. 3. Save. 4. Click ✏️ Sửa. 5. Quan sát mo_ta load lại. | **STATE**: BE lưu mo_ta. **UI**: Modal sửa load đúng giá trị mo_ta. **PERSIST**: GET reload thấy. | Happy | P2 |

---

## B. NEGATIVE — VALIDATION

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước | Kết quả mong đợi | Type | Priority |
|----|---------|---------------|----------------|-----------|----------|------------------|------|----------|
| TC-CH-NL-010 | ERR-NL-02 (E2) | ket_thuc < bat_dau | `qtht_01`. | bat_dau=2026-05-01, ket_thuc=2026-04-30 | 1. Save. | **STATE**: BE reject. **UI**: Toast nguyên văn "Ngày kết thúc phải >= ngày bắt đầu" (srs-fr-10:1424). | Negative | P0 |
| TC-CH-NL-011 | ERR-NL-02 boundary | ket_thuc == bat_dau hợp lệ | `qtht_01`. | bat_dau=ket_thuc=2026-05-08 | 1. Save. | BE accept (>= comparator). | Edge | P1 |
| TC-CH-NL-012 | ERR-NL-03 (E3) | Trùng ngày lễ — overlap | `qtht_01`. NGAY_LE có "Tết DL" 2026-01-01..03. | bat_dau=2026-01-02, ket_thuc=2026-01-04 (overlap với Tết DL) | 1. Save. | **STATE**: BE check overlap (step 3, line 1407). **UI**: WARNING "Khoảng thời gian trùng với ngày lễ 'Tết DL'" (srs-fr-10:1425). | Negative | P0 |
| TC-CH-NL-013 | input #1 required | ten_ngay_le trống | `qtht_01`. | ten_ngay_le="" | 1. Save. | **UI**: Inline error "Tên ngày lễ là bắt buộc". | Negative | P0 |
| TC-CH-NL-014 | input #2 required | ngay_bat_dau trống | `qtht_01`. | bat_dau=null | 1. Save. | **UI**: Inline error required. | Negative | P0 |

---

## C. IMPORT EXCEL (FR-VIII-29 step 6 + AC2)

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước | Kết quả mong đợi | Type | Priority |
|----|---------|---------------|----------------|-----------|----------|------------------|------|----------|
| TC-CH-NL-020 | step 6 + AC2 | Import file Excel — happy path | `qtht_01`. File `ngay-le-2027.xlsx` chứa 12 ngày lễ năm 2027 đúng format. | file 12 row | 1. Click [Import Excel]. 2. Chọn file. 3. Submit. | **STATE**: BE parse file, INSERT batch. AUDIT_LOG mỗi bản ghi. **UI**: Toast success "Đã import 12 ngày lễ". Bảng refresh có 12 row mới. **PERSIST**: — | Happy | P0 |
| TC-CH-NL-021 | step 6 (A4 merged) | Import file format sai (xls thay vì xlsx) | `qtht_01`. File `.xls`. | — | 1. Upload .xls. | **STATE**: BE/FE reject format. **UI**: Toast ERROR "Định dạng file không hợp lệ. Vui lòng dùng .xlsx" hoặc tương đương. | Negative | P1 |
| TC-CH-NL-022 | A4 boundary (A4 merged) | Import file 0 row (chỉ header) | `qtht_01`. | empty file | 1. Upload. | **UI**: Toast WARNING "File không có dữ liệu" hoặc tương đương. | Negative | P2 |
| TC-CH-NL-023 | CAUHINH-05 RESOLVED (theo business — BR-DATA-06 = 10K policy decision) | Import boundary 10.000 ngày lễ — VALID | `qtht_01`. File 10K row đúng format. | — | 1. Upload. | **STATE**: BE accept đầy đủ 10K. **Note**: codex review 2026-05-08 — "applying BR-DATA-06 export limit to holiday import is not text-backed in SRS"; đây là **policy inference** (extension default) chứ không phải spec literal. Phase B verify behavior thực tế; Bug chỉ log nếu BA confirm 10K áp dụng cho import. **UI**: Toast success "Đã import 10.000 ngày lễ" (nếu áp 10K). | Edge | P1 |
| TC-CH-NL-024 | A4 invalid row (A4 merged) | Import file có row sai (date format invalid) | `qtht_01`. File 10 row, row 5 date format sai "2026-13-45". | — | 1. Upload. | **STATE Phase B verify behavior cụ thể (1 trong 2):** (a) Partial-import: BE INSERT 9 row hợp lệ + Toast WARNING "Đã import 9/10. Lỗi row 5: định dạng ngày sai"; (b) All-or-nothing: BE reject toàn file + Toast ERROR "Có 1 row sai format. Vui lòng sửa file rồi upload lại". Cả 2 đều acceptable; log SPEC-CLARIFY nếu BA muốn behavior cụ thể. | Edge | P1 |
| TC-CH-NL-025 | BR-DATA-06 over-limit (paired CAUHINH-05 policy) | **Import over-limit 10.001 ngày lễ — TRUNCATE/REJECT** | `qtht_01`. File 10.001 row. | — | 1. Upload. | **STATE Phase B**: nếu BA confirm áp BR-DATA-06 10K cho import → 2 behavior hợp lệ: (a) truncate xuống 10K + WARNING; (b) reject toàn bộ + ERROR "File vượt quá 10.000 dòng". **NẾU BA không áp limit** → TC này N/A, BE accept full file. | Edge | P2 |

---

## D. CALENDAR VIEW (output #2 — SPEC-CLARIFY-CAUHINH-06)

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước | Kết quả mong đợi | Type | Priority |
|----|---------|---------------|----------------|-----------|----------|------------------|------|----------|
| TC-CH-NL-030 | output #2 + AC3 | Toggle calendar view | `qtht_01`. ≥ 5 ngày lễ năm 2026. | — | 1. Toggle "Calendar view" (nếu có). | **UI**: Hiển thị calendar 12 tháng năm hiện tại với ngày lễ highlight. (SPEC-CLARIFY-CAUHINH-06 — view này tùy chọn, có thể không impl Phase A.) | Happy | P2 |

---

## E. INTEGRATION — SLA / BR-CALC-03

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước | Kết quả mong đợi | Type | Priority |
|----|---------|---------------|----------------|-----------|----------|------------------|------|----------|
| TC-CH-NL-040 | BR-SLA-04 + BR-CALC-03 + AC1 (A4 merged) | **Verify SLA tính trừ ngày lễ — tích hợp e2e** | `qtht_01`. Đã thêm ngày lễ "Test 2026-08-15" + 1 VV mới tạo deadline 10 ngày LV. | bat_dau=ket_thuc=2026-08-15 (1 ngày lễ giữa khoảng deadline) | 1. Thêm ngày lễ. 2. Tạo VV mới hôm nay (giả định 2026-08-08). 3. Mở VV detail → quan sát deadline. | **STATE**: BR-CALC-03 tính `today + 10 ngày LV` trừ 2026-08-15. Deadline = today + 11 ngày calendar (skip lễ). **UI**: Field deadline VV = today + 11 ngày calendar (dài hơn 1 ngày so với deadline không có lễ). **PERSIST**: BR-CALC-03 áp đúng — đây là PURPOSE chính của module Ngày lễ. | Edge | P0 |
| TC-CH-NL-041 | A4 cascading (A4 merged) | Xóa ngày lễ — VV deadline đã set có cập nhật không? | `qtht_01`. VV TC-040 đã có deadline tính trừ ngày lễ. | Xóa ngày lễ "Test 2026-08-15" | 1. Xóa ngày lễ. 2. Mở VV. | **STATE**: Tùy implementation: (a) snapshot — VV giữ deadline cũ; (b) re-calc — VV nhảy về deadline trừ lễ cũ. **UI**: Verify behavior thực tế — log SPEC-CLARIFY nếu mâu thuẫn. **PERSIST**: — | Edge | P1 |

---

## F. PERMISSION

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước | Kết quả mong đợi | Type | Priority |
|----|---------|---------------|----------------|-----------|----------|------------------|------|----------|
| TC-CH-NL-050 | ERR-NL-01 (E1) + BR-AUTH-01 | CB_NV_TW không quản lý ngày lễ | `cb_nv_tw_01`. | — | 1. URL direct màn hình ngày lễ. | **STATE**: BE 403. **UI**: Toast "Bạn không có quyền quản lý ngày lễ" (srs-fr-10:1423) hoặc redirect. | Negative | P0 |
| TC-CH-NL-051 | BR-AUTH-01 Tier 2 | DN không truy cập | `dn_01`. | — | 1. URL direct. | 403. | Negative | P0 |

---

## Tổng số TC: 22 (6 Happy + 5 Negative + 6 Import + 1 Calendar + 2 Integration + 2 Permission) — A3 base 14 + A4 merged 6 + A6 fill 1 + CAUHINH-05 +1 (codex 2026-05-08: count fix)
**Priority**: P0=11 / P1=7 / P2=4

**Coverage:**
- BR: BR-AUTH-01 (TC-050-051), BR-DATA-01 (TC-004 soft delete), BR-DATA-03 (TC-001 common fields), BR-DATA-05 (mọi CUD), BR-CALC-03 + BR-SLA-04 (TC-040 — tích hợp e2e)
- AC SRS: AC1 ✅ (TC-001 + TC-040 e2e), AC2 ✅ (TC-020 import), AC3 ✅ (TC-030 calendar)
- Error codes: ERR-NL-01 (TC-050), ERR-NL-02 (TC-010, 011), ERR-NL-03 (TC-012)
- A4 merged 2026-05-08: TC-021 (file format), TC-022 (empty file), TC-023 (10K boundary), TC-024 (invalid row), TC-040 (e2e SLA integration), TC-041 (xóa cascading)
- SPEC-CLARIFY: CAUHINH-05 (Import limit — TC-023), CAUHINH-06 (Calendar view optional — TC-030)
