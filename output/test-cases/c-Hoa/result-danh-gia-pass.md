# Test Cases PASS — danh-gia
> **Nguồn**: result-danh-gia-all.md
> **Ngày tổng hợp**: 2026-05-11
> **Phạm vi**: chỉ Result ∈ {PASS, PASS-DEVIATE, PASS-RESOLVED}

## Summary

| File test-case | Total PASS | PASS | PASS-DEVIATE | PASS-RESOLVED |
|----------------|-----------:|-----:|-------------:|--------------:|
| 01-TC-FR-VI-01-lap-ke-hoach | 2 | 1 | 1 | 0 |
| 02-TC-FR-VI-02-thiet-lap-tieu-chi | 3 | 2 | 1 | 0 |
| 03-TC-FR-VI-03-04-phan-cong-duyet-pc | 1 | 1 | 0 | 0 |
| **Tổng** | **6** | **4** | **2** | **0** |

> **Lưu ý mapping cột**: file test-case dùng 7 cột (`TC ID / Mô tả / Pre-condition / Steps / Expected / Priority / BR/AC/ERR`). Output map sang 10 cột với `Test Data` = phần data có trong Pre-condition (giữ NGUYÊN VĂN), `TraceID (Mã SRS)` = cột `BR/AC/ERR`, `Type` = cột `Priority`. Cột `Chi tiết` để trống cho PASS/PASS-DEVIATE.

---

## 01-TC-FR-VI-01-lap-ke-hoach

> Source TC: `c:\HoaAG\LuatDN5\Ver3.1\output\test-cases\danh-gia\01-TC-FR-VI-01-lap-ke-hoach.md`
> Source report: `c:\HoaAG\LuatDN5\Ver3.1\output\execution-test\danh-gia\report-01-TC-FR-VI-01-lap-ke-hoach\Tcs-report\01-TC-FR-VI-01-lap-ke-hoach-execution-report-2026-05-11.md`

| ID | TraceID (Mã SRS) | Tên Test Case | Pre-conditions (Tiền đề) | Test Data (Dữ liệu) | Các bước thực hiện | Kết quả mong đợi | Type (Happy/Negative/Edge) | Kết quả test (Result) | Chi tiết |
|----|------------------|---------------|--------------------------|---------------------|--------------------|------------------|----------------------------|-----------------------|----------|
| TC-DG-KH-007 | ERR-DG-KH-01, AC E1 | Tạo đợt — thiếu nhiều trường bắt buộc → ERR-DG-KH-01 | Login. |  | 1. Click [+ Tạo đợt]<br>2. Để trống `ten_dot` + `muc_tieu`<br>3. Click [Lưu nháp] | Form không submit. Inline error trên 2 trường + toast NGUYÊN VĂN "Vui lòng nhập đầy đủ thông tin bắt buộc" (ERR-DG-KH-01) | High | PASS-DEVIATE |  |
| TC-DG-KH-009 | BR-LEGAL-08 | Tạo đợt — `tan_suat` chỉ chấp nhận `SO_BO_6_THANG` / `TRON_NAM` (BR-LEGAL-08) | Login. |  | 1. Mở dropdown tần suất | Dropdown chỉ có 2 option (KHÔNG có DOT_XUAT). Verify per BR-LEGAL-08 | Critical | PASS |  |

---

## 02-TC-FR-VI-02-thiet-lap-tieu-chi

> Source TC: `c:\HoaAG\LuatDN5\Ver3.1\output\test-cases\danh-gia\02-TC-FR-VI-02-thiet-lap-tieu-chi.md`
> Source report: `c:\HoaAG\LuatDN5\Ver3.1\output\execution-test\danh-gia\report-02-TC-FR-VI-02-thiet-lap-tieu-chi\Tcs-report\02-TC-FR-VI-02-thiet-lap-tieu-chi-execution-report-2026-05-11.md`

| ID | TraceID (Mã SRS) | Tên Test Case | Pre-conditions (Tiền đề) | Test Data (Dữ liệu) | Các bước thực hiện | Kết quả mong đợi | Type (Happy/Negative/Edge) | Kết quả test (Result) | Chi tiết |
|----|------------------|---------------|--------------------------|---------------------|--------------------|------------------|----------------------------|-----------------------|----------|
| TC-DG-TC-001 | SCR row #28-29 | Mở Tab Tiêu chí — bảng inline editable | Login `cb_nv_tw_01`. Đợt LAP_KE_HOACH (DG-20260502-0001). | Đợt DG-20260502-0001 | 1. Mở chi tiết đợt<br>2. Tab "Tiêu chí" | Tab hiển thị bảng cột: STT / Tên tiêu chí / Mô tả / Trọng số % / Điểm tối đa / Thứ tự / Hành động. Header info card hiển thị mã đợt + kỳ + đối tượng | High | PASS-DEVIATE |  |
| TC-DG-TC-004 | SCR row #30-31, ERR-DG-TC-01 | Cảnh báo realtime khi `SUM != 100%` | Login. Tổng đang = 100%. | Tổng 100% → sửa thành 110% | 1. Sửa trong_so tiêu chí 1 từ 40 → 50 | Tổng "110%" — màu đỏ. Banner WRN-TC-01 hiển thị "Tổng trọng số hiện tại: 110%. Cần đảm bảo = 100%" | High | PASS |  |
| TC-DG-TC-017 | ERR-DG-TC-02, AC E2 | Thiếu `ten_tieu_chi` khi lưu → ERR-DG-TC-02 (P0 F-001) | Login. Tab Tiêu chí mở. | trong_so=10, diem_toi_da=5, ten_tieu_chi trống | 1. Click [+ Thêm tiêu chí]<br>2. Để trống ten_tieu_chi<br>3. Save | Inline error + toast NGUYÊN VĂN "Vui lòng nhập tên tiêu chí" (ERR-DG-TC-02) | Critical | PASS |  |

---

## 03-TC-FR-VI-03-04-phan-cong-duyet-pc

> Source TC: `c:\HoaAG\LuatDN5\Ver3.1\output\test-cases\danh-gia\03-TC-FR-VI-03-04-phan-cong-duyet-pc.md`
> Source report: `c:\HoaAG\LuatDN5\Ver3.1\output\execution-test\danh-gia\report-03-TC-FR-VI-03-04-phan-cong-duyet-pc\Tcs-report\03-TC-FR-VI-03-04-phan-cong-duyet-pc-execution-report-2026-05-11.md`

| ID | TraceID (Mã SRS) | Tên Test Case | Pre-conditions (Tiền đề) | Test Data (Dữ liệu) | Các bước thực hiện | Kết quả mong đợi | Type (Happy/Negative/Edge) | Kết quả test (Result) | Chi tiết |
|----|------------------|---------------|--------------------------|---------------------|--------------------|------------------|----------------------------|-----------------------|----------|
| TC-DG-PC-001 | SCR row #35-36 | Mở Tab Phân công — bảng inline editable | Login `cb_nv_tw_01`. Đợt LAP_KE_HOACH có tiêu chí 100%. | Đợt LAP_KE_HOACH tiêu chí 100% | 1. Mở chi tiết đợt<br>2. Tab "Phân công" | Tab hiển thị bảng cột: Người ĐG / Vai trò / Lĩnh vực phụ trách / Ghi chú / Hành động + info card đợt | High | PASS |  |

---

## Skipped

Các section không có TC PASS/PASS-DEVIATE/PASS-RESOLVED:

- **04-TC-FR-VI-05-06-chon-vv-cham-diem** — 29 TC toàn bộ DEFERRED (chain dependency).
- **05-TC-FR-VI-07-08-09-bao-cao-trinh-duyet** — 32 TC toàn bộ DEFERRED (chain dependency).
- **06-TC-FR-VI-10-nhan-ket-qua** — 8 TC toàn bộ DEFERRED (chain dependency).
- **07-TC-permission-matrix** — 16 TC toàn bộ DEFERRED (multi-role chain + rate limit).
