# Bảng đối chiếu điều kiện — QLDX_03 (Hộp thoại cảnh báo sắp hết phiên khi idle)

Loại claim: Hiển thị hộp thoại cảnh báo tự động khi không thao tác — phụ thuộc **thời gian idle**, độc lập vai trò/dữ liệu nghiệp vụ.

| Điều kiện có thể đổi kết quả | Đối tác (evidence QLDX_03.webm) | Mình test (nip.io) | GAP? |
|---|---|---|---|
| Trạng thái phiên | Đã đăng nhập thành công | Đã đăng nhập thành công | Không |
| Thời gian không thao tác | ~25–30 phút không thao tác | Đặt mốc "hoạt động cuối" (auth-last-activity) về 26 phút trước = tương đương không thao tác 26 phút (hệ đo idle thuần theo mốc thời gian này, không theo đồng hồ treo tường) | Không |
| Kết quả quan sát được | "Không hiển thị hộp thoại cảnh báo" (dù idle 30 phút) | Modal "Phiên đăng nhập sắp hết hạn" HIỆN, có nút "Tiếp tục đăng nhập"/"Đăng xuất" + đồng hồ đếm ngược tới auto-logout (30 phút) | Không |

Kết luận: 0 GAP. Ngưỡng cảnh báo idle 25 phút (auto-logout 30 phút) là hành vi UI toàn cục theo mốc thời gian hoạt động cuối. Mô phỏng idle 26 phút đi đúng code-path như idle thật (đọc cùng một mốc thời gian) → modal cảnh báo hiện đúng thiết kế. KHÔNG tái hiện lỗi đối tác báo (không hiện modal).
