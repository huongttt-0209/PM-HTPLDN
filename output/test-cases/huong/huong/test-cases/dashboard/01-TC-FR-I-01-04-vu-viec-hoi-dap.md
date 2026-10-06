# Test Cases — FR-I-01..04: KPI Hỏi đáp + Vụ việc (UC1-UC4)

> **SRS Ref**: FR-I-01, FR-I-02, FR-I-03, FR-I-04, TPL-DASH-KPI (`srs-fr-01-dashboard-v3.1.md` line 168-225, 227-326)
> **Ngày tạo**: 2026-05-10 (Phase A3 + A4 merged)
> **Đặc thù**: 4 KPI thẻ — KPI-01 (HD MOI count) + KPI-02 (VV `ngay_tiep_nhan` trong kỳ) + KPI-03 (VV ảnh chụp 5 enum sống tại cuối kỳ) + KPI-04 (VV HOAN_THANH `ngay_hoan_thanh` trong kỳ). KPI-03 ảnh chụp đặc biệt — không khoảng thời gian, đếm tại boundary cuối kỳ. Drill-down chỉ verify URL params đúng spec, KHÔNG vào module target test sâu.

---

## Quy ước

- **Priority**: 🔴 P0 (critical) · 🟡 P1 (high) · 🟢 P2 (medium)
- **TraceID**: `FR-I-{NN} / {section}` link SRS line/heading
- **Pre-conditions mặc định**: User đã login + có quyền `DASHBOARD_VIEW` + ở SCR-I-01 `/dashboard`

---

## Output fields TPL-DASH-KPI (12 trường, áp cho cả 4 KPI)

| # | Field | Format | Áp KPI |
|---|-------|--------|--------|
| 1 | `gia_tri` | số (định dạng vi-VN: <1.000 nguyên, ≥1.000 dấu chấm phân tách hàng nghìn, ≥1tr "1,2 triệu" + tooltip giá trị đầy đủ) | 01/02/03/04 |
| 2 | `nhan` | text | 01/02/03/04 |
| 3 | `don_vi_tinh` | text ("yêu cầu", "vụ việc") | 01/02/03/04 |
| 4 | `drill_down_url` | URL với filter params kèm | 01/02/03/04 |
| 5 | `nam` | integer | 01/02/03/04 |
| 6 | `thang` | integer 1-12 hoặc NULL | 01/02/03/04 |
| 7 | `scope_label` | "Năm 2026" / "Tháng 4/2026" | 01/02/03/04 |
| 8 | `tu_ngay_boundary` | datetime đầu kỳ | 01/02/03/04 |
| 9 | `den_ngay_boundary` | cuối kỳ HOẶC NOW nếu kỳ hiện tại | 01/02/03/04 |
| 10 | `is_qua_khu_dong` | boolean | 01/02/03/04 |
| 11 | `xu_huong_phan_tram` | % chênh kỳ trước, có thể trống | 01/02/03/04 |
| 12 | `huong_tang_giam` | TANG / GIAM / KHONG_DOI | 01/02/03/04 |

KPI-03/05/07 (ảnh chụp) có thêm chú thích phụ "Tính đến DD/MM/YYYY" (SRS line 793-797).

---

## A. KPI-01..04 — HAPPY

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|---------|---------------|----------------|-----------|-------------------|------------------|------|
| TC-DASH-001 | FR-I-01 / Processing step 4 | KPI-01 đếm HD `MOI` đúng theo phạm vi đơn vị | cb_nv_tw_01 login. Năm hiện tại + Tháng "Tất cả". Có ≥3 HD trạng_thái=`MOI` thuộc TW. | Default filter | 1. Vào `/dashboard`. 2. Quan sát thẻ KPI-01 "Hỏi đáp / vướng mắc mới". | (1) `gia_tri` = số HD MOI thuộc phạm vi (toàn TW + cấp con per BR-AUTH-04). (2) `don_vi_tinh="yêu cầu"`. (3) `nhan="Hỏi đáp / vướng mắc mới"`. (4) Định dạng vi-VN. (5) Có chỉ dấu xu hướng so kỳ trước (TANG/GIAM/KHONG_DOI). | Happy 🔴 |
| TC-DASH-002 | FR-I-02 / Processing step 4 | KPI-02 đếm VV theo `ngay_tiep_nhan` trong kỳ | cb_nv_tw_01 login. Có ≥5 VV `ngay_tiep_nhan` ∈ kỳ hiện tại. | Default filter | 1. Vào `/dashboard`. 2. Quan sát thẻ KPI-02 "Vụ việc đã tiếp nhận". | (1) `gia_tri` = COUNT VV `ngay_tiep_nhan` ∈ [tu_ngay_boundary, den_ngay_boundary]. (2) `don_vi_tinh="vụ việc"`. (3) Áp BR-AUTH-08. | Happy 🔴 |
| TC-DASH-003 | FR-I-03 / Processing step 4 + AC#2..6 (SRS line 291-301) | KPI-03 ảnh chụp 5 enum sống tại cuối kỳ | cb_nv_tw_01 login. Có VV ở mỗi 5 trạng_thái: `DA_TIEP_NHAN`, `DANG_KIEM_TRA`, `YEU_CAU_BO_SUNG`, `DA_PHAN_CONG`, `DANG_XU_LY`. Có VV `CHO_PHE_DUYET` + `HOAN_THANH` (KHÔNG đếm). | Default filter | 1. Vào `/dashboard`. 2. Quan sát KPI-03 "Vụ việc đang hỗ trợ". | (1) `gia_tri` = COUNT VV `trang_thai ∈ {DA_TIEP_NHAN, DANG_KIEM_TRA, YEU_CAU_BO_SUNG, DA_PHAN_CONG, DANG_XU_LY}` (SRS line 291). (2) KHÔNG đếm VV `CHO_PHE_DUYET / HOAN_THANH / DA_DANH_GIA / TU_CHOI` (SRS line 302). (3) Chú thích phụ "Tính đến hôm nay (DD/MM/YYYY)" (SRS line 794). | Happy 🔴 |
| TC-DASH-004 | FR-I-04 / Processing step 4 | KPI-04 đếm VV `HOAN_THANH` `ngay_hoan_thanh` trong kỳ | cb_nv_tw_01 login. Có ≥2 VV `HOAN_THANH` `ngay_hoan_thanh` ∈ kỳ hiện tại. | Default filter | 1. Vào `/dashboard`. 2. Quan sát KPI-04. | (1) `gia_tri` = COUNT VV `HOAN_THANH` & `ngay_hoan_thanh` trong kỳ. (2) Áp BR-AUTH-08. | Happy 🔴 |
| TC-DASH-005 | FR-I-01 / Outputs#5-9 | Output fields render đúng cho KPI-01 (12 fields) | cb_nv_tw_01 login. Năm=2026, Tháng=4. | nam=2026, thang=4 | 1. Apply filter. 2. Inspect KPI-01 widget. | (1) `nam=2026`. (2) `thang=4`. (3) `scope_label="Tháng 4/2026"`. (4) `tu_ngay_boundary=2026-04-01 00:00`. (5) `den_ngay_boundary=2026-04-30 23:59`. (6) `is_qua_khu_dong=TRUE` (do tháng 4 < tháng hiện tại 5). | Happy 🟡 |
| TC-DASH-006 | FR-I-01 / Drill-down + AC#1 | KPI-01 click → drill-down `/hoi-dap/danh-sach` với URL params đúng | cb_nv_tw_01 login. KPI-01 = 5 HD MOI. Năm=2026, Tháng="Tất cả". | nam=2026, thang=NULL, don_vi_cap=DP, don_vi_id=NULL | 1. Click thẻ KPI-01. | URL navigate = `/hoi-dap/danh-sach?trang_thai=MOI&nam=2026&thang=&don_vi_cap=DP&don_vi_id=` (SRS FR-I-01 Drill-down). KHÔNG test sâu module target. | Happy 🟡 |
| TC-DASH-007 | FR-I-02 / Drill-down | KPI-02 click → URL params có `date_field=ngay_tiep_nhan` | cb_nv_tw_01 login. | nam=2026, thang=4 | 1. Click KPI-02. | URL = `/vu-viec/danh-sach?date_field=ngay_tiep_nhan&nam=2026&thang=4&don_vi_cap=DP&don_vi_id=` (SRS FR-I-02 Drill-down). | Happy 🟡 |
| TC-DASH-008 | FR-I-03 / Drill-down (SRS line 293) | KPI-03 click → URL params có 5 enum sống concatenated CSV | cb_nv_tw_01 login. | Default | 1. Click KPI-03. | URL = `/vu-viec/danh-sach?trang_thai=DA_TIEP_NHAN,DANG_KIEM_TRA,YEU_CAU_BO_SUNG,DA_PHAN_CONG,DANG_XU_LY&don_vi_cap=DP&don_vi_id=` (KHÔNG kèm time params — KPI-03 ảnh chụp). | Happy 🔴 |
| TC-DASH-009 | FR-I-04 / Drill-down | KPI-04 click → URL params có `trang_thai=HOAN_THANH&date_field=ngay_hoan_thanh` | cb_nv_tw_01 login. | nam=2026, thang=4 | 1. Click KPI-04. | URL = `/vu-viec/danh-sach?trang_thai=HOAN_THANH&date_field=ngay_hoan_thanh&nam=2026&thang=4&don_vi_cap=DP&don_vi_id=`. | Happy 🟡 |
| TC-DASH-010 | FR-I-01..04 / TPL Outputs#11-12 | Xu hướng TANG hiển thị đúng (so kỳ trước > 0) | cb_nv_tw_01 login. KPI-02 kỳ này=10 VV, kỳ trước=8 VV (theo audit). | Year=2026, Month=4 (kỳ trước=Month 3) | 1. Apply filter. 2. Quan sát chỉ dấu xu hướng KPI-02. | (1) `huong_tang_giam=TANG`. (2) `xu_huong_phan_tram=+25,0%`. (3) UI: ↑ "+25,0%" màu xanh + dòng "so kỳ trước" (SRS line 783). | Happy 🟡 |

---

## B. KPI-01..04 — NEGATIVE

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|---------|---------------|----------------|-----------|-------------------|------------------|------|
| TC-DASH-015 | FR-I-01..04 / E1 INFO-DASH-01 | Không có dữ liệu KPI → text "Chưa có dữ liệu trong kỳ" | cb_nv_tw_01 login. Đơn vị X=BTC không có HD/VV nào trong kỳ. | nam=2026, thang=1, don_vi_id=BTC | 1. Apply filter. 2. Quan sát các thẻ KPI. | (1) `gia_tri=0`. (2) UI text "0" + chú thích phụ "Chưa có dữ liệu trong kỳ" (E1 INFO-DASH-01). (3) Trend "—" (xám trung tính, không icon). | Negative 🟡 |
| TC-DASH-016 | FR-I-01..04 / E3 ERR-DASH-02 (SRS line 651, Trạng thái 28) | Widget hỏng cục bộ — KHÔNG kéo fail toàn trang | cb_nv_tw_01 login. Backend KPI-02 trả 5xx (sim qua DevTools network throttling). | Block `/api/dashboard/kpi-02` 500 | 1. Vào `/dashboard`. 2. Force fail KPI-02 endpoint. 3. Observe các widget khác. | (1) KPI-02 widget hiển thị Trạng thái 28: text "Không tải được dữ liệu" + nút "Thử lại" cục bộ. (2) KHÔNG có toast/modal toàn trang (SRS line 223). (3) KPI-01/03/04 + 3 biểu đồ tải bình thường. **DEFERRED nếu không có hook stub backend** — mark OBS với Chrome DevTools network block. | Negative 🔴 |
| TC-DASH-017 | FR-I-01..04 / E2 INFO-DASH-04 | Audit log thiếu kỳ trước → trend "—" + tooltip | cb_nv_tw_01 login. Audit log thiếu data tại boundary cuối kỳ trước. | nam=năm bắt đầu sd phần mềm, thang=1 | 1. Apply filter (kỳ đầu). 2. Quan sát trend. | (1) `xu_huong_phan_tram=NULL`. (2) UI hiển thị "—" (KHÔNG kèm %, không icon). (3) Hover tooltip "Chưa đủ dữ liệu lịch sử để so sánh" (SRS line 789). (4) Phần đuôi văn bản "so kỳ trước" ẨN (SRS line 789). | Negative 🟡 |

---

## C. KPI-01..04 — EDGE (A4 merged)

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|---------|---------------|----------------|-----------|-------------------|------------------|------|
| TC-DASH-020 | FR-I-03 / Processing step 3 (A4 merged) | KPI-03 ảnh chụp tại cuối kỳ đã đóng KHÁC tại hiện tại | cb_nv_tw_01 login. Có VV X transition `DANG_XU_LY` → `HOAN_THANH` tại 2026-03-15. | nam=2026, thang=2 vs nam=2026, thang=4 hiện tại | 1. Apply nam=2026, thang=2 (kỳ đóng). 2. Note KPI-03. 3. Apply nam=2026, thang=4 (kỳ hiện tại). | (1) Tại kỳ tháng 2: VV X **đếm** trong KPI-03 (vẫn DANG_XU_LY tại 2026-02-28). (2) Tại kỳ hiện tại: VV X **không đếm** (đã HOAN_THANH). (3) Cùng VV cùng filter cho 2 ảnh chụp khác nhau theo boundary. | Edge 🔴 |
| TC-DASH-021 | FR-I-01..04 / TPL Outputs#11 (A4 merged) | Kỳ trước = 0, kỳ này > 0 → TANG, % trống | cb_nv_tw_01 login. KPI-01 kỳ trước (Tháng 3) = 0 HD, kỳ này (Tháng 4) = 5 HD. | nam=2026, thang=4 | 1. Apply filter. 2. Quan sát trend KPI-01. | (1) `huong_tang_giam=TANG` (tăng từ 0). (2) `xu_huong_phan_tram=NULL` (không tính được %). (3) UI: KHÔNG icon ↑, hiển thị "—" (SRS line 787). (4) Tooltip "Không có dữ liệu kỳ trước để so sánh". | Edge 🟡 |
| TC-DASH-022 | FR-I-01..04 / TPL Outputs#11 (A4 merged) | Kỳ trước > 0, kỳ này = 0 → GIAM, % = -100% | cb_nv_tw_01 login. KPI-04 kỳ trước = 4, kỳ này = 0. | — | 1. Apply filter. 2. Quan sát trend KPI-04. | (1) `huong_tang_giam=GIAM`. (2) `xu_huong_phan_tram=-100,0%`. (3) UI: ↓ "−100,0%" màu đỏ. | Edge 🟡 |
| TC-DASH-023 | FR-I-01..04 / TPL Outputs#11 (A4 merged) | Cả 2 kỳ = 0 → KHONG_DOI, % trống | cb_nv_tw_01 login. KPI nào đó kỳ trước=0, kỳ này=0. | — | 1. Apply filter. 2. Quan sát trend. | (1) `huong_tang_giam=KHONG_DOI`. (2) `xu_huong_phan_tram=NULL`. (3) UI "—" (KHÔNG kèm "0,0%"). | Edge 🟢 |
| TC-DASH-024 | FR-I-03 / SRS line 794 (A4 merged) | KPI-03 chú thích phụ "Tính đến" theo kỳ chọn (3 dạng) | cb_nv_tw_01 login. | (a) Kỳ hiện tại / (b) Năm 2025 + Tháng 6 / (c) Năm 2025 + Tháng "Tất cả" | 1. Apply 3 filter scenario. 2. Quan sát chú thích phụ KPI-03. | (a) "Tính đến hôm nay (DD/MM/YYYY)". (b) "Tính đến 30/06/2025". (c) "Tính đến 31/12/2025". (SRS line 794-796). | Edge 🟡 |
| TC-DASH-025 | FR-I-01 / BR-AUTH-08 (A4 merged) | BR-AUTH-08 — cb_nv_dp_01 (AG) chỉ đếm VV của AG, KHÔNG đếm BG | cb_nv_dp_01 (Sở TP An Giang) login. AG có 5 VV. BG (Bắc Giang) có 8 VV. | Default | 1. Vào `/dashboard`. 2. Quan sát KPI-02. | (1) KPI-02 = 5 (chỉ AG). (2) KPI không đếm 8 VV BG (BR-AUTH-08). (3) Chip phạm vi "Phạm vi: Sở Tư pháp An Giang". | Edge 🔴 |
| TC-DASH-026 | FR-I-01..04 / SRS line 779 number format (A4 merged) | Định dạng số vi-VN: 12345 → "12.345", 1234567 → "1,2 triệu" | cb_nv_tw_01 login. Có data lớn để test format. | KPI-01 = 12345. KPI-02 = 1234567. | 1. Vào `/dashboard`. 2. Quan sát hiển thị giá trị + tooltip. | (1) KPI-01 hiển thị "12.345" (dấu chấm). (2) KPI-02 hiển thị "1,2 triệu" + tooltip hover full "1.234.567" (SRS line 779). | Edge 🟢 |
| TC-DASH-027 | FR-I-03 / Processing step 3 + Outputs#10 (A4 merged) | `is_qua_khu_dong=TRUE` khi chọn kỳ quá khứ | cb_nv_tw_01 login. | nam=2025, thang=12 vs nam=2026, thang=hiện tại | 1. Apply nam=2025, thang=12. 2. Inspect output. 3. Đổi sang kỳ hiện tại. | (1) Kỳ 2025/12: `is_qua_khu_dong=TRUE`. (2) Kỳ hiện tại: `is_qua_khu_dong=FALSE`. (3) Auto-refresh + nút "Làm mới" + nhãn timestamp behavior khác (test ở file 06). | Edge 🟡 |
| TC-DASH-028 | FR-I-01..04 / TPL Outputs#9 (A4 merged) | `den_ngay_boundary` = NOW khi chọn năm/tháng hiện tại | cb_nv_tw_01 login. Now = 2026-05-10 14:30. | nam=2026 hiện tại, thang=5 hiện tại | 1. Apply filter. 2. Inspect output. | `den_ngay_boundary` ≈ NOW (2026-05-10 14:30:00). KHÔNG = 2026-05-31 23:59 (vì tháng hiện tại). (SRS line 754). | Edge 🟢 |
| TC-DASH-029 | FR-I-01..04 / TPL Outputs#11 + KHONG_DOI vs gạch (A4 merged) | KHONG_DOI dùng dấu `=` không dùng `—` (tránh trùng với "trống") | cb_nv_tw_01 login. Cả 2 kỳ KPI = 5. | — | 1. Apply filter. 2. Inspect icon trend. | (1) UI hiển thị `=` (hoặc tương đương rõ nghĩa "bằng nhau") + "0,0%" (SRS line 790 quote: "KHÔNG dùng dấu gạch ngang `—` làm biểu tượng cho 'Không đổi'"). | Edge 🟢 |

---

## F. TPL-DASH-KPI Outputs verify — KPI-02..04 (Codex P1-2 fill)

> Verify 12 outputs TPL-DASH-KPI (SRS line 198-213) cho từng KPI: `gia_tri`, `nhan`, `don_vi_tinh`, `drill_down_url`, `nam`, `thang`, `scope_label`, `tu_ngay_boundary`, `den_ngay_boundary`, `is_qua_khu_dong`, `xu_huong_phan_tram`, `huong_tang_giam`.

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|---------|---------------|----------------|-----------|-------------------|------------------|------|
| TC-DASH-225 | FR-I-02 / TPL-DASH-KPI Outputs (Codex P1-2 fill) | KPI-02 — verify đủ 12 outputs trên UI/network | cb_nv_tw_01 login. Có ≥1 VV `ngay_tiep_nhan` ∈ kỳ hiện tại + ≥1 VV ở kỳ trước (Tháng 3/2026). | nam=2026, thang=4 | 1. Vào `/dashboard`. 2. Open chrome-devtools Network → tìm response của endpoint KPI-02 (vd `/api/dashboard/kpi-02`). 3. Verify response payload + UI render. | Network response chứa đủ **12 fields**: (1) `gia_tri`=number; (2) `nhan`="Vụ việc đã tiếp nhận"; (3) `don_vi_tinh`="vụ việc"; (4) `drill_down_url` chứa `/vu-viec/danh-sach?date_field=ngay_tiep_nhan&nam=2026&thang=4&don_vi_cap=DP&don_vi_id=...`; (5) `nam`=2026; (6) `thang`=4; (7) `scope_label`="Tháng 4/2026"; (8) `tu_ngay_boundary`="2026-04-01T00:00:00"; (9) `den_ngay_boundary`= NOW (vì kỳ hiện tại); (10) `is_qua_khu_dong`=false; (11) `xu_huong_phan_tram`=number hoặc NULL; (12) `huong_tang_giam` ∈ {TANG, GIAM, KHONG_DOI}. UI render: giá trị + xu hướng + chú thích đơn vị "vụ việc". | Behavior 🔴 |
| TC-DASH-226 | FR-I-03 / TPL-DASH-KPI Outputs + ảnh chụp (Codex P1-2 fill) | KPI-03 — verify đủ 12 outputs (KPI ảnh chụp đặc biệt) + chú thích "Tính đến ..." | cb_nv_tw_01 login. Có ≥1 VV ở mỗi 5 trạng thái sống. Kỳ hiện tại = năm/tháng hiện tại. | Default kỳ hiện tại | 1. Vào `/dashboard`. 2. Network → KPI-03 response. 3. Verify UI chú thích "Tính đến hôm nay (DD/MM/YYYY)" (SRS line 794). | Response chứa 12 fields: (1) `gia_tri`=COUNT 5 sống; (2) `nhan`="Vụ việc đang hỗ trợ"; (3) `don_vi_tinh`="vụ việc"; (4) `drill_down_url` chứa `?trang_thai=DA_TIEP_NHAN,DANG_KIEM_TRA,YEU_CAU_BO_SUNG,DA_PHAN_CONG,DANG_XU_LY&don_vi_cap=...&don_vi_id=...` (KHÔNG có nam/thang vì ảnh chụp); (5) `nam`=current; (6) `thang`=current; (7) `scope_label` reflect kỳ; (8) `tu_ngay_boundary`=NULL hoặc đầu kỳ; (9) `den_ngay_boundary`= NOW; (10) `is_qua_khu_dong`=false; (11) `xu_huong_phan_tram`=number/NULL; (12) `huong_tang_giam`. **UI chú thích phụ**: "Tính đến hôm nay (DD/MM/YYYY)" (SRS line 794). | Behavior 🔴 |
| TC-DASH-227 | FR-I-04 / TPL-DASH-KPI Outputs + kỳ đóng (Codex P1-2 fill) | KPI-04 — verify đủ 12 outputs khi chọn kỳ ĐÃ ĐÓNG (`is_qua_khu_dong=true`) | cb_nv_tw_01 login. ≥3 VV HOAN_THANH `ngay_hoan_thanh` ∈ tháng 3/2026. | nam=2026, thang=3 (kỳ đã đóng) | 1. Vào `/dashboard`. 2. Đổi filter Năm=2026, Tháng=3 (kỳ đã đóng). Apply. 3. Network → KPI-04. 4. Verify `is_qua_khu_dong=true` + UI ẩn nút "Làm mới" + nhãn "Cập nhật lúc HH:mm" (SRS line 715-716). | (1) `is_qua_khu_dong=**true**` (key field cho kỳ đóng — SRS line 211). (2) `den_ngay_boundary`="2026-03-31T23:59:59" (cuối tháng 3, không phải NOW). (3) `scope_label`="Tháng 3/2026". (4) UI: nút "Làm mới" + nhãn "Cập nhật lúc HH:mm" **ẨN HOÀN TOÀN** (SRS line 715-716 quote "ẨN HOÀN TOÀN khi `is_qua_khu_dong=TRUE`"). (5) Đủ 12 fields còn lại. | Behavior 🔴 |

---

## Tổng kết file 01-TC

- **Tổng số TC: 25** (10 Happy + 3 Negative + 9 Edge + 3 Codex P1-2 fill — A4 merged + Codex inline)
- **Critical TC (🔴)**: TC-DASH-001, 002, 003, 004, 008, 016, 020, 025, 225, 226, 227
- **A4 merged 2026-05-10**: TC-DASH-020..029 (snapshot semantics + trend edge cases + format vi-VN + BR-AUTH-08 + boundary semantic)
- **Codex 2026-05-10 P1-2 fill**: TC-DASH-225 (KPI-02 outputs) + TC-DASH-226 (KPI-03 outputs với ảnh chụp + chú thích) + TC-DASH-227 (KPI-04 outputs kỳ đã đóng `is_qua_khu_dong=true`)
- **DEFERRED**: TC-DASH-016 (cần stub backend 5xx — Chrome DevTools network throttling fallback)
- **SPEC-CLARIFY refs**: (none new — TPL-DASH-KPI rất rõ ràng)
- **Drill-down**: chỉ verify URL params đúng spec (TC-006, 007, 008, 009, 225, 226, 227), KHÔNG vào module target

*Generated 2026-05-10 — Phase A3 + A4 merged + Codex P1-2 fill (manual edge case hunter)*
