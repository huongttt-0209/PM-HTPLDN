# Test Cases — FR-I-05..07: KPI Khóa học + TVV (UC5-UC7)

> **SRS Ref**: FR-I-05, FR-I-06, FR-I-07 (`srs-fr-01-dashboard-v3.1.md` line 330-403)
> **Ngày tạo**: 2026-05-10 (Phase A3 + A4 merged)
> **Đặc thù**: KPI-05 (KH `DANG_DIEN_RA` ảnh chụp) + KPI-06 (KH `DA_KET_THUC` `ngay_ket_thuc` trong kỳ) + KPI-07 (TVV `DANG_HOAT_DONG` ảnh chụp). KPI-07 default user TW = L1 'DP' + L2 'Tất cả ĐP' (SRS line 397). KPI-05/07 KHÔNG dùng khoảng thời gian (ảnh chụp tại cuối kỳ).

---

## Quy ước

- **Priority**: 🔴 P0 (critical) · 🟡 P1 (high) · 🟢 P2 (medium)
- **TraceID**: `FR-I-{NN} / {section}` link SRS line/heading
- **Pre-conditions mặc định**: User đã login + `DASHBOARD_VIEW`

---

## Drill-down URL spec

| KPI | URL spec |
|-----|----------|
| KPI-05 | `/dao-tao/khoa-hoc?trang_thai=DANG_DIEN_RA&don_vi_cap={don_vi_cap}&don_vi_id={don_vi_id}` (SRS line 343) — KHÔNG kèm time params |
| KPI-06 | `/dao-tao/khoa-hoc?trang_thai=DA_KET_THUC&date_field=ngay_ket_thuc&nam={nam}&thang={thang}&don_vi_cap={don_vi_cap}&don_vi_id={don_vi_id}` (SRS line 366) |
| KPI-07 | `/chuyen-gia-tvv/danh-sach?trang_thai=DANG_HOAT_DONG&don_vi_cap={don_vi_cap}&don_vi_id={don_vi_id}` (SRS line 392) — KHÔNG kèm time params |

---

## A. KPI-05..07 — HAPPY

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|---------|---------------|----------------|-----------|-------------------|------------------|------|
| TC-DASH-030 | FR-I-05 / Processing step 4 + AC#1 | KPI-05 đếm KH `DANG_DIEN_RA` (ảnh chụp) | cb_nv_tw_01 login. Có ≥3 KH `DANG_DIEN_RA` thuộc TW (chế độ DP default). | Default | 1. Vào `/dashboard`. 2. Quan sát KPI-05 "Khóa đào tạo / tập huấn đang diễn ra". | (1) `gia_tri` = COUNT KH `DANG_DIEN_RA` thuộc phạm vi (DP scope). (2) `don_vi_tinh="khóa"`. (3) Chú thích phụ "Tính đến hôm nay (DD/MM/YYYY)". (4) Áp BR-AUTH-08. | Happy 🔴 |
| TC-DASH-031 | FR-I-06 / Processing step 4 | KPI-06 đếm KH `DA_KET_THUC` `ngay_ket_thuc` trong kỳ | cb_nv_tw_01 login. Có ≥2 KH `DA_KET_THUC` `ngay_ket_thuc` ∈ kỳ. | Default kỳ hiện tại | 1. Vào `/dashboard`. 2. Quan sát KPI-06. | (1) `gia_tri` = COUNT KH `DA_KET_THUC` & `ngay_ket_thuc` ∈ kỳ. (2) Filter ngày phát sinh. | Happy 🔴 |
| TC-DASH-032 | FR-I-07 / Processing step 4 + AC#1 (SRS line 390) — Codex P1-1 patched (cover đủ 8 trạng thái loại trừ exhaustive) | KPI-07 đếm TVV `DANG_HOAT_DONG` — exhaustive verify cả 8 trạng thái loại trừ | cb_nv_tw_01 login. Seed data đủ 9 trạng thái TVV thuộc DP scope: **DANG_HOAT_DONG (5)**, MOI_DANG_KY (2), CHO_THAM_DINH (3), DANG_THAM_DINH (1), YEU_CAU_BO_SUNG (2), CHO_PHE_DUYET (1), TU_CHOI (2), TAM_DUNG (2), VO_HIEU_HOA (1). Tổng 19 TVV nhưng chỉ 5 ở DANG_HOAT_DONG. | Default user TW (L1='DP', L2='Tất cả ĐP') | 1. Vào `/dashboard`. 2. Quan sát KPI-07 `gia_tri`. 3. (DB verify optional): COUNT WHERE trang_thai='DANG_HOAT_DONG' AND đơn vị thuộc DP scope. | (1) `gia_tri` = **5** (chỉ TVV `DANG_HOAT_DONG` thuộc DP scope). (2) KHÔNG bao gồm 8 trạng thái loại trừ — verify từng trạng thái KHÔNG đóng góp count: MOI_DANG_KY (2 không đếm), CHO_THAM_DINH (3 không đếm), DANG_THAM_DINH (1 không đếm), YEU_CAU_BO_SUNG (2 không đếm), CHO_PHE_DUYET (1 không đếm), TU_CHOI (2 không đếm), TAM_DUNG (2 không đếm), VO_HIEU_HOA (1 không đếm). Tổng `gia_tri` = 5, KHÔNG phải 19. (SRS line 390 quote 8 trạng thái loại trừ chính xác). (3) Default user TW: L1='DP', L2='Tất cả ĐP' (SRS line 397). | Happy 🔴 |
| TC-DASH-033 | FR-I-07 / AC#3 (SRS line 397) | KPI-07 default user TW vừa login = L1='DP' + L2='Tất cả ĐP' | cb_nv_tw_01 login lần đầu (clear cookie/state). | — | 1. Login. 2. Vào `/dashboard`. 3. Inspect bộ lọc default. | (1) L1 dropdown selected="Địa phương". (2) L2 dropdown selected="Tất cả địa phương". (3) Chip phạm vi "Phạm vi: Tất cả địa phương". (4) KPI-07 chỉ đếm TVV thuộc các ĐP, KHÔNG đếm TVV BN/TW (SRS line 397). | Happy 🔴 |
| TC-DASH-034 | FR-I-05 / Drill-down (SRS line 343) | KPI-05 click → URL params không kèm time | cb_nv_tw_01 login. KPI-05=3 KH. | Year=2026, Month=4 | 1. Click KPI-05. | URL = `/dao-tao/khoa-hoc?trang_thai=DANG_DIEN_RA&don_vi_cap=DP&don_vi_id=`. KHÔNG có `nam` / `thang` trong URL (KPI-05 ảnh chụp). | Happy 🟡 |
| TC-DASH-035 | FR-I-06 / Drill-down (SRS line 366) | KPI-06 click → URL params có `date_field=ngay_ket_thuc` + time | cb_nv_tw_01 login. | nam=2026, thang=4 | 1. Click KPI-06. | URL = `/dao-tao/khoa-hoc?trang_thai=DA_KET_THUC&date_field=ngay_ket_thuc&nam=2026&thang=4&don_vi_cap=DP&don_vi_id=`. | Happy 🟡 |
| TC-DASH-036 | FR-I-07 / Drill-down (SRS line 392) | KPI-07 click → URL params không kèm time | cb_nv_tw_01 login. | nam=2026, thang=4 | 1. Click KPI-07. | URL = `/chuyen-gia-tvv/danh-sach?trang_thai=DANG_HOAT_DONG&don_vi_cap=DP&don_vi_id=`. KHÔNG có time params (KPI-07 ảnh chụp). | Happy 🟡 |
| TC-DASH-037 | FR-I-07 / AC#5 (SRS line 399) | User TW chọn L1='BN' + L2='Tất cả' → KPI-07 đếm TVV BN | cb_nv_tw_01 login. Có 4 TVV `DANG_HOAT_DONG` thuộc BN (BTC + BKH). | L1='BN', L2='Tất cả Bộ ngành' | 1. Đổi L1 sang Bộ ngành. 2. L2 reset = "Tất cả Bộ ngành" (pending). 3. Click Áp dụng. | KPI-07 = 4 (chỉ TVV BN, KHÔNG đếm TVV ĐP). Chip phạm vi "Phạm vi: Tất cả bộ ngành". | Happy 🟡 |
| TC-DASH-038 | FR-I-07 / AC#7 (SRS line 401, BR-AUTH-08) | User BN/ĐP login → KPI-07 lock theo đơn vị user | cb_nv_dp_01 (Sở TP AG) login. AG có 2 TVV `DANG_HOAT_DONG`. BG có 5. | Auto-locked | 1. Login. 2. Vào `/dashboard`. | (1) L1 locked='DP', L2 locked='Sở TP An Giang' (SRS line 770). (2) KPI-07 = 2 (chỉ AG). (3) KHÔNG đếm BG (BR-AUTH-08). | Happy 🔴 |
| TC-DASH-039 | FR-I-05..07 / TPL Outputs#11 | Xu hướng GIAM hiển thị đúng | cb_nv_tw_01 login. KPI-06 kỳ này=2, kỳ trước=4. | nam=2026, thang=4 | 1. Apply filter. 2. Quan sát trend KPI-06. | (1) `huong_tang_giam=GIAM`. (2) `xu_huong_phan_tram=-50,0%`. (3) UI: ↓ "−50,0%" màu đỏ. | Happy 🟡 |

---

## B. KPI-05..07 — NEGATIVE

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|---------|---------------|----------------|-----------|-------------------|------------------|------|
| TC-DASH-042 | FR-I-05..07 / E1 INFO-DASH-01 | Không có TVV `DANG_HOAT_DONG` → "0" + "Chưa có dữ liệu trong kỳ" | cb_nv_dp_01 login. Đơn vị X có 0 TVV `DANG_HOAT_DONG`. | nam=2026, thang=hiện tại | 1. Vào `/dashboard`. 2. Quan sát KPI-07. | (1) `gia_tri=0`. (2) UI text "0" + "Chưa có dữ liệu trong kỳ". (3) Trend "—". | Negative 🟡 |
| TC-DASH-043 | FR-I-05..07 / E2 INFO-DASH-04 | Audit log thiếu kỳ trước cho KPI ảnh chụp | cb_nv_tw_01 login. Audit log thiếu snapshot tại boundary cuối kỳ trước cho KPI-05. | Năm = năm bắt đầu sd phần mềm | 1. Apply filter. 2. Observe trend. | (1) `xu_huong_phan_tram=NULL`. (2) UI "—" + tooltip "Chưa đủ dữ liệu lịch sử để so sánh". | Negative 🟡 |

---

## C. KPI-05..07 — EDGE (A4 merged)

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|---------|---------------|----------------|-----------|-------------------|------------------|------|
| TC-DASH-045 | FR-I-07 / AC#2 (SRS line 396) (A4 merged) | TVV transition `DANG_HOAT_DONG` → `TAM_DUNG` → KPI-07 giảm sau auto-refresh | cb_nv_tw_01 login. KPI-07 đang = 5 (đã load). | Trigger TVV X transition lúc t=10s | 1. Vào `/dashboard` (KPI-07=5). 2. Sysop transition TVV X từ DANG_HOAT_DONG → TAM_DUNG. 3. Đợi auto-refresh tick (60s). HOẶC click "Làm mới". | KPI-07 cập nhật = 4 (giảm 1). KHÔNG cập nhật real-time, chỉ sau tick / manual refresh (SRS line 396 quote: "Không cập nhật theo thời gian thực"). | Edge 🔴 |
| TC-DASH-046 | FR-I-05 / Processing step 3 (A4 merged) | KPI-05 ảnh chụp tại cuối kỳ đã đóng vs hiện tại | cb_nv_tw_01 login. KH X transition `DA_DUYET` → `DANG_DIEN_RA` tại 2026-03-01. KH X transition `DANG_DIEN_RA` → `DA_KET_THUC` tại 2026-04-15. | (a) nam=2026, thang=3 / (b) nam=2026, thang=4 / (c) nam=2026, thang=5 hiện tại | 1. Apply 3 filter scenario. 2. Quan sát KPI-05. | (a) Tháng 3: KH X `DANG_DIEN_RA` cuối tháng → đếm. (b) Tháng 4: KH X tại cuối tháng `DA_KET_THUC` → KHÔNG đếm. (c) Hiện tại: KHÔNG đếm. (3 ảnh chụp khác nhau cùng KH). | Edge 🔴 |
| TC-DASH-047 | FR-I-07 / SRS line 397 (A4 merged) | User TW default DP → manual switch BN → switch back DP | cb_nv_tw_01 login. Có 5 TVV ĐP + 4 TVV BN active. | — | 1. Login (KPI-07=5 ĐP). 2. Switch L1=BN, Apply (KPI-07=4 BN). 3. Switch L1=DP, Apply (KPI-07=5 ĐP). | Filter state đổi đúng + KPI-07 đếm tương ứng. (Chip phạm vi đổi mỗi step). | Edge 🟡 |
| TC-DASH-048 | FR-I-06 / Boundary date end-of-month (A4 merged) | KPI-06 boundary `ngay_ket_thuc` = ngày cuối tháng vs đầu tháng tiếp | cb_nv_tw_01 login. KH A `ngay_ket_thuc=2026-03-31 23:59`. KH B `ngay_ket_thuc=2026-04-01 00:00`. | nam=2026, thang=3 | 1. Apply filter. 2. Quan sát KPI-06. | KPI-06 đếm chỉ KH A (boundary cuối tháng inclusive: tu_ngay=2026-03-01 00:00, den_ngay=2026-03-31 23:59). KH B KHÔNG đếm. | Edge 🟡 |
| TC-DASH-049 | FR-I-07 / Drill-down + AC#9 (A4 merged) | Drill-down KPI-07 với cb_nv_dp_01 (locked) — URL có `don_vi_id` của user | cb_nv_dp_01 (AG) login. | Auto-locked DP+AG | 1. Click KPI-07. | URL = `/chuyen-gia-tvv/danh-sach?trang_thai=DANG_HOAT_DONG&don_vi_cap=DP&don_vi_id={AG_ID}` (BR-AUTH-08). Module target tự apply scope. | Edge 🟡 |

---

## E. A6 fill (gap A5)

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|---------|---------------|----------------|-----------|-------------------|------------------|------|
| TC-DASH-217 | FR-I-06 / AC#2 (SRS line 370) BR-AUTH-08 (A6 fill) | KPI-06 — CB BN/ĐP scope KH `DA_KET_THUC` chỉ đếm KH thuộc đơn vị user | cb_nv_dp_01 (Sở TP AG) login. AG có 3 KH `DA_KET_THUC` `ngay_ket_thuc` ∈ tháng 4. BG có 5 KH `DA_KET_THUC` cùng kỳ. | nam=2026, thang=4 | 1. Vào `/dashboard`. 2. Quan sát KPI-06. | (1) `gia_tri=3` (chỉ AG). (2) KHÔNG đếm 5 KH BG (BR-AUTH-08). (3) Chip phạm vi "Phạm vi: Sở Tư pháp An Giang". | Happy 🔴 |
| TC-DASH-218 | FR-I-07 / AC#6 (SRS line 400) (A6 fill) | KPI-07 — TW chọn 1 đơn vị cụ thể → đếm TVV `DANG_HOAT_DONG` thuộc đơn vị đó | cb_nv_tw_01 login. ĐP X có 4 TVV `DANG_HOAT_DONG`. Tất cả ĐP khác có total 30 TVV. | L1='DP', L2=ĐP X | 1. Login (default L1=DP, L2='Tất cả ĐP'). 2. Đổi L2 sang ĐP X. Apply. 3. Quan sát KPI-07. | (1) `gia_tri=4` (chỉ ĐP X). (2) Chip phạm vi "Phạm vi: {tên ĐP X}". (3) KHÔNG đếm 30 TVV của ĐP khác (SRS line 400 quote: "User TW chọn 1 đơn vị cụ thể → chỉ đếm tư vấn viên thuộc đơn vị đó"). | Happy 🔴 |
| TC-DASH-219 | FR-I-07 / AC#7 (SRS line 401) BR-AUTH-08 (A6 fill) | KPI-07 — User BN locked → chỉ đếm TVV thuộc BN của user | cb_nv_bn_01 (BKH) login. BKH có 6 TVV `DANG_HOAT_DONG`. BTC có 4 TVV. | Auto-locked L1='BN', L2='BKH' | 1. Login (BN locked). 2. Vào `/dashboard`. 3. Quan sát KPI-07 + chip phạm vi. | (1) L1 locked='BN', L2 locked='BKH' (per Permission Matrix line 878). (2) `gia_tri=6` (chỉ BKH). (3) KHÔNG đếm 4 TVV BTC (BR-AUTH-08 + BR-AUTH-03 ngang cấp BN). (4) Chip "Phạm vi: Bộ Kế hoạch và Đầu tư". | Happy 🟡 |

---

## F. TPL-DASH-KPI Outputs verify — KPI-05..07 (Codex P1-2 fill)

> Verify 12 outputs TPL-DASH-KPI (SRS line 198-213) cho từng KPI: `gia_tri`, `nhan`, `don_vi_tinh`, `drill_down_url`, `nam`, `thang`, `scope_label`, `tu_ngay_boundary`, `den_ngay_boundary`, `is_qua_khu_dong`, `xu_huong_phan_tram`, `huong_tang_giam`.

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|---------|---------------|----------------|-----------|-------------------|------------------|------|
| TC-DASH-228 | FR-I-05 / TPL-DASH-KPI Outputs + ảnh chụp (Codex P1-2 fill) | KPI-05 — verify đủ 12 outputs (KPI ảnh chụp `DANG_DIEN_RA`) + chú thích "Tính đến ..." | cb_nv_tw_01 login. ≥1 KH `DANG_DIEN_RA`. Kỳ hiện tại = năm/tháng hiện tại. | Default kỳ hiện tại | 1. Vào `/dashboard`. 2. Network → response endpoint KPI-05. 3. Verify UI chú thích "Tính đến hôm nay (DD/MM/YYYY)" (SRS line 794). | Response chứa **12 fields**: (1) `gia_tri`=COUNT KH `DANG_DIEN_RA`; (2) `nhan`="Khóa đào tạo / tập huấn đang diễn ra"; (3) `don_vi_tinh`="khóa"; (4) `drill_down_url` chứa `/dao-tao/khoa-hoc?trang_thai=DANG_DIEN_RA&don_vi_cap=DP&don_vi_id=...` (KHÔNG có nam/thang vì ảnh chụp — SRS line 343); (5) `nam`=current; (6) `thang`=current; (7) `scope_label`; (8) `tu_ngay_boundary`; (9) `den_ngay_boundary`= NOW; (10) `is_qua_khu_dong`=false; (11) `xu_huong_phan_tram`; (12) `huong_tang_giam`. **UI chú thích**: "Tính đến hôm nay (DD/MM/YYYY)" (SRS line 794 ảnh chụp). | Behavior 🔴 |
| TC-DASH-229 | FR-I-06 / TPL-DASH-KPI Outputs + KPI phát sinh (Codex P1-2 fill) | KPI-06 — verify đủ 12 outputs (KPI phát sinh trong kỳ + KHÔNG có chú thích "Tính đến ...") | cb_nv_tw_01 login. ≥3 KH `DA_KET_THUC` `ngay_ket_thuc` ∈ tháng 4/2026. | nam=2026, thang=4 | 1. Vào `/dashboard`. 2. Network → KPI-06. 3. Verify UI **KHÔNG** có chú thích "Tính đến ..." (SRS line 797). | Response 12 fields: (1) `gia_tri`=COUNT; (2) `nhan`="Khóa đào tạo / tập huấn đã hoàn thành"; (3) `don_vi_tinh`="khóa"; (4) `drill_down_url` chứa `/dao-tao/khoa-hoc?trang_thai=DA_KET_THUC&date_field=ngay_ket_thuc&nam=2026&thang=4&don_vi_cap=...&don_vi_id=...` (CÓ nam+thang vì phát sinh trong kỳ); (5-12) đầy đủ. **UI**: KHÔNG có chú thích phụ "Tính đến ..." (SRS line 797 quote: "KPI phát sinh trong kỳ không có chú thích phụ"). | Behavior 🔴 |
| TC-DASH-230 | FR-I-07 / TPL-DASH-KPI Outputs + ảnh chụp + locked user (Codex P1-2 fill) | KPI-07 — verify đủ 12 outputs khi user BN locked | cb_nv_bn_01 (BKH) login. ≥2 TVV `DANG_HOAT_DONG` thuộc BKH. | Auto-locked L1='BN', L2='BKH' | 1. Login BN. 2. Vào `/dashboard`. 3. Network → KPI-07. 4. Verify L1/L2 locked + 12 outputs. | Response 12 fields: (1) `gia_tri`=COUNT BKH-only; (2) `nhan`="Chuyên gia / Tư vấn viên đang hoạt động"; (3) `don_vi_tinh`="người"; (4) `drill_down_url` chứa `/chuyen-gia-tvv/danh-sach?trang_thai=DANG_HOAT_DONG&don_vi_cap=BN&don_vi_id={BKH_id}` (locked, KHÔNG có nam/thang); (5-12) đầy đủ. **UI chú thích**: "Tính đến hôm nay (DD/MM/YYYY)" (SRS line 794, KPI-07 ảnh chụp). **Filter L1/L2 locked** = không edit được (Permission Matrix P3 line 878). | Behavior 🔴 |

---

## Tổng kết file 02-TC

- **Tổng số TC: 22** (10 Happy + 2 Negative + 5 Edge + 3 A6 fill + 3 Codex P1-2 fill — A4 + A6 + Codex merged inline)
- **Critical TC (🔴)**: TC-DASH-030, 031, 032, 033, 038, 045, 046, 217, 218, 228, 229, 230
- **A4 merged 2026-05-10**: TC-DASH-045..049 (TVV transition mid-tick + ảnh chụp boundary semantic + KPI-07 default switch + boundary inclusive end-of-month + drill-down locked)
- **A6 fill 2026-05-10**: TC-DASH-217 (KPI-06 BN/ĐP scope) + TC-DASH-218 (KPI-07 TW chọn 1 ĐV) + TC-DASH-219 (KPI-07 BN locked) — fill GAP-1, GAP-2, GAP-6
- **Codex 2026-05-10 P1-1 patched**: TC-DASH-032 mở rộng cover **đủ 8 trạng thái loại trừ** TVV (was 3/8) — exhaustive verify per SRS line 390
- **Codex 2026-05-10 P1-2 fill**: TC-DASH-228 (KPI-05 outputs ảnh chụp) + TC-DASH-229 (KPI-06 outputs phát sinh) + TC-DASH-230 (KPI-07 outputs locked user)
- **SPEC-CLARIFY refs**: (none new — KPI 5/6/7 spec rất rõ)
- **Drill-down**: chỉ verify URL params, KHÔNG vào module target

*Generated 2026-05-10 — Phase A3 + A4 + A6 merged + Codex P1-1/P1-2 patched*
