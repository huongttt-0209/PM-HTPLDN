# Test Cases PASS — ct-htpldn-gd1

> **Nguồn**: result-ct-htpldn-gd1-all.md
> **Ngày tổng hợp**: 2026-05-11
> **Phạm vi**: chỉ Result ∈ {PASS, PASS-DEVIATE, PASS-RESOLVED}

## Summary

| File test-case | Total TC PASS |
|----------------|---------------|
| 01-TC-quan-ly-ct-CRUD | 12 |
| 02-TC-tim-kiem-ct | 7 |
| 03-TC-lifecycle-ct | 6 |
| 04-TC-trinh-phe-duyet-ct | 2 |
| 05-TC-phe-duyet-ct | 2 |
| 06-TC-cong-bo-ct | 2 |
| **Tổng** | **31** |

## 01-TC-quan-ly-ct-CRUD

> Source TC: `c:\HoaAG\LuatDN5\Ver3.1\output\test-cases\ct-htpldn-gd1\01-TC-quan-ly-ct-CRUD.md`
> Source report: `c:\HoaAG\LuatDN5\Ver3.1\output\execution-test\ct-htpldn-gd1\report-01-TC-quan-ly-ct-CRUD\Tcs-report.md`

| ID | TraceID (Mã SRS) | Tên Test Case | Pre-conditions (Tiền đề) | Test Data (Dữ liệu) | Các bước thực hiện | Kết quả mong đợi | Type (Happy/Negative/Edge) | Kết quả test (Result) | Chi tiết |
|----|------------------|---------------|--------------------------|---------------------|--------------------|------------------|----------------------------|------------------------|----------|
| TC-CT-CRUD-001 | FR-XI-01 / Processing Tạo step 1-7 | Tạo CT thành công — happy path | cb_nv_tw_01 login. | ten_chuong_trinh="CT HTPLDN 2026 Q1", muc_tieu="Tăng cường nhận thức PL DN", thoi_gian_bat_dau="2026-06-01", doi_tuong="DN nhỏ và vừa" | 1. Click [+ Thêm CT]. 2. Nhập đủ trường bắt buộc. 3. Lưu. | (1) POST `/api/v1/chuong-trinh-htpl` 200. (3) CT xuất hiện trong DS với ma_chuong_trinh auto `CT-{YYYYMMDD}-001`, trạng thái=DU_THAO, don_vi_id=user, ngày_tao=NOW(), nguoi_tao=cb_nv_tw_01. Audit log INSERT (BR-DATA-05). | Happy 🔴 | PASS |  |
| TC-CT-CRUD-002 | FR-XI-01 / Processing Cập nhật | Sửa CT khi DU_THAO | cb_nv_tw_01 login. CT-DT01 trạng thái DU_THAO. | ten="CT HTPLDN 2026 Q1 (Sửa)", ngan_sach=500000000 | 1. Click Sửa trên CT-DT01. 2. Đổi tên + thêm ngân sách. 3. Lưu. | (1) PUT 200. (3) Hiển thị tên mới + ngân sách. Audit log UPDATE. | Happy 🔴 | PASS |  |
| TC-CT-CRUD-003 | FR-XI-01 / Processing Xóa step 1-5 | Xóa mềm CT khi DU_THAO | cb_nv_tw_01 login. CT-DT02 trạng thái DU_THAO. | — | 1. Click Xóa trên CT-DT02. 2. Xác nhận. | (1) DELETE 200, soft delete (`is_deleted=1`, BR-DATA-01). (3) CT-DT02 biến mất khỏi DS. Audit log DELETE. | Happy 🔴 | PASS |  |
| TC-CT-CRUD-004 | FR-XI-01 / AC#1 + BR-DATA-07 | Hiển thị DS CT phân trang | cb_nv_tw_01 login. ≥25 CT thuộc đơn vị. | — | 1. Truy cập SCR-XI-01. | (3) DS phân trang 20/page. Cột: Mã CT / Tên / Mục tiêu (cắt 100 ký tự) / Thời gian / Ngân sách / Đơn vị / Trạng thái (badge) / Số đợt BC / Hành động. | Happy 🟡 | PASS |  |
| TC-CT-CRUD-005 | FR-XI-01 / AC#2 | Xem chi tiết CT (Tab Thông tin) | cb_nv_tw_01 login. CT-DT01 tồn tại. | — | 1. Click row CT-DT01. | (3) Mở Tab "Thông tin": form đầy đủ field + Thanh tiến trình SM-KH-CTHTPL highlight DU_THAO. | Happy 🟢 | PASS |  |
| TC-CT-CRUD-010 | FR-XI-01 / E1 ERR-XI-01-01 | Thiếu trường bắt buộc | cb_nv_tw_01 login. | ten="" | 1. Mở form Thêm CT. 2. Bỏ trống tên + Lưu. | (2) Error: **"Vui lòng nhập đầy đủ thông tin bắt buộc"** (ERR-XI-01-01). Form giữ. | Negative 🔴 | PASS |  |
| TC-CT-CRUD-011 | FR-XI-01 / E2 ERR-XI-01-02 + BR-FLOW-03 | Sửa CT khi ≠ DU_THAO | cb_nv_tw_01 login. CT-PD01 trạng thái CHO_PHE_DUYET. | — | 1. Click Sửa trên CT-PD01. | (1) Nút Sửa ẩn HOẶC backend reject với **"Chỉ chỉnh sửa CT ở trạng thái Dự thảo"** (ERR-XI-01-02). | Negative 🔴 | PASS |  |
| TC-CT-CRUD-012 | FR-XI-01 / E3 ERR-XI-01-03 + BR-FLOW-03 | Xóa CT khi ≠ DU_THAO | cb_nv_tw_01 login. CT-DD01 trạng thái DA_DUYET. | — | 1. Click Xóa trên CT-DD01. | (1) Nút Xóa ẩn HOẶC backend reject **"Chỉ xóa CT ở trạng thái Dự thảo"** (ERR-XI-01-03). | Negative 🔴 | PASS |  |
| TC-CT-CRUD-013 | FR-XI-01 / Inputs#5 | thoi_gian_ket_thuc <= thoi_gian_bat_dau | cb_nv_tw_01 login. | thoi_gian_bat_dau="2026-06-01", thoi_gian_ket_thuc="2026-05-31" | 1. Tạo CT với end < start + Lưu. | (2) Error inline trên field "Thời gian kết thúc phải sau Thời gian bắt đầu". KHÔNG persist. | Negative 🟡 | PASS |  |
| TC-CT-CRUD-014 | FR-XI-01 / Inputs#6 | ngan_sach < 0 | cb_nv_tw_01 login. | ngan_sach=-1000000 | 1. Nhập ngân sách âm + Lưu. | (2) Validation reject. KHÔNG persist. | Negative 🟢 | PASS |  |
| TC-CT-CRUD-015 | FR-XI-01 / Inputs#5 (A4 merged) | thoi_gian_bat_dau = thoi_gian_ket_thuc (boundary equal — strict `>`) | cb_nv_tw_01 login. | thoi_gian_bat_dau="2026-06-01", thoi_gian_ket_thuc="2026-06-01" | 1. Tạo CT với 2 ngày bằng nhau + Lưu. | (2) Backend reject vì spec quote "> thoi_gian_bat_dau". Toast/inline error. KHÔNG persist. | Negative 🟡 | PASS |  |
| TC-CT-CRUD-016 | FR-XI-01 / Inputs#6 (A4 merged) | ngan_sach = 0 (boundary inclusive `>=0`) | cb_nv_tw_01 login. | ngan_sach=0 | 1. Tạo CT với ngân sách=0 + Lưu. | (1) PASS — boundary `>=0` inclusive. CT lưu với ngân sách=0. UI hiển thị "0" hoặc "—" tùy spec format. | Edge 🟡 | PASS |  |

## 02-TC-tim-kiem-ct

> Source TC: `c:\HoaAG\LuatDN5\Ver3.1\output\test-cases\ct-htpldn-gd1\02-TC-tim-kiem-ct.md`
> Source report: `c:\HoaAG\LuatDN5\Ver3.1\output\execution-test\ct-htpldn-gd1\report-02-TC-tim-kiem-ct\Tcs-report.md`

| ID | TraceID (Mã SRS) | Tên Test Case | Pre-conditions (Tiền đề) | Test Data (Dữ liệu) | Các bước thực hiện | Kết quả mong đợi | Type (Happy/Negative/Edge) | Kết quả test (Result) | Chi tiết |
|----|------------------|---------------|--------------------------|---------------------|--------------------|------------------|----------------------------|------------------------|----------|
| TC-CT-TK-001 | FR-XI-02 / AC#1 | Tìm theo keyword (mã CT) | cb_nv_tw_01 login. CT-DT01 + CT-DD05 tồn tại. | keyword="CT-2026" | 1. Nhập keyword vào ô tìm. 2. Enter / Tìm kiếm. | (3) DS hiển thị các CT khớp `ma_chuong_trinh` chứa "CT-2026". Network GET `/api/v1/chuong-trinh-htpl?keyword=CT-2026` 200. | Happy 🔴 | PASS |  |
| TC-CT-TK-002 | FR-XI-02 / AC#1 + BR-DATA-07 | Lọc theo trạng thái + phân trang | cb_nv_tw_01 login. ≥25 CT trạng thái DA_DUYET. | trang_thai=DA_DUYET | 1. Chọn filter trạng thái DA_DUYET. 2. Tìm. | (3) DS chỉ chứa CT DA_DUYET, phân trang 20/page. | Happy 🔴 | PASS |  |
| TC-CT-TK-003 | FR-XI-02 / Processing step 2 | Lọc khoảng ngày AND keyword | cb_nv_tw_01 login. | tu_ngay="2026-01-01", den_ngay="2026-12-31", keyword="HTPLDN" | 1. Set 2 filter ngày + keyword. 2. Tìm. | (3) DS thỏa cả 3 điều kiện AND. Empty kết quả ngoài range KHÔNG hiển thị. | Happy 🟡 | PASS |  |
| TC-CT-TK-005 | FR-XI-02 / E1 INF-CT-TK-01 | Không tìm thấy | cb_nv_tw_01 login. | keyword="ZZZZ_KHONG_TON_TAI" | 1. Tìm với keyword không match. | (3) Toast/inline INFO "Không tìm thấy chương trình phù hợp" (INF-CT-TK-01). DS empty state. | Happy 🟢 | PASS |  |
| TC-CT-TK-009 | FR-XI-02 / BR-EC-12 | Pagination guard `page_size > 100` | cb_nv_tw_01 login. | URL `?page_size=200` | 1. Sửa URL set page_size=200. | (1) Backend reject với ERR-PARAM-01 HOẶC clamp về 100. Network response chứa lỗi rõ. | Edge 🟢 | PASS |  |
| TC-CT-TK-010 | FR-XI-02 / BR-EC-13 | Search sanitize SQL injection | cb_nv_tw_01 login. | keyword=`'; DROP TABLE CHUONG_TRINH_HTPL; --` | 1. Nhập keyword chứa SQL. 2. Tìm. | (3) Backend escape/sanitize, trả empty hoặc match literal. KHÔNG drop bảng. Network 200 với DS bình thường. | Edge 🔴 | PASS |  |
| TC-CT-TK-011 | FR-XI-02 / BR-EC-13 | Search sanitize XSS | cb_nv_tw_01 login. | keyword=`<script>alert(1)</script>` | 1. Nhập + Tìm. | (3) Keyword được escape khi render lại trong filter chip; KHÔNG trigger alert. | Edge 🔴 | PASS |  |

## 03-TC-lifecycle-ct

> Source TC: `c:\HoaAG\LuatDN5\Ver3.1\output\test-cases\ct-htpldn-gd1\03-TC-lifecycle-ct.md`
> Source report: `c:\HoaAG\LuatDN5\Ver3.1\output\execution-test\ct-htpldn-gd1\report-03-TC-lifecycle-ct\Tcs-report.md`

| ID | TraceID (Mã SRS) | Tên Test Case | Pre-conditions (Tiền đề) | Test Data (Dữ liệu) | Các bước thực hiện | Kết quả mong đợi | Type (Happy/Negative/Edge) | Kết quả test (Result) | Chi tiết |
|----|------------------|---------------|--------------------------|---------------------|--------------------|------------------|----------------------------|------------------------|----------|
| TC-LC-003 | FR-XI-01 / Kích hoạt E2 ERR-XI-01-KH-02 | Kích hoạt khi state ≠ DA_DUYET/DA_CONG_BO | cb_nv_tw_01 login. CT-DT01 trạng thái DU_THAO. | — | 1. Mở chi tiết. | (1) Nút [Kích hoạt] ẩn. Nếu force qua API → reject "CT phải ở Đã duyệt hoặc Đã công bố để kích hoạt" (ERR-XI-01-KH-02). | Negative 🟡 | PASS |  |
| TC-LC-005 | FR-XI-01 / Tạm dừng E3 ERR-XI-01-TD-03 (Codex fix 2026-05-09) | Thiếu lý do tạm dừng | cb_pd_tw_01 login. CT-TH02 DANG_THUC_HIEN. | ly_do="" | 1. [Tạm dừng] → bỏ trống lý do → Submit. | (2) Error inline "Vui lòng nhập lý do tạm dừng" (ERR-XI-01-TD-03, srs-fr-15:226). KHÔNG persist. **Note Codex 2026-05-09:** Bỏ trace `BR-FLOW-04` — BR-FLOW-04 (srs-fr-15:1467-1471) chỉ áp dụng cho hành động **Từ chối** (FR-XI-04, FR-XI-07a), KHÔNG áp dụng Tạm dừng. ERR-XI-01-TD-03 là rule riêng của FR-XI-01 Tạm dừng. | Negative 🔴 | PASS |  |
| TC-LC-008 | FR-XI-01 / Tiếp tục E2 ERR-XI-01-TT-02 | Tiếp tục khi không TAM_DUNG | cb_pd_tw_01 login. CT-TH04 DANG_THUC_HIEN. | — | — | (1) Nút [Tiếp tục] ẩn. Force API → reject (ERR-XI-01-TT-02). | Negative 🟢 | PASS |  |
| TC-LC-013 | FR-XI-01 / Hủy E2 ERR-XI-01-HC-02 | Hủy CT khi ≠ DU_THAO | cb_nv_tw_01 login. CT-DD05 DA_DUYET. | — | 1. Mở chi tiết. | (1) Nút [Hủy CT] ẩn. Force → reject "Chỉ hủy CT ở trạng thái Dự thảo" (ERR-XI-01-HC-02). | Negative 🟢 | PASS |  |
| TC-LC-015 | FR-XI-01 / Rút trình E1 ERR-XI-01-RT-01 | Không phải người trình → reject | cb_nv_tw_02 login (KHÔNG phải người trình). CT-PD03 CHO_PHE_DUYET trình bởi tw_01. | — | 1. Mở chi tiết. | (1) Nút [Rút trình] ẩn với user ≠ người trình. Force → reject "Chỉ người trình mới được rút trình" (ERR-XI-01-RT-01). | Negative 🟡 | PASS |  |
| TC-LC-015b | FR-XI-01 / Rút trình E2 ERR-XI-01-RT-02 (Codex 2026-05-09) | Rút trình khi state ≠ CHO_PHE_DUYET | cb_nv_tw_01 (người trình) login. CT-DD23 DA_DUYET (đã được duyệt rồi, không thể rút). | — | 1. Mở chi tiết. 2. Force API PATCH `/withdraw`. | (1) Nút [Rút trình] ẨN khi CT đã DA_DUYET (lifecycle move forward). Force API → reject "CT phải ở trạng thái Chờ phê duyệt để rút trình" (ERR-XI-01-RT-02, srs-fr-15:322). KHÔNG transition. | Negative 🟡 | PASS |  |

## 04-TC-trinh-phe-duyet-ct

> Source TC: `c:\HoaAG\LuatDN5\Ver3.1\output\test-cases\ct-htpldn-gd1\04-TC-trinh-phe-duyet-ct.md`
> Source report: `c:\HoaAG\LuatDN5\Ver3.1\output\execution-test\ct-htpldn-gd1\report-04-TC-trinh-phe-duyet-ct\Tcs-report.md`

| ID | TraceID (Mã SRS) | Tên Test Case | Pre-conditions (Tiền đề) | Test Data (Dữ liệu) | Các bước thực hiện | Kết quả mong đợi | Type (Happy/Negative/Edge) | Kết quả test (Result) | Chi tiết |
|----|------------------|---------------|--------------------------|---------------------|--------------------|------------------|----------------------------|------------------------|----------|
| TC-TR-CT-001 | FR-XI-03 / Processing step 1-6 + AC | Trình PD CT đầy đủ thông tin | cb_nv_tw_01 login. CT-DT04 DU_THAO, đầy đủ ten/muc_tieu/thoi_gian_bat_dau/doi_tuong. | — | 1. Mở chi tiết CT-DT04. 2. Click [Gửi phê duyệt]. | (1) PATCH `/api/v1/.../submit` 200. (3) Trạng thái → CHO_PHE_DUYET. Notification gửi CB PD cùng cấp (cb_pd_tw_01). Audit log. | Happy 🔴 | PASS |  |
| TC-TR-CT-003 | FR-XI-03 / E1 ERR-XI-03-01 | Trình PD khi state ≠ DU_THAO | cb_nv_tw_01 login. CT-PD04 CHO_PHE_DUYET. | — | 1. Mở chi tiết. | (1) Nút [Gửi phê duyệt] ẩn. Force API → reject "CT không ở trạng thái cho phép trình duyệt" (ERR-XI-03-01). | Negative 🔴 | PASS |  |

## 05-TC-phe-duyet-ct

> Source TC: `c:\HoaAG\LuatDN5\Ver3.1\output\test-cases\ct-htpldn-gd1\05-TC-phe-duyet-ct.md`
> Source report: `c:\HoaAG\LuatDN5\Ver3.1\output\execution-test\ct-htpldn-gd1\report-05-TC-phe-duyet-ct\Tcs-report.md`

| ID | TraceID (Mã SRS) | Tên Test Case | Pre-conditions (Tiền đề) | Test Data (Dữ liệu) | Các bước thực hiện | Kết quả mong đợi | Type (Happy/Negative/Edge) | Kết quả test (Result) | Chi tiết |
|----|------------------|---------------|--------------------------|---------------------|--------------------|------------------|----------------------------|------------------------|----------|
| TC-PD-CT-003 | FR-XI-04 / E2 ERR-XI-04-02 + BR-FLOW-04 | Từ chối thiếu lý do → reject | cb_pd_tw_01 login. CT-PD07 CHO_PHE_DUYET. | quyet_dinh=TU_CHOI, ly_do_tu_choi="" | 1. [Từ chối] → bỏ trống lý do → Submit. | (2) Error inline "Vui lòng nhập lý do từ chối" (ERR-XI-04-02). KHÔNG transition. | Negative 🔴 | PASS |  |
| TC-PD-CT-007 | FR-XI-04 / E1 ERR-XI-04-01 | Phê duyệt khi state ≠ CHO_PHE_DUYET | cb_pd_tw_01 login. CT-DD06 DA_DUYET. | quyet_dinh=DUYET | 1. Mở chi tiết. | (1) Nút [Phê duyệt] ẩn. Force API → reject "CT không ở trạng thái chờ phê duyệt" (ERR-XI-04-01). | Negative 🟡 | PASS |  |

## 06-TC-cong-bo-ct

> Source TC: `c:\HoaAG\LuatDN5\Ver3.1\output\test-cases\ct-htpldn-gd1\06-TC-cong-bo-ct.md`
> Source report: `c:\HoaAG\LuatDN5\Ver3.1\output\execution-test\ct-htpldn-gd1\report-06-TC-cong-bo-ct\Tcs-report.md`

| ID | TraceID (Mã SRS) | Tên Test Case | Pre-conditions (Tiền đề) | Test Data (Dữ liệu) | Các bước thực hiện | Kết quả mong đợi | Type (Happy/Negative/Edge) | Kết quả test (Result) | Chi tiết |
|----|------------------|---------------|--------------------------|---------------------|--------------------|------------------|----------------------------|------------------------|----------|
| TC-CB-CT-004 | FR-XI-05 / E1 ERR-XI-05-01 | Công bố khi state ≠ DA_DUYET | cb_nv_tw_01 login. CT-DT08 DU_THAO. | — | 1. Mở chi tiết. | (1) Nút [Công bố] ẩn. Force API → reject "CT chưa được phê duyệt" (ERR-XI-05-01). | Negative 🔴 | PASS |  |
| TC-CB-CT-007 | FR-XI-05 / Công bố lặp | Công bố lại CT đã DA_CONG_BO | cb_nv_tw_01 login. CT-CB03 DA_CONG_BO. | — | 1. Mở chi tiết. | (1) Nút [Công bố] ẩn (chỉ hiện [Hủy công bố]). Force API → reject ERR-XI-05-01. | Edge 🟢 | PASS |  |

## Skipped

Các section sau không có TC PASS (toàn bộ DEFERRED hoặc trạng thái khác):

- **07-TC-quan-ly-dot-bc** — 12 TC, 0 PASS (toàn bộ DEFERRED do token revoked / depend on B7-001 seed / cross-phase GĐ2 / SPEC-CLARIFY).
- **08-TC-permission-matrix** — 9 TC, 0 PASS (toàn bộ DEFERRED do cần đa role single-purpose users: cb_nv_dp_01 / cb_pd_tw_02 / cb_nv_bn_01 / nht_01 / tvv_01 / qtht_01 / logout).
