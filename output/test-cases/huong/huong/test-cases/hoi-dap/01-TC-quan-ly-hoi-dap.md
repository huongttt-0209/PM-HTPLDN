# Test Cases — FR-II-01 (UC10): Quản lý Hỏi đáp

> **SRS Ref**: FR-II-01 (lines 77-211), SCR-II-01 (lines 1023-1107), Entity HOI_DAP
> **Ngày tạo**: 2026-05-10
> **Đặc thù**: CRUD HOI_DAP với 9-state lifecycle. Tạo mới mặc định MOI + `muc_do_phuc_tap=THUONG`. Sửa/Xóa cấm khi state ∈ {DA_DUYET, CONG_KHAI, HOAN_THANH} (BR-FLOW-03 mở rộng theo F-19). Soft delete BR-DATA-01. Batch xóa per-record với optimistic locking.

---

## Quy ước

- **Priority**: 🔴 P0 (critical) · 🟡 P1 (high) · 🟢 P2 (medium)
- **TraceID**: `FR-II-01 / {section}` — truy vết SRS
- **Pre-conditions mặc định**: User đã đăng nhập, có quyền `HOI_DAP_CREATE/UPDATE/DELETE`, scope theo `don_vi_id` (BR-AUTH-08).

---

## Trường input FR-II-01

| # | Field | Bắt buộc | Kiểu | Ràng buộc |
|---|-------|----------|------|-----------|
| 1 | ma_hoi_dap | Y (auto) | text | Auto-gen `HD-YYYYMMDD-SEQ` (BR-DATA-04) |
| 2 | noi_dung | Y | text long | Max 5000 ký tự |
| 3 | linh_vuc_id | Y | identifier | FK DANH_MUC (UC99 Lĩnh vực PL) |
| 4 | ten_nguoi_gui | N | text | Max 100, strip emoji + zero-width |
| 5 | email_nguoi_gui | N | text | Max 100, RFC 5322 |
| 6 | sdt_nguoi_gui | N | text | 10-11 chữ số (có thể có "+" đầu) |
| 7 | doanh_nghiep_id | N | identifier | FK DOANH_NGHIEP |
| 8 | kenh_tiep_nhan | Y | enum 5 | DVC/CONG_PLQG/TRUC_TIEP/HE_THONG_KHAC/TVN_BRIDGE (TVN auto-set, không cho user nhập) |
| 9 | file_dinh_kem | N | binary[] | Max 10 file/upload, tổng 100MB, mỗi file 20MB. Format: doc/docx/xls/xlsx/pdf. ClamAV bắt buộc |
| 10 | don_vi_id | Y | identifier | FK DON_VI. Default: Sở TP tỉnh DN (CONG_PLQG) hoặc đơn vị CB (kênh khác) [CR-06][Q-04] |
| 11 | muc_do_phuc_tap | Y | enum | THUONG / PHUC_TAP. Default THUONG (NĐ55/2019 Đ.8 K.1) |

---

## A. CRUD HỎI ĐÁP — HAPPY PATH

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|---------|--------------|----------------|-----------|-------------------|------------------|------|
| TC-HD-001 | FR-II-01 / Processing Thêm mới step 2-10 | Tạo HOI_DAP mới — happy THUONG | cb_nv_tw_01 login. Lĩnh vực "Đất đai" tồn tại (UC99). | noi_dung="Thủ tục cấp sổ đỏ?", linh_vuc=Đất đai, kenh=TRUC_TIEP, muc_do_phuc_tap=THUONG | 1. SCR-II-01 click [+ Thêm mới]. 2. Drawer mở. 3. Nhập đủ trường bắt buộc. 4. Click [Lưu]. | (1) POST /hoi-dap thành công 201. (2) Drawer đóng + toast "Đã tạo HOI_DAP {ma}". (3) Danh sách reload, record mới có `ma=HD-YYYYMMDD-SEQ`, `trang_thai=MOI`, `don_vi_id=cb_nv_tw_01.don_vi_id` (TW), `muc_do_phuc_tap=THUONG`. (4) Audit log INSERT (BR-DATA-05). | Happy 🔴 |
| TC-HD-002 | FR-II-01 / AC #4 (PHUC_TAP path) | Tạo mới với muc_do_phuc_tap=PHUC_TAP → SLA 30 ngày LV | cb_nv_dp_01 login. CAU_HINH_SLA[HOI_DAP_PHUC_TAP]=30. | noi_dung="Vướng mắc liên ngành...", linh_vuc=Đầu tư, kenh=DVC, muc_do_phuc_tap=PHUC_TAP | 1. Click [+ Thêm mới]. 2. Chọn radio `PHUC_TAP`. 3. Lưu. | (3) Record có `muc_do_phuc_tap=PHUC_TAP`. Sau khi tiếp nhận (FR-II-03), `deadline = ngay_tiep_nhan + 30 ngày LV` theo BR-CALC-03. **Test này verify chỉ tạo + state=MOI**; deadline test ở file 03. | Happy 🔴 |
| TC-HD-003 | FR-II-01 / Processing Chỉnh sửa step 1-4 | Sửa HOI_DAP ở state MOI | cb_nv_tw_01 login. HOI_DAP HD-X tồn tại state MOI. | noi_dung sửa thành "Câu hỏi đã chỉnh sửa", linh_vuc đổi sang "Lao động" | 1. SCR-II-01. 2. Click icon Sửa trên dòng HD-X. 3. Drawer mở pre-fill. 4. Sửa + Lưu. | (1) PUT /hoi-dap/{id} thành công. (3) Danh sách hiển thị nội dung mới. (4) Audit log UPDATE (cũ→mới, BR-DATA-05). | Happy 🔴 |
| TC-HD-004 | FR-II-01 / Processing Xóa step 1-3 | Xóa soft delete HOI_DAP ở state MOI | cb_nv_tw_01 login. HOI_DAP HD-Y state MOI. | — | 1. Click icon Xóa. 2. Confirm dialog. | (1) DELETE thành công (UPDATE is_deleted=1, BR-DATA-01). (2) Toast "Đã xóa". (3) Record biến khỏi danh sách. (4) Audit log DELETE. | Happy 🔴 |
| TC-HD-005 | FR-II-01 / AC #1 + BR-AUTH-08 | Hiển thị danh sách scope đơn vị + phân trang | cb_nv_dp_01 (Sở TP AG) login. ≥25 HOI_DAP thuộc AG, 5 thuộc Sở TP BG. | — | 1. Truy cập SCR-II-01. | (3) Danh sách 20 records/page (BR-DATA-07), CHỈ scope AG (BR-AUTH-08). 5 record BG KHÔNG hiển thị. Pagination footer "Hiển thị 1-20 / 25 kết quả". | Happy 🔴 |
| TC-HD-006 | FR-II-01 / Processing Xuất Excel + AC #7 | Xuất Excel ≤10K rows | cb_nv_tw_01 login. ~50 HOI_DAP thuộc TW. | Filter: Trạng thái=Đang xử lý. | 1. Apply filter. 2. Click [Xuất Excel]. | (1) GET /hoi-dap/export thành công. (2) File `HoiDap_YYYYMMDD_HHmm.xlsx` download. (3) Excel chứa: header in đậm freeze row 1 + data rows + footer (Xuất lúc, Bởi, Filter, Tổng N). 19 cột tiếng Việt theo SRS:153. | Happy 🟡 |
| TC-HD-007 | FR-II-01 / AC #8 | Click "Làm mới" reload AJAX giữ filter | cb_nv_tw_01 login. Filter Lĩnh vực="Đất đai". | — | 1. Apply filter. 2. Scroll giữa trang. 3. Click [Làm mới]. | (1) GET /hoi-dap với cùng query params. (2) Spinner trên nút + bảng giữ stale data. (3) Sau load xong: filter + scroll giữ nguyên. | Happy 🟢 |

---

## B. CRUD HỎI ĐÁP — NEGATIVE

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|---------|--------------|----------------|-----------|-------------------|------------------|------|
| TC-HD-100 | FR-II-01 / E1 ERR-HD-01 | Tạo HOI_DAP nội dung trống | cb_nv_tw_01 login. | noi_dung="" | 1. Click [+ Thêm mới]. 2. Bỏ trống nội dung. 3. Lưu. | (2) Inline error đỏ dưới textarea: **"Nội dung câu hỏi là bắt buộc"** (ERR-HD-01). (3) KHÔNG POST. Form giữ. | Negative 🔴 |
| TC-HD-101 | FR-II-01 / E2 ERR-HD-02 | Tạo HOI_DAP nội dung > 5000 ký | cb_nv_tw_01 login. | noi_dung=5001 ký tự | 1. Paste 5001 ký vào nội dung. 2. Counter `5001/5000` chuyển đỏ. 3. Lưu. | (2) Counter cảnh báo + nút Lưu disabled HOẶC submit → ERR-HD-02 **"Nội dung câu hỏi tối đa 5000 ký tự"**. | Negative 🔴 |
| TC-HD-102 | FR-II-01 / E3 ERR-HD-03 | Tạo với linh_vuc_id invalid (FK đã vô hiệu) | cb_nv_tw_01 login. Linh_vuc "Cổ phần" đã `is_deleted=1`. | linh_vuc_id=Cổ phần (vô hiệu) | 1. Mở dropdown lĩnh vực. 2. Verify Cổ phần không xuất hiện. 3. Force submit qua DevTools. | (2) Backend reject ERR-HD-03 **"Lĩnh vực pháp luật không tồn tại"** (404). | Negative 🟡 |
| TC-HD-103 | FR-II-01 / E4 ERR-HD-04 + BR-FLOW-03 | Sửa HOI_DAP state DA_DUYET → cấm | cb_nv_tw_01 login. HD-Z state DA_DUYET. | noi_dung sửa | 1. Mở chi tiết HD-Z (SCR-II-02). 2. Verify nút Sửa disabled trên row icon. 3. Force PUT API. | (2) UI: nút disabled + tooltip "Không thể sửa: bản ghi đã duyệt/công khai/hoàn thành". (3) API: 403 ERR-HD-04. | Negative 🔴 |
| TC-HD-104 | FR-II-01 / E4 ERR-HD-04 + F-19 | Xóa HOI_DAP state CONG_KHAI → cấm (phải Hủy CK trước) | cb_nv_tw_01 login. HD-W state CONG_KHAI. | — | 1. Click icon Xóa. | (2) Nút Xóa disabled + tooltip "Không thể xóa: bản ghi đã duyệt/công khai/hoàn thành. Cần Hủy công khai (nếu đang ở trạng thái Công khai) rồi đóng hồ sơ". | Negative 🔴 |
| TC-HD-105 | FR-II-01 / E5 WRN-HD-01 | Export > 10,000 rows | cb_nv_tw_01 login. ~12K HOI_DAP scope TW. | — | 1. Click [Xuất Excel]. | (2) Modal warning: **"Hệ thống sẽ xuất 10.000 dòng đầu tiên. Thu hẹp bộ lọc để xuất đầy đủ"** (WRN-HD-01). 2 nút: Hủy / Tiếp tục. (3) Tiếp tục → file 10K + footer cảnh báo "Đã truncate". | Negative 🟡 |
| TC-HD-106 | FR-II-01 / BR-AUTH-08 cross-tenant | cb_nv_dp_02 (BG) attempt access HD-AG | cb_nv_dp_01 tạo HD-AG state MOI. cb_nv_dp_02 login. | URL `/hoi-dap/HD-AG-id` | 1. cb_nv_dp_02 paste URL. | (2) HTTP 404 (IDOR block, BR-AUTH-08). UI: SCR-II-02 dòng 30 — "Hỏi đáp #{id} không tồn tại hoặc đã bị xóa". | Negative 🔴 |

---

## C. CRUD HỎI ĐÁP — EDGE & BOUNDARY

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|---------|--------------|----------------|-----------|-------------------|------------------|------|
| TC-HD-200 | FR-II-01 / Inputs #2 boundary | noi_dung exact 5000 ký (boundary inclusive) | cb_nv_tw_01 login. | noi_dung=5000 ký | 1. Paste 5000 ký. 2. Counter `5000/5000`. 3. Lưu. | (3) Tạo OK. | Edge 🟡 |
| TC-HD-201 | FR-II-01 / Inputs #4-6 | strip emoji + control chars trong ten_nguoi_gui | cb_nv_tw_01 login. | ten_nguoi_gui="Nguyễn Văn A 😀​" | 1. Nhập tên có emoji + zero-width char. 2. Lưu. | (3) BE silent strip → save "Nguyễn Văn A". KHÔNG cảnh báo (F-33). | Edge 🟢 |
| TC-HD-202 | FR-II-01 / Inputs #5 | Email invalid format inline | cb_nv_tw_01 login. | email="abc.invalid@@" | 1. Nhập email invalid. 2. Blur. | (2) Inline error: "Email không đúng định dạng" (RFC 5322). | Edge 🟢 |
| TC-HD-203 | FR-II-01 / Inputs #6 | SDT 9 ký tự (under boundary) | cb_nv_tw_01 login. | sdt="012345678" | 1. Nhập 9 ký tự. 2. Blur. | (2) Inline error: "Số điện thoại phải có 10-11 chữ số". | Edge 🟢 |
| TC-HD-204 | FR-II-01 / Inputs #8 | TVN_BRIDGE auto-set, không cho user nhập tay | cb_nv_tw_01 login. | — | 1. Mở Form Thêm mới. 2. Verify dropdown Kênh tiếp nhận chỉ có 4 options (DVC/CONG_PLQG/TRUC_TIEP/HE_THONG_KHAC). | (2) TVN_BRIDGE KHÔNG hiển thị trong dropdown (auto-set khi escalate từ FR-13). | Edge 🟡 |
| TC-HD-205 | FR-II-01 / Inputs #9 ClamAV | Upload file virus (EICAR test) | cb_nv_tw_01 login. ClamAV OK. | file=eicar.com.txt | 1. Drag drop EICAR test file. 2. Verify spinner ClamAV. | (2) File reject + toast "Tệp 'eicar.com.txt' chứa mã độc hoặc không quét được, đã bị từ chối". | Edge 🟡 |
| TC-HD-206 | FR-II-01 / Inputs #9 boundary | Upload 11 file (vượt limit 10) | cb_nv_tw_01 login. | 11 files .pdf | 1. Select 11 files. | (2) Reject file thứ 11 + toast "Tối đa 10 file/lần upload". | Edge 🟢 |
| TC-HD-207 | FR-II-01 / Inputs #9 boundary | Upload file 21MB (>20MB limit) | cb_nv_tw_01 login. | 1 file .pdf 21MB | 1. Select file. | (2) Reject + toast "Tệp tối đa 20MB". | Edge 🟢 |
| TC-HD-208 | FR-II-01 / Inputs #9 zero-byte | Upload file 0 byte | cb_nv_tw_01 login. | 1 file .pdf 0 byte | 1. Select file. | (2) Reject + toast "Tệp '{name}' trống, không hợp lệ". | Edge 🟢 |
| TC-HD-209 | FR-II-01 / SCR-II-01 row 30a | Trạng thái lỗi API (network timeout) | cb_nv_tw_01 login. Mock backend trả 503. | — | 1. Reload SCR-II-01. | (2) Error block: ⚠️ "Không tải được danh sách hỏi đáp" + "Thử lại" + "Về trang chủ". | Edge 🟡 |
| TC-HD-210 | FR-II-01 / SCR-II-01 row 30 variant 4 | Empty state filter không khớp | cb_nv_tw_01 login. | Filter Lĩnh vực="Hôn nhân & Gia đình" (không có data) | 1. Apply filter. | (2) Empty state: "Không tìm thấy hỏi đáp phù hợp với bộ lọc. [Xóa bộ lọc]" + nút reset. | Edge 🟢 |
| TC-HD-211 | FR-II-01 / Excel structure | Excel header + footer đúng SRS:153 | cb_nv_tw_01 login. ≥5 HOI_DAP. | — | 1. Click [Xuất Excel]. 2. Mở file. | (3) Header 19 cột tiếng Việt theo SRS:153. Footer 4 dòng: "Xuất lúc...", "Bởi: {ho_ten} ({username}) — Đơn vị: {ten_dv}", "Bộ lọc áp dụng: ...", "Tổng số bản ghi: N". Datetime `dd/mm/yyyy HH:mm`, enum trạng thái tiếng Việt mapping. | Edge 🟡 |

---

## D. BATCH XÓA HÀNG LOẠT (action-bar dòng 33)

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|---------|--------------|----------------|-----------|-------------------|------------------|------|
| TC-HD-220 | FR-II-01 / Batch xóa happy | Xóa hàng loạt 5 record state hợp lệ | cb_nv_tw_01 login. 5 HD state MOI/TIEP_NHAN scope TW. | — | 1. Tab "Tất cả". 2. Tick 5 checkboxes. 3. Click [Xóa hàng loạt] action-bar. 4. Confirm. | (1) DELETE batch per-record. (2) Modal "Đã xử lý 5 bản ghi: thành công 5, lỗi 0". (3) 5 records biến khỏi danh sách. Audit log 5 entries. | Happy 🔴 |
| TC-HD-221 | FR-II-01 / E6 ERR-DELETE-STATE batch | Batch xóa lẫn state cấm | cb_nv_tw_01 login. 3 record MOI + 2 record DA_DUYET. | — | 1. Tick 5 checkboxes (3 MOI + 2 DA_DUYET). 2. [Xóa hàng loạt]. | (2) Modal report: "Thành công 3 (MOI), lỗi 2: ERR-DELETE-STATE — Bản ghi #{ma} ở trạng thái 'Đã duyệt' không thể xóa". | Negative 🔴 |
| TC-HD-222 | FR-II-01 / E7 ERR-AUTH-DEL batch | Batch xóa khác đơn vị | cb_nv_dp_01 (AG). qtht_01 force list cross-tenant 5 record (3 AG + 2 BG). | URL chứa cross-tenant IDs | 1. Force batch DELETE 5 IDs. | (2) Report: "Thành công 3 (AG), lỗi 2: ERR-AUTH-DEL — Không có quyền xóa bản ghi #{ma} (thuộc đơn vị khác)". | Negative 🟡 |
| TC-HD-223 | FR-II-01 / E8 ERR-BATCH-CONFLICT | Concurrent edit giữa chừng batch | cb_nv_tw_01 + cb_nv_tw_02 cùng login. cb_nv_tw_01 chọn 3 records để xóa. | — | 1. cb_nv_tw_01 tick 3 records. 2. cb_nv_tw_02 sửa 1 record giữa chừng (UPDATE version). 3. cb_nv_tw_01 click [Xóa hàng loạt]. | (2) Report: "Thành công 2, skip 1: ERR-BATCH-CONFLICT — Bản ghi #{ma} đã được {cb_nv_tw_02} cập nhật lúc {time}, đã skip trong batch. Vui lòng tải lại danh sách và thử lại". | Negative 🟡 |

---

---

## E. EDGE BỔ SUNG (A4 merged 2026-05-10)

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|---------|--------------|----------------|-----------|-------------------|------------------|------|
| TC-HD-230 | FR-II-01 / Inputs #7 + SCR-II-01 row 43 | Tạo HD với DN đã `is_deleted=1` (force qua API) | cb_nv_tw_01 login. DOANH_NGHIEP DN-VOHIEU đã soft-deleted. | doanh_nghiep_id=DN-VOHIEU (force) | 1. Form Thêm mới. 2. Dropdown DN KHÔNG hiển thị DN-VOHIEU. 3. Force POST API với DN-VOHIEU. | (2) Backend reject (FK DN trỏ vô hiệu). Hoặc accept với cảnh báo (SPEC-CLARIFY-HD-04 verify). Tag (DN đã vô hiệu) hiển thị edit record cũ. | Edge 🟡 |
| TC-HD-231 | FR-II-01 / BR-DATA-04 race | Auto-gen mã `HD-YYYYMMDD-SEQ` race 2 tab CREATE đồng thời | cb_nv_tw_01 mở 2 tab SCR-II-01 cùng ngày. | Tab1 + Tab2 cùng noi_dung, cùng don_vi_id | 1. Tab1 fill + Submit (delay backend giả lập). 2. Tab2 fill + Submit trước khi Tab1 response. | (3) UNIQUE constraint per ma_hoi_dap → 2 record, mã khác nhau (SEQ tăng monotonic). Audit log 2 INSERT. | Edge 🟡 |
| TC-HD-232 | FR-II-01 / UX browser back | Browser back sau khi Lưu drawer | cb_nv_tw_01 vừa tạo HD-NEW thành công. | — | 1. Sau toast success, click Browser Back. | (3) Behavior verify: hoặc về SCR-II-01 (preserved state) hoặc empty drawer. Verify URL state. | Edge 🟢 |
| TC-HD-233 | FR-II-01 / Inputs #2 / SPEC-CLARIFY-HD-04 | Whitespace trim noi_dung leading/trailing | cb_nv_tw_01 login. | noi_dung=`"  Câu hỏi với khoảng trắng đầu/cuối  "` | 1. Paste có whitespace. 2. Lưu. | (3) BE behavior: (a) trim → save "Câu hỏi..." hoặc (b) giữ nguyên. **SPEC-CLARIFY-HD-04**. | Edge 🟢 |
| TC-HD-234 | FR-II-01 / EC-03 batch full conflict | Batch DELETE 100 records ALL conflict | cb_nv_tw_01 + cb_nv_tw_02 cùng login. cb_nv_tw_02 sửa toàn bộ 100 records giữa chừng. | — | 1. cb_nv_tw_01 batch DELETE 100. | (2) Report 100 ERR-BATCH-CONFLICT. 0 thành công. UI hiển thị danh sách 100 entries. | Edge 🟡 |
| TC-HD-235 | FR-II-01 / SCR-II-01 dòng 4 + 29a | Refresh button trong khi filter đang load (concurrent) | cb_nv_tw_01 login. ≥50 records. | — | 1. Apply filter heavy (fake delay). 2. Click [Làm mới] giữa lúc loading. | (3) Cancel previous request hoặc queue. Bảng cuối cùng hiển thị data của request thứ 2. KHÔNG hiển thị data cũ + mới mix. | Edge 🟢 |
| TC-HD-236 | FR-II-01 / SM transition #3 MOI → HUY (GAP-A5-03 fix) | Hủy yêu cầu HD ở state MOI | cb_nv_tw_01 login. HD-NEW state MOI, chưa có PHAN_HOI. | ly_do_huy="Yêu cầu trùng với HD-X cũ" (28 ký) | 1. SCR-II-02 HD-NEW. 2. Click [Hủy yêu cầu] dòng 12. 3. C12 confirm. 4. Textarea ly_do_huy counter `{n}/1000`. 5. Submit. | (1) PUT /hoi-dap/{id}/huy thành công. (3) HD: `trang_thai=HUY`, `thoi_gian_huy=NOW()`, `nguoi_huy_id=cb_nv_tw_01`, `ly_do_huy=...`. (4) Audit log action='HUY'. SCR-II-02 reload với banner F-24 "🚫 Đã hủy". | Happy 🔴 (SM-coverage) |
| TC-HD-237 | FR-II-01 / Permission CB_PD CREATE (GAP-A5-04 fix) | CB_PD attempt tạo HOI_DAP | cb_pd_tw_01 login. | — | 1. Mở SCR-II-01. | (2) Nút [+ Thêm mới] KHÔNG hiển thị (chỉ CB_NV cùng đơn vị có quyền HOI_DAP_CREATE). Force POST API → 403. | Negative 🟡 |
| TC-HD-238 | FR-II-01 / Permission DN/GV (GAP-A5-05 fix) | DN attempt access HOI_DAP module | dn_01 login. | URL `/hoi-dap/danh-sach` | 1. Paste URL. | (2) HTTP 403 hoặc redirect về Dashboard. Module HOI_DAP block toàn bộ DN/GV/NHT-non-assigned. | Negative 🟡 |

---

## Tổng kết file 01

- **Tổng số TC: 32** (7 Happy + 7 Negative + 12 Edge C/D + 6 A4 merged + 3 A6 GAP fix = 35... wait, recount: 7+7+12+6+3 = 35)

Actual count: A=7, B=7, C=12, D=4, E=9 → **39 TC**.

- **Critical TC (🔴)**: TC-HD-001, 002, 003, 004, 005, 100, 101, 103, 104, 106, 220, 221, 236
- **Coverage**: BR-AUTH-01/05/08 (✅), BR-DATA-01/04/05/06/07 (✅), BR-FLOW-03 (✅), SM transition `MOI → HUY` (✅ TC-236 fix GAP-A5-03), Permission CB_NV/CB_PD/DN (✅ TC-237/238 fix GAP-A5-04/05)
- **Error codes covered**: ERR-HD-01, 02, 03, 04, WRN-HD-01, ERR-DELETE-STATE, ERR-AUTH-DEL, ERR-BATCH-CONFLICT
- **A4 merged 2026-05-10**: TC-HD-230..235 (6 TC). SPEC-CLARIFY-HD-04 (whitespace trim).
- **A6 merged 2026-05-10**: TC-HD-236..238 (3 TC fix GAP).

*Generated 2026-05-10 — Phase A step A3 + A4 inline merge + A6 GAP fix*
