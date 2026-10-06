# Bảng đối chiếu điều kiện — verify KTDGKQHT_08 (row 6)

Đối tác phản ánh: mở tab "Kết quả kiểm tra" của khóa học để nhập điểm không hợp lệ, nhưng hệ thống
KHÔNG hiển thị danh sách học viên dù khóa đã có học viên → không nhập được điểm để test rule 0-10.
Evidence video KTDGKQHT_08.webm: role CB_NV_TW, khóa học ở "Đang diễn ra" (stepper bước 4), tab
"Kết quả" hiện "Chưa có dữ liệu kết quả", nút "Lưu kết quả" bị khóa.

Verify 2026-07-16 (cbnv_tw / CB_NV_TW): mở tab "Kết quả" của nhiều khóa ở các trạng thái + dữ liệu
khác nhau để tìm điều kiện danh sách hiện.

| Điều kiện | Đối tác (vòng 1, từ evidence) | Mình test | GAP? |
|---|---|---|---|
| Vai trò/tài khoản | CB Nghiệp vụ Trung ương (CB_NV_TW) | CB Nghiệp vụ Trung ương `cbnv_tw` (CB_NV_TW) | Không |
| Trạng thái khóa học | "Đang diễn ra" (video) — precondition TC cho phép cả "Đã kết thúc" | Kiểm cả "Đang diễn ra" (khóa ddd-011) lẫn "Đã kết thúc" (khóa 5eed0002) — bao trùm 2 state đối tác nêu | Không |
| Dữ liệu tiền đề: học viên đăng ký | Khóa có học viên ("tồn tại dữ liệu") | Khóa 5eed0002 "Đã kết thúc" có 8 học viên đăng ký (xác nhận qua tab Học viên + API dang-ky) | Không |
| Dữ liệu tiền đề: điểm danh / bản ghi kết quả | Không có (đối tác chỉ có học viên, tab Kết quả trống) | 5eed0002 chưa điểm danh → tab Kết quả trống, "Lưu" khóa. Đối chiếu khóa "Hoàn thành" (aaaa-001) đã điểm danh → tab hiện đủ học viên + ô Điểm kiểm tra giới hạn 0–10 | Không |
