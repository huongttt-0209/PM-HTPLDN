# A6 — Test Quality Review (Báo cáo Thống kê FR-11)

> **BMAD step**: A6 (`bmad-testarch-test-review`)
> **Ngày**: 2026-05-10
> **Mục đích**: Review chất lượng TC theo 6 trục + fill gap A5 inline. File này CHỈ là audit log, TC mới đã merged inline vào file UC.

---

## 1. Quality Score (6 trục — Wells/IEEE 829)

| Trục | Điểm /10 | Note |
|------|----------|------|
| **Completeness** (BR/AC/Error/Permission cover) | 9.5 | 100% BR + 94→100% AC sau A6 fill + 100% Error + 100% Permission sau A6 fill |
| **Correctness** (TC vs SRS) | 9.5 | Mọi TC ref SRS line. SPEC-CLARIFY rõ 9 entry. |
| **Clarity** (TC dễ đọc, step rõ) | 9.0 | Format markdown table consistent. Step 1-N + Expected. |
| **Testability** (UI/function chạy được qua MCP) | 8.5 | 7 TC manual injection (timeout, BE error, template hỏng, 50K seed) — A7 sẽ verify UI bridge |
| **Independence** (TC độc lập, có precondition rõ) | 9.5 | Mỗi TC có pre-conditions + test data tách biệt |
| **Traceability** (TraceID + SRS line ref) | 10 | TraceID format `FR-IX-{NN} / TPL.{section}` xuyên suốt |

**Tổng: 9.33/10** ≈ **PASS** (target ≥8.5)

---

## 2. Gap fill từ A5

| Gap | A5 forward | A6 action | TC added |
|-----|-----------|-----------|----------|
| G1 | FR-IX-09 thiếu TC filter "đợt đánh giá cụ thể" | Inline merge file 02 | TC-BC-SM-09c |
| G2 | FR-IX-10 thiếu TC filter "KH cụ thể" | Inline merge file 02 | TC-BC-SM-10b |
| G3 | CB_PD_DP scope chưa cover | Inline merge file 03 | TC-BC-PERM-023 |
| G4 | BAO_CAO entity trang_thai (DB-only) | Forward A7 LOẠI nếu không UI bridge | (A7 decide) |
| G5 | SPEC-CLARIFY-BC-01 cap 50K vs 10K | TC-BC-EXP-006 đã có verify path | Document trong file 04 |

**Total A6 fill: 3 TC inline** → Coverage AC 94% → 100%, Permission 87.5% → 100%.

---

## 3. Issue list (cần Phase B chú ý)

| # | Issue | Severity | TC ref | Action |
|---|-------|----------|--------|--------|
| I1 | Manual injection TC khó reproduce qua chrome-devtools MCP | 🟡 | REP-023, 024, 027, EXP-021 | Phase B mark `MANUAL-EVIDENCE` — log finding nếu BE đã có inject hook |
| I2 | Manual seed 50K rows (REP cap test) | 🟡 | EXP-004, 005 | Phase B SPEC-CLARIFY-BC-07 confirm môi trường có data 50K hoặc skip |
| I3 | Snapshot consistency (UC126/129/131) phụ thuộc data sống | 🟢 | SM-03, SM-03c, SM-06, SM-08 | Phase B ghi rõ "Data sống thời điểm test" trong execution-report |
| I4 | Phụ thuộc 9 module nguồn có DA_DUYET data | 🔴 | Toàn bộ smoke 02-TC | Phase B BLOCK 🚫 cho đến khi 9 module có data DA_DUYET (per todo.md W5.2 B note) |

---

## 4. SPEC-CLARIFY summary (10 entries — pending BA)

| ID | Câu hỏi | TC ref | Status |
|----|---------|--------|--------|
| SPEC-CLARIFY-BC-01 | Cap rows 50K (TPL) vs 10K (BR-DATA-06) | EXP-006 | **Resolved** per memory feedback "UI vs business → theo business" 2026-05-08 (TPL more specific cho IX, default 50K) |
| SPEC-CLARIFY-BC-02 | E9 ERR-RPT-07 reproducibility | REP-027 | Pending (manual injection only) |
| SPEC-CLARIFY-BC-03 | QTHT bypass BR-AUTH-08? | PERM-040 | Pending |
| SPEC-CLARIFY-BC-04 | PDF font Times New Roman fallback? | EXP-011 | Pending |
| SPEC-CLARIFY-BC-05 | API outbound BC nào? | — | Pending (skip — không UI) |
| SPEC-CLARIFY-BC-06 | Export khi empty data — disable nút hay xuất rỗng? | REP-042 | Pending |
| SPEC-CLARIFY-BC-07 | Môi trường test có data 50K rows nguồn không? | EXP-004 | Pending (env-related) |
| SPEC-CLARIFY-BC-08 | PDF cap rows giống XLSX? | EXP-013 | Pending |
| SPEC-CLARIFY-BC-09 | SCR-IX-01 mobile responsive? | CHART-042 | Pending |
| SPEC-CLARIFY-BC-10 | Pagination data table BC? | REP-055 | Pending (BR-DATA-07 inheritance) |

**9 SPEC-CLARIFY pending BA + 1 RESOLVED per memory.**

---

## 5. Iron Rule check

✅ Mọi TC mới (A6 fill 3 TC) đã merged inline vào file UC.
✅ File 10 này CHỈ là audit log (issue list + score + gap fill mapping). KHÔNG chứa TC source.
✅ Quality score 9.33/10 đạt threshold (≥8.5 PASS).

---

## 6. TC count tổng cộng (sau A4 + A6)

| File | Base A3 | A4 merged | A6 fill | Final |
|------|---------|-----------|---------|-------|
| 01-TC-tpl-report-full-representative.md | 32 | +7 (049-055) | — | 39 |
| 02-TC-smoke-23-loai-bc.md | 34 | +4 (XC-09/10, SM-03c, SM-09b) | +2 (SM-09c, SM-10b) | 40 |
| 03-TC-permission-2tier-bc.md | 17 | — | +1 (PERM-023) | 18 |
| 04-TC-export-xlsx-pdf-tt17.md | 15 | +4 (EXP-024..027) | — | 19 |
| 05-TC-bieu-do-charts.md | 12 | — | — | 12 |
| **Tổng** | **110** | **+15** | **+3** | **128 TC** |

**Phase A est ~80 TC theo todo.md → actual 128 TC** (+60% do template-driven cover deep + 23 BC smoke + edge cases).

---

*Generated 2026-05-10 — Phase A step A6 (BMAD testarch-test-review)*
