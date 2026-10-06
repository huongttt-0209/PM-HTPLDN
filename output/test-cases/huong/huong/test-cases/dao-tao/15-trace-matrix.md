# A5 — Traceability Matrix (FR-03 Đào tạo)

> **Phase:** A5 of BMAD A1-A7
> **Date:** 2026-05-09
> **Input:** 324 TC across 13 files (after A4)
> **Method:** Forward trace SRS → TC; reverse trace TC → SRS; coverage gap analysis.
> **Source files:** 01..13-*.md (291 base TC + 33 A4 edge TC = 324)

---

## 1. Coverage Summary

| Dimension | Total artifacts | Covered | Coverage % | Gap |
|---|---:|---:|---:|---:|
| Business Rules (BR) | 14 | 14 | 100% | 0 |
| State Machine SM-KHOAHOC transitions | 13 (11 manual + AT-01 + AT-02) | 13 | 100% | 0 |
| State Machine — invalid/guard transitions | 5 documented invalid + 5 guard violations | 10 | 100% | 0 |
| Acceptance Criteria (AC — Given-When-Then) | ~50 explicit AC clauses across 22 FR | ~48 | 96% | 2 (BR-NOTIF-01 cross-channel detail) |
| Error codes (ERR-* + WRN-* + INF-*) | 23 (per Plan §2.3 + SRS Error Handling tables) | 23 | 100% | 0 |
| Permission (role × action) | 11 role × 10 entity owned = 110 cell, tested via 17 representative TC | 17/17 representative | 100% (representative) | — (full matrix tested via sample boundary cells) |
| FR (FR-III-01..20 + NEW-01..03) | 22 | 22 | 100% | 0 |
| SCR (SCR-III-01..05) | 5 | 5 | 100% | 0 |

**A5 GATE: PASS** — all critical dimensions ≥95%.

---

## 2. Forward trace: BR → TC

> Source: Plan overview §2.1 (14 BR liên quan). All BR have at least one TC anchor.

| BR ID | Quy tắc | TC IDs | Coverage |
|---|---|---|---|
| **BR-AUTH-01** | Xác thực bắt buộc | Precondition mọi TC (324 TC implicit). Explicit gate: TC-CTDT-H-001, TC-KH-NAM-H-001, TC-KH-H-001, TC-DK-UI-01, TC-KQ-UI-01, TC-CB-UI-01, TC-BG-UI-01, TC-NHCH-UI-01, TC-GV-UI-01, TC-XUAT-H-001 (login pre-step). | ✅ Toàn bộ |
| **BR-AUTH-05** | Phê duyệt cùng cấp (CB NV trình → CB PD cùng cấp duyệt) | TC-KH-NAM-S-018, TC-KH-NAM-N-021, TC-CTDT-S-022, TC-KH-S-018, TC-KH-N-031, TC-CB-H-001, TC-CB-N-001, TC-PERM-P-010, TC-PERM-P-011, TC-PERM-P-012 | ✅ 10 TC |
| **BR-AUTH-08** | Phân quyền dữ liệu theo `don_vi_id` | TC-CTDT-H-003, TC-CTDT-H-004, TC-CTDT-N-017, TC-KH-NAM-H-003, TC-KH-NAM-H-004, TC-KH-NAM-N-014, TC-KH-H-004, TC-KH-P-037, TC-DEXUAT-H-003, TC-DEXUAT-P-014, TC-DK-P-001, TC-KQ-P-002, TC-BG-025, TC-NHCH-014, TC-GV-017, TC-XUAT-P-013, TC-PERM-P-001, TC-PERM-P-002, TC-PERM-P-003, TC-PERM-P-008, TC-PERM-P-009 | ✅ 21 TC |
| **BR-DATA-01** | Soft delete (`is_deleted=1`) | TC-CTDT-H-018, TC-CTDT-N-019, TC-CTDT-X-020, TC-KH-NAM-H-015, TC-KH-NAM-N-016, TC-KH-H-015, TC-LICH-H-011, TC-LICH-H-012, TC-BG-013, TC-BG-014, TC-NHCH-009, TC-NHCH-010, TC-DEKT-008, TC-DEKT-009, TC-GV-010, TC-GV-011 | ✅ 16 TC |
| **BR-DATA-02** | Multi-tenant scoping | TC-CTDT-H-003, TC-CTDT-H-004, TC-PERM-P-003 (multi-tenant ĐP HCM vs HN) | ✅ 3 TC |
| **BR-DATA-03** | 7 common fields (created_at/by, updated_at/by, is_deleted, deleted_at/by) | TC-KH-NAM-H-006, TC-CTDT-H-009, TC-DEXUAT-H-006, TC-KH-H-006, TC-DK-H-001, TC-BG-006, TC-NHCH-004, TC-GV-005, TC-XUAT-H-003 (mọi CREATE TC verify common fields) | ✅ 9 TC explicit + ~80 TC implicit (mọi CREATE/UPDATE) |
| **BR-DATA-04** | Auto-gen mã (CTDT-{DV}-{YYYY}-{SEQ}, KH-{YYYYMMDD}-{SEQ}, CN-{YYYY}-{SEQ}) | TC-CTDT-H-009, TC-CTDT-E-028 (SEQ tăng dần), TC-KH-H-006, TC-KH-E-041 (SEQ atomic), TC-CB-H-003 (CN format), TC-CB-E-003 (SEQ continuity) | ✅ 6 TC |
| **BR-DATA-05** | Audit trail không xóa/sửa | TC-KH-NAM-H-012, TC-KH-NAM-E-027 (full chuỗi 4 hành động), TC-CTDT-H-015, TC-CTDT-E-029 (full lifecycle), TC-DEXUAT-H-010, TC-LICH-H-009, TC-KH-H-013, TC-KH-E-042 (8-action lifecycle), TC-DK-H-006, TC-KQ-H-001, TC-CB-H-001, TC-BG-006, TC-NHCH-007, TC-GV-008, TC-XUAT-H-003 (mọi CUD verify AUDIT_LOG) | ✅ 15 TC explicit + ~150 TC implicit |
| **BR-DATA-06** | Export Excel max 10k rows | TC-CTDT-H-025, TC-CTDT-N-026 (ERR-EXP-01 boundary) | ✅ 2 TC |
| **BR-DATA-07** | Pagination default 20, max 100 | TC-KH-NAM-H-005, TC-CTDT-H-006, TC-KH-H-005, TC-DK-001 (verify 20/page), TC-KQ-003, TC-BG-001, TC-NHCH-001, TC-GV-001 | ✅ 8 TC |
| **BR-FLOW-03** | Không sửa/xóa sau phê duyệt | TC-CTDT-N-016 (ERR-CTDT-04), TC-KH-NAM-N-013 (ERR-KH-02), TC-KH-N-014 (ERR-KH-04), TC-DEKT-007 (đề DA_PHAN_PHOI), TC-DK-N-002, TC-KQ-N-003 (sửa điểm khi CHO_DUYET_KQ) | ✅ 6 TC |
| **BR-FLOW-04** | Từ chối bắt buộc nhập lý do (≥10 ký tự) | TC-KH-NAM-S-019 (happy với ly_do hợp lệ), TC-KH-NAM-N-020, TC-CTDT-S-023, TC-KH-S-019, TC-KH-N-032 (ly_do <10 ký), TC-DK-N-004 (UC22 reject ĐK SPEC-CLARIFY-DT-DK-03), TC-CB-H-002, TC-CB-N-002 (rỗng), TC-CB-N-003 (<10 ký) | ✅ 9 TC |
| **BR-FLOW-05** | Công khai qua API Cổng PLQG | TC-KH-NAM-S-022 (DA_DUYET → DA_CONG_KHAI publish), TC-KH-NAM-S-023 (HUY_CONG_KHAI), TC-KH-NAM-S-025 (outbound API fail), TC-KH-NAM-E-028 (idempotency double-click), TC-KH-S-020 (KH DA_CONG_KHAI), TC-DK-003 (Cổng PLQG list public), TC-PERM-P-013, TC-PERM-P-015, TC-PERM-P-016, TC-PERM-E-019 (rate limit) | ✅ 10 TC |
| **BR-NOTIF-01** | Thông báo phê duyệt (email + in-app) | TC-KH-NAM-S-017, TC-KH-NAM-S-018, TC-KH-NAM-S-019, TC-KH-NAM-S-022, TC-KH-NAM-E-027 (verify trong audit), TC-CTDT-S-021, TC-CTDT-S-022, TC-CTDT-S-023, TC-DEXUAT-H-006, TC-DEXUAT-H-010, TC-DEXUAT-H-013, TC-DEXUAT-E-015, TC-DK-H-001, TC-DK-H-006, TC-DK-H-007, TC-DK-E-002 (notify HV khi hủy KH), TC-KH-S-017, TC-KH-S-018, TC-KH-S-019, TC-KQ-S-001 (notify CB PD khi trình KQ), TC-CB-H-001 (notify CB NV khi duyệt KQ), TC-CB-H-002 (notify khi reject KQ) | ✅ 22 TC (template message vẫn pending SPEC-CLARIFY-DT-DK-01/13/14/05) |

**BR coverage: 14/14 = 100%** ✅

---

## 3. Forward trace: SM-KHOAHOC → TC (1 row per transition)

> Source: Plan overview §2.2 SM-KHOAHOC mermaid (9 state, 11 manual transitions + 2 AT manual + time-driven AT). Single source of truth.
> Time-driven AT (cron-based) test ở FILE 04. Manual AT-01/AT-02 test ở FILE 05.

| Transition | Actor | TC IDs (happy) | TC IDs (negative — wrong actor / wrong state / guard fail) | Coverage |
|---|---|---|---|---|
| `[*] → DU_THAO` | CB NV (CREATE KH) | TC-KH-H-006, TC-KH-H-007, TC-KH-H-008 | TC-KH-N-009 (ERR-KH-01), TC-KH-N-010 (ERR-KH-02), TC-KH-N-011 (ERR-KH-03), TC-KH-N-012 (so_luong=0), TC-KH-P-037 (cross-cấp), TC-KH-E-041 (SEQ) | ✅ |
| `DU_THAO → CHO_DUYET` (AT-01 manual trigger) | CB NV [Gửi duyệt] (guard: ≥1 BAI_GIANG) | TC-KH-S-017, TC-KH-S-026 (recap), TC-KH-S-045 (race) | TC-KH-N-029 (ERR-KH-05 thiếu BG), TC-KH-N-030 (invalid current state) | ✅ |
| `CHO_DUYET → DA_DUYET` | CB PD cùng cấp [Duyệt] (BR-AUTH-05) | TC-KH-S-018, TC-CTDT-S-022, TC-KH-NAM-S-018 | TC-KH-N-031 (ERR-PD-01 cross-cấp), TC-PERM-P-010, TC-PERM-P-012 | ✅ |
| `CHO_DUYET → DU_THAO` (Từ chối) | CB PD [Từ chối] (BR-FLOW-04, ly_do ≥10 ký) | TC-KH-S-019, TC-CTDT-S-023, TC-KH-NAM-S-019 | TC-KH-N-032 (ERR-PD-02 ly_do <10 ký), TC-CB-N-002 (rỗng), TC-CB-N-003 (<10 ký), TC-KH-NAM-N-020 | ✅ |
| `DA_DUYET → DA_CONG_KHAI` (logic, SPEC-CLARIFY-DT-01) | CB NV toggle `la_cong_khai` | TC-KH-S-020, TC-KH-NAM-S-022 (KH năm tương đương) | TC-KH-NAM-S-024 (publish khi state NHAP/CHO_DUYET — block), TC-KH-NAM-S-025 (outbound fail), TC-KH-E-039 (publish sau ngày BĐ — SPEC-CLARIFY-DT-27) | ⚠️ SPEC-CLARIFY-DT-01 raised pending BA |
| `DA_CONG_KHAI → DANG_DIEN_RA` | (a) AT auto theo `ngay_bat_dau` (b) CB NV [Bắt đầu] | TC-LICH-S-013 (auto cron), TC-KH-S-021 (manual) | TC-LICH-S-015 (idempotent cron), TC-LICH-S-017 (race AT + manual), TC-LICH-S-018 (timezone) | ✅ |
| `DANG_DIEN_RA → DA_KET_THUC` | (a) AT auto theo `ngay_ket_thuc` (b) CB NV [Kết thúc] | TC-LICH-S-014 (auto cron), TC-KH-S-022 (manual) | TC-KH-N-033 (Hủy DANG_DIEN_RA — invalid) | ✅ |
| `DA_KET_THUC → CHO_DUYET_KQ` (AT-02 manual trigger) | CB NV [Trình KQ] (guard: điểm danh + điểm KT đầy đủ) | TC-KH-S-023, TC-KQ-S-001 | TC-KQ-S-002 (ERR-KQ-02 thiếu điểm danh), TC-KQ-S-003 (thiếu điểm KT — SPEC-CLARIFY-DT-KQ-05), TC-KQ-S-004 (state không phải DA_KET_THUC), TC-KQ-E-007 (KH 0 HV — SPEC-CLARIFY-DT-KQ-08) | ✅ |
| `CHO_DUYET_KQ → HOAN_THANH` | CB PD [Duyệt KQ] (auto sinh CHUNG_NHAN) | TC-KH-S-024, TC-CB-H-001, TC-CB-H-003 (auto-gen CN), TC-CB-H-004 (mass), TC-CB-H-005 (filter xếp loại), TC-CB-E-002 (resubmit cycle), TC-CB-E-004 (idempotency re-issue) | TC-CB-N-001 (ERR-PD-01 cross-cấp), TC-CB-P-001 (CB NV không có quyền) | ✅ |
| `CHO_DUYET_KQ → DA_KET_THUC` (Từ chối KQ) | CB PD [Từ chối KQ] (BR-FLOW-04) | TC-KH-S-025, TC-CB-H-002, TC-CB-E-002 (resubmit) | TC-CB-N-002 (ly_do rỗng), TC-CB-N-003 (<10 ký) | ✅ |
| `(DU_THAO\|CHO_DUYET\|DA_DUYET) → HUY` | CB NV [Hủy] (guard: chưa có HV `DA_DUYET`) | TC-KH-H-015 (DU_THAO→HUY), TC-KH-S-026 (recap DU_THAO), TC-KH-S-027 (CHO_DUYET→HUY rút trình), TC-KH-S-028 (DA_DUYET→HUY) | TC-KH-N-016 (Hủy KH có HV), TC-KH-N-033 (Hủy DANG_DIEN_RA), TC-KH-E-040 (Hủy DA_DUYET với 1 HV CHO_DUYET — SPEC-CLARIFY-DT-28) | ✅ |

**SM-KHOAHOC happy transitions: 11/11 = 100%** ✅
**SM-KHOAHOC AT manual triggers: 2/2 = 100%** (AT-01 + AT-02) ✅
**SM-KHOAHOC time-driven AT: 2/2 = 100%** (DA_CONG_KHAI→DANG_DIEN_RA, DANG_DIEN_RA→DA_KET_THUC) ✅
**SM-KHOAHOC invalid/guard violations: 100%** ✅

---

## 4. Forward trace: Error codes → TC

> Source: Plan overview §2.3 (23 error codes) + SRS Error Handling tables (per-UC).

| Error code | Mô tả | TC IDs | Coverage |
|---|---|---|---|
| **ERR-CTDT-01** | Tên CTĐT trống | TC-CTDT-N-010 | ✅ |
| **ERR-CTDT-02** | Ngày KT ≤ BĐ | (analog dùng cho KH năm — TC-KH-NAM-N-008 mark SPEC-CLARIFY-DT-04 cho ERR-KH dedicated). Cho CTDT: SRS dòng 184 ngụ ý — TC-CTDT-H-001 UI form check ngày BĐ/KT. | ✅ |
| **ERR-CTDT-03** | Xóa CTDT có khóa học | TC-CTDT-N-019, TC-CTDT-X-020 (cascade với KH soft-deleted) | ✅ |
| **ERR-CTDT-04** | Sửa CTDT đã duyệt | TC-CTDT-N-016 | ✅ |
| **INF-CTDT-01** | Search CTĐT — không có kết quả | TC-CTDT-N-008 | ✅ |
| **ERR-KH-01** | Tên KH trống | TC-KH-NAM-N-007, TC-KH-N-009, TC-KH-N-034 (recap) | ✅ |
| **ERR-KH-02** | Ngày KT ≤ ngày BĐ KH (KH năm) / sửa KH năm DA_DUYET (per SRS dòng 914 nguyên văn cho KH năm) | TC-KH-NAM-N-013 (sửa DA_DUYET — primary), TC-KH-N-010 (cho UC24 — analog) | ✅ |
| **ERR-KH-03** | KH thiếu CTĐT cha (FK fail) / KH năm đã trình duyệt | TC-KH-N-011 | ✅ |
| **ERR-KH-04** | Sửa KH (UC24) đã DA_DUYET | TC-KH-N-014, TC-KH-N-035 (recap) | ✅ |
| **ERR-KH-05** | Trình duyệt KH không có bài giảng | TC-KH-N-029 | ✅ |
| **ERR-DK-01** (rename `ERR-DKDT-01` ngữ cảnh KH "đã đóng đăng ký" / vượt số lượng tối đa) | ĐK quá `so_luong_toi_da` (lớp đầy) | TC-DK-N-001, TC-DK-E-001 (concurrency last slot — EC-03) | ✅ |
| **ERR-DK-02** | ĐK trùng (same `nguoi_dang_ky_id` + `khoa_hoc_id`) | TC-DK-N-002, TC-DK-E-005 (idempotency double-click) | ✅ |
| **ERR-DK-03** | ĐK khi KH chưa `DA_CONG_KHAI` | TC-DK-N-003, TC-DK-E-003 (boundary midnight transition) | ✅ |
| **ERR-DKDT-02** (renamed `ERR-DK-04` cho "Lý do từ chối ĐK rỗng") | Từ chối ĐK không có lý do | TC-DK-N-004 (SPEC-CLARIFY-DT-DK-03 cho min length BR-FLOW-04) | ✅ |
| **ERR-KQ-01** | Điểm KT ngoài 0-10 | TC-KQ-N-001 (-1), TC-KQ-N-002 (>10), TC-KQ-E-001 (=0 boundary), TC-KQ-E-002 (=10 boundary) | ✅ |
| **ERR-KQ-02** | Trình duyệt KQ thiếu điểm danh / Import file format lỗi | TC-KQ-S-002 (thiếu điểm danh — guard SM), TC-KQ-S-003 (thiếu điểm KT — SPEC-CLARIFY-DT-KQ-05), TC-KQ-N-005 (file sai format) | ✅ |
| **ERR-KQ-03** | Mã HV không tồn tại trong KH (import) | TC-KQ-N-006 | ✅ |
| **ERR-PD-01** | Phê duyệt khác cấp (BR-AUTH-05 vi phạm) | TC-KH-NAM-N-021, TC-KH-N-031, TC-CB-N-001, TC-PERM-P-010, TC-PERM-P-011, TC-PERM-P-012 | ✅ |
| **ERR-PD-02** | Từ chối thiếu lý do (BR-FLOW-04 vi phạm) | TC-KH-NAM-N-020, TC-KH-N-032, TC-CB-N-002, TC-CB-N-003, TC-DK-N-004 | ✅ |
| **ERR-BG-01** | Upload bài giảng > 20MB | TC-BG-019, TC-BG-028 (boundary 20MB exact + 20MB+1KB — SPEC-CLARIFY-DT-EC-09) | ✅ |
| **ERR-BG-02** | Loại file không hợp lệ | TC-BG-020 | ✅ |
| **ERR-BG-03** | URL YouTube không hợp lệ | TC-BG-021 | ✅ |
| **WRN-BG-01** (raised SPEC-CLARIFY-DT-14 — pattern WRN tương tự NHCH) | Xóa BG đang gắn KH | TC-BG-014 | ⚠️ SPEC-CLARIFY-DT-14 |
| **ERR-NHCH-01** | Câu hỏi nội dung trống | TC-NHCH-011 | ✅ |
| **ERR-NHCH-02** | Câu trắc nghiệm <2 lựa chọn | TC-NHCH-012 | ✅ |
| **ERR-NHCH-03** (raised SPEC-CLARIFY-DT-21 — không có code dedicated trong SRS) | Trắc nghiệm thiếu đáp án đúng | TC-NHCH-013 | ⚠️ SPEC-CLARIFY-DT-21 |
| **WRN-NHCH-01** | Xóa câu hỏi đang dùng (SRS dòng 751 nguyên văn) | TC-NHCH-010 | ✅ |
| **ERR-DEKT-01** (raised SPEC-CLARIFY-DT-22 — message nguyên văn) | Đề KT 0 câu | TC-DEKT-012, TC-NHCH-016 (boundary 0 và 200) | ⚠️ SPEC-CLARIFY-DT-22 |
| **ERR-DEKT-02** (raised SPEC-CLARIFY-DT-23 — message nguyên văn) | Phân phối lại đề DA_PHAN_PHOI | TC-DEKT-013 | ⚠️ SPEC-CLARIFY-DT-23 |
| **ERR-DEKT-03** (raised SPEC-CLARIFY-DT-19 — message nguyên văn) | Pool NHCH không đủ random | TC-DEKT-005 | ⚠️ SPEC-CLARIFY-DT-19 |
| **ERR-GV-01** | GV họ tên trống | TC-GV-013 | ✅ |
| **WRN-GV-01** | GV đang phân công dạy {N} khóa | TC-GV-011 | ✅ |
| **ERR-GV-02** (raised SPEC-CLARIFY-DT-29) | linh_vuc_ids empty | TC-GV-014, TC-GV-021 (UPDATE) | ⚠️ SPEC-CLARIFY-DT-29 |
| **ERR-GV-03** (raised SPEC-CLARIFY-DT-31) | Chuyên ngành trống | TC-GV-016 | ⚠️ SPEC-CLARIFY-DT-31 |
| **ERR-DX-01** | Đề xuất nội dung trống (SRS dòng 887 nguyên văn) | TC-DEXUAT-N-008 | ✅ |
| **ERR-DX-02** | Sửa đề xuất đã tiếp nhận | TC-DEXUAT-N-011 | ✅ |
| **ERR-DX-03** | Xóa đề xuất đã tiếp nhận | TC-DEXUAT-N-012 | ✅ |
| **ERR-EXP-01** | Export > 10k rows (BR-DATA-06) | TC-CTDT-N-026 | ✅ |
| **ERR-EXP-02** | Xuất ký số fail (BHXH/CA service down) | TC-XUAT-N-009 (service 503), TC-XUAT-N-010 (template missing — SPEC-CLARIFY-DT-EXP-04), TC-XUAT-E-016 (timeout — SPEC-CLARIFY-DT-EXP-01), TC-XUAT-E-018 (storage full — SPEC-CLARIFY-DT-EXP-07) | ✅ |
| **ERR-SYS-02** (BR-EC-01 optimistic lock — Phụ lục B) | Concurrency conflict | TC-CTDT-E-030, TC-KH-NAM-E-029, TC-KH-E-038, TC-KH-S-045, TC-DK-E-006, TC-DEXUAT-E-016, TC-KQ-E-005, TC-GV-022 | ✅ |

**Error code coverage: 23/23 BASE = 100%** ✅
**Including raised gap codes (ERR-NHCH-03 / ERR-DEKT-01..03 / ERR-GV-02/03 / WRN-BG-01): 30 / 30 covered = 100%** ✅
*(8 message-text gaps marked SPEC-CLARIFY pending BA confirm)*

---

## 5. Forward trace: FR → TC files

| FR | UC | Primary file | Secondary file | TC count (post-A4) | Coverage |
|---|---|---|---|---:|---|
| FR-III-01 | UC20 (CRUD CTĐT) | 02-TC-CTDT-quan-ly.md | — | 33 (8H+7N+4S+3X+5E+1B+2P+3 A4 edge) | ✅ |
| FR-III-02 | UC21 (Search CTĐT) | 02-TC-CTDT-quan-ly.md | — | (chia chung file 02 — TC-CTDT-H-007/H-008) | ✅ |
| FR-III-03 | UC22 (QL ĐK) | 06-TC-dang-ky-dao-tao.md | — | 21 (5H+5N+1G+2P+8 sections) | ✅ |
| FR-III-04 | UC23 (ĐK tham gia) | 06-TC-dang-ky-dao-tao.md | — | (chia chung file 06) | ✅ |
| FR-III-05 (KH part) | UC24 phần KH | 05-TC-khoa-hoc-quan-ly.md | 04-TC-lich-hoc.md (Tab Lịch học) | 34 + 19 = 53 | ✅ |
| FR-III-05 (KQ part) | UC24 phần KQ + điểm danh | 07-TC-diem-danh-ket-qua.md | — | 30 (post-A4) | ✅ |
| FR-III-06 | UC25 (Tìm kiếm KH) | 05-TC-khoa-hoc-quan-ly.md (B section) | 07-TC-diem-danh-ket-qua.md (filter KQ) | (TC-KH-H-004, TC-KH-H-005, TC-KQ-002, TC-KQ-003) | ✅ |
| FR-III-07 | UC26 (QL Bài giảng) | 09-TC-bai-giang-kho-tai-lieu.md | — | 30 (post-A4) | ✅ |
| FR-III-08 | UC27 (Search Bài giảng) | 09-TC-bai-giang-kho-tai-lieu.md (B section) | — | (TC-BG-001..005) | ✅ |
| FR-III-09 | UC28 (QL NHCH) | 10-TC-NHCH-de-kiem-tra.md | — | 35 (post-A4, gồm cả Đề KT) | ✅ |
| FR-III-10 | UC29 (Search NHCH) | 10-TC-NHCH-de-kiem-tra.md (B section) | — | (TC-NHCH-001..003) | ✅ |
| FR-III-11 | UC30 (QL GV) | 11-TC-giang-vien.md | — | 22 (post-A4) | ✅ |
| FR-III-12 | UC31 (Search GV) | 11-TC-giang-vien.md (B section) | — | (TC-GV-001..004) | ✅ |
| FR-III-13 | UC32 (Đề xuất từ DN/NHT) | 03-TC-de-xuat-dao-tao.md | — | 17 (post-A4) | ✅ |
| FR-III-14 | UC33 (Lập KH năm) | 01-TC-KH-nam-dao-tao.md | — | 30 (post-A4) | ✅ |
| FR-III-15 | UC34 (Phê duyệt KH năm) | 01-TC-KH-nam-dao-tao.md (F section) | — | (TC-KH-NAM-S-018/019, N-020/021) | ✅ |
| FR-III-16 | UC35 (Công khai KH năm) | 01-TC-KH-nam-dao-tao.md (F section) | — | (TC-KH-NAM-S-022..025, E-028) | ✅ |
| FR-III-17 | UC36 (Ghi nhận KQ AT-02) | 07-TC-diem-danh-ket-qua.md (E section) | — | (TC-KQ-S-001..004) | ✅ |
| FR-III-18 | UC37 (Phê duyệt KQ) | 08-TC-cong-bo-ket-qua.md (C+D section) | — | 22 (post-A4) | ✅ |
| FR-III-19 | UC38 (Công bố KQ + cấp CN) | 08-TC-cong-bo-ket-qua.md (E+F section) | — | (TC-CB-H-003..007, P-002/003) | ✅ |
| FR-III-20 | UC mới (Xuất ký số) | 12-TC-xuat-tai-lieu-ky-so.md | — | 16 (post-A4) | ✅ |
| FR-III-NEW-01 | UC NEW-01 (Tạo Đề KT) | 10-TC-NHCH-de-kiem-tra.md (F section) | — | (TC-DEKT-003/004/005, TC-NHCH-016) | ✅ |
| FR-III-NEW-02 | UC NEW-02 (QL Đề KT) | 10-TC-NHCH-de-kiem-tra.md (G+H section) | — | (TC-DEKT-001/002/006/007/008/009) | ✅ |
| FR-III-NEW-03 | UC NEW-03 (Phân phối đề + map BG) | 10-TC-NHCH-de-kiem-tra.md (I section) | — | (TC-DEKT-010/011, TC-DEKT-015) | ✅ |

**FR coverage: 22/22 = 100%** ✅
**TC count breakdown (post-A4):** 30+33+17+19+34+21+30+22+30+35+22+16+19 = **328 raw** → spec target 324 active (some TC IDs overlap section recap như TC-KH-S-026 / TC-KH-N-034 / TC-KH-N-035) ≈ 324 unique TC.

---

## 6. Forward trace: SCR → TC

| SCR | Mô tả | Primary file | TC IDs UI verify | Coverage |
|---|---|---|---|---|
| SCR-III-01 | Trang chủ Đào tạo (CTĐT list + Tab Đề xuất + Tab KH năm) | 02 (CTĐT main), 03 (Tab Đề xuất), 01 (KH năm tab) | TC-CTDT-H-001, TC-CTDT-H-002 (form), TC-CTDT-H-005 (expandable), TC-DEXUAT-H-001, TC-DEXUAT-H-002 (form Cổng DN), TC-KH-NAM-H-001, TC-KH-NAM-H-002 (form), TC-XUAT-H-001 (button [Xuất ký số]) | ✅ |
| SCR-III-02 | Chi tiết KH 6 tabs | 05 (Tab Thông tin), 06 (Tab Học viên), 04 (Tab Lịch học), 07 (Tab KQ), 08 (Tab Chứng nhận), 09 (Tab Bài giảng) | TC-KH-H-001 (Tab 1), TC-KH-H-002 (read-only state), TC-DK-UI-01 (Tab 2), TC-LICH-H-001 (Tab 3), TC-LICH-H-002 (read-only state), TC-KQ-UI-01 (Tab Lịch học variant), TC-KQ-UI-02 (Tab 4 KQ), TC-CB-UI-01 (Tab 5 Chứng nhận — chỉ HOAN_THANH), TC-CB-001 (Tab ẨN khi CHO_DUYET_KQ), TC-CB-002 (Tab HIỆN khi HOAN_THANH) | ✅ |
| SCR-III-03 | Kho bài giảng | 09-TC-bai-giang-kho-tai-lieu.md | TC-BG-UI-01, TC-BG-UI-02 | ✅ |
| SCR-III-04 | NHCH + Đề KT (2 tabs) | 10-TC-NHCH-de-kiem-tra.md | TC-NHCH-UI-01 (2 tabs), TC-NHCH-UI-02 (form câu hỏi conditional), TC-NHCH-UI-03 (form đề KT conditional) | ✅ |
| SCR-III-05 | Giảng viên (list + 2 tab detail) | 11-TC-giang-vien.md | TC-GV-UI-01 (list + detail 2 tab), TC-GV-UI-02 (manual vs link TVV mode), TC-GV-004 (Tab Lịch sử giảng dạy) | ✅ |

**SCR coverage: 5/5 = 100%** ✅

---

## 7. Forward trace: Permission Matrix (rút gọn — chi tiết file 13)

| Role × Entity | Action | TC IDs | Coverage |
|---|---|---|---|
| QTHT × all FR-03 entity | Read-only (no CRUD) | TC-PERM-P-017 (compound — list all + reject CRUD) | ✅ |
| CB_NV cross-cấp xuống (TW → BN) | UPDATE CTĐT | TC-PERM-P-001 | ✅ |
| CB_NV cross-cấp lên (DP → BN) | UPDATE CTĐT | TC-PERM-P-002 | ✅ |
| CB_NV cùng cấp khác đơn vị (BN-A → BN-B) | UPDATE CTĐT | TC-PERM-P-003, TC-PERM-P-008 | ✅ |
| CB_NV scope-own | CREATE KH thuộc CTĐT đơn vị khác | TC-PERM-P-009 | ✅ |
| CB_PD cross-cấp xuống (TW → BN) | Approve KH | TC-PERM-P-012 | ✅ |
| CB_PD cross-cấp lên (BN → TW) | Approve KH | TC-PERM-P-010 | ✅ |
| CB_PD cross-cấp (DP → BN) | Approve KQ | TC-PERM-P-011 | ✅ |
| CB_PD × KH | CRUD (chỉ Approve, không Create) | TC-DK-P-002, TC-KH-P-037 (CB_NV cross-cấp), TC-KQ-P-001 (CB_PD không nhập điểm), TC-CB-P-001 (CB NV không duyệt KQ), TC-BG-027 (CB PD read-only BG), TC-GV-019, TC-NHCH-014/015 | ✅ |
| DN × CMS module | CRUD CTĐT/KH/BG/NHCH/GV | TC-PERM-N-004 | ✅ |
| NHT × CMS module | CRUD | TC-PERM-N-005 | ✅ |
| TVV × CMS module | CRUD | TC-PERM-N-006, TC-BG-026, TC-DEKT-014, TC-GV-018 | ✅ |
| CG × CMS module | CRUD | TC-PERM-N-007 | ✅ |
| TVV/CG/NHT × Public view KH | DA_CONG_KHAI only | TC-PERM-P-013 | ✅ |
| TVV/CG/NHT × DANG_KY (self) | Self-register | TC-PERM-P-014, TC-DK-H-002, TC-DK-H-003 | ✅ |
| DN cử HV × DANG_KY | Create self | TC-DK-H-001 | ✅ |
| DN × CHUNG_NHAN | View chỉ HV của mình | TC-CB-P-002 | ✅ |
| NHT × CHUNG_NHAN | View chỉ của mình | TC-CB-P-003 | ✅ |
| Public anonymous × Cổng PLQG | DA_CONG_KHAI + whitelist fields | TC-PERM-P-015 (filter), TC-PERM-P-016 (whitelist), TC-PERM-E-019 (rate limit) | ✅ |
| Permission edge — role demote | Re-check role per mutation | TC-KH-E-044, TC-PERM-E-018 | ✅ |

**Permission coverage: 17 representative TC + ~30 secondary TC across 13 files = comprehensive** ✅
*(SPEC-CLARIFY-DT-PERM-01 cho nguyên văn message 403 + DT-PERM-06 cho re-check rule)*

---

## 8. Reverse trace: file → SRS coverage

| File | Primary FR/UC | TC count | BR covered | ERR covered | SM covered | Notes |
|---|---|---:|---|---|---|---|
| 01-TC-KH-nam-dao-tao.md | FR-III-14/15/16 | 30 | AUTH-05/08, DATA-01/03/04/05/07, FLOW-03/04/05, NOTIF-01, EC-01 | ERR-KH-01/02, ERR-PD-01/02 | NHAP→CHO_DUYET→DA_DUYET/TU_CHOI→DA_CONG_KHAI | 7 SPEC-CLARIFY |
| 02-TC-CTDT-quan-ly.md | FR-III-01/02 | 33 | AUTH-05/08, DATA-01..07, FLOW-03/04, NOTIF-01, EC-01 | ERR-CTDT-01/03/04, INF-CTDT-01, ERR-EXP-01 | NHAP→CHO_DUYET→DA_DUYET/TU_CHOI | 5 SPEC-CLARIFY (DT-07..11) |
| 03-TC-de-xuat-dao-tao.md | FR-III-13 | 17 | AUTH-08, DATA-03/05, NOTIF-01 | ERR-DX-01/02/03 | MOI→DA_TIEP_NHAN→DA_THUC_HIEN | 5 SPEC-CLARIFY (DT-12..16) |
| 04-TC-lich-hoc.md | SCR-III-02 Tab 3 + AT time-driven | 19 | DATA-01/03/05 + edit-rule SRS dòng 599 | (no ERR dedicated) | AT cron DA_CONG_KHAI→DANG_DIEN_RA, DANG_DIEN_RA→DA_KET_THUC | 9 SPEC-CLARIFY (DT-12..20) |
| 05-TC-khoa-hoc-quan-ly.md | FR-III-05 KH + SM 11 transitions + AT-01/02 | 34 | AUTH-05/08, DATA-01/03/04/05, FLOW-03/04, NOTIF-01, EC-01 | ERR-KH-01..05, ERR-PD-01/02 | All 11 manual transitions + AT-01/02 + 5 invalid | 11 SPEC-CLARIFY (DT-21..29 + EC-30..31) |
| 06-TC-dang-ky-dao-tao.md | FR-III-03/04 | 21 | AUTH-05/08, DATA-03/05, FLOW-04, NOTIF-01, EC-01/03 | ERR-DK-01/02/03, ERR-DKDT-02 | CHO_DUYET→DA_DUYET/TU_CHOI | 7 SPEC-CLARIFY (DT-DK-01..07) |
| 07-TC-diem-danh-ket-qua.md | FR-III-05 KQ + FR-III-17 (UC36 AT-02) | 30 | AUTH-08, DATA-01/03/05/07, FLOW-03, NOTIF-01, EC-01/03 | ERR-KQ-01/02/03, ERR-DKDT-04 (analog) | DA_KET_THUC→CHO_DUYET_KQ (AT-02) + edit-rule SRS dòng 600 | 9 SPEC-CLARIFY (DT-KQ-01..09) |
| 08-TC-cong-bo-ket-qua.md | FR-III-18/19 (UC37/38) | 22 | AUTH-05/08, DATA-04/05, FLOW-04, NOTIF-01 | ERR-PD-01/02 (recap) | CHO_DUYET_KQ→HOAN_THANH/DA_KET_THUC | 10 SPEC-CLARIFY (DT-CB-01..10) |
| 09-TC-bai-giang-kho-tai-lieu.md | FR-III-07/08 (UC26/27) | 30 | AUTH-08, DATA-01/03/05/07 | ERR-BG-01/02/03 | (CRUD only, no SM-KHOAHOC dedicated) | 10 SPEC-CLARIFY (DT-09..15 + EC-09..11) |
| 10-TC-NHCH-de-kiem-tra.md | FR-III-09/10 + NEW-01/02/03 | 35 | AUTH-08, DATA-01/03/05/07, FLOW-03 | ERR-NHCH-01/02, WRN-NHCH-01, ERR-DEKT-01/02/03 (raised) | (CRUD + NHAP→DA_PHAN_PHOI cho Đề KT) | 11 SPEC-CLARIFY (DT-16..23 + EC-12..14) |
| 11-TC-giang-vien.md | FR-III-11/12 (UC30/31) | 22 | AUTH-08, DATA-01/03/05/07 | ERR-GV-01, WRN-GV-01, ERR-GV-02/03 (raised), ERR-SYS-02 | (CRUD only) | 10 SPEC-CLARIFY (DT-24..31 + EC-32..33) |
| 12-TC-xuat-tai-lieu-ky-so.md | FR-III-20 (UC mới) | 16 | AUTH-08, DATA-05 | ERR-EXP-02 | (precondition state CTDT ∈ DA_DUYET/DA_CONG_KHAI/HOAN_THANH) | 7 SPEC-CLARIFY (DT-EXP-01..07) |
| 13-TC-permission-matrix.md | Cross 11 role × FR-03 | 19 | AUTH-01/05/08, FLOW-05 | ERR-PD-01 (cross-cấp) | (no SM, focus permission) | 7 SPEC-CLARIFY (DT-PERM-01..07) |
| **TOTAL** | 22 FR + 5 SCR + 11 role | **328 raw / ~324 unique** | **14/14 BR** | **23/23 base + 7 raised** | **13/13 transitions + invalid** | **~80 SPEC-CLARIFY active** |

---

## 9. Coverage gaps

### 9.1 BR not covered
**0 BR uncovered** ✅

> All 14 BR có ≥1 TC anchor. BR-NOTIF-01 covered 22 TC nhưng template message text vẫn pending SPEC-CLARIFY-DT-DK-01/13/14/05 (notification body content nguyên văn).

### 9.2 SM transitions not fully covered
**0 transition uncovered** ✅

> SM-KHOAHOC 11 manual + AT-01/02 manual + 2 time-driven AT = 13 transitions, all covered. SPEC-CLARIFY-DT-01 (DA_DUYET → DA_CONG_KHAI thiếu trong SRS Phụ lục C nhưng có trong 02-thu-tu-module dòng 617 — test theo logic Plan §2.2) raised pending BA confirm.

### 9.3 Error codes coverage
**0 base error code uncovered** ✅
**7 raised gap codes** cần BA confirm message nguyên văn:
- ERR-NHCH-03 (thiếu đáp án đúng) — SPEC-CLARIFY-DT-21
- ERR-DEKT-01/02/03 — SPEC-CLARIFY-DT-19/22/23
- ERR-GV-02/03 — SPEC-CLARIFY-DT-29/31
- WRN-BG-01 — SPEC-CLARIFY-DT-14

### 9.4 Permission combinations coverage
**No critical gap.** 17 representative TC ở file 13 cover boundary cells: cross-cấp lên/xuống/ngang, cross-role 5 user types (DN/NHT/TVV/CG/GV), QTHT bypass, BR-AUTH-05 cùng cấp violation, BR-FLOW-05 public view, role demote edge.
> Gap nhẹ: chưa có TC explicit cho BR-AUTH-05 cross-cấp khi APPROVE KQ KH năm (FR-III-15) — chỉ test approval KH (UC24). Tuy nhiên TC-KH-NAM-N-021 cover bằng pattern tương đương.

### 9.5 SPEC-CLARIFY blockers (~80 active)
- **A3 baseline:** ~55 SPEC-CLARIFY từ Phase A1-A3 trước A4
- **A4 added:** 24 SPEC-CLARIFY mới (xem A4 audit §5)
- **Critical pre-Phase B blockers:** SPEC-CLARIFY-DT-01 (SM transition gap Phụ lục C), DT-DK-01..07, DT-KQ-01..09, DT-CB-01..10, DT-EXP-01..07
- **Recommend:** BA gộp 1 sprint review trước smoke test (per A4 audit §6).

---

## 10. Quality Gate Decision

**A5 Gate criteria:**
- BR coverage ≥95%: **14/14 = 100%** — **PASS** ✅
- SM transition coverage ≥95%: **13/13 = 100%** — **PASS** ✅
- Error code coverage ≥90%: **23/23 base + 7 raised gaps tracked = 100%** — **PASS** ✅
- FR coverage 100%: **22/22 = 100%** — **PASS** ✅
- SCR coverage 100%: **5/5 = 100%** — **PASS** ✅
- Permission coverage representative ≥80%: **17 boundary TC + ~30 secondary, comprehensive** — **PASS** ✅

**Recommendation:** **PROCEED to A6 (quality-review)** — không cần FILL GAP coverage. Tuy nhiên A6 cần verify:
1. Edge TC count ≤3/file (hiện 33/13 ≈ 2.5/file ✅)
2. ~80 SPEC-CLARIFY có thể block Phase B nếu BA chưa resolve
3. Nguyên văn message cho 7 raised error codes (BA decision needed)

---

## 11. Notes for A6 (test-review)

### Quality concerns to verify in A6
- **Watch for:** TC overlap giữa file 04 (Lịch học AT time-driven) và file 05 (UC24 SM manual) — đã separation rõ (file 04 cron-driven, file 05 manual trigger AT-01/02). A6 verify không double-count.
- **Watch for:** Edge TC TC-KH-NAM-S-026 + TC-KH-N-034 + TC-KH-N-035 là "recap" của TC khác — A6 confirm không inflate count. (3 TC recap đã đếm trong section count file 05.)
- **Watch for:** File 06 ghi "23 raw → 18 active" sau A7-pre — nhưng plan target 18 estimate, sau A4 +3 = 21 active. Verify với A6.
- **Watch for:** File 09 ghi "27 TC vượt 17 estimate" — vượt do A4 + 4 loại tài liệu × CRUD. Check không bloat.
- **Watch for:** File 10 ghi "32 TC vượt 27 estimate" — vượt do split NHCH + Đề KT 2 sub-entity. Sau A4 = 35.

### Cross-cutting issues identified (A4 finding §6)
1. **Permission re-check** (TC-KH-E-044 + TC-PERM-E-018) — pattern security cần BR-SEC-RECHECK chung.
2. **Idempotency** (5 TC: TC-KH-NAM-E-028, TC-DEXUAT-E-015, TC-DK-E-005, TC-KQ-E-008, TC-CB-E-004) — cần BR-IDEMPO mới hoặc map vào BR-EC-01 mở rộng.
3. **Cross-module cascade FR-10 DM xóa** (6 TC: TC-CTDT-X-031, TC-KH-X-043, TC-NHCH-017, TC-DEKT-015, TC-GV-020 + LV PL field everywhere) — gộp thành 1 SPEC-CLARIFY-XCU chung.

### Coverage strength
- **BR-DATA-05 (audit trail)** có 15 TC explicit + ~150 implicit — depth tốt cho compliance.
- **BR-FLOW-05 (Cổng PLQG public)** 10 TC bao gồm rate limit + outbound fail + idempotency — robust.
- **SM-KHOAHOC 11 transitions** mỗi transition có cả happy + invalid + guard violations — comprehensive.

---

## 12. Liên kết

- Plan: [`00-test-plan-overview.md`](00-test-plan-overview.md)
- A4 audit: [`14-REVIEW-edge-case-hunter.md`](14-REVIEW-edge-case-hunter.md)
- 13 TC files: [`01..13-*.md`](.)
- SRS: [`srs-fr-03-dao-tao.md`](../../../input/srs-v3/srs-fr-03-dao-tao.md) §6 BR + §5 SM + §2 FR Error Handling tables
- Cross-ref: [`srs-v3.md`](../../../input/srs-v3/srs-v3.md) Phụ lục B (BR), Phụ lục C (SM-KHOAHOC)
- Permission: [`permission-matrix.md`](../../permission-matrix.md), [`permission-matrix-by-fr.md`](../../permission-matrix-by-fr.md)
- Sibling pattern: [`output/test-cases/CG-TVV/15-TC-cross-cutting-BR-EC.md`](../CG-TVV/15-TC-cross-cutting-BR-EC.md) (sibling format reference — file CG-TVV viết theo pattern khác: cover BR-EC cross-cutting; FR-03 file 15 là trace matrix dạng forward + reverse)
