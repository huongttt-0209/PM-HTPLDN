# Condition table — BUG-EM-DT-003 (R3)

| Điều kiện | Điều kiện gốc | Thực tế reverify 2026-08-25 | GAP |
|---|---|---|---|
| Khóa đủ điều kiện | Đã duyệt, đã công khai, trong thời gian diễn ra | `KH-20260803-002`, trạng thái `DA_DUYET`, công khai bật, ngày 03–31/08/2026 | Không |
| Giảng viên | Có GV không dùng kênh in-app | `GV-QA-001` — TS. Lê Hoàng Thái, email `diupt01+gv-01@gmail.com` | Không |
| Baseline MailHog | Chưa có thư khai giảng tới GV | Tổng theo người nhận = 0 | Không |
| Chuyển trạng thái | Khai giảng thành công | UI báo “Đã khai giảng khóa học”, API chuyển `DANG_DIEN_RA` | Không |
| Email giảng viên | Phải phát thư | MailHog tăng 0→1, thư đến `2026-08-25T03:39:12.960Z`, tiêu đề khóa học “đã khai giảng” | Không |
| Môi trường | DEV | `https://18.143.165.120.nip.io`, UI v1.0.16 | Không |

**Kết luận:** PASS — sự kiện khai giảng đã phát email đúng cho giảng viên.
