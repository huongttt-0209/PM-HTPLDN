# Workflow test report — R7.4.A2 Tiếp nhận TVV (3 transition entry/loop)

**Ngày chạy:** 2026-05-10 R21 (LATEST — UI re-verify BUG-002 + BUG-003, không API direct; vẫn Open) · 2026-05-09 23:50:00 (R20 — re-verify BUG-002 + BUG-003 sau ~25min, identical R19 dev chưa fix; bonus full A2.1 fresh walk TVV-0019) · 2026-05-09 23:25:00 (R19 — verify dev fix BUG-001 perm gap closed, phát hiện 2 bug mới BE+FE) · 2026-05-09 22:39:25 (R18 — quick verify dev fix nht_01 identical R17) · 2026-05-09 21:18:22 (R17 — cross-account verify 4 NHT identical loại trừ per-user) · 2026-05-09 21:06:35 (R16 — quick verify dev fix sau R15 unchanged) · 2026-05-09 20:00:18 (R15 — re-verify BUG-001 sau clear cache toàn bộ client-side) · 2026-05-09 19:50:19 (R14 — re-verify BUG-001 unchanged sau ~5h25min từ R13) · 2026-05-09 14:25:00 (R13 — verify BUG-001 still open + seed TU_CHOI pool) · 2026-05-09 10:55:00 (R12b — bug NHT perm gap) · 2026-05-09 09:40:00 (R12 walk TVV-0017) · 2026-05-07 R7 (archive)
**Account:** `cb_nv_tw_01` (Secret@123, OTP 666666) — chip role CB_PD_TW (dual permission); `nht_04_ui` (BTP-TW) cho A2.2/A2.3 path b
**SRS ref:** SM-TVV v3.5 line 2304-2319 ([smoke/6.4-sm-tvv.md](../../../../smoke/6.4-sm-tvv.md)) · FR-IV-06 line 483-551 (Thẩm định) · FR-IV-04 line 360-410 (Cập nhật năng lực — actor = NHT) · FR-IV-03 line 273-358 (Đăng ký TVV qua NHT — actor = NHT/CB NV)
**Scope:** 3 transition entry hoặc loop ngược về CHO_THAM_DINH/DANG_THAM_DINH
- A2.1 — `MOI_DANG_KY → CHO_THAM_DINH` (CB NV vào tab Thẩm định bắt đầu chấm, ngầm transition; BE skip CTD → đi thẳng DTD)
- A2.2 — `YEU_CAU_BO_SUNG → DANG_THAM_DINH` (NHT cập nhật năng lực FR-IV-04 step 7)
- A2.3 — `TU_CHOI → CHO_THAM_DINH` (NHT/CB nộp lại hồ sơ, không cooldown)

## Verdict

⚠️ **MỘT PHẦN** — 1/3 ✅ Đạt + 2/3 ❌ Lỗi sau R21 UI re-verify. R21 2026-05-10 qua browser UI, không API direct: A2.2 `nht_04_ui` cập nhật năng lực TVV-BTP-TW-0017 xong badge vẫn `Yêu cầu bổ sung` → BUG-TVV-A2-002 vẫn Open; A2.3 list NHT vẫn không có entry `Thêm mới`/`Đăng ký TVV` và route `/chuyen-gia-tvv/dang-ky` vẫn `ERR-HS-01` → BUG-TVV-A2-003 vẫn Open. BUG-TVV-A2-001 vẫn ✅ Closed. Tổng 1/3 PASS giữ nguyên, 2 bug Open Major.

## R21 Round (LATEST — 2026-05-10 — UI re-verify BUG-002 + BUG-003)

User chỉ định verify qua browse/UI, không chạy API. Re-test tập trung vào 2 bug còn Open sau R20.

### A2.2 R21 re-verify BUG-TVV-A2-002 — ❌ Lỗi

| Step | Action | Result |
|---|---|---|
| 1 | Login `nht_04_ui` qua browser UI → `/chuyen-gia-tvv/danh-sach` → tab `Yêu cầu bổ sung` | Có TVV-BTP-TW-0017 + TVV-BTP-TW-0010 |
| 2 | Mở TVV-BTP-TW-0017 → tab `Năng lực` → `Cập nhật năng lực` → `Lưu` bằng form UI | Save xong quay về detail |
| 3 | Quan sát header detail | Badge vẫn `Yêu cầu bổ sung`, không chuyển `Đang thẩm định` |

→ **BUG-TVV-A2-002 vẫn Open Major** — FR-IV-04 step 7 chưa tự transition `YEU_CAU_BO_SUNG → DANG_THAM_DINH` sau khi lưu năng lực bằng UI.

**Evidence:** [R21-2026-05-10-nht-ycbs-list-regex-tab.png](../../bug-reports/tu-van-vien-cg/evidence-r7-4-a2-nht-perm/R21-2026-05-10-nht-ycbs-list-regex-tab.png) + [R21-2026-05-10-tvv-btp-tw-0017-nang-luc-after-save-regex.png](../../bug-reports/tu-van-vien-cg/evidence-r7-4-a2-nht-perm/R21-2026-05-10-tvv-btp-tw-0017-nang-luc-after-save-regex.png)

### A2.3 R21 re-verify BUG-TVV-A2-003 — ❌ Lỗi

| Step | Action | Result |
|---|---|---|
| 1 | Login `nht_04_ui` → `/chuyen-gia-tvv/danh-sach` | Không có `Thêm mới` / `Thêm TVV` / `Đăng ký TVV` / `Tạo hồ sơ` |
| 2 | Navigate `/chuyen-gia-tvv/dang-ky` qua browser UI | Page hiển thị `Hồ sơ TVV không tồn tại`, `ERR-HS-01` |

→ **BUG-TVV-A2-003 vẫn Open Major** — NHT vẫn không có entry point đăng ký/nộp lại hồ sơ TVV.

**Evidence:** [R21-2026-05-10-nht-list-no-create-button.png](../../bug-reports/tu-van-vien-cg/evidence-r7-4-a2-nht-perm/R21-2026-05-10-nht-list-no-create-button.png) + [R21-2026-05-10-nht-dang-ky-route-regex.png](../../bug-reports/tu-van-vien-cg/evidence-r7-4-a2-nht-perm/R21-2026-05-10-nht-dang-ky-route-regex.png)

## R20 Round (2026-05-09 23:50:00 — re-verify BUG-002 + BUG-003 + bonus A2.1 fresh walk TVV-0019)

### Scope R20 (Re-verify 2 bug mới + full A2.1 fresh evidence)

User chỉ định: "Verify 2 bug + re-walk full A2.1 fresh evidence" — verify dev có push fix BUG-002 + BUG-003 trong window ~25min sau R19 (23:25:00 → 23:50:00) hay không. Đồng thời chạy A2.1 fresh với TVV-0019 (record MDK chưa từng walk) để có evidence độc lập với TVV-0017 R12.

### A2.1 R20 Walk fresh TVV-0019 — ✅ Đạt (re-verify ổn định)

| Step | Action | Result |
|---|---|---|
| 1 | Spawn isolated context `qa_r20_a2_cbnv_walk` + login `cb_nv_tw_01` (CB_PD_TW dual perm) | OK, role CB_PD_TW |
| 2 | Navigate `/chuyen-gia-tvv/danh-sach` → tab "Mới đăng ký" 12 records | OK 12 MDK visible |
| 3 | Click row TVV-BTP-TW-0019 (Lê Thị Tư Vấn 17) → detail page `/chuyen-gia-tvv/{uuid}` | OK badge "Mới đăng ký" |
| 4 | Click tab "Thẩm định" → fill Pháp lý=Đạt + Kết luận=ĐẠT → click "Lưu nháp" | POST `/api/v1/tu-van-viens/{id}/tham-dinh` reqid=226 **200 OK** |
| 5 | Reload detail → verify badge | **State badge changed `Mới đăng ký` → `Đang thẩm định`** ✅ |
| 6 | GET detail | `trangThai="DANG_THAM_DINH", version=2` ✅ — BE skip CHO_THAM_DINH đúng spec line 66 + SCR-IV-03 + FR-IV-04 line 396-398 |

→ **A2.1 ✅ Đạt** — fresh evidence với TVV-0019 (record khác TVV-0017 R12) confirm transition stable. State machine MDK→DTD ngầm pass đúng SRS.

**Evidence:** [R20-tvv0019-mdk-to-dtd-skip-ctd.png](../../bug-reports/tu-van-vien-cg/evidence-r7-4-a2-nht-perm/R20-tvv0019-mdk-to-dtd-skip-ctd.png)

### A2.2 R20 re-verify BUG-TVV-A2-002 — ❌ Lỗi (identical R19, dev chưa fix)

| Step | Action | Result |
|---|---|---|
| 1 | Spawn isolated context `qa_r20_a2_nht_verify` + login `nht_04_ui` (NHT-BTP-TW-0001, BTP-TW, TW) | OK, role NHT |
| 2 | GET `/api/v1/auth/me` | 200 — **perms_count=32 identical R19** (perm fix BUG-001 vẫn giữ, không regression) |
| 3 | Inspect perm list | `tvv_perms=[bo-sung_tu_van_vien, read_tu_van_vien, register_tu_van_vien, update_tu_van_vien]` ✅ identical R19 |
| 4 | Navigate detail TVV-BTP-TW-0017 (YEU_CAU_BO_SUNG, version=5 từ R19) | OK render |
| 5 | Click tab Năng lực → "Cập nhật năng lực" → đổi Chuyên ngành "LS-HN-2020-001-R19-UPDATED" → "LS-HN-2020-001-R20-UPDATED" → click Lưu | PATCH `/api/v1/tu-van-viens/{id}/nang-luc` reqid=231 **200 OK** ✅ |
| 6 | Reload detail → verify badge state | **Badge vẫn "Yêu cầu bổ sung"** ❌ |
| 7 | GET detail | `trangThai="YEU_CAU_BO_SUNG", version=6` (version increment 5→6 confirm PATCH applied; state KHÔNG transition) |

→ **BUG-TVV-A2-002 vẫn Open Major identical R19** — BE FR-IV-04 step 7 logic vẫn KHÔNG trigger auto-transition `YEU_CAU_BO_SUNG → DANG_THAM_DINH` sau PATCH /nang-luc 200. Dev chưa push BE fix trong window R19 → R20 (~25min).

**Evidence:** [R20-tvv0017-state-not-transitioned-after-nang-luc-update.png](../../bug-reports/tu-van-vien-cg/evidence-r7-4-a2-nht-perm/R20-tvv0017-state-not-transitioned-after-nang-luc-update.png)

### A2.3 R20 re-verify BUG-TVV-A2-003 — ❌ Lỗi (identical R19, dev chưa fix)

| Step | Action | Result |
|---|---|---|
| 1 | NHT navigate `/chuyen-gia-tvv/danh-sach` (cùng context `qa_r20_a2_nht_verify`) | OK render |
| 2 | Inspect toàn page list — tìm button "Thêm mới" / "Đăng ký TVV" / icon "+" | **KHÔNG có** — chỉ có filter + tabs + per-row Sao chép/Xem/Sửa/Xóa identical R19 |
| 3 | Click tab "Từ chối" → render TU_CHOI records | OK 5 records bao gồm TVV-BTP-TW-0018 |
| 4 | Click row TVV-0018 link "Xem" → navigate detail `/chuyen-gia-tvv/37f69293-9542-4ac9-bdbc-a848e5332e42` | OK badge "Từ chối", tab "Thẩm định" disabled (đúng spec) |
| 5 | Inspect detail page — tìm button "Đăng ký lại" / "Re-submit" | **KHÔNG có** — chỉ có "Sửa hồ sơ" identical R19 |
| 6 | URL probe `/chuyen-gia-tvv/dang-ky` | **404 ERR-HS-01 "Hồ sơ TVV không tồn tại"** identical R19 |

→ **BUG-TVV-A2-003 vẫn Open Major identical R19** — FE vẫn thiếu UI entry point đăng ký TVV cho NHT (button list page + button detail TU_CHOI + route `/dang-ky` đều missing). Dev chưa push FE fix trong window R19 → R20 (~25min).

**Evidence:** [R20-dang-ky-route-404-fe-missing.png](../../bug-reports/tu-van-vien-cg/evidence-r7-4-a2-nht-perm/R20-dang-ky-route-404-fe-missing.png)

### R20 Pool sau verify

| Mã | Tên | State trước R20 | State sau R20 | Note |
|---|---|---|---|---|
| TVV-BTP-TW-0019 | Lê Thị Tư Vấn 17 | MOI_DANG_KY | DANG_THAM_DINH | R20 walk A2.1 — MDK→DTD verified, fresh independent evidence từ TVV-0017 |
| TVV-BTP-TW-0017 | Nguyễn Văn Tư Vấn 15 | YEU_CAU_BO_SUNG (v5) | YEU_CAU_BO_SUNG (v6) | R20 PATCH /nang-luc 200, version increment, state unchanged (BUG-002 reproduce) |
| TVV-BTP-TW-0018 | Trần Thị Tư Vấn 16 | TU_CHOI | TU_CHOI | R20 không attempt PATCH (chỉ inspect UI), state giữ |

Pool count post-R20: Mới đăng ký 11 (-1) / Đang thẩm định 1 (+1) / Yêu cầu bổ sung 2 / Từ chối 5.

### R20 Outcome summary

- A2.1 ✅ Đạt — fresh walk TVV-0019 confirm transition MDK→DTD stable (independent evidence từ TVV-0017 R12).
- A2.2 ❌ BUG-TVV-A2-002 **vẫn Open Major** — dev chưa push BE fix step 7 state transition trong window 25 phút.
- A2.3 ❌ BUG-TVV-A2-003 **vẫn Open Major** — dev chưa push FE fix UI entry point trong window 25 phút.
- BUG-TVV-A2-001 vẫn ✅ Closed (perm fix R19 hold, không regression).
- **Tổng kết R20:** 1/3 PASS giữ nguyên, 2 bug Open Major. Cần dev push fix BUG-002 + BUG-003 rồi re-test R21.

---

## R19 Round (2026-05-09 23:25:00 — verify dev fix BUG-001 + phát hiện 2 bug mới)

### Scope R19 (Verify dev fix sau R18 — full re-run A2.2 + A2.3 path b)

User báo "dev vừa confirm đã fix" → R19 chạy lại A2.2 + A2.3 path b với `nht_04_ui` (NHT-BTP-TW-0001, BTP-TW, TW) trong isolated context `qa_r19_a2_dev_fix_verify`. Mục tiêu: xác nhận BUG-001 closed + nếu pass thì hoàn thành 3/3 transition.

### A2.1 R19 status — ✅ Đạt (no re-test, R12 evidence kept)

A2.1 đã ✅ Đạt sau R12 fresh walk TVV-0017. R19 không re-walk vì state machine path không thay đổi.

### A2.2 R19 verify FR-IV-04 step 7 — ❌ Lỗi (BUG-001 closed nhưng phát hiện BUG-002 mới)

| Step | Action | Result |
|---|---|---|
| 1 | Spawn isolated context `qa_r19_a2_dev_fix_verify` + login `nht_04_ui` (BTP-TW, TW, Secret@123 + OTP 666666) | OK, role NHT |
| 2 | GET `/api/v1/auth/me` | 200 — **perms_count=32 (+7 từ baseline 25 R12b/.../R18)** ✅ dev fix verified |
| 3 | Inspect perm list | perms_tvv_related đã có `read_tu_van_vien` + `update_tu_van_vien` (mới) + giữ `bo-sung_tu_van_vien` + `register_tu_van_vien` |
| 4 | GET `/api/v1/tu-van-viens?page=0&size=10` | **200 OK** ✅ (R18 trước đó 403) — list TVV trả về |
| 5 | GET TVV-0017 detail (state hiện tại `YEU_CAU_BO_SUNG`, version=4) | OK, hiển thị form Năng lực với button "Cập nhật năng lực" |
| 6 | Click "Cập nhật năng lực" → đổi field "Chuyên ngành" → "LS-HN-2020-001-R19-UPDATED" → submit | PATCH `/api/v1/tu-van-viens/{id}/nang-luc` **200 OK** ✅ (data persist verified GET sau đó) |
| 7 | Reload trang detail TVV-0017 → verify state badge + GET trangThai | **State badge "Yêu cầu bổ sung"** ❌ — GET trả `trangThai="YEU_CAU_BO_SUNG", version=5` |

→ **BUG-TVV-A2-001 ✅ Closed** (perm gap đã fix, NHT có thể GET + PATCH thành công). **Phát hiện BUG-TVV-A2-002 mới**: BE FR-IV-04 step 7 logic không trigger — sau khi NHT cập nhật năng lực thành công (PATCH 200), state KHÔNG tự transition về `DANG_THAM_DINH` như spec yêu cầu (line 398, line 408, SM line 2308).

**Spec quote (FR-IV-04 line 398, 408):**
> Bước 7: Nếu TVV đang ở `YEU_CAU_BO_SUNG` và có cập nhật hồ sơ → chuyển trạng thái về `DANG_THAM_DINH`.

**Evidence:** [R19-tvv0017-state-not-transitioned-after-nang-luc-update.png](../../bug-reports/tu-van-vien-cg/evidence-r7-4-a2-nht-perm/R19-tvv0017-state-not-transitioned-after-nang-luc-update.png)

### A2.3 R19 verify path b (NHT đăng ký lại) — 🚫 Không test được (phát hiện BUG-003 mới)

| Step | Action | Result |
|---|---|---|
| 1 | Login `nht_04_ui` perms_count=32 đã có `register_tu_van_vien` | OK |
| 2 | Tìm UI entry "Đăng ký TVV" / "Tạo TVV mới" trên sidebar + dashboard NHT | Không có |
| 3 | Probe trực tiếp 3 URL ứng viên: `/tu-van-vien/dang-ky`, `/tu-van-vien/them-moi`, `/tu-van-vien/dang-ky-tvv` | Tất cả 404 |
| 4 | Tìm trên trang detail TVV-0018 (TU_CHOI) — có button "Đăng ký lại" / "Nộp lại hồ sơ" cho NHT? | Không có (tab "Từ chối" chỉ hiển thị info read-only) |

→ **BUG-TVV-A2-003 mới**: FE thiếu UI entry point cho NHT đăng ký TVV mới (path b FR-IV-03). NHT đã có perm BE (`register_tu_van_vien`) nhưng không có route/button để invoke.

Path (a) chủ hồ sơ tự nộp lại — TVV-0018 CB-tạo không có TK (TK auto-tạo ở `CHO_KICH_HOAT` per FR-VIII-26), không thể test path a.

**Evidence:** [R19-tvv0018-tuchoi-no-dangky-button-fe-missing.png](../../bug-reports/tu-van-vien-cg/evidence-r7-4-a2-nht-perm/R19-tvv0018-tuchoi-no-dangky-button-fe-missing.png)

### R19 Pool sau verify

Pool TVV: TVV-0017 vẫn `YEU_CAU_BO_SUNG` (PATCH năng lực đã apply, version 4→5, nhưng state không transition theo spec). TVV-0018 vẫn `TU_CHOI`. Tổng state count post-R19 identical R18 baseline (TVV total 18, TU_CHOI:4, YEU_CAU_BO_SUNG:2, không thay đổi vì BE không transition).

### R19 Outcome summary

- BUG-TVV-A2-001 (BE perm gap): ✅ **Closed** — dev fix verified perms_count 25→32, NHT có `read_tu_van_vien` + `update_tu_van_vien`.
- BUG-TVV-A2-002 (BE FR-IV-04 step 7 state transition broken): **Open Major** — log mới R19, block A2.2.
- BUG-TVV-A2-003 (FE missing đăng ký TVV entry cho NHT): **Open Major** — log mới R19, block A2.3 path b.
- Tổng kết: 1/3 transition pass (A2.1), 2/3 vẫn không pass nhưng do bug khác (không phải perm gap nữa).

---

## R18 Round (2026-05-09 22:39:25 — quick verify dev fix sau R17)

### Scope R18 (Quick verify ~5 phút)

User yêu cầu chạy lại R7.4.A2 cẩn thận sau R17. R17 (21:18:22) đã loại trừ per-user / per-đơn vị / per-cấp với cross-account 4 NHT. R18 chạy sau ~1h21min với `nht_01` (NHT đầu tiên trong R17 sample) để check dev có push fix BE permission seed trong window R17 → R18 hay không. Nếu fix → run A2.2 + A2.3 path (b). Nếu không → kết luận identical, đóng nhanh.

### A2.1 R18 status — ✅ Đạt (no re-test, R12 evidence kept)

A2.1 đã ✅ Đạt sau R12 fresh walk TVV-0017. R13/R14/R15/R16/R17/R18 không re-walk vì transition đã verify ổn định + state machine path không thay đổi. Evidence + spec compliance giữ từ R12.

### A2.2 R18 verify BUG-TVV-A2-001 — 🚫 Không test được (bug vẫn open)

| Step | Action | Result |
|---|---|---|
| 1 | Spawn isolated context `qa_r18_a2_nht01_verify` + login `nht_01` (Phùng Thị NHT An Giang, STP-AG, DP, Secret@123 + OTP 666666) → landing `/dao-tao/chuong-trinh/danh-sach` | OK, role NHT, donVi `00000000-0000-4000-8002-000000000006` STP-AG |
| 2 | GET `/api/v1/auth/me` | 200 — **perms_count=25 identical R17/R16/R15/R14/R13/R12b** |
| 3 | Inspect perm list | perms_tvv_related vẫn `[bo-sung_tu_van_vien, register_tu_van_vien]` — **vẫn thiếu** `read_tu_van_vien`, `update_tu_van_vien`, `update-nang-luc_tu_van_vien` |
| 4 | GET `/api/v1/tu-van-viens?page=0&size=10` | **403 ERR-PERM-SYS-00-01 "Forbidden"** ❌ identical (requestId 9620d97a-bb1d-464b-9fd7-72ad654b9c62) |
| 5 | PATCH `/api/v1/tu-van-viens/00000000-0000-0000-0000-000000000999/nang-luc` | **403 ERR-PERM-SYS-00-01 "Forbidden"** ❌ identical (requestId 2db2dbd0-ad03-490e-bfd6-809d0736f5a0) |

→ **BUG-TVV-A2-001 confirmed reproduce 7 round consecutive (R12b/R13/R14/R15/R16/R17/R18)**. Dev chưa push fix BE permission seed trong window R17 → R18 (~1h21min).

**Evidence:** [R18-nht01-perms-25-403-still-open.png](../../bug-reports/tu-van-vien-cg/evidence-r7-4-a2-nht-perm/R18-nht01-perms-25-403-still-open.png)

### A2.3 R18 status — 🚫 Không test được (block 2 path identical R17)

Path (a) chủ hồ sơ tự nộp lại — TVV-0018 CB-tạo không có TK, R18 không seed thêm. Path (b) NHT đăng ký lại — block bởi BUG-TVV-A2-001 confirmed identical R18. Pool TU_CHOI vẫn 1 record (TVV-0018), unchanged R14/R15/R16/R17/R18.

### R18 Pool sau verify

Pool TVV unchanged R18 — không advance state, chỉ verify API permission. State count post-R18 identical R17 baseline (TVV total 18, TU_CHOI:4, YEU_CAU_BO_SUNG:2).

## R17 Round (2026-05-09 21:18:22 — cross-account verify 4 NHT identical)

### Scope R17 (Cross-account verify — ~12 phút)

User phản biện: "lỡ nguyên nhân do tài khoản thì sao?" → R12-R16 đều dùng `nht_04_ui` (R12 dùng nht_01) — chưa loại trừ per-user misconfig. R17 probe 3 NHT khác để build n=4 sample.

### A2.1 R17 status — ✅ Đạt (no re-test, R12 evidence kept)

A2.1 đã ✅ Đạt sau R12 fresh walk TVV-0017. R13/R14/R15/R16/R17 không re-walk vì transition đã verify ổn định + state machine path không thay đổi. Evidence + spec compliance giữ từ R12.

### A2.2 R17 cross-account verify — 🚫 Không test được (role-wide confirmed)

| # | Account | hoTen | donVi | capDonVi | perms_count | tvv_perms | GET /tu-van-viens | PATCH /nang-luc |
|---|---|---|---|---|---|---|---|---|
| 1 | `nht_01` | Phùng Thị NHT An Giang | STP-AG | DP | **25** | 2 (bo-sung + register) | **403 ERR-PERM-SYS-00-01** | **403 ERR-PERM-SYS-00-01** |
| 2 | `nht_02` | Lương Văn NHT Đà Nẵng | STP-DN | DP | **25** | 2 identical | **403 ERR-PERM-SYS-00-01** | **403 ERR-PERM-SYS-00-01** |
| 3 | `nht_03` | Đào Thị NHT Hải Phòng | STP-HP | DP | **25** | 2 identical | **403 ERR-PERM-SYS-00-01** | **403 ERR-PERM-SYS-00-01** |
| 4 | `nht_04_ui` (R16) | NHT-BTP-TW-0001 | BTP-TW | TW | **25** | 2 identical | **403 ERR-PERM-SYS-00-01** | **403 ERR-PERM-SYS-00-01** |

→ **4 NHT × 4 đơn vị × 2 cấp (3 DP + 1 TW) đều identical** → bug **100% role-wide BE permission seed gap**, loại trừ:
- per-user misconfig (4 user khác nhau, kết quả identical)
- per-đơn vị scope (4 đơn vị khác nhau STP-AG/STP-DN/STP-HP/BTP-TW)
- per-cấp drift (3 DP + 1 TW đều giống)
- FE cache stale (đã loại trừ R15 + 4 isolated context riêng R17)

→ **BUG-TVV-A2-001 confirmed reproduce 6 round consecutive (R12b/R13/R14/R15/R16/R17)** qua 4 method. Fix BẮT BUỘC ở BE side: bổ sung perm `read_tu_van_vien`, `update_tu_van_vien`, `update-nang-luc_tu_van_vien` vào DB role-permission mapping của role NHT.

**Evidence:** [R17-cross-account-4nht-identical-perms-25.png](../../bug-reports/tu-van-vien-cg/evidence-r7-4-a2-nht-perm/R17-cross-account-4nht-identical-perms-25.png)

### A2.3 R17 status — 🚫 Không test được (block 2 path identical R16)

Path (a) chủ hồ sơ tự nộp lại — TVV-0018 CB-tạo không có TK (TK auto-tạo ở CHO_KICH_HOAT per FR-VIII-26), R17 không seed thêm. Path (b) NHT đăng ký lại — block bởi BUG-TVV-A2-001 confirmed identical R17 (4 NHT đều thiếu perm). Pool TU_CHOI vẫn 1 record (TVV-0018 seeded R13), unchanged R14/R15/R16/R17.

### R17 Pool sau verify

Pool TVV unchanged R17 — không advance state, chỉ verify API permission cross-account. State count post-R17 identical R16 baseline (TVV total 18, TU_CHOI:4, YEU_CAU_BO_SUNG:2).

## R16 Round (2026-05-09 21:06:35 — quick verify dev fix sau R15)

### Scope R16 (Quick verify ~10 phút)

User yêu cầu chạy lại R7.4.A2 sau R15. R15 (20:00:18) đã loại trừ FE-side cache với clear cache toàn bộ client-side, kết luận bug 100% server-side. R16 chạy sau ~1h06min để check dev có push fix BE permission seed trong window R15 → R16 hay không. Nếu fix → run A2.2 + A2.3 path (b). Nếu không fix → kết luận identical, đóng nhanh.

### A2.1 R16 status — ✅ Đạt (no re-test, R12 evidence kept)

A2.1 đã ✅ Đạt sau R12 fresh walk TVV-0017. R13/R14/R15/R16 không re-walk vì transition đã verify ổn định + state machine path không thay đổi. Evidence + spec compliance giữ từ R12.

### A2.2 R16 verify BUG-TVV-A2-001 — 🚫 Không test được (bug vẫn open)

| Step | Action | Result |
|---|---|---|
| 1 | Spawn isolated context `qa_r16_a2_nht04_verify` + login `nht_04_ui` (Secret@123 + OTP 666666) → landing `/dao-tao/chuong-trinh/danh-sach` | OK, role NHT |
| 2 | GET `/api/v1/auth/me` | 200 — **perms_count=25 identical R15/R14/R13/R12b** |
| 3 | Inspect perm list | perms_tvv_related vẫn `[bo-sung_tu_van_vien, register_tu_van_vien]` — **vẫn thiếu** `read_tu_van_vien`, `update_tu_van_vien`, `update-nang-luc_tu_van_vien` |
| 4 | GET `/api/v1/tu-van-viens?page=0&size=10` | **403 ERR-PERM-SYS-00-01 "Forbidden"** ❌ identical (requestId 2b0b5da2-22c6-4b70-9d23-7bb292b1f23c) |
| 5 | PATCH `/api/v1/tu-van-viens/00000000-0000-0000-0000-000000000999/nang-luc` | **403 ERR-PERM-SYS-00-01 "Forbidden"** ❌ identical |
| 6 | Sidebar render → liệt kê 7 items | `[Quản lý đào tạo, tập huấn▶, Chương trình đào tạo, Khóa học, Kho tài liệu / Bài giảng, Quản lý vụ việc hỗ trợ pháp lý, Quản lý tư vấn▶, Tư vấn chuyên sâu]` — **KHÔNG có "Mạng lưới TVV"** |

→ **BUG-TVV-A2-001 confirmed reproduce 5 round consecutive (R12b/R13/R14/R15/R16)**. Dev chưa push fix BE permission seed trong window R15 → R16 (~1h06min).

**Evidence:** [R16-nht04ui-fresh-context-perms-25-403.png](../../bug-reports/tu-van-vien-cg/evidence-r7-4-a2-nht-perm/R16-nht04ui-fresh-context-perms-25-403.png)

### A2.3 R16 status — 🚫 Không test được (block 2 path identical R15)

Path (a) chủ hồ sơ tự nộp lại — TVV-0018 CB-tạo không có TK (TK auto-tạo ở CHO_KICH_HOAT per FR-VIII-26), R16 không seed thêm. Path (b) NHT đăng ký lại — block bởi BUG-TVV-A2-001 confirmed identical R16. Pool TU_CHOI vẫn 1 record (TVV-0018 seeded R13), unchanged R14/R15/R16.

### R16 Pool sau verify

Pool TVV unchanged R16 — không advance state, chỉ verify API + sidebar permission. State count post-R16 identical R15 baseline (TVV total 18, TU_CHOI:4, YEU_CAU_BO_SUNG:2).

## R15 Round (2026-05-09 20:00:18 — re-verify BUG-001 sau clear cache toàn bộ)

### Scope R15 (Quick verify with fresh cache — ~10 phút)

User yêu cầu verify lại bug với clear cache trước khi test, để loại trừ giả thuyết "FE cache stale token / FE permission cache outdated". R15 tạo isolated context fresh hoàn toàn + clear toàn bộ client-side state (localStorage / sessionStorage / cookies / Caches API / IndexedDB) + reload với `ignoreCache=true`, sau đó login lại và probe.

### A2.1 R15 status — ✅ Đạt (no re-test, R12 evidence kept)

A2.1 đã ✅ Đạt sau R12 fresh walk TVV-0017. R13/R14/R15 không re-walk vì transition đã verify ổn định + state machine path không thay đổi. Evidence + spec compliance giữ từ R12.

### A2.2 R15 verify BUG-TVV-A2-001 sau clear cache — 🚫 Không test được (bug vẫn open)

| Step | Action | Result |
|---|---|---|
| 0 | Spawn isolated context `qa_r15_a2_nht04_clear_cache_fresh` (new browser context, fresh storage) | OK |
| 1 | Clear toàn bộ client-side state: `localStorage.clear()` + `sessionStorage.clear()` + `document.cookie` expire all + `caches.keys() → caches.delete()` + `indexedDB.databases() → deleteDatabase()` | localStorage_size=0, sessionStorage_size=0, cookie="", caches deleted, IDBs deleted |
| 2 | `navigate_page reload ignoreCache=true` → /login render fresh | OK |
| 3 | Login `nht_04_ui` (Secret@123 + OTP 666666) → landing `/dao-tao/chuong-trinh/danh-sach` | OK, role NHT, donVi BTP-TW root |
| 4 | GET `/api/v1/auth/me` | 200 — vaiTro=["NHT"], **perms_count=25 identical R14/R13/R12b** |
| 5 | Inspect perm list | `perms_tvv_related=["bo-sung_tu_van_vien","register_tu_van_vien"]` identical — **vẫn thiếu** `read_tu_van_vien`, `update_tu_van_vien`, `update-nang-luc_tu_van_vien` |
| 6 | GET `/api/v1/tu-van-viens?page=0&size=10` | **403 ERR-PERM-SYS-00-01 "Forbidden"** ❌ identical |
| 7 | PATCH `/api/v1/tu-van-viens/00000000-0000-0000-0000-000000000999/nang-luc` | **403 ERR-PERM-SYS-00-01 "Forbidden"** ❌ identical |
| 8 | Click expand "Quản lý tư vấn▶" + "Quản lý đào tạo▶" → wait 600ms × 2 → list sidebar | sidebar_count=7, items: `[Quản lý đào tạo, tập huấn▶, Chương trình đào tạo, Khóa học, Kho tài liệu / Bài giảng, Quản lý vụ việc hỗ trợ pháp lý, Quản lý tư vấn▶, Tư vấn chuyên sâu]` — **KHÔNG có "Mạng lưới TVV"** |

→ **BUG-TVV-A2-001 confirmed reproduce 4 round consecutive (R12b/R13/R14/R15)** qua 3 method khác nhau:
- R12/R13: login chuẩn (default context, no clear)
- R14: isolated context fresh (new context, không clear cache)
- R15: isolated context fresh + clear toàn bộ cache + reload ignoreCache

→ **Kết luận R15:** clear cache + fresh context **KHÔNG ảnh hưởng** kết quả → bug **100% server-side** (BE permission seed gap thực sự, không phải FE cached token / stale permission cache / SW cache). Fix phải làm ở BE, không phải FE clear-cache hay update SW.

**Evidence:** [R15-nht04ui-fresh-cache-sidebar-no-mang-luoi-tvv.png](../../bug-reports/tu-van-vien-cg/evidence-r7-4-a2-nht-perm/R15-nht04ui-fresh-cache-sidebar-no-mang-luoi-tvv.png)

### A2.3 R15 status — 🚫 Không test được (cấu trúc block 2 path identical R14)

Path (a) chủ hồ sơ tự nộp lại — TVV-0018 CB-tạo không có TK (TK auto-tạo ở CHO_KICH_HOAT per FR-VIII-26), R15 không seed thêm. Path (b) NHT đăng ký lại — block bởi BUG-TVV-A2-001 confirmed identical R15. Pool TU_CHOI vẫn 1 record (TVV-0018 seeded R13), unchanged R14/R15.

### R15 Pool sau verify

Pool TVV unchanged R15 — không advance state, chỉ verify API + sidebar permission với fresh cache. State count post-R15 identical R14 baseline (TVV total 18, TU_CHOI:4, YEU_CAU_BO_SUNG:2).

## R14 Round (2026-05-09 19:50:19 — re-verify BUG-001 unchanged)

### Scope R14 (Quick verify — ~20 phút)

User yêu cầu chạy R7.4.A2 cẩn thận sau R13. R13 verify lúc 14:25:00 cùng ngày kết luận bug-001 vẫn Open. R14 quick re-verify để check dev có push fix trong window R13 → R14 hay không. Nếu fix → run A2.2 + A2.3 path (b). Nếu không fix → kết luận identical, đóng nhanh.

### A2.1 R14 status — ✅ Đạt (no re-test, R12 evidence kept)

A2.1 đã ✅ Đạt sau R12 fresh walk TVV-0017. R13 + R14 không re-walk vì transition đã verify ổn định + state machine path không thay đổi. Evidence + spec compliance giữ từ R12.

### A2.2 R14 verify BUG-TVV-A2-001 — 🚫 Không test được (bug vẫn open)

| Step | Action | Result |
|---|---|---|
| 1 | Login `nht_04_ui` (isolated context `qa_r14_a2_nht04_verify`, Secret@123 + OTP 666666) → landing `/dao-tao/chuong-trinh/danh-sach` | OK, role NHT, donVi `00000000-0000-4000-8000-000000000001` BTP-TW root |
| 2 | GET `/api/v1/auth/me` | 200 — vaiTro=["NHT"], **perms_count=25 identical R13** |
| 3 | Inspect perm list | `perms_tvv_related=["bo-sung_tu_van_vien","register_tu_van_vien"]` — **vẫn thiếu** `read_tu_van_vien`, `update_tu_van_vien`, `update-nang-luc_tu_van_vien` |
| 4 | GET `/api/v1/tu-van-viens?page=0&size=10` | **403 ERR-PERM-SYS-00-01 "Forbidden"** ❌ identical R13 |
| 5 | PATCH `/api/v1/tu-van-viens/00000000-0000-0000-0000-000000000999/nang-luc` (fake UUID probe) | **403 ERR-PERM-SYS-00-01 "Forbidden"** ❌ identical R13 |
| 6 | Sidebar render → liệt kê 7 items | `[Quản lý đào tạo, tập huấn▶, Chương trình đào tạo, Khóa học, Kho tài liệu / Bài giảng, Quản lý vụ việc hỗ trợ pháp lý, Quản lý tư vấn▶, Tư vấn chuyên sâu]` — **KHÔNG có "Mạng lưới TVV"** |
| 7 | Click expand "Quản lý tư vấn▶" → wait 500ms → re-list | sidebar_count vẫn = 7, chỉ render thêm "Tư vấn chuyên sâu". Không có thêm submenu TVV/Chuyên gia/Mạng lưới |

→ **BUG-TVV-A2-001 confirmed identical R12b → R13 → R14** (3 round consecutive). Delta R13 → R14 = ~5h25min, dev không push fix trong window này.

**Evidence:** [R14-nht04ui-sidebar-no-mang-luoi-tvv.png](../../bug-reports/tu-van-vien-cg/evidence-r7-4-a2-nht-perm/R14-nht04ui-sidebar-no-mang-luoi-tvv.png)

### A2.3 R14 status — 🚫 Không test được (cấu trúc block 2 path identical R13)

Path (a) chủ hồ sơ tự nộp lại — TVV-0018 CB-tạo không có TK (TK auto-tạo ở CHO_KICH_HOAT per FR-VIII-26), R14 không seed thêm. Path (b) NHT đăng ký lại — block bởi BUG-TVV-A2-001 verified identical R14. Pool TU_CHOI vẫn 1 record (TVV-0018 seeded R13), unchanged R14.

### R14 Pool sau verify

Pool TVV unchanged R14 — không advance state, chỉ verify API + sidebar permission. State-snapshot count post-R14 identical R13 18:22:00 baseline (TVV total 18, TU_CHOI:4, YEU_CAU_BO_SUNG:2).

## R13 Round (2026-05-09 14:25:00 — verify bug NHT perm + seed TU_CHOI pool)

### A2.1 R13 status — ✅ Đạt (no re-test, R12 evidence kept)

A2.1 đã ✅ Đạt sau R12 fresh walk TVV-0017. R13 không re-walk vì transition đã verify ổn định + state machine path không thay đổi giữa R12 và R13. Evidence + spec compliance giữ từ R12.

### A2.2 R13 verify BUG-TVV-A2-001 — 🚫 Không test được (bug vẫn open)

| Step | Action | Result |
|---|---|---|
| 1 | Login `nht_04_ui` (BTP-TW root) → fetch `/auth/me` | 200 — `vaiTro=["NHT"]`, `donViId=BTP-TW root`, **25 perms** |
| 2 | Inspect perm list | Chỉ có `bo-sung_tu_van_vien` + `register_tu_van_vien` — **KHÔNG có** `read_tu_van_vien`, `update_tu_van_vien`, `update-nang-luc_tu_van_vien` |
| 3 | GET `/api/v1/tu-van-viens?page=0&size=10` | **403 ERR-PERM-SYS-00-01** ❌ |
| 4 | PATCH `/api/v1/tu-van-viens/<id>/nang-luc` | **403 ERR-PERM-SYS-00-01** ❌ |
| 5 | Sidebar UI render | KHÔNG có "Mạng lưới TVV" menu — same gap với R12b |

→ **BUG-TVV-A2-001 confirmed identical R12b → R13** — perm count 25, missing perm list, sidebar UI gap đều khớp. Bug **chưa fix**.

**Evidence:** [R13-nht04ui-sidebar-no-mang-luoi-tvv.jpeg](../../bug-reports/tu-van-vien-cg/evidence-r7-4-a2-nht-perm/R13-nht04ui-sidebar-no-mang-luoi-tvv.jpeg)

### A2.3 R13 attempt — 🚫 Không test được (cấu trúc block 2 path)

**Pool seed:** Đẩy TVV-BTP-TW-0018 (Trần Thị Tư Vấn 16) từ MOI_DANG_KY → TU_CHOI thành công qua flow:
1. Login cb_nv_tw_01 → MLTVV → click TVV-0018 detail
2. Click tab Thẩm định → Pháp lý=Đạt + tick N/A Hiệu quả + Kết luận=KHÔNG ĐẠT + Lý do "R13 seed pool TU_CHOI cho A2.3 — TVV không đáp ứng tiêu chí năng lực thẩm định." (79 ký tự)
3. Click Gửi KQ → POST `/tham-dinh` 200 → badge `Mới đăng ký` → **`Từ chối`** ✅; tab thẩm định disabled

→ Pool TU_CHOI sau R13 = 1 record (TVV-0018). Sẵn sàng cho re-test A2.3 sau khi dev fix.

**Spec analysis 2 path cho TU_CHOI → CHO_THAM_DINH:**

| Path | SRS ref | Actor | R13 status |
|---|---|---|---|
| (a) Chủ hồ sơ tự nộp lại | line 1572 + line 2314 + line 314 | TVV/CG (chủ hồ sơ) login portal nộp lại | 🚫 **Cấu trúc block** — TVV-0018 CB-tạo, không có TK (TK chỉ auto-tạo ở CHO_KICH_HOAT per FR-VIII-26). Chủ hồ sơ login impossible. |
| (b) NHT đăng ký lại | FR-IV-03 line 314 | NHT cùng đơn vị | 🚫 Block bởi BUG-TVV-A2-001 — NHT thiếu perm `read/update_tu_van_vien` + sidebar gate. |

→ A2.3 **structurally blocked** với mọi TVV CB-tạo ở TU_CHOI. Cần dev fix BUG-001 (path b) HOẶC seed TVV qua flow tự đăng ký FR-IV-03 step 1 (path a — TVV self-register tạo TK ngay từ đăng ký, sau đó bị TU_CHOI vẫn login được portal nộp lại).

**Evidence:**
- [R13-seed-tvv0018-tu-choi.jpeg](evidence-r7-4-a2/R13-seed-tvv0018-tu-choi.jpeg) — TVV-0018 badge "Từ chối" sau Gửi KQ KHÔNG ĐẠT, pool TU_CHOI seeded

### R13 Pool sau walk

| Mã | Tên | State trước R13 | State sau R13 | Note |
|---|---|---|---|---|
| TVV-BTP-TW-0017 | Nguyễn Văn Tư Vấn 15 | YEU_CAU_BO_SUNG (R12) | YEU_CAU_BO_SUNG | Giữ nguyên — A2.2 vẫn block, sẵn sàng re-test sau dev fix |
| TVV-BTP-TW-0018 | Trần Thị Tư Vấn 16 | MOI_DANG_KY | TU_CHOI | R13 seeded — pool TU_CHOI từ 0 → 1, sẵn sàng re-test A2.3 sau dev fix |

Pool count post-R13: Mới đăng ký 10 (-1 sau R13) / Đang thẩm định 0 / Yêu cầu bổ sung 2 / **Từ chối 1** (+1 sau R13).

## R12 Round (2026-05-09 09:40:00 — fresh TVV-0017 walk UI thuần)

### Re-analyze root cause của blocker A2.2 + A2.3 (2 lần update)

R7 round attribute blocker tới "BUG-CG-A1-003 mail kích hoạt hỏng → TVV ứng viên không login portal". R12 (09:40:00) đổi attribution sang "đơn vị-match" theo SRS line 368/414. R12b (10:55:00) verify trực tiếp với 2 NHT account khác nhau, **đính chính tiếp một lần nữa** — root cause thật là **bug permission seed**, không phải đơn vị-match.

**Spec ground truth (xác nhận lại):**
- **FR-IV-04 line 366:** "TVV/CG có thể đăng nhập chuyên trang xem hồ sơ của mình ở chế độ chỉ đọc, **không sửa được**. Muốn thay đổi → **liên hệ NHT**."
- **FR-IV-04 line 368:** "**Tác nhân:** Người hỗ trợ pháp lý (NHT)" — actor cập nhật năng lực = NHT.
- **FR-IV-04 line 414 (E1 ERR-NL-01):** "NHT không cùng đơn vị với TVV → 403 'Bạn không có quyền cập nhật hồ sơ tư vấn viên này (khác đơn vị)'" — error trigger CHỈ khi khác đơn vị, không phải khi cùng đơn vị.

**Verify R12b ngày 2026-05-09 10:55:00:**

| Test | Account | TVV | Đơn vị NHT | Đơn vị TVV | Match? | Kết quả |
|---|---|---|---|---|---|---|
| A | nht_04_ui | TVV-0017 | BTP-TW root | BTP-TW root | ✅ MATCH | **403 ERR-PERM-SYS-00-01** ❌ |
| B | nht_01 | TVV-0017 | STP-AG | BTP-TW root | ❌ KHÁC | 403 ERR-PERM-SYS-00-01 |
| C | qtht_01 (bypass) | TVV-0017 | — | — | — | 403 ERR-NL-01 "Chỉ NHT mới được cập nhật" — đúng spec |

→ Test A loại trừ giả thuyết "đơn vị mismatch": NHT cùng đơn vị TVV-0017 vẫn bị 403, message **không phải** ERR-NL-01 (khác đơn vị) mà là **ERR-PERM-SYS-00-01** (system-level permission deny).

**Root cause thật (R12b verified):** `/auth/me` của NHT trả 25 perms — chỉ có `bo-sung_tu_van_vien` + `register_tu_van_vien` (đủ cho FR-IV-03 step 1 submit) — **KHÔNG có** `read_tu_van_vien`, `update_tu_van_vien`, `update-nang-luc_tu_van_vien`. UI sidebar NHT cũng KHÔNG render menu "Mạng lưới TVV". Direct route `/chuyen-gia-tvv` bị FE PermissionRoute chặn với toast "Bạn không có quyền truy cập chức năng này.".

→ **Bug permission seed gap** — log [BUG-TVV-A2-001](../../bug-reports/tu-van-vien-cg/Pass-bug-report-flow-r7-4-a2-nht-permission-gap.md) Major Open.

### A2.1 R12 Walk fresh TVV-0017 — Re-verify ✅ Đạt

| Step | Action | Result |
|---|---|---|
| 1 | Login cb_nv_tw_01 → MLTVV → Mới đăng ký tab (12 records) | OK 12 MDK visible (TVV-0017..0028) |
| 2 | Click TVV-0017 (Nguyễn Văn Tư Vấn 15) → Detail page | OK URL `/chuyen-gia-tvv/0448578f-...`, badge `Mới đăng ký` |
| 3 | Click tab Thẩm định | OK form 4 nhóm + button Hủy/Lưu nháp/Gửi KQ/Trình duyệt(disabled) |
| 4 | Click Lưu nháp without conclusions | Validation: "Vui lòng chọn kết quả pháp lý" + "Vui lòng chọn kết luận" |
| 5 | Pháp lý=Đạt + Kết luận=ĐẠT + Lưu nháp | POST `/tham-dinh` 200 (reqid=360); badge changed `Mới đăng ký` → **`Đang thẩm định`**; button Trình duyệt enabled |

**Spec compliance:** Line 66 + SCR-IV-03 + FR-IV-04 line 396-398 — BE skip CHO_THAM_DINH ngầm, đi thẳng MOI_DANG_KY → DANG_THAM_DINH. ✅ Đúng spec.

**Evidence:**
- [R12-A2-00-pool-tab-mdk-12records.jpeg](evidence-r7-4-a2/R12-A2-00-pool-tab-mdk-12records.jpeg) — pool 12 MDK trước walk
- [R12-A2-01-tvv0017-detail-mdk-baseline.jpeg](evidence-r7-4-a2/R12-A2-01-tvv0017-detail-mdk-baseline.jpeg) — baseline state MDK
- [R12-A2-1-tvv0017-mdk-to-dtd-skip-ctd.jpeg](evidence-r7-4-a2/R12-A2-1-tvv0017-mdk-to-dtd-skip-ctd.jpeg) — sau Lưu nháp, badge `Đang thẩm định`

### A2.2 R12 attempt — 🚫 Không test được (root cause: NHT actor + đơn vị-match)

| Step | Action | Result |
|---|---|---|
| 1 | TVV-0017 từ DTD → click Gửi KQ với conclusion=YÊU CẦU BỔ SUNG + Lý do | POST `/tham-dinh` 200 (reqid=364); badge `Đang thẩm định` → **`Yêu cầu bổ sung`** ✅ — pre-condition cho A2.2 đã đặt |
| 2 | Click tab Năng lực → Cập nhật năng lực → fill kinh nghiệm + Lưu | **PATCH `/api/v1/tu-van-viens/<id>/nang-luc` → 403 Forbidden** (reqid=369) — đúng spec FR-IV-04 line 368 actor=NHT |
| 3 | Fallback: Sửa hồ sơ → fill kinh nghiệm tư vấn + Lưu | PATCH `/api/v1/tu-van-viens/<id>` → 200 (reqid=385); badge **vẫn `Yêu cầu bổ sung`** — endpoint hồ sơ thường không trigger SM-TVV step 7 (đúng spec, chỉ /nang-luc trigger) |

**Bug thực (R12b verified):** Permission seed cho role NHT thiếu `read/update_tu_van_vien` + `update-nang-luc_tu_van_vien`. Verified 2 NHT account (nht_01 STP-AG khác đơn vị + nht_04_ui BTP-TW cùng đơn vị TVV-0017) — cả 2 đều bị `403 ERR-PERM-SYS-00-01` ngay từ GET `/api/v1/tu-van-viens`. UI sidebar không có Mạng lưới TVV, route /chuyen-gia-tvv bị FE chặn. Log bug [BUG-TVV-A2-001](../../bug-reports/tu-van-vien-cg/Pass-bug-report-flow-r7-4-a2-nht-permission-gap.md) Major Open.

**Cần để test A2.2:** Dev seed lại permission `read_tu_van_vien` + `update-nang-luc_tu_van_vien` cho role NHT + FE expose menu Mạng lưới TVV cho NHT + allow route `/chuyen-gia-tvv` với role NHT. Re-test với `nht_04_ui` cùng đơn vị TVV-0017.

**Evidence:**
- [R12-A2-2a-tvv0017-dtd-to-ycbs-precondition.jpeg](evidence-r7-4-a2/R12-A2-2a-tvv0017-dtd-to-ycbs-precondition.jpeg) — pre-condition YCBS đạt
- [R12-A2-2b-403-patch-nang-luc-cb-blocked.jpeg](evidence-r7-4-a2/R12-A2-2b-403-patch-nang-luc-cb-blocked.jpeg) — CB attempt /nang-luc, BE 403 ERR-NL-01 đúng spec

### A2.3 R12 status — 🚫 Không test được (same bug NHT perm gap + pool TU_CHOI=0)

Same root cause với A2.2 — actor cho `TU_CHOI → CHO_THAM_DINH` re-submission per FR-IV-03 = NHT cùng đơn vị, đang bị block bởi BUG-TVV-A2-001 (NHT thiếu permission). Đồng thời pool TU_CHOI hiện tại = 0 record. Cần (1) dev fix permission seed NHT; (2) đẩy ≥1 TVV qua đường KHÔNG ĐẠT → CB PD Phê duyệt từ chối → state TU_CHOI; (3) NHT đăng ký lại qua FR-IV-03.

KHÔNG capture screenshot riêng cho A2.3 R12 vì pre-condition không setup được + bug NHT permission cùng gốc với A2.2.

## Ý nghĩa cột Status

| Ký hiệu | Nghĩa |
|---|---|
| ✅ Đạt | Test xong, kết quả khớp spec |
| ⚠️ Sai spec | UI/BE làm khác spec nhưng chưa rõ là bug hay spec ambiguous → defer chờ BA |
| 🚫 Không test được | Thiếu điều kiện đầu vào (đơn vị NHT + TVV không match HOẶC pool TU_CHOI rỗng) |

## Pool sau R12 walk

| Mã | Tên | State trước R12 | State sau R12 | Note |
|---|---|---|---|---|
| TVV-BTP-TW-0017 | Nguyễn Văn Tư Vấn 15 | MOI_DANG_KY | YEU_CAU_BO_SUNG | A2.1 ✅ Đạt walk MDK→DTD; A2.2 attempt PATCH /nang-luc 403 đúng spec; pre-condition YCBS giữ lại cho re-test sau khi seed NHT phù hợp |

Pool count post-walk: Tất cả Mới đăng ký 11 (-1) / Đang thẩm định 0 / Yêu cầu bổ sung 2 (+1).

## Test Case Matrix

| TC ID | Transition | Loại | P | Status | Evidence |
|---|---|:-:|:-:|:-:|---|
| **TC-A2-01** | `MOI_DANG_KY → CHO_THAM_DINH` (ngầm khi CB NV bắt đầu thẩm định) | Workflow | P0 | ✅ Đạt | R12 fresh TVV-0017 walk: badge MDK→DTD sau Lưu nháp, BE skip CTD đúng SRS line 66 + SCR-IV-03 + FR-IV-04 line 396-398. POST `/tham-dinh` 200 reqid=360. [R12-A2-1-tvv0017-mdk-to-dtd-skip-ctd.jpeg](evidence-r7-4-a2/R12-A2-1-tvv0017-mdk-to-dtd-skip-ctd.jpeg) |
| **TC-A2-02** | `YEU_CAU_BO_SUNG → DANG_THAM_DINH` (NHT cập nhật năng lực FR-IV-04 step 7) | Workflow | P0 | 🚫 Không test được | R18 2026-05-09 22:39:25 quick verify dev fix sau R17 (delta ~1h21min) — `nht_01` isolated context `qa_r18_a2_nht01_verify` → perms_count=25 + GET 403 + PATCH 403 identical R17. Bug **identical 7 round (R12b → R13 → R14 → R15 → R16 → R17 → R18)** [BUG-TVV-A2-001](../../bug-reports/tu-van-vien-cg/Pass-bug-report-flow-r7-4-a2-nht-permission-gap.md) role-wide BE, dev chưa fix. |
| **TC-A2-03** | `TU_CHOI → CHO_THAM_DINH` (TVV/CG chủ hồ sơ nộp lại HOẶC NHT đăng ký lại) | Workflow | P0 | 🚫 Không test được | R13 seeded TU_CHOI pool 1 record (TVV-0018) unchanged R14/R15/R16/R17/R18. 2 path đều structurally block: (a) chủ hồ sơ — TVV CB-tạo không có TK (TK auto-tạo ở CHO_KICH_HOAT per FR-VIII-26); (b) NHT — block bởi BUG-001 confirmed identical R18. Cần dev fix BUG-001 (BE side) hoặc seed TVV qua self-register FR-IV-03 step 1. |

## Spec compliance summary

| Rule | Spec line | Observed | Compliant |
|---|---|---|:-:|
| MOI_DANG_KY → CHO_THAM_DINH ngầm (BE skip CTD) | line 2305 + line 66 + SCR-IV-03 + FR-IV-04 line 396 | R12 walk: badge MDK → DTD trực tiếp sau Lưu nháp | ✅ |
| YEU_CAU_BO_SUNG → DANG_THAM_DINH via NHT FR-IV-04 step 7 | line 2308 + FR-IV-04 line 368 + line 396-398 | Endpoint /nang-luc tồn tại + 403 cho non-NHT đúng spec; nhưng NHT (cả cùng + khác đơn vị) cũng 403 do thiếu permission seed | 🚫 Cannot test (bug NHT perm) |
| TU_CHOI → CHO_THAM_DINH (no cooldown) via FR-IV-03 line 314 / FR-IV-04 line 1572 | line 2314 + FR-IV-03 line 314 + line 1572 | R13 pool TU_CHOI seeded 1 record (TVV-0018 via flow KHÔNG ĐẠT). Path (a) chủ hồ sơ — TVV CB-tạo không có TK; path (b) NHT — block bởi BUG-001 | 🚫 Cannot test (cấu trúc block 2 path) |
| Optimistic lock | FR-IV-06 | TVV-0017 version tăng sau mỗi POST /tham-dinh + PATCH | ✅ |
| Validation conclusion required | FR-IV-06 form | Lưu nháp without Pháp lý/Kết luận → block với inline error | ✅ |
| Permission FR-IV-04 actor=NHT | line 368 | CB PATCH /nang-luc → 403 ERR-NL-01 đúng spec | ✅ |

## Bugs phát hiện

| Bug ID | Severity | Title | Status | File |
|---|---|---|---|---|
| BUG-TVV-A2-001 | Major | Role NHT thiếu permission seed `read/update_tu_van_vien` + UI sidebar gate `/chuyen-gia-tvv` | Open | [Pass-bug-report-flow-r7-4-a2-nht-permission-gap.md](../../bug-reports/tu-van-vien-cg/Pass-bug-report-flow-r7-4-a2-nht-permission-gap.md) |

R12b 2026-05-09 10:55:00 verify: 2 NHT account (cùng + khác đơn vị TVV) đều bị 403 ERR-PERM-SYS-00-01 ngay từ GET /tu-van-viens. Test bypass với QTHT trả ERR-NL-01 verbatim "Chỉ NHT mới được cập nhật" → BE policy đúng spec FR-IV-04 line 368, gap nằm ở permission seed phía role NHT.

R13 2026-05-09 14:25:00 verify lại với `nht_04_ui` — perm count 25 + missing perm list + sidebar gap đều **identical R12b**. Bug chưa được dev fix, vẫn Open Major.

R14 2026-05-09 19:50:19 verify lại với `nht_04_ui` (isolated context fresh) — perms_count=25 identical, GET /tu-van-viens 403, PATCH /nang-luc 403 (probe fake UUID), sidebar 7 items không có "Mạng lưới TVV" sau khi expand "Quản lý tư vấn▶". Bug chưa fix sau ~5h25min từ R13, vẫn Open Major.

R15 2026-05-09 20:00:18 verify lại với `nht_04_ui` sau **clear cache toàn bộ client-side** (localStorage + sessionStorage + cookies + Caches API + IndexedDB cleared + reload ignoreCache + new isolated context `qa_r15_a2_nht04_clear_cache_fresh`) — perms_count=25 identical, GET /tu-van-viens 403, PATCH /nang-luc 403, sidebar 7 items không có "Mạng lưới TVV". **Clear cache loại trừ FE-side hypothesis (FE permission cache stale, FE token cached, SW cached old role)** → bug **100% server-side**, BE permission seed thiếu thực sự. Reproduce 4 round consecutive (R12b/R13/R14/R15), vẫn Open Major.

R16 2026-05-09 21:06:35 quick verify dev fix sau R15 (delta ~1h06min) — `nht_04_ui` isolated context `qa_r16_a2_nht04_verify` → /auth/me 200 perms_count=25 identical, GET /tu-van-viens 403 ERR-PERM-SYS-00-01, PATCH /nang-luc 403 ERR-PERM-SYS-00-01, sidebar 7 items không có "Mạng lưới TVV". **Dev chưa push fix BE trong window R15 → R16**. Reproduce 5 round consecutive (R12b/R13/R14/R15/R16), vẫn Open Major.

R17 2026-05-09 21:18:22 cross-account verify 4 NHT khác nhau qua 4 isolated context riêng (`nht_01` STP-AG DP + `nht_02` STP-DN DP + `nht_03` STP-HP DP + `nht_04_ui` BTP-TW TW) — **tất cả 4 trả perms_count=25 identical** với perms_tvv_related=`[bo-sung_tu_van_vien, register_tu_van_vien]` identical, GET /tu-van-viens 403 + PATCH /nang-luc 403. **Loại trừ per-user / per-đơn vị / per-cấp hypothesis** → bug **100% role-wide BE permission seed gap**. Reproduce 6 round consecutive (R12b/R13/R14/R15/R16/R17) qua 4 method (login chuẩn → isolated context → fresh cache → cross-account 4 NHT), vẫn Open Major.

R18 2026-05-09 22:39:25 quick verify dev fix sau R17 (delta ~1h21min) với `nht_01` isolated context `qa_r18_a2_nht01_verify` → /auth/me 200 perms_count=25 identical R17, GET /tu-van-viens 403 (requestId 9620d97a-bb1d-464b-9fd7-72ad654b9c62), PATCH /nang-luc 403 (requestId 2db2dbd0-ad03-490e-bfd6-809d0736f5a0) — **dev chưa push fix BE trong window R17 → R18**. Reproduce **7 round consecutive** (R12b/R13/R14/R15/R16/R17/R18), vẫn Open Major.

A2.1 ✅ Đạt sau R12 fresh walk. A2.2 + A2.3 🚫 Không test được — block bởi BUG-TVV-A2-001 (chưa fix R18, role-wide confirmed).

## Tóm tắt: case không test được vì sao?

| Case | Lý do thật (R18 verify 2026-05-09 22:39:25 quick verify dev fix) | Cần làm gì để test? |
|---|---|---|
| A2.2 (YCBS → DTD) | Bug **NHT permission seed gap** ([BUG-TVV-A2-001](../../bug-reports/tu-van-vien-cg/Pass-bug-report-flow-r7-4-a2-nht-permission-gap.md)) **vẫn Open** sau 7 round consecutive (R12b/R13/R14/R15/R16/R17/R18). R18 quick verify (delta R17 → R18 ~1h21min) với nht_01 isolated context `qa_r18_a2_nht01_verify` → perms_count=25 + GET 403 + PATCH 403 identical R17. R17 cross-account 4 NHT đã loại trừ per-user/per-đơn vị/per-cấp → bug 100% role-wide BE permission seed gap, dev chưa push fix BE. | Dev fix BE: (1) seed perm `read_tu_van_vien` + `update_tu_van_vien` + `update-nang-luc_tu_van_vien` cho role NHT trong DB role-permission mapping (master role record, không phải per-user); (2) FE expose menu Mạng lưới TVV cho NHT; (3) FE allow route `/chuyen-gia-tvv` với role NHT. Sau đó re-test với bất kỳ NHT nào cùng đơn vị TVV-0017. |
| A2.3 (TU_CHOI → CTD) | R13 seeded pool TU_CHOI = 1 record (TVV-0018) unchanged R14/R15/R16/R17/R18. Cấu trúc block 2 path: (a) chủ hồ sơ TVV CB-tạo không có TK (TK auto-tạo ở CHO_KICH_HOAT); (b) NHT block bởi BUG-001 confirmed identical R18. | (a-fix) Dev seed flow self-register FR-IV-03 step 1 — TVV tự đăng ký, TK tạo từ đăng ký, TVV login portal nộp lại sau từ chối. (b-fix) Dev fix BE permission NHT role-wide (cùng A2.2). |

## Defer (chờ BA hoặc data setup)

Không có case nào defer chờ BA. Cần product owner chốt: có cần ưu tiên seed NHT cùng đơn vị + flow KHÔNG ĐẠT để verify A2.2 + A2.3 hay defer cho round sau (sau khi data setup hoàn chỉnh).

---

# Lifecycle archive — older rounds

## R7 Round (2026-05-07)

> **R7.4.A2 verify pass 2 (2026-05-07 23:30):** retry case A2.1 ⚠️ Sai spec qua NotebookLM HTPLDN + grep SRS local.
> - **A2.1** đổi ⚠️ Sai spec → ✅ Đạt: NotebookLM xác nhận SCR-IV-03 line "Bắt đầu thẩm định" hành vi: "Click → ngầm chuyển trạng thái Mới đăng ký/Chờ thẩm định → Đang thẩm định + chuyển sang tab Thẩm định". `srs-fr-04-chuyen-gia-tvv.md` line 66 cũng nói rõ: "KHÔNG yêu cầu thao tác 'Tiếp nhận hồ sơ' riêng — CB NV vào tab Thẩm định bắt đầu chấm = ngầm chuyển trạng thái". → BE skip CHO_THAM_DINH đi thẳng MOI_DANG_KY → DANG_THAM_DINH là **đúng spec**, không phải deviation.

R7 attribution gốc: blocker A2.2/A2.3 = "BUG-CG-A1-003 mail kích hoạt hỏng → TVV ứng viên không login portal". R12 verify SRS verbatim — root cause thật là **NHT actor + đơn vị-match constraint**, không phải portal TVV. R7 attribution updated theo R12 phân tích.

### R7 Pool sau test

| Mã | Tên | State trước | State sau | Note |
|---|---|---|---|---|
| TVV-BTP-TW-0013 | (auto-tạo qua A2.1) | MOI_DANG_KY | DANG_THAM_DINH | A2.1 ✅ Đạt — BE skip CHO_THAM_DINH đúng spec "ngầm chuyển trạng thái" |
| TVV-BTP-TW-0010 | NHT 04 (legacy YEU_CAU_BO_SUNG) | YEU_CAU_BO_SUNG | YEU_CAU_BO_SUNG | A2.2 NOT TESTABLE — root cause R7 attribute "CB NV Sửa hồ sơ không trigger transition" (đúng — CB NV không có quyền /nang-luc, đó là behavior đúng spec FR-IV-04) |
| TU_CHOI pool | — | — | — | A2.3 NOT TESTABLE — pool rỗng + đơn vị mismatch |

R7 evidence references kept: [A2-01-tvv0013-moi-dang-ky-skip-to-dang-tham-dinh.png](evidence-r7-4-a2/A2-01-tvv0013-moi-dang-ky-skip-to-dang-tham-dinh.png), [A2-02-tvv0010-yeu-cau-bo-sung-stays-after-sua-ho-so.png](evidence-r7-4-a2/A2-02-tvv0010-yeu-cau-bo-sung-stays-after-sua-ho-so.png), [A2-03-tu-choi-pool-empty.png](evidence-r7-4-a2/A2-03-tu-choi-pool-empty.png).
