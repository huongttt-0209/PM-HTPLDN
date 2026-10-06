# Bảng đối chiếu điều kiện — QLTMBMHD_19 (xóa hàng loạt toàn bộ: trạng thái chọn sau xóa)

Loại bug (phần Open): **Sau khi xóa hàng loạt thành công, thanh "Đã chọn N thư mục" + nút hành động hàng loạt không tự reset.** Bảng dưới chứng minh đã tái hiện ĐÚNG vai trò / loại thư mục / thao tác mà đối tác dùng, và quan sát đúng hiện tượng đối tác báo (dòng đã chọn + nút vẫn hiển thị sau xóa).

| Điều kiện có thể đổi kết quả | Đối tác (từ evidence QLTMBMHD_19 + sheet) | Mình test | GAP? |
|---|---|---|:-:|
| Vai trò người thao tác | **CB Nghiệp vụ - TW** (CB_NV_TW, BTP·TW) | `cbnv_tw` — CB Nghiệp vụ - TW (BTP·TW), cùng vai trò | Không |
| Loại thư mục xóa hàng loạt | Thư mục Nháp/Ẩn rỗng (đủ điều kiện xóa) | Tích 2 thư mục Nháp rỗng "BM-B1-0720 DelA" + "BM-B1-0720 Trung" (đều eligible) | Không |
| Thao tác thực hiện | Chọn nhiều → nút "Xóa hàng loạt" → xác nhận Xóa | Tích 2 thư mục → "Xóa hàng loạt" → xác nhận; 2 DELETE request (`SO_REQUEST=2`), 2 thư mục biến mất khỏi danh sách | Không |
| Hiện tượng verify (thanh chọn + nút sau xóa) | Sau xóa **vẫn hiển thị dòng đã chọn + nút hành động hàng loạt** | Thanh "Đã chọn 2 thư mục" (count CŨ) + nút [Xóa/Công khai/Ẩn hàng loạt] **VẪN hiện**; `checkboxesStillChecked=0` (0 dòng thực sự tích) — quan sát khớp đối tác | Không |

**Kết luận: 0 GAP.** Tái hiện đúng vai trò/loại thư mục/thao tác; quan sát khớp: sau xóa hàng loạt thành công, thanh "Đã chọn N thư mục" + nút hành động hàng loạt vẫn hiển thị với count cũ (stale), không tự reset. SRS `srs-fr-09-bieu-mau.md:616` (SCR-VII-01 #14 — Hành động hàng loạt: điều kiện hiển thị **"khi chọn nhiều"**): sau xóa không còn dòng nào được chọn (`checkboxesStillChecked=0`) → thanh + nút phải tự ẩn/reset. Vi phạm điều kiện hiển thị. → **Open** (BUG-QLTMBMHD_19).

**Phần claim KHÔNG tái hiện (không nằm trong verdict Open — ghi để đối tác đối chiếu):**
- Đối tác báo thông báo **"nhân đôi" + "sai thiết kế"**. Đo bằng `toast-capture.js`: `SO_KHUNG_THONG_BAO=1`, `chu=["Đã xóa 2 thư mục."]`, `BI_LAP=false` → chỉ **1 khung**, KHÔNG nhân đôi, đúng mẫu `Đã xóa {N} thư mục`. → phần "nhân đôi/sai thiết kế" của claim không phải bug.

Chi tiết: bug [`../bug-reports/bieu-mau/Pass-bug-report-bieu-mau-batch1.md`](../bug-reports/bieu-mau/Pass-bug-report-bieu-mau-batch1.md) (BUG-QLTMBMHD_19) + ảnh [`../bug-reports/bieu-mau/image/BUG-QLTMBMHD_19-selection-not-cleared.png`](../bug-reports/bieu-mau/image/BUG-QLTMBMHD_19-selection-not-cleared.png).
