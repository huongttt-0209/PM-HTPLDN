# Re-verify vòng 2 — QLDMTCTV_OOS_03 (dòng 329, tab `UAT_TGPL Doanh Nghiệp-tuần 3`)

**Ngày:** 2026-08-04 · **Môi trường:** https://htpldn-uat.ospgroup.vn (bản dựng UAT mới)
**Bản dựng đo được:** `assets/index-DpIXRGaI.js` · nhãn sidebar `HTPLDN · V1.0.5`
**Tài khoản:** `cbnv_tw` / `Test@1234` (`CB_NV_TW`) · `cbpd_tw` / `Test@1234` (`CB_PD_TW`) — cùng đơn vị `Cục Bổ trợ tư pháp – Bộ Tư pháp`
**Verdict:** ✅ Pass

---

## Nhật ký đo

### 13:19 — Nhóm lệnh "..." trên dòng "Đang hoạt động"
Cuộn ngang tới cột "Hành động": mỗi dòng có **3 biểu tượng — mắt (Xem), bút chì (Sửa), và ba chấm ⋮**.
Bấm ⋮ ở dòng TC-BTP-TW-0001 → menu bung ra với:
- **"Cập nhật trạng thái"** (có mũi tên ›, là mục có menu con)
- **"Xóa"** (chữ đỏ)

*Lưu ý kỹ thuật khi đo:* mục "Cập nhật trạng thái" không phải `.ant-dropdown-menu-item` mà là `.ant-dropdown-menu-submenu-title`; lần truy vấn đầu bỏ sót mục này, phải chụp ảnh mới phát hiện, sau đó truy vấn lại cho đủ.
Ảnh: `image/QLDMTCTV_OOS_03-v2-01-nhom-lenh-3-cham-dong-dang-hoat-dong.png` (đã mở đọc).

⇒ **Triệu chứng gốc "không có nhóm lệnh '...' nào" KHÔNG còn tái hiện.**

### 13:20 — Menu con của "Cập nhật trạng thái"
Rê chuột vào mục → bung menu con: **"Tạm dừng"** và **"Vô hiệu hóa"** (đỏ) — khớp bộ trạng thái mà đặc tả cho phép Cán bộ Nghiệp vụ đổi.
Ảnh: `image/QLDMTCTV_OOS_03-v2-02-submenu-cap-nhat-trang-thai-tam-dung-vo-hieu-hoa.png` (đã mở đọc).

### 13:21 — Bấm thật "Tạm dừng"
- Đường dẫn trước: `/chuyen-gia-tvv/to-chuc` → sau: `/chuyen-gia-tvv/to-chuc/beb25e6f-…` (trang nền chuyển sang màn Chi tiết).
- **Hộp thoại xác nhận MỞ RA NGAY**: **"Xác nhận tạm dừng — Vui lòng nhập lý do (≥ 10 ký tự)"** + ô nhập + nút **Hủy** / **Đồng ý**.
- 0 request, 0 thông báo (chưa xác nhận).
Ảnh: `image/QLDMTCTV_OOS_03-v2-03-bam-tam-dung-mo-hop-thoai-xac-nhan.png` (đã mở đọc: màn Chi tiết "Công ty Luật TNHH Alpha Hà Nội" ở nền, hộp thoại "Xác nhận tạm dừng" ở giữa).
Bấm **Hủy** → không đổi dữ liệu. (Sau khi hủy, người dùng đứng ở màn Chi tiết chứ không quay lại danh sách — xem mục Ghi chú.)

### 13:25–13:35 — Dựng tiền đề cho lệnh "Trình phê duyệt"
Thẻ "Mới đăng ký" đang rỗng nên không có dòng nào để soi lệnh này ⇒ **tự tạo** tổ chức mới qua màn "+ Thêm mới":
`Cong ty Luat QA Reverify V2 04-08` · Công ty Luật · người đại diện `Nguyen Van Reverify V2` · Giấy ĐKHĐ `DKHD-QA-V2-0804` (01/01/2025) · lĩnh vực `Doanh nghiệp` · địa chỉ Hà Nội → sinh **TC-BTP-TW-0010**, trạng thái `MOI_DANG_KY`.

### 13:36 — Nhóm lệnh "..." trên dòng "Mới đăng ký"
Bấm ⋮ ở TC-BTP-TW-0010 → menu có **"Trình phê duyệt"** + **"Xóa"**.
Ảnh: `image/QLDMTCTV_OOS_03-v2-04-nhom-lenh-3-cham-dong-moi-dang-ky-co-trinh-phe-duyet.png` (đã mở đọc).

### 13:37 — Bấm thật "Trình phê duyệt" và CHẠY TRỌN (phép thử quyết định)
- Bấm mục → hộp thoại **"Xác nhận trình phê duyệt — Bạn đang trình hồ sơ Cong ty Luat QA Reverify V2 04-08 lên Cán bộ Phê duyệt"** + nút Hủy / **Trình duyệt**.
- Bấm **Trình duyệt** → **1 request** `POST /api/v1/to-chuc-tu-vans/ee8cbdc6-…/trinh-phe-duyet` · **1 thông báo** "Đã trình phê duyệt".
- Kiểm chứng bằng API: bản ghi chuyển `trangThai: MOI_DANG_KY → CHO_PHE_DUYET`, có `nguoiGuiDuyetId` + `ngayGuiDuyet = 2026-08-04T06:19:15Z`.
Ảnh: `image/QLDMTCTV_OOS_03-v2-05-trinh-phe-duyet-tu-danh-sach-thanh-cong.png` (đã mở đọc: màn Chi tiết TC-BTP-TW-0010 mang nhãn trạng thái vàng **"Chờ phê duyệt"**).

⇒ Lệnh **"Trình phê duyệt" khởi động từ danh sách chạy được trọn vẹn** — đúng điều đối tác nói là không làm được.

### 13:48 — Các lệnh của vai trò Cán bộ Phê duyệt
Đăng xuất sạch, đăng nhập `cbpd_tw`, mở thẻ "Chờ phê duyệt" (3 dòng).
- Bấm ⋮ ở TC-BTP-TW-0010 → menu có **"Phê duyệt"** + **"Từ chối"** (đỏ). Không có "Cập nhật trạng thái"/"Trình phê duyệt" — đúng phân quyền theo vai trò.
Ảnh: `image/QLDMTCTV_OOS_03-v2-06-cbpd_tw-nhom-lenh-co-phe-duyet-tu-choi.png` (đã mở đọc).
- Bấm thật **"Phê duyệt"** → hộp thoại **"Xác nhận phê duyệt và công bố — Vui lòng nhập Số quyết định công bố"** + nút Hủy / Phê duyệt. Bấm **Hủy** (không đổi dữ liệu, giữ hồ sơ cho các phiếu khác).

### Bảng tổng hợp nhóm lệnh "..." đo được

| Trạng thái dòng | Vai trò | Lệnh trong "..." | Bấm vào thì ra gì |
|---|---|---|---|
| Đang hoạt động | cbnv_tw | Cập nhật trạng thái (› Tạm dừng · Vô hiệu hóa) · Xóa | hộp thoại "Xác nhận tạm dừng" (có ô nhập lý do) |
| Mới đăng ký | cbnv_tw | Trình phê duyệt · Xóa | hộp thoại "Xác nhận trình phê duyệt" → chạy trọn, đổi trạng thái thật |
| Chờ phê duyệt | cbpd_tw | Phê duyệt · Từ chối | hộp thoại "Xác nhận phê duyệt và công bố" |

### Đối chiếu đặc tả
`srs-v3.5/srs-fr-04-chuyen-gia-tvv.md` dòng 1646 — cột Hành động gồm 2 icon (Xem, Sửa) + dropdown "..." chứa "Trình phê duyệt" / "Phê duyệt" / "Từ chối" / "Cập nhật trạng thái" / "Xóa", mỗi mục hiện theo đúng vai trò và trạng thái dòng, `Click → tương ứng (mỗi mục mở modal MD-* tương ứng)`.

### Ghi chú (ngoài phạm vi triệu chứng đối tác nêu)
Khi bấm một mục trong nhóm "...", trang nền chuyển sang màn **Chi tiết** của tổ chức (`/chuyen-gia-tvv/to-chuc/{id}`) rồi hộp thoại mới hiện lên. Người dùng không phải tự đi tìm nút nào nữa (điều đối tác than phiền đã hết), nhưng nếu bấm Hủy thì đứng lại ở màn Chi tiết thay vì quay về danh sách. Đây là điểm tiện dụng nhỏ, không chặn thao tác.

### Kết luận
Nhóm lệnh "..." đã có, đủ các mục theo vai trò + trạng thái, và mỗi mục đều đưa ra bước xác nhận tương ứng; đã chạy trọn "Trình phê duyệt" từ danh sách ⇒ **Pass**.
