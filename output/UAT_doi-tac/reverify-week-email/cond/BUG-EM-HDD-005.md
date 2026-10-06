# Condition table — BUG-EM-HDD-005 (R3)

| Điều kiện | Điều kiện gốc | Thực tế reverify 2026-08-25 | GAP |
|---|---|---|---|
| Giới hạn UI | Tối đa 100 ký tự | Input `#emailNguoiGui` có `maxlength = 100` | Không |
| Biên hợp lệ | Email đúng 100 ký tự được lưu | API trả HTTP 201, tạo `HD-20260825-002`, lưu nguyên 100 ký tự | Không |
| Vượt biên | Email 101 ký tự phải bị chặn | API trả HTTP 422, mã `ERR-VAL-SYS-00-01`, field `emailNguoiGui` | Không |
| Thông báo lỗi | Nêu rõ giới hạn | “Email người gửi không được vượt quá 100 ký tự” | Không |
| Không cắt âm thầm | Vượt biên không được tạo bản ghi | Request 101 ký tự không tạo hồ sơ | Không |
| Môi trường | DEV | `https://18.143.165.120.nip.io`, UI v1.0.16 | Không |

**Kết luận:** PASS — UI và API đều thực thi giới hạn 100 ký tự; biên 100 hợp lệ, 101 bị từ chối rõ ràng.
