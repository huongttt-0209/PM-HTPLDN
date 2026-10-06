# Condition table — BUG-EM-TK-019 (R3)

| Điều kiện | Thao tác | Kỳ vọng | Thực tế | Kết quả |
|---|---|---|---|---|
| QTHT `admin`; có audit `TAI_KHOAN / UPDATE` mới từ TK-018 | Mở màn Nhật ký hệ thống trong khoảng 18–25/08/2026 | Cột Module của `TAI_KHOAN` hiển thị `Quản trị` | Hai audit cập nhật lúc 11:21:01 và 11:22:56 cùng các log đăng nhập/OTP/khóa tài khoản đều hiển thị `Quản trị` | PASS |
| Màn Nhật ký hệ thống | Chọn Module = `Quản trị`, bấm Tìm kiếm | Bộ lọc trả được log quản trị, không còn bảng `Trống` | URL có `module=QUAN_TRI`; bảng trả nhiều dòng `TAI_KHOAN`, cột Module đều là `Quản trị` | PASS |
| API ngày 25/08/2026 | Nhóm 54 dòng theo `entityType -> module` | `TAI_KHOAN` ánh xạ `QUAN_TRI`, không `null` | Có 25 dòng `TAI_KHOAN -> QUAN_TRI`, 0 dòng `TAI_KHOAN -> null`; hai log TVV mới cũng là `TU_VAN_VIEN -> CHUYEN_GIA_TVV` | PASS |
| API lọc `module=QUAN_TRI`, 18–25/08/2026 | Kiểm toàn bộ kết quả trả về | Kết quả lọc đúng module | Trả 48/48 dòng `TAI_KHOAN -> QUAN_TRI` | PASS |

**Kết luận:** PASS — module của nhật ký tài khoản đã được ánh xạ `QUAN_TRI`, hiển thị `Quản trị` và bộ lọc hoạt động.

**Evidence:** [UI lọc Module = Quản trị](../bug-report/image/bug-em-tk-019-r3-filter-quan-tri-results-2026-08-25.png) — SHA-256 `8405ee649346c81b785903572ac497d1f6861e0d8a512e04f43ce80e8ae39e42`; [audit detail API](../bug-report/image/bug-em-tk-018-r3-audit-old-new-diff-2026-08-25.png) thể hiện `module: QUAN_TRI`.
