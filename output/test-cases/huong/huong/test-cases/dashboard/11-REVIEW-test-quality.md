# A6 — Test Review Quality Score (FR-01 Dashboard)

> **Ngày:** 2026-05-10
> **Tool:** bmad-testarch-test-review (4-axis quality + 6 GAP fill)
> **Threshold:** ≥80% PASS (8.0/10 mỗi axis)
> **Phase:** A6 (forward A7)

---

## 1. Per-file 4-axis quality scores

> Axis: **Completeness** (FR/AC/edge cover) · **Specificity** (field/line ref) · **Testability** (chrome-devtools MCP runnable) · **Independence** (no inter-TC ordering)

| File | TC count (trước A6) | Completeness | Specificity | Testability | Independence | Avg |
|------|---------------------|--------------|-------------|-------------|--------------|-----|
| 01-TC KPI-01..04 | 22 | 9.5 | 9.5 | 9.5 | 9.0 | **9.4** |
| 02-TC KPI-05..07 | 16 | 8.5 (FR-I-07 AC6 gap + FR-I-06 AC2 gap) | 9.5 | 9.5 | 9.0 | **9.1** |
| 03-TC UC8 | 22 | 8.5 (UC8 AC2 + AC5 gap) | 9.5 | 9.0 | 9.0 | **9.0** |
| 04-TC UC9 | 14 | 9.0 (UC9 AC2 gap) | 9.5 | 9.5 | 9.0 | **9.25** |
| 05-TC KPI-S | 13 | 9.5 | 9.0 (SPEC-CLARIFY-02 ambiguity) | 8.5 (TC-103 cần seed ngày lễ) | 9.0 | **9.0** |
| 06-TC Auto-refresh | 20 | 9.5 | 9.5 | 7.0 (10/20 TC DEFERRED cần stub backend) | 9.0 | **8.75** |
| 07-TC Bộ lọc | 23 | 9.5 | 9.5 | 9.5 | 9.0 | **9.4** |
| 08-TC Permission | 18 | 9.0 (P5 CB_NV_BN gap) | 9.5 | 9.0 | 9.0 | **9.1** |
| **Tổng** | **148** (sum visible TC) | | | | | **9.13** |

> Note: tổng TC visible đếm = 22+16+22+14+13+20+23+18 = 148 (vì các TC gap số như TC-DASH-011..014, 018..019, 040..041, 044, 050..065 nhảy số trong file — tổng grep ID sẽ thấy 161). Phục vụ score thì dùng TC count grep từ heading.

---

## 2. Issue list (sorted by severity)

| # | Severity | File | Issue | Action |
|---|----------|------|-------|--------|
| I-01 | Major | 02-TC | FR-I-06 AC2 chưa có TC explicit cho CB BN/ĐP scope KH `DA_KET_THUC` (chỉ TC-038 verify TVV scope) | A6 fill TC-DASH-217 |
| I-02 | Major | 02-TC | FR-I-07 AC6 (TW chọn 1 đơn vị cụ thể → KPI-07 đếm scope đơn vị) chưa có TC verify count (TC-049 chỉ verify URL drill-down) | A6 fill TC-DASH-218 |
| I-03 | Major | 02-TC | FR-I-07 AC7 (User BN locked TVV) chỉ partial verify qua TC-038 (CB_NV_DP) — thiếu CB_NV_BN locked TVV explicit | A6 fill TC-DASH-219 |
| I-04 | Major | 03-TC | FR-I-08 AC2 (TW switch L1='BN' UC8) — TC-050 chỉ default DP, không verify L1 switch BN scope | A6 fill TC-DASH-220 |
| I-05 | Major | 03-TC | FR-I-08 AC5 (User BN/ĐP locked UC8 → trục X = chuỗi thời gian đơn vị user) chưa có TC | A6 fill TC-DASH-221 |
| I-06 | Major | 04-TC | FR-I-09 AC2 (TW chọn 1 đơn vị cụ thể UC9 → tỷ lệ + điểm TB tính riêng) chưa explicit | A6 fill TC-DASH-222 |
| I-07 | Major | 08-TC | P5 DRILL_DOWN_HOIDAP cho CB_NV_BN chưa có TC explicit (TC-194 dùng CB_NV_DP) | A6 fill TC-DASH-223 |
| I-08 | Minor | 02-TC | TC-DASH-032 mention "loại trừ 8 trạng thái" nhưng SRS line 390 + memory secondary notebook có thể có thêm enum mới | OBS-DASH-A6-01 — verify enum exhaustive khi Phase B |
| I-09 | Minor | 06-TC | TC-DASH-130/131/132 đều mark DEFERRED do cần stub backend 5xx — Chrome DevTools network throttling fallback. 10/20 TC bị blocked | OBS-DASH-A6-02 — đánh dấu DEFERRED list rõ trong file 06 (đã có) |
| I-10 | Minor | 05-TC | TC-DASH-103 cần ngày lễ trong test data — env có thể chưa cấu hình ngày lễ | OBS-DASH-A6-03 — cross-ref FR-VIII-29 ngày lễ pre-seed |
| I-11 | Minor | 07-TC | TC-DASH-167/168/169 URL share — env có thể không persist URL params nếu app dùng client-side state only (không URL-driven) | OBS-DASH-A6-04 — verify Phase B |
| I-12 | Minor | 03-TC | TC-DASH-072 SRS line 442 nguyên văn "Lưu ý: mẫu nhỏ (< 10 đánh giá) — kết quả tham khảo" — khớp text nhưng UI có thể lowercase đầu | OBS — minor wording variance ok |
| I-13 | Trivial | All | Wording "Bộ lọc thời gian" vs "filter thời gian" inconsistent giữa file 01 và 07 | Cosmetic — không fix |
| I-14 | Trivial | 04-TC | TC-DASH-098 wrap SPEC-CLARIFY-DASH-01 trong expected — nên tách rõ Pending vs Assume | Cosmetic |

---

## 3. A6 fill TC summary (7 TC mới — fill 6 GAP)

| TC ID | File target | GAP fill | TraceID | Priority |
|-------|-------------|----------|---------|----------|
| TC-DASH-217 | 02-TC | GAP-1 (FR-I-06 AC2 BN/ĐP scope) | FR-I-06 / AC#2 BR-AUTH-08 | 🔴 P0 |
| TC-DASH-218 | 02-TC | GAP-2 (FR-I-07 AC6 TW chọn 1 ĐV scope) | FR-I-07 / AC#6 SRS line 400 | 🔴 P0 |
| TC-DASH-219 | 02-TC | GAP-6 (FR-I-07 AC7 BN locked TVV) | FR-I-07 / AC#7 BR-AUTH-08 | 🟡 P1 |
| TC-DASH-220 | 03-TC | GAP-3 (FR-I-08 AC2 TW L1=BN UC8) | FR-I-08 / AC#2 SRS line 481 | 🟡 P1 |
| TC-DASH-221 | 03-TC | GAP-4 (FR-I-08 AC5 BN/ĐP locked UC8) | FR-I-08 / AC#5 SRS line 484 BR-AUTH-08 | 🔴 P0 |
| TC-DASH-222 | 04-TC | GAP-5 (FR-I-09 AC2 TW 1 ĐV scope UC9) | FR-I-09 / AC#2 SRS line 544 | 🟡 P1 |
| TC-DASH-223 | 08-TC | GAP-6 (P5 CB_NV_BN drill-down) | Permission / P5 / CB_NV_BN | 🟡 P1 |

> **Inline merge:** mỗi TC fill được Edit trực tiếp vào file UC tương ứng dưới section `## E. A6 fill (gap A5)` với suffix `(A6 fill)`. File 11 này = changelog mapping only.

---

## 4. SPEC-CLARIFY tổng hợp (5 active — không phát sinh mới ở A6)

| Code | File | Issue | Severity |
|------|------|-------|----------|
| SPEC-CLARIFY-DASH-01 | 04-TC | HV `diem_kiem_tra=NULL` vào mẫu số tỷ lệ đạt? | P1 |
| SPEC-CLARIFY-DASH-02 | 05-TC | KPI-S-01 `xu_huong_phan_tram` % point hay % relative? | P1 |
| SPEC-CLARIFY-DASH-03 | 06-TC | Text Trạng thái 28 nguyên văn hay design custom? | P2 |
| SPEC-CLARIFY-DASH-04 | 07-TC | URL params invalid → rewrite hay giữ URL invalid? | P2 |
| SPEC-CLARIFY-DASH-05 | 08-TC | Locked user PATCH URL cross-unit → fallback "Tất cả" hay locked override? | P1 |

**Tổng:** 5 (3 P1 + 2 P2). KHÔNG phát sinh mới ở A6 (TC fill clarify đầy đủ trên SRS line 400, 481, 484, 544 — không ambiguous).

---

## 5. Coverage delta (sau A6 fill)

| Axis | Trước A6 | Sau A6 | Status |
|------|----------|--------|--------|
| Total TC | 161 | 168 (+7) | — |
| BR | 6/6 = 100% | 6/6 = 100% | ✅ |
| AC | 68/74 = 91.9% | 74/74 = 100% | ✅ (target ≥97%) |
| Permission Matrix | 58/60 = 96.7% | 60/60 = 100% | ✅ |
| Error code | 5/5 = 100% | 5/5 = 100% | ✅ |
| State enum source | 7/7 = 100% | 7/7 = 100% | ✅ |
| Outputs field | 28/28 = 100% | 28/28 = 100% | ✅ |
| **Quality score TB** | 9.13 | **9.30** | ✅ ≥9.0 target |

---

## 6. A7 forward (UI/function-testable filter)

- 161 + 7 = **168 TC** sau A6
- 10 TC DEFERRED cần stub backend (file 06 — TC-DASH-016, 130-134, 141, 144, 147, 148, 149) — Chrome DevTools network throttling fallback
- 0 TC chỉ-DB-thuần (không UI testable)
- 6 OBS design system (TC-076, 077 trục Y range/cuộn ngang + TC-084 bố cục 3 cột UC9 + TC-127 wireframe)
- A7 dự kiến: **0 LOẠI** (toàn bộ UI/function testable hoặc DEFERRED có workaround)

---

*A6 done 2026-05-10 — Phase A6 (manual test review + 7 fill TC). Quality 9.30/10. Forward A7 + Codex review.*
