# Bảng đối chiếu điều kiện — QLDNDHTPL_21 (Xem chi tiết DN cho phép sửa)

| Điều kiện | Đối tác (evidence QLDNDHTPL_21.jpg) | Mình test | GAP? |
|---|---|---|---|
| Vai trò / tài khoản | CB Nghiệp vụ Trung ương (CB_NV_TW) — góc phải ảnh ghi "Cán bộ NV Trung ương CB_NV_TW" | CB_NV_TW (cbnv_tw / Test@1234) | Không |
| Chế độ màn (mở qua action Xem) | Mở qua nút "Xem" → URL /doanh-nghiep/7e1f0136-... (breadcrumb "Chi tiết"), tab Thông tin | Mở qua icon "Xem" (eye) trong danh sách → URL /doanh-nghiep/5eed0010-...001 (breadcrumb "Chi tiết"), tab Thông tin | Không |
| Dữ liệu tiền đề (DN tồn tại) | DN-HNI-0006 "Công ty TRIM Test" (MST 9988776601) | DN-SEED-0001 "Công ty TNHH Seed Publishable" (MST 0100000001) | Không |

**Kết luận:** 0 GAP. Cùng vai trò CB_NV_TW, cùng vào qua action "Xem" (URL /doanh-nghiep/:id không có /sua), cùng tiền đề DN tồn tại. Đối tác build ospgroup 11/07; mình build nip.io — cả hai đều render màn Xem ở chế độ chỉnh sửa.
