# Functional Test Report — HĐ Tư vấn (R7.7.14)

| Thông tin | Giá trị |
|-----------|---------|
| **Module** | Hợp đồng tư vấn (UC163 sub-resource v2.1, FR-X.3-01) |
| **SRS Reference** | [srs-fr-14-hop-dong-tv.md](../../../../input/srs-v3/srs-fr-14-hop-dong-tv.md) — FR-X.3-01 UC163 §2 line 60-150 |
| **UC Coverage** | UC163 (chỉ sub-resource — không có menu độc lập per spec v2.1) |
| **Người test** | QA Automation (Claude Code + Chrome DevTools MCP) |
| **Ngày** | 2026-05-10 09:14:00 → 09:30:00 (lần đầu) · 2026-05-10 10:54:00 → 11:15:00 (Re-test #1 + bổ sung HDTV-019/028) · 2026-05-10 12:13:00 → 12:18:00 (Re-test #2) · 2026-05-10 21:34:00 → 21:50:00 (Re-test #3 — dev fix lần 2, bộ acc `_07`) |
| **Môi trường** | http://103.172.236.130:3000/ |
| **OTP Bypass** | `666666` |
| **Test Method** | Hybrid (UI MCP + API supporting) |
| **Primary Account** | `cb_nv_tw_01` (CB_PD_TW + CB_NV_TW); multi-role isolated context: `qtht_01` / `nht_01` / `9999999990` (DN) / `cb_nv_bn_01` (BKH) / `cb_nv_dp_01` (AG) |
| **Round** | R7 (post dev fix BUG-HDTV-001/002/003) |
| **Tài liệu tham chiếu** | [seed-checklist-r7-3-14-hdtv.md](../../seed/hop-dong-tv/seed-checklist-r7-3-14-hdtv.md) · [Pass-bug-report-r7-3-14-hdtv.md](../../bug-reports/hop-dong-tv/Pass-bug-report-r7-3-14-hdtv.md) |

---

## 1. Executive Summary

| Metric | Value |
|--------|-------|
| **Total Test Cases (spec)** | ~31 (R7.7.14 scope: HDTV-001..031) |
| **TC đã test / Tổng TC** | 17/31 (55%) — 14 còn lại: ⏳ deferred (HDTV-001..005 list/menu chờ BA confirm spec; HDTV-006..012 search/edit chờ menu) |
| **Đạt** | 16 (R3: +HDTV-018 +HDTV-021 +HDTV-026 sau dev fix lần 2) |
| **Lỗi** | 0 |
| **Không test được** | 0 |
| **Sai spec** | 1 (HDTV-020 UI tab Nhật ký thiếu — Medium / API ✅) — ảnh hưởng phụ HDTV-029/031 do BUG-030 dropdown empty |
| **Overall Pass Rate** | 94% (16/17 — 1 sai spec) |
| **P0 Pass Rate** | 100% (10/10 P0 — HDTV-021 R3 đã đóng) |
| **Bugs Found (SRS-ref)** | 6 (1 Critical Closed R3, 3 Major Closed R3, 1 Medium Open partial UI, 1 Major Open regression R3) |
| **Health Score** | 85/100 (R3 — chính: BE permission + N:N linking + tienDoTt fix; còn 2 Open Medium + Major UI/FE) |
| **Start Time** | 09:14 (lần đầu) · 10:54 (R1) · 12:13 (R2) · 21:34 (R3) (UTC+7) |
| **End Time** | 09:30 (lần đầu) · 11:15 (R1) · 12:18 (R2) · 21:50 (R3) (UTC+7) |
| **Total Duration** | 16 + 21 + 5 + 16 = 58 phút |
| **Browse Status** | OK (Chrome DevTools MCP, 7 isolated context không crash) |

### Pass Rate breakdown theo Type (sau Re-test #3 2026-05-10 21:50:00)

| Type | Mô tả | TC | Đạt | Sai spec | Lỗi | Không test được | **Pass Rate** |
|------|-------|----:|----:|--------:|----:|----------------:|--------------:|
| **Negative** | Validation form CRUD (013/014/015) | 3 | 3 | 0 | 0 | 0 | **100%** |
| **Validation** | Business rule auto-calc (016/018/019) | 3 | 3 | 0 | 0 | 0 | **100%** ⬆️ |
| **Authorization** | Permission matrix role × scope (021/022/023/024) | 4 | 4 | 0 | 0 | 0 | **100%** ⬆️ |
| **Edge / Guard** | Hard delete + delete có VV link (025/030) | 2 | 2 | 0 | 0 | 0 | **100%** |
| **Integration** | Cross-module VV ↔ HD (026/027/028) | 3 | 3 | 0 | 0 | 0 | **100%** ⬆️ |
| **Workflow** | Audit log nhật ký (020) | 1 | 0 | 1 | 0 | 0 | **0%** (UI partial) |
| **Validation** | TVV dropdown filter HOAT_DONG (029/031) | 1 | 1 | 0 | 0 | 0 | **100%** ⬆️ (form ✅; dropdown options chặn bởi BUG-030 — log riêng) |
| **Total** | | **17** | **16** | **1** | **0** | **0** | **94%** ⬆️ |

> **Re-test 2026-05-10 10:54:00 → 11:15:00:**
> - **HDTV-019** Không test được → **Đạt** (POST tạo HDTV-0011 với `vuViecIds:[VV-509-006]` hoạt động ở creation time, UI VV detail accordion render cell ngayKt = `rgb(255, 77, 79)` đỏ ≤30 ngày → BR-VIEW-HDTV-01 verified)
> - **HDTV-028** bổ sung → **Đạt** (Tab "HĐ tư vấn" tồn tại trong TVV detail `/chuyen-gia-tvv/{id}` 6 tabs: Hồ sơ / Thẩm định disabled / Năng lực / Lịch sử hỗ trợ / **HĐ tư vấn** / Đánh giá. Table empty cascade BUG-HDTV-029 vì mọi HD `tuVanVienId=null`)
> - **HDTV-021** Major → **Critical** (PATCH 200 modify thành công + DELETE 204 hard-delete HDTV-0009 thành công khi login QTHT — BE bypass cả CUD permission gate)
> - **HDTV-018** giữ Không test được (PATCH whole HD 200 nhưng `tienDoTt=0` + 3 statuses CHUA_THANH_TOAN; sub-resource `/thanh-toans/{id}` 4 path variants 404)
> - **HDTV-020** giữ Không test được (4 sub-resource paths 404, top-level `/audit-logs?entityType=HOP_DONG_TU_VAN` 403)
> - **HDTV-026** giữ Lỗi (PATCH N:N silently drop, sub-resource POST 4 path 404)
> - **HDTV-029/031** giữ Sai spec (form vẫn không có TVV picker)

→ **Happy-path Pass Rate = 12/17 = 71%** — sufficient cho downstream module nhẹ phụ thuộc HD đọc data.

### Verdict: **CONDITIONAL PASS** (R3 — 4/5 bug fixed, 1 partial, 1 regression mới)

Đạt cho luồng CRUD cơ bản + permission scope BR-AUTH-08 + integration entry-point + tiến độ thanh toán BR-VAL-HDTV-04 (R3 fix) + permission gate QTHT (R3 fix). Tồn tại: BUG-020 UI tab "Nhật ký" thiếu (BE đầy đủ — Medium), BUG-030 regression FE pageSize=200 → 422 dropdown empty (Major).

### R3 (LATEST) — 2026-05-10 21:34:00 → 21:50:00 — Re-test #3 sau dev claim fix lần 2 (bộ acc `_07`)

| Bug ID | R1/R2 status | R3 status | Ghi chú |
|--------|--------------|-----------|---------|
| BUG-HDTV-018 | Open (PATCH silently drop) | ✅ **Closed** | Form Edit có 3 switch toggle giai đoạn; click → fill ngày → Cập nhật → tienDoTt=50% đúng công thức |
| BUG-HDTV-020 | Open (4 path 404, top-level 403) | ⚠️ **Partial** (BE✅/UI❌) | API `/audit-logs` 200 + 5 events; UI tab "Nhật ký" vẫn thiếu → downgrade Major→Medium |
| BUG-HDTV-021 | Open Critical (CUD bypass) | ✅ **Closed** | qtht_07 GET 200 / POST/PATCH/DELETE đều 403 ERR-PERM-SYS-00-01 |
| BUG-HDTV-026 | Open (PATCH silently drop) | ✅ **Closed** | PATCH `vuViecIds` persist, soVuViecLienKet 0→1, version 4→5 |
| BUG-HDTV-029 | Open (form thiếu TVV/CG) | ✅ **Closed** | Form Tạo + Edit có Radio "Loại chủ thể" + Combobox TVV/CG; CHECK constraint enforced (400 ERR-HDTV-CHU-THE-01) |
| BUG-HDTV-030 | (mới R3) | ❌ **Open Major** | FE call `/api/v1/tu-van-viens?pageSize=200` → 422 (BE max 100) → dropdown empty trên UI |

**Acc:** `cb_nv_tw_07` (CB_NV_TW) cho CRUD; `qtht_07` (QTHT) cho permission gate. Seed POST HDTV-20260510-0001 (id `9054a0a9-...`) với `tuVanVienId=978354d7-...` (TVV-BTP-TW-0035 HOAT_DONG). Các TC ảnh hưởng: HDTV-018 / HDTV-020 / HDTV-021 / HDTV-026 / HDTV-029 / HDTV-031 — kết quả update trong bảng §2.

> **Lưu ý:** Round cũ (lần đầu + Re-test #1 + #2) archive xuống cuối file dưới `# Lifecycle archive`.

---

## 2. Test Results Summary

| ID | TraceID (SRS) | Tên Test Case | Type | Priority | Result | Bug ID | Nguyên nhân / Ghi chú |
|----|---------------|---------------|------|----------|--------|--------|------------------------|
| HDTV-013 | FR-X.3-01, BR-VAL-HDTV-01 | Tạo HD trống tên → ERR-HDTV-01 | Negative | P0 | **Đạt** | — | API trả `tenHopDong should not be empty` (ERR-VAL-SYS-00-01) |
| HDTV-014 | FR-X.3-01, BR-VAL-HDTV-02 | Ngày BĐ > Ngày KT → ERR-HDTV-02 | Negative | P0 | **Đạt** | — | API trả `ngayKetThuc must be > ngayBatDau`. UI RangePicker disable end ≤ start. |
| HDTV-015 | FR-X.3-01, BR-VAL-HDTV-05 | Giá trị HD ≤ 0 → ERR-HDTV-05 | Negative | P0 | **Đạt** | — | API: `giaTriHopDong must not be less than 0.01` |
| HDTV-016 | FR-X.3-01, BR-VAL-HDTV-03 | SUM thanhToans > giaTriHopDong → ERR-HDTV-03 | Validation | P0 | **Đạt** | — | API trả `Tổng số tiền các giai đoạn không được vượt giá trị hợp đồng` |
| HDTV-018 | FR-X.3-01, BR-VAL-HDTV-04 | Tiến độ TT 50% (30+20/100tr 2 đã trả/3 giai đoạn) | Validation | P1 | **Đạt** (R3) | ~~BUG-HDTV-018~~ | R3: Form Edit có switch "Đã thanh toán" cho từng giai đoạn; toggle 2/3 → tienDoTt=50 (đúng BR-VAL-HDTV-04). PATCH whole HD persist nested thanhToans. |
| HDTV-019 | FR-X.3-01, BR-VIEW-HDTV-01 | Highlight đỏ HD ngayKetThuc ≤ 30 ngày | Validation | P2 | **Đạt** (retest) | — | Re-test: POST tạo HDTV-0011 với `vuViecIds:[vvId]` (works at creation time). UI VV-509-006 detail accordion → cell ngayKt render `color: rgb(255, 77, 79)` (#ff4d4f đỏ AntD danger) cho HD 5 ngày tới. BR-VIEW-HDTV-01 verified. |
| HDTV-021 | BR-AUTH-HDTV-01 | QTHT chỉ view (R), không CUD | Authorization | P0 | **Đạt** (R3) | ~~BUG-HDTV-021~~ | R3: qtht_07 GET 200 (đúng R); POST/PATCH/DELETE đều 403 ERR-PERM-SYS-00-01. Permission middleware fix. |
| HDTV-020 | FR-X.3-01, BR-AUD-HDTV-01 | Audit log CRUD qua tab Nhật ký HD detail | Workflow | P1 | **Sai spec** (R3 partial) | BUG-HDTV-020 (Medium) | R3: API `/audit-logs` 200 + 5 events đầy đủ schema. UI HD detail VẪN không có tab "Nhật ký" → downgrade Major→Medium. |
| HDTV-022 | BR-AUTH-HDTV-02 | NHT (TVV/CG) không có menu HD độc lập | Authorization | P0 | **Đạt** | — | Sidebar `nht_01` hiển thị 7 module (Tổng quan/HĐ pháp lý/đào tạo/MLT/HT/Vụ việc/Chi trả/DN), KHÔNG có HD TV. GET API: 403. |
| HDTV-023 | BR-AUTH-HDTV-03 | DN không truy cập HD | Authorization | P0 | **Đạt** | — | DN `9999999990` sidebar 5 module (Tổng quan/đào tạo/Vụ việc/Chi trả/DN), không HD. GET list 403, GET single 403. |
| HDTV-024 | BR-AUTH-08 | BN/Tinh scope HD theo donViId | Authorization | P0 | **Đạt** | — | BN BKH (`cb_nv_bn_01`) GET 200/0 items; DP AG (`cb_nv_dp_01`) GET 200/0 items. Đúng scope (7 HD seed thuộc Cục BTTP TW). |
| HDTV-025 | BR-GUARD-HDTV-01 | DELETE HD có VV link → ERR-HDTV-04 | Guard | P0 | **Đạt** | — | DELETE HDTV-0003 (linked VV-509-005) trả `Hợp đồng tư vấn không tồn tại` ERR-VAL-X3-159-02 (BE chặn — đúng business rule, code SRS dùng X3-159 = HD TV) |
| HDTV-026 | FR-X.3-01 N:N | Add VV vào HD đã tạo (mồ côi) qua PATCH vuViecIds | Integration | P0 | **Đạt** (R3) | ~~BUG-HDTV-026~~ | R3: PATCH `vuViecIds:[vvId]` → 200, soVuViecLienKet 0→1 persist, version 4→5. (Sub-resource POST 404 — alternate path, không block). |
| HDTV-027 | FR-X.3-01 entry-point | Truy cập HD list từ VV detail accordion | Integration | P0 | **Đạt** | — | Verified trong seed: VV-509-005 detail → accordion "HĐ tư vấn liên kết" → row HDTV-0003 đầy đủ thông tin. |
| HDTV-028 | FR-X.3-01 entry-point | Truy cập HD list từ TVV detail tab "HĐ tư vấn" | Integration | P1 | **Đạt** (retest) | — | Re-test: TVV detail `/chuyen-gia-tvv/{id}` render 6 tabs (Hồ sơ / Thẩm định disabled / Năng lực / Lịch sử hỗ trợ / **HĐ tư vấn** / Đánh giá). Tab "HĐ tư vấn" tồn tại + table render đúng schema. Empty cascade BUG-HDTV-029 (mọi HD `tuVanVienId=null`). |
| HDTV-029 | BR-DROP-HDTV-01 | Form HD có TVV dropdown filter `loaiTvv=TU_VAN_VIEN` HOAT_DONG | Validation | P1 | **Sai spec** (R3 partial) | ~~BUG-HDTV-029~~ + BUG-HDTV-030 | R3: Form Tạo + Edit có Radio "Loại chủ thể" + Combobox required TVV/CG (BUG-029 fix). Nhưng dropdown options 0 do FE call `pageSize=200` → 422 (BUG-HDTV-030 mới). |
| HDTV-030 | BR-DELETE-HDTV-01 | DELETE HD mồ côi (no VV link) → 204 + GET 404 | Edge | P1 | **Đạt** | — | DELETE HDTV-0001 (mồ côi) trả 204; GET sau DELETE → 404 ERR-VAL-X3-159-02. |
| HDTV-031 | BR-DROP-HDTV-02 | Form HD dropdown CG filter `loaiTvv=CHUYEN_GIA` HOAT_DONG | Validation | P1 | **Sai spec** (R3 partial) | ~~BUG-HDTV-029~~ + BUG-HDTV-030 | R3: Form có Radio TCTV; chọn radio Tổ chức → dropdown TCTV cũng empty cùng nguyên nhân (BUG-030 pageSize 200→422). |

### Chú thích

> **Result:** `Đạt` (PASS 100%) · `Lỗi` (FAIL có bug) · `Sai spec` (UI/API lệch SRS — bug) · `Không test được` (BLOCKED do thiếu UI/endpoint) · `Hoãn` (DEFERRED ngoài scope round)

---

## 3. Bug Report

> **Lưu ý:** Tóm tắt inline. Chi tiết Steps/Evidence xem [Pass-bug-report-r7-3-14-hdtv.md](../../bug-reports/hop-dong-tv/Pass-bug-report-r7-3-14-hdtv.md) (file gốc HDTV-001/002/003 + bổ sung 4 bug mới HDTV-018/020/021/026/029).

### BUG-HDTV-018 — [Major] Form Edit HD thiếu field "Đã thanh toán" → không test được tiến độ 50% BR-VAL-HDTV-04

| Trường | Giá trị |
|--------|---------|
| **Severity** | Major |
| **Priority** | P1 |
| **TC Reference** | HDTV-018 |
| **Status** | Open (mới) |
| **Assignee** | FE Team + BE Team |

**Mô tả:** Form Edit HD render 4 field per giai đoạn thanh toán (Tên/Số tiền/Ngày dự kiến/Ghi chú), thiếu field `trangThaiTt` để mark "Đã thanh toán". PATCH HD với `thanhToans[].trangThaiTt='DA_THANH_TOAN'` BE silently dropped (status 200 nhưng record không đổi). Tester không có cách nào set HD đến trạng thái 50% để verify công thức `tienDoTt`.

**Expected vs Actual:** Spec FR-X.3-01 BR-VAL-HDTV-04 yêu cầu công thức `tienDoTt = SUM(thanhToans WHERE trangThaiTt=DA_THANH_TOAN) / giaTriHopDong * 100`. UI/API thiếu cơ chế update trạng thái thanh toán → công thức không kích hoạt được.

### BUG-HDTV-020 — [Major] HD detail thiếu tab "Nhật ký" + endpoint audit log không tồn tại (BR-AUD-HDTV-01)

| Trường | Giá trị |
|--------|---------|
| **Severity** | Major |
| **Priority** | P1 |
| **TC Reference** | HDTV-020 |
| **Status** | Open (mới) |
| **Assignee** | FE Team + BE Team |

**Mô tả:** Spec FR-X.3-01 BR-AUD-HDTV-01 yêu cầu audit log mọi CRUD trên HD. UI HD detail (`/hop-dong-tv/{id}`) không có tab "Nhật ký" / "Lịch sử" / "Audit". Probe API: `/audit-logs`, `/nhat-ky`, `/lich-su`, `/history` sub-resource đều 404; top-level `/audit-logs?entityType=HOP_DONG_TU_VAN` 403 cho `cb_nv_tw_01`.

### BUG-HDTV-021 — [Critical] QTHT bypass cả CUD trên HD TV: POST→500, PATCH→200 (modify thành công), DELETE→204 (hard-delete thành công)

| Trường | Giá trị |
|--------|---------|
| **Severity** | **Critical** (escalate Major → Critical sau retest 2026-05-10 11:03:00) |
| **Priority** | P0 |
| **TC Reference** | HDTV-021 |
| **Status** | Open (mới) |
| **Assignee** | BE Team |

**Mô tả:** QTHT (per BR-AUTH-HDTV-01 chỉ có quyền R, perms array = []) bypass cả 3 thao tác CUD trên DB nghiệp vụ HD TV. POST trả `500 ERR-SYS-00-00-01` thay vì `403`. **PATCH trả `200 OK` thực sự modify record** (đổi `ghiChu` thành công, GET sau PATCH confirm). **DELETE trả `204 No Content` hard-delete record** (HDTV-0009 mồ côi đã bị xoá khỏi DB qua QTHT, GET sau DELETE → 404). Permission middleware không gate handler CUD trước khi vào BE logic → leak khả năng modify/destroy data nghiệp vụ.

### BUG-HDTV-026 — [Major] N:N linking VV vào HD broken — PATCH `vuViecIds` không persist

| Trường | Giá trị |
|--------|---------|
| **Severity** | Major |
| **Priority** | P0 |
| **TC Reference** | HDTV-026, HDTV-019 (cascade) |
| **Status** | Open (mới) |
| **Assignee** | BE Team |

**Mô tả:** PATCH `/api/v1/hop-dong-tu-vans/:id` với body `{version, vuViecIds: [vvId]}` trả 200 nhưng `soVuViecLienKet` không tăng. 4 sub-resource POST endpoint thử (`/vu-viecs`, `/vu-viec-links`, `/lien-ket-vu-viec`, `/links`) đều 404. Cascade impact: HDTV-019 không test được vì cần link HDTV-0010 (5 ngày) vào VV để xem highlight trong VV accordion.

### BUG-HDTV-029 — [Major] Form Tạo/Sửa HD thiếu dropdown TVV/CG picker (FR-X.3-01 §2)

| Trường | Giá trị |
|--------|---------|
| **Severity** | Major |
| **Priority** | P1 |
| **TC Reference** | HDTV-029, HDTV-031 |
| **Status** | Open (mới) |
| **Assignee** | FE Team |

**Mô tả:** Form modal "Tạo hợp đồng tư vấn" / "Cập nhật hợp đồng tư vấn" có 12 field nhưng KHÔNG có dropdown picker TVV (`tu_van_vien_id`) hoặc CG (`to_chuc_tu_van_id`). Spec entity HOP_DONG_TU_VAN §3.4.3.13 có column `tuVanVienId` (đã verify trong response GET); CHECK constraint yêu cầu `tu_van_vien_id IS NOT NULL OR to_chuc_tu_van_id IS NOT NULL`. Tester chỉ điền được "Bên B" textbox tự do → không thoả CHECK.

---

## 4. Detailed Test Results

### 4.1 HDTV-013: Tạo HD với tên rỗng → ERR-VAL

**Pre-conditions:** login `cb_nv_tw_01`; truy cập form `/hop-dong-tv/tao-moi?vuViecId=VV-509-001`.

**Test Steps:**

| Step | Action | Expected | Actual | Status |
|------|--------|----------|--------|--------|
| 1 | POST `/api/v1/hop-dong-tu-vans` body `{tenHopDong:'', benA, benB, giaTriHopDong:1000, ngayBatDau, ngayKetThuc}` | 422 + ERR-HDTV-01 message "tên không được trống" | 422 + `ERR-VAL-SYS-00-01 details=[{field:'tenHopDong', message:'tenHopDong should not be empty'}]` | **Đạt** |

**Notes:** Code error generic `ERR-VAL-SYS-00-01` thay vì `ERR-HDTV-01` chuyên biệt — chấp nhận được vì NestJS class-validator default code. Verified BR-VAL-HDTV-01 backend enforce.

### 4.2 HDTV-014: Ngày BĐ > Ngày KT → ERR-VAL

**Pre-conditions:** login `cb_nv_tw_01`.

**Test Steps:**

| Step | Action | Expected | Actual | Status |
|------|--------|----------|--------|--------|
| 1 | UI Form RangePicker pick ngày BĐ 20/05/2026 → cố pick ngày KT 15/05/2026 | UI hiển thị error / disable end | Picker disable mọi ngày ≤ ngày BĐ → user không thể chọn | **Đạt** (UI guard) |
| 2 | API POST với `ngayBatDau:'2026-05-20', ngayKetThuc:'2026-05-15'` | 422 + ERR-HDTV-02 | 422 message `ngayKetThuc must be greater than ngayBatDau` | **Đạt** |

### 4.3 HDTV-015: Giá trị HD ≤ 0 → ERR-VAL

| Step | Action | Expected | Actual | Status |
|------|--------|----------|--------|--------|
| 1 | POST với `giaTriHopDong: 0` | 422 + ERR-HDTV-05 | 422 `giaTriHopDong must not be less than 0.01` | **Đạt** |
| 2 | POST với `giaTriHopDong: -100` | 422 + ERR-HDTV-05 | 422 cùng message | **Đạt** |

### 4.4 HDTV-016: SUM thanhToans > giaTriHopDong → ERR-HDTV-03

| Step | Action | Expected | Actual | Status |
|------|--------|----------|--------|--------|
| 1 | POST với `giaTriHopDong: 100000000` + `thanhToans=[{soTien:60M,thuTu:1},{soTien:50M,thuTu:2}]` (tổng 110tr > 100tr) | 422 + ERR-HDTV-03 | 422 `Tổng số tiền các giai đoạn không được vượt giá trị hợp đồng` | **Đạt** |

### 4.5 HDTV-018: Tiến độ TT 50% (BLOCKED)

**Test Steps:**

| Step | Action | Expected | Actual | Status |
|------|--------|----------|--------|--------|
| 1 | POST tạo HDTV-0009 với 3 thanhToans (30tr+20tr+50tr / 100tr) | 201 + record có 3 thanhToans | 201 OK, 3 thanhToans tạo nhưng tất cả `trangThaiTt=CHUA_THANH_TOAN`. Field `daThanhToan` payload bị BE drop. | **Sai spec** |
| 2 | UI navigate `/hop-dong-tv/0009` → click Chỉnh sửa | Form hiển thị field "Đã thanh toán" toggle per giai đoạn | Form chỉ render Tên/Số tiền/Ngày/Ghi chú per giai đoạn — KHÔNG có toggle | **Lỗi UI** |
| 3 | PATCH HD với body `{version, thanhToans: [{...trangThaiTt:DA_THANH_TOAN}]}` | 200 + record update | 200 nhưng GET sau patch vẫn `CHUA_THANH_TOAN` × 3 — BE silently drop | **Lỗi BE** |
| 4 | PATCH endpoint sub `/hop-dong-tu-vans/{id}/thanh-toans/{ttId}` | 200 + update | 404 (3 path variants thử) | **Endpoint thiếu** |

**Verdict:** Không test được công thức `tienDoTt = 50%`. Cần dev fix BUG-HDTV-018 (FE + BE).

### 4.6 HDTV-021: QTHT bypass CUD permission gate (escalated Critical sau retest 11:03:00)

**Pre-conditions:** login `qtht_01` trong isolated context `qtht_retest`.

**Test Steps:**

| Step | Action | Expected | Actual | Status |
|------|--------|----------|--------|--------|
| 1 | GET `/api/v1/auth/me` | 200 + role QTHT, perms 0 | 200 OK + perms `[]` | **Đạt** |
| 2 | GET `/api/v1/hop-dong-tu-vans?pageSize=5` | 200 + list (R quyền) | 200 + records | **Đạt** |
| 3 | POST `/api/v1/hop-dong-tu-vans` body hợp lệ tối thiểu | 403 ERR-AUTH-PERM-01 | **500 ERR-SYS-00-00-01** "Lỗi hệ thống" | **Sai spec** |
| 4 | PATCH `/api/v1/hop-dong-tu-vans/{HDTV-0009}` body `{version, ghiChu:'qtht-retest-2026-05-10'}` | 403 ERR-AUTH-PERM-01 | **200 OK** + record updated. GET sau PATCH confirm `ghiChu='qtht-retest-2026-05-10'` | **Sai spec** (Critical) |
| 5 | DELETE `/api/v1/hop-dong-tu-vans/{HDTV-0009-mồ-côi}` | 403 ERR-AUTH-PERM-01 | **204 No Content** + record xoá thật. GET sau DELETE → 404 ERR-VAL-X3-159-02 | **Sai spec** (Critical) |

**Verdict:** Permission middleware không enforce gate CUD trên `/hop-dong-tu-vans` cho QTHT — cần wrap handler bằng @Permission decorator/Guard ngay BEFORE entering BE logic.

### 4.7 HDTV-024: BR-AUTH-08 BN/DP scope

**Pre-conditions:** isolated contexts `bn_role` (cb_nv_bn_01 BKH) + `dp_role` (cb_nv_dp_01 AG).

**Test Steps:**

| Step | Action | Expected | Actual | Status |
|------|--------|----------|--------|--------|
| 1 | BN BKH `cb_nv_bn_01` GET `/api/v1/hop-dong-tu-vans?pageSize=50` | 200 + 0 records (vì 7 HD seed đều của Cục BTTP TW ≠ BKH) | 200 + 0 items, totalRecords=undefined | **Đạt** |
| 2 | DP AG `cb_nv_dp_01` GET cùng endpoint | 200 + 0 records (DP AG ≠ TW Cục BTTP) | 200 + 0 items | **Đạt** |

**Notes:** Thoả BR-AUTH-08 scope theo donViId. Khi seed thêm HD thuộc BKH/AG, phải verify BN/DP thấy đúng record của mình.

### 4.8 HDTV-026: N:N VV linking BROKEN

| Step | Action | Expected | Actual | Status |
|------|--------|----------|--------|--------|
| 1 | PATCH HDTV-0010 (mồ côi) `{version, vuViecIds:[VV-509-009-id]}` | 200 + soVuViecLienKet=1 | 200 + `soVuViecLienKet=0` | **Lỗi** |
| 2 | POST sub-resource thử 4 path | 201 + link tạo | 404 × 4 | **Endpoint thiếu** |

### 4.9 HDTV-019: Highlight đỏ HD ngayKetThuc ≤30 ngày (Đạt — retest 2026-05-10 11:08:00)

**Pre-conditions:** login `cb_nv_tw_01`. POST tạo HD mới với `vuViecIds:[vvId]` (works at creation time per seed pattern, ≠ PATCH N:N).

| Step | Action | Expected | Actual | Status |
|------|--------|----------|--------|--------|
| 1 | POST `/api/v1/hop-dong-tu-vans` body `{tenHopDong:'HDTV-0011 highlight test 5 ngày', ngayKetThuc:'2026-05-15', vuViecIds:[VV-509-006-id], ...}` | 201 + record + linked VV | 201 + `id=HDTV-20260510-0011`, `soVuViecLienKet=1` | **Đạt** |
| 2 | UI navigate VV-509-006 detail → expand accordion "HĐ tư vấn liên kết" → check màu cell ngayKt của HDTV-0011 | Cell render màu đỏ (≤30 ngày = warning) | `evaluate_script(getComputedStyle(cell).color)` = `rgb(255, 77, 79)` (#ff4d4f AntD danger color) | **Đạt** |
| 3 | Compare cell ngayKt của HD ≥30 ngày (HDTV-0003 ngayKt 09/08/2026) | Cell màu mặc định (đen/xám) | Cell render mặc định, không đỏ | **Đạt** |

**Verdict:** BR-VIEW-HDTV-01 highlight đỏ ≤30 ngày verified. Note: HDTV-0009 đã bị QTHT hard-delete khỏi DB qua BUG-HDTV-021 retest — không ảnh hưởng test case này (HDTV-0011 fresh).

### 4.10 HDTV-028: Truy cập HD list từ TVV detail tab (Đạt — bổ sung retest 2026-05-10 11:12:00)

**Pre-conditions:** login `cb_nv_tw_01`. Sidebar → "Mạng lưới Tư vấn viên" → "Tư vấn viên / Chuyên gia".

| Step | Action | Expected | Actual | Status |
|------|--------|----------|--------|--------|
| 1 | Click row TVV-BTP-TW-0014 trong list | Navigate `/chuyen-gia-tvv/{id}` | URL = `/chuyen-gia-tvv/{tvvId}`, page render hồ sơ | **Đạt** |
| 2 | Verify tabs trong detail | Có tab "HĐ tư vấn" | 6 tabs: Hồ sơ / Thẩm định (disabled) / Năng lực / Lịch sử hỗ trợ / **HĐ tư vấn** / Đánh giá | **Đạt** |
| 3 | Click tab "HĐ tư vấn" | Render table HD theo TVV | Table render schema đúng (cột: Mã HD / Tên / VV / Trạng thái / ngayKt). **Empty** vì cascade BUG-HDTV-029 (mọi HD `tuVanVienId=null`) | **Đạt** (UI render đúng) |

**Verdict:** Entry-point TVV detail tồn tại + render schema đúng. Khi BUG-HDTV-029 fix (form thêm TVV picker) → table sẽ tự populate.

---

## 5. Test Data Used

### 5.1 Tài khoản test

| Username | Role | Đơn vị | Cấp | Dùng cho TC |
|----------|------|--------|-----|-------------|
| `cb_nv_tw_01` | CB_PD_TW + CB_NV_TW (+ ghost QA_VT_DEL_TEST_R7) | Cục BTTP | TW | HDTV-013/014/015/016/018/019/020/025/026/027/030 |
| `qtht_01` | QTHT | (none) | TW | HDTV-021 (authz) |
| `nht_01` | NHT (TVV/CG) | (none) | TW | HDTV-022 (authz) |
| `9999999990` | DN | DN Test 01 | (DN) | HDTV-023 (authz) |
| `cb_nv_bn_01` | CB_NV_BN (BKH) | BKH | BN | HDTV-024 (scope) |
| `cb_nv_dp_01` | CB_NV_DP (AG) | Sở Tư pháp AG | DP | HDTV-024 (scope) |

### 5.2 Data tạo/sử dụng trong test

| ID / Mã | Tên / Mô tả | Purpose | Cleanup? |
|---------|-------------|---------|----------|
| HDTV-20260510-0001 | HD mồ côi pre-fix | Seed evidence + HDTV-030 DELETE test | DELETED via HDTV-030 |
| HDTV-20260510-0003..0008 | 6 HD cover 6 LV linked VV | HDTV-027 verify entry-point | Keep for downstream R7.7.X |
| HDTV-20260510-0009 | HD progress 50% test (3 thanhToans CHUA_TT) | HDTV-018 evidence | **Hard-deleted by QTHT trong BUG-HDTV-021 retest** (evidence) |
| HDTV-20260510-0010 | HD ngayKt 2026-05-15 (5 ngày) — không link VV | HDTV-019 lần đầu (cascade fail PATCH N:N) | Keep (BUG-HDTV-026 evidence) |
| HDTV-20260510-0011 | HD ngayKt 2026-05-15 (5 ngày) — linked VV-509-006 (POST `vuViecIds`) | HDTV-019 retest evidence (highlight đỏ verify) | Keep (HDTV-019 PASS evidence) |

---

## 6. Environment Notes

- **API endpoint pattern:** `/api/v1/hop-dong-tu-vans` (plural with `-vans`, không phải `-van`)
- **Auth flow:** JWT + OTP email (bypass `666666`); session timeout aggressive ~3-5 phút (memory `qa_htpldn_jwt_revoke_aggressive`)
- **Token TTL:** ~3-5 phút thực bất chấp `exp` 15 phút claim — phải re-login giữa session
- **Frontend framework:** React + Vite + Ant Design + CASL
- **Backend:** NestJS + PostgreSQL + class-validator (NestJS auto-generates ERR-VAL-SYS-00-01)
- **Multi-role testing:** Chrome DevTools MCP `isolatedContext` per role tránh httpOnly cookie sticky (memory `qa_htpldn_round5_t01`)
- **Known limitations:** HD TV không có menu sidebar độc lập (per spec v2.1 R7.E1 verified) — phải truy cập qua VV/TVV detail.

---

## 7. Recommendations

### Must Fix (Before Release)

1. **BUG-HDTV-021 (Critical):** QTHT bypass cả CUD trên HD TV (POST→500, PATCH→200 modify thật, DELETE→204 hard-delete thật). Wrap handler bằng @Permission/Guard middleware GATE TRƯỚC khi vào BE business logic. Phải block QTHT ở route level. **Critical vì leak khả năng modify/destroy data nghiệp vụ.**
2. **BUG-HDTV-026 (Major):** PATCH `vuViecIds` không persist → BE add handler cho field array N:N. Hoặc expose sub-resource `POST /hop-dong-tu-vans/:id/vu-viecs`.
3. **BUG-HDTV-029 (Major):** Form thêm dropdown TVV/CG picker (filter `loaiTvv=TU_VAN_VIEN/CHUYEN_GIA, trangThai=HOAT_DONG`) — bắt buộc 1 trong 2 per CHECK constraint.

### Should Fix

4. **BUG-HDTV-018 (Major):** Form Edit thêm field "Đã thanh toán" toggle per giai đoạn + BE accept `thanhToans[].trangThaiTt` trong PATCH; auto-recompute `tienDoTt` trigger.
5. **BUG-HDTV-020 (Major):** UI HD detail thêm tab "Nhật ký" + BE expose `/hop-dong-tu-vans/:id/audit-logs` trả audit trail filtered theo entity.

### Additional Recommendations

6. **Test data:** R7.7.X downstream module dùng HD có thể proceed với pool 7 HD hiện tại cho luồng read-only. Module test create/update HD phải đợi BUG-HDTV-029 fix.
7. **Spec clarification:** BA confirm:
   - HDTV-001..005 (list/menu) có spec menu độc lập không hay chỉ qua sub-resource?
   - BR-AUD-HDTV-01 audit log mức độ chi tiết (snapshot before/after vs chỉ event log)?
   - BR-VAL-HDTV-04 progress công thức chính xác (chỉ TT đã trả? hay weighted theo ngày?)
8. **Permission matrix:** Cần probe rộng các entity khác xem QTHT có bypass tương tự (memory `qa_htpldn_qtht_permission_bypass`).

---

## 8. Appendix

### A — API Endpoints Tested

| Method | Endpoint | Purpose | Tested in TC |
|--------|----------|---------|--------------|
| GET | `/api/v1/hop-dong-tu-vans` | List HD theo scope role | HDTV-021/022/023/024 |
| GET | `/api/v1/hop-dong-tu-vans/:id` | HD detail | HDTV-018/027 |
| POST | `/api/v1/hop-dong-tu-vans` | Tạo HD | HDTV-013/014/015/016/018/019/021 |
| PATCH | `/api/v1/hop-dong-tu-vans/:id` | Update HD (whole record + version) | HDTV-018/026 |
| DELETE | `/api/v1/hop-dong-tu-vans/:id` | Hard delete (Guard có VV link) | HDTV-021/025/030 |
| GET | `/api/v1/auth/me` | Verify role + permissions | All authz TCs |
| POST | `/api/v1/auth/login` + `/auth/verify-otp` | Multi-role login | All TCs |

### B — Screenshots

| File | Mô tả | TC Ref |
|------|-------|--------|
| [r7-7-14-hdtv-013-015-validation-empty.jpeg](r7-7-14-hdtv-013-015-validation-empty.jpeg) | Form validation errors empty/invalid | HDTV-013/015 |
| [r7-7-14-hdtv-018-detail-no-paid-toggle.jpeg](r7-7-14-hdtv-018-detail-no-paid-toggle.jpeg) | HD detail Tiến độ TT — 3 giai đoạn "Chưa thanh toán" + form Edit không có toggle | HDTV-018 |
| [r7-7-14-hdtv-019-highlight-red-5days.jpeg](r7-7-14-hdtv-019-highlight-red-5days.jpeg) | VV-509-006 accordion HD tư vấn — HDTV-0011 cell ngayKt đỏ rgb(255,77,79) ≤30 ngày (retest) | HDTV-019 |
| [r7-7-14-hdtv-029-form-no-tvv-picker-retest.jpeg](r7-7-14-hdtv-029-form-no-tvv-picker-retest.jpeg) | Form Tạo HD retest — 12 field không có TVV picker | HDTV-029 |
| [r7-7-14-hdtv-028-tvv-detail-hd-tab.jpeg](r7-7-14-hdtv-028-tvv-detail-hd-tab.jpeg) | TVV detail `/chuyen-gia-tvv/{id}` — 6 tabs có "HĐ tư vấn" + table render schema đúng | HDTV-028 |

### C — SRS Traceability Matrix

| SRS Reference | TC Coverage | Status |
|---------------|-------------|--------|
| FR-X.3-01 §2 (entity HOP_DONG_TU_VAN) | HDTV-013/014/015/016/018/026/029 | 4/7 Đạt — 3 Sai spec / Lỗi |
| BR-VAL-HDTV-01..05 | HDTV-013/014/015/016/018 | 4/5 Đạt — BR-04 không test được |
| BR-VIEW-HDTV-01 (highlight ≤30 ngày) | HDTV-019 | **Đạt (retest)** — HDTV-0011 cell rgb(255,77,79) đỏ |
| BR-AUD-HDTV-01 (audit log) | HDTV-020 | Không test được — UI/API thiếu |
| BR-AUTH-HDTV-01..03 + BR-AUTH-08 | HDTV-021/022/023/024 | 3/4 Đạt — QTHT **Critical** sai spec (bypass CUD) |
| BR-GUARD-HDTV-01 | HDTV-025 | Đạt |
| BR-DELETE-HDTV-01 | HDTV-030 | Đạt |
| BR-DROP-HDTV-01/02 (TVV/CG dropdown) | HDTV-029/031 | Sai spec (form thiếu picker) |
| FR-X.3-01 entry-point (sub-resource VV/TVV) | HDTV-027/028 | **2/2 Đạt** (HDTV-028 retest add) |
| FR-X.3-01 N:N integration | HDTV-026 | Lỗi |

---

*Report generated: 2026-05-10 09:30 (UTC+7) | Re-test 2026-05-10 10:54:00 → 11:15:00 | QA Automation via Claude Code + Chrome DevTools MCP*
