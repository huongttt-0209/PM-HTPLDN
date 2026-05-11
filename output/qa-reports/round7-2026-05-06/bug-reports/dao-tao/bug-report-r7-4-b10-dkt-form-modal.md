# Bug Report — Đề kiểm tra Form Modal (R7.4.B10 R10)

| Thông tin | Giá trị |
|-----------|---------|
| **Dự án** | PM HTPLDN |
| **Môi trường** | http://103.172.236.130:3000/ |
| **Người test** | QA Automation via Claude Code (MCP) |
| **Ngày** | 2026-05-10 |
| **Loại test** | Workflow (R7.4.B10 R10 re-verify post FE-REGRESSION-01 fix) |
| **Round** | Round 7 — R10 |
| **Tài liệu tham chiếu** | [tasks/todo-dao-tao.md R7.4.B10](../../../../tasks/todo-dao-tao.md) · [SRS FR-III-NEW-02](../../../../input/srs-update-2026-5-5/srs-fr-03-dao-tao.md) · [workflow-test-report-r7-4-b10-r10.md](../../workflow/dao-tao/workflow-test-report-r7-4-b10-r10.md) |

---

## Tổng hợp

Sau khi BUG-DKT-FE-REGRESSION-01 (R9) closed (action buttons render đầy đủ), R10 verify 8 bước workflow R7.4.B10 phát hiện **2 bug FE form modal mới**:

1. Modal **Cập nhật** ĐKT không pre-fill `cachTao` từ record → form luôn invalid → bước Sửa BLOCKED qua UI.
2. Modal **Tạo** ĐKT thiếu field UI chọn câu hỏi (`cauHoiIds`) → submit POST 422.

## Bug Summary Table

| Bug ID | Severity | Priority | Type | TC Ref | **SRS Reference** | Title | Status |
|--------|----------|----------|------|--------|-------------------|-------|--------|
| BUG-DKT-EDIT-FORM-01 | Major | P1 | UI/FE | R7.4.B10 Bước 2 | `srs-fr-03-dao-tao.md FR-III-NEW-02 Processing-Sửa Bước 1-3` | Modal Cập nhật ĐKT không pre-fill `cachTao` từ record → combobox disabled + value rỗng + required → form luôn invalid | **Open** |
| BUG-DKT-CREATE-FORM-01 | Major | P1 | UI/FE | R7.4.B10 Bước 1b | `srs-fr-03-dao-tao.md FR-III-NEW-02 Processing-Tạo Bước 2-3` | Modal Tạo ĐKT thiếu field UI chọn câu hỏi (`cauHoiIds`) → BE 422 ERR-VAL-SYS-00-01 | **Open** |

---

## BUG-DKT-EDIT-FORM-01 — Modal Cập nhật ĐKT không pre-fill `cachTao`

### Mô tả

Trong modal "Cập nhật đề kiểm tra" mở từ button `edit Chỉnh sửa` trên trang chi tiết ĐKT NHAP, combobox `Cách tạo` (required) hiển thị disabled + value placeholder "Chọn cách tạo đề" (rỗng) + status `ant-select-status-error`. Record gốc có `cachTao="THU_CONG"` (verified API GET) nhưng FE không bind value vào form. Submit "Cập nhật" → AntD validation chặn với "Vui lòng chọn cách tạo" → form không POST được.

### Bước tái hiện

1. Login `cb_nv_tw_02 / Secret@123` + OTP `666666`.
2. Sidebar → Quản lý đào tạo → Ngân hàng câu hỏi & Đề kiểm tra → tab "Đề kiểm tra".
3. Click row "ĐKT cuối khóa - Sở hữu trí tuệ 2026 - R9" → vào detail page.
4. Click button "edit Chỉnh sửa" → modal "Cập nhật đề kiểm tra" hiện.
5. Quan sát: field "Cách tạo" disabled + placeholder "Chọn cách tạo đề" + ngay lúc mở đã có border đỏ + text "Vui lòng chọn cách tạo" — chưa nhập gì đã invalid.
6. Sửa Tên + giữ Time/Điểm → click "Cập nhật".
7. Form không submit, modal vẫn mở, không có network POST request mới.

### Kết quả mong đợi

- Modal mở phải pre-fill mọi field từ record gốc: `cachTao="THU_CONG"`, `tenDe`, `thoiGianLamBai`, `diemDat`.
- Combobox `Cách tạo` disabled vì spec không cho phép đổi cách tạo (acceptable), nhưng **value phải hiển thị "Thủ công"** đúng record, không phải rỗng.
- Submit "Cập nhật" → POST `PATCH /api/v1/de-kiem-tras/{id}` body có `cachTao` field → BE 200 OK.

### Kết quả thực tế

- Combobox `Cách tạo` disabled + value rỗng + status error → form invalid ngay khi mở modal.
- Click "Cập nhật" → AntD form validation chặn, không submit.
- Hậu quả: end-user không thể sửa ĐKT NHAP qua UI.

### Bằng chứng

- Screenshot: [r10-bug-dkt-edit-no-prefill-cachtao.png](../../screenshots/r10-bug-dkt-edit-no-prefill-cachtao.png)
- DOM probe: combobox `.ant-select` có classList chứa `ant-select-disabled`, `ant-select-status-error` nhưng `value=""` và record API `cachTao="THU_CONG"`.

---

## BUG-DKT-CREATE-FORM-01 — Modal Tạo ĐKT thiếu field chọn câu hỏi (`cauHoiIds`)

### Mô tả

Modal "Tạo đề kiểm tra" mở từ button "Tạo đề kiểm tra" trên list page chỉ có 4 field: `Tên đề` / `Cách tạo` / `Thời gian làm bài` / `Điểm đạt`. Không có UI để chọn câu hỏi từ Ngân hàng câu hỏi (NHCH). Submit POST `/api/v1/de-kiem-tras` → BE 422 với mã `ERR-VAL-SYS-00-01` field `cauHoiIds` message `"cauHoiIds must contain at least 1 elements"`. End-user không có cách tạo ĐKT mới qua UI.

### Bước tái hiện

1. Login `cb_nv_tw_02 / Secret@123` + OTP `666666`.
2. Sidebar → Quản lý đào tạo → Ngân hàng câu hỏi & Đề kiểm tra → tab "Đề kiểm tra".
3. Click button "Tạo đề kiểm tra" → modal mở.
4. Fill: Tên = "R10 Test", Cách tạo = "Thủ công", Time = 30, Điểm = 5.
5. Quan sát modal — không có section "Chọn câu hỏi" / list NHCH.
6. Click "Tạo mới" → POST 422.

### Kết quả mong đợi

- Theo SRS FR-III-NEW-02 Inputs: `cau_hoi_ids` field bắt buộc khi `cachTao=THU_CONG` (chọn câu hỏi từ NHCH) hoặc UI tự sinh khi `cachTao=NGAU_NHIEN` (random pick từ filter).
- Modal phải có UI section thứ 5: "Chọn câu hỏi" với checkbox list NHCH (filter LV/Mức độ/Loại) hoặc transfer-component.

### Kết quả thực tế

- Modal chỉ có 4 field, thiếu UI chọn `cauHoiIds`.
- POST → 422 `ERR-VAL-SYS-00-01 cauHoiIds must contain at least 1 elements`.
- Hậu quả: end-user không thể tạo ĐKT mới qua UI. Pre-existing 5 ĐKT R8/R9 baseline có thể đã được tạo qua API direct (không qua UI).

### Bằng chứng

```
reqid=1514 POST /api/v1/de-kiem-tras [422]
body: {tenDe: "R10 Verify Delete + Distribute Test", cachTao: "THU_CONG", thoiGianLamBai: 30, diemDat: 5}
response: {
  "error": {
    "code": "ERR-VAL-SYS-00-01",
    "field": "cauHoiIds",
    "message": "cauHoiIds must contain at least 1 elements",
    "details": [
      {"field": "cauHoiIds", "message": "cauHoiIds must contain at least 1 elements"},
      {"field": "cauHoiIds", "message": "each value in cauHoiIds must be a UUID"},
      {"field": "cauHoiIds", "message": "cauHoiIds must be an array"}
    ]
  }
}
```

---

## Phụ lục — Môi trường test

| Thành phần | Giá trị |
|------------|---------|
| URL | http://103.172.236.130:3000 |
| Account | `cb_nv_tw_02 / Secret@123` (CB_NV_TW BTP, full perms) |
| OTP | `666666` |
| Tool | Chrome DevTools MCP |
| Cache | Cleared (`caches.delete + SW unregister + localStorage.clear`) trước verify |

---

*Bug report generated R10: 2026-05-10 | QA Automation via Claude Code (Chrome DevTools MCP)*
