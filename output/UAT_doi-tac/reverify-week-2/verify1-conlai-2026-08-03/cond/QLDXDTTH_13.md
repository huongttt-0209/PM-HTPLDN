# QLDXDTTH_13 — Bảng đối chiếu điều kiện (re-verify sau dev fix, 2026-08-04)

> Sheet `UAT_TGPL Doanh Nghiệp-tuần 2` row 137 · Verdict QA vòng này = `Pass`
> Nội dung lỗi: dòng thông báo *"Đề xuất đào tạo mới"* của cán bộ nghiệp vụ được vẽ bằng biểu tượng báo lỗi (dấu X trong vòng tròn đỏ), trong khi các dòng khác cùng danh sách dùng dấu tích xanh.
> Lỗi phụ thuộc **luồng sinh thông báo** (phải có đề xuất mới gửi thì dòng thông báo mới xuất hiện) ⇒ **KHÔNG** phải bug tĩnh ⇒ bắt buộc điền bảng này.

| Điều kiện có thể đổi kết quả | Điều kiện của BUG GỐC | Điều kiện mình vừa test (2026-08-04) | GAP? |
|---|---|---|:-:|
| Vai trò / tài khoản | Người gửi: role **`DN`**, tài khoản **`0109998887`**. Người nhận thông báo: role **`CB_NV_DP`**, tài khoản **`cbnv_hn`** (`QA CB Nghiep vu Ha Noi`), đơn vị Sở Tư pháp Hà Nội | Người gửi: **`0109998887`** — giao diện hiện đúng `QA UAT Kiem Thu DN` · vai trò `DN` · `BTP · DP`. Người nhận: **`cbnv_hn`** — giao diện hiện đúng `QA CB Nghiep vu Ha Noi` · vai trò `CB_NV_DP` · `BTP · DP`. **Trùng khít** cả 2 vai | **Không** |
| Entity + trạng thái | Đề xuất đào tạo **vừa được gửi**, trạng thái **"Mới gửi"**; thông báo tương ứng ở trạng thái **chưa đọc** | Đề xuất **mới tạo lúc 00:27 ngày 04/08/2026** (`QA-RETEST-0804 …`), lĩnh vực `Lao động`, badge trạng thái **"Mới gửi"** trên cả danh sách lẫn màn chi tiết. Dòng thông báo sinh ra hiện **"3 phút trước"** và vẫn **chưa đọc** (có chấm xanh + số chưa đọc trên chuông tăng lên 13) | **Không** |
| Dữ liệu tiền đề | Đơn vị tiếp nhận của đề xuất **trùng** đơn vị của cán bộ nhận thông báo; hộp thông báo có **các dòng loại khác** (phân công / báo cáo đánh giá) để đối chứng biểu tượng | Đơn vị tiếp nhận của đề xuất = **Sở Tư pháp Hà Nội**, đúng đơn vị của `cbnv_hn` (cột "Người đề xuất" của bảng ghi rõ `QA UAT Kiem Thu DN · Sở Tư pháp Hà Nội`, và tài khoản đọc được bản ghi). Hộp thông báo có đủ **3 dòng loại khác** (1 phân công đánh giá được duyệt · 1 báo cáo bị từ chối · 1 báo cáo được phê duyệt) làm đối chứng — đúng như bug gốc | **Không** |
| Input / thao tác quan sát | Đăng nhập cán bộ → bấm **biểu tượng chuông** trên thanh đầu trang → đọc biểu tượng bên trái dòng *"Đề xuất đào tạo mới"* và so với các dòng còn lại | Đăng xuất sạch phiên DN (gọi thoát phiên + xoá toàn bộ dữ liệu lưu trên trình duyệt) → đăng nhập `cbnv_hn` → bấm **biểu tượng chuông** → đọc **lớp CSS + màu** của biểu tượng từng dòng bằng mã trang **và** chụp ảnh màn hình đối chiếu. Làm đúng thao tác của bug gốc, chỉ bổ sung phép đo thứ hai | **Không** |

⇒ **0 GAP.** Mọi tiền đề (2 vai trò · đơn vị tiếp nhận · đề xuất mới ở trạng thái "Mới gửi" · các dòng thông báo đối chứng) đều tự dựng lại qua giao diện thật trong lượt re-verify này, không đóng bằng lập luận và không đo trên dữ liệu cũ.
