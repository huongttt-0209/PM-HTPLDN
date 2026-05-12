# Plan — Xây dựng agent team test full luồng 18 module PM HTPLDN

> **Owner:** huongttt · **Ngày tạo:** 2026-05-12 11:30:00 · **Trạng thái:** Đang chờ user duyệt
>
> **Mục tiêu:** Cho 18 module (16 FR + 2 cross-cutting), produce 3 artifact mỗi module — test-plan.md đầy đủ 6 section, codex-review.md (feedback từ Codex CLI), todo.md (tracker theo convention dự án). Output vào `docs/todo-test/<module-slug>/`.
>
> **Nguồn input:** `docs/todo-test/list-module.md` · `input/quy-trinh-nghiep-vu/{01,02,flow-module}.md` · `tasks/system-overview.md` · `input/srs-v3/srs-fr-XX.md` · `input/srs-update-2026-5-5/srs-fr-XX.md`.

---

## 1. Assumptions surfaced

Đã hỏi user 4 câu, chốt:
- **Scope:** 16 FR (FR-01..FR-16) + 2 cross-cutting (hồ sơ/đổi MK + permission matrix) = **18 module**.
- **Depth:** Full template theo `output/template/test-plan-overview-template.md` 6 section.
- **Codex review:** Per-module (~18 lần gọi `codex exec`).
- **Output layout:** Per-module folder `docs/todo-test/<slug>/test-plan.md + todo.md + codex-review.md` + master `README.md`.

Assumption thêm (chưa hỏi, sẽ surface để user override nếu cần):
1. "Test full luồng" = workflow + functional + permission + edge + state machine (matches Full template), **KHÔNG** chỉ E2E happy path. Nếu user chỉ muốn E2E → switch sang depth Lightweight.
2. Output là **fresh plan cho handoff/onboarding tester mới**, **KHÔNG** sync ngược với artifact đã có ở `output/qa-reports/round7-2026-05-06/*`. Plan này độc lập với round R7-R8 hiện tại.
3. Todo.md theo convention `tasks/todo-<module>.md` hiện tại (≤25 từ Kết quả, dòng `**Bug:**`, status icon ✅⚠️🚫⏳🟢🔵) nhưng để TRỐNG cho round chưa chạy — đây là **shell todo** sẵn sàng cho tester pick up, không phải log kết quả retro.
4. Codex review = `codex exec` non-interactive, sandbox-disabled (read-only review không cần edit), output text capture vào codex-review.md. Nếu codex quota hết → fallback self-review bằng agent-skills:code-reviewer.
5. Mỗi subagent đọc CHỈ file scope của nó (SRS module + section liên quan của system-overview/02-thu-tu-module), KHÔNG load full SRS consolidated 6695 dòng → tránh context overflow.

→ User correct any assumption ngay, nếu im lặng tôi proceed với 5 assumption trên.

---

## 2. Architecture decisions

**AD-1. Lead Planner = main thread (Claude Opus), Drafter/Reviser = general-purpose subagents.**
- Main thread giữ context tổng, dispatch + checkpoint. Subagents context isolation, đọc scope hẹp.
- 18 module → 4 batch parallel × ~5 module/batch (max 5 song song để không tràn token budget).

**AD-2. ~~Codex review qua `codex exec`~~ → CHỐT 2026-05-12 12:00: Self-review bằng agent-skills:code-reviewer.**
- Codex pre-flight bị user interrupt → fallback sang Claude self-review per Plan Risk R1.
- Per-module: spawn `code-reviewer` subagent đọc test-plan.md + SRS file → output `review.md` structured (## Gaps / ## Suggestions / ## Verdict).
- File output `review.md` (rename từ `codex-review.md` cho tool-neutral).

**AD-3. Per-module folder `docs/todo-test/<slug>/` chứa 3 file cố định.**
```
docs/todo-test/
├── plan.md                       ← File này (master plan)
├── README.md                     ← Index aggregate 18 module
├── list-module.md                ← Đã có
├── _meta/
│   ├── module-matrix.md          ← Phase 0 output (classification table)
│   └── codex-review-summary.md   ← Phase 4 aggregate codex gaps
├── fr-01-dashboard/
│   ├── test-plan.md
│   ├── codex-review.md
│   └── todo.md
├── fr-02-hoi-dap/
│   ├── ...
... (16 module FR)
├── ho-so-doi-mat-khau/
│   └── ...
└── cross-cutting-permission/
    └── ...
```

**AD-4. Module slug naming (kebab-case từ list-module.md):**

| # | Slug | FR | Tầng | SRS Update v3.5? |
|:-:|---|---|:-:|:-:|
| 1 | `fr-01-dashboard` | FR-01 | 5 | ✅ |
| 2 | `fr-02-hoi-dap` | FR-02 | 3 | ✅ |
| 3 | `fr-03-dao-tao` | FR-03 | 3 | ✅ |
| 4 | `fr-04-chuyen-gia-tvv` | FR-04 | 2 | ✅ |
| 5 | `fr-05-vu-viec` | FR-05 | 3 | ✅ |
| 6 | `fr-06-chi-tra` | FR-06 | 4 | ✅ |
| 7 | `fr-07-doanh-nghiep` | FR-07 | 2 | ✅ |
| 8 | `fr-08-danh-gia-hq` | FR-08 | 4 | ✅ |
| 9 | `fr-09-bieu-mau` | FR-09 | 2 | ✅ |
| 10 | `fr-10-qtht` | FR-10 | 1 | ✅ |
| 11 | `fr-11-bao-cao` | FR-11 | 5 | ❌ (giữ v3) |
| 12 | `fr-12-tv-chuyen-sau` | FR-12 | 3 | ✅ |
| 13 | `fr-13-tv-nhanh` | FR-13 | 4 | ✅ |
| 14 | `fr-14-hop-dong-tv` | FR-14 | 4 | ❌ (giữ v3) |
| 15 | `fr-15-ct-htpldn` | FR-15 | 2+5 | ❌ (giữ v3) |
| 16 | `fr-16-api` | FR-16 | 5 | ❌ (giữ v3) |
| 17 | `ho-so-doi-mat-khau` | cross | — | ✅ (file riêng) |
| 18 | `cross-cutting-permission` | cross | — | ✅ (DELTA-MAP) |

**AD-5. Dependency graph cho order test plan (build foundation first):**

```
Tầng 1 (NỀN):       FR-10 QTHT
                       ↓
Tầng 2 (MASTER):    FR-07 DN, FR-04 CG/TVV/NHT, FR-09 Biểu mẫu, FR-15 GĐ1
                       ↓
Cross-cutting:      ho-so-doi-mat-khau, cross-cutting-permission
                       ↓
Tầng 3 (LÕI):       FR-05 Vụ việc, FR-02 Hỏi đáp, FR-12 TVCS, FR-03 Đào tạo
                       ↓
Tầng 4 (PHÁI SINH): FR-14 HĐTV, FR-06 Chi trả, FR-13 TVN, FR-08 Đánh giá HQ
                       ↓
Tầng 5 (TỔNG HỢP):  FR-11 Báo cáo, FR-01 Dashboard, FR-16 API, FR-15 GĐ2
```

Plan drafting có thể chạy parallel toàn bộ (mỗi module độc lập về SRS). Nhưng todo execution sau này phải theo order tầng. Order trong README.md theo tầng để tester dễ pick up.

---

## 3. Phases & tasks (vertical slicing)

> **Slicing logic:** Mỗi module = 1 vertical slice complete (test-plan + codex-review + todo). Phase 0/4 cross-cutting setup/aggregate, Phase 1-3 looping qua 18 module.

### Phase 0 — Discovery + classification (Lead Planner, sequential, ~15 phút)

#### Task 0.1: Module classification matrix
**Description:** Đọc list-module.md + system-overview.md §4 + 02-thu-tu-module.md, sinh bảng 18 module × { tầng, FR ref, SCR ref, v3.5 update?, nhóm Rule 4 A/B/C/D, complexity S/M/L, dependencies upstream }.

**Acceptance:**
- [ ] File `docs/todo-test/_meta/module-matrix.md` tồn tại
- [ ] 18 dòng module với 7 cột đầy đủ
- [ ] Có cột "Cite SRS local path" (`srs-v3/<file>` hoặc `srs-update-2026-5-5/<file>`)
- [ ] Có cột "Module upstream cần seed trước" (để order task execution)

**Verification:**
- [ ] `grep -c "^| fr-\|^| ho-\|^| cross-" docs/todo-test/_meta/module-matrix.md` = 18
- [ ] Mỗi module có ≥1 cite SRS line

**Files touched:** `docs/todo-test/_meta/module-matrix.md` (new)
**Scope:** S (1 file)

---

### Phase 1 — Test plan drafting (18 subagents parallel batches, ~3-4 giờ)

#### Task 1.X (×18): Draft test-plan.md cho module `<slug>`
**Description:** Spawn subagent (general-purpose) đọc SRS v3 + v3.5 module, system-overview section, 02-thu-tu-module section, drafts test plan theo `output/template/test-plan-overview-template.md`.

**Per-agent prompt skeleton:**
```
Brief: Draft test plan for module FR-XX <name> following project template.
Inputs to read:
  - /Users/teamai/Downloads/antigravity/QA/skilkk/input/srs-v3/srs-fr-XX.md
  - /Users/teamai/Downloads/antigravity/QA/skilkk/input/srs-update-2026-5-5/srs-fr-XX.md (if exists)
  - /Users/teamai/Downloads/antigravity/QA/skilkk/input/srs-update-2026-5-5/_DELTA-MAP-FRXX.md (if exists)
  - /Users/teamai/Downloads/antigravity/QA/skilkk/input/quy-trinh-nghiep-vu/02-thu-tu-module.md (section for module)
  - /Users/teamai/Downloads/antigravity/QA/skilkk/tasks/system-overview.md §4.<N> for module
  - /Users/teamai/Downloads/antigravity/QA/skilkk/input/users.csv (accounts)
  - /Users/teamai/Downloads/antigravity/QA/skilkk/input/data/entity-map.md (dependencies)
  - /Users/teamai/Downloads/antigravity/QA/skilkk/output/template/test-plan-overview-template.md (template)
Output: /Users/teamai/Downloads/antigravity/QA/skilkk/docs/todo-test/<slug>/test-plan.md
Constraints:
  - 6 section: Phạm vi / BR + Error codes + Permission + UI Layout / TC structure / TC count / Pass criteria / References
  - Cite SRS line numbers (KHÔNG paraphrase BR)
  - SOURCE MODE: LOCAL (đọc file local, KHÔNG NotebookLM)
  - Path SRS cite có prefix (srs-v3/ hoặc srs-update-2026-5-5/) — theo memory `feedback_bug_srs_ref_path`
  - Permission matrix table: liệt kê role × action specific cho module này
  - State machine: nếu module có workflow (FR-02, 05, 06, 08, 12, 13) → embed state diagram
  - TC breakdown: ≥10 TC chia happy/negative/edge/permission
Anti-pattern:
  - Tự suy luận BR "Áp dụng cho module X" không cite SRS
  - Skip §2.4 UI Layout
  - Để Pass criteria trống
Report: Tóm tắt ≤5 dòng (file path + section count + TC count + cite count).
```

**Acceptance per module:**
- [ ] `docs/todo-test/<slug>/test-plan.md` tồn tại, ≥150 dòng
- [ ] 6 section đầy đủ: §1 Phạm vi · §2 Quy tắc nghiệp vụ · §3 Cấu trúc TC · §4 TC count · §5 Tiêu chí PASS · §6 Tham chiếu
- [ ] §2.1 BR table có ≥5 row cite SRS line cụ thể
- [ ] §2.3 Permission matrix có ≥1 row cho mỗi role có quyền
- [ ] §2.4 UI Layout liệt kê components từ SCR liên quan
- [ ] §2.5 State machine nếu module có workflow
- [ ] §4 TC count table có ≥10 TC (chia ≥4 nhóm: happy/negative/edge/permission)

**Verification per module:**
- [ ] `grep -c "^## " test-plan.md` ≥ 6
- [ ] `grep -E "srs-(v3|update)/" test-plan.md | wc -l` ≥ 5
- [ ] `wc -l test-plan.md` ≥ 150
- [ ] Heading §2.5 (State machine) hiện diện nếu module ∈ {FR-02, FR-05, FR-06, FR-08, FR-12, FR-13}

**Dependencies:** Task 0.1 ✅ (cần matrix biết tầng/v3.5 status)
**Parallelism:** 4-5 module/batch, 4 batch tuần tự = ~18 module
**Scope per agent:** M (1 module = đọc 4-6 file + write 1 file)

**Suggested batching:**
- Batch A (5): fr-10-qtht, fr-07-doanh-nghiep, fr-04-chuyen-gia-tvv, fr-09-bieu-mau, fr-15-ct-htpldn (Tầng 1+2)
- Batch B (5): fr-05-vu-viec, fr-02-hoi-dap, fr-12-tv-chuyen-sau, fr-03-dao-tao, ho-so-doi-mat-khau (Tầng 3 + cross)
- Batch C (4): fr-14-hop-dong-tv, fr-06-chi-tra, fr-13-tv-nhanh, fr-08-danh-gia-hq (Tầng 4)
- Batch D (4): fr-11-bao-cao, fr-01-dashboard, fr-16-api, cross-cutting-permission (Tầng 5 + cross)

#### Checkpoint 1: After Phase 1
- [ ] 18 file `test-plan.md` tồn tại under `docs/todo-test/<slug>/`
- [ ] Tất cả pass verification grep + line count
- [ ] Lead Planner review 3 random module (1 tầng cao, 1 tầng giữa, 1 tầng thấp) — đảm bảo quality consistent
- [ ] **Review với human trước khi sang Phase 2** (codex call sẽ tốn quota — chốt quality trước)

---

### Phase 2 — Codex review (sequential per module, ~1-2 giờ; or parallel 3-4 nếu codex CLI hỗ trợ)

#### Task 2.0: Codex pre-flight (Lead Planner, ~5 phút)
**Description:** Chạy thử `codex exec` 1 lần với 1 test-plan.md để verify auth + output format + thời gian.

**Acceptance:**
- [ ] Chạy `codex exec --skip-git-repo-check "review file <path>"` cho 1 module (vd fr-10-qtht) — exit code 0
- [ ] Output có structure: gaps + suggestions + verdict
- [ ] Thời gian < 3 phút/call

**Fallback:** Nếu codex auth fail → STOP, ask user `codex login` qua `!` prompt.

#### Task 2.X (×18): Codex review per module
**Description:** Per module, run codex exec với test-plan.md path, save output to codex-review.md.

**Per call command (proposal):**
```bash
codex exec --skip-git-repo-check -C /Users/teamai/Downloads/antigravity/QA/skilkk \
  "Review test plan at docs/todo-test/<slug>/test-plan.md. \
   Focus on: BR completeness (cross-check srs-v3/srs-fr-XX.md), \
   missing edge cases, permission matrix correctness, \
   state machine completeness if applicable. \
   Output structured: ## Gaps · ## Suggestions · ## Verdict (APPROVE/REVISE)." \
  > docs/todo-test/<slug>/codex-review.md 2>&1
```

**Acceptance per module:**
- [ ] `docs/todo-test/<slug>/codex-review.md` tồn tại, ≥30 dòng
- [ ] Có section "Gaps" và "Verdict"
- [ ] Verdict ∈ {APPROVE, REVISE}

**Verification per module:**
- [ ] grep -E "^## (Gaps|Verdict)" codex-review.md count ≥ 2
- [ ] grep -E "(APPROVE|REVISE)" codex-review.md count ≥ 1

**Dependencies:** Task 1.X ✅ (cần test-plan.md draft)
**Parallelism:** 3 song song max (codex CLI có rate limit) — 6 batch × 3 module = ~6 round
**Scope:** XS (1 bash call per module)

#### Checkpoint 2: After Phase 2
- [ ] 18 codex-review.md files
- [ ] Lead Planner đọc Verdict aggregate, đếm APPROVE vs REVISE
- [ ] Nếu >50% REVISE → flag user trước Phase 3 (quality test-plan quá thấp)

---

### Phase 3 — Revision + todo generation (18 subagents parallel batches, ~2-3 giờ)

#### Task 3.X (×18): Revise test-plan + generate todo.md per module
**Description:** Spawn subagent (general-purpose) đọc `test-plan.md` + `codex-review.md`, apply codex feedback (nếu REVISE), generate `todo.md` theo convention dự án.

**Per-agent prompt skeleton:**
```
Brief: Revise test-plan.md based on codex review, then generate todo.md.
Inputs:
  - docs/todo-test/<slug>/test-plan.md (current draft)
  - docs/todo-test/<slug>/codex-review.md (codex feedback)
  - tasks/todo-qtht.md (sample todo convention)
  - /Users/teamai/Downloads/antigravity/QA/skilkk/CLAUDE.md (todo template rules section "Quy tắc viết todo.md")
Steps:
  1. If codex Verdict=REVISE: apply feedback to test-plan.md (address ≥80% gaps)
  2. Generate docs/todo-test/<slug>/todo.md:
     - Header: # TODO — <slug> — <module-name>
     - Tổng số task (TBD round, để placeholder R0.X.Y)
     - Section "## Tasks" với TC group từ test-plan §4 → split thành seed + workflow + functional + edge + permission
     - Mỗi task icon 🟢 (chưa chạy), placeholder "**Kết quả:** TBD", "**Output:**" trỏ tới future report path
     - KHÔNG fake icon ✅ vì plan chưa execute
     - Tuân CLAUDE.md "Quy tắc viết todo.md": ≤25 từ Kết quả, dòng **Bug:** chỉ khi có bug, etc.
Report: ≤5 dòng — diff summary test-plan + todo task count.
```

**Acceptance per module:**
- [ ] `docs/todo-test/<slug>/todo.md` tồn tại
- [ ] Header format đúng (`# TODO — <slug> — <name>`)
- [ ] ≥5 task với icon 🟢 (chưa chạy)
- [ ] Mỗi task có format CLAUDE.md template (template cứng)
- [ ] test-plan.md đã revise nếu codex REVISE — diff visible trong git

**Verification per module:**
- [ ] `grep -c "^- 🟢 \*\*" todo.md` ≥ 5
- [ ] `grep -c "^  - \*\*Kết quả:\*\*" todo.md` ≥ 5
- [ ] Hook `.claude/hooks/check-todo-concise.py` không block (nếu hook scan path `docs/todo-test/` thì pass; nếu hook chỉ scan `tasks/todo*.md` thì N/A)

**Dependencies:** Task 2.X ✅
**Parallelism:** 4-5 module/batch, 4 batch
**Scope per agent:** S (1-2 file)

#### Checkpoint 3: After Phase 3
- [ ] 18 todo.md files
- [ ] Lead Planner review 3 random module — đảm bảo todo format đúng template
- [ ] Verify hook check-todo-concise.py không bị trigger trên `docs/todo-test/`

---

### Phase 4 — Master index + summary (Lead Planner, sequential, ~20 phút)

#### Task 4.1: Generate master README.md
**Description:** Aggregate 18 module vào index, order theo tầng dependency.

**Acceptance:**
- [ ] `docs/todo-test/README.md` tồn tại
- [ ] Table: 18 row × { slug, FR, name, tầng, complexity, link test-plan, link todo, codex verdict }
- [ ] Order theo tầng 1→5 (foundation first)
- [ ] Section "How to use" cho tester mới

**Verification:** `grep -c "^| \[" README.md` ≥ 18

#### Task 4.2: Codex review summary
**Description:** Aggregate top gaps cross-module để escalate.

**Acceptance:**
- [ ] `docs/todo-test/_meta/codex-review-summary.md` tồn tại
- [ ] List top 5-10 gap themes cross-module (vd: missing BR-DATA-06 Export, miss permission row, etc.)
- [ ] Verdict distribution count (APPROVE vs REVISE)

#### Checkpoint 4: Complete
- [ ] All 18 module có 3 file (test-plan + codex-review + todo)
- [ ] README.md + module-matrix.md + codex-review-summary.md generated
- [ ] User review final & approve

---

## 4. Risks & mitigations

| # | Risk | Impact | Mitigation |
|:-:|---|:-:|---|
| R1 | Codex CLI auth chưa setup / hết quota | High | Task 2.0 pre-flight 1 call trước bulk. Fallback: dùng agent-skills:code-reviewer self-review |
| R2 | Subagent context overflow khi đọc full SRS v3.5 (6695 dòng) | High | Prompt subagent đọc CHỈ srs-fr-XX.md (per-module), KHÔNG đọc srs-v3.5.md consolidated |
| R3 | 18 module parallel = tràn token budget main thread | Medium | Batch 4-5 song song, mỗi subagent report ≤200 từ summary, không trả full file content |
| R4 | Codex review quality kém (generic feedback) | Medium | Prompt codex cụ thể: cite SRS line, list missing BR, check permission row by row |
| R5 | Hook `check-todo-concise.py` block khi write todo.md mới (vì hook scan path glob) | Low | Test 1 todo.md trước, nếu hook block → adjust path glob hook hoặc cấu hình skip |
| R6 | test-plan.md quá lớn cho codex exec input | Low | test-plan target 150-300 dòng (5-10KB), codex CLI nhận input lớn OK |
| R7 | User thay đổi scope giữa chừng (vd thêm module mới) | Low | Plan modular per-module, có thể chạy thêm 1 module riêng không phá structure |
| R8 | Module v3.5 update KHÔNG có file riêng (FR-11/14/15/16) → test plan có thể miss delta | Medium | Subagent kiểm tra existence của srs-update-2026-5-5/srs-fr-XX.md, nếu thiếu thì cite CHANGELOG-v3-to-v3.5.md |

---

## 5. Open questions — CHỐT 2026-05-12

1. ✅ **Codex auth:** Đã `codex login`, proceed pre-flight Phase 2.0.
2. ✅ **Parallelism:** 4-5 subagent/batch (~8-10 giờ wall-clock).
3. ✅ **Codex command:** `codex exec --skip-git-repo-check` non-interactive.
4. ✅ **Todo task ID:** Prefix `T-FR{XX}-{seq}` (plan-stage), phân biệt với `R{N}.{phase}.{seq}` round actual.
5. ✅ **Cross-module link:** CÓ — todo task seed/workflow ghi `[need: ...]` link tới todo module upstream theo memory `feedback_dependency_chain_state_explicit`.

---

## 6. Estimated timeline (best-case parallel)

| Phase | Task | Wall-clock |
|:-:|---|:-:|
| 0 | Discovery + matrix | 15 phút |
| 1 | 18 test-plan draft (4 batch × 5 parallel) | 3-4 giờ |
| Checkpoint 1 | User review 3 sample | 20 phút |
| 2.0 | Codex pre-flight | 5 phút |
| 2 | 18 codex review (6 batch × 3 parallel) | 1-2 giờ |
| Checkpoint 2 | Lead aggregate verdict | 10 phút |
| 3 | 18 revise + todo gen (4 batch × 5 parallel) | 2-3 giờ |
| Checkpoint 3 | User sanity check | 20 phút |
| 4 | Master index + summary | 20 phút |
| **Total** | | **~8-10 giờ wall-clock** |

Sequential nếu không parallel: ~20-25 giờ.

---

## 7. Tham chiếu

- [output/template/test-plan-overview-template.md](../../output/template/test-plan-overview-template.md) — Template Full 6 section
- [tasks/system-overview.md](../../tasks/system-overview.md) — Module overview §4
- [input/quy-trinh-nghiep-vu/02-thu-tu-module.md](../../input/quy-trinh-nghiep-vu/02-thu-tu-module.md) — Module dependency + state machine
- [docs/todo-test/list-module.md](list-module.md) — 18 module list
- [CLAUDE.md](../../CLAUDE.md) — Project conventions (todo template, bug template, skill routing)
- [tasks/todo-qtht.md](../../tasks/todo-qtht.md) — Sample todo convention
- [tasks/qa-workflow-template.md](../../tasks/qa-workflow-template.md) — Workflow template

---

*Plan version 1.0 — chờ user duyệt Open Questions §5 + 5 assumption §1 trước khi enter Phase 0.*
