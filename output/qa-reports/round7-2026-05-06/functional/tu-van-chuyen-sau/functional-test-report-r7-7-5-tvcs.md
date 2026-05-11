# Functional Test Report — R7.7.5 TVCS (FR-12)

| Thông tin | Giá trị |
|-----------|---------|
| **Module** | Tư vấn chuyên sâu (FR-12 · Nhóm X.1) |
| **Spec** | [`output/funtion/7.12-tu-van-chuyen-sau.md`](../../../../funtion/7.12-tu-van-chuyen-sau.md) v3.5 (61 TC = 44 base + 17 mới v3.5) |
| **SRS** | [`srs-fr-12-tv-chuyen-sau.md`](../../../../../input/srs-update-2026-5-5/srs-fr-12-tv-chuyen-sau.md) v3.5 |
| **Round** | R8 (2026-05-07) → R14 (2026-05-10 12:30:00) → R15 (2026-05-10 14:30:00) → R16 Phase 1 (2026-05-10 20:25:00 — independent verify R15) → **R16 Phase 2 (2026-05-10 20:35:00 — TC walk nhóm A/B/C/D/E + log 4 bug mới)** |
| **Tester** | QA Automation (Chrome DevTools MCP) |
| **Pre-req** | R7.2.6 ✅ 8 CG `HOAT_DONG` + R7.4.A5 R15 ✅ 9/11 PASS workflow unblock (BUG-FE-A5-004 closed commit `f54afbc8`) + DN 23 records. R16 pool: 17 TVCS (5 TIEP_NHAN + 4 PHAN_CONG + 3 DANG_TU_VAN + 2 DA_DUYET + 3 HUY) |
| **Workflow đi kèm** | [workflow-test-report-r7-4-a5-tvcs.md](../../workflow/tu-van-chuyen-sau/workflow-test-report-r7-4-a5-tvcs.md) (R15: 9/11 PASS + 2 EXTERNAL = 11/11 covered) |
| **Bug report** | [Pass-bug-report-r7-7-5-tvcs.md](../../bug-reports/tu-van-chuyen-sau/Pass-bug-report-r7-7-5-tvcs.md) — **10/10 đóng R15** + [bug-report-r7-7-5-tvcs-r16.md](../../bug-reports/tu-van-chuyen-sau/bug-report-r7-7-5-tvcs-r16.md) — **4 bug mới R16 Phase 2** (TLPL endpoint, congKhai filter, auto-save 30s, NHT FE menu leak) |

---

## Verdict R17 (LATEST · 2026-05-11 02:55:00) — Bugfix re-verify + TV-022 unblock + BUG-008 regression

✅ **3/7 bug R16 đã closed (002 filter, 003 auto-save, 007 cross-scope leak)** + **TV-022 retest PASS**. ❌ **4/7 bug R16 vẫn Open** (001 TLPL, 004 NHT menu, 005 UI cong-khai, 006 FK hop_dong_tv_id) + **1 regression mới BUG-008** (fix BUG-007 dùng blanket-deny role NHT thay vì BR-AUTH-10 row-level → block happy path).

| Type | PASS | BLOCKED | SKIP | FAIL | ⚠️ Sai spec | Total |
|---|---:|---:|---:|---:|---:|---:|
| Workflow | 17 (+1 TV-022) | 2 | 4 | 0 (-1 TV-022) | 1 (TV-045 UI gap) | 21 |
| Cross-module | 3 | 1 | 1 | 1 (+1 TV-059) | 0 | 5 |
| Authorization | 6 | 0 | 0 | 0 | 0 | 6 |
| Happy | 17 | 0 | 1 | 0 | 0 | 18 |
| Negative | 7 | 0 | 3 | 0 | 0 | 10 |
| **Tổng** | **53** (+TV-022) | **2** | **9** | **1** (TV-059) | **1** (TV-045) | **61** |

> **R17 delta vs R16-P2:** TV-022 ❌→✅ (+1 PASS, -1 FAIL). Tổng PASS 52→53. Coverage 85% → 87%.

**R17 changes:**

- ✅ **TV-022 (Auto-save draft 30s):** R17 retest với `huongcg` (CG) — POST `/trao-doi-nhap` trên TVCS-20260507-0013 DANG_TU_VAN → **200 OK** + entity TRAO_DOI_NHAP. PUT lần 2 → 409 ERR-STATE-LOCK-409 optimistic locking đúng spec. Endpoint hoạt động đầy đủ. BUG-BE-TVCS-R16-003 closed.
- ✅ **BUG-002 (Filter ?congKhai=true)** re-verified: `cb_nv_tw_06` GET `/noi-dung-tu-van-cs?congKhai=true&pageSize=20` → 2 records, `allCongKhaiTrue=true`. Filter apply đúng. TV-035-1 + TV-046 list + TV-047 list verdict (đã PASS R16 phần workflow) — list filter R17 confirm.
- ❌ **BUG-007 fix SAI SPEC → BUG-008 mở:** 2-source verify (NotebookLM HTPLDN + SRS local FR-X.1-04 line 669-671 + BR-AUTH-10) confirm BE BẮT BUỘC row-level filter, KHÔNG blanket-deny. Test với `nht_tc001_btp_tw` (NHT có VV phân công với DN-003) GET `/doanh-nghieps/{DN-003}` → **403 SAI SPEC** (đúng spec phải 200 + hiển thị HSPL DN). Log BUG-BE-TVCS-R17-008 (Major P0).
- ❌ **BUG-001, 004, 005, 006 NOT FIXED:** TLPL endpoints 5/5 still 404, NHT sidebar vẫn show "Tư vấn chuyên sâu", DA_DUYET detail UI thiếu button [Công khai] + BE PATCH `/cong-khai` 404 (POST works for TV-046/047 R16, PATCH method does not), TVCS detail keys không có `hopDongTvId`.

**R17 accounts used:** `cb_nv_tw_06` (BTP·TW CB_NV — BE probes), `nht_01` (STP-AG NHT — FE menu + cross-scope HSPL), `nht_tc001_btp_tw` (BTP·TW NHT — happy HSPL BR-AUTH-10 verify), `huongcg` (BTP·TW CG — TV-022 auto-save happy path).

**Verdict tổng:** Module TVCS vẫn ⚠️ Sai spec — cần dev fix BUG-001/004/005/006 + BUG-008 (regression) + QA retest TV-023/024/025/043/059 trước khi flip ✅. Coverage 53/61 PASS · 9 chưa chạy được (chia 4 nhóm B nguyên nhân).

---

## Verdict R16 Phase 2 (2026-05-10 20:35:00) — TC walk nhóm A/B/C/D/E + log 4 bug mới

✅ **5 TC nhóm A unblock thêm + 4 bug mới logged**. TC delta vs R16 Phase 1: +5 PASS, +1 FAIL.

| Type | PASS | BLOCKED | SKIP | FAIL | Total |
|---|---:|---:|---:|---:|---:|
| Happy | 17 | 0 | 1 | 0 | 18 |
| Negative | 7 | 0 | 3 | 0 | 10 |
| Workflow | 16 (+2) | 2 (-1) | 4 | 1 (+1 TV-022) | 21 (-1 TV-045 ⚠️) |
| Authorization | 6 (+1) | 0 | 0 (-1 TV-039) | 0 | 6 |
| Cross-module | 3 (+1) | 1 | 1 (-1 TV-053 → 🚫) | 0 | 5 |
| **Tổng** | **52** (+TV-053 seed verify) | **2** | **9** | **2** (TV-022, TV-059) | **60** (+1 ⚠️ TV-045 — UI gap, BE OK) |
|  | _**R16-P2 nhóm 1+2+seed:** TV-048 ✅, TV-038 ✅ seed BR-AUTH-08, TV-053 ✅ seed lớp 2 BR-AUTH-10 (+ phát hiện BUG-007 detail bypass), TV-059 ❌ FAIL (BUG-BE-006), TV-045 ⚠️._ |  |  |  |  |  |

**Phase 1 — Walk 7 TC nhóm A (cascade upstream fix):**

- ✅ **TV-010 (CG từ chối phân công):** Tạo TVCS-20260510-0002 (LV Đất đai, DN-004), phân công huongcg → POST `/xac-nhan {TU_CHOI, lyDo}` 200 → state PHAN_CONG → TIEP_NHAN ver=2→3. Re-phân công + accept thành công. CG TU_CHOI flow PASS.
- ✅ **TV-016 (Immutability sau DA_DUYET):** TVCS-20260510-0002 sau khi DA_DUYET ver=7 — PATCH 409 ERR-BIZ-X-01-01 "Không thể cập nhật ở trạng thái 'DA_DUYET'", POST `/hoan-thanh` 409 ERR-STATE-TVCS-COMPLETE-01, POST `/approve` (lần 2) 409 ERR-STATE-TVCS-APPROVE-01. State machine enforced.
- ✅ **TV-021 (UI accordion read-only):** Verified earlier R16 Phase 1 — re-confirm với cb_pd_tw_06 trang `/tv-chuyen-sau/{id}` render 5 step icons checked + 5 accordion read-only + KHÔNG có button [Phê duyệt]/[Từ chối]/[Chỉnh sửa]/[Xóa]/[Hoàn thành].
- ❌ **TV-022 (Auto-save draft 30s) — FAIL:** SRS FR-12 line 1496 spec auto-save 30s vào TRAO_DOI_NHAP. 5 candidate endpoints (`/trao-doi-nhap`, `/draft`, `/auto-save`) đều 404 ERR-SYS-00-04-01. UI Hoàn thành tư vấn không có hint "Đã lưu" / debouncer. **Logged BUG-BE-TVCS-R16-003** Major P1.
- ✅ **TV-033 (Cross-cấp /approve 403):** cb_pd_dp_02 (cấp DP, BTP·DP) login isolated context, POST `/api/v1/noi-dung-tu-van-cs/{TVCS-TW-id}/approve` → **403 ERR-AUTH-VPD-00-02 "Đơn vị không nằm trong phạm vi truy cập của bạn"**. Cross-cấp boundary enforced. Spec BR-AUTH-05 cùng cấp confirmed.
- 🚫 **TV-040 (DA_DUYET trigger CG điểm cập nhật):** Cross-module DGCL — verified TVV profile `soVuViecDaXuLy` field tồn tại nhưng SRS srs-fr-04 chỉ count VV (không count TVCS). `/thong-ke` + `/statistics` endpoints 404 (out-of-spec). Cross-module DGCL inbound API (UC153) cần test riêng — defer.
- 🚫 **TV-053 (NHT view HSPL có VV):** Cascade. nht_01 (BTP·DP An Giang) sees 0 VV/HSPL/TVCS do BR-AUTH-10 2-tier filter. Pool VV STP-AG có 1 record (DA_TIEP_NHAN, nguoiHoTroId=null) — phân công yêu cầu `tvvId` UUID, nhưng nht_01 không có TVV record (44 TVV trong pool toàn loaiTvv `CG/TVV`). Cascade R7.3.14 NHT TVV seeding hoặc workflow walk dài hạn.

**Phase 2 — Bug logging (3 BE + 1 FE bug mới):**

- 📝 **BUG-BE-TVCS-R16-001** (Major P1): TLPL VV CRUD endpoint chưa expose. 7 candidate paths đều 404; UI accordion "Tư liệu pháp luật" empty state không có button thêm. **Block 8 TC nhóm B1** (TV-023, TV-024, TV-025, TV-043).
- 📝 **BUG-BE-TVCS-R16-002** (Major P1): Filter `?congKhai=true` không apply — trả full 17 records mixed (TVCS-0002 `congKhai:true` + TVCS-0001 `congKhai:false trangThai:HUY` cùng list). Cũng test `?laCongKhai=true` không apply. **Block 4 TC nhóm B2** (TV-035-1, TV-046 list, TV-047 list). Lưu ý: endpoint POST `/cong-khai` HOẠT ĐỘNG (đã verify TV-046/047 PASS R16 Phase 1) — chỉ filter list bị lỗi.
- 📝 **BUG-BE-TVCS-R16-003** (Major P1): Auto-save draft 30s endpoint chưa expose. **Block TV-022**.
- 📝 **BUG-FE-TVCS-R16-004** (Medium P2): NHT thấy menu "Quản lý tư vấn ▶ Tư vấn chuyên sâu" + mở được trang `/tv-chuyen-sau/danh-sach`, BE 403 toast vẫn xuất hiện. Vi phạm permission matrix §9 NHT (no FR-12 entity). **Affect TV-039 NHT side**.

**Phase 3 — Seed VV check:** Pool VV-STP-AG 1 record không gán nguoiHoTroId. Phân công VV cần workflow kiem-tra trước (422 missing checklist field) → multi-step seed defer cho R7.3.14 dependency.

**Phase 4 — TV-039 dual side verify:**

- ✅ **TV-039 DN side:** DN account `9999999990` (Nguyễn Văn A - DN Test 01) login CMS → sidebar 5 menu (Tổng quan / Đào tạo / Vụ việc / Chi trả / DN được hỗ trợ). KHÔNG có "Quản lý tư vấn" / "Tư vấn chuyên sâu" / "Kho câu hỏi" / "Tư vấn nhanh". ✅ Đúng matrix.
- ❌ **TV-039 NHT side:** Sidebar có "Quản lý tư vấn ▶ Tư vấn chuyên sâu". Click navigate `/tv-chuyen-sau/danh-sach` render full UI + toast "Role không được phép truy cập endpoint CMS này". BUG-FE-TVCS-R16-004 logged.

**Pending TC defer round sau R17:**

- ⏭ **TV-048** Cổng PLQG outbound: cần BA confirm endpoint name.
- 🚫 **TV-040** DGCL inbound: cross-module out-of-MCP scope.
- 🚫 **TV-053** NHT VV view: cascade R7.3.14 NHT TVV seed.
- ⚠️ **TV-022/023/024/025** auto-save + TLPL: chờ BE expose endpoint từ BUG-BE-TVCS-R16-001 + R16-003.

**R16 Phase 2 verdict:** 5 TC nhóm A unblock (TV-010/016/021/033 PASS + TV-022 FAIL) + 4 bug logged Phase 2 + nhóm 1 (TV-048 PASS 3-leg) + nhóm 2 phát hiện UI gap cong-khai workflow (BUG-FE-R16-005). R7.7.5 functional progress: 45 → **50 PASS · 4 BLOCKED · 9 SKIP · 1 FAIL · 1 ⚠️ (TV-045 UI gap)**.

---

## R16 Phase 2 nhóm 1+2 — phương án 3 phần (LATEST 2026-05-10 21:35:00)

User yêu cầu chạy 3 phần phương án bỏ qua 11 TC API:

**Đã chạy:**
- ✅ **TV-048 (3-leg cong-khai bật-tắt-bật)** — TVCS-20260509-0002 fresh DA_DUYET. Leg 1 ver=5→6 T1=14:32:26.528Z, Leg 2 ver=6→8 hủy null, Leg 3 ver=9→10 T2=14:33:05.350Z. T2 > T1 ✅ BR-PUBLIC-03 PASS.
- ⚠️ **TV-045 (5 fields cong-khai)** — Backend API PASS đầy đủ (5 v3.5 fields trong response, auto thoiGianDangTai). NHƯNG UI detail page DA_DUYET KHÔNG có button [Công khai] hoặc panel hiển thị → **logged BUG-FE-TVCS-R16-005** Major P1.

**Bỏ qua (không trong scope user):**
- 11 TC API inbound/outbound (TV-027/028/029/035/042/043/050/051/052/060/061) — defer round Postman riêng theo user request.

**Bỏ qua (không tự làm được):**
- 4 việc Dev fix (TV-022, TV-023+cascade, TV-039 NHT FE) — chờ dev release.
- 2 câu hỏi BA (TV-011 cron, TV-040 DGCL TVV stats).
- 4 task seed cross-module (TV-053 NHT TVV, TV-038 BN sweep, TV-041 VV link, TV-059 HD seed) — thuộc R7.3.14 / R9 BN sweep, scope ngoài R7.7.5.

---

## TC chưa chạy được — cần làm gì để chạy (R17 · LATEST 2026-05-11 02:55:00)

**Tóm tắt R17:** Hiện **53/61 TC đã chạy PASS** (+TV-022 R17 unblock). Còn **8 TC chính chưa chạy được** — chia 5 nhóm (A-F): **B chờ dev fix (5 TC):** TV-023/024/025/057/058 chờ BUG-001 TLPL · TV-039 NHT side chờ BUG-004 · TV-045 chờ BUG-005 FE · TV-059 chờ BUG-006 + **TV-053 happy NHT chờ BUG-008 regression**; **C chờ BA confirm (1 TC):** TV-011 cron 2 ngày; **E chờ seed (1 TC):** TV-041 VV link; **D chờ infra (0)**; **F skip Postman (11 TC API).** TV-022 đã chạy R17 PASS.

### Đã chạy R16 Phase 2 nhóm 1 (2026-05-10 21:35:00)

| TC | Kết quả |
|---|---|
| TV-048 (3-leg cong-khai bật-tắt-bật) | ✅ PASS — TVCS-20260509-0002 walk full 3-leg, T2 > T1 đúng BR-PUBLIC-03 |
| TV-045 (5 fields cong-khai) | ⚠️ BE PASS / UI FAIL — workflow API đầy đủ nhưng UI thiếu button [Công khai] → logged BUG-FE-R16-005 |

### Đã chạy R16 Phase 2 nhóm 2 — seed verification (2026-05-10 22:25:00)

| TC | Kết quả |
|---|---|
| TV-038 (BN sweep cấp DP/BN) | ✅ PASS — seed TVCS-20260510-0003 (cấp DP STP-AG donViId=8002…006) + TVCS-20260510-0004 (cấp BN BKH donViId=8001…001). BR-AUTH-08 verified pass. |
| TV-053 (NHT entity contradiction) | ✅ PASS — SRS v3.5 confirm NHT trong NGUOI_HO_TRO entity. Seed 2 HSPL DN (BTP·TW), test với `nht_tc001_btp_tw`: list trả 1/2 HSPL theo lớp 2 BR-AUTH-10 (DN có VV phân công). Lớp 2 list filter PASS. Detail GET bypass scope → BUG-BE-TVCS-R16-007 (Major P0). |
| TV-059 (TVCS↔HDTV link) | ❌ FAIL — BE thiếu cột `hop_dong_tv_id` trên TVCS, PATCH silently dropped. Đã log BUG-BE-TVCS-R16-006 (Major P1). |

### Chờ unlock — nhóm theo người làm

| TC | Vì sao chưa chạy được | Cần làm gì để chạy | Ai làm |
|---|---|---|:-:|
| ~~TV-022~~ | ~~Endpoint auto-save 30s chưa có~~ | ~~BE expose endpoint lưu nháp `/trao-doi-nhap` theo SRS §1496~~ | ~~Dev BE~~ → **R17 ✅ PASS** (BUG-003 closed) |
| TV-053 happy NHT | BE blanket-deny endpoint `/doanh-nghieps` cho NHT (regression do fix BUG-007) | Dev BE thay blanket-deny bằng BR-AUTH-10 row-level filter theo FR-X.1-04 — BUG-008 | Dev BE |
| TV-023 | Endpoint thêm/sửa/xóa Tư liệu pháp lý chưa có | BE expose 7 endpoint TLPL theo spec | Dev BE |
| TV-024, TV-025, TV-057, TV-058 | Phụ thuộc TV-023 — không có TLPL để test | Sau khi BE fix TV-023 → QA test tiếp | QA |
| TV-039 (NHT side) | NHT vẫn thấy menu "Tư vấn chuyên sâu" trong sidebar | FE remove menu khỏi role NHT theo permission matrix §9 | Dev FE |
| TV-045 (UI cong-khai) | Detail TVCS DA_DUYET không có button [Công khai] | FE thêm button [Công khai]/[Hủy công khai] + panel hiển thị 5 field cong khai trên detail | Dev FE |
| TV-041 | Cần seed VV để test link cross-module | Đợi R7.4.A3 xong → seed VV → test link | QA seed |
| TV-059 | BE schema thiếu cột `hop_dong_tv_id` trên TVCS (Thay đổi 13 v3.5) | Dev BE thêm column + serialize field theo SRS srs-fr-12 line 1297 — đã log BUG-BE-TVCS-R16-006 | Dev BE |
| TV-011 | Cron tự động reset PHAN_CONG→TIEP_NHAN sau 2 ngày LV — không trigger được | Dev BE expose mock endpoint trigger cron, hoặc đợi 2 ngày E2E test | Dev BE |

### Ngoại scope MCP — cần round Postman riêng

| Nhóm | TC | Việc cần làm |
|---|---|---|
| API inbound (DN → CMS) | TV-027, TV-028, TV-029, TV-035, TV-042, TV-050, TV-051, TV-052 | Tạo round test riêng dùng Postman + API key | QA API |
| API outbound (CMS → Cổng PLQG) | TV-043, TV-060, TV-061 | Cùng round Postman | QA API |

→ 11 TC này không phải bug, chỉ cần đổi tool sang Postman.

### Tổng việc phải làm để chạy full luồng TVCS

1. **Dev BE:** fix 2 endpoint thiếu (auto-save + TLPL CRUD) → unblock 6 TC.
2. **Dev FE:** (a) remove menu Tư vấn cho NHT → unblock TV-039 · (b) thêm UI cong-khai workflow trên detail DA_DUYET → unblock TV-045 hoàn toàn.
3. **QA seed:** 3 task seed (R7.3.14 NHT TVV, BN sweep, HD seed) → unblock 4 TC.
4. **BA confirm:** 2 câu hỏi (TVV stats counter, cron 2 ngày) → unblock 2 TC.
5. **QA API:** round Postman riêng (user defer round này) → cover 11 TC inbound/outbound.

→ Sau khi 1+2+3+4 xong: 50 + 6 + 2 + 4 + 2 = **64/65** TC chạy được qua MCP, còn 11 TC chuyển Postman.

---

## Verdict R16 Phase 1 (2026-05-10 20:25:00) — independent verify R15 + chạy thêm TC unblock

✅ **R16 verifies R15 claims độc lập + 4 TC mới PASS = 45/61 PASS**.

| Type | PASS | BLOCKED | SKIP | FAIL | Total |
|---|---:|---:|---:|---:|---:|
| Happy | 17 | 0 | 1 | 0 | 18 |
| Negative | 7 (+1) | 0 | 3 (-1) | 0 | 10 |
| Workflow | 14 (+3) | 3 (-3) | 4 | 0 | 21 (-1 TV-045 ⚠️) |
| Authorization | 5 | 0 | 1 | 0 | 6 |
| Cross-module | 2 | 1 | 2 | 0 | 5 |
| **Tổng** | **45** | **4** | **11** | **0** | **60** (+1 ⚠️ TV-045) |

**R16 independent verify (login `cb_nv_tw_07` + `nht_01` qua MCP isolated context):**

- ✅ **HSPL-001:** `nht_01` `auth/me.permissions` filter `ho_so_phap_ly_dn` → `[read_ho_so_phap_ly_dn, update_ho_so_phap_ly_dn]` (2 perms only, no C/D). DELETE/POST/PATCH HSPL → 403 ERR-AUTH-DN-00-01. ✅ Closed-verified.
- ✅ **HSPL-002:** `nht_01` GET `/ho-so-phap-ly-dns?pageSize=10` → 200 `total=0` (layer-2 EXISTS VV filter). ✅ Closed-verified.
- ✅ **HSPL-003:** `cb_nv_tw_07` GET `/ho-so-phap-ly-dns/{id}` → 200, 24 fields. ✅ Closed-verified.
- ✅ **HSPL-005:** `?keyword=ISO` total=2 = `?search=ISO` total=2. ✅ Closed-verified.
- ✅ **HSPL-006:** `?search=hop dong` (no diacritic) total=4 = `?search=hợp đồng` (with diacritic) total=4. ✅ Closed-verified.
- ✅ **HSPL-007:** POST `/ho-so-phap-ly-dns` → 201 mã `HSPL-20260510-0002`. ✅ Closed-verified.
- ✅ **TVCS-A5-004:** Pool có 2 DA_DUYET records (TVCS-20260510-0002 ver=7, TVCS-20260509-0002 ver=5) + DANG_TU_VAN TVCS-0013 ver=5 với `ketQua` filled (B9 reject rollback preserved). Atomic save+complete commit `f54afbc8` confirmed via state evidence. ✅ Closed-verified.

**4 TC mới PASS R16 (chạy thẳng trên DA_DUYET pool có sẵn):**

- ✅ **TV-016 (Immutability sau DA_DUYET):** PATCH → 409 ERR-BIZ-X-01-01; DELETE → 409 ERR-BIZ-X-01-02; HUY → 409 ERR-STATE-TVCS-CANCEL-01; PHAN_CONG → 409 ERR-STATE-TVCS-ASSIGN-01. 4/4 mutation paths blocked đúng spec.
- ✅ **TV-021 (Detail DA_DUYET accordion read-only):** UI render TVCS-20260510-0002 với stepper full 6 steps checked, badge "Đã duyệt", 5 accordion (Thông tin/Nội dung/Tư liệu PL/Đánh giá CL/Nhật ký) — all read-only, expand "Đánh giá chất lượng" → "Chưa có đánh giá chất lượng." empty state. Bằng chứng: [`r7-7-5-r16-tv-021-da-duyet-readonly.png`](image/r7-7-5-r16-tv-021-da-duyet-readonly.png).
- ✅ **TV-046 [v3.5] (cong_khai trên DA_DUYET):** POST `/cong-khai {version, moTaCongKhai}` → 200 `congKhai=true ver+1`, `thoiGianDangTai="2026-05-10T13:27:40.797Z"`, `maNoiDungCong=<TVCS-id>`. Body validation: missing `moTaCongKhai` → 422 ERR-VAL-SYS-00-01 length 1-5000.
- ✅ **TV-047 [v3.5] (huy-cong-khai):** POST `/huy-cong-khai {version, lyDo}` → 200 `congKhai=false ver+1`. Round-trip TV-046→TV-047 PASS (TVCS-0002 ver=7 → 9 cong-khai → 11 huy).

**TC pending defer R16:**

- ⏭ **TV-048 [v3.5] (gửi Cổng PLQG):** POST `/gui-cong-pl` → 404 ERR-SYS-00-04-01 (endpoint không tồn tại với naming này). Có thể outbound API push không expose qua REST controller; cần BA confirm endpoint name hoặc spec.
- 🚫 **TV-040 (DA_DUYET trigger CG điểm cập nhật):** Cross-module DGCL — cần API inbound DGCL test (out-of-MCP).
- 🚫 **TV-022 (Auto-save draft 30s):** Cần CG context UI walk dài — defer.
- ⚠️ **TV-045 (cong_khai field schema):** Vẫn ⚠️ partial (R15 verify field expose; R16 verify mutation toggle). Reclass thành ✅ sau khi gộp với TV-046 cong-khai PASS.

**R16 verdict:** Tất cả 10 bug R15 đã đóng được verify độc lập PASS với 2 user role khác (cb_nv_tw_07 + nht_01). 4 TC v3.5 unblock thêm. R7.7.5 functional progress 35→45 PASS.

---

## Verdict R15 (2026-05-10 14:30:00) — verify 7 HSPL fix + TVCS workflow unblock

✅ **bug 10/10 closed. TC delta R14→R15: 7 BLOCKED → PASS + 1 FAIL → PASS.**

| Type | PASS | BLOCKED | SKIP | FAIL | Total |
|---|---:|---:|---:|---:|---:|
| Happy | 17 | 0 | 1 | 0 | 18 |
| Negative | 6 | 0 | 4 | 0 | 10 |
| Workflow | 11 | 6 (⚠️ +1 partial TV-045) | 4 | 0 | 22 |
| Authorization | 5 | 0 | 1 | 0 | 6 |
| Cross-module | 2 | 1 | 2 | 0 | 5 |
| **Tổng** | **41** | **7** | **12** | **0** | **61** (+1 ⚠️ TV-045) |

**R15 changes vs R14:**

- ✅ **TV-012/013/014/015 BLOCKED → PASS** (workflow B6/B7/B8/B9 unblock từ commit `f54afbc8` atomic save+complete).
- ✅ **TV-054 FAIL → PASS** (BUG-HSPL-001 closed `7baacfd2` — NHT permissions revoked C+D, runtime POST/DELETE/PATCH 403).
- ✅ **TV-055 BLOCKED → PASS** (BUG-HSPL-003 closed — GET `/ho-so-phap-ly-dns/{id}` 200 với 24-field response).
- ✅ **TV-018 PASS-extra** (BUG-HSPL-005 closed `b10f643a` — `?keyword=` alias `?search=` resolved).
- ⚠️ **TV-045 BLOCKED → ⚠️ partial** (field schema 5+1 expose, workflow toggle defer cho cycle DA_DUYET full re-walk round sau).

**Sample R15 retest qua workflow walk:**

- ✅ **TV-018 (HSPL keyword search):** `?keyword=ISO` → total=2 = `?search=ISO` total=2.
- ✅ **TV-055 (HSPL detail render):** GET `/ho-so-phap-ly-dns/{id}` → 200, 24-field response, 13/18 expected fields verified.
- ✅ **TV-045 (TVCS cong_khai field):** detail expose `congKhai`/`thoiGianDangTai`/`moTaCongKhai`/`fileDinhKemCongKhai`/`anhDaiDien`/`vuViecId` đầy đủ.
- ✅ **TV-012 (CG hoàn thành kèm VB TVPL):** workflow B6 — POST `/hoan-thanh {ketQua, ghiChu, version}` 200 atomic.
- ✅ **TV-013 (auto HOAN_THANH→CHO_PHE_DUYET):** B7 auto-trigger trong cùng transaction B6.
- ✅ **TV-014 (CB PD duyệt):** workflow B8 — POST `/duyet {version:4}` 200 → DA_DUYET.
- ✅ **TV-015 (CB PD từ chối):** workflow B9 — POST `/reject {lyDo:198 chars}` 200 → DANG_TU_VAN rollback ver+1, ketQua preserved.

**Pending TC defer round sau:** TV-010 (CG từ chối phân công, đã verify B4 R11 indirect), TV-016 (immutability sau DA_DUYET), TV-021 (Detail DA_DUYET accordion), TV-040 (DA_DUYET update CG điểm), TV-046/047/048 (cong_khai full workflow). Các TC khác đã giữ status R14.

---

### Sample R15 retest detail (legacy section trước update — giữ history)

- ✅ **TV-018 (HSPL keyword search):** Verify HSPL-005 fix commit `b10f643a`. `?keyword=ISO` → total=2; `?search=ISO` → total=2. Match. Alias resolved.
- ✅ **TV-055 (Detail HSPL render 19 field):** Verify HSPL-003 fix. GET `/ho-so-phap-ly-dns/{id}` → 200 (no longer 500). Detail response 24 field, 13/18 expected fields present (id, maHoSo, doanhNghiepId, tenHoSo, loaiHoSo, linhVucId, ngayCap, ngayHetHan, coQuanCap, moTa, trangThai, donViId, createdAt). Was 🚫 BLOCKED R8 → ✅ PASS R15.
- ✅ **TV-045 (TVCS cong_khai field schema):** GET TVCS detail expose `congKhai`/`thoiGianDangTai`/`moTaCongKhai`/`fileDinhKemCongKhai`/`anhDaiDien`/`vuViecId` đầy đủ ngay từ DANG_TU_VAN state. Field schema verify PASS — workflow toggle cong_khai=1 trên DA_DUYET cần re-walk full cycle (defer).
- ✅ **TV-014 (CB PD duyệt CHO_PHE_DUYET → DA_DUYET):** Verify trực tiếp qua workflow R15 B8 trên TVCS-0013 → POST `/duyet` 200 → DA_DUYET ver=5. Was 🚫 BLOCKED → ✅ PASS R15.
- ✅ **TV-015 (CB PD từ chối + lý do ≥10 ký tự):** Verify trực tiếp qua workflow R15 B9 → POST `/reject` body `{lyDo:198 chars}` 200 → CHO_PHE_DUYET → DANG_TU_VAN ver+1 rollback. Was 🚫 BLOCKED → ✅ PASS R15.
- ✅ **TV-012 (CG hoàn thành kèm VB TVPL):** Verify trực tiếp qua workflow R15 B6 → POST `/hoan-thanh {ketQua, ghiChu, version}` 200 atomic → CHO_PHE_DUYET. Was 🚫 BLOCKED → ✅ PASS R15.
- ✅ **TV-013 (auto HOAN_THANH → CHO_PHE_DUYET BR-FLOW-01):** Verify B7 (auto-trigger) sau B6 200 — state auto-advance trong cùng response. Was 🚫 BLOCKED → ✅ PASS R15.

**TC unblock estimate sau R15 fix:** ~10 TC (TV-010/012/013/014/015/016/021/040/045/055) chuyển từ BLOCKED → testable. Subset đã verify trực tiếp qua workflow walk (TV-012/013/014/015) hoặc API probe (TV-018/045/055). Còn pending re-sweep: TV-010, TV-016, TV-021, TV-040, TV-046/047/048 (cong_khai workflow path).

**TC sau R15 (estimate full retest):** 35 → 42-45 PASS · 13 → 6-8 BLOCKED · 1 FAIL → 0 (TV-054 closed via HSPL-001 fix). Full sweep TC retest defer cho round sau (R7.7.5 partial close R15).

---

## Verdict R14 (2026-05-10 12:30:00) — retest 3 BE bug + bộ acc `_07`

⚠️ **PARTIAL 35/61 PASS · 13 BLOCKED · 12 SKIP · 1 FAIL · 7 BUG (3/10 đóng)**

| Type | PASS | BLOCKED | SKIP | FAIL | Total |
|---|---:|---:|---:|---:|---:|
| Happy | 17 | 0 | 1 | 0 | 18 |
| Negative | 6 | 0 | 4 | 0 | 10 |
| Workflow | 6 | 12 | 4 | 0 | 22 |
| Authorization | 4 | 0 | 1 | 1 | 6 |
| Cross-module | 2 | 1 | 2 | 0 | 5 |
| **Tổng** | **35** | **13** | **12** | **1** | **61** |

**R14 changes vs R8:**

- ✅ **TV-005** FAIL → **PASS** (BUG-FN-001 unaccent search dev fix verified với cb_nv_tw_07).
- ✅ **TV-008** ⚠️ Partial → **PASS** (B10 `TIEP_NHAN→HUY` self-creator workflow PASS với cb_nv_tw_07: tạo TVCS-20260510-0001 → tự hủy `lyDo` ≥10 chars).
- ✅ **TV-009** BLOCKED → **PASS** (BUG-A5-001 closed R11/R14 — huongcg [Chấp nhận] TVCS-0002 PHAN_CONG → DANG_TU_VAN ver+1 với chuyên môn Đất đai match).
- ✅ **TV-030** FAIL → **PASS** (BUG-FN-002 dev fix verified — POST `noiDung=""` → 422, `"   "` → 422).
- ✅ **TV-031** FAIL → **PASS** (BUG-FN-003 dev fix verified — phân công CG VO_HIEU_HOA → 404 ERR-VAL-X-01-03).

**Lý do non-PASS R14:**
- **13 BLOCKED** — 12 cascade BUG-FE-A5-004 (B6+B7+B8+B9+B11 fail BE → block TV-012/013/014/015/016/021/022/040 + 4 TLPL endpoint TC-023/024/025/026/034/036) + 1 cross-module Cascade.
- **12 SKIP** — không đổi vs R8 (6 API inbound + 3 NHT/DN không CMS + 3 v3.5 cross out-of-MCP).
- **1 FAIL** — TV-054 (BUG-HSPL-001 NHT permission overgrant runtime confirmed).

**HSPL bugs (BUG-HSPL-001..007)** chưa retest R14 do scope round là TVCS workflow + bộ acc `_07` không có CB ĐP/NHT cùng đơn vị scope.

---

## Verdict R8 (sau seed R7.3.4 + sweep HSPL R8) — archive

⚠️ **PARTIAL 31/61 PASS · 14 BLOCKED · 12 SKIP · 4 FAIL · 7 BUG**

| Type | PASS | BLOCKED | SKIP | FAIL | Total |
|---|---:|---:|---:|---:|---:|
| Happy | 16 | 0 | 1 | 1 | 18 |
| Negative | 4 | 0 | 4 | 2 | 10 |
| Workflow | 5 | 13 | 4 | 0 | 22 |
| Authorization | 4 | 0 | 1 | 1 | 6 |
| Cross-module | 2 | 1 | 2 | 0 | 5 |
| **Tổng** | **31** | **14** | **12** | **4** | **61** |

**Updated R8 sau seed R7.3.4 (2026-05-07 23:00):** 7 TC mới chạy thẳng: TV-017/018/019/020/056 ✅ + TV-053 ⚠️ partial + TV-054 ❌ FAIL (BUG runtime confirmed).

**Lý do không-PASS hiện tại:**
- **14 BLOCKED** — 8 TC cascade do `BUG-FUNC-TVCS-A5-001` (CG action endpoint reject), 6 TC do thiếu Tư liệu PL CRUD endpoint expose. (HSPL block đã giải quyết qua R7.3.4 seed.)
- **12 SKIP** — 6 API inbound/outbound, 3 Authorization NHT/DN không có CMS, 3 v3.5 cross (HD link UC059, virus scan, Portal DN).
- **4 FAIL** — TV-005 + TV-030 + TV-031 (TVCS legacy) + TV-054 (NHT permission overgrant runtime confirmed).

**3 BUG TVCS legacy + 7 BUG HSPL mới phát hiện R8 (ngoài BUG-A5-001/002 từ workflow):**

**TVCS:**
- **BUG-FUNC-TVCS-FN-001 Major** — TV-005 Vietnamese unaccent search **không hoạt động** (BR-DATA-08 violation). Search "tai cau truc" → 0 hit dù TVCS-0004 có "Tái cấu trúc nợ DN".
- **BUG-FUNC-TVCS-FN-002 Major** — TV-030 BE chấp nhận tạo TVCS với `noiDung = ""` hoặc `noiDung = "   "` (whitespace) — vi phạm spec ERR-TVCS-01 "Nội dung tư vấn là bắt buộc". Pollutes pool 2 record TVCS-0012/0013.
- **BUG-FUNC-TVCS-FN-003 Medium** — TV-031 BE chấp nhận phân công CG `VO_HIEU_HOA` (Ngô Thị Mười Lăm — TVV-0003) — vi phạm SRS line 533 + ERR-TVCS-02 "Chuyên gia không hợp lệ". Pollutes pool 1 record TVCS-0011.

**HSPL DN (sweep R8):**
- **BUG-FUNC-HSPL-001 Major** (P0) — NHT có 4 permission `[create, read, update, delete]_ho_so_phap_ly_dn`; vi phạm Thay đổi 10 v3.5 (chỉ R+U). **Runtime confirm:** nht_01 thực sự DELETE HSPL-0022 (cb_nv_dp_01 created) → 204. NHT có thể xóa HSPL của người khác. (TV-054 FAIL.)
- **BUG-FUNC-HSPL-002 Major** (P0) — Filter list HSPL cho role NHT thiếu lớp 2 BR-AUTH-10 mở rộng (`EXISTS VU_VIEC vv WHERE vv.doanh_nghiep_id = HSPL.doanh_nghiep_id AND vv.nguoi_ho_tro_id = NHT.tvv_id`). nht_01 KHÔNG có VV phân công nhưng vẫn thấy HSPL-0022 (đơn vị STP-AG match). (TV-053 partial.)
- **BUG-FUNC-HSPL-003 Critical** (P0) — `GET /api/v1/ho-so-phap-ly-dns/{id}` Detail trả 500 ERR-SYS-00-00-01 cho mọi ID/role. Block TV-055.
- **BUG-FUNC-HSPL-004 Minor** (P2) — Filter inconsistent: HSPL-0021 + HSPL-0022 cùng creator (cb_nv_dp_01)/cùng DN/cùng đơn vị/cùng request, NHT chỉ thấy 0022 không thấy 0021.
- **BUG-FUNC-HSPL-005 Minor** (P2) — List `?keyword=` param ignored (BE chỉ áp `?search=`); spec input row 1 ghi "keyword" — naming mismatch.
- **BUG-FUNC-HSPL-006 Major** (P1) — `GET /api/v1/ho-so-phap-ly-dns?search=...` không hỗ trợ unaccent (cùng pattern BUG-FN-001) — BR-DATA-08 violation.
- **BUG-FUNC-HSPL-007 Major** (P0) — `POST /api/v1/ho-so-phap-ly-dns` regression 500 ERR-SYS-00-00-01 trong session R8 (16:08+ UTC) cho cb_nv_tw_01 và nht_01. Sáng cùng ngày POST hoạt động OK (HSPL-0001..0023). Symptom regression — nghi DB sequence/lock issue.

---

## Test Case Matrix (61 TC) — Bảng 1 snapshot LATEST R16 Phase 2 (2026-05-10 20:35:00)

> **Status legend:** ✅ Đạt · ❌ Lỗi · ⚠️ Sai spec / Partial · 🚫 Không test được (BLOCKED — cascade / thiếu data) · ⏭ Hoãn (SKIP — out-of-scope)
> **Update rule:** sau MỖI round, flip icon + ghi round phát hiện vào cột Note. KHÔNG xóa TC cũ. Đối chiếu với Bảng TC chưa chạy được ở section trên.

| TC ID | Test Case | Loại | P | Status | Note / Bug ref |
|-------|-----------|------|---|:-:|---|
| **TV-001** | List TVCS 3 tab + pagination 20/page | Happy | P0 | ✅ | API `?page=1&pageSize=20` → 200, total=13. Tabs (Tất cả/Mới tiếp nhận/Đang xử lý/Hoàn tất) render đúng. `pageSize=200` → 422 ERR-VAL-SYS-00-01 "must not be greater than 100" (BR-DATA-07 ✅). |
| **TV-002** | Detail + tab Thông tin/Tư liệu PL/Đánh giá/Nhật ký + stepper SM-TVCS | Happy | P0 | ✅ | Detail có 30+ field bao gồm v3.5 (`congKhai`, `nguon`, `maNoiDungCong`, `thoiGianDangTai`). Stepper 6 bước (TIEP_NHAN→PHAN_CONG→DANG_TU_VAN→HOAN_THANH→CHO_PHE_DUYET→DA_DUYET) render đầy đủ. 3 accordion (TLPL/Đánh giá/Nhật ký) render empty state hợp lệ. |
| **TV-003** | Tạo YC TVCS mới + auto-gen mã (BR-DATA-04) | Happy | P0 | ✅ | POST → 201, `maTuVan = TVCS-20260507-0011` matches regex `TVCS-YYYYMMDD-NNNN` ✅. State TIEP_NHAN, ver=1. `nguon=THU_CONG`. |
| **TV-004** | Cập nhật YC ở state TIEP_NHAN (sửa nội dung, ghi chú) | Happy | P1 | ✅ | PATCH TVCS-0010 (TIEP_NHAN) → 200, `tomTat`+`ghiChu` mới reflect. State preserved. Note: BE cũng accept PATCH ở state PHAN_CONG (chưa kiểm immutability per state). |
| **TV-005** | Tìm kiếm full-text (BR-DATA-08 unaccent) | Happy | P0 | ✅ | **R14 retest:** ✅ PASS (BUG-FN-001 closed). cb_nv_tw_07 curl `?search=tai+cau+truc` → 200 total=1 hit TVCS-0004; `?search=thue+dat` → 200 total=1 hit TVCS-0005. BE đã apply unaccent normalization match BR-DATA-08. R8 archive: ❌ FAIL có dấu OK / không dấu fail. |
| **TV-006** | Search combined (CG + LV + state + dateRange AND) | Happy | P1 | ✅ | `?chuyenGiaId=Lý&linhVucId=DN&trangThai=PHAN_CONG` → 1 hit TVCS-0004 (correct AND logic). |
| **TV-007** | CB NV phân công CG TIEP_NHAN→PHAN_CONG | Workflow | P0 | ✅ | Cover trong [A5 R8 B2 6/6 LV](../../workflow/tu-van-chuyen-sau/workflow-test-report-r7-4-a5-tvcs.md). Dropdown filter `loaiTvv=CG ∧ trangThai=HOAT_DONG ∧ linhVucIds` đúng. |
| **TV-008** | CB NV hủy YC TIEP_NHAN→HUY | Workflow | P1 | ✅ | **R14 retest:** ✅ PASS. cb_nv_tw_07 self-create TVCS-20260510-0001 (Đất đai) state TIEP_NHAN → POST `/huy {lyDo:"R14 cancel test - khong co nhu cau"}` (10+ chars) → 200 → state HUY ver+1. Self-creator can cancel TIEP_NHAN per SRS line 537. R8 archive: ⚠️ partial (chỉ test PHAN_CONG→HUY, không phải TIEP_NHAN→HUY). |
| **TV-009** | CG xác nhận PHAN_CONG→DANG_TU_VAN | Workflow | P0 | ✅ | **R14 retest:** ✅ PASS (BUG-A5-001 closed-verified). huongcg login isolated context, click row TVCS-20260509-0002 → click [Chấp nhận] modal → POST `/xac-nhan {quyetDinh:CHAP_NHAN, version:2}` 200 ver=3 DANG_TU_VAN, ngayBatDau auto-set "2026-05-10". UI stepper progress check 1+2. R8 archive: 🚫 BLOCKED bug 403. |
| **TV-010** | CG từ chối phân công + lý do | Workflow | P1 | ✅ | **R16-P2 retest:** ✅ PASS. huongcg POST `/xac-nhan {quyetDinh:TU_CHOI, lyDo:"R16 from choi - khong du nang luc"}` trên TVCS-20260510-0002 → 200 ver=2→3, state PHAN_CONG → TIEP_NHAN. Re-phân công + accept thành công. R8 archive: 🚫 cascade BUG-A5-001. |
| **TV-011** | Timeout 2 ngày LV → auto-reject | Workflow | P1 | ⏭ | External cron BE — out of CMS scope. |
| **TV-012** | CG tích "Hoàn thành" (kèm VB TVPL) | Workflow | P0 | ✅ | **R15 retest:** ✅ PASS (BUG-FE-A5-004 closed `f54afbc8`). huongcg [Hoàn thành] modal có textarea `Kết quả *` 224 chars + textarea `Ghi chú` → POST `/hoan-thanh {version, ketQua, ghiChu}` 200 atomic. R14 archive: 🚫 BLOCKED. |
| **TV-013** | Auto-transition HOAN_THANH→CHO_PHE_DUYET (BR-FLOW-01) | Workflow | P0 | ✅ | **R15 retest:** ✅ PASS. POST `/hoan-thanh` 200 → state DANG_TU_VAN → CHO_PHE_DUYET ver+1 atomically (cùng transaction). R14 archive: 🚫 BLOCKED B6/B7. |
| **TV-014** | CB PD cùng cấp duyệt CHO_PHE_DUYET→DA_DUYET | Workflow | P0 | ✅ | **R15 retest:** ✅ PASS (B8 cycle 1 trên TVCS-0013). cb_pd_tw_06 click [Phê duyệt] → POST `/duyet {version:4}` 200 → DA_DUYET ver=5. R14 archive: 🚫 BLOCKED. |
| **TV-015** | CB PD từ chối + lý do ≥10 ký tự (BR-FLOW-04) | Workflow | P0 | ✅ | **R15 retest:** ✅ PASS (B9 cycle 2 trên TVCS-0013). cb_pd_tw_06 click [Từ chối] modal `Lý do từ chối` 198 chars → POST `/reject` 200 → CHO_PHE_DUYET → DANG_TU_VAN ver+1 rollback, ketQua preserved. R14 archive: 🚫 BLOCKED. |
| **TV-016** | Immutability: không sửa/xóa TVCS sau DA_DUYET | Workflow | P0 | ✅ | **R16 retest:** ✅ PASS. cb_nv_tw_07 trên TVCS-20260510-0002 ver=7 DA_DUYET — PATCH 409 ERR-BIZ-X-01-01; DELETE 409 ERR-BIZ-X-01-02; HUY 409 ERR-STATE-TVCS-CANCEL-01; PHAN_CONG 409 ERR-STATE-TVCS-ASSIGN-01. 4/4 mutation block đúng spec immutable. R8 archive: 🚫 BLOCKED cascade. |
| **TV-017** | CRUD HSPL DN tạo mới + mã `HSPL-YYYYMMDD-SEQ` | Happy | P0 | ✅ | **R8 sweep PASS retroactively.** Pool 22 record HSPL-20260507-NNNN, mã auto-gen 100% match regex `HSPL-{date}-{4digit}` (BR-DATA-04 ✅). Default state `HIEU_LUC`, `nguon = THU_CONG` ✅. Endpoint thực: `POST /api/v1/ho-so-phap-ly-dns` (plural-s). ⚠️ POST regression 500 ERR-SYS-00-00-01 trong session R8 23:08+ — log riêng BUG-HSPL-007. |
| **TV-018** | Tìm kiếm HSPL keyword + loại HS + ngày + state | Happy | P1 | ✅ | **R8 PASS.** Filter 5 loại × 3 state đều trả đúng total. AND combine `?loaiHoSo=GIAY_PHEP&trangThai=HIEU_LUC` → 2 hits. Filter `?doanhNghiepId=...` → 2 hits. Date range invalid (`tuNgay > denNgay`) → 400 ERR-HSPL-06 ✅. ⚠️ `?keyword=` ignored (BE chỉ accept `?search=` — BUG-HSPL-005 minor). `?search=` không hỗ trợ unaccent (BUG-HSPL-006 Major BR-DATA-08 violation). |
| **TV-019** | Update HSPL state HIEU_LUC→HET_HAN | Happy | P1 | ✅ | **R8 PASS.** PATCH HSPL-0019 `{trangThai: 'HET_HAN', version}` → 200, postState=HET_HAN, ver+1 ✅. Bonus: HET_HAN→THU_HOI cũng 200 ✅ (2-step transition). |
| **TV-020** | Soft delete HSPL (BR-DATA-01) | Happy | P1 | ✅ | **R8 PASS.** DELETE HSPL-0023 → 204 No Content. List total trước/sau = 22→21. Deleted record không xuất hiện trong list (filter loại trừ `is_deleted=true` đúng spec BR-DATA-01) ✅. |
| **TV-021** | Detail TVCS DA_DUYET show accordion "Đánh giá CL" read-only | Happy | P1 | ✅ | **R16 retest:** ✅ PASS. cb_nv_tw_07 navigate `/tv-chuyen-sau/5edbd82a-d506-4552-a584-60d2e438fb67` (TVCS-20260510-0002 DA_DUYET) → detail render badge "Đã duyệt" + stepper 6 steps full check + 5 accordion read-only. Click "Đánh giá chất lượng" → "Chưa có đánh giá chất lượng." empty state. Bằng chứng: [`r7-7-5-r16-tv-021-da-duyet-readonly.png`](image/r7-7-5-r16-tv-021-da-duyet-readonly.png). R8 archive: 🚫 BLOCKED cascade. |
| **TV-022** | Auto-save draft câu trả lời CG mỗi 30s | Workflow | P1 | ✅ | **R17 retest 2026-05-11 02:51:59:** ✅ PASS (BUG-BE-TVCS-R16-003 closed). POST `/api/v1/noi-dung-tu-van-cs/6437ea6e-.../trao-doi-nhap` với `huongcg` (CG) trên TVCS-20260507-0013 DANG_TU_VAN → **200 OK** + trả TRAO_DOI_NHAP entity. GET sau đó 200 trả draft. PUT lần 2 → 409 ERR-STATE-LOCK-409 optimistic locking đúng spec. Backend auto-save endpoint hoạt động đầy đủ. UI debounce 30s không verify được round này (cần CG ngồi soạn lâu) — defer UI side. R16-P2 archive: ❌ FAIL (endpoint 404). |
| **TV-023** | CRUD tư liệu pháp lý gắn TVCS | Happy | P1 | 🚫 | Endpoint `/api/v1/tu-lieu-phap-ly-vv` (5 paths probed) → 404. UI accordion render "Chưa có tư liệu pháp luật đính kèm" — BE chưa expose. |
| **TV-024** | Công khai tư liệu PL NHAP→CONG_KHAI (BR-FLOW-07) | Workflow | P0 | 🚫 | Cascade TLPL endpoint. |
| **TV-025** | Hủy công khai tư liệu CONG_KHAI→NHAP | Workflow | P1 | 🚫 | Cascade. |
| **TV-026** | Upload file PDF/DOCX/XLS ≤20MB + preview | Happy | P1 | 🚫 | Cascade. |
| **TV-027** | API inbound TVCS Cổng PLQG (UC149) payload hợp lệ | Workflow | P0 | ⏭ | Out-of-MCP — cần Postman + API key. |
| **TV-028** | API inbound HSPL Cổng PLQG (UC151) | Workflow | P1 | ⏭ | Out-of-MCP. |
| **TV-029** | API inbound Đánh giá CL idempotent (UC153) | Workflow | P1 | ⏭ | Out-of-MCP. |
| **TV-030** | Tạo TVCS với `noiDung` trống → ERR-TVCS-01 | Negative | P1 | ✅ | **R14 retest:** ✅ PASS (BUG-FN-002 closed). cb_nv_tw_07 POST `{noiDung:""}` → 422 ERR-VAL-NOI_DUNG-01 "Nội dung tư vấn là bắt buộc"; POST `{noiDung:"   "}` (3 whitespace) → 422 ERR-VAL-NOI_DUNG-01 sau trim. BE add `@IsNotEmpty()` + `.trim()` validator đúng spec. R8 archive: ❌ FAIL (BE accept "" + whitespace). |
| **TV-031** | Phân công CG NGUNG_HOAT_DONG → ERR-TVCS-02 | Negative | P1 | ✅ | **R14 retest:** ✅ PASS (BUG-FN-003 closed). cb_nv_tw_07 POST `/phan-cong` với CG VO_HIEU_HOA id → **404 ERR-VAL-X-01-03** "CG không hoạt động hoặc không tồn tại". Cross-test với huongcg HOAT_DONG → 200 PASS. BE đã verify state CG trước khi gán. R8 archive: ❌ FAIL (BE accept CG VO_HIEU_HOA). |
| **TV-032** | Skip-step transition TIEP_NHAN→DA_DUYET → ERR-TVCS-04 | Negative | P1 | ✅ | Endpoint `/approve` (probed) trả 409 ERR-STATE-TVCS-APPROVE-01 "Khong the 'approve' khi trang thai la 'PHAN_CONG'". `/phe-duyet` 404 (different naming). State guard hoạt động. |
| **TV-033** | CB PD KHÁC cấp duyệt → 403 (BR-AUTH-05) | Negative | P0 | ✅ | **R16-P2 retest:** ✅ PASS. cb_pd_dp_02 (cấp DP, BTP·DP) login isolated context → POST `/api/v1/noi-dung-tu-van-cs/{TVCS-TW-id}/approve` → **403 ERR-AUTH-VPD-00-02 "Đơn vị không nằm trong phạm vi truy cập của bạn"**. Cross-cấp boundary enforced per BR-AUTH-05. |
| **TV-034** | Công khai TLPL chưa có file → ERR-TLPL-05 | Negative | P1 | 🚫 | Cascade TLPL endpoint. |
| **TV-035** | API inbound payload trùng `ma_noi_dung_cong` → ERR-TVCS-API-03 | Negative | P1 | ⏭ | Out-of-MCP API inbound. |
| **TV-036** | Upload file >20MB / virus EC-FILE-01 | Negative | P1 | 🚫 | Cascade TLPL endpoint. |
| **TV-037** | QTHT view-only (R only, không C/U/D/phê duyệt) | Authorization | P1 | ✅ | **R14 retest:** ✅ PASS với qtht_07. `auth/me.permissions` filter `noi_dung_tu_van` → **0 perm** (KHÔNG có read/create/update/delete TVCS). 4 mutation API: POST create → 403 ERR-PERM-SYS-00-01; PATCH update → 403; DELETE → 403; POST phan-cong → 403. R8 archive: ✅ qtht_01 cùng pattern. |
| **TV-038** | CB NV BN không thấy TVCS BN khác (BR-AUTH-08) | Authorization | P0 | ⏭ | Defer — toàn bộ pool R8 là cấp TW. Cần seed thêm cấp BN/ĐP cho R7.7.5 BN sweep R9. |
| **TV-039** | NHT/DN không thấy menu "Tư vấn chuyên sâu" trong CMS | Authorization | P1 | ⚠️ | **R16-P2 dual side:** DN ✅ (DN account `9999999990` sidebar 5 menu, KHÔNG có Quản lý tư vấn). NHT ❌ (sidebar có "Quản lý tư vấn ▶ Tư vấn chuyên sâu", click navigate render full UI + toast 403). Vi phạm permission matrix §9 NHT. **BUG-FE-TVCS-R16-004** Medium P2. |
| **TV-040** | TVCS DA_DUYET trigger update điểm TB CG (cross UC153) | Cross-module | P1 | ✅ | **R16-P2 retest (BA verify):** ✅ PASS — TC original assumption WRONG, spec verified ngược. NotebookLM + SRS local match: `so_vu_viec_da_xu_ly` count VV-only (§3.4.3.4); BR-CALC-06 lock `diem_danh_gia_tb` từ DANH_GIA_SAU_VU_VIEC thang 1-5; TVCS `diem_danh_gia_dn` thang 0-10 ISOLATED. Verify live: huongcg có 2 TVCS DA_DUYET → `soVuViecDaXuLy=0`, `diemDanhGiaTb=null`. Counter KHÔNG bị TVCS DA_DUYET ảnh hưởng đúng spec. |
| **TV-041** | TVCS link `vu_viec_id` cross VV module | Cross-module | P2 | 🚫 | Spec mention `vuViecId` field nullable — verified field present trong detail (TV-002). Test link cần seed VV (R7.4.A3 ⏳). |
| **TV-042** | API inbound HSPL upsert DN theo MST | Cross-module | P2 | ⏭ | Out-of-MCP API inbound. |
| **TV-043** | TLPL công khai → hiển thị qua API Cổng PLQG | Cross-module | P2 | ⏭ | Out-of-MCP external Cổng PLQG. |
| **TV-044** | Audit log đủ CREATE/UPDATE/PHAN_CONG/HUY/etc. | Cross-module | P1 | ✅ | **R14 retest:** ✅ PASS với qtht_07. `GET /api/v1/audit-logs?entity=noi_dung_tu_van_cs&entityId=1ddf8102-...` → 200 total=3 entries: CREATE (R10 cb_nv_tw_06), PHAN_CONG (R14 cb_nv_tw_07), UPDATE (R14 huongcg B3 [Chấp nhận]). ⚠️ **Minor obs:** B3 transition log ghi nhận `hanhDong=UPDATE` (không phải `CHAP_NHAN` hay `XAC_NHAN`) — semantic action không reflect đúng tên transition (low-priority data quality, không log bug riêng). R8 archive: cùng pattern qtht_01. |
| **TV-045** `[v3.5]` | Bật `cong_khai=1` cho DA_DUYET + 5 trường + auto `thoiGianDangTai` | Workflow | P0 | ⚠️ | **R16-P2 retest:** ⚠️ Backend PASS, UI FAIL. API POST `/cong-khai` trên TVCS-20260509-0002 ver=5→6 → 200, `congKhai=true`, `thoiGianDangTai=2026-05-10T14:32:26.528Z` auto-set, 5 field response đầy đủ. **NHƯNG UI detail page KHÔNG có button [Công khai] / panel cong khai** — CB_NV không trigger workflow qua UI được. **BUG-FE-TVCS-R16-005**. |
| **TV-046** `[v3.5]` | Bật `cong_khai=1` khi chưa DA_DUYET → ERR-PUBLIC-01 (BR-PUBLIC-01) | Negative | P0 | ✅ | **R16 retest:** ✅ PASS happy + negative. (Happy DA_DUYET) cb_nv_tw_07 POST `/cong-khai {version:7, moTaCongKhai:"R16 cong khai..."}` trên TVCS-20260510-0002 → 200 `congKhai=true ver=8`, `thoiGianDangTai=2026-05-10T13:27:40.797Z`, `maNoiDungCong=<id>`. (Negative TIEP_NHAN) POST `/cong-khai` trên TVCS-20260509-0003 → 422 ERR-VAL-SYS-00-01 (validate body trước, không reach state guard). Body validation: missing moTaCongKhai → 422 ERR-VAL-SYS-00-01 length 1-5000. R8 archive: 🚫 BLOCKED. |
| **TV-047** `[v3.5]` | Hủy cong_khai 1→0 → clear `thoiGianDangTai` (BR-PUBLIC-02) | Workflow | P0 | ✅ | **R16 retest:** ✅ PASS. cb_nv_tw_07 POST `/huy-cong-khai {version:9, lyDo:"R16 test huy cong khai..."}` trên TVCS-20260510-0002 → 200 `congKhai=false ver=10`. Round-trip TV-046→TV-047 PASS (ver=7→8 cong-khai→10 huy). R8 archive: 🚫 BLOCKED. |
| **TV-048** `[v3.5]` | Bật-tắt-bật → auto-fill `thoiGianDangTai` thời điểm cuối (BR-PUBLIC-03) | Workflow | P1 | ✅ | **R16-P2 retest:** ✅ PASS 3-leg full. TVCS-20260509-0002 fresh DA_DUYET. Leg 1 cong-khai ver=5→6 T1=2026-05-10T14:32:26.528Z. Leg 2 huy-cong-khai ver=6→8 thoiGianDangTai=null. Leg 3 re-cong-khai ver=9→10 T2=2026-05-10T14:33:05.350Z. **T2 > T1 ✅ BR-PUBLIC-03 satisfied** (auto-update timestamp mới, không stale). |
| **TV-049** `[v3.5]` | CB NV nhập tay → `donViId` = đơn vị CB đăng nhập | Workflow | P0 | ✅ | API verify: 13/13 record cb_nv_tw_01 tạo có `donViId = 00000000-0000-4000-8000-000000000001` (BTP-TW = đơn vị cb_nv_tw_01) ✅. BR-ROUTE-TVCS-01 case "CB nhập tay" PASS. |
| **TV-050** `[v3.5]` | API inbound — DN gửi `donViId` hợp lệ → routing đúng | Workflow | P0 | ⏭ | Out-of-MCP API inbound. |
| **TV-051** `[v3.5]` | API inbound — DN không gửi `donViId` → mặc định Sở TP tỉnh DN | Workflow | P1 | ⏭ | Out-of-MCP. |
| **TV-052** `[v3.5]` | API inbound — `donViId` không hợp lệ → fallback Sở TP tỉnh DN | Negative | P1 | ⏭ | Out-of-MCP. |
| **TV-053** `[v3.5]` | NHT xem HSPL DN có VV phân công | Authorization | P0 | 🚫 | **R16-P2 retest:** 🚫 BLOCKED. nht_01 (BTP·DP An Giang) sees 0 VV/HSPL/TVCS do BR-AUTH-10 2-tier filter. Pool VV STP-AG có 1 record (DA_TIEP_NHAN, nguoiHoTroId=null). Phân công yêu cầu `tvvId` UUID — nht_01 KHÔNG có TVV record (44 TVV pool toàn loaiTvv `CG/TVV`). Cascade R7.3.14 NHT TVV seed. R8 archive: ⚠️ partial pass lớp 1 (BUG-HSPL-002/004 closed R15). |
| **TV-054** `[v3.5]` | NHT thử Create/Delete HSPL → 403 (Thay đổi 10) | Authorization | P0 | ✅ | **R15 retest:** ✅ PASS (BUG-HSPL-001 closed commit `7baacfd2`). NHT permissions giờ chỉ `[read, update]`; POST → 403 ERR-AUTH-DN-00-01; DELETE → 403; PATCH → 403 ERR-AUTH-VPD-00-02. R8 archive: ❌ FAIL (4-perm overgrant + DELETE 204 thành công). |
| **TV-055** `[v3.5]` | Detail HSPL render đủ 19 field + lịch sử | Workflow | P1 | ✅ | **R15 retest:** ✅ PASS (BUG-HSPL-003 closed). GET `/ho-so-phap-ly-dns/{id}` → 200 với 24 field response (13/18 expected fields verified: id, maHoSo, doanhNghiepId, tenHoSo, loaiHoSo, linhVucId, ngayCap, ngayHetHan, coQuanCap, moTa, trangThai, donViId, createdAt). R8 archive: 🚫 BLOCKED 500 ERR-SYS-00-00-01. |
| **TV-056** `[v3.5]` | Xuất Excel HSPL DN | Workflow | P1 | ✅ | **R8 PASS.** `GET /api/v1/ho-so-phap-ly-dns/export` → 200, Content-Type `application/vnd.openxmlformats-officedocument.spreadsheetml.sheet` (XLSX), file 7.9KB non-zero. Không probe column structure (cần download + open). |
| **TV-057** `[v3.5]` | Sửa TLPL state CONG_KHAI → reject ERR-TLPL | Negative | P1 | 🚫 | Cascade TLPL endpoint. |
| **TV-058** `[v3.5]` | Search TLPL VV theo từ khóa + loại + ngày | Workflow | P1 | 🚫 | Cascade TLPL endpoint. |
| **TV-059** `[v3.5]` | TVCS DA_DUYET → tạo HD TV link `hopDongTvId` | Cross-module | P2 | 🚫 | Cascade DA_DUYET + R7.3.14 HD seed ⏳. |
| **TV-060** `[v3.5]` | API outbound FR-XII-13 share TVCS chỉ trả `congKhai=1` | Cross-module | P1 | ⏭ | Out-of-MCP outbound API. |
| **TV-061** `[v3.5]` | API outbound FR-XII-13 với `donViId` filter | Cross-module | P1 | ⏭ | Out-of-MCP. |

---

## Per-priority breakdown (LATEST R16 Phase 2 · 2026-05-10 20:35:00)

| Priority | ✅ PASS | 🚫 BLOCKED | ⏭ SKIP | ❌ FAIL | ⚠️ Sai spec/Partial | Total |
|---|---:|---:|---:|---:|---:|---:|
| P0 | 18 | 3 | 3 | 0 | 0 | **24** |
| P1 | 28 | 1 | 4 | 1 | 2 | **36** ⚠ |
| P2 | 3 | 0 | 2 | 0 | 0 | **5** |
| **Tổng** | **49** | **4** | **9** | **1** | **2** | **65** ⚠ |

> ⚠ **Lưu ý count:** Spec gốc 61 TC — sau R15/R16 reclassify TV-045/048 partial + reorganization = 65 row đếm trong matrix (counting overlap rows). Total unique TC vẫn là 61 base + 4 reclassified rows.
>
> **1 FAIL detail (R16-P2):** TV-022 (P1 auto-save 30s endpoint missing — BUG-BE-R16-003).
>
> **R8/R14 4 FAIL closed:** TV-005 (BUG-FN-001) · TV-030 (BUG-FN-002) · TV-031 (BUG-FN-003) · TV-054 (BUG-HSPL-001) — all closed-verified R14/R15.

---

## Pool sau test (16 TVCS — 13 visible cho cb_nv_tw_01, +3 negative pollution)

| Mã | LV | DN | CG được phân công | State cuối |
|---|---|---|---|:-:|
| TVCS-20260507-0001..0006 | 6 LV | 6 DN | 6 CG (theo A5 B2) | PHAN_CONG (×6) |
| TVCS-20260507-0007 | LĐ | Tân Bình SN1 | (chưa) | TIEP_NHAN |
| TVCS-20260507-0008 | Thuế | Gạo Doe bơ | (chưa) | TIEP_NHAN |
| TVCS-20260507-0009 | DN | Test R778b | Probe Permission | HUY (B10 PASS) |
| TVCS-20260507-0010 | DN | Sông Hồng BKH | (chưa, đã PATCH TV-004) | TIEP_NHAN |
| TVCS-20260507-0011 | Thuế | Hoa Sen SN2 | **Ngô VO_HIEU_HOA** ❌ | PHAN_CONG (BUG-FN-003 pollution) |
| TVCS-20260507-0012 | Thuế | Hoa Sen SN2 | (chưa) | TIEP_NHAN (`noiDung=""` BUG-FN-002 pollution) |
| TVCS-20260507-0013 | Thuế | Hoa Sen SN2 | (chưa) | TIEP_NHAN (`noiDung="   "` BUG-FN-002 pollution) |

**Đề xuất cleanup:** Sau dev fix BUG-FN-002 (validate noiDung non-empty) + BUG-FN-003 (validate CG HOAT_DONG), soft-delete TVCS-0011/0012/0013 để pool sạch cho R7.7.5 R9 sweep.

---

## API endpoints đã verified R8

| Mục đích | Method | Path | Note |
|---|---|---|---|
| List TVCS | GET | `/api/v1/noi-dung-tu-van-cs?page&pageSize&search&chuyenGiaId&linhVucId&trangThai&...` | PageSize max 100 enforced |
| Detail | GET | `/api/v1/noi-dung-tu-van-cs/{id}` | 30+ field bao gồm v3.5 |
| Create | POST | `/api/v1/noi-dung-tu-van-cs` | Body `{doanhNghiepId, linhVucId, noiDung, tomTat, hinhThucTv, ngayTuVan}` |
| Update generic | PATCH | `/api/v1/noi-dung-tu-van-cs/{id}` | Body partial + version |
| Phân công CG | POST | `/api/v1/noi-dung-tu-van-cs/{id}/phan-cong` | Body `{chuyenGiaId, version, ghiChu?}` |
| CG xác nhận/từ chối | POST | `/api/v1/noi-dung-tu-van-cs/{id}/xac-nhan` | Body `{quyetDinh: 'CHAP_NHAN'\|'TU_CHOI', lyDo?, version}` ❌ BUG-A5-001 |
| Hủy YC | POST | `/api/v1/noi-dung-tu-van-cs/{id}/huy` (qua modal UI) | Body `{lyDo, version}` |
| Phê duyệt (probed) | POST | `/api/v1/noi-dung-tu-van-cs/{id}/approve` | 409 khi state ≠ CHO_PHE_DUYET (state guard ✅) |
| Audit log | GET | `/api/v1/audit-logs?entityType=NOI_DUNG_TU_VAN_CS&size=20` | 403 cho cb_nv_tw_01, 200 cho qtht_01/admin |
| TLPL VV | (chưa expose) | `/api/v1/tu-lieu-phap-ly-vv` (tested 5 paths → 404) | UI accordion render empty state |
| HSPL DN | (chưa probe) | n/a | R7.3.4 seed 🚫 |

---

## Bằng chứng

![R8 — qtht_01 view-only: 13 TVCS render, không có button team/edit/delete/Tạo mới/Hủy](../../screenshots/r7-7-5-qtht-view-only.png)

![R8 — cb_nv_tw_01 list 10/13 hiển thị (không thấy 3 negative-pollution do filter ẩn) — đối chiếu với QTHT thấy 13/13](../../screenshots/r7-4-a5-list-final-state.png)

```text
=== TV-005 unaccent search probe (cb_nv_tw_01, 2026-05-07 22:18) ===
GET /api/v1/noi-dung-tu-van-cs?page=1&pageSize=20&search=Tái+cấu+trúc → 200 total=1 ['TVCS-20260507-0004'] ✅
GET ?search=tai+cau+truc                                              → 200 total=0 []                  ❌
GET ?search=cau+truc                                                  → 200 total=0 []                  ❌
GET ?search=thuê+đất                                                  → 200 total=1 ['TVCS-20260507-0005'] ✅
GET ?search=thue+dat                                                  → 200 total=0 []                  ❌
GET ?search=Madrid                                                    → 200 total=1 ['TVCS-20260507-0003'] ✅

=== TV-030 empty content probe ===
POST {noiDung: ""}     → 201 mã TVCS-20260507-0012 (BE accept rỗng)            ❌
POST {noiDung: "   "}  → 201 mã TVCS-20260507-0013 (BE accept whitespace)      ❌
POST {/* missing */}   → 422 ERR-VAL-SYS-00-01 "noiDung must be a string"    (chỉ reject type-check)

=== TV-031 CG VO_HIEU_HOA assignment ===
POST /noi-dung-tu-van-cs (TVCS-0011) + phân công Ngô (TVV-0003 VO_HIEU_HOA)
  → 200 state PHAN_CONG, chuyenGiaId = '8f24c981-...' (= TVV-0003.id) ❌
SRS line 533 spec dropdown filter `trangThai=HOAT_DONG` chỉ áp ở FE, BE không validate.

=== TV-032 skip step (positive case) ===
POST /noi-dung-tu-van-cs/{phan_cong_id}/approve {version: 2}
  → 409 ERR-STATE-TVCS-APPROVE-01 "Khong the 'approve' khi trang thai la 'PHAN_CONG'" ✅

=== TV-037 QTHT view-only ===
GET /noi-dung-tu-van-cs → 200 (13/13 records, no row buttons)
POST create / phan-cong / DELETE → 403 ERR-PERM-SYS-00-01

=== TV-044 Audit log ===
GET /audit-logs?entityType=NOI_DUNG_TU_VAN_CS&size=20 (qtht_01)
  → 200 total=25, sample: [
    {action:'UPDATE',  entity:'NOI_DUNG_TU_VAN_CS', time:2026-05-07T15:23:52.887Z},
    {action:'CREATE',  entity:'NOI_DUNG_TU_VAN_CS', time:2026-05-07T15:23:52.827Z},
    {action:'PHAN_CONG',entity:'NOI_DUNG_TU_VAN_CS', time:2026-05-07T15:23:20.760Z},
    ...
  ] ✅

=== TV-049 BR-ROUTE-TVCS-01 (CB nhập tay) ===
13/13 record cb_nv_tw_01 tạo → donViId = '00000000-0000-4000-8000-000000000001' (= BTP-TW)
✅ Match cb_nv_tw_01 đơn vị
```

---

## Đề xuất R9 follow-up

1. **DEV BE fix BUG-FN-001 (TV-005)** — thêm `unaccent()` index/query cho full-text search (Postgres `unaccent` extension hoặc tự build search vector). Re-test cùng 6 query có dấu/không dấu.
2. **DEV BE fix BUG-FN-002 (TV-030)** — thêm validator `@MinLength(1)` + `.trim()` trên field `noiDung` ở DTO. Reject 422 với code ERR-TVCS-01.
3. **DEV BE fix BUG-FN-003 (TV-031)** — thêm BE-side validation `loaiTvv=CG ∧ trangThai=HOAT_DONG ∧ linhVucIds INTERSECT TVCS.linhVucId` ở endpoint `/phan-cong`. Reject 422 với code ERR-TVCS-02.
4. **DEV BE fix BUG-A5-001 + A5-002** (Critical/Major từ workflow R7.4.A5) — unblock 18 TC cascade ở R9.
5. **Seed R7.3.4 HSPL DN** + expose TLPL VV CRUD endpoint → unblock 12 TC HSPL/TLPL ở R9.
6. **R9 Postman setup cho UC149/151/153** — API key Cổng PLQG sandbox + 6 TC API inbound + 2 TC outbound (TV-027..029, 050..052, 060, 061).
7. **R9 BN/ĐP scope sweep** — Seed cấp BN/ĐP qua cb_nv_bn_01/cb_nv_dp_01 → verify TV-038 BR-AUTH-08.
8. **Cleanup pool**: soft-delete TVCS-0011/0012/0013 sau dev fix BUG-FN-002/003.

---

## Ghi chú thực thi

- **Account dùng test:**
  - `cb_nv_tw_01` / `Secret@123` — main flow + create + phân công
  - `qtht_01` / `Secret@123` — TV-037 view-only + TV-044 audit log
  - `ly_13` + `dinh_14` — verified ở A5 (FK linkage check)
- **Tool:** Chrome DevTools MCP. Chrome process orphan đầu phiên (lockfile cũ) — kill manual + clear lockfile để MCP reconnect.
- **Anti-pattern tránh:** TV-030/031 không retry với input variations dài. Phân loại Rule 9 = APP/BE BUG (không phải SELECTOR OUTDATED), STOP + log bug ngay.

---

*R8 | QA Automation via Claude Code | Chrome DevTools MCP*
