# Test Cases PASS — ct-htpldn-gd2

> **Nguồn**: result-ct-htpldn-gd2-all.md
> **Ngày tổng hợp**: 2026-05-11
> **Phạm vi**: chỉ Result ∈ {PASS, PASS-DEVIATE, PASS-RESOLVED}

## Summary

| File test-case | Total TC PASS | PASS | PASS-DEVIATE | PASS-RESOLVED |
|----------------|--------------:|-----:|-------------:|--------------:|
| 01-TC-bat-dau-lap-bc | 2 | 2 | 0 | 0 |
| 02-TC-lap-bao-cao-kq | 1 | 1 | 0 | 0 |
| 03-TC-trinh-phe-duyet-bc | 2 | 2 | 0 | 0 |
| 04-TC-phe-duyet-bc | 3 | 3 | 0 | 0 |
| 05-TC-gui-len-tw | 2 | 2 | 0 | 0 |
| 06-TC-tw-tong-hop-bc | 1 | 1 | 0 | 0 |
| 07-TC-permission-matrix | 3 | 3 | 0 | 0 |
| **Tổng** | **14** | **14** | **0** | **0** |

---

## 01-TC-bat-dau-lap-bc

> Source TC: `c:\HoaAG\LuatDN5\Ver3.1\output\test-cases\ct-htpldn-gd2\01-TC-bat-dau-lap-bc.md`
> Source report: `c:\HoaAG\LuatDN5\Ver3.1\output\execution-test\ct-htpldn-gd2\report-01-bat-dau-lap-bc\Tcs-report\tcs-report.md`

| ID | TraceID (Mã SRS) | Tên Test Case | Pre-conditions (Tiền đề) | Test Data (Dữ liệu) | Các bước thực hiện | Kết quả mong đợi | Type (Happy/Negative/Edge) | Kết quả test (Result) | Chi tiết |
|----|------------------|---------------|--------------------------|---------------------|--------------------|------------------|----------------------------|------------------------|----------|
| TC-LBC-001 | SM-DOT-BC / TAO_DOT → DANG_LAP_BC | Bắt đầu lập BC happy path | cb_nv_tw_01 login. CT-TW01 DANG_THUC_HIEN. Đợt DOT-CTW01-001 ở TAO_DOT. | — | 1. Mở chi tiết CT-TW01 → Tab "Đợt báo cáo". 2. Click row DOT-CTW01-001 → drill-down. 3. Click [Bắt đầu lập BC]. | (3) PATCH `/api/v1/dot-bao-cao/{id}/start-lap-bc` 200. (3) Đợt BC trạng thái = `DANG_LAP_BC`, badge đổi màu `--color-warning`. (3) BAO_CAO_CT_HTPL record mới tạo (`ma_bao_cao` auto-gen, `ct_htpl_id`=CT-TW01.id, `trang_thai`=DU_THAO, `ky_bao_cao` đồng bộ từ đợt). (3) Form 21a/21b render editable. (3) Audit log INSERT BAO_CAO_CT_HTPL + UPDATE DOT_BAO_CAO (BR-DATA-05). | Happy 🔴 | PASS |  |
| TC-LBC-010 | SM-DOT-BC / Đợt ≠ TAO_DOT | Bắt đầu lập BC khi đợt ≠ TAO_DOT | cb_nv_tw_01 login. Đợt DOT-CTW01-010 đã ở DANG_LAP_BC. | — | 1. Drill-down. 2. Click [Bắt đầu lập BC]. | (1) Nút [Bắt đầu lập BC] **ẩn** vì đợt đã DANG_LAP_BC HOẶC backend reject 400 với toast "Đợt BC không ở trạng thái TAO_DOT" (transition guard). KHÔNG tạo BC trùng. | Negative 🔴 | PASS |  |

---

## 02-TC-lap-bao-cao-kq

> Source TC: `c:\HoaAG\LuatDN5\Ver3.1\output\test-cases\ct-htpldn-gd2\02-TC-lap-bao-cao-kq.md`
> Source report: `c:\HoaAG\LuatDN5\Ver3.1\output\execution-test\ct-htpldn-gd2\report-02-lap-bao-cao-kq\Tcs-report\tcs-report.md`

| ID | TraceID (Mã SRS) | Tên Test Case | Pre-conditions (Tiền đề) | Test Data (Dữ liệu) | Các bước thực hiện | Kết quả mong đợi | Type (Happy/Negative/Edge) | Kết quả test (Result) | Chi tiết |
|----|------------------|---------------|--------------------------|---------------------|--------------------|------------------|----------------------------|------------------------|----------|
| TC-BC-001 | FR-XI-06 / Processing step 4-5 | Lập BC happy path nhập tay | cb_nv_tw_01 login. Đợt DOT-CTW01-001 DANG_LAP_BC, biểu mẫu MAU_21A. | so_lieu (cột 21a): 5 dòng dữ liệu cơ bản; nhan_xet="Hoàn thành tốt 80% mục tiêu Q1." | 1. Drill-down đợt. 2. Nhập số liệu vào editable table 21a (5 cột × 5 dòng). 3. Nhập nhận xét. 4. Click [Lưu nháp]. | (4) PUT `/api/v1/bao-cao-ct/{id}` 200. (4) Toast "Lưu nháp thành công". (4) `so_lieu_tong_hop` = JSON serialize đúng cấu trúc 21a. (4) Reload page → render lại đúng dữ liệu. (4) `trang_thai`=DU_THAO. Audit log UPDATE (BR-DATA-05). | Happy 🔴 | PASS |  |

---

## 03-TC-trinh-phe-duyet-bc

> Source TC: `c:\HoaAG\LuatDN5\Ver3.1\output\test-cases\ct-htpldn-gd2\03-TC-trinh-phe-duyet-bc.md`
> Source report: `c:\HoaAG\LuatDN5\Ver3.1\output\execution-test\ct-htpldn-gd2\report-03-trinh-pd-bc\Tcs-report\tcs-report.md`

| ID | TraceID (Mã SRS) | Tên Test Case | Pre-conditions (Tiền đề) | Test Data (Dữ liệu) | Các bước thực hiện | Kết quả mong đợi | Type (Happy/Negative/Edge) | Kết quả test (Result) | Chi tiết |
|----|------------------|---------------|--------------------------|---------------------|--------------------|------------------|----------------------------|------------------------|----------|
| TC-TPD-001 | SM-DOT-BC + SM-BC sub / DANG_LAP_BC → CHO_DUYET_KQ + DU_THAO → CHO_PHE_DUYET | Trình PD BC happy path | cb_nv_tw_01 login. Đợt DOT-CTW01-001 DANG_LAP_BC, BC DU_THAO đầy đủ số liệu. Có ≥1 cb_pd_tw_01 active. | — | 1. Drill-down. 2. Click [Trình duyệt KQ]. 3. Modal xác nhận → OK. | (2) PATCH `/api/v1/dot-bao-cao/{id}/trinh-duyet` 200. (3) Đợt BC = `CHO_DUYET_KQ` (badge vàng đậm). (3) BC = `CHO_PHE_DUYET`. (3) Thanh tiến trình SM-DOT-BC highlight CHO_DUYET_KQ. (3) MCP `list_network_requests` thấy POST `/notifications` outbound (gửi CB PD cùng cấp). Audit log INSERT 2 entry (UPDATE cả đợt và BC) với `action_type=TRANSITION` (BR-DATA-05). | Happy 🔴 | PASS |  |
| TC-TPD-011 | SM-DOT-BC / Đợt ≠ DANG_LAP_BC | Trình PD khi đợt đã CHO_DUYET_KQ | cb_nv_tw_01 login. Đợt DOT-CTW01-011 CHO_DUYET_KQ. | — | 1. Drill-down. | (1) Nút [Trình duyệt KQ] **ẩn**. KHÔNG cho re-trigger. | Negative 🔴 | PASS |  |

---

## 04-TC-phe-duyet-bc

> Source TC: `c:\HoaAG\LuatDN5\Ver3.1\output\test-cases\ct-htpldn-gd2\04-TC-phe-duyet-bc.md`
> Source report: `c:\HoaAG\LuatDN5\Ver3.1\output\execution-test\ct-htpldn-gd2\report-04-phe-duyet-bc\Tcs-report\tcs-report.md`

| ID | TraceID (Mã SRS) | Tên Test Case | Pre-conditions (Tiền đề) | Test Data (Dữ liệu) | Các bước thực hiện | Kết quả mong đợi | Type (Happy/Negative/Edge) | Kết quả test (Result) | Chi tiết |
|----|------------------|---------------|--------------------------|---------------------|--------------------|------------------|----------------------------|------------------------|----------|
| TC-PD-BC-001 | SM-DOT-BC + SM-BC sub / CHO_DUYET_KQ → DA_DUYET_KQ + CHO_PHE_DUYET → DA_DUYET | Phê duyệt BC happy path | cb_pd_tw_01 login. Đợt DOT-CTW01-001 CHO_DUYET_KQ, BC CHO_PHE_DUYET, do cb_nv_tw_01 trình. | ghi_chu_phe_duyet="OK" | 1. Drill-down. 2. Click [Phê duyệt]. 3. Modal xác nhận → nhập ghi chú → OK. | (2) PATCH `/api/v1/bao-cao-ct/{id}/phe-duyet` 200. (3) Đợt BC = `DA_DUYET_KQ` (badge xanh lá). (3) BC = `DA_DUYET`. (3) Notification gửi cb_nv_tw_01 với "Có thể gửi lên TW". (3) Nút [Gửi lên TW] enable cho CB NV. Audit log INSERT (BR-DATA-05). | Happy 🔴 | PASS |  |
| TC-PD-BC-002 | FR-XI-07a / Inputs#4 — ghi_chu optional | Phê duyệt không nhập ghi chú | cb_pd_tw_01 login. Đợt DOT-CTW01-002 CHO_DUYET_KQ. | ghi_chu_phe_duyet="" | 1. Drill-down. 2. Click [Phê duyệt]. 3. Modal → để trống ghi chú → OK. | (3) PASS — ghi_chu là optional. Duyệt thành công. | Happy 🟢 | PASS |  |
| TC-PD-BC-010 | FR-XI-07a / E1 ERR-XI-07a-01 (Codex CT-GD2-07 rename) | Duyệt thất bại khi DOT_BAO_CAO không ở trạng thái CHO_DUYET_KQ | cb_pd_tw_01 login. Đợt DOT-CTW01-010 đã DA_DUYET_KQ. | — | 1. Drill-down. 2. Click [Phê duyệt] (nếu còn nút). | (1) Nút [Phê duyệt] **ẩn** vì đợt đã duyệt. HOẶC backend reject 400 với **"BC không ở trạng thái chờ duyệt kết quả"** (ERR-XI-07a-01). | Negative 🔴 | PASS |  |

---

## 05-TC-gui-len-tw

> Source TC: `c:\HoaAG\LuatDN5\Ver3.1\output\test-cases\ct-htpldn-gd2\05-TC-gui-len-tw.md`
> Source report: `c:\HoaAG\LuatDN5\Ver3.1\output\execution-test\ct-htpldn-gd2\report-05-gui-len-tw\Tcs-report\tcs-report.md`

| ID | TraceID (Mã SRS) | Tên Test Case | Pre-conditions (Tiền đề) | Test Data (Dữ liệu) | Các bước thực hiện | Kết quả mong đợi | Type (Happy/Negative/Edge) | Kết quả test (Result) | Chi tiết |
|----|------------------|---------------|--------------------------|---------------------|--------------------|------------------|----------------------------|------------------------|----------|
| TC-GTW-010 | FR-XI-08 / E1 ERR-XI-08-01 | Đợt BC chưa duyệt KQ | cb_nv_dp_01 login. Đợt DOT-CDP01-010 ở DANG_LAP_BC (chưa duyệt). | — | 1. Drill-down. | (1) Nút [Gửi lên TW] **ẩn**. HOẶC backend reject 400 với **"Đợt BC chưa được phê duyệt kết quả"** (ERR-XI-08-01). | Negative 🔴 | PASS |  |
| TC-GTW-011 | FR-XI-08 / E2 ERR-XI-08-02 | TW Gửi TW (cấp TW không gửi cho chính mình) | cb_nv_tw_01 (TW) login. Đợt DOT-CTW01-011 DA_DUYET_KQ. | — | 1. Drill-down. | (1) Nút [Gửi lên TW] **ẩn** (TW không thấy nút này). HOẶC nếu force trigger: backend reject 403 với **"Chỉ đơn vị BN/ĐP mới gửi BC lên TW"** (ERR-XI-08-02). | Negative 🔴 | PASS |  |

---

## 06-TC-tw-tong-hop-bc

> Source TC: `c:\HoaAG\LuatDN5\Ver3.1\output\test-cases\ct-htpldn-gd2\06-TC-tw-tong-hop-bc.md`
> Source report: `c:\HoaAG\LuatDN5\Ver3.1\output\execution-test\ct-htpldn-gd2\report-06-tw-tong-hop-bc\Tcs-report\tcs-report.md`

| ID | TraceID (Mã SRS) | Tên Test Case | Pre-conditions (Tiền đề) | Test Data (Dữ liệu) | Các bước thực hiện | Kết quả mong đợi | Type (Happy/Negative/Edge) | Kết quả test (Result) | Chi tiết |
|----|------------------|---------------|--------------------------|---------------------|--------------------|------------------|----------------------------|------------------------|----------|
| TC-TH-011 | FR-XI-09 / E2 ERR-XI-09-02 | BN/ĐP truy cập Tổng hợp TW | cb_nv_dp_01 (ĐP) login. | — | 1. Truy cập URL `/ct-htpldn/{id}/tong-hop-tw` trực tiếp. | (1) 403 Forbidden. HOẶC nút [Tổng hợp] **ẩn** trong UI cho ĐP. Backend reject với **"Chỉ cấp TW mới tổng hợp BC"** (ERR-XI-09-02). | Negative 🔴 | PASS |  |

---

## 07-TC-permission-matrix

> Source TC: `c:\HoaAG\LuatDN5\Ver3.1\output\test-cases\ct-htpldn-gd2\07-TC-permission-matrix.md`
> Source report: `c:\HoaAG\LuatDN5\Ver3.1\output\execution-test\ct-htpldn-gd2\report-07-permission-matrix\Tcs-report\tcs-report.md`

| ID | TraceID (Mã SRS) | Tên Test Case | Pre-conditions (Tiền đề) | Test Data (Dữ liệu) | Các bước thực hiện | Kết quả mong đợi | Type (Happy/Negative/Edge) | Kết quả test (Result) | Chi tiết |
|----|------------------|---------------|--------------------------|---------------------|--------------------|------------------|----------------------------|------------------------|----------|
| TC-PERM-002 | Matrix / CB_PD cùng cấp duyệt (BR-AUTH-05) | CB PD ĐP duyệt BC ĐP cùng đơn vị | cb_pd_dp_03 (Sở TP AG) login. Đợt DOT-CDP01-002 (Sở TP AG) CHO_DUYET_KQ. | — | 1. Drill-down. 2. Click [Phê duyệt]. | (2) PASS — CB PD ĐP cùng đơn vị duyệt được. Đợt → DA_DUYET_KQ. | Positive 🔴 | PASS |  |
| TC-PERM-011 | Matrix / TW không Gửi TW | CB NV TW thử Gửi TW (chính mình) | cb_nv_tw_03 login. Đợt DOT-CTW01-011 DA_DUYET_KQ. | — | 1. Drill-down. | (1) Nút [Gửi lên TW] **ẩn** cho cấp TW. (Hỗ trợ ERR-XI-08-02 nếu force trigger qua API.) | Negative 🔴 | PASS |  |
| TC-PERM-017 | Matrix / CB_PD không Gửi TW (Codex CT-GD2-04) | CB PD ĐP/BN thử action Gửi TW (chỉ CB NV BN/ĐP có quyền) | cb_pd_dp_03 (Sở TP AG) login. Đợt DOT-CDP01-017 (Sở TP AG) DA_DUYET_KQ. | — | 1. Drill-down. 2. Verify nút [Gửi lên TW]. | (2) Nút [Gửi lên TW] **ẩn** cho CB PD (chỉ CB NV BN/ĐP có quyền per FR-XI-08 line 901 "Tác nhân: Cán bộ Nghiệp vụ BN/ĐP"). Nếu force trigger qua API: backend reject 403 (ERR-XI-08-02 hoặc 403 generic). Repeat tương tự cho cb_pd_bn_03. | Negative 🔴 | PASS |  |

---

## Skipped

Không có section nào không chứa TC PASS — cả 7 file đều có ít nhất 1 TC PASS.

---

*Generated 2026-05-11 — filtered PASS-only từ result-ct-htpldn-gd2-all.md*
