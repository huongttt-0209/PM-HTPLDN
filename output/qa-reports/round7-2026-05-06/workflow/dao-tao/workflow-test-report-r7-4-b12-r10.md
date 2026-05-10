# Workflow Test Report — Quản lý Lịch học CRUD UI (R7.4.B12 — R10)

> **Module:** LICH_HOC CRUD UI (FR-III-22) · **SRS:** [`02-thu-tu-module.md §SM-LICH_HOC`](../../../../input/quy-trinh-nghiep-vu/02-thu-tu-module.md) · **Round:** R10 · **Date:** 2026-05-10 02:35-02:45 · **Tester:** QA Automation Claude Code MCP
> **Test mode:** UI click thực tế qua MCP với DatePicker workaround `type+Enter` (per memory `reference_antd_picker_workaround`).
> **Trigger:** User explicit "chạy R7.4.B12" sau R7.3.13 R10 unblock DatePicker workaround.

---

## 🎯 Tóm tắt nhanh (cho PM/BA)

**Kết quả: ⚠️ PARTIAL 7/8 — Bước 1-6 + 8 PASS clean (CRUD UI Create/Read/Update/Delete OK), Bước 7 conflict validation FAIL (BE 201 accept overlap thay vì 409/422).** R9 báo "chưa thấy Edit/Delete icons" SAI — icons có sẵn từ đầu, R9 chỉ chưa scroll/snapshot toàn row.

**1 BUG candidate Major mới phát hiện (Bước 7):** BE KHÔNG validate conflict — chấp nhận 2 buổi học cùng ngày overlap thời gian (POST 201). Bug logged + Open. Vì vậy task icon ⚠️ (không ✅) — chờ dev fix BUG-LH-CONFLICT-01 trước khi flip ✅.

| # | Bước test | Status | Endpoint |
|:-:|---|:-:|---|
| 1 | Tab Lịch học → "Thêm buổi học" → modal mở | ✅ | — |
| 2 | Fill form: ngày `18/06/2026` + giờ `09:00-12:00` + Trực tuyến + linkZoom | ✅ | DatePicker workaround `type+Enter` |
| 3 | Submit "Tạo" | ✅ | `POST /khoa-hocs/{id}/lich-hocs` 201 |
| 4 | Verify list hiển thị buổi mới (4 records) | ✅ | `GET .../lich-hocs` 200 |
| 5 | Click icon Edit row → modal "Sửa buổi học" data pre-filled → update ghiChu → Lưu | ✅ | `PATCH /lich-hocs/{id}` 200 (flat route) |
| 6 | Click icon Delete row → modal "Xác nhận xóa" hiển thị ngày giờ → Xóa | ✅ | `DELETE /lich-hocs/{id}` 204 (flat route) |
| 7 | **Conflict validate:** Tạo buổi 15/06 09:00-10:30 trùng overlap buổi 1 (15/06 08:30-11:30) | ❌ **BUG** | `POST` returned **201 Created** — no conflict check |
| 8 | Verify list final + cleanup pollution | ✅ | DELETE 204 cleanup OK |

**Ý nghĩa team:**
- ✅ FE+BE LICH_HOC CRUD UI hoàn chỉnh (Create/Read/Update/Delete với modal confirm + data pre-fill).
- ✅ Conditional render đúng: chọn "Trực tuyến" → field "Địa điểm" → "Link Zoom" (UX rõ).
- ⚠️ Cần dev BE thêm conflict validation (BR-LH suspected): chặn 2 buổi cùng ngày + overlap time của cùng KH.
- ⚠️ Cộng dồn từ R7.3.13 R10 → tổng 4 BUG candidate BE LICH_HOC validation: ERR-LH-01/03/04 (R7.3.13) + new conflict (R7.4.B12).

---

## ✅ R10 UI test 8 bước (chi tiết)

### Bước 1-4: Create buổi mới qua UI ✅

**Account:** `cb_nv_tw_02` (CB_NV_TW)

**Sequence:**
```
1. Navigate /dao-tao/khoa-hoc/{kh-002}?tab=lich-hoc
2. Click [+ Thêm buổi học]                                       → Modal "Thêm buổi học" mở
3. Click textbox "Ngày học" → type "18/06/2026" + Enter          → value="18/06/2026" ✅
4. Click textbox "Giờ bắt đầu" → type "09:00" + Enter            → value="09:00" ✅
5. Click textbox "Giờ kết thúc" → type "12:00" + Enter           → value="12:00" ✅
6. Click radio "Trực tuyến"                                       → checked + FE swap field "Địa điểm" → "Link Zoom" ✅
7. Click textbox "Link Zoom" → type "https://zoom.us/j/1234567890?pwd=R10b12"
8. Click textbox "Nội dung" → type "Buoi 4 R10 B12..."
9. Click [Tạo]                                                    → POST /khoa-hocs/{id}/lich-hocs 201 ✅
10. Verify list hiển thị 4 records (3 cũ + buổi 4 mới)            → ✅
```

**Network log (reqid 373):** `POST /api/v1/khoa-hocs/fb24a75b.../lich-hocs → 201` + auto refresh `GET .../lich-hocs → 200`.

### Bước 5: Edit row icon → PATCH ✅

```
1. Click button "edit" trên row buổi 4                            → Modal "Sửa buổi học" mở với data pre-filled:
   - Ngày học: "18/06/2026"
   - Giờ BĐ: "09:00", Giờ KT: "12:00"
   - Hình thức: "Trực tuyến" (radio checked)
   - Link Zoom: "https://zoom.us/j/1234567890?pwd=R10b12"
   - Nội dung: "Buoi 4 R10 B12..."
2. Click textbox "Ghi chú" → type "R10 B12 buoc 5 - PATCH ghi chu via UI edit modal"
3. Click [Lưu]                                                    → PATCH /lich-hocs/{id} 200 ✅ (flat route)
```

**FINDING ngược R9:** R9 báo "chưa thấy icon row action" SAI — Edit/Delete icons có sẵn trên mỗi row trong cột "Thao tác". Có thể R9 chưa scroll table hoặc tester miss.

### Bước 6: Delete row icon → confirm → DELETE 204 ✅

```
1. Click button "delete" trên row buổi 4                          → Modal "Xác nhận xóa" mở:
   "Xóa buổi học ngày 18/06/2026 (09:00:00–12:00:00)?"
2. Click [Xóa]                                                     → DELETE /lich-hocs/{id} 204 ✅ (flat route)
3. Verify list giảm về 3 records (buổi 4 removed)                 → ✅
```

UX modal xóa hiển thị ngày + giờ rõ — confirm before destructive action ✅.

### Bước 7: Conflict validation ❌ BUG

**Test setup:** KH-002 đã có buổi 1 (15/06/2026 08:30-11:30 Trực tiếp). Tạo buổi mới cùng ngày overlap time.

```
1. Click [+ Thêm buổi học]
2. Fill form: 15/06/2026 + 09:00-10:30 (overlap inside buổi 1) + Trực tiếp + "Conflict test"
3. Click [Tạo]
   → Expected: 409 Conflict / 422 Validation Error / FE block submit
   → Actual: POST /api/v1/khoa-hocs/{kh-002}/lich-hocs 201 ✅ (created!)
4. List hiển thị 2 buổi cùng ngày 15/06: 08:30-11:30 + 09:00-10:30 overlap visible
```

→ **BUG candidate Major:** BE KHÔNG validate conflict overlap. Vi phạm BR-LH conflict prevention.

**Cleanup R10:** Conflict record `1ed24f51` (giả định ID) đã DELETE 204 OK qua UI Delete icon → list trở về 3 records baseline.

### Bước 8: Verify list final + cleanup ✅

State BE final R10 sau R7.4.B12:
```json
GET /khoa-hocs/{kh-002}/lich-hocs  total=3

5d7898b6: 2026-06-15 08:30-11:30 TRUC_TIEP   v=2 (PATCH ghiChu R7.3.13)
c2ee1c96: 2026-06-16 14:00-17:00 TRUC_TUYEN  v=1
5577cffd: 2026-06-17 08:00-11:00 TRUC_TIEP   v=1
```

→ Identical baseline R7.3.13 R10. Buổi 4 + conflict record cleanup OK, không pollute downstream.

---

## API endpoint discovered R10 (full CRUD set)

| Method | Endpoint | Status | Note |
|:-:|---|:-:|---|
| POST | `/khoa-hocs/{khId}/lich-hocs` | ✅ 201 | Create — body required `khoaHocId`, `ngayHoc`, `gioBatDau`, `gioKetThuc`, `hinhThucBuoi` |
| GET | `/khoa-hocs/{khId}/lich-hocs` | ✅ 200 | List per KH |
| PATCH | `/lich-hocs/{lhId}` | ✅ 200 | Update — flat route (nested 404). Optimistic lock version field |
| DELETE | `/lich-hocs/{lhId}` | ✅ 204 | Delete — flat route (nested 404) |

**REST inconsistency Minor (carried from R7.3.13):** Mutation phải qua flat `/lich-hocs/{id}` route, list/create qua nested `/khoa-hocs/{khId}/lich-hocs`. FE đã handle đúng.

---

## ⚠️ BUG candidates — LICH_HOC validation gaps

Cộng dồn R7.3.13 R10 + R7.4.B12 R10:

| ID | Severity | Description | Status |
|---|:-:|---|:-:|
| BUG-LH-CONFLICT-01 | **Major** | BE KHÔNG validate conflict overlap — 2 buổi cùng ngày + overlap time của cùng KH được create thành công | ❌ Open |
| BUG-LH-VAL-01 | Minor | TRUC_TUYEN thiếu `linkZoom` → BE trả `ERR-SYS-00-00-01` (500 generic) thay vì 422 ERR-LH-03 | ❌ Open (R7.3.13) |
| BUG-LH-VAL-02 | Minor | TRUC_TIEP thiếu `diaDiem` → BE trả `ERR-SYS-00-00-01` (500 generic) thay vì 422 ERR-LH-04 | ❌ Open (R7.3.13) |
| BUG-LH-VAL-03 | Major | `ngayHoc` ngoài khoảng KH (KH-002 BĐ 01/06 - KT 03/06, ngayHoc=2025-01-01) → BE 200 accept | ❌ Open (R7.3.13) |

**Recommend escalate dev BE:** 4 bugs in 1 batch — implement validation rules ERR-LH-01/03/04/conflict cho LICH_HOC entity tại NestJS DTO + service layer.

---

## Findings R10

### 1. ✅ FE LICH_HOC CRUD UI hoàn chỉnh

R9 báo "Edit/Delete icons chưa thấy" → SAI. Cả 4 row actions hoạt động full:
- Tab Lịch học có Empty state "Chưa có buổi học nào." khi 0 record + button [+ Thêm buổi học] luôn visible
- Mỗi row có cột "Thao tác" với 2 button icon (edit/delete)
- Edit modal pre-fill data đúng từ API GET single record
- Delete modal hiển thị ngày + giờ trong message confirm
- FE auto-refresh list sau mutation OK (POST/PATCH/DELETE → GET re-fetch)

### 2. ✅ FE conditional render hình thức

Chọn radio "Trực tiếp" → field "Địa điểm" (text input).
Chọn radio "Trực tuyến" → field swap thành "Link Zoom" (text input).

→ UX rõ. Tuy nhiên FE KHÔNG enforce required cho linkZoom/diaDiem — submit empty vẫn pass FE (BE trả 500 generic, xem BUG-LH-VAL-01/02).

### 3. ⚠️ BUG MAJOR mới — BE thiếu conflict validation

`POST /khoa-hocs/{khId}/lich-hocs` accept buổi học cùng ngày + overlap time với buổi đã tồn tại của cùng KH. Vi phạm logic nghiệp vụ — không thể có 2 buổi học diễn ra song song trong cùng khóa học.

**Test reproducer:**
```
GIVEN KH-002 has buổi 1: 15/06/2026 08:30-11:30 TRUC_TIEP "Hội trường A"
WHEN  POST {ngayHoc: "2026-06-15", gioBatDau: "09:00", gioKetThuc: "10:30", hinhThucBuoi: "TRUC_TIEP", diaDiem: "..."}
THEN  Expected: 409 Conflict / 422 BR-LH-CONFLICT
      Actual: 201 Created  ❌
```

**Severity Major** — affect data integrity + UX. Cần escalate dev BE:
- Add validation rule trong service `khoaHocLichHocService.create()`:
  ```pseudocode
  existingSlots = LICH_HOC.find(khoaHocId=X, ngayHoc=Y)
  for slot in existingSlots:
    if (gioBatDau < slot.gioKetThuc AND gioKetThuc > slot.gioBatDau):
      throw ERR-LH-CONFLICT-01
  ```

### 4. ✅ DatePicker workaround `type+Enter` works repeatedly

R7.3.13 R10 discovered + R7.4.B12 R10 confirmed reuse — workaround robust qua nhiều lần test (4 buổi tạo + 1 conflict + 1 edit modal tất cả đều bind value đúng). Memory `reference_antd_picker_workaround.md` đã updated.

### 5. ✅ Modal confirm UX đầy đủ

- Modal Edit pre-fill data từ existing record (không cần GET single, có thể từ list cache)
- Modal Delete hiển thị specific record info (ngày + giờ) → user xác nhận chính xác record nào bị xóa
- Cả 2 modal có button "Hủy" để abort

### 6. ⚠️ Long type_text crash MCP (carry-over technique note)

R7.3.13 R10 đã noted MCP browser crash khi type_text >100 chars. R10 R7.4.B12 dùng text ngắn (<60 chars) → không crash. Tester technique: chia type_text thành chunks nhỏ.

---

## Cascade impact (post-R10)

| Task | Pre-R10 | Post-R10 | Reason |
|---|---|---|---|
| **R7.4.B12 Quản lý lịch học** | 🟢 sẵn sàng | ⚠️ PARTIAL 7/8 (Bước 7 conflict FAIL) | CRUD UI verified end-to-end; conflict validation BE thiếu |
| **R7.7.6 DT-056 LICH_HOC CRUD test** | 🚫 chờ workaround | ✅ inherit từ R7.4.B12 R10 | Same test scope |
| **R7.7.6 DT-056a negative validation** | 🚫 chờ workaround | ⚠️ inherit + thêm BUG-LH-CONFLICT-01 | 4 BUG candidates cộng dồn |
| **R7.4.B7 ĐiỂm danh DT-011** | 🚫 chờ HOC_VIEN | 🚫 vẫn chờ R7.3.12 | Independent block |

---

## Bằng chứng

### Network log R7.4.B12 R10 (chronological)
```
POST /api/v1/khoa-hocs/{kh-002}/lich-hocs              → 201  (B1-4 buổi 4 created)
GET  /api/v1/khoa-hocs/{kh-002}/lich-hocs              → 200  (auto refresh, 4 records)
PATCH /api/v1/lich-hocs/{lh-4}                         → 200  (B5 edit ghiChu)
GET  /api/v1/khoa-hocs/{kh-002}/lich-hocs              → 200  (auto refresh)
DELETE /api/v1/lich-hocs/{lh-4}                        → 204  (B6 delete buổi 4)
GET  /api/v1/khoa-hocs/{kh-002}/lich-hocs              → 200  (auto refresh, 3 records)
POST /api/v1/khoa-hocs/{kh-002}/lich-hocs              → 201  (B7 conflict test — BUG accept)
GET  /api/v1/khoa-hocs/{kh-002}/lich-hocs              → 200  (4 records, conflict visible)
DELETE /api/v1/lich-hocs/{lh-conflict}                 → 204  (B8 cleanup)
GET  /api/v1/khoa-hocs/{kh-002}/lich-hocs              → 200  (3 records baseline restored)
```

### Screenshot
[r7-4-b12-r10-lich-hoc-final-3-records.png](r7-4-b12-r10-lich-hoc-final-3-records.png) — Final state 3 buổi sau cleanup conflict pollution.

---

## Lịch sử round

| Round | Date | Kết quả |
|---|---|---|
| R8 | 2026-05-08 | Endpoint 404 — BE chưa deploy |
| R9 | 2026-05-09 | ⏳ BE deploy + UI tab có. Step 2 fill form blocked AntD picker. Step 5/6 báo "chưa thấy icon" (sai diagnose). |
| **R10** | **2026-05-10** | **⚠️ PARTIAL 7/8 PASS** — Bước 1-6 + 8 PASS clean. Bước 7 conflict FAIL (BE 201 accept overlap). DatePicker workaround unblock. Edit/Delete icons exist. **1 BUG Major mới** — BUG-LH-CONFLICT-01 logged Open. |

---

*R10 verify | QA Automation via Claude Code MCP | 2026-05-10 02:45 — UI mode (DatePicker workaround `type+Enter`)*
