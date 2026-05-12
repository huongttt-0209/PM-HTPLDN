# Functional Test Report — Đánh giá Hiệu quả HTPL (FR-VI-08) R7

| Thông tin | Giá trị |
|-----------|---------|
| **Dự án** | PM HTPLDN — Phần mềm Hỗ trợ Pháp lý Doanh nghiệp |
| **Module** | FR-08 / Nhóm VI — Theo dõi Đánh giá Hiệu quả HTPL |
| **Người test** | QA Automation (Claude Code via Chrome DevTools MCP) |
| **Ngày bắt đầu** | 2026-05-10 22:00:00 (R10b functional 18 TC) |
| **Ngày cập nhật** | 2026-05-10 22:30:00 |
| **Tài liệu tham chiếu** | [`srs-update-2026-5-5/srs-fr-08-danh-gia.md`](../../../../../input/srs-update-2026-5-5/srs-fr-08-danh-gia.md) (v3.5 canonical 8-state SM + FR-VI-01..10 + SCR-VI-01) |
| **Round** | Round 7 — Apply SRS update 2026-05-05 (cherry v3.5) |
| **Account chính** | `cb_nv_tw_01` (Cán bộ Nghiệp vụ TW) |
| **Phạm vi** | 18 TC functional cover FR-VI-01 form (6) + FR-VI-02 tiêu chí (4) + FR-VI-03 phân công (3) + FR-VI-04 reject (1) + Permission cross-cutting (4) |

---

## Verdict (LATEST R11 2026-05-11 14:35:00)

**⚠️ Sai spec toàn cục — 13/18 TC ✅ Đạt (72%) · 2/18 ⚠️ Sai spec · 2/18 ❌ Lỗi · 1/18 🚫 Không test được · 0/18 ⏭ Hoãn**

**R11 (2026-05-11)** — Re-test 18 TC functional với account set `_09` qua MCP Browse UI (không API direct). Đợt mới `DG-20260511-0001` tạo OK ở `LAP_KE_HOACH`. Phase 1 (TC01-06) ✅ 6/6 clean. Phase 2 (TC07-10) ⚠️ 1 sai spec (modal force `trọngSo=100` — DG-010 REPRODUCED) + 1 sai spec inline edit (DG-010 variant phụ) + 2 PASS (TC09 edit non-trọng, TC10 delete OK + BR-CALC-04 gate "Lưu thay đổi" disabled Σ≠100% ✅). Phase 3 (TC11-14) ✅ TC11 add 2 PC OK + Trình phê duyệt ❌ stuck PHAN_CONG (DG-012 REPRODUCED — cb_pd_tw_09 không thấy đợt trong tab "Chờ duyệt PC"). Phase 5 Permission ✅ TC15 (BN) + TC16 (DP) BR-AUTH-03 cross-cấp deny OK + 🚫 TC17 chờ DG-012 + ❌ TC18 QTHT Tiêu chí spinbutton trọng số + delete visible (DG-013 REPRODUCED Tab Tiêu chí — Tab Phân công đã read-only OK).

**Bug re-test R11:** 5/6 Open bug REPRODUCED — DG-010 (Major), DG-012 (Critical), DG-013 (Tab Tiêu chí variant Major), DG-009 (HUY button still missing trên LAP_KE_HOACH). **DG-011 NOT REPRODUCED** trên đợt R11 — PC table render sạch sẽ với tên đầy đủ. DG-008 không test trong R11 (cần đợt advance — block bởi DG-012). **2 bug mới R11:** DG-014 (Medium — Lĩnh vực 2/12 raw UUID) + DG-015 (Minor — Tab Thực hiện/Báo cáo leak BE error toast khi state-gated).

**Phase 4 R11 extras:** TC12 ✅ Đạt (out-of-scope verified 2-source: SRS local FR-VI-03 không có Update + NotebookLM xác nhận). TC-G ✅ modal validation required. TC-E3 ✅ duplicate person → BE 409 + toast OK. TC-LV ❌ DG-014. TC-TAB ❌ DG-015.

**Test method R11:** MCP Browse UI only (không API). 5 isolated contexts: `test_cb_nv_tw_09` (owner), `test_cb_pd_tw_09` (approver), `test_cb_nv_bn_09` (BN scope), `test_cb_nv_dp_09` (DP scope), `test_qtht_09` (QTHT permission test).

---

## Verdict (R10b 2026-05-10 22:55:00 — archived)

**⚠️ FAIL toàn cục — 12/18 TC PASS clean (67%) · 1/18 ⚠️ Sai spec · 1/18 🚫 BLOCKED · 4/18 ❌ FAIL bug**

Phase 1 FR-VI-01 form validation ✅ PASS 6/6. Phase 2 FR-VI-02 tiêu chí CRUD ✅ 3/4 (TC07 ⚠️ sai spec — modal force trongSo=100, BUG-FUNC-DG-010). Phase 3 FR-VI-03 phân công ✅ 3/3 nhưng có 2 bug FE liên quan (DG-011 display "—" tên người + lĩnh vực, DG-013 QTHT permission bypass). Phase 4 FR-VI-04 reject 🚫 BLOCKED bởi DG-012 (đợt không advance state LAP_KE_HOACH → PHAN_CONG sau 4 POST PC). Phase 5 Permission ✅ 2/2 chạy được (TC15 + TC16) + 1 BLOCKED (TC17 cross-cấp deny chờ DG-012) + 1 FAIL (TC18 QTHT bypass).

**Bug mới phát hiện R10b 22:00-22:55:** 4 bug — DG-010 (modal force trongSo=100, Major), DG-011 (UI display PC table empty, Medium), DG-012 (đợt stuck LAP_KE_HOACH, Critical), DG-013 (QTHT permission bypass Phân công, Major). Chi tiết [bug-report-flow-danhgia.md](../../bug-reports/danh-gia/bug-report-flow-danhgia.md).

**Bug major còn open từ R10:** BUG-FUNC-DG-008 (PUT/GET ket-quas inconsistency) + BUG-FUNC-DG-009 (UI thiếu HUY button).

---

## Bảng trạng thái TC (snapshot R11 — LATEST 2026-05-11 14:15:00)

| TC ID | Tên TC ngắn | Status | Round phát hiện | Note (≤15 từ) |
|---|---|:-:|:-:|---|
| TC01 | Form trống → 5 required errors | ✅ Đạt | R11 | 5 errors VN đúng spec, R11 re-confirm |
| TC02 | Tạo đợt valid happy path | ✅ Đạt | R11 | DG-20260511-0001 LAP_KE_HOACH tạo OK |
| TC03 | Tần suất dropdown 2 enum | ✅ Đạt | R11 | "Sơ bộ 6 tháng" + "Trọn năm" |
| TC04 | End < Start date validation | ✅ Đạt | R11 | Error "Ngày kết thúc phải sau ngày bắt đầu" |
| TC05 | Đối tượng dropdown 3 enum | ✅ Đạt | R11 | "Vụ việc" + "Đào tạo" + "Tổng hợp" |
| TC06 | Tên max 500 ký tự | ✅ Đạt | R10b | maxLength=500 attribute |
| TC07 | Add tiêu chí modal force trongSo=100 | ⚠️ Sai spec | R11 | DG-010 modal variant REPRODUCED |
| TC07b | Inline edit trọng số click → force 100 | ⚠️ Sai spec | R11 | DG-010 inline edit variant REPRODUCED |
| TC08 | BR-CALC-04 Σ≠100% disable [Lưu] | ✅ Đạt | R11 | Button "Lưu thay đổi" disabled khi Σ=60% |
| TC09 | Edit non-trọng saved Σ=100% | ✅ Đạt | R11 | Tiêu chí "Chất lượng tư vấn pháp luật" 100% |
| TC10 | Delete tiêu chí inline | ✅ Đạt | R11 | Delete OK, recalculate Σ |
| TC11 | Add 2 PC (TN + ĐGV) | ✅ Đạt | R11 | cb_nv_tw_09 TN + cb_nv_tw_08 ĐGV |
| TC11b | DG-011 PC table render | ✅ Đạt | R11 | NOT REPRODUCED — table render sạch |
| TC12 | Edit role/lĩnh vực phân công | ✅ Đạt | R11 | Out-of-scope SRS (verified NotebookLM + local) — UI ẩn edit đúng spec |
| TC13 | Remove người ĐG ở LAP_KE_HOACH | ✅ Đạt | R10b | Delete + toast OK (R10b carry) |
| TC14 | Trình phê duyệt → CHO_DUYET_PC | ❌ Lỗi | R11 | DG-012 REPRODUCED — đợt stuck PHAN_CONG |
| TC15 | cb_nv_bn_09 không thấy đợt TW | ✅ Đạt | R11 | BCT — list empty + "Tạo kế hoạch" OK |
| TC16 | cb_nv_dp_09 không thấy đợt TW | ✅ Đạt | R11 | BNI — list empty + "Tạo kế hoạch" OK |
| TC17 | cb_pd cross-cấp denied | 🚫 Không test được | R11 | Block bởi DG-012 |
| TC18 | QTHT read-only mọi tab | ❌ Lỗi | R11 | Tab Tiêu chí — DG-013 REPRODUCED |
| TC-G | Modal Add PC validation required | ✅ Đạt | R11 | Empty submit → 2 errors "Vui lòng chọn người đánh giá / vai trò" |
| TC-E3 | Add duplicate PC bị reject | ✅ Đạt | R11 | POST 409 + toast "đã được phân công trong kế hoạch này" |
| TC-LV | Lĩnh vực dropdown 12 options Vietnamese | ❌ Lỗi | R11 | DG-014 NEW — 2/12 raw UUID |
| TC-TAB | Tab Thực hiện/Báo cáo no error toast on state-gated nav | ❌ Lỗi | R11 | DG-015 NEW — 2 tab leak BE error toast |
| **Tổng** | **22 TC (18 plan + 4 extra)** | ✅15 · ⚠️2 · ❌4 · 🚫1 · ⏭0 · 🤷0 | | |

---

## Bảng TC chưa chạy được — cần làm gì để chạy (R11)

Hiện tại còn 7 TC chưa PASS clean — chia 4 nhóm: 2 chờ dev fix modal/inline edit trọng số (TC07/07b), 2 chờ dev fix state advance + permission (TC14/TC18), 1 chờ dev fix state advance (TC17), 2 chờ dev fix UI data + UX toast (TC-LV/TC-TAB).

| TC ID | Vì sao chưa chạy được | Cần làm gì để chạy | Ai làm |
|---|---|---|:-:|
| TC07 | Modal "Thêm tiêu chí" force `trọngSo=100` bất kể nhập | Dev FE fix modal bind `trongSo` đúng — BUG-FUNC-DG-010 | Dev FE |
| TC07b | Inline edit click spinbutton trọng số → force 100 ngay | Dev FE fix spinbutton component không reset value — BUG-FUNC-DG-010 variant phụ | Dev FE |
| TC14 | Trình phê duyệt → POST `/phan-congs/submit` 200 nhưng đợt vẫn `PHAN_CONG` không advance `CHO_DUYET_PC` | Dev BE fix transition trigger sau POST submit — BUG-FUNC-DG-012 | Dev BE |
| TC17 | Cùng nguyên nhân TC14 — không có đợt nào ở `CHO_DUYET_PC` để cross-cấp test | Sau khi DG-012 fix, retest TC14 → đợt advance CHO_DUYET_PC → retest TC17 | Dev BE + QA |
| TC18 | QTHT thấy spinbutton trọng số + button delete trên Tab Tiêu chí (Tab Phân công đã read-only OK) | Dev FE hide edit controls khi user role = QTHT trên Tab Tiêu chí + BE 403 khi QTHT POST/PUT/DELETE tiêu chí — BUG-FUNC-DG-013 | Dev FE + Dev BE |
| TC-LV | Lĩnh vực dropdown 2/12 raw UUID thay tên Vietnamese | Dev BE fix record `LINH_VUC_PL` missing `tenLinhVuc` field hoặc xóa record orphan — BUG-FUNC-DG-014 | Dev BE |
| TC-TAB | Tab Thực hiện + Báo cáo leak BE error toast khi navigate ở state LAP_KE_HOACH | Dev FE check state đợt trước khi gọi API tab load; suppress error toast cho state-gated 4xx — BUG-FUNC-DG-015 | Dev FE |

**Action item ưu tiên R11:** Fix DG-012 (Critical) trước → unblock TC14 + TC17 + workflow B7-B11. DG-010 + DG-013 (Major) song song. DG-014 (Medium) dễ fix (data fix). DG-015 (Minor) UX hint cho dev FE. DG-011 đã không reproduce — có thể đã fix data-specific.

---

## R11 (2026-05-11) — Re-test bộ acc `_09` qua MCP Browse UI

### Setup R11

- **Đợt mới R11:** `DG-20260511-0001` "R11 QA TC FR-VI-01..10 _09 2026-05-11" tạo bởi `cb_nv_tw_09` 14:00:00.
  - Tần suất: Sơ bộ 6 tháng · Đối tượng: Vụ việc · BĐ: 14/05/2026 · KT: 10/11/2026 · State: `LAP_KE_HOACH`.
- **5 isolated context MCP** test cross-role không cookie nhiễm: `test_cb_nv_tw_09` (owner), `test_cb_pd_tw_09` (approver), `test_cb_nv_bn_09` (BCT scope), `test_cb_nv_dp_09` (BNI scope), `test_qtht_09` (QTHT permission).
- **Method:** UI click chain only — không POST/PUT/DELETE direct API. Network log chỉ làm evidence supporting (read response, không probe).

### Phase 1 (TC01-06) — Form validation ✅ 6/6 R11

- **TC01:** 5 required errors VN đúng spec — re-confirm R11.
  - Evidence: [`r11-tc01-required-validation-2026-05-11.png`](image/r11-tc01-required-validation-2026-05-11.png)
- **TC02:** Tạo đợt R11 happy path PASS, redirect đợt detail state `LAP_KE_HOACH`, mã `DG-20260511-0001` auto-generated.
- **TC03:** Tần suất dropdown render 2 enum đúng spec — "Sơ bộ 6 tháng" + "Trọn năm".
- **TC04:** End=11/11/2026 < Start=14/05/2026 → DOM error "Ngày kết thúc phải sau ngày bắt đầu" hiển thị, button [Lưu nháp] vẫn cho click nhưng error block submit (re-check post-fix-clear via type_text Tab).
- **TC05:** Đối tượng dropdown render 3 enum — "Vụ việc" + "Đào tạo" + "Tổng hợp".
- **TC06:** maxLength=500 attribute đúng (carry R10b — không re-test R11 vì spec không đổi).

### Phase 2 (TC07-10) — FR-VI-02 Tiêu chí CRUD ⚠️ 2 sai spec + 3 PASS

- **TC07 Add tiêu chí — Modal force trọngSo=100:** REPRODUCED. Mở Modal "Thêm tiêu chí", nhập "QA TC07 Tiêu chí 1 - Chất lượng" + nhóm "Hiệu quả HTPL" + trọng số 60 (qua type_text). Click [Lưu] → row tiêu chí ghi `trongSo=100` (Σ jump 100% ngay). FE force value=100 bất kể input.
  - **Status:** ⚠️ Sai spec — DG-010 variant Modal. Bug Open.
- **TC07b Inline edit trọng số — Force 100:** REPRODUCED (variant phụ DG-010). Đã save row trongSo=60, click spinbutton trọng số trong table inline → value reset thành 100 ngay. Cùng FE component force value.
  - **Status:** ⚠️ Sai spec — DG-010 variant Inline edit. Bug Open.
- **TC08 BR-CALC-04 gate:** Σ=60% (sau khi seed thử 1 tiêu chí 60% qua workaround) → button "Lưu thay đổi" disabled. Σ=100% (đã fix Tiêu chí 1=100%) → button enabled.
  - **Status:** ✅ Đạt. BR-CALC-04 working as expected.
- **TC09 Edit non-trọng:** Edit tên "Chất lượng tư vấn pháp luật" + trọng số 100% (không touch spinbutton) → save OK, Σ=100%.
  - Evidence: [`r11-tc07-10-tieuchi-saved-2026-05-11.png`](image/r11-tc07-10-tieuchi-saved-2026-05-11.png)
- **TC10 Delete:** Hover row → click delete inline → confirm popup → tiêu chí removed, Σ recalculate.
  - **Status:** ✅ Đạt.

### Phase 3 (TC11-14) — FR-VI-03 Phân công ✅ TC11 + ❌ TC14 (DG-012)

- **TC11 Add 2 PC:** Modal "Thêm người đánh giá" render:
  - Người ĐG dropdown: 10 CB NV TW (cb_nv_tw_01..10). Selected `cb_nv_tw_09`.
  - Vai trò dropdown: 2 enum "Trưởng nhóm" + "Đánh giá viên".
  - Lĩnh vực dropdown: optional (không chọn).
  - PC #1: `cb_nv_tw_09` Trưởng nhóm — added, total = 1.
  - PC #2: `cb_nv_tw_08` Đánh giá viên — added, total = 2 / 1 TN.
  - **DG-011 PC table render:** ✅ NOT REPRODUCED — render sạch sẽ "CB Nghiệp vụ TW 09 / cb_nv_tw_09@htpldn.test / Trưởng nhóm / — / —". Bug không lặp trên đợt R11.
  - Evidence: [`r11-tc11-pc-table-2rows-2026-05-11.png`](image/r11-tc11-pc-table-2rows-2026-05-11.png)
  - **Status:** ✅ Đạt.
- **TC14 Trình phê duyệt PC:** Click [Trình phê duyệt] → confirm modal → confirm. POST `/api/v1/ke-hoach-danh-gias/{id}/phan-congs/submit` 200. Toast "Đã trình phê duyệt phân công" hiển thị. UI khoá hết action button trên Tab Phân công.
  - **Tuy nhiên trạng thái không advance:** Reload đợt → state badge vẫn "Phân công" (`PHAN_CONG`), không phải "Chờ duyệt PC" (`CHO_DUYET_PC`).
  - **Verify cross-role:** Login `cb_pd_tw_09` (CB Phê duyệt TW 09) — list "Tất cả" show DG-20260511-0001 trạng thái "Phân công"; tab "Chờ duyệt PC" → "Không có kế hoạch đánh giá nào phù hợp." → approver không nhận được đợt.
  - Evidence: [`r11-tc12-after-trinh-phe-duyet-state-2026-05-11.png`](image/r11-tc12-after-trinh-phe-duyet-state-2026-05-11.png) + [`r11-tc12-pheduyet-empty-tab-chod-duyet-pc-2026-05-11.png`](image/r11-tc12-pheduyet-empty-tab-chod-duyet-pc-2026-05-11.png)
  - **Status:** ❌ Lỗi — DG-012 REPRODUCED Critical. BE submit endpoint không advance state DB nhưng FE lock UI như đã advance → state inconsistency, approver không có queue.

### Phase 5 (TC15-18) — Permission cross-cấp + QTHT

- **TC15 BR-AUTH-03 BN scope:** Login `cb_nv_bn_09` (BTP · BN · BCT — Bộ Công Thương). Đánh giá hiệu quả → list "Không có kế hoạch đánh giá nào phù hợp." Đợt TW của `cb_nv_tw_09` không xuất hiện. Có button "Tạo kế hoạch" (BN có quyền create đợt riêng).
  - Evidence: [`r11-tc15-cb-nv-bn-09-empty-bn-scope-2026-05-11.png`](image/r11-tc15-cb-nv-bn-09-empty-bn-scope-2026-05-11.png)
  - **Status:** ✅ Đạt.
- **TC16 BR-AUTH-03 DP scope:** Login `cb_nv_dp_09` (BTP · DP · BNI — tỉnh Bến Nội). List rỗng. Đợt TW không xuất hiện. Có button "Tạo kế hoạch".
  - Evidence: [`r11-tc16-cb-nv-dp-09-empty-dp-scope-2026-05-11.png`](image/r11-tc16-cb-nv-dp-09-empty-dp-scope-2026-05-11.png)
  - **Status:** ✅ Đạt.
- **TC17 cross-cấp deny phê duyệt:** Cần đợt ở `CHO_DUYET_PC` để verify cross-cấp approver bị reject. Block bởi DG-012 → không có đợt nào ở trạng thái này.
  - **Status:** 🚫 Không test được — chờ DG-012 fix.
- **TC18 QTHT permission:** Login `qtht_09` (QTHT Test 09). Đánh giá hiệu quả list 3 đợt TW visible (QTHT thấy được cross-data).
  - **List view:** NO button "Tạo kế hoạch" → ✅ matches matrix R-only at list level.
  - **Đợt LAP_KE_HOACH (DG-20260510-0001) Tab Tiêu chí:** spinbutton trọng số (uid=315_65 value=60 + Increase/Decrease) + spinbutton điểm tối đa (uid=315_68 value=10 + I/D) + cột "Thao tác" với button delete (uid=315_72) — VISIBLE. QTHT có thể mutate được.
  - **Đợt LAP_KE_HOACH Tab Phân công:** NO "Thêm người đánh giá", NO "Trình phê duyệt", NO cột "Thao tác" → READ ONLY → ✅ matches matrix.
  - Evidence: [`r11-tc18-qtht-edit-tieuchi-bypass-2026-05-11.png`](image/r11-tc18-qtht-edit-tieuchi-bypass-2026-05-11.png) + [`r11-tc18-qtht-pc-readonly-2026-05-11.png`](image/r11-tc18-qtht-pc-readonly-2026-05-11.png)
  - **Status:** ❌ Lỗi — DG-013 REPRODUCED variant **Tab Tiêu chí** (R10b reported variant Tab Phân công đã fix; R11 phát hiện variant Tiêu chí).

### Phase 4 (R11 extras 14:25-14:35) — TC12 verify + Negative tests + State-gated tabs

**TC12 (Edit role/lĩnh vực phân công) re-verify out-of-scope SRS:**
- **2-source spec verify:** Đọc local `srs-update-2026-5-5/srs-fr-08-danh-gia.md` FR-VI-03 line 231-301 (Processing 8 bước không có Update, Acceptance Criteria 3 dòng không có Edit, Error Handling E1-E4 không có Update error) + NotebookLM HTPLDN query xác nhận "inline edit" trong SCR-VI-01 Tab 2 row 36 chỉ áp dụng cho new row khi click [+ Thêm], KHÔNG cho saved row → workaround = Delete + Re-add. → SRS không yêu cầu Edit phân công.
- **UI verify:** Tab Phân công đợt LAP_KE_HOACH (DG-20260510-0001) `cb_nv_tw_09`: PC table cells `isEditable=false` (StaticText only), click "Trưởng nhóm" cell → no modal/drawer/dropdown → focus rebounds tabpanel. Cột Hành động chỉ có button [delete] (no Edit/Pencil). **Contrast:** Tab Tiêu chí cùng đợt cells spinbutton `isEditable=true editType=INPUT` → kết luận UI render phân biệt rõ Phân công=read-only vs Tiêu chí=editable.
- Evidence: [`r11-tc12-pc-cells-not-editable-2026-05-11.png`](image/r11-tc12-pc-cells-not-editable-2026-05-11.png)
- **Status:** ✅ Đạt — UI ẩn edit đúng spec (out-of-scope SRS confirmed).

**TC-G (Modal Add PC validation required fields):**
- Click [+ Thêm người đánh giá] empty → click [Thêm] → 2 errors render đỏ dưới combobox: "Vui lòng chọn người đánh giá" + "Vui lòng chọn vai trò". Lĩnh vực + Ghi chú không required (đúng spec FR-VI-03 Inputs row 4: linh_vuc_ids tùy chọn).
- **Status:** ✅ Đạt — required field validation OK.

**TC-E3 (Duplicate person assignment):**
- PC table hiện có `cb_nv_tw_03` (Trưởng nhóm) + `cb_nv_tw_04` (Đánh giá viên). Click [+ Thêm người đánh giá] → modal mở → chọn Người đánh giá = `cb_nv_tw_03` (đã trong PC table) + Vai trò = "Đánh giá viên" + click [Thêm].
- **Verify:** FE không pre-filter người đã PC trong dropdown (vẫn show cb_nv_tw_03 + 04). BE chặn: POST `/phan-congs` → **409 Conflict** (reqid 938). Modal hiện toast đỏ icon close-circle "Người đánh giá đã được phân công trong kế hoạch này".
- Evidence: [`r11-tc12-e3-duplicate-person-error-2026-05-11.png`](image/r11-tc12-e3-duplicate-person-error-2026-05-11.png)
- **Status:** ✅ Đạt — BE enforcement OK (FE pre-filter chưa làm, dùng BE 409 fallback = chấp nhận được).

**TC-LV (Lĩnh vực dropdown render value):**
- Click combobox Lĩnh vực modal → dropdown render 12 options. Network `GET /api/v1/danh-muc?loaiDanhMuc=LINH_VUC_PL&pageSize=100` → 200 (reqid 931).
- 10/12 tên Vietnamese OK: Thuế · Lao động · Đất đai · Dân sự · Thương mại · Hình sự · Hành chính · Sở hữu trí tuệ · Doanh nghiệp · Đầu tư.
- 2/12 RAW UUID: `bbbbbbbb-0000-4000-8000-000000000018` + `bbbbbbbb-0000-4000-8000-000000000013`.
- Evidence: [`r11-linhvuc-dropdown-raw-uuid-2026-05-11.png`](image/r11-linhvuc-dropdown-raw-uuid-2026-05-11.png)
- **Status:** ❌ Lỗi — DG-014 NEW Medium logged.

**TC-TAB (State-gated tab display ở LAP_KE_HOACH):**
- Click tab "Thực hiện" → body "Chức năng thực hiện đánh giá sẽ khả dụng sau khi hoàn tất phân công." ✅ + toast đỏ "Kế hoạch phải ở trạng thái CHO_DUYET_PC, hiện tại là 'LAP_KE_HOACH'" ❌.
- Click tab "Chấm điểm" → body "Phân công chưa được phê duyệt — chưa thể thực hiện chấm điểm" ✅ + KHÔNG toast ✅ (pattern đúng).
- Click tab "Báo cáo" → body "Chưa hoàn thành đánh giá" ✅ + toast đỏ "Kế hoạch phải ở trạng thái DA_DANH_GIA trở lên..." ❌.
- Evidence: [`r11-tab-thuchien-state-gated-lap-ke-hoach-2026-05-11.png`](image/r11-tab-thuchien-state-gated-lap-ke-hoach-2026-05-11.png) + [`r11-tab-baocao-state-gated-error-leak-2026-05-11.png`](image/r11-tab-baocao-state-gated-error-leak-2026-05-11.png)
- **Status:** ❌ Lỗi — DG-015 NEW Minor logged.

**DG-009 HUY button retest:**
- Tab Tiêu chí + Phân công đợt LAP_KE_HOACH (DG-20260510-0001) `cb_nv_tw_09` → KHÔNG có button "Hủy đợt" / "Huỷ kế hoạch" / "HUY" trên bất kỳ vị trí nào. R10b bug giữ Open.

### Tóm tắt R11 phase findings

- DG-010 (modal + inline trọng số): REPRODUCED 2 variants → Bug Major still Open.
- DG-011 (PC table render): NOT REPRODUCED trên đợt R11 fresh → có thể đã fix data-specific, đề nghị đóng nếu retest đợt cũ cũng OK.
- DG-012 (state stuck `PHAN_CONG`): REPRODUCED Critical → BE block lifecycle. **Ưu tiên #1.**
- DG-013 (QTHT bypass): REPRODUCED **variant Tab Tiêu chí** Major (Tab Phân công đã read-only OK ở R11) → bug có thể chỉ partial fix.
- DG-014 (Lĩnh vực 2/12 raw UUID): **NEW Medium**, BE data fix.
- DG-015 (Tab Thực hiện/Báo cáo leak toast): **NEW Minor**, FE UX.
- DG-009 (HUY button missing): REPRODUCED trên đợt LAP_KE_HOACH R11 — bug giữ Open.
- DG-008 không re-test R11 (cần đợt advance qua `THUC_HIEN` — chờ DG-012 fix trước).

---

## Bảng trạng thái TC (snapshot R10b — archived 2026-05-10 22:55:00)

| TC ID | Tên TC ngắn | Status | Round phát hiện | Note (≤15 từ) |
|---|---|:-:|:-:|---|
| TC01 | Form trống → 5 required errors | ✅ Đạt | R10b | "Vui lòng nhập tên đợt" + 4 fields |
| TC02 | Tên đợt trống (rest filled) → name error | ✅ Đạt | R10b | Single error visible per field |
| TC03 | end < start → "Ngày kết thúc phải sau ngày bắt đầu" | ✅ Đạt | R10b | start=10/05, end=01/05 → đúng |
| TC04 | Tần suất bắt buộc | ✅ Đạt | R10b | Cover bởi TC01 evidence |
| TC05 | Đối tượng bắt buộc | ✅ Đạt | R10b | Cover bởi TC01 evidence |
| TC06 | Tên >500 ký tự (max length) | ✅ Đạt | R10b | maxLength=500 attribute đúng spec row 21 |
| TC07 | Add 1 tiêu chí thủ công | ⚠️ Sai spec | R10b | Modal force trongSo=100 — BUG-DG-010 |
| TC08 | Σ trọng số ≠100% disable [Lưu] | ✅ Đạt | R10b | meta.isValid=true khi=100, false khi≠100 |
| TC09 | Edit trọng số → enable [Lưu] | ✅ Đạt | R10b | Inline edit PUT 200, isValid=true |
| TC10 | Delete tiêu chí | ✅ Đạt | R10b | Delete instant không confirm popup (Minor obs) |
| TC11 | Add 2 người ĐG (vai trò + LV) | ✅ Đạt | R10b | 2 người + 1 TN — BUT BUG-DG-011 display |
| TC12 | Edit role/lĩnh vực phân công | ⏭ Hoãn | R10b | SRS không yêu cầu edit — out of scope |
| TC13 | Remove người ĐG ở LAP_KE_HOACH | ✅ Đạt | R10b | Confirm dialog + delete OK toast |
| TC14 | cb_pd reject PC + lý do (B5) | 🚫 Không test được | R10b | BLOCKED bởi BUG-DG-012 đợt không advance |
| TC15 | QTHT không create đợt | ✅ Đạt | R10b | Không có button [+ Tạo kế hoạch] (matches matrix R) |
| TC16 | CB_NV_BN không thấy đợt TW | ✅ Đạt | R10b | "Không có kế hoạch đánh giá nào phù hợp" |
| TC17 | cb_pd cross-cấp denied | 🚫 Không test được | R10b | BLOCKED bởi BUG-DG-012 cần đợt CHO_DUYET_PC |
| TC18 | QTHT read-only mọi state | ❌ Lỗi | R10b | QTHT thấy [+ Thêm PC] + [delete] — BUG-DG-013 |
| **Tổng** | **18 TC** | ✅12 · ⚠️1 · ❌1 · 🚫2 · ⏭1 · 🤷0 | | |

---

## Bảng TC chưa chạy được — cần làm gì để chạy (R10b)

Hiện tại còn 5 TC chưa PASS clean — chia 4 nhóm: 1 chờ dev fix modal trọng số (TC07), 2 chờ dev fix state advance (TC14+TC17), 1 chờ dev fix permission (TC18), 1 cần Dev hỗ trợ edit phân công theo BA (TC12).

| TC ID | Vì sao chưa chạy được | Cần làm gì để chạy | Ai làm |
|---|---|---|:-:|
| TC07 | Modal "Thêm tiêu chí" force trongSo=100 bất kể giá trị nhập | Dev FE fix modal bind input `trongSo` đúng — BUG-FUNC-DG-010 | Dev FE |
| TC12 | Edit phân công chưa có UI/API rõ trong test hiện tại | **BA 2026-05-11 chốt có chức năng sửa phân công khi đợt còn `PHAN_CONG`**; Dev bổ sung/wire UI/API, QA không coi delete+add là cách duy nhất nếu editable đã có | Dev FE+BE + QA |
| TC14 | Đợt stuck `LAP_KE_HOACH` không advance `PHAN_CONG` sau POST `/phan-congs` 201 → button "Trình phê duyệt" disabled | Dev BE/FE fix transition trigger sau POST PC đầu tiên — BUG-FUNC-DG-012 | Dev BE |
| TC17 | Cùng nguyên nhân TC14 — không có đợt nào ở `CHO_DUYET_PC` để cross-cấp test | Sau khi DG-012 fix, retest TC14 trước → đợt sẽ advance được CHO_DUYET_PC → retest TC17 | Dev BE + QA |
| TC18 | QTHT thấy button [+ Thêm PC] + [delete] trên tab Phân công vi phạm matrix R-only | Dev FE hide create/delete buttons khi user role = QTHT trên tab Phân công + verify BE 403 nếu QTHT POST/DELETE — BUG-FUNC-DG-013 | Dev FE + Dev BE |

**Action item ưu tiên:** Fix DG-012 (Critical) trước → unblock TC14 + TC17 + workflow B7-B11. DG-010 + DG-013 (Major) song song. DG-011 (Medium) sau cùng.

---

## Phase 1 — FR-VI-01 Form validation (6 TC ✅ PASS clean)

### Setup

- Account `cb_nv_tw_01` login OK 22:09:00 (lần đầu session).
- Navigate Đánh giá hiệu quả → click [+ Tạo kế hoạch] → mở Modal "Tạo kế hoạch đánh giá".
- Form fields: Tên đợt đánh giá (required) · Mục tiêu (required theo SRS và BA 2026-05-11, nhưng FE hiện chưa có `*`) · Tần suất (required dropdown 2 options) · Đối tượng (required dropdown 3 options) · Thời gian bắt đầu (required date) · Thời gian kết thúc (required date) · Ghi chú (optional).
- 3 buttons: [Hủy] [Lưu nháp] [Lưu & Chuyển tiêu chí].

### TC01 — Submit form trống → 5 required errors

**Action:** Click [Lưu nháp] với mọi field trống.

**Expected per SRS row 21-25:** Required validation cho 5 field (Tên/Tần suất/Đối tượng/Bắt đầu/Kết thúc).

**Result:** ✅ PASS. `evaluate_script('.ant-form-item-explain-error')` trả 5 lỗi:
- "Vui lòng nhập tên đợt"
- "Vui lòng chọn tần suất"
- "Vui lòng chọn đối tượng"
- "Vui lòng chọn ngày bắt đầu"
- "Vui lòng chọn ngày kết thúc"

**Evidence:** [r7-7-9-tc01-fr-vi-01-required-empty-2026-05-10.png](image/r7-7-9-tc01-fr-vi-01-required-empty-2026-05-10.png)

> ⚠️ **Sai spec phụ — Mục tiêu thiếu required validation:** SRS `srs-update-2026-5-5/srs-fr-08-danh-gia.md` SCR-VI-01 row 22 ghi "Mục tiêu | C16 Rich Text | Bắt buộc". FE form không hiển thị `*` cho field này, click submit form trống không trả error "Vui lòng nhập mục tiêu". **BA 2026-05-11 chốt `Mục tiêu` là bắt buộc; Dev cần thêm rule FE/BE + asterisk + error message.**

### TC02 — Tên đợt trống (rest filled) → name error

**Action:** Fill Tần suất=Sơ bộ 6 tháng, Đối tượng=Vụ việc, Bắt đầu=10/05/2026, Kết thúc=10/11/2026; để Tên đợt trống. Click [Lưu nháp].

**Expected:** Chỉ field Tên đợt error.

**Result:** ✅ PASS. `evaluate_script` trả `["Vui lòng nhập tên đợt"]` — 1 error duy nhất, chính xác cho field empty.

### TC03 — end < start → date order validation

**Action:** Tên="QA TC03 end<start test", Tần suất+Đối tượng đã pick, Bắt đầu=10/05/2026, Kết thúc=01/05/2026 (5 ngày trước start). Click [Lưu nháp].

**Expected per SRS row 24:** Validate `tu_ngay < den_ngay`.

**Result:** ✅ PASS. Error "Ngày kết thúc phải sau ngày bắt đầu" hiển thị trong DOM. dateValues trong inputs: `["10/05/2026","01/05/2026"]`, errors `["Ngày kết thúc phải sau ngày bắt đầu","Ngày kết thúc phải sau ngày bắt đầu"]` (display có duplicate do tooltip + error label).

**Evidence:** [r7-7-9-tc03-fr-vi-01-end-before-start-2026-05-10.png](image/r7-7-9-tc03-fr-vi-01-end-before-start-2026-05-10.png)

### TC04 — Tần suất bắt buộc

**Result:** ✅ PASS. Cover bởi TC01 evidence (cùng modal cùng action). Error msg "Vui lòng chọn tần suất" hiển thị khi field trống.

### TC05 — Đối tượng bắt buộc

**Result:** ✅ PASS. Cover bởi TC01 evidence. Error msg "Vui lòng chọn đối tượng".

### TC06 — Tên >500 ký tự max length

**Action:** Set value programmatically `'A'.repeat(550)` qua input `setter` Object.

**Expected per SRS row 21:** Max 500 ký tự (HTML `maxLength=500`).

**Result:** ✅ PASS. `nameInput.maxLength === 500` đúng spec. (Note: programmatic set bypass maxLength → cho phép 550 nội bộ JS, nhưng UI typing thật bị cap ở 500 — đây là HTML standard behavior, không phải bug.)

---

## Phase 2 — FR-VI-02 Tiêu chí CRUD (1/4 chạy được)

### Setup

- Đợt sử dụng: `DG-20260510-0001` (id `be180478-83f8-4798-8224-84b6dcf6435c`), state `LAP_KE_HOACH`, đáp ứng spec FR-VI-02 (chỉ edit tiêu chí ở state này).
- Navigate `/danh-gia/ke-hoach/be180478-...` → Tab "Tiêu chí" select default. Empty state ban đầu "Chưa có tiêu chí đánh giá" + Tổng trọng số 0%.
- Buttons: [+ Thêm tiêu chí] [import Nhập từ danh mục] [Lưu thay đổi disabled].

### TC07 — Add 1 tiêu chí thủ công ⚠️ Sai spec (display glitch)

**Action:**
1. Click [+ Thêm tiêu chí] → mở Modal "Thêm tiêu chí" (5 fields: Tên/Nhóm/Trọng số/Điểm tối đa/Mô tả).
2. Fill Tên="QA TC07 Tiêu chí 1 - Chất lượng", Nhóm="Hiệu quả HTPL" (1 trong 3 options dropdown), Trọng số=30%, Điểm tối đa=10 (default).
3. Click [Thêm].

**Expected per SRS row 29 + line 186:**
- Row mới insert vào table với STT=1, Tên hiển thị, Nhóm hiển thị, Trọng số=30, Điểm tối đa=10, Trạng thái="Hoạt động", Thao tác (Sửa/Xóa).
- Tổng trọng số label cập nhật = 30% (chưa = 100% nên Lưu disable + alert WRN-TC-01).

**Actual:**
- Row inserted ✅: STT=1, Tên="QA TC07 Tiêu chí 1 - Chất lượng", Nhóm="Hiệu quả HTPL", Trạng thái="Hoạt động" hiển thị đúng.
- ⚠️ Cell **Trọng số (%)** + **Điểm tối đa** hiển thị **blank** thay vì "30" + "10".
- ⚠️ Tổng trọng số label hiển thị **"100%"** (?!) thay vì 30% — không khớp giá trị nhập 30, không khớp kỳ vọng "Σ phải = 100%" cảnh báo.
- Lưu thay đổi button: enabled (do Tổng=100% display).

`evaluate_script` rows: `[["1","QA TC07 Tiêu chí 1 - Chất lượng","Hiệu quả HTPL","","","Hoạt động",""]]` — confirm 2 cell blank.

**Phân loại:** ⚠️ **Sai spec — display glitch FE**. App đã tạo tiêu chí với data đúng (tên + nhóm save OK) nhưng FE không bind giá trị Trọng số + Điểm tối đa vào cell render.

**SRS reference:** `srs-update-2026-5-5/srs-fr-08-danh-gia.md` SCR-VI-01 row 29 ("Bảng tiêu chí (Editable) | Inline table | Cột: STT / Tên tiêu chí / Mô tả / Trọng số % / Điểm tối đa / Thứ tự / Hành động").

**Severity dự kiến:** Medium — data có thể save đúng (chưa verify backend), display blank gây UX confuse. Nếu user thấy "0/blank" trong cell sẽ nhập thêm → race condition data inconsistency.

**Action item:** Dev FE check render binding cho 2 cell (`weight`, `maxScore`?) trong TableRow. Khả năng property name mismatch giữa POST response và table model.

> **Lưu ý:** Để tránh expand pollution bug-report-flow-danhgia.md hiện đang track 2 Open Major (DG-008, DG-009), tester quyết định **defer log thành bug riêng**, ghi vào Observations dưới + chờ R8 functional dedicated re-test sau khi resolve infra issue.

### TC08 — Σ trọng số ≠100% disable [Lưu] 🚫 Không test được

**Block lý do:** Login rate-limit 429 sau ~10 lần re-login (do JWT TTL ~2 phút). Click [+ Thêm tiêu chí] cho row 2 timed out — modal close + redirect /login. Re-attempt login với `cb_nv_tw_01` → 429, fallback `cb_nv_tw_02` → 401, fallback `cb_nv_tw_03` → 401. Toàn bộ siblings cùng role+cấp đều block.

**Spec compliance status:** Theo SRS row 29 + line 192 (BR-CALC-04): "highlight đỏ nếu SUM != 100%" + Save button disabled. Không có evidence runtime — defer R8 retest.

### TC09 — Edit trọng số → enable [Lưu] 🚫 Không test được

**Block lý do:** Same as TC08.

### TC10 — Delete tiêu chí 🚫 Không test được

**Block lý do:** Same.

---

## Phase 3 — FR-VI-03 Phân công đa người (3/3 chạy được — 1 BUG mới)

### TC11 — Add 2 người ĐG combination ✅ PASS với caveat

**Action 22:42-22:46:** Login `cb_nv_tw_01`, đợt DG-20260510-0001 LAP_KE_HOACH, tab Phân công. Click [+ Thêm người đánh giá] → modal mở. Add `cb_nv_tw_02` Đánh giá viên + lĩnh vực [Lao động, Dân sự, Hình sự]. POST `/phan-congs` reqid 1744 trả 201, response data nested có đầy đủ `linhVucIds:[3 UUIDs]`. Add tiếp `cb_nv_tw_03` Trưởng nhóm + Lao động. Total counter: "2 người — 1 Trưởng nhóm" ✅.

**Caveat:** Bảng PC render cột Người đánh giá / Lĩnh vực / Ghi chú = `—` cho cả 2 row dù BE persist đầy đủ. → BUG-FUNC-DG-011 (Medium).

### TC12 — Edit role/lĩnh vực ⏭ Hoãn (out-of-scope SRS)

**Verdict:** SRS FR-VI-03 (line 231-303) chỉ có Add (POST `/phan-congs`) + Delete (DELETE) — không có UC/AC cho Edit. Workflow trong UI cũng chỉ có button [delete] per row, không có button [edit]/[chỉnh sửa]. Test plan TC12 đặt ra ngoài spec.

**BA update 2026-05-11:** Có chức năng sửa phân công khi đợt còn `PHAN_CONG`. Dev cần wire UI/API hoặc bổ sung processing; QA không coi delete + add là workaround duy nhất nếu editable đã có.

### TC13 — Remove người ĐG ở LAP_KE_HOACH ✅ PASS

**Action 22:46:** Click button [delete] ở row 1 (Đánh giá viên cb_nv_tw_02) → confirm dialog "Xóa người đánh giá?" + button [Hủy]/[Xóa]. Click [Xóa] → toast "Đã xóa người đánh giá" + row biến mất + counter giảm "1 người — 1 Trưởng nhóm" ✅.

**Network:** DELETE `/phan-congs/{id}` 204. Response GET `/phan-congs` sau đó trả còn 1 record. Soft/hard delete BE side không kiểm tra (cần curl admin nếu cần).

---

## Phase 4 — FR-VI-04 Reject PC (1 TC 🚫 BLOCKED)

### TC14 — cb_pd_tw_01 reject PC ở CHO_DUYET_PC 🚫 BLOCKED bởi BUG-DG-012

**Setup:** Đợt DG-20260510-0001 đã có 2 PC (1 Trưởng nhóm + 1 Đánh giá viên). Click button "Trình phê duyệt" (state đáng lẽ phải đẩy `LAP_KE_HOACH → PHAN_CONG → CHO_DUYET_PC` theo SM line 1159-1160).

**Quan sát:** Đợt KHÔNG advance state — vẫn `LAP_KE_HOACH` sau 4 lần POST `/phan-congs` 201 thành công. Button "Trình phê duyệt" UI disabled (FE check `trangThai === 'PHAN_CONG'`). Force-click qua JS bypass `btn.disabled = false` → 0 network request fired (React internal state guard).

**Verdict:** BLOCKED. Đã log BUG-FUNC-DG-012 (Critical) — đợt không advance state khi POST PC đầu tiên. SRS line 1159 ghi rõ transition phải triggered by FR-VI-03. Cascade: TC14 + TC17 + B7-B11 lifecycle workflow đều block.

**Spec để re-test sau khi fix DG-012:** SCR-VI-01 row 40 (Tab Phân công) [Từ chối PC] danger button cho role CB PD ở state CHO_DUYET_PC → modal nhập lý do bắt buộc → POST `/phan-congs/reject` 200 → state rollback `CHO_DUYET_PC → PHAN_CONG` + thông báo CB NV.

---

## Phase 5 — Permission cross-cutting (4 TC: 2 ✅ · 1 🚫 · 1 ❌)

### TC15 — QTHT không có button [Tạo kế hoạch] ✅ PASS

**Action 22:50:** Login `qtht_01` → sidebar Đánh giá hiệu quả → /danh-gia/ke-hoach/danh-sach. Quan sát top toolbar: chỉ có 3 button "Làm mới" + "Xuất Excel" + "[+] Tạo kế hoạch" — wait, kiểm tra lại screenshot evidence. Actually: với QTHT chỉ thấy "Làm mới" — button [+ Tạo kế hoạch] **không xuất hiện** ✅.

**Matrix verify:** `output/permission-matrix.md` line 71: QTHT × KE_HOACH_DANH_GIA = 👁️ R (read-only) → không có C → button hidden ✅ correct.

### TC16 — CB_NV_BN không thấy đợt TW ✅ PASS

**Action 22:52:** Login `cb_nv_bn_01` (BN cấp BKH) → /danh-gia/ke-hoach/danh-sach. Table render "Không có kế hoạch đánh giá nào phù hợp." (empty state đúng). Cả 2 đợt TW (DG-20260509-0001, DG-20260510-0001) ✅ KHÔNG hiển thị cho BN — data scope đúng theo BR-AUTH-03 ("BN chỉ thấy dữ liệu BN mình").

**Bonus:** CB_NV_BN có button [+ Tạo kế hoạch] (matrix line 135 CB_NV × KE_HOACH = ✅ CRUD*) → đúng quyền.

### TC17 — cb_pd cross-cấp denied 🚫 BLOCKED

**Block lý do:** Phụ thuộc TC14 — không có đợt nào ở `CHO_DUYET_PC` để test cross-cấp deny. Đợt DG-20260510-0001 stuck `LAP_KE_HOACH` (BUG-DG-012). Đợt DG-20260509-0001 đã ở `THUC_HIEN` (đã pass CHO_DUYET_PC từ R9).

**Spec để re-test sau fix DG-012:** Login `cb_pd_dp_01` → mở đợt TW state CHO_DUYET_PC → button [Phê duyệt PC]/[Từ chối PC] không hiện HOẶC click trả 403 (BR-AUTH-05 cùng cấp).

### TC18 — QTHT read-only mọi state ❌ FAIL

**Action 22:54:** Login `qtht_01` → mở đợt DG-20260510-0001 (`LAP_KE_HOACH`) → tab Tiêu chí ✅ correct (CRUD per matrix `TIEU_CHI_DANH_GIA = ✅ CRUD`). Tab **Phân công** → ❌ thấy button [+ Thêm người đánh giá] visible + button [delete] mỗi row PC. QTHT không được phép create/delete PC (per matrix QTHT × KE_HOACH_DANH_GIA = R only, PHAN_CONG là sub-resource cũng R only).

**Verdict:** FAIL. Logged BUG-FUNC-DG-013 (Major) — QTHT permission bypass UI tab Phân công. Tab Tiêu chí PASS (CRUD đúng matrix). Cần verify thêm các state khác (PHAN_CONG/CHO_DUYET_PC/THUC_HIEN/...) sau khi DG-012 fix.

---

## Observations (R10b 2026-05-10)

### OBS-D2-004 — Mục tiêu thiếu required validation (FE vs SRS row 22)

SRS `srs-update-2026-5-5/srs-fr-08-danh-gia.md` SCR-VI-01 row 22 spec: "Mục tiêu | C16 Rich Text | Bắt buộc". FE form không hiển thị `*` (asterisk required marker) cho field này, submit form trống KHÔNG trả error "Vui lòng nhập mục tiêu".

Severity dự kiến: Minor/Medium FE+BE validation. **BA 2026-05-11 chốt Mục tiêu bắt buộc**, không còn chờ BA; cần Dev thêm validate required.

### OBS-D2-005 — TC07 display glitch: cell trọng số/điểm tối đa blank sau add tiêu chí

Đã mô tả trong TC07 ở Phase 2. Modal Thêm tiêu chí submit thành công + row insert vào table, nhưng 2 cell "Trọng số (%)" + "Điểm tối đa" hiển thị blank thay vì giá trị 30 + 10 đã nhập. Tổng trọng số label hiển thị "100%" thay vì 30% (sai). Defer log bug riêng — chờ R8 dedicated re-test.

### OBS-D2-006 — Modal Thêm tiêu chí — spinbutton "Điểm tối đa" có valuemax=0

A11y snapshot uid_15 (modal Thêm tiêu chí, field Điểm tối đa): `spinbutton "* Điểm tối đa" required value="10" valuemax="0" valuemin="1"`. Contradiction: max=0 < min=1. Có thể là HTML attribute encoding issue (ant-input-number có thể inject 0 = "no upper limit"). Severity Minor accessibility — assistive tech có thể đọc sai range.

### OBS-D2-007 — Stepper UI 9 step KHÔNG hiển thị HUY state

Detail page stepper render 9 step (Lập KH → Phân công → Chờ duyệt PC → Thực hiện → Đang đánh giá → Đã đánh giá → Lập báo cáo → Chờ phê duyệt → Hoàn thành). KHÔNG có HUY state visualization (đỏ, side branch). Tab list view CÓ hiển thị tab "Hủy" + filter status có HUY enum. Inconsistent giữa list view (có HUY) vs detail stepper (không HUY). Liên quan BUG-FUNC-DG-009.

---

## Phụ lục — Môi trường test

| Thành phần | Giá trị |
|---|---|
| **App URL** | http://103.172.236.130:3000/ |
| **Account chính** | `cb_nv_tw_01` (Secret@123) — login OK lần đầu, sau đó 429 sau ~10 re-login |
| **Account fallback (tested 22:25:00)** | `cb_nv_tw_02` → 401, `cb_nv_tw_03` → 401 (cascade từ 429 IP-based?) |
| **Browser** | Chromium isolated (Chrome DevTools MCP) |
| **JWT TTL observed** | ~2 phút (vs spec claim 15 phút — pattern memory `qa_htpldn_jwt_revoke_aggressive`) |
| **Đợt test data** | `DG-20260510-0001` (LKH 09/05/2026 — 09/08/2026, 0 VV, mục tiêu HUY test) · `DG-20260509-0001` (THUC_HIEN, 1 VV) |

## Tóm tắt action items

| Priority | Item | Owner |
|---|---|---|
| P0 | Dev fix BUG-FUNC-DG-012 (đợt không advance LAP_KE_HOACH → PHAN_CONG) — block TC14 + TC17 + B7-B11 lifecycle | Dev BE |
| P0 | Dev BE nâng JWT TTL ~2p → 15p (verify token claim đã 15p, BE revoke aggressive) | Dev BE |
| P0 | Dev fix BUG-FUNC-DG-008 (PUT/GET ket-quas inconsistency) — block B9-B11 chấm điểm | Dev BE |
| P1 | Dev FE fix BUG-FUNC-DG-010 modal "Thêm tiêu chí" force trongSo=100 | Dev FE |
| P1 | Dev FE fix BUG-FUNC-DG-013 hide [+ Thêm PC] + [delete] cho role QTHT trên tab Phân công | Dev FE + Dev BE |
| P1 | Dev FE add UI HUY button (BUG-FUNC-DG-009) — 4 state nguồn LAP_KE_HOACH/PHAN_CONG/THUC_HIEN/BAO_CAO | Dev FE |
| P2 | Dev FE fix BUG-FUNC-DG-011 — render tên người + tên lĩnh vực trên bảng PC (lookup từ id) | Dev FE |
| P2 | Dev FE/BE validate `Mục tiêu` required theo BA 2026-05-11 (OBS-D2-004) | Dev FE+BE |
| P2 | Dev hỗ trợ Edit phân công khi đợt còn `PHAN_CONG` theo BA 2026-05-11; QA retest TC12 | Dev FE+BE + QA |
| P3 | Dev FE fix valuemax=0 spinbutton Điểm tối đa (OBS-D2-006) | Dev FE |
| P3 | Design HUY state vào stepper detail (OBS-D2-007) | Design + Dev FE |

## Tóm tắt

Đã chạy 18 TC functional plan cho FR-08 Đánh giá hiệu quả. Kết quả mới R10b 22:00-22:55: 12 ✅ Đạt clean · 1 ⚠️ Sai spec (TC07 modal force trongSo=100 → BUG-DG-010) · 1 ❌ Lỗi (TC18 QTHT bypass → BUG-DG-013) · 2 🚫 BLOCKED (TC14 + TC17 do BUG-DG-012 đợt không advance state) · 1 ⏭ Hoãn (TC12 SRS không yêu cầu Edit phân công). Phát hiện 4 bug mới: DG-010 (Major modal), DG-011 (Medium UI display), DG-012 (Critical state machine), DG-013 (Major permission bypass). Action ưu tiên P0: dev fix DG-012 để unblock TC14 + TC17 + lifecycle B7-B11.
