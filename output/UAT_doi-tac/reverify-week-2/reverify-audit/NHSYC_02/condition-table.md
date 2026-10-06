# Bảng đối chiếu điều kiện — NHSYC_02 (Hiển thị các trường trong form nhập thủ công)

| Điều kiện có thể đổi kết quả | Đối tác (từ evidence, full-res) | Mình test | GAP? |
|---|---|---|:-:|
| Vai trò / tài khoản | CB Nghiệp vụ - Trung ương (CB_NV_TW) — hiển thị góc phải video | cbnv_tw — CB Nghiệp vụ - Trung ương (CB_NV_TW) | Không |
| Entity + trạng thái | Form thêm mới hồ sơ vụ việc (chưa lưu), URL `/vu-viec/tao-moi`, tiêu đề "Thêm mới Hồ sơ Vụ việc" | Form thêm mới hồ sơ vụ việc (chưa lưu), URL `/vu-viec/tao-moi`, tiêu đề "Thêm mới Hồ sơ Vụ việc" — cùng màn | Không |
| Dữ liệu tiền đề | Form trống, chưa chọn doanh nghiệp (nhóm 1 chỉ có nút "Tìm doanh nghiệp") | Đã test cả 3 trạng thái: form trống · sau khi CHỌN doanh nghiệp có sẵn · sau khi mở luồng TẠO DN mới — nhóm 1 vẫn không sinh thêm trường nhập nào | Không |
| Input / filter | Mở form, cuộn xem 4 nhóm; mở các danh sách chọn để đếm giá trị | Mở form, liệt kê toàn bộ trường của 4 nhóm; mở từng danh sách chọn để đếm giá trị thực | Không |

**Kết luận:** 0 GAP. Đã tái hiện đúng vai trò + đúng màn + đúng trạng thái form của đối tác, và còn test thêm nhánh "chọn DN" / "tạo DN mới" để loại trừ khả năng các trường nhóm 1 chỉ hiện sau khi chọn doanh nghiệp.
