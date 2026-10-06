# Audit — PDPCDG_05 (row 64) · Verdict: Open

## Cổng 1 — Evidence đối tác
- KQ mong đợi đối tác: (1) "Đã từ chối phân công"; (2) lưu lý do; (3) chuyển đợt "Chờ duyệt phân công" → "Phân công"; (4) ghi người từ chối, thời gian; (5) **Gửi thông báo kèm lý do cho Cán bộ nghiệp vụ**; (6) lưu vết thao tác.
- KQ thực tế đối tác: "Hệ thống không gửi thông báo kèm lý do cho cán bộ phê duyệt" (lưu ý: người nhận theo SRS + theo KQ mong đợi của chính đối tác là **Cán bộ nghiệp vụ**; chữ "cán bộ phê duyệt" ở ô KQ thực là ghi nhầm người nhận — bản chất bug = thiếu thông báo từ chối).

## Cổng 2 — Hiểu bug
- Test: CB PD từ chối phân công kèm lý do → verify (a) message + lý do + state → PHAN_CONG, (b) CB nghiệp vụ (người trình) có nhận thông báo kèm lý do không. Bug = thiếu (5) thông báo kèm lý do cho CB NV.

## Cổng 3 — Đối chiếu SRS vs thực tế (env 18.143, đợt DG-20260720-0002, id eaf06391-...)
| Mục | SRS | Thực tế | Kết luận |
|---|---|---|---|
| Message + lý do + state | KQ mong đợi #1/#2/#3; SRS #40 (dòng 866) từ chối → modal lý do >=10 ký tự → SET PHAN_CONG; dòng 365 (từ chối → PHAN_CONG) | [cbpd_tw] bấm "Từ chối" → modal "Lý do từ chối" → nhập lý do hợp lệ → "Xác nhận từ chối" → Toast "Đã từ chối phân công"; state Chờ duyệt PC → Phân công (PHAN_CONG) | ĐẠT |
| Gửi TB kèm lý do CB NV | Business rule "Phê duyệt/Từ chối (cả PC và BC) → gửi thông báo cho CB NV trình" (dòng 901); Postconditions "Thông báo gửi CB NV" (dòng 366) | [cbnv_tw] người trình. GET /api/v1/thong-baos (pageSize=30): 30 TB ngày 07-20 đều "Tài khoản vừa đăng nhập ở nơi khác"; rejectMatch (lọc "từ chối/phân công/đánh giá/DG-20260720-0002") = [] → không có TB từ chối kèm lý do. Reject ~13:44, danh sách quanh mốc đó không có entry đánh giá | **THIẾU** |

- Evidence: `action-log.txt`.

## Verdict: Open
- Message + lưu lý do + chuyển trạng thái (→ Phân công) đạt, nhưng thiếu bước SRS-mandated "gửi thông báo (kèm lý do) cho CB NV trình" (dòng 901/366) — CB nghiệp vụ không nhận thông báo từ chối để biết cần điều chỉnh. Khớp bản chất báo cáo đối tác.
- Mã lỗi nội bộ: BUG-PDPCDG_05.
