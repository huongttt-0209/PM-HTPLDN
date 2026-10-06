# Test Cases — UC96: Tìm kiếm Biểu mẫu (FR-VII-05)

> **SRS Ref**: FR-VII-05 (srs-fr-09:390-444), SCR-VII-02 (filter-bar), Entity BIEU_MAU
> **Ngày tạo**: 2026-05-06 (BMAD A3)
> **Tài khoản chính**: `cb_nv_tw_01`

---

## A. SEARCH BY KEYWORD + FILTER COMBO

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước | Kết quả mong đợi | Type | Priority |
|----|---------|--------------|----------------|-----------|----------|------------------|------|----------|
| TC-BM-501 | FR-VII-05 AC1 | Tìm theo keyword khớp tên BM | `cb_nv_tw_01`. ≥3 BM thuộc TW: "Mẫu HĐ LĐ", "Mẫu HĐ DV", "Đơn xin việc". | keyword="Mẫu HĐ" | 1. Vào SCR-VII-02. 2. Nhập keyword. 3. [Tìm kiếm]. | **STATE**: Backend `WHERE ten_bieu_mau LIKE '%Mẫu HĐ%' OR mo_ta LIKE '%Mẫu HĐ%'` AND `is_deleted=0` AND `don_vi_id=TW.id` (BR-AUTH-08, srs-fr-09:411-413). **UI**: Bảng 2 BM match. Cột Thư mục clickable. **PERSIST**: URL/query param có `q=Mẫu HĐ`. | Happy | P0 |
| TC-BM-502 | FR-VII-05 AC2 | Filter lĩnh vực + loại hình + thư mục (AND) | `cb_nv_tw_01`. Seed 5 BM với combo khác nhau. | linh_vuc=DAN_SU, loai_hinh=HOP_DONG, thu_muc=HĐ_LĐ | 1. Set 3 filter. 2. [Tìm kiếm]. | **STATE**: Backend `WHERE linh_vuc_id=DAN_SU AND loai_hinh='HOP_DONG' AND thu_muc_id=HĐ_LĐ.id` AND auth scope (AND logic, srs-fr-09:414). **UI**: Bảng intersect 3 điều kiện. **PERSIST**: — | Happy | P0 |
| TC-BM-503 | FR-VII-05 AC3 | Filter định dạng file (.docx) | `cb_nv_tw_01`. Seed 4 BM: 2 docx + 1 xlsx + 1 doc. | dinh_dang=DOCX | 1. Filter định dạng=DOCX. 2. [Tìm kiếm]. | **STATE**: Backend `WHERE dinh_dang='DOCX'` (srs-fr-09:631 SCR cột filter định dạng). **UI**: Bảng 2 record. **PERSIST**: — | Happy | P1 |
| TC-BM-507 | FR-VII-05 / mã BM scope-out / SPEC-CLARIFY-BM-17 (Codex fix 2026-05-09) | Search keyword vs mã BM — verify SRS scope chỉ tên + mô tả | `cb_nv_tw_01`. Seed 2 BM: mã="BM-001" + mã="BM-0011" (mã auto-gen, srs-fr-09:632). | keyword="BM-001" | 1. Search keyword. | **STATE**: SRS srs-fr-09:402 nguyên văn `keyword: text N — Từ khóa (tên, mô tả)` — KHÔNG quote mã BM trong scope keyword. Behavior thực tế cần verify: (a) Bê BE strict spec → 0 result (vì keyword không match tên/mô tả của 2 BM); (b) BE expand scope → match cả mã. **UI**: Empty state hoặc match (tùy BE). **PERSIST**: Mark **SPEC-CLARIFY-BM-17** scope keyword có nên include mã BM hay không. (Codex BM-MED-001 finding) | Edge | P2 |

---

## B. NEGATIVE & SECURITY

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước | Kết quả mong đợi | Type | Priority |
|----|---------|--------------|----------------|-----------|----------|------------------|------|----------|
| TC-BM-504 | INF-BM-TK-01 | Search 0 result | `cb_nv_tw_01`. | keyword="ZZZ-NONE-9999" | 1. Search keyword không match. | **STATE**: Backend trả 0 row. **UI**: Empty state nguyên văn "Không tìm thấy biểu mẫu phù hợp" (srs-fr-09:438 INF-BM-TK-01). **PERSIST**: — | Negative | P0 |
| TC-BM-505 | BR-EC-13 | Search SQL injection / XSS payload | `cb_nv_tw_01`. | keyword=`'; DROP TABLE BIEU_MAU; --` rồi `<img src=x onerror=alert(1)>` | 1. Paste 2 payload (2 lần test). 2. [Tìm kiếm]. | **STATE**: Backend escape/parameterize. KHÔNG drop table; KHÔNG execute script. **UI**: Empty state hoặc literal match. **PERSIST**: BIEU_MAU table còn data sau request. `list_console_messages` không có alert. | Negative | P0 |
| TC-BM-508 | INF-BM-TK-01 / multi-filter empty (A4 merged) | Multi-filter AND không có kết quả intersection | `cb_nv_tw_01`. Seed 5 BM với combo lĩnh vực + thư mục đa dạng (không có BM nào thuộc cả LV=DAN_SU + thư mục="HĐ DV"). | linh_vuc=DAN_SU, thu_muc="HĐ DV" | 1. Set 2 filter intersect không có kết quả. 2. [Tìm kiếm]. | **STATE**: Backend trả 0 row (AND logic strict). **UI**: Empty state nguyên văn "Không tìm thấy biểu mẫu phù hợp" (srs-fr-09:438 INF-BM-TK-01). Khác với TC-BM-504 — TC này verify empty result do filter combo, không phải keyword không match. **PERSIST**: — | Negative | P2 |

---

## C. EDGE

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước | Kết quả mong đợi | Type | Priority |
|----|---------|--------------|----------------|-----------|----------|------------------|------|----------|
| TC-BM-506 | BR-EC-12 | Pagination boundary — page=0 / page_size=200 | `cb_nv_tw_01`. ≥30 BM tồn tại. | URL `?page=0`, `?page=-1`, `?page_size=200` | 1. URL direct hoặc API call. | **STATE**: Backend reject (BR-EC-12 page_size ∈ [1,100], page ≥ 1). **UI**: HTTP 400 hoặc fallback default 20/1 — message `ERR-PARAM-01` (SRS Gap nguyên văn → SPEC-CLARIFY-BM-07). **PERSIST**: — | Edge | P1 |
| TC-BM-509 | FR-VII-05 AC1 / BR-DATA-07 (Codex 2026-05-09) | Search BM pagination positive — default 20/page + page navigation + total_count | `cb_nv_tw_01` login. ≥45 BM thuộc TW match keyword="HĐ". | keyword="HĐ" | 1. SCR-VII-02 search "HĐ". 2. Verify page 1 = 20 rows + footer "1-20 / 45". 3. Click page 2 → 20 rows. 4. Click page 3 → 5 rows. | **STATE**: Backend `LIMIT 20 OFFSET 0/20/40` (srs-fr-09:416 Phân trang + trả về, BR-DATA-07 srs-fr-09:907). Output `total_count=45` (srs-fr-09:430 output#9). **UI**: Bảng SCR-VII-02 hiển thị 20→20→5 BM mỗi page. Pagination footer count khớp. **PERSIST**: URL `?q=HĐ&page=2`, reload giữ state. | Happy | P0 |

---

## Tổng số TC: 9 (5 Happy + 3 Negative + 1 Edge) — A3 base 6 + A4 merged 2 + Codex 2026-05-09 +1
**Priority**: P0=5 / P1=2 / P2=2

**Coverage:**
- BR (formal SRS §6): BR-AUTH-08, BR-DATA-07
- BR (working labels srs-v3.md inline / inline rule labels — see 00-test-plan §2.1 footnote): BR-EC-12 (pagination boundary), BR-EC-13 (search sanitize)
- Error codes: INF-BM-TK-01 (cover 2 case: keyword + filter combo)
- AC SRS: 3/3 (srs-fr-09:441-443) — AC1 pagination verified by TC-BM-509 sau Codex review
- A4 merged 2026-05-06: TC-BM-507 (mã BM scope), TC-BM-508 (multi-filter empty)
- Codex review 2026-05-09: TC-BM-509 (positive pagination — fix BM-HIGH-005), TC-BM-507 chuyển P1→P2 + đổi assertion sang SPEC-CLARIFY-BM-17 (fix BM-MED-001).
- SPEC-CLARIFY: BM-07 (ERR-PARAM-01 message), BM-17 (search keyword scope mã BM)
