# Test Cases — Cross-FR-V.I: Permission Matrix (BR-AUTH-01/03/04/05/08)

> **SRS Ref**: BR-AUTH-01 (srs-fr-05:2377), BR-AUTH-03/04 (srs-fr-05:2469), BR-AUTH-05 (srs-fr-05:2385), BR-AUTH-08 (srs-fr-05:2391); permission matrix tổng `permission-matrix.md`
> **Ngày tạo**: 2026-05-06 (BMAD A3) · **A7 filter applied**: 2026-05-06
> **Tài khoản chính**: 7 role (`qtht_01`, `cb_nv_tw_01`, `cb_pd_tw_01`, `nht_01`, `tvv_01`, `dn_01`, mock_unauth) — verify cross-cutting auth.
> **A7 note**: Permission cross-FR — tất cả TC đều UI-driven (login + click + verify 403/redirect/hide). KHÔNG có TC chỉ-DB/API thuần.

---

## A. UI FIELD VERIFICATION

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước | Kết quả mong đợi | Type | Priority |
|----|---------|--------------|----------------|-----------|----------|------------------|------|----------|
| TC-VV-PERM-UI-01 | BR-AUTH-01 / Tier 2 VNeID | Verify chuyên trang DN dùng auth Tier 2 (KHÔNG phải Tier 1 nội bộ) | Browser private mode, chưa login. | — | 1. Truy cập URL chuyên trang DN `/ho-so-cua-toi/vu-viec`. | **UI**: Redirect tới trang đăng nhập VNeID (OIDC Authorization Code flow theo BR-AUTH-01 srs-fr-05:2377). KHÔNG hiển thị form username/password Tier 1. **PERSIST**: — | Happy | P0 |
| TC-VV-PERM-UI-02 | SCR-V.I-03 / context-sensitive button | Verify nút action-bar SCR-V.I-03 hiển thị THEO trạng thái + role | `cb_nv_tw_01` xem VV ở DA_PHAN_CONG. So với `cb_pd_tw_01` xem cùng VV (sau khi VV chuyển CHO_PHE_DUYET). | — | 1. CB NV xem VV DA_PHAN_CONG → quan sát action-bar. 2. CB NV trình PD → VV chuyển CHO_PHE_DUYET. 3. CB PD xem cùng VV → quan sát action-bar. 4. NHT xem cùng VV ở DA_PHAN_CONG → quan sát. | **UI**: (1) CB NV ở DA_PHAN_CONG: nút [Phân công] + tooltip điều kiện (srs-fr-05:1791-1795). (2) CB NV ở CHO_PHE_DUYET: KHÔNG hiển thị [Phê duyệt] [Từ chối] (vai trò KHÔNG đúng → ẩn nút). (3) CB PD ở CHO_PHE_DUYET: hiển thị [Phê duyệt] [Từ chối]. (4) NHT ở DA_PHAN_CONG (đã được phân công): hiển thị [Chấp nhận] [Từ chối]. **Quy ước:** vai trò KHÔNG đúng → ẩn (không mờ); vai trò ĐÚNG nhưng trạng thái sai → hiển thị mờ + tooltip. | Happy | P0 |

---

## B. CRUD HAPPY PATH — ROLE-SCOPED ACCESS

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước | Kết quả mong đợi | Type | Priority |
|----|---------|--------------|----------------|-----------|----------|------------------|------|----------|
| TC-VV-PERM-101 | BR-AUTH-03/04 / TW scope toàn quốc | CB NV TW xem được VV của tất cả đơn vị (TW + BN + DP) | `cb_nv_tw_01`. Có ≥3 VV thuộc TW + BN + DP. | — | 1. Login `cb_nv_tw_01`. 2. Vào DS VV (SCR-V.I-01). 3. Filter clear, scroll xem toàn list. | **STATE**: Backend skip don_vi_id filter cho user TW (BR-AUTH-03/04 srs-fr-05:2469). **UI**: Bảng hiện VV của cả TW, BN, DP (≥3 records, đa đơn vị trong cột "Tên DN" tooltip hiện đơn vị khác nhau). **PERSIST**: — | Happy | P0 |
| TC-VV-PERM-102 | BR-AUTH-08 / scope đơn vị | CB NV BN/DP chỉ xem VV của đơn vị mình | `cb_nv_bn_01` (giả lập — **SPEC-CLARIFY-VV-PERM-01**). Có VV của BN-X (sở hữu) và VV của DP-Y, BN-Z khác. | — | 1. Login user CB_NV_BN. 2. Vào DS VV. | **STATE**: Backend filter `WHERE don_vi_id = user.don_vi_id` (BR-AUTH-08 srs-fr-05:2391). **UI**: Bảng chỉ hiện VV của BN-X. KHÔNG hiển thị VV của DP-Y hay BN-Z (ngang cấp KHÔNG thấy nhau, BR-AUTH-02). **PERSIST**: — | Happy | P0 |
| TC-VV-PERM-103 | BR-AUTH-05 / PD cùng cấp | CB PD chỉ phê duyệt VV của đơn vị mình + cùng cấp với CB NV trình | `cb_pd_tw_01`. Có VV-1 trình bởi `cb_nv_tw_02` (TW) và VV-2 trình bởi user CB_NV_BN (BN). | — | 1. Login `cb_pd_tw_01`. 2. Vào DS VV (filter CHO_PHE_DUYET). 3. Try PD VV-1. 4. Try PD VV-2. | **STATE**: VV-1 PASS (cùng cấp TW). VV-2 FAIL với ERR-PD-02 "Bạn không có quyền phê duyệt vụ việc này" (BR-AUTH-05 srs-fr-05:2385). **UI**: VV-1 nút [Phê duyệt] active, click → DA_DUYET. VV-2 nút [Phê duyệt] mờ + tooltip "Cần cùng cấp đơn vị để phê duyệt" hoặc click → toast error ERR-PD-02. **PERSIST**: AUDIT_LOG PHE_DUYET cho VV-1; AUDIT_LOG attempt FAIL cho VV-2 (security log). | Happy | P0 |
| TC-VV-PERM-104 | DN scope theo doanh_nghiep_id | DN chỉ xem VV của DN mình (không thấy VV của DN khác) | `dn_01` (DN-AG). Có VV-X của DN-AG và VV-Y của DN-BG khác. | — | 1. Login `dn_01` qua VNeID. 2. Vào SCR-V.I-04 "/ho-so-cua-toi/vu-viec". 3. Try sửa URL truy cập VV-Y `/ho-so-cua-toi/vu-viec/{id-Y}`. | **STATE**: Backend filter `VU_VIEC.doanh_nghiep_id = current_user.doanh_nghiep_id` (cố định, srs-fr-05:1881). **UI**: SCR-V.I-04 chỉ hiện VV-X. Sửa URL VV-Y → 403 + redirect về SCR-V.I-04 (srs-fr-05:1828). **PERSIST**: AUDIT_LOG ATTEMPT_403 (security audit). | Happy | P0 |
| TC-VV-PERM-105 | NHT scope chỉ VV phân công | NHT chỉ xem VV được phân công cho mình | `nht_01` (AG). Có VV-1 phân công nht_01, VV-2 phân công nht_02 (BG), VV-3 chưa phân công. | — | 1. Login `nht_01`. 2. Truy cập DS VV (nếu có quyền). | **STATE**: Backend filter VU_VIEC `WHERE nguoi_xu_ly_id = nht_01.id` (UC60 PRE-02 srs-fr-05:796). **UI**: Bảng chỉ hiện VV-1. KHÔNG có VV-2 hay VV-3. NHT có thể KHÔNG có truy cập SCR-V.I-01 (CMS) — verify route — nếu redirect sang dashboard cá nhân thì OK. **PERSIST**: — | Happy | P0 |
| TC-VV-PERM-106 | UC67 / DN đánh giá scope DN | DN đánh giá chỉ VV của DN mình | `dn_01`. VV-X HOAN_THANH của dn_01, VV-Y HOAN_THANH của DN khác. | — | 1. `dn_01` xem VV-X → click [Đánh giá]. 2. Try gọi action đánh giá VV-Y (qua URL deeplink hoặc API replay). | **STATE**: VV-X PASS (đánh giá thành công). VV-Y FAIL với ERR-DG-VV-04 "Bạn không có quyền đánh giá vụ việc này" (srs-fr-05:1221, BR-AUTH-08). **UI**: VV-X form đánh giá hiện. VV-Y trang trả 403 hoặc tab DS không hiển thị. **PERSIST**: DANH_GIA_VU_VIEC INSERT cho VV-X; KHÔNG có entry cho VV-Y. | Happy | P0 |

---

## C. NEGATIVE — UNAUTHORIZED ACCESS

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước | Kết quả mong đợi | Type | Priority |
|----|---------|--------------|----------------|-----------|----------|------------------|------|----------|
| TC-VV-PERM-201 | BR-AUTH-01 / unauth access | User chưa login truy cập SCR-V.I-01/02/03 | Browser private mode, chưa login. | — | 1. Truy cập `/vu-viec`, `/vu-viec/them-moi`, `/vu-viec/{id}`. | **STATE**: Backend reject 401. **UI**: Redirect login page với `?redirect=/vu-viec` query param. **PERSIST**: AUDIT_LOG ATTEMPT_UNAUTH. | Negative | P0 |
| TC-VV-PERM-202 | UC59 / NHT cố phân công | NHT/TVV/DN truy cập action [Phân công] (chỉ CB_NV) | `nht_01` (đã login). | — | 1. Login `nht_01`. 2. Sửa URL hoặc replay request UC59. | **STATE**: Backend reject với ERR-PC-04 hoặc 403 (BR-AUTH-01 srs-fr-05:2377). **UI**: Toast error "Bạn không có quyền thực hiện thao tác này" (srs-fr-05:1619) hoặc 403 page. **PERSIST**: AUDIT_LOG ATTEMPT_403. | Negative | P0 |
| TC-VV-PERM-203 | UC63 / CB NV cố phê duyệt | CB NV (không phải CB PD) cố PD VV CHO_PHE_DUYET | `cb_nv_tw_01`. VV-X ở CHO_PHE_DUYET. | — | 1. Login `cb_nv_tw_01`. 2. Xem VV-X. 3. Action [Phê duyệt] có hiển thị? Try replay PD request. | **STATE**: Action [Phê duyệt] KHÔNG hiển thị cho CB_NV (srs-fr-05:1793). Replay request → 403 hoặc ERR-PD-02. **UI**: Action ẩn. Replay → toast error. **PERSIST**: — | Negative | P0 |
| TC-VV-PERM-204 | NEW-05 / CB NV cố công khai | CB NV (không phải CB PD) cố [Công khai] | `cb_nv_tw_01`. VV-X ở DA_DUYET cong_khai=0. | — | 1. Xem VV-X. 2. Action [Công khai]? Try replay request. | **STATE**: Action [Công khai] KHÔNG hiển thị cho CB_NV (srs-fr-05:1787 — CB Phê duyệt cùng cấp). Replay → 403 hoặc ERR-CK-VV-02. **UI**: Action ẩn. **PERSIST**: — | Negative | P0 |
| TC-VV-PERM-205 | NEW-01 / non-QTHT cố cấu hình quy trình | CB NV/PD/DN truy cập SCR cấu hình quy trình QTHT | `cb_nv_tw_01`. | — | 1. Login `cb_nv_tw_01`. 2. Truy cập URL cấu hình quy trình (`/qtht/cau-hinh-quy-trinh` — **SPEC-CLARIFY-VV-NEW-01**). | **STATE**: Backend reject 403 (BR-AUTH-01 srs-fr-05:2377, NEW-01 PRE-02 srs-fr-05:1242). **UI**: 403 page hoặc redirect dashboard với toast "Bạn không có quyền thực hiện thao tác này". **PERSIST**: AUDIT_LOG ATTEMPT_403. | Negative | P0 |

---

## D. EDGE CASES

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước | Kết quả mong đợi | Type | Priority |
|----|---------|--------------|----------------|-----------|----------|------------------|------|----------|
| TC-VV-PERM-301 | BR-AUTH-01 / session timeout | Session hết hạn giữa lúc thao tác | `cb_nv_tw_01`. Session timeout < 30 phút (giả lập invalidate token). | — | 1. Login. 2. Vào SCR-V.I-03 chi tiết VV. 3. Wait/invalidate token. 4. Click [Phân công]. | **STATE**: Backend trả 401. **UI**: Modal "Phiên làm việc đã hết hạn. Vui lòng đăng nhập lại." + nút [Đăng nhập] (srs-fr-05:1618). Sau click → redirect login với context. **PERSIST**: — | Edge | P0 |
| TC-VV-PERM-302 | BR-AUTH-08 / direct ID access (IDOR) | User cố truy cập VV không thuộc đơn vị qua sửa URL | `cb_nv_bn_01`. ID VV-Y của BN-Z khác đã biết. | — | 1. Login. 2. Sửa URL `/vu-viec/{id-Y}`. | **STATE**: Backend kiểm tra `WHERE don_vi_id = user.don_vi_id` (BR-AUTH-08). Nếu không match → 403/404 (security: nên 404 để không leak existence). **UI**: 404 page hoặc 403 + redirect DS VV. **PERSIST**: AUDIT_LOG ATTEMPT_IDOR (security audit). | Edge | P0 |
| TC-VV-PERM-303 | BR-AUTH-08 / batch action mixed scope | CB NV BN batch [Trình PD hàng loạt] với 1 VV của BN + 1 VV không thuộc đơn vị (forge ID) | `cb_nv_bn_01`. | — | 1. Forge request batch với 2 VV ID (1 thuộc BN, 1 thuộc DP). | **STATE**: Backend filter mỗi ID — chỉ process 1 VV thuộc BN. VV ngoài đơn vị → bỏ qua + audit. **UI**: Toast warning "Đã trình {1}/{2} vụ việc. {1} vụ việc gặp lỗi (không có quyền)." (srs-fr-05:1622). **PERSIST**: AUDIT_LOG TRINH_PD x1 + ATTEMPT_403 x1. | Edge | P1 |
| TC-VV-PERM-304 | UC60 / NHT phân công cũ → từ chối | NHT đã được phân công VV → CB NV phân công lại NHT khác → NHT cũ vẫn xem được? | `cb_nv_tw_01`. VV-X phân công `nht_01` → `nht_01` từ chối → CB NV phân công lại `nht_02`. | — | 1. Tạo flow trên. 2. Login `nht_01` xem VV-X. 3. Login `nht_02` xem VV-X. | **STATE**: VV-X.nguoi_xu_ly_id = `nht_02` sau phân công lại. **UI**: `nht_01` KHÔNG còn xem được VV-X (PHAN_CONG_VU_VIEC cũ trang_thai=TU_CHOI, current assignment là nht_02). `nht_02` xem được VV-X. **PERSIST**: 2 entries PHAN_CONG_VU_VIEC (1 TU_CHOI cho nht_01, 1 CHO_XAC_NHAN cho nht_02). | Edge | P1 |
| TC-VV-PERM-305 | NEW-05 / hủy công khai khác cấp | CB PD BN cố hủy công khai VV của TW (đã công khai) | CB PD BN giả lập + VV của TW cong_khai=1. | — | 1. Login CB PD BN. 2. Try [Hủy công khai] VV TW. | **STATE**: Backend kiểm tra cùng cấp (BR-AUTH-05 srs-fr-05:2385). Reject với ERR-CK-VV-02 "Bạn không có quyền công khai vụ việc thuộc đơn vị khác cấp" (srs-fr-05:1433). **UI**: Action ẩn hoặc click → toast error. **PERSIST**: VV cong_khai vẫn=1 unchanged. AUDIT_LOG ATTEMPT_403. | Edge | P0 |

---

## Tổng kết file

**Tổng TC: 18** (2 UI + 6 Happy + 5 Negative + 5 Edge) — ổn định sau Codex review 2026-05-09

**Priority**: P0 = 13 / P1 = 4 / P2 = 0 (cross-cutting permission luôn high priority)

**Coverage:**
- BR: BR-AUTH-01 (2-tier — TC-101/201), BR-AUTH-02 (kiến trúc 2-tier ngang cấp KHÔNG thấy nhau — TC-102), BR-AUTH-03/04 (TW/BN/DP scope — TC-101/102), BR-AUTH-05 (PD cùng cấp — TC-103/305), BR-AUTH-08 (don_vi_id filter + DN ownership — TC-104/302)
- Cross-FR coverage: FR-V.I-01 (DS scope — TC-101/102) + FR-V.I-06 (kiểm tra) + FR-V.I-09 (UC59 phân công — TC-202) + FR-V.I-13 (UC63 PD cùng cấp — TC-103/203) + FR-V.I-17 (UC67 đánh giá — TC-106) + NEW-01 (TC-205) + NEW-02 (TC-302) + NEW-05 (TC-204/305)
- Security tests: **IDOR (TC-302)**, session timeout (TC-301), batch mixed scope (TC-303), context-sensitive button rendering (UI-02), 403 audit log
- AC SRS: 100% permission AC documented across srs-fr-05:1241-1242 (NEW-01), 1370-1373 (NEW-05), 1303 (NEW-02 PRE-03), 1194-1195 (UC67 BR-AUTH-08)

**SPEC-CLARIFY:**
- **VV-PERM-01**: CSV thiếu user CB_NV_BN/DP và CB_PD_BN/DP — cần seed thêm hoặc chiến lược test 3-tier scope (mượn `cb_nv_tw_01` workaround? defer? seed thêm 3 user mỗi role?)
- **VV-NEW-01**: SCR cấu hình QTHT chưa spec rõ URL — placeholder `/qtht/cau-hinh-quy-trinh`
- **VV-IDOR**: BE response code khi user cố truy cập VV ngoài đơn vị — 403 (leak existence) vs 404 (an toàn hơn). SRS không quote rõ
- **VV-SESSION-TIMEOUT**: Thời gian session timeout cụ thể (15 phút? 30 phút?) — SRS không quote

> **Codex review 2026-05-09:**
> - File coverage cross-FR đã đầy đủ — KHÔNG thêm TC mới
> - 5 BR-AUTH + IDOR + session + batch mixed + 8 UC scope test trong 18 TC compact
> - Phối hợp với 13 file UC khác — file 14 là layer cross-cutting, không trùng lặp với permission test trong UC files
