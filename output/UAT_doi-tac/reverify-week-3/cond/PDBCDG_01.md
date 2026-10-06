# Bảng đối chiếu điều kiện — PDBCDG_01

Loại bug: **Phê duyệt (đồng ý) báo cáo đánh giá không gửi thông báo cho CB Nghiệp vụ; toast/thông báo thiếu nội dung "Đợt đánh giá hoàn thành".** Verdict phụ thuộc: (1) đúng role/state phê duyệt, (2) đúng người trình BC làm đối tượng nhận TB, (3) tái hiện được đúng hiện tượng đối tác báo.

| Điều kiện có thể đổi kết quả | Đối tác | Mình test | GAP? |
|---|---|---|:-:|
| Vai trò phê duyệt | CB Phê duyệt | `cbpd_hn` (CB_PD_DP Hà Nội) | Không |
| Vai trò trình BC (người nhận TB) | CB Nghiệp vụ | `cbnv_hn` (CB_NV_DP Hà Nội) — `nguoiTrinhId` của BC | Không |
| Trạng thái BC trước duyệt | CHO_PHE_DUYET | BC version 3, `trangThai=CHO_PHE_DUYET` (đã trình lại sau lần từ chối) | Không |
| Hành vi duyệt tái hiện | Bấm "Phê duyệt" | Xác nhận → toast "Đã phê duyệt báo cáo"; API `trangThai=DA_DUYET`, `ngayDuyet=2026-07-20T13:03:46`, đợt → HOAN_THANH | Không |
| Đối tượng so sánh — CB NV có nhận TB kết quả duyệt? | Đối tác báo: không có TB | Mình tái hiện đúng: cbnv_hn vẫn 6 TB chưa đọc, panel không có TB nào về BC được duyệt, API `eval_report_notifs=[]` | Không |
| Đối tượng so sánh — nội dung thông báo | Kỳ vọng "Đợt đánh giá hoàn thành" | Toast "Đã phê duyệt báo cáo" — không nhắc đợt hoàn thành | Không |

**Kết luận: 0 GAP điều kiện.** Tái hiện đúng hiện tượng đối tác báo: (1) duyệt BC KHÔNG gửi TB cho CB NV — vi phạm SRS FR-VI-09 Step 7 (BR-NOTIF-01) + Postconditions "Thông báo gửi CB NV"; (2) toast/thông báo không có nội dung đợt hoàn thành như đối tác kỳ vọng. → **Open**.
