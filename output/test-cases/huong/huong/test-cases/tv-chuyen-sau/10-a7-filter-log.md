# A7 — UI/Function-Testable Filter (Audit Log)

> **Phiên bản:** 1.0 · **Ngày:** 2026-05-07 · **Module:** FR-12 TV Chuyên sâu
> **Mục đích:** Log decision GIỮ/SỬA/LOẠI per TC. Đảm bảo Phase B chạy được 100% qua MCP chrome-devtools.
> **Iron rule áp dụng:** TC LOẠI/SỬA Edit IN-PLACE file UC gốc; file này chỉ là audit log.

---

## A7 Filter Rule (recap §3.1 plan.md)

| Action | Tiêu chí |
|--------|---------|
| ❌ **LOẠI** | TC require DB query trực tiếp / curl API thuần / cron-job background không có UI feedback |
| ✏️ **SỬA** | TC verify-DB → verify-network qua MCP `list_network_requests`; TC API-only nếu module có UI bridge → re-route qua UI flow |
| ✅ **GIỮ** | TC chạy 100% qua UI/function user-facing (verify network gián tiếp khi user thao tác UI vẫn OK) |

---

## 1. Tổng quan decision

| File | Trước A7 | Sau A7 | LOẠI | SỬA | GIỮ |
|---|---:|---:|---:|---:|---:|
| 01 quan-ly-tvcs (UC147) | 39 | 39 | 0 | 0 | 39 |
| 02 tim-kiem-tvcs (UC148) | 19 | 19 | 0 | 0 | 19 |
| 03 quan-ly-hspl (UC150) | 20 | 20 | 0 | 3 | 17 |
| 04 quan-ly-tu-lieu-pl (UC152) | 21 | 21 | 0 | 2 | 19 |
| 05 permission-matrix | 14 | 14 | 0 | 0 | 14 |
| 06 api-inbound (UC149/151/153) | 12 | 12 | 0 | 0 | 12 |
| **Total** | **125** | **125** | **0** | **5** | **120** |

**Lý do 0 LOẠI module-level:** UC149/151/153 (M-type API inbound) đã được merge vào file 06 với pattern verify SIDE-EFFECT UI ở A3 (file header line 9-13 đã quote A7 filter rule). Mọi TC trong 6 file đều có UI bridge — không TC nào require pure DB/API/cron isolation.

**Lý do 5 SỬA:** Step verify "Query DB direct (qtht_01)" / "Query Cổng PLQG backend log" / "Server: kiểm tra file storage orphan" → re-route sang `list_network_requests` verify response API hoặc verify gián tiếp qua UI list count.

---

## 2. Decision detail per TC

### File 01 — Quản lý TVCS (UC147) — 39 TC ✅ all GIỮ

| TC ID | Decision | Lý do |
|---|---|---|
| TC-TVCS-001 | ✅ GIỮ | UI Verify SCR-X1-01 + SCR-X1-02 layout — 100% MCP `take_snapshot` |
| TC-TVCS-002 | ✅ GIỮ | CREATE qua form UI + verify network POST `/api/v1/tu-van-chuyen-sau` |
| TC-TVCS-003 | ✅ GIỮ | READ list 3 tab + verify network GET có tab param |
| TC-TVCS-004 | ✅ GIỮ | UPDATE form UI + verify network PUT 200 |
| TC-TVCS-005 | ✅ GIỮ | DELETE soft qua action UI + network DELETE response |
| TC-TVCS-006 | ✅ GIỮ | Form UI inline error nguyên văn ERR-TVCS-01 |
| TC-TVCS-007 | ✅ GIỮ | API direct via DevTools (UI dropdown filter — bypass), verify HTTP 400 response qua `list_network_requests` (network verify gián tiếp) |
| TC-TVCS-008 | ✅ GIỮ | RTE paste 51KB qua UI form → inline error |
| TC-TVCS-009..019 | ✅ GIỮ | SM-TVCS T2-T10 transitions qua action button UI + modal + verify network response |
| TC-TVCS-020/021 | ✅ GIỮ | Invalid transition — API direct via DevTools, verify HTTP 400 response qua network capture |
| TC-TVCS-022 | ✅ GIỮ | Optimistic lock 2 user UI parallel session |
| TC-TVCS-023..027 | ✅ GIỮ | Công khai chuyên trang qua switch UI + verify network outbound API Cổng PLQG |
| TC-TVCS-028/029 | ✅ GIỮ | Batch action checkbox UI + verify boundary 100/101 qua network response |
| TC-TVCS-030 | ✅ GIỮ | Boundary noi_dung_tu_van qua RTE paste UI |
| TC-TVCS-031 | ✅ GIỮ | Data quality Unicode qua UI form + verify hiển thị detail |
| TC-TVCS-032 | ✅ GIỮ | Double-click race qua MCP `click` x2 |
| TC-TVCS-033 | ✅ GIỮ | Session expire — verify UI 401 redirect / modal |
| TC-TVCS-034 | ✅ GIỮ | Browser back button qua MCP navigation |
| TC-TVCS-035 | ✅ GIỮ | Concurrent CK 2 user UI parallel |
| TC-TVCS-036 | ✅ GIỮ | Boundary file size qua upload UI + verify HTTP 413 |
| TC-TVCS-037 | ✅ GIỮ | Dashboard widget UI + verify network GET aggregate response |
| TC-TVCS-038 | ✅ GIỮ | A6 fill — Notes đã ghi nguyên văn "verify qua network response, không query DB trực tiếp (A7-compliant)" |
| TC-TVCS-039 | ✅ GIỮ | API direct via DevTools `evaluate_script` override request body — verify response qua `list_network_requests` |

### File 02 — Tìm kiếm TVCS (UC148) — 19 TC ✅ all GIỮ

| TC ID | Decision | Lý do |
|---|---|---|
| TC-TVCS-TK-001 | ✅ GIỮ | UI Verify filter-bar 8 control |
| TC-TVCS-TK-002..010 | ✅ GIỮ | Filter qua UI control + verify network GET query params |
| TC-TVCS-TK-011 | ✅ GIỮ | UI inline error tu_ngay > den_ngay |
| TC-TVCS-TK-012 | ✅ GIỮ | SQL injection / XSS sanitize — verify UI behavior + network response |
| TC-TVCS-TK-013 | ✅ GIỮ | API direct via DevTools page_size boundary — verify HTTP 400 response |
| TC-TVCS-TK-014 | ✅ GIỮ | Cross-unit isolation — UI list filter scope |
| TC-TVCS-TK-015 | ✅ GIỮ | Export Excel — Notes đã quote "verify qua network endpoint + response... không verify query DB" (A7-compliant) |
| TC-TVCS-TK-016..019 | ✅ GIỮ | Boundary + cross-feature filter qua UI |

### File 03 — Quản lý HSPL (UC150) — 20 TC (3 SỬA + 17 GIỮ)

| TC ID | Decision | Lý do | Action |
|---|---|---|---|
| TC-HSPL-001 | ✅ GIỮ | UI Verify tab "Hồ sơ PL" toolbar + 11 cột | — |
| **TC-HSPL-002** | ✏️ **SỬA** | Notes ban đầu chỉ ghi "Verify network request `POST...`" — clarify thêm rằng STATE 7 common fields + ClamAV PASS verify qua response body, không cần DB query | Cập nhật Notes "A7 GIỮ — verify qua `list_network_requests` capture POST /api/v1/ho-so-phap-ly-dn response chứa 7 common fields + ma_ho_so regex; ClamAV PASS qua HTTP 200" |
| TC-HSPL-003 | ✅ GIỮ | READ chi tiết qua modal UI + network GET response |
| TC-HSPL-004 | ✅ GIỮ | UPDATE qua form UI + network PUT |
| **TC-HSPL-005** | ✏️ **SỬA** | Step "Query DB direct (qtht_01) → record vẫn tồn tại với is_deleted=1" → vi phạm A7 (DB query thuần) | Đổi sang `list_network_requests` verify response DELETE `/api/v1/ho-so-phap-ly-dn/{id}` body chứa `is_deleted: true`/`deleted_at` set; Notes thêm "A7 SỬA: changed from DB-direct to UI-verify via list_network_requests" |
| TC-HSPL-006 | ✅ GIỮ | Export Excel qua button UI + network endpoint verify |
| TC-HSPL-007..009 | ✅ GIỮ | Search 5 filter qua filter-bar UI |
| TC-HSPL-010..013 | ✅ GIỮ | ERR-HSPL-01..06 qua form UI hoặc API direct via DevTools (verify response) |
| TC-HSPL-014/015 | ✅ GIỮ | Permission cross-don_vi + NHT R+U qua UI navigation + API direct response 403 (verify qua network) |
| **TC-HSPL-017** | ✏️ **SỬA** | Step 4 "Server: kiểm tra file storage có file orphan" + "Storage scan: file 15MB không tồn tại" → vi phạm A7 (DB/storage query thuần, không phải UI) | Đổi sang `list_network_requests` verify GET list HSPL không có record dở dang; verify retry [+ Thêm hồ sơ] với cùng tên không bị duplicate-name reject (gián tiếp UI-bridge); Notes thêm "A7 SỬA: changed from server storage scan to UI list count + retry duplicate check" |
| TC-HSPL-016/018/019 | ✅ GIỮ | Boundary file / date validation / Unicode normalization qua UI form |
| TC-HSPL-020 | ✅ GIỮ | A6 đã note nguyên văn "A7 GIỮ" — chỉ verify render-side khi user truy cập (không test cron auto-update DB) |

### File 04 — Quản lý TLPL (UC152) — 21 TC (2 SỬA + 19 GIỮ)

| TC ID | Decision | Lý do | Action |
|---|---|---|---|
| TC-TLPL-001 | ✅ GIỮ | UI Verify tab "Tư liệu PL" toolbar + 5 cột |
| TC-TLPL-002..005 | ✅ GIỮ | CRUD qua form UI + verify network response |
| **TC-TLPL-006** | ✏️ **SỬA** | Step "Query Cổng PLQG (qtht_01 verify backend log) → tư liệu không còn" → vi phạm A7 (query backend log của Cổng PLQG external = DB-query thuần) | Đổi sang `list_network_requests` verify backend đã fire DELETE `/portal-plqg/tu-lieu/{ma_cong}` (outbound API call) + response 200; Notes thêm "A7 SỬA: changed from Cổng PLQG backend log query to network outbound DELETE verification" |
| TC-TLPL-007..010 | ✅ GIỮ | Upload file + virus scan + search qua UI |
| TC-TLPL-011..013 | ✅ GIỮ | Công khai BR-FLOW-07 qua action UI + verify network outbound Cổng PLQG |
| **TC-TLPL-014** | ✏️ **SỬA** | Step 6 "Query DB qtht_01 verify thoi_gian_dang_tai" → vi phạm A7 (DB query thuần) | Đổi sang `list_network_requests` capture response GET `/api/v1/tu-lieu-phap-ly-vv/{id}` mới nhất → verify field `thoi_gian_dang_tai` trong body; UI hiển thị "Đã đăng tải lúc {T3}"; AUDIT_LOG verify qua tab Nhật ký UI; Notes thêm "A7 SỬA: changed from DB query qtht to network response field verify" |
| TC-TLPL-015..020 | ✅ GIỮ | Negative ERR + edge race + boundary qua UI/API-via-DevTools |
| TC-TLPL-021 | ✅ GIỮ | Preview file qua viewer UI + network response Content-Disposition header verify |

### File 05 — Permission Matrix — 14 TC ✅ all GIỮ

| TC ID | Decision | Lý do |
|---|---|---|
| TC-PERM-001 | ✅ GIỮ | UI Verify role-based action visibility 4 role |
| TC-PERM-002/003 | ✅ GIỮ | BR-AUTH-01 Tier 1/2 login flow qua /login UI + OTP=666666 |
| TC-PERM-004 | ✅ GIỮ | PD cùng cấp Happy qua action UI |
| TC-PERM-005/006 | ✅ GIỮ | PD khác cấp Negative — direct URL deeplink + mock POST via DevTools (verify 403 response qua network) |
| TC-PERM-007/008 | ✅ GIỮ | Cross-unit IDOR — UI list filter + direct URL + mock PUT/DELETE via DevTools |
| TC-PERM-009 | ✅ GIỮ | CG vs CG ngoài action button visibility qua UI |
| TC-PERM-010 | ✅ GIỮ | NHT R+U HSPL — toolbar/action visibility UI + API direct 403 verify response |
| TC-PERM-011..013 | ✅ GIỮ | Edge session/role/SSO — qua devtools cookie clear + multi-tab |
| TC-PERM-014 | ✅ GIỮ | Permission HSPL/TLPL CB_PD/QTHT explicit — toolbar/action visibility UI + API direct response 403 |

### File 06 — API Inbound Side-Effect (UC149/151/153) — 12 TC ✅ all GIỮ

| TC ID | Decision | Lý do |
|---|---|---|
| Tất cả 12 TC | ✅ GIỮ | File header line 9-13 đã quote A7 rule + footer line 357-359 đã ghi rõ "Không có TC API curl thuần. Mọi TC verify SIDE-EFFECT UI (badge 'Mới', count tab, accordion, notification, audit log). Trigger API là phương tiện setup data (Postman/test endpoint), KHÔNG phải step verify chính." Tất cả TC verify count tab, badge, accordion, notification list (UI-driven). Trigger API qua test endpoint admin/Postman trong Notes (setup data, không phải step chính) |

---

## 3. SỬA decisions với before/after

### TC-HSPL-005 — DELETE soft HSPL với confirm modal

**Before (PERSIST):**
> Reload tab → record không còn. Query DB direct (qtht_01) → record vẫn tồn tại với is_deleted=1 (soft delete).

**After (PERSIST):**
> Reload tab → record không còn. `list_network_requests` verify DELETE `/api/v1/ho-so-phap-ly-dn/{id}` response 200 + body chứa `is_deleted: true`/`deleted_at` set (BR-DATA-01 soft delete — verify qua API response, KHÔNG query DB trực tiếp).

**Reason:** Step "Query DB direct (qtht_01)" yêu cầu DB query thuần — vi phạm A7 filter rule. Backend response API DELETE chứa flag is_deleted nên có thể verify qua network capture, không cần DB.

---

### TC-HSPL-002 — CREATE HSPL thành công

**Before (Notes):**
> Verify network request `POST /api/v1/ho-so-phap-ly-dn` với multipart/form-data (file upload).

**After (Notes):**
> A7 GIỮ — verify qua `list_network_requests` capture POST `/api/v1/ho-so-phap-ly-dn` response chứa 7 common fields + ma_ho_so regex; verify ClamAV PASS qua HTTP 200 (không query DB). Multipart/form-data file upload qua UI form.

**Reason:** Expected nói "INSERT HO_SO_PHAP_LY_DN với 7 common fields BR-DATA-03" + "INSERT FILE_DINH_KEM linked, ClamAV scan PASS" — clarify rằng verify qua network response body, không phải DB query.

---

### TC-HSPL-017 — File PDF corrupt mid-upload (network interrupt)

**Before (Step 4 + PERSIST):**
> 4. Server: kiểm tra file storage có file orphan không.
> ...
> PERSIST: Reload danh sách HSPL → KHÔNG có record dở dang. Storage scan: file 15MB không tồn tại hoặc cleanup theo policy.

**After (Step 4 + PERSIST):**
> 4. `list_network_requests` verify GET `/api/v1/ho-so-phap-ly-dn?...` response — count record của DN không có HSPL pending dở dang.
> ...
> PERSIST: Reload danh sách HSPL → KHÔNG có record dở dang. Verify retry [+ Thêm hồ sơ] với cùng tên HSPL không bị duplicate-name reject (chứng minh record interrupt đã được clean up backend-side).

**Reason:** Step "Server: kiểm tra file storage có file orphan" + "Storage scan" yêu cầu access filesystem backend trực tiếp — vi phạm A7 (no UI bridge). Re-route sang verify gián tiếp qua UI list count + retry duplicate-name check.

---

### TC-TLPL-006 — DELETE TLPL trạng thái CONG_KHAI → API gỡ Cổng PLQG

**Before (PERSIST):**
> Reload tab → record biến mất. Query Cổng PLQG (qtht_01 verify backend log) → tư liệu không còn.

**After (PERSIST):**
> Reload tab → record biến mất. `list_network_requests` verify backend đã fire `DELETE /portal-plqg/tu-lieu/{ma_cong}` (outbound API call tới Cổng PLQG) + response 200 OK trước khi soft delete; verify response DELETE `/api/v1/tu-lieu-phap-ly-vv/{id}` body chứa `is_deleted: true`.

**Reason:** "Query Cổng PLQG backend log" yêu cầu access log backend của hệ thống external (Cổng PLQG) — không có UI bridge. Re-route sang capture network outbound DELETE request fired (UI-driven action gián tiếp).

---

### TC-TLPL-014 — Edge bật-tắt-bật CONG_KHAI

**Before (Step 6):**
> 6. Query DB qtht_01 verify thoi_gian_dang_tai.
> Step 6 DB: thoi_gian_dang_tai = T3.

**After (Step 6):**
> 6. `list_network_requests` capture response GET `/api/v1/tu-lieu-phap-ly-vv/{id}` mới nhất → verify field `thoi_gian_dang_tai` trong response body.
> Step 6 API response: Body GET TLPL detail có `thoi_gian_dang_tai = T3` (verify qua network capture, không qua DB). UI hiển thị "Đã đăng tải lúc {T3 dd/mm/yyyy HH:mm}".
> AUDIT_LOG: 3 entries: PUBLISH (T1) / UNPUBLISH (T2) / PUBLISH (T3) — verify qua tab Nhật ký UI hoặc accordion timeline.

**Reason:** Step "Query DB qtht_01" yêu cầu DB query thuần. Field `thoi_gian_dang_tai` được serialize trong response GET detail nên verify qua network capture. AUDIT_LOG verify qua tab Nhật ký UI (accordion 5 SCR-X1-02).

---

## 4. LOẠI decisions với reasoning

**Không có TC LOẠI ở Phase A7.**

Lý do:
- 6 file UC đã được A3 design theo pattern UI-driven từ đầu (file 06 explicitly note A7 rule trong header).
- 3 UC inbound M-type (UC149/151/153) đã merge vào file 06 với verify SIDE-EFFECT UI (badge "Mới", count tab, accordion, notification list) — KHÔNG phải curl thuần.
- TC-HSPL-020 (SM HSPL HET_HAN render) đã được A6 note "A7 GIỮ" — chỉ verify render-side compute khi user truy cập, không test cron auto-update DB.
- 5 TC SỬA đều có UI bridge / network bridge nên không cần LOẠI.

**Cron job / scheduled job / queue worker no-UI:** SRS có quote SLA 2 ngày LV (SPEC-CLARIFY-TVCS-03) + cron HET_HAN HSPL (SPEC-CLARIFY-HSPL-CRON), nhưng:
- 2 SPEC-CLARIFY trên đang Open chờ BA respond.
- Hiện tại không có TC nào test cron job thuần (chỉ test render-side / side-effect UI khi user truy cập).
- Nếu BA respond cron auto-update DB no-UI → forwarded qua SPEC-CLARIFY-A7 ticket Phase B.

---

## 5. Final TC count + Phase A done acceptance

### Final TC counts

| File | Pre-A7 | Post-A7 | Δ |
|---|---:|---:|---:|
| 01-TC-FR-X1-01-quan-ly-tvcs.md | 39 | 39 | 0 |
| 02-TC-FR-X1-02-tim-kiem-tvcs.md | 19 | 19 | 0 |
| 03-TC-FR-X1-04-quan-ly-hspl.md | 20 | 20 | 0 |
| 04-TC-FR-X1-06-quan-ly-tu-lieu-pl.md | 21 | 21 | 0 |
| 05-TC-permission-matrix.md | 14 | 14 | 0 |
| 06-TC-FR-X1-03-05-07-API-inbound-side-effect.md | 12 | 12 | 0 |
| **GRAND TOTAL** | **125** | **125** | **0** |

**SỬA delta:** 5 TC SỬA in-place (3 file 03 + 2 file 04). 0 TC LOẠI. 120 TC GIỮ unchanged.

### Phase A done acceptance check

| Tiêu chí | Yêu cầu | Thực tế | Pass? |
|----------|---------|---------|-------|
| ✅ 7 bước A1-A7 done | 7 step | A1 (đọc SRS) + A2 (00-test-plan-overview) + A3 (6 file UC) + A4 (07-edge-case-hunter) + A5 (08-traceability) + A6 (09-test-quality + bổ sung TC) + A7 (file này) | ✅ |
| ✅ Traceability ≥95% BR + 100% AC | ≥95% / 100% | Sau A6: BR 100% / AC 100% (per `09-REVIEW-test-quality.md`) | ✅ |
| ✅ 0 TC chỉ-DB/API thuần | 0 | 5 TC đã SỬA (HSPL-002/005/017 + TLPL-006/014). 0 TC còn DB/storage query thuần. API direct qua DevTools `evaluate_script` chỉ là phương tiện bypass UI dropdown filter, verify qua `list_network_requests` response → A7-compliant | ✅ |
| ✅ 0 TC sống ở file phụ (07/08/09/10) | 0 TC ở file phụ | 07-REVIEW-edge-case-hunter.md (A4 audit, đã merge TC vào 6 file UC) + 08-traceability-matrix.md (A5) + 09-REVIEW-test-quality.md (A6) + 10-a7-filter-log.md (A7) — all audit logs, không chứa TC | ✅ |
| ✅ SPEC-CLARIFY listed | Phase B ticket | 17 SPEC-CLARIFY đã capture qua A2-A6 (xem 09-REVIEW-test-quality.md §3 + 08-traceability-matrix.md §6.2). A7 không phát sinh thêm SPEC-CLARIFY mới | ✅ |
| ✅ Sibling pattern compliance | Match `bieu-mau/11-a7-filter-log.md` | Format Section 1-5 đầy đủ, decision matrix, before/after pairs, acceptance check | ✅ |

### Module-level LOẠI nguyên văn check

Không có UC bị LOẠI module-level ở FR-12 (khác với module W3.2 VV LOẠI UC53/UC55/CROSS-01). UC149/151/153 inbound đã được merge vào file 06 với pattern verify side-effect UI — A7-compliant không cần LOẠI.

### A7 Acceptance keyword check

| Keyword | Yêu cầu | Thực tế | Pass? |
|----------|---------|---------|-------|
| 0 TC keyword "verify DB row" | 0 | 0 (5 TC đã SỬA) | ✅ |
| 0 TC keyword "Query DB direct" | 0 | 0 (TC-HSPL-005 đã SỬA) | ✅ |
| 0 TC keyword "Query Cổng PLQG backend log" | 0 | 0 (TC-TLPL-006 đã SỬA) | ✅ |
| 0 TC keyword "Storage scan" | 0 | 0 (TC-HSPL-017 đã SỬA) | ✅ |
| 0 TC keyword "curl POST" / API thuần step chính | 0 | 0 (file 06 trigger Postman trong Notes — setup data, KHÔNG step chính) | ✅ |
| 0 TC keyword "cron job" / "background worker" no-UI | 0 | 0 (TC-HSPL-020 chỉ verify render-side, không test cron) | ✅ |
| TC require API verify gián tiếp qua MCP `list_network_requests` | OK (UI-driven) | TVCS-002/038/039 + HSPL-002/005/017 + TLPL-006/014 + permission TC + API-inbound TC — đều thao tác UI hoặc DevTools rồi verify network response | ✅ |

**Verdict:** ✅ **A7 PASS** — 100% TC UI/function-testable qua chrome-devtools MCP.

---

## Phase A W3.3 TVCS — DONE sign-off

| Step | Output | Status |
|------|--------|--------|
| A1 | Đọc SRS srs-fr-12 + 2 sibling reference (bieu-mau, vu-viec) | ✅ |
| A2 | 00-test-plan-overview.md (BR + AC + ERR + Permission Matrix + 14 SPEC-CLARIFY) | ✅ |
| A3 | 6 file UC (01-06): 39 + 19 + 20 + 21 + 14 + 12 = 125 TC | ✅ |
| A4 | 07-REVIEW-edge-case-hunter.md (+21 edge merged inline) | ✅ |
| A5 | 08-traceability-matrix.md (BR 100% / AC 100% / ERR 100%) | ✅ |
| A6 | 09-REVIEW-test-quality.md (score PASS) + 5 TC bổ sung (HSPL-020 + TVCS-038/039 + API-IN-011/012) | ✅ |
| A7 | 10-a7-filter-log.md (5 TC SỬA in-place, 0 LOẠI, 120 GIỮ) | ✅ |

**Phase A W3.3 TVCS:** ✅ **DONE 2026-05-07** — sẵn sàng flip todo.md `📝 → ✅` + cell Phase B.

**Active baseline blocker (Phase B aware):**
- BUG-FR12-001 (Critical) — action-bar Detail SCR-X1-02 empty (verified 2026-05-03 smoke). Phase B viết theo SRS spec đầy đủ; verify lại khi bug fix.
- 17 SPEC-CLARIFY tickets gửi BA (5 P0 / 8 P1 / 4 P2) — Phase B-Plan trigger conditional re-test khi BA respond.

---

*Generated 2026-05-07 by BMAD A7 (manual filter) — Phase A W3.3 FR-12 TV Chuyên sâu*
