# TC — FR-V.II-13: Cập nhật Kết Quả Thanh Toán

> **UC ref**: UC80 | **Screen**: SCR-V.II-02 section 7 (Cập nhật Thanh toán) | **SRS**: srs-fr-06:772-829 + 996-1001
> **Roles**: CB_NV (TW/BN/DP) only
> **Mục tiêu**: Verify CB NV cập nhật KQ thanh toán cuối từ DA_DUYET → DA_THANH_TOAN hoặc TU_CHOI (ly_do="THANH_TOAN") + validate so_tien_thuc_tra ≤ so_tien_duoc_duyet + ngày thanh toán bắt buộc.

## Preconditions

- HS X DA_DUYET (đã qua TC-CT-PD-002), so_tien_duoc_duyet = 2.500.000đ
- Login `cb_nv_tw_01` (CB NV — KHÔNG phải CB PD)

## Scenarios

| TC ID | Preconditions | Steps | Expected | BR/AC ref | Severity |
|-------|---------------|-------|----------|-----------|----------|
| TC-CT-TT-001 | HS X DA_DUYET, login `cb_nv_tw_01` | 1. Vào /chi-tra/:id 2. Verify section "Cập nhật Thanh toán" | Section 7 hiện 4 field: "Số tiền thực trả" (Number, bắt buộc, > 0 AND ≤ so_tien_duoc_duyet), "Ngày thanh toán" (DatePicker, bắt buộc, default hôm nay, ≤ hôm nay), "Số biên nhận" (Text, optional), "Ghi chú thanh toán" (Textarea, optional) + nút "Cập nhật thanh toán" | AC#1, srs-fr-06:996-1001 | P0 |
| TC-CT-TT-002 | HS X DA_DUYET, so_tien_duoc_duyet=2.500.000đ | 1. Nhập so_tien_thuc_tra = 2.500.000đ 2. Ngày TT = hôm nay 3. Số biên nhận "BN-2026-0001" 4. Click "Cập nhật thanh toán" | HS X → DA_THANH_TOAN. `so_tien_thuc_tra=2500000`, `ngay_thanh_toan=NOW().date()`, `so_bien_nhan="BN-2026-0001"`. TB DN + TVV. AUDIT_LOG. Stepper [Thanh toán] done | SM-CHITRA, BR-DATA-05, srs-fr-06:794-802 | P0 |
| TC-CT-TT-003 | HS X DA_DUYET, so_tien_duoc_duyet=2.500.000đ | 1. Nhập so_tien_thuc_tra = 3.000.000đ (vượt) 2. Submit | Validation error "Số tiền thực trả không được vượt số tiền được duyệt" (ERR-CT-TT-02). KHÔNG submit | ERR-CT-TT-02, srs-fr-06:823 | P0 |
| TC-CT-TT-004 | HS X DA_DUYET | 1. Nhập so_tien_thuc_tra = 2.000.000đ 2. Để Ngày TT trống 3. Submit | Validation error "Ngày thanh toán là bắt buộc" (ERR-CT-TT-03) | ERR-CT-TT-03, srs-fr-06:824 | P0 |
| TC-CT-TT-005 | HS X DA_DUYET | 1. Nhập so_tien_thuc_tra = 2.000.000đ 2. Ngày TT = ngày mai (tương lai) 3. Submit | Validation error "Ngày thanh toán không được trong tương lai" (UI rule srs-fr-06:998 "Validate: ≤ hôm nay") | srs-fr-06:998 | P0 |
| TC-CT-TT-006 (Codex FINDING-CT-09 fix) | HS X DA_DUYET | 1. Click action "Từ chối thanh toán" (nếu UI section 7 chưa có nút riêng → CB NV thao tác qua menu kebab/dropdown action hoặc API endpoint testable) 2. Nhập lý do "Doanh nghiệp không cung cấp đủ chứng từ thanh toán" 3. Submit | HS X → TU_CHOI. `ly_do_tu_choi = "THANH_TOAN: Doanh nghiệp không cung cấp..."`, `thoi_gian_tu_choi=NOW()`, `nguoi_tu_choi_id=cb_nv_tw_01.id`. TB DN/TVV. **TC này BẮT BUỘC verify transition DA_DUYET → TU_CHOI per SM-CHITRA srs-fr-06:1326. SPEC-CLARIFY-CT-01 forward BA xác nhận UI entry point** — KHÔNG mark N/A khi Phase B; nếu UI thiếu entry point → log BUG-CT-MISSING-DENY-PAYMENT thay vì skip | SM-CHITRA, srs-fr-06:1326, **SPEC-CLARIFY-CT-01** | P0 |
| TC-CT-TT-007 | HS Y trạng thái khác (CHO_PHE_DUYET) | 1. Force POST API cập nhật TT Y | ERR-CT-TT-01 "Hồ sơ không ở trạng thái đã duyệt" — HTTP 400 | ERR-CT-TT-01, srs-fr-06:822 | P0 |
| TC-CT-TT-008 | HS X DA_DUYET, login `cb_nv_dp_01` (AG) — HS X thuộc TW | 1. Force GET /chi-tra/:id của X | 403/404 (BR-AUTH-08 scope đơn vị) | BR-AUTH-08 | P1 |

## Edge bổ sung (A4 inline merge)

| TC ID | Preconditions | Steps | Expected | BR/AC ref | Severity |
|-------|---------------|-------|----------|-----------|----------|
| TC-CT-TT-009 (Codex FINDING-CT-04 fix) | HS X DA_DUYET, so_tien_duoc_duyet=2.500.000đ | 1. Nhập so_tien_thuc_tra = 0 đ 2. Submit | Validation error "Số tiền thực trả phải > 0 và không được vượt số tiền được duyệt" (srs-fr-06:997 "Validate: > 0 AND ≤ so_tien_duoc_duyet"). KHÔNG submit. **Edge case riêng**: Nếu so_tien_duoc_duyet=0 (do EC-01 phí TV=0), không thực hiện luồng cập nhật thanh toán — xử lý theo BA clarification riêng (SPEC-CLARIFY-CT-08 forward) | srs-fr-06:997, **SPEC-CLARIFY-CT-08** | P1 |
| TC-CT-TT-010 | HS X DA_DUYET, ngày phê duyệt = 05/05/2026 | 1. Nhập ngay_thanh_toan = 01/05/2026 (trước phê duyệt) 2. Submit | **SPEC-CLARIFY-CT-09**: SRS không quy định ngay_thanh_toan ≥ ngay_phe_duyet. Logic nghiệp vụ: không thể TT trước khi duyệt → backend nên block | **SPEC-CLARIFY-CT-09** | P1 |
| TC-CT-TT-011 | HS X DA_DUYET | 1. Nhập so_bien_nhan = "BN-2026-0001" (đã dùng cho HS Y khác) 2. Submit | **SPEC-CLARIFY-CT-10**: SRS không có UNIQUE constraint trên `so_bien_nhan`. Cho phép trùng? Hay backend validate? | **SPEC-CLARIFY-CT-10** | P1 |
| TC-CT-TT-012 | HS X DA_DUYET | 1. Nhập so_tien_thuc_tra = "abc" (text trong field number) 2. Submit | UI Number input chặn keypress non-digit. Nếu paste → field trống hoặc validation "Vui lòng nhập số" | srs-fr-06:997 (Number type) | P1 |

## Tổng số TC: 12 (A4 +4 edge, Codex apply: TC-CT-TT-006 P1→P0)

**P0: 7** | P1: 5

> **A4 audit ref:** [`08-REVIEW-edge-case-hunter.md`](08-REVIEW-edge-case-hunter.md#file-06)
