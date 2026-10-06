# Baseline — Round 8 2026-05-27

## App version

| Item | Giá trị | Source |
|---|---|---|
| Frontend stack | React + Vite + AntD v5 | `packages/web/package.json` |
| App URL | http://103.172.236.130:3000 | CLAUDE.md |
| API base | http://103.172.236.130:3000/api/v1 | CLAUDE.md |
| MailHog inbox | http://103.172.236.130:8025 | CLAUDE.md |
| OTP bypass | `666666` (verified 2026-04-21) | CLAUDE.md MCP-Template login |
| Verify date | 2026-05-28 | Today |

## 6-agent ownership table (Phase 4-5 parallel)

| Agent | Owns account | Module focus |
|:-:|---|---|
| B (HIGH QA-UI 7 bug + Medium UI 24 bug) | `qtht_01` + `qtht_02` | Auth, layout, common UI |
| C1 (HIGH 38 split) | `cb_nv_tw_01` | TW-level data + roles |
| C2 (HIGH 38 split) | `cb_nv_tw_02` | TW-level data + roles |
| D (HIGH cross-tenant 7 bug + Medium cross-role 14 bug) | `cb_nv_dp_01` + `cb_nv_dp_02` | Cross-tenant 2-tab |
| E (HIGH 26 API + Medium 51 API) | API consumer + qtht_01 (UI) | API contract via MCP evaluate_script |
| F (HIGH 7 race + Medium 26 race) | tvv_01 + tvv_02 + admin | Race + Partial-QA |

## Record-locks init (empty — populated as agents claim)

```
# record-locks
# Format: entity_type:entity_id => agent_id (timestamp)
```

## API consumer credential

> Đặt trong `.private/api-consumer-tokens.txt` (gitignored). Auto-refresh qua MailHog OTP helper (MailHog API v2).

## SRS version

- Default: `input/srs-update-2026-5-5/` v3.5
- Fallback: `input/srs-v3/` (legacy)
- CHANGELOG: `input/srs-update-2026-5-5/CHANGELOG-v3-to-v3.5.md`

## Verify methodology constraints

1. **Browse UI Chrome DevTools MCP only** — primary tool (`mcp__chrome-devtools__*`)
2. **CẤM curl direct** — API verify dùng `evaluate_script(() => fetch(...))` trong authenticated session
3. **3-step verify TRƯỚC log bug:** (1) SRS version đúng, (2) quote nguyên văn line số, (3) cross-method UI↔fetch
4. **Screenshot inline base64** trong bug-report (Critical/Major Active)
5. **6 sections strict** trong bug entry — không Tác động / Đề xuất fix
