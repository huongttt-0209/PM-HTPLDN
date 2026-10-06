# Bảng đối chiếu điều kiện — DKTGMLTVV_14 (re-verify sau dev fix, 2026-07-15)

| Điều kiện | Bug gốc (Bước tái hiện) | Mình test (re-verify 2026-07-15) | GAP? |
|---|---|---|---|
| Vai trò / tài khoản | NHT (đối tác); bug ghi kiểm chéo CB_NV_TW cho kết quả như nhau | CB_NV_TW — `cbnv_tw` (role-independent theo ghi chú bug) | Không |
| Màn hình | Form Thêm mới TVV (`/chuyen-gia-tvv/tao-moi`) | Đúng màn `/chuyen-gia-tvv/tao-moi` | Không |
| Data tiền đề | Có thay đổi chưa lưu (đã nhập các trường cá nhân) | Đã nhập 5 trường: Họ tên / CMND / Email / SĐT / Địa chỉ | Không |
| Thao tác (mốc đo) | Bấm "Hủy" → đo value tại ② (dialog vừa hiện) và ③ (sau khi chọn "Ở lại") | ② dialog hiện: 5 trường GIỮ NGUYÊN giá trị; ③ sau "Ở lại": 5 trường GIỮ NGUYÊN, ở lại `/tao-moi`, dialog đóng | Không |

Kết luận: 0 GAP. Kết quả re-verify: **Đã fix**. Bấm "Hủy" KHÔNG còn xóa trắng biểu mẫu tại thời điểm mở hộp thoại; chọn "Ở lại" giữ nguyên toàn bộ dữ liệu đã nhập và giữ người dùng ở lại trang.
