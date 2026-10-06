# Bảng đối chiếu điều kiện — DKTGKH_12 (verify phản ánh vòng 2)

**Claim vòng 2 của đối tác:** Import Excel danh sách đăng ký → hệ thống báo "Email không hợp lệ" dù dữ liệu hợp lệ.

**Evidence:** `DKTGKH_12_v2.webm` — frame `t018.13s` (modal: Tổng 3 / Thành công 0 / Lỗi 3, "Dòng 2/3/4: Email không hợp lệ"),
frame `t024.16s` (file Excel nguồn: 3 email đúng định dạng, ô Email là ô liên kết `mailto:`).

| Điều kiện có thể đổi kết quả | Đối tác (từ evidence, full-res) | Mình test | GAP? |
|---|---|---|:-:|
| Vai trò / tài khoản | CB Nghiệp vụ - Trung ương (CB_NV_TW), đơn vị BTP·TW — đọc ở góc phải header frame t012/t018 | `cbnv_tw` / CB_NV_TW, đơn vị BTP·TW (Cục Bổ trợ tư pháp) | Không |
| Entity + trạng thái (state machine) | Khóa học ở bước **Đã duyệt** (stepper Dự thảo ✓ · Chờ duyệt ✓ · 3 Đã duyệt), nút hành động còn "Công khai"/"Khai giảng", tab Học viên đang mở | Khóa học `KH-QAW7-HOINGHI` (`a7480002-0000-4000-8000-000000000002`) ở bước **Đã duyệt**, stepper + nút "Công khai"/"Khai giảng" giống hệt, tab Học viên | Không |
| Dữ liệu tiền đề (file import) | File `dang-ky-dao-tao-template.xlsx` tải từ nút "Tải file mẫu" của hệ thống, điền 3 dòng; **ô Email là ô liên kết `mailto:`**; dòng 2 đủ Họ tên + Email + SĐT + Đơn vị, dòng 3-4 thiếu SĐT/Đơn vị | Tải lại chính file mẫu qua "Tải file mẫu" (`GET .../dang-ky-dao-taos/template`), điền đúng 3 dòng dữ liệu của đối tác, ô Email gắn hyperlink `mailto:` y hệt (`A-hyperlink-giong-doi-tac.xlsx`) | Không |
| Input / giá trị nhập | Email `linh@gmail.com`, `ngoc@gmail.com`, `nguyenvana@gmail.com` | Đúng 3 email đó | Không |

**Kết luận:** 0 GAP — tái hiện đúng vai trò, đúng trạng thái khóa học, đúng loại file và đúng giá trị nhập của đối tác.

Đối chiếu SRS vs thực tế web + toàn bộ phép đo: xem [`../reverify-audit/DKTGKH_12/audit.md`](../reverify-audit/DKTGKH_12/audit.md).
