# Test Cases — SCR-I-01 Vùng 1 + 2: Header + Bộ lọc (Năm + Tháng + L1 + L2)

> **SRS Ref**: SCR-I-01 Vùng 1 (`srs-fr-01-dashboard-v3.1.md` line 709-728), Vùng 2 (line 730-770), URL params silently fallback (line 768, 852), tab độc lập (line 853)
> **Ngày tạo**: 2026-05-10 (Phase A3 + A4 merged)
> **Đặc thù**:
> - Vùng 1: Breadcrumb + tiêu đề + nút "Làm mới" + nhãn "Cập nhật lúc HH:mm" + chip phạm vi (5 dòng state mapping per Vùng 1).
> - Vùng 2: Năm (bắt buộc, từ năm bắt đầu sd → năm hiện tại) + Tháng (Tất cả + 12 tháng cụ thể, năm hiện tại disable tháng tương lai) + L1 (DP/BN, locked cho user BN/DP) + L2 (Tất cả + danh sách đơn vị) + nút Áp dụng (mờ khi không pending) + nút Trở về mặc định (apply ngay không cần Áp dụng).
> - Pending state: change Năm/Tháng/L1/L2 → trạng thái pending; chỉ Apply mới commit.
> - Đổi L1 → L2 reset "Tất cả [cấp L1]" pending.
> - Năm hiện tại + Tháng tương lai → tự reset Tháng "Tất cả" (SRS line 740).
> - URL share giữ filter state, URL params invalid → silently fallback default (SRS line 768, 852).
> - Multi-tab: mỗi tab giữ filter state riêng (SRS line 853).
> - Chip phạm vi truncate >25 ký tự + tooltip full name (SRS line 717).
> - User BN/DP login: dropdown locked, KHÔNG hiển thị nhãn phụ "(khoá theo đơn vị bạn)" (SRS line 770).

---

## Quy ước

- **Priority**: 🔴 P0 (critical) · 🟡 P1 (high) · 🟢 P2 (medium)
- **TraceID**: `SCR-I-01 / {section}` link SRS line/heading

---

## A. Vùng 1 — HAPPY (Header + chip phạm vi)

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|---------|---------------|----------------|-----------|-------------------|------------------|------|
| TC-DASH-150 | SCR-I-01 / Vùng 1 #1-5 | Vùng 1 render đủ 5 thành phần | cb_nv_tw_01 login. | — | 1. Vào `/dashboard`. 2. Inspect Vùng 1 (header). | (1) Breadcrumb "Trang chủ > Tổng quan" (SRS line 713). (2) Tiêu đề "Tổng quan hệ thống". (3) Nút "Làm mới" + chỉ dấu trạng thái (kỳ hiện tại). (4) Nhãn "Cập nhật lúc HH:mm". (5) Chip phạm vi "Phạm vi: ..." (SRS line 717). | Happy 🔴 |
| TC-DASH-151 | SCR-I-01 / Vùng 1 chip mapping (SRS line 721-728) | Chip phạm vi mapping 5 state | cb_nv_tw_01 login. | (a) DP=NULL / (b) DP=ĐP X / (c) BN=NULL / (d) BN=BN X / (e) cb_nv_dp_01 locked | 1. Apply 5 filter scenario. 2. Quan sát chip text. | (a) "Phạm vi: Tất cả địa phương". (b) "Phạm vi: {tên ĐP X}". (c) "Phạm vi: Tất cả bộ ngành". (d) "Phạm vi: {tên BN X}". (e) "Phạm vi: {tên đơn vị user}". (SRS line 721-727 5 dòng). | Happy 🔴 |

---

## B. Vùng 2 — HAPPY (Bộ lọc Năm + Tháng + L1 + L2)

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|---------|---------------|----------------|-----------|-------------------|------------------|------|
| TC-DASH-152 | SCR-I-01 / Vùng 2 #6 (SRS line 740) | Dropdown Năm — options từ năm bắt đầu sd → năm hiện tại | cb_nv_tw_01 login. Năm bắt đầu sd = 2024. Năm hiện tại = 2026. | — | 1. Mở dropdown Năm. 2. Inspect options. | Options = [2024, 2025, 2026]. KHÔNG có "Tất cả" (SRS line 180 quote "KHÔNG có tùy chọn 'Tất cả'"). KHÔNG có 2027. Mặc định: 2026 (năm hiện tại). | Happy 🔴 |
| TC-DASH-153 | SCR-I-01 / Vùng 2 #7 (SRS line 741) | Dropdown Tháng — "Tất cả" + 12 tháng + năm hiện tại disable tháng tương lai | cb_nv_tw_01 login. Năm hiện tại = 2026, tháng hiện tại = 5. | nam=2026 | 1. Mở dropdown Tháng (đang chọn nam=2026). 2. Inspect options. | Options enabled = ["Tất cả", 1, 2, 3, 4, 5]. Options disabled (làm mờ) = [6, 7, 8, 9, 10, 11, 12] (tháng tương lai). Mặc định: "Tất cả" (SRS line 741). | Happy 🔴 |
| TC-DASH-154 | SCR-I-01 / Vùng 2 #7 năm quá khứ | Năm quá khứ → bật cả 12 tháng | cb_nv_tw_01 login. | nam=2025 (năm quá khứ) | 1. Đổi nam=2025. 2. Mở dropdown Tháng. | Options = ["Tất cả", 1..12] tất cả enabled (SRS line 741). | Happy 🟡 |
| TC-DASH-155 | SCR-I-01 / Vùng 2 #8 (SRS line 742) | Dropdown L1 — {Địa phương, Bộ ngành} + cb_nv_tw default DP | cb_nv_tw_01 login. | — | 1. Mở dropdown L1. 2. Inspect. | Options = [Địa phương, Bộ ngành]. Mặc định = Địa phương (SRS line 742). | Happy 🟡 |
| TC-DASH-156 | SCR-I-01 / Vùng 2 #9 (SRS line 743) | Dropdown L2 — "Tất cả [L1]" + danh sách đơn vị | cb_nv_tw_01 login. L1=DP. | — | 1. Mở dropdown L2 (L1=DP). 2. Inspect. | Options = ["Tất cả địa phương", + danh sách ĐP đang hoạt động]. Mặc định = "Tất cả địa phương" (SRS line 743). | Happy 🟡 |
| TC-DASH-157 | SCR-I-01 / Vùng 2 #10 (SRS line 744) | Pending state — change Năm/Tháng/L1/L2 → Apply mới commit | cb_nv_tw_01 login. KPI-01 = 5 (default). | Đổi Năm = 2025 | 1. Đổi Năm = 2025. 2. Quan sát data widget. 3. Click Apply. 4. Quan sát data. | (1) Sau bước 1: data KPI vẫn = 5 (filter cũ vẫn apply, chưa commit). Apply button bật. (2) Sau bước 3: 12 widget reload theo nam=2025, KPI cập nhật giá trị mới. | Happy 🔴 |
| TC-DASH-158 | SCR-I-01 / Vùng 2 #10 mờ khi no pending | Apply button mờ khi không có pending | cb_nv_tw_01 login. | — | 1. Vừa load `/dashboard`. 2. Inspect Apply button. | Button "Áp dụng" làm mờ (disabled) (SRS line 744). | Happy 🟢 |
| TC-DASH-159 | SCR-I-01 / Vùng 2 #11 (SRS line 745) | "Trở về mặc định" → reset filter + commit ngay (KHÔNG cần Apply) | cb_nv_tw_01 login. Đã đổi filter Năm=2025, L2=ĐP X. | — | 1. Đã đổi filter. 2. Click "Trở về mặc định". 3. Quan sát filter + data. | (1) Filter reset: Năm=năm hiện tại, Tháng="Tất cả", L1="Địa phương", L2="Tất cả địa phương" (mặc định cb_nv_tw). (2) Commit ngay — 12 widget reload (KHÔNG cần Apply). | Happy 🟡 |
| TC-DASH-160 | SCR-I-01 / Vùng 2 #8 (SRS line 742) | Đổi L1 → L2 tự reset "Tất cả [L1]" (pending) | cb_nv_tw_01 login. Đã chọn L1=DP, L2=ĐP X. | Đổi L1=BN | 1. Đã chọn L1=DP, L2=ĐP X. 2. Đổi L1 sang BN. 3. Inspect L2. | L2 tự đổi về "Tất cả bộ ngành" (pending — chưa commit per SRS line 742). | Happy 🟡 |
| TC-DASH-161 | SCR-I-01 / Vùng 2 #6 (SRS line 740) | Năm hiện tại + Tháng tương lai (từ trạng thái cũ) → tự reset Tháng "Tất cả" | cb_nv_tw_01 login. Đang chọn Năm=2025, Tháng=10. | Đổi Năm=2026 (năm hiện tại, tháng hiện tại=5) | 1. Đang ở Năm=2025+Tháng=10. 2. Đổi Năm=2026. 3. Inspect Tháng. | Tháng tự reset về "Tất cả" (vì 10 > 5 tháng hiện tại — tránh trạng thái vô lý "tháng tương lai" per SRS line 740). | Happy 🔴 |

---

## C. Vùng 1 + 2 — EDGE (A4 merged)

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|---------|---------------|----------------|-----------|-------------------|------------------|------|
| TC-DASH-165 | SCR-I-01 / Vùng 1 #5 (SRS line 717) (A4 merged) | Chip phạm vi truncate >25 ký tự + tooltip full | cb_nv_tw_01 login. ĐP có tên dài "Sở Tư pháp tỉnh Bà Rịa - Vũng Tàu" (>25 ký tự). | L2=ĐP đó | 1. Apply. 2. Hover chip. | (1) Chip text truncated với "..." (SRS line 717 quote "truncate với ellipsis '...'"). (2) Hover tooltip full name "Phạm vi: Sở Tư pháp tỉnh Bà Rịa - Vũng Tàu". | Edge 🟡 |
| TC-DASH-166 | SCR-I-01 / Vùng 2 user BN/DP locked (SRS line 770) (A4 merged) | User BN/DP login → L1+L2 disabled, KHÔNG nhãn phụ "(khoá theo đơn vị bạn)" | cb_nv_dp_01 (AG) login. | — | 1. Vào `/dashboard`. 2. Inspect dropdown L1+L2. | (1) L1 dropdown làm mờ (disabled) — KHÔNG đổi được. (2) L2 dropdown làm mờ — locked = "Sở TP An Giang". (3) **KHÔNG hiển thị nhãn phụ** "(khoá theo đơn vị bạn)" hay tương tự (SRS line 770 nguyên văn). (4) User tự nhận biết qua dropdown làm mờ + chip phạm vi. | Edge 🔴 |
| TC-DASH-167 | SCR-I-01 / URL share (SRS line 768, 852) (A4 merged) | URL share giữ filter state | cb_nv_tw_01 login. | URL `/dashboard?nam=2025&thang=4&don_vi_cap=BN&don_vi_id=BTC` | 1. Mở URL trực tiếp. 2. Inspect filter state. | (1) Năm = 2025. (2) Tháng = 4. (3) L1 = Bộ ngành. (4) L2 = BTC. (5) Data widget reload theo URL. (Tab độc lập per SRS line 853). | Edge 🟡 |
| TC-DASH-168 | SCR-I-01 / URL params invalid (SRS line 768) (A4 merged) | URL Năm out-of-range → silently fallback default (KHÔNG thông báo) | cb_nv_tw_01 login. | URL `/dashboard?nam=2099&thang=4` | 1. Mở URL. 2. Inspect filter + data. | (1) Năm fallback về năm hiện tại (2026) silently. (2) Tháng fallback về "Tất cả" silently. (3) **KHÔNG hiển thị thông báo** (SRS line 768 quote "tự đổi ngầm về mặc định — không hiển thị thông báo"). | Edge 🟡 |
| TC-DASH-169 | SCR-I-01 / URL don_vi_id invalid (SRS line 852) (A4 merged) | URL `don_vi_id` không tồn tại / `is_active=false` / cấp mismatched → silently fallback | cb_nv_tw_01 login. | URL `/dashboard?nam=2026&don_vi_id=99999` | 1. Mở URL. 2. Inspect filter. | (1) `don_vi_id` invalid → fallback về default "Tất cả [cấp L1]" silently (SRS line 852). (2) KHÔNG thông báo. | Edge 🟡 |
| TC-DASH-170 | SCR-I-01 / Multi-tab độc lập (SRS line 853) (A4 merged) | 2 tab giữ filter state riêng (KHÔNG sync cross-tab) | cb_nv_tw_01 login. | Tab1: Năm=2026 / Tab2: Năm=2025 | 1. Mở 2 tab `/dashboard`. 2. Tab1: chọn Năm=2026, Apply. 3. Tab2: chọn Năm=2025, Apply. 4. Đổi qua Tab1. | (1) Tab1 vẫn giữ filter Năm=2026 (KHÔNG bị overwrite bởi Tab2). (2) Tab2 vẫn Năm=2025. (3) Use case hợp lệ per SRS line 853. | Edge 🟡 |
| TC-DASH-171 | SCR-I-01 / Cross-year compare (SRS line 762) (A4 merged) | Tháng=1 → kỳ trước = Tháng 12 năm Y-1 (cross-year) | cb_nv_tw_01 login. | nam=2026, thang=1 | 1. Apply. 2. Inspect KPI trend. | (1) Kỳ này = Tháng 1/2026. (2) Kỳ trước tự suy ra = Tháng 12/2025 (cross-year per SRS line 762). (3) Trend KPI tính đúng. | Edge 🔴 |
| TC-DASH-172 | SCR-I-01 / Vùng 2 boundary năm bắt đầu sd (A4 merged) | Năm = năm bắt đầu sử dụng phần mềm (boundary min) | cb_nv_tw_01 login. Năm bắt đầu sd = 2024. | nam=2024 | 1. Đổi Năm=2024 (boundary min). 2. Apply. | Filter accept. Data widget reload theo nam=2024. KHÔNG có error. | Edge 🟢 |
| TC-DASH-173 | SCR-I-01 / Vùng 2 disable tháng tương lai (A4 merged) | Click vào tháng tương lai (làm mờ) → KHÔNG select | cb_nv_tw_01 login. Năm=2026 hiện tại, tháng hiện tại=5. | — | 1. Mở dropdown Tháng. 2. Try click Tháng 6 (làm mờ). | (1) Click không tác dụng (option disabled). (2) Tháng vẫn giữ giá trị cũ. | Edge 🟢 |
| TC-DASH-174 | SCR-I-01 / Vùng 2 SRS line 751-755 (A4 merged) | Boundary scope khác nhau theo state Năm/Tháng | cb_nv_tw_01 login. | (a) nam=2025, thang=6 / (b) nam=2025, thang=NULL / (c) nam=2026, thang=4 (< hiện tại 5) / (d) nam=2026, thang=5 (= hiện tại) / (e) nam=2026, thang=NULL | 1. Apply 5 scenario. 2. Inspect tu_ngay/den_ngay output. | (a) [01/06/2025 00:00 → 30/06/2025 23:59]. (b) [01/01/2025 00:00 → 31/12/2025 23:59]. (c) [01/04/2026 00:00 → 30/04/2026 23:59]. (d) [01/05/2026 00:00 → NOW]. (e) [01/01/2026 00:00 → NOW]. (SRS line 751-755 5 dòng). | Edge 🔴 |
| TC-DASH-175 | SCR-I-01 / Vùng 2 reset L2 keep Năm/Tháng (A4 merged) | "Trở về mặc định" reset L1/L2 nhưng cũng reset Năm/Tháng (full reset) | cb_nv_tw_01 login. Đã đổi filter Năm=2025, L1=BN, L2=BTC. | — | 1. Đổi filter. 2. Click "Trở về mặc định". 3. Inspect filter. | Reset toàn bộ filter (SRS line 745 quote "đặt lại tất cả bộ lọc về mặc định") — Năm=hiện tại + Tháng="Tất cả" + L1="Địa phương" + L2="Tất cả địa phương". | Edge 🟡 |
| TC-DASH-176 | SCR-I-01 / Vùng 2 invalid year < bắt đầu sd (A4 merged) | URL Năm < năm bắt đầu sd → silently fallback | cb_nv_tw_01 login. Năm bắt đầu sd = 2024. | URL `/dashboard?nam=2020` | 1. Mở URL. 2. Inspect Năm. | Năm fallback về năm hiện tại silently (SRS line 768). | Edge 🟡 |
| TC-DASH-177 | SCR-I-01 / Vùng 2 mismatch L1/L2 (A4 merged) | URL `don_vi_cap=DP` + `don_vi_id=BTC_BN_ID` (mismatched) → silently fallback | cb_nv_tw_01 login. | URL `/dashboard?don_vi_cap=DP&don_vi_id=BTC_BN_ID` | 1. Mở URL. 2. Inspect L2. | L2 fallback về "Tất cả địa phương" silently (cấp mismatched per SRS line 852 quote). | Edge 🟡 |
| TC-DASH-178 | SCR-I-01 / Vùng 1 nhãn timestamp cập nhật (A4 merged) | "Cập nhật lúc HH:mm" cập nhật sau mỗi lần tải | cb_nv_tw_01 login. Kỳ hiện tại. | — | 1. Vào `/dashboard` (note timestamp). 2. Click "Làm mới". 3. Đợi 60s tick. | Sau mỗi lần tải xong, nhãn cập nhật theo HH:mm hiện tại (SRS line 716 quote "Tự cập nhật sau mỗi lần tải xong"). | Edge 🟢 |
| TC-DASH-179 | SCR-I-01 / Vùng 2 disable tháng tương lai sau đổi Năm (A4 merged) | Năm hiện tại + Tháng đang chọn = "Tất cả" (default) → đổi sang Năm khác | cb_nv_tw_01 login. Default. | nam=2025 (đổi sang quá khứ) | 1. Default Năm=2026 + Tháng="Tất cả". 2. Đổi Năm=2025. 3. Inspect Tháng. | Tháng vẫn = "Tất cả" (KHÔNG bị reset vì "Tất cả" không phải tháng tương lai). | Edge 🟢 |

---

## Tổng kết file 07-TC

- **Tổng số TC: 23** (10 Happy + 0 Negative + 13 Edge — A4 merged inline)
- **Critical TC (🔴)**: TC-DASH-150, 152, 153, 157, 161, 166, 171, 174
- **A4 merged 2026-05-10**: TC-DASH-165..179 (chip truncate + locked không nhãn phụ + URL share/invalid + multi-tab + cross-year + boundary năm bắt đầu sd + disable tháng tương lai + boundary scope 5 scenarios + Trở về mặc định full reset + URL year < bắt đầu sd + mismatch L1/L2 + timestamp cập nhật + reset Năm sang quá khứ)
- **SPEC-CLARIFY refs**:
  - **SPEC-CLARIFY-DASH-04**: SRS line 768 nói "tự đổi ngầm" cho `nam` invalid — không rõ user thấy URL trên address bar có thay đổi không (rewrite URL hay giữ URL invalid). Assume rewrite URL về default cho consistency.

*Generated 2026-05-10 — Phase A3 + A4 merged (manual edge case hunter)*
