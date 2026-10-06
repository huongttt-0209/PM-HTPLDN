# Audit — PDPCDG_01 (row 63) · Verdict: Open

## Cổng 1 — Evidence đối tác
- KQ mong đợi đối tác: (1) "Đã phê duyệt phân công"; (2) chuyển đợt "Chờ duyệt phân công" → "Thực hiện"; (3) ghi người duyệt, thời gian; (4) **Gửi thông báo cho Cán bộ nghiệp vụ**.
- KQ thực tế đối tác: "Cán bộ nghiệp vụ không nhận được thông báo".

## Cổng 2 — Hiểu bug
- Test: CB PD phê duyệt phân công → verify (a) message + state → THUC_HIEN, (b) CB nghiệp vụ (người trình) có nhận thông báo không. Bug đối tác báo = thiếu (4) thông báo cho CB NV.

## Cổng 3 — Đối chiếu SRS vs thực tế (env 18.143, đợt DG-20260720-0002, id eaf06391-...)
| Mục | SRS | Thực tế | Kết luận |
|---|---|---|---|
| Message + state | KQ mong đợi #1/#2; SRS dòng 347/364/1143 (duyệt → THUC_HIEN) | [cbpd_tw] bấm "Phê duyệt" → confirm "Phê duyệt phân công?" → Toast "Đã phê duyệt phân công"; state Chờ duyệt PC → Thực hiện (CHO_DUYET_PC → THUC_HIEN) | ĐẠT |
| Gửi TB CB NV | FR-VI-04: Postconditions "Thông báo gửi CB NV" (dòng 366); main-flow bước 7 "Gửi thông báo CB NV trình" (dòng 349); business rule "Phê duyệt/Từ chối (cả PC và BC) → gửi thông báo cho CB NV trình" (dòng 901) | [cbnv_tw] donViId 00000000-...-0001 (người trình). GET /api/v1/thong-baos: meta.total=177; 30 TB ngày 07-20 đều là "Tài khoản vừa đăng nhập ở nơi khác" (do QA switch account). Lọc bỏ login: 7 TB non-login, mới nhất 2026-07-16 (khóa học), KHÔNG có TB phê duyệt/phân công đánh giá nào (approveMatch=[]) | **THIẾU** |

- Evidence: `action-log.txt`.

## Verdict: Open
- Message + chuyển trạng thái (→ Thực hiện) đạt, nhưng thiếu bước SRS-mandated "Thông báo gửi CB NV" (dòng 366/349/901) — CB nghiệp vụ (người trình) không nhận thông báo phân công đã duyệt. Khớp báo cáo đối tác.
- Mã lỗi nội bộ: BUG-PDPCDG_01.
