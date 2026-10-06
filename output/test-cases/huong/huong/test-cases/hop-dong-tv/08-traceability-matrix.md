# A5 — Traceability Matrix (FR-14 Hợp đồng Tư vấn)

> **Ngày:** 2026-05-10
> **Tool:** bmad-testarch-trace
> **Source:** SRS srs-fr-14-hop-dong-tv-v3.1.md + business-flow + 02-thu-tu-module §⑩

---

## 1. BR ↔ TC Matrix

| BR | Mô tả | SRS Ref | TC covered | Coverage |
|----|-------|---------|------------|----------|
| BR-AUTH-01 | Xác thực 2-tier | srs-fr-14:464,471-478 | TC-PERM-001..015, mọi TC (precondition login) | ✅ 100% |
| BR-AUTH-08 | Phân quyền dữ liệu theo `don_vi_id` | srs-fr-14:465,480-487 | TC-LVV-011, TC-HDTK-020, TC-PERM-015, TC-PERM-021, TC-HDTV-028 | ✅ 100% |
| BR-DATA-01 | Soft delete | srs-fr-14:466,489-496 | TC-HDTV-003, TC-LVV-022 | ✅ 100% |
| BR-DATA-04 | Sinh mã `HDTV-YYYYMMDD-SEQ` | srs-fr-14:467,498-504 | TC-HDTV-001, TC-HDTV-022, TC-HDTV-027 | ✅ 100% |
| BR-DATA-05 | Audit trail immutable | srs-fr-14:468,506-512 | TC-HDTV-001, 002, 003, TC-MTD-001..003, TC-TTGD-001, TC-LVV-001, 003, TC-LVV-021 | ✅ 100% |
| BR-DATA-07 | Pagination 20/page | srs-fr-14:469,514-520 | TC-HDTV-004, TC-HDTK-022, TC-HDTK-026 | ✅ 100% |

**BR coverage:** 6/6 = **100%**

---

## 2. Acceptance Criteria ↔ TC Matrix

### FR-X.3-01 (UC159)

| AC | Mô tả AC | Vị trí | TC covered | Coverage |
|----|----------|--------|------------|----------|
| AC1 | Hiển thị DS HĐ + phân trang | srs-fr-14:174 | TC-HDTV-004 | ✅ |
| AC2 | Thêm mới — nhập đủ trường + validate + lưu | srs-fr-14:175 | TC-HDTV-001, 010..013 | ✅ |
| AC3 | Thêm mốc tiến độ + ngày dự kiến | srs-fr-14:176 | TC-MTD-001 | ✅ |
| AC4 | Xóa HĐ không có VV — soft delete | srs-fr-14:177 | TC-HDTV-003 | ✅ |
| AC5 | Xóa HĐ có VV — từ chối + thông báo | srs-fr-14:178 | TC-HDTV-014, TC-LVV-010 | ✅ |
| AC6 | Xuất Excel theo filter | srs-fr-14:179 + GAP-X.3-02 | TC-HDTV-006, TC-HDTV-028 | ✅ |
| AC7 | Tạo HĐ với loại Bên B='CG' lưu tu_van_vien_id trỏ CG | srs-fr-14:180 | TC-HDTV-025 | ✅ |

**AC FR-X.3-01:** 7/7 = **100%**

### FR-X.3-02 (UC159e)

| AC | Mô tả AC | Vị trí | TC covered | Coverage |
|----|----------|--------|------------|----------|
| AC1 | Tìm theo từ khóa → DS matching, phân trang | srs-fr-14:245 | TC-HDTK-001, TC-HDTK-022, 023 | ✅ |
| AC2 | Lọc theo TVV → kết quả TVV đó | srs-fr-14:246 (GAP-X.3-03) | TC-HDTK-002 | ⚠️ GAP-X.3-03 |
| AC3 | Lọc khoảng ngày → kết quả theo thời gian | srs-fr-14:247 (GAP-X.3-03) | TC-HDTK-003 | ⚠️ GAP-X.3-03 |
| AC4 | Không có kết quả → thông báo "Không tìm thấy" | srs-fr-14:248 (GAP-X.3-03) | TC-HDTK-011 | ⚠️ GAP-X.3-03 |

**AC FR-X.3-02:** 4/4 = **100%** (3 marked GAP-X.3-03 nguyên SRS, đã có TC verify)

**AC tổng:** 11/11 = **100%**

---

## 3. Error Code ↔ TC Matrix

| ERR Code | Mô tả | TC covered | Coverage |
|----------|-------|------------|----------|
| ERR-HDTV-01 | Tên HĐ trống | TC-HDTV-010 | ✅ |
| ERR-HDTV-02 | Ngày BD > KT | TC-HDTV-011 | ✅ |
| ERR-HDTV-03 | Σ thanh toán > giá trị | TC-TTGD-010, TC-TTGD-022 | ✅ |
| ERR-HDTV-04 | Xóa HĐ có VV | TC-HDTV-014, TC-LVV-010 | ✅ |
| ERR-HDTV-05 | Giá trị HĐ ≤ 0 | TC-HDTV-012, TC-HDTV-013 | ✅ |
| ERR-HDTV-TK-01 | tu_ngay > den_ngay | TC-HDTK-010 | ✅ |
| INF-HDTV-TK-01 | Không có kết quả | TC-HDTK-011 | ✅ |

**Error coverage:** 7/7 = **100%**

---

## 4. Trạng thái HĐ (status field — KHÔNG phải SM, per SRS §5 line 450-452)

> **Codex P0-1 RESOLVED:** SRS §5 nguyên văn "Nhóm X.3 không có state machine, HĐ TV chỉ CRUD thuần. Trạng thái chỉ là status field đơn giản." → Bỏ axis "SM transition" khỏi gate Phase A. Thay bằng axis "trang_thai field enum coverage" (4 enum value: DANG_THUC_HIEN/TAM_DUNG/HOAN_THANH/HUY).

| Enum value của `trang_thai` | TC covered | Coverage |
|------------------------------|------------|----------|
| DANG_THUC_HIEN (default tạo) | TC-HDTV-001 | ✅ |
| TAM_DUNG (free-edit) | TC-HDTV-030, 031 | ✅ |
| HOAN_THANH (free-edit) | TC-HDTV-032 | ✅ |
| HUY (free-edit) | TC-HDTV-033 | ✅ |

**trang_thai field coverage:** 4/4 = **100%**

---

## 5. Permission Matrix ↔ TC (sau Codex P1-2 + P1-3)

| Cell | TC covered | Coverage |
|------|------------|----------|
| QTHT — Read OBS | TC-PERM-003 | ✅ (OBS HDTV-16) |
| CB_NV TW CRUD | TC-PERM-001, TC-HDTV-023 (DP) | ✅ |
| CB_NV BN CRUD scoped | TC-PERM-023 (Codex) | ✅ |
| CB_NV DP CRUD scoped | TC-HDTV-023, TC-PERM-021 | ✅ |
| CB_PD TW Read | TC-PERM-002, TC-PERM-014 | ✅ |
| CB_PD BN Read scoped | TC-PERM-024 (Codex) | ✅ |
| CB_PD DP Read scoped | TC-PERM-025 (Codex) | ✅ |
| CB_PD Excel block | TC-PERM-026 (Codex) | ✅ |
| NHT block | TC-PERM-010 | ✅ |
| TVV block | TC-PERM-011 | ✅ |
| CG block | TC-PERM-012 | ✅ |
| DN block | TC-PERM-013 | ✅ |
| GV block | TC-PERM-020 | ✅ |
| Cross-tenant DP-DP | TC-PERM-021 | ✅ |
| Cross-tenant TW-DP | TC-PERM-015 | ✅ |
| Embedded drawer NHT | TC-PERM-022 | ✅ |

**Permission coverage:** 16/16 = **100%** (sau Codex P1-2 + P1-3)

---

## 6. Entity field ↔ TC (Inputs FR-X.3-01 — sau A6 + Codex)

| Field | TC covered | Coverage |
|-------|------------|----------|
| ma_hop_dong (auto) | TC-HDTV-001, 027 | ✅ |
| ten_hop_dong | TC-HDTV-001, 010 | ✅ |
| ben_a (auto) | TC-HDTV-001, 023 | ✅ |
| ben_b | TC-HDTV-001 | ✅ |
| tvv_id | TC-HDTV-024, 025 | ✅ |
| gia_tri_hop_dong | TC-HDTV-001, 012, 013, TC-TTGD-022 | ✅ |
| thoi_han_bat_dau / ket_thuc | TC-HDTV-001, 011, 020, 021 | ✅ |
| noi_dung | TC-HDTV-002 | ✅ |
| vu_viec_ids | TC-LVV-001..003, 010..011, 022..025 | ✅ |
| ghi_chu | TC-HDTV-034 (A6 fill) | ✅ |
| file_dinh_kem | TC-HDTV-026 | ⚠️ SPEC-CLARIFY-HDTV-05 (SRS silent) |
| **Entity-level fields KHÔNG có UI** (Codex P1-4 OBS) | | |
| so_hop_dong | — | ⏳ OBS HDTV-17 (form không có) |
| ngay_ky | — | ⏳ OBS HDTV-17 (form không có) |

**Entity Inputs field:** 11/11 = **100%** (file_dinh_kem có TC nhưng SPEC-CLARIFY)
**Entity DB-only fields (so_hop_dong, ngay_ky):** OBS Excluded — không có UI input.

---

## 7. Tổng quan coverage (sau A6 + Codex)

| Axis | Coverage | Status |
|------|----------|--------|
| BR formal | 6/6 = 100% | ✅ |
| AC SRS | 11/11 = 100% | ✅ |
| ERR Code | 7/7 = 100% | ✅ |
| trang_thai enum (status field) | 4/4 = 100% | ✅ |
| Permission Matrix | 16/16 = 100% | ✅ |
| Entity Inputs field (form UI) | 11/11 = 100% | ✅ |

**Threshold:** ≥95% mọi axis. **Trace status:** ✅ ALL axis ≥95%.

---

*A5 done 2026-05-10 + A6 fill (5 TC) + Codex P0-1 P1-2 P1-3 P1-4 patches applied.*
