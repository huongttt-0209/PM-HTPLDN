# Bảng đối chiếu điều kiện — QLTMBMHD_10 (nút "Sửa" trên thư mục Công khai)

Loại bug: **Hiển thị nút Sửa theo trạng thái thư mục.** Đối tác kỳ vọng nút Sửa CHỈ hiện khi thư mục Nháp/Ẩn + đúng đơn vị sở hữu; thực tế nút Sửa hiện cả trên thư mục Công khai. Verdict phụ thuộc: tái hiện đúng role + đúng thư mục Công khai + đối chiếu điều kiện hiển thị SRS.

| Điều kiện có thể đổi kết quả | Đối tác (từ evidence QLTMBMHD_10.jpg) | Mình test | GAP? |
|---|---|---|:-:|
| Vai trò người xem | **CB Nghiệp vụ - TW** (CB_NV_TW, BTP·TW) | `cbnv_tw` — CB Nghiệp vụ - TW (BTP·TW), cùng vai trò | Không |
| Trạng thái thư mục kiểm | Thư mục **Đã công khai** (tab "Đã công khai", 3 thư mục) | Thư mục "Thư mục biểu mẫu seed" — **Đã công khai** (BTP·TW, 1 biểu mẫu) | Không |
| Đơn vị sở hữu | Thư mục thuộc đơn vị người xem (BTP·TW) | Tất cả 4 thư mục hiển thị đều thuộc BTP·TW (đúng đơn vị) — list chỉ hiện thư mục đơn vị mình | Không |
| Đối tượng so sánh (nút Sửa) | Nút **Sửa** hiển thị trên hàng thư mục Công khai | Nút **Sửa** hiển thị trên hàng "Thư mục biểu mẫu seed" (Công khai) — xác nhận qua evaluate_script + screenshot | Không |

**Kết luận: 0 GAP về role/state/đơn vị.** Tái hiện đúng: nút Sửa CÓ hiện trên thư mục Công khai (khớp đối tác). Đối chiếu SRS:

- SRS `srs-fr-09-bieu-mau.md:615` (SCR-VII-01 thành phần #13 — Cột Hành động): **"Công khai (khi NHAP/AN, có BM) / Ẩn (khi CONG_KHAI) / Sửa / Xóa (khi NHAP/AN, rỗng)"**.
- Nút **"Sửa" KHÔNG kèm điều kiện trạng thái** trong SRS (khác Công khai/Ẩn/Xóa đều có điều kiện rõ). → Theo SRS, Sửa hiển thị ở MỌI trạng thái, kể cả Công khai.
- App hiện Sửa trên Công khai = **ĐÚNG SRS**. Kỳ vọng đối tác (Sửa chỉ Nháp/Ẩn) **mâu thuẫn với SRS**.
- Vì SRS quy định rõ Sửa không giới hạn state, nhưng đối tác kỳ vọng khác → cần BA chốt luật hiển thị nút Sửa là authoritative theo SRS hay theo thiết kế đối tác. → **BA confirm** (không log bug, không tự khẳng định đối tác sai).

Chi tiết: xem [`../reverify-audit/QLTMBMHD_17/bulk-select-congkhai-nonempty.png`](../reverify-audit/QLTMBMHD_17/bulk-select-congkhai-nonempty.png) (ảnh list chung, hàng "Thư mục biểu mẫu seed" Công khai có nút Sửa).
