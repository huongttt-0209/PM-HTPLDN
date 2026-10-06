# Test Case — Permission Matrix Cross-FR-13 (BR-AUTH-01/05/08)

> **File:** `06-TC-permission-matrix.md`
> **Scope:** Cross-cutting BR-AUTH cho Kho Q&A (FR-X.2-01) + Phiên TVN (FR-X.2-02) + Công khai (FR-X.2-06)
> **SRS Reference:** [`srs-fr-13-tv-nhanh-v3.1.md`](../../../input/srs-v3/srs-fr-13-tv-nhanh-v3.1.md) §6 BR-AUTH-01 line 853-862, [`output/permission-matrix.md`](../../permission-matrix.md)
> **Loại:** B (verify UI hidden + API 403/404)

## TC Index

| TC ID | Tên TC | Trace | Tag | Role |
|-------|--------|-------|-----|------|
| TC-PERM-001 | QTHT chỉ READ Kho + phiên TVN, không CRUD | BR-AUTH-01 + Permission Matrix | Negative | qtht_01 |
| TC-PERM-002 | TVV/CG/NHT 403 module FR-13 | Permission Matrix | Negative | tvv_01, cg_01, nht_01 |
| TC-PERM-003 | DN không truy cập CMS FR-13 (chỉ chuyên trang) | Permission Matrix | Negative | dn_01 |
| TC-PERM-004 | CB_NV_DP cross-tenant: DP-AG đọc/sửa Kho của DP-BG → 404 | BR-AUTH-08 | Negative | cb_nv_dp_02 |
| TC-PERM-005 | CB_PD_TW phê duyệt Kho cấp ĐP → block | BR-AUTH-05 | Negative | cb_pd_tw_01 |
| TC-PERM-006 | CB_PD_DP phê duyệt Kho cấp TW → block | BR-AUTH-05 | Negative | cb_pd_dp_01 |

---

## Test Cases

### TC-PERM-001 — QTHT chỉ READ Kho + phiên TVN, không CRUD

**Precondition:** Login `qtht_01`.

**Steps:**
1. Mở SCR-X2-01 Kho câu hỏi.
2. Quan sát nút action.
3. Mở SCR-X2-03 phiên TVN.

**Expected:**
- SCR-X2-01: Hiển thị toàn HT (tất cả đơn vị) nhưng các nút [+ Thêm] / [Nhập Excel] / [Sửa] / [Xóa] / [Duyệt] / [Công khai] đều DISABLED hoặc ẨN.
- SCR-X2-03: Hiển thị toàn HT phiên TVN nhưng nút [Trả lời] / [Gửi trả lời] DISABLED.
- API thử CREATE/UPDATE/DELETE → 403 ERR-AUTH-01.

---

### TC-PERM-002 — TVV/CG/NHT 403 module FR-13

**Steps:**
1. Login `tvv_01`. Truy cập `/tu-van/kho-cau-hoi`.
2. Login `cg_01`. Tương tự.
3. Login `nht_01`. Tương tự.

**Expected:**
- Sidebar KHÔNG hiển thị mục "Tư vấn → Kho câu hỏi" và "Tư vấn → Tư vấn Nhanh".
- Truy cập trực tiếp URL → 403 hoặc redirect về dashboard với toast "Không có quyền truy cập".
- API `GET /api/v1/kho-cau-hoi` → 403.

---

### TC-PERM-003 — DN không truy cập CMS FR-13

**Steps:**
1. Login `dn_01` (qua SSO VNeID nếu có) hoặc verify routing CMS với DN account.
2. Truy cập `/tu-van/kho-cau-hoi`.

**Expected:**
- 403 / redirect.
- DN chỉ truy cập chuyên trang Cổng PLQG, KHÔNG vào CMS.

---

### TC-PERM-004 — CB_NV_DP cross-tenant DP-AG ↔ DP-BG

**Trace:** BR-AUTH-08
**Precondition:**
- `cb_nv_dp_01` (Sở TP AG) tạo Q&A QA-AG (CHO_DUYET).
- Phiên TVN PHIEN-AG có scope AG.

**Steps:**
1. Login `cb_nv_dp_02` (Sở TP BG).
2. Mở Kho Q&A → quan sát list.
3. Truy cập trực tiếp `/tu-van/kho-cau-hoi/{QA-AG.id}/edit`.
4. API `PATCH /api/v1/kho-cau-hoi/{QA-AG.id}`.
5. Mở phiên TVN → quan sát.
6. Truy cập trực tiếp `/tu-van/tu-van-nhanh/{PHIEN-AG.id}`.

**Expected:**
- List Kho: KHÔNG thấy QA-AG (scope đơn vị BG).
- Edit URL: 404 (IDOR block) hoặc 403.
- API PATCH: 404/403.
- List phiên TVN: KHÔNG thấy PHIEN-AG.
- URL trực tiếp: 404.

---

### TC-PERM-005 — CB_PD_TW phê duyệt Kho cấp ĐP → block

**Trace:** BR-AUTH-05
**Precondition:** QA-DP (cấp ĐP, CHO_DUYET) tạo bởi cb_nv_dp_01.

**Steps:**
1. Login `cb_pd_tw_01`.
2. Mở Kho Q&A tab "Chờ duyệt".
3. Quan sát có thấy QA-DP không.

**Expected:**
- Tùy implementation:
  - **Option A (BR-AUTH-05 strict):** QA-DP KHÔNG hiển thị cho cb_pd_tw_01 (do BR-AUTH-05 phê duyệt cùng cấp).
  - **Option B (BR-AUTH-08 scope đơn vị):** Hiển thị nhưng nút [Duyệt] disabled hoặc API reject.
- API `POST /api/v1/kho-cau-hoi/{QA-DP.id}/approve` (cb_pd_tw_01) → 403 với code ERR-PD-01 hoặc tương tự.
- **SPEC-CLARIFY-TVN-05:** SRS không khai báo error code cụ thể cho cross-cấp phê duyệt Kho. Cần BA xác nhận: Option A (ẩn) hay Option B (hiển thị + block).

---

### TC-PERM-006 — CB_PD_DP phê duyệt Kho cấp TW → block

**Trace:** BR-AUTH-05
**Precondition:** QA-TW (cấp TW, CHO_DUYET) tạo bởi cb_nv_tw_01.

**Steps:**
1. Login `cb_pd_dp_01` (Sở TP AG).
2. Mở tab "Chờ duyệt".

**Expected:** QA-TW KHÔNG hiển thị (BR-AUTH-08 scope đơn vị + BR-AUTH-05 cùng cấp).

---

**Tổng số TC:** 6 TC (0 Happy + 6 Negative cross-permission)

*Generated 2026-05-10 — Phase A step A3 (bmad-qa-generate-e2e-tests)*
