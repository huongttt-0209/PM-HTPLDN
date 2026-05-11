# Round 7 — Apply SRS update 2026-05-05 + partial reset DB (2026-05-06)

> **Lý do tồn tại:** Dev deploy 5 SRS update batch 2026-05-05 (FR-03 đào tạo, FR-04 CG/TVV/NHT/TC TV, FR-07 DN, FR-10 quản trị, FR-12 TVCS) + partial reset DB + **6 SRS v3.5 update 2026-05-06 batch 2** (FR-05 vụ việc, FR-06 chi trả, FR-08 đánh giá, FR-09 biểu mẫu, FR-12 TVCS đầy đủ stack, FR-16 API). Round 7 = re-seed Tier 0/1/2 cho actor mới + workflow E2E + functional 17 module + 2 NEW (NHT, TC TV) + cross-cutting + permission.

> **🆕 FR-06 Chi trả v3.5 PREP DONE 2026-05-06:** [funtion/7.6](../../funtion/7.6-chi-tra-chi-phi.md) (35 TC), [smoke/6.6](../../smoke/6.6-sm-chitra.md) (11 paths), R7.7.12 4 subtask sync. **2 BA Q chờ chốt** — [bug-reports/ba-questions-fr06-2026-05-06.md](bug-reports/ba-questions-fr06-2026-05-06.md): Q1 hành vi lần 4 bổ sung, Q2 SLA ngưỡng % deadline. Module BLOCKED end-to-end do thiếu LGSP integration. **R7.7.12.1 smoke regression IMPACT** (FR-07/08/11/13 × 5 phút) chạy được ngay.
> **Round 6 frozen:** [`../round6-2026-05-01-postreset/`](../round6-2026-05-01-postreset/) — frozen, làm history reference.
> **Plan trigger:** [`../../../tasks/plan-r7-trigger.md`](../../../tasks/plan-r7-trigger.md) · **Todo:** [`../../../tasks/todo.md`](../../../tasks/todo.md) · **Delta map:** [`../../../input/srs-update-2026-5-5/_DELTA-MAP-*.md`](../../../input/srs-update-2026-5-5/) · **Fixture:** v2.7.1

---

## 0. Tiền điều kiện (verify trước khi bắt đầu)

Đã verify 2026-05-06 — ghi log: [`bug-reports/deploy-gap/Pass-bug-report-audit-deploy-gap.md`](bug-reports/deploy-gap/Pass-bug-report-audit-deploy-gap.md).

| # | Check | Status | Note |
|:-:|---|---|---|
| 1 | App + BE up | ✅ | http://103.172.236.130:3000 |
| 2 | MailHog up | ✅ | http://103.172.236.130:8025 |
| 3 | qtht_01 login | ✅ | OTP 666666 bypass |
| 4 | cb_nv_tw_01 login | ✅ | OTP 666666 bypass |
| 5 | Sub-menu TC TV + NHT visible với CB_NV_TW | ✅ | Verified MCP 2026-05-06 |
| 6 | 8/18 deploy gap | ✅ **6/6 DEPLOY-* Closed** (5/6 R8 batch 2026-05-07: DEPLOY-001/002/004/005/006; DEPLOY-003 sidebar Đào tạo Closed R8 lần 3 2026-05-08 09:10 sau match SRS 6 sub-menu) + 2 false positive drop | [bug-report](bug-reports/deploy-gap/bug-report-audit-deploy-gap.md) |

> **R10 status (2026-05-10):** Tất cả 6 DEPLOY-* gap đã Closed. Block hiện tại = bug-level (không phải deploy-gap):
> - ~~**BUG-HV-BE-01 Major Open**~~ → **Closed R11 2026-05-11** (BE thay crash 500 bằng 403 guard đúng spec FR-III-04). 6 HV records đã có trong DB. Chuyên trang DN/NHT FR-III-04 (entry-point user thực) chưa test. [Detail](bug-reports/dao-tao/Pass-bug-report-r7-3-12-hoc-vien-deploy-partial.md)
> - Other module-specific bugs xem todo.md per task icon.

---

## Folder structure

```
round7-2026-05-06/
├── README.md                       (file này)
├── bug-reports/                    (bug-report-*.md per module)
│   └── deploy-gap/Pass-bug-report-audit-deploy-gap.md   (R7.0.2 — 6 bug verified)
├── seed/                           (seed-checklist-*.md per actor)
├── workflow/                       (workflow-test-report-*.md per Trụ A/B/C/D)
├── functional/                     (functional-test-report-*.md per module)
├── evidence/                       (output verify cross-module + KPI)
├── screenshots/                    (PNG evidence — relative path `../screenshots/...` từ bug file)
└── image/                          (image embed cho bug-reports — base64 hoặc relative)
```

---

## Phase plan tổng quan

| Phase | Việc | Status |
|:-:|---|---|
| 0 | Pre-test (deploy verify + bug gap + fixture + UI audit) | 🟢 in progress |
| 1 | Re-seed Tier 0 (DM/đơn vị/SLA/MPH/ngày lễ) | 🟢 ready |
| 2 | Re-seed Tier 1 (TC TV/DN/TVV/CG/NHT/account/PC) | ✅ done — NHT entity deployed R8, seeded R9-R10 (xem todo per task) |
| 3 | Re-seed Tier 2 (transactional state) | ⚠️ partial — Đào tạo 13/17 ✅ + 3 ⚠️ + 1 🚫 (R7.3.12 chờ BUG-HV-BE-01; R7.4.B10/B12/R7.7.6 ⚠️); module khác xem todo |
| 4 | Workflow E2E (Trụ A/B/C/D) | ⏳ chờ Phase 1-3 |
| 5 | Verification (KPI/cross/SLA/audit) | ⏳ chờ Phase 4 |
| 6 | Workflow đầu ra hậu kỳ (Chi trả/TVN/CT) | ⏳ chờ Phase 4 |
| 7 | Functional 17 module + 2 NEW (NHT/TC TV) | ⏳ chờ Phase 1-3 |
| 8 | Cross-cutting + Profile + Permission | 🟢 ready song song |

Chi tiết task: [`../../../tasks/todo.md` §Round 7](../../../tasks/todo.md).

---

## Bài học rút ra (cập nhật khi gặp sai)

- **2026-05-06:** Verify "UI element thiếu" phải dùng đúng role permission per SCR — không default QTHT all-access. False positive 2/8 bug deploy gap. [`tasks/lessons-learned.md` 2026-05-06](../../../tasks/lessons-learned.md). Memory: [`feedback_verify_ui_gap_role_permission.md`](../../../../../.claude/projects/-Users-teamai-Downloads-antigravity-QA-skilkk/memory/feedback_verify_ui_gap_role_permission.md).
