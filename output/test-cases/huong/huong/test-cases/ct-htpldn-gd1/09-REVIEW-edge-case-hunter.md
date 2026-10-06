# A4 — Edge Case Hunter Audit Log — CT HTPLDN GĐ1

> **Ngày**: 2026-05-06 · **Tool**: bmad-review-edge-case-hunter
> **Method**: Walk every branching path + boundary condition của 6 FR GĐ1 (FR-XI-01..FR-XI-05a) + cross-cutting BR.
> **Output**: Edge case proposed → merge inline vào file UC tương ứng (KHÔNG sống ở file này).

---

## Quy ước

- **PROPOSED**: Đề xuất TC mới
- **MERGED**: Đã Edit inline vào file UC nguồn
- **REJECTED**: Loại do trùng / spec gap quá xa / A7 filter sẽ xử lý

---

## Walk-through theo file

### File 01 — CRUD CT core

| TC ID đề xuất | Tiêu đề | Trace | Status | Merged vào |
|---------------|---------|-------|--------|-----------|
| TC-CT-CRUD-015 | thoi_gian_bat_dau = thoi_gian_ket_thuc (boundary equal — strict `>`) | FR-XI-01 / Inputs#5 | ✅ MERGED | `01-TC-quan-ly-ct-CRUD.md` Section B Negative |
| TC-CT-CRUD-016 | ngan_sach = 0 (boundary inclusive `>=0`) | FR-XI-01 / Inputs#6 | ✅ MERGED | `01-TC-quan-ly-ct-CRUD.md` Section C Edge |
| TC-CT-CRUD-017 | Concurrent UPDATE cùng CT (BR-EC-01 optimistic lock) | FR-XI-01 / BR-EC-01 | ✅ MERGED | `01-TC-quan-ly-ct-CRUD.md` Section C Edge |
| — | SPEC-CLARIFY-CT-03 max length của `ten_chuong_trinh / muc_tieu / doi_tuong / ghi_chu` không nêu trong SRS | FR-XI-01 / Inputs | ⚠️ SPEC-CLARIFY | (Gap report — không sinh TC) |

### File 02 — Search + Export

| TC ID đề xuất | Tiêu đề | Trace | Status | Merged vào |
|---------------|---------|-------|--------|-----------|
| TC-CT-TK-012 | tu_ngay > den_ngay validation | FR-XI-02 / Inputs#4-5 | ✅ MERGED | `02-TC-tim-kiem-ct.md` Section C Edge |

### File 03 — Lifecycle CT

| TC ID đề xuất | Tiêu đề | Trace | Status | Merged vào |
|---------------|---------|-------|--------|-----------|
| TC-LC-016 | Cycle Trình → Rút trình → Trình lại (re-submit) | FR-XI-01 / Rút trình + FR-XI-03 | ✅ MERGED | `03-TC-lifecycle-ct.md` Section E |
| TC-LC-017 | Cycle Trình → Từ chối → Sửa → Trình lại | FR-XI-04 + BR-FLOW-04 | ✅ MERGED | `03-TC-lifecycle-ct.md` Section A (sau Kích hoạt — flow re-submit) hoặc tạo Section F |

### File 06 — Công bố

| TC ID đề xuất | Tiêu đề | Trace | Status | Merged vào |
|---------------|---------|-------|--------|-----------|
| TC-CB-CT-009 | SPEC-CLARIFY-CT-04 — CT có `thoi_gian_ket_thuc` quá khứ vẫn cho công bố? | FR-XI-05 / Preconditions | ✅ MERGED | `06-TC-cong-bo-ct.md` Section D Edge |

### File 07 — CRUD đợt BC

| TC ID đề xuất | Tiêu đề | Trace | Status | Merged vào |
|---------------|---------|-------|--------|-----------|
| TC-DOT-BC-009 | Tạo đợt BC khi CT HOAN_THANH (boundary state pre-condition) | FR-XI-05a / Preconditions | ✅ MERGED | `07-TC-quan-ly-dot-bc.md` Section A Happy |
| TC-DOT-BC-010 | tu_ngay > den_ngay validation cho đợt BC | FR-XI-05a / Inputs#6-7 | ✅ MERGED | `07-TC-quan-ly-dot-bc.md` Section C Validation |

### File 04, 05, 08 — không có edge case bổ sung

- File 04 (Trình PD): TC-TR-CT-006 đã cover concurrent submit. Re-submit cycle move sang file 03.
- File 05 (Phê duyệt): TC-PD-CT-008 đã cover concurrent approve. Cùng-cấp khác đơn vị đã cover qua TC-PD-CT-005 (đã đánh dấu SPEC-CLARIFY-CT-01).
- File 08 (Permission): toàn negative; không sinh thêm edge.

---

## SPEC-CLARIFY tổng hợp (forward sang Gap report)

| ID | Mô tả | File / TC liên quan |
|----|-------|---------------------|
| SPEC-CLARIFY-CT-01 | "Cùng cấp" trong BR-AUTH-05 có cho phép CB PD đơn vị X duyệt CT đơn vị Y cùng cấp ĐP/BN không? | `05-TC-phe-duyet-ct.md` TC-PD-CT-005 |
| SPEC-CLARIFY-CT-02 | `han_nop` đợt BC có validate strict ≤ deadline TT17/2025 hay chỉ hiển thị info? | `07-TC-quan-ly-dot-bc.md` TC-DOT-BC-008 |
| SPEC-CLARIFY-CT-03 | Max length của `ten_chuong_trinh / muc_tieu / doi_tuong / ghi_chu` không nêu trong SRS | (Cross-cutting input boundary) |
| SPEC-CLARIFY-CT-04 | CT có `thoi_gian_ket_thuc` đã qua hôm nay vẫn cho công bố lên Cổng PLQG? | `06-TC-cong-bo-ct.md` TC-CB-CT-009 |
| SPEC-CLARIFY-CT-05 | Soft delete CT (xóa khi DU_THAO) có cascade đợt BC con không? Theo BR-EC-02 thì có, nhưng FR-XI-05a chỉ cho tạo đợt khi CT DANG_THUC_HIEN/HOAN_THANH → đợt không tồn tại khi DU_THAO. → KHÔNG cần test (đợt BC chỉ ra đời sau DA_DUYET / kích hoạt). | (Resolved by spec — không cần TC) |

---

## Tổng kết A4

- **9 TC PROPOSED** → 9 MERGED inline vào file UC
- **5 SPEC-CLARIFY** → forward Gap report
- **Coverage delta**: +9 TC. Total Phase A TC sau A4 = 74 + 9 = **83 TC**

*Generated 2026-05-06 — Phase A step A4 audit log*
