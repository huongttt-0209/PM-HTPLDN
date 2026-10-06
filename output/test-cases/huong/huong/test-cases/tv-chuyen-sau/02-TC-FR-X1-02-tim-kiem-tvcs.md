# Test Cases — UC148: Tìm kiếm nội dung TVCS (FR-X.1-02)

> **SRS Ref:** FR-X.1-02, SCR-X1-01 (filter-bar), Entity TU_VAN_CHUYEN_SAU
> **Nguồn:** `input/srs-v3/srs-fr-12-tv-chuyen-sau-v3.1.md` (line 319-398 UC148 + line 1057-1102 SCR-X1-01 filter-bar)
> **Ngày tạo:** 2026-05-06
> **Tác giả:** Phase A — bmad-qa-generate-e2e-tests (W3.3)

> **Iron rules:** Mỗi TC quote SRS line cụ thể. Không bịa BR/AC ngoài SRS. OTP login mặc định = `666666`.

---

## Section A — UI Verify (1 TC)

| ID | Tên | Type | Priority | Tài khoản | Steps | Expected | SRS ref | Notes |
|----|-----|------|----------|-----------|-------|----------|---------|-------|
| TC-TVCS-TK-001 | UI Verify SCR-X1-01 filter-bar 8 control + 3 tab + pagination | UI Verify | P0 | cb_nv_tw_01 | **Pre:** ≥20 record TVCS. **Steps:** 1) Login cb_nv_tw_01. 2) URL `/tv-chuyen-sau/danh-sach`. 3) `take_snapshot` verify filter-bar gồm: (1) ô Tìm kiếm full-text, (2) Dropdown Chuyên gia searchable, (3) Dropdown DN searchable, (4) Dropdown Lĩnh vực, (5) Dropdown Trạng thái 7 enum, (6) Khoảng ngày from/to, (7) 3 Tab phân loại "Chờ xử lý"/"Đang tư vấn"/"Hoàn thành" với count badge, (8) Pagination 20/page footer. 4) Verify filter logic AND default. | Tất cả 8 control hiển thị đúng vị trí + searchable interaction (CG, DN). 3 tab với count badge match dữ liệu. Pagination 20/page. Sort default ngày tạo DESC. | srs-fr-12 line 1071-1083 (toàn bộ component) + line 1100-1101 (sort default + AND logic) | — |

---

## Section B — Filter cá nhân (8 TC)

| ID | Tên | Type | Priority | Tài khoản | Steps | Expected | SRS ref | Notes |
|----|-----|------|----------|-----------|-------|----------|---------|-------|
| TC-TVCS-TK-002 | Filter `tu_khoa` — FTS noi_dung_tu_van + ma_noi_dung + ten DN | Happy | P0 | cb_nv_tw_01 | **Pre:** seed TVCS-X có noi_dung chứa "hợp đồng lao động", TVCS-Y có ten DN "Công ty ABC", TVCS-Z không match. **Steps:** 1) Filter tu_khoa="hợp đồng lao động" → verify TVCS-X xuất hiện. 2) Tu_khoa="ABC" → verify TVCS-Y xuất hiện qua match ten DN. 3) Tu_khoa=ma TVCS-Y → verify match ma_noi_dung. 4) `list_network_requests` verify GET `/api/v1/tu-van-chuyen-sau?q=...`. | Cả 3 lần search trả đúng record. TVCS-Z không match không xuất hiện. Network query param q gửi đúng. | srs-fr-12 line 341 (tu_khoa range) + line 356 (BR-DATA-08 FTS) + line 1074 (search-box full-text) | — |
| TC-TVCS-TK-003 | Filter `tu_ngay` + `den_ngay` trên ngay_tu_van | Happy | P0 | cb_nv_tw_01 | **Pre:** seed TVCS với ngay_tu_van: 2026-05-01, 2026-05-05, 2026-05-10. **Steps:** 1) Filter tu_ngay=2026-05-03, den_ngay=2026-05-08. 2) Verify chỉ record 2026-05-05 xuất hiện. | Chỉ record trong khoảng ngày trả về. Format date dd/mm/yyyy hiển thị (line 379). | srs-fr-12 line 342-343 (tu_ngay/den_ngay) + line 357 (Processing lọc khoảng ngày) + line 379 (format dd/mm/yyyy) | — |
| TC-TVCS-TK-004 | Filter `chuyen_gia_id` — chỉ TVCS của CG được chọn | Happy | P1 | cb_nv_tw_01 | **Pre:** seed TVCS phân công cg_01 (3 record), cg_02 (2 record). **Steps:** 1) Filter dropdown Chuyên gia = cg_01. 2) Verify 3 record. | 3 record cg_01 hiển thị, 2 record cg_02 ẩn. | srs-fr-12 line 344 (chuyen_gia_id) + line 358 + line 1075 (dropdown CG searchable) | — |
| TC-TVCS-TK-005 | Filter `linh_vuc_id` — chỉ TVCS thuộc lĩnh vực | Happy | P1 | cb_nv_tw_01 | **Pre:** seed TVCS lĩnh vực DAN_SU (4 record), HINH_SU (2 record). **Steps:** 1) Filter Lĩnh vực = DAN_SU. 2) Verify 4 record. | 4 record DAN_SU hiển thị. | srs-fr-12 line 345 (linh_vuc_id) + line 359 + line 1077 | — |
| TC-TVCS-TK-006 | Filter `trang_thai` — 7 enum SM-TVCS | Happy | P1 | cb_nv_tw_01 | **Pre:** seed 1 record mỗi trạng thái 7 enum. **Steps:** 1) Filter trang_thai=DA_DUYET → 1 record. 2) Filter HUY → 1 record. 3) Filter TIEP_NHAN → 1 record. | Mỗi filter trả đúng 1 record matching trạng thái chọn. | srs-fr-12 line 346 (7 enum SM-TVCS) + line 360 + line 1078 | — |
| TC-TVCS-TK-007 | Filter `page` >= 1 — pagination chuyển trang | Happy | P1 | cb_nv_tw_01 | **Pre:** seed ≥45 TVCS. **Steps:** 1) Default page=1, page_size=20 → 20 record. 2) Click page 2 → 20 record tiếp. 3) Click page 3 → 5 record cuối. | page 1: 20 record (sort ngay_tao DESC). page 2: 20 record. page 3: 5 record. Network query `?page=2&page_size=20`. | srs-fr-12 line 347 (page ≥1) + line 362 (BR-DATA-07) + line 1083 (pagination 20/page) | — |
| TC-TVCS-TK-008 | Filter `page_size` boundary — 1, 20 default, 100 max | Edge | P1 | cb_nv_tw_01 | **Pre:** seed ≥120 TVCS. **Steps:** 1) page_size=1 → 1 record. 2) page_size không truyền → default 20 (line 348). 3) page_size=100 → 100 record. | Cả 3 boundary đều OK theo BR-DATA-07. | srs-fr-12 line 348 (page_size 1-100 default 20) + line 362 (BR-DATA-07 max 100) | — |

---

## Section C — AND logic + Edge (2 TC)

| ID | Tên | Type | Priority | Tài khoản | Steps | Expected | SRS ref | Notes |
|----|-----|------|----------|-----------|-------|----------|---------|-------|
| TC-TVCS-TK-009 | AND logic — kết hợp 3 filter (tu_khoa + chuyen_gia + linh_vuc) | Happy | P0 | cb_nv_tw_01 | **Pre:** seed TVCS-A (cg_01 + DAN_SU + "hợp đồng"), TVCS-B (cg_02 + DAN_SU + "hợp đồng"), TVCS-C (cg_01 + HINH_SU + "hợp đồng"). **Steps:** 1) Filter tu_khoa="hợp đồng" + chuyen_gia=cg_01 + linh_vuc=DAN_SU. 2) Verify chỉ TVCS-A. | TVCS-A duy nhất khớp tất cả 3 điều kiện AND. TVCS-B/C bị loại. | srs-fr-12 line 361 (AND logic) + line 1101 (filter logic AND) + AC line 398 | — |
| TC-TVCS-TK-010 | Edge unicode tiếng Việt unaccent — "đào tạo" match "dao tao" (BR-DATA-08) | Edge | P1 | cb_nv_tw_01 | **Pre:** seed TVCS-X có noi_dung chứa "đào tạo nhân viên". **Steps:** 1) Filter tu_khoa="dao tao" (không dấu). 2) Verify TVCS-X xuất hiện. 3) Filter tu_khoa="ĐÀO TẠO" (UPPERCASE có dấu). 4) Verify cũng match. | Cả 2 lần search trả TVCS-X (BR-DATA-08 FTS hỗ trợ tiếng Việt unaccent + case-insensitive). | srs-fr-12 line 356 (BR-DATA-08 FTS unaccent) + Phụ lục B BR-DATA-08 | — |

---

## Section D — Negative (3 TC)

| ID | Tên | Type | Priority | Tài khoản | Steps | Expected | SRS ref | Notes |
|----|-----|------|----------|-----------|-------|----------|---------|-------|
| TC-TVCS-TK-011 | Negative `tu_ngay > den_ngay` → ERR-TVCS-TK-01 | Negative | P0 | cb_nv_tw_01 | **Steps:** 1) Filter tu_ngay=2026-05-10, den_ngay=2026-05-05. 2) Submit search. | Inline error nguyên văn "Ngày bắt đầu phải trước ngày kết thúc" (ERR-TVCS-TK-01). Không gửi request search. | srs-fr-12 line 343 (den_ngay >= tu_ngay) + line 390 (ERR-TVCS-TK-01) | — |
| TC-TVCS-TK-012 | Negative SQL injection / XSS — sanitize BR-EC-13 max 200 ký | Negative | P0 | cb_nv_tw_01 | **Steps:** 1) tu_khoa=`' OR 1=1--`. Submit. 2) tu_khoa=`<script>alert(1)</script>`. Submit. 3) tu_khoa=chuỗi 250 ký. Submit. | Cả 3 request: BE sanitize, không trả toàn bộ table; XSS không execute (HTML escape); chuỗi 250 ký bị truncate ở 200 hoặc reject inline "Tối đa 200 ký tự". Không có lỗi 500 hoặc data leak. | srs-fr-12 BR-EC-13 cross-cutting (sanitize max 200 ký) | — |
| TC-TVCS-TK-013 | Negative `page_size > 100` hoặc <= 0 → BR-DATA-07 cap/reject | Negative | P1 | cb_nv_tw_01 | **Steps:** 1) API direct GET `/api/v1/tu-van-chuyen-sau?page_size=200`. 2) `page_size=0`. 3) `page_size=-5`. | Bước 1: hoặc BE cap = 100 (trả 100 record), hoặc HTTP 400. Bước 2 + 3: HTTP 400 "page_size phải >=1" (line 348 ràng buộc 1-100). | srs-fr-12 line 348 (page_size 1-100) + line 362 (BR-DATA-07 max 100) | — |

---

## Section E — Cross-unit BR-AUTH-08 (1 TC)

| ID | Tên | Type | Priority | Tài khoản | Steps | Expected | SRS ref | Notes |
|----|-----|------|----------|-----------|-------|----------|---------|-------|
| TC-TVCS-TK-014 | BR-AUTH-08 cross-unit isolation — cb_nv_dp_01 chỉ thấy TVCS đơn vị mình | Negative | P0 | cb_nv_dp_01 | **Pre:** seed TVCS thuộc TW (3 record), BN (2 record), ĐP-AG (1 record của cb_nv_dp_01.don_vi_id), ĐP-BG (1 record). **Steps:** 1) Login cb_nv_dp_01 (đơn vị AG). 2) SCR-X1-01 → tab "Chờ xử lý" + tất cả tab khác. 3) Verify backend filter scope. | Chỉ 1 record ĐP-AG hiển thị. Các record TW/BN/ĐP-BG ẩn (BR-AUTH-08). API GET kèm filter don_vi_id automatically. Không có cross-cấp leak. | srs-fr-12 line 1531-1535 (BR-AUTH-08 nguyên văn) + line 354 (UC148 Processing Bước 1 "Kiểm tra quyền và phạm vi đơn vị") + Entity line 1298 (multi-tenant scope don_vi_id) | — |

---

## Section F — Export Excel (1 TC)

| ID | Tên | Type | Priority | Tài khoản | Steps | Expected | SRS ref | Notes |
|----|-----|------|----------|-----------|-------|----------|---------|-------|
| TC-TVCS-TK-015 | Export Excel max 10k rows (BR-DATA-06) | Edge | P1 | cb_nv_tw_01 | **Pre:** seed ≥10001 TVCS thuộc đơn vị TW. **Steps:** 1) SCR-X1-01 → click [Xuất Excel]. 2) `list_network_requests` verify GET `/api/v1/tu-van-chuyen-sau/export?...`. 3) Repeat với scope <=10k records. | Trường hợp >10k: API trả 400 hoặc cap export 10k đầu tiên + warning toast "Chỉ xuất tối đa 10,000 bản ghi" (BR-DATA-06). Trường hợp <=10k: file xlsx download thành công. KHÔNG verify query DB; chỉ verify network endpoint + response. | srs-fr-12 BR-DATA-06 cross-cutting (max 10k rows) + overview file 00 line 225 | A7 IN-PLACE: TC verify qua network request, không phải DB query thuần. |

---

## Section G — Edge bổ sung A4 (Boundary search + cross-feature state)

| ID | Tên | Type | Priority | Tài khoản | Steps | Expected | SRS ref | Notes |
|----|-----|------|----------|-----------|-------|----------|---------|-------|
| TC-TVCS-TK-016 | Boundary tu_khoa: chỉ space (1-5 ký tự whitespace) → trim/empty handling | Edge | P2 | cb_nv_tw_01 | **Steps:** 1) tu_khoa="     " (5 space). Submit. 2) tu_khoa="\t\n" (whitespace). Submit. 3) tu_khoa="" empty. | Cả 3 case: BE trim → coi như empty → trả full list theo các filter còn lại (không filter theo tu_khoa). KHÔNG lỗi 500. KHÔNG match record nào theo logic "space match all". | srs-fr-12 line 341 (tu_khoa optional) | No SRS quote whitespace handling — best practice extrapolation. SPEC-CLARIFY-TVCS-TK-01 trim policy. |
| TC-TVCS-TK-017 | Boundary tu_khoa max 200 ký exact + 201 ký reject (BR-EC-13 boundary) | Edge | P1 | cb_nv_tw_01 | **Steps:** 1) tu_khoa = chuỗi 200 ký "A" exact → Submit. 2) tu_khoa = chuỗi 201 ký → Submit. | Lần 1: PASS, search executed, response OK. Lần 2: UI inline error "Tối đa 200 ký tự" hoặc input bị cap ở 200 (BR-EC-13). KHÔNG gửi request với 201 ký. | srs-fr-12 BR-EC-13 cross-cutting | A4 boundary triple — extends TC-TVCS-TK-012 hỗn hợp 3 case. |
| TC-TVCS-TK-018 | Deep page navigation: page=99999 ngoài range → empty + status 200 | Edge | P2 | cb_nv_tw_01 | **Pre:** seed ≤100 TVCS. **Steps:** 1) URL `/tv-chuyen-sau/danh-sach?page=99999&page_size=20`. 2) `list_network_requests` GET `/api/v1/tu-van-chuyen-sau?page=99999`. | HTTP 200 với `data: []` empty array. UI hiển thị empty state "Không có dữ liệu". KHÔNG lỗi 500 hoặc OOM. Pagination footer "Trang 99999/X (X<99999)" hoặc auto-redirect page=last. | srs-fr-12 line 347 (page ≥1) + line 1083 (pagination) | No SRS quote upper bound page — best practice. SPEC-CLARIFY-TVCS-TK-02 auto-clamp behavior. |
| TC-TVCS-TK-019 | Cross-feature: chuyển tab giữ filter state (search persistent) | Edge | P1 | cb_nv_tw_01 | **Pre:** seed mỗi trạng thái 7 enum ≥2 record matching keyword "hợp đồng". **Steps:** 1) Tab "Chờ xử lý" → filter tu_khoa="hợp đồng" → submit. 2) Click tab "Đang tư vấn" → quan sát filter-bar. 3) Click tab "Hoàn thành". 4) Quay lại tab "Chờ xử lý". | Filter tu_khoa="hợp đồng" được giữ qua các tab (filter persist client-side). Mỗi tab trả record matching keyword + nhóm trạng thái tương ứng. URL deeplink param q="hợp đồng" giữ qua mọi tab navigation. | srs-fr-12 line 1073 (3 tab filter) + line 1100 | No SRS quote filter persistent across tabs — best practice extrapolation. SPEC-CLARIFY-TVCS-TK-03 reset on tab switch vs persist. |

---

## Section H — INF-TVCS-TK-01 Empty result (codex review fill 2026-05-09)

| ID | Tên | Type | Priority | Tài khoản | Steps | Expected | SRS ref | Notes |
|----|-----|------|----------|-----------|-------|----------|---------|-------|
| TC-TVCS-TK-020 | INF-TVCS-TK-01: Tìm kiếm không có kết quả → message INFO nguyên văn | Negative (info) | P1 | cb_nv_tw_01 | **Pre:** seed scope đơn vị TW có ≥10 TVCS nhưng không có record nào chứa keyword test. **Steps:** 1) Login cb_nv_tw_01. 2) URL `/tv-chuyen-sau/danh-sach`. 3) Filter tu_khoa=`zxywvut-noresult-xyz-${random}` (chuỗi unique không match). 4) Click [Tìm kiếm]. 5) `list_network_requests` verify GET `/api/v1/tu-van-chuyen-sau?q=...` response. 6) `take_snapshot` quan sát empty state UI. | Bước 5: HTTP 200 OK với body `{data: [], total_count: 0}` (read-only success — không phải error). Bước 6: UI empty state hiển thị message **nguyên văn line 391**: "**Không tìm thấy nội dung tư vấn phù hợp**" (INF-TVCS-TK-01). KHÔNG có error icon (chỉ INFO badge / icon thông tin). KHÔNG có nút "Thêm yêu cầu TV" trong empty state này (khác với empty state line 1081 khi chưa có record nào). | srs-fr-12 line 391 (INF-TVCS-TK-01 nguyên văn "Không tìm thấy nội dung tư vấn phù hợp") + line 1081 (empty state) | Codex review fill 2026-05-09. Phân biệt với line 1081 (empty state khi tab chưa có record nào): INF-TVCS-TK-01 là feedback search không khớp, line 1081 là feedback list rỗng. SPEC-CLARIFY-TVCS-TK-04 nếu UI gộp 2 empty state thành 1. |

---

**Tổng số TC: 20**
