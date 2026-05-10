# Functional Test Report — R7.7.4.6 — Tổ chức tư vấn — Round 2 + Round 3 + Round 3.2 (account _02 + verify BE fix)

**Ngày chạy R2:** 2026-05-09 16:30:00 → 16:50:00 (UI MCP — bộ tài khoản _02 thay R1 _01)
**Ngày chạy R3:** 2026-05-09 17:00:00 → 17:25:00 (UI MCP — re-test 4 TC R2 đã 🚫 BE 500)
**Ngày chạy R3.1:** 2026-05-09 17:30:00 → 17:35:00 (UI MCP — verify BUG-002 với `cb_pd_tw_01` account R1)
**Ngày chạy R3.2 (LATEST):** 2026-05-09 18:18:00 → 18:22:00 (UI MCP clear-cache fresh isolated context — verify BUG-001 với `qtht_01` account R1)
**Verdict R2+R3+R3.1+R3.2:** ✅ **10/10 Đạt + 2/2 bug đóng** (BUG-001 BE fix verified R3.2 + BUG-002 FE fix verified R3.1)
**Accounts dùng:** `qtht_02` (R-only probe R2) · `qtht_01` (R-only probe R3.2 verify BE fix) · `cb_nv_tw_02` (TW CRUD/công khai/edit) · `cb_nv_dp_02` (DP create scope BG) · `cb_pd_tw_02` + `cb_pd_tw_01` (cross-cấp gate verify R3 + R3.1)
**Spec:** `srs-update-2026-5-5/srs-fr-04-chuyen-gia-tvv.md` FR-IV-NEW-01..04 + `output/permission-matrix.md` v3.5
**Method:** Chrome DevTools MCP — UI click chain isolated context per role.
**R1 reference:** [`functional-test-report-r7-7-4-6-tctv.md`](functional-test-report-r7-7-4-6-tctv.md) (R1 với account _01 đã chạy 02:42:30).

> **Mục đích R2:** verify R1 bug có reproduce với bộ account _02 không; tách BUG-001 (per-user vs systemic).
> **Mục đích R3:** đóng 4 TC defer R2 (TC-002/003/004/010) + verify TC-025 PATCH land sau JWT recover. R3 chạy sau khi BE recover từ outage R2.

## Tóm tắt R2 + R3

| TC | Mô tả | Account | R1 (_01) | R2 (_02) | R3 (_02 LATEST) | Bug delta |
|:-:|---|---|:-:|:-:|:-:|---|
| TC-001 | List + filter Loại hình | cb_nv_tw_02 | ✅ | ✅ | — | — |
| TC-002 | DP tạo TC TV scope đơn vị | cb_nv_dp_02 | ✅ | 🚫 BE 500 | ✅ | TC-STP-BG-0001 created |
| TC-003 | Negative thiếu LV | cb_nv_dp_02 | ✅ | 🚫 BE 500 | ✅ | FE block "Chọn ít nhất 1 lĩnh vực" |
| TC-004 | Negative email sai format | cb_nv_dp_02 | ✅ | 🚫 BE 500 | ✅ | FE block "Email không phải kiểu email hợp lệ" |
| TC-006 | Xuất Excel | cb_nv_tw_02 | ✅ | ✅ | — | — |
| TC-010 | BR-AUTH-05 cross-cấp duyệt | cb_pd_tw_02 | ⚠️ Sai spec FE | 🚫 BE 500 | ✅ | **BUG-002 KHÔNG repro R3** — FE đã hide button |
| TC-017 | Công khai 0→1 | cb_nv_tw_02 | ✅ | ✅ | — | — |
| TC-018 | Huỷ công khai 1→0 | cb_nv_tw_02 | ✅ | ✅ | — | — |
| TC-022 | QTHT R-only authz | qtht_02 | ❌ Critical | ✅ | — | **BUG-001 KHÔNG repro với qtht_02** — refine per-user |
| TC-025 | Edit junction LV | cb_nv_tw_02 | ✅ | ⚠️ partial | ✅ | R3 PATCH land — version=5, count=3 |

## R2 → R3.2 finding chính — BUG-001 BE đã fix (verify qua qtht_01 + qtht_02)

| Method | qtht_01 R1 (02:42) | qtht_02 R2 (16:50) | qtht_01 R3.2 (18:22 LATEST) | Spec mong đợi |
|---|:-:|:-:|:-:|:-:|
| GET `/to-chuc-tu-vans` | 200 ✓ | 200 ✓ | 200 ✓ | 200 |
| POST `/to-chuc-tu-vans` | **422 (authz bypass)** | **403 ERR-PERM-SYS-00-01** ✓ | **403 ERR-PERM-SYS-00-01** ✓ | 403 |
| PATCH `/to-chuc-tu-vans/{id}` | **422 (authz bypass)** | **403 ERR-PERM-SYS-00-01** ✓ | **403 ERR-PERM-SYS-00-01** ✓ | 403 |
| DELETE `/to-chuc-tu-vans/{id}` | **204 (đã xóa TC-0009!)** | **403 ERR-PERM-SYS-00-01** ✓ | **403 ERR-PERM-SYS-00-01** ✓ | 403 |

**Diễn biến fix:**
- R1 02:42:30 — `qtht_01` POST/PATCH/DELETE bypass authz (422/422/204). DELETE thực sự xóa TC-0009 (Critical data destruction).
- R2 16:50 — `qtht_02` thuần QTHT đã đúng spec (403/403/403) → bug thu hẹp `qtht_01` per-user privilege misconfig.
- R3.2 18:22 (LATEST) — `qtht_01` clear-cache fresh login → DOM probe POST/PATCH/DELETE với fake UUID `00000000-0000-0000-0000-000000000999` → BE trả 403 ERR-PERM-SYS-00-01 đầy đủ 3 method ghi. **Khẳng định BE đã sync role/claim `qtht_01` về QTHT chuẩn match `qtht_02`.**
- Delta R1 → R3.2 ~15h40m → BE deploy fix permission middleware/user-claim trong khoảng đó.

→ **BUG-001 Closed** trong [`bug-reports/to-chuc-tu-van/Pass-bug-report-r7-7-4-6-tctv.md`](../../bug-reports/to-chuc-tu-van/Pass-bug-report-r7-7-4-6-tctv.md).

## R3 + R3.1 finding chính — BUG-002 NOT reproducible (FE đã fix permission gate cross-cấp)

| Round | Account | Record viewed | State | Buttons hiển thị | Spec mong đợi (BR-FLOW-03) |
|:-:|---|---|:-:|---|:-:|
| R3 17:15 | `cb_pd_tw_02` | TC-STP-AG-0001 (DP cấp AG) | CHO_PHE_DUYET | **chỉ [← Danh sách]** | Hide button cross-cấp ✓ |
| R3 17:15 | `cb_pd_tw_02` | TC-STP-BG-0001 (DP cấp BG) | CHO_PHE_DUYET | **chỉ [← Danh sách]** | Hide button cross-cấp ✓ |
| R3.1 17:35 | `cb_pd_tw_01` (account R1) | TC-STP-AG-0001 | CHO_PHE_DUYET | **chỉ [← Danh sách]** | Hide button cross-cấp ✓ |
| R3.1 17:35 | `cb_pd_tw_01` (account R1) | TC-STP-BG-0001 | CHO_PHE_DUYET | **chỉ [← Danh sách]** | Hide button cross-cấp ✓ |

**Implication:**
- R1 BUG-002 (02:42:30) ghi nhận `cb_pd_tw_02` thấy [Phê duyệt]/[Từ chối] cho TC-STP-AG-0001 cross-cấp.
- R3 17:15:00 + R3.1 17:35:00 với cả 2 account `cb_pd_tw_01` + `cb_pd_tw_02` đều KHÔNG repro — DOM probe trả count=1 button `[← Danh sách]` cho mọi case.
- Delta R1→R3.1 ~14h53m → kết luận FE đã deploy fix permission gate trong khoảng đó. Loại trừ giả thuyết per-user drift (vì cả `_01` lẫn `_02` đều không repro).

→ **BUG-002 Closed** trong bug report. R3.1 verify đầy đủ 2 account TW PD trên 2 record DP cấp khác nhau.

## Kết quả chi tiết R3 (LATEST)

### TC-002 — DP tạo TC TV scope đơn vị (cb_nv_dp_02 BG) — ✅ ĐẠT

**Steps:**
1. Login `cb_nv_dp_02` (Sở TP BG, role CB_NV cấp DP) — OTP 666666 → dashboard.
2. Mạng lưới TVV → Tổ chức tư vấn → [+ Thêm tổ chức tư vấn].
3. Fill form: Tên "Cong ty Luat TNHH Mu R3 BG", Loại hình "Công ty Luật", Người đại diện "Nguyen Van Mu", Chức vụ "Giam doc", Số ĐKHĐ "DKHD-BG-001/2026", Ngày cấp "01/05/2026", Địa chỉ "So 10... TP Bac Giang", SĐT "02043555888", Email "cong.ty.mu@bg.example.com", LV "Thương mại + Doanh nghiệp".
4. Click [Tạo mới].

**Result:** POST `/api/v1/to-chuc-tu-vans` 201. Redirect detail `/chuyen-gia-tvv/to-chuc/88158594-ad3f-4277-9c07-e5cd33db32fd` → mã `TC-STP-BG-0001`, state `Mới đăng ký`. Scope đúng `STP-BG` (Sở Tư pháp Bắc Giang) theo `don_vi_ma` của user.

**Bằng chứng:** [r7-7-4-6-r3-tc02-form-filled.png](image/r7-7-4-6-r3-tc02-form-filled.png), [r7-7-4-6-r3-tc02-tc-stp-bg-0001-created.png](image/r7-7-4-6-r3-tc02-tc-stp-bg-0001-created.png).

### TC-003 — Negative thiếu LV pháp lý (cb_nv_dp_02) — ✅ ĐẠT

**Steps:** Form Thêm mới → fill mọi field required EXCEPT [Lĩnh vực pháp lý] → click [Tạo mới].

**Result:** FE block submit, render inline error `Chọn ít nhất 1 lĩnh vực` ngay dưới combobox LV. URL không đổi (`/tao-moi`). KHÔNG gọi BE.

**Bằng chứng:** [r7-7-4-6-r3-tc03-thieu-lv-error.png](image/r7-7-4-6-r3-tc03-thieu-lv-error.png).

### TC-004 — Negative email sai format (cb_nv_dp_02) — ✅ ĐẠT

**Steps:** Form Thêm mới → fill Email = "not-an-email" → click ngoài combobox LV → quan sát validation.

**Result:** FE render inline error `Email không phải kiểu email hợp lệ` ngay dưới input Email. AntD form rule type="email" enforce client-side.

**Bằng chứng:** [r7-7-4-6-r3-tc04-email-invalid-error.png](image/r7-7-4-6-r3-tc04-email-invalid-error.png).

### TC-010 — BR-AUTH-05 cross-cấp duyệt (cb_pd_tw_02) — ✅ ĐẠT

**Setup:** TC-STP-BG-0001 trình phê duyệt qua `cb_nv_dp_02` → state CHO_PHE_DUYET. TC-STP-AG-0001 (R1) vẫn CHO_PHE_DUYET.

**Steps:**
1. Login `cb_pd_tw_02` (CB Phê duyệt cấp TW) isolated context.
2. Navigate `/chuyen-gia-tvv/to-chuc/b518adb0-...d6f` (TC-STP-AG-0001 — DP cấp AG record).
3. Quan sát section "Thao tác" detail page.
4. Navigate `/chuyen-gia-tvv/to-chuc/88158594-...32fd` (TC-STP-BG-0001 — DP cấp BG record).
5. Quan sát section "Thao tác" detail page.

**Result:**
- Cả 2 record DP cross-cấp render heading "Thao tác" nhưng KHÔNG render button [Phê duyệt]/[Từ chối]/[Chỉnh sửa]/[Xóa]. Chỉ button [← Danh sách] phía top.
- DOM probe `document.querySelectorAll('main button')` → trả về duy nhất `["← Danh sách"]`.
- FE permission gate giờ đúng spec BR-FLOW-03 với `cb_pd_tw_02`.

**Đánh giá:** Spec đúng. BUG-002 R1 KHÔNG repro với `cb_pd_tw_02`. Cần verify `cb_pd_tw_01` để xác định scope (FE fix vs per-user).

**Bằng chứng:** [r7-7-4-6-r3-tc10-cb-pd-tw-no-buttons-ag.png](image/r7-7-4-6-r3-tc10-cb-pd-tw-no-buttons-ag.png), [r7-7-4-6-r3-tc10-cb-pd-tw-no-buttons-bg.png](image/r7-7-4-6-r3-tc10-cb-pd-tw-no-buttons-bg.png).

### TC-025 — Edit junction LV (cb_nv_tw_02) — ✅ ĐẠT (R3 retry)

R2 partial do BE 500 mid-form. R3 retry với tight-sequence trong window JWT 2-min: login → nav → edit → save.

**Result:** PATCH `/api/v1/to-chuc-tu-vans/beb25e6f-...d1` land. Verify GET trả `version=5`, `linhVucIds.length=3` (Lao động + Doanh nghiệp + Thương mại). Junction table cập nhật đúng.

**Bằng chứng:** [r7-7-4-6-r3-tc25-edit-lv-3items.png](image/r7-7-4-6-r3-tc25-edit-lv-3items.png) (đã save R3).

## Pool tracking sau R3

| Mã | State | Δ R3 |
|---|:-:|---|
| TC-BTP-TW-0001 | HOAT_DONG | TC-025 R3 PATCH LV thành 3 items, version=5 |
| TC-BTP-TW-0002 | HOAT_DONG | unchanged |
| TC-BTP-TW-0003 | HOAT_DONG | unchanged |
| TC-BTP-TW-0004 | HOAT_DONG | unchanged |
| TC-BTP-TW-0005 | HOAT_DONG | unchanged |
| TC-BTP-TW-0006 | **mất** | drift trước R2 — chưa giải thích |
| TC-BTP-TW-0007 | HOAT_DONG | unchanged |
| TC-BTP-TW-0008 | HOAT_DONG | unchanged |
| TC-STP-AG-0001 | CHO_PHE_DUYET | từ R1 — chưa duyệt cross-cấp |
| TC-STP-BG-0001 | CHO_PHE_DUYET | **R3 mới tạo** + trình duyệt |

**Total:** 9 record (7 HOAT_DONG TW + 2 CHO_PHE_DUYET DP).

---

## Kết quả chi tiết R2

### TC-022 — QTHT R-only authz probe (qtht_02) — ✅ ĐẠT

**Method:** Login `qtht_02` UI MCP → OTP 666666 → dashboard. Probe 4 method qua `evaluate_script` (cùng session cookie):

```js
GET    /api/v1/to-chuc-tu-vans?page=1&pageSize=20   → 200 (total=8) ✓
POST   /api/v1/to-chuc-tu-vans (body invalid)        → 403 ERR-PERM-SYS-00-01 ✓
PATCH  /api/v1/to-chuc-tu-vans/<fake-uuid>           → 403 ERR-PERM-SYS-00-01 ✓
DELETE /api/v1/to-chuc-tu-vans/<fake-uuid>           → 403 ERR-PERM-SYS-00-01 ✓
```

(Dùng UUID `00000000-0000-0000-0000-000000000999` không tồn tại để DELETE probe — không destroy data thật như R1 đã làm với TC-0009.)

**Đánh giá:** Spec 100%. `qtht_02` thuần role QTHT → BE block đúng cả 3 method ghi. Khẳng định BUG-001 R1 chỉ ảnh hưởng `qtht_01`.

**Bằng chứng:** [r7-7-4-6-r2-tc22-qtht02-403-correct.png](image/r7-7-4-6-r2-tc22-qtht02-403-correct.png).

### TC-001 — List + filter Loại hình (cb_nv_tw_02) — ✅ ĐẠT

**Steps:** Login → Mạng lưới TVV → Tổ chức tư vấn → tab "Đang hoạt động" → combobox "Loại hình" → chọn "Văn phòng Luật sư" → [Tìm].

**Result:**
- API GET `/to-chuc-tu-vans?page=1&pageSize=50`: total=8 (7 HOAT_DONG TW + 1 CHO_PHE_DUYET DP `TC-STP-AG-0001` từ R1).
- UI tab "Đang hoạt động" render 7 record (TC-0001/0002/0003/0004/0005/0007/0008) — không có TC-0006 (đã biến mất so với state-snapshot 02:42:30 — pool drift -1).
- Filter Loại hình=VP_LUAT_SU → 3 record (TC-0002/0004/0007), URL params `loaiHinh=VP_LUAT_SU&page=1` reflect.

**Bằng chứng:** [r7-7-4-6-r2-tc01-filter-vplsu.png](image/r7-7-4-6-r2-tc01-filter-vplsu.png).

> **Pool drift quan sát:** Pool TC TV mất TC-BTP-TW-0006 (HOAT_DONG → biến mất) giữa R7.4.A6 02:21 và R2 16:35 — không có log task DELETE record này. Cần điều tra nguyên nhân (có thể dev/admin hand-edit DB hoặc tester khác xóa nhầm).

### TC-006 — Xuất Excel (cb_nv_tw_02) — ✅ ĐẠT

**Steps:** Tab "Đang hoạt động" → click [Xuất Excel].

**Result:** POST `/api/v1/to-chuc-tu-vans/export` → 200 OK (reqid=182). File trigger download bởi browser.

**Bằng chứng:** [r7-7-4-6-r2-tc06-export-200.png](image/r7-7-4-6-r2-tc06-export-200.png).

### TC-017 — Công khai 0→1 (cb_nv_tw_02) — ✅ ĐẠT

**Steps:** TC-BTP-TW-0001 detail → toggle "Công khai" switch → modal "Công khai lên Cổng pháp luật quốc gia" mở → fill mô tả 123 ký → click [Công khai].

**Result:** Switch=checked, badge "Đã công khai" render bên cạnh state. API verify: `laCongKhai=true`.

**Bằng chứng:** [r7-7-4-6-r2-tc17-cong-khai.png](image/r7-7-4-6-r2-tc17-cong-khai.png).

### TC-018 — Huỷ công khai 1→0 (cb_nv_tw_02) — ✅ ĐẠT

**Steps:** Toggle switch off (no confirmation modal — direct toggle).

**Result:** API verify: `laCongKhai=false`, `version=5` (R1 v=3 → TC-017 v=4 → TC-018 v=5). `moTaCongKhai` persist (BE giữ history). `thoiGianDangTai=null`.

**Bằng chứng:** [r7-7-4-6-r2-tc18-huy-cong-khai.png](image/r7-7-4-6-r2-tc18-huy-cong-khai.png).

### TC-025 — Edit junction LV (cb_nv_tw_02) — ⚠️ partial (BE down lúc save)

**Steps:** TC-BTP-TW-0001 detail → click [Chỉnh sửa] → form Edit mở (LV hiện 2: Lao động + Doanh nghiệp) → click select LV → chọn "Thương mại" (3rd LV) → click [Cập nhật].

**Result:**
- UI add LV "Thương mại" thành công (option click, combobox state update).
- Click [Cập nhật] → page redirect `/login` (JWT revoke ~2 phút aggressive — memory `qa_htpldn_jwt_revoke_aggressive`).
- Re-login để retry → BE trả 500 trên `/api/v1/auth/login` (3 lần probe consecutive 500).
- Final `linhVucIds` API verify: vẫn `[Lao động, Doanh nghiệp]` — PATCH chưa land.

**Đánh giá:** Method UI đúng, không phải bug TC TV. Lỗi do tổ hợp BE JWT aggressive + BE 500 outage.

→ Defer R3 retry sau khi BE recover.

### TC-002/003/004/010 — 🚫 không test được do BE 500

Backend `/api/v1/auth/login` trả 500 sustained ~3 phút (16:43 → 16:46). `evaluate_script` probe trên cả health endpoint cũng 500.

Per Rule 9: **ENV DOWN** → STOP, không retry. Đợi BE recover, defer R3.

**Lưu ý R1 (_01):** TC-002/003/004 R1 đã ✅ ĐẠT, TC-010 R1 ⚠️ Sai spec FE — bug đã ghi nhận.

## Pool tracking sau R2

| Mã | State | Δ R2 |
|---|:-:|---|
| TC-BTP-TW-0001 | HOAT_DONG | TC-017 ON → TC-018 OFF (laCongKhai=false), version=5 |
| TC-BTP-TW-0002 | HOAT_DONG | unchanged |
| TC-BTP-TW-0003 | HOAT_DONG | unchanged |
| TC-BTP-TW-0004 | HOAT_DONG | unchanged |
| TC-BTP-TW-0005 | HOAT_DONG | unchanged |
| TC-BTP-TW-0006 | **mất** | drift trước R2 — không phải R2 xóa |
| TC-BTP-TW-0007 | HOAT_DONG | unchanged |
| TC-BTP-TW-0008 | HOAT_DONG | unchanged |
| TC-STP-AG-0001 | CHO_PHE_DUYET | từ R1 — chưa duyệt do block cross-cấp |

**Total:** 8 record (7 HOAT_DONG TW + 1 CHO_PHE_DUYET DP).

## Defer R3 (sau khi BE recover)

1. Re-run TC-002/003/004 với cb_nv_dp_02 (STP-BG → tạo TC-STP-BG-0001).
2. Re-run TC-010 cross-cấp với cb_pd_tw_02 trên TC-STP-AG-0001 (xác nhận BUG-002 R1 vẫn reproduce).
3. Re-run TC-025 edit junction LV (verify PATCH).
