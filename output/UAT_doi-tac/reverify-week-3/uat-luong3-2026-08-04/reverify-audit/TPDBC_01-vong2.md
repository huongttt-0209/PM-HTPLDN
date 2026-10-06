# Nhật ký đo — TPDBC_01 (dòng 316) — vòng 2, 04/08/2026

**Bản dựng đang chạy:** `assets/index-DpIXRGaI.js` · `HTPLDN · V1.0.5`.
**Lỗi gốc cần kiểm:** trình phê duyệt báo cáo đánh giá nhưng cán bộ phê duyệt không nhận được thông báo.

| Giờ (VN) | Thao tác | Số liệu đo được |
|---|---|---|
| 14:25 | Chọn đợt đánh giá: `GET /api/v1/ke-hoach-danh-gias` | Duy nhất **1** đợt ở trạng thái `BAO_CAO`: `DG-20260526-0003`, đơn vị Trung ương, đã có báo cáo `BCDG-20260730-0002` lưu sẵn. |
| 14:25 | Xác định người nhận | Cán bộ phê duyệt cùng đơn vị Trung ương = **`cbpd_tw`**. Đếm hộp thông báo TRƯỚC: **96** mục (mục trên cùng là CTĐT 04/08 10:47, không liên quan). |
| 14:26 | Đăng nhập trình duyệt `cb_nv_tw_10`/`Secret@123` (cán bộ nghiệp vụ cùng đơn vị Cục Bổ trợ tư pháp) → Đánh giá → mở chi tiết đợt → tab "Báo cáo" | Báo cáo hiện đủ số liệu tổng hợp, điểm trung bình 7.5, biểu đồ. Có nút "Trình phê duyệt báo cáo". |
| 14:27 | Cài lại bộ bắt thông báo | `soObserverDangSong = 1`. |
| 14:27:34 | Bấm "Trình phê duyệt báo cáo" → hộp xác nhận "Báo cáo sẽ được gửi cho cán bộ phê duyệt." → "Trình phê duyệt" | `SO_REQUEST=1`: `POST .../bao-cao/submit` · `SO_KHUNG=1`, chữ "Đã trình phê duyệt" · thời điểm bấm `07:27:34.033Z`. |
| 14:27 | Đọc lại đợt đánh giá | `BAO_CAO` → `CHO_PHE_DUYET`, version 12 → 13. Ảnh `image/TPDBC_01-v2-01-trinh-phe-duyet-doi-trangthai-cho-phe-duyet.png`. |
| 14:28 | Đếm hộp thông báo SAU của `cbpd_tw` | 96 → **98**; mục mới `Báo cáo đánh giá chờ phê duyệt - DG-20260526-0003` @ `07:27:34Z` — trùng đúng giây với thời điểm bấm. |
| 14:29 | Đăng nhập trình duyệt bằng chính `cbpd_tw`, mở chuông | Ảnh `image/TPDBC_01-v2-02-canbo-phe-duyet-nhan-thongbao.png`: "Cán bộ PD Trung ương · CB_PD_TW"; mục "Báo cáo đánh giá chờ phê duyệt - DG-20…" / "Có báo cáo đánh giá vừa được trình lên chờ phê duyệt: - Mã …", vài giây trước. |

**Điểm cần nói thẳng về cách dựng tiền đề:** báo cáo `BCDG-20260730-0002` đang mang trạng thái "Bị từ chối" từ lần trình trước, nên phép đo này là **trình lại sau khi bị từ chối** chứ không phải trình lần đầu. Cùng một nút và cùng một luồng gửi thông báo, nên đủ để kết luận lỗi gốc đã hết; nhưng nếu muốn chặt hơn thì nên lặp lại trên một báo cáo chưa từng trình.

**Phát hiện thêm:** khung thông báo nổi ghi "Đã trình phê duyệt", phiếu ghi "Đã trình phê duyệt báo cáo" — lệch chữ, không phải triệu chứng gốc.

**Kết luận: Pass.**
