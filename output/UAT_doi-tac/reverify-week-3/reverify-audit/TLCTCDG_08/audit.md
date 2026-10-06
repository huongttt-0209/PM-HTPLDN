# Audit — TLCTCDG_08 (row 56) · Verdict: Open (BUG-TLCTCDG_08)

## Cổng 1 — Evidence đối tác
- KQ thực đối tác: xóa tiêu chí không có hộp thoại xác nhận.

## Cổng 2 — Hiểu bug
- Bug tĩnh (thiếu bước xác nhận cho thao tác destructive) — kiểm tra trực tiếp, không phụ thuộc role/state.

## Cổng 3 — Đối chiếu SRS vs thực tế (env 18.143, cbnv_tw, đợt DG-20260720-0002 LAP_KE_HOACH)
| Mục | SRS | Thực tế | Kết luận |
|---|---|---|---|
| Xóa tiêu chí | SCR-VI-01 #29 (dòng 850): "Hành động (Sửa/Xóa **C12**)" | Click Xóa → xóa ngay | — |
| C12 = xác nhận? | #39 (dòng 865): nút Phê duyệt PC "→ **C12 confirm**" ⇒ C12 gồm bước xác nhận | Không có Popconfirm / Modal.confirm / popup | THIẾU bước xác nhận |

- DOM khi click Xóa: `rowCountBefore=1 → rowCountAfter=0`; `popover=false`, `popconfirm=false`, `modalConfirm=false`, `anyModal=false`, `deletedImmediately=true`.

## Verdict: Open — BUG-TLCTCDG_08
- Xóa tiêu chí (thao tác mất dữ liệu) thực thi ngay không có bước xác nhận. SRS gán Xóa vào nhóm C12 mà C12 được mô tả là bước "confirm" (#39 dòng 865). → thiếu xác nhận, rủi ro thao tác nhầm.
- Evidence: `../../bug-reports/image/tlctcdg-row-action-onlydelete.png` (nút Xóa) + log DOM `deletedImmediately`.
