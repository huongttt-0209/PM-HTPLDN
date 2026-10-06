# Condition table — BUG-EM-DN-001 (R3)

| Điều kiện | Điều kiện gốc | Thực tế reverify 2026-08-25 | GAP |
|---|---|---|---|
| Tài khoản | DN `0109998887` | Đăng nhập thành công tài khoản `0109998887`, vai trò Doanh nghiệp | Không |
| Màn hình | `/doanh-nghiep/me/sua` | Mở đúng “Hồ sơ doanh nghiệp — Cong ty TNHH QA UAT Kiem Thu” | Không |
| Nhóm form | 4 nhóm thông tin ban đầu | Hiển thị 5 nhóm do Ghi chú được tách thành nhóm riêng; tất cả đang mở | Không |
| Trường Fax | Phải cho DN tự sửa | Có textbox “Fax” | Không |
| Phụ nữ làm chủ | Phải cho DN tự sửa | Có switch “Doanh nghiệp do phụ nữ làm chủ” | Không |
| Số LĐ khuyết tật | Phải cho DN tự sửa | Có spinbutton “Số lao động khuyết tật” | Không |
| Tổng nguồn vốn | Phải cho DN tự sửa | Có spinbutton “Tổng nguồn vốn (VNĐ)” | Không |
| Ghi chú | Phải cho DN tự sửa | Có textarea “Ghi chú” | Không |
| Tổng trường DN edit | 14 trường | Đủ 14 control theo SRS | Không |
| Môi trường | DEV | `https://18.143.165.120.nip.io`, UI v1.0.16 | Không |

**Kết luận:** PASS — cả 5 trường từng thiếu đã xuất hiện; form có đủ 14 trường DN được quyền tự cập nhật.
