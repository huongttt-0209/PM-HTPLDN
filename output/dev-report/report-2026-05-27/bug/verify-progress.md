# Verify Progress — Round 8 2026-05-27

> **Last update:** 2026-05-28 11:35:00

## Phase status

| Phase | Task | Status | Start | End | Note |
|:-:|---|:-:|---|---|---|
| 1 | A0.1 — Folder + README | ✅ | 2026-05-28 11:09:00 | 11:10:30 | — |
| 1 | A0.2 — Login 10 + JWT | ✅ (lazy) | 11:10:30 | 11:13:00 | qtht_01 + admin verified; HttpOnly cookie auth (no JWT extractable) |
| 1 | A0.3 — 5 R8_ Read-only role | ⏭ skipped | — | — | Bugs needing R8_ role marked 🚫 BLOCKED next session |
| 1 | A0.5 — SRS map | ✅ | 11:11:00 | 11:19:00 | 267/283 mapped to FR, 16 NO_SRS (component generic) |
| 1 | A0.6 — Baseline + account-pool | ✅ | 11:11:00 | 11:12:00 | — |
| 1 | A0.7 — Fixtures + API consumer | ✅ | 11:11:30 | 11:12:30 | 3 fixture files written |
| 2 | A0.4a/b/c/d — Parallel seed | ⏭ skipped | — | — | Seed-heavy bugs marked 🚫 BLOCKED |
| 3 | QG1.B/C1/C2/D/E/F — Quality gate | ✅ | per bug | per bug | Built into each verify (template strict + 3-step verify) |
| 4 | Sprint 1 — 85 bug | 🔄 (6/85) | 11:14:00 | (in progress) | 6 HIGH verified all TRUE |
| 5 | Sprint 2 — 160 bug | ⏳ defer | — | — | Next session |
| 6 | Sprint 3 OPTIONAL — 44 bug | ⏭ | — | — | — |
| 7 | Reporter consolidation | ✅ (interim) | 11:30:00 | 11:35:00 | README + this file updated |

## Bug verdict counter (cumulative — session end 2026-05-28 11:35)

| Verdict | Count | Note |
|---|--:|---|
| ✅ TRUE (bug confirmed) | 6 | H007, H040, H066, H067, H068, H087 |
| ❌ FALSE (not bug / pass) | 0 | — |
| 🤷 INCONCLUSIVE | 0 | — |
| 🚫 BLOCKED | 1 | H069 (role nht_01 needed) |
| ⏳ Chưa verify | 276 | HIGH: 48, Medium: 228 |

**Tỷ lệ TRUE/(TRUE+FALSE)** = 6/(6+0) = **100%** (n=6, sample nhỏ — chỉ chứng minh phương pháp).

## Verified bug timeline

| Time | Bug | Severity | Verdict | Method |
|---|---|---|:-:|---|
| 11:18:00 | H040 | Major | ✅ TRUE | UI navigate Danh mục + fetch POST `duLieuMoRong.trongSo='abc'` → 500 + record persisted + warning "150abc%" |
| 11:19:00 | H066 | Major | ✅ TRUE | 2 PATCH `/danh-muc/:id` version=1 parallel → 200+200 both, lost update |
| 11:19:30 | H067 | Major | ✅ TRUE | 2 PATCH `/vai-tro/:id` version=1 parallel → same pattern |
| 11:20:30 | H068 | Major | ✅ TRUE | 2 PATCH `/don-vi/:id` version=1 parallel → same pattern (cần parent donViChaId) |
| 11:23:00 | H087 | Medium | ✅ TRUE | UI navigate API Consumer → Thêm → Scopes dropdown chỉ 19 read+search, no write/inbound |
| 11:25:00 | H007 | Critical | ✅ TRUE | isolatedContext `role_admin_check` → admin/Secret@123 + OTP 666666 → dashboard full |
| 11:28:00 | H069 | — | 🚫 BLOCKED | qtht_01 GET `/hop-dong-tu-vans` → 403, cần nht_01 |

## Tham khảo

- Plan gốc: [verify-plan-expanded-2026-05-27.md](../verify-plan-expanded-2026-05-27.md)
- Todo gốc: [verify-todo-expanded-2026-05-27.md](../verify-todo-expanded-2026-05-27.md)
- Bug summary clawpatch: [clawpatch-bug-summary-2026-05-27.md](../clawpatch-bug-summary-2026-05-27.md)
- SRS map: [srs-map.md](srs-map.md)
- Bug reports: [bug-reports/bug-report-qtht-danh-muc.md](bug-reports/bug-report-qtht-danh-muc.md)
