# Test Cases — UC150: Quản lý hồ sơ pháp lý DN (FR-X.1-04)

> **SRS Ref:** FR-X.1-04 / UC150 — `srs-fr-12-tv-chuyen-sau-v3.1.md` line 513-672
> **Entity:** HO_SO_PHAP_LY_DN (HSPL)
> **Màn hình:** Tab "Hồ sơ PL" trong MH-07.2 chi tiết DN (FR-07) — KHÔNG có màn hình riêng (line 519 — SCR-X1-03 deprecated v2.1)
> **Ngày tạo:** 2026-05-06
> **Owner:** QA Automation Lead
> **Phase:** A3 (test-design generate)
> **Tài khoản test:** `input/users.csv` — cb_nv_tw_01, cb_nv_bn_01 (BKH), cb_nv_dp_01 (AG), cb_nv_dp_02 (BG), nht_01 (AG), tvv_01

---

## Phạm vi file

CRUD hồ sơ pháp lý DN trong tab "Hồ sơ PL" của MH-07.2 (chi tiết DN). Cover Happy/Negative/Edge/UI Verify cho:
- UI Verify Toolbar + Table 11 cột.
- CRUD HSPL (CREATE auto-gen mã / READ chi tiết / UPDATE / DELETE soft) + Export Excel.
- Tìm kiếm 5 filter AND logic.
- Negative ERR-HSPL-01..06 (line 652-658).
- Permission NHT BR-AUTH-10 (line 669-671) + BR-AUTH-08 multi-tenant (line 1531-1535).

> ⚠️ **Active bug baseline:** Phase A vẫn viết TC theo SRS spec đầy đủ; Phase B verify khi có bug action-bar HSPL phát sinh.

---

## Section A — UI Verify (BẮT BUỘC chạy trước functional)

### TC-HSPL-001 — Verify tab "Hồ sơ PL" trong MH-07.2: Toolbar + Table 11 cột + 3 trạng thái

- **TraceID:** FR-X.1-04 / SRS line 519, 626-640 (Outputs danh sách) / SCR MH-07.2 tab "Hồ sơ PL"
- **Type:** UI Verify (Happy)
- **Priority:** P0 🔴
- **Pre-conditions:**
  - cb_nv_tw_01 đã đăng nhập (BR-AUTH-01).
  - DN "DN-TW-001" tồn tại + có ≥3 HSPL (cover 3 trạng thái HIEU_LUC/HET_HAN/THU_HOI) + ≥1 HSPL có file đính kèm.
- **Test Data:** URL `/doanh-nghiep/{DN-TW-001-id}` → tab "Hồ sơ PL".
- **Steps:**
  1. Đăng nhập cb_nv_tw_01.
  2. Navigate menu "Doanh nghiệp > DN-TW-001 chi tiết" → mở MH-07.2.
  3. Click tab "Hồ sơ PL".
  4. Quan sát toolbar + table + filter-bar.
- **Expected:**
  - **Toolbar:** Có button [+ Thêm hồ sơ] (theo line 532-547 form CRUD).
  - **Filter-bar 5 ô:** Tìm kiếm keyword / Loại HS (5 enum GIAY_PHEP/HOP_DONG/GIAY_CN/QUYET_DINH/KHAC) / DN (auto-fill DN hiện tại nếu mở từ chi tiết DN, hoặc để chọn) / Khoảng ngày tu_ngay/den_ngay / Trạng thái (HIEU_LUC/HET_HAN/THU_HOI). Verify line 550-556.
  - **Table 11 cột** (line 626-640): Mã HS / Tên HS / Tên DN / Loại / Ngày cấp dd/mm/yyyy / Ngày hết hạn dd/mm/yyyy / Trạng thái badge 3 màu (HIEU_LUC=xanh, HET_HAN=cam, THU_HOI=đỏ) / Có file (icon) / Ngày tạo dd/mm/yyyy HH:mm / Hành động (Xem/Sửa/Xóa icon).
  - **Pagination:** Default 20/page (BR-DATA-07 line 1561-1565).
  - **Empty state** (nếu không có HSPL): "Chưa có hồ sơ pháp lý. [+ Thêm hồ sơ]".
- **SRS ref:** line 519 (deprecate SCR riêng), line 532-547 (Inputs CRUD), line 550-556 (Inputs Search), line 626-640 (Outputs).
- **Notes:** SPEC-CLARIFY-HSPL-UI-01 — SRS không quote nguyên văn cấu trúc tab MH-07.2 layout chi tiết "Hồ sơ PL" → assumption: render giống pattern CRUD chuẩn FR-07. Verify khi B-Run.

---

## Section B — CRUD HSPL + Export Excel

### TC-HSPL-002 — CREATE HSPL thành công với đầy đủ thông tin + auto-gen mã `HSPL-{YYYYMMDD}-{SEQ}`

- **TraceID:** FR-X.1-04 / BR-DATA-04 (line 1549-1553) / SRS line 568-577
- **Type:** Happy
- **Priority:** P0 🔴
- **Pre-conditions:**
  - cb_nv_tw_01 đăng nhập.
  - DN "DN-TW-001" tồn tại trong cùng đơn vị BTP-TW.
  - Lĩnh vực "DAN_SU" tồn tại trong DANH_MUC.
- **Test Data:**
  - doanh_nghiep_id=DN-TW-001
  - ten_ho_so="Giấy phép kinh doanh DN ABC 2026"
  - loai_ho_so=GIAY_PHEP
  - linh_vuc_id=DAN_SU
  - ngay_cap=2026-01-15, ngay_het_han=2031-01-15
  - co_quan_cap="Sở Kế hoạch Đầu tư TP.HCM"
  - mo_ta="Giấy phép kinh doanh ngành tư vấn pháp lý"
  - trang_thai=HIEU_LUC (default)
  - file_dinh_kem=giay-phep.pdf (5MB)
- **Steps:**
  1. Tab "Hồ sơ PL" → click [+ Thêm hồ sơ].
  2. Form modal/page mở → điền 10 field theo Test Data.
  3. Upload file 5MB PDF → tên file hiển thị.
  4. Click [Lưu].
- **Expected:**
  - **STATE:** INSERT HO_SO_PHAP_LY_DN với `ma_ho_so` match regex `^HSPL-20260506-\d+$` (auto-gen theo BR-DATA-04 + SRS line 574). 7 common fields BR-DATA-03 (id, created_at, updated_at, created_by=cb_nv_tw_01, updated_by, is_deleted=0, don_vi_id=BTP-TW). INSERT FILE_DINH_KEM linked, ClamAV scan PASS (BR-EC-03).
  - **AUDIT_LOG:** hanh_dong='CREATE', entity='HO_SO_PHAP_LY_DN' (BR-DATA-05 line 1555-1559).
  - **UI:** Toast "Thêm hồ sơ pháp lý thành công" (SRS Gap message — SPEC-CLARIFY-HSPL-MSG-01). Form đóng, tab "Hồ sơ PL" reload → record mới ở đầu list với mã `HSPL-20260506-...`, badge "HIEU_LUC" xanh, icon "có file".
  - **PERSIST:** Reload page → record vẫn xuất hiện. Click [Xem] → modal/page chi tiết hiển thị 11 field + danh sách file đính kèm 1 mục.
- **SRS ref:** line 568-577 (Processing Thêm mới), line 1549-1553 (BR-DATA-04 mã auto-gen).
- **Notes:** A7 GIỮ — verify qua `list_network_requests` capture POST `/api/v1/ho-so-phap-ly-dn` response chứa 7 common fields + ma_ho_so regex; verify ClamAV PASS qua HTTP 200 (không query DB). Multipart/form-data file upload qua UI form.

### TC-HSPL-003 — READ chi tiết HSPL: full record + DN liên kết + danh sách file

- **TraceID:** FR-X.1-04 / SRS line 606-614 (Processing Xem chi tiết — `[GAP-X.1-05]`)
- **Type:** Happy
- **Priority:** P0 🔴
- **Pre-conditions:** cb_nv_tw_01 đăng nhập. HSPL "HSPL-20260101-001" thuộc DN-TW-001 + có 2 file đính kèm.
- **Test Data:** —
- **Steps:**
  1. Tab "Hồ sơ PL" → click icon [Xem] trên row HSPL-20260101-001.
  2. Quan sát modal/page chi tiết.
- **Expected:**
  - **STATE:** Network `GET /api/v1/ho-so-phap-ly-dn/{id}` → 200 OK với full record + thông tin DN liên kết (tên, MST, địa chỉ, người đại diện) + array file_dinh_kem [{ten_file, loai_file, dung_luong, url_preview}].
  - **UI:** Modal/page hiển thị 11 field readonly (mã/tên/DN bold-link/loại/lĩnh vực/ngày cấp/ngày HH/cơ quan cấp/mô tả/trạng thái badge/ngày tạo). Section "File đính kèm": 2 mục với tên + size + nút [Xem preview] + [Tải xuống]. Nút [Sửa] [Đóng] ở footer.
  - **PERSIST:** Click [Tải xuống] → file download đúng tên + size đúng.
- **SRS ref:** line 606-614 (Processing Xem chi tiết — `[GAP-X.1-05]` 5 step).
- **Notes:** Verify file URL preview KHÔNG expose token raw trong query string (BR-EC-03 secure). Nếu file > 10MB thì preview load lazy.

### TC-HSPL-004 — UPDATE HSPL: đổi trạng thái HIEU_LUC → THU_HOI + thêm mô tả lý do

- **TraceID:** FR-X.1-04 / SRS line 579-586
- **Type:** Happy
- **Priority:** P0 🔴
- **Pre-conditions:** cb_nv_tw_01 đăng nhập. HSPL "HSPL-20260101-002" trạng thái HIEU_LUC tồn tại.
- **Test Data:** trang_thai=THU_HOI, mo_ta="Cơ quan cấp thu hồi do vi phạm điều khoản 5".
- **Steps:**
  1. Tab "Hồ sơ PL" → row HSPL-20260101-002 → click icon [Sửa].
  2. Form load đầy đủ data hiện tại.
  3. Đổi trạng thái dropdown → THU_HOI.
  4. Cập nhật mô tả.
  5. Click [Lưu].
- **Expected:**
  - **STATE:** UPDATE HO_SO_PHAP_LY_DN SET trang_thai='THU_HOI', mo_ta='...', updated_at=NOW(), updated_by=cb_nv_tw_01. AUDIT_LOG: hanh_dong='UPDATE', du_lieu_cu={trang_thai:'HIEU_LUC'}, du_lieu_moi={trang_thai:'THU_HOI'}.
  - **UI:** Toast "Cập nhật hồ sơ pháp lý thành công". Form đóng, list reload → row hiển thị badge "THU_HOI" đỏ.
  - **PERSIST:** Reload tab → trạng thái mới giữ nguyên. Detail [Xem] → mô tả mới + trạng thái mới.
- **SRS ref:** line 579-586 (Processing Chỉnh sửa).
- **Notes:** 3 trạng thái user-driven (line 163), không có auto flow.

### TC-HSPL-005 — DELETE soft HSPL với confirm modal nguyên văn "Bạn có chắc chắn muốn xóa hồ sơ '{tên}'?"

- **TraceID:** FR-X.1-04 / SRS line 588-595 / BR-DATA-01 (line 1537-1541)
- **Type:** Happy
- **Priority:** P0 🔴
- **Pre-conditions:** cb_nv_tw_01 đăng nhập. HSPL "HSPL-20260101-003" tên "Quyết định bổ nhiệm Q1/2026" tồn tại.
- **Test Data:** —
- **Steps:**
  1. Tab "Hồ sơ PL" → row HSPL-20260101-003 → click icon [Xóa].
  2. Confirm modal hiện.
  3. Click [Xác nhận xóa].
- **Expected:**
  - **STATE:** UPDATE HO_SO_PHAP_LY_DN SET is_deleted=1, deleted_at=NOW(), deleted_by=cb_nv_tw_01 (BR-DATA-01 soft delete). AUDIT_LOG: hanh_dong='DELETE'.
  - **UI:** Modal nguyên văn "Bạn có chắc chắn muốn xóa hồ sơ **'Quyết định bổ nhiệm Q1/2026'**?" (line 593). Nút [Xác nhận xóa] [Hủy]. Sau confirm: toast "Xóa hồ sơ thành công". Record biến mất khỏi list.
  - **PERSIST:** Reload tab → record không còn. `list_network_requests` verify DELETE `/api/v1/ho-so-phap-ly-dn/{id}` response 200 + body chứa `is_deleted: true`/`deleted_at` set (BR-DATA-01 soft delete — verify qua API response, KHÔNG query DB trực tiếp).
- **SRS ref:** line 588-595 (Processing Xóa), line 1537-1541 (BR-DATA-01).
- **Notes:** A7 SỬA — chuyển từ "Query DB direct (qtht_01)" sang verify response API DELETE qua `list_network_requests`. Click [Hủy] thay vì [Xác nhận] → modal đóng, record không bị xóa (verify side path).

### TC-HSPL-006 — Export Excel HSPL với filter hiện tại + max 10k rows + 8 cột nguyên văn

- **TraceID:** FR-X.1-04 / SRS line 616-624 (Processing Xuất Excel — `[GAP-X.1-05]`)
- **Type:** Happy
- **Priority:** P1
- **Pre-conditions:** cb_nv_tw_01 đăng nhập. ≥30 HSPL trong đơn vị BTP-TW.
- **Test Data:** Filter loai_ho_so=GIAY_PHEP + trang_thai=HIEU_LUC.
- **Steps:**
  1. Tab "Hồ sơ PL" → áp filter "Loại = GIAY_PHEP" + "Trạng thái = HIEU_LUC".
  2. Click [Xuất Excel] (toolbar).
  3. Đợi file download.
  4. Mở file .xlsx.
- **Expected:**
  - **STATE:** Network `GET /api/v1/ho-so-phap-ly-dn/export?loai=GIAY_PHEP&trang_thai=HIEU_LUC` → response Content-Type=application/vnd.openxmlformats-officedocument.spreadsheetml.sheet.
  - **UI:** Loading spinner trong khi tạo file. File `.xlsx` download.
  - **FILE CONTENT:** Sheet1 chứa **8 cột nguyên văn line 623**: mã hồ sơ / tên / DN / loại / ngày cấp / hết hạn / trạng thái / cơ quan cấp. Số row = số record sau filter (KHÔNG có HSPL HET_HAN/THU_HOI). Header row hiển thị tiếng Việt có dấu.
  - **BOUNDARY:** Nếu kết quả > 10k rows → giới hạn 10k + warning "Vượt quá 10.000 dòng, đã giới hạn" (SRS Gap nguyên văn).
- **SRS ref:** line 616-624 (Processing Xuất Excel — `[GAP-X.1-05]` 5 step).
- **Notes:** Verify Excel mở được trong LibreOffice + Excel 2019+. Verify ngày format dd/mm/yyyy.

---

## Section C — Tìm kiếm HSPL (5 filter AND logic + boundary)

### TC-HSPL-007 — Tìm kiếm AND logic 3 filter: keyword + loại + DN

- **TraceID:** FR-X.1-04 / SRS line 597-604 (Processing Tìm kiếm)
- **Type:** Happy
- **Priority:** P0 🔴
- **Pre-conditions:** cb_nv_tw_01 đăng nhập. Seed: 3 HSPL "Giấy phép..." thuộc DN-TW-001 + 2 HSPL "Hợp đồng..." thuộc DN-TW-001 + 5 HSPL "Giấy phép..." thuộc DN-TW-002.
- **Test Data:** keyword="Giấy phép" + loai_ho_so=GIAY_PHEP + doanh_nghiep_id=DN-TW-001.
- **Steps:**
  1. Tab "Hồ sơ PL" → điền filter-bar: keyword="Giấy phép", loại=GIAY_PHEP, DN=DN-TW-001.
  2. Click [Tìm kiếm].
- **Expected:**
  - **STATE:** Backend WHERE keyword LIKE + loai_ho_so='GIAY_PHEP' + doanh_nghiep_id='DN-TW-001' + is_deleted=0 + don_vi_id IN scope → AND logic (line 603).
  - **UI:** Hiển thị 3 record (chỉ DN-TW-001 + GIAY_PHEP). KHÔNG có HSPL HOP_DONG. KHÔNG có HSPL DN-TW-002. Pagination "Tổng: 3".
  - **PERSIST:** Reload (nếu có URL deeplink filter — SPEC-CLARIFY-HSPL-UI-02) → giữ filter, hoặc nếu không sync URL thì reset.
- **SRS ref:** line 597-604 (4 step Tìm kiếm AND logic).
- **Notes:** Keyword search tìm theo mã HS / tên DN / tên HS (line 552). Verify FTS unaccent VN BR-DATA-08 với keyword không dấu "giay phep" → vẫn match "Giấy phép".

### TC-HSPL-008 — Tìm kiếm boundary date: tu_ngay = den_ngay (cùng ngày → match record có ngày_cấp đúng ngày đó)

- **TraceID:** FR-X.1-04 / SRS line 555 (tu_ngay <= den_ngay)
- **Type:** Edge
- **Priority:** P1
- **Pre-conditions:** cb_nv_tw_01 đăng nhập. Seed: 1 HSPL có ngay_cap=2026-03-15.
- **Test Data:** tu_ngay=2026-03-15, den_ngay=2026-03-15.
- **Steps:**
  1. Tab "Hồ sơ PL" → filter tu_ngay=2026-03-15, den_ngay=2026-03-15.
  2. Click [Tìm kiếm].
- **Expected:**
  - **STATE:** Backend `WHERE ngay_cap >= '2026-03-15' AND ngay_cap <= '2026-03-15'` (boundary inclusive).
  - **UI:** Hiển thị 1 record HSPL ngay_cap=2026-03-15.
- **SRS ref:** line 555 (ràng buộc tu_ngay <= den_ngay).
- **Notes:** SPEC-CLARIFY-HSPL-DATE-01 — SRS không quote rõ "boundary inclusive vs exclusive". Default test inclusive (>=, <=).

### TC-HSPL-009 — Tìm kiếm INFO: keyword không có kết quả → message "Không tìm thấy hồ sơ pháp lý phù hợp"

- **TraceID:** INF-HSPL-01 (line 658)
- **Type:** Negative (info)
- **Priority:** P1
- **Pre-conditions:** cb_nv_tw_01 đăng nhập.
- **Test Data:** keyword="zxywvut-không-có-kết-quả-xyz".
- **Steps:**
  1. Tab "Hồ sơ PL" → keyword nhập chuỗi không match.
  2. Click [Tìm kiếm].
- **Expected:**
  - **STATE:** Backend trả empty array.
  - **UI:** Empty state hiển thị message **nguyên văn line 658**: "Không tìm thấy hồ sơ pháp lý phù hợp" (INF-HSPL-01). Không có error icon (chỉ INFO badge).
- **SRS ref:** line 658 (INF-HSPL-01).
- **Notes:** Verify message exactly match nguyên văn — không phải "Không có dữ liệu" hay khác.

---

## Section D — Negative ERR-HSPL-01..06

### TC-HSPL-010 — ERR-HSPL-01: Tên hồ sơ trống → reject INSERT

- **TraceID:** ERR-HSPL-01 (line 652)
- **Type:** Negative
- **Priority:** P0 🔴
- **Pre-conditions:** cb_nv_tw_01 đăng nhập. DN-TW-001 tồn tại.
- **Test Data:** ten_ho_so="" (rỗng), các field khác valid.
- **Steps:**
  1. Tab "Hồ sơ PL" → [+ Thêm hồ sơ].
  2. Bỏ trống Tên hồ sơ. Điền các field còn lại.
  3. Click [Lưu].
- **Expected:**
  - **STATE:** KHÔNG INSERT. Count record không đổi.
  - **UI:** Inline error nguyên văn line 652: "**Tên hồ sơ pháp lý là bắt buộc**". Focus field tên. Form không đóng.
  - **PERSIST:** Reload → record không tồn tại.
- **SRS ref:** line 652 (ERR-HSPL-01).
- **Notes:** Verify message exactly nguyên văn.

### TC-HSPL-011 — ERR-HSPL-03 + ERR-HSPL-04: File 21MB / file mã độc EICAR → reject upload

- **TraceID:** ERR-HSPL-03 (line 654) + ERR-HSPL-04 (line 655) / BR-EC-03 ClamAV
- **Type:** Negative
- **Priority:** P0 🔴
- **Pre-conditions:** cb_nv_tw_01 đăng nhập.
- **Test Data:**
  - Lần 1: file_21mb.pdf (size 21MB).
  - Lần 2: eicar-test.com (chuỗi EICAR signature).
- **Steps:**
  1. [+ Thêm hồ sơ] → điền field valid → upload file 21MB → click [Lưu].
  2. Lần 2: file 5MB nhưng chứa EICAR signature → upload → [Lưu].
- **Expected:**
  - **Lần 1:** Reject ngay tại client hoặc backend. Inline error nguyên văn line 654: "**File đính kèm tối đa 20MB**" (ERR-HSPL-03). KHÔNG INSERT.
  - **Lần 2:** Backend ClamAV scan trigger → reject. Toast/inline error nguyên văn line 655: "**File 'eicar-test.com' chứa mã độc, không thể tải lên**" (ERR-HSPL-04). KHÔNG INSERT record HSPL hoặc INSERT pending nhưng FILE_DINH_KEM = NULL + record rollback (SPEC-CLARIFY-HSPL-VIRUS-01: rollback toàn bộ INSERT hay chỉ skip file?).
  - **PERSIST:** Count HSPL không đổi cả 2 lần.
- **SRS ref:** line 654-655 (ERR-HSPL-03, ERR-HSPL-04), BR-EC-03.
- **Notes:** Test EICAR cần file standard `X5O!P%@AP[4\PZX54(P^)7CC)7}$EICAR-STANDARD-ANTIVIRUS-TEST-FILE!$H+H*`. Boundary: file 20.0MB exact → PASS; file 20.0001MB → FAIL.

### TC-HSPL-012 — ERR-HSPL-02: doanh_nghiep_id không tồn tại → reject

- **TraceID:** ERR-HSPL-02 (line 653)
- **Type:** Negative
- **Priority:** P1
- **Pre-conditions:** cb_nv_tw_01 đăng nhập.
- **Test Data:** doanh_nghiep_id="DN-INVALID-99999" (không tồn tại).
- **Steps:**
  1. API direct POST `/api/v1/ho-so-phap-ly-dn` body với doanh_nghiep_id không hợp lệ (bypass UI vì UI dùng searchable select).
- **Expected:**
  - **STATE:** Backend FK constraint check fail. KHÔNG INSERT.
  - **UI/HTTP:** Response 400 với message nguyên văn line 653: "**Doanh nghiệp không tồn tại hoặc đã bị xóa**" (ERR-HSPL-02).
- **SRS ref:** line 653 (ERR-HSPL-02).
- **Notes:** Boundary case: doanh_nghiep_id của DN đã soft delete (is_deleted=1) → cũng trả ERR-HSPL-02 (line 653 "hoặc đã bị xóa").

### TC-HSPL-013 — ERR-HSPL-05 + ERR-HSPL-06: Loại hồ sơ không hợp lệ + tu_ngay > den_ngay search

- **TraceID:** ERR-HSPL-05 (line 656) + ERR-HSPL-06 (line 657)
- **Type:** Negative
- **Priority:** P1
- **Pre-conditions:** cb_nv_tw_01 đăng nhập.
- **Test Data:**
  - Lần 1: loai_ho_so="LOAI_KHONG_HOP_LE" (không nằm trong 5 enum).
  - Lần 2: tu_ngay=2026-12-31, den_ngay=2026-01-01 (tu > den).
- **Steps:**
  1. API direct POST với loai_ho_so="LOAI_KHONG_HOP_LE" (UI dropdown không cho chọn → bypass).
  2. UI search filter tu_ngay=2026-12-31, den_ngay=2026-01-01 → click [Tìm kiếm].
- **Expected:**
  - **Lần 1:** Backend reject. Message nguyên văn line 656: "**Loại hồ sơ 'LOAI_KHONG_HOP_LE' không hợp lệ**" (ERR-HSPL-05). KHÔNG INSERT.
  - **Lần 2:** UI inline error hoặc toast nguyên văn line 657: "**Ngày bắt đầu phải trước ngày kết thúc**" (ERR-HSPL-06). KHÔNG gọi API search.
- **SRS ref:** line 656 (ERR-HSPL-05), line 657 (ERR-HSPL-06).
- **Notes:** 5 enum hợp lệ (line 539): GIAY_PHEP / HOP_DONG / GIAY_CN / QUYET_DINH / KHAC.

---

## Section E — Permission BR-AUTH-08 multi-tenant + BR-AUTH-10 NHT mở rộng

### TC-HSPL-014 — BR-AUTH-08 multi-tenant: cb_nv_dp_01 (AG) chỉ thấy HSPL thuộc don_vi_id = STP-AG

- **TraceID:** BR-AUTH-08 (line 1531-1535) / SRS line 530
- **Type:** Happy / Permission
- **Priority:** P0 🔴
- **Pre-conditions:**
  - Seed: 3 HSPL thuộc don_vi=STP-AG + 3 HSPL thuộc don_vi=STP-BG + 3 HSPL thuộc don_vi=BTP-TW.
  - cb_nv_dp_01 (AG) đăng nhập.
- **Test Data:** —
- **Steps:**
  1. cb_nv_dp_01 mở DN bất kỳ thuộc STP-AG → tab "Hồ sơ PL".
  2. Quan sát danh sách HSPL.
  3. Cố navigate URL trực tiếp đến HSPL của STP-BG (vd `/ho-so-phap-ly-dn/{HSPL-BG-id}`).
- **Expected:**
  - **STATE:** Backend WHERE `don_vi_id = STP-AG` (BR-AUTH-08 line 1533).
  - **UI:**
    - Tab "Hồ sơ PL" hiển thị 3 record STP-AG. KHÔNG hiển thị 6 record kia.
    - Direct URL HSPL của STP-BG → 403 hoặc redirect "Bạn không có quyền".
  - **PERSIST:** Reload giữ scope.
- **SRS ref:** line 1531-1535 (BR-AUTH-08), line 530 (User thuộc đơn vị có quyền).
- **Notes:** Cross-cấp test: cb_nv_dp_01 (AG) cố xem HSPL của BTP-TW → cũng 403 (BR-AUTH-03 ngang/dưới cấp không thấy lên).

### TC-HSPL-015 — BR-AUTH-10 NHT mở rộng: nht_01 (AG) chỉ R+U HSPL của DN có VV được phân công, KHÔNG C/D

- **TraceID:** BR-AUTH-10 mở rộng (line 669-671)
- **Type:** Permission / Edge
- **Priority:** P0 🔴
- **Pre-conditions:**
  - Seed: VU_VIEC "VV-AG-001" với doanh_nghiep_id=DN-AG-001 + nguoi_ho_tro_id=nht_01 (NHT phụ trách).
  - HSPL "HSPL-AG-001" thuộc DN-AG-001 + don_vi_id=STP-AG.
  - HSPL "HSPL-AG-002" thuộc DN-AG-002 (DN khác cùng đơn vị STP-AG nhưng KHÔNG có VV phân công cho nht_01).
  - nht_01 đăng nhập (vai_tro=NHT, don_vi=STP-AG).
- **Test Data:** —
- **Steps:**
  1. nht_01 mở DN-AG-001 → tab "Hồ sơ PL".
  2. Quan sát toolbar + actions.
  3. Click [Xem] → click [Sửa] HSPL-AG-001 → đổi mô tả → [Lưu].
  4. Mở DN-AG-002 → tab "Hồ sơ PL".
  5. Cố click [+ Thêm hồ sơ] / [Xóa] HSPL-AG-001.
- **Expected:**
  - **Step 1-2 (DN-AG-001):** Tab hiển thị HSPL-AG-001 (lọc 2 lớp: `HSPL.don_vi_id=STP-AG AND EXISTS VV WHERE doanh_nghiep_id=DN-AG-001 AND nguoi_ho_tro_id=nht_01` — line 669). Toolbar **KHÔNG có** [+ Thêm hồ sơ] (NHT chỉ R+U). Actions chỉ [Xem] [Sửa], **KHÔNG có** [Xóa].
  - **Step 3 (UPDATE):** Form Sửa load OK → [Lưu] thành công. AUDIT_LOG: nguoi_thuc_hien_id=nht_01 (line 671).
  - **Step 4 (DN-AG-002):** Tab "Hồ sơ PL" empty hoặc không hiển thị HSPL-AG-002 (vì không có VV phân công cho nht_01 với DN-AG-002).
  - **Step 5 CREATE/DELETE:** API direct POST → 403. API direct DELETE → 403.
- **SRS ref:** line 669-671 (3 AC nguyên văn cho NHT BR-AUTH-10 mở rộng).
- **Notes:** SPEC-CLARIFY-HSPL-NHT-01 — Khi VV chuyển sang HOAN_THANH/HUY thì NHT còn truy cập HSPL không? SRS line 669 không quote điều kiện trạng thái VV. Verify khi B-Run.

---

## Section F — Edge bổ sung A4 (Boundary file + Date validation + Unicode normalization)

### TC-HSPL-016 — Edge boundary file: 0 byte / 20.0MB exact / 20.0MB+1 byte (extends ERR-HSPL-03)

- **TraceID:** ERR-HSPL-03 (line 654) / BR-EC-03
- **Type:** Edge
- **Priority:** P1
- **Pre-conditions:** cb_nv_tw_01 đăng nhập. DN-TW-001 tồn tại.
- **Test Data:**
  - Lần 1: empty.pdf (0 byte size).
  - Lần 2: file_20mb_exact.pdf (20971520 byte = 20MB exact).
  - Lần 3: file_20mb_plus_1.pdf (20971521 byte).
- **Steps:**
  1. [+ Thêm hồ sơ] → điền field valid → upload empty.pdf → [Lưu].
  2. Lần 2: upload 20.0MB exact → [Lưu].
  3. Lần 3: upload 20MB+1 byte → [Lưu].
- **Expected:**
  - **Lần 1:** Reject. Toast/inline "File rỗng không được phép" (SRS Gap nguyên văn). HOẶC nếu BE accept 0 byte: cảnh báo nhưng cho phép. Default test: REJECT (best practice). KHÔNG INSERT FILE_DINH_KEM.
  - **Lần 2:** PASS, INSERT OK với size=20971520 byte (boundary inclusive at exactly 20MB).
  - **Lần 3:** Reject với ERR-HSPL-03 nguyên văn line 654: "File đính kèm tối đa 20MB". KHÔNG INSERT.
- **SRS ref:** line 654 (ERR-HSPL-03 max 20MB), BR-EC-03 ClamAV.
- **Notes:** A4 boundary triple — extends TC-HSPL-011 single-case. SPEC-CLARIFY-HSPL-FILE-01 — 0 byte file policy chưa quote.

### TC-HSPL-017 — Edge file PDF corrupt mid-upload (network interrupt)

- **TraceID:** ERR-HSPL-03/04 ext / BR-EC-03 / BR-EC-20
- **Type:** Edge / Error injection
- **Priority:** P2
- **Pre-conditions:** cb_nv_tw_01 đăng nhập. File "valid_15mb.pdf" sẵn sàng.
- **Test Data:** valid_15mb.pdf (size 15MB).
- **Steps:**
  1. [+ Thêm hồ sơ] → điền field valid → start upload 15MB.
  2. Sau khi upload đạt ~50% (qua devtools throttle Slow-3G), force kill tab/network offline.
  3. Mở tab mới, login lại, kiểm tra danh sách HSPL.
  4. `list_network_requests` verify GET `/api/v1/ho-so-phap-ly-dn?...` response — count record của DN không có HSPL pending dở dang.
- **Expected:**
  - **STATE:** Backend không INSERT HSPL nào (transaction chưa commit). Hoặc INSERT pending nhưng có TTL cleanup.
  - **UI:** Lần thử lại upload phải PASS bình thường. KHÔNG có record dở dang xuất hiện trong list HSPL.
  - **PERSIST:** Reload danh sách HSPL → KHÔNG có record dở dang. Verify retry [+ Thêm hồ sơ] với cùng tên HSPL không bị duplicate-name reject (chứng minh record interrupt đã được clean up backend-side).
- **SRS ref:** BR-EC-20 transactional consistency + BR-EC-03 cleanup.
- **Notes:** A7 SỬA — chuyển "Server: kiểm tra file storage có file orphan" + "Storage scan" sang verify gián tiếp qua UI list count + retry không bị duplicate. No SRS quote orphan cleanup policy — best practice extrapolation. SPEC-CLARIFY-HSPL-FILE-02 — TTL cleanup pending uploads.

### TC-HSPL-018 — Edge date validation: ngay_het_han < ngay_cap → reject

- **TraceID:** SRS line 540 (ngay_het_han > ngay_cap implicit) / SPEC-CLARIFY
- **Type:** Edge / Negative
- **Priority:** P1
- **Pre-conditions:** cb_nv_tw_01 đăng nhập.
- **Test Data:**
  - Lần 1: ngay_cap=2026-05-01, ngay_het_han=2026-04-01 (HH < cap).
  - Lần 2: ngay_cap=2026-05-01, ngay_het_han=2026-05-01 (cùng ngày).
  - Lần 3: ngay_cap=2030-12-31 (tương lai xa).
- **Steps:**
  1. [+ Thêm hồ sơ] → điền field với data 1 → [Lưu].
  2. Repeat data 2.
  3. Repeat data 3.
- **Expected:**
  - **Lần 1:** Reject. Inline error "Ngày hết hạn phải sau ngày cấp" (SRS Gap nguyên văn). KHÔNG INSERT.
  - **Lần 2:** SPEC-CLARIFY: hoặc PASS (boundary inclusive cùng ngày = giấy phép 1 ngày) hoặc reject (ngay_het_han > ngay_cap strict). Default test: PASS với warning. SPEC-CLARIFY-HSPL-DATE-02.
  - **Lần 3:** PASS (ngày cấp tương lai cũng valid - giấy phép cấp trước hiệu lực). KHÔNG có warning.
- **SRS ref:** line 540 (ngay_cap, ngay_het_han fields).
- **Notes:** No SRS quote business rule cho ngay_het_han > ngay_cap — best practice extrapolation. SPEC-CLARIFY-HSPL-DATE-02 boundary cùng ngày + tương lai.

### TC-HSPL-019 — Edge Unicode NFC vs NFD normalization trong ten_ho_so

- **TraceID:** BR-DATA-08 FTS / Unicode handling
- **Type:** Edge / Data quality
- **Priority:** P2
- **Pre-conditions:** cb_nv_tw_01 đăng nhập. DN-TW-001 tồn tại.
- **Test Data:**
  - Lần 1: ten_ho_so="Giấy phép Tế bào" (NFC composed: ế = U+1EBF).
  - Lần 2: ten_ho_so="Giấy phép Tế bào" (NFD decomposed: ế = e + U+0302 + U+0301, visual identical).
  - Lần 3: ten_ho_so chứa zero-width joiner U+200D.
- **Steps:**
  1. [+ Thêm hồ sơ] → tên = data 1 → [Lưu].
  2. Repeat data 2 → [Lưu].
  3. Repeat data 3 → [Lưu].
  4. Search keyword "Tế bào" → verify cả 2 record xuất hiện không.
- **Expected:**
  - **Lần 1+2:** Cả 2 INSERT OK (KHÔNG bị duplicate detect dù visually identical). HOẶC backend normalize NFC trước khi save → 2 lần thành 1 record duplicate (BR-DATA cross-cutting).
  - **Lần 3:** ZWJ accept hoặc strip — SPEC-CLARIFY-HSPL-UNI-01.
  - **Step 4:** Search "Tế bào" match cả 2 record (FTS unaccent BR-DATA-08).
- **SRS ref:** line 1567-1571 (BR-DATA-08 FTS) + Unicode best practice.
- **Notes:** No SRS quote Unicode normalization — best practice. Phase B verify NFC vs NFD policy. SPEC-CLARIFY-HSPL-UNI-01.

---

## Section G — SM HSPL trạng thái render HET_HAN

### TC-HSPL-020 — Edge SM HSPL: HSPL với ngay_het_han < today render badge "HET_HAN" khi user truy cập

- **TraceID:** FR-X.1-04 / SRS line 540 (`ngay_het_han` field) + line 1374 (entity CHECK constraint `IN ('HIEU_LUC','HET_HAN','THU_HOI')`)
- **Type:** Edge / Render-side state
- **Priority:** P2
- **Pre-conditions:**
  - cb_nv_tw_01 đăng nhập.
  - Seed HSPL "HSPL-EXPIRED-001" với `ngay_cap=2025-01-01`, `ngay_het_han=2026-05-06` (yesterday so với hôm nay 2026-05-07), `trang_thai` field gốc=`HIEU_LUC`.
  - Seed HSPL "HSPL-VALID-001" với `ngay_het_han=2027-01-01` (tương lai), `trang_thai`=HIEU_LUC.
- **Test Data:** —
- **Steps:**
  1. Login cb_nv_tw_01 → mở chi tiết DN → tab "Hồ sơ PL".
  2. `take_snapshot` table HSPL → quan sát badge trạng thái cột row HSPL-EXPIRED-001 và HSPL-VALID-001.
  3. Click [Xem] HSPL-EXPIRED-001 → quan sát detail badge.
  4. `list_network_requests` verify GET `/api/v1/ho-so-phap-ly-dn?...` response: kiểm tra computed field `trang_thai_render` hoặc `trang_thai` value.
  5. Filter trang_thai=HET_HAN trên filter-bar → verify HSPL-EXPIRED-001 xuất hiện.
- **Expected:**
  - **Bước 2-3:** Row HSPL-EXPIRED-001 hiển thị **badge "HET_HAN" (cam)** dù `trang_thai` field gốc=HIEU_LUC. Row HSPL-VALID-001 vẫn badge "HIEU_LUC" (xanh). Render rule: nếu `ngay_het_han < CURRENT_DATE` AND `trang_thai != THU_HOI` → render HET_HAN.
  - **Bước 4:** API response có thể: (Path A) BE compute `trang_thai_render`=HET_HAN khi serialize; HOẶC (Path B) FE compute từ `ngay_het_han`. Cả 2 path đều acceptable, miễn UI render đúng.
  - **Bước 5:** Filter HET_HAN trả về HSPL-EXPIRED-001.
- **SRS ref:** line 540 (`ngay_het_han` field), line 1374 (Entity HSPL `trang_thai CHECK IN ('HIEU_LUC','HET_HAN','THU_HOI')` — chỉ là enum constraint, KHÔNG quote auto/render transition trong SRS FR-12).
- **Notes:** A6 fill A5-G6 — A7 lưu ý cron auto-update DB có thể bị LOẠI (no-UI side effect). TC này chỉ verify **render-side** khi user truy cập (test qua MCP chrome-devtools được). SPEC-CLARIFY-HSPL-CRON: BA xác nhận cron job có chạy auto update DB hay chỉ render-side compute. Phase B verify path thực tế. **Sửa 2026-05-09 (codex review M5):** SRS line 1374 chỉ là Entity CHECK constraint enum, KHÔNG phải SM auto transition. TC vẫn giữ nguyên test scope (render-side check ngay_het_han < CURRENT_DATE) — đây là extrapolation hợp lý vì SRS line 540 chỉ định ngay_het_han nhưng không quote rule khi quá hạn → SPEC-CLARIFY-HSPL-CRON pending BA respond.

---

**Tổng số TC: 20**
