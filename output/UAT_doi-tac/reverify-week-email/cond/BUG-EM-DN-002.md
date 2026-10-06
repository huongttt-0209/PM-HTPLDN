# Condition table — BUG-EM-DN-002 (R3)

| Điều kiện | Điều kiện gốc | Thực tế reverify 2026-08-25 | GAP |
|---|---|---|---|
| Trang | Form đăng ký DN công khai | `/register/doanh-nghiep`, không đăng nhập | Không |
| Control | Ô “cam kết thông tin đúng sự thật” chưa tích | Checkbox giữ nguyên chưa chọn | Không |
| Hành động | Bấm Đăng ký | Đã bấm nút Đăng ký khi form trống | Không |
| Hành vi chặn | Không cho đăng ký | Form hiển thị 13 validation lỗi, không gửi request tạo tài khoản | Không |
| Nội dung lỗi cam kết | Phải nói về cam kết thông tin đúng sự thật | “Vui lòng tích cam kết thông tin đúng sự thật để tiếp tục” | Không |
| Môi trường | DEV | `https://18.143.165.120.nip.io`, UI v1.0.16 | Không |

**Kết luận:** PASS — thông báo validation đã trỏ đúng ô cam kết và không còn nhắc tới “Điều khoản sử dụng”.
