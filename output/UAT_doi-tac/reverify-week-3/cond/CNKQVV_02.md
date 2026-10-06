# Bảng đối chiếu điều kiện — CNKQVV_02

Loại bug: **Cập nhật kết quả cuối / hoàn thành vụ việc (Nhóm 6) — đối tác báo "tên nút chức năng và các trường thông tin không giống với thiết kế".** Hiển thị nút + modal phụ thuộc role (CB NV) + state (Đã duyệt) → điền bảng, xác nhận app thực tế đúng điều kiện đối tác trước khi kết luận.

| Điều kiện có thể đổi kết quả | Đối tác (từ evidence + cột Điều kiện/Bước) | Mình test | GAP? |
|---|---|---|:-:|
| Vai trò người thao tác | **Cán bộ nghiệp vụ** (CB NV) mở chức năng hoàn thành/cập nhật kết quả cuối | `cbnv_tw` — CB_NV_TW, đơn vị BTP·TW; là CB NV được giao của vụ việc | Không |
| Trạng thái vụ việc | Vụ việc ở **"Đã duyệt"** (có nút hoàn thành/cập nhật KQ cuối) | VV-BTP-TW-20260712-001 ở **DA_DUYET** ("Đã duyệt") | Không |
| Màn hình/thao tác đối chiếu | Mở chức năng cập nhật kết quả cuối → xem tên nút + các trường của modal | Bấm nút hành động → mở modal → đọc tên nút, tiêu đề modal, danh sách trường | Không |
| Đối tượng so sánh (tên nút) | "Tên nút chức năng không giống thiết kế" | Nút hành động = **"Hoàn thành"**; tiêu đề modal = **"Hoàn thành vụ việc"**; nút gửi = **"Xác nhận"** | Không |
| Đối tượng so sánh (các trường) | "Các trường thông tin không giống thiết kế" | Modal có 2 trường: **"Kết luận cuối cùng"** (bắt buộc, 0/5000) + **"Kết quả xử lý"** (radio Thành công / Không thành công) | Không |

**Kết luận: 0 GAP về role/state/data.** Đã test đúng điều kiện đối tác (CB NV, vụ việc "Đã duyệt", đúng modal đối tác chụp trong evidence). Kết quả đối chiếu SRS:

- **Chức năng chạy đúng:** điền "Kết luận cuối cùng" + chọn "Kết quả xử lý" → Xác nhận → `POST .../hoan-thanh` [201], vụ việc chuyển **"Hoàn thành"**. Nghiệp vụ đạt.
- **Lệch 1 — tên nút:** app dùng nút **"Hoàn thành"** / modal **"Hoàn thành vụ việc"**; đặc tả FR-V.I-16 (AC `srs-fr-05-vu-viec.md:1167`) + bảng nút hành động (`:1739`) ghi nút là **"Cập nhật kết quả cuối" / [Cập nhật KQ cuối]**.
- **Lệch 2 — trường:** modal có trường **"Kết quả xử lý (Thành công/Không thành công)"** — KHÔNG nằm trong danh sách Inputs của FR-V.I-16 (`:1136-1140`, chỉ có `ket_luan_cuoi`). Trường "Kết luận cuối cùng" khớp `ket_luan_cuoi` ✅.
- 2 lệch trên đều **nhẹ + hợp lý về mặt thiết kế** (tên "Hoàn thành" rõ nghĩa hơn theo transition → HOAN_THANH; trường "Kết quả xử lý" ánh xạ field `ketQuaXuLy` có sẵn trong mô hình dữ liệu). Không xác định được app SAI hay đặc tả text chưa cập nhật nếu không có nguồn thiết kế uy tín → **BA confirm** (không log bug, không tự khẳng định đúng/sai).

Chi tiết: xem [`../reverify-audit/CNKQVV_02/audit.md`](../reverify-audit/CNKQVV_02/audit.md).
