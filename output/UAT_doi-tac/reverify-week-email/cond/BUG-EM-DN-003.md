# Condition table — BUG-EM-DN-003 (R4)

| Điều kiện | Điều kiện gốc | Thực tế reverify 2026-08-25 | GAP |
|---|---|---|---|
| Dữ liệu kiểm | Token phải được sinh sau bản fix | Tự đăng ký mới DN `0108251437`; thư kích hoạt mới sinh lúc `2026-08-25T07:38:20.615Z` | Không |
| Kích hoạt lần đầu | Token hợp lệ kích hoạt đúng một lần | UI “Kích hoạt thành công”; tài khoản chuyển `CHO_KICH_HOAT → HOAT_DONG`, `version = 3` | Không |
| Token đã dùng | Phải nói rõ liên kết đã được sử dụng / tài khoản có thể đã kích hoạt | API 400 `ERR-REG-ACT-02`; UI “Liên kết kích hoạt đã được sử dụng” và có link đăng nhập | Không |
| Token sai đối chứng | Báo liên kết không hợp lệ | Sửa ký tự cuối token; API 400 `ERR-AUTH-VIII-22-05`; UI “Link không hợp lệ” | Không |
| Khả năng phân biệt | Hai tình huống phải có phản hồi khác nhau | Mã lỗi, tiêu đề, nội dung và hướng dẫn UI khác nhau đúng bản chất từng tình huống | Không |
| Môi trường | DEV | `https://18.143.165.120.nip.io`, UI v1.0.16 | Không |

**Kết luận:** PASS / Closed-verified. R3 dùng lại token cũ trước bản fix; R4 dùng token mới sau fix và hệ thống đã phân biệt đúng token đã dùng với token sai theo E8/E9.
