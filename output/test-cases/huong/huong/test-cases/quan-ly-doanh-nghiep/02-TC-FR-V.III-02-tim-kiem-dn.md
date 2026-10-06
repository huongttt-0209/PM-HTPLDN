# Test Cases — FR-V.III-02: Tìm kiếm Doanh nghiệp + Xuất Excel

> **SRS Ref**: FR-V.III-02 (UC82), SCR-V.III-01 filter-bar, Entity DOANH_NGHIEP + DOANH_NGHIEP_LINH_VUC
> **Nguồn**: NotebookLM `4dd0675e-a4fa-4ea6-80ae-48e76b3fa264` + LOCAL `srs-fr-07-doanh-nghiep-v3.1.md:213-281` + Xuất Excel section line 154-163 (FR-V.III-01 Processing)
> **Ngày tạo**: 2026-05-09
> **Lưu ý**: CHANGELOG OUT D.2.1 — Xuất Excel chỉ giữ nút (không có Processing/AC). TC giả định nút Xuất Excel hoạt động per srs-fr-07-doanh-nghiep-v3.1.md:154-163 (kế thừa); SPEC-CLARIFY-DN-07 nếu nút disable hoặc 404.

---

## A. UI FIELD VERIFICATION

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|---------|---------------|----------------|-----------|--------------------|-------------------|------|
| TC-DN-TK-UI-01 | FR-V.III-02 / 6 filter components | Verify 6 filter input components | qtht_01 | URL `/doanh-nghiep/danh-sach` | 1. Mở SCR-V.III-01<br>2. Verify từng input | **6 FILTERS** (per srs:233-239): (1) tu_khoa text-input "Tìm theo tên/MST", (2) quy_mo select 3 enum, (3) tinh_thanh_id select cây 63 tỉnh GSO, (4) linh_vuc_kd **multi-select** DANH_MUC LV-KINH-DOANH, (5) tu_ngay date-picker, (6) den_ngay date-picker. **2 nút action**: "Tìm kiếm" + "Xóa bộ lọc" | Happy 🔴 |
| TC-DN-TK-UI-02 | FR-V.III-02 / Filter linh_vuc multi-select v3.1 | Verify Lĩnh vực KD đổi từ select đơn → multi-select (Thay đổi 9 v3.1) | qtht_01 | DANH_MUC LV: Lao động, Thuế, Thương mại | 1. Mở filter LV<br>2. Tick 2 LV | UI: Chip multi với 2 LV; KHÔNG còn select đơn (Thay đổi 9); Network query có `linh_vuc_ids[]=...&linh_vuc_ids[]=...` | Happy 🔴 |

## B. SEARCH (single filter)

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|---------|---------------|----------------|-----------|--------------------|-------------------|------|
| TC-DN-TK-001 | FR-V.III-02 / AC1 từ khóa tên DN | Tìm theo từ khóa Tên DN | qtht_01, DN "Công ty A", "Công ty B", "Đại lý C" | tu_khoa: "Công ty" | 1. Nhập "Công ty"<br>2. Click "Tìm kiếm" hoặc debounce | **STATE**: Network `GET /api/v1/doanh-nghieps?tu_khoa=Công ty&page=1`<br>**UI**: Table 2 record A + B; pagination total=2 | Happy 🔴 |
| TC-DN-TK-002 | FR-V.III-02 / Search by MST | Tìm theo MST | qtht_01, DN MST "0123456789" | tu_khoa: "0123456789" | 1. Nhập MST đầy đủ | Table 1 record có MST khớp | Happy 🟡 |
| TC-DN-TK-003 | FR-V.III-02 / Filter quy_mo SIEU_NHO | Filter SIEU_NHO | qtht_01, ≥3 DN SIEU_NHO + 2 NHO + 1 VUA | quy_mo: "SIEU_NHO" | 1. Chọn quy_mo SIEU_NHO<br>2. Verify | Table chỉ DN SIEU_NHO; pagination total=3 | Happy 🟡 |
| TC-DN-TK-004 | FR-V.III-02 / Filter tinh_thanh | Filter Tỉnh thành (DANH_MUC TINH_THANH) | qtht_01, DN-HN-001 + DN-HP-002 | tinh_thanh_id: "01" (Hà Nội GSO) | 1. Filter tỉnh "Hà Nội"<br>2. Verify | Table chỉ DN HN; mã GSO 01-63 (QĐ 124/2004/QĐ-TTg) | Happy 🟡 |
| TC-DN-TK-005 | FR-V.III-02 / Filter linh_vuc multi | Filter 2 LV (OR trong cùng filter, AND với filter khác) | qtht_01, DN x LV: A:[Lao động], B:[Thuế], C:[Lao động, Thuế] | linh_vuc_ids: ["Lao động", "Thuế"] | 1. Tick 2 LV<br>2. Verify | Table 3 record (A + B + C) — multi-select OR semantics; SPEC-CLARIFY-DN-08 nếu spec không define rõ OR/AND trong cùng filter multi | Happy 🟡 |
| TC-DN-TK-006 | FR-V.III-02 / Filter tu_ngay-den_ngay | Filter ngày hỗ trợ từ-đến | qtht_01, DN có VV tạo: 15/01/2026 + 20/03/2026 + 01/05/2026 | tu_ngay: 2026-01-01, den_ngay: 2026-04-30 | 1. Pick range<br>2. Verify | Table 2 DN (15/01 + 20/03), DN có VV 01/05 KHÔNG hiển thị (boundary EXCLUSIVE den_ngay+1) — OR mở rộng SPEC-CLARIFY-DN-09 | Happy 🟡 |
| TC-DN-TK-007 | FR-V.III-02 / E1 INF-DN-TK-01 | Không có kết quả → INF-DN-TK-01 | qtht_01 | tu_khoa: "ZZZZ-not-exist" | 1. Nhập payload<br>2. Verify | **STATE**: Network response `{data: [], total: 0}`<br>**UI**: Empty state "Không tìm thấy doanh nghiệp phù hợp" (NGUYÊN VĂN INF-DN-TK-01); KHÔNG toast lỗi | Negative 🔴 |
| TC-DN-TK-008 | FR-V.III-02 / Search empty | Tu_khoa rỗng → trả full list | qtht_01, ≥5 DN | tu_khoa: "" | 1. Click "Xóa bộ lọc"<br>2. Verify | Table list mặc định 20/trang (BR-DATA-07) | Happy 🟡 |

## C. SEARCH (multi-filter AND)

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|---------|---------------|----------------|-----------|--------------------|-------------------|------|
| TC-DN-TK-101 | FR-V.III-02 / AC4 AND multi-filter | Combine tu_khoa + quy_mo + tinh_thanh (AND) | qtht_01, mixed data | tu_khoa: "Công ty", quy_mo: SIEU_NHO, tinh_thanh: Hà Nội | 1. Set 3 filter<br>2. Tìm kiếm | **STATE**: Network `?tu_khoa=...&quy_mo=SIEU_NHO&tinh_thanh_id=01&page=1`<br>**UI**: Table chỉ DN match TẤT CẢ điều kiện (AND logic per srs:246) | Happy 🔴 |
| TC-DN-TK-102 | FR-V.III-02 / Combine 5 filter | Combine 5 filter | qtht_01, data đa dạng | tu_khoa+quy_mo+tinh_thanh+linh_vuc+ngày | 1. Set 5 filter<br>2. Verify | Network có đủ 5 param; Table chỉ record AND tất cả | Happy 🟡 |
| TC-DN-TK-103 | FR-V.III-02 / Reset filter | Click "Xóa bộ lọc" → reset all | qtht_01, có filter đang active | — | 1. Set 3 filter<br>2. Click "Xóa bộ lọc" | Filter UI clear; URL bỏ query param; Table list mặc định | Happy 🟡 |

## D. PAGINATION (BR-DATA-07)

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|---------|---------------|----------------|-----------|--------------------|-------------------|------|
| TC-DN-TK-201 | BR-DATA-07 / Default 20/page | Pagination default 20/trang | qtht_01, ≥21 DN | — | 1. Mở list<br>2. Đếm row | Table 20 row; pagination "1 / N"; Network response `page_size=20` | Happy 🔴 |
| TC-DN-TK-202 | BR-DATA-07 / Page 2 | Click trang 2 → 20 row tiếp theo | qtht_01, ≥21 DN | — | 1. Click pagination "2"<br>2. Verify | Table 1+ row mới; URL `?page=2`; sort updated_at DESC giữ nguyên | Happy 🟡 |
| TC-DN-TK-203 | BR-DATA-07 / Max 100/page | Page size 100 max | qtht_01, ≥101 DN | — | 1. Đổi page size dropdown 100<br>2. Verify | Table 100 row; SPEC-CLARIFY-DN-10 nếu UI không có dropdown | Happy 🟡 |
| TC-DN-TK-204 | BR-DATA-07 / Sort default | Sort default updated_at DESC | qtht_01, ≥3 DN với updated_at khác | — | 1. Verify thứ tự | DN updated_at mới nhất ở đầu (per srs:328 "ngày cập nhật mới nhất trước") | Happy 🟡 |

## E. EXPORT EXCEL (FR-V.III-01 Processing line 154-163, OUT D.2.1)

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|---------|---------------|----------------|-----------|--------------------|-------------------|------|
| TC-DN-TK-301 | FR-V.III-01 Excel / Happy export | Xuất Excel với filter hiện tại | qtht_01, ≥10 DN match filter | filter quy_mo=NHO | 1. Apply filter<br>2. Click "Xuất Excel"<br>3. Verify file | **STATE**: Network `GET /api/v1/doanh-nghieps/export?quy_mo=NHO`<br>**UI**: Toast "Xuất Excel thành công"; File `.xlsx` auto-download<br>**PERSIST**: Mở file — header chứa các cột: STT/Mã DN/Tên DN/MST/Quy mô/Địa chỉ/Số lần hỗ trợ/Tổng chi phí; Số dòng = số record sau filter | Happy 🔴 |
| TC-DN-TK-302 | FR-V.III-01 / ERR-DN-04 boundary 10K | Export >10K dòng → ERR-DN-04 | qtht_01, no filter (hoặc filter cho ra >10K) | — | 1. Click "Xuất Excel"<br>2. Verify warning | **UI**: Modal/Toast "Kết quả vượt 10.000 dòng. Vui lòng thu hẹp bộ lọc" (NGUYÊN VĂN ERR-DN-04); KHÔNG xuất file | Edge 🔴 |
| TC-DN-TK-303 | FR-V.III-01 / Export 0 record | Export với 0 record sau filter | qtht_01, filter no-match | tu_khoa: "ZZZZ" | 1. Filter ZZZZ<br>2. Click "Xuất Excel" | File header chỉ có header row, 0 data row; HOẶC toast "Không có dữ liệu để xuất"; SPEC-CLARIFY-DN-11 nếu SRS không define behavior | Edge 🟡 |
| TC-DN-TK-304 | FR-V.III-01 / Export 9999 boundary | Boundary 9999 (just under cap) | qtht_01, có 9999 DN match | — | 1. Click Export | File 9999 row; KHÔNG warning ERR-DN-04 | Edge 🟡 |
| TC-DN-TK-305 | FR-V.III-01 / Export 10000 boundary | Boundary 10000 (exact cap) | qtht_01, có 10000 DN match | — | 1. Click Export | File 10000 row; KHÔNG warning (per srs "≤ 10.000 dòng" — INCLUSIVE) | Edge 🟡 |
| TC-DN-TK-306 | FR-V.III-01 / Export 10001 boundary | Boundary 10001 (just over cap) | qtht_01, có 10001 DN match | — | 1. Click Export | Warning ERR-DN-04; KHÔNG xuất file | Edge 🟡 |

## F. PERSIST FILTER

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|---------|---------------|----------------|-----------|--------------------|-------------------|------|
| TC-DN-TK-401 | FR-V.III-02 / URL param persist | Reload với filter trong URL → giữ filter | qtht_01 | URL `?quy_mo=NHO&tinh_thanh_id=01` | 1. Tamper URL<br>2. Reload page | Filter UI auto-fill quy_mo=NHO + tinh_thanh=HN; Table apply | Happy 🟡 |
| TC-DN-TK-402 | FR-V.III-02 / Back button preserve | Click DN detail rồi back → filter giữ | qtht_01 | filter quy_mo=NHO | 1. Filter<br>2. Click DN<br>3. Browser back | Filter giữ nguyên; URL giữ query | Happy 🟡 |

---

## G. EDGE bổ sung (A4 inline merge — 7 edge)

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|---------|---------------|----------------|-----------|--------------------|-------------------|------|
| TC-DN-TK-501 | EDGE-A4-j / SQL injection tu_khoa | SQL injection payload trong tu_khoa | qtht_01 | tu_khoa: `'; DROP TABLE DOANH_NGHIEP--` | 1. Nhập payload<br>2. Search | Sanitize PASS — query parameterized; KHÔNG execute SQL; trả empty INF-DN-TK-01 | Edge 🔴 |
| TC-DN-TK-502 | EDGE-A4-k / XSS in tu_khoa | XSS payload trong tu_khoa | qtht_01 | tu_khoa: `<img src=x onerror=alert(1)>` | 1. Nhập<br>2. Search | Sanitize escape; URL ?tu_khoa=encoded; KHÔNG execute | Edge 🔴 |
| TC-DN-TK-503 | EDGE-A4-l / Unicode no-dấu | Search "cong ty" tìm "Công ty" | qtht_01, DN "Công ty A" | tu_khoa: "cong ty" | 1. Search | Tìm thấy "Công ty A" (Unicode collation accent-insensitive); HOẶC KHÔNG tìm thấy nếu DB strict; SPEC-CLARIFY-DN-28 | Edge 🟡 |
| TC-DN-TK-504 | EDGE-A4-m / Boundary 200 char tu_khoa | tu_khoa 200 ký tự + 201 over | qtht_01 | tu_khoa: 200 char + 201 char | 1. Submit 200 boundary<br>2. Submit 201 over | 200 PASS; 201 reject hoặc truncate; SPEC-CLARIFY-DN-29 nếu SRS không có max length | Edge 🟡 |
| TC-DN-TK-505 | EDGE-A4-n / Reversed date range | tu_ngay > den_ngay → inline error | qtht_01 | tu_ngay: 2026-05-09, den_ngay: 2026-05-01 | 1. Pick reversed | Inline error "Từ ngày phải nhỏ hơn hoặc bằng Đến ngày"; tương tự ERR-HSPL-06 ở module HSPL; SPEC-CLARIFY-DN-30 nếu module DN không có ERR code | Edge 🟡 |
| TC-DN-TK-506 | EDGE-A4-o / Timezone UTC+7 boundary | DN created 2026-05-08 23:59:00 +0700 với filter từ 09/05 | qtht_01, DN created đúng 23:59 ngày 08/05 | tu_ngay: 2026-05-09 | 1. Filter từ 09/05 | DN 23:59:00 ngày 08/05 KHÔNG xuất hiện (boundary EXCLUSIVE bắt đầu 00:00 09/05); UTC+7 enforce | Edge 🟡 |
| TC-DN-TK-507 | EDGE-A4-p / Sort secondary tie-breaker | 5 DN cùng updated_at (cùng giây) | qtht_01, 5 DN created cùng millisecond | — | 1. Sort default<br>2. Verify order | Tie-breaker by id DESC (consistent ordering); SPEC-CLARIFY-DN-31 nếu SRS không define sort secondary | Edge 🟡 |

---

**Tổng số TC**: 32 (2 UI + 8 Search single + 3 Combo + 4 Pagination + 6 Export + 2 Persist + 7 Edge A4)
