# Bảng đối chiếu điều kiện — QLDX_02 (Hộp thoại xác nhận trước khi đăng xuất)

Loại claim: Hiển thị hộp thoại (modal xác nhận khi nhấn "Đăng xuất") — luồng UI toàn cục, độc lập vai trò/dữ liệu nghiệp vụ.

| Điều kiện có thể đổi kết quả | Đối tác (evidence QLDX_02.webm) | Mình test (nip.io) | GAP? |
|---|---|---|---|
| Trạng thái phiên | Đã đăng nhập thành công | Đã đăng nhập thành công | Không |
| Thao tác | Nhấn "Đăng xuất" trong menu avatar | Nhấn "Đăng xuất" trong menu avatar | Không |
| Hộp thoại quan sát được | "Hệ thống không hiển thị hộp thoại xác nhận" | Không có modal xác nhận — hệ thống đăng xuất & chuyển về trang đăng nhập ngay; MutationObserver (Rule 8) bắt 0 modal trong suốt thao tác | Không |

Kết luận: 0 GAP. Modal xác nhận đăng xuất là hành vi UI toàn cục (không phụ thuộc vai trò). Đo bằng MutationObserver còn sống suốt thao tác → 0 modal; click "Đăng xuất" chuyển thẳng về trang đăng nhập không qua bước xác nhận. Lỗi tái hiện trực tiếp trên env được giao.
