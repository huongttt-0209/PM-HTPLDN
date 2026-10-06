# Kế Hoạch Kiểm Thử — Nhật ký Hệ thống (FR-VIII-28, SCR-VIII-10)

> **Phiên bản**: 1.0
> **Ngày tạo**: 2026-05-08
> **Nguồn dữ liệu**: SRS v3.1 ([srs-fr-10-quan-tri-v3.1.md](../../../../input/srs-v3/srs-fr-10-quan-tri-v3.1.md) lines 1314-1372 + 1803-1834, kèm [srs-v3.1.md](../../../../input/srs-v3/srs-v3.1.md) Phụ lục B cho BR cross-cutting)
> **SRS Reference**: FR-VIII-28 `[GAP-VIII-02]` v2.1 formalize, MH-10.10 / SCR-VIII-10, Entity AUDIT_LOG (referenced)
>
> **Scope:** Test plan GĐ Functional + Auth + Edge cho module **Nhật ký Hệ thống**. Module read-only — tra cứu, lọc, xuất Excel. KHÔNG có CUD trên AUDIT_LOG (immutable per A.3 + BR-DATA-05).

---

## 1. Phạm Vi Kiểm Thử

### 1.1 Chức năng được kiểm thử
- 1 FR (FR-VIII-28) trên 1 màn hình (SCR-VIII-10 — MH-10.10).
- Entity chính: `AUDIT_LOG` (referenced — read-only).
- Đặc thù v3.1:
  - Constraint **90 ngày** giữa `thoi_gian_tu` và `thoi_gian_den` (FR-VIII-28 step 2 + ERR-LOG-02, srs-fr-10:1344, 1363).
  - Export Excel **max 10.000 dòng** (FR-VIII-28 step 6 + AC2, srs-fr-10:1348, 1371) ↔ **mâu thuẫn** SCR-VIII-10 line 1830 ghi 50.000 (SPEC-CLARIFY-NHATKY-01 — BR-DATA-06 Phụ lục B nguyên văn 10.000, theo BR Phụ lục B).
  - Audit log **immutable** (A.3 + BR-DATA-05) — không có CUD.
  - Retention **5 năm** (SCR-VIII-10 line 1828).
- Màn hình: SCR-VIII-10 (Danh sách read-only). Filter-bar: 5 select + 1 text + 1 date-range + 2 button. Bảng: 7 cột + sticky header. Footer: pagination 50/page.
- State Machine: Không áp dụng (read-only entity).

### 1.2 Danh sách FR / UC

| # | Mã FR | Use Case | Tên chức năng | Entity | File Test Case |
|---|--------|----------|--------------|--------|----------------|
| 1 | FR-VIII-28 | UC-LOG-01 (logical) | Tra cứu + Lọc + Sort + Pagination + View detail JSON diff | AUDIT_LOG | `01-TC-tra-cuu-loc-nhat-ky.md` (32 TC active, 3 marked DUPLICATE) |
| 2 | FR-VIII-28 | UC-LOG-02 (logical) | Xuất Excel (theo filter, max 10.000 dòng) | AUDIT_LOG | `02-TC-xuat-excel-nhat-ky.md` (12 TC) |
| 3 | — | — | Permission matrix (chỉ QTHT — BR-AUTH-01 + BR-DATA-05 immutable) | All | `03-TC-permission-matrix.md` (9 TC) |

**Total: 53 TC active** (sau codex review 2026-05-08: -3 duplicates marked + 2 added IP/boundary201; was 54)

> FR-VIII-28 chỉ có 1 UC (tra cứu/lọc + xuất). Tách 3 file UC theo functional area (Tra cứu vs Xuất Excel vs Permission) cho dễ quản lý B-Run; vẫn giữ cùng FR.

### 1.3 Tài khoản & role liên quan

| Role | Cấp | Username (users.csv) | Dùng cho TC loại |
|------|-----|-----------------------|-------------------|
| QTHT | — | qtht_01 | Read primary (toàn HT). `_02` fallback, `_03` permission test |
| CB_NV_TW | TW | cb_nv_tw_01 | Negative — verify 403 chặn (BR-AUTH-01: KHÔNG QTHT) |
| CB_NV_BN | BN | cb_nv_bn_01 | Negative — verify 403 |
| CB_NV_DP | DP | cb_nv_dp_01 | Negative — verify 403 |
| CB_PD_TW/BN/DP | — | cb_pd_tw_01 / cb_pd_bn_01 / cb_pd_dp_01 | Negative — verify 403 |
| NHT/TVV/CG/DN | — | nht_01, tvv_01, cg_01, dn_01 | Negative — verify 403 (Tier 2 SSO không vào CMS) |

> **Lý do:** SRS srs-fr-10:1322 nguyên văn "Chỉ QTHT truy cập"; AC3 "user không có quyền QTHT → từ chối truy cập". Tất cả role khác đều phải bị reject.

---

## 2. Quy Tắc Nghiệp Vụ Trích Xuất Từ SRS

### 2.1 Business Rules (BR)

| Mã | Quy tắc | Nguồn SRS | Áp dụng? | TC áp dụng |
|----|---------|-----------|----------|-----------|
| BR-AUTH-01 | Xác thực + chỉ QTHT (Tier 1) | srs-fr-10:1343, 1372; srs-v3.1.md §B.1 | ✅ | Precondition mọi UC + permission matrix |
| BR-DATA-05 | Audit log immutable, INSERT-only | srs-v3.1.md:5330 | ✅ | Verify không có nút Sửa/Xóa trên SCR-VIII-10 |
| BR-DATA-06 | Export Excel max 10.000 rows | srs-v3.1.md:5331 + srs-fr-10:1348, 1371 | ✅ | Boundary export 9.999 / 10.000 / 10.001 |
| BR-DATA-07 | Pagination default 20, max 100 / page (note: SCR-VIII-10 đặt 50/page custom — vẫn trong range) | srs-v3.1.md:5332 + srs-fr-10:1824 | ✅ | TC pagination 50 mặc định |
| BR-EC-13 | Search sanitize max 200 ký tự + escape SQL/XSS | srs-v3.1.md:5471 | ✅ | TC sanitize qua dropdown "Người dùng" search input (NHATKY-02 RESOLVED — không có Entity filter) |
| **Constraint 90 ngày** | `thoi_gian_den - thoi_gian_tu ≤ 90 ngày` (warning ERR-LOG-02 nếu vi phạm) | srs-fr-10:1344, 1363 | ✅ (v3.1 mới) | Boundary 89 / 90 / 91 ngày |

### 2.2 Error Codes / Messages

**FR-VIII-28 (Tra cứu/Lọc):**
- `ERR-LOG-01` ERROR — "Bạn không có quyền truy cập nhật ký hệ thống" (E1, srs-fr-10:1362)
- `ERR-LOG-02` WARNING — "Khoảng thời gian tối đa là 90 ngày" (E2, srs-fr-10:1363)

**Empty state:**
- "Không tìm thấy nhật ký phù hợp." (SCR-VIII-10 thành phần #11, srs-fr-10:1825)

**Cross-cutting:**
- BR-EC-13 search sanitize → KHÔNG có error code riêng, chỉ silent escape; verify không thực thi SQL/XSS.

### 2.3 Permission Matrix

| Action | QTHT | CB_NV (TW/BN/DP) | CB_PD (TW/BN/DP) | NHT/TVV/CG/DN |
|--------|------|------------------|-------------------|---------------|
| Truy cập SCR-VIII-10 (read) | ✅ | ❌ ERR-LOG-01 | ❌ ERR-LOG-01 | ❌ (Tier 2 không có entry menu) |
| Lọc/Tìm kiếm | ✅ | ❌ | ❌ | ❌ |
| Xuất Excel | ✅ | ❌ | ❌ | ❌ |
| Sửa/Xóa AUDIT_LOG | ❌ (KHÔNG ai) | ❌ | ❌ | ❌ |

> **Iron rule:** AUDIT_LOG là immutable theo A.3 + BR-DATA-05. KHÔNG có nút Sửa/Xóa trên SCR-VIII-10 cho bất kỳ role nào (kể cả QTHT). Test phải verify UI ẩn nút + backend reject DELETE/UPDATE direct.

### 2.4 State Machine — N/A

Module read-only, không có state machine. Verify entity AUDIT_LOG là append-only theo BR-DATA-05.

### 2.5 Filter / Search Fields (Inputs SRS line 1331-1338)

| # | Field | Type | Bắt buộc | Constraint | Default |
|---|-------|------|---------|------------|---------|
| 1 | `thoi_gian_tu` | date | N | — | hôm nay - 7 |
| 2 | `thoi_gian_den` | date | N | ≥ thoi_gian_tu, max 90 ngày so với tu | hôm nay |
| 3 | `nguoi_dung` | searchable dropdown → TAI_KHOAN | N | — | — |
| 4 | `module` | select 12 giá trị | N | Hỏi đáp / Đào tạo / CG-TVV / Vụ việc / Chi trả / DN / Đánh giá / Biểu mẫu / Quản trị / Báo cáo / Tư vấn / CT HTPLDN | — |
| 5 | `hanh_dong` | select 7 giá trị | N | Tạo / Sửa / Xóa / Phê duyệt / Từ chối / Đăng nhập / Đăng xuất | — |
| ~~6~~ | ~~`entity`~~ | ❌ NOT A FILTER | NHATKY-02 RESOLVED: FR-VIII-28 Inputs (line 1331-1338) chỉ có 5 field. SCR-VIII-10 #7 thêm Entity là UI spec sai. **Filter-bar có đúng 5 field**. (Entity vẫn xuất hiện làm cột bảng output — xem §2.6.) | — |

### 2.6 Output Columns (SRS line 1352-1356 + SCR-VIII-10 #9)

| # | Cột | Format | Sortable? |
|---|-----|--------|-----------|
| 1 | Thời gian | dd/mm/yyyy HH:mm:ss (DESC mặc định) | ✅ |
| 2 | Người dùng | ho_ten | — |
| 3 | Đơn vị | ten_don_vi | — |
| 4 | Module | nhãn module | — |
| 5 | Entity | tên bảng | — |
| 6 | Mã bản ghi | UUID hoặc business code | — |
| 7 | Loại thao tác | badge màu (Tạo=xanh, Sửa=vàng, Xóa=đỏ, Duyệt=xanh lá, Từ chối=cam, Đăng nhập=xám, Đăng xuất=xám) | — |
| 8 | Chi tiết thay đổi | JSON diff `{"field": "...", "old": "...", "new": "..."}` (expandable) | — |

---

## 3. Cấu Trúc File Test Case

```
QTHT/Nhat-ky-he-thong/
├── 00-test-plan-overview.md         ← file này (A2)
├── 01-TC-tra-cuu-loc-nhat-ky.md     ← FR-VIII-28 UC-LOG-01 (~30 TC, A3 base + A4)
├── 02-TC-xuat-excel-nhat-ky.md      ← FR-VIII-28 UC-LOG-02 (~12 TC)
├── 03-TC-permission-matrix.md       ← BR-AUTH-01 + BR-DATA-05 immutable (~10 TC)
├── 08-REVIEW-edge-case-hunter.md    ← A4 audit log (proposal + merge mapping)
├── 09-traceability-matrix.md        ← A5 BR/AC ↔ TC matrix
├── 10-REVIEW-test-quality.md        ← A6 6-axis quality score
└── 11-a7-filter-log.md              ← A7 filter UI/function-testable log
```

> **Phase B B-block ref CHỈ 3 file UC (01-03)**, total ~52 TC. File 08/09/10/11 là audit log, KHÔNG phải TC source.

---

## 4. Coverage Target

| Loại | Target | Note |
|------|--------|------|
| BR coverage | ≥95% | 6 BR áp dụng — BR-AUTH-01 / BR-DATA-05 / BR-DATA-06 / BR-DATA-07 / BR-EC-13 / Constraint 90 ngày |
| AC coverage | 100% | 3 AC SRS line 1370-1372 |
| Error code coverage | 100% | ERR-LOG-01, ERR-LOG-02 |
| SM transition coverage | N/A | Read-only |
| Permission combo | 100% | 4 role × access SCR-VIII-10 (QTHT ✅ + 3 nhóm khác ❌) |

---

## 5. Open Items / SPEC-CLARIFY

| ID | Status | Mô tả | SRS line | Action |
|----|--------|-------|----------|--------|
| ~~SPEC-CLARIFY-NHATKY-01~~ | ✅ RESOLVED 2026-05-08 (theo business) | Excel limit = **10.000 dòng** (FR-VIII-28 step 6 + AC2 + BR-DATA-06 Phụ lục B). SCR-VIII-10 line 1830 ghi 50K SAI so với business → coi như UI spec chưa update. | srs-fr-10:1348 ✓ vs 1830 ✗ | TC-NK-EXP-* test theo 10K. Phase B nếu BE accept >10K → BUG implementation. |
| ~~SPEC-CLARIFY-NHATKY-02~~ | ✅ RESOLVED 2026-05-08 (theo business) | Filter-bar có **đúng 5 field** theo FR-VIII-28 Inputs (line 1331-1338): tu/den/người dùng/module/hành động. **KHÔNG có Entity filter**. SCR-VIII-10 #7 thêm Entity là UI spec chưa khớp business. | srs-fr-10:1336 ✓ vs 1821 ✗ | TC-NK-106 convert thành verify Entity filter KHÔNG có. Sanitize TC-130-133 redirect sang dropdown người dùng search. Cleanup overview/traceability/TC-144 done 2026-05-08 (codex review). |
| SPEC-CLARIFY-NHATKY-03 | ⏳ pending BA | SCR-VIII-10 #5 module có **12 nhãn**; PM còn module Cấu hình/TKPQ/DM (FR-VIII-01..05) — gap completeness, không phải UI vs business pure. | srs-fr-10:1336 + 1819 | Cần BA xác nhận: thêm nhãn riêng hay gộp "Quản trị". |
| SPEC-CLARIFY-NHATKY-04 | ✅ ACCEPTED (50/page trong range BR-DATA-07 max 100) | Pagination 50/page custom — vẫn ≤ max 100 BR-DATA-07 → hợp lệ. | srs-fr-10:1824 ✓ trong range srs-v3.1.md:5332 | TC giữ 50/page. KHÔNG cần BA. |
| ~~SPEC-CLARIFY-NHATKY-05~~ | ✅ DOWNGRADED (codex 2026-05-08 — không cần BA blocker) | `den >= tu` line 1334 đã resolve behavior; chỉ thiếu exact text message. Phase B chấp nhận 1 trong các pattern (UC93 ERR-TK-01). | srs-fr-10:1334 | TC-NK-121 verify message theo pattern, log nếu khác. KHÔNG block BA. |
| SPEC-CLARIFY-NHATKY-06 | ⏳ pending BA | Cả 2 source silent về dropdown người dùng có include `is_deleted=1` không. | srs-fr-10:1335 | TC-NK-139 test 3 behavior (verify A.3 retention 5 năm). |
| **SPEC-CLARIFY-NHATKY-07** ⭐ NEW | ⏳ pending BA (codex review 2026-05-08) | **EXPORT audit action chưa có ở SRS.** FR-VIII-28 line 1337 + BR-DATA-05 (srs-v3.1.md:5330) chỉ define 7 action enum (CREATE/UPDATE/DELETE/APPROVE/REJECT/LOGIN/LOGOUT). TC-NK-EXP-001/004 ban đầu assert `hanh_dong=EXPORT` → có thể vi phạm enum strict. | srs-fr-10:1337 + srs-v3.1.md:5330 | TC-NK-EXP-001/004 reframed: KHÔNG assert EXPORT log Phase A. Phase B verify behavior thực tế. Cần BA confirm extend action enum hay accept "không log EXPORT". |

**Tổng:** 2 SPEC-CLARIFY ✅ RESOLVED (theo business spec), 1 ✅ ACCEPTED (trong range), 1 ✅ DOWNGRADED (codex review), 3 ⏳ pending BA (NHATKY-03/06/07).

---

## 6. Liên kết

- SRS FR-VIII-28: `input/srs-v3/srs-fr-10-quan-tri-v3.1.md` lines 1314-1372
- SCR-VIII-10: `input/srs-v3/srs-fr-10-quan-tri-v3.1.md` lines 1803-1834
- BR Phụ lục B: `input/srs-v3/srs-v3.1.md` (BR-AUTH-01, BR-DATA-05/06/07, BR-EC-13)
- Sibling pattern reference: `output/test-cases/bieu-mau/00-test-plan-overview.md`
- Plan: `Ver3.1/tasks/detailed-tc/plan.md` §3.1 Phase A workflow
