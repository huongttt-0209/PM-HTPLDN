# Bảng đối chiếu điều kiện — QLDMLHHT_16 (row 131)

**Bug:** Xóa DM Loại hình hỗ trợ đang tham chiếu → đối tác báo thông báo bị lặp (2 toast).
**Verdict:** `Reject` (không tái hiện).

| Điều kiện có thể đổi kết quả | Đối tác (video full-res, mốc 00:04) | Mình test | GAP? |
|---|---|---|:-:|
| Vai trò / tài khoản | QTHT (màn Quản trị hệ thống) | QTHT (`admin`) | Không |
| Entity + trạng thái | DM Loại hình HT **đang được tham chiếu** → xóa bị chặn | DM Loại hình HT "Tư vấn pháp luật" (TU_VAN) đang tham chiếu → xóa bị chặn | Không |
| Dữ liệu tiền đề | 1 record có liên kết entity khác | TU_VAN có liên kết, DELETE trả từ chối + toast | Không |

**Kết luận:** Tái hiện đúng điều kiện đối tác (xóa record loại hình HT đang tham chiếu, bị từ chối). Khác biệt duy nhất là **hiển thị**: đối tác thấy 2 toast, env hiện tại chỉ 1 toast/1 request (đo bằng `toast-capture.js`, observer=1). Lỗi "thông báo lặp" KHÔNG tái hiện → `Reject`. Cùng 1 bug gốc với QLDMLVPL_19. 0 GAP.
