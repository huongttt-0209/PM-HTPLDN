# Test Cases — FR-VIII-26 v3.1: Quên Mật khẩu / Kích hoạt Tài khoản Lần đầu

> **SRS Ref**: FR-VIII-26 (srs-fr-10:1241-1311 — v3.1 mới), SCR-VIII-07 link "Quên mật khẩu" (srs-fr-10:1722), Entity TAI_KHOAN field `token_reset_mk` + `token_het_han` (srs-fr-10:1951-1952), SM-TAIKHOAN T2/T3/T4 + trigger SM-TVV/SM-NHT
> **Ngày tạo**: 2026-05-08 (BMAD A3 base + A4 inline merge + A6 fill)
> **Tác nhân**: User bất kỳ có email trong hệ thống (DN/NHT/TVV/CG/CB) — public link, KHÔNG cần đăng nhập

> **Pre-condition chung mọi TC trong file:** TAI_KHOAN seed có ≥ 5 record đa dạng trạng thái (HOAT_DONG, CHO_KICH_HOAT vai_tro=DN, CHO_KICH_HOAT vai_tro=TVV, CHO_KICH_HOAT vai_tro=NULL, TAM_KHOA, VO_HIEU_HOA). MailHog `http://103.172.236.130:8025` accessible để verify mail.

> **Workflow tổng:** User → SCR-VIII-07 click "Quên mật khẩu" → form nhập email → BE sinh token → mail link → user click link → form đặt MK → submit → guard SM-TAIKHOAN.

---

## A. HAPPY PATH — REQUEST RESET + DELIVER MAIL

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước | Kết quả mong đợi | Type | Priority |
|----|---------|---------------|----------------|-----------|----------|------------------|------|----------|
| TC-PWD-101 | FR-VIII-26 step 1 + AC3 | User HOAT_DONG quên MK — submit email → nhận mail link 30 phút | Tester chưa login. TK `qtht_01` HOAT_DONG. | email=`qtht_01@example.com` (theo seed) | 1. Mở `/login` (logout nếu đang login). 2. Click link "Quên mật khẩu" (SCR-VIII-07 #10). 3. Form mở. 4. Nhập email. 5. Click submit. 6. Mở MailHog `http://103.172.236.130:8025`. | **STATE**: BE step 1-4. Sinh `token_reset_mk` random + `token_het_han` = NOW + 30 phút (HOAT_DONG case, srs-fr-10:1273). Gửi mail SMTP. **UI**: Toast/page chuyển sang "Đã gửi link đến email của bạn" hoặc trung tính TC-120. **PERSIST**: MailHog có 1 mail mới đến `qtht_01@example.com` chứa link `/reset-password?token=...`. | Happy | P0 |
| TC-PWD-102 | FR-VIII-26 step 1 + AC1 | TVV mới được CB Phê duyệt → nhận mail kích hoạt + đặt MK lần đầu (token vĩnh viễn) | TK `tvv_test_new` ở CHO_KICH_HOAT, vai_tro=TVV gán sẵn. Mail kích hoạt được gửi tự động khi tạo TK (srs-fr-10:1274 note). | (mail tự động) | 1. Mở MailHog. 2. Tìm mail kích hoạt cho TVV. 3. Click link. 4. Form đặt MK mở. 5. Nhập MK + xác nhận. 6. Submit. | **STATE**: BE step 7-13. Token vĩnh viễn (no `token_het_han` hoặc rất xa, srs-fr-10:1273). SM-T4: TAI_KHOAN.trang_thai='HOAT_DONG'. **Trigger SM-TVV**: TU_VAN_VIEN.trang_thai='HOAT_DONG' (srs-fr-10:1282, 1303). Token bị hủy (1 lần dùng, srs-fr-10:1280). AUDIT_LOG action='ACCOUNT_ACTIVATE'. **UI**: Toast "Đặt mật khẩu thành công, vui lòng đăng nhập" → redirect SCR-VIII-07. **PERSIST**: tvv_test_new đăng nhập được + xuất hiện trong UC59 phân công vụ việc. | Happy | P0 |
| TC-PWD-103 | FR-VIII-26 step 1 + AC2 | NHT mới được CB Nghiệp vụ tạo → nhận mail kích hoạt → đặt MK | TK `nht_test_new` CHO_KICH_HOAT, vai_tro=NHT. | (như TC-102 cho NHT) | (như TC-102) | **STATE**: SM-T4 + trigger SM-NHT (NGUOI_HO_TRO.trang_thai='HOAT_DONG' srs-fr-10:1282). **UI**: Toast OK. **PERSIST**: nht_test_new đăng nhập được + hiện trong list phân công VV. | Happy | P0 |
| TC-PWD-104 | FR-VIII-26 step 5-9 (form đặt MK) | Click link mail → form đặt MK với 2 field + submit thành công | TK k HOAT_DONG. Tester đã có link reset từ TC-101. | mat_khau_moi="NewPass@2026", mat_khau_xac_nhan="NewPass@2026" | 1. Click link trong mail. 2. Form đặt MK mở (2 field password). 3. Nhập MK mới + xác nhận. 4. Submit. | **STATE**: BE step 7-9: validate token + password strength + match. Hash + UPDATE TAI_KHOAN.mat_khau_hash. Hủy token. **UI**: Toast "Đặt mật khẩu thành công, vui lòng đăng nhập" → redirect `/login`. **PERSIST**: User k đăng nhập với MK mới OK. AUDIT_LOG action='PASSWORD_RESET'. | Happy | P0 |
| TC-PWD-105 | FR-VIII-26 step 11 (SM-T2 v3.1) | Self-reg DN cũ chưa có vai trò → click link → CHO_PHAN_QUYEN | TK `dn_self_reg` CHO_KICH_HOAT, vai_tro=NULL (luồng cũ trước v3.1 chưa gán DN sẵn). | mat_khau_moi="DN@Pass2026" | (như TC-104) | **STATE**: SM-T2: TAI_KHOAN.trang_thai='CHO_PHAN_QUYEN' (srs-fr-10:1281 + 2109). **UI**: Toast "Đặt mật khẩu thành công, chờ QTHT phân quyền". **PERSIST**: SCR-VIII-03 tab "Chờ phân quyền" có dn_self_reg. (Note: v3.1 self-reg DN gán DN sẵn → đi qua T4 thay T2; case này test backward-compat. SPEC-CLARIFY-TKPQ-04 confirm.) | Edge | P1 |
| TC-PWD-106 | FR-VIII-26 step 11 (SM same state HOAT_DONG) | User HOAT_DONG quên MK + reset → giữ HOAT_DONG | TK k HOAT_DONG. | (như TC-104) | (như TC-104) | **STATE**: SM transitions: HOAT_DONG → HOAT_DONG (giữ nguyên, srs-fr-10:1281 "Nếu TK đang HOAT_DONG → giữ nguyên"). **UI**: OK. **PERSIST**: k vẫn HOAT_DONG. | Happy | P0 |

---

## B. NEGATIVE — VALIDATION + TOKEN LIFECYCLE

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước | Kết quả mong đợi | Type | Priority |
|----|---------|---------------|----------------|-----------|----------|------------------|------|----------|
| TC-PWD-120 | ERR-PWD-01 (E1) + AC4 | Email không tồn tại — vẫn hiển thị thông báo trung tính (chống enumerate) | Tester chưa login. | email="not_exist@example.com" | 1. Form "Quên mật khẩu". 2. Nhập email không tồn tại. 3. Submit. | **STATE**: BE check email tồn tại → KHÔNG sinh token, KHÔNG gửi mail. **UI**: Toast/page **TRUNG TÍNH** nguyên văn "Nếu email đã đăng ký, link đặt mật khẩu sẽ được gửi đến hộp thư của bạn" (srs-fr-10:1290). KHÔNG báo "Email không tồn tại" — chống enumerate (security best practice). **PERSIST**: MailHog KHÔNG có mail mới. | Negative | P0 |
| TC-PWD-121 | ERR-PWD-02 (E2) | TK đang TAM_KHOA — request reset bị reject | TK locked_user TAM_KHOA. | email=locked_user_email | 1. Submit email. | **STATE**: BE check trang_thai (srs-fr-10:1272). **UI**: Toast/page ERROR nguyên văn "Tài khoản đã bị khóa hoặc vô hiệu hóa. Liên hệ quản trị viên để được hỗ trợ" (srs-fr-10:1291). **PERSIST**: KHÔNG có mail. | Negative | P0 |
| TC-PWD-122 | ERR-PWD-02 (E2) | TK VO_HIEU_HOA — request reset bị reject | TK disabled_user VO_HIEU_HOA. | email=disabled_user_email | 1. Submit email. | **STATE**: BE check. **UI**: ERR-PWD-02 (cùng nội dung TC-121). **PERSIST**: — | Negative | P0 |
| TC-PWD-123 | ERR-PWD-03 (E3) | Token reset hết hạn (>30 phút) — reject form đặt MK | Tester có link reset cách đây 31 phút (HOAT_DONG case). | mat_khau_moi="Test@2026" | 1. Click link đã hết hạn. 2. Form đặt MK mở. 3. Submit. | **STATE**: BE check `token_het_han < NOW`. **UI**: Toast/page ERROR "Link đặt mật khẩu đã hết hạn. Vui lòng yêu cầu link mới" (srs-fr-10:1292). Có link "Yêu cầu link mới". **PERSIST**: TAI_KHOAN.mat_khau_hash KHÔNG đổi. | Negative | P0 |
| TC-PWD-124 | ERR-PWD-04 (E4) | Token đã sử dụng — reject lần 2 | TK k HOAT_DONG đã reset MK qua TC-104 (token đã hủy). | (cùng link) | 1. Click LẠI link đã dùng. 2. Form mở (hoặc redirect direct). 3. Submit. | **STATE**: BE check `token_reset_mk IS NULL` (đã hủy sau lần 1) → reject. **UI**: ERROR "Link đặt mật khẩu đã được sử dụng. Vui lòng yêu cầu link mới" (srs-fr-10:1293). **PERSIST**: — | Negative | P0 |
| TC-PWD-125 | ERR-PWD-05 (E5) | Mật khẩu yếu (< 8 ký tự) | Tester có link reset hợp lệ. | mat_khau_moi="Abc1!" (5 chars) | 1. Click link. 2. Nhập MK 5 chars. 3. Submit. | **STATE**: BE/FE validate length + complexity (srs-fr-10:1264). **UI**: Inline ERROR "Mật khẩu chưa đủ mạnh" (srs-fr-10:1294). **PERSIST**: TAI_KHOAN không đổi. | Negative | P0 |
| TC-PWD-126 | ERR-PWD-05 (E5) | MK chỉ chữ thường (thiếu hoa + số + đặc biệt) | Token hợp lệ. | mat_khau_moi="abcdefgh" | 1. Submit MK chỉ chữ thường. | **STATE**: BE/FE validate complexity. **UI**: ERR-PWD-05. | Negative | P0 |
| TC-PWD-127 | ERR-PWD-05 boundary | MK 8 ký tự + đủ 4 nhóm — VALID | Token hợp lệ. | mat_khau_moi="Abc123!@" | 1. Submit. | **STATE**: Accept. **UI**: TC-104 success path. | Boundary | P0 |
| TC-PWD-128 | ERR-PWD-06 (E6) | MK xác nhận không khớp | Token hợp lệ. | mat_khau_moi="NewPass@1", mat_khau_xac_nhan="NewPass@2" | 1. Nhập 2 password khác nhau. 2. Submit. | **STATE**: FE/BE validate match. **UI**: Inline ERROR "Mật khẩu xác nhận không khớp" (srs-fr-10:1295). **PERSIST**: — | Negative | P0 |
| TC-PWD-129 | A4 token random hợp lệ nhưng không tồn tại trong DB | Token random fake — reject | Tester. | URL `/reset-password?token=randomfake12345` | 1. Mở URL fake token. | **STATE**: BE search `WHERE token_reset_mk='randomfake12345'` → 0 row. **UI**: ERROR ERR-PWD-03 hoặc ERR-PWD-04 (cùng nhóm "link không hợp lệ") hoặc redirect login với toast. **PERSIST**: — | Negative | P1 |
| TC-PWD-130 | A4 form email format | Email sai format RFC | Tester. | email="not-an-email" | 1. Form "Quên mật khẩu". 2. Nhập email sai. 3. Submit. | **STATE**: FE validate (srs-fr-10:1262). **UI**: Inline ERROR "Email không hợp lệ". | Negative | P0 |

---

## C. SECURITY & EDGE — TOKEN + RATE LIMIT + TRIGGER ENTITY

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước | Kết quả mong đợi | Type | Priority |
|----|---------|---------------|----------------|-----------|----------|------------------|------|----------|
| TC-PWD-140 | A4 token vĩnh viễn vs 30 phút (verify) | Verify token CHO_KICH_HOAT vĩnh viễn (srs-fr-10:1273) — chờ 31 phút vẫn dùng được | TK tvv_long_wait CHO_KICH_HOAT có vai_tro=TVV. Tester chờ 31 phút sau khi nhận mail. | — | 1. Tester nhận mail kích hoạt TVV. 2. Đợi 31 phút (hoặc time-travel mock). 3. Click link. 4. Đặt MK. | **STATE**: Token KHÔNG có `token_het_han` hoặc rất xa. BE accept dù trên 30 phút. **UI**: Form đặt MK OK. **PERSIST**: SM-T4 thực hiện. (Note: nếu test env không support wait, defer Phase B với note manual.) | Edge | P1 |
| TC-PWD-141 | A4 token reset 30 phút HOAT_DONG (verify time bound) | Token HOAT_DONG đúng 30 phút biên — VALID hoặc REJECT? | TK HOAT_DONG, link reset cách đây CHÍNH XÁC 30 phút. | — | 1. Click link đúng 30 phút sau request. | **STATE**: BE comparator `token_het_han <= NOW` (≤ thì hết, > thì còn). Boundary off-by-one. **UI**: Verify behavior — ngưỡng 1 giây. SPEC-CLARIFY-TKPQ-27. | Boundary | P1 |
| TC-PWD-142 | A4 trigger SM-TVV (verify side-effect) | Sau TC-102 (kích hoạt TVV) — verify TU_VAN_VIEN.trang_thai='HOAT_DONG' qua module CG/TVV | TK tvv_test_new đã activate qua TC-102. | — | 1. `qtht_01` login. 2. Module CG/TVV (FR-04). 3. Tìm tvv_test_new. 4. Quan sát trạng thái. | **STATE**: TU_VAN_VIEN.trang_thai='HOAT_DONG' (srs-fr-10:1303). **UI**: Module CG/TVV bảng có tvv_test_new badge "Hoạt động". **PERSIST**: tvv_test_new xuất hiện trong UC59 phân công vụ việc. | Happy | P0 |
| TC-PWD-143 | A4 trigger SM-NHT (verify side-effect) | Tương tự TC-142 cho NHT | nht_test_new activated qua TC-103. | — | 1. Module DM NHT. 2. Tìm nht_test_new. | **STATE**: NGUOI_HO_TRO.trang_thai='HOAT_DONG'. **UI**: Module có nht_test_new badge "Hoạt động". **PERSIST**: Xuất hiện trong UC59. | Happy | P0 |
| TC-PWD-144 | SPEC-CLARIFY-TKPQ-08 rate limit | Spam request "Quên MK" 10 lần liên tiếp — verify rate-limit/debounce | Tester chưa login. | email=`qtht_01@example.com` | 1. Submit form 10 lần liên tiếp trong 30s. | **STATE**: SRS không nói rate-limit (SPEC-CLARIFY-TKPQ-08). Behavior: (a) Accept tất cả → 10 mail; (b) Rate-limit cụ thể (vd 1 mail/5 phút); (c) Debounce silent. **UI**: Verify thực tế. **PERSIST**: MailHog có ≥ 1, ≤ 10 mail. | Edge | P2 |
| TC-PWD-145 | A4 token reuse cross-account | Token của TK A — sửa URL inject id của TK B | Token reset của user A. | URL inject `?token=A_token&user_id=B_id` | 1. Tester có token reset cho A. 2. Modify URL/payload thay user_id=B (nếu có). 3. Submit MK mới. | **STATE**: BE check token thuộc về tài khoản nào → chỉ cho phép reset MK của TK đó. **UI**: ERROR "Token không hợp lệ" hoặc reset MK A (KHÔNG B). **PERSIST**: B.mat_khau_hash KHÔNG đổi. | Negative | P0 |
| TC-PWD-146 | A4 BR-EC-13 sanitize email | Email có XSS payload | Tester. | email="<script>alert('XSS')</script>@x.com" | 1. Submit. | **STATE**: BE validate email format → reject (TC-130). KHÔNG render script. **UI**: Toast "Email không hợp lệ". | Negative | P0 |
| TC-PWD-147 | A4 form access with active session | User đang HOAT_DONG đã login mà click "Quên mật khẩu" — behavior? | qtht_01 đã login. | — | 1. Mở `/login` trong tab mới (hoặc click link "Quên mật khẩu" từ link bookmark). 2. Submit email qtht_01. | **STATE**: BE accept request. Mail vẫn được gửi (SRS không restrict user đã login). **UI**: Mail đến. User có thể đặt MK mới ngay. **PERSIST**: Session cũ có invalidate khi đổi MK không? SPEC-CLARIFY-TKPQ-28. | Edge | P1 |
| TC-PWD-148 | FR-VIII-26 step 14 audit | AUDIT_LOG ghi đầy đủ action='PASSWORD_RESET' / 'ACCOUNT_ACTIVATE' | qtht_01. Sau TC-104 + TC-102. | — | 1. Module SCR-VIII-10. 2. Filter Module=Quản trị, Hành động=Sửa hoặc custom. 3. Tìm 2 entry. | **STATE**: AUDIT_LOG có 2 entry: 1 cho TC-104 PASSWORD_RESET, 1 cho TC-102 ACCOUNT_ACTIVATE (srs-fr-10:1284). **UI**: Bảng có 2 dòng. KHÔNG ghi raw password trong chi_tiet (security). | Happy | P1 |
| TC-PWD-149 | A6 fill — link mail format verify | Verify link trong mail có format đúng `{base_url}/reset-password?token={random}` | qtht_01 yêu cầu reset. | — | 1. Submit form. 2. Mở MailHog. 3. Inspect HTML mail. | **STATE**: Mail có anchor `<a href="https://app.htpldn.gov.vn/reset-password?token=abc123def456...">Đặt mật khẩu mới</a>`. **UI**: Mail rendered. Link click → form đặt MK. **PERSIST**: Token chứa ≥ 32 ký tự random. | Happy | P1 |
| TC-PWD-150 | A6 fill — token expired auto cleanup | Token hết hạn được auto cleanup khỏi DB sau N ngày | TK có token hết hạn 1 tuần trước. | — | 1. Verify thông qua hành vi: (a) Click link cũ → ERR-PWD-03; (b) Backend cron cleanup expired tokens (SRS không nói rõ). | **STATE**: SPEC-CLARIFY-TKPQ-29 — có cleanup không? **UI**: KHÔNG verifable qua UI direct. Test qua hành vi reject. | Edge | P2 |
| TC-PWD-151 | BR-EC-13 boundary (Codex R2 fill) | Email input 200 ký tự — boundary max | Tester chưa login. | email = "a"×190 + "@x.com" (≈ 197 chars) | 1. Form "Quên mật khẩu". 2. Paste email 197 chars. 3. Submit. | **STATE**: BR-EC-13 (srs-v3.1.md §B BR-EC-13) max 200 ký tự + sanitize. BE accept (≤ 200). FE/BE: format check RFC 5322 + length validate. **UI**: Toast trung tính ERR-PWD-01 (vì email không tồn tại) HOẶC nếu FE strict format reject local-part 190 chars (RFC 5322 max 64 local-part) → ERROR "Email không hợp lệ". KHÔNG crash. **PERSIST**: — | Boundary | P1 |
| TC-PWD-152 | BR-EC-13 boundary (Codex R2 fill) | Email input 201 ký tự — boundary over | Tester. | email = "a"×195 + "@x.com" (201 chars) | 1. Submit email 201 chars. | **STATE**: BR-EC-13 reject (> 200). **UI**: Inline ERROR "Email vượt quá 200 ký tự" hoặc tương đương. (Note: FE thường truncate input field max length 200.) | Boundary | P2 |

---

## Tổng số TC: 29 (6 Happy + 11 Negative + 12 Edge/Security) — A3 base 18 + A4 merged 7 + A6 fill 2 + Codex R2 +2 BR-EC-13 boundary

**Priority**: P0=12 / P1=11 / P2=6

**Coverage (sau Codex R2):**
- BR: BR-DATA-05 (TC148 audit), BR-EC-13 ✅ (TC146 sanitize email + Codex R2 NEW TC151 boundary 200 + TC152 over 201), SM-TAIKHOAN T2/T3/T4 (TC102/103/105/106)
- AC SRS (4 AC): AC1 ✅ (TC102 TVV), AC2 ✅ (TC103 NHT), AC3 ✅ (TC101 user HOAT_DONG), AC4 ✅ (TC120 enumerate protection)
- Error codes (6): ERR-PWD-01..06 ✅ (TC120-128)
- SM-TAIKHOAN transitions: T2 ✅ (TC105 v3.1 backward), T4 ✅ (TC102/103), giữ HOAT_DONG ✅ (TC106)
- Trigger SM-TVV / SM-NHT: ✅ (TC102, 103, 142, 143)
- Token lifecycle: vĩnh viễn vs 30 phút ✅ (TC140-141), reuse + cross-account ✅ (TC124, 145), expired ✅ (TC123, 150)
- A4 merged 2026-05-08: TC129-130, TC140-148 (token edge, sanitize, trigger verify, audit, security)
- A6 fill 2026-05-08: TC149 (link format), TC150 (cleanup)
- SPEC-CLARIFY: TKPQ-04 (T2 vs T4 condition), TKPQ-08 (rate limit), TKPQ-09 (T12 vs token vĩnh viễn conflict), TKPQ-27 (boundary 30 phút), TKPQ-28 (session cũ khi đổi MK?), TKPQ-29 (token cleanup cron)

---

## D. Note về A7 — UI vs API

> TC-PWD-129 + TC-PWD-145 dùng modify URL + devtools — VALID UI bridge.
> TC-PWD-101 + TC-PWD-148 + TC-PWD-149 verify mail qua MailHog UI (`http://103.172.236.130:8025`) — KHÔNG curl thuần.
> TC-PWD-142 + TC-PWD-143 verify trigger entity qua module thực tế (CG/TVV / NHT) — UI bridge.
> TC-PWD-150 (cleanup) chỉ test được qua hành vi reject (TC-123 cùng pattern). KHÔNG verify DB direct.
> TC-PWD-140 (vĩnh viễn) + TC-PWD-141 (30 phút boundary) cần wait time hoặc time-travel — Phase B deferral nếu env không support, log Gap.
