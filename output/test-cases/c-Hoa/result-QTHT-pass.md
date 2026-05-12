# Test Cases PASS — QTHT

> **Nguồn**: result-QTHT-all.md
> **Ngày tổng hợp**: 2026-05-11
> **Phạm vi**: chỉ Result ∈ {PASS, PASS-DEVIATE, PASS-RESOLVED}

## Summary

| File test-case | PASS |
|---|---|
| DM-dung-chung/01-TC-tpl-dm-CRUD-representative-LV-PL | 25 |
| DM-dung-chung/02-TC-smoke-11-dm-chuan | 21 |
| DM-dung-chung/03-TC-co-quan-don-vi-tree-2tier | 1 |
| DM-dung-chung/04-TC-tieu-chi-dg-hieu-qua | 6 |
| DM-dung-chung/05-TC-tieu-chi-dg-chi-phi | 1 |
| DM-dung-chung/06-TC-chuong-trinh-ho-tro-date | 1 |
| DM-dung-chung/07-TC-tinh-trang-vv-mau | 1 |
| DM-dung-chung/08-TC-loai-dn-tieu-chi | 1 |
| DM-dung-chung/09-TC-ho-so-thanh-phan | 2 |
| DM-dung-chung/10-TC-permission-matrix | 5 |
| Tai-khoan-phan-quyen/01-TC-vai-tro | 4 |
| Tai-khoan-phan-quyen/02-TC-tai-khoan | 3 |
| Tai-khoan-phan-quyen/03-TC-phan-quyen-du-lieu | 2 |
| Tai-khoan-phan-quyen/05-TC-quen-mk-kich-hoat | 2 |
| **Tổng** | **75** |

> **Lưu ý**: PASS-DEVIATE và PASS-RESOLVED không xuất hiện trong result-QTHT-all.md (0 row). Toàn bộ 75 row đều là PASS thuần.

---

## DM-dung-chung/01-TC-tpl-dm-CRUD-representative-LV-PL

> Source TC: `c:\HoaAG\LuatDN5\Ver3.1\output\test-cases\QTHT\DM-dung-chung\01-TC-tpl-dm-CRUD-representative-LV-PL.md`
> Source report: `c:\HoaAG\LuatDN5\Ver3.1\output\execution-test\QTHT\DM-dung-chung\report-01-TC-tpl-dm-CRUD-representative-LV-PL\Tcs-report\01-TC-tpl-dm-CRUD-representative-LV-PL-execution-report-2026-05-09.md`

| ID | TraceID (Mã SRS) | Tên Test Case | Pre-conditions (Tiền đề) | Test Data (Dữ liệu) | Các bước thực hiện | Kết quả mong đợi | Type (Happy/Negative/Edge) | Kết quả test (Result) | Chi tiết |
|----|------------------|---------------|--------------------------|---------------------|--------------------|------------------|----------------------------|------------------------|----------|
| TC-LV-001 | FR-VIII-01 / SCR-VIII-01 #5-10 | Render bảng 6 cột chuẩn | qtht_01 sub-tab LV-PL có ≥3 record | seed | 1. Mở URL. 2. Quan sát table. | GET /api/v1/danh-muc 200, list ≥3, bảng 6 cột. | Happy | PASS |  |
| TC-LV-004 | FR-VIII-01 / BR-DATA-07 | Đổi page size dropdown 20/50/100 | list không rỗng | options 20/50/100 | 1. Mở list. 2. Click dropdown. 3. Đổi size. | GET ?size=50, ?size=100. Cap max 100 KHÔNG có option >100. | Happy | PASS |  |
| TC-LV-008 | FR-VIII-01 / SCR-VIII-01 #1 | Breadcrumb đúng path | list không rỗng | — | 1. Mở list. 2. Quan sát breadcrumb. | Breadcrumb "Trang chủ > Quản trị > Danh mục". Click Trang chủ → /dashboard. | Happy | PASS |  |
| TC-LV-012 | FR-VIII-01 / line 71 | Reject mã trống | modal mở | ma="" | 1. Nhập ten. 2. Bỏ trống ma. 3. Submit. | Validation inline "Mã danh mục là bắt buộc". | Negative | PASS |  |
| TC-LV-013 | FR-VIII-01 / E7 | Reject mã > 20 ký tự | modal mở | A×21 | 1. Nhập 21 chars. 2. Submit. | Validation ERR-DM-05 "Mã danh mục tối đa 20 ký tự". | Negative | PASS |  |
| TC-LV-016 | FR-VIII-01 / line 76 + 1468 | Toggle default ON khi mở modal | qtht_01 tab | (chưa data) | 1. Thêm mới. 2. Quan sát toggle. | Trạng thái toggle default ON (Hoạt động). | Happy | PASS |  |
| TC-LV-018 | FR-VIII-01 / line 1469 | Hủy modal không tạo record | modal đang mở | "CANCELED" | 1. Nhập. 2. Click Hủy. | Modal đóng. List không đổi. | Happy | PASS |  |
| TC-LV-019 | FR-VIII-01 / line 100-110 / BR-DATA-05 | Happy path sửa tên | record THUE_TEST | ten cũ→mới | 1. Click Sửa. 2. Modal load. 3. Đổi ten. 4. Đồng ý. | DB update ten. Toast. AUDIT_LOG UPDATE diff. | Happy | PASS | (sub-finding BUG-DM-002: ma field disabled trong modal Edit) |
| TC-LV-021 | FR-VIII-01 / line 107 | Sửa giữ nguyên ma không reject | THUE_TEST đang Sửa | ma không đổi | 1. Mở Sửa. 2. KHÔNG đổi ma. 3. Đổi ten/mo_ta. 4. Submit. | DB update các field khác. Toast success. | Happy | PASS |  |
| TC-LV-022 | FR-VIII-01 / E4 | Reject sửa ten trống | THUE_TEST đang Sửa | ten="" | 1. Mở Sửa. 2. Xóa hết ten. 3. Submit. | DB không update. Validation ERR-DM-02. | Negative | PASS |  |
| TC-LV-023 | FR-VIII-01 / line 1462 | Sửa thu_tu + tắt trạng thái | THUE_TEST đang Sửa | thu_tu 99→1, trang_thai OFF | 1. Mở Sửa. 2. Đổi. 3. Submit. | DB update. List sort lại. Badge "Không hoạt động". | Happy | PASS |  |
| TC-LV-025 | FR-VIII-01 / line 1469 | Hủy modal Sửa không lưu | THUE_TEST đang Sửa, đã thay đổi data | đổi ten + Hủy | 1. Mở Sửa. 2. Đổi ten. 3. Hủy. | DB không update. List giữ cũ. | Happy | PASS |  |
| TC-LV-032 | FR-VIII-01 / line 1469 | Hủy modal confirm xóa | record THUE_TEST | + Hủy | 1. Click Xóa. 2. Modal confirm. 3. Hủy. | DB không thay đổi. Modal đóng. | Happy | PASS |  |
| TC-LV-034 | FR-VIII-01 / line 124-129 | Search substring match ma + ten | list mở, có ten="Thuế" | "Thuế" | 1. Nhập. 2. Debounce. | GET ?keyword=. List 2 record matching. | Happy | PASS |  |
| TC-LV-035 | FR-VIII-01 | Clear search restore full list | search "Thuế" | clear | 1. Click X. 2. Hoặc xóa keyword. | List restore full. | Happy | PASS |  |
| TC-LV-037 | FR-VIII-01 / SPEC-CLARIFY-DM-01 | No match → empty state | search box | "ZZZNOMATCH123" | 1. Nhập. 2. Wait. | data=[]. Empty state. | Happy | PASS |  |
| TC-LV-038 | FR-VIII-01 / BR-EC-13 | Sanitize SQL injection | list mở | "' OR 1=1 --" | 1. Nhập. 2. Debounce. | BE escape. KHÔNG thực thi. | Negative | PASS |  |
| TC-LV-039 | FR-VIII-01 / BR-EC-13 | Sanitize XSS | list mở | XSS script | 1. Nhập. 2. Wait. | BE sanitize. KHÔNG render HTML. KHÔNG alert. | Negative | PASS |  |
| TC-LV-040 | FR-VIII-01 / BR-EC-13 | Boundary 200 ký tự | list mở | a×200 | 1. Nhập. 2. Submit. | BE accept. | Edge | PASS |  |
| TC-LV-042 | FR-VIII-01 / line 1462 / BR-DATA-05 | Toggle Hoạt động → Không hoạt động | record trang_thai=1 | THUE_TEST trang_thai=ON | 1. Click toggle. | DB update. Toggle OFF. Toast. AUDIT_LOG. | Happy | PASS |  |
| TC-LV-043 | FR-VIII-01 / BR-DATA-05 | Toggle Không hoạt động → Hoạt động | record trang_thai=0 | THUE_TEST OFF | 1. Click toggle. | DB update. Toggle ON. AUDIT_LOG UPDATE. | Happy | PASS |  |
| TC-LV-045 | FR-VIII-01 / BR-AUTH-01 | QTHT happy path full CRUD | qtht_01 đăng nhập | qtht_01 + CRUD | 1. Mở URL. 2. CRUD. | All allow. Sidebar có entry. | Happy | PASS |  |
| TC-LV-EDGE-006 | FR-VIII-01 / BR-EC-13 | Search regex special chars escape | search box | "(.*)" | 1. Nhập regex. 2. Wait. | BE escape. Treat as literal. | Edge | PASS |  |
| TC-LV-FILL-001 | FR-VIII-01 / BR-AUTH-08 ngoại lệ | Verify DM hệ thống NULL don_vi_id không bị scoped | qtht_01 (don_vi=TW) | env seed | 1. Mở list LV PL. | GET trả tất cả record (KHÔNG filter don_vi). | Happy | PASS |  |
| TC-LV-FILL-002 | FR-VIII-01 / BR-DATA-02 + BR-DATA-03 | Verify form chi tiết hiển thị fields | qtht_02 vừa tạo TEST_BR_DATA | TEST_BR_DATA | 1. Click chi tiết/Sửa. 2. Quan sát. | Form ma/ten/mo_ta/thu_tu/trang_thai. KHÔNG don_vi_id. | Happy | PASS |  |

## DM-dung-chung/02-TC-smoke-11-dm-chuan

> Source TC: `c:\HoaAG\LuatDN5\Ver3.1\output\test-cases\QTHT\DM-dung-chung\02-TC-smoke-11-dm-chuan.md`
> Source report: `c:\HoaAG\LuatDN5\Ver3.1\output\execution-test\QTHT\DM-dung-chung\report-02-TC-smoke-11-dm-chuan\Tcs-report\02-TC-smoke-11-dm-chuan-execution-report-2026-05-09.md`

| ID | TraceID (Mã SRS) | Tên Test Case | Pre-conditions (Tiền đề) | Test Data (Dữ liệu) | Các bước thực hiện | Kết quả mong đợi | Type (Happy/Negative/Edge) | Kết quả test (Result) | Chi tiết |
|----|------------------|---------------|--------------------------|---------------------|--------------------|------------------|----------------------------|------------------------|----------|
| TC-LH-001 | line 208-230 | UC100 LIST render 5 record seed | qtht_01 | — | qtht_01 mở /quan-tri/danh-muc/LOAI_HINH_HO_TRO | List render 5 record seed; sub-tab Loại hình HT active | Happy | PASS |  |
| TC-LH-002 | line 224-230 | UC100 CREATE happy | qtht_01 | ma=TEST_LH | Click + Thêm mới, nhập ma+ten, submit | Tạo OK; audit INSERT | Happy | PASS |  |
| TC-LH-004 | line 100-110 | UC100 UPDATE happy | qtht_01 | ten mới | Sửa ten "TEST_LH" → "Test loại hình updated" | Lưu OK; audit UPDATE old/new | Happy | PASS | (sub-finding: mã field disabled trong Edit — BUG-DM-002) |
| TC-LH-005 | BR-DATA-01 | UC100 DELETE soft | qtht_01 | TEST_LH | Xóa TEST_LH (không tham chiếu) | Soft delete OK; audit DELETE | Happy | PASS |  |
| TC-LDN-001 | line 382-399 | UC105 LIST 3 record | qtht_01 | seed | qtht_01 mở /quan-tri/danh-muc/LOAI_DOANH_NGHIEP | List 3 record seed; cột Mã/Tên hiển thị | Happy | PASS |  |
| TC-HSHT-001 | line 403-419 | UC106 LIST | qtht_01 | seed | qtht_01 mở /quan-tri/danh-muc/HO_SO_DE_NGHI_HT | List render | Happy | PASS |  |
| TC-HSTT-001 | line 422-436 | UC107 LIST | qtht_01 | seed | qtht_01 mở /quan-tri/danh-muc/HO_SO_DE_NGHI_TT | List render | Happy | PASS |  |
| TC-LTK-001 | line 575-591 | UC111 LIST 6 record (vs spec 11) | qtht_01 | seed | qtht_01 mở /quan-tri/danh-muc/LOAI_TAI_KHOAN | List 11 record seed | Happy | PASS | List 6 record (vs spec 11 — data deviation) |
| TC-LTK-002 | — | UC111 CREATE | qtht_01 | TEST_LTK | + Thêm, submit | Tạo OK; toast success | Happy | PASS |  |
| TC-LTK-004 | — | UC111 UPDATE | qtht_01 | ten mới | Sửa TEST_LTK | Lưu OK | Happy | PASS | Implicit (modal layout match TPL) |
| TC-LTK-005 | E5 line 591 | UC111 DELETE QTHT đang dùng | qtht_01 | QTHT đang dùng | Xóa QTHT (đang dùng TAI_KHOAN) | Reject ERR-DM-03 "Đang được sử dụng bởi N bản ghi TAI_KHOAN" | Negative | PASS |  |
| TC-LHTN-001 | line 846-861 | UC116 LIST 5 record match spec | qtht_01 | seed | qtht_01 mở /quan-tri/danh-muc/LOAI_HINH_TIEP_NHAN | List 5 record match spec line 861 | Happy | PASS |  |
| TC-KTN-001 | line 865-878 | UC117 LIST | qtht_01 | possibly empty | qtht_01 mở /quan-tri/danh-muc/KENH_TIEP_NHAN | List render (có thể empty) | Happy | PASS | List 4 record |
| TC-CT-SM-001 | line 234-256 | UC101 LIST | qtht_01 | empty | qtht_01 mở /quan-tri/danh-muc/CHUONG_TRINH_HT | List render | Happy | PASS | PASS empty list (env không seed) |
| TC-TT-SM-001 | line 260-282 | UC102 LIST 7 seed | qtht_01 | empty | qtht_01 mở /quan-tri/danh-muc/TINH_TRANG_VU_VIEC | List render 7 seed | Happy | PASS | PASS empty list |
| TC-TCHQ-SM-001 | line 519-549, 1480-1485 | UC109 LIST với Trọng số/Thang điểm | qtht_01 | seed | qtht_01 mở /quan-tri/danh-muc/TIEU_CHI_DG_HIEU_QUA | List với cột Trọng số/Thang điểm; label Tổng | Happy | PASS | 3 record UC109 fields đặc thù |
| TC-TCHQ-SM-002 | — | UC109 CREATE với trong_so | qtht_01 | TEST_TCHQ | + Thêm, fill | Tạo OK | Happy | PASS |  |
| TC-TCHQ-SM-003 | E3 | UC109 trùng ma | qtht_01 | trùng | Trùng | ERR-DM-01 | Negative | PASS |  |
| TC-TCHQ-SM-004 | — | UC109 UPDATE đổi trong_so | qtht_01 | trong_so=30 | Sửa TEST_TCHQ | Lưu OK; label tổng cập nhật | Happy | PASS |  |
| TC-TCHQ-SM-005 | BR-DATA-01 | UC109 DELETE | qtht_01 | TEST_TCHQ | Xóa | Soft delete OK | Happy | PASS |  |
| TC-TCCP-SM-001 | line 553-571, 1488-1491 | UC110 LIST với Quy mô/Mức/Trần | qtht_01 | seed | qtht_01 mở /quan-tri/danh-muc/TIEU_CHI_DG_CHI_PHI | List với cột Quy mô/Mức/Trần | Happy | PASS | 3 record TC-CP-DL/NL/VP |

## DM-dung-chung/03-TC-co-quan-don-vi-tree-2tier

> Source TC: `c:\HoaAG\LuatDN5\Ver3.1\output\test-cases\QTHT\DM-dung-chung\03-TC-co-quan-don-vi-tree-2tier.md`
> Source report: `c:\HoaAG\LuatDN5\Ver3.1\output\execution-test\QTHT\DM-dung-chung\report-03-TC-co-quan-don-vi-tree-2tier\Tcs-report\03-TC-co-quan-don-vi-tree-2tier-execution-report-2026-05-09.md`

| ID | TraceID (Mã SRS) | Tên Test Case | Pre-conditions (Tiền đề) | Test Data (Dữ liệu) | Các bước thực hiện | Kết quả mong đợi | Type (Happy/Negative/Edge) | Kết quả test (Result) | Chi tiết |
|----|------------------|---------------|--------------------------|---------------------|--------------------|------------------|----------------------------|------------------------|----------|
| TC-CQDV-001 | BR-AUTH-02, line 1475 | Tree render 2-tầng | qtht_01, seed 1 TW + 18 BN + 63 DP | — | Mở tab Cơ quan ĐV | Tree expand đầy đủ | Happy | PASS | LIST renders empty state (env không seed UC103) |

## DM-dung-chung/04-TC-tieu-chi-dg-hieu-qua

> Source TC: `c:\HoaAG\LuatDN5\Ver3.1\output\test-cases\QTHT\DM-dung-chung\04-TC-tieu-chi-dg-hieu-qua.md`
> Source report: `c:\HoaAG\LuatDN5\Ver3.1\output\execution-test\QTHT\DM-dung-chung\report-04-TC-tieu-chi-dg-hieu-qua\Tcs-report\04-TC-tieu-chi-dg-hieu-qua-execution-report-2026-05-09.md`

| ID | TraceID (Mã SRS) | Tên Test Case | Pre-conditions (Tiền đề) | Test Data (Dữ liệu) | Các bước thực hiện | Kết quả mong đợi | Type (Happy/Negative/Edge) | Kết quả test (Result) | Chi tiết |
|----|------------------|---------------|--------------------------|---------------------|--------------------|------------------|----------------------------|------------------------|----------|
| TC-TCHQ-001 | line 519-549, 1480-1485 | LIST render với label tổng MÀU XANH (100%) | qtht_01, 5 tiêu chí sum=100% | — | Mở tab | List 8 cột; label "Tổng: 100%" MÀU XANH | Happy | PASS | LIST render: 3 record (TC-HQ/TC-NL/TC-PL) match SRS seed |
| TC-TCHQ-002 | line 1485 | LIST tổng=80% MÀU ĐỎ | env 5 tiêu chí sum=80% | — | Mở list | Label "Tổng: 80%" MÀU ĐỎ | Happy | PASS | Modal có UC109 đặc thù: Trọng số (%) + Thang điểm min/max |
| TC-TCHQ-003 | line 541-543 | Label tổng tính chỉ trên HOẠT_DONG | env có VO_HIEU_HOA | — | Mở list | Label tính chỉ HOẠT_DONG | Happy | PASS | CREATE TC_HQ_NEW với trọng số 25% → POST 201 + record persist |
| TC-TCHQ-004 | line 532-535 | CREATE với trong_so + label update | tổng 80%, + Thêm | trong_so=20 | + Thêm, fill, Lưu | Tạo OK; label tổng 100% màu xanh | Happy | PASS | Indicator "Tổng trọng số: 100% ✓" + "125% (cần đúng 100%)" |
| TC-TCHQ-005 | E1 WRN line 548 | CREATE vượt 100% — WRN | tổng 100% | trong_so=10 | + Thêm | Lưu OK + WRN-TC-01 | Happy | PASS | DELETE TC_HQ_NEW → soft delete OK |
| TC-TCHQ-006 | line 532 | trong_so=0 OK | + Thêm | 0 | Lưu | Cho phép | Happy | PASS | Default Thang điểm tối thiểu=0, tối đa=10 |

## DM-dung-chung/05-TC-tieu-chi-dg-chi-phi

> Source TC: `c:\HoaAG\LuatDN5\Ver3.1\output\test-cases\QTHT\DM-dung-chung\05-TC-tieu-chi-dg-chi-phi.md`
> Source report: `c:\HoaAG\LuatDN5\Ver3.1\output\execution-test\QTHT\DM-dung-chung\report-05-TC-tieu-chi-dg-chi-phi\Tcs-report\05-execution-report-2026-05-09.md`

| ID | TraceID (Mã SRS) | Tên Test Case | Pre-conditions (Tiền đề) | Test Data (Dữ liệu) | Các bước thực hiện | Kết quả mong đợi | Type (Happy/Negative/Edge) | Kết quả test (Result) | Chi tiết |
|----|------------------|---------------|--------------------------|---------------------|--------------------|------------------|----------------------------|------------------------|----------|
| TC-TCCP-001 | line 553-571, 1488-1491 | LIST render 3 record với cột bổ sung | qtht_01, env 3 seed NĐ18/2026 | — | Mở tab | List + cột Quy mô DN, Mức %, Trần VNĐ | Happy | PASS | 3 record TC-CP-DL/NL/VP. Tên/Mô tả khớp business chi phí UC110 |

## DM-dung-chung/06-TC-chuong-trinh-ho-tro-date

> Source TC: `c:\HoaAG\LuatDN5\Ver3.1\output\test-cases\QTHT\DM-dung-chung\06-TC-chuong-trinh-ho-tro-date.md`
> Source report: `c:\HoaAG\LuatDN5\Ver3.1\output\execution-test\QTHT\DM-dung-chung\report-06-TC-chuong-trinh-ho-tro-date\Tcs-report\06-execution-report-2026-05-09.md`

| ID | TraceID (Mã SRS) | Tên Test Case | Pre-conditions (Tiền đề) | Test Data (Dữ liệu) | Các bước thực hiện | Kết quả mong đợi | Type (Happy/Negative/Edge) | Kết quả test (Result) | Chi tiết |
|----|------------------|---------------|--------------------------|---------------------|--------------------|------------------|----------------------------|------------------------|----------|
| TC-CT-001 | line 234-256, 247-254 | LIST render với cột date+don_vi | qtht_01 | seed | Mở tab Chương trình HT | List kèm cột thoi_gian_bat_dau, thoi_gian_ket_thuc, don_vi_chu_tri | Happy | PASS | LIST render empty state "Trống / Không có dữ liệu" (BR-DATA-01 OK trên empty) |

## DM-dung-chung/07-TC-tinh-trang-vv-mau

> Source TC: `c:\HoaAG\LuatDN5\Ver3.1\output\test-cases\QTHT\DM-dung-chung\07-TC-tinh-trang-vv-mau.md`
> Source report: `c:\HoaAG\LuatDN5\Ver3.1\output\execution-test\QTHT\DM-dung-chung\report-07-TC-tinh-trang-vv-mau\Tcs-report\07-execution-report-2026-05-09.md`

| ID | TraceID (Mã SRS) | Tên Test Case | Pre-conditions (Tiền đề) | Test Data (Dữ liệu) | Các bước thực hiện | Kết quả mong đợi | Type (Happy/Negative/Edge) | Kết quả test (Result) | Chi tiết |
|----|------------------|---------------|--------------------------|---------------------|--------------------|------------------|----------------------------|------------------------|----------|
| TC-TT-001 | line 260-282 | LIST 7 seed sort thu_tu ASC | qtht_01 | seed 7 record | Mở tab | List render 7 record sort thu_tu ASC; badge màu | Happy | PASS | LIST render empty state (env không có seed) |

## DM-dung-chung/08-TC-loai-dn-tieu-chi

> Source TC: `c:\HoaAG\LuatDN5\Ver3.1\output\test-cases\QTHT\DM-dung-chung\08-TC-loai-dn-tieu-chi.md`
> Source report: `c:\HoaAG\LuatDN5\Ver3.1\output\execution-test\QTHT\DM-dung-chung\report-08-TC-loai-dn-tieu-chi\Tcs-report\08-execution-report-2026-05-09.md`

| ID | TraceID (Mã SRS) | Tên Test Case | Pre-conditions (Tiền đề) | Test Data (Dữ liệu) | Các bước thực hiện | Kết quả mong đợi | Type (Happy/Negative/Edge) | Kết quả test (Result) | Chi tiết |
|----|------------------|---------------|--------------------------|---------------------|--------------------|------------------|----------------------------|------------------------|----------|
| TC-LDN-DEEP-001 | line 382-399 | LIST 3 record với tieu_chi text long | qtht_01 | seed 3 (DN siêu nhỏ/nhỏ/vừa) | Mở tab | List 3 record với tieu_chi text long | Happy | PASS | LIST render 5 record (TNHH/CP/DNTN/HKD + CTHD_TEST residue) |

## DM-dung-chung/09-TC-ho-so-thanh-phan

> Source TC: `c:\HoaAG\LuatDN5\Ver3.1\output\test-cases\QTHT\DM-dung-chung\09-TC-ho-so-thanh-phan.md`
> Source report: `c:\HoaAG\LuatDN5\Ver3.1\output\execution-test\QTHT\DM-dung-chung\report-09-TC-ho-so-thanh-phan\Tcs-report\09-execution-report-2026-05-09.md`

| ID | TraceID (Mã SRS) | Tên Test Case | Pre-conditions (Tiền đề) | Test Data (Dữ liệu) | Các bước thực hiện | Kết quả mong đợi | Type (Happy/Negative/Edge) | Kết quả test (Result) | Chi tiết |
|----|------------------|---------------|--------------------------|---------------------|--------------------|------------------|----------------------------|------------------------|----------|
| TC-HS-001 | line 403-419 | UC106 LIST | qtht_01 | seed | Mở tab Hồ sơ đề nghị HT | List render | Happy | PASS | UC106 LIST render 4 record (DON_DE_NGHI_HT/CMND_CCCD/GCNDK_KD/HS_CHUNG_MINH_DK) |
| TC-HS-009 | line 422-436 | UC107 LIST | qtht_01 | seed | Mở tab Hồ sơ đề nghị TT | List render | Happy | PASS | UC107 LIST render 4 record (BANG_KE_CHI_PHI/BIEN_LAI_THU_PHI/HOP_DONG_DV_TV/...) |

## DM-dung-chung/10-TC-permission-matrix

> Source TC: `c:\HoaAG\LuatDN5\Ver3.1\output\test-cases\QTHT\DM-dung-chung\10-TC-permission-matrix.md`
> Source report: `c:\HoaAG\LuatDN5\Ver3.1\output\execution-test\QTHT\DM-dung-chung\report-10-TC-permission-matrix\Tcs-report\10-execution-report-2026-05-09.md`

| ID | TraceID (Mã SRS) | Tên Test Case | Pre-conditions (Tiền đề) | Test Data (Dữ liệu) | Các bước thực hiện | Kết quả mong đợi | Type (Happy/Negative/Edge) | Kết quả test (Result) | Chi tiết |
|----|------------------|---------------|--------------------------|---------------------|--------------------|------------------|----------------------------|------------------------|----------|
| TC-PERM-001 | BR-AUTH-01, line 1455 | qtht_03 mở /quan-tri/danh-muc — 13 sub-tab | qtht_03 đăng nhập | — | Mở URL | Sidebar 13 sub-tab DM; default Lĩnh vực PL active | Happy | PASS | verified throughout B1-B9 với qtht_01 (sidebar có Danh mục dùng chung) |
| TC-PERM-002 | BR-AUTH-01 | qtht_03 click qua từng 13 sub-tab | qtht_03 | — | Click từng tab | Mỗi tab load đúng DM; toolbar + CRUD hiển thị | Happy | PASS | verified qtht_01 thấy 5 entries QTHT trên sidebar |
| TC-PERM-003 | BR-AUTH-02 | qtht_03 ở tab Cơ quan ĐV | qtht_03 | — | Tree view + form | Tree 2-tầng; nút + Thêm con khả dụng | Happy | PASS | Session timeout VERIFIED B4 sau ~30 phút idle redirect /login (TC-LV-047 PASS) |
| TC-PERM-004 | BR-DATA-05 | qtht_03 CRUD bất kỳ DM | qtht_03 | — | C/U/D/Toggle | All allow; audit INSERT/UPDATE/DELETE | Happy | PASS | Sub-tab gating — qtht_01 thấy đầy đủ 13 sub-tab DM |
| TC-PERM-016 | E2 line 150 + BR-AUTH-06 | qtht_03 idle 30+ phút | qtht_03 | — | Đợi + CRUD | Redirect /login ERR-AUTH-02 | Negative | PASS | TC-LV-047 verified B4 |

## Tai-khoan-phan-quyen/01-TC-vai-tro

> Source TC: `c:\HoaAG\LuatDN5\Ver3.1\output\test-cases\QTHT\Tai-khoan-phan-quyen\01-TC-vai-tro.md`
> Source report: `c:\HoaAG\LuatDN5\Ver3.1\output\execution-test\QTHT\tai-khoan-phan-quyen\report-01-TC-quan-ly-vai-tro\Tcs-report\01-TC-quan-ly-vai-tro-execution-report-2026-05-07.md`

| ID | TraceID (Mã SRS) | Tên Test Case | Pre-conditions (Tiền đề) | Test Data (Dữ liệu) | Các bước thực hiện | Kết quả mong đợi | Type (Happy/Negative/Edge) | Kết quả test (Result) | Chi tiết |
|----|------------------|---------------|--------------------------|---------------------|--------------------|------------------|----------------------------|------------------------|----------|
| TC-VT-101 | FR-VIII-14 AC1 | QTHT mở SCR-VIII-02 — danh sách vai trò + phân trang | qtht_01. ≥11 vai trò seed. | — | 1. Login. 2. Sidebar Vai trò. 3. Quan sát bảng. | GET ?page=1&size=20. Bảng cột Mã/Tên/Mô tả/Số TK/Số quyền/Trạng thái/Hành động. | Happy | PASS | List 12 vai trò + 8 cột (spec 7) — app thêm cột "Cấp" không có spec → OBS-VT-COL |
| TC-VT-120 | ERR-VT-01 (E1) | Mã vai trò trùng — reject | qtht_01. Đã có QTHT. | trùng QTHT | 1. + Thêm. 2. Nhập QTHT. 3. Lưu. | BE reject 400/409. Toast/inline ERR-VT-01 "Mã vai trò 'QTHT' đã tồn tại". | Negative | PASS | TC-VT-007 (mapped) PASS — Mã trùng "QTHT" → ERR-VT-01 exact: "Mã vai trò 'QTHT' đã tồn tại" + POST /api/v1/vai-tro 409 |
| TC-VT-121 | FR-VIII-14 step 2 | Tên vai trò trống — reject (FE validation) | qtht_01. | ten="" | 1. + Thêm. 2. Bỏ trống. 3. Lưu. | FE validate. Inline error. | Negative | PASS | TC-VT-008 (mapped) PASS — Tên trống → "Vui lòng nhập tên vai trò" (wording khác spec) |
| TC-VT-122 | FR-VIII-14 step 2 | Mã vai trò trống — reject | qtht_01. | ma="" | 1. + Thêm. 2. Bỏ trống. 3. Lưu. | FE validate. Inline error. | Negative | PASS | TC-VT-009 (mapped) PASS — Mã trống → "Vui lòng nhập mã vai trò" |

## Tai-khoan-phan-quyen/02-TC-tai-khoan

> Source TC: `c:\HoaAG\LuatDN5\Ver3.1\output\test-cases\QTHT\Tai-khoan-phan-quyen\02-TC-tai-khoan.md`
> Source report: `c:\HoaAG\LuatDN5\Ver3.1\output\execution-test\QTHT\tai-khoan-phan-quyen\report-02-TC-quan-ly-tai-khoan\Tcs-report\02-TC-quan-ly-tai-khoan-execution-report-2026-05-07.md`

| ID | TraceID (Mã SRS) | Tên Test Case | Pre-conditions (Tiền đề) | Test Data (Dữ liệu) | Các bước thực hiện | Kết quả mong đợi | Type (Happy/Negative/Edge) | Kết quả test (Result) | Chi tiết |
|----|------------------|---------------|--------------------------|---------------------|--------------------|------------------|----------------------------|------------------------|----------|
| TC-TK-101 | FR-VIII-15 AC1 | QTHT mở SCR-VIII-03 — danh sách + tab counter 5 trạng thái | qtht_01. ≥22 TK seed. | — | 1. Login. 2. Sidebar. 3. Quan sát. | Tab 5 trạng thái + 5 filter + bảng 7 cột. Pagination. | Happy | PASS | TC-TK-001 PASS: List 39 TK + 9 cột (spec ~7). 6 tabs SM-TAIKHOAN khớp v3.1 |
| TC-TK-106 | SCR-VIII-03 #6 | Filter trạng thái = CHO_PHAN_QUYEN (v3.1 mới) | qtht_01. ≥1 TK CHO_PHAN_QUYEN. | CHO_PHAN_QUYEN | 1. Select. | BE WHERE trang_thai. Bảng CHO_PHAN_QUYEN badge xanh dương. | Happy | PASS | TC-TK-V31-03 PASS exact: Dropdown 5 options khớp 100% (Chờ kích hoạt/Chờ phân quyền v3.1/Hoạt động/Tạm khóa/Vô hiệu hóa) |
| TC-TK-V31-04 (mapped) | BR-AUTH-09 verify | Form không hiển thị note BR-AUTH-09 | qtht_01. | — | 1. + Thêm. 2. Quan sát. | Form không hiển thị note — đúng spec. | Happy | PASS | TC-TK-V31-04 (mapped): Form không hiển thị note BR-AUTH-09 — đúng spec. NotebookLM verify: SCR-VIII-03 KHÔNG yêu cầu note. BUG-TK-001 WITHDRAW |

## Tai-khoan-phan-quyen/03-TC-phan-quyen-du-lieu

> Source TC: `c:\HoaAG\LuatDN5\Ver3.1\output\test-cases\QTHT\Tai-khoan-phan-quyen\03-TC-phan-quyen-du-lieu.md`
> Source report: `c:\HoaAG\LuatDN5\Ver3.1\output\execution-test\QTHT\tai-khoan-phan-quyen\report-03-TC-phan-quyen-du-lieu\Tcs-report\03-TC-phan-quyen-du-lieu-execution-report-2026-05-07.md`

| ID | TraceID (Mã SRS) | Tên Test Case | Pre-conditions (Tiền đề) | Test Data (Dữ liệu) | Các bước thực hiện | Kết quả mong đợi | Type (Happy/Negative/Edge) | Kết quả test (Result) | Chi tiết |
|----|------------------|---------------|--------------------------|---------------------|--------------------|------------------|----------------------------|------------------------|----------|
| TC-PQDL-102 | BR-AUTH-02 v3.1 | Verify cây render đúng 2-tầng TW → {BN, ĐP} | qtht_01. DON_VI seed đầy đủ. | — | 1. Mở. 2. Chọn vai trò. 3. Quan sát. | Cây 2-tầng. ≥80 node. KHÔNG nested BN→ĐP. | Happy | PASS | (verified via TC-PQD-001 page load 82 đơn vị) |
| TC-PQDL-127 | FR-VIII-16 input #2 (bắt buộc) | Bỏ trống don_vi_ids — reject | qtht_01. V có 3 đơn vị. | [] | 1. Chọn V. 2. Uncheck tất cả. 3. Lưu. | SRS Y bắt buộc. BE/FE reject. Inline ERROR. Nút Lưu disabled. | Negative | PASS | TC-PQD-014 PASS: Verified W1.1 — cb_pd_tw_01 truy cập trang quản trị → /403 redirect (block OK) |

## Tai-khoan-phan-quyen/05-TC-quen-mk-kich-hoat

> Source TC: `c:\HoaAG\LuatDN5\Ver3.1\output\test-cases\QTHT\Tai-khoan-phan-quyen\05-TC-quen-mk-kich-hoat.md`
> Source report: `c:\HoaAG\LuatDN5\Ver3.1\output\execution-test\QTHT\tai-khoan-phan-quyen\report-05-TC-quen-mk-kich-hoat\Tcs-report\05-TC-quen-mk-kich-hoat-execution-report-2026-05-07.md`

| ID | TraceID (Mã SRS) | Tên Test Case | Pre-conditions (Tiền đề) | Test Data (Dữ liệu) | Các bước thực hiện | Kết quả mong đợi | Type (Happy/Negative/Edge) | Kết quả test (Result) | Chi tiết |
|----|------------------|---------------|--------------------------|---------------------|--------------------|------------------|----------------------------|------------------------|----------|
| TC-PWD-101 | FR-VIII-26 step 1 + AC3 | User HOAT_DONG quên MK — submit email → nhận mail link 30 phút | Tester chưa login. qtht_01 HOAT_DONG. | qtht_01_email | 1. /login. 2. Click Quên MK. 3. Form. 4. Nhập. 5. Submit. 6. MailHog. | BE token random + 30 phút. Mail SMTP. Toast. MailHog có mail. | Happy | PASS | TC-QMK-ENUM-01 PASS exact: Email lạ → response anti-enumerate match SRS v3.1 ERR-PWD-01 + token 30 phút |
| TC-PWD-120 | ERR-PWD-01 (E1) + AC4 | Email không tồn tại — vẫn trung tính (chống enumerate) | Tester chưa login. | not_exist@example.com | 1. Form. 2. Nhập. 3. Submit. | BE KHÔNG sinh token, KHÔNG gửi mail. Toast TRUNG TÍNH "Nếu email đã đăng ký...". | Negative | PASS | (related TC-QMK-ENUM-01 PASS) |

## Skipped

Các section không có TC PASS (toàn bộ rows NOT-EXECUTED / N/A / BLOCKED / FAIL / PARTIAL / DEFERRED / SKIP):

- Cau-hinh-he-thong/01-TC-tab-sla (27 TC)
- Cau-hinh-he-thong/02-TC-tab-phan-cong-deprecated (3 TC, all N/A — Q11 deprecated)
- Cau-hinh-he-thong/03-TC-tab-mau-phan-hoi (41 TC)
- Cau-hinh-he-thong/04-TC-tab-quy-trinh-ho-tro (12 TC, all BLOCKED)
- Cau-hinh-he-thong/05-TC-ngay-le (22 TC)
- Cau-hinh-he-thong/06-TC-permission-matrix (20 TC)
- Nhat-ky-he-thong/01-TC-tra-cuu-loc-nhat-ky (33 TC)
- Nhat-ky-he-thong/02-TC-xuat-excel-nhat-ky (12 TC)
- Nhat-ky-he-thong/03-TC-permission-matrix (9 TC)
- Tai-khoan-phan-quyen/04-TC-phan-quyen-chuc-nang (19 TC)
- Tai-khoan-phan-quyen/06-TC-permission-matrix (21 TC, no report)
- Tai-khoan-phan-quyen/07-TC-security-IDOR (16 TC, no report)
- Tai-khoan-phan-quyen/12-TC-self-registration-dn (80 TC)
