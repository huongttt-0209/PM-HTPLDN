# Nhật ký đo — QLNDTVVCG_26 (dòng 323) — vòng 2, 04/08/2026

**Bản dựng đang chạy:** `assets/index-DpIXRGaI.js` · `HTPLDN · V1.0.5`.
**Lỗi gốc cần kiểm:** chuyên gia từ chối phân công nhưng cán bộ nghiệp vụ không nhận được thông báo (và thông báo không nêu lý do).

| Giờ (VN) | Thao tác | Số liệu đo được |
|---|---|---|
| 14:22 | Chọn bản ghi `TVCS-20260804-0005` (trạng thái "Phân công", chuyên gia `huongcg`) | Đọc `nguoiTaoId` của bản ghi → tra bằng `admin` ra tài khoản **`cb_nv_tw_10`**. Đây mới là hộp thông báo phải kiểm (vòng 1 nhiều khả năng mở nhầm hộp của người khác). |
| 14:22 | Đếm hộp thông báo TRƯỚC của `cb_nv_tw_10` | **83** mục, không mục nào nhắc `TVCS-20260804-0005`. |
| 14:23 | Vẫn phiên `huongcg`, mở chi tiết → cài lại bộ bắt thông báo (SPA điều hướng xoá observer) | `soObserverDangSong = 1`. |
| 14:23:02 | Bấm "Từ chối nhiệm vụ" → ô lý do (bắt buộc, `aria-required=true`, gợi ý "tối thiểu 10 ký tự") → nhập `QA-LYDO-V2-0408-742199 chuyen gia ban lich khong nhan nhiem vu nay` → bấm "Từ chối" | `SO_REQUEST=1`: `POST /api/v1/noi-dung-tu-van-cs/{id}/xac-nhan` · `SO_KHUNG=1` · thời điểm bấm `07:23:02.653Z`. |
| 14:23 | Đọc lại bản ghi | `PHAN_CONG` → `TIEP_NHAN`; `chuyenGiaId` được gỡ về `null`. Ảnh `image/QLNDTVVCG_26-v2-01-tuchoi-ve-tiepnhan-go-chuyengia.png`. |
| 14:24 | Đếm hộp thông báo SAU của `cb_nv_tw_10` | 83 → **85**; mục mới `Chuyên gia từ chối phân công: TVCS-20260804-0005` @ `07:23:02Z` — trùng đúng giây. |
| 14:25 | Đăng nhập trình duyệt bằng chính `cb_nv_tw_10`/`Secret@123`, mở màn Thông báo | Ảnh `image/QLNDTVVCG_26-v2-02-cbnv-nhan-thongbao-kem-ly-do.png`: "CB Nghiệp vụ TW 10 · CB_NV_TW"; nội dung **"Mã: TVCS-20260804-0005. Chuyên gia đã từ chối, cần phân công lại. Lý do: QA-LYDO-V2-0408-742199 chuyen gia ban lich khong nhan nhiem vu nay"** — chuỗi nhận dạng trùng khớp, chứng minh lý do được truyền nguyên văn. |

**Phát hiện thêm (ngoài phạm vi lỗi gốc, không đổi verdict):**
- Khung thông báo nổi sau khi từ chối vẫn ghi **"Đã xác nhận"** (giống hệt nhánh chấp nhận), trong khi "Kết quả mong đợi" của phiếu ghi "Đã từ chối yêu cầu".
- Sau khi từ chối, màn hình **ở lại trang chi tiết**, không quay về danh sách như phiếu mô tả.

**Kết luận: Pass** (lỗi gốc — cán bộ nghiệp vụ không nhận thông báo / thông báo thiếu lý do — đã hết).
