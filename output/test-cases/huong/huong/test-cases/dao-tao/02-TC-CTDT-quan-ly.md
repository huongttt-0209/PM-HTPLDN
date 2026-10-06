# Test Cases — UC20/UC21: Quản lý Chương trình Đào tạo (FR-III-01 + FR-III-02)

> **SRS Ref**: FR-III-01 (UC20 CRUD CTĐT), FR-III-02 (UC21 Search CTĐT). Entity: CHUONG_TRINH_DAO_TAO. Cấu trúc 2 cấp: CTĐT cha → KHOA_HOC con (soft-delete cascade rule, ERR-CTDT-03).
> **Nguồn**: SRS local `srs-fr-03-dao-tao.md` dòng 71-264 + Phụ lục B BR + `02-thu-tu-module.md` §⑨ + Plan overview §2.
> **Ngày tạo**: 2026-05-09 (Phase A re-run)
> **Phạm vi tài khoản**: cb_nv_tw_01 (CRUD scope TW), cb_nv_bn_01/cb_nv_dp_01 (scope mismatch), DN/NHT (public read).

---

## A. UI FIELD VERIFICATION (BẮT BUỘC chạy trước functional)

| ID | TraceID (Mã SRS) | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|-------------------|--------------|----------------|-----------|-------------------|------------------|------|
| TC-CTDT-H-001 | FR-III-01 / SCR-III-01 / UI | Verify SCR-III-01 Danh sách CTĐT — toolbar + filter + table + expandable rows | CB_NV_TW (cb_nv_tw_01) đăng nhập. Seed ≥3 CTĐT TW (1 NHAP + 1 DA_DUYET + 1 DA_CONG_KHAI). Mỗi CTĐT có ≥1 KHOA_HOC con. | URL: `/dao-tao/chuong-trinh` (SCR-III-01) | 1. Đăng nhập CB_NV_TW. 2. Vào menu "Đào tạo > Chương trình đào tạo". 3. Kiểm tra layout. | **STATE**: Backend `GET /api/v1/chuong-trinh-dao-tao?page=1&size=20`. **UI**: Breadcrumb "Đào tạo > Chương trình đào tạo" + toolbar [+ Thêm CTĐT] [Xuất Excel]. Filter-bar 6 ô: Từ khóa (text — tìm theo tên/mã CTĐT), Lĩnh vực PL (select FK DANH_MUC LINH_VUC_PL), Hình thức (TRUC_TUYEN/TRUC_TIEP), Từ ngày, Đến ngày, Trạng thái (dropdown 4 state CTĐT). Bảng cột: Mã CTĐT, Tên chương trình, Lĩnh vực, Hình thức, Ngày BĐ→KT, Số khóa học (số), Trạng thái (badge), Hành động (Xem/Sửa/Xóa icon). **EXPANDABLE ROW**: Click icon ▶ trên row → expand hiển thị danh sách KHOA_HOC con (mã, tên, ngày BĐ/KT, trạng thái SM-KHOAHOC). Pagination 20/page (BR-DATA-07). **PERSIST**: Reload giữ filter + page. | Happy 🔴 |
| TC-CTDT-H-002 | FR-III-01 / SCR-III-01 / UI Form | Verify Form Thêm CTĐT — đầy đủ 8 field input | CB_NV_TW đăng nhập. Lĩnh vực PL "DAN_SU" tồn tại. | — | 1. Click [+ Thêm CTĐT]. 2. Kiểm tra form. | **STATE**: — (form open). **UI**: Drawer/modal title "Thêm chương trình đào tạo". 8 field per FR-III-01 Inputs: Mã CTĐT (readonly auto-gen, chỉ hiện edit), Tên chương trình * (text không rỗng), Mô tả (textarea), Lĩnh vực * (searchable select FK), Ngân sách dự kiến (money ≥0), Số lượng khóa (number ≥0), Mục tiêu (textarea), File đính kèm (multi-upload). Action-bar [Hủy] [Lưu]. **PERSIST**: [Hủy] → form đóng, không INSERT. | Happy 🔴 |

---

## B. READ / LIST (BR-AUTH-08 scope, pagination, expandable rows)

| ID | TraceID (Mã SRS) | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|-------------------|--------------|----------------|-----------|-------------------|------------------|------|
| TC-CTDT-H-003 | FR-III-01 / BR-AUTH-08 / BR-DATA-02 | CB_NV_TW thấy CTĐT thuộc đơn vị TW + descendants | CB_NV_TW đăng nhập. Seed 3 CTĐT TW + 3 CTĐT BN + 3 CTĐT ĐP. | — | 1. Vào danh sách CTĐT. | **STATE**: Backend filter `WHERE don_vi_id IN (descendants_of_TW) AND is_deleted=0` (BR-AUTH-08 + BR-DATA-02). **UI**: Hiển thị 9 CTĐT (TW + BN + ĐP cấp dưới). **PERSIST**: Reload giữ scope. | Happy |
| TC-CTDT-H-004 | FR-III-01 / BR-AUTH-08 | CB_NV_DP chỉ thấy CTĐT thuộc đúng đơn vị ĐP | CB_NV_DP (cb_nv_dp_01). Seed CTĐT cả 3 cấp + ĐP khác. | — | 1. CB_NV_DP vào danh sách. | **STATE**: Backend `WHERE don_vi_id = cb_nv_dp_01.don_vi_id`. **UI**: Chỉ CTĐT đơn vị ĐP của user. KHÔNG thấy TW/BN/ĐP khác. **PERSIST**: Reload giữ scope. | Happy |
| TC-CTDT-H-005 | FR-III-01 / SCR-III-01 / Expandable | Click expand icon trên row CTĐT → hiển thị KHOA_HOC con | CB_NV_TW. CTĐT "CTDT-TW-2026-001" có 3 KHOA_HOC. | — | 1. Vào danh sách. 2. Click ▶ trên row CTDT-TW-2026-001. | **STATE**: Request `GET /api/v1/chuong-trinh-dao-tao/{id}/khoa-hoc`. **UI**: Row expand hiển thị nested table 3 KHOA_HOC: mã, tên, hình thức, ngày BĐ/KT, trạng thái SM-KHOAHOC (badge 9 màu). **PERSIST**: Click ▼ → collapse. | Happy |
| TC-CTDT-H-006 | FR-III-01 / BR-DATA-07 | Pagination CTĐT default 20/page + max 100 | CB_NV_TW. Seed ≥45 CTĐT TW. | URL `?size=200` (force) | 1. Default load → page 1. 2. Force URL `?size=200`. | **STATE**: Default `size=20`. Force `size=200` → BE cap về 100 (BR-DATA-07 max 100). **UI**: Default 20 dòng + "Tổng: 45 mục". Force size=200 → max 100 dòng. **PERSIST**: Reload giữ size. | Boundary 🟡 |
| TC-CTDT-H-007 | FR-III-02 / Filter | Search CTĐT — kết hợp từ_khóa + lĩnh_vực + hình_thức (AND) | CB_NV_TW. Seed: CTĐT "Pháp luật DN" lĩnh vực DAN_SU, hình thức TRUC_TUYEN; CTĐT "Pháp luật Lao động" lĩnh vực LAO_DONG, hình thức TRUC_TIEP. | tu_khoa="Pháp luật DN", linh_vuc=DAN_SU, hinh_thuc=TRUC_TUYEN | 1. Filter-bar nhập 3 điều kiện. 2. Click [Tìm kiếm]. | **STATE**: Backend WHERE AND giữa 3 condition (FR-III-02 Processing step 2). **UI**: Chỉ 1 CTĐT "Pháp luật DN" hiển thị. CTĐT khác bị lọc bỏ. **PERSIST**: Reload giữ filter. | Happy 🔴 |
| TC-CTDT-N-008 | INF-CTDT-01 | Search CTĐT — không có kết quả | CB_NV_TW. | tu_khoa="XYZ-NOT-EXIST" | 1. Search keyword không match. | **STATE**: Backend trả empty array. **UI**: Empty state "**Không tìm thấy chương trình phù hợp**" (FR-III-02 INF-CTDT-01 nguyên văn). KHÔNG render row. **PERSIST**: Reload giữ filter, vẫn empty. | Negative |

---

## C. CREATE (Thêm CTĐT — auto-gen mã, BR-DATA-04)

| ID | TraceID (Mã SRS) | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|-------------------|--------------|----------------|-----------|-------------------|------------------|------|
| TC-CTDT-H-009 | FR-III-01 / BR-DATA-04 / BR-DATA-03 | Thêm CTĐT thành công với đầy đủ field — verify auto-gen mã format | CB_NV_TW đăng nhập. Lĩnh vực "DAN_SU" tồn tại. Đơn vị TW code "TW01". Năm hiện tại 2026. | ten_chuong_trinh="CTDT Pháp luật DN 2026", linh_vuc_id=DAN_SU, ngan_sach_du_kien=200000000, so_luong_khoa=5, muc_tieu="Đào tạo 200 DN nhỏ và vừa" | 1. Click [+ Thêm CTĐT]. 2. Điền đủ field. 3. Lưu. | **STATE**: INSERT CHUONG_TRINH_DAO_TAO với `ma_ctdt` match regex `^CTDT-TW01-2026-\d+$` (BR-DATA-04 format `CTDT-{DON_VI}-{YYYY}-{SEQ}` per FR-III-01 Inputs row 1), `trang_thai='NHAP'` (FR-III-01 Processing step 4), 7 common fields BR-DATA-03 (created_at, created_by=cb_nv_tw_01, updated_at, updated_by, is_deleted=0...). AUDIT_LOG: hanh_dong='CREATE' (BR-DATA-05). **UI**: Toast "Thêm CTĐT thành công" (SPEC-CLARIFY-DT-07 nguyên văn). Form đóng, navigate về danh sách. **PERSIST**: Record mới hiển thị badge "Nháp", mã `CTDT-TW01-2026-001`. | Happy 🔴 |
| TC-CTDT-N-010 | ERR-CTDT-01 | Thêm CTĐT — tên trống | CB_NV_TW. | ten_chuong_trinh="" | 1. Form thêm. 2. Bỏ trống Tên. 3. Điền field còn lại. 4. Lưu. | **STATE**: KHÔNG INSERT. Count trước/sau bằng nhau. **UI**: Inline error "**Tên chương trình là bắt buộc**" (FR-III-01 ERR-CTDT-01 nguyên văn). Focus về field Tên. **PERSIST**: Reload → record không tồn tại. | Negative 🔴 |
| TC-CTDT-N-011 | FR-III-01 / Inputs row 4 | Thêm CTĐT — linh_vuc_id không tồn tại (FK fail) | CB_NV_TW. | linh_vuc_id="DAN_INVALID" | 1. API direct POST với linh_vuc_id sai. | **STATE**: KHÔNG INSERT. BE FK check fail → 400/422. **UI**: HTTP error / toast "Lĩnh vực không tồn tại". **PERSIST**: Count không đổi. | Negative |
| TC-CTDT-X-012 | FR-III-01 / Cross-module FR-10 DM | Field Lĩnh vực PL hiển thị data từ FR-10 DM dùng chung | CB_NV_TW. FR-10 W1.3 DM "LINH_VUC_PL" có 5 record DANG_HOAT_DONG (DAN_SU, HINH_SU, LAO_DONG, KINH_TE, HANH_CHINH). | — | 1. Form thêm CTĐT. 2. Click dropdown Lĩnh vực. | **STATE**: Backend `GET /api/v1/danh-muc?loai=LINH_VUC_PL&trang_thai=DANG_HOAT_DONG`. **UI**: Dropdown hiển thị 5 option theo seed. KHÔNG hiển thị item is_deleted=1 hoặc trang_thai=KHONG_HOAT_DONG. **PERSIST**: Reload giữ. | Cross-module 🔴 |
| TC-CTDT-X-013 | FR-III-01 / Cross-module FR-10 DM (Hình thức tập huấn) | Cross-ref: SRS Inputs Khóa học row 4 chỉ có TRUC_TUYEN/TRUC_TIEP — verify enum hard-coded vs DM | CB_NV_TW. | — | 1. Form thêm CTĐT (xem field Hình thức nếu có ở CTĐT-level) hoặc Form thêm KH con — field Hình thức. | **STATE**: Per FR-III-01 Inputs Khóa học row 4: enum = `TRUC_TUYEN` / `TRUC_TIEP`, default `TRUC_TUYEN`. **UI**: Dropdown 2 option hard-coded (KHÔNG lấy từ FR-10 DM). **PERSIST**: — **Note**: SPEC-CLARIFY-DT-08: Plan overview ghi "Hình thức tập huấn từ FR-10 DM" nhưng SRS quote enum hard-coded. Cần BA confirm có DM `HINH_THUC_TAP_HUAN` trong FR-10 hay enum static? | Cross-module 🟡 |
| TC-CTDT-N-014 | FR-III-01 / Inputs row 5 | Thêm CTĐT — ngan_sach_du_kien âm | CB_NV_TW. | ngan_sach_du_kien=-1000 | 1. API POST âm. | **STATE**: KHÔNG INSERT. BE check ≥0. **UI**: Inline error "Ngân sách phải ≥ 0". **PERSIST**: Count không đổi. | Negative 🟡 |

---

## D. UPDATE (Sửa CTĐT — chỉ NHAP, BR-FLOW-03)

| ID | TraceID (Mã SRS) | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|-------------------|--------------|----------------|-----------|-------------------|------------------|------|
| TC-CTDT-H-015 | FR-III-01 / BR-DATA-05 | Sửa CTĐT trạng thái NHAP — đổi mục tiêu + ngân sách | CB_NV_TW. CTĐT "CTDT-TW01-2026-001" NHAP. | muc_tieu_moi="Đào tạo 300 DN", ngan_sach=300000000 | 1. Row CTĐT → click [Sửa]. 2. Đổi 2 field. 3. Lưu. | **STATE**: UPDATE CHUONG_TRINH_DAO_TAO SET muc_tieu='Đào tạo 300 DN', ngan_sach_du_kien=300000000, updated_at=NOW(), updated_by=cb_nv_tw_01. AUDIT_LOG: hanh_dong='UPDATE' với du_lieu_cu/du_lieu_moi đầy đủ (BR-DATA-05). **UI**: Toast OK. **PERSIST**: Detail reflect. | Happy |
| TC-CTDT-N-016 | ERR-CTDT-04 / BR-FLOW-03 | Sửa CTĐT trạng thái DA_DUYET — bị chặn | CB_NV_TW. CTĐT "CTDT-TW01-2026-002" DA_DUYET. | muc_tieu mới | 1. Cố click [Sửa] hoặc force API PUT. | **STATE**: KHÔNG UPDATE. **UI**: Nút [Sửa] ẨN/disable per BR-FLOW-03. Force API PUT → BE reject với "**Không thể sửa chương trình đã được duyệt**" (ERR-CTDT-04 nguyên văn FR-III-01). **PERSIST**: Record không đổi. | Negative 🔴 |
| TC-CTDT-N-017 | FR-III-01 / BR-AUTH-08 | CB_NV_BN cố sửa CTĐT thuộc TW → 403 | CB_NV_BN. CTĐT TW seed. | API PUT | 1. CB_NV_BN call API PUT trên CTĐT TW. | **STATE**: KHÔNG UPDATE. BE check don_vi_id mismatch → 403. **UI**: HTTP 403. **PERSIST**: Record không đổi. | Negative |

---

## E. DELETE (Xóa mềm CTĐT — soft delete, ERR-CTDT-03)

| ID | TraceID (Mã SRS) | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|-------------------|--------------|----------------|-----------|-------------------|------------------|------|
| TC-CTDT-H-018 | FR-III-01 / BR-DATA-01 | Xóa mềm CTĐT thành công — chưa có khóa học con | CB_NV_TW. CTĐT "CTDT-TW01-2026-003" NHAP, KHÔNG có KHOA_HOC con. | — | 1. Row CTĐT → click [Xóa]. 2. Confirm dialog. | **STATE**: UPDATE SET is_deleted=1, deleted_at=NOW(), deleted_by=cb_nv_tw_01 (BR-DATA-01 soft delete). AUDIT_LOG: hanh_dong='DELETE'. **UI**: Toast "Xóa CTĐT thành công" (SPEC-CLARIFY-DT-07). Record biến mất khỏi list mặc định. **PERSIST**: Reload list → record ẩn. | Happy |
| TC-CTDT-N-019 | ERR-CTDT-03 | Xóa CTĐT có khóa học con — bị chặn | CB_NV_TW. CTĐT "CTDT-TW01-2026-001" có 3 KHOA_HOC con (is_deleted=0). | — | 1. Click [Xóa] trên CTĐT-001. 2. Confirm. | **STATE**: KHÔNG UPDATE is_deleted (FR-III-01 Processing Xóa step 2). **UI**: Toast/dialog "**Không thể xóa chương trình đã có khóa học**" (ERR-CTDT-03 nguyên văn). **PERSIST**: Record vẫn tồn tại. | Negative 🔴 |
| TC-CTDT-X-020 | FR-III-01 / BR-DATA-01 / Edge soft-delete cascade | Xóa CTĐT — sau khi xóa mềm tất cả KH con — verify CTĐT có thể xóa được | CB_NV_TW. CTĐT có 2 KH con đều `is_deleted=1`. | — | 1. Click [Xóa] trên CTĐT. 2. Confirm. | **STATE**: BE check `COUNT(KHOA_HOC WHERE ctdt_id=X AND is_deleted=0) = 0` → cho phép. UPDATE CTĐT SET is_deleted=1. **UI**: Toast OK. **PERSIST**: Record CTĐT ẩn. **Note**: SPEC-CLARIFY-DT-09: ERR-CTDT-03 áp dụng "có KH con" — định nghĩa "có" = active (is_deleted=0) hay all? Default theo logic = active only. | Edge 🟡 |

---

## F. STATE TRANSITIONS (CTĐT 4-state minimum: NHAP → CHO_DUYET → DA_DUYET / TU_CHOI)

| ID | TraceID (Mã SRS) | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|-------------------|--------------|----------------|-----------|-------------------|------------------|------|
| TC-CTDT-S-021 | FR-III-01 / SM-KHOAHOC analog | Trình duyệt CTĐT: NHAP → CHO_DUYET | CB_NV_TW. CTĐT "CTDT-TW01-2026-004" NHAP đầy đủ. | — | 1. Row → [Trình duyệt]. | **STATE**: UPDATE SET trang_thai='CHO_DUYET'. AUDIT_LOG: hanh_dong='SUBMIT'. Notification gửi cb_pd_tw_01 (BR-NOTIF-01). **UI**: Toast OK. Badge "Chờ duyệt". **PERSIST**: CHO_DUYET. | Happy |
| TC-CTDT-S-022 | FR-III-01 / BR-AUTH-05 | Phê duyệt CTĐT: CHO_DUYET → DA_DUYET (CB PD cùng cấp) | cb_pd_tw_01. CTĐT "CTDT-TW01-2026-004" CHO_DUYET. | — | 1. CB_PD_TW row → [Duyệt]. | **STATE**: UPDATE SET trang_thai='DA_DUYET'. AUDIT_LOG: hanh_dong='APPROVE'. Notification cb_nv_tw_01. **UI**: Toast. Badge "Đã duyệt". **PERSIST**: DA_DUYET. | Happy 🔴 |
| TC-CTDT-S-023 | FR-III-01 / BR-FLOW-04 | Từ chối CTĐT: CHO_DUYET → TU_CHOI (with ly_do ≥10 ký tự) | cb_pd_tw_01. CTĐT "CTDT-TW01-2026-005" CHO_DUYET. | ly_do="Mục tiêu chưa rõ ràng, cần bổ sung KPI cụ thể" | 1. Click [Từ chối]. 2. Modal nhập lý do. 3. Confirm. | **STATE**: UPDATE SET trang_thai='TU_CHOI', ly_do_tu_choi=<text>. AUDIT_LOG: hanh_dong='REJECT'. **UI**: Toast. Badge "Từ chối". **PERSIST**: TU_CHOI. | Happy 🔴 |
| TC-CTDT-S-024 | FR-III-01 / SM invalid | Trình duyệt CTĐT trạng thái DA_DUYET — invalid transition | CB_NV_TW. CTĐT DA_DUYET. | — | 1. Force API submit trên DA_DUYET. | **STATE**: KHÔNG UPDATE. BE check trang_thai NOT IN (NHAP) → reject. **UI**: Nút [Trình duyệt] không hiển thị trên DA_DUYET. Force API → 422. **PERSIST**: DA_DUYET unchanged. | Negative 🟡 |

---

## G. EXPORT EXCEL (BR-DATA-06 cap 10k)

| ID | TraceID (Mã SRS) | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|-------------------|--------------|----------------|-----------|-------------------|------------------|------|
| TC-CTDT-H-025 | FR-III-01 / BR-DATA-06 | Xuất Excel CTĐT — happy path < 10k row | CB_NV_TW. Seed 50 CTĐT TW. | filter mặc định | 1. Click [Xuất Excel]. | **STATE**: Backend `GET /api/v1/chuong-trinh-dao-tao/export?filter=...` → file xlsx. AUDIT_LOG: hanh_dong='EXPORT'. **UI**: Browser download `chuong-trinh-dao-tao-{timestamp}.xlsx`. File mở được, có header 9 cột (Mã, Tên, Lĩnh vực, Hình thức, Ngày BĐ, Ngày KT, Số khóa, Trạng thái, total_count). 50 row data. **PERSIST**: File có thể mở Excel. | Happy 🔴 |
| TC-CTDT-N-026 | ERR-EXP-01 / BR-DATA-06 | Xuất Excel CTĐT — vượt 10k row | CB_NV_TW (giả định). Seed/mock filter trả >10000 record. | filter "all years" | 1. Click [Xuất Excel] trên dataset >10k. | **STATE**: BE check `COUNT > 10000`. Hành vi mặc định: cap 10k row + WARNING (BR-DATA-06 + ERR-EXP-01 severity WARNING). **UI**: Toast warning "**Chỉ xuất được 10.000 dòng đầu, vui lòng lọc thu hẹp**" (SPEC-CLARIFY-DT-10 nguyên văn). File xlsx download chỉ chứa 10000 row. **PERSIST**: Re-filter < 10k → export đầy đủ. | Negative 🔴 |

---

## H. PERMISSION (high-level — chi tiết ở 13-TC-permission-matrix.md)

| ID | TraceID (Mã SRS) | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|-------------------|--------------|----------------|-----------|-------------------|------------------|------|
| TC-CTDT-P-027 | Permission Matrix / DN Public | DN/NHT public_view CTĐT trạng thái DA_CONG_KHAI qua Cổng PLQG | DN (dn_01) đăng nhập app HTPLDN hoặc NHT qua Cổng PLQG. | URL public chuyên trang | 1. DN truy cập trang công khai CTĐT. | **STATE**: BE filter `WHERE trang_thai='DA_CONG_KHAI' AND is_deleted=0` (no don_vi scope cho public). **UI**: Hiển thị danh sách CTĐT DA_CONG_KHAI từ tất cả đơn vị. CHỈ READ. KHÔNG có nút Sửa/Xóa/Trình duyệt. **PERSIST**: Reload giữ. | Happy |

---

## I. NEGATIVE / EDGE

| ID | TraceID (Mã SRS) | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|-------------------|--------------|----------------|-----------|-------------------|------------------|------|
| TC-CTDT-E-028 | FR-III-01 / BR-DATA-04 / Auto-gen sequence | Tạo 3 CTĐT cùng năm cùng đơn vị → SEQ tăng dần 001, 002, 003 | CB_NV_TW. Đơn vị TW01. Năm 2026. Pre-state: 0 CTĐT 2026 trong DB. | Tạo lần lượt 3 CTĐT | 1. Tạo CTĐT-A. 2. Tạo CTĐT-B. 3. Tạo CTĐT-C. 4. Query DB. | **STATE**: 3 record với `ma_ctdt` = `CTDT-TW01-2026-001`, `CTDT-TW01-2026-002`, `CTDT-TW01-2026-003` (BR-DATA-04 SEQ atomic). **UI**: Cột Mã hiển thị 3 mã tăng dần. **PERSIST**: Filter `ma_ctdt LIKE 'CTDT-TW01-2026-%'` → 3 record. | Edge 🟡 |
| TC-CTDT-E-029 | FR-III-01 / BR-DATA-05 / Audit trail full lifecycle | Verify AUDIT_LOG ghi đầy đủ chuỗi CRUD + state (qua FR-10 W1.1 UI) | CB_NV_TW + cb_pd_tw_01. FR-10 W1.1 Nhật ký HT screen sẵn dùng. | Sequence tạo→sửa→trình→duyệt→xóa | 1. Tạo CTĐT. 2. Sửa mục tiêu. 3. Trình duyệt. 4. CB_PD duyệt. 5. (Hoặc xóa CTĐT khác để cover DELETE). 6. qtht_01 mở FR-10 W1.1, filter entity_id=CTDT-001. | **STATE**: Backend ghi ≥4 row AUDIT_LOG. **UI**: FR-10 W1.1 lookup theo entity_id → table hiển thị ≥4 entries: CREATE, UPDATE (du_lieu_cu/du_lieu_moi visible), SUBMIT, APPROVE. Mỗi row: actor, thoi_gian, ip_address (BR-DATA-05). **PERSIST**: Reload FR-10 W1.1 → giữ 4 entries; UI KHÔNG có nút edit/delete (immutable). | Edge 🔴 |
| TC-CTDT-E-030 | FR-III-01 / Edge concurrent | 2 CB_NV_TW cùng sửa 1 CTĐT NHAP — optimistic lock | cb_nv_tw_01 (user A) + cb_nv_tw_02 (user B). CTĐT "CTDT-CONFLICT" NHAP. | A đổi mục tiêu, B đổi ngân sách | 1. Cả 2 mở form (updated_at=T1). 2. A lưu trước → T2. 3. B lưu sau. | **STATE**: A INSERT OK. B BE check `WHERE updated_at=T1` → 0 row → reject. **UI**: A toast OK. B toast "**Bản ghi đã bị thay đổi bởi người khác. Vui lòng tải lại trang**" (BR-EC-01 / ERR-SYS-02 — SPEC-CLARIFY-DT-11). **PERSIST**: Detail reflect chỉ A change. | Edge 🟡 |

---

## J. EDGE CASES (A4 added)

| ID | TraceID (Mã SRS) | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|-------------------|--------------|----------------|-----------|-------------------|------------------|------|
| TC-CTDT-X-031 | FR-III-01 / Cross-module FR-10 DM cascade | Lĩnh vực PL bị xóa mềm trong FR-10 khi đang được CTĐT đang DA_DUYET tham chiếu | CB_NV_TW + qtht_01. CTĐT "CTDT-LV-001" DA_DUYET, `linh_vuc_id=DAN_SU`. qtht_01 xóa mềm DM `DAN_SU` trong FR-10. | qtht_01 DELETE DM DAN_SU | 1. qtht_01 xóa DM DAN_SU. 2. cb_nv_tw_01 mở detail CTDT-LV-001. 3. Quan sát render Lĩnh vực field. | **STATE**: BE cần guard "DM đang dùng" hoặc cho phép xóa nhưng CTĐT phải hiển thị fallback. SPEC-CLARIFY-DT-EC-01: SRS FR-10 có rule "không xóa DM đang dùng" nhưng FR-03 không quote behavior khi đã xóa. Default: hiển thị "Lĩnh vực đã xóa" + tooltip warning. **UI**: Detail render gracefully, không 500. **PERSIST**: CTDT giữ linh_vuc_id (FK soft). | Cross-module 🔴 |
| TC-CTDT-X-032 | FR-III-01 / BR-FLOW-03 / Cascade rejected → resubmit | CTĐT bị TU_CHOI → CB NV sửa rồi resubmit lần 2 (per EC-04 dòng 406) | cb_nv_tw_01 + cb_pd_tw_01. CTĐT "CTDT-RESUB" CHO_DUYET → cb_pd_tw_01 từ chối. | ly_do_tu_choi → CB NV update mục tiêu → resubmit | 1. cb_pd_tw_01 từ chối CTDT-RESUB với lý do. 2. cb_nv_tw_01 sửa mục tiêu (state TU_CHOI cho phép sửa per EC-04). 3. CB NV [Trình duyệt] lần 2. | **STATE**: TU_CHOI → CHO_DUYET (resubmit). AUDIT_LOG ghi đủ 4 entry: SUBMIT-1 → REJECT → UPDATE → SUBMIT-2. ly_do_tu_choi cũ giữ trong history hoặc reset. **UI**: Toast "Đã gửi duyệt lại". Badge CHO_DUYET. **PERSIST**: SPEC-CLARIFY-DT-EC-02 — ly_do_tu_choi cũ giữ history hay reset. | Edge 🟡 |
| TC-CTDT-E-033 | FR-III-01 / Special character / SQL injection trong tên CTĐT | Tạo CTĐT với tên chứa Unicode + SQL/HTML injection pattern | cb_nv_tw_01. | ten="<script>alert(1)</script> Pháp luật DN — Đào tạo 2026 🎓"; ten2="' OR 1=1; DROP TABLE CHUONG_TRINH--" | 1. Tạo CTDT với tên test 1. 2. Tạo CTDT với tên test 2 (SQL injection). 3. Verify list render. | **STATE**: INSERT thành công cả 2 (BE escape + parameterized query). KHÔNG drop table. **UI**: Cột Tên hiển thị literal: `<script>alert(1)</script> Pháp luật DN — Đào tạo 2026 🎓` (HTML escape, không execute JS). Tên 2 hiển thị literal (không SQL exec). **PERSIST**: Reload list — 2 record đầy đủ. Audit log đủ 2 entry CREATE. | Edge 🔴 |

---

## SPEC-CLARIFY tickets (file này)

| ID | Mô tả |
|----|-------|
| SPEC-CLARIFY-DT-07 | Toast message thành công CREATE/UPDATE/DELETE CTĐT — chưa có nguyên văn trong SRS FR-III-01 (Error Handling chỉ có 4 ERR-CTDT-* cho fail cases). |
| SPEC-CLARIFY-DT-EC-01 | Cross-module FR-10 DM Lĩnh vực PL — behavior khi DM bị xóa mềm trong khi đang được CTĐT/KH/NHCH/GV tham chiếu. Default: hiển thị fallback. Cần BA confirm. |
| SPEC-CLARIFY-DT-EC-02 | EC-04 resubmit sau TU_CHOI — ly_do_tu_choi cũ giữ history hay reset. SRS quote EC-04 cho phép resubmit nhưng không quote rule history. |
| SPEC-CLARIFY-DT-08 | Plan overview ghi "Hình thức tập huấn từ FR-10 DM" nhưng SRS FR-III-01 Inputs Khóa học row 4 enum hard-coded TRUC_TUYEN/TRUC_TIEP. Clarify có DM `HINH_THUC_TAP_HUAN` trong FR-10 hay enum static? |
| SPEC-CLARIFY-DT-09 | ERR-CTDT-03 "có khóa học" — định nghĩa "có" = chỉ active (is_deleted=0) hay bao gồm soft-deleted? Default logic = active only. |
| SPEC-CLARIFY-DT-10 | ERR-EXP-01 "Export > 10k rows" message nguyên văn — SRS Phụ lục B BR-DATA-06 cap 10k nhưng UX behavior (cap silent / warning toast / block hoàn toàn) chưa quy định. |
| SPEC-CLARIFY-DT-11 | BR-EC-01 / ERR-SYS-02 message nguyên văn cho optimistic-lock conflict — SRS Phụ lục B chỉ có code, gap nguyên văn message cho FR-III. |

---

## Tổng kết file 02

- **33 TC active sau A7** phủ FR-III-01/02.
- **5 SPEC-CLARIFY** raise pending BA: DT-07, DT-08, DT-09, DT-10, DT-11.
- **BR coverage:** BR-AUTH-05/08, BR-DATA-01/02/03/04/05/06/07, BR-FLOW-03/04, BR-NOTIF-01, BR-EC-01.
- **ERR coverage:** ERR-CTDT-01, ERR-CTDT-02 (analog cho boundary date), ERR-CTDT-03, ERR-CTDT-04, INF-CTDT-01, ERR-EXP-01.
- **SM coverage:** NHAP → CHO_DUYET → DA_DUYET / TU_CHOI; invalid (resubmit DA_DUYET).
- **Cross-module:** TC-012 (Lĩnh vực PL từ FR-10 DM), TC-013 (Hình thức enum hard-coded), TC-020 (cascade soft-delete với FR-10 DM ràng buộc).

---

## A7 Filter Notes

- **SỬA:** TC-CTDT-E-029 — chuyển audit verify từ "Query AUDIT_LOG DB" sang "FR-10 W1.1 UI lookup theo entity_id". Phụ thuộc FR-10 W1.1.
- **KEEP all others:** Mọi TC observable qua UI + network panel.
