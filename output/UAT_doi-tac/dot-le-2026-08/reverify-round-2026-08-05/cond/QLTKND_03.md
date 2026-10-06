# Bảng đối chiếu điều kiện — QLTKND_03 (re-verify vòng 2, 05/08/2026)

Loại bug: **màu hiển thị của cột "Trạng thái" trên danh sách tài khoản**. Phạm vi còn lại theo note vòng 2 chỉ là bảng màu, nhưng để đọc được cả 4 màu phải có đủ 4 trạng thái trong dữ liệu ⇒ có tiền đề dữ liệu ⇒ điền bảng đầy đủ, 0 GAP.
Ô note của dòng này (*DEV phản hồi lần 2*) KHÔNG có khối `── CÁCH VERIFY sau Dev fix ──`, nên lấy phần **"Về ý Chờ kích hoạt chưa có màu nhấn"** (mục liệt kê 3/4 màu lệch) làm điều kiện phải hết lỗi; phần **thẻ lọc trạng thái đã đúng** là mốc đã đạt.

| Điều kiện | Bug gốc (note vòng 2) | Mình test | GAP? |
|---|---|---|---|
| Môi trường | Môi trường bàn giao, bản dựng đang chạy | `https://18.143.165.120.nip.io` — bản dựng **HTPLDN · V1.0.6** (đọc ở thanh bên trái) | Không |
| Vai trò | Vai trò vào được Quản trị hệ thống → Tài khoản & phân quyền | `cbnv_tw` KHÔNG có mục này trong menu (chỉ thấy "Cấu hình hệ thống") → dùng **`admin`** · vai trò QTHT · cấp TW, đăng nhập ở phiên trình duyệt riêng để không ảnh hưởng phiên `cbnv_tw` | Không |
| Màn hình | Quản trị hệ thống → Tài khoản & phân quyền | Quản trị hệ thống → **Tài khoản & phân quyền** (`/quan-tri/tai-khoan`) | Không |
| Vùng được quy định màu | Cột "Trạng thái" trong danh sách (không phải thẻ lọc) | Đọc đúng cột **Trạng thái** của bảng danh sách | Không |
| Tiền đề dữ liệu — Hoạt động | Cần có bản ghi trạng thái này để đọc màu | Có sẵn (55 tài khoản) | Không |
| Tiền đề dữ liệu — Chờ kích hoạt | Cần có bản ghi trạng thái này | Có sẵn (12 tài khoản) | Không |
| Tiền đề dữ liệu — Vô hiệu hóa | Cần có bản ghi trạng thái này | Có sẵn trong danh sách (xem qua bộ lọc Trạng thái) | Không |
| Tiền đề dữ liệu — Tạm khóa | Cần có bản ghi trạng thái này | Ban đầu **0 bản ghi** → đã TỰ TẠO: khóa tạm tài khoản kiểm thử `0455667700` (Pham Van State) để sinh 1 bản ghi Tạm khóa, đo màu xong đã **mở khóa trả về Hoạt động** như cũ | Không |
| Cách đo màu | Đối chiếu màu yêu cầu: vàng / đỏ / đen / xanh | Đọc màu thật của chấm trạng thái trên từng dòng (lấy giá trị màu do trình duyệt tính) + ảnh chụp màn để nhìn bằng mắt | Không |

**Kết luận: 0 GAP** — đúng bản dựng đang chạy, đúng màn hình, đúng vùng được quy định màu, có đủ cả 4 trạng thái trong dữ liệu (tự tạo phần còn thiếu rồi trả lại nguyên trạng), đo màu bằng cả số đo lẫn ảnh.

## Đo lường trực tiếp (05/08/2026, `18.143.165.120.nip.io`, bản dựng V1.0.6, tài khoản `admin`)

### Phần "còn lỗi" của note — bảng màu cột Trạng thái

- ✅ **"Chờ kích hoạt" yêu cầu VÀNG, trước đây đang xám** → nay là **vàng** (giá trị màu đo được `rgb(250, 173, 20)`).
- ✅ **"Tạm khóa" yêu cầu ĐỎ, trước đây đang vàng cam** → nay là **đỏ** (`rgb(245, 34, 45)`).
- ✅ **"Vô hiệu hóa" yêu cầu ĐEN, trước đây đang đỏ** → nay là **đen** (`rgb(0, 0, 0)`).
- ✅ **"Hoạt động" yêu cầu XANH, trước đã đúng** → vẫn **xanh lá** (`rgb(82, 196, 26)`), không hồi quy.
  Ảnh (Tạm khóa đỏ · Hoạt động xanh · Chờ kích hoạt vàng): [`../image/QLTKND_03-mau-cot-trang-thai-4-trang-thai.png`](../image/QLTKND_03-mau-cot-trang-thai-4-trang-thai.png)
  Ảnh (Vô hiệu hóa đen): [`../image/QLTKND_03-mau-trang-thai-vo-hieu-hoa-den.png`](../image/QLTKND_03-mau-trang-thai-vo-hieu-hoa-den.png)

### Phần "đã đạt" của note — kiểm lại xem có hồi quy không

- ✅ Thanh thẻ trạng thái còn đúng **4 thẻ**: Tất cả / Hoạt động / Chờ kích hoạt / Tạm khóa. Không xuất hiện lại thẻ lạ.
- ✅ Số trên thẻ khớp dữ liệu và cập nhật đúng theo thao tác: trước khi khóa tạm là Tất cả 79 · Hoạt động 55 · Chờ kích hoạt 12 · Tạm khóa (0, không hiện số); sau khi khóa tạm 1 tài khoản thành Tất cả 79 · Hoạt động 54 · Chờ kích hoạt 12 · **Tạm khóa 1**.
- ✅ Bấm từng thẻ đều lọc ra đúng bộ bản ghi tương ứng (thẻ Tạm khóa ra đúng 1 tài khoản vừa khóa).

### Ý note dặn khép lại — tôn trọng, KHÔNG chấm FAIL

- ⚠️ "Thiếu thẻ Vô hiệu hóa": note ghi rõ đặc tả chỉ quy định 4 thẻ, tài khoản vô hiệu hóa xem qua bộ lọc Trạng thái, và **"ý này xin phép khép lại"** → không dùng để chấm phiếu. Trên bản đang chạy vẫn đúng như vậy: không có thẻ Vô hiệu hóa, nhưng các tài khoản Vô hiệu hóa vẫn hiển thị trong danh sách và lọc được.

### Kết luận

Phạm vi còn lại của phiếu (bảng màu cột "Trạng thái") nay đã đúng cả 4 trạng thái; phần thẻ lọc đã đạt trước đó không hồi quy; ý được note đề nghị khép lại không tính vào chấm → **Pass**.

### Ghi nhận thêm (ngoài phạm vi phiếu — không tự thêm dòng mới vào sheet)

- Tài khoản `cbnv_tw` (Cán bộ nghiệp vụ Trung ương) KHÔNG nhìn thấy mục "Tài khoản & phân quyền" trong menu Quản trị hệ thống — chỉ thấy "Cấu hình hệ thống". Đây là phân quyền bình thường, chỉ ghi lại để đối tác biết phiếu này cần vai trò quản trị mới kiểm được.
- Dữ liệu dùng để đo: đã khóa tạm rồi mở khóa lại tài khoản kiểm thử `0455667700`; trạng thái cuối cùng đã trả về **Hoạt động** đúng như trước khi đo, không để lại thay đổi.
- Bảng danh sách tài khoản phải cuộn ngang mới thấy cột "Trạng thái" ở bề ngang 1440. Không thuộc phạm vi phiếu này, chỉ ghi lại.
