# TC — FR-V.II-14: DN Bổ Sung Hồ Sơ Chi Trả (GAP-V.II-01)

> **UC ref**: GAP-V.II-01 | **Screen**: Cổng DVC / Cổng PLQG (DN) hoặc SCR-V.II-02 (CB NV thủ công) | **SRS**: srs-fr-06:833-892
> **Roles**: DN (qua chuyên trang/DVC) hoặc CB_NV (thủ công)
> **Mục tiêu**: Verify DN upload tài liệu bổ sung khi HS YEU_CAU_BO_SUNG → trở lại DANG_KIEM_TRA + validate file (định dạng PDF/DOC/DOCX/JPG/PNG ≤ 10MB) + deadline 5 ngày LV.

## Preconditions

- HS X YEU_CAU_BO_SUNG (đã qua TC-CT-KT-004), `ngay_yeu_cau_bo_sung` đã set, `bo_sung_count = 1`
- Login `dn_01` (qua chuyên trang DN/Cổng PLQG)
- File test: `valid.pdf` (5MB), `valid.docx` (8MB), `huge.pdf` (15MB — quá), `script.exe` (sai định dạng)

## Scenarios

| TC ID | Preconditions | Steps | Expected | BR/AC ref | Severity |
|-------|---------------|-------|----------|-----------|----------|
| TC-CT-BS-001 | HS X YEU_CAU_BO_SUNG, login `dn_01` qua chuyên trang | 1. Vào trang HS Chi trả của tôi 2. Click HS X 3. Click "Bổ sung hồ sơ" 4. Upload `valid.pdf` 5. Nhập ghi chú "Bổ sung VB TVPL theo yêu cầu" 6. Submit | HS X → DANG_KIEM_TRA. File lưu vào FILE_DINH_KEM gắn với ho_so_chi_tra_id. CB NV phụ trách nhận TB "DN đã bổ sung hồ sơ chi trả, vui lòng kiểm tra lại". AUDIT_LOG hành động='BO_SUNG_HO_SO_CT'. Counter `bo_sung_count` giữ nguyên 1 (đã tăng ở UC70 lần trước) | SM-CHITRA, BR-NOTIF-01, srs-fr-06:858-867 | P0 |
| TC-CT-BS-002 | HS X YEU_CAU_BO_SUNG | 1. Upload `huge.pdf` (15MB > 10MB) | Validation error "File không hợp lệ" (ERR-CT-BS-02). Toast cảnh báo dung lượng | ERR-CT-BS-02, srs-fr-06:883 | P0 |
| TC-CT-BS-003 | HS X YEU_CAU_BO_SUNG | 1. Upload `script.exe` (sai định dạng) | Validation error "File không hợp lệ" (ERR-CT-BS-02) — chỉ accept PDF/DOC/DOCX/JPG/PNG | ERR-CT-BS-02, srs-fr-06:855 | P0 |
| TC-CT-BS-004 | HS X YEU_CAU_BO_SUNG, `ngay_yeu_cau_bo_sung` = 6 ngày LV trước (quá hạn 5 ngày LV) | 1. Upload `valid.pdf` 2. Submit | ERR-CT-BS-03 "Đã quá thời hạn bổ sung" — HTTP 400. KHÔNG cho upload | ERR-CT-BS-03, srs-fr-06:884, srs-fr-06:849 | P0 |
| TC-CT-BS-005 | HS Y DANG_KIEM_TRA (chưa bị YCBS) | 1. Force POST API bổ sung HS Y | ERR-CT-BS-01 "Hồ sơ không ở trạng thái yêu cầu bổ sung" — HTTP 400 | ERR-CT-BS-01, srs-fr-06:882 | P0 |
| TC-CT-BS-006 | HS X YEU_CAU_BO_SUNG của dn_01, login `dn_02` | 1. Force GET HS X qua chuyên trang dn_02 | 403/404 — DN khác KHÔNG thấy HS không phải của mình | BR-AUTH-08 (DN scope) | P0 |

## Edge bổ sung (A4 inline merge)

| TC ID | Preconditions | Steps | Expected | BR/AC ref | Severity |
|-------|---------------|-------|----------|-----------|----------|
| TC-CT-BS-007 | HS X YEU_CAU_BO_SUNG, login `dn_01` | 1. Upload 5 file PDF cùng lúc, mỗi file 9MB 2. Submit | Tổng dung lượng 45MB. **SPEC-CLARIFY-CT-11**: SRS chỉ nêu giới hạn 10MB/file (srs-fr-06:855), không giới hạn tổng. → Backend nên có cap tổng để tránh DoS | **SPEC-CLARIFY-CT-11** | P1 |
| TC-CT-BS-008 | HS X YEU_CAU_BO_SUNG, `ngay_yeu_cau_bo_sung` = đúng 5 ngày LV trước (boundary) | 1. Upload `valid.pdf` 2. Submit | Cho phép (boundary inclusive). HS → DANG_KIEM_TRA. **SPEC-CLARIFY-CT-12**: ERR-CT-BS-03 nói "> 5 ngày" hay "≥ 5 ngày"? Boundary inclusive/exclusive? | **SPEC-CLARIFY-CT-12**, srs-fr-06:849 | P1 |
| TC-CT-BS-009 | HS X YEU_CAU_BO_SUNG | 1. Upload file tên Unicode "Hợp đồng TVPL số 01/2026.pdf" | Cho phép. File lưu vào FILE_DINH_KEM với tên gốc Unicode. Tải về vẫn giữ tên đúng | BR-DATA-03 | P1 |
| TC-CT-BS-010 | HS X YEU_CAU_BO_SUNG, mỗi file đúng 10MB (boundary) | 1. Upload `boundary-10mb.pdf` exact 10MB 2. Submit | Cho phép (≤ 10MB inclusive — srs-fr-06:855). Verify backend accept | srs-fr-06:855 | P1 |

## Tổng số TC: 10 (sau A4: +4 edge)

**P0: 6** | P1: 4

> **A4 audit ref:** [`08-REVIEW-edge-case-hunter.md`](08-REVIEW-edge-case-hunter.md#file-07)
