# Bảng đối chiếu điều kiện — verify KTDGKQHT_03 (row 5, mode verify1)

Bug đối tác: điểm danh thủ công — đối tác báo "không hiển thị bảng danh sách học viên mặc dù tồn tại
dữ liệu học viên". Evidence video KTDGKQHT_03.webm: role CB_NV_TW, khóa "Đang diễn ra", tab Lịch học có
buổi 15/02/2026 07:00-09:00; tab Điểm danh chọn ngày 15/02/2026 → "Chưa có dữ liệu điểm danh cho ngày này".

Verify 2026-07-16 (`cbnv_tw` / CB_NV_TW) trên khóa 5eed0002 "Khóa học pháp luật doanh nghiệp seed"
(**Đã kết thúc** — 1 trong 2 state TC đối tác cho phép; cùng đơn vị với cbnv_tw nên thao tác được lịch học).
Seed 2 buổi cùng ngày 20/02/2026 (sáng 08:00-11:00 + chiều 14:00-17:00) → điểm danh THẬT (ghi + lưu).

| Điều kiện | Đối tác (vòng 1, từ evidence + TC) | Mình test | GAP? |
|---|---|---|---|
| Vai trò/tài khoản | CB Nghiệp vụ (CB_NV_TW) — quyền quản lý kết quả ĐT | `cbnv_tw` (CB_NV_TW) — cùng vai trò, có quyền theo FR-III-05 PRE-01 | Không |
| Trạng thái khóa học | "Đang diễn ra" (video); TC cho phép cả "Đã kết thúc" | Khóa 5eed0002 **"Đã kết thúc"** — đúng 1 trong 2 state TC nêu. (Khóa "Đang diễn ra" sẵn có DDD-011 thuộc đơn vị khác → API lịch học chặn ERR-VAL-III-23-03, không thao tác được; nên dùng state "Đã kết thúc" cùng đơn vị) | Không |
| Dữ liệu tiền đề: có lịch học (buổi) | Khóa đã có lịch học (buổi 15/02/2026) | Seed 2 buổi cùng ngày 20/02/2026 (sáng + chiều) + kiểm cả trường hợp ngày chỉ có 1 buổi | Không |
| Dữ liệu tiền đề: học viên | "tồn tại dữ liệu học viên" (đối tác khẳng định) | Khóa có 8 đăng ký: 1 **Đã duyệt** + 6 Chờ duyệt + 1 Từ chối → bảng điểm danh hiện đúng 1 học viên "Đã duyệt" | Không |
| Input (cách chọn để điểm danh) | Chọn buổi học từ danh sách (kỳ vọng theo TC/SRS) | UI chỉ có ô "Chọn ngày điểm danh" — chọn ngày 20/02/2026 (ngày có 2 buổi); không có chỗ chọn buổi | Không |
| Thao tác lưu | Bấm Lưu → kỳ vọng "Đã lưu điểm danh" | Bấm "Lưu điểm danh" thật: ngày 1 buổi → 200 "Đã lưu điểm danh"; ngày 2 buổi → 422 ERR-BIZ-III-05-04 "cần truyền lichHocId", không lưu được | Không |
