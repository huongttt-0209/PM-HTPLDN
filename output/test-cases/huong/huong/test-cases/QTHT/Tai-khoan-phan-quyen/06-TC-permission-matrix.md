# Test Cases — Permission Matrix Cross-FR (BR-AUTH-01 + IDOR + Tier 2 chặn)

> **SRS Ref**: BR-AUTH-01 (srs-v3.1.md §B.1, srs-fr-10:2155), BR-AUTH-08 (srs-fr-10:2191), BR-AUTH-09 (srs-fr-10:2197), Permission matrix module-level (xem 00-test-plan-overview §2.3)
> **Ngày tạo**: 2026-05-08 (BMAD A3 base + A4 inline merge)
> **Pattern reference**: `output/test-cases/QTHT/Nhat-ky-he-thong/03-TC-permission-matrix.md`

> **Iron rule:** UC112-115 (Vai trò + Tài khoản + PQ Dữ liệu + PQ Chức năng) thuần QTHT (BR-AUTH-01 Tier 1 nội bộ). Mọi role khác đều phải bị reject — không có exception "ngang cấp" như Mẫu phản hồi (Mô hình B Hybrid). FR-VIII-26 ngược lại — public link, mọi role có email đều dùng được.

---

## A. ROLE-BASED ACCESS HAPPY PATH

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước | Kết quả mong đợi | Type | Priority |
|----|---------|---------------|----------------|-----------|----------|------------------|------|----------|
| TC-TKPQ-PERM-001 | BR-AUTH-01 + AC1 (UC112) | QTHT truy cập SCR-VIII-02 — full quyền CRUD vai trò | `qtht_01`. | — | 1. Login `qtht_01`. 2. URL `/quan-tri/vai-tro`. 3. Quan sát toolbar + bảng + button [+ Thêm] / [Sửa] / [Xóa]. | **STATE**: BE accept (BR-AUTH-01). **UI**: Bảng load, đầy đủ button hành động. **PERSIST**: TC-VT-101 cùng coverage. | Happy | P0 |
| TC-TKPQ-PERM-002 | BR-AUTH-01 + AC1 (UC113) | QTHT truy cập SCR-VIII-03 — full quyền CRUD + lifecycle TK | `qtht_01`. | — | 1. URL `/quan-tri/tai-khoan`. | **STATE/UI**: Đầy đủ button [+ Thêm] / [Sửa] / [Khóa] / [Mở khóa] / [Vô hiệu hóa] / [Khôi phục] / [Phê duyệt]. **PERSIST**: — | Happy | P0 |
| TC-TKPQ-PERM-003 | BR-AUTH-01 + AC1 (UC114) | QTHT truy cập SCR-VIII-05 — full quyền phân quyền dữ liệu | `qtht_01`. | — | 1. URL `/quan-tri/phan-quyen-du-lieu`. | **STATE/UI**: Cây 2-tầng + dropdown vai trò + nút [Lưu]. | Happy | P0 |
| TC-TKPQ-PERM-004 | BR-AUTH-01 + AC1 (UC115) | QTHT truy cập SCR-VIII-04 — full quyền phân quyền chức năng | `qtht_01`. | — | 1. URL `/quan-tri/phan-quyen-chuc-nang`. | **STATE/UI**: Matrix + cây menu + nút [Lưu] [Reset]. | Happy | P0 |
| TC-TKPQ-PERM-005 | BR-AUTH-01 + AC1 cross-tenant | QTHT cap=ALL bypass BR-AUTH-08 — thấy/sửa được vai trò + TK của mọi đơn vị | `qtht_01`. | — | 1. UC112 list — đếm vai trò có cap đa dạng (TW, BN, DP). 2. UC113 filter đơn vị BN_BTC. 3. UC114 cây hiển thị đầy đủ TW + BN + ĐP. | **STATE**: BE bypass don_vi_id filter cho QTHT (BR-AUTH-08 ngoại lệ srs-fr-10:2191). **UI**: Verify QTHT thấy data cross cấp. **PERSIST**: — | Happy | P0 |

---

## B. NEGATIVE — NON-QTHT BLOCK (UC112-115)

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước | Kết quả mong đợi | Type | Priority |
|----|---------|---------------|----------------|-----------|----------|------------------|------|----------|
| TC-TKPQ-PERM-010 | BR-AUTH-01 (UC112) | CB_NV_TW không truy cập được SCR-VIII-02 | `cb_nv_tw_01`. | — | 1. Direct URL `/quan-tri/vai-tro` (sidebar không có entry nếu BE filter). | **STATE**: BE reject 403. **UI**: 2 option hợp lệ: (a) HTTP 403 page với toast "Bạn không có quyền truy cập"; (b) Sidebar không có entry → URL direct redirect home. **PERSIST**: — | Negative | P0 |
| TC-TKPQ-PERM-011 | BR-AUTH-01 (UC112) | CB_NV_BN không truy cập được | `cb_nv_bn_01`. | — | (như TC-010) | **STATE/UI**: Same. | Negative | P0 |
| TC-TKPQ-PERM-012 | BR-AUTH-01 (UC112) | CB_NV_DP không truy cập được | `cb_nv_dp_01`. | — | (như TC-010) | **STATE/UI**: Same. | Negative | P1 |
| TC-TKPQ-PERM-013 | BR-AUTH-01 (UC112) | CB_PD (TW/BN/DP) không truy cập được | 3 user `cb_pd_*_01`. | — | 1. Mỗi tài khoản, URL direct. | **STATE/UI**: Same TC-010 cho cả 3. | Negative | P1 |
| TC-TKPQ-PERM-014 | BR-AUTH-01 + Tier 2 (UC112) | DN/CG/TVV/NHT không vào CMS | 4 user `dn_01`, `cg_01`, `tvv_01`, `nht_01`. | — | 1. Mỗi tài khoản, URL direct CMS. | **STATE**: Tier 2 SSO không có entry CMS — chỉ Cổng PLQG. **UI**: Redirect Cổng hoặc 403/login CMS. **PERSIST**: — | Negative | P0 |
| TC-TKPQ-PERM-015 | BR-AUTH-01 (UC113) | CB_NV_TW không truy cập SCR-VIII-03 | `cb_nv_tw_01`. | — | 1. URL `/quan-tri/tai-khoan`. | **STATE**: BE reject 403. **UI**: Same TC-010. | Negative | P0 |
| TC-TKPQ-PERM-016 | BR-AUTH-01 (UC113) | CB_NV_BN/DP + CB_PD all chặn | (multi user 6 lượt) | — | 1. Mỗi user URL direct UC113. | **STATE/UI**: 403 toàn bộ. | Negative | P1 |
| TC-TKPQ-PERM-017 | BR-AUTH-01 (UC114) | Non-QTHT chặn UC114 | (như TC-015 với 6 user khác) | — | 1. URL `/quan-tri/phan-quyen-du-lieu`. | **STATE/UI**: 403. | Negative | P0 |
| TC-TKPQ-PERM-018 | BR-AUTH-01 (UC115) | Non-QTHT chặn UC115 | (như TC-017) | — | 1. URL `/quan-tri/phan-quyen-chuc-nang`. | **STATE/UI**: 403. | Negative | P0 |

---

## C. IDOR — MOVED TO `07-TC-security-IDOR.md` (Codex R2 2026-05-08)

> **6 TC IDOR** (TC-TKPQ-PERM-020 to 025) đã chuyển sang file `07-TC-security-IDOR.md` Section E (TC-IDOR-PERM-001 to 006). A7 rule cấm test API thuần "đội lốt" UI bridge trong functional UC suite. Security/dev team chạy file 07 qua tool API riêng.

- ~~TC-TKPQ-PERM-020~~ → moved as TC-IDOR-PERM-001 (UC112 POST non-QTHT)
- ~~TC-TKPQ-PERM-021~~ → moved as TC-IDOR-PERM-002 (UC112 DELETE non-QTHT)
- ~~TC-TKPQ-PERM-022~~ → moved as TC-IDOR-PERM-003 (UC113 POST non-QTHT)
- ~~TC-TKPQ-PERM-023~~ → moved as TC-IDOR-PERM-004 (UC113 PATCH lock non-QTHT)
- ~~TC-TKPQ-PERM-024~~ → moved as TC-IDOR-PERM-005 (UC114 PUT non-QTHT)
- ~~TC-TKPQ-PERM-025~~ → moved as TC-IDOR-PERM-006 (UC115 PUT non-QTHT)

---

## D. FR-VIII-26 PUBLIC ACCESS (KHÔNG CẦN ĐĂNG NHẬP)

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước | Kết quả mong đợi | Type | Priority |
|----|---------|---------------|----------------|-----------|----------|------------------|------|----------|
| TC-TKPQ-PERM-030 | FR-VIII-26 public | DN truy cập "Quên mật khẩu" — không cần đăng nhập trước | Tester chưa login. | email=dn_01_email | 1. Mở `/login`. 2. Click "Quên mật khẩu" link. 3. Submit email. | **STATE**: BE accept không yêu cầu auth. **UI**: Form mở. Toast trung tính. **PERSIST**: Mail gửi. | Happy | P0 |
| TC-TKPQ-PERM-031 | FR-VIII-26 + AC1 | TVV mới chưa từng login → kích hoạt qua mail | `tvv_test_new` chưa từng login (CHO_KICH_HOAT). | (mail tự động) | 1. MailHog. 2. Click link. 3. Đặt MK. | **STATE**: SM-T4. **UI**: TC-PWD-102 pattern. | Happy | P0 |
| TC-TKPQ-PERM-032 | FR-VIII-26 cross-role | CB nội bộ (qtht_01, cb_nv_tw_01...) cũng dùng được "Quên mật khẩu" | qtht_01 quên MK. | — | (như TC-030 cho qtht_01) | **STATE**: BE accept (FR-VIII-26 nguyên văn "user bất kỳ" srs-fr-10:1252). **UI**: Form OK. **PERSIST**: Mail đến. | Happy | P1 |

---

## E. CROSS-TENANT VERIFICATION (BR-AUTH-08)

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước | Kết quả mong đợi | Type | Priority |
|----|---------|---------------|----------------|-----------|----------|------------------|------|----------|
| TC-TKPQ-PERM-040 | BR-AUTH-08 (sibling pattern) | QTHT bypass don_vi_id filter cho UC113 — thấy TK đa cấp | `qtht_01`. ≥ 1 TK mỗi cấp (TW + BN + DP). | — | 1. UC113 không filter. 2. Đếm số TK + cấp đơn vị. | **STATE**: BE bypass `don_vi_id` filter cho QTHT (BR-AUTH-08 ngoại lệ srs-fr-10:2191). **UI**: Bảng có TK của TW + BN + DP. Cột Đơn vị có ≥ 3 giá trị. | Happy | P0 |
| TC-TKPQ-PERM-041 | A4 IDOR cross-tenant (sibling) | `qtht_01` xem TK của BN_BKH (đã thuộc đơn vị TW khác) | `qtht_01`. TK x thuộc BN_BKH. | filter don_vi=BN_BKH | 1. UC113 filter đơn vị. 2. Quan sát. | **STATE**: BE accept (QTHT bypass). **UI**: TK x hiện. **PERSIST**: — | Happy | P1 |

---

## F. AUDIT TRAIL (BR-DATA-05)

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước | Kết quả mong đợi | Type | Priority |
|----|---------|---------------|----------------|-----------|----------|------------------|------|----------|
| TC-TKPQ-PERM-050 | BR-DATA-05 cross-FR | AUDIT_LOG ghi đầy đủ mọi action UC112-115 (CREATE/UPDATE/DELETE/LOCK/UNLOCK/DEACTIVATE/RESTORE/APPROVE/REJECT/PERMISSION_UPDATE) | `qtht_01`. | (sequential ops) | 1. Tạo vai trò. 2. Tạo TK. 3. Khóa TK. 4. Đổi quyền dữ liệu. 5. Đổi quyền chức năng. 6. SCR-VIII-10 filter Module=Quản trị. | **STATE**: 5+ entry trong AUDIT_LOG với action codes phân biệt. **UI**: Bảng SCR-VIII-10 có nhiều dòng badge khác. | Happy | P1 |
| TC-TKPQ-PERM-051 | BR-DATA-05 ip_address | AUDIT_LOG có IP của QTHT thực hiện | `qtht_01`. | — | 1. Tạo vai trò. 2. SCR-VIII-10 expand chi tiết. | **STATE**: Mỗi entry có `ip_address` field (theo SCR-VIII-10 #9 Output srs-fr-10:1354). **UI**: Verify cột/expand có IP. | Happy | P2 |

---

## Tổng số TC: 18 (5 Happy + 9 Negative role-block + 3 FR-VIII-26 public + 2 Cross-tenant + 2 Audit + 6 IDOR moved to 07) — A3 base 18 - Codex R2 -6 IDOR moved

**Priority**: P0=9 / P1=8 / P2=1

**Coverage (sau Codex R2):**
- BR: BR-AUTH-01 ✅ (TC role-based UI access; IDOR API moved 07), BR-AUTH-08 ✅ (TC005, TC040, TC041 cross-tenant), BR-AUTH-09 (verify CB không VNeID — file 02 TC-198), BR-DATA-05 ✅ (TC050-051 audit cross-FR)
- AC SRS module-level: AC permission ✅ (tất cả 4 UC đều có permission AC)
- Roles tested: QTHT (full), CB_NV (TW/BN/DP × 4 UC = 12 entry), CB_PD (TW/BN/DP × 4 UC = 12 entry), Tier 2 (DN/CG/TVV/NHT × 4 UC), FR-VIII-26 public access (3 nhóm)
- IDOR coverage: MOVED to file 07 (file này focus UI access via URL direct + audit verify)

---

## G. Note về A7 — UI vs API (Codex R2 update)

> **2026-05-08 Codex R2:** 6 TC IDOR (TC-020 đến TC-025) đã MOVE sang `07-TC-security-IDOR.md` Section E. A7 rule cấm test API thuần. File này còn lại 100% functional UC test qua URL direct navigate + UI access verify.
> TC-050 + TC-051 verify AUDIT_LOG qua SCR-VIII-10 (UI module W1.1) — UI bridge.
> TC-031 verify mail qua MailHog UI — UI bridge.
