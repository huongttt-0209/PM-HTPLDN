# Audit — LKHDG_16/20/21/22 (rows 50/52/53/54) · Verdict: Open (BUG-LKHDG-EDIT)

Gộp 4 case cùng gốc: chức năng **Sửa đợt** không mở form chỉnh sửa.

## Cổng 1 — Evidence đối tác
- LKHDG_16 (Sửa): "Các trường thông tin không được chỉnh sửa" + "Breadcrumb hiển thị Chi tiết".
- LKHDG_20 (Hủy): "không hiển thị cửa sổ xác nhận" + "Màn chỉnh sửa không có nút chức năng".
- LKHDG_21 (Lưu nháp): "Màn chỉnh sửa không có nút chức năng".
- LKHDG_22 (Lưu & Chuyển tiêu chí): "Màn chỉnh sửa không có nút chức năng".

## Cổng 2 — Hiểu bug
- Cả 4 xoay quanh màn Edit. Deterministic (không phụ thuộc data combinatorial); cần đợt ở trạng thái LAP_KE_HOACH/PHAN_CONG để nút Sửa hiện.

## Cổng 3 — Đối chiếu SRS vs web (env 18.143, cbnv_tw, đợt DG-20260720-0002 LAP_KE_HOACH)
| Mục | SRS | Web thực tế | Kết luận |
|---|---|---|---|
| Nút Sửa hiện | SCR-VI-01 #18 (dòng 827): "Sửa (chỉ LAP_KE_HOACH/PHAN_CONG)" | Icon Sửa hiện đúng ở đợt Lập kế hoạch | ĐẠT |
| Sửa mở form chỉnh sửa | SCR-VI-01 "Form tạo/**sửa** đợt" (dòng 831-840) + AC (dòng 158): "chỉnh sửa KH chưa duyệt → thay đổi → validate + lưu" | Bấm Sửa → điều hướng URL chi tiết, trường read-only, KHÔNG sửa được | SAI — không mở form sửa |
| Breadcrumb | Màn Sửa (chỉnh sửa) | "Trang chủ / Đánh giá hiệu quả / Kế hoạch đánh giá / **Chi tiết**" | SAI (LKHDG_16) |
| Nút [Hủy] form | SCR-VI-01 #27 (dòng 841): "[Hủy] ..." → hủy bỏ thay đổi, đóng form, về danh sách | Không có [Hủy] của form (chỉ "Hủy đợt" = chuyển state HUY, khác) | SAI (LKHDG_20) |
| Nút [Lưu nháp] | SCR-VI-01 #27 (dòng 841): "[Lưu nháp]" | Không có | SAI (LKHDG_21) |
| Nút [Lưu & Chuyển tiêu chí] | SCR-VI-01 #27 (dòng 841): "[Lưu & Chuyển tiêu chí]" | Không có (cho việc sửa đợt) | SAI (LKHDG_22) |

## Verdict: Open — BUG-LKHDG-EDIT (Major/P1)
- Chức năng Sửa đợt (LAP_KE_HOACH/PHAN_CONG) không hoạt động: mở màn chi tiết read-only thay vì form chỉnh sửa. Không thể sửa thông tin đợt, không có thanh hành động form → vi phạm AC dòng 158 + Form sửa dòng 831-841 + Hành động Sửa dòng 827.
- Evidence: `web-sua-mo-chitiet-readonly.png` (breadcrumb "Chi tiết", đợt info read-only, chỉ có "Quay lại danh sách"/"Hủy đợt").
- Bug-report: `bug-reports/Pass-bug-report-DGHQ-batchA.md` (BUG-LKHDG-EDIT).
