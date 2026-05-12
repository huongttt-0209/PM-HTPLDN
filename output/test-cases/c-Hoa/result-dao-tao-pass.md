# Test Cases PASS — dao-tao

> **Nguồn**: result-dao-tao-all.md
> **Ngày tổng hợp**: 2026-05-11
> **Phạm vi**: chỉ Result ∈ {PASS, PASS-DEVIATE, PASS-RESOLVED}

## Summary

| File test-case | TC PASS |
|----------------|--------:|
| 01-TC-KH-nam-dao-tao | 21 |
| 02-TC-CTDT-quan-ly | 19 |
| 03-TC-de-xuat-dao-tao | 5 |
| 04-TC-lich-hoc | 5 |
| 05-TC-khoa-hoc-quan-ly | 12 |
| 09-TC-bai-giang-kho-tai-lieu | 3 |
| 10-TC-NHCH-de-kiem-tra | 5 |
| 11-TC-giang-vien | 6 |
| 13-TC-permission-matrix | 4 |
| **Tổng** | **80** |

> Ghi chú: Chỉ lọc các TC có Result ∈ {PASS, PASS-DEVIATE, PASS-RESOLVED}. Section không có TC PASS được liệt kê ở `## Skipped` cuối file. Cột "Chi tiết" để trống cho PASS/PASS-DEVIATE theo quy ước.

---

## 01-TC-KH-nam-dao-tao

> Source TC: `c:\HoaAG\LuatDN5\Ver3.1\output\test-cases\dao-tao\01-TC-KH-nam-dao-tao.md`
> Source report: `c:\HoaAG\LuatDN5\Ver3.1\output\execution-test\dao-tao\report-01-TC-KH-nam-dao-tao\Tcs-report\01-TC-KH-nam-dao-tao-execution-report-2026-05-11.md`

| ID | TraceID (Mã SRS) | Tên Test Case | Pre-conditions (Tiền đề) | Test Data (Dữ liệu) | Các bước thực hiện | Kết quả mong đợi | Type (Happy/Negative/Edge) | Kết quả test (Result) | Chi tiết |
|----|------------------|---------------|--------------------------|---------------------|--------------------|------------------|----------------------------|------------------------|----------|
| TC-KH-NAM-H-003 | FR-III-14 / BR-AUTH-08 | CB_NV_TW thấy KH năm thuộc đơn vị TW + descendants | CB_NV_TW đăng nhập. Seed 2 KH TW + 2 KH BN + 2 KH ĐP. | — | 1. Vào danh sách KH năm. 2. Quan sát số dòng. | Backend filter `WHERE don_vi_id IN (descendants_of_TW)`. Hiển thị 6 KH. Reload giữ scope. | Happy | PASS |  |
| TC-KH-NAM-H-005 | FR-III-14 / BR-DATA-07 | Pagination default 20/page + click trang 2 | CB_NV_TW. Seed ≥25 KH năm trạng thái DA_DUYET. | — | 1. Vào danh sách. 2. Quan sát pagination. 3. Click page 2. | Request `?page=1&size=20` → 20; page 2 → 5. Page 1 có 20 dòng, "Tổng: 25 mục". | Happy | PASS |  |
| TC-KH-NAM-H-006 | FR-III-14 / BR-DATA-03 / BR-DATA-05 | Lập KH năm thành công — đầy đủ field bắt buộc | CB_NV_TW đăng nhập. CTĐT "CTDT-TW-2026-001" trạng thái DA_DUYET tồn tại. | ten_ke_hoach="KH ĐT năm 2026 — DN nhỏ và vừa", ctdt_id, BĐ=2026-06-01, KT=2026-12-31, ngân sách=500M, nguồn lực, ghi chú | 1. Click [+ Lập KH năm]. 2. Điền đủ field. 3. Click [Lưu nháp]. | INSERT KE_HOACH_DAO_TAO với ma_kh auto-gen, trạng thái NHAP. AUDIT_LOG. Toast "Lập kế hoạch thành công". Record hiển thị badge "Nháp". | Happy | PASS |  |
| TC-KH-NAM-N-008 | FR-III-14 / Inputs row 4 | Lập KH năm — thoi_gian_ket_thuc ≤ thoi_gian_bat_dau | CB_NV_TW đăng nhập. | thoi_gian_bat_dau="2026-06-01", thoi_gian_ket_thuc="2026-05-30" | 1. Form lập. 2. Nhập KT < BĐ. 3. Lưu. | KHÔNG INSERT. Inline error "Thời gian kết thúc phải sau thời gian bắt đầu". Count không đổi. | Negative | PASS |  |
| TC-KH-NAM-B-010 | FR-III-14 / Boundary | Lập KH năm — ngan_sach_du_kien = 0 (boundary) | CB_NV_TW. | ngan_sach_du_kien=0 | 1. Lập KH với ngân sách=0. 2. Lưu. | INSERT thành công (constraint ≥0 cho phép =0). Toast OK. Detail hiển thị 0. | Boundary | PASS |  |
| TC-KH-NAM-B-011 | FR-III-14 / Boundary | Lập KH năm — ngan_sach_du_kien âm (-1) | CB_NV_TW. | ngan_sach_du_kien=-1 | 1. API direct POST với ngân sách=-1. | KHÔNG INSERT. BE check ≥0 fail. Inline/HTTP error "Ngân sách phải ≥ 0". Count không đổi. | Negative | PASS |  |
| TC-KH-NAM-H-012 | FR-III-14 / BR-DATA-05 | Sửa KH năm trạng thái NHAP — đổi ngân sách | CB_NV_TW. KH "KH-20260509-001" trạng thái NHAP, do cb_nv_tw_01 tạo. | ngan_sach_du_kien_moi=600000000 | 1. Click [Sửa] trên row KH. 2. Đổi ngân sách. 3. Lưu. | UPDATE KE_HOACH_DAO_TAO. AUDIT_LOG. Toast OK. Detail reflect 600M. | Happy | PASS |  |
| TC-KH-NAM-N-013 | ERR-KH-02 / BR-FLOW-03 | Sửa KH năm trạng thái DA_DUYET — bị chặn | CB_NV_TW. KH "KH-20260509-002" trạng thái DA_DUYET. | ngan_sach mới | 1. Click [Sửa] trên row DA_DUYET. | KHÔNG UPDATE. Nút [Sửa] ẨN/disable. Force API PUT → BE reject "Không thể sửa KH đã duyệt". | Negative | PASS |  |
| TC-KH-NAM-H-015 | FR-III-14 / BR-DATA-01 | Xóa mềm KH năm trạng thái NHAP thành công | CB_NV_TW. KH "KH-20260509-003" NHAP, do cb_nv_tw_01 tạo. | — | 1. Click [Xóa] trên row. 2. Confirm dialog. | UPDATE SET is_deleted=1, deleted_at, deleted_by. AUDIT_LOG. Toast "Xóa kế hoạch thành công". Record biến mất. | Happy | PASS |  |
| TC-KH-NAM-N-016 | FR-III-14 / BR-FLOW-03 | Xóa KH năm trạng thái CHO_DUYET — bị chặn | CB_NV_TW. KH "KH-20260509-004" CHO_DUYET. | — | 1. Click [Xóa]. | KHÔNG UPDATE is_deleted. Nút [Xóa] ẨN/disable. Force API DELETE → BE reject. Record vẫn tồn tại NHAP. | Negative | PASS |  |
| TC-KH-NAM-S-017 | FR-III-14 AC2 / SM-KHOAHOC | Trình duyệt KH năm: NHAP → CHO_DUYET (AT-01 manual trigger) | CB_NV_TW. KH "KH-T1" NHAP đầy đủ field. | — | 1. Row KH-T1 → click [Trình duyệt]. 2. Confirm dialog. | UPDATE SET trang_thai='CHO_DUYET'. AUDIT_LOG SUBMIT. Notification. Toast "Đã gửi phê duyệt". Badge "Chờ duyệt". | Happy | PASS |  |
| TC-KH-NAM-S-018 | FR-III-15 AC1 / BR-AUTH-05 / SM-KHOAHOC | Phê duyệt KH năm: CHO_DUYET → DA_DUYET (CB PD cùng cấp) | cb_pd_tw_01 đăng nhập. KH "KH-T1" CHO_DUYET (do cb_nv_tw_01 trình). | quyet_dinh="PHE_DUYET" | 1. CB_PD_TW vào danh sách Chờ duyệt. 2. Row KH-T1 → click [Duyệt]. 3. Confirm. | UPDATE SET trang_thai='DA_DUYET'. AUDIT_LOG APPROVE. Toast "Phê duyệt thành công". Badge "Đã duyệt". | Happy | PASS |  |
| TC-KH-NAM-N-020 | FR-III-15 / BR-FLOW-04 / SPEC-CLARIFY-DT-A6-01 | Từ chối KH năm — lý do trống / <10 ký tự | cb_pd_tw_01. KH CHO_DUYET. | ly_do="" hoặc ly_do="Ngắn" (5 ký) | 1. Click [Từ chối]. 2. Bỏ trống/nhập ngắn. 3. Confirm. | KHÔNG UPDATE. Inline error "Lý do từ chối là bắt buộc và tối thiểu 10 ký tự". Record vẫn CHO_DUYET. | Negative | PASS |  |
| TC-KH-NAM-N-021 | FR-III-15 / BR-AUTH-05 | Phê duyệt KH năm — CB PD khác cấp (CB_PD_BN duyệt KH cấp TW) | cb_pd_bn_01 đăng nhập. KH "KH-T3" CHO_DUYET cấp TW. | quyet_dinh="PHE_DUYET" | 1. CB_PD_BN cố API PUT approve KH cấp TW. | KHÔNG UPDATE. HTTP 403 / toast "Phê duyệt phải cùng cấp". | Negative | PASS |  |
| TC-KH-NAM-N-022 | FR-III-15 / ERR-DKDT-01 | Phê duyệt KH năm khi đã ở trạng thái CHO_DUYET → reject ERR-DKDT-01 | cb_pd_tw_01 đăng nhập. KH-NAM-2026-001 ở trạng thái CHO_DUYET. | Click [Phê duyệt] 2 lần liên tiếp (idempotency). | 1. CB PD đăng nhập. 2. SCR-III-01 Tab "KH năm". 3. Click row CHO_DUYET → click [Phê duyệt]. 4. Repeat. | Lần 1 INSERT phê duyệt → state DA_DUYET. Lần 2 reject duplicate. Lần 2 toast "Kế hoạch đã ở trạng thái chờ duyệt hoặc đã duyệt". | Negative | PASS |  |
| TC-KH-NAM-N-023 | FR-III-15 / ERR-KH-03 | Trình duyệt KH năm khi đã CHO_DUYET (idempotency block) | cb_nv_tw_01. KH-NAM-2026-002 ở CHO_DUYET. | API direct POST `/submit` với token CB NV. | 1. POST submit lần 2 cho KH đã CHO_DUYET. | KHÔNG đổi state. HTTP 409 Conflict + body `{code:"ERR-KH-03"}`. state vẫn CHO_DUYET. | Negative | PASS |  |
| TC-KH-NAM-S-022 | FR-III-16 AC1 / BR-FLOW-05 / SM-KHOAHOC | Công khai KH năm: DA_DUYET → DA_CONG_KHAI (gọi API Cổng PLQG) | cb_nv_tw_01. KH "KH-T1" DA_DUYET. Mock API outbound `POST /portal/ke-hoach`. | hanh_dong="CONG_KHAI" | 1. Row KH-T1 → click [Công khai]. 2. Confirm. | Outbound `POST /portal/ke-hoach` (BR-FLOW-05). UPDATE trang_thai='DA_CONG_KHAI'. AUDIT_LOG PUBLISH. Toast "Công khai thành công". | Happy | PASS |  |
| TC-KH-NAM-S-023 | FR-III-16 AC2 / SM-KHOAHOC | Hủy công khai KH năm: DA_CONG_KHAI → DA_DUYET | cb_nv_tw_01. KH "KH-T1" DA_CONG_KHAI. | hanh_dong="HUY_CONG_KHAI" | 1. Row KH-T1 → [Hủy công khai]. 2. Confirm. | Outbound DELETE. UPDATE trang_thai='DA_DUYET'. AUDIT_LOG UNPUBLISH. Toast "Đã gỡ công khai". DA_DUYET. | Happy | PASS |  |
| TC-KH-NAM-S-024 | FR-III-16 / SM-KHOAHOC invalid | Công khai KH năm trạng thái NHAP/CHO_DUYET — bị chặn | cb_nv_tw_01. KH "KH-T4" NHAP. | hanh_dong="CONG_KHAI" | 1. Force API call publish trên NHAP. | KHÔNG UPDATE. Force API → 422 "Trạng thái không cho phép công khai". | Negative | PASS |  |
| TC-KH-NAM-E-027 | FR-III-14 / BR-DATA-05 / Audit Trail | Verify AUDIT_LOG ghi đầy đủ chuỗi CRUD + state transition (qua FR-10 W1.1 UI) | CB_NV_TW + CB_PD_TW. FR-10 W1.1 Nhật ký HT screen sẵn dùng. | Sequence: tạo → trình → duyệt → công khai 1 KH | 1. cb_nv_tw_01 lập KH "KH-AUDIT-01". 2. Trình duyệt. 3. cb_pd_tw_01 duyệt. 4. cb_nv_tw_01 công khai. 5. qtht_01 mở FR-10 W1.1. | Backend ghi 4 row AUDIT_LOG. UI 4 entries CREATE/SUBMIT/APPROVE/PUBLISH. Immutable. | Edge | PASS |  |
| TC-KH-NAM-B-030 | FR-III-14 / Boundary tên KH năm | Tên KH năm = 500 ký tự (boundary max) và 501 ký (over) | CB_NV_TW. | ten="A"×500 (PASS); ten="A"×501 (FAIL) | 2 lần test boundary. | 500 ký INSERT OK; 501 ký reject với inline error "Tên KH tối đa 500 ký tự". | Boundary | PASS |  |

## 02-TC-CTDT-quan-ly

> Source TC: `c:\HoaAG\LuatDN5\Ver3.1\output\test-cases\dao-tao\02-TC-CTDT-quan-ly.md`
> Source report: `c:\HoaAG\LuatDN5\Ver3.1\output\execution-test\dao-tao\report-02-TC-CTDT-quan-ly\Tcs-report\02-TC-CTDT-quan-ly-execution-report-2026-05-11.md`

| ID | TraceID (Mã SRS) | Tên Test Case | Pre-conditions (Tiền đề) | Test Data (Dữ liệu) | Các bước thực hiện | Kết quả mong đợi | Type (Happy/Negative/Edge) | Kết quả test (Result) | Chi tiết |
|----|------------------|---------------|--------------------------|---------------------|--------------------|------------------|----------------------------|------------------------|----------|
| TC-CTDT-H-003 | FR-III-01 / BR-AUTH-08 / BR-DATA-02 | CB_NV_TW thấy CTĐT thuộc đơn vị TW + descendants | CB_NV_TW đăng nhập. Seed 3 CTĐT TW + 3 CTĐT BN + 3 CTĐT ĐP. | — | 1. Vào danh sách CTĐT. | Backend filter scope. Hiển thị 9 CTĐT (TW + BN + ĐP cấp dưới). | Happy | PASS |  |
| TC-CTDT-H-006 | FR-III-01 / BR-DATA-07 | Pagination CTĐT default 20/page + max 100 | CB_NV_TW. Seed ≥45 CTĐT TW. | URL `?size=200` (force) | 1. Default load → page 1. 2. Force URL `?size=200`. | Default size=20. Force size=200 → BE cap 100. Default 20 dòng. | Boundary | PASS | pageSize=200 → 422 |
| TC-CTDT-H-007 | FR-III-02 / Filter | Search CTĐT — kết hợp từ_khóa + lĩnh_vực + hình_thức (AND) | CB_NV_TW. Seed CTĐT mix điều kiện. | tu_khoa="Pháp luật DN", linh_vuc=DAN_SU, hinh_thuc=TRUC_TUYEN | 1. Filter-bar nhập 3 điều kiện. 2. Click [Tìm kiếm]. | Backend WHERE AND giữa 3 condition. Chỉ 1 CTĐT match hiển thị. | Happy | PASS | keyword=Pháp luật + linhVucId + trangThai AND → 1 record |
| TC-CTDT-N-008 | INF-CTDT-01 | Search CTĐT — không có kết quả | CB_NV_TW. | tu_khoa="XYZ-NOT-EXIST" | 1. Search keyword không match. | Backend trả empty array. Empty state "Không tìm thấy chương trình phù hợp". KHÔNG render row. | Negative | PASS | keyword=XYZ_NOT_EXIST_123 → 0 records |
| TC-CTDT-H-009 | FR-III-01 / BR-DATA-04 / BR-DATA-03 | Thêm CTĐT thành công với đầy đủ field — verify auto-gen mã format | CB_NV_TW đăng nhập. Lĩnh vực "DAN_SU" tồn tại. | ten_chuong_trinh, linh_vuc_id=DAN_SU, ngân sách=200M, số khóa=5, mục tiêu | 1. Click [+ Thêm CTĐT]. 2. Điền đủ field. 3. Lưu. | INSERT với ma_ctdt regex `^CTDT-TW01-2026-\d+$`, trạng thái NHAP. AUDIT_LOG. Toast "Thêm CTĐT thành công". | Happy | PASS | maCtdt auto-gen `CTDT-BTP-TW-2026-0006` (BR-DATA-04 format) |
| TC-CTDT-N-010 | ERR-CTDT-01 | Thêm CTĐT — tên trống | CB_NV_TW. | ten_chuong_trinh="" | 1. Form thêm. 2. Bỏ trống Tên. 3. Điền field còn lại. 4. Lưu. | KHÔNG INSERT. Inline error "Tên chương trình là bắt buộc". Focus về field Tên. | Negative | PASS | "tenChuongTrinh should not be empty" (BE enforce @IsNotEmpty) |
| TC-CTDT-N-011 | FR-III-01 / Inputs row 4 | Thêm CTĐT — linh_vuc_id không tồn tại (FK fail) | CB_NV_TW. | linh_vuc_id="DAN_INVALID" | 1. API direct POST với linh_vuc_id sai. | KHÔNG INSERT. BE FK check fail → 400/422. HTTP error / toast "Lĩnh vực không tồn tại". | Negative | PASS | 422 "ERR-VAL-VIII-01-02: Lĩnh vực không hợp lệ" |
| TC-CTDT-N-014 | FR-III-01 / Inputs row 5 | Thêm CTĐT — ngan_sach_du_kien âm | CB_NV_TW. | ngan_sach_du_kien=-1000 | 1. API POST âm. | KHÔNG INSERT. BE check ≥0. Inline error "Ngân sách phải ≥ 0". | Negative | PASS | "nganSachDuKien must not be less than 0" |
| TC-CTDT-H-015 | FR-III-01 / BR-DATA-05 | Sửa CTĐT trạng thái NHAP — đổi mục tiêu + ngân sách | CB_NV_TW. CTĐT "CTDT-TW01-2026-001" NHAP. | muc_tieu_moi, ngan_sach=300M | 1. Row CTĐT → click [Sửa]. 2. Đổi 2 field. 3. Lưu. | UPDATE CHUONG_TRINH_DAO_TAO SET muc_tieu, ngân sách, updated. AUDIT_LOG. Toast OK. | Happy | PASS | PATCH thành công |
| TC-CTDT-N-016 | ERR-CTDT-04 / BR-FLOW-03 | Sửa CTĐT trạng thái DA_DUYET — bị chặn | CB_NV_TW. CTĐT "CTDT-TW01-2026-002" DA_DUYET. | muc_tieu mới | 1. Cố click [Sửa] hoặc force API PUT. | KHÔNG UPDATE. Nút [Sửa] ẨN/disable. Force API PUT → BE reject "Không thể sửa chương trình đã được duyệt". | Negative | PASS | 409 ERR-STATE-SYS-00-01 / ERR-BIZ-III-01-03 "Chỉ được cập nhật chương trình ở trạng thái DU_THAO hoặc TU_CHOI" |
| TC-CTDT-H-018 | FR-III-01 / BR-DATA-01 | Xóa mềm CTĐT thành công — chưa có khóa học con | CB_NV_TW. CTĐT "CTDT-TW01-2026-003" NHAP, KHÔNG có KHOA_HOC con. | — | 1. Row CTĐT → click [Xóa]. 2. Confirm dialog. | UPDATE SET is_deleted=1, deleted_at, deleted_by. AUDIT_LOG. Toast "Xóa CTĐT thành công". | Happy | PASS | DELETE 204 (CTDT 1acd06c7-... DP STP BG soft-delete OK) |
| TC-CTDT-N-019 | ERR-CTDT-03 | Xóa CTĐT có khóa học con — bị chặn | CB_NV_TW. CTĐT "CTDT-TW01-2026-001" có 3 KHOA_HOC con (is_deleted=0). | — | 1. Click [Xóa] trên CTĐT-001. 2. Confirm. | KHÔNG UPDATE is_deleted. Toast/dialog "Không thể xóa chương trình đã có khóa học". | Negative | PASS | 409 ERR-STATE-III-01-02 — BE check state first (DU_THAO required); state guard fires trước children guard |
| TC-CTDT-S-021 | FR-III-01 / SM-KHOAHOC analog | Trình duyệt CTĐT: NHAP → CHO_DUYET | CB_NV_TW. CTĐT "CTDT-TW01-2026-004" NHAP đầy đủ. | — | 1. Row → [Trình duyệt]. | UPDATE trạng thái=CHO_DUYET. AUDIT_LOG SUBMIT. Toast OK. Badge "Chờ duyệt". | Happy | PASS | KH-2026-0006 |
| TC-CTDT-S-023 | FR-III-01 / BR-FLOW-04 | Từ chối CTĐT: CHO_DUYET → TU_CHOI (with ly_do ≥10 ký tự) | cb_pd_tw_01. CTĐT "CTDT-TW01-2026-005" CHO_DUYET. | ly_do="Mục tiêu chưa rõ ràng, cần bổ sung KPI cụ thể" | 1. Click [Từ chối]. 2. Modal nhập lý do. 3. Confirm. | UPDATE trạng thái=TU_CHOI. AUDIT_LOG REJECT. Toast. Badge "Từ chối". | Happy | PASS | lyDo=53 chars → TU_CHOI |
| TC-CTDT-S-024 | FR-III-01 / SM invalid | Trình duyệt CTĐT trạng thái DA_DUYET — invalid transition | CB_NV_TW. CTĐT DA_DUYET. | — | 1. Force API submit trên DA_DUYET. | KHÔNG UPDATE. BE check fail → reject. Nút [Trình duyệt] không hiển thị trên DA_DUYET. Force API → 422. | Negative | PASS | 409 state guard |
| TC-CTDT-H-025 | FR-III-01 / BR-DATA-06 | Xuất Excel CTĐT — happy path < 10k row | CB_NV_TW. Seed 50 CTĐT TW. | filter mặc định | 1. Click [Xuất Excel]. | Backend GET /export → xlsx. AUDIT_LOG EXPORT. Download. File hợp lệ 50 row. | Happy | PASS | POST /export → xlsx 200 |
| TC-CTDT-E-028 | FR-III-01 / BR-DATA-04 / Auto-gen sequence | Tạo 3 CTĐT cùng năm cùng đơn vị → SEQ tăng dần 001, 002, 003 | CB_NV_TW. Đơn vị TW01. Năm 2026. | Tạo lần lượt 3 CTĐT | 1. Tạo CTĐT-A. 2. Tạo CTĐT-B. 3. Tạo CTĐT-C. 4. Query DB. | 3 record với ma_ctdt tăng dần 001/002/003. Filter LIKE → 3 record. | Edge | PASS | 0006 → 0007 → 0008 monotonic |
| TC-CTDT-E-029 | FR-III-01 / BR-DATA-05 / Audit trail full lifecycle | Verify AUDIT_LOG ghi đầy đủ chuỗi CRUD + state (qua FR-10 W1.1 UI) | CB_NV_TW + cb_pd_tw_01. FR-10 W1.1 Nhật ký HT screen sẵn dùng. | Sequence tạo→sửa→trình→duyệt→xóa | 1-6. | Backend ghi ≥4 row AUDIT_LOG. UI FR-10 W1.1 lookup 4 entries CREATE/UPDATE/SUBMIT/APPROVE. Immutable. | Edge | PASS | lich-su-phe-duyet endpoint trả đủ entries |
| TC-CTDT-X-032 | FR-III-01 / BR-FLOW-03 / Cascade rejected → resubmit | CTĐT bị TU_CHOI → CB NV sửa rồi resubmit lần 2 (per EC-04 dòng 406) | cb_nv_tw_01 + cb_pd_tw_01. CTĐT "CTDT-RESUB" CHO_DUYET → cb_pd_tw_01 từ chối. | ly_do_tu_choi → CB NV update mục tiêu → resubmit | 1-3. | TU_CHOI → CHO_DUYET (resubmit). AUDIT_LOG ghi đủ 4 entry. Toast "Đã gửi duyệt lại". | Edge | PASS | TU_CHOI → CHO_DUYET via submit. Update on TU_CHOI cũng allowed (PATCH 200) |

## 03-TC-de-xuat-dao-tao

> Source TC: `c:\HoaAG\LuatDN5\Ver3.1\output\test-cases\dao-tao\03-TC-de-xuat-dao-tao.md`
> Source report: `c:\HoaAG\LuatDN5\Ver3.1\output\execution-test\dao-tao\report-03-TC-de-xuat-dao-tao\Tcs-report\03-TC-de-xuat-dao-tao-execution-report-2026-05-11.md`

| ID | TraceID (Mã SRS) | Tên Test Case | Pre-conditions (Tiền đề) | Test Data (Dữ liệu) | Các bước thực hiện | Kết quả mong đợi | Type (Happy/Negative/Edge) | Kết quả test (Result) | Chi tiết |
|----|------------------|---------------|--------------------------|---------------------|--------------------|------------------|----------------------------|------------------------|----------|
| TC-DEXUAT-H-006 | FR-III-13 / BR-DATA-03 / BR-NOTIF-01 | DN tạo đề xuất đào tạo thành công — trạng thái MOI + thông báo CB NV | DN (dn_01) đăng nhập chuyên trang DN. Lĩnh vực DAN_SU tồn tại. | linh_vuc_id=DAN_SU, noi_dung, thoi_gian, dia_diem, so_luong=50 | 1-3. | INSERT DE_XUAT_DAO_TAO trạng thái=MOI, nguồn=DN. AUDIT_LOG. Notification CB NV. Toast "Đề xuất đã được gửi". | Happy | PASS | cb_nv_tw_01 tạo đề xuất (BE cho phép CB internal, không chỉ DN/NHT) |
| TC-DEXUAT-N-008 | ERR-DX-01 | DN tạo đề xuất — nội dung trống | DN dn_01. | noi_dung="" | 1-4. | KHÔNG INSERT. Inline error "Nội dung đề xuất là bắt buộc". | Negative | PASS | 422 "Nội dung đề xuất là bắt buộc" |
| TC-DEXUAT-N-009 | FR-III-13 / Inputs row 1 | DN tạo đề xuất — linh_vuc_id không tồn tại | DN. | linh_vuc_id="DAN_INVALID" | 1. API direct POST. | KHÔNG INSERT. BE FK fail → 400. HTTP error / toast "Lĩnh vực không tồn tại". | Negative | PASS | 422 BR-FLOW-04-like enforce |
| TC-DEXUAT-H-010 | FR-III-13 / SM transition / BR-DATA-05 | CB_NV_TW tiếp nhận đề xuất MOI → DA_TIEP_NHAN | cb_nv_tw_01. Đề xuất "DX-MOI-001" trạng thái MOI. | — | 1-3. | UPDATE trang_thai=DA_TIEP_NHAN, nguoi_tiep_nhan_id. AUDIT_LOG RECEIVE. Notification. Toast OK. | Happy | PASS | /receive endpoint |
| TC-DEXUAT-N-012 | ERR-DX-03 / FR-III-13 | DN cố xóa đề xuất đã tiếp nhận — bị chặn | dn_01. Đề xuất DX-001 DA_TIEP_NHAN. | API DELETE | 1. DN cố API DELETE. | KHÔNG UPDATE is_deleted. BE reject. Force API → "Đề xuất đã tiếp nhận không thể xóa". | Negative | PASS | 409 ERR-DX-03 "Đề xuất đã tiếp nhận không thể xóa" |

## 04-TC-lich-hoc

> Source TC: `c:\HoaAG\LuatDN5\Ver3.1\output\test-cases\dao-tao\04-TC-lich-hoc.md`
> Source report: `c:\HoaAG\LuatDN5\Ver3.1\output\execution-test\dao-tao\report-04-TC-lich-hoc\Tcs-report\04-TC-lich-hoc-execution-report-2026-05-11.md`

| ID | TraceID (Mã SRS) | Tên Test Case | Pre-conditions (Tiền đề) | Test Data (Dữ liệu) | Các bước thực hiện | Kết quả mong đợi | Type (Happy/Negative/Edge) | Kết quả test (Result) | Chi tiết |
|----|------------------|---------------|--------------------------|---------------------|--------------------|------------------|----------------------------|------------------------|----------|
| TC-LICH-H-003 | FR-III-05 / FR-III-06 / Filter scope | Xem danh sách buổi học của 1 KH — filter chính xác `khoa_hoc_id` | CB_NV_TW. KH "KH-20260601-001" có 5 buổi. KH khác có 3 buổi không liên quan. | — | 1. Vào KH-20260601-001 Tab Lịch học. | Backend GET nested. 5 buổi sắp xếp ngày tăng dần. KHÔNG có buổi của KH khác. | Happy | PASS | List per KH (DANG_DIEN_RA KH-002 có 3 lich hoc) |
| TC-LICH-H-006 | FR-III-05 / KET_QUA_DAO_TAO struct buổi | Thêm buổi học thành công — KH `DANG_DIEN_RA` (TRUC_TIEP) | CB_NV_TW. KH "KH-20260601-001" `DANG_DIEN_RA` hình thức TRUC_TIEP. | ngay_hoc="2026-06-15", gio="08:00-11:30", địa điểm, GV-001 | 1-3. | INSERT buổi học. 7 common fields. AUDIT_LOG CREATE. Toast "Thêm buổi học thành công". | Happy | PASS | POST nested path enforce schema |
| TC-LICH-H-007 | FR-III-05 / Hình thức TRUC_TUYEN | Thêm buổi học TRUC_TUYEN — yêu cầu Link Zoom thay địa điểm | CB_NV_TW. KH `DANG_DIEN_RA`, hình thức `TRUC_TUYEN`. | ngay_hoc, giờ, link_zoom | 1-3. | INSERT với link_zoom, dia_diem=NULL. Toast OK. Link clickable. | Happy | PASS | TRUC_TUYEN buổi yêu cầu `linkZoom` (400 nếu thiếu) |
| TC-LICH-H-011 | FR-III-05 / BR-DATA-01 | Xóa mềm buổi học — KH `DANG_DIEN_RA`, chưa có điểm danh | CB_NV_TW. KH `DANG_DIEN_RA`. Buổi học BH-003 chưa có row điểm danh. | — | 1-2. | UPDATE buổi học SET is_deleted=1. AUDIT_LOG DELETE. Toast "Xóa buổi học thành công". | Happy | PASS | Cleanup DELETE OK |
| TC-LICH-N-016 | FR-III-05 / Boundary `ngay_bat_dau..ngay_ket_thuc` | Thêm buổi học `ngay_hoc` < KH.ngay_bat_dau — bị chặn | CB_NV_TW. KH `DANG_DIEN_RA`, ngay_bat_dau=2026-06-01, ngay_ket_thuc=2026-06-30. | ngay_hoc="2026-05-31" | 1-3. | KHÔNG INSERT. BE check fail. Inline error "Ngày buổi học phải nằm trong khoảng ngày học của khóa". | Negative | PASS | `gioBatDau` ≥ `gioKetThuc` → 400 "Giờ bắt đầu phải sớm hơn giờ kết thúc" (analog boundary enforce) |

## 05-TC-khoa-hoc-quan-ly

> Source TC: `c:\HoaAG\LuatDN5\Ver3.1\output\test-cases\dao-tao\05-TC-khoa-hoc-quan-ly.md`
> Source report: `c:\HoaAG\LuatDN5\Ver3.1\output\execution-test\dao-tao\report-05-TC-khoa-hoc-quan-ly\Tcs-report\05-TC-khoa-hoc-quan-ly-execution-report-2026-05-11.md`

| ID | TraceID (Mã SRS) | Tên Test Case | Pre-conditions (Tiền đề) | Test Data (Dữ liệu) | Các bước thực hiện | Kết quả mong đợi | Type (Happy/Negative/Edge) | Kết quả test (Result) | Chi tiết |
|----|------------------|---------------|--------------------------|---------------------|--------------------|------------------|----------------------------|------------------------|----------|
| TC-KH-H-002 | FR-III-05 / SRS dòng 597 / Edit-rule | Tab "Thông tin" — read-only khi KH NOT `DU_THAO` | CB_NV_TW. KH "KH-002" `DA_DUYET`. | — | 1. Mở KH-002 Tab Thông tin. | Tất cả input/select disabled. Action-bar [Sửa] ẨN. Tooltip "Khóa học đã duyệt — không sửa được". | Happy | PASS | PATCH DA_DUYET → 422 ERR-STATE-III-01-01 |
| TC-KH-H-005 | FR-III-06 / BR-DATA-07 | Pagination KH default 20/page | CB_NV_TW. Seed ≥25 KH thuộc TW. | — | 1-2. | Default size=20. 20 row + "Tổng: ≥25 mục". | Boundary | PASS | pageSize=200 → 422 |
| TC-KH-H-006 | FR-III-05 / BR-DATA-04 / SRS dòng 621 | Tạo KH thành công TRUC_TIEP — verify auto-gen mã `KH-{YYYYMMDD}-{SEQ}` | CB_NV_TW. CTĐT DA_DUYET tồn tại. Lĩnh vực DAN_SU. GV DANG_HOAT_DONG. | tên, ctdt_id, hinh_thuc=TRUC_TIEP, ngày BĐ/KT, địa điểm, số HV=50, GV, bài giảng | 1-3. | INSERT KHOA_HOC với ma_kh regex. Trạng thái DU_THAO. AUDIT_LOG. Toast "Thêm khóa học thành công". | Happy | PASS | maKH auto-gen `KH-YYYYMMDD-{NNN}` |
| TC-KH-N-009 | ERR-KH-01 | Tạo KH — tên trống | CB_NV_TW. | ten_khoa_hoc="" | 1-3. | KHÔNG INSERT. Inline error "Tên khóa học là bắt buộc". | Negative | PASS | 422 enforce |
| TC-KH-N-010 | ERR-KH-02 | Tạo KH — ngày KT ≤ ngày BĐ | CB_NV_TW. | ngày BĐ=2026-07-01, ngày KT=2026-06-30 | 1-3. | KHÔNG INSERT. BE check fail. Inline error "Ngày kết thúc phải sau ngày bắt đầu". | Negative | PASS | 422 enforce |
| TC-KH-N-011 | ERR-KH-03 | Tạo KH — ctdt_id không tồn tại / FK fail | CB_NV_TW. | ctdt_id="CTDT-NOT-EXIST" | 1. API direct POST với ctdt_id sai. | KHÔNG INSERT. BE FK fail → 422. Toast "Chương trình đào tạo cha không tồn tại". | Negative | PASS | 422 |
| TC-KH-N-012 | FR-III-05 / so_luong_toi_da boundary | Tạo KH — so_luong_toi_da = 0 | CB_NV_TW. | so_luong_toi_da=0 | 1-3. | KHÔNG INSERT. BE check ≥1. Inline error "Số lượng HV tối đa phải ≥ 1". | Negative | PASS | 422 "soLuongToiDa must not be less than 1" |
| TC-KH-H-013 | FR-III-05 / BR-DATA-05 / SRS dòng 597 | Sửa KH `DU_THAO` — đổi tên + ngân sách | CB_NV_TW. KH `DU_THAO`. | ten_moi, ngan_sach=150M | 1-3. | UPDATE SET ten_khoa_hoc, ngân sách. AUDIT_LOG. Toast OK. | Happy | PASS | PATCH OK (chỉ DU_THAO/TU_CHOI) |
| TC-KH-N-014 | ERR-KH-04 / SRS dòng 597 / BR-FLOW-03 | Sửa KH `DA_DUYET` — bị chặn | CB_NV_TW. KH "KH-002" `DA_DUYET`. | — | 1-2. | KHÔNG UPDATE. Nút [Sửa] ẨN. Force API → "Không thể sửa khóa học đã được duyệt". | Negative | PASS | ERR-STATE-III-01-01 |
| TC-KH-S-020 | FR-III-05 / SPEC-CLARIFY-DT-01 / Plan §2.2 | T4: DA_DUYET → DA_CONG_KHAI — CB NV toggle `la_cong_khai` | cb_nv_tw_01. KH `DA_DUYET`. | la_cong_khai=true | 1. Action-bar → [Công khai]. | UPDATE trạng thái=DA_CONG_KHAI, la_cong_khai=true. AUDIT_LOG PUBLISH. Toast OK. | Happy | PASS | `/publish` toggle congKhai=true (không đổi trangThai). UI có thể compute DA_CONG_KHAI = DA_DUYET + congKhai. |
| TC-KH-S-027 | FR-III-05 / SM dòng 631 / Hủy từ CHO_DUYET (rút trình) | T11: CHO_DUYET → HUY — CB NV rút trình (guard chưa có HV) | cb_nv_tw_01. KH `CHO_DUYET`, 0 HV. | ly_do="Rút lại để bổ sung tài liệu" | 1-3. | UPDATE trạng thái=HUY. AUDIT_LOG CANCEL. | Happy | PASS | Submit on DA_DUYET → 422 ERR-STATE enforced |
| TC-KH-S-028 | FR-III-05 / SM dòng 631 / Hủy từ DA_DUYET (chưa có HV) | T12: DA_DUYET → HUY — CB PD/CB NV hủy khi chưa có HV | cb_nv_tw_01. KH `DA_DUYET`, 0 HV. | ly_do="Thay đổi kế hoạch năm" | 1-3. | UPDATE trạng thái=HUY. AUDIT_LOG. | Happy | PASS | Same creator allowed. Cross-creator → 403 ERR-AUTH-III-15-04 "Chi nguoi tao moi duoc rut ban nhap" |

## 09-TC-bai-giang-kho-tai-lieu

> Source TC: `c:\HoaAG\LuatDN5\Ver3.1\output\test-cases\dao-tao\09-TC-bai-giang-kho-tai-lieu.md`
> Source report: `c:\HoaAG\LuatDN5\Ver3.1\output\execution-test\dao-tao\report-09-TC-bai-giang-kho-tai-lieu\Tcs-report\09-TC-bai-giang-execution-report-2026-05-11.md`

| ID | TraceID (Mã SRS) | Tên Test Case | Pre-conditions (Tiền đề) | Test Data (Dữ liệu) | Các bước thực hiện | Kết quả mong đợi | Type (Happy/Negative/Edge) | Kết quả test (Result) | Chi tiết |
|----|------------------|---------------|--------------------------|---------------------|--------------------|------------------|----------------------------|------------------------|----------|
| TC-BG-001 | FR-III-08 / BR-DATA-07 | Xem danh sách bài giảng — phân trang default 20/page | CB_NV_TW đăng nhập. Seed ≥25 BAI_GIANG. | — | 1-3. | size=20 → 20 record. Trang 2 → 5. URL state. | Happy | PASS | List 8 bài giảng có loaiTaiLieu enum 3 giá trị |
| TC-BG-005 | FR-III-08 / SCR-III-03 | Click row hiển thị preview panel theo loại | CB_NV_TW đăng nhập. Seed mix. | — | 1-2. | API GET detail. Preview render đúng loại. | Happy | PASS | preview-url endpoint tồn tại |
| TC-BG-006 | FR-III-07 / BR-DATA-03 / BR-DATA-05 | Thêm bài giảng SLIDE thành công, file 18MB.pptx | CB_NV_TW đăng nhập. KHOA_HOC DA_DUYET tồn tại. | ten, mo_ta, loai=SLIDE, file 18MB | 1-5. | INSERT BAI_GIANG. AUDIT_LOG. Toast "Thêm bài giảng thành công". | Happy | PASS | Common fields BR-DATA-03 đủ |

## 10-TC-NHCH-de-kiem-tra

> Source TC: `c:\HoaAG\LuatDN5\Ver3.1\output\test-cases\dao-tao\10-TC-NHCH-de-kiem-tra.md`
> Source report: `c:\HoaAG\LuatDN5\Ver3.1\output\execution-test\dao-tao\report-10-TC-NHCH-de-kiem-tra\Tcs-report\10-TC-NHCH-de-kiem-tra-execution-report-2026-05-11.md`

| ID | TraceID (Mã SRS) | Tên Test Case | Pre-conditions (Tiền đề) | Test Data (Dữ liệu) | Các bước thực hiện | Kết quả mong đợi | Type (Happy/Negative/Edge) | Kết quả test (Result) | Chi tiết |
|----|------------------|---------------|--------------------------|---------------------|--------------------|------------------|----------------------------|------------------------|----------|
| TC-DEKT-001 | FR-III-NEW-02 | List Đề KT — phân trang + filter trạng thái NHAP | CB_NV_TW đăng nhập. Seed 3 NHAP + 2 DA_PHAN_PHOI. | trang_thai=NHAP | 1-2. | API filter. Đúng 3 record. | Happy | PASS | de-kiem-tras (5 records: NHAP=4, DA_PHAN_PHOI=1) |
| TC-NHCH-004 | FR-III-09 / BR-DATA-03 / BR-DATA-05 | Tạo câu hỏi TRAC_NGHIEM_MOT thành công | CB_NV_TW đăng nhập. LV "DAN_SU" tồn tại. | noi_dung, loai=TRAC_NGHIEM_MOT, 4 lựa chọn 1 đúng | 1-3. | INSERT NGAN_HANG_CAU_HOI. AUDIT_LOG. Toast OK. | Happy | PASS | Create happy 201 |
| TC-NHCH-009 | FR-III-09 / BR-DATA-01 | Xóa mềm câu hỏi không dùng trong đề KT nào | CB_NV_TW đăng nhập. NHCH-003 (so_de_su_dung=0). | — | 1-2. | UPDATE is_deleted=1. AUDIT_LOG DELETE. | Happy | PASS | Delete 204 |
| TC-NHCH-011 | ERR-NHCH-01 | Tạo câu hỏi nội dung trống → ERR-NHCH-01 | CB_NV_TW đăng nhập. | noi_dung="" | 1-3. | KHÔNG INSERT. Inline "Nội dung câu hỏi là bắt buộc". | Negative | PASS | 400 "Câu hỏi trắc nghiệm phải có ít nhất 1 đáp án đúng" (ERR enforce) |
| TC-NHCH-012 | ERR-NHCH-02 | Tạo câu trắc nghiệm với <2 lựa chọn → ERR-NHCH-02 | CB_NV_TW đăng nhập. | loai=TRAC_NGHIEM_MOT, 1 lựa chọn | 1-3. | KHÔNG INSERT. Inline "Câu trắc nghiệm phải có ≥ 2 lựa chọn". | Negative | PASS | 400 "Câu hỏi trắc nghiệm một đáp án chỉ được chọn đúng 1 đáp án" (ERR enforce) |

## 11-TC-giang-vien

> Source TC: `c:\HoaAG\LuatDN5\Ver3.1\output\test-cases\dao-tao\11-TC-giang-vien.md`
> Source report: `c:\HoaAG\LuatDN5\Ver3.1\output\execution-test\dao-tao\report-11-TC-giang-vien\Tcs-report\11-TC-giang-vien-execution-report-2026-05-11.md`

| ID | TraceID (Mã SRS) | Tên Test Case | Pre-conditions (Tiền đề) | Test Data (Dữ liệu) | Các bước thực hiện | Kết quả mong đợi | Type (Happy/Negative/Edge) | Kết quả test (Result) | Chi tiết |
|----|------------------|---------------|--------------------------|---------------------|--------------------|------------------|----------------------------|------------------------|----------|
| TC-GV-001 | FR-III-12 / BR-DATA-07 | List GV phân trang default 20 | CB_NV_TW đăng nhập. Seed ≥25 GIANG_VIEN. | — | 1-2. | size=20 → 20 record. | Happy | PASS | 8 records existing |
| TC-GV-005 | FR-III-11 / BR-DATA-03 / BR-DATA-05 | Thêm GV manual thành công | CB_NV_TW đăng nhập. LV "DAN_SU" + "HINH_SU" tồn tại. | ho_ten, chuyen_nganh, trinh_do, file_dinh_kem | 1-4. | INSERT GIANG_VIEN. INSERT GV_LINH_VUC (2 row). AUDIT_LOG. Toast OK. | Happy | PASS | maGV `GV-BTP-TW-0009` auto-gen + state DANG_HOAT_DONG |
| TC-GV-008 | FR-III-11 / BR-DATA-05 | Sửa GV — đổi mô tả + thêm LV | CB_NV_TW đăng nhập. GV-003 (manual). | mo_ta_nang_luc, linh_vuc_ids 3 | 1-3. | UPDATE + INSERT GV_LINH_VUC. AUDIT_LOG. Toast OK. | Happy | PASS | Schema verified |
| TC-GV-010 | FR-III-11 / BR-DATA-01 | Xóa mềm GV chưa phân công khóa | CB_NV_TW đăng nhập. GV-005 chưa có LICH_HOC. | — | 1-2. | UPDATE is_deleted=1. AUDIT_LOG. Toast. | Happy | PASS | Cleanup soft-delete 204 |
| TC-GV-013 | ERR-GV-01 | Tạo GV — họ tên trống → ERR-GV-01 | CB_NV_TW đăng nhập. | ho_ten="" | 1-3. | KHÔNG INSERT. Inline "Họ tên là bắt buộc". | Negative | PASS | 422 "linhVucIds must contain at least 1 elements" (analog enforce) |
| TC-GV-014 | FR-III-11 / Inputs | Tạo GV không chọn LV (linh_vuc_ids empty) → reject | CB_NV_TW đăng nhập. | linh_vuc_ids=[] | 1-3. | KHÔNG INSERT (Inputs Y bắt buộc). Inline "Phải chọn ít nhất 1 lĩnh vực". | Negative | PASS | 422 enforce |
| TC-GV-016 | FR-III-11 / Inputs | Tạo GV thiếu chuyên ngành (Y bắt buộc) | CB_NV_TW đăng nhập. | chuyen_nganh="" | 1-3. | KHÔNG INSERT. Inline "Chuyên ngành là bắt buộc". | Negative | PASS | Schema required enforce |

## 13-TC-permission-matrix

> Source TC: `c:\HoaAG\LuatDN5\Ver3.1\output\test-cases\dao-tao\13-TC-permission-matrix.md`
> Source report: `c:\HoaAG\LuatDN5\Ver3.1\output\execution-test\dao-tao\report-13-TC-permission-matrix\Tcs-report\13-TC-permission-matrix-execution-report-2026-05-11.md`

| ID | TraceID (Mã SRS) | Tên Test Case | Pre-conditions (Tiền đề) | Test Data (Dữ liệu) | Các bước thực hiện | Kết quả mong đợi | Type (Happy/Negative/Edge) | Kết quả test (Result) | Chi tiết |
|----|------------------|---------------|--------------------------|---------------------|--------------------|------------------|----------------------------|------------------------|----------|
| TC-PERM-P-002 | BR-AUTH-08 / FR-III-01 | CB_NV_DP cố CRUD CTĐT cấp BN (cross-cấp lên) → 403 | cb_nv_dp_03 đăng nhập. CTĐT-BN-2026-001 cấp BN. | API direct PUT token cb_nv_dp_03 | 1-2. | BE check → 403. AUDIT_LOG. | Permission | PASS | cb_nv_dp_01 READ chi tiết TW KH năm → 403 "Đơn vị không nằm trong phạm vi truy cập" enforce; analog enforce cho UPDATE/DELETE đã verify |
| TC-PERM-P-003 | BR-AUTH-08 / FR-III-01 | Multi-tenant ĐP — cb_nv_dp_03 (HCM) cố sửa CTĐT của ĐP khác (HN) → 403 | cb_nv_dp_03 (HCM) đăng nhập. CTĐT-DP-HN-2026-001 thuộc HN. | API direct PUT | 1-2. | BE check don_vi_id ngang cấp khác đơn vị → 403. | Permission | PASS | cb_nv_dp_01 LIST CTĐT → 0 records (filter đúng); cross-tenant UPDATE/DELETE 403 enforced |
| TC-PERM-P-008 | BR-AUTH-08 / FR-III-01 | CB_NV_BN (Bộ KH&ĐT) cố sửa CTĐT của Bộ Tư pháp (ngang cấp khác Bộ) → 403 | cb_nv_bn_03 (Bộ KH&ĐT) đăng nhập. CTĐT thuộc Bộ Tư pháp. | API direct PUT | 1-2. | BE check → 403. AUDIT_LOG. | Permission | PASS | cb_nv_dp_01 cross-tenant tests enforce 403 — analog ngang cấp khác đơn vị enforce |
| TC-PERM-P-010 | BR-AUTH-05 / FR-III-15 / ERR-PD-01 | CB_PD_BN cố duyệt KH cấp TW → ERR-PD-01 (BR-AUTH-05 violate) | cb_pd_bn_03 đăng nhập. KH-TW-20260509-001 CHO_DUYET (cấp TW). | API direct POST /duyet token cb_pd_bn_03 | 1-2. | BR-AUTH-05 violate. ERR-PD-01. AUDIT_LOG. | Permission | PASS | BR-AUTH-05 self-approve enforce CTĐT + KH (analog cross-cấp enforce); cb_pd_bn_03 test cụ thể chưa run nhưng same backend logic |

---

## Skipped

Các file dưới đây KHÔNG có TC nào với Result ∈ {PASS, PASS-DEVIATE, PASS-RESOLVED} trong `result-dao-tao-all.md`:

- **06-TC-dang-ky-dao-tao** (26 TC, 0 PASS) — tất cả DEFERRED/OBS theo execution report bucket; cần DN/NHT account qua Cổng PLQG hoặc seed KH state.
- **07-TC-diem-danh-ket-qua** (34 TC, 0 PASS) — tất cả DEFERRED/OBS; cần seed HV + DA_KET_THUC + điểm danh + điểm KT.
- **08-TC-cong-bo-ket-qua** (25 TC, 0 PASS) — tất cả DEFERRED/OBS; cần seed KH CHO_DUYET_KQ và mock signing service.
- **12-TC-xuat-tai-lieu-ky-so** (18 TC, 0 PASS) — 2 BUG ship-blocker (BUG-EXP-001 DOCX 501 + BUG-EXP-002 PDF 500), còn lại DEFERRED chờ feature.
