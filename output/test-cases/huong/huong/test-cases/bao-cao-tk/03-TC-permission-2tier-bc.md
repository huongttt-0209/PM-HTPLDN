# Test Cases — Permission Matrix BC (BR-AUTH-08, 2-tier TW/BN/ĐP)

> **SRS Ref**: srs-fr-11:39-49 (phân quyền tổng quan), srs-fr-11:1258-1262 (BR-AUTH-08 formal), srs-fr-11:1043 (SCR-IX-01 row#5 dropdown đơn vị)
> **Ngày tạo**: 2026-05-10
> **Đặc thù**: Test phân quyền data scope 2-tier cho TOÀN BỘ 23 loại BC (UC124-UC146). Mỗi cấp role chỉ thấy data scope đơn vị mình. CB_NV và CB_PD đều có quyền xem BC theo srs-fr-11:49 Tác nhân chính.

---

## Quy ước

- **Priority**: 🔴 P0 · 🟡 P1 · 🟢 P2
- **TraceID**: `BR-AUTH-08 / {scope}` hoặc `FR-IX / Permission`

---

## A0. UNAUTHENTICATED (BR-AUTH-01 — Codex F-03)

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|---------|--------------|----------------|-----------|-------------------|------------------|------|
| TC-BC-PERM-000 | BR-AUTH-01 / Codex F-03 | Chưa đăng nhập truy cập /bao-cao | Browser session sạch (clear cookies/localStorage). Chưa đăng nhập. | — | 1. Truy cập trực tiếp URL `http://103.172.236.130:3000/bao-cao`. | (1) Redirect về `/login` HOẶC trả 401 (không lộ data BC). (3) KHÔNG trả dữ liệu BC. KHÔNG render SCR-IX-01. Sau khi login → resume URL hoặc về dashboard. | Permission 🔴 |

---

## A. POSITIVE — TW thấy toàn quốc

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|---------|--------------|----------------|-----------|-------------------|------------------|------|
| TC-BC-PERM-001 | BR-AUTH-08 / TW scope | CB_NV_TW xem BC HD toàn quốc | cb_nv_tw_01 login. HD ở 3 đơn vị: TW + BN + ĐP. | ky=THANG | 1. Chọn BC HD. 2. don_vi=Toàn quốc. 3. [Xem]. | (3) tong_hoi_dap = sum 3 đơn vị. theo_don_vi[] hiện 3 đơn vị. | Permission 🔴 |
| TC-BC-PERM-002 | BR-AUTH-08 / TW filter BN bất kỳ | CB_NV_TW filter BN cụ thể | cb_nv_tw_01 login. | don_vi=Bộ KH&ĐT (BN) | 1. Chọn BC HD. 2. Dropdown đơn vị → chọn Bộ KH&ĐT. 3. [Xem]. | (3) Chỉ HD scope Bộ KH&ĐT. theo_don_vi[] 1 entry. | Permission 🟡 |
| TC-BC-PERM-003 | BR-AUTH-08 / TW filter ĐP bất kỳ | CB_NV_TW filter ĐP cụ thể | cb_nv_tw_01 login. | don_vi=Sở TP AG (ĐP) | 1. Chọn BC VV. 2. Dropdown → Sở TP AG. 3. [Xem]. | (3) Chỉ VV scope Sở TP AG. | Permission 🟡 |
| TC-BC-PERM-004 | BR-AUTH-08 / TW + CB_PD | CB_PD_TW cũng xem được BC | cb_pd_tw_01 login. | ky=THANG | 1. Truy cập SCR-IX-01. 2. Chọn BC HD. 3. [Xem]. | (3) PD_TW xem được giống NV_TW (Tác nhân chính srs-fr-11:49). | Permission 🟡 |

---

## B. POSITIVE — BN chỉ thấy BN mình

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|---------|--------------|----------------|-----------|-------------------|------------------|------|
| TC-BC-PERM-010 | BR-AUTH-08 / BN scope | CB_NV_BN chỉ thấy BN mình | cb_nv_bn_01 login (Bộ KH&ĐT). HD: 5 ở Bộ KH&ĐT + 5 ở Bộ TP. | ky=THANG | 1. Chọn BC HD. 2. [Xem]. | (3) tong_hoi_dap=5 (chỉ Bộ KH&ĐT). theo_don_vi[] chỉ Bộ KH&ĐT. KHÔNG thấy Bộ TP. | Permission 🔴 |
| TC-BC-PERM-011 | SCR-IX-01 row#5 | Dropdown đơn vị locked cho CB_NV_BN | cb_nv_bn_01 login. | — | 1. Open dropdown đơn vị. | (3) Dropdown disabled hoặc chỉ có 1 option "Bộ KH&ĐT" (không cho phép chọn "Toàn quốc" hoặc BN khác). | Permission 🔴 |
| TC-BC-PERM-012 | BR-AUTH-08 / BN cross-attempt API / Codex F-05 | CB_NV_BN gọi API với don_vi_id của BN khác → 403 (deterministic) | cb_nv_bn_01 login. | don_vi_id=Bộ TP (BN khác) | 1. DevTools modify request: don_vi_id=Bộ TP. 2. POST. | (1) **HTTP 403** (deterministic — KHÔNG accept silent override 200). (3) Toast/page: **"Bạn không có quyền xem báo cáo này"** (ERR-RPT-05). KHÔNG có data Bộ TP trong response. Silent override scope = FAIL (security IDOR). | Permission 🔴 (security) |
| TC-BC-PERM-013 | BR-AUTH-08 / BN + CB_PD_BN | CB_PD_BN chỉ thấy BN mình | cb_pd_bn_01 login. | ky=THANG | 1. Chọn BC VV đã tiếp nhận. 2. [Xem]. | (3) Chỉ VV thuộc Bộ KH&ĐT. | Permission 🟡 |

---

## C. POSITIVE — ĐP chỉ thấy ĐP mình

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|---------|--------------|----------------|-----------|-------------------|------------------|------|
| TC-BC-PERM-020 | BR-AUTH-08 / ĐP scope | CB_NV_DP chỉ thấy ĐP mình | cb_nv_dp_01 login (Sở TP AG). HD: 3 Sở TP AG + 4 Sở TP BG. | ky=THANG | 1. Chọn BC HD. 2. [Xem]. | (3) tong_hoi_dap=3. KHÔNG thấy Sở TP BG. | Permission 🔴 |
| TC-BC-PERM-021 | BR-AUTH-08 / DP và BN không thấy nhau | DP không thấy BN parent | cb_nv_dp_01 (Sở TP AG, thuộc Bộ TP) login. HD: 5 Bộ TP (BN parent). | ky=THANG | 1. [Xem]. | (3) **DP không thấy BN parent** (per srs-fr-11:79 "BN và ĐP ngang cấp song song"). tong_hoi_dap=0 nếu chỉ có data Bộ TP. | Permission 🔴 |
| TC-BC-PERM-022 | SCR-IX-01 row#5 | Dropdown đơn vị locked cho CB_NV_DP | cb_nv_dp_01 login. | — | 1. Open dropdown đơn vị. | (3) Dropdown disabled hoặc chỉ "Sở TP AG". | Permission 🔴 |
| TC-BC-PERM-023 | BR-AUTH-08 / DP + CB_PD / A6 G3 fill | CB_PD_DP locked ĐP mình | cb_pd_dp_01 login (Sở TP AG). HD: 3 Sở TP AG + 4 Sở TP BG. | ky=THANG | 1. Chọn BC HD. 2. [Xem]. | (3) tong_hoi_dap=3 (chỉ Sở TP AG). KHÔNG thấy Sở TP BG. Dropdown đơn vị locked. | Permission 🟡 |

---

## D. NEGATIVE — Không có quyền

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|---------|--------------|----------------|-----------|-------------------|------------------|------|
| TC-BC-PERM-030 | E7 ERR-RPT-05 (NHT) | NHT không có quyền xem BC | nht_01 login. | — | 1. Truy cập `/bao-cao` URL trực tiếp. | (1) 403. (3) Toast "Bạn không có quyền xem báo cáo này" (ERR-RPT-05). Sidebar không có mục "Báo cáo thống kê". | Permission 🔴 |
| TC-BC-PERM-031 | E7 ERR-RPT-05 (TVV) | TVV không có quyền | tvv_01 login. | — | 1. URL `/bao-cao`. | (1) 403. | Permission 🟡 |
| TC-BC-PERM-032 | E7 ERR-RPT-05 (CG) | CG không có quyền | cg_01 login. | — | 1. URL `/bao-cao`. | (1) 403. | Permission 🟡 |
| TC-BC-PERM-033 | E7 ERR-RPT-05 (DN) | DN không có quyền | dn_01 login. | — | 1. URL `/bao-cao`. | (1) 403. | Permission 🟡 |
| TC-BC-PERM-034 | E7 ERR-RPT-05 (GV) | GV không có quyền | gv_01 login. | — | 1. URL `/bao-cao`. | (1) 403. | Permission 🟢 |

---

## E. EDGE — QTHT bypass + cross-scope

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|---------|--------------|----------------|-----------|-------------------|------------------|------|
| TC-BC-PERM-040 | BR-AUTH-08 / QTHT bypass / SPEC-CLARIFY-BC-03 | QTHT bypass scope (theo SRS ngoại lệ srs-fr-11:1262) | qtht_01 login. HD ở 3 đơn vị TW+BN+ĐP. | — | 1. Truy cập SCR-IX-01. 2. Chọn BC HD. | (3) **SPEC-CLARIFY-BC-03**: 2 hành vi possible — (a) QTHT thấy toàn quốc giống TW (bypass), hoặc (b) QTHT bị 403 vì BC không phải module QTHT. Verify thực tế + log. | Edge 🟢 |
| TC-BC-PERM-041 | BR-AUTH-08 / Export scope | Export Excel cũng tuân thủ scope | cb_nv_dp_01 login. HD: 3 ĐP + 5 BN. | format=XLSX | 1. Chạy BC HD. 2. Xuất Excel. | (3) File chỉ chứa 3 record ĐP. KHÔNG có BN data leak vào file. | Permission 🔴 |

---

## Tổng kết file 03-TC

- **19 TC**: 1 A0 unauthenticated (Codex F-03) + 4 A + 4 B + 4 C + 5 D + 2 E.
- **Critical TC (🔴)**: PERM-000, 001, 010, 011, 012, 013, 020, 021, 022, 030, 041.
- **Security TC**: PERM-000 (unauth redirect), PERM-012 (cross-attempt API hard 403), PERM-041 (export scope leak).
- **SPEC-CLARIFY ref**: BC-03 (PERM-040 QTHT bypass).
- **A6 inline merged 2026-05-10**: TC-BC-PERM-023 (CB_PD_DP fill G3).
- **Codex review applied 2026-05-10**: F-03 (PERM-000 unauth NEW), F-05 (PERM-012 hard 403), F-09 (PERM-023 confirmed).

*Generated 2026-05-10 — Phase A step A3 (BMAD generate-e2e-tests)*
