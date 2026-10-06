# Bảng đối chiếu điều kiện — DKTGMLTVV_05 (row 123, tab tuần 2)

Case: Kiểm tra hiển thị Nhóm 4 "File đính kèm" trên form Thêm mới Tư vấn viên (SCR-IV-02).

| Điều kiện có thể đổi kết quả | Đối tác (từ evidence, full-res) | Mình test | GAP? |
|---|---|---|:-:|
| Vai trò / tài khoản | NHT — ảnh `DKTGMLTVV_05_v2.jpg` góc phải hiện "hương 3 NHT · NHT", đơn vị "BTP · DP" | NHT — `nht_qa_tw` ("QA NHT Trung uong", `vaiTro:["NHT"]`, quyền `register_tu_van_vien`), đơn vị "BTP · TW". Cùng vai trò NHT; form Thêm mới TVV chỉ NHT mới mở được. Bộ tài khoản `_02` không có biến thể NHT nên giữ `nht_qa_tw` | Không |
| Entity + trạng thái (state machine) | Form tạo mới, chưa có bản ghi — URL `/chuyen-gia-tvv/tao-moi`, breadcrumb "... > Thêm mới" | Form tạo mới — URL `/chuyen-gia-tvv/tao-moi`, breadcrumb "Trang chủ / Mạng lưới Tư vấn viên / Thêm mới", vào đúng theo bước đối tác (tab "Mới đăng ký" → "Thêm mới") | Không |
| Dữ liệu tiền đề | Form rỗng lúc mở — nhóm 4 chưa đính kèm file nào (khung kéo-thả trống) | Đo ở CẢ HAI trạng thái: (a) nhóm 4 rỗng — đúng trạng thái ảnh đối tác; (b) nhóm 4 đã upload 1 PDF thật (`bang-cap-qa-test.pdf`, 620 B) để kiểm mục 5.3 "Danh sách file đã tải" chỉ render sau khi có file | Không |
| Input / filter / giá trị nhập | Ảnh đối tác bị cắt phía trên nên KHÔNG thấy ô "Loại" đang chọn giá trị nào | Đã đo CẢ HAI giá trị "Loại": "Tư vấn viên (TVV)" và "Chuyên gia (CG)". Nhóm 4 giữ nguyên đúng 1 mục ở cả hai → phủ trọn mọi khả năng của đối tác, không cần đoán | Không |

**Kết luận bảng:** 0 GAP — verify đúng vai trò (NHT), đúng màn hình (form tạo mới), đúng bước thao tác, phủ cả 2 giá trị "Loại" và cả 2 trạng thái đính kèm (rỗng / đã có file). Đủ điều kiện chốt verdict.
