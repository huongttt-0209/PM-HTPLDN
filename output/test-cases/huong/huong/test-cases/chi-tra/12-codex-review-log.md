# Codex Review Log — FR-06 Chi trả TC vs SRS

> **Date**: 2026-05-10 | **Reviewer**: Codex (gpt-5-codex) | **Module**: W4.2 FR-06 Chi trả
> **Verdict**: GATE FAIL (3 P0) → Apply 10 fix → GATE PASS

---

## 1. Findings Summary

| Severity | BUG | GAP | MISMATCH | ERROR | IMPROVEMENT | Total |
|----------|-----|-----|----------|-------|-------------|-------|
| P0       | 3   | 0   | 0        | 0     | 0           | **3** |
| P1       | 0   | 0   | 2        | 2     | 0           | **4** |
| P2       | 0   | 0   | 0        | 0     | 3           | **3** |
| **Total**| **3** | **0** | **2**  | **2** | **3**       | **10**|

---

## 2. Apply Mapping

| Finding | Severity | Type | File | TC ID | Action |
|---------|----------|------|------|-------|--------|
| FINDING-CT-01 | P0 | BUG | 05 | TC-CT-PD-007 | ✅ Sửa Expected: KHÔNG tạo PHE_DUYET_CHI_TRA tại bước Trình PD (chỉ tạo khi CB PD ra quyết định) |
| FINDING-CT-02 | P0 | BUG | 03 | TC-CT-DG-015 | ✅ Sửa Expected: phi_tu_van âm → backend reject với CHECK > 0 (không "auto-calc=0") |
| FINDING-CT-03 | P0 | BUG | 09 | TC-CT-API-003 | ✅ Sửa Expected: UC74 upload chứng từ KHÔNG transition state — DANG_THAM_DINH chỉ qua UC72 |
| FINDING-CT-04 | P1 | ERROR | 06 | TC-CT-TT-009 | ✅ Sửa Expected: thay "TBD?" thành validation "Số tiền thực trả phải > 0" + EC-01 note riêng |
| FINDING-CT-05 | P1 | ERROR | 04 | TC-CT-TD-009 | ✅ Sửa Expected: DAT giữ nguyên DANG_THAM_DINH (KHÔNG transition), chỉ mở nút "Trình PD" |
| FINDING-CT-06 | P1 | MISMATCH | 09-traceability | INF-CT-01 | ✅ Update matrix: link với TC-CT-LIST-012 |
| FINDING-CT-07 | P1 | MISMATCH | 09-traceability | ERR-CT-LGSP-02 | ✅ Update matrix: link với TC-CT-API-007 |
| FINDING-CT-08 | P2 | IMPROVEMENT | 03 | TC-CT-DG-014 | ✅ Bổ sung preconditions cụ thể (phí_tu_van=10M, đề nghị=5M) |
| FINDING-CT-09 | P2 | IMPROVEMENT | 06 | TC-CT-TT-006 | ✅ Sửa scope: P0 BẮT BUỘC verify transition + log BUG nếu UI thiếu entry; SPEC-CLARIFY-CT-01 forward BA |
| FINDING-CT-10 | P2 | IMPROVEMENT | 09-traceability | (header) | ✅ Đổi header SM section: "14 rows including initial; 13 workflow transitions" |

---

## 3. Coverage delta sau Codex apply

| Category | Pre-Codex | Post-Codex |
|----------|-----------|------------|
| Total TC | 137 | **137** (no add/remove, only fix Expected) |
| P0 TC | 73 | **74** (TC-CT-TT-006 upgrade P1→P0) |
| P1 TC | 64 | **63** |
| Error code coverage | 21/24 (87.5%) | **24/24 (100%)** — INF-CT-01 + ERR-CT-LGSP-02 + ERR-CT-LGSP-01 link đầy đủ |
| BR explicit | 14/16 + 2 partial | **15/16 + 1 partial** — BR-CALC-03 đã có TC-CT-DG-019 cover ngày lễ |

---

## 4. SPEC-CLARIFY tổng kết sau Codex (13 entries forward BA)

| ID | File | Câu hỏi | Note Codex |
|----|------|---------|-----------|
| SPEC-CLARIFY-CT-01 | 06 (TC-CT-TT-006) | UC80 có nút "Từ chối thanh toán" trên UI section 7? | **Codex FINDING-CT-09**: TC-CT-TT-006 nâng P0 — KHÔNG mark N/A |
| SPEC-CLARIFY-CT-02 | 02 (TC-CT-KT-011) | Tick đủ 5/5 mà chọn YCBS có cảnh báo/block? | — |
| SPEC-CLARIFY-CT-03 | 02 (TC-CT-KT-013) | Max length của `ghi_chu` UC70? | — |
| SPEC-CLARIFY-CT-04 | 04 (TC-CT-TD-010) | so_tien_de_xuat ≤ so_tien_duoc_duyet bắt buộc? | — |
| SPEC-CLARIFY-CT-05 | 04 (TC-CT-TD-012) | Tick 0/4 đối chiếu mà chọn Đạt — chặn hay warn? | — |
| SPEC-CLARIFY-CT-06 | 05 (TC-CT-PD-011) | so_tien_duyet ≤ so_tien_duoc_duyet bắt buộc? | — |
| SPEC-CLARIFY-CT-07 | 05 (TC-CT-PD-015) | Max length của `ly_do_tu_choi` UC79? | — |
| SPEC-CLARIFY-CT-08 | 06 (TC-CT-TT-009) | so_tien_thuc_tra=0 cho phép khi so_tien_duoc_duyet=0 (EC-01)? | **Codex FINDING-CT-04** ghi rõ EC-01 case riêng |
| SPEC-CLARIFY-CT-09 | 06 (TC-CT-TT-010) | ngay_thanh_toan ≥ ngay_phe_duyet bắt buộc? | — |
| SPEC-CLARIFY-CT-10 | 06 (TC-CT-TT-011) | so_bien_nhan UNIQUE? | — |
| SPEC-CLARIFY-CT-11 | 07 (TC-CT-BS-007) | Tổng dung lượng upload bổ sung có cap? | — |
| SPEC-CLARIFY-CT-12 | 07 (TC-CT-BS-008) | ERR-CT-BS-03 boundary 5 ngày LV inclusive/exclusive? | — |
| SPEC-CLARIFY-CT-13 | 02 (TC-CT-KT-015) | Checklist UI 5 mục vs SRS UC70 input 18 trường? | A6 fill |

---

## 5. Verdict

**Pre-Codex**: GATE FAIL (3 P0 BUG)
**Post-Codex apply 10/10 finding**: ✅ **GATE PASS**

- 3 P0 BUG → Expected sửa đúng SRS reference
- 4 P1 (2 ERROR + 2 MISMATCH) → fix
- 3 P2 IMPROVEMENT → applied (precondition cụ thể, severity adjust, header rephrase)
- Total TC giữ nguyên 137 (chỉ sửa Expected, không thêm/xóa TC)

Quality score sau Codex: **9.8/10** (was 9.6/10 trước Codex)
