# Phát hiện thêm — ngoài phạm vi 2 bug của round 9 (2026-07-25)

Ghi lại để báo, **không** tự mở dòng TC mới trên sheet.

---

## 1. Ô "Thư mục đích" ở màn Nhập hàng loạt cho chọn cả thư mục của đơn vị khác, chọn xong mới báo lỗi

**Màn:** Biểu mẫu → Nhập hàng loạt → bước 1 "Chọn file" → ô **Thư mục đích**.
**Tài khoản:** `cbnv_tw_04` — CB Nghiệp vụ Trung ương (Cục Bổ trợ tư pháp).

**Quan sát:**
- Danh sách xổ xuống của ô "Thư mục đích" có 13 thư mục, trong đó **3 thư mục thuộc đơn vị khác** (Bộ Kế hoạch và Đầu tư): `QA-IMPORT-R7`, `QA-IMPORT-KQ`, `BM-B6-BN-Import-20260720`.
- Chọn `QA-IMPORT-R7` → tải 4 tệp lên bước 1 **thành công bình thường** (2 tệp hợp lệ vào danh sách).
- Chỉ khi bấm **[Kiểm tra và tiếp tục]** hệ thống mới chặn, hiện 1 khung thông báo: **"Thư mục biểu mẫu không tồn tại hoặc không thuộc đơn vị"** → người dùng mất công chọn tệp và chờ tải lên rồi mới biết thư mục không dùng được.
- Làm lại với thư mục đúng đơn vị (`QA-R7-D-RONG`) thì đi tiếp bước 2/bước 3 trơn tru.

**Vì sao đáng lưu ý:** thông báo nói *"không tồn tại hoặc không thuộc đơn vị"* trong khi thư mục **có tồn tại** và **do chính hệ thống đưa vào danh sách chọn** — người dùng khó hiểu mình sai ở đâu. Hợp lý hơn là không đưa thư mục ngoài đơn vị vào danh sách chọn, hoặc báo ngay lúc chọn thư mục thay vì sau khi đã tải tệp.

**Chưa log thành bug** vì nằm ngoài phạm vi 2 case được giao. Đề nghị BA/QA quyết có mở TC riêng không.

---

## 2. Không có bất thường nào khác

Trong suốt phiên (tạo 2 biểu mẫu mới, 9 lượt sửa/lưu, 2 lượt nhập hàng loạt trọn 3 bước) không gặp lỗi tải trang, không thấy chữ tiếng Anh lọt ra, không thấy `null`/`undefined` hiển thị, không thấy thông báo hiện lặp 2 lần.
