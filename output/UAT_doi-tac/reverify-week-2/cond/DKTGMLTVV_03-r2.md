# Bảng đối chiếu điều kiện — DKTGMLTVV_03 (verify phản ánh vòng 2)

**Claim vòng 2 của đối tác:** Nhóm 2 — Thông tin chuyên môn: "SRS quy định chỉ hiển thị các trường Trình độ chuyên môn, Chuyên ngành đào tạo, Số năm kinh nghiệm. Nhưng hệ thống hiển thị nhiều hơn."

**Evidence:** `DKTGMLTVV_03_v2.jpg` (ảnh tĩnh 1 khung hình) — `htpldn-uat.ospgroup.vn/chuyen-gia-tvv/tao-moi`,
breadcrumb "Trang chủ / Mạng lưới Tư vấn viên / Thêm mới", header **"BTP · DP · hương 3 NHT · NHT"**,
nhóm "Nghề nghiệp" đang mở, vùng nhìn thấy 6 trường: Trình độ học vấn · Chuyên ngành · Chức vụ · Nơi công tác · Số năm kinh nghiệm · Mô tả kinh nghiệm.

| Điều kiện có thể đổi kết quả | Đối tác (từ evidence, full-res) | Mình test | GAP? |
|---|---|---|:-:|
| Vai trò / tài khoản | Người hỗ trợ pháp lý (**NHT**), badge đơn vị **"BTP · DP"** | `nht_qa_01` — vai trò NHT, badge **"BTP · DP"** (trùng khít badge đối tác) | Không |
| Màn hình + chế độ | Form **Thêm mới** Tư vấn viên, `/chuyen-gia-tvv/tao-moi`, breadcrumb dừng ở "Thêm mới" | Cùng đường dẫn `/chuyen-gia-tvv/tao-moi`, cùng breadcrumb | Không |
| Nhóm đang xét | Nhóm thu gọn "Nghề nghiệp" — đang MỞ | Cùng nhóm "Nghề nghiệp" — đã mở toàn bộ 6 nhóm để liệt kê đủ trường | Không |
| Trạng thái form | Form trống, chưa nhập gì | Form trống, chưa nhập gì | Không |
| Phạm vi quan sát trong nhóm 2 | Ảnh 1 khung hình, dừng ở "Mô tả kinh nghiệm" — chưa hết nhóm | Đọc **toàn bộ nhãn** của nhóm 2 bằng DOM (11 trường), không phụ thuộc vùng nhìn | Không |

**Kết luận:** 0 GAP — cùng vai trò NHT, cùng badge "BTP · DP", cùng màn/nhóm/trạng thái form; phạm vi quan sát của mình rộng hơn (đọc hết nhãn thay vì 1 khung hình).

Đối chiếu SRS vs thực tế web + toàn bộ phép đo: xem [`../reverify-audit/DKTGMLTVV_03/audit.md`](../reverify-audit/DKTGMLTVV_03/audit.md).
