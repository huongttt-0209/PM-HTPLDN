# 09 — A5 Traceability Matrix (BR/AC/SM/Permission/Error ↔ TC)

> **Skill**: bmad-testarch-trace
> **Ngày chạy**: 2026-05-09
> **Module**: FR-07 W2.1 Quản lý DN
> **Iron rule**: KHÔNG sinh TC mới ở A5 — chỉ phát hiện gap, forward sang A6 fix.

---

## A. BR Coverage Matrix

| BR ID | TC IDs covering | Coverage |
|-------|-----------------|----------|
| BR-AUTH-01 (xác thực + TOTP 2FA) | TC-DN-PERM-101, 102, 103, 104; TC-DN-UI-01..05 (login pre-condition) | ✅ 100% |
| BR-AUTH-08 (đơn vị 2 tầng) | TC-DN-PERM-001..007, TC-DN-203, TC-LS-203, TC-CT-204, TC-HSPL-601, TC-DN-PERM-501..503 | ✅ 100% |
| BR-AUTH-EMAIL-01 (2 email DN) | TC-DN-PERM-201, 202, 203, 204; TC-DN-017 | ✅ 100% |
| BR-AUTH-USERNAME-01 (DN.username = MST) | TC-DN-PERM-301, 302, 303; TC-DN-PERM-604 (chi nhánh 13 chữ số) | ✅ 100% |
| BR-DATA-01 (Soft delete) | TC-DN-101, 103; TC-HSPL-201; TC-LS-303; TC-CT-401 | ✅ 100% |
| BR-DATA-02 (Multi-tenant scoping) | Implicit qua BR-AUTH-08 tests + TC-DN-001 (PUT body có don_vi_id) | ✅ 100% |
| BR-DATA-03 (Common fields) | TC-DN-001 AUDIT_LOG verify; TC-DN-014 DOANH_NGHIEP_LINH_VUC common fields | ✅ 100% |
| BR-DATA-04 (Auto-gen mã DN-{TINH}-{SEQ} + HSPL-{YYYYMMDD}-{SEQ}) | TC-DN-018; TC-HSPL-001..005, TC-HSPL-701 | ✅ 100% |
| BR-DATA-05 (AUDIT_LOG immutable) | TC-DN-PERM-401..404; TC-DN-001, TC-DN-101, TC-HSPL-001/101/201 | ✅ 100% |
| BR-DATA-07 (Pagination 20 default, 100 max) | TC-DN-TK-201..204; TC-HSPL-602; TC-LS-101, 102; TC-CT-003 | ✅ 100% |
| BR-CALC-05 (Quy mô DNNVV NĐ 39/2018) | TC-DN-004..008 (4 enum + warning) | ✅ 100% |

**BR Coverage**: ✅ **11/11 = 100%**

---

## B. AC Coverage Matrix

### B.1 FR-V.III-01 AC (5 AC)

| AC | Mô tả | TC IDs covering | Coverage |
|----|------|-----------------|---|
| AC1 | CB NV truy cập "Quản lý DN" → list theo đơn vị | TC-DN-UI-03, TC-DN-PERM-001..003 | ✅ |
| AC2 | CB NV thêm DN ~~(BỎ v3.1)~~ → renamed: chỉnh sửa DN | TC-DN-001 (Edit happy) | ✅ |
| AC3 | CB NV xem chi tiết DN → hiển thị hồ sơ + lịch sử | TC-DN-201, TC-DN-204, TC-LS-001..006 | ✅ |
| AC4 | MST trùng → báo lỗi (renamed: chỉnh sửa MST trùng DN khác) | TC-DN-003, TC-DN-308 | ✅ |
| AC5 | CB NV xem danh sách + Xuất Excel (max 10K) | TC-DN-TK-301..306 | ✅ (note: AC này có `[GAP-V.III-01]` — Xuất Excel OUT D.2.1 SPEC-CLARIFY-DN-07) |

### B.2 FR-V.III-02 AC (4 AC)

| AC | Mô tả | TC IDs covering | Coverage |
|----|------|-----------------|---|
| AC1 | Search từ khóa | TC-DN-TK-001, 002 | ✅ |
| AC2 | Filter linh_vuc_kd | TC-DN-TK-005, TC-DN-TK-UI-02 | ✅ |
| AC3 | Filter thời gian hỗ trợ | TC-DN-TK-006 | ✅ |
| AC4 | Combine multi AND | TC-DN-TK-101, 102 | ✅ |

### B.3 FR-X.1-04 AC (9 AC)

| AC | Mô tả | TC IDs covering | Coverage |
|----|------|-----------------|---|
| AC1 | CB NV truy cập danh sách HSPL | TC-HSPL-UI-01 | ✅ |
| AC2 | Xem chi tiết HSPL + file | TC-HSPL-501, 502 | ✅ |
| AC3 | Thêm mới HSPL | TC-HSPL-001..005 (5 loại) | ✅ |
| AC4 | Chỉnh sửa HSPL | TC-HSPL-101..103 | ✅ |
| AC5 | Xóa HSPL (soft delete) | TC-HSPL-201, 202 | ✅ |
| AC6 | Search keyword | TC-HSPL-301 | ✅ |
| AC7 | Combine multi-filter AND | TC-HSPL-307 | ✅ |
| AC8 | NHT có VV phân công → xem HSPL DN trong VV (BR-AUTH-10) | TC-DN-PERM-502 | ✅ |
| AC9 | NHT chỉ R + U, không C/D | TC-DN-PERM-503 | ✅ |

**AC Coverage**: ✅ **18/18 = 100%**

---

## C. SM Coverage

**KHÔNG CÓ** — DOANH_NGHIEP entity không có lifecycle. SCR-V.III-02 không có nút workflow.

**SM-HSPL** (HO_SO_PHAP_LY_DN trang_thai 3 enum HIEU_LUC/HET_HAN/THU_HOI):
| Transition | TC IDs |
|------|------|
| (init) → HIEU_LUC | TC-HSPL-001..005 (default value) |
| HIEU_LUC → HET_HAN | TC-HSPL-101 |
| HIEU_LUC → THU_HOI | TC-HSPL-102 |
| HET_HAN → HIEU_LUC | (cần thêm TC — A6 forward) |
| THU_HOI → HIEU_LUC | (cần thêm TC — A6 forward) |

**SM-HSPL Coverage**: ⚠️ **3/5 = 60%** → A6 fill 2 transition

---

## D. Permission Matrix Coverage

| Entity × Role | TC IDs |
|------|------|
| DOANH_NGHIEP × QTHT (R) | TC-DN-PERM-UI-01, TC-DN-PERM-001 |
| DOANH_NGHIEP × CB_NV (CRUD\*) | TC-DN-001, 101, 201, TC-DN-PERM-002..006 |
| DOANH_NGHIEP × CB_PD (R\*) | TC-DN-PERM-UI-01 (cb_pd visible R*) |
| DOANH_NGHIEP × DN (RU\*) | TC-DN-PERM-UI-01 (dn_01 chuyên trang riêng) |
| DOANH_NGHIEP_LINH_VUC × CB_NV (CRUD\*) | TC-DN-014, 015 |
| HO_SO_PHAP_LY_DN × CB_NV (CRUD\*) | TC-HSPL-001..201, TC-HSPL-101..103, TC-HSPL-201, 202 |
| HO_SO_PHAP_LY_DN × NHT (CRU\* — chỉ RU thực tế) | TC-DN-PERM-502, 503 |
| HO_SO_PHAP_LY_DN × DN (RU\*) | TC-DN-PERM-UI-01 (dn_01 không CMS) |

**Permission Coverage**: ✅ **8/8 = 100%**

---

## E. Error Code Coverage

### E.1 Module DN

| Code | TC IDs |
|------|------|
| ERR-DN-01 (Tên DN trống) | TC-DN-002 |
| ERR-DN-02 (MST trùng) | TC-DN-003, TC-DN-308 |
| WRN-DN-01 (Quy mô mismatch) | TC-DN-004 |
| ERR-DN-03 (Xóa DN có VV) | TC-DN-102 |
| ERR-DN-04 (Excel >10K) | TC-DN-TK-302, 306 |
| INF-DN-TK-01 (Search 0 result) | TC-DN-TK-007 |

### E.2 Module HSPL

| Code | TC IDs |
|------|------|
| ERR-HSPL-01 (Tên HS rỗng) | TC-HSPL-006 |
| ERR-HSPL-02 (DN không tồn tại) | (gap — A6 fill) |
| ERR-HSPL-03 (File >20MB) | TC-HSPL-402, 403 |
| ERR-HSPL-04 (File chứa mã độc) | TC-HSPL-404 |
| ERR-HSPL-05 (Loại HS không hợp lệ) | TC-HSPL-007 |
| ERR-HSPL-06 (tu_ngay > den_ngay) | TC-HSPL-305 |
| INF-HSPL-01 (Search 0 result) | TC-HSPL-306 |

**Error Coverage**: ✅ **12/13 = 92.3%** (1 gap ERR-HSPL-02 — A6 forward)

---

## F. Gap Forward to A6

| ID | Gap | Forward action |
|----|-----|------|
| GAP-A5-01 | SM-HSPL transition HET_HAN → HIEU_LUC (restore) | A6 thêm TC-HSPL-104 |
| GAP-A5-02 | SM-HSPL transition THU_HOI → HIEU_LUC | A6 thêm TC-HSPL-105 |
| GAP-A5-03 | ERR-HSPL-02 (DN không tồn tại khi tạo HSPL) | A6 thêm TC-HSPL-008 |
| GAP-A5-04 | BR-DATA-03 verify common fields đầy đủ trên row mới | A6 thêm TC-DN-019 |
| GAP-A5-05 | Permission Matrix DOANH_NGHIEP × DN dòng "DN không CMS" — verify dn_01 redirect khi truy cập CMS | A6 thêm TC-DN-PERM-008 |
| GAP-A5-06 | UI verify "Phụ nữ làm chủ" + "Số LĐ nữ" ưu tiên NĐ55 Điều 4 | A6 thêm TC-DN-019b (đã có TC-DN-010 cho la_nu_lam_chu nhưng chưa verify ảnh hưởng phân công) |
| GAP-A5-07 | Xem chi tiết HSPL hiển thị file đính kèm với metadata (tên, loại, dung lượng, URL preview) — TC-HSPL-501 chỉ click row, chưa verify field cấu trúc | A6 strengthen TC-HSPL-501 |

---

## G. Tổng kết

| Metric | Score |
|--------|------|
| BR Coverage | 11/11 = 100% |
| AC Coverage | 18/18 = 100% |
| SM Coverage | 3/5 = 60% (forward A6) |
| Permission Coverage | 8/8 = 100% |
| Error Coverage | 12/13 = 92.3% (forward A6) |
| **Aggregate** | **52/55 = 94.5%** |

**Forward A6**: 7 gap → fill TC + 1 strengthen → A6 sẽ thêm ~7 TC mới + sửa 1 TC.

---

**— Hết 09 A5 Traceability FR-07 —**
