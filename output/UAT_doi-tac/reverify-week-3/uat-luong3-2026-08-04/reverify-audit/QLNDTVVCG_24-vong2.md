# Nhật ký đo — QLNDTVVCG_24 (dòng 322) — vòng 2, 04/08/2026

**Bản dựng đang chạy:** `assets/index-DpIXRGaI.js` · nhãn sidebar `HTPLDN · V1.0.5` (kiểm lúc 14:1x sau khi tải lại trang bỏ bộ nhớ đệm).
**Lỗi gốc cần kiểm:** chuyên gia bấm "Chấp nhận" nhưng doanh nghiệp và cán bộ nghiệp vụ không nhận được thông báo.

| Giờ (VN) | Thao tác | Số liệu đo được |
|---|---|---|
| 14:18 | Chọn bản ghi: `GET /api/v1/noi-dung-tu-van-cs?trangThai=PHAN_CONG` | 6 bản ghi. Chọn `TVCS-20260803-0003` (id `06d6dd08-…`) vì chuyên gia được phân công là `huongcg` (đăng nhập được) **và** doanh nghiệp TKM Company có tài khoản `0151554887` (mở được hộp thông báo). |
| 14:19 | Đếm hộp thông báo TRƯỚC, bằng phiên curl riêng của từng người nhận | DN `0151554887`: **10** mục · CBNV `cbnv_tw`: **336** mục. Không mục nào nhắc `TVCS-20260803-0003`. |
| 14:20 | Đăng nhập trình duyệt `huongcg`/`Secret@123`, OTP 666666 → Tư vấn chuyên sâu → mở chi tiết | Trạng thái "Phân công", trục tiến trình ở bước 2. Có 2 nút "Chấp nhận" / "Từ chối nhiệm vụ". |
| 14:21 | Cài bộ bắt thông báo dùng chung (`tools/toast-capture.js`) | Tự kiểm: `soObserverDangSong = 1`. |
| 14:21:44 | Bấm "Chấp nhận" → hộp xác nhận "Chấp nhận tư vấn?" → xác nhận | `SO_REQUEST=1`: `POST /api/v1/noi-dung-tu-van-cs/{id}/xac-nhan` · `SO_KHUNG=1`, chữ "Đã xác nhận" · thời điểm bấm `07:21:44.275Z`. |
| 14:21 | Đọc lại bản ghi | `PHAN_CONG` → `DANG_TU_VAN`; `ngayBatDau = 07:21:44.370Z`; sinh **1 phiên tư vấn mới** (`ngayTao 07:21:44.362Z`). Ảnh `image/QLNDTVVCG_24-v2-01-chapnhan-doi-trangthai-dang-tu-van.png`. |
| 14:22 | Đếm hộp thông báo SAU | DN: 10 → **12**; mục mới `Chuyên gia đã xác nhận tư vấn: TVCS-20260803-0003` @ `07:21:44Z`. CBNV `cbnv_tw`: 336 → **338**; cùng tiêu đề, @ `07:21:44Z`. **Trùng đúng giây với thời điểm bấm.** |
| 14:22 | Đăng nhập trình duyệt bằng chính DN `0151554887`, mở chuông | Ảnh `image/QLNDTVVCG_24-v2-02-chuong-doanhnghiep-nhan-thongbao.png`: đầu trang ghi "Tester TKM · DN"; mục thông báo "Chuyên gia đã xác nhận tư vấn: TVCS-20…" / "Mã: TVCS-20260803-0003. Chuyên gia đã nhận việc, nội dung đa…". |

**Vì sao phải đếm trước/sau chứ không nhìn tổng số:** mỗi lần đăng nhập hệ thống tự sinh thông báo "Tài khoản vừa đăng nhập ở nơi khác", nên chỉ nhìn số tổng sẽ nhầm. Phép thử quyết định là **tiêu đề thông báo + dấu thời gian tới giây** trùng thời điểm bấm.

**Kết luận: Pass.**
