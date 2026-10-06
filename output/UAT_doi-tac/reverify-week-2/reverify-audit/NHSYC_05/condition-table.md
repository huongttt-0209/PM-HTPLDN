# Bảng đối chiếu điều kiện — NHSYC_05 (Giới hạn ký tự Nội dung vụ việc)

| Điều kiện có thể đổi kết quả | Đối tác (từ evidence, full-res) | Mình test | GAP? |
|---|---|---|:-:|
| Vai trò / tài khoản | CB Nghiệp vụ - Trung ương (CB_NV_TW) — hiển thị góc phải ảnh | cbnv_tw — CB Nghiệp vụ - Trung ương (CB_NV_TW) | Không |
| Entity + trạng thái | Form thêm mới hồ sơ vụ việc (chưa lưu), URL `/vu-viec/tao-moi` | Form thêm mới hồ sơ vụ việc (chưa lưu), URL `/vu-viec/tao-moi` — cùng màn | Không |
| Dữ liệu tiền đề | Trường "Nội dung yêu cầu" còn trống (bộ đếm 0/50000) | Trường "Nội dung yêu cầu" còn trống, rồi nhập nội dung dài để dò trần | Không |
| Input / giá trị nhập | Đọc bộ đếm ký tự của trường "Nội dung yêu cầu" → "0 / 50000" (đối tác tô vàng) | Đọc thuộc tính maxlength (=50000) + bộ đếm; nhập thử 10.050 ký tự (vượt trần SRS 10.000) và kiểm tra có báo lỗi không | Không |

**Kết luận:** 0 GAP — cùng vai trò, cùng màn, cùng trường. Mình test kỹ hơn đối tác: ngoài đọc bộ đếm còn nhập thật vượt ngưỡng SRS để chứng minh hệ thống không chặn.
