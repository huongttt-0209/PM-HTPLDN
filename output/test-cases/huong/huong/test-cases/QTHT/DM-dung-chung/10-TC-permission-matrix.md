# Test Cases — Permission Matrix DM Dùng Chung (cross BR-AUTH-01)

> **Module:** QTHT — DM dùng chung · **FR:** Cross-cutting BR-AUTH-01 + BR-AUTH-08
> **Mục đích:** Verify SCR-VIII-01 + tất cả 13 DM trong scope (SRS gốc FR-VIII-01..09 + 11..13 + 18..19 = 14 FR; loại FR-VIII-06 CR-02 → 13 DM) chỉ truy cập được bởi QTHT. Mọi role khác → 403 ERR-AUTH-01.
> **Tài khoản test:** `_03` permission test (qtht_03 / cb_nv_tw_03 / cb_pd_bn_03 / nht_03 / dn_03 / etc.)
> **Tổng số TC:** 15 (TC-PERM-008 LOẠI R3 A7 violation)

---

## A. QTHT — happy path (positive)

| ID | Tiền điều kiện | Bước | KQ mong đợi | BR/AC ref |
|---|---|---|---|---|
| TC-PERM-001 | qtht_03 đăng nhập | Mở `/quan-tri/danh-muc` | Sidebar 13 sub-tab DM hiển thị; default tab Lĩnh vực PL active | BR-AUTH-01, line 1455 |
| TC-PERM-002 | qtht_03 đăng nhập | Click qua từng 13 sub-tab | Mỗi tab load đúng DM; toolbar [+ Thêm mới] hiển thị; cột Hành động (Sửa/Xóa) hiển thị | BR-AUTH-01 |
| TC-PERM-003 | qtht_03 ở tab "Cơ quan ĐV" | Tree view + form chi tiết render | Tree 2-tầng đầy đủ; nút [+ Thêm con] khả dụng (cho TW root) | BR-AUTH-02 |
| TC-PERM-004 | qtht_03 thực hiện CRUD bất kỳ DM | Create/Update/Delete/Toggle | All allow; audit log INSERT/UPDATE/DELETE entry | BR-DATA-05 |

---

## B. CB_NV (TW/BN/DP) — negative

| ID | Tiền điều kiện | Bước | KQ mong đợi | BR/AC ref |
|---|---|---|---|---|
| TC-PERM-005 | cb_nv_tw_03 đăng nhập | Mở URL trực tiếp `/quan-tri/danh-muc` | 403 ERR-AUTH-01 "Bạn không có quyền thực hiện chức năng này"; sidebar KHÔNG có entry "Danh mục dùng chung" | E1 line 149 |
| TC-PERM-006 | cb_nv_bn_03 đăng nhập | Direct URL `/quan-tri/danh-muc/LINH_VUC_PL` | 403 ERR-AUTH-01; redirect/error page | BR-AUTH-01 |
| TC-PERM-007 | cb_nv_dp_03 đăng nhập | Direct URL | 403 ERR-AUTH-01 | BR-AUTH-01 |
| ~~TC-PERM-008~~ | _LOẠI R3 — DevTools Console `fetch()` là API-call chủ động ngoài user UI flow, vi phạm A7. Coverage cb_nv API auth đã đảm bảo bởi TC-PERM-005..007 (cb_nv login → click sidebar / direct URL → 403). Nếu cần backend assertion, test riêng ở /api integration test layer ngoài Phase B này._ | — | — | _removed (A7 violation)_ |

---

## C. CB_PD (TW/BN/DP) — negative

| ID | Tiền điều kiện | Bước | KQ mong đợi | BR/AC ref |
|---|---|---|---|---|
| TC-PERM-009 | cb_pd_tw_03 đăng nhập | Direct URL `/quan-tri/danh-muc` | 403 ERR-AUTH-01 | BR-AUTH-01 |
| TC-PERM-010 | cb_pd_bn_03 đăng nhập | Direct URL | 403 ERR-AUTH-01 | BR-AUTH-01 |
| TC-PERM-011 | cb_pd_dp_03 đăng nhập | Direct URL | 403 ERR-AUTH-01 | BR-AUTH-01 |

---

## D. Tier 2 (NHT/TVV/CG/DN) — negative

| ID | Tiền điều kiện | Bước | KQ mong đợi | BR/AC ref |
|---|---|---|---|---|
| TC-PERM-012 | nht_03 đăng nhập (Tier 2 SSO VNeID) | Cố vào CMS `/quan-tri/danh-muc` | 403 hoặc redirect ra trang chuyên trang NHT (Tier 2 KHÔNG có entry CMS) | BR-AUTH-01 + BR-INTG-06 |
| TC-PERM-013 | tvv_03 đăng nhập | Cố vào CMS | 403 / redirect | BR-AUTH-01 |
| TC-PERM-014 | cg_03 đăng nhập | Cố vào CMS | 403 / redirect | BR-AUTH-01 |
| TC-PERM-015 | dn_03 đăng nhập | Cố vào CMS | 403 / redirect (DN chỉ có chuyên trang riêng) | BR-AUTH-01 |

---

## E. Session expired

| ID | Tiền điều kiện | Bước | KQ mong đợi | BR/AC ref |
|---|---|---|---|---|
| TC-PERM-016 | qtht_03 đăng nhập, idle 30+ phút | Bất kỳ thao tác CRUD trên DM | Redirect `/login` ERR-AUTH-02 + msg "Phiên làm việc hết hạn" | E2 line 150, BR-AUTH-06 |

---

**Tổng số TC:** 15 (TC-PERM-001..016, **TC-PERM-008 LOẠI ở R3** A7 violation)

**Coverage Matrix:**
| Action | QTHT | CB_NV | CB_PD | NHT/TVV/CG/DN |
|--------|:-:|:-:|:-:|:-:|
| LIST/Read SCR-VIII-01 | TC-PERM-001..002 ✅ | TC-PERM-005..007 ❌ | TC-PERM-009..011 ❌ | TC-PERM-012..015 ❌ |
| CRUD all DM | TC-PERM-004 ✅ | TC-PERM-005..007 ❌ (UI direct URL 403) | — | — |
| Tree UC103 | TC-PERM-003 ✅ | — | — | — |
| Session timeout | TC-PERM-016 | — | — | — |
