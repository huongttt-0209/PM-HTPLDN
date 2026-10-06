# TC — FR-V.II-11 + FR-V.II-12: Trình Phê Duyệt + Phê Duyệt / Trả Về Thẩm Định

> **UC ref**: UC78 + UC79 | **Screen**: SCR-V.II-02 section 5 (Trình PD) + section 6 (Phê duyệt) | **SRS**: srs-fr-06:661-769 + 991-995
> **Roles**: CB_NV (Trình PD) + CB_PD cùng cấp (Duyệt/Trả về — BR-AUTH-05)
> **Mục tiêu**: Verify CB NV trình PD chỉ khi DANG_THAM_DINH + ket_qua=DAT + CB PD cùng cấp đơn vị duyệt/trả về (BR-FLOW-04 lý do ≥10 ký tự) + N:1 history PHE_DUYET_CHI_TRA + multi-loop trả về → trình lại.

## Preconditions

- HS X DANG_THAM_DINH với ket_qua_tham_dinh=DAT (đã qua TC-CT-TD-002)
- Login `cb_nv_tw_01` cho Trình PD; `cb_pd_tw_01` cho Phê duyệt
- HS Y DANG_THAM_DINH với ket_qua=KHONG_DAT để verify guard

## Scenarios

| TC ID | Preconditions | Steps | Expected | BR/AC ref | Severity |
|-------|---------------|-------|----------|-----------|----------|
| TC-CT-TRINH-001 | HS X DANG_THAM_DINH + DAT, login `cb_nv_tw_01` | 1. Vào /chi-tra/:id 2. Click "Trình phê duyệt" | HS X → CHO_PHE_DUYET. CB PD TW (cùng cấp) nhận TB. AUDIT_LOG ghi transition. Stepper [Phê duyệt] active | SM-CHITRA, BR-AUTH-05, BR-DATA-05, srs-fr-06:684-686 | P0 |
| TC-CT-TRINH-002 | HS Y DANG_THAM_DINH + KHONG_DAT (chưa thẩm định Đạt) | 1. Vào /chi-tra/:id của Y 2. Tìm nút Trình PD | Nút "Trình phê duyệt" KHÔNG hiện (conditional render — srs-fr-06:991). Force POST API → ERR-CT-TRINH-01 "Hồ sơ chưa đủ điều kiện trình phê duyệt" | ERR-CT-TRINH-01, srs-fr-06:702-707 | P0 |
| TC-CT-TRINH-003 | HS Z DANG_DANH_GIA (chưa thẩm định) | 1. Force POST API trình PD HS Z | ERR-CT-TRINH-01 "Hồ sơ chưa đủ điều kiện trình phê duyệt" | ERR-CT-TRINH-01 | P0 |
| TC-CT-PD-001 | HS X CHO_PHE_DUYET cùng cấp TW, login `cb_pd_tw_01` | 1. Vào /chi-tra/:id 2. Verify section "Phê duyệt" hiện | Section 6 hiện Info card tóm tắt: DN/Quy mô/Phí TV/Số tiền đề nghị/Số tiền duyệt/Mức hỗ trợ%. Nút "Phê duyệt" + "Từ chối — trả về thẩm định" hiện | AC#1, srs-fr-06:993-995 | P0 |
| TC-CT-PD-002 | HS X CHO_PHE_DUYET, login `cb_pd_tw_01` | 1. Click "Phê duyệt" 2. Modal xác nhận hiện 3. Nhập số tiền duyệt 2.500.000đ 4. Confirm | HS X → DA_DUYET. `ngay_phe_duyet=NOW()`, `nguoi_phe_duyet_id=cb_pd_tw_01.id`. Tạo PHE_DUYET_CHI_TRA (quyet_dinh=DUYET, so_tien_duyet=2500000). TB CB NV + TVV + DN. | SM-CHITRA, srs-fr-06:736, srs-fr-06:1227-1244 | P0 |
| TC-CT-PD-003 | HS X CHO_PHE_DUYET, login `cb_pd_tw_01` | 1. Click "Phê duyệt" 2. Để số tiền duyệt trống | Validation error "Số tiền phê duyệt là bắt buộc" (ERR-CT-PD-03) | ERR-CT-PD-03, srs-fr-06:762 | P0 |
| TC-CT-PD-004 | HS X CHO_PHE_DUYET, login `cb_pd_tw_01` | 1. Click "Từ chối — trả về thẩm định" 2. Modal nhập lý do "Số tiền duyệt cần xem xét lại" (≥10 ký tự) 3. Confirm | HS X → DANG_THAM_DINH (TRẢ VỀ, KHÔNG phải TU_CHOI cuối). Tạo PHE_DUYET_CHI_TRA (quyet_dinh=TU_CHOI, ly_do_tu_choi). KHÔNG ghi `thoi_gian_tu_choi`. TB CB NV "CB PD từ chối, yêu cầu điều chỉnh" — KHÔNG gửi TVV/DN. AUDIT_LOG | SM-CHITRA, BR-FLOW-04, srs-fr-06:737, srs-fr-06:766 | P0 |
| TC-CT-PD-005 | HS X CHO_PHE_DUYET, login `cb_pd_tw_01` | 1. Click "Từ chối" 2. Để Lý do trống | Validation "Lý do từ chối là bắt buộc" (ERR-CT-PD-02) | ERR-CT-PD-02, srs-fr-06:761 | P0 |
| TC-CT-PD-006 | HS X CHO_PHE_DUYET, login `cb_pd_tw_01` | 1. Click "Từ chối" 2. Nhập lý do 5 ký tự "ngắn" 3. Confirm | Validation "Lý do từ chối phải ≥ 10 ký tự" (BR-FLOW-04) | BR-FLOW-04, srs-fr-06:1238, srs-fr-06:766 | P0 |
| TC-CT-PD-007 (Codex FINDING-CT-01 fix) | HS X DANG_THAM_DINH (vừa bị PD trả về TC-CT-PD-004), CB NV chỉnh lại | 1. Login `cb_nv_tw_01` 2. Vào /chi-tra/:id 3. Sửa Nhận xét + so_tien_de_xuat 4. Click "Trình phê duyệt" lại | HS X → CHO_PHE_DUYET (lần 2). **KHÔNG tạo PHE_DUYET_CHI_TRA tại bước Trình PD** (PHE_DUYET_CHI_TRA chỉ được tạo khi CB PD DUYET hoặc TU_CHOI ở UC79 — srs-fr-06:738). Chỉ AUDIT_LOG ghi hành động TRINH_PHE_DUYET. CB PD TW nhận TB lần 2. Bản ghi PHE_DUYET_CHI_TRA mới sẽ tạo khi CB PD ra quyết định kế tiếp (N:1 — multi-loop) | srs-fr-06:684, srs-fr-06:738 | P0 |
| TC-CT-PD-008 | HS X CHO_PHE_DUYET cùng cấp TW, login `cb_pd_dp_01` (DP — KHÁC CẤP) | 1. Force GET /chi-tra/:id của X 2. Hoặc force POST /api/chi-tra/:id/duyet | 403 Forbidden (BR-AUTH-05). KHÔNG cho duyệt xuyên cấp | BR-AUTH-05, srs-fr-06:734, srs-fr-06:768 | P0 |
| TC-CT-PD-009 | HS Y trạng thái khác (DA_DUYET đã duyệt) | 1. Force POST API duyệt Y | ERR-CT-PD-01 "Hồ sơ không ở trạng thái chờ phê duyệt" | ERR-CT-PD-01, srs-fr-06:760 | P0 |
| TC-CT-PD-010 | HS X CHO_PHE_DUYET, login `cb_nv_tw_01` (CB NV — KHÔNG phải CB PD) | 1. Vào /chi-tra/:id 2. Tìm nút Phê duyệt | Nút "Phê duyệt" + "Từ chối" KHÔNG hiện. CB NV chỉ thấy info card. Force API → 403 | BR-AUTH-05 (role) | P0 |

## Edge bổ sung (A4 inline merge)

| TC ID | Preconditions | Steps | Expected | BR/AC ref | Severity |
|-------|---------------|-------|----------|-----------|----------|
| TC-CT-PD-011 | HS X CHO_PHE_DUYET, so_tien_duoc_duyet=2.500.000đ, login `cb_pd_tw_01` | 1. Click "Phê duyệt" 2. Nhập so_tien_duyet = 5.000.000đ (vượt) 3. Confirm | **SPEC-CLARIFY-CT-06**: SRS không nêu rõ ràng buộc so_tien_duyet ≤ so_tien_duoc_duyet ở UC79 (chỉ CHECK ≥ 0 trên PHE_DUYET_CHI_TRA — srs-fr-06:1237). EC-02 (srs-fr-06:427) chỉ nói thanh toán không vượt duyệt. CB PD có thể duyệt nhiều hơn evaluation nếu có lý do? Nên cảnh báo | **SPEC-CLARIFY-CT-06**, EC-02 | P1 |
| TC-CT-PD-012 | HS X CHO_PHE_DUYET, login `cb_pd_tw_01` | 1. Click "Phê duyệt" 2. Nhập so_tien_duyet = 0 đ 3. Confirm | CHECK ≥ 0 cho phép. Edge case: duyệt 0đ — HS → DA_DUYET nhưng không phát sinh thanh toán. UI nên có warning | srs-fr-06:1237 | P1 |
| TC-CT-PD-013 | 2 CB PD cùng cấp (cb_pd_tw_01 + cb_pd_tw_02) cùng vào HS X CHO_PHE_DUYET | 1. Cả hai click "Phê duyệt" gần đồng thời | Một thắng (HS → DA_DUYET, ghi nguoi_phe_duyet_id của user đầu). User thứ 2 nhận ERR-CT-PD-01 + toast "Hồ sơ đã được duyệt" | ERR-CT-PD-01, BR-EC-01 | P1 |
| TC-CT-PD-014 | HS X qua nhiều vòng PD: trả về 3 lần, duyệt lần 4 | 1. Verify PHE_DUYET_CHI_TRA 2. Verify Timeline | PHE_DUYET_CHI_TRA có 4 bản ghi (3 TU_CHOI + 1 DUYET cuối). Timeline hiển thị đầy đủ. AUDIT_LOG đầy đủ transitions | srs-fr-06:1227-1244, BR-DATA-05 | P0 |
| TC-CT-PD-015 | HS X CHO_PHE_DUYET, login `cb_pd_tw_01` | 1. Click "Từ chối" 2. Nhập lý do dài 3000 ký tự (giả định cap 1000) 3. Submit | Validation hoặc backend cắt + cảnh báo. **SPEC-CLARIFY-CT-07**: SRS không nêu max length của ly_do_tu_choi UC79 (chỉ ≥ 10 — BR-FLOW-04) | **SPEC-CLARIFY-CT-07** | P1 |

## Tổng số TC: 18 (sau A4: +5 edge)

**P0: 14** | P1: 4

> **A4 audit ref:** [`08-REVIEW-edge-case-hunter.md`](08-REVIEW-edge-case-hunter.md#file-05)
