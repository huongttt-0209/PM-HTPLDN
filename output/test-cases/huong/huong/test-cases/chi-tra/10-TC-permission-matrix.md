# TC — Permission Matrix Cross-FR-V.II Chi trả

> **Cross-FR ref**: BR-AUTH-01 + BR-AUTH-05 (cùng cấp) + BR-AUTH-08 (scope đơn vị) | **SRS**: srs-fr-06:1376-1386
> **Roles**: All (QTHT, CB_NV TW/BN/DP, CB_PD TW/BN/DP, TVV, DN)
> **Mục tiêu**: Verify ma trận quyền — đúng role thấy/làm được, sai role/sai cấp/sai đơn vị bị 403/404. Đặc biệt BR-AUTH-05 cùng cấp duyệt + BR-AUTH-08 scope đơn vị.

## Preconditions

- HS X TW (cb_nv_tw_01 quản lý), trạng thái CHO_PHE_DUYET → cần CB_PD_TW duyệt
- HS Y AG (cb_nv_dp_01 quản lý), CHO_PHE_DUYET → cần CB_PD_DP_01 duyệt
- HS Z BG, DA_THANH_TOAN
- HS W BNI, YEU_CAU_BO_SUNG (cho dn_03 bổ sung)

## Scenarios

| TC ID | Role / Action | Steps | Expected | BR ref | Severity |
|-------|---------------|-------|----------|--------|----------|
| TC-CT-PERM-001 | qtht_01 read DS | 1. Login qtht_01 2. Vào /chi-tra/danh-sach | Read-only toàn HT (TW + BN + DP). KHÔNG có nút "Tiếp nhận / Kiểm tra / Đánh giá / Thẩm định / Trình PD / Phê duyệt / Cập nhật TT" | BR-AUTH-08 | P1 |
| TC-CT-PERM-002 | cb_nv_tw_01 scope TW | 1. Vào /chi-tra/danh-sach | Thấy HS toàn quốc (TW + BN + DP). Có quyền tiếp nhận/kiểm tra/đánh giá/thẩm định/trình PD/cập nhật TT trên HS thuộc đơn vị TW | BR-AUTH-08 | P0 |
| TC-CT-PERM-003 | cb_nv_dp_01 scope AG | 1. Vào /chi-tra/danh-sach | CHỈ thấy HS đơn vị AG. KHÔNG thấy HS BG/BNI hay TW. Force GET /chi-tra/:id của HS BG → 403/404 | BR-AUTH-08 | P0 |
| TC-CT-PERM-004 | cb_pd_tw_01 duyệt HS X TW (CHO_PHE_DUYET) | 1. Login cb_pd_tw_01 2. Click Phê duyệt HS X | Cho phép — cùng cấp đơn vị TW | BR-AUTH-05 | P0 |
| TC-CT-PERM-005 | cb_pd_dp_01 duyệt HS X TW (CHO_PHE_DUYET) | 1. Login cb_pd_dp_01 2. Force GET /chi-tra/:id HS X | 403/404 — CB PD DP KHÔNG duyệt được HS TW (BR-AUTH-05 cùng cấp + BR-AUTH-08 scope) | BR-AUTH-05, BR-AUTH-08 | P0 |
| TC-CT-PERM-006 | cb_pd_tw_01 duyệt HS Y AG (CHO_PHE_DUYET) | 1. Login cb_pd_tw_01 2. Force GET HS Y | 403 hoặc thấy nhưng nút Phê duyệt disabled. CB PD TW KHÔNG duyệt được HS AG | BR-AUTH-05 | P0 |
| TC-CT-PERM-007 | cb_pd_dp_01 (AG) duyệt HS Y (AG) | 1. Login cb_pd_dp_01 2. Phê duyệt HS Y | Cho phép — cùng cấp đơn vị AG | BR-AUTH-05 | P0 |
| TC-CT-PERM-008 | dn_01 truy cập DS Chi trả CMS | 1. Login dn_01 2. Force /chi-tra/danh-sach (URL CMS) | 403 — DN KHÔNG có quyền vào CMS DS Chi trả. DN chỉ truy cập qua chuyên trang DN (HS của tôi) | BR-AUTH-01 (role) | P0 |
| TC-CT-PERM-009 | dn_01 xem HS dn_01 qua chuyên trang | 1. Login dn_01 chuyên trang DN 2. Vào trang HS Chi trả của tôi | Thấy DS HS gắn dn_01. KHÔNG thấy HS dn_02/dn_03 | BR-AUTH-08 (DN scope) | P0 |
| TC-CT-PERM-010 | dn_01 rút HS của dn_02 | 1. Force POST API rút HS của dn_02 | 403/404 | BR-AUTH-08 | P0 |
| TC-CT-PERM-011 | tvv_01 vào CMS Chi trả | 1. Login tvv_01 2. Force /chi-tra/danh-sach | 403 — TVV KHÔNG có quyền CMS Chi trả. TVV chỉ thấy DS Thông báo (UC75) | BR-AUTH-01 (role) | P0 |
| TC-CT-PERM-012 | tvv_01 đọc TB của tvv_02 | 1. Login tvv_01 2. Force GET /thong-bao/:id TB gắn tvv_02 | 403/404 | BR-AUTH-08 | P1 |
| TC-CT-PERM-013 | cb_nv_tw_01 force POST API kiểm tra HS X (CHO_TIEP_NHAN) chưa tiếp nhận | 1. Force POST /chi-tra/:id/kiem-tra | ERR-CT-KT-01 — HS không ở DANG_KIEM_TRA. State guard backend | ERR-CT-KT-01 | P1 |
| TC-CT-PERM-014 | dn_01 force POST kiểm tra HS X | 1. Force POST API kiểm tra (role DN) | 403 — DN KHÔNG có role kiểm tra (chỉ CB NV) | BR-AUTH-01 (role) | P0 |

## Edge bổ sung (A4 inline merge)

| TC ID | Preconditions | Steps | Expected | BR/AC ref | Severity |
|-------|---------------|-------|----------|-----------|----------|
| TC-CT-PERM-015 | login cb_nv_tw_01 → session timeout 30 phút idle | 1. Idle 31 phút 2. Click "Tiếp nhận" trên DS | Redirect login page hoặc toast "Phiên đăng nhập hết hạn" + 401. KHÔNG submit | BR-AUTH-01 (session) | P1 |
| TC-CT-PERM-016 | login dn_01, IDOR test | 1. dn_01 vào HS X (của dn_01) qua /chi-tra/:id?id=100 2. Đổi URL thành /chi-tra/:id?id=200 (HS dn_02) | 403/404 — backend validate ownership theo session, KHÔNG dựa vào URL param | BR-AUTH-08 (IDOR) | P0 |
| TC-CT-PERM-017 | login cb_pd_dp_01 (AG) — HS X TW đang CHO_PHE_DUYET | 1. cb_pd_dp_01 force POST /api/chi-tra/:id/duyet HS X | 403 — BR-AUTH-05 cùng cấp đơn vị. Backend validate `cb_pd.don_vi_id == hs.don_vi_id` (srs-fr-06:734) | BR-AUTH-05, srs-fr-06:734 | P0 |
| TC-CT-PERM-018 | dn_01 force POST /api/chi-tra/:id/bo-sung của dn_02 | 1. dn_01 inspect /chi-tra/:id của dn_02 2. Force POST bổ sung | 403 — backend validate DN ownership. `ho_so.doanh_nghiep_id != current_dn.id` → reject | BR-AUTH-08 (DN scope) | P0 |

## Tổng số TC: 18 (sau A4: +4 edge)

**P0: 14** | P1: 4

> **A4 audit ref:** [`08-REVIEW-edge-case-hunter.md`](08-REVIEW-edge-case-hunter.md#file-10)
