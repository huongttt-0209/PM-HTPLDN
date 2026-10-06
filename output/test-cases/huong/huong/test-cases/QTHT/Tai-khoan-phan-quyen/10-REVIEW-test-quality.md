# A6 — Test Quality Review (FR-VIII-14..17 + FR-VIII-26)

> **Tác nhân**: bmad-testarch-test-review
> **Ngày**: 2026-05-08
> **Mục đích**: Review chất lượng TC theo 6 axis. Fill gap A5 (TC mới INLINE merge vào file UC, audit log ở đây).

---

## 1. 6-Axis Quality Score

| Axis | Score (/10) | Reasoning |
|------|------------|-----------|
| 1. Coverage SRS | 9.5 | BR 96.4% (BR-AUTH-06 + BR-DATA-03 ⚠️ rely sibling/inspection), AC 100%, ERR 100%, SM 100%, Permission 100%. SRS GAP-VIII-04 (password complexity) đã trace explicit. |
| 2. Test design quality (BVA + EP + Error Guess) | 9.3 | BVA đủ 4 boundary (3/4/50/51 username), 8/8 password, 11/12 CCCD, 89/90/91 ngày sibling. EP partition đủ states + roles. Error guess đủ XSS + SQL + IDOR + race. Thiếu: stress test 50K+. |
| 3. Trace ID + sourceability | 9.5 | Mọi TC có TraceID link BR/AC/ERR/SM. Cell `Kết quả mong đợi` chia STATE/UI/PERSIST. Pre-condition tường minh. |
| 4. Independence + idempotency | 9.0 | Mỗi TC isolated tốt; vài TC dùng output TC trước (TC-104 → TC-128 cross is_deleted; TC-115 → TC-116-117) — đã document chain. SM lifecycle TC chuỗi rõ ràng. |
| 5. Maintainability | 9.0 | Pre-condition chung mỗi file giảm duplicate. SPEC-CLARIFY tách rõ. File 08/10/11 audit log không lẫn TC. |
| 6. Phase B executability (UI/MCP) | 9.2 | A7 đã filter — 0 TC chỉ-DB/API thuần. Mọi IDOR test dùng MCP `evaluate_script` UI bridge. Wait-time test (TC-139, TC-142, TC-150) có note deferral. MailHog UI verify (`http://103.172.236.130:8025`). Cross-module verify dùng thực entity (CG/TVV, NHT). |
| **Average** | **9.25** | Quality target ≥ 8.5 — **PASS** |

---

## 2. Issue list (Severity Critical / Major / Minor)

### Critical issues (block Phase B)
**Không có Critical.**

### Major issues (cần xử lý trước Phase B)

| Major ID | File | TC | Issue | Action |
|----------|------|-----|-------|--------|
| MAJ-A6-01 | 02-TC-tai-khoan.md | TC-139 + TC-142 | Auto unlock 30 phút + auto disable 7 ngày — KHÔNG test được trên env real-time. | Defer Phase B với note "manual time check" hoặc "time-travel mock if env support". |
| MAJ-A6-02 | 03-TC-phan-quyen-du-lieu.md | TC-105 | Cross-module verify cần module Vụ việc có data — phụ thuộc Phase A vụ việc + Phase B seed. | Phase B sẽ run sau khi W3.2 Phase B done với seed VV. |
| MAJ-A6-03 | 05-TC-quen-mk-kich-hoat.md | TC-140-141 | Token vĩnh viễn vs 30 phút boundary — cần wait time. | Defer Phase B với note. |

### Minor issues (FYI, không chặn)

| Minor ID | File | TC | Issue | Action |
|----------|------|-----|-------|--------|
| MIN-A6-01 | 01-TC-vai-tro.md | TC-110 (search) | SCR-VIII-02 không liệt kê tường minh ô search → log SPEC-CLARIFY-TKPQ-12 + TC marked P2. | OK. |
| MIN-A6-02 | 04-TC-phan-quyen-chuc-nang.md | TC-108 | Cây menu count exact KHÔNG biết — test "≥ 12-16". | SPEC-CLARIFY-TKPQ-10 + dynamic verify. |
| MIN-A6-03 | All UC | — | Output column verify chỉ qua UI (cột bảng) — không verify DB schema directly. | A7 rule: UI bridge OK. |

---

## 3. A6 Fill Gap (forward từ A5) — đã INLINE MERGE

| A5 Gap ID | TC mới | File UC | Status |
|-----------|--------|---------|--------|
| A5-GAP-01 | TC-VT-110 (search box UC112) | 01-TC-vai-tro.md | ✅ inline merged |
| A5-GAP-02 | TC-VT-138 (cap field clarify) | 01-TC-vai-tro.md | ✅ inline merged |
| A5-GAP-03 | TC-TK-110 (click username chi tiết) | 02-TC-tai-khoan.md | ✅ inline merged |
| A5-GAP-04 | TC-TK-131 (SM-T2 v3.1 backward compat) | 02-TC-tai-khoan.md | ✅ inline merged |
| A5-GAP-05 | TC-TK-135 (SM-T5 button manual activate) | 02-TC-tai-khoan.md | ✅ inline merged |
| A5-GAP-06 | TC-TK-194 (lan_dang_nhap_cuoi update) | 02-TC-tai-khoan.md | ✅ inline merged |
| A5-GAP-07 | TC-TK-195 (button [Xóa] vs [Vô hiệu hóa]) | 02-TC-tai-khoan.md | ✅ inline merged |
| A5-GAP-08 | TC-TK-196 (so_tai_khoan derive realtime) | 02-TC-tai-khoan.md | ✅ inline merged |
| A5-GAP-09 | TC-PQDL-137 (vai trò mới chưa quyền) | 03-TC-phan-quyen-du-lieu.md | ✅ inline merged |
| A5-GAP-10 | TC-PQDL-138 (đơn vị TAM_DUNG) | 03-TC-phan-quyen-du-lieu.md | ✅ inline merged |
| A5-GAP-11 | TC-PQCN-108 (count menu cây) | 04-TC-phan-quyen-chuc-nang.md | ✅ inline merged |
| A5-GAP-12 | TC-PWD-149 (mail link format) | 05-TC-quen-mk-kich-hoat.md | ✅ inline merged |
| A5-GAP-13 | TC-PWD-150 (token cleanup cron) | 05-TC-quen-mk-kich-hoat.md | ✅ inline merged |

**Tổng A6 fill: 13 TC inline merged** (đã được tính trong tổng 188 TC).

---

## 4. Test review checklist

| Item | Status |
|------|--------|
| Pre-condition chung mỗi file rõ ràng | ✅ |
| Mỗi TC có Pre-condition + Test Data + Steps + Expected | ✅ |
| Expected chia STATE / UI / PERSIST | ✅ |
| TraceID link BR/AC/ERR/SM rõ ràng | ✅ |
| Priority P0/P1/P2 phân loại | ✅ |
| Type Happy/Negative/Edge/Boundary phân loại | ✅ |
| Tổng count footer mỗi file | ✅ |
| Coverage summary mỗi file | ✅ |
| Note A7 cuối mỗi file | ✅ |
| SPEC-CLARIFY listed | ✅ (29 entries trong 09-traceability-matrix) |
| File 08/09/10/11 KHÔNG chứa TC source | ✅ |
| TC chỉ-DB/API thuần | ✅ 0 TC (verify A7) |

---

## 5. Recommendation cho Phase B

1. **Seed data ưu tiên:**
   - VAI_TRO ≥ 11 record + 1 NEW_ROLE / TEST_CASCADE / ALL_PERMS để test phân quyền sạch.
   - TAI_KHOAN seed 5 trạng thái (HOAT_DONG / CHO_KICH_HOAT × 3 vai trò khác / TAM_KHOA / VO_HIEU_HOA).
   - DON_VI cây 2-tầng (1 TW + ≥ 5 BN + ≥ 5 ĐP) để test BR-AUTH-02 + cây render + cascade.
   - DANH_MUC LOAI_TAI_KHOAN ≥ 2 enum (NOI_BO + DOANH_NGHIEP).
2. **Tài khoản test:**
   - `qtht_01` primary CRUD.
   - `qtht_02` fallback khi `qtht_01` lock + race condition test.
   - `qtht_03` (nếu có) permission test khi cần verify view-only QTHT.
   - 6 user (CB_NV/CB_PD × 3 cấp) + 4 user Tier 2 cho 06-permission-matrix.
3. **MailHog access**: verify `http://103.172.236.130:8025` accessible từ test env.
4. **Time-travel constraint**: TC-TK-139, TC-TK-142, TC-PWD-140, TC-PWD-141, TC-PWD-150 cần wait thực 30 phút / 7 ngày HOẶC mock — note deferral.
5. **Cross-module dependency**:
   - TC-PQDL-105 phụ thuộc data Vụ việc → run sau W3.2 Phase B.
   - TC-PWD-142 + TC-PWD-143 phụ thuộc module CG/TVV + NHT (FR-04) → run sau W2.2 Phase B.
6. **MCP chrome-devtools setup**: theo CLAUDE.md MCP-Rule 1-7. Login pattern: `qtht_01 / Secret@123 / OTP 666666`.

---

## 6. Phase A → Phase B handoff acceptance (Codex R2 update 2026-05-08)

- ✅ 7 bước A1-A7 done + Codex R2 round
- ✅ Traceability **100% BR** (14/14, sau Codex R2 fill BR-AUTH-06/09 + BR-DATA-03 + BR-EC-13 boundary)
- ✅ AC 100% (16/16)
- ✅ ERR 100% (19/19)
- ✅ SM-TAIKHOAN 100% (12/12 transitions, T4/T5 wording note)
- ✅ Permission 100%
- ✅ 0 TC chỉ-DB/API thuần trong functional suite (16 TC IDOR moved to file 07 security)
- ✅ 0 TC sống ở file phụ (08/09/10/11) — TC nằm trong 6 file UC `01-06` + 1 file security `07`
- ✅ SPEC-CLARIFY listed (29 entries — TKPQ-20 + TKPQ-25 withdrawn sau Codex R2; +TKPQ-30 NEW SCR vs FR Output)
- ✅ Quality avg 9.45/10 (sau Codex R2 — tăng từ 9.25 do BR coverage 100% + A7 strict compliance)

## 7. Codex R2 Round Summary (2026-05-08)

**Findings:** 5 P1 + 5 P2 from Codex independent review.

**Resolutions:**
- P1#1 (A7 violation 14 TC IDOR) → MOVE to `07-TC-security-IDOR.md`
- P1#2 (DB-direct verify in soft delete) → RESHAPE expected qua UI + AUDIT_LOG
- P1#3 (UC114 role-mapping wrong) → RESHAPE TC-PQDL-120-123 dựa trên cap enum
- P1#4 (TC-PQDL-127, TC-PQCN-122 false clarify) → FORCE expected reject empty (SRS rõ Y)
- P1#5 (BR coverage overstated) → FILL 4 new TC (TC-TK-197/198/199 + TC-PWD-151/152)
- P2#1 (TC-VT-110 search false flag) → REMOVE out-of-scope
- P2#2 (TC perf/race exploratory) → KEEP với note non-functional
- P2#3 (TC-TK-101 duplicate filter) → FIX 5 filter
- P2#4 (SM-T4/T5 wording) → ADD note 1 SRS transition split 2 paths
- P2#5 (TC count footer mismatch) → FIX all 6 file UC + audit logs

**Net delta:** +5 TC functional (195 → 200 grand total; 184 functional + 16 security).

**Phase A done — ready for Phase B.**

---

## 8. UC120 / FR-VIII-22 Append (2026-05-10)

> **Scope mới**: 12-TC-self-registration-dn.md (UC120 self-registration DN). A6 review riêng cho file mới — 6-axis score + issue + A5-GAP-14..17 fill log. KHÔNG ảnh hưởng review cũ Section 1-7.

### 8.1 6-Axis Quality Score (UC120)

| Axis | Score (/10) | Reasoning |
|------|------------|-----------|
| 1. Coverage SRS | 9.5 | BR 100% (BR-DATA-02 unique + BR-AUTH-01 password + BR-DATA-05 audit + BR-EC-13 sanitize), AC 100% (4/4), ERR-REG 100% (6/6), SM T1 + T4 paths cover, 22 fields cover full BVA. |
| 2. Test design quality (BVA + EP + Error Guess) | 9.4 | BVA: MST 9/10/13/14, username 3/4/50/51, password 7/8, email 254 RFC max. EP: 22 fields × required/optional/format. Error guess: XSS, MIME spoof, race condition, leading-zero MST, IDN email, browser autofill, network failure mid-submit. |
| 3. Trace ID + sourceability | 9.5 | Mọi TC có TraceID link SRS line / SCR-VIII-08 component / FR-VIII-22 step. STATE/UI/PERSIST đầy đủ. Phụ lục field-index map field → SRS line → TC ID. |
| 4. Independence + idempotency | 9.0 | TC-REG-103 → 196 → 197 chain explicit. TC-REG-180/181/182 (ERR trùng) phụ thuộc TC-REG-102 (data đã tạo). Pre-cond chung của file ghi rõ. TC-REG-198/199 race idempotent test. |
| 5. Maintainability | 9.2 | Pre-condition chung file rõ. SPEC-CLARIFY tách 14 entries (TKPQ-30..43). Field index phụ lục map dễ tra. |
| 6. Phase B executability (UI/MCP) | 9.0 | Public form không OTP — login MCP unauth context. MailHog API verify (`http://103.172.236.130:8025`). Một số TC defer Phase B: TC-REG-104 (chờ 31 phút), TC-REG-198 (race fast double click), TC-REG-209 (network throttle), TC-REG-212 (storage cleanup). A7 BẮT BUỘC chạy sau để filter API-only. |
| **Average** | **9.27** | Quality target ≥ 8.5 — **PASS** |

### 8.2 Issue list UC120

**Critical:** Không có.

**Major:**

| Major ID | TC | Issue | Action |
|----------|-----|-------|--------|
| MAJ-A6-UC120-01 | TC-REG-104 | Token vĩnh viễn — verify bằng wait 31 phút (không feasible env real-time) | Defer Phase B với note "manual time check / time-travel mock" |
| MAJ-A6-UC120-02 | TC-REG-198/199/209 | Race condition + network mid-submit — cần test infra hỗ trợ throttle/concurrent | Defer Phase B với note "DevTools throttle + 2 client" |

**Minor:**

| Minor ID | TC | Issue | Action |
|----------|-----|-------|--------|
| MIN-A6-UC120-01 | TC-REG-211 | Email IDN test — RFC 5322 vs 6531 (SRS không rõ chuẩn nào) | SPEC-CLARIFY-TKPQ-43 forward BA |
| MIN-A6-UC120-02 | TC-REG-205 | MIME spoof — cần file binary thực tế (`malicious.exe` rename `malicious.pdf`); test env cần có file fixture | Phase B prepare fixture |
| MIN-A6-UC120-03 | TC-REG-212 | File storage cleanup — KHÔNG verify được qua UI direct, defer storage admin check | Phase B note manual |

### 8.3 A6 Fill Gap (forward từ A5) — đã INLINE MERGE

| A5 Gap ID | TC mới | File UC | Status |
|-----------|--------|---------|--------|
| A5-GAP-14 | TC-REG-220 (Form tab order + group label SCR-VIII-08) | 12-TC-self-registration-dn.md | ✅ inline merged |
| A5-GAP-15 | TC-REG-221 (Mail HTML format kích hoạt) | 12-TC-self-registration-dn.md | ✅ inline merged |
| A5-GAP-16 | TC-REG-222 (SMTP MailHog API connectivity) | 12-TC-self-registration-dn.md | ✅ inline merged |
| A5-GAP-17 | TC-REG-223 (File upload network response storage URL/UUID) | 12-TC-self-registration-dn.md | ✅ inline merged |

### 8.4 Tổng count UC120 (sau A6)

```
12-TC-self-registration-dn.md → 68 TC
                                  Section A Happy: 6
                                  Section B Validation Nhóm 1: 23
                                  Section C Validation Nhóm 2: 18
                                  Section D ERR-REG: 6
                                  Section E Security/Audit/Integration: 10
                                  Section F Edge (A4): 13
                                  Section G A6 Fill: 4
```

**Tổng cumulative W1.4 sau UC120 + A6:** 200 + 68 = **268 TC** (184 functional + 16 security + 68 UC120 functional). Final count sẽ adjust sau A7 filter (loại / sửa TC chỉ-DB/API thuần).

**UC120 Phase A status (sau A6):** A1-A6 ✅ done. A7 ⏳ pending. Sau A7 → Phase A UC120 PASS.
