# Bug Report — Form Tạo KH FE thiếu field "Giảng viên" (R7.7.6 DT-004 R10)

> **Module:** Đào tạo / Khóa học (FR-III KHOA_HOC)
> **Discovered:** 2026-05-10 09:48 (R7.7.6 phase 2 R10)
> **Reporter:** QA Automation Claude Code MCP

## Bug Summary

| ID | Severity | Title | Status |
|---|:-:|---|:-:|
| BUG-DT-FORM-GV-01 | **Major** | Form Tạo KH (`/dao-tao/khoa-hoc/tao-moi`) thiếu field required "Giảng viên" → POST always 422 `giangVienIds must contain at least 1 elements` | Open |

---

## Mô tả
FE form Tạo KH render 8 fields. BE schema yêu cầu thêm `giangVienIds: UUID[]` với `min 1 element`. Submit form đầy đủ vẫn POST 422.

## Bước tái hiện
1. Login `cb_nv_tw_02` (CB_NV_TW)
2. Navigate `/dao-tao/khoa-hoc/tao-moi`
3. Fill form đầy đủ:
   - Tên khóa học: `R10 DT-004 KH happy path qua UI`
   - CTDT: `CTDT-BTP-TW-2026-0002 — CTĐT 2026 - ATLĐ ngành xây dựng`
   - Hình thức: Trực tuyến (default)
   - Thời gian: 15/07/2026 → 20/07/2026 (DatePicker workaround)
   - Địa điểm: `Online qua Zoom (R10 DT-004)`
   - Đối tượng tham gia: `CB ATLĐ DN xây dựng - test functional`
4. Click [Tạo khóa học]

## Kết quả mong đợi
- HTTP 201 + redirect to KH detail
- Auto-gen mã `KH-{YYYYMMDD}-{SEQ}` (vd `KH-20260510-008`)
- State `DU_THAO`

## Kết quả thực tế
```
POST /api/v1/khoa-hocs → 422 ERR-VAL-SYS-00-01

Validation errors:
- field: giangVienIds, message: "each value in giangVienIds must be a UUID"
- field: giangVienIds, message: "giangVienIds must contain at least 1 elements"
- field: giangVienIds, message: "giangVienIds must be an array"
```

→ Form FE không gửi `giangVienIds` (default undefined) → BE 422.

## Bằng chứng

**Form HTML inputs verified (10 elements):**
```
1. Tên khóa học (text)
2. Chương trình đào tạo (search/combobox)
3. Hình thức TRUC_TUYEN (radio)
4. Hình thức TRUC_TIEP (radio)
5. Ngày bắt đầu (text — RangePicker)
6. Ngày kết thúc (text — RangePicker)
7. Sĩ số tối đa (text spinbutton)
8. Số buổi học (text spinbutton)
9. Địa điểm (text)
10. Đối tượng tham gia (textarea)
```

→ **0 dropdown / select / multi-select cho "Giảng viên"**.

**BE schema discovered (POST với empty body):**
```
required: tenKhoaHoc, ctdtId, ngayBatDau, ngayKetThuc, giangVienIds
```

## So sánh spec
SRS FR-III + Mô hình A: KHOA_HOC junction `KHOA_HOC_GIANG_VIEN` (N-N) → KH cần ít nhất 1 GV. R7.3.15 R9 đã seed 7 KH thành công via API direct với `giangVienIds` filled từ fixture.

→ FE form chưa update theo BE schema mới. Cần dev FE add multi-select GV.

## Recommend dev FE
- Add multi-select dropdown "Giảng viên" trên form Tạo KH
- Required validation: tối thiểu 1 GV
- Source data: GET `/api/v1/giang-viens?trangThai=DANG_HOAT_DONG` (8 records seed R7.3.11)

## Impact
- DT-004 Tạo KH happy path qua UI: **BLOCKED** (FE form incomplete)
- R7.7.6 phase 2 cannot complete DT-004 cho đến khi FE fix

---

*R10 log | QA Automation via Claude Code MCP | 2026-05-10 09:48*
