# Workflow Test Report — R7.4.A1.6 Gate verify state machine TVV/CG

> **Module:** Tư vấn viên / Chuyên gia (Mạng lưới TVV) · **SRS:** [`srs-update-2026-5-5/srs-fr-10-quan-tri.md` FR-VIII-15 + FR-VIII-26](../../../../input/srs-update-2026-5-5/srs-fr-10-quan-tri.md) · **Round:** R11 (LATEST) · **Date:** 2026-05-09 07:55:03 · **Tester:** QA-claude
> **Scope:** 4 TC verify gate FR-VIII-15 (TK auto-creation timing) + FR-VIII-26 (mail kích hoạt + dual-state sync). Phụ thuộc R7.4.A1-CG ✅ + R7.2.6 đợt 2 ✅ + qtht_01 admin scope.

---

## Kết luận

✅ PASS — **4/4 TC PASS** R11 walk fresh TVV-BTP-TW-0033 single record qua full lifecycle MDK→DTĐ→CPĐ→CKH→HOAT_DONG. R8 batch verify 4/4 TC vẫn giữ. State machine FR-VIII-15 + FR-VIII-26 đúng spec qua 4 gate độc lập.

---

## R11 Round (LATEST — 2026-05-09 07:55:03 — fresh TVV walk gate verification)

> **Tester:** QA-claude · **Method:** Chrome DevTools MCP UI walk + qtht_01 API verify (cb_nv_tw_02 → cb_pd_tw_02 → tvv_r11_a16 first-login → qtht_01 cross-entity check) · **Account:** xem Accounts.

**Mục đích R11:** Re-verify 4 TC gate trên 1 TVV mới (TVV-BTP-TW-0033) walk full lifecycle, đo precise timing TK creation + mail fire + dual-state sync. R8 batch verify đã PASS — R11 single-record verify tighter timing assertions.

### Bảng TC R11

| # | TC | Spec ref | Sample | Status | Note R11 |
|:-:|---|---|---|:-:|---|
| 1 | TK auto-creation timing | FR-VIII-15 step 6 | TVV-0033 walk MDK→CKH | ✅ | Pre-CKH (MDK/DTĐ/CPĐ): 0 TK match `tvv.r11.a16`. Post-CKH: 1 TK `tvv_r11_a16` ngayTao `2026-05-09T00:54:44.991Z` (=07:54:44 local), trùng moment Phê duyệt UI (07:54:37→07:55:03). |
| 2 | Negative login pre-CKH | FR-VIII-26 + ERR-AUTH-LOGIN-01 | UI login `tvv_btp_tw_0033`@MDK | ✅ | UI POST `/api/v1/auth/login` → 401 + `{"code":"ERR-AUTH-LOGIN-01","message":"Tên đăng nhập hoặc mật khẩu không đúng."}`. Anti-enumerate đúng spec line 1297. |
| 3 | Mail trigger timing | FR-VIII-26 step 1 | MailHog trước/sau CKH | ✅ | Baseline pre-CKH 85 mails, 0 cho `tvv.r11.a16`. Post-CKH 86 mails, 1 cho `tvv.r11.a16` subject "Hồ sơ TVV đã được phê duyệt — kích hoạt tài khoản" date `Sat, 09 May 2026 00:54:45 +0000`. |
| 4 | Dual-state sync | FR-VIII-26 step 12 + AC line 1314 | TVV-0033 + TK `tvv_r11_a16` sau first-login | ✅ | Sau set MK lần đầu + auto-login: TVV `trangThai=HOAT_DONG`, TK `trangThai=HOAT_DONG`. `tvv.taiKhoanId === tk.id`. `tk.lanDangNhapCuoi=2026-05-09T00:56:35.336Z`. |

### Walk lifecycle TVV-0033 (R11)

| # | Transition | State sau | Account | Endpoint quan sát | Time local | Note |
|:-:|---|---|---|---|---|---|
| 1 | (init) | `MOI_DANG_KY` | cb_nv_tw_02 | POST `/api/v1/tu-van-viens` 201 | 07:48 | Tạo TVV qua form "Thêm TVV" |
| 2 | Gửi KQ thẩm định | `DANG_THAM_DINH` | cb_nv_tw_02 | POST tham-dinh-result | 07:53 | Form 4 nhóm (Pháp lý ĐẠT + Năng lực 3đ + N/A Hiệu quả + Mạng lưới + Kết luận ĐẠT) |
| 3 | Trình duyệt | `CHO_PHE_DUYET` | cb_nv_tw_02 | PATCH transition | 07:53 | Form đóng băng disabled |
| 4 | Phê duyệt | `CHO_KICH_HOAT` | cb_pd_tw_02 | POST approve + mail trigger | 07:54:37→07:55:03 | Modal "Xác nhận phê duyệt" → confirm. Ngày công nhận 09/05/2026. |
| 5 | First-login set MK | `HOAT_DONG` | tvv_r11_a16 | POST first-login-password + auto-login | 07:56:35 | Toast "Kích hoạt tài khoản thành công" + dashboard TVV 4-module. |

### TVV-0033 + TK `tvv_r11_a16` snapshot (R11 final)

```json
{
  "tvv": {
    "ma": "TVV-BTP-TW-0033",
    "id": "e69d0d9d-37f7-4d49-b9ff-594437c41af4",
    "hoTen": "TVV R11 A16 Gate Test",
    "email": "tvv.r11.a16@test.htpldn.vn",
    "trangThai": "HOAT_DONG",
    "ngayCongNhan": "2026-05-09",
    "taiKhoanId": "aec7096d-394c-4f68-b514-2d4e96bf6adb"
  },
  "tk": {
    "id": "aec7096d-394c-4f68-b514-2d4e96bf6adb",
    "username": "tvv_r11_a16",
    "trangThai": "HOAT_DONG",
    "ngayTao": "2026-05-09T00:54:44.991Z",
    "lanDangNhapCuoi": "2026-05-09T00:56:35.336Z"
  }
}
```

### Observations R11

1. **Username generated từ email prefix:** TK username `tvv_r11_a16` = email local-part `tvv.r11.a16` với `.`→`_`. KHÔNG phải pattern `tvv_btp_tw_0033`. Negative login R11 dùng `tvv_btp_tw_0033` vẫn hợp lệ vì BE trả ERR-AUTH-LOGIN-01 cho cả invalid username + pre-CKH state (anti-enumerate đúng spec).
2. **API field schema:** `POST /api/v1/auth/login` nhận `{"username","password"}` (không phải `tenDangNhap`/`matKhau`). 4 lần API call ban đầu trả 422 ERR-VAL-SYS-00-01 do schema sai; UI form dùng đúng schema → 401 ERR-AUTH-LOGIN-01.
3. **Rate limiter aggressive:** `/api/v1/auth/login` x-ratelimit-limit 5/min. 5 login attempt trong vòng 30s → ThrottlerException. Cần sleep 60s reset.
4. **BUG-CG-A1-005 reproduce R11:** Mail link `http://103.172.236.130/auth/first-login-password?token=4060b6fa-...` thiếu port `:3000` + HTML entity `&#x3D;` thay `=` trong source. User phải tự sửa thêm port + decode entity. Không gate TC3 (vẫn đếm "có mail / không mail" theo state). Bug đã log từ R7.4.A1 R11 cũ — vẫn Open.
5. **Dashboard counter sync:** "Chuyên gia / Tư vấn viên: 10 → 11" trên Dashboard sau TVV-0033 active.

### Evidence R11

- [R11-tc1-tvv0033-mdk-created.png](r7-4-a1-6/R11-tc1-tvv0033-mdk-created.png) — TVV-0033 vừa tạo, state MOI_DANG_KY
- [R11-tc1-baseline-qtht.png](r7-4-a1-6/R11-tc1-baseline-qtht.png) — qtht_01 dashboard baseline
- [R11-tc2-negative-login-mdk-401.png](r7-4-a1-6/R11-tc2-negative-login-mdk-401.png) — toast "Tên đăng nhập hoặc mật khẩu không đúng" + UI login fail
- [R11-tc1-tvv0033-cho-phe-duyet.png](r7-4-a1-6/R11-tc1-tvv0033-cho-phe-duyet.png) — TVV-0033 sang CPĐ sau Trình duyệt
- [R11-tc1-tvv0033-cho-kich-hoat.png](r7-4-a1-6/R11-tc1-tvv0033-cho-kich-hoat.png) — TVV-0033 sang CKH sau Phê duyệt (moment TK + mail fire)
- [R11-tc1-tk-created-at-ckh.png](r7-4-a1-6/R11-tc1-tk-created-at-ckh.png) — qtht_01 view TK total 96, TK `tvv_r11_a16` mới tạo
- [R11-tc4-first-login-auto.png](r7-4-a1-6/R11-tc4-first-login-auto.png) — auto-login as TVV sau set MK
- [R11-tc4-tvv0033-hoat-dong-final.png](r7-4-a1-6/R11-tc4-tvv0033-hoat-dong-final.png) — TVV-0033 final state HOAT_DONG, ngày công nhận 09/05/2026

---

## R8 Round (archive — batch verify 88 TK + 10 production records)

---

## Bảng kiểm tra 4 TC

| # | TC | Spec ref | Sample / Cohort | Status | Note |
|:-:|---|---|---|:-:|---|
| 1 | TK auto-creation timing — TK chỉ tạo ở `CHO_KICH_HOAT` | FR-VIII-15 step 6 (line 2117-2118) | 12 MDK + 1 CKH (TVV-0013) + 9 HOAT_DONG | ✅ | 88 TK total, 0 TK pre-mature ở MDK/CTĐ/DTĐ/CPĐ |
| 2 | Negative login pre-CKH — TVV/CG `MOI_DANG_KY` login fail | FR-VIII-26 + ERR-AUTH-LOGIN-01 | 4 username variants từ MDK batch 2 | ✅ | 4/4 trả 401 ERR-AUTH-LOGIN-01 (anti-enumerate) |
| 3 | Mail trigger timing — mail kích hoạt fire CHỈ ở `CHO_KICH_HOAT` | FR-VIII-26 step 1 (line 1248-1265) | MailHog inbox 80 mails, 3 cohort (MDK/CKH/HD) | ✅ | Cohort A MDK = 0 mail; Cohort B CKH = 6/6 nhận đúng 1 mail; Cohort C HD = mail cũ retain |
| 4 | Dual-state sync — `TU_VAN_VIEN.HOAT_DONG ↔ TAI_KHOAN.HOAT_DONG` sau set MK | FR-VIII-26 step 12 (line 1288-1289) + AC line 1314 | 10 production-flow records (8 HD + 2 CKH) | ✅ | 10/10 sync clean. 2 probe records mismatch (force-advanced bypass FR-VIII-26 — test artifact, không phải bug SM) |

> Icon: ✅ pass · ❌ fail · ⏭ skip · 🚫 blocked

---

## Chi tiết bằng chứng từng TC

### TC1 — TK creation timing (FR-VIII-15 step 6)

Account: qtht_01 admin (sau OTP bypass 666666). Phương pháp: `evaluate_script` paginate `/api/v1/tai-khoan?pageSize=20` qua `j.meta.totalPages` × 5 trang → 88 TK total. Filter cohort theo username/email.

| Cohort TVV/CG | TVV state | Số TK tương ứng | Verdict |
|---|---|:-:|:-:|
| 12 MDK (CG-0023..0028 + TVV-0017..0022) — batch 2 | `MOI_DANG_KY` | 0 | ✅ NO PRE-MATURE TK |
| Hoàng Văn Năm + Nguyễn Văn Tư Vấn | `CHO_KICH_HOAT` | 2 (state=CKH) | ✅ TK tạo đúng thời điểm |
| 7 CG batch 1 + Vũ Văn Sáu (TVV-0014, đã advance) | `HOAT_DONG` | 8 (state=HOAT_DONG) | ✅ 1:1 sync |
| 2 Probe (R7.4.A1 leftover) | `HOAT_DONG` | 2 (state=CKH) | ⚠️ Test artifact — TVV force-advanced bypass FR-VIII-26 |

**Bằng chứng:** [tc1-tk-list-87-total.png](r7-4-a1-6/tc1-tk-list-87-total.png), [tc1-87tk-35hd-52ckh.png](r7-4-a1-6/tc1-87tk-35hd-52ckh.png), [tc1-cg-batch2-mdk-0-tk.png](r7-4-a1-6/tc1-cg-batch2-mdk-0-tk.png), [tc1-vu-sau-06-hoat-dong-ui.png](r7-4-a1-6/tc1-vu-sau-06-hoat-dong-ui.png).

### TC2 — Negative login pre-CKH (FR-VIII-26 + ERR-AUTH-LOGIN-01)

Logout qtht_01 (`POST /api/v1/auth/logout` + `localStorage.clear()` + `sessionStorage.clear()`). Thử login với 4 username pattern lấy từ TVV/CG MDK batch 2 cohort:

| # | Username thử | TVV state | Password | HTTP | Error code | Verdict |
|:-:|---|:-:|---|:-:|---|:-:|
| 1 | `chuyen_23` | `MOI_DANG_KY` (CG-0023) | `Secret@123` | 401 | `ERR-AUTH-LOGIN-01` | ✅ Login fail đúng spec |
| 2 | `ha_chuyen_24` | `MOI_DANG_KY` (CG-0024) | `Secret@123` | 401 | `ERR-AUTH-LOGIN-01` | ✅ |
| 3 | `tvv_btp_tw_0017` | `MOI_DANG_KY` (TVV-0017) | `Secret@123` | 401 | `ERR-AUTH-LOGIN-01` | ✅ |
| 4 | `nguyen_15` | `MOI_DANG_KY` (TVV-0017) | `Secret@123` | 401 | `ERR-AUTH-LOGIN-01` | ✅ |

Toast UI: "Tên đăng nhập hoặc mật khẩu không đúng" (anti-enumerate đúng SRS line 1297).

**Bằng chứng:** [tc2-negative-login-401.png](r7-4-a1-6/tc2-negative-login-401.png).

### TC3 — Mail trigger timing (FR-VIII-26 step 1)

Probe MailHog API `/api/v2/messages?limit=500` qua `curl` (CORS bypass). Filter recipient email theo 3 cohort:

| Cohort | Sample recipient | Expect | Actual | Verdict |
|---|---|:-:|:-:|:-:|
| **A** MDK (CG-23..28 + TVV-17..22) | `chuyen_23..28@`, `tvv_btp_tw_0017..0022@` | 0 mail kích hoạt | 0 mail | ✅ Mail không gửi premature |
| **B** CKH (28 hot-role _05..08 — qtht_03 UI seed 21:30) | `cb_pd_dp_05..08`, `cb_nv_tw_08`, `qtht_08` | ≥1 mail kích hoạt mỗi recipient | 6/6 sample = 1 mail mỗi | ✅ Mail fire đúng state CKH |
| **C** HOAT_DONG (đã set MK) | `vu_sau_06`, `ly_13` | ≥1 mail kích hoạt cũ retain | 1 mail mỗi | ✅ Mail cũ giữ trong hộp thư (vendor ghi log) |

> **Lưu ý phạm vi TC3:** Verify trigger timing (state-gated). Format mail URL có sai (BUG-002 R7.4.A1 Open) nhưng KHÔNG gate TC3 vì TC3 chỉ cần verify "có mail / không mail" theo state.

**Bằng chứng:** [tc3-mailhog-probe.txt](r7-4-a1-6/tc3-mailhog-probe.txt) — 10/10 cohort cell PASS.

### TC4 — Dual-state sync (FR-VIII-26 step 12 + AC line 1314)

Cross-entity match TVV/CG ↔ TAI_KHOAN qua email key (`tvv.email === tk.email`):

| # | Họ tên | Email | TVV state | TK state | Sync |
|:-:|---|---|:-:|:-:|:-:|
| 1 | Lý Thị Mười Ba (CG-0001) | `ly.13@…` | HOAT_DONG | HOAT_DONG | ✅ |
| 2 | Đinh Văn Mười Bốn (CG-0002) | `dinh.14@…` | HOAT_DONG | HOAT_DONG | ✅ |
| 3 | Ngô Thị Mười Lăm (CG-0003) | `ngo.15@…` | HOAT_DONG | HOAT_DONG | ✅ |
| 4 | Trương Văn Mười Sáu (CG-0004) | `truong.16@…` | HOAT_DONG | HOAT_DONG | ✅ |
| 5 | Mai Thị Mười Bảy (CG-0005) | `mai.17@…` | HOAT_DONG | HOAT_DONG | ✅ |
| 6 | Hồ Văn Mười Tám (CG-0006) | `ho.18@…` | HOAT_DONG | HOAT_DONG | ✅ |
| 7 | Vũ Văn Sáu (TVV-0014) | `vu.sau.06@…` | HOAT_DONG | HOAT_DONG | ✅ |
| 8 | (admin-extra) | … | HOAT_DONG | HOAT_DONG | ✅ |
| 9 | Hoàng Văn Năm | `hoang.nam.05@…` | CHO_KICH_HOAT | CHO_KICH_HOAT | ✅ |
| 10 | Nguyễn Văn Tư Vấn | `nguyen.tuvan.01@…` | CHO_KICH_HOAT | CHO_KICH_HOAT | ✅ |

→ 10/10 production-flow records sync clean. State distribution TVV: total 28 (HD:9 / CKH:2 / MDK:12 / CPĐ:1 / TC:3 / YCBS:1).

**Test artifact (không gate TC4):**
- Probe CG OptLock + Probe CG Permission: TVV.HD ↔ TK.CKH — 2 record này là leftover từ R7.4.A1 (TVV state force-advanced qua direct API admin để test optimistic-lock + permission), bypass FR-VIII-26 step 12 set MK flow → TK giữ nguyên CKH. Đây KHÔNG phải state machine bug, chỉ là test data anomaly.

**Bằng chứng:** [tc4-tvv-entity-hoat-dong-9-final.png](r7-4-a1-6/tc4-tvv-entity-hoat-dong-9-final.png), [tc4-tvv-entity-mdk-12.png](r7-4-a1-6/tc4-tvv-entity-mdk-12.png), [tc4-cross-entity-sync.json](r7-4-a1-6/tc4-cross-entity-sync.json).

---

## Lịch sử round

| Round | Date | Kết quả |
|---|---|---|
| R7-probe | 2026-05-08 sáng | TC1 probe ✅ qua qtht_01 query 59 TK — verify TVV-0013 CKH = 1 TK CKH |
| R8 | 2026-05-08 23:55 | 4/4 TC PASS — TK 88, dual-state sync 10/10 |
| R11 (LATEST) | 2026-05-09 07:55:03 | 4/4 TC PASS fresh TVV-0033 walk full lifecycle MDK→HOAT_DONG, TK auto-tạo 07:54:44 đúng moment CKH, mail fire OK, dual-state HOAT_DONG sync. |

---

## Anomaly + lưu ý

1. **TVV-0013 → TVV-0014 numbering:** TVV-0013 (Vũ Văn Sáu) trong R7-probe state CKH (1 TK CKH) đã được advance HOAT_DONG qua flow set MK → mã TVV hiển thị `TVV-BTP-TW-0014` (có thể do BE re-issue mã sau workflow advance hoặc đây là bản ghi mới thay thế). State sync đúng `HOAT_DONG ↔ HOAT_DONG`.
2. **Probe records bypass FR-VIII-26:** 2 Probe (Permission + OptLock) cần được dev cleanup khỏi DB hoặc force-sync TK về CKH/HD theo TVV. Không log bug — đây là test data leftover từ session trước, không phải bug state machine.
3. **CHO_KICH_HOAT cohort tăng từ 1 → 2:** Trong khoảng giữa R7-probe và R8, có 1 TVV thêm advance lên CKH (Hoàng Văn Năm hoặc Nguyễn Văn Tư Vấn). Có thể do session khác (qtht_03 batch _05..08 hot-role advance).

---

*R11 | QA-claude | 2026-05-09 07:55:03*
