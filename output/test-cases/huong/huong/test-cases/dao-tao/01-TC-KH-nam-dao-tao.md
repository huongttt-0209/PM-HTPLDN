# Test Cases — UC33/UC34/UC35: Kế hoạch năm Đào tạo (FR-III-14 + FR-III-15 + FR-III-16)

> **SRS Ref**: FR-III-14 (UC33 Lập KH), FR-III-15 (UC34 Phê duyệt KH), FR-III-16 (UC35 Công khai KH). Entity: KE_HOACH_DAO_TAO. Workflow: CB NV [Lập] → [Trình duyệt] → CB PD cùng cấp [Duyệt/Từ chối] → CB NV [Công khai] (BR-FLOW-05 outbound API).
> **Nguồn**: SRS local `srs-fr-03-dao-tao.md` dòng 895-969 + `02-thu-tu-module.md` §⑨ dòng 573-633 + Phụ lục B BR + Plan overview §2.
> **Ngày tạo**: 2026-05-09 (Phase A re-run)
> **Phạm vi tài khoản**: cb_nv_tw_01 (lập KH), cb_pd_tw_01 (phê duyệt), cb_nv_bn_01/cb_pd_bn_01 (BN cross-cấp), DN/NHT (read public).

---

## A. UI FIELD VERIFICATION (BẮT BUỘC chạy trước functional)

| ID | TraceID (Mã SRS) | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|-------------------|--------------|----------------|-----------|-------------------|------------------|------|
| TC-KH-NAM-H-001 | FR-III-14 / SCR-III-01 / UI | Verify Tab "Kế hoạch năm" SCR-III-01 — danh sách + filter + action-bar | CB_NV_TW (cb_nv_tw_01) đăng nhập. Seed ≥3 KH năm cover trạng thái NHAP/CHO_DUYET/DA_DUYET. | URL: `/dao-tao/ke-hoach-nam` (giả định theo SCR-III-01 layout) | 1. Đăng nhập CB_NV_TW. 2. Vào menu "Đào tạo > Kế hoạch năm". 3. Kiểm tra layout. | **STATE**: Backend `GET /api/v1/ke-hoach-dao-tao?...` (verify network). **UI**: Breadcrumb "Đào tạo > Kế hoạch năm" + toolbar [+ Lập KH năm] [Xuất Excel]. Filter-bar: Năm (select), Tên KH (text), CTĐT (select FK), Trạng thái (dropdown 4 giá trị NHAP/CHO_DUYET/DA_DUYET/TU_CHOI), [Tìm kiếm] [Xóa lọc]. Bảng cột: Mã KH, Tên KH, CTĐT liên kết, Thời gian (BĐ→KT), Ngân sách, Trạng thái (badge), Hành động (Xem/Sửa/Xóa/Trình duyệt/Công khai theo state). Pagination 20/page. **PERSIST**: Reload giữ filter. | Happy 🔴 |
| TC-KH-NAM-H-002 | FR-III-14 / SCR-III-01 / UI Form | Verify Form Lập KH năm — đầy đủ field theo FR-III-14 inputs | CB_NV_TW đăng nhập. CTĐT TW seed sẵn ≥1 record. | — | 1. Click [+ Lập KH năm]. 2. Kiểm tra form. | **STATE**: — (form open). **UI**: Drawer/modal title "Lập kế hoạch đào tạo". 7 field: Tên KH * (text max 500), CTĐT * (searchable select FK), Thời gian BĐ * (date), Thời gian KT * (date > BĐ), Ngân sách dự kiến (money ≥0), Nguồn lực (textarea max 5000), Ghi chú (textarea max 5000). Action-bar [Hủy] [Lưu nháp]. **PERSIST**: Click [Hủy] → form đóng, không INSERT. | Happy 🔴 |

---

## B. READ / LIST

| ID | TraceID (Mã SRS) | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|-------------------|--------------|----------------|-----------|-------------------|------------------|------|
| TC-KH-NAM-H-003 | FR-III-14 / BR-AUTH-08 | CB_NV_TW thấy KH năm thuộc đơn vị TW + descendants | CB_NV_TW đăng nhập. Seed 2 KH TW + 2 KH BN + 2 KH ĐP. | — | 1. Vào danh sách KH năm. 2. Quan sát số dòng. | **STATE**: Backend filter `WHERE don_vi_id IN (descendants_of_TW)`. **UI**: Hiển thị tất cả 6 KH (TW + BN + ĐP) per BR-AUTH-04 cấp trên thấy cấp dưới. Pagination 20/page. **PERSIST**: Reload giữ scope. | Happy |
| TC-KH-NAM-H-004 | FR-III-14 / BR-AUTH-08 | CB_NV_BN chỉ thấy KH năm thuộc đơn vị BN | CB_NV_BN (cb_nv_bn_01) đăng nhập. Seed 2 KH TW + 2 KH BN + 2 KH ĐP khác. | — | 1. CB_NV_BN vào danh sách. | **STATE**: Backend `WHERE don_vi_id = cb_nv_bn_01.don_vi_id`. **UI**: Chỉ 2 KH BN của user. KHÔNG thấy KH TW (cấp trên) hoặc KH BN khác. **PERSIST**: Reload giữ scope. | Happy |
| TC-KH-NAM-H-005 | FR-III-14 / BR-DATA-07 | Pagination default 20/page + click trang 2 | CB_NV_TW. Seed ≥25 KH năm trạng thái DA_DUYET. | — | 1. Vào danh sách. 2. Quan sát pagination. 3. Click page 2. | **STATE**: Request `?page=1&size=20` → 20 record; page 2 → 5 record. **UI**: Page 1 có 20 dòng, "Tổng: 25 mục". Page 2 có 5 dòng. **PERSIST**: Reload page 2 → giữ trang nếu URL sync (SPEC-CLARIFY-DT-02 nếu không sync). | Happy |

---

## C. CREATE (Lập KH năm)

| ID | TraceID (Mã SRS) | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|-------------------|--------------|----------------|-----------|-------------------|------------------|------|
| TC-KH-NAM-H-006 | FR-III-14 / BR-DATA-03 / BR-DATA-05 | Lập KH năm thành công — đầy đủ field bắt buộc | CB_NV_TW đăng nhập. CTĐT "CTDT-TW-2026-001" trạng thái DA_DUYET tồn tại. | ten_ke_hoach="KH ĐT năm 2026 — DN nhỏ và vừa", ctdt_id="CTDT-TW-2026-001", thoi_gian_bat_dau="2026-06-01", thoi_gian_ket_thuc="2026-12-31", ngan_sach_du_kien=500000000, nguon_luc="20 GV TW + 5 phòng học", ghi_chu="" | 1. Click [+ Lập KH năm]. 2. Điền đủ field. 3. Click [Lưu nháp]. | **STATE**: INSERT KE_HOACH_DAO_TAO với `ma_kh` auto-gen (per BR-DATA-04 format `KH-{YYYYMMDD}-{SEQ}` — 02-thu-tu-module dòng 588), `trang_thai='NHAP'` (FR-III-14 Processing step 4), `don_vi_id=cb_nv_tw_01.don_vi_id`, `created_by=cb_nv_tw_01`, `created_at=NOW()` (BR-DATA-03 7 common fields). AUDIT_LOG: hanh_dong='CREATE', entity='KE_HOACH_DAO_TAO' (BR-DATA-05). **UI**: Toast "Lập kế hoạch thành công" (SRS Gap nguyên văn — SPEC-CLARIFY-DT-03). Form đóng, navigate về danh sách. **PERSIST**: Record mới hiển thị badge "Nháp"; reload → tồn tại. | Happy 🔴 |
| TC-KH-NAM-N-007 | ERR-KH-01 | Lập KH năm — tên kế hoạch trống | CB_NV_TW đăng nhập. | ten_ke_hoach="" | 1. Form lập KH. 2. Bỏ trống Tên KH. 3. Điền field còn lại. 4. Click [Lưu]. | **STATE**: KHÔNG INSERT. Count KE_HOACH_DAO_TAO trước/sau bằng nhau. **UI**: Inline error "**Tên kế hoạch là bắt buộc**" (FR-III-14 ERR-KH-01 nguyên văn). Focus về field. **PERSIST**: Reload → record không tồn tại. | Negative 🔴 |
| TC-KH-NAM-N-008 | FR-III-14 / Inputs row 4 | Lập KH năm — thoi_gian_ket_thuc ≤ thoi_gian_bat_dau | CB_NV_TW đăng nhập. | thoi_gian_bat_dau="2026-06-01", thoi_gian_ket_thuc="2026-05-30" | 1. Form lập. 2. Nhập KT < BĐ. 3. Lưu. | **STATE**: KHÔNG INSERT. **UI**: Inline error "Thời gian kết thúc phải sau thời gian bắt đầu" (analog ERR-CTDT-02 — SPEC-CLARIFY-DT-04 cho ERR-KH thiếu code dedicated). **PERSIST**: Count không đổi. | Negative 🔴 |
| TC-KH-NAM-N-009 | FR-III-14 / Inputs row 2 | Lập KH năm — ctdt_id không tồn tại (FK fail) | CB_NV_TW. | ctdt_id="CTDT-INVALID-999" | 1. API direct POST với ctdt_id sai. | **STATE**: KHÔNG INSERT. BE FK check fail → 400/422. **UI**: HTTP error / toast "CTĐT không tồn tại". **PERSIST**: Count không đổi. | Negative |
| TC-KH-NAM-B-010 | FR-III-14 / Boundary | Lập KH năm — ngan_sach_du_kien = 0 (boundary) | CB_NV_TW. | ngan_sach_du_kien=0 | 1. Lập KH với ngân sách=0. 2. Lưu. | **STATE**: INSERT thành công (constraint ≥0 cho phép =0). **UI**: Toast OK. **PERSIST**: Detail hiển thị 0. | Boundary 🟡 |
| TC-KH-NAM-B-011 | FR-III-14 / Boundary | Lập KH năm — ngan_sach_du_kien âm (-1) | CB_NV_TW. | ngan_sach_du_kien=-1 | 1. API direct POST với ngân sách=-1. | **STATE**: KHÔNG INSERT. BE check ≥0 fail. **UI**: Inline/HTTP error "Ngân sách phải ≥ 0". **PERSIST**: Count không đổi. | Negative 🟡 |

---

## D. UPDATE (Sửa KH năm — chỉ NHAP)

| ID | TraceID (Mã SRS) | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|-------------------|--------------|----------------|-----------|-------------------|------------------|------|
| TC-KH-NAM-H-012 | FR-III-14 / BR-DATA-05 | Sửa KH năm trạng thái NHAP — đổi ngân sách | CB_NV_TW. KH "KH-20260509-001" trạng thái NHAP, do cb_nv_tw_01 tạo. | ngan_sach_du_kien_moi=600000000 | 1. Click [Sửa] trên row KH. 2. Đổi ngân sách. 3. Lưu. | **STATE**: UPDATE KE_HOACH_DAO_TAO SET ngan_sach_du_kien=600000000, updated_at=NOW(), updated_by=cb_nv_tw_01. AUDIT_LOG: hanh_dong='UPDATE' với du_lieu_cu={ngan_sach:500000000}, du_lieu_moi={ngan_sach:600000000}. **UI**: Toast OK. Form đóng. **PERSIST**: Detail reflect 600M. | Happy |
| TC-KH-NAM-N-013 | ERR-KH-02 / BR-FLOW-03 | Sửa KH năm trạng thái DA_DUYET — bị chặn | CB_NV_TW. KH "KH-20260509-002" trạng thái DA_DUYET. | ngan_sach mới | 1. Click [Sửa] trên row DA_DUYET. | **STATE**: KHÔNG UPDATE. **UI**: Nút [Sửa] ẨN/disable per BR-FLOW-03. Nếu force API PUT → BE reject với "**Không thể sửa KH đã duyệt**" (ERR-KH-02 nguyên văn FR-III-14). **PERSIST**: Record không đổi. | Negative 🔴 |
| TC-KH-NAM-N-014 | FR-III-14 / BR-AUTH-08 | CB_NV_BN cố sửa KH thuộc cấp TW → 403 | CB_NV_BN đăng nhập. KH "KH-TW-001" thuộc TW. | API PUT /api/v1/ke-hoach-dao-tao/{id} | 1. CB_NV_BN call API PUT. | **STATE**: KHÔNG UPDATE. BE check don_vi_id mismatch → 403. **UI**: HTTP 403 hoặc toast "Không có quyền". **PERSIST**: Record không đổi. | Negative |

---

## E. DELETE (Xóa mềm KH năm — chỉ NHAP)

| ID | TraceID (Mã SRS) | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|-------------------|--------------|----------------|-----------|-------------------|------------------|------|
| TC-KH-NAM-H-015 | FR-III-14 / BR-DATA-01 | Xóa mềm KH năm trạng thái NHAP thành công | CB_NV_TW. KH "KH-20260509-003" NHAP, do cb_nv_tw_01 tạo. | — | 1. Click [Xóa] trên row. 2. Confirm dialog. | **STATE**: UPDATE SET is_deleted=1, deleted_at=NOW(), deleted_by=cb_nv_tw_01 (BR-DATA-01). AUDIT_LOG: hanh_dong='DELETE'. **UI**: Toast "Xóa kế hoạch thành công" (SPEC-CLARIFY-DT-03). Record biến mất khỏi list. **PERSIST**: Reload list → record ẩn. | Happy |
| TC-KH-NAM-N-016 | FR-III-14 / BR-FLOW-03 | Xóa KH năm trạng thái CHO_DUYET — bị chặn | CB_NV_TW. KH "KH-20260509-004" CHO_DUYET. | — | 1. Click [Xóa]. | **STATE**: KHÔNG UPDATE is_deleted. **UI**: Nút [Xóa] ẨN/disable. Force API DELETE → BE reject "Không thể xóa KH đã trình duyệt" (SPEC-CLARIFY-DT-05 — SRS chỉ có ERR-KH-02 cho UPDATE, gap cho DELETE). **PERSIST**: Record vẫn tồn tại NHAP. | Negative 🟡 |

---

## F. STATE TRANSITIONS (NHAP → CHO_DUYET → DA_DUYET / TU_CHOI → DA_CONG_KHAI)

| ID | TraceID (Mã SRS) | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|-------------------|--------------|----------------|-----------|-------------------|------------------|------|
| TC-KH-NAM-S-017 | FR-III-14 AC2 / SM-KHOAHOC | Trình duyệt KH năm: NHAP → CHO_DUYET (AT-01 manual trigger) | CB_NV_TW. KH "KH-T1" NHAP đầy đủ field. | — | 1. Row KH-T1 → click [Trình duyệt]. 2. Confirm dialog. | **STATE**: UPDATE SET trang_thai='CHO_DUYET', updated_at=NOW(). AUDIT_LOG: hanh_dong='SUBMIT'. Notification (BR-NOTIF-01) gửi cb_pd_tw_01 (CB PD cùng cấp). **UI**: Toast "Đã gửi phê duyệt". Badge đổi từ "Nháp" → "Chờ duyệt". **PERSIST**: Reload → CHO_DUYET. | Happy 🔴 |
| TC-KH-NAM-S-018 | FR-III-15 AC1 / BR-AUTH-05 / SM-KHOAHOC | Phê duyệt KH năm: CHO_DUYET → DA_DUYET (CB PD cùng cấp) | cb_pd_tw_01 đăng nhập. KH "KH-T1" CHO_DUYET (do cb_nv_tw_01 trình). | quyet_dinh="PHE_DUYET" | 1. CB_PD_TW vào danh sách Chờ duyệt. 2. Row KH-T1 → click [Duyệt]. 3. Confirm. | **STATE**: UPDATE SET trang_thai='DA_DUYET', nguoi_duyet_id=cb_pd_tw_01. AUDIT_LOG: hanh_dong='APPROVE'. Notification gửi cb_nv_tw_01 (BR-NOTIF-01). **UI**: Toast "Phê duyệt thành công". Badge → "Đã duyệt". **PERSIST**: Reload → DA_DUYET. | Happy 🔴 |
| TC-KH-NAM-S-019 | FR-III-15 AC2 / BR-FLOW-04 / SM-KHOAHOC | Từ chối KH năm: CHO_DUYET → TU_CHOI (with ly_do ≥10 ký) | cb_pd_tw_01. KH "KH-T2" CHO_DUYET. | quyet_dinh="TU_CHOI", ly_do="Ngân sách vượt mức cho phép, cần điều chỉnh giảm 30%" | 1. Row KH-T2 → click [Từ chối]. 2. Modal nhập lý do. 3. Confirm. | **STATE**: UPDATE SET trang_thai='TU_CHOI', ly_do_tu_choi=<text>, nguoi_duyet_id=cb_pd_tw_01. AUDIT_LOG: hanh_dong='REJECT'. Notification gửi cb_nv_tw_01. **UI**: Toast "Đã từ chối". Badge → "Từ chối". Hiển thị lý do trong detail. **PERSIST**: TU_CHOI. SM-KHOAHOC cho phép TU_CHOI → CHO_DUYET (resubmit). | Happy 🔴 |
| TC-KH-NAM-N-020 | FR-III-15 / BR-FLOW-04 / SPEC-CLARIFY-DT-A6-01 | Từ chối KH năm — lý do trống / <10 ký tự | cb_pd_tw_01. KH CHO_DUYET. | ly_do="" hoặc ly_do="Ngắn" (5 ký) | 1. Click [Từ chối]. 2. Bỏ trống/nhập ngắn. 3. Confirm. | **STATE**: KHÔNG UPDATE. **UI**: Inline error "Lý do từ chối là bắt buộc và tối thiểu 10 ký tự" (BR-FLOW-04). **PERSIST**: Record vẫn CHO_DUYET. | Negative 🔴 |
| TC-KH-NAM-N-021 | FR-III-15 / BR-AUTH-05 | Phê duyệt KH năm — CB PD khác cấp (CB_PD_BN duyệt KH cấp TW) | cb_pd_bn_01 đăng nhập. KH "KH-T3" CHO_DUYET cấp TW. | quyet_dinh="PHE_DUYET" | 1. CB_PD_BN cố API PUT approve KH cấp TW. | **STATE**: KHÔNG UPDATE. BE check `nguoi_duyet.don_vi_id == ke_hoach.don_vi_id` fail. **UI**: HTTP 403 / toast "Phê duyệt phải cùng cấp" (BR-AUTH-05 vi phạm). UI: nút [Duyệt] không hiển thị cho CB_PD_BN trên KH cấp TW. **PERSIST**: Record vẫn CHO_DUYET. | Negative 🔴 |
| TC-KH-NAM-N-022 | FR-III-15 / ERR-DKDT-01 | Phê duyệt KH năm khi đã ở trạng thái CHO_DUYET → reject ERR-DKDT-01 | cb_pd_tw_01 đăng nhập. KH-NAM-2026-001 ở trạng thái CHO_DUYET (đang chờ). | Click [Phê duyệt] 2 lần liên tiếp (idempotency). | 1. CB PD đăng nhập. 2. SCR-III-01 Tab "KH năm". 3. Click row CHO_DUYET → click [Phê duyệt]. 4. Repeat click [Phê duyệt] lần 2 trước khi UI refresh. | **STATE**: Lần 1 INSERT phê duyệt → state DA_DUYET. Lần 2: BE detect duplicate, return error. KHÔNG INSERT bản ghi 2. **UI**: Lần 2 hiện toast/error "ERR-DKDT-01 — Kế hoạch đã ở trạng thái chờ duyệt hoặc đã duyệt" (SRS Gap nguyên văn — SPEC-CLARIFY-DT-A6-03). **PERSIST**: Reload → trạng thái DA_DUYET, audit log 1 row. | Negative 🟡 |
| TC-KH-NAM-N-023 | FR-III-15 / ERR-KH-03 | Trình duyệt KH năm khi đã CHO_DUYET (idempotency block) | cb_nv_tw_01. KH-NAM-2026-002 ở CHO_DUYET. | API direct POST `/api/v1/ke-hoach-dao-tao/{id}/submit` với token CB NV. | 1. POST submit lần 2 cho KH đã CHO_DUYET. | **STATE**: KHÔNG đổi state. **UI**: HTTP 409 Conflict + body `{code: "ERR-KH-03", message: "KH đã ở trạng thái chờ duyệt"}`. **PERSIST**: state vẫn CHO_DUYET. | Negative 🟡 |
| TC-KH-NAM-S-022 | FR-III-16 AC1 / BR-FLOW-05 / SM-KHOAHOC | Công khai KH năm: DA_DUYET → DA_CONG_KHAI (gọi API Cổng PLQG) | cb_nv_tw_01. KH "KH-T1" DA_DUYET. Mock API outbound `POST /portal/ke-hoach`. | hanh_dong="CONG_KHAI" | 1. Row KH-T1 → click [Công khai]. 2. Confirm. | **STATE**: Backend gọi outbound `POST <portal_plqg>/api/ke-hoach` (BR-FLOW-05). Nếu API 200 → UPDATE SET trang_thai='DA_CONG_KHAI', api_response_log=<json>. AUDIT_LOG: hanh_dong='PUBLISH'. **UI**: Toast "Công khai thành công". Badge → "Đã công khai". **PERSIST**: Reload → DA_CONG_KHAI. Verify Cổng PLQG receive (mock). | Happy 🔴 |
| TC-KH-NAM-S-023 | FR-III-16 AC2 / SM-KHOAHOC | Hủy công khai KH năm: DA_CONG_KHAI → DA_DUYET | cb_nv_tw_01. KH "KH-T1" DA_CONG_KHAI. | hanh_dong="HUY_CONG_KHAI" | 1. Row KH-T1 → [Hủy công khai]. 2. Confirm. | **STATE**: Outbound `DELETE <portal_plqg>/api/ke-hoach/{id}`. UPDATE SET trang_thai='DA_DUYET'. AUDIT_LOG: hanh_dong='UNPUBLISH'. **UI**: Toast "Đã gỡ công khai". Badge → "Đã duyệt". **PERSIST**: DA_DUYET. | Happy |
| TC-KH-NAM-S-024 | FR-III-16 / SM-KHOAHOC invalid | Công khai KH năm trạng thái NHAP/CHO_DUYET — bị chặn | cb_nv_tw_01. KH "KH-T4" NHAP. | hanh_dong="CONG_KHAI" | 1. Force API call publish trên NHAP. | **STATE**: KHÔNG UPDATE, KHÔNG gọi outbound. BE check trang_thai NOT IN (DA_DUYET, DA_CONG_KHAI) → reject. **UI**: Nút [Công khai] không hiển thị trên NHAP. Force API → 422 "Trạng thái không cho phép công khai". **PERSIST**: Record vẫn NHAP. | Negative 🔴 |
| TC-KH-NAM-S-025 | FR-III-16 / BR-FLOW-05 / Edge | Công khai KH — outbound API Cổng PLQG fail (5xx) | cb_nv_tw_01. KH DA_DUYET. Mock outbound trả 503. | hanh_dong="CONG_KHAI" | 1. Click [Công khai]. | **STATE**: Outbound 503 → KHÔNG UPDATE trang_thai. AUDIT_LOG: hanh_dong='PUBLISH_FAIL', api_response_log=<error>. **UI**: Toast "Lỗi kết nối Cổng PLQG, vui lòng thử lại" (SPEC-CLARIFY-DT-06 nguyên văn). **PERSIST**: Record vẫn DA_DUYET. Có thể retry. | Edge 🟡 |

---

## G. PERMISSION (high-level — chi tiết ở 13-TC-permission-matrix.md)

| ID | TraceID (Mã SRS) | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|-------------------|--------------|----------------|-----------|-------------------|------------------|------|
| TC-KH-NAM-P-026 | Permission Matrix / DN | DN không thấy menu KH năm trong sidebar (chỉ public_view qua Cổng PLQG) | DN (dn_01) đăng nhập app HTPLDN. | URL `/dao-tao/ke-hoach-nam` | 1. Đăng nhập DN. 2. Quan sát sidebar. 3. Force URL. | **STATE**: BE 403 nếu DN call API quản lý. **UI**: Sidebar KHÔNG có menu "KH năm". Force URL → "Không có quyền" hoặc redirect dashboard. DN chỉ truy cập KH DA_CONG_KHAI qua chuyên trang Cổng PLQG (không qua app HTPLDN). **PERSIST**: Reload vẫn bị chặn. | Negative |

---

## H. NEGATIVE / EDGE

| ID | TraceID (Mã SRS) | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|-------------------|--------------|----------------|-----------|-------------------|------------------|------|
| TC-KH-NAM-E-027 | FR-III-14 / BR-DATA-05 / Audit Trail | Verify AUDIT_LOG ghi đầy đủ chuỗi CRUD + state transition (qua FR-10 W1.1 UI) | CB_NV_TW + CB_PD_TW. FR-10 W1.1 Nhật ký HT screen sẵn dùng. | Sequence: tạo → trình → duyệt → công khai 1 KH | 1. cb_nv_tw_01 lập KH "KH-AUDIT-01". 2. Trình duyệt. 3. cb_pd_tw_01 duyệt. 4. cb_nv_tw_01 công khai. 5. qtht_01 mở FR-10 W1.1 Nhật ký HT, filter entity_id=KH-AUDIT-01. | **STATE**: Backend ghi 4 row AUDIT_LOG. **UI**: FR-10 W1.1 Nhật ký HT lookup theo entity_id → bảng hiển thị 4 entries: (1) CREATE bởi cb_nv_tw_01; (2) SUBMIT (NHAP→CHO_DUYET); (3) APPROVE bởi cb_pd_tw_01 (CHO_DUYET→DA_DUYET); (4) PUBLISH (DA_DUYET→DA_CONG_KHAI). Mỗi row hiển thị actor, thoi_gian, du_lieu_cu/du_lieu_moi (BR-DATA-05). **PERSIST**: Reload screen FR-10 → vẫn 4 entries; cố sửa/xóa entry → KHÔNG có nút edit/delete (immutable). | Edge 🔴 |

---

## I. EDGE CASES (A4 added)

| ID | TraceID (Mã SRS) | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|-------------------|--------------|----------------|-----------|-------------------|------------------|------|
| TC-KH-NAM-E-028 | FR-III-16 / BR-FLOW-05 / Idempotency | Click [Công khai] 2 lần liên tiếp (double-click race) — chỉ 1 outbound call thực thi | cb_nv_tw_01. KH "KH-IDEMPO-001" DA_DUYET. Mock outbound `POST /portal/ke-hoach` log số lần gọi. | Double-click button [Công khai] trong <500ms | 1. Click [Công khai] nhanh 2 lần. 2. Quan sát mock outbound log. 3. Query DB. | **STATE**: Outbound CHỈ 1 lần (BE phải debounce / lock theo `ma_kh` hoặc check trang_thai='DA_DUYET' atomic). UPDATE chỉ 1 lần. AUDIT_LOG `PUBLISH` chỉ 1 entry. **UI**: Toast "Công khai thành công" (1 lần). Lần 2 → button disabled hoặc no-op. **PERSIST**: DA_CONG_KHAI. SPEC-CLARIFY-DT-DC-01 nếu app cho 2 outbound call. | Edge 🔴 |
| TC-KH-NAM-E-029 | FR-III-14 / BR-EC-01 / Concurrency phê duyệt | 2 CB_PD_TW cùng duyệt 1 KH năm CHO_DUYET | cb_pd_tw_01 + cb_pd_tw_02. KH "KH-DUYET-CONFLICT" CHO_DUYET. | Cả 2 mở form approve cùng updated_at=T1 | 1. CB_PD_TW_01 click [Duyệt] T2. 2. CB_PD_TW_02 click [Duyệt] T3. | **STATE**: PD-01 INSERT OK → DA_DUYET, nguoi_duyet=cb_pd_tw_01. PD-02 BE check `WHERE updated_at=T1 AND trang_thai='CHO_DUYET'` → 0 row → reject với ERR-SYS-02 (BR-EC-01 optimistic lock). **UI**: PD-01 toast OK. PD-02 toast "Bản ghi đã được duyệt bởi người khác". **PERSIST**: AUDIT_LOG chỉ 1 APPROVE entry. nguoi_duyet_id=cb_pd_tw_01. | Edge 🔴 |
| TC-KH-NAM-B-030 | FR-III-14 / Boundary tên KH năm | Tên KH năm = 500 ký tự (boundary max) và 501 ký (over) | CB_NV_TW. | ten="A"×500 (PASS); ten="A"×501 (FAIL) | 2 lần test boundary. | **STATE**: 500 ký INSERT OK; 501 ký reject (per UI A field "max 500"). **UI**: 500 ký toast OK. 501 ký inline error "Tên KH tối đa 500 ký tự" (SPEC-CLARIFY-DT-DC-02 nguyên văn). **PERSIST**: Count chỉ +1. | Boundary 🟡 |

---

## SPEC-CLARIFY tickets (file này)

| ID | Mô tả |
|----|-------|
| SPEC-CLARIFY-DT-02 | Pagination URL sync? Reload page 2 có giữ trạng thái page=2 hay reset về page=1? |
| SPEC-CLARIFY-DT-DC-01 | Idempotency outbound API Cổng PLQG — debounce/lock theo `ma_kh` hay client-side disable? Tránh double publish khi double-click. |
| SPEC-CLARIFY-DT-DC-02 | Nguyên văn message overflow tên KH năm 500 ký — SRS không quote, cần BA confirm. |
| SPEC-CLARIFY-DT-03 | Toast message thành công CREATE/UPDATE/DELETE KH năm — chưa có nguyên văn trong SRS FR-III-14. |
| SPEC-CLARIFY-DT-04 | ERR-KH dedicated cho `thoi_gian_ket_thuc ≤ thoi_gian_bat_dau` — SRS chỉ có ERR-CTDT-02 analog, gap cho KH năm. |
| SPEC-CLARIFY-DT-05 | Xóa KH năm trạng thái CHO_DUYET/DA_DUYET — SRS gap (chỉ có ERR-KH-02 cho UPDATE). Mặc định BR-FLOW-03 chặn? |
| SPEC-CLARIFY-DT-06 | Outbound API Cổng PLQG fail — message nguyên văn + retry policy chưa có trong FR-III-16. |
| SPEC-CLARIFY-DT-A6-01 | Phê duyệt KH cần error code chính thức từ BA — hiện tại trace via BR-FLOW-04 (TC-KH-NAM-N-020). |
| SPEC-CLARIFY-DT-A6-03 | ERR-DKDT-01 nguyên văn message khi phê duyệt idempotent (TC-KH-NAM-N-022) — SRS Gap. |

---

## Tổng kết file 01

- **32 TC active sau A8 Codex** (8H + 9N + 2B + 5S + 1P + 1E + 3 edge A4 + 2 P1 codex new) phủ FR-III-14/15/16.
- **7 SPEC-CLARIFY** raise pending BA: DT-02, DT-03, DT-04, DT-05, DT-06, DT-A6-01, DT-A6-03.
- **BR coverage:** BR-AUTH-08, BR-AUTH-05, BR-DATA-01/03/05/07, BR-FLOW-03/04/05, BR-NOTIF-01.
- **ERR coverage:** ERR-KH-01, ERR-KH-02, ERR-PD-01, ERR-PD-02.
- **SM coverage:** NHAP → CHO_DUYET → DA_DUYET → DA_CONG_KHAI; TU_CHOI; invalid transitions.

---

## A7 Filter Notes

- **SỬA:** TC-KH-NAM-E-027 — chuyển từ "Query AUDIT_LOG DB" sang "FR-10 W1.1 Nhật ký HT UI lookup". Phụ thuộc FR-10 W1.1 ready.
- **KEEP all others:** Mọi TC khác observable qua UI + network panel (toast, badge, Cổng PLQG mock, network call log).
