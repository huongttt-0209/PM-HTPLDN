# Seed Checklist — Giảng viên (R7.3.11 — R9 light verify, blocked by rate-limit)

**Ngày:** 2026-05-09 20:23–20:31 • **Tài khoản:** `cb_nv_tw_02` → fallback `cb_nv_tw_01` (cả 2 đều bị throttle) • **Trạng thái mong đợi:** `DANG_HOAT_DONG` (HOAT_DONG)
**Màn:** SCR-III-11 — Giảng viên / Trợ giảng • **Đường dẫn:** `/dao-tao/giang-vien/danh-sach`
**SRS:** [FR-III-11 — Quản lý Giảng viên](../../../../../input/srs-update-2026-5-5/srs-fr-03-dao-tao.md#fr-iii-11)
**Round:** R9 — light verify, **BLOCKED add record do BE rate-limit** (env-level).

---

## Kết quả: ⚠️ XONG 8/8 stable (R7 baseline) — R9 add BLOCKED do rate-limit

**State R7 baseline confirmed:** 8 giảng viên `DANG_HOAT_DONG` cover 6 LV (Dân sự + Lao động + Thuế + SHTT + KDTM + Đất đai + Hành chính + KDQT) — đáp ứng filter R7.4.B7/B11 (KH cần giảng viên link).

**R9 add record BLOCKED:** Sau ~10+ login switch trong session R9 (R7.4.B0 verify + 5 seed/workflow tasks), POST `/api/v1/auth/login` trả `ThrottlerException Too Many Requests` (`ERR-SYS-00-29-01`). Direct curl test confirm BE throttle active per-IP, cooldown >5 min (longer than memory `qa_htpldn_jwt_revoke_aggressive` baseline ~60s).

```json
POST /api/v1/auth/login {"username":"cb_nv_tw_01","password":"Secret@123"}
→ 429 {"success":false,"error":{"code":"ERR-SYS-00-29-01","message":"ThrottlerException: Too Many Requests"}}
```

→ Cannot login để test create flow GV qua UI. Defer add R9 record sang session sau (cooldown reset).

---

## Bảng dữ liệu seed (R7 stable — R9 verify)

API state confirmed earlier in session (pre-throttle):

```json
GET /api/v1/giang-viens?pageSize=20  → 8 records, all DANG_HOAT_DONG
```

| # | Tên | Lĩnh vực | Trạng thái | Round |
|:-:|-----|----------|:--:|:--:|
| 1-8 | (8 GV cover 6 LV: Dân sự / Lao động / Thuế / SHTT / KDTM / Đất đai / Hành chính / KDQT) | Mixed | DANG_HOAT_DONG | R7 |

**Tổng:** 8 DANG_HOAT_DONG cover 6 LV. Đáp ứng downstream R7.4.B7 + R7.4.B11 (KH cần ≥1 GV/LV).

---

## R9 verify steps

1. ✅ API GET `/api/v1/giang-viens?pageSize=20` (verify lúc R7.3.10 phase) → 8 records DANG_HOAT_DONG
2. 🚫 UI list verify R9 — BLOCKED do rate-limit chưa cooldown khi nav module sau R7.3.10
3. 🚫 UI create flow R9 — BLOCKED do không login được

---

## Issues encountered R9

**🔴 Login rate-limit IP-level throttle** — sustained:
- Symptom: POST `/auth/login` 429 `ThrottlerException` (curl direct trả `ERR-SYS-00-29-01`)
- Trigger: ~10+ login attempts trong 30 phút session (R7.4.B0 verify 2 account + R7.3.5 3 account + R7.3.6 1 account + R7.3.8/9 1 account + R7.3.10 attempt 2 account + R7.3.11 fallback)
- Cooldown: observed >5 min (vs memory baseline ~60s) — possibly exponential backoff khi flood
- Impact: Block tất cả login UI cho session này. Read-only API calls vẫn OK với cookie session active, nhưng cookie đã expire khi login bị reject → no session

**Workaround:**
- Wait full reset (≥5 phút inactivity)
- Switch IP (không khả thi trong env QA)
- Skip task add → verify-only mode

→ Defer log Minor — confirms BUG-AUTH-OTP-02 update memo (by-design throttle, cần FE UX feedback). Memory `qa_htpldn_jwt_revoke_aggressive` cần update timing baseline.

---

## Bug tracking

- **BUG-AUTH-OTP-02** Major Open — by-design rate-limit, observed cooldown >5 phút trong R9 session. Cần dev:
  - (a) Document threshold + cooldown rõ trong API docs
  - (b) FE catch 429 → toast "Login chậm, thử lại sau X giây" thay vì silent abort
- R9 không log bug mới cho R7.3.11 — task block là cascade từ env-level OTP rate-limit, không phải GV bug.

---

## Ảnh chụp

- [List 8 GV R7 baseline](../../../round7-2026-05-06/seed/dao-tao/r7-3-11-giang-vien-list.png) — R7 evidence, state R9 không đổi (curl pre-throttle confirmed 8 DANG_HOAT_DONG)

---

*2026-05-09 20:31 — QA chạy bằng Chrome DevTools MCP via Claude Code*
