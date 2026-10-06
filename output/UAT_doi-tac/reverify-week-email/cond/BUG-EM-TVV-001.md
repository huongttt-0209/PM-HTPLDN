# Condition table — BUG-EM-TVV-001 (R3)

| Điều kiện | Thao tác | Kỳ vọng | Thực tế | Kết quả |
|---|---|---|---|---|
| Đăng nhập `cbnv_tw_01`; TVV `TVV-BTP-TW-0049` (`bfbf0032-d4f0-456c-af9a-62888d795972`) ở version 11, điện thoại `0912340811` | PATCH hồ sơ, đổi điện thoại thành `0912340812` | Cập nhật thành công và sinh audit UPDATE | API trả 200, hồ sơ sang version 12; audit `761ac895-e229-479c-b895-1e1990b9c5ee` được tạo | PASS |
| Audit của lần cập nhật trên | Đọc chi tiết audit | `duLieuCu` và `duLieuMoi` đều có dữ liệu, thể hiện rõ cũ → mới | `duLieuCu.version=11`, `dienThoai=0912340811`; `duLieuMoi.version=12`, `dienThoai=0912340812`; endpoint và responseCode đúng | PASS |
| Hoàn nguyên dữ liệu kiểm thử | PATCH điện thoại từ `0912340812` về `0912340811` bằng version 12 | Dữ liệu trở lại ban đầu | API trả 200, hồ sơ sang version 13 và điện thoại đã về `0912340811` | PASS |

## Bằng chứng

- [Audit hiển thị dữ liệu cũ](../bug-report/image/bug-em-tvv-001-r3-audit-old-new-diff-2026-08-25.png) — SHA-256 `98dd8384aaba6c0a5d6257aa35305f2b0a416066ac6de44dafb2e7aa6ceac220`.
- [Audit hiển thị dữ liệu mới](../bug-report/image/bug-em-tvv-001-r3-audit-new-value-2026-08-25.png) — SHA-256 `8961087f81baeef5f274c25bf8a3082855e05958cec90ee2b859f88796d8a285`.

Kết luận R3: **PASS** — lỗi đã được sửa; audit UPDATE hồ sơ Tư vấn viên lưu đủ giá trị cũ và giá trị mới.
