# Báo dev: 2 entity module Đào tạo chưa deploy

**Ngày:** 2026-05-09 20:33 (R9 verify) · **QA:** Claude Code MCP

## 1. HOC_VIEN (FR-III-NEW Mô hình A)

```
GET /api/v1/hoc-viens  → 404
GET /api/v1/hoc-vien   → 404
```

→ Entity chưa code. Cần tạo migration + entity + endpoint plural `/hoc-viens`.

## 2. LICH_HOC (FR-III-22)

```
GET /api/v1/lich-hocs  → 404  (plural)
GET /api/v1/lich-hoc   → 401  (singular, route exists)
```

→ Naming inconsistent. Các module khác đều plural (`khoa-hocs`, `bai-giangs`, `giang-viens`, `de-kiem-tras`, ...). Sửa thành `/lich-hocs` hoặc thêm alias.

## Impact

Block: **R7.3.12 + R7.3.13** + cascade **R7.4.B7 / B11 / B12** + **R7.7.6** functional cuối module.

## Reference

- [tasks/todo-dao-tao.md](../../../tasks/todo-dao-tao.md) — chi tiết task block
- [tasks/state-snapshot.md](../../../tasks/state-snapshot.md) — entity state hiện tại
