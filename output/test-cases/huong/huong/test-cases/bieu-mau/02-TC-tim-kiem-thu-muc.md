# Test Cases — UC93: Tìm kiếm Thư mục Biểu mẫu (FR-VII-02)

> **SRS Ref**: FR-VII-02 (srs-fr-09:150-205), SCR-VII-01 (filter-bar), Entity THU_MUC_BIEU_MAU
> **Ngày tạo**: 2026-05-06 (BMAD A3)
> **Tài khoản chính**: `cb_nv_tw_01`

---

## A. SEARCH BY KEYWORD + FILTER

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước | Kết quả mong đợi | Type | Priority |
|----|---------|--------------|----------------|-----------|----------|------------------|------|----------|
| TC-BM-201 | FR-VII-02 AC1 | Tìm theo keyword khớp tên thư mục | `cb_nv_tw_01` đăng nhập. Đã có thư mục "Hợp đồng lao động" + "Hợp đồng dịch vụ" + "Mẫu đơn xin việc" thuộc TW. | keyword="Hợp đồng" | 1. Vào SCR-VII-01. 2. Nhập "Hợp đồng" vào ô từ khóa. 3. Click [Tìm kiếm] (hoặc Enter). | **STATE**: Backend `WHERE ten_thu_muc LIKE '%Hợp đồng%' OR mo_ta LIKE '%Hợp đồng%'` AND `is_deleted=0` AND `don_vi_id=TW.id` (BR-AUTH-08, srs-fr-09:174). **UI**: Bảng hiển thị 2 thư mục match. URL/query param có `q=Hợp%20đồng`. **PERSIST**: Reload giữ filter (qua URL state). Response ≤ 2s (mặc định). | Happy | P0 |
| TC-BM-202 | FR-VII-02 AC2 | Filter date range + lĩnh vực kết hợp | `cb_nv_tw_01`. 4 thư mục: 2026-01-15 (DAN_SU), 2026-03-20 (HINH_SU), 2026-04-25 (DAN_SU), 2026-05-01 (LAO_DONG). | tu_ngay=2026-02-01, den_ngay=2026-04-30, linh_vuc=DAN_SU | 1. Filter từ ngày + đến ngày + lĩnh vực=DAN_SU. 2. [Tìm kiếm]. | **STATE**: Backend `WHERE created_at BETWEEN '2026-02-01' AND '2026-04-30' AND linh_vuc_id=DAN_SU` (AND logic, srs-fr-09:175-176). **UI**: Bảng hiển thị 1 record (2026-04-25 DAN_SU). **PERSIST**: — | Happy | P0 |
| TC-BM-203 | FR-VII-02 AC3 | Filter trạng thái = CONG_KHAI | `cb_nv_tw_01`. 5 thư mục: 2 NHAP + 2 CONG_KHAI + 1 AN. | trang_thai=CONG_KHAI | 1. Filter trạng thái = "Đã công khai". 2. [Tìm kiếm]. | **STATE**: Backend `WHERE trang_thai='CONG_KHAI'`. **UI**: Bảng 2 record CONG_KHAI. Tab "Đã công khai" badge số = 2. **PERSIST**: — | Happy | P1 |

---

## B. NEGATIVE — VALIDATION & EMPTY

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước | Kết quả mong đợi | Type | Priority |
|----|---------|--------------|----------------|-----------|----------|------------------|------|----------|
| TC-BM-204 | ERR-TK-01 | Date range invalid: tu_ngay > den_ngay | `cb_nv_tw_01`. | tu_ngay=2026-05-01, den_ngay=2026-04-01 | 1. Filter date range invalid. 2. [Tìm kiếm]. | **STATE**: Backend reject hoặc client validate trước. **UI**: Toast error nguyên văn "Ngày bắt đầu phải trước ngày kết thúc" (srs-fr-09:198 ERR-TK-01). Bảng KHÔNG reload. **PERSIST**: — | Negative | P1 |
| TC-BM-205 | INF-TM-TK-01 | Search 0 result | `cb_nv_tw_01`. | keyword="ZZZZ-NOT-EXIST-9999" | 1. Search keyword không match. | **STATE**: Backend trả 0 row. **UI**: Empty state nguyên văn "Không tìm thấy thư mục phù hợp" (srs-fr-09:199 INF-TM-TK-01). Bảng trống. **PERSIST**: — | Negative | P0 |

---

## C. SECURITY & EDGE

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước | Kết quả mong đợi | Type | Priority |
|----|---------|--------------|----------------|-----------|----------|------------------|------|----------|
| TC-BM-206 | BR-EC-13 | Search SQL injection — sanitize | `cb_nv_tw_01`. | keyword=`'; DROP TABLE THU_MUC_BIEU_MAU; --` | 1. Paste payload. 2. [Tìm kiếm]. | **STATE**: Backend escape/parameterize query. KHÔNG drop table. **UI**: Empty state hoặc match literal. KHÔNG expose stack trace. **PERSIST**: Verify THU_MUC_BIEU_MAU table còn data sau request (count > 0). | Negative | P0 |
| TC-BM-207 | BR-EC-13 | Search XSS — sanitize | `cb_nv_tw_01`. | keyword=`<script>alert('XSS')</script>` | 1. Paste XSS payload. 2. [Tìm kiếm]. | **STATE**: Backend lưu plain string. **UI**: Trình duyệt KHÔNG execute script (verify `list_console_messages` không có alert dialog). Hiển thị payload escaped trong breadcrumb/echo. **PERSIST**: — | Negative | P0 |
| TC-BM-208 | FR-VII-02 / Vietnamese Unicode (A4 merged) | Search keyword tiếng Việt có dấu — Unicode collation | `cb_nv_tw_01`. TM "Lê Văn Cường" tồn tại. | keyword="Lê Văn" | 1. Search. | **STATE**: Backend handle Vietnamese Unicode collation (LIKE `%Lê Văn%` với UTF-8). **UI**: Bảng match "Lê Văn Cường". **PERSIST**: — | Edge | P2 |
| TC-BM-209 | BR-EC-13 / SQL LIKE wildcard escape (A4 merged) | Search keyword `100%` và `user_name` — escape `%` `_` | `cb_nv_tw_01`. TM "Báo cáo 100%" + TM "user_name_test" tồn tại. | keyword="100%" rồi "user_name" | 1. Search 2 keyword (2 lần). | **STATE**: Backend escape `%` và `_` trước khi build LIKE. **UI**: Bảng hiển thị chỉ TM match LITERAL "100%" + literal "user_name" (KHÔNG match toàn bộ records — nếu match all = BE bug missing escape). **PERSIST**: — Sibling pattern: CG-TVV TC-CG-115. | Edge | P1 |
| TC-BM-210 | BR-EC-13 / boundary 200 ký tự (A4 merged) | Search keyword exactly 200 ký tự (BR-EC-13 boundary) | `cb_nv_tw_01`. | keyword="A"×200 | 1. Paste 200 ký tự. 2. [Tìm kiếm]. | **STATE**: BE accept (BR-EC-13 nguyên văn "max 200 ký tự"). **UI**: Hiển thị empty/match. **PERSIST**: Test thêm boundary 201 → expect reject hoặc truncate. | Edge | P2 |
| TC-BM-211 | FR-VII-02 / BR-DATA-07 (Codex 2026-05-09) | Search TM pagination boundary — default 20/page, max 100, page=2 navigation | `cb_nv_tw_01` login. ≥125 TM thuộc TW (seed). | page_size không set (default), keyword=`""` empty | 1. Vào SCR-VII-01 search (no keyword). 2. Verify page 1 = 20 rows. 3. Click page 2 → verify 20 rows. 4. Đổi page_size=100 → verify 100 rows. 5. URL `?page_size=101` direct. | **STATE**: Backend `LIMIT 20 OFFSET 0` mặc định (srs-fr-09:177, 907 BR-DATA-07). page_size=100 accepted. page_size=101 reject hoặc clamp về 100 (verify behavior thực tế — mark **SPEC-CLARIFY-BM-18** nếu silent clamp). **UI**: Pagination footer "1-20 / 125", "21-40 / 125" sau click page 2. Total_count=125 hiển thị. **PERSIST**: URL có `?page=2`, reload giữ page state. | Edge | P1 |

---

## Tổng số TC: 11 (3 Happy + 2 Negative + 6 Edge) — A3 base 7 + A4 merged 3 + Codex 2026-05-09 +1
**Priority**: P0=4 / P1=5 / P2=2

**Coverage:**
- BR: BR-AUTH-08, BR-DATA-07, BR-EC-13
- Error codes: ERR-TK-01, INF-TM-TK-01
- AC SRS: 3/3 (srs-fr-09:201-204)
- A4 merged 2026-05-06: TC-BM-208..210 (Unicode + wildcard escape + boundary 200)
- Codex review 2026-05-09: TC-BM-211 (pagination default/max BR-DATA-07 — fix BM-HIGH-001). SPEC-CLARIFY-BM-18 (page_size=101 reject vs clamp).
