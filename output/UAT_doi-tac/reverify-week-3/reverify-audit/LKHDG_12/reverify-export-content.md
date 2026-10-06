# Re-verify LKHDG_12 — Nội dung file Xuất Excel (2026-07-23 R2)

Đọc trực tiếp cell values từ blob `.xlsx` sinh client-side (env test 18.143, cbnv_tw). File gốc: `reverify-export-danhsach-dot.xlsx` (size 7375 bytes).

## Header (A1:J1, 10 cột — bug gốc chỉ 7)

```
Mã KH | Tên đợt | Tần suất | Đối tượng | Số vụ việc | Từ ngày | Đến ngày | Trạng thái | Người tạo | Ngày tạo
```

→ Đã thêm 3 cột trước đây thiếu: **Số vụ việc**, **Người tạo**, **Ngày tạo**.

## Dòng dữ liệu (7 đợt, nhãn tiếng Việt — bug gốc ghi mã enum thô)

```
DG-20260722-0002 | QA-THDG05-multiassessor-test        | Trọn năm | Vụ việc | 2 | 1/1/2026 | 31/12/2026 | Đang đánh giá | CB Nghiệp vụ - Trung ương | 08:13 22/7/26
DG-20260722-0001 | QA-THDG05-partial-save-test         | Trọn năm | Vụ việc | 3 | 1/1/2026 | 31/12/2026 | Đang đánh giá | CB Nghiệp vụ - Trung ương | 07:35 22/7/26
DG-20260720-0004 | DGHQ-B3-20260720 ky rong khong VV   | Trọn năm | Vụ việc | 0 | 1/1/2024 | 31/3/2024  | Thực hiện     | QA CB Nghiep vu Ha Noi    | 13:20 20/7/26
DG-20260720-0003 | DGHQ-B2-20260720 trung dot va cham diem | Trọn năm | Vụ việc | 1 | 1/1/2026 | 31/12/2026 | Đang đánh giá | QA CB Nghiep vu Ha Noi | 13:19 20/7/26
DG-20260720-0002 | QA-LKHDG-Test-LapKeHoach-20260720   | Trọn năm | Vụ việc | 0 | 1/8/2026 | 31/12/2026 | Thực hiện     | CB Nghiệp vụ - Trung ương | 12:19 20/7/26
DG-20260720-0001 | DGHQ-B1-20260720 Batch B downstream | Trọn năm | Vụ việc | 1 | 1/1/2026 | 31/12/2026 | Hoàn thành    | QA CB Nghiep vu Ha Noi    | 11:22 20/7/26
KHDG-SEED-0001   | Đợt đánh giá seed 2026              | Trọn năm | Vụ việc | 0 | 1/1/2026 | 30/6/2026  | Hoàn thành    | Hệ thống HTPLDN           | 12:28 30/6/26
```

## Kết luận

- Facet (1) — thiếu cột: **FIXED**. File có đủ 10 cột gồm Số vụ việc/Người tạo/Ngày tạo.
- Facet (2) — mã enum thô: **FIXED**. Tần suất/Đối tượng/Trạng thái đều là nhãn tiếng Việt ("Trọn năm", "Vụ việc", "Đang đánh giá"/"Thực hiện"/"Hoàn thành"), không còn `TRON_NAM`/`VU_VIEC`/`LAP_KE_HOACH`.

→ **PASS.**
