# Test Cases — FR-XI-07 (UC167): Trình phê duyệt BC

> **SRS Ref**: FR-XI-07, SCR-XI-01 Drill-down (action [Trình duyệt KQ]), Entity DOT_BAO_CAO + BAO_CAO_CT_HTPL
> **Ngày tạo**: 2026-05-10
> **Đặc thù**: 2 SM cùng chuyển: Đợt BC `DANG_LAP_BC → CHO_DUYET_KQ`; BC `DU_THAO → CHO_PHE_DUYET`. Side-effect: gửi thông báo CB PD cùng cấp.
> **Scope**: Hành động trình + verify 2 SM transition + thông báo. KHÔNG gồm phê duyệt (xem `04-TC-phe-duyet-bc.md`).

---

## Quy ước

- **Priority**: 🔴 P0 · 🟡 P1 · 🟢 P2
- **TraceID**: `FR-XI-07 / {section}` — truy vết SRS
- **Pre-conditions mặc định**: User đã đăng nhập, có quyền "Lập BC kết quả CT", BC đã có số liệu, đợt BC ở DANG_LAP_BC.

---

## A. Trình phê duyệt BC — HAPPY

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|---------|--------------|----------------|-----------|-------------------|------------------|------|
| TC-TPD-001 | SM-DOT-BC + SM-BC sub / DANG_LAP_BC → CHO_DUYET_KQ + DU_THAO → CHO_PHE_DUYET | Trình PD BC happy path | cb_nv_tw_01 login. Đợt DOT-CTW01-001 DANG_LAP_BC, BC DU_THAO đầy đủ số liệu. Có ≥1 cb_pd_tw_01 active. | — | 1. Drill-down. 2. Click [Trình duyệt KQ]. 3. Modal xác nhận → OK. | (2) PATCH `/api/v1/dot-bao-cao/{id}/trinh-duyet` 200. (3) Đợt BC = `CHO_DUYET_KQ` (badge vàng đậm). (3) BC = `CHO_PHE_DUYET`. (3) Thanh tiến trình SM-DOT-BC highlight CHO_DUYET_KQ. (3) MCP `list_network_requests` thấy POST `/notifications` outbound (gửi CB PD cùng cấp). Audit log INSERT 2 entry (UPDATE cả đợt và BC) với `action_type=TRANSITION` (BR-DATA-05). | Happy 🔴 |
| TC-TPD-002 | FR-XI-07 / AC#1 — sau Trình form read-only | Sau Trình PD form chuyển read-only | cb_nv_tw_01 login. Đợt DOT-CTW01-002 vừa Trình PD xong. | — | 1. Drill-down lại đợt vừa trình. | (1) Form 21a/21b **read-only**. Nút [Lưu nháp], [Trình duyệt KQ] **ẩn**. Hiển thị "Đang chờ phê duyệt" + thông tin người trình + thời điểm trình. | Happy 🟡 |
| TC-TPD-003 | FR-XI-07 / AC scope ĐP — gửi thông báo CB PD cùng cấp | Trình PD ở cấp ĐP — TB chỉ tới CB PD ĐP cùng đơn vị | cb_nv_dp_01 (Sở TP AG) login. Đợt DOT-CDP01-003 DANG_LAP_BC. Có cb_pd_dp_01 (Sở TP AG) + cb_pd_dp_02 (Sở TP BG) + cb_pd_tw_01. | — | 1. Trình PD. 2. MCP `list_network_requests` capture POST `/notifications`. | (2) Notification chỉ tới `cb_pd_dp_01` (cùng cấp ĐP + cùng đơn vị Sở TP AG). KHÔNG tới `cb_pd_dp_02` (khác đơn vị) hay `cb_pd_tw_01` (khác cấp). (Áp BR-AUTH-05 + BR-AUTH-08 cho notification scope) | Happy 🟡 |

---

## B. Trình phê duyệt BC — NEGATIVE

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|---------|--------------|----------------|-----------|-------------------|------------------|------|
| TC-TPD-010 | FR-XI-07 / E1 ERR-XI-07-01 | BC chưa hoàn chỉnh — số liệu rỗng | cb_nv_tw_01 login. Đợt DOT-CTW01-010 DANG_LAP_BC, BC `so_lieu`=null. | — | 1. Drill-down. 2. Click [Trình duyệt KQ]. | (2) Reject với **"Vui lòng hoàn chỉnh BC trước khi trình"** (ERR-XI-07-01). KHÔNG transition. | Negative 🔴 |
| TC-TPD-011 | SM-DOT-BC / Đợt ≠ DANG_LAP_BC | Trình PD khi đợt đã CHO_DUYET_KQ | cb_nv_tw_01 login. Đợt DOT-CTW01-011 CHO_DUYET_KQ. | — | 1. Drill-down. | (1) Nút [Trình duyệt KQ] **ẩn**. KHÔNG cho re-trigger. | Negative 🔴 |
| TC-TPD-012 | BR-AUTH-08 — chỉ người trình hoặc cùng đơn vị | CB NV khác đơn vị Trình PD | cb_nv_dp_02 (Sở TP BG) login. Đợt DOT-CDP01-012 (Sở TP AG) DANG_LAP_BC. | — | 1. Truy cập URL drill-down trực tiếp. | (1) 403 Forbidden HOẶC redirect/blank vì khác `don_vi_id` (BR-AUTH-08). KHÔNG thấy nút. | Negative 🟡 |

---

## C. Trình phê duyệt BC — EDGE (A4 merged)

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|---------|--------------|----------------|-----------|-------------------|------------------|------|
| TC-TPD-013 | FR-XI-07 / Idempotency 2 lần Trình (A4) | Click [Trình duyệt KQ] 2 lần | cb_nv_tw_01 login. Đợt DOT-CTW01-013 DANG_LAP_BC, BC đầy đủ. | — | 1. Click [Trình duyệt KQ] lần 1 → Modal OK. 2. Reload. 3. Click lần 2 (nếu nút còn). | (1) Sau lần 1: đợt CHO_DUYET_KQ, nút ẩn. (3) Lần 2 không trigger được. KHÔNG tạo notification trùng cho CB PD. | Edge 🟡 |
| TC-TPD-014 | FR-XI-07 / Network failure rollback (A4) | Trình PD lúc network fail | cb_nv_tw_01 login. Đợt DOT-CTW01-014 DANG_LAP_BC. | — | 1. MCP intercept POST `/trinh-duyet` → fail 500. 2. Click [Trình duyệt KQ]. | (2) Toast error "Lỗi hệ thống, vui lòng thử lại". (2) Đợt giữ DANG_LAP_BC, BC giữ DU_THAO. KHÔNG dirty state. KHÔNG audit log INSERT (chỉ log nếu thành công). | Edge 🟡 |

---

## Tổng kết file 03-TC

- **8 TC**: 3 Happy + 3 Negative + 2 Edge (A3 base 6 + A4 merged 2)
- **Critical TC (🔴)**: 001, 010, 011
- **A4 merged 2026-05-10**: TC-TPD-013, TC-TPD-014

*Generated 2026-05-10 — Phase A step A3 + A4 inline merge*
