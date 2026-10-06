# Test Cases — Tab Lịch sử Hỗ trợ (SCR-V.III-02 Tab 3)

> **SRS Ref**: FR-V.III-01 Processing "Xem lịch sử hỗ trợ" (`srs-fr-07-doanh-nghiep-v3.1.md:146-152`), SCR-V.III-02 Tab 3 (`srs-fr-07-doanh-nghiep-v3.1.md:348` + `:382` Quy tắc tương tác), Entity DOANH_NGHIEP counter `tong_so_vu_viec` + `tong_chi_phi_ho_tro` (srs-v3.5:1604-1605)
> **Nguồn**: NotebookLM `4dd0675e-a4fa-4ea6-80ae-48e76b3fa264` + LOCAL
> **Ngày tạo**: 2026-05-09
> **Note**: Tab 3 readonly — chỉ hiển thị **3 KPI + danh sách VV liên kết**. Cross-FR-05 (VU_VIEC).

---

## A. UI FIELD VERIFICATION

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|---------|---------------|----------------|-----------|--------------------|-------------------|------|
| TC-LS-UI-01 | SCR-V.III-02 Tab 3 / 3 KPI cards | Verify 3 KPI cards hiển thị | qtht_01, DN-TW-001 có 5 VV (3 HOAN_THANH + 2 DANG_XU_LY), tổng chi phí 100M | URL `/doanh-nghiep/DN-TW-001` Tab 3 | 1. Click Tab 3 | **3 KPI** (per srs:382 "Tab Lịch sử Hỗ trợ hiển thị 3 KPI: Tổng VV, VV hoàn thành, Tổng chi phí"): (1) Tổng VV: 5, (2) VV hoàn thành: 3, (3) Tổng chi phí: 100.000.000 VND format | Happy 🔴 |
| TC-LS-UI-02 | SCR-V.III-02 Tab 3 / DS VV table | Verify table VV liên kết | qtht_01, DN-001 có 5 VV | — | 1. Tab 3<br>2. Verify table cấu trúc | **TABLE COLUMNS** (cross-ref FR-05 SCR-V.I-01): Mã VV (VV-{TINH}-{SEQ}), Tiêu đề, Trạng thái (badge SM-VV), Ngày tạo, Chi phí; KHÔNG có cột Hành động (readonly Tab) | Happy 🔴 |
| TC-LS-UI-03 | SCR-V.III-02 Tab 3 / Click VV → mở chi tiết VV | Click mã VV → navigate sang FR-05 chi tiết VV | qtht_01, VV-TW-001 thuộc DN-TW-001 | — | 1. Click mã VV | URL chuyển `/vu-viec/{vv-id}` (cross-FR-05); KHÔNG mở modal trong Tab | Happy 🟡 |

## B. KPI ACCURACY (counter sync)

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|---------|---------------|----------------|-----------|--------------------|-------------------|------|
| TC-LS-001 | FR-V.III-01 / Tổng VV count | Tổng VV = COUNT(vv WHERE doanh_nghiep_id = DN AND is_deleted=0) | qtht_01, DN-TW-001 có 5 VV active + 1 VV soft-deleted | — | 1. Tab 3<br>2. Verify KPI 1 | KPI 1 = 5 (KHÔNG đếm VV is_deleted=1) | Happy 🔴 |
| TC-LS-002 | FR-V.III-01 / VV hoàn thành count | VV hoàn thành = COUNT(state=HOAN_THANH) | qtht_01, DN-001: 3 HOAN_THANH + 2 DANG_XU_LY | — | 1. Verify KPI 2 | KPI 2 = 3 | Happy 🔴 |
| TC-LS-003 | FR-V.III-01 / Tổng chi phí SUM | Tổng chi phí = SUM(chi_phi) all VV | qtht_01, DN-001: VV1 30M + VV2 50M + VV3 20M | — | 1. Verify KPI 3 | KPI 3 = 100.000.000 VND format `100.000.000` (dấu chấm phân cách per FR-V.III-01 Output line 184) | Happy 🔴 |
| TC-LS-004 | FR-V.III-01 / DN không có VV | DN mới chưa có VV → KPI = 0 | qtht_01, DN-TW-099 mới chưa có VV | — | 1. Tab 3 | 3 KPI = 0 / 0 / 0 VND; Empty state "Chưa có vụ việc nào" | Happy 🟡 |
| TC-LS-005 | FR-V.III-01 / Counter sync | Counter `tong_so_vu_viec` đồng bộ sau create VV mới | cb_nv_tw_01, DN-001 hiện có 5 VV | tạo VV mới qua FR-05 | 1. Tạo VV mới cho DN-001<br>2. Quay lại Tab 3 | KPI 1 = 6 (sync materialized view hoặc trigger per srs-v3.5:1618); SPEC-CLARIFY-DN-15 nếu counter lệch | Happy 🟡 |
| TC-LS-006 | FR-V.III-01 / Counter sync delete VV | Counter giảm sau soft-delete VV | cb_nv_tw_01, DN-001 6 VV | xóa VV qua FR-05 | 1. Soft-delete 1 VV<br>2. Tab 3 | KPI 1 = 5; SPEC-CLARIFY-DN-15 | Happy 🟡 |

## C. VV LIST PAGINATION

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|---------|---------------|----------------|-----------|--------------------|-------------------|------|
| TC-LS-101 | BR-DATA-07 / Default 20/page | Pagination default | qtht_01, DN có 25 VV | — | 1. Tab 3<br>2. Verify | Table 20 row; pagination "1 / 2" | Happy 🟡 |
| TC-LS-102 | BR-DATA-07 / Sort default ngày | Sort default updated_at DESC | qtht_01, DN có VV ngày khác nhau | — | 1. Verify sort | VV mới nhất ở đầu | Happy 🟡 |
| TC-LS-103 | FR-V.III-01 / KHÔNG ảnh hưởng cross-DN | DN-001 Tab 3 không hiển thị VV của DN-002 | qtht_01, DN-001 5 VV + DN-002 3 VV | — | 1. Tab 3 DN-001<br>2. Tab 3 DN-002 | DN-001 chỉ thấy 5; DN-002 chỉ thấy 3; KHÔNG cross-leak | Happy 🔴 |

## D. PERMISSION TAB

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|---------|---------------|----------------|-----------|--------------------|-------------------|------|
| TC-LS-201 | BR-AUTH-08 / Tab 3 cb_nv scope | cb_nv_tw_01 xem Tab 3 đầy đủ DN-TW | cb_nv_tw_01, DN-TW-001 có 5 VV | — | 1. Tab 3 | KPI + DS VV đầy đủ; có thể click VV → mở chi tiết | Happy 🟡 |
| TC-LS-202 | BR-AUTH-08 / cb_pd readonly | cb_pd_tw_01 xem Tab 3 readonly | cb_pd_tw_01, DN-TW-001 | — | 1. Tab 3 | Hiển thị readonly; KHÔNG có nút action | Happy 🟡 |
| TC-LS-203 | BR-AUTH-08 / cb_nv_dp_HN không xem DN-HP Tab 3 | Cross-tenant block | cb_nv_dp_HN_01 | URL `/doanh-nghiep/DN-HP-001` | 1. Tamper URL Tab 3 | API 403 hoặc redirect; KHÔNG hiển thị KPI/DS | Negative 🔴 |

---

## E. EDGE bổ sung (A4 inline merge — 5 edge)

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|---------|---------------|----------------|-----------|--------------------|-------------------|------|
| TC-LS-301 | EDGE-A4-w / VV chi_phi NULL | KPI tổng chi phí khi VV.chi_phi=NULL | qtht_01, DN-001 5 VV: 3 có chi_phi (10M+20M+5M) + 2 NULL | — | 1. Tab 3<br>2. Verify KPI 3 | KPI 3 = 35.000.000 (NULL → 0 trong SUM); KHÔNG NaN/error | Edge 🟡 |
| TC-LS-302 | EDGE-A4-x / Performance 1000 VV | DN có 1000 VV → KPI sum + pagination performance | qtht_01, DN-001 1000 VV (large data) | — | 1. Tab 3 | Render <3s; KPI sum chính xác; pagination 20/page; SPEC-CLARIFY-DN-35 nếu SRS không có SLA performance | Edge 🟡 |
| TC-LS-303 | EDGE-A4-y / VV soft-deleted KHÔNG đếm | VV is_deleted=1 KHÔNG vào KPI | qtht_01, DN có 5 active + 1 soft-deleted | — | 1. Tab 3<br>2. Verify KPI 1 | KPI 1 = 5; row 6 (soft-deleted) KHÔNG hiển thị + KHÔNG đếm | Edge 🔴 |
| TC-LS-304 | EDGE-A4-z / Counter desync stress (A7 SỬA UI bridge) | Stress test counter sync: tạo 10 VV mới qua FR-05, mỗi lần verify KPI 1 tăng đúng +1 | cb_nv_tw_01, DN-001 hiện 5 VV | — | 1. Tab 3 → KPI 1 = 5<br>2. Tạo VV mới qua FR-05 (cross-module)<br>3. Quay Tab 3 → KPI 1 = 6<br>4. Lặp 10 lần | Sau 10 vòng KPI 1 = 15; sync materialized view/trigger PASS; nếu lệch → SPEC-CLARIFY-DN-36 (recover policy) | Edge 🟡 |
| TC-LS-305 | EDGE-A4-aa / Click VV soft-deleted | Click row VV nhưng VV đã soft-deleted giữa Tab 3 và click | qtht_01, race: VV-005 vừa bị xóa | — | 1. Tab 3 hiển thị 5 VV<br>2. User khác xóa VV-005<br>3. Click VV-005 | API 404 hoặc redirect; UI toast "Vụ việc không còn tồn tại" | Edge 🟡 |

---

**Tổng số TC**: 19 (3 UI + 6 KPI + 3 Pagination + 3 Permission + 5 Edge A4)
