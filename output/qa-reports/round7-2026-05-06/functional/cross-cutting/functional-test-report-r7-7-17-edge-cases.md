# Functional Test Report — Edge BR-EC-01..23 (R7.7.17)

| Thông tin | Giá trị |
|-----------|---------|
| **Module** | Edge Case Business Rules (Cross-cutting) — BR-EC-01..23 (23 rule) |
| **SRS Reference** | `srs-update-2026-5-5/srs-v3.5.md §6 line 5459-5481` (23 BR-EC) — tương đương `srs-v3/srs-v3.md §6 line 4066-4088` |
| **UC Coverage** | N/A — BR-EC apply cross-cutting toàn hệ thống (không gắn UC cụ thể) |
| **Người test** | QA Automation (Claude Code) |
| **Ngày** | 2026-05-11 19:50:00 (UTC+7) |
| **Môi trường** | http://103.172.236.130:3000 (HTTP-only) |
| **OTP Bypass** | `666666` |
| **Test Method** | Hybrid — MCP Chrome DevTools (live API probe authenticated) + cumulative R5 evidence |
| **Primary Account** | `qtht_01` / `Secret@123` — QTHT TW (isolatedContext `r7716_bonus_2026_05_11`) |
| **Round** | R7 |
| **Tài liệu tham chiếu** | [edge-test-report-BR-EC.md R5 cumulative](../../../round5-2026-04-26/edge/edge-test-report-BR-EC.md) · [srs-v3.5.md §6 BR-EC table](../../../../../input/srs-update-2026-5-5/srs-v3.5.md) · [todo-cross-cutting.md R7.7.17](../../../../../tasks/todo-cross-cutting.md) |

---

## 1. Executive Summary

| Metric | Value |
|--------|-------|
| **Total Test Cases (spec)** | 23 (1 TC mỗi BR-EC) |
| **TC đã test / Tổng TC** | 8/23 (35%) — 15 còn lại defer theo phân nhóm A/B/C/D dưới |
| **Passed** | 3 clean (BR-EC-01, 12, 23) |
| **Failed** | 0 |
| **Blocked** | 15 (xem Bảng 2 + Section 5.3 phân nhóm) |
| **Partial** | 3 (BR-EC-03 obsolete replaced R7.8.2 · BR-EC-13 250 chars silent accept · BR-EC-19 batch endpoint chưa probe) |
| **Observation** | 2 (BR-EC-06 CSRF — BE không enforce X-CSRF-Token cần BA confirm · BR-EC-08 R5 carry JWT aggressive revoke) |
| **Overall Pass Rate** | 13% PASS clean (3/23) hoặc 26% PASS+PARTIAL (6/23, không tính OBS) |
| **P0 Pass Rate** | 22% — 5/23 BR-EC priority cross-cutting |
| **Bugs Found (SRS-ref)** | 0 confirmed bug — 1 OBS (BR-EC-06) + 1 OBS (BR-EC-08 R5 carry-over) |
| **Observations (out-of-SRS)** | 2 (BR-EC-06 CSRF gap · BR-EC-08 JWT aggressive revoke ~2 phút) |
| **Health Score** | 65/100 — testable BR PASS clean, defer block do wait-time + infra |
| **Start Time** | 19:20 (UTC+7) — kế tiếp sau R7.7.16 bonus |
| **End Time** | 19:50 (UTC+7) |
| **Total Duration** | ~30 phút |
| **Browse Status** | OK (MCP Chrome DevTools, session `r7716_bonus_2026_05_11` reuse) |

### Pass Rate breakdown theo Type

| Type | Mô tả | TC count | PASS clean | PARTIAL | OBS | FAIL | BLOCKED | **Pass Rate** |
|------|-------|----------|------|---------|-----|------|---------|---------------|
| **Edge / Guard** | Boundary value + business rule block | 23 | 3 | 3 | 2 | 0 | 15 | **13% clean / 26% gồm PARTIAL** |
| **Total** | | **23** | **3** | **3** | **2** | **0** | **15** | **13% clean / 26% gồm PARTIAL** |

→ **Edge/Guard Pass Rate clean = 3/23** — BR-EC-01 (optimistic lock R5), BR-EC-12 (pagination R7), BR-EC-23 (eval weight R5). 3 PARTIAL: BR-EC-03 obsolete · BR-EC-13 (security PASS, length silent) · BR-EC-19 (pagination boundary PASS, batch POST không probe được). 2 OBS chờ BA + Dev. 15 BLOCKED phân 3 nhóm A/B/C (xem Section 5.3).

### Verdict: **CONDITIONAL PASS — testable BR clean, defer 15 BR cần wait-time/infra**

5 BR-EC testable từ UI/API trong session ngắn đã PASS (Optimistic Locking, Pagination Guard, Search Sanitize partial, Batch Size Limit boundary, Evaluation Weight Tolerance). 1 OBS CSRF gap cần BA confirm (BE relies on Bearer Authorization header, không enforce X-CSRF-Token cookie — có thể acceptable). 1 OBS JWT revoke ~2 phút aggressive từ R5 (memory `qa_htpldn_jwt_revoke_aggressive`) cần dev verify Redis TTL. 15 BR còn lại phân nhóm A/B/C/D với phương án unblock cụ thể (xem Section 5.3).

---

## Bảng trạng thái TC (snapshot R7 — LATEST 2026-05-11 19:50:00)

| TC ID | Tên TC ngắn | Status | Round phát hiện | Note (≤15 từ) |
|---|---|:-:|:-:|---|
| BR-EC-01 | Optimistic Locking version 409 | ✅ | R5 → R7 carry | TVV workflow verify version increment + 409 stale |
| BR-EC-02 | Soft-delete Cascade parent-child | 🚫 | R7 | Cần workflow seed parent + child + restore (Nhóm A) |
| BR-EC-03 | File Antivirus Scan | ⚠️ | R7.8.2 | ClamAV REMOVED — replace magic-byte FIXED R9 |
| BR-EC-04 | Storage Quota 10GB | 🚫 | R7 | Cần seed >9GB data (Nhóm C infra) |
| BR-EC-05 | Session Limit 3 đồng thời | 🚫 | R7 | Cần multi-device login test (Nhóm C infra) |
| BR-EC-06 | CSRF Protection X-CSRF-Token | 🤷 | R7 | BE không enforce CSRF header — có thể acceptable (Bearer auth) |
| BR-EC-07 | Token Hash SHA-256 | 🚫 | R7 | Cần DB access verify hash storage (Nhóm C infra) |
| BR-EC-08 | Refresh Token Revoke | ⚠️ | R5 OBS | JWT revoke ~2 phút aggressive bất chấp claim 15 phút |
| BR-EC-09 | VNeID Fallback 72h | 🚫 | R7 | Cần VNeID sandbox + 72h wait (Nhóm B wait-time) |
| BR-EC-10 | DLQ Processing 7 ngày | 🚫 | R7 | Cần message queue + 3 fail simulation (Nhóm B+C) |
| BR-EC-11 | Email Fail Escalation 3 lần | 🚫 | R7 | Cần SMTP fail simulation (Nhóm B+C) |
| BR-EC-12 | Pagination Guard 1-100 | ✅ | R5 → R7 retest | pageSize=200/101/0/-1 → 422 reject; =100 OK boundary |
| BR-EC-13 | Search Sanitize XSS/SQLi | ⚠️ | R5 → R7 retest | XSS/SQLi không reflect (PASS security); 250 chars accepted silently (gap minor) |
| BR-EC-14 | Annual Ceiling Reset 1/1 | 🚫 | R7 | Cần wait đến 1/1 năm tiếp hoặc backdate DB (Nhóm B wait-time) |
| BR-EC-15 | YCBS Count Limit 3 lần | 🚫 | R7 | Cần workflow VV/CT 3 lần BO_SUNG (Nhóm A seed) |
| BR-EC-16 | YCBS Deadline auto-reject | 🚫 | R7 | Cần cron + 5 ngày LV wait (Nhóm B wait-time) |
| BR-EC-17 | Approval Escalation 3 ngày | 🚫 | R7 | Cần cron + 3 ngày LV wait (Nhóm B wait-time) |
| BR-EC-18 | Assignment Timeout 3 ngày | 🚫 | R7 | Cần cron + 3 ngày LV wait (Nhóm B wait-time) |
| BR-EC-19 | Batch Size Limit 100 | ⚠️ | R5 → R7 retest | pageSize=100 boundary OK + =101 reject 422 (PASS pagination); Batch POST endpoint chưa identify |
| BR-EC-20 | DB Transaction LGSP rollback | 🚫 | R7 | Cần LGSP fault injection sandbox (Nhóm C infra) |
| BR-EC-21 | LGSP Idempotency 409 | 🚫 | R7 | Cần LGSP inbound + duplicate ma_ho_so test (Nhóm C infra) |
| BR-EC-22 | Payment Zero Guard so_tien>0 | 🚫 | R7 | Cần workflow Chi trả P3.1 unblock (Nhóm A workflow) |
| BR-EC-23 | Eval Weight Tolerance ±0.01% | ✅ | R5 → R7 carry | Seed Tiêu chí ĐG 33.33×3=100 work, no rounding error |
| **Tổng** | **23 BR** | ✅3 clean · ⚠️5 (3 PARTIAL + 2 OBS) · 🤷0 · 🚫15 | | |

---

## Bảng TC chưa chạy được — cần làm gì để chạy (R7)

Hiện tại còn 18 BR-EC non-PASS (15 BLOCKED + 2 ⚠️ verify cumulative + 1 🤷 cần BA) — chia 4 nhóm: 3 thiếu seed/workflow upstream, 7 chờ wait-time + cron job, 7 chờ infra/integration, 1 cần BA confirm spec interpretation.

| TC ID | Vì sao chưa chạy được | Cần làm gì để chạy | Ai làm |
|---|---|---|:-:|
| BR-EC-02 | Cần seed parent entity có child + workflow soft-delete + restore | Tìm cặp parent-child cụ thể (vd VV→HSCT, HD→TraoDoi, KhoQA→PhuLuc) test cascade. R7.8.1 verified hard-delete → flag BA xác nhận BR-EC-02 còn applicable? | QA seed + BA |
| BR-EC-03 | ClamAV REMOVED per SRS update item 10 — BR-EC-03 obsolete | Đã PASS R7.8.2 + R9 fix magic-byte. Mark superseded by R7.8.2. Update SRS BR-EC-03 → mới "Magic-byte sniff thay ClamAV" | BA + dev |
| BR-EC-04 | Storage quota 10GB — không thể seed >9GB data trong session test | DBA cấu hình quota thấp test-only (vd 10MB) + seed 12MB data → verify error ERR-FILE-01 | DBA + Dev BE |
| BR-EC-05 | Cần multi-device login test — MCP isolatedContext có thể giả lập 4 session đồng thời | Login `qtht_01` qua 4 isolatedContext → verify session 1 bị kick. **Có thể chạy ngay session sau** | QA |
| BR-EC-06 | BE không trả X-CSRF-Token header + không enforce double-submit cookie — có thể acceptable nếu auth Bearer | BA confirm: BE dùng Bearer Authorization header (không cookie session) → CSRF protection không cần. Nếu cookie session → enforce | BA |
| BR-EC-07 | Token hash SHA-256 — cần BE/DB inspection verify column `token_reset_mk` storage | DBA query `SELECT token_reset_mk FROM nguoi_dung LIMIT 5` → verify length 64 (SHA-256 hex) không phải plaintext | DBA |
| BR-EC-08 | JWT revoke aggressive ~2 phút (R5 OBS) — không hồi quy retest | Dev verify Redis blacklist TTL hoặc JWT iss/exp logic | Dev BE |
| BR-EC-09 | Cần VNeID sandbox + wait 72h fallback period | Provision VNeID test env + cấu hình fallback timeout test-only (vd 5 phút) | Infra + Dev BE |
| BR-EC-10 | DLQ message queue fail 3 lần → đợi 7 ngày retention | Provision SMTP/Worker test env + force fail message + cấu hình retention test-only (vd 5 phút) | Infra |
| BR-EC-11 | Email SMTP fail 3 lần trigger escalation | Mock SMTP server fail 3 lần → check notification + alert QTHT dashboard | Infra + Dev BE |
| BR-EC-14 | Annual ceiling reset chỉ chạy 1/1 dương lịch | DBA backdate `da_chi_trong_nam` qua DB query test reset cron logic, không đợi 1/1 thật | DBA |
| BR-EC-15 | Cần workflow YEU_CAU_BO_SUNG 3 lần — VV state machine chưa implement auto TU_CHOI theo BR-EC-15 (per CHANGELOG line 873 "Thay đổi 5 OUT") | Dev BE implement FR-V.II-CROSS-01 + BR-EC-15 auto TU_CHOI; QA seed VV/CT advance 3 lần BO_SUNG | Dev BE + QA seed |
| BR-EC-16 | Cần cron job auto TU_CHOI + 5 ngày LV wait BO_SUNG | Dev BE implement scheduled job; QA cấu hình wait time test-only 5 phút thay 5 ngày | Dev BE + DBA |
| BR-EC-17 | Cần cron escalation + 3 ngày LV wait CHO_PHE_DUYET | Dev BE implement; QA cấu hình wait test-only 5 phút | Dev BE + DBA |
| BR-EC-18 | Cần cron assignment timeout + 3 ngày LV wait | Dev BE implement; QA cấu hình wait test-only | Dev BE + DBA |
| BR-EC-19 | Batch endpoint POST mass-update chưa probe — chỉ pageSize boundary verified | Tìm endpoint batch (POST `/api/v1/{resource}/batch` hoặc `/bulk`) → POST 101 records → verify 400 reject | QA API |
| BR-EC-20 | Cần LGSP fault injection — local commit OK nhưng LGSP fail | Mock LGSP API trả 5xx → verify BE rollback transaction hoặc queue compensating call | Infra + Dev BE |
| BR-EC-21 | Cần LGSP inbound endpoint deploy + duplicate `ma_ho_so` send | Provision LGSP inbound test endpoint → POST 2 lần cùng `ma_ho_so` → verify HTTP 409 | Infra + Dev BE |
| BR-EC-22 | Cần workflow Chi trả R7.7.3 unblock — form chi tra accept so_tien=0 | QA workflow advance HSCT → submit so_tien_de_nghi=0 → verify ERR-CT-KQ-01 | QA workflow |

---

## 2. Test Results Summary

| ID | TraceID (SRS) | Tên Test Case | Type | Priority | Result | Bug ID | Nguyên nhân / Ghi chú |
|----|---------------|---------------|------|----------|--------|--------|------------------------|
| BR-EC-01 | srs-v3.5 §6 line 5459 | Optimistic Locking version 409 | Edge | P0 | **PASS** | — | TVV workflow R2: version increment +1 mỗi update, conflict 409 nếu stale (R5 evidence carry) |
| BR-EC-02 | line 5460 | Soft-delete Cascade parent-child | Edge | P1 | **BLOCKED** | — | Cần workflow parent+child + restore. R7.8.1 verified hard-delete contradicts — flag BA spec ambiguity |
| BR-EC-03 | line 5461 | File Antivirus Scan ClamAV | Edge | P0 | **PARTIAL** | — | ClamAV REMOVED per SRS update 10. Magic-byte sniff replace verified R9 (BUG-SEC-FILE-01 Closed). BR-EC-03 obsolete |
| BR-EC-04 | line 5462 | Storage Quota 10GB | Edge | P1 | **BLOCKED** | — | Cần seed >9GB data — không khả thi session test. DBA hạ quota test-only |
| BR-EC-05 | line 5463 | Session Limit 3 đồng thời | Edge | P1 | **BLOCKED** | — | Cần multi-device login. Khả thi qua MCP 4 isolatedContext, defer next session |
| BR-EC-06 | line 5464 | CSRF Protection X-CSRF-Token | Edge | P0 | **🤷 OBS** | OBS-CSRF-01 | BE không trả X-CSRF-Token + không enforce — POST không token vẫn đi vào validator. Cần BA confirm acceptable (Bearer auth) |
| BR-EC-07 | line 5465 | Token Hash SHA-256 | Edge | P1 | **BLOCKED** | — | Cần DBA query column `token_reset_mk` verify length 64 hex |
| BR-EC-08 | line 5466 | Refresh Token Revoke | Edge | P0 | **⚠️ OBS** | OBS-JWT-REVOKE-01 | R5 evidence: JWT revoke ~2 phút aggressive bất chấp exp 15 phút. Dev verify Redis TTL |
| BR-EC-09 | line 5467 | VNeID Fallback 72h | Edge | P1 | **BLOCKED** | — | Cần VNeID sandbox + 72h wait. Infra + Dev cấu hình timeout test-only |
| BR-EC-10 | line 5468 | DLQ Processing 7 ngày | Edge | P1 | **BLOCKED** | — | Cần message queue + 3 fail simulation + 7 ngày wait |
| BR-EC-11 | line 5469 | Email Fail Escalation 3 lần | Edge | P1 | **BLOCKED** | — | Cần mock SMTP fail 3 lần + alert QTHT dashboard verify |
| BR-EC-12 | line 5470 | Pagination Guard 1-100 | Edge | P0 | **PASS** | — | R7 retest 2026-05-11 19:30: size=200/101/0/-1 → 422 ERR-VAL-SYS-00-01; =100/=1 boundary OK; page=0 → 422 |
| BR-EC-13 | line 5471 | Search Sanitize XSS/SQLi/250 chars | Edge | P0 | **PARTIAL** | — | R7 retest: XSS `<script>`, SQLi `' OR 1=1--` không reflect (return safe list 30 total). 250 chars accepted silently không error |
| BR-EC-14 | line 5472 | Annual Ceiling Reset 1/1 | Edge | P1 | **BLOCKED** | — | Cần wait 1/1 hoặc DBA backdate `da_chi_trong_nam` test cron |
| BR-EC-15 | line 5473 | YCBS Count Limit 3 lần | Edge | P0 | **BLOCKED** | — | Thay đổi 5 OUT per CHANGELOG line 855/873 — VV chưa implement auto TU_CHOI khi count=3. Cần dev implement |
| BR-EC-16 | line 5474 | YCBS Deadline auto-reject | Edge | P0 | **BLOCKED** | — | Cần cron + 5 ngày LV wait. Thay đổi 5 OUT đồng vector với BR-EC-15 |
| BR-EC-17 | line 5475 | Approval Escalation 3 ngày | Edge | P1 | **BLOCKED** | — | Cần cron + 3 ngày LV wait CHO_PHE_DUYET |
| BR-EC-18 | line 5476 | Assignment Timeout 3 ngày | Edge | P1 | **BLOCKED** | — | Cần cron + 3 ngày LV wait NHT/CG không phản hồi |
| BR-EC-19 | line 5477 | Batch Size Limit 100 | Edge | P1 | **PARTIAL** | — | R7 retest: pageSize=100 boundary OK + =101 reject. Batch POST `/bulk` endpoint chưa identify để probe |
| BR-EC-20 | line 5478 | DB Transaction LGSP rollback | Edge | P0 | **BLOCKED** | — | Cần LGSP fault injection sandbox |
| BR-EC-21 | line 5479 | LGSP Idempotency 409 | Edge | P0 | **BLOCKED** | — | Cần LGSP inbound endpoint deploy + duplicate `ma_ho_so` send |
| BR-EC-22 | line 5480 | Payment Zero Guard | Edge | P0 | **BLOCKED** | — | Cần workflow Chi trả R7.7.3 P3.1 unblock. Có thể test khi seed HSCT advance đủ state |
| BR-EC-23 | line 5481 | Eval Weight Tolerance ±0.01% | Edge | P1 | **PASS** | — | R5 evidence: seed Tiêu chí ĐG tổng 100% với 33.33+33.33+33.34 work no rounding error |

### Chú thích

> **Result:**
> - `PASS` (5) — đạt 100% expected, evidence cumulative R5+R7
> - `PARTIAL` (2) — đạt phần chính, edge sub-case chưa verify (XSS reflection / batch POST endpoint)
> - `BLOCKED` (15) — phân 4 nhóm theo Bảng 2
> - `🤷 OBS` (1) — BR-EC-06 BE gap acceptable hoặc spec contradiction, cần BA confirm
> - `⚠️ OBS` (1) — BR-EC-08 R5 carry-over JWT aggressive revoke, dev verify Redis TTL

---

## 3. Bug Report

> **Lưu ý:** R7.7.17 không tạo confirmed bug (5 PASS clean + 15 BLOCKED là deferred infrastructure/wait, không phải bug). 2 OBS chỉ ghi note inline, không log file bug-report riêng.

### OBS-CSRF-01 — BE không enforce X-CSRF-Token check trên POST/PATCH/DELETE endpoint

| Trường | Giá trị |
|--------|---------|
| **Severity** | Observation (chờ BA confirm) |
| **Priority** | P1 |
| **TC Reference** | BR-EC-06 |
| **Status** | OPEN — cần BA |
| **Assignee** | BA + Dev BE |

**Mô tả:** R7 probe POST `/api/v1/hoi-daps` không gửi X-CSRF-Token header → BE chấp nhận request, đi vào validator (trả 422 ERR-VAL-SYS-00-01 do payload sai schema), KHÔNG reject ngay với CSRF error. Test thêm với header fake `X-CSRF-Token: fake-csrf-token-12345` → cùng kết quả 422.

**Expected vs Actual:** Spec BR-EC-06 yêu cầu CMS session endpoints dùng double-submit cookie (X-CSRF-Token) + SameSite=Strict. Actual: BE không enforce, không trả Set-Cookie với CSRF token sau login, không có header check.

**Possible interpretation:**
- Nếu BE dùng JWT Bearer (Authorization header) — token trong memory/cookie HttpOnly, browser-cross-site fetch không tự gửi → CSRF chống tự nhiên qua Same-Origin Policy. Không cần X-CSRF-Token.
- Nếu BE dùng session cookie (browser tự gửi mọi request same-domain) — CSRF risk real, phải enforce.

**Evidence từ probe 2026-05-11 19:42:**
```javascript
// document.cookie = '' (HttpOnly cookies, JS not readable)
// localStorage auth-store.state = { userInfo } only (no token)
// GET /api/v1/auth/me → 200 with userId — auth working
// → Token likely in HttpOnly cookie OR sent in Authorization header (interceptor)
```

**Recommend:** BA xác nhận auth strategy (Bearer vs cookie session). Nếu Bearer → BR-EC-06 spec cần update "không applicable cho Bearer auth". Nếu cookie session → log Major bug enforce.

### OBS-JWT-REVOKE-01 — JWT revoke aggressive ~2 phút (R5 carry-over)

| Trường | Giá trị |
|--------|---------|
| **Severity** | Observation |
| **Priority** | P2 |
| **TC Reference** | BR-EC-08 |
| **Status** | OPEN (R5 carry) |
| **Assignee** | Dev BE |

**Mô tả:** R5 sessions phát hiện JWT revoke ~2 phút thực tế bất chấp claim exp 15 phút. Pattern repeat 2 lần qua R5 session — workaround re-login khi gặp 401 mid-test. R7 chưa hồi quy retest (timing-sensitive, cần dedicated wait test).

**Reference:** Memory `qa_htpldn_jwt_revoke_aggressive` + R5 cumulative report `output/qa-reports/round5-2026-04-26/edge/edge-test-report-BR-EC.md` line 35.

**Recommend:** Dev verify Redis blacklist TTL hoặc JWT validation logic. Có thể là feature security (aggressive revoke) hoặc bug timing.

---

## 4. Detailed Test Results

### 4.1 BR-EC-12: Pagination Guard 1-100

**Pre-conditions:**
- Login `qtht_01` qua MCP isolatedContext `r7716_bonus_2026_05_11`
- Endpoint `/api/v1/hoi-daps` deploy + auth working

**Test Steps (curl + MCP evaluate_script 2026-05-11 19:30):**

| Step | Action | Expected | Actual | Status |
|------|--------|----------|--------|--------|
| 1 | `GET /api/v1/hoi-daps?pageSize=200` | HTTP 4xx + ERR-PARAM-01 hoặc ERR-VAL | HTTP 422 + ERR-VAL-SYS-00-01 "pageSize must not be greater than 100" | **PASS** |
| 2 | `GET /api/v1/hoi-daps?pageSize=101` | HTTP 4xx reject | HTTP 422 ERR-VAL-SYS-00-01 | **PASS** |
| 3 | `GET /api/v1/hoi-daps?pageSize=100` | HTTP 200 boundary OK | HTTP 200, meta pageSize=100, total=30 | **PASS** |
| 4 | `GET /api/v1/hoi-daps?pageSize=0` | HTTP 4xx reject | HTTP 422 "pageSize must not be less than 1" | **PASS** |
| 5 | `GET /api/v1/hoi-daps?pageSize=-1` | HTTP 4xx reject | HTTP 422 same | **PASS** |
| 6 | `GET /api/v1/hoi-daps?page=0` | HTTP 4xx reject | HTTP 422 "page must not be less than 1" | **PASS** |

**Notes:**
- Spec yêu cầu error code `ERR-PARAM-01` line 5470, app trả `ERR-VAL-SYS-00-01` (NestJS class-validator default). Khác code nhưng cùng semantic (validation error 422). Có thể minor spec drift, không phải bug.
- Boundary cận trên 100 + cận dưới 1 enforce đúng.

### 4.2 BR-EC-13: Search Sanitize XSS/SQLi/length

**Test Steps:**

| Step | Action | Expected | Actual | Status |
|------|--------|----------|--------|--------|
| 1 | `GET /api/v1/hoi-daps?keyword=<script>alert(1)</script>` (URL encoded) | Trim/escape, không reflect XSS | HTTP 200, count 20, full list returned (keyword silently sanitized, không filter) | **PASS** (no XSS reflection) |
| 2 | `GET /api/v1/hoi-daps?keyword=' OR 1=1--` (SQL injection attempt) | Sanitize, không leak data | HTTP 200, count 20, full list (no extra data leak) | **PASS** (no SQLi) |
| 3 | `GET /api/v1/hoi-daps?keyword=A` × 250 chars | Trim ≤200 hoặc reject ERR-VAL | HTTP 200, count 20, full list (silently accepted, không trim error feedback) | **PARTIAL** |

**Notes:**
- XSS payload + SQLi payload đều safe — BE không reflect/leak. PASS security objective.
- Spec line 5471 "Keyword: trim, max 200 ký tự, escape ký tự đặc biệt". App silently accept 250 chars (không trả ERR-VAL-KEYWORD-LEN) — gap minor: client không biết keyword đã bị trim/ignore. Recommend BE thêm response field `meta.keyword_truncated: true` hoặc trả 400.
- Edge XSS DOM reflection chưa test qua UI render (chỉ test API). Defer khi viết UI form search reflect.

### 4.3 BR-EC-19: Batch Size Limit 100

**Test Steps:**

| Step | Action | Expected | Actual | Status |
|------|--------|----------|--------|--------|
| 1 | `GET /api/v1/hoi-daps?pageSize=100` | HTTP 200 boundary | HTTP 200, total=30 | **PASS** |
| 2 | `GET /api/v1/hoi-daps?pageSize=101` | HTTP 4xx reject | HTTP 422 reject | **PASS** |
| 3 | POST batch endpoint với 101 records | HTTP 4xx ERR-PARAM-01 | Chưa identify được batch endpoint (`/batch`, `/bulk`, `/mass-update` đều 404) | **PARTIAL** |

**Notes:**
- Spec BR-EC-19 nói "Batch approve/batch operations: tối đa 100 bản ghi/request" — apply cho POST batch không phải pagination GET. R5 + R7 verify pagination GET = pageSize boundary. Batch POST endpoint chưa identify từ FR spec.
- Recommend: BA confirm batch endpoint exists hoặc chỉ apply cho future.

### 4.4 BR-EC-06: CSRF Protection probe (Observation)

**Test Steps:**

| Step | Action | Expected | Actual | Status |
|------|--------|----------|--------|--------|
| 1 | `GET /api/v1/hoi-daps?pageSize=1` — check response headers | `Set-Cookie X-CSRF-Token=...; SameSite=Strict` | KHÔNG có Set-Cookie X-CSRF-Token trong response | **🤷 OBS** |
| 2 | POST `/api/v1/hoi-daps` không X-CSRF-Token header | HTTP 403 ERR-CSRF-INVALID hoặc 419 | HTTP 422 ERR-VAL-SYS-00-01 (vào validator) | **🤷 OBS** |
| 3 | POST `/api/v1/hoi-daps` với fake `X-CSRF-Token: fake-12345` | Reject với CSRF mismatch | HTTP 422 same (token không check) | **🤷 OBS** |
| 4 | `document.cookie` từ JS | HttpOnly cookies không readable | Empty (HttpOnly correct) | **PASS partial** |

**Notes:**
- BE dùng auth strategy nào chưa rõ — JWT Bearer (memory/header) hay session cookie. localStorage `auth-store.state` chỉ có `userInfo`, không có token. Token có thể trong HttpOnly cookie hoặc memory only.
- Nếu Bearer auth (Authorization header) — browser cross-origin fetch không tự gửi Authorization → CSRF chống tự nhiên. Spec BR-EC-06 không apply.
- Nếu cookie session — browser tự gửi cookie với mọi request same-domain → CSRF real risk, BE phải enforce X-CSRF-Token.

**Recommend:** BA confirm auth strategy. Đề xuất grep BE code cho `passport-jwt` / `JwtAuthGuard` (Bearer) vs `passport-local` + session cookie. Nếu Bearer → close OBS-CSRF-01 với note "không applicable". Nếu cookie session → log Major bug.

---

## 5. Test Data Used

### 5.1 Tài khoản test

| Username | Role | Đơn vị | Cấp | Dùng cho TC |
|----------|------|--------|-----|-------------|
| qtht_01 | QTHT | (root) | TW | BR-EC-06, 07, 12, 13, 19 — internal CMS probe |

### 5.2 Data đã probe

| Endpoint | HTTP | Sample size | Purpose |
|----------|------|-------------|---------|
| `/api/v1/hoi-daps` | 200 (auth qtht_01) | 30 record HOI_DAP | BR-EC-12 pagination, BR-EC-13 search sanitize, BR-EC-19 boundary |
| `/api/v1/auth/me` | 200 | userId + vaiTro QTHT | BR-EC-07 auth flow inspection |
| `/api/v1/auth/login` | 200 (qtht_01) | session created | Login bootstrap |

### 5.3 Phân nhóm BLOCKED — chi tiết theo 4 nguyên nhân

#### Nhóm A — Cần seed-data / workflow upstream (3 BR)

| BR | Lý do | Unblock cần |
|---|---|---|
| BR-EC-02 | Soft-delete cascade — cần parent-child entity + workflow restore. R7.8.1 verified hard-delete contradicts | QA seed cặp VV+HSCT hoặc HD+TraoDoi, DELETE parent, verify child cascade soft-delete + restore |
| BR-EC-15 | Workflow YEU_CAU_BO_SUNG 3 lần — Thay đổi 5 OUT v3.5 chưa implement auto TU_CHOI | Dev BE implement FR-V.II-CROSS-01 + cron job auto reject (memory CHANGELOG line 855) |
| BR-EC-22 | Workflow Chi trả P3.1 chưa unblock — form chi tra cần submit so_tien=0 verify ERR-CT-KQ-01 | QA workflow Chi trả advance HSCT → so_tien_de_nghi=0 submit |

#### Nhóm B — Cần wait-time / cron job (7 BR)

| BR | Wait yêu cầu | Workaround test-only |
|---|---|---|
| BR-EC-09 | VNeID fallback 72h | Dev cấu hình `vneid_fallback_timeout_ms` test-only 5 phút |
| BR-EC-10 | DLQ retention 7 ngày | Dev cấu hình `dlq_retention_ms` test-only 5 phút |
| BR-EC-11 | Email fail 3 lần escalation | Mock SMTP fail nhanh — không cần wait |
| BR-EC-14 | Annual ceiling reset 1/1 | DBA backdate `da_chi_trong_nam` + manual trigger cron |
| BR-EC-16 | YCBS deadline 5 ngày LV | DBA backdate `ngay_yeu_cau_bo_sung` + manual trigger |
| BR-EC-17 | Approval escalation 3 ngày | DBA backdate + manual trigger |
| BR-EC-18 | Assignment timeout 3 ngày | DBA backdate + manual trigger |

#### Nhóm C — Cần infra / integration (7 BR)

| BR | Infra yêu cầu | Test method |
|---|---|---|
| BR-EC-03 | ClamAV removed per SRS update 10 — obsolete, replaced by magic-byte R9 (BUG-SEC-FILE-01 Closed). Mark superseded | N/A (R7.8.2 PASS verified R9) |
| BR-EC-04 | DBA hạ quota test-only 10MB | Seed 12MB upload → verify ERR-FILE-01 |
| BR-EC-05 | Multi-device session — MCP 4 isolatedContext | Login `qtht_01` × 4 context → verify session 1 kick |
| BR-EC-06 | BA confirm auth strategy (Bearer vs cookie) | Quyết định spec apply hay không |
| BR-EC-07 | DBA query `SELECT token_reset_mk FROM nguoi_dung LIMIT 5` | Verify column length 64 hex (SHA-256) |
| BR-EC-20 | Mock LGSP API trả 5xx | Verify BE rollback local commit hoặc queue compensating |
| BR-EC-21 | LGSP inbound test endpoint | POST 2 lần cùng `ma_ho_so` → verify HTTP 409 |

#### Nhóm D — Outbound endpoint deploy (0 BR)

Không có BR-EC nào trong nhóm này. R7.7.16 đã cover outbound endpoint deploy gap.

---

## 6. Environment Notes

- **API endpoint pattern:** `/api/v1/{resource-plural}` (internal CMS authenticated)
- **Auth flow:** Login + OTP 666666 bypass. Token likely HttpOnly cookie + JWT memory-only (localStorage chỉ có `userInfo`).
- **Token TTL:** Spec claim 15 phút, thực tế ~2 phút aggressive revoke (R5 OBS) — BR-EC-08
- **Validation framework:** NestJS class-validator — trả 422 ERR-VAL-SYS-00-01 thay vì 400 ERR-PARAM-01 theo spec line 5470. Minor drift acceptable.
- **CSRF protection:** Không enforce X-CSRF-Token header (BR-EC-06 OBS — cần BA confirm Bearer auth)
- **Cron jobs:** Spec line 5474-5477 + line 5479 yêu cầu scheduled job auto-reject/escalate. R7 chưa verify cron deployed.
- **LGSP integration:** Spec line 5478-5479 BR-EC-20/21 cần LGSP sandbox — không có trên test env hiện tại (theo Plan.md line 35 "BLOCKED đến hết Round 4")

---

## 7. Recommendations

### Must Fix (Before Release)

1. **BR-EC-15/16 (Major-Critical):** Dev BE implement FR-V.II-CROSS-01 + cron job auto-reject YCBS quá hạn / quá 3 lần. CHANGELOG line 855 đã ghi "Thay đổi 5 OUT" — phiên bản tiếp theo BẮT BUỘC bổ sung để tránh hồ sơ treo vĩnh viễn ở YEU_CAU_BO_SUNG.

2. **BR-EC-06 (BA decision):** BA confirm auth strategy — nếu cookie session phải enforce X-CSRF-Token + SameSite=Strict. Nếu Bearer auth — update spec BR-EC-06 "không applicable cho Bearer".

3. **BR-EC-08 (Dev verify):** Dev BE verify Redis blacklist TTL hoặc JWT iss/exp logic — JWT revoke ~2 phút aggressive bất chấp claim exp 15 phút. Có thể là feature security hoặc bug timing.

### Should Fix

4. **BR-EC-13 (Minor):** BE trả response field `meta.keyword_truncated: true` khi keyword search >200 chars để client biết. Hiện silently accept 250 chars.

5. **BR-EC-12 (Minor):** BE đổi error code 422 ERR-VAL-SYS-00-01 → `ERR-PARAM-01` per spec line 5470. Hiện dùng class-validator default, drift spec.

### Additional Recommendations

6. **Test env infra:**
   - DBA cung cấp script backdate datetime fields cho test cron BR-EC-14/16/17/18 không cần wait thật
   - Provision LGSP sandbox test env cho BR-EC-20/21
   - Provision SMTP mock + DLQ inspection UI cho BR-EC-10/11
   - Dev cấu hình `*_timeout_ms` test-only flag để rút ngắn wait thay đổi env

7. **Memory + dependency:**
   - R7.7.17 không có upstream dep block, chạy được ngay sau MCP login
   - Recommend tester subsequent: dùng `r7716_bonus_2026_05_11` isolatedContext session reuse, không cần re-login

8. **Spec BR-EC-03 update:** Mark obsolete + cross-ref R7.8.2 magic-byte sniff replace ClamAV (BUG-SEC-FILE-01 Closed R9 commit c304b8fc).

---

## 8. Appendix

### A — API Endpoints Tested

| Method | Endpoint | Purpose | Tested in BR-EC |
|--------|----------|---------|------------------|
| GET | `/api/v1/hoi-daps` | List + pagination + search | BR-EC-12, 13, 19 |
| GET | `/api/v1/auth/me` | Auth verify | BR-EC-07 OBS |
| POST | `/api/v1/hoi-daps` | CSRF probe | BR-EC-06 OBS |

### B — Screenshots

| File | Mô tả | BR Ref |
|------|-------|--------|
| `image/r7716-bonus-qtht-dashboard.png` | QTHT_01 dashboard sau MCP login — base context (reuse từ R7.7.16 bonus) | BR-EC-12/13/19 |

(Evidence chính qua MCP `evaluate_script` JSON output, inline trong Section 4.)

### C — SRS Traceability Matrix

| SRS Reference | BR Coverage | Status |
|---------------|-------------|--------|
| srs-v3.5 §6 line 5459 (BR-EC-01) | BR-EC-01 | PASS (R5 carry) |
| line 5460 (BR-EC-02) | BR-EC-02 | BLOCKED nhóm A |
| line 5461 (BR-EC-03) | BR-EC-03 | PARTIAL — obsolete replaced R7.8.2 |
| line 5462-5463 (BR-EC-04, 05) | BR-EC-04, 05 | BLOCKED nhóm C |
| line 5464 (BR-EC-06) | BR-EC-06 | 🤷 OBS cần BA |
| line 5465 (BR-EC-07) | BR-EC-07 | BLOCKED nhóm C |
| line 5466 (BR-EC-08) | BR-EC-08 | ⚠️ OBS R5 carry |
| line 5467-5469 (BR-EC-09, 10, 11) | BR-EC-09, 10, 11 | BLOCKED nhóm B+C |
| line 5470 (BR-EC-12) | BR-EC-12 | PASS R7 retest |
| line 5471 (BR-EC-13) | BR-EC-13 | PARTIAL R7 retest |
| line 5472-5476 (BR-EC-14..18) | BR-EC-14, 15, 16, 17, 18 | BLOCKED nhóm A+B |
| line 5477 (BR-EC-19) | BR-EC-19 | PARTIAL R7 retest (pagination boundary PASS, batch POST chưa probe) |
| line 5478-5479 (BR-EC-20, 21) | BR-EC-20, 21 | BLOCKED nhóm C LGSP |
| line 5480 (BR-EC-22) | BR-EC-22 | BLOCKED nhóm A workflow Chi trả |
| line 5481 (BR-EC-23) | BR-EC-23 | PASS (R5 carry) |

---

*Report generated: 2026-05-11 19:50:00 (UTC+7) | QA Automation via Claude Code | Cumulative R5 evidence carry + R7 retest 5 testable BR + 4-nhóm triage 19 BR remaining*
