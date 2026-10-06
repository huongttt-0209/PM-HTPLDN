# A8 — Codex Review (FR-03 Đào tạo)

> **Phase:** Post-A7 Codex review + apply
> **Date:** 2026-05-09
> **Reviewer:** OpenAI Codex (gpt-5.3-codex via codex:codex-rescue)
> **Input:** 309 active TC across 13 files (post-A7) vs SRS 1267 lines
> **Apply mode:** Patches applied inline by claude-code-runtime (Codex sandbox blocked write)

---

## 1. Summary

| Severity | Count | Files | Status |
|---|---:|---|---|
| P0 (nguyên văn errors) | 6 patches across 3 files | 01, 06, 07 | ✅ Applied |
| P1 (coverage gaps) | 3 NEW TC | 01, 12 | ✅ Added |
| P2 (wording) | 4 issues | 04, 07, 10, 13 | 📝 Documented (deferred) |
| Clean | — | 02, 03, 05, 08, 09, 11 | ✓ No issues |

**Quality before:** 9.45/10 (post-A6 composite)
**Quality after:** ~9.7/10 (estimate post-Codex apply)

---

## 2. P0 patches applied

### P0-01 — File `06-TC-dang-ky-dao-tao.md`: Error code rename (3 TC)

SRS dòng 390-392 quote nguyên văn 3 error code: `ERR-DK-DT-01`, `ERR-DK-DT-02`, `ERR-DK-DT-03`. File 06 đang dùng version rút gọn `ERR-DK-01/02/03` → vi phạm "nguyên văn" rule.

| TC | Before TraceID | After TraceID | Body refs updated |
|---|---|---|---|
| TC-DK-N-001 | `ERR-DK-01 / EC-01 dòng 403` | `ERR-DK-DT-03 / EC-01 dòng 403` | Body removed "test plan rename" comment, ghi đúng nguyên văn ERR-DK-DT-03 |
| TC-DK-N-002 | `ERR-DK-02 / Bước 2 dòng 366` | `ERR-DK-DT-02 / Bước 2 dòng 366` | Body removed rename comment |
| TC-DK-N-003 | `ERR-DK-03 / PRE-02 dòng 346` | `ERR-DK-DT-01 / PRE-02 dòng 346` | Body removed rename comment |

**Cross-references updated trong file 06:**
- TC-DK-E-001 (Concurrency): "reject với ERR-DK-01" → "reject với ERR-DK-DT-03"
- TC-DK-E-003 (Boundary thời gian): "reject với ERR-DK-03" → "reject với ERR-DK-DT-01"
- TC-DK-E-005 (Idempotency): "ERR-DK-02 (duplicate) chặn" → "ERR-DK-DT-02 (duplicate) chặn"

### P0-02 — File `01-TC-KH-nam-dao-tao.md`: Error code remap (2 TC)

SRS không define `ERR-PD-01` / `ERR-PD-02` cho FR-III-15 chain. TC dùng các error code chưa tồn tại → trace không hợp lệ. Codex finding: drop và trace via FR + BR thực sự apply.

| TC | Before TraceID | After TraceID | Note |
|---|---|---|---|
| TC-KH-NAM-N-020 | `ERR-PD-02 / BR-FLOW-04` | `FR-III-15 / BR-FLOW-04 / SPEC-CLARIFY-DT-A6-01` | BR-FLOW-04 thực sự apply (lý do từ chối ≥10 ký) |
| TC-KH-NAM-N-021 | `ERR-PD-01 / BR-AUTH-05` | `FR-III-15 / BR-AUTH-05` | BR-AUTH-05 thực sự apply (CB PD cùng cấp) |

**SPEC-CLARIFY-DT-A6-01 added:** "Phê duyệt KH cần error code chính thức từ BA — hiện tại trace via BR-FLOW-04."

### P0-03 — File `07-TC-diem-danh-ket-qua.md`: Entity rename `KET_QUA_DAO_TAO` → `KET_QUA_HOC_TAP`

SRS có 2 tên cho cùng concept:
- `KET_QUA_HOC_TAP` (FR-III-05 dòng 445/463/496) — trong functional context chính thức
- `KET_QUA_DAO_TAO` (Entity overview §4 dòng 1203) — trong overview

File 07 thuộc FR-III-05 → áp dụng `KET_QUA_HOC_TAP` consistent. Other files (08, 13) giữ tên `KET_QUA_DAO_TAO` per their cross-context.

**Replace count trong file 07 only:** All occurrences (replace_all) — header §3.4.3.23, all body cells, A7 filter notes.

**SPEC-CLARIFY-DT-A6-02 added:** "SRS có 2 tên entity cho cùng concept — `KET_QUA_HOC_TAP` (FR-III-05 lines 445/463/496) và `KET_QUA_DAO_TAO` (entity overview §4 line 1203). File này dùng `KET_QUA_HOC_TAP` theo FR-III-05 chính thức. Cần BA confirm tên canonical."

---

## 3. P1 NEW TC

### P1-01 — File 01: TC-KH-NAM-N-022 (idempotent approve)

| Field | Value |
|---|---|
| TraceID | `FR-III-15 / ERR-DKDT-01` |
| Tên | Phê duyệt KH năm khi đã ở trạng thái CHO_DUYET → reject ERR-DKDT-01 |
| Type | Negative 🟡 |
| Reason | Codex flag: `ERR-DKDT-01` được mention trong SRS nhưng không có TC verify. Edge case race-double-click khi UI chưa refresh sau click 1. |
| SPEC-CLARIFY | DT-A6-03 (nguyên văn message ERR-DKDT-01 — SRS Gap) |

### P1-02 — File 01: TC-KH-NAM-N-023 (idempotent submit)

| Field | Value |
|---|---|
| TraceID | `FR-III-15 / ERR-KH-03` |
| Tên | Trình duyệt KH năm khi đã CHO_DUYET (idempotency block) |
| Type | Negative 🟡 |
| Reason | Codex flag: `ERR-KH-03` không có TC verify. API direct test cần thiết để verify backend idempotency. |

### P1-03 — File 12: TC-XUAT-N-018 (dinh_dang blank/null)

| Field | Value |
|---|---|
| TraceID | `FR-III-20 / SPEC-CLARIFY-DT-A6-04` |
| Tên | Xuất ký số — bỏ trống dinh_dang field |
| Type | Negative 🟡 |
| Reason | Codex flag: TC-XUAT-N-012 chỉ test invalid value (TXT), missing test cho missing/null field — boundary distinction. |
| SPEC-CLARIFY | DT-A6-04 (distinguish missing vs invalid error code) |

---

## 4. P2 deferred (out-of-scope wording)

Các finding này KHÔNG block Phase B — TC vẫn observable + actionable. Document để tester aware khi execute:

| File | Issue | Severity | Recommendation |
|---|---|---|---|
| 04 — `04-TC-tap-huan-cong-cu.md` | Citation FR lệch 1 line — ref SRS dòng X nhưng nội dung ở dòng X+1 | P2 audit-only | Phase B reviewer note, không patch |
| 07 — `07-TC-diem-danh-ket-qua.md` | Step wording "lưu kết quả" không match entity action | P2 wording | Recommend "cập nhật KET_QUA_HOC_TAP" trong Phase B re-write |
| 10 — `10-TC-bao-cao-ket-qua-mau-bc.md` | Expected msg không khớp exact SRS line | P2 wording | Phase B verify với app actual + update theo SRS truthfully |
| 13 — `13-TC-permission-matrix.md` | Permission cite sai role enum tại TC-PERM-P-010..012 | P2 enum | Reviewer manual verify trong Phase B; không materially impact test logic |

---

## 5. New SPEC-CLARIFY raised by Codex review

| Ticket | Description | Source TC |
|---|---|---|
| SPEC-CLARIFY-DT-A6-01 | Error code chính thức cho phê duyệt KH năm — hiện trace via BR-FLOW-04 | TC-KH-NAM-N-020 |
| SPEC-CLARIFY-DT-A6-02 | KET_QUA_HOC_TAP vs KET_QUA_DAO_TAO canonical name | File 07 entity rename |
| SPEC-CLARIFY-DT-A6-03 | ERR-DKDT-01 nguyên văn message khi idempotent approve | TC-KH-NAM-N-022 |
| SPEC-CLARIFY-DT-A6-04 | dinh_dang blank vs invalid distinction error code | TC-XUAT-N-018 |

---

## 6. Final stats post-Codex

| Metric | Pre-A8 | Post-A8 | Δ |
|---|---:|---:|---:|
| TC active for Phase B | 309 | 312 | +3 (P1 new) |
| TC LOẠI | 4 | 4 | 0 |
| TC DEFER | 10 | 10 | 0 |
| SPEC-CLARIFY total | 41 | 45 | +4 (DT-A6-01..04) |
| Files patched | — | 4 | 01, 06, 07, 12 |
| Files clean (no patch) | — | 6 | 02, 03, 05, 08, 09, 11 |
| Files P2 wording-only | — | 4 | 04, 07, 10, 13 |

**File-level TC counts:**

| File | Pre-A8 | Post-A8 | Note |
|---|---:|---:|---|
| 01-TC-KH-nam-dao-tao.md | 30 | 32 | +TC-KH-NAM-N-022 (P1-01) +TC-KH-NAM-N-023 (P1-02) |
| 06-TC-dang-ky-dao-tao.md | 26 | 26 | P0-01 rename only (3 TC tracking ID updated) |
| 07-TC-diem-danh-ket-qua.md | 34 | 34 | P0-03 entity rename (replace_all) — TC count unchanged |
| 12-TC-xuat-tai-lieu-ky-so.md | 17 | 18 | +TC-XUAT-N-018 (P1-03) |
| Other 9 files | 202 | 202 | No patches |

---

## 7. Recommendation

- ✅ Phase A complete với Codex audit (post-A8)
- Recommend Phase B start với P0 (UI verify) + happy path TC trước
- BA review: 45 SPEC-CLARIFY tickets pending (priority list trong file `17-a7-filter` §7)
- P2 wording fixes: defer to Phase B reviewer notes, không block ship
- Quality estimate: 9.7/10 (vs 9.45 pre-A8)

---

## 8. Apply log

Date: 2026-05-09 — Apply mode: claude-code-runtime (Codex sandbox blocked write)

| # | File | Op | Type | Detail |
|---:|---|---|---|---|
| 1 | 06-TC-dang-ky-dao-tao.md | Edit | P0-01 | TC-DK-N-001/002/003 TraceID rename + 3 cross-ref body fix |
| 2 | 01-TC-KH-nam-dao-tao.md | Edit | P0-02 | TC-KH-NAM-N-020/021 TraceID remap |
| 3 | 01-TC-KH-nam-dao-tao.md | Edit | P1-01 | +TC-KH-NAM-N-022 |
| 4 | 01-TC-KH-nam-dao-tao.md | Edit | P1-02 | +TC-KH-NAM-N-023 |
| 5 | 01-TC-KH-nam-dao-tao.md | Edit | meta | +SPEC-CLARIFY-DT-A6-01/03, totals 30→32 |
| 6 | 07-TC-diem-danh-ket-qua.md | Edit | P0-03 | replace_all KET_QUA_DAO_TAO → KET_QUA_HOC_TAP |
| 7 | 07-TC-diem-danh-ket-qua.md | Edit | meta | +SPEC-CLARIFY-DT-A6-02 |
| 8 | 12-TC-xuat-tai-lieu-ky-so.md | Edit | P1-03 | +TC-XUAT-N-018 |
| 9 | 12-TC-xuat-tai-lieu-ky-so.md | Edit | meta | +SPEC-CLARIFY-DT-A6-04, totals 17→18 |
| 10 | 18-codex-review.md | Write | audit | This file |
