# Bảng đối chiếu điều kiện — QLTMBMHD_20 (xóa hàng loạt một phần: trạng thái chọn sau xóa)

Loại bug (phần Open): **Xóa hàng loạt MỘT PHẦN (eligible + ineligible) → sau xóa thanh "Đã chọn N thư mục" + nút hành động hàng loạt không tự reset.** Bảng dưới chứng minh đã tái hiện ĐÚNG vai trò / tổ hợp thư mục / thao tác mà đối tác dùng, và quan sát đúng hiện tượng đối tác báo.

| Điều kiện có thể đổi kết quả | Đối tác (từ evidence QLTMBMHD_20 + sheet) | Mình test | GAP? |
|---|---|---|:-:|
| Vai trò người thao tác | **CB Nghiệp vụ - TW** (CB_NV_TW, BTP·TW) | `cbnv_tw` — CB Nghiệp vụ - TW (BTP·TW), cùng vai trò | Không |
| Tổ hợp thư mục tích chọn | 1 eligible (Nháp rỗng) + 1 ineligible (còn biểu mẫu) | Tích "BM-B1-Partial-0720" (Nháp rỗng, eligible) + "QA Hidden Folder 715" (Nháp, 1 BM, ineligible) | Không |
| Thao tác thực hiện | Chọn nhiều → "Xóa hàng loạt" → xác nhận | Tích 2 thư mục → "Xóa hàng loạt" → modal xác nhận → Xóa; `SO_REQUEST=1` DELETE (chỉ xóa thư mục eligible) | Không |
| Hiện tượng verify (thanh chọn + nút sau xóa) | Sau xóa **vẫn hiển thị dòng đã chọn + nút hành động hàng loạt** | Thanh "Đã chọn 2 thư mục" (count CŨ) + nút VẪN hiện; `checkboxesStillChecked=1` (thư mục bị bỏ qua vẫn tích) — quan sát khớp đối tác | Không |

**Kết luận: 0 GAP.** Tái hiện đúng vai trò/tổ hợp thư mục/thao tác; quan sát khớp: sau xóa hàng loạt một phần, thanh "Đã chọn 2 thư mục" + nút hành động hàng loạt vẫn hiển thị, thư mục bị bỏ qua vẫn ở trạng thái tích chọn. SRS `srs-fr-09-bieu-mau.md:616` (SCR-VII-01 #14 — "khi chọn nhiều"): sau khi thao tác xong phải tự ẩn/reset. Vi phạm. → **Open** (cùng BUG-QLTMBMHD_19).

**Ghi nhận tích cực (app xử lý ĐÚNG phần một phần):** Modal xác nhận cảnh báo "Xóa 1 thư mục? ... **(1 thư mục đang chứa biểu mẫu sẽ được bỏ qua)**"; sau xóa chỉ `SO_REQUEST=1` DELETE, thư mục ineligible "QA Hidden Folder 715" **CÒN NGUYÊN** (không xóa nhầm). Giải tỏa nghi vấn "xóa nhầm" nêu ở QLTMBMHD_17.

**Phần cần BA chốt (KHÔNG nằm trong verdict Open):** wording/thời điểm thông báo phần bị bỏ qua — app báo ở **modal xác nhận** (trước xóa), toast thành công chỉ "Đã xóa 1 thư mục." (`SO_KHUNG=1`, `BI_LAP=false`); đối tác kỳ vọng gộp cả 2 vào toast thành công. SRS không quy định mẫu thông báo xóa hàng loạt một phần → **BA confirm** (`../ba-confirm/bieu-mau/ba-confirmation-needed-week-3-bieu-mau-batch1.md`).

Chi tiết: bug [`../bug-reports/bieu-mau/Pass-bug-report-bieu-mau-batch1.md`](../bug-reports/bieu-mau/Pass-bug-report-bieu-mau-batch1.md) (BUG-QLTMBMHD_19, phần QLTMBMHD_20) + ảnh [`../reverify-audit/QLTMBMHD_20/post-partial-delete-selection-not-cleared.png`](../reverify-audit/QLTMBMHD_20/post-partial-delete-selection-not-cleared.png).
