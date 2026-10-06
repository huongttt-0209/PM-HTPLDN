# Test Cases — FR-I-08: UC8 — 2 biểu đồ cột song song (Đánh giá hiệu quả + SLA)

> **SRS Ref**: FR-I-08 (`srs-fr-01-dashboard-v3.1.md` line 406-490), BR-SLA-05 (line 1153-1157), Vùng 5 components #23-#24 (line 822-823)
> **Ngày tạo**: 2026-05-10 (Phase A3 + A4 merged)
> **Đặc thù**: 2 biểu đồ cột **độc lập** (KHÔNG dual axis Y) — biểu đồ TRÁI 0-100 điểm đánh giá `KET_QUA_DANH_GIA.diem_tong` + biểu đồ PHẢI % SLA. Trục X dynamic theo filter. BR-SLA-05 mẫu số includes vụ "Đang xử lý đã quá hạn" (tránh tỷ lệ ảo). Cỡ mẫu N<10 → asterisk + tooltip generic.

---

## Quy ước

- **Priority**: 🔴 P0 (critical) · 🟡 P1 (high) · 🟢 P2 (medium)
- **TraceID**: `FR-I-08 / {section}` link SRS line/heading
- **Pre-conditions mặc định**: User đã login + `DASHBOARD_VIEW`. Có dữ liệu Nhóm VI (KET_QUA_DANH_GIA) trong kỳ.

---

## Trục X logic theo filter (SRS line 442 + Rule table line 466-475)

| Filter state | Trục X (biểu đồ trái + phải) | Sort |
|---|---|---|
| `don_vi_id=NULL` (L2='Tất cả') | Các đơn vị cấp L1 có data | Giá trị **DESC** (mỗi biểu đồ độc lập) |
| `don_vi_id=X` (1 đơn vị) + `thang=NULL` (Tất cả) | 12 cột tháng (T1..T12) của X | Niên đại |
| `don_vi_id=X` + `thang=N` (1 tháng) | Max 31 cột ngày trong tháng N của X | Niên đại |
| User BN/ĐP locked | Chuỗi thời gian của đơn vị user | Niên đại |

---

## A. UC8 — HAPPY

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|---------|---------------|----------------|-----------|-------------------|------------------|------|
| TC-DASH-050 | FR-I-08 / AC#1 (SRS line 480) | User TW default → trục X = tất cả ĐP có data | cb_nv_tw_01 login (default L1=DP, L2='Tất cả ĐP'). Có 5 ĐP có data đánh giá trong kỳ. | Default | 1. Vào `/dashboard`. 2. Quan sát Vùng 5 — 2 biểu đồ UC8. | (1) Biểu đồ TRÁI: trục X = 5 cột (5 ĐP), trục Y 0-100 điểm đánh giá, sort DESC theo điểm. (2) Biểu đồ PHẢI: trục X = cùng 5 ĐP, trục Y 0-100% SLA, sort DESC theo SLA (độc lập). (3) Mỗi biểu đồ có header xu hướng. | Happy 🔴 |
| TC-DASH-051 | FR-I-08 / AC#3 (SRS line 482) | TW chọn 1 đơn vị + 1 Tháng cụ thể → trục X = ngày trong tháng (max 31) | cb_nv_tw_01 login. ĐP X có data đánh giá ngày 1, 5, 10, 15, 20, 25, 30 trong tháng 4. | nam=2026, thang=4, don_vi_id=X | 1. Apply filter. 2. Quan sát biểu đồ. | (1) Trục X = 7 cột ngày (chỉ ngày có data — bỏ ngày không có data per SRS line 442). (2) Sort niên đại. | Happy 🔴 |
| TC-DASH-052 | FR-I-08 / AC#4 (SRS line 483) | TW chọn 1 đơn vị + Tháng "Tất cả" → trục X = 12 cột tháng | cb_nv_tw_01 login. ĐP X có data 12 tháng năm 2025. | nam=2025, thang=NULL, don_vi_id=X | 1. Apply filter. 2. Quan sát biểu đồ. | Trục X = 12 cột (T1..T12) sort niên đại. | Happy 🟡 |
| TC-DASH-053 | FR-I-08 / Outputs#5-6 | Biểu đồ trái render `chart_data_hai_long` đúng | cb_nv_tw_01 login. ĐP A điểm TB=80,5, ĐP B=72,3, ĐP C=65,1. | Default | 1. Apply. 2. Hover từng cột biểu đồ trái. | Hover gợi ý "ĐP A: 80,5/100", "ĐP B: 72,3/100", "ĐP C: 65,1/100". Sort DESC. | Happy 🟡 |
| TC-DASH-054 | FR-I-08 / Outputs#6 + BR-SLA-05 | Biểu đồ phải render `chart_data_sla` áp BR-SLA-05 | cb_nv_tw_01 login. ĐP A: 8 vụ HT đúng hạn / 10 mẫu số (8 HT + 2 đang xử lý quá hạn) → 80%. | Default | 1. Apply. 2. Hover cột ĐP A biểu đồ phải. | (1) Hover "ĐP A: 80,0%". (2) Mẫu số = 10 (HT + đang xử lý quá hạn) per BR-SLA-05 (SRS line 1157). | Happy 🔴 |
| TC-DASH-055 | FR-I-08 / Outputs#7-8 | Header xu hướng so kỳ trước (cả 2 biểu đồ độc lập) | cb_nv_tw_01 login. Điểm TB kỳ này=75 vs kỳ trước=70. SLA kỳ này=85 vs kỳ trước=90. | nam=2026, thang=4 | 1. Apply. 2. Quan sát header 2 biểu đồ. | (1) Biểu đồ trái header: ↑ "+7,1%" (TANG) màu xanh + chênh lệch điểm. (2) Biểu đồ phải header: ↓ "−5,6%" (GIAM) màu đỏ. (Độc lập). | Happy 🟡 |
| TC-DASH-056 | FR-I-08 / Component #23 (SRS line 822) | Biểu đồ trái — trục Y 0-100 điểm đánh giá | cb_nv_tw_01 login. | — | 1. Apply. 2. Inspect biểu đồ trái axis. | Trục Y range 0-100 (điểm `KET_QUA_DANH_GIA.diem_tong` constraint 0-100 per entity SRS line 1066). | Happy 🟢 |
| TC-DASH-057 | FR-I-08 / Component #24 (SRS line 823) | Biểu đồ phải — trục Y 0-100% SLA | cb_nv_tw_01 login. | — | 1. Apply. 2. Inspect biểu đồ phải axis. | Trục Y range 0-100%. | Happy 🟢 |
| TC-DASH-058 | FR-I-08 / SRS line 822-823 | Chú thích chân biểu đồ — cỡ mẫu in đậm | cb_nv_tw_01 login. so_luong_danh_gia=42, so_luong_vu_viec_sla=56. | — | 1. Apply. 2. Quan sát chú thích chân 2 biểu đồ. | (1) Trái: "Dựa trên **42** đánh giá" (cỡ mẫu in đậm). (2) Phải: "Tính trên **56** vụ việc". | Happy 🟢 |
| TC-DASH-059 | FR-I-08 / SRS line 825 | KHÔNG dùng dual axis Y (2 biểu đồ tách biệt) | cb_nv_tw_01 login. | — | 1. Apply. 2. Inspect Vùng 5 layout UC8. | (1) 2 biểu đồ riêng biệt cạnh nhau (KHÔNG cùng container axis Y kép). (2) Mỗi biểu đồ có axis riêng. | Happy 🔴 |
| TC-DASH-060 | FR-I-08 / BR-SLA-05 (SRS line 1157) — Kịch bản 1 | BR-SLA-05 (1) chỉ HT đúng hạn → 100% | cb_nv_tw_01 login. ĐP X: 5 vụ HT đúng hạn / 0 vụ HT trễ / 0 vụ đang xử lý quá hạn. | nam=2026, thang=4, don_vi_id=X | 1. Apply. 2. Inspect biểu đồ phải ĐP X. | (1) ty_le_tuan_thu_sla=100%. (2) Cột X cao = 100. | Happy 🔴 |
| TC-DASH-061 | FR-I-08 / BR-SLA-05 — Kịch bản 2 | BR-SLA-05 (2) có vụ HT trễ → giảm | cb_nv_tw_01 login. ĐP X: 4 HT đúng / 1 HT trễ → tỷ lệ = 4/5 = 80%. | Default | 1. Apply. 2. Inspect biểu đồ phải ĐP X. | (1) ty_le_tuan_thu_sla=80%. | Happy 🟡 |
| TC-DASH-062 | FR-I-08 / BR-SLA-05 — Kịch bản 3 | BR-SLA-05 (3) có vụ đang xử lý quá hạn → giảm (dù chưa đóng) | cb_nv_tw_01 login. ĐP X: 5 HT đúng / 0 HT trễ / 3 đang xử lý quá hạn → 5/(5+3) = 62,5%. | Default | 1. Apply. 2. Inspect biểu đồ phải ĐP X. | (1) ty_le_tuan_thu_sla=62,5%. (2) Mẫu số = 8 (5 HT + 3 đang quá hạn — tránh tỷ lệ ảo per BR-SLA-05). | Happy 🔴 |

---

## B. UC8 — NEGATIVE

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|---------|---------------|----------------|-----------|-------------------|------------------|------|
| TC-DASH-068 | FR-I-08 / E1 INFO-DASH-02 (SRS line 464) | Không có data đánh giá trong kỳ + scope | cb_nv_dp_01 login. AG có 0 đánh giá trong tháng 4. | nam=2026, thang=4 | 1. Apply. 2. Quan sát biểu đồ trái. | Biểu đồ trống + caption "Chưa có dữ liệu trong kỳ" (E1 INFO-DASH-02). | Negative 🟡 |
| TC-DASH-069 | FR-I-08 / E1 — biểu đồ phải vẫn render khi trái trống | Trái không có data nhưng phải có (vụ HT) | cb_nv_dp_01 login. AG có 0 đánh giá nhưng có 5 vụ HT trong kỳ. | nam=2026, thang=4 | 1. Apply. 2. Inspect 2 biểu đồ. | (1) Trái trống + "Chưa có dữ liệu trong kỳ". (2) Phải vẫn render với 5 vụ. (Độc lập per SRS line 825). | Negative 🟡 |

---

## C. UC8 — EDGE (A4 merged)

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|---------|---------------|----------------|-----------|-------------------|------------------|------|
| TC-DASH-072 | FR-I-08 / SRS line 442 (A4 merged) | Cỡ mẫu N<10 → asterisk + tooltip generic | cb_nv_tw_01 login. ĐP X có 8 đánh giá (< 10). | Default | 1. Apply. 2. Hover cột ĐP X biểu đồ trái. 3. Inspect value row. | (1) Cột ĐP X có dấu `*` (asterisk). (2) Tooltip "Lưu ý: mẫu nhỏ (< 10 đánh giá) — kết quả tham khảo" (SRS line 442 quote — KHÔNG đưa số N cụ thể vào nhãn chú giải). (3) Value row: "Điểm đánh giá: {X,X}/100 * (N=8)" (số N hiển thị ở value row dạng `(N={n})` per SRS line 442). | Edge 🔴 |
| TC-DASH-073 | FR-I-08 / SRS line 442 (A4 merged) | Cỡ mẫu N<10 cho biểu đồ phải (vụ việc) | cb_nv_tw_01 login. ĐP Y có 7 vụ trong mẫu số SLA. | Default | 1. Apply. 2. Hover cột ĐP Y biểu đồ phải. | Tooltip "Lưu ý: mẫu nhỏ (< 10 vụ việc) — kết quả tham khảo" (cùng pattern, đổi tên đối tượng). | Edge 🟡 |
| TC-DASH-074 | FR-I-08 / SRS line 442 (A4 merged) | 1 đơn vị có data khi phạm vi nhiều → vẫn hiển thị 1 cột | cb_nv_tw_01 login. Chỉ ĐP A có data đánh giá. ĐP B, C, D, E... có 0. | Default L2='Tất cả ĐP' | 1. Apply. 2. Quan sát biểu đồ. | Biểu đồ trái + phải mỗi biểu đồ có **1 cột** (chỉ ĐP A). KHÔNG cảnh báo. (SRS line 442 quote: "1 đơn vị có dữ liệu khi phạm vi = nhiều → vẫn hiển thị 1 cột, không cảnh báo"). | Edge 🟡 |
| TC-DASH-075 | FR-I-08 / SRS line 442 (A4 merged) | Ngày không có data (trục X = ngày) → bỏ qua, không vẽ cột | cb_nv_tw_01 login. ĐP X có data ngày 5, 10, 15 trong tháng 4. | nam=2026, thang=4, don_vi_id=X | 1. Apply. 2. Quan sát biểu đồ. | Trục X = 3 cột (chỉ 5, 10, 15 — bỏ qua các ngày không có data per SRS line 442). | Edge 🟡 |
| TC-DASH-076 | FR-I-08 / Component #23-24 SRS line 822 (A4 merged) | Trục Y giới hạn cận dưới ≥0 (làm nổi chênh lệch) | cb_nv_tw_01 login. Điểm TB các ĐP: 75, 78, 82 (chênh nhỏ). | Default | 1. Apply. 2. Inspect trục Y biểu đồ trái. | (1) Trục Y range hẹp (vd 70-85) để làm nổi chênh lệch. (2) Cận dưới ≥ 0 (SRS line 822 quote "đội thiết kế UI có thể giới hạn khoảng hiển thị trục Y (cận dưới ≥ 0)"). **OBS** — design system quyết. | Edge 🟢 |
| TC-DASH-077 | FR-I-08 / Cuộn ngang SRS line 442 (A4 merged) | Tổng chiều rộng cột vượt vùng hiển thị → cuộn ngang | cb_nv_tw_01 login. Có 30+ ĐP với data đánh giá. | Default L2='Tất cả ĐP' | 1. Apply. 2. Inspect biểu đồ. | (1) Biểu đồ scrollable horizontal. (2) Trục Y cố định bên trái. (SRS line 442 quote). **OBS** — design system. | Edge 🟢 |
| TC-DASH-078 | FR-I-08 / BR-SLA-05 boundary (A4 merged) | Mẫu số = 0 (không có HT + không có quá hạn) → biểu đồ phải trống | cb_nv_tw_01 login. ĐP Y: 0 HT + 0 đang xử lý quá hạn. | Default | 1. Apply. 2. Inspect biểu đồ phải ĐP Y. | (1) Cột ĐP Y KHÔNG render (0/0 không tính được). (2) HOẶC empty per E1. | Edge 🟡 |
| TC-DASH-079 | FR-I-08 / Cross-year boundary (A4 merged) | Tháng 1 → kỳ trước = Tháng 12 năm Y-1 | cb_nv_tw_01 login. Có data tháng 12/2025 và tháng 1/2026. | nam=2026, thang=1 | 1. Apply. 2. Inspect header xu hướng. | (1) Kỳ này = tháng 1/2026. (2) Kỳ trước = tháng 12/2025 (cross-year per SRS line 762). (3) Trend tính đúng giữa 2 kỳ. | Edge 🟡 |

---

## E. A6 fill (gap A5)

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|---------|---------------|----------------|-----------|-------------------|------------------|------|
| TC-DASH-220 | FR-I-08 / AC#2 (SRS line 481) (A6 fill) | TW switch L1='BN' + L2='Tất cả BN' UC8 → trục X = tất cả BN có data, sort DESC | cb_nv_tw_01 login (default L1=DP). 4 BN có data đánh giá: BTC=82đ, BKH=75đ, BGTVT=68đ, BCT=60đ. | L1='BN', L2='Tất cả BN' | 1. Login. 2. Đổi L1 sang Bộ ngành. 3. L2 reset = "Tất cả Bộ ngành". 4. Apply. 5. Quan sát biểu đồ trái + phải. | (1) Biểu đồ TRÁI: trục X = 4 cột (BTC=82, BKH=75, BGTVT=68, BCT=60), sort DESC theo điểm. (2) Biểu đồ PHẢI: trục X = cùng 4 BN, sort DESC theo SLA độc lập (có thể thứ tự khác). (3) Chip "Phạm vi: Tất cả bộ ngành". (SRS line 481 quote: "TW đổi filter sang L1='BN' + L2='Tất cả BN' → trục X = tất cả BN có data, sort giá trị DESC"). | Happy 🟡 |
| TC-DASH-221 | FR-I-08 / AC#5 (SRS line 484) BR-AUTH-08 (A6 fill) | User BN/ĐP locked UC8 → trục X = chuỗi thời gian của đơn vị user | cb_nv_dp_01 (Sở TP AG) login. AG có data đánh giá tháng 1, 2, 3, 4 năm 2026 (4 tháng). | nam=2026, thang=NULL (Tất cả), L1+L2 locked AG | 1. Login (locked AG). 2. Vào `/dashboard` (default Tháng="Tất cả"). 3. Quan sát Vùng 5 — UC8. | (1) Biểu đồ trái + phải mỗi biểu đồ trục X = 4 cột tháng (T1, T2, T3, T4 — chỉ tháng có data của AG). (2) Sort niên đại (KHÔNG sort DESC vì là chuỗi thời gian per Rule table line 475-476). (3) Chip "Phạm vi: Sở Tư pháp An Giang". (4) KHÔNG aggregate ĐP khác (BR-AUTH-08). (SRS line 484 quote "User BN/ĐP đăng nhập (bộ lọc khóa) → trục X = các kỳ của đơn vị user"). | Happy 🔴 |

---

## Tổng kết file 03-TC

- **Tổng số TC: 24** (13 Happy + 2 Negative + 8 Edge + 2 A6 fill — A4 + A6 merged inline)  
- **Critical TC (🔴)**: TC-DASH-050, 051, 054, 059, 060, 062, 072, 221
- **A4 merged 2026-05-10**: TC-DASH-072..079 (cỡ mẫu N<10 + 1 đơn vị có data + ngày không có data + trục Y range + cuộn ngang + mẫu số 0 + cross-year)
- **A6 fill 2026-05-10**: TC-DASH-220 (TW L1=BN UC8 sort DESC) + TC-DASH-221 (BN/ĐP locked UC8 chuỗi thời gian) — fill GAP-3, GAP-4
- **OBS**: TC-076, 077 (design system decisions — không block)
- **SPEC-CLARIFY refs**: (none new — UC8 spec rất chi tiết tại SRS line 442 + Rule table)

*Generated 2026-05-10 — Phase A3 + A4 + A6 merged (manual edge case hunter + A6 gap fill)*
