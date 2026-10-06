# Bảng đối chiếu điều kiện — QLDN_12 (Đăng nhập bằng tài khoản Tạm khóa do QTHT)

Loại claim: Hiển thị thông báo (nội dung thông báo khi đăng nhập tài khoản bị tạm khóa) — thuộc tầng xác thực, phát sinh dựa trên **trạng thái + nguồn khóa** của tài khoản, độc lập vai trò/dữ liệu nghiệp vụ.

| Điều kiện có thể đổi kết quả | Đối tác (evidence QLDN_12.webm) | Mình test (nip.io) | GAP? |
|---|---|---|---|
| Trạng thái tài khoản | Tài khoản "Tạm khóa" | Đặt tài khoản về TAM_KHOA rồi đăng nhập | Không |
| Nguồn khóa | Do QTHT chủ động cập nhật trạng thái Tạm khóa (admin-lock) | Do QTHT chủ động khóa (không phải do đăng nhập sai 5 lần) — cùng loại khóa | Không |
| Thao tác đăng nhập | Nhập đúng thông tin tài khoản (bị khóa) → Đăng nhập | Nhập đúng thông tin tài khoản (bị khóa) → Đăng nhập | Không |
| Thông báo quan sát được | "không giống với thiết kế" (đối tác không trích chuỗi cụ thể) | "Tài khoản tạm khóa. Vui lòng thử lại sau 0 phút." (toast hiển thị + phản hồi API 401) | Không |

Kết luận: 0 GAP. Điều kiện quyết định kết quả là **trạng thái Tạm khóa + nguồn khóa (admin-lock)** — đều khớp đúng kịch bản đối tác. Thông báo do tầng xác thực sinh theo trạng thái khóa, trước khi phân giải vai trò → vai trò không làm đổi kết quả. Lỗi tái hiện trực tiếp trên env được giao.
