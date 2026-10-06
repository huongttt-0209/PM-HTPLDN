# 10 — A6 Test Quality Review (audit log)

> **Skill**: bmad-testarch-test-review
> **Ngày chạy**: 2026-05-09
> **Module**: FR-07 W2.1 Quản lý DN
> **Iron rule**: TC mới (fill gap A5) đã MERGE TRỰC TIẾP vào file UC tương ứng. File này CHỈ là issue list + score.

---

## A. Quality Score (10-axis)

| Axis | Score (0-10) | Notes |
|------|---:|------|
| **Coverage BR** | 10 | 11/11 BR cover 100% (BR-AUTH-01/08/EMAIL-01/USERNAME-01 + 6 BR-DATA + BR-CALC-05) |
| **Coverage AC** | 10 | 18/18 AC FR-V.III-01/02 + FR-X.1-04 cover 100% |
| **Coverage Error** | 10 | 13/13 ERR/WRN/INF code cover 100% (sau A6 fill ERR-HSPL-02) |
| **Coverage Permission** | 10 | 8/8 entity-role pair cover (sau A6 fill DN role redirect) |
| **Coverage SM** | 10 | 5/5 SM-HSPL transition (sau A6 fill HET_HAN/THU_HOI → HIEU_LUC) |
| **Test data realism** | 9 | Seed plan §D 00-overview rõ ràng, 10 loại data, account đầy đủ; -1 do chưa verify env có Excel >10K |
| **Edge case depth** | 9 | 37 edge merged inline (XSS/SQL/Concurrency/Unicode/Boundary/Soft delete invariants/Performance); -1 do thiếu chaos engineering scenarios |
| **Test independence** | 9 | Mỗi TC pre-condition độc lập; -1 do TC-LS-005/006 phụ thuộc cross-FR-05 (cần seed VV trước) |
| **Reproducibility** | 10 | Test data + step + expected rõ ràng |
| **Spec gap detection** | 10 | 27 SPEC-CLARIFY entries (DN-01..45 sparse) — đã list ở 11-a7-filter-log.md |
| **Aggregate Quality** | **9.7/10** | (97/100) |

---

## B. Issue list

### B.1 Issues fixed by A6 inline (+ 7 TC mới + 1 strengthen)

| Issue ID | Severity | File | Fix |
|----------|---|------|-----|
| GAP-A5-01 | Medium | 03-HSPL Section C | +TC-HSPL-104 SM HET_HAN→HIEU_LUC |
| GAP-A5-02 | Medium | 03-HSPL Section C | +TC-HSPL-105 SM THU_HOI→HIEU_LUC |
| GAP-A5-03 | Medium | 03-HSPL Section B | +TC-HSPL-008b ERR-HSPL-02 |
| GAP-A5-04 | Medium | 01-CRUD Section B | +TC-DN-019 BR-DATA-03 common fields |
| GAP-A5-05 | High | 06-Permission Section B | +TC-DN-PERM-008 DN role redirect CMS |
| GAP-A5-06 | Low | 01-CRUD Section B | +TC-DN-019b la_nu_lam_chu badge ưu tiên |
| GAP-A5-07 | Low | 03-HSPL Section G | Strengthen TC-HSPL-501 — verify file metadata field cấu trúc |

### B.2 Issues KHÔNG fix (defer hoặc ngoài scope)

| Issue | Severity | Lý do defer |
|-------|---|------|
| Chaos engineering (network failure mid-upload, DB connection drop) | Low | Ngoài scope manual QA, chỉ áp ở perf/load test riêng |
| Backup/restore policy | Low | Ngoài scope FR-07 |
| Audit log retention 5 năm + archive | Low | Ngoài scope test, thuộc DBA |

---

## C. SPEC-CLARIFY tổng hợp (45 entries — sẽ liệt kê đầy đủ ở 11-a7-filter-log.md)

| Category | Count |
|----------|---:|
| Module DN field/UI | 14 (DN-01..14) |
| Module HSPL field/UI | 12 (DN-12..27) |
| Permission/security | 8 (DN-19..22, 39..42) |
| Performance | 2 (DN-35) |
| Cross-module | 5 (DN-15..18, 33) |
| Wave-level (BA pending) | 4 (DN-43..45) |

> Detailed list tại `11-a7-filter-log.md` Section D

---

## D. Test Type Distribution

| Type | Count | % |
|------|---:|---:|
| Happy path 🔴 (P0 must) | 30 | 22.4% |
| Happy path 🟡 (P1 should) | 60 | 44.8% |
| Negative 🔴 | 20 | 14.9% |
| Negative 🟡 | 8 | 6.0% |
| Edge 🔴 | 8 | 6.0% |
| Edge 🟡 | 8 | 6.0% |
| **Tổng** | **134** | **100%** |

> ✅ Cân bằng: ~67% happy / ~21% negative / ~12% edge

---

## E. Action items cho Phase B

1. ⚠️ Verify SCR-V.III-03 Wizard Import: nếu UI vẫn còn → log bug Critical (UI giữ nhưng FR-V.III-NEW-01 đã BỎ)
2. ⚠️ Verify nút "Thêm mới" SCR-V.III-01: nếu vẫn còn → log bug Critical
3. ⚠️ Nút "Xuất Excel" SCR-V.III-01: kiểm tra hoạt động vì OUT D.2.1 chỉ giữ nút (không có Processing/AC) — high risk regression
4. ⚠️ Performance benchmark 10K record export: cần env có ≥10K DN
5. ⚠️ Counter sync verify cho Tab 3 KPI — nếu trigger không setup, KPI sẽ lệch

---

**— Hết 10 A6 Test Quality FR-07 —**
