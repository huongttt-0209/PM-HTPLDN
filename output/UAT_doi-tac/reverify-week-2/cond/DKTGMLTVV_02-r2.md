# Bảng đối chiếu điều kiện — DKTGMLTVV_02 (verify phản ánh vòng 2)

**Claim vòng 2 của đối tác:** Nhóm 1 — Thông tin cá nhân ứng viên của form Thêm mới Tư vấn viên **thiếu trường "Đơn vị quản lý"**.

**Evidence:** `DKTGMLTVV_02_v2.jpg` (ảnh tĩnh 1 khung hình) — `htpldn-uat.ospgroup.vn/chuyen-gia-tvv/tao-moi`,
breadcrumb "Trang chủ / Mạng lưới Tư vấn viên / Thêm mới", header hiện **"BTP · DP · hương 3 NHT · NHT"**,
nhóm "Thông tin cá nhân" đang mở, vùng nhìn thấy dừng ở trường **"Giới tính"**.

| Điều kiện có thể đổi kết quả | Đối tác (từ evidence, full-res) | Mình test | GAP? |
|---|---|---|:-:|
| Vai trò / tài khoản | Người hỗ trợ pháp lý (**NHT**), badge đơn vị **"BTP · DP"** — đọc ở góc phải header ảnh | Kiểm bằng **2 tài khoản NHT**: `nht_qa_tw` (badge "BTP · TW", Cục Bổ trợ tư pháp) và `nht_qa_01` (badge **"BTP · DP"** — trùng khít badge đối tác, Sở Tư pháp An Giang) | Không |
| Màn hình + chế độ | Form **Thêm mới** Tư vấn viên, đường dẫn `/chuyen-gia-tvv/tao-moi`, breadcrumb dừng ở "Thêm mới" | Cùng đường dẫn `/chuyen-gia-tvv/tao-moi`, cùng breadcrumb "Trang chủ / Mạng lưới Tư vấn viên / Thêm mới" | Không |
| Nhóm đang xét | Nhóm thu gọn "Thông tin cá nhân" — đang MỞ | Cùng nhóm "Thông tin cá nhân" — đang mở (đã chủ động mở hết 6 nhóm để liệt kê đủ trường) | Không |
| Trạng thái form | Form trống, chưa nhập gì (mọi ô còn placeholder) | Form trống, chưa nhập gì | Không |
| Phạm vi quan sát trong nhóm 1 | Ảnh chỉ chụp 1 khung hình, vùng nhìn dừng ở "Giới tính" — **chưa tới cuối nhóm 1** | Đã cuộn hết nhóm 1 và liệt kê **toàn bộ 12 nhãn** bằng cách đọc DOM (không phụ thuộc vùng nhìn) | Không |

**Kết luận:** 0 GAP — cùng vai trò NHT, cùng badge đơn vị "BTP · DP", cùng đường dẫn/màn/nhóm, cùng trạng thái form trống; và phạm vi quan sát của mình rộng hơn (đọc toàn bộ nhãn trong nhóm 1 thay vì 1 khung hình).

Đối chiếu SRS vs thực tế web + toàn bộ phép đo: xem [`../reverify-audit/DKTGMLTVV_02/audit.md`](../reverify-audit/DKTGMLTVV_02/audit.md).
