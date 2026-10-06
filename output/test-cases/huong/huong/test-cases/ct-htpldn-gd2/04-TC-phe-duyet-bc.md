# Test Cases — FR-XI-07a (UC168): Phê duyệt / Từ chối BC kết quả

> **SRS Ref**: FR-XI-07a, SCR-XI-01 Drill-down (action [Phê duyệt] + [Từ chối]), Entity DOT_BAO_CAO + BAO_CAO_CT_HTPL
> **Ngày tạo**: 2026-05-10
> **Đặc thù**: CB PD cùng cấp (BR-AUTH-05) duyệt BC ở CHO_DUYET_KQ. Duyệt → đợt DA_DUYET_KQ + BC DA_DUYET. Từ chối → đợt DANG_LAP_BC + BC TU_CHOI + lý do (BR-FLOW-04).
> **Scope**: 2 transition Duyệt/Từ chối + verify state + cross-cấp/cross-đơn vị + lý do bắt buộc. KHÔNG gồm Gửi TW (xem `05-TC-gui-len-tw.md`).

---

## Quy ước

- **Priority**: 🔴 P0 · 🟡 P1 · 🟢 P2
- **TraceID**: `FR-XI-07a / {section}` — truy vết SRS
- **Pre-conditions mặc định**: User đã đăng nhập, có quyền "Phê duyệt BC kết quả CT", BC ở CHO_DUYET_KQ, CB PD cùng cấp với CB NV trình.

---

## Trường input FR-XI-07a

| # | Field | Bắt buộc | Kiểu | Ràng buộc |
|---|-------|----------|------|-----------|
| 1 | bao_cao_id | Y | identifier | FK BAO_CAO_CT_HTPL — Context |
| 2 | quyet_dinh | Y | text | DUYET / TU_CHOI |
| 3 | ly_do_tu_choi | Conditional | text (long) | Bắt buộc khi TU_CHOI |
| 4 | ghi_chu_phe_duyet | N | text (long) | — |

---

## A. Phê duyệt BC — HAPPY

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|---------|--------------|----------------|-----------|-------------------|------------------|------|
| TC-PD-BC-001 | SM-DOT-BC + SM-BC sub / CHO_DUYET_KQ → DA_DUYET_KQ + CHO_PHE_DUYET → DA_DUYET | Phê duyệt BC happy path | cb_pd_tw_01 login. Đợt DOT-CTW01-001 CHO_DUYET_KQ, BC CHO_PHE_DUYET, do cb_nv_tw_01 trình. | ghi_chu_phe_duyet="OK" | 1. Drill-down. 2. Click [Phê duyệt]. 3. Modal xác nhận → nhập ghi chú → OK. | (2) PATCH `/api/v1/bao-cao-ct/{id}/phe-duyet` 200. (3) Đợt BC = `DA_DUYET_KQ` (badge xanh lá). (3) BC = `DA_DUYET`. (3) Notification gửi cb_nv_tw_01 với "Có thể gửi lên TW". (3) Nút [Gửi lên TW] enable cho CB NV. Audit log INSERT (BR-DATA-05). | Happy 🔴 |
| TC-PD-BC-002 | FR-XI-07a / Inputs#4 — ghi_chu optional | Phê duyệt không nhập ghi chú | cb_pd_tw_01 login. Đợt DOT-CTW01-002 CHO_DUYET_KQ. | ghi_chu_phe_duyet="" | 1. Drill-down. 2. Click [Phê duyệt]. 3. Modal → để trống ghi chú → OK. | (3) PASS — ghi_chu là optional. Duyệt thành công. | Happy 🟢 |

---

## B. Từ chối BC — HAPPY

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|---------|--------------|----------------|-----------|-------------------|------------------|------|
| TC-PD-BC-003 | SM-DOT-BC + SM-BC sub / CHO_DUYET_KQ → DANG_LAP_BC + CHO_PHE_DUYET → TU_CHOI / BR-FLOW-04 | Từ chối BC happy path | cb_pd_tw_01 login. Đợt DOT-CTW01-003 CHO_DUYET_KQ. | ly_do_tu_choi="Số liệu cột 3 chưa khớp với báo cáo gốc, vui lòng xem lại." | 1. Drill-down. 2. Click [Từ chối]. 3. Modal → nhập lý do → OK. | (2) PATCH `/api/v1/bao-cao-ct/{id}/tu-choi` 200. (3) Đợt BC = `DANG_LAP_BC` (rollback). (3) BC = `TU_CHOI` + `ly_do_tu_choi` lưu. (3) Notification gửi cb_nv_tw_01 kèm lý do. (3) CB NV mở lại đợt → form editable + hiển thị banner "Bị từ chối: <lý do>". Audit log INSERT (BR-DATA-05). | Happy 🔴 |
| TC-PD-BC-004 | FR-XI-07a / Postcondition — CB NV chỉnh sửa + trình lại | Sau Từ chối CB NV chỉnh sửa và trình lại | cb_nv_tw_01 login. Đợt DOT-CTW01-004 vừa bị Từ chối (DANG_LAP_BC, BC TU_CHOI). | so_lieu mới (cập nhật cột 3) | 1. Drill-down. 2. Verify form editable + banner "Bị từ chối". 3. Sửa số liệu. 4. Click [Lưu nháp] → [Trình duyệt KQ]. | (2) Form editable lại. (4) Đợt BC quay lại CHO_DUYET_KQ + BC quay lại CHO_PHE_DUYET. Cycle Trình → Từ chối → Sửa → Trình lại verified. | Happy 🟡 |

---

## C. Phê duyệt BC — NEGATIVE

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|---------|--------------|----------------|-----------|-------------------|------------------|------|
| TC-PD-BC-010 | FR-XI-07a / E1 ERR-XI-07a-01 (Codex CT-GD2-07 rename) | Duyệt thất bại khi DOT_BAO_CAO không ở trạng thái CHO_DUYET_KQ | cb_pd_tw_01 login. Đợt DOT-CTW01-010 đã DA_DUYET_KQ. | — | 1. Drill-down. 2. Click [Phê duyệt] (nếu còn nút). | (1) Nút [Phê duyệt] **ẩn** vì đợt đã duyệt. HOẶC backend reject 400 với **"BC không ở trạng thái chờ duyệt kết quả"** (ERR-XI-07a-01). | Negative 🔴 |
| TC-PD-BC-011 | FR-XI-07a / E2 ERR-XI-07a-02 + BR-FLOW-04 | Từ chối thiếu lý do | cb_pd_tw_01 login. Đợt DOT-CTW01-011 CHO_DUYET_KQ. | ly_do_tu_choi="" | 1. Drill-down. 2. Click [Từ chối]. 3. Modal → bỏ trống lý do → OK. | (3) Reject với **"Vui lòng nhập lý do từ chối"** (ERR-XI-07a-02). KHÔNG transition. Modal giữ. | Negative 🔴 |
| TC-PD-BC-012 | FR-XI-07a / E3 ERR-XI-07a-03 + BR-AUTH-05 | CB PD khác cấp duyệt | cb_pd_tw_01 (TW) login. Đợt DOT-CDP01-012 ở ĐP CHO_DUYET_KQ (do cb_nv_dp_01 trình). | — | 1. Truy cập drill-down URL trực tiếp. 2. Click [Phê duyệt]. | (1) Nút [Phê duyệt] **ẩn** trong UI vì khác cấp. HOẶC nếu force trigger qua API: backend reject 403 với **"Bạn chỉ được phê duyệt BC cùng cấp"** (ERR-XI-07a-03). | Negative 🔴 |

---

## D. Phê duyệt BC — EDGE

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|---------|--------------|----------------|-----------|-------------------|------------------|------|
| TC-PD-BC-013 | BR-AUTH-05 cùng cấp ĐP cross-đơn vị (SPEC-CLARIFY-CT-GD2-02) | CB PD ĐP duyệt BC ĐP khác đơn vị | cb_pd_dp_02 (Sở TP BG) login. Đợt DOT-CDP01-013 ở Sở TP AG CHO_DUYET_KQ. | — | 1. Truy cập drill-down URL. 2. Click [Phê duyệt]. | (1) ⚠️ SPEC-CLARIFY-CT-GD2-02: SRS srs-fr-15:1428-1435 + 884 nói "cùng cấp" nhưng không nói rõ "cùng đơn vị". Expected: BLOCK theo BR-AUTH-08 (khác don_vi_id) HOẶC PASS nếu BR-AUTH-05 chỉ check `cap` (TW/BN/ĐP). Cần BA clarify. | Edge 🟡 |
| TC-PD-BC-014 | BR-EC-13 / XSS sanitize ly_do_tu_choi (A4) | Inject XSS vào lý do từ chối | cb_pd_tw_01 login. Đợt DOT-CTW01-014 CHO_DUYET_KQ. | ly_do_tu_choi=`<img src=x onerror=alert('xss')>` + 50 ký tự text | 1. Click [Từ chối]. 2. Modal nhập payload XSS. 3. OK. | (3) Backend chấp nhận text raw. CB NV mở banner "Bị từ chối" → render escape, hiển thị literal payload, KHÔNG execute. | Edge 🔴 |
| TC-PD-BC-015 | FR-XI-07a / Inputs#3 — ly_do > 5000 ký tự (A4) | Nhập lý do từ chối > giới hạn | cb_pd_tw_01 login. Đợt DOT-CTW01-015 CHO_DUYET_KQ. | ly_do_tu_choi=5001 ký tự | 1. Modal Từ chối → nhập 5001 ký tự. 2. OK. | (2) ⚠️ SRS không nói explicit max length cho ly_do_tu_choi (chỉ là `text (long)`). Expected: cap 5000 (đồng nhất với nhan_xet) HOẶC hiển thị giới hạn cụ thể. Log SPEC-CLARIFY-CT-GD2-07 nếu unclear. | Edge 🟢 |
| TC-PD-BC-016 | FR-XI-07a / Audit dual entry (A4 + A7 SỬA UI) | Audit ghi 2 entry khi duyệt (đợt + BC) | cb_pd_tw_01 login. Đợt DOT-CTW01-016 CHO_DUYET_KQ. | — | 1. Phê duyệt. 2. Mở module Nhật ký HT (FR-10) qua sidebar `/quan-tri/audit-log` lọc `entity IN (DOT_BAO_CAO, BAO_CAO_CT_HTPL)` + filter `record_id` đợt vừa duyệt. 3. MCP `take_snapshot` table audit log. | (3) UI table audit log hiển thị 2 entries: 1 UPDATE DOT_BAO_CAO (TRANSITION DA_DUYET_KQ), 1 UPDATE BAO_CAO_CT_HTPL (TRANSITION DA_DUYET). Cùng `actor=cb_pd_tw_01`, `transaction_id` chung trong cell hiển thị. (BR-DATA-05) | Edge 🟡 |

---

## Tổng kết file 04-TC

- **12 TC**: 2 Happy duyệt + 2 Happy từ chối + 3 Negative + 1 Edge cross-đơn vị + 3 Edge A4 (A3 base 9 + A4 merged 3)
- **Critical TC (🔴)**: 001, 003, 010, 011, 012, 014
- **A4 merged 2026-05-10**: TC-PD-BC-014, 015, 016
- **SPEC-CLARIFY**: CT-GD2-02 (TC-PD-BC-013 cross-đơn vị ĐP), CT-GD2-07 (TC-PD-BC-015 ly_do max length)

*Generated 2026-05-10 — Phase A step A3 + A4 inline merge*
