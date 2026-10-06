# A5 Traceability Matrix — Cấu hình Hệ thống

> **Module**: QTHT Cấu hình HT (SCR-VIII-06 + FR-VIII-29)
> **Ngày chạy**: 2026-05-08
> **Skill**: bmad-testarch-trace (manual)
> **Output**: Matrix BR/AC/Error/Permission ↔ TC. Phát hiện gap → forward A6 fix inline.

---

## 1. BR Coverage

| BR | Mô tả | Source | TC cover | Coverage |
|----|-------|--------|----------|----------|
| BR-AUTH-01 | Authentication + role-based | srs-v3.1.md §B.1 | TC-CH-SLA-030/031/032, TC-CH-MPH-001..003 (precondition), TC-CH-NL-050/051, TC-CH-PERM-001..007, TC-CH-QT-020..022 | ✅ 100% |
| BR-AUTH-08 | Phân quyền theo đơn vị + ngoại lệ Mô hình B | srs-v3.md §3.4.2 + srs-v3.1.md §B.1 | TC-CH-MPH-010..014 (READ scope), TC-CH-PERM-010..012 (cross-isolation), TC-CH-MPH-067 (IDOR) | ✅ 100% |
| BR-DATA-01 | Soft delete | srs-v3.1.md §B.2 | TC-CH-MPH-021 (DELETE mẫu), TC-CH-NL-004 (DELETE ngày lễ) | ✅ 100% |
| BR-DATA-03 | 7 common fields | srs-v3.1.md §B.2 | TC-CH-MPH-001 (CREATE schema), TC-CH-NL-001 (CREATE schema) | ✅ 100% |
| BR-DATA-05 | Audit log immutable | srs-v3.1.md §B.2 | TC-CH-SLA-043, TC-CH-MPH-001 (audit pham_vi), TC-CH-NL-001/003/004, TC-CH-QT-031 | ✅ 100% |
| BR-DATA-06 | Export Excel max 10K | srs-v3.1.md §B.2 | TC-CH-NL-023 (Import 10K — đảo chiều) | ⚠️ partial — KHÔNG có export trên SCR-VIII-06 (verify) |
| BR-DATA-07 | Pagination 20/page | srs-v3.1.md §B.2 | TC-CH-MPH-046 | ✅ 100% |
| BR-EC-01 | Optimistic Locking | srs-v3.1.md §B.4 | TC-CH-SLA-040, TC-CH-MPH-063, TC-CH-QT-030 | ✅ 100% |
| BR-EC-13 | Search sanitize 200 + escape | srs-v3.1.md §B.4 | TC-CH-MPH-060/061/062/065 | ✅ 100% |
| BR-SLA-01 | SLA mặc định 10 ngày LV NĐ55 | srs-v3.1.md §B.5 | TC-CH-SLA-002 (verify default seed) | ✅ 100% |
| BR-SLA-02 | 4 mức cảnh báo | srs-v3.1.md §B.5 | TC-CH-SLA-001 (info box hiển thị 4 mức) | ✅ 100% |
| BR-SLA-04 | Ngày làm việc trừ lễ | srs-v3.1.md §B.5 | TC-CH-NL-040 (e2e) | ✅ 100% |
| BR-CALC-03 | Deadline ngày LV dùng NGAY_LE | srs-v3.1.md §B.5 | TC-CH-NL-040, TC-CH-SLA-021 (HS mới áp config) | ✅ 100% |
| **Mô hình B Hybrid** | TW/BN/DP scope rules + auto-fill + immutable | srs-v3.md §3.4.2 | TC-CH-MPH-001..004 (auto-fill), TC-CH-MPH-010..014 (READ scope), TC-CH-MPH-033..038 (BE check), TC-CH-PERM-033 (UI immutable) | ✅ 100% |
| **Snapshot pattern** | HS đang xử lý giữ config cũ | srs-fr-10:493/1645/1675 | TC-CH-SLA-020/021/022, TC-CH-QT-010/011/032 | ✅ 100% |

**Total BR coverage: 14/14 valid + 1/2 partial = 14.5/15 = 97%** ✅ (target ≥95%)

---

## 2. AC Coverage

| AC | Source FR | TC cover | Coverage |
|----|-----------|----------|----------|
| FR-VIII-10 AC1 (QTHT truy cập SLA hiển thị danh sách) | srs-fr-10:504 | TC-CH-SLA-001 | ✅ |
| FR-VIII-10 AC2 (Thêm cấu hình mới + nhập đủ trường + lưu) | srs-fr-10:505 | ⚠️ Skipped — UI inline-only 4 record, không có Add new (verify thực tế Phase B) | ⚠️ A6 fill |
| FR-VIII-10 AC3 (Sửa thời hạn / mức CB → validate + lưu) | srs-fr-10:506 | TC-CH-SLA-003/004 | ✅ |
| FR-II-NEW-02 AC1 (TW tạo TW_QUOC_GIA → 63 ĐP đọc) | srs-fr-02:961 | TC-CH-MPH-001 + TC-CH-MPH-012 | ✅ |
| FR-II-NEW-02 AC2 (BN tạo BN_RIENG → chỉ BN mình thấy) | srs-fr-02:962 | TC-CH-MPH-002 + TC-CH-MPH-011 | ✅ |
| FR-II-NEW-02 AC3 (DP tạo DP_RIENG → chỉ DP mình thấy) | srs-fr-02:963 | TC-CH-MPH-003 + TC-CH-MPH-012 | ✅ |
| FR-II-NEW-02 AC4 (DP soạn phản hồi → dropdown 2 nhóm TW + ĐP mình) | srs-fr-02:964 | TC-CH-MPH-068 | ✅ |
| FR-II-NEW-02 AC5 (BN bypass UI → BE reject 403) | srs-fr-02:965 | TC-CH-MPH-033 | ✅ |
| FR-II-NEW-02 AC6 (DP cố sửa mẫu TW → BE 403) | srs-fr-02:966 | TC-CH-MPH-036 | ✅ |
| FR-II-NEW-02 AC7 (XSS noi_dung sanitize) | srs-fr-02:967 | TC-CH-MPH-004 | ✅ |
| FR-VIII-29 AC1 (Thêm ngày lễ → SLA tính trừ) | srs-fr-10:1432 | TC-CH-NL-001 + TC-CH-NL-040 | ✅ |
| FR-VIII-29 AC2 (Import file Excel → cập nhật hàng loạt) | srs-fr-10:1433 | TC-CH-NL-020 | ✅ |
| FR-VIII-29 AC3 (Calendar view → thấy tất cả ngày lễ) | srs-fr-10:1434 | TC-CH-NL-030 | ⚠️ partial (SPEC-CLARIFY-CAUHINH-06 — optional) |

**Total AC coverage: 11/13 ✅ + 2/13 ⚠️ = 84.6% explicit → A6 fill 1 TC (AC2 Add new SLA)** 

> AC FR-VIII-29 AC3 nếu BA confirm calendar view optional → coverage = 12/13 = 92.3%; nếu mandatory → cần Phase B fill thêm. Hiện ⚠️ partial.

---

## 3. Error Code Coverage

| Error code | Severity | Source | TC cover | Coverage |
|------------|----------|--------|----------|----------|
| ERR-SLA-01 | ERROR | srs-fr-10:499 | TC-CH-SLA-010, 011 | ✅ |
| ERR-SLA-02 | ERROR | srs-fr-10:500 | TC-CH-SLA-012, 013, 014 | ✅ |
| ERR-SLA-03 | ERROR | srs-fr-10:501 | ⚠️ Skipped — UI inline-only không có Add new để duplicate | ⚠️ A6 fill |
| ERR-MPH-01 | ERROR | srs-fr-02:934 | TC-CH-MPH-030 | ✅ |
| ERR-MPH-02 | ERROR | srs-fr-02:935 | TC-CH-MPH-031 | ✅ |
| ERR-MPH-03 | ERROR | srs-fr-02:936 | TC-CH-MPH-032 | ✅ |
| ERR-MPH-04 | ERROR (403) | srs-fr-02:937 | TC-CH-MPH-033, 034, TC-CH-PERM-042 | ✅ |
| ERR-MPH-05 | ERROR | srs-fr-02:938 | TC-CH-MPH-035 | ✅ |
| ERR-MPH-06 | ERROR (403) | srs-fr-02:939 | TC-CH-MPH-036, 037, 038 | ✅ |
| ERR-NL-01 | ERROR | srs-fr-10:1423 | TC-CH-NL-050, TC-CH-PERM-041 | ✅ |
| ERR-NL-02 | ERROR | srs-fr-10:1424 | TC-CH-NL-010, 011 | ✅ |
| ERR-NL-03 | WARNING | srs-fr-10:1425 | TC-CH-NL-012 | ✅ |

**Total Error code coverage: 11/12 ✅ → A6 fill 1 TC (ERR-SLA-03)**

---

## 4. Permission Combo Coverage

| Combo | TC cover | Coverage |
|-------|----------|----------|
| QTHT × Tab 1 CRUD | TC-CH-SLA-001..006 | ✅ |
| QTHT × Tab 2 (deprecated) | TC-CH-PC-001 | ✅ |
| QTHT × Tab 3 READ | TC-CH-MPH-013, TC-CH-MPH-048 | ✅ |
| QTHT × Tab 4 CRUD | TC-CH-QT-001..004 | ✅ |
| QTHT × Ngày lễ CRUD | TC-CH-NL-001..005 | ✅ |
| CB_NV_TW × Tab 1/2/4 BLOCK | TC-CH-SLA-030, TC-CH-QT-020, TC-CH-PERM-002 | ✅ |
| CB_NV_TW × Tab 3 CRUD TW | TC-CH-MPH-001, TC-CH-MPH-010 | ✅ |
| CB_NV_BN × Tab 3 CRUD BN | TC-CH-MPH-002, TC-CH-MPH-011 | ✅ |
| CB_NV_DP × Tab 3 CRUD DP | TC-CH-MPH-003, TC-CH-MPH-012 | ✅ |
| CB_PD × Tab 3 READ scope | TC-CH-PERM-005..007, TC-CH-MPH-014 | ✅ |
| CB_PD × Tab 1/2/4 BLOCK | TC-CH-SLA-031, TC-CH-PERM-005..007 | ✅ |
| Tier 2 (DN/CG/TVV/NHT) × ANY tab BLOCK | TC-CH-SLA-032, TC-CH-NL-051, TC-CH-PERM-020/021, TC-CH-QT-022 | ✅ |
| Cross-don_vi (BN A vs BN B; DP A vs DP B) | TC-CH-MPH-037, TC-CH-MPH-038, TC-CH-PERM-010..012 | ✅ |
| Cross-cấp UI auto-fill bypass via API | TC-CH-MPH-033/034, TC-CH-PERM-042 | ✅ |
| IDOR direct API (SLA/Ngày lễ/Mẫu PH) | TC-CH-PERM-040/041, TC-CH-MPH-067 | ✅ |

**Total Permission combo: 15/15 = 100%** ✅

---

## 5. SM Transition Coverage

| Transition | TC cover | Coverage |
|------------|----------|----------|
| MAU_PHAN_HOI: KICH_HOAT ⟷ VO_HIEU_HOA | TC-CH-MPH-022 | ✅ |
| NGAY_LE: is_deleted 0 → 1 (soft delete) | TC-CH-NL-004 | ✅ |

**Total SM coverage: 2/2 = 100%** ✅

---

## 6. Output Field Coverage

### Tab 1 SLA (8 input fields)

| Field | TC cover | Coverage |
|-------|----------|----------|
| loai_yeu_cau | TC-CH-SLA-001 | ✅ |
| ten_loai | TC-CH-SLA-001 | ✅ |
| thoi_han_ngay | TC-CH-SLA-003, 010, 011, 041, 042 | ✅ |
| canh_bao_1 | TC-CH-SLA-004, 012, 013, 014 | ✅ |
| canh_bao_2 | TC-CH-SLA-004, 012, 013, 014 | ✅ |
| qua_han_phan_tram (= 100, readonly) | TC-CH-SLA-001 | ✅ |
| gui_email_canh_bao | TC-CH-SLA-005 | ✅ |
| gui_thong_bao_app | ⚠️ partial — A6 fill | ⚠️ |
| QH-NT (SCR-VIII-06 only) | TC-CH-SLA-006 | ⚠️ SPEC-CLARIFY |

### Tab 3 Mẫu phản hồi (8 input fields)

| Field | TC cover | Coverage |
|-------|----------|----------|
| ten_mau | TC-CH-MPH-001/030, TC-CH-MPH-006/064/065 | ✅ |
| linh_vuc_id | TC-CH-MPH-001/032/042 | ✅ |
| noi_dung | TC-CH-MPH-001/004/005/031 | ✅ |
| mo_ta | TC-CH-MPH-065 (XSS) | ⚠️ partial (no main happy) |
| tu_khoa | ⚠️ no TC — A6 fill | ⚠️ |
| trang_thai | TC-CH-MPH-022/043 | ✅ |
| pham_vi_ap_dung | TC-CH-MPH-001/002/003/035, TC-CH-PERM-033 | ✅ |
| don_vi_id | TC-CH-MPH-001 (auto) | ✅ |

### FR-VIII-29 Ngày lễ (5 input fields)

| Field | TC cover | Coverage |
|-------|----------|----------|
| ten_ngay_le | TC-CH-NL-001/013 | ✅ |
| ngay_bat_dau | TC-CH-NL-001/014 | ✅ |
| ngay_ket_thuc | TC-CH-NL-001/010/011 | ✅ |
| mo_ta | ⚠️ partial — A6 fill | ⚠️ |
| lap_lai_hang_nam | TC-CH-NL-002 | ✅ |

**Total Output field coverage: 17/22 explicit + 5 partial = 77% explicit → A6 fill 4-5 TC** ⚠️

---

## 7. Gap Analysis (forward → A6 fix inline)

| Gap # | Mô tả | Suggested TC | A6 action |
|-------|-------|--------------|-----------|
| A5-GAP-CH-01 | FR-VIII-10 AC2 "Thêm mới cấu hình SLA" — verify spec UI thực tế (inline-only 4 record fixed hay có Add new?) | TC verify behavior thực tế: nếu có nút Add new → test tạo loại YC mới | A6 fill inline → 01-TC-tab-sla.md, Section A |
| A5-GAP-CH-02 | ERR-SLA-03 (loại YC duplicate) — chưa cover vì TC Add new skip | TC verify behavior nếu cố tạo trùng loai_yeu_cau | A6 fill inline → 01-TC-tab-sla.md (paired với GAP-01) |
| A5-GAP-CH-03 | Toggle `gui_thong_bao_app` chưa có TC riêng | TC toggle OFF/ON → verify scheduled job không gửi | A6 fill inline → 01-TC-tab-sla.md, Section B |
| A5-GAP-CH-04 | Mẫu phản hồi field `tu_khoa` chưa có TC happy + edge | TC verify tu_khoa được lưu + dùng để search | A6 fill inline → 03-TC-tab-mau-phan-hoi.md, Section A |
| A5-GAP-CH-05 | Mẫu phản hồi field `mo_ta` chỉ có XSS test, thiếu happy path | TC verify mo_ta lưu + hiển thị | A6 fill inline → 03-TC-tab-mau-phan-hoi.md, Section A |
| A5-GAP-CH-06 | Ngày lễ field `mo_ta` chưa có TC | TC verify mo_ta lưu | A6 fill inline → 05-TC-ngay-le.md, Section A |
| A5-GAP-CH-07 | Tab 3 — empty state khi tất cả filter no match (sau khi đã có data) | TC verify empty state khác empty state khi DB clean | A6 fill inline → 03-TC-tab-mau-phan-hoi.md, Section E |

**Forward to A6:** 7 TC mới merge inline. BR + Permission + SM + Error đầy đủ; chỉ Output field + 2 AC partial.

---

## 8. Coverage Summary

| Loại | Target | Actual (sau A6) | Status |
|------|--------|-----------------|--------|
| BR | ≥95% | 97% | ✅ |
| AC | 100% | 92.3% (sau A6 fill 1 + AC FR-VIII-29 AC3 partial pending BA) | ⚠️ |
| Error code | 100% | 100% (sau A6 fill ERR-SLA-03) | ✅ |
| Permission | 100% | 100% | ✅ |
| SM | 100% | 100% | ✅ |
| Output field | 100% | 91% (sau A6 fill 5) | ⚠️ |

**Phase A Acceptance Status (sau A6):** 4/6 dimension ≥ target ✅; 2/6 partial pending SPEC-CLARIFY (AC FR-VIII-29 AC3, AC FR-VIII-10 AC2 chờ BA confirm spec).
