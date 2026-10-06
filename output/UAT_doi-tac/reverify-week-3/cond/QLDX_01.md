# Bảng đối chiếu điều kiện — QLDX_01 (Thông báo "Đăng xuất thành công" sau khi đăng xuất)

Loại claim: Hiển thị thông báo (toast "Đăng xuất thành công" sau thao tác đăng xuất chủ động) — luồng UI toàn cục, độc lập vai trò/dữ liệu nghiệp vụ.

| Điều kiện có thể đổi kết quả | Đối tác (evidence QLDX_01.webm) | Mình test (nip.io) | GAP? |
|---|---|---|---|
| Trạng thái phiên | Đã đăng nhập thành công | Đã đăng nhập thành công | Không |
| Thao tác đăng xuất | Nhấn "Đăng xuất" trong menu avatar | Nhấn "Đăng xuất" trong menu avatar | Không |
| Thông báo quan sát được | "Hệ thống không hiển thị thông báo" | Không có toast "Đăng xuất thành công" — bộ quan sát MutationObserver (Rule 8) bắt 0 toast phía dashboard; màn đăng nhập sau redirect không có toast | Không |

Kết luận: 0 GAP. Toast đăng xuất là hành vi UI toàn cục (không phụ thuộc vai trò). Đã đo bằng MutationObserver còn sống suốt thao tác đăng xuất (không dùng poll) → 0 toast; kiểm chứng thêm ảnh màn login sau redirect. Lỗi tái hiện trực tiếp trên env được giao.
