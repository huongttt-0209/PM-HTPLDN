# Test Cases — FR-I-CROSS-02: Auto-refresh 60s + Per-widget fail isolation

> **SRS Ref**: FR-I-CROSS-02 (`srs-fr-01-dashboard-v3.1.md` line 633-668), Trạng thái 28-30 (line 837-843), kiến trúc resilience (line 891-899)
> **Ngày tạo**: 2026-05-10 (Phase A3 + A4 merged)
> **Đặc thù**: 60s tick → 12 widget song song (9 KPI + 3 chart). Tab visibility hidden → pause; visible → tải lại ngay. Kỳ đóng → ẨN HOÀN TOÀN nút "Làm mới" + nhãn timestamp. Per-widget fail isolation (Trạng thái 28/29). ≥50% widget fail → banner Trạng thái 30 (page-level) + sau 3 chu kỳ liên tiếp → banner kèm dòng phụ. Quyền user thay đổi → tự logout. Đơn vị bị vô hiệu hóa → fallback "Tất cả [cấp L1]". Click "Làm mới" disabled + spinner. Filter pending KHÔNG bị overwrite. KHÔNG toast/modal cấp trang khi widget timeout.

---

## Quy ước

- **Priority**: 🔴 P0 (critical) · 🟡 P1 (high) · 🟢 P2 (medium)
- **TraceID**: `FR-I-CROSS-02 / {section}` link SRS line/heading
- **Pre-conditions mặc định**: User đã login + `DASHBOARD_VIEW`. Headless browser hỗ trợ `Page Visibility API` qua `evaluate_script`.

---

## A. Auto-refresh — HAPPY

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|---------|---------------|----------------|-----------|-------------------|------------------|------|
| TC-DASH-120 | FR-I-CROSS-02 / Processing step 1 + AC#1 | 60s tick auto-refresh 12 widget song song | cb_nv_tw_01 login. Kỳ hiện tại. | Default | 1. Vào `/dashboard`. 2. Chờ 60s. 3. Inspect 12 widget reload. | (1) Sau 60s, network tab hiển thị 12 request song song (9 KPI endpoint + 3 chart endpoint per SRS line 648). (2) Widget update giá trị + chỉ dấu xu hướng. (3) Nhãn "Cập nhật lúc HH:mm" cập nhật. | Happy 🔴 |
| TC-DASH-121 | FR-I-CROSS-02 / Processing step 2 + AC#2 (SRS line 659) | Tab visibility hidden → pause auto-refresh | cb_nv_tw_01 login. | Switch tab via `evaluate_script` → `Object.defineProperty(document, 'visibilityState', {value: 'hidden'})` + dispatchEvent('visibilitychange') | 1. Vào `/dashboard`. 2. Switch tab (hidden). 3. Chờ 90s. 4. Inspect network. | KHÔNG có request mới (auto-refresh paused per SRS line 649). | Happy 🔴 |
| TC-DASH-122 | FR-I-CROSS-02 / Processing step 2 + AC#3 (SRS line 660) | Tab visible trở lại → tải lại ngay + reset timer | cb_nv_tw_01 login. Tab đang hidden 30s. | Switch tab visible | 1. Tab visible (dispatchEvent visibilitychange). 2. Inspect network. | (1) NGAY LẬP TỨC 12 request được gọi (KHÔNG đợi tick 60s). (2) Timer reset về 0. (3) Filter pending nếu có giữ nguyên (SRS line 660). | Happy 🔴 |
| TC-DASH-123 | FR-I-CROSS-02 / Processing step 3 + AC#4 (SRS line 661) | Kỳ đóng (`is_qua_khu_dong=TRUE`) → ẨN HOÀN TOÀN nút "Làm mới" + nhãn timestamp | cb_nv_tw_01 login. | nam=2025, thang=6 (kỳ đóng) | 1. Apply filter kỳ đóng. 2. Inspect Vùng 1 header. | (1) Nút "Làm mới" KHÔNG hiển thị (display:none, không chỉ disabled — SRS line 715 + 661 quote "ẨN HOÀN TOÀN"). (2) Nhãn "Cập nhật lúc HH:mm" KHÔNG hiển thị (SRS line 716 + 661). (3) Auto-refresh paused. | Happy 🔴 |
| TC-DASH-124 | FR-I-CROSS-02 / AC#5 (SRS line 662) | Đổi bộ lọc về kỳ hiện tại → cả 2 hiển thị lại + tự làm mới chạy lại | cb_nv_tw_01 login. Đang ở kỳ đóng (124). | Đổi nam=hiện tại, thang=NULL | 1. Đổi filter sang kỳ hiện tại. 2. Apply. 3. Inspect header. | (1) Nút "Làm mới" hiển thị lại. (2) Nhãn "Cập nhật lúc HH:mm" hiển thị lại. (3) Auto-refresh chạy lại. | Happy 🔴 |
| TC-DASH-125 | FR-I-CROSS-02 / Processing step 8 + AC#11 (SRS line 668) | Click "Làm mới" → button disabled + spinner; bật lại khi xong | cb_nv_tw_01 login. Kỳ hiện tại. | — | 1. Vào `/dashboard`. 2. Click nút "Làm mới". 3. Inspect button state. | (1) Button làm mờ + chỉ dấu spinner đang tải. (2) 12 request đồng loạt. (3) Khi xong (success hoặc error), button bật lại. (4) Chống click chồng — nhấn lần 2 trong khi đang tải KHÔNG gọi thêm. | Happy 🟡 |
| TC-DASH-126 | FR-I-CROSS-02 / AC#6 + Processing step 1 (SRS line 648, 663) | Filter pending KHÔNG bị overwrite bởi auto-refresh tick | cb_nv_tw_01 login. Đang chỉnh filter (Năm hoặc Tháng), CHƯA Apply. | Tháng đang chọn = 3 (pending) | 1. Vào `/dashboard`. 2. Mở dropdown Tháng, chọn 3 (pending — chưa Apply). 3. Chờ 60s tick. 4. Inspect dropdown Tháng + dữ liệu. | (1) Dropdown Tháng vẫn = 3 (pending — KHÔNG bị tick reset, SRS line 648). (2) Dữ liệu widget reload theo filter đã apply trước (KHÔNG theo pending). | Happy 🔴 |

---

## B. Auto-refresh — NEGATIVE / FAIL HANDLING

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|---------|---------------|----------------|-----------|-------------------|------------------|------|
| TC-DASH-130 | FR-I-CROSS-02 / Processing step 4 + AC#8 (SRS line 651, 665) | 1 widget timeout 30s → Trạng thái 28 cục bộ, KHÔNG toast/modal toàn trang | cb_nv_tw_01 login. Block `/api/dashboard/kpi-02` với delay 60s qua DevTools network throttling. | — | 1. Vào `/dashboard` (lần đầu). 2. Đợi 30s timeout cho KPI-02. 3. Inspect KPI-02 + page-level. | (1) KPI-02 widget hiển thị Trạng thái 28: text "Không tải được dữ liệu" + nút "Thử lại" cục bộ widget (SRS line 841). (2) **KHÔNG có toast/modal page-level** (SRS line 651 quote "KHÔNG hiển thị thông báo nổi / hộp thoại cấp trang"). (3) 11 widget khác render bình thường. (4) Per-widget fail isolation OK. | Negative 🔴 |
| TC-DASH-131 | FR-I-CROSS-02 / Trạng thái 29 (SRS line 842) | Đã load OK + auto-refresh sau fail → giữ giá trị cũ + chỉ dấu "Dữ liệu cũ" | cb_nv_tw_01 login. KPI-02 đã load OK lần đầu = 5. Sau đó endpoint trả 5xx ở tick tiếp. | Block sau lần 1 thành công | 1. Load lần 1 (KPI-02=5). 2. Block endpoint. 3. Đợi tick 60s. | (1) KPI-02 vẫn hiển thị "5" (giá trị cũ — SRS line 842). (2) Chỉ dấu "Dữ liệu cũ" (SRS line 842). (3) KHÔNG hiển thị mốc thời gian. (4) KHÔNG có nút "Thử lại" tại widget — user dùng "Làm mới" tại header (SRS line 121, 842). | Negative 🔴 |
| TC-DASH-132 | FR-I-CROSS-02 / Trạng thái 30 (SRS line 843, AC#10) | ≥50% widget (≥6/12) cùng fail → banner Trạng thái 30 page-level | cb_nv_tw_01 login. Block 6/12 endpoint trả 5xx. | Block KPI-01..04 + KPI-S-01..02 (6 endpoint) | 1. Vào `/dashboard`. 2. Đợi tick. 3. Inspect page-level. | (1) Banner cấp trang trên đầu Dashboard text "**Không tải được dữ liệu**" + nút "**Tải lại**" (SRS line 843). (2) 6 widget riêng vẫn giữ Trạng thái 28/29 cục bộ. (3) Click "Tải lại" tải lại đồng loạt 12 widget. | Negative 🔴 |
| TC-DASH-133 | FR-I-CROSS-02 / Trạng thái 30 + AC#10 (SRS line 654, 667) | Sau 3 chu kỳ liên tiếp banner vẫn xuất hiện → banner kèm dòng phụ | cb_nv_tw_01 login. Block ≥6/12 endpoint suốt 3 chu kỳ liên tiếp. | Persistent block | 1. Vào `/dashboard`. 2. Đợi 3 chu kỳ 60s liên tiếp (~3 phút). 3. Inspect banner ở chu kỳ 4. | Banner kèm dòng phụ "**Đã thử lại 3 lần không thành công. Liên hệ quản trị viên nếu vấn đề tiếp diễn.**" (SRS line 667 nguyên văn). | Negative 🟡 |
| TC-DASH-134 | FR-I-CROSS-02 / Trạng thái 30 hide rule (SRS line 843) | Banner ẨN khi ≥1 chu kỳ tải thành công toàn bộ | cb_nv_tw_01 login. Banner đang hiển thị (132). Unblock endpoint. | — | 1. Banner đang hiển thị. 2. Unblock 6 endpoint. 3. Click "Tải lại" trên banner. | (1) 12 widget reload thành công. (2) Banner ẨN ngay (SRS line 843 quote "Ẩn banner ngay khi có ≥ 1 chu kỳ tải thành công toàn bộ widget"). | Negative 🟡 |
| TC-DASH-135 | FR-I-CROSS-02 / Processing step 5 + AC#7 (SRS line 652, 664) | Quyền user thay đổi giữa phiên (revoke) → tự logout + redirect login (KHÔNG dialog tại Dashboard) | cb_nv_tw_01 login. Sysop revoke role giữa phiên. | Sysop disable account / revoke `DASHBOARD_VIEW` | 1. Vào `/dashboard`. 2. Sysop revoke role. 3. Đợi tick 60s. | (1) Tự navigate về `/login` (SRS line 652 quote "tự vô hiệu Dashboard và chuyển hướng về trang đăng nhập qua tầng xác thực chung"). (2) **KHÔNG hiển thị dialog/toast tại Dashboard** (SRS line 652, 664). | Negative 🔴 |

---

## C. Auto-refresh — EDGE (A4 merged)

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|---------|---------------|----------------|-----------|-------------------|------------------|------|
| TC-DASH-140 | FR-I-CROSS-02 / Processing step 6 + AC#9 (SRS line 653, 666) (A4 merged) | Đơn vị đang chọn bị vô hiệu hóa giữa phiên → fallback "Tất cả [cấp L1]" | cb_nv_tw_01 login. Đã chọn L2=ĐP X (đang active). Sysop disable ĐP X giữa phiên. | — | 1. Đã chọn L2=ĐP X. 2. Sysop disable ĐP X. 3. Đợi tick auto-refresh tải lại dropdown. 4. Inspect L2. | (1) L2 tự đổi về "Tất cả địa phương" (SRS line 653, 666). (2) **KHÔNG hiển thị thông báo** (SRS line 653 quote). (3) Dữ liệu widget reload theo scope mới. | Edge 🔴 |
| TC-DASH-141 | FR-I-CROSS-02 / Processing step 4 + 7 + AC#8 (A4 merged) | 5/12 widget fail (chưa đủ 50%) → KHÔNG banner | cb_nv_tw_01 login. Block 5/12 endpoint. | — | 1. Vào `/dashboard`. 2. Đợi tick. 3. Inspect page-level. | (1) **KHÔNG có banner** (5/12 < 50% — SRS line 843 ngưỡng ≥6/12). (2) 5 widget có Trạng thái 28 cục bộ riêng. (3) 7 widget khác render OK. | Edge 🟡 |
| TC-DASH-142 | FR-I-CROSS-02 / Concurrency 2 tab (A4 merged) | 2 tab cùng tab visible → mỗi tab tự refresh độc lập | cb_nv_tw_01 login. | Mở 2 tab `/dashboard` | 1. Mở tab1 + tab2. 2. Inspect network mỗi tab. | (1) Mỗi tab có timer riêng. (2) Tab nào active thì refresh tab đó. (3) KHÔNG sync cross-tab. (Tab độc lập per SRS line 853). | Edge 🟡 |
| TC-DASH-143 | FR-I-CROSS-02 / SRS line 716 (A4 merged) | Kỳ đóng + click vào header cũ → KHÔNG có nút Làm mới để click | cb_nv_tw_01 login. Apply filter kỳ đóng. | nam=2025, thang=6 | 1. Apply. 2. Try locate nút "Làm mới". | (1) Nút "Làm mới" KHÔNG còn trong DOM (display:none) per SRS line 715. (2) User KHÔNG có cách trigger refresh thủ công cho kỳ đóng (data không đổi nên KHÔNG cần). | Edge 🟢 |
| TC-DASH-144 | FR-I-CROSS-02 / SRS line 666 (A4 merged) | Banner ≥50% sau 5 chu kỳ — vẫn dòng phụ "3 lần" KHÔNG tăng số | cb_nv_tw_01 login. Block ≥6/12 suốt 5 chu kỳ. | — | 1. Đợi 5 chu kỳ. 2. Inspect banner text. | Banner kèm dòng phụ "Đã thử lại 3 lần không thành công..." vẫn ổn định, KHÔNG tăng "5 lần" hay "10 lần" (SRS line 667 chỉ có dòng "3 lần" — text cố định). | Edge 🟢 |
| TC-DASH-145 | FR-I-CROSS-02 / Tab hidden ngay sau Apply filter (A4 merged) | Tab hidden NGAY SAU click Apply filter pending | cb_nv_tw_01 login. Đang có filter pending. | — | 1. Đổi Tháng pending. 2. Click Apply. 3. NGAY LẬP TỨC switch tab hidden trước khi response về. 4. Switch tab visible sau 30s. | (1) Apply request gửi đi. (2) Khi visible lại: Dashboard tải lại ngay với filter đã apply. (3) Filter pending cũng giữ nguyên (SRS line 649). | Edge 🟡 |
| TC-DASH-146 | FR-I-CROSS-02 / Page reload trong khi đang tải (A4 merged) | F5 reload trong khi 12 widget đang tải | cb_nv_tw_01 login. | — | 1. Vào `/dashboard`. 2. F5 ngay khi đang load. 3. Inspect. | Reload thành công, 12 widget tải lại từ đầu, KHÔNG có error/duplicated request. | Edge 🟢 |
| TC-DASH-147 | FR-I-CROSS-02 / SRS line 651 (A4 merged) | Multiple widgets timeout cùng lúc — vẫn KHÔNG toast | cb_nv_tw_01 login. Block 3 endpoint trả 5xx (3 widgets timeout ≠ 50%). | — | 1. Vào `/dashboard`. 2. Đợi timeout. 3. Inspect page-level. | (1) 3 widget có Trạng thái 28 cục bộ. (2) **KHÔNG có toast/modal page-level** (3/12 < 50%, KHÔNG đủ banner ngưỡng). (3) Per-widget fail isolation per SRS line 651. | Edge 🟡 |
| TC-DASH-148 | FR-I-CROSS-02 / Click "Tải lại" trên banner (A4 merged) | Click banner "Tải lại" → 12 widget reload đồng loạt + banner state | cb_nv_tw_01 login. Banner đang hiển thị (≥6 fail). | — | 1. Banner. 2. Click "Tải lại". 3. Inspect network + state. | (1) 12 request gọi đồng loạt (KHÔNG đợi tick). (2) Nếu success: banner ẩn (134). (3) Nếu vẫn fail ≥50%: banner vẫn hiển thị, đếm chu kỳ tăng. | Edge 🟡 |
| TC-DASH-149 | FR-I-CROSS-02 / Trạng thái 28 retry button (A4 merged) | Click "Thử lại" trên Trạng thái 28 widget riêng → chỉ widget đó reload | cb_nv_tw_01 login. KPI-02 widget Trạng thái 28. Endpoint unblock. | — | 1. KPI-02 = Trạng thái 28. 2. Click "Thử lại" trên widget. 3. Inspect network. | (1) Chỉ 1 request `/api/dashboard/kpi-02` (KHÔNG kéo 12 widget khác). (2) Nếu success: widget render giá trị + chỉ dấu xu hướng. | Edge 🟡 |

---

## Tổng kết file 06-TC

- **Tổng số TC: 20** (7 Happy + 6 Negative + 10 Edge — A4 merged inline)
- **Critical TC (🔴)**: TC-DASH-120, 121, 122, 123, 124, 126, 130, 131, 132, 135, 140
- **A4 merged 2026-05-10**: TC-DASH-140..149 (vô hiệu hóa đơn vị + boundary 5/12 + 2 tab + kỳ đóng KHÔNG có refresh + dòng phụ stable + tab hidden post-Apply + F5 reload + multiple timeout + click Tải lại banner + click Thử lại widget)
- **DEFERRED**: TC-130, 131, 132, 133, 134, 141, 144, 147, 148, 149 cần stub backend 5xx (Chrome DevTools network block fallback per memory `htpldn_mcp_ui_patterns`). Mark OBS nếu không trigger được trong env.
- **SPEC-CLARIFY refs**:
  - **SPEC-CLARIFY-DASH-03**: SRS không quy định cụ thể text Trạng thái 28 ("Không tải được dữ liệu") vs custom design — assume nguyên văn từ SRS line 841.
- **Behavior tools**: Cần `evaluate_script` + DevTools network throttling/block. Tab visibility test qua `Object.defineProperty(document, 'visibilityState')` + `dispatchEvent`.

*Generated 2026-05-10 — Phase A3 + A4 merged (manual edge case hunter)*
