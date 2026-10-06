# Bảng đối chiếu điều kiện — QLDN_07 (Nhập mã OTP sai/hết hạn)

Loại claim: Hiển thị/thao tác (thông báo lỗi khi nhập sai mã OTP) — thuộc tầng xác thực, độc lập vai trò/dữ liệu nghiệp vụ.

| Điều kiện có thể đổi kết quả | Đối tác (evidence QLDN_07.jpg) | Mình test (nip.io) | GAP? |
|---|---|---|---|
| Vai trò / màn hình | CB Nghiệp vụ (cbn***@htpldn.gov.vn), màn "Nhập mã xác thực" | cbnv_tw (CB Nghiệp vụ TW), màn "Nhập mã xác thực" | Không |
| Input (mã OTP) | Nhập mã OTP sai hoặc hết hạn | Nhập mã OTP sai "000000", API verify-otp trả 401 | Không |

Kết luận: 0 GAP. Lỗi tái hiện trực tiếp trên env được giao (nip.io) — không phụ thuộc env đối tác.
