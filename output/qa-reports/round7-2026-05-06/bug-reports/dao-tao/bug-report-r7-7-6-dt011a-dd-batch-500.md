# Bug Report — R7.7.6 DT-011a DD POST batch-update 500 + FE schema mismatch

> **Module:** Đào tạo / Khóa học / Tab "Điểm danh" (FR-III-21 BR-DD-01 + DT-011a "Điểm danh không lich_hoc")
> **Discovered:** 2026-05-12 R12.4
> **Reporter:** QA Automation Claude Code MCP

## Bug Summary

| ID | Severity | Title | Status |
|---|:-:|---|:-:|
| BUG-DT-011a-BE-DD-500-01 | Major | POST `/khoa-hocs/{id}/diem-danhs/batch-update` trả 500 ERR-SYS-00-00-01 với mọi payload có valid HV (cả schema cũ `coMat` lẫn schema mới `trangThai`) | Open |
| BUG-DT-011a-FE-SCHEMA-LEGACY-01 | Medium | FE form Điểm danh chỉ render checkbox `coMat: boolean` — gửi schema cũ thay vì enum 3 trị `trangThai: CO_MAT/VANG_PHEP/VANG_KHONG_PHEP` per spec FR-III-21 BR-DD-01 | Open |

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
