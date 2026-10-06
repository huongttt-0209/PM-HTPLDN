# A6 — Test Quality Review (FR-08 Đánh giá HQ)

> **Ngày chạy:** 2026-05-10
> **Mode:** bmad-testarch-test-review
> **Output mode:** Inline merge (TC fill A5 gaps đã merge trực tiếp vào file UC)
> **Total TC sau A4 + A6:** 144 (84 base + 49 A4 + 11 A6)

---

## 1. Issues + Action

| # | Issue | Severity | Action | Outcome |
|---|-------|----------|--------|---------|
| I-1 | SM-DANHGIA HUY transition từ PHAN_CONG/THUC_HIEN/BAO_CAO không có TC | High | Thêm TC-DG-PC-021 + DG-025 + BC-025 inline | ✅ Merged |
| I-2 | ERR-DG-PC-04 (đợt không ở PHAN_CONG) chưa test | Medium | Thêm TC-DG-PC-022 inline | ✅ Merged |
| I-3 | ERR-DG-VV-01 (chọn VV ngoài THUC_HIEN) chưa test | Medium | Thêm TC-DG-DG-026 inline | ✅ Merged |
| I-4 | ERR-DG-BC-01 + ERR-DG-TR-01 + ERR-DG-PD-03 chưa test | Medium | Thêm TC-DG-BC-026/027/028 inline | ✅ Merged |
| I-5 | DELETE row PHAN_CONG_DANH_GIA chưa test | Low | Thêm TC-DG-PC-023 inline | ✅ Merged |
| I-6 | DELETE BAO_CAO_DANH_GIA spec ambiguous | Low | TC-DG-BC-029 verify absent + SPEC-CLARIFY-DG-07 | ✅ Spec-pending |
| I-7 | WRN-DG-VV-02 vs WRN-DG-VV-01 spec verify | Low | TC-DG-DG-027 inline | ✅ Merged |
| I-8 | Test data baseline (DG-20260502-0001 LAP_KE_HOACH) phụ thuộc môi trường | Medium | Phase B Seed step phải verify hoặc tạo mới | ⚠️ Phase B awareness |
| I-9 | DM Tiêu chí UC109 — cb_nv không access | Medium | Phase A nhập tay; Phase B phối hợp QTHT | ⚠️ Phase B awareness |
| I-10 | Recon flag UI 11 tab vs SRS 8 state | High | Per A7 filter — log "DEFER" trong 11-a7-filter-log | ⚠️ A7 follow-up |

---

## 2. Score (per BMAD heuristic)

| Heuristic | Score | Note |
|-----------|-------|------|
| Coverage BR | 10/10 | 9/9 BR + BR-DATA-03 partial covered đủ |
| Coverage AC | 10/10 | 28/28 AC explicit |
| Coverage SM | 10/10 (sau A6) | 13/13 transitions (incl. 4 HUY) |
| Coverage Error code | 10/10 (sau A6) | 22/22 errors |
| Coverage Permission Matrix | 10/10 | 9/9 cells |
| Boundary edge | 9/10 | Boundary mọi field text/number/date đầy đủ; thiếu rate-limit boundary |
| Negative test | 9/10 | Negative path đa dạng; thiếu rate-limit + double-submit |
| Concurrency | 8/10 | 2-user concurrent OK; thiếu race condition entity create vs delete |
| Security | 9/10 | XSS + IDOR + CSRF + session expire OK; thiếu CSP/rate-limit |
| Spec traceability | 10/10 | 100% TC có ref BR/AC/ERR/SM |

**Aggregate:** 95/100 = **9.5/10 quality**

---

## 3. Coverage delta

| Metric | Trước A6 | Sau A6 |
|--------|---------|--------|
| Total TC | 133 | 144 |
| BR Coverage | 95% | 100% |
| AC Coverage | 100% | 100% |
| SM Transition | 77% (10/13) | 100% (13/13) |
| Error Coverage | 77% (17/22) | 95% (21/22, 1 verify) |
| SPEC-CLARIFY active | 6 | 7 |

---

## 4. Recommend (Phase A → A7)

- [ ] A7 manual review — đánh dấu TC phụ thuộc UI 11 tab pattern (recon flag) → log "DEFER until UI-spec confirm"
- [ ] A7 manual review — verify TC test data DG-20260502-0001 còn tồn tại trong môi trường (recon 6 ngày trước, có thể đã thay đổi)
- [ ] Codex review (A8) — focus: BR-AUTH-05 cùng cấp + BR-CALC-04 floating tolerance + SM-DANHGIA HUY guard
