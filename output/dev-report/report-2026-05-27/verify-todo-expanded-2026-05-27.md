# Verify Todo EXPANDED — ALL QA-verifiable bugs (2026-05-27, codex revise applied)

> **Plan:** [verify-plan-expanded-2026-05-27.md](verify-plan-expanded-2026-05-27.md)
> **Source:** [clawpatch-bug-summary-2026-05-27.md](clawpatch-bug-summary-2026-05-27.md)
> **Classification:** [all-bugs-classified.json](all-bugs-classified.json)
> **Codex review:** [codex-review-expanded-plan.md](codex-review-expanded-plan.md) — REVISE → fixes applied
> **Scope:** 283 bug QA verify được (55 HIGH + 228 Medium)
> **Wall-time dự kiến:** 7 agent parallel ~40-55h (codex revise — 26-36h not realistic), serial ~161h
> **Sprint 3 = OPTIONAL** (chỉ run nếu S1+S2 finish clean)

## Icon legend

- ⏳ Chưa chạy
- 🔄 Đang chạy
- ✅ Đạt (PASS clean)
- ⚠️ Sai spec (Minor defer)
- ❌ Lỗi (FAIL — bug confirmed)
- 🚫 Không test được (BLOCKED data/env/DBA dependency)
- ⏭️ Hoãn

---

## Bảng tiến độ tổng (3 sprint — codex revise)

| Sprint | Phase | Owner | Bug count | Effort serial | Status |
|---|---|---|--:|--:|:-:|
| — | P0 Setup (sequential ~6h + parallel sub-tasks ~6h) | Agent A + 5 sub-agent | 10 task | ~12h | ⏳ |
| — | Quality gate (2 sample reports per agent) | Coordinator review | per-agent | ~2h | ⏳ |
| S1 | HIGH critical + Top 15-20 Medium UI ngắn | Agent B/C1/C2/D/E/F | 70-75 | ~50h | ⏳ |
| S2 | Medium QA-UI bulk + Medium QA-API short | Agent B/C1/C2/E | ~160 | ~70h | ⏳ |
| S3 | Medium cross-role + Partial-QA + best-effort race | Agent D/F | 44 | ~36h | ⏳ **OPTIONAL** |
| — | Reporter consolidation | Coordinator | 3 task | ~2h30 | ⏳ |
| **Tổng (S1+S2 bắt buộc)** | | | **~233 bug + 13 task** | **~136h serial** | |
| **+ Sprint 3 OPTIONAL** | | | **+44 bug** | **+36h** | |

**Codex revise notes:**
- 7 agent (split C → C1+C2). 6 agent fallback: merge F vào A sau setup.
- Wall-time realistic: **40-55h** với 7 agent đồng thời (S1+S2 mandatory ~30-40h, S3 +10-15h nếu opt-in).
- Best-effort race cap: 50 attempts × 200ms = 10s max per bug. >2h tổng = STOP escalate.
- Partial-QA cần DBA inject BLOCKED >1h → mark 🚫 ngay, không spend QA time fake state.

---

## 🚦 THỨ TỰ CHẠY THEO PHASE (BẮT BUỘC tuân thủ — không nhảy phase)

> **Quy tắc chung:** Không bắt đầu phase mới khi phase trước chưa pass acceptance. Mỗi phase có gate cụ thể ở cột "Pass khi".

### Phase 1 — P0 Sequential Core (Agent A chính, ~6h)

| Thứ tự | Task ID | Tên | Effort | Pass khi |
|:-:|---|---|---|---|
| 1 | **A0.1** | Tạo round8 folder + index README + verify-progress.md | 15p | Folder `bug/`, `image/` tồn tại; README liệt kê đúng 4 file template |
| 2 | **A0.2** | Login 10 account + capture JWT pool `.private/jwt-tokens.txt` (gitignored) | 30p | `wc -l jwt-tokens.txt` ≥ 10 dòng; 10 user login OK qua UI MCP |
| 3 | **A0.3** | Tạo 5 vai trò R8_ Read-only (DG-NoDelete, CT-NoEdit, GV-NoEdit, DN-NoEdit, API-Consumer) | 2h30 | `GET /api/v1/vai-tro?ma=R8_*` trả về 5 role, mỗi role 68-84 quyền |
| 4 | **A0.5** | SRS map 283 bug → SRS file:line table (`srs-map.md`) | 1h30 | File `srs-map.md` chứa mapping cho ≥ 283 bug × SRS ref |
| 5 | **A0.6** | Baseline app version + record-locks init + account-pool ownership table | 1h | File `baseline.md` chứa: version, 6 agent ownership, record-locks rỗng |
| 6 | **A0.7** | API consumer credential setup + MailHog OTP helper + 3 fixture file (clean/failed/virus) | 1h30 | `fixtures/clean-sample.txt` + `eicar-test.txt` tạo OK; MailHog helper test thành công |

> **Phase 1 done →** mark all A0.1-A0.7 ✅ + verify A0.3 5 R8_ roles existing via API → **gate Phase 2**.

### Phase 2 — A0.4 Parallel Seed (4 sub-agent đồng thời, ~3h wall-time / ~7h sum)

> **Spawn 4 Agent (subagent_type=general-purpose) parallel.** Mỗi sub-agent nhận file `seed-plan-a04.md` (sẽ tạo ở Phase 1 hoặc tạo thêm task trước Phase 2) + CLAUDE.md UI-only rule.

| Sub-agent | Task ID | Tên | Effort | Pass khi |
|:-:|---|---|---|---|
| A1 | **A0.4a** | Seed nhóm 1 — Auth/Permission: 5 account dedicated × 5 R8_ role | 1h30 | 5 account `r8_*_01` tạo, login OK, `vaiTros[]` length=1 |
| A2 | **A0.4b** | Seed nhóm 2 — Workflow/Form: CTDT NHAP, KhoaHoc CHO_HOAN_TAT, DotBaoCao TAO_DOT, KHDG, HSCT | 2h | ≥1 record mỗi state đích, verify qua API count |
| A3 | **A0.4c** | Seed nhóm 3 — Cross-tenant: NHCH/TCTV/GV × 2 đơn vị (TW + ĐP) marker prefix | 2h | 12 record (6 entity × 2 ĐV) với marker `TW-R8-MARKER-*` / `BG-R8-MARKER-*` |
| A4 | **A0.4d** | Seed nhóm 4 — Heavy data + virus flag: DN >100 HSCT, EICAR file scan | 1h30-3h | DN có ≥100 HSCT (verify count API); 1 file `trangThaiQuetVirus=VIRUS_DETECTED` |

> **Phase 2 done →** mark A0.4a-d ✅ + run verify query count cho từng state đích → **gate Phase 3**.

### Phase 3 — Quality Gate (Coordinator review, ~2h)

| Thứ tự | Task ID | Tên | Pass khi |
|:-:|---|---|---|
| 11 | **QG1.B** | Agent B 2 sample bug-report → review 6-section + wording describe-not-prescribe | 2 sample đạt template strict, không có forbidden section (Tác động/Đề xuất fix) |
| 12 | **QG1.C1** | Agent C1 2 sample bug-report → review | Same |
| 13 | **QG1.C2** | Agent C2 2 sample bug-report → review | Same |
| 14 | **QG1.D** | Agent D 2 sample bug-report (cross-tenant 2-tab evidence) → review | Cross-tenant evidence valid |
| 15 | **QG1.E** | Agent E 2 sample bug-report (curl evidence cho API contract bugs) → review | curl evidence + UI cross-method |
| 16 | **QG1.F** | Agent F 2 sample bug-report (race + Partial-QA cap) → review | Race attempts ≤ 50, cap 10s/bug |

> **Phase 3 done →** Coordinator approve mọi agent → **gate Phase 4**.

### Phase 4 — Sprint 1: HIGH critical + Top 15-20 Medium UI (~60h serial, ~12-15h parallel 6 agent)

Run 6 agent parallel: **B (7 bug), C1+C2 (38 bug), D (cross-tenant cap), E (API contract), F (race + Partial-QA)**. Chi tiết per-agent bug list ở section "Sprint 1" dưới.

> **Phase 4 done →** mark mọi bug Sprint 1 với verdict TRUE/FALSE/INCONCLUSIVE/BLOCKED + bug-report đầy đủ → **gate Phase 5**.

### Phase 5 — Sprint 2: Medium QA-UI bulk + Medium QA-API short (~70h serial, ~14-18h parallel 4 agent)

Run 4 agent parallel: **B/C1/C2/E** xử lý ~160 Medium bug. Chi tiết ở section "Sprint 2".

> **Phase 5 done →** mark mọi bug Sprint 2 verdict → **gate Phase 6 (chỉ run nếu Phase 4+5 finish clean)**.

### Phase 6 (OPTIONAL) — Sprint 3: Medium cross-role + Partial-QA + best-effort race (~36h)

44 bug nhóm cross-role + race condition. Skip nếu Phase 4+5 không finish clean (codex risk #2).

### Phase 7 — Reporter consolidation (~2h30)

| Thứ tự | Task ID | Tên |
|:-:|---|---|
| N-2 | **R1** | Cumulative TRUE/FALSE ratio per Sprint + extrapolate 283 |
| N-1 | **R2** | Bug-report consolidated `bug/bug-report-sprint{1,2,3}-round8.md` per sprint |
| N | **R3** | Final README cập nhật roadmap + Closed bug rename `Pass-*.md` |

---

## P0 — Setup/Seed (Agent A + 5 sub-agent) — Sequential core ~6h + Parallel sub-tasks ~6h (codex revise)

- ⏳ **A0.1** Tạo round8 folder structure + index README + verify-progress.md
  - **Kết quả:** TBD
  - **Cần có sẵn:** A0.1 sub-task chuẩn bị folder
  - **Effort:** 15p

- ⏳ **A0.2** Verify 10 account login + capture JWT (jwt-tokens.txt gitignored)
  - **Kết quả:** TBD
  - **Cần có sẵn:** A0.1 ✅
  - **Effort:** 30p

- ⏳ **A0.3** Tạo 5+ vai trò Read-only + tài khoản gán (DG-NoDelete, CT-NoEdit, GV-NoEdit, DN-NoEdit, API-consumer)
  - **Kết quả:** TBD
  - **Cần có sẵn:** A0.2 ✅
  - **Effort:** 2h30

### Sequential core (~6h) — Agent A chính

- ⏳ **A0.5** SRS map 283 bug → SRS file:line table
  - **Kết quả:** TBD
  - **Cần có sẵn:** A0.1 ✅
  - **Effort:** 1h30

- ⏳ **A0.6** Baseline app version + deploy timestamp + record-locks.md init + **account-pool ownership table**
  - **Kết quả:** TBD
  - **Cần có sẵn:** A0.1 ✅
  - **Effort:** 1h
  - **Output:** record-locks.md + account-pool.md (Agent B owns qtht_01/02, C1 owns cb_nv_tw_01, C2 owns cb_nv_tw_02, D owns cb_nv_dp_*, E owns API consumer)

### Parallel sub-tasks sau A0.3 (~6h chạy đồng thời 5 sub-agent — codex split A0.4 + A0.7)

- ⏳ **A0.4a** [Sub-agent A1] Seed nhóm 1 — Auth/Permission (CTDT DU_THAO, DN, GV, TaiKhoan mixed status)
  - **Kết quả:** TBD
  - **Cần có sẵn:** A0.3 ✅
  - **Effort:** 1h30
  - **Run parallel với:** A0.4b, A0.4c, A0.4d, A0.7

- ⏳ **A0.4b** [Sub-agent A2] Seed nhóm 2 — Workflow/Form (TVV no thẻ CHO_PHE_DUYET, CTDT NHAP, dot báo cáo TAO_DOT, KHDG, HSCT)
  - **Kết quả:** TBD
  - **Cần có sẵn:** A0.3 ✅
  - **Effort:** 2h
  - **Run parallel với:** A0.4a, A0.4c, A0.4d, A0.7

- ⏳ **A0.4c** [Sub-agent A3] Seed nhóm 3 — Cross-tenant (NHCH 2 ĐV, TCTV 2 ĐV, GV/DeXuat/DiemDanh 2 ĐV, marker record)
  - **Kết quả:** TBD
  - **Cần có sẵn:** A0.3 ✅
  - **Effort:** 2h
  - **Run parallel với:** A0.4a, A0.4b, A0.4d, A0.7

- ⏳ **A0.4d** [Sub-agent A4] Seed nhóm 4 — Heavy data + virus flag (DN >100 HoSoChiTra, file NHIEM flag)
  - **Kết quả:** TBD
  - **Cần có sẵn:** A0.3 ✅
  - **Effort:** 1h30-3h
  - **Run parallel với:** A0.4a, A0.4b, A0.4c, A0.7
  - **BLOCKED gate (codex risk #4):** Nếu DBA inject virus flag >1h không xong → mark M3 + sec idx 7 status 🚫, KHÔNG spend QA time fake state. Escalate DBA ticket riêng.

- ⏳ **A0.7** [Sub-agent A5] API consumer credential setup + MailHog OTP path + file fixtures (clean/failed/virus)
  - **Kết quả:** TBD
  - **Cần có sẵn:** A0.2 ✅
  - **Effort:** 1h30
  - **Output:** api-consumer-tokens.txt (gitignored) + fixtures/{clean.pdf, fail-trigger.docx, virus.eicar}

> **Checkpoint P0:** Sequential core ✅ + 5 sub-tasks parallel ✅ → Quality gate → Sprint 1 (parallel 6 agent B/C1/C2/D/E/F)

### Quality gate (~2h, codex risk #4 — bug-report quality)

- ⏳ **QG1.B** Agent B: 2 sample bug-report → Coordinator review 6-section + wording → pass
- ⏳ **QG1.C1** Agent C1: 2 sample bug-report → review → pass
- ⏳ **QG1.C2** Agent C2: 2 sample bug-report → review → pass
- ⏳ **QG1.D** Agent D: 2 sample bug-report (cross-tenant, 2-tab screenshot) → review → pass
- ⏳ **QG1.E** Agent E: 2 sample bug-report (curl evidence) → review → pass
- ⏳ **QG1.F** Agent F: 2 sample bug-report (race + Partial-QA) → review → pass

> **Gate:** Mọi agent phải pass QG1 trước khi full execution. Sample bug bất kỳ trong Sprint 1.

---

## Sprint 1 — HIGH critical + Top 30 Medium UI (85 bug, ~60h serial)

### Agent B — 7 bug, ~3.8h

- ⏳ **MB024** [QA-UI] Delayed login redirect fires after leaving verify page
  - **Kết quả:** TBD
  - **Verify:** Vào verify-email, ngay khi setTimeout pending thì navigate đi page khác, check không bị bounce
  - **Tool:** MCP navigate_page + timing · **Owner:** Agent B · **Module:** auth
  - **Effort:** 30p
  - **Source ref:** `packages/web/src/pages/auth/verify-email/index.tsx:22`

- ⏳ **MB028** [QA-UI] VNeID login button never starts authorization
  - **Kết quả:** TBD
  - **Verify:** Vào /login, click button VNeID, check network có redirect/POST đến VNeID authorization endpoint
  - **Tool:** MCP click + list_network_requests · **Owner:** Agent B · **Module:** auth
  - **Effort:** 20p
  - **Source ref:** `packages/web/src/pages/auth/login/index.tsx:217`

- ⏳ **H008** [QA-UI] PermissionAction disabled={false} bypass
  - **Kết quả:** TBD
  - **Verify:** Click button denied vẫn fire — check network panel
  - **Tool:** MCP evaluate_script · **Owner:** Agent B · **Module:** other
  - **Effort:** 30p

- ⏳ **H018** [QA-UI] UpdateProfile bypass cap guard
  - **Kết quả:** TBD
  - **Verify:** 🚨 PUT donViId TW từ lower-cap account
  - **Tool:** MCP click + curl · **Owner:** Agent B · **Module:** other
  - **Effort:** 1h

- ⏳ **H021** [QA-UI] Giảng viên detail edit dù read-only
  - **Kết quả:** TBD
  - **Verify:** Click tên GV → form edit hiển thị
  - **Tool:** MCP click · **Owner:** Agent B · **Module:** other
  - **Effort:** 30p

- ⏳ **H045** [QA-UI] Lưu quyền sai role sau navigate
  - **Kết quả:** TBD
  - **Verify:** 🚨 /vai-tro/A → toggle → SPA nav B → Save lưu sai role
  - **Tool:** MCP click · **Owner:** Agent B · **Module:** other
  - **Effort:** 30p

- ⏳ **MB042** [QA-UI] Bulk account actions send empty/partial id list
  - **Kết quả:** TBD
  - **Verify:** Select bulk accounts, đổi pagination/filter, click bulk action check payload không bị stale ids
  - **Tool:** MCP click + list_network_requests · **Owner:** Agent B · **Module:** qtht
  - **Effort:** 30p
  - **Source ref:** `packages/web/src/pages/quan-tri/tai-khoan/index.tsx:84`

### Agent C — 38 bug, ~16.5h

- ⏳ **MB002** [QA-UI] Changing report type re-runs with previous filters
  - **Kết quả:** TBD
  - **Verify:** Vào báo cáo, submit filter A, đổi report type, check kết quả không re-run với filter cũ
  - **Tool:** MCP click + take_snapshot · **Owner:** Agent C · **Module:** bao-cao
  - **Effort:** 20p
  - **Source ref:** `packages/web/src/pages/bao-cao/index.tsx:113`

- ⏳ **MB021** [QA-UI] Trend line reads primary aggregate rows
  - **Kết quả:** TBD
  - **Verify:** Run báo cáo có time-series, check trend line render đúng time-series data không phải aggregate
  - **Tool:** MCP evaluate_script chart data · **Owner:** Agent C · **Module:** bao-cao
  - **Effort:** 30p
  - **Source ref:** `packages/web/src/pages/bao-cao/components/charts/TrendLineChart.tsx:21`

- ⏳ **MB022** [QA-UI] Late URL initialValues never hydrate the form
  - **Kết quả:** TBD
  - **Verify:** Deep-link URL bao-cao với query params, check form filter hydrate giá trị từ URL
  - **Tool:** MCP navigate_page + take_snapshot · **Owner:** Agent C · **Module:** bao-cao
  - **Effort:** 20p
  - **Source ref:** `packages/web/src/pages/bao-cao/components/ReportFilterPanel.tsx:50`

- ⏳ **MB040** [QA-UI] Custom date range shows error but not validated
  - **Kết quả:** TBD
  - **Verify:** Chọn custom date invalid (end < start), check form không submit được
  - **Tool:** MCP fill_form + submit · **Owner:** Agent C · **Module:** bao-cao
  - **Effort:** 20p
  - **Source ref:** `packages/web/src/pages/bao-cao/components/KyBaoCaoFilter.tsx:89`

- ⏳ **MB012** [QA-UI] Clearing optional fields in edit mode not persisted
  - **Kết quả:** TBD
  - **Verify:** Edit ThuMucBieuMau, xóa giá trị optional field, save, reload check field rỗng đã persist
  - **Tool:** MCP fill + reload · **Owner:** Agent C · **Module:** bieu-mau
  - **Effort:** 20p
  - **Source ref:** `packages/web/src/pages/bieu-mau/components/ThuMucBieuMauModal.tsx:70`

- ⏳ **MB001** [QA-UI] Merging target defaults drops repeated query params
  - **Kết quả:** TBD
  - **Verify:** Tạo URL có 2 query param trùng key, navigate qua RedirectPreservingSearch, check URL đích còn giữ cả 2
  - **Tool:** MCP navigate_page + evaluate_script · **Owner:** Agent C · **Module:** common
  - **Effort:** 20p
  - **Source ref:** `packages/web/src/components/RedirectPreservingSearch/redirect-preserving-search.tsx:23`

- ⏳ **MB003** [QA-UI] Detail drawer navigation drops list filters
  - **Kết quả:** TBD
  - **Verify:** Apply filter list KCH, click row mở drawer, back ra check filter còn giữ
  - **Tool:** MCP click + evaluate_script URL · **Owner:** Agent C · **Module:** common
  - **Effort:** 20p
  - **Source ref:** `packages/web/src/pages/tv-nhanh/kho-cau-hoi/hooks/use-kch-filters.ts:22`

- ⏳ **MB005** [QA-UI] Detail drawer endless skeleton on fetch error
  - **Kết quả:** TBD
  - **Verify:** Block API detail (network throttle/wrong ID), mở drawer, check có error state thay vì skeleton mãi
  - **Tool:** MCP DevTools network block · **Owner:** Agent C · **Module:** common
  - **Effort:** 20p
  - **Source ref:** `packages/web/src/pages/tv-nhanh/kho-cau-hoi/components/KhoCauHoiDetailDrawer.tsx:41`

- ⏳ **MB007** [QA-UI] Unread count polling stops after transient error
  - **Kết quả:** TBD
  - **Verify:** Login, throttle notification API gây 500 1 lần, check polling vẫn tiếp tục sau lỗi
  - **Tool:** MCP DevTools network · **Owner:** Agent C · **Module:** common
  - **Effort:** 30p
  - **Source ref:** `packages/web/src/components/NotificationBell/use-notification-bell.ts:27`

- ⏳ **MB009** [QA-UI] Clearing column sort never notifies parent
  - **Kết quả:** TBD
  - **Verify:** Mở table có sort, click toggle clear sort, check network request không còn param sort
  - **Tool:** MCP click + list_network_requests · **Owner:** Agent C · **Module:** common
  - **Effort:** 20p
  - **Source ref:** `packages/web/src/components/ProTableWrapper/pro-table-wrapper.tsx:30`

- ⏳ **MB010** [QA-UI] Unread badge polling stops after transient error
  - **Kết quả:** TBD
  - **Verify:** Dup #7 — throttle notification gây 500, badge polling phải resume
  - **Tool:** MCP DevTools network · **Owner:** Agent C · **Module:** common
  - **Effort:** 30p
  - **Source ref:** `packages/web/src/components/NotificationBell/use-notification-bell.ts:27`

- ⏳ **MB018** [QA-UI] Chart bars show empty state during initial loading
  - **Kết quả:** TBD
  - **Verify:** Throttle dashboard API, mở dashboard, check chart hiện skeleton/loading thay vì empty
  - **Tool:** MCP DevTools network throttle · **Owner:** Agent C · **Module:** common
  - **Effort:** 20p
  - **Source ref:** `packages/web/src/pages/dashboard/components/ChartBar.tsx:50`

- ⏳ **MB019** [QA-UI] Severe SLA tag does not render black tag
  - **Kết quả:** TBD
  - **Verify:** Seed/tạo record SLA severe (overdue), check tag màu đen render đúng
  - **Tool:** MCP evaluate_script CSS color · **Owner:** Agent C · **Module:** common
  - **Effort:** 20p
  - **Source ref:** `packages/web/src/components/SlaIndicator/sla-indicator.tsx:71`

- ⏳ **MB034** [QA-UI] Clearing sort state not reported to parent
  - **Kết quả:** TBD
  - **Verify:** Dup #9 — Click clear sort, check network không còn sort param
  - **Tool:** MCP click + list_network_requests · **Owner:** Agent C · **Module:** common
  - **Effort:** 20p
  - **Source ref:** `packages/web/src/components/ProTableWrapper/pro-table-wrapper.tsx:31`

- ⏳ **MB037** [QA-UI] PDF previews marked done even when no tab opens
  - **Kết quả:** TBD
  - **Verify:** Block popup, preview PDF, check state preview không bị marked done khi tab fail
  - **Tool:** MCP click + browser popup blocker · **Owner:** Agent C · **Module:** common
  - **Effort:** 30p
  - **Source ref:** `packages/web/src/components/FileViewer/FileViewerProvider.tsx:13`

- ⏳ **MB039** [QA-UI] Page-size changes invoke onPaginationChange twice
  - **Kết quả:** TBD
  - **Verify:** Mở table, đổi page size, check chỉ 1 API call (không phải 2)
  - **Tool:** MCP click + list_network_requests count · **Owner:** Agent C · **Module:** common
  - **Effort:** 20p
  - **Source ref:** `packages/web/src/components/proto/ProtoTable.tsx:31`

- ⏳ **MB047** [QA-UI] Malformed date props lock browser in infinite loop
  - **Kết quả:** TBD
  - **Verify:** Tạo SLA record với malformed date, mở page check browser không freeze (timeout 10s)
  - **Tool:** MCP performance trace + wait · **Owner:** Agent C · **Module:** common
  - **Effort:** 30p
  - **Source ref:** `packages/web/src/components/SlaIndicator/sla-indicator.tsx:20`

- ⏳ **MB031** [QA-UI] Detail route captures DeXuat list URL as id
  - **Kết quả:** TBD
  - **Verify:** Navigate /dao-tao/de-xuat (list URL), check không bị match route detail :id
  - **Tool:** MCP navigate_page + URL check · **Owner:** Agent C · **Module:** dao-tao
  - **Effort:** 15p
  - **Source ref:** `packages/web/src/pages/dao-tao/index.tsx:117`

- ⏳ **MB025** [QA-UI] Legacy edit alias redirects to wrong doanh-nghiep id
  - **Kết quả:** TBD
  - **Verify:** Navigate /doanh-nghiep/:id/edit legacy alias, check redirect đến đúng id chứ không phải sai id
  - **Tool:** MCP navigate_page + URL check · **Owner:** Agent C · **Module:** doanh-nghiep
  - **Effort:** 20p
  - **Source ref:** `packages/web/src/pages/doanh-nghiep/index.tsx:41`

- ⏳ **MB011** [QA-UI] Batch delete treats cancelled Hỏi đáp as eligible
  - **Kết quả:** TBD
  - **Verify:** Filter hoi-dap cancelled, select all, check batch delete button bị disable hoặc reject
  - **Tool:** MCP click + take_snapshot · **Owner:** Agent C · **Module:** hoi-dap
  - **Effort:** 20p
  - **Source ref:** `packages/web/src/pages/hoi-dap/list/columns.tsx:52`

- ⏳ **MB029** [QA-UI] Export drops selected complexity filter
  - **Kết quả:** TBD
  - **Verify:** Filter hoi-dap by complexity, click Export, check request export có param complexity
  - **Tool:** MCP click + list_network_requests · **Owner:** Agent C · **Module:** hoi-dap
  - **Effort:** 15p
  - **Source ref:** `packages/web/src/pages/hoi-dap/list/components/HoiDapFilterBar.tsx:46`

- ⏳ **H007** [QA-UI] Default admin Secret@123
  - **Kết quả:** TBD
  - **Verify:** 🚨 Login admin/Secret@123 — nếu PASS = root compromise
  - **Tool:** MCP click · **Owner:** Agent C · **Module:** other
  - **Effort:** 15p

- ⏳ **H020** [QA-UI] Route /:id render edit khi chỉ Read
  - **Kết quả:** TBD
  - **Verify:** Mở /ct-htpldn/{id} DU_THAO, nút Lưu hiện
  - **Tool:** MCP click + evaluate · **Owner:** Agent C · **Module:** other
  - **Effort:** 30p

- ⏳ **H037** [QA-UI] Hoàn tất chấm điểm mất edit
  - **Kết quả:** TBD
  - **Verify:** 🚨 Đổi điểm KHÔNG Lưu → Hoàn tất → input mất
  - **Tool:** MCP click + evaluate · **Owner:** Agent C · **Module:** other
  - **Effort:** 30p

- ⏳ **H039** [QA-UI] Form CT-HTPLDN giữ value cũ
  - **Kết quả:** TBD
  - **Verify:** Detail A → SPA route B → Lưu, value của A persist
  - **Tool:** MCP click · **Owner:** Agent C · **Module:** other
  - **Effort:** 30p

- ⏳ **H043** [QA-UI] submitResult ghi đè override điểm
  - **Kết quả:** TBD
  - **Verify:** Set override điểm → submit → check override discard
  - **Tool:** MCP click + evaluate · **Owner:** Agent C · **Module:** other
  - **Effort:** 1h30

- ⏳ **H054** [QA-UI] FE thiếu nút start dot bao cao
  - **Kết quả:** TBD
  - **Verify:** Tạo dot BC → check nút Start hiện
  - **Tool:** MCP click · **Owner:** Agent C · **Module:** other
  - **Effort:** 15p

- ⏳ **H055** [QA-UI] Edit-mode fail fallback create
  - **Kết quả:** TBD
  - **Verify:** Mock getById fail → check POST thay vì show error
  - **Tool:** MCP click + evaluate · **Owner:** Agent C · **Module:** other
  - **Effort:** 1h

- ⏳ **H058** [QA-UI] TVV tạo thiếu thẻ hành nghề
  - **Kết quả:** TBD
  - **Verify:** Mock upload thẻ fail → vẫn tạo TVV
  - **Tool:** MCP click + list_network · **Owner:** Agent C · **Module:** other
  - **Effort:** 1h

- ⏳ **H074** [QA-UI] AntD notif thiếu message field
  - **Kết quả:** TBD
  - **Verify:** 🚨 Cấu hình SLA → Lưu, toast field sai
  - **Tool:** MCP click · **Owner:** Agent C · **Module:** other
  - **Effort:** 15p

- ⏳ **H085** [QA-UI] Duyệt TVV thiếu gate file thẻ
  - **Kết quả:** TBD
  - **Verify:** 🚨 TVV không file thẻ → duyệt PASS sai
  - **Tool:** MCP click · **Owner:** Agent C · **Module:** other
  - **Effort:** 30p

- ⏳ **H087** [QA-UI] API consumer thiếu scope inbound
  - **Kết quả:** TBD
  - **Verify:** Form API consumer scope list missing
  - **Tool:** MCP click · **Owner:** Agent C · **Module:** other
  - **Effort:** 15p

- ⏳ **MB016** [QA-UI] Toggle/delete mutations leave detail queries stale
  - **Kết quả:** TBD
  - **Verify:** Mở danh-muc detail, toggle status, navigate ra rồi vào lại check status mới (cache invalidate)
  - **Tool:** MCP click + reload · **Owner:** Agent C · **Module:** qtht
  - **Effort:** 30p
  - **Source ref:** `packages/web/src/services/danh-muc/danh-muc.service.ts:69`

- ⏳ **MB013** [QA-UI] Whitespace approval/rejection fields pass validation
  - **Kết quả:** TBD
  - **Verify:** Mở modal phê duyệt hàng loạt, nhập 3 dấu cách vào reason, submit check validation reject
  - **Tool:** MCP fill_form + take_snapshot · **Owner:** Agent C · **Module:** tu-van
  - **Effort:** 15p
  - **Source ref:** `packages/web/src/pages/chuyen-gia-tvv/danh-sach/ModalPheDuyetHangLoat.tsx:56`

- ⏳ **MB043** [QA-UI] Lưu nháp and Gửi KQ submit same request
  - **Kết quả:** TBD
  - **Verify:** Click Lưu nháp vs Gửi KQ, so sánh payload + endpoint khác nhau
  - **Tool:** MCP click + list_network_requests diff · **Owner:** Agent C · **Module:** tu-van
  - **Effort:** 20p
  - **Source ref:** `packages/web/src/pages/chuyen-gia-tvv/chi-tiet/TabThamDinh.tsx:62`

- ⏳ **MB048** [QA-UI] Search panel filters not fully applied to list/export
  - **Kết quả:** TBD
  - **Verify:** Apply filter TVV, click Tìm rồi click Export, check 2 request đều có cùng filter param
  - **Tool:** MCP click + list_network_requests · **Owner:** Agent C · **Module:** tu-van
  - **Effort:** 30p
  - **Source ref:** `packages/web/src/pages/chuyen-gia-tvv/danh-sach/TuVanVienSearchPanel.tsx:34`

- ⏳ **MB015** [QA-UI] Detail-page delete button rendered but inert
  - **Kết quả:** TBD
  - **Verify:** Vào vu-viec detail, click nút Xóa, check có gọi API delete hoặc confirm modal
  - **Tool:** MCP click + list_network_requests · **Owner:** Agent C · **Module:** vu-viec
  - **Effort:** 15p
  - **Source ref:** `packages/web/src/pages/vu-viec/detail/index.tsx:222`

- ⏳ **MB020** [QA-UI] Filtered timeline empty state before all events loaded
  - **Kết quả:** TBD
  - **Verify:** Mở vu-viec detail có nhiều event, apply filter, throttle network check không hiện empty sớm
  - **Tool:** MCP click + DevTools network · **Owner:** Agent C · **Module:** vu-viec
  - **Effort:** 30p
  - **Source ref:** `packages/web/src/pages/vu-viec/detail/components/SectionTimeline.tsx:139`

### Agent D — 7 bug, ~9.5h

- ⏳ **H004** [QA-cross-role] BaiGiang/DeKiemTra list cross-tenant
  - **Kết quả:** TBD
  - **Verify:** GET /bai-giangs cross tenant, đếm row tenant khác
  - **Tool:** curl + API GET · **Owner:** Agent D · **Module:** other
  - **Effort:** 1h-2h+

- ⏳ **H016** [QA-cross-role] Phan-cong list bypass tenant
  - **Kết quả:** TBD
  - **Verify:** GET /phan-cong-danh-gia keHoachId cross
  - **Tool:** curl · **Owner:** Agent D · **Module:** other
  - **Effort:** 1h

- ⏳ **H019** [QA-cross-role] Export NHCH leak cross-tenant
  - **Kết quả:** TBD
  - **Verify:** Export Excel đếm row đơn vị khác
  - **Tool:** MCP + curl · **Owner:** Agent D · **Module:** other
  - **Effort:** 1h30-2h

- ⏳ **H029** [QA-cross-role] TCTV list/export bypass tenant filter
  - **Kết quả:** TBD
  - **Verify:** 🚨 List TCTV không truyền donViId
  - **Tool:** MCP + curl · **Owner:** Agent D · **Module:** other
  - **Effort:** 1h

- ⏳ **H031** [QA-cross-role] Đào tạo list/export bypass RLS
  - **Kết quả:** TBD
  - **Verify:** List GiangVien/DeXuat/DiemDanh cross
  - **Tool:** MCP + curl · **Owner:** Agent D · **Module:** other
  - **Effort:** 2h+

- ⏳ **H035** [QA-cross-role] goi-y ghi đè TuVanNhanh khác donVi
  - **Kết quả:** TBD
  - **Verify:** GET /tu-van-nhanhs/{B-id}/goi-y từ A
  - **Tool:** curl · **Owner:** Agent D · **Module:** other
  - **Effort:** 30p

- ⏳ **H062** [QA-cross-role] maChuongTrinh collision tenant
  - **Kết quả:** TBD
  - **Verify:** 2 đơn vị tạo CT cùng ngày, mã trùng
  - **Tool:** curl parallel · **Owner:** Agent D · **Module:** other
  - **Effort:** 1h

### Agent E — 26 bug, ~16.2h

- ⏳ **H001** [QA-API] TVV đọc lịch sử VV khác
  - **Kết quả:** TBD
  - **Verify:** GET /vu-viecs/:id/lich-su id không gán cho tvv
  - **Tool:** curl · **Owner:** Agent E · **Module:** other
  - **Effort:** 30p

- ⏳ **H006** [QA-API] Client assertion exp missing
  - **Kết quả:** TBD
  - **Verify:** Sign JWT không exp claim, POST /token
  - **Tool:** curl · **Owner:** Agent E · **Module:** other
  - **Effort:** 1h

- ⏳ **H010** [QA-API] File mutation sau DA_THANH_TOAN
  - **Kết quả:** TBD
  - **Verify:** POST attach file vào HSCT đã đóng thanh toán
  - **Tool:** curl · **Owner:** Agent E · **Module:** other
  - **Effort:** 30p

- ⏳ **H011** [QA-API] X-Forwarded-For spoof IP whitelist
  - **Kết quả:** TBD
  - **Verify:** curl header X-Forwarded-For spoof IP whitelist
  - **Tool:** curl · **Owner:** Agent E · **Module:** other
  - **Effort:** 30p

- ⏳ **H012** [QA-API] String 'false' qua @Equals(true)
  - **Kết quả:** TBD
  - **Verify:** POST dongYDieuKhoan:'false' (string) thay vì false
  - **Tool:** curl · **Owner:** Agent E · **Module:** other
  - **Effort:** 15p

- ⏳ **H013** [QA-API] Download file thiếu check BieuMau
  - **Kết quả:** TBD
  - **Verify:** GET /bieu-maus/files/{otherFid}/download cross
  - **Tool:** curl · **Owner:** Agent E · **Module:** other
  - **Effort:** 30p

- ⏳ **H022** [QA-API] Captcha hard-coded mock-captcha
  - **Kết quả:** TBD
  - **Verify:** 🚨 POST đăng ký body có captchaToken:'mock-captcha'
  - **Tool:** MCP list_network · **Owner:** Agent E · **Module:** other
  - **Effort:** 15p

- ⏳ **H026** [QA-API] Create PQDL bypass same-cap
  - **Kết quả:** TBD
  - **Verify:** POST 2 lần cùng vaiTroId, 2 DP khác
  - **Tool:** curl · **Owner:** Agent E · **Module:** other
  - **Effort:** 1h

- ⏳ **H028** [QA-API] System role bị edit/toggle qua PATCH
  - **Kết quả:** TBD
  - **Verify:** 🚨 PATCH /vai-tro/{systemId} với role có update_vai_tro
  - **Tool:** curl · **Owner:** Agent E · **Module:** other
  - **Effort:** 30p

- ⏳ **H030** [QA-API] TVV file delete bypass CB_NV policy
  - **Kết quả:** TBD
  - **Verify:** DELETE /tu-van-viens/:id/files/:fid role non-CBNV
  - **Tool:** curl · **Owner:** Agent E · **Module:** other
  - **Effort:** 30p

- ⏳ **H032** [QA-API] TuLieuPhapLyVv link parent cross-tenant
  - **Kết quả:** TBD
  - **Verify:** POST với noiDungTvId tenant B
  - **Tool:** curl · **Owner:** Agent E · **Module:** other
  - **Effort:** 30p

- ⏳ **H034** [QA-API] fileDinhKemIds re-parent file người khác
  - **Kết quả:** TBD
  - **Verify:** PATCH HoiDap A với fileId của B
  - **Tool:** curl · **Owner:** Agent E · **Module:** other
  - **Effort:** 30p

- ⏳ **H036** [QA-API] Tổng hợp BC lan sibling dot
  - **Kết quả:** TBD
  - **Verify:** Tạo 2 dot DA_GUI_TW cùng ct
  - **Tool:** curl + API GET · **Owner:** Agent E · **Module:** other
  - **Effort:** 2h+

- ⏳ **H040** [QA-API] trongSo 'abc' lưu được
  - **Kết quả:** TBD
  - **Verify:** POST DM trongSo:'abc' (string thay vì number)
  - **Tool:** curl · **Owner:** Agent E · **Module:** other
  - **Effort:** 15p

- ⏳ **H047** [QA-API] Batch upsert tiêu chí xóa nhầm
  - **Kết quả:** TBD
  - **Verify:** PUT tieu-chi với id giả → xóa nhầm record khác
  - **Tool:** curl · **Owner:** Agent E · **Module:** other
  - **Effort:** 30p

- ⏳ **H049** [QA-API] congKhai publish trước validate
  - **Kết quả:** TBD
  - **Verify:** File attach lỗi → publish vẫn pass
  - **Tool:** curl + MCP · **Owner:** Agent E · **Module:** other
  - **Effort:** 1h

- ⏳ **H052** [QA-API] Batch duyệt bypass BR-CALC-01
  - **Kết quả:** TBD
  - **Verify:** 🚨 batchPheDuyet mismatch NHO+90% gây sai tiền chi trả
  - **Tool:** curl · **Owner:** Agent E · **Module:** other
  - **Effort:** 30p

- ⏳ **H053** [QA-API] File VV duongDanFile = ID sai
  - **Kết quả:** TBD
  - **Verify:** Upload → GET hồ sơ → download 404
  - **Tool:** curl · **Owner:** Agent E · **Module:** other
  - **Effort:** 30p

- ⏳ **H059** [QA-API] Public TVV list/search rỗng
  - **Kết quả:** TBD
  - **Verify:** 🚨 GET /public/tu-van-vien empty list
  - **Tool:** curl · **Owner:** Agent E · **Module:** other
  - **Effort:** 15p

- ⏳ **H060** [QA-API] batchCongKhai publish chưa duyệt
  - **Kết quả:** TBD
  - **Verify:** hoi-dap chưa DA_DUYET → batch publish pass
  - **Tool:** curl · **Owner:** Agent E · **Module:** other
  - **Effort:** 30p

- ⏳ **H063** [QA-API] Overbook khóa học
  - **Kết quả:** TBD
  - **Verify:** 🚨 curl 2 POST inbound song song khóa soLuongToiDa=1
  - **Tool:** curl parallel xargs -P · **Owner:** Agent E · **Module:** other
  - **Effort:** 1h-2h+

- ⏳ **H066** [QA-API] Optimistic lock DanhMuc
  - **Kết quả:** TBD
  - **Verify:** 🚨 2 PATCH version=1 song song
  - **Tool:** curl parallel · **Owner:** Agent E · **Module:** other
  - **Effort:** 30p

- ⏳ **H067** [QA-API] Optimistic lock VaiTro
  - **Kết quả:** TBD
  - **Verify:** 🚨 2 PATCH /vai-tro version=1
  - **Tool:** curl parallel · **Owner:** Agent E · **Module:** other
  - **Effort:** 30p

- ⏳ **H068** [QA-API] Optimistic lock DonVi
  - **Kết quả:** TBD
  - **Verify:** 2 PATCH /don-vi version=1
  - **Tool:** curl parallel · **Owner:** Agent E · **Module:** other
  - **Effort:** 30p

- ⏳ **H069** [QA-API] Optimistic lock HopDongTV
  - **Kết quả:** TBD
  - **Verify:** 2 PATCH /hop-dong-tu-vans
  - **Tool:** curl parallel · **Owner:** Agent E · **Module:** other
  - **Effort:** 30p

- ⏳ **H086** [QA-API] Lưu nháp CTDT gọi PUT sai
  - **Kết quả:** TBD
  - **Verify:** 🚨 CTDT nháp → Lưu → 405/404 method
  - **Tool:** MCP list_network · **Owner:** Agent E · **Module:** other
  - **Effort:** 15p

### Agent F — 7 bug, ~13.5h

- ⏳ **H002** [Partial-QA] Attach file cross-tenant qua DVC
  - **Kết quả:** TBD
  - **Verify:** POST intake fileDinhKemIds tenant khác (cần DVC token + seed file)
  - **Tool:** curl · **Owner:** Agent F · **Module:** other
  - **Effort:** 1h30-2h+

- ⏳ **H009** [Partial-QA] Pending account hết hạn vẫn active
  - **Kết quả:** TBD
  - **Verify:** Cần DBA seed ngayTao cũ rồi thử login active
  - **Tool:** curl + DBA seed · **Owner:** Agent F · **Module:** other
  - **Effort:** 2h+

- ⏳ **H023** [Partial-QA] Cache report ignore allowedDonViIds
  - **Kết quả:** TBD
  - **Verify:** Seed PQDL qua admin UI, tránh cache cũ bằng unique filter
  - **Tool:** curl + MCP · **Owner:** Agent F · **Module:** other
  - **Effort:** 2h+

- ⏳ **H024** [Partial-QA] Cache report scope leak HoiDap/CT
  - **Kết quả:** TBD
  - **Verify:** Tương tự #23, unique filter mỗi run
  - **Tool:** curl + MCP · **Owner:** Agent F · **Module:** other
  - **Effort:** 2h+

- ⏳ **H038** [QA-API best-effort] Race delete HĐ-TV vs link VV
  - **Kết quả:** TBD
  - **Verify:** curl 2 thread DELETE + POST link, repeat 20-50 lần
  - **Tool:** curl parallel + retry · **Owner:** Agent F · **Module:** other
  - **Effort:** 2h+

- ⏳ **H065** [QA-API best-effort] Mã HoiDap trùng cross-tenant
  - **Kết quả:** TBD
  - **Verify:** curl POST hoi-dap 2 tenant cùng ngày retry 20+
  - **Tool:** curl parallel · **Owner:** Agent F · **Module:** other
  - **Effort:** 1h30+

- ⏳ **H070** [QA-API best-effort] Payment validate state stale
  - **Kết quả:** TBD
  - **Verify:** curl PATCH cùng version repeat — không cần load infra
  - **Tool:** curl parallel/retry · **Owner:** Agent F · **Module:** other
  - **Effort:** 2h+

---

## Sprint 2 — Medium QA-UI bulk + Medium QA-API short (154 bug, ~65h serial)

### Agent B — 24 bug, ~11.2h

- ⏳ **MB050** [QA-UI] Missing callback params leave VNeID page spinning
  - **Kết quả:** TBD
  - **Verify:** Navigate /auth/vneid/callback không có code/state, check hiện error thay vì spinner mãi
  - **Tool:** MCP navigate_page + wait · **Owner:** Agent B · **Module:** auth
  - **Effort:** 20p
  - **Source ref:** `packages/web/src/pages/auth/vneid/callback/index.tsx:17`

- ⏳ **MB056** [QA-UI] Invalid first-login tokens trigger global logout
  - **Kết quả:** TBD
  - **Verify:** Vào /first-login-password với token invalid, check hiện local error không bị global logout redirect
  - **Tool:** MCP navigate_page + URL check · **Owner:** Agent B · **Module:** auth
  - **Effort:** 20p
  - **Source ref:** `packages/web/src/pages/auth/first-login-password/index.tsx:37`

- ⏳ **MB062** [QA-UI] VNeID callback spins forever when code/state missing
  - **Kết quả:** TBD
  - **Verify:** Dup #50 — navigate callback no code/state, check error UI
  - **Tool:** MCP navigate_page · **Owner:** Agent B · **Module:** auth
  - **Effort:** 20p
  - **Source ref:** `packages/web/src/pages/auth/vneid/callback/index.tsx:17`

- ⏳ **MB077** [QA-UI] Public first-login password fail triggers global logout
  - **Kết quả:** TBD
  - **Verify:** Dup pattern #56 — first-login password fail, check không bị global logout redirect
  - **Tool:** MCP navigate + URL check · **Owner:** Agent B · **Module:** auth
  - **Effort:** 20p
  - **Source ref:** `packages/web/src/pages/auth/login/index.tsx:135`

- ⏳ **MC009** [QA-UI] OTP auto-submit paths send concurrent verification while pending
  - **Kết quả:** TBD
  - **Verify:** MCP UI: 2 tab nhập OTP 6 ký tự cuối gần đồng thời, check network có 2 POST verify-otp
  - **Tool:** MCP · **Owner:** Agent B · **Module:** auth
  - **Effort:** 45p
  - **Source ref:** `packages/web/src/pages/auth/login/index.tsx:221`

- ⏳ **MC035** [QA-UI] Transition dialogs submit outside single-pending guard
  - **Kết quả:** TBD
  - **Verify:** MCP UI: double-click approve button nhanh, check network có 2 POST approve cùng entityId
  - **Tool:** MCP · **Owner:** Agent B · **Module:** common
  - **Effort:** 30p
  - **Source ref:** `packages/web/src/components/ApprovalActions/approval-actions.tsx:43`

- ⏳ **MS031** [QA-UI] Denied actions stay enabled when child passes disabled=false
  - **Kết quả:** TBD
  - **Verify:** Test PermissionAction với child Button disabled={false} + role denied, verify button vẫn click được
  - **Tool:** MCP click + evaluate_script · **Owner:** Agent B · **Module:** common
  - **Effort:** 20 phút
  - **Source ref:** `packages/web/src/components/PermissionAction/permission-action.tsx:48`

- ⏳ **MD002** [QA-UI] Unsaved-change guard bypassed by SPA navigation
  - **Kết quả:** TBD
  - **Verify:** Edit form CT-HTPLDN detail không save, MCP click sidebar link khác, verify dialog confirm bypass và data lost
  - **Tool:** MCP click · **Owner:** Agent B · **Module:** ct-htpldn
  - **Effort:** S
  - **Source ref:** `packages/web/src/pages/ct-htpldn/detail/index.tsx:113`

- ⏳ **MS019** [QA-UI] Draft action bar ignores update submit cancel permissions
  - **Kết quả:** TBD
  - **Verify:** Login role read CTDT, mở draft detail, verify action bar Update/Submit/Cancel có disabled theo CASL không
  - **Tool:** MCP click + take_snapshot · **Owner:** Agent B · **Module:** ct-htpldn
  - **Effort:** 20 phút
  - **Source ref:** `packages/web/src/pages/dao-tao/chuong-trinh/detail/index.tsx:146`

- ⏳ **MS036** [QA-UI] Read-only detail route renders and submits edit form
  - **Kết quả:** TBD
  - **Verify:** Login role read CT-HTPLDN, mở detail, verify form edit có render và submit button có disabled không
  - **Tool:** MCP click + take_snapshot · **Owner:** Agent B · **Module:** ct-htpldn
  - **Effort:** 20 phút
  - **Source ref:** `packages/web/src/pages/ct-htpldn/index.tsx:79`

- ⏳ **MS003** [QA-UI] Read-only users reach mutation controls detail route
  - **Kết quả:** TBD
  - **Verify:** Login role read-only danh-gia, navigate detail route, verify mutation buttons disabled hay vẫn click được
  - **Tool:** MCP click + take_snapshot · **Owner:** Agent B · **Module:** danh-gia
  - **Effort:** 20 phút
  - **Source ref:** `packages/web/src/pages/danh-gia/index.tsx:35`

- ⏳ **MS022** [QA-UI] Batch delete exposed without CASL delete permission
  - **Kết quả:** TBD
  - **Verify:** Login role không có delete kế hoạch, verify batch delete button trên list page có hiển thị/clickable
  - **Tool:** MCP click + take_snapshot · **Owner:** Agent B · **Module:** danh-gia
  - **Effort:** 20 phút
  - **Source ref:** `packages/web/src/pages/danh-gia/ke-hoach/list/index.tsx:111`

- ⏳ **MS023** [QA-UI] Attachment uploads ignore CASL update permission
  - **Kết quả:** TBD
  - **Verify:** Login role read kế hoạch, mở detail, verify attachment upload UI bị disabled theo CASL update check
  - **Tool:** MCP click + take_snapshot · **Owner:** Agent B · **Module:** danh-gia
  - **Effort:** 20 phút
  - **Source ref:** `packages/web/src/pages/danh-gia/ke-hoach/detail/index.tsx:107`

- ⏳ **MS029** [QA-UI] DeXuat tab protected by ChuongTrinh instead of DeXuat permission
  - **Kết quả:** TBD
  - **Verify:** Login role có ChuongTrinh nhưng không có DeXuat, verify tab DeXuat vẫn hiện do dùng sai permission predicate
  - **Tool:** MCP click + take_snapshot · **Owner:** Agent B · **Module:** dao-tao
  - **Effort:** 20 phút
  - **Source ref:** `packages/web/src/pages/dao-tao/index.tsx:38`

- ⏳ **MS024** [QA-UI] Read-only doanh nghiệp route exposes write controls
  - **Kết quả:** TBD
  - **Verify:** Login role read-only DN, verify trên list/detail có button Create/Edit/Delete hiển thị/clickable không
  - **Tool:** MCP click + take_snapshot · **Owner:** Agent B · **Module:** doanh-nghiep
  - **Effort:** 20 phút
  - **Source ref:** `packages/web/src/pages/doanh-nghiep/index.tsx:77`

- ⏳ **MS037** [QA-UI] Read-only route renders edit-only doanh nghiệp form
  - **Kết quả:** TBD
  - **Verify:** Login role read DN, navigate edit route, verify form render và submit có bị disabled theo CASL không
  - **Tool:** MCP click + take_snapshot · **Owner:** Agent B · **Module:** doanh-nghiep
  - **Effort:** 20 phút
  - **Source ref:** `packages/web/src/pages/doanh-nghiep/index.tsx:65`

- ⏳ **MB123** [QA-UI] Admin session management panel unreachable from account detail
  - **Kết quả:** TBD
  - **Verify:** Admin login, vào /quan-tri/tai-khoan/:id, check tab/section Sessions hiển thị
  - **Tool:** MCP click + take_snapshot · **Owner:** Agent B · **Module:** qtht
  - **Effort:** 20p
  - **Source ref:** `packages/web/src/pages/quan-tri/tai-khoan/[id]/components/SessionsPanel.tsx:22`

- ⏳ **MS035** [QA-UI] Edit and delete actions gated by create permission
  - **Kết quả:** TBD
  - **Verify:** Login role có create ngày lễ nhưng không update/delete, verify Edit/Delete buttons có hiển thị/clickable
  - **Tool:** MCP click + take_snapshot · **Owner:** Agent B · **Module:** qtht
  - **Effort:** 20 phút
  - **Source ref:** `packages/web/src/pages/quan-tri/ngay-le/index.tsx:31`

- ⏳ **MS013** [QA-UI] Approval entrypoints enforce different permission predicates
  - **Kết quả:** TBD
  - **Verify:** Test các approval button trên detail page, verify mỗi entrypoint dùng cùng CASL ability check không bị inconsistent
  - **Tool:** MCP click multiple buttons · **Owner:** Agent B · **Module:** tu-van
  - **Effort:** 30 phút
  - **Source ref:** `packages/web/src/pages/chuyen-gia-tvv/to-chuc/detail.tsx:134`

- ⏳ **MS016** [QA-UI] Delete publish batch bypass CASL UI gating
  - **Kết quả:** TBD
  - **Verify:** Login role không có delete permission, verify batch action bar Delete/Publish có hiển thị/clickable không
  - **Tool:** MCP click + take_snapshot · **Owner:** Agent B · **Module:** tu-van
  - **Effort:** 20 phút
  - **Source ref:** `packages/web/src/pages/chuyen-gia-tvv/danh-sach/TuVanVienTable.tsx:48`

- ⏳ **MS025** [QA-UI] Batch publish exposed without publish permission check
  - **Kết quả:** TBD
  - **Verify:** Login role không có publish TVV, verify batch publish button hiển thị/clickable trên danh sách
  - **Tool:** MCP click + take_snapshot · **Owner:** Agent B · **Module:** tu-van
  - **Effort:** 20 phút
  - **Source ref:** `packages/web/src/pages/chuyen-gia-tvv/danh-sach/index.tsx:17`

- ⏳ **MS046** [QA-UI] Publish and delete mutations exposed without CASL gates
  - **Kết quả:** TBD
  - **Verify:** Login role không có publish/delete TVV, verify row action publish/delete có hiển thị/clickable trong table
  - **Tool:** MCP click + take_snapshot · **Owner:** Agent B · **Module:** tu-van
  - **Effort:** 20 phút
  - **Source ref:** `packages/web/src/pages/chuyen-gia-tvv/danh-sach/TuVanVienTable.tsx:65`

- ⏳ **MB089** [QA-UI] Bulk delete bypasses same state guard as row delete
  - **Kết quả:** TBD
  - **Verify:** Select vu-viec có state không cho phép xóa, click bulk delete check bị reject (giống row delete)
  - **Tool:** MCP click + take_snapshot · **Owner:** Agent B · **Module:** vu-viec
  - **Effort:** 20p
  - **Source ref:** `packages/web/src/pages/vu-viec/list/columns.tsx:34`

- ⏳ **MS034** [QA-UI] DN self-submit permission opens staff-only manual intake
  - **Kết quả:** TBD
  - **Verify:** Login role DN có self-submit, verify route manual intake (staff-only) có accessible thông qua permission misuse
  - **Tool:** MCP click + navigate · **Owner:** Agent B · **Module:** vu-viec
  - **Effort:** 25 phút
  - **Source ref:** `packages/web/src/pages/vu-viec/index.tsx:38`

### Agent C — 79 bug, ~33.2h

- ⏳ **MB051** [QA-UI] Report header omits creator falls back to unit IDs
  - **Kết quả:** TBD
  - **Verify:** Run báo cáo, check header có tên người tạo + tên đơn vị (không phải UUID raw)
  - **Tool:** MCP evaluate_script DOM text · **Owner:** Agent C · **Module:** bao-cao
  - **Effort:** 20p
  - **Source ref:** `packages/web/src/pages/bao-cao/components/ReportHeader.tsx:5`

- ⏳ **MB057** [QA-UI] Secondary trend lines read primary breakdown rows
  - **Kết quả:** TBD
  - **Verify:** Dup pattern #21 — verify secondary trend lines đọc đúng data series
  - **Tool:** MCP evaluate_script chart data · **Owner:** Agent C · **Module:** bao-cao
  - **Effort:** 30p
  - **Source ref:** `packages/web/src/pages/bao-cao/components/ReportChartRenderer.tsx:53`

- ⏳ **MB096** [QA-UI] Export use form values not matching displayed report
  - **Kết quả:** TBD
  - **Verify:** Run report với filter A, đổi form filter B (chưa submit), click Export check export dùng filter A (đã submit)
  - **Tool:** MCP click + list_network_requests · **Owner:** Agent C · **Module:** bao-cao
  - **Effort:** 30p
  - **Source ref:** `packages/web/src/pages/bao-cao/components/ReportFilterPanel.tsx:70`

- ⏳ **MB097** [QA-UI] Changing report type keeps previous filters/result
  - **Kết quả:** TBD
  - **Verify:** Dup #2 — đổi report type, check filter/result reset
  - **Tool:** MCP click + take_snapshot · **Owner:** Agent C · **Module:** bao-cao
  - **Effort:** 20p
  - **Source ref:** `packages/web/src/pages/bao-cao/index.tsx:83`

- ⏳ **MB105** [QA-UI] Deep-linked URL filters missed by form after catalog load
  - **Kết quả:** TBD
  - **Verify:** Dup #22 — deep-link URL, check form hydrate sau catalog load
  - **Tool:** MCP navigate + wait + snapshot · **Owner:** Agent C · **Module:** bao-cao
  - **Effort:** 20p
  - **Source ref:** `packages/web/src/pages/bao-cao/index.tsx:70`

- ⏳ **MB124** [QA-UI] Header omits required creator when nguoiTao not supplied
  - **Kết quả:** TBD
  - **Verify:** Dup #51 — run report check header có creator
  - **Tool:** MCP evaluate_script DOM · **Owner:** Agent C · **Module:** bao-cao
  - **Effort:** 20p
  - **Source ref:** `packages/web/src/pages/bao-cao/components/ReportHeader.tsx:5`

- ⏳ **MB134** [QA-UI] Chart auto-detection drops valid report series
  - **Kết quả:** TBD
  - **Verify:** Run report với multiple payload shapes (nested/flat), check chart auto-detect render đúng
  - **Tool:** MCP evaluate_script + diff · **Owner:** Agent C · **Module:** bao-cao
  - **Effort:** 30p
  - **Source ref:** `packages/web/src/pages/bao-cao/components/charts/TrendLineChart.tsx:21`

- ⏳ **MB135** [QA-UI] Radar scale ignores maximum score
  - **Kết quả:** TBD
  - **Verify:** Run radar chart với score max=10, check axis scale [0, 10] không phải auto
  - **Tool:** MCP evaluate_script chart scale · **Owner:** Agent C · **Module:** bao-cao
  - **Effort:** 20p
  - **Source ref:** `packages/web/src/pages/bao-cao/components/charts/RadarChartView.tsx:35`

- ⏳ **MB141** [QA-UI] Malformed row arrays crash SimpleBarChart
  - **Kết quả:** TBD
  - **Verify:** Mock API trả về malformed row array, check chart render empty state (không crash)
  - **Tool:** MCP DevTools network override · **Owner:** Agent C · **Module:** bao-cao
  - **Effort:** 30p
  - **Source ref:** `packages/web/src/pages/bao-cao/components/charts/SimpleBarChart.tsx:29`

- ⏳ **MB150** [QA-UI] Report header never receives required creator/unit label
  - **Kết quả:** TBD
  - **Verify:** Dup #51 #124 — run report check creator + unit label rendered
  - **Tool:** MCP evaluate_script DOM · **Owner:** Agent C · **Module:** bao-cao
  - **Effort:** 20p
  - **Source ref:** `packages/web/src/pages/bao-cao/components/ReportHeader.tsx:5`

- ⏳ **MB155** [QA-UI] Time-series report renders rows with zero columns
  - **Kết quả:** TBD
  - **Verify:** Run time-series vụ việc report, check rows có >=1 column (không bị zero col)
  - **Tool:** MCP evaluate_script DOM table · **Owner:** Agent C · **Module:** bao-cao
  - **Effort:** 20p
  - **Source ref:** `packages/web/src/pages/bao-cao/components/ReportResultView.tsx:90`

- ⏳ **MB106** [QA-UI] Edit modal submit create before edit detail loads
  - **Kết quả:** TBD
  - **Verify:** Click edit, ngay lập tức submit trước khi detail load xong, check không gửi create
  - **Tool:** MCP click + DevTools network throttle · **Owner:** Agent C · **Module:** bieu-mau
  - **Effort:** 30p
  - **Source ref:** `packages/web/src/pages/bieu-mau/ThuMucBieuMauPage.tsx:93`

- ⏳ **MB129** [QA-UI] Create/update errors handled twice
  - **Kết quả:** TBD
  - **Verify:** Trigger create error, check chỉ 1 toast lỗi (không phải 2)
  - **Tool:** MCP click + DOM toast · **Owner:** Agent C · **Module:** bieu-mau
  - **Effort:** 20p
  - **Source ref:** `packages/web/src/services/thu-muc-bieu-mau/thu-muc-bieu-mau.service.ts:188`

- ⏳ **MB130** [QA-UI] Turning public mode off doesn't clear public description
  - **Kết quả:** TBD
  - **Verify:** Bật public mode, nhập public description, off public mode, save, reload check description đã clear
  - **Tool:** MCP click + reload · **Owner:** Agent C · **Module:** bieu-mau
  - **Effort:** 20p
  - **Source ref:** `packages/web/src/pages/bieu-mau/BieuMauForm.tsx:117`

- ⏳ **MB136** [QA-UI] Edit mode fall through to create when detail missing
  - **Kết quả:** TBD
  - **Verify:** Throttle detail API mở edit form, submit check không gọi create endpoint
  - **Tool:** MCP DevTools throttle + click · **Owner:** Agent C · **Module:** bieu-mau
  - **Effort:** 30p
  - **Source ref:** `packages/web/src/pages/bieu-mau/BieuMauForm.tsx:101`

- ⏳ **MB146** [QA-UI] Bulk folder actions only on selected rows current page
  - **Kết quả:** TBD
  - **Verify:** Select rows page 1, switch page 2, click bulk action check payload đúng ids (không pre-page)
  - **Tool:** MCP click + list_network_requests · **Owner:** Agent C · **Module:** bieu-mau
  - **Effort:** 30p
  - **Source ref:** `packages/web/src/pages/bieu-mau/ThuMucBieuMauPage.tsx:128`

- ⏳ **MB154** [QA-UI] Bulk actions use current-page rows with stale selection
  - **Kết quả:** TBD
  - **Verify:** Dup #146 — bulk select cross-page, check payload đúng
  - **Tool:** MCP click + list_network_requests · **Owner:** Agent C · **Module:** bieu-mau
  - **Effort:** 30p
  - **Source ref:** `packages/web/src/pages/bieu-mau/ThuMucBieuMauPage.tsx:124`

- ⏳ **MC020** [QA-UI] Removed queued files can still upload and be imported
  - **Kết quả:** TBD
  - **Verify:** MCP UI: add file → trigger upload → remove file ngay → confirm import, check upload vẫn submit qua network
  - **Tool:** MCP · **Owner:** Agent C · **Module:** bieu-mau
  - **Effort:** 45p
  - **Source ref:** `packages/web/src/pages/bieu-mau/BieuMauImportWizard.tsx:115`

- ⏳ **MC023** [QA-UI] Removed files re-enter hidden import payload
  - **Kết quả:** TBD
  - **Verify:** MCP UI: add 3 files, remove 1, submit, check hidden payload qua DOM/network có file đã remove
  - **Tool:** MCP · **Owner:** Agent C · **Module:** bieu-mau
  - **Effort:** 45p
  - **Source ref:** `packages/web/src/pages/bieu-mau/BieuMauImportWizard.tsx:115`

- ⏳ **MC034** [QA-UI] In-flight upload restores file after remove/replace
  - **Kết quả:** TBD
  - **Verify:** MCP UI: add file → upload chậm → remove/replace ngay → check state qua snapshot + network response handling
  - **Tool:** MCP · **Owner:** Agent C · **Module:** bieu-mau
  - **Effort:** 45p
  - **Source ref:** `packages/web/src/pages/bieu-mau/components/BieuMauFileUpload.tsx:45`

- ⏳ **MB066** [QA-UI] Bulk approve offered for rejected rows in pending tab
  - **Kết quả:** TBD
  - **Verify:** Mở mixed pending tab có rejected rows, select rejected, check button bulk approve disabled
  - **Tool:** MCP click + take_snapshot · **Owner:** Agent C · **Module:** common
  - **Effort:** 20p
  - **Source ref:** `packages/web/src/pages/tv-nhanh/kho-cau-hoi/hooks/use-kch-filters.ts:62`

- ⏳ **MB072** [QA-UI] URL pagination applied to fetches not to table pager
  - **Kết quả:** TBD
  - **Verify:** Deep-link URL ?page=3, check table pager hiển thị page 3 (highlighted)
  - **Tool:** MCP navigate + take_snapshot · **Owner:** Agent C · **Module:** common
  - **Effort:** 20p
  - **Source ref:** `packages/web/src/hooks/use-pagination-params.ts:13`

- ⏳ **MB084** [QA-UI] Rejected async action callbacks become unhandled promises
  - **Kết quả:** TBD
  - **Verify:** Click approve, BE reject, check console.error có handle (không unhandled promise rejection)
  - **Tool:** MCP click + list_console_messages · **Owner:** Agent C · **Module:** common
  - **Effort:** 20p
  - **Source ref:** `packages/web/src/components/ApprovalActions/approval-actions.tsx:81`

- ⏳ **MB109** [QA-UI] custom-multi controls not connected to form state
  - **Kết quả:** TBD
  - **Verify:** Mở SearchPanel có custom-multi, chọn value, submit check form payload có value
  - **Tool:** MCP click + list_network_requests · **Owner:** Agent C · **Module:** common
  - **Effort:** 20p
  - **Source ref:** `packages/web/src/components/SearchPanel/search-panel.tsx:60`

- ⏳ **MB110** [QA-UI] Count label drops zero counts not matching contract
  - **Kết quả:** TBD
  - **Verify:** Mở StateTabs có tab count=0, check label render '0' không bị drop
  - **Tool:** MCP evaluate_script DOM text · **Owner:** Agent C · **Module:** common
  - **Effort:** 15p
  - **Source ref:** `packages/web/src/components/StateTabs/state-tabs.tsx:115`

- ⏳ **MB114** [QA-UI] Whitespace-only rejection/supplement reasons pass
  - **Kết quả:** TBD
  - **Verify:** Dup pattern — whitespace reason approval action, submit check reject
  - **Tool:** MCP fill + submit · **Owner:** Agent C · **Module:** common
  - **Effort:** 15p
  - **Source ref:** `packages/web/src/components/ApprovalActions/approval-actions.tsx:162`

- ⏳ **MB119** [QA-UI] Count labels do not match StateTabs rendering contract
  - **Kết quả:** TBD
  - **Verify:** Dup #110 — StateTabs count label render
  - **Tool:** MCP evaluate_script DOM · **Owner:** Agent C · **Module:** common
  - **Effort:** 15p
  - **Source ref:** `packages/web/src/components/StateTabs/state-tabs.tsx:115`

- ⏳ **MB120** [QA-UI] Extension allow-list rejects valid files no MIME
  - **Kết quả:** TBD
  - **Verify:** Upload file .pdf với MIME bị omit (drag-drop), check upload accept (không reject)
  - **Tool:** MCP upload_file · **Owner:** Agent C · **Module:** common
  - **Effort:** 20p
  - **Source ref:** `packages/web/src/components/FileUpload/file-upload.tsx:64`

- ⏳ **MB137** [QA-UI] Bulk approve submits rejected rows from Chờ duyệt tab
  - **Kết quả:** TBD
  - **Verify:** Dup #66 — mixed pending tab có rejected, bulk approve check không submit rejected
  - **Tool:** MCP click + list_network_requests · **Owner:** Agent C · **Module:** common
  - **Effort:** 20p
  - **Source ref:** `packages/web/src/pages/tv-nhanh/kho-cau-hoi/hooks/use-kch-filters.ts:62`

- ⏳ **MB165** [QA-UI] Rejected transition callbacks unhandled promise rejections
  - **Kết quả:** TBD
  - **Verify:** Dup #84 — click approve BE reject check no unhandled promise
  - **Tool:** MCP click + list_console_messages · **Owner:** Agent C · **Module:** common
  - **Effort:** 20p
  - **Source ref:** `packages/web/src/components/ApprovalActions/approval-actions.tsx:81`

- ⏳ **MB173** [QA-UI] Network failures rendered as empty catalog
  - **Kết quả:** TBD
  - **Verify:** Block API linh-vuc, mở select, check hiện error message thay vì empty catalog
  - **Tool:** MCP DevTools network block · **Owner:** Agent C · **Module:** common
  - **Effort:** 20p
  - **Source ref:** `packages/web/src/components/LinhVucKinhDoanhSelect/index.tsx:62`

- ⏳ **MC005** [QA-UI] Import validation can restore stale state after wizard closed
  - **Kết quả:** TBD
  - **Verify:** MCP UI: trigger validation slow, close wizard, mở lại check stale state qua snapshot + DOM inspect
  - **Tool:** MCP · **Owner:** Agent C · **Module:** common
  - **Effort:** 45p
  - **Source ref:** `packages/web/src/pages/tv-nhanh/kho-cau-hoi/components/KhoCauHoiImportWizard.tsx:51`

- ⏳ **MB113** [QA-UI] TW-approved aggregation candidates rendered but not selectable
  - **Kết quả:** TBD
  - **Verify:** Mở tong-hop có TW-approved candidate, check checkbox enabled
  - **Tool:** MCP click + take_snapshot · **Owner:** Agent C · **Module:** ct-htpldn
  - **Effort:** 20p
  - **Source ref:** `packages/web/src/pages/ct-htpldn/tong-hop/index.tsx:24`

- ⏳ **MB149** [QA-UI] January deadlines for current year skipped
  - **Kết quả:** TBD
  - **Verify:** Set system date Jan 15 2026, check DeadlineInfoBox hiện deadline Jan 2026 (không skip)
  - **Tool:** MCP emulate clock + snapshot · **Owner:** Agent C · **Module:** ct-htpldn
  - **Effort:** 30p
  - **Source ref:** `packages/web/src/pages/ct-htpldn/components/DeadlineInfoBox.tsx:15`

- ⏳ **MD005** [QA-UI] Draft report edits submitted/overwritten without saving
  - **Kết quả:** TBD
  - **Verify:** Edit Form21a draft cells, MCP click submit without save, verify cells revert hoặc submit dùng giá trị cũ
  - **Tool:** MCP click · **Owner:** Agent C · **Module:** ct-htpldn
  - **Effort:** S
  - **Source ref:** `packages/web/src/pages/ct-htpldn/dot-bao-cao/components/Form21aTable.tsx:31`

- ⏳ **MB170** [QA-UI] Whitespace-only criterion names pass modal validation
  - **Kết quả:** TBD
  - **Verify:** Mở AddTieuChi modal, nhập name='   ', submit check validation reject
  - **Tool:** MCP fill + submit · **Owner:** Agent C · **Module:** danh-gia
  - **Effort:** 15p
  - **Source ref:** `packages/web/src/pages/danh-gia/ke-hoach/components/AddTieuChiModal.tsx:27`

- ⏳ **MB053** [QA-UI] Failed document uploads leave UI stuck disabled
  - **Kết quả:** TBD
  - **Verify:** Upload file fail (size > limit), check upload UI re-enable không bị stuck
  - **Tool:** MCP upload_file + take_snapshot · **Owner:** Agent C · **Module:** dao-tao
  - **Effort:** 20p
  - **Source ref:** `packages/web/src/pages/dao-tao/bai-giang/form/BaiGiangForm.tsx:116`

- ⏳ **MB082** [QA-UI] Imported attendance leaves cached results stale
  - **Kết quả:** TBD
  - **Verify:** Import attendance Excel, check list/cache refetch (không stale)
  - **Tool:** MCP upload_file + take_snapshot · **Owner:** Agent C · **Module:** dao-tao
  - **Effort:** 30p
  - **Source ref:** `packages/web/src/pages/dao-tao/khoa-hoc/hooks/use-khoa-hoc-queries.ts:65`

- ⏳ **MB138** [QA-UI] Detail view omits saved plan content field
  - **Kết quả:** TBD
  - **Verify:** Tạo ke-hoach với plan content, mở detail view check field hiển thị
  - **Tool:** MCP take_snapshot + DOM · **Owner:** Agent C · **Module:** dao-tao
  - **Effort:** 20p
  - **Source ref:** `packages/web/src/pages/dao-tao/ke-hoach/form/KeHoachDaoTaoForm.tsx:201`

- ⏳ **MB158** [QA-UI] Attendance cannot be created for absent date
  - **Kết quả:** TBD
  - **Verify:** Chọn date không trong returned records, click tạo điểm danh, check enabled không bị disable
  - **Tool:** MCP click + DOM · **Owner:** Agent C · **Module:** dao-tao
  - **Effort:** 30p
  - **Source ref:** `packages/web/src/pages/dao-tao/khoa-hoc/tabs/LichHocDiemDanhTab.tsx:20`

- ⏳ **MC004** [QA-UI] Closing import dialog does not cancel in-flight state updates
  - **Kết quả:** TBD
  - **Verify:** MCP UI: trigger import lớn rồi close dialog ngay, check state restore qua list_network_requests + console
  - **Tool:** MCP · **Owner:** Agent C · **Module:** dao-tao
  - **Effort:** 45p
  - **Source ref:** `packages/web/src/pages/dao-tao/ngan-hang-cau-hoi/components/NganHangCauHoiImportDialog.tsx:97`

- ⏳ **MD009** [QA-UI] Removed attendance import file can still be submitted
  - **Kết quả:** TBD
  - **Verify:** Upload diem-danh file rồi click X remove, MCP click Submit, verify file cũ vẫn được POST hay không
  - **Tool:** MCP click + network · **Owner:** Agent C · **Module:** dao-tao
  - **Effort:** S
  - **Source ref:** `packages/web/src/pages/dao-tao/khoa-hoc/components/ImportDiemDanhModal.tsx:34`

- ⏳ **MD018** [QA-UI] Random-config edits accepted in modal but never submitted
  - **Kết quả:** TBD
  - **Verify:** Open DeKiemTra form random-config modal, edit values, click OK, verify payload network request có chứa updated config
  - **Tool:** MCP + network · **Owner:** Agent C · **Module:** dao-tao
  - **Effort:** S
  - **Source ref:** `packages/web/src/pages/dao-tao/de-kiem-tra/form/DeKiemTraForm.tsx:129`

- ⏳ **MD021** [QA-UI] Attendance edits saved to wrong date after picker change
  - **Kết quả:** TBD
  - **Verify:** MCP open LichHoc tab, edit attendance, change date picker without save, click save, verify payload date đúng date mới
  - **Tool:** MCP + network · **Owner:** Agent C · **Module:** dao-tao
  - **Effort:** M
  - **Source ref:** `packages/web/src/pages/dao-tao/khoa-hoc/tabs/LichHocDiemDanhTab.tsx:44`

- ⏳ **MD031** [QA-UI] Unsaved attendance and result edits overwritten by query refresh
  - **Kết quả:** TBD
  - **Verify:** MCP edit DiemDanh tab values, trigger query refetch (refocus tab/network event), verify edits có bị revert
  - **Tool:** MCP click · **Owner:** Agent C · **Module:** dao-tao
  - **Effort:** M
  - **Source ref:** `packages/web/src/pages/dao-tao/khoa-hoc/components/DiemDanhTab.tsx:29`

- ⏳ **MD038** [QA-UI] Budget field silently saves cleared or negative input as number
  - **Kết quả:** TBD
  - **Verify:** MCP input budget field cleared/negative, click save, verify payload có giá trị invalid hay validation block
  - **Tool:** MCP + network · **Owner:** Agent C · **Module:** dao-tao
  - **Effort:** S
  - **Source ref:** `packages/web/src/pages/dao-tao/ke-hoach/form/KeHoachDaoTaoForm.tsx:77`

- ⏳ **MB060** [QA-UI] Optional-field clears omitted from update payloads
  - **Kết quả:** TBD
  - **Verify:** Edit doanh-nghiep, clear optional field, save check payload có field=null
  - **Tool:** MCP fill + list_network_requests · **Owner:** Agent C · **Module:** doanh-nghiep
  - **Effort:** 20p
  - **Source ref:** `packages/web/src/pages/doanh-nghiep/detail/index.tsx:147`

- ⏳ **MB101** [QA-UI] Legacy edit alias drops business id during redirect
  - **Kết quả:** TBD
  - **Verify:** Dup #25 — legacy edit alias redirect check giữ id
  - **Tool:** MCP navigate + URL check · **Owner:** Agent C · **Module:** doanh-nghiep
  - **Effort:** 20p
  - **Source ref:** `packages/web/src/pages/doanh-nghiep/index.tsx:73`

- ⏳ **MB161** [QA-UI] Legacy edit alias drops enterprise id
  - **Kết quả:** TBD
  - **Verify:** Dup #25 #101 — legacy edit alias redirect giữ enterprise id
  - **Tool:** MCP navigate + URL · **Owner:** Agent C · **Module:** doanh-nghiep
  - **Effort:** 20p
  - **Source ref:** `packages/web/src/pages/doanh-nghiep/index.tsx:41`

- ⏳ **MB091** [QA-UI] Assignment mode submit stale TVV as personal assignee
  - **Kết quả:** TBD
  - **Verify:** Mở phan cong modal, chọn TVV, switch mode personal, check payload có account đúng (không TVV stale)
  - **Tool:** MCP click + list_network_requests · **Owner:** Agent C · **Module:** hoi-dap
  - **Effort:** 30p
  - **Source ref:** `packages/web/src/pages/hoi-dap/detail/components/PhanCongModal.tsx:98`

- ⏳ **MB175** [QA-UI] Deep-linked filters displayed but not applied to query
  - **Kết quả:** TBD
  - **Verify:** Deep-link URL filter, check form hiện + API request có param filter
  - **Tool:** MCP navigate + list_network_requests · **Owner:** Agent C · **Module:** hoi-dap
  - **Effort:** 20p
  - **Source ref:** `packages/web/src/pages/hoi-dap/da-xu-ly/index.tsx:12`

- ⏳ **MD033** [QA-UI] Saved draft responses render as blank form after query resolves
  - **Kết quả:** TBD
  - **Verify:** MCP save draft response, navigate away rồi quay lại detail, verify form load draft content hay blank
  - **Tool:** MCP click · **Owner:** Agent C · **Module:** hoi-dap
  - **Effort:** S
  - **Source ref:** `packages/web/src/pages/hoi-dap/detail/index.tsx:274`

- ⏳ **MD039** [QA-UI] Edit save discards milestone edits cannot clear last payment
  - **Kết quả:** TBD
  - **Verify:** MCP edit HopDong milestones và clear last payment, save, verify milestone edits persist và last payment xóa được
  - **Tool:** MCP click · **Owner:** Agent C · **Module:** hop-dong
  - **Effort:** M
  - **Source ref:** `packages/web/src/pages/hop-dong-tv/form/HopDongForm.tsx:169`

- ⏳ **MB055** [QA-UI] Batch approval selection survives filter/pagination
  - **Kết quả:** TBD
  - **Verify:** Select rows chi-tra, đổi filter/page, click batch approve check không submit hidden rows
  - **Tool:** MCP click + list_network_requests · **Owner:** Agent C · **Module:** other
  - **Effort:** 30p
  - **Source ref:** `packages/web/src/pages/chi-tra/list/index.tsx:34`

- ⏳ **MB063** [QA-UI] Status filter survives tab changes overrides selected tab
  - **Kết quả:** TBD
  - **Verify:** Set status filter trên tab A, switch sang tab B, check status filter của tab A không carry over
  - **Tool:** MCP click + URL check · **Owner:** Agent C · **Module:** other
  - **Effort:** 20p
  - **Source ref:** `packages/web/src/pages/tv-nhanh/use-tvn-filters.ts:31`

- ⏳ **MB068** [QA-UI] Selected rows survive filter changes batch approval hidden
  - **Kết quả:** TBD
  - **Verify:** Dup pattern #55 — select rows, đổi filter, batch approve check không submit hidden
  - **Tool:** MCP click + list_network_requests · **Owner:** Agent C · **Module:** other
  - **Effort:** 30p
  - **Source ref:** `packages/web/src/pages/chi-tra/list/index.tsx:56`

- ⏳ **MB083** [QA-UI] Hoàn thành blocks legal-advice results >1000 chars
  - **Kết quả:** TBD
  - **Verify:** Nhập legal advice >1000 chars, click Hoàn thành check submit OK (không bị block validation)
  - **Tool:** MCP fill + submit · **Owner:** Agent C · **Module:** other
  - **Effort:** 20p
  - **Source ref:** `packages/web/src/pages/tv-chuyen-sau/detail/index.tsx:363`

- ⏳ **MB087** [QA-UI] Payment amount parser lets NaN pass validation
  - **Kết quả:** TBD
  - **Verify:** Nhập amount='abc' hoặc 'NaN', submit check form validation reject
  - **Tool:** MCP fill_form + submit · **Owner:** Agent C · **Module:** other
  - **Effort:** 15p
  - **Source ref:** `packages/web/src/pages/chi-tra/detail/forms/ThanhToanForm.tsx:98`

- ⏳ **MB093** [QA-UI] Whitespace-only rejection reason pass client validation
  - **Kết quả:** TBD
  - **Verify:** Nhập rejection reason='   ', submit check client validation reject
  - **Tool:** MCP fill + submit · **Owner:** Agent C · **Module:** other
  - **Effort:** 15p
  - **Source ref:** `packages/web/src/pages/chi-tra/detail/forms/ThamDinhForm.tsx:51`

- ⏳ **MB103** [QA-UI] Status-changing mutations leave list/tab caches stale
  - **Kết quả:** TBD
  - **Verify:** Change status chi-tra detail, back ra list/tab check counts/rows update
  - **Tool:** MCP click + take_snapshot · **Owner:** Agent C · **Module:** other
  - **Effort:** 30p
  - **Source ref:** `packages/web/src/pages/chi-tra/detail/use-ho-so-chi-tra-detail.ts:107`

- ⏳ **MB107** [QA-UI] Required reason fields accept blank whitespace
  - **Kết quả:** TBD
  - **Verify:** Dup pattern #88 — reason='   ', submit check reject
  - **Tool:** MCP fill + submit · **Owner:** Agent C · **Module:** other
  - **Effort:** 15p
  - **Source ref:** `packages/web/src/pages/chi-tra/detail/forms/PheDuyetActions.tsx:50`

- ⏳ **MB121** [QA-UI] Mandatory reason fields accept whitespace-only
  - **Kết quả:** TBD
  - **Verify:** Dup #107 — reason whitespace check reject
  - **Tool:** MCP fill + submit · **Owner:** Agent C · **Module:** other
  - **Effort:** 15p
  - **Source ref:** `packages/web/src/pages/chi-tra/detail/forms/PheDuyetActions.tsx:50`

- ⏳ **MB122** [QA-UI] Status tabs keep stale explicit status filter
  - **Kết quả:** TBD
  - **Verify:** Dup #63 — tab switch status filter stale check
  - **Tool:** MCP click + URL · **Owner:** Agent C · **Module:** other
  - **Effort:** 20p
  - **Source ref:** `packages/web/src/pages/tv-nhanh/list/index.tsx:34`

- ⏳ **MB132** [QA-UI] Missing /hoi-dap/tao-moi alias falls into detail route
  - **Kết quả:** TBD
  - **Verify:** Navigate /hoi-dap/tao-moi, check không bị match detail route (treat 'tao-moi' as id)
  - **Tool:** MCP navigate + URL/snapshot · **Owner:** Agent C · **Module:** other
  - **Effort:** 15p
  - **Source ref:** `packages/web/src/routes/router.tsx:101`

- ⏳ **MB152** [QA-UI] Create page preassigns consultant outside CG constraints
  - **Kết quả:** TBD
  - **Verify:** Mở tao-moi tv-chuyen-sau với linh-vuc X, check consultant pre-select chỉ trong CG có linh-vuc X
  - **Tool:** MCP click + DOM dropdown · **Owner:** Agent C · **Module:** other
  - **Effort:** 30p
  - **Source ref:** `packages/web/src/pages/tv-chuyen-sau/tao-moi/index.tsx:106`

- ⏳ **MB157** [QA-UI] Approval defaults ignore thẩm định proposal amount
  - **Kết quả:** TBD
  - **Verify:** Mở approval form sau thẩm định, check số tiền default = đề xuất thẩm định (không 0/null)
  - **Tool:** MCP take_snapshot + DOM · **Owner:** Agent C · **Module:** other
  - **Effort:** 20p
  - **Source ref:** `packages/web/src/pages/chi-tra/detail/forms/ThamDinhForm.tsx:34`

- ⏳ **MC029** [QA-UI] Edit modal opens in create mode while edit detail loading
  - **Kết quả:** TBD
  - **Verify:** MCP UI: click edit row → trước khi load xong, click create → modal state mix, check qua snapshot
  - **Tool:** MCP · **Owner:** Agent C · **Module:** other
  - **Effort:** 45p
  - **Source ref:** `packages/web/src/pages/nguoi-ho-tro/index.tsx:57`

- ⏳ **MB133** [QA-UI] Optional fields cannot be cleared in edit mode
  - **Kết quả:** TBD
  - **Verify:** Dup #12 — edit, clear optional field, save check persist null
  - **Tool:** MCP fill + reload · **Owner:** Agent C · **Module:** qtht
  - **Effort:** 20p
  - **Source ref:** `packages/web/src/pages/quan-tri/tieu-chi-danh-gia/components/TieuChiForm.tsx:29`

- ⏳ **MB142** [QA-UI] Audit export downloads same blob twice
  - **Kết quả:** TBD
  - **Verify:** Mở audit-log, click Export, check chỉ 1 file download (không phải 2)
  - **Tool:** MCP click + DevTools download · **Owner:** Agent C · **Module:** qtht
  - **Effort:** 20p
  - **Source ref:** `packages/web/src/pages/quan-tri/audit-log/index.tsx:209`

- ⏳ **MB176** [QA-UI] URL pagination used for fetching not bound back to table
  - **Kết quả:** TBD
  - **Verify:** Dup #72 — URL ?page=3, check pager highlight
  - **Tool:** MCP navigate + DOM · **Owner:** Agent C · **Module:** qtht
  - **Effort:** 20p
  - **Source ref:** `packages/web/src/pages/quan-tri/danh-muc/components/DanhMucTable.tsx:55`

- ⏳ **MC022** [QA-UI] Import wizard can reopen on canceled validation session
  - **Kết quả:** TBD
  - **Verify:** MCP UI: trigger validation, cancel, reopen modal, check session ID stale qua snapshot + state
  - **Tool:** MCP · **Owner:** Agent C · **Module:** qtht
  - **Effort:** 45p
  - **Source ref:** `packages/web/src/pages/quan-tri/ngay-le/components/ImportNgayLeModal.tsx:59`

- ⏳ **MS009** [QA-UI] Clearing key/cert omits PATCH leaves old credentials
  - **Kết quả:** TBD
  - **Verify:** Open consumer modal, clear key field, submit PATCH, verify network request không include cleared fields
  - **Tool:** MCP fill + list_network_requests · **Owner:** Agent C · **Module:** qtht
  - **Effort:** 20 phút
  - **Source ref:** `packages/web/src/pages/quan-tri/api-consumer/ConsumerFormModal.tsx:37`

- ⏳ **MB076** [QA-UI] Rendered filters not propagated into list/export
  - **Kết quả:** TBD
  - **Verify:** Dup #48 — apply filter TVV, click list/export, check param propagated
  - **Tool:** MCP click + list_network_requests · **Owner:** Agent C · **Module:** tu-van
  - **Effort:** 30p
  - **Source ref:** `packages/web/src/pages/chuyen-gia-tvv/danh-sach/TuVanVienSearchPanel.tsx:34`

- ⏳ **MB088** [QA-UI] Whitespace-only reasons pass validation submitted
  - **Kết quả:** TBD
  - **Verify:** Mở modal cap nhat TT, nhập reason='   ', submit check validation reject
  - **Tool:** MCP fill + submit · **Owner:** Agent C · **Module:** tu-van
  - **Effort:** 15p
  - **Source ref:** `packages/web/src/pages/chuyen-gia-tvv/chi-tiet/ModalCapNhatTrangThai.tsx:26`

- ⏳ **MB108** [QA-UI] Trạng thái filter conflicts with tab-owned status
  - **Kết quả:** TBD
  - **Verify:** Apply status filter, switch tab, check tab status override filter cũ
  - **Tool:** MCP click + URL check · **Owner:** Agent C · **Module:** tu-van
  - **Effort:** 20p
  - **Source ref:** `packages/web/src/pages/chuyen-gia-tvv/danh-sach/TuVanVienSearchPanel.tsx:39`

- ⏳ **MB174** [QA-UI] Server-driven pagination not forwarded to table control
  - **Kết quả:** TBD
  - **Verify:** API trả pagination meta page=3, check table pager highlight page 3
  - **Tool:** MCP take_snapshot + DOM · **Owner:** Agent C · **Module:** tu-van
  - **Effort:** 20p
  - **Source ref:** `packages/web/src/pages/chuyen-gia-tvv/danh-sach/TuVanVienTable.tsx:36`

- ⏳ **MD006** [QA-UI] Voided records remain editable and deletable
  - **Kết quả:** TBD
  - **Verify:** Set to-chuc record sang voided state, MCP open detail, verify Sửa/Xóa button hiển thị và clickable
  - **Tool:** MCP click · **Owner:** Agent C · **Module:** tu-van
  - **Effort:** S
  - **Source ref:** `packages/web/src/pages/chuyen-gia-tvv/to-chuc/detail.tsx:235`

- ⏳ **MD026** [QA-UI] Cancelled certificate removals persist and can be submitted
  - **Kết quả:** TBD
  - **Verify:** MCP open TabNangLuc, mark certificate remove, click Cancel modal, save form, verify certificate vẫn còn trong DB
  - **Tool:** MCP click · **Owner:** Agent C · **Module:** tu-van
  - **Effort:** S
  - **Source ref:** `packages/web/src/pages/chuyen-gia-tvv/chi-tiet/TabNangLuc.tsx:38`

- ⏳ **MD032** [QA-UI] Canceled certificate deletions persist into later saves
  - **Kết quả:** TBD
  - **Verify:** MCP mark certificate delete, click Cancel, edit khác và save, verify cancelled deletion vẫn được submit trong payload
  - **Tool:** MCP click + network · **Owner:** Agent C · **Module:** tu-van
  - **Effort:** S
  - **Source ref:** `packages/web/src/pages/chuyen-gia-tvv/chi-tiet/TabNangLuc.tsx:39`

### Agent E — 51 bug, ~20.9h

- ⏳ **MB177** [QA-API] Completed-training trend reports annual as monthly
  - **Kết quả:** TBD
  - **Verify:** curl GET trend báo cáo annual, check buckets là yearly (không phải monthly)
  - **Tool:** curl + math verify · **Owner:** Agent E · **Module:** bao-cao
  - **Effort:** 30p
  - **Source ref:** `packages/api/src/modules/bao-cao/services/bc-lop-dao-tao-da-dien-ra.service.ts:31`

- ⏳ **MB059** [QA-API] Publish/unpublish idempotency cache not scoped to folder
  - **Kết quả:** TBD
  - **Verify:** curl publish folder A 2 lần với cùng idempotency key, sau đó publish folder B, check không hit cache
  - **Tool:** curl + idempotency-key header · **Owner:** Agent E · **Module:** bieu-mau
  - **Effort:** 30p
  - **Source ref:** `packages/api/src/modules/bieu-mau/thu-muc-bieu-mau.controller.ts:126`

- ⏳ **MB115** [QA-API] Public FTS queries are accent-sensitive
  - **Kết quả:** TBD
  - **Verify:** curl GET search 'thư mục' và 'thu muc', check trả về cùng kết quả (accent-insensitive)
  - **Tool:** curl 2 query + diff · **Owner:** Agent E · **Module:** bieu-mau
  - **Effort:** 20p
  - **Source ref:** `packages/api/src/modules/api-public/services/bieu-mau-public.service.ts:103`

- ⏳ **MB049** [QA-API] Template lookup cannot filter by template type
  - **Kết quả:** TBD
  - **Verify:** curl GET mau-phan-hoi với query loaiMau, check kết quả filtered đúng type
  - **Tool:** curl · **Owner:** Agent E · **Module:** common
  - **Effort:** 15p
  - **Source ref:** `packages/web/src/services/mau-phan-hoi.api.ts:28`

- ⏳ **MB071** [QA-API] Invalid ISO timestamps normalized instead of rejected
  - **Kết quả:** TBD
  - **Verify:** curl với date='2024-13-45T99:99:99', check 400 reject thay vì normalize
  - **Tool:** curl · **Owner:** Agent E · **Module:** common
  - **Effort:** 15p
  - **Source ref:** `packages/api/src/common/utils/date.util.ts:25`

- ⏳ **MD041** [QA-API] Audit logs lose entityId for valid data-meta create responses
  - **Kết quả:** TBD
  - **Verify:** POST create endpoint returning {data, meta} shape, query audit_log verify entityId column có persist hay null
  - **Tool:** curl + DB · **Owner:** Agent E · **Module:** common
  - **Effort:** S
  - **Source ref:** `packages/api/src/common/interceptors/audit.interceptor.ts:102`

- ⏳ **MB046** [QA-API] Standalone reporting periods created but not listable
  - **Kết quả:** TBD
  - **Verify:** curl POST tạo dot-bao-cao standalone, curl GET list check thấy record
  - **Tool:** curl POST + GET · **Owner:** Agent E · **Module:** ct-htpldn
  - **Effort:** 20p
  - **Source ref:** `packages/api/src/modules/ct-htpldn/dot-bao-cao/dot-bao-cao.entity.ts:21`

- ⏳ **MB102** [QA-API] laCongBo=false coerced to true during DTO transform
  - **Kết quả:** TBD
  - **Verify:** curl GET chuong-trinh-htpl?laCongBo=false, check response chỉ laCongBo=false
  - **Tool:** curl · **Owner:** Agent E · **Module:** ct-htpldn
  - **Effort:** 15p
  - **Source ref:** `packages/api/src/modules/ct-htpldn/dto/chuong-trinh-htpl-list-query.dto.ts:15`

- ⏳ **MB148** [QA-API] Manual audit inserts not suppressed, endpoints double-log
  - **Kết quả:** TBD
  - **Verify:** curl POST bao-cao-ct-htpl, query audit_log DB check chỉ 1 entry (không double)
  - **Tool:** curl + psql · **Owner:** Agent E · **Module:** ct-htpldn
  - **Effort:** 30p
  - **Source ref:** `packages/api/src/modules/ct-htpldn/bao-cao-ct-htpl/bao-cao-ct-htpl.controller.ts:26`

- ⏳ **MS021** [QA-API] Export endpoint checks read instead of export permission
  - **Kết quả:** TBD
  - **Verify:** Login role có read CT-HTPLDN nhưng không có export, curl export endpoint, verify 403 hay trả file
  - **Tool:** curl + role không export · **Owner:** Agent E · **Module:** ct-htpldn
  - **Effort:** 20 phút
  - **Source ref:** `packages/api/src/modules/ct-htpldn/chuong-trinh-htpl.controller.ts:64`

- ⏳ **MD016** [QA-API] Feedback sanitizer deletes non-HTML angle bracket content
  - **Kết quả:** TBD
  - **Verify:** POST danh-gia-tvv với content chứa <example> hoặc 3 < 5, verify response preserve content gốc hay strip
  - **Tool:** curl · **Owner:** Agent E · **Module:** danh-gia
  - **Effort:** S
  - **Source ref:** `packages/api/src/modules/chuyen-gia-tvv/dto/create-danh-gia-tvv.dto.ts:4`

- ⏳ **MD020** [QA-API] Selecting cases not idempotent duplicates ket_qua rows
  - **Kết quả:** TBD
  - **Verify:** POST select cases endpoint cùng payload 2 lần liên tiếp, GET ket_qua_danh_gia rows verify count không nhân đôi
  - **Tool:** curl + DB · **Owner:** Agent E · **Module:** danh-gia
  - **Effort:** S
  - **Source ref:** `packages/api/src/modules/danh-gia/ket-qua-danh-gia.service.ts:194`

- ⏳ **MB006** [QA-API] UpdateDeKiemTraDto allows invalid exam shape
  - **Kết quả:** TBD
  - **Verify:** curl PATCH de-kiem-tra với payload exam shape invalid (missing required nested), check 400 reject
  - **Tool:** curl · **Owner:** Agent E · **Module:** dao-tao
  - **Effort:** 20p
  - **Source ref:** `packages/api/src/modules/dao-tao/dto/update-de-kiem-tra.dto.ts:9`

- ⏳ **MB086** [QA-API] Attendance import skip recompute for valid rows
  - **Kết quả:** TBD
  - **Verify:** curl import attendance batch có 1 row invalid, check valid rows vẫn được recompute
  - **Tool:** curl + DB query · **Owner:** Agent E · **Module:** dao-tao
  - **Effort:** 30p
  - **Source ref:** `packages/api/src/modules/dao-tao/diem-danh.service.ts:300`

- ⏳ **MB104** [QA-API] Registration close date rejects same-day range valid
  - **Kết quả:** TBD
  - **Verify:** curl POST khoa-hoc với ngayMo=ngayDong same day, check 201 OK (DTO doc nói valid)
  - **Tool:** curl · **Owner:** Agent E · **Module:** dao-tao
  - **Effort:** 15p
  - **Source ref:** `packages/api/src/modules/dao-tao/dto/create-khoa-hoc.dto.ts:98`

- ⏳ **MB112** [QA-API] Bài giảng list duplicates rows for multi-lĩnh-vực records
  - **Kết quả:** TBD
  - **Verify:** Seed bài giảng với 3 linhVuc, curl GET list check 1 row (không phải 3)
  - **Tool:** curl + seed · **Owner:** Agent E · **Module:** dao-tao
  - **Effort:** 30p
  - **Source ref:** `packages/api/src/modules/api-public/services/bai-giang-public.service.ts:42`

- ⏳ **MB164** [QA-API] Create DTOs accept negative size and duration
  - **Kết quả:** TBD
  - **Verify:** curl POST bai-giang size=-1 duration=-10, check 400 reject negative
  - **Tool:** curl · **Owner:** Agent E · **Module:** dao-tao
  - **Effort:** 15p
  - **Source ref:** `packages/api/src/modules/dao-tao/dto/create-bai-giang.dto.ts:34`

- ⏳ **MB167** [QA-API] KetQua Excel import does not transition to DA_NHAP
  - **Kết quả:** TBD
  - **Verify:** curl import Excel ket-qua, psql query check rows status=DA_NHAP
  - **Tool:** curl + psql · **Owner:** Agent E · **Module:** dao-tao
  - **Effort:** 30p
  - **Source ref:** `packages/api/src/modules/dao-tao/ket-qua-dao-tao.service.ts:124`

- ⏳ **MD036** [QA-API] Attendance Excel round-trip loses VANG_PHEP state
  - **Kết quả:** TBD
  - **Verify:** Set diem_danh records VANG_PHEP, export Excel, re-import file, verify state VANG_PHEP còn nguyên hay convert
  - **Tool:** Export + import API · **Owner:** Agent E · **Module:** dao-tao
  - **Effort:** M
  - **Source ref:** `packages/api/src/modules/dao-tao/diem-danh.service.ts:197`

- ⏳ **MS015** [QA-API] Upload type validation accepts mismatched spoofed types
  - **Kết quả:** TBD
  - **Verify:** Curl upload với file .exe rename .pdf, verify pipe magic-byte check hay chỉ extension/mimetype
  - **Tool:** curl multipart upload · **Owner:** Agent E · **Module:** dao-tao
  - **Effort:** 30 phút
  - **Source ref:** `packages/api/src/modules/dao-tao/pipes/bai-giang-file-validation.pipe.ts:5`

- ⏳ **MS042** [QA-API] Test distribution persists arbitrary lesson IDs without validation
  - **Kết quả:** TBD
  - **Verify:** Curl create đề kiểm tra với lesson_id không thuộc khóa học, verify validation reject hay persist
  - **Tool:** curl + invalid lessonId · **Owner:** Agent E · **Module:** dao-tao
  - **Effort:** 25 phút
  - **Source ref:** `packages/api/src/modules/dao-tao/de-kiem-tra.service.ts:472`

- ⏳ **MB163** [QA-API] Lowering total employees bypasses subcount validation
  - **Kết quả:** TBD
  - **Verify:** curl PATCH doanh-nghiep giảm totalEmployees < sum subcount, check 400 reject
  - **Tool:** curl · **Owner:** Agent E · **Module:** doanh-nghiep
  - **Effort:** 20p
  - **Source ref:** `packages/api/src/modules/doanh-nghiep/doanh-nghiep.service.ts:246`

- ⏳ **MS002** [QA-API] Enterprise registration fake CAPTCHA token
  - **Kết quả:** TBD
  - **Verify:** Inspect network request đăng ký DN, verify CAPTCHA token là hard-coded fake string không validate BE
  - **Tool:** MCP list_network_requests + curl · **Owner:** Agent E · **Module:** doanh-nghiep
  - **Effort:** 20 phút
  - **Source ref:** `packages/web/src/pages/auth/register/doanh-nghiep.tsx:173`

- ⏳ **MB044** [QA-API] Batch DTOs allow duplicate IDs
  - **Kết quả:** TBD
  - **Verify:** curl batch cong-khai với ids [1,1,2,2], check 400 validation reject duplicate
  - **Tool:** curl · **Owner:** Agent E · **Module:** hoi-dap
  - **Effort:** 15p
  - **Source ref:** `packages/api/src/modules/hoi-dap/dto/batch-cong-khai.dto.ts:4`

- ⏳ **MB074** [QA-API] Processed congKhai=false query coerced to true
  - **Kết quả:** TBD
  - **Verify:** curl GET hoi-dap?congKhai=false, check response chỉ trả congKhai=false rows
  - **Tool:** curl · **Owner:** Agent E · **Module:** hoi-dap
  - **Effort:** 15p
  - **Source ref:** `packages/api/src/modules/hoi-dap/dto/processed-hoi-dap-list-query.dto.ts:16`

- ⏳ **MB169** [QA-API] String false can submit a draft response
  - **Kết quả:** TBD
  - **Verify:** curl PATCH phan-hoi với isDraft='false' (string), check coerce đúng boolean false (không phải true)
  - **Tool:** curl · **Owner:** Agent E · **Module:** hoi-dap
  - **Effort:** 15p
  - **Source ref:** `packages/api/src/modules/hoi-dap/dto/update-phan-hoi.dto.ts:18`

- ⏳ **MD011** [QA-API] CreatePhanHoiDto accepts attachment IDs not consumed downstream
  - **Kết quả:** TBD
  - **Verify:** POST /api/v1/phan-hoi với attachment IDs, verify response success rồi GET phan-hoi check attachment có persist không
  - **Tool:** curl · **Owner:** Agent E · **Module:** hoi-dap
  - **Effort:** S
  - **Source ref:** `packages/api/src/modules/hoi-dap/dto/create-phan-hoi.dto.ts:21`

- ⏳ **MB027** [QA-API] Required text fields accept whitespace-only
  - **Kết quả:** TBD
  - **Verify:** curl PATCH NHT trạng thái với reason = '   ', check 400 validation reject
  - **Tool:** curl · **Owner:** Agent E · **Module:** other
  - **Effort:** 15p
  - **Source ref:** `packages/api/src/modules/nguoi-ho-tro/dto/cap-nhat-trang-thai-nht.dto.ts:25`

- ⏳ **MB061** [QA-API] Copying Feb 29 to non-leap year creates March 1
  - **Kết quả:** TBD
  - **Verify:** curl copy ngay-le 2024-02-29 sang 2025, check trả về 2025-02-28 (last day Feb) hoặc error, không phải 03-01
  - **Tool:** curl · **Owner:** Agent E · **Module:** other
  - **Effort:** 20p
  - **Source ref:** `packages/api/src/modules/ngay-le/ngay-le.service.ts:117`

- ⏳ **MB070** [QA-API] Training KPI cache ignores requested period
  - **Kết quả:** TBD
  - **Verify:** curl dashboard period A → cache; curl period B với cùng key, check trả khác data
  - **Tool:** curl 2 lần + diff · **Owner:** Agent E · **Module:** other
  - **Effort:** 30p
  - **Source ref:** `packages/api/src/modules/dashboard/dashboard.service.ts:906`

- ⏳ **MB156** [QA-API] Missing hoSoJson bypasses DVC intake validation
  - **Kết quả:** TBD
  - **Verify:** curl POST tiep-nhan-dvc no hoSoJson, check 400 validation reject
  - **Tool:** curl · **Owner:** Agent E · **Module:** other
  - **Effort:** 15p
  - **Source ref:** `packages/api/src/modules/chi-tra/dto/tiep-nhan-dvc.dto.ts:12`

- ⏳ **MB168** [QA-API] Tab counts ignore doanhNghiepId filter used by list
  - **Kết quả:** TBD
  - **Verify:** curl GET chi-tra tab counts với doanhNghiepId=X, check counts khớp list filtered
  - **Tool:** curl 2 endpoint + diff · **Owner:** Agent E · **Module:** other
  - **Effort:** 30p
  - **Source ref:** `packages/api/src/modules/chi-tra/chi-tra.service.ts:178`

- ⏳ **MD022** [QA-API] Import validation silently truncates overlong text
  - **Kết quả:** TBD
  - **Verify:** Import ngay-le Excel với text >255 chars, verify response báo error hay silent truncate, check DB stored value
  - **Tool:** curl + DB · **Owner:** Agent E · **Module:** other
  - **Effort:** S
  - **Source ref:** `packages/api/src/modules/ngay-le/ngay-le-import.service.ts:193`

- ⏳ **MS008** [QA-API] Unvalidated sortBy interpolated ORDER BY
  - **Kết quả:** TBD
  - **Verify:** Curl notification list endpoint với sortBy=invalid_column hoặc SQL injection payload, verify 400 hay execute
  - **Tool:** curl + payload injection · **Owner:** Agent E · **Module:** other
  - **Effort:** 20 phút
  - **Source ref:** `packages/api/src/modules/notification/notification.controller.ts:43`

- ⏳ **MS033** [QA-API] Consumer expiry accepted by DTO not persisted/enforced
  - **Kết quả:** TBD
  - **Verify:** Curl tạo API consumer với expiry, verify field persist DB + endpoint enforce expiry khi consumer expired
  - **Tool:** curl + DBA query check · **Owner:** Agent E · **Module:** other
  - **Effort:** 45 phút
  - **Source ref:** `packages/api/src/modules/api-public/dto/create-api-consumer.dto.ts:56`

- ⏳ **MB038** [QA-API] TVCS update can bypass expert-field compatibility
  - **Kết quả:** TBD
  - **Verify:** curl PATCH TVCS với expert có linhVuc không khớp, check 400 reject
  - **Tool:** curl · **Owner:** Agent E · **Module:** tu-van
  - **Effort:** 30p
  - **Source ref:** `packages/api/src/modules/tu-van/noi-dung-tu-van-cs.service.ts:121`

- ⏳ **MB067** [QA-API] Video session link validation permits unusable values
  - **Kết quả:** TBD
  - **Verify:** curl POST phien-tu-van link='javascript:' hoặc 'ftp://...', check 400 reject
  - **Tool:** curl · **Owner:** Agent E · **Module:** tu-van
  - **Effort:** 15p
  - **Source ref:** `packages/api/src/modules/tu-van/dto/create-phien-tu-van.dto.ts:18`

- ⏳ **MB075** [QA-API] Blank quick-consultation answers pass validation
  - **Kết quả:** TBD
  - **Verify:** curl POST tra-loi tvn answer='', check 400 validation reject
  - **Tool:** curl · **Owner:** Agent E · **Module:** tu-van
  - **Effort:** 15p
  - **Source ref:** `packages/api/src/modules/tu-van/dto/tra-loi-tu-van-nhanh.dto.ts:5`

- ⏳ **MB081** [QA-API] Contract value can be lowered below scheduled payments
  - **Kết quả:** TBD
  - **Verify:** curl PATCH hop-dong giảm giá trị < tổng payment scheduled, check 400 reject
  - **Tool:** curl + seed payments · **Owner:** Agent E · **Module:** tu-van
  - **Effort:** 30p
  - **Source ref:** `packages/api/src/modules/tu-van/hop-dong-tv/hop-dong-tu-van.service.ts:303`

- ⏳ **MB147** [QA-API] hieuLuc=false query coerced to true
  - **Kết quả:** TBD
  - **Verify:** Dup pattern — curl GET kho-cau-hoi?hieuLuc=false check chỉ hieuLuc=false rows
  - **Tool:** curl · **Owner:** Agent E · **Module:** tu-van
  - **Effort:** 15p
  - **Source ref:** `packages/api/src/modules/tu-van/dto/kho-cau-hoi-list-query.dto.ts:24`

- ⏳ **MB172** [QA-API] PhienTuVan create sends notif to tu_van_vien id wrong
  - **Kết quả:** TBD
  - **Verify:** curl POST phien-tu-van, psql query notification check recipient_id = tai_khoan id (không tu_van_vien id)
  - **Tool:** curl + psql · **Owner:** Agent E · **Module:** tu-van
  - **Effort:** 30p
  - **Source ref:** `packages/api/src/modules/tu-van/phien-tu-van.service.ts:194`

- ⏳ **MD001** [QA-API] Trao-doi attachment link failures silently swallowed
  - **Kết quả:** TBD
  - **Verify:** Upload trao-doi với invalid attachment ID, curl POST /api/v1/lich-su-trao-doi, verify response code và DB row attachment link
  - **Tool:** curl + DB query · **Owner:** Agent E · **Module:** tu-van
  - **Effort:** M
  - **Source ref:** `packages/api/src/modules/tu-van/lich-su-trao-doi-tv.service.ts:154`

- ⏳ **MD024** [QA-API] Profile file relinking writes entity_type values unused downstream
  - **Kết quả:** TBD
  - **Verify:** PATCH tu-van-vien profile với file relink, GET sub-endpoint files verify entity_type value khớp filter query
  - **Tool:** curl + DB · **Owner:** Agent E · **Module:** tu-van
  - **Effort:** M
  - **Source ref:** `packages/api/src/modules/chuyen-gia-tvv/tu-van-vien.controller.ts:229`

- ⏳ **MS017** [QA-API] Cong-khai file preview accepts orphan file IDs
  - **Kết quả:** TBD
  - **Verify:** Curl preview endpoint với fileId không thuộc TVV nào, verify 404/403 hay trả content
  - **Tool:** curl + orphan fileId · **Owner:** Agent E · **Module:** tu-van
  - **Effort:** 25 phút
  - **Source ref:** `packages/api/src/modules/chuyen-gia-tvv/controllers/tu-van-vien-cong-khai.controller.ts:87`

- ⏳ **MS026** [QA-API] KhoCauHoi import size limit enforced after upload
  - **Kết quả:** TBD
  - **Verify:** Curl upload kho câu hỏi với file >limit, verify reject trước buffer hay sau (memory exhaustion risk)
  - **Tool:** curl + large file · **Owner:** Agent E · **Module:** tu-van
  - **Effort:** 30 phút
  - **Source ref:** `packages/api/src/modules/tu-van/kho-cau-hoi.controller.ts:77`

- ⏳ **MS027** [QA-API] Export bypasses accordion-only context gating
  - **Kết quả:** TBD
  - **Verify:** Curl export hợp đồng TV ngoài context accordion (không qua UI guard), verify accept hay reject
  - **Tool:** curl direct endpoint · **Owner:** Agent E · **Module:** tu-van
  - **Effort:** 25 phút
  - **Source ref:** `packages/api/src/modules/tu-van/hop-dong-tv/hop-dong-tu-van.controller.ts:59`

- ⏳ **MS040** [QA-API] TCTV publish sends before sanitizing public description
  - **Kết quả:** TBD
  - **Verify:** Curl publish TCTV với public_description chứa XSS payload, verify sanitize trước khi persist + send
  - **Tool:** curl + XSS payload · **Owner:** Agent E · **Module:** tu-van
  - **Effort:** 30 phút
  - **Source ref:** `packages/api/src/modules/chuyen-gia-tvv/services/to-chuc-tu-van.service.ts:584`

- ⏳ **MB054** [QA-API] Required free-text reasons accept whitespace
  - **Kết quả:** TBD
  - **Verify:** curl POST gui-thong-bao reason='   ', check 400 reject
  - **Tool:** curl · **Owner:** Agent E · **Module:** vu-viec
  - **Effort:** 15p
  - **Source ref:** `packages/api/src/modules/vu-viec/dto/gui-thong-bao.dto.ts:4`

- ⏳ **MB085** [QA-API] Phân tích vụ việc totals include non-counted statuses
  - **Kết quả:** TBD
  - **Verify:** curl báo cáo phân tích vụ việc, check tổng = sum của visible buckets (không có hidden status)
  - **Tool:** curl + math verify · **Owner:** Agent E · **Module:** vu-viec
  - **Effort:** 30p
  - **Source ref:** `packages/api/src/modules/bao-cao/services/bc-vu-viec-phan-tich.service.ts:67`

- ⏳ **MB139** [QA-API] Checklist length check allows duplicate items
  - **Kết quả:** TBD
  - **Verify:** curl POST kiem-tra vu-viec với checklist ['A','A','B'], check 400 reject duplicate
  - **Tool:** curl · **Owner:** Agent E · **Module:** vu-viec
  - **Effort:** 15p
  - **Source ref:** `packages/api/src/modules/vu-viec/dto/kiem-tra-vu-viec.dto.ts:14`

- ⏳ **MD015** [QA-API] Batch approvals do not create per-case timeline audit rows
  - **Kết quả:** TBD
  - **Verify:** Batch approve nhiều vu-viec qua POST endpoint, GET timeline mỗi case verify có audit row riêng cho từng case
  - **Tool:** curl + DB · **Owner:** Agent E · **Module:** vu-viec
  - **Effort:** M
  - **Source ref:** `packages/api/src/modules/vu-viec/vu-viec.controller.ts:135`

---

## Sprint 3 — Medium cross-role + Partial-QA + best-effort (44 bug, ~36h serial) — **OPTIONAL** (codex revise)

> **OPTIONAL gate:** Chỉ run Sprint 3 nếu Sprint 1 + Sprint 2 finish clean (≥90% bug ✅/❌/⚠️, không stuck 🔄 hoặc 🚫 bulk).
> Nếu S1 hoặc S2 còn nhiều task incomplete → **DEFER Sprint 3 sang Sprint 4** (round riêng).
>
> **Codex rule:**
> - Best-effort race cap retry **50 attempts × 200ms = 10s wall-time max** per bug. >2h tổng/bug → STOP escalate Dev.
> - Partial-QA cần DBA inject state BLOCKED >1h → mark 🚫 ngay, không spend QA time fake.


### Agent D — 14 bug, ~8.5h

- ⏳ **MB008** [QA-cross-role] denyRoles over-blocks multi-role users
  - **Kết quả:** TBD
  - **Verify:** Login multi-role user (có role bị deny + role được allow), check route được phép truy cập đúng sidebar contract
  - **Tool:** MCP 2 tab role + cookies · **Owner:** Agent D · **Module:** common
  - **Effort:** 1h
  - **Source ref:** `packages/web/src/components/PermissionRoute/permission-route.tsx:23`

- ⏳ **MB035** [QA-cross-role] Self-loop fallback denied immediately by role guards
  - **Kết quả:** TBD
  - **Verify:** Login user bị deny, trigger fallback route, check không bị loop denied
  - **Tool:** MCP role + navigate · **Owner:** Agent D · **Module:** common
  - **Effort:** 1h
  - **Source ref:** `packages/web/src/components/PermissionRoute/denied-access.tsx:48`

- ⏳ **MS011** [QA-cross-role] CTDT creation validates parent via unscoped raw query
  - **Kết quả:** TBD
  - **Verify:** Test 2 tenant, tenant A tạo CTDT reference parent của tenant B qua API, verify accept hay reject
  - **Tool:** curl + 2 tenant account · **Owner:** Agent D · **Module:** ct-htpldn
  - **Effort:** 30 phút
  - **Source ref:** `packages/api/src/modules/dao-tao/chuong-trinh-dao-tao.service.ts:222`

- ⏳ **MS028** [QA-cross-role] Resume omits cross-unit guard used by pause
  - **Kết quả:** TBD
  - **Verify:** Test 2 đơn vị, đơn vị A tạo CT pause, đơn vị B gọi resume endpoint, verify cross-unit guard reject
  - **Tool:** curl + 2 unit account · **Owner:** Agent D · **Module:** ct-htpldn
  - **Effort:** 30 phút
  - **Source ref:** `packages/api/src/modules/ct-htpldn/chuong-trinh-htpl.controller.ts:246`

- ⏳ **MS039** [QA-cross-role] Rating list bypasses parent TVV tenant check
  - **Kết quả:** TBD
  - **Verify:** Test 2 tenant TVV, tenant A query rating list TVV của tenant B, verify response empty hay leak data
  - **Tool:** curl + 2 tenant account · **Owner:** Agent D · **Module:** danh-gia
  - **Effort:** 30 phút
  - **Source ref:** `packages/api/src/modules/chuyen-gia-tvv/controllers/danh-gia-tu-van-vien.controller.ts:47`

- ⏳ **MB026** [QA-cross-role] Training module denies tab-only permission users
  - **Kết quả:** TBD
  - **Verify:** Login user chỉ có permission cho subfeature tab dao-tao, check vào được module
  - **Tool:** MCP 2 role + cookies · **Owner:** Agent D · **Module:** dao-tao
  - **Effort:** 1h
  - **Source ref:** `packages/web/src/pages/dao-tao/index.tsx:36`

- ⏳ **MB064** [QA-cross-role] DeKiemTra detail permits users denied from list
  - **Kết quả:** TBD
  - **Verify:** Login user bị deny list de-kiem-tra, navigate direct URL detail, check bị deny
  - **Tool:** MCP 2 role + navigate · **Owner:** Agent D · **Module:** dao-tao
  - **Effort:** 30p
  - **Source ref:** `packages/web/src/pages/dao-tao/index.tsx:129`

- ⏳ **MB166** [QA-cross-role] Create-only GiangVien blocked by parent route guard
  - **Kết quả:** TBD
  - **Verify:** Login GiangVien create-only, navigate /dao-tao/tao-moi, check không bị deny parent guard
  - **Tool:** MCP role + navigate · **Owner:** Agent D · **Module:** dao-tao
  - **Effort:** 30p
  - **Source ref:** `packages/web/src/pages/dao-tao/index.tsx:171`

- ⏳ **MS001** [QA-cross-role] Course CTDT validation unscoped weaker on update
  - **Kết quả:** TBD
  - **Verify:** Test 2 tenant tạo CTDT cùng mã, verify update endpoint không enforce tenant scope qua curl PUT
  - **Tool:** curl + 2 account khác tenant · **Owner:** Agent D · **Module:** dao-tao
  - **Effort:** 30 phút
  - **Source ref:** `packages/api/src/modules/dao-tao/khoa-hoc.service.ts:126`

- ⏳ **MB100** [QA-cross-role] Existing answer hidden in CB_TRA_LOI detail mode
  - **Kết quả:** TBD
  - **Verify:** Login CB_TRA_LOI role, mở tv-nhanh detail có answer cũ, check answer hiện
  - **Tool:** MCP role + take_snapshot · **Owner:** Agent D · **Module:** other
  - **Effort:** 30p
  - **Source ref:** `packages/web/src/pages/tv-nhanh/detail/index.tsx:77`

- ⏳ **MB153** [QA-cross-role] Direct URLs bypass danh-muc tab allowlist
  - **Kết quả:** TBD
  - **Verify:** Login user không có permission tab X, navigate direct URL /danh-muc/X, check bị deny
  - **Tool:** MCP role + navigate · **Owner:** Agent D · **Module:** qtht
  - **Effort:** 30p
  - **Source ref:** `packages/web/src/pages/quan-tri/danh-muc/index.tsx:33`

- ⏳ **MB036** [QA-cross-role] TVV owners cannot edit own capability tab
  - **Kết quả:** TBD
  - **Verify:** Login TVV owner, vào chi-tiet TabNangLuc, check button Sửa enabled
  - **Tool:** MCP role TVV + take_snapshot · **Owner:** Agent D · **Module:** tu-van
  - **Effort:** 30p
  - **Source ref:** `packages/web/src/pages/chuyen-gia-tvv/chi-tiet/TabNangLuc.tsx:31`

- ⏳ **MB117** [QA-cross-role] Owner editing of Năng lực tab broken from detail
  - **Kết quả:** TBD
  - **Verify:** Dup #36 — TVV owner edit NangLuc tab, check enabled
  - **Tool:** MCP role TVV · **Owner:** Agent D · **Module:** tu-van
  - **Effort:** 30p
  - **Source ref:** `packages/web/src/pages/chuyen-gia-tvv/chi-tiet/index.tsx:49`

- ⏳ **MS006** [QA-cross-role] History statistics ignore own-history authorization filter
  - **Kết quả:** TBD
  - **Verify:** Test 2 TVV khác, gọi statistics endpoint verify TVV-A thấy history TVV-B (bypass own-only filter)
  - **Tool:** curl + 2 TVV account · **Owner:** Agent D · **Module:** tu-van
  - **Effort:** 30 phút
  - **Source ref:** `packages/api/src/modules/chuyen-gia-tvv/services/lich-su-ho-tro-tvv.service.ts:45`

### Agent E — 4 bug, ~4.0h

- ⏳ **MC014** [QA-API] Optimistic-lock check not atomic with the update
  - **Kết quả:** TBD
  - **Verify:** curl parallel 2 PATCH cùng version=N của câu hỏi, xargs -P2 retry 20, expect 1 thắng 1 fail nhưng cả 2 PASS
  - **Tool:** curl xargs · **Owner:** Agent E · **Module:** dao-tao
  - **Effort:** 1h
  - **Source ref:** `packages/api/src/modules/dao-tao/ngan-hang-cau-hoi.service.ts:142`

- ⏳ **MB065** [QA-API] Hoi dap period aggregation buckets different date
  - **Kết quả:** TBD
  - **Verify:** curl báo cáo hoi-dap với filter period, check aggregation dùng cùng date expression với filter
  - **Tool:** curl + DB compare · **Owner:** Agent E · **Module:** hoi-dap
  - **Effort:** 1h
  - **Source ref:** `packages/api/src/modules/bao-cao/services/bc-hoi-dap.service.ts:137`

- ⏳ **MC027** [QA-API] Profile optimistic locking is non-atomic pre-check
  - **Kết quả:** TBD
  - **Verify:** curl parallel 2 PATCH profile cùng version=N, xargs -P2 retry 20, expect 1 win 1 reject nhưng cả 2 PASS
  - **Tool:** curl xargs · **Owner:** Agent E · **Module:** qtht
  - **Effort:** 1h
  - **Source ref:** `packages/api/src/modules/tai-khoan/tai-khoan.service.ts:397`

- ⏳ **MC006** [QA-API] Version checks not atomic, concurrent updates overwrite
  - **Kết quả:** TBD
  - **Verify:** curl parallel 2 PATCH cùng version=N, xargs -P2 retry 20 lần, expect 1 thành công + 1 reject nhưng cả 2 PASS
  - **Tool:** curl xargs · **Owner:** Agent E · **Module:** tu-van
  - **Effort:** 1h
  - **Source ref:** `packages/api/src/modules/tu-van/phien-tu-van.service.ts:279`

### Agent F — 26 bug, ~23.5h

- ⏳ **MB023** [Partial-QA] VNeID logins drop session IP and user-agent
  - **Kết quả:** TBD
  - **Verify:** Login qua VNeID mock, query DB session check IP + UA columns không null
  - **Tool:** DBA query + VNeID mock · **Owner:** Agent F · **Module:** auth
  - **Effort:** 1h
  - **Source ref:** `packages/api/src/modules/auth/services/vneid.service.ts:137`

- ⏳ **MC011** [QA-API best-effort] OTP verification non-atomic Redis get/set/delete
  - **Kết quả:** TBD
  - **Verify:** curl parallel 2 POST verify-otp cùng code, race Redis get/del, retry 50 lần expect cả 2 PASS thay vì 1
  - **Tool:** curl xargs · **Owner:** Agent F · **Module:** auth
  - **Effort:** 1.5h
  - **Source ref:** `packages/api/src/modules/auth/auth.service.ts:282`

- ⏳ **MS020** [Partial-QA] Email activation treats inactive role mappings as provisioning
  - **Kết quả:** TBD
  - **Verify:** DBA seed user với role mapping is_active=false, gọi email activation, verify role inactive vẫn được provision
  - **Tool:** DBA seed + curl activation · **Owner:** Agent F · **Module:** auth
  - **Effort:** 1 giờ
  - **Source ref:** `packages/api/src/modules/auth/auth.service.ts:539`

- ⏳ **MB127** [Partial-QA] Subtable hides biểu mẫu after first page
  - **Kết quả:** TBD
  - **Verify:** Seed >10 bieu-mau trong subtable, check pagination hoạt động (page 2 hiện)
  - **Tool:** DBA seed + MCP · **Owner:** Agent F · **Module:** bieu-mau
  - **Effort:** 30p
  - **Source ref:** `packages/web/src/pages/bieu-mau/components/BieuMauSubTable.tsx:17`

- ⏳ **MC031** [QA-API best-effort] Import confirmation processed twice (session not atomic)
  - **Kết quả:** TBD
  - **Verify:** curl parallel 2 POST confirm-import cùng sessionId, xargs -P2 retry 30, expect 1 thành công cả 2 PASS
  - **Tool:** curl xargs · **Owner:** Agent F · **Module:** bieu-mau
  - **Effort:** 1h
  - **Source ref:** `packages/api/src/modules/bieu-mau/bieu-mau.service.ts:833`

- ⏳ **MB069** [Partial-QA] Virus scan status stuck after backend marks clean
  - **Kết quả:** TBD
  - **Verify:** Upload file, BE update scan status clean, poll UI check status update. Cần backend trigger scan complete
  - **Tool:** MCP upload + BE webhook · **Owner:** Agent F · **Module:** common
  - **Effort:** 1h
  - **Source ref:** `packages/web/src/components/FileUpload/file-upload.tsx:140`

- ⏳ **MC024** [QA-API best-effort] HSPL code generation lock ends before insert
  - **Kết quả:** TBD
  - **Verify:** curl parallel POST 5 HSPL qua public API xargs -P5, retry 20 round, check duplicate code
  - **Tool:** curl xargs · **Owner:** Agent F · **Module:** common
  - **Effort:** 1h
  - **Source ref:** `packages/api/src/modules/api-public/services/ho-so-pl-dn-public.service.ts:75`

- ⏳ **MC036** [QA-API best-effort] maNht generation races concurrent creates
  - **Kết quả:** TBD
  - **Verify:** curl parallel POST 5 NHT đồng thời xargs -P5, retry 20 round, check duplicate maNht
  - **Tool:** curl xargs · **Owner:** Agent F · **Module:** common
  - **Effort:** 1h
  - **Source ref:** `packages/api/src/modules/nguoi-ho-tro/services/nguoi-ho-tro.service.ts:167`

- ⏳ **MS038** [Partial-QA] Virus scan terminal states not reliably applied
  - **Kết quả:** TBD
  - **Verify:** DBA seed file với virus_scan_status INFECTED/QUARANTINED, verify FileUpload UI render đúng terminal state
  - **Tool:** DBA seed + MCP snapshot · **Owner:** Agent F · **Module:** common
  - **Effort:** 45 phút
  - **Source ref:** `packages/web/src/components/FileUpload/file-upload.tsx:32`

- ⏳ **MB017** [Partial-QA] Lecture assignment modal builds options from partial pages
  - **Kết quả:** TBD
  - **Verify:** Seed >20 bài giảng để có pagination, mở modal assign, check option list đủ tất cả pages
  - **Tool:** DBA seed + MCP click · **Owner:** Agent F · **Module:** dao-tao
  - **Effort:** 1h
  - **Source ref:** `packages/web/src/pages/dao-tao/khoa-hoc/components/BaiGiangDaGanTab.tsx:51`

- ⏳ **MC013** [QA-API best-effort] Concurrent registration approvals increment enrollment twice
  - **Kết quả:** TBD
  - **Verify:** curl parallel 2 POST approve cùng dangKyId, xargs -P2 retry 30, check enrollment count tăng 2 thay vì 1
  - **Tool:** curl xargs · **Owner:** Agent F · **Module:** dao-tao
  - **Effort:** 1h
  - **Source ref:** `packages/api/src/modules/dao-tao/dang-ky-dao-tao.controller.ts:109`

- ⏳ **MC017** [QA-API best-effort] GiangVien code generation races under concurrent creates
  - **Kết quả:** TBD
  - **Verify:** curl parallel POST 5 giảng viên đồng thời xargs -P5, retry 20, check duplicate maGV
  - **Tool:** curl xargs · **Owner:** Agent F · **Module:** dao-tao
  - **Effort:** 1h
  - **Source ref:** `packages/api/src/modules/dao-tao/giang-vien.service.ts:151`

- ⏳ **MC028** [QA-API best-effort] Course code generation races under concurrent creates
  - **Kết quả:** TBD
  - **Verify:** curl parallel POST 5 khóa học đồng thời xargs -P5, retry 20 round, check duplicate maKH
  - **Tool:** curl xargs · **Owner:** Agent F · **Module:** dao-tao
  - **Effort:** 1h
  - **Source ref:** `packages/api/src/modules/dao-tao/khoa-hoc.service.ts:141`

- ⏳ **MB090** [Partial-QA] Detail child tables truncate after first 100 rows
  - **Kết quả:** TBD
  - **Verify:** Seed >100 ho-so chi-tra cho doanh-nghiep, mở detail tab, check pagination/scroll thấy >100
  - **Tool:** DBA seed + MCP · **Owner:** Agent F · **Module:** doanh-nghiep
  - **Effort:** 1h
  - **Source ref:** `packages/web/src/pages/doanh-nghiep/detail/HoSoChiTraTab.tsx:34`

- ⏳ **MB092** [Partial-QA] Company code generation collides after hard deletes
  - **Kết quả:** TBD
  - **Verify:** DBA hard delete doanh-nghiep với code mới nhất, curl POST tạo mới check không collide
  - **Tool:** DBA DELETE + curl POST · **Owner:** Agent F · **Module:** doanh-nghiep
  - **Effort:** 1h
  - **Source ref:** `packages/api/src/modules/doanh-nghiep/doanh-nghiep.service.ts:347`

- ⏳ **MC037** [QA-API best-effort] linkFilesToEntity overwrites associations in concurrent requests
  - **Kết quả:** TBD
  - **Verify:** curl parallel 2 POST linkFiles cùng entityId fileIds khác nhau, xargs -P2 retry 20, check 1 set ghi đè set kia
  - **Tool:** curl xargs · **Owner:** Agent F · **Module:** other
  - **Effort:** 1h
  - **Source ref:** `packages/api/src/modules/file/file.service.ts:429`

- ⏳ **MC038** [QA-API best-effort] Batch replacement not serialized per role
  - **Kết quả:** TBD
  - **Verify:** curl parallel 2 PUT batch-replace cùng roleId, xargs -P2 retry 20, check 2 set permission ghi đè lẫn nhau
  - **Tool:** curl xargs · **Owner:** Agent F · **Module:** other
  - **Effort:** 1h
  - **Source ref:** `packages/api/src/modules/phan-quyen-du-lieu/phan-quyen-du-lieu.service.ts:145`

- ⏳ **MD025** [Partial-QA] Audit log export silently truncates at 10000 rows
  - **Kết quả:** TBD
  - **Verify:** DBA seed >10k audit log rows, GET export endpoint, verify response có cảnh báo truncate hay silent cut
  - **Tool:** DBA seed + curl · **Owner:** Agent F · **Module:** other
  - **Effort:** M
  - **Source ref:** `packages/api/src/modules/audit-log/audit-log.service.ts:268`

- ⏳ **MC002** [QA-API best-effort] Concurrent activation resends email invalid temp passwords
  - **Kết quả:** TBD
  - **Verify:** curl parallel 2 POST resend-activation cùng userId, xargs -P2 retry 30 lần, check email queue có 2 mật khẩu khác nhau
  - **Tool:** curl xargs · **Owner:** Agent F · **Module:** qtht
  - **Effort:** 1h
  - **Source ref:** `packages/api/src/modules/tai-khoan/tai-khoan.service.ts:737`

- ⏳ **MD003** [Partial-QA] Changing parent unit cap corrupts child hierarchy
  - **Kết quả:** TBD
  - **Verify:** Seed don-vi hierarchy đa cấp, PATCH parent cap qua curl, verify children tree còn integrity qua API list
  - **Tool:** curl + DB · **Owner:** Agent F · **Module:** qtht
  - **Effort:** M
  - **Source ref:** `packages/api/src/modules/quan-tri/don-vi/don-vi.service.ts:194`

- ⏳ **MB041** [Partial-QA] Lexicographic MAX breaks after sequence 9999
  - **Kết quả:** TBD
  - **Verify:** Seed DB tu_van với mã ending 9999, tạo record mới, check mã tiếp theo = 10000 không phải reset
  - **Tool:** DBA seed + curl POST · **Owner:** Agent F · **Module:** tu-van
  - **Effort:** 1h
  - **Source ref:** `packages/api/src/modules/tu-van/helpers/ma-tu-van.helper.ts:27`

- ⏳ **MB118** [Partial-QA] KhoCauHoi code generation reuses codes after hard delete
  - **Kết quả:** TBD
  - **Verify:** DBA hard delete KCH code mới nhất, curl POST tạo check không reuse code
  - **Tool:** DBA DELETE + curl POST · **Owner:** Agent F · **Module:** tu-van
  - **Effort:** 1h
  - **Source ref:** `packages/api/src/modules/tu-van/kho-cau-hoi.service.ts:98`

- ⏳ **MC010** [QA-API best-effort] TVCS unpublish has no state or optimistic-lock guard
  - **Kết quả:** TBD
  - **Verify:** curl parallel 2 POST unpublish cùng tvcsId, xargs -P2 retry 30 lần, expect 1 success 1 reject nhưng cả 2 trả 200
  - **Tool:** curl xargs · **Owner:** Agent F · **Module:** tu-van
  - **Effort:** 1h
  - **Source ref:** `packages/api/src/modules/tu-van/noi-dung-tu-van-cs.controller.ts:249`

- ⏳ **MC016** [QA-API best-effort] maTvv generation races on MAX(seq)+1
  - **Kết quả:** TBD
  - **Verify:** curl parallel POST 5 TVV đồng thời xargs -P5, retry 20 round, check duplicate maTvv hoặc gap
  - **Tool:** curl xargs · **Owner:** Agent F · **Module:** tu-van
  - **Effort:** 1h
  - **Source ref:** `packages/api/src/modules/chuyen-gia-tvv/tu-van-vien.service.ts:567`

- ⏳ **MC012** [QA-API best-effort] Case code allocation duplicates under concurrent creates
  - **Kết quả:** TBD
  - **Verify:** curl parallel POST 5 vụ việc đồng thời xargs -P5, retry 20 round, check trả về duplicate maVuViec
  - **Tool:** curl xargs · **Owner:** Agent F · **Module:** vu-viec
  - **Effort:** 1h
  - **Source ref:** `packages/api/src/modules/vu-viec/helpers/ma-vu-viec.helper.ts:30`

- ⏳ **MS007** [Partial-QA] Virus-flagged documents expose download action
  - **Kết quả:** TBD
  - **Verify:** Cần seed file với virus_scan_status=INFECTED, verify UI vẫn render download button thay vì disable
  - **Tool:** DBA seed + MCP take_snapshot · **Owner:** Agent F · **Module:** vu-viec
  - **Effort:** 45 phút
  - **Source ref:** `packages/web/src/pages/vu-viec/detail/components/SectionTaiLieu.tsx:19`

---

## P5 — Reporter (Coordinator) — SEQUENTIAL sau Sprint 3

- ⏳ **F5.1** Consolidate bug-report đúng template 6 sections
  - **Kết quả:** TBD
  - **Cần có sẵn:** Sprint 1+2+3 ✅
  - **Effort:** 1h

- ⏳ **F5.2** Generate round8-summary.md
  - **Kết quả:** TBD
  - **Cần có sẵn:** F5.1 ✅
  - **Effort:** 1h

- ⏳ **F5.3** Update master todo + state snapshot
  - **Kết quả:** TBD
  - **Cần có sẵn:** F5.2 ✅
  - **Effort:** 30p

---

## Acceptance criteria chung (mỗi bug task)

Mỗi task ⏳ → ✅/❌ phải có:

1. **Screenshot evidence inline base64** → `bug-reports/<category>/image/r8-<bug_id>-*.png`
2. **Bug-report file 6 sections** (Mô tả/Bước/KQ mong đợi/KQ thực tế/Bằng chứng/So sánh) — chỉ tạo nếu confirmed FAIL
3. **SRS verify 3-step** (CLAUDE.md): version check + line quote + verify alternate method
4. **Wording describe requirement** — KHÔNG prescribe button label / endpoint / error code
5. **Network panel evidence** (`list_network_requests` / curl response) khi bug API-related
6. **Update verify-progress.md** ngay sau task done (≤5p)
7. **Claim record lock** (`record-locks.md`) trước mutate, release sau verify

---

## Out-of-scope (106 bug → escalate team khác)

- **Dev-needed (63):** code-review, RLS context, integration test, JWT/OAuth, queue concurrency
- **DBA-needed (31):** psql query, migration up/down, FORCE RLS, audit table
- **DevOps-needed (10):** CI build, partition migration, load test k6, mTLS config
- **SKIP (2):** A11y cosmetic

Reference: bug list per team trong [`all-bugs-classified.json`](all-bugs-classified.json) field `high_non_qa` + `medium_non_qa`.

---

## Tóm tắt

**283 bug QA verify** + 10 setup + 3 report = **296 task**. 6 agent specialist (A setup, B auth UI, C workflow UI, D cross-role, E API, F Partial+race). 3 sprint ~161h serial = ~26-36h wall-time với 6 agent parallel. Phase 0 ~12h sequential.

**Việc tiếp theo:** codex review plan + todo → user approve → start P0 Agent A sequential.
