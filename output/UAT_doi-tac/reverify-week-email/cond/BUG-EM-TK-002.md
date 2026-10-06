# Condition table — BUG-EM-TK-002 (R3)

| Điều kiện | Thao tác | Kỳ vọng | Thực tế | Kết quả |
|---|---|---|---|---|
| QTHT; tài khoản DN `9908070802` | Mở form Chỉnh sửa tài khoản | Có trường Vai trò bắt buộc | Hiển thị nhãn `* Vai trò`, combobox `required` | PASS |
| Form sửa đã mở | Mở danh sách Vai trò | Điều khiển multi-select, giữ role hiện tại | Danh sách role mở; chip `Doanh nghiep` có nút xóa; option hiện tại được đánh dấu | PASS |
| Chỉ kiểm UI | Không bấm Lưu | Không thay đổi dữ liệu | Không phát sinh request cập nhật | PASS |

**Kết luận:** PASS — trường Vai trò đã xuất hiện đúng trên form sửa tài khoản doanh nghiệp.

**Evidence:** [Form sửa và dropdown Vai trò](../bug-report/image/bug-em-tk-002-r3-edit-form-co-vai-tro-2026-08-25.png) — SHA-256 `4649d1504b09a3d10ce6bbda3cad47377afd6249a6a15fce9c56e58eb6a08399`.
