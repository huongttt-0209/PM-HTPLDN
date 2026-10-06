# Test Cases — Permission Matrix 11 Role × FR-03 (Đào tạo, Tập huấn)

> **SRS Ref**: BR-AUTH-01 / BR-AUTH-05 / BR-AUTH-08 / BR-FLOW-05 (srs-fr-03-dao-tao.md §6 dòng 1241-1262 + srs-v3.md Phụ lục B), [permission-matrix.md](../../permission-matrix.md) section "Đào tạo, Tập huấn".
> **Nguồn**: Plan overview §3 Permission Matrix + sibling DN `06-TC-permission-matrix.md`.
> **Ngày tạo**: 2026-05-09
> **Đặc thù**: Cross 4-cấp (TW/BN/ĐP) × 11 role × 10 entity owned. Phân biệt **scope-own** (CB_NV CRUD chính scope mình) vs **approve-cùng-cấp** (CB_PD chỉ duyệt cùng cấp — BR-AUTH-05). DN/NHT API-only qua Cổng PLQG (BR-FLOW-05). QTHT read-only entity FR-03.

---

## Quy ước

- **TC ID:** `TC-PERM-{type}-{seq:03d}` — type: `P` (permission, default cho file này) / `N` (negative — block 403). Mọi TC ở file này = Permission hoặc Negative.
- **Account convention:** `_03` accounts dành cho permission negative (qtht_03, cb_nv_tw_03, cb_nv_bn_03, cb_nv_dp_03, cb_pd_tw_03, cb_pd_bn_03, cb_pd_dp_03, tvv_03, cg_03, nht_03, dn_03). Reference [`input/users.csv`](../../../input/users.csv) + [`test-accounts-isolation.csv`](../../../input/test-accounts-isolation.csv).
- **Kết quả mong đợi:** `**STATE**: ... **UI**: ... **PERSIST**: ...`.
- **Priority:** 🔴 Critical · 🟡 Major · 🟢 Minor.
- **Mặc định 403 cho UI:** sidebar không có menu Đào tạo / URL hack → redirect `/403` hoặc `/dashboard` / API direct → HTTP 403.

---

## Permission Matrix Reference (rút gọn từ Plan §3 + permission-matrix.md)

| Entity | QTHT | CB_NV_TW | CB_NV_BN | CB_NV_DP | CB_PD_TW | CB_PD_BN | CB_PD_DP | TVV | CG | NHT | DN |
|--------|:----:|:--------:|:--------:|:--------:|:--------:|:--------:|:--------:|:---:|:--:|:---:|:--:|
| CTDT (CRUD) | R only | scope-TW | scope-BN | scope-ĐP | — | — | — | — | — | — | — |
| CTDT (Public_view) | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | DA_CONG_KHAI | DA_CONG_KHAI | DA_CONG_KHAI | DA_CONG_KHAI |
| KHOA_HOC (Create/Update/Delete) | — | scope-TW | scope-BN | scope-ĐP | — | — | — | — | — | — | — |
| KHOA_HOC (Approve trước thực thi) | — | — | — | — | scope-TW | scope-BN | scope-ĐP | — | — | — | — |
| KHOA_HOC (Approve_KQ sau thực thi) | — | — | — | — | scope-TW | scope-BN | scope-ĐP | — | — | — | — |
| BAI_GIANG / NHCH / DE_KIEM_TRA / GV (CRUD) | — | scope-TW | scope-BN | scope-ĐP | — | — | — | — | — | — | — |
| DANG_KY (self) | — | — | — | — | — | — | — | self | self | self | self (DN cử HV) |
| DANG_KY (Approve) | — | scope-own | scope-own | scope-own | — | — | — | — | — | — | — |
| KET_QUA (Create) | — | scope-own | scope-own | scope-own | — | — | — | — | — | — | — |
| DE_XUAT (Create từ Cổng PLQG) | — | — | — | — | — | — | — | — | — | ✓ | ✓ |
| DE_XUAT (Receive trên CMS) | — | scope-own | scope-own | scope-own | — | — | — | — | — | — | — |
| CHUNG_NHAN (Issue) | — | — | — | — | scope-TW | scope-BN | scope-ĐP | — | — | — | (DN xem chỉ HV của mình) |

> Test accounts cụ thể: xem [permission-matrix-by-fr.md](../../permission-matrix-by-fr.md) tab FR-III.

---

## SPEC-CLARIFY (file này)

| Mã | Mô tả | Trạng thái |
|----|-------|-----------|
| SPEC-CLARIFY-DT-PERM-01 | SRS không quote nguyên văn message 403 cho từng role × entity. Test theo HTTP code + UI toast generic ("Bạn không có quyền"). Cần BA confirm message chuẩn. | Pending BA |
| SPEC-CLARIFY-DT-PERM-02 | BR-AUTH-08 (Plan §2.1) chỉ quote FR-III-01/02/06 — KHÔNG bao FR-III-15/18 (Approve flow). Verify approve cũng bị scope: CB_PD_BN cố duyệt KH cấp TW → 403 (BR-AUTH-05 + BR-AUTH-08 combined). | Pending BA |
| SPEC-CLARIFY-DT-PERM-03 | DN cử HV qua Cổng PLQG (BR-FLOW-05) — CMS có endpoint riêng cho DN tạo DANG_KY hay DN chỉ qua API public? Per memory `qa_htpldn_api_wrap_bug` + Plan §3 row "DN: self (DN cử HV)" — assume API public. | Pending BA |
| SPEC-CLARIFY-DT-PERM-04 | Cổng PLQG public API — return CTĐT/KH `DA_CONG_KHAI` only? Hay cả `DA_DUYET`? SRS dòng BR-FLOW-05 quote "Công khai qua API" — assume DA_CONG_KHAI only. Test với guest/anonymous token. | Pending BA |
| SPEC-CLARIFY-DT-PERM-05 | QTHT read-only — có quyền read AUDIT_LOG cross-entity FR-03 không? Per Plan §1.3 "Read-only entity FR-03" → assume YES. Verify endpoint `/api/v1/audit-log?entity=CHUONG_TRINH_DAO_TAO` với token QTHT. | Pending BA |
| SPEC-CLARIFY-DT-PERM-06 | BE convention re-check role per mutation (không trust JWT cache) — best practice security | BA confirm + nguyên văn message demote |
| SPEC-CLARIFY-DT-PERM-07 | Rate limit public API Cổng PLQG (anonymous) — req/min/IP threshold | BA confirm SLA |

---

## A. CROSS-CẤP — CB_NV cố CRUD CTĐT khác cấp (BR-AUTH-08 violate)

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|---------|--------------|----------------|-----------|-------------------|------------------|------|
| TC-PERM-P-001 | BR-AUTH-08 / FR-III-01 | CB_NV_TW cố sửa CTĐT cấp BN (cross-cấp xuống) → 403 | cb_nv_tw_03 đăng nhập. CTĐT-BN-2026-001 thuộc đơn vị BN (cấp BN, owner cb_nv_bn_01). | API direct `PUT /api/v1/ctdt/CTDT-BN-2026-001` body `{ten_ctdt:"hack"}` token cb_nv_tw_03 | 1. Login cb_nv_tw_03. 2. Call API direct PUT. 3. Check response. | **STATE**: BE check `don_vi_id` mismatch (TW token vs BN record) → 403 (BR-AUTH-08). KHÔNG UPDATE. AUDIT_LOG: hanh_dong='ACCESS_DENIED', entity='CHUONG_TRINH_DAO_TAO', entity_id=CTDT-BN-2026-001, ly_do='cross-cap-down'. **UI**: HTTP 403 + toast "Bạn không có quyền truy cập tài nguyên này" (SPEC-CLARIFY-DT-PERM-01). **PERSIST**: Record giữ nguyên ten_ctdt cũ. | Permission 🔴 |
| TC-PERM-P-002 | BR-AUTH-08 / FR-III-01 | CB_NV_DP cố CRUD CTĐT cấp BN (cross-cấp lên) → 403 | cb_nv_dp_03 đăng nhập. CTĐT-BN-2026-001 cấp BN. | API direct `PUT /api/v1/ctdt/CTDT-BN-2026-001` token cb_nv_dp_03 | 1. Login cb_nv_dp_03. 2. POST/PUT/DELETE API direct. | **STATE**: BE check don_vi_id mismatch → 403. KHÔNG modify. AUDIT_LOG ACCESS_DENIED. **UI**: HTTP 403. **PERSIST**: Record giữ nguyên. | Permission 🔴 |
| TC-PERM-P-003 | BR-AUTH-08 / FR-III-01 | Multi-tenant ĐP — cb_nv_dp_03 (HCM) cố sửa CTĐT của ĐP khác (HN) → 403 | cb_nv_dp_03 (đơn vị HCM) đăng nhập. CTĐT-DP-HN-2026-001 thuộc đơn vị HN. | API direct PUT token cb_nv_dp_03 | 1. Login cb_nv_dp_03. 2. PUT API direct. | **STATE**: BE check don_vi_id ngang cấp khác đơn vị → 403 (BR-AUTH-08 multi-tenant). **UI**: HTTP 403. **PERSIST**: Record giữ nguyên. | Permission 🔴 |

---

## B. CROSS-ROLE — DN/NHT/TVV/CG/GV cố CRUD entity FR-03 trên CMS

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|---------|--------------|----------------|-----------|-------------------|------------------|------|
| TC-PERM-N-004 | Permission Matrix / BR-AUTH-08 | DN không truy cập CMS module Đào tạo | dn_03 đăng nhập (giả định CMS có DN account — Plan §3 row DN public viewer). Per memory `qa_htpldn_otp_default` OTP=666666. | URL `/dao-tao/ctdt` | 1. Login dn_03. 2. Quan sát sidebar. 3. Cố navigate URL `/dao-tao/ctdt` direct. | **STATE**: — (read attempt). **UI**: Sidebar **KHÔNG hiển thị** menu "Đào tạo, Tập huấn" cho role DN. URL hack → redirect `/403` hoặc `/dashboard` (per memory `qa_htpldn_403_redirect`). API direct GET → 403. **PERSIST**: Reload — vẫn bị chặn. **Note**: Per Plan §3 + SPEC-CLARIFY-DT-PERM-03 — DN tương tác qua Cổng PLQG, không CMS direct. | Negative 🔴 |
| TC-PERM-N-005 | Permission Matrix | NHT cố CRUD CTĐT/KH trên CMS → 403 | nht_03 đăng nhập. | API direct `POST /api/v1/ctdt` token nht_03 + URL `/dao-tao/ctdt` | 1. Login nht_03. 2. Sidebar quan sát. 3. URL hack. 4. API direct POST. | **STATE**: BE return 403 (NHT chỉ Create DE_XUAT qua Cổng PLQG, không CRUD CTĐT/KH trên CMS). **UI**: Sidebar KHÔNG có menu Đào tạo (chỉ Public_view qua portal). URL → /403. API → 403. **PERSIST**: Không tạo record. | Negative 🔴 |
| TC-PERM-N-006 | Permission Matrix | TVV/CG cố CRUD CTĐT — chỉ public view + ĐK self | tvv_03 đăng nhập. CTĐT-TW-2026-001 DA_CONG_KHAI. | API direct PUT token tvv_03 | 1. Login tvv_03. 2. Quan sát sidebar. 3. API direct PUT/DELETE CTĐT. | **STATE**: BE return 403. KHÔNG modify. AUDIT_LOG ACCESS_DENIED. **UI**: Sidebar KHÔNG có menu CRUD; có thể có menu "Đăng ký KH" (self ĐK). API direct CRUD → 403. **PERSIST**: Record giữ nguyên. | Negative 🟡 |
| TC-PERM-N-007 | Permission Matrix | CG (chuyên gia) cố CRUD BAI_GIANG / NHCH / GV → 403 | cg_03 đăng nhập. | API direct POST/PUT các entity | 1. Login cg_03. 2. API direct. | **STATE**: BE 403 — CG không có quyền CRUD entity tài nguyên đào tạo (Permission Matrix row "BAI_GIANG/NHCH/GV CRUD" CG=—). **UI**: HTTP 403. **PERSIST**: Không modify. | Negative 🟡 |

---

## C. SCOPE_OWN — CB_NV cố sửa record không thuộc scope own (cùng cấp khác đơn vị)

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|---------|--------------|----------------|-----------|-------------------|------------------|------|
| TC-PERM-P-008 | BR-AUTH-08 / FR-III-01 | CB_NV_BN (Bộ KH&ĐT) cố sửa CTĐT của Bộ Tư pháp (ngang cấp khác Bộ) → 403 | cb_nv_bn_03 (đơn vị Bộ KH&ĐT) đăng nhập. CTĐT-BN-BTP-2026-001 thuộc Bộ Tư pháp. | API direct PUT token cb_nv_bn_03 | 1. Login. 2. PUT API direct. | **STATE**: BE check don_vi_id mismatch (cùng cấp BN nhưng đơn vị khác) → 403. AUDIT_LOG ACCESS_DENIED. **UI**: HTTP 403. **PERSIST**: Record không đổi. | Permission 🔴 |
| TC-PERM-P-009 | BR-AUTH-08 / FR-III-05 | CB_NV_DP cố tạo KH gắn CTĐT của ĐP khác (FK violate scope) → reject | cb_nv_dp_03 (HCM) đăng nhập. CTĐT-DP-HN-2026-001 thuộc HN. | API direct `POST /api/v1/khoa-hoc` body `{ctdt_id: "CTDT-DP-HN-2026-001", ...}` token DP HCM | 1. POST API direct với ctdt_id outside scope. | **STATE**: BE check ctdt_id thuộc don_vi_id của user → mismatch → 400/403. KHÔNG INSERT KHOA_HOC. **UI**: HTTP 400/403 + message "Không thể tạo khóa học cho chương trình thuộc đơn vị khác". **PERSIST**: Count KHOA_HOC không đổi. | Permission 🔴 |

---

## D. APPROVE_CROSS_LEVEL — CB_PD cố duyệt cross-cấp (BR-AUTH-05 violate)

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|---------|--------------|----------------|-----------|-------------------|------------------|------|
| TC-PERM-P-010 | BR-AUTH-05 / FR-III-15 / ERR-PD-01 | CB_PD_BN cố duyệt KH cấp TW → ERR-PD-01 (BR-AUTH-05 violate) | cb_pd_bn_03 đăng nhập. KH-TW-20260509-001 trạng thái CHO_DUYET (cấp TW). | API direct `POST /api/v1/khoa-hoc/KH-TW-20260509-001/duyet` token cb_pd_bn_03 | 1. Login cb_pd_bn_03. 2. POST API direct duyệt. | **STATE**: BE check `cap_pd === cap_kh` (BR-AUTH-05 cùng cấp). Mismatch (BN vs TW) → ERR-PD-01. KHÔNG transition state. AUDIT_LOG: hanh_dong='ACCESS_DENIED' + ly_do='cross-cap-approval'. **UI**: HTTP 403/422 + message "**Phê duyệt khác cấp không hợp lệ**" (per Plan §2.3 ERR-PD-01 — message nguyên văn pending SPEC-CLARIFY-DT-PERM-01). **PERSIST**: KH state vẫn CHO_DUYET. | Permission 🔴 |
| TC-PERM-P-011 | BR-AUTH-05 / FR-III-18 | CB_PD_DP cố duyệt KQ KH cấp BN → ERR-PD-01 | cb_pd_dp_03 đăng nhập. KH-BN-20260509-001 trạng thái CHO_DUYET_KQ (cấp BN). | API direct `POST /api/v1/khoa-hoc/KH-BN-20260509-001/duyet-kq` token cb_pd_dp_03 | 1. POST API direct duyệt KQ. | **STATE**: BR-AUTH-05 violate (DP vs BN) → 403/422 ERR-PD-01. KHÔNG transition CHO_DUYET_KQ → HOAN_THANH. **UI**: HTTP 403/422. **PERSIST**: KH giữ CHO_DUYET_KQ. CHUNG_NHAN không phát sinh. | Permission 🔴 |
| TC-PERM-P-012 | BR-AUTH-05 / SPEC-CLARIFY-DT-PERM-02 | CB_PD_TW cố duyệt KH cấp ĐP (cross-cấp xuống) → ERR-PD-01 | cb_pd_tw_03 đăng nhập. KH-DP-20260509-001 cấp ĐP CHO_DUYET. | API direct duyệt token cb_pd_tw_03 | 1. POST API direct. | **STATE**: BR-AUTH-05 cùng cấp tuyệt đối → cross down cũng reject. 403/422 ERR-PD-01. **UI**: HTTP 403/422. **PERSIST**: KH giữ CHO_DUYET. | Permission 🟡 |

---

## E. SELF_PERMISSION — TVV/CG/NHT chỉ thấy KH public + tự ĐK

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|---------|--------------|----------------|-----------|-------------------|------------------|------|
| TC-PERM-P-013 | BR-FLOW-05 / Permission Matrix | TVV chỉ thấy KH `DA_CONG_KHAI` qua public view, không thấy DU_THAO/CHO_DUYET | tvv_03 đăng nhập. Seed: KH-001 DA_CONG_KHAI + KH-002 DU_THAO + KH-003 DA_DUYET (chưa public). | API `GET /api/v1/khoa-hoc/public` hoặc URL public list | 1. Login tvv_03. 2. Mở trang public KH (hoặc URL `/dao-tao/khoa-hoc-public`). | **STATE**: BE filter `WHERE trang_thai IN ('DA_CONG_KHAI','DANG_DIEN_RA','DA_KET_THUC')` (per BR-FLOW-05 + SPEC-CLARIFY-DT-PERM-04). **UI**: List chỉ KH-001 (DA_CONG_KHAI). KHÔNG thấy KH-002 (DU_THAO) + KH-003 (DA_DUYET pre-public). **PERSIST**: Reload — same dataset. | Permission 🔴 |
| TC-PERM-P-014 | FR-III-04 / Permission Matrix | TVV/CG/NHT đăng ký tham gia KH thành công (self ĐK) — happy gate | tvv_03 đăng nhập. KH-001 DA_CONG_KHAI có slot. | `POST /api/v1/dang-ky` body `{khoa_hoc_id: "KH-001"}` | 1. Login. 2. Click [Đăng ký] tại KH-001 hoặc API direct. | **STATE**: INSERT DANG_KY_DAO_TAO với hoc_vien_id=tvv_03 (self), trang_thai='CHO_DUYET' hoặc 'DA_DUYET' tùy quy trình. **UI**: Toast thành công. **PERSIST**: Detail TVV/CG → tab "Khóa học đã đăng ký" có KH-001. | Permission 🟡 |

---

## F. PUBLIC_API — Cổng PLQG chỉ trả CTDT/KH `DA_CONG_KHAI` (BR-FLOW-05)

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|---------|--------------|----------------|-----------|-------------------|------------------|------|
| TC-PERM-P-015 | BR-FLOW-05 / FR-III-16 | Cổng PLQG public API — anonymous request chỉ thấy CTDT `DA_CONG_KHAI` | Seed: 4 CTDT — DU_THAO/CHO_DUYET/DA_DUYET/DA_CONG_KHAI. | `GET /api/public/v1/ctdt` (anonymous, không token) | 1. Curl public API anonymous. 2. Verify response data. | **STATE**: BE filter `WHERE trang_thai = 'DA_CONG_KHAI' AND la_cong_khai = 1` (BR-FLOW-05 + SPEC-CLARIFY-DT-PERM-04). **UI**: HTTP 200 + response data chỉ chứa 1 CTDT (DA_CONG_KHAI). KHÔNG có DU_THAO/CHO_DUYET/DA_DUYET (chưa toggle public). **PERSIST**: Reload — same. | Permission 🔴 |
| TC-PERM-P-016 | BR-FLOW-05 / FR-III-16 | Cổng PLQG public API — KHÔNG expose private fields (vd ghi_chu_noi_bo, audit_log) | Anonymous GET public API. | `GET /api/public/v1/ctdt/CTDT-TW-2026-001` (DA_CONG_KHAI) | 1. Curl public API. 2. Verify response schema. | **STATE**: BE serialize chỉ public fields: ten, ma, mo_ta, don_vi, ngay_bd, ngay_kt, danh_sach_kh_public. KHÔNG expose: ghi_chu_noi_bo, created_by, updated_by, ip_address, audit_log. **UI**: Response JSON keys = whitelist subset (SPEC-CLARIFY-DT-PERM-04 chuẩn schema pending). **PERSIST**: Same response cross-call. | Permission 🟡 |

---

## G. ADMIN_BYPASS — QTHT read-only entity FR-03 (KHÔNG CRUD)

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|---------|--------------|----------------|-----------|-------------------|------------------|------|
| TC-PERM-P-017 | Permission Matrix / Plan §1.3 | QTHT read CTĐT toàn HT cross-đơn-vị nhưng KHÔNG CRUD | qtht_03 đăng nhập. Seed CTĐT cả 3 cấp (TW + BN + ĐP). | URL `/dao-tao/ctdt` + API direct PUT/POST/DELETE | 1. Login qtht_03. 2. GET API list CTĐT. 3. Quan sát toolbar. 4. Cố API direct POST/PUT/DELETE. | **STATE**: GET → 200 + data toàn hệ thống (cross-đơn-vị, all 3 cấp). POST/PUT/DELETE → 403 (read-only per Plan §1.3 + Permission Matrix). AUDIT_LOG ACCESS_DENIED cho mọi attempt CRUD. **UI**: List hiển thị tất cả CTĐT toàn HT. KHÔNG có nút [+ Thêm mới], [Sửa], [Xóa] (chỉ icon [Xem]). API CRUD direct → 403. **PERSIST**: Read repeatable — same dataset. CRUD attempt không thay đổi DB. | Permission 🔴 |

---

## H. EDGE CASES (A4 added)

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|---------|--------------|----------------|-----------|-------------------|------------------|------|
| TC-PERM-E-018 | BR-AUTH-08 / Permission edge / Role demote during action | CB_NV_TW bị demote QTHT giữa session — token cũ vẫn valid → BE re-check role | cb_nv_tw_03 đăng nhập + đã có form sửa CTĐT mở (Tab 1). Admin (qtht_01) đăng nhập Tab 2 và demote cb_nv_tw_03 role qua FR-10 W1.4 TKPQ UI hoặc PUT /api/v1/tai-khoan/{id}. | Token cũ + role mới | 1. cb_nv_tw_03 đang giữ form sửa CTDT (Tab 1). 2. qtht_01 update role qua FR-10 W1.4 (Tab 2). 3. cb_nv_tw_03 click [Lưu] ở Tab 1. 4. Quan sát toast + network response. | **STATE**: BE re-check role → reject 403. **UI**: Toast "Vai trò đã thay đổi, vui lòng đăng nhập lại" (SPEC-CLARIFY-DT-PERM-06). Network panel hiển thị PUT request trả 403. **PERSIST**: CTDT không đổi. Reload Tab 1 → user redirect login hoặc /403. | Edge 🔴 |
| TC-PERM-E-019 | BR-FLOW-05 / Public API / Idempotency | Anonymous request public API CTDT 1000 lần liên tiếp — verify rate limit | Anonymous (no token). curl/wrk tool sẵn dùng. | Loop 1000 GET `/api/public/v1/ctdt` | 1. Bash loop curl 1000 lần. 2. Đếm response code 200 vs 429. | **STATE**: BE rate limit (vd 60 req/min/IP) → trả 429 sau N requests. **UI**: Network response trả HTTP 429 + header `Retry-After` sau ngưỡng. Aggregate count: ≤60 200, còn lại 429. **PERSIST**: SPEC-CLARIFY-DT-PERM-07 ngưỡng pending BA — test đo threshold thực tế. | Edge 🟡 |

---

## A7 Filter Notes

- **SỬA:** TC-PERM-E-018 — role demote test thực thi qua 2 tabs (Tab 1 = cb_nv_tw_03 mở form, Tab 2 = qtht_01 demote qua FR-10 W1.4 UI hoặc API). Observable qua toast + network 403. Phụ thuộc FR-10 W1.4 ready (đã done per memory).
- **SỬA:** TC-PERM-E-019 — rate limit test qua curl loop từ host (env có anonymous public API endpoint). Observable qua HTTP response codes aggregate.
- **KEEP all 17 base TC:** Mọi permission negative TC observable qua sidebar không có menu / URL hack → 403 / API direct → 403.

---

## Tổng hợp file 13

- **Total TC active sau A7:** 19 (post-A4: 17 base + 2 edge — TC-PERM-E-018 role demote SỬA + TC-PERM-E-019 rate limit SỬA)
  - A: 3 (cross-cấp CB_NV CRUD CTDT)
  - B: 4 (cross-role DN/NHT/TVV/CG)
  - C: 2 (scope-own ngang cấp khác đơn vị)
  - D: 3 (approve cross-cấp BR-AUTH-05)
  - E: 2 (TVV/CG self permission + public view)
  - F: 2 (public API BR-FLOW-05)
  - G: 1 (QTHT read-only)
  - H: 2 (A4 edge — role demote security re-check + rate limit anonymous)
- **SPEC-CLARIFY:** 7 (DT-PERM-01..07)
- **Priority:** 12 🔴 + 7 🟡

> **Coverage notes:**
> - 11 role × 10 entity owned mapping được test qua 17 representative TC (không bloat — pick boundary cases per Plan §3 matrix).
> - QTHT bypass test (TC-PERM-P-017) cover toàn matrix row "QTHT" trong 1 TC compound.
> - DN role test (TC-PERM-N-004) — note SPEC-CLARIFY-DT-PERM-03 nếu DN không có CMS user thì TC = "edge — verify expected fail" (sibling DN file 06 row TC-PERM-020 pattern).
> - 5 SPEC-CLARIFY tickets pending BA — BLOCK Phase B nếu không resolve trước smoke.

---

## Liên kết

- SRS: [`srs-fr-03-dao-tao.md`](../../../input/srs-v3/srs-fr-03-dao-tao.md) §6 BR + Plan §3 Permission
- Permission ref: [`permission-matrix.md`](../../permission-matrix.md), [`permission-matrix-by-fr.md`](../../permission-matrix-by-fr.md)
- Plan: [`00-test-plan-overview.md`](00-test-plan-overview.md) §3
- Sibling pattern: [`output/test-cases/doanh-nghiep/06-TC-permission-matrix.md`](../doanh-nghiep/06-TC-permission-matrix.md)
- Account ref: [`input/users.csv`](../../../input/users.csv), [`input/test-accounts-isolation.csv`](../../../input/test-accounts-isolation.csv)
