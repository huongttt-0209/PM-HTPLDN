# Bảng đối chiếu điều kiện — CVVDG_04

Loại bug: **Message khi không có vụ việc nào để chọn trong kỳ đánh giá — đối tác báo wording sai.** Verdict phụ thuộc: (1) đúng role/state, (2) kỳ đánh giá thực sự rỗng (0 VV hoàn thành), (3) đối chiếu chuỗi message app vs SRS.

| Điều kiện có thể đổi kết quả | Đối tác | Mình test | GAP? |
|---|---|---|:-:|
| Vai trò | CB Nghiệp vụ | `cbnv_hn` (CB_NV_DP Hà Nội) | Không |
| Trạng thái đợt | THUC_HIEN (đang chọn VV) | Đợt B3 THUC_HIEN, tab Thực hiện | Không |
| Kỳ đánh giá không có VV hoàn thành | Có (kỳ rỗng) | B3 kỳ 01/01/2024–31/03/2024, 0 VV hoàn thành trong kỳ; bảng "Đã chọn: 0/0" | Không |
| Message hiển thị khi kỳ rỗng | Đối tác kỳ vọng chuỗi khác | App hiện **"Không có vụ việc nào phù hợp"** (empty state chung của bảng) | Không |

**Kết luận: 0 GAP điều kiện.** Tái hiện đúng bối cảnh kỳ rỗng. App hiển thị empty-state chung **"Không có vụ việc nào phù hợp"**, khác chuỗi SRS FR-VI-05 E1 `WRN-DG-VV-01` = **"Không có vụ việc nào hoàn thành trong kỳ đánh giá này"** (L442) — chuỗi app vague hơn, mất thông tin "hoàn thành trong kỳ". Hành vi (xử lý kỳ rỗng, disable nút Xác nhận) đúng; chỉ khác wording. SRS có quy định chuỗi cụ thể nhưng theo nguyên tắc describe-not-prescribe QA không tự chốt buộc khớp chuỗi. → **BA confirm** (wording).
