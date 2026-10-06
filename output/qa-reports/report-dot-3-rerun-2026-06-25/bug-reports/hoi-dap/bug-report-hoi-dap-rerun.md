# Bug Report — Hỏi đáp pháp lý (FR-02) — rerun report-dot-3

| Thông tin | Giá trị |
|-----------|---------|
| **Dự án** | PM HTPLDN |
| **Môi trường** | http://103.172.236.130:3000 |
| **Người test** | QA Automation (Chrome DevTools MCP) |
| **Ngày** | 2026-06-25 21:20:00 |
| **Loại test** | Functional / Negative / UI-UX (rerun CHƯA CHẠY batch 1) |
| **Round** | rerun report-dot-3 — batch 1 |
| **Tài liệu tham chiếu** | `input/srs-update-2026-5-5/srs-fr-02-hoi-dap.md` · `output/bao-cao-tong-hop-qa/report-dot-3.xlsx` sheet "03. Hỏi đáp pháp lý" |

---

## Tổng hợp

Phát hiện **7** lỗi còn Open sau rerun module Hỏi đáp pháp lý. 15 testcase FAIL hiện gom về 7 bug gốc.

### Severity breakdown

| Tổng | Critical | Major | Medium | Minor | Trivial | Closed | Open |
|------|----------|-------|--------|-------|---------|--------|------|
| 7    | 0        | 0     | 3      | 4     | 0       | 0      | 7    |

## Bug Summary Table

| Bug ID | Severity | Priority | Type | TC Ref | **SRS Reference** | Title | Status |
|--------|----------|----------|------|--------|-------------------|-------|--------|
| BUG-HD-RR-001 | Medium | P2 | Data | TC-HD-201 | `srs-fr-02-hoi-dap.md:1073` (SCR-II-01 row 40) + F-16/F-33 | `ten_nguoi_gui` không loại bỏ emoji / zero-width / control chars trước khi lưu (cả UI form lẫn API) | Open |
| BUG-HD-RR-002 | Minor | P3 | UI/UX | TC-HDTK-101, TC-HD-210, TC-PD-061 | `srs-fr-02-hoi-dap.md:1057` (SCR-II-01 row 30, F-27) + TC-PD-061 | Trạng thái rỗng hiển thị "Trống" mặc định, không phải empty-state context-aware theo spec | Open |
| BUG-HD-RR-003 | Minor | P3 | Negative | TC-TN-203 | `srs-fr-02-hoi-dap.md:19` (F-14/15 counter `{n}/1000`) | `ghi_chu_tiep_nhan` 1001 ký tự được Backend chấp nhận (201), không enforce giới hạn 1000 ký phía server | Open |
| BUG-HD-RR-004 | Minor | P3 | UI/UX | TC-DXL-110/111/112/113/208 | `srs-fr-02-hoi-dap.md:19` (F-02 nút "Đổi mức độ phức tạp" SCR-II-02) | Không tìm thấy endpoint API "Đổi mức độ phức tạp"; PATCH bỏ qua `mucDoPhucTap` → tính năng F-02 chưa wiring | Open |
| BUG-HD-RR-005 | Minor | P3 | Export | TC-HD-211 | `srs-fr-02-hoi-dap.md:154-166` | Export Excel chỉ có 11 cột và không có footer 4 dòng metadata, sai cấu trúc SRS 19 cột + footer | Open |
| BUG-HD-RR-006 | Medium | P2 | Permission/Workflow | TC-PD-030 | `report-dot-3.xlsx` TC-PD-030 + BR-FLOW-03 | CB_NV cùng đơn vị mở được DA_DUYET nhưng không đóng hồ sơ được, API trả 403 Forbidden | Open |
| BUG-HD-RR-007 | Medium | P2 | Upload/Validation | TC-HD-206/207/208 | `report-dot-3.xlsx` TC-HD-206/207/208 | Upload file không enforce đúng validation/toast: 11 file redirect login, 21MB thiếu toast, 0 byte được nhận | Open |

---

## BUG-HD-RR-001 — Tên người gửi giữ nguyên emoji + zero-width khi lưu (không strip theo F-33)

### Mô tả

Theo SRS, trường "Tên người gửi" phải loại bỏ emoji + control chars + zero-width chars trước khi lưu (silent strip). Khi tạo hỏi đáp với tên người gửi chứa emoji, hệ thống lưu nguyên ký tự emoji + zero-width — không strip. Tái hiện ở cả 2 đường: nhập qua form UI (role CB_NV_TW có quyền HOI_DAP_CREATE) và gọi API trực tiếp.

### Các bước tái hiện

1. Đăng nhập `cb_nv_tw_01` (CB_NV_TW, có quyền tạo hỏi đáp theo SCR-II-01).
2. Mở màn Hỏi đáp pháp lý → "Thêm mới".
3. Nhập Nội dung hợp lệ (≥20 ký), chọn Lĩnh vực "Lao động", Kênh "Trực tiếp".
4. Trường "Tên người gửi" nhập: `Nguyễn Văn B 😀<zero-width>🎉`.
5. Bấm "Lưu" → tạo thành công (HD-20260625-008).
6. GET lại bản ghi → kiểm tra `tenNguoiGui` đã lưu.

### Kết quả mong đợi

Theo `srs-fr-02-hoi-dap.md:1073` (SCR-II-01 row 40): *"...loại bỏ emoji + control chars + zero-width chars trước khi save (silent strip, không cảnh báo). Sau strip nếu rỗng → coi là null. Ref F-33"*. Tên lưu phải là `Nguyễn Văn B` (đã strip).

### Kết quả thực tế

`tenNguoiGui` lưu = `Nguyễn Văn B 😀​🎉` — code points gồm `1f600` (😀), `200b` (zero-width space), `1f389` (🎉) vẫn còn nguyên. Không strip ở cả FE lẫn BE. Đường API trực tiếp (HD-20260625-002) cũng cho kết quả tương tự.

### Bằng chứng

- Form UI tạo HD-20260625-008, GET trả `tenNguoiGui` code points `["4e","67","75","79","1ec5","6e","20","56","103","6e","20","42","20","1f600","200b","1f389"]`.
- API POST HD-20260625-002 trả `"tenNguoiGui":"Nguyễn Văn A 😀​"`.

---

## BUG-HD-RR-002 — Trạng thái rỗng dùng empty mặc định, thiếu context-aware 5 variant (F-27)

### Mô tả

Theo SRS, bảng danh sách hỏi đáp có các trạng thái rỗng context-aware (theo tab + quyền + filter). Thực tế khi tìm kiếm/lọc không khớp hoặc vào tab Hoàn thành không có dữ liệu, bảng chỉ hiển thị empty mặc định của thư viện UI (ảnh + chữ "Trống"), không có thông điệp theo ngữ cảnh.

### Các bước tái hiện

1. Đăng nhập `cb_nv_tw_01` → màn Hỏi đáp pháp lý.
2. Nhập từ khoá vô nghĩa `xyzkhongton` vào ô tìm kiếm → "Tìm kiếm" (hoặc lọc Lĩnh vực không có dữ liệu).
3. Quan sát vùng bảng khi 0 kết quả.
4. Đăng nhập `cb_nv_dp_01` → tab `Hoàn thành` trong bối cảnh không có HD hoàn thành.

### Kết quả mong đợi

Theo `srs-fr-02-hoi-dap.md:1057` (SCR-II-01 row 30, ref F-27), variant 4: *"Tìm kiếm/bộ lọc không khớp: 'Không tìm thấy hỏi đáp phù hợp với bộ lọc. [Xóa bộ lọc]' (nút reset)"*. Với TC-PD-061, tab Hoàn thành rỗng phải hiển thị: "Chưa có hỏi đáp nào đã xử lý".

### Kết quả thực tế

Vùng bảng chỉ hiển thị empty mặc định: ảnh placeholder + mô tả "Trống". Không có thông điệp "Không tìm thấy hỏi đáp phù hợp với bộ lọc", không có nút reset inline trong empty-state (chỉ có nút "Xóa bộ lọc" ở thanh filter phía trên). Tab Hoàn thành rỗng cũng chỉ hiển thị "Trống", thiếu "Chưa có hỏi đáp nào đã xử lý".

### Bằng chứng

- DOM `.ant-empty-description` = "Trống"; không có node chứa text "Không tìm thấy".
- Ảnh: `image/tc-hdtk-101-emptystate-generic.png`.
- Ảnh: `functional/hoi-dap/ui-pd061-hoan-thanh-empty-20260626.png`.

---

## BUG-HD-RR-003 — ghi_chu_tiep_nhan vượt 1000 ký tự được Backend chấp nhận

### Mô tả

Khi tiếp nhận hỏi đáp, trường `ghiChuTiepNhan` với 1001 ký tự được Backend chấp nhận (HTTP 201, chuyển trạng thái TIEP_NHAN thành công), không enforce giới hạn 1000 ký tự ở phía server. Đối chiếu: trường `lyDo` của cập nhật thời hạn lại enforce đúng max 500 (422), nên đây là gap riêng của ghi_chu_tiep_nhan.

### Các bước tái hiện

1. Đăng nhập `cb_nv_tw_01`, tạo 1 hỏi đáp (state MOI).
2. Gọi tiếp nhận với `ghiChuTiepNhan` = chuỗi 1001 ký tự + version hợp lệ.
3. Quan sát kết quả.

### Kết quả mong đợi

Theo F-14/15 (counter `{n}/1000` cho ghi_chu_tiep_nhan), nội dung vượt 1000 ký tự phải bị từ chối (hoặc cắt) — server không nên lưu quá 1000 ký.

### Kết quả thực tế

POST tiếp nhận với 1001 ký tự → HTTP 201, state = TIEP_NHAN. Trong khi đó 1000 ký tự cũng 201 (đúng). Không có ràng buộc max 1000 phía server (có thể chỉ có counter FE).

### Bằng chứng

- TC-TN-202 (1000 ký): 201 TIEP_NHAN. TC-TN-203 (1001 ký): 201 TIEP_NHAN (lẽ ra phải 422).

---

## BUG-HD-RR-004 — Không tìm thấy cơ chế "Đổi mức độ phức tạp" qua API

### Mô tả

Tính năng "Đổi mức độ phức tạp" (F-02, nút trên SCR-II-02, dùng để chuyển THUONG ↔ PHUC_TAP và tính lại deadline) không có endpoint API tương ứng qua dò tìm, và PATCH `/hoi-daps/{id}` bỏ qua field `mucDoPhucTap` (trả 200 nhưng mức độ không đổi). Nhóm TC-DXL-110/111/112/113/208 được xác nhận FAIL bằng evidence API.

### Các bước tái hiện

1. Đăng nhập `cb_nv_tw_01`, walk 1 hỏi đáp tới TIEP_NHAN/DANG_XU_LY.
2. Thử PATCH `/hoi-daps/{id}` với `{mucDoPhucTap:'PHUC_TAP', version}`.
3. Thử các endpoint: `doi-muc-do`, `doi-muc-do-phuc-tap`, `cap-nhat-muc-do`, `thay-doi-muc-do`, `muc-do-phuc-tap`...

### Kết quả mong đợi

Theo F-02, phải có cơ chế đổi mức độ phức tạp → cập nhật `muc_do_phuc_tap` + tính lại deadline (THUONG↔PHUC_TAP, +30/-15 ngày LV theo TC-DXL-110/111), có state guard và validation lý do theo TC-DXL-112/113/208.

### Kết quả thực tế

PATCH với `mucDoPhucTap` → 200 nhưng `mucDoPhucTap` giữ nguyên THUONG, deadline không đổi. Các biến thể endpoint đổi-mức-độ đều 404 ("Cannot POST"). Không drive được mức độ qua API nên các case đổi mức độ FAIL.

### Bằng chứng

- PATCH `mucDoPhucTap=PHUC_TAP` trên HD-20260625-049 → 200, response và GET sau đó vẫn `mucDoPhucTap="THUONG"`, version không đổi.
- Endpoint probes `doi-muc-do`, `doi-muc-do-phuc-tap`, `cap-nhat-muc-do`, `thay-doi-muc-do`, `muc-do-phuc-tap` → 404 `ERR-SYS-00-04-01`.
- Evidence: `functional/hoi-dap/remaining-actions-20260626.json`, `functional/hoi-dap/remaining-actions-2-20260626.json`.

---

## BUG-HD-RR-005 — Export Excel thiếu 19 cột + footer metadata theo SRS

### Mô tả

TC-HD-211 yêu cầu file export Excel có header 19 cột tiếng Việt theo SRS và footer 4 dòng metadata cuối file. Khi tải export thật từ `/api/v1/hoi-daps/export`, workbook chỉ có 11 cột dữ liệu và không có các dòng footer "Xuất lúc", "Bởi", "Bộ lọc áp dụng", "Tổng số bản ghi".

### Các bước tái hiện

1. Đăng nhập `cb_nv_tw_01`.
2. Mở module Hỏi đáp pháp lý.
3. Click hoặc gọi luồng export `/api/v1/hoi-daps/export`.
4. Mở file `.xlsx` tải về và kiểm tra sheet đầu tiên.

### Kết quả mong đợi

Theo `srs-fr-02-hoi-dap.md:154-166`, file export phải có 19 cột theo thứ tự: Số thứ tự, Mã hỏi đáp, Tiêu đề, Nội dung đầy đủ, Lĩnh vực pháp luật, Người gửi, Email, Số điện thoại, Doanh nghiệp, Kênh tiếp nhận, Trạng thái, Đơn vị tiếp nhận, Ngày tạo, Ngày tiếp nhận, Hạn xử lý, Mức thời hạn xử lý, Người xử lý, Người duyệt, Ngày duyệt. Cuối file phải có footer 4 dòng metadata.

### Kết quả thực tế

Workbook `Hỏi đáp` có 90 dòng x 11 cột. Header thực tế: `Mã hỏi đáp`, `Trích yếu`, `Lĩnh vực`, `Kênh tiếp nhận`, `Người gửi`, `Người xử lý`, `Trạng thái`, `Mức độ cảnh báo`, `Ngày tiếp nhận`, `Deadline`, `Ngày tạo`. Không có footer metadata ở các dòng cuối.

### Bằng chứng

- File evidence: `functional/hoi-dap/export-hoi-dap-ui-batch.xlsx`.
- JSON parse: `functional/hoi-dap/export-hoi-dap-ui-batch-evidence.json`.

---

## BUG-HD-RR-006 — CB_NV cùng đơn vị không đóng được hồ sơ DA_DUYET

### Mô tả

TC-PD-030 yêu cầu CB_NV cùng đơn vị đóng hồ sơ ở trạng thái `DA_DUYET` sang `HOAN_THANH`. Thực tế `cb_nv_dp_01` đăng nhập thành công, GET được record `HD-QA-R7-064` trạng thái `DA_DUYET` thuộc AG, nhưng gọi `POST /hoi-daps/{id}/dong-ho-so` trả 403 `ERR-PERM-SYS-00-01`.

### Các bước tái hiện

1. Đăng nhập `cb_nv_dp_01`.
2. GET `/api/v1/hoi-daps/aa064064-0000-4000-8000-000000000064` → record `DA_DUYET`, version `1`.
3. POST `/api/v1/hoi-daps/aa064064-0000-4000-8000-000000000064/dong-ho-so` với `{version:1}`.
4. GET lại record.

### Kết quả mong đợi

Theo TC-PD-030, thao tác đóng hồ sơ thành công: `trang_thai=HOAN_THANH`, `ngay_hoan_thanh=NOW()`, audit log action `DONG_HO_SO`.

### Kết quả thực tế

API trả HTTP 403 `ERR-PERM-SYS-00-01` `"Forbidden"`. GET sau đó vẫn `trangThai="DA_DUYET"`, `ngayHoanThanh=null`.

### Bằng chứng

- Evidence: `functional/hoi-dap/pd030-close-cbnvdp-20260626.json`.

---

## BUG-HD-RR-007 — Upload file không enforce đúng validation/toast

### Mô tả

Nhóm TC-HD-206/207/208 yêu cầu upload file đính kèm phải reject đúng boundary và hiển thị toast rõ ràng. Khi kiểm thử qua drawer "Thêm mới hỏi đáp", UI không đáp ứng đúng: 11 file làm app redirect về `/login`, file 21MB bị loại nhưng không có toast, file 0 byte lại được thêm vào file-list.

### Các bước tái hiện

1. Đăng nhập UI `cb_nv_dp_01` → Hỏi đáp pháp lý → "Thêm mới".
2. Với TC-HD-207, chọn file `.pdf` 21MB.
3. Với TC-HD-208, chọn file `.pdf` 0 byte.
4. Mở lại form sạch, với TC-HD-206 chọn 11 file `.pdf` nhỏ.

### Kết quả mong đợi

- TC-HD-206: Reject file thứ 11 + toast "Tối đa 10 file/lần upload".
- TC-HD-207: Reject + toast "Tệp tối đa 20MB".
- TC-HD-208: Reject + toast "Tệp '{name}' trống, không hợp lệ".

### Kết quả thực tế

- TC-HD-206: Sau khi chọn 11 file, app redirect về `/login`, không có toast giới hạn 10 file.
- TC-HD-207: File 21MB không xuất hiện trong file-list nhưng cũng không có toast "Tệp tối đa 20MB".
- TC-HD-208: File `hd-empty.pdf` được nhận vào file-list, không reject và không có toast file rỗng.

### Bằng chứng

- `functional/hoi-dap/ui-hd206-11files-redirect-login-20260626.png`
- `functional/hoi-dap/ui-hd207-21mb-no-toast-20260626.png`
- `functional/hoi-dap/ui-hd208-zero-byte-accepted-20260626.png`
