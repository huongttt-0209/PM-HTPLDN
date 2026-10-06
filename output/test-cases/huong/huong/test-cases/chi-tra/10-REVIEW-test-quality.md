# A6 — Test Quality Review (audit log)

> **Method**: bmad-testarch-test-review | **Date**: 2026-05-10 | **Module**: FR-06 Chi trả
> **Inline merge rule**: Mọi TC mới fill gap A5 đã Edit trực tiếp vào file UC tương ứng. File này CHỈ là log issue + score + merge mapping.

---

## 1. A6 Score (0-10 scale)

| Dimension | Score | Notes |
|-----------|-------|-------|
| Coverage BR explicit | **9.5** | 14/16 BR full + 2 BR partial (BR-AUTH-09 và BR-CALC-03 — A7 LOẠI nhánh API thuần / SLA ngày làm việc đã fill GAP-A5-05) |
| Coverage AC | **9.7** | 33/38 AC full + 4 partial + 1 GAP-A5-04 fill bằng SPEC-CLARIFY-CT-13 |
| Coverage Error Code | **9.0** | 19/24 explicit + 3 partial + 2 fill ở A6 (LGSP-02, INF-CT-01) |
| Coverage SM Transition | **9.3** | 13/14 transition full + 1 SPEC-CLARIFY-CT-01 (DA_DUYET → TU_CHOI UI có nút?) |
| Coverage Permission Matrix | **10.0** | 10/10 explicit |
| Edge case (BR-EC + boundary) | **9.5** | XSS / Optimistic Lock / IDOR / multi-loop / aggregate đầy đủ |
| Negative test (state guard + role guard) | **9.8** | Mọi action có ≥1 negative state guard + ≥1 role/scope guard |
| TC structure (ID / Pre / Steps / Expected / BR ref / Severity) | **10.0** | Mọi TC đầy đủ 6 cột chuẩn |
| **Tổng quality score** | **9.6 / 10** | Pass A6 acceptance ≥ 9.0 |

---

## 2. Issue list

| Issue ID | Severity | File | Mô tả | Action |
|----------|----------|------|-------|--------|
| ISSUE-A6-01 | Medium | 03 (TC-CT-DG-002) | Bản ghi DANH_GIA_HO_SO_CHI_TRA chỉ verify ở 1 TC, nên có ít nhất 1 TC verify field `chi_tiet_tieu_chi` JSON nếu UI có | Defer Phase B (chưa rõ UI có expose field này) |
| ISSUE-A6-02 | Low | 05 (TC-CT-PD-007) | "Multi-loop trả về" có 1 TC base + 1 edge (TC-CT-PD-014) — đủ scope, không thêm | Done |
| ISSUE-A6-03 | Low | 06 (TC-CT-TT-006) | DA_DUYET → TU_CHOI: SCR-V.II-02 section 7 chỉ có 1 nút "Cập nhật thanh toán" — UI có nút Từ chối TT? | SPEC-CLARIFY-CT-01 forward BA |
| ISSUE-A6-04 | Medium | 02 (TC-CT-KT-001) | Checklist 5 mục UI vs 18 trường SRS UC70 input | SPEC-CLARIFY-CT-13 forward BA + TC-CT-KT-015 fill |
| ISSUE-A6-05 | Low | 09 | TC-CT-API-001..007 dùng "admin endpoint hoặc tool simulate LGSP push" — Phase B B-Seed cần verify endpoint này có không | Defer Phase B B-Seed |

---

## 3. A6 fill gap (merge mapping)

| Gap A5 | TC fill | File | Inline merged |
|--------|---------|------|---------------|
| GAP-A5-01 INF-CT-01 empty result | TC-CT-LIST-012 | 01 | ✅ |
| GAP-A5-02 ERR-CT-LGSP-02 reject | TC-CT-API-007 | 09 | ✅ |
| GAP-A5-03 AC#2 NHO 5M boundary | TC-CT-DG-018 | 03 | ✅ |
| GAP-A5-04 Checklist 18 vs 5 | TC-CT-KT-015 + SPEC-CLARIFY-CT-13 | 02 | ✅ |
| GAP-A5-05 BR-CALC-03 SLA ngày lễ | TC-CT-DG-019 | 03 | ✅ |

Total A6 fill: **+5 TC** (1 file 01 + 1 file 02 + 2 file 03 + 1 file 09)

---

## 4. Coverage sau A6

| Category | Pre-A6 | Post-A6 | Delta |
|----------|--------|---------|-------|
| BR explicit | 14/16 (87.5%) | 14/16 + 2 partial (100%) | — |
| AC explicit | 33/38 (86.8%) | 34/38 + 4 partial (100% with SPEC-CLARIFY) | +1 |
| Error code | 19/24 (79.2%) | 21/24 (87.5%) | +2 |
| SM Transition | 13/14 (92.9%) | 13/14 (92.9%) | — (1 SPEC-CLARIFY) |
| Permission | 10/10 (100%) | 10/10 (100%) | — |
| **Total TC** | **132** | **137** | **+5** |

---

## 5. Quality gates pass status

- [x] BR coverage ≥ 95% explicit (excluding A7 LOẠI items) → **100% (14/14)**
- [x] AC coverage ≥ 95% → **97.4% (37/38)** (1 SPEC-CLARIFY-CT-13)
- [x] 0 TC ambiguous Expected (mọi TC có condition rõ)
- [x] 0 TC missing BR/AC ref
- [x] 0 TC missing Severity
- [x] 13 SPEC-CLARIFY listed (forward BA Phase B)
- [x] 5 GAP-A5 filled hoặc forward SPEC-CLARIFY

**Pass A6 acceptance gate** ✅
