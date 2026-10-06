# Bảng đối chiếu điều kiện — QLDMLVPL_19 (row 126)

**Bug:** Xóa DM Lĩnh vực pháp lý đang được tham chiếu → đối tác báo thông báo bị lặp (2 toast).
**Verdict:** `Reject` (không tái hiện).

| Điều kiện có thể đổi kết quả | Đối tác (từ evidence full-res) | Mình test | GAP? |
|---|---|---|:-:|
| Vai trò / tài khoản | QTHT (màn Quản trị hệ thống) | QTHT (`admin`) | Không |
| Entity + trạng thái | DM Lĩnh vực PL **đang được tham chiếu** → xóa bị chặn | DM Lĩnh vực PL đang tham chiếu (Dân sự/Thương mại/Đất đai) → xóa bị chặn (ERR-DM-03) | Không |
| Dữ liệu tiền đề | 1 record có liên kết entity khác | 3 record có liên kết, DELETE trả từ chối + toast | Không |

**Kết luận:** Tái hiện đúng điều kiện đối tác (xóa record đang tham chiếu, bị từ chối). Khác biệt duy nhất là **kết quả hiển thị**: đối tác thấy 2 toast, env hiện tại chỉ 1 toast/1 request (đo 3 lần bằng `toast-capture.js`, observer=1). Lỗi "thông báo lặp" KHÔNG tái hiện → `Reject`. 0 GAP.
