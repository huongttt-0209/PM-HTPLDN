# Bảng đối chiếu điều kiện — TPDBC_01 (dòng 316) — Trình phê duyệt báo cáo đánh giá có gửi thông báo cho CB phê duyệt

**Kết luận:** Pass — trình phê duyệt báo cáo thì cán bộ phê duyệt cùng đơn vị nhận được thông báo ngay, đúng giây bấm.

| Điều kiện có thể đổi kết quả | Bug gốc (vòng 1 / phiếu đối tác) | Mình đo lại (04/08/2026 14:27, bản dựng index-DpIXRGaI.js · V1.0.5) | GAP? |
|---|---|---|:-:|
| Vai trò người thao tác | Cán bộ nghiệp vụ trình lãnh đạo phê duyệt | `cb_nv_tw_10` — Cán bộ Nghiệp vụ Trung ương, cùng đơn vị Cục Bổ trợ tư pháp với đợt đánh giá | Không |
| Vai trò người nhận | Cán bộ phê duyệt **cùng đơn vị** | `cbpd_tw` — Cán bộ PD Trung ương (`CB_PD_TW`), cùng đơn vị Trung ương | Không |
| Entity + trạng thái | Đợt đánh giá ở trạng thái "Báo cáo" | `DG-20260526-0003`, trạng thái "Lập báo cáo" (bước 7), đơn vị `...8000-000000000001` | Không |
| Dữ liệu tiền đề | Báo cáo đã được lưu | Báo cáo `BCDG-20260730-0002` đã lưu sẵn trong tab "Báo cáo" (có số liệu tổng hợp, điểm trung bình 7.5, biểu đồ) | Không |
| Thao tác | Mở Chi tiết → tab Báo cáo → "Trình phê duyệt báo cáo" | Đúng như vậy; hộp xác nhận "Trình phê duyệt báo cáo? Báo cáo sẽ được gửi cho cán bộ phê duyệt." → bấm "Trình phê duyệt" | Không |

**Bằng chứng:**
- `image/TPDBC_01-v2-01-trinh-phe-duyet-doi-trangthai-cho-phe-duyet.png` — đợt đánh giá sau thao tác.
- `image/TPDBC_01-v2-02-canbo-phe-duyet-nhan-thongbao.png` — mở chuông bằng chính tài khoản `Cán bộ PD Trung ương · CB_PD_TW`: mục "Báo cáo đánh giá chờ phê duyệt - DG-20…" / "Có báo cáo đánh giá vừa được trình lên chờ phê duyệt: - Mã …", vài giây trước.
- Đếm hộp thông báo trước/sau: trước 96 mục (mục trên cùng liên quan là CTĐT ngày 04/08 10:47) → sau 98 mục, mục mới `Báo cáo đánh giá chờ phê duyệt - DG-20260526-0003` ghi nhận `07:27:34Z`, trùng đúng giây với thời điểm bấm `07:27:34.033Z`.
- Trạng thái đợt chuyển `BAO_CAO` → `CHO_PHE_DUYET` (version 12 → 13). 1 request `POST .../bao-cao/submit`, 1 khung thông báo "Đã trình phê duyệt".

**⚠️ Lưu ý cách dựng tiền đề:** báo cáo của đợt này đang mang trạng thái "Bị từ chối" từ lần trình trước, nên lần đo này là **trình lại sau khi bị từ chối**. Cùng một nút, cùng một luồng gửi thông báo; nhưng nếu cần chặt hơn thì nên lặp lại trên một báo cáo chưa từng trình.
