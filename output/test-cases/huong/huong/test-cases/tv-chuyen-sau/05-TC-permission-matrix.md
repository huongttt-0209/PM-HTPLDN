# Test Cases — Permission Matrix Cross-cutting FR-X.1 (BR-AUTH-01 / BR-AUTH-05 / BR-AUTH-08)

> **Module:** FR-12 — Quản lý Tư vấn pháp luật chuyên sâu
> **SRS Ref:** `input/srs-v3/srs-fr-12-tv-chuyen-sau-v3.1.md`
> **BR áp dụng:** BR-AUTH-01 (line 1525-1529) / BR-AUTH-05 (line 1489 + AC line 198) / BR-AUTH-08 (line 1531-1535)
> **Permission Matrix:** Overview file 00-test-plan-overview.md §2.4
> **Pattern reference:** `output/test-cases/bieu-mau/07-TC-permission-matrix.md` (FR-09)
> **Phase:** A3 (BMAD test-design) — 2026-05-06
> **Scope cross-FR-X.1:** TU_VAN_CHUYEN_SAU + HO_SO_PHAP_LY_DN + TU_LIEU_PHAP_LY_VV + DANH_GIA_CHAT_LUONG_TV + PHIEN_TU_VAN

---

## Section A: UI Verify role-based action visibility

### TC-PERM-001 — UI Verify role-based visibility action button trên SCR-X1-01 / SCR-X1-02

- **Type:** UI Verify
- **Priority:** P0
- **Tài khoản:** Loop 4 role: cb_nv_tw_01 / cb_pd_tw_01 / cg_01 / qtht_01
- **Preconditions:**
  - Seed 1 TVCS trạng thái TIEP_NHAN (do cb_nv_tw_01 tạo, scope TW), 1 TVCS DA_DUYET, 1 TVCS CHO_PHE_DUYET (cùng cấp TW), 1 TVCS PHAN_CONG cho cg_01.
  - Mỗi user đăng nhập riêng phiên test.
- **Steps:**
  1. Login `cb_nv_tw_01` → SCR-X1-01 → quan sát toolbar + cột "Hành động". Click TVCS TIEP_NHAN → SCR-X1-02 → quan sát action-bar.
  2. Login `cb_pd_tw_01` → mở TVCS CHO_PHE_DUYET trên SCR-X1-02 → quan sát action-bar.
  3. Login `cg_01` → mở TVCS PHAN_CONG (đã được phân công) trên SCR-X1-02 → quan sát action-bar.
  4. Login `qtht_01` → SCR-X1-01 → quan sát toolbar + click 1 TVCS bất kỳ.
- **Expected:**
  - **cb_nv_tw_01 (CB_NV CRUD\*):** Toolbar hiển thị `[+ Thêm yêu cầu TV]` + `[Xuất Excel]`. Cột Hành động có Xem/Sửa/Phân công CG/Hủy. Detail action-bar TIEP_NHAN: `[Hủy] [Lưu] [Phân công CG →]`.
  - **cb_pd_tw_01 (CB_PD RU\*):** Toolbar KHÔNG có `[+ Thêm yêu cầu TV]` (CB_PD không có C). Cột Hành động chỉ có Xem. Detail action-bar CHO_PHE_DUYET: `[Phê duyệt]` + `[Từ chối]` (BR-AUTH-05 cùng cấp TW).
  - **cg_01 (CG R\* được PC):** Toolbar KHÔNG có `[+ Thêm yêu cầu TV]`. Detail action-bar PHAN_CONG: `[Chấp nhận]` + `[Từ chối]` (CG được phân công).
  - **qtht_01 (R toàn bộ):** Read-only — toolbar không có nút thêm/sửa, action-bar tất cả nút disabled hoặc ẩn (chỉ Xem).
- **SRS ref:** Action-bar conditional theo trạng thái + role overview §2.5 (line 213-220) + Permission Matrix §2.4 line 171.
- **Notes:** Active bug BUG-FR12-001 — action-bar empty trên Detail. Phase B verify, A3 viết theo SRS spec đầy đủ.

---

## Section B: BR-AUTH-01 — Login & Authentication Tier 1 / Tier 2

### TC-PERM-002 — BR-AUTH-01 Tier 1: CB nội bộ login U/P + TOTP, anonymous user redirect /login

- **Type:** Negative + Happy
- **Priority:** P0
- **Tài khoản:** cb_nv_tw_01 (Tier 1)
- **Preconditions:** Logout / clear cookie. Hệ thống env LuatDN5 fix cứng OTP=666666.
- **Steps:**
  1. Mở browser ẩn danh, navigate `https://app/tv-chuyen-sau/danh-sach` không kèm session.
  2. Verify response.
  3. Tại trang `/login`, nhập username=`cb_nv_tw_01`, password đúng → Submit.
  4. Tại bước OTP, nhập `666666` → Submit.
  5. Verify post-login redirect.
- **Expected:**
  - Bước 1-2: HTTP 302 redirect → `/login` (BR-AUTH-01 "Mọi user phải xác thực trước khi truy cập"). KHÔNG render data SCR-X1-01.
  - Bước 3-4: Tier 1 flow — sau U/P prompt OTP qua email; nhập 666666 PASS.
  - Bước 5: Redirect về `/tv-chuyen-sau/danh-sach`, list render. AUDIT_LOG có entry `LOGIN` actor=cb_nv_tw_01 (BR-DATA-05).
- **SRS ref:** BR-AUTH-01 line 1525-1529 — "Tier 1 (nội bộ qua mạng kín) = Username/password + TOTP 2FA qua email".
- **Notes:** Env LuatDN5 không cần MailHog, OTP=666666 fix cứng (per memory). Tier 2 SSO VNeID test ở TC-PERM-003.

### TC-PERM-003 — BR-AUTH-01 Tier 2: DN không dùng route Tier 1; CG/TVV truy cập SCR-X1-02 sau SSO

- **Type:** Negative + Happy hybrid
- **Priority:** P1
- **Tài khoản:** dn_01 (Tier 2 — SSO VNeID OIDC, ngoài scope CMS), cg_01 (Tier 2 — sau SSO truy cập CMS để [Chấp nhận]/[Từ chối] TVCS phân công)
- **Preconditions:** Logout. Tier 1 login route giả định `/login` cho CB nội bộ. cg_01 đã có TVCS PHAN_CONG (`tvcs-pc-cg01`).
- **Steps:**
  1. Mở `/login` (Tier 1 form). Nhập username=`dn_01`, password đúng → Submit.
  2. Quan sát phản hồi.
  3. Mở `/login` Tier 1. Nhập username=`cg_01` → quan sát reject hay accept.
  4. Mở route SSO VNeID giả định `/login-vneid` hoặc nút "Đăng nhập bằng VNeID" trên trang public → flow OIDC cho cg_01.
  5. Sau khi cg_01 SSO thành công → navigate `/tv-chuyen-sau/chi-tiet/tvcs-pc-cg01` → quan sát action-bar.
- **Expected:**
  - **Bước 1-2 (DN qua Tier 1):** Hệ thống reject (DN thuộc Tier 2 không được login qua Tier 1 form). Message "Tài khoản này đăng nhập qua VNeID" hoặc redirect → SSO route. KHÔNG cấp session app nội bộ. DN sau khi auth qua VNeID có thể truy cập tính năng Cổng PLQG (FR-VIII-22 ngoài scope module này) — KHÔNG truy cập SCR-X1-01 CMS internal.
  - **Bước 3 (CG qua Tier 1):** Hệ thống reject — CG thuộc Tier 2 (BR-AUTH-01 line 1529 nguyên văn "áp cho tác nhân bên ngoài DN, TVV, CG, NHT"). Redirect SSO route HOẶC error "Đăng nhập qua VNeID".
  - **Bước 4-5 (CG qua SSO VNeID):** SSO success → cấp session. cg_01 ĐƯỢC truy cập SCR-X1-02 chi tiết TVCS phân công (theo Permission Matrix overview §2.4 line 171 `CG/TVV R* (CG được PC)` + SRS line 1136 quote nguyên văn "khi user là CG được phân công, hiện [Chấp nhận] / [Từ chối] trên thanh hành động"). Action-bar PHAN_CONG render `[Chấp nhận]` + `[Từ chối]`.
- **SRS ref:** BR-AUTH-01 line 1525-1529 (2-tier model + Tier 2 áp DN/TVV/CG/NHT) + line 164 (UC147 Processing — CG xác nhận: "Kiểm tra user là CG được phân công") + line 1136 (action-bar khi user là CG được phân công) + Permission Matrix overview §2.4 line 171 (CG R* TVCS được PC).
- **Notes:** SPEC-CLARIFY-TVCS-PERM-03 — SRS không quote rõ route SSO VNeID URL. Phase B verify URL thực tế trong env LuatDN5. **Sửa 2026-05-09 (codex review):** Original TC sai logic — CG/TVV vẫn truy cập SCR-X1-02 sau Tier 2 SSO để xác nhận/từ chối TVCS, KHÔNG phải cấm hoàn toàn. Tách thành 2 path: DN ngoài scope CMS / CG vào CMS qua SSO.

---

## Section C: BR-AUTH-05 — Phê duyệt cùng cấp

### TC-PERM-004 — BR-AUTH-05 Happy: CB_PD_TW phê duyệt TVCS cấp TW (cùng cấp)

- **Type:** Happy
- **Priority:** P0
- **Tài khoản:** cb_pd_tw_01
- **Preconditions:**
  - Seed 1 TVCS thuộc don_vi_id = TW, trạng thái CHO_PHE_DUYET (cb_nv_tw_01 đã trình từ HOAN_THANH).
- **Steps:**
  1. Login `cb_pd_tw_01` → SCR-X1-01, tab "Đang tư vấn" → tìm record CHO_PHE_DUYET.
  2. Click record → SCR-X1-02 → quan sát action-bar.
  3. Click `[Phê duyệt]` → confirm.
  4. Verify state.
- **Expected:**
  - Action-bar render `[Phê duyệt]` + `[Từ chối]`.
  - Sau confirm: TVCS chuyển CHO_PHE_DUYET → DA_DUYET (SM-TVCS transition #7 line 1489 "Cùng cấp đơn vị BR-AUTH-05").
  - TB DN gửi (qua FR-X.1-01 action), AUDIT_LOG ghi `PHE_DUYET` actor=cb_pd_tw_01 (BR-DATA-05).
  - Record di chuyển sang tab "Hoàn thành".
- **SRS ref:** BR-AUTH-05 SM-TVCS line 1489 "CHO_PHE_DUYET → DA_DUYET — Guard: Cùng cấp" + AC nhóm UC147 line 198 "phê duyệt cùng cấp đơn vị".
- **Notes:** Active bug BUG-FR12-001 chặn action-bar Phase B; A3 viết theo SRS đầy đủ.

### TC-PERM-005 — BR-AUTH-05 Negative: CB_PD_BN cố phê duyệt TVCS thuộc cấp TW (khác cấp)

- **Type:** Negative
- **Priority:** P0
- **Tài khoản:** cb_pd_bn_01
- **Preconditions:**
  - Seed 1 TVCS thuộc don_vi_id = TW, trạng thái CHO_PHE_DUYET (uuid = `tvcs-tw-cpd-001`).
- **Steps:**
  1. Login `cb_pd_bn_01` → SCR-X1-01 → kiểm tra danh sách (BR-AUTH-08 — không thấy TVCS TW).
  2. Direct URL `/tv-chuyen-sau/chi-tiet/tvcs-tw-cpd-001` (deeplink IDOR).
  3. Quan sát phản hồi + action-bar.
  4. Mock POST `/api/tvcs/tvcs-tw-cpd-001/phe-duyet` qua DevTools → quan sát.
- **Expected:**
  - Bước 1: KHÔNG hiển thị record TW trong list (BR-AUTH-08 multi-tenant — cb_pd_bn_01 chỉ thấy don_vi BN của mình).
  - Bước 2-3: HTTP 403 hoặc 404 "Không tìm thấy" / "Bạn không có quyền truy cập tài nguyên này". Action-bar `[Phê duyệt]` KHÔNG hiển thị.
  - Bước 4: Backend reject HTTP 403 với message "Chỉ phê duyệt cùng cấp" hoặc tương đương — không thực hiện transition. AUDIT_LOG ghi attempt failed.
- **SRS ref:** BR-AUTH-05 line 1489 "Guard: Cùng cấp đơn vị" + BR-AUTH-08 line 1531-1535 multi-tenant.
- **Notes:** SPEC-CLARIFY-TVCS-PERM-04 — SRS không quote nguyên văn message error code khi cross-cấp PD. Default test với assumption 403 + UI hide.

### TC-PERM-006 — BR-AUTH-05 Negative: CB_PD_DP cố phê duyệt TVCS thuộc cấp BN (khác cấp DP→BN)

- **Type:** Negative
- **Priority:** P1
- **Tài khoản:** cb_pd_dp_01 (cấp ĐP — AG)
- **Preconditions:**
  - Seed 1 TVCS thuộc don_vi_id = BN (BKH), trạng thái CHO_PHE_DUYET (uuid = `tvcs-bn-cpd-001`).
- **Steps:**
  1. Login `cb_pd_dp_01` → SCR-X1-01.
  2. Direct URL deeplink `/tv-chuyen-sau/chi-tiet/tvcs-bn-cpd-001`.
  3. Mock POST `/api/tvcs/tvcs-bn-cpd-001/phe-duyet`.
- **Expected:**
  - Bước 1: List không hiển thị TVCS thuộc BN (BR-AUTH-08).
  - Bước 2: 403/404. Nếu render thì action-bar `[Phê duyệt]` ẨN.
  - Bước 3: Backend reject HTTP 403. KHÔNG transition. Audit log ghi failed attempt.
- **SRS ref:** BR-AUTH-05 line 1489 "Cùng cấp đơn vị" — DP không phê duyệt cho BN.
- **Notes:** Cùng pattern TC-PERM-005, khác cấp khác hướng (DP→BN thay vì BN→TW).

---

## Section D: BR-AUTH-08 — Multi-tenant data isolation

### TC-PERM-007 — BR-AUTH-08 Cross-unit ngang cấp BN: cb_nv_bn_01 (BKH) KHÔNG thấy TVCS của cb_nv_bn_02 (BTC)

- **Type:** Negative
- **Priority:** P0
- **Tài khoản:** cb_nv_bn_01 (Bộ KH&ĐT) + cb_nv_bn_02 (Bộ Tài chính)
- **Preconditions:**
  - Seed 2 TVCS:
    - `tvcs-bkh-001` thuộc don_vi_id = BKH, do cb_nv_bn_01 tạo.
    - `tvcs-btc-001` thuộc don_vi_id = BTC, do cb_nv_bn_02 tạo.
- **Steps:**
  1. Login `cb_nv_bn_01` → SCR-X1-01 → quan sát danh sách.
  2. Direct URL `/tv-chuyen-sau/chi-tiet/tvcs-btc-001` (IDOR cross-unit).
  3. Mock PUT `/api/tvcs/tvcs-btc-001` payload sửa nội dung.
  4. Logout, login `cb_nv_bn_02` → SCR-X1-01.
- **Expected:**
  - Bước 1: List chỉ render `tvcs-bkh-001` (1 record). KHÔNG có `tvcs-btc-001` (BR-AUTH-08 filter `WHERE don_vi_id = BKH.id`).
  - Bước 2: HTTP 403/404. UI redirect SCR-X1-01 + toast error.
  - Bước 3: Backend reject 403. KHÔNG có UPDATE entry trong AUDIT_LOG.
  - Bước 4: cb_nv_bn_02 chỉ thấy `tvcs-btc-001`. Verify isolation 2 chiều.
- **SRS ref:** BR-AUTH-08 line 1531-1535 "Chính sách phân quyền dữ liệu áp dụng cho MỌI bảng có cột don_vi_id. Không có exception ngoại trừ QTHT."
- **Notes:** Permission Matrix overview §2.4 line 171 TU_VAN_CHUYEN_SAU CB_NV_BN = CRUD\* (scoped). Pattern same với TC-BM-PERM-007 sibling.

### TC-PERM-008 — BR-AUTH-08 Cross-unit ngang cấp ĐP: cb_nv_dp_01 (AG) KHÔNG thấy TVCS của cb_nv_dp_02 (BG) + IDOR HSPL

- **Type:** Negative
- **Priority:** P1
- **Tài khoản:** cb_nv_dp_01 (STP An Giang) + cb_nv_dp_02 (STP Bắc Giang)
- **Preconditions:**
  - Seed 1 TVCS `tvcs-ag-001` thuộc don_vi_id = STP-AG.
  - Seed 1 HSPL `hspl-ag-001` thuộc don_vi_id = STP-AG (DN địa chỉ AG).
  - Seed 1 TLPL `tlpl-ag-001` thuộc don_vi_id = STP-AG.
- **Steps:**
  1. Login `cb_nv_dp_02` (BG) → SCR-X1-01 → quan sát.
  2. Direct URL `/tv-chuyen-sau/chi-tiet/tvcs-ag-001` (IDOR).
  3. Direct URL `/doanh-nghiep/{dn-ag-id}/ho-so-phap-ly/hspl-ag-001` (IDOR HSPL cross-unit).
  4. Direct URL `/tu-lieu-phap-ly/tlpl-ag-001` (IDOR TLPL).
- **Expected:**
  - Bước 1: List rỗng hoặc không có record AG. cb_nv_dp_02 chỉ thấy don_vi STP-BG.
  - Bước 2-3-4: Cả 3 entity đều trả 403/404 (BR-AUTH-08 áp cho cả 3 bảng TU_VAN_CHUYEN_SAU + HO_SO_PHAP_LY_DN + TU_LIEU_PHAP_LY_VV — overview §2.4).
  - AUDIT_LOG ghi failed access attempts (BR-DATA-05).
- **SRS ref:** BR-AUTH-08 line 1531-1535 + Permission Matrix overview §2.4 (3 entity đều CRUD\* scoped cho CB_NV_DP).
- **Notes:** Cover IDOR cross-cutting cho 3 entity trong 1 TC.

---

## Section E: SPEC-CLARIFY — CG action button visibility + DANH_GIA tab

### TC-PERM-009 — CG được phân công vs CG ngoài: action button + tab Đánh giá CL visibility

- **Type:** UI Verify + Negative
- **Priority:** P1
- **Tài khoản:** cg_01 (được phân công) + cg_02 (KHÔNG được phân công)
- **Preconditions:**
  - Seed 1 TVCS `tvcs-pc-001` PHAN_CONG cho cg_01 (chuyen_gia_id = cg_01).
  - Seed 1 TVCS `tvcs-da-duyet-001` DA_DUYET (đã có ≥1 đánh giá DANH_GIA_CHAT_LUONG_TV) phân công cg_01.
- **Steps:**
  1. Login `cg_01` → SCR-X1-01 → mở `tvcs-pc-001` → quan sát action-bar.
  2. Mở `tvcs-da-duyet-001` → quan sát accordion "Đánh giá CL".
  3. Logout, login `cg_02` → SCR-X1-01 → quan sát có thấy `tvcs-pc-001` không.
  4. Direct URL `/tv-chuyen-sau/chi-tiet/tvcs-pc-001`.
  5. Mock POST `/api/tvcs/tvcs-pc-001/cg-chap-nhan` từ session cg_02.
- **Expected:**
  - Bước 1: cg_01 thấy `tvcs-pc-001`. Action-bar PHAN_CONG hiển thị `[Chấp nhận]` + `[Từ chối]` (CG được phân công — overview §2.5 line 215).
  - Bước 2: Accordion "Đánh giá CL" — assumption per **SPEC-CLARIFY-TVCS-PERM-01** = ẩn cho CG chính chủ (DANH_GIA permission CG=`—` overview §2.4 line 174). Phase B verify behavior thực tế.
  - Bước 3: cg_02 KHÔNG thấy `tvcs-pc-001` (R\* "CG được PC" — overview §2.4 line 171). List rỗng/không có record.
  - Bước 4: HTTP 403 hoặc render read-only KHÔNG có nút Chấp nhận/Từ chối.
  - Bước 5: Backend reject 403 — cg_02 không phải CG được phân công. AUDIT_LOG attempt failed.
- **SRS ref:** Permission Matrix overview §2.4 line 171 TU_VAN_CHUYEN_SAU "CG/TVV R\* (CG được PC)" + line 174 DANH_GIA "CG/TVV `—`" + SPEC-CLARIFY-TVCS-PERM-01.
- **Notes:** SPEC-CLARIFY-TVCS-PERM-01 ưu tiên BA respond — assumption tab Đánh giá ẨN cho CG chính chủ. Phase B-Verify document UI behavior thực tế.

---

## Section F: BR-AUTH-10 NHT — HSPL R+U special

### TC-PERM-010 — BR-AUTH-10 NHT: R+U HSPL của DN trong VV được phân công, KHÔNG được Create/Delete

- **Type:** Negative + Happy hybrid
- **Priority:** P1
- **Tài khoản:** nht_01 (Người hỗ trợ trợ giúp pháp lý — Tier 2 SSO)
- **Preconditions:**
  - Seed 1 VV (vụ việc) `vv-pc-nht-001` phân công nht_01 (giả định route FR-04 / PHAN_CONG_VV).
  - Seed 1 HSPL `hspl-nht-001` thuộc DN trong VV trên (don_vi_id matched).
  - Seed 1 HSPL `hspl-other-001` thuộc DN khác (NHT KHÔNG được phân công).
- **Steps:**
  1. Login `nht_01` → mở chi tiết DN tương ứng (FR-07 tab "Hồ sơ PL") → quan sát danh sách HSPL.
  2. Click `hspl-nht-001` → quan sát action-bar form HSPL.
  3. Click `[Sửa]` → cập nhật field `noi_dung` → Lưu.
  4. Quan sát có nút `[+ Thêm hồ sơ pháp lý]` không.
  5. Quan sát có nút `[Xóa]` trong cột Hành động không.
  6. Direct URL HSPL `hspl-other-001` (DN khác).
- **Expected:**
  - Bước 1-2: NHT thấy `hspl-nht-001` (R\*). Form render với button `[Sửa]` enable.
  - Bước 3: PUT `/api/hspl/hspl-nht-001` thành công 200. AUDIT_LOG ghi `UPDATE` actor=nht_01 (BR-DATA-05).
  - Bước 4: Nút `[+ Thêm hồ sơ pháp lý]` ẨN/disabled (NHT không có C — Permission overview §2.4 line 172 NHT = `R+U*` đặc biệt).
  - Bước 5: Nút `[Xóa]` ẨN (NHT không có D).
  - Bước 6: HTTP 403 — NHT chỉ R+U cho HSPL của DN trong VV được phân công (BR-AUTH-08 + BR-AUTH-10 đặc biệt).
- **SRS ref:** Overview §2.4 line 172 HO_SO_PHAP_LY_DN "NHT R+U* (BR-AUTH-10 đặc biệt)" + SRS UC150 line 671 "NHT cập nhật/đính kèm tài liệu hồ sơ — chỉ R + U".
- **Notes:** SPEC-CLARIFY-TVCS-05 (overview line 301) — SRS không quote rõ route SCR-IV-03 hay route khác cho NHT. Default test qua tab HSPL của DN. Phase B confirm route thực tế.

---

## Section G: Edge bổ sung A4 (Session lifecycle + Role change + SSO failure)

### TC-PERM-011 — Edge: Token expire mid-action (CB NV đang điền form CREATE TVCS)

- **Type:** Edge / Error injection
- **Priority:** P2
- **Tài khoản:** cb_nv_tw_01
- **Preconditions:**
  - Token TTL config (vd JWT 15 phút) — hoặc force invalidate qua admin endpoint.
  - cb_nv_tw_01 login, mở SCR-X1-01 → click [+ Thêm yêu cầu TV] → form mở.
- **Test Data:** Form data: doanh_nghiep_id=DN-001, noi_dung_tu_van="...".
- **Steps:**
  1. Login cb_nv_tw_01.
  2. Mở form CREATE TVCS → điền đầy đủ Accordion 1+2 (~5KB RTE).
  3. Force token expire: qua devtools application > cookies, xóa session/JWT cookie. HOẶC wait token TTL.
  4. Click [Lưu].
  5. Quan sát UI + network response.
- **Expected:**
  - **Bước 4:** Backend trả 401 Unauthorized.
  - **UI Path A:** Modal "Phiên hết hạn, vui lòng đăng nhập lại" → redirect /login. Form data lost (acceptable) HOẶC giữ trong sessionStorage để re-submit.
  - **UI Path B:** Auto silent refresh token (nếu có refresh token strategy) → resubmit transparent → success.
  - **STATE:** KHÔNG INSERT TU_VAN_CHUYEN_SAU bản nháp. AUDIT_LOG có entry session_expired.
- **SRS ref:** BR-AUTH-01 line 1525-1529 (session lifecycle).
- **Notes:** No SRS quote refresh token policy — best practice extrapolation. SPEC-CLARIFY-TVCS-PERM-05 — refresh strategy + form data preservation.

### TC-PERM-012 — Edge: Role change mid-session (qtht thu hồi role CB NV → user mất quyền giữa flow)

- **Type:** Edge
- **Priority:** P2
- **Tài khoản:** cb_nv_tw_01 (active session) + qtht_01 (admin)
- **Preconditions:**
  - cb_nv_tw_01 login active, mở SCR-X1-01 → mở chi tiết TVCS-X TIEP_NHAN → click [Phân công CG →] → modal mở.
  - qtht_01 trong tab khác đăng nhập admin panel.
- **Test Data:** —
- **Steps:**
  1. cb_nv_tw_01 mở modal phân công, chọn CG-A nhưng **chưa submit**.
  2. qtht_01 thu hồi role CB_NV của cb_nv_tw_01 (đặt vai_tro=NULL hoặc disable user).
  3. cb_nv_tw_01 click [Xác nhận] submit phân công.
  4. Quan sát UI + backend response.
- **Expected:**
  - **Bước 3:** Backend revalidate permission tại endpoint POST `/api/v1/tu-van-chuyen-sau/{id}/phan-cong` → reject HTTP 403 "Bạn không còn quyền thực hiện hành động này" (BR-AUTH-08 + per-request authz).
  - **UI:** Toast/modal lỗi 403. Modal đóng. Force redirect /login HOẶC reload session.
  - **STATE:** TVCS-X vẫn TIEP_NHAN, chuyen_gia_id=NULL. AUDIT_LOG: attempt-failed entry.
- **SRS ref:** BR-AUTH-01 + BR-AUTH-08 line 1531-1535 (per-request validation).
- **Notes:** No SRS quote per-action revalidation timing — best practice. SPEC-CLARIFY-TVCS-PERM-06.

### TC-PERM-013 — Edge: Tier 2 SSO VNeID callback fail (DN/CG flow)

- **Type:** Edge / Negative
- **Priority:** P2
- **Tài khoản:** dn_01 (Tier 2)
- **Preconditions:** Logout. SSO VNeID provider mock fail (return error_code=access_denied tại callback).
- **Test Data:** —
- **Steps:**
  1. Mở route SSO VNeID `/login-vneid` hoặc nút "Đăng nhập bằng VNeID".
  2. Redirect → VNeID provider auth.
  3. Mock VNeID return callback với `?error=access_denied&state=...`.
  4. Quan sát app callback handler + UI.
  5. Mock VNeID timeout (no response 60s) tại callback.
- **Expected:**
  - **Bước 3-4:** App callback `/oauth/callback` nhận error → render error page "Đăng nhập VNeID thất bại. Vui lòng thử lại" (SRS Gap nguyên văn). KHÔNG cấp session app. AUDIT_LOG: SSO_FAIL entry.
  - **Bước 5:** Timeout → app render timeout error page với nút retry. KHÔNG hang vô hạn.
  - **STATE:** dn_01 không có active session. KHÔNG truy cập được CMS.
- **SRS ref:** BR-AUTH-01 line 1525-1529 "Tier 2 = SSO VNeID OIDC Authorization Code flow".
- **Notes:** No SRS quote callback error handling — best practice OAuth/OIDC. SPEC-CLARIFY-TVCS-PERM-07 — error page wording + retry policy.

---

## Section H: Permission HSPL/TLPL cho CB_PD/QTHT explicit

### TC-PERM-014 — Permission HSPL/TLPL: cb_pd_tw_01 R only (no C/U/D), qtht_01 R cross-cấp toàn hệ thống

- **Type:** Permission / UI Verify
- **Priority:** P2
- **Tài khoản:** cb_pd_tw_01 (CB phê duyệt cấp TW) + qtht_01 (Quản trị hệ thống)
- **Preconditions:**
  - Seed 3 HSPL: `hspl-tw-001` thuộc don_vi_id=BTP-TW + `hspl-bn-001` thuộc don_vi_id=BKH (cấp BN) + `hspl-ag-001` thuộc don_vi_id=STP-AG (cấp ĐP).
  - Seed 3 TLPL tương tự thuộc TW/BN/AG.
  - cb_pd_tw_01 + qtht_01 sẵn sàng đăng nhập riêng phiên.
- **Steps:**
  1. **Login `cb_pd_tw_01`** → mở chi tiết DN cấp TW → tab "Hồ sơ PL".
  2. `take_snapshot` toolbar + actions cột Hành động trên row HSPL-TW-001.
  3. Click [Xem] HSPL-TW-001 → quan sát footer modal action.
  4. Cố navigate URL `/doanh-nghiep/{DN-BN}/...` để xem HSPL của BN cấp khác.
  5. Mở chi tiết TVCS có TLPL → tab "Tư liệu PL" → quan sát toolbar + actions.
  6. **Logout, login `qtht_01`** → mở DN bất kỳ thuộc TW → tab "Hồ sơ PL".
  7. Mở DN thuộc BKH (cross-cấp) → tab "Hồ sơ PL".
  8. Mở DN thuộc STP-AG (cross-cấp ĐP) → tab "Hồ sơ PL".
  9. Quan sát toolbar + actions cho qtht_01 trên cả 3 cấp.
  10. Mở chi tiết TVCS có TLPL → quan sát.
- **Expected:**
  - **cb_pd_tw_01 (R\* same-cấp):**
    - Bước 2: Toolbar tab "Hồ sơ PL" **KHÔNG có** [+ Thêm hồ sơ]. Cột Hành động chỉ có icon [Xem]; **KHÔNG có** [Sửa] [Xóa].
    - Bước 3: Modal chi tiết HSPL footer chỉ có [Đóng]; **KHÔNG có** [Sửa].
    - Bước 4: HSPL của BN không hiển thị (BR-AUTH-08). Hoặc render 403 nếu deeplink direct.
    - Bước 5: Tab TLPL same — KHÔNG có [+ Thêm tư liệu] / [Sửa] / [Xóa] / [Công khai] / [Hủy CK]. Chỉ [Xem].
  - **qtht_01 (R toàn hệ thống):**
    - Bước 6-8: qtht_01 thấy được HSPL của cả 3 cấp TW/BN/AG (BR-AUTH-08 exception cho QTHT — overview §2.4 line 159 "Không có exception ngoại trừ QTHT").
    - Bước 9: Toolbar tab "Hồ sơ PL" KHÔNG có [+ Thêm hồ sơ] (qtht read-only). Actions chỉ [Xem]. **KHÔNG có** [Sửa]/[Xóa].
    - Bước 10: Tab TLPL same — read-only, chỉ [Xem].
  - API direct POST/PUT/DELETE từ session 2 user trên → 403 cho cả HSPL và TLPL.
- **SRS ref:** Overview §2.4 (Permission Matrix line 171-175 nguyên văn): HSPL CB_PD=R\*, QTHT=R; TLPL CB_PD=R\*, QTHT=R + BR-AUTH-08 line 1531-1535 exception QTHT.
- **Notes:** A6 fill A5-G7 (gap permission HSPL/TLPL CB_PD + QTHT explicit). Trước A6 chỉ có TC-PERM-010 (NHT R+U) + TC-PERM-008 (CB_NV_DP IDOR). TC này close 2 cell missing trong matrix 6.2/6.3 (HSPL/TLPL × QTHT/CB_PD).

---

**Tổng số TC: 14**

**Phân bổ:**
- 🟢 UI Verify: 1 (TC-PERM-001)
- 🟢 Happy: 2 (TC-PERM-002 hybrid, TC-PERM-004)
- 🔴 Negative: 7 (TC-PERM-003, 005, 006, 007, 008, 009, 010)
- 🟡 Edge (A4): 3 (TC-PERM-011, 012, 013)
- 🟢 Permission explicit (A6): 1 (TC-PERM-014)

**Priority:** P0=5 (001, 002, 004, 005, 007) / P1=5 (003, 006, 008, 009, 010) / P2=4 (011, 012, 013, 014)

**Coverage:**
- BR-AUTH-01: Tier 1 + Tier 2 + redirect /login (TC-PERM-002, 003)
- BR-AUTH-05: PD cùng cấp (Happy TW + Negative BN→TW + Negative DP→BN) (TC-PERM-004, 005, 006)
- BR-AUTH-08: Cross-unit BN-BN ngang cấp + DP-DP ngang cấp + IDOR 3 entity (TC-PERM-007, 008)
- BR-AUTH-10: NHT R+U HSPL đặc biệt (TC-PERM-010)
- Permission Matrix: TVCS / HSPL / TLPL / DANH_GIA / PHIEN_TU_VAN — covered cross-FR-X.1
- CG action button visibility + DANH_GIA tab (TC-PERM-009)

**SPEC-CLARIFY phát sinh trong file này:**
- SPEC-CLARIFY-TVCS-PERM-03 — SRS không quote URL route SSO VNeID (Tier 2). Phase B verify URL thực tế.
- SPEC-CLARIFY-TVCS-PERM-04 — SRS không quote nguyên văn message error khi cross-cấp PD (BR-AUTH-05 violation). Default 403 + UI hide.
- (Tham chiếu hiện hữu: SPEC-CLARIFY-TVCS-PERM-01 + SPEC-CLARIFY-TVCS-05.)

*Tạo bởi BMAD A3 — 2026-05-06. Cập nhật A6 (+1 TC TC-PERM-014) + A7 finalized 2026-05-07.*

---

**Tổng số TC: 14**
