# Nhật ký đo — QLHSPLDN_06 (dòng 324) — vòng 2, 04/08/2026

**Bản dựng đang chạy:** `assets/index-DpIXRGaI.js` · nhãn sidebar `HTPLDN · V1.0.5` (tải lại trang bỏ bộ nhớ đệm lúc 14:38 rồi mới đo).
**Tài khoản:** `cb_nv_tw_01` — đọc `/api/v1/auth/me` xác nhận `vaiTro: CB_NV_TW`, `capDonVi: TW`, `donViId …8000-000000000001`, có quyền `read_ho_so_phap_ly_dn`.
**Lỗi gốc cần kiểm:** thẻ "Hồ sơ pháp lý" trong màn Chi tiết doanh nghiệp không có nút xem chi tiết.

| Giờ (VN) | Thao tác | Số liệu đo được |
|---|---|---|
| 14:39 | Chọn dữ liệu: `GET /api/v1/ho-so-phap-ly-dns?limit=100` | 20 hồ sơ — 16 "Hiệu lực", 2 "Hết hạn", 2 "Thu hồi". Chọn DN "Công ty TNHH Mẫu Test" (3 hồ sơ, 1 hồ sơ có tệp) và DN "Đại Phúc NH2" (đủ 3 trạng thái). |
| 14:39 | Menu Doanh nghiệp → nút xem chi tiết dòng DN-XX-0005 → thẻ "Hồ sơ pháp lý" | Bảng 10 cột, cột cuối "Hành động". Cả 3 dòng đều có **Xem (biểu tượng con mắt) / Sửa / Xoá**, không nút nào `disabled`. |
| 14:40 | Bấm "Xem" trên `HSPL-20260803-0001` (hồ sơ **có** tệp) | Mở cửa sổ "Chi tiết hồ sơ pháp lý" đủ 10 trường + mục "Tệp đính kèm" ghi `2K15 T3 (4.8) & CN (9.8).pdf (258.2 KB)` kèm nút Xem/Tải. Ảnh `image/QLHSPLDN_06-v2-01-…png`. |
| 14:40 | Đếm ô nhập liệu trong cửa sổ bằng mã | **0 ô** (`input, textarea, select, .ant-select, .ant-picker, [contenteditable="true"]`) → đúng chế độ chỉ đọc. Nút: Đóng + Xem/Tải tệp, không nút nào bị vô hiệu hoá. |
| 14:40 | Bấm "Xem" trên `HSPL-20260803-0002` (hồ sơ **không** tệp) | Mở bình thường, mục tệp ghi "Chưa có tệp đính kèm". |
| 14:41 | Sang DN "Đại Phúc NH2" — 3 hồ sơ ở 3 trạng thái | Hiệu lực / Hết hạn / Thu hồi — **cả 3 dòng đều có nút Xem, `disabled = false`**. Bấm Xem trên hồ sơ "Thu hồi" → mở đúng cửa sổ chi tiết. Ảnh `image/QLHSPLDN_06-v2-02-…png`. |

**Vì sao phải kiểm đủ 3 trạng thái:** nút có thể chỉ hiện với một số trạng thái hồ sơ — nếu chỉ kiểm "Hiệu lực" rồi kết luận thì có nguy cơ Pass oan. Tổng cộng đã kiểm **6 hồ sơ**.

**Kết luận: Pass.**
