# A5 — Traceability Matrix BR/AC ↔ TC (FR-08 Đánh giá HQ)

> **Ngày chạy:** 2026-05-10 (revised after A6 + Codex apply)
> **Mode:** bmad-testarch-trace (audit only — KHÔNG sinh TC mới)
> **Output:** Gap list forward sang A6 fix → all resolved + Codex apply +23 TC
> **Total TC sau A4 + A6 + Codex:** 167 (84 base + 49 A4 + 11 A6 + 23 Codex)

---

## 1. BR Coverage Matrix

| BR ID | Tên | TC ref | Coverage |
|-------|-----|--------|----------|
| BR-AUTH-01 | Xác thực truy cập | TC-DG-PERM-001/002, KH-006 (login precondition) | ✅ 100% |
| BR-AUTH-05 | Phê duyệt cùng cấp | TC-DG-PC-008/011, BC-008/011, PERM-005/006 | ✅ 100% |
| BR-AUTH-08 | Phân quyền dữ liệu theo `don_vi_id` | TC-DG-PC-006, DG-002, NK-003, PERM-004/006/011 | ✅ 100% |
| BR-CALC-04 | Tổng trọng số tiêu chí = 100% | TC-DG-TC-002/003/004/005/011/013/016, DG-005/011 | ✅ 100% |
| BR-DATA-03 | Common fields | TC-DG-KH-006 (created_by), KH-013 (is_deleted) | ✅ 80% |
| BR-DATA-04 | Auto-gen mã DG-{YYYYMMDD}-{SEQ} | TC-DG-KH-006/023/024 | ✅ 100% |
| BR-DATA-05 | Audit trail INSERT-only | TC-DG-KH-006/011/013/015, PC-008/010, BC-008/010 | ✅ 100% |
| BR-FLOW-04 | Lý do từ chối ≥10 ký tự | TC-DG-PC-009/010/015/016/017, BC-009/010/015/016 | ✅ 100% |
| BR-LEGAL-08 | Tần suất ĐG: sơ bộ 6T + tròn năm | TC-DG-KH-009/010 | ✅ 100% |
| BR-NOTIF-01 | TB phê duyệt | TC-DG-PC-007/008/010, BC-006/008/010, PERM-007/008 | ✅ 100% |

**BR Coverage:** 9/9 explicit + 1/1 BR-DATA-03 partial = **9.5/10 = 95%**

---

## 2. AC Coverage Matrix (per FR)

### FR-VI-01 (Lập KH) — 4 AC

| # | AC | TC ref |
|---|----|--------|
| AC-1 | List KH thuộc đơn vị, phân trang | TC-DG-KH-001/018, PERM-004 ✅ |
| AC-2 | Thêm mới + validate + LAP_KE_HOACH | TC-DG-KH-006 ✅ |
| AC-3 | Chỉnh sửa KH chưa duyệt | TC-DG-KH-011 ✅ |
| AC-4 | Xóa KH chưa duyệt + soft delete | TC-DG-KH-013/024 ✅ |

**Coverage:** 4/4 = 100%

### FR-VI-02 (Tiêu chí) — 2 AC
- AC §UC84: Hiển thị DS tiêu chí khi mở Tab → TC-DG-TC-001 ✅
- AC §UC84: Validate tổng = 100% khi lưu → TC-DG-TC-005 ✅

### FR-VI-03 (Phân công) — 3 AC
- AC: DS CB/CG đủ điều kiện cùng đơn vị → TC-DG-PC-006 ✅
- AC: Lưu phân công + gửi TB → TC-DG-PC-002/007 ✅
- AC: Trình duyệt → CHO_DUYET_PC → TC-DG-PC-007 ✅

### FR-VI-04 (Duyệt PC) — 3 AC
- AC: Xem DS PC chờ duyệt → TC-DG-PC-008 ✅
- AC: Duyệt → THUC_HIEN → TC-DG-PC-008 ✅
- AC: Từ chối + lý do → trả PHAN_CONG → TC-DG-PC-010 ✅

### FR-VI-05 (Chọn VV) — 3 AC
- AC: DS VV HOAN_THANH trong kỳ → TC-DG-DG-001/002 ✅
- AC: Chọn → lưu DS VV → TC-DG-DG-004 ✅
- AC: VV đã thuộc đợt khác → cảnh báo → TC-DG-DG-003 ✅

### FR-VI-06 (Chấm điểm) — 2 AC
- AC: Form nhập điểm theo tiêu chí → TC-DG-DG-001/004 ✅
- AC: Lưu điểm + tính tổng hợp → TC-DG-DG-005/011 ✅

### FR-VI-07 (Lập BC) — 3 AC
- AC: Sinh BC + tổng hợp số liệu → TC-DG-BC-001/002 ✅
- AC: Chỉnh sửa BC → lưu → TC-DG-BC-003/004/005 ✅
- AC: Xuất BC → tải file → TC-DG-BC-012/013 ✅

### FR-VI-08 (Trình BC) — 2 AC
- AC: Trình BC hoàn chỉnh → CHO_PHE_DUYET + TB CB PD → TC-DG-BC-006 ✅
- AC: BC thiếu dữ liệu → cảnh báo → TC-DG-BC-007/022 ✅

### FR-VI-09 (Duyệt BC) — 4 AC
- AC: Xem BC chờ duyệt → TC-DG-BC-008 ✅
- AC: Duyệt → HOAN_THANH → TC-DG-BC-008 ✅
- AC: Từ chối + lý do → BAO_CAO → TC-DG-BC-010 ✅
- AC: Hiển thị KQ phê duyệt (trạng thái + người + thời gian + lý do) → TC-DG-BC-008/023 ✅

### FR-VI-10 (Nhận KQ) — 2 AC
- AC: User thuộc cơ quan ĐG xem KQ → TC-DG-NK-001 ✅
- AC: User cơ quan khác → từ chối → TC-DG-NK-003 ✅

**AC Coverage Total:** 28/28 = **100%**

---

## 3. SM-DANHGIA Transition Coverage

| # | Transition | TC ref | Coverage |
|---|-----------|--------|----------|
| 1 | [*] → LAP_KE_HOACH | TC-DG-KH-006 | ✅ |
| 2 | LAP_KE_HOACH → PHAN_CONG | TC-DG-PC-002 | ✅ |
| 3 | PHAN_CONG → CHO_DUYET_PC | TC-DG-PC-007/014 | ✅ |
| 4 | CHO_DUYET_PC → THUC_HIEN | TC-DG-PC-008/014 | ✅ |
| 5 | CHO_DUYET_PC → PHAN_CONG | TC-DG-PC-010/014 | ✅ |
| 6 | THUC_HIEN → BAO_CAO | TC-DG-DG-010 | ✅ |
| 7 | BAO_CAO → CHO_PHE_DUYET | TC-DG-BC-006/014 | ✅ |
| 8 | CHO_PHE_DUYET → HOAN_THANH | TC-DG-BC-008/014 | ✅ |
| 9 | CHO_PHE_DUYET → BAO_CAO | TC-DG-BC-010/014/024 | ✅ |
| 10 | LAP_KE_HOACH → HUY | TC-DG-KH-015 | ✅ |
| 11-13 | PHAN_CONG/THUC_HIEN/BAO_CAO → HUY | ⚠️ GAP — chỉ test từ LAP_KE_HOACH | ❌ Forward A6 |

**SM Coverage:** 10/13 explicit + GAP 3 transition HUY → **77% — A6 fill**

---

## 4. Error Code Coverage

| ERR ID | TC ref |
|--------|--------|
| ERR-DG-KH-01 | TC-DG-KH-007 ✅ |
| ERR-DG-KH-02 | TC-DG-KH-008/022 ✅ |
| ERR-AUTH-01 | TC-DG-PERM-005 (cross-cấp) ✅ |
| ERR-DG-TC-01 | TC-DG-TC-005/013, PC-018 ✅ |
| ERR-DG-TC-02 | TC-DG-DG-012 ✅ |
| ERR-DG-TC-03 | TC-DG-TC-009 ✅ |
| ERR-DG-PC-01 | TC-DG-PC-004 ✅ |
| ERR-DG-PC-02 | TC-DG-PC-003 ✅ |
| ERR-DG-PC-03 | TC-DG-PC-005 ✅ |
| ERR-DG-PC-04 | ⚠️ GAP — chưa test "đợt không ở PHAN_CONG → block thêm phân công" → Forward A6 |
| ERR-DG-PD-01 | TC-DG-PC-012 ✅ |
| ERR-DG-PD-02 | TC-DG-PC-009 ✅ |
| WRN-DG-VV-01 | TC-DG-DG-014 ✅ |
| ERR-DG-VV-01 | ⚠️ GAP — chưa test "chọn VV khi đợt không THUC_HIEN" → Forward A6 |
| ERR-DG-DG-01 | TC-DG-DG-006/007 ✅ |
| WRN-DG-VV-02 | ⚠️ Duplicate WRN-DG-VV-01 (renumbered)? → Forward A6 verify |
| ERR-DG-BC-01 | ⚠️ GAP — chưa test "Lập BC khi state != BAO_CAO" → Forward A6 |
| ERR-DG-TR-01 | ⚠️ GAP — chưa test ERR-DG-TR-01 explicit → Forward A6 |
| WRN-DG-TR-01 | TC-DG-BC-007/022 ✅ |
| ERR-DG-PD-03 | ⚠️ GAP — chưa test "Duyệt BC khi state != CHO_PHE_DUYET" → Forward A6 |
| ERR-DG-PD-04 | TC-DG-BC-009 ✅ |
| ERR-DG-10 | TC-DG-NK-003 ✅ |
| ERR-DG-11 | TC-DG-NK-004/007 ✅ |

**Error Coverage:** 17/22 explicit = **77% — 5 gap forward A6**

---

## 5. Permission Matrix Coverage

| Cell | TC ref | Coverage |
|------|--------|----------|
| qtht read-only | TC-DG-PERM-003 | ✅ |
| cb_nv_tw CRUD scope TW | Toàn bộ file 01 | ✅ |
| cb_nv_bn CRUD scope BN (cross-unit) | TC-DG-PERM-006 | ✅ |
| cb_nv_dp CRUD scope ĐP (cross-unit) | TC-DG-PERM-004 | ✅ |
| cb_pd duyệt cùng cấp | TC-DG-PC-008/011, BC-008/011 | ✅ |
| cg/nht chấm khi được PC | TC-DG-DG-005/013 | ✅ |
| tvv 403 | TC-DG-PERM-001 | ✅ |
| dn 403 | TC-DG-PERM-002 | ✅ |
| FR-VI-10 cơ quan được ĐG | TC-DG-NK-001/003 | ✅ |

**Permission Coverage:** 9/9 = **100%**

---

## 6. Entity CRUD Coverage

| Entity | C | R | U | D |
|--------|---|---|---|---|
| KE_HOACH_DANH_GIA | KH-006 ✅ | KH-001/016 ✅ | KH-011 ✅ | KH-013 ✅ |
| TIEU_CHI_DANH_GIA (per đợt) | TC-002/003 ✅ | TC-001 ✅ | TC-006 ✅ | TC-007 ✅ |
| PHAN_CONG_DANH_GIA | PC-002 ✅ | PC-001 ✅ | PC-013 (read-only post-trinh) ✅ | ⚠️ GAP — DELETE row phân công → Forward A6 |
| KET_QUA_DANH_GIA | DG-005 ✅ | DG-011 ✅ | DG-008 (lưu nháp) ✅ | DG-024 (deselect VV → xóa KQ) ✅ |
| BAO_CAO_DANH_GIA | BC-001 (auto on state BAO_CAO) ✅ | BC-001 ✅ | BC-003/004/005 ✅ | ⚠️ GAP — DELETE BC? Spec không cho phép explicit → Forward A6 verify |

**CRUD Coverage:** 4/5 entities full + 2 gap → **88%**

---

## 7. GAP forward A6 (TC mới cần fill)

| GAP # | Mô tả | TC dự kiến |
|-------|-------|-----------|
| GAP-A5-01 | SM-DANHGIA HUY transition từ PHAN_CONG | TC mới ở file 01 hoặc 03 |
| GAP-A5-02 | SM-DANHGIA HUY transition từ THUC_HIEN | TC mới ở file 04 |
| GAP-A5-03 | SM-DANHGIA HUY transition từ BAO_CAO | TC mới ở file 05 |
| GAP-A5-04 | ERR-DG-PC-04 (đợt không ở PHAN_CONG) | TC mới ở file 03 |
| GAP-A5-05 | ERR-DG-VV-01 (đợt không ở THUC_HIEN khi chọn VV) | TC mới ở file 04 |
| GAP-A5-06 | ERR-DG-BC-01 (lập BC khi state != BAO_CAO) | TC mới ở file 05 |
| GAP-A5-07 | ERR-DG-TR-01 (trình BC khi state != BAO_CAO) | TC mới ở file 05 |
| GAP-A5-08 | ERR-DG-PD-03 (duyệt BC khi state != CHO_PHE_DUYET) | TC mới ở file 05 |
| GAP-A5-09 | DELETE PHAN_CONG_DANH_GIA row | TC mới ở file 03 |
| GAP-A5-10 | DELETE/Cancel BAO_CAO_DANH_GIA (verify spec) | TC mới ở file 05 hoặc SPEC-CLARIFY |
| GAP-A5-11 | WRN-DG-VV-02 vs WRN-DG-VV-01 — verify duplicate code | A6 verify |

**Total: 10 GAP TC + 1 spec verify** → forward A6.

---

## 8. Summary (revised post A6 + Codex)

| Metric | Pre-A6 | Post-A6 | Post-Codex |
|--------|--------|---------|-----------|
| BR Coverage | 95% (9.5/10) | 100% (10/10) | 100% (10/10) |
| AC Coverage | 100% (28/28) | 100% (28/28) | 100% (28/28) |
| SM Transition | 77% (10/13) | 100% (13/13) | 100% (13/13) |
| Error Code | 77% (17/22) | 95% (21/22) | 100% (22/22 — ERR-DG-TC-02 + WRN-DG-VV-02 added) |
| Permission Matrix (cells) | 90% (9/10 broad) | 90% | 95% (16 TC after Codex F-006) |
| Entity CRUD | 88% (12/14) | 95% (13/14, 1 SPEC) | 95% |
| **Aggregate** | **89.5%** | **96.7%** | **98.3%** |

## 9. Codex apply summary (2026-05-10)

- 4 P0 fixed: ERR-DG-TC-02 (F-001), WRN-DG-VV-02 executable (F-002), ERR-AUTH-01 wording (F-003), WRN-DG-TR-01 deterministic (F-004)
- 16 P1 applied: F-005..F-020 (one fix per finding)
- 10 P2 applied: F-021..F-030
- TC delta: 144 → 167 (+23 TC = 7 file 01 + 3 file 02 + 5 file 03 + 2 file 04 + 3 file 05 + 0 file 06 + 5 file 07; 4 TC EDIT inline TC-DG-DG-020/021/024/027 + TC-DG-BC-007/022/023 + TC-DG-NK-005/006 + TC-DG-PC-011 + TC-DG-PERM-005)
- 1 SPEC-CLARIFY mới (DG-08 deselect VV)
- 1 SPEC-CLARIFY RESOLVED (DG-01 read-only mode)
