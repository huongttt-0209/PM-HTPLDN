# Verify Plan EXPANDED — ALL QA-verifiable bugs (2026-05-27, codex revise applied)

> **Scope:** Toàn bộ 283 bug QA verify được (UI + API + cross-role + Partial-QA + best-effort)
> **Source:** [clawpatch-bug-summary-2026-05-27.md](clawpatch-bug-summary-2026-05-27.md) (87 HIGH + 302 Medium confirmed-bug)
> **Classification:** [all-bugs-classified.json](all-bugs-classified.json)
> **Codex review:** [codex-review-expanded-plan.md](codex-review-expanded-plan.md) — REVISE → 8 fix items applied
> **Sprint plan:** 3 sprint (~161h serial, ~40-55h wall-time với 7 agent — Sprint 3 OPTIONAL)

## 1. Tổng quan classification

| Severity × Category | QA-UI | QA-API | cross-role | Partial-QA | API best-effort | **QA-verify** | Non-QA |
|---|--:|--:|--:|--:|--:|--:|--:|
| **HIGH** (87) | 15 | 26 | 7 | 4 | 3 | **55** | 32 |
| **Medium** (302) | 133 | 55 | 14 | 13 | 13 | **228** | 74 |
| **Tổng** | **148** | **81** | **21** | **17** | **16** | **283** | **106** |

**Non-QA 106 escalate:** Dev-needed 63, DBA-needed 31, DevOps-needed 10, SKIP 2 → bug-report riêng cho team khác (xem chi tiết per-bug trong [all-bugs-classified.json](all-bugs-classified.json) field `high_non_qa` + `medium_non_qa`).

---

## 2. Sprint breakdown (3 sprint, ~161h serial, ~40-55h wall-time với 7 agent — codex revise)

| Sprint | Focus | Bug count | Effort serial | Wall-time (7 agent parallel) | Status |
|---|---|--:|--:|--:|:-:|
| **Sprint 1** | HIGH critical + Top 15-20 Medium UI ngắn | 70-75 | ~50h | ~15-20h | Bắt buộc |
| **Sprint 2** | Medium QA-UI bulk + Medium QA-API short | ~160 | ~70h | ~15-20h | Bắt buộc |
| **Sprint 3** | Medium cross-role + Partial-QA + best-effort | 44 | ~36h | ~10-15h | **OPTIONAL** (codex: chỉ run nếu S1+S2 finish clean) |
| **Tổng** | | **~283** | **~161h serial** | **~40-55h parallel** | |

**Codex revise note:**
- 26-36h wall-time NOT realistic. Better: **40-55h** với assumption env stable + fast triage.
- Sprint 3 commit chỉ khi Sprint 1+2 hoàn thành sạch — tránh overcommit dead time.

---

## 3. Agent team — 7 agent (codex split C → C1+C2)

Codex gap #2: Agent C 117 bug overloaded → split C1 (workflow state machine) + C2 (form/UI persistence). Mỗi agent có MCP isolatedContext riêng tránh cookie cross-contamination.

| Agent | Owner | MCP context / Tool | Phụ trách | Bug count target |
|---|---|---|---|--:|
| **A — Setup/Seed Engineer** | Coordinator | `setup-default` | Phase 0: round folder + seed split + JWT + role + record-locks | 10 task |
| **B — Auth/Permission UI** | Specialist | `qtht_01-tab`, `admin-tab`, `readonly-*-tab` | UI permission/auth bugs (HIGH + Medium security UI) | ~31 |
| **C1 — Workflow UI (state machine)** | Specialist | `cb_nv_tw_01-tab`, `tvv_01-tab`, `nht_01-tab` | Submit/approve/complete/reopen workflow chain | ~60 |
| **C2 — Form/UI persistence** | Specialist | `cb_nv_tw_02-tab`, `tvv_02-tab` | Field loss, validation, edit/save, display, filter persist | ~57 |
| **D — Cross-tenant/Cross-role data** | Specialist | `cb_nv_dp_01-tab`, `cb_nv_dp_02-tab`, `cb_nv_bn_01-tab` | Cross-tenant + heavy data | ~21 |
| **E — API Engineer (curl)** | Specialist | curl + bash + jq | QA-API + QA-API best-effort | ~81 |
| **F — Partial-QA + Race + Escalation** | Specialist | curl xargs -P + MCP guest-tab | Partial-QA + best-effort race + escalation evidence | ~33 |
| ~~G — Reporter~~ | — | — | Merged into Coordinator final | — |

**Phối hợp:**
- Agent A sequential trước, output là pre-condition cho B-F.
- Agent B, C1, C2, D, E, F PARALLEL — `record-locks.md` claim record + account-pool ownership trước mutate.
- Coordinator sequential sau cùng: consolidate bug-report + summary.

**Per-agent effort estimate (Sprint 1+2+3):**

- **Agent B (auth UI):** 31 bug, ~15h
- **Agent C1 (workflow UI):** ~60 bug, ~26h
- **Agent C2 (form/UI persistence):** ~57 bug, ~24h
- **Agent D (cross-role):** 21 bug, ~18h
- **Agent E (API):** 81 bug, ~41h
- **Agent F (Partial+best-effort):** 33 bug, ~37h

**Codex revise note:**
- Nếu chỉ 6 agent → merge F vào A sau setup. Wall-time sẽ dài hơn (50-55h thay vì 40-45h).
- Account-pool per agent (vd B owns qtht_01/_02, C1 owns cb_nv_tw_01, C2 owns cb_nv_tw_02) tránh collision.

---

## 3.5. Quality gates — BẮT BUỘC trước full execution (codex risk #4)

1. **Sample bug-report gate (2 reports per agent):**
   - Mỗi Agent B/C1/C2/D/E/F verify 2 bug đầu tiên → tạo bug-report → Coordinator review 6-section template + wording rule pass.
   - Chỉ sau khi 2 sample pass mới được full-speed execution. Tránh rework hàng loạt.

2. **Best-effort race cap-retry rule (codex risk #3):**
   - Bug `QA-API best-effort` retry tối đa **50 attempts × 200ms gap = ~10s wall-time max**.
   - Nếu không repro stable sau 50 attempt → **escalate Dev integration test**, mark 🚫 BLOCKED.
   - Cấm spend >2h cho 1 race bug (cost cap).

3. **Partial-QA BLOCKED fallback rule (codex risk #4):**
   - Bug `Partial-QA` cần DBA/BE inject state (vd M3 virus flag `trang_thai_quet=NHIEM`).
   - **Nếu DBA inject BLOCKED 1h** → verify visible behavior xung quanh + document missing precondition + escalate ticket DBA → mark 🚫 BLOCKED.
   - **Cấm fake DB-only states qua trick** (rule project: feedback_test_method_ui_only).

4. **Account-pool ownership (codex risk #5):**
   - `record-locks.md` ghi rõ entity_id × locked_by_agent × released_at.
   - Cấm 2 agent dùng cùng account/entity cùng lúc.

---

## 4. Phase 0 — Setup (Agent A) — Sequential ~6h + Parallel sub-tasks ~6h (codex revise)

Codex gap #1: 12h sequential A là bottleneck. Split A0.1-A0.7 thành sequential core (~6h) + parallel sub-tasks (~6h chạy đồng thời sub-agent).

### Sequential core (~6h)

| Task | Description | Effort | Output |
|---|---|--:|---|
| **A0.1** | Round8 folder + index README + report template validation | 15p | `output/qa-reports/round8-2026-05-27/` |
| **A0.2** | Verify 10 account login + JWT capture | 30p | `jwt-tokens.txt` gitignored |
| **A0.3** | Tạo 5+ vai trò Read-only custom + tài khoản gán | 2h30 | role-snapshot.md |
| **A0.5** | SRS map 283 bug → SRS file:line | 1h30 | srs-map-r8.md |
| **A0.6** | Baseline app version + deploy + record-locks.md init + **account-pool ownership table** | 1h | record-locks.md + account-pool.md |

### Parallel sub-tasks sau A0.3 (~6h chạy đồng thời, 5 sub-agent)

Codex gap #1 fix: split A0.4 + A0.7 + setup chuyên biệt thành parallel sub-tasks.

| Sub-task | Description | Owner | Effort | Output |
|---|---|---|--:|---|
| **A0.4a** | Seed nhóm 1 — Auth/Permission (CTDT DU_THAO, DN, GV) | Sub-agent A1 | 1h30 | seed-checklist.md |
| **A0.4b** | Seed nhóm 2 — Workflow/Form (TVV no thẻ, CTDT NHAP, dot BC, KHDG, HSCT) | Sub-agent A2 | 2h | seed-checklist.md |
| **A0.4c** | Seed nhóm 3 — Cross-tenant (NHCH 2 ĐV, TCTV 2 ĐV, marker record) | Sub-agent A3 | 2h | seed-checklist.md |
| **A0.4d** | Seed nhóm 4 — Heavy data + virus flag (escalate DBA nếu BLOCKED) | Sub-agent A4 | 1h30-3h | seed-checklist.md + DBA-escalate.md |
| **A0.7** | API consumer credential setup + MailHog OTP path verify + file fixtures (clean/failed/virus) | Sub-agent A5 | 1h30 | api-consumer-tokens.txt + fixtures/ |

**Checkpoint P0:** Sequential core ✅ + 5 sub-tasks parallel ✅ → unlock Phase 1-5.

**Gate:** Nếu A0.4d virus flag BLOCKED (no DBA) → mark 2 bug Partial-QA (M3 + sec idx 7) status 🚫 ngay, không spend QA time fake state.

---

## 5. Phase 1 — QA-UI bugs (Agent B + C)

**Tổng:** 148 bug (15 HIGH + 133 Medium). Split B (auth/permission ~50) + C (workflow/form ~98).

| Bug ID | Title | Module | Tool | Effort | Verify approach |
|---|---|---|---|--:|---|
| `MB024` | Delayed login redirect fires after leaving verify page | auth | MCP navigate_page + timing | 30p | Vào verify-email, ngay khi setTimeout pending thì navigate đi page khác, check k |
| `MB028` | VNeID login button never starts authorization | auth | MCP click + list_network_reque | 20p | Vào /login, click button VNeID, check network có redirect/POST đến VNeID authori |
| `MB050` | Missing callback params leave VNeID page spinning | auth | MCP navigate_page + wait | 20p | Navigate /auth/vneid/callback không có code/state, check hiện error thay vì spin |
| `MB056` | Invalid first-login tokens trigger global logout | auth | MCP navigate_page + URL check | 20p | Vào /first-login-password với token invalid, check hiện local error không bị glo |
| `MB062` | VNeID callback spins forever when code/state missing | auth | MCP navigate_page | 20p | Dup #50 — navigate callback no code/state, check error UI |
| `MB077` | Public first-login password fail triggers global logout | auth | MCP navigate + URL check | 20p | Dup pattern #56 — first-login password fail, check không bị global logout redire |
| `MC009` | OTP auto-submit paths send concurrent verification while pen | auth | MCP | 45p | MCP UI: 2 tab nhập OTP 6 ký tự cuối gần đồng thời, check network có 2 POST verif |
| `MB002` | Changing report type re-runs with previous filters | bao-cao | MCP click + take_snapshot | 20p | Vào báo cáo, submit filter A, đổi report type, check kết quả không re-run với fi |
| `MB021` | Trend line reads primary aggregate rows | bao-cao | MCP evaluate_script chart data | 30p | Run báo cáo có time-series, check trend line render đúng time-series data không  |
| `MB022` | Late URL initialValues never hydrate the form | bao-cao | MCP navigate_page + take_snaps | 20p | Deep-link URL bao-cao với query params, check form filter hydrate giá trị từ URL |
| `MB040` | Custom date range shows error but not validated | bao-cao | MCP fill_form + submit | 20p | Chọn custom date invalid (end < start), check form không submit được |
| `MB051` | Report header omits creator falls back to unit IDs | bao-cao | MCP evaluate_script DOM text | 20p | Run báo cáo, check header có tên người tạo + tên đơn vị (không phải UUID raw) |
| `MB057` | Secondary trend lines read primary breakdown rows | bao-cao | MCP evaluate_script chart data | 30p | Dup pattern #21 — verify secondary trend lines đọc đúng data series |
| `MB096` | Export use form values not matching displayed report | bao-cao | MCP click + list_network_reque | 30p | Run report với filter A, đổi form filter B (chưa submit), click Export check exp |
| `MB097` | Changing report type keeps previous filters/result | bao-cao | MCP click + take_snapshot | 20p | Dup #2 — đổi report type, check filter/result reset |
| `MB105` | Deep-linked URL filters missed by form after catalog load | bao-cao | MCP navigate + wait + snapshot | 20p | Dup #22 — deep-link URL, check form hydrate sau catalog load |
| `MB124` | Header omits required creator when nguoiTao not supplied | bao-cao | MCP evaluate_script DOM | 20p | Dup #51 — run report check header có creator |
| `MB134` | Chart auto-detection drops valid report series | bao-cao | MCP evaluate_script + diff | 30p | Run report với multiple payload shapes (nested/flat), check chart auto-detect re |
| `MB135` | Radar scale ignores maximum score | bao-cao | MCP evaluate_script chart scal | 20p | Run radar chart với score max=10, check axis scale [0, 10] không phải auto |
| `MB141` | Malformed row arrays crash SimpleBarChart | bao-cao | MCP DevTools network override | 30p | Mock API trả về malformed row array, check chart render empty state (không crash |
| `MB150` | Report header never receives required creator/unit label | bao-cao | MCP evaluate_script DOM | 20p | Dup #51 #124 — run report check creator + unit label rendered |
| `MB155` | Time-series report renders rows with zero columns | bao-cao | MCP evaluate_script DOM table | 20p | Run time-series vụ việc report, check rows có >=1 column (không bị zero col) |
| `MB012` | Clearing optional fields in edit mode not persisted | bieu-mau | MCP fill + reload | 20p | Edit ThuMucBieuMau, xóa giá trị optional field, save, reload check field rỗng đã |
| `MB106` | Edit modal submit create before edit detail loads | bieu-mau | MCP click + DevTools network t | 30p | Click edit, ngay lập tức submit trước khi detail load xong, check không gửi crea |
| `MB129` | Create/update errors handled twice | bieu-mau | MCP click + DOM toast | 20p | Trigger create error, check chỉ 1 toast lỗi (không phải 2) |
| `MB130` | Turning public mode off doesn't clear public description | bieu-mau | MCP click + reload | 20p | Bật public mode, nhập public description, off public mode, save, reload check de |
| `MB136` | Edit mode fall through to create when detail missing | bieu-mau | MCP DevTools throttle + click | 30p | Throttle detail API mở edit form, submit check không gọi create endpoint |
| `MB146` | Bulk folder actions only on selected rows current page | bieu-mau | MCP click + list_network_reque | 30p | Select rows page 1, switch page 2, click bulk action check payload đúng ids (khô |
| `MB154` | Bulk actions use current-page rows with stale selection | bieu-mau | MCP click + list_network_reque | 30p | Dup #146 — bulk select cross-page, check payload đúng |
| `MC020` | Removed queued files can still upload and be imported | bieu-mau | MCP | 45p | MCP UI: add file → trigger upload → remove file ngay → confirm import, check upl |
| `MC023` | Removed files re-enter hidden import payload | bieu-mau | MCP | 45p | MCP UI: add 3 files, remove 1, submit, check hidden payload qua DOM/network có f |
| `MC034` | In-flight upload restores file after remove/replace | bieu-mau | MCP | 45p | MCP UI: add file → upload chậm → remove/replace ngay → check state qua snapshot  |
| `MB001` | Merging target defaults drops repeated query params | common | MCP navigate_page + evaluate_s | 20p | Tạo URL có 2 query param trùng key, navigate qua RedirectPreservingSearch, check |
| `MB003` | Detail drawer navigation drops list filters | common | MCP click + evaluate_script UR | 20p | Apply filter list KCH, click row mở drawer, back ra check filter còn giữ |
| `MB005` | Detail drawer endless skeleton on fetch error | common | MCP DevTools network block | 20p | Block API detail (network throttle/wrong ID), mở drawer, check có error state th |
| `MB007` | Unread count polling stops after transient error | common | MCP DevTools network | 30p | Login, throttle notification API gây 500 1 lần, check polling vẫn tiếp tục sau l |
| `MB009` | Clearing column sort never notifies parent | common | MCP click + list_network_reque | 20p | Mở table có sort, click toggle clear sort, check network request không còn param |
| `MB010` | Unread badge polling stops after transient error | common | MCP DevTools network | 30p | Dup #7 — throttle notification gây 500, badge polling phải resume |
| `MB018` | Chart bars show empty state during initial loading | common | MCP DevTools network throttle | 20p | Throttle dashboard API, mở dashboard, check chart hiện skeleton/loading thay vì  |
| `MB019` | Severe SLA tag does not render black tag | common | MCP evaluate_script CSS color | 20p | Seed/tạo record SLA severe (overdue), check tag màu đen render đúng |
| `MB034` | Clearing sort state not reported to parent | common | MCP click + list_network_reque | 20p | Dup #9 — Click clear sort, check network không còn sort param |
| `MB037` | PDF previews marked done even when no tab opens | common | MCP click + browser popup bloc | 30p | Block popup, preview PDF, check state preview không bị marked done khi tab fail |
| `MB039` | Page-size changes invoke onPaginationChange twice | common | MCP click + list_network_reque | 20p | Mở table, đổi page size, check chỉ 1 API call (không phải 2) |
| `MB047` | Malformed date props lock browser in infinite loop | common | MCP performance trace + wait | 30p | Tạo SLA record với malformed date, mở page check browser không freeze (timeout 1 |
| `MB066` | Bulk approve offered for rejected rows in pending tab | common | MCP click + take_snapshot | 20p | Mở mixed pending tab có rejected rows, select rejected, check button bulk approv |
| `MB072` | URL pagination applied to fetches not to table pager | common | MCP navigate + take_snapshot | 20p | Deep-link URL ?page=3, check table pager hiển thị page 3 (highlighted) |
| `MB084` | Rejected async action callbacks become unhandled promises | common | MCP click + list_console_messa | 20p | Click approve, BE reject, check console.error có handle (không unhandled promise |
| `MB109` | custom-multi controls not connected to form state | common | MCP click + list_network_reque | 20p | Mở SearchPanel có custom-multi, chọn value, submit check form payload có value |
| `MB110` | Count label drops zero counts not matching contract | common | MCP evaluate_script DOM text | 15p | Mở StateTabs có tab count=0, check label render '0' không bị drop |
| `MB114` | Whitespace-only rejection/supplement reasons pass | common | MCP fill + submit | 15p | Dup pattern — whitespace reason approval action, submit check reject |
| `MB119` | Count labels do not match StateTabs rendering contract | common | MCP evaluate_script DOM | 15p | Dup #110 — StateTabs count label render |
| `MB120` | Extension allow-list rejects valid files no MIME | common | MCP upload_file | 20p | Upload file .pdf với MIME bị omit (drag-drop), check upload accept (không reject |
| `MB137` | Bulk approve submits rejected rows from Chờ duyệt tab | common | MCP click + list_network_reque | 20p | Dup #66 — mixed pending tab có rejected, bulk approve check không submit rejecte |
| `MB165` | Rejected transition callbacks unhandled promise rejections | common | MCP click + list_console_messa | 20p | Dup #84 — click approve BE reject check no unhandled promise |
| `MB173` | Network failures rendered as empty catalog | common | MCP DevTools network block | 20p | Block API linh-vuc, mở select, check hiện error message thay vì empty catalog |
| `MC005` | Import validation can restore stale state after wizard close | common | MCP | 45p | MCP UI: trigger validation slow, close wizard, mở lại check stale state qua snap |
| `MC035` | Transition dialogs submit outside single-pending guard | common | MCP | 30p | MCP UI: double-click approve button nhanh, check network có 2 POST approve cùng  |
| `MS031` | Denied actions stay enabled when child passes disabled=false | common | MCP click + evaluate_script | 20 phút | Test PermissionAction với child Button disabled={false} + role denied, verify bu |
| `MB113` | TW-approved aggregation candidates rendered but not selectab | ct-htpldn | MCP click + take_snapshot | 20p | Mở tong-hop có TW-approved candidate, check checkbox enabled |
| `MB149` | January deadlines for current year skipped | ct-htpldn | MCP emulate clock + snapshot | 30p | Set system date Jan 15 2026, check DeadlineInfoBox hiện deadline Jan 2026 (không |
| `MD002` | Unsaved-change guard bypassed by SPA navigation | ct-htpldn | MCP click | S | Edit form CT-HTPLDN detail không save, MCP click sidebar link khác, verify dialo |
| `MD005` | Draft report edits submitted/overwritten without saving | ct-htpldn | MCP click | S | Edit Form21a draft cells, MCP click submit without save, verify cells revert hoặ |
| `MS019` | Draft action bar ignores update submit cancel permissions | ct-htpldn | MCP click + take_snapshot | 20 phút | Login role read CTDT, mở draft detail, verify action bar Update/Submit/Cancel có |
| `MS036` | Read-only detail route renders and submits edit form | ct-htpldn | MCP click + take_snapshot | 20 phút | Login role read CT-HTPLDN, mở detail, verify form edit có render và submit butto |
| `MB170` | Whitespace-only criterion names pass modal validation | danh-gia | MCP fill + submit | 15p | Mở AddTieuChi modal, nhập name='   ', submit check validation reject |
| `MS003` | Read-only users reach mutation controls detail route | danh-gia | MCP click + take_snapshot | 20 phút | Login role read-only danh-gia, navigate detail route, verify mutation buttons di |
| `MS022` | Batch delete exposed without CASL delete permission | danh-gia | MCP click + take_snapshot | 20 phút | Login role không có delete kế hoạch, verify batch delete button trên list page c |
| `MS023` | Attachment uploads ignore CASL update permission | danh-gia | MCP click + take_snapshot | 20 phút | Login role read kế hoạch, mở detail, verify attachment upload UI bị disabled the |
| `MB031` | Detail route captures DeXuat list URL as id | dao-tao | MCP navigate_page + URL check | 15p | Navigate /dao-tao/de-xuat (list URL), check không bị match route detail :id |
| `MB053` | Failed document uploads leave UI stuck disabled | dao-tao | MCP upload_file + take_snapsho | 20p | Upload file fail (size > limit), check upload UI re-enable không bị stuck |
| `MB082` | Imported attendance leaves cached results stale | dao-tao | MCP upload_file + take_snapsho | 30p | Import attendance Excel, check list/cache refetch (không stale) |
| `MB138` | Detail view omits saved plan content field | dao-tao | MCP take_snapshot + DOM | 20p | Tạo ke-hoach với plan content, mở detail view check field hiển thị |
| `MB158` | Attendance cannot be created for absent date | dao-tao | MCP click + DOM | 30p | Chọn date không trong returned records, click tạo điểm danh, check enabled không |
| `MC004` | Closing import dialog does not cancel in-flight state update | dao-tao | MCP | 45p | MCP UI: trigger import lớn rồi close dialog ngay, check state restore qua list_n |
| `MD009` | Removed attendance import file can still be submitted | dao-tao | MCP click + network | S | Upload diem-danh file rồi click X remove, MCP click Submit, verify file cũ vẫn đ |
| `MD018` | Random-config edits accepted in modal but never submitted | dao-tao | MCP + network | S | Open DeKiemTra form random-config modal, edit values, click OK, verify payload n |
| `MD021` | Attendance edits saved to wrong date after picker change | dao-tao | MCP + network | M | MCP open LichHoc tab, edit attendance, change date picker without save, click sa |
| `MD031` | Unsaved attendance and result edits overwritten by query ref | dao-tao | MCP click | M | MCP edit DiemDanh tab values, trigger query refetch (refocus tab/network event), |
| `MD038` | Budget field silently saves cleared or negative input as num | dao-tao | MCP + network | S | MCP input budget field cleared/negative, click save, verify payload có giá trị i |
| `MS029` | DeXuat tab protected by ChuongTrinh instead of DeXuat permis | dao-tao | MCP click + take_snapshot | 20 phút | Login role có ChuongTrinh nhưng không có DeXuat, verify tab DeXuat vẫn hiện do d |
| `MB025` | Legacy edit alias redirects to wrong doanh-nghiep id | doanh-nghiep | MCP navigate_page + URL check | 20p | Navigate /doanh-nghiep/:id/edit legacy alias, check redirect đến đúng id chứ khô |
| `MB060` | Optional-field clears omitted from update payloads | doanh-nghiep | MCP fill + list_network_reques | 20p | Edit doanh-nghiep, clear optional field, save check payload có field=null |
| `MB101` | Legacy edit alias drops business id during redirect | doanh-nghiep | MCP navigate + URL check | 20p | Dup #25 — legacy edit alias redirect check giữ id |
| `MB161` | Legacy edit alias drops enterprise id | doanh-nghiep | MCP navigate + URL | 20p | Dup #25 #101 — legacy edit alias redirect giữ enterprise id |
| `MS024` | Read-only doanh nghiệp route exposes write controls | doanh-nghiep | MCP click + take_snapshot | 20 phút | Login role read-only DN, verify trên list/detail có button Create/Edit/Delete hi |
| `MS037` | Read-only route renders edit-only doanh nghiệp form | doanh-nghiep | MCP click + take_snapshot | 20 phút | Login role read DN, navigate edit route, verify form render và submit có bị disa |
| `MB011` | Batch delete treats cancelled Hỏi đáp as eligible | hoi-dap | MCP click + take_snapshot | 20p | Filter hoi-dap cancelled, select all, check batch delete button bị disable hoặc  |
| `MB029` | Export drops selected complexity filter | hoi-dap | MCP click + list_network_reque | 15p | Filter hoi-dap by complexity, click Export, check request export có param comple |
| `MB091` | Assignment mode submit stale TVV as personal assignee | hoi-dap | MCP click + list_network_reque | 30p | Mở phan cong modal, chọn TVV, switch mode personal, check payload có account đún |
| `MB175` | Deep-linked filters displayed but not applied to query | hoi-dap | MCP navigate + list_network_re | 20p | Deep-link URL filter, check form hiện + API request có param filter |
| `MD033` | Saved draft responses render as blank form after query resol | hoi-dap | MCP click | S | MCP save draft response, navigate away rồi quay lại detail, verify form load dra |
| `MD039` | Edit save discards milestone edits cannot clear last payment | hop-dong | MCP click | M | MCP edit HopDong milestones và clear last payment, save, verify milestone edits  |
| `H007` | Default admin Secret@123 | other | MCP click | 15p | 🚨 Login admin/Secret@123 — nếu PASS = root compromise |
| `H008` | PermissionAction disabled={false} bypass | other | MCP evaluate_script | 30p | Click button denied vẫn fire — check network panel |
| `H018` | UpdateProfile bypass cap guard | other | MCP click + curl | 1h | 🚨 PUT donViId TW từ lower-cap account |
| `H020` | Route /:id render edit khi chỉ Read | other | MCP click + evaluate | 30p | Mở /ct-htpldn/{id} DU_THAO, nút Lưu hiện |
| `H021` | Giảng viên detail edit dù read-only | other | MCP click | 30p | Click tên GV → form edit hiển thị |
| `H037` | Hoàn tất chấm điểm mất edit | other | MCP click + evaluate | 30p | 🚨 Đổi điểm KHÔNG Lưu → Hoàn tất → input mất |
| `H039` | Form CT-HTPLDN giữ value cũ | other | MCP click | 30p | Detail A → SPA route B → Lưu, value của A persist |
| `H043` | submitResult ghi đè override điểm | other | MCP click + evaluate | 1h30 | Set override điểm → submit → check override discard |
| `H045` | Lưu quyền sai role sau navigate | other | MCP click | 30p | 🚨 /vai-tro/A → toggle → SPA nav B → Save lưu sai role |
| `H054` | FE thiếu nút start dot bao cao | other | MCP click | 15p | Tạo dot BC → check nút Start hiện |
| `H055` | Edit-mode fail fallback create | other | MCP click + evaluate | 1h | Mock getById fail → check POST thay vì show error |
| `H058` | TVV tạo thiếu thẻ hành nghề | other | MCP click + list_network | 1h | Mock upload thẻ fail → vẫn tạo TVV |
| `H074` | AntD notif thiếu message field | other | MCP click | 15p | 🚨 Cấu hình SLA → Lưu, toast field sai |
| `H085` | Duyệt TVV thiếu gate file thẻ | other | MCP click | 30p | 🚨 TVV không file thẻ → duyệt PASS sai |
| `H087` | API consumer thiếu scope inbound | other | MCP click | 15p | Form API consumer scope list missing |
| `MB055` | Batch approval selection survives filter/pagination | other | MCP click + list_network_reque | 30p | Select rows chi-tra, đổi filter/page, click batch approve check không submit hid |
| `MB063` | Status filter survives tab changes overrides selected tab | other | MCP click + URL check | 20p | Set status filter trên tab A, switch sang tab B, check status filter của tab A k |
| `MB068` | Selected rows survive filter changes batch approval hidden | other | MCP click + list_network_reque | 30p | Dup pattern #55 — select rows, đổi filter, batch approve check không submit hidd |
| `MB083` | Hoàn thành blocks legal-advice results >1000 chars | other | MCP fill + submit | 20p | Nhập legal advice >1000 chars, click Hoàn thành check submit OK (không bị block  |
| `MB087` | Payment amount parser lets NaN pass validation | other | MCP fill_form + submit | 15p | Nhập amount='abc' hoặc 'NaN', submit check form validation reject |
| `MB093` | Whitespace-only rejection reason pass client validation | other | MCP fill + submit | 15p | Nhập rejection reason='   ', submit check client validation reject |
| `MB103` | Status-changing mutations leave list/tab caches stale | other | MCP click + take_snapshot | 30p | Change status chi-tra detail, back ra list/tab check counts/rows update |
| `MB107` | Required reason fields accept blank whitespace | other | MCP fill + submit | 15p | Dup pattern #88 — reason='   ', submit check reject |
| `MB121` | Mandatory reason fields accept whitespace-only | other | MCP fill + submit | 15p | Dup #107 — reason whitespace check reject |
| `MB122` | Status tabs keep stale explicit status filter | other | MCP click + URL | 20p | Dup #63 — tab switch status filter stale check |
| `MB132` | Missing /hoi-dap/tao-moi alias falls into detail route | other | MCP navigate + URL/snapshot | 15p | Navigate /hoi-dap/tao-moi, check không bị match detail route (treat 'tao-moi' as |
| `MB152` | Create page preassigns consultant outside CG constraints | other | MCP click + DOM dropdown | 30p | Mở tao-moi tv-chuyen-sau với linh-vuc X, check consultant pre-select chỉ trong C |
| `MB157` | Approval defaults ignore thẩm định proposal amount | other | MCP take_snapshot + DOM | 20p | Mở approval form sau thẩm định, check số tiền default = đề xuất thẩm định (không |
| `MC029` | Edit modal opens in create mode while edit detail loading | other | MCP | 45p | MCP UI: click edit row → trước khi load xong, click create → modal state mix, ch |
| `MB016` | Toggle/delete mutations leave detail queries stale | qtht | MCP click + reload | 30p | Mở danh-muc detail, toggle status, navigate ra rồi vào lại check status mới (cac |
| `MB042` | Bulk account actions send empty/partial id list | qtht | MCP click + list_network_reque | 30p | Select bulk accounts, đổi pagination/filter, click bulk action check payload khô |
| `MB123` | Admin session management panel unreachable from account deta | qtht | MCP click + take_snapshot | 20p | Admin login, vào /quan-tri/tai-khoan/:id, check tab/section Sessions hiển thị |
| `MB133` | Optional fields cannot be cleared in edit mode | qtht | MCP fill + reload | 20p | Dup #12 — edit, clear optional field, save check persist null |
| `MB142` | Audit export downloads same blob twice | qtht | MCP click + DevTools download | 20p | Mở audit-log, click Export, check chỉ 1 file download (không phải 2) |
| `MB176` | URL pagination used for fetching not bound back to table | qtht | MCP navigate + DOM | 20p | Dup #72 — URL ?page=3, check pager highlight |
| `MC022` | Import wizard can reopen on canceled validation session | qtht | MCP | 45p | MCP UI: trigger validation, cancel, reopen modal, check session ID stale qua sna |
| `MS009` | Clearing key/cert omits PATCH leaves old credentials | qtht | MCP fill + list_network_reques | 20 phút | Open consumer modal, clear key field, submit PATCH, verify network request không |
| `MS035` | Edit and delete actions gated by create permission | qtht | MCP click + take_snapshot | 20 phút | Login role có create ngày lễ nhưng không update/delete, verify Edit/Delete butto |
| `MB013` | Whitespace approval/rejection fields pass validation | tu-van | MCP fill_form + take_snapshot | 15p | Mở modal phê duyệt hàng loạt, nhập 3 dấu cách vào reason, submit check validatio |
| `MB043` | Lưu nháp and Gửi KQ submit same request | tu-van | MCP click + list_network_reque | 20p | Click Lưu nháp vs Gửi KQ, so sánh payload + endpoint khác nhau |
| `MB048` | Search panel filters not fully applied to list/export | tu-van | MCP click + list_network_reque | 30p | Apply filter TVV, click Tìm rồi click Export, check 2 request đều có cùng filter |
| `MB076` | Rendered filters not propagated into list/export | tu-van | MCP click + list_network_reque | 30p | Dup #48 — apply filter TVV, click list/export, check param propagated |
| `MB088` | Whitespace-only reasons pass validation submitted | tu-van | MCP fill + submit | 15p | Mở modal cap nhat TT, nhập reason='   ', submit check validation reject |
| `MB108` | Trạng thái filter conflicts with tab-owned status | tu-van | MCP click + URL check | 20p | Apply status filter, switch tab, check tab status override filter cũ |
| `MB174` | Server-driven pagination not forwarded to table control | tu-van | MCP take_snapshot + DOM | 20p | API trả pagination meta page=3, check table pager highlight page 3 |
| `MD006` | Voided records remain editable and deletable | tu-van | MCP click | S | Set to-chuc record sang voided state, MCP open detail, verify Sửa/Xóa button hiể |
| `MD026` | Cancelled certificate removals persist and can be submitted | tu-van | MCP click | S | MCP open TabNangLuc, mark certificate remove, click Cancel modal, save form, ver |
| `MD032` | Canceled certificate deletions persist into later saves | tu-van | MCP click + network | S | MCP mark certificate delete, click Cancel, edit khác và save, verify cancelled d |
| `MS013` | Approval entrypoints enforce different permission predicates | tu-van | MCP click multiple buttons | 30 phút | Test các approval button trên detail page, verify mỗi entrypoint dùng cùng CASL  |
| `MS016` | Delete publish batch bypass CASL UI gating | tu-van | MCP click + take_snapshot | 20 phút | Login role không có delete permission, verify batch action bar Delete/Publish có |
| `MS025` | Batch publish exposed without publish permission check | tu-van | MCP click + take_snapshot | 20 phút | Login role không có publish TVV, verify batch publish button hiển thị/clickable  |
| `MS046` | Publish and delete mutations exposed without CASL gates | tu-van | MCP click + take_snapshot | 20 phút | Login role không có publish/delete TVV, verify row action publish/delete có hiển |
| `MB015` | Detail-page delete button rendered but inert | vu-viec | MCP click + list_network_reque | 15p | Vào vu-viec detail, click nút Xóa, check có gọi API delete hoặc confirm modal |
| `MB020` | Filtered timeline empty state before all events loaded | vu-viec | MCP click + DevTools network | 30p | Mở vu-viec detail có nhiều event, apply filter, throttle network check không hiệ |
| `MB089` | Bulk delete bypasses same state guard as row delete | vu-viec | MCP click + take_snapshot | 20p | Select vu-viec có state không cho phép xóa, click bulk delete check bị reject (g |
| `MS034` | DN self-submit permission opens staff-only manual intake | vu-viec | MCP click + navigate | 25 phút | Login role DN có self-submit, verify route manual intake (staff-only) có accessi |

**Subtotal:** 148 bug, ~64.8h serial

---

## 6. Phase 2 — QA-API bugs (Agent E)

**Tổng:** 81 bug (26 HIGH + 55 Medium). Verify qua curl + jq. Agent E owns full Phase 2.

| Bug ID | Title | Module | Tool | Effort | Verify approach |
|---|---|---|---|--:|---|
| `MB177` | Completed-training trend reports annual as monthly | bao-cao | curl + math verify | 30p | curl GET trend báo cáo annual, check buckets là yearly (không phải monthly) |
| `MB059` | Publish/unpublish idempotency cache not scoped to folder | bieu-mau | curl + idempotency-key header | 30p | curl publish folder A 2 lần với cùng idempotency key, sau đó publish folder B, c |
| `MB115` | Public FTS queries are accent-sensitive | bieu-mau | curl 2 query + diff | 20p | curl GET search 'thư mục' và 'thu muc', check trả về cùng kết quả (accent-insens |
| `MB049` | Template lookup cannot filter by template type | common | curl | 15p | curl GET mau-phan-hoi với query loaiMau, check kết quả filtered đúng type |
| `MB071` | Invalid ISO timestamps normalized instead of rejected | common | curl | 15p | curl với date='2024-13-45T99:99:99', check 400 reject thay vì normalize |
| `MD041` | Audit logs lose entityId for valid data-meta create response | common | curl + DB | S | POST create endpoint returning {data, meta} shape, query audit_log verify entity |
| `MB046` | Standalone reporting periods created but not listable | ct-htpldn | curl POST + GET | 20p | curl POST tạo dot-bao-cao standalone, curl GET list check thấy record |
| `MB102` | laCongBo=false coerced to true during DTO transform | ct-htpldn | curl | 15p | curl GET chuong-trinh-htpl?laCongBo=false, check response chỉ laCongBo=false |
| `MB148` | Manual audit inserts not suppressed, endpoints double-log | ct-htpldn | curl + psql | 30p | curl POST bao-cao-ct-htpl, query audit_log DB check chỉ 1 entry (không double) |
| `MS021` | Export endpoint checks read instead of export permission | ct-htpldn | curl + role không export | 20 phút | Login role có read CT-HTPLDN nhưng không có export, curl export endpoint, verify |
| `MD016` | Feedback sanitizer deletes non-HTML angle bracket content | danh-gia | curl | S | POST danh-gia-tvv với content chứa <example> hoặc 3 < 5, verify response preserv |
| `MD020` | Selecting cases not idempotent duplicates ket_qua rows | danh-gia | curl + DB | S | POST select cases endpoint cùng payload 2 lần liên tiếp, GET ket_qua_danh_gia ro |
| `MB006` | UpdateDeKiemTraDto allows invalid exam shape | dao-tao | curl | 20p | curl PATCH de-kiem-tra với payload exam shape invalid (missing required nested), |
| `MB086` | Attendance import skip recompute for valid rows | dao-tao | curl + DB query | 30p | curl import attendance batch có 1 row invalid, check valid rows vẫn được recompu |
| `MB104` | Registration close date rejects same-day range valid | dao-tao | curl | 15p | curl POST khoa-hoc với ngayMo=ngayDong same day, check 201 OK (DTO doc nói valid |
| `MB112` | Bài giảng list duplicates rows for multi-lĩnh-vực records | dao-tao | curl + seed | 30p | Seed bài giảng với 3 linhVuc, curl GET list check 1 row (không phải 3) |
| `MB164` | Create DTOs accept negative size and duration | dao-tao | curl | 15p | curl POST bai-giang size=-1 duration=-10, check 400 reject negative |
| `MB167` | KetQua Excel import does not transition to DA_NHAP | dao-tao | curl + psql | 30p | curl import Excel ket-qua, psql query check rows status=DA_NHAP |
| `MC014` | Optimistic-lock check not atomic with the update | dao-tao | curl xargs | 1h | curl parallel 2 PATCH cùng version=N của câu hỏi, xargs -P2 retry 20, expect 1 t |
| `MD036` | Attendance Excel round-trip loses VANG_PHEP state | dao-tao | Export + import API | M | Set diem_danh records VANG_PHEP, export Excel, re-import file, verify state VANG |
| `MS015` | Upload type validation accepts mismatched spoofed types | dao-tao | curl multipart upload | 30 phút | Curl upload với file .exe rename .pdf, verify pipe magic-byte check hay chỉ exte |
| `MS042` | Test distribution persists arbitrary lesson IDs without vali | dao-tao | curl + invalid lessonId | 25 phút | Curl create đề kiểm tra với lesson_id không thuộc khóa học, verify validation re |
| `MB163` | Lowering total employees bypasses subcount validation | doanh-nghiep | curl | 20p | curl PATCH doanh-nghiep giảm totalEmployees < sum subcount, check 400 reject |
| `MS002` | Enterprise registration fake CAPTCHA token | doanh-nghiep | MCP list_network_requests + cu | 20 phút | Inspect network request đăng ký DN, verify CAPTCHA token là hard-coded fake stri |
| `MB044` | Batch DTOs allow duplicate IDs | hoi-dap | curl | 15p | curl batch cong-khai với ids [1,1,2,2], check 400 validation reject duplicate |
| `MB065` | Hoi dap period aggregation buckets different date | hoi-dap | curl + DB compare | 1h | curl báo cáo hoi-dap với filter period, check aggregation dùng cùng date express |
| `MB074` | Processed congKhai=false query coerced to true | hoi-dap | curl | 15p | curl GET hoi-dap?congKhai=false, check response chỉ trả congKhai=false rows |
| `MB169` | String false can submit a draft response | hoi-dap | curl | 15p | curl PATCH phan-hoi với isDraft='false' (string), check coerce đúng boolean fals |
| `MD011` | CreatePhanHoiDto accepts attachment IDs not consumed downstr | hoi-dap | curl | S | POST /api/v1/phan-hoi với attachment IDs, verify response success rồi GET phan-h |
| `H001` | TVV đọc lịch sử VV khác | other | curl | 30p | GET /vu-viecs/:id/lich-su id không gán cho tvv |
| `H006` | Client assertion exp missing | other | curl | 1h | Sign JWT không exp claim, POST /token |
| `H010` | File mutation sau DA_THANH_TOAN | other | curl | 30p | POST attach file vào HSCT đã đóng thanh toán |
| `H011` | X-Forwarded-For spoof IP whitelist | other | curl | 30p | curl header X-Forwarded-For spoof IP whitelist |
| `H012` | String 'false' qua @Equals(true) | other | curl | 15p | POST dongYDieuKhoan:'false' (string) thay vì false |
| `H013` | Download file thiếu check BieuMau | other | curl | 30p | GET /bieu-maus/files/{otherFid}/download cross |
| `H022` | Captcha hard-coded mock-captcha | other | MCP list_network | 15p | 🚨 POST đăng ký body có captchaToken:'mock-captcha' |
| `H026` | Create PQDL bypass same-cap | other | curl | 1h | POST 2 lần cùng vaiTroId, 2 DP khác |
| `H028` | System role bị edit/toggle qua PATCH | other | curl | 30p | 🚨 PATCH /vai-tro/{systemId} với role có update_vai_tro |
| `H030` | TVV file delete bypass CB_NV policy | other | curl | 30p | DELETE /tu-van-viens/:id/files/:fid role non-CBNV |
| `H032` | TuLieuPhapLyVv link parent cross-tenant | other | curl | 30p | POST với noiDungTvId tenant B |
| `H034` | fileDinhKemIds re-parent file người khác | other | curl | 30p | PATCH HoiDap A với fileId của B |
| `H036` | Tổng hợp BC lan sibling dot | other | curl + API GET | 2h+ | Tạo 2 dot DA_GUI_TW cùng ct |
| `H040` | trongSo 'abc' lưu được | other | curl | 15p | POST DM trongSo:'abc' (string thay vì number) |
| `H047` | Batch upsert tiêu chí xóa nhầm | other | curl | 30p | PUT tieu-chi với id giả → xóa nhầm record khác |
| `H049` | congKhai publish trước validate | other | curl + MCP | 1h | File attach lỗi → publish vẫn pass |
| `H052` | Batch duyệt bypass BR-CALC-01 | other | curl | 30p | 🚨 batchPheDuyet mismatch NHO+90% gây sai tiền chi trả |
| `H053` | File VV duongDanFile = ID sai | other | curl | 30p | Upload → GET hồ sơ → download 404 |
| `H059` | Public TVV list/search rỗng | other | curl | 15p | 🚨 GET /public/tu-van-vien empty list |
| `H060` | batchCongKhai publish chưa duyệt | other | curl | 30p | hoi-dap chưa DA_DUYET → batch publish pass |
| `H063` | Overbook khóa học | other | curl parallel xargs -P | 1h-2h+ | 🚨 curl 2 POST inbound song song khóa soLuongToiDa=1 |
| `H066` | Optimistic lock DanhMuc | other | curl parallel | 30p | 🚨 2 PATCH version=1 song song |
| `H067` | Optimistic lock VaiTro | other | curl parallel | 30p | 🚨 2 PATCH /vai-tro version=1 |
| `H068` | Optimistic lock DonVi | other | curl parallel | 30p | 2 PATCH /don-vi version=1 |
| `H069` | Optimistic lock HopDongTV | other | curl parallel | 30p | 2 PATCH /hop-dong-tu-vans |
| `H086` | Lưu nháp CTDT gọi PUT sai | other | MCP list_network | 15p | 🚨 CTDT nháp → Lưu → 405/404 method |
| `MB027` | Required text fields accept whitespace-only | other | curl | 15p | curl PATCH NHT trạng thái với reason = '   ', check 400 validation reject |
| `MB061` | Copying Feb 29 to non-leap year creates March 1 | other | curl | 20p | curl copy ngay-le 2024-02-29 sang 2025, check trả về 2025-02-28 (last day Feb) h |
| `MB070` | Training KPI cache ignores requested period | other | curl 2 lần + diff | 30p | curl dashboard period A → cache; curl period B với cùng key, check trả khác data |
| `MB156` | Missing hoSoJson bypasses DVC intake validation | other | curl | 15p | curl POST tiep-nhan-dvc no hoSoJson, check 400 validation reject |
| `MB168` | Tab counts ignore doanhNghiepId filter used by list | other | curl 2 endpoint + diff | 30p | curl GET chi-tra tab counts với doanhNghiepId=X, check counts khớp list filtered |
| `MD022` | Import validation silently truncates overlong text | other | curl + DB | S | Import ngay-le Excel với text >255 chars, verify response báo error hay silent t |
| `MS008` | Unvalidated sortBy interpolated ORDER BY | other | curl + payload injection | 20 phút | Curl notification list endpoint với sortBy=invalid_column hoặc SQL injection pay |
| `MS033` | Consumer expiry accepted by DTO not persisted/enforced | other | curl + DBA query check | 45 phút | Curl tạo API consumer với expiry, verify field persist DB + endpoint enforce exp |
| `MC027` | Profile optimistic locking is non-atomic pre-check | qtht | curl xargs | 1h | curl parallel 2 PATCH profile cùng version=N, xargs -P2 retry 20, expect 1 win 1 |
| `MB038` | TVCS update can bypass expert-field compatibility | tu-van | curl | 30p | curl PATCH TVCS với expert có linhVuc không khớp, check 400 reject |
| `MB067` | Video session link validation permits unusable values | tu-van | curl | 15p | curl POST phien-tu-van link='javascript:' hoặc 'ftp://...', check 400 reject |
| `MB075` | Blank quick-consultation answers pass validation | tu-van | curl | 15p | curl POST tra-loi tvn answer='', check 400 validation reject |
| `MB081` | Contract value can be lowered below scheduled payments | tu-van | curl + seed payments | 30p | curl PATCH hop-dong giảm giá trị < tổng payment scheduled, check 400 reject |
| `MB147` | hieuLuc=false query coerced to true | tu-van | curl | 15p | Dup pattern — curl GET kho-cau-hoi?hieuLuc=false check chỉ hieuLuc=false rows |
| `MB172` | PhienTuVan create sends notif to tu_van_vien id wrong | tu-van | curl + psql | 30p | curl POST phien-tu-van, psql query notification check recipient_id = tai_khoan i |
| `MC006` | Version checks not atomic, concurrent updates overwrite | tu-van | curl xargs | 1h | curl parallel 2 PATCH cùng version=N, xargs -P2 retry 20 lần, expect 1 thành côn |
| `MD001` | Trao-doi attachment link failures silently swallowed | tu-van | curl + DB query | M | Upload trao-doi với invalid attachment ID, curl POST /api/v1/lich-su-trao-doi, v |
| `MD024` | Profile file relinking writes entity_type values unused down | tu-van | curl + DB | M | PATCH tu-van-vien profile với file relink, GET sub-endpoint files verify entity_ |
| `MS017` | Cong-khai file preview accepts orphan file IDs | tu-van | curl + orphan fileId | 25 phút | Curl preview endpoint với fileId không thuộc TVV nào, verify 404/403 hay trả con |
| `MS026` | KhoCauHoi import size limit enforced after upload | tu-van | curl + large file | 30 phút | Curl upload kho câu hỏi với file >limit, verify reject trước buffer hay sau (mem |
| `MS027` | Export bypasses accordion-only context gating | tu-van | curl direct endpoint | 25 phút | Curl export hợp đồng TV ngoài context accordion (không qua UI guard), verify acc |
| `MS040` | TCTV publish sends before sanitizing public description | tu-van | curl + XSS payload | 30 phút | Curl publish TCTV với public_description chứa XSS payload, verify sanitize trước |
| `MB054` | Required free-text reasons accept whitespace | vu-viec | curl | 15p | curl POST gui-thong-bao reason='   ', check 400 reject |
| `MB085` | Phân tích vụ việc totals include non-counted statuses | vu-viec | curl + math verify | 30p | curl báo cáo phân tích vụ việc, check tổng = sum của visible buckets (không có h |
| `MB139` | Checklist length check allows duplicate items | vu-viec | curl | 15p | curl POST kiem-tra vu-viec với checklist ['A','A','B'], check 400 reject duplica |
| `MD015` | Batch approvals do not create per-case timeline audit rows | vu-viec | curl + DB | M | Batch approve nhiều vu-viec qua POST endpoint, GET timeline mỗi case verify có a |

**Subtotal:** 81 bug, ~41.2h serial

---

## 7. Phase 3 — QA-cross-role/tenant (Agent D)

**Tổng:** 21 bug (7 HIGH + 14 Medium). Cần 2+ account khác role/tenant. Verify song song qua MCP isolatedContext + curl.

| Bug ID | Title | Module | Tool | Effort | Verify approach |
|---|---|---|---|--:|---|
| `MB008` | denyRoles over-blocks multi-role users | common | MCP 2 tab role + cookies | 1h | Login multi-role user (có role bị deny + role được allow), check route được phép |
| `MB035` | Self-loop fallback denied immediately by role guards | common | MCP role + navigate | 1h | Login user bị deny, trigger fallback route, check không bị loop denied |
| `MS011` | CTDT creation validates parent via unscoped raw query | ct-htpldn | curl + 2 tenant account | 30 phút | Test 2 tenant, tenant A tạo CTDT reference parent của tenant B qua API, verify a |
| `MS028` | Resume omits cross-unit guard used by pause | ct-htpldn | curl + 2 unit account | 30 phút | Test 2 đơn vị, đơn vị A tạo CT pause, đơn vị B gọi resume endpoint, verify cross |
| `MS039` | Rating list bypasses parent TVV tenant check | danh-gia | curl + 2 tenant account | 30 phút | Test 2 tenant TVV, tenant A query rating list TVV của tenant B, verify response  |
| `MB026` | Training module denies tab-only permission users | dao-tao | MCP 2 role + cookies | 1h | Login user chỉ có permission cho subfeature tab dao-tao, check vào được module |
| `MB064` | DeKiemTra detail permits users denied from list | dao-tao | MCP 2 role + navigate | 30p | Login user bị deny list de-kiem-tra, navigate direct URL detail, check bị deny |
| `MB166` | Create-only GiangVien blocked by parent route guard | dao-tao | MCP role + navigate | 30p | Login GiangVien create-only, navigate /dao-tao/tao-moi, check không bị deny pare |
| `MS001` | Course CTDT validation unscoped weaker on update | dao-tao | curl + 2 account khác tenant | 30 phút | Test 2 tenant tạo CTDT cùng mã, verify update endpoint không enforce tenant scop |
| `H004` | BaiGiang/DeKiemTra list cross-tenant | other | curl + API GET | 1h-2h+ | GET /bai-giangs cross tenant, đếm row tenant khác |
| `H016` | Phan-cong list bypass tenant | other | curl | 1h | GET /phan-cong-danh-gia keHoachId cross |
| `H019` | Export NHCH leak cross-tenant | other | MCP + curl | 1h30-2h | Export Excel đếm row đơn vị khác |
| `H029` | TCTV list/export bypass tenant filter | other | MCP + curl | 1h | 🚨 List TCTV không truyền donViId |
| `H031` | Đào tạo list/export bypass RLS | other | MCP + curl | 2h+ | List GiangVien/DeXuat/DiemDanh cross |
| `H035` | goi-y ghi đè TuVanNhanh khác donVi | other | curl | 30p | GET /tu-van-nhanhs/{B-id}/goi-y từ A |
| `H062` | maChuongTrinh collision tenant | other | curl parallel | 1h | 2 đơn vị tạo CT cùng ngày, mã trùng |
| `MB100` | Existing answer hidden in CB_TRA_LOI detail mode | other | MCP role + take_snapshot | 30p | Login CB_TRA_LOI role, mở tv-nhanh detail có answer cũ, check answer hiện |
| `MB153` | Direct URLs bypass danh-muc tab allowlist | qtht | MCP role + navigate | 30p | Login user không có permission tab X, navigate direct URL /danh-muc/X, check bị  |
| `MB036` | TVV owners cannot edit own capability tab | tu-van | MCP role TVV + take_snapshot | 30p | Login TVV owner, vào chi-tiet TabNangLuc, check button Sửa enabled |
| `MB117` | Owner editing of Năng lực tab broken from detail | tu-van | MCP role TVV | 30p | Dup #36 — TVV owner edit NangLuc tab, check enabled |
| `MS006` | History statistics ignore own-history authorization filter | tu-van | curl + 2 TVV account | 30 phút | Test 2 TVV khác, gọi statistics endpoint verify TVV-A thấy history TVV-B (bypass |

**Subtotal:** 21 bug, ~18.0h serial

---

## 8. Phase 4a — Partial-QA (Agent F)

**Tổng:** 17 bug (4 HIGH + 13 Medium). Cần DBA seed state đặc biệt hoặc API consumer trước, sau đó QA verify. Sequential dependency với A0.4 (DBA inject + API consumer setup).

| Bug ID | Title | Module | Tool | Effort | Verify approach |
|---|---|---|---|--:|---|
| `MB023` | VNeID logins drop session IP and user-agent | auth | DBA query + VNeID mock | 1h | Login qua VNeID mock, query DB session check IP + UA columns không null |
| `MS020` | Email activation treats inactive role mappings as provisioni | auth | DBA seed + curl activation | 1 giờ | DBA seed user với role mapping is_active=false, gọi email activation, verify rol |
| `MB127` | Subtable hides biểu mẫu after first page | bieu-mau | DBA seed + MCP | 30p | Seed >10 bieu-mau trong subtable, check pagination hoạt động (page 2 hiện) |
| `MB069` | Virus scan status stuck after backend marks clean | common | MCP upload + BE webhook | 1h | Upload file, BE update scan status clean, poll UI check status update. Cần backe |
| `MS038` | Virus scan terminal states not reliably applied | common | DBA seed + MCP snapshot | 45 phút | DBA seed file với virus_scan_status INFECTED/QUARANTINED, verify FileUpload UI r |
| `MB017` | Lecture assignment modal builds options from partial pages | dao-tao | DBA seed + MCP click | 1h | Seed >20 bài giảng để có pagination, mở modal assign, check option list đủ tất c |
| `MB090` | Detail child tables truncate after first 100 rows | doanh-nghiep | DBA seed + MCP | 1h | Seed >100 ho-so chi-tra cho doanh-nghiep, mở detail tab, check pagination/scroll |
| `MB092` | Company code generation collides after hard deletes | doanh-nghiep | DBA DELETE + curl POST | 1h | DBA hard delete doanh-nghiep với code mới nhất, curl POST tạo mới check không co |
| `H002` | Attach file cross-tenant qua DVC | other | curl | 1h30-2h+ | POST intake fileDinhKemIds tenant khác (cần DVC token + seed file) |
| `H009` | Pending account hết hạn vẫn active | other | curl + DBA seed | 2h+ | Cần DBA seed ngayTao cũ rồi thử login active |
| `H023` | Cache report ignore allowedDonViIds | other | curl + MCP | 2h+ | Seed PQDL qua admin UI, tránh cache cũ bằng unique filter |
| `H024` | Cache report scope leak HoiDap/CT | other | curl + MCP | 2h+ | Tương tự #23, unique filter mỗi run |
| `MD025` | Audit log export silently truncates at 10000 rows | other | DBA seed + curl | M | DBA seed >10k audit log rows, GET export endpoint, verify response có cảnh báo t |
| `MD003` | Changing parent unit cap corrupts child hierarchy | qtht | curl + DB | M | Seed don-vi hierarchy đa cấp, PATCH parent cap qua curl, verify children tree cò |
| `MB041` | Lexicographic MAX breaks after sequence 9999 | tu-van | DBA seed + curl POST | 1h | Seed DB tu_van với mã ending 9999, tạo record mới, check mã tiếp theo = 10000 kh |
| `MB118` | KhoCauHoi code generation reuses codes after hard delete | tu-van | DBA DELETE + curl POST | 1h | DBA hard delete KCH code mới nhất, curl POST tạo check không reuse code |
| `MS007` | Virus-flagged documents expose download action | vu-viec | DBA seed + MCP take_snapshot | 45 phút | Cần seed file với virus_scan_status=INFECTED, verify UI vẫn render download butt |

**Subtotal:** 17 bug, ~18.0h serial

---

## 9. Phase 4b — QA-API best-effort (Agent F)

**Tổng:** 16 bug (3 HIGH + 13 Medium). Race condition window 100-500ms — verify qua curl parallel (xargs -P) + retry 20-50 lần. Best-effort: nếu race không repro stable sau 50 retry → escalate Dev integration test.

| Bug ID | Title | Module | Tool | Effort | Verify approach |
|---|---|---|---|--:|---|
| `MC011` | OTP verification non-atomic Redis get/set/delete | auth | curl xargs | 1.5h | curl parallel 2 POST verify-otp cùng code, race Redis get/del, retry 50 lần expe |
| `MC031` | Import confirmation processed twice (session not atomic) | bieu-mau | curl xargs | 1h | curl parallel 2 POST confirm-import cùng sessionId, xargs -P2 retry 30, expect 1 |
| `MC024` | HSPL code generation lock ends before insert | common | curl xargs | 1h | curl parallel POST 5 HSPL qua public API xargs -P5, retry 20 round, check duplic |
| `MC036` | maNht generation races concurrent creates | common | curl xargs | 1h | curl parallel POST 5 NHT đồng thời xargs -P5, retry 20 round, check duplicate ma |
| `MC013` | Concurrent registration approvals increment enrollment twice | dao-tao | curl xargs | 1h | curl parallel 2 POST approve cùng dangKyId, xargs -P2 retry 30, check enrollment |
| `MC017` | GiangVien code generation races under concurrent creates | dao-tao | curl xargs | 1h | curl parallel POST 5 giảng viên đồng thời xargs -P5, retry 20, check duplicate m |
| `MC028` | Course code generation races under concurrent creates | dao-tao | curl xargs | 1h | curl parallel POST 5 khóa học đồng thời xargs -P5, retry 20 round, check duplica |
| `H038` | Race delete HĐ-TV vs link VV | other | curl parallel + retry | 2h+ | curl 2 thread DELETE + POST link, repeat 20-50 lần |
| `H065` | Mã HoiDap trùng cross-tenant | other | curl parallel | 1h30+ | curl POST hoi-dap 2 tenant cùng ngày retry 20+ |
| `H070` | Payment validate state stale | other | curl parallel/retry | 2h+ | curl PATCH cùng version repeat — không cần load infra |
| `MC037` | linkFilesToEntity overwrites associations in concurrent requ | other | curl xargs | 1h | curl parallel 2 POST linkFiles cùng entityId fileIds khác nhau, xargs -P2 retry  |
| `MC038` | Batch replacement not serialized per role | other | curl xargs | 1h | curl parallel 2 PUT batch-replace cùng roleId, xargs -P2 retry 20, check 2 set p |
| `MC002` | Concurrent activation resends email invalid temp passwords | qtht | curl xargs | 1h | curl parallel 2 POST resend-activation cùng userId, xargs -P2 retry 30 lần, chec |
| `MC010` | TVCS unpublish has no state or optimistic-lock guard | tu-van | curl xargs | 1h | curl parallel 2 POST unpublish cùng tvcsId, xargs -P2 retry 30 lần, expect 1 suc |
| `MC016` | maTvv generation races on MAX(seq)+1 | tu-van | curl xargs | 1h | curl parallel POST 5 TVV đồng thời xargs -P5, retry 20 round, check duplicate ma |
| `MC012` | Case code allocation duplicates under concurrent creates | vu-viec | curl xargs | 1h | curl parallel POST 5 vụ việc đồng thời xargs -P5, retry 20 round, check trả về d |

**Subtotal:** 16 bug, ~19.0h serial

---

## 10. Acceptance template cho mỗi bug (xem todo file)

Mỗi task ⏳ → ✅/❌ phải có:

1. **Screenshot evidence inline base64** (rule project) → `bug-reports/<category>/image/r8-<bug>-*.png`
2. **Bug-report file 6 sections** (Mô tả/Bước/KQ mong đợi/KQ thực tế/Bằng chứng/So sánh) — chỉ tạo nếu confirmed FAIL
3. **SRS verify 3-step** (CLAUDE.md): version check + line quote + verify alternate method
4. **Wording describe requirement** — KHÔNG prescribe button label/endpoint/error code
5. **Network panel evidence** (`list_network_requests`) khi bug API-related
6. **Update verify-progress.md** ngay sau task done (≤5p)
7. **Claim record lock** (`record-locks.md`) trước mutate, release sau verify

---

## 11. Out-of-scope (106 bug → escalate team khác)

- **Dev-needed (63):** code-review, RLS context, integration test cron/job, queue concurrency injection, JWT/OAuth flow.
- **DBA-needed (31):** psql query RLS/GUC, migration up/down, schema CHECK constraint, FORCE RLS, audit table.
- **DevOps-needed (10):** CI build TypeScript, partition migration, load test k6, mTLS sandbox config.
- **SKIP (2):** A11y cosmetic dropdown mouse-only.

Reference: bug list per team trong `all-bugs-classified.json` field `high_non_qa` + `medium_non_qa`.

---

## 12. Tóm tắt

**283 bug QA verify được** (55 HIGH + 228 Medium). Split 6 agent (A setup, B auth UI, C workflow UI, D cross-role, E API, F Partial+race). 3 sprint ~110h serial = ~26-36h wall-time với 6 agent parallel. Phase 0 ~12h sequential setup (folder + role + seed + SRS map + API consumer + record-locks).

Việc tiếp theo: codex review plan + todo → user approve → start P0.
