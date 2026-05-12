# Test Cases PASS — tv-chuyen-sau

> **Nguồn**: result-tv-chuyen-sau-all.md
> **Ngày tổng hợp**: 2026-05-11
> **Phạm vi**: chỉ Result ∈ {PASS, PASS-DEVIATE, PASS-RESOLVED}

## Summary

| File test-case | Total TC nguồn | PASS | PASS-DEVIATE | PASS-RESOLVED |
|----------------|---------------:|-----:|-------------:|--------------:|
| 01-TC-FR-X1-01-quan-ly-tvcs | 44 | 12 | 0 | 0 |
| 02-TC-FR-X1-02-tim-kiem-tvcs | 20 | 16 | 0 | 0 |
| 03-TC-FR-X1-04-quan-ly-hspl | 20 | 12 | 0 | 0 |
| 04-TC-FR-X1-06-quan-ly-tu-lieu-pl | 21 | 0 | 0 | 0 |
| 05-TC-permission-matrix | 14 | 4 | 0 | 0 |
| 06-TC-FR-X1-03-05-07-API-inbound | 15 | 0 | 0 | 0 |
| **Tổng** | **134** | **44** | **0** | **0** |

---

## 01-TC-FR-X1-01-quan-ly-tvcs

> Source TC: `c:\HoaAG\LuatDN5\Ver3.1\output\test-cases\tv-chuyen-sau\01-TC-FR-X1-01-quan-ly-tvcs.md`
> Source report: `c:\HoaAG\LuatDN5\Ver3.1\output\execution-test\tv-chuyen-sau\report-01-TC-FR-X1-01-quan-ly-tvcs\Tcs-report\01-TC-FR-X1-01-quan-ly-tvcs-execution-report-2026-05-11.md`

| ID | TraceID (Mã SRS) | Tên Test Case | Pre-conditions (Tiền đề) | Test Data (Dữ liệu) | Các bước thực hiện | Kết quả mong đợi | Type (Happy/Negative/Edge) | Kết quả test (Result) | Chi tiết |
|----|------------------|---------------|--------------------------|---------------------|--------------------|------------------|----------------------------|------------------------|----------|
| TC-TVCS-001 | srs-fr-12 line 1057-1140 (SCR-X1-01 + SCR-X1-02) + line 1086-1095 + line 1129 | UI Verify SCR-X1-01 + SCR-X1-02 layout đầy đủ | ≥1 record TVCS sẵn cover 7 trạng thái | (không có test data) | Login cb_nv_tw_01; navigate sidebar TV pháp luật chuyên sâu; take_snapshot SCR-X1-01 list + SCR-X1-02 detail; verify breadcrumb, toolbar, 3 tab, filter-bar 6 control, table 10 cột, stepper 6 step, 6 accordion, action-bar conditional | Tất cả components hiển thị đúng vị trí + count badge + badge màu 7 trạng thái. Stepper SM-TVCS 6 step + nhánh HUY. Accordion 6 Công khai ẨN khi != DA_DUYET | UI Verify | PASS |  |
| TC-TVCS-002 | srs-fr-12 line 104 + 110 + 113 + 136 + 1483 (T1) | CREATE TVCS happy path — auto-gen mã TVCS-{YYYYMMDD}-{SEQ} | DN "DN-001" + CG "TVV-001" hoạt động + Lĩnh vực "DAN_SU" tồn tại | doanh_nghiep_id=DN-001, chuyen_gia_id=TVV-001, linh_vuc_id=DAN_SU, noi_dung_tu_van ~5KB | Login cb_nv_tw_01; vào SCR-X1-01; click [+ Thêm yêu cầu TV]; điền Accordion 1+2; click [Lưu]; verify POST /api/v1/tu-van-chuyen-sau | Toast thành công. Record mới mã regex TVCS-20260506-\d+, trạng thái TIEP_NHAN, don_vi_id auto-set, AUDIT_LOG ghi CREATE | Happy | PASS |  |
| TC-TVCS-003 | srs-fr-12 line 1073 (3 tab filter) + line 1100 (sort default) | READ list 3 tab + chuyển tab giữ filter | seed ≥1 record mỗi trạng thái 7 enum | (không có test data) | SCR-X1-01 default tab Chờ xử lý; verify TIEP_NHAN + PHAN_CONG; click tab Đang tư vấn; click tab Hoàn thành; verify GET API filter theo tab | Mỗi tab filter đúng nhóm trạng thái. Count badge match record. Sort default ngày tạo DESC | Happy | PASS |  |
| TC-TVCS-004 | srs-fr-12 line 1134 (mode sửa) + line 137 (BR-DATA-03) | UPDATE TVCS — chỉ enable khi trạng thái IN (TIEP_NHAN, DANG_TU_VAN) | TVCS-A trạng thái TIEP_NHAN, TVCS-B trạng thái HOAN_THANH | (không có test data) | Mở chi tiết TVCS-A; verify form editable; đổi tom_tat+ghi_chu; click [Lưu]; verify PUT 200; mở chi tiết TVCS-B (HOAN_THANH) verify read-only | TVCS-A update OK. AUDIT_LOG UPDATE với du_lieu_cu/moi. TVCS-B form read-only | Happy | PASS |  |
| TC-TVCS-005 | srs-fr-12 line 263 (BR-DATA-01 soft delete) | DELETE soft TVCS — owner thực hiện thành công | TVCS-X created_by=cb_nv_tw_01, trạng thái TIEP_NHAN | (không có test data) | Action [Hủy] hoặc icon Xóa trên row TVCS-X; confirm dialog; verify DELETE | Toast thành công. Record ẩn khỏi list (is_deleted=1). AUDIT_LOG ghi DELETE | Happy | PASS |  |
| TC-TVCS-006 | srs-fr-12 line 302 (ERR-TVCS-01) + line 108 | CREATE — noi_dung_tu_van trống → ERR-TVCS-01 | (không có pre-conditions) | (không có test data) | Form CREATE; bỏ trống Accordion 2 noi_dung_tu_van; click [Lưu] | Inline error nguyên văn "Nội dung tư vấn là bắt buộc". Form không submit. Count không đổi | Negative | PASS |  |
| TC-TVCS-018 | srs-fr-12 line 219-227 + line 1491-1492 (T9) | T9: TIEP_NHAN/PHAN_CONG → HUY (CB NV hủy) | TVCS-A TIEP_NHAN, TVCS-B PHAN_CONG | (không có test data) | Detail TVCS-A; [Hủy yêu cầu]; modal lý do; submit; repeat TVCS-B | Cả 2 → trang_thai=HUY. AUDIT_LOG + TB CG (TVCS-B) | Happy | PASS |  |
| TC-TVCS-020 | srs-fr-12 line 305 (ERR-TVCS-04) + line 1481-1492 | Invalid transition: TIEP_NHAN → DA_DUYET trực tiếp → ERR-TVCS-04 | TVCS-D TIEP_NHAN | (không có test data) | API direct POST phe-duyet | HTTP 400 + ERR-TVCS-04. trang_thai không đổi | Negative | PASS |  |
| TC-TVCS-028 | srs-fr-12 line 1082 + line 199-200 | Batch [Phân công CG hàng loạt] — chỉ enable khi tất cả TIEP_NHAN | seed 3 TIEP_NHAN + 1 PHAN_CONG | (không có test data) | Check 3 TIEP_NHAN verify enable; check thêm 1 PHAN_CONG verify disable; submit batch | Bước 2 enable, bước 3 disable, bước 5 cả 3 chuyển PHAN_CONG | Happy | PASS |  |
| TC-TVCS-038 | srs-fr-12 line 1543-1547 (BR-DATA-03) | BR-DATA-03 verify 7 common fields trên response CREATE TVCS | DN-001 + cg_01 + DAN_SU sẵn | (không có test data) | Form CREATE điền valid; [Lưu]; capture POST response; parse JSON | Response chứa 7 fields: id, created_at, updated_at, created_by, updated_by, is_deleted, don_vi_id | Happy | PASS |  |
| TC-TVCS-039 | srs-fr-12 line 304 (ERR-TVCS-03) + line 109 | ERR-TVCS-03: lĩnh vực không tồn tại → reject | Không tồn tại lĩnh vực DM-INVALID-99 | linh_vuc_id=DM-INVALID-99 | API direct POST với linh_vuc_id invalid | HTTP 400 + ma_loi:ERR-TVCS-03. Form không submit | Negative | PASS |  |
| TC-TVCS-041 | srs-fr-12 line 109 + line 112 | Boundary tom_tat 500 ký + ghi_chu 2000 ký exact / +1 reject | Form CREATE mở | (A)499+1999 (B)500+2000 (C)501 (D)2001 | Điền data A-D lần lượt [Lưu] | A+B PASS. C inline error tom_tat. D inline error ghi_chu | Edge | PASS |  |

---

## 02-TC-FR-X1-02-tim-kiem-tvcs

> Source TC: `c:\HoaAG\LuatDN5\Ver3.1\output\test-cases\tv-chuyen-sau\02-TC-FR-X1-02-tim-kiem-tvcs.md`
> Source report: `c:\HoaAG\LuatDN5\Ver3.1\output\execution-test\tv-chuyen-sau\report-02-TC-FR-X1-02-tim-kiem-tvcs\Tcs-report\02-TC-FR-X1-02-tim-kiem-tvcs-execution-report-2026-05-11.md`

| ID | TraceID (Mã SRS) | Tên Test Case | Pre-conditions (Tiền đề) | Test Data (Dữ liệu) | Các bước thực hiện | Kết quả mong đợi | Type (Happy/Negative/Edge) | Kết quả test (Result) | Chi tiết |
|----|------------------|---------------|--------------------------|---------------------|--------------------|------------------|----------------------------|------------------------|----------|
| TC-TVCS-TK-001 | srs-fr-12 line 1071-1083 + line 1100-1101 | UI Verify SCR-X1-01 filter-bar 8 control + 3 tab + pagination | ≥20 record TVCS | (không có test data) | Login cb_nv_tw_01; URL /tv-chuyen-sau/danh-sach; take_snapshot verify 8 control filter + 3 tab + pagination | 8 control hiển thị, 3 tab count badge, pagination 20/page, sort default DESC | UI Verify | PASS |  |
| TC-TVCS-TK-002 | srs-fr-12 line 341 + line 356 (BR-DATA-08) + line 1074 | Filter tu_khoa — FTS noi_dung_tu_van + ma_noi_dung + ten DN | seed TVCS-X noi_dung "hợp đồng lao động", TVCS-Y ten DN "ABC", TVCS-Z không match | (không có test data) | Filter tu_khoa lần lượt 3 keyword; verify network GET ?q= | Mỗi search trả đúng record. TVCS-Z không match | Happy | PASS |  |
| TC-TVCS-TK-003 | srs-fr-12 line 342-343 + line 357 + line 379 | Filter tu_ngay + den_ngay trên ngay_tu_van | seed TVCS ngày 2026-05-01, 05, 10 | (không có test data) | Filter tu_ngay=05-03 den_ngay=05-08 | Chỉ record 05-05 xuất hiện. Format dd/mm/yyyy | Happy | PASS |  |
| TC-TVCS-TK-004 | srs-fr-12 line 344 + line 358 + line 1075 | Filter chuyen_gia_id — chỉ TVCS của CG được chọn | seed cg_01 3 record, cg_02 2 record | (không có test data) | Filter Chuyên gia=cg_01 | 3 record cg_01 hiển thị, cg_02 ẩn | Happy | PASS |  |
| TC-TVCS-TK-005 | srs-fr-12 line 345 + line 359 + line 1077 | Filter linh_vuc_id — chỉ TVCS thuộc lĩnh vực | seed DAN_SU 4, HINH_SU 2 | (không có test data) | Filter Lĩnh vực=DAN_SU | 4 record DAN_SU | Happy | PASS |  |
| TC-TVCS-TK-006 | srs-fr-12 line 346 + line 360 + line 1078 | Filter trang_thai — 7 enum SM-TVCS | seed 1 record mỗi trạng thái | (không có test data) | Filter trang_thai DA_DUYET / HUY / TIEP_NHAN | Mỗi filter trả 1 record matching | Happy | PASS |  |
| TC-TVCS-TK-007 | srs-fr-12 line 347 + line 362 + line 1083 | Filter page >=1 — pagination chuyển trang | seed ≥45 TVCS | (không có test data) | Page=1, 2, 3 | page1: 20, page2: 20, page3: 5. Sort DESC. Network ?page=2&page_size=20 | Happy | PASS |  |
| TC-TVCS-TK-008 | srs-fr-12 line 348 + line 362 (BR-DATA-07) | Filter page_size boundary — 1, 20 default, 100 max | seed ≥120 TVCS | (không có test data) | page_size=1, default, 100 | Cả 3 boundary OK theo BR-DATA-07 | Edge | PASS |  |
| TC-TVCS-TK-009 | srs-fr-12 line 361 + line 1101 + AC line 398 | AND logic — kết hợp 3 filter (tu_khoa + chuyen_gia + linh_vuc) | seed TVCS-A/B/C khác combinations | (không có test data) | Filter tu_khoa+chuyen_gia=cg_01+linh_vuc=DAN_SU | Chỉ TVCS-A khớp 3 điều kiện AND | Happy | PASS |  |
| TC-TVCS-TK-010 | srs-fr-12 line 356 + Phụ lục B BR-DATA-08 | Edge unicode tiếng Việt unaccent — "đào tạo" match "dao tao" | seed TVCS-X "đào tạo nhân viên" | (không có test data) | Filter tu_khoa "dao tao" (không dấu); repeat "ĐÀO TẠO" UPPERCASE | Cả 2 trả TVCS-X. BR-DATA-08 unaccent + case-insensitive | Edge | PASS |  |
| TC-TVCS-TK-012 | srs-fr-12 BR-EC-13 | Negative SQL injection / XSS — sanitize BR-EC-13 max 200 ký | (không có pre-conditions) | 3 payload | tu_khoa=' OR 1=1--; tu_khoa=<script>; tu_khoa=250 ký | Cả 3 sanitize, không leak/exec; 250 ký truncate/reject; không 500 | Negative | PASS |  |
| TC-TVCS-TK-013 | srs-fr-12 line 348 + line 362 (BR-DATA-07) | Negative page_size > 100 hoặc <= 0 → BR-DATA-07 cap/reject | (không có pre-conditions) | (không có test data) | API direct page_size=200, 0, -5 | Cap=100 hoặc 400; 0/-5 → 400 page_size phải >=1 | Negative | PASS |  |
| TC-TVCS-TK-016 | srs-fr-12 line 341 | Boundary tu_khoa: chỉ space (1-5 ký whitespace) → trim/empty handling | (không có pre-conditions) | "     " 5 space; "\t\n"; "" | tu_khoa whitespace; submit | Cả 3 trim → empty → trả full list. KHÔNG 500 | Edge | PASS |  |
| TC-TVCS-TK-017 | srs-fr-12 BR-EC-13 | Boundary tu_khoa max 200 ký exact + 201 ký reject (BR-EC-13) | (không có pre-conditions) | 200 ký exact / 201 ký | tu_khoa 200 → Submit; 201 → Submit | 200 PASS. 201 inline error/cap | Edge | PASS |  |
| TC-TVCS-TK-018 | srs-fr-12 line 347 + line 1083 | Deep page navigation: page=99999 ngoài range → empty + status 200 | seed ≤100 TVCS | (không có test data) | URL ?page=99999&page_size=20 | HTTP 200 data:[] empty. KHÔNG 500/OOM | Edge | PASS |  |
| TC-TVCS-TK-020 | srs-fr-12 line 391 (INF-TVCS-TK-01) + line 1081 | INF-TVCS-TK-01: Tìm kiếm không có kết quả → message INFO nguyên văn | seed scope TW ≥10 TVCS không match keyword test | (không có test data) | URL danh-sach; tu_khoa chuỗi unique; [Tìm kiếm]; verify GET API + UI empty | HTTP 200 data:[]. UI nguyên văn "Không tìm thấy nội dung tư vấn phù hợp" | Negative | PASS |  |

---

## 03-TC-FR-X1-04-quan-ly-hspl

> Source TC: `c:\HoaAG\LuatDN5\Ver3.1\output\test-cases\tv-chuyen-sau\03-TC-FR-X1-04-quan-ly-hspl.md`
> Source report: `c:\HoaAG\LuatDN5\Ver3.1\output\execution-test\tv-chuyen-sau\report-03-TC-FR-X1-04-quan-ly-hspl\Tcs-report\03-TC-FR-X1-04-quan-ly-hspl-execution-report-2026-05-11.md`

| ID | TraceID (Mã SRS) | Tên Test Case | Pre-conditions (Tiền đề) | Test Data (Dữ liệu) | Các bước thực hiện | Kết quả mong đợi | Type (Happy/Negative/Edge) | Kết quả test (Result) | Chi tiết |
|----|------------------|---------------|--------------------------|---------------------|--------------------|------------------|----------------------------|------------------------|----------|
| TC-HSPL-001 | FR-X.1-04 / SRS line 519, 626-640 | Verify tab "Hồ sơ PL" trong MH-07.2: Toolbar + Table 11 cột + 3 trạng thái | cb_nv_tw_01 đăng nhập; DN-TW-001 + ≥3 HSPL 3 trạng thái + ≥1 có file | URL /doanh-nghiep/{DN-TW-001-id} → tab Hồ sơ PL | Login; navigate DN-TW-001 chi tiết → MH-07.2; click tab Hồ sơ PL; quan sát | Toolbar [+ Thêm hồ sơ]; Filter-bar 5 ô; Table 11 cột; Pagination 20/page; Empty state nguyên văn | UI Verify | PASS |  |
| TC-HSPL-002 | FR-X.1-04 / BR-DATA-04 + SRS line 568-577 | CREATE HSPL thành công với đầy đủ thông tin + auto-gen mã HSPL-{YYYYMMDD}-{SEQ} | cb_nv_tw_01; DN-TW-001 cùng BTP-TW; Lĩnh vực DAN_SU | 10 field: ten_ho_so, loai_ho_so=GIAY_PHEP, ngay_cap=2026-01-15, file 5MB PDF, etc. | Click [+ Thêm hồ sơ]; điền form; upload file 5MB; [Lưu] | INSERT với mã regex HSPL-20260506-\d+. 7 common fields BR-DATA-03. AUDIT_LOG CREATE. Toast | Happy | PASS |  |
| TC-HSPL-003 | FR-X.1-04 / SRS line 606-614 | READ chi tiết HSPL: full record + DN liên kết + danh sách file | cb_nv_tw_01; HSPL-20260101-001 + 2 file đính kèm | (không có test data) | Click icon [Xem]; quan sát modal/page chi tiết | GET 200 OK full record + DN info + array file. Modal 11 field readonly. Section File 2 mục | Happy | PASS |  |
| TC-HSPL-004 | FR-X.1-04 / SRS line 579-586 | UPDATE HSPL: đổi trạng thái HIEU_LUC → THU_HOI + thêm mô tả lý do | cb_nv_tw_01; HSPL-20260101-002 trạng thái HIEU_LUC | trang_thai=THU_HOI, mo_ta lý do | Row HSPL-002 [Sửa]; đổi trạng thái dropdown; cập nhật mô tả; [Lưu] | UPDATE SET trang_thai='THU_HOI'. AUDIT_LOG du_lieu_cu/moi. Toast. Reload badge đỏ | Happy | PASS |  |
| TC-HSPL-006 | FR-X.1-04 / SRS line 616-624 | Export Excel HSPL với filter hiện tại + max 10k rows + 8 cột nguyên văn | cb_nv_tw_01; ≥30 HSPL BTP-TW | Filter loai=GIAY_PHEP + trang_thai=HIEU_LUC | Áp filter; [Xuất Excel]; đợi download; mở .xlsx | Network GET export response xlsx content-type. 8 cột nguyên văn. >10k cap+warning | Happy | PASS |  |
| TC-HSPL-007 | FR-X.1-04 / SRS line 597-604 | Tìm kiếm AND logic 3 filter: keyword + loại + DN | cb_nv_tw_01; seed 10 HSPL khác combinations | keyword="Giấy phép" + loai=GIAY_PHEP + DN=DN-TW-001 | Filter-bar 3 ô; [Tìm kiếm] | AND logic. 3 record. Pagination "Tổng: 3" | Happy | PASS |  |
| TC-HSPL-008 | FR-X.1-04 / SRS line 555 | Tìm kiếm boundary date: tu_ngay = den_ngay (cùng ngày) | cb_nv_tw_01; 1 HSPL ngay_cap=2026-03-15 | tu_ngay=2026-03-15, den_ngay=2026-03-15 | Filter; [Tìm kiếm] | WHERE >= AND <= boundary inclusive. 1 record HSPL ngay_cap=03-15 | Edge | PASS |  |
| TC-HSPL-009 | INF-HSPL-01 (line 658) | Tìm kiếm INFO: keyword không có kết quả → message "Không tìm thấy hồ sơ pháp lý phù hợp" | cb_nv_tw_01 | keyword="zxywvut-không-có-kết-quả-xyz" | Filter keyword không match; [Tìm kiếm] | Empty array. Empty state nguyên văn line 658 | Negative | PASS | (Note: Export endpoint marked BUG NEW in report nhưng actually WORKS — opposite of TVCS missing.) |
| TC-HSPL-010 | ERR-HSPL-01 (line 652) | ERR-HSPL-01: Tên hồ sơ trống → reject INSERT | cb_nv_tw_01; DN-TW-001 | ten_ho_so="", các field khác valid | [+ Thêm hồ sơ]; bỏ trống tên; [Lưu] | KHÔNG INSERT. Inline error nguyên văn "Tên hồ sơ pháp lý là bắt buộc" | Negative | PASS |  |
| TC-HSPL-012 | ERR-HSPL-02 (line 653) | ERR-HSPL-02: doanh_nghiep_id không tồn tại → reject | cb_nv_tw_01 | doanh_nghiep_id="DN-INVALID-99999" | API direct POST | FK fail. 400 nguyên văn "Doanh nghiệp không tồn tại hoặc đã bị xóa" | Negative | PASS |  |
| TC-HSPL-013 | ERR-HSPL-05 + ERR-HSPL-06 | ERR-HSPL-05 + ERR-HSPL-06: Loại hồ sơ không hợp lệ + tu_ngay > den_ngay | cb_nv_tw_01 | loai="LOAI_KHONG_HOP_LE"; tu_ngay=12-31, den_ngay=01-01 | API POST invalid loại; UI search tu>den | Lần 1: 400 nguyên văn ERR-HSPL-05. Lần 2: inline ERR-HSPL-06 | Negative | PASS |  |
| TC-HSPL-020 | FR-X.1-04 / SRS line 540 + line 1374 | Edge SM HSPL: HSPL với ngay_het_han < today render badge "HET_HAN" | cb_nv_tw_01; HSPL-EXPIRED-001 hết hạn yesterday; HSPL-VALID-001 tương lai | (không có test data) | Tab Hồ sơ PL; take_snapshot badge; click [Xem] EXPIRED; verify GET API computed; filter HET_HAN | Row EXPIRED badge HET_HAN cam dù field gốc HIEU_LUC. Row VALID xanh. Filter HET_HAN trả EXPIRED | Edge / Render-side state | PASS |  |

---

## 05-TC-permission-matrix

> Source TC: `c:\HoaAG\LuatDN5\Ver3.1\output\test-cases\tv-chuyen-sau\05-TC-permission-matrix.md`
> Source report: `c:\HoaAG\LuatDN5\Ver3.1\output\execution-test\tv-chuyen-sau\report-05-TC-permission-matrix\Tcs-report\05-TC-permission-matrix-execution-report-2026-05-11.md`

| ID | TraceID (Mã SRS) | Tên Test Case | Pre-conditions (Tiền đề) | Test Data (Dữ liệu) | Các bước thực hiện | Kết quả mong đợi | Type (Happy/Negative/Edge) | Kết quả test (Result) | Chi tiết |
|----|------------------|---------------|--------------------------|---------------------|--------------------|------------------|----------------------------|------------------------|----------|
| TC-PERM-001 | Action-bar conditional theo trạng thái + role overview §2.5 (line 213-220) + Permission Matrix §2.4 line 171 | UI Verify role-based visibility action button trên SCR-X1-01 / SCR-X1-02 | Seed 1 TVCS mỗi state TIEP_NHAN/DA_DUYET/CHO_PHE_DUYET/PHAN_CONG cho cg_01; mỗi user đăng nhập riêng phiên | (không có test data) | Loop 4 role login: cb_nv_tw, cb_pd_tw, cg_01, qtht_01; SCR-X1-01 toolbar + cột Hành động; SCR-X1-02 action-bar | CB_NV: toolbar + Thêm + Xuất Excel + action-bar CRUD. CB_PD: chỉ Xem + Phê duyệt/Từ chối. CG: Chấp nhận/Từ chối. QTHT: read-only | UI Verify | PASS | cb_nv_tw_01 GET trang TVCS 27 records (toàn bộ env). BR-AUTH-08 TW cấp có cross-tenant Read scope verified. Verify với HSPL 25 records cũng OK. |
| TC-PERM-002 | BR-AUTH-01 line 1525-1529 | BR-AUTH-01 Tier 1: CB nội bộ login U/P + TOTP, anonymous redirect /login | Logout / clear cookie. OTP=666666 fix cứng | username cb_nv_tw_01, password đúng, OTP 666666 | Browser ẩn danh navigate URL; /login U/P; OTP 666666; verify post-login redirect | 302 → /login. Tier 1 flow OK. Redirect /tv-chuyen-sau/danh-sach. AUDIT LOGIN | Negative + Happy | PASS | IDOR direct GET cùng đơn vị OK. Random TVCS GET 200. UUID không tồn tại → 404 ERR-VAL-VII-02-01 "Bản ghi không tồn tại". KHÔNG IDOR bypass leak. |
| TC-PERM-003 | BR-AUTH-01 line 1525-1529 + line 164 + line 1136 + Permission Matrix §2.4 line 171 | BR-AUTH-01 Tier 2: DN không dùng route Tier 1; CG/TVV truy cập SCR-X1-02 sau SSO | Logout. Tier 1 /login form. cg_01 đã có TVCS PHAN_CONG tvcs-pc-cg01 | username dn_01, cg_01 | /login Tier 1 với dn_01 → reject; /login với cg_01 → reject SSO; /login-vneid OIDC cg_01; navigate /tv-chuyen-sau/chi-tiet/tvcs-pc-cg01 | DN reject Tier 1 redirect SSO. CG reject Tier 1 redirect SSO. CG sau SSO truy cập detail thấy [Chấp nhận]/[Từ chối] | Negative + Happy hybrid | PASS | Invalid UUID format hard-reject. GET /api/v1/noi-dung-tu-van-cs/not-a-uuid → 404. BE phân biệt invalid format vs not-found OK. |
| TC-PERM-004 | BR-AUTH-05 SM-TVCS line 1489 + AC nhóm UC147 line 198 | BR-AUTH-05 Happy: CB_PD_TW phê duyệt TVCS cấp TW (cùng cấp) | Seed 1 TVCS thuộc TW, trạng thái CHO_PHE_DUYET | (không có test data) | Login cb_pd_tw_01; SCR-X1-01 tab Đang tư vấn → record CHO_PHE_DUYET; click; SCR-X1-02; [Phê duyệt]; confirm | Action-bar Phê duyệt/Từ chối. Sau confirm CHO_PHE_DUYET → DA_DUYET (T7). TB DN. AUDIT PHE_DUYET. Record sang Hoàn thành | Happy | PASS | Random UUID not exist → 404 ERR-VAL-VII-02-01 "Bản ghi không tồn tại" nguyên văn match SRS quote. |

---

## Skipped

Các section sau KHÔNG có TC nào đạt Result ∈ {PASS, PASS-DEVIATE, PASS-RESOLVED}:

- **04-TC-FR-X1-06-quan-ly-tu-lieu-pl** — 21/21 TC BLOCKED do Backend KHÔNG implement module TLPL/UC152 (16 path API discovery trả 404). Đề xuất: Dev implement UC152 hoặc xác nhận deprecated.
- **06-TC-FR-X1-03-05-07-API-inbound-side-effect** — 15/15 TC BLOCKED do endpoint inbound TVCS/HSPL/DG/Phiên TV/Nhật ký đều MISSING. Report 06 dùng prefix ID khác không khớp 15 TC nguồn.
