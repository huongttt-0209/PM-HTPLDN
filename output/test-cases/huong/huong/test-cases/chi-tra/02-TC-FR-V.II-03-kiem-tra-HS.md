# TC — FR-V.II-03: Kiểm tra Hồ sơ Chi trả

> **UC ref**: UC70 | **Screen**: SCR-V.II-02 section 3 (Kiểm tra) | **SRS**: srs-fr-06:233-298 + 974-979
> **Roles**: CB_NV (TW/BN/DP) only
> **Mục tiêu**: Verify checklist 5 thành phần Mẫu 01 NĐ55 + 3 kết quả Đạt/Yêu cầu bổ sung/Không đạt + counter `bo_sung_count` 0..3 + transition state đúng + ghi chú bắt buộc khi YEU_CAU_BO_SUNG/KHONG_DAT.

## Preconditions

- HS X đang ở DANG_KIEM_TRA (đã qua TC-CT-TIEP-NHAN-001 hoặc seed sẵn)
- Login role `cb_nv_tw_01` (hoặc cb_nv_dp_01 cho HS thuộc AG)

## Scenarios

| TC ID | Preconditions | Steps | Expected | BR/AC ref | Severity |
|-------|---------------|-------|----------|-----------|----------|
| TC-CT-KT-001 | HS X DANG_KIEM_TRA | 1. Vào /chi-tra/:id của X 2. Verify section "Kiểm tra hồ sơ" hiện | Section 3 hiện checkbox 5 mục: ☐ Mẫu 01 NĐ55/2019 / ☐ Giấy CN ĐKKD / ☐ Tờ khai / ☐ Hợp đồng TVPL / ☐ Văn bản TVPL. Radio "Đạt / Yêu cầu bổ sung / Không đạt". Textarea "Lý do" + Info "Lần bổ sung: 0/3" | AC#1, srs-fr-06:294, srs-fr-06:975-978 | P0 |
| TC-CT-KT-002 | HS X DANG_KIEM_TRA | 1. Tick đủ 5 checkbox 2. Chọn "Đạt" 3. Click "Xác nhận kiểm tra" | HS X → DANG_DANH_GIA. Stepper bước [Kiểm tra] highlight done, [Đánh giá] active. AUDIT_LOG ghi transition. Toast success. | SM-CHITRA, BR-DATA-05, AC#3 | P0 |
| TC-CT-KT-003 | HS X DANG_KIEM_TRA | 1. Tick 3/5 checkbox 2. Chọn "Yêu cầu bổ sung" 3. Để Lý do trống 4. Click "Xác nhận kiểm tra" | Validation error inline "Ghi chú là bắt buộc khi yêu cầu bổ sung" (ERR-CT-KT-02). KHÔNG submit. Trạng thái KHÔNG đổi. | ERR-CT-KT-02, srs-fr-06:291 | P0 |
| TC-CT-KT-004 | HS X DANG_KIEM_TRA, bo_sung_count=0 | 1. Tick 3/5 2. Chọn "Yêu cầu bổ sung" 3. Nhập Lý do "Thiếu Văn bản TVPL và HĐ TVPL" (≥10 ký tự) 4. Submit | HS X → YEU_CAU_BO_SUNG. `bo_sung_count = 1`, `ngay_yeu_cau_bo_sung = NOW()`. UI counter "Lần bổ sung: 1/3". TB DN qua DVC. | SM-CHITRA, srs-fr-06:267 | P0 |
| TC-CT-KT-005 | HS X DANG_KIEM_TRA, bo_sung_count=2 (đã trải qua 2 lần CBS) | 1. Vào /chi-tra/:id 2. Verify counter | Info "Lần bổ sung: 2/3" highlight đỏ (n ≥ 2 — srs-fr-06:978). Vẫn cho thao tác kiểm tra | AC#1, srs-fr-06:978 | P1 |
| TC-CT-KT-006 | HS X DANG_KIEM_TRA, bo_sung_count=3 (đã 3 lần CBS) | 1. Vào /chi-tra/:id 2. Chọn "Yêu cầu bổ sung" 3. Submit | Hệ thống chặn — counter đã đạt cap 3 (HO_SO_CHI_TRA.bo_sung_count CHECK BETWEEN 0 AND 3 — srs-fr-06:1184). Bắt buộc chuyển sang "Đạt" hoặc "Không đạt". Hoặc ERR thông báo "Đã đạt giới hạn 3 lần bổ sung" | srs-fr-06:1184 | P1 |
| TC-CT-KT-007 | HS X DANG_KIEM_TRA | 1. Tick 0/5 2. Chọn "Không đạt" 3. Nhập Lý do "Doanh nghiệp không đủ điều kiện đề nghị" 4. Submit | HS X → TU_CHOI. `ly_do_tu_choi = "Doanh nghiệp không đủ điều kiện đề nghị"`, `thoi_gian_tu_choi = NOW()`, `nguoi_tu_choi_id = cb_nv_tw_01.id`. TB DN qua DVC | SM-CHITRA, srs-fr-06:268 | P0 |
| TC-CT-KT-008 | HS X DANG_KIEM_TRA | 1. Chọn "Không đạt" 2. Để Lý do trống 3. Submit | Validation error "Lý do là bắt buộc khi không đạt". KHÔNG submit | BR-FLOW-04 (implied), AC#3 | P0 |
| TC-CT-KT-009 | HS Y CHO_TIEP_NHAN (chưa tiếp nhận) | 1. Force vào /chi-tra/:id của Y | Section "Kiểm tra hồ sơ" KHÔNG hiện (conditional render — srs-fr-06:974). Stepper bước [Kiểm tra] chưa active | AC#1, srs-fr-06:974 | P0 |
| TC-CT-KT-010 | HS Z DANG_DANH_GIA (đã qua kiểm tra) | 1. Force POST API kiểm tra với HS Z | ERR-CT-KT-01 "Hồ sơ không ở trạng thái đang kiểm tra" — HTTP 400 | ERR-CT-KT-01, srs-fr-06:290 | P0 |

## Edge bổ sung (A4 inline merge)

| TC ID | Preconditions | Steps | Expected | BR/AC ref | Severity |
|-------|---------------|-------|----------|-----------|----------|
| TC-CT-KT-011 | HS X DANG_KIEM_TRA | 1. Tick 5/5 2. Chọn "Yêu cầu bổ sung" 3. Nhập Lý do 4. Submit | UI rule: nếu tick đủ 5/5 mà chọn YCBS → có cảnh báo "Đã đủ thành phần, vẫn chuyển YCBS?" hoặc cho phép tự do (BA quyết định). **SPEC-CLARIFY-CT-02**: SRS chưa nói có constraint "tick đầy đủ → bắt buộc Đạt" hay không | **SPEC-CLARIFY-CT-02** | P1 |
| TC-CT-KT-012 | HS X DANG_KIEM_TRA | 1. Nhập Lý do chứa XSS payload `<script>alert(1)</script>` 2. Submit | Backend sanitize. Khi xem lại Lý do trong Timeline section 8 → hiển thị plain text, KHÔNG execute script | BR-EC-13 (XSS guard cross-module) | P0 |
| TC-CT-KT-013 | HS X DANG_KIEM_TRA | 1. Nhập Lý do dài 5000 ký tự (giả định cap 2000) 2. Submit | Validation error "Lý do tối đa N ký tự" hoặc backend cắt + cảnh báo. **SPEC-CLARIFY-CT-03**: SRS không nêu max length của ghi_chu UC70 | **SPEC-CLARIFY-CT-03** | P1 |
| TC-CT-KT-014 | HS X YEU_CAU_BO_SUNG, DN bổ sung qua DVC → quay về DANG_KIEM_TRA, bo_sung_count=1 | 1. CB NV vào /chi-tra/:id 2. Verify file đính kèm bổ sung hiện 3. Tick 5/5 4. Đạt 5. Submit | HS → DANG_DANH_GIA. Counter giữ 1. AUDIT_LOG ghi cả 2 lần kiểm tra (lần đầu YCBS + lần 2 DAT). Section 8 Timeline hiển thị đầy đủ | SM-CHITRA, BR-DATA-05 | P0 |
| TC-CT-KT-015 (A6 fill GAP-A5-04 → SPEC-CLARIFY-CT-13) | HS X DANG_KIEM_TRA | 1. Vào /chi-tra/:id 2. Đối chiếu UI checklist trong section 3 với SRS UC70 input "checklist_items: 18 trường" (srs-fr-06:255) | UI hiển thị 5 mục checklist (srs-fr-06:975) NHƯNG SRS UC70 input nói 18 trường Mẫu 01. **SPEC-CLARIFY-CT-13**: 5 mục UI có map tương ứng 18 trường nội bộ hay UI thực sự chỉ check 5 thành phần file đính kèm (Mẫu 01/CN ĐKKD/Tờ khai/HĐ TVPL/VB TVPL)? | **SPEC-CLARIFY-CT-13**, AC#1 | P1 |

## Tổng số TC: 15 (A4 +4 edge, A6 +1 fill GAP-A5-04)

**P0: 10** | P1: 5

> **A4 audit ref:** [`08-REVIEW-edge-case-hunter.md`](08-REVIEW-edge-case-hunter.md#file-02)
