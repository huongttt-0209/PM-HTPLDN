# TC — FR-V.II-05: Đánh giá Hồ sơ theo Tiêu chí (auto-calc BR-CALC-01/02)

> **UC ref**: UC72 | **Screen**: SCR-V.II-02 section 4 (Đánh giá tiêu chí) | **SRS**: srs-fr-06:352-431 + 980-986
> **Roles**: CB_NV (TW/BN/DP) only
> **Mục tiêu**: Verify auto-calc 3 quy mô × NĐ18/2026 (Siêu nhỏ 100%/3M, Nhỏ 30%/5M, Vừa 10%/10M) + công thức BR-CALC-02 `MIN(so_tien_de_nghi, phi_tu_van × muc_ho_tro%, tran_ho_tro_nam − da_chi_trong_nam)` + edge case (phí 0, hết trần năm, snapshot quy mô).

## Preconditions

- HS X đang ở DANG_DANH_GIA (đã qua kiểm tra Đạt — TC-CT-KT-002)
- Login `cb_nv_tw_01`
- 3 HS test seed: X1 (DN siêu nhỏ phí 2.5M), X2 (DN nhỏ phí 10M), X3 (DN vừa phí 200M, đã hỗ trợ 8M trong năm)

## Scenarios

| TC ID | Preconditions | Steps | Expected | BR/AC ref | Severity |
|-------|---------------|-------|----------|-----------|----------|
| TC-CT-DG-001 | HS X1 DANG_DANH_GIA, quy mô SIEU_NHO, phí 2.500.000đ, đề nghị 2.500.000đ, đã hỗ trợ 0đ | 1. Vào /chi-tra/:id 2. Verify section "Đánh giá tiêu chí" hiện | Section 4 hiện 4 readonly: "Mức hỗ trợ (%) = 100%", "Trần hỗ trợ/năm = 3.000.000đ", "Đã chi trả trong năm = 0đ", "Số tiền được duyệt = 2.500.000đ" (= MIN(2.5M, 2.5M×100%, 3M-0)). Hiển thị 3 thành phần MIN | BR-CALC-01, BR-CALC-02, AC#1 | P0 |
| TC-CT-DG-002 | HS X1 DANG_DANH_GIA | 1. Nhập "Ghi chú đánh giá" 2. Click "Xác nhận đánh giá" | HS X1 → DANG_THAM_DINH. Tạo bản ghi DANH_GIA_HO_SO_CHI_TRA (1:1 ho_so_chi_tra_id, ket_qua=DAT, nguoi_danh_gia_id=cb_nv_tw_01.id, ngay_danh_gia=NOW()). AUDIT_LOG. Stepper [Đánh giá] done | SM-CHITRA, BR-DATA-05, srs-fr-06:1191-1206 | P0 |
| TC-CT-DG-003 | HS X2 DANG_DANH_GIA, quy mô NHO, phí 10.000.000đ, đề nghị 5.000.000đ, đã hỗ trợ 0đ | 1. Vào /chi-tra/:id 2. Verify auto-calc | Mức hỗ trợ 30%, Trần 5.000.000đ, Đã chi trả 0đ. Số tiền được duyệt = MIN(5M, 10M×30%=3M, 5M-0) = **3.000.000đ**. Đề nghị 5M nhưng phí×% chặn ở 3M | BR-CALC-01, BR-CALC-02 | P0 |
| TC-CT-DG-004 | HS X3 DANG_DANH_GIA, quy mô VUA, phí 200.000.000đ, đề nghị 10.000.000đ, đã hỗ trợ 8.000.000đ trong năm | 1. Vào /chi-tra/:id 2. Verify auto-calc | Mức hỗ trợ 10%, Trần 10.000.000đ, Đã chi trả 8.000.000đ. Số tiền được duyệt = MIN(10M, 200M×10%=20M, 10M-8M=2M) = **2.000.000đ**. Phần còn trần năm chặn — AC chính BR-CALC-02 MIN | BR-CALC-02, AC#2 | P0 |
| TC-CT-DG-005 | HS DANG_DANH_GIA, quy mô VUA, phí 5.000.000đ, đề nghị 5.000.000đ, đã hỗ trợ 10.000.000đ (đã hết trần năm) | 1. Vào /chi-tra/:id 2. Verify | Số tiền được duyệt = MIN(5M, 5M×10%=0.5M, 10M-10M=0) = **0đ**. UI hiển thị cảnh báo "Doanh nghiệp đã hết trần hỗ trợ trong năm" (EC-05 — srs-fr-06:430). Vẫn cho tiếp tục quy trình | BR-CALC-01, AC#3, EC-05 | P1 |
| TC-CT-DG-006 | HS DANG_DANH_GIA, quy mô SIEU_NHO, phí 0đ (edge), đề nghị 0đ | 1. Vào /chi-tra/:id 2. Verify | Số tiền được duyệt = 0đ (EC-01). Hệ thống cho phép, ghi nhận HS nhưng không phát sinh thanh toán | EC-01, srs-fr-06:426 | P1 |
| TC-CT-DG-007 | HS DANG_DANH_GIA, quy mô SIEU_NHO, phí 1.000.000đ, đề nghị 800.000đ (đề nghị < phí×%) | 1. Vào /chi-tra/:id 2. Verify | Số tiền được duyệt = MIN(800K, 1M×100%=1M, 3M-0) = **800.000đ**. Trường hợp đề nghị thấp hơn phí×% — chặn ở đề nghị | BR-CALC-02 | P0 |
| TC-CT-DG-008 | HS X1 DANG_DANH_GIA, DN đổi quy mô từ SIEU_NHO sang NHO sau khi nộp HS | 1. Vào /chi-tra/:id 2. Verify quy mô hiển thị | Quy mô áp dụng = quy mô tại thời điểm nộp HS (SIEU_NHO snapshot) — KHÔNG đổi theo entity DOANH_NGHIEP hiện tại. (EC-04) | EC-04, srs-fr-06:429 | P1 |
| TC-CT-DG-009 | HS Y trạng thái khác (DANG_KIEM_TRA) | 1. Force POST API đánh giá HS Y | ERR-CT-DG-01 "Hồ sơ không ở trạng thái cho phép đánh giá" — HTTP 400 | ERR-CT-DG-01, srs-fr-06:411 | P0 |
| TC-CT-DG-010 | HS có quy mô_dn = NULL (data corruption hoặc seed thủ công) | 1. Force API đánh giá | ERR-CT-DG-02 "Quy mô DN không hợp lệ" — HTTP 400. UI block submit | ERR-CT-DG-02, srs-fr-06:412 | P0 |
| TC-CT-DG-011 | Reset trần năm 01/01: HS đã được duyệt 2.500.000đ năm 2025 (DA_THANH_TOAN). Tạo HS mới 02/01/2026 quy mô SIEU_NHO | 1. Đánh giá HS mới | Đã chi trả trong năm = 0đ (reset 01/01 — srs-fr-06:1028). Trần lại đầy đủ 3M | BR-CALC-01, srs-fr-06:1028 | P1 |
| TC-CT-DG-012 | HS DANG_DANH_GIA, phí 2.500.000đ, đề nghị 2.500.000đ. CB NV nhập field readonly thử bypass | 1. Inspect element DOM, gỡ readonly attribute từ field "Số tiền được duyệt" 2. Sửa giá trị 5.000.000đ 3. Submit | Backend validate — ignore client value, recalculate theo BR-CALC-02. Số tiền được duyệt vẫn = 2.500.000đ. KHÔNG cho client tampering | BR-CALC-02 (defense) | P0 |

## Edge bổ sung (A4 inline merge)

| TC ID | Preconditions | Steps | Expected | BR/AC ref | Severity |
|-------|---------------|-------|----------|-----------|----------|
| TC-CT-DG-013 | HS DANG_DANH_GIA, quy mô NHO, phí 1.000.000đ, đề nghị 2.000.000đ (đề nghị > phí×%, vẫn dưới trần) | 1. Vào /chi-tra/:id 2. Verify | Số tiền duyệt = MIN(2M, 1M×30%=300K, 5M-0) = **300.000đ**. Phí TV × % chặn — đáng lý DN đề nghị nhiều nhưng pháp lý chỉ chi phần trăm phí TV thực tế | BR-CALC-02 | P0 |
| TC-CT-DG-014 (Codex FINDING-CT-08 fix) | HS DANG_DANH_GIA, quy mô NHO, **phí_tu_van=10.000.000đ, so_tien_de_nghi=5.000.000đ**, đã hỗ trợ trong năm 4.999.999đ (gần hết trần 5M) | 1. Vào /chi-tra/:id 2. Verify | Số tiền duyệt = MIN(5.000.000, 10M×30%=3.000.000, 5M-4.999.999=**1**) = **1đ** (boundary trần năm chặn). Hệ thống cho phép tiếp tục, hiển thị cảnh báo gần hết trần | BR-CALC-01, BR-CALC-02, EC-05 | P1 |
| TC-CT-DG-015 (Codex FINDING-CT-02 fix) | HS DANG_DANH_GIA, phí TV âm (-1.000.000đ — data corruption hoặc DVC payload sai) | 1. Force API đánh giá | Backend reject với validation error do `phi_tu_van CHECK > 0` (HO_SO_CHI_TRA constraint — srs-fr-06:1166). KHÔNG tạo/cập nhật DANH_GIA_HO_SO_CHI_TRA, KHÔNG auto-calc = 0. HTTP 400 + thông báo "Phí tư vấn phải lớn hơn 0" | srs-fr-06:1166 | P1 |
| TC-CT-DG-016 | HS DANG_DANH_GIA, ghi chú đánh giá XSS `<img src=x onerror=alert(1)>` | 1. Nhập + submit 2. Vào lại view Timeline | Backend sanitize. Hiển thị plain text trong Timeline section 8 | BR-EC-13 | P0 |
| TC-CT-DG-017 | DN có 2 HS trong cùng năm: HS_A đã DA_THANH_TOAN 2.000.000đ, HS_B đang DANG_DANH_GIA quy mô NHO | 1. Đánh giá HS_B | "Đã chi trả trong năm" của HS_B = 2.000.000đ (aggregate từ HS_A đã DA_THANH_TOAN — KHÔNG tính TU_CHOI/HUY). Trần còn = 5M-2M=3M | BR-CALC-01 (aggregate scope) | P1 |
| TC-CT-DG-018 (A6 fill GAP-A5-03) | HS DANG_DANH_GIA, quy mô NHO, phí 10.000.000đ, đề nghị 5.000.000đ, đã hỗ trợ 3.000.000đ trong năm (case AC chính SRS srs-fr-06:419) | 1. Vào /chi-tra/:id 2. Verify auto-calc | Số tiền duyệt = MIN(5M, 10M×30%=3M, 5M-3M=2M) = **2.000.000đ**. Trần còn năm chặn — đây là case AC chuẩn SRS | BR-CALC-01, BR-CALC-02, AC#2, srs-fr-06:419 | P0 |
| TC-CT-DG-019 (A6 fill GAP-A5-05) | HS X CHO_TIEP_NHAN, ngày tiếp nhận = 30/04/2026 (thứ 4) — N=10 ngày LV, có ngày lễ 01/05/2026 (Lễ Lao động) | 1. CB NV tiếp nhận HS X 2. Vào /chi-tra/:id 3. Verify cột "Deadline SLA" hoặc cột SLA trên DS | Deadline tính = 30/04 + 10 ngày LV = không tính 01/05 (lễ). Verify deadline = 14/05/2026 (skip 1 ngày lễ + 4 cuối tuần). Cấu hình ngày lễ từ QTHT FR-VIII-29 | BR-CALC-03, srs-fr-06:1370 | P1 |

## Tổng số TC: 19 (A4 +5 edge, A6 +2 fill GAP-A5-03/05)

**P0: 12** | P1: 7

> **A4 audit ref:** [`08-REVIEW-edge-case-hunter.md`](08-REVIEW-edge-case-hunter.md#file-03)
