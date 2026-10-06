# Bảng đối chiếu điều kiện — QLDMTCTV_OOS_03 (dòng 329) — Cột "Hành động" thiếu nhóm lệnh "..."

**Kết luận:** Pass — nhóm lệnh "..." đã có trên mọi dòng, các lệnh hiện đúng theo vai trò + trạng thái, và mỗi lệnh khi bấm đều đưa ra hộp thoại xác nhận tương ứng ngay (đã chạy trọn "Trình phê duyệt" từ danh sách, hồ sơ chuyển trạng thái thật).

| Điều kiện có thể đổi kết quả | Bug gốc (vòng 1) | Mình đo lại (cbnv_tw + cbpd_tw, 04/08/2026) | GAP? |
|---|---|---|:-:|
| Vai trò / tài khoản | Cán bộ Nghiệp vụ cấp Trung ương (`cbnv_tw_04`), Cục Bổ trợ tư pháp – Bộ Tư pháp | `cbnv_tw` (`CB_NV_TW`, cùng đơn vị) cho các lệnh của Cán bộ Nghiệp vụ; `cbpd_tw` (`CB_PD_TW`, cùng đơn vị) cho các lệnh của Cán bộ Phê duyệt | Không |
| Màn hình / entity + trạng thái | Danh sách Tổ chức tư vấn, cột "Hành động" | Đúng màn `/chuyen-gia-tvv/to-chuc`, cuộn ngang tới cột "Hành động" | Không |
| Dữ liệu tiền đề | 3 tổ chức "Đang hoạt động" + 2 tổ chức "Mới đăng ký" | 8 "Đang hoạt động" · 1 "Mới đăng ký" (tự tạo vì thẻ đang rỗng) · 3 "Chờ phê duyệt" ⇒ đủ 3 nhóm trạng thái để soi từng lệnh | Không |
| Thao tác / input | Chỉ đếm và đọc các nút, tìm nhóm "..." | **Bấm thật** vào nhóm "..." ở cả 3 trạng thái, mở cả menu con, và **bấm thật vào từng lệnh** để xem có ra bước xác nhận không | Không |

**Nhóm lệnh "..." đo được (đọc từ DOM sau khi bấm mở):**

- Dòng "Đang hoạt động" (TC-BTP-TW-0001), vai trò `cbnv_tw` → **Cập nhật trạng thái** (menu con: Tạm dừng · Vô hiệu hóa) · **Xóa**.
- Dòng "Mới đăng ký" (TC-BTP-TW-0010), vai trò `cbnv_tw` → **Trình phê duyệt** · **Xóa**.
- Dòng "Chờ phê duyệt" (TC-BTP-TW-0010), vai trò `cbpd_tw` → **Phê duyệt** · **Từ chối**.

**Bấm thật từng lệnh — kết quả:**
- "Cập nhật trạng thái → Tạm dừng": mở hộp thoại **"Xác nhận tạm dừng — Vui lòng nhập lý do (≥ 10 ký tự)"** với nút Hủy / Đồng ý. (Đã bấm Hủy, không đổi dữ liệu.)
- "Trình phê duyệt": mở hộp thoại **"Xác nhận trình phê duyệt — Bạn đang trình hồ sơ … lên Cán bộ Phê duyệt"** → bấm **Trình duyệt** → `POST /api/v1/to-chuc-tu-vans/ee8cbdc6-…/trinh-phe-duyet`, thông báo "Đã trình phê duyệt", hồ sơ TC-BTP-TW-0010 chuyển từ "Mới đăng ký" sang **"Chờ phê duyệt"** ⇒ lệnh chạy được trọn vẹn khi khởi động từ danh sách.
- "Phê duyệt" (cbpd_tw): mở hộp thoại **"Xác nhận phê duyệt và công bố — Vui lòng nhập Số quyết định công bố"**. (Đã bấm Hủy.)

**Ghi chú quan sát (không phải triệu chứng đối tác nêu):** khi bấm một lệnh trong nhóm "...", trang nền chuyển sang màn Chi tiết của tổ chức đó (đường dẫn đổi thành `/chuyen-gia-tvv/to-chuc/{id}`) rồi hộp thoại xác nhận mới hiện lên. Người dùng KHÔNG phải tự tìm nút nào nữa (đúng điều đối tác than phiền đã hết), nhưng nếu bấm Hủy thì sẽ đứng ở màn Chi tiết chứ không quay lại danh sách.

**Bằng chứng:**
- `image/QLDMTCTV_OOS_03-v2-01-nhom-lenh-3-cham-dong-dang-hoat-dong.png` — dòng "Đang hoạt động": menu "..." mở ra với "Cập nhật trạng thái ›" và "Xóa" (chữ đỏ).
- `image/QLDMTCTV_OOS_03-v2-02-submenu-cap-nhat-trang-thai-tam-dung-vo-hieu-hoa.png` — menu con bung ra bên trái: "Tạm dừng" và "Vô hiệu hóa" (đỏ).
- `image/QLDMTCTV_OOS_03-v2-03-bam-tam-dung-mo-hop-thoai-xac-nhan.png` — hộp thoại "Xác nhận tạm dừng" với ô nhập lý do + nút Hủy / Đồng ý.
- `image/QLDMTCTV_OOS_03-v2-04-nhom-lenh-3-cham-dong-moi-dang-ky-co-trinh-phe-duyet.png` — dòng "Mới đăng ký" TC-BTP-TW-0010: menu "..." có "Trình phê duyệt" + "Xóa".
- `image/QLDMTCTV_OOS_03-v2-05-trinh-phe-duyet-tu-danh-sach-thanh-cong.png` — sau khi xác nhận: màn Chi tiết TC-BTP-TW-0010 mang nhãn trạng thái **"Chờ phê duyệt"**.
- `image/QLDMTCTV_OOS_03-v2-06-cbpd_tw-nhom-lenh-co-phe-duyet-tu-choi.png` — vai trò CB_PD_TW ở thẻ "Chờ phê duyệt": menu "..." có "Phê duyệt" + "Từ chối".
- Đặc tả: `srs-v3.5/srs-fr-04-chuyen-gia-tvv.md` dòng 1646 (nhóm icon + dropdown "..." chứa Trình phê duyệt / Phê duyệt / Từ chối / Cập nhật trạng thái / Xóa, mỗi mục mở modal MD-* tương ứng).
