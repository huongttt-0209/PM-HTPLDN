# Test Cases — UC30/UC31: Quản lý Giảng viên & Tìm kiếm GV (FR-III-11 / FR-III-12)

> **SRS Ref:** FR-III-11 (UC30 — `srs-fr-03-dao-tao.md` dòng 816-841), FR-III-12 (UC31 — dòng 843-865), SCR-III-05 (dòng 1182-1186 — list + chi tiết 2 tab Thông tin / Lịch sử giảng dạy), Entity GIANG_VIEN.
> **Phase:** A (Phase A re-run 2026-05-09)
> **Cross-module:** GV chọn từ TU_VAN_VIEN (FR-04 CG/TVV) lọc `trang_thai=DANG_HOAT_DONG` (xem `02-thu-tu-module.md` dòng 605, 621). Lĩnh vực PL ← FR-10 DM. Tab "Lịch sử giảng dạy" ← join `LICH_HOC` + `KHOA_HOC` (FR-03 nội bộ).

---

## A. UI FIELD VERIFICATION (BẮT BUỘC)

| ID | TraceID (Mã SRS) | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|-------------------|--------------|----------------|-----------|-------------------|------------------|------|
| TC-GV-UI-01 | FR-III-11 / SCR-III-05 / UI | Verify SCR-III-05 list GV + chi tiết 2 tab | CB_NV_TW (cb_nv_tw_01) đăng nhập. Seed ≥6 GIANG_VIEN cover 2 trạng thái (DANG_GIANG_DAY/TAM_DUNG) + 2 vai_tro (GIANG_VIEN/TRO_GIANG) + đa LV. | URL `/dao-tao/giang-vien` (sub-menu 4) | 1. Đăng nhập. 2. Vào "Đào tạo > Giảng viên/Trợ giảng". 3. Verify list + chi tiết. | **LAYOUT-LIST**: Breadcrumb "Trang chủ > Đào tạo > Giảng viên". Toolbar [+ Thêm GV] [+ Chọn từ TVV]. **FILTER**: Từ khóa, Lĩnh vực PL, Vai trò (GIANG_VIEN/TRO_GIANG), Trạng thái (DANG_GIANG_DAY/TAM_DUNG), Chuyên ngành. **TABLE 8 cột** (Outputs dòng 831): Mã, Họ tên, Chuyên ngành, Vai trò badge, Lĩnh vực (max 3 tag + "+N"), Số khóa đã dạy (number), Trạng thái badge, Hành động (Xem/Sửa/Xóa). **CLICK row** → DETAIL view 2 tab: Tab "Thông tin" (đầy đủ accordion) + Tab "Lịch sử giảng dạy" (table khóa đã dạy). **NEGATIVE — KHÔNG có**: KHÔNG có tab thứ 3. KHÔNG có batch action. | Happy 🔴 |
| TC-GV-UI-02 | FR-III-11 / SCR-III-05 / UI | Verify form Thêm GV — 2 mode: manual vs link TVV | CB_NV_TW đăng nhập. | — | 1. Click [+ Thêm GV] → form manual. 2. Click [+ Chọn từ TVV] → modal picker TVV. | **MANUAL FORM** (Inputs dòng 827): ho_ten *, chuyen_nganh *, trinh_do * (Cử nhân/Thạc sĩ/Tiến sĩ/Khác), don_vi (text), email, so_dien_thoai, linh_vuc_ids * (multi-select ≥1), mo_ta_nang_luc (textarea max 5000), trang_thai * (radio DANG_GIANG_DAY/TAM_DUNG default DANG_GIANG_DAY), file_dinh_kem (multi-file). [Hủy] [Đồng ý]. **LINK TVV MODE**: Modal picker hiển thị danh sách TU_VAN_VIEN filter `trang_thai=DANG_HOAT_DONG` (per `02-thu-tu-module.md` dòng 621). Chọn 1 TVV → form auto-fill ho_ten, chuyen_nganh, email, sdt, linh_vuc từ TVV; user nhập thêm chỉ trinh_do + mo_ta_nang_luc nếu khác. **NEGATIVE — KHÔNG có**: KHÔNG có dropdown vai_tro trong manual form (SRS Gap — mark SPEC-CLARIFY-DT-24: vai_tro Inputs UC30 dòng 827 không list — Outputs dòng 831 có vai_tro nhưng Inputs thiếu). | Happy 🔴 |

---

## B. READ / SEARCH (FR-III-12 — UC31)

| ID | TraceID (Mã SRS) | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|-------------------|--------------|----------------|-----------|-------------------|------------------|------|
| TC-GV-001 | FR-III-12 / BR-DATA-07 | List GV phân trang default 20 | CB_NV_TW đăng nhập. Seed ≥25 GIANG_VIEN. | — | 1. SCR-III-05. 2. Quan sát pagination. | **STATE**: `GET /api/v1/giang-vien?page=1&size=20`. **UI**: 20 dòng + count tổng. **PERSIST**: Reload trang 2 → giữ. | Happy |
| TC-GV-002 | FR-III-12 | Filter LV PL + vai_tro=TRO_GIANG (AND) | CB_NV_TW đăng nhập. Seed: GV DAN_SU 5, TRO_GIANG DAN_SU 2, GV HINH_SU 3. | linh_vuc_id=DAN_SU, vai_tro=TRO_GIANG | 1. Filter. 2. Tìm. | **STATE**: `?linh_vuc_id=DAN_SU&vai_tro=TRO_GIANG`. **UI**: Đúng 2 record. **PERSIST**: — | Happy |
| TC-GV-003 | FR-III-11 / SCR-III-05 | Click row → mở detail tab Thông tin với đầy đủ field | CB_NV_TW đăng nhập. GV-001 "Nguyễn Văn A" có file đính kèm + 5 LV. | — | 1. Click row GV-001. | **STATE**: `GET /api/v1/giang-vien/{id}`. **UI**: Drawer/Modal chi tiết. Tab "Thông tin" hiển thị: ho_ten, chuyen_nganh, trinh_do, don_vi, email, sdt, lĩnh vực (5 tag), mo_ta_nang_luc, trang_thai badge, file_dinh_kem (download link). **PERSIST**: F5 giữ URL detail. | Happy |
| TC-GV-004 | FR-III-11 / SCR-III-05 | Click tab "Lịch sử giảng dạy" → list khóa đã dạy auto-aggregate | CB_NV_TW đăng nhập. GV-002 đã dạy 3 KH (DA_KET_THUC + HOAN_THANH + DANG_DIEN_RA). | — | 1. Detail GV-002. 2. Click tab "Lịch sử giảng dạy". | **STATE**: `GET /api/v1/giang-vien/{id}/lich-su` join LICH_HOC + KHOA_HOC. **UI**: Table cột: Mã KH, Tên KH, Thời gian (BD-KT), Vai trò (GIANG_VIEN/TRO_GIANG), Trạng thái khóa badge. 3 row. **PERSIST**: F5 giữ tab active. **AC dòng 839**: "DS khóa đã dạy, vai trò" — verify đầy đủ. | Happy 🔴 |

---

## C. CREATE — Thêm GV manual

| ID | TraceID (Mã SRS) | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|-------------------|--------------|----------------|-----------|-------------------|------------------|------|
| TC-GV-005 | FR-III-11 / BR-DATA-03 / BR-DATA-05 | Thêm GV manual thành công | CB_NV_TW đăng nhập. LV "DAN_SU" + "HINH_SU" tồn tại. | ho_ten="Lê Văn B", chuyen_nganh="Luật Dân sự", trinh_do="Tiến sĩ", don_vi="ĐH Luật HN", email="b@law.edu.vn", sdt="0901234567", linh_vuc_ids=[DAN_SU, HINH_SU], mo_ta_nang_luc="20 năm kinh nghiệm", trang_thai=DANG_GIANG_DAY, file_dinh_kem=cv.pdf (2MB) | 1. Click [+ Thêm GV]. 2. Điền đầy đủ form manual. 3. Upload 1 file PDF. 4. Lưu. | **STATE**: INSERT GIANG_VIEN với 7 common fields (BR-DATA-03), tu_van_vien_id=NULL (manual). INSERT GV_LINH_VUC junction (2 row). INSERT FILE_DINH_KEM. AUDIT_LOG CREATE entity=GIANG_VIEN (BR-DATA-05). **UI**: Toast "Thêm GV thành công" (SRS Gap message → SPEC-CLARIFY-DT-25). **PERSIST**: List refresh, record xuất hiện badge trạng thái "Đang giảng dạy". | Happy 🔴 |

---

## C2. CREATE — Thêm GV link from TVV

| ID | TraceID (Mã SRS) | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|-------------------|--------------|----------------|-----------|-------------------|------------------|------|
| TC-GV-006 | FR-III-11 / Cross-FR-04 | Link GV từ TVV (DANG_HOAT_DONG) | CB_NV_TW đăng nhập. TVV "TVV-TW-001" trang_thai=DANG_HOAT_DONG, LV=DAN_SU. | tu_van_vien_id=TVV-TW-001 | 1. Click [+ Chọn từ TVV]. 2. Modal picker hiển thị TVV active. 3. Chọn TVV-TW-001. 4. Form auto-fill metadata. 5. Bổ sung trinh_do. 6. Lưu. | **STATE**: INSERT GIANG_VIEN với tu_van_vien_id=TVV-TW-001 (FK), ho_ten/chuyen_nganh/email/sdt/linh_vuc_ids copy từ TVV. AUDIT_LOG. **UI**: Toast OK. **PERSIST**: Detail GV → có badge "Liên kết TVV-TW-001" (SPEC-CLARIFY-DT-26: SRS không quote UI badge này — đề xuất cho rõ link bidirectional). | Happy 🔴 |
| TC-GV-007 | FR-III-11 / Cross-FR-04 | Modal picker TVV chỉ list TVV trạng thái DANG_HOAT_DONG | CB_NV_TW đăng nhập. Seed 3 TVV DANG_HOAT_DONG + 2 TVV TAM_DUNG + 1 TVV VO_HIEU_HOA. | — | 1. Click [+ Chọn từ TVV]. 2. Modal picker open. 3. Quan sát danh sách. | **STATE**: `GET /api/v1/tu-van-vien?trang_thai=DANG_HOAT_DONG` (per `02-thu-tu-module.md` dòng 621). **UI**: Đúng 3 TVV active hiển thị. KHÔNG hiển thị TAM_DUNG/VO_HIEU_HOA. **PERSIST**: — | Happy 🔴 |

---

## D. UPDATE — Sửa GV

| ID | TraceID (Mã SRS) | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|-------------------|--------------|----------------|-----------|-------------------|------------------|------|
| TC-GV-008 | FR-III-11 / BR-DATA-05 | Sửa GV — đổi mô tả + thêm LV | CB_NV_TW đăng nhập. GV-003 (manual). | mo_ta_nang_luc mới, linh_vuc_ids=[DAN_SU, HINH_SU, HANH_CHINH] | 1. Click [Sửa] GV-003. 2. Đổi mô tả + thêm 1 LV. 3. Lưu. | **STATE**: UPDATE GIANG_VIEN + INSERT 1 GV_LINH_VUC mới. AUDIT_LOG du_lieu_cu/moi. **UI**: Toast OK. **PERSIST**: Reload → 3 LV tag. | Happy |
| TC-GV-009 | FR-III-11 / SPEC-CLARIFY-DT-27 | Sửa GV linked TVV — sync field từ TVV hay cho phép override? | CB_NV_TW đăng nhập. GV-004 link TVV-TW-001 (ho_ten="Trần A"). | đổi ho_ten GV thành "Trần A (đổi tên)" | 1. Sửa GV-004. 2. Đổi ho_ten. 3. Lưu. | **STATE**: SRS không quote rõ — SPEC-CLARIFY-DT-27: Khi GV linked TVV, UPDATE field "ho_ten" có override TVV không? Hay chỉ field non-shared (mo_ta_nang_luc, file_dinh_kem) mới sửa được? **UI**: Tùy logic — nếu allow override → field ho_ten editable; nếu lock → readonly khi linked. **PERSIST**: Mark SPEC-CLARIFY-DT-27 cho BA confirm. | Edge 🟡 |

---

## E. DELETE — Xóa mềm

| ID | TraceID (Mã SRS) | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|-------------------|--------------|----------------|-----------|-------------------|------------------|------|
| TC-GV-010 | FR-III-11 / BR-DATA-01 | Xóa mềm GV chưa phân công khóa | CB_NV_TW đăng nhập. GV-005 chưa có LICH_HOC. | — | 1. Click [Xóa] GV-005. 2. Confirm. | **STATE**: UPDATE is_deleted=1 (BR-DATA-01). AUDIT_LOG DELETE. **UI**: Toast "Xóa thành công". **PERSIST**: Ẩn khỏi list. | Happy |
| TC-GV-011 | FR-III-11 / WRN-GV-01 | Xóa GV đang dạy → cảnh báo | CB_NV_TW đăng nhập. GV-006 đang dạy 2 KH (DANG_DIEN_RA). | — | 1. Click [Xóa] GV-006. | **STATE**: BE check số KH active. **UI**: Dialog warning "**GV đang phân công dạy 2 khóa**" (NLM nguyên văn WRN-GV-01 dòng 835). 2 nút [Hủy] [Vẫn xóa]. **PERSIST**: Tùy chọn user. **Note**: Nếu [Vẫn xóa] → KH vẫn giữ FK đến GV soft-deleted (mark SPEC-CLARIFY-DT-28). | Negative 🔴 |

---

## F. LICH_SU_GIANG_DAY — Verify auto-aggregate

| ID | TraceID (Mã SRS) | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|-------------------|--------------|----------------|-----------|-------------------|------------------|------|
| TC-GV-012 | FR-III-11 / SCR-III-05 / Outputs | Tab "Lịch sử giảng dạy" auto-aggregate khoá đã dạy với vai_tro phân biệt | CB_NV_TW đăng nhập. GV-007 vai trò GV trong KH-A (DA_KET_THUC), TRO_GIANG trong KH-B (HOAN_THANH), GV trong KH-C (DANG_DIEN_RA). | — | 1. Detail GV-007. 2. Tab Lịch sử giảng dạy. | **STATE**: Backend join LICH_HOC + KHOA_HOC. **UI**: Table 3 row: KH-A vai trò "Giảng viên" + trạng thái "Đã kết thúc"; KH-B "Trợ giảng" + "Hoàn thành"; KH-C "Giảng viên" + "Đang diễn ra". Cột "Số khóa đã dạy" trên list = 3. **PERSIST**: F5 giữ. **AC dòng 839** verify đủ. | Happy 🔴 |

---

## G. NEGATIVE — Error Handling

| ID | TraceID (Mã SRS) | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|-------------------|--------------|----------------|-----------|-------------------|------------------|------|
| TC-GV-013 | ERR-GV-01 | Tạo GV — họ tên trống → ERR-GV-01 | CB_NV_TW đăng nhập. | ho_ten="" | 1. Tạo GV manual. 2. Bỏ trống Họ tên. 3. Lưu. | **STATE**: KHÔNG INSERT. **UI**: Inline "**Họ tên là bắt buộc**" (NLM nguyên văn ERR-GV-01 dòng 835). **PERSIST**: Count không đổi. | Negative 🔴 |
| TC-GV-014 | FR-III-11 / Inputs | Tạo GV không chọn LV (linh_vuc_ids empty) → reject | CB_NV_TW đăng nhập. | linh_vuc_ids=[] | 1. Tạo. 2. Skip multi-select LV. 3. Lưu. | **STATE**: KHÔNG INSERT (Inputs dòng 827 mark linh_vuc_ids=Y bắt buộc). **UI**: Inline "Phải chọn ít nhất 1 lĩnh vực" (SRS Gap message → mark SPEC-CLARIFY-DT-29). **PERSIST**: Count không đổi. | Negative 🔴 |
| TC-GV-015 | FR-III-11 / Cross-FR-04 | Link GV với tu_van_vien_id không tồn tại (FK invalid) | CB_NV_TW đăng nhập. | tu_van_vien_id="TVV-INVALID-999" | 1. API direct POST với FK invalid. | **STATE**: KHÔNG INSERT. BE FK check fail. **UI**: HTTP error "**Tư vấn viên không tồn tại**" (SRS Gap nguyên văn → mark SPEC-CLARIFY-DT-30). **PERSIST**: Count không đổi. | Negative |
| TC-GV-016 | FR-III-11 / Inputs | Tạo GV thiếu chuyên ngành (Y bắt buộc) | CB_NV_TW đăng nhập. | chuyen_nganh="" | 1. Tạo. 2. Bỏ trống chuyên ngành. 3. Lưu. | **STATE**: KHÔNG INSERT (Inputs dòng 827 chuyen_nganh=Y). **UI**: Inline "Chuyên ngành là bắt buộc" (SRS Gap → mark SPEC-CLARIFY-DT-31). **PERSIST**: Count không đổi. | Negative |

---

## H. PERMISSION

| ID | TraceID (Mã SRS) | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|-------------------|--------------|----------------|-----------|-------------------|------------------|------|
| TC-GV-017 | BR-AUTH-08 | CB_NV_DP chỉ thấy GV thuộc đơn vị ĐP | CB_NV_DP_01 đăng nhập. Seed GV TW + BN + ĐP. | — | 1. SCR-III-05. | **STATE**: Filter WHERE don_vi_id ĐP. **UI**: Chỉ GV thuộc đơn vị ĐP. **PERSIST**: Reload giữ scope. | Permission |
| TC-GV-018 | Permission Matrix | TVV không có quyền CRUD GV | TVV (tvv_01) đăng nhập. | — | 1. Quan sát menu sidebar. | **STATE**: — **UI**: Sidebar không có menu Giảng viên cho TVV (per Permission Matrix dòng 167). **PERSIST**: — | Permission |
| TC-GV-019 | Permission Matrix | CB_PD chỉ Read-only GV (không CRUD) | CB_PD_TW (cb_pd_tw_01) đăng nhập. | — | 1. Vào SCR-III-05. 2. Quan sát toolbar. | **STATE**: — **UI**: Per Permission Matrix dòng 167 (GV CRUD chỉ CB_NV) → CB_PD button [+ Thêm] và [Sửa]/[Xóa] ẨN/DISABLE. Read-only. API direct PUT → 403. **PERSIST**: — | Permission 🟡 |

---

## I. EDGE CASES (A4 added)

| ID | TraceID (Mã SRS) | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|-------------------|--------------|----------------|-----------|-------------------|------------------|------|
| TC-GV-020 | FR-III-11 / Cross-module FR-04 / SM-TVV cascade | TVV linked GV bị TAM_DUNG (FR-04) — verify GV detail phản ánh | cb_nv_tw_01 + cb_pd_tw_01. GV-link-001 link TVV-TW-001 DANG_HOAT_DONG. cb_pd_tw_01 chuyển TVV → TAM_DUNG (UC50 FR-04). | TVV TAM_DUNG | 1. cb_pd_tw_01 chuyển TVV → TAM_DUNG. 2. cb_nv_tw_01 mở GV-link-001 detail. 3. Quan sát Tab Thông tin trang_thai field. | **STATE**: SPEC-CLARIFY-DT-EC-32: SRS không quote sync trang_thai TVV → GV. Default: GV giữ trang_thai riêng (DANG_GIANG_DAY) nhưng badge banner "TVV liên kết đang tạm dừng". KH đang dạy phải re-assign GV khác. **UI**: GV detail header có warning badge. **PERSIST**: KH đang dạy không transition. | Cross-module 🟡 |
| TC-GV-021 | FR-III-11 / Idempotency / Empty edge | GV chuyên môn 0 LV (linh_vuc_ids=NULL/[] sau update đã bỏ hết) | cb_nv_tw_01. GV-002 hiện có 2 LV. | UPDATE GV-002 với linh_vuc_ids=[] | 1. Sửa GV-002. 2. Bỏ chọn hết LV. 3. Lưu. | **STATE**: SRS Inputs UC30 dòng 827 mark linh_vuc_ids=Y bắt buộc → reject với 0 LV. **UI**: Inline error "Phải chọn ít nhất 1 lĩnh vực" (per TC-GV-014 logic mở rộng cho UPDATE). **PERSIST**: GV-002 giữ 2 LV cũ. SPEC-CLARIFY-DT-EC-33: Inputs Y constraint áp dụng cả CREATE và UPDATE. | Edge 🟡 |
| TC-GV-022 | FR-III-11 / Special character / Concurrency rename | 2 CB_NV_TW cùng đổi ho_ten GV manual (race) | cb_nv_tw_01 + cb_nv_tw_02. GV-003 manual (không link TVV). | A: ho_ten="Trần A (sửa 1)"; B: ho_ten="Trần A (sửa 2)" | 1. Cả 2 mở form sửa updated_at=T1. 2. A lưu T2. 3. B lưu T3. | **STATE**: A success → ho_ten="Trần A (sửa 1)". B BE check `WHERE updated_at=T1` → 0 row → reject ERR-SYS-02. **UI**: A toast OK. B toast "Bản ghi đã thay đổi". **PERSIST**: GV reflect chỉ A change. AUDIT_LOG 1 UPDATE entry. | Edge 🟡 |
| TC-GV-023 | FR-III-11 / Inputs validation | Tạo GV với email format invalid → reject | cb_nv_tw_01. LV "DAN_SU" tồn tại. | ho_ten="Lê A", chuyen_nganh="Luật DS", trinh_do="Thạc sĩ", email="not-an-email", sdt="0901234567", linh_vuc_ids=[DAN_SU] | 1. Tạo GV manual. 2. Email = "not-an-email". 3. Lưu. | **STATE**: KHÔNG INSERT. BE validate email format RFC 5322 fail → 400. **UI**: Inline error "Email không hợp lệ" (SPEC-CLARIFY-DT-32 — SRS UC30 Inputs dòng 827 không có ERR code dedicated cho email format). **PERSIST**: Count GIANG_VIEN không đổi. | Negative 🟡 |

---

## SPEC-CLARIFY tickets (file này)

| Ticket | Issue | Đề xuất |
|--------|-------|---------|
| SPEC-CLARIFY-DT-24 | SRS UC30 Inputs dòng 827 không list `vai_tro` (GIANG_VIEN/TRO_GIANG) nhưng Outputs dòng 831 có | BA confirm vai_tro nhập tay khi CREATE hay assign per LICH_HOC |
| SPEC-CLARIFY-DT-25 | SRS UC30 không có nguyên văn message thành công | BA confirm |
| SPEC-CLARIFY-DT-26 | SRS UC30 không quote UI badge "Liên kết TVV" cho GV linked | BA confirm |
| SPEC-CLARIFY-DT-27 | SRS UC30 UPDATE: Khi GV linked TVV, field nào override được, field nào lock? | BA confirm field-level rule |
| SPEC-CLARIFY-DT-28 | SRS UC30 DELETE: GV soft-deleted nhưng còn FK trong KH active → cascade behavior? | BA confirm |
| SPEC-CLARIFY-DT-29 | SRS UC30 không có ERR code khi linh_vuc_ids empty | BA confirm ERR-GV-02 |
| SPEC-CLARIFY-DT-30 | SRS UC30 không có nguyên văn message FK TVV invalid | BA confirm |
| SPEC-CLARIFY-DT-31 | SRS UC30 không có ERR code chuyen_nganh trống | BA confirm ERR-GV-03 |
| SPEC-CLARIFY-DT-EC-32 | Sync trạng thái TVV → GV linked (FR-04 → FR-03 cascade) — SRS không quote rule | BA confirm |
| SPEC-CLARIFY-DT-EC-33 | linh_vuc_ids Y constraint — apply cả UPDATE hay chỉ CREATE | BA confirm |
| SPEC-CLARIFY-DT-32 | Email format validation cho GV — SRS UC30 không có ERR code dedicated. Default RFC 5322 | BA confirm ERR-GV-04 + nguyên văn message |

---

**Tổng TC file 11:** 23 TC active sau A7 (A7 không LOẠI/DEFER).

---

## A7 Filter Notes

- **KEEP all 23 TC:** Mọi TC observable qua UI SCR-III-05 list + 2 tab detail + modal picker TVV + network. Concurrency TC-GV-022 thực thi 2 sessions parallel. Cross-module cascade TC-GV-020 (TVV TAM_DUNG) observable qua badge banner GV detail.
