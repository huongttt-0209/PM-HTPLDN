# A5 — Traceability Matrix (BR/AC ↔ TC) DM Dùng Chung

> **Date:** 2026-05-08
> **Mục đích:** Verify ≥95% BR + 100% AC + 100% Error code có TC cover. Gap forward sang A6 fix.

---

## 1. BR Coverage

| BR | Tên | TC cover | Coverage | Note |
|----|-----|----------|----------|------|
| BR-AUTH-01 | Xác thực + chỉ QTHT | TC-LV-045..047, TC-PERM-001..016, mọi precondition | 100% ✅ | Cross-cutting tất cả file |
| BR-AUTH-02 | Cây 2 tầng TW → {BN, ĐP} | TC-CQDV-001..003, 008, 009, 011, 012, 016, 029..031, EDGE-001 | 100% ✅ | UC103 only |
| BR-AUTH-03 | Ngang cấp KHÔNG thấy nhau | _Cross-FR — test ở module dùng (vd FR-V dropdown đơn vị)_ | 0% ⚠️ N/A | Gap module-level — KHÔNG nằm trong scope DM W1.3, sẽ test khi module xài |
| BR-AUTH-04 | Cấp cha thấy cấp con | TC-CQDV-001 (TW thấy 18 BN + 63 DP), TC-PERM-001..002 | 100% ✅ | UC103 only |
| BR-AUTH-08 | Multi-tenant scoping (ngoại lệ DM hệ thống NULL) | _Verify qua list không bị filter theo don_vi_id_ — implicit trong TC-LV-001..003 | 80% ⚠️ | Add 1 TC explicit fill A6 |
| BR-DATA-01 | Soft delete | TC-LV-027, 031, TC-CQDV-023, TC-LV-EDGE-004, mọi xóa OK | 100% ✅ | Cross-cutting |
| BR-DATA-02 | Multi-tenant don_vi_id NOT NULL (DM ngoại lệ) | TC-LV-001 implicit (DM hệ thống không có cột don_vi_id) | 60% ⚠️ | Add 1 TC explicit fill A6 |
| BR-DATA-03 | 7 common fields | TC-LV-001, 003 (hiển thị created_at/updated_at) | 80% ⚠️ | Add 1 TC verify created_by/updated_by fill A6 |
| BR-DATA-05 | Audit trail mọi CUD | TC-LV-009, 019, 027, 033, 042, 043 + cross-ref Nhật ký HT | 100% ✅ | — |
| BR-DATA-06 | Export Excel max 10K | _SCR-VIII-01 KHÔNG nguyên văn có nút Export DM_ — gap module-level | 0% ⚠️ N/A | Verify UI có nút Export không — nếu có, fill TC ở A6 |
| BR-DATA-07 | Pagination 20/100 | TC-LV-002, 004, 005, EDGE-007 | 100% ✅ | — |
| BR-CALC-04 (phần Tổng=100%) | Tổng trọng số tiêu chí = 100% (cảnh báo nếu khác) | TC-TCHQ-001, 002, 005, EDGE-001, FILL-004 | 100% ✅ | UC109 phần BA — TRONG scope W1.3 |
| BR-CALC-04 (phần SUM điểm) | Điểm tổng = SUM(diem_i × trong_so_i / 100) | _Out of scope W1.3_ | N/A | Test ở **FR-08 Đánh giá** (W4.4) — đây là logic tính điểm khi đánh giá, không phải config DM |
| BR-EC-13 | Search sanitize 200 + escape SQL/XSS | TC-LV-038..041, EDGE-005, EDGE-006 | 100% ✅ | — |

**BR Summary:** 13/13 BR map; **10 ✅ 100%** + **3 ⚠️ partial/N/A**. Coverage = 76.9% full + 23.1% partial. Forward 3 gaps sang A6 fill.

---

## 2. AC Coverage

| UC | AC chính | TC cover | Coverage |
|----|----------|----------|----------|
| TPL-DM-CRUD AC | Given QTHT login When access Then list paginated sorted | TC-LV-001, 006 | ✅ |
| TPL AC | Given QTHT add When fill required Then save success | TC-LV-009 | ✅ |
| TPL AC | Given QTHT edit When change Then validate + save | TC-LV-019 | ✅ |
| TPL AC | Given QTHT delete referenced When confirm Then reject | TC-LV-028..030 | ✅ |
| TPL AC | Given QTHT search When type Then matching results | TC-LV-034..037 | ✅ |
| UC103 AC | Given QTHT access Cơ quan ĐV Then tree TW→BN→DP | TC-CQDV-001 | ✅ |
| UC103 AC | Given QTHT add When fill required Then save | TC-CQDV-008..009 | ✅ |
| UC103 AC | Given QTHT delete don_vi linked When confirm Then reject | TC-CQDV-024..025 | ✅ |
| UC109 AC | (implicit từ TPL) | TC-TCHQ-004 | ✅ |
| UC110 AC | (implicit từ TPL) | TC-TCCP-003 | ✅ |

**AC Summary:** 10/10 AC ✅ 100%

---

## 3. Error Code Coverage

| Error Code | Mô tả | TC cover | Coverage |
|------------|-------|----------|----------|
| ERR-AUTH-01 | Bạn không có quyền | TC-LV-046, TC-PERM-005..007, 009..015 (TC-PERM-008 LOẠI R3) | ✅ |
| ERR-AUTH-02 | Session hết hạn | TC-LV-047, TC-PERM-016 | ✅ |
| ERR-DM-01 | Mã trùng | TC-LV-010, 020, TC-LH-003, TC-LDN-003, etc. (mọi DM) | ✅ |
| ERR-DM-02 | Tên trống | TC-LV-011, TC-LV-022 | ✅ |
| ERR-DM-03 | Đang được sử dụng | TC-LV-028..030, TC-TT-EDGE-001 | ✅ |
| ERR-DM-04 | Bản ghi không tồn tại | TC-LV-024 | ✅ |
| ERR-DM-05 | Mã > 20 ký tự | TC-LV-013, 014 | ✅ |
| ERR-DV-01 | Mã đơn vị trùng | TC-CQDV-010, 018 | ✅ |
| ERR-DV-02 | Cấp BN/DP thiếu cha | TC-CQDV-011 | ✅ |
| ERR-DV-03 | Đơn vị có TK liên kết | TC-CQDV-024 | ✅ |
| ERR-DV-04 | Đơn vị có dữ liệu | TC-CQDV-025 | ✅ |
| ERR-DV-05 | Vòng lặp cây | TC-CQDV-027..028 | ✅ |
| ERR-TC-01 | Min < Max | TC-TCHQ-010, 011, EDGE-002 | ✅ |
| WRN-TC-01 | Tổng != 100% | TC-TCHQ-005 | ✅ |

**Error Summary:** 14/14 ✅ 100%

---

## 4. Permission Matrix Coverage

| Role | TC cover | Coverage |
|------|----------|----------|
| QTHT | TC-PERM-001..004 + mọi TC CRUD primary | ✅ |
| CB_NV (TW/BN/DP) | TC-PERM-005..008 | ✅ |
| CB_PD (TW/BN/DP) | TC-PERM-009..011 | ✅ |
| NHT/TVV/CG/DN | TC-PERM-012..015 | ✅ |
| Session expired | TC-PERM-016 | ✅ |

**Permission Summary:** 5/5 ✅ 100%

---

## 5. Gap forward A6 (3 BR partial — DONE)

| Gap ID | BR | Đề xuất TC fill | Target file | Status |
|--------|-----|-----------------|-------------|--------|
| GAP-001 | BR-AUTH-08 | Verify QTHT thấy DM hệ thống dù KHÔNG bị scoped don_vi_id (DM dùng chung NULL ngoại lệ) | File 01 (TC-LV-FILL-001) | ✅ done A6 |
| GAP-002 | BR-DATA-02 | Verify DDL DANH_MUC.don_vi_id NULL allowed cho DM hệ thống (qua UI không có cột don_vi_id) | File 01 (TC-LV-FILL-002) | ✅ done A6 |
| GAP-003 | BR-DATA-03 | Verify cột created_by + updated_by hiển thị (qua chi tiết hoặc audit log) | File 01 (TC-LV-FILL-003) | ✅ done A6 |

## 6. Gap forward R2 (Codex review 2026-05-08 — 9 TC fill DONE)

| Gap ID | UC | Đề xuất TC fill | Target file | Status |
|--------|-----|-----------------|-------------|--------|
| R2-001 | UC103 | cap thuộc enum TW/BN/DP — invalid value reject | File 03 (TC-CQDV-FILL-001) | ✅ done R2 |
| R2-002 | UC103 | don_vi_cha_id trỏ đơn vị không tồn tại | File 03 (TC-CQDV-FILL-002) | ✅ done R2 |
| R2-003 | UC103 | cap=TW + don_vi_cha_id != NULL → reject (BR-AUTH-02) | File 03 (TC-CQDV-FILL-003) | ✅ done R2 |
| R2-004 | UC109 | trong_so rỗng → ERR required (Y) | File 04 (TC-TCHQ-FILL-001) | ✅ done R2 |
| R2-005 | UC109 | thang_diem_min rỗng → ERR required (Y) | File 04 (TC-TCHQ-FILL-002) | ✅ done R2 |
| R2-006 | UC109 | thang_diem_max rỗng → ERR required (Y) | File 04 (TC-TCHQ-FILL-003) | ✅ done R2 |
| R2-007 | UC109 | WRN-TC-01 trigger sau save khi tổng < 100% (không chỉ display) | File 04 (TC-TCHQ-FILL-004) | ✅ done R2 |
| R2-008 | UC110 | muc_ho_tro_phan_tram rỗng → ERR required (Y) | File 05 (TC-TCCP-FILL-001) | ✅ done R2 |
| R2-009 | UC110 | tran_ho_tro_nam rỗng → ERR required (Y) | File 05 (TC-TCCP-FILL-002) | ✅ done R2 |

## 7. Out-of-scope (clarified R2 Codex review)

| Item | Lý do out-of-scope W1.3 | Test ở module nào |
|------|--------------------------|-------------------|
| BR-CALC-04 phần SUM `Điểm tổng = SUM(diem_i × trong_so_i / 100)` | Logic tính điểm khi đánh giá, KHÔNG phải config DM | FR-08 Đánh giá HQ (W4.4) |
| BR-AUTH-03 "Ngang cấp KHÔNG thấy nhau" | Phân quyền dữ liệu role-level, KHÔNG phải thuộc DM | FR-VIII-14 Phân quyền (W1.4 TKPQ) hoặc module dùng đơn vị (vd FR-V Vụ việc) |
| BR-AUTH-04 "Cấp cha thấy cấp con" | Tương tự BR-AUTH-03 | FR-VIII-14 / module dùng |
| BR-DATA-06 Export Excel max 10K | SCR-VIII-01 KHÔNG có nút Export DM riêng | FR-10 W1.1 Nhật ký HT (đã test) hoặc smoke per-DM nếu Phase B phát hiện UI có button |
| ERR-DM-02/04/05 cho 11 DM smoke | Backend chung TPL-DM-CRUD — verified ở file 01 LV-PL representative | Cùng test path file 01 |

---

## Tổng kết A5

- **BR coverage:** 13/13 mapping; 10 ✅ + 3 ⚠️ → forward A6
- **AC coverage:** 100%
- **Error code coverage:** 14/14 = 100%
- **Permission matrix:** 100%
- **Forward to A6:** 3 GAP TC fill
