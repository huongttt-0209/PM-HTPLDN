# Test Cases — UC152: Quản lý tư liệu pháp lý vụ việc (FR-X.1-06)

> **SRS Ref:** FR-X.1-06 / UC152 — `srs-fr-12-tv-chuyen-sau-v3.1.md` line 778-952
> **Entity:** TU_LIEU_PHAP_LY_VV (TLPL)
> **Màn hình:** Tab "Tư liệu PL" trong MH-12.2 chi tiết TVCS — KHÔNG có màn hình riêng (line 784 — SCR-X1-07 deprecated v2.1, gộp inline accordion)
> **Ngày tạo:** 2026-05-06
> **Owner:** QA Automation Lead
> **Phase:** A3 (test-design generate)
> **Tài khoản test:** `input/users.csv` — cb_nv_tw_01, cb_nv_dp_01 (AG), cb_nv_dp_02 (BG)

---

## Phạm vi file

CRUD tư liệu pháp lý vụ việc + Công khai BR-FLOW-07 trực tiếp lên Cổng PLQG (KHÔNG cần phê duyệt). Cover Happy/Negative/Edge/UI Verify cho:
- UI Verify tab "Tư liệu PL" + table actions.
- CRUD TLPL (CREATE / READ / UPDATE chặn CONG_KHAI / DELETE soft + API gỡ Cổng).
- Upload/xóa file + virus scan ClamAV (BR-EC-03).
- Tìm kiếm FTS unaccent VN.
- Công khai BR-FLOW-07 (NHAP ↔ CONG_KHAI) + BR-PUBLIC-01..03.
- Negative ERR-TLPL-01..06 + WRN-TLPL-01.
- Edge: bật-tắt-bật, optimistic lock, API rollback BR-EC-20.

---

## Section A — UI Verify

### TC-TLPL-001 — Verify tab "Tư liệu PL" trong MH-12.2: Toolbar + Table 5 cột + 5 actions per row

- **TraceID:** FR-X.1-06 / SRS line 784, 909-922 (Outputs danh sách) / SCR MH-12.2 tab "Tư liệu PL"
- **Type:** UI Verify (Happy)
- **Priority:** P0 🔴
- **Pre-conditions:**
  - cb_nv_tw_01 đăng nhập.
  - TVCS "TVCS-20260101-001" thuộc cùng đơn vị BTP-TW + có ≥3 TLPL (cover 2 trạng thái NHAP/CONG_KHAI + ≥1 TLPL có 2 file).
- **Test Data:** URL `/tv-chuyen-sau/{TVCS-id}` → tab "Tư liệu PL".
- **Steps:**
  1. Đăng nhập cb_nv_tw_01.
  2. Navigate menu "Tư vấn > TV pháp luật chuyên sâu > TVCS-20260101-001 chi tiết" → MH-12.2.
  3. Click tab "Tư liệu PL" (accordion 3 inline).
  4. Quan sát toolbar + table + actions per row.
- **Expected:**
  - **Toolbar:** Có button [+ Thêm tư liệu] (line 800-806).
  - **Table 5 cột chính** (theo line 909-922): Tên tư liệu / Loại (5 enum: VAN_BAN_PL/TAI_LIEU/NGHIEN_CUU/TIEN_LE/KHAC) / Trạng thái badge 2 màu (NHAP=xám, CONG_KHAI=xanh) / Số file (number) / Hành động.
  - **Actions per row** (5 hành động): [Sửa] / [Xóa] / [Upload file] (icon attach) / [Công khai] (chỉ enable khi NHAP + có ≥1 file) / [Hủy công khai] (chỉ enable khi CONG_KHAI). Conditional theo trạng thái.
  - **Pagination:** Default 20/page (BR-DATA-07).
  - **Empty state:** "Chưa có tư liệu pháp lý. [+ Thêm tư liệu]".
- **SRS ref:** line 784 (deprecate SCR riêng), line 800-806 (Inputs CRUD), line 909-922 (Outputs).
- **Notes:** SPEC-CLARIFY-TLPL-UI-01 — SRS không quote rõ vị trí action [Công khai]/[Hủy công khai] (button row vs context menu). Default test: button nhỏ trong cột Hành động + tooltip.

---

## Section B — CRUD TLPL (Happy + Update chặn CONG_KHAI + Delete CONG_KHAI)

### TC-TLPL-002 — CREATE TLPL thành công với trạng thái default = NHAP

- **TraceID:** FR-X.1-06 / SRS line 826-833
- **Type:** Happy
- **Priority:** P0 🔴
- **Pre-conditions:** cb_nv_tw_01 đăng nhập. TVCS-20260101-001 trạng thái DANG_TU_VAN tồn tại.
- **Test Data:**
  - noi_dung_tv_id=TVCS-20260101-001
  - ten_tu_lieu="Văn bản hợp nhất Luật Doanh nghiệp 2020"
  - loai_tu_lieu=VAN_BAN_PL
  - linh_vuc_id=DOANH_NGHIEP
  - mo_ta="Tham chiếu Luật DN khoản 5 điều 17"
- **Steps:**
  1. Tab "Tư liệu PL" → click [+ Thêm tư liệu].
  2. Form modal mở → điền 5 field theo Test Data (noi_dung_tv_id auto-fill từ context TVCS hiện tại).
  3. Click [Lưu].
- **Expected:**
  - **STATE:** INSERT TU_LIEU_PHAP_LY_VV với trang_thai='NHAP' (default theo line 806). 7 common fields BR-DATA-03 (id, created_at, updated_at, created_by=cb_nv_tw_01, updated_by, is_deleted=0, don_vi_id=BTP-TW). cong_khai=0, thoi_gian_dang_tai=NULL.
  - **AUDIT_LOG:** hanh_dong='CREATE', entity='TU_LIEU_PHAP_LY_VV' (BR-DATA-05).
  - **UI:** Toast "Thêm tư liệu thành công" (SRS Gap message — SPEC-CLARIFY-TLPL-MSG-01). Form đóng, table reload → record mới với badge "NHAP" xám, số file=0.
  - **PERSIST:** Reload tab → record vẫn xuất hiện. Action [Công khai] disable (chưa có file).
- **SRS ref:** line 826-833 (4 step Thêm mới), line 806 (default NHAP).
- **Notes:** ten_tu_lieu boundary 500 ký tự (line 802) — verify ở edge TC riêng.

### TC-TLPL-003 — READ chi tiết TLPL: hiển thị thông tin + danh sách file

- **TraceID:** FR-X.1-06 / SRS line 946 (AC chi tiết)
- **Type:** Happy
- **Priority:** P1
- **Pre-conditions:** cb_nv_tw_01 đăng nhập. TLPL "TLPL-001" có 2 file đính kèm.
- **Test Data:** —
- **Steps:**
  1. Tab "Tư liệu PL" → click vào tên TLPL-001 hoặc icon [Xem] (nếu có).
  2. Quan sát modal/page chi tiết.
- **Expected:**
  - **STATE:** Network `GET /api/v1/tu-lieu-phap-ly-vv/{id}` → 200 OK với full record + array file_dinh_kem [{ten_file, loai_file, dung_luong, url_preview}].
  - **UI:** Modal hiển thị 6 field (tên / loại / VV liên kết / lĩnh vực / mô tả / trạng thái badge). Section "File đính kèm": 2 mục với tên + size + nút [Xem preview] + [Tải xuống] + [Xóa file].
  - **PERSIST:** Click [Tải xuống] → file download đúng tên + size đúng.
- **SRS ref:** line 946 (Given chọn tư liệu Then hiển thị thông tin + danh sách file).
- **Notes:** —

### TC-TLPL-004 — UPDATE TLPL trạng thái NHAP thành công

- **TraceID:** FR-X.1-06 / SRS line 865-874 (Processing Chỉnh sửa — `[GAP-X.1-02]`)
- **Type:** Happy
- **Priority:** P0 🔴
- **Pre-conditions:** cb_nv_tw_01 đăng nhập. TLPL "TLPL-002" trạng thái NHAP.
- **Test Data:** ten_tu_lieu="Văn bản hợp nhất Luật DN 2020 (cập nhật mục 2)", mo_ta="Bổ sung phân tích điều 25".
- **Steps:**
  1. Tab "Tư liệu PL" → row TLPL-002 → [Sửa].
  2. Form load đầy đủ data.
  3. Đổi tên + mô tả.
  4. Click [Lưu].
- **Expected:**
  - **STATE:** Backend kiểm tra trang_thai != CONG_KHAI (line 871) → PASS. UPDATE SET ten_tu_lieu, mo_ta, updated_at, updated_by. AUDIT_LOG: UPDATE.
  - **UI:** Toast "Cập nhật tư liệu thành công". Form đóng, table reload → tên mới hiển thị.
  - **PERSIST:** Reload → data mới giữ nguyên.
- **SRS ref:** line 865-874 (Processing Chỉnh sửa 6 step).
- **Notes:** —

### TC-TLPL-005 — UPDATE TLPL trạng thái CONG_KHAI bị chặn → WRN-TLPL-01

- **TraceID:** WRN-TLPL-01 (line 941) / SRS line 871
- **Type:** Negative / Edge
- **Priority:** P0 🔴
- **Pre-conditions:** cb_nv_tw_01 đăng nhập. TLPL "TLPL-003" trạng thái CONG_KHAI (đã push lên Cổng).
- **Test Data:** Cố sửa ten_tu_lieu.
- **Steps:**
  1. Tab "Tư liệu PL" → row TLPL-003 (badge CONG_KHAI xanh) → click [Sửa].
- **Expected (per SPEC-CLARIFY-TVCS-07 — overview line 303):**
  - **Path A (WARNING):** Form Sửa mở nhưng disable input + warning banner nguyên văn line 941: "**Tư liệu đã ở trạng thái công khai**" (WRN-TLPL-01). Có hint "Vui lòng [Hủy công khai] trước khi chỉnh sửa". Nút [Lưu] disabled.
  - **Path B (REJECTION):** Click [Sửa] → toast/modal nguyên văn line 941: "**Tư liệu đã ở trạng thái công khai**". KHÔNG mở form.
- **STATE:** KHÔNG UPDATE record dù có cố submit qua API direct → backend reject với code WRN-TLPL-01.
- **PERSIST:** Reload → data không đổi.
- **SRS ref:** line 871 ("nếu CONG_KHAI → từ chối sửa (phải hủy công khai trước)"), line 941 (WRN-TLPL-01).
- **Notes:** SPEC-CLARIFY-TVCS-07 — verify Path A vs Path B. Cả 2 phải có message nguyên văn.

### TC-TLPL-006 — DELETE TLPL trạng thái CONG_KHAI → API gỡ Cổng PLQG trước + soft delete

- **TraceID:** FR-X.1-06 / SRS line 876-885 (Processing Xóa mềm — `[GAP-X.1-02]`)
- **Type:** Happy / Edge
- **Priority:** P0 🔴
- **Pre-conditions:** cb_nv_tw_01 đăng nhập. TLPL "TLPL-004" trạng thái CONG_KHAI + cong_khai=1 + thoi_gian_dang_tai not NULL.
- **Test Data:** —
- **Steps:**
  1. Tab "Tư liệu PL" → row TLPL-004 → [Xóa].
  2. Modal confirm.
  3. Click [Xác nhận xóa].
- **Expected:**
  - **STATE Step 3 backend** (line 882-884):
    - Bước 3: Gọi API Cổng PLQG `DELETE /portal-plqg/tu-lieu/{ma_cong}` để gỡ tư liệu. Nếu Cổng OK → tiếp tục.
    - Bước 5: Soft delete `is_deleted=1, deleted_at=NOW()`.
    - AUDIT_LOG: hanh_dong='DELETE' với note "Đã gỡ khỏi Cổng PLQG".
  - **UI:** Modal nguyên văn (line 883): "Bạn có chắc chắn muốn xóa tư liệu **'{ten}'**?". Sau confirm: loading spinner (gọi Cổng) → toast "Xóa tư liệu thành công + đã gỡ khỏi Cổng PLQG".
  - **PERSIST:** Reload tab → record biến mất. `list_network_requests` verify backend đã fire `DELETE /portal-plqg/tu-lieu/{ma_cong}` (outbound API call tới Cổng PLQG) + response 200 OK trước khi soft delete; verify response DELETE `/api/v1/tu-lieu-phap-ly-vv/{id}` body chứa `is_deleted: true`.
- **Edge ROLLBACK:** Nếu API Cổng PLQG fail (mock 500) → KHÔNG soft delete (BR-EC-20 transactional consistency). Toast lỗi nguyên văn line 940: "**Lỗi kết nối Cổng PLQG. Vui lòng thử lại sau**" (ERR-TLPL-06). Record vẫn tồn tại trạng thái CONG_KHAI.
- **SRS ref:** line 876-885 (6 step Xóa mềm), BR-EC-20 (overview line 107).
- **Notes:** A7 SỬA — chuyển "Query Cổng PLQG (qtht_01 verify backend log)" sang `list_network_requests` verify outbound network request DELETE /portal-plqg/tu-lieu fired + response 200 (UI-bridge gián tiếp). SPEC-CLARIFY-TLPL-DELETE-01 — Nếu Cổng API timeout (>30s) thì có rollback nguyên trạng hay queue retry async? Verify khi B-Run.

---

## Section C — Upload/xóa file + virus scan

### TC-TLPL-007 — Upload file PDF/DOCX/XLS/image hợp lệ + cảnh báo khi xóa file cuối cùng của TLPL CONG_KHAI

- **TraceID:** FR-X.1-06 / SRS line 835-843 (Tải lên) + line 887-896 (Xóa file đính kèm — `[GAP-X.1-02]`)
- **Type:** Happy + Edge
- **Priority:** P0 🔴
- **Pre-conditions:** cb_nv_tw_01 đăng nhập. TLPL "TLPL-005" trạng thái CONG_KHAI có 1 file PDF.
- **Test Data:**
  - Lần 1 (upload): file_a.pdf (10MB), file_b.docx (3MB), file_c.xls (2MB), file_d.png (1MB).
  - Lần 2 (xóa file cuối): xóa file PDF duy nhất của TLPL-005.
- **Steps:**
  1. Tab "Tư liệu PL" → TLPL-NEW (NHAP) → [Upload file] → upload 4 file lần lượt.
  2. Sau upload: chuyển sang TLPL-005 → mở [Xem file đính kèm] → click [Xóa file] trên file PDF cuối.
- **Expected:**
  - **Lần 1:**
    - Mỗi file: backend ClamAV scan PASS (BR-EC-03) → INSERT FILE_DINH_KEM linked.
    - Toast "Tải lên thành công" per file. Số file của TLPL-NEW = 4. AUDIT_LOG: UPLOAD per file.
  - **Lần 2:**
    - Backend kiểm tra: TLPL-005 trạng thái CONG_KHAI + xóa file → còn 0 file.
    - Bước 5 line 895: "Nếu tư liệu CONG_KHAI và không còn file nào: cảnh báo CB NV".
    - **UI:** Modal warning trước khi xóa: "Tư liệu đang công khai. Sau khi xóa file này, tư liệu sẽ không còn file đính kèm. Tiếp tục?". User chọn [Có] → xóa file. AUDIT_LOG: hanh_dong='DELETE_FILE' + warning_logged=true.
- **SRS ref:** line 835-843 (5 step Tải lên), line 887-896 (6 step Xóa file đính kèm), BR-EC-03.
- **Notes:** SPEC-CLARIFY-TLPL-FILE-01 — Sau cảnh báo line 895, TLPL CONG_KHAI không còn file thì có auto chuyển NHAP + gỡ Cổng không? SRS không quote → default test: KHÔNG auto chuyển, chỉ warning.

### TC-TLPL-008 — Negative file: 21MB + EICAR virus + định dạng không hỗ trợ (.exe)

- **TraceID:** ERR-TLPL-03 (line 937) + ERR-TLPL-04 (line 938) / BR-EC-03
- **Type:** Negative
- **Priority:** P0 🔴
- **Pre-conditions:** cb_nv_tw_01 đăng nhập. TLPL "TLPL-006" trạng thái NHAP.
- **Test Data:**
  - Lần 1: file_21mb.pdf (21MB).
  - Lần 2: eicar-test.com (EICAR signature 5MB).
  - Lần 3: malware.exe (định dạng không trong PDF/DOCX/XLS/image).
- **Steps:**
  1. TLPL-006 → [Upload file] → 3 lần với 3 file trên.
- **Expected:**
  - **Lần 1:** Reject. Toast nguyên văn line 937: "**File tối đa 20MB**" (ERR-TLPL-03). KHÔNG INSERT FILE_DINH_KEM.
  - **Lần 2:** ClamAV scan trigger → reject. Toast nguyên văn line 938: "**File 'eicar-test.com' chứa mã độc**" (ERR-TLPL-04). FILE_DINH_KEM không INSERT.
  - **Lần 3:** Reject ngay client + backend. Toast (SRS Gap message): "Định dạng file không hỗ trợ. Chấp nhận: PDF/DOCX/XLS/image" (line 812 quote định dạng cho phép). KHÔNG INSERT.
- **SRS ref:** line 812 (định dạng), line 937-938 (ERR-TLPL-03, 04), BR-EC-03.
- **Notes:** Boundary: file 20.0MB exact → PASS; file 20.0001MB → FAIL.

---

## Section D — Tìm kiếm TLPL

### TC-TLPL-009 — Tìm kiếm AND logic 4 filter: keyword FTS unaccent + lĩnh vực + loại + trạng thái

- **TraceID:** FR-X.1-06 / SRS line 898-907 (Processing Tìm kiếm — `[GAP-X.1-02]`) / BR-DATA-08 (line 1567-1571)
- **Type:** Happy
- **Priority:** P0 🔴
- **Pre-conditions:** cb_nv_tw_01 đăng nhập. Seed:
  - 3 TLPL "Văn bản pháp luật doanh nghiệp" loai=VAN_BAN_PL, linh_vuc=DOANH_NGHIEP, NHAP.
  - 2 TLPL "Văn bản về hợp đồng" loai=VAN_BAN_PL, linh_vuc=HOP_DONG, CONG_KHAI.
  - 1 TLPL "Tài liệu nghiên cứu" loai=NGHIEN_CUU, linh_vuc=DOANH_NGHIEP, NHAP.
- **Test Data:** keyword="van ban" (không dấu) + loai_tu_lieu=VAN_BAN_PL + linh_vuc=DOANH_NGHIEP + trang_thai=NHAP.
- **Steps:**
  1. Tab "Tư liệu PL" → filter-bar điền 4 ô.
  2. Click [Tìm kiếm].
- **Expected:**
  - **STATE:** Backend FTS unaccent VN trên `ten_tu_lieu + mo_ta` (BR-DATA-08 line 1569 + line 904) → keyword "van ban" match "Văn bản". WHERE AND `loai_tu_lieu='VAN_BAN_PL' AND linh_vuc_id=DOANH_NGHIEP AND trang_thai='NHAP' AND is_deleted=0 AND don_vi_id IN scope`.
  - **UI:** Hiển thị 3 record (chỉ TLPL VAN_BAN_PL + DOANH_NGHIEP + NHAP). KHÔNG có 2 TLPL HOP_DONG. KHÔNG có 1 TLPL NGHIEN_CUU. Pagination "Tổng: 3".
- **SRS ref:** line 898-907 (6 step Tìm kiếm), line 1567-1571 (BR-DATA-08 FTS unaccent VN).
- **Notes:** Verify FTS match keyword Việt có dấu vs không dấu đều ra cùng kết quả.

### TC-TLPL-010 — Tìm kiếm sanitize SQL injection + max 200 ký tự

- **TraceID:** BR-EC-13 (overview line 105) / SRS line 902
- **Type:** Negative / Edge
- **Priority:** P1
- **Pre-conditions:** cb_nv_tw_01 đăng nhập.
- **Test Data:**
  - Lần 1: keyword="' OR 1=1 --" (SQL injection).
  - Lần 2: keyword=251 ký "A".
- **Steps:**
  1. Filter keyword với payload SQL injection → [Tìm kiếm].
  2. Filter keyword 251 ký → [Tìm kiếm].
- **Expected:**
  - **Lần 1:** Backend sanitize escape → query trở thành literal text "' OR 1=1 --" → empty result. KHÔNG có data leak. Toast INF "Không tìm thấy tư liệu" (SRS Gap nguyên văn — INF-TLPL-01 chưa quote).
  - **Lần 2:** UI inline error hoặc input bị truncate ở 200 ký. Toast "Từ khóa tối đa 200 ký tự" (BR-EC-13).
- **SRS ref:** line 902 (Nhận tiêu chí), BR-EC-13 (overview line 105).
- **Notes:** —

---

## Section E — Công khai BR-FLOW-07 + BR-PUBLIC-01..03

### TC-TLPL-011 — Công khai TLPL Happy: NHAP → CONG_KHAI + auto fill thoi_gian_dang_tai + push API Cổng PLQG (KHÔNG cần phê duyệt)

- **TraceID:** BR-FLOW-07 (line 1579-1583) + BR-PUBLIC-03 (line 1609-1613) / SRS line 845-855
- **Type:** Happy
- **Priority:** P0 🔴
- **Pre-conditions:** cb_nv_tw_01 đăng nhập. TLPL "TLPL-007" trạng thái NHAP + có 1 file PDF đính kèm.
- **Test Data:**
  - mo_ta_cong_khai="Văn bản pháp luật về thuế thu nhập DN — bản tổng hợp 2026"
  - anh_dai_dien=cover.jpg (2MB)
  - file_dinh_kem_cong_khai=appendix.pdf (15MB)
- **Steps:**
  1. Tab "Tư liệu PL" → row TLPL-007 → click [Công khai] (action enable vì NHAP + có file).
  2. Modal "Công khai tư liệu" mở → điền 3 field.
  3. Upload ảnh đại diện + file đính kèm CK.
  4. Click [Công khai].
- **Expected:**
  - **STATE backend** (line 849-854):
    - Bước 2: Kiểm tra ≥1 file đính kèm → PASS.
    - Bước 3: Validate mo_ta_cong_khai not null + ảnh hợp lệ + file CK hợp lệ.
    - Bước 4: SET `cong_khai=1, trang_thai='CONG_KHAI', thoi_gian_dang_tai=NOW()` (BR-PUBLIC-03).
    - Bước 5: Gọi API trực tiếp Cổng PLQG `POST /portal-plqg/tu-lieu` (kèm mô tả + ảnh + file). Cổng trả 200 OK.
    - Bước 6: AUDIT_LOG: hanh_dong='PUBLISH', thoi_gian_dang_tai logged.
  - **KHÔNG cần phê duyệt CB PD** (BR-FLOW-07 line 1581 nguyên văn).
  - **UI:** Loading spinner (gọi Cổng) → toast "Công khai tư liệu thành công lên Cổng PLQG". Modal đóng, badge chuyển CONG_KHAI xanh, hiển thị "Đã đăng tải lúc dd/mm/yyyy HH:mm".
  - **PERSIST:** Reload tab → trạng thái CONG_KHAI giữ. Query Cổng PLQG verify tư liệu hiển thị công khai.
- **SRS ref:** line 845-855 (6 step Công khai), line 1579-1583 (BR-FLOW-07), line 1609-1613 (BR-PUBLIC-03).
- **Notes:** Verify Cổng PLQG API response chứa ma_cong (mã trên Cổng) lưu lại để dùng cho gỡ.

### TC-TLPL-012 — ERR-TLPL-05: Công khai TLPL không có file → reject

- **TraceID:** ERR-TLPL-05 (line 939) / SRS line 850
- **Type:** Negative
- **Priority:** P0 🔴
- **Pre-conditions:** cb_nv_tw_01 đăng nhập. TLPL "TLPL-008" trạng thái NHAP **+ KHÔNG có file đính kèm**.
- **Test Data:** —
- **Steps:**
  1. Tab "Tư liệu PL" → row TLPL-008.
  2. Cố click [Công khai] (action có thể disable hoặc enable tùy UI).
- **Expected:**
  - **Path A (UI disable):** Action [Công khai] disable + tooltip nguyên văn line 939: "Tư liệu chưa có file đính kèm, không thể công khai".
  - **Path B (UI enable + backend reject):** Click [Công khai] → backend bước 2 line 850 fail → toast nguyên văn line 939: "**Tư liệu chưa có file đính kèm, không thể công khai**" (ERR-TLPL-05). KHÔNG SET cong_khai=1.
  - **STATE:** Trạng thái không đổi NHAP. cong_khai=0. thoi_gian_dang_tai=NULL.
- **SRS ref:** line 850 (Bước 2 yêu cầu ≥1 file), line 939 (ERR-TLPL-05).
- **Notes:** —

### TC-TLPL-013 — ERR-TLPL-06 + BR-EC-20 rollback: API Cổng PLQG fail → KHÔNG SET CONG_KHAI

- **TraceID:** ERR-TLPL-06 (line 940) / BR-EC-20 (overview line 107)
- **Type:** Negative / Edge
- **Priority:** P0 🔴
- **Pre-conditions:** cb_nv_tw_01 đăng nhập. TLPL "TLPL-009" NHAP + 1 file. Mock Cổng PLQG endpoint trả 500/timeout.
- **Test Data:** mo_ta_cong_khai="Test rollback" + ảnh + file CK.
- **Steps:**
  1. (Setup mock Cổng PLQG fail).
  2. TLPL-009 → [Công khai] → điền form → submit.
- **Expected:**
  - **STATE backend** (BR-EC-20 transactional consistency):
    - Bước 4 SET cong_khai=1, trang_thai=CONG_KHAI executed trong transaction.
    - Bước 5 API Cổng fail → ROLLBACK transaction.
    - Cuối: cong_khai=0, trang_thai='NHAP', thoi_gian_dang_tai=NULL (không persist change).
    - AUDIT_LOG: hanh_dong='PUBLISH_FAIL' + chi_tiet_loi.
  - **UI:** Toast lỗi nguyên văn line 940: "**Lỗi kết nối Cổng PLQG. Vui lòng thử lại sau**" (ERR-TLPL-06). Modal vẫn mở (cho phép retry). Badge vẫn NHAP.
  - **PERSIST:** Reload → record vẫn NHAP. Query Cổng PLQG → tư liệu KHÔNG xuất hiện.
- **SRS ref:** line 940 (ERR-TLPL-06), BR-EC-20 (KHÔNG set trạng thái trước khi LGSP/Portal API thành công).
- **Notes:** Verify transactional rollback: nếu DB SET trước rồi API fail thì có race condition không? Backend phải dùng 2-phase commit hoặc API call trước khi DB commit.

### TC-TLPL-014 — Edge bật-tắt-bật CONG_KHAI: thoi_gian_dang_tai = lần bật cuối (BR-PUBLIC-03)

- **TraceID:** BR-PUBLIC-03 (line 1609-1613) + BR-PUBLIC-02 (line 1603-1607) / SRS line 856-863
- **Type:** Edge
- **Priority:** P1
- **Pre-conditions:** cb_nv_tw_01 đăng nhập. TLPL "TLPL-010" NHAP + 1 file.
- **Test Data:** —
- **Steps:**
  1. T1=NOW() — Click [Công khai] TLPL-010 → điền form → submit. → CONG_KHAI lần 1, thoi_gian_dang_tai=T1.
  2. Đợi 5 phút.
  3. T2=NOW() — Click [Hủy công khai] → confirm. → NHAP, thoi_gian_dang_tai=NULL (BR-PUBLIC-02 line 1605).
  4. Đợi 5 phút.
  5. T3=NOW() — Click [Công khai] lần 2 → điền form → submit. → CONG_KHAI lần 2, thoi_gian_dang_tai=T3.
  6. `list_network_requests` capture response GET `/api/v1/tu-lieu-phap-ly-vv/{id}` mới nhất → verify field `thoi_gian_dang_tai` trong response body.
- **Expected:**
  - **Step 1:** thoi_gian_dang_tai=T1 (auto fill BR-PUBLIC-03 nguyên văn line 1611). API Cổng push.
  - **Step 3:** thoi_gian_dang_tai=NULL (BR-PUBLIC-02 nguyên văn line 1605 "clear `thoi_gian_dang_tai` = NULL"). API Cổng gỡ.
  - **Step 5:** thoi_gian_dang_tai=T3 (KHÔNG phải T1) — BR-PUBLIC-03 nguyên văn line 1613: "bật-tắt-bật → cập nhật thời điểm bật mới nhất". API Cổng push lần 2.
  - **Step 6 API response:** Body GET TLPL detail có `thoi_gian_dang_tai = T3` (verify qua network capture, không qua DB). UI hiển thị "Đã đăng tải lúc {T3 dd/mm/yyyy HH:mm}".
  - **AUDIT_LOG:** 3 entries: PUBLISH (T1) / UNPUBLISH (T2) / PUBLISH (T3) — verify qua tab Nhật ký UI hoặc accordion timeline.
- **SRS ref:** line 856-863 (Hủy công khai 4 step), line 1603-1607 (BR-PUBLIC-02), line 1609-1613 (BR-PUBLIC-03).
- **Notes:** A7 SỬA — Step 6 chuyển từ "Query DB qtht_01" sang `list_network_requests` verify field `thoi_gian_dang_tai` trong response body GET TLPL detail. Optimistic lock BR-EC-01 (line 103): nếu 2 user cùng [Công khai] cùng TLPL → user thứ 2 nhận ERR-SYS-02 (verify ở edge BR-EC-01 cross-cutting).

---

## Section F — Negative ERR-TLPL-01..02 + WRN coverage

### TC-TLPL-015 — Negative ERR-TLPL-01 + ERR-TLPL-02: Tên trống / VV không tồn tại

- **TraceID:** ERR-TLPL-01 (line 935) + ERR-TLPL-02 (line 936)
- **Type:** Negative
- **Priority:** P1
- **Pre-conditions:** cb_nv_tw_01 đăng nhập.
- **Test Data:**
  - Lần 1: ten_tu_lieu="" (rỗng), noi_dung_tv_id=valid.
  - Lần 2: noi_dung_tv_id="TVCS-INVALID-99999" (không tồn tại), ten_tu_lieu valid.
- **Steps:**
  1. [+ Thêm tư liệu] → bỏ trống ten_tu_lieu → [Lưu].
  2. API direct POST với noi_dung_tv_id không hợp lệ (UI dùng searchable select, bypass).
- **Expected:**
  - **Lần 1:** Reject. Inline error nguyên văn line 935: "**Tên tư liệu là bắt buộc**" (ERR-TLPL-01). Focus field tên. Form không đóng.
  - **Lần 2:** Backend FK check fail. HTTP 400 với message nguyên văn line 936: "**Vụ việc tư vấn không tồn tại**" (ERR-TLPL-02).
  - **STATE:** Cả 2 lần KHÔNG INSERT TU_LIEU_PHAP_LY_VV.
- **SRS ref:** line 935 (ERR-TLPL-01), line 936 (ERR-TLPL-02).
- **Notes:** Boundary case TVCS đã soft delete (is_deleted=1) → cũng trả ERR-TLPL-02 (assumption SRS không quote rõ "đã bị xóa" cho TLPL như HSPL — SPEC-CLARIFY-TLPL-02).

---

## Section G — Edge bổ sung A4 (State race + boundary file + cross-feature)

### TC-TLPL-016 — Edge race: toggle CONG_KHAI vs DELETE 2 user concurrent

- **TraceID:** BR-EC-01 (optimistic lock) + BR-EC-20 (transactional)
- **Type:** Edge
- **Priority:** P1
- **Pre-conditions:** cb_nv_tw_01 + cb_nv_tw_02 cùng đơn vị BTP-TW. TLPL "TLPL-RACE" trạng thái NHAP có 1 file. Cả 2 user mở tab "Tư liệu PL" cùng lúc, updated_at=T0.
- **Test Data:** —
- **Steps:**
  1. cb_nv_tw_01 click [Công khai] TLPL-RACE → điền form → submit (T1).
  2. cb_nv_tw_02 (đã mở từ T0) click [Xóa] TLPL-RACE → confirm modal → submit (T2 sau T1 ~1s).
- **Expected:**
  - **User 1 success:** trang_thai=CONG_KHAI, cong_khai=1, API Cổng push thành công.
  - **User 2 receive ERR-SYS-02:** "Bản ghi đã bị thay đổi bởi người khác. Vui lòng tải lại trang" (BR-EC-01 optimistic lock). KHÔNG soft delete. KHÔNG gọi API Cổng PLQG gỡ (vì Cổng vừa nhận push).
  - **STATE:** is_deleted=0, trang_thai=CONG_KHAI. Cổng PLQG có tư liệu hiển thị.
  - **AUDIT_LOG:** 1 entry PUBLISH (user 1) + 1 entry attempt-failed DELETE (user 2).
- **SRS ref:** BR-EC-01 line 103 + BR-EC-20 line 107.
- **Notes:** SPEC-CLARIFY-TLPL-EDGE-01 — Reverse case (DELETE first, PUBLISH second) chưa cover; assumption: user 2 nhận "Tư liệu đã bị xóa".

### TC-TLPL-017 — Edge boundary file đính kèm: 20MB exact / 20MB+1 byte (extends ERR-TLPL-03)

- **TraceID:** ERR-TLPL-03 (line 937)
- **Type:** Edge
- **Priority:** P1
- **Pre-conditions:** cb_nv_tw_01 đăng nhập. TLPL "TLPL-BOUND" NHAP.
- **Test Data:**
  - Lần 1: file_20mb_exact.pdf (20971520 byte = 20MB exact).
  - Lần 2: file_20mb_plus_1.pdf (20971521 byte).
- **Steps:**
  1. TLPL-BOUND → [Upload file] → file 20MB exact → submit.
  2. Repeat với file 20MB+1 byte.
- **Expected:**
  - **Lần 1:** PASS, INSERT FILE_DINH_KEM với size=20971520. Boundary inclusive at 20MB exact.
  - **Lần 2:** Reject. Toast nguyên văn line 937 "File tối đa 20MB" (ERR-TLPL-03). KHÔNG INSERT.
- **SRS ref:** line 937 (ERR-TLPL-03 max 20MB).
- **Notes:** A4 boundary triple — extends TC-TLPL-008 single-case. Verify content-length header và actual stored size.

### TC-TLPL-018 — Edge API Cổng PLQG timeout 30s khi PUBLISH → rollback nhưng UI cho phép retry

- **TraceID:** ERR-TLPL-06 (line 940) + BR-EC-20
- **Type:** Edge / Error injection
- **Priority:** P1
- **Pre-conditions:** cb_nv_tw_01 đăng nhập. TLPL "TLPL-TIMEOUT" NHAP có 1 file. Mock Cổng PLQG endpoint delay 35s (>30s timeout threshold).
- **Test Data:** mo_ta_cong_khai="Test timeout" + ảnh + file CK.
- **Steps:**
  1. (Setup mock Cổng delay 35s).
  2. TLPL-TIMEOUT → [Công khai] → điền form → submit.
  3. Đợi 30-35s.
  4. Quan sát UI + DB state.
  5. Click [Công khai] lần 2 (mock đã trở về 200 OK).
- **Expected:**
  - **Step 3-4:** Backend timeout sau 30s → rollback transaction. trang_thai=NHAP, cong_khai=0. Toast nguyên văn line 940 "Lỗi kết nối Cổng PLQG. Vui lòng thử lại sau" (ERR-TLPL-06). Modal vẫn mở để retry. SPEC-CLARIFY-TLPL-DELETE-01 confirm policy = no async queue, full rollback.
  - **Step 5:** Retry thành công, trang_thai=CONG_KHAI. KHÔNG có duplicate trên Cổng PLQG (vì lần 1 rollback nên không persist).
  - **AUDIT_LOG:** 1 entry PUBLISH_FAIL (lần 1) + 1 entry PUBLISH success (lần 2).
- **SRS ref:** line 940 (ERR-TLPL-06) + BR-EC-20 transactional consistency.
- **Notes:** SPEC-CLARIFY-TLPL-DELETE-01 đã pending — verify timeout là 30s exact. No SRS quote timeout interval — best practice extrapolation.

### TC-TLPL-019 — Edge cross-feature: NHAP→CONG_KHAI khi parent TVCS bị HUY (state inconsistency)

- **TraceID:** BR-FLOW-07 + cross-state validation
- **Type:** Edge
- **Priority:** P1
- **Pre-conditions:** cb_nv_tw_01 đăng nhập. TVCS "TVCS-PARENT" trạng thái DANG_TU_VAN. TLPL "TLPL-CHILD" thuộc TVCS-PARENT, NHAP, có 1 file. Sau đó TVCS-PARENT chuyển HUY (T9).
- **Test Data:** —
- **Steps:**
  1. Setup: tạo TVCS-PARENT DANG_TU_VAN + TLPL-CHILD NHAP có file.
  2. Chuyển TVCS-PARENT → HUY (qua action [Hủy yêu cầu] với DN đồng ý + CB PD duyệt).
  3. Mở TVCS-PARENT detail → tab "Tư liệu PL" → row TLPL-CHILD.
  4. Cố click [Công khai].
- **Expected:**
  - **Step 3:** Tab "Tư liệu PL" hiển thị TLPL-CHILD (read-only) với badge "NHAP" + warning banner "TVCS đã hủy".
  - **Step 4:** Action [Công khai] disable hoặc backend reject với message "Không thể công khai tư liệu thuộc TVCS đã hủy" (SRS Gap nguyên văn). cong_khai vẫn=0.
  - **STATE:** TLPL-CHILD vẫn NHAP. KHÔNG gọi API Cổng PLQG.
- **SRS ref:** line 845-855 (Processing CK) + BR-FLOW-07 + line 1492 (T10 HUY).
- **Notes:** No SRS quote về parent TVCS HUY block child TLPL public — best practice extrapolation per state consistency. SPEC-CLARIFY-TLPL-EDGE-02.

### TC-TLPL-020 — Edge multiple file CK chain: 5 file lần lượt push Cổng PLQG → atomicity

- **TraceID:** BR-EC-20 + line 854 (API Cổng push)
- **Type:** Edge
- **Priority:** P2
- **Pre-conditions:** cb_nv_tw_01 đăng nhập. TLPL "TLPL-MULTI" NHAP có 5 file PDF (mỗi file 5MB). Mock Cổng PLQG: file 1+2+3 OK, file 4 fail 500.
- **Test Data:** —
- **Steps:**
  1. (Setup mock).
  2. TLPL-MULTI → [Công khai] với 5 file → submit.
  3. Quan sát network + DB state.
- **Expected:**
  - **Path A (Atomic - all-or-nothing):** Backend gửi 5 file lên Cổng. File 4 fail → rollback toàn bộ transaction → trang_thai=NHAP, KHÔNG có file nào trên Cổng. Toast ERR-TLPL-06.
  - **Path B (Best-effort):** File 1+2+3 trên Cổng, file 4+5 chưa. Backend retry queue async cho file 4+5. trang_thai=CONG_KHAI partial. Warning toast "3/5 file đã đăng tải, 2 file đang thử lại".
  - Default test: **Path A** (BR-EC-20 transactional consistency strict). Verify Phase B BA respond.
- **SRS ref:** line 854 (Bước 5 API Cổng push) + BR-EC-20.
- **Notes:** SPEC-CLARIFY-TLPL-EDGE-03 — multi-file atomicity policy. Phase B BA respond.

### TC-TLPL-021 — UC152 AC-5: Xem file đính kèm trực tuyến (preview) không trigger download

- **TraceID:** FR-X.1-06 / SRS line 949 (AC-5 xem file trực tuyến)
- **Type:** Happy
- **Priority:** P1
- **Pre-conditions:**
  - cb_nv_tw_01 đăng nhập.
  - TLPL "TLPL-PREVIEW-001" có 2 file: `doc1.pdf` (5MB) + `doc2.docx` (2MB) đã đính kèm.
- **Test Data:** —
- **Steps:**
  1. Login cb_nv_tw_01 → mở chi tiết TVCS chứa TLPL-PREVIEW-001.
  2. Tab "Tư liệu PL" → click [Xem] hoặc tên TLPL-PREVIEW-001 → modal/page chi tiết mở.
  3. Section "File đính kèm" → click nút [Xem preview] / icon mắt trên row `doc1.pdf`.
  4. `list_network_requests` capture GET file URL.
  5. `take_snapshot` viewer area / new tab.
  6. Verify response header `Content-Disposition`.
  7. Repeat với `doc2.docx`.
  8. Click [Tải xuống] (so sánh) → quan sát Content-Disposition khác.
- **Expected:**
  - **Bước 3-5:** PDF render trong viewer inline (`<iframe>`, modal viewer hoặc tab mới với plugin browser PDF viewer). KHÔNG trigger save dialog.
  - **Bước 6 preview:** Response header `Content-Disposition: inline; filename="doc1.pdf"` + Content-Type=application/pdf.
  - **Bước 7 (.docx):** Hoặc render qua Office Online viewer / Google Docs viewer / convert preview, hoặc fallback message "Định dạng .docx không hỗ trợ preview, vui lòng tải xuống" (SPEC-CLARIFY).
  - **Bước 8 download:** Response header `Content-Disposition: attachment; filename="doc1.pdf"` → trigger save dialog.
  - File URL không expose token raw trong query string (BR-EC-03 secure URL).
- **SRS ref:** line 949 (AC-5: Given user mở chi tiết tư liệu When click file đính kèm Then xem file trực tuyến không cần download).
- **Notes:** A6 fill A5-G4 (UC152 AC-5). SPEC-CLARIFY-TLPL-PREVIEW-01: SRS không quote định dạng nào hỗ trợ preview (PDF chắc chắn, DOCX/XLS có thể fallback). Phase B verify danh sách định dạng hỗ trợ thực tế.

---

**Tổng số TC: 21**
