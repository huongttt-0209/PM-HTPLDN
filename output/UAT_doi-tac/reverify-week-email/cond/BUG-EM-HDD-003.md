# Condition table — BUG-EM-HDD-003 (R3)

| Điều kiện | Điều kiện gốc | Thực tế reverify 2026-08-25 | GAP |
|---|---|---|---|
| Đúng tài khoản/đơn vị | `cbnv_bn_01`, Bộ KH&ĐT | Đăng nhập `cbnv_bn_01`, phạm vi BTP · BN | Không |
| Kiểm tra liên đơn vị | Mã phải theo sequence toàn cục, không theo danh sách nhìn thấy | Fixture hậu-fix 24/08 của Bộ KH&ĐT là `HD-20260824-005`, sau các mã `001`–`004` toàn hệ thống | Không |
| Tạo mới trực tiếp | UI tạo được hồ sơ hợp lệ | Tạo nội dung R3 qua dialog Thêm mới, lĩnh vực Lao động, kênh Trực tiếp, đơn vị Bộ KH&ĐT | Không |
| Phản hồi dịch vụ | Không còn 409 trùng mã | UI báo “Tạo hỏi đáp thành công. Mã: HD-20260825-001”; danh sách tăng từ 2→3 | Không |
| Dữ liệu sau tạo | Hồ sơ xuất hiện đúng phạm vi | Dòng `HD-20260825-001` hiển thị trong danh sách của `cbnv_bn_01` | Không |
| Môi trường | DEV | `https://18.143.165.120.nip.io`, UI v1.0.16 | Không |

**Kết luận:** PASS — mã hỏi đáp được sinh hợp lệ và cán bộ Bộ/Ngành tạo mới thành công, không còn lỗi “Bản ghi đã tồn tại”.
