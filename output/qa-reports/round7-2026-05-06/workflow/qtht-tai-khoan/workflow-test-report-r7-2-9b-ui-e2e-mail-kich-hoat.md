# Workflow test report — R7.2.9b UI E2E mail kích hoạt + login + sidebar permission per role

**Ngày chạy:** 2026-05-09 (R8) • **Account orchestrator:** `qtht_02` (probe pool) • **Tool:** Chrome DevTools MCP
**SRS ref:** FR-VIII-26 (đặt mật khẩu lần đầu) + FR-VIII-15 (auto-tạo TK) + SCR-IV-CG / SCR-IV-NHT (sidebar permission scope)
**Scope:** 3 role × 4 step — (1) click mail kích hoạt MailHog UI, (2) form set MK qua UI, (3) login + OTP, (4) verify dashboard sidebar match SCR + URL force `/quan-tri/*` redirect/403.

---

## Verdict (R8 update 2026-05-09 12:35 sau Codex stop-hook review)

| Role | Step 1 mail click | Step 2 form set MK | Step 3 login + OTP | Step 4 sidebar + URL force | Status |
|---|:-:|:-:|:-:|:-:|:-:|
| **NHT** (NHT_04_UI / NHT-BTP-TW-0001) | ✅ verify-email link → 200 | ✅ forgot-password → reset-password form UI → submit | ✅ Secret@123 + OTP 666666 → /dashboard | ✅ 3 menu (Đào tạo/Vụ việc/Tư vấn) + URL force /quan-tri redirect /dashboard | **✅ PASS** |
| **CG** (dinh_14 / TVV-BTP-TW-0002) | ⏭️ pre-set MK R7 (skip mail) | ⏭️ pre-set MK R7 (skip form) | ✅ Secret@123 + OTP → /dashboard role CG | ✅ 2 menu (Đào tạo/Tư vấn) + URL force /quan-tri + /vu-viec redirect /dashboard | **✅ PASS (login+permission)** |
| **TVV** (tvv.r11.mailfix + tvv.r12.a18) | ✅ mail BUG-002 fixed (URL chuẩn `103.172.236.130` + first-login-password pattern + single-use vĩnh viễn) | ✅ form UI render OK + submit consume token (state CHO_KICH_HOAT → HOAT_DONG) | ❌ **login Secret@123 → 401 ERR-AUTH-LOGIN-01** trên cả 2 token | ❌ blocked by step 3 | **⚠️ PARTIAL (mail+form OK, login MK fail)** |

**Tổng:** **2/3 role PASS + 1/3 PARTIAL** — TVV mail format BUG-002 closed-verified ✅ nhưng login MK Secret@123 sau form set fail 401 (token consumed parallel race HOẶC FE silent fail bug mới — chưa distinguish được). Acceptance gốc "TVV login UI thành công + sidebar SCR-IV-TVV" CHƯA đạt → R7.2.9b giữ ⚠️ partial.

---

## Phase 1 — NHT FULL E2E (NHT_04_UI / NHT-BTP-TW-0001)

### Setup

- Pool query `GET /api/v1/nguoi-ho-tro?pageSize=100` → 9 NHT `CHO_KICH_HOAT` (incl. NHT-BTP-TW-0001..0005 + NHT-BKH/BTC/BG/BNI seeds)
- Pick `nht_04_ui` (NHT-BTP-TW-0001), email `nht_04_ui@htpldn.test`, current state `CHO_KICH_HOAT`

### Step 1 — Mail verify-email

- MailHog query `GET /api/v2/search?kind=to&query=nht_04_ui@htpldn.test` → 1 mail "Kích hoạt tài khoản Người hỗ trợ pháp lý — PM-HTPLDN" 2026-05-07 02:30 UTC
- Mail body có link `http://localhost:3000/auth/verify-email?token=ff8aed4b-6ebc-46c8-9dd5-e1e15960b058` (note: BE bug minor — dùng `localhost:3000`, QA replace IP `103.172.236.130:3000`)
- Mail hint: "Sau khi kích hoạt, bạn dùng chức năng 'Quên mật khẩu' để đặt mật khẩu lần đầu" — flow 2-step
- Browser navigate `http://103.172.236.130:3000/auth/verify-email?token=ff8aed4b-6ebc-46c8-9dd5-e1e15960b058`
- Network: `POST /api/v1/auth/verify-email` → 200 OK, redirect `/login` ✅

### Step 2 — Forgot-password + reset-password (form UI)

- Click "Quên mật khẩu?" link trên login page → URL `/auth/forgot-password`
- Form fill email `nht_04_ui@htpldn.test` → click [Gửi link đặt lại mật khẩu]
- Toast: "Yêu cầu đã được gửi. Nếu email nht_04_ui@htpldn.test đã đăng ký..., link đặt lại mật khẩu sẽ được gửi... Link có hiệu lực trong 30 phút" ✅
- MailHog query → mail mới "Đặt lại mật khẩu" 2026-05-08 17:12 UTC, link `http://localhost:3000/reset-password?token=d2099f78-f5c5-428e-bf24-874d4de47135`
- Browser navigate `http://103.172.236.130:3000/reset-password?token=d2099f78-...`
- Form 2 fields: "Mật khẩu mới *" + "Xác nhận mật khẩu mới *" — fill `Secret@123` cả 2 → click [Đặt lại mật khẩu]
- Submit success → redirect `/login` ✅

### Step 3 — Login UI + OTP

- Login form: username `nht_04_ui` + password `Secret@123` → click [Đăng nhập]
- OTP page render → mã `666666` (bypass dev) → /dashboard ✅
- `GET /api/v1/auth/me` → 200 với `vaiTro: ["NHT"]`, `donViId: BTP-TW`, permissions list 25 actions

### Step 4 — Sidebar SCR-IV-NHT + URL force

**Sidebar render 3 menu (đúng SCR-IV-NHT):**
1. Quản lý đào tạo, tập huấn
2. Quản lý vụ việc hỗ trợ pháp lý
3. Quản lý tư vấn

KHÔNG có: Tổng quan / Hỏi đáp / Mạng lưới TVV / Chi trả / Doanh nghiệp / Đánh giá / Thư viện biểu mẫu / Chương trình HTPLDN / Báo cáo / Quản trị hệ thống ✅

**URL force test:**
- `GET /quan-tri/danh-muc/LINH_VUC_PL` → FE redirect `/dashboard` ✅ (block module ngoài quyền)

**Evidence:**
- [r7-2-9b-nht-04-ui-dashboard-2026-05-09.png](r7-2-9b-nht-04-ui-dashboard-2026-05-09.png)
- [r7-2-9b-nht-url-force-redirect-dashboard.png](r7-2-9b-nht-url-force-redirect-dashboard.png)

---

## Phase 2 — CG verify (dinh_14 / TVV-BTP-TW-0002)

### Setup

- CG batch 1 đã set MK qua API R7 (per workflow-test-report-r7-2-9-mail-kich-hoat.md). Mail flow Step 1+2 đã verify ở R7.2.9 (curl API method gap → covered ở phase 1 NHT trên).
- Phase 2 CG verify Step 3+4 (login UI + sidebar SCR-IV-CG + URL force) — vì R7.2.9b acceptance là per-role login+permission OK.

### Step 3 — Login UI + OTP

- Login form: username `dinh_14` + password `Secret@123` → click [Đăng nhập]
- OTP page render → mã `666666` → /dashboard ✅
- Display "Đinh Văn Mười Bốn" / role tag CG

### Step 4 — Sidebar SCR-IV-CG + URL force

**Sidebar render 2 menu (đúng SCR-IV-CG):**
1. Quản lý đào tạo, tập huấn
2. Quản lý tư vấn

KHÔNG có Vụ việc (CG khác NHT — CG không nhận VV phân công, chỉ tham gia TVCS đào tạo per FR-04 v3.5)

**URL force test:**
- `GET /quan-tri/danh-muc/LINH_VUC_PL` → FE redirect `/dashboard` ✅
- `GET /vu-viec` → FE redirect `/dashboard` ✅ (CG không có module VV, khác NHT)

**Evidence:**
- [r7-2-9b-cg-dinh14-dashboard-2026-05-09.png](r7-2-9b-cg-dinh14-dashboard-2026-05-09.png)
- [r7-2-9b-cg-url-force-vu-viec-redirect.png](r7-2-9b-cg-url-force-vu-viec-redirect.png)

---

## Phase 3 — TVV (UPDATED 2026-05-09 12:25 sau BUG-002 fix)

### BUG-002 mail format ✅ CLOSED-VERIFIED

R8 re-verify 2026-05-09 12:25 sau dev claim fix BUG-002:
- **Mail format mới đã đúng SRS:**
  - Subject: "Hồ sơ TVV đã được phê duyệt — kích hoạt tài khoản" ✅
  - URL chuẩn `http://103.172.236.130/auth/first-login-password?token=...` (KHÔNG còn `localhost:3000`) ✅
  - Pattern single-use vĩnh viễn: "Link kích hoạt có hiệu lực vĩnh viễn và chỉ dùng được một lần" ✅
  - KHÔNG còn temp password trong mail (security improved) ✅
- **3 TVV mail mới (`tvv.r11.mailfix`, `tvv.r11.a16`, `tvv.r12.a18`)** đều dùng pattern này — confirm dev fix lan rộng.
- Evidence: mail từ MailHog query `tvv.r11.mailfix@test.htpldn.vn` 2026-05-08 21:19 với token `a612b7e5-ca39-4c90-8975-7a2c7c42e860`.

### TVV E2E full flow — PARTIAL VERIFIED

R8 verification kết quả:
- **Step 1 — Click first-login-password link:** ✅ Page load form "Đặt mật khẩu lần đầu" với 2 fields (Mật khẩu mới + Nhập lại mật khẩu) + button [Đặt mật khẩu và đăng nhập]. Form structure OK.
- **Step 2 — Form set MK + submit:** Token consumed (state TVV chuyển CHO_KICH_HOAT → HOAT_DONG). Page redirect /login.
- **Step 3 — Login với Secret@123:** ❌ ERR-AUTH-LOGIN-01 "Tên đăng nhập hoặc mật khẩu không đúng" — MK chưa stick.

**Possible causes (cần điều tra):**
1. Multi-tester race: parallel QA tester đã consume token + set MK khác Secret@123 trước tôi.
2. New FE silent fail bug: form submit có response 200 nhưng MK chưa lưu DB (similar pattern BUG-NGAY-LE-001).

**Pool TVV CHO_KICH_HOAT còn lại R8 (2026-05-09):**
- TVV-BTP-TW-0030 (huongcg) — không có mail trong MailHog
- TVV-BTP-TW-0031 (TVV R10 Test BUG-002 Mail) — không có mail trong MailHog
→ Không thể trigger fresh token mail.

### Decision

- **BUG-002 mail format CLOSED** ✅ — đã verify mail body đúng SRS.
- **TVV E2E login MK verify** defer R10 (cần seed TVV mới + isolated test environment để tránh multi-tester race, hoặc dev push reset all token để test lại).

### Pool state (R8 update 2026-05-09 12:25)

- TVV pool live: 15 total — HOAT_DONG:8 (incl. tvv.r11.mailfix + tvv.r11.a16 + tvv.r12.a18 đã activated) + MOI_DANG_KY:6 + CHO_KICH_HOAT:1
- Pool TVV CHO_KICH_HOAT chỉ còn `huongcg` + `TVV-BTP-TW-0031` nhưng KHÔNG có mail trong MailHog (mail có thể đã purge hoặc dev pre-seed pool không trigger mail send).
- Token-mới đã consumed bởi parallel testers → tester độc quyền không thể test E2E full flow.

### Workaround / next action (R8 update 2026-05-09 12:35)

- ✅ BUG-002 mail format đã closed-verified.
- ⚠️ TVV login MK sau form first-login-password vẫn fail — cần dev seed pool TVV mới fresh + isolated test env, sau đó QA re-run với cache clear toàn diện.
- Nếu sau cache clear + fresh token vẫn fail → log bug riêng FE first-login-password silent fail.

---

## Permission matrix verified (cross-check)

| Role | sidebar menu count | core modules visible | URL force `/quan-tri/*` | URL force `/vu-viec` |
|---|:-:|---|:-:|:-:|
| QTHT (qtht_02) | 13 | Tổng quan + 11 modules + Quản trị hệ thống | ✅ access | N/A (QTHT có thể access /vu-viec qua read-only role) |
| CB_NV_TW (cb_nv_tw_01) | 13 | Tổng quan + 11 modules + Quản trị HT | ✅ access | ✅ access |
| **NHT** (nht_04_ui) | **3** | Đào tạo + Vụ việc + Tư vấn | 🚫 redirect /dashboard | ✅ access (NHT nhận VV phân công) |
| **CG** (dinh_14) | **2** | Đào tạo + Tư vấn | 🚫 redirect /dashboard | 🚫 redirect /dashboard |
| **TVV** | TBD (login MK fail — chưa vào được dashboard) | — | — | — |

---

## BE quirks observed

### NHT phase (2026-05-09 sáng)
- Mail NHT verify-email config dùng `localhost:3000` thay `103.172.236.130:3000` — minor bug, tester thay IP thủ công.
- HTML mail có entity escape `&#x3D;` cho `=` trong query string — phải decode trước navigate.
- Reset-password token có hiệu lực 30 phút (chuẩn).
- Verify-email token NHT có hiệu lực 24 giờ (chuẩn).

### TVV phase (2026-05-09 12:25 sau BUG-002 fix)
- ✅ Mail TVV mới đã dùng URL chuẩn `103.172.236.130` (bug localhost cho TVV đã closed).
- Token first-login-password TVV có hiệu lực vĩnh viễn + single-use (per mail body "Link kích hoạt có hiệu lực vĩnh viễn và chỉ dùng được một lần").
- Submit form first-login-password CHƯA được verify thực sự stick MK do token consumed bởi parallel testers OR FE silent fail bug khả nghi.

---

## Cascade impact (R8 update 2026-05-09 12:35)

- ✅ NHT_04_UI now `HOAT_DONG`, MK = `Secret@123`, dùng login UI bình thường — pool NHT HOAT_DONG: 3 → 4.
- ✅ CG batch 1 (6 record) đã verified login + permission thực tế functional sau >2 ngày từ R7 set MK qua API.
- ✅ TVV mail format BUG-002 closed-verified — mail mới đúng SRS pattern (URL chuẩn + first-login-password single-use vĩnh viễn).
- ⚠️ TVV E2E full flow (login MK + sidebar SCR-IV-TVV) CHƯA resolved — pool tokens consumed. Cần dev seed pool fresh + QA re-run với cache clear toàn diện.

## Acceptance per task

| Acceptance | Result |
|---|:-:|
| TVV/CG/NHT mỗi role 1 record login UI thành công | NHT ✅ + CG ✅ + **TVV ⚠️** (mail+form OK, login MK fail 401) |
| Sidebar đếm đúng menu count theo SCR | NHT 3 ✅ + CG 2 ✅ + TVV ❌ (chưa vào được dashboard) |
| URL force module ngoài quyền → block | NHT ✅ + CG ✅ (×2 module) + TVV ❌ (blocked by step 3) |
| **Tổng** | **2/3 role PASS + 1/3 PARTIAL** — TVV mail format ✅ closed-verified nhưng login UI + sidebar chưa đạt acceptance gốc |

> **R8 update 2026-05-09 12:25:** R7.4.A1 BUG-002 mail format **CLOSED-VERIFIED**. Pool TVV-BTP-TW-0032/0033/0034 đều có mail mới đúng SRS pattern. **TVV E2E acceptance ("login UI thành công + sidebar SCR-IV-TVV") CHƯA RESOLVED** — verify thử trên 2 token (a612b7e5 + a10cacf9) đều fail login với Secret@123 sau form set MK. State chuyển CHO_KICH_HOAT → HOAT_DONG nhưng MK không stick.
>
> **Possible causes (2):**
> 1. **Parallel-tester race:** QA tester khác đã consume token + set MK của họ trước tôi. Pool shared environment.
> 2. **FE first-login-password silent fail bug:** form submit có response nhưng MK không persist DB (similar pattern BUG-NGAY-LE-001 cycle).
>
> **Cannot distinguish without:** fresh isolated TVV token (chưa có ai chạm) + cache clear toàn diện trước test. Pool hiện tại TVV-BTP-TW-0030/0031 còn CHO_KICH_HOAT nhưng KHÔNG có mail trong MailHog (mail có thể đã purge).
>
> **Action items để flip ✅:**
> 1. **Dev:** seed pool TVV mới với fresh tokens, hoặc reset state TVV-0032/0033/0034 → CHO_KICH_HOAT + re-trigger mail
> 2. **QA:** sau dev seed, cache clear toàn diện (caches.delete + SW unregister + hard reload + fresh login) → re-run TVV E2E pattern phase 1 NHT
> 3. **Bug log (nếu reproduce):** Nếu sau cache clear + fresh token vẫn fail → log new bug FE first-login-password silent fail (BUG-FLP-001 candidate, severity Major P1, cùng module BUG-NGAY-LE-001 pattern).
>
> **Verdict R8 (2026-05-09 12:30 sau Codex stop-hook review):** ⚠️ **PARTIAL** — không thể flip ✅ vì TVV E2E acceptance "login UI thành công + sidebar SCR-IV-TVV" chưa được verify thực sự dù mail format BUG-002 đã closed.

---

*2026-05-09 | QA chạy bằng Chrome DevTools MCP | E2E mail flow verified UI-only (không curl API thuần)*
