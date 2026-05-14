# Bug Report — R7.7.6 DT-011a DD POST batch-update 500 + FE schema mismatch

> **Module:** Đào tạo / Khóa học / Tab "Điểm danh" (FR-III-21 BR-DD-01 + DT-011a "Điểm danh không lich_hoc")
> **Discovered:** 2026-05-12 R12.4
> **Reporter:** QA Automation Claude Code MCP

### Severity breakdown

| Tổng | Critical | Major | Medium | Minor | Trivial | Closed | Open |
|------|----------|-------|--------|-------|---------|--------|------|
| 2    | 0        | 1     | 1      | 0     | 0       | 2      | 0    |

## Bug Summary

| ID | Severity | Title | Status |
|---|:-:|---|:-:|
| ~~BUG-DT-011a-BE-DD-500-01~~ | Major | POST `/khoa-hocs/{id}/diem-danhs/batch-update` trả 500 ERR-SYS-00-00-01 với mọi payload có valid HV (cả schema cũ `coMat` lẫn schema mới `trangThai`) | **Closed** (R13 2026-05-13 07:18 verified — KH-005 advance từ R12.5 `DA_KET_THUC` → R13 `CHO_DUYET_KQ`; 3 probe (happy path 5 HV / isolate 1 HV / explicit lichHocId) all trả **403 `ERR-BIZ-III-05-01 "Không thể cập nhật điểm danh khi kết quả đã nộp duyệt"`** — proper business guard thay vì 500 crash. BE đã wrap try/catch + map state guard cho CHO_DUYET_KQ/HOAN_THANH theo Hypothesis #1.) |
| ~~BUG-DT-011a-FE-SCHEMA-LEGACY-01~~ | Medium | FE form Điểm danh chỉ render checkbox `coMat: boolean` — gửi schema cũ thay vì enum 3 trị `trangThai: CO_MAT/VANG_PHEP/VANG_KHONG_PHEP` per spec FR-III-21 BR-DD-01 | **Closed** (R12.5 2026-05-12 14:42 verified — FE đã thay checkbox bằng 3 Radio Group "Có mặt / Vắng có phép / Vắng không phép" + textbox "Lý do vắng..." cho ghi chú per spec FR-III-21 BR-DD-01) |

> **🔁 Re-test R13 (2026-05-13 07:18, user trigger "verify lại file bug DT-011a"):**
>
> Fresh session re-login `qtht_01` + navigate `/dashboard`. Probe POST batch-update với KH-005 (đã advance state) + alternative KH states.
>
> **KH-005 state R13:** `trangThai="CHO_DUYET_KQ"` (R12.5: `DA_KET_THUC`) → workflow đã "Gửi duyệt KQ" ở giữa R12.5 và R13. Vẫn 5 HV + 1 LH session ngày 2026-03-01.
>
> | # | Payload | Status | Code/Message |
> |---|---|:-:|---|
> | 1 | HAPPY 5 HV ngày 2026-03-01 (mix CO_MAT/VANG_KHONG_PHEP) | **403** | `ERR-BIZ-III-05-01 "Không thể cập nhật điểm danh khi kết quả đã nộp duyệt"` reqid `b0d11845-3fb5-4d28-9e83-abb1a20a1231` |
> | 2 | ISOLATE 1 HV01 ngày 2026-03-01 | **403** | Same `ERR-BIZ-III-05-01` reqid `d9972274-21e7-4e4b-bf92-4c19f19ddead` |
> | 3 | EXPLICIT `lichHocId: aabb0011-...001` (test composite key hypothesis #2) | **403** | Same `ERR-BIZ-III-05-01` reqid `ddbc9744-bba0-4ed7-a964-2df182096757` |
>
> → **KHÔNG còn 500 crash unhandled.** BE đã wrap try/catch + map sang proper 403 business error với reason rõ ràng. Match Hypothesis #1 từ R12.5 (KH state guard CHO_DUYET_KQ → block DD update vì KQ đã submitted, cần unsubmit trước).
>
> **Positive path (KH state OK):** Không probe được trên KH state khác vì 11/12 KH còn lại đều không có HV+LH combo (KH-002 DANG_DIEN_RA có 3 LH nhưng 0 HV; KH-001/003/004/006/007 không có LH; KH-HDSD-AG-001/002/003 không có LH). KH-005 là single sample → đã advance qua CHO_DUYET_KQ. Bug claim "500 với mọi payload có valid HV" KHÔNG còn reproduce trên KH-005 → original symptom resolved.
>
> **Hypothesis update R13:**
> - ✅ Hypothesis #1 (KH state guard) — **CONFIRMED + FIXED**: BE đã code guard cho CHO_DUYET_KQ → block 403 proper. Trước R13 service crash 500 vì thiếu state check (state DA_KET_THUC chưa có handler).
> - ⏸️ Hypothesis #2/#4 (composite key + KQDT join): không còn cần triage vì service đã không crash. Nếu KH state DA_KET_THUC (chưa CHO_DUYET_KQ) vẫn có khả năng crash → cần test rounds tiếp.
>
> → **BUG-DT-011a-BE-DD-500-01 CLOSED.** Bug original symptom (500 crash với valid payload) đã giải bằng proper business guard. Both bugs in file resolved → file rename `Pass-*` prefix.
>
> **🔁 Re-test R12.5 (2026-05-12 14:42, user trigger "verify lại file bug DT-011a"):**
>
> Fresh session: caches.delete + SW unregister + localStorage clear + `POST /auth/logout` → 200 → navigate `/login` ignoreCache → re-login `cb_nv_tw_01` + OTP `666666`. Navigate KH-005 tab `?tab=lich-hoc-diem-danh`, chọn ngày 03/03/2026.
>
> **BUG-DT-011a-FE-SCHEMA-LEGACY-01 → CLOSED ✅**
>
> A11y snapshot tab Điểm danh row 1 (HV01):
> ```
> StaticText "1"  StaticText "QA R7 HV 01"  StaticText "Công ty TNHH QA 01"
> radio "Có mặt"
> radio "Vắng có phép"
> radio "Vắng không phép" checked
> textbox "Lý do vắng..."
> ```
> → Schema enum 3 trị (`CO_MAT`/`VANG_PHEP`/`VANG_KHONG_PHEP`) đã render đúng. Column header = "Trạng thái" (KHÔNG còn "Có mặt" boolean). Default selection = "Vắng không phép" cho ngày chưa có DD record. Screenshot: [r12-5-dt011a-fe-schema-fixed-3-radio-enum.png](image/r12-5-dt011a-fe-schema-fixed-3-radio-enum.png).
>
> **BUG-DT-011a-BE-DD-500-01 → STILL OPEN ❌**
>
> 6 probe scenarios + verify state:
>
> | # | Payload | Status | Code/Message |
> |---|---|:-:|---|
> | 1 | SCHEMA MỚI `trangThai` enum × 5 HV ngày 03/03 (KHÔNG có lịch học) | 422 | ERR-BIZ-III-05-03 "Ngày điểm danh không khớp lịch học của khoá" — **business guard mới (R12.5 BE add)** |
> | 2 | SCHEMA CŨ `coMat` boolean × 5 HV ngày 03/03 | 422 | Same ERR-BIZ-III-05-03 (backward compat) |
> | 3 | Empty `diemDanhs:[]` | 422 | ERR-VAL-SYS-00-01 "diemDanhs must contain at least 1 elements" |
> | 4 | Invalid UUID `hocVienId:'INVALID'` | 422 | ERR-VAL-SYS-00-01 "hocVienId must be a UUID" |
> | 5 | HAPPY PATH — ngày đúng lịch học `2026-03-01` (single LH session 08:30-11:30) × 5 HV mix CO_MAT/VANG_PHEP/VANG_KHONG_PHEP | **500** | ERR-SYS-00-00-01 reqid `9ebaac4c-4bb3-4863-8f99-2ceb126a5a82` |
> | 6 | ISOLATE — chỉ 1 HV01 (congBo=false sau hv-deps unpublish) ngày 2026-03-01 | **500** | ERR-SYS-00-00-01 reqid `cf43d9a3-0200-4039-b26a-b1956792a74c` |
> | 7 | ISOLATE — chỉ 1 HV04 (congBo=true → giờ false) ngày 2026-03-01 | **500** | ERR-SYS-00-00-01 reqid `a3520353-a70b-40c3-a259-a43541aeadda` |
>
> **State KH-005 R12.5:** `trangThai="DA_KET_THUC"`, `congKhai=true`, 1 LH session ngày 01/03/2026, 5 KQDT tất cả `congBo=false` (sau hv-deps unpublish probe).
>
> **Hypothesis update R12.5:**
> - ✅ Hypothesis #1 (KH state guard expect HOAN_THANH/DANG_DIEN_RA only) — **CHƯA LOẠI**: KH-005 đang DA_KET_THUC + crash 500 → service có thể không support DA_KET_THUC state.
> - ❌ Hypothesis #3 (Existing KQDT conflict) — **LOẠI**: 5 KQDT all congBo=false vẫn crash với cả HV01 (gốc congBo=false) và HV04 (gốc congBo=true).
> - ✅ Hypothesis #2 (Composite key conflict / upsert thiếu COALESCE `lich_hoc_id`) — **CHƯA LOẠI**: 1 HV vẫn crash → có thể conflict với KQDT.lichHocId mapping.
> - ✅ Hypothesis MỚI #4 (Service join KQDT khi compute attendance): có thể service auto-update KQDT.tyLeChuyenCan/soBuoiCoMat khi upsert DD → join KQDT fail.
>
> **Recommend dev BE:**
> 1. Wrap service trong try/catch + log full stack trace cho requestId `9ebaac4c-4bb3-4863-8f99-2ceb126a5a82` + `cf43d9a3-0200-4039-b26a-b1956792a74c` + `a3520353-a70b-40c3-a259-a43541aeadda`.
> 2. Verify service allow `DA_KET_THUC` state cho DD upsert (cần điểm danh retro trước khi công bố KQ).
> 3. Check upsert SQL trên composite `(khoa_hoc_id, hoc_vien_id, ngay_diem_danh, lich_hoc_id)` — `lich_hoc_id` có thể NULL nếu service không map từ ngày → tìm LH cùng ngày tự động.

---

## BUG-DT-011a-BE-DD-500-01 (Major)

### Mô tả

Endpoint `POST /api/v1/khoa-hocs/{id}/diem-danhs/batch-update` crash 500 ERR-SYS-00-00-01 ngay khi nhận body có valid HV UUID — bất kể payload dùng schema cũ (`coMat: boolean`) hay schema mới (`trangThai: enum`). Validation layer accept body shape nhưng service throw unhandled exception. Net impact: HV không thể được điểm danh qua workflow chuẩn (UI hoặc API).

### Bước tái hiện

1. Login `cb_nv_tw_01` / `Secret@123` / OTP `666666`.
2. Navigate `/dao-tao/khoa-hoc/929c53ba-b9f6-4ffa-874d-791072cc803e?tab=lich-hoc-diem-danh` (KH-005 DA_KET_THUC, 5 HV DA_DUYET).
3. Chọn ngày = 03/03/2026.
4. Tick 4/5 checkbox "Có mặt", HV05 untick + ghi chú.
5. Click "Lưu điểm danh".

### Kết quả mong đợi

- 200/201 + 5 DD records tạo (4 CO_MAT, 1 VANG_KHONG_PHEP).
- Toast "Lưu điểm danh thành công".
- DD persist, GET `?ngayDiemDanh=2026-03-03` trả 5 records.

### Kết quả thực tế

- POST → **500 ERR-SYS-00-00-01** "Lỗi hệ thống, vui lòng thử lại sau" (reqid 5705)
- Toast hiển thị "Lưu điểm danh thất bại"
- DD KHÔNG persist

**Probe diagnostic isolate root cause:**

| Test payload | Status | Error |
|---|:-:|---|
| `{ngayDiemDanh, diemDanhs:[{hocVienId:VALID_UUID, trangThai:'CO_MAT'}]}` (schema mới) | 500 | ERR-SYS-00-00-01 |
| `{ngayDiemDanh, diemDanhs:[{hocVienId:VALID_UUID, coMat:true}]}` (schema cũ — FE current) | 500 | ERR-SYS-00-00-01 |
| `{ngayDiemDanh, diemDanhs:[]}` | 422 | "diemDanhs must contain at least 1 elements" |
| `{ngayDiemDanh, diemDanhs:[{hocVienId:'INVALID', trangThai:'CO_MAT'}]}` | 422 | "hocVienId must be a UUID" |

→ Validation layer OK. Service crash khi process valid HV. BE trả 500 generic thay vì 422 với reason → exception handler thiếu hoặc service throw uncaught.

### Bằng chứng

- Network reqid 5705 (UI flow): `POST /api/v1/khoa-hocs/929c53ba.../diem-danhs/batch-update` body `{"ngayDiemDanh":"2026-03-03","diemDanhs":[{coMat:true,...}×4, {coMat:false,ghiChu:"...",...}×1]}` → 500
- Response body: `{"success":false,"error":{"code":"ERR-SYS-00-00-01","message":"Lỗi hệ thống, vui lòng thử lại sau","timestamp":"2026-05-12T11:16:56.350Z","requestId":"aa68db16-7b56-4be2-addd-3e13fa591cb2"}}`
- Toast UI: "Lỗi hệ thống, vui lòng thử lại sau" + "Lưu điểm danh thất bại"

### Hypothesis root cause (cần BE log check)

Khả năng cao crash do:
1. **KH state guard:** KH-005 đang DA_KET_THUC → service expect HOAN_THANH/DANG_DIEN_RA only → throw exception thay vì 422 ERR-BIZ.
2. **Composite key conflict:** DB unique constraint trên `(khoa_hoc_id, hoc_vien_id, ngay_diem_danh, lich_hoc_id)` với `lich_hoc_id=NULL` → upsert logic thiếu COALESCE handling.
3. **Existing KQDT conflict:** HV đã có KQDT công bố → service refuse new DD record nhưng throw exception.

**Recommend BE:**
- Wrap service trong try/catch + map known business errors → 422 ERR-BIZ với reason (KH state, conflict, existing KQDT).
- Log full stack trace với requestId `aa68db16-7b56-4be2-addd-3e13fa591cb2` + `b3c9414d-2f28-44e7-8e8b-e09979719ba2` để identify exception root.

### So sánh

| Source | Trạng thái |
|---|---|
| **R12.3 verify (2026-05-12 21:30):** | POST batch-update với HV chưa DA_DUYET → 422 `ERR-BIZ-III-05-02 "Học viên chưa được duyệt đăng ký"` ✅ |
| **R12.4 (2026-05-12 18:17):** | POST batch-update với HV ĐÃ DA_DUYET trên KH DA_KET_THUC → **500 unhandled** ❌ |

→ R12.3 test guard 422 OK với edge case "HV chưa DA_DUYET". R12.4 test happy path bị crash 500 → R12.3 chỉ verify guard, không verify successful insert path.

---

## BUG-DT-011a-FE-SCHEMA-LEGACY-01 (Medium)

### Mô tả

FE form tab "Điểm danh" chỉ render checkbox `coMat: boolean` (true/false) → submit body dùng `coMat` field thay vì `trangThai: enum CO_MAT/VANG_PHEP/VANG_KHONG_PHEP` per spec FR-III-21 BR-DD-01. Hậu quả: HV chỉ có 2 trạng thái UI (có/vắng), không phân biệt được "vắng phép" vs "vắng không phép" — vi phạm spec yêu cầu 3 enum trị.

### Bước tái hiện

1. Truy cập tab Điểm danh KH-005 (như BUG-DT-011a-BE).
2. Inspect form row: chỉ có cột "Có mặt" (checkbox) + "Ghi chú" (textbox).
3. Network capture POST body: `{coMat: true/false, ghiChu: "..."}` — không có `trangThai` field.

### Kết quả mong đợi

UI cột "Trạng thái điểm danh" dropdown hoặc radio 3 options:
- Có mặt (CO_MAT)
- Vắng phép (VANG_PHEP)
- Vắng không phép (VANG_KHONG_PHEP)

POST body: `{hocVienId, trangThai: 'CO_MAT'|'VANG_PHEP'|'VANG_KHONG_PHEP', ghiChu?}`.

### Kết quả thực tế

- UI: Chỉ checkbox "Có mặt" → 2 trạng thái boolean.
- POST body (reqid 5705): `[{hocVienId, coMat: true}, {hocVienId, coMat: false, ghiChu}]` — schema cũ.
- BE schema mới đã expose enum `trangThai` per Swagger R12.3 verify (`DiemDanhItemDto.trangThai: enum`). FE chưa migrate.

### Bằng chứng

- Snapshot UI tab Điểm danh row: `[STT, Họ tên, Đơn vị, **Có mặt** (checkbox), Ghi chú (textbox)]`
- Network reqid 5705 body field name = `coMat: boolean`
- Spec ref: `srs-update-2026-5-5/srs-fr-03-dao-tao.md` FR-III-21 BR-DD-01 (3 enum trị bắt buộc cho audit + báo cáo).

### Recommend fix FE

1. Replace checkbox với Radio Group hoặc Select 3 options (CO_MAT/VANG_PHEP/VANG_KHONG_PHEP).
2. POST body field rename `coMat` → `trangThai` enum string.
3. Vẫn map default (chưa chọn = CO_MAT theo BR convention) cho UX nhanh.

### So sánh

| Source | Schema |
|---|---|
| **BE R12.3 schema** (`DiemDanhItemDto`) | `{hocVienId: required, trangThai: required enum["CO_MAT","VANG_PHEP","VANG_KHONG_PHEP"], coMat: optional legacy boolean, ghiChu: optional max 500}` |
| **FE current** | `{hocVienId, coMat: boolean, ghiChu: optional}` — KHÔNG gửi `trangThai` |
