# A4 — Edge Case Hunter Review (audit log)

> **Method**: bmad-review-edge-case-hunter | **Date**: 2026-05-10 | **Module**: FR-06 Chi trả
> **Inline merge rule (Iron Rule)**: Mọi TC mới phát sinh từ A4 đã Edit trực tiếp vào file UC `NN-TC-*.md` (Section "Edge bổ sung"). File này CHỈ là audit log proposal + reasoning + merge mapping — KHÔNG phải TC source.

---

## Tổng quan A4 delta

| File UC | TC base (A3) | TC sau A4 | Delta | Reasoning |
|---------|--------------|-----------|-------|-----------|
| 01-TC-FR-V.II-02-quan-ly-HS-de-nghi.md (#file-01) | 13 | 18 | +5 | Range ngày đảo, sort + pagination, race condition tiếp nhận, xuất Excel, cancel modal rút HS |
| 02-TC-FR-V.II-03-kiem-tra-HS.md (#file-02) | 10 | 14 | +4 | UI rule 5/5 + YCBS, XSS sanitize, max length ghi chú, re-loop YCBS→DANG_KIEM_TRA |
| 03-TC-FR-V.II-05-danh-gia-tieu-chi.md (#file-03) | 12 | 17 | +5 | Phí×% dominate, boundary trần năm 1đ, phí âm, XSS ghi chú, multi-HS aggregate cùng năm |
| 04-TC-FR-V.II-09-tham-dinh.md (#file-04) | 9 | 13 | +4 | so_tien_de_xuat > duoc_duyet, re-edit thẩm định, tick 0/4 vẫn Đạt, XSS nhận xét |
| 05-TC-FR-V.II-11-12-trinh-PD-phe-duyet.md (#file-05) | 13 | 18 | +5 | so_tien_duyet > duoc_duyet, duyệt 0đ, race CB PD, multi-loop trả về, max length lý do |
| 06-TC-FR-V.II-13-cap-nhat-thanh-toan.md (#file-06) | 8 | 12 | +4 | so_tien_thuc_tra=0 conflict EC-01, ngày TT < ngày duyệt, biên nhận trùng, text vào field number |
| 07-TC-FR-V.II-14-DN-bo-sung-HS.md (#file-07) | 6 | 10 | +4 | Multi-file 5×9MB, boundary 5 ngày LV, file Unicode, file đúng 10MB |
| 08-TC-FR-V.II-08-thong-bao-TVV.md (#file-08) | 4 | 6 | +2 | Empty state, > 100 TB pagination |
| 09-TC-API-side-effect.md (#file-09) | 4 | 6 | +2 | LGSP idempotent (ERR-CT-02), retry 3 lần fail → cảnh báo CB NV |
| 10-TC-permission-matrix.md (#file-10) | 14 | 18 | +4 | Session timeout, IDOR thay đổi URL param, BR-AUTH-05 force xuyên cấp, DN force bổ sung HS DN khác |
| **Tổng** | **93** | **132** | **+39** | — |

---

## SPEC-CLARIFY phát sinh từ A4 (12 entries forward Phase B BA)

| ID | File | Câu hỏi | Lý do |
|----|------|---------|-------|
| SPEC-CLARIFY-CT-01 | 06 (TC-CT-TT-006) | UC80 có nút "Từ chối thanh toán" trên UI section 7? | SCR-V.II-02 section 7 chỉ có nút "Cập nhật thanh toán", nhưng SM-CHITRA srs-fr-06:1326 cho phép DA_DUYET → TU_CHOI |
| SPEC-CLARIFY-CT-02 | 02 (TC-CT-KT-011) | Tick đủ 5/5 mà chọn YCBS có cảnh báo/block? | SRS không nêu UI rule cảnh báo |
| SPEC-CLARIFY-CT-03 | 02 (TC-CT-KT-013) | Max length của `ghi_chu` UC70? | SRS không nêu cap |
| SPEC-CLARIFY-CT-04 | 04 (TC-CT-TD-010) | so_tien_de_xuat ≤ so_tien_duoc_duyet bắt buộc? | SRS chỉ CHECK ≥ 0 (srs-fr-06:1219) |
| SPEC-CLARIFY-CT-05 | 04 (TC-CT-TD-012) | Tick 0/4 đối chiếu mà chọn Đạt — chặn hay warn? | SRS không nêu UI rule |
| SPEC-CLARIFY-CT-06 | 05 (TC-CT-PD-011) | so_tien_duyet ≤ so_tien_duoc_duyet bắt buộc? | SRS chỉ CHECK ≥ 0 (srs-fr-06:1237). EC-02 nói TT không vượt duyệt nhưng không nói duyệt vs evaluation |
| SPEC-CLARIFY-CT-07 | 05 (TC-CT-PD-015) | Max length của `ly_do_tu_choi` UC79? | SRS chỉ ≥ 10 (BR-FLOW-04), không cap upper |
| SPEC-CLARIFY-CT-08 | 06 (TC-CT-TT-009) | so_tien_thuc_tra = 0 cho phép khi so_tien_duoc_duyet=0 (EC-01)? | Conflict UI rule "> 0" (srs-fr-06:997) vs EC-01 |
| SPEC-CLARIFY-CT-09 | 06 (TC-CT-TT-010) | ngay_thanh_toan ≥ ngay_phe_duyet bắt buộc? | SRS không nêu |
| SPEC-CLARIFY-CT-10 | 06 (TC-CT-TT-011) | so_bien_nhan UNIQUE? | SRS không nêu unique constraint |
| SPEC-CLARIFY-CT-11 | 07 (TC-CT-BS-007) | Tổng dung lượng upload bổ sung có cap? | SRS chỉ 10MB/file (srs-fr-06:855) |
| SPEC-CLARIFY-CT-12 | 07 (TC-CT-BS-008) | ERR-CT-BS-03 boundary 5 ngày LV inclusive/exclusive? | SRS srs-fr-06:849 chỉ nói "≤ 5 ngày LV" — chưa rõ cận trên |

---

## Categories edge cases applied

| Category | Số TC | Notes |
|----------|-------|-------|
| Boundary value | 9 | Trần năm boundary (1đ, hết trần), 5 ngày LV, 10MB exact, 20 ký tự lý do |
| State machine race | 3 | Concurrent tiếp nhận / duyệt → optimistic locking |
| Security (XSS / IDOR / Session) | 6 | XSS sanitize ghi chú/lý do/nhận xét, IDOR URL param, session timeout, force POST cross-tenant |
| Multi-loop / Re-submit | 4 | YCBS → DANG_KIEM_TRA, thẩm định re-edit, PD trả về 3 lần, kiểm tra lần 2 sau bổ sung |
| Aggregate / Cross-record | 2 | Multi-HS trong năm aggregate "đã chi trả", reset 01/01 |
| Field validation | 8 | Phí âm, text vào number, max length, file định dạng, file tên Unicode |
| Empty / Negative state | 3 | TVV chưa có TB, > 100 TB pagination, range ngày đảo |
| API side-effect | 4 | LGSP idempotent ERR-CT-02, retry 3 lần fail → cảnh báo CB NV |

---

## Coverage cải thiện sau A4

- BR-EC-01 Optimistic Locking: covered (file 01 race tiếp nhận, file 05 race duyệt)
- BR-EC-13 XSS sanitize: covered ở 4 file (02, 03, 04, 05)
- EC-01..EC-05 (Edge cases SRS srs-fr-06:422-431): covered đầy đủ
- BR-AUTH-05 cùng cấp force xuyên cấp: covered (file 10 TC-CT-PERM-017)
- BR-AUTH-08 IDOR + DN scope: covered (file 10 TC-CT-PERM-016/018)
- BR-RETRY-01 LGSP: covered (file 09 TC-CT-API-006)
- ma_ho_so_dvc UNIQUE idempotent: covered (file 09 TC-CT-API-005)
