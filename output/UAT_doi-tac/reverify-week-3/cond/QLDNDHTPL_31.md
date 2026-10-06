# Bảng đối chiếu điều kiện — QLDNDHTPL_31 (Nút Sửa tại màn xem chi tiết)

| Điều kiện | Đối tác (evidence QLDNDHTPL_31.jpg) | Mình test | GAP? |
|---|---|---|---|
| Vai trò / tài khoản | CB Nghiệp vụ (CB_NV) | CB_NV_TW (cbnv_tw / Test@1234) | Không |
| Chế độ màn (mở qua action Xem) | Mở qua nút "Xem" → màn Chi tiết DN | Mở qua nút "Xem" → URL /doanh-nghiep/5eed0010-...001, tab Thông tin | Không |
| Dữ liệu tiền đề (DN tồn tại) | DN tồn tại | DN-SEED-0001 "Công ty TNHH Seed Publishable" (MST 0100000001) | Không |

**Kết luận:** 0 GAP. Cùng vai trò CB_NV, cùng vào qua nút "Xem", cùng tiền đề DN tồn tại. Cả 2 build đều mở màn Chi tiết ở chế độ chỉnh sửa (2 nút Hủy/Lưu), không có nút "Sửa" và không có chế độ chỉ đọc. Cùng gốc lỗi BUG-QLDNDHTPL_21.
