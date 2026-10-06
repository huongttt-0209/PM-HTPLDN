# Test Cases — KPI-S-01 + KPI-S-02 — KPI bổ sung Dashboard

> **SRS Ref**: KPI-S-01, KPI-S-02 (`srs-fr-01-dashboard-v3.1.md` line 555-629), Vùng 4 #18-19 (line 808-809), color semantic line 783-789
> **Ngày tạo**: 2026-05-10 (Phase A3 + A4 merged)
> **Đặc thù**:
> - **KPI-S-01** = Σ vụ HT đã từng đi qua YEU_CAU_BO_SUNG (đếm 1 lần/vụ) / Σ vụ HT trong kỳ × 100. Đơn vị `%`.
> - **KPI-S-02** = mean(số ngày làm việc T2-T6, trừ ngày lễ — BR-CALC-03) cho vụ HT trong kỳ. Đơn vị "ngày làm việc", 1 chữ số thập phân.
> - **KHÔNG có drill-down** (SRS line 585, 614 — chỉ số tổng hợp).
> - **KPI ngược chiều** (SRS line 783-789): TANG = đỏ, GIAM = xanh (chất lượng kém hơn / thời gian dài hơn).
> - Mẫu số = 0 → UI "—" + KHÔNG tính xu hướng.

---

## Quy ước

- **Priority**: 🔴 P0 (critical) · 🟡 P1 (high) · 🟢 P2 (medium)
- **TraceID**: `KPI-S-{NN} / {section}` link SRS line/heading
- **Pre-conditions mặc định**: User đã login + `DASHBOARD_VIEW`

---

## A. KPI-S-01..02 — HAPPY

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|---------|---------------|----------------|-----------|-------------------|------------------|------|
| TC-DASH-100 | KPI-S-01 / Processing step 4 + AC#1 (SRS line 588) | KPI-S-01 = 30% (100 HT, 30 từng qua YEU_CAU_BO_SUNG) | cb_nv_tw_01 login. Trong kỳ: 100 vụ HT, 30 vụ trong số đó đã từng đi qua YEU_CAU_BO_SUNG ≥1 lần. | nam=2026, thang=4 | 1. Vào `/dashboard`. 2. Quan sát thẻ KPI-S-01. | (1) `gia_tri=30,0%`. (2) `don_vi_tinh="%"` (SRS line 581 + Vùng 4 line 808). (3) `nhan="Tỷ lệ vụ việc phải bổ sung"`. | Happy 🔴 |
| TC-DASH-101 | KPI-S-01 / AC#2 (SRS line 589) | 1 vụ qua YEU_CAU_BO_SUNG 3 lần → vẫn đếm 1 lần ở tử số | cb_nv_tw_01 login. Có vụ X HT, đã đi qua YEU_CAU_BO_SUNG 3 lần trước khi HT. Tổng kỳ = 10 HT, trong đó 1 (vụ X) qua bổ sung. | Default | 1. Apply. 2. Inspect KPI-S-01. | KPI-S-01 = 1/10 × 100 = 10% (KHÔNG đếm vụ X 3 lần — SRS line 579 quote "đếm 1 lần / vụ — không đếm lặp"). | Happy 🔴 |
| TC-DASH-102 | KPI-S-02 / Processing step 4 + AC#1 (SRS line 617) | KPI-S-02 = 5 (T2 → T2 sau, không lễ) | cb_nv_tw_01 login. 1 vụ tiếp nhận T2 05/01/2026, HT T2 12/01/2026. Không có ngày lễ giữa. | nam=2026, thang=1 | 1. Apply. 2. Inspect KPI-S-02. | (1) Số ngày làm việc đóng góp = 5 (T2,T3,T4,T5,T6 — 5 ngày làm việc per BR-CALC-03 SRS line 1163). (2) `gia_tri=5,0`. (3) `don_vi_tinh="ngày làm việc"`. | Happy 🔴 |
| TC-DASH-103 | KPI-S-01..02 / SRS line 618 (BR-CALC-03) | KPI-S-02 trừ ngày lễ giữa kỳ | cb_nv_tw_01 login. 1 vụ tiếp nhận T2 05/01/2026, HT T2 12/01/2026 nhưng có 1 ngày lễ giữa (vd 08/01 cấu hình holiday). | Default | 1. Apply. 2. Inspect KPI-S-02. | Số ngày làm việc đóng góp = 4 (5 - 1 lễ per SRS line 618 + BR-CALC-03). | Happy 🔴 |
| TC-DASH-104 | KPI-S-02 / Processing step 4 SRS line 608 | KPI-S-02 làm tròn 1 chữ số thập phân | cb_nv_tw_01 login. 3 vụ HT trong kỳ với ngày làm việc: 5, 7, 8 → mean=6,67 → làm tròn 6,7. | Default | 1. Apply. 2. Inspect KPI-S-02. | `gia_tri=6,7` (1 chữ số thập phân per SRS line 608). | Happy 🟡 |
| TC-DASH-105 | KPI-S-01..02 / AC#4 (SRS line 591, BR-AUTH-08) | User BN/ĐP locked → chỉ tính vụ thuộc đơn vị user | cb_nv_dp_01 (AG) login. AG có 5 vụ HT, 1 qua BS. BG có 10 vụ. | Auto-locked | 1. Vào `/dashboard`. 2. Inspect KPI-S-01. | (1) KPI-S-01 = 1/5 × 100 = 20%. (2) KHÔNG tính BG (BR-AUTH-08). | Happy 🔴 |
| TC-DASH-106 | KPI-S-01..02 / SRS line 585+614 | KHÔNG có drill-down (chỉ số tổng hợp) | cb_nv_tw_01 login. KPI-S-01=30%, KPI-S-02=5. | — | 1. Vào `/dashboard`. 2. Click thẻ KPI-S-01 (HOẶC hover xem cursor). 3. Click KPI-S-02. | (1) Click KPI-S-01: KHÔNG navigate (cursor không pointer hoặc click không tác dụng — SRS line 585 quote "không có"). (2) Click KPI-S-02: KHÔNG navigate (SRS line 614). | Happy 🟡 |

---

## B. KPI-S-01..02 — NEGATIVE

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|---------|---------------|----------------|-----------|-------------------|------------------|------|
| TC-DASH-110 | KPI-S-01 / AC#3 (SRS line 590) | Mẫu số = 0 (không có vụ HT trong kỳ) → UI "—" | cb_nv_tw_01 login. Đơn vị X 0 vụ HT trong tháng 1. | nam=2026, thang=1, don_vi_id=X | 1. Apply. 2. Inspect KPI-S-01. | (1) `gia_tri=NULL` (mẫu số = 0). (2) UI hiển thị "—" (SRS line 579 quote "Nếu mẫu số = 0 → giá trị trống (UI hiển thị '—', không tính xu hướng)"). (3) Trend KHÔNG hiển thị. | Negative 🟡 |
| TC-DASH-111 | KPI-S-02 / SRS line 608 + AC#3 (line 619) | Tập rỗng (không HT) → UI "—" | cb_nv_tw_01 login. 0 vụ HT trong kỳ. | Default | 1. Apply. 2. Inspect KPI-S-02. | (1) `gia_tri=NULL`. (2) UI "—" (SRS line 608 quote "Nếu tập rỗng → giá trị trống"). | Negative 🟡 |

---

## C. KPI-S-01..02 — EDGE (A4 merged)

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|---------|---------------|----------------|-----------|-------------------|------------------|------|
| TC-DASH-114 | KPI-S-01..02 / SRS line 195 + 783-789 (A4 merged + Codex P0-1 patched) | KPI-S-01 KPI ngược chiều — TANG = ĐỎ, GIAM = XANH | cb_nv_tw_01 login. KPI-S-01 kỳ này=35% vs kỳ trước=20% (TANG = chất lượng kém hơn). | nam=2026, thang=4 | 1. Apply. 2. Inspect màu chỉ dấu trend KPI-S-01. | (1) `huong_tang_giam=TANG`. (2) `xu_huong_phan_tram=+75,0%` (relative %, công thức TPL-DASH-KPI bước 5: `(N−M)/M×100 = (35−20)/20×100 = +75,0%`). KHÔNG phải +15 point change — TPL output là **relative %** (SRS line 195 + 212). (3) UI: ↑ "+75,0%" **màu ĐỎ** (KPI ngược chiều — chất lượng kém hơn — SRS line 784 quote "đỏ với KPI ngược chiều: KPI-S-01/02"). **SPEC-CLARIFY-DASH-02 RESOLVED**: per TPL bước 5 → relative %. | Edge 🔴 |
| TC-DASH-115 | KPI-S-02 / SRS line 195 + 212 + 783-789 (A4 merged + Codex P0-2 patched) | KPI-S-02 KPI ngược chiều — GIAM = XANH | cb_nv_tw_01 login. KPI-S-02 kỳ này=4 ngày vs kỳ trước=6 ngày (GIAM = nhanh hơn = tốt hơn). | Default | 1. Apply. 2. Inspect màu chỉ dấu trend KPI-S-02. | (1) `huong_tang_giam=GIAM`. (2) `xu_huong_phan_tram=−33,3%` (relative %, công thức TPL bước 5: `(4−6)/6×100 = −33,3%`). KHÔNG phải −2,0 ngày delta — TPL output `xu_huong_phan_tram` là **percent**, không phải absolute delta (SRS line 212 "% chênh lệch so kỳ trước"). (3) UI: ↓ "−33,3%" **màu XANH** (KPI ngược chiều — thời gian ngắn hơn = tốt hơn per SRS line 785). | Edge 🔴 |
| TC-DASH-116 | KPI-S-02 / Boundary T6 → T2 cuối tuần (A4 merged) | Vụ tiếp nhận T6, HT T2 tuần sau (cuối tuần KHÔNG đếm) | cb_nv_tw_01 login. 1 vụ tiếp nhận T6 02/01/2026, HT T2 05/01/2026. | Default | 1. Apply. 2. Inspect KPI-S-02 contribution. | Số ngày làm việc đóng góp = 1 (T6 → T2: T6,T7,CN,T2 → chỉ T6 (đầu) → T2 (kết thúc), khoảng cách 1 ngày làm việc — T7+CN không đếm per BR-CALC-03 SRS line 1163). | Edge 🟡 |
| TC-DASH-117 | KPI-S-01 / Boundary 0% (A4 merged) | KPI-S-01 = 0% (10 HT, 0 từng qua bổ sung) | cb_nv_tw_01 login. 10 HT trong kỳ, 0 đã đi qua YEU_CAU_BO_SUNG. | Default | 1. Apply. 2. Inspect KPI-S-01. | (1) `gia_tri=0,0%`. (2) UI hiển thị "0,0%" (KHÔNG hiển thị "—" vì mẫu số > 0). | Edge 🟢 |
| TC-DASH-118 | KPI-S-01 / Boundary 100% (A4 merged) | KPI-S-01 = 100% (5 HT, 5 đều từng qua bổ sung) | cb_nv_tw_01 login. 5 HT, 5 đều qua bổ sung. | Default | 1. Apply. 2. Inspect KPI-S-01. | `gia_tri=100,0%`. | Edge 🟢 |
| TC-DASH-119 | KPI-S-02 / Cuối tuần range cross-month (A4 merged) | Vụ tiếp nhận cuối tháng, HT đầu tháng sau | cb_nv_tw_01 login. 1 vụ tiếp nhận 31/03/2026 (T2), HT 02/04/2026 (T4). | nam=2026, thang=4 | 1. Apply. 2. Inspect KPI-S-02. | (1) `ngay_hoan_thanh ∈ tháng 4` → vụ này được include. (2) Số ngày làm việc đóng góp = 2 (T2 31/03 → T3 01/04 → T4 02/04 = 2 ngày làm việc). | Edge 🟡 |

---

## Tổng kết file 05-TC

- **Tổng số TC: 13** (7 Happy + 2 Negative + 6 Edge — A4 merged inline)
- **Critical TC (🔴)**: TC-DASH-100, 101, 102, 103, 105, 114, 115
- **A4 merged 2026-05-10**: TC-DASH-114..119 (KPI ngược chiều color semantic + boundary T6/T2 weekend + boundary 0%/100% + cross-month)
- **Codex 2026-05-10 patches**: TC-DASH-114 sửa expected `+15,0%` → `+75,0%` (relative % per TPL bước 5, P0-1). TC-DASH-115 sửa expected `−2,0` ngày → `−33,3%` (relative % per TPL line 212, P0-2). **SPEC-CLARIFY-DASH-02 RESOLVED** — per TPL bước 5 + line 212: `xu_huong_phan_tram` là **relative %**, không phải absolute delta.
- **SPEC-CLARIFY refs**:
  - ~~**SPEC-CLARIFY-DASH-02**: KPI-S-01 đơn vị thay đổi `xu_huong_phan_tram` là % point hay % relative?~~ → **RESOLVED 2026-05-10 by Codex P0-1/P0-2**: TPL-DASH-KPI bước 5 SRS line 195 quote công thức `(giá trị kỳ này − giá trị kỳ trước) ÷ giá trị kỳ trước × 100` → **relative %** cho mọi KPI (kể cả KPI-S-01/02 theo TPL).
- **OBS**: KHÔNG có drill-down (SRS line 585, 614)

*Generated 2026-05-10 — Phase A3 + A4 merged (manual edge case hunter)*
