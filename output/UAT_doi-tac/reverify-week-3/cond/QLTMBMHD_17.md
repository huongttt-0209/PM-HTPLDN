# Bảng đối chiếu điều kiện — QLTMBMHD_17 (tích chọn hàng loạt thư mục Công khai / còn biểu mẫu)

Loại bug: **Cho phép tích chọn thư mục không đủ điều kiện xóa để xóa hàng loạt.** Đối tác kỳ vọng chỉ tích chọn/xóa hàng loạt được thư mục Nháp/Ẩn + rỗng; thực tế app cho tích chọn cả thư mục Công khai + thư mục còn biểu mẫu và nút "Xóa hàng loạt" vẫn bật. Verdict phụ thuộc: tái hiện đúng role + tích đúng thư mục ineligible + đối chiếu SRS về điều kiện tích chọn.

| Điều kiện có thể đổi kết quả | Đối tác (từ evidence QLTMBMHD_17.webm + sheet) | Mình test | GAP? |
|---|---|---|:-:|
| Vai trò người thao tác | **CB Nghiệp vụ - TW** (CB_NV_TW, BTP·TW) | `cbnv_tw` — CB Nghiệp vụ - TW (BTP·TW), cùng vai trò | Không |
| Loại thư mục tích chọn | Thư mục **Công khai** + thư mục **còn biểu mẫu** | Tích "Thư mục biểu mẫu seed" (Công khai, 1 BM) + "QA Hidden Folder 715" (Nháp, 1 BM) — cả 2 đều ineligible | Không |
| Trạng thái checkbox | Ô chọn cho tích được trên thư mục ineligible | `checkboxDisabled=false` trên MỌI hàng (kể cả Công khai/còn biểu mẫu) — evaluate_script | Không |
| Đối tượng so sánh (nút Xóa hàng loạt) | Nút "Xóa hàng loạt" bật khi chọn thư mục ineligible | Bar "Đã chọn 2 thư mục" hiện, nút **"Xóa hàng loạt" enabled** (disabled=false) — screenshot | Không |

**Kết luận: 0 GAP về role/loại thư mục.** Tái hiện đúng: app CHO tích chọn thư mục Công khai + còn biểu mẫu, nút "Xóa hàng loạt" bật (khớp đối tác). Đối chiếu SRS:

- SRS `srs-fr-09-bieu-mau.md:610` (SCR-VII-01 thành phần #8 — Checkbox "Chọn hàng loạt"): điều kiện hiển thị **"luôn hiển thị"** — KHÔNG nêu điều kiện hạn chế tích chọn theo state/rỗng.
- SRS `:616` (thành phần #14 — Hành động hàng loạt [Xóa hàng loạt]): điều kiện **"khi chọn nhiều"** — KHÔNG nêu điều kiện eligibility theo state/rỗng cho việc tích chọn.
- Kỳ vọng của chính đối tác ở case liền kề **QLTMBMHD_20** (`Đã xóa {X} thư mục. {Y} thư mục không đủ điều kiện xóa (còn biểu mẫu)`) cho thấy **thiết kế là: chọn bất kỳ → khi XÓA hệ thống validate + báo phần không đủ điều kiện** (select-then-validate). Theo mô hình này, việc CHO tích chọn thư mục ineligible KHÔNG phải lỗi — validate xảy ra ở bước xóa.
- SRS không quy định rõ checkbox phải bị vô hiệu cho thư mục ineligible → đây là câu hỏi thiết kế UX (chặn tích chọn từ đầu vs cho chọn rồi validate). → **BA confirm.**
- ⚠️ Điểm cần verify riêng ở **QLTMBMHD_20 (case 86)**: khi thực sự bấm "Xóa hàng loạt" trên thư mục Công khai/còn biểu mẫu, hệ thống có CHẶN đúng (không xóa các thư mục này) hay xóa nhầm → nếu xóa nhầm sẽ là bug Open riêng (vi phạm ERR-TM-02 + SRS:615 điều kiện Xóa).

Chi tiết: xem [`../reverify-audit/QLTMBMHD_17/bulk-select-congkhai-nonempty.png`](../reverify-audit/QLTMBMHD_17/bulk-select-congkhai-nonempty.png).
