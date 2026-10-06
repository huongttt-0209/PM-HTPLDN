# Test Cases — UC22 + UC23: Quản lý đăng ký + Đăng ký tham gia khóa học (FR-III-03 + FR-III-04)

> **SRS Ref**: FR-III-03 (UC22 — Quản lý đăng ký) + FR-III-04 (UC23 — Đăng ký tham gia) — `srs-fr-03-dao-tao.md` dòng 265-410.
> **Màn hình**: SCR-III-02 Tab "Học viên" (CB NV thêm thủ công + duyệt) + chuyên trang Cổng PLQG (DN/NHT/TVV tự đăng ký).
> **Entity**: `DANG_KY_DAO_TAO` (§3.4.3.26).
> **Process flow**: `02-thu-tu-module.md` §⑨ dòng 598 + 626 (Tab Học viên + DN cử HV).
> **Phase**: A — Phase A re-run.
> **Ngày tạo**: 2026-05-09.

---

## A. UI FIELD VERIFICATION (BẮT BUỘC chạy trước functional)

| ID | TraceID (Mã SRS) | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|-------------------|--------------|----------------|-----------|-------------------|------------------|------|
| TC-DK-UI-01 | FR-III-03 / SCR-III-02 / Tab Học viên | Verify Tab "Học viên" trong SCR-III-02 — bảng danh sách + filter trạng thái + nút thêm thủ công | CB_NV_TW (cb_nv_tw_01) đã đăng nhập. KH "KH-TW-DDR-001" trạng thái `DANG_DIEN_RA` có ≥3 đăng ký (CHO_DUYET + DA_DUYET + TU_CHOI). | URL: `/dao-tao/khoa-hoc/{id}/hoc-vien` | 1. Mở SCR-III-02 cho KH-TW-DDR-001. 2. Click Tab "Học viên". 3. Kiểm tra row-by-row vs SRS dòng 598. | **LAYOUT**: Tab "Học viên" tại tab thứ 2 (sau Tab Thông tin). Toolbar: nút [+ Thêm thủ công] (chỉ hiện cho CB NV). **TABLE — 5 cột nguyên văn dòng 598**: Họ tên / MST DN / Đơn vị / Trạng thái phê duyệt (badge: `CHO_DUYET`=cam / `DA_DUYET`=xanh lá / `TU_CHOI`=đỏ) / Hành động ([Duyệt] [Từ chối] khi `CHO_DUYET`). **FILTER**: dropdown Trạng thái (3 giá trị + Tất cả), tìm theo Họ tên/MST. **PAGINATION**: 20 mục/trang theo BR-DATA-07. **NEGATIVE**: KHÔNG có nút [Xóa đăng ký] cho CB NV (chỉ có [Từ chối]). | Happy 🔴 |
| TC-DK-UI-02 | FR-III-04 / Cổng PLQG | Verify form đăng ký Cổng PLQG cho DN/NHT/TVV — 7 field theo dòng 350-358 | DN (dn_01) đã đăng nhập Cổng PLQG. KH "KH-TW-DCK-001" `DA_CONG_KHAI` mở đăng ký, `so_luong_toi_da=20`, đã có 5 ĐK. | URL Cổng: `/cong/dao-tao/{kh_id}/dang-ky` | 1. DN duyệt danh sách KH công khai. 2. Click [Đăng ký tham gia] trên KH-TW-DCK-001. 3. Quan sát form. | **LAYOUT**: Header KH (tên, hình thức, ngày BĐ-KT, địa điểm/Zoom, slot còn lại = 15/20). **FORM 7 FIELDS** (dòng 350-358): (1) `khoa_hoc_id` (hidden auto-fill); (2) `ho_ten` * (text max 200); (3) `don_vi` (text optional, max 200); (4) `email` *; (5) `so_dien_thoai` *; (6) `ghi_chu` (textarea max 1000); (7) `nguon_dang_ky` (auto = `CHUYEN_TRANG`, hidden). Action-bar [Hủy] [Đăng ký]. **PERSIST**: Sau submit form đóng → toast + redirect dashboard DN. **NEGATIVE — ẩn khi KH chưa `DA_CONG_KHAI`**: Cố mở URL với KH `DU_THAO`/`DA_DUYET` → 403 hoặc redirect. | Happy 🔴 |

---

## B. READ / LIST (Filter trạng thái đăng ký)

| ID | TraceID (Mã SRS) | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|-------------------|--------------|----------------|-----------|-------------------|------------------|------|
| TC-DK-001 | FR-III-03 / Outputs cite dòng 302-309 | Xem danh sách đăng ký Tab "Học viên" — verify 6 fields output | CB_NV_TW đăng nhập. KH-TW-DDR-001 có 5 ĐK trộn 3 trạng thái. | — | 1. Mở Tab "Học viên" KH-TW-DDR-001. 2. Quan sát danh sách. | **STATE**: Backend `GET /api/v1/dang-ky?khoa_hoc_id={id}&page=1&size=20`. **UI**: Bảng 5 dòng. Mỗi dòng đủ 6 field nguyên văn dòng 302-309: id (hidden), ten_hoc_vien, don_vi, khoa_hoc (current), ngay_dang_ky (dd/mm/yyyy HH:mm), trang_thai (badge). **PERSIST**: Reload → cùng dataset. | Happy |
| TC-DK-002 | FR-III-03 / SCR Filter | Filter Tab "Học viên" theo trạng thái = `CHO_DUYET` | CB_NV_TW đăng nhập. KH-TW-DDR-001 có ≥1 ĐK mỗi trạng thái. | filter trạng thái = `CHO_DUYET` | 1. Tab Học viên. 2. Dropdown Trạng thái = `CHO_DUYET`. 3. Click Tìm. | **STATE**: API `?trang_thai=CHO_DUYET`. **UI**: Chỉ ĐK CHO_DUYET hiển thị. Action cột chứa [Duyệt] [Từ chối]. **PERSIST**: Reload giữ filter. | Happy |
| TC-DK-003 | FR-III-04 / Cổng PLQG | DN xem danh sách KH `DA_CONG_KHAI` qua Cổng — chỉ thấy KH mở đăng ký | DN (dn_01) đăng nhập Cổng. Seed: 1 KH `DA_CONG_KHAI` + 1 KH `DU_THAO` + 1 KH `DA_KET_THUC`. | URL `/cong/dao-tao/danh-sach` | 1. DN vào trang danh sách KH công khai. | **STATE**: API `GET /api/cong/khoa-hoc?trang_thai=DA_CONG_KHAI`. **UI**: Chỉ 1 KH `DA_CONG_KHAI` hiển thị + nút [Đăng ký]. KHÔNG hiển thị `DU_THAO`/`DA_KET_THUC`. **PERSIST**: Reload giữ list. | Happy 🔴 |

---

## C. CREATE_SELF — DN/NHT/TVV tự đăng ký qua Cổng PLQG (UC23)

| ID | TraceID (Mã SRS) | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|-------------------|--------------|----------------|-----------|-------------------|------------------|------|
| TC-DK-H-001 | FR-III-04 / AC dòng 394-396 | DN cử HV đăng ký KH thành công qua Cổng PLQG | DN (dn_01) đăng nhập. KH-TW-DCK-001 `DA_CONG_KHAI`, slot còn 15/20. **Cross-module**: DN từ FR-07. | ho_ten="Nguyễn Văn HV", don_vi="Cty TNHH ABC", email="hv@abc.vn", sdt="0901234567", ghi_chu="Tham gia học online" | 1. DN click [Đăng ký] trên KH. 2. Điền form 5 field. 3. Submit. | **STATE**: INSERT `DANG_KY_DAO_TAO` với `khoa_hoc_id={id}`, `trang_thai='CHO_DUYET'` (dòng 367), `nguon_dang_ky='CHUYEN_TRANG'`, `nguoi_dang_ky_id=dn_01`. AUDIT_LOG hành động='CREATE'. Notify CB_NV_TW (BR-NOTIF-01 — gốc `srs-fr-03` dòng 369). **UI**: Toast "Đăng ký thành công, chờ duyệt" (SRS Gap nguyên văn — **SPEC-CLARIFY-DT-DK-01**). Form đóng. **PERSIST**: Tab "Lịch sử đăng ký" của DN → record mới với trạng thái CHO_DUYET. | Happy 🔴 |
| TC-DK-H-002 | FR-III-04 / Tác nhân NHT | NHT (nguoi_huong_thu) tự đăng ký KH qua Cổng PLQG | NHT (nht_01) đăng nhập Cổng. KH-TW-DCK-001 `DA_CONG_KHAI`, slot còn ≥1. | ho_ten=NHT info, email NHT | 1. NHT đăng ký tương tự DN. | **STATE**: INSERT với `nguoi_dang_ky_id=nht_01`. **UI**: Tương tự TC-DK-H-001. **PERSIST**: Lookup ĐK của nht_01 → record xuất hiện. | Happy |
| TC-DK-H-003 | FR-III-04 / Tác nhân TVV | TVV đăng ký KH qua Cổng (Cross-module FR-04 CG/TVV) | TVV (tvv_01) đăng nhập Cổng. KH-TW-DCK-001 `DA_CONG_KHAI`, slot còn ≥1. | TVV info | 1. TVV đăng ký. | **STATE**: INSERT với `nguoi_dang_ky_id=tvv_01`. **UI**: Form đóng + toast. **PERSIST**: Record xuất hiện trong Tab Học viên KH (CB NV thấy ngay). | Happy |

---

## D. CREATE_MANUAL — CB NV thêm thủ công (Tab Học viên)

| ID | TraceID (Mã SRS) | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|-------------------|--------------|----------------|-----------|-------------------|------------------|------|
| TC-DK-H-004 | FR-III-04 / 02-thu-tu dòng 598+626 | CB NV thêm HV thủ công vào KH `DANG_DIEN_RA` qua Tab Học viên | CB_NV_TW đăng nhập. KH-TW-DDR-001 `DANG_DIEN_RA`, slot còn ≥1. | ma_so_thue="0123456789", ho_ten="Lê Thị HV", email="ht@cty.vn", sdt="0912345678" | 1. Tab Học viên. 2. Click [+ Thêm thủ công]. 3. Điền form modal 4 field (dòng 626). 4. Lưu. | **STATE**: INSERT `DANG_KY_DAO_TAO` với `nguon_dang_ky='NHAP_TAY'` (per dòng 358 enum), `trang_thai='DA_DUYET'` (CB NV thêm = đã duyệt sẵn — **SPEC-CLARIFY-DT-DK-02**: cần BA xác nhận default state). AUDIT_LOG. **UI**: Toast OK. Modal đóng. **PERSIST**: Bảng Tab Học viên thêm 1 dòng. | Happy 🔴 |
| TC-DK-H-005 | FR-III-04 / Import Excel | CB NV import Excel danh sách HV (dòng 369) | CB_NV_TW đăng nhập. KH-TW-DDR-001 `DANG_DIEN_RA`. File `hv-template.xlsx` 5 dòng (4 hợp lệ + 1 thiếu email). | file 5 dòng | 1. Tab Học viên. 2. Click [+ Thêm thủ công] → tab Import Excel. 3. Upload file. 4. Xem báo cáo + xác nhận. | **STATE**: 4 row INSERT thành công với `nguon_dang_ky='IMPORT_EXCEL'` (dòng 358). 1 row reject vì thiếu email. AUDIT_LOG: 4 entries CREATE. **UI**: Bảng review hiển thị 4 OK + 1 LỖI dòng (lý do "Email bắt buộc"). Sau confirm → toast "Import thành công 4/5". **PERSIST**: Tab Học viên +4 record. | Happy 🟡 |

---

## E. APPROVE / REJECT (CB NV duyệt/từ chối ĐK — UC22)

| ID | TraceID (Mã SRS) | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|-------------------|--------------|----------------|-----------|-------------------|------------------|------|
| TC-DK-H-006 | FR-III-03 / Bước 4 dòng 296 | CB NV duyệt 1 ĐK `CHO_DUYET` → `DA_DUYET` | CB_NV_TW đăng nhập. ĐK-001 trạng thái `CHO_DUYET` thuộc KH-TW-DDR-001 (cùng đơn vị TW). | — | 1. Tab Học viên KH-TW-DDR-001. 2. Filter `CHO_DUYET`. 3. Click [Duyệt] trên ĐK-001. 4. Confirm. | **STATE**: UPDATE DANG_KY_DAO_TAO SET `trang_thai='DA_DUYET'`, updated_at, updated_by=cb_nv_tw_01. AUDIT_LOG hành động='APPROVE'. Notify nguoi_dang_ky qua email + in-app (BR-NOTIF-01). **UI**: Toast "Đã duyệt đăng ký" (SRS Gap nguyên văn — SPEC-CLARIFY-DT-DK-01). Badge ĐK đổi sang DA_DUYET (xanh lá). **PERSIST**: Reload → record giữ DA_DUYET. | Happy 🔴 |
| TC-DK-H-007 | FR-III-03 / Bước 5 dòng 297 | CB NV từ chối ĐK với lý do (BR-FLOW-04) → `TU_CHOI` | CB_NV_TW đăng nhập. ĐK-002 `CHO_DUYET`. | ly_do_tu_choi="Số CMND không khớp với DN cử" (≥10 ký tự) | 1. Click [Từ chối] trên ĐK-002. 2. Modal nhập lý do. 3. Confirm. | **STATE**: UPDATE SET `trang_thai='TU_CHOI'`, `ly_do_tu_choi=...`. AUDIT_LOG hành động='REJECT'. Notify nguoi_dang_ky. **UI**: Toast "Đã từ chối đăng ký". Badge → TU_CHOI (đỏ). **PERSIST**: Reload giữ TU_CHOI + lý do trong tooltip. | Happy 🔴 |

---

## F. NEGATIVE / ERROR

| ID | TraceID (Mã SRS) | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|-------------------|--------------|----------------|-----------|-------------------|------------------|------|
| TC-DK-N-001 | ERR-DK-DT-03 / EC-01 dòng 403 | Đăng ký vượt `so_luong_toi_da` (lớp đầy) | DN (dn_01) đăng nhập Cổng. KH-TW-DCK-FULL `DA_CONG_KHAI`, `so_luong_toi_da=20`, đã có 20 ĐK `DA_DUYET`. | full form | 1. DN click [Đăng ký] trên KH-FULL. 2. Submit. | **STATE**: KHÔNG INSERT. Backend check count ĐK NOT TU_CHOI ≥ so_luong_toi_da → reject. **UI**: Toast/inline "**Lớp đã đủ số lượng**" (nguyên văn `srs-fr-03` dòng 392 ERR-DK-DT-03). Form không đóng. **PERSIST**: Count ĐK không đổi. | Negative 🔴 |
| TC-DK-N-002 | ERR-DK-DT-02 / Bước 2 dòng 366 | Đăng ký trùng (cùng `nguoi_dang_ky_id` + `khoa_hoc_id`) | DN (dn_01) đăng nhập Cổng. DN đã có 1 ĐK `CHO_DUYET` cho KH-TW-DCK-001. | submit lại | 1. DN truy cập lại KH-TW-DCK-001. 2. Click [Đăng ký]. 3. Submit. | **STATE**: KHÔNG INSERT. **UI**: Toast "**Bạn đã đăng ký khóa học này**" (nguyên văn dòng 391 ERR-DK-DT-02). Có thể disable nút [Đăng ký] trên KH đã ĐK. **PERSIST**: Count = 1 (không thêm). | Negative 🔴 |
| TC-DK-N-003 | ERR-DK-DT-01 / PRE-02 dòng 346 | Đăng ký khi KH chưa `DA_CONG_KHAI` | DN (dn_01). KH-TW-DUTHAO-001 trạng thái `DA_DUYET` (chưa công khai). | API direct hoặc URL trực tiếp | 1. DN cố call POST `/api/cong/dang-ky` với khoa_hoc_id của KH chưa công khai. | **STATE**: KHÔNG INSERT. **UI**: Toast "**Khóa học chưa/đã đóng đăng ký**" (nguyên văn dòng 390 ERR-DK-DT-01). UI Cổng KHÔNG hiển thị nút [Đăng ký] trên KH chưa công khai (preventive). **PERSIST**: Count không đổi. | Negative 🔴 |
| TC-DK-N-004 | FR-III-03 / BR-FLOW-04 / dòng 287 | CB NV từ chối ĐK không nhập lý do | CB_NV_TW. ĐK-003 `CHO_DUYET`. | ly_do_tu_choi="" | 1. Click [Từ chối]. 2. Để trống lý do. 3. Confirm. | **STATE**: KHÔNG UPDATE. **UI**: Inline error "**Lý do từ chối là bắt buộc**" (nguyên văn ERR-DKDT-02 dòng 321). BR-FLOW-04 ≥10 ký tự — **SPEC-CLARIFY-DT-DK-03**: BR-FLOW-04 áp dụng cho UC22 reject ĐK hay chỉ UC34/UC37 reject KH? SRS dòng 287 chỉ ghi "bắt buộc" không nói min 10. **PERSIST**: ĐK giữ CHO_DUYET. | Negative 🔴 |
| TC-DK-N-005 | FR-III-04 / Email format | Đăng ký với email sai format RFC 5322 | DN (dn_01) đăng nhập Cổng. KH-TW-DCK-001 `DA_CONG_KHAI` slot còn ≥1. | ho_ten="Trần B", email="not-an-email", sdt="0901234567" | 1. Form ĐK. 2. Email = "not-an-email" (thiếu @ + domain). 3. Submit. | **STATE**: KHÔNG INSERT. BE validate regex RFC 5322 fail → 400. **UI**: Inline "Email không hợp lệ" (SRS Gap nguyên văn — **SPEC-CLARIFY-DT-DK-04**). Focus về field email. **PERSIST**: Count DANG_KY_DAO_TAO không đổi. Reload list DN — record không tồn tại. | Negative 🟡 |

---

## G. PERMISSION

| ID | TraceID (Mã SRS) | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|-------------------|--------------|----------------|-----------|-------------------|------------------|------|
| TC-DK-P-001 | FR-III-03 / BR-AUTH-08 | CB_NV_DP cố duyệt ĐK của KH thuộc đơn vị TW (cross-cấp) | CB_NV_DP (cb_nv_dp_01) đăng nhập. ĐK-001 thuộc KH-TW-DDR-001 (TW). | API direct PUT `/api/v1/dang-ky/{id}/duyet` | 1. CB_NV_DP cố call API duyệt ĐK của KH TW. | **STATE**: KHÔNG UPDATE. BE check `khoa_hoc.don_vi_id != user.don_vi_id` → 403 (BR-AUTH-08). **UI**: HTTP 403 hoặc toast "Bạn không có quyền". **PERSIST**: ĐK giữ CHO_DUYET. | Negative |
| TC-DK-P-002 | FR-III-03 / Permission Matrix | CB_PD cố duyệt ĐK qua UI → action không hiển thị | CB_PD_TW (cb_pd_tw_01) đăng nhập. KH-TW-DDR-001. | — | 1. Mở Tab Học viên. 2. Lọc `CHO_DUYET`. 3. Quan sát cột Hành động. | **STATE**: — **UI**: KHÔNG có nút [Duyệt]/[Từ chối] (CB PD không có quyền theo Permission Matrix dòng 162: `DANG_KY Approve = scope-own CB_NV` chỉ CB NV). Có thể hiện [Xem]. **PERSIST**: Reload giữ. | Negative 🟡 |

---

## H. EDGE & BOUNDARY

| ID | TraceID (Mã SRS) | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|-------------------|--------------|----------------|-----------|-------------------|------------------|------|
| TC-DK-E-001 | FR-III-04 / EC-03 dòng 405 | Concurrency — 2 DN cùng đăng ký KH với slot cuối | DN-A (dn_01) và DN-B (dn_02) cùng đăng nhập. KH-TW-DCK-LAST `DA_CONG_KHAI`, `so_luong_toi_da=10`, đã có 9 ĐK `DA_DUYET`. | 2 form ĐK đồng thời | 1. Cả 2 DN mở form ĐK cùng lúc. 2. DN-A submit trước (slot 10/10). 3. DN-B submit sau. | **STATE**: DN-A INSERT thành công (slot full). DN-B: BE check count → reject với ERR-DK-DT-03 (per EC-01 dòng 403). **UI**: DN-A toast OK. DN-B toast "Lớp đã đủ số lượng". **PERSIST**: Count ĐK = 10 (không vượt). EC-03 nguyên văn dòng 405: "khóa hàng trên KHOA_HOC" → BE phải dùng row-lock pessimistic. | Edge 🔴 |
| TC-DK-E-002 | FR-III-04 / EC-02 dòng 404 | Hủy KH đã có ĐK `DA_DUYET` → notify all HV | CB_NV_TW. KH-TW-CANCELED có 5 ĐK `DA_DUYET`. KH chưa diễn ra (DA_CONG_KHAI hoặc DA_DUYET). | — | 1. CB NV [Hủy KH] trên SCR-III-02. 2. Nhập lý do hủy. 3. Confirm. | **STATE**: UPDATE KHOA_HOC SET trang_thai='HUY' (SM-KHOAHOC dòng 105). EC-02 dòng 404: bắt buộc gửi notify cho **tất cả HV `DA_DUYET`** (5 email). 5 row notification. **UI**: Toast "KH đã hủy. Đã thông báo 5 HV." (SRS Gap nguyên văn — **SPEC-CLARIFY-DT-DK-05**). **PERSIST**: ĐK vẫn giữ trạng thái cũ (không auto đổi). KH = HUY. | Edge 🟡 |
| TC-DK-E-003 | FR-III-04 / Boundary thời gian | Đăng ký phút cuối — KH `DA_CONG_KHAI` đến 23:59 ngày BĐ rồi auto chuyển `DANG_DIEN_RA` 00:00 | DN (dn_01). KH-TW-MIDNIGHT `DA_CONG_KHAI`, `ngay_bat_dau=2026-05-10 00:00:00`. Test tại 23:58 ngày 2026-05-09 và 00:01 ngày 2026-05-10. | submit form ĐK 2 lần | 1. Test 23:58 → submit. 2. Test 00:01 → submit. | **STATE**: 23:58 INSERT thành công (KH vẫn DA_CONG_KHAI). 00:01: KH đã auto-transition `DANG_DIEN_RA` (per SM dòng 101) → reject với ERR-DK-DT-01 (KH không còn `DA_CONG_KHAI`). **UI**: Lần 1 OK. Lần 2 toast "Khóa học đã bắt đầu, không thể đăng ký". **PERSIST**: ĐK đầu giữ CHO_DUYET. | Edge 🟡 |
| TC-DK-E-004 | FR-III-04 / Hủy ĐK self-service | DN/NHT/TVV hủy ĐK của mình khi `CHO_DUYET` | DN (dn_01). DN có 1 ĐK `CHO_DUYET` trên KH-TW-DCK-001 (chưa duyệt). | — | 1. DN vào "Lịch sử đăng ký". 2. Click [Hủy đăng ký] trên ĐK. 3. Confirm. | **STATE**: SRS không có UC nguyên văn cho self-cancel ĐK → **SPEC-CLARIFY-DT-DK-06**: DN/NHT/TVV có quyền tự hủy ĐK trước duyệt? Kỳ vọng: UPDATE trang_thai='TU_CHOI' với `ly_do_tu_choi='Người ĐK tự hủy'` HOẶC DELETE soft. **UI**: Tùy implementation. **PERSIST**: Per BA confirm. | Edge 🟡 |

---

## I. EDGE CASES (A4 added)

| ID | TraceID (Mã SRS) | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|-------------------|--------------|----------------|-----------|-------------------|------------------|------|
| TC-DK-E-005 | FR-III-04 / Idempotency / Approve race | DN double-click [Đăng ký] (race) — chỉ 1 ĐK tạo | DN dn_01 đăng nhập Cổng. KH-TW-DCK-001 `DA_CONG_KHAI`. | Double-click button [Đăng ký] <500ms | 1. DN click [Đăng ký] nhanh 2 lần. 2. Query DB. | **STATE**: INSERT chỉ 1 record. ERR-DK-DT-02 (duplicate) chặn lần 2 hoặc client disable. AUDIT_LOG chỉ 1 CREATE. **UI**: Toast OK 1 lần; lần 2 (nếu trigger) → "Bạn đã đăng ký khóa học này". **PERSIST**: 1 ĐK. SPEC-CLARIFY-DT-DK-07: BE debounce qua composite key `(nguoi_dang_ky_id, khoa_hoc_id)` UNIQUE. | Edge 🔴 |
| TC-DK-E-006 | FR-III-03 / Concurrency approve | 2 CB_NV_TW cùng [Duyệt] 1 ĐK `CHO_DUYET` (race) | cb_nv_tw_01 + cb_nv_tw_02. ĐK-001 CHO_DUYET. | Cả 2 click [Duyệt] cùng updated_at=T1 | 1. CB-A click T2. 2. CB-B click T3. | **STATE**: CB-A success → DA_DUYET. CB-B BE check `WHERE updated_at=T1 AND trang_thai='CHO_DUYET'` → 0 row → reject ERR-SYS-02. **UI**: A toast OK. B toast "ĐK đã được duyệt bởi người khác". **PERSIST**: AUDIT_LOG chỉ 1 APPROVE. updated_by=cb_nv_tw_01. | Edge 🟡 |
| TC-DK-N-006 | FR-III-04 / Special character / Họ tên Unicode + emoji | Đăng ký với họ tên chứa Unicode + emoji + ký tự đặc biệt | DN dn_01 đăng nhập Cổng. KH `DA_CONG_KHAI`. | ho_ten="Nguyễn Văn Á 🎓 (XSS<script>)" | 1. Form ĐK. 2. Họ tên = test data. 3. Submit. | **STATE**: INSERT thành công (BE escape HTML). KHÔNG execute JS. **UI**: List Tab Học viên render literal "Nguyễn Văn Á 🎓 (XSS<script>)" (HTML escape). **PERSIST**: Reload → giữ nguyên text. | Edge 🟡 |

---

## SPEC-CLARIFY tickets bổ sung (file này)

| ID | Mô tả | Action |
|----|-------|--------|
| SPEC-CLARIFY-DT-DK-01 | SRS không có message toast nguyên văn cho "Đăng ký thành công" / "Đã duyệt" / "Đã từ chối" — nguyên văn cho FE | Confirm với BA copy chuẩn |
| SPEC-CLARIFY-DT-DK-02 | CB NV thêm HV thủ công từ Tab Học viên — `trang_thai` default = `DA_DUYET` (đã duyệt sẵn) hay `CHO_DUYET` (cần duyệt lại)? SRS dòng 626 không nói rõ | Confirm BA: Manual = auto DA_DUYET |
| SPEC-CLARIFY-DT-DK-03 | BR-FLOW-04 (lý do ≥10 ký tự) áp dụng cho UC22 reject ĐK hay chỉ UC34/UC37 reject KH? SRS dòng 287 chỉ ghi "bắt buộc" không quote min length | Confirm BA mở rộng BR-FLOW-04 cho UC22 |
| SPEC-CLARIFY-DT-DK-04 | Validation email format — SRS không có ERR-DK-* riêng cho email format. Test plan kỳ vọng inline error chuẩn RFC 5322 | Confirm BA bổ sung error code |
| SPEC-CLARIFY-DT-DK-05 | EC-02 dòng 404: nội dung notify HV khi hủy KH — SRS không có template nguyên văn | Confirm BA template email |
| SPEC-CLARIFY-DT-DK-06 | DN/NHT/TVV có UC tự hủy ĐK của mình trước khi CB NV duyệt? SRS không có UC riêng cho self-cancel | Confirm BA bổ sung UC self-cancel hoặc khẳng định KHÔNG |
| SPEC-CLARIFY-DT-DK-07 | Composite UNIQUE `(nguoi_dang_ky_id, khoa_hoc_id)` để chặn duplicate ĐK — SRS chỉ quote ERR-DK-02 logic, chưa quote schema constraint. |

---

## A7 Filter Notes

- **KEEP all 26 TC:** Mọi TC observable qua UI (Cổng PLQG DN side + Tab Học viên CB NV side) + network. TC-DK-E-003 boundary thời gian (auto-transition midnight) — KEEP nhưng phụ thuộc seed time đã expire (xem cross-ref TC-LICH-S-013/014 DEFER A7). TC-DK-E-004 self-cancel keep nhưng pending BA SPEC-CLARIFY-DT-DK-06.

---

## Tóm tắt file

- **Tổng TC**: 26 active (post-A4) — A6 audit reconciled.
- **Section count cuối:**
  - A. UI = 2 (TC-DK-UI-01, 02)
  - B. READ = 3 (TC-DK-001, 002, 003)
  - C. CREATE_SELF = 3 (TC-DK-H-001, 002, 003)
  - D. CREATE_MANUAL = 2 (TC-DK-H-004, 005)
  - E. APPROVE/REJECT = 2 (TC-DK-H-006, 007)
  - F. NEGATIVE = 5 (TC-DK-N-001..005)
  - G. PERMISSION = 2 (TC-DK-P-001..002)
  - H. EDGE & BOUNDARY = 4 (TC-DK-E-001..004)
  - I. EDGE A4 = 3 (TC-DK-E-005, E-006, N-006)
- **A7-filter recommendation:** giữ tất cả 26 TC; cân nhắc downgrade priority TC-DK-E-003 (timezone) + TC-DK-E-004 (self-cancel pending SPEC-CLARIFY-DT-DK-06).
- **SPEC-CLARIFY active**: 7 (DT-DK-01..07).
