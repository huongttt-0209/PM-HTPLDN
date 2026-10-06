# Bảng đối chiếu điều kiện — PDBCDG_04

Loại bug: **Từ chối phê duyệt báo cáo đánh giá không gửi thông báo cho CB Nghiệp vụ.** Verdict phụ thuộc: (1) đúng role/state từ chối, (2) đúng người trình BC làm đối tượng nhận TB, (3) tái hiện được đúng hiện tượng đối tác báo.

| Điều kiện có thể đổi kết quả | Đối tác | Mình test | GAP? |
|---|---|---|:-:|
| Vai trò phê duyệt | CB Phê duyệt | `cbpd_hn` (CB_PD_DP Hà Nội) | Không |
| Vai trò trình BC (người nhận TB) | CB Nghiệp vụ | `cbnv_hn` (CB_NV_DP Hà Nội) — `nguoiTrinhId` của BC | Không |
| Trạng thái BC trước từ chối | CHO_PHE_DUYET | BC version 2, `trangThai=CHO_PHE_DUYET` | Không |
| Hành vi từ chối tái hiện | Bấm "Từ chối" + nhập lý do | Xác nhận → toast "Đã từ chối báo cáo"; API `trangThai=TU_CHOI` (v3), `lyDoTuChoi` được set, đợt → BAO_CAO | Không |
| Đối tượng so sánh — CB NV có nhận TB kết quả từ chối + lý do? | Đối tác báo: không có TB | Mình tái hiện đúng: cbnv_hn vẫn 6 TB chưa đọc, panel không có TB nào về BC bị từ chối, API `eval_report_notifs=[]` | Không |

**Kết luận: 0 GAP điều kiện.** Tái hiện đúng hiện tượng đối tác báo: từ chối BC KHÔNG gửi TB cho CB NV — CB NV không được báo để sửa/trình lại. Vi phạm SRS FR-VI-09 Step 7 (BR-NOTIF-01, áp dụng cho cả duyệt lẫn từ chối) + Postconditions "Thông báo gửi CB NV". → **Open**.
