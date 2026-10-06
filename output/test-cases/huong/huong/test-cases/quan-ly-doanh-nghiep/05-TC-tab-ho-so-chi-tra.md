# Test Cases — Tab Hồ sơ Chi trả (SCR-V.III-02 Tab 4)

> **SRS Ref**: SCR-V.III-02 Tab 4 (`srs-fr-07-doanh-nghiep-v3.1.md:349` + `:383` Quy tắc tương tác), Cross-FR-06 (HO_SO_CHI_TRA entity), Permission Matrix HO_SO_CHI_TRA dòng srs-v3.5:1259
> **Nguồn**: NotebookLM `4dd0675e-a4fa-4ea6-80ae-48e76b3fa264` + LOCAL
> **Ngày tạo**: 2026-05-09
> **Note**: Tab 4 readonly — chỉ hiển thị **danh sách HS chi trả liên kết**. Cross-FR-06 (Chi trả). Mỗi DN có nhiều HS chi trả thông qua VV.

---

## A. UI FIELD VERIFICATION

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|---------|---------------|----------------|-----------|--------------------|-------------------|------|
| TC-CT-UI-01 | SCR-V.III-02 Tab 4 / Table HSCT | Verify table HS chi trả Tab 4 | qtht_01, DN-TW-001 có 3 HSCT (DA_DUYET, DANG_XU_LY, YC_BO_SUNG) | URL `/doanh-nghiep/DN-TW-001` Tab 4 | 1. Click Tab 4<br>2. Verify cấu trúc | **TABLE COLUMNS** (cross-ref FR-06): Mã HS chi trả (HSCT-{YYYYMMDD}-{SEQ}), Mã VV liên kết, Số tiền chi trả (VND format), Trạng thái (badge SM-HSCT), Ngày tạo, Ngày cập nhật; KHÔNG có cột Hành động (readonly Tab) | Happy 🔴 |
| TC-CT-UI-02 | SCR-V.III-02 Tab 4 / Empty state | DN không có HSCT → empty state | qtht_01, DN-TW-099 chưa có HSCT | — | 1. Tab 4 | Empty state "Chưa có hồ sơ chi trả nào liên kết" hoặc tương đương; SPEC-CLARIFY-DN-16 nếu SRS không define text | Happy 🟡 |
| TC-CT-UI-03 | SCR-V.III-02 Tab 4 / Click HSCT navigate FR-06 | Click row → mở chi tiết HSCT (cross-FR-06) | qtht_01, HSCT-001 thuộc DN-TW-001 | — | 1. Click mã HSCT | URL chuyển sang FR-06 chi tiết HSCT (vd `/chi-tra/{id}` hoặc `/ho-so-chi-tra/{id}`); SPEC-CLARIFY-DN-17 nếu route chưa có | Happy 🟡 |

## B. DS HSCT LIÊN KẾT

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|---------|---------------|----------------|-----------|--------------------|-------------------|------|
| TC-CT-001 | SCR-V.III-02 Tab 4 / Linked correctly | HSCT chỉ thuộc DN của Tab | qtht_01, DN-001 3 HSCT, DN-002 2 HSCT | — | 1. Tab 4 DN-001<br>2. Tab 4 DN-002 | DN-001: 3 row; DN-002: 2 row; KHÔNG cross-DN leak | Happy 🔴 |
| TC-CT-002 | SCR-V.III-02 Tab 4 / All states displayed | Hiển thị HSCT mọi state SM-HSCT | qtht_01, DN có HSCT các state: KHOI_TAO, CHO_PD, DA_DUYET, YC_BO_SUNG | — | 1. Tab 4 | Tất cả 4 HSCT hiển thị với badge state đúng; KHÔNG filter mặc định | Happy 🟡 |
| TC-CT-003 | SCR-V.III-02 Tab 4 / Pagination | HSCT >20 → phân trang | qtht_01, DN có 25 HSCT | — | 1. Tab 4 | Default 20/page; click trang 2 | Happy 🟡 |
| TC-CT-004 | SCR-V.III-02 Tab 4 / Sort default | Sort updated_at DESC | qtht_01 | — | 1. Verify | HSCT mới nhất đầu | Happy 🟡 |

## C. ROLLUP / TOTAL (nếu có — SPEC-CLARIFY)

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|---------|---------------|----------------|-----------|--------------------|-------------------|------|
| TC-CT-101 | SPEC-CLARIFY-DN-18 / Total chi phí Tab 4 | Tab 4 có dòng tổng SUM chi phí HSCT? | qtht_01, DN-001 3 HSCT: 10M + 20M + 5M | — | 1. Tab 4<br>2. Tìm dòng total | Pre-condition: SRS không define rõ — SPEC-CLARIFY: hiển thị 1 dòng SUM cuối table = 35M? Hoặc KHÔNG có rollup? Áp dụng "UI vs business" rule — assume KHÔNG có rollup vì spec im lặng | Happy 🟡 |

## D. PERMISSION TAB

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|---------|---------------|----------------|-----------|--------------------|-------------------|------|
| TC-CT-201 | BR-AUTH-08 / cb_nv scope | cb_nv_tw_01 xem Tab 4 đầy đủ DN-TW | cb_nv_tw_01, DN-TW-001 | — | 1. Tab 4 | DS HSCT đầy đủ | Happy 🟡 |
| TC-CT-202 | BR-AUTH-08 / cb_pd readonly | cb_pd_tw_01 xem Tab 4 | cb_pd_tw_01 | — | 1. Tab 4 | Hiển thị readonly; KHÔNG action | Happy 🟡 |
| TC-CT-203 | Permission Matrix / TVV access HSCT R* | tvv_01 truy cập DN không qua CMS | tvv_01 (chuyên trang) | — | 1. tvv_01 cố mở SCR-V.III-02 | TVV không có sidebar DN trên CMS (per Permission Matrix); chỉ có chuyên trang riêng | Negative 🟡 |
| TC-CT-204 | BR-AUTH-08 / Cross-tenant Tab 4 | cb_nv_dp_HN_01 không xem được Tab 4 DN-HP-001 | cb_nv_dp_HN_01 | URL `/doanh-nghiep/DN-HP-001` Tab 4 | 1. Tamper URL | API 403 hoặc redirect | Negative 🔴 |

## E. CROSS-FR-06 INTEGRATION

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|---------|---------------|----------------|-----------|--------------------|-------------------|------|
| TC-CT-301 | Cross-FR-06 / HSCT created sync | Tạo HSCT mới qua FR-06 → reload Tab 4 thấy | cb_nv_tw_01, DN-001 hiện có 3 HSCT | tạo HSCT-MOI qua FR-06 | 1. Tạo HSCT cho VV thuộc DN-001 (cross-FR-06)<br>2. Quay lại Tab 4 | DS Tab 4 có thêm HSCT-MOI; pagination total +1 | Happy 🟡 |
| TC-CT-302 | Cross-FR-06 / Soft delete HSCT | HSCT soft-deleted → ẩn khỏi Tab 4 | cb_nv_tw_01, HSCT-001 | xóa HSCT-001 qua FR-06 | 1. Soft delete<br>2. Tab 4 | HSCT-001 biến mất; pagination total -1 | Happy 🟡 |

---

## F. EDGE bổ sung (A4 inline merge — 4 edge)

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|---------|---------------|----------------|-----------|--------------------|-------------------|------|
| TC-CT-401 | EDGE-A4-bb / HSCT soft-deleted | HSCT is_deleted=1 ẩn khỏi Tab 4 | qtht_01, DN có 4 HSCT (1 soft-deleted) | — | 1. Tab 4<br>2. Đếm row | Hiển thị 3 row; HSCT soft-deleted KHÔNG hiển thị (BR-DATA-01) | Edge 🔴 |
| TC-CT-402 | EDGE-A4-cc / Filter trang_thai HSCT | Tab 4 có filter trạng thái HSCT? | qtht_01 | — | 1. Tab 4<br>2. Verify | SRS không define filter trên Tab 4 → SPEC-CLARIFY-DN-37 (assume KHÔNG có filter, list mặc định all states) | Edge 🟡 |
| TC-CT-403 | EDGE-A4-dd / Performance 1000 HSCT | DN có 1000 HSCT → pagination + render | qtht_01 | — | 1. Tab 4 | Render <3s; pagination 20/page; SPEC-CLARIFY-DN-35 SLA performance | Edge 🟡 |
| TC-CT-404 | EDGE-A4-ee / VV không liên kết HSCT | VV không có HSCT → Tab 4 vẫn empty với VV đó | qtht_01, DN có 3 VV nhưng chỉ 1 VV có HSCT | — | 1. Tab 4 | Tab 4 chỉ hiển thị HSCT của 1 VV (DS HSCT, không phải DS VV); SPEC-CLARIFY-DN-38 nếu user mong VV grouping | Edge 🟡 |

---

**Tổng số TC**: 18 (3 UI + 4 DS + 1 Rollup + 4 Permission + 2 Cross-FR-06 + 4 Edge A4)
