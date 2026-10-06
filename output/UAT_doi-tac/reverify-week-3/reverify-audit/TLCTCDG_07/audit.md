# Audit — TLCTCDG_07 (row 55) · Verdict: Open (BUG-TLCTCDG_07)

## Cổng 1 — Evidence đối tác
- KQ thực đối tác: dòng tiêu chí không có nút Sửa → không sửa được tiêu chí đã tạo.

## Cổng 2 — Hiểu bug
- Bug tĩnh (thiếu affordance sửa) — kiểm tra trực tiếp trên UI, không phụ thuộc role/state khác (state LAP_KE_HOACH là state cho phép sửa tiêu chí).

## Cổng 3 — Đối chiếu SRS vs thực tế (env 18.143, cbnv_tw, đợt DG-20260720-0002 LAP_KE_HOACH)
| Mục | SRS | Thực tế | Kết luận |
|---|---|---|---|
| Cột Hành động dòng tiêu chí | SCR-VI-01 #29 (dòng 850): "Hành động (Sửa/Xóa C12)" | Chỉ có 1 nút Xóa (icon `anticon-delete`), không có nút Sửa | THIẾU nút Sửa |
| Sửa inline trên ô | #29 (dòng 850): "Bảng tiêu chí (Editable)... C09 inline... inline edit" | Click ô Tên / double-click / click dòng → không xuất hiện input, không mở modal | THIẾU inline edit |

- DOM: `rowActionButtons = [[{label:"",icon:"anticon anticon-delete",text:""}]]`; `inlineEditInputAppeared=false`, `rowClickModal=false`, `dblclickInputAppeared=false`, `dblclickModal=false`.

## Verdict: Open — BUG-TLCTCDG_07
- Tiêu chí đã tạo không thể chỉnh sửa bằng bất kỳ đường nào (nút Sửa lẫn inline edit đều thiếu) → vi phạm SRS SCR-VI-01 #29 dòng 850.
- Evidence: `../../bug-reports/image/tlctcdg-row-action-onlydelete.png`.
