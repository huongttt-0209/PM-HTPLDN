# Bug Report — LICH_HOC Validation Gaps (R7.4.B12 + R7.3.13 R10)

> **Module:** Đào tạo / Lịch học (LICH_HOC entity FR-III-22)
> **Discovered:** 2026-05-10 (R7.3.13 R10 + R7.4.B12 R10)
> **Reporter:** QA Automation Claude Code MCP

### Severity breakdown

| Tổng | Critical | Major | Medium | Minor | Trivial | Closed | Open |
|------|----------|-------|--------|-------|---------|--------|------|
| 4    | 0        | 2     | 0      | 2     | 0       | 4      | 0    |

> **Quy tắc đếm:**
> - `Tổng` = tổng số dòng bug trong **Bug Summary Table** (kể cả Closed strikethrough).
> - 5 cột severity (Critical / Major / Medium / Minor / Trivial) tổng = `Tổng`.
> - `Closed` + `Open` = `Tổng`. `Open` đếm Status ∈ {Open, Reopen}; `Closed` đếm Status ∈ {Closed, ~~closed~~}.
> - Update bảng này **sau MỖI lần đóng/mở bug** (cùng nhịp với rename Pass- prefix).

## Bug Summary

| ID | Severity | Title | Status |
|---|:-:|---|:-:|
| ~~BUG-LH-CONFLICT-01~~ | **Major** | BE accept overlap time — 2 buổi cùng ngày + chồng giờ của cùng KH được tạo thành công | **Closed** (R10 verified) |
| ~~BUG-LH-VAL-01~~ | Minor | TRUC_TUYEN thiếu `linkZoom` → BE 500 generic thay vì 422 ERR-LH-03 | **Closed** (R10 verified) |
| ~~BUG-LH-VAL-02~~ | Minor | TRUC_TIEP thiếu `diaDiem` → BE 500 generic thay vì 422 ERR-LH-04 | **Closed** (R10 verified) |
| ~~BUG-LH-VAL-03~~ | **Major** | `ngayHoc` ngoài khoảng `[ngayBatDau, ngayKetThuc]` của KH cha → BE 200 accept vi phạm ERR-LH-01 | **Closed** (R10 verified) |

> **Re-test:** 2026-05-10 R10 — ✅ ALL 4 PASS (Closed-verified). Sau cache clear + fresh login `cb_nv_tw_02`, probe 6 case POST `/api/v1/khoa-hocs/{KH-002}/lich-hocs` (KH-002 có ngayBatDau=2026-06-01, ngayKetThuc=2026-06-03):
>
> | # | Probe | HTTP | Error code |
> |---|---|:-:|---|
> | V3 | ngayHoc=2025-01-01 (trước range) | 400 | `ERR-VAL-III-23-04 "Ngày học phải nằm trong khoảng 2026-06-01 – 2026-06-03 của khóa học"` ✅ |
> | V3b | ngayHoc=2027-01-01 (sau range) | 400 | `ERR-VAL-III-23-04` ✅ |
> | V1 | TRUC_TUYEN no linkZoom | 400 | `ERR-VAL-III-23-05 "Buổi học trực tuyến phải có linkZoom"` ✅ |
> | V2 | TRUC_TIEP no diaDiem | 400 | `ERR-VAL-III-23-06 "Buổi học trực tiếp phải có địa điểm"` ✅ |
> | V4 base | 02/06 08:00-10:00 TRUC_TIEP | 201 | created (in-range, no overlap) |
> | V4 overlap | 02/06 09:00-10:30 (overlap base 08-10) | 409 | `ERR-BIZ-III-23-01 "Buổi học bị trùng giờ với buổi đã có (08:00:00–10:00:00)"` ✅ |
> | V4 non-overlap | 02/06 10:30-12:00 (boundary touching) | 201 | created (boundary OK) |
>
> Cả 2 record V4 (base + non-overlap) cleanup DELETE 204. Fix theo `_qa-summary-2026-05-10.md` line 176 stale-fixed sweep commit `af8276fd`. **Note error code drift vs SRS:** BE dùng `ERR-VAL-III-23-04/05/06` + `ERR-BIZ-III-23-01` (HTTP 400/409), bug original spec `ERR-LH-01/03/04/CONFLICT-01` (HTTP 422). Validation logic match spec, naming khác (per FR-III-22 / FR-III-23 numbering convention BE đang dùng). Acceptable — không re-open.
>
> Screenshot: [r10-verify-2026-05-10-lich-hoc-4-bugs-pass.png](../../screenshots/r10-verify-2026-05-10-lich-hoc-4-bugs-pass.png)

---

## BUG-LH-CONFLICT-01 — BE thiếu conflict validation overlap time

### Mô tả
BE chấp nhận tạo 2 buổi học cùng ngày với thời gian overlap nhau trong cùng một Khóa học. Vi phạm logic nghiệp vụ — không thể có 2 buổi học diễn ra song song trong cùng KH.

### Bước tái hiện
1. Login `cb_nv_tw_02` (CB_NV_TW)
2. Navigate KH-20260509-002 detail → tab Lịch học (đã có 3 buổi từ R7.3.13 R10)
3. Click **[+ Thêm buổi học]**
4. Fill form:
   - Ngày học: `15/06/2026` (cùng ngày buổi 1 hiện có 08:30-11:30 TRUC_TIEP)
   - Giờ bắt đầu: `09:00`
   - Giờ kết thúc: `10:30`
   - Hình thức: Trực tiếp
   - Địa điểm: "Conflict test"
5. Click **[Tạo]**

### Kết quả mong đợi
- HTTP 409 Conflict hoặc 422 Validation Error
- Error code `ERR-LH-CONFLICT-01` với message tiếng Việt
- FE hiển thị toast/inline error: "Buổi học chồng thời gian với buổi đã tồn tại của khóa này"

### Kết quả thực tế
- HTTP **201 Created** ✅
- Buổi mới tạo thành công với UUID
- List hiển thị 2 buổi cùng ngày 15/06/2026 overlap visible

### Bằng chứng
**Network log (reqid=384):**
```
POST /api/v1/khoa-hocs/fb24a75b-e338-4bf5-9410-aa8396231557/lich-hocs
Body: {
  "khoaHocId": "fb24a75b-...",
  "ngayHoc": "2026-06-15",
  "gioBatDau": "09:00",
  "gioKetThuc": "10:30",
  "hinhThucBuoi": "TRUC_TIEP",
  "diaDiem": "Conflict test - overlap with Buoi 1"
}
Response: 201 {success: true, data: {...id, version: 1}}
```

**UI list sau create:**
```
Row 1: 15/06/2026 08:30:00–11:30:00 Trực tiếp Hội trường A — Buoi 1
Row 2: 15/06/2026 09:00:00–10:30:00 Trực tiếp Conflict test — overlap visible ❌
Row 3: 16/06/2026 14:00:00–17:00:00 Trực tuyến (Buoi 2)
Row 4: 17/06/2026 08:00:00–11:00:00 Trực tiếp (Buoi 3)
```

### So sánh spec
SRS FR-III-22 (suspect — chưa quote line cụ thể) + nghiệp vụ general: KH có nhiều buổi học theo lịch, mỗi buổi có thời gian không overlap.

→ **Cần BA confirm spec line số.** Nếu spec chưa explicit, escalate dev BE bổ sung BR-LH-CONFLICT-01.

---

## BUG-LH-VAL-01 — TRUC_TUYEN thiếu linkZoom → BE 500 generic

### Mô tả
Khi POST với `hinhThucBuoi=TRUC_TUYEN` mà thiếu `linkZoom`, BE trả `ERR-SYS-00-00-01` (500-class generic) thay vì 422 field-level validation ERR-LH-03.

### Bước tái hiện
```bash
POST /api/v1/khoa-hocs/{khId}/lich-hocs
Body: {
  "khoaHocId": "<UUID>",
  "ngayHoc": "2026-06-18",
  "gioBatDau": "08:00",
  "gioKetThuc": "10:00",
  "hinhThucBuoi": "TRUC_TUYEN"
}
```

### Kết quả mong đợi
422 với:
```json
{"code":"ERR-LH-03","field":"linkZoom","message":"linkZoom bắt buộc khi hình thức Trực tuyến"}
```

### Kết quả thực tế
```json
{"success":false,"error":{"code":"ERR-SYS-00-00-01","message":"Lỗi hệ thống, vui lòng thử lại sau"}}
```

→ Generic 500 → noise log + UX kém. Cần dev add conditional validation rule.

---

## BUG-LH-VAL-02 — TRUC_TIEP thiếu diaDiem → BE 500 generic

Same pattern as BUG-LH-VAL-01 nhưng cho `hinhThucBuoi=TRUC_TIEP` thiếu `diaDiem`. Spec ERR-LH-04. BE trả `ERR-SYS-00-00-01` 500.

---

## BUG-LH-VAL-03 — ngayHoc ngoài khoảng KH → BE 200 accept

### Mô tả
BE accept tạo buổi học với `ngayHoc` nằm hoàn toàn ngoài khoảng `[ngayBatDau, ngayKetThuc]` của KH cha. Vi phạm spec ERR-LH-01.

### Bước tái hiện
KH-002: ngayBatDau=`01/06/2026`, ngayKetThuc=`03/06/2026`
```bash
POST /api/v1/khoa-hocs/{kh-002}/lich-hocs
Body: {
  "khoaHocId": "...",
  "ngayHoc": "2025-01-01",  ← 1 năm trước ngayBatDau KH
  "gioBatDau": "08:00",
  "gioKetThuc": "10:00",
  "hinhThucBuoi": "TRUC_TIEP",
  "diaDiem": "X"
}
```

### Kết quả mong đợi
422 với `ERR-LH-01: Ngày học phải nằm trong khoảng diễn ra khóa học`.

### Kết quả thực tế
HTTP **200 Created** ✅. Record `0aafc513` được tạo (đã cleanup R7.3.13 R10 via DELETE 204).

→ **Severity Major:** Cho phép pollute data với ngày invalid. Affect downstream điểm danh, lịch hiển thị, báo cáo.

---

## Recommend dev fix (1 batch 4 BUG)

```pseudocode
# Service: khoaHocLichHocService.create()

# Rule 1 — BUG-LH-CONFLICT-01
existingSlots = LICH_HOC.find(khoaHocId, ngayHoc)
for slot in existingSlots:
  if (gioBatDau < slot.gioKetThuc AND gioKetThuc > slot.gioBatDau):
    throw ERR-LH-CONFLICT-01

# Rule 2 — BUG-LH-VAL-01
if (hinhThucBuoi == "TRUC_TUYEN" AND empty(linkZoom)):
  throw ERR-LH-03

# Rule 3 — BUG-LH-VAL-02
if (hinhThucBuoi == "TRUC_TIEP" AND empty(diaDiem)):
  throw ERR-LH-04

# Rule 4 — BUG-LH-VAL-03
khoaHoc = KHOA_HOC.findById(khoaHocId)
if (ngayHoc < khoaHoc.ngayBatDau OR ngayHoc > khoaHoc.ngayKetThuc):
  throw ERR-LH-01
```

---

*R10 log | QA Automation via Claude Code MCP | 2026-05-10 02:45*
