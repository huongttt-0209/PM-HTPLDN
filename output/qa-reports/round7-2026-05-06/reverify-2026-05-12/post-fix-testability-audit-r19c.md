# Post-Fix Testability Audit — R19/R19c (2026-05-12)

**Phạm vi:** 7 module có bug đã re-verify ở R19 (cross-module 2026-05-12 14:30→17:50) + R19c (TVCS-R16-001 CRUD + VV LICHSU/TVV-PERM, 2026-05-12 18:42→22:00).

**Nguồn:**
- Bug status: 7 file `bug-report-*.md` trong `output/qa-reports/round7-2026-05-06/bug-reports/<module>/`.
- TC status: 7 file `functional-test-report-*.md` snapshot LATEST tương ứng.
- Todo: 7 file `tasks/todo-<module>.md`.

**Quy tắc taxonomy blocker** (xem [`.agents/skills/qa-bugfix-reverify-audit/SKILL.md`](../../../../.agents/skills/qa-bugfix-reverify-audit/SKILL.md)): thiếu seed/state/account/file/email/dev fix/BA spec/env/upstream/backdate/rate-limit/data drift/API undeployed/DBA/mock/evidence/lý do khác.

---

## Master Summary — 7 module

| Module / task | Bug Open | Bug Closed | Bug re-verify R19/R19c | TC/path unblock | TC/path vẫn block | Next action ngắn |
|---|---:|---:|---|---|---|---|
| **TVCS** (R7.7.5) | 1 (R16-005) | 8 | R16-001 ✅R19c · R16-004/008/009 ✅R19 · R16-005 ⚠️ partial | 0 TC mới (R16-001 fix sửa lỗi BE, ko unblock TC functional list — TC TVCS-TLPL không nằm trong 61 TC plan) | TC liên quan button [Công khai]/[Hủy công khai] (5 TC TVCS-DA_DUYET) | Dev FE add button [Công khai] (BR-PUBLIC-01..03) — sau đó retest 5 TC |
| **VV functional** (R7.7.3) | 2 (LICHSU-01 · TVV-PERM-GAP) | 10 | 9 Closed R7-R12 + LICHSU-01 R19c walk YCBS confirm Open · TVV-PERM-GAP R19c partial 2/3 | 11 TC unblock từ phân công cá nhân CG (POOL-CG fix) + TVV detail (TVV-DETAIL-403 fix) | LICHSU 4/18 enum thiếu (1 TC C8-3) · 1 TC `/trinh-phe-duyet` 403 (VV-017) · 32 TC còn (24 chưa chạy + 8 defer DN VNeID/mTLS) | Dev BE thêm perm `trinh-phe-duyet_vu_viec` + log 4 enum LICHSU còn thiếu |
| **VV workflow** (R7.4.A3) | 1 (PC-WRN-01 Minor) | 6 | 6 Closed R7-R13. PC-WRN-01 R19 ❌ confirm Open | 12/12 transition đã PASS R13 (workflow đóng) | 0 — workflow đã đóng. Button [Tìm thủ công] missing UI Minor không block transition | Dev FE add button [Tìm thủ công] vào modal Phân công empty state |
| **DG** (R7.7.9) | 1 (DG-014 Medium) | 14 | DG-010 ✅R19 + DG-013 ✅R19 + 12 Closed R6-R12. DG-014 R19 ❌ confirm Open | 2 TC unblock R19 (TC07 trọng số + TC18 QTHT permission) | 1 TC (TC11/12 modal dropdown raw UUID) + 24 TC chưa chạy P7 functional | Dev FE filter dropdown LV null name + BA confirm UUID `bbbbbbbb-...-0018` |
| **ChiTra** (R7.7.12.2) | 1 (CHITRA-010 Major) | 1 (CHITRA-009) | CHITRA-009 ✅R19 + CHITRA-010 ❌R19 confirm Open + CHITRA-008 🚫 defer | 10/18 TC sub-phase R7.7.12.2 unblock (wording B8 đã đúng spec) | 8 TC deadline tracking 5 ngày LV (BR-CHITRA-BS01) + 5 TC sync DVC (CHITRA-008 defer) | Dev BE persist `ngayYeuCauBoSung = NOW()` khi DKT→YCBS |
| **TVN** (R7.7.11) | 2 (TVN-005 · TVN-008) | 5 | 4 Closed R10-R12. TVN-005 R19 ❌ confirm Open Partial · TVN-008 🚫 defer | 31/35 PASS đã verify trước R19. R19 không unblock thêm | 1 TC (TVN-039 audit-log filter Module thiếu "Tư vấn") + 5 TC defer external (TVN-020 Kho QA empty + 4 TC Cổng PLQG) | Dev FE+BE thêm enum `TU_VAN` vào dropdown Module audit-log |
| **HDTV** (R7.7.14) | 3 (HDTV-034 · 037 · 038) | 12 | 9 Closed R3-R6 (018/020/021/026/029/030/031/033/035/036). HDTV-034 R19 ❌ confirm Open · 037/038 mới R19 | 24/26 TC PASS đã verify trước R19. R19 không unblock thêm | 2 TC HDTV-028 (i18n raw enum + pagination "mặt hàng") + 1 TC HDTV-024 (route standalone) + 14 TC defer (v2.1 out-of-scope) | Dev FE: add i18n enum `DANG_THUC_HIEN`→"Đang thực hiện" + đổi "mặt hàng"→"mục"/"kết quả" + add route guard `/hop-dong-tv/danh-sach` · BA chốt giữ/xoá route |

**Tổng:** 11 bug Open · 47 bug Closed sau R19/R19c · ~143 TC chạy được (đã chạy trước R19) + 25 TC mới unblock từ R19/R19c · ~58 TC vẫn block (chia 6 nhóm: dev fix bug / BA confirm / DVC sandbox / mTLS PLQG / DN VNeID Tier 2 / out-of-scope v2.1).

---

## 1. TVCS — Tư vấn chuyên sâu (R7.7.5)

**File nguồn:** [`bug-report-r7-7-5-tvcs-r16.md`](../bug-reports/tu-van-chuyen-sau/bug-report-r7-7-5-tvcs-r16.md) · [`functional-test-report-r7-7-5-tvcs.md`](../../functional/tu-van-chuyen-sau/functional-test-report-r7-7-5-tvcs.md) (R20 snapshot) · [`todo-tvcs.md`](../../../../../tasks/todo-tvcs.md)

### Bug Re-verify R19/R19c

| Bug ID | Trạng thái trước | Kết quả re-test | Evidence | Verdict |
|---|---|---|---|---|
| BUG-BE-TVCS-R16-001 | Open Major (5 path 404, R16) | R19c UI thuần 4-step CRUD UI (Read/Update/Delete/Create) `cb_nv_tw_06` TVCS-20260507-0013. Mỗi step reload-verify-persist. | [image r19c-step1..step4](../bug-reports/tu-van-chuyen-sau/image/) | ✅ **Closed-verified R19c** |
| BUG-FE-TVCS-R16-004 | Open Medium (NHT thấy menu TVCS, R16) | R19 `nht_tc001_btp_tw` isolatedContext: sidebar 5 menu (no TVCS) + navigate `/tv-chuyen-sau/danh-sach` → bounced `/dao-tao/chuong-trinh/danh-sach`. Route guard active. | [reverify-2026-05-12-r16-004-nht-no-tvcs-bounced.png](../bug-reports/tu-van-chuyen-sau/image/reverify-2026-05-12-r16-004-nht-no-tvcs-bounced.png) | ✅ **Closed-verified R19** |
| BUG-BE-TVCS-R17-008 | Open Major (NHT blanket-deny `/doanh-nghieps`) | R19 NHT GET DN-003 (có VV phân công) → 200 OK. GET DN-001/002/004/005 → 403 ERR-AUTH-DN-00-01. Row-level filter đúng FR-X.1-04 + BR-AUTH-10. | API probe blob | ✅ **Closed-verified R19** |
| BUG-FEBE-TVCS-R20-009 | Open Major (cross-link TVCS↔VV gap) | R19 form `/tv-chuyen-sau/tao-moi` dropdown "Vụ việc liên kết" có filter `?doanhNghiepId` narrow DN-HNI-0015 total=2 OK | [reverify-2026-05-12-r20-009](../bug-reports/tu-van-chuyen-sau/image/reverify-2026-05-12-r20-009-vv-link-dropdown-narrow.png) | ✅ **Closed-verified R19** |
| BUG-FE-TVCS-R16-005 | Open Major (panel + button missing) | R19 panel 5/5 v3.5 field PASS (`congKhai`/`thoiGianDangTai`/`moTaCongKhai`/`anhDaiDien`/`fileDinhKem`). **Button [Công khai]/[Hủy công khai] vẫn thiếu** (`congKhai|publish` grep 0 hit). | [reverify-2026-05-12-r16-005-tlpl-congkhai-panels.png](../bug-reports/tu-van-chuyen-sau/image/reverify-2026-05-12-r16-005-tlpl-congkhai-panels.png) | ⚠️ **Partial — giữ Open** |

### Bug Summary

| Tổng | Open | Partial | Closed | Closed-verified R19/R19c | New bug | Nguồn |
|---:|---:|---:|---:|---:|---:|---|
| 9 | 1 (R16-005) | 1 (R16-005 panel ✅ button ❌) | 8 | 4 (001/004/008/009) | 0 | Bug Summary Table `bug-report-r7-7-5-tvcs-r16.md` |

### TC/Path Bị Ảnh Hưởng

| TC/path | Liên quan bug | Trạng thái sau re-test | Nguyên nhân nếu vẫn block | Phương án xử lý tiếp theo | Owner |
|---|---|---|---|---|---|
| TV-023/024/025/043 (TLPL CRUD link TVCS) | R16-001 | ✅ Có thể chạy (CRUD UI đã verify R19c) | — | Chạy 4 TC theo functional plan R20 — verify cover 4 LV variant | QA |
| TV-039 (NHT no menu TVCS) | R16-004 | ✅ Chạy clean R19 | — | Đã verify, đóng TC | QA |
| TV-053 happy (NHT GET DN có VV) | R17-008 | ✅ Chạy clean R19 | — | Đã verify, đóng TC | QA |
| TV-041 (TVCS↔VV cross-link) | R20-009 | ✅ Chạy R19 (mặc dù bug functional report mark ⚠️ — dev claim fix R19 PASS) | — | Đối chiếu functional report ⚠️ với R19 verify — quyết flip ✅ | QA |
| TV-045/047 (Công khai TVCS DA_DUYET) | R16-005 | 🚫 Vẫn block | Dev FE chưa add button [Công khai]/[Hủy công khai] | Dev FE add button + retest 2 TC | Dev FE |

### Testability Sweep Sau Dev Fix

| TC/path | Trạng thái hiện tại | Chạy được? | Điều kiện cần | Loại blocker | Action trước khi chạy | Owner |
|---|---|---|---|---|---|---|
| TV-023/024/025/043 (TLPL CRUD) | Mới unblock R19c | ✅ Chạy ngay | TVCS state DANG_TU_VAN (✓ 6 pool) | — | Chạy theo `7.12-tu-van-chuyen-sau.md` TLPL section | QA |
| TV-045/047 (Công khai TVCS) | Vẫn block | ❌ Không | Button [Công khai]/[Hủy công khai] | chờ dev fix bug (R16-005 partial) | Dev FE wire button + workflow API POST `/cong-khai`/`/huy-cong-khai` | Dev FE |
| 5/61 TC R20 còn chưa chạy được | Trong plan TVCS | ⚠️ Một phần | Tùy TC — đa số DA_DUYET dependent | dependency upstream R7.4.A5 DA_DUYET | Chạy sau R16-005 fix | QA |

### Setup Cần Chuẩn Bị

Không có setup QA-side cần chuẩn bị — chỉ cần Dev FE fix R16-005 button. Sau khi fix, QA chạy 5 TC `cong_khai` flow trực tiếp UI.

### Spec / BA Confirmation Check

Không có case cần BA confirm.

### Phương Án Xử Lý Tiếp Theo

| Nhóm | Áp dụng cho | Việc cần làm | Điều kiện xong | Ưu tiên | Owner |
|---|---|---|---|---|---|
| Dev FE button | R16-005 | Add button [Công khai] khi `congKhai=false` POST `/cong-khai`; button [Hủy công khai] khi `congKhai=true` POST `/huy-cong-khai` | TVCS-20260509-0002 DA_DUYET click → toggle state thành công | P1 | Dev FE |
| QA chạy follow-up | TV-023/024/025/043 (TLPL) | Chạy 4 TC TLPL CRUD theo plan R20+ | 4 TC PASS clean | P2 | QA |

### Follow-up TC Cần Chạy

| TC/path | Lý do chạy bây giờ | Setup cần | Kết quả kỳ vọng |
|---|---|---|---|
| TV-023 (Create TLPL link TVCS) | R16-001 ✅ CRUD endpoint deploy | TVCS-20260507-0013 DANG_TU_VAN | POST `/tu-lieu-phap-luats` 201 + persist sau reload |
| TV-024 (Read/List TLPL) | R16-001 ✅ | TVCS-20260507-0013 có ≥1 TLPL | GET trả list TLPL filter `?tuVanChuyenSauId` |
| TV-025 (Update/Delete TLPL) | R16-001 ✅ | TVCS-20260507-0013 có ≥1 TLPL | PATCH/DELETE 200/204 persist |
| TV-043 (Công khai TLPL nội bộ) | R16-001 ✅ + R16-005 partial (BE đã có endpoint nhưng FE chưa wire) | TLPL NHAP | POST `/tu-lieu-phap-luats/{id}/cong-khai` |

### Tóm Tắt Cuối — TVCS

- Re-verify R19/R19c: **4 bug Closed-verified · 1 partial (R16-005 panel ✅ button ❌).**
- TC/path chạy được ngay: **4 TC TLPL CRUD (TV-023/024/025/043).**
- TC/path chạy được sau setup QA-side: không có.
- TC/path vẫn block bởi bên ngoài: **2 TC TVCS-Cong-khai (TV-045/047) — chờ Dev FE add button.**
- Cần dev BE seed dữ liệu trong hệ thống: không có.
- Việc cần làm tiếp: (1) Dev FE add button [Công khai]/[Hủy công khai] R16-005 · (2) QA chạy 4 TC TLPL CRUD · (3) Sau khi R16-005 fix → QA chạy TV-045/047.
- Sau khi xong: dùng `qa-module-status-audit` để kết luận TVCS module.

---

## 2. VV functional — Vụ việc HTPL (R7.7.3)

**File nguồn:** [`bug-report-r7-7-3-functional-vu-viec.md`](../bug-reports/vu-viec/bug-report-r7-7-3-functional-vu-viec.md) · [`functional-test-report-r7-7-3-vu-viec.md`](../../functional/vu-viec/functional-test-report-r7-7-3-vu-viec.md) (R18-P2 LATEST + R19c add) · [`todo-vu-viec.md`](../../../../../tasks/todo-vu-viec.md)

### Bug Re-verify R19/R19c

| Bug ID | Trạng thái trước | Kết quả re-test | Evidence | Verdict |
|---|---|---|---|---|
| BUG-VV-FN-POOL-CG-MISSING-01 | Open Minor R18 | Dev fix R19: dropdown CÁ NHÂN nay có 3 loại (TVV/CG/NHT) match SRS FR-V.I-09 Acceptance | — | ✅ **Closed** |
| BUG-VV-FN-TVV-DETAIL-403-01 | Open Major R18 | Dev fix R19: TVV login → mở VV detail được phân công → 200 không 403. UC60 + BR-AUTH-08 đúng | — | ✅ **Closed** |
| BUG-VV-FN-TVV-PERMISSION-GAP-01 | Open Major R18 (3 endpoint 403) | R19c probe API 5 endpoint sau dev BE thêm 6 perm: `/cap-nhat-ket-qua` 422 (perm OK) · `/hoan-thanh` 422 (perm OK) · `/nhan-pc` 422 (perm OK) · `/tu-choi-pc` 422 (perm OK) · **`/trinh-phe-duyet` 403 ERR-PERM-SYS-00-01** | API probe blob | ⚠️ **Partial 4/5 — giữ Open** |
| BUG-VV-FN-LICHSU-01 | Open Major R18 (12/18 enum) | R19c walk branch YCBS `cb_nv_tw_03` → KIEM_TRA → YEU_CAU_BO_SUNG. State chuyển OK, NHƯNG UI Tab Dòng thời gian chỉ 1 entry KIEM_TRA, API `/lich-su` cũng 1 entry. MISS entry YEU_CAU_BO_SUNG. Pool 17 enum (R19 +1 `MO_LAI`). Còn miss 4 (`TIEP_NHAN`/`TU_CHOI`/`TU_CHOI_DUYET`/`YEU_CAU_BO_SUNG`) | [r19c-lichsu-01-ycbs-missing-timeline-entry-2026-05-12.png](../bug-reports/vu-viec/image/r19c-lichsu-01-ycbs-missing-timeline-entry-2026-05-12.png) | ⚠️ **Partial — giữ Major P1** (rollback reclass R19b) |

### Bug Summary

| Tổng | Open | Partial | Closed | Closed-verified R19/R19c | New bug | Nguồn |
|---:|---:|---:|---:|---:|---:|---|
| 12 | 2 (LICHSU-01 · TVV-PERM) | 2 | 10 | 2 (POOL-CG + TVV-DETAIL) | 0 | Bug Summary Table `bug-report-r7-7-3-functional-vu-viec.md` |

### TC/Path Bị Ảnh Hưởng

| TC/path | Liên quan bug | Trạng thái sau re-test | Nguyên nhân block | Phương án xử lý | Owner |
|---|---|---|---|---|---|
| VV-013 (Phân công CÁ NHÂN với loại CG) | POOL-CG-MISSING-01 | ✅ Unblock R19 | — | Chạy theo `7.5-vu-viec-htpl.md` VV-013 | QA |
| VV-014/015/017/033 (TVV detail + actions) | TVV-DETAIL-403-01 | ✅ Unblock R19 | — | Chạy 4 TC TVV detail flow | QA |
| VV-015 cập nhật KQ + VV-016 hoàn thành | TVV-PERMISSION-GAP-01 | ✅ Chạy được R19c (perm OK) | — | Chạy 2 TC qua UI thao tác — không probe API direct | QA |
| VV-017 trình phê duyệt | TVV-PERMISSION-GAP-01 | 🚫 Vẫn block | BE thiếu perm `trinh-phe-duyet_vu_viec` cho TVV | Dev BE thêm perm → retest UI | Dev BE |
| C8-3 (LICHSU 18 enum) | LICHSU-01 | 🚫 Vẫn block | BE chưa log 4 enum thiếu (TIEP_NHAN/TU_CHOI/TU_CHOI_DUYET/YEU_CAU_BO_SUNG) | Dev BE bổ sung audit log enum | Dev BE |
| 32/72 TC còn chưa chạy | Chia 3 nhóm | ⚠️ Mixed | (a) DN VNeID Tier 2 chưa setup (8 TC privacy/E2E) · (b) mTLS PLQG cert (6 TC integration) · (c) 18 TC thuộc Cluster 1-8 cần seed thêm | Dep tooling/integration | Infra + Dev BE |

### Testability Sweep Sau Dev Fix

| TC/path | Trạng thái | Chạy được? | Điều kiện cần | Loại blocker | Action | Owner |
|---|---|---|---|---|---|---|
| VV-013 (Phân công CG) | Mới unblock R19 | ✅ Chạy ngay | ≥1 CG HOAT_DONG cover ≥2 LV (✓ huongcg R12) | — | Chạy theo VV-013 plan | QA |
| VV-014/015/017/033 (TVV detail) | Mới unblock R19 | ✅ Chạy ngay (trừ VV-017) | TVV account active + VV phân công TVV | — | Chạy 3/4 TC trực tiếp UI | QA |
| VV-017 (trinh-phe-duyet) | Vẫn block | ❌ Không | Perm BE | chờ dev fix bug | Dev BE add perm `trinh-phe-duyet_vu_viec` | Dev BE |
| C8-3 LICHSU 18 enum | Vẫn block (R19c partial) | ❌ Không | BE log 4 enum thiếu | chờ dev fix bug | Dev BE expand state machine audit log | Dev BE |
| 8 TC privacy/E2E DN | Defer | ❌ Không | DN VNeID Tier 2 sandbox | thiếu env/tooling + thiếu account/role | Infra setup VNeID Tier 2 + seed DN test | Infra + Dev |
| 6 TC integration | Defer | ❌ Không | mTLS cert PLQG | chờ env/tooling | Infra setup mTLS cert sandbox | Infra |
| 18 TC Cluster 1-8 còn | Mixed | ⚠️ Phần lớn | Seed cụ thể per cluster | Mix seed + state setup | Audit từng TC sau khi unblock major | QA |

### Setup Cần Chuẩn Bị (QA-side)

| Nhóm setup | Áp dụng cho | Cần chuẩn bị | Cách tạo/kiểm tra | Ai | Sau khi xong rerun |
|---|---|---|---|---|---|
| TVV active password | VV-015/016 (cập nhật KQ + hoàn thành) | TVV account login OK | Dùng `tvv_r11_mailfix` (✓ R13 verified) | QA | VV-015/016 |
| ≥1 VV YEU_CAU_BO_SUNG có audit log | C8-3 LICHSU verify | VV state YCBS, retest sau dev fix | Walk DA_PHAN_CONG → DA_TIEP_NHAN → KIEM_TRA → YCBS | QA sau dev BE fix | C8-3 |

### Spec / BA Confirmation Check

| TC / vấn đề | Câu hỏi | SRS local check | NotebookLM | Kết luận | Verdict |
|---|---|---|---|---|---|
| LICHSU enum spec 18 | Spec yêu cầu log đủ 18 enum? | `srs-fr-05-vu-viec.md` LICH_SU_VU_VIEC enum + BR-AUDIT-VV-01 | — | SRS rõ 18 enum, BE đang thiếu 4 | Không phải BA-blocked. Dev BE fix |

### Phương Án Xử Lý Tiếp Theo

| Nhóm | Áp dụng | Việc cần làm | Điều kiện xong | Ưu tiên | Owner |
|---|---|---|---|---|---|
| Dev BE perm | TVV-PERMISSION-GAP-01 | Add perm `trinh-phe-duyet_vu_viec` cho role TVV | TVV `/trinh-phe-duyet` → 201/200 không 403 | P1 | Dev BE |
| Dev BE audit log | LICHSU-01 | Log 4 enum còn thiếu khi state machine advance đúng transition | Pool 18/18 enum cover | P3 | Dev BE |
| Infra | 8 TC privacy + 6 TC integration | Setup VNeID Tier 2 + mTLS PLQG sandbox | Endpoint reachable + cert install | P2 (external) | Infra |
| QA chạy follow-up | 11 TC unblock R19 | Chạy VV-013/014/015/016/033 | TC PASS clean | P1 | QA |

### Follow-up TC Cần Chạy

| TC | Lý do | Setup | Kết quả kỳ vọng |
|---|---|---|---|
| VV-013 (Phân công CG cá nhân) | POOL-CG fix R19 | ≥1 CG HOAT_DONG cover ≥2 LV (✓) | Dropdown CÁ NHÂN có 3 loại + chọn CG → 201 |
| VV-014 (TVV xem VV detail) | TVV-DETAIL-403 fix | TVV account + ≥1 VV phân công TVV | GET `/vu-viec/{id}` 200, render full detail |
| VV-015 (TVV cập nhật KQ) | TVV-PERM 4/5 perm OK R19c | TVV + VV state DANG_XU_LY | Click [Cập nhật KQ] → modal submit → 201 |
| VV-016 (TVV hoàn thành VV) | TVV-PERM perm OK R19c | TVV + VV state DANG_XU_LY có KQ | Click [Hoàn thành] → 201 + state HOAN_THANH |
| VV-033 (TVV nhận/từ chối PC) | TVV-PERM perm OK R19c | TVV + VV state DA_PHAN_CONG | Click [Nhận]/[Từ chối] → 201 |

### Tóm Tắt Cuối — VV functional

- Re-verify R19/R19c: **2 bug Closed-verified (POOL-CG + TVV-DETAIL) · 2 partial (TVV-PERM 4/5 + LICHSU 17/18) — giữ Open.**
- TC/path chạy được ngay: **5 TC (VV-013/014/015/016/033).**
- TC/path chạy được sau setup QA-side: không có (đã có TVV account active).
- TC/path vẫn block bởi bên ngoài: **VV-017 chờ Dev BE perm · C8-3 LICHSU chờ Dev BE audit log · 14 TC defer DN VNeID + mTLS.**
- Cần dev BE seed dữ liệu trong hệ thống: không có (QA tự seed được VV state từ UI workflow).
- Việc cần làm tiếp: (1) Dev BE thêm perm `trinh-phe-duyet_vu_viec` · (2) Dev BE log 4 enum LICHSU thiếu · (3) QA chạy 5 TC unblock.
- Sau khi xong: dùng `qa-module-status-audit` để kết luận VV.

---

## 3. VV workflow — Vụ việc HTPL (R7.4.A3)

**File nguồn:** [`bug-report-flow-vu-viec.md`](../bug-reports/vu-viec/bug-report-flow-vu-viec.md) · [`workflow-test-report-r7-4-a3-vu-viec.md`](../../workflow/vu-viec/workflow-test-report-r7-4-a3-vu-viec.md)

### Bug Re-verify R19

| Bug ID | Trạng thái trước | Kết quả re-test | Verdict |
|---|---|---|---|
| BUG-VV-PC-WRN-01 | Open Minor (R18 dev fix text empty state ✅ nhưng button [Tìm thủ công] vẫn thiếu) | R19 `cb_nv_tw_03` mở VV-BTP-TW-20260511-001 LV Thuế → modal Phân công → combobox CÁ NHÂN focus → text mismatch "XXKHONGMATCH99" → empty state khớp WRN-PC-01 line 768 ✅, **button [Tìm thủ công] vẫn 0 hit** | ❌ **Still Open Minor P2** |

### Bug Summary

| Tổng | Open | Partial | Closed | Closed-verified R19 | New bug | Nguồn |
|---:|---:|---:|---:|---:|---:|---|
| 7 | 1 (PC-WRN-01) | 0 | 6 | 0 (chỉ retest PC-WRN-01 → vẫn Open) | 0 | Bug Summary Table `bug-report-flow-vu-viec.md` |

### TC/Path Bị Ảnh Hưởng

| TC/path | Liên quan bug | Trạng thái | Nguyên nhân | Phương án | Owner |
|---|---|---|---|---|---|
| C3-6 (Phân công empty state override) | PC-WRN-01 | 🚫 Vẫn block | FE thiếu button [Tìm thủ công] | Dev FE add button | Dev FE |
| 12/12 transition lifecycle | 6 bug đã Closed R13 | ✅ PASS R13 | — | Đã đóng workflow | QA |

### Testability Sweep

| TC/path | Chạy được? | Loại blocker | Action | Owner |
|---|---|---|---|---|
| 12 transition VV (full lifecycle) | ✅ Đã chạy clean R13 | — | Không cần làm gì thêm | — |
| C3-6 override Phân công | ❌ Không | chờ dev fix bug | Dev FE add button [Tìm thủ công] vào modal empty state per FR-V.I-09 Acceptance line 778 | Dev FE |

### Setup Cần Chuẩn Bị

Không có setup QA-side.

### Spec/BA Check

Không có case cần BA confirm — spec `srs-fr-05-vu-viec.md:778` đã rõ "cho phép tìm thủ công".

### Phương Án Xử Lý Tiếp Theo

| Nhóm | Áp dụng | Việc cần làm | Điều kiện xong | Ưu tiên | Owner |
|---|---|---|---|---|---|
| Dev FE button | PC-WRN-01 | Add button [Tìm thủ công] vào modal empty state | Mở modal → button hiện + click mở mode tìm override LV | P2 | Dev FE |

### Follow-up TC

| TC | Lý do | Setup | Kết quả kỳ vọng |
|---|---|---|---|
| C3-6 (Phân công override search) | Sau FE add button | VV state DA_TIEP_NHAN không có người match LV | Click [Tìm thủ công] → modal override mode mở |

### Tóm Tắt Cuối — VV workflow

- Re-verify R19: **0 bug mới closed · 1 bug Open Minor giữ nguyên (PC-WRN-01).**
- TC/path chạy được ngay: không có TC mới (12/12 transition đã đóng R13).
- TC vẫn block: **C3-6 chờ Dev FE add button [Tìm thủ công].**
- Cần dev BE seed: không có.
- Việc cần làm tiếp: (1) Dev FE add button [Tìm thủ công] vào modal Phân công empty state.

---

## 4. DG — Đánh giá Hiệu quả HTPL (R7.7.9)

**File nguồn:** [`bug-report-flow-danhgia.md`](../bug-reports/danh-gia/bug-report-flow-danhgia.md) · [`functional-test-report-r7-7-9-danh-gia.md`](../../functional/danh-gia/functional-test-report-r7-7-9-danh-gia.md) (R11 LATEST) · [`todo-danh-gia-hq.md`](../../../../../tasks/todo-danh-gia-hq.md)

### Bug Re-verify R19

| Bug ID | Trạng thái trước | Kết quả re-test | Evidence | Verdict |
|---|---|---|---|---|
| BUG-FUNC-DG-010 | Open Major (modal Thêm tiêu chí force `trongSo=100`) | R19 16:30 `cb_nv_tw_06` đợt DG-20260510-0001 LAP_KE_HOACH → [+ Thêm tiêu chí] → Trọng số=30, Điểm tối đa=10 → table row 2 spinbutton Trọng số=**30** không force 100. Tổng=90. FE honor đúng giá trị user nhập. | [reverify-2026-05-12-dg010-trongso-30-pass.png](../bug-reports/danh-gia/image/reverify-2026-05-12-dg010-trongso-30-pass.png) | ✅ **Closed-verified R19** |
| BUG-FUNC-DG-013 | Open Major (QTHT có button edit Tab Tiêu chí + delete + Hủy đợt) | R19 15:45 `qtht_01` DG-20260510-0001 LAP_KE_HOACH: Tab Tiêu chí spinbutton valuemin=0 read-only + 0 button (Hủy đợt/Thêm tiêu chí/delete). Tab Phân công: 0 button (Thêm/delete). SCR-DG-VIII đúng R-only. | [reverify-2026-05-12-dg013-qtht-no-buttons.png](../bug-reports/danh-gia/image/reverify-2026-05-12-dg013-qtht-no-buttons.png) | ✅ **Closed-verified R19** |
| BUG-FUNC-DG-014 | Open Medium (dropdown LV render raw UUID) | R19 15:50 `cb_nv_tw_06` modal Thêm người đánh giá → dropdown LV scroll virtual-list → 13 options, vẫn 2 raw UUID `e5d17437-...` + `bbbbbbbb-0000-4000-8000-000000000018`. | [r11-linhvuc-dropdown-raw-uuid-2026-05-11.png](../bug-reports/danh-gia/image/r11-linhvuc-dropdown-raw-uuid-2026-05-11.png) | ❌ **Reproduced — giữ Open Medium** |

### Bug Summary

| Tổng | Open | Partial | Closed | Closed-verified R19 | New bug | Nguồn |
|---:|---:|---:|---:|---:|---:|---|
| 15 | 1 (DG-014) | 0 | 14 | 2 (DG-010 + DG-013) | 0 | Bug Summary Table `bug-report-flow-danhgia.md` |

### TC/Path Bị Ảnh Hưởng

| TC/path | Liên quan bug | Trạng thái sau re-test | Nguyên nhân block | Phương án | Owner |
|---|---|---|---|---|---|
| TC07 (FR-VI-02 Thêm tiêu chí trọng số tự chọn) | DG-010 | ✅ Unblock R19 | — | Chạy theo plan | QA |
| TC18 (FR-VI-03 × QTHT permission R-only) | DG-013 | ✅ Unblock R19 | — | Chạy theo plan | QA |
| TC11/TC12 (modal Phân công dropdown LV) | DG-014 | 🚫 Vẫn block | FE chưa filter LV null name + BA chưa quyết UUID `bbbbbbbb-...-0018` | Dev FE filter + BA confirm | Dev FE + BA |
| 24/46 TC còn chưa chạy P7 | Mix | ⚠️ Mixed | Đa số cần state advance + seed | dependency upstream + seed gap | Audit từng TC | QA |

### Testability Sweep

| TC/path | Chạy được? | Setup cần | Loại blocker | Action | Owner |
|---|---|---|---|---|---|
| TC07 (trọng số 30 PASS) | ✅ Chạy ngay | DG-20260510-0001 LAP_KE_HOACH (✓ pool R7.4.D1) | — | Chạy theo TC07 plan | QA |
| TC18 (QTHT R-only verify) | ✅ Chạy ngay | DG-20260510-0001 + `qtht_01` | — | Chạy theo TC18 plan | QA |
| TC11/12 (modal dropdown filter) | ❌ Vẫn block | FE filter + BA UUID | chờ dev fix bug + chờ BA confirm spec | Dev FE filter LV null name → retest sau BA confirm UUID giữ/xoá | Dev FE + BA |
| TC14 + TC17 + B7..B11 (workflow advance) | ❌ Vẫn block | Dev fix BUG-DG-008 (PUT `/ket-quas` persist) — đã Closed R12 nhưng todo nói cần fix | data drift/cleanup | Re-verify DG-008 closed → flip todo flag | QA |
| 24 TC còn chưa chạy | Mixed | Tuỳ TC | Mix seed + state | Audit per-TC | QA |

### Setup Cần Chuẩn Bị

| Nhóm | TC | Cần chuẩn bị | Cách tạo | Ai | Rerun |
|---|---|---|---|---|---|
| DG đợt LAP_KE_HOACH | TC07/TC18 | DG-20260510-0001 còn LAP_KE_HOACH | (✓ R7.4.D1 PASS đã seed) | QA | TC07/TC18 |
| DG đợt HOAN_THANH | FR-VI-10 read-only test | ≥1 đợt HOAN_THANH (BUG-DG-008 closed) | Walk full lifecycle DG advance | QA | R7.4.D2b |

### Spec / BA Confirmation Check

| TC / vấn đề | Câu hỏi | SRS check | NotebookLM | Kết luận | Verdict |
|---|---|---|---|---|---|
| DG-014 LV UUID `bbbbbbbb-...-0018` | BA giữ LV không tên hay xoá? Nếu giữ thì set tên Vietnamese? | `srs-fr-08-danh-gia.md` FR-VI-03 Inputs row 4: yêu cầu "Lĩnh vực" nhưng không quy định LV ẩn/loại | Cần query | Không trong SRS rõ — cần BA quyết | ⚠️ **BA-blocked confirm** |

### Phương Án Xử Lý Tiếp Theo

| Nhóm | Áp dụng | Việc cần làm | Điều kiện xong | Ưu tiên | Owner |
|---|---|---|---|---|---|
| Dev FE filter | DG-014 | Filter dropdown LV chỉ render record có `tenDanhMuc` không null | Dropdown 11 options (loại 2 UUID raw) | P3 | Dev FE |
| BA confirm | DG-014 UUID | Quyết giữ LV `bbbbbbbb-...-0018` (set tên Vietnamese) hay xoá | BA chốt 1 trong 2 hướng | P3 | BA |
| QA follow-up | TC07/TC18 | Chạy 2 TC unblock R19 | PASS clean | P1 | QA |

### Follow-up TC

| TC | Lý do | Setup | Kết quả kỳ vọng |
|---|---|---|---|
| TC07 (FR-VI-02 trọng số) | DG-010 fix | DG-20260510-0001 LAP_KE_HOACH | Thêm tiêu chí trọng số 30 → table row spinbutton=30 |
| TC18 (FR-VI-03 QTHT R-only) | DG-013 fix | DG-20260510-0001 + `qtht_01` | QTHT vào DG detail: 0 button edit/delete |

### Tóm Tắt Cuối — DG

- Re-verify R19: **2 bug Closed-verified (DG-010 + DG-013) · 1 reproduced (DG-014 giữ Open).**
- TC/path chạy được ngay: **2 TC (TC07 + TC18).**
- TC/path vẫn block: **TC11/12 chờ Dev FE filter + BA confirm UUID.**
- Cần dev BE seed: không có.
- Việc cần làm tiếp: (1) Dev FE filter dropdown LV null name · (2) BA confirm UUID `bbbbbbbb-...-0018` · (3) QA chạy TC07 + TC18.

---

## 5. ChiTra — Chi trả (R7.7.12.2)

**File nguồn:** [`bug-report-r7-7-12-2-fr14-bo-sung.md`](../bug-reports/chi-tra/bug-report-r7-7-12-2-fr14-bo-sung.md) · [`functional-test-report-r7-7-12-2-fr14-bo-sung.md`](../../functional/chi-tra/functional-test-report-r7-7-12-2-fr14-bo-sung.md) (R2 LATEST) · [`todo-chi-tra.md`](../../../../../tasks/todo-chi-tra.md)

### Bug Re-verify R19

| Bug ID | Trạng thái trước | Kết quả re-test | Evidence | Verdict |
|---|---|---|---|---|
| BUG-CHITRA-009 | Open Minor (wording row 841 mâu thuẫn 8+ chỗ DVC-only) | R19 18:45 grep `srs-fr-06-chi-tra.md` line 841 hiện tại: `"Doanh nghiệp (qua DVC/Cổng PLQG)"` — BA đã xoá `"hoặc CB NV (thủ công)"`. NotebookLM HTPLDN confirm. | Grep SRS local | ✅ **Closed-verified R19** |
| BUG-CHITRA-010 | Open Major (`ngayYeuCauBoSung = null` 6/6 HSCT YCBS) | R19 18:42 `cb_nv_dp_01` AG fetch 6/6 HSCT YCBS (HSCT000004/011/012/013/014/200002). API: `ngayYeuCauBoSung = null` cho cả 6 records. Lichsu có entry "KIEM_TRA→YEU_CAU_BO_SUNG" cho 2 records. BE chưa set `ngay_yeu_cau_bo_sung = NOW()`. Deadline tracking 5 ngày LV vẫn không trigger. | API fetch blob | ❌ **Still Open Major P1** |

### Bug Summary

| Tổng | Open | Defer | Closed | Closed-verified R19 | New bug | Nguồn |
|---:|---:|---:|---:|---:|---:|---|
| 3 | 1 (CHITRA-010) | 1 (CHITRA-008 LGSP sandbox) | 1 (CHITRA-009) | 1 (CHITRA-009) | 0 | Bug Summary Table `bug-report-r7-7-12-2-fr14-bo-sung.md` |

### TC/Path Bị Ảnh Hưởng

| TC/path | Liên quan bug | Trạng thái | Nguyên nhân block | Phương án | Owner |
|---|---|---|---|---|---|
| 10/18 TC sub-phase R7.7.12.2 (wording B8 align) | CHITRA-009 | ✅ Unblock R19 | — | Đã chạy R2 — đóng | QA |
| 8 TC deadline tracking 5 ngày LV | CHITRA-010 | 🚫 Vẫn block | BE chưa persist `ngayYeuCauBoSung` | Dev BE fix BR-CHITRA-BS01 | Dev BE |
| 5 TC sync DVC sandbox | CHITRA-008 | 🚫 Defer external | DVC LGSP gateway endpoint chưa expose | Chờ phase tích hợp API ngoài | Infra + Dev |

### Testability Sweep

| TC/path | Chạy được? | Setup | Loại blocker | Action | Owner |
|---|---|---|---|---|---|
| 10 TC wording B8 align spec | ✅ Đã chạy R2 (đóng) | — | — | — | — |
| 8 TC deadline 5 ngày LV | ❌ Không | HSCT YCBS có `ngayYeuCauBoSung` ≠ null | chờ dev fix bug | Dev BE persist timestamp DKT→YCBS | Dev BE |
| 5 TC sync DVC | ❌ Defer | DVC LGSP sandbox | thiếu env/tooling (integration/API endpoint chưa deploy) | Chờ phase tích hợp external | Infra |

### Setup Cần Chuẩn Bị

| Nhóm | TC | Cần chuẩn bị | Cách tạo | Ai | Rerun |
|---|---|---|---|---|---|
| HSCT YCBS có ngayYeuCauBoSung | 8 TC deadline | ≥6 HSCT state YCBS với `ngayYeuCauBoSung` ≠ null sau dev BE fix | Walk DKT→YCBS UI sau dev fix → verify field | QA sau dev fix | 8 TC deadline |

### Spec/BA Check

Không có case cần BA confirm — spec FR-V.II-03 Bước 5 + BR-CHITRA-BS01 đã rõ.

### Phương Án Xử Lý Tiếp Theo

| Nhóm | Áp dụng | Việc cần làm | Điều kiện xong | Ưu tiên | Owner |
|---|---|---|---|---|---|
| Dev BE persist | CHITRA-010 | Persist `ngay_yeu_cau_bo_sung = NOW()` khi BE chuyển state DKT→YCBS | 6/6 HSCT YCBS có `ngayYeuCauBoSung` ≠ null | P1 | Dev BE |
| External (defer) | CHITRA-008 (5 TC DVC) | Setup LGSP gateway sandbox | Endpoint DVC reachable | P2 (external) | Infra |

### Follow-up TC

| TC | Lý do | Setup | Kết quả kỳ vọng |
|---|---|---|---|
| 8 TC deadline 5 ngày LV | Sau CHITRA-010 fix | HSCT YCBS với `ngayYeuCauBoSung` ≠ null | Deadline counter trigger ERR-CT-BS-03 đúng |

### Tóm Tắt Cuối — ChiTra

- Re-verify R19: **1 bug Closed-verified (CHITRA-009 wording) · 1 reproduced (CHITRA-010 deadline tracking).**
- TC/path chạy được ngay: **10 TC R7.7.12.2 wording B8 đã pass R2.**
- TC/path vẫn block: **8 TC deadline chờ Dev BE persist `ngayYeuCauBoSung` · 5 TC DVC sync defer external.**
- Cần dev BE seed: không có (QA seed được HSCT YCBS từ UI sau dev fix).
- Việc cần làm tiếp: (1) Dev BE persist `ngayYeuCauBoSung = NOW()` khi DKT→YCBS · (2) QA retest 8 TC deadline sau fix.

---

## 6. TVN — Tư vấn nhanh (R7.7.11)

**File nguồn:** [`bug-report-r7-7-11-tvn.md`](../bug-reports/tu-van-nhanh/bug-report-r7-7-11-tvn.md) · [`functional-test-report-r7-7-11-tvn.md`](../../functional/tu-van-nhanh/functional-test-report-r7-7-11-tvn.md) (R15-P2 LATEST) · [`todo-tv-nhanh.md`](../../../../../tasks/todo-tv-nhanh.md)

### Bug Re-verify R19

| Bug ID | Trạng thái trước | Kết quả re-test | Evidence | Verdict |
|---|---|---|---|---|
| BUG-FUNC-TVN-005 | Open Partial (R15 KHO_CAU_HOI 6 action chuẩn ✅, dropdown filter Module thiếu "Tư vấn" ❌) | R19 15:30 `qtht_01` `/quan-tri/audit-log` → dropdown Module 12 option, **không có "Tư vấn"**. CB NV không filter được TVN/KHO_CAU_HOI entries. | [reverify-2026-05-12-tvn005-module-dropdown-no-tuvan.png](../bug-reports/tu-van-nhanh/image/reverify-2026-05-12-tvn005-module-dropdown-no-tuvan.png) | ❌ **Still Open Minor** (giảm xuống Minor R15 KHO_CAU_HOI fix một phần) |
| BUG-FUNC-TVN-008 | Open Minor R15 (WARNING ERR-TVN-01 không surface trong `/cms-create`) | Defer external — chờ phase tích hợp API Cổng PLQG | — | 🚫 **Defer external** |

### Bug Summary

| Tổng | Open | Defer | Closed | Closed-verified R10-R15 | New bug | Nguồn |
|---:|---:|---:|---:|---:|---:|---|
| 8 | 1 (TVN-005 Partial) | 1 (TVN-008 external) | 6 | 0 ở R19 (4 đã closed R10-R15) | 0 | Bug Summary Table `bug-report-r7-7-11-tvn.md` |

### TC/Path Bị Ảnh Hưởng

| TC/path | Liên quan bug | Trạng thái | Nguyên nhân block | Phương án | Owner |
|---|---|---|---|---|---|
| TVN-039 (audit-log filter Module) | TVN-005 | 🚫 Vẫn block | Dropdown Module dropdown audit-log thiếu enum "Tư vấn" | Dev FE + BE thêm enum `TU_VAN` | Dev FE + BE |
| TVN-020 (Kho QA rỗng WARNING) | TVN-008 | 🚫 Defer external | Cổng PLQG CMS proxy `/cms-create` external | Chờ phase tích hợp | Infra |
| 31/35 TC R7.7.11 ✅ PASS R13 + R14 5/5 UI re-audit | — | — | — | Module 89% pass | — |

### Testability Sweep

| TC/path | Chạy được? | Setup | Loại blocker | Action | Owner |
|---|---|---|---|---|---|
| 31 TC core | ✅ Đã pass R13/R14 (đóng) | — | — | — | — |
| TVN-039 audit-log Module filter | ❌ Vẫn block | Enum `TU_VAN` trong dropdown | chờ dev fix bug | Dev FE+BE thêm enum | Dev FE + BE |
| TVN-020 Kho QA rỗng WARNING | ❌ Defer | Cổng PLQG sandbox | thiếu env/tooling external + integration/API undeploy | Chờ external | Infra |
| 5 TC defer Cổng PLQG | ❌ Defer | mTLS PLQG | thiếu env/tooling external | Chờ external | Infra |

### Setup Cần Chuẩn Bị

Không có setup QA-side — tất cả 31 core TC đã pass.

### Spec/BA Check

Không có case cần BA confirm.

### Phương Án Xử Lý Tiếp Theo

| Nhóm | Áp dụng | Việc cần làm | Điều kiện xong | Ưu tiên | Owner |
|---|---|---|---|---|---|
| Dev FE+BE enum | TVN-005 | Thêm enum `TU_VAN` (label "Tư vấn") vào dropdown Module audit-log | Dropdown có option "Tư vấn" + filter trả TVN entries | P3 | Dev FE + BE |
| External | TVN-008 + 5 TC Cổng PLQG | Setup external sandbox | Endpoint reachable | P2 (external) | Infra |

### Follow-up TC

| TC | Lý do | Setup | Kết quả kỳ vọng |
|---|---|---|---|
| TVN-039 (filter Module = Tư vấn) | Sau dev fix enum | QTHT vào audit-log + ≥1 TVN entry | Dropdown có "Tư vấn" + filter trả ≥1 row |

### Tóm Tắt Cuối — TVN

- Re-verify R19: **0 bug closed mới · 1 reproduced (TVN-005 Open Partial).**
- TC/path chạy được ngay: không có (31 core đã pass).
- TC/path vẫn block: **TVN-039 chờ Dev FE+BE enum · 5 TC Cổng PLQG defer external.**
- Cần dev BE seed: không có.
- Việc cần làm tiếp: (1) Dev FE+BE thêm enum `TU_VAN` vào dropdown audit-log · (2) Defer 5 TC Cổng PLQG chờ external sandbox.

---

## 7. HDTV — Hợp đồng tư vấn (R7.7.14)

**File nguồn:** [`bug-report-r7-7-14-hdtv.md`](../bug-reports/hop-dong-tv/bug-report-r7-7-14-hdtv.md) · [`functional-test-report-r7-7-14-hdtv.md`](../../functional/hop-dong-tv/functional-test-report-r7-7-14-hdtv.md) (R6 LATEST) · [`todo-hop-dong-tv.md`](../../../../../tasks/todo-hop-dong-tv.md)

### Bug Re-verify R19

| Bug ID | Trạng thái trước | Kết quả re-test | Evidence | Verdict |
|---|---|---|---|---|
| BUG-HDTV-034 | Open Minor R5 (standalone route render OK trái BA chốt "không menu riêng"; dev-fix-list nâng Major P1 RBAC bypass) | R19 15:55 `cb_nv_tw_06` navigate `/hop-dong-tv/danh-sach` → render 9 records, no `/403`, no route guard. FE chưa add guard/redirect theo BA chốt 2026-05-11. | [r7-reverify-2026-05-12-bug-034-standalone-list-still-open.png](../bug-reports/hop-dong-tv/image/r7-reverify-2026-05-12-bug-034-standalone-list-still-open.png) | ❌ **Still Open** (Minor per bug file · Major per dev-fix-list — sev drift, BA chốt) |
| BUG-HDTV-037 (mới R19) | New R19 | TVV detail tab "Lịch sử hỗ trợ" → table HDTV cột Trạng thái render raw enum `DANG_THUC_HIEN` thay vì "Đang thực hiện" (i18n missing) | [r7-2026-05-12-hdtv-028-multi-row-tvv0035-2-rows.png](../bug-reports/hop-dong-tv/image/r7-2026-05-12-hdtv-028-multi-row-tvv0035-2-rows.png) | ❌ **New Open Minor P3** |
| BUG-HDTV-038 (mới R19) | New R19 | TVV detail tab "Lịch sử hỗ trợ" → pagination text "mặt hàng" thay vì "kết quả"/"mục" (e-commerce template leak) | Cùng screenshot trên | ❌ **New Open Minor P3** |

### Bug Summary

| Tổng | Open | Partial | Closed | Closed-verified R6-R7 | New bug R19 | Nguồn |
|---:|---:|---:|---:|---:|---:|---|
| 15 | 3 (HDTV-034/037/038) | 0 | 12 | 0 ở R19 retest (10 đã Closed R3-R6) | 2 (HDTV-037 + 038) | Bug Summary Table `bug-report-r7-7-14-hdtv.md` |

### TC/Path Bị Ảnh Hưởng

| TC/path | Liên quan bug | Trạng thái | Nguyên nhân block | Phương án | Owner |
|---|---|---|---|---|---|
| 24/26 TC HDTV PASS R3-R6 | 10 bug Closed R3-R6 | ✅ Đã đóng | — | — | — |
| HDTV-024 (route standalone) | HDTV-034 | 🚫 Vẫn block | FE chưa add guard, BE chưa middleware role check | Dev FE add guard + Dev BE 403 + BA chốt giữ/xoá | Dev FE + BE + BA |
| HDTV-028 (TVV detail i18n) | HDTV-037 + HDTV-038 | 🚫 Vẫn block | FE missing i18n mapping cho enum DANG_THUC_HIEN + text "mặt hàng" leak | Dev FE: add i18n + đổi pagination text | Dev FE |
| 14 TC defer v2.1 out-of-scope | — | — | Spec v2.1 ngăn UC163 sub-resource | Out-of-scope per SRS v2.1 | — |

### Testability Sweep

| TC/path | Chạy được? | Setup | Loại blocker | Action | Owner |
|---|---|---|---|---|---|
| 24 core HDTV CRUD + accordion + N:N link VV | ✅ Đã pass R3-R6 | — | — | — | — |
| HDTV-024 standalone route | ❌ Vẫn block | FE guard + BE 403 + BA chốt | chờ dev fix bug + chờ BA confirm spec | Dev FE+BE+BA cùng quyết | Dev FE + BE + BA |
| HDTV-028 TVV i18n | ❌ Vẫn block | FE add mapping enum + text override | chờ dev fix bug | Dev FE i18n fix | Dev FE |
| 14 TC v2.1 defer | ❌ Out-of-scope | — | lý do khác (out-of-scope spec) | Không action | — |

### Setup Cần Chuẩn Bị

Không có setup QA-side.

### Spec/BA Check

| TC/vấn đề | Câu hỏi | SRS check | Kết luận | Verdict |
|---|---|---|---|---|
| HDTV-034 standalone route | Giữ route ẩn có guard hay xoá hoàn toàn? | `srs-v3.5.md line 660 M-01` "KHÔNG có menu riêng" + BA chốt 2026-05-11 "route HDTV chỉ truy cập từ accordion VV" | BA đã chốt route HDTV không standalone — chỉ accordion VV. Dev FE+BE phải implement guard/redirect | ⚠️ **BA đã chốt 2026-05-11. Dev chưa apply** — không phải BA-blocked, mà là dev fix |

### Phương Án Xử Lý Tiếp Theo

| Nhóm | Áp dụng | Việc cần làm | Điều kiện xong | Ưu tiên | Owner |
|---|---|---|---|---|---|
| Dev FE guard | HDTV-034 | Add route guard `/hop-dong-tv/danh-sach` — non-context-VV → redirect dashboard hoặc 404 | `cb_nv_tw_06` gõ URL trực tiếp → /403 hoặc redirect; accordion VV vẫn render | P1 (dev-fix-list) | Dev FE |
| Dev BE 403 | HDTV-034 | Middleware role check `/api/v1/hop-dong-tu-vans` role không có perm `read_hdtv` → 403 ERR-PERM-SYS-00-01 | Cross-role test confirm 403 | P1 | Dev BE |
| Dev FE i18n | HDTV-037 + HDTV-038 | Map enum `DANG_THUC_HIEN`→"Đang thực hiện" + pagination text "mặt hàng"→"mục"/"kết quả" | TVV detail tab render label tiếng Việt + pagination đúng từ | P3 | Dev FE |

### Follow-up TC

| TC | Lý do | Setup | Kết quả kỳ vọng |
|---|---|---|---|
| HDTV-024 (standalone route block) | Sau Dev FE+BE fix HDTV-034 | `cb_nv_tw_06` gõ URL trực tiếp | /403 hoặc redirect dashboard |
| HDTV-028 (TVV i18n) | Sau Dev FE fix HDTV-037/038 | TVV detail có ≥1 HDTV link | Cột Trạng thái = "Đang thực hiện" + pagination "mục"/"kết quả" |

### Tóm Tắt Cuối — HDTV

- Re-verify R19: **0 bug closed mới · 3 Open giữ nguyên (HDTV-034 + 2 mới HDTV-037/038 i18n).**
- TC/path chạy được ngay: không có (24 core đã pass).
- TC/path vẫn block: **HDTV-024 standalone route chờ Dev FE+BE · HDTV-028 i18n chờ Dev FE.**
- Cần dev BE seed: không có.
- Việc cần làm tiếp: (1) Dev FE add route guard + Dev BE middleware 403 (HDTV-034) · (2) Dev FE i18n enum + pagination (HDTV-037/038).

---

## Tóm Tắt Cuối — Toàn 7 module

- **Re-verify R19/R19c:** 9 bug Closed-verified (R16-001/004/008/009 TVCS + DG-010/013 + POOL-CG/TVV-DETAIL VV + CHITRA-009) · 5 bug Open/Partial giữ nguyên (R16-005 + TVV-PERM + LICHSU-01 + DG-014 + CHITRA-010) · 2 bug Reproduced (PC-WRN-01 + TVN-005) · 3 bug Open mới HDTV-034/037/038.
- **TC/path chạy được ngay (sau R19/R19c):**
  - TVCS: 4 TC TLPL CRUD (TV-023/024/025/043)
  - VV: 5 TC TVV/PC (VV-013/014/015/016/033)
  - DG: 2 TC (TC07 + TC18)
  - ChiTra: 10 TC sub-phase R7.7.12.2 wording (đã pass R2)
  - VV workflow: 12/12 transition (đã pass R13)
  - HDTV: 24 core TC (đã pass R6)
  - TVN: 31 core TC (đã pass R14)
  - **Tổng: 25 TC mới unblock + 77 TC đã pass trước R19 = 102 TC clean.**
- **TC/path chạy được sau setup QA-side:** không có TC nào cần setup QA-side mới (mọi state advance đã có hoặc cần dev fix).
- **TC/path vẫn block bởi bên ngoài:**
  - Dev FE bug: R16-005 button [Công khai] · DG-014 dropdown filter · PC-WRN-01 button [Tìm thủ công] · HDTV-034 route guard · HDTV-037/038 i18n
  - Dev BE bug: TVV-PERM `trinh-phe-duyet_vu_viec` · LICHSU 4 enum thiếu · CHITRA-010 `ngayYeuCauBoSung` · TVN-005 enum `TU_VAN`
  - BA confirm spec: DG-014 UUID `bbbbbbbb-...-0018` giữ/xoá (Minor)
  - External integration: DVC LGSP (CHITRA-008) · mTLS PLQG (TVN-008 + 5 TC) · DN VNeID Tier 2 (8 TC VV) — defer
- **Cần dev BE seed dữ liệu trong hệ thống:** **không có**. Mọi seed gap đều seed được từ UI workflow QA-side (VV state advance, HSCT state, DG đợt advance, TVCS state).
- **Việc cần làm tiếp (ưu tiên P1→P3):**
  1. **P1 Dev FE:** R16-005 (TVCS button Công khai) · HDTV-034 (route guard) · TVV-PERM (BE) trinh-phe-duyet · CHITRA-010 (BE) ngayYeuCauBoSung
  2. **P2 Dev:** PC-WRN-01 (FE button Tìm thủ công) · TVN-005 (FE+BE enum TU_VAN)
  3. **P3 Dev:** DG-014 (FE filter) · LICHSU-01 (BE 4 enum) · HDTV-037/038 (FE i18n)
  4. **P3 BA:** DG-014 UUID confirm
  5. **QA chạy ngay:** 11 TC unblock R19/R19c (TVCS-4 + VV-5 + DG-2)
- **Sau khi xong follow-up TC:** dùng `qa-module-status-audit` cho từng module để kết luận full readiness.

---

---

## R19c-followup execution — 11 TC unblock (2026-05-12 21:30:00)

**Mục tiêu:** Chạy 11 TC unblock identified ở audit này bằng 3 agent song song (MCP Chrome DevTools), mỗi module dùng 1 account khác.

**Verdict tổng:** 8/11 ✅ Đạt · 0 ⚠️ Sai spec · 2 ❌ Lỗi mới · 1 🚫 Block cascade.

### Bảng tổng kết 11 TC

| Module | TC | Account | Status | Note |
|---|---|---|:-:|---|
| TVCS | TV-023 Create TLPL | `cb_nv_tw_06` | ✅ Đạt | POST 201, row visible |
| TVCS | TV-024 Read/List + Update | `cb_nv_tw_06` | ✅ Đạt | GET 200 + PATCH 200 persist |
| TVCS | TV-025 Delete TLPL | `cb_nv_tw_06` | ✅ Đạt | DELETE 204 |
| TVCS | TV-043 Công khai TLPL | `cb_nv_tw_06` | ❌ Lỗi | Upload BE 500 → block workflow |
| VV | VV-013 Phân công CG cá nhân | `cb_nv_tw_03` | ✅ Đạt | Dropdown 3 loại OK, lưu phân công |
| VV | VV-014 TVV detail view | `tvv_r11_mailfix` | ✅ Đạt | TVV-DETAIL-403 R18 fix confirm |
| VV | VV-015 Cập nhật KQ | `tvv_r11_mailfix` | ❌ Lỗi | FE thiếu button action ở DANG_XU_LY |
| VV | VV-016 Hoàn thành VV | `tvv_r11_mailfix` | 🚫 Block | Cascade VV-015 + perm gap |
| VV | VV-033 Nhận phân công | `tvv_r11_mailfix` | ✅ Đạt | DA_PHAN_CONG → DANG_XU_LY OK |
| DG | TC07 Trọng số 30 | `cb_nv_tw_05` | ✅ Đạt | Σ=90% lưu OK, BUG-DG-010 fix confirm |
| DG | TC18 QTHT R-only | `qtht_01` | ✅ Đạt | 0 button create/edit/delete |

### Bug mới phát hiện (2 bug Major P1)

| Bug ID | Module | Severity | Mô tả ngắn | File |
|---|---|:-:|---|---|
| BUG-BE-TVCS-R19c-010 | TVCS | Major P1 | POST `/api/v1/tu-lieu-phap-ly-vvs/upload` trả 500 `ERR-SYS-00-00-01` với multipart PDF hợp lệ. Cascade block TV-057/058. | [bug-report-r7-7-5-tvcs-r16.md](../bug-reports/tu-van-chuyen-sau/bug-report-r7-7-5-tvcs-r16.md) |
| BUG-VV-R19c-001 | VV | Major P1 | TVV state DANG_XU_LY không thấy button [Cập nhật KQ]/[Hoàn thành]/[Trình phê duyệt] dù BE 20 perm + endpoint POST OK 201. Root cause FE missing render. | [bug-report-r7-7-3-functional-vu-viec.md](../bug-reports/vu-viec/bug-report-r7-7-3-functional-vu-viec.md) |

### Action tiếp theo

| Ưu tiên | Nội dung | Owner |
|:-:|---|:-:|
| P1 | Fix BE upload handler `/tu-lieu-phap-ly-vvs/upload` 500 → unblock TV-043 + TV-057/058 | Dev BE |
| P1 | Fix FE render action buttons cho TVV state DANG_XU_LY (UC65 FR-V.I-15) → unblock VV-015/016 | Dev FE |
| P2 | Dev FE add button [Công khai]/[Hủy công khai] TVCS DA_DUYET (BUG-FE-TVCS-R16-005 vẫn Open) | Dev FE |

### Files updated

- Functional report appended `## R19c-followup` section:
  - [functional-test-report-r7-7-5-tvcs.md](../../functional/tu-van-chuyen-sau/functional-test-report-r7-7-5-tvcs.md) — TVCS 4 TC
  - [functional-test-report-r7-7-3-vu-viec.md](../../functional/vu-viec/functional-test-report-r7-7-3-vu-viec.md) — VV 5 TC
  - [functional-test-report-r7-7-9-danh-gia.md](../../functional/danh-gia/functional-test-report-r7-7-9-danh-gia.md) — DG 2 TC
- Bug-report mới row + entry:
  - TVCS BUG-BE-TVCS-R19c-010 vào `bug-report-r7-7-5-tvcs-r16.md` (9→10 bug, severity 8/1→9/2)
  - VV BUG-VV-R19c-001 vào `bug-report-r7-7-3-functional-vu-viec.md` (11/3/7 severity sync)
- Screenshots: 17 file (7 TVCS + 5 VV + 5 DG) tại `bug-reports/<module>/image/r19c-followup-*.png`

---

**File này tạo bởi:** Claude Code (Opus 4.7) 2026-05-12 22:30:00 theo template [`.agents/skills/qa-bugfix-reverify-audit/SKILL.md`](../../../../.agents/skills/qa-bugfix-reverify-audit/SKILL.md). R19c-followup execution section append 2026-05-12 22:45:00.

**Bug-report nguồn (status sync verified):**
- [tu-van-chuyen-sau/bug-report-r7-7-5-tvcs-r16.md](../bug-reports/tu-van-chuyen-sau/bug-report-r7-7-5-tvcs-r16.md) — Round R20
- [vu-viec/bug-report-r7-7-3-functional-vu-viec.md](../bug-reports/vu-viec/bug-report-r7-7-3-functional-vu-viec.md) — Round R19c
- [vu-viec/bug-report-flow-vu-viec.md](../bug-reports/vu-viec/bug-report-flow-vu-viec.md) — Round R19
- [danh-gia/bug-report-flow-danhgia.md](../bug-reports/danh-gia/bug-report-flow-danhgia.md) — Round R19
- [chi-tra/bug-report-r7-7-12-2-fr14-bo-sung.md](../bug-reports/chi-tra/bug-report-r7-7-12-2-fr14-bo-sung.md) — Round R19
- [tu-van-nhanh/bug-report-r7-7-11-tvn.md](../bug-reports/tu-van-nhanh/bug-report-r7-7-11-tvn.md) — Round R19
- [hop-dong-tv/bug-report-r7-7-14-hdtv.md](../bug-reports/hop-dong-tv/bug-report-r7-7-14-hdtv.md) — Round R19
