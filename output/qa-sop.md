# QA SOP — PM Hỗ trợ Pháp lý Doanh nghiệp (PM HTPLDN)

> **Mục đích:** Tài liệu quy trình chuẩn cho QA tester làm việc trong project này. Áp dụng cho **mọi tester** — hiện tại + tương lai. Đọc file này TRƯỚC khi bắt đầu round QA mới.
>
> **Phạm vi:** 8 quy trình QA chính + phương pháp xử lý chất lượng cho từng quy trình.
>
> **Nguồn gốc:** Đúc kết từ 20 round QA (R1 → R20) trong giai đoạn 2026-04-15 → 2026-05-13. Đã chứng kiến 5/9 bug Open có vấn đề do dùng SRS cũ + quote sai mã (deep-verify 2026-05-13).
>
> **Ngôn ngữ:** Tiếng Việt thường, câu ngắn, ít jargon. Nếu phải dùng từ tiếng Anh (Open/Closed/PASS/FAIL...) thì để nguyên — đã quen trong team.

---

## Mục lục

| # | Quy trình | Mục tiêu 1 câu |
|:-:|---|---|
| 1 | [Lập kế hoạch test](#1--lập-kế-hoạch-test-test-planning) | Quyết định test cái gì, không test cái gì, ngưỡng PASS là gì |
| 2 | [Chuẩn bị test data (seed)](#2--chuẩn-bị-test-data-seed) | Tạo đủ data tiền điều kiện để TC chạy được |
| 3 | [Thực thi test](#3--thực-thi-test-test-execution) | Chạy TC, ghi nhận kết quả, phân loại block đúng nguyên nhân |
| 4 | [Log bug](#4--log-bug-bug-logging) | Ghi bug đúng, đủ bằng chứng, đúng spec ref |
| 5 | [Verify bug đã fix (re-test)](#5--verify-bug-đã-fix-bug-verification) | Xác nhận dev fix thật sự đóng bug, không tin chay claim |
| 6 | [Verify spec + escalate BA](#6--verify-spec--escalate-ba) | Đảm bảo bug/test reference đúng SRS version, không suy luận |
| 7 | [Đóng round + báo cáo](#7--đóng-round--báo-cáo) | Kết round có 2 bảng tổng + handoff rõ |
| 8 | [Quản lý regression](#8--quản-lý-regression) | Bug đóng rồi mở lại + bug tái phát cross-module |

**Phụ lục:**
- A — [Checklist 30s trước mọi action](#phụ-lục-a--checklist-30s-trước-mọi-action)
- B — [6 nhóm nguyên nhân TC block (A-F)](#phụ-lục-b--6-nhóm-nguyên-nhân-tc-block)
- C — [Reference card: tool mapping MCP](#phụ-lục-c--tool-mapping-mcp-quick-ref)

---

## Nguyên tắc nền tảng — đọc TRƯỚC khi đi vào từng quy trình

**5 nguyên tắc bất biến.** Vi phạm = lặp lại bài học cũ.

1. **Spec là sự thật, không phải dev claim hay trí nhớ.** Mỗi bug/test/closure phải có quote SRS line — không quote không log, không quote không đóng.

2. **State (data thực) là sự thật, không phải task icon ✅.** Trước khi flip task ⏳→🟢 dep upstream, chạy verify query thật. Trust state, not task icon.

3. **UI là kênh test mặc định, API là evidence phụ.** Mọi seed/workflow/permission test phải UI click chain qua Chrome DevTools MCP. API `list_network_requests` chỉ để verify response, KHÔNG dùng API direct POST để pass nhanh.

4. **Bug describe requirement, không prescribe implementation.** Viết "Khi A xảy ra, phải hiển thị X theo SRS line N" — KHÔNG viết "Phải có button Y" hoặc "Phải gọi endpoint Z với mã ERR-X".

5. **SRS mới đè SRS cũ.** Project có 2 version: `input/srs-v3/` (cũ) + `input/srs-update-2026-5-5/` (v3.5, latest). Mọi bug/test mới phải dùng v3.5. Nếu không thấy module trong v3.5 → đọc CHANGELOG-v3-to-v3.5.md kiểm tra có deprecate không.

---

## 1 — Lập kế hoạch test (Test Planning)

### 1.1 Mục tiêu

Xác định **test cái gì** (scope), **không test cái gì** (out-of-scope), **bao nhiêu là đủ** (ngưỡng PASS), và **làm thế nào** (method per TC). Không có plan = test ad-hoc = miss coverage.

### 1.2 Input bắt buộc

| Input | Vị trí | Vì sao cần |
|---|---|---|
| SRS module | `input/srs-update-2026-5-5/srs-fr-NN-*.md` | Source of truth cho UC + AC + state machine + error code |
| CHANGELOG v3→v3.5 | `input/srs-update-2026-5-5/CHANGELOG-v3-to-v3.5.md` | Biết module nào đổi state machine, đổi enum, deprecate |
| Permission matrix | `output/permission-matrix.md` | Biết role nào CRUD-able trên entity nào |
| Entity map | `input/data/entity-map.md` | Biết entity "tạo tại" module nào, "đọc tại" module nào |
| State snapshot | `tasks/state-snapshot.md` | Biết hiện tại có bao nhiêu data ở state nào |
| Test plan template | `output/template/test-plan-overview-template.md` | Khung viết plan |

### 1.3 Output

1 file `output/funtion/<module>/test-plan-<module>.md` chứa:
- Danh sách TC × ID × tên × method × precondition × expected × priority
- Bảng "Out-of-scope" — TC không test round này + lý do
- Bảng "Dependency" — TC nào cần data/setup từ module khác

### 1.4 Phương pháp chất lượng (8 bước)

**B1. Phân loại module theo SRS update batch.** Khi BA gửi SRS update, KHÔNG test lại toàn bộ. Phân 4 nhóm (xem CLAUDE.md global rule 4):

| Nhóm | Trigger | Cách test |
|:-:|---|---|
| **A** FULL | Module có file SRS update + Δ >50% | Test lại HẾT như chưa từng test |
| **B** DELTA+IMPACT | Module bị refactor data/API/schema lan từ A | Test phần thay đổi đầy đủ + sample happy path |
| **C** IMPACT only | Module chỉ đọc data thay đổi (KPI, dropdown) | Sample 2-3 màn hình đại diện |
| **D** SKIP | Không liên quan | Smoke 5 phút verify login + render OK |

**Dùng `Agent` với `subagent_type=general-purpose`** để grep cross-reference TRƯỚC khi phân nhóm. `Explore` (read-only nông) sẽ MISS impact cross-module.

**B2. Đọc SRS module CỤ THỂ + state machine TRƯỚC khi list TC.**
- Mở `input/srs-update-2026-5-5/srs-fr-NN-*.md` đọc §UC + §State machine + §Inputs + §Outputs + §Error codes.
- Đối chiếu với `input/data/state-machines-v3.5.md` (reference card) — biết module này có bao nhiêu state, transition nào hợp lệ.
- **CẤM bịa state từ trí nhớ.** Ví dụ Đánh giá v3.5 = 8 states (LAP_KE_HOACH → ... → HOAN_THANH), KHÔNG còn `DA_DANH_GIA` như v3.

**B3. Sibling-check ≥2 module cùng pattern.** Module mới có UC pattern tương tự module cũ (vd CRUD + workflow approve) → đọc test-plan module cũ + clone TC matrix → adjust theo SRS mới. Tiết kiệm 60% effort + cover edge cases đã biết.

**B4. List TC theo nhóm:**
- **Happy path** — tất cả AC chính (M nhóm bắt buộc)
- **State machine** — mỗi transition 1 TC (cho cả allowed + rejected transition)
- **Permission** — mỗi role × CRUD action (theo permission-matrix)
- **Validation** — required field, length, format, business rule
- **Edge case** — boundary, concurrency, error path
- **Integration** — module này ảnh hưởng module khác (entity-map cột "Đọc tại")

**B5. Mark priority P0/P1/P2/P3.**
- **P0** = block UC chính, dev phải fix trước khi ship.
- **P1** = major feature fail hoặc data corruption.
- **P2** = minor UX bug, có workaround.
- **P3** = nice-to-have, defer được.

**B6. Method per TC.** Mỗi TC ghi rõ:
- Tool: Chrome DevTools MCP (default) / curl API direct (chỉ khi UI không expose) / DB query (DBA hỗ trợ)
- Account: từ `input/users.csv` theo role cần test
- Precondition: data state nào cần có trước (link đến seed task)

**B7. Out-of-scope explicit.** TC không test round này phải ghi rõ + lý do:
- Cost cao (vd timeout 30 ngày) → defer
- Cần infra ngoài (mTLS sandbox) → defer
- Out-of-scope SRS update batch hiện tại → defer

**B8. BA sign-off khi spec ambiguous.** TC dựa trên SRS ambiguous → list câu hỏi BA + đánh dấu `[BLOCK-BA-Q1]` trong TC. KHÔNG bịa expected behavior.

### 1.5 Anti-pattern

- ❌ Viết test plan mà chưa đọc SRS module → bịa AC, miss state.
- ❌ Test lại toàn bộ system mỗi lần SRS đổi → lãng phí 64% công sức.
- ❌ Chỉ test 3 file SRS update → miss regression cross-module impact.
- ❌ Mark P0/P1/P2 theo cảm tính → P0 thật bị defer, P3 trivial chiếm timeline.
- ❌ TC "Verify module hoạt động đúng" — quá chung chung, không testable.

---

## 2 — Chuẩn bị test data (Seed)

### 2.1 Mục tiêu

Tạo đủ data **theo filter downstream** để TC chạy được. Seed sai → TC block dây chuyền cả round.

### 2.2 Input bắt buộc

| Input | Vị trí |
|---|---|
| Seed fixture YAML | `input/data/seed-fixture.yaml` |
| Entity map | `input/data/entity-map.md` |
| Flow + state machine | `input/flow-module.md` |
| Account convention | `input/users.csv` (suffix `_01/_02/_03`) |

### 2.3 Output

1 file `output/qa-reports/round{N}/seed/seed-checklist-<module>.md` + records trong DB qua UI walk.

### 2.4 Phương pháp chất lượng (6 bước)

**B1. Acceptance theo filter, KHÔNG theo số lượng tổng.**
- ❌ Sai: "Seed 12 record TVV"
- ✅ Đúng: "Seed ≥3 record cho mỗi `loaiTvv` (CG / NHT / TVV) × ≥1 record cho mỗi LV (6 LV)"

**B2. Mở entity-map cột "Đọc tại" TRƯỚC khi viết acceptance.**
- List downstream module nào sẽ filter entity này.
- Quote SRS filter param (vd `?loaiTvv=CG&trangThai=DANG_HOAT_DONG`).
- Fill section "Downstream consumer × filter" trong seed-checklist.

**B3. Verify per-filter TRƯỚC khi đóng task.**
- ❌ Sai: `total = 12 → ✅ pass`
- ✅ Đúng: `?loaiTvv=CG → ≥1 (verify ✓), ?loaiTvv=NHT → ≥1 (verify ✓), ?loaiTvv=TVV → ≥1 (verify ✓) → ✅`

**B4. Tách 2 task cho entity actor (TVV/CG/NHT/CB/giảng viên/học viên/user).**
- `seed-create` — tạo entity, acceptance theo count + variant coverage.
- `advance-state` — đẩy state từ default sang state consumer cần (vd DA_DUYET, DANG_HOAT_DONG).

**B5. UI walk, KHÔNG bulk POST API.**
- Login đúng role có quyền tạo (theo permission-matrix).
- Walk workflow click-by-click qua Chrome DevTools MCP.
- API direct POST chỉ dùng khi UI thật sự không expose endpoint (rare).

**B6. Update state-snapshot sau khi seed.**
- Mỗi task seed ✅ → chạy verify command (curl / MCP `list_network_requests`).
- Update `tasks/state-snapshot.md` count + timestamp.
- Grep todo.md `[need: ... <entity> ...]` → đổi marker `(✗ N)` → `(✓ N)` cho task có dep entity này.

### 2.5 Anti-pattern (đã gãy thật)

- ❌ Acceptance "12 variant TVV" gộp loại → A5 R5/R6/R7 fail vì 0 CG / 12 TVV (block 4 round).
- ❌ Seed bằng bulk POST API → bypass FE validation, data shape lệch.
- ❌ Reuse account `_01` cho permission test → cookie sticky → false positive.
- ❌ Tạo entity nhưng quên advance state → consumer query trả `data:[]`.

---

## 3 — Thực thi test (Test Execution)

### 3.1 Mục tiêu

Chạy TC theo plan, ghi nhận kết quả với evidence, phân loại block đúng nguyên nhân (KHÔNG retry mù).

### 3.2 Input bắt buộc

| Input | Vị trí |
|---|---|
| Test plan | `output/funtion/<module>/test-plan-<module>.md` |
| Seed checklist (đã PASS) | `output/qa-reports/round{N}/seed/seed-checklist-<module>.md` |
| Account list | `input/users.csv` |
| Tool routing | CLAUDE.md §"Tool routing" — Chrome DevTools MCP mặc định |

### 3.3 Output

- File `output/qa-reports/round{N}/functional/<module>/functional-test-report-<module>.md` (TC functional)
- File `output/qa-reports/round{N}/workflow/<module>/workflow-test-report-<module>.md` (TC workflow)
- 2 bảng bắt buộc sau Verdict (Bảng 1 snapshot TC + Bảng 2 TC chưa chạy được)

### 3.4 Phương pháp chất lượng (8 bước)

**B1. Pre-flight check 30s** (xem [Phụ lục A](#phụ-lục-a--checklist-30s-trước-mọi-action)).

**B2. Login đúng role, KHÔNG default QTHT.**
- TC permission BẮT BUỘC dùng role có quyền theo SCR spec.
- Multi-role test → dùng `isolatedContext` riêng per role qua `mcp__chrome-devtools__new_page` (không logout + login lại, BE cookie sticky).

**B3. Capture evidence trước khi report.**
- Mọi PASS/FAIL phải có ≥1 screenshot.
- API verify qua `list_network_requests` — screenshot Network panel nếu cần.
- Console errors qua `list_console_messages({types:["error","warn"]})` cho mọi FAIL.

**B4. Status terminology Việt** (CLAUDE.md rule, hook check-tc-status):
- ✅ Đạt (PASS clean)
- ⚠️ Sai spec (PASS but deviates SRS, log Minor)
- ❌ Lỗi (FAIL — bug confirmed)
- 🚫 Không test được (BLOCKED — thiếu data/permission/env)
- ⏭ Hoãn (SKIP — out-of-scope round)
- 🤷 Không xác định (cần re-test) — **CẤM kết luận**, phải retry method

**B5. Khi TC block → phân loại 6 nhóm A-F** (xem [Phụ lục B](#phụ-lục-b--6-nhóm-nguyên-nhân-tc-block)).

**B6. Khi TC fail → phân loại lỗi TRƯỚC khi react** (CLAUDE.md §Rule 9):
- Capture diagnostic ngay (URL, screenshot, console, network).
- Phân loại theo bảng (SELECTOR OUTDATED / APP-BE BUG / APP-FE BUG / ACCOUNT / ENV / CRASH).
- Action theo phân loại — KHÔNG retry mù.

**B7. Khi gặp 🤷 Không xác định → retry method TRƯỚC khi defer:**
- Reload fresh page → re-test.
- Mở fresh isolatedContext → re-test.
- Verify qua curl direct → so sánh UI vs API.
- Vẫn ambiguous → mới mark 🤷 + ghi câu hỏi BA.

**B8. Update state machine + todo sau mỗi TC ✅.**
- TC ✅ làm thay đổi state entity → re-run verify command.
- Update state-snapshot.md count + timestamp.
- Hook `auto-rescan-todo.py` tự flip ⏳→🟢 dep task downstream.

### 3.5 Anti-pattern

- ❌ Mark FAIL ngay khi thấy timeout đầu tiên — chưa phân loại Rule 9.
- ❌ Mark BLOCKED không pick nhóm A-F — không actionable.
- ❌ Mark "Sai spec" mà chưa quote SRS line — false positive.
- ❌ Mark "🤷 Không xác định" mà chưa retry method 2-3 lần.
- ❌ Test permission TC bằng QTHT thay vì role spec — bypass permission gate.
- ❌ Logout + login lại để test role khác — cookie sticky → contaminated.

---

## 4 — Log bug (Bug Logging)

### 4.1 Mục tiêu

Ghi bug **đúng** (true bug, không false positive), **đủ** (bằng chứng, repro steps), **đúng spec ref** (SRS version đúng + line cụ thể).

### 4.2 Input bắt buộc

| Input | Vị trí |
|---|---|
| Bug template | `output/template/bug-report-template.md` |
| SRS module | `input/srs-update-2026-5-5/srs-fr-NN-*.md` (NEW) hoặc `input/srs-v3/...` (legacy) |
| NotebookLM HTPLDN | ID `a4ae45bf-cea0-4325-8fee-b1e0be702cf2` |
| State machines v3.5 | `input/data/state-machines-v3.5.md` |
| SRS contradictions tracker | `tasks/srs-contradictions.md` |

### 4.3 Output

Bug entry trong file `output/qa-reports/round{N}/bug-reports/<module>/bug-report-<slug>.md` — theo template 6 sections.

### 4.4 Phương pháp chất lượng — **3-Step Verify TRƯỚC khi log** (mandatory từ 2026-05-13)

**Step 1 — Kiểm tra SRS version.**
- Bug thuộc module nào? → mở `input/srs-update-2026-5-5/srs-fr-NN-*.md` TRƯỚC.
- Module không có trong v3.5? → đọc `CHANGELOG-v3-to-v3.5.md` xem có deprecate.
- v3.5 không cover → fallback `input/srs-v3/` + ghi rõ "Dùng v3 vì v3.5 chưa update module này".

**Step 2 — Quote nguyên văn SRS line số.**
- Mở SRS, tìm line cụ thể, quote `srs-update-2026-5-5/srs-fr-NN-X.md:LINE` + nội dung.
- KHÔNG dùng số dòng từ trí nhớ — luôn mở file verify.
- 2-source verify: query NotebookLM HTPLDN cùng câu → đối chiếu match.

**Step 3 — Verify lại UI/API bằng method khác.**
- UI fail → curl API direct cùng action → so sánh.
- API fail → reload UI fresh → re-test.
- Mâu thuẫn UI vs API → ghi cả 2 trong bug entry, đề xuất BA confirm shape.

### 4.5 6 sections bắt buộc của bug entry (CLAUDE.md rule + hook enforce)

```markdown
## BUG-{MODULE}-{ID} — {Severity} — {Title}

> **Re-test:** YYYY-MM-DD HH:MM:SS R{N} — ❌ Open / ✅ PASS (Closed-verified). {1-2 câu why}.

### Mô tả
{1-3 câu: ai làm gì ở đâu ra sao}

### Các bước tái hiện
1. {step}
2. {step}
...

### Kết quả mong đợi
Theo SRS `srs-update-2026-5-5/srs-fr-NN-X.md:LINE`:
> "{quote nguyên văn line số}"

→ {1-2 câu diễn giải}

### Kết quả thực tế
{Mô tả + console/API trích}

### Bằng chứng
![alt](../image/screenshot.png)

### So sánh  ← optional, chỉ cho bug phân quyền
| Role | Expected | Actual |
```

### 4.6 Wording rule — describe requirement, NOT prescribe implementation

**❌ Sai (prescribe):**
- "Phải hiện button **Đồng ý / Hủy** để duyệt phân công"
- "Phải gọi `POST /api/v1/phan-cong/duyet` trả 200"
- "Phải có mã `ERR-PC-06` khi role TVV phân công"

**✅ Đúng (describe requirement):**
- "Theo SRS line 770, khi role NHT bấm duyệt phân công không hợp lệ, hệ thống phải hiển thị thông báo từ chối + giữ trạng thái cũ"
- "Theo SRS §UC-PC-04, hành động duyệt phân công phải trả về kết quả thành công + chuyển state sang DA_DUYET"

**Lý do:** Dev có thể implement bằng nhiều cách. Bug describe yêu cầu nghiệp vụ, dev tự chọn implementation. Prescribe → talk past (8+ round như BUG-PC-INACTIVE).

### 4.7 Severity guide

| Severity | Trigger | Ví dụ |
|---|---|---|
| **Critical** | UC chính fail hoàn toàn, data corruption, security leak | DN không submit được UC52, role A xem được data role B |
| **Major** | Feature fail nhưng có workaround OR P0 đe doạ ship | Dropdown rỗng do mismatch enum, button approve không hiện |
| **Medium** | Feature partial, UX broken, validation thiếu | Toast không hiện, validation message sai, sort không chạy |
| **Minor** | Cosmetic, copy text sai, alignment | Label sai chính tả, icon lệch |
| **Trivial** | Không ảnh hưởng UC, nice-to-have | Hover tooltip thiếu, animation lag |

### 4.8 Anti-pattern

- ❌ Log bug mà chưa quote SRS line → false positive (3/9 bug R20 deep-verify).
- ❌ Quote sai số line / sai version (v3 thay vì v3.5) → bug invalid.
- ❌ Prescribe implementation (button name, endpoint path, error code cụ thể) → talk past dev.
- ❌ Workaround = bug candidate, nhưng skip vì "tự fix được" → miss regression.
- ❌ Log "UI thiếu element" mà chưa test bằng role có quyền per SCR → false positive.
- ❌ Bug entry thiếu screenshot inline → dev không có context.
- ❌ Thêm section "Tác động" / "Đề xuất fix" / "SRS verification" / "Phân biệt module" → hook block.

---

## 5 — Verify bug đã fix (Bug Verification)

### 5.1 Mục tiêu

Xác nhận dev fix **thật sự** đóng bug — KHÔNG tin chay claim "đã fix". Đây là quy trình gãy nhiều nhất qua 20 round (DEV-FIX-LIST.md tracking).

### 5.2 Input bắt buộc

| Input | Vị trí |
|---|---|
| Dev fix list | `output/qa-reports/round{N}/reverify-*/dev-fix-list.md` |
| Bug entry gốc | `output/qa-reports/round{N}/bug-reports/<module>/bug-report-*.md` |
| SRS module (v3.5) | `input/srs-update-2026-5-5/srs-fr-NN-*.md` |

### 5.3 Output

- Update Bug Summary Table: Status `Open → Closed` hoặc `Open → Reopen`
- **Đúng 1 dòng** Re-test latest sau heading bug (OVERWRITE, KHÔNG append)
- Rename file `bug-report-*.md` → `Pass-bug-report-*.md` khi 100% bug Closed — **tester manual rename + update inbound link** (hook `auto-rename-pass-prefix.py` warn-only, KHÔNG auto-rename vì rename phá link cross-file). Chi tiết CLAUDE.md §"Hook contract auto-rename-pass-prefix.py" + §"Bug-report folder discipline".
- Update todo.md dòng `**Bug:**` count

### 5.4 Phương pháp chất lượng (7 bước)

**B1. Đọc bug entry gốc + dev claim TRƯỚC khi test.**
- Bug expected behavior là gì? (quote SRS line)
- Dev claim fix gì? (commit message, endpoint, file changed)
- Có mâu thuẫn dev claim vs spec → ghi note, ưu tiên spec.

**B2. Re-test bằng UI fresh, KHÔNG curl direct shortcut.**
- Reload page / isolatedContext mới.
- Repro lại đúng các bước ghi trong bug entry.
- Verify expected behavior theo SRS line.

**B3. Verify negative — bug có thật sự đóng KHÔNG?**
- Repro 2 lần (clear cache giữa 2 lần).
- Test edge case adjacent (vd bug A đóng → test bug A' similar không tái phát).

**B4. Khi PASS — overwrite Re-test latest, KHÔNG append.**
```markdown
> **Re-test:** 2026-05-12 15:55:00 R19 — ✅ PASS (Closed-verified). FE đã thêm validation block ERR-PC-02, repro 2 lần đều block đúng.
```
- CHỈ 1 dòng. Xóa dòng cũ.
- Sync field `**Ngày**` ở header với timestamp này (hook auto-bump).

**B5. Khi FAIL hoặc PARTIAL — Reopen + update entry.**
- Status: `Open → Reopen` (KHÔNG `Closed`).
- Update Re-test latest line với why fail.
- Add note dưới Mô tả: "R{N} dev claim fix bằng X nhưng test lại Y vẫn fail vì Z".

**B6. Khi 100% bug trong file Closed → rename Pass- prefix (MANUAL, hook chỉ warn).**

Hook `auto-rename-pass-prefix.py` là **warn-only** — chỉ stderr nhắc, KHÔNG tự rename. Lý do: rename phá link cross-file (todo.md, workflow/functional/seed report, master-index), tester phải quyết + update inbound link bằng MultiEdit batch để tránh 404 cascade. Workflow 3 bước:

1. **Verify điều kiện đủ:** Bug Summary Table KHÔNG còn dòng Status `Open`/`Reopen` (tất cả Closed hoặc strikethrough `~~`) **VÀ** task gốc todo.md đã flip icon ✅ với Kết quả PASS clean.
2. **Rename giữ history:** `git mv output/qa-reports/.../bug-report-<slug>.md output/qa-reports/.../Pass-bug-report-<slug>.md`. Nếu file chưa track: rename filesystem → `git add` file mới + `git rm` file cũ.
3. **MultiEdit update tất cả inbound link** chứa `bug-report-<slug>.md` → `Pass-bug-report-<slug>.md`. Grep nguồn cần update:
   - `tasks/todo.md` + `tasks/todo-<module>.md` — dòng `**Bug:**`
   - `output/qa-reports/round{N}/workflow/` workflow-test-report-*.md
   - `output/qa-reports/round{N}/functional/` functional-test-report-*.md
   - `output/qa-reports/round{N}/seed/` seed-checklist-*.md
   - `output/qa-reports/round{N}/README.md` + `master-index*.md`

**Anti-pattern (KHÔNG rename khi):**
- File một-bug Closed nhưng task todo còn ⚠️/🚫 (bug khác chưa log) → đợi.
- Còn risk re-open (FE fix chưa deploy stable, dev claim mà chưa user manual verify).
- Status có `Reopen` (đã đóng rồi mở lại) → giữ tên cũ.

**B7. Update todo.md dòng `**Bug:**` count.**
- `**Bug:** X/Y đóng` — tăng X khi đóng thêm 1 bug.
- Task icon flip ⚠️→✅ chỉ khi Kết quả PASS clean + chỉ Minor defer OK.

**B8. Testability Sweep sau dev fix — BẮT BUỘC (lesson 2026-05-11).**

Sau re-verify bug, KHÔNG dừng ở chỉ liệt kê bug đóng/mở. Phải rà tất cả TC/path liên quan đã `BLOCKED / DEFER / SKIP / Not run / Partial` để biết bug fix có unblock TC khác không. Output bắt buộc thêm vào reverify report:

```markdown
## Testability Sweep Sau Dev Fix (R{N} reverify YYYY-MM-DD HH:MM:SS)

| TC ID | Status cũ | Trạng thái mới sau fix | Phân loại | Action |
|---|---|---|---|---|
| TV-022 | 🚫 BLOCKED R16 | ✅ Chạy được ngay | Unblock by BUG-X closed | Run trong R{N+1} |
| TV-053 | 🚫 BLOCKED R16 | 🚫 Vẫn block | Cần QA setup NHT seed | QA seed → R{N+2} |
| TV-040 | 🤷 R16 | 🤷 Vẫn block | Chờ BA confirm spec | Escalate BA |

## Setup Cần Chuẩn Bị Để Chạy TC Tiếp
- ...
```

Phân loại bắt buộc 3 nhóm:
- **Chạy ngay** — bug fix unblock, không cần setup.
- **Chạy sau QA setup** — bug fix unblock nhưng cần seed data / account / file.
- **Vẫn block bởi external owner** — chờ BA / Infra / Dev fix bug khác.

### 5.5 Deep-review trigger (mandatory từ 2026-05-13)

Khi gặp 1 trong 3 trường hợp, **CẤM mark closure / defer ngay** — phải deep-review SRS + NotebookLM:

1. Bug mark `[BLOCK chờ BA Q...]`
2. TC mark ⚠️ Sai spec
3. TC mark 🤷 Không xác định

**Deep-review 4 bước:**
1. Grep SRS local — full module + cross-module FR.
2. Query NotebookLM cùng câu — đối chiếu match.
3. Cross-check FR khác có cite mã/state/enum này → SRS contradict?
4. Tự verify lại UI/API bằng curl / fresh context.

Sau deep-review:
- Spec rõ + bug đúng → giữ Open, escalate dev.
- Spec rõ + bug sai → close INVALID, ghi lý do.
- Spec ambiguous + 2 source local-NotebookLM conflict → escalate BA + ghi vào `tasks/srs-contradictions.md`.

### 5.6 Pattern recurring bug — middleware/route-level audit

Khi bug tái phát ≥3 lần ở các module khác nhau (vd permission leak ở 5 entity khác nhau), **không fix per-bug** — request dev audit middleware/route-level. Ghi vào dev-fix-list với note "Recurring pattern — fix at route guard level, not entity level".

### 5.7 Anti-pattern

- ❌ Tin dev claim "đã fix" mà không re-test UI.
- ❌ Verify bằng curl thay vì UI walk → miss FE bug.
- ❌ Append `> Re-verify #6 / #7 / #8` blockquote list → noise, drift Ngày header (CLAUDE.md rule 2026-05-12).
- ❌ Close bug khi PARTIAL fix (1/2 sub-issue) — phải tách bug hoặc giữ Open.
- ❌ Rename Pass- prefix mà quên update inbound link → 404 cascade.
- ❌ Re-test 1 lần PASS → close ngay. Phải repro 2 lần (memory leak / race condition).

---

## 6 — Verify spec + escalate BA

### 6.1 Mục tiêu

Đảm bảo mọi bug/test reference đúng SRS version + đúng line. Khi spec mâu thuẫn → escalate BA có đầy đủ evidence, KHÔNG bịa expected behavior.

### 6.2 Input bắt buộc

| Input | Vị trí |
|---|---|
| SRS v3.5 (latest) | `input/srs-update-2026-5-5/` |
| SRS v3 (legacy) | `input/srs-v3/` |
| CHANGELOG | `input/srs-update-2026-5-5/CHANGELOG-v3-to-v3.5.md` |
| State machines ref | `input/data/state-machines-v3.5.md` |
| SRS contradictions tracker | `tasks/srs-contradictions.md` |
| NotebookLM HTPLDN | ID `a4ae45bf-cea0-4325-8fee-b1e0be702cf2` |

### 6.3 Phương pháp chất lượng (6 bước)

**B1. SRS v3.5 luôn ưu tiên — fallback master nội bộ TRƯỚC khi qua v3 legacy.**

Thứ tự ưu tiên (V3.5 publish 2026-05-05 chưa hoàn thiện hết slice file):
1. `input/srs-update-2026-5-5/srs-fr-NN-*.md` — slice file per module (nếu có).
2. `input/srs-update-2026-5-5/srs-v3.5.md` — master file v3.5 (fallback khi slice thiếu).
3. `input/srs-v3/...` — v3 legacy (fallback cuối khi v3.5 hoàn toàn không cover).
4. Mọi fallback PHẢI ghi rõ trong bug entry: "Dùng srs-v3.5.md master vì slice fr-NN chưa có" hoặc "Dùng v3 vì v3.5 chưa update".

**B2. 2-source verify mọi spec citation.**
- Grep SRS local: `grep -rn "<keyword>" input/srs-update-2026-5-5/`
- Query NotebookLM HTPLDN cùng câu hỏi
- Đối chiếu match → quote local + ghi note NotebookLM match status

**B3. Cross-FR check khi state/enum/error code lạ.**
- Module A dùng `LOAI_HINH_HT`, module B dùng `LOAI_HINH_HO_TRO` → grep cả 2 enum across SRS folder.
- Nếu thấy contradict → ghi vào `tasks/srs-contradictions.md` + escalate BA.

**B4. Khi spec ambiguous — escalate BA với evidence.**
Format câu hỏi BA chuẩn:
```
[BA-Q-N] {Module} — {Topic}
- Spec hiện trạng: SRS line X nói "..." vs SRS line Y nói "..."
- Bug/TC ảnh hưởng: BUG-X-001, TC-Y-002
- 2 phương án có thể: (a) ..., (b) ...
- Khuyến nghị: (a) vì ...
- Cần BA chốt trước YYYY-MM-DD để unblock {round N}
```

**B5. Update SRS contradictions tracker.**
Mỗi contradiction → 1 entry trong `tasks/srs-contradictions.md`:
- ID + module + 2 line conflict + impact (bug/TC) + status (open/BA-resolved) + decision date.

**B6. CHANGELOG tracking khi BA chốt.**
BA confirm decision → update CHANGELOG-v3-to-v3.5.md hoặc tạo CHANGELOG-fix-NNN.md.
Update tất cả bug/test reference theo decision mới.

### 6.4 Anti-pattern

- ❌ Quote SRS từ trí nhớ → sai line, sai version.
- ❌ Đẩy BA ngay khi gặp ambiguous mà chưa search SRS local + NotebookLM.
- ❌ Bịa expected behavior khi spec im lặng → false bug.
- ❌ Trust v3 cũ khi v3.5 đã update → spec stale, test invalid.
- ❌ BA confirm verbal mà không update CHANGELOG → next round QA dùng spec cũ.

---

## 7 — Đóng round + báo cáo

### 7.1 Mục tiêu

Kết round có 2 bảng tổng + dev-fix-list rõ + handoff cho tester sau hiểu được state ngay.

### 7.2 Input bắt buộc

| Input | Vị trí |
|---|---|
| Tất cả TC report của round | `output/qa-reports/round{N}/functional/` + `workflow/` |
| Tất cả bug report của round | `output/qa-reports/round{N}/bug-reports/` |
| State snapshot | `tasks/state-snapshot.md` |
| Todo.md | `tasks/todo.md` + module split files |

### 7.3 Output

1. **2 bảng bắt buộc** trong mọi `functional-test-report-*.md` + `workflow-test-report-*.md` — **đặt ngay sau Verdict + Accounts (LATEST round), TRƯỚC narrative deep-dive Phase 1/2/3.** Format exact ở §7.4.
2. **Dev-fix-list** trong `output/qa-reports/round{N}/reverify-YYYY-MM-DD/dev-fix-list.md`:
   - Bug ID × severity × priority × status × dev claim × QA verify result × SRS ref
3. **Lessons-learned append** — nếu có bài học mới, append `tasks/lessons-learned.md`
4. **Master index update** — `output/qa-reports/round{N}/README.md` + `master-index.md`

### 7.4 Phương pháp chất lượng (6 bước)

**B1. Bảng 1 — Trạng thái toàn bộ TC (snapshot LATEST).**

Aggregate **toàn bộ TC** trong test plan của module × cột Status mới nhất × Note 1-line. Update sau MỖI round. Không xóa TC cũ — TC đổi status flip icon + ghi round phát hiện.

Format exact (copy nguyên cột):

```markdown
## Bảng trạng thái TC (snapshot R{N} — LATEST YYYY-MM-DD HH:MM:SS)

| TC ID | Tên TC ngắn | Status | Round phát hiện | Note (≤15 từ) |
|---|---|:-:|:-:|---|
| TV-001 | Tạo VV | ✅ PASS | R8 | OK clean |
| TV-022 | Auto-save 30s | ❌ FAIL | R16-P2 | Endpoint /trao-doi missing — BUG-BE-R16-003 |
| TV-053 | NHT phân công CG | 🚫 BLOCKED | R16-P2 | Cascade R7.3.14 NHT TVV seed |
| ... | ... | ... | ... | ... |
| **Tổng** | **N TC** | ✅X · ⚠️Y · ❌Z · 🚫W · ⏭V · 🤷U | | |
```

Status icon: ✅Đạt / ⚠️Sai spec / ❌Lỗi / 🚫Không test được / ⏭Hoãn / 🤷Không xác định.

**B2. Bảng 2 — TC chưa chạy được + cần làm gì để chạy.**

Aggregate CHỈ TC non-PASS (⚠️/❌/🚫/⏭/🤷). Format **đơn giản, ngôn ngữ tự nhiên, ngắn gọn**.

**Trước Bảng 2 BẮT BUỘC 1 dòng tóm tắt:** "Hiện tại còn N TC chưa chạy được — chia M nhóm: X chờ dev fix · Y chờ seed · Z out-of-scope..."

Format exact:

```markdown
## Bảng TC chưa chạy được — cần làm gì để chạy (R{N})

| TC ID | Vì sao chưa chạy được | Cần làm gì để chạy | Ai làm |
|---|---|---|:-:|
| TV-022 | Endpoint auto-save 30s chưa có (BUG-BE-R16-003) | BE expose endpoint `/trao-doi-nhap` theo SRS §1496 | Dev BE |
| TV-053 | NHT chưa có TVV record để phân công | Seed R7.3.14 — walk workflow tạo NHT có TVV | QA seed |
| TV-040 | TVV stats counter không có trong spec | BA confirm có yêu cầu không | BA |
```

Cột constraint:
- "Vì sao chưa chạy được" — 1 câu ≤20 từ, ngôn ngữ tự nhiên (KHÔNG ERR code, KHÔNG endpoint path đầy đủ — đẩy chi tiết vào bug-report). Pick 1 trong 6 nhóm A-F (xem Phụ lục B). CẤM tự nghĩ nhóm 7+.
- "Cần làm gì để chạy" — action cụ thể ≤25 từ. Không "Defer/TBD" — phải nói rõ task / ai cần làm trước.
- "Ai làm" — chọn 1: `Dev BE / Dev FE / QA seed / QA API / BA / Infra / DBA`.

**Lý do 2 bảng quan trọng:** user / QA handoff cross-tester / dev / BA cần đọc 1 lần biết ngay "TC nào chạy được, TC nào kẹt vì gì, ai cần unblock". Không có 2 bảng này → tester sau phải đọc full narrative Phase 1/2/3 nhiều round → tốn thời gian + miss status.

**B3. Sync state-snapshot sau round.**
- Mọi entity có state thay đổi → re-run verify command.
- Update count + timestamp `tasks/state-snapshot.md`.
- Hook `auto-rescan-todo.py` tự flip ⏳→🟢 dep task downstream.

**B4. Dev-fix-list — priority + severity + SRS ref.**
- Mỗi bug Open 1 dòng: BUG-ID | Severity | Priority (P0-P3) | Title | SRS ref | Dev claim | QA verify result.
- Sort: P0 trên cùng → P3 dưới cùng.
- Section "Phương án xử lý" — nhóm bug theo loại fix (FE/BE/Spec/Recurring).

**B5. Bug-report rename Pass- prefix.**
- File 100% bug Closed → `git mv bug-report-*.md Pass-bug-report-*.md`.
- Update inbound link (todo.md, workflow/functional/seed report, master-index).
- Hook auto-warn khi quên rename.

**B6. Lessons-learned append (nếu có).**
Trigger append `tasks/lessons-learned.md`:
- Pattern bug tái phát ≥3 lần
- Workflow QA gãy (vd seed split fail, verify miss)
- Spec contradict mới phát hiện
- Tool/method workflow mới validated

Format entry:
```markdown
## YYYY-MM-DD HH:MM:SS — {Tiêu đề ngắn}

**Vấn đề:** {1-3 câu}
**Quyết định xử lý:** {1-3 câu}
**Bài học áp dụng:** {bullet list, mỗi bullet 1-2 câu}
```

### 7.5 Anti-pattern

- ❌ Quên 2 bảng → tester sau phải đọc full narrative để biết state.
- ❌ Bảng 2 cột "Vì sao" >25 từ → đẩy chi tiết ra bug-report.
- ❌ Cột "Ai làm" ghi "QA team" / "Dev team" → không actionable.
- ❌ Dev-fix-list không sort priority → P0 lẫn P3 → dev không biết fix gì trước.
- ❌ Quên rename Pass- prefix → next round nhầm bug đã đóng là chưa đóng.
- ❌ Append lessons-learned trùng nội dung memory → drift.

---

## 8 — Quản lý regression

### 8.1 Mục tiêu

Phát hiện sớm bug đóng rồi mở lại + bug tái phát cross-module → fix root cause, không patch per-bug.

### 8.2 Phương pháp chất lượng (4 bước)

**B1. Regression smoke sau mỗi dev deploy.**
- 5-10 TC critical path (login → main UC → main report) chạy lại sau mỗi deploy mới.
- Mỗi bug Closed có 1 TC regression riêng — track trong file `output/qa-reports/regression-tests.md`.

**B2. Recurring bug tracker.**
- Bug đóng → mở lại lần 2 → flag `[RECURRING]` trong bug-report.
- Bug pattern xuất hiện ở ≥3 module khác nhau → flag `[CROSS-MODULE PATTERN]` + escalate dev audit middleware.
- Track trong `tasks/recurring-bugs.md` (tạo khi cần).

**B3. Cross-module audit khi pattern phát hiện.**
- Ví dụ: permission leak ở 5 entity khác nhau → request dev audit route guard / middleware level.
- Bug entry ghi note "Recurring pattern — fix at <layer> level, not entity level".

**B4. Round retro — mỗi 5 round.**
- Kết R5, R10, R15, R20: viết retro `output/qa-reports/round{N}/retro.md`:
  - Top 3 bug pattern repeat
  - Top 3 workflow QA gãy
  - 1-3 cải tiến SOP cho 5 round tiếp

### 8.3 Anti-pattern

- ❌ Đóng bug recurring lần thứ 3 mà không escalate cross-module audit.
- ❌ Skip regression smoke sau deploy mới → miss regression.
- ❌ Bug mới tương tự bug cũ trong module khác → log file riêng thay vì link cross-ref.

---

## Phụ lục A — Checklist 30s trước mọi action

Trước khi viết test plan / seed / chạy TC / log bug / verify / đóng round, đọc nhanh:

```
[ ] SRS version đang dùng đúng chưa? (v3.5 default, v3 chỉ khi v3.5 chưa cover)
[ ] State machine module đã đọc từ ref card chưa? (input/data/state-machines-v3.5.md)
[ ] Permission matrix role test đúng chưa? (output/permission-matrix.md)
[ ] State snapshot count latest chưa? (tasks/state-snapshot.md)
[ ] Tool routing đúng? Chrome DevTools MCP default, không gstack mặc định.
[ ] Account convention đúng suffix? _01 primary, _02 fallback, _03 permission test.
[ ] Round folder đúng latest chưa? round{N}-YYYY-MM-DD/
[ ] Nếu log bug — 3-step verify đã làm chưa? (version + quote line + verify method khác)
```

---

## Phụ lục B — 6 nhóm nguyên nhân TC block

| Nhóm | Tên | Trigger | Phương án | Owner |
|:-:|---|---|---|:-:|
| **A** | Thiếu seed data | DB chưa có record / variant / state | Walk UI tạo data per filter | QA seed |
| **B** | Chờ dev fix bug | Đã log BUG-{ID} với SRS ref, status Open | Wait dev fix → verify | Dev BE/FE |
| **C** | Chờ BA confirm spec | 2 spec mâu thuẫn / SRS ambiguous | Query NotebookLM + SRS local → escalate BA | BA |
| **D** | Lỗi env / chờ infra | mTLS sandbox / API key / batch / mock | Request infra setup | Infra |
| **E** | Dependency upstream chưa xong | TC/task khác chưa PASS | Format `[need: ≥N entity state X]` | QA seed / Dev |
| **F** | Lý do khác | DB-level only / out-of-scope / cost cao | Document + defer / DBA hỗ trợ | DBA / Tester lead |

**Cấm:**
- Tự nghĩ nhóm 7+ ngoài A-F.
- Ghi "Defer/TBD/Skip" mà không pick nhóm A-F.
- Mark nhóm B mà chưa log bug — phải log BUG-{ID} TRƯỚC, mark nhóm B SAU.
- Defer >2 round nhóm F mà không escalate user lead.

Chi tiết trigger + workflow re-test: `output/template/tc-block-classification-template.md`.

---

## Phụ lục C — Tool mapping MCP quick ref

| Action | Chrome DevTools MCP |
|---|---|
| Login flow | Template 15 step (xem CLAUDE.md §Template login MCP) |
| Get URL | `mcp__chrome-devtools__evaluate_script(() => window.location.href)` |
| Screenshot | `mcp__chrome-devtools__take_screenshot({filePath: ".../image/X.png"})` |
| Console errors | `mcp__chrome-devtools__list_console_messages({types:["error","warn"]})` |
| Network XHR | `mcp__chrome-devtools__list_network_requests({resourceTypes:["xhr","fetch"]})` |
| DOM inspect | `mcp__chrome-devtools__evaluate_script(() => document.querySelector(...))` |
| Wait UI ready | `mcp__chrome-devtools__wait_for({text:["..."], timeout:15000})` |
| Click element | `mcp__chrome-devtools__click({uid:"..."})` ← uid từ `take_snapshot` |
| Fill form | `mcp__chrome-devtools__fill_form({elements:[{uid, value}]})` |
| Multi-role isolation | `mcp__chrome-devtools__new_page({isolatedContext:"role-X-rN"})` |
| Verify toast (ephemeral) | MutationObserver pattern (xem CLAUDE.md §MCP-Rule 8) |

**App-side quirks (verified 2026-04-20/21):**
- Login dùng `localStorage` key `auth-store` + HttpOnly refresh-token cookie.
- Logout đúng cách: POST `/api/v1/auth/logout` → clear localStorage + sessionStorage → navigate `/login`.
- Sidebar default collapsed 64px → click "Thu gọn menu" để expand 260px trước khi truy cập submenu.
- UI dùng Drawer (right panel) cho CRUD form, KHÔNG Modal dialog (spec sai).
- Button submit label **[Đồng ý]** thay vì [Lưu].
- Row action Sửa/Xóa là `<a>` tag, không phải `<button>`.

**Khi nào fallback gstack `$B`:** chỉ khi MCP crash thật + restart không recover, hoặc user explicit "dùng gstack". Chi tiết: `docs/legacy/gstack-fallback-rules.md`.

---

## Phụ lục D — Quy tắc giao tiếp + viết report

(Áp dụng cho mọi tester, mọi report)

- **Câu ngắn 1-2 dòng** trong giao tiếp + status update.
- **Phản biện trước action** — không yes-machine. Spot vấn đề trước khi run.
- **Status terminology Việt** — không English jargon (BLOCKED/PENDING/DEFERRED).
- **Mỗi response BẮT BUỘC kết thúc đoạn "Tóm tắt" 2-5 dòng** trả lời "đã làm gì + kết quả / việc tiếp theo".
- **Note ngày kèm `HH:MM:SS`** — không chỉ `YYYY-MM-DD` trống.
- **Bug report header chỉ 1 trường Ngày + 1 trường Round** — timestamp update gần nhất.
- **Re-test latest OVERWRITE 1 dòng** — không append history blockquote list.
- **Workflow report round mới nhất lên đầu** với hậu tố `(LATEST)`.

---

## Bảo trì SOP này

- File này được commit vào repo, đọc tự động qua CLAUDE.md reference.
- Mỗi 5 round (R{5N}) → review SOP có cần update không (đặc biệt sau retro).
- Cải tiến SOP phải có ≥1 ví dụ thực tế support (lesson learned từ round vừa qua).
- KHÔNG override CLAUDE.md global rule — SOP bổ sung chi tiết, CLAUDE.md là root.
- Cross-project rule (TVV/CG/NHT seed split, dep chain state-explicit, bug 6 sections) đã ở `~/.claude/CLAUDE.md` — SOP project chỉ tham chiếu.

---

*Version: 1.0 — 2026-05-13. Maintained by QA team.*
