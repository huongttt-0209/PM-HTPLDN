# A5 Traceability Matrix — Nhật ký Hệ thống (FR-VIII-28)

> **Module**: QTHT Nhật ký Hệ thống
> **Ngày chạy**: 2026-05-08
> **Skill**: bmad-testarch-trace (manual)
> **Output**: Matrix BR/AC/Error/Permission ↔ TC. Phát hiện gap → forward A6 fix inline.

---

## 1. BR Coverage

| BR | Mô tả | Source | TC cover | Coverage |
|----|-------|--------|----------|----------|
| BR-AUTH-01 | Authentication + chỉ QTHT | srs-fr-10:1343, 1372; srs-v3.1.md §B.1 | TC-NK-101 (precondition), TC-NK-PERM-001..007 | ✅ 100% |
| BR-DATA-05 | AUDIT_LOG immutable, INSERT-only | srs-v3.1.md:5330; srs-fr-10:1828 | TC-NK-EXP-004 (audit-of-export), TC-NK-141, TC-NK-142, TC-NK-PERM-008, TC-NK-PERM-009 | ✅ 100% |
| BR-DATA-06 | Export Excel max 10.000 rows | srs-v3.1.md:5331; srs-fr-10:1348, 1371 | TC-NK-EXP-007/008/009/010 | ✅ 100% |
| BR-DATA-07 | Pagination default 20, max 100 (50/page custom) | srs-v3.1.md:5332; srs-fr-10:1824 | TC-NK-110, TC-NK-111 | ✅ 100% |
| BR-EC-13 | Search sanitize max 200 + escape SQL/XSS | srs-v3.1.md:5471 | TC-NK-130, TC-NK-131, TC-NK-132 | ✅ 100% |
| **Constraint 90 ngày (v3.1)** | `den - tu <= 90 ngày` + ERR-LOG-02 | srs-fr-10:1344, 1363 | TC-NK-120, TC-NK-134/135/136, TC-NK-EXP-006 | ✅ 100% |

**Total BR coverage: 6/6 = 100%** ✅ (target ≥95%)

---

## 2. AC Coverage (3 AC SRS)

| AC | Mô tả | Source | TC cover | Coverage |
|----|-------|--------|----------|----------|
| AC1 | QTHT lọc theo thời gian → log phân trang 50/page | srs-fr-10:1370 | TC-NK-101, TC-NK-102, TC-NK-110, TC-NK-PERM-001 | ✅ |
| AC2 | QTHT nhấn Xuất Excel → file .xlsx max 10K | srs-fr-10:1371 | TC-NK-EXP-001, TC-NK-EXP-002, TC-NK-EXP-008, TC-NK-PERM-002 | ✅ |
| AC3 | Non-QTHT → từ chối truy cập | srs-fr-10:1372 | TC-NK-PERM-003..007, TC-NK-123 (empty distinct) | ✅ |

**Total AC coverage: 3/3 = 100%** ✅

---

## 3. Error Code Coverage

| Error code | Severity | Source | TC cover | Coverage |
|------------|----------|--------|----------|----------|
| ERR-LOG-01 | ERROR | srs-fr-10:1362 | TC-NK-PERM-003..006 | ✅ |
| ERR-LOG-02 | WARNING | srs-fr-10:1363 | TC-NK-120, TC-NK-136, TC-NK-EXP-006 | ✅ |

**Total Error code coverage: 2/2 = 100%** ✅

---

## 4. Permission Combo Coverage

| Role × Action | TC cover | Coverage |
|--------------|----------|----------|
| QTHT × Read | TC-NK-PERM-001 | ✅ |
| QTHT × Export | TC-NK-PERM-002 | ✅ |
| QTHT × Delete/Update AUDIT_LOG | TC-NK-PERM-008, TC-NK-PERM-009 (cả UI + BE) | ✅ (KHÔNG được phép — verify reject) |
| CB_NV (TW/BN/DP) × Read | TC-NK-PERM-003, 004, 005 | ✅ |
| CB_PD (TW/BN/DP) × Read | TC-NK-PERM-006 | ✅ |
| Tier 2 (DN/CG/TVV/NHT) × Read | TC-NK-PERM-007 | ✅ |

**Total Permission combo: 6/6 = 100%** ✅

---

## 5. Filter Field Coverage (Inputs SRS line 1331-1338 + SCR-VIII-10 #7)

| Field | TC cover | Coverage |
|-------|----------|----------|
| `thoi_gian_tu` / `thoi_gian_den` | TC-NK-101, 102, 120-122, 134-137 | ✅ |
| `nguoi_dung` (searchable) | TC-NK-103, 138, 139 | ✅ |
| `module` | TC-NK-104, 107 | ✅ |
| `hanh_dong` | TC-NK-105, 107 | ✅ |
| `entity` filter (NHATKY-02 RESOLVED: NOT a filter) | TC-NK-106 (verify NOT exist) — sanitize redirect 130-133 sang dropdown người dùng | ✅ (negative coverage) |

**Total Filter coverage: 5/5 = 100%** ✅

---

## 6. Output Column Coverage (SCR-VIII-10 #9 — 8 cột)

| Cột | TC cover | Coverage |
|-----|----------|----------|
| Thời gian (sortable) | TC-NK-108, TC-NK-111 | ✅ |
| Người dùng (ho_ten) | TC-NK-103 | ✅ |
| Đơn vị | TC-NK-PERM-001 | ✅ |
| Module | TC-NK-104 | ✅ |
| Entity (cột bảng output) | TC-NK-106 (verify Entity KHÔNG là filter input) + TC-NK-101 (cột bảng) | ✅ |
| Mã bản ghi | (implicit qua filter entity) | ⚠️ partial — chưa có TC riêng verify cột (gap → A6 #1) |
| Loại thao tác (badge color) | TC-NK-105, TC-NK-140 | ✅ (color verify partial — gap → A6 #2) |
| Chi tiết thay đổi (JSON expand) | TC-NK-109 | ✅ |

**Total Output column coverage: 6/8 = 75% explicit + 8/8 = 100% implicit**

---

## 7. SM Coverage — N/A (read-only entity)

---

## 8. State / Persistence

| Aspect | TC cover |
|--------|----------|
| URL query param round-trip (filter persist qua reload) | TC-NK-102, 107 |
| Pagination URL state | TC-NK-110 |
| Reset filter | TC-NK-144 |

---

## 9. Gap Analysis (forward → A6 fix inline)

| Gap # | Mô tả | Suggested TC | A6 action |
|-------|-------|--------------|-----------|
| A5-GAP-01 | Cột "Mã bản ghi" chưa có TC riêng verify hiển thị | TC verify dòng có ma_ban_ghi đúng + format UUID/business code | A6 fill inline → 01-TC, Section A |
| A5-GAP-02 | Badge màu cho 7 loại hành động chưa verify đầy đủ (chỉ cover Tạo) | TC verify 7 màu badge khác nhau Tạo/Sửa/Xóa/Duyệt/Từ chối/Đăng nhập/Đăng xuất | A6 fill inline → 01-TC, Section A |
| A5-GAP-03 | Empty state khi `qtht_01` mở SCR-VIII-10 lần đầu mà DB chưa có log nào | TC: AUDIT_LOG hoàn toàn trống → empty state | A6 fill inline → 01-TC, Section B |

**Forward to A6:** 3 TC mới sẽ merge inline. Không có gap BR/AC/Error/Permission.

---

## 10. Coverage Summary

| Loại | Target | Actual | Status |
|------|--------|--------|--------|
| BR | ≥95% | 100% | ✅ |
| AC | 100% | 100% | ✅ |
| Error code | 100% | 100% | ✅ |
| Permission | 100% | 100% | ✅ |
| Filter field | 100% | 100% | ✅ |
| Output column | 100% | 75% explicit | ⚠️ — A6 fill 3 TC |
| SM | N/A | — | — |

**Phase A Acceptance Status (sau A6):** 7/7 dimension ≥ target ✅
