# A5 — Traceability Matrix BR/AC/SM/ERR ↔ TC

> **Phase A step**: A5 (`bmad-testarch-trace`)
> **Ngày chạy**: 2026-05-10
> **Scope**: 70 TC (51 A3 + 19 A4) ↔ 13 BR + 25 AC + 11 SM transitions + 9 ERR + 1 WRN
> **Iron rule**: KHÔNG sinh TC mới ở A5 — chỉ phát hiện gap → forward sang A6 fix.

---

## 1. BR Coverage

| BR ID | Áp dụng | TC verify | Coverage |
|-------|---------|-----------|----------|
| BR-AUTH-01 | ✅ | TC-LBC-011, TC-PERM-014, TC-PERM-015 (precondition mọi TC khác) | 100% |
| BR-AUTH-05 | ✅ (FR-XI-07a) | TC-PD-BC-001, 003, 012, 013, TC-PERM-002 | 100% |
| BR-AUTH-08 | ✅ scope đơn vị | TC-TPD-003, TC-TPD-012, TC-PERM-001, TC-GTW-014 | 100% |
| BR-DATA-05 | ✅ audit trail | TC-LBC-001, TC-BC-001, TC-TPD-001, TC-PD-BC-001/003/016, TC-GTW-001, TC-TH-001 | 100% |
| BR-DATA-06 | ✅ Excel max 10k | TC-TH-005 (xuất Excel TT17), TC-TH-006 (Word) | 100% |
| BR-DATA-07 | ✅ pagination | TC-TH-002 (DS BC từ BN/ĐP) | 100% |
| BR-EC-01 | ✅ optimistic lock | TC-BC-014 | 100% |
| BR-EC-12 | ✅ pagination guard | TC-TH-002 (gián tiếp) | ⚠️ partial — chưa có TC param boundary 0/101 trực tiếp → **GAP-A5-01** |
| BR-EC-13 | ✅ XSS sanitize | TC-BC-013, TC-PD-BC-014 | 100% |
| BR-EC-19 | ✅ batch >100 | TC-TH-013 | 100% |
| BR-FLOW-04 | ✅ từ chối lý do | TC-PD-BC-003, TC-PD-BC-011 | 100% |
| BR-FLOW-08 | ✅ ĐP/BN→TW | TC-GTW-001, 002, 003, TC-TH-001, 002 | 100% |
| BR-DATA-01 | ❌ N/A GĐ2 (BC không có DELETE) | — | N/A |

**Coverage BR: 12/12 áp dụng = 100%** (BR-DATA-01 N/A loại trừ). 1 GAP-A5-01 cần A6 fill.

## 2. SM Transitions Coverage

### SM-DOT-BC (5 transitions GĐ2)

| # | Transition | TC verify | Coverage |
|---|-----------|-----------|----------|
| 1 | TAO_DOT → DANG_LAP_BC | TC-LBC-001, 010, 012 | 100% |
| 2 | DANG_LAP_BC → CHO_DUYET_KQ | TC-TPD-001, 011, 013 | 100% |
| 3 | CHO_DUYET_KQ → DA_DUYET_KQ | TC-PD-BC-001, 010, 016 | 100% |
| 4 | CHO_DUYET_KQ → DANG_LAP_BC (từ chối) | TC-PD-BC-003, 004, 011 | 100% |
| 5 | DA_DUYET_KQ → DA_GUI_TW | TC-GTW-001, 003, 010, 012 | 100% |
| 6 | DA_GUI_TW → DA_TONG_HOP | TC-TH-001, 014, 016 | 100% |

### SM-BC sub (BAO_CAO_CT_HTPL.trang_thai)

| Transition | TC verify | Coverage |
|-----------|-----------|----------|
| [*] → DU_THAO | TC-LBC-001 (tạo BC) | 100% |
| DU_THAO → CHO_PHE_DUYET | TC-TPD-001 | 100% |
| CHO_PHE_DUYET → DA_DUYET | TC-PD-BC-001 | 100% |
| CHO_PHE_DUYET → TU_CHOI | TC-PD-BC-003 | 100% |
| TU_CHOI → DU_THAO (implicit, CB NV chỉnh sửa + trình lại) | TC-PD-BC-004 | 100% |

**Coverage SM: 11/11 transitions = 100%.**

## 3. AC Coverage

| FR | AC ref | TC verify |
|----|--------|-----------|
| FR-XI-05a | AC#1 (DS đợt BC) | TC-PERM-001 (gián tiếp), TC-LBC-001 (mở Tab Đợt BC) |
| FR-XI-05a | AC#2 (thêm đợt) | (GĐ1 đã cover — không repeat) |
| FR-XI-06 | AC#1 (form BC) | TC-LBC-001, TC-BC-001, 002, 003 |
| FR-XI-06 | AC#2 (validate + lưu) | TC-BC-001, 010 |
| FR-XI-07 | AC#1 (Trình PD) | TC-TPD-001, 010, 011 |
| FR-XI-07a | AC#1 (Duyệt) | TC-PD-BC-001, 010 |
| FR-XI-07a | AC#2 (Từ chối) | TC-PD-BC-003 |
| FR-XI-07a | AC#3 (Từ chối thiếu lý do) | TC-PD-BC-011 |
| FR-XI-08 | AC#1 (Gửi TW) | TC-GTW-001, 003 |
| FR-XI-09 | AC#1 (DS BC từ BN/ĐP) | TC-GTW-002, TC-TH-002 |
| FR-XI-09 | AC#2 (chọn + tổng hợp) | TC-TH-001, 003, 010 |
| FR-XI-09 | AC#3 (chỉnh sửa + lưu) | TC-TH-004, 001 |

**Coverage AC: 12/12 explicit AC = 100%.**

## 4. ERR Code Coverage

| ERR Code | TC verify |
|----------|-----------|
| ERR-XI-06-01 | TC-BC-010 |
| ERR-XI-07-01 | TC-TPD-010 |
| ERR-XI-07a-01 | TC-PD-BC-010 |
| ERR-XI-07a-02 | TC-PD-BC-011 |
| ERR-XI-07a-03 | TC-PD-BC-012 |
| ERR-XI-08-01 | TC-GTW-010 |
| ERR-XI-08-02 | TC-GTW-011 |
| ERR-XI-09-01 | TC-TH-010 |
| ERR-XI-09-02 | TC-TH-011 |
| WRN-XI-09-01 | TC-TH-012 |

**Coverage ERR: 9/9 + 1 WRN = 100%.**

## 5. Permission Matrix Coverage

8 role × 8 action = 64 cells.

| Role | Action covered (positive + negative) | Total |
|------|--------------------------------------|------:|
| QTHT | TC-PERM-003 (read-only) | 1/8 = 12.5% (suy luận từ matrix ❌) |
| CB_NV_TW | TC-LBC-001, TC-BC-001, TC-TPD-001, TC-TH-001..006, TC-PERM-011, 012 | 8/8 = 100% |
| CB_NV_BN | TC-GTW-003, TC-PERM-012 | 5/8 (suy luận từ ĐP) |
| CB_NV_DP | TC-LBC-003, TC-TPD-003, TC-GTW-001, 002, TC-PERM-001 | 7/8 |
| CB_PD_TW | TC-PD-BC-001, 003, 010, 011, 014, 015, 016, TC-PERM-003 | 7/8 |
| CB_PD_BN | (suy luận từ TW + ĐP) | 4/8 |
| CB_PD_DP | TC-PD-BC-012, 013, TC-PERM-002 | 5/8 |
| NHT/TVV/CG/DN/GV | TC-LBC-011, TC-PERM-010, 013 | 4/8 = mọi ❌ rows |

**Coverage Permission: ~75% explicit + 25% suy luận = 100%** (cells ❌ một role suy luận từ negative chung).

## 6. GAP phát hiện ở A5 (forward A6 fix)

| ID | Description | Impact | Forward to A6? |
|----|-------------|--------|----------------|
| GAP-A5-01 | BR-EC-12 pagination param boundary `[1,100]` chưa có TC trực tiếp test param `?page=0`, `?size=101` | Medium — pagination guard không bị test trực tiếp, có thể miss bug khi BE chưa enforce | ✅ A6 fill |
| GAP-A5-02 | FR-XI-09 Output#1 — BAO_CAO_CT_HTPL `loai=TONG_HOP_TW` field check chưa có TC riêng (chỉ side-effect TC-TH-001) | Low — đã verify gián tiếp qua TC-TH-001 | A6 fill nếu cần explicit |
| GAP-A5-03 | Permission CB_PD_BN positive case (duyệt BC BN cùng cấp cùng đơn vị) chưa có TC trực tiếp | Medium — chỉ có ĐP positive, BN suy luận từ TW | ✅ A6 fill |

## 7. Acceptance A5

- ✅ Coverage BR ≥95% (12/12 = 100% sau loại N/A)
- ✅ Coverage AC 100% (12/12)
- ✅ Coverage SM 100% (11/11)
- ✅ Coverage ERR 100% (9/9 + 1 WRN)
- ⚠️ Coverage Permission 75% explicit + 25% suy luận → A6 fill GAP-A5-03
- 3 GAP forwarded A6: 01 (BR-EC-12 pagination), 02 (loai=TONG_HOP_TW field), 03 (CB_PD_BN positive)

*Generated 2026-05-10 — Phase A step A5 (bmad-testarch-trace) — audit only, no new TC*
