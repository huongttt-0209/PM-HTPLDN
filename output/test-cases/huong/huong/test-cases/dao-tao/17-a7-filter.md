# A7 — Environment Reality Filter (FR-03 Đào tạo)

> **Phase:** A7 of BMAD A1-A7 — final filter
> **Date:** 2026-05-09
> **Input:** 313 TC (post-A6) across 13 files
> **Env:** http://103.172.236.130:3000/ + Chrome DevTools MCP + accounts users.csv (Secret@123, OTP=666666)
> **Method:** 3-category filter (KEEP / SỬA / LOẠI), DEFER tracked separately
> **Caps:** LOẠI ≤8, SỬA ≤30, DEFER unlimited (with reason)

---

## 1. Filter Summary

| Category | Count | % of 313 |
|---|---:|---:|
| KEEP (unchanged) | 294 | 93.9% |
| SỬA (rewrite observable) | 5 | 1.6% |
| LOẠI (delete) | 4 | 1.3% |
| DEFER (Phase B env tooling) | 10 | 3.2% |
| **TOTAL** | **313** | **100%** |

**Active TC for Phase B (Phase B smoke):** 313 - 4 (LOẠI) = **309 TC** (10 DEFER chỉ chạy nếu env tooling sẵn).

---

## 2. Per-file delta

| File | TC pre-A7 | KEEP | SỬA | LOẠI | DEFER | TC post-A7 active |
|---|---:|---:|---:|---:|---:|---:|
| 01 KH năm Đào tạo | 30 | 29 | 1 | 0 | 0 | 30 |
| 02 CTĐT quản lý | 33 | 32 | 1 | 0 | 0 | 33 |
| 03 Đề xuất đào tạo | 17 | 17 | 0 | 0 | 0 | 17 |
| 04 Lịch học + AT cron | 19 | 15 | 0 | 1 | 3 | 18 (15 KEEP + 3 DEFER) |
| 05 KH quản lý + SM | 34 | 31 | 1 | 2 | 0 | 32 |
| 06 Đăng ký đào tạo | 26 | 26 | 0 | 0 | 0 | 26 |
| 07 Điểm danh + KQ | 34 | 34 | 0 | 0 | 0 | 34 |
| 08 Công bố KQ + CN | 19 | 16 | 0 | 0 | 3 | 19 (16 KEEP + 3 DEFER) |
| 09 Bài giảng | 28 | 27 | 0 | 0 | 1 | 28 (27 KEEP + 1 DEFER) |
| 10 NHCH + Đề KT | 33 | 33 | 0 | 0 | 0 | 33 |
| 11 Giảng viên | 23 | 23 | 0 | 0 | 0 | 23 |
| 12 Xuất ký số | 18 | 13 | 0 | 1 | 3 | 17 (13 KEEP + 3 DEFER) |
| 13 Permission Matrix | 19 | 17 | 2 | 0 | 0 | 19 |
| (audit) 14-16 | — | — | — | — | — | — |
| **TOTAL** | **313** | **313 (294+5SỬA+14 affected)** | **5** | **4** | **10** | **309 active + 10 DEFER** |

> Note: KEEP cột = TC giữ nguyên Kết quả mong đợi text. SỬA cột = TC giữ nhưng cell Kết quả đã rewrite cho UI/network observable.

---

## 3. LOẠI list (delete reasons)

| TC ID | File | Reason | Replacement (if any) |
|---|---|---|---|
| TC-LICH-S-018 | 04 Lịch học | Timezone test cần DB server timezone control (env không expose admin TZ override). SRS không quote convention timezone (SPEC-CLARIFY-DT-EC-05) → defer assumption "BE store + compare UTC", không testable smoke. | — Replace by Phase B production check (SPEC-CLARIFY-DT-EC-05 follow-up) |
| TC-KH-N-034 | 05 KH quản lý | Explicit recap "xem TC-KH-N-009" — A6 flagged acceptable nhưng A7 trim slim. Coverage không mất. | — Already covered by TC-KH-N-009 (ERR-KH-01) |
| TC-KH-N-035 | 05 KH quản lý | Explicit recap "xem TC-KH-N-014" — A7 trim slim. Coverage không mất. | — Already covered by TC-KH-N-014 (ERR-KH-04 / BR-FLOW-03) |
| TC-XUAT-E-018 | 12 Xuất ký số | Storage disk full — environmental, không có cách reproduce trong env smoke; rare edge case không justify mock infra build. SPEC-CLARIFY-DT-EXP-07 vẫn pending BA. | — Replace by infra monitoring (out of QA scope) |

**Total LOẠI: 4** (cap ≤8 — well within budget).

---

## 4. SỬA list (rewrite reasons)

| TC ID | File | Before observability | After observability |
|---|---|---|---|
| TC-KH-NAM-E-027 | 01 KH năm | "5. Query AUDIT_LOG" + "verify 4 row AUDIT_LOG" + immutable check assumed DB | "5. qtht_01 mở FR-10 W1.1 Nhật ký HT, filter entity_id" → table render 4 entries với actor/thoi_gian/du_lieu_cu/du_lieu_moi visible. Immutable verify qua "UI KHÔNG có nút edit/delete". |
| TC-CTDT-E-029 | 02 CTĐT | "6. Query AUDIT_LOG" — DB direct verify | "6. qtht_01 mở FR-10 W1.1, filter entity_id=CTDT-001" → bảng hiển thị ≥4 entries với actor + ip_address. Immutable qua UI no edit/delete. |
| TC-KH-E-042 | 05 KH | "Query AUDIT_LOG WHERE entity_id" + verify 8 row + immutable assumed | "qtht_01 mở FR-10 W1.1 Nhật ký HT, filter entity_id" → table render 8 entries (CREATE/SUBMIT/APPROVE/PUBLISH/START/END/SUBMIT_RESULT/APPROVE_RESULT). 2 AUTO_TRANSITION SYSTEM verify riêng ở file 04 (DEFER). |
| TC-PERM-E-018 | 13 Permission | "Admin update role qua API" assumed direct DB | "qtht_01 demote cb_nv_tw_03 qua FR-10 W1.4 TKPQ UI Tab 2; cb_nv_tw_03 click [Lưu] ở Tab 1" → 2-tab observable. Network panel hiển thị PUT 403 + toast vai trò đổi. |
| TC-PERM-E-019 | 13 Permission | "Curl loop 1000 + observe response" — ambiguous tooling | "Bash loop curl từ host máy chạy QA. Đếm response code 200 vs 429 aggregate" — observable qua curl exit codes + HTTP code log. |

**Total SỬA: 5** (cap ≤30 — comfortable margin).

---

## 5. DEFER list (Phase B env tooling required)

| TC ID | File | Why deferred to Phase B | Required tool |
|---|---|---|---|
| TC-LICH-S-013 | 04 Lịch học | Cron auto-transition `DA_CONG_KHAI → DANG_DIEN_RA` cần đợi cron tick (5 phút) — env không expose admin trigger endpoint | Seed time đã expire HOẶC admin POST /api/v1/internal/cron/transition-khoa-hoc (BE expose) |
| TC-LICH-S-014 | 04 Lịch học | Cron auto-transition `DANG_DIEN_RA → DA_KET_THUC` cùng pattern | Same as S-013 |
| TC-LICH-S-015 | 04 Lịch học | Cron idempotency 2 tick liên tiếp — verify qua FR-10 W1.1 audit UI | FR-10 W1.1 ready + cron tick 2 lần |
| TC-CB-E-001 | 08 Công bố KQ | Mass 100 HV CN — cần heavy seed 100 HV DAT (env không sẵn lượng này) | Phase B performance round seed lớn |
| TC-CB-N-005 | 08 Công bố KQ | Service ký số BHXH/CA fail mock — env cần admin toggle disable signing service | Mock signing service toggle (env config) |
| TC-CB-E-005 | 08 Công bố KQ | Storage rate-limit 429 partial — cần mock storage trả 429 cho 1/4 calls | Mock storage rate-limit toggle |
| TC-BG-029 | 09 Bài giảng | Multipart upload network drop — cần Chrome DevTools "Throttling: Offline" toggle giữa upload (manual operator) | Operator manual + Chrome DevTools |
| TC-XUAT-N-009 | 12 Xuất ký số | Service BHXH-CA ký số DOWN — cần mock signing service toggle | Mock signing service OFF config |
| TC-XUAT-N-010 | 12 Xuất ký số | Template file MISSING — cần infra remove file (server-side action) | Infra coordinate Phase B |
| TC-XUAT-E-016 | 12 Xuất ký số | Service ký số timeout (mock delay 30s) — cần mock service delay config | Mock signing service delay config |

**Total DEFER: 10.** Phase B run dependencies:
- 3 TC (S-013, S-014, S-015) phụ thuộc cron tick + FR-10 W1.1 audit UI ready (đã done per memory `fr10_w11_phase_b_progress`).
- 4 TC (CB-N-005, CB-E-005, XUAT-N-009, XUAT-E-016) phụ thuộc mock service toggle config.
- 1 TC (CB-E-001) phụ thuộc Phase B performance round (heavy seed).
- 1 TC (BG-029) phụ thuộc operator manual + DevTools.
- 1 TC (XUAT-N-010) phụ thuộc infra remove template file.

---

## 6. Final TC stats

| Metric | Count |
|---|---:|
| TC total written (post-A6) | 313 |
| TC LOẠI A7 | 4 |
| TC DEFER A7 (Phase B env tooling) | 10 |
| TC SỬA A7 (rewrite observable) | 5 |
| TC KEEP unchanged | 294 |
| TC active for Phase B smoke (KEEP+SỬA) | **299** |
| TC total post-A7 (active + DEFER) | **309** |
| TC reduced from A6 → A7 | -4 (LOẠI) |
| FR-10 W1.1 audit UI dependency | 3 SỬA TC + 3 DEFER TC = 6 TC phụ thuộc FR-10 W1.1 ready |
| FR-10 W1.4 TKPQ dependency | 1 SỬA TC (TC-PERM-E-018 role demote) |
| Mock signing service dependency | 3 DEFER TC (CB-N-005, XUAT-N-009, XUAT-E-016) |
| Mock storage rate-limit dependency | 1 DEFER TC (CB-E-005) |
| BR coverage (carry from A5) | 14/14 = 100% |
| SM transitions (carry from A5) | 13/13 = 100% |
| ERR codes (carry from A5) | 23/23 = 100% |
| FR coverage (carry from A5) | 22/22 = 100% |

---

## 7. Phase B handoff notes

### Run order (per dependency in 02-thu-tu-module §⑨ + plan §1.2)

1. **File 01** (KH năm Đào tạo) — depend on FR-10 W1.1 audit UI ready cho TC-027.
2. **File 02** (CTĐT quản lý) — depend on FR-10 W1.3 DM Lĩnh vực PL DA_DUYET seed + FR-10 W1.1 audit UI cho TC-029.
3. **File 03** (Đề xuất đào tạo) — depend on Cổng PLQG mock + DN/NHT seed accounts.
4. **File 11** (Giảng viên) — depend on FR-04 TVV DANG_HOAT_DONG seed (run trước file 05).
5. **File 09** (Bài giảng) — depend on KH DA_DUYET seed (file 05 prereq).
6. **File 10** (NHCH + Đề KT) — depend on FR-10 DM Lĩnh vực + BAI_GIANG seed (file 09).
7. **File 05** (KH quản lý) — depend on CTĐT DA_DUYET (file 02) + GV (file 11) + BG (file 09). **Critical path file** — SM-KHOAHOC 11 transitions.
8. **File 06** (Đăng ký) — depend on KH DA_CONG_KHAI seed (file 05).
9. **File 04** (Lịch học) — depend on KH DANG_DIEN_RA seed (file 05) + cron tick wait (3 DEFER TC).
10. **File 07** (Điểm danh + KQ) — depend on KH DANG_DIEN_RA + HV DA_DUYET (file 06) + buổi học (file 04).
11. **File 08** (Công bố KQ + CN) — depend on KH CHO_DUYET_KQ (file 07) + mock services (3 DEFER).
12. **File 12** (Xuất ký số) — depend on CTĐT DA_DUYET/DA_CONG_KHAI/HOAN_THANH (file 02 + file 08) + mock signing service (3 DEFER).
13. **File 13** (Permission Matrix) — chạy cuối, cross-cấp negative + 2 tab role demote (depend FR-10 W1.4 ready).

### Required seed (recap from overview §4.3)

- **CTĐT seed:** 3 record DA_DUYET ở 3 cấp (TW/BN/ĐP), 1 DU_THAO TW, 1 DA_CONG_KHAI, 1 HOAN_THANH (cho file 12 export).
- **Khóa học seed:** Mỗi state SM-KHOAHOC có ≥1 record (9 state × 1) + 1 KH DANG_DIEN_RA có ≥3 HV.
- **KH với time-driven AT prereq (DEFER):** ≥1 KH DA_CONG_KHAI có `ngay_bat_dau ≤ NOW()` + ≥1 KH DANG_DIEN_RA có `ngay_ket_thuc < NOW()` để đợi cron tick.
- **Bài giảng seed:** 5 PPTX + 3 PDF + 2 YouTube (đa LV PL, đa cong_khai true/false).
- **NHCH seed:** 50 câu hỏi (đa loại + đa LV + đa độ khó), 3 Đề KT (10/20/30 câu).
- **GV seed:** 5 GV TVV active (FR-04) + 1 GV manual.
- **HV seed:** 10 DN (FR-07) × ≥1 HV → 10+ DANG_KY DA_DUYET. 1 KH có 100 HV DAT cho TC-CB-E-001 DEFER.
- **Đề xuất seed:** 3 đề xuất MOI (NHT 1 + DN 2).

### Tools required

- **Chrome DevTools MCP** (primary tool per CLAUDE.md): `mcp__chrome-devtools__*` cho auth + UI navigation + network inspection + screenshot.
- **FR-10 W1.1 Nhật ký HT UI**: phải ready cho 5 TC SỬA audit verify + 3 DEFER cron audit.
- **FR-10 W1.4 TKPQ UI**: phải ready cho TC-PERM-E-018 role demote 2-tab test.
- **curl/bash**: cho TC-PERM-E-019 rate limit loop.
- **pdfsig CLI** (poppler-utils) + **unzip**: cho TC-XUAT-H-007/H-008 signature verify (binary check, available locally).
- **Mock signing service** (env coordinate): cho 3 DEFER TC (CB-N-005, XUAT-N-009, XUAT-E-016).
- **Mock storage rate-limit** (env coordinate): cho TC-CB-E-005 DEFER.

### Known blockers

- **5 critical SPEC-CLARIFY pending BA** (must resolve trước Phase B per A6 §7):
  - DT-01 (SM-KHOAHOC `DA_DUYET → DA_CONG_KHAI` transition) — block file 05 + file 01
  - DT-DK-02 (CB NV thêm HV manual default state) — block file 06 TC-DK-H-004
  - DT-DK-03 (BR-FLOW-04 áp dụng UC22 reject ĐK) — block file 06 TC-DK-N-004
  - DT-CB-09 (PDF rate limit partial fail strategy) — DEFER A7 TC-CB-E-005 dependent
  - DT-EC-14 (BG xóa cascade khi gắn đề KT DA_PHAN_PHOI) — block file 10 TC-DEKT-015
- **41 SPEC-CLARIFY total** (per A6) — các tickets ngoài 5 critical có thể test với assumption + flag SPEC-CLARIFY trong test result.
- **3 cron-driven TC DEFER** (S-013/014/015) — chỉ chạy được nếu seed time đã expire HOẶC BE expose admin trigger endpoint.

---

## 8. Liên kết

- Plan overview: [`00-test-plan-overview.md`](00-test-plan-overview.md)
- A4 edge audit: [`14-REVIEW-edge-case-hunter.md`](14-REVIEW-edge-case-hunter.md)
- A5 trace matrix: [`15-trace-matrix.md`](15-trace-matrix.md)
- A6 quality review: [`16-quality-review.md`](16-quality-review.md)
- SRS chính: [`srs-fr-03-dao-tao.md`](../../../input/srs-v3/srs-fr-03-dao-tao.md)
- 13 TC files: 01..13 trong cùng folder
- Cross-ref: [02-thu-tu-module §⑨](../../../input/quy-trinh-nghiep-vu/02-thu-tu-module.md), [Permission Matrix](../../permission-matrix.md), [users.csv](../../../input/users.csv)
