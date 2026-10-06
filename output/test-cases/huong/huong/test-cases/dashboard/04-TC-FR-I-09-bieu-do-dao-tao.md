# Test Cases — FR-I-09: UC9 — Biểu đồ vành (Chất lượng đào tạo)

> **SRS Ref**: FR-I-09 (`srs-fr-01-dashboard-v3.1.md` line 493-552), Vùng 5 component #25 (line 833)
> **Ngày tạo**: 2026-05-10 (Phase A3 + A4 merged)
> **Đặc thù**: Donut 2 phần "Đạt"/"Không đạt" + nhãn trung tâm "Điểm trung bình: {X.X}/10" + caption "Dựa trên {N} học viên". Tỷ lệ đạt = học viên `xep_loai ∈ {DAT, GIOI, KHA, TRUNG_BINH}` / tổng học viên × 100. Điểm TB = mean(`diem_kiem_tra`), 1 chữ số thập phân, range 0-10. Bố cục thẻ 3 cột (donut + tỷ lệ đạt khối + điểm KT khối) trải hết hàng. Trend cho cả 2 chỉ số.

---

## Quy ước

- **Priority**: 🔴 P0 (critical) · 🟡 P1 (high) · 🟢 P2 (medium)
- **TraceID**: `FR-I-09 / {section}` link SRS line/heading
- **Pre-conditions mặc định**: User đã login + `DASHBOARD_VIEW`. Có dữ liệu `KET_QUA_DAO_TAO` Nhóm III trong kỳ.

---

## A. UC9 — HAPPY

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|---------|---------------|----------------|-----------|-------------------|------------------|------|
| TC-DASH-080 | FR-I-09 / Processing step 2 + AC#1 (SRS line 543) | UC9 render donut 2 phần với center label + caption | cb_nv_tw_01 login. Có 50 học viên: 40 Đạt (xếp loại ∈ {DAT, GIOI, KHA, TRUNG_BINH}), 10 KHONG_DAT. Điểm TB=7,5/10. | Default | 1. Vào `/dashboard`. 2. Quan sát Vùng 5 — biểu đồ UC9. | (1) Donut 2 phần: "Đạt" 80% + "Không đạt" 20%. (2) Nhãn trung tâm "Điểm trung bình: 7,5/10". (3) Caption "Dựa trên 50 học viên" (SRS line 833). | Happy 🔴 |
| TC-DASH-081 | FR-I-09 / Processing step 2 (SRS line 516) | Tỷ lệ đạt counts 4 enum xếp loại + KHONG_DAT loại trừ | cb_nv_tw_01 login. 30 học viên: 5 GIOI + 10 KHA + 8 TRUNG_BINH + 2 DAT + 5 KHONG_DAT. | Default | 1. Apply. 2. Inspect ty_le_dat. | (1) Tử số = 25 (5+10+8+2 — 4 enum đạt). (2) Mẫu số = 30. (3) ty_le_dat = 25/30 × 100 = 83,3% (SRS line 516 quote: "xếp loại 'Đạt' / 'Giỏi' / 'Khá' / 'Trung bình'"). | Happy 🔴 |
| TC-DASH-082 | FR-I-09 / Processing step 3 + Outputs#4 | Điểm TB = mean(diem_kiem_tra), 1 chữ số thập phân, range 0-10 | cb_nv_tw_01 login. Học viên có điểm 8.5, 7.0, 6.5, 9.0, 5.5 → mean = 7.3. | Default | 1. Apply. 2. Inspect nhãn trung tâm donut. | (1) `diem_tb=7,3` (1 chữ số thập phân, làm tròn theo SRS line 517). (2) Nhãn trung tâm "Điểm trung bình: 7,3/10". | Happy 🔴 |
| TC-DASH-083 | FR-I-09 / Outputs#7 | sample_size = tổng số học viên có điểm trong kỳ + phạm vi | cb_nv_tw_01 login. 50 học viên có điểm trong kỳ. | Default | 1. Apply. 2. Inspect chú thích chân biểu đồ. | (1) `sample_size=50`. (2) Caption "Dựa trên 50 học viên". | Happy 🟡 |
| TC-DASH-084 | FR-I-09 / Component #25 SRS line 833 | Bố cục thẻ trải hết hàng, chia 3 cột | cb_nv_tw_01 login. | — | 1. Apply. 2. Inspect bố cục Vùng 5 UC9. | (1) Thẻ trải hết chiều ngang. (2) Chia 3 cột: cột 1 = donut, cột 2 = khối "Tỷ lệ đạt chứng nhận" (chú thích Đạt/Không đạt + xu hướng), cột 3 = khối "Điểm kiểm tra trung bình" (xu hướng). (3) Chân thẻ trải hết: "Dựa trên {sample_size} học viên" (SRS line 833 quote). **OBS** — design system. | Happy 🟡 |
| TC-DASH-085 | FR-I-09 / Outputs#2-3 + AC#6 (SRS line 548) | Trend cho cả tỷ lệ đạt + điểm TB | cb_nv_tw_01 login. ty_le_dat kỳ này=80% vs kỳ trước=77%. diem_tb kỳ này=7,5 vs kỳ trước=7,3. | nam=2026, thang=4 | 1. Apply. 2. Quan sát 2 khối trend. | (1) Khối tỷ lệ đạt: ↑ "+3,9%" (TANG). (2) Khối điểm TB: ↑ "+0,2" (TANG). (Cả 2 chỉ số có trend riêng per SRS line 548). | Happy 🟡 |
| TC-DASH-086 | FR-I-09 / AC#3 (SRS line 545) | TW chọn L1='BN' aggregate cả tất cả BN | cb_nv_tw_01 login. BN1 có 30 HV (24 Đạt). BN2 có 20 HV (15 Đạt). | L1='BN', L2='Tất cả' | 1. Apply. 2. Inspect ty_le_dat. | ty_le_dat = (24+15)/(30+20) × 100 = 78%. (Aggregate gộp toàn bộ học viên BN per SRS line 545). | Happy 🟡 |
| TC-DASH-087 | FR-I-09 / AC#4 (SRS line 546, BR-AUTH-08) | User BN/ĐP locked → tỷ lệ đạt + điểm TB của đơn vị user | cb_nv_dp_01 (AG) login. AG có 25 HV (20 Đạt + 5 KHONG_DAT), điểm TB=7.0. BG có 30 HV. | Auto-locked | 1. Vào `/dashboard`. 2. Inspect UC9. | (1) ty_le_dat = 80% (chỉ AG). (2) diem_tb = 7,0. (3) sample_size=25. (4) KHÔNG aggregate BG (BR-AUTH-08). | Happy 🔴 |

---

## B. UC9 — NEGATIVE

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|---------|---------------|----------------|-----------|-------------------|------------------|------|
| TC-DASH-090 | FR-I-09 / E1 INFO-DASH-03 (SRS line 540) | Không có data đào tạo trong kỳ → donut trống | cb_nv_dp_01 login. AG có 0 học viên có điểm trong tháng 4. | nam=2026, thang=4 | 1. Apply. 2. Quan sát UC9. | Donut trống + caption "Chưa có dữ liệu trong kỳ" (E1 INFO-DASH-03). | Negative 🟡 |

---

## C. UC9 — EDGE (A4 merged)

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|---------|---------------|----------------|-----------|-------------------|------------------|------|
| TC-DASH-093 | FR-I-09 / AC#7 (SRS line 549) (A4 merged) | Kỳ trước thiếu data → trend "—" cho cả 2 chỉ số | cb_nv_tw_01 login. Audit log thiếu data tại boundary kỳ trước (KET_QUA_DAO_TAO). | nam=năm bắt đầu sd, thang=1 | 1. Apply. 2. Inspect 2 khối trend. | (1) Khối tỷ lệ đạt trend "—" (SRS line 549 quote: "không có dữ liệu kỳ trước → '—'"). (2) Khối điểm TB trend "—". | Edge 🟡 |
| TC-DASH-094 | FR-I-09 / Outputs#3 + #6 boundary (A4 merged) | Kỳ trước=0 học viên, kỳ này>0 → trend "—" + TANG (impl) | cb_nv_tw_01 login. Kỳ trước=0 HV, kỳ này=10 HV (8 Đạt). | Default | 1. Apply. 2. Inspect trend khối tỷ lệ đạt. | (1) `ty_le_dat_phan_tram_change=NULL`. (2) UI "—" (theo TPL line 787). | Edge 🟡 |
| TC-DASH-095 | FR-I-09 / Tỷ lệ đạt = 100% (A4 merged) | Tất cả học viên Đạt → donut 100% Đạt | cb_nv_tw_01 login. 20 học viên đều Đạt. | Default | 1. Apply. 2. Inspect donut. | (1) Donut 100% phần "Đạt" + 0% "Không đạt" (1 phần che hết). (2) ty_le_dat=100%. (3) Donut vẫn render hợp lệ. | Edge 🟢 |
| TC-DASH-096 | FR-I-09 / Tỷ lệ đạt = 0% (A4 merged) | Tất cả học viên KHONG_DAT → donut 0% Đạt | cb_nv_tw_01 login. 15 học viên đều KHONG_DAT. | Default | 1. Apply. 2. Inspect donut. | (1) Donut 0% Đạt + 100% KHONG_DAT. (2) ty_le_dat=0%. | Edge 🟢 |
| TC-DASH-097 | FR-I-09 / SRS line 1080 entity diem_kiem_tra range (A4 merged) | Boundary điểm KT 0 vs 10 | cb_nv_tw_01 login. 3 HV: điểm 0, điểm 10, điểm 5 → mean=5,0. | Default | 1. Apply. 2. Inspect diem_tb. | (1) `diem_tb=5,0`. (2) Range valid 0-10 (SRS line 1080 entity constraint `CHECK BETWEEN 0 AND 10`). | Edge 🟢 |
| TC-DASH-098 | FR-I-09 / Học viên KHÔNG có điểm KT (A4 merged) | Học viên `diem_kiem_tra=NULL` → loại khỏi sample_size | cb_nv_tw_01 login. 20 HV: 18 có điểm + 2 NULL. | Default | 1. Apply. 2. Inspect sample_size + diem_tb. | (1) `sample_size=18` (chỉ HV có điểm — SRS line 518 quote "tổng số học viên có điểm kiểm tra"). (2) `diem_tb` tính trên 18 HV. (3) ty_le_dat tính trên 18 HV (xếp loại tự động khi có điểm? **SPEC-CLARIFY-DASH-01**: 2 HV NULL có vào mẫu số tỷ lệ đạt không? Likely loại). | Edge 🟡 |

---

## E. A6 fill (gap A5)

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|---------|---------------|----------------|-----------|-------------------|------------------|------|
| TC-DASH-222 | FR-I-09 / AC#2 (SRS line 544) (A6 fill) | TW chọn 1 đơn vị cụ thể UC9 → tỷ lệ đạt + điểm TB tính riêng cho đơn vị | cb_nv_tw_01 login. ĐP X có 25 HV (20 Đạt + 5 KHONG_DAT, điểm TB=7,2). ĐP Y có 50 HV (35 Đạt + 15 KHONG_DAT, điểm TB=6,5). | L1='DP', L2=ĐP X | 1. Login. 2. Đổi L2 sang ĐP X. Apply. 3. Quan sát UC9. | (1) Donut: "Đạt" 80% + "Không đạt" 20% (chỉ ĐP X). (2) Center label "Điểm trung bình: 7,2/10". (3) Caption "Dựa trên 25 học viên". (4) KHÔNG aggregate ĐP Y (50 HV không vào tỷ lệ). (5) Chip "Phạm vi: {tên ĐP X}". (SRS line 544 quote "user TW chọn 1 đơn vị cụ thể → tỷ lệ đạt + điểm TB tính riêng cho đơn vị đó"). | Happy 🟡 |

---

## Tổng kết file 04-TC

- **Tổng số TC: 15** (8 Happy + 1 Negative + 6 Edge + 1 A6 fill — A4 + A6 merged inline)
- **Critical TC (🔴)**: TC-DASH-080, 081, 082, 087
- **A4 merged 2026-05-10**: TC-DASH-093..098 (audit log thiếu kỳ trước + boundary 100%/0% + boundary điểm + NULL handling)
- **A6 fill 2026-05-10**: TC-DASH-222 (UC9 TW chọn 1 đơn vị scope) — fill GAP-5
- **SPEC-CLARIFY refs**:
  - **SPEC-CLARIFY-DASH-01**: học viên `diem_kiem_tra=NULL` có vào mẫu số tỷ lệ đạt? (SRS line 516 chỉ rõ tử số dựa xếp loại — không rõ NULL có xếp loại không)
- **OBS**: TC-084 (3 cột bố cục — design system decision)

*Generated 2026-05-10 — Phase A3 + A4 + A6 merged (manual edge case hunter + A6 gap fill)*
