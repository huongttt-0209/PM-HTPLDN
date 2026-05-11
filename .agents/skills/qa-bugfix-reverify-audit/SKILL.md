---
name: qa-bugfix-reverify-audit
description: Use when the user asks to re-verify bugs that dev claims were fixed for any QA module or feature, determine whether each bug is Closed-verified/Open/Partial, identify which blocked test cases are now unblocked by those fixes, and list immediate follow-up TC to run. Especially useful for HTPLDN QA bug-report and functional report folders.
metadata:
  short-description: Re-verify fixed bugs and audit QA blocks
---

# QA Bugfix Reverify Audit

## Purpose

Run a repeatable bug-fix verification workflow after dev claims fixes: re-test the fixed bugs, update bug verdicts, identify TC/path unblocked by those fixes, and list the immediate follow-up test cases to run next.

## Inputs

Ask for missing inputs only if they cannot be inferred from the user request or repo layout.

Preferred inputs:

- Module or feature name, e.g. `Hỏi đáp`, `Tư vấn chuyên sâu`, `Chi trả`, `Dashboard`.
- Todo file, e.g. `tasks/todo-hoi-dap.md`, `tasks/todo-tvcs.md`, or another module todo.
- State snapshot, e.g. `tasks/state-snapshot.md`.
- Bug report directory.
- Functional report directory.
- Workflow report directory if the bug affects workflow paths.
- Local SRS file(s), e.g. `input/srs-update-*/srs-fr-*.md`, `input/quy-trinh-nghiep-vu/*.md`, `output/funtion/*.md`.
- Optional NotebookLM source/link/context if available for spec cross-check.
- Optional: specific bug IDs or TC IDs to prioritize.

## Source Order

Read sources in this order:

1. Bug report directory for bug status, repro steps, fix claims, and re-test notes.
2. Functional report directory for latest phase reports and affected TC.
3. Workflow report directory only if the bug affects workflow paths.
4. `todo-*.md` for latest phase links, coverage claims, and dependencies.
5. `state-snapshot.md` only for current data counts, state distributions, or seed availability.

Prefer `rg`, `ls -lt`, and `sed`. If multiple reports exist, choose the newest report by filename phase number and file mtime, then cross-check against the todo file. Do not conclude from an older phase if a newer phase exists.

## Reverify Workflow

1. Build the bug-fix map:
   - Identify bugs marked `dev fixed`, `claim fixed`, `Open`, `Partial`, `Open (partial)`, `re-test`, or recently changed.
   - Map each bug to affected TC/path and source report.
   - Note any required seed data, accounts, endpoints, or environment conditions for re-test.

2. Identify bugs to re-verify:
   - Include bugs marked `Open`, `Open (partial)`, `Partial`, `dev claim fixed`, `re-test`, or recently changed.
   - Include bugs listed as closed only if the latest report says they were re-tested in the current round.
   - For each bug, capture previous status, expected behavior, actual latest evidence, and verdict.
   - Compute bug totals from the latest bug report(s): `Open`, `Partial/Open`, `Closed`, `Closed-verified`, and newly found bugs. If counts differ between todo and bug report, cite both and prefer the newer timestamp.

3. Execute verification when feasible:
   - Use UI/API/browser checks if the repo has a reachable test environment and the user asked to actually verify.
   - If verification cannot run, classify it as blocked and state exactly what is missing.
   - Do not mark a bug closed without fresh evidence from a latest report or current verification.

4. Identify newly unblocked TC/path:
   - If a bug is Closed-verified, list the TC/path that can now be run or re-run.
   - If a bug remains Open/Partial, list the TC/path that stay blocked.
   - Do not perform a full module status audit here; defer that to `qa-module-status-audit`.

5. Run a post-fix testability sweep:
   - Review TC/path that were `BLOCKED`, `DEFER`, `SKIP`, `Not run`, `Partial`, or blocked by the fixed bug.
   - Decide whether each TC can be run now, can be run after QA prepares conditions, or must remain blocked by an external owner.
   - Do not limit this to seed data. Check data, accounts, permissions, upstream endpoints, environment, files, mail, time travel, rate limits, and spec status.

6. Classify every unrun, blocked, partial, or failed TC using this taxonomy:
   - `thiếu seed data`
   - `thiếu state/data setup` (record exists but wrong status/version/scope)
   - `thiếu account/role/permission`
   - `thiếu file/upload artifact`
   - `thiếu email/notification setup`
   - `chờ dev fix bug`
   - `chờ BA confirm spec`
   - `lỗi env/tooling`
   - `dependency upstream chưa xong`
   - `thiếu backdated/time-travel data`
   - `rate limit/session/JWT/OTP issue`
   - `data drift/cleanup làm mất pool`
   - `integration/API endpoint chưa deploy`
   - `cần DBA/API direct hỗ trợ setup`
   - `cần mock/stub lỗi external service`
   - `chưa đủ evidence/report cũ`
   - `lý do khác`

7. Resolve `chờ BA confirm spec` items before treating them as BA-blocked:
   - First search local SRS and QA spec files with `rg` using TC ID, FR ID, rule ID, screen ID, field names, enum values, error codes, and Vietnamese/English labels.
   - Check the primary SRS before derived QA plans. Prefer `input/srs-update-*`, `input/quy-trinh-nghiep-vu`, then `output/funtion`, smoke specs, permission matrix, and existing BA question docs.
   - If NotebookLM access/context is available, query it after local SRS search to catch missed references. Use NotebookLM only as a cross-check, not as a replacement for local source citations.
   - Provide exact source references: file path + line number or section/table name. Short direct quotes are allowed only when needed; otherwise paraphrase tightly.
   - If SRS answers the question, do not classify it as BA-blocked. Reclassify to the real cause: dev bug, seed gap, test data gap, env/tooling, or upstream dependency.
   - If SRS is contradictory, ambiguous, or silent after search, then mark `chờ BA confirm spec` and write the exact BA question plus the SRS evidence/gap.
   - Never invent an expected behavior just to close a question. If evidence is missing, say `Không đủ căn cứ trong SRS local/NotebookLM`.

8. Propose next actions. This is mandatory, not optional:
   - For dev bugs: name the bug, expected fix, and affected TC.
   - For seed gaps: name the exact seed record/state needed.
   - For upstream dependencies: name the upstream task or endpoint.
   - For BA gaps: state the decision needed and include why SRS local/NotebookLM did not already answer it.
   - For tooling/data gaps: state the needed capability, e.g. time-travel or backdated insert.
   - For account/permission gaps: name the role/account or permission needed.
   - For upload/mail/mock gaps: name the exact artifact or service setup needed.
   - For data drift: state whether to re-seed, restore, or create replacement records.
   - For each blocked/failed/partial TC, provide at least one concrete next action.
   - If no action is possible from QA side, state who must act next and what deliverable is needed.

9. Produce immediate follow-up testing plan:
   - List TC/path that should be run now because the verified bug fix unblocked them.
   - List TC/path that can run after QA prepares conditions such as seed/state/account/file/mock/backdate setup.
   - List TC/path that still cannot run because the bug did not fix or another blocker remains.
   - If the user needs full module readiness, recommend running `qa-module-status-audit` after these follow-up TC finish.

## Output Format

Use Vietnamese unless the user asks otherwise.

Start with a concise summary table:

```markdown
| Module / task | Bug Open | Bug Closed | Bug re-verify | TC/path được unblock | TC/path vẫn block | Next action |
|---|---:|---:|---|---|---|---|
```

Then include details:

```markdown
**Bug Re-verify**

| Bug ID | Trạng thái trước | Kết quả re-test | Evidence | Verdict |
|---|---|---|---|---|

**Bug Summary**

| Tổng bug | Open | Partial/Open | Closed | Closed-verified | New bug trong lần audit | Ghi chú nguồn |
|---:|---:|---:|---:|---:|---:|---|

**TC/Path Bị Ảnh Hưởng**

| TC/path | Liên quan bug | Trạng thái sau re-test | Nguyên nhân nếu vẫn block | Phương án xử lý tiếp theo | Owner tiếp theo |
|---|---|---|---|---|---|---|

**Testability Sweep Sau Dev Fix**

| TC/path | Trạng thái hiện tại | Có thể chạy tiếp? | Điều kiện cần chuẩn bị | Loại blocker | Action trước khi chạy | Owner |
|---|---|---|---|---|---|---|

**Setup Cần Chuẩn Bị Để Chạy TC Tiếp**

| Nhóm setup | Áp dụng cho TC/path | Cần chuẩn bị cụ thể | Cách tạo/kiểm tra đề xuất | Ai xử lý | Sau khi xong rerun |
|---|---|---|---|---|---|

**Spec / BA Confirmation Check**

| TC / vấn đề | Câu hỏi cần xác nhận | SRS local đã kiểm tra | NotebookLM đã kiểm tra | Kết luận từ nguồn | Verdict |
|---|---|---|---|---|---|

**Phương Án Xử Lý Tiếp Theo**

| Nhóm vấn đề | Áp dụng cho | Việc cần làm cụ thể | Điều kiện xong | Ưu tiên | Owner |
|---|---|---|---|---|---|

**Follow-up TC Cần Chạy Sau Re-verify**

| TC/path | Lý do có thể chạy bây giờ | Điều kiện/setup cần chuẩn bị | Kết quả kỳ vọng |
|---|---|---|---|

**Tóm Tắt Cuối**

- Kết quả re-verify: <N> bug đã Closed-verified, <N> bug vẫn Open/Partial.
- TC/path chạy được ngay: <list hoặc "không có">.
- TC/path chạy được sau setup QA-side: <list + setup chính>.
- TC/path vẫn block bởi bên ngoài: <list + owner/blocker>.
- Việc cần làm tiếp: <1-3 action ngắn, rõ>.
- Sau khi chạy xong follow-up TC: dùng `qa-module-status-audit` để kết luận module đã full luồng hay chưa.
```

End with:

- `Kết luận re-verify`: bug nào closed, bug nào còn open/partial.
- `TC/path có thể chạy ngay tiếp theo` if any.
- `Tóm Tắt Cuối` must be present as bullet points. Use natural, plain Vietnamese. Do not write this as a dense paragraph.
- `Phương án xử lý tiếp theo` must be present as its own section. If there are no open or blocked items, state `Không còn action mở`.
- `Testability Sweep Sau Dev Fix` must be present. It must distinguish `chạy ngay`, `chạy sau QA setup`, and `vẫn block bởi external owner`.
- `Setup Cần Chuẩn Bị Để Chạy TC Tiếp` must be present when any TC is runnable after preparation. If none, state `Không có setup QA-side có thể chuẩn bị`.
- `Spec / BA Confirmation Check` must be present when any item is categorized as `chờ BA confirm spec`. If no BA/spec item exists, state `Không có case cần BA confirm`.
- `Bug Open` and `Bug Closed` counts must appear in the top summary table. If exact counts cannot be derived, use `N/A` and explain why in `Bug Summary`.

## Rules

- Be strict about “latest”: always compare phase numbers, modified times, and todo links.
- Focus on bug re-verification. Do not claim full module readiness unless the user explicitly asks and you have run a module status audit.
- Separate blocked TC from failed TC.
- Do not hide partial failures inside PASS counts; call out caveats.
- Use clickable file links with absolute paths and line numbers when referencing local files.
- If you did not run fresh UI/API verification, say the answer is based on existing reports.
- Keep the final answer high-signal; detailed evidence belongs in tables, not long prose.
- The final summary must be short bullet points, easy for a human project lead to scan.
- Do not omit next actions. Every `Open`, `Partial`, `FAIL`, `BLOCKED`, `SKIP`, `DEFER`, or unrun TC must map to a concrete next action or an explicit external owner/dependency.
- Do not treat all deferred TC as seed gaps. Use the full blocker taxonomy and say exactly what is missing.
- Prefer running all TC that are runnable now or after QA-side setup before handing off to module status audit.
- Do not omit bug counts from the summary. The reader must be able to see how many bugs remain open and how many are closed without reading details.
- Do not label a case `chờ BA confirm spec` until after checking local SRS. If NotebookLM is available, cross-check there too.
- Do not fabricate spec answers. If SRS evidence is absent or contradictory, say that clearly and ask a precise BA question.
- Any spec-based answer must cite exact local file path and line/section. NotebookLM evidence can support the conclusion, but local SRS citation is the primary source.

## Invocation Examples

```text
Use qa-bugfix-reverify-audit for module <MODULE>. Re-verify bugs dev claims fixed, update bug verdicts, and list TC/path now unblocked.
```

```text
Dùng qa-bugfix-reverify-audit cho module <MODULE> sau dev fix. Re-test bug đã fix, tổng hợp bug Open/Closed, chạy testability sweep cho TC defer/block/unrun, chỉ rõ TC nào chạy ngay, TC nào chạy sau setup QA-side, TC nào vẫn block external, và follow-up TC cần chạy tiếp.
```
