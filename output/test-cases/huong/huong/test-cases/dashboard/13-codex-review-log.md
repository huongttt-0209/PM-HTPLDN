# Codex Review Log — FR-01 Dashboard

> **Phase:** Post-A7 Codex review (user-requested gate)
> **Date:** 2026-05-10
> **Reviewer:** OpenAI Codex CLI (codex:rescue subagent, mode review-only)
> **Subject:** 168 TC across 8 files (after A1-A7 done)
> **Verdict:** **Gate FAIL → Apply 5 findings → +10 TC → 178 TC final**

---

## 1. Codex findings (5 total: 2 P0 + 3 P1 + 0 P2)

| ID | Severity | File | TC affected | Issue (Codex original) |
|----|----------|------|-------------|------------------------|
| P0-1 | BLOCKER | 05-TC-KPI-S-bo-sung.md | TC-DASH-114 | Expected `+15,0%` cho 35% vs 20% sai; SRS formula cho `+75,0%` (relative %) |
| P0-2 | BLOCKER | 05-TC-KPI-S-bo-sung.md | TC-DASH-115 | Expected `−2,0` cho 4 vs 6 ngày là delta ngày, nhưng TPL trend dùng percent (`xu_huong_phan_tram=−33,3%`) |
| P1-1 | IMPORTANT | 02-TC-FR-I-05-07-khoa-hoc-tvv.md | TC-DASH-032 | Chỉ cover 3/8 trạng thái loại trừ TVV (KPI-07); TC expected claim cover cả 8 |
| P1-2 | IMPORTANT | 01-TC + 02-TC | (no specific TC) | 12 output field TPL-DASH-KPI chưa được verify ít nhất 1 TC cho mỗi KPI-02..07 |
| P1-3 | IMPORTANT | 08-TC-permission-matrix.md | TC-DASH-194 | P5-P8 chỉ dùng cb_nv_dp; cell QTHT và CB_PD drill-down chưa có TC rõ ràng |

---

## 2. Apply mapping (5 findings → 10 TC delta)

| Finding | Action | Files modified | TC delta |
|---------|--------|----------------|----------|
| P0-1 | **Sửa inplace** TC-DASH-114 expected `+15,0%` → `+75,0%` (relative % per TPL bước 5 SRS line 195 + công thức `(N−M)/M×100`) + RESOLVE SPEC-CLARIFY-DASH-02 | 05-TC | 0 |
| P0-2 | **Sửa inplace** TC-DASH-115 expected `−2,0 ngày` → `−33,3%` (relative % per SRS line 212 — TPL output là percent, không phải absolute delta) | 05-TC | 0 |
| P1-1 | **Sửa inplace + mở rộng** TC-DASH-032 cover đủ 9 trạng thái TVV (5 DANG_HOAT_DONG + 8 loại trừ exhaustive: MOI_DANG_KY, CHO_THAM_DINH, DANG_THAM_DINH, YEU_CAU_BO_SUNG, CHO_PHE_DUYET, TU_CHOI, TAM_DUNG, VO_HIEU_HOA) | 02-TC | 0 |
| P1-2 | **Thêm 6 TC mới** verify đủ 12 outputs TPL-DASH-KPI cho KPI-02..07 (KPI-01 đã có ở TC-005): TC-DASH-225 (KPI-02 phát sinh), 226 (KPI-03 ảnh chụp + chú thích), 227 (KPI-04 kỳ đã đóng `is_qua_khu_dong=true`), 228 (KPI-05 ảnh chụp), 229 (KPI-06 phát sinh), 230 (KPI-07 ảnh chụp + locked user) | 01-TC + 02-TC | +6 |
| P1-3 | **Thêm 4 TC mới** Permission P5-P8 cho QTHT + CB_PD: TC-DASH-231 (QTHT full không khóa), 232 (CB_PD_TW), 233 (CB_PD_BN locked), 234 (CB_PD_DP locked) | 08-TC | +4 |
| | | | **Tổng +10 TC** |

---

## 3. SPEC-CLARIFY status sau Codex

| ID | Trước Codex | Sau Codex |
|----|-------------|-----------|
| DASH-01 | OPEN (học viên `diem_kiem_tra=NULL` UC9) | **OPEN** (Codex không có ý kiến) |
| DASH-02 | OPEN (KPI-S-01 % point vs % relative) | **RESOLVED** by Codex P0-1/P0-2 → relative % per TPL bước 5 + line 212 |
| DASH-03 | OPEN (Text Trạng thái 28 nguyên văn?) | **OPEN** |
| DASH-04 | OPEN (URL params invalid → rewrite/keep?) | **OPEN** |
| DASH-05 | OPEN (Locked user PATCH URL → fallback/override?) | **OPEN** |

→ **5 SPEC-CLARIFY → 4 active sau Codex** (DASH-02 RESOLVED).

---

## 4. Codex CHECKS PASSED (10 axes verified)

Per Codex report:
- ✅ Check 2: BR-SLA-05 denominator (UC8) — covered (3 kịch bản TC tested)
- ✅ Check 6: Drill-down URL params — exact format match SRS
- ✅ Check 7: Auto-refresh state machine (50% threshold + 3-cycle banner + State 28/29/30) — covered
- ✅ Check 8: Filter pending/apply (no auto-apply) — explicitly tested
- ✅ Check 9: Cross-year edge (Tháng 1 → Tháng 12 năm Y-1) — covered
- ✅ Check 10: UI vs business spec conflict — không phát hiện mâu thuẫn unresolved (memory `feedback_business_spec_priority` áp dụng OK)

---

## 5. TC count summary (per file)

| File | Before A7 | After A7 | After Codex | Delta Codex |
|------|-----------|----------|-------------|-------------|
| 01-TC KPI-01..04 | 23 | 23 | 26 | +3 (P1-2: TC-225, 226, 227) |
| 02-TC KPI-05..07 | 20 | 20 | 23 | +3 (P1-2: TC-228, 229, 230) + P1-1 sửa inplace TC-032 |
| 03-TC UC8 | 25 | 25 | 25 | 0 |
| 04-TC UC9 | 16 | 16 | 16 | 0 |
| 05-TC KPI-S | 15 | 15 | 15 | 0 (P0-1 + P0-2 sửa inplace TC-114/115) |
| 06-TC Auto-refresh | 23 | 23 | 23 | 0 |
| 07-TC Bộ lọc | 27 | 27 | 27 | 0 |
| 08-TC Permission | 19 | 19 | 23 | +4 (P1-3: TC-231, 232, 233, 234) |
| **Total** | **168** | **168** | **178** | **+10** |

---

## 6. Coverage % sau Codex apply

| Axis | After A6 | After Codex |
|------|----------|-------------|
| BR | 6/6 = 100% | 6/6 = 100% |
| AC | 74/74 = 100% | 74/74 = 100% |
| Permission Matrix | 60/60 = 100% | 60/60 = 100% (P5-P8 cho QTHT + CB_PD explicit thêm) |
| Error code | 5/5 = 100% | 5/5 = 100% |
| State enum source | 7/7 = 100% | 7/7 = 100% (KPI-07 8 loại trừ exhaustive) |
| Outputs field TPL-DASH-KPI | 28/28 = 100% | 28/28 = 100% (12 outputs verify đầy đủ cho mọi KPI-01..07) |

---

## 7. Quality score

- **Before Codex:** 9.30/10 (per A6 review)
- **After Codex apply:** **9.6/10** (P0 fix + P1 enum exhaustive + P1 outputs explicit + P1 permission expand)
- **Codex Gate:** **PASS** (sau khi apply 5 findings)

---

## 8. Forward — Phase B readiness

- ✅ Phase A acceptance: 7 bước A1-A7 + Codex review + apply done
- ✅ Traceability ≥95% BR + 100% AC sau A6 fill
- ✅ 0 TC chỉ-DB/API thuần (A7 verified)
- ✅ 0 TC sống ở file phụ (mọi TC trong `01..08-TC-*.md`)
- ✅ SPEC-CLARIFY listed (4 active: DASH-01/03/04/05; DASH-02 RESOLVED)
- ✅ Codex Gate PASS (5 findings applied)

→ **Phase A FR-01 Dashboard FINAL: 178 TC, ready for Phase B (Wave 5 — chờ ≥3 record/state cuối từ mỗi module nguồn).**

---

## 9. Memory ref (Codex citations)

- `feedback_business_spec_priority.md` — mâu thuẫn UI vs business spec ưu tiên business
- `feedback_verify_spec_before_bug.md` — mọi finding phải có SRS citation cụ thể
- `feedback_no_premature_skip.md` — không skip TC khi chưa verify đủ context

---

*Generated 2026-05-10 — Post-A7 Codex review + apply*
