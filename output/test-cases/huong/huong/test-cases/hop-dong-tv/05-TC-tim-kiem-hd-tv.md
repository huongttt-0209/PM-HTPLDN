# Test Cases — FR-X.3-02 (UC159e): Tìm kiếm HĐ Tư vấn

> **SRS Ref**: FR-X.3-02, SCR-X3-01 (filter-bar row#3), Entity HOP_DONG_TU_VAN
> **Ngày tạo**: 2026-05-10
> **Đặc thù**: Full-text search trên tên + mã + bên B. Filter TVV (searchable), khoảng ngày. AND logic. Phân trang BR-DATA-07. Phân quyền BR-AUTH-08.

---

## Quy ước

- **Priority**: 🔴 P0 · 🟡 P1 · 🟢 P2
- **TraceID**: `FR-X.3-02 / {section}`
- **Pre-conditions mặc định**: cb_nv_tw_01 login. ≥30 HĐ thuộc TW (test phân trang).

---

## Trường input FR-X.3-02

| # | Field | Bắt buộc | Kiểu | Ràng buộc |
|---|-------|----------|------|-----------|
| 1 | keyword | N | text | Match tên HĐ + mã HĐ + bên B (full-text) |
| 2 | tvv_id | N | identifier | FK → TU_VAN_VIEN |
| 3 | tu_ngay | N | date | — |
| 4 | den_ngay | N | date | ≥ tu_ngay (E1 ERR-HDTV-TK-01) |

---

## A. TÌM KIẾM — HAPPY

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|---------|---------------|----------------|-----------|-------------------|------------------|------|
| TC-HDTK-001 | FR-X.3-02 / AC#1 + Processing step 2 | Tìm theo keyword (tên HĐ) | HĐ "Tư vấn pháp lý ABC" tồn tại. | keyword="ABC" | 1. Filter-bar nhập "ABC". 2. Submit/blur. | (1) GET `/hop-dong-tv/search?keyword=ABC`. (2) Danh sách lọc HĐ matching tên/mã/bên B. (3) Phân trang 20/page (BR-DATA-07). | Happy 🔴 |
| TC-HDTK-002 | FR-X.3-02 / AC#2 + GAP-X.3-03 | Lọc theo TVV | TVV "Nguyễn Văn A" (TVV001). HĐ link TVV001 = 5 HĐ. | tvv_id=TVV001 | 1. Filter dropdown TVV searchable. 2. Chọn "Nguyễn Văn A". | (1) GET với `tvv_id=TVV001`. (2) Trả 5 HĐ link TVV001. **AC marked `[GAP-X.3-03]` SRS line 246** — confirm với CĐT. | Happy 🟡 |
| TC-HDTK-003 | FR-X.3-02 / AC#3 + GAP-X.3-03 | Lọc khoảng ngày (theo thoi_han_bat_dau hay ngay_ky?) | HĐ A bat_dau=2026-06-01. HĐ B bat_dau=2026-08-01. | tu_ngay=2026-07-01, den_ngay=2026-09-30 | 1. Filter ngày. 2. Submit. | (1) Trả HĐ B (ngày 2026-08-01 trong khoảng). (2) **SPEC-CLARIFY-HDTV-04**: lọc theo `thoi_han_bat_dau` hay `ngay_ky` hay `created_at`? Quote `[GAP-X.3-03]`. | Happy 🟡 |

---

## B. TÌM KIẾM — NEGATIVE

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|---------|---------------|----------------|-----------|-------------------|------------------|------|
| TC-HDTK-010 | FR-X.3-02 / E1 ERR-HDTV-TK-01 | tu_ngay > den_ngay | cb_nv_tw_01 login. | tu_ngay=2026-09-01, den_ngay=2026-06-01 | 1. Filter ngày. 2. Submit. | (1) Reject: **"Ngày bắt đầu phải trước ngày kết thúc"** (ERR-HDTV-TK-01). (2) Không gọi API search. | Negative 🔴 |
| TC-HDTK-011 | FR-X.3-02 / E2 INF-HDTV-TK-01 + AC#3 | Không có kết quả | cb_nv_tw_01 login. | keyword="ZZZ_NOT_EXIST" | 1. Tìm với keyword không tồn tại. | (1) Hiển thị empty state: **"Không tìm thấy hợp đồng phù hợp"** (INF-HDTV-TK-01). | Negative 🟡 |

---

## C. TÌM KIẾM — EDGE

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|---------|---------------|----------------|-----------|-------------------|------------------|------|
| TC-HDTK-020 | FR-X.3-02 / BR-AUTH-08 + Processing step 1 | cb_nv_dp_01 (AG) chỉ thấy HĐ thuộc AG | cb_nv_dp_01 login. HĐ A thuộc TW. HĐ B thuộc AG. | keyword="" (all) | 1. Vào danh sách HĐ. | (1) Chỉ list HĐ thuộc AG (HĐ B). (2) HĐ A (TW) KHÔNG hiển thị. (BR-AUTH-08 enforce — no exception). | Edge 🔴 |
| TC-HDTK-021 | FR-X.3-02 / Processing step 3 (AND logic) | Combine keyword + TVV + ngày → AND filter | cb_nv_tw_01 login. HĐ matching keyword=ABC + TVV001 + range 2026-06..2026-09 = 1 HĐ. | keyword="ABC", tvv_id=TVV001, range=06-09 | 1. Filter tất cả 3 trường. 2. Submit. | (1) Trả 1 HĐ thỏa cả 3 điều kiện AND. | Edge 🟡 |
| TC-HDTK-022 | FR-X.3-02 / BR-DATA-07 boundary | Phân trang boundary 20/page | cb_nv_tw_01 login. ≥21 HĐ TW. | — | 1. Vào list HĐ. 2. Click trang 2. | (1) Trang 1 = 20 row. (2) Trang 2 = 1+ row. (3) Total count chính xác. | Edge 🟢 |
| TC-HDTK-023 | FR-X.3-02 / keyword full-text 3 fields (A4 merged) | Keyword match TÊN + MÃ + BÊN B (3 fields full-text) | HĐ A tên="Tư vấn ABC", HĐ B mã="HDTV-20260101-099", HĐ C ben_b="Công ty XYZ". | keyword="ABC" / "099" / "XYZ" | 1. Test 3 lần với 3 keyword. | Mỗi keyword trả về HĐ matching theo field tương ứng (full-text trên 3 fields, business §6 quote). | Edge 🟡 |
| TC-HDTK-024 | FR-X.3-02 / SQL injection (A4 merged) | Keyword chứa SQL injection payload — sanitize | cb_nv_tw_01 login. | keyword="' OR 1=1 --" | 1. Filter keyword với payload injection. | (1) Sanitize: query chạy như literal text. (2) KHÔNG return all rows (SQL injection block). (3) BR-EC-13 max 200 ký tự nếu áp dụng. | Edge 🔴 |
| TC-HDTK-025 | FR-X.3-02 / keyword Unicode (A4 merged) | Keyword tiếng Việt có dấu (Unicode UTF-8) | HĐ tên="Tư vấn Đại Học Bách Khoa". | keyword="Bách" | 1. Filter keyword tiếng Việt có dấu. | (1) Match đúng. (2) Test cả keyword không dấu "Bach" — kỳ vọng KHÔNG match (full-text strict) hoặc match (collation tiếng Việt). **SPEC-CLARIFY**: collation rule. | Edge 🟡 |
| TC-HDTK-026 | FR-X.3-02 / empty keyword (A4 merged) | Keyword rỗng → trả tất cả (scope đơn vị) | cb_nv_tw_01 login. ≥30 HĐ TW. | keyword="" | 1. Filter keyword rỗng. 2. Submit. | Trả tất cả HĐ TW phân trang 20/page (BR-DATA-07). KHÔNG validate "keyword bắt buộc". | Edge 🟢 |

---

## Tổng kết file 05-TC

- **Tổng số TC: 12** (3 Happy + 2 Negative + 7 Edge — A4 +4)
- **Critical TC (🔴)**: TC-HDTK-001, 010, 020, 024
- **A4 merged 2026-05-10**: TC-HDTK-023, 024, 025, 026
- **SPEC-CLARIFY refs**: HDTV-04 (lọc ngày theo field nào)

*Generated 2026-05-10 — Phase A step A3*
