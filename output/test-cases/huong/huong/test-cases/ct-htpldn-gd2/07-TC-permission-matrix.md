# Test Cases — Permission Matrix Cross-FR-XI GĐ2 (UC165 cont + UC166..UC170)

> **SRS Ref**: FR-XI-05a..09 + Permission Matrix tổng hợp 8 role × 8 action GĐ2 (xem `00-test-plan-overview.md` §2.3)
> **Ngày tạo**: 2026-05-10
> **Đặc thù**: Verify boundary 8 role (QTHT/CB_NV TW/BN/ĐP/CB_PD TW/BN/ĐP/Negative) với 8 action GĐ2 (Lập/Trình/Duyệt/Từ chối/Gửi TW/Tổng hợp/Xuất file). Áp dụng BR-AUTH-08 (don_vi_id scope) + BR-AUTH-05 (cùng cấp PD).
> **Scope**: TC permission positive + negative — BỎ duplicate với TC permission rời rạc trong file 01-06.

---

## Quy ước

- **Priority**: 🔴 P0 · 🟡 P1 · 🟢 P2
- **TraceID**: Permission Matrix cell — cross-ref §2.3 plan overview
- **Pre-conditions mặc định**: Module CT HTPLDN có sẵn data đa cấp (TW/BN/ĐP), test fallback `_03` cho permission test (tránh lock primary `_01`).

---

## A. Permission Matrix — POSITIVE (đúng quyền — pass)

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|---------|--------------|----------------|-----------|-------------------|------------------|------|
| TC-PERM-001 | Matrix / CB_NV scope đơn vị (BR-AUTH-08) | CB NV ĐP chỉ thấy đợt BC scope đơn vị mình | cb_nv_dp_03 (Sở TP AG) login. Có đợt DOT-CDP01-AG (Sở TP AG) + DOT-CDP01-BG (Sở TP BG) cùng kỳ. | — | 1. Truy cập SCR-XI-01 → tab Đợt báo cáo. | (1) Chỉ thấy DOT-CDP01-AG. KHÔNG thấy DOT-CDP01-BG (BR-AUTH-08 scope). | Positive 🔴 |
| TC-PERM-002 | Matrix / CB_PD cùng cấp duyệt (BR-AUTH-05) | CB PD ĐP duyệt BC ĐP cùng đơn vị | cb_pd_dp_03 (Sở TP AG) login. Đợt DOT-CDP01-002 (Sở TP AG) CHO_DUYET_KQ. | — | 1. Drill-down. 2. Click [Phê duyệt]. | (2) PASS — CB PD ĐP cùng đơn vị duyệt được. Đợt → DA_DUYET_KQ. | Positive 🔴 |
| TC-PERM-003 | Matrix / QTHT Read-only | QTHT có thể xem nhưng KHÔNG thao tác | qtht_03 login. Đợt DOT-CTW01-003 ở mọi state. | — | 1. Truy cập SCR-XI-01 → drill-down. 2. Verify nút action. | (2) Form 21a/21b read-only. KHÔNG thấy nút [Lưu nháp], [Trình duyệt KQ], [Phê duyệt], [Từ chối], [Gửi lên TW], [Tổng hợp]. Chỉ có [Xem]. | Positive 🟡 |

---

## B. Permission Matrix — NEGATIVE (sai quyền — block)

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|---------|--------------|----------------|-----------|-------------------|------------------|------|
| TC-PERM-010 | Matrix / NHT/TVV/CG/DN/GV chặn module | Role ngoài CB block module CT HTPLDN | nht_03 login. (Repeat cho tvv_03, cg_03, dn_03, gv_03 với cùng pattern.) | — | 1. Truy cập URL `/ct-htpldn` trực tiếp. | (1) 403 Forbidden HOẶC redirect khỏi module. KHÔNG hiển thị menu/sidebar entry "Quản lý CT HTPLDN". | Negative 🔴 |
| TC-PERM-011 | Matrix / TW không Gửi TW | CB NV TW thử Gửi TW (chính mình) | cb_nv_tw_03 login. Đợt DOT-CTW01-011 DA_DUYET_KQ. | — | 1. Drill-down. | (1) Nút [Gửi lên TW] **ẩn** cho cấp TW. (Hỗ trợ ERR-XI-08-02 nếu force trigger qua API.) | Negative 🔴 |
| TC-PERM-012 | Matrix / BN/ĐP không Tổng hợp | CB NV BN/ĐP thử action Tổng hợp | cb_nv_bn_03 login. ≥1 BC DA_GUI_TW available. | — | 1. Truy cập URL `/ct-htpldn/{id}/tong-hop-tw` trực tiếp. | (1) 403 Forbidden. UI KHÔNG show bảng BC từ BN/ĐP cho cấp BN/ĐP. (Hỗ trợ ERR-XI-09-02.) | Negative 🔴 |

---

## C. Permission Matrix — EDGE (A4 merged)

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|---------|--------------|----------------|-----------|-------------------|------------------|------|
| TC-PERM-013 | Matrix / DN/GV không thấy module (A4) | DN/GV truy cập CT HTPLDN | dn_03 login, sau đó gv_03 login (lặp). | — | 1. Truy cập URL `/ct-htpldn` trực tiếp. 2. Verify sidebar menu. | (1) 403 Forbidden cho cả DN và GV. Sidebar KHÔNG có entry CT HTPLDN cho 2 role này. (Hỗ trợ Permission Matrix line "NHT/TVV/CG/DN/GV" → ❌). | Negative 🔴 |
| TC-PERM-014 | Matrix / Session expired during action (A4) | Session expire khi đang lập BC | cb_nv_tw_03 login. Đợt DOT-CTW01-014 DANG_LAP_BC. | — | 1. Drill-down + nhập số liệu form 21a. 2. MCP `evaluate_script` clear `sessionStorage.auth-store` (mô phỏng session expired). 3. Click [Lưu nháp]. | (3) 401 Unauthorized → redirect `/login`. KHÔNG persist số liệu chưa Lưu. (BR-AUTH-01) | Edge 🟡 |
| TC-PERM-015 | Matrix / TK TAM_KHOA active session (A4) | TK bị TAM_KHOA giữa session active | cb_nv_dp_03 login. Admin set TK `cb_nv_dp_03.trang_thai=TAM_KHOA` qua DB seed (precondition). | — | 1. Đang ở drill-down. 2. Reload page hoặc click action. | (2) Auth check fail trên next request → toast "Tài khoản tạm khóa" + redirect login. (BR-AUTH-01 + AC TAI_KHOAN.trang_thai) | Edge 🟢 |
| TC-PERM-016 | Matrix / CB_PD_BN positive cùng cấp + cùng đơn vị (A6 fill GAP-A5-03) | CB PD BN duyệt BC BN cùng đơn vị | cb_pd_bn_03 (Bộ KH&ĐT) login. Đợt DOT-CBN01-016 (Bộ KH&ĐT) CHO_DUYET_KQ. | — | 1. Drill-down. 2. Click [Phê duyệt]. | (2) PASS — CB PD BN cùng đơn vị duyệt được. Đợt → DA_DUYET_KQ. (Symmetrical với TC-PERM-002 cho ĐP — verify pattern BN cũng cover.) | Positive 🔴 |
| TC-PERM-017 | Matrix / CB_PD không Gửi TW (Codex CT-GD2-04) | CB PD ĐP/BN thử action Gửi TW (chỉ CB NV BN/ĐP có quyền) | cb_pd_dp_03 (Sở TP AG) login. Đợt DOT-CDP01-017 (Sở TP AG) DA_DUYET_KQ. | — | 1. Drill-down. 2. Verify nút [Gửi lên TW]. | (2) Nút [Gửi lên TW] **ẩn** cho CB PD (chỉ CB NV BN/ĐP có quyền per FR-XI-08 line 901 "Tác nhân: Cán bộ Nghiệp vụ BN/ĐP"). Nếu force trigger qua API: backend reject 403 (ERR-XI-08-02 hoặc 403 generic). Repeat tương tự cho cb_pd_bn_03. | Negative 🔴 |

---

## Tổng kết file 07-TC

- **11 TC**: 4 Positive + 4 Negative + 3 Edge (A3 base 6 + A4 merged 3 + A6 merged 1 + Codex merged 1)
- **Critical TC (🔴)**: 001, 002, 010, 011, 012, 013, 016, 017
- **A4 merged 2026-05-10**: TC-PERM-013, 014, 015
- **A6 merged 2026-05-10**: TC-PERM-016 (GAP-A5-03)
- **Codex merged 2026-05-10**: TC-PERM-017 (CODEX-CT-GD2-04)
- Coverage permission matrix: 8 role × 8 action = 64 cells, hợp nhất với positive case in-line trong file 01-06 → ~33 cells verify trực tiếp + 31 cells suy luận từ negative chung.

*Generated 2026-05-10 — Phase A step A3 + A4 + A6 + Codex inline merge*
