# Test Cases — UC115: Phân quyền Chức năng (FR-VIII-17)

> **SRS Ref**: FR-VIII-17 (srs-fr-10:796-843), SCR-VIII-04 (srs-fr-10:1564-1588), Entity QUYEN_HAN loại=CHUC_NANG (srs-fr-10:1993-2007), VAI_TRO_QUYEN_HAN junction (implicit)
> **Ngày tạo**: 2026-05-08 (BMAD A3 base + A4 inline merge + A6 fill)
> **Tài khoản chính**: `qtht_01` (chỉ QTHT — BR-AUTH-01)

> **Pre-condition chung mọi TC trong file:** `qtht_01` đăng nhập (URL `/quan-tri/phan-quyen-chuc-nang` hoặc menu "Quản trị → Phân quyền → Chức năng"). OTP `666666`. VAI_TRO ≥ 11 record. QUYEN_HAN seed có ≥ 100 record loại CHUC_NANG (srs-fr-10:2007). Cây menu: 16 module (Dashboard / Hỏi đáp / Đào tạo / CG-TVV / Vụ việc / Chi trả / DN / Đánh giá / Biểu mẫu / Quản trị / Báo cáo / Tư vấn CS / Tư vấn nhanh / Hợp đồng TV / CT HTPLDN / API kết nối) — verify đếm thực tế ở Phase B.

---

## A. HAPPY PATH — UI MATRIX + LOAD QUYỀN

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước | Kết quả mong đợi | Type | Priority |
|----|---------|---------------|----------------|-----------|----------|------------------|------|----------|
| TC-PQCN-101 | FR-VIII-17 AC1 | QTHT mở SCR-VIII-04 — chọn vai trò → cây menu + matrix 6 cột | `qtht_01`. Vai trò QTHT đã có quyền sẵn. | vai_tro=QTHT | 1. Login `qtht_01`. 2. Sidebar "Quản trị → Phân quyền → Chức năng". 3. Click dropdown vai trò. 4. Chọn QTHT. | **STATE**: BE GET `/api/v1/phan-quyen-chuc-nang?vai_tro_id=...`. **UI**: Dropdown vai trò (#1, srs-fr-10:1574). Cây menu cột trái (#2). 6 cột checkbox: Xem / Thêm / Sửa / Xóa / Phê duyệt / Xuất (#3-8, srs-fr-10:1576-1581). Nút [Lưu phân quyền] + [Reset về mặc định] (#9-10). Checkbox đánh dấu quyền hiện tại của QTHT. **PERSIST**: — | Happy | P0 |
| TC-PQCN-102 | FR-VIII-17 AC2 | Bật quyền Xem cho 1 module → Lưu → user thuộc vai trò thấy menu | `qtht_01`. Vai trò NEW_ROLE chưa có quyền. | vai_tro=NEW_ROLE, quyen=DOANH_NGHIEP_XEM | 1. Chọn NEW_ROLE. 2. Tick checkbox "Xem" hàng "Doanh nghiệp". 3. [Lưu phân quyền]. | **STATE**: BE PUT `/api/v1/phan-quyen-chuc-nang` body `{vai_tro_id, quyen_ids:[DN_XEM_id]}`. Transaction xóa cũ + tạo mới (srs-fr-10:826). AUDIT_LOG ghi quyền cũ → mới (srs-fr-10:827). **UI**: Toast "Lưu phân quyền thành công". **PERSIST**: User thuộc NEW_ROLE login → sidebar có entry "Doanh nghiệp" (read-only, KHÔNG có nút Thêm/Sửa). | Happy | P0 |
| TC-PQCN-103 | SCR-VIII-04 #2 + Quy tắc tương tác (cha → con cascade) | Tick cha "Quản trị" → auto tick tất cả sub-menu (DM dùng chung, TKPQ, Cấu hình HT, Nhật ký HT) | `qtht_01`. Vai trò TEST_CASCADE. | vai_tro=TEST_CASCADE, click cha "Quản trị" cột "Xem" | 1. Chọn TEST_CASCADE. 2. Click cha "Quản trị" cột Xem. | **STATE**: FE cascade. **UI**: Tất cả sub-menu của Quản trị tick cột Xem. (srs-fr-10:1586). **PERSIST**: — | Happy | P0 |
| TC-PQCN-104 | Quy tắc tương tác cột | Click header cột "Xem" → tick tất cả module | `qtht_01`. Vai trò TEST_HEADER. | — | 1. Chọn TEST_HEADER. 2. Click header cột "Xem". | **STATE**: FE tick all. **UI**: Tất cả 16 module tick cột Xem (srs-fr-10:1587). | Happy | P0 |
| TC-PQCN-105 | FR-VIII-17 step 5 (audit ghi quyền cũ → mới) | AUDIT_LOG ghi đủ JSON diff old → new | `qtht_01`. Vai trò X có quyền {A_XEM, A_THEM}. | new={A_XEM, A_SUA} | 1. Chọn X. 2. Uncheck A_THEM, tick A_SUA. 3. [Lưu]. 4. SCR-VIII-10. | **STATE**: AUDIT_LOG action='UPDATE' với chi_tiet `{vai_tro_id, old:[A_XEM, A_THEM], new:[A_XEM, A_SUA]}` (srs-fr-10:837). **UI**: Expand JSON OK. | Happy | P1 |
| TC-PQCN-106 | SCR-VIII-04 #10 + SPEC-CLARIFY-TKPQ-06 | Click "Reset về mặc định" — quyền template theo loại vai trò | `qtht_01`. Vai trò X đang có quyền custom. | — | 1. Chọn X. 2. Click [Reset về mặc định]. 3. Modal xác nhận. 4. Confirm. | **STATE**: BE behavior: (a) Reset về template quyền của loại vai trò (vd CB_NV_TW có template sẵn); (b) Reset về rỗng. SPEC-CLARIFY-TKPQ-06. **UI**: Matrix re-load với set quyền mới. **PERSIST**: AUDIT_LOG action='RESET'. | Edge | P1 |
| TC-PQCN-107 | FR-VIII-17 input #2 (multi quyền 1 module) | Tick 6 cột (Xem+Thêm+Sửa+Xóa+Phê duyệt+Xuất) cho 1 module | `qtht_01`. | vai_tro=ADMIN_DN, module=DOANH_NGHIEP, all 6 quyền | 1. Chọn ADMIN_DN. 2. Tick 6 checkbox hàng DN. 3. [Lưu]. | **STATE**: BE INSERT 6 row VAI_TRO_QUYEN_HAN. **UI**: 6 checkbox đều tick. **PERSIST**: User thuộc ADMIN_DN có full quyền DN module. | Happy | P0 |
| TC-PQCN-108 | A6 fill (count menu) | Verify cây menu có đủ 16 module (theo plan §1.3 16 FR) | `qtht_01`. Bất kỳ vai trò. | — | 1. Mở SCR-VIII-04. 2. Đếm số node cây cha. | **STATE**: SRS srs-fr-10:1575 nguyên văn "Phân cấp module: Dashboard / Hỏi đáp / Đào tạo / ..." (không liệt kê hết). **UI**: Đếm thực tế ≥ 12-16 module. SPEC-CLARIFY-TKPQ-10 confirm exact count. | Happy | P1 |

---

## B. NEGATIVE — VALIDATION + ERROR HANDLING

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước | Kết quả mong đợi | Type | Priority |
|----|---------|---------------|----------------|-----------|----------|------------------|------|----------|
| TC-PQCN-120 | ERR-PQ-02 (E1) | Vai trò bị xóa giữa chừng — reject | `qtht_01`. Vai trò V đã chọn. | — | 1. Chọn V. 2. Tab khác xóa V (UC112). 3. Quay lại tab gốc, tick quyền. 4. [Lưu]. | **STATE**: BE check vai_tro tồn tại → reject 400. **UI**: Toast ERROR "Vai trò không tồn tại" (srs-fr-10:833). | Negative | P1 |
| ~~TC-PQCN-121~~ | ~~ERR-PQ-04~~ | **MOVED to `07-TC-security-IDOR.md` TC-IDOR-PQCN-001 (2026-05-08 Codex R2)** — FK injection test, A7 cấm. | — | — | — | Moved | — |
| TC-PQCN-122 | FR-VIII-17 input #2 bắt buộc (srs-fr-10:817) | Bỏ trống quyen_ids — reject | `qtht_01`. Vai trò X trước đó có quyền. | quyen_ids=[] | 1. Chọn X. 2. Uncheck tất cả. 3. [Lưu]. | **STATE**: SRS srs-fr-10:817 nguyên văn `quyen_ids | identifier[] | Y` — bắt buộc ≥ 1. BE/FE reject. **UI**: Inline ERROR "Vui lòng bật ít nhất 1 quyền cho vai trò" hoặc tương đương. Nút [Lưu phân quyền] disabled khi tất cả checkbox uncheck. **PERSIST**: Quyền cũ giữ nguyên (không bị clear). (Note Codex R2: SPEC-CLARIFY-TKPQ-25 đã withdraw — SRS rõ ràng yêu cầu Y, không phải ambiguity.) | Negative | P1 |
| TC-PQCN-123 | A4 cha tick mà con không tick (inconsistent state) | Manual edit DB inject inconsistent state — verify UI | `qtht_01`. Vai trò X có quyền cha "DM_DUNG_CHUNG_XEM" nhưng KHÔNG có "DM_LINH_VUC_PL_XEM" (con). | — | 1. Chọn X. 2. Quan sát cây. | **STATE**: SRS Quy tắc cha → con cascade (srs-fr-10:1586) — dùng cho user input. Nhưng nếu DB inject inconsistent, UI behavior thế nào? **UI**: (a) Cha tick + con không tick — hiển thị nửa-tick (indeterminate); (b) Cha tick = check tất cả con auto trên load. SPEC-CLARIFY-TKPQ-26. | Edge | P2 |

---

## C. SECURITY & EDGE — IDOR + Cache + Permission Cascade

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước | Kết quả mong đợi | Type | Priority |
|----|---------|---------------|----------------|-----------|----------|------------------|------|----------|
| ~~TC-PQCN-130~~ | ~~BR-AUTH-01 IDOR~~ | **MOVED to `07-TC-security-IDOR.md` TC-IDOR-PQCN-002 (2026-05-08 Codex R2)** — Direct API authz test, A7 cấm. | — | — | — | Moved | — |
| TC-PQCN-131 | A4 cache invalidation | Sau khi đổi quyền chức năng, user thuộc vai trò cần re-login để áp dụng | `qtht_01`. User U đang login, thuộc vai trò X có quyền DN_XEM. | — | 1. User U thấy menu "Doanh nghiệp" trong sidebar. 2. `qtht_01` bỏ quyền DN_XEM của X. 3. User U reload sidebar/page. | **STATE**: BE invalidate session/JWT cho user thuộc X HOẶC lazy refresh. **UI**: Sau reload (hoặc re-login) U KHÔNG thấy "Doanh nghiệp" trong sidebar nữa. **PERSIST**: SPEC-CLARIFY-TKPQ-21 cross-ref. | Edge | P1 |
| TC-PQCN-132 | A4 quyền Phê duyệt — cross-module | User thuộc vai trò có quyền Phê duyệt → có button [Phê duyệt] trên module Vụ việc | `qtht_01`. Vai trò CB_PD có quyền VU_VIEC_PHE_DUYET. User cb_pd_tw_01. | — | 1. Login cb_pd_tw_01. 2. Vào module Vụ việc → 1 vụ việc CHO_PHE_DUYET. 3. Quan sát button. | **STATE**: BE filter actions theo quyền user. **UI**: Button [Phê duyệt] hiện. (Test cross-module cho FR-VIII-17 cột "Phê duyệt".) **PERSIST**: — | Happy | P1 |
| TC-PQCN-133 | A4 quyền Xuất — cross-module | User thuộc vai trò có quyền Xuất → có button [Xuất Excel] trên module DN | `qtht_01`. Vai trò V có quyền DOANH_NGHIEP_XUAT. User u thuộc V. | — | 1. Login u. 2. Module DN. 3. Quan sát button [Xuất]. | **STATE**: BE filter button theo quyền. **UI**: Button [Xuất Excel] hiện. | Happy | P1 |
| TC-PQCN-134 | A4 quyền Xóa — verify hard delete vs soft delete | User có quyền XOA → có button [Xóa] | `qtht_01`. Vai trò V có DN_XOA. User u. | — | 1. Login u. 2. Module DN row bất kỳ. 3. Quan sát button [Xóa]. | **STATE**: BE filter. **UI**: Button [Xóa] hiện. Click → soft delete (BR-DATA-01). **PERSIST**: — | Happy | P1 |
| TC-PQCN-135 | A4 cây menu collapse/expand | Cây menu cha có icon expand/collapse — click toggle | `qtht_01`. | — | 1. Mở SCR-VIII-04. 2. Click icon expand "Quản trị" (cha). | **STATE**: FE only. **UI**: Sub-menu hiện/ẩn. Checkbox cha vẫn nguyên trạng. | Happy | P2 |
| TC-PQCN-136 | A4 audit log permission cascade | Khi cha tick auto check con → AUDIT_LOG ghi đủ tất cả quyền con | `qtht_01`. Vai trò X chưa có quyền. | click cha "Quản trị" cột Xem | 1. Tick cha. 2. [Lưu]. 3. SCR-VIII-10. | **STATE**: AUDIT_LOG action='UPDATE' với chi_tiet ghi tất cả quyen_ids con (vd 4 sub-menu × 1 cột = 4 quyền). **UI**: Expand JSON đầy đủ. | Happy | P1 |
| TC-PQCN-137 | A4 IDOR cross-vai_tro | QTHT đổi quyền vai trò khác cấp mình (vd QTHT TW đổi quyền vai trò ADMIN_BN) | `qtht_01` (cap ALL). | vai_tro=ADMIN_BN | 1. Chọn ADMIN_BN. 2. Đổi quyền. | **STATE**: BE accept (QTHT cap=ALL bypass mọi ràng buộc). **UI**: Lưu OK. **PERSIST**: AUDIT_LOG. | Happy | P1 |
| TC-PQCN-138 | A6 fill — ma trận 16 module × 6 cột (96 checkbox) | Performance: tick 96 checkbox + lưu | `qtht_01`. Vai trò ALL_PERMS. | tất cả 96 quyền | 1. Chọn ALL_PERMS. 2. Click cột header lần lượt 6 cột "Xem"/"Thêm"/"Sửa"/"Xóa"/"Phê duyệt"/"Xuất" → tick toàn bộ. 3. [Lưu]. 4. Đo response time. | **STATE**: BE INSERT batch ~96 row. **UI**: Lưu ≤ 3s. **PERSIST**: AUDIT_LOG có 1 entry. | Edge | P2 |

---

## Tổng số TC: 19 (8 Happy + 3 Negative + 8 Security/Edge) — A3 base 14 + A4 merged 7 + A6 fill 1 - Codex R2 -2 IDOR moved (TC-121, 130)

**Priority**: P0=6 / P1=10 / P2=3

**Coverage (sau Codex R2):**
- BR: BR-AUTH-01 (precondition; IDOR moved 07), BR-DATA-05 (TC105, TC136 audit), BR-DATA-01 (TC134 cross quyền XOA → soft delete)
- AC SRS (2 AC): AC1 ✅ (TC101), AC2 ✅ (TC102, TC103, TC107)
- Error codes (2): ERR-PQ-02 ✅ (TC120), ERR-PQ-04 ✅ (moved 07 TC-IDOR-PQCN-001)
- Codex R2 fix 2026-05-08: TC122 force expected reject empty (SPEC-CLARIFY-TKPQ-25 withdrawn — SRS rõ Y bắt buộc)
- A4 merged 2026-05-08: TC123 (inconsistent state), TC131-134 (cache + permission cascade cross-module), TC135-138 (UI affordance + perf)
- A6 fill 2026-05-08: TC108 (count menu cây)
- SPEC-CLARIFY: TKPQ-06 (Reset về mặc định template gì?), TKPQ-10 (cây menu count), TKPQ-21 (cache refresh), TKPQ-26 (inconsistent cha-con state UI behavior)

---

## D. Note về A7 — UI vs API (Codex R2 update)

> **2026-05-08 Codex R2:** TC-PQCN-121 + TC-PQCN-130 (IDOR/FK injection) đã MOVE sang `07-TC-security-IDOR.md`. A7 rule cấm test API thuần. File này còn lại 100% functional UC.
> TC-PQCN-131 + TC-PQCN-132/133/134 cross-module verify — login user thuộc vai trò + check sidebar/button hiển thị thực tế. UI bridge OK.
> TC-PQCN-105 + TC-PQCN-136 verify audit log qua SCR-VIII-10 — UI bridge.
