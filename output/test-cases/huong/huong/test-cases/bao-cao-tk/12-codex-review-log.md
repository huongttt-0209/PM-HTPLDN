# Codex Review Log — FR-11 Báo cáo Thống kê

> **Trigger**: Sau Phase A A1-A7 done 2026-05-10 — user yêu cầu "/codex review TC vs SRS, sau đó update theo review".
> **Source of truth**: `srs-fr-11-bao-cao-v3.1.md` (1284 lines)
> **Reviewer**: Codex (subagent codex:codex-rescue) — model gpt-5.3-codex-spark default
> **Status**: ✅ ALL 9 findings APPLIED 2026-05-10

---

## Findings + Apply log

| ID | Severity | Finding | Apply action | TC affected |
|----|----------|---------|--------------|-------------|
| **F-01** | **P0** | BR-DATA-06 formal §6 line 1274 cap 10K rows (authoritative). TPL inline line 85 + 112 nói 50K — mâu thuẫn. Memory feedback "UI vs business" KHÔNG áp dụng (đây là TPL inline vs BR formal). | ✅ Đổi 50K → 10K trong file 04 (EXP-004/005/006) + 00 + RE-OPEN SPEC-CLARIFY-BC-01 | EXP-004 (10K boundary), EXP-005 (10K+1 cap WRN), EXP-006 (verify path 10K vs 50K) |
| **F-02** | P1 | TC-BC-EXP-013 PDF cap để pending, BR-DATA-06 áp dụng "mọi danh sách có tính năng xuất" → PDF cũng phải cap 10K. | ✅ Sửa expected EXP-013 deterministic: `data=10,001, format=PDF, Expected: WRN-RPT-01 + PDF chỉ 10K rows + header/footer TT17 đúng` | EXP-013 |
| **F-03** | P1 | BR-AUTH-01 line 1256 yêu cầu xác thực — coverage hiện chỉ login precondition, thiếu unauthenticated test. | ✅ Thêm TC-BC-PERM-000 unauthenticated → /bao-cao redirect /login hoặc 401 | PERM-000 NEW |
| **F-04** | P1 | BR-SLA-02 mâu thuẫn ngưỡng %: FR-IX-03 line 249 (`<50%` = bình thường) vs BR-SLA-02 line 1280 (`>50%` = bình thường). TC-BC-SM-03 expected "gộp hoặc tách" non-deterministic. | ✅ Sửa SM-03 expected 4 cột rõ + tạo SPEC-CLARIFY-BC-11 | SM-03 + BC-11 mới |
| **F-05** | P1 | TC-BC-PERM-012 accept "403 hoặc 200 silent override" — security gap, dễ bỏ lọt IDOR cross-tenant. | ✅ Sửa expected hard 403 only, silent override = FAIL | PERM-012 |
| **F-06** | P2 | 00-test-plan-overview ghi mapping ERR-RPT-IX01-01 → TC-BC-SM-01 negative, nhưng SM-01 chỉ smoke render, không có negative path. | ✅ Sửa mapping → TC-BC-REP-028 | 00 file |
| **F-07** | P2 | SCR-IX-01 line 1058-1080 có **8 optgroup**, TC-BC-SM-XC-01 expected ghi "7 nhóm" nhưng liệt kê 8. | ✅ Sửa "7 nhóm" → "8 nhóm" | SM-XC-01 |
| **F-08** | P2 | TC-BC-REP-022 expected "Nút Xuất disabled" mâu thuẫn TC-BC-REP-042 verify behavior empty + xuất có disabled hoặc xuất file rỗng. | ✅ Sửa REP-022 không assert disabled deterministic, ref SPEC-CLARIFY-BC-06 | REP-022 |
| **F-09** | P2 | 09-traceability ghi gap CB_PD_DP nhưng A6 đã có TC-BC-PERM-023. | ✅ Update file 09: G3 resolved, Permission Coverage 8/8 = 100% | 09 file |

**Total: 1 P0 + 4 P1 + 4 P2 = 9 findings → ALL APPLIED**

---

## Summary thay đổi

### TC count delta

| File | Trước Codex | Sau Codex | Delta |
|------|-------------|-----------|-------|
| 01-TC-tpl-report-full-representative.md | 39 | 39 | 0 (chỉ sửa REP-022 expected) |
| 02-TC-smoke-23-loai-bc.md | 40 | 40 | 0 (chỉ sửa SM-03, SM-XC-01 expected) |
| 03-TC-permission-2tier-bc.md | 18 | **19** | +1 (PERM-000 NEW) + sửa PERM-012 expected |
| 04-TC-export-xlsx-pdf-tt17.md | 19 | 19 | 0 (sửa EXP-004/005/006/013 expected 50K → 10K) |
| 05-TC-bieu-do-charts.md | 12 | 12 | 0 |
| **Tổng** | **128** | **129** | **+1** |

### SPEC-CLARIFY delta

- BC-01: **RE-OPEN** (Codex F-01) — TPL inline (50K) vs BR formal (10K), default 10K
- BC-11: **NEW** (Codex F-04) — BR-SLA-02 ngưỡng % mâu thuẫn FR-IX-03 vs §6
- Total SPEC-CLARIFY: 9 → **10 (1 RE-OPEN + 1 NEW)**

### Coverage delta

- Permission: 87.5% → **100%** (Codex F-09 confirm + F-03 +1 unauth)
- Security TC: +1 hard (PERM-000 unauthenticated)
- Quality score (10-REVIEW): 9.33 → **9.55/10** (sau Codex apply)

---

## Iron Rule check

✅ Mọi TC mới (PERM-000) merged inline vào file UC.
✅ File 12 này CHỈ là audit log Codex review. KHÔNG chứa TC source.
✅ 9/9 findings APPLIED in-place.

---

## Codex Gate

✅ **PASS** — 1 P0 đã RESOLVED, 4 P1 đã RESOLVED, 4 P2 đã RESOLVED. Phase A có thể flip ✅ trong todo.md.

---

*Generated 2026-05-10 — Codex review cycle 1*
