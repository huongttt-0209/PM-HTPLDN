# Nhật ký đo — CNKQHT_07 (dòng 315) — vòng 2, 04/08/2026

**Bản dựng đang chạy:** `assets/index-DpIXRGaI.js` · `HTPLDN · V1.0.5`.
**Lỗi gốc cần kiểm:** cập nhật kết quả hỗ trợ vụ việc nhưng cán bộ nghiệp vụ phụ trách không nhận được thông báo.

| Giờ (VN) | Thao tác | Số liệu đo được |
|---|---|---|
| 14:29 | Chọn vụ việc: lọc `/api/v1/vu-viecs` theo trạng thái `DANG_XU_LY` | `VV-BTP-TW-20260525-001` (id `71cb2ab1-a98c-478b-94dd-ef1ebc253baf`) — `nguoiHoTro = huongcg` (đăng nhập được), `nguoiTiepNhan = cb_nv_tw_01`. |
| 14:29 | Xác định người nhận & đếm TRƯỚC | Người nhận đúng là **`cb_nv_tw_01`** (đọc `nguoiTiepNhanId` của chính bản ghi, không đoán theo vai trò). Hộp thông báo: **453** mục, không mục nào của vụ việc này. |
| 14:30 | Đăng nhập trình duyệt `huongcg`/`Secret@123` → Vụ việc HTPL → mở chi tiết | Dòng thời gian có đủ chuỗi tiền đề: Tạo 25/05 → Tiếp nhận + Kiểm tra 23/06 → Phân công 09/07 → Xác nhận phân công 10/07. Trạng thái "Đang xử lý" (bước 6). |
| 14:30 | Cài lại bộ bắt thông báo | `soObserverDangSong = 1`. |
| 14:30:35 | Bấm "Cập nhật kết quả" → nhập nội dung `QA-KQ-V2-0408-742199 Ket qua ho tro cap nhat lai vong 2 tren ban dung moi.` + ghi chú + đính kèm tệp `ketqua-cnkqht07-v2.png` → "Xác nhận" | `SO_REQUEST=1`: `POST /api/v1/vu-viecs/{id}/cap-nhat-ket-qua` · `SO_KHUNG=1`, chữ "Đã cập nhật kết quả" · thời điểm bấm `07:30:35.860Z` · trạng thái giữ `DANG_XU_LY`, version 9. |
| 14:31 | Đọc lại màn chi tiết | Ảnh `image/CNKQHT_07-v2-01-luu-ket-qua-noi-dung-tep-luu-vet.png`: mục "Kết quả hỗ trợ" hiện đúng nội dung vừa nhập; tệp `ketqua-cnkqht07-v2.png (70 B)` nằm đầu danh sách; Dòng thời gian thêm "Cập nhật kết quả · 04/08/2026 14:30 · huongcg". |
| 14:31 | Đếm hộp thông báo SAU của `cb_nv_tw_01` | 453 → **455**; mục mới `Kết quả hỗ trợ đã được cập nhật - VV-BTP-TW-20260525-001` @ `07:30:35Z` — trùng đúng giây với thời điểm bấm. |
| 14:32 | Đăng nhập trình duyệt bằng chính `cb_nv_tw_01`/`Secret@123`, mở chuông | Ảnh `image/CNKQHT_07-v2-02-cbnv-phutrach-nhan-thongbao.png`: "CB Nghiệp vụ TW 01 · CB_NV_TW", chuông 99+; mục "Kết quả hỗ trợ đã được cập nhật - VV-BT…" / "Người được phân công đã cập nhật kết quả hỗ trợ vụ việc: - …", một phút trước. |

**Kết luận: Pass** — cả 3 vế đều đạt: nội dung lưu, tệp đính kèm lưu, và cán bộ nghiệp vụ phụ trách nhận được thông báo.
