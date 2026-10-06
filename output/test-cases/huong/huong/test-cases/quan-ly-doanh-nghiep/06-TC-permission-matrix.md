# Test Cases — Permission Matrix DN (Cross-FR-V.III BR-AUTH-01/08/EMAIL-01/USERNAME-01 + IDOR + AUDIT_LOG)

> **SRS Ref**: BR-AUTH-01 (xác thực + TOTP 2FA), BR-AUTH-08 (đơn vị 2 tầng TW → {BN, ĐP} ngang cấp), BR-AUTH-EMAIL-01 (2 email DN), BR-AUTH-USERNAME-01 (DN.username = MST), BR-DATA-05 (AUDIT_LOG immutable), Permission Matrix `srs-v3.5:1259-1289`
> **Nguồn**: NotebookLM `4dd0675e-a4fa-4ea6-80ae-48e76b3fa264` + LOCAL `srs-v3.5.md:5317-5318` (BR text)
> **Ngày tạo**: 2026-05-09

---

## A. UI FIELD VERIFICATION

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|---------|---------------|----------------|-----------|--------------------|-------------------|------|
| TC-DN-PERM-UI-01 | BR-AUTH-01 + Sidebar visibility per role | Verify sidebar menu DN visibility per role | 8 role test | — | 1. Login 8 role tuần tự<br>2. Verify sidebar Doanh nghiệp | **qtht_01**: ✅ Doanh nghiệp (R toàn cục)<br>**cb_nv_tw_01/bn_01/dp_01**: ✅ Doanh nghiệp (CRUD scope)<br>**cb_pd_tw_01/bn_01/dp_01**: ✅ Doanh nghiệp (chỉ R*, KHÔNG nút Edit/Delete)<br>**nht_01**: ❌ KHÔNG có sidebar Doanh nghiệp (Permission Matrix DN row "—")<br>**tvv_01/cg_01**: ❌ KHÔNG có sidebar CMS — chỉ chuyên trang xem hồ sơ TVV của mình<br>**dn_01**: ❌ KHÔNG truy cập CMS — chuyên trang riêng (Cổng PLQG) | Happy 🔴 |

## B. BR-AUTH-08 — Phân quyền dữ liệu cây 2 tầng (Thay đổi 5 srs-fr-10)

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|---------|---------------|----------------|-----------|--------------------|-------------------|------|
| TC-DN-PERM-001 | BR-AUTH-08 / TW ngoại lệ | TW xem được toàn bộ DN | cb_nv_tw_01, mixed data TW/BN/HN/HP | — | 1. Login cb_nv_tw_01<br>2. Mở SCR-V.III-01 | TW thấy toàn bộ DN cả 3 cấp (READ ngoại lệ TW per BR-AUTH-08); CRUD chỉ trên DN do TW tạo | Happy 🔴 |
| TC-DN-PERM-002 | BR-AUTH-08 / BN ngang cấp HN | cb_nv_bn_01 (Bộ TP) KHÔNG xem được DN-HN | cb_nv_bn_01 | — | 1. Login<br>2. Cố search DN-HN | Network response chỉ DN thuộc BN; tampered URL `/doanh-nghiep/DN-HN-001` → 403 | Negative 🔴 |
| TC-DN-PERM-003 | BR-AUTH-08 / ĐP ngang cấp | cb_nv_dp_HN_01 KHÔNG xem được DN-HP (cùng cấp khác đơn vị) | cb_nv_dp_HN_01, DN-HP-001 | — | 1. Direct URL `/doanh-nghiep/DN-HP-001` | API 403; UI redirect hoặc empty list | Negative 🔴 |
| TC-DN-PERM-004 | BR-AUTH-08 / IDOR PUT cross-tenant | IDOR: cb_nv_dp_HN_01 cố sửa DN-HP-001 qua DevTools | cb_nv_dp_HN_01 | — | 1. DevTools `PUT /api/v1/doanh-nghieps/{HP-001-id}` body | API 403 ERR-AUTH-08 (NGUYÊN VĂN); AUDIT_LOG ghi attempt; KHÔNG cập nhật | Negative 🔴 |
| TC-DN-PERM-005 | BR-AUTH-08 / IDOR DELETE cross-tenant | IDOR: cố DELETE DN cross-tenant | cb_nv_dp_HN_01 | — | 1. DevTools `DELETE /api/v1/doanh-nghieps/{HP-001-id}` | API 403; KHÔNG soft-delete; AUDIT_LOG ghi attempt | Negative 🔴 |
| TC-DN-PERM-006 | BR-AUTH-08 / Filter scope auto | cb_nv_dp_HN_01 filter Đơn vị → auto-set HN, không sửa được | cb_nv_dp_HN_01 | — | 1. Mở filter tinh_thanh<br>2. Verify | Filter tinh_thanh disabled hoặc auto-set "Hà Nội"; KHÔNG cho chọn HP/BN khác (BR-AUTH-08 enforce) | Happy 🟡 |
| TC-DN-PERM-007 | BR-AUTH-08 / TW xuyên scope khi Edit | cb_nv_tw_01 Edit DN-HN-001 (do CB NV ĐP HN tạo) | cb_nv_tw_01, DN-HN-001 | — | 1. Login TW<br>2. Mở Edit DN-HN-001 | Read PASS (TW ngoại lệ); Edit theo BR scope tạo (TW có thể edit nếu policy cho phép — SPEC-CLARIFY-DN-19) | Happy 🟡 |
| TC-DN-PERM-008 | A6-fill / DN role redirect khi truy cập CMS | dn_01 cố truy cập CMS DN list → redirect chuyên trang | dn_01 (chuyên trang) | URL `http://103.172.236.130:3000/doanh-nghiep/danh-sach` | 1. Login dn_01<br>2. Direct URL CMS | Per Permission Matrix dòng srs-v3.5:1262 — DN không truy cập CMS; redirect về chuyên trang DN (Cổng PLQG hoặc trang profile DN); SPEC-CLARIFY-DN-45 nếu hệ thống cho login DN vào CMS | Negative 🔴 |

## C. BR-AUTH-01 — Xác thực + TOTP 2FA

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|---------|---------------|----------------|-----------|--------------------|-------------------|------|
| TC-DN-PERM-101 | BR-AUTH-01 / Unauthorized | Truy cập SCR-V.III-01 không login → redirect login | — | URL `/doanh-nghiep/danh-sach` | 1. Direct URL không session | Redirect `/login`; URL gốc lưu callback | Negative 🔴 |
| TC-DN-PERM-102 | BR-AUTH-01 / TOTP 2FA happy | Login Tier 1 + OTP 666666 (env test) | qtht_01 | OTP: 666666 | 1. Submit username/password<br>2. OTP screen<br>3. Nhập 666666 | Login PASS; redirect home | Happy 🟡 |
| TC-DN-PERM-103 | BR-AUTH-01 / OTP wrong | OTP sai → reject | qtht_01 | OTP: 000000 | 1. Submit OTP wrong | UI inline "OTP không đúng"; KHÔNG login | Negative 🟡 |
| TC-DN-PERM-104 | BR-AUTH-01 / Session timeout | Session 30 phút expire → redirect login | qtht_01 | session > 30 min | 1. Đăng nhập<br>2. Đợi 31 phút<br>3. Click Edit DN | API 401 "Phiên đăng nhập hết hạn"; redirect login + lưu callback URL | Edge 🟡 |

## D. BR-AUTH-EMAIL-01 — 2 email DN độc lập

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|---------|---------------|----------------|-----------|--------------------|-------------------|------|
| TC-DN-PERM-201 | BR-AUTH-EMAIL-01 / Đăng ký 2 cột cùng giá trị | DN tự đăng ký FR-VIII-22 → 2 cột cùng giá trị | DN tự đăng ký mới với email "moi@dn.com" | — | 1. Cross-FR-VIII-22 đăng ký<br>2. Verify 2 cột | TAI_KHOAN.email = "moi@dn.com" + DOANH_NGHIEP.email = "moi@dn.com" (cùng giá trị); UI hiển thị 1 ô email khi đăng ký | Happy 🔴 |
| TC-DN-PERM-202 | BR-AUTH-EMAIL-01 / Edit DN.email không cần OTP | Sửa DOANH_NGHIEP.email không cần OTP confirm | cb_nv_tw_01, DN-TW-001 (đã DN tự đăng ký) | DOANH_NGHIEP.email mới: "ketoan@svc.com" | 1. Mở Edit DN-001<br>2. Đổi email<br>3. Submit | PUT thành công không cần OTP; DN.email = "ketoan@svc.com"; TAI_KHOAN.email KHÔNG đổi | Happy 🔴 |
| TC-DN-PERM-203 | BR-AUTH-EMAIL-01 / DN.email KHÔNG UNIQUE | DN.email cho phép trùng nhiều DN | cb_nv_tw_01, DN-001 email "ketoan@svc.com", DN-002 cùng email | DN-002.email: "ketoan@svc.com" | 1. Edit DN-002.email = "ketoan@svc.com"<br>2. Submit | PASS — KHÔNG báo lỗi UNIQUE; 2 DN cùng email PASS (per BR-AUTH-EMAIL-01 srs-v3.5:5318) | Happy 🔴 |
| TC-DN-PERM-204 | BR-AUTH-EMAIL-01 / TAI_KHOAN.email UNIQUE | Đổi TAI_KHOAN.email không trùng DN khác | cb_nv_tw_01 | — | 1. Đổi TAI_KHOAN.email cá nhân (cross-FR-VIII chức năng "Đổi email TK") | UNIQUE constraint enforce; trùng DN khác → ERR | Negative 🟡 |

## E. BR-AUTH-USERNAME-01 — DN.username = MST

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|---------|---------------|----------------|-----------|--------------------|-------------------|------|
| TC-DN-PERM-301 | BR-AUTH-USERNAME-01 / DN username = MST | DN.username auto = ma_so_thue (10 chữ số) | DN tự đăng ký mới với MST 0123456789 | — | 1. Cross-FR-VIII-22 đăng ký<br>2. Verify TAI_KHOAN.username | TAI_KHOAN.username = "0123456789" (= MST); regex `^[a-z0-9_]{4,50}$` PASS | Happy 🔴 |
| TC-DN-PERM-302 | BR-AUTH-USERNAME-01 / Username readonly sau đăng ký | Username KHÔNG sửa được sau đăng ký | dn_01 | — | 1. Login dn_01<br>2. Profile<br>3. Verify username | Field readonly; nếu DevTools tamper PUT body → backend ignore | Happy 🟡 |
| TC-DN-PERM-303 | BR-AUTH-USERNAME-01 / MST đổi không đổi username | Đổi DN.MST không đổi TAI_KHOAN.username | cb_nv_tw_01, DN-001 MST cũ "0123456789", username TK = "0123456789" | DN-001.MST mới: "9876543210" | 1. Edit DN.MST<br>2. Submit<br>3. Verify TAI_KHOAN.username | DN.MST = "9876543210"; TAI_KHOAN.username vẫn giữ "0123456789" (không đồng bộ ngược); SPEC-CLARIFY-DN-20 nếu BA muốn sync | Happy 🟡 |
| TC-DN-PERM-304 | Codex P0-002 / MST 9 digits invalid | DN tự đăng ký với MST 9 chữ số → reject | DN tự đăng ký FR-VIII-22 | ma_so_thue: "012345678" (9 digit) | 1. Submit form đăng ký | API/UI reject — vi phạm BR-AUTH-USERNAME-01 (username regex `^[a-z0-9_]{4,50}$` PASS nhưng MST format TT 105/2020/TT-BTC Điều 5 yêu cầu 10 chữ số); inline error "Mã số thuế phải đủ 10 chữ số"; SPEC-CLARIFY-DN-25 nếu SRS không có ERR code | Negative 🔴 |
| TC-DN-PERM-305 | Codex P0-002 / MST 11 digits invalid | DN tự đăng ký với MST 11 chữ số → reject | DN tự đăng ký FR-VIII-22 | ma_so_thue: "01234567890" (11 digit) | 1. Submit | API/UI reject — vi phạm format TT 105/2020 (10 chữ số DN tự đăng ký, 13 chữ số chỉ chi nhánh không tự đăng ký per srs-v3.5:5317); inline error "Mã số thuế không hợp lệ" | Negative 🔴 |
| TC-DN-PERM-306 | Codex P0-002 / MST non-digit invalid | DN tự đăng ký với MST có chữ cái → reject | DN tự đăng ký FR-VIII-22 | ma_so_thue: "ABC1234567" | 1. Submit | API/UI reject — không match regex `^\d{10}$`; inline error "Mã số thuế chỉ chứa chữ số"; SPEC-CLARIFY-DN-25 ERR code chính thức | Negative 🔴 |

## F. AUDIT_LOG — BR-DATA-05 immutable

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|---------|---------------|----------------|-----------|--------------------|-------------------|------|
| TC-DN-PERM-401 | BR-DATA-05 / AUDIT_LOG ghi UPDATE | Edit DN → AUDIT_LOG ghi 1 row UPDATE | cb_nv_tw_01, DN-TW-001 | sửa ghi_chu | 1. Edit + Save<br>2. Cross-FR-VIII-28 mở Nhật ký HT filter entity=DOANH_NGHIEP | AUDIT_LOG có row: entity=DOANH_NGHIEP, entity_id={DN-001-id}, hanh_dong=UPDATE, nguoi_thuc_hien_id=cb_nv_tw_01.id, gia_tri_cu=old, gia_tri_moi=new | Happy 🔴 |
| TC-DN-PERM-402 | BR-DATA-05 / AUDIT_LOG ghi DELETE | Delete DN → AUDIT_LOG ghi DELETE | cb_nv_tw_01, DN-TW-099 | — | 1. Delete<br>2. Cross-FR-VIII-28 verify | AUDIT_LOG row hanh_dong=DELETE | Happy 🟡 |
| TC-DN-PERM-403 | BR-DATA-05 / AUDIT_LOG immutable (A7 SỬA UI bridge security test) | AUDIT_LOG không sửa/xóa được — verify backend reject tampered request | qtht_01 | MCP `evaluate_script` chạy fetch tampered từ session đang login | 1. Login qtht_01 qua UI<br>2. Mở UI Nhật ký HT — verify KHÔNG có nút Edit/Delete trên row AUDIT<br>3. MCP `evaluate_script` `fetch('/api/v1/audit-logs/{id}', {method:'PUT', body: ...})`<br>4. Verify response | UI: KHÔNG có nút Edit/Delete (immutable design)<br>API: 403 hoặc 405 Method Not Allowed; nếu 200 → log bug Critical (BR-DATA-05 violated) | Negative 🔴 |
| TC-DN-PERM-404 | BR-DATA-05 / AUDIT_LOG ghi attempt 403 | Cross-tenant 403 vẫn ghi AUDIT_LOG | cb_nv_dp_HN_01 cố Edit DN-HP-001 | — | 1. Cross-tenant edit<br>2. Verify AUDIT_LOG | AUDIT_LOG có row hanh_dong=UPDATE_ATTEMPT_DENIED hoặc tương đương; ghi user_id + IP; SPEC-CLARIFY-DN-21 nếu SRS không define hành vi log denied | Edge 🟡 |

## G. CROSS-MODULE LINK INTEGRITY

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|---------|---------------|----------------|-----------|--------------------|-------------------|------|
| TC-DN-PERM-501 | Cross-FR-05 / FK protect | DELETE DN có VV → reject ERR-DN-03 (đã cover ở 01) | cb_nv_tw_01, DN-001 có VV active | — | 1. Click Xóa | ERR-DN-03 hiển thị; FK integrity preserved | Negative 🟡 (cross-ref TC-DN-102) |
| TC-DN-PERM-502 | Cross-FR-X.1-04 / NHT scope HSPL | nht_01 chỉ Read+Update HSPL của DN trong VV được phân công | nht_01, NHT-001 phân công VV-001 thuộc DN-001 | — | 1. nht_01 mở chuyên trang<br>2. Mở HSPL của DN-001 | HSPL của DN-001 hiển thị (read+update); HSPL DN khác → 403 (per FR-X.1-04 AC line 669-671) | Happy 🟡 |
| TC-DN-PERM-503 | Cross-FR-X.1-04 / NHT KHÔNG Create+Delete | nht_01 không thể Create hoặc Delete HSPL | nht_01 | — | 1. nht_01 mở HSPL<br>2. Tìm nút Create/Delete | KHÔNG có nút Create + Delete (Permission Matrix HSPL row: NHT = CRU* nhưng AC FR-X.1-04 line 671 NGUYÊN VĂN "Không cho NHT tạo mới hoặc xóa hồ sơ — chỉ R + U") — SPEC-CLARIFY-DN-22 mâu thuẫn 2 nguồn | Negative 🟡 |

---

## H. EDGE bổ sung (A4 inline merge — 6 edge)

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|---------|---------------|----------------|-----------|--------------------|-------------------|------|
| TC-DN-PERM-601 | EDGE-A4-ff / Session expire giữa edit | Session timeout giữa khi đang edit DN form | cb_nv_tw_01, mở edit + đợi session expire | — | 1. Mở edit DN-001<br>2. Đợi 31 phút<br>3. Submit | API 401 "Phiên đăng nhập hết hạn"; UI redirect login + lưu draft (sessionStorage); sau login → restore form data; SPEC-CLARIFY-DN-39 nếu SRS không có draft restore | Edge 🟡 |
| TC-DN-PERM-602 | EDGE-A4-gg / OTP brute force lockout | Sai OTP nhiều lần → lockout | dn_01 | OTP wrong x 5 | 1. Submit OTP wrong 5 lần | API 429 "Quá nhiều lần thử, vui lòng đợi N phút"; KHÔNG cho thêm attempt; SPEC-CLARIFY-DN-40 nếu SRS không có max attempt | Edge 🟡 |
| TC-DN-PERM-603 | EDGE-A4-hh / TAI_KHOAN.email change conflict (Codex P0-001 fix) | Đổi TAI_KHOAN.email trùng email khác user → UNIQUE violation | dn_01 | TAI_KHOAN.email mới = qtht_01.email | 1. Đổi email TK qua chức năng "Đổi email TK" (cross-FR-VIII)<br>2. Submit | UNIQUE constraint violation (TAI_KHOAN.email UNIQUE per srs-v3.5:1990); UI hiển thị toast/inline error báo trùng email — **NGUYÊN VĂN text TBD ở module FR-VIII** (SRS srs-fr-07/srs-v3.5 không có ERR code text cho luồng đổi TK email); SPEC-CLARIFY-DN-41 — confirm với BA: error message khi đổi TAI_KHOAN.email trùng user khác | Negative 🟡 |
| TC-DN-PERM-604 | EDGE-A4-ii / DN MST 13 chữ số chi nhánh | MST chi nhánh 13 chữ số (TT 105/2020) | DN tự đăng ký với MST 13 chữ số | ma_so_thue: "0123456789-001" | 1. Cross-FR-VIII-22 đăng ký | BR-AUTH-USERNAME-01 ghi "chi nhánh có MST 13 chữ số không tự đăng ký" → block; SPEC-CLARIFY-DN-42 confirm UI | Edge 🟡 |
| TC-DN-PERM-605 | EDGE-A4-jj / IDOR via API direct | IDOR direct API không qua UI | cb_nv_dp_HN_01 | DevTools fetch GET cross-tenant DN-HP-001 | 1. Capture token<br>2. fetch GET trực tiếp body | API 403 ERR-AUTH-08 (NGUYÊN VĂN); AUDIT_LOG ghi attempt với IP + user_id; KHÔNG leak data | Edge 🔴 |
| TC-DN-PERM-606 | EDGE-A4-kk / DN.email 100 trùng | 100 DN cùng email — verify NOT UNIQUE | qtht_01, 100 DN với DN.email="ketoan@svc.com" | — | 1. Search filter email (nếu có) | List 100 DN cùng email; KHÔNG báo lỗi UNIQUE; verify BR-AUTH-EMAIL-01 NOT UNIQUE | Edge 🟡 |

---

**Tổng số TC**: 33 (1 UI + 8 BR-AUTH-08 + 4 BR-AUTH-01 + 4 EMAIL-01 + 6 USERNAME-01 + 4 AUDIT + 3 Cross-module + 6 Edge A4 — sau A6 +1 TC-DN-PERM-008 + Codex +3 TC-DN-PERM-304/305/306 MST boundary)
