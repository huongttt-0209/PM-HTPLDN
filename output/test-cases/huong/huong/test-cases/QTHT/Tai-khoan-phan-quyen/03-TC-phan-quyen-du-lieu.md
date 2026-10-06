# Test Cases — UC114: Phân quyền truy cập Dữ liệu (FR-VIII-16)

> **SRS Ref**: FR-VIII-16 (srs-fr-10:738-793), SCR-VIII-05 (srs-fr-10:1591-1606), BR-AUTH-02/03/04/08 (srs-fr-10:2161, 2167, 2173, 2191), Entity QUYEN_HAN (srs-fr-10:1993-2007), DON_VI cây 2-tầng (srs-fr-10:1956-1975)
> **Ngày tạo**: 2026-05-08 (BMAD A3 base + A4 inline merge + A6 fill)
> **Tài khoản chính**: `qtht_01` (chỉ QTHT — BR-AUTH-01)

> **Pre-condition chung mọi TC trong file:** `qtht_01` đăng nhập (URL `/quan-tri/phan-quyen-du-lieu` hoặc menu "Quản trị → Phân quyền → Dữ liệu"). OTP `666666`. VAI_TRO seed có ≥ 11 record với field `cap` đa dạng (TW, BN, DP, ALL). DON_VI seed cây 2-tầng v3.1: 1 TW (Cục BLDS&KT) + ~20 BN (Bộ Tài chính, Bộ KH-ĐT...) + ~63 ĐP (Sở TP HN, Sở TP HCM...) — ĐP.don_vi_cha_id trỏ TW (KHÔNG qua BN).

> **Mô hình quyền:** Vai trò X được gán quyền xem dữ liệu của tập đơn vị Y. User thuộc vai trò X chỉ thấy dữ liệu thuộc tập Y. BR-AUTH-03 (ngang cấp KHÔNG thấy nhau) + BR-AUTH-04 (chỉ TW thấy cấp con).

---

## A. HAPPY PATH — UI CÂY + LOAD QUYỀN

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước | Kết quả mong đợi | Type | Priority |
|----|---------|---------------|----------------|-----------|----------|------------------|------|----------|
| TC-PQDL-101 | FR-VIII-16 AC1 | QTHT mở SCR-VIII-05 — chọn vai trò → load quyền hiện tại | `qtht_01`. Vai trò CB_NV_TW đã có sẵn quyền xem TW. | vai_tro=CB_NV_TW | 1. Login `qtht_01`. 2. Sidebar "Quản trị → Phân quyền → Dữ liệu". 3. Click dropdown vai trò. 4. Chọn CB_NV_TW. | **STATE**: BE GET `/api/v1/phan-quyen-du-lieu?vai_tro_id=...`. **UI**: SCR-VIII-05 có dropdown vai trò (#1, srs-fr-10:1601). Cây đơn vị render 2-tầng. Checkbox đánh dấu TW (đã có quyền). Tag-list (#4) hiển thị "Cục BLDS&KT". Nút [Lưu] (#5). **PERSIST**: — | Happy | P0 |
| TC-PQDL-102 | BR-AUTH-02 v3.1 (cây 2-tầng) | Verify cây render đúng mô hình 2-tầng TW → {BN, ĐP} (KHÔNG nested BN→ĐP) | `qtht_01`. DON_VI seed đầy đủ. | — | 1. Mở SCR-VIII-05. 2. Chọn 1 vai trò bất kỳ. 3. Quan sát cây expand đầy đủ. | **STATE**: BE GET cây — DON_VI.don_vi_cha_id ĐP trỏ TW (srs-fr-10:1967). **UI**: Cây có cấu trúc: TW (root) → 2 nhánh ngang cấp song song [BN_*..., DP_*...]. KHÔNG có nested BN_ABC → DP_XYZ. Số node = 1 + ~20 + ~63 ≈ 84 node tổng (verify ≥ 80). **PERSIST**: — | Happy | P0 |
| TC-PQDL-103 | FR-VIII-16 AC2 | Gán quyền xem 1 ĐP cho vai trò CB_NV_DP | `qtht_01`. CB_NV_DP chưa có quyền nào. | vai_tro=CB_NV_DP, don_vi_ids=[DP_HCM] | 1. Chọn vai trò CB_NV_DP. 2. Tick checkbox DP_HCM trong cây. 3. Quan sát tag-list (#4). 4. Click [Lưu]. | **STATE**: BE PUT `/api/v1/phan-quyen-du-lieu` body `{vai_tro_id, don_vi_ids:[DP_HCM_id]}`. Transaction: xóa quyền cũ + tạo mới (srs-fr-10:772). Cập nhật cache (#7 srs-fr-10:773). AUDIT_LOG. **UI**: Tag-list hiển thị "Sở Tư pháp HCM". Toast "Lưu thành công". **PERSIST**: User thuộc CB_NV_DP login → chỉ thấy dữ liệu DP_HCM. | Happy | P0 |
| TC-PQDL-104 | SCR-VIII-05 #2 (cha → con auto check) | Tick TW (parent) → auto tick BN + ĐP (children) | `qtht_01`. Vai trò QTHT_BACKUP. | — | 1. Chọn vai trò. 2. Tick checkbox TW. 3. Quan sát BN + ĐP. | **STATE**: FE cascade. **UI**: Tất cả ~83 node con (BN + ĐP) tự tick (BR-AUTH-04 cha thấy cấp con — srs-fr-10:1602, 2173). Tag-list có ≥ 84 đơn vị. **PERSIST**: — | Happy | P0 |
| TC-PQDL-105 | BR-AUTH-04 (verify TW thấy con) | Sau khi tick TW → user thuộc vai trò thấy data BN + ĐP | `qtht_01`. Vai trò QTHT_BACKUP gán full TW + cascade. | — | 1. Login user thuộc QTHT_BACKUP (vd qtht_03 nếu có). 2. Vào module có data BN + ĐP (vd UC57 Vụ việc). | **STATE**: BE filter `WHERE don_vi_id IN (TW + cascade BN + ĐP)`. **UI**: User thấy data của TW + BN + ĐP. **PERSIST**: Cross-module verify. | Happy | P1 |
| TC-PQDL-106 | SCR-VIII-05 #4 (tag-list bỏ chọn) | Click X trên tag → uncheck checkbox tương ứng | `qtht_01`. Vai trò có 5 đơn vị đã chọn. | — | 1. Chọn vai trò. 2. Click X trên 1 tag (vd Sở TP HCM). | **STATE**: FE remove. Cây checkbox uncheck. **UI**: Tag biến mất. Checkbox cây uncheck. | Happy | P1 |
| TC-PQDL-107 | FR-VIII-16 step 6 (transaction) | Gán quyền — verify atomic transaction (xóa cũ + tạo mới) | `qtht_01`. Vai trò X đã có 3 đơn vị {A, B, C}. | vai_tro=X, don_vi_ids=[D, E] (khác hoàn toàn) | 1. Chọn vai trò X. 2. Uncheck A/B/C. 3. Tick D, E. 4. [Lưu]. | **STATE**: BE 1 transaction: DELETE old (3 row), INSERT new (2 row). Nếu BE crash giữa chừng → rollback. **UI**: Toast "Lưu thành công". Reload → tag-list chỉ còn D, E. **PERSIST**: AUDIT_LOG action='UPDATE' với chi_tiet diff `{old:[A,B,C], new:[D,E]}`. | Happy | P0 |

---

## B. NEGATIVE — BR-AUTH-03 NGANG CẤP + ERROR HANDLING

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước | Kết quả mong đợi | Type | Priority |
|----|---------|---------------|----------------|-----------|----------|------------------|------|----------|
| TC-PQDL-120 | ERR-PQ-01 + BR-AUTH-03 (SPEC-CLARIFY-TKPQ-05) | Vai trò cap=BN cố gán quyền xem ĐP — block ngang cấp | `qtht_01`. Vai trò Y có `cap=BN` (ERD srs-fr-10:1988 chỉ enum 'TW'/'BN'/'DP'/'ALL' — KHÔNG chứa đơn vị cụ thể). Y đã thuộc đơn vị BN bất kỳ qua liên kết khác (BA chốt 2026-05-08 cần clarify). | vai_tro=Y (cap=BN), don_vi_ids=[DP bất kỳ] | 1. Chọn vai trò Y. 2. Tick checkbox 1 ĐP. 3. Quan sát alert + nút Lưu. | **STATE**: FE/BE detect ngang cấp dựa trên `Y.cap='BN'` vs `target_don_vi.cap='DP'` (BR-AUTH-03 srs-fr-10:2167 — BN/ĐP độc lập, không thấy nhau). **UI**: Alert đỏ với pattern "Không thể gán quyền xem đơn vị {ten_dp} cho vai trò {ten_y} (ngang cấp)" (SCR-VIII-05 #3 + ERR-PQ-01 srs-fr-10:780). Nút [Lưu] disabled. **PERSIST**: KHÔNG có quyền tạo. **Note SPEC-CLARIFY-TKPQ-05**: SRS line 780 nói "vai trò thuộc đơn vị {B}" nhưng VAI_TRO entity không có `don_vi_id` field — chỉ có `cap`. Cách suy "vai trò thuộc đơn vị" cần BA clarify (qua TAI_KHOAN_VAI_TRO junction? qua VAI_TRO.cap + tenant context?). TC này test logic ngang cấp dựa trên cap, không assert mapping role→specific đơn vị. | Negative | P0 |
| TC-PQDL-121 | ERR-PQ-01 + BR-AUTH-03 | Vai trò cap=BN cố gán quyền xem BN khác (KHÔNG cùng tenant) — block | `qtht_01`. Vai trò Z `cap=BN`. | vai_tro=Z, don_vi_ids=[1 BN khác tenant] | 1. Chọn Z. 2. Tick BN bất kỳ khác. | **STATE**: FE/BE detect ngang cấp theo cap (BN target ≠ BN của Z). **UI**: Alert tương tự TC-120 — KHÔNG cho gán BN khác cho vai trò cap=BN. **PERSIST**: SPEC-CLARIFY-TKPQ-05 cross-ref. | Negative | P0 |
| TC-PQDL-122 | ERR-PQ-01 + BR-AUTH-03 | Vai trò cap=DP cố gán quyền xem DP khác — block | `qtht_01`. Vai trò W `cap=DP`. | vai_tro=W, don_vi_ids=[1 DP khác] | 1. Chọn W. 2. Tick DP khác. | **STATE**: FE/BE detect ngang cấp DP-DP. **UI**: Alert. Block. | Negative | P0 |
| TC-PQDL-123 | BR-AUTH-04 + SPEC-CLARIFY-TKPQ-05 | Vai trò cap=BN gán đơn vị BN cùng tenant — hợp lệ | `qtht_01`. Vai trò Z cap=BN. | vai_tro=Z, don_vi_ids=[BN cùng tenant với Z] | 1. Chọn Z. 2. Tick BN cùng tenant. | **STATE**: BE accept (cùng cấp + cùng tenant). **UI**: Tag-list hiện đơn vị BN. [Lưu] enabled. **PERSIST**: SPEC-CLARIFY-TKPQ-05 — cách suy "cùng tenant" cần BA clarify. | Happy | P0 |
| TC-PQDL-124 | BR-AUTH-04 (cap=ALL hoặc TW thấy con) | Vai trò TW (cap=TW) có thể gán BN/ĐP bất kỳ | `qtht_01`. Vai trò QTHT (cap=ALL hoặc TW). | don_vi_ids=[TW + BN_BTC + DP_HCM] | 1. Chọn QTHT. 2. Tick 3 đơn vị 3 cấp. | **STATE**: BE accept (BR-AUTH-04 cha thấy con — srs-fr-10:2173). **UI**: 3 tag. [Lưu] OK. | Happy | P0 |
| TC-PQDL-125 | ERR-PQ-02 (E2) | Vai trò bị xóa giữa lúc đang phân quyền | `qtht_01`. Vai trò V đã chọn. | — | 1. Chọn V. 2. Tab khác xóa V (qua UC112). 3. Quay lại tab gốc, tick đơn vị. 4. [Lưu]. | **STATE**: BE check vai trò tồn tại → reject 400. **UI**: Toast ERROR nguyên văn "Vai trò không tồn tại" (srs-fr-10:781). Form clear hoặc redirect. | Negative | P1 |
| ~~TC-PQDL-126~~ | ~~ERR-PQ-03~~ | **MOVED to `07-TC-security-IDOR.md` TC-IDOR-PQDL-001 (2026-05-08 Codex R2)** — FK injection test, A7 cấm. | — | — | — | Moved | — |
| TC-PQDL-127 | FR-VIII-16 input #2 bắt buộc (srs-fr-10:760) | Bỏ trống don_vi_ids — reject | `qtht_01`. Vai trò V trước đó có 3 đơn vị. | don_vi_ids=[] | 1. Chọn V. 2. Uncheck tất cả. 3. [Lưu]. | **STATE**: SRS srs-fr-10:760 nguyên văn `don_vi_ids | identifier[] | Y` — bắt buộc ≥ 1. BE/FE reject. **UI**: Inline ERROR "Vui lòng chọn ít nhất 1 đơn vị" hoặc tương đương. Nút [Lưu] disabled khi tag-list rỗng. **PERSIST**: Quyền cũ giữ nguyên (không bị clear). (Note Codex R2: SPEC-CLARIFY-TKPQ-20 đã withdraw — SRS rõ ràng yêu cầu Y, không phải ambiguity.) | Negative | P1 |

---

## C. SECURITY & EDGE — IDOR + Cache + Cascading

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước | Kết quả mong đợi | Type | Priority |
|----|---------|---------------|----------------|-----------|----------|------------------|------|----------|
| ~~TC-PQDL-130~~ | ~~BR-AUTH-01 IDOR~~ | **MOVED to `07-TC-security-IDOR.md` TC-IDOR-PQDL-002 (2026-05-08 Codex R2)** — Direct API authz test, A7 cấm. | — | — | — | Moved | — |
| TC-PQDL-131 | BR-AUTH-08 cache refresh (FR-VIII-16 step 7) | Sau khi đổi quyền, user thuộc vai trò đó cần re-login để áp dụng | `qtht_01`. User U đang login, thuộc vai trò X. | — | 1. User U mở module, thấy data đơn vị A. 2. `qtht_01` đổi quyền X → bỏ A, thêm B. 3. User U reload module. 4. (Nếu vẫn thấy A) — User U logout/login lại. | **STATE**: BE invalidate session/cache cho user thuộc vai trò X (srs-fr-10:773). Hoặc lazy refresh khi user request mới. **UI**: User U sau reload (hoặc re-login) chỉ thấy data B, không thấy A. **PERSIST**: AUDIT_LOG ghi UPDATE policy. SPEC-CLARIFY-TKPQ-21 — cần reload tự động hay user phải re-login. | Edge | P1 |
| TC-PQDL-132 | A4 cascade uncheck parent | Tick TW rồi uncheck TW → uncheck BN + ĐP cascade | `qtht_01`. | — | 1. Tick TW (84 node). 2. Uncheck TW. | **STATE**: FE cascade reverse. **UI**: Tất cả 84 node uncheck. Tag-list rỗng. | Happy | P1 |
| TC-PQDL-133 | A4 partial check (1 BN + 1 ĐP cùng nhánh hợp lệ) | Tick BN_BTC + DP_HN cho vai trò QTHT (cap=ALL) | `qtht_01`. Vai trò QTHT cap=ALL. | don_vi_ids=[BN_BTC, DP_HN] | 1. Chọn QTHT. 2. Tick 2 đơn vị (1 BN + 1 ĐP). 3. [Lưu]. | **STATE**: BE accept (QTHT bypass BR-AUTH-03 — TC-124 pattern). Tuy nhiên ngang cấp BN-DP — verify behavior nếu vai trò cap=ALL có miễn ngang cấp không. **UI**: 2 tag. [Lưu] OK. **PERSIST**: SPEC-CLARIFY-TKPQ-22 — vai trò cap=ALL có chịu ràng buộc ngang cấp BR-AUTH-03? | Edge | P1 |
| TC-PQDL-134 | A4 large selection (84 node) | Tick TW (cascade 84 node) → submit — verify performance | `qtht_01`. | don_vi_ids = full tree | 1. Tick TW (auto cascade). 2. [Lưu]. 3. Đo response time qua list_network_requests. | **STATE**: BE INSERT 84 row trong 1 transaction. **UI**: Response ≤ 3s. KHÔNG hang. **PERSIST**: AUDIT_LOG có 1 entry với chi_tiet (84 đơn vị). | Edge | P2 |
| TC-PQDL-135 | A4 entity_type filter (FR-VIII-16 input #3) | Gán quyền chỉ cho 1 entity type cụ thể | `qtht_01`. | vai_tro=X, don_vi_ids=[A], entity_type='VU_VIEC' | 1. (Nếu UI có select entity_type — SCR-VIII-05 không show tường minh). 2. Set entity_type=VU_VIEC. 3. [Lưu]. | **STATE**: BE lưu QUYEN_HAN với entity_type. User thuộc X chỉ thấy VU_VIEC của đơn vị A, KHÔNG thấy DOANH_NGHIEP của A. **UI**: SPEC-CLARIFY-TKPQ-23 — UI có hiển thị entity_type filter không? Nếu không, log gap. | Edge | P2 |
| TC-PQDL-136 | A4 audit log gán quyền | AUDIT_LOG ghi đầy đủ chi_tiet old/new khi đổi quyền | `qtht_01`. Vai trò X có quyền {A,B}. | new=[B,C] | 1. Đổi quyền X. 2. SCR-VIII-10 filter Module=Quản trị, Entity=QUYEN_HAN. | **STATE**: AUDIT_LOG action='UPDATE' chi_tiet `{vai_tro_id, old:[A,B], new:[B,C]}`. **UI**: Expand JSON OK. | Happy | P1 |
| TC-PQDL-137 | A6 fill — vai trò chưa có quyền nào | Chọn vai trò mới tạo (chưa gán quyền) → cây render rỗng | `qtht_01`. Tạo vai trò NEW_ROLE qua UC112, chưa gán quyền. | vai_tro=NEW_ROLE | 1. Mở SCR-VIII-05. 2. Chọn NEW_ROLE. | **STATE**: BE GET trả `don_vi_ids=[]`. **UI**: Cây render đầy đủ 84 node nhưng KHÔNG có checkbox nào tick. Tag-list trống. **PERSIST**: — | Happy | P1 |
| TC-PQDL-138 | A6 fill — đơn vị bị TAM_DUNG | Đơn vị HOẠT ĐỘNG=TAM_DUNG vẫn hiện trong cây? | `qtht_01`. DON_VI có 1 ĐP `trang_thai=TAM_DUNG` (srs-fr-10:1973). | — | 1. Mở SCR-VIII-05. 2. Quan sát cây. | **STATE**: BE filter `WHERE trang_thai='HOAT_DONG'` HOẶC include TAM_DUNG với badge khác. **UI**: Verify behavior. SPEC-CLARIFY-TKPQ-24. | Edge | P2 |

---

## Tổng số TC: 22 (7 Happy + 6 Negative + 9 Security/Edge) — A3 base 16 + A4 merged 6 + A6 fill 2 - Codex R2 -2 IDOR moved (TC-126, 130)

**Priority**: P0=9 / P1=9 / P2=4

**Coverage (sau Codex R2):**
- BR: BR-AUTH-01 (precondition; IDOR moved 07), BR-AUTH-02 v3.1 (TC102 cây 2-tầng), BR-AUTH-03 (TC120-122 ngang cấp dựa trên cap), BR-AUTH-04 (TC104-105 cha-con), BR-AUTH-08 (TC131 cache refresh), BR-DATA-05 (TC136 audit)
- AC SRS (3 AC): AC1 ✅ (TC101), AC2 ✅ (TC103), AC3 (Quy tắc ngang cấp ✅ TC120-122)
- Error codes (3): ERR-PQ-01 ✅ (TC120-122), ERR-PQ-02 ✅ (TC125), ERR-PQ-03 ✅ (moved 07 TC-IDOR-PQDL-001)
- Codex R2 fix 2026-05-08: TC120-123 reframe ngang cấp dựa trên `cap` enum (KHÔNG assert mapping role→specific don_vi); TC127 force expected reject empty (SPEC-CLARIFY-TKPQ-20 withdrawn — SRS rõ Y bắt buộc)
- A4 merged 2026-05-08: TC131-136 (cache, cascade, large selection, entity_type, audit) — IDOR (TC130) moved
- A6 fill 2026-05-08: TC137 (vai trò mới chưa quyền), TC138 (đơn vị TAM_DUNG)
- SPEC-CLARIFY: TKPQ-05 (vai trò "thuộc đơn vị" suy thế nào — VAI_TRO không có don_vi_id), TKPQ-21 (cache refresh strategy), TKPQ-22 (cap=ALL có ràng buộc ngang cấp?), TKPQ-23 (entity_type UI), TKPQ-24 (đơn vị TAM_DUNG)

---

## D. Note về A7 — UI vs API (Codex R2 update)

> **2026-05-08 Codex R2:** TC-PQDL-126 + TC-PQDL-130 (IDOR/FK injection) đã MOVE sang `07-TC-security-IDOR.md`. A7 rule cấm test API thuần. File này còn lại 100% functional UC.
> TC-PQDL-105 + TC-PQDL-131 cross-module verify — login user thuộc vai trò + vào module có data thực tế (vd UC57 Vụ việc) → kiểm tra qua list rendered. UI bridge OK.
> TC-PQDL-120-123 reframe (Codex R2): không assert mapping role→specific don_vi (vì VAI_TRO ERD không có don_vi_id field — chỉ `cap` TW/BN/DP/ALL). Test logic ngang cấp dựa trên cap enum. Mapping cụ thể chờ BA clarify SPEC-CLARIFY-TKPQ-05.
> TC-PQDL-136 verify audit qua SCR-VIII-10 — UI bridge.
