# Bảng đối chiếu điều kiện — QLDMLDN_16 (row 145)

**Bug:** Xóa DM Loại doanh nghiệp đang tham chiếu → đối tác báo thông báo bị lặp (2 toast).
**Verdict:** `Reject` (không tái hiện).

| Điều kiện có thể đổi kết quả | Đối tác (ảnh full-res) | Mình test | GAP? |
|---|---|---|:-:|
| Vai trò / tài khoản | QTHT (màn Quản trị hệ thống) | QTHT (`admin`) | Không |
| Entity + trạng thái | DM Loại DN **đang được tham chiếu** → xóa bị chặn | DM Loại DN "Công ty TNHH" (TNHH) đang tham chiếu → xóa bị chặn | Không |
| Dữ liệu tiền đề | 1 record có liên kết entity khác | TNHH có liên kết, DELETE trả từ chối + toast | Không |

**Kết luận:** Tái hiện đúng điều kiện đối tác (xóa record loại DN đang tham chiếu, bị từ chối). Khác biệt duy nhất là **hiển thị**: đối tác thấy 2 toast, env hiện tại chỉ 1 toast/1 request (đo bằng `toast-capture.js`, observer=1). Lỗi "thông báo lặp" KHÔNG tái hiện → `Reject`. Cùng 1 bug gốc với QLDMLVPL_19 + QLDMLHHT_16. 0 GAP.
