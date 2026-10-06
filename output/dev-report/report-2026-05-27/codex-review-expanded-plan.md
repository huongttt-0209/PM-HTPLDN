# Codex review — expanded plan 283 bug (2026-05-27)

> **Session:** 019e689d-02b5-7ae1-8129-4b2b375d733d
> **Files reviewed:** verify-plan-expanded-2026-05-27.md, verify-todo-expanded-2026-05-27.md, all-bugs-classified.json
> **Verdict:** **REVISE** — directionally workable, but not start-ready.

---

## Summary

The 283-bug scope can be QA-verified, but the current wall-time estimate is too optimistic, Agent C is overloaded, and several categories depend on missing seed/control hooks. Start only after fixing setup, blocking-data paths, and rebalance.

---

## Top 5 Critical Gaps

### 1. Setup/seed is a bottleneck

Agent A has 12h sequential setup for all others. If seed/account/env state is late or flaky, B-F idle or produce invalid results. **Split setup into parallel sub-tasks:**
- A0.x.1: auth/account validation
- A0.x.2: workflow seed
- A0.x.3: API token/session setup
- A0.x.4: MailHog OTP path verify
- A0.x.5: evidence folder/report template validation

### 2. Agent C is overloaded

117 UI workflow/form bugs at 50h is the biggest execution risk. These are state-machine-heavy and require click chains. **Split C immediately into C1 + C2:**
- **C1 Workflow state machines:** high-friction submit/approve/complete/reopen paths
- **C2 Forms/validation/UI persistence:** field loss, validation, edit/save, display bugs

### 3. Best-effort race bugs are underdefined

`H070` Payment validate state stale should remain **best-effort only if** the expected race behavior can be observed with curl retries and version conflicts. If the app gives no deterministic signal, mark **Dev-needed**, not QA. QA should not spend open-ended time proving nondeterministic races.

**Concrete rule:** cap best-effort retry = 50 attempts × 200ms gap. Nếu không repro stable → escalate Dev integration test.

### 4. Partial-QA needs a hard fallback rule

`M3` virus-flagged docs is **BLOCKED without DBA injection** if `trang_thai_quet=NHIEM` cannot be created through UI/API. **Fallback rule:**
- Verify visible behavior around available scan states (CHO_QUET, DA_QUET)
- Document missing precondition in `record-locks.md`
- Escalate DBA seed request as separate ticket
- **Do not burn QA time trying to fake DB-only states**

### 5. Bug report quality gate is missing

The 6-section Vietnamese template and wording rule need a pre-flight sample review. Otherwise 6 agents will create inconsistent reports that later need rework. **Require 2 accepted sample reports per agent before full-speed execution.**

---

## Effort Sanity Check

26-36h wall-time is **NOT realistic** as written.

A better estimate is **40-55h wall-time** with 6 agents, assuming environment stability and fast triage. Reasons:

- 14 state-machine modules require UI click chains
- 148 QA-UI bugs are not equal-effort; workflow bugs compound setup time
- API tests still need token/session/account setup and evidence capture
- Partial-QA/race bugs often create dead time waiting for DBA/dev clarification
- Report writing with 6-section template is nontrivial

**Cut scope if deadline is fixed:**

- **Sprint 1:** keep all 55 HIGH + only truly short top Mediums (15-20 bug only, not 30)
- **Sprint 2:** keep API + stable UI bulk
- **Sprint 3:** **DEFER** unless Sprint 1/2 finish cleanly

Do not commit Sprint 3 inside 36h wall-time.

---

## Sample Bug Classification

| Bug | Current | Codex verdict |
|---|---|---|
| **H037** Hoàn tất chấm điểm | QA-UI 30p | OK only if seed lands directly on scoring screen. If login/navigation included, bump to **45-60p** |
| **H043** submitResult override | QA-UI 1h30 | OK. Stateful enough |
| **H070** Payment race | best-effort 2h+ | OK **only with capped retry plan** (≤50 attempts). Else → Dev-needed |
| **M3** Virus-flagged | Partial-QA 1-2h | Correct. Without DBA inject → **BLOCKED**, not failed QA |

---

## Agent Rebalance — Recommended 7-agent shape

| Agent | Focus | Bug count target |
|---|---|--:|
| **A** | Setup/Seed + unblock queue | 10 task |
| **B** | Auth/Permission UI | 31 |
| **C1** | Workflow UI (state machine paths) | ~60 |
| **C2** | Form/UI persistence (validation, edit/save) | ~57 |
| **D** | Cross-role/cross-tenant | 21 |
| **E** | API curl | 81 |
| **F** | Partial-QA/race/escalation evidence | 33 |

With 6 agents, **merge F into A** after setup, but expect longer wall-time.

---

## Risk Register

1. **Environment/data instability**
   App at `http://103.172.236.130:3000/` may not preserve test state across agents. **Escalate need for reset/seed ownership before start.**

2. **DBA dependency blocks Partial-QA**
   Bugs like M3 requiring DB-only states cannot be fully verified without DBA support. **Escalate as scheduled dependency.**

3. **False negatives from state-machine shortcuts**
   Since 14 modules require UI click chains, any shortcut via POST risks invalid QA. **Enforce UI path for state bugs (memory `feedback_test_method_ui_only`).**

4. **Evidence/report rework**
   If agents prescribe fixes like buttons/endpoints/error codes instead of requirements, reports will fail PM review. **Add report QA gate (2 sample reports per agent reviewed before full execution).**

5. **Parallel agent collision**
   Six agents using shared accounts/data can overwrite each other's workflow states. **Assign account pools and object ownership per agent before execution (record-locks.md mandatory).**

---

## Bottom Line

**Revise before start.** The scope is feasible, but not in 26-36h with the current staffing and assumptions. Split Agent C, define BLOCKED/Dev-needed rules for H070/M3-style cases, and **treat Sprint 3 as optional** unless Sprints 1-2 finish cleanly.

---

## Action items (apply before user approve)

- [ ] Split Agent C → C1 (workflow) + C2 (form/UI persistence) — rebalance ~60 + ~57 bug
- [ ] Add cap-retry rule for best-effort race (50 attempts × 200ms)
- [ ] Add Partial-QA BLOCKED fallback rule (no DB-state-faking)
- [ ] Add 2-sample-report quality gate per agent before full execution
- [ ] Re-estimate wall-time: 26-36h → **40-55h realistic**
- [ ] Mark Sprint 3 OPTIONAL — only run if Sprint 1+2 finish clean
- [ ] Split A0 setup into parallel sub-tasks (auth / seed / API token / OTP / template)
- [ ] Document account-pool/object-ownership per agent in record-locks.md
