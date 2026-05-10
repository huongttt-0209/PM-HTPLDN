# Functional Test Report — Thư viện Biểu mẫu (Module 7.9 v3.5)

| Thông tin | Giá trị |
|-----------|---------|
| **Module** | Thư viện Biểu mẫu, Hợp đồng — Module 7.9 |
| **SRS Reference** | [`srs-update-2026-5-5/_DELTA-MAP-FR09.md`](../../../../../input/srs-update-2026-5-5/_DELTA-MAP-FR09.md) + [`srs-update-2026-5-5/CHANGELOG-v3-to-v3.5.md` line 1010-1117](../../../../../input/srs-update-2026-5-5/CHANGELOG-v3-to-v3.5.md) — apply CR-01 (4 trường công khai + BR-PUBLIC-01/02/03) |
| **UC Coverage** | UC 92, 93, 94, 95, 96, 97, 98 (UC 163 đã MOVE sang FR-14) |
| **Người test** | QA Automation (Claude Code MCP) |
| **Ngày** | 2026-05-07 |
| **Môi trường** | http://103.172.236.130:3000/ |
| **OTP Bypass** | `666666` |
| **Test Method** | Hybrid (UI MCP + API direct via `evaluate_script` cho batch validation) |
| **Primary Account** | `cb_nv_tw_01` / `Secret@123` — CB Nghiệp vụ TW, đơn vị BTP-TW |
| **Round** | R7.7.10 |
| **Tài liệu tham chiếu** | [`output/funtion/7.9-bieu-mau.md`](../../../../funtion/7.9-bieu-mau.md) (47 TC) · [`workflow-test-report-r7-4-c1-bm.md`](../../workflow/bieu-mau/workflow-test-report-r7-4-c1-bm.md) (R7.4.C1) · [`bug-report-function-bm-r7-7-10.md`](../../bug-reports/bm/bug-report-function-bm-r7-7-10.md) (2 bugs R7.7.10) · [`bug-report-flow-bm-r7-4-c1.md`](../../bug-reports/bm/bug-report-flow-bm-r7-4-c1.md) (6 bugs R7.4.C1) |

---

## 1. Executive Summary

| Metric | Value |
|--------|-------|
| **Total Test Cases (spec v3.5)** | 47 (50 - 3 MOVED to 7.14) |
| **TC đã chạy thực tế (✅+⚠️+❌)** | 32/47 (68%) — TC đã đạt verdict cuối (PASS/PARTIAL/FAIL); KHÔNG tính ⏳ (chờ re-test) hoặc ⏭ (defer) |
| **TC đã thử (attempted, ≠ DEFER)** | 42/47 (89%) — gồm 32 đã chạy thực tế + 10 ⏳ Pending re-test (R7 attempt nhưng BLOCKED, R8 lần 3 unblock chờ R8 lần 4) |
| **Passed (✅)** | 23 — Happy 9 + Negative 4 + Workflow 5 + Authorization 3 (BM-032/033/034 R7.7.10b) + Cross-module 2 (BM-039/040 R7.7.10b) |
| **Failed (❌)** | 3 (BM-007 preview + BM-008 download — MinIO localhost; BM-016 UI silent reject) |
| **Blocked (🚫)** | 0 — sau R8 lần 3 BUG-BM-001 Closed (Switch added) → 10 CR-01 unblocked. BM-043/049/050 conditional (BUG-BM-002/004 chưa verify) chuyển sang ⏳ chờ test riêng. |
| **Pending re-test (⏳)** | 10 — BM-041..050 (CR-01) đã unblock R8 lần 3. Sẵn sàng dispatch R8 lần 4. |
| **Partial (⚠️)** | 6 — Negative 4 (BM-015 R7.7.10b TCP reset + BM-018/019/021 English error leak) + Workflow 1 (BM-026 UI silent 409) + Authorization 1 (BM-035 R7.7.10b NHT/CG PASS, TVV sub-defer) |
| **Defer (⏭/🔁)** | 5 — BM-010 (MinIO cascade) + BM-028/029 (R7.7.10b MCP upload tool block) + BM-036 (DN portal scope) + BM-038 (mTLS Postman) |
| **Overall Pass Rate** | 49% (23/47) PASS only · 62% (29/47) PASS+PARTIAL · 72% (23/32) PASS / TC đã chạy thực tế — sau R7.7.10b unblock + R8 lần 3 BUG-BM-001 closed |
| **P0 Pass Rate** | 64% (9/14 P0 tested) — 4 P0 CR-01 (BM-041/042/045/046) ⏳ Pending re-test R8 lần 4 (đã unblock R8 lần 3 BUG-BM-001 closed) |
| **Bugs Found (SRS-ref)** | 9 tổng (6 từ R7.4.C1 + 2 từ R7.7.10 + 1 mới R7.7.10b BUG-BM-009 Medium): 3 Critical, 2 Major, 4 Medium |
| **Health Score** | 60/100 (R7.7.10b unblock Authorization layer + audit verify; MinIO + 21MB-handling vẫn issue) |
| **Start Time** | 18:03 (UTC+7) |
| **End Time** | 19:00 (UTC+7) |
| **Total Duration** | 57 phút |
| **Browse Status** | OK — MCP suốt session ổn định, 0 crash |

### Pass Rate breakdown theo Type

| Type | Mô tả | TC count | PASS | PARTIAL | FAIL | BLOCKED | ⏳ Pending | DEFER | **Pass Rate** |
|------|-------|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| **Happy** | CRUD + list + filter (incl. 5 CR-01 ⏳ 041/046/047/049/050) | 17 | 9 | 0 | 2 (007/008) | 0 | 5 (041/046/047/049/050) | 1 (010) | **53%** |
| **Negative** | Validate input (incl. 3 CR-01 ⏳ 044/045/048) | 12 | 4 | 4 (015/018/019/021) | 1 (016) | 0 | 3 (044/045/048) | 0 | **33%** |
| **Workflow** | SM-BIEUMAU + công khai + xóa + bulk import (incl. 2 CR-01 ⏳ 042/043) | 10 | 5 | 1 (026) | 0 | 0 | 2 (042/043) | 2 (028/029) | **50%** |
| **Authorization** | Permission matrix R7.7.10b | 5 | 3 (032/033/034) | 1 (035) | 0 | 0 | 0 | 1 (036) | **60%** |
| **Cross-module** | API + Lĩnh vực + Audit | 3 | 2 (039/040) | 0 | 0 | 0 | 0 | 1 (038) | **67%** |
| **MOVED** | UC163 HĐ TV → FR-14 | 3 | — | — | — | — | — | — | N/A |
| **Total (47 TC v3.5)** | | **47** | **23** | **6** | **3** | **0** | **10** | **5** | **49%** PASS · **62%** PASS+PARTIAL |

> **Note:** CR-01 (10 TC = 041..050) được phân về Type column tự nhiên (Happy/Negative/Workflow), không tách row riêng để tránh double-count. Tất cả 10 CR-01 R7 ban đầu BLOCKED bởi BUG-BM-001/002/004 — **R8 lần 3 (2026-05-09): BUG-BM-001 Closed** (Switch added) → 7 CR-01 hoàn toàn unblocked (BM-041/042/044/045/046/047/048); 3 CR-01 conditional (BM-043/049/050 chờ verify BUG-BM-002/004). Tất cả 10 đã chuyển ⏳ Pending re-test, sẵn sàng R8 lần 4.

→ **Happy-path Pass Rate = 9/17 = 53%** (excluding CR-01 ⏳: 9/12 = 75%) — đủ seed cho module downstream. R7.7.10b unblock toàn bộ Authorization layer (60% PASS) + Cross-module (67% PASS). R8 lần 3 unblock 10 CR-01. Critical bug MinIO + BR-PUBLIC-02 vẫn pending.

### Verdict: **CONDITIONAL PASS — không thể release v3.5 cho đến khi fix BUG-BM-002/007 + BUG-BM-009** (BUG-BM-001 ✅ Closed R8 lần 3)

CRUD core + state machine + BR-PUBLIC-01 (BE-side) hoạt động đúng. R7.7.10b unblock toàn bộ Authorization layer (3 TC PASS + 1 PARTIAL) + Audit cross-module (BM-040 PASS). **R8 lần 3 (2026-05-09):** BUG-BM-001 đã Closed (Switch added) → 10 TC CR-01 (BM-041..050) chuyển từ 🚫 BLOCKED sang ⏳ Pending re-test, sẵn sàng dispatch R8 lần 4. Còn lại 2 bug Critical chặn release: BR-PUBLIC-02 không clear timestamp + MinIO localhost broken (chặn BM-007/008 preview/download). Thêm BUG-BM-009 Medium R7.7.10b — upload >20MB qua TCP reset thay vì graceful 413 Vietnamese error + side-effect kill auth session.

---

## 2. Test Case Results

> Status icon: ✅ PASS · ⚠️ PARTIAL · ❌ FAIL · 🚫 BLOCKED · ⏭ DEFER · 🔁 (carry-forward từ R7.4.C1) · ⏳ Pending re-test (đã unblock, chờ round mới)
>
> **Update 2026-05-09 (R8 lần 3 sync):** 10 TC CR-01 (BM-041..050) flip 🚫 → ⏳ — BUG-BM-001 đã Closed R8 lần 3 (Switch component đã add vào form). 10 TC ready để chạy trong R8 lần 4. Detail xem [`functional-test-report-r7-7-10-bm-r8.md` §0 Addendum](functional-test-report-r7-7-10-bm-r8.md#0-addendum-r8-lần-3--2026-05-09-1955-cập-nhật-sau-dev-claim-fix).

### 2.1 P0 — Core CRUD + State Machine (14 TC)

| TC ID | UC | Tên | Type | Status | Note |
|-------|-----|-----|------|:-:|------|
| BM-001 | UC92 | List TM phân trang + filter trạng thái | Happy | ✅ | Filter `?trangThai=AN` → 1 record (Biểu mẫu SHTT). Tabs Tất cả/Đã công khai/Nháp/Đã ẩn render. |
| BM-002 | UC92 | Tạo TM mới (default NHAP) | Happy | ✅ | POST `/thu-muc-bieu-maus` 201, id `58a429a8-...`, `trangThai=NHAP`. |
| BM-003 | UC95 | Xem list BM trong TM | Happy | ✅ | GET `/bieu-maus?thuMucId=...` 200, render BM-20260507-001 đầy đủ (cột Mã/Tên/Loại TL/TM/Kích thước/Trạng thái/Sync/Action). |
| BM-004 | UC95 | Tạo BM upload doc/docx ≤20MB | Happy | ✅ 🔁 | Đã seed BM-20260507-001 ở R7.4.C1 với `test-bm-r7-4-c1.docx` 917B. Upload+entity OK; Switch behavior verify R8 lần 4 sau BUG-BM-001 closed. |
| BM-005 | UC96 | Search BM theo keyword | Happy | ✅ | `?search=R7.4.C1` → 1 match. `?search=NotExists` → 0. |
| BM-008 | UC95 | Tải BM về (giữ tên gốc) | Happy | ❌ | [BUG-BM-007](../../bug-reports/bm/bug-report-function-bm-r7-7-10.md#bug-bm-007--preview--download-biểu-mẫu-trỏ-minio-localhost9000-không-reachable) — 302 → `localhost:9000/...` `ERR_CONNECTION_REFUSED` |
| BM-012 | UC95 | Xem chi tiết BM | Happy | ✅ | `/bieu-mau/{id}` render: Mã, Trạng thái, Tên, TM, Lĩnh vực, Loại hình, Định dạng (DOCX), Kích thước (917 B), Số lượt tải, Ngày tạo, Mô tả + 4 nút action. |
| BM-014 | UC92 | Tạo TM trùng tên | Negative | ✅ | POST với `tenThuMuc: "Biểu mẫu SHTT"` → 422 `ERR-TM-01` "Tên thư mục đã tồn tại trong đơn vị" (match spec). |
| BM-015 | UC95 | Upload file >20MB | Negative | ⚠️ | **R7.7.10b** — File `test-bm-21mb.docx` 22020096 bytes upload qua API direct → `ERR_CONNECTION_RESET`, side-effect kill auth session (`/auth/me 401`). BE rejects ≥20MB nhưng KHÔNG có graceful HTTP 413 + Vietnamese error. → [BUG-BM-009](../../bug-reports/bm/bug-report-r7-7-10b-bm.md#bug-bm-009--upload-file-20mb-không-có-graceful-413--invalidate-auth-session). |
| BM-016 | UC95 | Upload file sai format | Negative | ❌ | [BUG-BM-008](../../bug-reports/bm/bug-report-function-bm-r7-7-10.md#bug-bm-008--form-thêm-bm-silent-reject-file-invalid-không-có-toasterror) — `.txt` upload silent reject (no toast/error). |
| BM-022 | UC94 | Công khai TM NHAP→CONG_KHAI | Workflow | ✅ 🔁 | R7.4.C1 step 6 PASS. POST `/cong-khai` 200, syncStatus=SYNCED. |
| BM-023 | UC94 | Hủy công khai CONG_KHAI→AN | Workflow | ✅ 🔁 | R7.4.C1 step 7 — TM transition OK. ⚠️ BR-PUBLIC-02 FAIL ở BM (BUG-BM-002). |
| BM-026 | UC94 | Công khai TM rỗng → ERR-CK-01 | Workflow | ⚠️ 🔁 | R7.4.C1 step 4 — BE 409 ERR-CK-01 PASS, UI silent (BUG-BM-005). |
| BM-041 | UC95 | Switch công khai OFF mặc định, 3 trường ẩn | Happy | ⏳ | R7: 🚫 BUG-BM-001. **R8 lần 3 (2026-05-09): UNBLOCKED — Switch added.** Pending re-test R8 lần 4. |
| BM-042 | UC95 | Bật Switch → 3 trường hiện + auto-fill `thoi_gian_dang_tai` | Workflow | ⏳ | R7: 🚫 BUG-BM-001. **R8 lần 3: UNBLOCKED.** BR-PUBLIC-03 BE OK (R7.4.C1 step 6). Pending re-test R8 lần 4. |
| BM-045 | UC95 | Bản ghi AN/HUY → bật Switch reject `ERR-PUBLIC-01` | Negative | ⏳ | R7: 🚫 BUG-BM-001. **R8 lần 3: UNBLOCKED.** Pending re-test R8 lần 4. |
| BM-046 | UC95 | Cột "Đã công khai" badge xanh + tooltip `thoi_gian_dang_tai` | Happy | ⏳ | R7: 🚫 BUG-BM-001. **R8 lần 3: UNBLOCKED.** Pending re-test R8 lần 4. |

### 2.2 P1 — CRUD nâng cao + Filter + Authorization (28 TC)

| TC ID | UC | Tên | Type | Status | Note |
|-------|-----|-----|------|:-:|------|
| BM-006 | UC93 | Search TM theo lĩnh vực + ngày | Happy | ✅ | Filter `?linhVucId=SHTT` → 2 records. `?search=Test` → 1. UI param: `search` (BE alias `keyword`/`tenThuMuc` không hoạt động — observation). |
| BM-007 | UC95 | Preview online doc/docx → PDF | Happy | ❌ | BUG-BM-007 — modal hiện "Không kết nối được máy chủ" do MinIO localhost. |
| BM-009 | UC92 | Sửa TM (tên/lĩnh vực/mô tả/thứ tự) | Happy | ✅ | PATCH với `version: 1` → 200, version increment to 2 (optimistic concurrency). |
| BM-010 | UC95 | Sửa BM + upload file mới | Happy | ⏭ | Defer (BM-007/008 broken trước nên không verify được file replacement có thực sự thay file mới hay không). |
| BM-011 | UC92 | Xuất Excel TM | Happy | ✅ | POST `/thu-muc-bieu-maus/export` 200, `application/vnd.openxmlformats-officedocument.spreadsheetml.sheet`, 7134B, filename `thu-muc-bieu-mau-{ts}.xlsx`. |
| BM-013 | UC92 | TM tên trống/whitespace | Negative | ✅ | 422 + msg "Tên thư mục không được chỉ chứa khoảng trắng" |
| BM-017 | UC92 | Xóa TM có ≥1 BM | Negative | ✅ | DELETE TM SHTT (1 BM) → 409 `ERR-TM-02` "Thư mục chứa 1 biểu mẫu, không thể xóa" |
| BM-018 | UC92 | Tên TM >500 ký tự | Negative | ⚠️ | 422 "tenThuMuc must be shorter than or equal to 500 characters" — message English, spec yêu cầu `ERR-TM-03` "Tên thư mục tối đa 500 ký tự" |
| BM-019 | UC95 | Tên BM trống | Negative | ⚠️ | 422 nhưng error "thuMucId must be a UUID" hit trước — BE order validation khác spec ERR-BM-03. |
| BM-020 | UC93 | tu_ngay > den_ngay | Negative | ✅ | 400 `ERR-TK-01` "Ngày bắt đầu phải trước ngày kết thúc" (match spec) |
| BM-021 | UC95 | Tạo BM không chọn TM | Negative | ⚠️ | 422 "thuMucId must be a UUID" — English msg, spec yêu cầu `ERR-BM-05`. |
| BM-024 | UC94 | Công khai lại AN→CONG_KHAI | Workflow | ✅ 🔁 | R7.4.C1 step 8 PASS. |
| BM-025 | UC92 | Xóa TM rỗng NHAP | Workflow | ✅ | DELETE `/thu-muc-bieu-maus/{id}` 204 (TM Test BM-002 đã xóa). |
| BM-027 | UC92 | Xóa TM rỗng AN | Workflow | ✅ | DELETE TM SHTT (sau khi xóa BM bên trong) 204. List còn 3 TM. |
| BM-028 | UC97 | Import hàng loạt ≤50 file hợp lệ | Workflow | 🔁 | **R7.7.10b** — Wizard `/bieu-mau/nhap-hang-loat` 3 step verified accessible (Chọn file → Kiểm tra → Hoàn thành; combobox Thư mục đích + multi-file dropzone .doc/.docx/.xls/.xlsx 20MB/file 50 file/lần). DEFER tool block: MCP `upload_file` incompatible với custom dropzone. Cần real browser. |
| BM-029 | UC97 | Import mixed valid+invalid | Workflow | 🔁 | **R7.7.10b** — Same tool block as BM-028. |
| BM-032 | — | QTHT R only, không C/U/D/Publish | Authorization | ✅ | **R7.7.10b** — `qtht_01` thấy 7 TM (cross-unit, all scope), KHÔNG có button Thêm thư mục/Sửa/Xóa/Công khai trên list view. `evaluate_script` confirm: `headerActions=["Xóa bộ lọc"]` only, `rowActionLinks=[]`. Match permission-matrix line 75-76 QTHT `BIEU_MAU 👁️ R`. Screenshot: [bm-032-qtht-r-only-no-action-buttons.png](screenshots-r7-7-10b/bm-032-qtht-r-only-no-action-buttons.png). |
| BM-033 | — | CB NV BN không thấy TM của BN khác | Authorization | ✅ | **R7.7.10b** — Isolation 2 chiều confirmed: `cb_nv_bn_01` (BKH) tạo TM `6ad5bf52` Doanh nghiệp → "Tất cả (1)"; logout + login `cb_nv_bn_02` (BTC) → "Tất cả (0)" KHÔNG thấy TM BKH; tạo TM `65471c03` Thuế → "Tất cả (1)". |
| BM-034 | — | CB NV ĐP scope đơn vị | Authorization | ✅ | **R7.7.10b** — Isolation 2 chiều confirmed: `cb_nv_dp_01` (STP-AG) tạo TM `11fe7276` Hành chính → "Tất cả (1)"; `cb_nv_dp_02` (STP-BG) → "Tất cả (0)" KHÔNG thấy AG/BN/TW. Screenshot: [bm-034-dp02-bg-empty-isolation.png](screenshots-r7-7-10b/bm-034-dp02-bg-empty-isolation.png). |
| BM-035 | — | NHT/TVV/CG không thấy menu | Authorization | ⚠️ | **R7.7.10b** — Spec test case OUTDATED. Per [permission-matrix line 534](../../../../permission-matrix.md): NHT có `BIEU_MAU 👁️ R` → menu render đúng spec (R-only, scope đơn vị); CG (line 566-578 không entry FR-09) — `dinh_14` sidebar 2 menu (Đào tạo + Tư vấn) KHÔNG có menu BM + URL `/bieu-mau/thu-muc` route guard redirect về `/dao-tao`. TVV `vu_sau_06`/`tvv_r11_a16` → defer pwd unknown (TVV password set qua mail flow, không có trong fixture). Screenshots: [bm-035-nht-r-only-1tm.png](screenshots-r7-7-10b/bm-035-nht-r-only-1tm.png), [bm-035-cg-no-menu-bm.png](screenshots-r7-7-10b/bm-035-cg-no-menu-bm.png). Sub-finding: NHT scope appears own-unit despite `R` no asterisk → BA confirm. |
| BM-036 | — | DN không truy cập CMS, chỉ qua API Cổng | Authorization | ⏭ | Defer — DN flow ngoài scope CMS (DN dùng portal Cổng PLQG). |
| BM-038 | UC98 | API GET /api/v1/bieu-mau (JWT) trả `cong_khai=1` | Cross-module | ⏭ | Defer — cần JWT mTLS Postman setup ngoài scope MCP. |
| BM-039 | — | Lĩnh vực PL từ DANH_MUC | Cross-module | ✅ | Cover trong BM-002/006 (đã verify select Lĩnh vực hoạt động). |
| BM-040 | — | Audit log CRUD + PUBLISH/UNPUBLISH | Cross-module | ✅ | **R7.7.10b** — `qtht_01` GET `/audit-logs?entityType=BIEU_MAU` → 20 entries (DOWNLOAD:14 + CREATE:5 + DELETE:1); `?entityType=THU_MUC_BIEU_MAU` → 37 entries (CREATE:16 + DELETE:8 + UNPUBLISH:5 + PUBLISH:6 + UPDATE:1 + EXPORT:1). Cover 5/5 SRS actions. Sample CREATE `entityId=11fe7276-...` match TM AG vừa tạo. `cb_nv_tw_01` cùng query → 403 ERR-PERM-SYS-00-01 → ACL QTHT-only đúng spec. |
| BM-043 | UC95 | Tắt Switch công khai → clear `thoi_gian_dang_tai` + gỡ Cổng | Workflow | ⏳ | R7: 🚫 BUG-BM-001 + BUG-BM-002. **R8 lần 3: BUG-BM-001 closed**, BUG-BM-002 vẫn Open → re-test còn phụ thuộc BR-PUBLIC-02 fix. |
| BM-044 | UC95 | `thoi_gian_dang_tai` read-only | Negative | ⏳ | R7: 🚫 BUG-BM-001. **R8 lần 3: UNBLOCKED.** Pending re-test R8 lần 4. |
| BM-047 | UC95 | Cột "Ảnh đại diện" thumbnail | Happy | ⏳ | R7: 🚫 BUG-BM-001. **R8 lần 3: UNBLOCKED.** Pending re-test R8 lần 4. |
| BM-048 | UC95 | Upload `anh_dai_dien` jpg/png/gif ≤5MB | Negative | ⏳ | R7: 🚫 BUG-BM-001. **R8 lần 3: UNBLOCKED.** Pending re-test R8 lần 4. |
| BM-049 | UC95 | Upload nhiều `file_dinh_kem_cong_khai` | Happy | ⏳ | R7: 🚫 BUG-BM-001 + BUG-BM-004 (entity). **R8 lần 3: BUG-BM-001 closed**, BUG-BM-004 entity status chưa verify → re-test conditional. |
| BM-050 | UC95 | `mo_ta_cong_khai` tách biệt với `mo_ta` nội bộ | Happy | ⏳ | R7: 🚫 BUG-BM-001 + BUG-BM-004. **R8 lần 3: BUG-BM-001 closed**, BUG-BM-004 chưa verify → re-test conditional. |

---

## 3. Observations (out-of-SRS, không log thành bug)

> 2 quan sát quá generic không gắn được clause SRS cụ thể — note ở đây để team backend xem xét.

1. **English error message leak** — Validation errors trong tình huống generic (Class-validator default) trả tiếng Anh: `"thuMucId must be a UUID"`, `"tenThuMuc must be shorter than or equal to 500 characters"`. SRS không có clause "all error messages must be Vietnamese" cụ thể, nhưng các module khác (Hỏi đáp, Vụ việc) trả tiếng Việt → consistency issue. Spec ERR-TM-03 tiếng Việt nhưng không match BE response.
2. **Search param naming mismatch** — Spec FR-VII-02 dùng `keyword`. FE thực tế gửi `search`, BE chỉ accept `search` (các tên `keyword`/`q`/`tenThuMuc` BE bỏ qua, vẫn trả full list). Spec docs cần update để khớp implementation, hoặc BE phải accept `keyword` để khớp spec.

---

## 4. Test Data Used

### Tài khoản
- Primary: `cb_nv_tw_01` (CB NV TW, BTP-TW, role `CB_NV_TW`)
- **R7.7.10b multi-account:** `qtht_01` (QTHT R-only verify) · `cb_nv_bn_01` (BKH) + `cb_nv_bn_02` (BTC) (BN isolation 2 chiều) · `cb_nv_dp_01` (STP-AG) + `cb_nv_dp_02` (STP-BG) (ĐP scope 2 chiều) · `nht_01` (Phùng Thị NHT An Giang — NHT R menu verify) · `dinh_14` (Đinh Văn Mười Bốn — CG no-menu verify)
- TVV defer: `vu_sau_06`/`tvv_r11_a16` Secret@123 fail (password do user tự set qua mail flow, không có trong fixture)

### TM seeded/tested
- 4 TM gốc từ R7.3.7 (Biểu mẫu SHTT / Biểu mẫu Thuế / HĐ Dân sự - Thương mại / HĐ Lao động)
- 1 TM tạo mới R7.7.10: `TM Test R7.7.10 BM-002` (id `58a429a8-...`) — sửa thành `TM Test BM-002 (sua)` — đã xóa.
- 1 TM xóa cuối: `Biểu mẫu SHTT` (sau khi xóa BM bên trong, ở state AN) — verify BM-027 PASS.
- **R7.7.10b cross-unit seed (3 TM mới):**
  - `Biểu mẫu BKH - R7.7.10b` (id `6ad5bf52-8865-4c52-a415-96a8f7d2e428`, Doanh nghiệp, NHAP, owner `cb_nv_bn_01`)
  - `Biểu mẫu BTC - R7.7.10b` (id `65471c03-d3ac-4ff5-a2ab-b279dd5e5727`, Thuế, NHAP, owner `cb_nv_bn_02`)
  - `Biểu mẫu STP-AG - R7.7.10b` (id `11fe7276-f3b1-4f0d-93ab-3ab5e84bee6b`, Hành chính, NHAP, owner `cb_nv_dp_01`)
- **Cuối session R7.7.10b:** 7 TM total (4 BTP-TW gốc + 3 cross-unit R7.7.10b). Pool tăng 4→7. Giữ lại làm seed cho R7.7.10c bulk import test.

### BM seeded/tested
- 1 BM tạo R7.4.C1: `BM-20260507-001` "Biểu mẫu SHTT - test R7.4.C1" file `test-bm-r7-4-c1.docx` 917B.
- BM đã được dùng cho: SM transitions (R7.4.C1), BM-007 preview (broken), BM-008 download (broken), BM-012 chi tiết, BM-005 search.
- **Cuối session:** BM đã xóa (DELETE 204) để clean BM-027 test.

### File test artifacts (`output/qa-reports/round7-2026-05-06/workflow/`)
- `test-bm-r7-4-c1.docx` 917B — minimal DOCX hợp lệ (Python zip).
- `test-bm-invalid.txt` 36B — file `.txt` để test BM-016 silent reject.

---

## 5. Bug Linkage

**File 1 — R7.4.C1 workflow bugs:** [`bug-report-flow-bm-r7-4-c1.md`](../../bug-reports/bm/bug-report-flow-bm-r7-4-c1.md) (6 bugs)

| Bug ID | Severity | Status | TC chặn |
|--------|----------|--------|---------|
| BUG-BM-001 | Critical | ✅ Closed R8 lần 3 (2026-05-09) | BM-041..050 (10 TC) — 7 unblocked, 3 conditional (BM-043/049/050 chờ BUG-BM-002/004) |
| BUG-BM-002 | Critical | Open | BM-043 (cascade) |
| BUG-BM-003 | Major | Open | Tất cả TC kiểm tra response (entity field rename pending) |
| BUG-BM-004 | Major | Open (chưa verify R8) | BM-049, 050 (entity thiếu 3 fields) |
| BUG-BM-005 | Medium | Open | BM-026 UI feedback |
| BUG-BM-006 | Medium | Open | BM-001 cột counter |

**File 2 — R7.7.10 functional bugs:** [`bug-report-function-bm-r7-7-10.md`](../../bug-reports/bm/bug-report-function-bm-r7-7-10.md) (2 bugs)

| Bug ID | Severity | TC chặn |
|--------|----------|---------|
| BUG-BM-007 | Critical | BM-007, BM-008 (preview + download) |
| BUG-BM-008 | Medium | BM-016 (silent reject upload) |

**File 3 — R7.7.10b functional bugs:** [`bug-report-r7-7-10b-bm.md`](../../bug-reports/bm/bug-report-r7-7-10b-bm.md) (1 bug)

| Bug ID | Severity | TC chặn |
|--------|----------|---------|
| BUG-BM-009 | Medium | BM-015 (upload >20MB ERR_CONNECTION_RESET + session invalidate, no graceful 413 + Vietnamese error) |

---

## 6. Recommended Next Round

1. **Fix BUG-BM-001** (FE 4 trường công khai): unblock 10 TC CR-01 — BM-041/042/043/044/045/046/047/048/049/050. **(BUG-BM-001 đã closed R8 lần 3 — chờ test riêng 10 TC)**
2. **Fix BUG-BM-002** (BE BR-PUBLIC-02): unblock BM-043 cascade.
3. **Fix BUG-BM-007** (MinIO localhost config): unblock BM-007 + BM-008 + BM-010.
4. **Fix BUG-BM-009** (R7.7.10b — upload >20MB graceful 413 + Vietnamese error + session preserve): unblock BM-015 PASS clean.
5. **Round R7.7.10b — DONE 2026-05-10** ✅: unblocked 6 TC (BM-032/033/034/040 ✅ PASS + BM-039 implicit ✅ + BM-015/035 ⚠️ PARTIAL); BM-028/029 deferred do MCP tool block; BM-035 sub-defer TVV pwd → see [`functional-test-report-r7-7-10b-bm.md`](functional-test-report-r7-7-10b-bm.md) + [`bug-report-r7-7-10b-bm.md`](../../bug-reports/bm/bug-report-r7-7-10b-bm.md). Pass rate **49%** PASS only (23/47) hoặc **62%** PASS+PARTIAL (29/47).
6. **Round R7.7.10c** (next):
   - Real browser test (Playwright/manual) BM-028/029 bulk import — workaround MCP `upload_file` incompatible custom dropzone.
   - TVV password discovery hoặc tạo TVV mới với fixture password → BM-035b sub-defer.
   - Postman run BM-038 (API mTLS Cổng PLQG).
   - Re-run 10 CR-01 TC sau BUG-BM-001 closed.
   - Re-run BM-007/008/010 sau MinIO fix.
   - BA confirm NHT scope intent (own-unit vs read-all per permission-matrix line 534).
7. **Reseed pre-round**: 3 TM cross-unit R7.7.10b (BKH/BTC/STP-AG) đã có sẵn để re-use cho R7.7.10c. Pool TM hiện 7 (4 BTP-TW + 3 cross-unit).

---

*Functional report generated: 2026-05-07 19:00 (UTC+7) | Updated R7.7.10b: 2026-05-10 16:55 (UTC+7) | QA Automation via Claude Code MCP*
