# Bảng đối chiếu điều kiện — CNDSMLTVV_OOS_03 (row 143, tab `UAT_TGPL Doanh Nghiệp-tuần 2`)

**Chức năng:** Công khai mạng lưới TVV — FR-IV-08 (UC46), hộp thoại `MD-CONG-KHAI`, nhánh lỗi E2 / `ERR-CK-02`
**Nội dung TC:** bỏ trống "Mô tả công khai" rồi xác nhận → hệ thống chặn đúng nhưng hiện **2 dòng báo lỗi trùng nghĩa** cho cùng một ô, cả 2 đều không dùng nội dung `ERR-CK-02` (SRS `:682`).
**Loại bug:** thông báo lỗi chỉ hiện khi thao tác **rơi vào nhánh lỗi** (ô mô tả để trống + bấm xác nhận) → KHÔNG phải bug tĩnh, BẮT BUỘC có bảng này (QA_VERIFY_PROTOCOL §Quy tắc VÀNG).
**Ngày verify:** 2026-08-03 · **Tài khoản QA dùng:** `cbnv_tw_02` (CB_NV_TW, đơn vị Cục Bổ trợ tư pháp - Bộ Tư pháp, cấp TW)

> **Nguồn gốc dòng TC:** lỗi do QA tự phát hiện khi verify CNDSMLTVV_01 (row 124), nằm ngoài tiêu chí của phiếu nên mở dòng mới. **Không có evidence đối tác cho riêng lỗi này** — cột "Đối tác" ghi rõ "Không áp dụng" thay vì suy diễn điều kiện đối tác.

| Điều kiện có thể đổi kết quả | Đối tác | Mình test | GAP? |
|---|---|---|:-:|
| Vai trò / tài khoản | Không áp dụng — lỗi do QA phát hiện, không có báo cáo đối tác | `cbnv_tw_02` — "CB Nghiệp vụ - Trung ương #02", vai trò `CB_NV_TW`, đơn vị `Cục Bổ trợ tư pháp - Bộ Tư pháp`, cấp `BTP · TW` — đúng vai trò thao tác luồng công khai theo `FR-IV-08:657` | Không |
| Màn hình + hộp thoại | Không áp dụng — lỗi do QA phát hiện, không có báo cáo đối tác | Màn "Tư vấn viên / Chuyên gia", tab "Đang hoạt động"; hộp thoại **"Công khai hàng loạt lên Cổng PLQG"** đang mở | Không |
| Trạng thái entity | Không áp dụng — lỗi do QA phát hiện, không có báo cáo đối tác | `TVV-SEED-0001` "Nguyễn Văn Seed" — `trangThai = HOAT_DONG`, `laCongKhai = false` (chưa công khai, nên mở được hộp thoại công khai) | Không |
| Dữ liệu đưa vào nhánh lỗi | Không áp dụng — lỗi do QA phát hiện, không có báo cáo đối tác | Ô **"Mô tả công khai" để trống** — đọc được bộ đếm ký tự hiển thị `0 / 5000` trước khi bấm. Đây đúng là điều kiện E2 mà `:682` mô tả ("Thiếu mô tả công khai khi CONG_KHAI") | Không |
| Thao tác / nút bấm | Không áp dụng — lỗi do QA phát hiện, không có báo cáo đối tác | Bấm nút xác nhận **[Công khai]** trong hộp thoại, đúng 1 lần | Không |

## Ghi chú đóng GAP

- **Không có ô GAP nào vì không có điều kiện đối tác để lệch:** dòng TC do QA mở, toàn bộ điều kiện do QA tự dựng và đã ghi đủ ở cột "Mình test".
- **Số liệu quyết định:** `SO_NODE_LOI = 2`, `SO_REQUEST = 0` (hệ thống chặn đúng, không gửi gì ra máy chủ). Hai dòng chữ đo được:
  1. *"Vui lòng nhập mô tả công khai"*
  2. *"Mô tả công khai không được để trống"*
- **Đã loại trừ bẫy "node ẩn" của bài học 2026-07-16:** không kết luận bằng cách nối chữ trong DOM. Với **từng** node đã đo diện tích chiếm chỗ thực tế — mỗi node **592×22** điểm ảnh, khác 0, `visibility` và `display` đều không bị ẩn. Tức cả 2 dòng đều là chữ người dùng nhìn thấy, không phải node dành riêng cho trình đọc màn hình.
- **Ảnh chụp xác nhận lại kết quả đo:** ảnh full-res bắt được cả 2 dòng chữ đỏ cùng hiện dưới một ô nhập — khớp với số liệu, không phải hiện tượng chỉ tồn tại trong công cụ đo.
- **Đã phân biệt "lặp hiển thị" với "gửi trùng":** `SO_REQUEST = 0` nên đây là lỗi hiển thị thông báo, không có nguy cơ tạo dữ liệu trùng.
- **Không thay đổi dữ liệu ở bước đo này:** thao tác bị chặn nên `TVV-SEED-0001` giữ nguyên `laCongKhai = false`.

**Kết luận: 0 GAP** — mọi điều kiện quan sát lỗi đã được dựng và test thật.
