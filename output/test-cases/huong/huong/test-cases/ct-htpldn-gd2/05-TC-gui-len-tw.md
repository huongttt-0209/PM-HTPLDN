# Test Cases — FR-XI-08 (UC169): Gửi BC lên TW

> **SRS Ref**: FR-XI-08, SCR-XI-01 Drill-down (action [Gửi lên TW]), Entity DOT_BAO_CAO
> **Ngày tạo**: 2026-05-10
> **Đặc thù**: Chỉ CB NV BN/ĐP gửi BC đã duyệt KQ lên TW. Side-effect: đợt BC `DA_DUYET_KQ → DA_GUI_TW`, set `da_gui_tw=1`, `ngay_gui=NOW`. BC hiển thị trong DS "Tổng hợp" của TW.
> **Scope**: Hành động Gửi + verify state + permission BN/ĐP. KHÔNG gồm Tổng hợp TW (xem `06-TC-tw-tong-hop-bc.md`).

---

## Quy ước

- **Priority**: 🔴 P0 · 🟡 P1 · 🟢 P2
- **TraceID**: `FR-XI-08 / {section}` — truy vết SRS
- **Pre-conditions mặc định**: User đã đăng nhập, thuộc cấp BN hoặc ĐP, đợt BC ở DA_DUYET_KQ.

---

## A. Gửi BC lên TW — HAPPY

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|---------|--------------|----------------|-----------|-------------------|------------------|------|
| TC-GTW-001 | SM-DOT-BC / DA_DUYET_KQ → DA_GUI_TW + BR-FLOW-08 | Gửi TW happy path từ ĐP | cb_nv_dp_01 (Sở TP AG) login. Đợt DOT-CDP01-001 DA_DUYET_KQ. | — | 1. Drill-down. 2. Click [Gửi lên TW]. 3. Modal xác nhận → OK. | (2) PATCH `/api/v1/dot-bao-cao/{id}/gui-tw` 200. (3) Đợt BC = `DA_GUI_TW` (badge xanh dương). (3) `da_gui_tw=1`, `ngay_gui=NOW()`. (3) Toast "Gửi BC lên TW thành công". (3) MCP `list_network_requests` thấy POST `/notifications` outbound (gửi CB NV TW). Audit log INSERT (BR-DATA-05). | Happy 🔴 |
| TC-GTW-002 | FR-XI-08 / Postcondition + BR-FLOW-08 | TW thấy BC vừa gửi trong DS "Tổng hợp" | cb_nv_tw_01 (TW) login NGAY SAU TC-GTW-001. | — | 1. Truy cập drill-down CT có đợt vừa gửi. 2. MCP `evaluate_script` đọc bảng "BC từ BN/ĐP" trong UI tổng hợp (line 1104 SRS). | (2) Đợt DOT-CDP01-001 xuất hiện trong bảng với cột: Đơn vị "Sở TP AG", Cấp "ĐP", Mã đợt, Kỳ, Ngày gửi, Trạng thái "Đã gửi TW", Hành động [Xem]. Filter `da_gui_tw=1` áp dụng đúng. | Happy 🔴 |
| TC-GTW-003 | FR-XI-08 / Happy từ BN | Gửi TW happy path từ BN | cb_nv_bn_01 (Bộ KH&ĐT) login. Đợt DOT-CBN01-003 DA_DUYET_KQ. | — | 1. Drill-down. 2. Gửi TW. | (2) PASS — BN cũng được gửi (Tác nhân SRS dòng 901: "Cán bộ Nghiệp vụ BN/ĐP"). | Happy 🟡 |

---

## B. Gửi BC lên TW — NEGATIVE

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|---------|--------------|----------------|-----------|-------------------|------------------|------|
| TC-GTW-010 | FR-XI-08 / E1 ERR-XI-08-01 | Đợt BC chưa duyệt KQ | cb_nv_dp_01 login. Đợt DOT-CDP01-010 ở DANG_LAP_BC (chưa duyệt). | — | 1. Drill-down. | (1) Nút [Gửi lên TW] **ẩn**. HOẶC backend reject 400 với **"Đợt BC chưa được phê duyệt kết quả"** (ERR-XI-08-01). | Negative 🔴 |
| TC-GTW-011 | FR-XI-08 / E2 ERR-XI-08-02 | TW Gửi TW (cấp TW không gửi cho chính mình) | cb_nv_tw_01 (TW) login. Đợt DOT-CTW01-011 DA_DUYET_KQ. | — | 1. Drill-down. | (1) Nút [Gửi lên TW] **ẩn** (TW không thấy nút này). HOẶC nếu force trigger: backend reject 403 với **"Chỉ đơn vị BN/ĐP mới gửi BC lên TW"** (ERR-XI-08-02). | Negative 🔴 |

---

## C. Gửi BC lên TW — EDGE

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|---------|--------------|----------------|-----------|-------------------|------------------|------|
| TC-GTW-012 | FR-XI-08 / Idempotency — 2 lần Gửi liên tiếp | Click [Gửi lên TW] 2 lần liên tiếp | cb_nv_dp_01 login. Đợt DOT-CDP01-012 DA_DUYET_KQ. | — | 1. Click [Gửi lên TW] lần 1 → OK. 2. Reload page. 3. Click [Gửi lên TW] lần 2 (nếu nút còn). | (2) Sau lần 1: đợt DA_GUI_TW, nút ẩn. (3) Lần 2 không thể trigger (nút ẩn). KHÔNG tạo notification trùng. KHÔNG ghi audit log trùng. | Edge 🟡 |

---

| TC-GTW-013 | FR-XI-08 / Network failure (A4) | Gửi TW lúc network fail | cb_nv_dp_01 login. Đợt DOT-CDP01-013 DA_DUYET_KQ. | — | 1. MCP intercept POST `/gui-tw` → fail 500. 2. Click [Gửi lên TW]. | (2) Toast error "Lỗi hệ thống". (2) Đợt giữ DA_DUYET_KQ. KHÔNG audit. KHÔNG notification CB NV TW. | Edge 🟡 |
| TC-GTW-014 | FR-XI-08 / BR-AUTH-08 scope notification (A4) | Notification chỉ tới CB NV TW (không tới TW khác đơn vị nếu có nhiều) | cb_nv_dp_01 login. Đợt DOT-CDP01-014 DA_DUYET_KQ. Có cb_nv_tw_01 + cb_nv_tw_02 active. | — | 1. Gửi TW. 2. MCP capture notifications. | (2) ⚠️ SRS srs-fr-15:922 nói "Gửi thông báo CB NV TW" nhưng không nói scope rộng/hẹp. Expected: gửi TẤT CẢ CB NV TW (do chỉ có 1 đơn vị TW). Verify thực tế. | Edge 🟢 |

---

## Tổng kết file 05-TC

- **8 TC**: 3 Happy + 2 Negative + 3 Edge (A3 base 6 + A4 merged 2)
- **Critical TC (🔴)**: 001, 002, 010, 011
- **A4 merged 2026-05-10**: TC-GTW-013, TC-GTW-014

*Generated 2026-05-10 — Phase A step A3 + A4 inline merge*
