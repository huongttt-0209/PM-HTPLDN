# Audit — LKHDG_08 (row 47) · Verdict: Open (BUG-LKHDG_08)

## Cổng 1 — Evidence đối tác
- File: `partner-evidence/LKHDG_08.jpg`. Env đối tác submit form trống → hiện lỗi bắt buộc cho MỌI trường (Vui lòng nhập tên đợt, chọn tần suất, đối tượng, cơ quan, thời gian...) nhưng **"Mục tiêu" KHÔNG có thông báo lỗi**.
- Đối tác báo: "Trường thông tin Mục tiêu không hiển thị thông báo bắt buộc".

## Cổng 2 — Hiểu bug
- Bug về hành vi validate bắt buộc khi submit form trống — deterministic (không phụ thuộc data/state; mở form + submit trống). Chỉ cần Cổng 3.

## Cổng 3 — Đối chiếu SRS vs web (env 18.143, cbnv_tw)
| Mục | SRS | Web thực tế | Kết luận |
|---|---|---|---|
| muc_tieu bắt buộc | FR-VI-01 Inputs #2 (dòng 107): `muc_tieu ... Y` | Submit form trống: "Mục tiêu" error = null (không báo lỗi) | SAI — không validate bắt buộc |
| Form validate | SCR-VI-01 #22 (dòng 836): "Mục tiêu | Bắt buộc" | 6 field required khác đều báo "Vui lòng ..."; riêng Mục tiêu bỏ qua | Vi phạm |

## Verdict: Open — BUG-LKHDG_08
- "Mục tiêu" bắt buộc theo SRS nhưng submit trống không bị chặn/không báo lỗi → có thể lưu kế hoạch thiếu mục tiêu. Cùng gốc lỗi với LKHDG_07 (không đánh dấu *).
- Bug-report: `bug-reports/Pass-bug-report-DGHQ-batchA.md` (BUG-LKHDG_07_08). Evidence: `bug-reports/image/BUG-LKHDG_07_08-muctieu-khong-batbuoc.png` (1 ảnh: 6 field báo lỗi, Mục tiêu không).
- Note sheet: `note.txt`.
