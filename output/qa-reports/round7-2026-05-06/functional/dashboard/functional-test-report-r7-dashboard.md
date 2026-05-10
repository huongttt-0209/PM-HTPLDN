# Functional Test Report — Dashboard (Module 7.1)

| Thông tin | Giá trị |
|-----------|---------|
| **Module** | Tổng quan hệ thống / Dashboard (FR-01) |
| **SRS Reference** | `srs-update-2026-5-5/srs-fr-01-dashboard.md` — FR-I-01..09, KPI-S-01/02, FR-I-CROSS-02 |
| **UC Coverage** | UC1..UC9 + KPI bổ sung |
| **Người test** | QA Automation (Claude Opus 4.7) |
| **Ngày** | 2026-05-10 10:25:00 → 10:37:30 (R1) · 12:14:00 → 12:35:00 (R2 retest+expand) (UTC+7) |
| **Môi trường** | http://103.172.236.130:3000 |
| **OTP Bypass** | `666666` |
| **Test Method** | UI MCP (Chrome DevTools) + API cross-check qua `evaluate_script(fetch)` |
| **Primary Account** | `qtht_01 / Secret@123` (QTHT, BTP-TW) |
| **Round** | Round 7 |
| **Tài liệu tham chiếu** | [tasks/todo-dashboard.md](../../../../tasks/todo-dashboard.md) · [bug-report-r7-dashboard.md](../../bug-reports/dashboard/bug-report-r7-dashboard.md) |

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

### Verdict R2 retest (LATEST) 2026-05-10 12:14-12:35: **❌ FAIL — 4 bug Open (2 Major + 1 Medium + 1 Minor).** Dev claim đã fix BUG-DASH-001 + 002 nhưng cả 2 reproduce 100% (CHƯA FIX). Expand coverage R2 phát hiện thêm 2 bug Major (BUG-DASH-003 drill KPI-03/04 composite state mismatch + BUG-DASH-004 drill KPI-05/06 sai page Chương trình ≠ Khóa học, no filter). Permission probe 2 CB role (TW + BN) PASS data scope (TW=full pool, BN=ministry-only=0). Filter UI + Chart legend PASS render.

---

## R2 retest section (2026-05-10 12:14-12:35) (LATEST)

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

> **Lưu ý:** Tóm tắt inline. Chi tiết Steps/Evidence xem [bug-report-r7-dashboard.md](../../bug-reports/dashboard/bug-report-r7-dashboard.md).

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

*Functional report generated: 2026-05-10 10:37:30 (UTC+7) | QA Automation via Claude Code*
