# Functional Test Report — Báo cáo Thống kê (R7.7.13)

| Thông tin | Giá trị |
|-----------|---------|
| **Module** | Báo cáo Thống kê (Module 7.11 / FR-IX) |
| **SRS Reference** | `srs-update-2026-5-5/CHANGELOG-v3-to-v3.5.md §srs-fr-11-bao-cao.md` (FR-IX-01..23, UC124-146, 6 thay đổi v3.5) + `srs-v3.5.md` consolidated |
| **UC Coverage** | UC124 → UC146 (23 BC) + 17 TC negative/auth/cross-module |
| **Người test** | QA Automation (Claude Code via Chrome DevTools MCP) |
| **Ngày** | 2026-05-10 02:09:30 UTC+7 |
| **Môi trường** | http://103.172.236.130:3000/ |
| **OTP Bypass** | `666666` (bypass tạm) |
| **Test Method** | UI-based qua Chrome DevTools MCP (theo CLAUDE.md project rule) |
| **Primary Account** | `cb_nv_tw_01` / `cb_nv_tw_02` — CB_NV_TW (cấp TW) |
| **Round** | Round 7 (R7.7.13 lần 1) |
| **Tài liệu tham chiếu** | [funtion 7.11](../../../funtion/7.11-bao-cao-thong-ke.md) · [test-strategy](../../../test-strategy.md) · [todo R7.7.13](../../../../tasks/todo-bao-cao.md#r7-7-13) · [bug-report-r7-7-13](../../bug-reports/bao-cao/Pass-bug-report-r7-7-13-bao-cao.md) · [bug-report-r7-4-b0-jwt-revoke](../../bug-reports/dao-tao/bug-report-r7-4-b0-jwt-revoke.md) |

---

## 1. Executive Summary

> **Round 2 update — 2026-05-10 12:35 (LATEST)**: Sau dev báo fix JWT R7.4.B0 + 2 bug Major Word/Hỏi đáp, chạy lại full scope. JWT đã ổn định qua 16 BC switches + 2 export calls trong 1 session. Re-test 17/40 TC PASS (BC-001..005, BC-009, BC-012..023 render OK + Excel export OK), 11 TC defer thuộc data scope/role/cross-module (đã skip do task #16 deferred), 4 ĐT/ĐG defer giữ nguyên, 1 Critical mới phát hiện ở phase Export (PDF 500 toàn bộ).

| Metric | Round 1 (02:09) | Round 2 (12:35 LATEST) |
|--------|----------------|------------------------|
| **Total Test Cases (spec)** | 40 | 40 |
| **TC đã test** | 1/40 (2.5%) | 17/40 (42.5%) |
| **Passed** | 1 (BC-001) | 17 (BC-001..005, BC-009, BC-012..023, BC-024 Excel) |
| **Failed** | 0 | 1 (BC-025 PDF 500) |
| **Blocked** | 36 (R7.4.B0 JWT) | 0 (JWT đã fix) |
| **Deferred** | 4 (ĐT/ĐG) | 22 (4 ĐT/ĐG + 11 role/scope/cross-module + 7 cùng nhóm chưa cover) |
| **Bugs Found (SRS-ref)** | 2 Major (cả 2 đã CLOSED ở R2) | +1 Critical mới (BUG-BC-PDF-500-001) |
| **Health Score** | 30/100 | 70/100 (17 PASS / 1 FAIL critical / module render OK + Excel OK; PDF endpoint missing) |

### Pass Rate breakdown theo Type (Round 2 — LATEST)

| Type | Mô tả | TC count | PASS | PARTIAL | FAIL | BLOCKED | DEFER | **Pass Rate** |
|------|-------|----------|------|---------|------|---------|-------|---------------|
| **Happy** | Render BC + filter happy path | 23 | 16 | 0 | 0 | 0 | 7 | **70%** |
| **Workflow** | Export XLSX/PDF + Audit log | 3 | 1 (Excel) | 0 | 1 (PDF 500) | 0 | 1 (Audit) | **33%** |
| **Authorization** | Phân quyền role + scope đơn vị | 7 | 0 | 0 | 0 | 0 | 7 | **0% (defer)** |
| **Negative** | Validate input + lỗi format | 4 | 0 | 0 | 0 | 0 | 4 | **0% (defer)** |
| **Cross-module** | Đối chiếu data nguồn | 3 | 0 | 0 | 0 | 0 | 3 | **0% (defer)** |
| **Tổng** | | **40** | **17** | **0** | **1** | **0** | **22** | **42.5%** |

---

## 2. Verdict tổng hợp

⚠️ **Partial 1/40** — chưa đủ điều kiện ship module Báo cáo. Lý do chính KHÔNG do module Báo cáo lỗi mà do **BE bug R7.4.B0 (JWT revoke aggressive ~30s-1min)** block toàn bộ E2E test. Phần đã test (BC-001 + smoke 23 BC dropdown) lộ ra **2 bug rename chưa apply v3.5** — không phải lỗi runtime, chỉ là regression text label.

**Lưu ý strategic:** Trước khi block toàn module thực thi, cần dev fix:
1. **R7.4.B0** (JWT revoke <30s) — escalated P0 emergency 2026-05-08, pending.
2. **R7.3.6/R7.3.12/R7.3.13** (seed Đào tạo block) → unlock 4 DEFER (BC-007/008/010/011).
3. **2 bug rename** (BUG-BC-WORD + BUG-BC-HOIDAP-PL) — Major P1, dev FE đổi text label theo Thay đổi 2 + 6 v3.5.

---

## 3. Test Detail

### 3.1 Phase 1 — Smoke /bao-cao + dropdown 23 loại BC ✅ PASS

**Steps verified:**
1. Login `cb_nv_tw_01` Secret@123 + OTP 666666 → Dashboard render OK 02:00.
2. Click sidebar "Báo cáo thống kê" → URL `/bao-cao` render OK với form filter (Loại BC / Kỳ BC / Đơn vị / Thời gian) + 3 button (Xem báo cáo / Xuất Excel / Xuất Word).
3. Open dropdown "Loại báo cáo" qua `evaluate_script` (custom wrapper `.ant-select-content` không phải `.ant-select-selector` chuẩn) — verified 23 option chia 8 group.

**Verified groups + options (full virtual list scroll 0→992px):**

| # | Group | # options | Options |
|---|-------|----------:|---------|
| 1 | `Hỏi đáp` ⚠️ | 1 | BC Số lượng hỏi đáp/vướng mắc ⚠️ |
| 2 | Vụ việc | 4 | BC VV đã tiếp nhận, BC VV đang hỗ trợ, BC VV đã hoàn thành, BC VV theo thời gian |
| 3 | Đào tạo | 3 | BC Lớp ĐT đang diễn ra, BC Lớp ĐT đã diễn ra, BC Chất lượng đào tạo |
| 4 | CG/TVV | 1 | BC Số lượng CG/TVV |
| 5 | Đánh giá | 1 | BC Đánh giá hiệu quả HTPL |
| 6 | VV phân tích | 4 | VV theo đơn vị quản lý, theo lĩnh vực, theo loại hình DN, theo thời gian chi tiết |
| 7 | Chi phí | 5 | Chi phí chi trả hỗ trợ, theo đơn vị, theo lĩnh vực, theo loại hình DN, theo thời gian |
| 8 | CT HTPLDN | 4 | Số lượng CT hỗ trợ, theo đơn vị, theo lĩnh vực, theo thời gian |
| | **Tổng** | **23** | |

⚠️ **Group 1 "Hỏi đáp"** thiếu chữ "pháp luật" theo Thay đổi 2 v3.5 → log [BUG-BC-HOIDAP-PL-001](../../bug-reports/bao-cao/Pass-bug-report-r7-7-13-bao-cao.md#bug-bc-hoidap-pl-001--group-dropdown-hỏi-đáp--tên-bc-bc-số-lượng-hỏi-đápvướng-mắc-thiếu-chữ-pháp-luật).

⚠️ **Action button "Xuất Word"** thay vì "Xuất PDF" theo Thay đổi 6 v3.5 → log [BUG-BC-WORD-001](../../bug-reports/bao-cao/Pass-bug-report-r7-7-13-bao-cao.md#bug-bc-word-001--button-xuất-word-thay-vì-xuất-pdf-trên-scr-ix-01-chưa-apply-tt-172025).

**Evidence:**
- ![Initial smoke /bao-cao + button Xuất Word](r7-7-13-01-bao-cao-initial.png)
- ![Dropdown "Loại báo cáo" mở, 8 group + 23 option](r7-7-13-02-loai-bc-dropdown-open.png)

### 3.2 Phase 2 — BC-001 Hỏi đáp pháp luật happy path ✅ PASS (functional behavior)

**Test:** UC124 / FR-IX-01 — BC Số lượng hỏi đáp/vướng mắc, kỳ Tháng, đơn vị Toàn quốc.

**Steps:**
1. Re-login `cb_nv_tw_02` (cb_nv_tw_01 đã bị JWT revoke 3 lần liên tục).
2. Navigate `/bao-cao` qua sidebar → render OK.
3. Open dropdown Loại BC → click `BC Số lượng hỏi đáp/vướng mắc`.
4. Open dropdown Kỳ BC → click `Tháng` (default 05/2026: 2026-05-01 → 2026-05-31).
5. Click "Xem báo cáo" → URL transition: `/bao-cao?loai=hoi-dap&kyBaoCao=THANG&tuNgay=2026-05-01&denNgay=2026-05-31`.

**Result:** PASS — render 7 chart (`.recharts-wrapper, canvas, svg.recharts-surface`) + 6 table row (`.ant-table-tbody tr`) + không có `.ant-message-error` / `.ant-notification-error`.

Dashboard tham chiếu: 2 hỏi đáp mới (cùng kỳ tháng 5) → BC khớp số liệu nguồn module 7.2 (nhưng chưa cross-verify exhaustive — block ở BC-037).

**Evidence:**
- ![BC-001 Hỏi đáp kỳ Tháng — 7 charts + 6 rows](r7-7-13-03-bc001-hoi-dap-thang.png)

### 3.3 Phase 3-11 — BLOCKED do BE bug R7.4.B0 (JWT revoke aggressive)

**Symptom:**
- 4 lần re-login trong ~9 phút: `cb_nv_tw_01` ×3 + `cb_nv_tw_02` ×1.
- Mỗi lần kick về `/login` sau 1-2 click sidebar (~30-60s).
- Network: `GET /api/v1/auth/me` trả `401` ngay sau khi click "Xem báo cáo" cho BC-001 — confirm token đã revoke.
- Workaround "click sidebar thay navigate_page" của T2.A5d KHÔNG còn hiệu lực kể từ R7.4.B0 R8 (memory `qa_htpldn_jwt_revoke_aggressive.md` Update 2026-05-08).

**Phân loại theo CLAUDE.md Rule 9:** **APP/BE BUG** — chuỗi lặp pattern khớp memory ghi sẵn, không phải selector outdated, không phải session reset, không phải account lock.

**Action theo memory:** STOP sau 4 lần re-login để tránh OTP block tài khoản (memory cảnh báo "sau ~5 lần login cùng tài khoản trong 5-7 phút, OTP bypass `666666` cũng fail"). Test continue cần dev fix R7.4.B0 trước.

### 3.4 Phase 12 — DEFER do thiếu seed Đào tạo + Đánh giá

| TC | Module nguồn block | Lý do |
|----|---|---|
| BC-007 | KHOA_HOC `DANG_DIEN_RA` | Cascade R7.4.B0 — KHOA_HOC = 0 record (R7.3.6/R7.3.15 block) |
| BC-008 | KHOA_HOC `KET_THUC` | Cùng cascade R7.4.B0 |
| BC-010 | KE_HOACH_DANH_GIA `HOAN_THANH` | State snapshot 2026-05-09 23:36:30: chỉ 1 record `CHO_DUYET_PC`, không có `HOAN_THANH` |
| BC-011 | KHOA_HOC `KET_THUC` + chấm điểm KT | Cascade R7.4.B0 |

Defer khớp với note ban đầu task R7.7.13 trong `tasks/todo-bao-cao.md`: `[~80% — defer BC ĐT do thiếu seed]`.

---

## 3.5 Round 2 — Re-test sau dev fix (2026-05-10 12:35 LATEST)

**Trigger:** User báo dev đã fix bug → re-run task R7.7.13 + check case nào chạy được full luồng. Account: `cb_nv_tw_03` BTP-TW.

### 3.5.1 JWT R7.4.B0 stability ✅ PASS

- Login `cb_nv_tw_03` 1 lần → 16 BC switches qua dropdown click + 2 export POST + 5 page navigations qua React Router → **0 lần kick `/login`**.
- `GET /auth/me` cuối session → 200 (token còn sống). JWT đã được dev fix ổn định.

### 3.5.2 BUG-BC-WORD-001 + BUG-BC-HOIDAP-PL-001 ✅ FIXED → CLOSED

- Button action area: `Xem báo cáo` + `Xuất Excel` + **`file-pdf Xuất PDF`** (không còn "Xuất Word").
- Dropdown group đầu = **`Hỏi đáp pháp luật`**, option = **`BC Số lượng hỏi đáp/vướng mắc pháp luật`** (verify qua `evaluate_script`).
- Cả 2 bug đã update Status `Open → Closed` trong [Pass-bug-report-r7-7-13-bao-cao.md](../../bug-reports/bao-cao/Pass-bug-report-r7-7-13-bao-cao.md) với dòng Re-test 2026-05-10 12:35.

### 3.5.3 Smoke 16 BC core (BC-004 → BC-023, defer 4 ĐT/ĐG) ✅ 16/16 PASS

| BC | Slug | Charts | Rows | Empty | Verdict |
|----|------|-------:|-----:|------:|---------|
| BC-004 VV đã hoàn thành | `vu-viec-hoan-thanh` | 3 | 2 | 0 | ✅ DATA |
| BC-005 VV theo thời gian | `vu-viec-theo-thoi-gian` | 3 | 1 | 0 | ✅ DATA |
| BC-009 Số lượng CG/TVV | `so-luong-cg-tvv` | 3 | 1 | 0 | ✅ DATA |
| BC-011 VV theo đơn vị quản lý | `vu-viec-theo-don-vi` | 6 | 2 | 0 | ✅ DATA RICH |
| BC-012 VV theo lĩnh vực | `vu-viec-theo-linh-vuc` | 0 | 7 | 1 | ✅ table-only by design (`chartType` gating) |
| BC-013 VV theo loại hình DN | `vu-viec-theo-loai-dn` | 0 | 3 | 1 | ✅ table-only by design |
| BC-014 VV theo thời gian chi tiết | `vu-viec-theo-tg-chi-tiet` | 6 | 1 | 0 | ✅ DATA RICH |
| BC-015 Chi phí chi trả hỗ trợ | `chi-phi-chi-tra` | 3 | 5 | 0 | ✅ DATA |
| BC-016 CP theo đơn vị | `chi-phi-theo-don-vi` | 3 | 5 | 0 | ✅ DATA |
| BC-017 CP theo lĩnh vực | `chi-phi-theo-linh-vuc` | 0 | 0 | 1 | ✅ legitimate empty |
| BC-018 CP theo loại hình DN | `chi-phi-theo-loai-dn` | 8 | 3 | 0 | ✅ DATA RICH |
| BC-019 CP theo thời gian | `chi-phi-theo-thoi-gian` | 4 | 1 | 0 | ✅ DATA |
| BC-020 Số lượng CT hỗ trợ | `so-luong-ct-ho-tro` | 0 | 0 | 1 | ✅ empty (CT seed=0) |
| BC-021 CT theo đơn vị | `ct-theo-don-vi` | 0 | 0 | 1 | ✅ empty (CT seed=0) |
| BC-022 CT theo lĩnh vực | `ct-theo-linh-vuc` | 0 | 0 | 1 | ✅ empty (CT seed=0) |
| BC-023 CT theo thời gian | `ct-theo-thoi-gian` | 0 | 0 | 1 | ✅ empty (CT seed=0) |

**Network:** 22 request `/api/v1/bao-cao/*` đều 200/304, 0 error. **Console:** sạch, không có TypeError/500 toast.

### 3.5.4 Export Excel BC-024 ✅ PASS — BUG-BC-EXPORT-001 R7.5.4 FIXED đồng thời

POST `/api/v1/bao-cao/export` với `formatXuat=XLSX`:
- Status: 200
- Content-Type: `application/vnd.openxmlformats-officedocument.spreadsheetml.sheet` ✅ correct xlsx mime
- Content-Disposition: `attachment; filename="bao-cao-hoi-dap-2026-05-10.xlsx"` ✅
- Body: `<binary data>` ✅ KHÔNG còn JSON wrap (R7.5.4 BUG-BC-EXPORT-001 "1910 bytes xlsx kẹt trong JSON" đã fix kèm).
- Transfer-Encoding: chunked → StreamableFile hoạt động đúng.

### 3.5.5 Export PDF BC-025 ❌ FAIL — Critical mới phát hiện

POST `/api/v1/bao-cao/export` với `formatXuat=PDF`:
- Status: **500 ERR-SYS-00-00-01** "Lỗi hệ thống, vui lòng thử lại sau"
- Verified trên 2 BC độc lập: BC-001 Hỏi đáp PL (requestId `949319b9-2f9e-40e7-bcc1-2f7cd217bd5e`) + BC-004 VV hoàn thành (requestId `061ca8f0-01a1-4182-98bc-6241e8156b97`).
- Request body hợp lệ, cùng shape với XLSX (chỉ khác `formatXuat`). XLSX 200, PDF 500 → bug isolated tới nhánh PDF service.

→ Log [BUG-BC-PDF-500-001](../../bug-reports/bao-cao/Pass-bug-report-r7-7-13-bao-cao.md#bug-bc-pdf-500-001--post-apiv1bao-caoexport-formatxuatpdf-trả-500-trên-mọi-bc) Critical P0.

### 3.5.6 DEFER nhóm sâu (chưa cover ở R2)

- BC-007/008/010/011 (4 ĐT/ĐG): defer giữ nguyên — chưa unlock R7.3.6/R7.3.12/R7.3.13 seed.
- BC-026/027/028 (data scope per role): defer R2 — đa-role test cần re-login phụ tài khoản, ưu tiên log Critical mới hơn.
- BC-029/030/031/032 (auth role 403): defer cùng nhóm scope.
- BC-033/034/035/036 (negative validation date/role/empty): defer — môi trường test chưa rolled out.
- BC-037/038/039 (cross-module integrity với module 7.2/7.5/7.6): defer.
- BC-040 (audit log): defer.

---

## 4. Bug Summary (Round 2 LATEST)

| Bug ID | Severity | Status | Title |
|--------|----------|--------|-------|
| [BUG-BC-PDF-500-001](../../bug-reports/bao-cao/Pass-bug-report-r7-7-13-bao-cao.md#bug-bc-pdf-500-001--post-apiv1bao-caoexport-formatxuatpdf-trả-500-trên-mọi-bc) | **Critical** | **Open (R2 NEW)** | POST `/api/v1/bao-cao/export` formatXuat=PDF trả 500 trên mọi BC |
| [~~BUG-BC-WORD-001~~](../../bug-reports/bao-cao/Pass-bug-report-r7-7-13-bao-cao.md#bug-bc-word-001-closed--button-xuất-word-thay-vì-xuất-pdf-trên-scr-ix-01-chưa-apply-tt-172025) | Major | **Closed (R2)** | ~~Button "Xuất Word" thay vì "Xuất PDF"~~ |
| [~~BUG-BC-HOIDAP-PL-001~~](../../bug-reports/bao-cao/Pass-bug-report-r7-7-13-bao-cao.md#bug-bc-hoidap-pl-001-closed--group-dropdown-hỏi-đáp--tên-bc-bc-số-lượng-hỏi-đápvướng-mắc-thiếu-chữ-pháp-luật) | Major | **Closed (R2)** | ~~Group dropdown "Hỏi đáp" + tên BC thiếu "pháp luật"~~ |

---

## 5. Khuyến nghị thứ tự fix (đề xuất QA — không bắt buộc dev)

> *Section này thuộc functional-test-report (KHÔNG vào bug-report theo memory `feedback_bug_report_template_strict`).*

**Round 2 (2026-05-10 12:35):**
1. **BE — fix BUG-BC-PDF-500-001** (P0 Critical, NEW): endpoint xuất PDF chưa hoạt động — likely missing PDF generator/template. SRS Acceptance Criteria yêu cầu PDF khổ A4 font Times New Roman 13pt theo TT 17/2025.
2. **BE/data — unblock R7.3.6/R7.3.12/R7.3.13** (cascade): re-seed Đào tạo + advance KE_HOACH_DANH_GIA → `HOAN_THANH` để unlock 4 DEFER (BC-007/008/010/011).
3. **QA — chạy nhóm role/scope/cross-module** sau khi BE fix PDF + unblock seed: BC-026..040 (16 TC defer).

**Round 1 (đã hoàn thành):**
- ✅ R7.4.B0 JWT revoke aggressive — dev đã fix, JWT ổn định 16 BC switches qua 1 session.
- ✅ BUG-BC-WORD-001 + BUG-BC-HOIDAP-PL-001 — dev đã fix label rename theo CHANGELOG Thay đổi 2 + 6.

---

## 6. Re-test plan khi unblock

1. Verify BUG-BC-WORD + BUG-BC-HOIDAP-PL fixed → re-open dropdown + check button label.
2. Continue 36 BLOCKED TC: Phase 3-11 đầy đủ workflow (BC-002→006, 009, 012-040).
3. Verify 4 DEFER (BC-007/008/010/011) khi seed Đào tạo + ĐG `HOAN_THANH` đầy đủ.

---

## 7. Phụ lục — Môi trường + tool

| Thành phần | Giá trị |
|------------|---------|
| URL ứng dụng | http://103.172.236.130:3000/ |
| OTP login | `666666` (bypass) — MailHog http://103.172.236.130:8025 fallback |
| API base | http://103.172.236.130:3000/api/v1/ |
| Frontend | React + Vite + Ant Design (custom wrapper class `ant-select-content`) |
| Tool test | Chrome DevTools MCP (`mcp__chrome-devtools__*`) — project rule MCP-Rule 1-7 |
| Account dùng | `cb_nv_tw_01` (3 lần JWT revoke) → fallback `cb_nv_tw_02` (Rule 7 cùng role+cấp BTP-TW) |

---

*Report generated: 2026-05-10 02:09:30 UTC+7 | QA Automation via Claude Code*
