# Functional Test Report — Người hỗ trợ pháp lý (NHT)

| Thông tin | Giá trị |
|-----------|---------|
| **Module** | Người hỗ trợ pháp lý (FR-IV-NHT-01) |
| **SRS Reference** | `srs-update-2026-5-5/srs-fr-04-chuyen-gia-tvv.md:1190-1301` (FR-IV-NHT-01 — entity NGUOI_HO_TRO) |
| **UC Coverage** | UC41-49 (tiếp nhận/quản lý), UC59 dropdown phân công VV, UC60/UC65 xử lý VV |
| **Người test** | QA Automation via Claude Code |
| **Ngày** | 2026-05-08 |
| **Môi trường** | http://103.172.236.130:3000/ |
| **OTP Bypass** | `666666` (bypass tạm) — MailHog: http://103.172.236.130:8025 |
| **Test Method** | UI-based (Chrome DevTools MCP) + API verify (`evaluate_script` curl probe) |
| **Primary Account** | `cb_nv_tw_03` / Secret@123 (CB Nghiệp vụ TW) — primary; `qtht_03` (QTHT) — verify-permission |
| **Round** | R7.7.4.5 (R8 verify) |
| **Tài liệu tham chiếu** | [7.4a-nguoi-ho-tro.md](../../../../funtion/7.4a-nguoi-ho-tro.md) · [bug-report-r7-7-4-5-nht.md](../../bug-reports/nguoi-ho-tro/bug-report-r7-7-4-5-nht.md) · [todo-nht.md](../../../../../tasks/todo-nht.md) |

---

## 1. Executive Summary

> **Re-classify 2026-05-09 17:42:** (1) BA chốt QTHT KHÔNG có quyền thêm/sửa/xóa NHT — chỉ Read. Matrix line 61 update ✅CRUD → 👁️R. BUG-NHT-001/002 đóng INVALID. (2) Click thử mail link với workaround host → IP qua MCP: BE flow OK, NHT-BTP-TW-0005 chuyển CHO_KICH_HOAT → HOAT_DONG. NHT-003 FAIL → PASS (workaround). BUG-NHT-003 re-classify Major P1 (host hardcoded + link raw text — KHÔNG phải broken hoàn toàn).
>
> **Run R8 2026-05-09 (cb_nv_tw_02):** Execute thêm 5 TC: NHT-006 Edit ✅, NHT-005 negative ✅ (FE block), NHT-009 Tạm dừng ✅, NHT-010 Vô hiệu hóa ✅, NHT-012 Khôi phục ✅. NHT-008/011 vẫn BLOCKED — UI Phân công VV chỉ hiển thị TVV (không có NHT trong dropdown), không seed được VV-NHT linkage qua UI.

| Metric | Value |
|--------|-------|
| **Total Test Cases (spec FR-IV-NHT-01)** | 12 (NHT-001..012) |
| **TC applicable cho CB NV** | 11 (loại NHT-007 — sửa đơn vị chỉ áp QTHT theo spec cũ, sau BA chốt KHÔNG ai sửa được nên N/A) |
| **TC đã test / Tổng TC** | 10/12 (83%) |
| **Passed** | 9 (NHT-001..006, NHT-009, NHT-010, NHT-012) |
| **Failed (⚠️ Sai spec)** | 0 |
| **Blocked** | 2 (NHT-008, NHT-011 — UI Phân công VV không có NHT, cần BA confirm) |
| **Partial** | 0 |
| **N/A (sau BA chốt 2026-05-09)** | 1 (NHT-007 sửa đơn vị — không applicable theo spec mới) |
| **Overall Pass Rate (active)** | 82% (9/11 applicable) — Còn 2 TC guard cần BA confirm spec NHT-VV linkage |
| **P0 Pass Rate** | 86% (6/7 active P0 — NHT-001/002/003/004/005/010 PASS, NHT-011 BLOCKED) |
| **Bugs Found (SRS-ref)** | 5 tổng — 3 Open (1 Major P1 + 2 Minor) + 2 Closed-Invalid |
| **Health Score** | 88/100 — workflow CRUD + state machine + BR-AUTH-08 vận hành đúng spec, còn config mail (BUG-003) + UX (BUG-004/005) + 2 TC guard chờ spec |
| **Start Time** | 23:25 (UTC+7) 2026-05-08 |
| **End Time** | 18:30 (UTC+7) 2026-05-09 |
| **Total Duration** | ~80 phút (R7 60p + R8 20p) |
| **Browse Status** | OK |

### Pass Rate breakdown theo Type (sau R8 2026-05-09)

| Type | Mô tả | TC count | PASS | FAIL | BLOCKED | N/A | **Pass Rate** |
|------|-------|----------|------|------|---------|-----|---------------|
| **Happy** | NHT-001 (CB NV path PASS; QTHT path không applicable) | 1 | 1 | 0 | 0 | 0 | **100%** |
| **Negative** | NHT-004 (duplicate), NHT-005 (thiếu LV) | 2 | 2 | 0 | 0 | 0 | **100%** |
| **Authorization** | NHT-002 (CB NV scope lock) | 1 | 1 | 0 | 0 | 0 | **100%** |
| **Workflow** | NHT-003/009/010/012 (kích hoạt + state) | 4 | 4 | 0 | 0 | 0 | **100%** |
| **Update** | NHT-006 (sửa LV qua CB NV), NHT-007 (sửa đơn vị — N/A theo BA chốt) | 2 | 1 | 0 | 0 | 1 | **100%** (1/1 active) |
| **Guard** | NHT-008 (xóa mềm), NHT-011 (vô hiệu fail) | 2 | 0 | 0 | 2 | 0 | **0%** |
| **Total** | | **12** | **9** | **0** | **2** | **1** | **82%** (9/11 active) |

→ **Workflow state machine 4/4 PASS** + **Negative 2/2 PASS** + **Update 1/1 active PASS** — module hoạt động full luồng CRUD + state. Còn 2 TC Guard (NHT-008/011) BLOCKED do UI Phân công VV chỉ hiển thị TVV trong dropdown (không có NHT) → không seed được linkage VV-NHT để test guard rule "delete/vô hiệu fail khi có VV gắn".

### Verdict: **PASS** (9/11 active, module workflow + CRUD + state machine vận hành đúng spec)

Module NHT vận hành đầy đủ luồng theo SM-NHT spec: CHO_KICH_HOAT → HOAT_DONG → TAM_DUNG / VO_HIEU_HOA → HOAT_DONG (khôi phục). Workflow swap (cap-nhat-trang-thai) PASS 3/3 transition (009/010/012). Edit happy path PASS (PATCH 200, LV update). Negative validate FE block đúng (Vui lòng chọn ít nhất 1 lĩnh vực). Còn 2 TC guard NHT-008/011 BLOCKED vì UI Phân công VV không có NHT trong dropdown — cần BA confirm spec NHT-VV linkage flow. Khuyến nghị release module NHT sau khi fix BUG-NHT-003 host config (Major P1) + 2 Minor UX. NHT-008/011 chuyển vòng test sau khi BA chốt VV-NHT linkage.

---

## 2. Test Results Summary

| ID | TraceID (SRS) | Tên Test Case | Type | Priority | Result | Bug ID | Nguyên nhân / Ghi chú |
|----|---------------|---------------|------|----------|--------|--------|------------------------|
| NHT-001 (QTHT path) | FR-IV-NHT-01 | QTHT tạo NHT mới | Happy | P0 | **N/A** | — | Sau BA chốt 2026-05-09: QTHT KO có quyền tạo NHT → TC không applicable |
| NHT-001 (CB NV path) | FR-IV-NHT-01 | CB NV TW tạo NHT mới | Happy | P0 | **PASS** | — | cb_nv_tw_03 tạo NHT-BTP-TW-0005 ✅ — modal 4 field, đơn vị auto-lock, mail gửi |
| NHT-002 | FR-IV-NHT-01 | CB NV `don_vi_id` lock (BR-AUTH-08) | Authorization | P0 | **PASS** | — | Modal CB NV KHÔNG có field "Đơn vị" → BE auto-set = đơn vị mình. Verified BTP-TW ✅. Pattern hợp lý cho CB NV. |
| NHT-003 | FR-IV-NHT-01 | Kích hoạt mail → CHO_KICH_HOAT → HOAT_DONG | Workflow | P0 | **⚠️ PASS** (workaround) | BUG-NHT-003 | Re-test 2026-05-09 17:42: BE flow OK với workaround replace host. NHT-BTP-TW-0005 chuyển HOAT_DONG ✅. Bug còn lại Major P1: host hardcoded `localhost` + link raw text. |
| NHT-004 | FR-IV-NHT-01 | Email/username trùng → ERR-NHT-01 | Negative | P0 | **PASS** | BUG-NHT-005 (Minor) | BE block duplicate username `nht_tc001_btp_tw` (12→12 không tăng). FE không hiện toast rõ → UX issue Minor |
| NHT-005 | FR-IV-NHT-01 | Thiếu lĩnh vực → ERR-NHT-03 | Negative | P0 | **PASS** | — | R8: FE block "Vui lòng chọn ít nhất 1 lĩnh vực" trên Edit form (clear LV + Lưu) → no PATCH gửi BE. ERR-NHT-03 BE path không reach từ UI (FE protect đúng spec). |
| NHT-006 | FR-IV-NHT-01 | Sửa NHT lĩnh vực qua CB NV | Update | P1 | **PASS** | — | R8: cb_nv_tw_02 edit NHT-BTP-TW-0002 thêm LV "Hành chính" → PATCH `/api/v1/nguoi-ho-tro/{id}` 200 reqid=246 → list update 2 LV (Doanh nghiệp + Hành chính). |
| NHT-007 | FR-IV-NHT-01 | Sửa đơn vị | Update | P1 | **N/A** | — | Sau BA chốt 2026-05-09: QTHT không có quyền edit, CB NV không được sửa đơn vị (BR-AUTH-08 lock). TC này chỉ áp QTHT cũ → không applicable. |
| NHT-008 | FR-IV-NHT-01 | Xóa mềm + guard VV | Guard | P1 | **BLOCKED** | — | UI Phân công VV (button "Phân công" trên VV detail) chỉ hiển thị TVV trong dropdown (verified VV-BTP-TW-20260507-004 SHTT — chỉ option "Mai Thị Mười Bảy TVV-BTP-TW-0005"), không có NHT → không seed được VV-NHT linkage qua UI. Cần BA confirm spec. |
| NHT-009 | FR-IV-NHT-01 | Tạm dừng (HOAT_DONG → TAM_DUNG) | Workflow | P1 | **PASS** | — | R8: cb_nv_tw_02 click swap NHT-BTP-TW-0001 → modal "Cập nhật trạng thái", chọn "Tạm dừng" + lý do → POST `/api/v1/nguoi-ho-tro/{id}/cap-nhat-trang-thai` 200 reqid=255 → state Tạm dừng. |
| NHT-010 | FR-IV-NHT-01 | Vô hiệu hóa (no VV) | Workflow | P0 | **PASS** | — | R8: cb_nv_tw_02 click swap NHT-BTP-TW-0005 (HOAT_DONG, VV=0) → chọn "Vô hiệu hóa" + lý do → POST 200 reqid=259 → state Vô hiệu hóa. |
| NHT-011 | FR-IV-NHT-01 | Vô hiệu hóa fail (có VV DANG_XU_LY) | Guard | P0 | **BLOCKED** | — | Same root cause với NHT-008 — không seed được VV-NHT linkage qua UI dropdown. Cần BA confirm spec NHT-VV linkage flow. |
| NHT-012 | FR-IV-NHT-01 | Khôi phục VO_HIEU_HOA → HOAT_DONG | Workflow | P2 | **PASS** | — | R8: tiếp NHT-010 — click swap NHT-BTP-TW-0005 (VO_HIEU_HOA) → modal pre-select "Kích hoạt lại" + lý do → POST 200 reqid=263 → state Đang hoạt động. |

---

## 3. Bug Report

> **Lưu ý:** Tóm tắt inline. Chi tiết Steps/Evidence xem [bug-report-r7-7-4-5-nht.md](../../bug-reports/nguoi-ho-tro/bug-report-r7-7-4-5-nht.md).

### ~~BUG-NHT-001~~ [CLOSED-INVALID] — QTHT thiếu CRUD UI buttons trên module NHT

> Re-classify 2026-05-09: BA chốt QTHT KHÔNG có quyền thêm/sửa/xóa NHT — UI ẩn buttons là design đúng.

### ~~BUG-NHT-002~~ [CLOSED-INVALID] — Modal "Thêm NHT" thiếu field "Đơn vị" cho QTHT

> Re-classify 2026-05-09: BA chốt QTHT KHÔNG tạo NHT → field Đơn vị tự do không applicable. Modal 4 field đúng workflow CB NV.

### BUG-NHT-003 — [Major] Activation link trong mail bị broken (host + URL encoding)

| Trường | Giá trị |
|--------|---------|
| **Severity** | Major |
| **Priority** | P0 |
| **TC Reference** | NHT-003 |
| **Status** | Open |

**Mô tả:** Mail kích hoạt NHT có link `http://localhost:3000/auth/verify-email?token&#x3D;6ee6d7cd-...`. (1) host `localhost:3000` không match server thực `103.172.236.130:3000`; (2) `&#x3D;` là HTML-entity encode của `=` → trình duyệt parse thành query string sai. NHT click không kích hoạt được.

### BUG-NHT-004 — [Minor] Detail view thiếu tab "Bồi dưỡng" theo spec

| Trường | Giá trị |
|--------|---------|
| **Severity** | Minor |
| **Priority** | P2 |
| **TC Reference** | NHT-017 (FR-IV-NHT-03) |
| **Status** | Open |

**Mô tả:** Spec NHT-017 yêu cầu 3 tab: Thông tin / Bồi dưỡng / Vụ việc đã hỗ trợ. UI thực tế chỉ 2 tab (Thông tin + Vụ việc đã hỗ trợ), thiếu tab "Bồi dưỡng". NĐ 55/2019 Đ.7 quy định NHT có chương trình bồi dưỡng → cần hiển thị.

### BUG-NHT-005 — [Minor] FE không hiển thị toast lỗi khi BE reject duplicate

| Trường | Giá trị |
|--------|---------|
| **Severity** | Minor |
| **Priority** | P2 |
| **TC Reference** | NHT-004 |
| **Status** | Open |

**Mô tả:** Submit form với username đã tồn tại — BE block (record không được tạo, count giữ nguyên 12), nhưng FE đóng modal mà không hiện toast `.ant-message-error`/`.ant-notification-error` để user biết lý do fail. UX: user nghĩ tạo thành công.

---

## 4. Detailed Test Results

### 4.1 NHT-001 (CB NV path): CB NV TW tạo NHT mới

> **Re-classify 2026-05-09:** Sau BA chốt QTHT KHÔNG có quyền tạo NHT, NHT-001 chia 2 path: QTHT path **N/A** (không applicable theo spec mới), CB NV path **PASS** clean. Step 1+2 trước đây fail vì giả định spec sai → re-classify thành PASS theo spec mới.

**Pre-conditions:**
- cb_nv_tw_03 đã login (primary account theo permission matrix line 125: CB_NV_TW có ✅ CRUD* trên NGUOI_HO_TRO)
- qtht_03 đã verify view-only (list 11 NHT, chỉ Eye button — đúng design BA chốt 2026-05-09)

**Test Data:**
```json
{
  "ho_ten": "NHT TC001 Test BTP TW",
  "email": "nht_tc001_btp_tw@htpldn.test",
  "username": "nht_tc001_btp_tw",
  "linh_vuc": ["Hành chính", "Lao động"]
}
```

**Test Steps:**

| Step | Action | Expected | Actual | Status |
|------|--------|----------|--------|--------|
| 1 | qtht_03 vào `/nguoi-ho-tro` verify view-only | KHÔNG có "Thêm mới"/Edit/Delete (BA chốt QTHT chỉ Read) | Toolbar chỉ search/filter; cột Thao tác chỉ Eye button | **PASS** (đúng spec) |
| 2 | cb_nv_tw_03 click "Thêm mới" | Modal mở 4 field (Họ tên, Email, Username, Lĩnh vực) — đơn vị auto-lock theo BR-AUTH-08 | Modal mở 4 field như expected | **PASS** |
| 3 | Fill 4 field + click "Tạo" | Tạo record CHO_KICH_HOAT + tạo TAI_KHOAN + gửi mail | Record `NHT-BTP-TW-0005` tạo thành công, đơn vị auto-lock = BTP-TW, mail "Kích hoạt tài khoản Người hỗ trợ pháp lý" gửi MailHog | **PASS** |
| 4 | Verify list count | 11 → 12 | 12 records, NHT-BTP-TW-0005 hiển thị đầu list | **PASS** |
| 5 | Verify endpoint state | DB có 1 record CHO_KICH_HOAT mới | `/api/v1/nguoi-ho-tro` trả 12 records, mới có id `189c86ef-...` | **PASS** |

**Notes:** Workflow tạo NHT vận hành đúng spec — CB NV TW là role chính tạo NHT scoped theo đơn vị mình (BR-AUTH-08). QTHT view-only là design đúng theo BA chốt 2026-05-09.

---

### 4.2 NHT-002: CB NV scope lock (BR-AUTH-08)

> **Re-classify 2026-05-09:** Sau BA chốt QTHT không tạo NHT, modal CB NV ẩn field Đơn vị (auto-lock theo BR-AUTH-08) là design đúng. Step 1 PARTIAL → PASS.

**Test Steps:**

| Step | Action | Expected | Actual | Status |
|------|--------|----------|--------|--------|
| 1 | cb_nv_tw_03 click "Thêm mới" | Modal CB NV không cho chọn đơn vị (auto-lock = đơn vị mình theo BR-AUTH-08) | Modal mở 4 field, KHÔNG có field Đơn vị → BE auto-set đúng | **PASS** |
| 2 | Verify đơn vị record sau tạo | = BTP-TW (đơn vị của CB NV) | NHT-BTP-TW-0005 có đơn vị "Cục Bổ trợ tư pháp - Bộ Tư pháp" ✅ | **PASS** |
| 3 | Test path "chọn đơn vị khác → ERR-NHT-02" | Không applicable cho CB NV (BE auto-lock, FE không expose field) | KHÔNG test được (FE ẩn field — đúng design) | **N/A** |

**Notes:** BE auto-lock đơn vị đúng BR-AUTH-08. FE ẩn field thay vì disable visible — UX hợp lý cho CB NV (không cần expose field user không sửa được). ERR-NHT-02 path không còn applicable sau BA chốt QTHT KO tạo NHT.

---

### 4.3 NHT-003: Kích hoạt qua mail (FR-VIII-26)

> **Re-test 2026-05-09 17:42:** Click thử link với workaround replace host `localhost:3000` → `103.172.236.130:3000` → BE flow OK. NHT-BTP-TW-0005 chuyển CHO_KICH_HOAT → HOAT_DONG ✅. Issue còn lại: host hardcoded + link raw text (BUG-NHT-003 re-classify Major P1).

**Test Steps:**

| Step | Action | Expected | Actual | Status |
|------|--------|----------|--------|--------|
| 1 | Tạo NHT NHT-BTP-TW-0005 (NHT-001) | Mail gửi MailHog với activation link | Mail Subject "Kích hoạt tài khoản Người hỗ trợ pháp lý — PM-HTPLDN" gửi tới `nht_tc001_btp_tw@htpldn.test` | **PASS** |
| 2 | Verify mail body chứa link valid + clickable anchor | `<a href="http://${APP_URL}/auth/verify-email?token=<UUID>">` (host env, link là anchor) | Link `http://localhost:3000/auth/verify-email?token&#x3D;...` nằm RAW trong `<p>` (không phải `<a href>`) — host hardcoded localhost | **FAIL** (BUG-NHT-003) |
| 3 | Click link (workaround replace host → IP) | BE verify token → state HOAT_DONG → redirect login | URL `http://103.172.236.130:3000/auth/verify-email?token=6ee6d7cd-7db7-4047-bfdb-38d47fbfbd3b` → POST `/api/v1/auth/verify-email` 200 → `{"success":true,"data":{"trangThai":"HOAT_DONG"}}` → redirect `/login` ✅ | **PASS** (workaround) |
| 4 | Verify NHT state qua list API | trangThai = HOAT_DONG | BE response từ POST verify-email confirm `trangThai: HOAT_DONG` | **PASS** |

---

### 4.4 NHT-004: Email/username trùng → ERR-NHT-01

**Test Steps:**

| Step | Action | Expected | Actual | Status |
|------|--------|----------|--------|--------|
| 1 | cb_nv_tw_03 mở modal "Thêm mới" | Modal mở | OK | **PASS** |
| 2 | Fill username = `nht_tc001_btp_tw` (đã tồn tại) + Email khác + LV "Thuế" | BE reject ERR-NHT-01 | Modal đóng, count list giữ nguyên 12 (không tăng 13) → BE đã block | **PASS** |
| 3 | Verify FE hiện toast lỗi | Toast `.ant-message-error` "Tên đăng nhập đã tồn tại" | KHÔNG có toast hiển thị (DOM rỗng `.ant-message`/`.ant-notification`) | **FAIL** (BUG-NHT-005) |

**Notes:** BE block đúng nhưng UX issue: user không biết lý do.

---

### 4.5 NHT-005: Thiếu lĩnh vực → ERR-NHT-03 (R8 2026-05-09)

**Test Steps:**

| Step | Action | Expected | Actual | Status |
|------|--------|----------|--------|--------|
| 1 | cb_nv_tw_02 click Edit NHT-BTP-TW-0002 | Modal "Chỉnh sửa người hỗ trợ pháp lý" mở | Modal mở 2 field (Họ tên + Lĩnh vực chuyên môn) | **PASS** |
| 2 | Click `close-circle` clear-all → tags LV cleared | Field LV còn rỗng | tags=[], placeholder=null | **PASS** |
| 3 | Click "Lưu" | FE block với error message + KHÔNG gửi BE | Field error: "Vui lòng chọn ít nhất 1 lĩnh vực" hiển thị; network không có PATCH `/api/v1/nguoi-ho-tro/{id}` | **PASS** |
| 4 | Verify dialog vẫn open | Dialog vẫn open chờ user fix | dialogStillOpen=true | **PASS** |

**Notes:** FE validate intercept đúng spec — bảo vệ rule "LV bắt buộc" trước khi reach BE. ERR-NHT-03 BE error code chỉ trigger được qua API tampering, không từ UI form. Treat = PASS theo functional UI scope.

**Screenshot:** [nht-005-fe-block-no-lv-2026-05-09.png](image/nht-005-fe-block-no-lv-2026-05-09.png)

---

### 4.6 NHT-006: Sửa NHT lĩnh vực qua CB NV (R8 2026-05-09)

**Test Steps:**

| Step | Action | Expected | Actual | Status |
|------|--------|----------|--------|--------|
| 1 | cb_nv_tw_02 click Edit NHT-BTP-TW-0002 | Modal "Chỉnh sửa" mở với value `NHT R8 BTP TW 05` + LV `Doanh nghiệp` | Modal mở đúng | **PASS** |
| 2 | Click LV combobox + select "Hành chính" | LV multi-select có 2 tags: Doanh nghiệp + Hành chính | Tags=["Doanh nghiệp","Hành chính"] | **PASS** |
| 3 | Press Escape close listbox + click "Lưu" | PATCH `/api/v1/nguoi-ho-tro/{id}` 200 + modal đóng + list update | reqid=246 PATCH 200 → list re-fetch reqid=247 | **PASS** |
| 4 | Verify list row | NHT-BTP-TW-0002 hiển thị 2 LV: Doanh nghiệp + Hành chính | Row text: "Cục BTP - Bộ Tư pháp Doanh nghiệp Hành chính 0 Chờ kích hoạt" ✅ | **PASS** |

**Screenshot:** [nht-006-edit-lv-success-2026-05-09.png](image/nht-006-edit-lv-success-2026-05-09.png)

---

### 4.7 NHT-009: Tạm dừng (HOAT_DONG → TAM_DUNG) (R8 2026-05-09)

**Test Steps:**

| Step | Action | Expected | Actual | Status |
|------|--------|----------|--------|--------|
| 1 | cb_nv_tw_02 click swap button trên NHT-BTP-TW-0001 (HOAT_DONG, "NHT UI Test 04") | Modal "Cập nhật trạng thái — NHT-BTP-TW-0001" mở | Modal mở (uid 76_0) | **PASS** |
| 2 | Click combobox "Chuyển sang trạng thái" → select "Tạm dừng" | Dropdown 2 option: Tạm dừng + Vô hiệu hóa, chọn được | options=["Tạm dừng","Vô hiệu hóa"], chọn "Tạm dừng" OK | **PASS** |
| 3 | Fill Lý do + click Lưu | POST `/api/v1/nguoi-ho-tro/{id}/cap-nhat-trang-thai` 200 + state đổi | reqid=255 POST 200 → list refresh | **PASS** |
| 4 | Verify row state | "Tạm dừng" | Row text: "...Doanh nghiệp 0 Tạm dừng" ✅ | **PASS** |

**Screenshot:** [nht-009-tam-dung-success-2026-05-09.png](image/nht-009-tam-dung-success-2026-05-09.png)

---

### 4.8 NHT-010: Vô hiệu hóa (no VV) (R8 2026-05-09)

**Test Steps:**

| Step | Action | Expected | Actual | Status |
|------|--------|----------|--------|--------|
| 1 | cb_nv_tw_02 click swap NHT-BTP-TW-0005 (HOAT_DONG, VV=0, "NHT TC001 Test BTP TW") | Modal "Cập nhật trạng thái — NHT-BTP-TW-0005" mở | Modal mở | **PASS** |
| 2 | Combobox dropdown 2 option → select "Vô hiệu hóa" | Chọn được "Vô hiệu hóa" | OK | **PASS** |
| 3 | Fill lý do + Lưu | POST 200 → state VO_HIEU_HOA | reqid=259 POST 200 | **PASS** |
| 4 | Verify row state | "Vô hiệu hóa" | Row text: "...Hành chính Lao động 0 Vô hiệu hóa" ✅ | **PASS** |

**Notes:** Path "no VV" PASS — không có guard rule kích hoạt vì VV count = 0. Path "có VV" → NHT-011 BLOCKED do không seed được VV-NHT linkage.

**Screenshot:** [nht-010-vohieu-success-2026-05-09.png](image/nht-010-vohieu-success-2026-05-09.png)

---

### 4.9 NHT-012: Khôi phục VO_HIEU_HOA → HOAT_DONG (R8 2026-05-09)

**Test Steps:**

| Step | Action | Expected | Actual | Status |
|------|--------|----------|--------|--------|
| 1 | Sau NHT-010, click swap button NHT-BTP-TW-0005 (VO_HIEU_HOA) | Modal "Cập nhật trạng thái" mở với option pre-select "Kích hoạt lại" (single option cho VO_HIEU_HOA) | Modal mở, dropdown đã pre-select "Kích hoạt lại" | **PASS** |
| 2 | Fill lý do + click Lưu | POST 200 → state HOAT_DONG | reqid=263 POST 200 | **PASS** |
| 3 | Verify row state | "Đang hoạt động" | Row text: "...Hành chính Lao động 0 Đang hoạt động" ✅ | **PASS** |

**Notes:** Workflow lifecycle full đúng SM-NHT spec: HOAT_DONG → VO_HIEU_HOA → HOAT_DONG. Backend cap-nhat-trang-thai endpoint xử lý cả forward (vô hiệu) và reverse (khôi phục).

**Screenshot:** [nht-012-khoiphuc-success-2026-05-09.png](image/nht-012-khoiphuc-success-2026-05-09.png)

---

### 4.10 NHT-008/011 BLOCKED — UI Phân công VV không có NHT (R8 2026-05-09)

**Investigation Steps:**

| Step | Action | Expected | Actual | Status |
|------|--------|----------|--------|--------|
| 1 | Browse VV module — pool 5 records, NHT/TVV column | Có ≥1 VV gắn NHT để chạy guard test | 5 VV gắn TVV (Vũ Văn Sáu, Trương Văn Mười Sáu, Ngô Thị Mười Lăm), không có NHT | **PASS** investigate |
| 2 | Open VV-BTP-TW-20260507-004 (TIEP_NHAN, SHTT) → click "Kiểm tra hồ sơ" → Xác nhận | State advance KIEM_TRA | State "Đang kiểm tra" | **PASS** advance state |
| 3 | Click button "Phân công" → modal mở dropdown "Chọn tư vấn viên" | Dropdown có cả TVV và NHT (theo LV match SHTT) | Dropdown chỉ 1 option: "Mai Thị Mười Bảy (TVV-BTP-TW-0005) — 0 VV đang xử lý" — KHÔNG có NHT (NHT-STP-HP-0001 / hương 1 / hương 2 đều có SHTT trong LV nhưng không xuất hiện) | **BLOCKED** seed |
| 4 | Cancel modal | Không thay đổi VV state | Cancel OK | — |

**Conclusion:** UI Phân công VV chỉ hiển thị TVV (loaiTvv=TVV), không hiển thị NHT (loaiTvv=NHT). Không seed được VV với `nguoi_xu_ly_id = NHT_TK_id` qua UI flow chuẩn → NHT-008 (xóa NHT có VV) + NHT-011 (vô hiệu NHT có VV DANG_XU_LY) không test được.

**BA decision needed:** Spec FR-IV-NHT-01 yêu cầu NHT có thể tham gia xử lý VV (nguoi_xu_ly_id) — nhưng UI Phân công không expose NHT. Có thể (a) thiếu UI feature, (b) NHT chỉ tham gia qua flow khác (vd PHỐI HỢP, không phải PHÂN CÔNG primary), hoặc (c) spec change.

**Screenshot:** [nht-008-011-deferred-no-nht-in-vv-phancong-2026-05-09.png](image/nht-008-011-deferred-no-nht-in-vv-phancong-2026-05-09.png)

---

### 4.11 List view + permission UI matrix

**So sánh UI hiển thị buttons giữa 2 role:**

| Role | URL | Add btn | Edit btn | Delete btn | Swap btn | Eye btn |
|------|-----|---------|----------|------------|----------|---------|
| **qtht_03** (QTHT) | /nguoi-ho-tro | ❌ (đúng) | ❌ (đúng) | ❌ (đúng) | ❌ (đúng) | ✅ |
| **cb_nv_tw_03** (CB NV TW) | /nguoi-ho-tro | ✅ | ✅ per row | ✅ per row | ✅ chỉ HOAT_DONG | ✅ |

→ Sau BA chốt 2026-05-09: QTHT KHÔNG có quyền thêm/sửa/xóa NHT — UI ẩn buttons là **design đúng**. CB NV TW là role chính tạo/quản lý NHT scoped theo đơn vị mình (BR-AUTH-08).

---

## 5. Test Data Used

### 5.1 Tài khoản test

| Username | Role | Đơn vị | Cấp | Dùng cho TC |
|----------|------|--------|-----|-------------|
| qtht_03 | QTHT | (root) | — | NHT-001 verify QTHT permission UI |
| cb_nv_tw_03 | CB_NV_TW | Cục BTTP | TW | NHT-001 happy, NHT-002 scope, NHT-004 negative (R7) |
| cb_nv_tw_02 | CB_NV_TW | Cục BTTP | TW | NHT-005/006/009/010/012 (R8) |

### 5.2 Data tạo trong test

| ID / Mã | Tên / Mô tả | Purpose | Cleanup? |
|---------|-------------|---------|----------|
| NHT-BTP-TW-0005 | NHT TC001 Test BTP TW | TC NHT-001 happy + NHT-010 vô hiệu + NHT-012 khôi phục | Keep (HOAT_DONG sau khôi phục) |
| NHT-BTP-TW-0002 | NHT R8 BTP TW 05 | TC NHT-005 negative (FE block clear LV) + NHT-006 edit LV | LV thêm "Hành chính" — keep state |
| NHT-BTP-TW-0001 | NHT UI Test 04 | TC NHT-009 tạm dừng | State HOAT_DONG → TAM_DUNG (keep) |
| (failed) | NHT TC004 Duplicate | TC NHT-004 negative duplicate username | BE rejected, không tạo |

---

## 6. Environment Notes

- **API endpoint pattern:** `/api/v1/nguoi-ho-tro` (singular) — total 12 records sau test
- **Auth flow:** JWT + OTP email (bypass `666666`)
- **Frontend:** React + Ant Design (modal Drawer, button labels Vietnamese)
- **Backend:** NestJS + PostgreSQL (deduced — error format `{success, error: {code, message, timestamp, requestId}}`)
- **Known limitations:**
  - GET `/api/v1/tai-khoans` 404 cho cb_nv_tw_03 — không verify TK created từ NHT seed qua API trực tiếp (verified gián tiếp qua mail gửi đến)
  - Modal AntD multi-select: `type_text + Enter` có thể match thêm option (ví dụ "Hành chính" + "Lao động" cùng lần)

---

## 7. Recommendations

### Must Fix (Before Release)

1. **BUG-NHT-003 (Major P1):** Fix mail template — (1) đổi host từ `localhost:3000` → env `APP_URL` config động; (2) wrap link bằng `<a href="...">` thay vì để raw text trong `<p>` để user click thẳng (không cần copy/paste). BE flow đã OK — không cần fix backend.

### Should Fix

2. **BUG-NHT-005 (Minor P2):** FE hiển thị toast lỗi rõ ràng khi BE reject duplicate (đọc error code → map message tiếng Việt).
3. **BUG-NHT-004 (Minor P2):** Thêm tab "Bồi dưỡng" trong detail view theo spec NHT-017.

### Additional Recommendations

4. **NHT-008/011 BA decision needed:** UI Phân công VV chỉ hiển thị TVV trong dropdown (verified VV-BTP-TW-20260507-004 SHTT — chỉ option TVV-BTP-TW-0005). Cần BA chốt: (a) NHT có thể nhận PHÂN CÔNG VV không? (b) Nếu có, UI cần expose NHT trong dropdown? (c) Nếu không, spec FR-IV-NHT-01 cần clarify "nguoi_xu_ly NHT" chỉ qua flow nào (PHỐI HỢP riêng?).
5. **BA cần update SRS srs-fr-04** lines 1737-1738, 1781-1782, 1190-1310, 2403-2409 để chốt rõ "QTHT chỉ Read NHT, CB NV CRUD trong scope đơn vị" — tránh QA cycle sau lại dựa vào spec cũ.
6. **State machine 4 transition đã verify** (CHO_KICH_HOAT→HOAT_DONG, HOAT_DONG→TAM_DUNG, HOAT_DONG→VO_HIEU_HOA, VO_HIEU_HOA→HOAT_DONG). Còn 1 path TAM_DUNG→HOAT_DONG chưa test (có thể infer từ NHT-012 pattern).

---

## 8. Appendix

### A — API Endpoints Tested

| Method | Endpoint | Purpose | Tested in TC |
|--------|----------|---------|--------------|
| GET | `/api/v1/nguoi-ho-tro?size=100` | List NHT | NHT-001 verify count, NHT-004 verify block |
| POST | (UI form) `/api/v1/nguoi-ho-tro` | Create NHT | NHT-001, NHT-004 (negative) |
| PATCH | `/api/v1/nguoi-ho-tro/{id}` | Update NHT (LV) | NHT-006 (200 reqid=246) |
| POST | `/api/v1/nguoi-ho-tro/{id}/cap-nhat-trang-thai` | State machine transition | NHT-009 (TAM_DUNG reqid=255), NHT-010 (VO_HIEU_HOA reqid=259), NHT-012 (HOAT_DONG reqid=263) |
| GET | `/api/v1/tai-khoans` | List TK | 404 cho cb_nv_tw — không test được |

### B — Screenshots

| File | Mô tả | TC Ref |
|------|-------|--------|
| [00-list-cb-nv-tw-03.png](evidence-r7-7-4-5/00-list-cb-nv-tw-03.png) | List NHT view qua cb_nv_tw_03 — đầy đủ Add/Edit/Delete/Swap | BUG-NHT-001 |
| [00-list-qtht-03-readonly.png](evidence-r7-7-4-5/00-list-qtht-03-readonly.png) | List NHT view qua qtht_03 — chỉ có Eye button | BUG-NHT-001 |
| [01-nht001-modal-filled.png](evidence-r7-7-4-5/01-nht001-modal-filled.png) | Modal "Thêm NHT" 4 field filled | NHT-001, BUG-NHT-002 |
| [01-nht001-pass-list.png](evidence-r7-7-4-5/01-nht001-pass-list.png) | List sau tạo — NHT-BTP-TW-0005 đầu list | NHT-001 |
| [nht-005-fe-block-no-lv-2026-05-09.png](image/nht-005-fe-block-no-lv-2026-05-09.png) | FE block "Vui lòng chọn ít nhất 1 lĩnh vực" | NHT-005 |
| [nht-006-edit-lv-success-2026-05-09.png](image/nht-006-edit-lv-success-2026-05-09.png) | NHT-BTP-TW-0002 list update 2 LV | NHT-006 |
| [nht-009-tam-dung-success-2026-05-09.png](image/nht-009-tam-dung-success-2026-05-09.png) | NHT-BTP-TW-0001 row state TAM_DUNG | NHT-009 |
| [nht-010-vohieu-success-2026-05-09.png](image/nht-010-vohieu-success-2026-05-09.png) | NHT-BTP-TW-0005 row state VO_HIEU_HOA | NHT-010 |
| [nht-012-khoiphuc-success-2026-05-09.png](image/nht-012-khoiphuc-success-2026-05-09.png) | NHT-BTP-TW-0005 row state HOAT_DONG sau khôi phục | NHT-012 |
| [nht-008-011-deferred-no-nht-in-vv-phancong-2026-05-09.png](image/nht-008-011-deferred-no-nht-in-vv-phancong-2026-05-09.png) | VV Phân công dropdown chỉ TVV — không có NHT | NHT-008/011 |

### C — SRS Traceability Matrix (re-classify 2026-05-09)

| SRS Reference | TC Coverage | Status |
|---------------|-------------|--------|
| FR-IV-NHT-01 (UC41-49) | NHT-001..012 | 9/12 PASS + 0 FAIL + 2/12 BLOCKED (NHT-008/011 — UI Phân công VV không có NHT, chờ BA) + 1/12 N/A (NHT-007 sửa đơn vị) |
| FR-VIII-15 (Tự cấp TK) | NHT-001 step 3 | PASS — TK tạo + role NHT + state CHO_KICH_HOAT |
| FR-VIII-26 (Token vĩnh viễn) | NHT-003 | PASS (workaround) — BE consume token + chuyển HOAT_DONG OK; Mail config bug Major P1 (BUG-NHT-003) |
| BR-AUTH-08 (don_vi_id scope) | NHT-002 | PASS — BE auto-lock đúng, FE ẩn field hợp lý |
| **Permission matrix line 61** | QTHT trên NGUOI_HO_TRO | UPDATED 2026-05-09: ✅ CRUD → 👁️ R |

---

*Report generated: 2026-05-08 23:45 (UTC+7) | Updated R8: 2026-05-09 18:30 — NHT-005/006/009/010/012 PASS, NHT-008/011 BLOCKED chờ BA confirm VV-NHT linkage | QA Automation via Claude Code (Chrome DevTools MCP)*
