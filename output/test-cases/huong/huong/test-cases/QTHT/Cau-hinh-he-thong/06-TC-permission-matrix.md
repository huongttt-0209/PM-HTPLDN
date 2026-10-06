# Test Cases — Permission Matrix Cross-cutting (BR-AUTH-01 + BR-AUTH-08 + Mô hình B Hybrid)

> **SRS Ref**: SCR-VIII-06 tab gating (srs-fr-10:1681-1689), Mô hình B exception (srs-v3.md §3.4.2 MAU_PHAN_HOI), BR-AUTH-01/08 Phụ lục B
> **Ngày tạo**: 2026-05-08 (BMAD A3, A4 inline merge)
> **Pattern reference**: `output/test-cases/QTHT/Nhat-ky-he-thong/03-TC-permission-matrix.md`
> **URL:** `/quan-tri/cau-hinh`

> **Iron rule:**
> - Tab 1 (SLA), Tab 2 (Phân công), Tab 4 (Quy trình): chỉ QTHT.
> - Tab 3 (Mẫu phản hồi): QTHT (READ) + CB_NV_{TW/BN/DP} (CRUD scope) + CB_PD_{cap} (READ scope).
> - DN/CG/TVV/NHT (Tier 2) KHÔNG truy cập SCR-VIII-06.

---

## A. TAB GATING per role

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước | Kết quả mong đợi | Type | Priority |
|----|---------|---------------|----------------|-----------|----------|------------------|------|----------|
| TC-CH-PERM-001 | line 1685 (sync CAUHINH-01 — Tab 2 deprecated) | QTHT thấy 3 tab functional + Tab 2 ẨN/banner | `qtht_01`. | — | 1. Vào /quan-tri/cau-hinh. 2. Quan sát tab list. | **UI**: 2 behavior PASS theo CAUHINH-01 RESOLVED (FR-II-NEW-01 đã bỏ Q11): (a) Tab list hiển thị **3 tab functional** "Thời hạn xử lý / SLA", "Mẫu phản hồi", "Quy trình hỗ trợ" — Tab 2 ẨN hoàn toàn; (b) Tab list 4 tab nhưng Tab 2 "Phân công mặc định" disabled + deprecation banner "Tính năng đã bỏ". Tab 1 (SLA) active mặc định. **Behavior FAIL = render bảng CRUD Tab 2 cũ** = BUG implementation chưa update theo BA Q11. | Happy | P0 |
| TC-CH-PERM-002 | line 1686 | CB_NV_TW chỉ thấy Tab 3 | `cb_nv_tw_01`. | — | 1. Vào URL. | **UI**: Tab list **chỉ Tab 3** "Mẫu phản hồi" (mặc định active). KHÔNG có Tab 1, 2, 4. **PERSIST**: Verify URL `?tab=1` bị reject hoặc redirect. | Happy | P0 |
| TC-CH-PERM-003 | line 1687 | CB_NV_BN chỉ thấy Tab 3 | `cb_nv_bn_01` (Bộ TC). | — | Tương tự. | **UI**: Tab list chỉ Tab 3. | Happy | P0 |
| TC-CH-PERM-004 | line 1688 | CB_NV_DP chỉ thấy Tab 3 | `cb_nv_dp_01` (Sở HN). | — | Tương tự. | **UI**: Tab list chỉ Tab 3. | Happy | P0 |
| TC-CH-PERM-005 | line 1689 | CB_PD_TW chỉ thấy Tab 3 (READ-only, không có nút CRUD) | `cb_pd_tw_01`. | — | 1. Vào URL. 2. Quan sát Tab 3. | **UI**: Tab list chỉ Tab 3. Trong Tab 3: KHÔNG có nút [+ Thêm mẫu phản hồi]. KHÔNG có cột Hành động Sửa/Xóa per-row. Chỉ có 👁 Xem. | Happy | P0 |
| TC-CH-PERM-006 | line 1689 | CB_PD_BN chỉ thấy Tab 3 READ scope BN | `cb_pd_bn_01`. | — | Tương tự, scope BN. | **UI**: Bảng Tab 3 chỉ TW + BN cấp mình. KHÔNG có nút CRUD. | Happy | P1 |
| TC-CH-PERM-007 | line 1689 | CB_PD_DP chỉ thấy Tab 3 READ scope DP | `cb_pd_dp_01`. | — | Tương tự, scope DP. | **UI**: Bảng Tab 3 chỉ TW + DP cấp mình. | Happy | P1 |

---

## B. CROSS-DON_VI ISOLATION (Tab 3 — Mô hình B Hybrid)

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước | Kết quả mong đợi | Type | Priority |
|----|---------|---------------|----------------|-----------|----------|------------------|------|----------|
| TC-CH-PERM-010 | BR-AUTH-08 ngoại lệ + line 1662 | BN A (Bộ TC) KHÔNG thấy mẫu BN B (Bộ KH&ĐT) | `cb_nv_bn_01` (Bộ TC). Seed mẫu BN của Bộ KH&ĐT id=`mph-bn-bkhdt-001`. | — | 1. Tab 3. 2. Search "Bộ KH". | **STATE**: BE filter `WHERE pham_vi=BN_RIENG AND don_vi_id=BoTC.id`. **UI**: Bảng KHÔNG có mẫu Bộ KH&ĐT. URL direct edit `mph-bn-bkhdt-001` → 403/404 (ERR-MPH-06). **PERSIST**: — | Negative | P0 |
| TC-CH-PERM-011 | BR-AUTH-08 ngoại lệ | DP A (Sở HN) KHÔNG thấy mẫu DP B (Sở HCM) | `cb_nv_dp_01` (Sở HN). | — | Tương tự. | **STATE/UI**: Bảng filter scope. URL direct → 403. | Negative | P0 |
| TC-CH-PERM-012 | line 1689 | CB_PD_BN (Bộ TC) KHÔNG thấy mẫu BN khác (cùng cấp khác BN) | `cb_pd_bn_01`. Mẫu BN Bộ KH&ĐT. | — | 1. Tab 3 quan sát. | **UI**: Chỉ TW + Bộ TC. KHÔNG Bộ KH&ĐT. | Negative | P1 |

---

## C. NON-MEMBER ACCESS BLOCK

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước | Kết quả mong đợi | Type | Priority |
|----|---------|---------------|----------------|-----------|----------|------------------|------|----------|
| TC-CH-PERM-020 | BR-AUTH-01 Tier 2 | DN không truy cập SCR-VIII-06 | `dn_01`. | — | 1. URL direct CMS `/quan-tri/cau-hinh`. | **STATE**: BE reject Tier 2. **UI**: Redirect Cổng PLQG hoặc 403. | Negative | P0 |
| TC-CH-PERM-021 | BR-AUTH-01 Tier 2 | TVV/CG/NHT không truy cập | `tvv_01`, `cg_01`, `nht_01` (3 lượt). | — | URL direct. | 3 lượt: 403/redirect. | Negative | P0 |

---

## D. ELEMENT GATING (line 1690-1693)

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước | Kết quả mong đợi | Type | Priority |
|----|---------|---------------|----------------|-----------|----------|------------------|------|----------|
| TC-CH-PERM-030 | line 1691 | QTHT — nút [+ Thêm mẫu] disabled với tooltip | `qtht_01`. | — | 1. Tab 3. 2. Hover nút. | **UI**: Nút disabled (greyed). Tooltip giải thích "QTHT chỉ READ, không tạo mẫu." | Happy | P1 |
| TC-CH-PERM-031 | line 1691 | CB_PD — nút [+ Thêm mẫu] disabled | `cb_pd_tw_01`. | — | Tương tự. | **UI**: Nút disabled. | Happy | P1 |
| TC-CH-PERM-032 | line 1692 | CB_NV_BN — Sửa/Xóa chỉ với mẫu cùng don_vi_id | `cb_nv_bn_01` (Bộ TC). | — | 1. Tab 3. 2. Quan sát hành động per row trên mẫu Bộ TC vs mẫu TW. | **UI**: Mẫu Bộ TC: có nút ✏️🗑. Mẫu TW: chỉ có 👁 (BN không sở hữu). | Happy | P0 |
| TC-CH-PERM-033 | line 1693 + AC | Field "Phạm vi áp dụng" trong modal create — read-only auto-fill | `cb_nv_dp_01`. | — | 1. Click [+ Thêm mẫu]. 2. Quan sát field "Phạm vi". | **UI**: Field hiển thị 🟨 "Địa phương Sở TP HN" + tooltip *"Phạm vi tự gán theo cấp đơn vị bạn (DP). Không thể thay đổi sau khi tạo."*. KHÔNG cho input/click. | Happy | P0 |

---

## E. EDGE — IDOR + DIRECT API

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước | Kết quả mong đợi | Type | Priority |
|----|---------|---------------|----------------|-----------|----------|------------------|------|----------|
| TC-CH-PERM-040 | A4 IDOR (A4 merged) | CB_NV_TW gọi API SLA direct với JWT của mình | `cb_nv_tw_01`. | PATCH `/api/cau-hinh-sla/{id}` | 1. Devtools console: PATCH với JWT TW. | **STATE**: BE check role QTHT only → reject 403. **UI**: HTTP 403. **PERSIST**: SLA không đổi. | Negative | P0 |
| TC-CH-PERM-041 | A4 IDOR (A4 merged) | CB_NV_DP gọi API CRUD ngày lễ direct | `cb_nv_dp_01`. | POST `/api/ngay-le` | 1. Devtools: POST. | **STATE**: BE 403 (ERR-NL-01). **UI**: 403. | Negative | P0 |
| TC-CH-PERM-042 | A4 cross-cấp BE direct (A4 merged) | CB_NV_BN bypass UI — POST mẫu pham_vi=DP_RIENG | `cb_nv_bn_01`. | API payload pham_vi=DP_RIENG | 1. Devtools console: POST với pham_vi=DP_RIENG. | **STATE**: BE check MPH_CREATE_DP (BN cấp không có) → reject 403 (ERR-MPH-04 hoặc tương đương). **UI**: 403. **PERSIST**: KHÔNG insert. | Negative | P0 |
| TC-CH-PERM-043 | A4 token expire (A4 merged) | JWT expired — toàn bộ tab bị block | `qtht_01`. JWT đã expire (manual override). | — | 1. Modify token. 2. Refresh trang. | **STATE**: BE 401 Unauthorized. **UI**: Redirect login page. | Edge | P1 |

---

## Tổng số TC: 19 (7 Tab gating + 3 Cross-don_vi + 2 Non-member + 4 Element gating + 4 IDOR/Edge) — A3 base 15 + A4 merged 4
**Priority**: P0=14 / P1=5 / P2=0

**Coverage:**
- BR: BR-AUTH-01 (mọi TC), BR-AUTH-08 (TC-010-012 — Mô hình B exception), Mô hình B Hybrid full coverage
- Roles tested: QTHT (full + element disabled), CB_NV_TW/BN/DP (Tab 3 only), CB_PD_TW/BN/DP (Tab 3 read-only), Tier 2 (DN/CG/TVV/NHT — block toàn bộ)
- A4 merged 2026-05-08: TC-040 (IDOR SLA), TC-041 (IDOR ngày lễ), TC-042 (cross-cấp BE direct), TC-043 (token expire)
- Cross-references: 03-TC-tab-mau-phan-hoi.md TC-033, TC-036 cho ERR-MPH-04, ERR-MPH-06 detailed

---

## Note A7 — UI/function-testable

TC-040..042 dùng `evaluate_script` qua devtools console của browser đã login user tương ứng (UI bridge hợp lệ — pattern từ W1.1 Nhật ký HT). KHÔNG curl/Postman thuần.
