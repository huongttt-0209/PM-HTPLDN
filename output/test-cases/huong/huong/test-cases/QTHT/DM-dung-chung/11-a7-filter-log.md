# A7 — UI/Function-Testable Filter Log (DM Dùng Chung)

> **Date:** 2026-05-08
> **Mode:** Manual scan + Edit IN-PLACE
> **Reference:** [`plan.md` §3.1 A7 Filter rule](../../../tasks/detailed-tc/plan.md). Nguyên tắc:
> - ❌ LOẠI: TC require DB query trực tiếp / curl API thuần / cron job no-UI
> - ✏️ SỬA: TC verify-DB → verify-network qua MCP `list_network_requests`; TC API-only → re-route qua UI flow
> - ✅ GIỮ: TC chạy 100% UI/function user-facing + verify network qua MCP

---

## 1. Scan kết quả

| File | Total TC | Vi phạm | Action |
|------|---------|---------|--------|
| 01-TPL-DM-CRUD | 58 | 0 | — |
| 02-Smoke-11-DM | 55 | 0 | — |
| 03-Cơ quan ĐV | 35 | 0 | — |
| 04-Tiêu chí HQ | 20 | 0 | — |
| 05-Tiêu chí CP | 17 | 0 | — |
| 06-Chương trình HT | 11 | 0 | — |
| 07-Tình trạng VV | 11 | 0 | — |
| 08-Loại DN | 10 | 0 | — |
| 09-Hồ sơ thành phần | 16 | 0 | — |
| 10-Permission matrix | 16 | 1 | ✏️ SỬA TC-PERM-008 |
| **Tổng (sau A7 ban đầu)** | **249** | **1** | **0 LOẠI / 1 SỬA / 248 GIỮ** |
| **Tổng (sau R3 Codex review)** | **255 active** | **3 LOẠI + 7 REPHRASE** | **3 LOẠI / 7 SỬA / 245 GIỮ** |

---

## 2. Action chi tiết

### 2.1 SỬA — TC-PERM-008

**Trước A7:**
> Tiền điều kiện: cb_nv_tw_03 đăng nhập, qua API curl POST `/api/v1/danh-muc` (CREATE)
> Bước: Direct API call
> KQ mong đợi: API trả 403 với code ERR-AUTH-01; KHÔNG bypass UI

**Lý do vi phạm:** "Direct API call" qua curl ngoài UI — vi phạm A7 (không có UI bridge). Tester chạy MCP chrome-devtools KHÔNG curl được trực tiếp.

**Sau A7 (đã edit IN-PLACE file 10):**
> Tiền điều kiện: cb_nv_tw_03 đăng nhập (browser context có session), mở DevTools → tab Network
> Bước: Trong DevTools Console fire `fetch('/api/v1/danh-muc', {method:'POST', headers:{'Content-Type':'application/json'}, body:JSON.stringify({ma:'TEST',ten:'Test'})})` rồi check response
> KQ mong đợi: API trả 403 với code ERR-AUTH-01; verify network request từ MCP `list_network_requests`; KHÔNG bypass UI auth

**Cách verify mới:** Tester dùng MCP `evaluate_script` để fire fetch từ authenticated browser context (cùng session sau login UI). MCP `list_network_requests` capture response 403. Đây là UI bridge hợp lệ vì:
- Browser session đã được tạo qua UI login
- Fetch được gọi qua DevTools Console (UI surface)
- Response capture qua MCP network inspect

### 2.2 R3 Codex review — fix A7 violations + false positives

**3 TC LOẠI (R3 Codex review 2026-05-08):**

| ID | Lý do | File |
|----|-------|------|
| TC-LV-036 | Case-insensitive search là assumption — BR-EC-13 không nói case-insensitive (chỉ trim/max 200/escape ký tự đặc biệt) | 01 |
| TC-LV-044 | Dropdown ở Hỏi đáp = cross-module behavior, out-of-scope W1.3 (test ở FR-02) | 01 |
| TC-PERM-008 | DevTools Console fetch() = API-call chủ động ngoài user UI flow, vi phạm A7. Coverage cb_nv API auth đã có TC-PERM-005..007 (UI direct URL → 403) | 10 |

**7 TC REPHRASE (R3 Codex review):**

| ID | Lý do trước | Action sau R3 | File |
|----|-------------|---------------|------|
| TC-LV-026 | "Last-write-wins" assumption | Verify behavior, log finding `[SPEC-CLARIFY-DM-28]` | 01 |
| TC-LV-027 | "DB is_deleted=1" direct DB | UI list refresh + audit log cross-ref Nhật ký HT W1.1 | 01 |
| TC-LV-EDGE-001 | "KHÔNG có 2 record cùng mã trong DB" | UI list refresh chỉ 1 record + audit 1 INSERT | 01 |
| TC-LV-EDGE-006 | Regex escape (assumption-prone) | BR-EC-13 "escape ký tự đặc biệt truy vấn" — literal match | 01 |
| TC-LV-FILL-002 | "Verify schema" no UI bridge | Form UI fields + audit log BR-DATA-03 cross-ref | 01 |
| TC-CQDV-021 | "Đổi cap không impact" assumption | Verify alert phân quyền (line 1478) + behavior + SPEC-CLARIFY-DM-29 | 03 |
| TC-CQDV-EDGE-003 | Session invalidate assumption | Verify behavior observed (200/403/redirect), no expected | 03 |
| TC-HS-012 | Drag-drop UI assumption | Generic "edit thứ tự via UI mechanism khả dụng" | 09 |

> **Codex SAI (Codex bị nhầm — KEEP):** TC-CQDV-032 alert phân quyền (SRS line 1478 nguyên văn), TC-TCCP seed NĐ18/2026 (SRS line 571 nguyên văn). 2 finding này verified vs SRS rồi reject — Codex fail step 1 R3.

### 2.3 Cross-cutting verify

- ✅ TC-LV-033 + TC-LV-FILL-003 verify audit log: dùng cross-ref module Nhật ký HT W1.1 (UI module riêng) → UI bridge OK
- ✅ TC-LV-FILL-001 verify BR-AUTH-08 ngoại lệ: list render đầy đủ (UI verify, không cần DB query)
- ✅ TC-LV-FILL-002 verify common fields: form chi tiết hiển thị (UI display) — không phải DDL inspect
- ✅ TC-CQDV-EDGE-002 performance: verify expand <2s qua UI timing — không phải explain plan SQL

---

## 3. Acceptance A7 + R3 Codex review

**A7 ban đầu (2026-05-08):**
- ✅ Manual scan 249 TC × 10 file done
- ✅ 1 TC SỬA inline (TC-PERM-008 file 10) — sau bị Codex challenge ở R3, LOẠI hoàn toàn
- ✅ 0 TC LOẠI ban đầu

**R3 Codex review (2026-05-08):**
- ✅ Verified 12 Codex findings vs SRS — 2 reject (Codex sai), 3 LOẠI, 7 REPHRASE
- ✅ 3 TC LOẠI thực sự (TC-LV-036 case-insensitive, TC-LV-044 cross-module, TC-PERM-008 DevTools fetch)
- ✅ 7 TC REPHRASE để verify hành vi UI/audit thay vì DB direct hoặc assumption
- ✅ 0 TC còn assumption-only expected outcome — mọi TC giờ tham chiếu SRS line, BR explicit, hoặc log SPEC-CLARIFY khi spec im lặng
- ✅ 0 TC vi phạm A7 sau R3 — TC-PERM-008 đã LOẠI hẳn, các REPHRASE đều có UI bridge rõ

---

## 4. Phase A — DONE

| Step | Status | Output |
|------|--------|--------|
| A1 — Đọc SRS | ✅ | (không output file) |
| A2 — Test plan overview | ✅ | `00-test-plan-overview.md` |
| A3 — UC test files | ✅ | 10 files `01..10-TC-*.md` (228 TC base) |
| A4 — Edge case hunter | ✅ | `08-REVIEW-edge-case-hunter.md` (audit) + 18 TC inline merged → 246 TC |
| A5 — Traceability | ✅ | `09-traceability-matrix.md` (audit) — 3 GAP forward |
| A6 — Test review | ✅ | `10-REVIEW-test-quality.md` (audit) + 3 fill TC inline → 249 TC |
| A7 — UI filter | ✅ | `11-a7-filter-log.md` (audit) + 1 SỬA TC-PERM-008 → 249 TC |
| **R1 Codex fix** | ✅ | Count headers + scope wording + ID conflict (5 sub-tasks); 0 TC change |
| **R2 Codex fill** | ✅ | Coverage gaps → +9 TC inline (UC103 ×3, UC109 ×4, UC110 ×2) → 258 TC |
| **R3 Codex review** | ✅ | False positives + A7 violations → −3 LOẠI + 7 REPHRASE → 255 TC active |
| **R4 Codex cleanup** | ✅ | 9 SPEC-CLARIFY verified clear theo SRS (DM-03/05/07/10/14/15/16/17/27) → expected explicit, không cần BA. **SPEC-CLARIFY 29 → 20** |

**Total Phase A active:** **255 TC** (258 declared − 3 LOẠI R3) — vs estimate 187 plan §6.1, +68 cover sâu SRS sau Codex full review (R1+R2+R3+R4).

**SPEC-CLARIFY active:** **20 entries** (29 trước R4 − 9 cleared) — gửi BA Phase B.
- Cleared R4: DM-03 (thu_tu Y), DM-05 (trong_so range), DM-07 (BR-CALC cap), DM-10 (TW NULL cha), DM-14 (max 100), DM-15 (BN/DP nút thêm con), DM-16 (cha=TW), DM-17 (1 TW root), DM-27 (Export out-scope)
