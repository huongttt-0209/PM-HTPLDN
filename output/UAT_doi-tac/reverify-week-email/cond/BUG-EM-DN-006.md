# Condition table — BUG-EM-DN-006 (R3)

| Điều kiện | Điều kiện gốc | Thực tế reverify 2026-08-25 | GAP |
|---|---|---|---|
| Đúng quyền/phạm vi | Cán bộ địa phương sửa DN cùng đơn vị | `cbnv_hn` (CB_NV_DP) sửa `DN-HNI-0001` | Không |
| Giá trị ban đầu | Email có dữ liệu | `diupt01+dn-contact@gmail.com`, `version = 7` | Không |
| Xác nhận thay đổi | Hiển thị email cũ → trống | Dialog hiển thị `Email: diupt01+dn-contact@gmail.com → —` | Không |
| Kết quả lưu UI | Phải báo thành công | Toast “Cập nhật doanh nghiệp thành công” | Không |
| Dữ liệu API | Email phải được gỡ thực sự | API trả `email = null`, `version = 8`, `ngayCapNhat = 2026-08-25T03:32:20.946Z` | Không |
| Sau tải lại | Ô Email vẫn phải trống | Reload không cache: textbox Email trống | Không |
| Môi trường | DEV | `https://18.143.165.120.nip.io`, UI v1.0.16 | Không |

**Kết luận:** PASS — thao tác xóa email qua UI đã gửi và lưu giá trị `null`; email cũ không còn xuất hiện sau khi tải lại.

**Dọn dữ liệu:** sau khi chụp bằng chứng, email fixture được khôi phục về `diupt01+dn-contact@gmail.com`.
