# Functional Test Report — R7.7.1 Hỏi đáp Phase 3b UI-only (Retest)

| Thông tin | Giá trị |
|-----------|---------|
| **Module** | Quản lý hỏi đáp pháp lý (Module 7.2) |
| **SRS Reference** | `srs-update-2026-5-5/srs-fr-02-hoi-dap.md` v3.5 — FR-II-04 (Tiếp nhận), FR-II-06 (Phân công), FR-II-NEW-04 (Cập nhật thời hạn) |
| **UC Coverage** | UC HD-30 / HD-49 / HD-50 / HD-51 / HD-52 / HD-59 |
| **Người test** | QA Automation (Claude Code) |
| **Ngày** | 2026-05-10 |
| **Môi trường** | http://103.172.236.130:3000/ |
| **OTP Bypass** | `666666` (bypass tạm) |
| **Test Method** | UI-only via Chrome DevTools MCP — fill_form / click / evaluate_script. API only as supporting evidence (`list_network_requests` + `get_network_request`) |
| **Primary Account** | `cb_nv_tw_04` (CB_NV TW), `cb_nv_tw_05` (CB_NV TW — Session B HD-059) |
| **Round** | Round 7 / R7.7.1 Phase 3b — Retest careful sau Phase 3b first-run (00:35-00:48) |
| **Tài liệu tham chiếu** | [todo-hoi-dap.md R7.7.1](../../../../tasks/todo-hoi-dap.md#r7-7-1) · [Pass-bug-report-r7-7-1-hd-049-tc-org-ui-block.md](../../bug-reports/hoi-dap/Pass-bug-report-r7-7-1-hd-049-tc-org-ui-block.md) · `srs-update-2026-5-5/srs-fr-02-hoi-dap.md` |

---

## 1. Executive Summary

| Metric | Value |
|--------|-------|
| **Total Test Cases (spec)** | 6 (HD-030, HD-049, HD-050, HD-051, HD-052, HD-059) |
| **TC đã test / Tổng TC** | 6/6 (100%) |
| **Passed** | 2 (HD-030 upgrade từ PARTIAL → PASS, HD-059 mới PASS) |
| **Failed** | 1 (HD-049 reproduces — FE bug Major) |
| **Blocked** | 3 (HD-050, HD-051 cascade từ HD-049; HD-052 scope-only) |
| **Partial** | 0 (HD-030 trước PARTIAL → upgrade PASS lần này) |
| **Overall Pass Rate** | 33% (2/6, PARTIAL không tính PASS) |
| **P0 Pass Rate** | 33% (2/6 P0 tested) |
| **Bugs Found (SRS-ref)** | 1 (0 Critical, 1 Major, 0 Medium, 0 Minor) — BUG-HD-049-TC-ORG-UI-001 reproduces |
| **Observations (out-of-SRS)** | 0 |
| **Health Score** | 50/100 — happy path concurrency PASS đầy đủ, nhưng nhánh TC TV blocker giữ Open |
| **Start Time** | 00:35 (UTC+7) |
| **End Time** | 01:30 (UTC+7) |
| **Total Duration** | ~55 phút (gồm 13 phút first-run + ~42 phút retest careful) |
| **Browse Status** | OK — Chrome DevTools MCP stable, 1 cross-context isolation cho HD-059 |

### Pass Rate breakdown theo Type

| Type | Mô tả | TC count | PASS | PARTIAL | FAIL | BLOCKED | **Pass Rate** |
|------|-------|----------|------|---------|------|---------|---------------|
| **Happy** | TIEP_NHAN → DANG_XU_LY phân công cá nhân (HD-030) | 1 | 1 | 0 | 0 | 0 | **100%** |
| **Workflow** | Concurrency version conflict 2 phiên (HD-059) | 1 | 1 | 0 | 0 | 0 | **100%** |
| **Authorization** | — | 0 | 0 | 0 | 0 | 0 | — |
| **Negative** | Validate thiếu TC/TVV (HD-051) | 1 | 0 | 0 | 0 | 1 | **0%** |
| **Validation** | Filter TVV theo TC (HD-050) | 1 | 0 | 0 | 0 | 1 | **0%** |
| **Edge / Guard** | Bypass UI TVV không thuộc TC (HD-052) | 1 | 0 | 0 | 0 | 1 | **0%** |
| **Integration** | UI render TC list cấp 1 (HD-049) | 1 | 0 | 0 | 1 | 0 | **0%** |
| **Total** | | **6** | **2** | **0** | **1** | **3** | **33%** |

→ **Happy-path Pass Rate = 1/1 (100%)**, **Workflow Pass Rate = 1/1 (100%)** — concurrency hoạt động đúng. Phase 3b nhánh phân công TC TV vẫn block do FE bug binding.

### Verdict: **CONDITIONAL PASS**

Concurrency 409 + happy assign cá nhân hoạt động đúng SRS. Nhánh "Tổ chức tư vấn" của modal Phân công không render danh sách TC TV cấp 1 dù BE trả 200 với 7 TC active — block 3 TC còn lại. Cần FE fix BUG-HD-049-TC-ORG-UI-001 trước khi đóng nhánh phân công TO_CHUC của FR-II-06.

---

## 2. Test Results Summary

| ID | TraceID (SRS) | Tên Test Case | Type | Priority | Result | Bug ID | Nguyên nhân / Ghi chú |
|----|---------------|---------------|------|----------|--------|--------|------------------------|
| HD-030 | FR-II-04 + FR-II-06 (UC HD-30) | Phân công cá nhân: `TIEP_NHAN → DANG_XU_LY` end-to-end | Happy | P0 | **PASS** | — | Stepper "Tiếp nhận" đã check, header state = "Đang xử lý", `nguoiPhanCongTen` = "Đinh Văn Mười Bốn", lichSu CREATE→TIEP_NHAN→PHAN_CONG. Verified API `GET /hoi-daps/{id}` = `trangThai:DANG_XU_LY`, `version:3`. Upgrade từ PARTIAL → PASS. |
| HD-049 | FR-II-06 §Phân công TC TV cấp 1 | Tab "Tổ chức tư vấn" trong modal Phân công render danh sách TC TV `HOAT_DONG` cấp 1 | Integration | P0 | **FAIL** | BUG-HD-049-TC-ORG-UI-001 | Segmented `Tổ chức tư vấn` selected nhưng table headers vẫn `Họ tên/Email/Workload` (40 rows cá nhân). API `GET /to-chuc-tu-vans?trangThai=HOAT_DONG` reqid=232 → 200 với 7 TC active. FE bug binding/render. Reproduces từ first-run. |
| HD-050 | FR-II-06 §Filter TVV theo TC đã chọn | Chọn 1 TC TV cấp 1 → table cấp 2 chỉ hiện TVV thuộc TC | Validation | P0 | **BLOCKED** | BUG-HD-049-... | Block bởi HD-049: không có TC list để chọn cấp 1 → không thể test filter cấp 2. |
| HD-051 | FR-II-06 §Validate thiếu TC/TVV → ERR-PC-04 | Submit Phân công TO_CHUC thiếu TC hoặc thiếu TVV | Negative | P0 | **BLOCKED** | BUG-HD-049-... | Block bởi HD-049: nhánh TO_CHUC không hoạt động → không thể submit thiếu field để verify ERR-PC-04. |
| HD-052 | FR-II-06 §Bypass UI TVV không thuộc TC | API negative: gán TVV cấp 2 không thuộc TC cấp 1 → BE reject | Edge / Guard | P1 | **BLOCKED** | — | TC gốc spec là API-bypass negative; không feasible UI-only. Cần BA quyết: (a) cho phép API negative riêng, hoặc (b) UI có path tương đương. |
| HD-059 | FR-II-NEW-04 §Optimistic locking version | 2 phiên cùng record cùng version → submit deadline → phiên thứ 2 nhận 409 ERR-STATE-LOCK | Workflow | P0 | **PASS** | — | Session A (cb_nv_tw_04, page 1) submit version=3 → 200, BE bump version=4. Session B (cb_nv_tw_05, page 2 isolatedContext) submit version=3 stale → **409 ERR-STATE-LOCK-409** "Dữ liệu đã bị thay đổi bởi người dùng khác". Optimistic locking hoạt động đúng. |

---

## 3. Bug Report

> Tóm tắt inline. Chi tiết Steps/Evidence xem [Pass-bug-report-r7-7-1-hd-049-tc-org-ui-block.md](../../bug-reports/hoi-dap/Pass-bug-report-r7-7-1-hd-049-tc-org-ui-block.md).

### BUG-HD-049-TC-ORG-UI-001 — Major — Tab "Tổ chức tư vấn" của modal Phân công không render TC list cấp 1

| Trường | Giá trị |
|--------|---------|
| **Severity** | Major |
| **Priority** | P0 |
| **TC Reference** | HD-049 (FAIL), HD-050 (BLOCKED), HD-051 (BLOCKED) |
| **Status** | Open (reproduces R10b 2026-05-10 01:25:24) |
| **Assignee** | FE Team |

**Mô tả:** Trong modal Phân công xử lý của Hỏi đáp, khi switch segmented control sang "Tổ chức tư vấn", segmented control selected đúng nhưng phần body bên dưới vẫn render bảng "Cá nhân chịu trách nhiệm" với 40 user. BE API `to-chuc-tu-vans?trangThai=HOAT_DONG` đã trả 200 với 7 TC TV active (2 cover linhVuc Doanh nghiệp). FE không bind dữ liệu API vào view layer của tab TC TV.

**Các bước tái hiện:** Login `cb_nv_tw_04` → mở `HD-20260509-004` (state TIEP_NHAN) → click [Phân công] → click segmented option "Tổ chức tư vấn".

**Expected vs Actual:** Expected — table cấp 1 với 7 TC TV active (cột mã/tên/loại hình/lĩnh vực/người đại diện) và Select dropdown TC để filter theo lĩnh vực. Actual — table cá nhân giữ nguyên (Họ tên/Email/Workload, 40 rows), Select TC TV không có placeholder/options.

**Impact:** Block toàn bộ nhánh phân công TO_CHUC của FR-II-06 (3/6 TC Phase 3b BLOCKED).

**Root Cause (Suggested):** FE conditional render section body theo `loaiDoiTuongXuLy` không nhận event change từ AntD Segmented; hoặc binding state trỏ vào props sai (vẫn trỏ list `nhanSu` thay vì `toChucTuVans`). Cần FE inspect Redux/Zustand store sau khi click segmented + thêm useEffect dispatch fetch TC list.

---

## 4. Detailed Test Results

### 4.1 HD-030: Phân công cá nhân `TIEP_NHAN → DANG_XU_LY`

**Pre-conditions:**
- Login `cb_nv_tw_04` (CB_NV TW)
- Có ≥1 record state TIEP_NHAN (HD-20260509-004 sẵn từ Phase 2)
- Có ≥1 user xử lý workload=0 trong table (chọn "Đinh Văn Mười Bốn")

**Test Data:**
```json
{
  "hoiDapId": "2c68648d-87b7-432c-aea2-b4f26ccf6e71",
  "maHoiDap": "HD-20260509-004",
  "linhVuc": "Doanh nghiệp",
  "kenhTiepNhan": "DVC",
  "trangThaiTruoc": "TIEP_NHAN",
  "trangThaiSau": "DANG_XU_LY",
  "loaiDoiTuongXuLy": "CA_NHAN",
  "nguoiPhanCong": "Đinh Văn Mười Bốn (workload=0)"
}
```

**Test Steps:**

| Step | Action | Expected | Actual | Status |
|------|--------|----------|--------|--------|
| 1 | UI: vào `/hoi-dap` → click record HD-20260509-004 | Detail page render, header state = "Tiếp nhận" | Stepper hiện 7 steps, state = "Tiếp nhận", action panel có 3 button [Phân công] [Cập nhật thời hạn] [Sửa] | PASS |
| 2 | Click [Phân công] | Modal "Phân công xử lý — #HD-20260509-004" mở, segmented mặc định "Cá nhân", table 41 user load | Modal mở đúng, default `Cá nhân` checked, table 41 user, Phân công button disabled | PASS |
| 3 | Chọn radio user "Đinh Văn Mười Bốn" workload=0 | Phân công button enabled | Button enabled (disabled=false, class `ant-btn-primary`) | PASS |
| 4 | Click [Phân công] submit | Toast success + state header → "Đang xử lý" + lichSu thêm row PHAN_CONG | Header state = "Đang xử lý", stepper "Tiếp nhận" có check icon, "Người phân công" = "Đinh Văn Mười Bốn", section "Soạn phản hồi" xuất hiện (chỉ render ở DANG_XU_LY) | PASS |
| 5 | API verify: `GET /hoi-daps/{id}` reqid=237 | `trangThai:"DANG_XU_LY"`, `loaiDoiTuongXuLy:"CA_NHAN"`, `nguoiPhanCongTen:"Đinh Văn Mười Bốn"`, `version:3`, lichSu CREATE→TIEP_NHAN→PHAN_CONG | Match exact spec | PASS |

**Notes:**
- Phase 3b first-run mark PARTIAL vì chưa verify final state. Retest careful chốt PASS qua API JSON.
- Evidence: [r7-7-1-hd-030-retest-dangxuly-pass.png](r7-7-1-hd-030-retest-dangxuly-pass.png)

---

### 4.2 HD-049: Tab "Tổ chức tư vấn" render TC list cấp 1

**Pre-conditions:**
- Login `cb_nv_tw_04`
- Modal Phân công đang mở trên record TIEP_NHAN/DANG_XU_LY
- BE phải có ≥1 TC TV state HOAT_DONG (verified 7 TC trong seed R7.3.1.MoB)

**Test Data:**
```json
{
  "loaiDoiTuongXuLy": "TO_CHUC",
  "linhVucCanFilter": "Doanh nghiệp",
  "expectedTCTVCount": 2,
  "expectedTCTVCovers": ["TC-BTP-TW-0001 Alpha", "TC-BTP-TW-0002 Beta"]
}
```

**Test Steps:**

| Step | Action | Expected | Actual | Status |
|------|--------|----------|--------|--------|
| 1 | Mở modal Phân công trên HD-20260509-004 | Default `Cá nhân` selected, table 41 user | OK | PASS |
| 2 | Click segmented option "Tổ chức tư vấn" (qua `evaluate_script` vì AntD a11y label không enable click trực tiếp) | Segmented switch sang "Tổ chức tư vấn"; section body đổi sang bảng TC TV cấp 1 (cột Mã/Tên/Loại hình/Lĩnh vực/Người đại diện) + Select TC TV | Segmented đúng (`ant-segmented-item-selected` checked = "Tổ chức tư vấn"); body GIỮ NGUYÊN table cá nhân `Họ tên/Email/Workload` 40 rows; Select TC TV render nhưng `placeholder=null, selected=null` | **FAIL** |
| 3 | Click vào Select TC TV để mở dropdown | Dropdown overlay hiện ≥7 TC TV options | `.ant-select-dropdown:not(.hidden)` count = 0 → dropdown không mở; không option | **FAIL** |
| 4 | API verify song song reqid=232 | `to-chuc-tu-vans?trangThai=HOAT_DONG&pageSize=100&page=1` 200 với data ≥7 TC | Đúng 7 TC (TC-BTP-TW-0001..0008 trừ TC bị cancel), 2 cover linhVuc Doanh nghiệp | API PASS — FE BIND BUG |

**Notes:**
- Bug reproduces từ first-run (00:44-00:47) ở record cùng tên + retest 01:25:24 trên cùng record sau khi nó chuyển sang DANG_XU_LY (BUG không liên quan state record).
- Evidence: [r7-7-1-hd-049-retest-tc-tab-broken.png](r7-7-1-hd-049-retest-tc-tab-broken.png), [r7-7-1-hd-049-modal-viewport-tc-tab.png](r7-7-1-hd-049-modal-viewport-tc-tab.png).
- API response chi tiết save trong bug-report.

---

### 4.3 HD-050 / HD-051 (BLOCKED)

| Sub-TC | Lý do BLOCKED |
|--------|---------------|
| **HD-050** Filter TVV theo TC đã chọn | Cần TC list cấp 1 để chọn 1 TC, từ đó verify table cấp 2 chỉ hiện TVV thuộc TC đó. UI cấp 1 không render → không thể chọn → không thể verify cấp 2. |
| **HD-051** Validate thiếu TC/TVV | Cần submit nhánh TO_CHUC nhưng nhánh không hoạt động. ERR-PC-04 không thể trigger UI-only. |

→ Cả 2 chờ FE fix BUG-HD-049-TC-ORG-UI-001 rồi retest.

---

### 4.4 HD-052: Bypass UI TVV không thuộc TC (BLOCKED)

**Pre-conditions:** spec gốc HD-052 là negative API test (gửi `nhanSuId` là TVV không thuộc `toChucTuVanId`). UI flow chuẩn không cho phép gửi mismatch (cấp 2 lọc theo cấp 1).

**Reason BLOCKED:** Project rule cấm dùng API direct để pass test (CLAUDE.md MCP-Rule + memory `feedback_test_method_ui_only`). HD-052 cần BA xác nhận:

- (a) Cho phép ngoại lệ API-only cho TC negative này → tester gửi POST `phan-cong` với mismatch → kỳ vọng 422 ERR-PC-04 hoặc tương tự.
- (b) UI có path tương đương (vd "Lock TC sau khi chọn TVV" rồi đổi cấp 2) → tester verify qua UI.

→ Đẩy ra BA decision queue, không tự quyết.

---

### 4.5 HD-059: Optimistic locking 2-session

**Pre-conditions:**
- 2 isolatedContext: page 1 (cb_nv_tw_04), page 2 isolatedContext=`hd059_session_b` (cb_nv_tw_05)
- Cùng record HD-20260509-004, cùng `version:3` lúc cả 2 load detail

**Test Data:**
```json
{
  "session_A": { "deadline_new": "22/05/2026 10:00", "lyDo": "Session A - cb_nv_tw_04 ...", "version": 3 },
  "session_B": { "deadline_new": "20/05/2026 14:00", "lyDo": "Session B - cb_nv_tw_05 ...", "version": 3 }
}
```

**Test Steps:**

| Step | Action | Expected | Actual | Status |
|------|--------|----------|--------|--------|
| 1 | Page 1 (A): Mở record + click [Cập nhật thời hạn] | Modal mở, "Thời hạn hiện tại: 16/05/2026 00:41" | OK | PASS |
| 2 | Page 2 (B isolatedContext): Login `cb_nv_tw_05` → vào cùng record + click [Cập nhật thời hạn] | Modal mở same state | OK | PASS |
| 3 | Page 2 (B): Fill date `20/05/2026 14:00:00` + reason → click date picker OK → Submit button enabled | Cả 2 field valid | OK (sau press Ctrl+A + Delete + fill + Enter để chốt date input clean) | PASS |
| 4 | Page 1 (A): Fill date `22/05/2026 10:00:00` + reason → Submit `Cập nhật` | POST `cap-nhat-thoi-han` với version=3 → 200, version BE bump = 4 | Header state header SLA "Còn 9 ngày LV" (deadline = 22/05/2026 10:00) | PASS |
| 5 | Page 2 (B): Submit `Cập nhật` (form vẫn giữ version=3 stale) | POST với version=3 → BE detect mismatch (BE đã 4) → 409 ERR-STATE-LOCK-409 | reqid=234 `POST /cap-nhat-thoi-han` Status **409**, body `{"error":{"code":"ERR-STATE-LOCK-409","message":"Dữ liệu đã bị thay đổi bởi người dùng khác","timestamp":"2026-05-09T18:30:13.918Z","requestId":"81cfa315-..."}}` | PASS |

**Notes:**
- Optimistic locking pattern hoạt động đúng theo spec FR-II-NEW-04.
- Evidence: [r7-7-1-hd-059-conflict-409-session-b.png](r7-7-1-hd-059-conflict-409-session-b.png).
- Modal session B vẫn mở sau 409, date input đánh dấu `invalid="true"` (FE catch error response, render aria-invalid). UX dynamic: có thể cần FE thêm toast cụ thể "Bản ghi đã bị cập nhật, vui lòng tải lại" thay vì chỉ aria-invalid.

---

## 5. Test Data Used

### 5.1 Tài khoản test

| Username | Role | Đơn vị | Cấp | Dùng cho TC |
|----------|------|--------|-----|-------------|
| `cb_nv_tw_04` | CB_NV | Cục Bổ trợ tư pháp | TW | HD-030, HD-049, HD-050, HD-051, HD-052, HD-059 (Session A) |
| `cb_nv_tw_05` | CB_NV | Cục Bổ trợ tư pháp | TW | HD-059 (Session B isolatedContext `hd059_session_b`) |

### 5.2 Data tạo/sử dụng trong test

| ID / Mã | Tên / Mô tả | Purpose | Cleanup? |
|---------|-------------|---------|----------|
| HD-20260509-004 | UI-R7 record TIEP_NHAN → DANG_XU_LY (linhVuc Doanh nghiệp, kênh DVC) | HD-030 + HD-049 + HD-059 | Keep — state đã chuyển DANG_XU_LY + deadline 22/05/2026 10:00, version=4 |
| `Đinh Văn Mười Bốn` (uid `4b732377-009f-418a-8186-cd98c2db4faf`) | TVV workload=0 chosen for HD-030 assign | Phân công CA_NHAN | Keep |
| 7 TC TV HOAT_DONG (TC-BTP-TW-0001..0008) | BE seed từ R7.3.1.MoB | HD-049 expected source list | Keep |

---

## 6. Environment Notes

- **API endpoint pattern:** `/api/v1/{resource-plural}` (REST + JWT cookie `access_token`)
- **Auth flow:** username/password → email OTP 6 digits → JWT cookie HttpOnly + Bearer header
- **Token TTL:** ~30 ngày (`exp` field decoded ~2026-06-09), không revoke aggressive như JWT R10 cũ
- **Frontend framework:** React + Vite + Ant Design (Modal, Segmented, DatePicker, Select)
- **Backend:** Express + PostgreSQL (verified qua `x-powered-by: Express` header)
- **Concurrency strategy:** Optimistic locking via `version` field in request body (PASS HD-059)
- **Known limitations:**
  - AntD `Segmented` a11y radio label không enable trực tiếp click MCP (cần `evaluate_script` để label.click())
  - AntD `DatePicker` cần click vào input → fill string → press Enter để chốt OR click OK button trong dropdown overlay
  - Modal Phân công section "Tổ chức tư vấn" có FE bug binding (BUG-HD-049-TC-ORG-UI-001)

---

## 7. Recommendations

### Must Fix (Before Release)

1. **BUG-HD-049-TC-ORG-UI-001 (Major):** FE binding bug nhánh TO_CHUC trong modal Phân công. Inspect React component xử lý `onChange` của `<Segmented>` — đảm bảo dispatch fetch `to-chuc-tu-vans` + bind store `toChucTuVans` thay vì giữ list `nhanSu`. Sau fix retest HD-049/050/051 cùng record HD-20260509-004 (DANG_XU_LY) hoặc seed thêm record TIEP_NHAN mới.

### Should Fix

2. **UX HD-059 conflict toast (Minor — observation):** Khi BE trả 409 ERR-STATE-LOCK-409, FE chỉ aria-invalid date input. Nên thêm AntD message/notification rõ "Bản ghi đã được cập nhật bởi user khác, vui lòng tải lại trang" để user hiểu cần reload thay vì sửa input.

### Additional Recommendations

3. **HD-052 scope decision (BA):** Cần BA quyết spec HD-052 (API negative bypass): (a) cho phép ngoại lệ API-only cho TC này, hoặc (b) UI có flow tương đương để cover. Hiện đang BLOCKED do project rule cấm API direct.
4. **Test data:** Sau fix BUG-HD-049, seed thêm 1-2 record state TIEP_NHAN linhVuc Doanh nghiệp để có pool record clean cho retest 3 TC nhánh TO_CHUC.
5. **Concurrency monitoring:** HD-059 PASS, nhưng nên thêm test concurrency cho các state transition khác (TIEP_NHAN, PHAN_CONG, GUI_DUYET) trong round sau để verify optimistic locking enforce trên toàn bộ FR-II.

---

## 8. Appendix

### A — API Endpoints Tested

| Method | Endpoint | Purpose | Tested in TC |
|--------|----------|---------|--------------|
| POST | `/api/v1/hoi-daps/{id}/phan-cong` | Phân công xử lý | HD-030 (reqid=236, 200) |
| GET | `/api/v1/hoi-daps/{id}` | Detail verify state | HD-030 (reqid=237, 200) |
| GET | `/api/v1/to-chuc-tu-vans?trangThai=HOAT_DONG&pageSize=100&page=1` | TC TV list nguồn cho modal | HD-049 (reqid=232, 200) |
| POST | `/api/v1/hoi-daps/{id}/cap-nhat-thoi-han` | Cập nhật thời hạn | HD-059 Session A (200, version 3→4); HD-059 Session B (**409 ERR-STATE-LOCK-409**) |
| GET | `/api/v1/mau-phan-hois/by-linh-vuc/{linhVucId}` | Mẫu phản hồi load sau DANG_XU_LY | HD-030 supporting (reqid=238, 200) |

### B — Screenshots

| File | Mô tả | TC Ref |
|------|-------|--------|
| [r7-7-1-hd-030-retest-dangxuly-pass.png](r7-7-1-hd-030-retest-dangxuly-pass.png) | Detail HD-004 sau Phân công, header "Đang xử lý", người phân công Đinh Văn Mười Bốn, section Soạn phản hồi xuất hiện | HD-030 |
| [r7-7-1-hd-049-retest-tc-tab-broken.png](r7-7-1-hd-049-retest-tc-tab-broken.png) | Modal Phân công sau click "Tổ chức tư vấn": segmented switched, body vẫn table cá nhân | HD-049 retest |
| [r7-7-1-hd-049-modal-viewport-tc-tab.png](r7-7-1-hd-049-modal-viewport-tc-tab.png) | First-run evidence (Phase 3b 00:44-00:47) | HD-049 first-run |
| [r7-7-1-hd-049-org-dropdown-open-viewport.png](r7-7-1-hd-049-org-dropdown-open-viewport.png) | Click Select TC TV → dropdown empty (first-run) | HD-049 / HD-050 |
| [r7-7-1-hd-059-conflict-409-session-b.png](r7-7-1-hd-059-conflict-409-session-b.png) | Session B sau submit, modal vẫn mở, date input invalid=true (BE 409 caught) | HD-059 |

### C — SRS Traceability Matrix

| SRS Reference | TC Coverage | Status |
|---------------|-------------|--------|
| FR-II-04 (Tiếp nhận) + FR-II-06 (Phân công CA_NHAN) | HD-030 | 1/1 PASS |
| FR-II-06 (Phân công TO_CHUC cấp 1 + cấp 2) | HD-049, HD-050, HD-051 | 0/3 — 1 FAIL + 2 BLOCKED — FE bug |
| FR-II-06 (Bypass TVV không thuộc TC) | HD-052 | 0/1 BLOCKED — BA decision |
| FR-II-NEW-04 (Cập nhật thời hạn + optimistic locking version) | HD-059 | 1/1 PASS |

---

## Cumulative R7.7.1 (sau Phase 3b retest)

| Phase | TC PASS | Tên |
|---|---|---|
| Phase 1 | 13 | HD-001..HD-014, HD-019 base lifecycle |
| Phase 2A | 4 | HD-013, HD-023, HD-024, HD-031 |
| Phase 2B | 7 | HD-029, HD-034, HD-035, HD-046, HD-056, HD-058, HD-063 |
| Phase 3a | 3 | HD-025, HD-026, HD-064 (permission scope BN/DP + cross-cấp) |
| **Phase 3b retest** | **2** | **HD-030, HD-059** |
| **Total** | **29** | **48% R7.7.1 coverage** |

**Defer/Block 31 TCs** (chi tiết Phase 3b cụ thể trên + Phase 3 còn lại depend R7.6.3 ⏳ Cổng PLQG endpoint).

---

*Report generated: 2026-05-10 01:30:00 UTC+7 | QA Automation via Claude Code (Opus 4.7)*
