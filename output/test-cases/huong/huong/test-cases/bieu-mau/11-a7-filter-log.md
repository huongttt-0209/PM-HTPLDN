# A7 Filter Log — FR-09 Biểu mẫu

> **Ngày**: 2026-05-06 · **Phase**: A7 (Manual filter UI/function-testable per `tasks/detailed-tc/plan.md` §3.1)
> **Mục đích**: Log số TC loại / sửa / giữ sau khi áp A7 Filter rule. Output bắt buộc theo todo.md D0.5 acceptance.

---

## A7 Filter Rule (recap §3.1 plan.md)

| Action | Tiêu chí |
|--------|---------|
| ❌ **LOẠI** | TC require DB query trực tiếp / curl API thuần / cron-job background không có UI feedback |
| ✏️ **SỬA** | TC verify-DB → verify-network qua MCP `list_network_requests`; TC API-only nếu module có UI bridge → re-route qua UI flow |
| ✅ **GIỮ** | TC chạy 100% qua UI/function user-facing (verify network gián tiếp khi user thao tác UI vẫn OK) |

---

## Action log per TC file

### 01-TC-quan-ly-thu-muc.md (12 TC)

| Action | Count | TC ID | Lý do |
|--------|------:|-------|-------|
| ✅ Giữ | 12 | TC-TM-001..022 | Tất cả qua UI SCR-VII-01 (CRUD + Export Excel + Search) |
| ❌ Loại | 0 | — | — |
| ✏️ Sửa | 0 | — | — |

### 02-TC-tim-kiem-thu-muc.md (7 TC)

| Action | Count | TC ID | Lý do |
|--------|------:|-------|-------|
| ✅ Giữ | 7 | TC-BM-201..207 | UI search + filter + sanitize SQL/XSS qua MCP DevTools |

### 03-TC-cong-khai-thu-muc.md (7 TC)

| Action | Count | TC ID | Lý do |
|--------|------:|-------|-------|
| ✅ Giữ | 7 | TC-BM-301..307 | UI publish/unpublish + verify network outbound (gián tiếp) |

### 04-TC-quan-ly-bieu-mau.md (16 TC sau A7)

| Action | Count | TC ID | Lý do |
|--------|------:|-------|-------|
| ✅ Giữ | 13 | TC-BM-UI-04, 401, 402, 403, 404, 405, 406, 407, 408, 409, 410, 411, 412, 414 | UI CRUD + Switch CR-01 + file upload boundary + virus + retry. Network verify ở 404/405 là gián tiếp khi user thao tác UI → vẫn UI-driven. |
| ❌ **Loại** | 1 | **TC-BM-413** (UC98) | **A7 filter strict**: UC98 API outbound thuần — không có UI bridge ở app PM (chỉ Cổng PLQG bên ngoài). User chốt FR-VII-07 LOẠI ở 00-test-plan §1.1. Test API thuần require curl/Postman → vi phạm §3.1. |
| ✏️ Bổ sung (A6) | 3 | TC-BM-401b, TC-BM-420, TC-BM-421 | A6 review: fill gap AC5 + ERR-BM-04 + ERR-BM-05. Tất cả UI-testable. |

### 05-TC-tim-kiem-bieu-mau.md (6 TC)

| Action | Count | TC ID | Lý do |
|--------|------:|-------|-------|
| ✅ Giữ | 6 | TC-BM-501..506 | UI search + sanitize + pagination boundary |

### 06-TC-import-hang-loat.md (8 TC)

| Action | Count | TC ID | Lý do |
|--------|------:|-------|-------|
| ✅ Giữ | 8 | TC-BM-UI-06, 601..607 | UI Wizard SCR-VII-03 + boundary + virus + storage quota |

### 07-TC-permission-matrix.md (6 TC)

| Action | Count | TC ID | Lý do |
|--------|------:|-------|-------|
| ✅ Giữ | 6 | TC-BM-PERM-001..006 | Permission cross-don_vi + low-priv + DN block — tất cả UI-driven. TC-BM-PERM-006 verify URL direct/redirect → UI behavior |

### 08-REVIEW-edge-case-hunter.md (21 TC bổ sung) — UPDATED 2026-05-06

| Action | Count | Lý do |
|--------|------:|-------|
| ✅ Merge inline | 21 | **2026-05-06**: Per plan.md §3.1 forced inline merge rule (lesson learned W2.3) — 21 edge case đã merge vào 7 file UC (01-07). File 08 chuyển thành audit log. |

---

## Tổng kết (sau inline merge 2026-05-06)

| File UC | Pre-merge | Post-merge | Δ |
|---------|----------:|-----------:|--:|
| 01-TC-quan-ly-thu-muc.md | 12 | 16 | +4 |
| 02-TC-tim-kiem-thu-muc.md | 7 | 10 | +3 |
| 03-TC-cong-khai-thu-muc.md | 7 | 9 | +2 |
| 04-TC-quan-ly-bieu-mau.md | 17 (A6+A7) | 22 | +5 |
| 05-TC-tim-kiem-bieu-mau.md | 6 | 8 | +2 |
| 06-TC-import-hang-loat.md | 8 | 11 | +3 |
| 07-TC-permission-matrix.md | 6 | 8 | +2 |
| **GRAND TOTAL UC files** | **63** | **84** | **+21** |

**A7 actions lifecycle:**
- 1 LOẠI: TC-BM-413 (UC98 verify gián tiếp) — vi phạm filter rule
- 3 THÊM (A6): TC-BM-401b, 420, 421 — fill gap AC + ERR
- 21 MERGE (A4): TC-TM-023..026, TC-BM-208..210, 308..309, 415..419, 507..508, 608..610, PERM-007..008

---

## A7 Acceptance check (per plan.md §3.1)

| Tiêu chí | Yêu cầu | Thực tế | Pass? |
|----------|---------|---------|-------|
| 0 TC keyword "verify DB row" | 0 | 0 | ✅ |
| 0 TC keyword "check index" | 0 | 0 | ✅ |
| 0 TC keyword "curl POST" / API thuần | 0 | 0 (TC-BM-413 đã xóa) | ✅ |
| 0 TC "cron job" / "background worker" no-UI | 0 | 0 | ✅ |
| TC require API verify gián tiếp qua MCP `list_network_requests` | OK (UI-driven) | TC-BM-301/302/305/404/405/412 — đều thao tác UI rồi verify network | ✅ |

**Verdict**: ✅ **A7 PASS** — 100% TC UI/function-testable qua chrome-devtools MCP.

---

## Phase A done sign-off

| Step | Output | Status |
|------|--------|--------|
| A1 | Đọc SRS + sibling | ✅ |
| A2 | 00-test-plan-overview.md | ✅ |
| A3 | 7 TC files (01-07) | ✅ |
| A4 | 08-REVIEW-edge-case-hunter.md (+21) | ✅ |
| A5 | 09-traceability-matrix.md (BR 100% / AC 96.4% / ERR 100% sau A6) | ✅ |
| A6 | 10-REVIEW-test-quality.md (score 86.7% PASS) + 3 TC bổ sung vào 04 | ✅ |
| A7 | 11-a7-filter-log.md (xóa TC-BM-413, recount 83 TC) | ✅ |

**Phase A W2.3 Biểu mẫu**: ✅ **DONE 2026-05-06** — sẵn sàng flip todo.md `📝 → ✅` + cell Phase B từ `🚫 chờ A` → `🚫 chờ bug` (3 bug-flow-BIEUMAU).

---

*Generated 2026-05-06 by BMAD A7 (manual filter) — Phase A W2.3 Biểu mẫu*
