# A5 — Traceability Matrix (Báo cáo Thống kê FR-11)

> **BMAD step**: A5 (`bmad-testarch-trace`)
> **Ngày**: 2026-05-10
> **Mục đích**: Map BR/AC/Error/Permission ↔ TC. Xác định gap để A6 fix.

---

## 1. BR Coverage

### 1.1 BR formal §6 srs-fr-11 (5 BR)

| BR | Tên | TC áp dụng | Status |
|----|-----|-----------|--------|
| BR-AUTH-01 | Xác thực trước truy cập | TC-BC-REP-* (precondition login mọi UC) | ✅ 100% |
| BR-AUTH-08 | Phân quyền 2-tier theo don_vi_id | TC-BC-PERM-001, 010, 011, 012, 013, 020, 021, 022, 040, 041 (10 TC file 03) | ✅ 100% |
| BR-DATA-05 | Audit trail xem/xuất BC | TC-BC-REP-010, REP-011, REP-052 | ✅ 100% |
| BR-DATA-06 | Export Excel max 10K rows | TC-BC-EXP-006 (verify thực tế cap 50K vs 10K) | ⚠️ SPEC-CLARIFY-BC-01 |
| BR-SLA-02 | 4 mức cảnh báo SLA | TC-BC-SM-03, SM-03b | ✅ 100% |

### 1.2 BR working labels (BR-RPT-*, inline)

| BR | Tên | TC áp dụng | Status |
|----|-----|-----------|--------|
| BR-RPT-01 | Chỉ bản ghi đã duyệt | TC-BC-REP-047, TC-BC-SM-XC-07 | ✅ 100% |
| BR-RPT-02 | Khoảng thời gian ≤ 366 ngày | TC-BC-REP-021, REP-040, REP-041 | ✅ 100% |

### 1.3 BR thừa kế từ master srs-v3.md

| BR | Tên | TC áp dụng | Status |
|----|-----|-----------|--------|
| BR-DATA-01 | Soft delete | TC-BC-SM-09b | ✅ |
| BR-DATA-07 | Pagination 20/page | TC-BC-REP-055 (verify hành vi data table BC) | ⚠️ SPEC-CLARIFY-BC-10 |

**BR Coverage tổng:** 7/7 explicit + 2 inheritance = **100% coverage** (2 BR có SPEC-CLARIFY pending).

---

## 2. AC Coverage

### 2.1 AC chung (TPL-REPORT-FULL — srs-fr-11:119-123)

| AC | Phát biểu | TC áp dụng | Status |
|----|-----------|-----------|--------|
| AC#1 | Given CB đăng nhập có quyền BC When chọn loại BC + kỳ + đơn vị Then hiển thị bảng dữ liệu + biểu đồ trong phạm vi đơn vị | TC-BC-REP-001, SM-01..23 | ✅ 100% |
| AC#2 | Given CB nhấn "Xuất Excel" When click Then tải file .xlsx theo TT17/2025 | TC-BC-REP-006, EXP-001 | ✅ |
| AC#3 | Given CB nhấn "Xuất PDF" When click Then tải file .pdf theo TT17/2025 | TC-BC-REP-007, EXP-010 | ✅ |
| AC#4 | Given không có dữ liệu When tạo BC Then hiển thị "Không có dữ liệu" | TC-BC-REP-022 | ✅ |

### 2.2 AC đặc thù mỗi FR-IX (23 BC × 1-2 AC bổ sung)

| FR | AC bổ sung | TC áp dụng | Status |
|----|-----------|-----------|--------|
| FR-IX-01 (UC124) | 2 AC: kỳ Quý + filter lĩnh vực | TC-BC-REP-001, REP-060, REP-061 | ✅ |
| FR-IX-02 (UC125) | 2 AC: kỳ Tháng + filter DVC | TC-BC-SM-02, SM-02b | ✅ |
| FR-IX-03 (UC126) | 2 AC: snapshot + filter QUA_HAN | TC-BC-SM-03, SM-03b | ✅ |
| FR-IX-04 (UC127) | 2 AC: kỳ Quý + filter ket_qua | TC-BC-SM-04 | ✅ |
| FR-IX-05 (UC128) | 1 AC: kỳ 6 tháng line trend | TC-BC-SM-05 | ✅ |
| FR-IX-06 (UC129) | 2 AC: snapshot + filter Trực tuyến | TC-BC-SM-06 | ✅ |
| FR-IX-07 (UC130) | 1 AC: kỳ Quý theo đơn vị + hình thức | TC-BC-SM-07 | ✅ |
| FR-IX-08 (UC131) | 2 AC: snapshot + filter CG | TC-BC-SM-08, SM-08b | ✅ |
| FR-IX-09 (UC132) | 2 AC: kỳ Năm + filter đợt | TC-BC-SM-09 | ⚠️ thiếu TC filter đợt cụ thể (gap) |
| FR-IX-10 (UC133) | 2 AC: kỳ Quý + filter KH | TC-BC-SM-10 | ⚠️ thiếu TC filter KH cụ thể (gap) |
| FR-IX-11 (UC134) | 1 AC: cross-tab TW | TC-BC-SM-11 | ✅ |
| FR-IX-12 (UC135) | 1 AC: cross-tab lĩnh vực | TC-BC-SM-12 | ✅ |
| FR-IX-13 (UC136) | 1 AC: cross-tab loại DN | TC-BC-SM-13 | ✅ |
| FR-IX-14 (UC137) | 1 AC: stacked bar 6 tháng | TC-BC-SM-14 | ✅ |
| FR-IX-15 (UC138) | 1 AC: kỳ Năm tổng CP + TB | TC-BC-SM-15 | ✅ |
| FR-IX-16 (UC139) | 1 AC: cross-tab đơn vị | TC-BC-SM-16 | ✅ |
| FR-IX-17 (UC140) | 1 AC: bảng lĩnh vực | TC-BC-SM-17 | ✅ |
| FR-IX-18 (UC141) | 1 AC: bảng loại DN + so trần | TC-BC-SM-18 | ✅ |
| FR-IX-19 (UC142) | 1 AC: line 12 tháng trend CP | TC-BC-SM-19 | ✅ |
| FR-IX-20 (UC143) | 1 AC: tổng CT theo đơn vị | TC-BC-SM-20 | ✅ |
| FR-IX-21 (UC144) | 1 AC: cross-tab đơn vị | TC-BC-SM-21 | ✅ |
| FR-IX-22 (UC145) | 1 AC: bảng lĩnh vực | TC-BC-SM-22 | ✅ |
| FR-IX-23 (UC146) | 1 AC: line trend số CT | TC-BC-SM-23 | ✅ |

**AC Coverage:** 4/4 chung + 30/32 đặc thù = **94/100% (gap 2 — FR-IX-09 + FR-IX-10 thiếu TC filter đợt/KH cụ thể)** → **A6 fill gap**.

---

## 3. Error Code Coverage

| Mã | Điều kiện | TC áp dụng | Status |
|----|-----------|-----------|--------|
| ERR-RPT-01 | tu_ngay > den_ngay | TC-BC-REP-020 | ✅ |
| ERR-RPT-02 | Khoảng > 366 ngày | TC-BC-REP-021, REP-040, REP-041 (boundary) | ✅ |
| INF-RPT-01 | Không có dữ liệu | TC-BC-REP-022 | ✅ |
| WRN-RPT-01 | Export vượt cap | TC-BC-EXP-005 | ✅ |
| ERR-RPT-03 | Timeout > 30s | TC-BC-REP-023 | ✅ (manual) |
| ERR-RPT-04 | Lỗi xuất file | TC-BC-REP-024, EXP-021 | ✅ (manual) |
| ERR-RPT-05 | Không có quyền | TC-BC-REP-025, PERM-030..034 | ✅ |
| ERR-RPT-06 | Format invalid | TC-BC-REP-026, EXP-020 | ✅ |
| ERR-RPT-07 | Template hỏng | TC-BC-REP-027 | ✅ (manual) |
| ERR-RPT-IX01-01 | Lĩnh vực không tồn tại | TC-BC-REP-028 | ✅ |

**Error Coverage:** 10/10 = **100%**.

---

## 4. Permission Matrix Coverage

| Role | Action | TC | Status |
|------|--------|-----|--------|
| QTHT | Bypass scope | TC-BC-PERM-040 | ⚠️ SPEC-CLARIFY-BC-03 |
| CB_NV_TW | Toàn quốc + filter scope bất kỳ | TC-BC-PERM-001, 002, 003 | ✅ |
| CB_NV_BN | Locked BN mình + cross-attempt 403 | TC-BC-PERM-010, 011, 012 | ✅ |
| CB_NV_DP | Locked ĐP mình + không thấy BN parent | TC-BC-PERM-020, 021, 022 | ✅ |
| CB_PD_TW | Toàn quốc | TC-BC-PERM-004 | ✅ |
| CB_PD_BN | Locked BN mình | TC-BC-PERM-013 | ✅ |
| CB_PD_DP | Locked ĐP mình | TC-BC-PERM-023 (A6 fill 2026-05-10) | ✅ resolved (Codex F-09) |
| NHT/TVV/CG/DN/GV | 403 chặn | TC-BC-PERM-030..034 | ✅ |

**Permission Coverage:** 8/8 = **100%** sau A6 fill TC-BC-PERM-023 (Codex F-09 confirmed). Bonus +1 TC unauthenticated (TC-BC-PERM-000 — Codex F-03).

---

## 5. Entity / Output Field Coverage

### BAO_CAO entity (18 columns)
- TC verify BAO_CAO state (DANG_TAO/HOAN_THANH/LOI): chỉ TC-BC-REP-051 (verify gián tiếp qua audit log) — **gap** verify trang_thai BAO_CAO entity.
- **A6 fill**: thêm TC verify trang_thai badge nếu UI có lịch sử BC, hoặc mark "DB-only — A7 LOẠI" nếu không có UI bridge.

### Output fields chung (8 fields)
- ten_bao_cao, ky_bao_cao, tu_ngay/den_ngay, don_vi_ten, ngay_tao_bc, nguoi_tao, tong_ban_ghi, data[]: TC-BC-REP-008 verify all → ✅.

### Output đặc thù mỗi FR (~7 fields/FR × 23 FR)
- Coverage qua smoke 02-TC: mỗi smoke verify ≥3-5 trường output đặc thù (theo bảng smoke). Không phải 100% deep verify nhưng đủ representative.

---

## 6. State Machine Coverage

BAO_CAO 3 trạng thái (DANG_TAO → HOAN_THANH | LOI):
- DANG_TAO → HOAN_THANH: TC-BC-REP-001 (implicit qua [Xem]).
- DANG_TAO → LOI: TC-BC-REP-024, REP-027 (BE inject) → ✅.

**SM Coverage:** 100% transitions covered.

---

## 7. Gap Forwarded to A6

| # | Gap | Severity | A6 action |
|---|-----|----------|-----------|
| G1 | FR-IX-09 thiếu TC filter "đợt đánh giá cụ thể" | 🟡 | Thêm TC-BC-SM-09c (filter ke_hoach_dg_id cụ thể) |
| G2 | FR-IX-10 thiếu TC filter "KH cụ thể" | 🟡 | Thêm TC-BC-SM-10b (filter khoa_hoc_id cụ thể) |
| G3 | CB_PD_DP scope chưa cover | 🟡 | ✅ Resolved A6: TC-BC-PERM-023 (CB_PD_DP locked ĐP) — Codex F-09 confirm |
| G4 | BAO_CAO entity trang_thai verify (DB-only?) | 🟢 | Mark A7 LOẠI hoặc verify qua UI bridge nếu có |
| G5 | SPEC-CLARIFY-BC-01 cap 50K vs 10K — verify path | 🟡 | TC-BC-EXP-006 đã cover, nhưng cần document finding A6 |

**Tổng:** 5 gaps → forward A6.

---

## 8. Coverage Summary

| Aspect | Coverage | Notes |
|--------|----------|-------|
| BR formal | 5/5 (100%) | 2 BR có SPEC-CLARIFY pending |
| BR inline | 2/2 (100%) | — |
| AC chung | 4/4 (100%) | — |
| AC đặc thù | 30/32 (94%) | 2 gap → A6 fill |
| Error code | 10/10 (100%) | — |
| Permission | 7/8 (87.5%) | 1 gap CB_PD_DP → A6 fill |
| Entity output chung | 8/8 (100%) | — |
| Entity output đặc thù | ~75% representative | OK với strategy "1 đại diện + smoke" |
| State machine | 100% | 2/2 transitions |

**Quality target:** ≥95% BR + ≥95% AC → A6 cần fill 3 gap (G1, G2, G3) để đạt 100%.

---

*Generated 2026-05-10 — Phase A step A5 (BMAD testarch-trace)*
