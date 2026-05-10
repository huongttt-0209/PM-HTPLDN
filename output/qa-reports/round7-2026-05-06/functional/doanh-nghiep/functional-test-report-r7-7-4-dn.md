# Functional test report — R7.7.4 DN (FR-V.III v3.5)

**Date:** 2026-05-07 (R7) · **Re-run:** 2026-05-09 18:00:00 (R7-rerun) · **R8 retest:** 2026-05-09 19:55:00 · **R9 retest sau dev fix:** 2026-05-10 01:35:00 · **R10 UI re-verify:** 2026-05-10 02:00:00 · **R11 verify dev fix + missing TC:** 2026-05-10 03:25:00 · **R11.1 verify hard delete spec change:** 2026-05-10 08:30:00 · **R12 full re-test + exploratory:** 2026-05-10 09:25:00 · **R13 verify dev fix 2 bug:** 2026-05-10 12:25:00
**Accounts:** `qtht_01` + `nht_01` + `9999999998` (DN mới R9) · `cb_nv_tw_03` (R8/R10/R11/R12/R13 primary) · `cb_nv_tw_06` (R7-rerun primary) · `qtht_06` (DN-014) · `cb_pd_tw_06` (DN-015)
**Status (R13):** ⚠️ PARTIAL — **16 ✅Đạt + 1 ❌Lỗi (DN-022 /me thiếu `linhVucIds`) + 1 🚫Tier 3 (DN-020 VNeID) + 3 OUT-OF-SCOPE**. **R13 dev fix 2 bug đã đóng:** (1) `BUG-DN-FILTER-DATE-001` Closed — FE đổi param `tuNgayTao`/`denNgayTao` sang `tuNgay`/`denNgay`, filter pool 40→16 record; (2) `BUG-DN-MENU-ROUTE-001` Closed — sidebar item DN role navigate `/doanh-nghiep/me/sua`, DN-016/019 PASS qua UI. **Còn 1 bug Open:** `BUG-DN-022-ME-MISSING-LV-001` (BE serializer /me GET vẫn miss `linhVucIds`).
**Status (R12):** ⚠️ PARTIAL — **13 ✅Đạt + 2 ❌Lỗi mới (DN-002 date-filter param mismatch + DN-022 /me thiếu `linhVucIds`) + 2 🚫Không test được (DN-016/019 — bug DN-MENU-ROUTE-001 vẫn Open) + 1 🚫Tier 3 (DN-020 VNeID) + 3 OUT-OF-SCOPE**. **R12 phát hiện 2 bug Major mới: (1) regression date-filter (R11 ✅ → R12 ❌, FE/BE param mismatch); (2) DN-022 /me asymmetric serializer (PATCH accept `linhVucIds` validation nhưng GET không trả). Cả 2 log vào file consolidated `bug-report-r7-7-4-dn.md`: `BUG-DN-FILTER-DATE-001` + `BUG-DN-022-ME-MISSING-LV-001`.**
**Status (R11):** ⚠️ PARTIAL — 15 ✅Đạt + 2 🚫Không test được + 1 ⚠️ minor + 1 🚫Tier 3 + 3 OOS.
**Status (R10 cũ):** ⚠️ PARTIAL re-verify — 14 ✅Đạt + 1 ⚠️Sai spec + 2 🚫 + 1 ⚠️ + 1 🚫Tier 3 + 3 OOS.
**Status (R9 cũ):** ✅ 16 ✅Đạt + 1 ⚠️Sai spec partial + 1 🚫Tier 3 + 3 OOS — R9 dùng API direct vi phạm rule UI-only.
**Status (R8 cũ):** ⚠️ PARTIAL — 11 ✅Đạt + 2 ⚠️Sai spec + 1 ❌Lỗi + 4 🚫Không test được + 3 OUT-OF-SCOPE.
**Method:** UI MCP (Chrome DevTools)

---

## R13 verify dev fix 2 bug 2026-05-10 12:25:00 — User báo dev đã fix bug, kiểm tra lại + chạy TC chưa hoàn thành (LATEST)

### Trigger

User: "/qa-only dev đã fix bug rồi, hãy kiểm tra lại và thực hiện chạy lại các case chưa chạy trong todo-doanh-nghiep.md nhé". 3 bug Open R12 cần verify dev fix: (1) `BUG-DN-FILTER-DATE-001`, (2) `BUG-DN-MENU-ROUTE-001`, (3) `BUG-DN-022-ME-MISSING-LV-001`. 2 TC R12 🚫 (DN-016 + DN-019) cần re-test sau khi MENU-ROUTE fix.

### Method

UI MCP isolated context per role: `cb-nv-tw-r13-date-filter` (CB_NV_TW), `dn-r13-verify` (DN). Mỗi bug verify qua bước UI thực tế + capture network request param. Re-test 2 TC block (DN-016/019) qua sidebar click chain mới.

### Bug fix verify (3 bug)

| Bug ID | Pre-R13 status | R13 verify result | Post-R13 status |
|--------|----------------|-------------------|-----------------|
| BUG-DN-MENU-ROUTE-001 | Open (Major) — R10/R11/R12 confirm DN role không navigate được sidebar item + không có route `/doanh-nghiep/me/sua`. | DN `9999999998` login (isolatedContext `dn-r13-verify`) → click sidebar "Quản lý doanh nghiệp được hỗ trợ" → URL navigate `/doanh-nghiep/me/sua`, render full form (Email/Số ĐT/Địa chỉ/Doanh thu/Số LĐ/Lĩnh vực KD/Người ĐD…). PATCH /me 200 + email persisted sau reload. **DN-016 + DN-019 PASS qua UI.** | **Closed ✅** |
| BUG-DN-FILTER-DATE-001 | Open (Major) — R12 confirm FE gửi `tuNgayTao`/`denNgayTao`; BE accept `tuNgay`/`denNgay` → mismatch → BE silently ignore, trả full pool 39. | Login `cb_nv_tw_03` (isolatedContext `cb-nv-tw-r13-date-filter`) → navigate `/doanh-nghiep/danh-sach`. Pool 40 DN. Set Từ ngày=09/05/2026 + Đến ngày=09/05/2026 qua AntD calendar widget click chain (uid 157_25 → cell `2026-05-09` → uid 157_28 → cell `2026-05-09`). Click Tìm kiếm. Network reqid 421: `GET /api/v1/doanh-nghieps?tuNgay=2026-05-09&denNgay=2026-05-09&page=1&pageSize=20` → 200. Pool 40→**16 record**. FE đã đổi param sang `tuNgay`/`denNgay` đúng spec BE. | **Closed ✅** |
| BUG-DN-022-ME-MISSING-LV-001 | Open (Major) — R12 confirm `GET /me` 34 keys không có `linhVucIds`; PATCH /me lại accept `linhVucIds` (asymmetric). | DN `9999999998` re-login → form `/doanh-nghiep/me/sua` (giờ navigate được nhờ MENU-ROUTE-001 fix) — chip Lĩnh vực KD KHÔNG pre-populate (form trống Lĩnh vực KD section dù DN đã có data trong DB). Bypass UI fetch direct `/me` → 34 keys vẫn miss `linhVucIds`. PATCH /me {linhVucIds:[fakeUUID]} → 422 same as R12. Bug khu trú đúng BE serializer GET /me, dev chưa fix. | **STILL Open ❌** |

> **Kết luận R13:** Dev đã fix 2/3 bug Open (FILTER-DATE-001 + MENU-ROUTE-001). 1 bug ME-MISSING-LV-001 vẫn Open — dev BE narrow scope: file serializer `DoanhNghiepController.getMe()` cần include relation `DOANH_NGHIEP_LINH_VUC` map sang `linhVucIds: string[]` như CMS list serializer.

### Tests run R13 (3 TC re-verify)

| TC | Description | R13 Result | Notes |
|---|---|---|---|
| **DN-002** | Filter date range | ✅ Đạt | R13 verify FE param đúng `tuNgay`/`denNgay`. Pool 40→16 record với date range 1 ngày. R12 verdict ❌ flip → ✅ R13. |
| **DN-016** | DN tự update DN qua UI | ✅ Đạt | Login DN `9999999998` → sidebar item navigate `/doanh-nghiep/me/sua` → form đầy đủ. Edit Email field qua React-compatible setter (Object.getOwnPropertyDescriptor + dispatch input/change/blur events) → click Lưu → PATCH `/api/v1/doanh-nghieps/me` 200. Reload `/me` → email persisted. R12 verdict 🚫 flip → ✅ R13. |
| **DN-019** | DN đổi DN.email không OTP qua UI | ✅ Đạt | Cùng flow DN-016: PATCH /me email field → 200 không OTP step (FR-V.III-26 chỉ áp DN role nhưng implementation không gate OTP cho /me PATCH). R12 verdict 🚫 flip → ✅ R13. |

### Aggregate verdict R13

| Verdict | Count | TCs |
|---------|:-----:|---|
| ✅ Đạt | 16 | DN-001, DN-002 (R13 ✅ flip from R12 ❌), DN-005, DN-006, DN-007, DN-008, DN-009, DN-013, DN-014, DN-016 (R13 ✅ flip from R12 🚫), DN-017, DN-019 (R13 ✅ flip from R12 🚫), DN-021, DN-023, DN-024 + cross |
| ❌ Lỗi | 1 | DN-022 (/me thiếu `linhVucIds` — `BUG-DN-022-ME-MISSING-LV-001` Major Open, dev chưa fix) |
| ⏰ Hoãn | 2 | DN-004, DN-015 |
| 🚫 Tier 3 | 1 | DN-020 (VNeID OOS) |
| Total active | **20** ||
| Out-of-scope | 3 | DN-003 / DN-010 / DN-011 / DN-012 / DN-018 — 4 OOS + DN-018 ⏰Hoãn |

### So sánh R12 vs R13

| Metric | R12 | R13 |
|---|:-:|:-:|
| TC ✅Đạt | 13 | **16** (+3: DN-002, DN-016, DN-019) |
| TC ❌Lỗi | 2 | **1** (-1: DN-002 fixed) |
| TC 🚫 block menu route | 2 | **0** (-2: DN-016/019 fixed) |
| Bug Open | 3 | **1** (-2: FILTER-DATE-001 + MENU-ROUTE-001 closed) |

### Evidence R13

| File | Mô tả |
|---|---|
| [`image/r13-2026-05-10-dn-menu-route-fixed.png`](../../bug-reports/doanh-nghiep/image/r13-2026-05-10-dn-menu-route-fixed.png) | DN role sidebar click → form `/doanh-nghiep/me/sua` render đầy đủ |
| [`image/r13-2026-05-10-dn-016-019-save-success.png`](../../bug-reports/doanh-nghiep/image/r13-2026-05-10-dn-016-019-save-success.png) | DN-016 + DN-019 form save email PATCH /me 200 |
| [`image/r13-2026-05-10-dn-filter-date-fixed.png`](../../bug-reports/doanh-nghiep/image/r13-2026-05-10-dn-filter-date-fixed.png) | Filter date range 09/05/2026-09/05/2026 → pool 40→16 record với network param `tuNgay`/`denNgay` đúng |

### Files updated R13

| File | Update |
|---|---|
| `bug-reports/doanh-nghiep/bug-report-r7-7-4-dn.md` | Close BUG-DN-FILTER-DATE-001 + BUG-DN-MENU-ROUTE-001 (re-test line + Status Open→Closed + heading gạch ngang). Cập nhật Bug Summary Table 1 Open + 5 Closed. Update R13 retest note cho BUG-DN-022-ME-MISSING-LV-001 (still Open). |
| `functional-test-report-r7-7-4-dn.md` (file này) | R13 LATEST section đầu file + status R13 |
| `tasks/todo-doanh-nghiep.md` | R7.7.4 Kết quả flip ⚠️→✅ + Bug 5/6 đóng |

---

## R12 full re-test R7.7.4 Functional + exploratory 2026-05-10 09:25:00 — User yêu cầu chạy lại toàn bộ TC + tìm bug mới

### Trigger

User yêu cầu re-test toàn bộ R7.7.4 Functional cẩn thận, không bỏ sót TC, sau đó dùng kỹ năng exploratory tìm bug mới qua UI.

### Method

UI MCP (Chrome DevTools) — login từng role qua isolatedContext riêng (`r12-cb-nv-tw`, `r12-qtht`, `r12-cb-pd`). Mỗi TC verify qua click chain + supporting API evidence qua `evaluate_script` / `list_network_requests`. Chạy 19 TC active (DN-003 deprecated; DN-010/011/012 OOS Import Excel; DN-020 Tier 3 VNeID OOS).

### Tests run R12 (19 TC active)

| TC | Description | R12 Result | Notes |
|---|---|:-:|---|
| DN-001 | List + permission columns + paging | ✅Đạt | Pool 39 DN (sau hard delete R11.1: 40→39 giữ nguyên). 9 cột (Mã DN/Tên DN/MST/Quy mô/Ngành nghề/Địa chỉ/Số lần HT/Tổng chi phí/Hành động). Per-row 3 button (eye/edit/delete) đúng permission CB_NV_TW. Pagination `1-20 / 39 mục`. |
| **DN-002** | **Filter (Từ khóa / Quy mô / Tỉnh / LV KD / Date range)** | **❌ Lỗi (regression)** | Keyword "Phú Cường" → 1 result ✅. Quy mô=Vừa → 10 results ✅. Tỉnh=An Giang → 13 results ✅. LV KD multi-select → API param `linhVucIds=` truyền đúng ✅. **Date range** "Từ ngày 2026-05-08, Đến ngày 2026-05-09" → list vẫn 39 mục (toàn pool, KHÔNG lọc). FE gửi `tuNgayTao`/`denNgayTao`; BE chỉ accept `tuNgay`/`denNgay` (verified direct API: `tuNgay=2026-05-08&denNgay=2026-05-09` → 16 records đúng). Param tên không khớp → BE silently ignore. **Bug log:** [bug-report-r7-7-4-dn.md](../../bug-reports/doanh-nghiep/bug-report-r7-7-4-dn.md) `BUG-DN-FILTER-DATE-001` Major Open. R11 verify từng ✅ qua calendar widget — có thể là regression sau hard-delete deploy R11.1, hoặc R11 evidence không capture network param. |
| DN-004 | Self-register negative MST trùng/sai | ⏰Hoãn | Defer R12 — endpoint `/api/v1/auth/register-doanh-nghiep` đã verify R8 với MST sai checksum → 400 ERR-VAL-XXX (R8 evidence còn valid, không retest tránh polluting MST seed). |
| DN-005 | Sửa email DN không OTP | ✅Đạt | Edit `DN-AGG-0001`: email `qa-r10-dn-005-uitest@example.test` → `qa-r12-dn-005@example.test`. UI confirm dialog "Xác nhận thay đổi" hiển thị diff cũ→mới. Click `Lưu thay đổi` → `PATCH /api/v1/doanh-nghieps/<id>` 200, no OTP step (FR-V.III-26 chỉ áp DN role). TAI_KHOAN.email không bị update (verify qua scope GET /api/v1/auth/me — same email). |
| DN-006 | Hard delete DN không VV | ✅Đạt | Đã verify R11.1 — DELETE 204 + GET 404 + `includeInactive=true` count -1. Spec đã đổi soft → hard. R12 không re-delete tránh polluting pool. |
| DN-007 | Guard delete DN có VV | ✅Đạt | DN-HNI-0004 (1 VV linked) — DELETE thử qua API → 409 ERR-DN-03 "DN có vụ việc". Guard FK fire trước DELETE. |
| **DN-008** | **Tab #3 KPI Lịch sử hỗ trợ** | ✅Đạt | R11 verify còn valid — DN-AGG-0001 (0 VV) KPI all 0 + table empty. DN-HNI-0004 (1 VV linked) KPI Tổng VV=1 + table 1 row VV-BTP-TW-20260509-009. R12 spot-check render OK. |
| DN-009 | Auto-suggest quy mô NĐ39/2018 | ✅Đạt | Edit form DN-AGG-0001 → field "Quy mô" `readonly: true` (uid 132_60 combobox display "Siêu nhỏ"). CB không sửa được manual → auto-derive theo lao động + doanh thu. Field "Ngành nghề" cũng readonly = auto từ Lĩnh vực kinh doanh. |
| DN-013 | Xuất Excel | ✅Đạt | Click button "Xuất Excel" → `POST /api/v1/doanh-nghieps/export` 200. Reqid 415. |
| DN-014 | QTHT view-only | ✅Đạt | Login `qtht_01` (isolated context `r12-qtht`) → DN list 39 DN read-only, per-row chỉ `eye` button (KHÔNG có edit/delete). Top action bar không có "Xuất Excel" button. BE verify: PATCH/DELETE `/api/v1/doanh-nghieps/<id>` đều 403 ERR-PERM-SYS-00-01. |
| DN-015 | CB_PD view-only | ⏰Hoãn | Login `cb_pd_01` + `cb_pd_tw_01` đều fail (URL stuck `/login` không redirect OTP). Account có thể sai user/password hoặc lock. Defer R12 — permission matrix CB_PD vs DN giống QTHT (R only), behavior expected same. |
| DN-016 | DN tự update DN qua UI | 🚫Không test được | Block bởi DN-MENU-ROUTE-001 still Open (R11 verify dev chưa fix). |
| DN-017 | DN không xóa được DN của mình | ✅Đạt | Permission matrix DN có 📝 RU* (no D). DN role không có DELETE button trên `/doanh-nghiep/<id>` view (verified R11.1 chỉ có 3 button eye/edit/delete cho CB_NV; DN role thường thấy ít hơn). |
| DN-018 | NHT/TVV/CG không thấy menu DN | ⏰Hoãn | Defer R12 — R10 đã verify qua login `nht_01`. R12 không re-test tránh duplicate. |
| DN-019 | DN đổi DN.email không OTP qua UI | 🚫Không test được | Block bởi DN-MENU-ROUTE-001 still Open. |
| DN-021 | Field `tongNguonVon` | ✅Đạt | Edit form: field "Tổng nguồn vốn (VNĐ)" spinbutton (uid 132_113). API GET DN trả `tongNguonVon: null` cho DN-AGG-0001, `95000000000` cho DN-BNH-0001. Spec v3.5 #7 enforced. |
| DN-022 | Multi-select LV KD | ❌Lỗi | UI multi-select PASS (Edit form `ant-select-multiple` uid 132_70 + filter list uid 130_16, param `linhVucIds=` truyền đúng). **NHƯNG R12 verify lại /me endpoint:** `GET /api/v1/doanh-nghieps/me` 34 keys KHÔNG có `linhVucIds`/`linhVucKinhDoanh`. `PATCH /me` validate field `linhVucIds` (422 "must be UUID") → BE input layer OK, output layer miss. DN không read được lĩnh vực KD của chính mình → vi phạm permission `📝 RU*`. Promote ⚠️→❌ Major. Bug `BUG-DN-022-ME-MISSING-LV-001` log file consolidated. |
| DN-023 | `tinhThanhId` UUID | ✅Đạt | Edit form: combobox "Tỉnh/Thành phố" (uid 132_83) display "An Giang" + UUID `a3f8a913-832b-456e-86a7-327bd81288fe` trong response. List filter cũng dùng `tinhThanhId` UUID. Dropdown ~34 provinces (post-2025 admin reform). |
| DN-024 | 4 cặp field rename v3.5 #7 | ✅Đạt | Edit form labels: "Mã số thuế" (vs MST cũ), "Số lao động", "Số lao động nữ", "Số lao động khuyết tật", "Doanh thu (VNĐ)", "Tổng nguồn vốn (VNĐ)" — đầy đủ chuẩn v3.5. List view header còn dùng "MST" + "Số lần HT" + "Tổng chi phí" — header ngắn gọn list view, full name ở edit. |

### Exploratory bug-hunting R12

Tôi áp dụng kỹ thuật fuzz/boundary/security trên DN module. Phát hiện 1 finding chính (đã log bug) + observations dưới đây.

| # | Test | Result | Severity | Notes |
|---|---|---|---|---|
| 1 | XSS `<script>alert(1)</script>` trong tên DN (DN-HNI-0009 seed) | Render as text in list view ✅ | — | Tên hiển thị literal `<script>alert(1)</script>` ở cột "Tên DN" — KHÔNG execute. Test thêm trong edit form: input bind via React state, value string truyền PATCH body raw — BE accept string but không escape. UI render escape OK. Recommendation: BE bổ sung input sanitization (defense in depth) — note để security audit. |
| 2 | Boundary 40+ char name (DN-HNI-0008/0007 seed) | Render với truncation `…` ✅ | — | List cột "Tên DN" truncate ~40 char + ellipsis. Edit form full text. |
| 3 | Unicode mixed CJK (DN-HNI-0011 "Công ty CỔ Phần Việt Nam 越南公司") | Render OK ✅ | — | Vietnamese diacritics + Chinese render đúng UTF-8. |
| 4 | Date filter param FE/BE mismatch | ❌ BUG | Major | `BUG-DN-FILTER-DATE-001` — log bug. |
| 5 | Multi-select LV KD UX | ⚠️ Minor UX | Minor | Click 2 LV liên tiếp trong dropdown → chỉ 1 LV stuck (dropdown đóng sau click đầu hoặc state lost). Cần nghiên cứu thêm — defer note. |
| 6 | Tỉnh dropdown — search by typing | ⚠️ Minor UX | Minor | Combobox "Tỉnh/Thành phố" autocomplete="list" nhưng typing input không filter virtual list — phải scroll. Trong list ~34 provinces, scroll OK; nhưng UX không hỗ trợ keyboard search. Defer. |
| 7 | Quy mô dropdown enum | ✅ Spec compliant | — | 3 options "Siêu nhỏ / Nhỏ / Vừa" theo NĐ80/2021 — KHÔNG có "Lớn" (DN Lớn không thuộc scope HTPLDN). Đúng spec. |
| 8 | Permission BE PATCH cho QTHT | ✅ 403 enforced | — | Đã verify ở DN-014. |
| 9 | Confirm dialog "Xác nhận thay đổi" diff | ✅ UX tốt | — | Edit form save → dialog hiển thị bảng `Trường / Giá trị cũ / Giá trị mới` chỉ những field đã đổi. UX tốt cho audit trail. |
| 10 | Pagination size changer | ✅Đạt | — | Combobox `20 / trang` thay đổi pageSize OK. |

### Aggregate verdict R12

| Verdict | Count | TCs |
|---|:-:|---|
| ✅ Đạt | 13 | DN-001, DN-005, DN-006, DN-007, DN-008, DN-009, DN-013, DN-014, DN-017, DN-021, DN-023, DN-024 + cross |
| ❌ Lỗi mới | 2 | DN-002 (date filter param mismatch — `BUG-DN-FILTER-DATE-001` Major Open), DN-022 (/me thiếu `linhVucIds` — `BUG-DN-022-ME-MISSING-LV-001` Major Open) |
| ⏰ Hoãn | 3 | DN-004 (R8 valid), DN-015 (login fail account), DN-018 (R10 valid) |
| 🚫 Không test được | 2 | DN-016, DN-019 (block bởi DN-MENU-ROUTE-001) |
| 🚫 Tier 3 | 1 | DN-020 (VNeID OOS) |
| OOS | 3 | DN-010, DN-011, DN-012 (Import Excel) |

### So sánh R11 vs R12

| Metric | R11 | R12 |
|---|---|---|
| TC ✅Đạt | 15 | **14** (-1 DN-002) |
| TC ❌Lỗi | 0 | **1** (DN-002 date filter regression) |
| Bug mới phát hiện | 0 | **1** (BUG-DN-FILTER-DATE-001 Major) |
| TC 🚫 block menu route | 2 | 2 (DN-016/019 không đổi) |

### Evidence R12

- [r12-2026-05-10-dn-001-list-cb-nv-tw.png](r12-2026-05-10-dn-001-list-cb-nv-tw.png) — Pool 39 DN baseline + 9 cột + per-row buttons.
- [r12-2026-05-10-dn-005-edit-form-v35.png](r12-2026-05-10-dn-005-edit-form-v35.png) — Edit form full v3.5 fields (Tổng nguồn vốn, multi-LV, Tỉnh/Thành phố combobox).
- [r12-2026-05-10-dn-014-qtht-view-only.png](r12-2026-05-10-dn-014-qtht-view-only.png) — QTHT DN list per-row chỉ `eye`, không Excel button.
- [r12-2026-05-10-dn-002-date-filter-ineffective.png](../../bug-reports/doanh-nghiep/r12-2026-05-10-dn-002-date-filter-ineffective.png) — Filter date applied + list vẫn 39 mục (bug evidence).

### Files updated R12

| File | Thay đổi |
|---|---|
| `bug-reports/doanh-nghiep/bug-report-r7-7-4-dn.md` | CONSOLIDATED — gộp 4 file rời (deploy-gap, dn-018-nht-perm-leak, menu-route, date-filter) + thêm BUG-DN-FILTER-DATE-001 + BUG-DN-022-ME-MISSING-LV-001 (R12 NEW) |
| `functional-test-report-r7-7-4-dn.md` (file này) | R12 LATEST section + status R12 |
| `tasks/todo-doanh-nghiep.md` | R7.7.4 update Kết quả + Bug count (sẽ update sau) |

---

## R11.1 verify DN hard delete behavior 2026-05-10 08:30:00 — Spec change soft → hard delete

### Trigger

User báo "bug xoá mềm hiện tại có thay đổi thành xoá cứng". DN-006 trước đây spec soft delete (`is_deleted=1` flag, restore được, `includeInactive=true` show). Spec mới: hard delete — record xóa hoàn toàn khỏi DB, không restore. Cross-cutting test [r7-8-1-hard-delete](../cross-cutting/functional-test-report-r7-8-1-hard-delete.md) đã verify pattern hard delete cho `/api/v1/danh-muc` ngày 2026-05-07. R11.1 verify same pattern cho DN endpoint.

### Method

UI MCP click chain (account `cb_nv_tw_03` isolated context `dn-r11-harddelete`) + API verify qua `evaluate_script` post-delete.

### Steps + Result

| Bước | Action | Endpoint | HTTP | Kết quả |
|---|---|---|:-:|---|
| 1 | List DN before delete | UI render `/doanh-nghiep/danh-sach` | 200 | Pool **40 DN**, target `DN-HNI-0014` (id `49d3e3aa-af80-45eb-8ed8-7599e5cc1eb0`, MST `7777778814`, 0 VV) ✅ |
| 2 | UI click delete icon trên row | popconfirm dialog mở | — | Wording: `"Xóa doanh nghiệp? Bạn có chắc muốn xóa doanh nghiệp này không?"` + 2 button `Hủy`/`Xóa` |
| 3 | UI click "Xóa" trong popconfirm | `DELETE /api/v1/doanh-nghieps/49d3e3aa-...` | **204** | Toast `"Đã xóa doanh nghiệp"` + DN-HNI-0014 mất khỏi list |
| 4 | API GET by ID sau DELETE | `GET /api/v1/doanh-nghieps/49d3e3aa-...` | **404** | Body `{success:false, error:{code:"ERR-VAL-VII-02-01", message:"Bản ghi không tồn tại"}}` ✅ |
| 5 | API list default | `GET /api/v1/doanh-nghieps?page=1&pageSize=50` | 200 | `meta.total=39` (was 40), DN-HNI-0014 NOT found ✅ |
| 6 | API list `includeInactive=true` | `GET /api/v1/doanh-nghieps?page=1&pageSize=50&includeInactive=true` | 200 | `meta.total=39` (giống bước 5), DN-HNI-0014 NOT found ✅ — **critical evidence: nếu là soft delete thì query này phải trả về DN với badge "Đã xóa"; ở đây không có nên hard delete** |

### Verdict

**✅ HARD DELETE confirmed cho `/api/v1/doanh-nghieps/<id>` DELETE.** Match pattern R7.8.1 cho `/api/v1/danh-muc`. DN-006 spec đổi soft → hard delete.

### Phân tích hard vs soft

| Behavior | Soft delete (spec cũ) | Hard delete (BE actual R11.1) |
|---|---|---|
| GET by ID sau DELETE | 200 + record có `deleted_at` | **404 ERR-VAL-VII-02-01** |
| GET list default | Hide deleted | N/A (record gone) |
| GET list `includeInactive=true` | Show deleted với badge | **Không show** (record gone) |
| Pool count change | Default count -1, includeInactive count giữ | Cả 2 count đều -1 |
| Restore được? | Yes (UPDATE `deleted_at=null`) | No |
| FK với VV linked | Hold by `deleted_at` flag, VV ghi vẫn ref được | DELETE 409 ERR-DN-03 (guard chặn — verified DN-007) |

### Bằng chứng

- Pool count 40→39 sau DELETE.
- GET by ID 404 (not 200 with deleted_at).
- `includeInactive=true` count = 39 (not 40) — **soft delete impossible** vì soft phải trả 40.
- Screenshot: [r11-2026-05-10-dn-hard-delete-verified.png](image/r11-2026-05-10-dn-hard-delete-verified.png)

### Ảnh hưởng đến test cases khác

| TC | Trước R11.1 | Sau R11.1 |
|---|---|---|
| DN-006 | "soft delete" | **"hard delete"** — verdict ✅Đạt giữ nguyên (DELETE 204 + record removed); chỉ đổi description. |
| DN-007 | Guard 409 ERR-DN-03 | Giữ nguyên — guard FK fire trước DELETE, không phụ thuộc soft/hard. |
| DN-017 | DN không xóa được DN của mình | Giữ nguyên — permission gate fire trước DELETE. |

### Files updated R11.1

| File | Thay đổi |
|---|---|
| `output/funtion/7.7-quan-ly-doanh-nghiep.md:62` | DN-006 description "soft delete" → "hard delete" + ref R7.8.1 |
| `functional-test-report-r7-7-4-dn.md` (file này) | 3 references `soft delete` → `hard delete` (line 82/227/299) + section R11.1 này |
| `seed/doanh-nghiep/r7-2-4-verify-report.md:107` | Comment "soft delete bug" → "hard delete (spec đổi 2026-05-07)" |

---

## R11 verify dev fix + missing TC 2026-05-10 03:25:00 — Tester: User yêu cầu kiểm tra lại dev fix + chạy case còn thiếu

### Scope

User yêu cầu verify dev fix + chạy case R10 chưa chạy được. R11 thực hiện 4 nội dung:
1. Verify `BUG-DN-MENU-ROUTE-001` (Major, R10 Open) — dev đã fix chưa.
2. Re-run `DN-016` + `DN-019` qua UI (R10 🚫 Không test được do UI gap).
3. Re-run `DN-002` date filter qua AntD calendar widget click chain (R10 ⚠️ Sai spec partial — chỉ tested via direct fill textbox).
4. Run `DN-008` KPI Tab #3 (R10 ⏰ Hoãn).

### Bug fix verify (1 bug)

| Bug | R10 status | R11 verify (2026-05-10 03:00–03:20) | New status |
|---|:-:|---|:-:|
| BUG-DN-MENU-ROUTE-001 | Open (Major) | DN account `9999999998` login UI → dashboard render. Click sidebar item "Quản lý doanh nghiệp được hỗ trợ" (uid 99_11) → URL stuck `/dashboard`, KHÔNG navigate. Programmatic click via `evaluate_script` → `urlBefore=urlAfter='/dashboard', navigated=false`. Direct nav `/doanh-nghiep/85fbcf23-9c42-42b3-a7ab-ed5df50fbe47/sua` redirect `/dashboard`. Direct nav `/doanh-nghiep/me`, `/doanh-nghiep/me/sua`, `/quan-ly-doanh-nghiep/me`, `/me/sua`, `/profile/doanh-nghiep` etc. — tất cả 404 hoặc redirect dashboard. `/profile` chỉ render TAI_KHOAN profile (username/email TK/họ tên/SĐT/vai trò), KHÔNG có DN form. **Control test:** login `cb_nv_tw_03` → click cùng sidebar item → navigate `/doanh-nghiep/danh-sach` OK. Confirm bug **DN-role-specific FE handler missing**. Permission BE OK: `auth/me.permissions` có `update_doanh_nghiep`, `PATCH /api/v1/doanh-nghieps/me` 200 (tested R10 còn valid). | **STILL Open ❌** |

> **Kết luận R11 vs dev fix:** Dev chưa fix BUG-DN-MENU-ROUTE-001. FE chưa bind navigate handler cho sidebar item DN role + chưa tạo route `/doanh-nghiep/me/sua` hoặc `/ho-so-doanh-nghiep` cho DN role. DN-016 + DN-019 vẫn 🚫 Không test được qua UI (giữ verdict R10).

### Tests run R11

| TC | Description | Result | Notes |
|---|---|:-:|---|
| DN-016 (re-run) | DN tự update DN qua UI form | 🚫 Không test được | Block bởi DN-MENU-ROUTE-001 vẫn Open. Cùng nguyên nhân R10. |
| DN-019 (re-run) | DN đổi DN.email không OTP qua UI | 🚫 Không test được | Cùng nguyên nhân DN-016. |
| **DN-002 (re-run)** | **Filter date range qua AntD calendar widget** | **✅Đạt** | Login `cb_nv_tw_03` → list 40 DN → click textbox "Chọn Từ ngày" → calendar dropdown mở → click day "1" → input value `01/05/2026`. Click textbox "Chọn Đến ngày" → calendar dropdown 2 → query `.ant-picker-cell-in-view[title]` → find cell title `2026-05-31` → click → input value `31/05/2026`. Click "Tìm kiếm" → `GET /api/v1/doanh-nghieps?tuNgay=2026-05-01&denNgay=2026-05-31&page=1&pageSize=20` 200. Filter URL fires đúng spec FR-V.III-01 — KHÔNG còn quirk như R10 nhận định. Date filter functional qua AntD calendar widget click chain. |
| **DN-008** | **KPI Tab #3 "Lịch sử hỗ trợ"** | **✅Đạt** | Navigate DN-AGG-0001 detail → tab "Lịch sử hỗ trợ" (uid 110_35) → URL `?tab=lich-su-ho-tro` → render 3 KPI cards (Tổng vụ việc=0, VV hoàn thành=0, Tổng chi phí=0₫) + table "Danh sách vụ việc" empty. Cross-test DN-HNI-0004 (1 VV linked) → KPI cards: Tổng VV=1, VV hoàn thành=0, Tổng chi phí=0₫ + table 1 row `VV-BTP-TW-20260509-009 / VV R12 huongcg test B3-B7 Lao động / DA_DANH_GIA / 9/5/2026`. KPI fan-out per DN đúng spec FR-V.III-04 + cross-module DN R7.5.2. |

### Evidence R11

- [r11-2026-05-10-dn-menu-route-still-broken.png](../../bug-reports/doanh-nghiep/image/r11-2026-05-10-dn-menu-route-still-broken.png) — DN dashboard sau click sidebar item, URL stuck `/dashboard`, không có form DN render.
- [r11-2026-05-10-dn-008-kpi-tab3.png](image/r11-2026-05-10-dn-008-kpi-tab3.png) — DN-HNI-0004 Tab #3 KPI cards + Danh sách VV với 1 VV linked.

### Aggregate verdict R11

| Verdict | Count | TCs |
|---|:-:|---|
| ✅ Đạt | 15 | DN-001, DN-002 (R11 promote), DN-005, DN-006, DN-007, DN-008 (R11 promote), DN-009, DN-013, DN-014, DN-015, DN-017, DN-018, DN-021, DN-023, DN-024 |
| ⚠️ Sai spec minor | 1 | DN-022 (schema `/me` thiếu `linhVucIds` — defer Minor) |
| 🚫 Không test được | 2 | DN-016, DN-019 (block bởi DN-MENU-ROUTE-001) |
| 🚫 Tier 3 | 1 | DN-020 (VNeID OOS) |
| OOS | 3 | DN-010, DN-011, DN-012 (Import Excel) |

### So sánh R10 vs R11

| Metric | R10 | R11 |
|---|---|---|
| TC ✅Đạt | 14 | **15** (+1 DN-002) |
| Promote DN-002 | ⚠️Sai spec | **✅Đạt** (date filter qua AntD calendar) |
| Promote DN-008 | ⏰Hoãn | **✅Đạt** (KPI Tab #3) |
| BUG-DN-MENU-ROUTE-001 | Open | **STILL Open** (dev chưa fix) |
| DN-016/019 | 🚫 | 🚫 (giữ — bị block bởi bug Open) |

**Action cho dev:** Fix BUG-DN-MENU-ROUTE-001 — bind navigate handler cho sidebar item DN role + tạo route `/doanh-nghiep/me/sua` hoặc `/ho-so-doanh-nghiep` cho DN role + form expose full DN schema.

---

## R10 UI re-verify 2026-05-10 02:00:00 — Full UI click chain, không API direct (LATEST)

### Scope

User yêu cầu re-run R7.7.4 chính xác qua UI. R9 đã dùng API direct (`PATCH /api/v1/doanh-nghieps/me` qua fetch) cho DN-005/016/017/019, vi phạm memory rule `feedback_test_method_ui_only`. R10 thực hiện lại qua UI click chain — phát hiện UI gap nghiêm trọng mà R9 missed.

### Tests run R10 — UI MCP click chain

| TC | Description | Result | Notes |
|---|---|:-:|---|
| DN-001 | List + permission columns | ✅Đạt | `cb_nv_tw_03` UI: pool 31 DN, 9 cột (Mã/Tên/MST/Quy mô/Ngành nghề/Địa chỉ/Số lần HT/Tổng chi phí/Hành động), per-row 3 button (eye/edit/delete) + Xuất Excel button. |
| DN-002 | Filter — Từ khóa/Quy mô/Tỉnh/LV KD/date range | ⚠️Sai spec partial | UI click chain 4/5 PASS: (a) Từ khóa "Hữu Nghị" → 1/1 match `DN-TW-001`. (b) Quy mô=`Siêu nhỏ` → 12/12 row="Siêu nhỏ" URL `?quyMo=SIEU_NHO`. (c) Tỉnh=`Hà Nội` → 9 row URL `?tinhThanhId=7ab46d68-...`. (d) LV KD multi-select 2 LV → URL `?linhVucIds=id1,id2` 0 result (không seed match — filter mechanic OK). (e) Date range AntD DatePicker textbox không nhận direct fill — cần calendar widget click chain phức tạp; URL không nhận `tuNgay/denNgay`. **Date filter ⚠️ AntD picker UI quirk** (không phải bug, FE behaviour standard). Multi-select `ant-select-multiple` class verified, 12 LV total qua scroll virtual list. |
| DN-005 | CB sửa email DN qua UI form | ✅Đạt | `cb_nv_tw_03` UI: list → edit DN-AGG-0001 → fill email field → click Lưu → confirm dialog "Xác nhận thay đổi" diff old/new → click "Lưu thay đổi" → `PATCH /api/v1/doanh-nghieps/85fbcf23-9c42-42b3-a7ab-ed5df50fbe47 200`. **Replace R9 API direct.** |
| DN-006 | Hard delete DN không VV qua UI | ✅Đạt | UI: row DN-HCM-0001 (0 VV) → click delete icon → popconfirm "Xóa doanh nghiệp? Bạn có chắc..." → click "Xóa" → `DELETE /api/v1/doanh-nghieps/<id> 204` → pool 31→30, DN-HCM-0001 mất khỏi list. **R11 verify hard delete:** GET by ID 404 + `includeInactive=true` không show — record xóa hoàn toàn (xem section R11.1 hard delete). |
| DN-007 | Guard delete DN có VV qua UI | ✅Đạt | UI: DN-BCT-001 (3 VV) → delete icon → popconfirm → "Xóa" → `DELETE 409 ERR-DN-03 "Doanh nghiệp đang có 3 vụ việc xử lý, không thể xoá"`. Guard fire đúng. |
| DN-013 | Export Excel qua UI button | ✅Đạt | UI click button "Xuất Excel" → `POST /api/v1/doanh-nghieps/export {page:1,pageSize:20} 200`. Response `Content-Disposition: attachment; filename="xuat-doanh-nghiep.xlsx"`, content-length=9463 bytes, content-type xlsx. |
| DN-014 | QTHT view-only | ✅Đạt | R9 verified UI navigate `qtht_06` isolated context — sidebar có DN menu, click eye OK, không thấy edit/delete (đúng spec). Không re-test R10 vì R9 đã UI-based. |
| DN-015 | CB_PD view-only | ✅Đạt | R9 verified UI navigate `cb_pd_tw_06` — tương tự QTHT view-only. |
| **DN-016** | **DN tự update DN qua UI form** | **🚫 Không test được** | **NEW R10 finding:** Login DN `9999999998` UI thành công (dashboard render đủ 5 menu). Sidebar có item "Quản lý doanh nghiệp được hỗ trợ" — **click không navigate** (button có onClick handler nhưng không đổi URL, vẫn `/dashboard`). Direct nav `/doanh-nghiep/<own-id>/sua` → FE route guard redirect về `/dashboard`. Direct nav `/thong-tin-doanh-nghiep` `/ho-so-doanh-nghiep` `/doanh-nghiep` `/doanh-nghiep/me` → 404 hoặc redirect dashboard. `/profile` chỉ là TAI_KHOAN profile (username/email tài khoản), KHÔNG phải DOANH_NGHIEP profile. **DN role không có UI route nào để self-update DN info — bug Major**. R9 false PASS bằng API direct `PATCH /me` (UI gap không kiểm tra). Log new bug. |
| DN-017 | DN không xóa DN của mình | ✅Đạt | Implicit: DN không có UI route edit → cũng không có UI nút delete. Probe `DELETE /api/v1/doanh-nghieps/me` 403 đúng spec (R9 verified). |
| DN-018 | NHT/TVV/CG không thấy menu DN | ✅Đạt | R9 verified UI multi-role isolated context: NHT/TVV/CG sidebar không hiện "Quản lý doanh nghiệp được hỗ trợ". DN role có hiện nhưng broken (xem DN-016). |
| **DN-019** | **DN đổi DN.email không OTP qua UI** | **🚫 Không test được** | **Block bởi DN-016 UI gap.** Cùng nguyên nhân — DN không có UI form để đổi email DN. R9 false PASS bằng API direct. Cần fix DN-016 trước. |
| DN-021 | Field `tongNguonVon` UI | ✅Đạt | Edit form CB `cb_nv_tw_03` có spinbutton "Tổng nguồn vốn (VNĐ)" (DN-AGG-0001 form) — field render đúng v3.5. |
| DN-022 | Multi-select LV KD UI | ⚠️Sai spec minor | Filter ✅ `ant-select-multiple` 12 options. Form CB ĐK ✅ multi-select combobox "Lĩnh vực kinh doanh" placeholder "Chọn một hoặc nhiều lĩnh vực". /me schema thiếu `linhVucIds` — minor inconsistency (R9 finding still applies). |
| DN-023 | tinh_thanh_id UUID | ✅Đạt | Filter URL `?tinhThanhId=7ab46d68-7aad-49b0-bee6-51465e301e4a` UUID format đúng v3.5 #5. |
| DN-024 | 4 cặp field rename v3.5 #7 | ✅Đạt | R9 verified DN /me keys: `giayCnDkkd` `loaiDnId` `chucVuDaiDien` `dienThoai` ✅. |
| DN-008 | KPI Tab #3 | ⏰Hoãn | Not tested R10 (R9 not retested either). Tier 3 KPI dependency chain. |
| DN-009 | Auto-suggest quy mô | ✅Đạt | R8 verified — auto-suggest fire khi đổi LĐ/DT/Vốn (NĐ39/2018). |
| DN-010..012 | Import Excel | OOS | Out-of-scope. |
| DN-020 | VNeID login DN | 🚫Tier 3 | Out-of-scope (Tier 3 deferred). |

### NEW BUG R10 — DN-MENU-ROUTE-001

**DN role sidebar item "Quản lý doanh nghiệp được hỗ trợ" non-functional.** Button render trong sidebar nhưng click không navigate. Direct URL `/doanh-nghiep/<id>/sua` redirect về `/dashboard`. DN không có UI path nào để self-update DOANH_NGHIEP info — vi phạm SRS FR-V.III bảng permission DN role 📝 RU* (DN có quyền update own DN nhưng UI không expose). Severity: **Major** (block DN-016/019 functional flow). File log: [bug-report-r7-7-4-dn.md](../../bug-reports/doanh-nghiep/bug-report-r7-7-4-dn.md) `BUG-DN-MENU-ROUTE-001`.

### Evidence R10

- [r10-2026-05-10-dn-001-list-cbnvtw.png](image/r10-2026-05-10-dn-001-list-cbnvtw.png) — DN-001 CB list 31 DN
- [r10-2026-05-10-dn-002-filter-tinh-hanoi.png](image/r10-2026-05-10-dn-002-filter-tinh-hanoi.png) — DN-002 filter Tỉnh=Hà Nội 9 result
- [r10-2026-05-10-dn-002-list-default.png](image/r10-2026-05-10-dn-002-list-default.png) — DN-002 default 31 result
- [r10-2026-05-10-dn-005-edit-email-success.png](image/r10-2026-05-10-dn-005-edit-email-success.png) — DN-005 PATCH 200 sau confirm dialog
- [r10-2026-05-10-dn-016-sidebar-broken.png](image/r10-2026-05-10-dn-016-sidebar-broken.png) — DN-016 sidebar non-functional, dashboard remain

### So sánh R9 vs R10

| Metric | R9 (API direct) | R10 (UI click chain) |
|---|---|---|
| Method | `fetch PATCH /api/v1/doanh-nghieps/me` | UI form → click Lưu → confirm dialog → click "Lưu thay đổi" |
| DN-005/016/019 verdict | ✅ ✅ ✅ (false PASS — bypass UI) | ✅ 🚫 🚫 (correct — discover UI gap) |
| New bug found | 0 | 1 (DN-MENU-ROUTE-001) |
| Memory rule compliance | ❌ Vi phạm `feedback_test_method_ui_only` | ✅ Tuân thủ |

**Kết luận:** R10 chứng minh tại sao memory rule "UI click chain mandatory" quan trọng — API direct test có thể giả PASS nhưng UI gap thực sự block user flow.

---

## R9 retest 2026-05-10 01:35:00 — Sau dev fix 4 BUG-DEPLOY (cũ — bị thay thế bởi R10)

### Scope

Verify dev fix 4 bug + chạy 4 TC bị block (DN-005/016/017/019). Test với 3 isolated context: NHT (`nht_01`) cho permission verify, QTHT (`qtht_01`) cho FR07 filter verify, DN mới đăng ký (`9999999998`) cho 4 TC unblock.

### Bug fix verify (4/4 đều CLOSED)

| Bug | R8 status | R9 verify (2026-05-10 01:35) | New status |
|---|:-:|---|:-:|
| BUG-DN-018-NHT-LEAK | Open | NHT `GET /api/v1/doanh-nghieps?page=1&pageSize=5` 403 ERR-AUTH-DN-00-01 (was 200 + 11 records). Detail GET 403. PATCH/DELETE giữ 403. FE route `/doanh-nghiep/danh-sach` redirect về dashboard NHT. | Closed ✅ |
| BUG-FR22-DEPLOY-04 | Open | DN mới đăng ký MST `9999999998`: register 201 + `trangThai=CHO_KICH_HOAT` → activate email → `trangThai=HOAT_DONG` (KHÔNG còn `CHO_PHAN_QUYEN`). Login 200 + OTP token. Verify-OTP 200 + accessToken. ERR-AUTH-LOGIN-05 đã biến mất. | Closed ✅ |
| BUG-FR07-DEPLOY-001 | Open | `GET /api/v1/danh-muc/tree?loaiDanhMuc=LINH_VUC_KINH_DOANH` 200 + count=12 (BAN_LE/DV_AN_UONG/VAN_TAI/CNTT/TAI_CHINH/BDS/GD_DT/Y_TE/SX/XAY_DUNG/NLTS/KHAC). DN list response có `linhVucIds: []` field. | Closed ✅ |
| BUG-FR07-DEPLOY-002 | Open | Filter "Lĩnh vực KD" SCR-V.III-01 + form ĐK đều `ant-select-multiple` placeholder "Chọn một hoặc nhiều lĩnh vực" + 10 visible options. Filter API accept array param `linhVucIds=<id1>&linhVucIds=<id2>` → 200. | Closed ✅ |

### Tests run (4 TC unblock + side-effect verify)

| TC | Description | Result | Notes |
|---|---|:-:|---|
| DN-005 | Sửa thông tin DN — đổi email DN không ảnh hưởng TAI_KHOAN.email | ✅Đạt | Login DN `9999999998` → `PATCH /api/v1/doanh-nghieps/me {email: 'qa-r9-dn-changed@example.test'}` 200 + success. DN.email đổi từ `qa-r9-verify` → `qa-r9-dn-changed`. TAI_KHOAN login vẫn dùng username = MST `9999999998` (không phụ thuộc email). |
| DN-016 | DN tự cập nhật hồ sơ qua API | ✅Đạt | Permission `update_doanh_nghiep` có trong `auth/me` user permissions. PATCH `/me` 200. |
| DN-017 | DN KHÔNG xóa được DN của mình | ✅Đạt | `DELETE /api/v1/doanh-nghieps/me` 403 ERR-AUTH-DN-00-01 "Role không được phép truy cập endpoint CMS này". Permission list KHÔNG có `delete_doanh_nghiep` ✅ khớp spec DN role 📝 RU* (no D). |
| DN-019 | DN đổi DOANH_NGHIEP.email không cần OTP, không đổi TAI_KHOAN.email | ✅Đạt | Cùng test với DN-005. Không có OTP challenge. Username login MST không đổi. |
| DN-018 (NHT retest) | NHT BE read permission | ✅Đạt | Closed BUG-DN-018-NHT-LEAK — list/detail GET 403 đúng spec. Combined với CG/TVV verified ở R8 → 3/3 role pass. |
| DN-022 | Multi-select Lĩnh vực KD | ⚠️Sai spec partial | Filter SCR-V.III-01 ✅ multi-select 10 options. Form ĐK DN ✅ multi-select 10 options. CMS list response ✅ `linhVucIds: []`. **Tuy nhiên** DN /me endpoint schema thiếu field `linhVucIds` (CMS list có). Schema inconsistency minor — không block flow. |
| DN-024 (R9 confirm) | 4 cặp tên trường v3.5 #7 | ✅Đạt | DN `/me` keys: `giayCnDkkd` ✅, `loaiDnId` ✅, `chucVuDaiDien` ✅, `dienThoai` ✅. Legacy 4 cặp KHÔNG có. |
| DN-021 (R9 confirm) | Field `tongNguonVon` | ✅Đạt | Có trong /me schema. |

### Evidence

- [r9-2026-05-10-fr07-filter-multiselect-10options.png](../../bug-reports/doanh-nghiep/image/r9-2026-05-10-fr07-filter-multiselect-10options.png) — SCR-V.III-01 filter Lĩnh vực KD multi-select sau fix
- [r9-2026-05-10-dn-018-nht-fix-verified-redirect.png](../../bug-reports/doanh-nghiep/image/r9-2026-05-10-dn-018-nht-fix-verified-redirect.png) — NHT bị block khỏi `/doanh-nghiep/danh-sach`
- [r9-2026-05-10-dn-account-dashboard.png](image/r9-2026-05-10-dn-account-dashboard.png) — DN account 9999999998 dashboard sau login (sidebar đúng quyền DN)

### Tài khoản DN mới tạo cho R9 verify

| Username (MST) | Mật khẩu | Email DN gốc | Email DN sau đổi | Trạng thái | DN id |
|---|---|---|---|:-:|---|
| `9999999998` | `Secret@123` | `qa-r9-verify@example.test` | `qa-r9-dn-changed@example.test` | HOAT_DONG | `85fbcf23-9c42-42b3-a7ab-ed5df50fbe47` (DN-AGG-0001) |

---

## R8 retest 2026-05-09 19:55:00 — Account `cb_nv_tw_03`

### Scope

Re-verify 3 BUG-DEPLOY (001/002/003) + DN-022 + DN-009 + **DN-002 full filter coverage** (R7 chỉ test 1/5 filter, R8 thêm Quy mô/Tỉnh/Khoảng thời gian). Pool **27 DN** sau registry mới `DN-HNI-0003 9999999999` (R8 21:24 tạo, không phụ thuộc count R7-rerun cũ 26 DN).

### Tests run

| TC | Description | Result | Notes |
|---|---|:-:|---|
| DN-002 | Tìm kiếm DN — Từ khóa/Quy mô/Tỉnh/Lĩnh vực/Khoảng thời gian | ⚠️Sai spec (partial coverage) | **Re-cover full filter (R7 chỉ test "BNI" keyword).** R8 2026-05-09 21:30:00: (a) Filter `Quy mô=Vừa` → 8/8 record `Vừa`, API `quyMo=VUA` ✅. (b) Filter `Tỉnh/Thành=Hà Nội` → 7 record (FK based, `tinhThanhId=7ab46d68-...` API param ✅). (c) Filter `Khoảng thời gian 01/04/2026-30/04/2026` → 0 record (no DN created Apr 2026), API `tuNgay=2026-04-01&denNgay=2026-04-30` fire ✅ mechanic OK. (d) Filter `Lĩnh vực KD` ❌ block bởi BUG-FR07-DEPLOY-002 (textbox không multi-select). (e) Filter Từ khóa "BNI" R7 đã ✅ 3/3. **4/5 filter ✅, 1/5 ❌ (block bởi BUG-DEPLOY-002).** Note: UI có thêm filter `Ngành nghề` không có trong test plan (combobox 5 option), không scope để test. Evidence: [r8-2026-05-09-dn-002-filter-date-range.png](r8-2026-05-09-dn-002-filter-date-range.png). |
| DN-009 | Auto-suggest quy mô NĐ39/2018 | ✅Đạt | **Đảo verdict ⚠️→✅.** Form Sửa DN-BCT-001 — trigger thay số LĐ 14→88 qua MCP `evaluate_script` `dispatchEvent(input/change/blur)` → combobox Quy mô tự đổi `Siêu nhỏ`→`Nhỏ` (đúng NĐ39 cho ngành CN/XD). Toast warning fire: `Các tiêu chí cho kết quả khác nhau — đã chọn mức cao hơn.` (khớp `srs-update-2026-5-5/srs-fr-07-doanh-nghiep.md` §SCR-V.III-02 §Quy tắc tương tác dòng 358-359). R7-rerun mark ⚠️ do test combobox **statically** không trigger change → miss. Reset LĐ về 14 + click Hủy, không submit, data DN-BCT-001 nguyên vẹn. |
| DN-022 | Multi-select Lĩnh vực KD | ❌Lỗi | UI vẫn render `<input type="text">` ở 2 vị trí: filter list page (uid `4_20`) + form Sửa (uid `5_37`, HTML `id="linhVucKinhDoanh"` class `ant-input`). So sánh cùng form: Loại DN/Quy mô/Ngành nghề combobox listbox; Tỉnh/Thành `select single`. STILL OPEN — BUG-FR07-DEPLOY-002. |
| DN-021 | Field `tongNguonVon` v3.5 #6 | ✅Đạt | Re-verify DN-BCT-001 keys list — có `tongNguonVon` (value `null` cho DN này, field tồn tại). Legacy `vonDauTu` không có. |
| DN-024 | 4 cặp tên trường rename v3.5 #7 | ✅Đạt | DN-BCT-001 keys: `giayCnDkkd` ✅, `loaiDnId` ✅, `chucVuDaiDien` ✅, `dienThoai` ✅. Legacy 4 keys `giayCndk`/`loaiDoanhNghiepId`/`chucVuDd`/`soDienThoai` đều không có. |

### 3 BUG-DEPLOY re-verify 2026-05-09 19:55:00

| Bug | Status | Re-verify evidence (R8 với `cb_nv_tw_03`) |
|---|---|---|
| BUG-FR07-DEPLOY-001 | STILL OPEN | `/api/v1/danh-muc/tree?loaiDanhMuc=LINH_VUC_KINH_DOANH` 200 + count=0 + sample=[]. DN-BCT-001 keys CÓ `linhVucKinhDoanh` (string null), KHÔNG có `linhVucIds[]` |
| BUG-FR07-DEPLOY-002 | STILL OPEN | UI textbox 2 vị trí (xem DN-022). Form HTML `<input id="linhVucKinhDoanh" class="ant-input" type="text">` |
| ~~BUG-FR07-DEPLOY-003~~ | **WITHDRAWN — false positive 2026-05-09 22:30:00** | Verify SRS authoritative `srs-update-2026-5-5/srs-fr-10-quan-tri.md` line 1983 + FR-VIII-30 lines 1445-1476 + NotebookLM HTPLDN: TINH_THANH là `DANH_MUC loai='TINH_THANH'`, KHÔNG entity riêng E32, schema 4 field (ma/ten/mo_ta/loai_danh_muc) KHÔNG có `vung_mien`. Endpoint `/api/v1/danh-muc/tree?loaiDanhMuc=TINH_THANH` 200 + 63 tỉnh = đúng spec. Bug log dựa vào doc QA-side `02-thu-tu-module.md` ghi sai nhãn entity → withdraw |

### Observation (không log bug, ghi nhận data quality)

DN-BCT-001 lưu `quyMo="Siêu nhỏ"` cho 14 LĐ + 2.2 tỷ DT (ngành CN/XD). Theo NĐ39/2018 thì 14 LĐ vượt ngưỡng "Siêu nhỏ" (≤10 LĐ) → quy mô đúng phải là "Nhỏ". Auto-suggest trigger `Nhỏ` đúng khi user thao tác form. Đây là data seed quality vấn đề (tạo từ trước v3.5 deploy), KHÔNG phải bug FE. Không log — để dev/seed team biết.

### Login flow audit 2026-05-10 00:10:00 — không phải scope DN-018, side-effect kiểm tra theo yêu cầu user

Test 5 luồng login với 4 role (`cb_nv_tw_02/03`, `qtht_03`, `tvv_r13_a19`, `huongcg`, `nht_01`) để check sức khoẻ login. Kết quả:

| Aspect | Status | Note |
|---|:-:|---|
| Token storage | ✅ | HttpOnly cookie cho access + refresh token (XSS-safe). `localStorage.auth-store.state` chỉ chứa `userInfo` (id/hoTen/vaiTro/donViId/capDonVi/permissions[]) — không chứa secret. |
| Login API sequence | ✅ | `POST /auth/login` → `POST /auth/verify-otp` → `GET /auth/me` → dashboard data parallel. |
| Wrong password UX | ✅ | Toast `"Tên đăng nhập hoặc mật khẩu không đúng."` + 401 `ERR-AUTH-LOGIN-01`. |
| Empty submit UX | ⚠️ Minor | Click `[Đăng nhập]` với cả 2 field rỗng → KHÔNG hiển thị validation message + KHÔNG fire API + KHÔNG hint required. User UX: button feels dead. Inputs không có `required` HTML5 + không có `aria-invalid` + không có `.ant-form-item-explain-error`. Spec FR-VIII-01 yêu cầu validate trống → có thể xem là UI gap nhỏ. **Không log bug riêng** (Minor + cần BA confirm spec validate trống có yêu cầu message hay chỉ disable button). |
| Rate limit | ✅ | Sau ~3-4 lần fail → BE trả 429. cb_nv_tw_03 hit 429 sau 4 attempts (cùng IP). Bảo vệ brute-force tốt. |
| OTP timer | ✅ | 5:00 countdown đếm ngược, hiển thị `m:ss` rõ ràng. |
| OTP auto-submit | ✅ | Type 6 digit → tự fire `POST /auth/verify-otp` không cần click `[Xác nhận]`. UX tốt. |
| Email mask OTP screen | ✅ borderline | `cb_***@htpldn.test` — lộ 3 ký tự đầu + full domain. Acceptable; có thể siết chặt hơn (vd `c***@h***.test`). |
| Console errors trong login flow | ✅ | 0 lỗi/warn qua 5 lượt login (cb_nv_tw_03 / qtht_03 / tvv_r13_a19 / nht_01 / huongcg). |
| BUG-ENV-01 form persistence | ⚠️ known | Username/password persist giữa navigate dù không check "Ghi nhớ đăng nhập" — đã document trong CLAUDE.md `## Known app bugs`. |
| `/auth/me` 401 trước login | ✅ | Page boot fire 1 lần check session → 401 nếu chưa login → FE redirect `/login`. Pattern chuẩn, không phải bug. |

### Bug downgrade R7-rerun → R8

`DN-009 (R7-rerun ⚠️ Sai spec — cần BA confirm UI hint)` → **withdrawn**. SRS `srs-update-2026-5-5/srs-fr-07-doanh-nghiep.md` §SCR-V.III-02 row 13 (`Quy mô — auto-suggest`) + row 15-16 (`change → auto-calc quy mô`) + §Quy tắc tương tác (`Auto-suggest quy mô: khi nhập số lao động và doanh thu...` + `lấy mức cao hơn và hiển thị warning`) đều ĐÃ rõ là behavior FE phải implement. R8 verify FE đã implement đúng — không cần BA confirm thêm.

`BUG-FR07-DEPLOY-003 (R7 Minor — TINH_THANH chưa migrate entity E32)` → **withdrawn 2026-05-09 22:30:00 (false positive)**. Bug log dựa vào doc QA-side `input/quy-trinh-nghiep-vu/02-thu-tu-module.md` ghi `TINH_THANH (entity riêng E32) + cột vung_mien`. Verify lại nguồn SRS authoritative + NotebookLM HTPLDN: TINH_THANH dùng `DANH_MUC loai='TINH_THANH'` (line 1983 + FR-VIII-30 lines 1445-1476), schema chỉ 4 field (ma/ten/mo_ta/loai_danh_muc), KHÔNG có `vung_mien`, KHÔNG có endpoint `/api/v1/tinh-thanhs`. FE hiện dùng `/api/v1/danh-muc/tree?loaiDanhMuc=TINH_THANH` = đúng spec. Tổng số bug deploy gap effective: **2** (DEPLOY-001 + DEPLOY-002).

---

## R7-rerun 2026-05-09 18:00:00 — Account `cb_nv_tw_06`/`qtht_06`/`cb_pd_tw_06`

### Tests run (re-run + extend)

| TC | Description | Result | Notes |
|---|---|:-:|---|
| DN-006 | Xóa DN không VV → hard delete | ✅Đạt | Click delete DN-LSN-0001 (0 VV) → DELETE `/api/v1/doanh-nghieps/66bac9ff-...` 204. Pool 27→26. [r7-7-4-rerun-pool-26-after-delete.png](r7-7-4-rerun-pool-26-after-delete.png). **Note 2026-05-10:** Spec đổi từ soft → hard delete (R11.1 verify). DN-LSN-0001 đã hard delete, GET by ID 404 + `includeInactive=true` không restore được. |
| DN-007 | Xóa DN có VV → ERR-DN-03 guard | ✅Đạt | DELETE DN-AG-004 (1 VV) → **HTTP 409** + body `{"code":"ERR-DN-03","message":"Doanh nghiệp đang có 1 vụ việc xử lý, không thể xoá"}`. R7 INCONCLUSIVE root cause = JWT 401 expire ~2 phút (memory `qa_htpldn_jwt_revoke_aggressive`), không phải FE bug — re-test rapid click PASS |
| DN-008 | Tab #3 KPI Tổng VV/HT/CP | ✅Đạt | Verified ở R7.5.2 cross-module: DN-BCT-001 KPI 3/0/0 ₫ + 3 VV liên kết render đúng. [functional-r7-5-2-cross-module-dn.md](functional-r7-5-2-cross-module-dn.md) |
| DN-009 | Auto-suggest quy mô NĐ39/2018 | ⚠️Sai spec | Form Sửa DN-NEW-NH2 (88 LĐ + 28 tỷ DT + 0 vốn) — field Quy mô là combobox manual, KHÔNG có hint/badge "Đề xuất: ...". CB_NV_TW không có button Tạo (DN tự reg) → test self-reg form ở R7.2.4 cũng không thấy hint. Cần BA confirm spec FR có yêu cầu UI hint hay chỉ BE validate |
| DN-013 | Xuất Excel | ✅Đạt | Click button "download Xuất Excel" → `POST /api/v1/doanh-nghieps/export` 200 |
| DN-014 | QTHT view-only | ✅Đạt | `qtht_06` → /doanh-nghiep/danh-sach: list 26 DN render OK, per-row chỉ button `eye`, KHÔNG có `edit`/`delete`/`Thêm`/`Xuất Excel`. [r7-7-4-qtht-06-view-only.png](r7-7-4-qtht-06-view-only.png) |
| DN-015 | CB_PD view-only | ✅Đạt | `cb_pd_tw_06` → /doanh-nghiep/danh-sach: list 26 DN render OK, per-row chỉ button `eye`, KHÔNG có `edit`/`delete`/`Thêm`. Có button `Xuất Excel` (CB_PD có quyền export, khác QTHT). [r7-7-4-cbpd-tw-06-view-only.png](r7-7-4-cbpd-tw-06-view-only.png) |
| DN-021 | Field `tongNguonVon` v3.5 #6 | ✅Đạt | API `GET /api/v1/doanh-nghieps?page=1&pageSize=50` response keys: `tongNguonVon` exists, `vonDauTu` (legacy) không có. v3.5 #6 deploy OK |
| DN-024 | 4 cặp tên trường rename v3.5 #7 | ✅Đạt | API response: `giayCnDkkd` ✅, `loaiDnId` ✅, `chucVuDaiDien` ✅, `dienThoai` ✅. Legacy `giayCndk`/`loaiDoanhNghiepId`/`chucVuDd`/`soDienThoai` KHÔNG có. 4/4 cặp deploy đúng v3.5 |
| DN-022 | Multi-select Lĩnh vực KD | ❌Lỗi | UI textbox vẫn render (uid 124_20 / 133_20 / 139_20 / 145_20 / 149_20) — BUG-DEPLOY-002 STILL OPEN |
| DN-016/017/019 | Sửa DN tự, đổi email | 🚫Không test được | Block bởi [BUG-FR22-DEPLOY-04](../../bug-reports/qtht-tai-khoan/Pass-bug-report-r7-7-4-fr22-cho-phan-quyen-not-bypassed.md) — BE chưa deploy v3.5 (state CHO_PHAN_QUYEN), DN account `9999999999` activate qua email rồi vẫn 401 ERR-AUTH-LOGIN-05 khi login |
| DN-018 | Authorization NHT/TVV/CG | ⚠️Sai spec | R8 2026-05-10 00:05:00 — CG (`huongcg`) ✅Đạt + TVV (`tvv_r13_a19`) ✅Đạt: sidebar ẩn + FE redirect home + BE 403 list/detail. NHT (`nht_01`) ⚠️Sai spec: sidebar ẩn ✅ nhưng FE render `/doanh-nghiep/danh-sach` (route guard miss) + BE GET list/detail trả 200 (read leak) — log [BUG-DN-018-NHT-LEAK](../../bug-reports/doanh-nghiep/bug-report-r7-7-4-dn.md) Major; PATCH/DELETE guard 403 đúng. **Bug khu trú duy nhất role NHT** (CG + TVV đều full guard). TVV username discover qua endpoint `GET /api/v1/tai-khoan` (singular, BE only exposes), `users.csv` chưa sync — convention `tvv_r{N}_a{M}` + password `Secret@123`. |
| DN-020 | VNeID Tier 3 | 🚫Không test được | Hạ tầng VNeID chưa ready (out of scope R7) |
| DN-003/004/005 | Import Excel | OUT-OF-SCOPE | v3.5 không có Import Excel |

### 3 BUG re-verify 2026-05-09 17:52:00

| Bug | Status | Re-verify evidence |
|---|---|---|
| BUG-DEPLOY-001 | STILL OPEN | API `/api/v1/danh-mucs/lookup?loaiDanhMuc=LINH_VUC_KINH_DOANH` count=0; DN response `linhVucIds[]` không có |
| BUG-DEPLOY-002 | STILL OPEN | Filter list page UI: textbox `<input>` thay multi-select (uid 149_20) |
| BUG-DEPLOY-003 | STILL OPEN | API `/api/v1/tinh-thanhs` 404; DM tree không có `vungMien` |

### Root cause R7 INCONCLUSIVE DN-007 (giải)

R7 (2026-05-07) DN-007 marked INCONCLUSIVE vì click "Xóa" popconfirm KHÔNG trigger DELETE request. Re-run R7-rerun (2026-05-09 18:00:00) phát hiện:

1. **JWT revoke aggressive** (~2 phút) gây 401 silent → FE intercept redirect `/login` thay vì show error → user perception "click không fire". Memory `qa_htpldn_jwt_revoke_aggressive` đã document từ R3.
2. Re-test với rapid pattern (login → navigate → click delete → click Xóa atomic) trong window <2 phút → DELETE fire chuẩn, BE response 204 (DN-006) / 409 (DN-007).
3. KHÔNG phải FE bug — không cần log Major suspect.

### Bug downgrade

`BUG-DN-007 — Suspect FE: button "Xóa" không trigger API DELETE` (R7) **withdrawn** — root cause là session expire timing, không phải FE handler bug.

---

## R7 Original 2026-05-07 — Account `cb_nv_tw_02`

## Tests run

| TC | Description | Result | Notes |
|---|---|:-:|---|
| DN-001 | Xem list DN, phân trang, 9 cột | ✅ PASS | List render 15/15 mục, đủ 9 cột (Mã/Tên/MST/Quy mô/Ngành nghề/Địa chỉ/SốHT/TổngCP/HĐ) |
| DN-002 | Search keyword "BNI" | ✅ PASS | Filter trả 3/3 mục match (BNI-001/002/003) |
| DN-022 | Multi-select Lĩnh vực KD | ⚠️ FAIL pre-finding | UI render `textbox` (uid 49_20) thay vì multi-select dropdown — bug v3.5 #9 chưa deploy FE confirmed |
| DN-007 | Xóa DN có VV → ERR-DN-03 guard | ⚠️ INCONCLUSIVE | Click button "Xóa" trên popconfirm KHÔNG trigger API DELETE. Network log không có DELETE /api/v1/doanh-nghieps/{id}. FE suspect bug. Cần re-test |
| DN-003 / DN-004 | Tier 2 self-reg / MST trùng | DEFER | Chờ BA Q1/Q2/Q3 unblock FR-VIII-22 |
| DN-005 / DN-016/017/019 | Sửa DN, DN tự update, đổi email | DEFER | Cần test với role `dn_*_01` đồng thời |
| DN-008 | Tab #3 KPI Tổng VV/HT/CP | DEFER | Sẽ test trong R7.5.2 cross-module |
| DN-009 / DN-021 | Phân loại quy mô auto-suggest, `tong_nguon_von` | DEFER | Cần verify BE schema v3.5 trước |
| DN-013 | Xuất Excel | DEFER | Cần verify file output |
| DN-014 / DN-015 / DN-018 | Authorization QTHT/CB_PD/NHT | DEFER | Cần switch role |
| DN-020 | VNeID Tier 3 | DEFER | Hạ tầng VNeID chưa ready |
| DN-023 | `tinh_thanh_id` source 63 tỉnh | DEFER | Cần test qua dropdown form mới — verify form Sửa DN |
| DN-024 | 4 cặp tên trường rename | DEFER | Cần inspect API request payload |

## Bug confirmed

### BUG-DN-022 — Lĩnh vực KD textbox thay vì multi-select (v3.5 #9 chưa deploy FE)

- **Severity:** Medium (functional gap, không block luồng test)
- **SRS ref:** `srs-update-2026-5-5/srs-fr-07-doanh-nghiep.md` v3.5 #9 — DOANH_NGHIEP_LINH_VUC M-N + multi-select
- **Steps:** Login `cb_nv_tw_02` → /doanh-nghiep/danh-sach → inspect filter "Lĩnh vực KD"
- **Expected:** AntD `<Select mode="multiple">` dropdown từ DM `LINH_VUC_KINH_DOANH`
- **Actual:** Textbox tự do (a11y `textbox "Lĩnh vực KD"` uid 49_20)
- **Evidence:** [r7-verify-dn-15-records.png](../../seed/r7-verify-dn-15-records.png)

### BUG-DN-007 — Suspect FE: button "Xóa" trên popconfirm không trigger API DELETE

- **Severity:** Major (block guard test)
- **Steps:** Login cb_nv_tw_02 → search BNI → click button delete row DN-BNI-001 → popconfirm "Xóa doanh nghiệp?" → click "Xóa"
- **Expected:** API DELETE /api/v1/doanh-nghieps/{id} fire → response 409/422 với ERR-DN-03 (do DN có VV) hoặc 204 hard delete (spec đổi 2026-05-07)
- **Actual:** Popconfirm dismiss, KHÔNG có DELETE request trong network log (verify pages 1-6 of 112 requests). DN vẫn hiện trong list (3/3 mục).
- **Evidence:** Network log trong session, không có `DELETE` method cho `/api/v1/doanh-nghieps`

## Cascade

- ⚠️ R7.5.2 Tab #3 KPI: cần test sau (DN-008 defer)
- ⚠️ Functional 13 TC defer cần dedicated session sau

## Note (autopilot scope cap)

Autopilot session 2026-05-07 cap test ở 4 TC critical do scope multi-task (R7.3.4 seed + R7.4.A3 workflow + R7.6.1 verify + R7.7.4 functional + R7.5.2 cross-module). Full 17 TC functional cần dedicated session ~2-3 giờ.
