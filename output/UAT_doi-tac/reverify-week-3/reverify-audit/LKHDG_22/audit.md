# Audit — LKHDG_22 (row 54) · Verdict: Open (BUG-LKHDG-EDIT)

Cùng gốc với LKHDG_16/20/21 — chi tiết đầy đủ tại `reverify-audit/LKHDG_16/audit.md`.

- Đối tác: màn chỉnh sửa không có nút "Lưu & Chuyển tiêu chí".
- Verify (cbnv_tw, đợt DG-20260720-0002 LAP_KE_HOACH): bấm Sửa → màn chi tiết read-only, không có nút [Lưu & Chuyển tiêu chí] cho sửa thông tin đợt.
- SRS SCR-VI-01 #27 (dòng 841): form phải có nút [Lưu & Chuyển tiêu chí] (→ lưu + mở tab tiêu chí). → Open.
- Evidence: `../LKHDG_16/web-sua-mo-chitiet-readonly.png`.
