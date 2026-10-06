# A4 Edge Case Hunter Review — FR-01 Dashboard

> **Phase**: A4 (BMAD Edge Case Hunter — manual variant)
> **Approach**: For each TC file (01-08), identified candidate edge cases inline at section "C. Edge" with TraceID suffix `(A4 merged)`. This file = audit log of proposals + final inline mapping.
> **Generated**: 2026-05-10

---

## 1. Edge case categories explored (per task spec)

| Category | Definition | Applied to files |
|----------|------------|------------------|
| Boundary numeric | 0/1/max for Năm range, % values | 01, 04, 05, 07 |
| Boundary time | cuối tháng/đầu năm boundary, cross-year (T1 → T12 năm trước) | 01, 02, 03, 05, 07 |
| Concurrency | 2 tab refresh simultaneously, multi-tab filter state | 06, 07 |
| State transition affecting count mid-tick | TVV transition `DANG_HOAT_DONG → TAM_DUNG` during 60s window | 02, 06 |
| Audit log gaps | Kỳ trước data missing (INFO-DASH-04) | 01, 02, 04 |
| Empty data set | 0 records → "—" rendering | 01, 02, 04, 05 |
| Permission edge | Locked user thử PATCH URL params → ignored / silently fallback | 07, 08 |
| Locale | Số format vi-VN (1.000.000 / 1.000,5%) | 01 |
| KPI ngược chiều | TANG=đỏ, GIAM=xanh cho KPI-S-01/02 | 05 |
| Snapshot semantic | KPI-03/05/07 ảnh chụp tại boundary cuối kỳ vs hiện tại | 01, 02 |
| BR-SLA-05 boundary | mẫu số = 0 (không có HT + không có quá hạn) | 03 |
| BR-AUTH cross-unit | AG vs BG, ngang cấp BN/DP, TW thấy cấp con | 08 |
| URL params invalid | `nam` out of range, `don_vi_id` không tồn tại / mismatched, locked user URL override | 07 |

---

## 2. Edge case proposals → TC mapping (35 proposals → 49 inline merged)

Each row: A4 proposal → final TC ID merged inline (or REJECTED with reason).

### File 01 — KPI-01..04 Vụ việc + Hỏi đáp

| # | Edge Proposal | Merged TC | Notes |
|---|---------------|-----------|-------|
| A4-01-01 | KPI-03 ảnh chụp tại cuối kỳ đã đóng KHÁC tại hiện tại (cùng VV) | TC-DASH-020 | Critical — snapshot boundary semantic |
| A4-01-02 | Kỳ trước = 0, kỳ này > 0 → TANG, % trống | TC-DASH-021 | TPL-DASH-KPI Outputs#11 |
| A4-01-03 | Kỳ trước > 0, kỳ này = 0 → GIAM, % = -100% | TC-DASH-022 | |
| A4-01-04 | Cả 2 kỳ = 0 → KHONG_DOI, % trống | TC-DASH-023 | |
| A4-01-05 | KPI-03 chú thích "Tính đến" 3 dạng (hiện tại / Tháng cụ thể / "Tất cả") | TC-DASH-024 | SRS line 794 quote 3 quy ước |
| A4-01-06 | BR-AUTH-08 — cb_nv_dp_01 (AG) chỉ đếm AG, KHÔNG đếm BG | TC-DASH-025 | Cross-unit isolation |
| A4-01-07 | Locale vi-VN: 12345 → "12.345", 1234567 → "1,2 triệu" | TC-DASH-026 | SRS line 779 |
| A4-01-08 | `is_qua_khu_dong=TRUE` khi chọn kỳ quá khứ | TC-DASH-027 | TPL Outputs#10 |
| A4-01-09 | `den_ngay_boundary` = NOW khi chọn năm/tháng hiện tại | TC-DASH-028 | TPL Outputs#9 |
| A4-01-10 | KHONG_DOI dùng dấu `=` không dùng `—` | TC-DASH-029 | SRS line 790 quote |

### File 02 — KPI-05..07 KH + TVV

| # | Edge Proposal | Merged TC | Notes |
|---|---------------|-----------|-------|
| A4-02-01 | TVV transition `DANG_HOAT_DONG → TAM_DUNG` mid-tick → KPI-07 giảm sau auto-refresh | TC-DASH-045 | Critical — SRS line 396 quote |
| A4-02-02 | KPI-05 ảnh chụp tại cuối kỳ đã đóng vs hiện tại (cùng KH 3 ảnh chụp khác nhau) | TC-DASH-046 | Critical |
| A4-02-03 | User TW default DP → manual switch BN → switch back DP | TC-DASH-047 | KPI-07 default switch |
| A4-02-04 | KPI-06 boundary `ngay_ket_thuc` = ngày cuối tháng vs đầu tháng tiếp | TC-DASH-048 | Boundary inclusive |
| A4-02-05 | Drill-down KPI-07 với cb_nv_dp_01 (locked) — URL có `don_vi_id` user | TC-DASH-049 | BR-AUTH-08 |

### File 03 — UC8 Biểu đồ + SLA

| # | Edge Proposal | Merged TC | Notes |
|---|---------------|-----------|-------|
| A4-03-01 | Cỡ mẫu N<10 cho biểu đồ trái → asterisk + tooltip + (N=8) | TC-DASH-072 | Critical — SRS line 442 quote |
| A4-03-02 | Cỡ mẫu N<10 cho biểu đồ phải (vụ việc tooltip name khác) | TC-DASH-073 | |
| A4-03-03 | 1 đơn vị có data khi phạm vi nhiều → vẫn hiển thị 1 cột, không cảnh báo | TC-DASH-074 | |
| A4-03-04 | Ngày không có data (trục X = ngày) → bỏ qua, không vẽ cột | TC-DASH-075 | |
| A4-03-05 | Trục Y giới hạn cận dưới ≥ 0 (làm nổi chênh lệch nhỏ) | TC-DASH-076 | OBS — design system |
| A4-03-06 | Tổng chiều rộng cột vượt vùng hiển thị → cuộn ngang, trục Y cố định | TC-DASH-077 | OBS — design system |
| A4-03-07 | BR-SLA-05 mẫu số = 0 (không HT + không quá hạn) → biểu đồ phải trống | TC-DASH-078 | |
| A4-03-08 | Cross-year — Tháng 1 → kỳ trước = Tháng 12 năm Y-1 | TC-DASH-079 | SRS line 762 |

### File 04 — UC9 Biểu đồ vành

| # | Edge Proposal | Merged TC | Notes |
|---|---------------|-----------|-------|
| A4-04-01 | Audit log thiếu kỳ trước → trend "—" cho cả 2 chỉ số | TC-DASH-093 | |
| A4-04-02 | Kỳ trước = 0 học viên, kỳ này > 0 → trend "—" + TANG | TC-DASH-094 | |
| A4-04-03 | Tỷ lệ đạt = 100% (tất cả học viên Đạt) | TC-DASH-095 | Boundary |
| A4-04-04 | Tỷ lệ đạt = 0% (tất cả KHONG_DAT) | TC-DASH-096 | Boundary |
| A4-04-05 | Boundary điểm KT 0 vs 10 (entity constraint range) | TC-DASH-097 | SRS line 1080 |
| A4-04-06 | Học viên `diem_kiem_tra=NULL` → loại khỏi sample_size + SPEC-CLARIFY-01 | TC-DASH-098 | SRS line 518 + SPEC-CLARIFY-DASH-01 |

### File 05 — KPI-S-01/02 KPI bổ sung

| # | Edge Proposal | Merged TC | Notes |
|---|---------------|-----------|-------|
| A4-05-01 | KPI-S-01 KPI ngược chiều — TANG = ĐỎ | TC-DASH-114 | Critical — SRS line 784 quote |
| A4-05-02 | KPI-S-02 KPI ngược chiều — GIAM = XANH | TC-DASH-115 | Critical |
| A4-05-03 | Boundary T6 → T2 cuối tuần (T7+CN không đếm BR-CALC-03) | TC-DASH-116 | |
| A4-05-04 | KPI-S-01 = 0% boundary (mẫu số > 0 nhưng tử số = 0) | TC-DASH-117 | |
| A4-05-05 | KPI-S-01 = 100% boundary (5 HT, 5 đều qua bổ sung) | TC-DASH-118 | |
| A4-05-06 | KPI-S-02 cross-month boundary (tiếp nhận cuối tháng, HT đầu tháng sau) | TC-DASH-119 | |

### File 06 — Auto-refresh

| # | Edge Proposal | Merged TC | Notes |
|---|---------------|-----------|-------|
| A4-06-01 | Đơn vị đang chọn bị vô hiệu hóa → fallback "Tất cả [cấp L1]", KHÔNG thông báo | TC-DASH-140 | Critical — SRS line 653 |
| A4-06-02 | 5/12 widget fail (chưa đủ 50%) → KHÔNG banner | TC-DASH-141 | Boundary 50% |
| A4-06-03 | 2 tab cùng visible → mỗi tab tự refresh độc lập (KHÔNG sync) | TC-DASH-142 | SRS line 853 |
| A4-06-04 | Kỳ đóng + click vào header → KHÔNG có nút "Làm mới" để click | TC-DASH-143 | SRS line 715 |
| A4-06-05 | Banner ≥50% sau 5 chu kỳ — vẫn dòng phụ "3 lần" KHÔNG tăng số | TC-DASH-144 | Text stable |
| A4-06-06 | Tab hidden NGAY SAU click Apply filter pending | TC-DASH-145 | Concurrency timing |
| A4-06-07 | F5 reload trong khi 12 widget đang tải | TC-DASH-146 | Concurrency |
| A4-06-08 | Multiple widgets timeout cùng lúc — vẫn KHÔNG toast (3/12) | TC-DASH-147 | SRS line 651 |
| A4-06-09 | Click "Tải lại" trên banner → 12 widget reload đồng loạt + state | TC-DASH-148 | |
| A4-06-10 | Click "Thử lại" trên Trạng thái 28 widget → chỉ widget đó reload | TC-DASH-149 | Per-widget isolation |

### File 07 — SCR-I-01 Vùng 1+2

| # | Edge Proposal | Merged TC | Notes |
|---|---------------|-----------|-------|
| A4-07-01 | Chip phạm vi truncate >25 ký tự + tooltip full | TC-DASH-165 | SRS line 717 |
| A4-07-02 | User BN/DP locked, KHÔNG nhãn phụ "(khoá theo đơn vị bạn)" | TC-DASH-166 | Critical — SRS line 770 |
| A4-07-03 | URL share giữ filter state | TC-DASH-167 | SRS line 768, 853 |
| A4-07-04 | URL Năm out-of-range → silently fallback (KHÔNG thông báo) | TC-DASH-168 | SRS line 768 |
| A4-07-05 | URL `don_vi_id` không tồn tại / `is_active=false` / cấp mismatched → fallback | TC-DASH-169 | SRS line 852 |
| A4-07-06 | Multi-tab độc lập (KHÔNG sync cross-tab) | TC-DASH-170 | SRS line 853 |
| A4-07-07 | Cross-year: Tháng=1 → kỳ trước = Tháng 12 năm Y-1 | TC-DASH-171 | Critical — SRS line 762 |
| A4-07-08 | Năm = năm bắt đầu sd phần mềm (boundary min) | TC-DASH-172 | |
| A4-07-09 | Click vào tháng tương lai (làm mờ) → KHÔNG select | TC-DASH-173 | |
| A4-07-10 | Boundary scope khác nhau theo state Năm/Tháng (5 scenario) | TC-DASH-174 | Critical — SRS line 751-755 |
| A4-07-11 | "Trở về mặc định" reset full filter (Năm/Tháng/L1/L2) | TC-DASH-175 | SRS line 745 |
| A4-07-12 | URL Năm < năm bắt đầu sd → silently fallback | TC-DASH-176 | |
| A4-07-13 | URL `don_vi_cap` mismatched với `don_vi_id` → fallback | TC-DASH-177 | SRS line 852 |
| A4-07-14 | Nhãn timestamp cập nhật sau mỗi lần tải | TC-DASH-178 | SRS line 716 |
| A4-07-15 | Đổi Năm sang quá khứ + Tháng="Tất cả" → KHÔNG bị reset Tháng | TC-DASH-179 | |

### File 08 — Permission Matrix

| # | Edge Proposal | Merged TC | Notes |
|---|---------------|-----------|-------|
| A4-08-01 | cb_nv_dp_01 (AG) KHÔNG đếm vụ việc của cb_nv_dp_02 (BG) | TC-DASH-195 | Critical — BR-AUTH-08 + BR-AUTH-03 |
| A4-08-02 | cb_nv_bn_01 (BKH) KHÔNG đếm BTC | TC-DASH-196 | Critical — BR-AUTH-03 ngang cấp BN |
| A4-08-03 | cb_nv_tw_01 (TW) thấy cấp con (DP scope: ĐP1+ĐP2) | TC-DASH-197 | Critical — BR-AUTH-04 |
| A4-08-04 | TW switch L1='BN' → KPI đếm BN scope (BN1+BN2) | TC-DASH-198 | BR-AUTH-04 + L1 switch |
| A4-08-05 | Locked user (cb_nv_dp_01) PATCH URL `don_vi_id=BG` → ignored | TC-DASH-199 | Critical — security boundary + SPEC-CLARIFY-DASH-05 |

---

## 3. REJECTED edge cases (with reason)

| # | Edge Proposal | Rejected Reason |
|---|---------------|-----------------|
| R-01 | Test KPI-S-02 ngày lễ giữa kỳ (lễ rơi vào T2-T6) cho FR-VIII-29 | Out of scope — đã test ở Nhóm VIII / FR-VIII-29 ngày lễ. Memory rule: don't repeat đã test ở module khác. |
| R-02 | Test BR-CALC-03 chi tiết deadline calculation | Out of scope — Nhóm VIII test riêng. Dashboard chỉ kiểm KPI-S-02 trừ ngày lễ (TC-DASH-103). |
| R-03 | Backend stub fail hết 12/12 widget | DEFERRED — cần dev hook stub. Mark trong file 06 deferred section. |
| R-04 | Test responsive breakpoint cụ thể (mobile/tablet) | Out of scope — Design system decision (SRS line 855-861). |
| R-05 | Drill-down deep test ở module target (data scope filter actually apply) | Out of scope per task: "Don't include drill-down deep tests — only verify URL params correct". OBS data scope tại module target. |
| R-06 | Test color/icon spec cụ thể của design system | Out of scope — Design system decision. |
| R-07 | DN/NHT/TVV/CG có quyền gì khác ngoài DASHBOARD_VIEW | Out of scope — Permission Matrix file 08 chỉ test 8 quyền dashboard. CRUD entity-level permissions tại srs-v3.md Section 3.4.2 (cross-ref). |

---

## 4. SPEC-CLARIFY summary (5 active)

| ID | File | Issue | Recommendation |
|----|------|-------|----------------|
| SPEC-CLARIFY-DASH-01 | 04 | Học viên `diem_kiem_tra=NULL` có vào mẫu số tỷ lệ đạt? | Likely loại — chỉ count HV có điểm + xếp loại. BA confirm. |
| SPEC-CLARIFY-DASH-02 | 05 | KPI-S-01 đơn vị `xu_huong_phan_tram` là % point hay % relative? | Assume % relative theo TPL Processing line 195. BA confirm format display. |
| SPEC-CLARIFY-DASH-03 | 06 | Text Trạng thái 28 ("Không tải được dữ liệu") nguyên văn hay design custom? | Assume nguyên văn từ SRS line 841. |
| SPEC-CLARIFY-DASH-04 | 07 | URL params invalid → rewrite URL về default hay giữ URL invalid? | Assume rewrite cho consistency. BA/dev confirm. |
| SPEC-CLARIFY-DASH-05 | 08 | Locked user PATCH URL `don_vi_id=cross-unit` → fallback "Tất cả" hay locked override (giữ đơn vị user)? | Assume locked override (security boundary mạnh hơn URL fallback). BA confirm. |

---

## 5. DEFERRED tests (cần stub backend / hook đặc biệt)

| TC ID | Lý do | Workaround |
|-------|-------|------------|
| TC-DASH-016 | Cần stub backend 5xx cho 1 endpoint cụ thể | Chrome DevTools network block (mcp__chrome-devtools__evaluate_script + intercept) |
| TC-DASH-130, 131, 132, 133, 134 | Cần stub backend 5xx + delay 60s + persistent block 3 chu kỳ | DevTools network throttling fallback |
| TC-DASH-141, 144, 147 | Cần stub backend 5xx cho ≥6 endpoint cùng lúc | DevTools batch block |
| TC-DASH-148, 149 | Trigger Trạng thái 28 → click retry button | Cần TC-130/131 setup pre-condition |
| TC-DASH-135 | Sysop revoke role giữa phiên | Cần sysop hook + cb_pd_tw_01 hỗ trợ revoke |

---

## 6. Total summary

- **Total A4 proposals**: 49 inline (across 8 files)
- **Total REJECTED**: 7 (out of scope)
- **Active SPEC-CLARIFY**: 5 (DASH-01 đến DASH-05)
- **DEFERRED tests**: 11 (cần stub backend)

*Generated 2026-05-10 — Phase A4 (Edge Case Hunter manual variant)*
