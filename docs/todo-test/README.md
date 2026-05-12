# Master TODO test — PM HTPLDN — 18 module

> **Generated:** 2026-05-12 22:15:00 (Phase 4 — Aggregator)
> **Workflow:** xem [plan.md](plan.md) (Phase 0-4) · Module classification matrix: [_meta/module-matrix.md](_meta/module-matrix.md) · Cross-module review summary: [_meta/codex-review-summary.md](_meta/codex-review-summary.md)
> **Total:** 320 task across 18 module, 7513 dòng test plan, 1052 dòng review.
> **List nguồn:** [list-module.md](list-module.md) · 16 FR + 2 cross-cutting.

---

## Quick link — 18 module (order theo tầng 1 → 5)

| # | Slug | FR | Tên module | Tầng | Nhóm Rule 4 | Complexity | Tasks | Plan | Review | Todo |
|:-:|---|:-:|---|:-:|:-:|:-:|:-:|---|---|---|
| 1 | `fr-10-qtht` | FR-10 | Quản trị hệ thống | 1 | A | L | 18 | [plan](fr-10-qtht/test-plan.md) | [review](fr-10-qtht/review.md) | [todo](fr-10-qtht/todo.md) |
| 2 | `fr-07-doanh-nghiep` | FR-07 | Doanh nghiệp | 2 | B | M | 13 | [plan](fr-07-doanh-nghiep/test-plan.md) | [review](fr-07-doanh-nghiep/review.md) | [todo](fr-07-doanh-nghiep/todo.md) |
| 3 | `fr-04-chuyen-gia-tvv` | FR-04 | CG/TVV/NHT/TC-TV | 2 | A | L | 21 | [plan](fr-04-chuyen-gia-tvv/test-plan.md) | [review](fr-04-chuyen-gia-tvv/review.md) | [todo](fr-04-chuyen-gia-tvv/todo.md) |
| 4 | `fr-09-bieu-mau` | FR-09 | Biểu mẫu | 2 | B | M | 13 | [plan](fr-09-bieu-mau/test-plan.md) | [review](fr-09-bieu-mau/review.md) | [todo](fr-09-bieu-mau/todo.md) |
| 5 | `fr-15-ct-htpldn` | FR-15 | CT HTPLDN GĐ1 (KH) + GĐ2 (Đợt BC) | 2+5 | C | M | 15 | [plan](fr-15-ct-htpldn/test-plan.md) | [review](fr-15-ct-htpldn/review.md) | [todo](fr-15-ct-htpldn/todo.md) |
| 6 | `ho-so-doi-mat-khau` | cross | Hồ sơ + đổi mật khẩu | — | A | S | 14 | [plan](ho-so-doi-mat-khau/test-plan.md) | [review](ho-so-doi-mat-khau/review.md) | [todo](ho-so-doi-mat-khau/todo.md) |
| 7 | `cross-cutting-permission` | cross | Permission matrix + state machine | — | A | M | 25 | [plan](cross-cutting-permission/test-plan.md) | [review](cross-cutting-permission/review.md) | [todo](cross-cutting-permission/todo.md) |
| 8 | `fr-05-vu-viec` | FR-05 | Vụ việc TGPL | 3 | A | XL | 30 | [plan](fr-05-vu-viec/test-plan.md) | [review](fr-05-vu-viec/review.md) | [todo](fr-05-vu-viec/todo.md) |
| 9 | `fr-02-hoi-dap` | FR-02 | Hỏi đáp | 3 | A | L | 19 | [plan](fr-02-hoi-dap/test-plan.md) | [review](fr-02-hoi-dap/review.md) | [todo](fr-02-hoi-dap/todo.md) |
| 10 | `fr-12-tv-chuyen-sau` | FR-12 | Tư vấn pháp luật chuyên sâu | 3 | B | L | 12 | [plan](fr-12-tv-chuyen-sau/test-plan.md) | [review](fr-12-tv-chuyen-sau/review.md) | [todo](fr-12-tv-chuyen-sau/todo.md) |
| 11 | `fr-03-dao-tao` | FR-03 | Đào tạo (4 sub-menu) | 3 | B | L | 20 | [plan](fr-03-dao-tao/test-plan.md) | [review](fr-03-dao-tao/review.md) | [todo](fr-03-dao-tao/todo.md) |
| 12 | `fr-14-hop-dong-tv` | FR-14 | Hợp đồng tư vấn | 4 | C | M | 12 | [plan](fr-14-hop-dong-tv/test-plan.md) | [review](fr-14-hop-dong-tv/review.md) | [todo](fr-14-hop-dong-tv/todo.md) |
| 13 | `fr-06-chi-tra` | FR-06 | Chi trả chi phí | 4 | A | XL | 33 | [plan](fr-06-chi-tra/test-plan.md) | [review](fr-06-chi-tra/review.md) | [todo](fr-06-chi-tra/todo.md) |
| 14 | `fr-13-tv-nhanh` | FR-13 | TV nhanh — Phiên + Kho QA | 4 | A | L | 13 | [plan](fr-13-tv-nhanh/test-plan.md) | [review](fr-13-tv-nhanh/review.md) | [todo](fr-13-tv-nhanh/todo.md) |
| 15 | `fr-08-danh-gia-hq` | FR-08 | Theo dõi Đánh giá HQ HTPL | 4 | A | L | 18 | [plan](fr-08-danh-gia-hq/test-plan.md) | [review](fr-08-danh-gia-hq/review.md) | [todo](fr-08-danh-gia-hq/todo.md) |
| 16 | `fr-11-bao-cao` | FR-11 | Báo cáo 23 loại | 5 | D | M | 15 | [plan](fr-11-bao-cao/test-plan.md) | [review](fr-11-bao-cao/review.md) | [todo](fr-11-bao-cao/todo.md) |
| 17 | `fr-01-dashboard` | FR-01 | Dashboard 9 KPI + 2 chart | 5 | C | M | 16 | [plan](fr-01-dashboard/test-plan.md) | [review](fr-01-dashboard/review.md) | [todo](fr-01-dashboard/todo.md) |
| 18 | `fr-16-api` | FR-16 | API kết nối Cổng PLQG | 5 | D | M | 13 | [plan](fr-16-api/test-plan.md) | [review](fr-16-api/review.md) | [todo](fr-16-api/todo.md) |
| **Tổng** | | | | | | | **320** | | | |

---

## Batch execution order (Phase 1 draft batch — informational)

### Batch A — Tầng 1+2 foundation (5 module, 80 task)
- `fr-10-qtht` (18) → `fr-07-doanh-nghiep` (13) → `fr-04-chuyen-gia-tvv` (21) → `fr-09-bieu-mau` (13) → `fr-15-ct-htpldn` (15)
- **Mục đích:** Master data + DM dùng chung + actor seed. Phải xong trước Tầng 3 vì cung cấp dropdown/role/đơn vị/lĩnh vực.

### Batch B — Tầng 3 + cross (5 module, 100 task)
- `fr-05-vu-viec` (30) → `fr-02-hoi-dap` (19) → `fr-12-tv-chuyen-sau` (12) → `fr-03-dao-tao` (20) → `ho-so-doi-mat-khau` (14) → `cross-cutting-permission` (25)
- *Ghi chú:* Plan gốc liệt kê 5 module Tầng 3 + cross-cutting đẩy sang Batch B/C. Plan thực tế đã include `cross-cutting-permission` trong Batch C — tổng task của 5 module Batch B (không gồm cross) = 95. Cross-cutting đếm riêng 25.

### Batch C — Tầng 4 + cross-cutting (5 module, 88 task)
- `fr-14-hop-dong-tv` (12) → `fr-06-chi-tra` (33) → `fr-13-tv-nhanh` (13) → `fr-08-danh-gia-hq` (18) → `cross-cutting-permission` (25 — counted ở Batch B summary)
- **Tổng task Batch C không trùng cross:** 12+33+13+18 = 76 (cross-cutting 25 đếm 1 lần ở Batch B).

### Batch D — Tầng 5 output (3 module, 44 task)
- `fr-11-bao-cao` (15) → `fr-01-dashboard` (16) → `fr-16-api` (13)
- **Mục đích:** Module aggregate đọc data từ MỌI upstream. Phải xong cuối cùng để có data thật để verify KPI/báo cáo/API outbound.

> Tổng cộng 4 batch = 320 task (Batch A 80 + Batch B core 95 + cross-cutting 25 + Batch C non-cross 76 + Batch D 44 = 320).

---

## Cross-cutting reference

- [Permission matrix 11 role × 49 entity](../../output/permission-matrix.md)
- [Test strategy](../../output/test-strategy.md)
- [Entity map cross-module](../../input/data/entity-map.md)
- [Seed fixture (YAML)](../../input/data/seed-fixture.yaml)
- [Flow state machine 14 module](../../input/flow-module.md) — bao gồm Phụ lục 2 Seed Presets + Phụ lục 3 Troubleshooting
- [Test accounts (users.csv)](../../input/users.csv) · [Permission test isolation](../../input/test-accounts-isolation.csv)

---

## Workflow tóm tắt

1. **Phase 0 — Discovery + classification.** Đọc list-module + system-overview §4 + 02-thu-tu-module → sinh `_meta/module-matrix.md` (18 module × { tầng, FR, SCR, v3.5 status, nhóm Rule 4 A/B/C/D, complexity, SRS path, upstream cần seed }).
2. **Phase 1 — Test plan drafting (4 batch parallel, ~3-4 giờ).** 18 subagent general-purpose, mỗi subagent đọc SRS v3 + v3.5 riêng của module, draft test-plan.md theo template Full 6 section.
3. **Phase 2 — Self-review (agent-skills:code-reviewer).** Codex pre-flight bị user interrupt → fallback Claude self-review. Output `review.md` structured: ## Gaps · ## Suggestions · ## Verdict (APPROVE/REVISE).
4. **Phase 3 — Revise + sinh todo.md per module.** Subagent đọc test-plan + review, apply ≥80% gap, sinh todo.md theo convention CLAUDE.md (≤25 từ Kết quả, dòng `**Bug:**` khi có bug, icon ✅⚠️🚫⏳🟢🔵).
5. **Phase 4 — Master index (file này) + codex-review-summary.** Aggregate stats + Top pattern gap cross-module + BA-Q tracker + env infra blocker.

---

## Nhóm Rule 4 cheat sheet (informational — cho tester pick up sau Phase 4)

| Nhóm | Ý nghĩa | Hành động khi pick up |
|:-:|---|---|
| **A FULL** | Module có file SRS v3.5 đụng MỚI (rename, lifecycle mới, feature mới) | Test FULL — workflow + functional + permission + edge + state machine |
| **B DELTA+IMPACT** | Có v3.5 update nhưng impact giới hạn | Test phần delta đầy đủ + sample workflow happy path + sample permission |
| **C IMPACT only** | KHÔNG có file v3.5 riêng nhưng chịu impact cross-cutting (UC renumber, hard-delete, 5 trường công khai) | Sample 2-3 màn đại diện + smoke permission |
| **D SKIP / smoke** | Module ổn định, không update v3.5 | Smoke 5 phút verify login + render |

Source: CLAUDE.md user-level "Rule 4 — Khi nhận SRS update".

**Phân bố 18 module theo nhóm:**
- **A FULL (8):** fr-10-qtht · fr-04-chuyen-gia-tvv · fr-05-vu-viec · fr-02-hoi-dap · fr-13-tv-nhanh · fr-08-danh-gia-hq · fr-06-chi-tra · ho-so-doi-mat-khau · cross-cutting-permission (9 actually — A nhóm chung 9 module)
- **B DELTA (4):** fr-07-doanh-nghiep · fr-09-bieu-mau · fr-12-tv-chuyen-sau · fr-03-dao-tao
- **C IMPACT (3):** fr-15-ct-htpldn · fr-14-hop-dong-tv · fr-01-dashboard
- **D SKIP (2):** fr-11-bao-cao · fr-16-api

---

## Cách dùng cho tester onboard mới

1. Đọc `plan.md` để hiểu workflow Phase 0-4.
2. Đọc `_meta/module-matrix.md` để biết module nào tầng nào + dep upstream.
3. Đọc `_meta/codex-review-summary.md` để biết Top gap cross-module + BA-Q chờ confirm + env blocker.
4. Chọn module cần test → mở `<slug>/test-plan.md` (6 section) → `<slug>/review.md` (gap chi tiết) → `<slug>/todo.md` (tracker tasks).
5. Theo CLAUDE.md "Tool routing" — dùng Chrome DevTools MCP làm tool mặc định.
6. Khi PASS task → update todo.md theo workflow `feedback_todo_update_after_run` (flip icon + state-snapshot.md + dep gate).

---

*Generated by Aggregator subagent — Phase 4 final, 2026-05-12. 18/18 module có đủ 3 file (test-plan + review + todo) — tổng 320 task ready cho Round 1 execute.*
