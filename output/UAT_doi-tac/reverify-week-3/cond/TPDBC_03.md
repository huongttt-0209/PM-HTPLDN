# Bảng đối chiếu điều kiện — TPDBC_03

Loại bug: **Trình phê duyệt báo cáo khi đợt không ở trạng thái đã lập BC — đối tác báo message sai state/sai wording.** Verdict phụ thuộc: (1) đúng role, (2) đợt KHÔNG ở BAO_CAO, (3) đối chiếu message app vs SRS E1.

| Điều kiện có thể đổi kết quả | Đối tác | Mình test | GAP? |
|---|---|---|:-:|
| Vai trò trình BC | CB Nghiệp vụ | `cbnv_hn` (CB_NV_DP Hà Nội) | Không |
| Trạng thái đợt khi trình | Không ở BAO_CAO | Đợt B3 ở THUC_HIEN (chưa lập BC) | Không |
| Thao tác | Trình phê duyệt BC ở sai state | `POST /bao-cao/submit` khi đợt THUC_HIEN | Không |
| Message hệ thống trả | Đối tác báo: sai state/sai wording | App trả **404 `ERR-VAL-BC-DG-02`** "Báo cáo đánh giá không tồn tại" | Không |
| UI có chặn thao tác không | (đối tác kiểm qua UI) | UI **gate nút** — ở THUC_HIEN không có nút "Trình phê duyệt" (xác nhận ở TPDBC_02); lỗi trên chỉ xuất hiện khi gọi API trực tiếp | Không |

**Kết luận: 0 GAP điều kiện.** Hành vi **đúng**: hệ thống chặn trình BC ở sai state (404), UI ẩn nút nên user thường không chạm tới. Điểm khác biệt: message app "Báo cáo đánh giá không tồn tại" (`ERR-VAL-BC-DG-02`) khác chuỗi SRS FR-VI-08 E1 `ERR-DG-TR-01` = "Đợt không ở trạng thái đã lập BC" (L670). Ở THUC_HIEN chưa có BC nên "báo cáo không tồn tại" cũng hợp lý về mặt logic, chỉ khác cách diễn đạt (report-không-tồn-tại vs đợt-sai-state). SRS quy định wording E1 nhưng theo describe-not-prescribe QA không tự chốt buộc khớp chuỗi. → **BA confirm** (wording/framing message sai state).
