# Bug Report — Báo cáo Thống kê (R7.7.13)

| Thông tin | Giá trị |
|-----------|---------|
| **Dự án** | PM HTPLDN |
| **Môi trường** | http://103.172.236.130:3000/ |
| **Người test** | QA Automation (Claude Code via Chrome DevTools MCP) |
| **Ngày** | 2026-05-10 02:09:00 |
| **Loại test** | Functional (Module Báo cáo Thống kê — task R7.7.13) |
| **Round** | Round 7 (R7.7.13 lần 1) |
| **Tài liệu tham chiếu** | [funtion 7.11](../../../../funtion/7.11-bao-cao-thong-ke.md) · [SRS CHANGELOG-v3-to-v3.5 §srs-fr-11](../../../../../input/srs-update-2026-5-5/CHANGELOG-v3-to-v3.5.md) · [todo R7.7.13](../../../../../tasks/todo-bao-cao.md#r7-7-13) |

---

## Tổng hợp

Phát hiện **3** lỗi có SRS reference cụ thể trong phase smoke + functional module Báo cáo Thống kê. **Round 1 (2026-05-10 02:09)** log 2 Major UI/UX (Word→PDF rename, Hỏi đáp pháp luật rename) — cả 2 đã được dev fix và Closed-verified ở **Round 2 (2026-05-10 12:35)**. Round 2 phát hiện thêm **1 Critical mới** — endpoint xuất PDF (`/api/v1/bao-cao/export` với `formatXuat=PDF`) trả 500 toàn bộ, nhánh xuất Excel hoạt động bình thường.

> **Bối cảnh:** Round 1 bị BE bug R7.4.B0 (JWT revoke aggressive ~30s-1min) làm block 36/40 TC. Round 2 (sau dev báo fix JWT) re-test: JWT đã ổn định qua 16 BC switches + 2 export calls trong 1 session, không bị kick `/login`. Đã chạy được 16/16 BC core (BC-004→BC-023, defer 4 ĐT/ĐG) — render OK 100%, 12 BC có data, 4 BC empty hợp lệ (CT HTPLDN seed chưa).

### Severity breakdown

| Tổng | Critical | Major | Medium | Minor | Trivial |
|------|----------|-------|--------|-------|---------|
| 3    | 1        | 2     | 0      | 0     | 0       |

## Bug Summary Table

| Bug ID | Severity | Priority | Type | TC Ref | **SRS Reference** | Title | Status |
|--------|----------|----------|------|--------|-------------------|-------|--------|
| BUG-BC-PDF-500-001 | Critical | P0 | Workflow | BC-025 | `srs-update-2026-5-5/CHANGELOG-v3-to-v3.5.md §srs-fr-11-bao-cao.md` Thay đổi 6 line 509-519 — Acceptance Criteria "Given CB nhấn 'Xuất PDF' When click Then tải file `.pdf` theo format TT17/2025" | POST `/api/v1/bao-cao/export` formatXuat=PDF trả 500 `ERR-SYS-00-00-01` cho mọi BC — endpoint xuất PDF chưa hoàn thiện | Open |
| ~~BUG-BC-WORD-001~~ | Major | P1 | UI/UX | BC-024, BC-025 | `srs-update-2026-5-5/CHANGELOG-v3-to-v3.5.md §srs-fr-11-bao-cao.md` Thay đổi 6 (line 509-519) — `SCR-IX-01 row Nút Xuất line 1047` | ~~Button "Xuất Word" thay vì "Xuất PDF" — chưa apply Thay đổi 6 v3.5 (TT 17/2025 đổi DOCX→PDF)~~ | Closed |
| ~~BUG-BC-HOIDAP-PL-001~~ | Major | P1 | UI/UX | BC-001, BC-006 | `srs-update-2026-5-5/CHANGELOG-v3-to-v3.5.md §srs-fr-11-bao-cao.md` Thay đổi 2 (line 463-466, 552) — ITEM-14 đối tác TT CNTT | ~~Group label "Hỏi đáp" + tên BC "BC Số lượng hỏi đáp/vướng mắc" thiếu chữ "pháp luật" — chưa apply Thay đổi 2 v3.5 rename CR-09~~ | Closed |

---

## BUG-BC-PDF-500-001 — POST `/api/v1/bao-cao/export` formatXuat=PDF trả 500 trên mọi BC

### Mô tả

Cán bộ TW đăng nhập module Báo cáo Thống kê, chọn BC bất kỳ + Kỳ + Thời gian + click "Xem báo cáo" OK, rồi click "Xuất PDF". BE trả `500 ERR-SYS-00-00-01 "Lỗi hệ thống, vui lòng thử lại sau"` ngay cả khi request body hợp lệ. Đã verify trên 2 BC (BC-001 Hỏi đáp pháp luật + BC-004 Vụ việc đã hoàn thành) → cùng 500. Endpoint xuất Excel hoạt động bình thường (200 + binary xlsx) → bug isolated tới nhánh `formatXuat=PDF` trong service xuất.

### Các bước tái hiện

1. Login `cb_nv_tw_03` / `Secret@123` → OTP `666666` → Dashboard.
2. Click sidebar **Báo cáo thống kê** → URL `/bao-cao` render OK.
3. Chọn Loại báo cáo = `BC Số lượng hỏi đáp/vướng mắc pháp luật` (BC-001).
4. Chọn Kỳ báo cáo = `Tháng`. Thời gian auto-fill `2026-05-01 — 2026-05-31`.
5. Click `Xem báo cáo` → table + chart render OK (verify GET `/api/v1/bao-cao/hoi-dap` trả 200).
6. Click button `Xuất PDF`. Quan sát Network tab.
7. Lặp với BC-004 `BC Vụ việc đã hoàn thành` cùng kỳ Tháng → cùng kết quả.

### Kết quả mong đợi

Theo `srs-update-2026-5-5/CHANGELOG-v3-to-v3.5.md §srs-fr-11-bao-cao.md` Thay đổi 6:

- Line 84 §2 TPL-REPORT-FULL Processing Bước 8: "Nếu xuất PDF: tạo file `.pdf` giữ nguyên định dạng trình bày theo Thông tư 17/2025 (khổ A4, font Times New Roman cỡ 13)"
- Line 122 §2 Acceptance Criteria: "Given CB nhấn 'Xuất PDF' When click Then tải file `.pdf` theo format TT17/2025"

POST `/api/v1/bao-cao/export` body `{loaiBaoCao,kyBaoCao,tuNgay,denNgay,formatXuat:"PDF"}` phải trả 200 + `content-type: application/pdf` + binary body file PDF khổ A4 font Times New Roman 13pt.

### Kết quả thực tế

Cùng request body cho XLSX trả 200 + binary xlsx OK; đổi `formatXuat: "PDF"` → 500 toàn bộ.

```
POST /api/v1/bao-cao/export
Body: {"loaiBaoCao":"BC_VU_VIEC_HOAN_THANH","kyBaoCao":"THANG","tuNgay":"2026-05-01","denNgay":"2026-05-31","filterDacThu":{},"formatXuat":"PDF"}

Response 500:
{"success":false,"error":{"code":"ERR-SYS-00-00-01","message":"Lỗi hệ thống, vui lòng thử lại sau","timestamp":"2026-05-10T05:27:12.220Z","requestId":"061ca8f0-01a1-4182-98bc-6241e8156b97"}}
```

Đối chiếu với XLSX cùng BC (verified 200, reqid=288):

```
POST /api/v1/bao-cao/export
Body: {"loaiBaoCao":"BC_HOI_DAP","kyBaoCao":"THANG","tuNgay":"2026-05-01","denNgay":"2026-05-31","filterDacThu":{},"formatXuat":"XLSX"}

Response 200:
content-type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
content-disposition: attachment; filename="bao-cao-hoi-dap-2026-05-10.xlsx"
Body: <binary data>
```

### Bằng chứng

**1. Ảnh chụp** *(Network tab thể hiện POST `/api/v1/bao-cao/export` 500 cho PDF)*:

![BUG-BC-PDF-500-001 — PDF export trả 500 ERR-SYS-00-00-01](image/bug-bc-pdf-500-export-error.png)

**2. API response 500 (BC-004 PDF, requestId `061ca8f0-01a1-4182-98bc-6241e8156b97`)**:

```json
{
  "success": false,
  "error": {
    "code": "ERR-SYS-00-00-01",
    "message": "Lỗi hệ thống, vui lòng thử lại sau",
    "timestamp": "2026-05-10T05:27:12.220Z",
    "requestId": "061ca8f0-01a1-4182-98bc-6241e8156b97"
  }
}
```

**3. API response 500 (BC-001 PDF, requestId `949319b9-2f9e-40e7-bcc1-2f7cd217bd5e`)**:

```json
{
  "success": false,
  "error": {
    "code": "ERR-SYS-00-00-01",
    "message": "Lỗi hệ thống, vui lòng thử lại sau",
    "timestamp": "2026-05-10T05:24:59.177Z",
    "requestId": "949319b9-2f9e-40e7-bcc1-2f7cd217bd5e"
  }
}
```

---

## ~~BUG-BC-WORD-001~~ [CLOSED] — Button "Xuất Word" thay vì "Xuất PDF" trên SCR-IX-01 (chưa apply TT 17/2025)

> **Re-test:** 2026-05-10 02:35:00 R7.7.13-r2 — ✅ PASS (Closed-verified). Login `cb_nv_tw_03` → `/bao-cao` → action area hiển thị `Xem báo cáo` + `Xuất Excel` + **`file-pdf Xuất PDF`** (không còn "Xuất Word"). FE đã apply Thay đổi 6 v3.5 (TT 17/2025).

### Mô tả

Cán bộ TW đăng nhập module Báo cáo Thống kê (`/bao-cao`). Vùng action header có 3 button: `Xem báo cáo`, `Xuất Excel`, **`Xuất Word`**. Theo Thay đổi 6 v3.5 (TT 17/2025/TT-BTP) định dạng xuất Word `.docx` đã được đổi sang PDF `.pdf` — UI vẫn để Word, không còn nút PDF.

### Các bước tái hiện

1. Login `cb_nv_tw_02` / `Secret@123` → OTP `666666` → Dashboard.
2. Click sidebar **Báo cáo thống kê** → URL `/bao-cao` render OK.
3. Quan sát vùng action ngang hàng với form filter (Loại báo cáo / Kỳ báo cáo / Đơn vị):
   - Button 1: "search Xem báo cáo" (enabled).
   - Button 2: "file-excel Xuất Excel" (disabled khi chưa Xem BC).
   - Button 3: **"file-word Xuất Word"** (disabled khi chưa Xem BC).
4. Quan sát: KHÔNG có button "Xuất PDF" trong UI.

### Kết quả mong đợi

Theo `srs-update-2026-5-5/CHANGELOG-v3-to-v3.5.md §srs-fr-11-bao-cao.md` Thay đổi 6 (line 509-519):

- §2 TPL-REPORT-FULL Processing chung Bước 8 (line 84): "Nếu xuất PDF: tạo file `.pdf` giữ nguyên định dạng trình bày theo Thông tư 17/2025 (khổ A4, font Times New Roman cỡ 13)"
- §2 TPL-REPORT-FULL Acceptance Criteria (line 122): "Given CB nhấn 'Xuất PDF' When click Then tải file `.pdf` theo format TT17/2025"
- §3 SCR-IX-01 Nút Xuất (line 1047): **"Xuất PDF (.pdf) → xuất theo mẫu TT17/2025"**

UI phải hiển thị 2 button: `Xuất Excel` (`.xlsx`) + **`Xuất PDF`** (`.pdf`). Click "Xuất PDF" tải file `.pdf` khổ A4, font Times New Roman 13pt.

### Kết quả thực tế

UI vẫn còn button **"file-word Xuất Word"** thay vì "Xuất PDF". Không có nút Xuất PDF nào trong UI.

A11y snapshot:
```
uid=16_19 button "search Xem báo cáo"
uid=16_20 button "file-excel Xuất Excel" disableable disabled
uid=16_21 button "file-word Xuất Word" disableable disabled
```

### Bằng chứng

**1. Ảnh chụp** *(màn hình `/bao-cao` action area, button "Xuất Word" hiển thị thay vì "Xuất PDF")*:

![BUG-BC-WORD-001 — Action area /bao-cao có button "Xuất Word" thay vì "Xuất PDF"](image/bug-bc-001-xuat-word-button.png)

---

## ~~BUG-BC-HOIDAP-PL-001~~ [CLOSED] — Group dropdown "Hỏi đáp" + tên BC "BC Số lượng hỏi đáp/vướng mắc" thiếu chữ "pháp luật"

> **Re-test:** 2026-05-10 02:35:00 R7.7.13-r2 — ✅ PASS (Closed-verified). Dropdown `Loại báo cáo` group đầu = **`Hỏi đáp pháp luật`**, option = **`BC Số lượng hỏi đáp/vướng mắc pháp luật`** (verify qua `evaluate_script`). FE đã apply Thay đổi 2 v3.5 rename CR-09.

### Mô tả

Cán bộ TW mở dropdown "Loại báo cáo" trên `/bao-cao`. Group đầu tiên hiển thị label `Hỏi đáp` với option `BC Số lượng hỏi đáp/vướng mắc`. Theo Thay đổi 2 v3.5 (yêu cầu đối tác TT CNTT, ITEM-14, đồng bộ với CR-09 nhóm FR-02 hỏi đáp) text phải là **"Hỏi đáp pháp luật"** ở cả group label và tên BC. UI chưa apply rename.

### Các bước tái hiện

1. Login `cb_nv_tw_02` / `Secret@123` → OTP `666666` → Dashboard.
2. Click sidebar **Báo cáo thống kê** → URL `/bao-cao`.
3. Click dropdown **Loại báo cáo** (`#loaiBaoCao`) → dropdown render 23 option chia 8 group.
4. Quan sát group đầu (vị trí top): label = `Hỏi đáp` (KHÔNG có "pháp luật").
5. Option duy nhất trong group đầu: `BC Số lượng hỏi đáp/vướng mắc` (KHÔNG có "pháp luật").

### Kết quả mong đợi

Theo `srs-update-2026-5-5/CHANGELOG-v3-to-v3.5.md §srs-fr-11-bao-cao.md` Thay đổi 2 (line 463-466):

> "Đổi tên báo cáo hỏi đáp pháp lý → hỏi đáp pháp luật ... liệt kê 3 vị trí cần đổi: mục lục tài liệu chính, **danh sách thả xuống chọn loại báo cáo trong FR-11** và tên báo cáo FR-IX-01. v4 đã áp 2 vị trí thuộc FR-11"

Cite CHANGELOG `_DELTA-MAP-CROSS-CUTTING` line 552:

> "**srs-v3.md mục lục danh sách FR group** (Thay đổi 2): 'BC Hỏi đáp' → '**Báo cáo hỏi đáp pháp luật**' — đồng bộ với CR-09."

UI phải hiển thị:
- Group label: `Hỏi đáp pháp luật` (hoặc `Báo cáo hỏi đáp pháp luật`)
- Option text: `BC Số lượng hỏi đáp/vướng mắc pháp luật` (hoặc tương đương rename CR-09 nhóm FR-02 đã áp)

### Kết quả thực tế

Dropdown render giữ nguyên text v3 cũ:
- Group label: `Hỏi đáp`
- Option: `BC Số lượng hỏi đáp/vướng mắc`

`evaluate_script` output (verified 2026-05-10 02:07:30 UTC+7):

```json
{
  "ordered": [
    {"type":"group","text":"Hỏi đáp"},
    {"type":"opt","text":"BC Số lượng hỏi đáp/vướng mắc"},
    {"type":"group","text":"Vụ việc"},
    ...
  ]
}
```

URL query khi chọn option này: `?loai=hoi-dap&kyBaoCao=THANG&...` — slug nội bộ vẫn `hoi-dap` đúng (rename không cần phá API), chỉ label UI sai.

### Bằng chứng

**1. Ảnh chụp** *(dropdown "Loại báo cáo" mở, group đầu tiên hiển thị "Hỏi đáp" + option "BC Số lượng hỏi đáp/vướng mắc")*:

![BUG-BC-HOIDAP-PL-001 — Dropdown loại BC group "Hỏi đáp" thiếu "pháp luật"](image/bug-bc-002-group-hoidap-pl-thieu.png)

**2. Output evaluate_script** *(phụ trợ — 23 BC + 8 group toàn bộ)*:

```json
{
  "holder": {"sH": 992, "cH": 256},
  "optionCount": 23,
  "groupCount": 8,
  "groups": ["Hỏi đáp", "Vụ việc", "Đào tạo", "CG/TVV", "Đánh giá", "VV phân tích", "Chi phí", "CT HTPLDN"]
}
```

8 group hiện tại: `Hỏi đáp` ❌ (thiếu "pháp luật"), Vụ việc ✅, Đào tạo ✅, CG/TVV ✅, Đánh giá ✅, VV phân tích ✅, Chi phí ✅, CT HTPLDN ✅.

---

## Phụ lục — Môi trường test

| Thành phần | Giá trị |
|------------|---------|
| URL ứng dụng | http://103.172.236.130:3000/ |
| OTP login | `666666` (bypass tạm) |
| MailHog (OTP inbox) | http://103.172.236.130:8025 |
| API base | http://103.172.236.130:3000/api/v1/ |
| Frontend | React + Vite + Ant Design (custom wrapper class `ant-select-content` thay `ant-select-selector`) |
| Xác thực | JWT + OTP — JWT revoke aggressive ~30s-1min (bug R7.4.B0 cascade) |
| Tool test | Chrome DevTools MCP (`mcp__chrome-devtools__*`) |

---

*Bug report generated: 2026-05-10 02:09:00 UTC+7 | QA Automation via Claude Code*
