# Audit — TLCTCDG_12 (row 59) · Verdict: Open (BUG-TLCTCDG_12)

## Cổng 1 — Evidence đối tác
- KQ thực đối tác: không có nút "Lưu & Quay lại Kế hoạch".

## Cổng 2 — Hiểu bug
- Bug tĩnh (thiếu nút trong thanh hành động) — kiểm tra trực tiếp, không phụ thuộc role/state.

## Cổng 3 — Đối chiếu SRS vs thực tế (env 18.143, cbnv_tw, đợt DG-20260720-0002 LAP_KE_HOACH)
| Mục | SRS | Thực tế | Kết luận |
|---|---|---|---|
| Thanh hành động Tab Tiêu chí | SCR-VI-01 #34 (dòng 855): "[Hủy] [Lưu] [**Lưu & Quay lại KH**]" | ["Quay lại danh sách","Hủy đợt","Thêm tiêu chí","Nhập từ danh mục","Lưu"] (+"Hủy thay đổi" khi có sửa) | THIẾU "[Lưu & Quay lại KH]" |

- DOM: `actionBar = ["Quay lại danh sách","Hủy đợt","Thêm tiêu chí","Nhập từ danh mục","Hủy thay đổi","Lưu"]` — không có "Lưu & Quay lại KH".

## Verdict: Open — BUG-TLCTCDG_12
- Thanh hành động Tab Tiêu chí thiếu nút "[Lưu & Quay lại KH]" theo SRS SCR-VI-01 #34 dòng 855.
- Evidence: `../../bug-reports/image/tlctcdg-criteria-tab-actionbar.png`.
