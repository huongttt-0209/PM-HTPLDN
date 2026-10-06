# Bảng đối chiếu điều kiện — DKTGMLTVV_02 (re-verify sau dev fix, 2026-07-15)

| Điều kiện | Bug gốc (Bước tái hiện) | Mình test (re-verify 2026-07-15) | GAP? |
|---|---|---|---|
| Vai trò / tài khoản | NHT (đối tác) — bug xác nhận lỗi không phụ thuộc vai trò (kiểm chéo CB_NV_TW) | CB_NV_TW — `cbnv_tw` (theo ghi chú bug: kết quả trùng với NHT ⇒ role-independent) | Không |
| Màn hình | Form Thêm mới TVV (`/chuyen-gia-tvv/tao-moi`) nhóm "Thông tin cá nhân" | Đúng màn `/chuyen-gia-tvv/tao-moi` | Không |
| Thao tác (Giới tính) | Xem kiểu điều khiển + tập giá trị của "Giới tính" | Giới tính = `ant-radio-group` gồm đúng ["Nam","Nữ"], KHÔNG phải select, KHÔNG có "Khác" | Không |
| Thao tác (Ảnh chân dung) | Tải ảnh → xem có khu vực xem trước 120×160 | Tải `.png` → hiển thị khu xem trước `ant-image` render 118×160 (natural 120×160), không còn thumbnail 48×48 | Không |

Kết luận: 0 GAP. Kết quả re-verify: **Đã fix cả 2 ý** — Giới tính là radio 2 giá trị Nam/Nữ (bỏ "Khác"); Ảnh chân dung có khu vực xem trước 120×160.
