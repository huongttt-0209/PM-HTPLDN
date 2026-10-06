# Bảng đối chiếu điều kiện — DKTGMLTVV_04 (row 122, tab tuần 2)

Case: Kiểm tra hiển thị Nhóm 3 "Tổ chức & Mạng lưới" trên form Thêm mới Tư vấn viên.

| Điều kiện có thể đổi kết quả | Đối tác (từ evidence, full-res) | Mình test | GAP? |
|---|---|---|:-:|
| Vai trò / tài khoản | NHT — ảnh `DKTGMLTVV_04_v2.jpg` góc phải hiện "hương 3 NHT · NHT", đơn vị "BTP · DP" | NHT — `nht_qa_tw` (QA NHT Trung uong · NHT), đơn vị "BTP · TW". Cùng vai trò NHT, cùng là đơn vị thuộc Bộ Tư pháp; form Thêm mới TVV chỉ NHT mới mở được | Không |
| Entity + trạng thái (state machine) | Form tạo mới (chưa có bản ghi) — URL `/chuyen-gia-tvv/tao-moi`, breadcrumb "... > Thêm mới" | Form tạo mới — URL `/chuyen-gia-tvv/tao-moi`, breadcrumb "Trang chủ / Mạng lưới Tư vấn viên / Thêm mới". Vào đúng theo bước đối tác: tab "Mới đăng ký" → nút "Thêm mới" | Không |
| Dữ liệu tiền đề | Không cần bản ghi nào — form rỗng lúc mở, mọi trường nhóm 3 đều trống | Form rỗng, mọi trường nhóm 3 đều trống (placeholder còn nguyên) | Không |
| Input / filter / giá trị nhập | Dropdown "Loại" = "Tư vấn viên" (mặc định) | Đã đo CẢ HAI giá trị của "Loại": "Tư vấn viên (TVV)" và "Chuyên gia (CG)". Nhóm 3 giữ nguyên đúng 3 trường ở cả hai → phủ trọn điều kiện của đối tác | Không |

**Kết luận bảng:** 0 GAP — đã verify đúng vai trò (NHT), đúng màn hình (form tạo mới), đúng bước thao tác và phủ cả 2 giá trị dropdown "Loại". Đủ điều kiện chốt verdict.
