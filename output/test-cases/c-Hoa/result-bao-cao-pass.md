# Test Cases PASS — Báo cáo Thống kê (FR-11 W5.2)

> **Nguồn**: result-bao-cao-all.md
> **Ngày tổng hợp**: 2026-05-11
> **Phạm vi**: chỉ Result ∈ {PASS, PASS-DEVIATE, PASS-RESOLVED}

## Summary

| File test-case | PASS | PASS-DEVIATE | PASS-RESOLVED | Tổng |
|----------------|------|--------------|---------------|------|
| 01-TC-tpl-report-full-representative | 4 | 0 | 0 | 4 |
| 02-TC-smoke-23-loai-bc | 4 | 19 | 0 | 23 |
| 03-TC-permission-2tier-bc | 3 | 1 | 0 | 4 |
| 04-TC-export-xlsx-pdf-tt17 | 0 | 0 | 1 | 1 |
| 05-TC-bieu-do-charts | 1 | 1 | 0 | 2 |
| **Tổng** | **12** | **21** | **1** | **34** |

---

## 01-TC-tpl-report-full-representative

> Source TC: `c:\HoaAG\LuatDN5\Ver3.1\output\test-cases\bao-cao-tk\01-TC-tpl-report-full-representative.md`
> Source report: `c:\HoaAG\LuatDN5\Ver3.1\output\execution-test\bao-cao\report-01-TC-tpl-report-full-representative\Tcs-report\Tcs-report-01-TC-tpl-report-full-representative.md`

| ID | TraceID (Mã SRS) | Tên Test Case | Pre-conditions (Tiền đề) | Test Data (Dữ liệu) | Các bước thực hiện | Kết quả mong đợi | Type (Happy/Negative/Edge) | Kết quả test (Result) | Chi tiết |
|----|------------------|---------------|--------------------------|---------------------|--------------------|------------------|----------------------------|------------------------|----------|
| TC-BC-REP-025 | FR-IX-01 / E7 ERR-RPT-05 | Không có quyền (NHT/TVV/CG/DN/GV) | nht_01 login (hoặc tvv_01/cg_01/dn_01/gv_01) | — | 1. Truy cập `/bao-cao` URL trực tiếp. | (1) GET 403. (3) Toast/page: **"Bạn không có quyền xem báo cáo này"** (ERR-RPT-05). Sidebar không có mục "Báo cáo thống kê" cho role này. | Negative 🔴 | PASS |  |
| TC-BC-REP-044 | SCR-IX-01 row#3 + AC | Đổi loại BC giữa lần xem (dropdown grouped) | cb_nv_tw_01 login. | BC HD → BC VV đã tiếp nhận | 1. Chọn HD + [Xem]. 2. Đổi dropdown sang BC VV đã tiếp nhận. | (3) Bộ lọc đặc thù tự render lại theo loại BC mới (linh_vuc + trang_thai_hd → kenh_tiep_nhan + linh_vuc). Bảng/biểu đồ refresh. | Edge 🟡 | PASS |  |
| TC-BC-REP-045 | SCR-IX-01 row#10 | Toggle hiện/ẩn biểu đồ | cb_nv_tw_01 login. Đã xem BC. | — | 1. Click toggle "Ẩn biểu đồ". 2. Click "Hiện biểu đồ". | (3) Biểu đồ ẩn → bảng full width. Toggle hiện lại → bảng + biểu đồ. | Edge 🟢 | PASS |  |
| TC-BC-REP-054 | SCR-IX-01 / A4 E10 | Deep-link URL pre-filled filter | cb_nv_tw_01 login. | URL `/bao-cao?loai=HOI_DAP&ky=THANG` | 1. Paste URL trực tiếp vào browser. | (3) **Behavior verify**: (a) SCR auto-select dropdown HD + kỳ THANG, hoặc (b) bỏ qua param, mở SCR clean. Log nếu surprising. | Edge 🟡 | PASS |  |

---

## 02-TC-smoke-23-loai-bc

> Source TC: `c:\HoaAG\LuatDN5\Ver3.1\output\test-cases\bao-cao-tk\02-TC-smoke-23-loai-bc.md`
> Source report: `c:\HoaAG\LuatDN5\Ver3.1\output\execution-test\bao-cao\report-02-TC-smoke-23-loai-bc\Tcs-report\Tcs-report-02-TC-smoke-23-loai-bc.md`

| ID | TraceID (Mã SRS) | Tên Test Case | Pre-conditions (Tiền đề) | Test Data (Dữ liệu) | Các bước thực hiện | Kết quả mong đợi | Type (Happy/Negative/Edge) | Kết quả test (Result) | Chi tiết |
|----|------------------|---------------|--------------------------|---------------------|--------------------|------------------|----------------------------|------------------------|----------|
| TC-BC-SM-03 | FR-IX-03 / UC126 / BR-SLA-02 / Codex F-04 / SPEC-CLARIFY-BC-11 | Smoke BC VV đang hỗ trợ — snapshot SLA 4 mức | VV DANG_HO_TRO: 2 BINH_THUONG, 2 SAP_HET_HAN, 2 QUA_HAN, 1 QUA_HAN_NGHIEM_TRONG. | (snapshot) | 1. Chọn "BC Vụ việc đang hỗ trợ". 2. [Xem]. | (3) Bộ lọc: nht_id + muc_sla. Output 4 cột rõ ràng: `binh_thuong=2, sap_het_han=2, qua_han=2, qua_han_nghiem_trong=1`. tong_dang_xu_ly=7. **SPEC-CLARIFY-BC-11**: SRS FR-IX-03 line 249 nói "<50% bình thường, 50-100% sắp hết hạn" mâu thuẫn BR-SLA-02 line 1280 ">50% bình thường, <50% sắp hết hạn" — verify thực tế FE follow chiều nào, log finding. Biểu đồ Bar snapshot. | Smoke 🔴 | PASS-DEVIATE |  |
| TC-BC-SM-04 | FR-IX-04 / UC127 / AC#bổ sung | Smoke BC VV đã hoàn thành | ≥5 VV HOAN_THANH với mix THANH_CONG/KHONG. | ky=QUY | 1. Chọn "BC Vụ việc đã hoàn thành". 2. [Xem]. | (3) Bộ lọc: linh_vuc + ket_qua. Output: tong_hoan_thanh, thanh_cong, khong_thanh_cong, ty_le_thanh_cong, theo_linh_vuc[], theo_don_vi[], theo_ky[]. Biểu đồ Bar + Donut. | Smoke 🟡 | PASS-DEVIATE |  |
| TC-BC-SM-06 | FR-IX-06 / UC129 / AC#bổ sung | Smoke BC Lớp đào tạo đang diễn ra (snapshot) | ≥3 KH DANG_DIEN_RA mix online/offline. | (snapshot) | 1. Chọn "BC Lớp đào tạo đang diễn ra". 2. [Xem]. | (3) Bộ lọc: hinh_thuc + linh_vuc. Output: tong_dang_dien_ra, truc_tuyen, truc_tiep, ds_khoa_hoc[]. Biểu đồ Bar snapshot. | Smoke 🟡 | PASS-DEVIATE |  |
| TC-BC-SM-07 | FR-IX-07 / UC130 / AC#bổ sung | Smoke BC Lớp đào tạo đã diễn ra | ≥3 KH KET_THUC trong kỳ với HV. | ky=QUY | 1. Chọn "BC Lớp đào tạo đã diễn ra". 2. [Xem]. | (3) Bộ lọc: hinh_thuc. Output: tong_da_dien_ra, tong_hoc_vien, theo_don_vi[], theo_hinh_thuc[], theo_ky[]. Biểu đồ Bar + Trend. | Smoke 🟡 | PASS-DEVIATE |  |
| TC-BC-SM-08 | FR-IX-08 / UC131 + Khoản 2 Điều 19 NĐ77/2008 | Smoke BC Số lượng CG/TVV (snapshot) | ≥3 TVV + ≥2 CG + ≥2 NHT đang hoạt động. | (snapshot) | 1. Chọn "BC Số lượng CG/TVV". 2. [Xem]. | (3) Bộ lọc: loai_tvv + linh_vuc + don_vi (đơn vị quản lý/công nhận, KHÔNG giới hạn địa bàn theo NĐ77/2008). Output: tong_tvv, so_tvv, so_cg, so_nht, theo_don_vi[], theo_linh_vuc[], theo_dia_ban[]. Biểu đồ Donut + Bar. | Smoke 🟡 | PASS-DEVIATE |  |
| TC-BC-SM-10 | FR-IX-10 / UC133 / AC#bổ sung | Smoke BC Chất lượng đào tạo | ≥1 KH có kết quả kiểm tra ≥10 HV. | ky=QUY | 1. Chọn "BC Chất lượng đào tạo". 2. [Xem]. | (3) Bộ lọc: khoa_hoc_id. Output: diem_trung_binh, ty_le_dat, tong_hoc_vien, theo_khoa_hoc[], theo_don_vi[]. Biểu đồ Bar + Line. | Smoke 🟡 | PASS-DEVIATE |  |
| TC-BC-SM-11 | FR-IX-11 / UC134 / AC#bổ sung | Smoke BC VV theo đơn vị (cross-tab) | VV phân bố TW/BN/ĐP với 4 trạng thái mix. | ky=NAM | 1. Chọn "BC Vụ việc theo đơn vị quản lý". 2. [Xem]. | (3) Bộ lọc đặc thù: KHÔNG. Output cross-tab: hàng=đơn vị, cột=trạng thái (moi/tiep_nhan/dang_ho_tro/hoan_thanh) + tong. Biểu đồ Stacked bar. | Smoke 🟡 | PASS-DEVIATE |  |
| TC-BC-SM-12 | FR-IX-12 / UC135 / AC#bổ sung | Smoke BC VV theo lĩnh vực (cross-tab) | VV phân bố ≥3 lĩnh vực × ≥3 đơn vị. | ky=NAM | 1. Chọn "BC Vụ việc theo lĩnh vực". 2. [Xem]. | (3) Bộ lọc đặc thù: KHÔNG. Output cross-tab: hàng=lĩnh vực, cột=đơn vị. Biểu đồ Grouped bar. | Smoke 🟡 | PASS-DEVIATE |  |
| TC-BC-SM-13 | FR-IX-13 / UC136 / AC#bổ sung | Smoke BC VV theo loại hình DN | VV với DN mix SIEU_NHO/NHO/VUA. | ky=NAM | 1. Chọn "BC Vụ việc theo loại hình DN". 2. [Xem]. | (3) Bộ lọc: loai_dn. Output: hàng=loai_dn, cột=đơn vị. Biểu đồ Grouped bar. | Smoke 🟡 | PASS-DEVIATE |  |
| TC-BC-SM-14 | FR-IX-14 / UC137 / AC#bổ sung | Smoke BC VV theo thời gian chi tiết — Stacked bar trend | ≥20 VV phân bố 6 tháng × 4 trạng thái. | ky=KHOANG, 6 tháng | 1. Chọn "BC Vụ việc theo thời gian chi tiết". 2. [Xem]. | (3) Bộ lọc đặc thù: KHÔNG. Output: chart_data[] 6 điểm {ky_label, moi, tiep_nhan, dang_ho_tro, hoan_thanh}, chart_type=STACKED_BAR. | Smoke 🟡 | PASS-DEVIATE |  |
| TC-BC-SM-15 | FR-IX-15 / UC138 / AC#bổ sung | Smoke BC Chi phí chi trả hỗ trợ | ≥5 HSCT DA_THANH_TOAN trong kỳ. | ky=NAM | 1. Chọn "BC Chi phí chi trả hỗ trợ". 2. [Xem]. | (3) Bộ lọc: KHÔNG. Output: tong_chi_phi (VND), tong_ho_so, trung_binh_ho_so, theo_don_vi[], theo_ky[]. Biểu đồ Bar + Summary. | Smoke 🟡 | PASS-DEVIATE |  |
| TC-BC-SM-16 | FR-IX-16 / UC139 / AC#bổ sung | Smoke BC Chi phí theo đơn vị | HSCT phân bố TW/BN/ĐP. | ky=NAM | 1. Chọn "BC Chi phí theo đơn vị". 2. [Xem]. | (3) Bộ lọc: KHÔNG. Output: hàng=đơn vị (TW/BN/ĐP), cột=tong_chi_phi + so_ho_so + trung_binh. Biểu đồ Bar cross-tab. | Smoke 🟡 | PASS-DEVIATE |  |
| TC-BC-SM-18 | FR-IX-18 / UC141 / NĐ55/2019 | Smoke BC Chi phí theo loại hình DN + so trần | HSCT mix loại DN với mức hỗ trợ 100%/30%/10%. | ky=NAM | 1. Chọn "BC Chi phí theo loại hình DN". 2. [Xem]. | (3) Bộ lọc: loai_dn. Output: loai_dn, ten_loai_dn, muc_ho_tro (100%/30%/10%), so_ho_so, tong_chi_phi, tran_chi_phi (theo NĐ55/2019), chenh_lech. Biểu đồ Grouped bar. | Smoke 🟡 | PASS-DEVIATE |  |
| TC-BC-SM-19 | FR-IX-19 / UC142 / AC#bổ sung | Smoke BC Chi phí theo thời gian — Line trend | HSCT phân bố 12 tháng. | ky=KHOANG, 12 tháng | 1. Chọn "BC Chi phí theo thời gian". 2. Chọn 12 tháng. 3. [Xem]. | (3) Bộ lọc: KHÔNG. Output: trend_data[] 12 điểm {ky_label, tong_chi_phi, so_ho_so}, chart_type=LINE, tong_chi_phi_ky. | Smoke 🟡 | PASS-DEVIATE |  |
| TC-BC-SM-20 | FR-IX-20 / UC143 / AC#bổ sung | Smoke BC Số lượng CT hỗ trợ | ≥3 CT mix DANG_THUC_HIEN/HOAN_THANH. | ky=NAM | 1. Chọn "BC Số lượng CT hỗ trợ". 2. [Xem]. | (3) Bộ lọc: trang_thai_ct. Output: tong_ct, dang_thuc_hien, hoan_thanh, theo_don_vi[], theo_ky[]. Biểu đồ Bar + Trend. | Smoke 🟡 | PASS-DEVIATE |  |
| TC-BC-SM-21 | FR-IX-21 / UC144 / AC#bổ sung | Smoke BC CT theo đơn vị | CT phân bố TW/BN/ĐP với ngân sách. | ky=NAM | 1. Chọn "BC CT theo đơn vị". 2. [Xem]. | (3) Bộ lọc: KHÔNG. Output: hàng=đơn vị, cột=so_ct + tong_ngan_sach. Biểu đồ Bar cross-tab. | Smoke 🟡 | PASS-DEVIATE |  |
| TC-BC-SM-23 | FR-IX-23 / UC146 / AC#bổ sung | Smoke BC CT theo thời gian — Line trend | CT phân bố 12 tháng. | ky=KHOANG, 12 tháng | 1. Chọn "BC CT theo thời gian". 2. [Xem]. | (3) Bộ lọc: KHÔNG. Output: trend_data[] 12 điểm {ky_label, so_ct, so_dn}, chart_type=LINE, tong_ct. | Smoke 🟡 | PASS-DEVIATE |  |
| TC-BC-SM-XC-01 | SCR-IX-01 row#3 / Codex F-07 | Dropdown 23 BC grouped optgroup | cb_nv_tw_01 login. | — | 1. Mở dropdown loại BC. | (3) Dropdown grouped **8 nhóm**: "Hỏi đáp pháp luật" (1) + "Vụ việc" (4) + "Đào tạo" (2) + "CG/TVV" (1) + "Đánh giá" (2) + "VV theo chiều phân tích" (4) + "Chi phí" (5) + "CT HTPLDN" (4) = 23 options. Mỗi option label "[Mã UC] Tên BC" theo srs-fr-11:1041. | Smoke 🟡 | PASS-DEVIATE |  |
| TC-BC-SM-XC-03 | SCR-IX-01 row#6 dynamic filter | Đổi loại BC → bộ lọc đặc thù tự render lại | cb_nv_tw_01 login. | UC125 → UC126 | 1. Chọn UC125 (kenh + linh_vuc). 2. Đổi sang UC126 (nht + sla). | (3) Bộ lọc đặc thù tự cập nhật theo loại BC. Filter cũ clear hoặc preserve theo behavior thực tế (mark verify). | Smoke 🟡 | PASS |  |
| TC-BC-SM-XC-04 | SCR-IX-01 row#7 | Disable nút "Xem báo cáo" khi chưa chọn loại BC | cb_nv_tw_01 login (mới mở SCR). | — | 1. Chưa chọn loại BC. | (3) Nút [Xem báo cáo] disabled. | Smoke 🟢 | PASS-DEVIATE |  |
| TC-BC-SM-XC-05 | SCR-IX-01 row#8-9 | Disable nút Xuất khi chưa chạy [Xem] | cb_nv_tw_01 login. | — | 1. Chọn loại BC. 2. Chưa click [Xem]. | (3) Nút [Xuất Excel] + [Xuất PDF] disabled. | Smoke 🟢 | PASS |  |
| TC-BC-SM-XC-06 | SCR-IX-01 row#1-2 | Breadcrumb + Tiêu đề + Làm mới | cb_nv_tw_01 login. | — | 1. Mở SCR-IX-01. | (3) Breadcrumb "Trang chủ > Báo cáo thống kê". Tiêu đề "Báo cáo Thống kê". Nút "Làm mới" hiện. 2. Click [Làm mới] → reset filter + clear data. | Smoke 🟢 | PASS |  |
| TC-BC-SM-XC-08 | SCR-IX-01 row#11 (sticky) | Sticky header + Sort cột + Hàng tổng cộng | Đã chạy BC có ≥30 dòng. | — | 1. Cuộn bảng xuống. 2. Click sort cột tổng. | (3) Header sticky giữ trên khi cuộn. Click sort → reorder ASC/DESC. Hàng tổng cộng (bold) ở cuối bảng. | Smoke 🟡 | PASS |  |

---

## 03-TC-permission-2tier-bc

> Source TC: `c:\HoaAG\LuatDN5\Ver3.1\output\test-cases\bao-cao-tk\03-TC-permission-2tier-bc.md`
> Source report: `c:\HoaAG\LuatDN5\Ver3.1\output\execution-test\bao-cao\report-03-TC-permission-2tier-bc\Tcs-report\Tcs-report-03-TC-permission-2tier-bc.md`

| ID | TraceID (Mã SRS) | Tên Test Case | Pre-conditions (Tiền đề) | Test Data (Dữ liệu) | Các bước thực hiện | Kết quả mong đợi | Type (Happy/Negative/Edge) | Kết quả test (Result) | Chi tiết |
|----|------------------|---------------|--------------------------|---------------------|--------------------|------------------|----------------------------|------------------------|----------|
| TC-BC-PERM-000 | BR-AUTH-01 / Codex F-03 | Chưa đăng nhập truy cập /bao-cao | Browser session sạch (clear cookies/localStorage). Chưa đăng nhập. | — | 1. Truy cập trực tiếp URL `http://103.172.236.130:3000/bao-cao`. | (1) Redirect về `/login` HOẶC trả 401 (không lộ data BC). (3) KHÔNG trả dữ liệu BC. KHÔNG render SCR-IX-01. Sau khi login → resume URL hoặc về dashboard. | Permission 🔴 | PASS |  |
| TC-BC-PERM-001 | BR-AUTH-08 / TW scope | CB_NV_TW xem BC HD toàn quốc | cb_nv_tw_01 login. HD ở 3 đơn vị: TW + BN + ĐP. | ky=THANG | 1. Chọn BC HD. 2. don_vi=Toàn quốc. 3. [Xem]. | (3) tong_hoi_dap = sum 3 đơn vị. theo_don_vi[] hiện 3 đơn vị. | Permission 🔴 | PASS-DEVIATE |  |
| TC-BC-PERM-022 | SCR-IX-01 row#5 | Dropdown đơn vị locked cho CB_NV_DP | cb_nv_dp_01 login. | — | 1. Open dropdown đơn vị. | (3) Dropdown disabled hoặc chỉ "Sở TP AG". | Permission 🔴 | PASS |  |
| TC-BC-PERM-030 | E7 ERR-RPT-05 (NHT) | NHT không có quyền xem BC | nht_01 login. | — | 1. Truy cập `/bao-cao` URL trực tiếp. | (1) 403. (3) Toast "Bạn không có quyền xem báo cáo này" (ERR-RPT-05). Sidebar không có mục "Báo cáo thống kê". | Permission 🔴 | PASS |  |

---

## 04-TC-export-xlsx-pdf-tt17

> Source TC: `c:\HoaAG\LuatDN5\Ver3.1\output\test-cases\bao-cao-tk\04-TC-export-xlsx-pdf-tt17.md`
> Source report: `c:\HoaAG\LuatDN5\Ver3.1\output\execution-test\bao-cao\report-04-TC-export-xlsx-pdf-tt17\Tcs-report\Tcs-report-04-TC-export-xlsx-pdf-tt17.md`

| ID | TraceID (Mã SRS) | Tên Test Case | Pre-conditions (Tiền đề) | Test Data (Dữ liệu) | Các bước thực hiện | Kết quả mong đợi | Type (Happy/Negative/Edge) | Kết quả test (Result) | Chi tiết |
|----|------------------|---------------|--------------------------|---------------------|--------------------|------------------|----------------------------|------------------------|----------|
| TC-BC-EXP-006 | BR-DATA-06 / SPEC-CLARIFY-BC-01 verify path | Verify thực tế FE follow BR formal (10K) hay TPL inline (50K) | cb_nv_tw_01 login. data=10,001 rows. | — | 1. Chạy BC + xuất XLSX. | (3) **SPEC-CLARIFY-BC-01 verify path**: Nếu cap=10K (BR formal) → file chỉ 10K + WRN-RPT-01. Nếu cap=50K (TPL inline) → file đủ 10,001 rows + KHÔNG WRN. Log finding vào gap-report — cần BA chốt update TPL hoặc nâng BR. | Edge 🔴 | PASS-RESOLVED | API /bao-cao/loai returned maxRows: 50000 cho 23/23 BC. FE+BE follow TPL inline 50K, KHÔNG follow BR formal 10K. SPEC-CLARIFY-BC-01 verified → BUG-BC-EXP-001 |

---

## 05-TC-bieu-do-charts

> Source TC: `c:\HoaAG\LuatDN5\Ver3.1\output\test-cases\bao-cao-tk\05-TC-bieu-do-charts.md`
> Source report: `c:\HoaAG\LuatDN5\Ver3.1\output\execution-test\bao-cao\report-05-TC-bieu-do-charts\Tcs-report\Tcs-report-05-TC-bieu-do-charts.md`

| ID | TraceID (Mã SRS) | Tên Test Case | Pre-conditions (Tiền đề) | Test Data (Dữ liệu) | Các bước thực hiện | Kết quả mong đợi | Type (Happy/Negative/Edge) | Kết quả test (Result) | Chi tiết |
|----|------------------|---------------|--------------------------|---------------------|--------------------|------------------|----------------------------|------------------------|----------|
| TC-BC-CHART-003 | FR-IX-08 / chart Donut + Bar | Donut + Bar BC CG/TVV | cb_nv_tw_01 login. TVV/CG/NHT đều có. | (snapshot) | 1. Chạy BC FR-IX-08. | (3) Donut (TVV/CG/NHT) + Bar (theo đơn vị). | Happy 🟡 | PASS-DEVIATE |  |
| TC-BC-CHART-020 | SCR-IX-01 row#10 | Toggle "Ẩn biểu đồ" → bảng full width | cb_nv_tw_01 login. Đã chạy BC có biểu đồ. | — | 1. Click toggle "Ẩn biểu đồ". | (3) Vùng biểu đồ collapse, bảng full width. Toggle label đổi thành "Hiện biểu đồ". | Happy 🟡 | PASS |  |

---

## Skipped

Không có section nào bị skip — cả 5 section đều có ≥1 TC PASS/PASS-DEVIATE/PASS-RESOLVED.

*Generated 2026-05-11 — QA aggregator (Phase B execution roll-up, PASS-only filter)*
