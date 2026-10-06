# Test Cases — Smoke 23 loại BC (FR-IX-01..FR-IX-23 / UC124-UC146)

> **SRS Ref**: srs-fr-11:127-1019 (toàn bộ 23 FR), SCR-IX-01 dropdown grouped (srs-fr-11:1054-1080)
> **Ngày tạo**: 2026-05-10
> **Đặc thù**: Smoke 1-2 TC mỗi loại BC để verify dropdown render + filter đặc thù + dimension output + biểu đồ phù hợp. KHÔNG re-test template chung (đã ở `01-TC-tpl-report-full-representative.md`).

---

## Quy ước

- **Priority**: 🔴 P0 · 🟡 P1 · 🟢 P2
- **TraceID**: `FR-IX-{NN} / {UC} / {AC#}`
- **Pre-conditions mặc định**: cb_nv_tw_01 login, kỳ THANG, scope toàn quốc, dữ liệu nguồn ≥5 record DA_DUYET trong kỳ.

---

## A. Hỏi đáp + Vụ việc + Đào tạo (UC124-UC130)

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|---------|--------------|----------------|-----------|-------------------|------------------|------|
| TC-BC-SM-01 | FR-IX-01 / UC124 (đã rep file 01) | Smoke BC Hỏi đáp — verify chỉ render OK | Đã có data ở module Hỏi đáp. | ky=THANG | 1. Chọn dropdown "BC Số lượng hỏi đáp". 2. [Xem]. | (3) Bộ lọc đặc thù: linh_vuc + trang_thai_hd hiện. Biểu đồ Donut + Trend. | Smoke 🟢 (đã rep) |
| TC-BC-SM-02 | FR-IX-02 / UC125 / AC#bổ sung | Smoke BC Vụ việc đã tiếp nhận | ≥5 VU_VIEC trạng thái TIEP_NHAN trong kỳ với 2-3 kênh khác nhau. | ky=THANG | 1. Chọn "BC Vụ việc đã tiếp nhận". 2. [Xem]. | (3) Bộ lọc: kenh_tiep_nhan (DVC/HE_THONG_KHAC/TRUC_TIEP/BUU_CHINH/DIEN_THOAI) + linh_vuc. Output: tong_vu_viec, theo_kenh[], theo_linh_vuc[], theo_don_vi[], theo_ky[]. Biểu đồ Bar + Trend. | Smoke 🟡 |
| TC-BC-SM-02b | FR-IX-02 / Kênh DVC | Filter kênh DVC | ≥3 VV qua DVC. | kenh_tiep_nhan=DVC | 1. Filter kênh DVC. 2. [Xem]. | (3) Chỉ VV qua DVC được tính. | Smoke 🟢 |
| TC-BC-SM-03 | FR-IX-03 / UC126 / BR-SLA-02 / Codex F-04 / SPEC-CLARIFY-BC-11 | Smoke BC VV đang hỗ trợ — snapshot SLA 4 mức | VV DANG_HO_TRO: 2 BINH_THUONG, 2 SAP_HET_HAN, 2 QUA_HAN, 1 QUA_HAN_NGHIEM_TRONG. | (snapshot) | 1. Chọn "BC Vụ việc đang hỗ trợ". 2. [Xem]. | (3) Bộ lọc: nht_id + muc_sla. Output 4 cột rõ ràng: `binh_thuong=2, sap_het_han=2, qua_han=2, qua_han_nghiem_trong=1`. tong_dang_xu_ly=7. **SPEC-CLARIFY-BC-11**: SRS FR-IX-03 line 249 nói "<50% bình thường, 50-100% sắp hết hạn" mâu thuẫn BR-SLA-02 line 1280 ">50% bình thường, <50% sắp hết hạn" — verify thực tế FE follow chiều nào, log finding. Biểu đồ Bar snapshot. | Smoke 🔴 |
| TC-BC-SM-03b | FR-IX-03 / BR-SLA-02 | Filter mức SLA Quá hạn | Đã seed như SM-03. | muc_sla=QUA_HAN | 1. Filter QUA_HAN. 2. [Xem]. | (3) Chỉ VV >100% deadline. | Smoke 🟡 |
| TC-BC-SM-04 | FR-IX-04 / UC127 / AC#bổ sung | Smoke BC VV đã hoàn thành | ≥5 VV HOAN_THANH với mix THANH_CONG/KHONG. | ky=QUY | 1. Chọn "BC Vụ việc đã hoàn thành". 2. [Xem]. | (3) Bộ lọc: linh_vuc + ket_qua. Output: tong_hoan_thanh, thanh_cong, khong_thanh_cong, ty_le_thanh_cong, theo_linh_vuc[], theo_don_vi[], theo_ky[]. Biểu đồ Bar + Donut. | Smoke 🟡 |
| TC-BC-SM-05 | FR-IX-05 / UC128 / AC#bổ sung | Smoke BC VV theo thời gian — Line trend | ≥10 VV phân bố 6 tháng. | ky=KHOANG, 6 tháng | 1. Chọn "BC Vụ việc theo thời gian". 2. Chọn 6 tháng. 3. [Xem]. | (3) Output: trend_data[] 6 điểm {ky_label, tiep_nhan, hoan_thanh}, chart_type=LINE. Bộ lọc đặc thù KHÔNG có. | Smoke 🟡 |
| TC-BC-SM-06 | FR-IX-06 / UC129 / AC#bổ sung | Smoke BC Lớp đào tạo đang diễn ra (snapshot) | ≥3 KH DANG_DIEN_RA mix online/offline. | (snapshot) | 1. Chọn "BC Lớp đào tạo đang diễn ra". 2. [Xem]. | (3) Bộ lọc: hinh_thuc + linh_vuc. Output: tong_dang_dien_ra, truc_tuyen, truc_tiep, ds_khoa_hoc[]. Biểu đồ Bar snapshot. | Smoke 🟡 |
| TC-BC-SM-07 | FR-IX-07 / UC130 / AC#bổ sung | Smoke BC Lớp đào tạo đã diễn ra | ≥3 KH KET_THUC trong kỳ với HV. | ky=QUY | 1. Chọn "BC Lớp đào tạo đã diễn ra". 2. [Xem]. | (3) Bộ lọc: hinh_thuc. Output: tong_da_dien_ra, tong_hoc_vien, theo_don_vi[], theo_hinh_thuc[], theo_ky[]. Biểu đồ Bar + Trend. | Smoke 🟡 |

---

## B. CG/TVV + Đánh giá (UC131-UC133)

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|---------|--------------|----------------|-----------|-------------------|------------------|------|
| TC-BC-SM-08 | FR-IX-08 / UC131 + Khoản 2 Điều 19 NĐ77/2008 | Smoke BC Số lượng CG/TVV (snapshot) | ≥3 TVV + ≥2 CG + ≥2 NHT đang hoạt động. | (snapshot) | 1. Chọn "BC Số lượng CG/TVV". 2. [Xem]. | (3) Bộ lọc: loai_tvv + linh_vuc + don_vi (đơn vị quản lý/công nhận, KHÔNG giới hạn địa bàn theo NĐ77/2008). Output: tong_tvv, so_tvv, so_cg, so_nht, theo_don_vi[], theo_linh_vuc[], theo_dia_ban[]. Biểu đồ Donut + Bar. | Smoke 🟡 |
| TC-BC-SM-08b | FR-IX-08 / Filter loại CG | Filter loại CG | Đã seed. | loai_tvv=CG | 1. Filter loại CG. 2. [Xem]. | (3) Chỉ CG hiện. so_tvv=0. | Smoke 🟢 |
| TC-BC-SM-09 | FR-IX-09 / UC132 / AC#bổ sung | Smoke BC Đánh giá hiệu quả HTPL | ≥1 KE_HOACH_DG đã có kết quả với ≥3 VV được ĐG. | ky=NAM | 1. Chọn "BC Đánh giá hiệu quả HTPL". 2. [Xem]. | (3) Bộ lọc: ke_hoach_dg_id. Output: diem_trung_binh, so_vu_viec_danh_gia, theo_don_vi[], theo_tieu_chi[], theo_dot[]. Biểu đồ Bar + Radar. | Smoke 🟡 |
| TC-BC-SM-10 | FR-IX-10 / UC133 / AC#bổ sung | Smoke BC Chất lượng đào tạo | ≥1 KH có kết quả kiểm tra ≥10 HV. | ky=QUY | 1. Chọn "BC Chất lượng đào tạo". 2. [Xem]. | (3) Bộ lọc: khoa_hoc_id. Output: diem_trung_binh, ty_le_dat, tong_hoc_vien, theo_khoa_hoc[], theo_don_vi[]. Biểu đồ Bar + Line. | Smoke 🟡 |
| TC-BC-SM-09c | FR-IX-09 / Filter đợt cụ thể / A6 G1 fill | Filter "Đợt đánh giá Q1/2026" cụ thể | cb_nv_tw_01 login. KE_HOACH_DG có 2 đợt: "Q1/2026" + "Q2/2026" với data ĐG. | ke_hoach_dg_id=Q1/2026 | 1. Chọn BC FR-IX-09. 2. Dropdown đợt → Q1/2026. 3. [Xem]. | (3) Chỉ data đợt Q1/2026. theo_dot[] 1 entry duy nhất Q1/2026. Q2/2026 KHÔNG hiện. | Happy 🟡 |
| TC-BC-SM-10b | FR-IX-10 / Filter KH cụ thể / A6 G2 fill | Filter "Khóa học cụ thể" | cb_nv_tw_01 login. ≥2 KH có kết quả kiểm tra. | khoa_hoc_id=KH001 | 1. Chọn BC FR-IX-10. 2. Dropdown khóa học → KH001. 3. [Xem]. | (3) Chỉ data KH001. theo_khoa_hoc[] 1 entry. KH khác KHÔNG hiện. | Happy 🟡 |

---

## C. Vụ việc cross-tab (UC134-UC137)

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|---------|--------------|----------------|-----------|-------------------|------------------|------|
| TC-BC-SM-11 | FR-IX-11 / UC134 / AC#bổ sung | Smoke BC VV theo đơn vị (cross-tab) | VV phân bố TW/BN/ĐP với 4 trạng thái mix. | ky=NAM | 1. Chọn "BC Vụ việc theo đơn vị quản lý". 2. [Xem]. | (3) Bộ lọc đặc thù: KHÔNG. Output cross-tab: hàng=đơn vị, cột=trạng thái (moi/tiep_nhan/dang_ho_tro/hoan_thanh) + tong. Biểu đồ Stacked bar. | Smoke 🟡 |
| TC-BC-SM-12 | FR-IX-12 / UC135 / AC#bổ sung | Smoke BC VV theo lĩnh vực (cross-tab) | VV phân bố ≥3 lĩnh vực × ≥3 đơn vị. | ky=NAM | 1. Chọn "BC Vụ việc theo lĩnh vực". 2. [Xem]. | (3) Bộ lọc đặc thù: KHÔNG. Output cross-tab: hàng=lĩnh vực, cột=đơn vị. Biểu đồ Grouped bar. | Smoke 🟡 |
| TC-BC-SM-13 | FR-IX-13 / UC136 / AC#bổ sung | Smoke BC VV theo loại hình DN | VV với DN mix SIEU_NHO/NHO/VUA. | ky=NAM | 1. Chọn "BC Vụ việc theo loại hình DN". 2. [Xem]. | (3) Bộ lọc: loai_dn. Output: hàng=loai_dn, cột=đơn vị. Biểu đồ Grouped bar. | Smoke 🟡 |
| TC-BC-SM-14 | FR-IX-14 / UC137 / AC#bổ sung | Smoke BC VV theo thời gian chi tiết — Stacked bar trend | ≥20 VV phân bố 6 tháng × 4 trạng thái. | ky=KHOANG, 6 tháng | 1. Chọn "BC Vụ việc theo thời gian chi tiết". 2. [Xem]. | (3) Bộ lọc đặc thù: KHÔNG. Output: chart_data[] 6 điểm {ky_label, moi, tiep_nhan, dang_ho_tro, hoan_thanh}, chart_type=STACKED_BAR. | Smoke 🟡 |

---

## D. Chi phí (UC138-UC142)

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|---------|--------------|----------------|-----------|-------------------|------------------|------|
| TC-BC-SM-15 | FR-IX-15 / UC138 / AC#bổ sung | Smoke BC Chi phí chi trả hỗ trợ | ≥5 HSCT DA_THANH_TOAN trong kỳ. | ky=NAM | 1. Chọn "BC Chi phí chi trả hỗ trợ". 2. [Xem]. | (3) Bộ lọc: KHÔNG. Output: tong_chi_phi (VND), tong_ho_so, trung_binh_ho_so, theo_don_vi[], theo_ky[]. Biểu đồ Bar + Summary. | Smoke 🟡 |
| TC-BC-SM-16 | FR-IX-16 / UC139 / AC#bổ sung | Smoke BC Chi phí theo đơn vị | HSCT phân bố TW/BN/ĐP. | ky=NAM | 1. Chọn "BC Chi phí theo đơn vị". 2. [Xem]. | (3) Bộ lọc: KHÔNG. Output: hàng=đơn vị (TW/BN/ĐP), cột=tong_chi_phi + so_ho_so + trung_binh. Biểu đồ Bar cross-tab. | Smoke 🟡 |
| TC-BC-SM-17 | FR-IX-17 / UC140 / AC#bổ sung | Smoke BC Chi phí theo lĩnh vực | HSCT mix lĩnh vực. | ky=NAM | 1. Chọn "BC Chi phí theo lĩnh vực". 2. [Xem]. | (3) Bộ lọc: linh_vuc. Output: hàng=lĩnh vực, cột=tong_chi_phi + so_ho_so. Biểu đồ Bar. | Smoke 🟡 |
| TC-BC-SM-18 | FR-IX-18 / UC141 / NĐ55/2019 | Smoke BC Chi phí theo loại hình DN + so trần | HSCT mix loại DN với mức hỗ trợ 100%/30%/10%. | ky=NAM | 1. Chọn "BC Chi phí theo loại hình DN". 2. [Xem]. | (3) Bộ lọc: loai_dn. Output: loai_dn, ten_loai_dn, muc_ho_tro (100%/30%/10%), so_ho_so, tong_chi_phi, tran_chi_phi (theo NĐ55/2019), chenh_lech. Biểu đồ Grouped bar. | Smoke 🟡 |
| TC-BC-SM-19 | FR-IX-19 / UC142 / AC#bổ sung | Smoke BC Chi phí theo thời gian — Line trend | HSCT phân bố 12 tháng. | ky=KHOANG, 12 tháng | 1. Chọn "BC Chi phí theo thời gian". 2. Chọn 12 tháng. 3. [Xem]. | (3) Bộ lọc: KHÔNG. Output: trend_data[] 12 điểm {ky_label, tong_chi_phi, so_ho_so}, chart_type=LINE, tong_chi_phi_ky. | Smoke 🟡 |

---

## E. CT HTPLDN (UC143-UC146)

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|---------|--------------|----------------|-----------|-------------------|------------------|------|
| TC-BC-SM-20 | FR-IX-20 / UC143 / AC#bổ sung | Smoke BC Số lượng CT hỗ trợ | ≥3 CT mix DANG_THUC_HIEN/HOAN_THANH. | ky=NAM | 1. Chọn "BC Số lượng CT hỗ trợ". 2. [Xem]. | (3) Bộ lọc: trang_thai_ct. Output: tong_ct, dang_thuc_hien, hoan_thanh, theo_don_vi[], theo_ky[]. Biểu đồ Bar + Trend. | Smoke 🟡 |
| TC-BC-SM-21 | FR-IX-21 / UC144 / AC#bổ sung | Smoke BC CT theo đơn vị | CT phân bố TW/BN/ĐP với ngân sách. | ky=NAM | 1. Chọn "BC CT theo đơn vị". 2. [Xem]. | (3) Bộ lọc: KHÔNG. Output: hàng=đơn vị, cột=so_ct + tong_ngan_sach. Biểu đồ Bar cross-tab. | Smoke 🟡 |
| TC-BC-SM-22 | FR-IX-22 / UC145 / AC#bổ sung | Smoke BC CT theo lĩnh vực | CT mix lĩnh vực với DN tham gia. | ky=NAM | 1. Chọn "BC CT theo lĩnh vực". 2. [Xem]. | (3) Bộ lọc: linh_vuc. Output: hàng=lĩnh vực, cột=so_ct + so_dn_tham_gia. Biểu đồ Bar. | Smoke 🟡 |
| TC-BC-SM-23 | FR-IX-23 / UC146 / AC#bổ sung | Smoke BC CT theo thời gian — Line trend | CT phân bố 12 tháng. | ky=KHOANG, 12 tháng | 1. Chọn "BC CT theo thời gian". 2. [Xem]. | (3) Bộ lọc: KHÔNG. Output: trend_data[] 12 điểm {ky_label, so_ct, so_dn}, chart_type=LINE, tong_ct. | Smoke 🟡 |

---

## F. Cross-cutting (Dropdown grouped + chuyển BC)

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|---------|--------------|----------------|-----------|-------------------|------------------|------|
| TC-BC-SM-XC-01 | SCR-IX-01 row#3 / Codex F-07 | Dropdown 23 BC grouped optgroup | cb_nv_tw_01 login. | — | 1. Mở dropdown loại BC. | (3) Dropdown grouped **8 nhóm**: "Hỏi đáp pháp luật" (1) + "Vụ việc" (4) + "Đào tạo" (2) + "CG/TVV" (1) + "Đánh giá" (2) + "VV theo chiều phân tích" (4) + "Chi phí" (5) + "CT HTPLDN" (4) = 23 options. Mỗi option label "[Mã UC] Tên BC" theo srs-fr-11:1041. | Smoke 🟡 |
| TC-BC-SM-XC-02 | SCR-IX-01 row#3 | Searchable dropdown filter "vụ việc" | cb_nv_tw_01 login. | search="vụ việc" | 1. Type "vụ việc" trong dropdown search. | (3) Filter còn 8 options (4 VV + 4 VV cross-tab UC134-137). | Smoke 🟢 |
| TC-BC-SM-XC-03 | SCR-IX-01 row#6 dynamic filter | Đổi loại BC → bộ lọc đặc thù tự render lại | cb_nv_tw_01 login. | UC125 → UC126 | 1. Chọn UC125 (kenh + linh_vuc). 2. Đổi sang UC126 (nht + sla). | (3) Bộ lọc đặc thù tự cập nhật theo loại BC. Filter cũ clear hoặc preserve theo behavior thực tế (mark verify). | Smoke 🟡 |
| TC-BC-SM-XC-04 | SCR-IX-01 row#7 | Disable nút "Xem báo cáo" khi chưa chọn loại BC | cb_nv_tw_01 login (mới mở SCR). | — | 1. Chưa chọn loại BC. | (3) Nút [Xem báo cáo] disabled. | Smoke 🟢 |
| TC-BC-SM-XC-05 | SCR-IX-01 row#8-9 | Disable nút Xuất khi chưa chạy [Xem] | cb_nv_tw_01 login. | — | 1. Chọn loại BC. 2. Chưa click [Xem]. | (3) Nút [Xuất Excel] + [Xuất PDF] disabled. | Smoke 🟢 |
| TC-BC-SM-XC-06 | SCR-IX-01 row#1-2 | Breadcrumb + Tiêu đề + Làm mới | cb_nv_tw_01 login. | — | 1. Mở SCR-IX-01. | (3) Breadcrumb "Trang chủ > Báo cáo thống kê". Tiêu đề "Báo cáo Thống kê". Nút "Làm mới" hiện. 2. Click [Làm mới] → reset filter + clear data. | Smoke 🟢 |
| TC-BC-SM-XC-07 | TPL.Process step 4 + BR-RPT-01 (cross BC) | Verify "chỉ bản ghi đã duyệt" áp dụng đồng nhất 23 BC | Module nguồn có cả CHO_DUYET + DA_DUYET. | (mỗi BC) | 1. Chạy 3 BC mẫu (UC124 HD, UC125 VV, UC138 HSCT). 2. So tổng đếm với count DA_DUYET. | (3) Mọi BC chỉ tính bản ghi đã duyệt. KHÔNG có BC nào tính CHO_DUYET. | Smoke 🔴 |
| TC-BC-SM-XC-08 | SCR-IX-01 row#11 (sticky) | Sticky header + Sort cột + Hàng tổng cộng | Đã chạy BC có ≥30 dòng. | — | 1. Cuộn bảng xuống. 2. Click sort cột tổng. | (3) Header sticky giữ trên khi cuộn. Click sort → reorder ASC/DESC. Hàng tổng cộng (bold) ở cuối bảng. | Smoke 🟡 |

---

## G. EDGE bổ sung (A4 inline merge 2026-05-10)

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|---------|--------------|----------------|-----------|-------------------|------------------|------|
| TC-BC-SM-XC-09 | SCR-IX-01 row#5 / A4 E8 | Don_vi_ten dài 200+ ký tự trong dropdown | cb_nv_tw_01 login. (Seed 1 don_vi với ten 200 ký tự). | — | 1. Open dropdown đơn vị. | (3) Tên truncate với ellipsis "..." + tooltip hover hiển thị full tên. KHÔNG vỡ layout dropdown. | Edge 🟢 |
| TC-BC-SM-XC-10 | SCR-IX-01 row#3 / A4 E9 | Search dropdown loại BC accent-aware | cb_nv_tw_01 login. | search="dao tao" (không dấu) | 1. Type "dao tao" trong dropdown search. | (3) Filter match "Đào tạo" group (UC129, UC130) + "Chất lượng đào tạo" (UC133). Vietnamese accent-insensitive. | Edge 🟢 |
| TC-BC-SM-03c | FR-IX-03 / Snapshot consistency / A4 E13 | Snapshot UC126 — 2 lần [Xem] cách 2 phút có thể khác | cb_nv_tw_01 login. | (snapshot) | 1. [Xem] BC FR-IX-03 lần 1, capture tổng. 2. (Seed thêm 1 VV DANG_HO_TRO mới). 3. [Xem] lần 2. | (3) Lần 2 tổng tăng +1 (snapshot là realtime tại thời điểm query). Hoặc nếu snapshot có cache, log behavior. | Edge 🟡 |
| TC-BC-SM-09b | FR-IX-09 / A4 E15 | Filter "Đợt đánh giá" đã soft-delete | cb_nv_tw_01 login. KE_HOACH_DG có 1 đợt active + 1 đợt is_deleted=1. | — | 1. Chọn BC FR-IX-09. 2. Open dropdown đợt. | (3) Dropdown chỉ hiện đợt active. Đợt soft-deleted KHÔNG hiện (BR-DATA-01). | Edge 🟢 |

---

## Tổng kết file 02-TC

- **38 TC**: 9 A + 4 B + 4 C + 5 D + 4 E + 8 F + 4 G (A4 merged).
  - Recount: A=9 (SM-01,02,02b,03,03b,04,05,06,07), B=6 (SM-08,08b,09,09c,10,10b — 09c+10b A6 fill), C=4 (SM-11..14), D=5 (SM-15..19), E=4 (SM-20..23), F=8 (XC-01..08), G=4 (XC-09,10,SM-03c,SM-09b A4 merged). **Tổng 9+6+4+5+4+8+4 = 40 TC**.
- **Critical TC (🔴)**: SM-03 (BR-SLA-02), SM-XC-07 (BR-RPT-01).
- **A4 inline merged 2026-05-10**: TC-BC-SM-XC-09, XC-10, SM-03c, SM-09b (was A4 proposal E8, E9, E13, E15).
- **A6 inline merged 2026-05-10**: TC-BC-SM-09c (G1 fill FR-IX-09 đợt cụ thể), SM-10b (G2 fill FR-IX-10 KH cụ thể).
- Mỗi BC ≥1 TC verify dropdown + filter + dimension + chart type khớp srs-fr-11:1054-1080 mapping table.

*Generated 2026-05-10 — Phase A step A3 (BMAD generate-e2e-tests)*
