# Test Cases — Tab Hồ sơ pháp lý DN (SCR-V.III-02 Tab 2, gộp từ MH-12.3 SCR-X1-03 DEPRECATED)

> **SRS Ref**: FR-X.1-04 (UC150) — `srs-fr-12-tv-chuyen-sau-v3.1.md:513-672`, SCR-V.III-02 Tab 2 (`srs-fr-07-doanh-nghiep-v3.1.md:347`), Entity HO_SO_PHAP_LY_DN §3.4.3.46
> **Nguồn**: NotebookLM `4dd0675e-a4fa-4ea6-80ae-48e76b3fa264` + LOCAL `srs-fr-12-tv-chuyen-sau-v3.1.md:513-672`
> **Ngày tạo**: 2026-05-09
> **Note v2.1**: SCR-X1-03 DEPRECATED → CRUD HSPL chuyển sang **Tab 2 trong SCR-V.III-02 chi tiết DN**. Mỗi DN có nhiều HSPL.

---

## A. UI FIELD VERIFICATION

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|---------|---------------|----------------|-----------|--------------------|-------------------|------|
| TC-HSPL-UI-01 | SCR-V.III-02 Tab 2 / Table 8 cột | Verify table HSPL trong Tab 2 | cb_nv_tw_01, DN-TW-001 có ≥3 HSPL | URL `/doanh-nghiep/DN-TW-001` Tab 2 | 1. Mở Tab 2<br>2. Verify | **TABLE COLUMNS** (per srs-fr-12:629-640): Mã HS (HSPL-{YYYYMMDD}-{SEQ}), Tên HS, Loại HS, Ngày cấp, Ngày hết hạn, Trạng thái (HIEU_LUC/HET_HAN/THU_HOI badge), Có file (icon), Hành động (Sửa/Xóa)<br>**TOOLBAR**: Nút "Thêm hồ sơ pháp lý" + Search + Filter loai + Filter trạng thái | Happy 🔴 |
| TC-HSPL-UI-02 | FR-X.1-04 / Form Thêm/Sửa 11 trường | Verify form HSPL | cb_nv_tw_01, DN-TW-001 | Click "Thêm hồ sơ" | 1. Click thêm<br>2. Verify modal/form | **11 FIELDS** (per srs-fr-12:534-546): (1) ma_ho_so auto-readonly, (2) doanh_nghiep_id auto-fill DN-TW-001 readonly, (3) ten_ho_so text 500 char Y, (4) loai_ho_so select 5 enum Y, (5) linh_vuc_id select N, (6) ngay_cap date N, (7) ngay_het_han date N, (8) co_quan_cap text N, (9) mo_ta textarea N, (10) trang_thai select 3 enum default HIEU_LUC Y, (11) file_dinh_kem upload PDF/image 20MB N | Happy 🔴 |

## B. CREATE HSPL

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|---------|---------------|----------------|-----------|--------------------|-------------------|------|
| TC-HSPL-001 | FR-X.1-04 AC3 / Create happy 5 loại | Tạo HSPL loại GIAY_PHEP | cb_nv_tw_01, DN-TW-001 | ten_ho_so: "GP kinh doanh 2026", loai: GIAY_PHEP, ngay_cap: 2026-01-15, trang_thai: HIEU_LUC | 1. Click "Thêm hồ sơ"<br>2. Fill form<br>3. Submit | **STATE**: Network `POST /api/v1/ho-so-phap-ly-dn` body chứa data; response 201 + auto-gen ma_ho_so HSPL-20260509-001<br>**UI**: Toast "Tạo thành công"; modal đóng; table reload có row mới<br>**AUDIT_LOG**: hanh_dong=CREATE entity=HO_SO_PHAP_LY_DN | Happy 🔴 |
| TC-HSPL-002 | FR-X.1-04 / Create HOP_DONG | Tạo HSPL loại HOP_DONG | cb_nv_tw_01 | loai: HOP_DONG, các trường còn lại mặc định | 1. Tương tự | Auto-gen mã HSPL-{date}-{seq}; trang_thai default HIEU_LUC | Happy 🟡 |
| TC-HSPL-003 | FR-X.1-04 / Create GIAY_CN | Tạo HSPL loại GIAY_CN | cb_nv_tw_01 | loai: GIAY_CN | 1. Submit | Tạo PASS | Happy 🟡 |
| TC-HSPL-004 | FR-X.1-04 / Create QUYET_DINH | Tạo HSPL loại QUYET_DINH | cb_nv_tw_01 | loai: QUYET_DINH | 1. Submit | Tạo PASS | Happy 🟡 |
| TC-HSPL-005 | FR-X.1-04 / Create KHAC | Tạo HSPL loại KHAC | cb_nv_tw_01 | loai: KHAC | 1. Submit | Tạo PASS | Happy 🟡 |
| TC-HSPL-006 | FR-X.1-04 / ERR-HSPL-01 | Tên HS rỗng → ERR-HSPL-01 | cb_nv_tw_01 | ten_ho_so: "" | 1. Submit form | **UI**: Inline error "Tên hồ sơ pháp lý là bắt buộc" (NGUYÊN VĂN ERR-HSPL-01) | Negative 🔴 |
| TC-HSPL-007 | FR-X.1-04 / ERR-HSPL-05 | Loại HS không hợp lệ → ERR-HSPL-05 | cb_nv_tw_01 | DevTools tamper loai_ho_so: "INVALID" | 1. DevTools fetch POST<br>2. Verify | API 422 "Loại hồ sơ '{loai}' không hợp lệ" (NGUYÊN VĂN ERR-HSPL-05) | Negative 🟡 |
| TC-HSPL-008 | FR-X.1-04 / ten_ho_so 500 char boundary | Boundary 500 char | cb_nv_tw_01 | ten_ho_so: 500 char string | 1. Submit | PASS — accept đúng 500; SPEC-CLARIFY-DN-12 nếu UI không có maxlength | Edge 🟡 |
| TC-HSPL-009 | FR-X.1-04 / ten_ho_so 501 over | 501 char → reject | cb_nv_tw_01 | ten_ho_so: 501 char | 1. Submit | Reject; UI inline error "Tên hồ sơ tối đa 500 ký tự" | Negative 🟡 |
| TC-HSPL-008b | A6-fill ERR-HSPL-02 / DN không tồn tại (A7 SỬA UI bridge) | Tạo HSPL với doanh_nghiep_id soft-deleted (UI sẵn có) | cb_nv_tw_01 | Soft delete DN-TW-097 trước; sau đó user khác mở Tab 2 DN-097 (chưa reload) | 1. User A xóa DN-TW-097 ở module DN<br>2. User B (cb_nv_tw_02) đã mở Tab 2 DN-097 trước (cached state), tạo HSPL<br>3. Submit | API 404 hoặc 422 "Doanh nghiệp không tồn tại hoặc đã bị xóa" (NGUYÊN VĂN ERR-HSPL-02); KHÔNG tạo HSPL; race condition realistic | Negative 🟡 |

## C. UPDATE HSPL

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|---------|---------------|----------------|-----------|--------------------|-------------------|------|
| TC-HSPL-101 | FR-X.1-04 AC4 / Update happy | Sửa HSPL — đổi trạng thái HIEU_LUC → HET_HAN | cb_nv_tw_01, HSPL-20260509-001 | trang_thai: HET_HAN | 1. Click row Sửa<br>2. Đổi trạng thái<br>3. Submit | PUT /api/v1/ho-so-phap-ly-dn/{id}; reload — badge HET_HAN; AUDIT_LOG hanh_dong=UPDATE | Happy 🔴 |
| TC-HSPL-102 | FR-X.1-04 / Update trang_thai THU_HOI | Đổi trạng thái → THU_HOI | cb_nv_tw_01 | trang_thai: THU_HOI | 1. Submit | Badge THU_HOI; AUDIT log | Happy 🟡 |
| TC-HSPL-103 | FR-X.1-04 / Update mã HS readonly | ma_ho_so KHÔNG sửa được | cb_nv_tw_01, HSPL-20260509-001 | DevTools sửa ma_ho_so | 1. Mở edit<br>2. Verify field<br>3. DevTools tamper input value<br>4. Submit | UI input ma_ho_so disabled/readonly; nếu DevTools tamper PUT body — backend ignore (auto-gen immutable) | Negative 🟡 |
| TC-HSPL-104 | A6-fill SM-HSPL / HET_HAN → HIEU_LUC restore | Restore HSPL HET_HAN về HIEU_LUC (gia hạn) | cb_nv_tw_01, HSPL-001 trang_thai=HET_HAN | trang_thai: HIEU_LUC | 1. Edit<br>2. Đổi trạng thái<br>3. Submit | PASS — badge HIEU_LUC; AUDIT_LOG ghi UPDATE; SPEC-CLARIFY-DN-44 nếu BA muốn block transition này (HET_HAN không nên restore?) | Happy 🟡 |
| TC-HSPL-105 | A6-fill SM-HSPL / THU_HOI → HIEU_LUC restore | Restore HSPL THU_HOI về HIEU_LUC | cb_nv_tw_01, HSPL-002 THU_HOI | trang_thai: HIEU_LUC | 1. Edit<br>2. Submit | PASS hoặc SPEC-CLARIFY-DN-44 (THU_HOI thường irreversible per nghiệp vụ pháp luật); SRS không define rõ | Happy 🟡 |

## D. DELETE HSPL (Soft delete)

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|---------|---------------|----------------|-----------|--------------------|-------------------|------|
| TC-HSPL-201 | FR-X.1-04 AC5 / Delete happy | Xóa HSPL → soft delete | cb_nv_tw_01, HSPL-20260509-002 | — | 1. Click icon Xóa<br>2. Confirm modal "Bạn có chắc chắn muốn xóa hồ sơ '{tên}'?" (NGUYÊN VĂN per srs:593) | DELETE thành công; row biến mất; DB is_deleted=1 (BR-DATA-01); AUDIT_LOG hanh_dong=DELETE | Happy 🔴 |
| TC-HSPL-202 | FR-X.1-04 / Cancel delete | Cancel modal → không xóa | cb_nv_tw_01 | — | 1. Click Xóa<br>2. Cancel | Row giữ nguyên | Happy 🟡 |

## E. SEARCH HSPL trong Tab

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|---------|---------------|----------------|-----------|--------------------|-------------------|------|
| TC-HSPL-301 | FR-X.1-04 / Search keyword | Tìm theo từ khóa (mã HS / tên DN / tên HS) | cb_nv_tw_01, ≥3 HSPL | keyword: "GP kinh" | 1. Nhập keyword<br>2. Search | Table chỉ HSPL match keyword (per srs:552) | Happy 🟡 |
| TC-HSPL-302 | FR-X.1-04 / Filter loai | Filter loai = GIAY_PHEP | cb_nv_tw_01, mixed loai | loai: GIAY_PHEP | 1. Filter<br>2. Verify | Chỉ HSPL loại GIAY_PHEP | Happy 🟡 |
| TC-HSPL-303 | FR-X.1-04 / Filter trang_thai | Filter trang_thai = HIEU_LUC | cb_nv_tw_01 | trang_thai: HIEU_LUC | 1. Filter<br>2. Verify | Chỉ HIEU_LUC | Happy 🟡 |
| TC-HSPL-304 | FR-X.1-04 / Filter date range | Filter ngay_cap từ-đến | cb_nv_tw_01 | tu_ngay/den_ngay | 1. Pick range<br>2. Verify | HSPL trong range | Happy 🟡 |
| TC-HSPL-305 | FR-X.1-04 / ERR-HSPL-06 | tu_ngay > den_ngay → ERR-HSPL-06 | cb_nv_tw_01 | tu_ngay: 2026-05-09, den_ngay: 2026-05-01 | 1. Pick reversed<br>2. Search | UI inline "Ngày bắt đầu phải trước ngày kết thúc" (NGUYÊN VĂN ERR-HSPL-06) | Negative 🟡 |
| TC-HSPL-306 | FR-X.1-04 / INF-HSPL-01 | Không có kết quả → INF-HSPL-01 | cb_nv_tw_01 | keyword: "ZZZZ" | 1. Search | Empty state "Không tìm thấy hồ sơ pháp lý phù hợp" (NGUYÊN VĂN INF-HSPL-01) | Negative 🟡 |
| TC-HSPL-307 | FR-X.1-04 / AC7 AND multi-filter | Multi-filter AND | cb_nv_tw_01 | loai+trang_thai+keyword | 1. Set 3 filter<br>2. Search | AND logic | Happy 🟡 |

## F. UPLOAD FILE đính kèm

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|---------|---------------|----------------|-----------|--------------------|-------------------|------|
| TC-HSPL-401 | FR-X.1-04 / Upload PDF 5MB happy | Upload file PDF 5MB | cb_nv_tw_01, HSPL-001 | file: gp.pdf 5MB | 1. Mở edit<br>2. Click upload<br>3. Chọn file<br>4. Submit | Network multipart; response file_id; co_file=true; FILE_DINH_KEM table có row | Happy 🔴 |
| TC-HSPL-402 | FR-X.1-04 / ERR-HSPL-03 20MB boundary | Upload file 21MB → ERR-HSPL-03 | cb_nv_tw_01 | file: big.pdf 21MB | 1. Upload | UI block + toast "File đính kèm tối đa 20MB" (NGUYÊN VĂN ERR-HSPL-03); Network 413 hoặc client-side reject | Negative 🔴 |
| TC-HSPL-403 | FR-X.1-04 / 20MB exact boundary | Upload exact 20MB | cb_nv_tw_01 | file: 20MB | 1. Upload | PASS — INCLUSIVE 20MB | Edge 🟡 |
| TC-HSPL-404 | FR-X.1-04 / ERR-HSPL-04 virus | File chứa mã độc → ERR-HSPL-04 | cb_nv_tw_01 | file: eicar.com test virus | 1. Upload | API response 400 "File 'eicar.com' chứa mã độc, không thể tải lên" (NGUYÊN VĂN ERR-HSPL-04); SPEC-CLARIFY-DN-13 nếu antivirus chưa setup | Negative 🟡 |
| TC-HSPL-405 | FR-X.1-04 / Upload image | Upload PNG/JPG | cb_nv_tw_01 | file: scan.png 2MB | 1. Upload | PASS — image accepted (per srs:546 "PDF/image") | Happy 🟡 |
| TC-HSPL-406 | FR-X.1-04 / Upload .exe reject | Upload .exe → reject | cb_nv_tw_01 | file: bad.exe | 1. Upload | UI block "Chỉ chấp nhận PDF/image"; SPEC-CLARIFY-DN-14 nếu SRS không có ERR code cho file type | Negative 🟡 |

## G. VIEW DETAIL HSPL

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|---------|---------------|----------------|-----------|--------------------|-------------------|------|
| TC-HSPL-501 | FR-X.1-04 / View detail (A6 strengthen) | Click row → mở chi tiết HSPL với file metadata đầy đủ | cb_nv_tw_01, HSPL-001 có 2 file (a.pdf 5MB, b.png 1MB) | — | 1. Click row HSPL | Modal/Drawer chứa: (1) Full 11 trường HSPL, (2) DS file 2 row với metadata: tên file (a.pdf), loại (PDF), dung lượng (5MB/1MB format human-readable), URL preview/download (per srs-fr-12:614), (3) Nút "Tải" mỗi file | Happy 🟡 |
| TC-HSPL-502 | FR-X.1-04 / Download file | Click "Tải" file đính kèm | cb_nv_tw_01 | — | 1. Click Tải | File download; Network GET có URL preview/download | Happy 🟡 |

## H. CROSS-DN

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|---------|---------------|----------------|-----------|--------------------|-------------------|------|
| TC-HSPL-601 | FR-X.1-04 / HSPL liên kết đúng DN | HSPL chỉ thuộc DN của Tab | cb_nv_tw_01, DN-TW-001 có 3 HSPL, DN-TW-002 có 2 HSPL | — | 1. Mở Tab 2 DN-TW-001<br>2. Verify count<br>3. Mở Tab 2 DN-TW-002 | Tab 2 DN-001: 3 row; Tab 2 DN-002: 2 row; KHÔNG cross-DN leak | Happy 🔴 |
| TC-HSPL-602 | FR-X.1-04 / Pagination | HSPL >20 → phân trang BR-DATA-07 | cb_nv_tw_01, DN-001 có 25 HSPL | — | 1. Tab 2<br>2. Pagination | Default 20/page; click trang 2 → 5 row tiếp | Happy 🟡 |

---

## I. EDGE bổ sung (A4 inline merge — 6 edge)

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|---------|---------------|----------------|-----------|--------------------|-------------------|------|
| TC-HSPL-701 | EDGE-A4-q / Concurrent CREATE | 2 user tạo HSPL cùng DN cùng giây | cb_nv_tw_01 + cb_nv_tw_02 đồng thời tạo HSPL cho DN-001 | — | 1. 2 POST đồng thời | Cả 2 PASS với 2 ma_ho_so khác nhau (HSPL-{date}-001, HSPL-{date}-002); SEQ tăng atomically (BR-DATA-04) | Edge 🟡 |
| TC-HSPL-702 | EDGE-A4-r / ngay_cap > ngay_het_han | Logical ngày cấp > ngày hết hạn | cb_nv_tw_01 | ngay_cap: 2026-12-31, ngay_het_han: 2026-01-01 | 1. Submit | Inline error "Ngày hết hạn phải sau ngày cấp"; SPEC-CLARIFY-DN-32 nếu SRS không có ERR (form Inputs FR-X.1-04 không có CHECK constraint giữa 2 trường) | Edge 🟡 |
| TC-HSPL-703 | EDGE-A4-s / DELETE HSPL có file orphan | Soft delete HSPL có file → file orphan | cb_nv_tw_01, HSPL-001 có 2 file | — | 1. Delete HSPL-001<br>2. Verify FILE_DINH_KEM | FILE_DINH_KEM table: 2 row vẫn tồn tại (cascade soft-delete hoặc orphan); SPEC-CLARIFY-DN-33 cascade policy | Edge 🟡 |
| TC-HSPL-704 | EDGE-A4-t / File extension spoofing | File .jpg đổi tên .pdf upload | cb_nv_tw_01 | bad.pdf nhưng content là .exe | 1. Upload | Server detect MIME mismatch → reject; antivirus check (ERR-HSPL-04 nếu virus); SPEC-CLARIFY-DN-34 | Edge 🔴 |
| TC-HSPL-705 | EDGE-A4-u / ten_ho_so XSS | XSS payload trong ten_ho_so | cb_nv_tw_01 | ten_ho_so: `<script>alert(1)</script>` | 1. Submit<br>2. Mở list | Sanitize escape; hiển thị literal | Edge 🔴 |
| TC-HSPL-706 | EDGE-A4-v / Bulk delete sequence | Xóa 5 HSPL liên tiếp nhanh | cb_nv_tw_01, DN có 5 HSPL | — | 1. Click 5 nút Xóa liên tiếp<br>2. Confirm tất cả | 5 row biến mất; Network 5 DELETE; AUDIT_LOG 5 row; KHÔNG race condition | Edge 🟡 |

---

**Tổng số TC**: 40 (2 UI + 10 Create + 5 Update + 2 Delete + 7 Search + 6 Upload + 2 Detail + 2 Cross-DN + 6 Edge A4 — sau A6 +3: TC-HSPL-008b/104/105 + strengthen 501)
