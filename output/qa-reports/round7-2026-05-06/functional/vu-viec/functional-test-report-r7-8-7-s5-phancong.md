# Functional Test Report — R7.8.7-S5 Phân công VV (UC59 v3.5 refactor)

| Thông tin | Giá trị |
|-----------|---------|
| **Module** | Vụ việc — Phân công TVV/NHT (Module 7.7, Seam 5 trong E2E flow) |
| **SRS Reference** | `srs-update-2026-5-5/srs-fr-05-vu-viec.md` — FR-V.I-09 UC59 (Outputs.6 `don_vi_quan_ly`) + SCR-V.I-03 (Accordion 5) + BR-CALC-04 (priority sort) + Changelog line 18 (v3.5 rev. 2 G2+G4) |
| **UC Coverage** | UC59 — Lựa chọn người hỗ trợ (refactor v3.5: 2 thẻ Cá nhân/Tổ chức) |
| **Người test** | QA huongttt via Claude Code (Chrome DevTools MCP) |
| **Ngày** | 2026-05-12 02:00:00 → 02:25:00 (UTC+7) |
| **Môi trường** | http://103.172.236.130:3000 |
| **OTP Bypass** | `666666` |
| **Test Method** | UI-based qua Chrome DevTools MCP + isolatedContext `r787_s5_cb_nv_tw_10` + API trace qua `list_network_requests` |
| **Primary Account** | `cb_nv_tw_10` / `Secret@123` — CB Nghiệp vụ TW, đơn vị BTP-TW |
| **Round** | Round 7 — R7.8.7 (E2E 12 bước DN, sub-step S5 Phân công) |
| **Tài liệu tham chiếu** | [`bug-report-r7-8-7-e2e-seam-gaps.md`](../../bug-reports/cross-cutting/bug-report-r7-8-7-e2e-seam-gaps.md) · [`workflow-test-report-r7-8-7-e2e-dn.md`](../../workflow/cross-cutting/workflow-test-report-r7-8-7-e2e-dn.md) · [`srs-fr-05-vu-viec.md`](../../../../input/srs-update-2026-5-5/srs-fr-05-vu-viec.md) |

---

## 1. Executive Summary

| Metric | Value |
|--------|-------|
| **Total Test Cases (sub-step S5)** | 5 |
| **TC đã test** | 5/5 (100%) |
| **Passed** | 4 |
| **Failed** | 1 |
| **Blocked** | 0 |
| **Partial** | 0 |
| **Overall Pass Rate** | 80% (4/5) |
| **P0 Pass Rate** | 100% (3/3 P0 PASS) — luồng functional state advance + dropdown cascade OK |
| **Bugs Found (SRS-ref)** | 1 Minor — `BUG-E2E-S5` (label Outputs "Địa bàn" thay vì "Đơn vị quản lý") |
| **Observations (out-of-SRS)** | 0 |
| **Health Score** | 75/100 (state machine + functional OK, Outputs UI deviate spec rev. 2) |
| **Start Time** | 02:00 (UTC+7) |
| **End Time** | 02:25 (UTC+7) |
| **Total Duration** | 25 phút |
| **Browse Status** | OK — MCP single session, không crash |

### Pass Rate breakdown theo Type

| Type | Mô tả | TC count | PASS | PARTIAL | FAIL | BLOCKED | **Pass Rate** |
|------|-------|----------|------|---------|------|---------|---------------|
| **Happy** | Cá nhân + Tổ chức cascade — state advance | 2 | 2 | 0 | 0 | 0 | **100%** |
| **Validation** | BR-CALC-04 sort workload ASC | 1 | 1 | 0 | 0 | 0 | **100%** |
| **Guard** | TC TV 0 TVV active → empty + alert | 1 | 1 | 0 | 0 | 0 | **100%** |
| **UI/UX** | SCR-V.I-03 Accordion 5 label + value Outputs | 1 | 0 | 0 | 1 | 0 | **0%** |
| **Total** | | **5** | **4** | **0** | **1** | **0** | **80%** |

→ **Happy-path Pass Rate = 2/2** — state machine `DANG_KIEM_TRA → DA_PHAN_CONG` chạy OK qua UI.

### Verdict: **CONDITIONAL PASS**

Functional core (modal 2 thẻ + dropdown cascade + state advance + workload sort + empty guard) đã apply đúng spec v3.5 UC59 refactor. Tuy nhiên Outputs SCR-V.I-03 Accordion 5 chưa rename label "Địa bàn" → "Đơn vị quản lý" theo v3.5 rev. 2 G2+G4 (NĐ 77/2008 Đ.19) → log Minor `BUG-E2E-S5`. KHÔNG block release vì label rename chỉ ảnh hưởng UI hiển thị, không sai data logic.

---

## Bảng trạng thái TC (snapshot R7.8.7-S5 — LATEST 2026-05-12 02:25:00)

| TC ID | Tên TC ngắn | Status | Round phát hiện | Note (≤15 từ) |
|---|---|:-:|:-:|---|
| R7.8.7-S5.1 | Modal phân công có 2 thẻ Cá nhân/Tổ chức | ✅ Đạt | R7.8.7 | UI render đúng spec v3.5, default "Cá nhân" |
| R7.8.7-S5.2 | Phân công Cá nhân — sort workload ASC + state advance | ✅ Đạt | R7.8.7 | 4 record, sort 0→2 OK, state DA_PHAN_CONG |
| R7.8.7-S5.3 | Phân công Tổ chức — cascade 2 dropdown TC TV → TVV | ✅ Đạt | R7.8.7 | TC-BTP-TW-0001 → 4 TVV active list |
| R7.8.7-S5.4 | TC TV 0 TVV active → guard empty + alert | ✅ Đạt | R7.8.7 | TC-BTP-TW-0008 hiện alert + dropdown empty |
| R7.8.7-S5.5 | Outputs Accordion 5 hiển thị "Đơn vị quản lý" | ❌ Lỗi | R7.8.7 | Vẫn label "Địa bàn" + address — BUG-E2E-S5 |
| **Tổng** | **5 TC** | ✅4 · ❌1 · ⚠️0 · 🚫0 · ⏭0 · 🤷0 | | |

## Bảng TC chưa chạy được — cần làm gì để chạy (R7.8.7-S5)

> Hiện tại còn 1 TC fail — 1 TC chờ FE rename label theo v3.5 rev. 2 G2+G4.

| TC ID | Vì sao chưa chạy được | Cần làm gì để chạy | Ai làm |
|---|---|---|:-:|
| R7.8.7-S5.5 | Label Outputs vẫn "Địa bàn" thay vì "Đơn vị quản lý" — BUG-E2E-S5 | FE rename label + BE expose `don_vi_quan_ly` (Sở TP/Bộ ngành) trong response `goi-y-tvv` | Dev FE + Dev BE |

> **Phân loại nhóm**: B (chờ dev fix bug đã log).

---

## 2. Test Results Summary

| ID | TraceID (SRS) | Tên Test Case | Type | Priority | Result | Bug ID | Nguyên nhân / Ghi chú |
|----|---------------|---------------|------|----------|--------|--------|------------------------|
| R7.8.7-S5.1 | FR-V.I-09 UC59 + SCR-V.I-03 | Modal phân công render 2 thẻ Cá nhân/Tổ chức | UI/UX | P0 | **PASS** | — | Default tab "Cá nhân", click tab "Tổ chức" → 2 dropdown cascade hiện |
| R7.8.7-S5.2 | FR-V.I-09 + BR-CALC-04 + SM transition DANG_KIEM_TRA→DA_PHAN_CONG | Phân công Cá nhân — sort workload ASC + state advance | Happy | P0 | **PASS** | — | 4 record sort 0,0,0,2 (workload ASC), POST `/phan-cong` 201, timeline ghi đúng |
| R7.8.7-S5.3 | FR-V.I-09 §Inputs row 4-5 (cascade TC TV → TVV thuộc TC) | Phân công Tổ chức — cascade dropdown TC TV → TVV | Happy | P0 | **PASS** | — | Pick TC-BTP-TW-0001 → dropdown TVV liệt kê 4 active records của TC |
| R7.8.7-S5.4 | FR-V.I-09 §Error Handling EN-09 (TC không có TVV active → alert) | TC TV 0 TVV active → guard empty + alert | Guard | P1 | **PASS** | — | Pick TC-BTP-TW-0008 → alert hiện "Không có TVV active", dropdown TVV empty |
| R7.8.7-S5.5 | `srs-fr-05-vu-viec.md` line 18 (v3.5 rev. 2 G2+G4) + FR-V.I-09 Outputs.6 `don_vi_quan_ly` | Outputs Accordion 5 hiển thị "Đơn vị quản lý" + Sở TP/Bộ ngành | UI/UX | P2 | **FAIL** | BUG-E2E-S5 | App vẫn render label `Địa bàn` + value address của TVV (chưa apply rev. 2 rename) |

---

## 3. Bug Report

### BUG-E2E-S5 — Minor — SCR-V.I-03 Accordion 5 vẫn label "Địa bàn" + address (chưa apply v3.5 rev. 2 G2+G4)

| Trường | Giá trị |
|--------|---------|
| **Severity** | Minor |
| **Priority** | P2 |
| **TC Reference** | R7.8.7-S5.5 |
| **Status** | Open |
| **Assignee** | Dev FE + Dev BE |

**Mô tả:** Sau khi phân công cá nhân (TVV/NHT) thành công, accordion "Phân công Người hỗ trợ / Tư vấn viên" mở ra hiển thị field `Địa bàn: <address>` thay vì `Đơn vị quản lý: <Sở TP/Bộ ngành>`. Vi phạm `srs-fr-05-vu-viec.md` line 18 (v3.5 rev. 2 G2+G4) + FR-V.I-09 Outputs.6 `don_vi_quan_ly` ("KHÔNG dùng 'địa bàn' do Thẻ TVV PL có hiệu lực toàn quốc theo NĐ 77/2008 Điều 19").

**Expected vs Actual:**
- Expected: `Đơn vị quản lý: Sở Tư pháp An Giang` (Sở/Bộ ngành công nhận TVV).
- Actual: `Địa bàn: 88 Nguyễn Trãi, TP. Châu Đốc, An Giang` (address thường trú TVV).

**Impact:** UI hiển thị sai theo NĐ 77/2008 Đ.19 — user (CB) có thể hiểu nhầm TVV chỉ làm việc trong địa bàn cụ thể, trong khi TVV PL có hiệu lực toàn quốc.

**Root Cause (Suggested):** Response BE `GET /goi-y-tvv` chỉ trả `maTvv/hoTen/loaiTvv/diemDanhGiaTb/activeWorkload` — KHÔNG có field `don_vi_quan_ly`. FE fallback render `dia_chi` của TVV thay vì query Sở TP/Bộ ngành. Cần BE expose `don_vi_quan_ly` (Sở TP công nhận) + FE rename label + dùng field mới.

> Chi tiết Steps/Evidence đầy đủ: [bug-report-r7-8-7-e2e-seam-gaps.md §BUG-E2E-S5](../../bug-reports/cross-cutting/bug-report-r7-8-7-e2e-seam-gaps.md).

---

## 4. Detailed Test Results

### 4.1 R7.8.7-S5.1: Modal phân công render 2 thẻ Cá nhân/Tổ chức

**Pre-conditions:**
- CB_NV_TW_10 đã login + có VV state `DANG_KIEM_TRA` (vd `aaff0000-0000-4000-8000-000000000002`).
- VV đã qua "Kiểm tra hồ sơ" Đạt 6/6 hạng mục.

**Test Steps:**

| Step | Action | Expected | Actual | Status |
|------|--------|----------|--------|--------|
| 1 | Mở VV state `Đang kiểm tra` → click button "Phân công" | Modal "Phân công tư vấn viên" mở | Modal mở, header "Phân công tư vấn viên" | **PASS** |
| 2 | `take_snapshot` modal | Có 2 thẻ "Cá nhân" + "Tổ chức tư vấn" (radio/tab) — default "Cá nhân" active | Radio 2 option visible, default "Cá nhân" checked, dropdown "Chọn người được phân công" hiện bên dưới | **PASS** |
| 3 | Click radio "Tổ chức tư vấn" | Modal switch sang form Tổ chức với 2 dropdown cascade (TC TV → TVV thuộc TC) | UI re-render: dropdown 1 "Chọn tổ chức tư vấn" + dropdown 2 "Chọn tư vấn viên thuộc tổ chức" (disabled khi chưa pick TC) | **PASS** |

**Notes:** v3.5 UC59 refactor apply đúng — 2 thẻ Cá nhân/Tổ chức render đúng spec. Screenshot: [`image/r787-s5-modal-phancong-canhan-dropdown.png`](image/r787-s5-modal-phancong-canhan-dropdown.png).

---

### 4.2 R7.8.7-S5.2: Phân công Cá nhân — sort workload ASC + state advance

**Pre-conditions:**
- Modal phân công đang ở thẻ "Cá nhân" (S5.1 PASS).
- DB có ≥4 TVV/NHT state HOAT_DONG với mix workload (0 → 2 VV đang xử lý).

**Test Steps:**

| Step | Action | Expected | Actual | Status |
|------|--------|----------|--------|--------|
| 1 | Click dropdown "Chọn người được phân công" | Dropdown mở, render 4 record sort theo `activeWorkload` ASC | 4 record: TVV-BTP-TW-0034 (0 VV) → TVV-BTP-TW-0035 (0 VV) → NHT-STP-AG-0001 (0 VV) → TVV-BTP-TW-0032 (2 VV) | **PASS** |
| 2 | Verify response `GET /vu-viecs/{id}/goi-y-tvv?limit=20` | 200 + data array sort ASC + meta `casePriorityScore` | 200, 4 records, `meta.casePriorityScore=2, isHighPriority=false` | **PASS** |
| 3 | Pick TVV-BTP-TW-0034 "TVV R12 A18 UI Walk" → click "Xác nhận" | POST `/phan-cong` 201, state DANG_KIEM_TRA → DA_PHAN_CONG | POST 201, state advance, timeline ghi `Phân công (cá nhân) 12/05/2026 02:21 CB Nghiệp vụ TW 10` | **PASS** |

**Notes:** BR-CALC-04 sort workload ASC verified. 4 tiêu chí ưu tiên còn lại (DN nữ chủ +3, LĐ nữ +2, LĐ KT +2, FIFO +1) chưa test full vì sample DN không có flag — defer cho TC riêng. Screenshot: [`image/r787-s5-modal-phancong-canhan-dropdown.png`](image/r787-s5-modal-phancong-canhan-dropdown.png).

---

### 4.3 R7.8.7-S5.3: Phân công Tổ chức — cascade dropdown TC TV → TVV thuộc TC

**Pre-conditions:**
- VV mới (state `DANG_KIEM_TRA`) — phải tạo VV mới sau khi S5.2 advance state.
- DB có ≥1 TC TV active với ≥1 TVV thuộc TC.

**Test Steps:**

| Step | Action | Expected | Actual | Status |
|------|--------|----------|--------|--------|
| 1 | Modal phân công → click radio "Tổ chức tư vấn" | UI render 2 dropdown cascade — dropdown 2 (TVV) disabled | 2 dropdown hiện, dropdown TVV disabled với placeholder "Chọn tổ chức trước" | **PASS** |
| 2 | Click dropdown "Chọn tổ chức tư vấn" → pick TC-BTP-TW-0001 | Dropdown TVV enable + load TVV thuộc TC | Dropdown TVV enable, load 4 TVV active thuộc TC-BTP-TW-0001 | **PASS** |
| 3 | Verify response `GET /to-chuc-tu-van/{tcId}/tvv-active` | 200 + data array TVV cùng TC | 200, 4 records, đúng TC | **PASS** |

**Notes:** Cascade hoạt động đúng — dropdown TVV chỉ enable sau khi TC chọn. Screenshot: [`image/r787-s5-modal-phancong-tochuc-cascade.png`](image/r787-s5-modal-phancong-tochuc-cascade.png).

---

### 4.4 R7.8.7-S5.4: TC TV 0 TVV active → guard empty + alert

**Pre-conditions:**
- VV mới state `DANG_KIEM_TRA`.
- DB có TC TV `TC-BTP-TW-0008` có 0 TVV active (verified qua API `/to-chuc-tu-van/.../tvv-active` trả empty array).

**Test Steps:**

| Step | Action | Expected | Actual | Status |
|------|--------|----------|--------|--------|
| 1 | Modal phân công → click radio "Tổ chức tư vấn" → pick TC-BTP-TW-0008 | Alert "Không có TVV active trong tổ chức này" hiện + dropdown TVV vẫn empty | Alert AntD `.ant-alert-warning` hiện text "Không có TVV active trong tổ chức này", dropdown TVV liệt kê 0 option | **PASS** |
| 2 | Click "Xác nhận" mà chưa pick TVV | Button "Xác nhận" disabled hoặc form trả validation error | Button disabled (greyed), không trigger POST | **PASS** |

**Notes:** Guard empty TC verified — App đúng spec FR-V.I-09 §Error Handling EN-09. Screenshot: [`image/r787-s5-modal-phancong-tochuc-empty-tvv-guard.png`](image/r787-s5-modal-phancong-tochuc-empty-tvv-guard.png).

---

### 4.5 R7.8.7-S5.5: Outputs Accordion 5 hiển thị "Đơn vị quản lý" + Sở TP/Bộ ngành

**Pre-conditions:**
- S5.2 PASS (VV `aaff0000-0000-4000-8000-000000000002` đã advance state DA_PHAN_CONG với TVV-BTP-TW-0034).

**Test Steps:**

| Step | Action | Expected | Actual | Status |
|------|--------|----------|--------|--------|
| 1 | Mở VV `aaff0000-0000-4000-8000-000000000002` → click accordion "Phân công Người hỗ trợ / Tư vấn viên" mở rộng | Accordion 5 render 4 field gồm `Đơn vị quản lý: Sở Tư pháp <tỉnh>` | Accordion render `Địa bàn: 88 Nguyễn Trãi, TP. Châu Đốc, An Giang` (address của TVV) | **FAIL** |
| 2 | Inspect DOM label text | Label DOM `<span>` chứa text "Đơn vị quản lý" | Label DOM chứa text "Địa bàn" | **FAIL** |
| 3 | Verify response `GET /goi-y-tvv` có field `don_vi_quan_ly` | Field `don_vi_quan_ly` trong record TVV | Response chỉ có `maTvv/hoTen/loaiTvv/diemDanhGiaTb/activeWorkload` — KHÔNG có `don_vi_quan_ly` | **FAIL** |

**Notes:** Bug log `BUG-E2E-S5` (Minor, P2). Cần FE rename label + BE expose field `don_vi_quan_ly` (Sở TP/Bộ ngành công nhận TVV). Screenshot: [`image/r787-s5-bug-output-label-diaban-vs-spec-donviquanly.png`](image/r787-s5-bug-output-label-diaban-vs-spec-donviquanly.png).

---

## 5. Test Data Used

### 5.1 Tài khoản test

| Username | Role | Đơn vị | Cấp | Dùng cho TC |
|----------|------|--------|-----|-------------|
| `cb_nv_tw_10` | CB_NV_TW | BTP-TW | TW | R7.8.7-S5.1 → S5.5 (primary tester) |

### 5.2 Data tạo/sử dụng trong test

| ID / Mã | Tên / Mô tả | Purpose | Cleanup? |
|---------|-------------|---------|----------|
| `aaff0000-0000-4000-8000-000000000002` | VV `VV-QA-R7-PRIVACY-DNAG003` | Subject VV state DA_TIEP_NHAN → DA_PHAN_CONG (S5.2) | Keep — evidence cho BUG-E2E-S5 |
| `TVV-BTP-TW-0034` | TVV R12 A18 UI Walk (0 workload) | Pick cá nhân S5.2 | Keep — workload=1 sau test |
| `TC-BTP-TW-0001` | Tổ chức tư vấn TW 01 | Pick tổ chức S5.3 (cascade dropdown TVV) | Keep |
| `TC-BTP-TW-0008` | Tổ chức tư vấn TW 08 (0 TVV active) | Pick tổ chức S5.4 (guard empty) | Keep |

---

## 6. Environment Notes

- **API endpoint pattern:** `/api/v1/vu-viecs/{id}/{action}` (kiem-tra / goi-y-tvv / phan-cong)
- **Auth flow:** JWT cookie + OTP `666666` bypass
- **Token TTL:** ~2 phút thực (BE revoke aggressive — memory `qa_htpldn_jwt_revoke_aggressive`) — không ảnh hưởng S5 vì test trong window ngắn
- **Frontend framework:** React + Vite + Ant Design v5
- **Backend:** NestJS + PostgreSQL
- **State machine reference:** `02-thu-tu-module.md` SM-VUVIEC — verified transition DANG_KIEM_TRA → DA_PHAN_CONG OK
- **Test method:** Chrome DevTools MCP (`mcp__chrome-devtools__*`) với `isolatedContext=r787_s5_cb_nv_tw_10` — single session 25 phút không crash

---

## 7. Recommendations

### Must Fix (Before Release)

Không có. Functional core PASS, không có bug Critical/Major block release.

### Should Fix

1. **BUG-E2E-S5 (Minor, P2):** FE rename label "Địa bàn" → "Đơn vị quản lý" trong SCR-V.I-03 Accordion 5. BE expose field `don_vi_quan_ly` (Sở TP/Bộ ngành công nhận TVV) trong response `GET /goi-y-tvv` + endpoint trả thông tin TVV cho FE render. Cần 1 sprint FE + 1 task BE.

### Additional Recommendations

2. **Test BR-CALC-04 đầy đủ:** Tạo TC riêng test 4 tiêu chí priority còn lại (DN nữ chủ +3, LĐ nữ +2, LĐ KT +2, FIFO +1) — round này chỉ verify workload ASC vì sample DN không có flag.
3. **Test Outputs Accordion 5 cho phân công Tổ chức:** Hiện tại chỉ verify Outputs sau phân công Cá nhân. Cần test thêm Outputs khi phân công Tổ chức để verify G2 "thêm row 'Tên tổ chức: <tên TC TV>'" có apply không.

---

## 8. Appendix

### A — API Endpoints Tested

| Method | Endpoint | Purpose | Tested in TC |
|--------|----------|---------|--------------|
| POST | `/api/v1/vu-viecs/{id}/kiem-tra` | Advance state DA_TIEP_NHAN → DANG_KIEM_TRA | S5 pre-condition |
| GET | `/api/v1/vu-viecs/{id}/goi-y-tvv?limit=20` | Lấy danh sách gợi ý TVV/NHT (sort workload + priority) | S5.2 |
| POST | `/api/v1/vu-viecs/{id}/phan-cong` | Phân công TVV/NHT + state advance DA_PHAN_CONG | S5.2 |
| GET | `/api/v1/to-chuc-tu-van/{tcId}/tvv-active` | Cascade dropdown TVV thuộc TC | S5.3, S5.4 |

### B — Screenshots

| File | Mô tả | TC Ref |
|------|-------|--------|
| [`image/r787-s5-modal-phancong-canhan-dropdown.png`](image/r787-s5-modal-phancong-canhan-dropdown.png) | Modal thẻ Cá nhân + dropdown 4 record sort workload | S5.1, S5.2 |
| [`image/r787-s5-modal-phancong-tochuc-cascade.png`](image/r787-s5-modal-phancong-tochuc-cascade.png) | Modal thẻ Tổ chức + cascade 2 dropdown TC TV → TVV | S5.3 |
| [`image/r787-s5-modal-phancong-tochuc-empty-tvv-guard.png`](image/r787-s5-modal-phancong-tochuc-empty-tvv-guard.png) | TC-BTP-TW-0008 → alert empty TVV active | S5.4 |
| [`image/r787-s5-bug-output-label-diaban-vs-spec-donviquanly.png`](image/r787-s5-bug-output-label-diaban-vs-spec-donviquanly.png) | Accordion 5 hiển thị "Địa bàn" + address — bug evidence | S5.5 |

### C — SRS Traceability Matrix

| SRS Reference | TC Coverage | Status |
|---------------|-------------|--------|
| `FR-V.I-09 UC59` (Processing 2 thẻ Cá nhân/Tổ chức) | S5.1, S5.2, S5.3 | 3/3 PASS |
| `BR-CALC-04` (priority sort) | S5.2 (workload ASC verified) | 1/1 PASS (4 tiêu chí khác defer) |
| `FR-V.I-09 §Error Handling EN-09` (TC 0 TVV active → alert) | S5.4 | 1/1 PASS |
| `srs-fr-05-vu-viec.md` line 18 + FR-V.I-09 Outputs.6 (v3.5 rev. 2 G2+G4) | S5.5 | FAIL — `BUG-E2E-S5` |
| `02-thu-tu-module.md` SM-VUVIEC transition DANG_KIEM_TRA → DA_PHAN_CONG | S5.2 | 1/1 PASS |

---

*Report generated: 2026-05-12 02:30:00 | QA huongttt via Claude Code (Chrome DevTools MCP)*
