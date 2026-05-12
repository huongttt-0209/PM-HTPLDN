# TODO — Hồ sơ + Đổi mật khẩu (cross-cutting)

> **Module:** Hồ sơ cá nhân + Đổi MK (cross-cutting 11 role)
> **Ngày tạo:** 2026-05-12 13:00:00
> **Source plan:** [test-plan.md](./test-plan.md) v1.1 (revised)
> **SRS:** `srs-update-2026-5-5/ho-so-doi-mat-khau.md` + cross-ref `srs-fr-10-quan-tri.md` FR-VIII-26
> **Total task:** 12 · 🟢 ready 12 · ⏳ pending 0 · ✅ done 0

## Icon meaning

- 🟢 Sẵn sàng run (mọi dep state thoả)
- ⏳ Chờ upstream / chờ BA confirm
- 🚫 Block cứng (gap spec / data / env)
- ⚠️ Sai spec (PASS but deviates)
- ✅ Đạt (PASS clean)
- ❌ Lỗi (FAIL bug confirmed)

---

## Cross-module dependency global

- `[need: ≥3 user HOAT_DONG mỗi role (✗ chờ T-FR10-XXX seed CB nội bộ + QTHT)]` — applied cho T-PROF-001/002/003/006/014.
- `[need: ≥1 VNeID account HOAT_DONG mỗi loại DN/NHT/TVV/CG (✗ chờ seed FR-VIII-25 đồng bộ VNeID)]` — applied cho T-PROF-008.
- `[need: BA confirm 6 mâu thuẫn (rule MK 4 vs 5 thành phần / VNeID UI hide vs disable / AUDIT_LOG action code / Avatar field / DN sửa hoTen scope / Multi-device cơ chế)]` — applied cho T-PROF-005/008/010/011/012.

---

## Task list

### Nhóm 1 — Hồ sơ self-view (xem read-only)

- 🟢 **T-PROF-001** Xem hồ sơ self QTHT — verify 5 field render đúng DB
  - **Kết quả:** chưa run. Cover TC-01 + sub TC-02 cho `qtht_01`. [test-plan §4 TC-01/02]
  - **Cần có sẵn:** `qtht_01` HOAT_DONG (sẵn `users.csv`).
  - **Output:** `01-TC-xem-ho-so.md`

- 🟢 **T-PROF-002** Cross-role read-only verify 11 role — username/email/vaiTro không editable
  - **Kết quả:** chưa run. Cover TC-02 toàn bộ 11 role per `users.csv`. [test-plan §4 TC-02]
  - **Cần có sẵn:** 11 account `_01` HOAT_DONG (sẵn `users.csv`).
  - **Output:** `01-TC-xem-ho-so.md`

- 🟢 **T-PROF-003** Entry-point smoke 11 role — header dropdown + landing `/profile` không 403
  - **Kết quả:** chưa run. Cover TC-14 (scope thuần entry, KHÔNG lặp field verify — fix G1). [test-plan §4 TC-14]
  - **Cần có sẵn:** 11 account `_01` HOAT_DONG.
  - **Output:** `01-TC-xem-ho-so.md`

### Nhóm 2 — Hồ sơ self-edit (sửa hoTen + dienThoai)

- 🟢 **T-PROF-004** Sửa hoTen + dienThoai happy path — save persist DB + reload verify
  - **Kết quả:** chưa run. Cover TC-03 với 1 role primary (QTHT) + sample 2 role khác (DN, CG). [test-plan §4 TC-03]
  - **Cần có sẵn:** account HOAT_DONG có quyền edit own profile.
  - **Output:** `02-TC-sua-ho-so.md`

- 🟢 **T-PROF-005** Negative validate hoTen + dienThoai
  - **Kết quả:** chưa run. Cover TC-04 tách 3 sub (empty / >200 / XSS) + TC-05 (regex phone). [test-plan §4 TC-04/05]
  - **Cần có sẵn:** account HOAT_DONG.
  - **Output:** `02-TC-sua-ho-so.md`

### Nhóm 3 — Avatar upload (defer-conditional)

- ⏳ **T-PROF-006** Avatar upload positive + negative (PNG/JPG/SVG/size)
  - **Kết quả:** chưa run. Cover TC-15. **Block Nhóm C — chờ BA confirm Mâu thuẫn 4 (avatar có hay không trên `/profile`).** [test-plan §4 TC-15 + §5 Mâu thuẫn 4]
  - **Cần có sẵn:** BA decision avatar field. Nếu BA bỏ → đóng task ⏭ skip.
  - **Output:** `02-TC-sua-ho-so.md`

### Nhóm 4 — Đổi MK happy

- 🟢 **T-PROF-007** Đổi MK self-service LOCAL happy path + verify MK cũ không login được
  - **Kết quả:** chưa run. Cover TC-06 + TC-06b (positive-negative pair verify đổi MK persist DB). [test-plan §4 TC-06/06b]
  - **Cần có sẵn:** account LOCAL HOAT_DONG biết MK gốc (`qtht_01` / `Secret@123`).
  - **Output:** `03-TC-doi-mat-khau.md`

### Nhóm 5 — Đổi MK negative (regex/length/match)

- ⏳ **T-PROF-008** Negative newPassword độ mạnh — parameterize 4 vs 5 thành phần
  - **Kết quả:** chưa run. Cover TC-07 — default 4 thành phần (BR-AUTH-PWD-01). **Block Nhóm C — chờ BA chốt Mâu thuẫn 1 §5 (4 vs 5 thành phần).** Nếu BA chốt 5 → thêm sub-case `Abc12345` thiếu ký tự đặc biệt. [test-plan §4 TC-07 + §5 Mâu thuẫn 1]
  - **Cần có sẵn:** BA decision rule MK profile.
  - **Output:** `03-TC-doi-mat-khau.md`

- 🟢 **T-PROF-009** Negative currentPassword sai + newPasswordConfirm mismatch
  - **Kết quả:** chưa run. Cover TC-08 + TC-09. Verify TC-06b vẫn login được MK cũ sau TC-08 (đảm bảo không đổi MK trong DB khi current sai). [test-plan §4 TC-08/09]
  - **Cần có sẵn:** account LOCAL HOAT_DONG biết MK gốc.
  - **Output:** `03-TC-doi-mat-khau.md`

### Nhóm 6 — Multi-device invalidate

- 🟢 **T-PROF-010** Multi-device invalidate sau đổi MK — verify 401 server-side + timing + tách session đổi vs bị invalidate
  - **Kết quả:** chưa run. Cover TC-10 (fix G2). 2 session MCP isolated context: session 1 đổi MK → session 2 gọi `/api/v1/auth/me` → expect 401 + redirect `/login`. Verify session 1 KHÔNG bị invalidate. Đo timing. **Quirk `qa_htpldn_jwt_revoke_aggressive`:** BE revoke JWT ~2 phút bất chấp `exp` claim → phải tách rõ session để loại false positive. [test-plan §4 TC-10]
  - **Cần có sẵn:** account LOCAL biết MK + có thể đổi MK lại sau test.
  - **Output:** `03-TC-doi-mat-khau.md`

### Nhóm 7 — Cross-user 403

- 🟢 **T-PROF-011** Cross-user 403 — verify endpoint thực tế qua MCP TRƯỚC khi viết TC
  - **Kết quả:** chưa run. Cover TC-12 (fix G5). **Step 1:** Login QTHT mở `/profile` capture `list_network_requests` ghi endpoint thực (có thể `/api/v1/auth/me` / `/api/v1/users/me` / `/api/v1/tai-khoans/{id}`). **Step 2:** User A login → cố GET/PATCH endpoint của user_B id → expect 403. KHÔNG đoán endpoint từ SRS (SRS không nói URL pattern). [test-plan §4 TC-12]
  - **Cần có sẵn:** 2 account khác user_id (vd `qtht_01` + `cb_nv_tw_01`).
  - **Output:** `05-TC-permission-cross-user.md`

### Nhóm 8 — VNeID Tier 2

- ⏳ **T-PROF-012** VNeID readonly tab Bảo mật — 4 role DN/NHT/TVV/CG
  - **Kết quả:** chưa run. Cover TC-11 (fix G4 — chỉ 4 role có LOAI_DK=VNEID; CB nội bộ N/A). **Block Nhóm A — chờ seed FR-VIII-25 đồng bộ VNeID account.** Verify tab Bảo mật disabled / hide + message redirect VNeID. **Block Nhóm C song song — chờ BA confirm Mâu thuẫn 2 (hide vs disable).** [test-plan §4 TC-11]
  - **Cần có sẵn:** `[need: ≥1 VNeID account HOAT_DONG mỗi loại DN/NHT/TVV/CG (✗ chưa seed)]`
  - **Output:** `04-TC-vneid-readonly.md`

### Nhóm 9 — BA escalate rule MK conflict + edge defer

- ⏳ **T-PROF-013** BA escalate package — 6 mâu thuẫn + 3 gap SRS
  - **Kết quả:** chưa run. **Action không phải test — package câu hỏi BA:** (1) Rule MK 4 vs 5 thành phần · (2) VNeID hide vs disable · (3) AUDIT_LOG action code chính thức · (4) Avatar field có/không · (5) DN sửa hoTen scope · (6) Multi-device cơ chế. + 3 gap: SCR ID `/profile` + ERR code chính thức + Permission matrix dedicated. [test-plan §5 Mâu thuẫn 1-6 + Gap SRS]
  - **Cần có sẵn:** BA available.
  - **Output:** session-handoff hoặc BA decision log.

- ⏳ **T-PROF-014** Edge defer cluster — TAM_KHOA login + rate-limit + AUDIT_LOG verify method
  - **Kết quả:** chưa run. Cover TC-16 (TAM_KHOA login + đổi MK behavior) + TC-17 (rate-limit đổi MK liên tục) + TC-13 (audit log method). **Block Nhóm C/F — chờ BA confirm spec + DBA support nếu DB-level.** [test-plan §4 TC-13/16/17]
  - **Cần có sẵn:** BA decision + DBA contact nếu cần query AUDIT_LOG.
  - **Output:** `03-TC-doi-mat-khau.md` (TC-16/17) + audit cross-cut report (TC-13).

---

## Tiến độ

| Trạng thái | Số task |
|---|--:|
| 🟢 Ready | 8 |
| ⏳ Pending (BA / seed) | 4 |
| 🚫 Blocked cứng | 0 |
| ✅ Done | 0 |
| ❌ FAIL | 0 |
| ⚠️ Sai spec | 0 |
| **Tổng** | **12** |

---

## Mapping TC → Task

| TC | Task ID | Status |
|---|---|:-:|
| TC-01 | T-PROF-001 | 🟢 |
| TC-02 | T-PROF-001 + T-PROF-002 | 🟢 |
| TC-03 | T-PROF-004 | 🟢 |
| TC-04 | T-PROF-005 | 🟢 |
| TC-05 | T-PROF-005 | 🟢 |
| TC-06 | T-PROF-007 | 🟢 |
| TC-06b | T-PROF-007 | 🟢 |
| TC-07 | T-PROF-008 | ⏳ BA |
| TC-08 | T-PROF-009 | 🟢 |
| TC-09 | T-PROF-009 | 🟢 |
| TC-10 | T-PROF-010 | 🟢 |
| TC-11 | T-PROF-012 | ⏳ seed + BA |
| TC-12 | T-PROF-011 | 🟢 |
| TC-13 | T-PROF-014 | ⏳ BA/DBA |
| TC-14 | T-PROF-003 | 🟢 |
| TC-15 | T-PROF-006 | ⏳ BA |
| TC-16 | T-PROF-014 | ⏳ BA |
| TC-17 | T-PROF-014 | ⏳ BA |

---

*Todo generated 2026-05-12 13:00:00 — sau revise test-plan v1.1. Task ID prefix `T-PROF-` cross-cutting. Mọi task icon 🟢 ready nếu không có dep block; ⏳ pending nếu chờ BA / seed. Khi BA confirm 6 mâu thuẫn → re-eval ⏳ → 🟢 cho T-PROF-006/008/012/013/014.*
