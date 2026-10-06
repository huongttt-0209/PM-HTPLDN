# A4 — Edge Case Hunter Review (Audit Log) — FR-12 TV Chuyên sâu

> **Phiên bản:** 1.0 · **Ngày:** 2026-05-06 · **Module:** FR-12 TV Chuyên sâu (W3.3)
> **Reviewer:** BMAD edge-case-hunter
> **Status:** MERGED 2026-05-06 — 26 edge case proposed đã inline merge vào 6 file UC.
> **Mục đích:** Log proposal + reasoning + merge mapping cho edge cases mới.
> **Iron rule:** File này KHÔNG phải TC source — TC đã merged INLINE vào file UC gốc. Phase B B-block KHÔNG ref file này.

---

## 1. Tổng quan delta merge

| File UC | TC trước A4 | TC sau A4 | Delta | Section merge |
|---|---:|---:|---:|---|
| 01-TC-FR-X1-01-quan-ly-tvcs.md | 29 | 36 | +7 | F. Edge bổ sung A4 |
| 02-TC-FR-X1-02-tim-kiem-tvcs.md | 15 | 19 | +4 | G. Edge bổ sung A4 |
| 03-TC-FR-X1-04-quan-ly-hspl.md | 15 | 19 | +4 | F. Edge bổ sung A4 |
| 04-TC-FR-X1-06-quan-ly-tu-lieu-pl.md | 15 | 20 | +5 | G. Edge bổ sung A4 |
| 05-TC-permission-matrix.md | 10 | 13 | +3 | G. Edge bổ sung A4 |
| 06-TC-FR-X1-03-05-07-API-inbound-side-effect.md | 7 | 10 | +3 | E. Edge bổ sung A4 |
| **Total** | **91** | **117** | **+26** | — |

**Verify command:** `grep -cE "^\| TC-TVCS-" 01.md` etc — đã verify khớp footer mỗi file (xem §4 dưới).

---

## 2. Proposals + merge mapping

### File 01 — UC147 Quản lý TVCS (+7 edge case)

#### TC-TVCS-030 — Boundary noi_dung_tu_van: 50KB-1 / 50KB exact / 50KB+1
- **Dimension:** Boundary value
- **Reasoning:** TC-TVCS-008 chỉ test 51KB single-case. SRS line 108 quote max 50KB → cần boundary triple để verify inclusive at 50KB exact.
- **Merged inline:** Section F file 01.
- **SRS hint:** srs-fr-12 line 108 (max 50KB).
- **Priority:** P1.

#### TC-TVCS-031 — Data quality Unicode emoji + RTL Arabic + zero-width
- **Dimension:** Data quality
- **Reasoning:** A3 không cover Unicode edge — emoji/RTL trong RTE có thể break encoding hoặc FTS.
- **Merged inline:** Section F file 01.
- **SRS hint:** No SRS quote — best practice extrapolation (TEXT field UTF-8).
- **Priority:** P2.

#### TC-TVCS-032 — Double-click [Phê duyệt] race
- **Dimension:** State transitions / SM violations
- **Reasoning:** TC-TVCS-022 cover optimistic lock 2 user, thiếu single-user double-click idempotency.
- **Merged inline:** Section F file 01.
- **SRS hint:** No SRS quote idempotency — best practice (BR-EC-01 extends).
- **Priority:** P1.

#### TC-TVCS-033 — Session expire giữa form CREATE TVCS
- **Dimension:** Error injection
- **Reasoning:** A3 không cover session lifecycle mid-form. Form data loss policy chưa quote.
- **Merged inline:** Section F file 01.
- **SRS hint:** BR-AUTH-01 line 1525-1529 (session); no quote refresh policy.
- **Priority:** P2. SPEC-CLARIFY-TVCS-EDGE-01.

#### TC-TVCS-034 — Browser back giữa flow PD modal
- **Dimension:** Error injection
- **Reasoning:** A3 không cover SPA navigation edge — modal state, ghost transition.
- **Merged inline:** Section F file 01.
- **SRS hint:** No SRS quote — best practice SPA.
- **Priority:** P2.

#### TC-TVCS-035 — Concurrent toggle CONG_KHAI 2 user race
- **Dimension:** State transitions
- **Reasoning:** TC-TVCS-027 cover API fail rollback single-user; thiếu race 2 user toggle CK.
- **Merged inline:** Section F file 01.
- **SRS hint:** BR-EC-01 + line 234 (BR-PUBLIC-01).
- **Priority:** P1. SPEC-CLARIFY-TVCS-EDGE-02.

#### TC-TVCS-036 — file_dinh_kem_cong_khai tổng > 100MB → reject
- **Dimension:** Boundary value
- **Reasoning:** A3 chỉ cover single file 10MB CK; thiếu tổng dung lượng aggregate.
- **Merged inline:** Section F file 01.
- **SRS hint:** No SRS quote tổng size — extrapolation BR-EC-03.
- **Priority:** P2. SPEC-CLARIFY-TVCS-EDGE-03.

### File 02 — UC148 Tìm kiếm TVCS (+4 edge case)

#### TC-TVCS-TK-016 — Boundary tu_khoa: chỉ space
- **Dimension:** Boundary value / Data quality
- **Reasoning:** A3 không cover whitespace handling (trim policy).
- **Merged inline:** Section G file 02.
- **SRS hint:** line 341 (tu_khoa optional); no quote trim.
- **Priority:** P2. SPEC-CLARIFY-TVCS-TK-01.

#### TC-TVCS-TK-017 — Boundary tu_khoa max 200 ký exact + 201 reject
- **Dimension:** Boundary value
- **Reasoning:** TC-TVCS-TK-012 cover hỗn hợp SQL+XSS+250 ký, thiếu boundary chính xác 200/201 (BR-EC-13).
- **Merged inline:** Section G file 02.
- **SRS hint:** BR-EC-13 cross-cutting (max 200 ký).
- **Priority:** P1.

#### TC-TVCS-TK-018 — Deep page=99999 ngoài range
- **Dimension:** Boundary value
- **Reasoning:** A3 không cover upper bound page → OOM hoặc empty handling.
- **Merged inline:** Section G file 02.
- **SRS hint:** line 347 (page ≥1); no quote upper bound.
- **Priority:** P2. SPEC-CLARIFY-TVCS-TK-02.

#### TC-TVCS-TK-019 — Tab switch giữ filter state
- **Dimension:** Cross-feature
- **Reasoning:** A3 test tab switch riêng, thiếu filter persistence across tabs.
- **Merged inline:** Section G file 02.
- **SRS hint:** line 1073 + 1100; no quote persistence.
- **Priority:** P1. SPEC-CLARIFY-TVCS-TK-03.

### File 03 — UC150 HSPL (+4 edge case)

#### TC-HSPL-016 — Boundary file: 0 byte / 20MB exact / 20MB+1
- **Dimension:** Boundary value
- **Reasoning:** TC-HSPL-011 test 21MB; thiếu boundary triple + 0 byte edge.
- **Merged inline:** Section F file 03.
- **SRS hint:** line 654 (ERR-HSPL-03 max 20MB); no quote 0 byte.
- **Priority:** P1. SPEC-CLARIFY-HSPL-FILE-01.

#### TC-HSPL-017 — File corrupt mid-upload (network interrupt)
- **Dimension:** Error injection
- **Reasoning:** A3 không cover network interrupt → orphan file/transaction state.
- **Merged inline:** Section F file 03.
- **SRS hint:** BR-EC-20 + BR-EC-03; no quote orphan cleanup.
- **Priority:** P2. SPEC-CLARIFY-HSPL-FILE-02.

#### TC-HSPL-018 — Date validation: ngay_het_han < ngay_cap
- **Dimension:** Boundary value
- **Reasoning:** A3 không cover business rule date relationship.
- **Merged inline:** Section F file 03.
- **SRS hint:** line 540 (fields); no quote business rule.
- **Priority:** P1. SPEC-CLARIFY-HSPL-DATE-02.

#### TC-HSPL-019 — Unicode NFC vs NFD normalization
- **Dimension:** Data quality
- **Reasoning:** A3 không cover Unicode normalization edge — duplicate detect false-negative.
- **Merged inline:** Section F file 03.
- **SRS hint:** BR-DATA-08 line 1567-1571 FTS; no quote NFC/NFD policy.
- **Priority:** P2. SPEC-CLARIFY-HSPL-UNI-01.

### File 04 — UC152 TLPL (+5 edge case)

#### TC-TLPL-016 — Race CONG_KHAI vs DELETE 2 user
- **Dimension:** State transitions
- **Reasoning:** A3 cover BR-EC-01 single-action; thiếu race giữa 2 hành động khác nhau.
- **Merged inline:** Section G file 04.
- **SRS hint:** BR-EC-01 + BR-EC-20.
- **Priority:** P1. SPEC-CLARIFY-TLPL-EDGE-01.

#### TC-TLPL-017 — Boundary file 20MB exact / 20MB+1
- **Dimension:** Boundary value
- **Reasoning:** TC-TLPL-008 test 21MB; thiếu boundary inclusive at 20MB.
- **Merged inline:** Section G file 04.
- **SRS hint:** line 937 (ERR-TLPL-03 max 20MB).
- **Priority:** P1.

#### TC-TLPL-018 — API Cổng PLQG timeout 30s rollback + retry
- **Dimension:** Error injection
- **Reasoning:** TC-TLPL-013 cover 500 fail; thiếu timeout boundary + retry flow.
- **Merged inline:** Section G file 04.
- **SRS hint:** line 940 (ERR-TLPL-06) + BR-EC-20; no quote timeout interval.
- **Priority:** P1. SPEC-CLARIFY-TLPL-DELETE-01.

#### TC-TLPL-019 — NHAP→CONG_KHAI khi parent TVCS HUY
- **Dimension:** Cross-feature / state inconsistency
- **Reasoning:** A3 không cover cascade state validation từ parent.
- **Merged inline:** Section G file 04.
- **SRS hint:** line 845-855 + BR-FLOW-07; no quote parent state guard.
- **Priority:** P1. SPEC-CLARIFY-TLPL-EDGE-02.

#### TC-TLPL-020 — Multi-file CK chain: atomicity 5 file Cổng push
- **Dimension:** Cross-feature
- **Reasoning:** A3 cover single file CK; thiếu multi-file partial fail.
- **Merged inline:** Section G file 04.
- **SRS hint:** line 854 + BR-EC-20.
- **Priority:** P2. SPEC-CLARIFY-TLPL-EDGE-03.

### File 05 — Permission Matrix (+3 edge case)

#### TC-PERM-011 — Token expire mid-action form CREATE
- **Dimension:** Error injection / Session lifecycle
- **Reasoning:** A3 không cover session expire mid-form.
- **Merged inline:** Section G file 05.
- **SRS hint:** BR-AUTH-01 line 1525-1529; no quote refresh strategy.
- **Priority:** P2. SPEC-CLARIFY-TVCS-PERM-05.

#### TC-PERM-012 — Role change mid-session
- **Dimension:** State transitions / Permission
- **Reasoning:** A3 không cover per-request authz revalidation.
- **Merged inline:** Section G file 05.
- **SRS hint:** BR-AUTH-01 + BR-AUTH-08; no quote per-action timing.
- **Priority:** P2. SPEC-CLARIFY-TVCS-PERM-06.

#### TC-PERM-013 — Tier 2 SSO callback fail
- **Dimension:** Error injection
- **Reasoning:** TC-PERM-003 cover happy path Tier 2; thiếu error/timeout flow.
- **Merged inline:** Section G file 05.
- **SRS hint:** BR-AUTH-01 line 1525-1529 (Tier 2 OIDC); no quote callback error UI.
- **Priority:** P2. SPEC-CLARIFY-TVCS-PERM-07.

### File 06 — API Inbound Side-Effect (+3 edge case)

#### TC-API-IN-008 — Rate limit ngưỡng burst 110 req
- **Dimension:** Boundary value (A7-compatible verify UI count)
- **Reasoning:** A3 không cover rate limit side-effect; trigger qua admin endpoint, verify UI count delta.
- **Merged inline:** Section E file 06.
- **SRS hint:** BR-EC cross-cutting + UC149 line 442; no quote rate limit threshold.
- **Priority:** P2. SPEC-CLARIFY-TVCS-API-RL.

#### TC-API-IN-009 — Payload corrupt: malformed/oversize/missing field
- **Dimension:** Error injection / Data quality
- **Reasoning:** A3 cover duplicate (003); thiếu malformed/oversize/missing.
- **Merged inline:** Section E file 06.
- **SRS hint:** UC149 Step 4 line 451 + E1-E2 line 496-497.
- **Priority:** P1. SPEC-CLARIFY-TVCS-API-PAYLOAD.

#### TC-API-IN-010 — Concurrent push 2 record cùng ma_noi_dung_cong race
- **Dimension:** State transitions / race
- **Reasoning:** TC-API-IN-003 cover sequential duplicate; thiếu concurrent race với DB unique constraint.
- **Merged inline:** Section E file 06.
- **SRS hint:** UC149 Step 5 line 454 + E3 line 498 (ERR-TVCS-API-03).
- **Priority:** P1. SPEC-CLARIFY-TVCS-API-RACE.

---

## 3. Spec gaps phát sinh (SPEC-CLARIFY mới từ A4)

| ID | Origin TC | Question |
|----|-----------|----------|
| SPEC-CLARIFY-TVCS-EDGE-01 | TC-TVCS-033 | Session expire mid-form: refresh token strategy + form data preservation? |
| SPEC-CLARIFY-TVCS-EDGE-02 | TC-TVCS-035 | Concurrent CONG_KHAI 2 user: optimistic lock reject vs idempotent skip? |
| SPEC-CLARIFY-TVCS-EDGE-03 | TC-TVCS-036 | Tổng dung lượng file CK aggregate threshold? |
| SPEC-CLARIFY-TVCS-TK-01 | TC-TVCS-TK-016 | tu_khoa whitespace trim policy (full trim hay strict)? |
| SPEC-CLARIFY-TVCS-TK-02 | TC-TVCS-TK-018 | page upper bound auto-clamp last vs return empty? |
| SPEC-CLARIFY-TVCS-TK-03 | TC-TVCS-TK-019 | Filter state: persist across tabs vs reset? |
| SPEC-CLARIFY-HSPL-FILE-01 | TC-HSPL-016 | 0 byte file accept hay reject? |
| SPEC-CLARIFY-HSPL-FILE-02 | TC-HSPL-017 | TTL cleanup pending uploads (interrupt mid-upload)? |
| SPEC-CLARIFY-HSPL-DATE-02 | TC-HSPL-018 | ngay_het_han = ngay_cap (cùng ngày) PASS hay reject? |
| SPEC-CLARIFY-HSPL-UNI-01 | TC-HSPL-019 | Unicode normalization NFC vs NFD policy? |
| SPEC-CLARIFY-TLPL-EDGE-01 | TC-TLPL-016 | Race CK vs DELETE: precedence rule? |
| SPEC-CLARIFY-TLPL-EDGE-02 | TC-TLPL-019 | Parent TVCS HUY block child TLPL CK? |
| SPEC-CLARIFY-TLPL-EDGE-03 | TC-TLPL-020 | Multi-file CK atomic vs best-effort? |
| SPEC-CLARIFY-TVCS-PERM-05 | TC-PERM-011 | Session refresh strategy + form preservation? |
| SPEC-CLARIFY-TVCS-PERM-06 | TC-PERM-012 | Per-request authz revalidation timing? |
| SPEC-CLARIFY-TVCS-PERM-07 | TC-PERM-013 | SSO VNeID callback error UI + retry? |
| SPEC-CLARIFY-TVCS-API-RL | TC-API-IN-008 | API inbound rate limit threshold + retry-after header? |
| SPEC-CLARIFY-TVCS-API-PAYLOAD | TC-API-IN-009 | Payload size limit + error response schema? |
| SPEC-CLARIFY-TVCS-API-RACE | TC-API-IN-010 | Concurrent ma_noi_dung_cong race resolution policy? |

→ **19 SPEC-CLARIFY mới** sẽ gửi BA ở Phase B B-Verify.

---

## 4. Verification — count khớp footer

| File UC | Pre-merge | Post-merge | Δ | grep verify |
|---------|----------:|-----------:|--:|---|
| 01-TC-FR-X1-01-quan-ly-tvcs.md | 29 | 36 | +7 | `grep -cE "^\| TC-TVCS-[0-9]+"` = 36 OK |
| 02-TC-FR-X1-02-tim-kiem-tvcs.md | 15 | 19 | +4 | `grep -cE "^\| TC-TVCS-TK-[0-9]+"` = 19 OK |
| 03-TC-FR-X1-04-quan-ly-hspl.md | 15 | 19 | +4 | `grep -cE "^### TC-HSPL-[0-9]+"` = 19 OK |
| 04-TC-FR-X1-06-quan-ly-tu-lieu-pl.md | 15 | 20 | +5 | `grep -cE "^### TC-TLPL-[0-9]+"` = 20 OK |
| 05-TC-permission-matrix.md | 10 | 13 | +3 | `grep -cE "^### TC-PERM-[0-9]+"` = 13 OK |
| 06-TC-FR-X1-03-05-07-API-inbound-side-effect.md | 7 | 10 | +3 | `grep -cE "^### TC-API-IN-[0-9]+"` = 10 OK |
| **Total** | **91** | **117** | **+26** | All OK |

---

## 5. Phase B B-block ref (cập nhật todo.md §W3.3)

```
| B1 | 01-TC-FR-X1-01-quan-ly-tvcs.md                       | 36 |
| B2 | 02-TC-FR-X1-02-tim-kiem-tvcs.md                      | 19 |
| B3 | 03-TC-FR-X1-04-quan-ly-hspl.md                       | 19 |
| B4 | 04-TC-FR-X1-06-quan-ly-tu-lieu-pl.md                 | 20 |
| B5 | 05-TC-permission-matrix.md                           | 13 |
| B6 | 06-TC-FR-X1-03-05-07-API-inbound-side-effect.md      | 10 |
| TOTAL                                                     | 117 |
```

→ **117 TC chính** sẽ chạy Phase B `/qa-only`. File 07 = audit log only (không có B-block).

---

*Generated 2026-05-06 by BMAD A4 (edge-case-hunter) → MERGED 2026-05-06 (per Iron rule inline merge — Phase B B-block ref only file UC).*
