# Test Cases — UC55 (CMS phần): Tiếp nhận hồ sơ từ HT khác — DS / Search / Delete (FR-V.I-05)

> **SRS Ref**: FR-V.I-05 (srs-fr-05:363-490) — **CHỈ phần CMS** (Inputs/Processing/Outputs CMS); A7 LOẠI nhánh API Inbound.
> **Ngày tạo**: 2026-05-06 (BMAD A3) · **A7 filter applied**: 2026-05-06
> **Tài khoản chính**: `cb_nv_tw_01` (CB NV TW — quyền "Quản lý hồ sơ VV", scope toàn quốc), `cb_nv_tw_02` (concurrent), `qtht_01` (admin verify audit).
> **A7 note**: Toàn bộ TC API Inbound (E1..E5 inbound, EC-V.I-05-01..12 inbound) đã LOẠI — hệ thống bên ngoài. Chỉ giữ TC liên quan UI CMS DS/Search/Delete + verify side-effects qua `list_network_requests`.

---

## A. UI FIELD VERIFICATION

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước | Kết quả mong đợi | Type | Priority |
|----|---------|--------------|----------------|-----------|----------|------------------|------|----------|
| TC-VV-HK-UI-01 | FR-V.I-05 / SCR-V.I-01 (filter HT_KHAC) | Verify trang DS HS từ HT khác: filter-bar (keyword + he_thong_nguon + date range) + table cột | `cb_nv_tw_01`. Login → vào "Vụ việc > Hồ sơ từ HT khác" (filter `kenh=HE_THONG_KHAC`). Có ≥3 VV kênh HT khác. | — | 1. Quan sát breadcrumb. 2. Quan sát filter-bar. 3. Quan sát table header. 4. Quan sát hàng action. | **UI**: (1) Breadcrumb "Trang chủ > Vụ việc > Hồ sơ từ HT khác". (2) Filter-bar 4 control: ô keyword (placeholder "Mã hồ sơ / Tên DN / HT nguồn") + dropdown `he_thong_nguon_filter` (load từ DANH_MUC `loai='HE_THONG_NGUON'` trang_thai=1) + DateRange (`tu_ngay`/`den_ngay`) + nút [Tìm] [Xóa] (srs-fr-05:391-396). (3) Table header 9 cột: ma_vu_viec / he_thong_nguon / ma_ho_so_nguon / ten_doanh_nghiep / noi_dung_yeu_cau (rút gọn ≤80 ký tự + tooltip) / trang_thai / ngay_tiep_nhan / [Hành động] (srs-fr-05:432-444). (4) Cột hành động hiển thị nút [Xem] cho mọi VV; nút [Xóa] CHỈ hiện khi `trang_thai=CHO_TIEP_NHAN` (srs-fr-05:451 + Processing CMS step 5). | Happy | P1 |

---

## B. CRUD HAPPY PATH

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước | Kết quả mong đợi | Type | Priority |
|----|---------|--------------|----------------|-----------|----------|------------------|------|----------|
| TC-VV-HK-101 | FR-V.I-05 AC3 / Processing CMS B2 | Hiển thị DS VV kênh HE_THONG_KHAC chưa xóa, scope theo đơn vị | `cb_nv_tw_01` (TW). Có ≥5 VV `kenh=HE_THONG_KHAC` thuộc nhiều đơn vị (TW + BN + DP-AG). | — | 1. Login. 2. Vào DS HS từ HT khác. | **STATE**: Backend `WHERE kenh='HE_THONG_KHAC' AND is_deleted=0` + scope đơn vị (BR-AUTH-08, srs-fr-05:417). CB NV TW thấy toàn quốc (BR-AUTH-03/04). **UI**: Bảng hiện ≥5 VV. Pagination "1-20 / N" (default page=1, size=20 — srs-fr-05:396). **PERSIST**: AUDIT_LOG SELECT (verify gián tiếp qua `list_network_requests` GET `/vu-viec?kenh=HE_THONG_KHAC` 200). | Happy | P0 |
| TC-VV-HK-102 | FR-V.I-05 AC4 / Processing CMS B4 | Search keyword theo mã hồ sơ nguồn + tên DN + HT nguồn | `cb_nv_tw_01`. VV-HK-001 (`ma_ho_so_nguon=HSN-2026-001`, DN "Cty TNHH An Phát", HT nguồn "DVC-BTP"). | keyword="An Phát" | 1. Vào DS. 2. Gõ "An Phát" vào ô keyword. 3. Click [Tìm]. | **STATE**: Backend `WHERE (ma_ho_so_nguon LIKE %?% OR ten_doanh_nghiep LIKE %?% OR he_thong_nguon LIKE %?%)` + filter HT_KHAC + scope (srs-fr-05:393, 420). **UI**: Bảng chỉ hiện VV-HK-001. Pagination cập nhật count. **PERSIST**: — | Happy | P0 |
| TC-VV-HK-103 | FR-V.I-05 / Processing CMS B4 | Filter `he_thong_nguon` + date range combine | `cb_nv_tw_01`. ≥3 HT nguồn distinct ("DVC-BTP", "TTHC-XXX", "VBQPPL"). VV trong khoảng 2026-04-01..2026-04-30 = 5 record cho "DVC-BTP". | he_thong_nguon="DVC-BTP", tu_ngay=2026-04-01, den_ngay=2026-04-30 | 1. Chọn HT nguồn "DVC-BTP". 2. Set date range. 3. [Tìm]. | **STATE**: Backend `WHERE kenh=HE_THONG_KHAC AND he_thong_nguon='DVC-BTP' AND ngay_tiep_nhan BETWEEN ?...?` (srs-fr-05:394-395). **UI**: Bảng hiện đúng 5 VV. URL có thể chứa query params (verify deep-link — nếu không có → mark **SPEC-CLARIFY-VV-HK-01**). **PERSIST**: — | Happy | P1 |
| TC-VV-HK-104 | FR-V.I-05 AC / Processing CMS B3 | Click [Xem] → modal/page chi tiết HS từ HT khác (DN + file đính kèm) | `cb_nv_tw_01`. VV-HK-001 có 2 file đính kèm (PDF + DOCX). | — | 1. Click [Xem] dòng VV-HK-001. | **STATE**: Backend GET `/vu-viec/{id}` join DOANH_NGHIEP + FILE_DINH_KEM (srs-fr-05:419). **UI**: Modal/page hiện thông tin DN (ten / ma_so_thue / dia_chi / nguoi_dai_dien / sdt / email) + nội dung yêu cầu + danh sách 2 file (tên / kích thước / nút [Xem]/[Tải]) + trạng thái CHO_TIEP_NHAN + ngày tiếp nhận từ API. **PERSIST**: — | Happy | P1 |
| TC-VV-HK-105 | FR-V.I-05 AC / Processing CMS B5 / BR-DATA-01 | Xóa mềm HS đang ở CHO_TIEP_NHAN | `cb_nv_tw_01`. VV-HK-DEL-01 ở `trang_thai=CHO_TIEP_NHAN`. | — | 1. Click [Xóa] dòng VV-HK-DEL-01. 2. Confirm modal "Xác nhận xóa hồ sơ?". | **STATE**: Backend chỉ xóa khi `trang_thai='CHO_TIEP_NHAN'` (srs-fr-05:421, 451). UPDATE `is_deleted=1` (BR-DATA-01). **UI**: Toast success "Đã xóa hồ sơ {ma_vu_viec}". Hàng biến mất khỏi bảng (DS reload). **PERSIST**: AUDIT_LOG action='DELETE_HS_HT_KHAC' với user=`cb_nv_tw_01` (BR-DATA-05, srs-fr-05:422). Verify gián tiếp qua `list_network_requests` DELETE `/vu-viec/{id}` 200. | Happy | P0 |
| TC-VV-HK-106 | FR-V.I-05 Outputs CMS DS#8 / ngay_tiep_nhan datetime format | Verify cột ngay_tiep_nhan hiển thị datetime (dd/mm/yyyy HH:mm) — KHÁC SCR-V.I-01 cột 18 (chỉ date) | `cb_nv_tw_01`. VV-HK-001 với `ngay_tiep_nhan=2026-04-15 14:30:00` (timestamp từ API Inbound). | — | 1. Vào DS HS HT khác. 2. Quan sát cột "Ngày tiếp nhận" cho VV-HK-001. | **STATE**: Backend trả `ngay_tiep_nhan` kiểu datetime (srs-fr-05:443 quote "datetime"). **UI**: Cột hiển thị "15/04/2026 14:30" (dd/mm/yyyy HH:mm) — phân biệt với SCR-V.I-01:1679 cột 18 chỉ "dd/mm/yyyy" (date format) cho luồng CB NV thường. UC55 datetime quan trọng để CB NV biết HT khác gửi lúc nào (compliance trace). **CRITICAL**: nếu UI bỏ time component → mất trace giờ phút khi nhiều HS vào cùng ngày. **PERSIST**: — | Happy | P1 |
| TC-VV-HK-107 | FR-V.I-05 Outputs CMS DS#6 / noi_dung_yeu_cau rút gọn + tooltip | Cột nội dung rút gọn ≤80 ký tự + tooltip hover hiện full text | `cb_nv_tw_01`. VV-HK-LONG (noi_dung_yeu_cau >200 ký tự). | — | 1. Quan sát cột nội dung trong DS. 2. Hover cell nội dung VV-HK-LONG. | **STATE**: Backend trả `noi_dung_yeu_cau` rút gọn theo SRS:441 (chỉ trả phần đầu hoặc full). **UI**: Cell hiển thị ≤80 ký tự đầu + "…" suffix. Hover → tooltip hiện full text. Nếu BE trả raw long string + FE cắt clientside → cũng valid. Verify CSS `text-overflow: ellipsis` hoặc JS truncate. **SPEC-CLARIFY-VV-HK-02**: 80 ký tự là quy ước UI-01 set, SRS:441 chỉ ghi "rút gọn" không quote số ký tự cụ thể. | Happy | P2 |

---

## C. NEGATIVE — VALIDATION ERRORS

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước | Kết quả mong đợi | Type | Priority |
|----|---------|--------------|----------------|-----------|----------|------------------|------|----------|
| TC-VV-HK-201 | FR-V.I-05 / E7 ERR-VV-01 | Xóa HS đã DA_TIEP_NHAN → reject | `cb_nv_tw_01`. VV-HK-002 ở `trang_thai=DA_TIEP_NHAN` (đã được CB NV tiếp nhận). | — | 1. Mở DS. 2. Quan sát hàng VV-HK-002. 3. (Nếu nút [Xóa] hidden — happy path UI). 4. Thử gọi DELETE qua devtools (negative API test). | **STATE**: Backend reject với điều kiện `trang_thai != CHO_TIEP_NHAN` (srs-fr-05:421, 463). **UI**: Hàng VV-HK-002 KHÔNG hiển thị nút [Xóa] (UI guard). Nếu user bypass UI → toast error nguyên văn "Không thể xóa hồ sơ đã được tiếp nhận" (ERR-VV-01 srs-fr-05:463). **PERSIST**: VV-HK-002 vẫn `is_deleted=0`, trạng thái giữ nguyên DA_TIEP_NHAN. | Negative | P0 |
| TC-VV-HK-202 | FR-V.I-05 / E6 ERR-AUTH-01 | User không có quyền "Quản lý hồ sơ VV" truy cập DS | User `tvv_01` (vai trò TVV — không có quyền CMS HS HT_KHAC). | — | 1. Login `tvv_01`. 2. Truy cập URL `/vu-viec/ho-so-ht-khac` trực tiếp. | **STATE**: Backend reject 403 (srs-fr-05:417 BR-AUTH-01, 462). **UI**: Trang chuyển về 403 page hoặc toast error nguyên văn "Bạn không có quyền thực hiện chức năng này" (ERR-AUTH-01). Menu "HS từ HT khác" không hiển thị trong sidebar. **PERSIST**: AUDIT_LOG ghi attempt từ chối (nếu policy log). | Negative | P0 |
| TC-VV-HK-203 | FR-V.I-05 / EC-V.I-05-13 (CMS scope phân quyền DELETE) | CB NV BN cố xóa VV của ĐP-AG → reject | `cb_nv_bn_01` (CB NV BN). VV-HK-DP-01 thuộc đơn vị DP-AG, `trang_thai=CHO_TIEP_NHAN`. | — | 1. Login `cb_nv_bn_01`. 2. Vào DS — VV-HK-DP-01 KHÔNG hiển thị (scope BN không thấy DP). 3. Thử DELETE trực tiếp `/vu-viec/{id-DP}` qua devtools. | **STATE**: Backend kiểm tra phân quyền dữ liệu cho DELETE (KHÔNG chỉ LIST — srs-fr-05:481 EC-V.I-05-13). Reject 403. **UI**: Toast error 403 hoặc "Bạn không có quyền thực hiện chức năng này" (ERR-AUTH-01). **PERSIST**: VV-HK-DP-01 không bị xóa. **CRITICAL**: Nếu BE chỉ check scope ở LIST mà không check ở DELETE → cross-tenant data deletion vulnerability. | Negative | P0 |

---

## D. EDGE CASES

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước | Kết quả mong đợi | Type | Priority |
|----|---------|--------------|----------------|-----------|----------|------------------|------|----------|
| TC-VV-HK-301 | FR-V.I-05 / search XSS sanitize | XSS payload trong ô keyword | `cb_nv_tw_01`. | keyword=`<script>alert('XSS-HK')</script>` | 1. Gõ XSS payload. 2. [Tìm]. | **STATE**: Backend sanitize input — KHÔNG execute script. **UI**: Bảng load result (likely empty), `list_console_messages` clean (no alert fired). Input field hiển thị raw text payload (escaped). URL share KHÔNG re-execute. **PERSIST**: KHÔNG persist payload vào DB / search log. **CRITICAL**: Nếu thiếu sanitize → reflected XSS qua URL share. | Edge | P0 |
| TC-VV-HK-302 | FR-V.I-05 / EC-V.I-05-04 idempotency UI verify | Tạo lại từ HT khác cùng `ma_ho_so_nguon` (đã tồn tại) — UI hiển thị bản ghi cũ, không tạo trùng | `cb_nv_tw_01`. VV-HK-001 đã tồn tại với `ma_ho_so_nguon=HSN-2026-001`. (API Inbound được Test team trigger từ HT giả lập với cùng key — A7 chỉ verify CMS phần). | — | 1. (Setup ngoài: trigger API Inbound retry với cùng `he_thong_nguon`+`ma_ho_so_nguon` + cùng payload). 2. Reload DS CMS. | **STATE**: Backend idempotent (srs-fr-05:472) — KHÔNG tạo bản ghi trùng. **UI**: DS chỉ có 1 dòng VV-HK-001 (count không tăng). **PERSIST**: VU_VIEC count không đổi. **A7 note**: Phần API Inbound verify thuộc test riêng — A7 LOẠI khỏi auto suite, ghi gap-report. | Edge | P2 |
| TC-VV-HK-303 | FR-V.I-05 / Processing CMS B6 audit log delete | Audit log ghi nhận DELETE đầy đủ (user / time / VV) | `qtht_01`. VV-HK-AUD-01 ở CHO_TIEP_NHAN. `cb_nv_tw_01` xóa. | — | 1. Tab1 `cb_nv_tw_01` xóa VV-HK-AUD-01. 2. Tab2 `qtht_01` vào màn hình Audit log lọc theo VV-HK-AUD-01. | **STATE**: AUDIT_LOG ghi entry mới (BR-DATA-05 srs-fr-05:422). **UI** (Tab2): Audit log có entry với hanh_dong='DELETE_HS_HT_KHAC' (hoặc tương đương) / nguoi_thuc_hien=`cb_nv_tw_01` / thoi_gian=NOW / vu_viec_id=VV-HK-AUD-01. **PERSIST**: Verify gián tiếp qua `list_network_requests` Tab2 GET `/audit-log` thấy entry. | Edge | P1 |
| TC-VV-HK-304 | FR-V.I-05 / pagination + search combine | Search kết hợp pagination — page 2 giữ filter context | `cb_nv_tw_01`. ≥45 VV với keyword "Cty" match. | keyword="Cty", page=2 | 1. Gõ "Cty". 2. [Tìm]. 3. Click trang 2. | **STATE**: Backend `WHERE keyword match LIMIT 20 OFFSET 20` (srs-fr-05:396 BR-DATA-07). **UI**: Trang 2 vẫn 20 dòng match keyword "Cty". Filter UI giữ nguyên giá trị. URL có thể có `?keyword=Cty&page=2` (verify — mark SPEC-CLARIFY-VV-HK-01 nếu không có). **PERSIST**: — | Edge | P1 |
| TC-VV-HK-305 | FR-V.I-05 / concurrent delete | 2 CB NV cùng xóa 1 VV CHO_TIEP_NHAN — chỉ 1 thành công | Tab1 `cb_nv_tw_01` + Tab2 `cb_nv_tw_02`. VV-HK-CONC-01 ở CHO_TIEP_NHAN. | — | 1. Tab1 click [Xóa] VV-HK-CONC-01 → confirm. 2. Tab2 (chưa reload) cũng click [Xóa] → confirm. | **STATE**: Tab1 SUCCESS — VV-HK-CONC-01 `is_deleted=1`. Tab2 FAIL với optimistic lock conflict hoặc not-found (BR-EC-01). **UI**: Tab1 toast success. Tab2 toast error "Vụ việc đã được cập nhật / không tồn tại. Vui lòng tải lại." **PERSIST**: AUDIT_LOG 1 entry DELETE bởi `cb_nv_tw_01`. | Edge | P1 |

---

## Tổng kết file

**Tổng TC: 16** (1 UI + 7 Happy + 3 Negative + 5 Edge) — sau Codex review 2026-05-09

| Section | TC IDs | Count |
|---------|--------|------:|
| A. UI verification | UI-01 | 1 |
| B. Happy | 101, 102, 103, 104, 105, **106** ⭐, **107** ⭐ | 7 |
| C. Negative | 201, 202, 203 | 3 |
| D. Edge | 301, 302, 303, 304, 305 | 5 |

⭐ = thêm sau Codex review 2026-05-09.

> **Changelog 2026-05-06:**
> - **A7 LOẠI**: API Inbound TC (E1 ERR-INTG-01, E2 ERR-INTG-02, E3 ERR-INTG-03, E4 ERR-FILE-01, E5 ERR-FILE-02, EC-V.I-05-01..12 inbound) — vi phạm A7 filter (hệ thống bên ngoài, không UI CMS).
> - **Giữ**: TC liên quan UI CMS (DS/Search/Delete) + verify side-effect qua network log.
> - **EC-V.I-05-04 (idempotency)** giữ ở P2 với note A7 — chỉ verify CMS không hiện trùng, không test API Inbound.
>
> **Codex review 2026-05-09:**
> - CLEANUP recount confusion (line 52-54 redundant block)
> - ADD TC-VV-HK-106 (ngay_tiep_nhan datetime format dd/mm/yyyy HH:mm — gap srs-fr-05:443 phân biệt UC55 datetime vs SCR-V.I-01:1679 date)
> - ADD TC-VV-HK-107 (noi_dung_yeu_cau rút gọn + tooltip — gap srs-fr-05:441)
> - ADD SPEC-CLARIFY-VV-HK-02 (rút gọn 80 ký tự — số chính xác chưa quote)

**Priority**: P0=6 / P1=8 / P2=2

**Coverage:**
- BR: BR-AUTH-01/03/04/08, BR-DATA-01/05/07, BR-EC-01, BR-EC-13 (XSS sanitize)
- Error codes: ERR-VV-01 (xóa HS đã tiếp nhận), ERR-AUTH-01 (3 nhánh: no permission, cross-tenant, role mismatch). API Inbound errors (ERR-INTG-01..05, ERR-FILE-01..03) **A7 LOẠI**.
- AC SRS CMS: 4/4 (srs-fr-05:486-488 + 2 AC API Inbound LOẠI A7)
- Outputs CMS DS: 9/9 column tested (TC-101 cấu trúc + TC-106 datetime + TC-107 cut/tooltip)
- SPEC-CLARIFY:
  - **VV-HK-01**: Deep-link query params trên URL DS HS HT khác (filter context preserve qua share link)
  - **VV-HK-02 (mới)**: noi_dung_yeu_cau "rút gọn" — SRS:441 không quote số ký tự cụ thể (UI-01 set 80 nhưng cần BA confirm)

---

> **A7 gap-report (cho Phase B integration)**:
> - API Inbound (UC55 nhánh hệ thống nguồn → REST POST `/api/v1/vu-viec/inbound`) cần test riêng với HT giả lập + API key whitelist (EC-V.I-05-04/05/10/11). KHÔNG nằm trong auto suite UI A3.
