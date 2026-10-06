# Audit — LKHDG_07 (row 46) · Verdict: Open (BUG-LKHDG_07)

## Cổng 1 — Evidence đối tác
- File: `partner-evidence/LKHDG_07.jpg`. Form "Tạo kế hoạch đánh giá" (env đối tác `htpldn-uat.ospgroup.vn`): các trường "Tên đợt đánh giá *", "Tần suất *", "Đối tượng *", "Cơ quan được đánh giá *", "Thời gian bắt đầu *", "Thời gian kết thúc *" đều có dấu *; riêng **"Mục tiêu"** KHÔNG có dấu *.
- Đối tác báo: "Trường thông tin Mục tiêu không được đánh dấu bắt buộc".

## Cổng 2 — Hiểu bug
- Bug tĩnh về đánh dấu bắt buộc (required marking) của 1 field trên form — deterministic, không phụ thuộc input/data/state. Chỉ cần Cổng 3 (đối chiếu SRS), không cần bảng điều kiện.

## Cổng 3 — Đối chiếu SRS vs web (env 18.143, cbnv_tw)
| Mục | SRS | Web thực tế | Kết luận |
|---|---|---|---|
| muc_tieu bắt buộc | FR-VI-01 Inputs #2 (dòng 107): `muc_tieu | text (long) | Y` | Nhãn "Mục tiêu" không có dấu * (required:false trong DOM `.ant-form-item-required`) | SAI — không đánh dấu bắt buộc |
| Form field Mục tiêu | SCR-VI-01 #22 (dòng 836): "Mục tiêu | C16 Rich Text | **Bắt buộc**" | 6 field khác đều có * (required:true), riêng Mục tiêu required:false | Vi phạm |

## Verdict: Open — BUG-LKHDG_07
- "Mục tiêu" bắt buộc theo SRS nhưng form đánh dấu là tùy chọn → user có thể bỏ trống, sai chuẩn nhập liệu. Cùng gốc lỗi với LKHDG_08 (không validate bắt buộc).
- Bug-report: `bug-reports/Pass-bug-report-DGHQ-batchA.md` (BUG-LKHDG_07_08). Evidence: `bug-reports/image/BUG-LKHDG_07_08-muctieu-khong-batbuoc.png`.
- Note sheet: `note.txt`.
