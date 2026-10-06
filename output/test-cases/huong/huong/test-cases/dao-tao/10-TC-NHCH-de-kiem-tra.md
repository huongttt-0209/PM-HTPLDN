# Test Cases — UC28/UC29/NEW-01/NEW-02/NEW-03: Ngân hàng Câu hỏi & Đề Kiểm tra (FR-III-09/10 + FR-III-NEW-01/02/03)

> **SRS Ref:** FR-III-09 (UC28 — `srs-fr-03-dao-tao.md` dòng 685-758), FR-III-10 (UC29 — dòng 762-812), FR-III-NEW-01 (Tạo đề KT — dòng 1069-1090), FR-III-NEW-02 (QL đề KT — dòng 1094-1113), FR-III-NEW-03 (Phân phối đề + map BG — dòng 1117-1138). SCR-III-04 (dòng 1174-1178 — 2 tabs Câu hỏi / Đề kiểm tra). Entity NGAN_HANG_CAU_HOI + DE_KIEM_TRA.
> **Phase:** A (Phase A re-run 2026-05-09)
> **Phạm vi:** SCR-III-04 sub-menu 3 — 2 tabs. NHCH 3 loại câu hỏi (TRAC_NGHIEM_MOT / TRAC_NGHIEM_NHIEU / TU_LUAN). Đề KT có 2 cách tạo (NGAU_NHIEN / THU_CONG) + DA_PHAN_PHOI khi map vào KHOA_HOC.
> **Cross-module:** `linh_vuc_id` ← FR-10 DM Lĩnh vực PL. `khoa_hoc_id` ← KHOA_HOC FR-03. `bai_giang_ids` ← BAI_GIANG FR-03.

---

## A. UI FIELD VERIFICATION (BẮT BUỘC)

| ID | TraceID (Mã SRS) | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|-------------------|--------------|----------------|-----------|-------------------|------------------|------|
| TC-NHCH-UI-01 | FR-III-09 / SCR-III-04 / UI | Verify SCR-III-04 layout 2 tabs (Câu hỏi / Đề kiểm tra) | CB_NV_TW (cb_nv_tw_01) đăng nhập. Seed ≥10 NHCH (đa loại + đa LV + đa độ khó) + 3 DE_KIEM_TRA. | URL `/dao-tao/ngan-hang-cau-hoi` | 1. Đăng nhập. 2. Vào "Đào tạo > Ngân hàng câu hỏi & Đề kiểm tra". 3. Verify 2 tab. | **LAYOUT**: Breadcrumb "Trang chủ > Đào tạo > NHCH & Đề KT". 2 tab: "Câu hỏi" (active default) + "Đề kiểm tra". Mỗi tab có toolbar [+ Thêm] [Tìm kiếm]. **Tab Câu hỏi**: filter (Từ khóa, Lĩnh vực, Mức độ DE/TB/KHO, Loại TRAC_NGHIEM_MOT/NHIEU/TU_LUAN, Trạng thái NHAP/CONG_KHAI/AN). Cột: Mã, Nội dung (truncate 200), Lĩnh vực, Mức độ badge, Loại badge, Số đề sử dụng, Trạng thái, Hành động. **Tab Đề KT**: filter (Từ khóa, Khóa học, Trạng thái NHAP/DA_PHAN_PHOI). Cột: Mã đề, Tên đề, Số câu, Khóa học, Thời gian làm bài, Điểm đạt, Trạng thái, Hành động. **NEGATIVE — KHÔNG có**: KHÔNG batch action xóa. KHÔNG có tab thứ 3 (per SRS dòng 1176 chỉ 2 tab). | Happy 🔴 |
| TC-NHCH-UI-02 | FR-III-09 / SCR-III-04 / UI | Verify form Thêm câu hỏi — conditional theo loai_cau_hoi | CB_NV_TW đăng nhập. | — | 1. Tab Câu hỏi → [+ Thêm câu hỏi]. 2. Đổi loai_cau_hoi 3 lần. | **LAYOUT**: Drawer/Modal. Common: Nội dung * (rich text), Lĩnh vực *, Mức độ * (radio DE/TB/KHO), Loại * (radio TRAC_NGHIEM_MOT/TRAC_NGHIEM_NHIEU/TU_LUAN), Trạng thái * (default NHAP). **CONDITIONAL** (Inputs dòng 700-710): TRAC_NGHIEM_MOT → field "Các lựa chọn" (≥2 entries, mỗi entry: text + radio "Đúng" — chỉ 1 radio chọn được). TRAC_NGHIEM_NHIEU → tương tự nhưng radio đổi thành checkbox (≥2 đáp án đúng). TU_LUAN → ẨN field lựa chọn + đáp án; có thể có "Đáp án mẫu" (textarea) nếu spec mở rộng (mark SPEC-CLARIFY-DT-16). [Hủy] [Đồng ý]. | Happy 🔴 |
| TC-NHCH-UI-03 | FR-III-NEW-01 / SCR-III-04 / UI | Verify form Tạo đề KT — conditional theo cach_tao | CB_NV_TW đăng nhập. | — | 1. Tab Đề KT → [+ Thêm đề KT]. 2. Đổi cach_tao 2 lần. | **LAYOUT**: Common: Tên đề *, Khóa học (FK), Cách tạo * (radio NGAU_NHIEN/THU_CONG), Thời gian làm bài (number, phút), Điểm đạt (default 5). **CONDITIONAL** (Inputs dòng 1080): NGAU_NHIEN → "Số câu hỏi *" (number) + "Cấu hình ngẫu nhiên" (lĩnh vực + độ khó + count per nhóm). THU_CONG → "Chọn câu hỏi" (multi-select có search NHCH, hiển thị checked count). [Hủy] [Đồng ý]. | Happy 🔴 |

---

## B. READ NHCH (FR-III-10 — UC29)

| ID | TraceID (Mã SRS) | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|-------------------|--------------|----------------|-----------|-------------------|------------------|------|
| TC-NHCH-001 | FR-III-10 / BR-DATA-07 | List NHCH phân trang default 20 | CB_NV_TW đăng nhập. Seed ≥25 NHCH. | — | 1. Tab Câu hỏi. 2. Quan sát pagination. | **STATE**: `GET /api/v1/cau-hoi?page=1&size=20`. **UI**: 20 dòng/page + count tổng. **PERSIST**: Reload page 2 → giữ. | Happy |
| TC-NHCH-002 | FR-III-10 | Filter Lĩnh vực + Mức độ KHO (AND) | CB_NV_TW đăng nhập. Seed: DAN_SU/KHO 3 câu, DAN_SU/DE 2 câu, HINH_SU/KHO 1 câu. | linh_vuc_id=DAN_SU, muc_do=KHO | 1. Tab Câu hỏi. 2. Filter LV=DAN_SU + Mức=KHO. 3. Tìm kiếm. | **STATE**: `?linh_vuc_id=DAN_SU&muc_do=KHO`. **UI**: Đúng 3 record. **PERSIST**: Reload giữ filter. | Happy |
| TC-NHCH-003 | FR-III-10 | Filter loai=TRAC_NGHIEM_NHIEU (đa đáp án) | CB_NV_TW đăng nhập. Seed mỗi loại 2 câu. | loai_cau_hoi=TRAC_NGHIEM_NHIEU | 1. Filter loại. 2. Tìm. | **STATE**: `?loai_cau_hoi=TRAC_NGHIEM_NHIEU`. **UI**: Đúng 2 record. Loại badge "Trắc nghiệm nhiều". **PERSIST**: — | Happy |

---

## B2. READ Đề KT (FR-III-NEW-02)

| ID | TraceID (Mã SRS) | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|-------------------|--------------|----------------|-----------|-------------------|------------------|------|
| TC-DEKT-001 | FR-III-NEW-02 | List Đề KT — phân trang + filter trạng thái NHAP | CB_NV_TW đăng nhập. Seed 3 NHAP + 2 DA_PHAN_PHOI. | trang_thai=NHAP | 1. Tab Đề KT. 2. Filter trạng thái NHAP. | **STATE**: `GET /api/v1/de-kiem-tra?trang_thai=NHAP`. **UI**: Đúng 3 record. **PERSIST**: — | Happy |
| TC-DEKT-002 | FR-III-NEW-02 | Click Đề KT → mở chi tiết hiển thị danh sách câu hỏi đã chọn | CB_NV_TW đăng nhập. DEKT-001 (THU_CONG) có 5 câu. | — | 1. Click row DEKT-001. | **STATE**: `GET /api/v1/de-kiem-tra/{id}` + DE_CAU_HOI join. **UI**: Drawer/Modal hiển thị 5 câu hỏi (thứ tự, nội dung, đáp án đúng, điểm). **PERSIST**: — | Happy |

---

## C. CREATE Câu hỏi

| ID | TraceID (Mã SRS) | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|-------------------|--------------|----------------|-----------|-------------------|------------------|------|
| TC-NHCH-004 | FR-III-09 / BR-DATA-03 / BR-DATA-05 | Tạo câu hỏi TRAC_NGHIEM_MOT thành công | CB_NV_TW đăng nhập. LV "DAN_SU" tồn tại. | noi_dung="Luật DN 2020 có hiệu lực từ năm nào?", linh_vuc_id=DAN_SU, muc_do=DE, loai=TRAC_NGHIEM_MOT, cac_lua_chon=[{txt:"2018",dung:false},{txt:"2019",dung:false},{txt:"2020",dung:true},{txt:"2021",dung:false}], dap_an_dung="2020", trang_thai=NHAP | 1. Tab Câu hỏi → [+ Thêm]. 2. Điền form, chọn TRAC_NGHIEM_MOT, 4 lựa chọn (1 đúng). 3. Lưu. | **STATE**: INSERT NGAN_HANG_CAU_HOI với loai_cau_hoi=TRAC_NGHIEM_MOT, cac_lua_chon JSON, dap_an_dung="2020". 7 common fields (BR-DATA-03). AUDIT_LOG CREATE. **UI**: Toast "Tạo câu hỏi thành công" (SRS Gap). **PERSIST**: Tab Câu hỏi list refresh, record xuất hiện. | Happy 🔴 |
| TC-NHCH-005 | FR-III-09 | Tạo câu hỏi TRAC_NGHIEM_NHIEU (≥2 đáp án đúng) | CB_NV_TW đăng nhập. | loai=TRAC_NGHIEM_NHIEU, cac_lua_chon=[{txt:"A",dung:true},{txt:"B",dung:true},{txt:"C",dung:false},{txt:"D",dung:false}], dap_an_dung=["A","B"] | 1-3 như TC-NHCH-004 nhưng loại=NHIEU + 2 đáp án đúng. | **STATE**: INSERT loai=TRAC_NGHIEM_NHIEU, dap_an_dung là array `["A","B"]` (JSON, Inputs dòng 709 — array ≥2 cho MULTI). **UI**: Toast OK. **PERSIST**: Detail hiển thị 2 đáp án đúng được tick. | Happy 🔴 |
| TC-NHCH-006 | FR-III-09 | Tạo câu hỏi TU_LUAN (không có lựa chọn) | CB_NV_TW đăng nhập. | loai=TU_LUAN, noi_dung="Phân tích nguyên tắc tự do hợp đồng" | 1. Tạo câu hỏi. 2. Loại=TU_LUAN. 3. Bỏ qua field lựa chọn (ẩn). 4. Lưu. | **STATE**: INSERT loai=TU_LUAN, cac_lua_chon=NULL, dap_an_dung=NULL (Inputs dòng 708-709 Cond chỉ áp dụng trắc nghiệm). **UI**: Toast OK. **PERSIST**: List hiển thị badge "Tự luận". | Happy |

---

## D. UPDATE câu hỏi

| ID | TraceID (Mã SRS) | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|-------------------|--------------|----------------|-----------|-------------------|------------------|------|
| TC-NHCH-007 | FR-III-09 / BR-DATA-05 | Sửa nội dung + đổi mức độ câu hỏi NHAP | CB_NV_TW đăng nhập. NHCH-001 trạng thái NHAP. | noi_dung mới + muc_do=KHO | 1. Click [Sửa] NHCH-001. 2. Đổi nội dung + mức độ. 3. Lưu. | **STATE**: UPDATE NGAN_HANG_CAU_HOI SET noi_dung, muc_do, updated_at. AUDIT_LOG UPDATE. **UI**: Toast OK. **PERSIST**: Reload → fields mới. | Happy |
| TC-NHCH-008 | FR-III-09 / SPEC-CLARIFY-DT-17 | Sửa câu hỏi đang dùng trong đề KT đã DA_PHAN_PHOI → cảnh báo? | CB_NV_TW đăng nhập. NHCH-002 đang dùng trong DEKT-001 (DA_PHAN_PHOI). | nội dung mới | 1. Sửa NHCH-002. 2. Lưu. | **STATE**: SRS không quote rule này — SPEC-CLARIFY-DT-17: SRS UC28 Processing-Xóa có WRN-NHCH-01 nhưng UPDATE thì không. Kỳ vọng cảnh báo "Câu hỏi đang dùng trong N đề KT đã phân phối — vẫn sửa?". **UI**: Tùy logic. **PERSIST**: — | Edge 🟡 |

---

## E. DELETE câu hỏi (BR-DATA-01 + WRN)

| ID | TraceID (Mã SRS) | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|-------------------|--------------|----------------|-----------|-------------------|------------------|------|
| TC-NHCH-009 | FR-III-09 / BR-DATA-01 | Xóa mềm câu hỏi không dùng trong đề KT nào | CB_NV_TW đăng nhập. NHCH-003 (so_de_su_dung=0). | — | 1. Click [Xóa] NHCH-003. 2. Confirm. | **STATE**: UPDATE is_deleted=1 (BR-DATA-01). AUDIT_LOG DELETE. **UI**: Toast OK. **PERSIST**: List ẩn record. | Happy |
| TC-NHCH-010 | FR-III-09 / WRN-NHCH-01 | Xóa câu hỏi đang dùng trong đề KT → cảnh báo liên kết | CB_NV_TW đăng nhập. NHCH-004 đang dùng trong 2 đề KT. | — | 1. Click [Xóa] NHCH-004. | **STATE**: BE check so_de_su_dung. **UI**: Dialog warning "**Câu hỏi đang dùng trong 2 đề kiểm tra**" (NLM nguyên văn WRN-NHCH-01 dòng 751). 2 nút [Hủy] [Vẫn xóa]. **PERSIST**: Tùy chọn user. Nếu [Vẫn xóa] → soft delete, đề KT chứa câu hỏi → cần re-evaluate (mark SPEC-CLARIFY-DT-18 cho behavior). | Negative 🔴 |

---

## F. CREATE Đề KT

| ID | TraceID (Mã SRS) | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|-------------------|--------------|----------------|-----------|-------------------|------------------|------|
| TC-DEKT-003 | FR-III-NEW-01 | Tạo đề KT thủ công (THU_CONG) chọn 5 câu hỏi cụ thể | CB_NV_TW đăng nhập. Seed ≥5 NHCH trạng thái CONG_KHAI. | ten_de="Đề KT bài 1", cach_tao=THU_CONG, cau_hoi_ids=[NHCH-001..005], thoi_gian_lam_bai=30, diem_dat=5 | 1. Tab Đề KT → [+ Thêm]. 2. Cách tạo=THU_CONG. 3. Chọn 5 câu. 4. Thời gian=30 phút, điểm đạt=5. 5. Lưu. | **STATE**: INSERT DE_KIEM_TRA với cach_tao=THU_CONG, trang_thai=NHAP. INSERT 5 row DE_CAU_HOI (FK câu hỏi). AUDIT_LOG CREATE. **UI**: Toast OK. **PERSIST**: List Đề KT có record mới với so_cau=5. | Happy 🔴 |
| TC-DEKT-004 | FR-III-NEW-01 | Tạo đề KT ngẫu nhiên (NGAU_NHIEN) — auto chọn 10 câu theo LV+độ khó | CB_NV_TW đăng nhập. Seed ≥30 NHCH (mix LV + độ khó). | cach_tao=NGAU_NHIEN, so_cau_hoi=10, random_config={linh_vuc_ids:[DAN_SU], muc_do_distribution:{DE:3,TB:4,KHO:3}} | 1. Tạo. 2. Cách tạo=NGAU_NHIEN. 3. Cấu hình LV+độ khó. 4. Số câu=10. 5. Lưu. | **STATE**: BE random select 10 câu match config (3 DE + 4 TB + 3 KHO + linh_vuc=DAN_SU). INSERT DE_KIEM_TRA + 10 DE_CAU_HOI. **UI**: Toast OK + danh sách câu được random. **PERSIST**: Detail đề → 10 câu thuộc đúng cấu hình. | Happy 🔴 |
| TC-DEKT-005 | FR-III-NEW-01 / Boundary | Tạo đề NGAU_NHIEN — yêu cầu 10 câu nhưng pool LV+độ khó chỉ có 7 | CB_NV_TW đăng nhập. Seed: 7 câu DAN_SU/KHO. | cach_tao=NGAU_NHIEN, so_cau_hoi=10, linh_vuc_ids=[DAN_SU], muc_do=KHO | 1-5 như TC-DEKT-004 nhưng pool không đủ. 5. Lưu. | **STATE**: KHÔNG INSERT (pool insufficient). **UI**: Toast/inline error "**Không đủ câu hỏi trong ngân hàng theo điều kiện (yêu cầu 10, hiện có 7)**" (SRS Gap message — mark SPEC-CLARIFY-DT-19 cho ERR code đủ pool). **PERSIST**: Count đề KT không đổi. | Negative 🔴 |

---

## G. UPDATE Đề KT (FR-III-NEW-02)

| ID | TraceID (Mã SRS) | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|-------------------|--------------|----------------|-----------|-------------------|------------------|------|
| TC-DEKT-006 | FR-III-NEW-02 | Sửa đề KT trạng thái NHAP — đổi tên + thêm câu | CB_NV_TW đăng nhập. DEKT-002 NHAP, có 5 câu. | thêm câu thứ 6 + đổi tên | 1. Click [Sửa] DEKT-002. 2. Thêm 1 câu. 3. Đổi tên. 4. Lưu. | **STATE**: UPDATE DE_KIEM_TRA + INSERT 1 DE_CAU_HOI mới. AUDIT_LOG. **UI**: Toast OK. **PERSIST**: Detail → so_cau=6. | Happy |
| TC-DEKT-007 | FR-III-NEW-02 / BR-FLOW-03 | Sửa đề KT đã DA_PHAN_PHOI → bị chặn | CB_NV_TW đăng nhập. DEKT-003 trạng thái DA_PHAN_PHOI. | — | 1. Quan sát [Sửa] icon trên row DEKT-003. | **STATE**: — **UI**: Per SRS dòng 1099 "chỉnh sửa (chỉ khi NHAP)" + AC dòng 1112 "đề chưa phân phối" → nút [Sửa] ẨN/DISABLE khi DA_PHAN_PHOI. Click direct API → 403/400 "Đề đã phân phối, không sửa được". **PERSIST**: Record không đổi. | Negative 🔴 |

---

## H. DELETE Đề KT (chỉ NHAP / chưa sử dụng)

| ID | TraceID (Mã SRS) | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|-------------------|--------------|----------------|-----------|-------------------|------------------|------|
| TC-DEKT-008 | FR-III-NEW-02 / BR-DATA-01 | Xóa mềm đề KT NHAP chưa phân phối | CB_NV_TW đăng nhập. DEKT-004 NHAP. | — | 1. Click [Xóa] DEKT-004. 2. Confirm. | **STATE**: UPDATE is_deleted=1 + DE_CAU_HOI cascade soft (mark SPEC-CLARIFY-DT-20 cho cascade strategy). AUDIT_LOG. **UI**: Toast OK. **PERSIST**: Ẩn khỏi list. | Happy |
| TC-DEKT-009 | FR-III-NEW-02 / AC dòng 1113 | Xóa đề KT đã DA_PHAN_PHOI → bị chặn | CB_NV_TW đăng nhập. DEKT-005 DA_PHAN_PHOI. | — | 1. Click [Xóa] DEKT-005. | **STATE**: KHÔNG xóa. **UI**: Per AC dòng 1113 "xóa đề chưa sử dụng". Nút [Xóa] ẨN/DISABLE. Direct API → 400 "Đề đã phân phối, không xóa được". **PERSIST**: Record giữ nguyên. | Negative 🔴 |

---

## I. MAP Đề KT → Khóa học (FR-III-NEW-03)

| ID | TraceID (Mã SRS) | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|-------------------|--------------|----------------|-----------|-------------------|------------------|------|
| TC-DEKT-010 | FR-III-NEW-03 | Phân phối đề NHAP → KHOA_HOC + map bài giảng | CB_NV_TW đăng nhập. DEKT-006 NHAP. KHOA_HOC "KH-001" DA_DUYET. BG-001/002 đã gắn KH-001. | de_kiem_tra_id=DEKT-006, khoa_hoc_id=KH-001, bai_giang_ids=[BG-001, BG-002] | 1. Tab Đề KT row DEKT-006 → click [Phân phối]. 2. Chọn KHOA_HOC=KH-001. 3. Chọn 2 bài giảng map. 4. Lưu. | **STATE**: UPDATE DE_KIEM_TRA SET khoa_hoc_id=KH-001, trang_thai=DA_PHAN_PHOI. INSERT DE_BAI_GIANG (FK DEKT + BG) cho 2 cặp. AUDIT_LOG. **UI**: Toast "Phân phối thành công". Trạng thái đề chuyển DA_PHAN_PHOI. **PERSIST**: SCR-III-02 tab "Bài giảng" của KH-001 → BG-001/002 link với DEKT-006. | Happy 🔴 |
| TC-DEKT-011 | FR-III-NEW-03 | Phân phối đề chưa NHAP (chẳng hạn DA_PHAN_PHOI rồi) → bị chặn | CB_NV_TW đăng nhập. DEKT-007 DA_PHAN_PHOI. | — | 1. Quan sát nút [Phân phối] trên row DEKT-007. | **STATE**: Per SRS dòng 1126 "Đề kiểm tra ở NHAP" precondition. **UI**: Nút [Phân phối] ẨN/DISABLE. Direct API → 400. **PERSIST**: Record không đổi. | Negative 🟡 |

---

## J. NEGATIVE — Error Handling

| ID | TraceID (Mã SRS) | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|-------------------|--------------|----------------|-----------|-------------------|------------------|------|
| TC-NHCH-011 | ERR-NHCH-01 | Tạo câu hỏi nội dung trống → ERR-NHCH-01 | CB_NV_TW đăng nhập. | noi_dung="" | 1. Tạo. 2. Bỏ trống nội dung. 3. Lưu. | **STATE**: KHÔNG INSERT. **UI**: Inline "**Nội dung câu hỏi là bắt buộc**" (NLM nguyên văn ERR-NHCH-01 dòng 749). **PERSIST**: Count không đổi. | Negative 🔴 |
| TC-NHCH-012 | ERR-NHCH-02 | Tạo câu trắc nghiệm với <2 lựa chọn → ERR-NHCH-02 | CB_NV_TW đăng nhập. | loai=TRAC_NGHIEM_MOT, cac_lua_chon=[{txt:"chỉ 1 đáp án",dung:true}] | 1. Tạo trắc nghiệm. 2. Chỉ thêm 1 lựa chọn. 3. Lưu. | **STATE**: KHÔNG INSERT. **UI**: Inline "**Câu trắc nghiệm phải có ≥ 2 lựa chọn**" (NLM nguyên văn ERR-NHCH-02 dòng 750). **PERSIST**: Count không đổi. | Negative 🔴 |
| TC-NHCH-013 | FR-III-09 / SPEC-CLARIFY-DT-21 | Tạo câu TRAC_NGHIEM_MOT không có đáp án đúng (cả 4 chọn = false) | CB_NV_TW đăng nhập. | loai=TRAC_NGHIEM_MOT, cac_lua_chon=[{txt:"A",dung:false},{txt:"B",dung:false},{txt:"C",dung:false},{txt:"D",dung:false}] | 1. Tạo. 2. 4 lựa chọn không tick đúng. 3. Lưu. | **STATE**: KHÔNG INSERT. **UI**: Inline "Phải chọn ít nhất 1 đáp án đúng" — SRS Gap nguyên văn (Inputs dòng 709 Cond ngụ ý nhưng không có ERR code) → mark SPEC-CLARIFY-DT-21. **PERSIST**: Count không đổi. | Negative 🟡 |
| TC-DEKT-012 | ERR-DEKT-01 | Tạo đề KT thủ công với 0 câu | CB_NV_TW đăng nhập. | cach_tao=THU_CONG, cau_hoi_ids=[] | 1. Tạo. 2. Cách=THU_CONG. 3. Không chọn câu nào. 4. Lưu. | **STATE**: KHÔNG INSERT. **UI**: Inline "**Đề kiểm tra phải có ít nhất 1 câu hỏi**" (ERR-DEKT-01 — SRS Gap message → mark SPEC-CLARIFY-DT-22 cho nguyên văn; logic per AC dòng 1090). **PERSIST**: Count không đổi. | Negative 🔴 |
| TC-DEKT-013 | ERR-DEKT-02 | Phân phối lại đề đã DA_PHAN_PHOI vào KH khác → reject | CB_NV_TW đăng nhập. DEKT-008 DA_PHAN_PHOI cho KH-001. | re-distribute KH-002 | 1. Cố call API `POST /api/v1/de-kiem-tra/{id}/phan-phoi` với khoa_hoc_id=KH-002. | **STATE**: KHÔNG UPDATE. BE check trang_thai=NHAP guard fail. **UI**: HTTP 400 "**Đề đã phân phối, không thể phân phối lại**" (ERR-DEKT-02 — SRS Gap nguyên văn → mark SPEC-CLARIFY-DT-23). **PERSIST**: Đề vẫn map KH-001. | Negative 🔴 |

---

## K. PERMISSION

| ID | TraceID (Mã SRS) | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|-------------------|--------------|----------------|-----------|-------------------|------------------|------|
| TC-NHCH-014 | BR-AUTH-08 | CB_NV_BN chỉ thấy NHCH thuộc đơn vị BN | CB_NV_BN_01 đăng nhập. Seed NHCH TW + BN + ĐP. | — | 1. Tab Câu hỏi. | **STATE**: Filter WHERE don_vi_id BN. **UI**: Chỉ NHCH thuộc đơn vị BN. **PERSIST**: Reload giữ scope. | Permission |
| TC-NHCH-015 | Permission Matrix | DN không có quyền vào SCR-III-04 | DN (dn_01) đăng nhập. | URL `/dao-tao/ngan-hang-cau-hoi` | 1. Đăng nhập DN. 2. Quan sát sidebar. 3. Direct URL. | **STATE**: 403 nếu cố call. **UI**: Sidebar không có menu NHCH. Direct URL → page lỗi. **PERSIST**: — | Permission |
| TC-DEKT-014 | Permission Matrix | TVV không có quyền CRUD Đề KT | TVV (tvv_01) đăng nhập. | — | 1. Quan sát menu. | **STATE**: — **UI**: Sidebar không có menu Đề KT. **PERSIST**: — | Permission 🟡 |

---

## L. EDGE CASES (A4 added)

| ID | TraceID (Mã SRS) | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|-------------------|--------------|----------------|-----------|-------------------|------------------|------|
| TC-NHCH-016 | FR-III-NEW-01 / Boundary số câu | Tạo đề KT THU_CONG với 0 câu (boundary dưới) và 200 câu (boundary trên thường gặp) | cb_nv_tw_01. | cau_hoi_ids=[] (FAIL); cau_hoi_ids=[200 NHCH] (PASS) | 2 lần test. | **STATE**: 0 câu reject ERR-DEKT-01. 200 câu INSERT OK. SPEC-CLARIFY-DT-EC-12: SRS không quote upper bound số câu/đề. Default no upper limit (BE perf risk nếu >1000). **UI**: Toast OK với 200; error với 0. **PERSIST**: Count đề KT +1 chỉ với 200. | Boundary 🟡 |
| TC-NHCH-017 | FR-III-09 / Cross-module FR-10 cascade | Lĩnh vực PL bị xóa mềm trong FR-10 khi đang được câu hỏi tham chiếu | cb_nv_tw_01 + qtht_01. NHCH-001 `linh_vuc_id=DAN_SU`. qtht_01 xóa DM DAN_SU. | qtht DELETE DM DAN_SU | 1. qtht xóa DM DAN_SU. 2. cb_nv_tw_01 mở Tab Câu hỏi. 3. Quan sát NHCH-001 render. 4. Filter dropdown "Lĩnh vực". | **STATE**: SPEC-CLARIFY-DT-EC-13: BE behavior — NHCH giữ FK soft, render fallback "Lĩnh vực đã xóa". Filter dropdown không list DM xóa. **UI**: NHCH-001 cột Lĩnh vực hiển thị "[DAN_SU - Đã xóa]" badge warning. Filter chỉ list DM còn active. **PERSIST**: Reload — NHCH không 500. | Cross-module 🟡 |
| TC-DEKT-015 | FR-III-NEW-03 / Cross-module FR-03 BG cascade | Bài giảng (FR-03) bị xóa mềm khi đang map vào đề KT DA_PHAN_PHOI | cb_nv_tw_01. DEKT-006 DA_PHAN_PHOI map BG-001. cb_nv_tw_01 xóa BG-001. | DELETE BG-001 | 1. cb_nv_tw_01 xóa BG-001. 2. Mở detail DEKT-006. 3. Quan sát map. | **STATE**: SPEC-CLARIFY-DT-EC-14: BG soft-deleted nhưng FK trong DE_BAI_GIANG vẫn giữ. Render fallback "Bài giảng đã xóa". KHÔNG cho phép xóa BG nếu đang gắn DE_PHAN_PHOI active (BR-FLOW-03 analog). Default: cảnh báo trước khi xóa. **UI**: Detail đề KT cột Bài giảng hiển thị "[BG-001 - Đã xóa]". **PERSIST**: HV vẫn truy cập được đề KT. | Cross-module 🟡 |
| TC-NHCH-018 | FR-III-09 / Inputs enum invalid | Tạo câu hỏi với muc_do enum không hợp lệ (vd "EXTREME") qua API direct | cb_nv_tw_01. | API direct POST `/api/v1/cau-hoi` body `{noi_dung:"x",linh_vuc_id:"DAN_SU",muc_do:"EXTREME",loai_cau_hoi:"TRAC_NGHIEM_MOT",cac_lua_chon:[{txt:"a",dung:true},{txt:"b",dung:false}]}` | 1. Bypass UI gọi API direct với muc_do invalid. | **STATE**: KHÔNG INSERT. BE validation enum check fail → 400/422. AUDIT_LOG không có entry CREATE. **UI**: HTTP 400/422 + body chứa error code "Mức độ không hợp lệ — chỉ chấp nhận DE/TB/KHO" (SRS Inputs dòng 705 enum chỉ 3 giá trị → SPEC-CLARIFY-DT-24 cho ERR code dedicated). **PERSIST**: Count NGAN_HANG_CAU_HOI không đổi. | Negative 🟡 |

---

## SPEC-CLARIFY tickets (file này)

| Ticket | Issue | Đề xuất |
|--------|-------|---------|
| SPEC-CLARIFY-DT-16 | SRS UC28 không quote field "Đáp án mẫu" cho TU_LUAN | BA confirm có/không có field này |
| SPEC-CLARIFY-DT-17 | SRS UC28 không có rule UPDATE câu hỏi đang dùng trong đề KT đã phân phối | Pattern WRN tương tự DELETE |
| SPEC-CLARIFY-DT-18 | SRS UC28 DELETE: behavior khi đã xóa câu hỏi đang trong đề KT (đề bị thiếu câu?) | BA confirm cascade rule |
| SPEC-CLARIFY-DT-19 | SRS UC NEW-01 không có ERR code khi pool NHCH không đủ random | BA confirm ERR-DEKT-03 + message |
| SPEC-CLARIFY-DT-20 | SRS UC NEW-02 DELETE: cascade soft delete DE_CAU_HOI hay giữ? | BA confirm |
| SPEC-CLARIFY-DT-21 | SRS UC28 không có ERR code "thiếu đáp án đúng" cho trắc nghiệm | BA confirm ERR-NHCH-03 |
| SPEC-CLARIFY-DT-22 | SRS UC NEW-01 không có nguyên văn message ERR-DEKT-01 (đề 0 câu) | BA confirm |
| SPEC-CLARIFY-DT-23 | SRS UC NEW-03 không có ERR code phân phối lại đề đã DA_PHAN_PHOI | BA confirm ERR-DEKT-02 + message |
| SPEC-CLARIFY-DT-EC-12 | Upper bound số câu/đề KT — SRS không quote, default no limit | BA confirm + perf cap |
| SPEC-CLARIFY-DT-EC-13 | Cross-module FR-10 DM xóa khi câu hỏi đang tham chiếu — fallback render rule | BA confirm |
| SPEC-CLARIFY-DT-EC-14 | Cross-module BG xóa khi đang gắn đề KT DA_PHAN_PHOI — guard hay fallback | BA confirm rule |
| SPEC-CLARIFY-DT-24 | ERR code dedicated cho enum invalid (muc_do, loai_cau_hoi, trang_thai) — SRS không có ERR-NHCH-04 | BA confirm + nguyên văn message |

---

**Tổng TC file 10:** 33 TC active sau A7 (A7 không LOẠI/DEFER).

> Note: Đếm thực 33 TC active sau A6. Section header giữ section A-L theo plan.

---

## A7 Filter Notes

- **KEEP all 33 TC:** Mọi TC observable qua UI 2-tab SCR-III-04 + network panel. TC-NHCH-016 boundary 200 câu KEEP (depends on BA SLA — pending SPEC-CLARIFY-DT-EC-12 nhưng test data 200 câu là achievable trong env). Cross-module cascade TC-NHCH-017 + TC-DEKT-015 observable qua UI fallback render khi DM/BG xóa.
