# Traceability Matrix — FR-15 CT HTPLDN GĐ1 (BMAD A5)

> **Ngày**: 2026-05-06 · **Tool**: bmad-testarch-trace
> **Scope**: 8 TC files (01-08) sau A3 + A4 = 83 TC
> **Mục đích**: Map 2 chiều BR/AC ↔ TC ID, đảm bảo coverage ≥95% BR (loại BR-EC-19 thuộc GĐ2) và 100% AC SRS GĐ1.

---

## 1. BR Coverage Matrix

| BR ID | Phát biểu (rút gọn) | Source | TC cover |
|-------|---------------------|--------|----------|
| BR-AUTH-01 | Xác thực 2-tier (TOTP/SSO VNeID) | srs-fr-15:1419 | Precondition mọi TC + TC-PERM-CT-006 |
| BR-AUTH-05 | Phê duyệt cùng cấp | srs-fr-15:1428 | TC-PD-CT-001/002, TC-PD-CT-004 (E3), TC-PD-CT-005 (SPEC), TC-PERM-CT-002 |
| BR-AUTH-08 | Phân quyền theo `don_vi_id` | srs-v3 Phụ lục B | TC-CT-CRUD-006, TC-CT-TK-004, TC-CB-CT-006, TC-PERM-CT-001/003 |
| BR-DATA-01 | Soft delete | srs-fr-15:1437 | TC-CT-CRUD-003, TC-DOT-BC-003 |
| BR-DATA-05 | Audit trail INSERT-only | srs-fr-15:1444 | TC-CT-CRUD-001/002/003, TC-LC-001/004/007/009/012/014, TC-TR-CT-001, TC-PD-CT-001/002, TC-CB-CT-001/003, TC-DOT-BC-001/002/003, TC-LC-016/017 |
| BR-DATA-06 | Export Excel max 10k rows | srs-v3:3977 | TC-CT-TK-006, TC-CT-TK-007 (boundary), TC-CT-TK-008 (empty) |
| BR-DATA-07 | Pagination 20 default, max 100 | srs-fr-15:1453 | TC-CT-CRUD-004, TC-CT-TK-002, TC-DOT-BC-004, TC-CT-TK-009 (page_size guard) |
| BR-FLOW-03 | Không sửa/xóa sau phê duyệt | srs-fr-15:1460 | TC-CT-CRUD-011/012, TC-DOT-BC-005/006 |
| BR-FLOW-04 | Từ chối yêu cầu lý do | srs-fr-15:1467 | TC-PD-CT-002/003, TC-LC-005 (tạm dừng), TC-LC-017 (re-submit cycle TC) |
| BR-FLOW-05 | Công bố qua API trực tiếp Cổng PLQG | srs-fr-15:1474 | TC-CB-CT-001/002/003 |
| BR-EC-01 | Optimistic Locking | srs-v3:4066 | TC-CT-CRUD-017 (concurrent UPDATE), TC-TR-CT-006 (concurrent submit), TC-PD-CT-008 (concurrent approve), TC-CB-CT-008 (concurrent publish) |
| BR-EC-12 | Pagination guard `[1,100]` | srs-v3:4077 | TC-CT-TK-009 |
| BR-EC-13 | Search sanitize max 200 ký tự + escape | srs-v3:4078 | TC-CT-TK-010 (SQL inj), TC-CT-TK-011 (XSS) |
| **SM-KH-CTHTPL** | State machine 8 states + 12 transitions | srs-fr-15:1331-1370 | All file 03-06 + lifecycle TC trong 01 |
| **SM-DOT-BC** | State machine 6 states (chỉ TAO_DOT trong GĐ1) | srs-fr-15:1371-1397 | File 07 — TC-DOT-BC-001..010 (transition `[*] → TAO_DOT`) |

**Coverage BR GĐ1:** 13/14 BR áp dụng = **92.8%** (BR-EC-19 batch ops loại do thuộc GĐ2 — TW tổng hợp)
**Coverage SM:** 100% transition GĐ1 (8 states + 12 transitions của SM-KH-CTHTPL) + 1/6 transition của SM-DOT-BC (`[*] → TAO_DOT`, các transition còn lại defer GĐ2)

---

## 2. AC (Acceptance Criteria) Coverage

| FR | AC# | Mô tả AC (rút gọn) | TC cover |
|----|-----|-------------------|----------|
| FR-XI-01 | AC1 | DS CT phân trang scope đơn vị | TC-CT-CRUD-004, TC-CT-CRUD-006 |
| FR-XI-01 | AC2 | Thêm mới CT validate + lưu | TC-CT-CRUD-001, TC-CT-CRUD-010 |
| FR-XI-01 | AC3 | Sửa CT DU_THAO | TC-CT-CRUD-002, TC-CT-CRUD-011 |
| FR-XI-01 | AC4 | Xóa CT DU_THAO soft delete | TC-CT-CRUD-003, TC-CT-CRUD-012 |
| FR-XI-01 sub | Kích hoạt — AC | CT DA_DUYET/DA_CONG_BO → DANG_THUC_HIEN | TC-LC-001, TC-LC-002, TC-LC-003 |
| FR-XI-01 sub | Tạm dừng — AC | DANG_THUC_HIEN → TAM_DUNG có lý do | TC-LC-004, TC-LC-005, TC-LC-006 |
| FR-XI-01 sub | Tiếp tục — AC | TAM_DUNG → DANG_THUC_HIEN | TC-LC-007, TC-LC-008 |
| FR-XI-01 sub | Hoàn thành — AC | CB PD, guard BC done | TC-LC-009, TC-LC-010, TC-LC-011 |
| FR-XI-01 sub | Hủy — AC | DU_THAO → HUY | TC-LC-012, TC-LC-013 |
| FR-XI-01 sub | Rút trình — AC | CB NV người trình, CHO_PHE_DUYET → DU_THAO | TC-LC-014, TC-LC-015, TC-LC-016 (cycle) |
| FR-XI-02 | AC1 | Tìm theo từ khóa/lọc, AND nhiều điều kiện, phân trang | TC-CT-TK-001, TC-CT-TK-002, TC-CT-TK-003, TC-CT-TK-005 |
| FR-XI-02 | Xuất Excel — AC1 | Xuất theo filter hiện tại | TC-CT-TK-006 |
| FR-XI-02 | Xuất Excel — AC2 | DS trống → INF | TC-CT-TK-008 |
| FR-XI-02 | Xuất Excel — AC3 | >10,000 dòng cảnh báo | TC-CT-TK-007 |
| FR-XI-03 | AC1 | CB NV trình PD | TC-TR-CT-001, TC-TR-CT-002 (notification cùng cấp) |
| FR-XI-04 | AC1 | CB PD duyệt CT | TC-PD-CT-001, TC-PD-CT-007 (state guard) |
| FR-XI-04 | AC2 | CB PD từ chối với lý do | TC-PD-CT-002, TC-PD-CT-003 |
| FR-XI-05 | AC1 | Công bố CT đã duyệt | TC-CB-CT-001, TC-CB-CT-004 (state guard) |
| FR-XI-05 | AC2 | Hủy công bố | TC-CB-CT-003 |
| FR-XI-05a | AC1 | DS đợt BC phân trang | TC-DOT-BC-004 |
| FR-XI-05a | AC2 | Thêm đợt BC validate | TC-DOT-BC-001, TC-DOT-BC-005 (state guard CT), TC-DOT-BC-007 (trùng kỳ) |
| FR-XI-05a | AC3 | Sửa đợt BC TAO_DOT | TC-DOT-BC-002, TC-DOT-BC-006 |
| FR-XI-05a | AC4 | Xóa đợt BC TAO_DOT | TC-DOT-BC-003, TC-DOT-BC-006 |
| FR-XI-05a | AC tạo HOAN_THANH | Tạo đợt BC khi CT HOAN_THANH | TC-DOT-BC-009 |

**Coverage AC GĐ1:** 24/24 AC trong 6 FR = **100%** ✅

---

## 3. State Machine Transition Coverage

### SM-KH-CTHTPL (12 transitions)

| Từ → Đến | Trigger | TC cover |
|----------|---------|----------|
| `[*] → DU_THAO` | CB NV tạo CT | TC-CT-CRUD-001 |
| `DU_THAO → CHO_PHE_DUYET` | CB NV trình | TC-TR-CT-001, TC-TR-CT-002, TC-LC-016 |
| `CHO_PHE_DUYET → DA_DUYET` | CB PD duyệt | TC-PD-CT-001, TC-LC-017 |
| `CHO_PHE_DUYET → DU_THAO` (TC) | CB PD từ chối | TC-PD-CT-002, TC-LC-017 |
| `CHO_PHE_DUYET → DU_THAO` (rút) | CB NV rút trình | TC-LC-014, TC-LC-016 |
| `DA_DUYET → DA_CONG_BO` | CB NV công bố | TC-CB-CT-001 |
| `DA_CONG_BO → DA_DUYET` | CB NV hủy CB | TC-CB-CT-003 |
| `DA_DUYET → DANG_THUC_HIEN` | CB NV kích hoạt | TC-LC-001 |
| `DA_CONG_BO → DANG_THUC_HIEN` | CB NV kích hoạt | TC-LC-002 |
| `DANG_THUC_HIEN → TAM_DUNG` | CB NV/PD tạm dừng + lý do | TC-LC-004 |
| `TAM_DUNG → DANG_THUC_HIEN` | CB NV/PD tiếp tục | TC-LC-007 |
| `DANG_THUC_HIEN → HOAN_THANH` | CB PD hoàn thành | TC-LC-011 |
| `DU_THAO → HUY` | CB NV hủy | TC-LC-012 |

**Coverage SM-KH-CTHTPL:** 12/12 transition + 1 init = 100% ✅

### SM-DOT-BC (6 transitions, GĐ1 chỉ test 1)

| Từ → Đến | Trigger | TC cover (GĐ1) |
|----------|---------|----------------|
| `[*] → TAO_DOT` | CB NV tạo đợt | TC-DOT-BC-001, TC-DOT-BC-009 |
| 5 transition còn lại | Lập BC / Trình duyệt KQ / Phê duyệt / Gửi TW / Tổng hợp | (Defer GĐ2 W5.1) |

**Coverage SM-DOT-BC GĐ1:** 1/1 in-scope = 100% ✅

---

## 4. Permission Cross-Matrix Coverage

| Action | TC cover |
|--------|----------|
| QTHT read-only verify | TC-PERM-CT-005 |
| CB_NV scope đơn vị | TC-CT-CRUD-006, TC-CT-TK-004, TC-PERM-CT-001 |
| CB_PD cùng cấp duyệt | TC-PD-CT-001, TC-PD-CT-004, TC-PERM-CT-002 |
| CB_PD KHÔNG CRUD | TC-CB-CT-005, TC-PD-CT-006, TC-TR-CT-005 |
| NHT/TVV/CG/DN block 403 | TC-PERM-CT-004 |
| Unauthenticated redirect | TC-PERM-CT-006 |

---

## 5. Gap Analysis (forward A6)

| Gap | Mô tả | Action A6 |
|-----|-------|-----------|
| GAP-CT-A5-01 | TC-LC-011 (Hoàn thành happy) phụ thuộc đợt BC DA_TONG_HOP — cross-phase seed | A6: thêm note "cross-phase seed" + giữ TC, defer Phase B nếu không seed được |
| GAP-CT-A5-02 | Notification CT (BR-NOTIFY-* không có trong SRS FR-15 BR list) — verify gửi cb_pd_cùng_cấp khi NV trình | A6: bổ sung TC verify network/notification UI nếu có |
| GAP-CT-A5-03 | BR-DATA-05 audit log: chưa có TC dedicated verify audit log entry detail (chỉ ghi "Audit log" trong expected) | A6: thêm 1 TC E2E audit trace cho 1 lifecycle full-cycle |
| GAP-CT-A5-04 | BR-EC-02 cascade soft delete (xóa CT DU_THAO) — đã resolve qua SPEC-CLARIFY-CT-05 (đợt BC chỉ tồn tại sau DA_DUYET → không xảy ra cascade) | (No action) |
| GAP-CT-A5-05 | TC-CB-CT-002 rollback Cổng PLQG fail — chưa có TC verify state KHÔNG persist DA_CONG_BO trong DB sau rollback | A6: tăng cường expected — verify reload page state vẫn DA_DUYET |

---

## Tổng kết A5

- **Coverage BR**: 13/14 = 92.8% (loại BR-EC-19 GĐ2)
- **Coverage AC**: 24/24 = 100%
- **Coverage SM transitions**: 12/12 (SM-KH-CTHTPL) + 1/1 in-scope (SM-DOT-BC) = 100%
- **Permission**: cross-cutting đầy đủ
- **Gap forward A6**: 5 gap items

*Generated 2026-05-06 — Phase A step A5*
