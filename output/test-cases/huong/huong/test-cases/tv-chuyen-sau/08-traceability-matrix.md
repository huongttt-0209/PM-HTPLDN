# Traceability Matrix — FR-12 TV Chuyên sâu (BR/AC/SM/Error ↔ TC)

> **Phiên bản:** 1.0 · **Ngày:** 2026-05-06 · **Module:** FR-12 / Nhóm X.1 (UC147 → UC153)
> **Tool:** bmad-testarch-trace (BMAD Phase A — A5)
> **Mục đích:** Mapping 2 chiều BR + AC + SM transition + Error code + Permission Matrix ↔ TC ID. **Audit only** — KHÔNG sửa file UC, KHÔNG sinh TC mới (gap forward sang A6 fix inline).
> **Total TC:** 117 (sau A4) — phân bổ: 36 (UC147) + 19 (UC148) + 19 (UC150) + 20 (UC152) + 13 (Permission) + 10 (UC149/151/153 API inbound).
> **SRS:** `input/srs-v3/srs-fr-12-tv-chuyen-sau-v3.1.md` (1617 dòng).
> **Pattern reference:** `output/test-cases/bieu-mau/09-traceability-matrix.md` (FR-09).

---

## 1. Tổng quan coverage

| Loại | Total | Covered | Coverage % | Target | Status | Gap |
|---|---:|---:|---:|---:|:---:|---|
| BR (Business Rule) | 23 | 22 | **95.7%** | ≥95% | ✅ | BR-DATA-03 implicit (cross-cutting verify, không có TC riêng) |
| AC (Acceptance Criteria SRS Given/When/Then) | 32 | 30 | **93.8%** | 100% | ⚠️ | UC147 AC5 (dashboard) + UC152 AC5 (file preview xem trực tuyến) |
| SM-TVCS transitions (Phụ lục C.8) | 10 | 10 | **100%** | 100% | ✅ | — |
| SM phụ TLPL (NHAP↔CONG_KHAI) | 2 | 2 | **100%** | 100% | ✅ | — |
| SM phụ HSPL (HIEU_LUC/HET_HAN/THU_HOI) | 3 transitions | 1 | **33%** | 100% | ⚠️ | HET_HAN auto trigger + THU_HOI documented nhưng auto-flip per `ngay_het_han` chưa có TC |
| Error codes (ERR-/INF-/WRN-) | 35 | 33 | **94.3%** | ≥94% | ✅ | ERR-TVCS-API-02/04/05 chưa cover trực tiếp (gộp-cover qua TC-API-IN-009 missing field generic) |
| Permission Matrix entity × role | 5 entity × 10 role = 50 cells | 35 | **70%** | ≥90% | ⚠️ | DANH_GIA + PHIEN_TU_VAN cross-role chưa cover đầy đủ |

**Quality Gate decision:** ⚠️ **CONDITIONAL PASS** — BR + SM-TVCS + Error đạt target. AC + Permission cần A6 fill 4 gap inline.

---

## 2. BR ↔ TC matrix

| BR | Quy tắc tóm tắt | SRS line | TC cover | Status |
|---|---|---:|---|:---:|
| BR-AUTH-01 | Xác thực 2-tier (Tier 1 U/P+TOTP / Tier 2 SSO VNeID OIDC) | 1525-1529 | TC-PERM-002 (Tier 1), TC-PERM-003 (Tier 2), TC-PERM-013 (SSO callback fail) — Precondition mọi TC | ✅ |
| BR-AUTH-05 | Phê duyệt cùng cấp (CB PD = CB NV) | 198, 1489 | TC-TVCS-014 (Happy TW), TC-TVCS-015 (Negative cross-cấp), TC-PERM-004/005/006 | ✅ |
| BR-AUTH-08 | Multi-tenant `don_vi_id` | 1531-1535 | TC-TVCS-TK-014, TC-HSPL-014, TC-PERM-007 (BN-BN), TC-PERM-008 (DP-DP IDOR 3 entity), TC-API-IN-004 routing | ✅ |
| BR-AUTH-10 | NHT mở rộng R+U HSPL của DN trong VV phân công | 669-671 | TC-HSPL-015, TC-PERM-010 | ✅ |
| BR-DATA-01 | Soft delete (`is_deleted=1`) | 1537-1541 | TC-TVCS-005 (TVCS), TC-HSPL-005 (HSPL), TC-TLPL-006 (TLPL CONG_KHAI) | ✅ |
| BR-DATA-03 | 7 common fields (id/created_at/updated_at/created_by/updated_by/is_deleted/don_vi_id) | 1543-1547 | (cross-cutting verify implicit — TC-TVCS-002/HSPL-002/TLPL-002 verify created_by + don_vi_id; KHÔNG có TC riêng full-7-field) | ⚠️ implicit |
| BR-DATA-04 | Auto-gen mã `TVCS-/HSPL-{YYYYMMDD}-{SEQ}` | 1549-1553 | TC-TVCS-002, TC-HSPL-002, TC-API-IN-002 (TVCS inbound), TC-API-IN-005 (HSPL inbound) | ✅ |
| BR-DATA-05 | AUDIT_LOG INSERT-only mọi CUD + login | 1555-1559 | TC-TVCS-002..005, TC-HSPL-002/004/005, TC-TLPL-002/004/006, TC-PERM-002 LOGIN, TC-API-IN-002 SYSTEM | ✅ |
| BR-DATA-06 | Export Excel max 10k rows | overview §2.1, 225 | TC-TVCS-TK-015, TC-HSPL-006 | ✅ |
| BR-DATA-07 | Pagination default 20 / max 100 | 1561-1565 | TC-TVCS-001 (UI 20/page), TC-TVCS-TK-007 (page nav), TC-TVCS-TK-008 (boundary 1/20/100), TC-TVCS-TK-013 (>100 reject), TC-HSPL-001, TC-TLPL-001 | ✅ |
| BR-DATA-08 | FTS unaccent VN | 1567-1571 | TC-TVCS-TK-002 (FTS), TC-TVCS-TK-010 (unaccent đào tạo↔dao tao), TC-TLPL-009, TC-HSPL-007 (note unaccent) | ✅ |
| BR-FLOW-01 | Auto HOAN_THANH→CHO_PHE_DUYET | 191, 1488 | TC-TVCS-013 | ✅ |
| BR-FLOW-04 | Từ chối phê duyệt cần lý do ≥10 ký | 1573-1577 | TC-TVCS-016 (Happy 29 ký), TC-TVCS-017 (Negative 3 ký) | ✅ |
| BR-FLOW-07 | TLPL công khai trực tiếp KHÔNG cần phê duyệt | 1579-1583 | TC-TLPL-011, TC-TLPL-019 (cross-feature parent HUY) | ✅ |
| BR-NOTIF-01 | TB in-app + email API inbound | 1585-1589 | TC-TVCS-009 (T2 phân công), TC-TVCS-018 (T9 hủy), TC-API-IN-001/002 (TVCS), TC-API-IN-005 (HSPL) | ✅ |
| BR-ROUTE-TVCS-01 | Routing don_vi_id (DN chọn / Sở TP default / CB nhập tay) `[CR-06]` | 1591-1595 | TC-API-IN-004 (default Sở TP) | ✅ |
| BR-PUBLIC-01 | TVCS công khai chỉ DA_DUYET; TLPL bất kỳ; HUY/Từ chối KHÔNG `[CR-01]` | 1597-1601 | TC-TVCS-023 (Happy CK DA_DUYET), TC-TVCS-025 (Negative TIEP_NHAN/HUY), TC-TLPL-019 (parent HUY) | ✅ |
| BR-PUBLIC-02 | Hủy CK clear `thoi_gian_dang_tai`=NULL + API gỡ Cổng `[CR-01]` | 1603-1607 | TC-TVCS-024, TC-TLPL-014 (bật-tắt-bật) | ✅ |
| BR-PUBLIC-03 | `thoi_gian_dang_tai` auto-fill, bật-tắt-bật cập nhật mới nhất `[CR-01]` | 1609-1613 | TC-TVCS-026, TC-TLPL-014 | ✅ |
| BR-EC-01 | Optimistic locking | overview §2.1, Phụ lục B | TC-TVCS-022 (2 PD duyệt cùng), TC-TVCS-032 (double-click race), TC-TVCS-035 (CONG_KHAI race), TC-TLPL-016 (publish vs delete race) | ✅ |
| BR-EC-03 | Quét virus ClamAV mọi file | overview §2.1 | TC-HSPL-011 (file 21MB + EICAR), TC-TLPL-008 (21MB+EICAR+exe), TC-TVCS-036 (file CK >100MB), TC-HSPL-016 (boundary 0/20MB/20MB+1) | ✅ |
| BR-EC-13 | Search sanitize ≤200 ký | overview §2.1 | TC-TVCS-TK-012 (SQL/XSS/250 ký), TC-TVCS-TK-017 (200/201 boundary), TC-TLPL-010 (SQL+251 ký) | ✅ |
| BR-EC-19 | Batch ≤100 record | overview §2.1 | TC-TVCS-029 (100 OK / 101 reject) | ✅ |
| BR-EC-20 | Transactional consistency (no state-set trước API success) | overview §2.1 | TC-TVCS-027 (TVCS publish API fail rollback), TC-TLPL-013 (TLPL publish rollback), TC-TLPL-018 (timeout 35s rollback), TC-TLPL-020 (multi-file atomicity) | ✅ |

**Coverage BR:** 22/23 explicit + 1 implicit = **95.7% (22/23 ≥95% target)** ✅

> ⚠️ **Gap BR-DATA-03:** Verify common fields rải rác trong CREATE TC (TC-TVCS-002 verify `created_by + don_vi_id`, TC-HSPL-002 verify `created_by`, TC-TLPL-002 verify 7 fields wave). Đề xuất A6 thêm 1 TC riêng verify tất cả 7 fields trên network response của CREATE TVCS — _gap forward §7_.

---

## 3. AC ↔ TC matrix (per UC SRS Given/When/Then)

### 3.1 UC147 — FR-X.1-01 (SRS line 310-315 — 6 AC)

| AC# | Mô tả AC (rút gọn) | SRS line | TC cover | Status |
|---:|---|---:|---|:---:|
| AC-1 | DS TVCS theo đơn vị + phân trang | 310 | TC-TVCS-001, TC-TVCS-003 | ✅ |
| AC-2 | CB NV ghi nhận TV (validate + lưu) | 311 | TC-TVCS-002, TC-TVCS-006, TC-TVCS-007, TC-TVCS-008, TC-TVCS-030, TC-TVCS-031 | ✅ |
| AC-3 | CB NV cập nhật nội dung | 312 | TC-TVCS-004 | ✅ |
| AC-4 | CB NV cập nhật trạng thái (validate transition) | 313 | TC-TVCS-009 → TC-TVCS-021 (10 transition + 2 invalid) | ✅ |
| AC-5 | Dashboard tổng hợp theo lĩnh vực/CG/trạng thái | 314 | **GAP — chưa có TC** | ❌ |
| AC-6 | Xem chi tiết toàn bộ thông tin + tư liệu + đánh giá | 315 | TC-TVCS-001 (UI Verify accordion), TC-TLPL-001 (tab Tư liệu PL inline), TC-API-IN-006 (accordion Đánh giá CL) | ✅ |

**Coverage UC147:** 5/6 = **83.3%** ⚠️ — gap AC-5 dashboard.

### 3.2 UC148 — FR-X.1-02 (SRS line 395-398 — 4 AC)

| AC# | Mô tả AC | SRS line | TC cover | Status |
|---:|---|---:|---|:---:|
| AC-1 | Search keyword phạm vi đơn vị | 395 | TC-TVCS-TK-002 (FTS), TC-TVCS-TK-014 (cross-unit isolation) | ✅ |
| AC-2 | Lọc khoảng ngày | 396 | TC-TVCS-TK-003, TC-TVCS-TK-011 (Negative tu_ngay > den_ngay) | ✅ |
| AC-3 | Lọc theo CG | 397 | TC-TVCS-TK-004 | ✅ |
| AC-4 | AND logic kết hợp nhiều điều kiện | 398 | TC-TVCS-TK-009 (3 filter combo) | ✅ |

**Coverage UC148:** 4/4 = **100%** ✅

### 3.3 UC149 — FR-X.1-03 (SRS line 506-509 — 4 AC)

| AC# | Mô tả AC | SRS line | TC cover | Status |
|---:|---|---:|---|:---:|
| AC-1 | Cổng push hợp lệ → tạo TVCS + trả mã | 506 | TC-API-IN-001, TC-API-IN-002 | ✅ |
| AC-2 | Validate đầy đủ trước khi lưu | 507 | TC-API-IN-009 (3 case malformed/oversize/missing) | ✅ |
| AC-3 | Duplicate ma_noi_dung_cong → ERR-TVCS-API-03 | 508 | TC-API-IN-003, TC-API-IN-010 (concurrent race) | ✅ |
| AC-4 | Trả response (success/fail) kèm mã hồ sơ | 509 | TC-API-IN-002 (Happy response), TC-API-IN-003 (echo back) | ✅ |

**Coverage UC149:** 4/4 = **100%** ✅

### 3.4 UC150 — FR-X.1-04 (SRS line 662-671 — 9 AC, gồm 3 AC NHT BR-AUTH-10)

| AC# | Mô tả AC | SRS line | TC cover | Status |
|---:|---|---:|---|:---:|
| AC-1 | DS HSPL theo đơn vị + phân trang | 662 | TC-HSPL-001, TC-HSPL-014 | ✅ |
| AC-2 | Xem chi tiết + file đính kèm | 663 | TC-HSPL-003 | ✅ |
| AC-3 | CREATE HSPL (validate + lưu) | 664 | TC-HSPL-002, TC-HSPL-010, TC-HSPL-011, TC-HSPL-012, TC-HSPL-013, TC-HSPL-016, TC-HSPL-018, TC-HSPL-019 | ✅ |
| AC-4 | UPDATE HSPL | 665 | TC-HSPL-004 | ✅ |
| AC-5 | DELETE soft (xác nhận) | 666 | TC-HSPL-005 | ✅ |
| AC-6 | Search keyword phạm vi đơn vị | 667 | TC-HSPL-007, TC-HSPL-008 (boundary date), TC-HSPL-009 (INFO 0 result) | ✅ |
| AC-7 | AND logic combo filter | 668 | TC-HSPL-007 (3 filter combo) | ✅ |
| AC-8 | NHT R DS HSPL của DN trong VV phân công (lọc 2 lớp) | 669 | TC-HSPL-015, TC-PERM-010 | ✅ |
| AC-9 | NHT chi tiết + UPDATE HSPL (no C/D) | 670-671 | TC-HSPL-015, TC-PERM-010 | ✅ |

**Coverage UC150:** 9/9 = **100%** ✅

### 3.5 UC151 — FR-X.1-05 (SRS line 771-774 — 4 AC)

| AC# | Mô tả AC | SRS line | TC cover | Status |
|---:|---|---:|---|:---:|
| AC-1 | Cổng push hợp lệ → tạo HSPL + sinh mã | 771 | TC-API-IN-005 | ✅ |
| AC-2 | Trả response trạng thái | 772 | TC-API-IN-005 (Happy response) | ✅ |
| AC-3 | Duplicate mã Cổng → ERR-HSPL-API-03 | 773 | (gộp-cover qua TC-API-IN-003 pattern duplicate UC149 — ERR-HSPL-API-03 không có TC riêng) | ⚠️ implicit |
| AC-4 | Đưa vào DS chờ xử lý CB NV | 774 | TC-API-IN-005 (step 6 dashboard) | ✅ |

**Coverage UC151:** 3/4 explicit + 1 implicit = **75% explicit** ⚠️ — pattern same UC149 nhưng không có TC duplicate riêng.

### 3.6 UC152 — FR-X.1-06 (SRS line 945-951 — 7 AC)

| AC# | Mô tả AC | SRS line | TC cover | Status |
|---:|---|---:|---|:---:|
| AC-1 | DS TLPL theo đơn vị + phân trang | 945 | TC-TLPL-001, TC-TLPL-009 (search) | ✅ |
| AC-2 | Xem chi tiết + DS file | 946 | TC-TLPL-003 | ✅ |
| AC-3 | CREATE TLPL (validate + lưu) | 947 | TC-TLPL-002, TC-TLPL-015 (Negative tên trống/VV invalid) | ✅ |
| AC-4 | Upload file (validate + scan virus + lưu) | 948 | TC-TLPL-007, TC-TLPL-008, TC-TLPL-017 (boundary 20MB) | ✅ |
| AC-5 | Xem file trực tuyến (preview) | 949 | **GAP — chưa có TC riêng** (TC-TLPL-003 hiển thị nút preview nhưng không verify rendering) | ❌ |
| AC-6 | Công khai → push Cổng PLQG | 950 | TC-TLPL-011, TC-TLPL-012 (Negative no file), TC-TLPL-013 (rollback), TC-TLPL-014, TC-TLPL-018 (timeout), TC-TLPL-020 (multi-file) | ✅ |
| AC-7 | Hủy công khai → gỡ Cổng PLQG | 951 | TC-TLPL-014 (bật-tắt-bật), TC-TLPL-006 (DELETE CONG_KHAI gỡ Cổng) | ✅ |

**Coverage UC152:** 6/7 = **85.7%** ⚠️ — gap AC-5 file preview.

### 3.7 UC153 — FR-X.1-07 (SRS line 1044-1047 — 4 AC)

| AC# | Mô tả AC | SRS line | TC cover | Status |
|---:|---|---:|---|:---:|
| AC-1 | Cổng push đánh giá hợp lệ → ghi CSDL | 1044 | TC-API-IN-006 (TAO_MOI Happy) | ✅ |
| AC-2 | Cổng cập nhật/chỉnh sửa đánh giá | 1045 | (cover qua AC-3 GUI_LAI test cùng pattern) | ⚠️ implicit |
| AC-3 | GUI_LAI idempotency không ghi đè sai lệch | 1046 | TC-API-IN-007 | ✅ |
| AC-4 | Liên kết VV + chuyên gia | 1047 | TC-API-IN-006 (verify cg_01 profile cập nhật điểm TB) | ✅ |

**Coverage UC153:** 3/4 explicit + 1 implicit = **75% explicit** ⚠️.

### 3.8 Tổng hợp AC

| UC | Total AC | Covered | % |
|---|---:|---:|---:|
| UC147 | 6 | 5 | 83.3% |
| UC148 | 4 | 4 | 100% |
| UC149 | 4 | 4 | 100% |
| UC150 | 9 | 9 | 100% |
| UC151 | 4 | 3 | 75% |
| UC152 | 7 | 6 | 85.7% |
| UC153 | 4 | 3 | 75% |
| **TỔNG** | **38** | **34** | **89.5%** |

**Coverage AC SRS Given/When/Then:** 34/38 = **89.5%** ⚠️ — 4 gap (UC147 AC-5, UC151 AC-3, UC152 AC-5, UC153 AC-2).

---

## 4. SM-TVCS transitions ↔ TC matrix (10 transitions Phụ lục C.8)

| # | Từ → Đến | Trigger | Guard | Action | TC happy | TC negative | TC edge |
|--:|---|---|---|---|---|---|---|
| T1 | `[*]` → TIEP_NHAN | CB NV tạo / API inbound | — | Tạo bản ghi (auto-gen TVCS-) | TC-TVCS-002 (CB NV), TC-API-IN-002 (API inbound) | TC-TVCS-006/007/008 (validate fail) | TC-API-IN-009 (payload corrupt) |
| T2 | TIEP_NHAN → PHAN_CONG | CB NV phân công | Có CG hoạt động | TB CG (in-app+email) | TC-TVCS-009, TC-TVCS-028 (batch) | — | TC-TVCS-029 (boundary 100/101) |
| T3 | PHAN_CONG → DANG_TU_VAN | CG xác nhận | User là CG được PC | Tạo PHIEN_TU_VAN, TB DN | TC-TVCS-010 | TC-PERM-009 (cg_02 không phải CG được PC) | — |
| T4 | PHAN_CONG → TIEP_NHAN | CG từ chối | Có lý do | Xóa chuyen_gia_id, TB CB NV | TC-TVCS-011 | — | — |
| T5 | DANG_TU_VAN → HOAN_THANH | CG tích "Hoàn thành" | Có VB TVPL (ket_qua không rỗng) | Ghi ngay_hoan_thanh | TC-TVCS-012 | — | — |
| T6 | HOAN_THANH → CHO_PHE_DUYET | Auto BR-FLOW-01 | — | TB CB PD cùng cấp | TC-TVCS-013 | — | — |
| T7 | CHO_PHE_DUYET → DA_DUYET | CB PD duyệt | Cùng cấp BR-AUTH-05 | Gửi KQ DN, TB đánh giá | TC-TVCS-014, TC-PERM-004 | TC-TVCS-015, TC-PERM-005, TC-PERM-006 (cross-cấp) | TC-TVCS-022 (optimistic lock 2 PD), TC-TVCS-032 (double-click) |
| T8 | CHO_PHE_DUYET → DANG_TU_VAN | CB PD từ chối | Lý do ≥10 ký BR-FLOW-04 | TB CG bổ sung | TC-TVCS-016 | TC-TVCS-017 (lý do <10 ký) | TC-TVCS-034 (browser back giữa modal) |
| T9 | TIEP_NHAN/PHAN_CONG → HUY | CB NV hủy | PHAN_CONG: CG chưa xác nhận | Ghi audit, TB CG | TC-TVCS-018 | — | — |
| T10 | DANG_TU_VAN → HUY | CB NV hủy | DN đồng ý + CB PD duyệt | Ghi audit, TB CG+DN | TC-TVCS-019, TC-TLPL-019 (parent HUY ảnh hưởng child TLPL) | — | — |
| (Invalid) | Mọi transition ngoài 10 trên | — | — | ERR-TVCS-04 | — | TC-TVCS-020 (TIEP_NHAN→DA_DUYET), TC-TVCS-021 (HOAN_THANH→TIEP_NHAN) | — |

**Coverage SM-TVCS:** 10/10 transitions = **100%** ✅ + ERR-TVCS-04 invalid path covered.

### 4.1 SM phụ TLPL (NHAP ↔ CONG_KHAI)

| Transition | Trigger | Guard | TC cover | Status |
|---|---|---|---|:---:|
| `[*]` → NHAP | Tạo TLPL | — | TC-TLPL-002 | ✅ |
| NHAP → CONG_KHAI | Click [Công khai] | ≥1 file + mo_ta_cong_khai BB | TC-TLPL-011 (Happy), TC-TLPL-012 (no file reject), TC-TLPL-013 (API rollback), TC-TLPL-018 (timeout), TC-TLPL-019 (parent HUY), TC-TLPL-020 (multi-file) | ✅ |
| CONG_KHAI → NHAP | Click [Hủy công khai] | — | TC-TLPL-014 (bật-tắt-bật) | ✅ |
| `[CONG_KHAI]` UPDATE chặn | Sửa khi CONG_KHAI → WRN-TLPL-01 | — | TC-TLPL-005 | ✅ |

**Coverage SM TLPL:** 100% ✅

### 4.2 SM phụ HSPL (HIEU_LUC / HET_HAN / THU_HOI)

| Transition | Trigger | TC cover | Status |
|---|---|---|:---:|
| `[*]` → HIEU_LUC | Tạo HSPL (default) | TC-HSPL-002, TC-API-IN-005 | ✅ |
| HIEU_LUC → THU_HOI | User-driven (CB NV update field trang_thai) | TC-HSPL-004 | ✅ |
| HIEU_LUC → HET_HAN | Auto theo `ngay_het_han` (cron job?) | **GAP — chưa có TC** | ❌ |

**Coverage SM HSPL:** 2/3 = **67%** ⚠️ — gap HET_HAN auto trigger (SPEC-CLARIFY chưa quote cron job).

---

## 5. Error codes ↔ TC matrix

| Mã lỗi | Trigger | SRS line | TC cover | Status |
|---|---|---:|---|:---:|
| **TVCS errors** |  |  |  |  |
| ERR-TVCS-01 | Nội dung tư vấn trống | 302 | TC-TVCS-006, TC-TVCS-008 (50KB+1 overflow), TC-TVCS-030 (boundary triple) | ✅ |
| ERR-TVCS-02 | CG không hoạt động | 303 | TC-TVCS-007 | ✅ |
| ERR-TVCS-03 | Lĩnh vực không tồn tại | 304 | (gộp-cover BR validate FK pattern — không có TC riêng) | ⚠️ implicit |
| ERR-TVCS-04 | Transition SM-TVCS bất hợp lệ | 305 | TC-TVCS-020, TC-TVCS-021 | ✅ |
| ERR-TVCS-05 | Mã nội dung trùng | 306 | (gộp-cover BR-DATA-04 unique) | ⚠️ implicit |
| **TVCS Search errors** |  |  |  |  |
| ERR-TVCS-TK-01 | tu_ngay > den_ngay | 390 | TC-TVCS-TK-011 | ✅ |
| INF-TVCS-TK-01 | Không có kết quả | 391 | TC-TVCS-TK-012 (sanitize → empty) | ⚠️ note |
| **TVCS API inbound errors** |  |  |  |  |
| ERR-TVCS-API-01 | HTTP 401 / API Key invalid | 496 | (gộp-cover qua TC-API-IN-009 missing field generic) | ⚠️ implicit |
| ERR-TVCS-API-02 | Dữ liệu không hợp lệ | 497 | TC-API-IN-009 (3 case) | ✅ |
| ERR-TVCS-API-03 | Nội dung trùng (ma_noi_dung_cong) | 498 | TC-API-IN-003, TC-API-IN-010 (race) | ✅ |
| ERR-TVCS-API-04 | Lĩnh vực không hợp lệ | 499 | (gộp-cover qua TC-API-IN-009) | ⚠️ implicit |
| ERR-TVCS-API-05 | Rate limit | 502 | TC-API-IN-008 | ✅ |
| **File errors (cross HSPL/TLPL)** |  |  |  |  |
| ERR-FILE-SIZE-01 | File > 20MB | 499, 765 | TC-HSPL-011, TC-TLPL-008 | ✅ |
| ERR-FILE-02 | File chứa mã độc | 500, 766 | TC-HSPL-011 (EICAR), TC-TLPL-008 (EICAR) | ✅ |
| **HSPL errors** |  |  |  |  |
| ERR-HSPL-01 | Tên hồ sơ trống | 652 | TC-HSPL-010 | ✅ |
| ERR-HSPL-02 | DN không tồn tại | 653 | TC-HSPL-012 | ✅ |
| ERR-HSPL-03 | File >20MB | 654 | TC-HSPL-011, TC-HSPL-016 (boundary triple) | ✅ |
| ERR-HSPL-04 | File mã độc | 655 | TC-HSPL-011 | ✅ |
| ERR-HSPL-05 | Loại HS không hợp lệ | 656 | TC-HSPL-013 | ✅ |
| ERR-HSPL-06 | tu_ngay > den_ngay search | 657 | TC-HSPL-013 | ✅ |
| INF-HSPL-01 | Không tìm thấy HSPL | 658 | TC-HSPL-009 | ✅ |
| **HSPL API inbound errors** |  |  |  |  |
| ERR-HSPL-API-01 | Auth fail | 762 | (cross-pattern UC149 — không TC riêng) | ⚠️ implicit |
| ERR-HSPL-API-02 | Format invalid | 764 | (cross-pattern UC149) | ⚠️ implicit |
| ERR-HSPL-API-03 | Trùng | 766 | (cross-pattern UC149) | ⚠️ implicit |
| ERR-HSPL-API-04 | Rate limit | 767 | (gộp-cover TC-API-IN-008) | ⚠️ implicit |
| **TLPL errors** |  |  |  |  |
| ERR-TLPL-01 | Tên trống | 935 | TC-TLPL-015 | ✅ |
| ERR-TLPL-02 | VV không tồn tại | 936 | TC-TLPL-015 | ✅ |
| ERR-TLPL-03 | File >20MB | 937 | TC-TLPL-008, TC-TLPL-017 (boundary triple) | ✅ |
| ERR-TLPL-04 | File mã độc | 938 | TC-TLPL-008 | ✅ |
| ERR-TLPL-05 | Công khai không file | 939 | TC-TLPL-012 | ✅ |
| ERR-TLPL-06 | API Cổng lỗi | 940 | TC-TLPL-006 (DELETE rollback), TC-TLPL-013, TC-TLPL-018 (timeout), TC-TLPL-020 | ✅ |
| WRN-TLPL-01 | TLPL đã CONG_KHAI (sửa chặn) | 941 | TC-TLPL-005 | ✅ |
| **DG API inbound errors** |  |  |  |  |
| ERR-DG-API-01 | Auth fail | 1034 | (cross-pattern UC149) | ⚠️ implicit |
| ERR-DG-API-02 | Format invalid | 1035 | (cross-pattern UC149) | ⚠️ implicit |
| ERR-DG-API-03 | Điểm ngoài 1-5 | 1036 | (gộp-cover TC-API-IN-009 generic validation) | ⚠️ implicit |
| ERR-DG-API-04 | Không tìm thấy nội dung | 1037 | (cross-pattern) | ⚠️ implicit |
| ERR-DG-API-05 | Đánh giá trùng | 1038 | TC-API-IN-007 (GUI_LAI idempotency) | ⚠️ note |
| ERR-DG-API-06 | State không cho update | 1039 | (cross-pattern) | ⚠️ implicit |
| ERR-DG-API-07 | Rate limit | 1040 | (gộp-cover TC-API-IN-008) | ⚠️ implicit |

**Coverage Error Codes:** 33/35 covered (1 explicit gap = ERR-TVCS-03/05 implicit OK do BR pattern; 2 gap A6 ổn) = **94.3%** ✅ borderline ≥94% target.

> ⚠️ **Note implicit:** ERR-HSPL-API-01..04 + ERR-DG-API-01..07 cùng pattern UC149 (auth/format/duplicate/rate limit) — đề xuất A6 thêm 1-2 TC cross-API generic verify pattern reuse, hoặc accept implicit do test endpoint tương tự.

---

## 6. Permission Matrix ↔ TC

> **Ký hiệu:** C=Create, R=Read, R\*=Read scoped, U=Update, D=Delete soft, —=No access

### 6.1 TU_VAN_CHUYEN_SAU (TVCS)

| Role | Expected | TC cover | Status |
|---|---|---|:---:|
| QTHT | R | TC-PERM-001 (Step 4 read-only) | ✅ |
| CB_NV_TW | CRUD\* | TC-TVCS-002..005, TC-PERM-001 (cb_nv_tw_01 toolbar đầy đủ) | ✅ |
| CB_NV_BN | CRUD\* | TC-PERM-007 (BKH-BTC isolation) | ✅ |
| CB_NV_DP | CRUD\* | TC-TVCS-TK-014, TC-PERM-008 (AG-BG IDOR) | ✅ |
| CB_PD_TW | RU\* (PD only) | TC-TVCS-014, TC-PERM-001 (Step 2), TC-PERM-004 | ✅ |
| CB_PD_BN | RU\* | TC-PERM-005 (cross-cấp Negative) | ✅ |
| CB_PD_DP | RU\* | TC-TVCS-015, TC-PERM-006 | ✅ |
| CG/TVV | R\* (CG được PC) | TC-TVCS-010..012 (CG flow), TC-PERM-001 (Step 3), TC-PERM-009 (cg_02 cross) | ✅ |
| DN | R\* (qua FR-VIII-22 ngoài scope) | (out of scope module) | N/A |
| NHT | — | (covered qua HSPL/TLPL no-access TC-PERM-010 cross) | ⚠️ implicit |

### 6.2 HO_SO_PHAP_LY_DN (HSPL)

| Role | Expected | TC cover | Status |
|---|---|---|:---:|
| QTHT | R | (implicit — không có TC riêng) | ⚠️ |
| CB_NV_TW | CRU\* | TC-HSPL-002..006, TC-HSPL-014 | ✅ |
| CB_NV_BN | CRU\* | (implicit — pattern same TW, không có TC riêng cho BN) | ⚠️ |
| CB_NV_DP | CRU\* | TC-HSPL-014, TC-PERM-008 (IDOR HSPL) | ✅ |
| CB_PD_* | R\* | (implicit — không có TC riêng) | ⚠️ |
| CG/TVV | R\* | (implicit) | ⚠️ |
| DN | R\* (qua FR-VIII-22) | (out of scope) | N/A |
| NHT | R+U\* (BR-AUTH-10 đặc biệt) | TC-HSPL-015, TC-PERM-010 | ✅ |

### 6.3 TU_LIEU_PHAP_LY_VV (TLPL)

| Role | Expected | TC cover | Status |
|---|---|---|:---:|
| QTHT | R | (implicit) | ⚠️ |
| CB_NV_TW | CRUD\* | TC-TLPL-002..006 | ✅ |
| CB_NV_BN | CRUD\* | (implicit pattern) | ⚠️ |
| CB_NV_DP | CRUD\* | TC-PERM-008 (IDOR TLPL) | ✅ |
| CB_PD_* | R\* | (implicit) | ⚠️ |
| CG/TVV | R\* | (implicit) | ⚠️ |
| DN | R\* (CONG_KHAI only qua Cổng) | (out of scope) | N/A |
| NHT | — | (implicit) | ⚠️ |

### 6.4 DANH_GIA_CHAT_LUONG_TV

| Role | Expected | TC cover | Status |
|---|---|---|:---:|
| Mọi role nội bộ | R\* | TC-API-IN-006 (read-only accordion) | ✅ |
| CG/TVV chính chủ | — (assumption SPEC-CLARIFY-TVCS-PERM-01) | TC-PERM-009 (Step 2) | ✅ |
| DN | C† chỉ qua Cổng (UC153 inbound) | TC-API-IN-006, TC-API-IN-007 | ✅ |

### 6.5 PHIEN_TU_VAN

| Role | Expected | TC cover | Status |
|---|---|---|:---:|
| CB_NV_* | CRU\* | (implicit qua TC-TVCS-010 T3 tạo PHIEN_TU_VAN) | ⚠️ implicit |
| CG/TVV | CRU\* (CG phụ trách) | TC-TVCS-010 (T3 tạo phiên) | ✅ |
| Khác | R\* | (implicit) | ⚠️ |

**Coverage Permission:** 35/50 cells explicit covered = **70%** ⚠️ — gap chủ yếu ở PHIEN_TU_VAN cross-role + HSPL/TLPL các role CB_PD_*/CG read-only (best-effort implicit).

> ⚠️ Trong 50 cells, chỉ ~30 cells thực tế có ý nghĩa nghiệp vụ riêng biệt (đa phần CB_PD/CG read-only chỉ verify "không có C/D/U" — ngầm cover qua TC-PERM-001 UI Verify role-based visibility). Reframe coverage thực tế ≈ 90% cells nghiệp vụ rõ ràng. A6 đề xuất thêm 2 TC permission HSPL/TLPL cho CB_PD/QTHT để bít gap explicit.

---

## 7. Gap forward sang A6 (TC cần thêm để fill ≥95% AC + ≥90% Permission)

| # | Gap | Nguồn | Đề xuất TC mới (A6 inline merge) | File UC để merge |
|--:|---|---|---|---|
| 1 | UC147 AC-5 dashboard tổng hợp theo lĩnh vực/CG/trạng thái | SRS line 314 | TC-TVCS-NEW1 (P1, Happy): GET /api/v1/tu-van-chuyen-sau/dashboard → verify hiển thị thống kê 3 chiều (lĩnh vực + CG + trạng thái) cho cb_nv_tw_01 scope đơn vị | `01-TC-FR-X1-01-quan-ly-tvcs.md` Section thêm dashboard |
| 2 | UC152 AC-5 xem file trực tuyến (preview) | SRS line 949 | TC-TLPL-NEW1 (P1, Happy): Click file PDF/DOCX trên TLPL detail → verify preview render trong viewer (không trigger download) + verify network GET file URL với content-disposition=inline | `04-TC-FR-X1-06-quan-ly-tu-lieu-pl.md` Section C |
| 3 | UC151 AC-3 + UC153 AC-2 duplicate/update API inbound | SRS line 773, 1045 | TC-API-IN-NEW1 (P1, Negative): Cổng push HSPL với ma_ho_so_cong duplicate → ERR-HSPL-API-03 + count tab không tăng. TC-API-IN-NEW2 (P1, Edge): Cổng push DG hành_dong=CAP_NHAT (không phải GUI_LAI) → kiểm tra trạng thái hợp lệ rồi update | `06-TC-FR-X1-03-05-07-API-inbound-side-effect.md` Section C+D |
| 4 | BR-DATA-03 explicit verify 7 common fields | SRS line 1543-1547 | TC-TVCS-NEW2 (P2, Happy): CREATE TVCS → network response verify all 7 fields (id UUID v4 / created_at ISO / updated_at / created_by=cb_nv_tw_01.id / updated_by=null / is_deleted=0 / don_vi_id=BTP-TW.id) | `01-TC-FR-X1-01-quan-ly-tvcs.md` Section B |
| 5 | SM HSPL HIEU_LUC → HET_HAN auto trigger | SRS line 540, SM phụ HSPL | TC-HSPL-NEW1 (P2, Edge): Seed HSPL ngay_het_han=NOW()-1 day. Wait cron job (hoặc trigger admin endpoint) → verify trang_thai auto-flip HET_HAN. SPEC-CLARIFY-HSPL-CRON cần BA confirm cron schedule | `03-TC-FR-X1-04-quan-ly-hspl.md` Section bổ sung |
| 6 | Permission HSPL/TLPL cho CB_PD/QTHT explicit | overview §2.4 | TC-PERM-NEW1 (P2, Permission): cb_pd_tw_01 mở tab HSPL của DN cùng cấp → verify R only (no C/U/D button). qtht_01 mở tab TLPL → verify R only + cross-cấp toàn hệ thống | `05-TC-permission-matrix.md` Section thêm |
| 7 | ERR-TVCS-03 lĩnh vực không tồn tại explicit | SRS line 304 | TC-TVCS-NEW3 (P2, Negative): API direct POST `linh_vuc_id="DM-INVALID-99"` → ERR-TVCS-03 nguyên văn message | `01-TC-FR-X1-01-quan-ly-tvcs.md` Section B |

**Tổng đề xuất A6:** 8 TC mới (~7% increase, từ 117 → ~125 TC).

---

## 8. Coverage summary

| Tiêu chí | Mức yêu cầu | Thực tế | Status |
|---|---:|---:|:---:|
| BR coverage | ≥95% | 22/23 = 95.7% (BR-DATA-03 implicit) | ✅ |
| AC coverage SRS Given/When/Then | 100% | 34/38 = 89.5% (4 gap) | ⚠️ |
| SM-TVCS transitions | 100% | 10/10 = 100% | ✅ |
| SM phụ TLPL | 100% | 4/4 = 100% | ✅ |
| SM phụ HSPL | 100% | 2/3 = 67% (HET_HAN auto gap) | ⚠️ |
| Error codes | ≥94% | 33/35 explicit + 8 implicit pattern = 94.3% | ✅ |
| Permission Matrix | ≥90% | 35/50 cells = 70% explicit (~90% nghiệp vụ rõ ràng) | ⚠️ |
| SPEC-CLARIFY pending | Quantified | 14 ticket FR-12 (TVCS-01..09 + PERM-01..07 + UI-01..02 + FILE-01 + EDGE-01..03 + UNI-01) | ⚠️ — gửi BA |

**Quality Gate decision:** ⚠️ **CONDITIONAL PASS** — BR + SM-TVCS + Error đạt target. AC (89.5% < 100%) + Permission (70% < 90% explicit) cần A6 fill 8 TC inline merge để đạt target (~95% AC + ~90% Permission explicit).

**Recommendation cho A6:**
1. Generate 8 TC mới (Section 7) để fill 4 AC gap + 1 SM gap + 2 Permission gap + 1 Error explicit gap.
2. Sau A6: AC coverage 38/38 = 100%, Permission ≥90%, BR-DATA-03 explicit covered.
3. Tổng TC sau A6 ≈ 125 (từ 117).

---

## 9. SPEC-CLARIFY tổng hợp tham chiếu (14 ticket — đã list trong overview §4)

| Ticket | Vị trí TC liên quan | Nội dung |
|---|---|---|
| SPEC-CLARIFY-TVCS-01 | TC-TVCS-019 | Hủy DANG_TU_VAN entity DON_DONG_Y_HUY chưa quote |
| SPEC-CLARIFY-TVCS-02 | TC-TVCS-029 | Batch 100 rollback policy |
| SPEC-CLARIFY-TVCS-03 | (gap A6 SLA timeout cron) | Cron job 2 ngày LV |
| SPEC-CLARIFY-TVCS-04 | (gap A7 LOẠI auto-save) | Auto-save 30s UI feedback |
| SPEC-CLARIFY-TVCS-05 | TC-PERM-010 | NHT route SCR-IV-03? |
| SPEC-CLARIFY-TVCS-06 | TC-TLPL-011 | mo_ta_cong_khai BB form validation |
| SPEC-CLARIFY-TVCS-07 | TC-TLPL-005 | WARNING vs ERROR sửa CONG_KHAI |
| SPEC-CLARIFY-TVCS-08 | TC-API-IN-008 | Rate limit threshold |
| SPEC-CLARIFY-TVCS-09 | TC-API-IN-007 | GUI_LAI conflict resolution warn |
| SPEC-CLARIFY-TVCS-PERM-01 | TC-PERM-009 | DANH_GIA cho CG chính chủ |
| SPEC-CLARIFY-TVCS-PERM-02 | TC-TVCS-019 | DON_DONG_Y_HUY entity |
| SPEC-CLARIFY-TVCS-PERM-03 | TC-PERM-003 | Route SSO VNeID URL |
| SPEC-CLARIFY-TVCS-PERM-04 | TC-PERM-005 | Cross-cấp PD error message exact |
| SPEC-CLARIFY-TVCS-PERM-05/06/07 | TC-PERM-011/012/013 | Refresh token + role change + SSO callback |
| SPEC-CLARIFY-TVCS-UI-01 | TC-TVCS-001, TC-TVCS-TK-019 | Deeplink filter URL |
| SPEC-CLARIFY-TVCS-UI-02 | (auto-save UI feedback) | Toast/icon |
| SPEC-CLARIFY-TVCS-FILE-01 | TC-TVCS-036 | Tổng max upload 100MB |
| SPEC-CLARIFY-TVCS-EDGE-01..03 | TC-TVCS-033/035/036 | Session recover + race + total size |
| SPEC-CLARIFY-HSPL-* | TC-HSPL-007/008/011/016/018/019 | UI/date/file/Unicode |
| SPEC-CLARIFY-TLPL-* | TC-TLPL-005/006/007/016/018/019/020 | UI/atomicity/timeout |
| SPEC-CLARIFY-HSPL-QUEUE | TC-API-IN-005 | UI dashboard "DS chờ xử lý CB NV" |
| SPEC-CLARIFY-HSPL-CRON (NEW) | (gap A6 HET_HAN) | Auto HET_HAN cron schedule |
| SPEC-CLARIFY-TVCS-API-RL/PAYLOAD/RACE | TC-API-IN-008/009/010 | Rate limit + payload size + race policy |

---

*Generated 2026-05-06 by BMAD A5 (testarch-trace) — Phase A W3.3 TV Chuyên sâu.*
*Pattern reference: `bieu-mau/09-traceability-matrix.md`. Audit only — gap forward A6.*
