# A7 Filter Log — CT HTPLDN GĐ1

> **Ngày**: 2026-05-06 · **Phase**: A7 (Manual filter UI/function-testable per `tasks/detailed-tc/plan.md` §3.1)
> **Mục đích**: Log số TC LOẠI / SỬA / GIỮ sau A7 Filter rule.

---

## A7 Filter Rule (recap §3.1 plan.md)

| Action | Tiêu chí |
|--------|---------|
| ❌ **LOẠI** | TC require DB query trực tiếp / curl API thuần / cron-job background không có UI feedback |
| ✏️ **SỬA** | TC verify-DB → verify-network qua MCP `list_network_requests`; TC API-only nếu module có UI bridge → re-route qua UI flow |
| ✅ **GIỮ** | TC chạy 100% qua UI/function user-facing (verify network gián tiếp khi user thao tác UI vẫn OK) |

---

## Action log per TC file

### 01-TC-quan-ly-ct-CRUD.md (15 TC)

| Action | Count | TC ID | Lý do |
|--------|------:|-------|-------|
| ✅ Giữ | 15 | TC-CT-CRUD-001..017, TC-CT-AUDIT-001 | Tất cả qua UI SCR-XI-01 (CRUD form + table). TC-CT-AUDIT-001 verify qua module Nhật ký HT (FR-10) — UI có sẵn. Network verify qua MCP `list_network_requests` gián tiếp khi user thao tác UI. |
| ❌ Loại | 0 | — | — |
| ✏️ Sửa | 0 | — | — |

### 02-TC-tim-kiem-ct.md (12 TC)

| Action | Count | TC ID | Lý do |
|--------|------:|-------|-------|
| ✅ Giữ | 12 | TC-CT-TK-001..012 | UI search filter-bar + Export Excel. TC-TK-009 (page_size) verify qua URL manipulation + UI behavior — user-facing. SQL/XSS sanitize verify qua UI render + network response. |
| ❌ Loại | 0 | — | — |

### 03-TC-lifecycle-ct.md (17 TC)

| Action | Count | TC ID | Lý do |
|--------|------:|-------|-------|
| ✅ Giữ | 17 | TC-LC-001..017 | Tất cả qua action-bar Tab Thông tin SCR-XI-01. State guard verify nút button visibility + network response. |
| ❌ Loại | 0 | — | — |

### 04-TC-trinh-phe-duyet-ct.md (6 TC)

| Action | Count | TC ID | Lý do |
|--------|------:|-------|-------|
| ✅ Giữ | 6 | TC-TR-CT-001..006 | UI [Gửi phê duyệt] button + state transition + notification UI. |

### 05-TC-phe-duyet-ct.md (10 TC)

| Action | Count | TC ID | Lý do |
|--------|------:|-------|-------|
| ✅ Giữ | 10 | TC-PD-CT-001..010 | UI action-bar + modal confirm + lý do. TC-PD-CT-010 (notification) verify qua UI Notification panel — user-facing. |

### 06-TC-cong-bo-ct.md (9 TC)

| Action | Count | TC ID | Lý do |
|--------|------:|-------|-------|
| ✅ Giữ | 9 | TC-CB-CT-001..009 | UI [Công bố]/[Hủy CB] button + verify outbound API (Cổng PLQG) qua MCP `list_network_requests` — gián tiếp khi user click UI. Rollback verify qua reload page UI. |
| ❌ Loại | 0 | — | — |
| **Note** | — | — | TC-CB-CT-001 verify outbound API tới Cổng PLQG (FR-XII-15) — **A7 filter pass** vì user trigger qua UI [Công bố], API call là consequence chứ không phải direct test endpoint. |

### 07-TC-quan-ly-dot-bc.md (10 TC)

| Action | Count | TC ID | Lý do |
|--------|------:|-------|-------|
| ✅ Giữ | 10 | TC-DOT-BC-001..010 | UI Tab "Đợt báo cáo" + modal CRUD + state guard. |

### 08-TC-permission-matrix.md (6 TC)

| Action | Count | TC ID | Lý do |
|--------|------:|-------|-------|
| ✅ Giữ | 6 | TC-PERM-CT-001..006 | UI permission verify: sidebar visibility + 403 page + force deep-link UI behavior. |

---

## Tổng kết A7

| Metric | Value |
|--------|------:|
| Total TC sau A6 | 85 |
| ✅ Giữ | 85 (100%) |
| ❌ Loại | 0 |
| ✏️ Sửa | 0 |
| **Total Phase A final** | **85 TC** |

**Acceptance D0.5 plan.md**: ✅ 0 TC còn keyword "verify DB row", "check index", "curl POST", "cron job", "background worker" không có UI bridge.

---

## Verification grep (proof 0 keyword forbidden)

Manual scan các file UC 01-08:
- `verify DB row` → 0 hits
- `check INDEX` → 0 hits
- `curl POST` → 0 hits
- `cron job` → 0 hits
- `background worker` → 0 hits

Mọi TC verify qua UI flow + network inspection (`list_network_requests`) — UI-driven.

*Generated 2026-05-06 — Phase A step A7 filter log*
