# Test Cases PASS — hoi-dap

> **Nguồn**: result-hoi-dap-all.md
> **Ngày tổng hợp**: 2026-05-11
> **Phạm vi**: chỉ Result ∈ {PASS, PASS-DEVIATE, PASS-RESOLVED}

## Summary

| File test-case | Total PASS | PASS | PASS-DEVIATE | PASS-RESOLVED |
|----------------|------------|------|--------------|---------------|
| 01-TC-quan-ly-hoi-dap         | 3 | 3 | 0 | 0 |
| 02-TC-tim-kiem-tong-hop       | 1 | 1 | 0 | 0 |
| 03-TC-tiep-nhan-xu-ly         | 1 | 1 | 0 | 0 |
| 04-TC-quan-ly-tiep-nhan       | 1 | 1 | 0 | 0 |
| 05-TC-phan-cong-xu-ly         | 1 | 1 | 0 | 0 |
| 06-TC-phan-hoi-cau-hoi        | 1 | 1 | 0 | 0 |
| **Tổng**                      | **8** | **8** | **0** | **0** |

---

## 01-TC-quan-ly-hoi-dap

> Source TC: `c:\HoaAG\LuatDN5\Ver3.1\output\test-cases\hoi-dap\01-TC-quan-ly-hoi-dap.md`
> Source report: `c:\HoaAG\LuatDN5\Ver3.1\output\execution-test\hoi-dap\report-01-TC-quan-ly-hoi-dap\Tcs-report\01-TC-quan-ly-hoi-dap-execution-report-2026-05-10.md`

| ID | TraceID (Mã SRS) | Tên Test Case | Pre-conditions (Tiền đề) | Test Data (Dữ liệu) | Các bước thực hiện | Kết quả mong đợi | Type (Happy/Negative/Edge) | Kết quả test (Result) | Chi tiết |
|----|------------------|---------------|--------------------------|---------------------|--------------------|------------------|----------------------------|------------------------|----------|
| TC-HD-001 | FR-II-01 / Processing Thêm mới step 2-10 | Tạo HOI_DAP mới — happy THUONG | cb_nv_tw_01 login. Lĩnh vực "Đất đai" tồn tại (UC99). | noi_dung="Thủ tục cấp sổ đỏ?", linh_vuc=Đất đai, kenh=TRUC_TIEP, muc_do_phuc_tap=THUONG | 1. SCR-II-01 click [+ Thêm mới]. 2. Drawer mở. 3. Nhập đủ trường bắt buộc. 4. Click [Lưu]. | (1) POST /hoi-dap thành công 201. (2) Drawer đóng + toast "Đã tạo HOI_DAP {ma}". (3) Danh sách reload, record mới có `ma=HD-YYYYMMDD-SEQ`, `trang_thai=MOI`, `don_vi_id=cb_nv_tw_01.don_vi_id` (TW), `muc_do_phuc_tap=THUONG`. (4) Audit log INSERT (BR-DATA-05). | Happy | PASS |  |
| TC-HD-005 | FR-II-01 / AC #1 + BR-AUTH-08 | Hiển thị danh sách scope đơn vị + phân trang | cb_nv_dp_01 (Sở TP AG) login. ≥25 HOI_DAP thuộc AG, 5 thuộc Sở TP BG. | — | 1. Truy cập SCR-II-01. | (3) Danh sách 20 records/page (BR-DATA-07), CHỈ scope AG (BR-AUTH-08). 5 record BG KHÔNG hiển thị. Pagination footer "Hiển thị 1-20 / 25 kết quả". | Happy | PASS |  |
| TC-HD-204 | FR-II-01 / Inputs #8 | TVN_BRIDGE auto-set, không cho user nhập tay | cb_nv_tw_01 login. | — | 1. Mở Form Thêm mới. 2. Verify dropdown Kênh tiếp nhận chỉ có 4 options (DVC/CONG_PLQG/TRUC_TIEP/HE_THONG_KHAC). | (2) TVN_BRIDGE KHÔNG hiển thị trong dropdown (auto-set khi escalate từ FR-13). | Edge | PASS |  |

---

## 02-TC-tim-kiem-tong-hop

> Source TC: `c:\HoaAG\LuatDN5\Ver3.1\output\test-cases\hoi-dap\02-TC-tim-kiem-tong-hop.md`
> Source report: `c:\HoaAG\LuatDN5\Ver3.1\output\execution-test\hoi-dap\report-02-TC-tim-kiem-tong-hop\Tcs-report\02-TC-tim-kiem-tong-hop-execution-report-2026-05-10.md`

| ID | TraceID (Mã SRS) | Tên Test Case | Pre-conditions (Tiền đề) | Test Data (Dữ liệu) | Các bước thực hiện | Kết quả mong đợi | Type (Happy/Negative/Edge) | Kết quả test (Result) | Chi tiết |
|----|------------------|---------------|--------------------------|---------------------|--------------------|------------------|----------------------------|------------------------|----------|
| TC-HDTK-010 | FR-II-05 / AC #1 + filter cứng | Tab "Đang xử lý" filter cứng IN(TIEP_NHAN, DANG_XU_LY) | cb_nv_tw_01 login. HD seed: 3 MOI + 5 TIEP_NHAN + 7 DANG_XU_LY + 2 CHO_PHE_DUYET. | — | 1. Click tab "Đang xử lý". | (3) Hiển thị 12 records (5+7), KHÔNG hiển thị MOI/CHO_PD. Tab badge "(12)". | Happy | PASS |  |

---

## 03-TC-tiep-nhan-xu-ly

> Source TC: `c:\HoaAG\LuatDN5\Ver3.1\output\test-cases\hoi-dap\03-TC-tiep-nhan-xu-ly.md`
> Source report: `c:\HoaAG\LuatDN5\Ver3.1\output\execution-test\hoi-dap\report-03-TC-tiep-nhan-xu-ly\Tcs-report\03-TC-tiep-nhan-xu-ly-execution-report-2026-05-10.md`

| ID | TraceID (Mã SRS) | Tên Test Case | Pre-conditions (Tiền đề) | Test Data (Dữ liệu) | Các bước thực hiện | Kết quả mong đợi | Type (Happy/Negative/Edge) | Kết quả test (Result) | Chi tiết |
|----|------------------|---------------|--------------------------|---------------------|--------------------|------------------|----------------------------|------------------------|----------|
| TC-TN-001 | FR-II-03 / AC #2 + BR-CALC-03 (THUONG) | Tiếp nhận MOI → TIEP_NHAN với muc_do_phuc_tap=THUONG → deadline +15 ngày LV | cb_nv_tw_01 login. HD-X state MOI, muc_do_phuc_tap=THUONG, ngay_tao=2026-04-15 (Thứ Tư). CAU_HINH_SLA[HOI_DAP_THUONG]=15. | — | 1. Mở SCR-II-02 HD-X. 2. Click [Tiếp nhận]. 3. Modal mở (ghi_chu trống OK). 4. Click [Xác nhận tiếp nhận]. | (1) PUT /hoi-dap/{id}/tiep-nhan thành công. (2) Modal đóng + toast "Đã tiếp nhận". (3) State badge → "Tiếp nhận" (xanh lá). `nguoi_tiep_nhan_id=cb_nv_tw_01`, `ngay_tiep_nhan=NOW()`, `deadline = ngay_tiep_nhan + 15 ngày LV`. (4) Audit log INSERT action='TIEP_NHAN'. | Happy | PASS |  |

---

## 04-TC-quan-ly-tiep-nhan

> Source TC: `c:\HoaAG\LuatDN5\Ver3.1\output\test-cases\hoi-dap\04-TC-quan-ly-tiep-nhan.md`
> Source report: `c:\HoaAG\LuatDN5\Ver3.1\output\execution-test\hoi-dap\report-04-TC-quan-ly-tiep-nhan\Tcs-report\04-TC-quan-ly-tiep-nhan-execution-report-2026-05-10.md`

| ID | TraceID (Mã SRS) | Tên Test Case | Pre-conditions (Tiền đề) | Test Data (Dữ liệu) | Các bước thực hiện | Kết quả mong đợi | Type (Happy/Negative/Edge) | Kết quả test (Result) | Chi tiết |
|----|------------------|---------------|--------------------------|---------------------|--------------------|------------------|----------------------------|------------------------|----------|
| TC-DXL-003 | FR-II-04 / Filter cứng | Tab "Đang xử lý" filter cứng + filter user | cb_nv_tw_01 login. ≥10 HD scope TW: 4 TIEP_NHAN + 6 DANG_XU_LY + 3 khác state. | linh_vuc=Đất đai filter user thêm | 1. Tab "Đang xử lý". 2. Apply filter Lĩnh vực. | (3) AND logic: 10 records (TIEP_NHAN OR DANG_XU_LY) + thêm filter user → giảm scope. URL `?tab=dang-xu-ly&linh_vuc=...`. | Happy | PASS |  |

---

## 05-TC-phan-cong-xu-ly

> Source TC: `c:\HoaAG\LuatDN5\Ver3.1\output\test-cases\hoi-dap\05-TC-phan-cong-xu-ly.md`
> Source report: `c:\HoaAG\LuatDN5\Ver3.1\output\execution-test\hoi-dap\report-05-TC-phan-cong-xu-ly\Tcs-report\05-TC-phan-cong-xu-ly-execution-report-2026-05-10.md`

| ID | TraceID (Mã SRS) | Tên Test Case | Pre-conditions (Tiền đề) | Test Data (Dữ liệu) | Các bước thực hiện | Kết quả mong đợi | Type (Happy/Negative/Edge) | Kết quả test (Result) | Chi tiết |
|----|------------------|---------------|--------------------------|---------------------|--------------------|------------------|----------------------------|------------------------|----------|
| TC-PC-001 | FR-II-06 / AC #2 + Processing step 5 (auto-filter) | Phân công TVV cá nhân tự do — happy | cb_nv_tw_01 login. HD-X TIEP_NHAN, linh_vuc=Đất đai. ≥3 TVV cá nhân (`to_chuc_chinh_id IS NULL`) HOAT_DONG có `linh_vuc_chuyen_mon` chứa Đất đai trong scope TW. | tab=Cá nhân, nguoi_xu_ly=TVV-001 | 1. SCR-II-02 HD-X. 2. Click [Phân công] dòng 10. 3. Modal SCR-II-03 mở. 4. Tab "Cá nhân tự do" mặc định active. 5. Bảng gợi ý 4a hiển thị ≥3 TVV theo workload ASC. 6. Click radio TVV-001. 7. nguoi_xu_ly auto-fill. 8. Click [Phân công]. | (1) PUT /hoi-dap/{id}/phan-cong thành công. (3) Modal đóng + toast "Đã phân công cho TVV-001". (4) HD: `loai_doi_tuong_xu_ly=CA_NHAN`, `nguoi_phan_cong_id=TVV-001`, `to_chuc_tu_van_id=NULL`, `trang_thai=DANG_XU_LY`. (5) Notification in-app + email cho TVV-001 (BR-DATA-05). | Happy | PASS |  |

---

## 06-TC-phan-hoi-cau-hoi

> Source TC: `c:\HoaAG\LuatDN5\Ver3.1\output\test-cases\hoi-dap\06-TC-phan-hoi-cau-hoi.md`
> Source report: `c:\HoaAG\LuatDN5\Ver3.1\output\execution-test\hoi-dap\report-06-TC-phan-hoi-cau-hoi\Tcs-report\06-TC-phan-hoi-cau-hoi-execution-report-2026-05-10.md`

| ID | TraceID (Mã SRS) | Tên Test Case | Pre-conditions (Tiền đề) | Test Data (Dữ liệu) | Các bước thực hiện | Kết quả mong đợi | Type (Happy/Negative/Edge) | Kết quả test (Result) | Chi tiết |
|----|------------------|---------------|--------------------------|---------------------|--------------------|------------------|----------------------------|------------------------|----------|
| TC-PH-001 | FR-II-07 / AC #1 | Mở form phản hồi từ SCR-II-02 | cb_nv_tw_01 login. HD-X DANG_XU_LY, đã phân công cho cb_nv_tw_01. | — | 1. SCR-II-02 HD-X. 2. Click [Soạn phản hồi] dòng 11. | (3) Cuộn đến form phản hồi (rich-text editor + dropdown chèn mẫu + checkbox + nút Lưu nháp + Gửi). Khối thông tin câu hỏi gốc accordion mở. | Happy | PASS |  |

---

## Skipped

- **07-TC-phe-duyet-cong-khai**: 0 TC PASS. Toàn bộ 38 TC BLOCKED do env không có records state CHO_PHE_DUYET hoặc CONG_KHAI. Dependency chain: TC-PH-005 BUG → CHO_PHE_DUYET seed gap. Cần fix BUG-HD-001 + BUG-PC-001 + BUG-PH-001, seed ≥5 CHO_PHE_DUYET, setup mock API Cổng PLQG.
