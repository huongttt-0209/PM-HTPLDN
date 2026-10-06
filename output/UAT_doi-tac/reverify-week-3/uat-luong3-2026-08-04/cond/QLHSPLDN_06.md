# Bảng đối chiếu điều kiện — QLHSPLDN_06 (dòng 324) — Xem chi tiết hồ sơ pháp lý doanh nghiệp

**Kết luận:** Pass — mỗi dòng hồ sơ đã có nút "Xem", bấm mở đúng cửa sổ chi tiết chỉ đọc kèm danh sách tệp đính kèm.

| Điều kiện có thể đổi kết quả | Bug gốc (vòng 1 / phiếu đối tác) | Mình đo lại (04/08/2026 14:38–14:41, bản dựng index-DpIXRGaI.js · V1.0.5) | GAP? |
|---|---|---|:-:|
| Vai trò / tài khoản | Cán bộ Nghiệp vụ Trung ương | `cb_nv_tw_01` — vai trò `CB_NV_TW`, cấp TW, đơn vị `…8000-000000000001` (Cục Bổ trợ tư pháp) — cùng vai trò + cùng cấp + cùng đơn vị với ảnh đối tác | Không |
| Màn hình / entity | Doanh nghiệp → Xem chi tiết → thẻ "Hồ sơ pháp lý" | Đúng 4 bước của phiếu: menu Doanh nghiệp → nút xem chi tiết trên dòng → thẻ "Hồ sơ pháp lý" | Không |
| Trạng thái hồ sơ (nút có thể chỉ hiện ở vài trạng thái) | Không nêu | Kiểm 6 hồ sơ đủ 3 trạng thái: "Hiệu lực" (4), "Hết hạn" (1), "Thu hồi" (1) — cả 6 đều có nút "Xem", không nút nào bị vô hiệu hoá | Không |
| Có / không có tệp đính kèm | Ảnh đối tác không rõ | Kiểm cả 2: hồ sơ có tệp (HSPL-20260803-0001) và hồ sơ không tệp (HSPL-20260803-0002, HSPL-20260507-0019) — đều mở được | Không |
| Thao tác | Nhấn "Xem" | Bấm nút "Xem" (có biểu tượng con mắt) ở cột Hành động | Không |

**Bằng chứng:**
- `image/QLHSPLDN_06-v2-01-cua-so-chi-tiet-ho-so-chi-doc-co-tep-dinh-kem.png` — cửa sổ "Chi tiết hồ sơ pháp lý" của HSPL-20260803-0001: đủ 10 trường (Mã hồ sơ, Tên hồ sơ, Loại hồ sơ, Lĩnh vực pháp lý, Nguồn, Cơ quan cấp, Ngày cấp, Ngày hết hạn, Trạng thái, Mô tả), mục "Tệp đính kèm" ghi `2K15 T3 (4.8) & CN (9.8).pdf (258.2 KB)` kèm nút Xem/Tải, nút Đóng. Nền phía sau: cả 3 dòng đều có bộ nút Xem / Sửa / Xoá.
- `image/QLHSPLDN_06-v2-02-nut-Xem-du-3-trang-thai-ho-so.png` — doanh nghiệp DN-NEW-NH2 có 3 hồ sơ ở 3 trạng thái khác nhau, cả 3 dòng đều có nút Xem; cửa sổ đang mở là hồ sơ trạng thái "Thu hồi", mục tệp ghi "Chưa có tệp đính kèm".
- Đếm ô nhập liệu trong cửa sổ chi tiết bằng mã: **0 ô** (`input, textarea, select, .ant-select, .ant-picker, [contenteditable]`) → đúng chế độ chỉ đọc. Nút trong cửa sổ: Đóng, và Xem/Tải của tệp — không nút nào bị vô hiệu hoá.
