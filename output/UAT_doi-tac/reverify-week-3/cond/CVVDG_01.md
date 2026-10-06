# Bảng đối chiếu điều kiện — CVVDG_01

Loại bug: **Chọn vụ việc đánh giá (FR-VI-05) — đối tác báo toast "Đã lưu {N} vụ việc" không giống thiết kế.** App thực tế hiện toast khác khi CB NV xác nhận chọn VV. Verdict phụ thuộc: (1) tái hiện đúng role/state, (2) SRS có quy định chuỗi toast cụ thể không.

| Điều kiện có thể đổi kết quả | Đối tác (từ evidence CVVDG_01.jpg) | Mình test | GAP? |
|---|---|---|:-:|
| Vai trò người thao tác | **Cán bộ Nghiệp vụ** (CB_NV_TW trong ảnh) xác nhận chọn VV | `cbnv_hn` — CB_NV_DP, Sở Tư pháp Hà Nội; là CB NV + trưởng nhóm được phân công của đợt | Không |
| Trạng thái đợt | Đợt ở **THUC_HIEN** (Tab Thực hiện mở, section "Chọn vụ việc đánh giá") | Đợt DGHQ-B1 ở **THUC_HIEN** (đã duyệt phân công) | Không |
| Thao tác đối chiếu | Tích VV hoàn thành → **Xác nhận chọn** → xem toast | Tích EEE-VH-014 (HOAN_THANH) → Xác nhận chọn → confirm "Xác nhận" → đọc toast qua observer | Không |
| Đối tượng so sánh (toast) | App hiện **"Đã chọn vụ việc đánh giá"**; đối tác kỳ vọng (theo thiết kế) **"Đã lưu {N} vụ việc"** | Toast thực = **"Đã chọn vụ việc đánh giá"** (1 toast / 1 POST `vu-viec-select`, không double) | Không |

**Kết luận: 0 GAP về role/state/data.** Tái hiện đúng điều kiện đối tác (CB NV, đợt THUC_HIEN, đúng thao tác). Đối chiếu SRS:

- **Chức năng chạy đúng:** tích VV → Xác nhận → `POST .../vu-viec-select` [200], đợt "Số vụ việc đánh giá" = 1, VV chuyển "Đã chọn". Nghiệp vụ đạt.
- **Lệch wording:** app hiện **"Đã chọn vụ việc đánh giá"**; đối tác kỳ vọng **"Đã lưu {N} vụ việc"** (có số lượng + động từ "Lưu").
- **SRS FR-VI-05 KHÔNG quy định chuỗi toast thành công cụ thể.** Bước xử lý số 6 ghi "Lưu danh sách VV đánh giá" (mô tả xử lý, không phải chuỗi UI). Bảng Outputs / Error Handling không có dòng nào prescribe text toast "Đã lưu {N} vụ việc". Kỳ vọng của đối tác đến từ bản thiết kế (mockup), không phải SRS.
- Toast hiện tại truyền đạt đúng ý nghĩa (chọn/lưu thành công). Không xác định được app SAI hay bản thiết kế mới đúng nếu không có nguồn thiết kế uy tín → **BA confirm** (không log bug, không tự khẳng định đúng/sai wording).

Chi tiết: xem [`../reverify-audit/CVVDG_01/audit.md`](../reverify-audit/CVVDG_01/audit.md).
