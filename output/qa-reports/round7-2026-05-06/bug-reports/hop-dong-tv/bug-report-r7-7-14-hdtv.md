# Bug Report — HĐ Tư vấn (R7.7.14 Functional)

| Thông tin | Giá trị |
|-----------|---------|
| **Dự án** | PM HTPLDN |
| **Môi trường** | http://103.172.236.130:3000/ |
| **Người test** | QA Automation (Claude Code + Chrome DevTools MCP) |
| **Ngày** | 2026-05-10 09:14:00 → 09:30:00 (lần đầu) · 2026-05-10 10:54:00 → 11:05:00 (Re-test #1) · 2026-05-10 12:13:00 → 12:18:00 (Re-test #2) · 2026-05-10 21:34:00 → 21:50:00 (Re-test #3 với bộ acc _07 sau dev claim fix lần 2) |
| **Loại test** | Functional |
| **Round** | R7 (post dev fix BUG-HDTV-001/002/003 seed) |
| **Tài liệu tham chiếu** | [functional-test-report-r7-7-14-hdtv.md](../../functional/hop-dong-tv/functional-test-report-r7-7-14-hdtv.md) · [seed-checklist-r7-3-14-hdtv.md](../../seed/hop-dong-tv/seed-checklist-r7-3-14-hdtv.md) |

---

## Tổng hợp

Phát hiện **5** lỗi gốc R7.7.14 (lần đầu) + **1** regression mới phát hiện R3 (Re-test #3) = **6** lỗi tổng. Sau Re-test #3 lần 2: **4 Closed · 1 Partial (BE✅/UI❌) · 1 mới Open**.

### Severity breakdown

| Tổng | Critical | Major | Medium | Minor | Trivial |
|------|----------|-------|--------|-------|---------|
| 6    | 1        | 5     | 0      | 0     | 0       |

> **Re-test 2026-05-10 11:05:00:** 5/5 bug VẪN reproducing. **BUG-HDTV-021 escalate Major → Critical** sau retest phát hiện QTHT bypass cả PATCH (200) + DELETE (204) — không chỉ POST 500 như log gốc. QTHT thực tế hard-delete được HDTV-0009 mồ côi.
>
> **Re-test #2 2026-05-10 12:13:00 → 12:18:00 (bộ acc `_07`, dev claim đã fix):** ❌ **5/5 bug VẪN Open**. Account: `cb_nv_tw_07` (CB_NV_TW + CB_PD_TW) cho luồng CRUD cơ bản, `qtht_07` (QTHT perms=[]) cho permission test BUG-HDTV-021. Findings:
> - **BUG-HDTV-018** ❌ VẪN broken — POST tạo HDTV-0012 với 3 thanhToans CHUA_THANH_TOAN, PATCH whole HD với `thanhToans[].trangThaiTt='DA_THANH_TOAN'` → 200 nhưng GET sau patch `tienDoTt=0` + 3 statuses unchanged. 5 sub-resource path variants (`/thanh-toans`, `/thanh-toan-hop-dongs`, `/thanh-toan-giai-doans`, `/giai-doan-thanh-toans`) đều 404.
> - **BUG-HDTV-020** ❌ VẪN broken — 4 sub-resource path 404 + top-level `/audit-logs?entityType=HOP_DONG_TU_VAN` → 403.
> - **BUG-HDTV-021** ❌ **TỆ HƠN** — POST tạo HD thành công 201 (HDTV-0012) thay vì 500 lúc trước. Dev "fix" có thể đã đổi error path thành success path → QTHT giờ tạo được record nghiệp vụ persisted (verified GET single 200 + list 8/8 chứa record mới). PATCH 200 modify (verified ghiChu update + version 2→3). DELETE 204 hard-delete trên orphan HDTV-0012 (verified GET sau DELETE = 404). DELETE 403 trên HDTV-0011 nhưng do `ERR-HDTV-04 "Không thể xóa hợp đồng đang liên kết với vụ việc"` (BR-GUARD-HDTV-01 business rule) — KHÔNG phải permission gate.
> - **BUG-HDTV-026** ❌ VẪN broken — PATCH `vuViecIds` thêm VV mới vào HDTV-0008 (1 VV → 2 VV) → 200 nhưng response data không có field `vuViecIds`, GET sau patch `soVuViecLienKet=1` (không tăng).
> - **BUG-HDTV-029** ❌ VẪN broken — Form `/hop-dong-tv/tao-moi?vuViecId=...` render 12 field giống lần test đầu, KHÔNG có TVV/CG picker.
>
> **Re-test #3 2026-05-10 21:34:00 → 21:50:00 (bộ acc `_07`, dev claim đã fix lần 2):** ✅ **4/5 bug PASS · 1 PARTIAL · 1 regression mới**. Account: `cb_nv_tw_07` (CB_NV_TW) cho luồng CRUD, `qtht_07` (QTHT) cho permission test. POST seed HDTV-20260510-0001 (id `9054a0a9-3139-42e3-b817-e7d8a0edb4b2`) với `tuVanVienId=978354d7-...` (TVV-BTP-TW-0035 HOAT_DONG). Findings:
> - **BUG-HDTV-018** ✅ **PASS Closed** — Form Edit có 3 switch toggle "Đã thanh toán" cho từng giai đoạn. Click 2/3 switch + Cập nhật → API GET trả `tienDoTt=50` (đúng công thức 50tr/100tr × 100), `thanhToans[0,1].trangThaiTt='DA_THANH_TOAN'` + `ngayThanhToan` populated. Version bump 1→4.
> - **BUG-HDTV-020** ⚠️ **PARTIAL** — API endpoint `GET /api/v1/hop-dong-tu-vans/{id}/audit-logs` giờ **200 OK** với 5 events đầy đủ schema (entityType, hanhDong, nguoiThucHienId, thoiGian, endpoint, responseCode). UI HD detail VẪN KHÔNG có tab "Nhật ký" → tester chỉ access được audit log qua API, không qua UI. **Downgrade Major → Medium** (BE đầy đủ, UI tab thiếu).
> - **BUG-HDTV-021** ✅ **PASS Closed** — qtht_07 GET 200 (đúng quyền R), POST→**403 ERR-PERM-SYS-00-01** "Forbidden", PATCH→**403** "Forbidden", DELETE→**403** "Forbidden". Permission middleware giờ block QTHT đúng spec BR-AUTH-HDTV-01.
> - **BUG-HDTV-026** ✅ **PASS Closed** — PATCH HDTV-0001 với `{version, tuVanVienId, vuViecIds: [vvId]}` → 200, GET sau patch `soVuViecLienKet=0→1` persist. Version bump 4→5. (4 sub-resource path POST vẫn 404 — chấp nhận vì PATCH whole record là main path đã work).
> - **BUG-HDTV-029** ✅ **PASS Closed** — Form Tạo HD `/hop-dong-tv/tao-moi` + Form Edit modal đều có **Radio "Loại chủ thể thực hiện"** (Cá nhân TVV/CG vs Tổ chức TCTV) + **Combobox required "Tư vấn viên / Chuyên gia"** với placeholder "Chọn tư vấn viên hoặc chuyên gia". CHECK constraint enforced: POST không có `tuVanVienId`/`toChucTuVanId` → 400 ERR-HDTV-CHU-THE-01.
> - **BUG-HDTV-030** ❌ **NEW Open Major (regression Re-test #3)** — FE Form Tạo HD truyền `GET /api/v1/tu-van-viens?trangThai=HOAT_DONG&pageSize=200` → BE cap `pageSize ≤ 100` → 422 ERR-VAL-SYS-00-01 "pageSize must not be greater than 100". Cùng pattern cho `/to-chuc-tu-vans?pageSize=200`. Dropdown TVV/CG empty trong UI → user UI thuần KHÔNG chọn được TVV → submit fail. Workaround: API direct.

## Bug Summary Table

| Bug ID | Severity | Priority | Type | TC Ref | **SRS Reference** | Title | Status |
|--------|----------|----------|------|--------|-------------------|-------|--------|
| BUG-HDTV-020 | Medium ⬇️ | P2 | UI/UX | HDTV-020 | `FR-X.3-01 §2 BR-AUD-HDTV-01` | HD detail thiếu tab "Nhật ký" trên UI (BE audit-logs API ✅ fix R3) | Open (UI partial) |
| BUG-HDTV-030 | Major | P1 | UI/Data | HDTV-029 (regression) | `BR-VAL-SYS-pagination` | FE Form Tạo HD truyền `pageSize=200` vượt BE max 100 → 422, dropdown TVV/CG empty trên UI | Open (new R3) |
| ~~BUG-HDTV-018~~ | ~~Major~~ | P1 | UI/UX + Data | HDTV-018 | `FR-X.3-01 §2 BR-VAL-HDTV-04` | ~~Form Edit thiếu toggle "Đã thanh toán" + PATCH HD silently drop nested thanhToans → không update được tiến độ TT~~ | Closed ✅ R3 |
| ~~BUG-HDTV-021~~ | ~~Critical~~ | P0 | Permission | HDTV-021 | `FR-X.3-01 §2 BR-AUTH-HDTV-01` | ~~QTHT bypass cả POST/PATCH/DELETE: POST→201, PATCH→200, DELETE→204. Vi phạm phân quyền nghiêm trọng.~~ | Closed ✅ R3 |
| ~~BUG-HDTV-026~~ | ~~Major~~ | P0 | Data | HDTV-026, HDTV-019 | `FR-X.3-01 §2 N:N relation HD↔VV` | ~~PATCH `vuViecIds` trả 200 nhưng không persist~~ | Closed ✅ R3 |
| ~~BUG-HDTV-029~~ | ~~Major~~ | P1 | UI/UX | HDTV-029, HDTV-031 | `FR-X.3-01 §2 BR-DROP-HDTV-01/02 + entity §3.4.3.13 CHECK constraint` | ~~Form Tạo/Sửa HD thiếu dropdown TVV và CG~~ | Closed ✅ R3 |

---

## ~~BUG-HDTV-018~~ [CLOSED] — Form Edit HD thiếu toggle "Đã thanh toán" + BE silently drop thanhToans patch → không test được tiến độ TT 50%

> **Re-test 2026-05-10 11:00:00:** ❌ VẪN reproducing. PATCH HDTV-0009 với `thanhToans[].trangThaiTt='DA_THANH_TOAN'` trả 200 nhưng GET sau patch `tienDoTt=0` + 3 statuses vẫn `CHUA_THANH_TOAN`. Status: **Open**.
>
> **Re-test #3 2026-05-10 21:38:00 — ✅ PASS Closed-verified.** Form Edit modal có 3 switch toggle "Đã thanh toán" cho 3 giai đoạn (uid 121_57/69/81 a11y `switch question-circle`). Click switch giai đoạn 1+2 → fill ngày dự kiến → Cập nhật → toast success → detail render Đợt 1+2 = "Đã thanh toán" với ngày 09/06+09/07. API GET trả `tienDoTt=50` (đúng công thức 50tr/100tr × 100), `thanhToans[0,1].trangThaiTt='DA_THANH_TOAN'` + ngayThanhToan populated. Version 1→4. Account `cb_nv_tw_07`. HDTV-20260510-0001 (id `9054a0a9-...`).
>
> Evidence: ![Form Edit có 3 switch toggle](image/r7-3-018-form-edit-with-switch-r3.png) ![Detail render tienDoTt 50%](image/r7-3-018-detail-tiendott-50-r3.png)

### Mô tả

CB Nghiệp vụ TW (`cb_nv_tw_01`) tạo HDTV-20260510-0009 với 3 thanhToans (30tr+20tr+50tr / 100tr giá trị). Cần mark 2 đợt đầu thành DA_THANH_TOAN để verify công thức `tienDoTt = 50%` per BR-VAL-HDTV-04. Form Edit modal render 4 field per giai đoạn (Tên/Số tiền/Ngày dự kiến/Ghi chú) — KHÔNG có toggle/checkbox `trangThaiTt`. Thử PATCH API trực tiếp với `thanhToans[].trangThaiTt='DA_THANH_TOAN'` BE trả 200 nhưng GET sau patch vẫn `CHUA_THANH_TOAN × 3`. Sub-resource endpoint `/thanh-toans/:id` trả 404.

### Các bước tái hiện

1. Login `cb_nv_tw_01` (CB_PD_TW + CB_NV_TW), OTP `666666`.
2. POST `/api/v1/hop-dong-tu-vans` body `{tenHopDong, benA, benB, giaTriHopDong:100000000, ngayBatDau:'2026-05-10', ngayKetThuc:'2026-08-10', thanhToans:[{giaiDoan:'Đợt 1', soTien:30000000, thuTu:1},{giaiDoan:'Đợt 2', soTien:20000000, thuTu:2},{giaiDoan:'Đợt 3', soTien:50000000, thuTu:3}]}` → 201 với id HD `a6006815-...`.
3. Navigate UI `/hop-dong-tv/a6006815-468c-4fcf-ace2-a4725db62ae8` → click button "Chỉnh sửa".
4. Modal mở: scroll xuống section "Thanh toán giai đoạn" — quan sát chỉ có Tên/Số tiền/Ngày/Ghi chú, không có toggle "Đã thanh toán".
5. Đóng modal. Thử PATCH `/api/v1/hop-dong-tu-vans/{id}` body `{version, thanhToans: [{...trangThaiTt:'DA_THANH_TOAN', ngayThanhToan:'2026-05-10'}, ...]}` → 200.
6. GET `/api/v1/hop-dong-tu-vans/{id}` → `tienDoTt=0`, `thanhToans[].trangThaiTt = CHUA_THANH_TOAN × 3` (không thay đổi).
7. PATCH `/api/v1/hop-dong-tu-vans/{id}/thanh-toans/{ttId}` → 404. PATCH `/api/v1/thanh-toan-hop-dongs/{ttId}` → 404. PATCH `/api/v1/thanh-toans/{ttId}` → 404.

### Kết quả mong đợi

- Per **FR-X.3-01 §2 BR-VAL-HDTV-04**: hệ thống phải auto-tính `tienDoTt = SUM(thanhToans WHERE trangThaiTt=DA_THANH_TOAN) / giaTriHopDong * 100`.
- UI Form Edit phải có cơ chế (toggle/checkbox/dropdown) để mark từng giai đoạn thanh toán → DA_THANH_TOAN + nhập ngayThanhToan.
- Hoặc API có sub-resource `/hop-dong-tu-vans/{id}/thanh-toans/{ttId}` PATCH với body `{trangThaiTt, ngayThanhToan}`.
- Sau khi 2 đợt đầu mark paid (50tr / 100tr) → GET HD trả `tienDoTt=50`.

### Kết quả thực tế

- Form Edit chỉ render 4 field per giai đoạn, không có UI để update trạng thái.
- PATCH HD whole record với `thanhToans[]` mới: BE trả 200 OK nhưng silently drop array → record không thay đổi.
- 3 path API sub-resource cho thanhToans đều 404.
- Tester KHÔNG có cách nào set HD đến `tienDoTt > 0` để verify công thức.

### Bằng chứng

![BUG-HDTV-018 — HD detail render 3 thanhToans tất cả "Chưa thanh toán" + form Edit không có toggle](r7-7-14-hdtv-018-detail-no-paid-toggle.jpeg)

API response sample:

```json
{
  "data": {
    "tienDoTt": 0,
    "thanhToans": [
      {"thuTu":1, "soTien":30000000, "trangThaiTt":"CHUA_THANH_TOAN", "ngayThanhToan":null},
      {"thuTu":2, "soTien":20000000, "trangThaiTt":"CHUA_THANH_TOAN", "ngayThanhToan":null},
      {"thuTu":3, "soTien":50000000, "trangThaiTt":"CHUA_THANH_TOAN", "ngayThanhToan":null}
    ]
  }
}
```

PATCH attempt response:

```json
{ "patchStatus": 200, "afterStatuses": ["CHUA_THANH_TOAN","CHUA_THANH_TOAN","CHUA_THANH_TOAN"] }
```

---

## BUG-HDTV-020 — HD detail thiếu tab "Nhật ký" + endpoint audit log không tồn tại (BR-AUD-HDTV-01)

> **Re-test 2026-05-10 11:01:00:** ❌ VẪN reproducing. 4 sub-resource path (`/audit-logs`, `/nhat-ky`, `/lich-su`, `/history`) đều trả 404; top-level `/audit-logs?entityType=HOP_DONG_TU_VAN` trả 403. Status: **Open**.
>
> **Re-test #3 2026-05-10 21:42:00 — ⚠️ PARTIAL (BE✅/UI❌).** API endpoint `GET /api/v1/hop-dong-tu-vans/{id}/audit-logs` giờ **200 OK** với 5 events đầy đủ schema (`entityType, entityId, hanhDong, nguoiThucHienId, systemActor, thoiGian, ipAddress, endpoint, responseCode, sessionId`). Action types: CREATE × 2, UPDATE × 3 — match thực tế CRUD seed + 2 PATCH. UI HD detail page snapshot VẪN KHÔNG có tab/section "Nhật ký" — tester chỉ access được audit log qua API call thủ công. **Downgrade Major → Medium** (BE đã đầy đủ, chỉ UI tab thiếu). Status: **Open (UI partial)**.

### Mô tả

CB Nghiệp vụ TW navigate `/hop-dong-tv/{id}` quan sát detail page chỉ render: Header, Thông tin hợp đồng, Mốc tiến độ, Thanh toán giai đoạn, button Chỉnh sửa/Xóa. KHÔNG có tab "Nhật ký" / "Lịch sử" / "Audit log" để xem audit trail CRUD per BR-AUD-HDTV-01. Probe API: 4 sub-resource path đều 404; top-level `/audit-logs?entityType=HOP_DONG_TU_VAN` 403 cho `cb_nv_tw_01` (role có 235 perm).

### Các bước tái hiện

1. Login `cb_nv_tw_01` (235 permissions).
2. Navigate `/hop-dong-tv/a6006815-468c-4fcf-ace2-a4725db62ae8`.
3. Quan sát layout: section heading "Tiến độ thanh toán", "Thông tin hợp đồng", "Mốc tiến độ", "Thanh toán giai đoạn" — không có tab "Nhật ký".
4. Probe sub-resource API:
   - GET `/api/v1/hop-dong-tu-vans/{id}/audit-logs` → 404
   - GET `/api/v1/hop-dong-tu-vans/{id}/nhat-ky` → 404
   - GET `/api/v1/hop-dong-tu-vans/{id}/lich-su` → 404
   - GET `/api/v1/hop-dong-tu-vans/{id}/history` → 404
5. Probe top-level:
   - GET `/api/v1/audit-logs?entityType=HOP_DONG_TU_VAN&entityId={id}` → 403
   - GET `/api/v1/audit-logs?resource=hop-dong-tu-van&id={id}` → 403

### Kết quả mong đợi

- Per **FR-X.3-01 §2 BR-AUD-HDTV-01**: Mọi CRUD trên HD phải log audit trail (CREATE/UPDATE/DELETE/STATUS_CHANGE), kèm `actorId`, `timestamp`, `before/after snapshot` (hoặc tối thiểu event log).
- UI HD detail có tab "Nhật ký" hiển thị audit trail từ mới nhất → cũ.
- Hoặc UI riêng `/audit-logs?entityType=HOP_DONG_TU_VAN` cho QTHT.
- API `/hop-dong-tu-vans/{id}/audit-logs` trả 200 + array events cho CB có permission.

### Kết quả thực tế

- UI: KHÔNG có tab "Nhật ký" trong HD detail page.
- API: 4 path sub-resource 404 (endpoint chưa được implement).
- API top-level 403 (endpoint có thể tồn tại nhưng không expose cho `cb_nv_tw_01` — không clear).
- Tester KHÔNG có cách nào kiểm tra audit log của HD.

### Bằng chứng

![BUG-HDTV-020 — HD detail full page, không có tab "Nhật ký"](r7-7-14-hdtv-018-detail-no-paid-toggle.jpeg)

*(Cùng screenshot với BUG-HDTV-018 — vì cả 2 issue đều ở trên cùng detail page)*

API probe response:

```json
{
  "/hop-dong-tu-vans/{id}/audit-logs": 404,
  "/hop-dong-tu-vans/{id}/nhat-ky":   404,
  "/hop-dong-tu-vans/{id}/lich-su":   404,
  "/hop-dong-tu-vans/{id}/history":   404,
  "/audit-logs?entityType=HOP_DONG_TU_VAN": 403
}
```

---

## ~~BUG-HDTV-021~~ [CLOSED] — QTHT bypass cả CUD trên HD TV: POST→500, PATCH→200 (modify), DELETE→204 (hard-delete)

> **Re-test 2026-05-10 11:03:00:** ❌ VẪN reproducing + PHÁT HIỆN MỚI nghiêm trọng hơn:
> - POST `/hop-dong-tu-vans` → vẫn 500 ERR-SYS-00-00-01
> - PATCH `/hop-dong-tu-vans/{id}` body `{version, ghiChu:'qtht-retest'}` → **200 OK** (QTHT modify thành công, không 403!)
> - DELETE `/hop-dong-tu-vans/{HDTV-0009-mồ-côi}` → **204 No Content** (hard-deleted thật sự!) → GET sau DELETE trả 404
>
> **Severity escalate Major → Critical** vì QTHT (vai trò Quản trị hệ thống — không có permission CUD trên HD TV per BR-AUTH-HDTV-01) thực tế thao tác CUD đầy đủ trên DB nghiệp vụ. Status: **Open**.
>
> **Re-test #3 2026-05-10 21:44:00 — ✅ PASS Closed-verified.** Login `qtht_07` (vai trò QTHT) trong isolated context `qa_r3_hdtv_qtht_07`. Probe 4 endpoint:
> - GET `/api/v1/hop-dong-tu-vans?pageSize=2` → 200 (đúng quyền R)
> - POST `/api/v1/hop-dong-tu-vans` body `{tenHopDong, benA, benB, giaTriHopDong, ngayBatDau, ngayKetThuc, tuVanVienId}` → **403 ERR-PERM-SYS-00-01 "Forbidden"**
> - PATCH `/api/v1/hop-dong-tu-vans/{id}` body `{version, ghiChu}` → **403 ERR-PERM-SYS-00-01 "Forbidden"**
> - DELETE `/api/v1/hop-dong-tu-vans/{id}` → **403 ERR-PERM-SYS-00-01 "Forbidden"**
>
> Permission middleware giờ block QTHT đúng spec BR-AUTH-HDTV-01 (R-only). Không còn bypass. Severity downgrade Critical → Closed.

### Mô tả

QTHT (`qtht_01`) per BR-AUTH-HDTV-01 chỉ có permission R (read) trên HD TV. Test phân quyền: GET `/api/v1/hop-dong-tu-vans` trả 200 (đúng); POST tạo HD trả **500 ERR-SYS-00-00-01 "Lỗi hệ thống, vui lòng thử lại sau"** thay vì 403; DELETE `/api/v1/hop-dong-tu-vans/{id}` trả **404 ERR-VAL-X3-159-02 "Hợp đồng tư vấn không tồn tại"** (business error, leak existence info) thay vì 403 perm error.

### Các bước tái hiện

1. Login `qtht_01` (Quản trị hệ thống) trong isolated context (Chrome DevTools MCP `isolatedContext=qtht_role`).
2. GET `/api/v1/hop-dong-tu-vans?pageSize=5` → 200 OK (đúng — quyền R).
3. POST `/api/v1/hop-dong-tu-vans` body `{tenHopDong:'qtht-test', benA:'a', benB:'b', giaTriHopDong:1000, ngayBatDau:'2026-05-10', ngayKetThuc:'2026-05-15'}` → 500 ERR-SYS-00-00-01 (sai).
4. DELETE `/api/v1/hop-dong-tu-vans/{validHdId}` (HD thật, đã verify GET thấy) → 404 ERR-VAL-X3-159-02 (sai — phải 403).

### Kết quả mong đợi

- Per **FR-X.3-01 §2 BR-AUTH-HDTV-01**: QTHT chỉ có permission R. CUD attempts phải trả `403 ERR-AUTH-PERM-01` consistent.
- POST 403 trước khi vào handler (permission middleware).
- DELETE 403 trước khi check existence (permission middleware).

### Kết quả thực tế

- POST trả `500 ERR-SYS-00-00-01` — có thể là CHECK constraint violation (`tu_van_vien_id IS NOT NULL OR to_chuc_tu_van_id IS NOT NULL`) bypass permission check vào tận BE.
- DELETE trả `404 ERR-VAL-X3-159-02 "Hợp đồng tư vấn không tồn tại"` — leak info HD tồn tại hay không (security concern); permission check không chạy trước existence check.
- Tham chiếu memory `qa_htpldn_qtht_permission_bypass` — pattern đã thấy trên TU_VAN_VIEN R14 W1, có vẻ lặp ở entity HD TV.

### Bằng chứng

API response:

```json
{
  "POST /hop-dong-tu-vans (qtht_01)": {
    "status": 500,
    "body": {"success":false,"error":{"code":"ERR-SYS-00-00-01","message":"Lỗi hệ thống, vui lòng thử lại sau","timestamp":"2026-05-10T02:27:32.600Z","requestId":"479ac42c-..."}}
  },
  "DELETE /hop-dong-tu-vans/{id} (qtht_01)": {
    "status": 404,
    "body": {"success":false,"error":{"code":"ERR-VAL-X3-159-02","message":"Hợp đồng tư vấn không tồn tại","timestamp":"2026-05-10T02:27:32.625Z","requestId":"d40f5ff6-..."}}
  }
}
```

### So sánh

| Role | GET list | POST create | DELETE |
|------|----------|-------------|--------|
| `cb_nv_tw_01` (CB_NV_TW) | ✅ 200 | ✅ 201 | ✅ 204 hoặc 403 ERR-HDTV-04 (nếu có VV link) |
| `qtht_01` (QTHT) | ✅ 200 (R quyền) | ❌ 500 (BUG! phải 403) | ❌ 404 leak (BUG! phải 403) |
| `nht_01` (NHT) | ❌ 403 | ❌ 403 (chưa test cụ thể) | ❌ 403 (chưa test) |
| `9999999990` (DN) | ❌ 403 | ❌ 403 (chưa test) | ❌ 403 (chưa test) |

---

## ~~BUG-HDTV-026~~ [CLOSED] — N:N linking VV vào HD broken: PATCH `vuViecIds` không persist + 4 sub-resource POST 404

> **Re-test #3 2026-05-10 21:46:00 — ✅ PASS Closed-verified.** PATCH HDTV-0001 (`9054a0a9-...`) body `{version: 4, tuVanVienId: "978354d7-...", vuViecIds: ["dce4c308-..." VV-BTP-TW-20260510-002]}` → 200, version bump 4→5. GET sau patch `soVuViecLienKet=0→1` (persist OK). 4 sub-resource POST path (`/vu-viecs`, `/vu-viec-links`, `/lien-ket-vu-viec`, `/links`) vẫn 404 ERR-SYS-00-04-01 — chấp nhận vì PATCH whole record là main path đã work, sub-resource là alternate optional.

### Mô tả

CB Nghiệp vụ TW tạo HD mồ côi (HDTV-20260510-0010, không link VV). Cần add VV-BTP-TW-20260509-009 (Lao động) vào HD qua API để verify N:N relation per spec FR-X.3-01 §2. PATCH `/api/v1/hop-dong-tu-vans/{id}` body `{version, vuViecIds:[vvId]}` trả 200 OK nhưng GET sau patch `soVuViecLienKet` vẫn `0`. Thử 4 path sub-resource POST đều 404 (`/vu-viecs`, `/vu-viec-links`, `/lien-ket-vu-viec`, `/links`).

### Các bước tái hiện

1. Login `cb_nv_tw_01`.
2. POST tạo HDTV-0010 mồ côi (no `vuViecIds` trong body) → 201, `soVuViecLienKet=0`.
3. GET `/api/v1/vu-viecs?pageSize=30` → tìm VV-BTP-TW-20260509-009 (Lao động) id `765920aa-43e4-...`.
4. GET `/api/v1/hop-dong-tu-vans/{hdId}` → lấy `version` field.
5. PATCH `/api/v1/hop-dong-tu-vans/{hdId}` body `{version, vuViecIds:[vvId]}` → 200 OK.
6. GET `/api/v1/hop-dong-tu-vans/{hdId}` lại → `soVuViecLienKet=0` (KHÔNG đổi).
7. POST `/api/v1/hop-dong-tu-vans/{hdId}/vu-viecs` body `{vuViecId}` → 404.
8. POST `/api/v1/hop-dong-tu-vans/{hdId}/vu-viec-links` → 404.
9. POST `/api/v1/hop-dong-tu-vans/{hdId}/lien-ket-vu-viec` → 404.
10. POST `/api/v1/hop-dong-tu-vans/{hdId}/links` → 404.

### Kết quả mong đợi

- Per **FR-X.3-01 §2** N:N relation: HD và VV có quan hệ N:N (1 HD link nhiều VV; 1 VV có thể link nhiều HD).
- POST tạo HD với `vuViecIds: [vvId, vvId2]` đã work trong seed (HDTV-0003..0008 cover 6 LV với `soVvLink=1`).
- PATCH HD đã tồn tại với `vuViecIds: [vvId]` phải persist + tăng `soVuViecLienKet`.
- Hoặc có sub-resource endpoint `POST /hop-dong-tu-vans/{id}/vu-viecs` body `{vuViecId}` để add từng link.

### Kết quả thực tế

- PATCH với `vuViecIds` trong body: BE trả 200 nhưng silently drop array — không có error message, không có state change.
- 4 path sub-resource POST đều 404 → endpoint chưa implement.
- Tester chỉ có thể link VV vào HD tại thời điểm POST tạo HD; sau đó không có cách nào add/remove VV link.

### Bằng chứng

API response:

```json
{
  "PATCH /hop-dong-tu-vans/{id}": {
    "request_body": { "version": 1, "vuViecIds": ["765920aa-43e4-47c0-a8ce-bf6e9c24e53e"] },
    "response_status": 200,
    "after_get_soVuViecLienKet": 0
  },
  "POST /hop-dong-tu-vans/{id}/vu-viecs":          404,
  "POST /hop-dong-tu-vans/{id}/vu-viec-links":     404,
  "POST /hop-dong-tu-vans/{id}/lien-ket-vu-viec":  404,
  "POST /hop-dong-tu-vans/{id}/links":             404
}
```

---

## ~~BUG-HDTV-029~~ [CLOSED] — Form Tạo/Sửa HD thiếu dropdown TVV (`tu_van_vien_id`) + CG (`to_chuc_tu_van_id`) — vi phạm CHECK constraint entity §3.4.3.13

> **Re-test #3 2026-05-10 21:48:00 — ✅ PASS Closed-verified.** Form Tạo HD `/hop-dong-tv/tao-moi` + Form Edit modal đều đã có:
> - **Radio "Loại chủ thể thực hiện"** (segmented control): "Cá nhân (TVV/CG)" (mặc định checked) vs "Tổ chức (TCTV)"
> - **Combobox required "Tư vấn viên / Chuyên gia"** với placeholder "Chọn tư vấn viên hoặc chuyên gia" — uid 126_65 trong form Tạo
> - CHECK constraint enforced ở BE: POST không kèm `tuVanVienId`/`toChucTuVanId` → 400 **ERR-HDTV-CHU-THE-01 "Hợp đồng phải gán Tư vấn viên hoặc Tổ chức tư vấn"**
>
> Bug gốc về thiếu dropdown đã fix. **Phát hiện regression mới: dropdown options KHÔNG load** do FE call `pageSize=200` vượt BE max 100 → log riêng tại BUG-HDTV-030.

### Mô tả

Form modal "Tạo hợp đồng tư vấn" (mở từ VV detail accordion "HĐ tư vấn liên kết" → button "Tạo hợp đồng") render 12 field: Tên/Vụ việc liên kết (auto-fill disabled)/Số HD/Bên A/Bên B/Giá trị/Trạng thái/Thời gian/Ngày ký/Mốc tiến độ/Thanh toán/Hủy-Tạo. KHÔNG có dropdown picker cho TVV (`tu_van_vien_id`) hoặc CG (`to_chuc_tu_van_id`). Form Sửa cũng tương tự. Spec entity HOP_DONG_TU_VAN §3.4.3.13 có column `tu_van_vien_id` UUID NULL (verified GET API trả `tuVanVienId` trong allKeys); CHECK constraint yêu cầu `tu_van_vien_id IS NOT NULL OR to_chuc_tu_van_id IS NOT NULL` để HD có entity tư vấn cụ thể.

### Các bước tái hiện

1. Login `cb_nv_tw_01`.
2. Navigate `/vu-viec/{vvId}` (VV detail của VV-BTP-TW-20260509-001 Lao động).
3. Cuộn xuống section "HĐ tư vấn liên kết" → click button "Tạo hợp đồng" → modal mở.
4. Quan sát 12 field trong form: không có select/combobox cho "Tư vấn viên" hoặc "Tổ chức tư vấn".
5. Đóng modal. Mở 1 HD đã tồn tại (vd HDTV-0009) → click "Chỉnh sửa" → modal Cập nhật cùng layout, cũng không có dropdown TVV/CG.
6. Verify entity field qua API: GET `/api/v1/hop-dong-tu-vans/{id}` → response có key `tuVanVienId` (giá trị `null` cho mọi HD seed via API direct vì BE chưa enforce CHECK constraint).

### Kết quả mong đợi

- Per **FR-X.3-01 §2 + entity §3.4.3.13 CHECK**: Form Tạo/Sửa HD phải có dropdown picker cho phép chọn 1 trong 2:
  - **TVV picker** (filter `loaiTvv=TU_VAN_VIEN, trangThai=HOAT_DONG`) — per BR-DROP-HDTV-01.
  - **CG picker** (filter `loaiTvv=CHUYEN_GIA, trangThai=HOAT_DONG`) — per BR-DROP-HDTV-02. *(Spec gốc dùng chung field `loaiTvv` cho TU_VAN_VIEN/CHUYEN_GIA hoặc 2 entity riêng — cần BA confirm)*.
  - Hoặc **TCTV picker** (`to_chuc_tu_van_id`) — chọn tổ chức tư vấn pháp luật.
- Submit không thoả CHECK → form hiển thị error inline.

### Kết quả thực tế

- Form chỉ có "Bên B" textbox tự do — user nhập chuỗi text bất kỳ ("DN test", "Test BR-VAL-HDTV-04 progress" v.v.) làm `benB` field, không liên kết entity.
- BE accept POST với `tuVanVienId=null + toChucTuVanId=null` (CHECK constraint không enforce hoặc field optional contrary spec).
- Cascade impact: HDTV-029/031 (test dropdown filter HOAT_DONG) không thực hiện được vì không có dropdown để filter.

### Bằng chứng

![BUG-HDTV-029 — Form Tạo HD modal post-fix, có Vụ việc liên kết auto-fill nhưng KHÔNG có TVV/CG picker](image/r7-3-14-create-form-postfix-vv-field.jpeg)

API response sample (GET HD chỉ ra schema có `tuVanVienId` key):

```json
{
  "data": {
    "id": "...",
    "maHopDong": "HDTV-20260510-0008",
    "tuVanVienId": null,
    "benA": "Bộ Tư pháp - Cục Bổ trợ tư pháp",
    "benB": "Công ty Cổ phần Phúc An AG",
    "..."
  }
}
```

---

## BUG-HDTV-030 — FE Form Tạo HD truyền `pageSize=200` vượt BE max 100 → dropdown TVV/CG empty trên UI

### Mô tả

CB Nghiệp vụ TW (`cb_nv_tw_07`) navigate `/hop-dong-tv/tao-moi`. Modal "Tạo hợp đồng tư vấn" mở. Click combobox "Tư vấn viên / Chuyên gia" → dropdown ant-select-dropdown render class `ant-select-dropdown-empty`, 0 option. Inspect Network: FE thực hiện 2 GET liền tiếp `/api/v1/tu-van-viens?trangThai=HOAT_DONG&pageSize=200` và `/api/v1/to-chuc-tu-vans?trangThai=HOAT_DONG&pageSize=200` — cả 2 đều **422 ERR-VAL-SYS-00-01** "pageSize must not be greater than 100". Do response 422, FE không có data populate dropdown → user UI thuần KHÔNG chọn được TVV/CG → form submit fail.

### Các bước tái hiện

1. Login `cb_nv_tw_07` (CB_NV_TW), OTP `666666`.
2. Navigate `/hop-dong-tv/tao-moi`.
3. Modal "Tạo hợp đồng tư vấn" mở; "Loại chủ thể" mặc định "Cá nhân (TVV/CG)".
4. Click combobox "Tư vấn viên / Chuyên gia".
5. Quan sát dropdown render empty (`.ant-select-dropdown-empty`).
6. Mở DevTools Network: 2 request fail `pageSize=200 → 422`.
7. Đổi radio sang "Tổ chức (TCTV)" → kết quả tương tự `/to-chuc-tu-vans?pageSize=200 → 422`.

### Kết quả mong đợi

- Per **BR-VAL-SYS-pagination** (BE convention chung): mọi pagination request `pageSize ≤ 100`.
- FE phải truyền `pageSize ≤ 100` (hoặc dùng pagination + lazy load) để fetch danh sách TVV/CG.
- Dropdown render đầy đủ option active để user chọn.

### Kết quả thực tế

- FE hard-code `pageSize=200` trong fetch dropdown TVV/CG → BE return 422.
- Dropdown empty → user không submit được form qua UI thuần.
- API direct POST `/hop-dong-tu-vans` với `tuVanVienId` lấy từ list khác vẫn work, nhưng đó không phải user flow.

### Bằng chứng

![BUG-HDTV-030 — Form Tạo HD dropdown TVV empty do pageSize=200 → 422](image/r7-3-029-create-form-pagesize422-r3.png)

Network response (reqid 600):

```json
{
  "url": "/api/v1/tu-van-viens?trangThai=HOAT_DONG&pageSize=200",
  "status": 422,
  "body": {
    "success": false,
    "error": {
      "code": "ERR-VAL-SYS-00-01",
      "field": "pageSize",
      "message": "pageSize must not be greater than 100",
      "details": [{"field":"pageSize","message":"pageSize must not be greater than 100"}],
      "timestamp": "2026-05-10T14:43:54.579Z",
      "requestId": "5145b62c-..."
    }
  }
}
```

---

## Phụ lục — Môi trường test

| Thành phần | Giá trị |
|------------|---------|
| URL ứng dụng | http://103.172.236.130:3000/ |
| OTP login | `666666` (bypass tạm) |
| MailHog (OTP inbox) | http://103.172.236.130:8025 |
| API base | `/api/v1/` |
| Frontend | React + Vite + Ant Design + CASL |
| Backend | NestJS + PostgreSQL + class-validator |
| Xác thực | JWT + OTP email; session timeout aggressive ~3-5 phút |
| Tool test | Chrome DevTools MCP (`mcp__chrome-devtools__*`) với 6 isolated context |

---

*Bug report generated: 2026-05-10 09:30:00 | QA Automation via Claude Code + Chrome DevTools MCP*
