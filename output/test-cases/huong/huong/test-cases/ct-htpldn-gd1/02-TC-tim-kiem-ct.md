# Test Cases — FR-XI-02 (UC161): Tìm kiếm CT HTPL + Xuất Excel

> **SRS Ref**: FR-XI-02, SCR-XI-01 (filter-bar + table + export Excel), Entity CHUONG_TRINH_HTPL
> **Ngày tạo**: 2026-05-06
> **Đặc thù**: Filter AND nhiều điều kiện. Read-only. Pagination 20/page. Export tối đa 10,000 rows.

---

## Quy ước

- **Priority**: 🔴 P0 · 🟡 P1 · 🟢 P2
- **Pre-conditions mặc định**: User đã đăng nhập, có quyền truy cập SCR-XI-01

---

## Trường input filter

| # | Field | Bắt buộc | Kiểu | Ràng buộc |
|---|-------|----------|------|-----------|
| 1 | keyword | N | text | Tìm theo `ten_chuong_trinh` hoặc `ma_chuong_trinh` |
| 2 | don_vi_id | N | identifier | Auto phân quyền nếu không truyền (BR-AUTH-08) |
| 3 | trang_thai | N | text | Trạng thái SM-KH-CTHTPL |
| 4 | tu_ngay | N | date | — |
| 5 | den_ngay | N | date | — |

---

## A. SEARCH — HAPPY

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|---------|--------------|----------------|-----------|-------------------|------------------|------|
| TC-CT-TK-001 | FR-XI-02 / AC#1 | Tìm theo keyword (mã CT) | cb_nv_tw_01 login. CT-DT01 + CT-DD05 tồn tại. | keyword="CT-2026" | 1. Nhập keyword vào ô tìm. 2. Enter / Tìm kiếm. | (3) DS hiển thị các CT khớp `ma_chuong_trinh` chứa "CT-2026". Network GET `/api/v1/chuong-trinh-htpl?keyword=CT-2026` 200. | Happy 🔴 |
| TC-CT-TK-002 | FR-XI-02 / AC#1 + BR-DATA-07 | Lọc theo trạng thái + phân trang | cb_nv_tw_01 login. ≥25 CT trạng thái DA_DUYET. | trang_thai=DA_DUYET | 1. Chọn filter trạng thái DA_DUYET. 2. Tìm. | (3) DS chỉ chứa CT DA_DUYET, phân trang 20/page. | Happy 🔴 |
| TC-CT-TK-003 | FR-XI-02 / Processing step 2 | Lọc khoảng ngày AND keyword | cb_nv_tw_01 login. | tu_ngay="2026-01-01", den_ngay="2026-12-31", keyword="HTPLDN" | 1. Set 2 filter ngày + keyword. 2. Tìm. | (3) DS thỏa cả 3 điều kiện AND. Empty kết quả ngoài range KHÔNG hiển thị. | Happy 🟡 |
| TC-CT-TK-004 | FR-XI-02 / Inputs#2 + BR-AUTH-08 | Filter đơn vị scoped | cb_nv_dp_01 (Sở TP AG) login. | — | 1. Mở filter "Đơn vị". | (3) Dropdown chỉ hiện đơn vị thuộc scope user (Sở TP AG). KHÔNG thấy Bộ KH&ĐT (BN). | Happy 🟢 |
| TC-CT-TK-005 | FR-XI-02 / E1 INF-CT-TK-01 | Không tìm thấy | cb_nv_tw_01 login. | keyword="ZZZZ_KHONG_TON_TAI" | 1. Tìm với keyword không match. | (3) Toast/inline INFO "Không tìm thấy chương trình phù hợp" (INF-CT-TK-01). DS empty state. | Happy 🟢 |

---

## B. EXPORT EXCEL — HAPPY + EDGE

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|---------|--------------|----------------|-----------|-------------------|------------------|------|
| TC-CT-TK-006 | FR-XI-02 / AC Xuất Excel#1 | Xuất Excel theo filter hiện tại | cb_nv_tw_01 login. ≥5 CT thỏa filter. | trang_thai=DA_DUYET | 1. Set filter. 2. Click [Xuất Excel]. | (3) File `.xlsx` tải về với cột: Mã CT / Tên CT / Mục tiêu / Đối tượng / Thời gian (BĐ-KT) / Ngân sách / Đơn vị / Trạng thái / Số đợt BC. Số dòng = kết quả filter. | Happy 🔴 |
| TC-CT-TK-007 | FR-XI-02 / AC Xuất Excel#3 + BR-DATA-07 (Codex fix 2026-05-09) | Xuất Excel >10,000 dòng → cắt + cảnh báo | cb_nv_tw_01 login. >10,000 CT (test env hoặc set page_size cao). | — | 1. Click [Xuất Excel] khi DS >10k. | (3) File chỉ có 10,000 dòng đầu + Toast WARNING "Kết quả vượt 10.000 dòng, chỉ xuất 10.000 dòng đầu tiên" (WRN-XI-02-XL-01). **Note Codex 2026-05-09:** Đổi trace từ `BR-DATA-06` (không có trong srs-fr-15 §6) → `BR-DATA-07` (srs-fr-15:395 nguyên văn "Giới hạn tối đa 10.000 dòng xuất | BR-DATA-07"). 00-test-plan §2.1 row BR-DATA-06 vẫn giữ làm working label từ srs-v3.md. | Edge 🟡 |
| TC-CT-TK-008 | FR-XI-02 / AC Xuất Excel#2 | Xuất Excel khi DS trống | cb_nv_tw_01 login. Filter rỗng kết quả. | keyword="ZZZ" | 1. Set filter no-match. 2. Click [Xuất Excel]. | (3) Toast INFO "Không có chương trình nào để xuất" (INF-XI-02-XL-01). KHÔNG tạo file. | Negative 🟡 |

---

## C. SEARCH — EDGE / SECURITY

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|---------|--------------|----------------|-----------|-------------------|------------------|------|
| TC-CT-TK-009 | FR-XI-02 / BR-EC-12 | Pagination guard `page_size > 100` | cb_nv_tw_01 login. | URL `?page_size=200` | 1. Sửa URL set page_size=200. | (1) Backend reject với ERR-PARAM-01 HOẶC clamp về 100. Network response chứa lỗi rõ. | Edge 🟢 |
| TC-CT-TK-010 | FR-XI-02 / BR-EC-13 | Search sanitize SQL injection | cb_nv_tw_01 login. | keyword=`'; DROP TABLE CHUONG_TRINH_HTPL; --` | 1. Nhập keyword chứa SQL. 2. Tìm. | (3) Backend escape/sanitize, trả empty hoặc match literal. KHÔNG drop bảng. Network 200 với DS bình thường. | Edge 🔴 |
| TC-CT-TK-011 | FR-XI-02 / BR-EC-13 | Search sanitize XSS | cb_nv_tw_01 login. | keyword=`<script>alert(1)</script>` | 1. Nhập + Tìm. | (3) Keyword được escape khi render lại trong filter chip; KHÔNG trigger alert. | Edge 🔴 |
| TC-CT-TK-012 | FR-XI-02 / Inputs#4-5 (A4 merged) | tu_ngay > den_ngay validation | cb_nv_tw_01 login. | tu_ngay="2026-12-31", den_ngay="2026-01-01" | 1. Set 2 date range ngược nhau. 2. Tìm. | (2) Validation reject — DatePicker tự disable selection ngược, hoặc backend reject với inline error "Ngày bắt đầu phải trước Ngày kết thúc". KHÔNG submit. | Edge 🟡 |

---

## Tổng kết file 02-TC

- **12 TC**: 5 Happy search + 3 Export + 4 Edge/Security (A3 base 11 + A4 merged 1)
- **Critical TC (🔴)**: 001, 002, 006, 010, 011
- **A4 merged 2026-05-06**: TC-CT-TK-012

*Generated 2026-05-06 — Phase A step A3 + A4 inline merge*
