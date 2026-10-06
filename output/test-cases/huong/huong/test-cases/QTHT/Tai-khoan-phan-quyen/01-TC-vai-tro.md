# Test Cases — UC112: Quản lý Vai trò (FR-VIII-14)

> **SRS Ref**: FR-VIII-14 (srs-fr-10:595-653), SCR-VIII-02 (srs-fr-10:1499-1520), Entity VAI_TRO (srs-fr-10:1985-1989), TAI_KHOAN_VAI_TRO junction (srs-fr-10:2030-2036)
> **Ngày tạo**: 2026-05-08 (BMAD A3 base + A4 inline merge + A6 fill)
> **Tài khoản chính**: `qtht_01` (chỉ QTHT — BR-AUTH-01)

> **Pre-condition chung mọi TC trong file:** `qtht_01` đăng nhập (URL `/quan-tri/vai-tro` hoặc menu "Quản trị → Phân quyền → Vai trò"). OTP `666666`. VAI_TRO seed có ≥ 11 record (QTHT, CB_NV_TW/BN/DP, CB_PD_TW/BN/DP, DN, NHT, TVV, CG — srs-fr-10:1991). TAI_KHOAN seed có ≥ 5 record gắn vai trò khác nhau để test ERR-VT-02.

---

## A. HAPPY PATH — DANH SÁCH + CRUD CƠ BẢN

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước | Kết quả mong đợi | Type | Priority |
|----|---------|---------------|----------------|-----------|----------|------------------|------|----------|
| TC-VT-101 | FR-VIII-14 AC1 | QTHT mở SCR-VIII-02 — danh sách vai trò + phân trang | `qtht_01`. ≥ 11 vai trò seed. | — | 1. Login `qtht_01`. 2. Sidebar "Quản trị → Phân quyền → Vai trò". 3. Quan sát bảng + phân trang. | **STATE**: BE GET `/api/v1/vai-tro?page=1&size=20`. **UI**: Bảng có cột Mã vai trò / Tên vai trò / Mô tả / Số tài khoản / Số quyền / Trạng thái (toggle) / Hành động (Sửa/Xóa) (SCR-VIII-02 #3-9, srs-fr-10:1511-1517). Pagination footer hiển thị "1-11 trong số 11" hoặc "1 / 1". Breadcrumb "Trang chủ > Quản trị > Phân quyền > Vai trò". Nút [+ Thêm vai trò] toolbar. **PERSIST**: Reload giữ trang. | Happy | P0 |
| TC-VT-102 | FR-VIII-14 AC2 | Thêm vai trò mới — mã unique + tên + mô tả + trạng thái = Hoạt động | `qtht_01`. | ma="VT_TEST_01", ten="Vai trò test 01", mo_ta="Mô tả vai trò test", trang_thai=1 | 1. Click [+ Thêm vai trò]. 2. Modal mở với 4 field (Mã, Tên, Mô tả, Trạng thái). 3. Nhập đủ. 4. Click [Lưu]. | **STATE**: BE POST `/api/v1/vai-tro` body 4 field; status 201 Created với id mới. AUDIT_LOG ghi action='CREATE' entity='VAI_TRO' (BR-DATA-05). **UI**: Modal đóng. Toast "Thêm vai trò thành công" (hoặc tương đương). Bảng có dòng mới với mã VT_TEST_01. **PERSIST**: Reload, dòng mới còn. | Happy | P0 |
| TC-VT-103 | FR-VIII-14 AC2 | Sửa tên + mô tả vai trò có sẵn (không đổi mã) | `qtht_01`. VT_TEST_01 từ TC-102. | ten="Vai trò test 01 SỬA", mo_ta="updated" | 1. Click [Sửa] dòng VT_TEST_01. 2. Modal mở pre-fill. 3. Sửa ten + mo_ta (không đổi mã). 4. Click [Lưu]. | **STATE**: BE PUT/PATCH `/api/v1/vai-tro/:id` 200 OK. AUDIT_LOG ghi action='UPDATE' với chi_tiet JSON diff old→new. **UI**: Modal đóng. Toast "Cập nhật thành công". Bảng dòng VT_TEST_01 có ten/mo_ta mới. **PERSIST**: Reload giữ. | Happy | P0 |
| TC-VT-104 | FR-VIII-14 step 3 (BR-DATA-01) | Xóa vai trò chưa gán cho TK nào — soft delete | `qtht_01`. Tạo VT_TEST_DEL có `so_tai_khoan=0`. | — | 1. Click [Xóa] dòng VT_TEST_DEL. 2. Modal/popconfirm "Xác nhận xóa?". 3. Click [Đồng ý]. | **STATE**: BE DELETE `/api/v1/vai-tro/:id` 200 OK; soft delete (BR-DATA-01 srs-fr-10:2203). AUDIT_LOG action='DELETE'. **UI**: Modal đóng. Toast "Xóa thành công". Dòng biến mất khỏi bảng. **PERSIST**: Reload SCR-VIII-02, dòng KHÔNG xuất hiện. Verify qua SCR-VIII-10 Nhật ký HT (W1.1 module): có entry action='DELETE' entity='VAI_TRO' với mã VT_TEST_DEL — chứng minh soft delete (entry tồn tại = record được đánh dấu, không hard-delete). | Happy | P0 |
| TC-VT-105 | FR-VIII-14 step 3 + SCR-VIII-02 #8 | Toggle trạng thái Hoạt động → Vô hiệu hóa (KHÔNG xóa) | `qtht_01`. VT_TEST_01 đang Hoạt động. | toggle off | 1. Quan sát dòng VT_TEST_01 cột Trạng thái = ✅ Hoạt động. 2. Click toggle. 3. Confirm popup. | **STATE**: BE PATCH với `trang_thai=VO_HIEU_HOA`. AUDIT_LOG. **UI**: Toggle về vị trí off (xám/đỏ). Tooltip/badge "Vô hiệu hóa". Cột Trạng thái update inline. **PERSIST**: Reload, toggle vẫn off. | Happy | P0 |
| TC-VT-106 | FR-VIII-14 step 3 + SCR-VIII-02 #8 | Toggle ngược Vô hiệu hóa → Hoạt động | `qtht_01`. VT_TEST_01 đang Vô hiệu hóa. | toggle on | 1. Click toggle. 2. Confirm. | **STATE**: BE PATCH `trang_thai=KICH_HOAT`. AUDIT_LOG. **UI**: Toggle on (xanh). Cột Trạng thái = "Hoạt động". | Happy | P1 |
| TC-VT-107 | SCR-VIII-02 #6 (cột Số tài khoản click filter) | Click cột "Số tài khoản" → navigate sang UC113 với filter vai trò | `qtht_01`. Vai trò QTHT có ≥ 1 TK. | — | 1. Click số ở cột "Số tài khoản" của QTHT. | **STATE**: FE navigate `/quan-tri/tai-khoan?vai_tro_id={QTHT_id}`. **UI**: Trang UC113 mở, filter "Vai trò" đã preset = QTHT, bảng hiển thị TK của vai trò QTHT. **PERSIST**: URL chứa query param. | Happy | P1 |
| TC-VT-108 | SCR-VIII-02 #7 (cột Số quyền click → MH-10.4) | Click cột "Số quyền" → navigate sang SCR-VIII-04 (UC115) với role preset | `qtht_01`. Vai trò QTHT có quyền gán sẵn. | — | 1. Click số ở cột "Số quyền" của QTHT. | **STATE**: FE navigate `/quan-tri/phan-quyen-chuc-nang?vai_tro_id={QTHT_id}`. **UI**: Trang UC115 mở, dropdown vai trò đã preset QTHT, matrix checkbox load. **PERSIST**: — | Happy | P1 |
| TC-VT-109 | FR-VIII-14 + BR-DATA-07 | Pagination 20/page (default) | `qtht_01`. Seed 25 vai trò để test pagination. | — | 1. Mở SCR-VIII-02. 2. Quan sát footer. 3. Click trang 2. | **STATE**: BE `LIMIT 20 OFFSET 0` rồi `OFFSET 20`. **UI**: Trang 1 = 20 dòng, trang 2 = 5 dòng. Footer "1-20 / 25". **PERSIST**: URL có `?page=N`. | Happy | P1 |
| ~~TC-VT-110~~ | ~~SPEC-CLARIFY-TKPQ-12~~ | **REMOVED 2026-05-08 Codex R2** — Search box UC112 là false flag. SCR-VIII-02 (srs-fr-10:1505-1518) liệt kê tường minh 10 component KHÔNG có search box. Đây là out-of-scope, không phải clarify. Nếu UI thực tế có search box — log thành **bug "feature undocumented"** ở Phase B, không phải TC functional. | — | — | — | Removed | — |

---

## B. NEGATIVE — VALIDATION + UNIQUE CONSTRAINT + DELETE BLOCK

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước | Kết quả mong đợi | Type | Priority |
|----|---------|---------------|----------------|-----------|----------|------------------|------|----------|
| TC-VT-120 | ERR-VT-01 (E1) | Mã vai trò trùng — reject | `qtht_01`. VAI_TRO đã có "QTHT". | ma="QTHT" | 1. Click [+ Thêm vai trò]. 2. Nhập ma="QTHT", ten="Test trùng". 3. [Lưu]. | **STATE**: BE reject 400/409. AUDIT_LOG KHÔNG ghi (chưa create thành công). **UI**: Toast/inline ERROR nguyên văn "Mã vai trò 'QTHT' đã tồn tại" (srs-fr-10:642). Modal vẫn mở để user sửa. Field Mã có border đỏ. **PERSIST**: KHÔNG có dòng mới. | Negative | P0 |
| TC-VT-121 | FR-VIII-14 step 2 | Tên vai trò trống — reject (FE validation) | `qtht_01`. | ma="VT_TEST_02", ten="" | 1. Click [+ Thêm]. 2. Bỏ trống Tên. 3. [Lưu]. | **STATE**: FE validate trước submit (HTML5 required hoặc Antd form). BE không nhận request. **UI**: Field Tên có inline error "Vui lòng nhập tên vai trò" (hoặc tương đương). [Lưu] disabled hoặc click không submit. | Negative | P0 |
| TC-VT-122 | FR-VIII-14 step 2 | Mã vai trò trống — reject | `qtht_01`. | ma="", ten="Test" | 1. Click [+ Thêm]. 2. Bỏ trống Mã. 3. [Lưu]. | **STATE**: FE validate. **UI**: Field Mã inline error "Vui lòng nhập mã vai trò". | Negative | P0 |
| TC-VT-123 | ERR-VT-02 (E2) | Xóa vai trò đang gán cho TK — reject với cảnh báo | `qtht_01`. Vai trò QTHT đang gán cho `qtht_01` (≥ 1 TK). | — | 1. Click [Xóa] dòng QTHT. 2. Click [Đồng ý]. | **STATE**: BE check TAI_KHOAN_VAI_TRO COUNT(*) > 0 → reject 400. **UI**: Toast/popup ERROR nguyên văn "Không thể xóa. Vai trò đang gán cho 1 tài khoản" (srs-fr-10:643, N thay theo thực tế). Bảng KHÔNG đổi. **PERSIST**: Vai trò QTHT vẫn còn. | Negative | P0 |
| TC-VT-124 | A4 boundary mã ≥ 50 ký tự (lesson sibling W1.1) | Mã vai trò quá dài (boundary) | `qtht_01`. | ma="A".repeat(60), ten="Test long" | 1. Click [+ Thêm]. 2. Paste 60 chars. 3. [Lưu]. | **STATE**: SRS không nói tường minh max length cho `ma_vai_tro` (chỉ Unique). BE/FE behavior: (a) accept (TEXT field unlimited DB); (b) reject với inline "Mã quá dài". **UI**: Verify behavior thực tế. Nếu accept — verify lưu đầy đủ; nếu reject — verify inline error. SPEC-CLARIFY-TKPQ-13. | Edge | P2 |
| TC-VT-125 | BR-EC-13 (sanitize) | Mã vai trò chứa SQL injection | `qtht_01`. | ma="QT'; DROP TABLE VAI_TRO; --", ten="Test" | 1. Paste payload vào Mã. 2. [Lưu]. | **STATE**: BE escape/parameterize. VAI_TRO không bị drop. **UI**: (a) Accept literal — vai trò mới có mã y nguyên (không thực thi SQL); HOẶC (b) reject với "Mã chứa ký tự không hợp lệ". **PERSIST**: Reload SCR-VIII-02 — bảng vẫn hiển thị đầy đủ vai trò trước (≥ 11 seed) + dòng mới (nếu accept). KHÔNG có table truncate. | Negative | P0 |
| TC-VT-126 | BR-EC-13 (sanitize) | Tên vai trò chứa XSS payload | `qtht_01`. | ten="<script>alert('XSS')</script>" | 1. Paste XSS vào Tên. 2. [Lưu]. | **STATE**: BE lưu plain string. **UI**: (a) Bảng hiển thị literal (escape) `<script>alert('XSS')</script>`; HOẶC (b) reject. KHÔNG render `<script>`. `list_console_messages` KHÔNG có alert. **PERSIST**: — | Negative | P0 |
| TC-VT-127 | A4 unique case-insensitive (sibling pattern) | Mã trùng nhưng khác case ("qtht" vs "QTHT") | `qtht_01`. VAI_TRO có "QTHT". | ma="qtht" | 1. Click [+ Thêm]. 2. Nhập "qtht" (lowercase). 3. [Lưu]. | **STATE**: SRS không nói rõ unique case-sensitive vs insensitive. (a) Reject với ERR-VT-01 (unique case-insensitive như nhiều enum hệ thống); (b) Accept (case-sensitive). Verify behavior + log SPEC-CLARIFY-TKPQ-14 nếu có ambiguity. **UI**: — | Edge | P1 |
| TC-VT-128 | A4 unique cross is_deleted (sibling pattern BR-DATA-01) | Tạo lại vai trò có mã trùng vai trò ĐÃ XÓA mềm | `qtht_01`. Đã xóa VT_TEST_DEL ở TC-104 (`is_deleted=1`). | ma="VT_TEST_DEL" | 1. Click [+ Thêm]. 2. Nhập "VT_TEST_DEL". 3. [Lưu]. | **STATE**: BR-DATA-01 soft delete. Behavior: (a) Reject vì unique constraint trên ma_vai_tro KHÔNG filter is_deleted (DB-level); (b) Accept và "resurrect" record cũ; (c) Accept tạo bản ghi mới. SRS không nói rõ → SPEC-CLARIFY-TKPQ-15. **UI**: Verify thực tế. | Edge | P2 |
| TC-VT-129 | A4 mô tả null vs empty string | Bỏ trống Mô tả (optional field) | `qtht_01`. | ma="VT_NO_DESC", ten="No desc", mo_ta="" | 1. Click [+ Thêm]. 2. Bỏ trống Mô tả. 3. [Lưu]. | **STATE**: BE lưu `mo_ta=NULL` hoặc `''`. **UI**: Bảng cột Mô tả hiển thị "—" hoặc trống. KHÔNG crash. | Negative | P1 |

---

## C. SECURITY & EDGE — IDOR + PERMISSION + AUDIT LOG

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước | Kết quả mong đợi | Type | Priority |
|----|---------|---------------|----------------|-----------|----------|------------------|------|----------|
| TC-VT-130 | BR-DATA-05 audit (A4 merged) | AUDIT_LOG ghi đầy đủ JSON diff khi UPDATE vai trò | `qtht_01`. VT_AUDIT có `ten="Tên cũ"`. | ten="Tên mới" | 1. Sửa ten = "Tên mới". 2. Mở SCR-VIII-10 Nhật ký HT (`/quan-tri/audit-log`). 3. Filter Module=Quản trị, Hành động=Sửa, Entity=VAI_TRO. | **STATE**: AUDIT_LOG có entry với chi_tiet JSON `{"field":"ten_vai_tro","old":"Tên cũ","new":"Tên mới"}`. **UI**: SCR-VIII-10 expand JSON diff hiển thị đúng old→new (cross-module verify). **PERSIST**: — | Happy | P1 |
| TC-VT-131 | BR-DATA-05 audit + soft-delete (A4 merged) | AUDIT_LOG ghi DELETE khi soft-delete | `qtht_01`. VT_AUDIT_DEL không gán TK. | — | 1. Xóa VT_AUDIT_DEL. 2. SCR-VIII-10 filter. | **STATE**: AUDIT_LOG có entry action='DELETE' entity_type='VAI_TRO' với ma_ban_ghi đúng. **UI**: SCR-VIII-10 có dòng tương ứng badge "Xóa" đỏ. **PERSIST**: — | Happy | P1 |
| ~~TC-VT-132~~ | ~~BR-AUTH-01 IDOR~~ | **MOVED to `07-TC-security-IDOR.md` TC-IDOR-VT-001 (2026-05-08 Codex R2)** — Direct API authorization test, A7 rule cấm trộn vào functional UC suite. Security/dev team chạy qua tool API. | — | — | — | Moved | — |
| TC-VT-133 | A4 concurrent edit (sibling pattern) | 2 QTHT cùng sửa 1 vai trò → race condition | `qtht_01` + `qtht_02` cùng login. VT_RACE đang Hoạt động. | qtht_01: ten="A1"; qtht_02: ten="A2" — cùng lúc submit | 1. `qtht_01` mở modal sửa VT_RACE → đang gõ. 2. `qtht_02` (browser khác) mở cùng VT_RACE → sửa ten="A2" → [Lưu]. 3. `qtht_01` submit ten="A1". | **STATE**: SRS không bắt buộc optimistic locking. (a) Last-write-wins (qtht_01 thắng); (b) Có version field → 1 trong 2 reject với "Bản ghi đã được cập nhật". **UI**: Verify behavior. **PERSIST**: AUDIT_LOG có 2 entry CREATE/UPDATE liên tiếp. | Edge | P2 |
| TC-VT-134 | A4 trang_thai default true | Tạo mới với trang_thai=false (Vô hiệu) ngay từ đầu | `qtht_01`. | trang_thai=false | 1. [+ Thêm]. 2. Toggle trạng thái off. 3. [Lưu]. | **STATE**: SRS srs-fr-10:617 mặc định 1 nhưng cho phép user nhập. BE accept trang_thai=0. **UI**: Vai trò mới hiển thị trong bảng với toggle off + badge "Vô hiệu hóa". **PERSIST**: TC-105 toggle on lại OK. | Edge | P1 |
| TC-VT-135 | A4 unicode mã (sibling pattern) | Mã chứa Unicode/dấu — accept hay reject | `qtht_01`. | ma="QTHT_DỆMỚI" | 1. [+ Thêm]. 2. Nhập mã có dấu. 3. [Lưu]. | **STATE**: SRS không restrict charset cho `ma_vai_tro`. BE behavior: (a) Accept (TEXT UTF-8); (b) Reject "Mã chỉ chấp nhận chữ cái không dấu, số, _" (sibling pattern username UC113 ERR-TK-04 srs-fr-10:720). **UI**: Verify thực tế. SPEC-CLARIFY-TKPQ-16. | Edge | P2 |
| TC-VT-136 | A4 mô tả 5000 ký tự (sibling) | Mô tả rất dài (5K ký tự) | `qtht_01`. | mo_ta="lorem ipsum".repeat(500) | 1. [+ Thêm]. 2. Paste mô tả dài. 3. [Lưu]. | **STATE**: SRS không cap. BE: (a) Accept (TEXT field); (b) Reject với "Mô tả tối đa N ký tự". **UI**: Verify lưu đầy đủ. Bảng cột Mô tả hiển thị truncate (nếu có). **PERSIST**: Click Sửa, modal hiện đầy đủ 5K ký tự. | Edge | P2 |
| TC-VT-137 | A6 fill (gap số_quyền/số_TK derived) | Số tài khoản + Số quyền tự động cập nhật khi gán/bỏ gán | `qtht_01`. VT_TEST có `so_tai_khoan=0`. | — | 1. Vào UC113. 2. Tạo TK mới gán vai trò VT_TEST. 3. Quay lại UC112. 4. Quan sát cột Số tài khoản. | **STATE**: BE COUNT TAI_KHOAN_VAI_TRO realtime hoặc materialized view. **UI**: Cột "Số tài khoản" của VT_TEST = 1 (tăng từ 0). **PERSIST**: Reload giữ. | Happy | P1 |
| TC-VT-138 | A6 fill (cap field từ ERD) | SPEC-CLARIFY-TKPQ-01 — verify field `cap` có hiện trên form không | `qtht_01`. | — | 1. [+ Thêm vai trò]. 2. Quan sát modal có field "Cấp" (TW/BN/DP/ALL) không. | **STATE**: ERD VAI_TRO có `cap` (srs-fr-10:1988 default 'ALL'). **UI**: Behavior 1: Form không hiện → BE default 'ALL'; Behavior 2: Form có dropdown → user chọn. **PERSIST**: Verify VAI_TRO.cap = 'ALL' hoặc giá trị user chọn. SPEC-CLARIFY-TKPQ-01 confirm. | Edge | P1 |

---

## Tổng số TC: 28 (10 Happy + 8 Negative + 10 Edge/Audit) — A3 base 22 + A4 merged 7 + A6 fill 2 - Codex R2 removed 1 IDOR (TC-VT-132 → 07) - Codex R2 removed 1 false flag (TC-VT-110 → out-of-scope)

**Priority**: P0=10 / P1=10 / P2=8

**Coverage:**
- BR: BR-AUTH-01 (precondition; IDOR moved to 07), BR-DATA-01 (soft delete TC104, TC128 — verify qua UI list + audit log), BR-DATA-05 (audit TC130-131), BR-DATA-07 (pagination TC109), BR-EC-13 (sanitize TC125-126)
- AC SRS: AC1 ✅ (TC101), AC2 ✅ (TC102-103), AC3 ✅ (TC123 — block xóa khi gán)
- Error codes: ERR-VT-01 ✅ (TC120), ERR-VT-02 ✅ (TC123)
- Edge unique: case-insensitive (TC127), cross is_deleted (TC128), unicode (TC135)
- A4 merged 2026-05-08: TC125-128 + TC130-131, TC133-136 (sanitize, audit, race, edge)
- A6 fill 2026-05-08: TC137 (so_tai_khoan derive), TC138 (cap field clarify)
- SPEC-CLARIFY: TKPQ-01 (cap field), TKPQ-13 (mã max length), TKPQ-14 (unique case), TKPQ-15 (cross is_deleted), TKPQ-16 (mã unicode)

---

## D. Note về A7 — UI vs API (Codex R2 update)

> **2026-05-08 Codex R2:** IDOR TC TC-VT-132 đã được TÁCH ra `07-TC-security-IDOR.md` (TC-IDOR-VT-001). A7 rule cấm test API thuần "đội lốt" UI bridge. File này còn lại 100% functional UC test qua MCP UI flow.
> TC-VT-104 + TC-VT-128 verify soft-delete qua UI: list không hiển thị + AUDIT_LOG SCR-VIII-10 — KHÔNG `SELECT raw is_deleted=1`.
> TC-VT-130 + TC-VT-131 verify AUDIT_LOG qua SCR-VIII-10 (UI module Nhật ký HT W1.1) — UI bridge OK A7.
