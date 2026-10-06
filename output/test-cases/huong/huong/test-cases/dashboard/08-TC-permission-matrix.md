# Test Cases — Permission Matrix 8 quyền × 12 vai trò

> **SRS Ref**: SCR-I-01 Permission Matrix (`srs-fr-01-dashboard-v3.1.md` line 870-889), BR-AUTH-01/03/04/08 (line 1129-1151)
> **Ngày tạo**: 2026-05-10 (Phase A3 + A4 merged)
> **Đặc thù**:
> - 8 quyền: P1 VIEW_DASHBOARD / P2 FILTER_TIME / P3 FILTER_CHANGE_SCOPE / P4 MANUAL_REFRESH / P5 DRILL_DOWN_HOIDAP / P6 DRILL_DOWN_VUVIEC / P7 DRILL_DOWN_KHOAHOC / P8 DRILL_DOWN_TVV.
> - 12 vai trò: QTHT, CB_NV_TW, CB_NV_BN, CB_NV_DP, CB_PD_TW, CB_PD_BN, CB_PD_DP, DN, NHT, TVV, CG.
> - DN/NHT/TVV/CG: P1=✗ → các P2-P8 đương nhiên `—` (không vào được dashboard) → redirect trang chủ theo vai trò.
> - 7 vai trò có quyền: QTHT, CB_NV_TW/BN/DP, CB_PD_TW/BN/DP. P3 lock theo cấp đơn vị. P5-P8 ✓* (data scope theo BR-AUTH-08 ở module target — chỉ verify URL truyền filter đúng).
> - BR-AUTH-04: TW thấy cấp con (BN + ĐP). BN/ĐP ngang cấp song song (KHÔNG cấp con).
> - BR-AUTH-03: ngang cấp không thấy nhau (BN ≠ ĐP, DP ≠ DP khác).

---

## Quy ước

- **Priority**: 🔴 P0 (critical) · 🟡 P1 (high) · 🟢 P2 (medium)
- **TraceID**: `Permission / P{N} / {role}` link SRS line 876-883

---

## Account Map (per Permission Matrix SCR-I-01)

| Vai trò | Username (primary) | Đơn vị |
|---------|--------------------|--------|
| QTHT | `qtht_01` | (no don_vi_id, see all) |
| CB_NV_TW | `cb_nv_tw_01` | BTP-TW |
| CB_NV_BN | `cb_nv_bn_01` | BKH (Bộ KH&ĐT) |
| CB_NV_DP | `cb_nv_dp_01` | STP-AG (Sở TP An Giang) |
| CB_NV_DP (cross) | `cb_nv_dp_02` | STP-BG (Sở TP Bắc Giang) |
| CB_PD_TW | `cb_pd_tw_01` | BTP-TW |
| CB_PD_BN | `cb_pd_bn_01` | BKH |
| CB_PD_DP | `cb_pd_dp_01` | STP-AG |
| DN | `dn_01` | (Cổng DN — không có DASHBOARD_VIEW) |
| NHT | `nht_01` | (Form public — không có DASHBOARD_VIEW) |
| TVV | `tvv_01` | (Form public — không có DASHBOARD_VIEW) |
| CG | `cg_01` | (Form public — không có DASHBOARD_VIEW) |

---

## A. P1 VIEW_DASHBOARD — HAPPY (vai trò có quyền)

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|---------|---------------|----------------|-----------|-------------------|------------------|------|
| TC-DASH-180 | Permission / P1 / QTHT | qtht_01 vào `/dashboard` thành công | qtht_01 login. | — | 1. Vào `/dashboard`. | (1) SCR-I-01 render đầy đủ. (2) Bộ lọc L1+L2 KHÔNG locked (QTHT có thể đổi tự do per SRS line 728 + 887 quote "QTHT ngoại lệ — có thể xem tất cả cấp không giới hạn"). | Happy 🔴 |
| TC-DASH-181 | Permission / P1 / CB_NV_TW + CB_PD_TW | cb_nv_tw_01 + cb_pd_tw_01 vào dashboard | cb_nv_tw_01 / cb_pd_tw_01 login. | — | 1. Vào `/dashboard`. | (1) SCR-I-01 render. (2) Bộ lọc L1+L2 KHÔNG locked (TW có thể đổi). (3) Default L1='DP', L2='Tất cả ĐP'. | Happy 🔴 |
| TC-DASH-182 | Permission / P1 / CB_NV_BN + CB_PD_BN | cb_nv_bn_01 + cb_pd_bn_01 vào dashboard, locked BN | cb_nv_bn_01 / cb_pd_bn_01 login. | — | 1. Vào `/dashboard`. 2. Inspect dropdown L1+L2. | (1) SCR-I-01 render. (2) L1 locked='BN' (`locked=BN user` per matrix line 878). (3) L2 locked = đơn vị BN của user (vd BKH). (4) Chip "Phạm vi: {tên BN}". | Happy 🔴 |
| TC-DASH-183 | Permission / P1 / CB_NV_DP + CB_PD_DP | cb_nv_dp_01 + cb_pd_dp_01 vào dashboard, locked DP | cb_nv_dp_01 / cb_pd_dp_01 login. | — | 1. Vào `/dashboard`. 2. Inspect dropdown. | (1) L1 locked='DP'. (2) L2 locked = ĐP của user (STP-AG). (3) Chip "Phạm vi: Sở Tư pháp An Giang". | Happy 🔴 |

---

## B. P1 VIEW_DASHBOARD — NEGATIVE (vai trò KHÔNG có quyền — redirect)

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|---------|---------------|----------------|-----------|-------------------|------------------|------|
| TC-DASH-185 | Permission / P1 / DN (SRS line 685) | dn_01 vào `/dashboard` URL → redirect Cổng DN | dn_01 login. | URL `/dashboard` trực tiếp | 1. Mở URL. | (1) Redirect về trang chủ Cổng DN (Nhóm VII per SRS line 684). (2) KHÔNG render SCR-I-01. (3) URL change. | Negative 🔴 |
| TC-DASH-186 | Permission / P1 / NHT | nht_01 vào `/dashboard` URL → redirect form public NHT | nht_01 login. | URL `/dashboard` | 1. Mở URL. | Redirect về trang chủ NHT (form public per SRS line 684). KHÔNG render SCR-I-01. | Negative 🔴 |
| TC-DASH-187 | Permission / P1 / TVV | tvv_01 vào `/dashboard` URL → redirect view TVV | tvv_01 login. | URL `/dashboard` | 1. Mở URL. | Redirect về view TVV (vụ việc được phân công per SRS line 684). | Negative 🔴 |
| TC-DASH-188 | Permission / P1 / CG | cg_01 vào `/dashboard` URL → redirect view CG | cg_01 login. | URL `/dashboard` | 1. Mở URL. | Redirect về view CG. | Negative 🔴 |

---

## C. P2-P4 + Drill-down — HAPPY

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|---------|---------------|----------------|-----------|-------------------|------------------|------|
| TC-DASH-190 | Permission / P2 FILTER_TIME / 7 vai trò | 7 vai trò active đều có quyền đổi Năm + Tháng | 7 vai trò (qtht_01, cb_nv_tw_01, cb_nv_bn_01, cb_nv_dp_01, cb_pd_tw_01, cb_pd_bn_01, cb_pd_dp_01) login lần lượt. | — | 1. Vào `/dashboard`. 2. Mở dropdown Năm + Tháng. | Tất cả 7 role đều có thể đổi Năm + Tháng (P2 = ✓ cho tất cả 7 role per matrix line 877). | Happy 🟡 |
| TC-DASH-191 | Permission / P3 FILTER_CHANGE_SCOPE / locked behavior | BN/DP locked, TW/QTHT free | 4 role locked (cb_nv_bn_01, cb_nv_dp_01, cb_pd_bn_01, cb_pd_dp_01) + 3 free (qtht_01, cb_nv_tw_01, cb_pd_tw_01). | — | 1. 7 role login lần lượt. 2. Try đổi L1+L2. | (1) qtht_01, cb_nv_tw_01, cb_pd_tw_01: L1+L2 đổi tự do. (2) cb_nv_bn_01, cb_pd_bn_01: locked='BN user' (đơn vị BN). (3) cb_nv_dp_01, cb_pd_dp_01: locked='DP user' (đơn vị DP). (Per matrix line 878). | Happy 🔴 |
| TC-DASH-192 | Permission / P4 MANUAL_REFRESH / 7 vai trò | 7 vai trò đều click "Làm mới" được | 7 role login lần lượt (kỳ hiện tại). | — | 1. Vào `/dashboard`. 2. Click "Làm mới". | Tất cả 7 role click được — button trigger reload 12 widget. (P4 = ✓ per matrix line 879). | Happy 🟢 |
| TC-DASH-193 | Permission / P5 DRILL_DOWN_HOIDAP / URL truyền filter | Click KPI-01 → URL có filter đúng | cb_nv_dp_01 (locked AG) login. | — | 1. Vào `/dashboard`. 2. Click KPI-01. | URL = `/hoi-dap/danh-sach?trang_thai=MOI&nam=2026&thang=&don_vi_cap=DP&don_vi_id={AG_ID}` (BR-AUTH-08 — `don_vi_id` của user). KHÔNG test data scope ở module target. | Happy 🟡 |
| TC-DASH-194 | Permission / P5-P8 ✓* / OBS data scope | Drill-down — URL truyền đúng cho 4 link | cb_nv_dp_01 (locked AG) login. | — | 1. Click KPI-01 (P5). 2. Back. Click KPI-02/03/04 (P6). 3. Back. Click KPI-05/06 (P7). 4. Back. Click KPI-07 (P8). | (P5) `/hoi-dap/danh-sach?...don_vi_id=AG`. (P6) `/vu-viec/danh-sach?...don_vi_id=AG`. (P7) `/dao-tao/khoa-hoc?...don_vi_id=AG`. (P8) `/chuyen-gia-tvv/danh-sach?...don_vi_id=AG`. (Per matrix line 880-883). **OBS** data scope ở module target — KHÔNG test sâu, chỉ verify URL params. | Happy 🟡 |

---

## D. BR-AUTH cross-unit verification — EDGE (A4 merged)

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|---------|---------------|----------------|-----------|-------------------|------------------|------|
| TC-DASH-195 | BR-AUTH-08 + BR-AUTH-03 (A4 merged) | cb_nv_dp_01 (AG) KHÔNG đếm vụ việc của cb_nv_dp_02 (BG) | cb_nv_dp_01 (AG) + cb_nv_dp_02 (BG) login khác nhau. AG có 5 VV, BG có 8 VV. | — | 1. cb_nv_dp_01 login → KPI-02 đếm chỉ AG=5. 2. Logout. 3. cb_nv_dp_02 login → KPI-02 đếm chỉ BG=8. | (1) AG user thấy 5 (chỉ AG). (2) BG user thấy 8 (chỉ BG). (3) Cross-unit query = 0 rows (BR-AUTH-03 + BR-AUTH-08). | Edge 🔴 |
| TC-DASH-196 | BR-AUTH-08 + BR-AUTH-03 (A4 merged) | cb_nv_bn_01 (BKH) KHÔNG đếm vụ việc của BTC | cb_nv_bn_01 (BKH) login. BKH có 3 VV, BTC có 5 VV. | — | 1. Vào `/dashboard`. 2. Inspect KPI-02. | KPI-02 = 3 (chỉ BKH). KHÔNG đếm BTC (BR-AUTH-03 ngang cấp BN). | Edge 🔴 |
| TC-DASH-197 | BR-AUTH-04 (A4 merged) | cb_nv_tw_01 (TW) thấy cấp con (BN + ĐP) | cb_nv_tw_01 login. TW có 0 VV trực tiếp. BN1=3, BN2=2. ĐP1=5, ĐP2=4. | L1='DP', L2='Tất cả ĐP' | 1. Vào `/dashboard`. 2. KPI-02. | KPI-02 = 5+4 = 9 (TW thấy tất cả ĐP per BR-AUTH-04 SRS line 1145 quote "TW thấy toàn bộ dữ liệu TW + BN + ĐP"). KHÔNG đếm BN1+BN2 vì L1 đang chọn DP. | Edge 🔴 |
| TC-DASH-198 | BR-AUTH-04 + L1 switch (A4 merged) | TW switch L1='BN' → KPI-02 đếm BN1+BN2 | cb_nv_tw_01 login. | L1='BN', L2='Tất cả BN' | 1. Switch L1=BN. 2. Apply. 3. KPI-02. | KPI-02 = 3+2 = 5 (TW thấy tất cả BN khi switch L1=BN). | Edge 🟡 |
| TC-DASH-199 | Permission / P3 FILTER_CHANGE_SCOPE locked PATCH URL (A4 merged) | Locked user (cb_nv_dp_01) thử PATCH URL params → ignored | cb_nv_dp_01 (AG) login. | URL `/dashboard?don_vi_id=BG_ID` (cố ép sang BG) | 1. Mở URL với `don_vi_id` cross-unit. 2. Inspect filter + data. | (1) URL params don_vi_id ignore (silently fallback về AG đơn vị user — hoặc fallback "Tất cả [cấp L1]" per SRS line 852, nhưng locked user phải giữ đơn vị mình). (2) KPI vẫn đếm AG (BR-AUTH-08). (3) **SPEC-CLARIFY-DASH-05**: SRS không chỉ rõ behavior khi locked user URL có don_vi_id khác — assume locked override URL param. | Edge 🔴 |

---

## E. A6 fill (gap A5)

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|---------|---------------|----------------|-----------|-------------------|------------------|------|
| TC-DASH-223 | Permission / P5 / CB_NV_BN (matrix line 880) (A6 fill) | CB_NV_BN drill-down KPI-01 → URL có `don_vi_cap=BN&don_vi_id={BN}` (BR-AUTH-08) | cb_nv_bn_01 (BKH) login. KPI-01 = 3 HD MOI thuộc BKH. | Auto-locked L1='BN', L2='BKH' | 1. Vào `/dashboard`. 2. Click KPI-01. | (1) URL = `/hoi-dap/danh-sach?trang_thai=MOI&nam=2026&thang=&don_vi_cap=BN&don_vi_id={BKH_ID}` (P5 ✓* per matrix line 880). (2) `don_vi_id` của BN user (BKH) auto-fill từ locked filter. (3) **OBS** data scope ở module target — KHÔNG test sâu, chỉ verify URL params truyền đúng. | Happy 🟡 |

---

## F. Permission P5-P8 cho QTHT + CB_PD (Codex P1-3 fill)

> Codex P1-3: P5-P8 chỉ cover cb_nv_dp; QTHT và CB_PD drill-down chưa rõ. Thêm 4 TC explicit cho QTHT (full scope) + CB_PD_TW/BN/DP (matrix line 880-883).

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|---------|---------------|----------------|-----------|-------------------|------------------|------|
| TC-DASH-231 | Permission / P5-P8 / QTHT (matrix line 876-883 + 887) (Codex P1-3 fill) | QTHT drill-down KPI-01..07 — full scope (không khóa) | qtht_01 login. KPI-01..07 có data ở mọi cấp (TW + BN + ĐP). | Default L1='DP', L2='Tất cả ĐP' (QTHT giống TW per line 728) | 1. Vào `/dashboard`. 2. Click lần lượt KPI-01..07. 3. Verify URL params + redirect target. | (1) **P5** (KPI-01 → `/hoi-dap/danh-sach?trang_thai=MOI&don_vi_cap=DP&don_vi_id=NULL`). (2) **P6** (KPI-02/03/04 → `/vu-viec/danh-sach?...&don_vi_cap=DP&don_vi_id=NULL`). (3) **P7** (KPI-05/06 → `/dao-tao/khoa-hoc?...`). (4) **P8** (KPI-07 → `/chuyen-gia-tvv/danh-sach?trang_thai=DANG_HOAT_DONG&...`). (5) QTHT có quyền tất cả P1-P8 ✓ (matrix line 876-883). (6) Filter L1/L2 KHÔNG bị khóa (matrix line 887 quote "QTHT ngoại lệ — có thể xem tất cả cấp không giới hạn"). | Happy 🔴 |
| TC-DASH-232 | Permission / P5-P8 / CB_PD_TW (matrix line 880-883) (Codex P1-3 fill) | CB_PD_TW drill-down KPI-01..07 — same scope as CB_NV_TW | cb_pd_tw_01 login. KPI có data mọi cấp. | Default user TW (L1='DP', L2='Tất cả ĐP') | 1. Vào `/dashboard`. 2. Click lần lượt KPI-01, 02, 05, 07. | (1) **P5-P8 ✓** cho CB_PD_TW (matrix cell row CB_PD_TW). (2) URL params identical với CB_NV_TW (vì cùng level TW + filter scope). (3) **OBS** data thấy ở module target = full scope vì TW (BR-AUTH-04 cấp cha thấy cấp con). | Happy 🟡 |
| TC-DASH-233 | Permission / P5-P8 / CB_PD_BN (matrix line 880-883 + 888) (Codex P1-3 fill) | CB_PD_BN drill-down KPI — locked scope BN | cb_pd_bn_01 (BKH) login. | Auto-locked L1='BN', L2='BKH' | 1. Vào `/dashboard`. 2. Click KPI-01, 02, 05, 07. | (1) **P5-P8 ✓*** cho CB_PD_BN — data scope BR-AUTH-08 (matrix cell `✓*` line 880-883). (2) URL params: `don_vi_cap=BN&don_vi_id={BKH_ID}` auto-locked. (3) Redirect 200 OK đến module target — không bị 403 (vì có quyền VIEW). (4) **OBS** ở module target chỉ thấy data BKH (BR-AUTH-08 + BR-AUTH-03 ngang cấp). | Happy 🟡 |
| TC-DASH-234 | Permission / P5-P8 / CB_PD_DP (matrix line 880-883 + 888) (Codex P1-3 fill) | CB_PD_DP drill-down KPI — locked scope DP | cb_pd_dp_01 (AG) login. | Auto-locked L1='DP', L2='AG' | 1. Vào `/dashboard`. 2. Click KPI-01, 02, 05, 07. 3. Verify URL params + chip phạm vi. | (1) **P5-P8 ✓*** cho CB_PD_DP. (2) URL params: `don_vi_cap=DP&don_vi_id={AG_ID}` auto-locked. (3) Chip phạm vi "Phạm vi: Sở Tư pháp An Giang". (4) **OBS** module target chỉ thấy data AG (BR-AUTH-08 + ngang cấp DP). | Happy 🟡 |

---

## Tổng kết file 08-TC

- **Tổng số TC: 23** (4 Happy P1 + 4 Negative redirect + 5 Happy P2-P5-P8 + 5 Edge BR-AUTH + 1 A6 fill + 4 Codex P1-3 fill)
- **Critical TC (🔴)**: TC-DASH-180, 181, 182, 183, 185, 186, 187, 188, 191, 195, 196, 197, 199, 231
- **A4 merged 2026-05-10**: TC-DASH-195..199 (BR-AUTH-08 cross-unit AG vs BG + BR-AUTH-03 ngang cấp BN + BR-AUTH-04 TW thấy cấp con DP/BN scope + locked URL PATCH override)
- **A6 fill 2026-05-10**: TC-DASH-223 (CB_NV_BN drill-down P5 explicit) — fill GAP-6 Permission
- **Codex 2026-05-10 P1-3 fill**: TC-DASH-231 (QTHT full P5-P8 không khóa) + TC-DASH-232 (CB_PD_TW P5-P8 same as CB_NV_TW) + TC-DASH-233 (CB_PD_BN P5-P8 locked BN) + TC-DASH-234 (CB_PD_DP P5-P8 locked DP)
- **OBS**: TC-DASH-194 — drill-down chỉ verify URL truyền filter đúng, OBS data scope tại module target (BR-AUTH-08 ở module target test riêng).
- **SPEC-CLARIFY refs**:
  - **SPEC-CLARIFY-DASH-05**: SRS không chỉ rõ behavior khi locked user URL có `don_vi_id` cross-unit — assume locked override URL param.

*Generated 2026-05-10 — Phase A3 + A4 + A6 merged (manual edge case hunter + A6 gap fill)*
