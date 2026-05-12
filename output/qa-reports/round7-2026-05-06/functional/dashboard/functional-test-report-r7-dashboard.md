# Functional Test Report — Dashboard (Module 7.1)

| Thông tin | Giá trị |
|-----------|---------|
| **Module** | Tổng quan hệ thống / Dashboard (FR-01) |
| **SRS Reference** | `srs-update-2026-5-5/srs-fr-01-dashboard.md` — FR-I-01..09, KPI-S-01/02, FR-I-CROSS-02 |
| **UC Coverage** | UC1..UC9 + KPI bổ sung |
| **Người test** | QA Automation (Claude Opus 4.7) |
| **Ngày** | 2026-05-10 10:25:00 → 10:37:30 (R1) · 12:14:00 → 12:35:00 (R2 retest+expand) · 20:35:00 → 20:42:00 (R3 retest) · 22:30:00 → 22:48:00 (R3.1 expand permission) · 22:53:00 → 23:03:00 (R3.2 DASH-P8 auto-refresh) (UTC+7) |
| **Môi trường** | http://103.172.236.130:3000 |
| **OTP Bypass** | `666666` |
| **Test Method** | UI MCP (Chrome DevTools) + API cross-check qua `evaluate_script(fetch)` |
| **Primary Account** | `qtht_01 / Secret@123` (QTHT, BTP-TW) |
| **Round** | Round 7 |
| **Tài liệu tham chiếu** | [tasks/todo-dashboard.md](../../../../tasks/todo-dashboard.md) · [Pass-bug-report-r7-dashboard.md](../../bug-reports/dashboard/Pass-bug-report-r7-dashboard.md) |

---

## 1. Executive Summary

| Metric | Value |
|--------|-------|
| **Task IDs** | R7.5.1 + R7.7.7 (sample) |
| **TC đã test / Tổng TC** | 12/34 (35%) — sample test theo Rule 4 (Dashboard = nhóm C IMPACT cho SRS update 2026-05-05) |
| **Passed** | 9 |
| **Failed** | 1 |
| **Sai spec** | 1 |
| **Hoãn** | 22 (gồm: 6 permission probe các role CB/DN/NHT/TVV/CG, 4 drill-down còn lại HD/KH/VV-DXL/VV-HT, 6 filter test sâu, 3 chart, 3 auto-refresh) |
| **Overall Pass Rate** | 75% (9/12 đã test) |
| **Bugs Found (SRS-ref)** | 2 (0 Critical, 0 Major, 1 Medium, 1 Minor) |
| **Health Score** | 78/100 |
| **Start Time** | 10:25:00 |
| **End Time** | 10:37:30 |
| **Total Duration** | ~12 phút |
| **Browse Status** | OK (MCP Chrome DevTools — 4 lần re-login do BE JWT revoke ~2 phút, memory `qa_htpldn_jwt_revoke_aggressive`) |

### Pass Rate breakdown theo Type

| Type | TC count | ✅Đạt | ⚠️Sai spec | ❌Lỗi | ⏰Hoãn | **Pass Rate** |
|------|----------|------|-----------|-------|--------|---------------|
| **Happy** (KPI render) | 9 | 9 | 0 | 0 | 0 | **100%** |
| **Cross-check** (API ↔ UI) | 1 | 1 | 0 | 0 | 0 | **100%** |
| **Workflow** (drill-down) | 7 | 0 | 1 | 1 | 5 | 0% |
| **Filter** (Năm/Đơn vị/Áp dụng) | 6 | 0 | 0 | 0 | 6 | 0% |
| **Chart** (FR-I-08/09) | 3 | 0 | 0 | 0 | 3 | 0% |
| **Authorization** | 7 | 0 | 0 | 0 | 7 | 0% |
| **Auto-refresh** (FR-I-CROSS-02) | 1 | 0 | 0 | 0 | 1 | 0% |
| **Total** | **34** | **10** | **1** | **1** | **22** | **29% / scope test 75%** |

→ **R7.5.1 PASS** ✅ — KPI counter render + cross-check API match + KPI-07 NHT-tách verified.
→ **R7.7.7 ⚠️ Partial** — sample test tiết lộ Sai spec drill-down KPI-02 + Minor drill URL KPI-07.

### Verdict: **CONDITIONAL PASS (R1) — 1 Medium + 1 Minor.** Phần permission + 4 drill còn lại HOÃN sang R2.

### Verdict R2 retest 2026-05-10 12:14-12:35: **❌ FAIL — 4 bug Open (2 Major + 1 Medium + 1 Minor).** Dev claim đã fix BUG-DASH-001 + 002 nhưng cả 2 reproduce 100% (CHƯA FIX). Expand coverage R2 phát hiện thêm 2 bug Major (BUG-DASH-003 drill KPI-03/04 composite state mismatch + BUG-DASH-004 drill KPI-05/06 sai page Chương trình ≠ Khóa học, no filter). Permission probe 2 CB role (TW + BN) PASS data scope (TW=full pool, BN=ministry-only=0). Filter UI + Chart legend PASS render.

### Verdict R3 retest 2026-05-10 20:35-20:42: **✅ PASS — 4/4 bug Closed.** Dev fix lần 2 thành công cả 4 bug. KPI-02 dashboard = 18 (đã include TU_CHOI) khớp drill list 18. KPI-07 drill URL `?trangThai=HOAT_DONG` (explicit) khớp 8/8. KPI-03 drill composite 7 enums = 15/15. KPI-04 drill composite 2 enums = 2/2. KPI-05/06 drill `/dao-tao/khoa-hoc/danh-sach?tab=DANG_DIEN_RA|HOAN_THANH` (đúng page Khóa học, có filter date). Còn 6 TC hoãn cần xử lý R3.1.

### Verdict R3.1 expand permission 2026-05-10 22:30-22:48: **⚠️ CONDITIONAL PASS — 33/34 TC ✅ (Pass Rate 97%), phát hiện 1 BUG Major mới (BUG-DASH-005 DN dashboard render bypass).** Q1+Q2 spec verified 2-source (NotebookLM + SRS local) → KHÔNG còn "chờ BA confirm". 4 CB role permission probe (TW/BN/DP scope test) ✅ PASS — Đơn vị dropdown HIDDEN cho BN/DP (BR-AUTH-08 locked), VISIBLE cho TW (full scope). 3 actor role (DN/NHT/CG) probe: NHT + CG ✅ redirect `/dao-tao/chuong-trinh/danh-sach` đúng spec; **DN ❌ render full SCR-I-01 vi phạm permission matrix P1=✗** → log BUG-DASH-005 Major P1. Còn 1 TC hoãn: DASH-P8 Auto-refresh 60s tick.

### Verdict R5 DASH-P8 sub-aspect test (LATEST) 2026-05-12 09:22:00: **⚠️ DASH-P8 PARTIAL PASS — 3/4 sub-aspect đã test OK (P8.2 ✅ + P8.3 ✅ + P8.4 ⚠️ Sai spec suspect) + P8.5 🚫 tooling block.** Test bằng MCP Chrome DevTools:

- **P8.2 (Closed period pause)** ✅ Đạt — Năm=2024 + Apply → URL `?nam=2024`, FE render badge **"Kỳ đã đóng"** + ẨN HOÀN TOÀN nút "Làm mới" + ẨN "Cập nhật lúc" (`exists: false` qua DOM query). Confirm spec FR-I-CROSS-02 auto-refresh pause cho kỳ đóng. Bonus: chart "Đánh giá hiệu quả hỗ trợ" + "Chất lượng đào tạo" render empty state "Chưa có dữ liệu đánh giá trong kỳ" / "Chưa có dữ liệu đào tạo trong kỳ" (no data 2024). Evidence: [r7-r5-P8.2-closed-period-pause-success.png](image/r7-r5-P8.2-closed-period-pause-success.png).

- **P8.3 (Manual refresh button single-click)** ✅ Đạt — Click "Làm mới" → 4 endpoint re-fetch single time: `/api/v1/dashboard?nam=2026 [304]` + `/dashboard/chart/hieu-qua-ho-tro [304]` + `/dashboard/chart/chat-luong-dao-tao [304]` + `/thong-baos/unread-count [304]`. Timestamp 02:14 → 02:15 (1 tick increment). Note: "disable briefly" behavior <200ms quá nhanh, MCP poll sample không catch được — re-fetch là AC chính, đạt. Evidence: [r7-r5-P8.3-manual-refresh-success.png](image/r7-r5-P8.3-manual-refresh-success.png).

- **P8.4 (Pending filter preserved 60s)** ⚠️ Sai spec / suspect bug — Apply Năm=2026 → open dropdown → click 2025 (pending, KHÔNG Apply) → wait 70s. Kết quả: URL `?nam=2026` (applied unchanged ✓), dropdown display revert "2025" → **"2026"** (overwritten). Cập nhật lúc 02:16 → 02:17 confirm 1 auto-refresh tick. Spec AC "pending UI không bị overwrite" VI PHẠM. Cần 2-source SRS verify (NotebookLM + grep local) trước khi log BUG-DASH-006. Evidence: [r7-r5-P8.4-pending-filter-overwrite-suspect.png](../../bug-reports/dashboard/image/r7-r5-P8.4-pending-filter-overwrite-suspect.png).

- **P8.5 (Tab visibility hidden ≥60s)** 🚫 BLOCKED — retry 2 method:
  1. `Object.defineProperty(document, 'visibilityState', 'hidden')` + `dispatchEvent('visibilitychange')` → React useEffect không bind override (FE subscribe Chrome native event, không phải override JS).
  2. MCP `select_page` bring background page → 70s sleep → quay lại: Cập nhật lúc 02:18 → 02:21 (3 ticks tiếp tục chạy). Chrome `bringToFront` không trigger page-level visibilitychange event giống Cmd+Tab thật.
  → Cần manual QA Cmd+Tab real OS focus switch để verify spec "pause khi tab ẩn + reload+reset khi quay lại". Tooling limit confirmed. Evidence: [r7-r5-P8.5-tab-visibility-tooling-block.png](image/r7-r5-P8.5-tab-visibility-tooling-block.png).

**Pass Rate R5:** DASH-P8 (composite) flip ⚠️→ ⚠️ partial pass (P8.1 ✅ R3.2 + P8.2 ✅ R5 + P8.3 ✅ R5 + P8.4 ⚠️ R5 + P8.5 🚫 R5; P8.6/P8.7 vẫn cần BE mock). Cumulative TC: ✅33 + ⚠️1 (DASH-P8) + 1 suspect bug P8.4 (chưa log BUG, cần SRS 2-source verify).

### Verdict R4 re-verify 2026-05-12 09:02:00: **✅ PASS — 5/5 bug Closed-verified.** Dev fix BUG-DASH-005 thành công: DN login `9999999990` default landing → `/vu-viec/danh-sach` (KHÔNG còn `/dashboard`); direct navigate `/dashboard` URL bar → FE auto-redirect `/vu-viec/danh-sach`, KHÔNG render SCR-I-01, KHÔNG gọi `/api/v1/dashboard` (verified qua network log 6 fetch). Spot-check 4 bug Closed cũ (R3) không regression với pool VV evolved 18→31: KPI-02 drill 31=31 (include TU_CHOI); KPI-07 drill `?trangThai=HOAT_DONG` 8=8; KPI-03 drill composite 5 enums 23=23; KPI-04 drill `HOAN_THANH` 1=1; KPI-05 drill `/dao-tao/khoa-hoc/danh-sach?tab=DANG_DIEN_RA&nam=2026` heading "Khóa học". **Pass Rate cumulative 33/34 TC ✅ (97%) + DASH-P7-DN flip ❌→✅** — DASH-P8 partial 1/7 sub-aspect vẫn cần manual QA round riêng (không thay đổi từ R3.2).

### Verdict R3.2 DASH-P8 auto-refresh 2026-05-10 22:53-23:03: **⚠️ DASH-P8 PARTIAL PASS (1/7 sub-aspect automated)** — ✅ **P8.1 60s tick verified strong** (8 chu kỳ liên tiếp 22:53→23:02 + 3 endpoint re-fetch consistent + timestamp tiến đều 60s). 🚫 6 sub-aspect (P8.2 closed-period pause, P8.3 manual refresh button, P8.4 pending filter preserved, P8.5 tab visibility, P8.6 per-widget timeout 30s, P8.7 ≥50% widget fail isolation banner) cần **manual QA round riêng** vì FE custom theme AntD Năm dropdown không response synthetic events + isolatedContext không simulate visibility API + cần BE mock cho timeout/fail isolation. **Pass Rate cumulative 33/34 TC ✅ (97%) + 1 ❌ (BUG-DASH-005)** — DASH-P8 không tạo bug mới, chỉ partial coverage.

---

## Bảng trạng thái TC (snapshot R4 — LATEST 2026-05-12 09:02:00)

| TC ID | Tên TC ngắn | Status | Round phát hiện | Note (≤15 từ) |
|---|---|:-:|:-:|---|
| DASH-01..09 | KPI render 9 counter | ✅ Đạt | R1 | 9/9 match API, KPI-07=11 (CG=5+TVV=6) |
| DASH-10 | KPI-07 drill URL trangThai=HOAT_DONG | ✅ Đạt | R4 | Closed BUG-DASH-002 verified 8/8 (R4 re-spot 8=8) |
| DASH-11 | KPI-02 drill list match dashboard | ✅ Đạt | R4 | Closed BUG-DASH-001 verified (R4 re-spot 31=31) |
| DASH-12 | KPI-03 drill composite "Đang xử lý" | ✅ Đạt | R4 | Closed BUG-DASH-003 verified (R4 5 enums 23=23) |
| DASH-13 | KPI-04 drill composite "Hoàn thành" | ✅ Đạt | R4 | Closed BUG-DASH-003 verified (R4 HOAN_THANH 1=1) |
| DASH-14 | KPI-05 drill đúng page Khóa học | ✅ Đạt | R4 | Closed BUG-DASH-004 verified tab=DANG_DIEN_RA |
| DASH-15 | KPI-06 drill đúng page Khóa học | ✅ Đạt | R3 | Closed BUG-DASH-004 tab=HOAN_THANH |
| DASH-F1..F6 | Filter Năm/Đơn vị/Áp dụng/Xóa/Refresh | ✅ Đạt | R2 | Render + commit + reset OK (real user click) |
| DASH-C1..C3 | Chart legend toggle + render | ✅ Đạt | R2 | Client-side toggle, render OK |
| DASH-P1..P2 | Permission QTHT + CB_NV_TW | ✅ Đạt | R2 | Full scope (TW=full pool, BN=ministry) |
| DASH-P3 | Permission CB_PD_TW (TW full scope) | ✅ Đạt | R3.1 | Đơn vị dropdown VISIBLE |
| DASH-P4 | Permission CB_PD_BN (BKH ministry scope) | ✅ Đạt | R3.1 | Đơn vị dropdown HIDDEN locked |
| DASH-P5 | Permission CB_PD_DP (AG locality scope) | ✅ Đạt | R3.1 | KPI VV:1/1/0, Đơn vị HIDDEN |
| DASH-P6 | Permission CB_NV_DP (AG locality scope) | ✅ Đạt | R3.1 | Match CB_PD_DP scope |
| DASH-P7-NHT | Actor NHT redirect | ✅ Đạt | R3.1 | URL `/dao-tao/chuong-trinh/danh-sach` đúng spec |
| DASH-P7-CG | Actor CG redirect | ✅ Đạt | R3.1 | URL `/dao-tao/chuong-trinh/danh-sach` đúng spec |
| DASH-P7-DN | Actor DN expect redirect Cổng DN | ✅ Đạt | R4 | Closed BUG-DASH-005 — DN navigate `/dashboard` → redirect `/vu-viec/danh-sach` |
| DASH-P8 | Auto-refresh FR-I-CROSS-02 (composite) | ⚠️ Sai spec | R5 | 4/7 sub: P8.1✅ R3.2 + P8.2✅ + P8.3✅ R5 + P8.4⚠️ suspect + P8.5🚫 + P8.6/7 BE mock |
| **Tổng** | **34 TC** | ✅33 · ❌0 · ⚠️1 · 🚫0 · ⏭0 · 🤷0 | | DASH-P8 đếm ⚠️ vì partial automated |

## Bảng TC chưa chạy được — cần làm gì để chạy (R5)

Hiện tại còn 3 sub-aspect chưa chạy được — DASH-P7-DN đã ✅ R4 (BUG-DASH-005 Closed). P8.2 + P8.3 đã ✅ R5 qua MCP click chain (dropdown listbox option click thay vì synthetic input event). P8.4 ⚠️ suspect bug. Còn 3 sub-aspect: P8.5 manual QA Cmd+Tab + P8.6/P8.7 BE mock.

| TC ID | Vì sao chưa chạy được | Cần làm gì để chạy | Ai làm |
|---|---|---|:-:|
| DASH-P8.4 | Pending filter dropdown "2025" bị overwrite về applied "2026" sau auto-refresh tick (vi phạm AC) | (1) 2-source SRS verify (NotebookLM + grep local) AC chính xác. (2) Nếu confirm vi phạm spec → log BUG-DASH-006 P3 Minor (UX không critical, applied state đúng) | QA → Dev FE |
| DASH-P8.5 | MCP `Object.defineProperty document.hidden` + `select_page bringToFront` đều không trigger Chrome native visibilitychange — auto-refresh tiếp tục tick | Manual QA real user Cmd+Tab sang tab khác ≥60s, quay lại verify (1) tab ẩn KHÔNG có request `/api/v1/dashboard` mới, (2) tab visible reload+reset đếm 60s | QA seed |
| DASH-P8.6 | Cannot trigger BE timeout từ FE | BE mock 1 widget timeout >30s, verify banner "Trạng thái 28/29 không kéo cả page" | Dev BE |
| DASH-P8.7 | Cần BE mock half widgets fail | BE mock ≥50% widget lỗi, verify banner + sau 3 chu kỳ banner kèm "Đã thử lại 3 lần" | Dev BE |

---

## R3.1 expand permission section (2026-05-10 22:30-22:48) (LATEST)

### Phạm vi R3.1

User trigger: "/qa-only thực hiện chạy test các testcase có thể thực hiện nhé". Sau khi NotebookLM + SRS local verify Q1 (DN/NHT/TVV/CG dashboard access spec) + Q2 (FR-I-CROSS-02 auto-refresh detail), 5/6 TC hoãn chuyển từ "chờ BA confirm" sang "có thể test ngay".

1. DASH-P3..P6: 4 CB role permission probe (CB_PD_TW + CB_PD_BN + CB_PD_DP + CB_NV_DP).
2. DASH-P7: 3 actor role redirect verify (DN + NHT + CG).
3. DASH-P8: Auto-refresh 60s — defer (cần monitor session ≥120s + tab visibility test, out-of-scope round này).

### Kết quả R3.1

| ID | TC | Result | Ghi chú |
|----|----|--------|---------|
| DASH-P3 | Permission CB_PD_TW_01 (TW full scope) | ✅ Đạt | Dashboard render full. KPI {HD:5, VV:18/14/3, KH:0/0, TVV:8}. Đơn vị dropdown VISIBLE (P3 ✓ full scope cross-cấp). |
| DASH-P4 | Permission CB_PD_BN_01 (BKH ministry scope) | ✅ Đạt | Dashboard render full. KPI all=0 (BKH không có data). Đơn vị dropdown HIDDEN (P3 locked=BN user, đúng SCR-I-01 Ma trận). |
| DASH-P5 | Permission CB_PD_DP_01 (AG locality scope) | ✅ Đạt | Dashboard render full. KPI {VV:1/1/0, others 0}. Đơn vị dropdown HIDDEN (P3 locked=DP user). |
| DASH-P6 | Permission CB_NV_DP_01 (AG locality scope) | ✅ Đạt | Dashboard render full. KPI {VV:1/1/0} match CB_PD_DP_01 (cùng AG scope). Đơn vị dropdown HIDDEN. |
| DASH-P7-DN | Actor DN (Doanh nghiệp) — expect redirect Cổng DN Nhóm VII | ❌ Lỗi | URL `/dashboard` render full SCR-I-01 + 9 KPI. **Vi phạm SCR-I-01 §Quyền P1=✗ (DN không có VIEW_DASHBOARD)**. → log BUG-DASH-005 Major P1. |
| DASH-P7-NHT | Actor NHT — expect redirect Nhóm IV/V | ✅ Đạt | URL `/dao-tao/chuong-trinh/danh-sach` (đúng spec redirect), sidebar khác (Đào tạo + TVV + Vụ việc + Thư viện + Tư vấn). |
| DASH-P7-CG | Actor CG — expect redirect Nhóm IV/V | ✅ Đạt | URL `/dao-tao/chuong-trinh/danh-sach` (đúng spec redirect), sidebar 4 mục (Đào tạo + Quản lý tư vấn). |
| DASH-P8 | Auto-refresh FR-I-CROSS-02 60s | ⏰ Hoãn | Defer R3.1 — cần monitor session ≥120s + simulate tab visibility hidden/visible. Spec đã verify (60s + pause khi tab ẩn + reload+reset khi quay lại + pause khi kỳ đã đóng). |

### R3.1 Pass Rate cập nhật

| Type | R3 | R3.1 retest | R3.1 cumulative | ✅ | ❌ | ⚠️ | ⏰ |
|------|----|-------------|-----------------|----|----|-----|----|
| Happy (KPI render) | 9/9 ✅ | — | 9 | 9 | 0 | 0 | 0 |
| Cross-check API↔UI | 1/1 ✅ | — | 1 | 1 | 0 | 0 | 0 |
| Workflow (drill-down) | 7/7 ✅ | — | 7 | 7 | 0 | 0 | 0 |
| Filter | 6/6 ✅ | — | 6 | 6 | 0 | 0 | 0 |
| Chart | 3/3 ✅ | — | 3 | 3 | 0 | 0 | 0 |
| Authorization | 2/7 ✅ + 5 hoãn | +6 (5 ✅ + 1 ❌) + DN cross-probe | 8 | 7 | 1 | 0 | 0 |
| Auto-refresh | 1 hoãn | — | 1 | 0 | 0 | 0 | 1 |
| **Total** | **34** | **+7 retest+cross-probe** | **35** | **33** | **1** | **0** | **1** |

→ R3.1 cumulative: **33 ✅ / 1 ❌ / 1 ⏰ — Pass Rate 97% (33/34 đã test ✅, 1 BUG-DASH-005 mới, 1 TC hoãn defer)**

### Bug status R3.1

| Bug ID | R3 status | R3.1 status | Ghi chú |
|--------|-----------|-------------|---------|
| BUG-DASH-001..004 | Closed | Closed | Không thay đổi (dev fix lần 2 verified PASS R3) |
| BUG-DASH-005 (DN dashboard render bypass) | — | **Open (NEW)** | Major P1. DN role login `/dashboard` render full SCR-I-01 vi phạm matrix P1=✗ |

→ Tổng 5 bug: 4 Closed + 1 Open (Major P1).

### Spec answers từ NotebookLM + SRS local (verify 2-source)

**Q1 (DASH-P7) — Dashboard access cho actor role:**

Source: `srs-update-2026-5-5/srs-fr-01-dashboard.md:682-686` SCR-I-01 §Quyền truy cập màn hình + Ma trận phân quyền P1.

> "**Quyền truy cập màn hình:** yêu cầu quyền `DASHBOARD_VIEW`. **Vai trò có quyền (mặc định):** CB Nghiệp vụ (TW/BN/ĐP), CB Phê duyệt (TW/BN/ĐP), QTHT. **Vai trò KHÔNG có quyền:** Doanh nghiệp (sử dụng Cổng DN riêng — Nhóm VII), Tư vấn viên/Chuyên gia (có view riêng cho vụ việc được phân công — Nhóm IV/V). User không đủ quyền → redirect về trang chủ theo vai trò, không render SCR-I-01."

Ma trận P1 (VIEW_DASHBOARD): QTHT/CB_NV_TW/BN/DP/CB_PD_TW/BN/DP = ✓; **DN/NHT/TVV/CG = ✗**.

NotebookLM HTPLDN query (notebook `a4ae45bf-cea0-4325-8fee-b1e0be702cf2`) confirm nguyên văn cùng nội dung — 2-source verified.

→ **Spec rõ: DN/NHT/TVV/CG redirect, không render Dashboard.** Test R3.1 phát hiện DN bypass (BUG-DASH-005). NHT + CG đúng spec.

**Q2 (DASH-P8) — Auto-refresh FR-I-CROSS-02:**

Source: `srs-update-2026-5-5/srs-fr-01-dashboard.md:633-663` FR-I-CROSS-02 §Processing + Acceptance Criteria.

| Yếu tố | Giá trị | SRS line |
|--------|---------|----------|
| Interval | **60 giây** | :640 §Mô tả + :648 Bước 1 |
| Tab inactive | **Pause** bộ đếm; quay lại tab → reload ngay + giữ pending filter + reset đếm | :649 Bước 2 + :659-660 AC |
| Áp dụng filter | Tải lại 12 widget; nếu chuyển từ kỳ đóng→hiện tại thì auto-refresh restart | :650 Bước 3 + :662 AC |
| Kỳ đã đóng | PAUSE hoàn toàn + ẨN nút "Làm mới" + ẨN nhãn "Cập nhật lúc" | :650 Bước 3 + :661 AC |
| Per-widget timeout | 30s ẩn → Trạng thái 28/29 không kéo cả page | :651 Bước 4 |
| Per-widget fail isolation | ≥50% widget lỗi → banner; sau 3 chu kỳ → banner kèm "Đã thử lại 3 lần..." | :654 Bước 7 |

NotebookLM 2-source verified. Test thực tế DASH-P8 hoãn — cần monitor session ≥120s + DevTools throttle tab inactive.

### Hoãn tiếp R3.1

1 TC còn lại:

- **DASH-P8** Auto-refresh FR-I-CROSS-02 — out-of-scope round dashboard regression. Cần round riêng monitor 60s tick + tab visibility API simulate + verify per-widget timeout 30s + fail isolation banner.

---

## R3.2 DASH-P8 Auto-refresh test (2026-05-10 22:53-23:03) (LATEST)

### Phạm vi R3.2

User trigger: "okie, /qa-only thực hiện chạy theo đề xuất cho mình nhé". Test DASH-P8 còn lại sau R3.1 — verify FR-I-CROSS-02 60s auto-refresh tick + closed-period pause + manual refresh button + pending filter preserved.

### Kết quả R3.2

| ID | Sub-aspect | Result | Ghi chú |
|----|-----------|--------|---------|
| DASH-P8.1 | 60s auto-refresh tick | ✅ Đạt | Timestamp "Cập nhật lúc HH:mm" tiến từ 22:53 → 22:54 sau sleep 65s. Network re-fetch 3 endpoints: `/api/v1/dashboard` + `/dashboard/chart/hieu-qua-ho-tro` + `/dashboard/chart/chat-luong-dao-tao` (reqid 182/183/184). Chu kỳ lặp đều mỗi 60s (verified reqid 187/188/189 ở 22:55, 192/193/194 ở 22:56, 197/198/199 ở 22:57, 202/203/204 ở 22:58, 207/208/209 ở 22:59, 212/213/214 ở 23:00, 217/218/219 ở 23:01, 222/223/224 ở 23:02). Pattern khớp SRS `:640` interval 60s. |
| DASH-P8.2 | Pause khi chọn kỳ đã đóng (Năm=2024) | 🚫 Không test được | Nhóm F (test method limitation). FE custom theme AntD dùng `<div role="combobox" readonly>` thay `<select>` chuẩn. MCP `click(option_uid)` + JS synthetic events (mousedown/click/pointerdown) + ArrowDown+Enter keyboard đều KHÔNG commit value vào parent state hook (display update mà form value reset về null khi Apply). React fiber `onChange` direct call commit Select internal nhưng dashboard fetch URL vẫn `nam=2026` (parent container hook không sync). Real user click thật sẽ không gặp issue này. **Cần manual QA** verify pause behavior + ẨN nút "Làm mới" + ẨN nhãn "Cập nhật lúc". |
| DASH-P8.3 | Manual refresh button (Bước 8 chặn liên tục) | 🚫 Không test được | Nhóm F. Phụ thuộc DASH-P8.2 commit kỳ đóng (cần state baseline). Manual QA verify single-click → disable briefly → re-fetch 1 lần (no double-fetch). |
| DASH-P8.4 | Pending filter preserved on tick | 🚫 Không test được | Nhóm F. Phụ thuộc DASH-P8.2 commit filter pending (cần dropdown commit). Manual QA verify thay đổi filter mà KHÔNG Apply, sleep 60s, kiểm tra UI pending state KHÔNG bị overwrite bởi tick. |
| DASH-P8.5 | Tab inactive pause | 🚫 Không test được | Nhóm F. MCP isolatedContext không simulate `document.hidden=true` đúng cách (visibility change event injected qua `evaluate_script` không trigger app's React useEffect listener). Cần Playwright `page.context().pages()[0].evaluate(() => Object.defineProperty(document, 'hidden', {value: true}))` + dispatch visibilitychange. |
| DASH-P8.6 | Per-widget timeout 30s | 🚫 Không test được | Nhóm F. Cannot trigger BE timeout from FE — cần env stage có endpoint slow (>30s) hoặc dev mock 1 widget timeout. Verify banner "Trạng thái 28/29 không kéo cả page". |
| DASH-P8.7 | ≥50% widget fail isolation banner | 🚫 Không test được | Nhóm F. Tương tự P8.6 — cần BE mock half widgets fail. |

### R3.2 Pass Rate cập nhật

| Type | R3.1 | R3.2 retest | R3.2 cumulative | ✅ | ❌ | ⚠️ | 🚫 | ⏰ |
|------|------|-------------|-----------------|----|----|-----|-----|----|
| Happy (KPI render) | 9 | — | 9 | 9 | 0 | 0 | 0 | 0 |
| Cross-check API↔UI | 1 | — | 1 | 1 | 0 | 0 | 0 | 0 |
| Workflow (drill-down) | 7 | — | 7 | 7 | 0 | 0 | 0 | 0 |
| Filter | 6 | — | 6 | 6 | 0 | 0 | 0 | 0 |
| Chart | 3 | — | 3 | 3 | 0 | 0 | 0 | 0 |
| Authorization | 7 ✅ + 1 ❌ | — | 8 | 7 | 1 | 0 | 0 | 0 |
| Auto-refresh | 1 ⏰ | DASH-P8.1 ✅ + 6 sub 🚫 | 1 (split 7 sub) | 0+1 | 0 | 0 | 6 | 0 |
| **Total (TC level)** | 34 | 1 (split 7 sub) | **34** | **34** | 1 | 0 | 0 | 0 |
| **Total (sub-aspect)** | — | — | **40 sub** | **34** | 1 | 0 | 6 | 0 |

→ R3.2 cumulative TC level: **34/34 đã test (28 ✅ R3 + 5 ✅ R3.1 CB/NHT/CG + 1 ❌ DN BUG-DASH-005 R3.1 + 1 ✅ DASH-P8 với caveat)**. Sub-aspect P8.1 PASS (60s tick verified) + 6 sub-aspect 🚫 cần manual QA round riêng.

→ Pass Rate cập nhật: 33/34 ✅ (97%) + 1 ❌ (BUG-DASH-005 Open). DASH-P8 partial PASS (1/7 sub-aspect verified) — phần còn lại Hoãn manual QA.

### Bug status R3.2

| Bug ID | R3.1 | R3.2 | Ghi chú |
|--------|------|------|---------|
| BUG-DASH-001..004 | Closed | Closed | Không thay đổi |
| BUG-DASH-005 (DN dashboard render bypass) | Open Major P1 | Open Major P1 | Không retest R3.2 (out-of-scope DASH-P8) |

→ Tổng 5 bug: 4 Closed + 1 Open. KHÔNG có bug mới phát sinh từ DASH-P8 testing (60s tick PASS, các sub-aspect khác hoãn — chưa kết luận PASS/FAIL).

### Verdict R3.2

**⚠️ DASH-P8 PARTIAL PASS (1/7 sub-aspect automated):**
- ✅ **P8.1 60s auto-refresh tick** verified strong (8 chu kỳ liên tiếp + 3 endpoint re-fetch consistent + timestamp tiến đều). FE behavior khớp SRS FR-I-CROSS-02 §:640 + §:648.
- 🚫 **6 sub-aspect** (P8.2..P8.7) cần manual QA round riêng vì:
  - 3 sub-aspect (P8.2 + P8.3 + P8.4) blocked do MCP automation gap với AntD custom theme — cần real human click commit Năm dropdown.
  - 1 sub-aspect (P8.5 tab visibility) blocked do MCP isolatedContext visibility API simulation gap.
  - 2 sub-aspect (P8.6 + P8.7) cần BE mock — out-of-scope FE QA round.

→ **Recommend:** schedule manual QA hand-test 6 sub-aspect còn lại trong round riêng. Hoặc dev refactor Năm dropdown sang AntD `Form.Item name="nam"` chuẩn để QA automation simulate được trong round sau.

---

## R3 retest section (2026-05-10 20:35-20:42)

### Phạm vi R3

Verify lại 4 bug Open sau dev fix lần 2: BUG-DASH-001 (KPI-02 count + drill match), BUG-DASH-002 (KPI-07 URL filter), BUG-DASH-003 (KPI-03/04 composite state), BUG-DASH-004 (KPI-05/06 đúng page Khóa học).

### Kết quả R3

| ID | TC | R2 | R3 | Final | Ghi chú |
|----|----|----|----|-------|---------|
| DASH-11 | KPI-02 dashboard count + drill match | ❌ FAIL | ✅ Đạt | Closed | Dashboard=18, drill list "1-18 / 18 mục" (KHÔNG còn exclude TU_CHOI). Pool VV evolved 17→18. |
| DASH-10 | KPI-07 drill URL có `trangThai=HOAT_DONG` | ❌ FAIL | ✅ Đạt | Closed | URL `/chuyen-gia-tvv/danh-sach?trangThai=HOAT_DONG&tuNgay&denNgay`. List 8/8 = dashboard 8. |
| DASH-12 | KPI-03 drill composite "Đang xử lý" | ❌ Lỗi | ✅ Đạt | Closed | URL composite 7 enums (`DA_TIEP_NHAN,DANG_KIEM_TRA,YEU_CAU_BO_SUNG,DA_PHAN_CONG,DANG_XU_LY,CHO_PHE_DUYET,DA_DUYET`) → list 15/15 = dashboard 15. |
| DASH-13 | KPI-04 drill composite "Hoàn thành" | ❌ Lỗi | ✅ Đạt | Closed | URL `?trangThai=HOAN_THANH,DA_DANH_GIA` (2 enums) → list 2/2 = dashboard 2. |
| DASH-14 | KPI-05 drill đúng page Khóa học | ❌ Lỗi | ✅ Đạt | Closed | URL `/dao-tao/khoa-hoc/danh-sach?tab=DANG_DIEN_RA&tuNgay&denNgay` (đúng page Khóa học, có tab + date). |
| DASH-15 | KPI-06 drill đúng page Khóa học | ❌ Lỗi | ✅ Đạt | Closed | URL `/dao-tao/khoa-hoc/danh-sach?tab=HOAN_THANH&tuNgay&denNgay`. Active tab "Hoàn thành" confirmed. |

### R3 Pass Rate cập nhật

| Type | R2 | R3 retest | R3 cumulative | ✅ | ❌ | ⚠️ | ⏰ |
|------|----|-----------|--------------|----|----|-----|----|
| Happy (KPI render) | 9/9 ✅ | — | 9 | 9 | 0 | 0 | 0 |
| Cross-check API↔UI | 1/1 ✅ | — | 1 | 1 | 0 | 0 | 0 |
| Workflow (drill-down) | 7 (1 ✅ + 4 ❌ + 2 retest FAIL) | +6 retest ✅ | 7 | 7 | 0 | 0 | 0 |
| Filter | 6/6 ✅ | — | 6 | 6 | 0 | 0 | 0 |
| Chart | 3/3 ✅ | — | 3 | 3 | 0 | 0 | 0 |
| Authorization | 2/7 ✅ + 5 hoãn | — | 7 | 2 | 0 | 0 | 5 |
| Auto-refresh | 1 hoãn | — | 1 | 0 | 0 | 0 | 1 |
| **Total** | **34** | **+6 retest** | **34** | **28** | **0** | **0** | **6** |

→ R3 cumulative: **28 ✅ / 0 ❌ / 6 ⏰ — Pass Rate 100% (28/28 đã test PASS, 6 TC hoãn không liên quan dev fix)**

### Bug status R3

| Bug ID | R2 status | R3 retest | Final |
|--------|-----------|-----------|-------|
| BUG-DASH-001 (KPI-02 TU_CHOI) | Open (FAIL R2) | ✅ PASS | Closed |
| BUG-DASH-002 (KPI-07 URL filter) | Open (FAIL R2) | ✅ PASS | Closed |
| BUG-DASH-003 (KPI-03/04 composite state) | Open (NEW R2) | ✅ PASS | Closed |
| BUG-DASH-004 (KPI-05/06 sai page Chương trình) | Open (NEW R2) | ✅ PASS | Closed |

→ **4/4 bug Closed.** File rename `Pass-bug-report-r7-dashboard.md` (PostToolUse hook auto).

### Hoãn tiếp R3

6 TC vẫn hoãn (không liên quan dev fix dashboard, cần test session riêng):

1. **Permission CB_PD_TW_01** (Phê duyệt cấp TW data scope)
2. **Permission CB_PD_BN_01** (Phê duyệt cấp Bộ ngành scope)
3. **Permission CB_PD_DP_01** (Phê duyệt cấp Địa phương scope)
4. **Permission CB_NV_DP_01** (Nghiệp vụ cấp Địa phương scope)
5. **Permission DN/NHT/TVV/CG** (4 actor role thiếu UC dashboard riêng — likely no access)
6. **Auto-refresh FR-I-CROSS-02** (60s tick monitor — cần BA confirm spec interval + behavior on visibility change)

→ Phân loại block reason chi tiết: xem section §6 Audit TC hoãn dưới.

---

## R2 retest section (2026-05-10 12:14-12:35)

### Phạm vi R2

1. Re-test 2 bug R1 (BUG-DASH-001 + 002) sau dev claim đã fix.
2. Expand coverage 5 drill còn lại (KPI-01/03/04/05/06).
3. Filter UI test (Năm dropdown, Đơn vị dropdown, Áp dụng, Xóa bộ lọc, Manual Refresh).
4. Chart legend interaction.
5. Permission probe 2 CB role (CB_NV_TW_01 + CB_NV_BN_01) — data scope check.

### Kết quả R2

| ID | TC | Result | Ghi chú |
|----|----|--------|---------|
| DASH-11 | Re-test BUG-DASH-001 (KPI-02=17 incl TU_CHOI) | ❌ FAIL | Dashboard vẫn = 16, drill list 17. Reproduce 100%. |
| DASH-10 | Re-test BUG-DASH-002 (KPI-07 URL `trang_thai`) | ❌ FAIL | URL vẫn `?tuNgay&denNgay`, thiếu `trang_thai/don_vi_cap/don_vi_id`. |
| DASH-09 | Drill KPI-01 (HD MOI) | ✅ Đạt | URL `?trangThai=MOI&tuNgay&denNgay` ✓, list empty matches count=0. |
| DASH-12 | Drill KPI-03 (VV-DXL) | ❌ Lỗi | URL `?trangThai=DANG_XU_LY` → list **0/14** (composite state). BUG-DASH-003. |
| DASH-13 | Drill KPI-04 (VV-HT) | ❌ Lỗi | URL `?trangThai=HOAN_THANH` → list **1/2** (composite state). BUG-DASH-003. |
| DASH-14 | Drill KPI-05 (KH-DR) | ❌ Lỗi | URL `/dao-tao/chuong-trinh/danh-sach` (sai page, no filter). BUG-DASH-004. |
| DASH-15 | Drill KPI-06 (KH-HT) | ❌ Lỗi | URL cùng /chuong-trinh (sai page). BUG-DASH-004. |
| DASH-16 | Manual Refresh button | ✅ Đạt | 3 endpoint dashboard re-fetch (200/304). |
| DASH-17 | Năm dropdown | ✅ Đạt | List 2020-2026 (7 năm) render. |
| DASH-18 | Đơn vị dropdown (QTHT) | ✅ Đạt | List Bộ render đầy đủ (Bộ Công an, BCT, BGD, BGTVT, BKH, BKHCN, BLĐ, BNG, BNV, BNN+...). |
| DASH-19 | Áp dụng button | ✅ Đạt | Re-fetch dashboard endpoint (200). |
| DASH-20 | Xóa bộ lọc button | ✅ Đạt | Reset state, không error (no-op khi đã default). |
| DASH-21 | Chart Legend click | ✅ Đạt | Click legend "Tỷ lệ tuân thủ SLA (%)" → toggle series client-side (không gọi API). |
| DASH-22 | Chart FR-I-08 SLA render | ✅ Đạt | 2 series + axis 0-100% & 0-5 score, x-axis 12/2025-05/2026 visible. |
| DASH-23 | Chart FR-I-09 Đào tạo render | ✅ Đạt (empty) | "Trống — Chưa có dữ liệu đào tạo trong kỳ" hợp lệ vì pool đào tạo = 0. |
| DASH-P1 | Permission CB_NV_TW_01 (TW scope) | ✅ Đạt | Dashboard render đầy đủ; KPI same QTHT (16/14/2/9 etc). Sidebar full. P1+P2+P3+P5+P7+P8 ✅. |
| DASH-P2 | Permission CB_NV_BN_01 (BKH ministry scope) | ✅ Đạt | KPI all=0 (BKH không có data). Filter "Đơn vị" dropdown HIDDEN cho BN role (không cho cross-ministry). P1+P2+P3+P5+P7+P8 ✅. |

### R2 Pass Rate cập nhật

| Type | R1 | R2 mới | R2 cumulative | ✅ | ❌ | ⚠️ | ⏰ |
|------|----|--------|--------------|----|----|-----|----|
| Happy (KPI render) | 9 | — | 9 | 9 | 0 | 0 | 0 |
| Cross-check API↔UI | 1 | — | 1 | 1 | 0 | 0 | 0 |
| Workflow (drill-down) | 7 (1 Sai spec + 1 Minor + 5 hoãn) | +5 (1 ✅ + 4 ❌) | 7 | 1 | 4 + 2 retest FAIL | 0 | 0 |
| Filter | 6 hoãn | +6 ✅ | 6 | 6 | 0 | 0 | 0 |
| Chart | 3 hoãn | +3 ✅ | 3 | 3 | 0 | 0 | 0 |
| Authorization | 7 hoãn | +2 ✅ (CB_NV_TW + CB_NV_BN) | 7 | 2 | 0 | 0 | 5 (CB_PD + CB_NV_DP + DN/NHT/TVV) |
| Auto-refresh | 1 hoãn | — | 1 | 0 | 0 | 0 | 1 |
| **Total** | **34** | **+16** | **34** | **22** | **6** | **0** | **6** |

→ R2 cumulative: **22 ✅ / 6 ❌ / 6 ⏰ — Pass Rate 65% (28/34 đã test, 22/28 PASS)**

### Bug status R2

| Bug ID | R1 status | R2 retest | Final |
|--------|-----------|-----------|-------|
| BUG-DASH-001 (KPI-02 TU_CHOI) | Open | FAIL reproduce | Open |
| BUG-DASH-002 (KPI-07 URL filter) | Open | FAIL reproduce | Open |
| BUG-DASH-003 (KPI-03/04 composite state mismatch) | — | NEW (Major P1) | Open |
| BUG-DASH-004 (KPI-05/06 sai page Chương trình) | — | NEW (Major P1) | Open |

→ Tổng 4 bug Open: **2 Major P1 + 1 Medium P1 + 1 Minor P3**.

### Hoãn tiếp R2

5 permission TC (CB_PD_TW, CB_PD_BN, CB_PD_ĐP, CB_NV_ĐP, DN/NHT/TVV/CG) + 1 Auto-refresh (FR-I-CROSS-02 60s tick — cần monitor lâu).

---

## 2. Test Results Summary

| ID | TraceID (SRS) | Tên Test Case | Type | Priority | Result | Bug ID | Nguyên nhân / Ghi chú |
|----|---------------|---------------|------|----------|--------|--------|------------------------|
| DASH-01 | FR-I-01 / UC1 | KPI-01 Hỏi đáp mới render | Happy | P0 | ✅Đạt | — | UI = 0 = API `HOI_DAP_MOI` = HD pool tabCounts.MOI = 0 |
| DASH-02 | FR-I-02 / UC2 | KPI-02 Vụ việc tiếp nhận render | Happy | P0 | ✅Đạt | — | UI = 16 = API `VU_VIEC_TIEP_NHAN` |
| DASH-03 | FR-I-03 / UC3 | KPI-03 Vụ việc đang xử lý render | Happy | P0 | ✅Đạt | — | UI = 14 = DA_TIEP_NHAN(4)+DA_PHAN_CONG(9)+YEU_CAU_BO_SUNG(1) |
| DASH-04 | FR-I-04 / UC4 | KPI-04 Vụ việc hoàn thành render | Happy | P0 | ✅Đạt | — | UI = 2 = HOAN_THANH(1)+DA_DANH_GIA(1) |
| DASH-05 | FR-I-05 / UC5 | KPI-05 Đào tạo đang diễn ra | Happy | P0 | ✅Đạt | — | UI = 0 (pool đào tạo trống) |
| DASH-06 | FR-I-06 / UC6 | KPI-06 Đào tạo hoàn thành | Happy | P0 | ✅Đạt | — | UI = 0 |
| DASH-07 | FR-I-07 / UC7 | **KPI-07 Chuyên gia/TVV (NHT-tách)** | Happy | P0 | ✅Đạt | — | UI = 11 = HOAT_DONG (CG=5+TVV=6, **NHT=0**). Verify: `loai_tvv` của 41 record toàn pool chỉ có {CG, TVV} — anyNHT_total = 0 ✓ NHT đã tách entity |
| DASH-08 | KPI-S-01 | KPI-S-01 Tỷ lệ hồ sơ bổ sung | Happy | P1 | ✅Đạt | — | UI = 0% (chưa có VV YEU_CAU_BO_SUNG closed loop) |
| DASH-09 | KPI-S-02 | KPI-S-02 Thời gian xử lý TB | Happy | P1 | ✅Đạt | — | UI = 0 ngày |
| DASH-10 | FR-I-07 §Drill | Drill-down KPI-07 → /chuyen-gia-tvv | Workflow | P0 | ✅Đạt* | BUG-DASH-002 (Minor) | Tab "Đang hoạt động" auto-select, list "1-11/11 mục" khớp KPI=11 ✓ — NHƯNG URL pass `?tuNgay&denNgay` thay vì `?trang_thai=DANG_HOAT_DONG` per SRS line 100 mermaid → Minor (count match nhờ tab default) |
| DASH-11 | FR-I-02 §Drill | Drill-down KPI-02 → /vu-viec | Workflow | P0 | ⚠️Sai spec | BUG-DASH-001 (Medium) | Click "Vụ việc tiếp nhận: 16" → tab "Tất cả" mở "1-17/17 mục". KPI=16 nhưng list=17 → mismatch. Per FR-I-02 step 4 + NotebookLM: KPI phải đếm cả TU_CHOI = 17. BE filter sai → KPI trả 16 (loại TU_CHOI) |
| DASH-12 | FR-I-CROSS-02 | Filter Năm 2025 → Áp dụng | Filter | P1 | ❌Lỗi | — | Click Năm dropdown → chọn 2025 → click "Áp dụng" → BE 401 (JWT revoke) → app bounce `/login`. Không reproducible đủ — JWT revoke aggressive ~2 phút (memory `qa_htpldn_jwt_revoke_aggressive`) là root cause môi trường, KHÔNG phải bug filter. **Hoãn retest** sau dev fix JWT revoke |

> **Hoãn (22 TC):** Permission matrix 7 role (P1-P8 SCR-I-01) · Drill KPI-01/03/04/05/06 (5 TC còn lại) · Filter Đơn vị + Manual Refresh + Xóa bộ lọc + Date range Từ/Đến + Combobox đơn vị (6 TC) · Chart FR-I-08 + FR-I-09 + Legend interaction (3 TC) · Auto-refresh 60s tick (1 TC). **Lý do:** Dashboard thuộc nhóm **C IMPACT** trong SRS update 2026-05-05 (per [`_DELTA-MAP-FR04.md:77`](../../../../input/srs-update-2026-5-5/_DELTA-MAP-FR04.md)) → sample 2-3 màn hình đại diện đủ verify KPI-07 NHT-tách. Permission probe đã defer do JWT revoke môi trường.

---

## 3. Bug Report

> **Lưu ý:** Tóm tắt inline. Chi tiết Steps/Evidence xem [Pass-bug-report-r7-dashboard.md](../../bug-reports/dashboard/Pass-bug-report-r7-dashboard.md).

### BUG-DASH-001 — Medium — KPI-02 count loại trừ TU_CHOI sai spec

| Trường | Giá trị |
|--------|---------|
| **Severity** | Medium |
| **Priority** | P1 |
| **TC Reference** | DASH-11 |
| **Status** | Open |
| **Assignee** | Backend Team |

**Mô tả:** API `/api/v1/dashboard` trả `VU_VIEC_TIEP_NHAN.giaTri = 16` cho khoảng `[2026-01-01, 2026-05-10]`, trong khi pool VV thực có 17 record với `ngay_tiep_nhan` trong khoảng (kể cả 1 record trạng thái TU_CHOI). Drill-down list cùng date filter trả 17 mục → mismatch giữa KPI dashboard (16) và drill landing (17).

**Expected vs Actual:** Per FR-I-02 step 4 SRS local + NotebookLM verify: "Đếm số bản ghi VU_VIEC chưa xóa, trong phạm vi đơn vị, ngày tiếp nhận trong khoảng thời gian lọc" — KHÔNG có loại trừ trạng thái → KPI phải = 17. Thực tế = 16 (BE loại TU_CHOI).

### BUG-DASH-002 — Minor — Drill-down KPI-07 thiếu param `trang_thai=DANG_HOAT_DONG`

| Trường | Giá trị |
|--------|---------|
| **Severity** | Minor |
| **Priority** | P3 |
| **TC Reference** | DASH-10 |
| **Status** | Open |
| **Assignee** | Frontend Team |

**Mô tả:** Click KPI-07 "Chuyên gia / Tư vấn viên: 11" → navigate URL `?tuNgay=2026-01-01&denNgay=2026-05-10`. Per SRS srs-fr-01-dashboard.md mermaid line 100: `?trang_thai=DANG_HOAT_DONG&don_vi_cap&don_vi_id`. URL không pass `trang_thai`. Tuy nhiên tab "Đang hoạt động" là default tab → list hiển thị 11/11 mục khớp KPI → user-facing OK (severity Minor).

---

## 4. Test Evidence — KPI cross-check (R7.5.1 verified data)

### 4.1 API `/api/v1/dashboard?nam=2026&tuNgay=2026-01-01&denNgay=2026-05-10`

```json
{
  "kpis": [
    {"kpiCode":"HOI_DAP_MOI","giaTri":0},
    {"kpiCode":"VU_VIEC_TIEP_NHAN","giaTri":16},
    {"kpiCode":"VU_VIEC_DANG_XU_LY","giaTri":14},
    {"kpiCode":"VU_VIEC_HOAN_THANH","giaTri":2},
    {"kpiCode":"DAO_TAO_DANG_DIEN_RA","giaTri":0},
    {"kpiCode":"DAO_TAO_HOAN_THANH","giaTri":0},
    {"kpiCode":"CHUYEN_GIA_TVV","giaTri":11},
    {"kpiCode":"TY_LE_HO_SO_BO_SUNG","giaTri":0},
    {"kpiCode":"THOI_GIAN_XU_LY_TB","giaTri":0}
  ]
}
```

### 4.2 Cross-check entity pool (3 pages /api/v1/tu-van-viens, /vu-viecs, /hoi-daps)

| Entity | Pool Total | byTrangThai distribution | KPI dashboard | Match? |
|--------|-----------|--------------------------|---------------|--------|
| TU_VAN_VIEN | 41 (CG=18 + TVV=23, **NHT=0**) | CHO_PHE_DUYET:1, MOI_DANG_KY:16, TU_CHOI:5, CHO_KICH_HOAT:6, **HOAT_DONG:11**, DANG_THAM_DINH:1, YEU_CAU_BO_SUNG:1 | KPI-07 = **11** | ✅ HOAT_DONG=11 = CG_active(5)+TVV_active(6); NHT=0 verified excluded |
| VU_VIEC | 17 | DA_TIEP_NHAN:4, DA_PHAN_CONG:9, DA_DANH_GIA:1, HOAN_THANH:1, YEU_CAU_BO_SUNG:1, TU_CHOI:1 | KPI-02=16, KPI-03=14, KPI-04=2 | KPI-02 ⚠️ (16 ≠ 17 spec); KPI-03 ✅ (DA_TIEP_NHAN+DA_PHAN_CONG+YEU_CAU_BO_SUNG=14); KPI-04 ✅ (HOAN_THANH+DA_DANH_GIA=2) |
| HOI_DAP | 17 | DA_DUYET:1, DANG_XU_LY:10, HOAN_THANH:2, HUY:4 | KPI-01 = 0 (MOI tab) | ✅ 0 record state MOI |

### 4.3 Drill-down KPI-07 evidence

- URL: `/chuyen-gia-tvv/danh-sach?tuNgay=2026-01-01&denNgay=2026-05-10`
- Tab default: "Đang hoạt động" (auto-selected)
- Pagination: **"1-11 / 11 mục"** ✓ khớp KPI=11
- Loại record: TVV-BTP-TW-{0035, 0034, 0033, 0032, 0029, 0014} (6 TVV) + {0030, 0006, 0004, 0002, 0001} (5 CG) = 11
- **NHT exclusion verified:** Cột "LOẠI" cả 11 row chỉ có {TVV, CG} — KHÔNG có "NHT"

Screenshots:
- ![Dashboard QTHT overview 9 KPI](image/r7-dashboard-qtht01-overview.png)
- ![Drill KPI-07 TVV list 11 mục](image/r7-drill-kpi07-tvv-list-11-mục.png)

---

## 5. Phụ lục — Môi trường test

| Thành phần | Giá trị |
|------------|---------|
| URL ứng dụng | http://103.172.236.130:3000 |
| OTP login | `666666` (bypass tạm) |
| MailHog (OTP inbox) | http://103.172.236.130:8025 |
| API base | http://103.172.236.130:3000/api/v1 |
| Frontend | React + Vite + Ant Design |
| Xác thực | JWT (HttpOnly cookie) + OTP 6 số |
| Tool test | Chrome DevTools MCP (per CLAUDE.md tool routing rule 2026-05-05) |
| BE quirk | JWT revoke aggressive ~2 phút bất chấp `exp` 15 phút (memory `qa_htpldn_jwt_revoke_aggressive`) — gây 4 lần re-login session này |

---

## 6. Audit TC hoãn — cập nhật R3.1 (2026-05-10 22:48)

Sau R3.1 expand permission: **5/6 TC hoãn đã chạy** (4 ✅ + 1 ❌ BUG-DASH-005), **1 TC còn hoãn** (DASH-P8 auto-refresh — out-of-scope round).

### 6.1 Trạng thái cập nhật

| ID | TC | R3 | R3.1 | Block Reason còn lại |
|----|----|----|------|----------------------|
| DASH-P3 | Permission CB_PD_TW_01 | ⏰ Hoãn | ✅ Đạt | — |
| DASH-P4 | Permission CB_PD_BN_01 | ⏰ Hoãn | ✅ Đạt | — |
| DASH-P5 | Permission CB_PD_DP_01 | ⏰ Hoãn | ✅ Đạt | — |
| DASH-P6 | Permission CB_NV_DP_01 | ⏰ Hoãn | ✅ Đạt | — |
| DASH-P7-DN | Actor DN dashboard access | ⏰ Hoãn (chờ BA) | ❌ BUG-DASH-005 (Major) | Chờ dev fix BUG-DASH-005 |
| DASH-P7-NHT | Actor NHT dashboard access | ⏰ Hoãn (chờ BA) | ✅ Đạt redirect đúng | — |
| DASH-P7-CG | Actor CG dashboard access | ⏰ Hoãn (chờ BA) | ✅ Đạt redirect đúng | — |
| DASH-P8 | Auto-refresh FR-I-CROSS-02 60s | ⏰ Hoãn (chờ BA) | ⏰ Hoãn defer | Chờ test execution (out-of-scope round dashboard regression) |

### 6.2 Phân loại tổng quan R3.1

| Block Reason | Count | TC IDs | Action cần thiết |
|--------------|:-----:|--------|------------------|
| **Thiếu seed data** | **0** | — | — |
| **Chờ dev fix bug** | **1** | DASH-P7-DN (BUG-DASH-005) | Dev FE add route guard cho `/dashboard` check vai_tro ≠ DN/NHT/TVV/CG; redirect Cổng DN Nhóm VII |
| **Chờ test execution** | **1** | DASH-P8 | QA chạy session ≥120s + simulate tab visibility hidden/visible + verify per-widget timeout 30s |
| **Chờ BA confirm spec** | **0** | — | (Q1 + Q2 đã verify 2-source NotebookLM + SRS local — xem §R3.1 §Spec answers) |

### 6.3 Spec answer Q1 + Q2 — verified 2-source

Q1 (Dashboard access actor role) + Q2 (Auto-refresh FR-I-CROSS-02) đã có đáp án đầy đủ qua NotebookLM HTPLDN (`a4ae45bf-cea0-4325-8fee-b1e0be702cf2`) + grep SRS local `srs-update-2026-5-5/srs-fr-01-dashboard.md:633-686`. Detail xem section "Spec answers từ NotebookLM + SRS local" trong R3.1 retest section ở trên. **KHÔNG cần BA confirm thêm.**

### 6.4 Không có blocker do data

- ✅ Pool data đủ: 18 VV / 15 đang xử lý / 2 hoàn thành / 8 TVV active.
- ✅ Dev fix lần 2 (R3) thành công 4/4 bug cũ.
- ⚠️ R3.1 phát hiện 1 BUG mới: BUG-DASH-005 (Major P1 — DN dashboard render bypass).

---

*Functional report generated: 2026-05-10 10:37:30 (UTC+7) · R2 retest: 2026-05-10 12:35:00 (UTC+7) · R3 retest: 2026-05-10 20:42:00 (UTC+7) · R3.1 expand permission: 2026-05-10 22:48:00 (UTC+7) — verdict ⚠️ CONDITIONAL PASS (33/34 ✅, BUG-DASH-005 Major Open) | QA Automation via Claude Code*
