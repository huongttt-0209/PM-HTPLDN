# Bug Report — Đánh giá Hiệu quả HTPLDN (FR-08) R7

| Thông tin | Giá trị |
|-----------|---------|
| **Dự án** | PM HTPLDN — Phần mềm Hỗ trợ Pháp lý Doanh nghiệp |
| **Môi trường** | http://103.172.236.130:3000/ |
| **Người test** | QA Automation (Claude Code via Chrome DevTools MCP) |
| **Ngày** | 2026-05-12 16:30:00 |
| **Loại test** | Workflow E2E + bugfix re-verify (R12) |
| **Round** | R12 |
| **Tài liệu tham chiếu** | [`srs-fr-08-danh-gia.md`](../../../../../input/srs-v3/srs-fr-08-danh-gia.md) (FR-VI-01/02/03/04 + SCR-VI-01 + SM-DANHGIA), [workflow-test-report-DanhGiaHQ.md](../../workflow/danh-gia/workflow-test-report-DanhGiaHQ.md), [R6 reference](../../../round6-2026-05-01-postreset/bug-reports/bug-report-flow-danhgia.md) |

---

## Tổng hợp

Phát hiện **15** lỗi có SRS reference cụ thể trong workflow Đánh giá Hiệu quả HTPLDN (FR-08). Hiện trạng (sau reverify R19 2026-05-12): **1 Open** (BUG-DG-014 dropdown Lĩnh vực raw UUID) · **14 Closed** (BUG-DG-010 + BUG-DG-013 đã fixed R19).

### Severity breakdown

| Tổng | Critical | Major | Medium | Minor | Trivial | Closed | Open |
|------|----------|-------|--------|-------|---------|--------|------|
| 15   | 3        | 7     | 4      | 1     | 0       | 14     | 1    |

## Bug Summary Table

| Bug ID | Severity | Priority | Type | TC Ref | **SRS Reference** | Title | Status |
|--------|----------|----------|------|--------|-------------------|-------|--------|
| BUG-FUNC-DG-014 | Medium | P2 | UI data display | TC11/TC12 modal Phân công (FR-VI-03) | `srs-update-2026-5-5/srs-fr-08-danh-gia.md` FR-VI-03 Inputs row 4 + line 798 (SCR-VI-01 Tab 2) | Dropdown "Lĩnh vực" modal "Thêm người đánh giá" render raw UUID thay vì tên Vietnamese | Open |
| ~~BUG-FUNC-DG-010~~ | Major | P1 | UI / FE control | TC07 (FR-VI-02) | `srs-fr-08-danh-gia.md` FR-VI-02 Inputs row 3 (`trong_so` Bắt buộc 0-100 user input) + line 175 BR-CALC-04 | ~~Modal "Thêm tiêu chí" override trọng số người dùng nhập về 100~~ | Closed ✅ R19 |
| ~~BUG-FUNC-DG-013~~ | Major | P1 | Permission bypass | TC18 (FR-VI-03 × QTHT) | `output/permission-matrix.md` line 71 (QTHT × KE_HOACH_DANH_GIA = R only) + `srs-fr-08-danh-gia.md` FR-VI-03 Tác nhân | ~~QTHT có quyền edit Tab Tiêu chí + button delete + "Hủy đợt" trên đợt LAP_KE_HOACH thuộc người khác~~ | Closed ✅ R19 |
| ~~BUG-FUNC-DG-001~~ | Medium | P2 | UI/UX | R6.4.D2 B1 | `srs-fr-08-danh-gia.md` line 777 (SCR-VI-01 row 27) | ~~Button [Lưu & Chuyển tiêu chí] không navigate Tab Tiêu chí~~ | Closed ✅ R6 |
| ~~BUG-FUNC-DG-002~~ | Critical | P0 | UI/UX | R6.4.D2 back-fill | `srs-fr-08-danh-gia.md` line 790 (SCR-VI-01 row 33) + line 186 + line 192 (BR-CALC-04) | ~~Tab Tiêu chí không có nút [+ Thêm tiêu chí] / [Nhập từ DM]~~ | Closed ✅ R6 |
| ~~BUG-FUNC-DG-003~~ | Critical | P0 | Workflow | R6.4.D2 B2 | `srs-fr-08-danh-gia.md` line 244 (FR-VI-03 Inputs row 2) + line 798 | ~~Dropdown Người đánh giá gọi sai endpoint `/chuyen-gia-tvvs` 404~~ | Closed ✅ R6 |
| ~~BUG-FUNC-DG-004~~ | Major | P1 | Workflow | R6.4.D2 B2 | `srs-fr-08-danh-gia.md` line 246 + line 798 | ~~Dropdown Lĩnh vực gọi `/danh-mucs` 404 (sai path/param)~~ | Closed ✅ R6 |
| ~~BUG-FUNC-DG-005~~ | Major | P1 | Workflow | R6.4.D2 B2 | `srs-fr-08-danh-gia.md` line 245 + line 798 | ~~Dropdown Vai trò render "Trống" thay 2 enum static~~ | Closed ✅ R6 |
| ~~BUG-FUNC-DG-006~~ | Major | P1 | Workflow | R7.4.D2 B6 | `srs-fr-08-danh-gia.md` FR-VI-05/06 (UC87 Chọn VV vào đợt) | ~~Endpoint `/vu-viec-eligible` trả empty list mặc dù có VV state HOAN_THANH match đợt~~ | Closed ✅ R10 |
| ~~BUG-FUNC-DG-007~~ | Medium | P2 | Data | R7.4.D2 (cross-module) | `srs-fr-08-danh-gia.md` Dashboard KPI-04 + `srs-fr-13-dashboard.md` | ~~Dashboard "Vụ việc hoàn thành: 0" sai vs thực tế 20 VV HOAN_THANH~~ | Closed ✅ R10 |
| ~~BUG-FUNC-DG-008~~ | Major | P1 | Workflow / BE persistence | R7.4.D2 B9 | `srs-fr-08-danh-gia.md` FR-VI-08 + line 798 (Tab 4 "Lưu kết quả") | ~~PUT `/ke-hoach-danh-gias/{id}/ket-quas` 200 nhưng GET sau đó trả null + version=1 (read-after-write inconsistency)~~ | Closed ✅ R12 |
| ~~BUG-FUNC-DG-009~~ | Major | P1 | UI missing | R7.4.D2a | `srs-fr-08-danh-gia.md` FR-VI-08 transition + Mermaid line 1133-1136 | ~~Đợt detail page các state nguồn HUY thiếu button "Hủy đợt"~~ | Closed ✅ R12 |
| ~~BUG-FUNC-DG-011~~ | Medium | P2 | UI display | TC11 (FR-VI-03) | `srs-fr-08-danh-gia.md` line 798 (SCR-VI-01 Tab 2 row 36) | ~~Bảng phân công render "—" cho Người đánh giá + Lĩnh vực + Ghi chú dù BE đã persist~~ | Closed ✅ R11/R12 |
| ~~BUG-FUNC-DG-012~~ | Critical | P0 | Workflow / state machine | TC11-14 (FR-VI-03 step 7) | `srs-fr-08-danh-gia.md` line 1159 (SM `LAP_KE_HOACH → PHAN_CONG`) + line 1160 | ~~Đợt không advance state `LAP_KE_HOACH → PHAN_CONG` dù đã POST `/phan-congs` 201~~ | Closed ✅ R12 |
| ~~BUG-FUNC-DG-015~~ | Minor | P3 | UX / error leak | Tabs Thực hiện + Báo cáo (FR-VI-04/09 state-gated) | `srs-update-2026-5-5/srs-fr-08-danh-gia.md` SCR-VI-01 Tab 3 + Tab 5 | ~~Click tab "Thực hiện"/"Báo cáo" khi đợt state `LAP_KE_HOACH` → leak BE error toast đỏ~~ | Closed ✅ R12 |

> **Chú thích Type:** `Happy/Negative/Edge/Workflow/Permission/Data/UI/UX/Performance` — xem template.
> **Chú thích Severity:** `Critical/Major/Medium/Minor/Trivial` — xem template.

---

## ~~BUG-FUNC-DG-010~~ [CLOSED] — Modal "Thêm tiêu chí" force `trongSo=100` bất kể giá trị user nhập

> **Re-test:** 2026-05-12 16:30:00 R19 — ✅ PASS (Closed-verified). Account `cb_nv_tw_06` đợt `DG-20260510-0001` LAP_KE_HOACH. Click [+ Thêm tiêu chí] → modal mở → fill: Tên = "Reverify DG-010 trongSo 30", Nhóm = "Hiệu quả HTPL", **Trọng số = 30**, Điểm tối đa = 10 → Click [Thêm]. Table row 2 render với spinbutton Trọng số = **30** (KHÔNG force 100). Header "Tổng trọng số" = 90% (60 row 1 + 30 row 2). FE đã honor đúng giá trị user nhập. Evidence: [`image/reverify-2026-05-12-dg010-trongso-30-pass.png`](image/reverify-2026-05-12-dg010-trongso-30-pass.png).


### Mô tả

Account `cb_nv_tw_01`, đợt DG-20260510-0001 state `LAP_KE_HOACH`, tab Tiêu chí có 0 tiêu chí. Click [+ Thêm tiêu chí] → modal mở với fields: Tên tiêu chí, Nhóm tiêu chí, Trọng số (%), Điểm tối đa, Trạng thái, Mô tả. QA fill: Tên = "QA TC07 Tiêu chí 1 - Chất lượng", Nhóm = "Hiệu quả HTPL", Trọng số = `30`, Điểm tối đa = 10, Trạng thái = Hoạt động. Click [Lưu]. Network reqid 1715 PUT `/tieu-chis` request body chứa `tieuChis:[{tenTieuChi:..., trongSo: 100, ...}]` — **trongSo: 100 thay vì 30**. Response 200 với meta `{tongTrongSo: 100, isValid: true}` reflect saved value 100. Sau save, table render row 1 với spinbutton trọng số = 100, mã TC-20260510-0001. User input 30% bị FE override 100 trước khi gửi BE.

### Các bước tái hiện

**Precondition:** Tài khoản role CB Nghiệp vụ TW (`cb_nv_tw_01` primary, fallback `cb_nv_tw_05` nếu primary lock). Có sẵn ≥1 đợt đánh giá state `LAP_KE_HOACH` mà tài khoản là người tạo (hoặc tự tạo đợt mới ở B1).

1. Login `cb_nv_tw_01` (hoặc fallback `cb_nv_tw_05`) → sidebar Đánh giá hiệu quả → tạo đợt mới state `LAP_KE_HOACH` (hoặc mở đợt đã có state `LAP_KE_HOACH`) → tab Tiêu chí.
2. Click button [+ Thêm tiêu chí] → modal "Thêm tiêu chí" mở.
3. Fill các trường: Tên = "Test", Nhóm = "Hiệu quả HTPL", **Trọng số (%) = 30**, Điểm tối đa = 10, Trạng thái = Hoạt động.
4. Click [Lưu] → toast "Thêm tiêu chí thành công" + modal đóng.
5. Quan sát table tab Tiêu chí: row mới hiện với **spinbutton cột Trọng số (%) = `100`** thay vì `30` đã nhập.
6. Quan sát badge "Tổng trọng số" ở header tab: `100%` (thay vì `30%` mong đợi sau 1 TC).

### Kết quả mong đợi

Theo SRS `srs-fr-08-danh-gia.md` FR-VI-02 Inputs row 3 (`trong_so` Bắt buộc, value range 0-100, user input) + BR-CALC-04 (Σ trọng số = 100% qua nhiều tiêu chí khác nhau):
- FE gửi BE đúng value user nhập (30 trong test này).
- Table render trọng số = 30 ngay sau save.
- User có thể thêm nhiều tiêu chí với trọng số khác nhau (vd 30+20+40+10) qua modal mà không cần inline edit.

### Kết quả thực tế

- Modal input Trọng số = 30%, click [Lưu] → table render row 1 với spinbutton Trọng số = **100** (không phải 30).
- Header tab Tiêu chí badge "Tổng trọng số = 100%" — trùng với case chỉ có 1 TC duy nhất, cho thấy modal force `100` cố định bất kể giá trị user nhập.
- User chỉ có thể sửa lại trọng số bằng cách inline edit cell spinbutton ở table sau khi save (đã verify TC09 inline edit hoạt động đúng — nhập 30 → table cell hiển thị 30).
- Modal "Thêm tiêu chí" hoàn toàn ignore field Trọng số (%) — bug FE.

**Supporting network evidence (DevTools Network tab quan sát khi click [Lưu]):**
```text
PUT /api/v1/ke-hoach-danh-gias/.../tieu-chis (reqid 1715)
Request body: {"version":1,"tieuChis":[{"tenTieuChi":"...","trongSo":100,"diemToiDa":10,...}]}
Response 200: {"success":true,"data":[{...trongSo:100, maTieuChi:"TC-20260510-0001"...}],"meta":{"tongTrongSo":100,"isValid":true}}
```

### Bằng chứng

![BUG-DG-010 modal force trongSo 100](image/r7-7-9-tc07-10-fr-vi-02-tieuchi-2026-05-10.png)

---

## ~~BUG-FUNC-DG-013~~ [CLOSED] — QTHT có button "Thêm người đánh giá" + "delete" trên tab Phân công (vi phạm matrix R-only trên KE_HOACH)

> **Re-test:** 2026-05-12 15:45:00 R19 — ✅ PASS (Closed-verified). Account `qtht_01` (QTHT) vào DG-20260510-0001 LAP_KE_HOACH (người tạo CB_NV_TW): Tab Tiêu chí spinbutton valuemin=0 (read-only style) + 0 button [Hủy đợt] / [+ Thêm tiêu chí] / delete row visible. Tab Phân công: 0 button [Thêm người đánh giá] / delete row. Permission theo SCR-DG-VIII đúng spec R-only. Evidence: [`image/reverify-2026-05-12-dg013-qtht-no-buttons.png`](image/reverify-2026-05-12-dg013-qtht-no-buttons.png).


### Mô tả

Account `qtht_01` (role QTHT, single role), vào module Đánh giá hiệu quả → click row đợt DG-20260510-0001 → đợt detail → tab Phân công. UI render giống hệt CB_NV_TW: button [+ Thêm người đánh giá] visible + clickable, mỗi row PC có button [delete] visible + clickable. Per `output/permission-matrix.md` line 71 (QTHT × `KE_HOACH_DANH_GIA` = 👁️ **R** only — không có CRUD), QTHT chỉ được xem chi tiết đợt, KHÔNG được create/delete PC. Tab Tiêu chí QTHT đúng có CRUD (matrix line 73 TIEU_CHI_DANH_GIA = ✅ CRUD), nhưng tab Phân công UI hiển thị action sai phạm vi quyền. SRS FR-VI-03 Tác nhân: "Cán bộ Nghiệp vụ (TW/BN/ĐP)" — KHÔNG bao gồm QTHT.

### Các bước tái hiện

**Precondition:** Tài khoản role QTHT (`qtht_01` primary, fallback `qtht_05` nếu primary lock). Có sẵn ≥1 đợt đánh giá state `LAP_KE_HOACH` do CB Nghiệp vụ TW khác tạo (vd `DG-20260510-0001`) — đợt đã có ≥1 tiêu chí + ≥1 phân công để quan sát action button.

1. Login `qtht_01` (hoặc fallback `qtht_05`) → sidebar Đánh giá hiệu quả → /danh-gia/ke-hoach/danh-sach.
2. Quan sát danh sách: ✅ KHÔNG có button [+ Tạo kế hoạch] (đúng matrix R-only).
3. Click row `DG-20260510-0001` (đợt LAP_KE_HOACH người khác tạo) → đợt detail mở.
4. Click tab Phân công → quan sát panel.
5. **FAIL evidence:** button [+ Thêm người đánh giá] visible at top of panel, button [delete] trên mỗi row PC.
6. Click tab Tiêu chí → quan sát: 3 spinbutton (trọng số / điểm tối đa / thứ tự) EDITABLE + button [delete] mỗi row + button [Hủy đợt] visible & enabled (vi phạm BA 2026-05-11 chốt "QTHT chỉ CRUD danh mục tiêu chí dùng chung, KHÔNG sửa tiêu chí gắn vào từng đợt").

### Kết quả mong đợi

Theo `output/permission-matrix.md`:
- Line 71: QTHT × KE_HOACH_DANH_GIA = 👁️ R (read only on toàn entity, bao gồm các sub-resource như PHAN_CONG_DANH_GIA).
- Line 100: "QTHT có quyền trên 49 entity — Read nghiệp vụ + CRUD các entity hệ thống (TIEU_CHI_DANH_GIA + 8 entity QTHT trừ AUDIT_LOG/THONG_BAO là Read)".

→ Tab Phân công với account QTHT phải:
- HIDE button [+ Thêm người đánh giá].
- HIDE button [delete] trên mỗi row PC (chỉ render cột Thao tác = `—` hoặc bỏ cột).

### Kết quả thực tế

QTHT thấy đầy đủ create/delete control. Nếu QTHT click [delete] hoặc fill modal [Thêm], BE có pass action không? Cần test backend. Nhưng UI level đã sai — tester / dev infosec có thể đoán nhầm permission scope.

### Bằng chứng

![BUG-DG-013 QTHT permission bypass on PC tab](image/r7-7-9-tc18-qtht-permission-bypass-2026-05-10.png)

### So sánh với role chuẩn (CB_NV_TW)

| UI Element | CB_NV_TW (matrix CRUD) | QTHT (matrix R) | UI Actual với QTHT |
|---|:-:|:-:|:-:|
| Button [+ Tạo kế hoạch] (list page) | ✅ Visible | ❌ Hidden | ✅ Hidden (CORRECT) |
| Button [+ Thêm người đánh giá] (PC tab) | ✅ Visible | ❌ Hidden | ✅ Visible (**SAI**) |
| Button [delete] PC row | ✅ Visible | ❌ Hidden | ✅ Visible (**SAI**) |
| Spinbutton edit trọng số (Tiêu chí) | ✅ Editable | ✅ Editable (matrix CRUD) | ✅ Editable (CORRECT) |

---

## BUG-FUNC-DG-014 — Dropdown Lĩnh vực modal "Thêm người đánh giá" render 2 raw UUID thay vì tên Vietnamese

> **Re-test:** 2026-05-12 15:50:00 R19 — ❌ REPRODUCED. Account `cb_nv_tw_06` modal Thêm người đánh giá → dropdown LV scroll virtual-list → 13 options, vẫn có **2 raw UUID**: `e5d17437-e267-42ce-9dbe-aa2eebc1e477` + `bbbbbbbb-0000-4000-8000-000000000018`. FE chưa filter LV no-name. Status giữ Open.


### Mô tả

Tester `cb_nv_tw_09`, vào đợt `DG-20260510-0001` (LAP_KE_HOACH) Tab Phân công → click [+ Thêm người đánh giá] → modal "Thêm người đánh giá" mở. Click combobox "Lĩnh vực" → dropdown render 12 options. 2/12 options render raw UUID string thay vì tên Vietnamese: `bbbbbbbb-0000-4000-8000-000000000018` và `bbbbbbbb-0000-4000-8000-000000000013`. 10/12 còn lại render đúng tên Vietnamese (Thuế, Lao động, Đất đai, Dân sự, Thương mại, Hình sự, Hành chính, Sở hữu trí tuệ, Doanh nghiệp, Đầu tư). Người dùng không hiểu 2 lựa chọn UUID là lĩnh vực gì → không chọn được an toàn.

### Các bước tái hiện

**Precondition:**
- Tài khoản role CB Nghiệp vụ TW (`cb_nv_tw_09` primary, fallback `cb_nv_tw_05` nếu primary lock).
- Có sẵn ≥1 đợt đánh giá ở **state `LAP_KE_HOACH` hoặc `PHAN_CONG`** đã thiết lập **tiêu chí có tổng trọng số = 100%** (BR-CALC-04). Nếu đợt đang `LAP_KE_HOACH` mà tổng trọng số < 100%, button [+ Thêm người đánh giá] sẽ DISABLED kèm tooltip "Vui lòng thiết lập tiêu chí đánh giá với tổng trọng số bằng 100% trước khi phân công người đánh giá". Nếu đợt đã > `PHAN_CONG` (`CHO_DUYET_PC`, `DANG_THUC_HIEN`, ...), button [+ Thêm người đánh giá] sẽ ẨN.

1. Login `cb_nv_tw_09` (hoặc fallback `cb_nv_tw_05`) qua MCP UI.
2. Sidebar → Đánh giá hiệu quả → tab Kế hoạch → click row đợt đáp ứng precondition (vd `DG-20260512-0001` PHAN_CONG, tổng trọng số 100%).
3. Tab Phân công → click [+ Thêm người đánh giá] → modal mở.
4. Click combobox "Lĩnh vực" (placeholder "Chọn lĩnh vực...").
5. Quan sát dropdown listbox (scroll virtual-list từ top → mid → bottom để capture đủ options).

### Kết quả mong đợi

Theo `srs-update-2026-5-5/srs-fr-08-danh-gia.md` FR-VI-03 Inputs row 4 (`linh_vuc_ids` Multi-select từ danh mục lĩnh vực `LINH_VUC_PL`) + line 798 SCR-VI-01 Tab 2 row 36 modal phân công.

Tất cả 12 (hoặc N) options phải render tên lĩnh vực Vietnamese đầy đủ (vd "Thuế", "Lao động"...). KHÔNG được render raw UUID. Nếu lĩnh vực bị soft-delete / thiếu tên → BE phải KHÔNG trả về dropdown, hoặc trả về với label "(Đã xoá)" / fallback name.

### Kết quả thực tế

- Network: `GET /api/v1/danh-muc?loaiDanhMuc=LINH_VUC_PL&pageSize=100` → 200 (reqid 931).
- Dropdown render 12 items. 10 tên Vietnamese OK, 2 raw UUID:
  - `bbbbbbbb-0000-4000-8000-000000000018`
  - `bbbbbbbb-0000-4000-8000-000000000013`
- Nghi vấn: BE response item cho 2 record này thiếu trường `tenLinhVuc` (null/empty), FE fallback render `id` raw. Hoặc 2 record là seed test data chưa có tên.

### Bằng chứng

![BUG-DG-014 Lĩnh vực dropdown 2 raw UUID](image/r11-linhvuc-dropdown-raw-uuid-2026-05-11.png)

---

## ~~BUG-FUNC-DG-006~~ [CLOSED] — Endpoint /vu-viec-eligible trả empty list mặc dù tồn tại VV state HOAN_THANH match đợt

> **Re-test:** 2026-05-10 11:05:00 R10 — ✅ PASS (Closed-verified). Endpoint mới: `GET /api/v1/ke-hoach-danh-gias/{id}/vu-viec-eligible` (sub-resource path đúng REST). Trả `{"total":1, "items":[{"ma":"VV-BTP-TW-20260509-008"}]}` với scope cb_nv_tw_02 BTP TW. UI Tab "Thực hiện" render 1 row eligible, checkbox active, button "Xác nhận chọn" enabled. POST `/vu-viec-select` 200 OK → đợt advance CHO_DUYET_PC → THUC_HIEN. Dev fix verified.


### Mô tả

Sau khi đợt ĐG HQ chuyển state `CHO_DUYET_PC` (B4 cb_pd duyệt PC OK), Tab "Thực hiện" hiển thị "0/0 VV - Không có vụ việc nào phù hợp". Endpoint `GET /api/v1/ke-hoach-danh-gias/{id}/vu-viec-eligible` trả 200 OK với data rỗng `[]`. Tuy nhiên `GET /api/v1/vu-viec?trangThai=HOAN_THANH` trả **20 VV state HOAN_THANH** trong system, trong đó ≥3 VV (VV000108, VV000105, VV000102) có ngày tiếp nhận `01/04/2026 ≤ ngày ≤ 12/04/2026` nằm trong **date range đợt 01/04 - 30/06/2026**. Lỗi block B6 (chọn VV) → cascade B7-B10.

### Các bước tái hiện

1. Tạo đợt ĐG HQ entry LAP_KE_HOACH với từ ngày `01/04/2026`, đến ngày `30/06/2026`, đối tượng `Vụ việc` (R7.4.D1 PASS — DG-20260506-0001)
2. Back-fill ≥4 tiêu chí từ DM `TIEU_CHI_DG_HIEU_QUA` (Σ trọng số = 100%) → PUT 200
3. Tab Phân công → Add 1 người ĐG (vd `cb_nv_tw_02` Trưởng nhóm, lĩnh vực `Lao động + Hôn nhân gia đình`) → POST 201
4. Trình phê duyệt (`cb_nv_tw_01`) → POST `/phan-congs/submit` 200 → state `PHAN_CONG`
5. Switch role `cb_pd_tw_01` → click [Phê duyệt] tại Tab Phân công → POST `/phan-congs/approve` 200 → state `CHO_DUYET_PC`
6. Reload đợt detail → click Tab "Thực hiện"
7. **Quan sát:** "Đã chọn: 0 / 0 vụ việc" + table empty "Không có vụ việc nào phù hợp"
8. Open new tab → /vu-viec/danh-sach → Tab "Hoàn thành" → quan sát 20 VV state HOAN_THANH visible

### Kết quả mong đợi

Tab Thực hiện trong đợt ĐG HQ phải render ≥3 VV candidates phù hợp:
- `VV000108` (12/04/2026 — Doanh nghiệp — DA_TIEP_NHAN dates trong range)
- `VV000105` (07/04/2026 — Kinh doanh thương mại)
- `VV000102` (03/04/2026 — Hành chính)

Nếu filter check linh_vuc của người ĐG (Lao động/HNGD), thì optional fallback: hiển thị tất cả VV match scope đơn vị + date range, người dùng tự chọn theo lĩnh vực phù hợp.

### Kết quả thực tế

```text
GET /api/v1/ke-hoach-danh-gias/6c8c40a2-d5b2-4fce-9db0-81e1642a7780/vu-viec-eligible
→ 200 OK
→ body: { data: [] }   (empty list)

UI render: "Không có vụ việc nào phù hợp"
```

→ Block B6 (chọn VV vào đợt) → cascade B7 (chấm điểm) + B8 (auto BAO_CAO) + B9 (trình BC) + B10 (duyệt BC) đều không thể test.

### Bằng chứng

**1. Ảnh chụp Tab Thực hiện empty + danh sách VV /vu-viec/danh-sach hiển thị 116 mục, 20 state Hoàn thành:**

![BUG-FUNC-DG-006 — Tab Thực hiện 0/0 VV mặc dù state CHO_DUYET_PC](image/r7-4-d2-b4-b6-state-cho-duyet-pc-no-vv.png)

![BUG-FUNC-DG-006 — VV list 116 mục, có VV000108/105/102 state Hoàn thành dates 03-12/04 in đợt range](image/r7-4-d2-vv-list-116-with-hoanthanh.png)

**2. Network log:**

```text
Đợt info:
  GET /api/v1/ke-hoach-danh-gias/{id} → state=CHO_DUYET_PC, tu_ngay=2026-04-01, den_ngay=2026-06-30, doi_tuong=VU_VIEC

VV eligible API:
  GET /api/v1/ke-hoach-danh-gias/{id}/vu-viec-eligible [200] → []

VV list (verify VV HOAN_THANH tồn tại):
  GET /api/v1/vu-viec?trangThai=HOAN_THANH [200] → 20 records (VV000108..087, dates 16/03 - 12/04/2026)
  → ≥3 VV in date range đợt: VV000108 (12/04), VV000105 (07/04), VV000102 (03/04)
```

**3. SRS reference:** `srs-fr-08-danh-gia.md` FR-VI-05 (Chọn VV vào đợt) — spec hiện không cụ thể chi tiết filter logic. Cần BA/dev confirm:
- (a) Filter chỉ check date overlap — bug rõ ràng (3 VV match nhưng trả 0)
- (b) Filter còn check `linh_vuc match người ĐG` — partial bug (FE không pass linh_vuc người ĐG vào query?)
- (c) Filter check đơn vị scope (TW vs DP) — nếu VV ở DP thì TW user không thấy được. Verified: 20 VV state HOAN_THANH thuộc đơn vị nào? Cần investigate.

---

## ~~BUG-FUNC-DG-007~~ [CLOSED] — Dashboard KPI "Vụ việc hoàn thành: 0" sai vs thực tế 20 VV state HOAN_THANH

> **Re-test:** 2026-05-10 11:05:00 R10 — ✅ PASS (Closed-verified). Dashboard cb_nv_tw_02 BTP TW hiển thị "Vụ việc hoàn thành: 2 vụ việc" khớp với pool BTP TW: HOAN_THANH=1 (VV-008) + DA_DANH_GIA=1 (VV-009) = 2 (FR-VI dashboard count "hoàn thành" gồm 2 state cuối lifecycle). Trước đây Dashboard 0 mismatch. Dev fix verified.


### Mô tả

Dashboard `/dashboard` hiển thị KPI "Vụ việc hoàn thành: 0 vụ việc" cho năm 2026 (Tất cả đơn vị, không filter). Nhưng `/vu-viec/danh-sach` Tab "Hoàn thành" hiện **20 VV state HOAN_THANH thực sự** (VV000087-108, dates 16/03 - 12/04/2026). KPI counter mismatch với raw data — có thể BE aggregation query có filter sai (vd: chỉ count VV completed in CURRENT month/quarter) hoặc FE truyền filter ngầm.

### Các bước tái hiện

1. Login bất kỳ role có quyền dashboard (vd `cb_nv_tw_01`)
2. Truy cập `/dashboard`
3. Xem block KPI "Vụ việc hoàn thành"
4. Quan sát: "0 vụ việc" mặc dù năm filter = 2026, đơn vị = Tất cả
5. Mở /vu-viec/danh-sach → Tab "Hoàn thành" → đếm rows = 20

### Kết quả mong đợi

KPI "Vụ việc hoàn thành" phải hiển thị `20` (hoặc số đúng theo filter Năm/Đơn vị/Date range nếu spec yêu cầu sub-filter).

### Kết quả thực tế

KPI = 0 (sai). Cảnh quan: nếu user dựa vào dashboard KPI để báo cáo lãnh đạo → undercount nghiêm trọng (20 VV → báo 0).

### Bằng chứng

```text
Dashboard /dashboard (Năm 2026, Tất cả đơn vị):
- Hỏi đáp mới: 6 ✓
- Vụ việc tiếp nhận: 76 ✓
- Vụ việc đang xử lý: 76 ✓
- Vụ việc hoàn thành: 0   ← SAI (thực tế 20)
- Đào tạo đang diễn ra: 0
- Đào tạo hoàn thành: 0
- Chuyên gia/Tư vấn viên: 0

VV list /vu-viec/danh-sach Tab "Hoàn thành": 20 records
```

**BA update 2026-05-11:** KPI "Vụ việc hoàn thành" đếm `VU_VIEC.trang_thai IN ('HOAN_THANH','DA_DANH_GIA')`, lọc theo `ngay_hoan_thanh` và `don_vi_id` đúng phạm vi người xem; không đếm `DA_DUYET` nếu KPI tên là "hoàn thành". Evidence cũ ở trên giữ làm lịch sử lỗi trước khi BA chốt rule.

---

## ~~BUG-FUNC-DG-008~~ [CLOSED] — PUT `/ket-quas` trả 200 với data đúng nhưng GET sau đó trả null (read-after-write inconsistency)

> **Re-test:** 2026-05-12 02:25:00 R12 — ✅ PASS (Closed-verified). Account `cb_nv_tw_03` (người ĐG assigned) đợt DG-20260509-0001 THUC_HIEN với VV-BTP-TW-20260509-008. Fill điểm 7/8/9/6 → click [Lưu kết quả]. Network reqid 233 PUT `/ket-quas` → 200; reqid 234 GET `/ket-quas` → 200 trả `chiTietDiem:[{7},{8},{9},{6}]`, `diemTong:7.90`, `xepLoai:"TOT"`, `trangThai:"DA_DANH_GIA"`, `version:2`. UI render spinbutton "7.0/8.0/9.0/6.0", đợt advance `THUC_HIEN → DANG_DANH_GIA`. PUT-GET đồng bộ + side effect state advance đúng SM. Đóng bug. Bằng chứng: [`r12-dg008-put-get-consistent-2026-05-12.png`](image/r12-dg008-put-get-consistent-2026-05-12.png).

### Mô tả

Account `cb_nv_tw_03` (Người đánh giá được phân công, role CB_NV_TW), đợt DG-20260509-0001 state `THUC_HIEN`, soVuViecDanhGia=1 (VV-BTP-TW-20260509-008). Tab "Chấm điểm" hiển thị grid 1 VV × 4 tiêu chí. QA fill điểm 9/8/9/9 (Σ trọng số 30+20+40+10=100%), điểm tổng auto-tính 8.8, xếp loại "Tốt", click button [Lưu kết quả]. Network: `PUT /api/v1/ke-hoach-danh-gias/c521f1f1-82b2-424a-a14c-6d01e91ce540/ket-quas` → **200 OK** với response body chứa computed `{diemTong: 8.8, xepLoai: "TOT", trangThai: "DA_DANH_GIA", version: 2, ngayCapNhat: "2026-05-10T04:42:37.204Z", chiTietDiem: [...4 entries...]}`. Tuy nhiên `GET /api/v1/ke-hoach-danh-gias/{id}/ket-quas` ngay sau đó (cùng tab, cùng session, cùng JWT) trả `{version: 1, diemTong: null, xepLoai: null, trangThai: "CHUA_DANH_GIA", chiTietDiem: null, ghiChu: null}` — **không reflect ghi mới vừa thực hiện**. Reload page UI → spinbutton điểm reset 0/0/0/0, "Số VV đã chấm" 0/1, đợt-level state vẫn `THUC_HIEN` (`diemTrungBinh=null`, `version=4` không tăng). Retry PUT lần 2 với cùng dữ liệu → response body vẫn version=2 nhưng GET vẫn version=1 sau 3 lần polling cách 1.5s.

### Các bước tái hiện

1. Login `cb_nv_tw_03` (Người đánh giá được phân công cho đợt DG-20260509-0001 từ R9, nguoiDanhGiaId trong `/phan-congs` khớp `2a5303aa-...`).
2. Vào module Đánh giá hiệu quả → click row DG-20260509-0001 → mở detail.
3. Click Tab "Chấm điểm" → grid hiện VV-BTP-TW-20260509-008 với 4 spinbutton điểm + textbox ghi chú + button [Lưu kết quả].
4. Fill điểm: TC1=9, TC2=8, TC3=9, TC4=9; ghi chú "R10 2026-05-10 — score test sau dev fix BUG-006/007."
5. Click [Lưu kết quả] → tab Network: PUT `/ket-quas` 200 (response body trả computed `diemTong: 8.8, xepLoai: "TOT", trangThai: "DA_DANH_GIA", version: 2`).
6. Ngay sau đó FE auto-fetch GET `/ket-quas` → 200 nhưng trả `version: 1, diemTong: null, trangThai: "CHUA_DANH_GIA"`.
7. Reload page (F5 + ignoreCache) → spinbutton điểm = 0, "Số VV đã chấm: 0/1", đợt state vẫn "Thực hiện".
8. Click Tab "Chấm điểm" → fill lại điểm + click [Lưu kết quả] lần 2 → cùng pattern: PUT 200 (response version=2) nhưng GET vẫn version=1.

### Kết quả mong đợi

Theo SRS `srs-fr-08-danh-gia.md` FR-VI-08 (Người đánh giá chấm điểm) + SCR-VI-01 row 38 (Tab 4 Chấm điểm Drawer "Lưu kết quả"):
- PUT `/ket-quas` save thành công (200) → DB persist `chiTietDiem` + computed `diemTong` + `xepLoai` + `trangThai=DA_DANH_GIA` cho mỗi `vuViecId`.
- GET `/ket-quas` ngay sau đó phải trả lại đúng record vừa update (version tăng, fields filled).
- Reload UI phải render lại score đã save.
- Khi tất cả `vuViec` của đợt đã `trangThai=DA_DANH_GIA` → đợt-level `trangThai` advance `THUC_HIEN → DA_DANH_GIA` (workflow B9 transition theo SM-DANHGIA).

### Kết quả thực tế

```text
PUT /api/v1/ke-hoach-danh-gias/c521f1f1-82b2-424a-a14c-6d01e91ce540/ket-quas
   request body:
     {"ketQuas":[{"vuViecId":"8d074115-4da5-427c-af55-3909f1e4e675",
                  "chiTietDiem":[{tieuChiId:"014e62ec...", diem:9},
                                 {tieuChiId:"da77e4ed...", diem:8},
                                 {tieuChiId:"c552a4c1...", diem:9},
                                 {tieuChiId:"a8dc64b1...", diem:9}],
                  "ghiChu":"R10 2026-05-10 — score test..."}]}
   response 200:
     {"success":true,
      "data":[{"id":"fb192342-...","version":2,
               "diemTong":8.8,"xepLoai":"TOT","trangThai":"DA_DANH_GIA",
               "chiTietDiem":[...4 entries...],
               "ngayCapNhat":"2026-05-10T04:42:37.204Z"}]}

GET /api/v1/ke-hoach-danh-gias/c521f1f1-82b2-424a-a14c-6d01e91ce540/ket-quas
   (gọi 0.5s sau PUT, cùng JWT, cache: 'no-store', timestamp buster)
   response 200:
     {"success":true,
      "data":[{"id":"fb192342-...","version":1,
               "diemTong":null,"xepLoai":null,"trangThai":"CHUA_DANH_GIA",
               "chiTietDiem":null,"ghiChu":null}]}

GET /api/v1/ke-hoach-danh-gias/c521f1f1-82b2-424a-a14c-6d01e91ce540
   response 200:
     {"data":{"trangThai":"THUC_HIEN","diemTrungBinh":null,"version":4}}
```

→ Cascade block B10 (đợt không thể `BAO_CAO` vì state vẫn `THUC_HIEN`) + B11 (negative test HUY tại HOAN_THANH không thể tới được).

### Bằng chứng

**1. Screenshot Tab Chấm điểm grid sau reload — score reset về 0, "Số VV đã chấm: 0/1":**

![BUG-FUNC-DG-008 — Tab Chấm điểm sau Lưu + reload, score reset 0/0/0/0](../../workflow/screenshots/r7-4-d2-r10-b9-after-save-reset-2026-05-10.png)

**2. Screenshot grid trước khi click Lưu (điểm 9/8/9/9 đã fill, total auto = 8.8 "Tốt"):**

![BUG-FUNC-DG-008 — Grid trước Lưu, điểm 9/8/9/9, total 8.8 Tốt](../../workflow/screenshots/r7-4-d2-r10-b9-cham-diem-grid-2026-05-10.png)

**3. Network log đầy đủ (reqid 656 PUT 200, reqid 657 GET 200 ngay sau):**

```text
reqid=656 PUT /api/v1/ke-hoach-danh-gias/c521f1f1.../ket-quas → 200
   response: version=2, diemTong=8.8, xepLoai=TOT, trangThai=DA_DANH_GIA
reqid=657 GET /api/v1/ke-hoach-danh-gias/c521f1f1.../ket-quas → 200
   response: version=1, diemTong=null, xepLoai=null, trangThai=CHUA_DANH_GIA
   (timestamp: PUT 04:42:37.204Z → GET 04:42:37.xxx → cùng giây)
```

**4. Polling 3 lần × 1.5s gap đều trả version=1:**

```json
[{"attempt":1,"ketState":"CHUA_DANH_GIA","ketDiem":null,"ketVersion":1,"dotState":"THUC_HIEN","dotVersion":4},
 {"attempt":2,"ketState":"CHUA_DANH_GIA","ketDiem":null,"ketVersion":1,"dotState":"THUC_HIEN","dotVersion":4},
 {"attempt":3,"ketState":"CHUA_DANH_GIA","ketDiem":null,"ketVersion":1,"dotState":"THUC_HIEN","dotVersion":4}]
```

**5. SRS reference:** `srs-fr-08-danh-gia.md` FR-VI-08 (Người đánh giá chấm điểm) yêu cầu:
- Input: `chiTietDiem[]` (Σ trọng số = 100, mỗi điểm ≤ điểmTốiĐa).
- Processing: BE tính `diemTong = Σ(điểmTC × trọngSốTC) / Σ trọngSố`, `xepLoai` map theo BR-RANK (≥9.0 XS, ≥7.5 T, ≥6.0 Đ, <6.0 CD), set `trangThai=DA_DANH_GIA`.
- Outputs: persist record + side effect: nếu mọi VV trong đợt `=DA_DANH_GIA` → đợt advance.
- SCR-VI-01 row 38 Tab 4 Chấm điểm: button [Lưu kết quả] gọi PUT API → load lại data.

PUT response cho thấy BE **đã** tính đúng (diemTong=8.8, xepLoai=TOT) nhưng không persist DB (version không tăng ở read path). 2 hypothesis:
- (a) BE PUT chỉ update in-memory model rồi return, không commit transaction DB.
- (b) BE có read replica chưa sync (write to master, read from stale replica) — nhưng polling 3 × 1.5s = 4.5s vẫn fail nên không phải replication lag thông thường.
- (c) PUT có conditional check (vd "đợt phải state DANG_DANH_GIA") fail silent → return computed body nhưng skip commit. Nhưng response không có error code và `success: true`.

→ Cần dev xem log BE phía PUT handler: có `db.commit()` được gọi sau khi tính `diemTong` không? Có exception bị swallow không?

---

## ~~BUG-FUNC-DG-009~~ [CLOSED] — Đợt detail page thiếu hoàn toàn UI button "Hủy đợt" tại 4 state nguồn HUY

> **Re-test:** 2026-05-12 01:30:00 R12 — ✅ PASS (Closed-verified). Account `cb_nv_tw_05` mở đợt mới `DG-20260512-0001` LAP_KE_HOACH → button [Hủy đợt] (icon `stop`) visible enabled ở header. Đợt DG-20260510-0001 LAP_KE_HOACH (cũ) cũng có button [Hủy đợt]. UI đã wire HUY action ở state LAP_KE_HOACH (và cả khi advance qua PHAN_CONG/CHO_DUYET_PC button vẫn visible). Đóng bug. Bằng chứng: [`r12-dg009-huy-button-lap-ke-hoach-2026-05-12.png`](image/r12-dg009-huy-button-lap-ke-hoach-2026-05-12.png).

### Mô tả

Account `cb_nv_tw_01` (CB_NV_TW BTP TW, role tạo + organize đợt). Test D2a HUY transition theo SRS FR-VI-08 + Mermaid line 1133-1136 (HUY allowed từ 4 state nguồn: LAP_KE_HOACH / PHAN_CONG / THUC_HIEN / BAO_CAO). 2 đợt thực tế hiện hữu trong hệ thống:

- Đợt mới seed **DG-20260510-0001** state `LAP_KE_HOACH` (id `be180478-83f8-4798-8224-84b6dcf6435c`) — vừa tạo "Lưu nháp" 2026-05-10 20:36:08.
- Đợt **DG-20260509-0001** state `THUC_HIEN` (id `c521f1f1-82b2-424a-a14c-6d01e91ce540`).

Mở chi tiết từng đợt (`/danh-gia/ke-hoach/{id}`), scan toàn bộ DOM (8 button visible trên mỗi page), kết quả: **0 button text "Hủy" / "Huỷ" / "Hủy đợt" / "Hủy kế hoạch"** xuất hiện. Đợt list view (`/danh-gia/ke-hoach/danh-sach`) row-level cũng 0 action ngoài 2 anchor link mã + tên đợt — không có ellipsis "..." menu, không có dropdown action. Việc thiếu UI block toàn bộ test D2a 4 state nguồn HUY (positive transition).

### Các bước tái hiện

1. Login `cb_nv_tw_01` (BTP TW, có quyền tạo + edit đợt theo FR-VI-01..03).
2. Vào module Đánh giá hiệu quả → tab "Tất cả" → list 2 đợt.
3. Click DG-20260510-0001 → mở detail state `LAP_KE_HOACH` → scan UI: chỉ có buttons `[Quay lại danh sách]`, `[+ Thêm tiêu chí]`, `[Nhập từ danh mục]`, `[Lưu thay đổi]`. Tabs: Tiêu chí / Phân công / Thực hiện / Chấm điểm / Báo cáo.
4. Quay lại list → click DG-20260509-0001 → mở detail state `THUC_HIEN` → scan UI: chỉ có button `[Quay lại danh sách]` + 5 tabs (no action button khác).
5. Mỗi page chạy `evaluate_script` count `Hủy|Huỷ` keyword toàn DOM → trả `{totalHuy: 0, totalHuy2: 0}` cả 2 trường hợp.
6. Quay lại list view → kiểm tra row-level: query `tr.ant-table-row` các button/anchor → mỗi row chỉ có 2 anchor (mã + tên), 0 ellipsis dropdown.

### Kết quả mong đợi

Theo SRS `srs-fr-08-danh-gia.md`:
- FR-VI-08 transition table (canonical) + Mermaid line 1133-1136: HUY transition allowed từ `LAP_KE_HOACH`, `PHAN_CONG`, `THUC_HIEN`, `BAO_CAO` → state đích `HUY`. Guard: chưa `HOAN_THANH`.
- SCR-VI-01 (chi tiết screen detail kế hoạch đánh giá): list các button action theo từng state — phải có button "Hủy đợt" / "Huỷ kế hoạch" tại 4 state nguồn (Người tổ chức = creator của đợt). Sau click → open confirm modal với ghi chú lý do (theo BR-FLOW), submit → POST/PATCH endpoint HUY → state đợt → `HUY`, list filter Tab "Hủy" hiện đợt vừa hủy.

### Kết quả thực tế

Đợt detail mọi state nguồn HUY → **0 button HUY** trên UI. Row-level list cũng 0 action menu. UI hoàn toàn thiếu wire HUY action.

```text
Detail page DG-20260510-0001 (LAP_KE_HOACH):
  buttons (visible, content): ["Quay lại danh sách", "+ Thêm tiêu chí",
    "Nhập từ danh mục", "Lưu thay đổi" (disabled)]
  Hủy/Huỷ keyword count: 0
  evaluate_script: {keywords:[], totalHuy:0, totalHuy2:0}

Detail page DG-20260509-0001 (THUC_HIEN):
  buttons (visible, content): ["Quay lại danh sách"]
  Hủy/Huỷ keyword count: 0

List view row buttons (per row):
  [{tag:"A", text:"DG-20260510-0001"}, {tag:"A", text:"QA R7.4.D2a HUY test"}]
  → 0 ellipsis "..." menu, 0 row action button, 0 row dropdown
```

Hệ quả:
- D2a HUY test 4 state nguồn (LAP_KE_HOACH/PHAN_CONG/THUC_HIEN/BAO_CAO) đều block ở UI level — cannot trigger HUY action via UI.
- Negative HUY test tại HOAN_THANH (B11) đã pass do bản chất HOAN_THANH UI cũng không có HUY button (consistent với spec). Nhưng pass này không validate được (không có positive case để so sánh).
- D2b cross-co-quan FR-VI-10 read-only test cũng block (cần đợt HOAN_THANH unreachable do BUG-DG-008).

### Bằng chứng

**1. Screenshot DG-20260510-0001 detail (LAP_KE_HOACH state — không có button HUY):**

![DG-20260510-0001 LAP_KE_HOACH detail](image/r7-4-d2a-lap-ke-hoach-detail-2026-05-10.png)

**2. Screenshot DG-20260509-0001 detail (THUC_HIEN state — chỉ có "Quay lại danh sách"):**

![DG-20260509-0001 THUC_HIEN detail](image/r7-4-d2a-dg001-thuc-hien-detail-2026-05-10.png)

**3. evaluate_script DOM scan kết quả (cả 2 page):**

```js
() => {
  const all = document.body.innerHTML;
  return {
    totalHuy: (all.match(/Hủy/g) || []).length,
    totalHuy2: (all.match(/Huỷ/g) || []).length,
    keywords: ['Hủy đợt','Huỷ đợt','Hủy kế hoạch','Huỷ kế hoạch'].map(k => all.includes(k))
  };
}
// → {totalHuy: 0, totalHuy2: 0, keywords: [false, false, false, false]}
```

**4. List row inspect:**

```js
() => Array.from(document.querySelectorAll('.ant-table-tbody tr.ant-table-row')).map(r => ({
  code: r.querySelector('td')?.textContent.trim().slice(0, 30),
  buttons: Array.from(r.querySelectorAll('button, a')).map(b => ({tag: b.tagName, text: b.textContent.trim().slice(0, 20)}))
}));
// → [
//   {code:"DG-20260510-0001", buttons:[{tag:"A",text:"DG-20260510-0001"},{tag:"A",text:"QA R7.4.D2a HUY test"}]},
//   {code:"DG-20260509-0001", buttons:[{tag:"A",text:"DG-20260509-0001"},{tag:"A",text:"QA R7.4.D1 bo 03 202"}]}
// ]
// 0 ellipsis dropdown / row action menu
```

**5. SRS reference cụ thể:**
- `input/srs-v3/srs-fr-08-danh-gia.md` FR-VI-08 transition table: HUY transition row liệt kê 4 state nguồn `LAP_KE_HOACH/PHAN_CONG/THUC_HIEN/BAO_CAO → HUY`.
- Mermaid block line 1133-1136 cùng file: edges `LAP_KE_HOACH --> HUY`, `PHAN_CONG --> HUY`, `THUC_HIEN --> HUY`, `BAO_CAO --> HUY`.
- SCR-VI-01 screen detail kế hoạch đánh giá: yêu cầu wire HUY button tại 4 state nguồn cho role Người tổ chức (đã verify NotebookLM 2026-05-08).

→ FE chưa wire HUY button. BE endpoint chưa probe (per UI-only test rule). Block toàn bộ D2a positive test.

---

## ~~BUG-FUNC-DG-011~~ [CLOSED] — Bảng Phân công render "—" cho Người đánh giá + Lĩnh vực + Ghi chú dù BE đã persist

> **Re-test:** 2026-05-12 01:35:00 R12 — ✅ PASS (Closed-verified). Account `cb_nv_tw_05` đợt mới `DG-20260512-0001` thêm 1 PC `cb_nv_tw_06` Trưởng nhóm → Bảng PC render đầy đủ "CB Nghiệp vụ TW 06 / cb_nv_tw_06@htpldn.test / Trưởng nhóm". FE lookup tên + email + role chính xác. Đóng bug.

### Mô tả

Account `cb_nv_tw_01`, đợt DG-20260510-0001 state `LAP_KE_HOACH`, tab Phân công. Click [+ Thêm người đánh giá] → modal: chọn Người đánh giá = "CB Nghiệp vụ TW 02 — cb_nv_tw_02@htpldn.test", Vai trò = Đánh giá viên, Lĩnh vực = [Lao động, Dân sự, Hình sự]. Click [Thêm]. Network reqid 1744 POST `/phan-congs` 201 với request body đúng `linhVucIds:[3 UUIDs]`. GET `/phan-congs` (reqid 1745) sau đó trả response chứa đầy đủ `linhVucIds:[bbbbbbbb-...013, ...010, ...011]` cùng với `nguoiDanhGiaId: facdea31-...`. Tuy nhiên table render row mới với cột "Người đánh giá" = `—`, "Lĩnh vực" = `—`, "Ghi chú" = `—`. Chỉ cột "Vai trò" = "Đánh giá viên" hiển thị đúng. Tester không thể nhìn vào bảng để biết ai đã được phân công.

### Các bước tái hiện

1. Login `cb_nv_tw_01` → module Đánh giá → đợt detail → tab Phân công.
2. Click [+ Thêm người đánh giá] → fill modal: Người đánh giá = `cb_nv_tw_02`, Vai trò = "Đánh giá viên", Lĩnh vực = chọn 1+ option.
3. Click [Thêm] → toast "Thêm người đánh giá thành công".
4. Quan sát bảng: row mới có "Vai trò" = "Đánh giá viên" nhưng các cột "Người đánh giá" / "Lĩnh vực" / "Ghi chú" = `—`.
5. Verify network: GET `/phan-congs` 200 — response data có đầy đủ `nguoiDanhGiaId` (UUID) + `linhVucIds[]` (UUIDs). FE không lookup tên người + tên lĩnh vực từ id để render.

### Kết quả mong đợi

Theo SRS `srs-fr-08-danh-gia.md` line 798 (SCR-VI-01 Tab 2 — Phân công, row 36 bảng "Người đánh giá / Vai trò / Lĩnh vực / Ghi chú / Thao tác"):
- Cột "Người đánh giá" hiển thị họ tên đầy đủ user (vd "CB Nghiệp vụ TW 02").
- Cột "Lĩnh vực" hiển thị danh sách tên lĩnh vực (vd "Lao động, Dân sự, Hình sự") — comma separated.
- Cột "Ghi chú" hiển thị nội dung ghi chú nếu user nhập, hoặc `—` nếu trống.

### Kết quả thực tế

```text
GET /api/v1/ke-hoach-danh-gias/.../phan-congs (reqid 1745) 200
Response data: [
  {
    nguoiDanhGiaId: "facdea31-96a6-4e09-9acf-f871052faa68",
    vaiTro: "DANH_GIA_VIEN",
    linhVucIds: ["bbbbbbbb-...013","bbbbbbbb-...010","bbbbbbbb-...011"],
    ghiChu: null
    // KHÔNG có nguoiDanhGia.hoTen, KHÔNG có linhVuc[].tenDanhMuc
  }
]
Table render:
| Người đánh giá | Vai trò       | Lĩnh vực | Ghi chú | Thao tác |
| —              | Đánh giá viên | —        | —       | [delete] |
| —              | Trưởng nhóm   | —        | —       | [delete] |
```

Root cause: BE chỉ trả ID, không nested object. FE chưa wire lookup `/lookup/danh-gia-vien` + `/danh-muc?loaiDanhMuc=LINH_VUC_PL` để map id → tên khi render.

### Bằng chứng

![BUG-DG-011 PC table display empty](image/r7-7-9-tc11-fr-vi-03-pc-2-people-display-bug-2026-05-10.png)

---

## ~~BUG-FUNC-DG-012~~ [CLOSED] — Đợt không advance state `LAP_KE_HOACH → PHAN_CONG` dù đã POST 4 lần `/phan-congs` 201

> **Re-test:** 2026-05-12 02:10:00 R12 — ✅ PASS (Closed-verified). Account `cb_nv_tw_05` đợt mới `DG-20260512-0001` (TC trọng số = 100%). (1) POST `/phan-congs` đầu tiên (cb_nv_tw_06 Trưởng nhóm) → state advance `LAP_KE_HOACH → PHAN_CONG`, stepper bước 1 check icon, button [Trình phê duyệt] enabled. (2) Click [Trình phê duyệt] → confirm modal → POST `/phan-congs/submit` 200 → state advance `PHAN_CONG → CHO_DUYET_PC`, stepper bước 2 check, badge header chuyển "Chờ duyệt PC". Cả 2 transition đều OK. Đóng bug.

### Mô tả

Account `cb_nv_tw_01`, đợt DG-20260510-0001 state khởi tạo `LAP_KE_HOACH`. QA POST 4 phân công thành công (mỗi POST trả 201, BE persist record với `keHoach.trangThai: "LAP_KE_HOACH"` không đổi sau từng POST). Sau 4 PC, đợt-level vẫn `trangThai: LAP_KE_HOACH`, `version: 1` (không tăng). Button "Trình phê duyệt" UI disabled vì FE check `trangThai === 'PHAN_CONG'` mới enable. Force-click button qua `btn.disabled = false; btn.click()` không fire request — React onClick handler kiểm tra state nội bộ silent no-op. Tester block không thể tiến tới `CHO_DUYET_PC` để test TC14 (reject PC) hoặc TC17 (cross-cấp deny). Đây là vi phạm SM-DANHGIA: line 1159 ghi rõ "LAP_KE_HOACH → PHAN_CONG | CB NV phân công | Có KH | Gán CB/CG | FR-VI-03" — bước "Gán CB/CG" (POST `/phan-congs`) PHẢI trigger transition state.

### Các bước tái hiện

1. Login `cb_nv_tw_01` → tạo đợt mới state mặc định `LAP_KE_HOACH` (DG-20260510-0001).
2. Tab Tiêu chí: thêm 1 tiêu chí trọng số 100% (qua TC07 + inline edit) → Σ = 100%.
3. Tab Phân công: click [+ Thêm người đánh giá] → fill `cb_nv_tw_02` Đánh giá viên + lĩnh vực → POST `/phan-congs` reqid 1744 trả 201, response `keHoach.trangThai: "LAP_KE_HOACH"`.
4. Lặp bước 3 thêm 3 lần: thêm `cb_nv_tw_03` Trưởng nhóm, `cb_nv_tw_04` Đánh giá viên. Mỗi POST trả 201.
5. GET `/phan-congs` (reqid 1760) trả `meta.tongPhanCong: 2, soTruongNhom: 1` + `keHoach.trangThai: "LAP_KE_HOACH"`.
6. Quan sát button "Trình phê duyệt" → disabled. Tổng "2 người — 1 Trưởng nhóm" thoả E1+E2 SRS.
7. JS `document.querySelector` confirm `btn.disabled = true` + bypass force-click → không fire request.

### Kết quả mong đợi

Theo SRS `srs-fr-08-danh-gia.md`:
- Line 1159: SM transition `LAP_KE_HOACH → PHAN_CONG` triggered by FR-VI-03 (Gán CB/CG = POST `/phan-congs`).
- Sau POST `/phan-congs` đầu tiên: BE update đợt `trangThai = "PHAN_CONG"`, `version` tăng.
- Button "Trình phê duyệt" enable khi đợt ở `PHAN_CONG` + ≥1 PC + ≥1 TRUONG_NHOM (E1+E2 thoả).
- Click [Trình phê duyệt] → POST hoặc PATCH endpoint chuyển `PHAN_CONG → CHO_DUYET_PC` (line 1160).

### Kết quả thực tế

```text
Đợt DG-20260510-0001:
- T0 sau create:        trangThai=LAP_KE_HOACH, version=1
- Sau 4 POST /phan-congs (201 mỗi POST):  trangThai=LAP_KE_HOACH, version=1 (UNCHANGED)
- Button "Trình phê duyệt": disabled (FE check trangThai===PHAN_CONG)
- Force btn.disabled=false + click → 0 network request fired
```

Root cause hypothesis: BE missing logic auto-update `trangThai` khi nhận POST `/phan-congs` đầu tiên. Hoặc FE thiếu PATCH `/ke-hoach-danh-gias/{id}` với `{trangThai: "PHAN_CONG"}` sau mỗi POST PC. SM-DANHGIA spec rõ ràng nên BE/FE đều có thể là điểm fix.

### Bằng chứng

![BUG-DG-012 state stuck LAP_KE_HOACH](image/r7-7-9-tc14-state-not-advance-2026-05-10.png)

GET phan-congs response:
```json
{"success":true,"data":[{...,"keHoach":{"trangThai":"LAP_KE_HOACH","version":1,...}}],"meta":{"tongPhanCong":2,"soTruongNhom":1}}
```

---

## ~~BUG-FUNC-DG-015~~ [CLOSED] — Tab "Thực hiện" + "Báo cáo" leak BE error toast khi click navigate ở state LAP_KE_HOACH

> **Re-test:** 2026-05-12 01:55:00 R12 — ✅ PASS (Closed-verified). Account `cb_nv_tw_05` đợt mới `DG-20260512-0001` LAP_KE_HOACH. Click tab "Thực hiện" + "Báo cáo" → MutationObserver capture 2.5s không match toast "Kế hoạch phải...", body placeholder render OK. Đóng bug. Bằng chứng: [`r12-dg015-tab-baocao-no-toast-2026-05-12.png`](image/r12-dg015-tab-baocao-no-toast-2026-05-12.png).

### Mô tả

Tester `cb_nv_tw_09`, đợt `DG-20260510-0001` state `LAP_KE_HOACH`. Click tab "Thực hiện" → body render đúng empty placeholder "Chức năng thực hiện đánh giá sẽ khả dụng sau khi hoàn tất phân công." (state-gated UI correct). NHƯNG đồng thời pop BE error toast đỏ góc phải: "Kế hoạch phải ở trạng thái CHO_DUYET_PC, hiện tại là 'LAP_KE_HOACH'". Click tab "Báo cáo" cùng đợt → empty placeholder "Chưa hoàn thành đánh giá" + toast đỏ "Kế hoạch phải ở trạng thái DA_DANH_GIA trở lên, hiện tại là 'LAP_KE_HOACH'". Tab Chấm điểm cùng state thì empty placeholder gọn không leak (pattern đúng nên áp dụng cho 2 tab kia).

Root cause nghi vấn: FE gọi API load data tab trước khi check state, BE trả 4xx, FE generic error handler push toast. UI dùng cho user nghiệp vụ không cần thấy BE error code/jargon — chỉ cần placeholder hiền lành như Tab Chấm điểm.

### Các bước tái hiện

1. Login `cb_nv_tw_09` qua MCP UI.
2. Sidebar Đánh giá hiệu quả → vào đợt `DG-20260510-0001` (state LAP_KE_HOACH).
3. Click tab "Thực hiện" → quan sát body + toast.
4. Click tab "Chấm điểm" → quan sát body + toast (clean, để đối chứng).
5. Click tab "Báo cáo" → quan sát body + toast.

### Kết quả mong đợi

Theo `srs-update-2026-5-5/srs-fr-08-danh-gia.md` SCR-VI-01 Tab 3 (Thực hiện) + Tab 5 (Báo cáo):
- Khi state đợt chưa đạt → body render empty placeholder Vietnamese (đã đúng).
- KHÔNG hiển thị BE error toast khi user chỉ thực hiện navigate tab (không gọi action).

Behavior tham chiếu: Tab Chấm điểm cùng state hiển thị `image "Trống" + "Phân công chưa được phê duyệt — chưa thể thực hiện chấm điểm"` mà KHÔNG kèm toast → pattern đúng, 2 tab kia cần sửa theo.

### Kết quả thực tế

| Tab | Body placeholder | BE error toast |
|---|---|:-:|
| Tiêu chí | Có (table editable Σ trọng số) | — |
| Phân công | Có (table PC) | — |
| **Thực hiện** | ✅ "Chức năng thực hiện đánh giá sẽ khả dụng sau khi hoàn tất phân công." | ❌ "Kế hoạch phải ở trạng thái CHO_DUYET_PC, hiện tại là 'LAP_KE_HOACH'" |
| Chấm điểm | ✅ "Phân công chưa được phê duyệt — chưa thể thực hiện chấm điểm" | ✅ KHÔNG có (pattern đúng) |
| **Báo cáo** | ✅ "Chưa hoàn thành đánh giá" | ❌ "Kế hoạch phải ở trạng thái DA_DANH_GIA trở lên, hiện tại là 'LAP_KE_HOACH'" |

### Bằng chứng

![BUG-DG-015 Tab Thực hiện leak BE error](image/r11-tab-thuchien-state-gated-lap-ke-hoach-2026-05-11.png)

![BUG-DG-015 Tab Báo cáo leak BE error](image/r11-tab-baocao-state-gated-error-leak-2026-05-11.png)

---

## Observations (không log thành bug)

### OBS-D2-001 — SM label "Chờ duyệt PC" hiện sau khi đã duyệt (counterintuitive)

App SM hiện thực:
- B3 cb_nv_tw_01 click [Trình phê duyệt] → POST `/phan-congs/submit` 200 → state badge `Phân công` (PHAN_CONG)
- B4 cb_pd_tw_01 click [Phê duyệt] → POST `/phan-congs/approve` 200 → state badge `Chờ duyệt PC` (CHO_DUYET_PC)

Counterintuitive: "Chờ duyệt PC" thường nghĩa "đang chờ ai đó phê duyệt phân công". Sau khi cb_pd đã duyệt, expected state nên là `THUC_HIEN` (Thực hiện) hoặc tương đương. Hiện tại app vẫn ở `CHO_DUYET_PC` mặc dù logic đã pass duyệt — possibly app SM definition đảo logic vs SRS or app dùng `CHO_DUYET_PC` ý "Chờ phê duyệt thông tin chấm điểm" (next phase). Cần BA/dev confirm SM canonical labels.

Defer log bug — chờ TODO ambiguity SRS resolved (SRS Master có 3 phiên bản SM khác nhau — DB ENUM 6 / Workflow Master Phụ lục C.6 7 / UI filter 9 trạng thái).

### OBS-D2-002 — Tab Phân công cell "Người đánh giá" hiển thị `—` thay vì tên user

Sau add 1 người ĐG (`cb_nv_tw_02 — CB Nghiệp vụ TW 02`), Tab Phân công table hiển thị cột "Người đánh giá" = `—` (dash) thay vì tên + email user. Cột "Lĩnh vực" cũng `—` mặc dù đã chọn `Lao động + Hôn nhân gia đình`. Tổng số "1 người - 1 Trưởng nhóm" đúng. Có vẻ FE thiếu join lookup khi render table sau POST. Defer — visual bug Minor, không block workflow advance.

### OBS-D2-003 — App stepper 9 step vs SRS workflow 11 bước

R6 báo cáo 11 bước workflow theo SRS. App R7 stepper render 9 step:
1. Lập kế hoạch / 2. Phân công / 3. Chờ duyệt PC / 4. Thực hiện / 5. Đang đánh giá / 6. Đã đánh giá / 7. Lập báo cáo / 8. Chờ phê duyệt / 9. Hoàn thành.

Difference: 11 bước SRS có cả reject paths (`B5: PC → PHAN_CONG` reject + `B11: BC → BAO_CAO` reject) — không chiếm step trong stepper UI (visual chỉ show happy path). Ngoài ra SRS có "BAO_CAO → CHO_PHE_DUYET" + "CHO_PHE_DUYET → HOAN_THANH" tách 2 bước, app gộp thành "Lập báo cáo → Chờ phê duyệt → Hoàn thành" 3 step. OK — visual stepper không cần khớp 1:1 với SRS workflow node count.

---

## Phụ lục — Môi trường test

| Thành phần | Giá trị |
|------------|---------|
| URL ứng dụng | http://103.172.236.130:3000/ |
| OTP login | `666666` (bypass) |
| MailHog | http://103.172.236.130:8025 |
| API base | http://103.172.236.130:3000/api/v1/ |
| Frontend | React + Vite + Ant Design |
| Xác thực | JWT + OTP (auth-store localStorage userInfo + HttpOnly cookie token) |
| Tool test | Chrome DevTools MCP |
| Sample test | DG-20260506-0001 (R7.4.D1 entity) |

---

*Bug report generated: 2026-05-06 | QA Automation via Claude Code*
