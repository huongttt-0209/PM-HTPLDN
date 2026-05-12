# TODO — fr-16-api — API kết nối Cổng PLQG

> **Module:** FR-16 (Nhóm XII) · **Phân nhóm SRS v3.5:** Nhóm D SKIP / Smoke 5 phút mỗi đợt upstream update · **Tier:** 5 (chạy sau cùng) · **No UI / No state machine** — toàn bộ TC chạy qua curl + k6 + pytest.
> **Test plan:** [test-plan.md](./test-plan.md) v1.1 · **Tổng TC**: 67 (live testable round 1: 59 sau khi mTLS sandbox provisioned + 8 inbound BLOCKED nhóm B).
> **Đặc thù:** Mọi task phụ thuộc 3 prereq infra — `mTLS sandbox provisioned` + `JWT issuance flow ready (TC-AUTH-00 PASS)` + `9 upstream module có state cuối seed đủ`. Block do env phổ biến — mark `[need: env mTLS sandbox provisioned (✗ chờ Infra)]` rõ ràng.

---

## Icon column meaning

| Icon | Nghĩa |
|:-:|---|
| 🟢 | Sẵn sàng chạy — mọi dep đã ✓ |
| ⏳ | Chờ dep upstream (chưa thoả) |
| 🚫 | Block cứng (chờ BA confirm spec / env infra) |
| ✅ | Đã PASS clean |
| ⚠️ | PASS có Minor / Sai spec |
| ❌ | FAIL — log bug |
| 🤷 | Không xác định — cần retry method |

---

## Round 1 — Active task tracker

### Group A — Prerequisite infra + auth flow (P0, làm trước)

- 🚫 **T-FR16-001** Verify mTLS sandbox + base URL dev sẵn sàng
  - **Kết quả:** TBD — chưa chạy round
  - **Cần có sẵn:** [need: mTLS sandbox endpoint deployed `https://htpldn-dev.moj.gov.vn/api/v1` + test cert `cert/consumer-test.crt`+`.key` cấp xong (✗ chờ Infra + Dev BE)]
  - **Output:** docs/todo-test/fr-16-api/results/round1/

- 🚫 **T-FR16-002** TC-AUTH-00 — Cấp JWT happy flow (prereq mọi TC sau)
  - **Kết quả:** TBD — chưa chạy round
  - **Cần có sẵn:** [need: T-FR16-001 ✓ + JWKS endpoint URL từ Dev BE (✗ ambiguity #1 deadline 2026-05-19) + `POST /api/v1/auth/token` spec confirmed]
  - **Output:** docs/todo-test/fr-16-api/results/round1/

- 🚫 **T-FR16-003** TC-AUTH-01..08 — 8 negative auth (no JWT/expired/sig/scope/mTLS/issuer/algorithm/missing-claim)
  - **Kết quả:** TBD — chưa chạy round
  - **Cần có sẵn:** [need: T-FR16-002 ✓ + `scripts/gen-jwt.sh` để generate JWT variant (✗ chờ tool)]
  - **Output:** docs/todo-test/fr-16-api/results/round1/

### Group B — 9 outbound list + search happy (P0)

- ⏳ **T-FR16-004** TC-OUT-HD/DT/TVV/VV/DG/BM/TVCS/CT/DN list + search (18 TC)
  - **Kết quả:** TBD — chưa chạy round
  - **Cần có sẵn:** [need: T-FR16-002 ✓ + ≥3 record state cuối mỗi entity từ 9 upstream module (✗ chờ FR-02/03/04/05/08/09/12/15/07 seed-advance ≥1 entity); env mTLS sandbox provisioned (✗ chờ Infra)]
  - **Output:** docs/todo-test/fr-16-api/results/round1/

### Group C — Compliance + security (P0)

- ⏳ **T-FR16-005** TC-FILTER-01..09 — BR-INTG-07 state filter (draft KHÔNG hiện)
  - **Kết quả:** TBD — chưa chạy round
  - **Cần có sẵn:** [need: T-FR16-004 ✓ + mỗi entity có MIX state (≥3 publishable + ≥2 draft/chờ duyệt) để chứng minh filter loại trừ (✗ chờ upstream seed mix-state)]
  - **Output:** docs/todo-test/fr-16-api/results/round1/

- ⏳ **T-FR16-006** TC-OUT-TVV-03/VV-03/TVCS-03 — BR-SEC-01 exclude PII/MST/metadata whitelist
  - **Kết quả:** TBD — chưa chạy round
  - **Cần có sẵn:** [need: T-FR16-004 ✓ + sample TVV có CMND/CCCD/SĐT field, VV có MST DN, TVCS có nội dung chi tiết (✗ chờ FR-04/05/12 seed full field)]
  - **Output:** docs/todo-test/fr-16-api/results/round1/

- ⏳ **T-FR16-007** TC-AUDIT-01..04 — Audit log INSERT + error path + consumer_id + latency_ms
  - **Kết quả:** TBD — chưa chạy round
  - **Cần có sẵn:** [need: T-FR16-003 ✓ + endpoint admin `GET /api/admin/audit-log` hoặc DBA approve SELECT AUDIT_LOG (✗ ambiguity S8 pre-check); ambiguity #9 latency_ms field confirmed (✗ chờ Dev BE)]
  - **Output:** docs/todo-test/fr-16-api/results/round1/

### Group D — Rate limit + performance (P0/P1)

- ⏳ **T-FR16-008** TC-RATE-01..04 — 100 req/min + 429 + reset window + scope
  - **Kết quả:** TBD — chưa chạy round
  - **Cần có sẵn:** [need: T-FR16-002 ✓ + k6 tool installed + ambiguity #8 rate window confirmed (✗ chờ BA + Dev BE); env mTLS sandbox provisioned]
  - **Output:** docs/todo-test/fr-16-api/results/round1/

- ⏳ **T-FR16-009** TC-PERF-01..03 — p95 list + concurrent 50 VU + search latency p99
  - **Kết quả:** TBD — chưa chạy round
  - **Cần có sẵn:** [need: T-FR16-004 ✓ + ≥100 record/endpoint để load test có ý nghĩa (✗ chờ upstream seed ≥100); k6 tool installed]
  - **Output:** docs/todo-test/fr-16-api/results/round1/

### Group E — Payload edge (P1/P2)

- ⏳ **T-FR16-010** TC-PAG-01..07 + TC-SEARCH-01..02 + TC-DATE-01..02 (12 TC payload edge)
  - **Kết quả:** TBD — chưa chạy round
  - **Cần có sẵn:** [need: T-FR16-004 ✓ — chỉ cần 1 endpoint outbound hoạt động để probe pagination/search/date edge]
  - **Output:** docs/todo-test/fr-16-api/results/round1/

- ⏳ **T-FR16-011** TC-OUT-BM-DL-01..02 — Download endpoint + binary integrity
  - **Kết quả:** TBD — chưa chạy round
  - **Cần có sẵn:** [need: T-FR16-004 ✓ + ≥1 BIEU_MAU `la_cong_khai=1` có file upload thật PDF/DOCX (✗ chờ FR-09 seed file upload); ambiguity scope download (`:read` vs `:download`) confirmed]
  - **Output:** docs/todo-test/fr-16-api/results/round1/

### Group F — Defer / Block (P2)

- 🚫 **T-FR16-012** TC-IN-01..08 — 8 inbound endpoint (BLOCKED nhóm B)
  - **Kết quả:** TBD — Defer chờ 3 unblock condition mỗi endpoint
  - **Cần có sẵn:** [need: (a) BA confirm LGSP envelope format (✗ ambiguity #3 deadline 2026-05-26); (b) Dev BE deploy sandbox 8 inbound endpoint (✗ chờ Dev BE); (c) Sample client cert + signing key cấp QA (✗ chờ Infra)]
  - **Output:** docs/todo-test/fr-16-api/results/round1/

- 🚫 **T-FR16-013** Verify auto-push event-driven outbound (nếu có)
  - **Kết quả:** TBD — Defer chờ ambiguity #6 BA + CĐT
  - **Cần có sẵn:** [need: BA + CĐT confirm có cơ chế push event-driven hay không (event bus / webhook / cron polling) — ambiguity #6 deadline 2026-05-19 (✗ chờ BA + CĐT); nếu có, cần spec endpoint Cổng PLQG receiver]
  - **Output:** docs/todo-test/fr-16-api/results/round1/

---

## Bảng tiến độ (auto-recount sau mỗi Edit)

| Trạng thái | Count | Note |
|:-:|---:|---|
| 🟢 Sẵn sàng | 0 | — |
| ⏳ Chờ dep | 8 | T-FR16-004..011 chờ upstream seed + auth prereq + env infra |
| 🚫 Block | 5 | T-FR16-001..003 (env+auth prereq) + T-FR16-012 (inbound spec) + T-FR16-013 (auto-push spec) |
| ✅ Done | 0 | Chưa chạy round |
| ⚠️ Partial | 0 | — |
| ❌ Fail | 0 | — |
| **Tổng** | **13** | |

---

## Phân loại block (theo nhóm A-F CLAUDE.md)

| Task | Nhóm | Vì sao | Cần làm gì | Ai làm |
|---|:-:|---|---|:-:|
| T-FR16-001 | D | mTLS sandbox + base URL dev chưa provisioned | Infra cấp cert + endpoint dev | Infra + Dev BE |
| T-FR16-002 | C | Auth flow ambiguity #1 — JWKS endpoint chưa rõ | BA + Dev BE confirm flow spec | BA + Dev BE |
| T-FR16-003 | C/D | Phụ thuộc T-FR16-002 + tool gen-jwt.sh chưa có | Dev tooling | QA API |
| T-FR16-004 | E | Chờ 9 upstream module seed state cuối | Chạy seed-advance ở FR-02/03/04/05/08/09/12/15/07 | QA seed |
| T-FR16-005 | E | Chờ upstream seed mix-state (cả publishable + draft) | Bổ sung seed draft 2-3 record/entity | QA seed |
| T-FR16-006 | E | Chờ FR-04/05/12 seed full field PII/MST/nội dung | Seed-advance đủ field schema | QA seed |
| T-FR16-007 | C | Audit endpoint admin chưa rõ + ambiguity #9 latency_ms | Dev BE confirm endpoint + field | Dev BE |
| T-FR16-008 | C | Ambiguity #8 rate window + scope chưa rõ | BA + Dev BE confirm policy | BA + Dev BE |
| T-FR16-009 | E | Cần ≥100 record/endpoint cho load test | Seed bulk upstream | QA seed |
| T-FR16-010 | E | Chỉ chờ 1 endpoint outbound hoạt động | Chờ T-FR16-004 | QA API |
| T-FR16-011 | E/C | Chờ FR-09 seed file upload thật + scope download confirm | Seed BM có file + Dev BE confirm scope | QA seed + Dev BE |
| T-FR16-012 | C | 8 inbound BLOCKED — không có spec LGSP | BA confirm + Dev BE deploy sandbox + Infra cấp cert | BA + Dev BE + Infra |
| T-FR16-013 | C | Ambiguity #6 — auto-push event-driven có hay không | BA + CĐT clarify | BA + CĐT |

> **Defer >2 round nhóm F escalate user lead** (CLAUDE.md). Hiện chưa có task nào nhóm F — T-FR16-012/013 là nhóm C chờ BA, không phải out-of-scope.
