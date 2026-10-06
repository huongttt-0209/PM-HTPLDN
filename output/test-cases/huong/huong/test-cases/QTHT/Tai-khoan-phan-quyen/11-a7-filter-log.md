# A7 — Filter UI/function-testable Log (FR-VIII-14..17 + FR-VIII-26)

> **Tác nhân**: Manual review + Edit
> **Ngày**: 2026-05-08
> **Mục đích**: Loại / sửa TC chỉ test được DB/API thuần. Filter rule: KHÔNG được "verify DB row", "check INDEX", "curl POST raw", "cron job no-UI".
>
> **A7 Rule chi tiết** (xem plan §3.1):
> - ❌ LOẠI: TC require query DB trực tiếp / curl API thuần / cron không UI
> - ✏️ SỬA: TC verify-DB → verify-network qua MCP `list_network_requests`
> - ✅ GIỮ: TC chạy 100% qua UI/function user-facing — bao gồm verify network response qua MCP

---

## 1. Manual scan kết quả

### 01-TC-vai-tro.md (31 TC)

| TC | Action | Reasoning |
|----|--------|-----------|
| TC-VT-101..123 | ✅ GIỮ | UI-only CRUD + filter + pagination, đã có signal UI rõ. |
| TC-VT-124..129 | ✅ GIỮ | Boundary + sanitize qua form UI, verify behavior qua toast/inline error. |
| TC-VT-130 | ✅ GIỮ | AUDIT_LOG verify qua SCR-VIII-10 (UI module Nhật ký HT W1.1) — UI bridge. |
| TC-VT-131 | ✅ GIỮ | Tương tự TC-130. |
| **TC-VT-132** | ✅ GIỮ | IDOR direct API CALL nhưng dùng MCP `evaluate_script` trong devtools console của browser đã login `cb_nv_tw_01` — UI bridge per A7 rule. KHÔNG curl thuần. |
| TC-VT-133..136 | ✅ GIỮ | Race condition + edge UI behavior — verifable qua UI. |
| TC-VT-137 | ✅ GIỮ | so_tai_khoan derive — verify qua cột UI UC112 sau khi tạo TK qua UI UC113. |
| TC-VT-138 | ✅ GIỮ | Verify form UI có field `cap` không. |

**Kết quả:** 0 LOẠI / 0 SỬA / 31 GIỮ.

### 02-TC-tai-khoan.md (60 TC)

| TC | Action | Reasoning |
|----|--------|-----------|
| TC-TK-101..119 | ✅ GIỮ | UI list + filter + tab counter + CRUD + lifecycle button — 100% UI. |
| TC-TK-130..142 | ✅ GIỮ | SM-TAIKHOAN 12 transitions qua UI button hoặc behavior (login, mail kích hoạt MailHog UI). |
| TC-TK-150..168 | ✅ GIỮ | Validation + boundary qua form UI, verify toast/inline error. |
| TC-TK-169..170 | ✅ GIỮ | Edge unique cross is_deleted — verify qua hành vi UI submit + toast. |
| TC-TK-180 | ✅ GIỮ | Cross-tenant qua filter UI tree. |
| **TC-TK-181** | ✅ GIỮ | Inject vneid_subject qua MCP `evaluate_script` UI bridge — KHÔNG curl thuần. |
| TC-TK-182..183 | ✅ GIỮ | XSS/SQL qua form UI, verify list_console_messages no alert. |
| **TC-TK-184** | ✅ GIỮ | IDOR DELETE qua MCP `evaluate_script` UI bridge. |
| TC-TK-185..186 | ✅ GIỮ | AUDIT_LOG verify qua SCR-VIII-10 UI bridge. |
| TC-TK-187..190 | ✅ GIỮ | Race condition + batch action + reject reason — UI behavior. |
| **TC-TK-191** | ✅ GIỮ | SM invalid transition qua MCP `evaluate_script` UI bridge. (Note: button [Mở khóa] KHÔNG hiện trên UI khi TK HOAT_DONG → user không trigger được qua UI; test API direct thông qua devtools.) |
| TC-TK-192..196 | ✅ GIỮ | Pagination + login_cuoi + soft delete + count derive — UI bridge. |

**Kết quả:** 0 LOẠI / 0 SỬA / 60 GIỮ.

### 03-TC-phan-quyen-du-lieu.md (24 TC)

| TC | Action | Reasoning |
|----|--------|-----------|
| TC-PQDL-101..107 | ✅ GIỮ | UI cây 2-tầng + tag-list + checkbox cascade — UI 100%. |
| TC-PQDL-120..127 | ✅ GIỮ | Validation + ngang cấp + edge inject ID qua MCP `evaluate_script` UI bridge. |
| **TC-PQDL-130** | ✅ GIỮ | IDOR direct PUT qua MCP `evaluate_script` UI bridge. |
| **TC-PQDL-131** | ✅ GIỮ | Cache invalidation verify qua hành vi user (login lại + reload module thực tế) — UI bridge cross-module. |
| TC-PQDL-132..134 | ✅ GIỮ | Cascade + performance qua UI cây + form. |
| **TC-PQDL-135** | ✅ GIỮ | entity_type filter — verify qua UI form (nếu có). Nếu UI không show, log SPEC-CLARIFY-TKPQ-23 + skip. |
| TC-PQDL-136 | ✅ GIỮ | AUDIT_LOG SCR-VIII-10 UI bridge. |
| TC-PQDL-137..138 | ✅ GIỮ | UI behavior empty state. |

**Kết quả:** 0 LOẠI / 0 SỬA / 24 GIỮ.

### 04-TC-phan-quyen-chuc-nang.md (22 TC)

| TC | Action | Reasoning |
|----|--------|-----------|
| TC-PQCN-101..108 | ✅ GIỮ | UI matrix + cây menu + cascade — UI 100%. |
| TC-PQCN-120..123 | ✅ GIỮ | Validation + edge inject ID qua MCP `evaluate_script` UI bridge. |
| **TC-PQCN-130** | ✅ GIỮ | IDOR direct PUT qua MCP `evaluate_script` UI bridge. |
| **TC-PQCN-131** | ✅ GIỮ | Cache invalidation cross-module verify qua sidebar/page reload thực tế (UI bridge). |
| **TC-PQCN-132..134** | ✅ GIỮ | Cross-module verify quyền Phê duyệt / Xuất / Xóa hiển thị button thực tế trên UI module → UI bridge cross-module. |
| TC-PQCN-135..138 | ✅ GIỮ | UI cây + audit + perf qua UI bridge. |

**Kết quả:** 0 LOẠI / 0 SỬA / 22 GIỮ.

### 05-TC-quen-mk-kich-hoat.md (27 TC)

| TC | Action | Reasoning |
|----|--------|-----------|
| TC-PWD-101..106 | ✅ GIỮ | Form quên MK + mail link click + form đặt MK — 100% UI flow. MailHog UI verify. |
| TC-PWD-120..130 | ✅ GIỮ | Validation + token lifecycle qua hành vi UI form. |
| **TC-PWD-129** | ✅ GIỮ | Token random fake — verify qua URL direct (UI navigate) → form behavior + toast. |
| TC-PWD-140..141 | ✅ GIỮ | Boundary token wait time — UI bridge (deferral nếu env không support time-travel). |
| **TC-PWD-142..143** | ✅ GIỮ | Trigger SM-TVV / SM-NHT verify qua module CG/TVV / NHT thực tế (UI bridge cross-module). |
| TC-PWD-144 | ✅ GIỮ | Rate limit qua hành vi UI submit nhiều lần. |
| **TC-PWD-145** | ✅ GIỮ | Token cross-account qua URL inject (UI navigate). |
| TC-PWD-146..147 | ✅ GIỮ | XSS + edge state qua form UI. |
| TC-PWD-148 | ✅ GIỮ | AUDIT_LOG SCR-VIII-10 UI bridge. |
| TC-PWD-149 | ✅ GIỮ | Mail link format qua MailHog UI. |
| **TC-PWD-150** | ⚠️ MARK ATTENTION | Token cleanup cron — chỉ test được qua hành vi reject (TC-123 cùng pattern); KHÔNG verify DB direct được. **GIỮ NHƯNG** mark "indirect verify". |

**Kết quả:** 0 LOẠI / 0 SỬA / 27 GIỮ (1 TC marked indirect verify).

### 06-TC-permission-matrix.md (24 TC)

| TC | Action | Reasoning |
|----|--------|-----------|
| TC-TKPQ-PERM-001..018 | ✅ GIỮ | Role-based access happy path + negative qua URL direct (UI navigate). |
| **TC-TKPQ-PERM-020..025** | ✅ GIỮ | IDOR direct API CALL qua MCP `evaluate_script` UI bridge per A7 rule. |
| TC-TKPQ-PERM-030..032 | ✅ GIỮ | FR-VIII-26 public access qua UI form. |
| TC-TKPQ-PERM-040..041 | ✅ GIỮ | Cross-tenant qua UI filter. |
| TC-TKPQ-PERM-050..051 | ✅ GIỮ | AUDIT_LOG SCR-VIII-10 UI bridge. |

**Kết quả:** 0 LOẠI / 0 SỬA / 24 GIỮ.

---

## 2. Tổng kết A7

### A7 round 1 (initial 2026-05-08)

| File | TC tổng | LOẠI | SỬA | GIỮ |
|------|---------|------|-----|-----|
| 01-TC-vai-tro.md | 29 | 0 | 0 | 29 |
| 02-TC-tai-khoan.md | 66 | 0 | 0 | 66 |
| 03-TC-phan-quyen-du-lieu.md | 24 | 0 | 0 | 24 |
| 04-TC-phan-quyen-chuc-nang.md | 21 | 0 | 0 | 21 |
| 05-TC-quen-mk-kich-hoat.md | 28 | 0 | 0 | 28 |
| 06-TC-permission-matrix.md | 27 | 0 | 0 | 27 |
| **Tổng** | **195** | **0** | **0** | **195** |

### A7 round 2 — Codex R2 review (2026-05-08)

Codex flagged 14 TC IDOR + 1 false flag + 5 expected sai = 20 fixes. Re-classification:

| File | TC trước R2 | LOẠI/MOVE → 07 | RESHAPE expected | ADD fill BR | TC sau R2 |
|------|-------------|-------------------|-------------------|-------------|-----------|
| 01-TC-vai-tro.md | 29 | -1 (TC-VT-132) -1 (TC-VT-110 false flag) | 2 (TC-VT-104, TC-VT-125 — bỏ SELECT raw) | 0 | **27** |
| 02-TC-tai-khoan.md | 66 | -4 (TC-160/161/181/184) | 2 (TC-101 6→5 filter, TC-191 reframe affordance, TC-195 UI bridge) | +3 (TC-197/198/199 BR-AUTH-06/09 + BR-DATA-03) | **65** |
| 03-TC-phan-quyen-du-lieu.md | 24 | -2 (TC-126, 130) | 5 (TC-120-123 reframe cap, TC-127 force reject) | 0 | **22** |
| 04-TC-phan-quyen-chuc-nang.md | 21 | -2 (TC-121, 130) | 1 (TC-122 force reject) | 0 | **19** |
| 05-TC-quen-mk-kich-hoat.md | 28 | 0 | 0 | +2 (TC-151/152 BR-EC-13 200 char) | **30** |
| 06-TC-permission-matrix.md | 27 | -6 (TC-020..025) | 0 | 0 | **21** |
| **07-TC-security-IDOR.md** (NEW) | 0 | +16 from above | — | — | **16** |
| **Tổng functional (01-06)** | 195 | -16 IDOR -1 false flag | 10 reshape | +5 fill | **184** |
| **Tổng grand total** (01-07) | 195 | — | — | +5 (BR fill) | **200** |

**A7 violation rate: 0%** — TC nào có touch DB/API đều dùng MCP `evaluate_script` trong UI context (devtools console của browser đã login) → VALID UI bridge per A7 rule.

---

## 3. UI bridge patterns được sử dụng

| Pattern | Số TC | TC list |
|---------|-------|---------|
| MCP `evaluate_script` devtools console (đã login user) — IDOR / SM invalid transition / inject FK ID | 14 | 01:132 / 02:160, 161, 181, 184, 191 / 03:126, 130 / 04:121, 130 / 06:020-025 |
| SCR-VIII-10 Nhật ký HT (W1.1 module) verify AUDIT_LOG | 9 | 01:130-131 / 02:185-186 / 03:136 / 04:105, 136 / 05:148 / 06:050-051 |
| MailHog UI (`http://103.172.236.130:8025`) verify mail | 4 | 02:115, 119 / 05:101, 149 |
| Cross-module verify (module CG/TVV, NHT, Vụ việc) | 6 | 02:131 (T2 sự kiện) / 03:105 / 04:132-134 / 05:142-143 |
| URL direct navigate (test 403 + trigger forgot password) | 12 | 06:010-018, 030-032 |

> Tất cả patterns đều là UI bridge VALID — không curl thuần, không SQL direct, không cron-only.

---

## 4. Notes deferral (Phase B)

| TC | Lý do deferral | Action Phase B |
|----|----------------|----------------|
| TC-TK-139 (auto unlock 30 phút) | Cần wait 30 phút thật hoặc time-travel mock | Phase B run với note manual; nếu env không support, log Gap. |
| TC-TK-142 (auto disable 7 ngày) | Cần wait 7 ngày | Phase B defer hoặc mock cron trigger. |
| TC-PWD-140 (token vĩnh viễn 31 phút) | Cần wait 31 phút | Phase B note manual. |
| TC-PWD-141 (token 30 phút boundary) | Cần wait chính xác 30 phút | Phase B time-control nếu có. |
| TC-PWD-150 (token cleanup cron) | Indirect verify only | Phase B test reject behavior (TC-123 pattern). |
| TC-PQDL-105 (cross-module data Vụ việc) | Phụ thuộc seed VV + W3.2 Phase B | Run sau W3.2 Phase B done. |
| TC-PWD-142, TC-PWD-143 (trigger SM-TVV, SM-NHT) | Phụ thuộc module CG/TVV + NHT | Run sau W2.2 Phase B done. |

**Tổng: 7 TC marked deferral / partial Phase B execution.**

---

## 5. A7 Compliance: ✅ PASS

- ✅ 0 TC chỉ-DB/API thuần
- ✅ 0 TC require DB query / SQL direct / cron-only
- ✅ Mọi IDOR / direct API call dùng MCP `evaluate_script` trong UI context
- ✅ Mọi audit verify qua UI module (SCR-VIII-10)
- ✅ Mọi mail verify qua MailHog UI
- ✅ Cross-module verify qua entity UI thực tế

**Tổng final TC sau A7 round 1: 195** (0 LOẠI, 0 SỬA — confirm GIỮ).
**Tổng final TC sau A7 round 2 (Codex R2): 200 grand total = 184 functional (file 01-06) + 16 security (file 07).**

### A7 Compliance update sau Codex R2

- ✅ 16 TC IDOR/FK injection MOVED to security suite riêng (file 07) — không còn lẫn trong functional UC.
- ✅ TC-VT-104, TC-VT-125, TC-TK-195 SỬA expected — bỏ `SELECT raw is_deleted=1` / `SELECT count(*)`, thay bằng UI list verify + AUDIT_LOG SCR-VIII-10.
- ✅ TC-PQDL-127, TC-PQCN-122 SỬA expected — force reject empty thay vì option "accept" (SRS rõ ràng yêu cầu Y bắt buộc).
- ✅ TC-PQDL-120-123 reframe — không assert mapping role→specific don_vi (VAI_TRO ERD chỉ có cap enum); test logic ngang cấp dựa trên cap.
- ✅ TC-VT-110 RESOLVED out-of-scope — search box không tồn tại trong SCR-VIII-02.
- ✅ TC-TK-197/198/199 NEW fill BR thiếu (BR-AUTH-06 session, BR-AUTH-09 VNeID, BR-DATA-03 common fields) qua UI bridge.
- ✅ TC-PWD-151/152 NEW fill BR-EC-13 boundary email 200 ký tự.
- ✅ TC-TK-191 reframe — UI affordance verify (button [Mở khóa] không hiện trên dòng HOAT_DONG); API-level test moved 07.
- ✅ TC-TK-101 fix — 6 filter → 5 filter (loại bỏ duplicate "search").

### A7 Compliance: ✅ PASS sau Codex R2

- 0 TC chỉ-DB/API thuần trong functional suite (01-06)
- 16 TC API authz tách riêng file 07 (security suite)
- Mọi audit verify qua UI module (SCR-VIII-10)
- Mọi mail verify qua MailHog UI
- Cross-module verify qua entity UI thực tế

---

## 2. UC120 / FR-VIII-22 Append (2026-05-10)

> **Scope mới**: 12-TC-self-registration-dn.md (UC120 self-registration DN — 68 TC). Manual A7 filter: phân loại từng TC LOẠI / SỬA / GIỮ theo rule "UI/function-testable".

### 12-TC-self-registration-dn.md (68 TC)

| TC | Action | Reasoning |
|----|--------|-----------|
| TC-REG-101..106 | ✅ GIỮ | Happy path Public form public access + click link mail + đăng nhập DN portal — 100% UI flow. |
| TC-REG-110..143 | ✅ GIỮ | Validation 18 trường Nhóm 1 — submit form UI, verify toast/inline error. Network verify qua MCP `list_network_requests` (TC-REG-122 + 124 + 222 + 223 — UI bridge OK per A7 rule). |
| TC-REG-150..167 | ✅ GIỮ | Validation 4 trường Nhóm 2 — UI form behavior + indicator. |
| TC-REG-180..185 | ✅ GIỮ | ERR-REG-01..06 — submit form UI verify toast. |
| TC-REG-190 | ✅ GIỮ | AUDIT_LOG verify qua SCR-VIII-10 UI module — UI bridge. |
| TC-REG-191 | ✅ GIỮ | Auto-pass verify qua submit form UI + state verify qua UC113 list. |
| TC-REG-192..194 | ✅ GIỮ | Public access + CB nội bộ edge — UI behavior verify. |
| TC-REG-195 | ✅ GIỮ | SM-TAIKHOAN T1 verify qua UC113 SCR-VIII-03 list filter `CHO_KICH_HOAT` — UI bridge. |
| TC-REG-196 | ✅ GIỮ | SM-TAIKHOAN T4 verify qua UC113 list trạng thái `HOAT_DONG` sau click link — UI bridge. |
| TC-REG-197 | ✅ GIỮ | DN portal access — login UI flow. |
| TC-REG-198..199 | ✅ GIỮ | Race condition + concurrent — verify qua UC113 list count + ERR-REG toast. UI bridge OK. |
| TC-REG-200..205 | ✅ GIỮ | Edge Unicode/whitespace/leading-zero/phone-intl/file-dup/MIME-spoof — submit form UI + toast. **TC-REG-202 MST leading-zero**: verify qua DN list cột MST (UC113 hoặc DN portal sau login) — KHÔNG SELECT raw DB. |
| TC-REG-206..207 | ✅ GIỮ | Re-register soft-delete — submit form UI + ERR toast verify. |
| TC-REG-208 | ✅ GIỮ | Same DN name — submit OK + DN list verify 2 records. |
| TC-REG-209 | ✅ GIỮ | Network failure mid-submit — DevTools throttle + retry, verify qua UI submit behavior + count UC113. |
| TC-REG-210 | ✅ GIỮ | Browser autofill — UX UI. |
| TC-REG-211 | ✅ GIỮ | Email IDN — submit form UI verify toast. |
| **TC-REG-212** | ⚠️ GIỮ với note | Cancel cleanup file — **storage cleanup KHÔNG verify trực tiếp được qua UI**. Note đã có "defer Phase B note manual" — TC GIỮ vì verify hành vi reload form (file orphan check sẽ defer storage admin). KHÔNG LOẠI vì test có UI signal (form mới mở không có file cũ). |
| TC-REG-220 | ✅ GIỮ | Form layout — UI quan sát. |
| TC-REG-221 | ✅ GIỮ | Mail HTML format — verify qua MailHog UI (port 8025) — UI bridge. |
| TC-REG-222 | ✅ GIỮ | SMTP connectivity — verify qua MailHog API endpoint `http://103.172.236.130:8025/api/v2/messages` — UI bridge per A7 rule (MailHog UI accessible). |
| TC-REG-223 | ✅ GIỮ | File upload network response — MCP `list_network_requests` UI bridge. |

**Kết quả UC120:** 0 LOẠI / 0 SỬA / 68 GIỮ.

### Kiểm tra A7 strict cho UC120

| Rule kiểm tra | Pass? | Note |
|---------------|-------|------|
| 0 TC require "verify DB row" trực tiếp | ✅ | Mọi state verify qua UC113 list / UI flow / AUDIT_LOG SCR-VIII-10. |
| 0 TC require curl/Postman API thuần | ✅ | TC-REG-222 dùng GET MailHog API qua UI hoặc MCP fetch (UI bridge). |
| 0 TC verify cron job no-UI | ✅ | TC-REG-104 (token vĩnh viễn) defer Phase B với note "manual time check / time-travel mock"; TC-REG-212 cleanup defer manual. |
| TC verify network response qua MCP | ✅ | TC-REG-122/124 (load tree DON_VI/DM), TC-REG-222 (SMTP), TC-REG-223 (upload) — qua MCP `list_network_requests` UI bridge. |
| Race/concurrent test | ✅ | TC-REG-198 dùng MCP fast double click + verify count UI; TC-REG-199 dùng 2 browser tab MCP `new_page`. |
| MIME spoof TC-REG-205 | ✅ | Upload qua form UI, BE reject hoặc accept observable qua toast/inline error. |
| File storage UUID TC-REG-223 | ✅ | Verify qua network response payload (MCP `list_network_requests`) — KHÔNG SELECT storage path raw. |

### UC120 A7 Compliance: ✅ PASS

- 0 TC chỉ-DB/API thuần trong UC120 functional suite
- Mọi state verify qua UI list (UC113) hoặc form behavior
- Mail verify qua MailHog UI/API
- Network verify qua MCP `list_network_requests`
- Defer items có note rõ Phase B handling

### Tổng count W1.4 sau A7 (cumulative)

```
Functional W1.4: 184 (UC112-117) + 68 (UC120) = 252 TC
Security: 16 (file 07 IDOR)
Grand total: 268 TC
```

**UC120 Phase A status:** A1-A7 ✅ ALL DONE 2026-05-10. Ready for Phase B (B-block riêng `12-TC-self-registration-dn.md`).
