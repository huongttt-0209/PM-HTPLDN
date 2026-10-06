# Test Cases — UC32: Đề xuất đào tạo từ DN/NHT (FR-III-13)

> **SRS Ref**: FR-III-13 (UC32 Đề xuất đào tạo). Entity: DE_XUAT_DAO_TAO. Workflow: DN/NHT (qua chuyên trang Cổng PLQG) tạo đề xuất `MOI` → CB NV cấp tương ứng tiếp nhận `DA_TIEP_NHAN` → CB NV ghép vào KH năm `DA_THUC_HIEN`.
> **Nguồn**: SRS local `srs-fr-03-dao-tao.md` dòng 868-892 + `02-thu-tu-module.md` §⑨ + Plan overview §2.
> **Ngày tạo**: 2026-05-09 (Phase A re-run)
> **Phạm vi tài khoản**: dn_01 (DN tạo đề xuất), nht_01 (NHT tạo đề xuất), cb_nv_tw_01 (tiếp nhận + ghép KH), cb_nv_bn_01 (cross-cấp).

---

## A. UI FIELD VERIFICATION (BẮT BUỘC chạy trước functional)

| ID | TraceID (Mã SRS) | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|-------------------|--------------|----------------|-----------|-------------------|------------------|------|
| TC-DEXUAT-H-001 | FR-III-13 / SCR-III-01 / UI Tab "Đề xuất" | Verify SCR-III-01 Tab "Đề xuất" — danh sách trên view CB NV | CB_NV_TW (cb_nv_tw_01) đăng nhập app HTPLDN. Seed 3 đề xuất MOI + 1 DA_TIEP_NHAN + 1 DA_THUC_HIEN. | URL: `/dao-tao/chuong-trinh` Tab "Đề xuất" | 1. Đăng nhập CB_NV_TW. 2. Vào "Đào tạo > Chương trình đào tạo". 3. Click tab "Đề xuất". | **STATE**: Backend `GET /api/v1/de-xuat-dao-tao?...`. **UI**: Tab "Đề xuất" active. Filter-bar: Lĩnh vực (select FK), Trạng thái (dropdown 3 giá trị MOI/DA_TIEP_NHAN/DA_THUC_HIEN), Loại nguồn (DN/NHT), Từ ngày, Đến ngày. Bảng cột: ID, Nguồn (DN/NHT badge), Tên DN/NHT, Lĩnh vực, Nội dung (truncate), Số lượng dự kiến, Ngày tạo, Trạng thái (badge), Hành động (Tiếp nhận/Ghép KH/Xem). Pagination 20/page. **PERSIST**: Reload giữ tab. | Happy 🔴 |
| TC-DEXUAT-H-002 | FR-III-13 / Cổng PLQG / UI Form (DN/NHT side) | Verify Form "Gửi đề xuất đào tạo" trên chuyên trang DN/NHT (Cổng PLQG) | DN (dn_01) đăng nhập chuyên trang DN qua Cổng PLQG. | URL chuyên trang DN `/dn-portal/de-xuat-dao-tao` | 1. DN vào trang "Đề xuất đào tạo". 2. Click [+ Gửi đề xuất]. | **STATE**: — (form open). **UI**: Form 5 field per FR-III-13 Inputs: Lĩnh vực * (select FK DANH_MUC LINH_VUC_PL), Nội dung * (textarea max 5000), Thời gian mong muốn (text), Địa điểm mong muốn (text), Số lượng dự kiến (number ≥1). Action-bar [Hủy] [Gửi đề xuất]. **PERSIST**: [Hủy] → form đóng. | Happy 🔴 |

---

## B. READ / LIST (Filter trang_thai IN MOI/DA_TIEP_NHAN/DA_THUC_HIEN)

| ID | TraceID (Mã SRS) | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|-------------------|--------------|----------------|-----------|-------------------|------------------|------|
| TC-DEXUAT-H-003 | FR-III-13 / BR-AUTH-08 | CB_NV_TW thấy đề xuất gửi tới đơn vị TW (DN/NHT chọn cấp tương ứng) | CB_NV_TW đăng nhập. Seed: 2 đề xuất gửi TW (DN_01, NHT_01) + 1 gửi BN. | — | 1. Vào tab "Đề xuất". | **STATE**: Backend `WHERE don_vi_id_dich = cb_nv_tw_01.don_vi_id` (BR-AUTH-08). **UI**: Hiển thị 2 đề xuất TW. KHÔNG thấy đề xuất gửi BN. **PERSIST**: Reload giữ scope. | Happy |
| TC-DEXUAT-H-004 | FR-III-13 / Filter trang_thai | Filter dropdown Trạng thái = MOI → chỉ hiển thị MOI | CB_NV_TW. Seed 3 MOI + 2 DA_TIEP_NHAN + 1 DA_THUC_HIEN. | trang_thai="MOI" | 1. Filter Trạng thái = MOI. 2. Tìm. | **STATE**: Backend `WHERE trang_thai='MOI'` (FR-III-13 Outputs row 4 enum). **UI**: 3 record MOI. Badge xám "Mới". KHÔNG hiển thị 3 record khác. **PERSIST**: Reload giữ filter. | Happy 🔴 |
| TC-DEXUAT-H-005 | FR-III-13 / Output truncate | Cột Nội dung hiển thị truncate (...) khi > N ký tự | CB_NV_TW. Đề xuất "DX-001" có nội dung 2000 ký tự. | — | 1. Vào tab Đề xuất. 2. Quan sát cột Nội dung. | **STATE**: — **UI**: Nội dung truncate ~100 ký tự + "..." (FR-III-13 Outputs row 3 "noi_dung (truncate)"). Click row → mở detail hiển thị full text. **PERSIST**: Reload giữ. | Happy |

---

## C. CREATE (DN/NHT submit qua Cổng PLQG)

| ID | TraceID (Mã SRS) | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|-------------------|--------------|----------------|-----------|-------------------|------------------|------|
| TC-DEXUAT-H-006 | FR-III-13 / BR-DATA-03 / BR-NOTIF-01 | DN tạo đề xuất đào tạo thành công — trạng thái MOI + thông báo CB NV | DN (dn_01) đăng nhập chuyên trang DN. Lĩnh vực DAN_SU tồn tại trong FR-10 DM. | linh_vuc_id=DAN_SU, noi_dung="Đề xuất đào tạo Pháp luật DN cho 50 nhân viên công ty ABC, tập trung Luật Doanh nghiệp 2020 và Luật Lao động 2019", thoi_gian_mong_muon="Quý 3/2026", dia_diem_mong_muon="Hà Nội", so_luong_du_kien=50 | 1. Form "Gửi đề xuất". 2. Điền đủ field. 3. [Gửi đề xuất]. | **STATE**: INSERT DE_XUAT_DAO_TAO với `trang_thai='MOI'`, `nguon='DN'`, `nguon_id=dn_01.id`, `don_vi_id_dich=<đơn vị quản lý DN, default TW>`, 7 common fields BR-DATA-03 (created_at, created_by=dn_01...). AUDIT_LOG: hanh_dong='CREATE', entity='DE_XUAT_DAO_TAO' (BR-DATA-05). Notification BR-NOTIF-01 gửi cb_nv_tw_01 (email + in-app). **UI**: Toast "Đề xuất đào tạo đã được gửi" (SPEC-CLARIFY-DT-12 nguyên văn). Form đóng. Quay về list đề xuất của DN với badge "Mới". **PERSIST**: Reload list DN → record tồn tại. CB NV side reload → record xuất hiện trong tab "Đề xuất". | Happy 🔴 |
| TC-DEXUAT-H-007 | FR-III-13 / NHT source | NHT tạo đề xuất đào tạo thành công — verify nguồn=NHT | NHT (nht_01) đăng nhập chuyên trang NHT. | Tương tự TC-006 với nguon=NHT | 1. NHT submit form. | **STATE**: INSERT với `nguon='NHT'`, `nguon_id=nht_01.id`. Notification gửi CB NV cấp tương ứng. **UI**: Badge nguồn "NHT" (xanh lá) trên list CB NV. **PERSIST**: Filter Loại nguồn=NHT → record xuất hiện. | Happy 🔴 |
| TC-DEXUAT-N-008 | ERR-DX-01 | DN tạo đề xuất — nội dung trống | DN dn_01. | noi_dung="" | 1. Form gửi đề xuất. 2. Bỏ trống Nội dung. 3. Điền field còn lại. 4. [Gửi]. | **STATE**: KHÔNG INSERT. **UI**: Inline error "**Nội dung đề xuất là bắt buộc**" (FR-III-13 ERR-DX-01 nguyên văn). **PERSIST**: Count không đổi. | Negative 🔴 |
| TC-DEXUAT-N-009 | FR-III-13 / Inputs row 1 | DN tạo đề xuất — linh_vuc_id không tồn tại | DN. | linh_vuc_id="DAN_INVALID" | 1. API direct POST. | **STATE**: KHÔNG INSERT. BE FK fail → 400. **UI**: HTTP error / toast "Lĩnh vực không tồn tại". **PERSIST**: Count không đổi. | Negative |

---

## D. RECEIVE (CB NV tiếp nhận MOI → DA_TIEP_NHAN)

| ID | TraceID (Mã SRS) | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|-------------------|--------------|----------------|-----------|-------------------|------------------|------|
| TC-DEXUAT-H-010 | FR-III-13 / SM transition / BR-DATA-05 | CB_NV_TW tiếp nhận đề xuất MOI → DA_TIEP_NHAN | cb_nv_tw_01. Đề xuất "DX-MOI-001" trạng thái MOI. | — | 1. Tab "Đề xuất". 2. Row DX-MOI-001 → click [Tiếp nhận]. 3. Confirm dialog. | **STATE**: UPDATE DE_XUAT_DAO_TAO SET trang_thai='DA_TIEP_NHAN', nguoi_tiep_nhan_id=cb_nv_tw_01, ngay_tiep_nhan=NOW(), updated_at=NOW(). AUDIT_LOG: hanh_dong='RECEIVE'. Notification BR-NOTIF-01 gửi DN/NHT (email "Đề xuất đã được tiếp nhận" — SPEC-CLARIFY-DT-13). **UI**: Toast "Tiếp nhận thành công". Badge MOI → "Đã tiếp nhận" (xanh dương). Cột Hành động bỏ [Tiếp nhận], hiện [Ghép vào KH]. **PERSIST**: Reload → DA_TIEP_NHAN. | Happy 🔴 |
| TC-DEXUAT-N-011 | ERR-DX-02 / FR-III-13 | DN cố sửa đề xuất đã tiếp nhận — bị chặn | dn_01. Đề xuất "DX-001" do DN gửi, trạng thái DA_TIEP_NHAN. | API PUT update noi_dung | 1. DN cố API PUT đề xuất DA_TIEP_NHAN. | **STATE**: KHÔNG UPDATE. BE check trang_thai NOT IN (MOI) → reject. **UI**: Nút [Sửa] ẨN trên DN list khi state ≠ MOI. Force API → "**Không thể sửa đề xuất đã tiếp nhận**" (FR-III-13 ERR-DX-02 nguyên văn). **PERSIST**: Record không đổi. | Negative 🔴 |
| TC-DEXUAT-N-012 | ERR-DX-03 / FR-III-13 | DN cố xóa đề xuất đã tiếp nhận — bị chặn | dn_01. Đề xuất DX-001 DA_TIEP_NHAN. | API DELETE | 1. DN cố API DELETE. | **STATE**: KHÔNG UPDATE is_deleted. BE check trang_thai NOT IN (MOI) → reject. **UI**: Nút [Xóa] ẨN. Force API → "**Đề xuất đã tiếp nhận không thể xóa**" (FR-III-13 ERR-DX-03 nguyên văn). **PERSIST**: Record vẫn tồn tại DA_TIEP_NHAN. | Negative 🔴 |

---

## E. LINK (Ghép vào KH năm: DA_TIEP_NHAN → DA_THUC_HIEN)

| ID | TraceID (Mã SRS) | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|-------------------|--------------|----------------|-----------|-------------------|------------------|------|
| TC-DEXUAT-H-013 | FR-III-13 / SM transition / Cross-module FR-III-14 | CB NV ghép đề xuất DA_TIEP_NHAN vào KH năm → DA_THUC_HIEN | cb_nv_tw_01. Đề xuất "DX-002" DA_TIEP_NHAN. KH năm "KH-2026-001" trạng thái NHAP/DA_DUYET (cùng lĩnh vực DAN_SU) sẵn. | ke_hoach_id="KH-2026-001" | 1. Tab "Đề xuất". 2. Row DX-002 → click [Ghép vào KH]. 3. Modal chọn KH năm (dropdown filter cùng lĩnh vực). 4. Chọn KH-2026-001. 5. Confirm. | **STATE**: UPDATE DE_XUAT_DAO_TAO SET trang_thai='DA_THUC_HIEN', ke_hoach_id='KH-2026-001'. AUDIT_LOG: hanh_dong='LINK_TO_PLAN'. Notification gửi DN/NHT "Đề xuất đã được đưa vào KH". **UI**: Toast "Ghép vào kế hoạch thành công" (SPEC-CLARIFY-DT-14 nguyên văn). Badge DA_TIEP_NHAN → "Đã thực hiện" (xanh lá). Detail đề xuất hiển thị link tới KH-2026-001. **PERSIST**: Reload → DA_THUC_HIEN. KH năm detail hiển thị "1 đề xuất liên kết". | Happy 🔴 |

---

## F. PERMISSION

| ID | TraceID (Mã SRS) | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|-------------------|--------------|----------------|-----------|-------------------|------------------|------|
| TC-DEXUAT-P-014 | Permission Matrix / Cross-cấp | CB_NV_BN cố tiếp nhận đề xuất gửi cấp TW → bị chặn | cb_nv_bn_01. Đề xuất "DX-TW-001" gửi đơn vị TW (don_vi_id_dich=TW), trạng thái MOI. | — | 1. cb_nv_bn_01 vào tab "Đề xuất". 2. Force API call [Tiếp nhận] trên DX-TW-001. | **STATE**: KHÔNG UPDATE. BE check don_vi_id_dich mismatch → 403 (BR-AUTH-08). **UI**: DX-TW-001 không hiển thị trong list của cb_nv_bn_01 (filtered by scope). Force API → 403 / toast "Không có quyền tiếp nhận đề xuất khác cấp". **PERSIST**: Record vẫn MOI. | Negative 🔴 |

---

## G. EDGE CASES (A4 added)

| ID | TraceID (Mã SRS) | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|-------------------|--------------|----------------|-----------|-------------------|------------------|------|
| TC-DEXUAT-E-015 | FR-III-13 / Idempotency / BR-NOTIF-01 | DN double-click [Gửi đề xuất] (race) — chỉ 1 đề xuất tạo + 1 notification | DN dn_01 đăng nhập Cổng. KH form mở. | Double-click button [Gửi đề xuất] <500ms | 1. Click [Gửi đề xuất] nhanh 2 lần. 2. Quan sát list đề xuất DN. 3. Query DB. | **STATE**: INSERT chỉ 1 record. AUDIT_LOG chỉ 1 CREATE. Notification gửi cb_nv_tw_01 chỉ 1 lần (BE phải debounce hoặc client disable button after first click). **UI**: Toast "Đã gửi" 1 lần. Form đóng. **PERSIST**: List DN +1 record. SPEC-CLARIFY-DT-DC-15 nếu trùng. | Edge 🔴 |
| TC-DEXUAT-E-016 | FR-III-13 / Concurrency receive | 2 CB_NV_TW cùng [Tiếp nhận] 1 đề xuất MOI | cb_nv_tw_01 + cb_nv_tw_02. Đề xuất "DX-RACE" MOI. | Cả 2 click [Tiếp nhận] cùng updated_at=T1 | 1. CB-A click [Tiếp nhận] T2. 2. CB-B click [Tiếp nhận] T3. | **STATE**: CB-A success → DA_TIEP_NHAN, nguoi_tiep_nhan_id=cb_nv_tw_01. CB-B BE check `WHERE updated_at=T1 AND trang_thai='MOI'` → 0 row → reject ERR-SYS-02 (BR-EC-01). **UI**: A toast OK. B toast "Đề xuất đã được tiếp nhận bởi người khác". **PERSIST**: AUDIT_LOG chỉ 1 RECEIVE entry. nguoi_tiep_nhan=cb_nv_tw_01. | Edge 🟡 |
| TC-DEXUAT-E-017 | FR-III-13 / Boundary nội dung | Nội dung đề xuất 5000 ký (boundary max) và 5001 ký (over) | DN dn_01 đăng nhập Cổng. | noi_dung="A"×5000 (PASS); noi_dung="A"×5001 (FAIL) | 2 lần test boundary. | **STATE**: 5000 ký INSERT OK; 5001 ký reject. **UI**: 5001 inline error "Nội dung tối đa 5000 ký tự" (SPEC-CLARIFY-DT-DC-16 nguyên văn). **PERSIST**: Count chỉ +1. | Boundary 🟡 |

---

## SPEC-CLARIFY tickets (file này)

| ID | Mô tả |
|----|-------|
| SPEC-CLARIFY-DT-12 | Toast message thành công CREATE đề xuất (DN/NHT side) — chưa có nguyên văn trong SRS FR-III-13. |
| SPEC-CLARIFY-DT-DC-15 | Idempotency [Gửi đề xuất] — debounce server-side hay client disable. SRS không quote. |
| SPEC-CLARIFY-DT-DC-16 | Nguyên văn message overflow nội dung 5000 ký — SRS không quote. |
| SPEC-CLARIFY-DT-13 | Notification message khi CB NV [Tiếp nhận] gửi DN/NHT — chưa có nguyên văn trong SRS (BR-NOTIF-01 chỉ generic). |
| SPEC-CLARIFY-DT-14 | Modal "Ghép vào KH năm" — filter dropdown KH năm: chỉ KH cùng lĩnh vực + cùng don_vi_id + state nào (NHAP/CHO_DUYET/DA_DUYET)? Cần BA confirm rule filter. |

---

## Tổng kết file 03

- **17 TC active sau A7** (7H + 5N + 1G + 1P + 3 edge A4) phủ FR-III-13.
- **3 SPEC-CLARIFY** raise pending BA: DT-12, DT-13, DT-14.
- **BR coverage:** BR-AUTH-08, BR-DATA-03/05, BR-NOTIF-01.
- **ERR coverage:** ERR-DX-01, ERR-DX-02, ERR-DX-03.
- **SM coverage:** MOI → DA_TIEP_NHAN → DA_THUC_HIEN; invalid (sửa/xóa khi đã tiếp nhận).
- **Cross-module:** TC-013 ghép vào FR-III-14 KH năm; nguồn DN từ FR-07, NHT từ FR-04.

---

## A7 Filter Notes

- **KEEP all 17 TC:** Mọi TC observable qua UI (Tab Đề xuất CB NV side + chuyên trang DN side) + network panel. Concurrency TC-DEXUAT-E-016 thực thi qua 2 tabs/sessions parallel.
