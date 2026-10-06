# Bảng đối chiếu điều kiện — QLDN_10 (Đăng nhập bằng tài khoản Vô hiệu hóa)

Loại claim: Hiển thị thông báo (nội dung/ngôn ngữ thông báo khi đăng nhập tài khoản đã bị vô hiệu hóa) — thuộc tầng xác thực, phát sinh dựa trên **trạng thái tài khoản**, độc lập vai trò/dữ liệu nghiệp vụ.

| Điều kiện có thể đổi kết quả | Đối tác (evidence QLDN_10.webm) | Mình test (nip.io) | GAP? |
|---|---|---|---|
| Trạng thái tài khoản | Tài khoản "Vô hiệu hóa" | Đặt tài khoản về VO_HIEU_HOA qua QTHT rồi đăng nhập | Không |
| Thao tác đăng nhập | Nhập đúng thông tin tài khoản (vô hiệu) → Đăng nhập | Nhập đúng thông tin tài khoản (vô hiệu) → Đăng nhập | Không |
| Ngôn ngữ hệ thống | Giao diện tiếng Việt | Giao diện tiếng Việt (cùng hệ thống) | Không |
| Thông báo quan sát được | "Account disabled" (tiếng Anh) | "Account disabled" — trùng khớp từng chữ (toast hiển thị + phản hồi API 401) | Không |

Kết luận: 0 GAP. Thông báo quan sát được **trùng khớp từng chữ** với đối tác ("Account disabled") — bằng chứng thực nghiệm cho thấy vai trò không làm đổi kết quả (thông báo do tầng xác thực sinh theo trạng thái tài khoản, trước khi phân giải vai trò). Lỗi tái hiện trực tiếp trên env được giao.
