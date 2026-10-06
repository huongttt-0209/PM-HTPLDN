# 12 — Codex Review Log (FR-07 W2.1 Quản lý DN)

> **Reviewer**: Codex (gpt-5-codex helper)
> **Date**: 2026-05-09
> **Model**: gpt-5.3-codex (default)
> **Verdict Round 1**: GATE FAIL — 3 P0 findings
> **Verdict Round 2 (post-patch)**: ✅ PASS — apply 3 patches

---

## A. Round 1 Findings

| ID | Severity | Category | TC ref | SRS line | Issue | Fix proposal |
|----|---|---|---|---|---|---|
| P0-001 | P0 | GAP | TC-DN-PERM-603 | srs-v3.5:5318 | TAI_KHOAN.email duplicate ERR text "Email đã được sử dụng" chưa grounded NGUYÊN VĂN từ SRS | Mark TBD + SPEC-CLARIFY-DN-41 (FR-VIII-15 module sẽ define text) |
| P0-002 | P0 | GAP | TC-DN-PERM-301..303 | srs-v3.5:5317 | Thiếu negative MST boundary: 9 digits, 11 digits, non-digit chars | Thêm 3 TC negative format MST |
| P0-003 | P0 | GAP | TC-DN-014, 015 | srs-v3.5:1622-1643 + 01-CRUD.md:37-38 | DOANH_NGHIEP_LINH_VUC junction thiếu remove + cascade DN soft-delete | Thêm 2 TC: untick LV soft-delete junction + DN soft-delete cascade |

**Round 1 verdict**: GATE FAIL — apply 3 patches

---

## B. Patches Applied (Round 2)

### B.1 P0-001 fix — TC-DN-PERM-603 NGUYÊN VĂN drift

**File**: `06-TC-permission-matrix.md`
**Change**: Replaced ERR text `"Email đã được sử dụng"` (chưa grounded SRS) → mark "**NGUYÊN VĂN text TBD ở module FR-VIII** ... SPEC-CLARIFY-DN-41 — confirm với BA". Vẫn giữ TC để verify UNIQUE constraint behavior.

### B.2 P0-002 fix — MST boundary negative

**File**: `06-TC-permission-matrix.md`
**Add 3 TCs**:
- `TC-DN-PERM-304` — MST 9 digits → reject
- `TC-DN-PERM-305` — MST 11 digits → reject (chỉ chi nhánh 13 digits không tự đăng ký)
- `TC-DN-PERM-306` — MST non-digit (`ABC1234567`) → reject

Tất cả map BR-AUTH-USERNAME-01 (srs-v3.5:5317) — DN auto username = MST 10 chữ số per TT 105/2020/TT-BTC Điều 5.

### B.3 P0-003 fix — DOANH_NGHIEP_LINH_VUC junction

**File**: `01-TC-FR-V.III-01-quan-ly-dn-CRUD.md`
**Add 2 TCs**:
- `TC-DN-015b` — Untick lĩnh vực → soft-delete junction row (Happy P0)
- `TC-DN-015c` — Cascade soft-delete DN → junction ẩn khỏi list (Edge SPEC-CLARIFY-DN-46)

---

## C. Round 2 Verdict (post-patch)

✅ **GATE PASS**

| Metric | Round 1 | Round 2 (post-patch) |
|--------|---|---|
| Total TC | 134 | 139 (+5: 3 MST boundary + 2 LV junction) |
| BR Coverage | 11/11 (100%) | 11/11 (100%) — strengthen BR-AUTH-USERNAME-01 |
| AC Coverage | 18/18 (100%) | 18/18 (100%) |
| SM Coverage | 5/5 (100%) | 5/5 (100%) |
| Permission Coverage | 8/8 (100%) | 8/8 (100%) |
| Error Coverage | 13/13 (100%) | 13/13 (100%) |
| SPEC-CLARIFY count | 45 | 46 (+ DN-46 cascade junction) |
| Quality Score | 9.7/10 | 9.8/10 (sau Codex +5 TC, narrowed boundary gap) |

---

## D. Special items resolution

| Codex Item | Round 1 | Round 2 |
|------|---|---|
| A — Version tag | PASS | PASS |
| B — Import Excel BỎ | PASS | PASS |
| C — NHT HSPL CRU\* vs R+U | PASS (TC-503 áp dụng FR-X.1-04 AC override Permission Matrix per memory rule UI vs business → business priority) | PASS |
| D — DN.email NOT UNIQUE | PARTIAL | PARTIAL (D vẫn pending — text TAI_KHOAN.email duplicate cần BA) |
| E — username MST 10 digits | PARTIAL | PASS (sau +3 TC boundary) |
| F — Core ERR strings | PARTIAL | PARTIAL (F pending — ưu tiên D first) |
| G — 10 cherry-pick CHANGELOG | PARTIAL | PASS (sau +5 TC LV + MST cover hết gap) |
| H — BR-CALC-05 quy mô | PASS | PASS |
| I — DOANH_NGHIEP_LINH_VUC | PARTIAL | PASS (sau +2 TC remove + cascade) |

---

## E. Action items cho Phase B

1. SPEC-CLARIFY-DN-41 confirm với BA: NGUYÊN VĂN text khi đổi TAI_KHOAN.email trùng user khác (cross-FR-VIII)
2. SPEC-CLARIFY-DN-46 confirm: junction DOANH_NGHIEP_LINH_VUC cascade soft-delete khi DN.is_deleted=1?
3. SPEC-CLARIFY-DN-25 (đã có): MST format ERR code chính thức cho 3 TC negative MST boundary

---

**— Hết 12 Codex Review Log FR-07 —**
