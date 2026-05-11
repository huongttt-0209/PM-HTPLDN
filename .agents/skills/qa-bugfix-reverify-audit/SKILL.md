---
name: qa-bugfix-reverify-audit
description: Use when the user asks to re-verify dev-fixed bugs and audit QA completion status for any QA module or feature, including current workflow status, functional coverage, unrun or blocked test cases, block causes, and next actions. Especially useful for HTPLDN QA report folders with todo, workflow, functional, bug-report, and state-snapshot files.
metadata:
  short-description: Re-verify fixed bugs and audit QA blocks
---

# QA Bugfix Reverify Audit

## Purpose

Run a repeatable audit for any module or feature after dev claims fixes: verify the fixed bugs, recompute test coverage, identify unrun or blocked test cases, classify block causes, and propose the next concrete action.

## Inputs

Ask for missing inputs only if they cannot be inferred from the user request or repo layout.

Preferred inputs:

- Module or feature name, e.g. `Hỏi đáp`, `Tư vấn chuyên sâu`, `Chi trả`, `Dashboard`.
- Todo file, e.g. `tasks/todo-hoi-dap.md`, `tasks/todo-tvcs.md`, or another module todo.
- State snapshot, e.g. `tasks/state-snapshot.md`.
- Workflow report directory.
- Functional report directory.
- Bug report directory.
- Local SRS file(s), e.g. `input/srs-update-*/srs-fr-*.md`, `input/quy-trinh-nghiep-vu/*.md`, `output/funtion/*.md`.
- Optional NotebookLM source/link/context if available for spec cross-check.
- Optional: specific bug IDs or TC IDs to prioritize.

## Source Order

Read sources in this order:

1. `todo-*.md` for task status, latest phase links, coverage claims, and dependencies.
2. Workflow report directory for latest workflow status.
3. Functional report directory for latest phase reports.
4. Bug report directory for bug status and re-test notes.
5. `state-snapshot.md` only for current data counts, state distributions, or seed availability.

Prefer `rg`, `ls -lt`, and `sed`. If multiple reports exist, choose the newest report by filename phase number and file mtime, then cross-check against the todo file. Do not conclude from an older phase if a newer phase exists.

## Reverify Workflow

1. Build the module map:
   - Identify seed tasks, workflow tasks, and functional tasks.
   - Extract current status icons and coverage numbers.
   - Note dependencies such as upstream deploys, seed tasks, BA confirmations, or tooling needs.

2. Identify bugs to re-verify:
   - Include bugs marked `Open`, `Open (partial)`, `Partial`, `dev claim fixed`, `re-test`, or recently changed.
   - Include bugs listed as closed only if the latest report says they were re-tested in the current round.
   - For each bug, capture previous status, expected behavior, actual latest evidence, and verdict.
   - Compute bug totals from the latest bug report(s): `Open`, `Partial/Open`, `Closed`, `Closed-verified`, and newly found bugs. If counts differ between todo and bug report, cite both and prefer the newer timestamp.

3. Execute verification when feasible:
   - Use UI/API/browser checks if the repo has a reachable test environment and the user asked to actually verify.
   - If verification cannot run, classify it as blocked and state exactly what is missing.
   - Do not mark a bug closed without fresh evidence from a latest report or current verification.

4. Recompute coverage:
   - Count PASS from the latest cumulative table when available.
   - If a later phase adds PASS/FAIL/BLOCKED after a cumulative table, adjust the total explicitly and cite the phase.
   - Keep deprecated TC separate from active TC.

5. Classify every unrun, blocked, partial, or failed TC:
   - `thiếu seed data`
   - `chờ dev fix bug`
   - `chờ BA confirm spec`
   - `lỗi env/tooling`
   - `dependency upstream chưa xong`
   - `thiếu backdated/time-travel data`
   - `lý do khác`

6. Resolve `chờ BA confirm spec` items before treating them as BA-blocked:
   - First search local SRS and QA spec files with `rg` using TC ID, FR ID, rule ID, screen ID, field names, enum values, error codes, and Vietnamese/English labels.
   - Check the primary SRS before derived QA plans. Prefer `input/srs-update-*`, `input/quy-trinh-nghiep-vu`, then `output/funtion`, smoke specs, permission matrix, and existing BA question docs.
   - If NotebookLM access/context is available, query it after local SRS search to catch missed references. Use NotebookLM only as a cross-check, not as a replacement for local source citations.
   - Provide exact source references: file path + line number or section/table name. Short direct quotes are allowed only when needed; otherwise paraphrase tightly.
   - If SRS answers the question, do not classify it as BA-blocked. Reclassify to the real cause: dev bug, seed gap, test data gap, env/tooling, or upstream dependency.
   - If SRS is contradictory, ambiguous, or silent after search, then mark `chờ BA confirm spec` and write the exact BA question plus the SRS evidence/gap.
   - Never invent an expected behavior just to close a question. If evidence is missing, say `Không đủ căn cứ trong SRS local/NotebookLM`.

7. Propose next actions. This is mandatory, not optional:
   - For dev bugs: name the bug, expected fix, and affected TC.
   - For seed gaps: name the exact seed record/state needed.
   - For upstream dependencies: name the upstream task or endpoint.
   - For BA gaps: state the decision needed and include why SRS local/NotebookLM did not already answer it.
   - For tooling/data gaps: state the needed capability, e.g. time-travel or backdated insert.
   - For each blocked/failed/partial TC, provide at least one concrete next action.
   - If no action is possible from QA side, state who must act next and what deliverable is needed.

8. Produce a final completion roadmap:
   - This is a required report-level section, separate from per-TC actions.
   - Answer: “Muốn hoàn thành full luồng chức năng thì phải làm gì tiếp?”
   - Group actions by real blocker, not by individual TC when multiple TC share the same cause.
   - Include concrete completion criteria and the TC/workflow paths that will be unblocked.
   - Examples: deploy upstream endpoint, seed exact missing data, create backdated records, ask BA to decide a spec conflict, or fix a named bug.

## Output Format

Use Vietnamese unless the user asks otherwise.

Start with a concise summary table:

```markdown
| Module / task | Trạng thái luồng | Coverage hiện tại | Bug Open | Bug Closed | Bug re-verify | TC còn thiếu/block | Nguyên nhân chính | Next action |
|---|---:|---:|---:|---:|---|---|---|---|
```

Then include details:

```markdown
**Bug Re-verify**

| Bug ID | Trạng thái trước | Kết quả re-test | Evidence | Verdict |
|---|---|---|---|---|

**Bug Summary**

| Tổng bug | Open | Partial/Open | Closed | Closed-verified | New bug trong lần audit | Ghi chú nguồn |
|---:|---:|---:|---:|---:|---:|---|

**TC Chưa Chạy / Block**

| TC | Mục tiêu | Trạng thái | Nguyên nhân block | Điều kiện unblock | Phương án xử lý tiếp theo | Owner tiếp theo |
|---|---|---|---|---|---|---|

**Spec / BA Confirmation Check**

| TC / vấn đề | Câu hỏi cần xác nhận | SRS local đã kiểm tra | NotebookLM đã kiểm tra | Kết luận từ nguồn | Verdict |
|---|---|---|---|---|---|

**Phương Án Xử Lý Tiếp Theo**

| Nhóm vấn đề | Áp dụng cho | Việc cần làm cụ thể | Điều kiện xong | Ưu tiên | Owner |
|---|---|---|---|---|---|

**Phương Án Để Hoàn Thành Full Luồng Chức Năng**

| Mục tiêu hoàn tất | Việc cần làm tiếp | Loại blocker | Owner | Điều kiện xác nhận xong | TC/luồng được unblock |
|---|---|---|---|---|---|

Kết luận full luồng: Module hiện <Ready/Conditional/Not ready> vì <lý do chính>. Để hoàn tất full, cần ưu tiên: <action 1>; <action 2>; <action 3>. Sau đó rerun: <TC/path list>.
```

End with:

- `Ship-readiness`: `Ready`, `Conditional`, or `Not ready`.
- `Điều kiện tối thiểu để hoàn tất`.
- `TC có thể chạy ngay tiếp theo` if any.
- `Phương án xử lý tiếp theo` must be present as its own section. If there are no open or blocked items, state `Không còn action mở`.
- `Phương Án Để Hoàn Thành Full Luồng Chức Năng` must be present as the final report-level roadmap. If the module is already fully complete, state `Đã hoàn thành full luồng; không còn blocker`.
- `Spec / BA Confirmation Check` must be present when any item is categorized as `chờ BA confirm spec`. If no BA/spec item exists, state `Không có case cần BA confirm`.
- `Bug Open` and `Bug Closed` counts must appear in the top summary table. If exact counts cannot be derived, use `N/A` and explain why in `Bug Summary`.

## Rules

- Be strict about “latest”: always compare phase numbers, modified times, and todo links.
- Separate workflow completion from functional coverage.
- Separate blocked TC from failed TC.
- Do not hide partial failures inside PASS counts; call out caveats.
- Use clickable file links with absolute paths and line numbers when referencing local files.
- If you did not run fresh UI/API verification, say the answer is based on existing reports.
- Keep the final answer high-signal; detailed evidence belongs in tables, not long prose.
- Do not omit next actions. Every `Open`, `Partial`, `FAIL`, `BLOCKED`, `SKIP`, `DEFER`, or unrun TC must map to a concrete next action or an explicit external owner/dependency.
- Do not stop at per-TC actions. Always add the final completion roadmap explaining the shortest path to full-pass/full-workflow completion.
- Do not omit bug counts from the summary. The reader must be able to see how many bugs remain open and how many are closed without reading details.
- Do not label a case `chờ BA confirm spec` until after checking local SRS. If NotebookLM is available, cross-check there too.
- Do not fabricate spec answers. If SRS evidence is absent or contradictory, say that clearly and ask a precise BA question.
- Any spec-based answer must cite exact local file path and line/section. NotebookLM evidence can support the conclusion, but local SRS citation is the primary source.

## Invocation Examples

```text
Use qa-bugfix-reverify-audit for module <MODULE>. Read the module todo file, state snapshot, workflow/functional/bug report folders, then audit fixed bugs and remaining blocked TC.
```

```text
Dùng qa-bugfix-reverify-audit audit lại module <MODULE> sau dev fix. Cho bảng tổng hợp, bug re-verify, TC chưa chạy/block, nguyên nhân, spec/BA confirmation check dựa trên SRS local + NotebookLM nếu có, và bắt buộc có mục Phương án để hoàn thành full luồng chức năng.
```
