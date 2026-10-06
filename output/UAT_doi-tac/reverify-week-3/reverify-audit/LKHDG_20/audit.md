# Audit — LKHDG_20 (row 52) · Verdict: Open (BUG-LKHDG-EDIT)

Cùng gốc với LKHDG_16/21/22 — chi tiết đầy đủ tại `reverify-audit/LKHDG_16/audit.md`.

- Đối tác: nút "Hủy" trên màn chỉnh sửa không hiện cửa sổ xác nhận + màn chỉnh sửa không có nút chức năng.
- Verify (cbnv_tw, đợt DG-20260720-0002 LAP_KE_HOACH): bấm Sửa → màn chi tiết read-only, không có nút [Hủy] của form (chỉ "Hủy đợt" = chuyển state HUY, khác nghiệp vụ).
- SRS SCR-VI-01 #27 (dòng 841): form phải có nút [Hủy] → hủy bỏ thay đổi + đóng form + về danh sách. → Open.
- Evidence: `../LKHDG_16/web-sua-mo-chitiet-readonly.png`.
