---
name: qa-module-status-audit
description: Use when the user asks to review the current completion status of any QA module or feature, determine whether the full workflow is complete, summarize workflow and functional coverage, count open/closed bugs, identify unrun/deferred/blocked TC or paths, verify BA/spec blockers against local SRS and NotebookLM when available, and propose the roadmap to reach full completion.
metadata:
  short-description: Audit module workflow status and full completion
---

# QA Module Status Audit

## Purpose

Review the current state of a module or feature and answer: “Chức năng này đã hoạt động full luồng chưa? Nếu chưa, còn thiếu gì và phải làm gì để hoàn tất?”

Use this after bug re-verification and follow-up TC runs, or whenever the user needs a status report for module readiness.

## Inputs

Ask only for missing inputs that cannot be inferred from repo layout.

Preferred inputs:

- Module or feature name, e.g. `Hỏi đáp`, `Tư vấn chuyên sâu`, `Chi trả`, `Dashboard`.
- Todo file, e.g. `tasks/todo-*.md`.
- State snapshot, e.g. `tasks/state-snapshot.md`.
- Workflow report directory.
- Functional report directory.
- Bug report directory.
- Local SRS/spec files, e.g. `input/srs-update-*/srs-fr-*.md`, `input/quy-trinh-nghiep-vu/*.md`, `output/funtion/*.md`.
- Optional NotebookLM source/link/context for spec cross-check.

## Source Order

1. `todo-*.md`: task status, current coverage claims, latest phase links, dependencies.
2. Workflow reports: full workflow/path status.
3. Functional reports: TC coverage, latest phase, PASS/FAIL/BLOCK/DEFER.
4. Bug reports: Open/Closed counts, remaining blockers, re-test evidence.
5. `state-snapshot.md`: current entity counts, state distribution, seed readiness.
6. Local SRS/spec files for any spec/BA questions.

Use `rg`, `ls -lt`, and `sed`. When several phase reports exist, choose the latest by phase number, modified time, and todo link. Never conclude from an older phase if a newer phase exists.

## Workflow

1. Build module status:
   - Identify seed tasks, workflow tasks, functional tasks, and dependencies.
   - Extract status icons and latest coverage numbers.
   - Separate workflow completion from functional TC coverage.

2. Determine full workflow status:
   - `Đã xong`: all required workflow paths passed and no blocker remains.
   - `Còn dở`: some paths passed, but at least one path is blocked, failed, skipped, or deferred.
   - `Chưa bắt đầu`: no meaningful workflow path has run.
   - Name the exact missing path(s), not only the percentage.

3. Compute functional coverage:
   - Total planned TC, active TC, deprecated TC when available.
   - PASS, FAIL, PARTIAL, BLOCKED, DEFER, SKIP, unrun.
   - If latest report adds new PASS/FAIL/BLOCK after an older cumulative table, adjust the total and cite the latest source.

4. Compute bug summary:
   - Count `Open`, `Partial/Open`, `Closed`, `Closed-verified`, and new bugs from latest bug reports.
   - If todo and bug report disagree, cite both and prefer the newer timestamp.

5. Classify all unrun/deferred/blocked/failed TC or paths:
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

6. Resolve BA/spec blockers before leaving them as BA blockers:
   - First search local SRS/spec files with `rg` using TC ID, FR ID, rule ID, screen ID, field names, enum values, error codes, and Vietnamese/English labels.
   - Prefer primary SRS files under `input/srs-update-*`, then `input/quy-trinh-nghiep-vu`, then derived QA docs under `output/`.
   - If NotebookLM access/context is available, query it after local SRS search as a cross-check for missed references.
   - If SRS answers the question, reclassify the blocker to the real cause and cite the exact file path + line/section.
   - If SRS is silent, ambiguous, or contradictory, keep `chờ BA confirm spec` and write the exact BA question plus evidence/gap.
   - Do not invent expected behavior. If evidence is missing, say `Không đủ căn cứ trong SRS local/NotebookLM`.

7. Produce roadmap to full completion:
   - Group by root blocker, not only by TC.
   - State exact action, owner, completion criteria, and TC/path that will be unblocked.
   - Include all required setup actions explicitly, e.g. “seed 1 record state X”, “backdate DA_DUYET 30+ ngày”, “create account role Y”, “prepare upload file Z”, “mock external API fail”, “deploy endpoint Y”.

## Output Format

Use Vietnamese unless the user asks otherwise.

Start with:

```markdown
| Module | Trạng thái luồng | Workflow | Functional coverage | Bug Open | Bug Closed | TC/path còn thiếu | Blocker chính | Phương án để full |
|---|---|---:|---:|---:|---:|---|---|---|
```

Then include:

```markdown
**Bug Summary**

| Tổng bug | Open | Partial/Open | Closed | Closed-verified | New bug | Ghi chú nguồn |
|---:|---:|---:|---:|---:|---:|---|

**Workflow / Functional Coverage**

| Nhóm | Tổng | PASS | FAIL | PARTIAL | BLOCKED/DEFER/SKIP | Chưa chạy | Ghi chú |
|---|---:|---:|---:|---:|---:|---:|---|

**TC/Path Chưa Hoàn Tất**

| TC/path | Mục tiêu | Trạng thái | Nguyên nhân block | Điều kiện unblock | Phương án xử lý tiếp theo | Owner |
|---|---|---|---|---|---|---|

**Setup / Điều Kiện Cần Chuẩn Bị**

| Nhóm setup | Áp dụng cho TC/path | Cần chuẩn bị cụ thể | Cách tạo/kiểm tra đề xuất | Owner | Sau khi xong rerun |
|---|---|---|---|---|---|

**Spec / BA Confirmation Check**

| TC / vấn đề | Câu hỏi cần xác nhận | SRS local đã kiểm tra | NotebookLM đã kiểm tra | Kết luận từ nguồn | Verdict |
|---|---|---|---|---|---|

**Phương Án Để Hoàn Thành Full Luồng Chức Năng**

| Mục tiêu hoàn tất | Việc cần làm tiếp | Loại blocker | Owner | Điều kiện xác nhận xong | TC/luồng được unblock |
|---|---|---|---|---|---|

**Tóm Tắt Cuối**

- Trạng thái module: <Sẵn sàng/Có điều kiện/Chưa sẵn sàng>.
- Full luồng chưa: <đã full / chưa full> vì <lý do chính>.
- Coverage hiện tại: <workflow + functional coverage>.
- Bug còn mở: <số lượng + bug chính nếu có>.
- Blocker chính: <1-3 blocker quan trọng nhất>.
- Việc cần làm để full: <1-3 action ngắn, rõ>.
- Sau khi xử lý xong cần rerun: <TC/path list>.
```

End with:

- `Kết luận full luồng`: use Vietnamese statuses only:
  - `Sẵn sàng` = full workflow/coverage required for current scope is complete, no blocking bug remains.
  - `Có điều kiện` = core flow works but some TC/path remains blocked/deferred or non-critical blocker remains.
  - `Chưa sẵn sàng` = critical workflow/functionality remains failed or blocked.
- `Điều kiện tối thiểu để hoàn tất`.
- `TC/path cần rerun sau khi unblock`.
- `Tóm Tắt Cuối` must be present as bullet points. Use natural, plain Vietnamese. Do not write this as a dense paragraph.
- If already complete: `Đã hoàn thành full luồng; không còn blocker`.

## Rules

- Always show `Bug Open` and `Bug Closed` in the top summary.
- Always include the final roadmap section `Phương Án Để Hoàn Thành Full Luồng Chức Năng`.
- Always classify blockers with the full taxonomy; do not collapse everything into seed data.
- Include `Setup / Điều Kiện Cần Chuẩn Bị` when any remaining TC can run after QA/DBA/dev prepares data, account, file, mock, env, or time-travel conditions.
- Do not label a case `chờ BA confirm spec` until local SRS has been checked; use NotebookLM too if available.
- Any spec-based conclusion must cite exact local file path and line/section. NotebookLM can support, but local SRS is primary.
- Do not fabricate spec behavior.
- Separate blocked TC from failed TC.
- Separate workflow status from functional coverage.
- If no fresh UI/API verification was run, state that the audit is based on existing reports.
- The final summary must be short bullet points, easy for a human project lead to scan.
- Do not use `Ready`, `Conditional`, or `Not ready` in user-facing status. Use `Sẵn sàng`, `Có điều kiện`, or `Chưa sẵn sàng`.

## Invocation Examples

```text
Dùng qa-module-status-audit review trạng thái hiện tại của module <MODULE>: đã full luồng chưa, coverage hiện tại, bug open/closed, TC/path còn block, nguyên nhân và phương án để hoàn thành full.
```

```text
Use qa-module-status-audit for module <MODULE>. Read todo, state snapshot, workflow, functional, bug reports, and SRS local if needed. Report whether full workflow is complete and what remains to reach full completion.
```
