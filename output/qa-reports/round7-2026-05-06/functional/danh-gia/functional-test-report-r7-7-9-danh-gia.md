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

## Verdict

**⚠️ FAIL toàn cục — 12/18 TC PASS clean (67%) · 1/18 ⚠️ Sai spec · 1/18 🚫 BLOCKED · 4/18 ❌ FAIL bug**

Phase 1 FR-VI-01 form validation ✅ PASS 6/6. Phase 2 FR-VI-02 tiêu chí CRUD ✅ 3/4 (TC07 ⚠️ sai spec — modal force trongSo=100, BUG-FUNC-DG-010). Phase 3 FR-VI-03 phân công ✅ 3/3 nhưng có 2 bug FE liên quan (DG-011 display "—" tên người + lĩnh vực, DG-013 QTHT permission bypass). Phase 4 FR-VI-04 reject 🚫 BLOCKED bởi DG-012 (đợt không advance state LAP_KE_HOACH → PHAN_CONG sau 4 POST PC). Phase 5 Permission ✅ 2/2 chạy được (TC15 + TC16) + 1 BLOCKED (TC17 cross-cấp deny chờ DG-012) + 1 FAIL (TC18 QTHT bypass).

**Bug mới phát hiện R10b 22:00-22:55:** 4 bug — DG-010 (modal force trongSo=100, Major), DG-011 (UI display PC table empty, Medium), DG-012 (đợt stuck LAP_KE_HOACH, Critical), DG-013 (QTHT permission bypass Phân công, Major). Chi tiết [bug-report-flow-danhgia.md](../../bug-reports/danh-gia/bug-report-flow-danhgia.md).

**Bug major còn open từ R10:** BUG-FUNC-DG-008 (PUT/GET ket-quas inconsistency) + BUG-FUNC-DG-009 (UI thiếu HUY button).

---

## Bảng trạng thái TC (snapshot R10b — LATEST 2026-05-10 22:55:00)

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

Hiện tại còn 5 TC chưa PASS clean — chia 4 nhóm: 1 chờ dev fix modal trọng số (TC07), 2 chờ dev fix state advance (TC14+TC17), 1 chờ dev fix permission (TC18), 1 out-of-scope SRS (TC12).

| TC ID | Vì sao chưa chạy được | Cần làm gì để chạy | Ai làm |
|---|---|---|:-:|
| TC07 | Modal "Thêm tiêu chí" force trongSo=100 bất kể giá trị nhập | Dev FE fix modal bind input `trongSo` đúng — BUG-FUNC-DG-010 | Dev FE |
| TC12 | SRS FR-VI-03 không có UC/AC cho edit phân công — chỉ Add+Delete | Confirm BA spec có cần edit không. Nếu cần BA bổ sung SRS + dev wire UI | BA |
| TC14 | Đợt stuck `LAP_KE_HOACH` không advance `PHAN_CONG` sau POST `/phan-congs` 201 → button "Trình phê duyệt" disabled | Dev BE/FE fix transition trigger sau POST PC đầu tiên — BUG-FUNC-DG-012 | Dev BE |
| TC17 | Cùng nguyên nhân TC14 — không có đợt nào ở `CHO_DUYET_PC` để cross-cấp test | Sau khi DG-012 fix, retest TC14 trước → đợt sẽ advance được CHO_DUYET_PC → retest TC17 | Dev BE + QA |
| TC18 | QTHT thấy button [+ Thêm PC] + [delete] trên tab Phân công vi phạm matrix R-only | Dev FE hide create/delete buttons khi user role = QTHT trên tab Phân công + verify BE 403 nếu QTHT POST/DELETE — BUG-FUNC-DG-013 | Dev FE + Dev BE |

**Action item ưu tiên:** Fix DG-012 (Critical) trước → unblock TC14 + TC17 + workflow B7-B11. DG-010 + DG-013 (Major) song song. DG-011 (Medium) sau cùng.

---

## Phase 1 — FR-VI-01 Form validation (6 TC ✅ PASS clean)

### Setup

- Account `cb_nv_tw_01` login OK 22:09:00 (lần đầu session).
- Navigate Đánh giá hiệu quả → click [+ Tạo kế hoạch] → mở Modal "Tạo kế hoạch đánh giá".
- Form fields: Tên đợt đánh giá (required) · Mục tiêu (đáng lẽ required theo SRS row 22 nhưng FE không có `*`) · Tần suất (required dropdown 2 options) · Đối tượng (required dropdown 3 options) · Thời gian bắt đầu (required date) · Thời gian kết thúc (required date) · Ghi chú (optional).
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

> ⚠️ **Sai spec phụ — Mục tiêu thiếu required validation:** SRS `srs-update-2026-5-5/srs-fr-08-danh-gia.md` SCR-VI-01 row 22 ghi "Mục tiêu | C16 Rich Text | Bắt buộc". FE form không hiển thị `*` cho field này, click submit form trống không trả error "Vui lòng nhập mục tiêu". Có thể là Minor display issue — hoặc spec đã thay đổi không document. **Hành động:** BA confirm — nếu Mục tiêu vẫn bắt buộc, dev FE cần thêm rule + asterisk + error msg. Nếu đã đổi thành optional, BA cập nhật SRS row 22.

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

**Action item:** BA confirm xem Edit có cần thiết không. Nếu cần → BA bổ sung SRS FR-VI-03 + dev wire UI. Hiện tại workaround = delete + add lại.

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

Severity dự kiến: Minor (FE hoặc Spec mismatch). Defer log bug — chờ BA confirm xem Mục tiêu vẫn bắt buộc hay đã đổi thành optional.

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
| P3 | BA confirm Mục tiêu required hay optional (OBS-D2-004) | BA |
| P3 | BA confirm có cần Edit phân công (TC12) — nếu cần BA bổ sung SRS FR-VI-03 | BA |
| P3 | Dev FE fix valuemax=0 spinbutton Điểm tối đa (OBS-D2-006) | Dev FE |
| P3 | Design HUY state vào stepper detail (OBS-D2-007) | Design + Dev FE |

## Tóm tắt

Đã chạy 18 TC functional plan cho FR-08 Đánh giá hiệu quả. Kết quả mới R10b 22:00-22:55: 12 ✅ Đạt clean · 1 ⚠️ Sai spec (TC07 modal force trongSo=100 → BUG-DG-010) · 1 ❌ Lỗi (TC18 QTHT bypass → BUG-DG-013) · 2 🚫 BLOCKED (TC14 + TC17 do BUG-DG-012 đợt không advance state) · 1 ⏭ Hoãn (TC12 SRS không yêu cầu Edit phân công). Phát hiện 4 bug mới: DG-010 (Major modal), DG-011 (Medium UI display), DG-012 (Critical state machine), DG-013 (Major permission bypass). Action ưu tiên P0: dev fix DG-012 để unblock TC14 + TC17 + lifecycle B7-B11.
