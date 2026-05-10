# Bug Report — System BE / Auth Login Endpoint

| Thông tin | Giá trị |
|-----------|---------|
| **Dự án** | PM HTPLDN |
| **Môi trường** | http://103.172.236.130:3000/ |
| **Người test** | QA Automation (Claude Code) |
| **Ngày** | 2026-05-09 13:18:42 → 13:21:14 (sustained ~3 phút) |
| **Loại test** | Functional R7.7.1 (block khi probe pool) |
| **Round** | Round 7 / R7.7.1 Phase 1 |
| **Tài liệu tham chiếu** | [todo-hoi-dap.md R7.7.1](../../../../../tasks/todo-hoi-dap.md#r7-7-1) · [users.csv](../../../../../input/users.csv) · `srs-update-2026-5-5/srs-fr-22-tai-khoan.md` (auth flow) · Error code `ERR-SYS-00-00-01` |

---

## Tổng hợp

Phát hiện **1 bug Critical** block toàn bộ QA: BE endpoint `POST /api/v1/auth/login` sustained 500 ERR-SYS-00-00-01 cho TẤT CẢ accounts đang test (đã verify 5 accounts: `cb_nv_tw_02/03/04`, `cb_pd_tw_04`, `cb_nv_bn_04`). Static FE + non-login API endpoints vẫn 200/401 bình thường → BE hệ thống còn sống nhưng riêng login service crash.

> **Rule log bug (feedback 2026-04-23):** Bug có Error code reference `ERR-SYS-00-00-01` trong response → đủ điều kiện log bug. Không có FR/BR cụ thể vì lỗi ở tầng infrastructure auth.

### Severity breakdown

| Tổng | Critical | Major | Medium | Minor | Trivial |
|------|----------|-------|--------|-------|---------|
| 1    | 1        | 0     | 0      | 0     | 0       |

## Bug Summary Table

| Bug ID | Severity | Priority | Type | TC Ref | **SRS Reference** | Title | Status |
|--------|----------|----------|------|--------|-------------------|-------|--------|
| ~~BUG-BE-LOGIN-001~~ | Critical | P0 | Workflow/Infra | R7.7.1 (block toàn module) | Error catalog `ERR-SYS-00-00-01` | ~~`POST /api/v1/auth/login` 500 sustained, block toàn QA~~ | Closed |

> **Chú thích Severity:**
> - `Critical` — hệ thống/tính năng chính không dùng được, lộ dữ liệu, sai nghiệp vụ nghiêm trọng

---

## ~~BUG-BE-LOGIN-001~~ [CLOSED] — `POST /api/v1/auth/login` trả 500 ERR-SYS-00-00-01 cho mọi tài khoản, sustained ~3 phút

> **Re-test:** 2026-05-09 22:09:11 (15:09:12 GMT) R10 — ✅ PASS (Closed-verified). `POST /api/v1/auth/login` với `cb_nv_tw_04` trả `HTTP 200 + otpToken=dec58078-6c4f-4977-bce8-f21e517e20b2 + maskedEmail=cb_***@htpldn.test`. BE login service đã khôi phục, không reproduce. Resume R7.7.1 Phase 1.

### Mô tả

QA login bằng `cb_nv_tw_04` qua UI MCP để chạy R7.7.1 thì FE đứng ở trang `/login` sau khi click [Đăng nhập]. Probe trực tiếp BE `POST /api/v1/auth/login` 5 accounts khác nhau (TW NV/PD, BN NV, suffix _02/_03/_04) đều trả `HTTP 500 ERR-SYS-00-00-01 "Lỗi hệ thống, vui lòng thử lại sau"`. Header `x-ratelimit-remaining` đếm bình thường (5→4→3→2→1→0) → request đến BE thành công, BE crash khi process login. Sau đợi 70s (rate-limit reset), retry vẫn 500. Tổng quan FE static `/login` 200, public API `auth/me` không token trả 401 đúng spec → riêng login endpoint hỏng.

### Các bước tái hiện

1. Navigate `http://103.172.236.130:3000/login` (FE 200 OK).
2. Fill form `username=cb_nv_tw_04`, `password=Secret@123`, click [Đăng nhập].
3. Quan sát: FE đứng ở `/login`, không có toast lỗi visible (form không hiện error message), DevTools Network thấy `POST /api/v1/auth/login` HTTP 500.
4. Probe trực tiếp qua `curl -X POST` cùng payload → BE trả `{"success":false,"error":{"code":"ERR-SYS-00-00-01","message":"Lỗi hệ thống, vui lòng thử lại sau"}}` HTTP 500.
5. Lặp với 4 accounts khác `cb_nv_tw_02 / cb_nv_tw_03 / cb_pd_tw_04 / cb_nv_bn_04` → cùng response 500.
6. Đợi 70s (rate-limit reset), retry `cb_nv_tw_02 + cb_nv_tw_04` → vẫn 500.
7. Cross-check env: `GET /` 200 (44ms), `GET /login` 200 (16ms), `GET /api/v1/auth/me` 401 đúng spec, `GET /api/v1/danh-muc?...` 401 đúng spec → BE alive, riêng login endpoint chết.

### Kết quả mong đợi

- `POST /api/v1/auth/login` với credentials hợp lệ → HTTP 200 + cookie session + redirect FE sang trang OTP `Nhập mã xác thực`.
- Nếu credentials sai → HTTP 401 ERR-AUTH-LOGIN-01 "Sai tên đăng nhập hoặc mật khẩu".
- Nếu account locked → HTTP 423 ERR-AUTH-LOCKED-01.
- Error code `ERR-SYS-00-00-01` chỉ xuất hiện khi BE infrastructure exception thực sự (DB down, service crash) — không phải behavior bình thường khi login.

### Kết quả thực tế

- Tất cả 5 accounts test trả `HTTP 500 ERR-SYS-00-00-01` ngay từ request đầu tiên (không phải sau exhaust rate-limit).
- Sustained ≥3 phút (13:18:42 → 13:21:14), không tự khôi phục.
- FE không hiện toast lỗi visible khi BE 500 → user-facing UX cũng broken (silent fail).

```
=== POST /api/v1/auth/login ===
HTTP/1.1 500 Internal Server Error
x-powered-by: Express
x-ratelimit-limit: 5
x-ratelimit-remaining: 3..0
x-ratelimit-reset: 24..60s
content-type: application/json
date: Sat, 09 May 2026 13:18:42 → 13:21:14 GMT

{"success":false,"error":{"code":"ERR-SYS-00-00-01","message":"Lỗi hệ thống, vui lòng thử lại sau","timestamp":"2026-05-09T13:18:42.119Z","requestId":"4ce8dbfb-6701-4687-b9b2-da76b70ff5e2"}}
```

Test 5 accounts đầy đủ:

| # | Username | HTTP | Code | requestId | Time (UTC) |
|---|----------|:-:|---|---|---|
| 1 | cb_nv_tw_04 | 500 | ERR-SYS-00-00-01 | 4ce8dbfb-6701-4687-b9b2-da76b70ff5e2 | 13:18:42 |
| 2 | cb_nv_tw_02 | 500 | ERR-SYS-00-00-01 | 65d30823-6ba9-4231-a65f-992e88dd1775 | 13:19:00 |
| 3 | cb_nv_tw_03 | 500 | ERR-SYS-00-00-01 | 98388022-186f-4d6e-9b0e-c0b931b6f23b | 13:19:10 |
| 4 | cb_pd_tw_04 | 500 | ERR-SYS-00-00-01 | 8c7874c5-0c6c-4da4-9334-a889254e1812 | 13:19:20 |
| 5 | cb_nv_bn_04 | 500 | ERR-SYS-00-00-01 | 5ec447f2-045f-4cc0-9e93-0d42e0aa54c8 | 13:19:30 |
| 6 | cb_nv_tw_02 (retry sau 70s) | 500 | ERR-SYS-00-00-01 | 5c30ba0d-92a3-4626-921e-5beea2eaff0c | 13:21:03 |
| 7 | cb_nv_tw_04 (retry sau 70s) | 500 | ERR-SYS-00-00-01 | 07f82e2d-ad63-4d68-9be5-9708585bcc86 | 13:21:13 |

Cross-check env health (cùng thời điểm):

```
GET /                              → HTTP 200 (44ms)
GET /login                         → HTTP 200 (16ms)
GET /api/v1/auth/me  (no token)    → HTTP 401 (đúng spec — BE alive, only login endpoint dead)
GET /api/v1/danh-muc?loaiDanhMuc=LINH_VUC_PL (no token) → HTTP 401 (đúng spec)
```

### Bằng chứng

**1. Ảnh chụp:**

![BUG-BE-LOGIN-001 — Trang OTP đứng sau verify-otp 400, OTP `666666` không bypass với cb_nv_tw_04](image/bug-be-login-001-otp-fail-page.png)

![BUG-BE-LOGIN-001 — FE stuck `/login` sau khi BE login endpoint trả 500, không có toast lỗi](image/bug-be-login-002-login-page-stuck.png)

**2. API response:**

```json
{
  "success": false,
  "error": {
    "code": "ERR-SYS-00-00-01",
    "message": "Lỗi hệ thống, vui lòng thử lại sau",
    "timestamp": "2026-05-09T13:21:13.774Z",
    "requestId": "07f82e2d-ad63-4d68-9be5-9708585bcc86"
  }
}
```

**3. Phân loại theo Rule 9 (CLAUDE.md):**

| Tiêu chí | Đánh giá |
|---|---|
| URL `/login` static + public API trả 401 đúng spec | ✅ Env BE alive |
| `POST /auth/login` 500 sustained, requestId khác nhau mỗi lần | ✅ BE process per-request, exception handler trigger ERR-SYS catch |
| 5 accounts khác nhau (suffix `_02/_03/_04`, role NV/PD, cấp TW/BN) đều fail | ✅ Không phải account-specific lock |
| Sau 70s đợi rate-limit reset, retry vẫn 500 | ✅ Không phải transient (cold cache, throttle) |
| → **Phân loại: APP/BE BUG** (login service crash, không phải ENV DOWN, không phải REAL CRASH browser, không phải SELECTOR OUTDATED, không phải ACCOUNT ISSUE) | ✅ |

---

## Phụ lục — Môi trường test

| Thành phần | Giá trị |
|------------|---------|
| URL ứng dụng | http://103.172.236.130:3000/ |
| OTP login | `666666` bypass (verify-otp 400 vì không pass được tầng login trước) |
| MailHog (OTP inbox) | http://103.172.236.130:8025 (kiểm tra: KHÔNG có mail OTP login mới cho 5 accounts test → endpoint không gửi được mail do crash sớm) |
| API base | http://103.172.236.130:3000/api/v1 |
| Frontend | React + Vite + Ant Design |
| Xác thực | JWT + OTP qua mail (BE flow: login → return tempToken → verify-otp → return JWT cookie) |
| Tool test | Chrome DevTools MCP + curl |

---

*Bug report generated: 2026-05-09 13:23:00 | QA Automation via Claude Code (Opus 4.7)*
