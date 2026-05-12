# Bug Report — Báo cáo Thống kê (Export Excel/Word) — R7.5.4

| Thông tin | Giá trị |
|-----------|---------|
| **Dự án** | PM HTPLDN |
| **Môi trường** | http://103.172.236.130:3000/ |
| **Người test** | QA Automation (Claude Code via MCP Chrome DevTools) |
| **Ngày** | 2026-05-08 09:04:18 (approx — git commit time) |
| **Loại test** | Verification (R7.5.4 BC04 export Excel HD/VV — re-test R6.5.4) |
| **Round** | R7 |
| **Tài liệu tham chiếu** | [verification-test-report-r7-5-4-bc-export.md](../../workflow/bao-cao/verification-test-report-r7-5-4-bc-export.md) · `tasks/todo.md` R7.5.4 · R6 origin: [bug-report-flow-bao-cao.md](../../../round6-2026-05-01-postreset/bug-reports/bug-report-flow-bao-cao.md) |

---

## Tổng hợp

Re-test 2 bug log từ R6.5.4 (BUG-BC-EXPORT-001 + BUG-BC-LEGEND-001). Round 2 đã Closed-verified cả 2 bug gốc. Round 2/R7.7.13 phát hiện thêm BUG-BC-LEGEND-002 cho BC-018 (Minor), sau đó đã Closed-verified R4. Tổng trạng thái hiện tại: 3/3 bug Closed.

### Severity breakdown

| Tổng | Critical | Major | Medium | Minor | Trivial | Closed | Open |
|------|----------|-------|--------|-------|---------|--------|------|
| 3    | 1        | 0     | 0      | 2     | 0       | 3      | 0    |

## Bug Summary Table

| Bug ID | Severity | Priority | Type | TC Ref | **SRS Reference** | Title | Status |
|--------|----------|----------|------|--------|-------------------|-------|--------|
| ~~BUG-BC-EXPORT-001~~ | Critical | P0 | Data | R7.5.4 | `FR-12 Báo cáo §Xuất file` | ~~API `/bao-cao/export` body vẫn JSON wrap NestJS `StreamableFile` — file `.xlsx` tải về không mở được~~ | **Closed (R2)** |
| ~~BUG-BC-LEGEND-001~~ | Minor | P3 | UI/UX | R7.5.4 | `FR-12 Báo cáo §Trình bày kết quả — Biểu đồ` | ~~Pie chart legend hiển thị raw UUID `bbbbbbbb-...000013` cho LV và enum `TRUC_TIEP` cho kênh tiếp nhận~~ | **Closed (R2)** |
| ~~BUG-BC-LEGEND-002~~ | Minor | P3 | UI/UX | BC-018 | `FR-12 Báo cáo §Trình bày kết quả — Biểu đồ` | ~~BC-018 (CP loại DN) bar chart legend leak raw camelCase field names: `chenhLech`, `mucHoTroPhanTram`, `tranChiPhi`, `tranChiPhiMoiHoSo` thay vì label tiếng Việt~~ | **Closed (R4)** |

---

## ~~BUG-BC-EXPORT-001~~ [CLOSED] — API `/bao-cao/export` body JSON wrap, file xlsx tải về không mở được (R7 regression: header đã đúng nhưng body chưa fix → tệ hơn R6)

> **Re-test:** 2026-05-10 12:25:00 R7.7.13-r2 — ✅ PASS (Closed-verified). Login `cb_nv_tw_03` → BC-001 Hỏi đáp PL → click Xuất Excel → POST `/api/v1/bao-cao/export` reqid=288 trả 200 với `content-type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet` + `content-disposition: attachment; filename="bao-cao-hoi-dap-2026-05-10.xlsx"` + body `<binary data>` (KHÔNG còn JSON wrap). `Transfer-Encoding: chunked` → StreamableFile pipe đúng. Verified trong [functional-test-report-r7-7-13-bao-cao.md §3.5.4](../../functional/bao-cao/functional-test-report-r7-7-13-bao-cao.md).


### Mô tả

Click [Xuất Excel] tại trang Báo cáo Thống kê → BE trả `200 OK` với `Content-Type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet` + `Content-Disposition: attachment; filename="bao-cao-*.xlsx"` (R7 đã sửa từ R6 `application/json`), NHƯNG body vẫn là JSON envelope `{"success":true,"data":{"options":{},"logger":{...},"stream":{...}},"meta":null}` chứa Node.js `StreamableFile` đã `JSON.stringify`. Bytes xlsx hợp lệ (`PK\x03\x04` ZIP magic) vẫn nằm trong `data.stream._readableState.buffer[].data` (mảng integer), 27 chunks, total 1910 bytes — nhưng đã bị wrap. Verify trên 2 endpoint khác nhau (BC_HOI_DAP + BC_VU_VIEC_TIEP_NHAN) cho cùng pattern → bug structural toàn module.

### Các bước tái hiện

1. Login `qtht_01` / `Secret@123` / OTP `666666`.
2. Sidebar → "Báo cáo thống kê".
3. Loại báo cáo = `BC Số lượng hỏi đáp/vướng mắc` → Kỳ = `Năm` → app auto-fill `Từ 01/01/2026 — Đến 31/12/2026` → [Xem báo cáo].
4. Bảng + biểu đồ render OK (6 records: Lao động 3, Đất đai 1, SHTT 1, DN 1).
5. Click [Xuất Excel] → Chrome download file `bao-cao-hoi-dap-2026-05-08.xlsx` (7934 bytes).
6. Mở bằng Excel/LibreOffice → "Excel cannot open the file because the file format or file extension is not valid".
7. Inspect: `xxd` 16 byte đầu = `7b 22 73 75 63 63 65 73 73 22 3a 74 72 75 65 2c` (`{"success":true,`) thay vì `50 4B 03 04 ...` (PK ZIP magic).
8. Lặp lại với loại "BC Vụ việc đã tiếp nhận" → cùng pattern (file 7934 bytes, body `{"success":true,...}`).

### Kết quả mong đợi

- Theo `FR-12 Báo cáo §Xuất file`: hệ thống tải về file `.xlsx` mở được trong Excel, sheet ≥1 hàng data thống kê tương ứng filter.
- Body response phải là **binary stream xlsx** (4 byte đầu = `0x50 0x4B 0x03 0x04` ZIP magic), KHÔNG phải JSON.
- Header xlsx mime + Content-Disposition cần đi kèm body binary thật để Chrome / OS handler mở đúng tool.

### Kết quả thực tế

- Header HTTP đã đổi sang `application/vnd.openxmlformats-officedocument.spreadsheetml.sheet; charset=utf-8` (R7 fix một phần).
- Body vẫn là JSON envelope chuẩn của project: `{ success: true, data: { options:{}, logger:{ context:"StreamableFile" }, stream:{ _readableState:{ buffer:[...], ...} } }, meta: null }`.
- Bytes xlsx thật nằm trong `data.stream._readableState.buffer[].data`: chunk[0] = `[80, 75, 3, 4]`, 27 chunks tổng 1910 bytes — đúng signature ZIP nhưng đã bị `JSON.stringify`.
- Excel/LibreOffice mở báo file format invalid.
- **Regression risk:** R6 user còn có header `Content-Type: application/json` để debug; R7 header lừa user là xlsx + extension `.xlsx` → mất dấu hiệu cảnh báo, harder to triage.

### Bằng chứng

**1. Ảnh chụp** (BC HD load thành công, sẵn sàng click [Xuất Excel]):

![BUG-BC-EXPORT-001 — BC HD 6 records, button Xuất Excel enabled](image/r7-5-4-bc-hd-data-loaded.png)

![BUG-BC-EXPORT-001 — BC VV tiếp nhận 5 records, cross-verify cùng pattern bug](image/r7-5-4-bc-vv-tiepnhan-data.png)

**2. API response (corrupt body — JSON thay vì xlsx binary)**:

File raw (rename `.bin` cho dễ inspect):
- BC HD: [r7-5-4-bc-hd-export.network-response](../../workflow/evidence/r7-5-4-bc-hd-export.network-response) — 7934 bytes
- BC VV tiếp nhận: [r7-5-4-bc-vv-tiepnhan-export.network-response](../../workflow/evidence/r7-5-4-bc-vv-tiepnhan-export.network-response) — 7934 bytes

```json
{
  "success": true,
  "data": {
    "options": {},
    "logger": { "context": "StreamableFile", "options": {} },
    "stream": {
      "_readableState": {
        "highWaterMark": 16384,
        "buffer": [
          { "type": "Buffer", "data": [80, 75, 3, 4] },
          { "type": "Buffer", "data": [20, 0] },
          ...  /* 27 chunks total, 1910 xlsx bytes */
        ]
      }
    }
  },
  "meta": null
}
```

Bytes `[80, 75, 3, 4]` (`0x504B0304`) = ZIP magic = đúng signature đầu file `.xlsx`.

**3. Network**:

```
POST /api/v1/bao-cao/export → 200
Request body:
  {"loaiBaoCao":"BC_HOI_DAP","kyBaoCao":"NAM","tuNgay":"2026-01-01","denNgay":"2026-12-31","filterDacThu":{},"formatXuat":"XLSX"}
Response Headers:
  content-type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet; charset=utf-8   ← R7 đã sửa, R6 sai application/json
  content-disposition: attachment; filename="bao-cao-hoi-dap-2026-05-08.xlsx"
  content-length: 7934
Response Body (16 byte đầu hex):
  7b 22 73 75 63 63 65 73 73 22 3a 74 72 75 65 2c   = `{"success":true,`   ← SAI, phải là `50 4B 03 04 ...`
```

---

## ~~BUG-BC-LEGEND-001~~ [CLOSED] — Pie chart legend hiển thị raw enum/UUID thay vì label hiển thị (re-confirm Open R7)

> **Re-test:** 2026-05-10 20:35:00 R7.7.13-r2 — ✅ PASS (Closed-verified). BC-001 HD pháp luật → API trả `theoLinhVuc[].ten = "Lao động"` + chart legend hiển thị tên tiếng Việt đúng ("Lao động: 43.8%", "Doanh nghiệp: 25.0%", "Đất đai: 18.8%", "Sở hữu trí tuệ: 6.3%", "Đầu tư: 6.3%"), KHÔNG còn UUID `bbbbbbbb-...`. Chart kênh tiếp nhận `TRUC_TIEP` không còn xuất hiện trong BC v3.5 (BE response không trả `theoKenhTiepNhan`). FE đã pass `ten` xuống `nameKey` prop.


### Mô tả

Pie chart trong các BC vẫn render legend bằng raw `id`/`enum` thay vì label tiếng Việt. R7 verify trên 2 BC khác nhau:
- BC HD: legend `bbbbbbbb-0000-4000-8000-000000000013` (LV `linh_vuc_pl_id` của Lao động) thay vì "Lao động".
- BC VV tiếp nhận: legend `TRUC_TIEP` (raw enum `kenh_tiep_nhan`) thay vì "Trực tiếp".

Bảng dữ liệu phía dưới biểu đồ hiển thị đúng tên ("Lao động 3", "Trực tiếp 5") → confirm BE trả đủ label, FE chưa pass label xuống chart `nameKey` prop.

### Các bước tái hiện

1. Login `qtht_01`.
2. Sidebar → "Báo cáo thống kê".
3. Loại báo cáo = `BC Số lượng hỏi đáp/vướng mắc` → Kỳ = `Năm` → [Xem báo cáo].
4. Quan sát pie chart phía trên bảng dữ liệu — legend hiển thị 4 entries dạng `bbbbbbbb-0000-4000-8000-00000000001x: NN.N%`.
5. Đổi loại báo cáo = `BC Vụ việc đã tiếp nhận` → [Xem báo cáo] → legend hiển thị `TRUC_TIEP: 100%` thay vì "Trực tiếp".

### Kết quả mong đợi

- Theo `FR-12 §Trình bày kết quả — Biểu đồ`: legend hiển thị **tên** danh mục đúng như cột trong bảng dữ liệu (Lao động, Đất đai, Trực tiếp, ...).

### Kết quả thực tế

- BC HD legend: `bbbbbbbb-...000013: 50.0%` (Lao động 3 record), `bbbbbbbb-...000014: 16.7%`, `bbbbbbbb-...000019: 16.7%`, `bbbbbbbb-...00001a: 16.7%`.
- BC VV tiếp nhận legend: `TRUC_TIEP` (raw enum constant) — bảng dưới hiển thị "Trực tiếp".

### Bằng chứng

![BUG-BC-LEGEND-001 — BC HD legend raw UUID, bảng dưới hiển thị tên LV đúng](image/r7-5-4-bc-hd-data-loaded.png)

![BUG-BC-LEGEND-001 — BC VV tiếp nhận legend raw enum `TRUC_TIEP`, bảng dưới "Trực tiếp"](image/r7-5-4-bc-vv-tiepnhan-data.png)

---

## ~~BUG-BC-LEGEND-002~~ [CLOSED] — BC-018 (CP loại DN) bar chart legend leak raw camelCase field name

> **Re-test:** 2026-05-11 09:35:00 R4 — ✅ PASS (Closed-verified) bộ acc 08. Login `cb_nv_tw_08` → BC-018 (Chi phí theo loại hình DN) → kỳ Năm 2026 → Xem báo cáo. Legend bar chart hiện sạch tiếng Việt: "Chênh lệch / Mức hỗ trợ (%) / Số hồ sơ / Trần / hồ sơ / Trần chi phí / Tổng chi phí" — không còn camelCase. Evidence: [image/bug-bc-legend-002-bc018-fixed-r4.png](image/bug-bc-legend-002-bc018-fixed-r4.png).

### Mô tả

Khi xem BC-018 "BC Chi phí theo loại hình DN" với kỳ Tháng, biểu đồ thanh (bar chart) hiển thị legend bằng tên trường JSON camelCase (`chenhLech`, `mucHoTroPhanTram`, `tranChiPhi`, `tranChiPhiMoiHoSo`) thay vì label tiếng Việt như "Chênh lệch", "Mức hỗ trợ %", "Trần chi phí", "Trần chi phí mỗi hồ sơ". Legend `Số hồ sơ` và `Tổng chi phí` đã đúng tiếng Việt → chỉ một số series bị miss mapping tên hiển thị.

### Các bước tái hiện

1. Login `cb_nv_tw_03` / `Secret@123` / OTP `666666`.
2. Sidebar → "Báo cáo thống kê" → URL `/bao-cao`.
3. Loại báo cáo = `BC Chi phí theo loại hình DN` → Kỳ = `Tháng` → [Xem báo cáo].
4. Quan sát legend trên biểu đồ kết hợp (combined chart): xuất hiện cả label tiếng Việt + raw field name trộn lẫn.

### Kết quả mong đợi

Theo `FR-12 §Trình bày kết quả — Biểu đồ`: legend hiển thị **tên** đầy đủ tiếng Việt cho mọi series — đồng nhất với cột bảng dưới. Bảng dưới biểu đồ đã có cột "Chênh lệch", "Mức hỗ trợ (%)", "Trần chi phí", "Trần chi phí mỗi hồ sơ" → FE phải pass cùng label sang chart `legendName`.

### Kết quả thực tế

Legend chứa:
- ✅ `Số hồ sơ`, `Tổng chi phí` (đúng tiếng Việt)
- ❌ `chenhLech`, `mucHoTroPhanTram`, `tranChiPhi`, `tranChiPhiMoiHoSo` (raw camelCase từ JSON BE response)

API response cho BC-018 trả các field cùng tên camelCase, FE chưa map sang label hiển thị.

### Bằng chứng

![BUG-BC-LEGEND-002 — BC-018 legend leak camelCase field names](image/bug-bc-legend-002-camelcase-bc018.png)

---

## Phụ lục — Môi trường test

| Thành phần | Giá trị |
|------------|---------|
| URL ứng dụng | http://103.172.236.130:3000/ |
| OTP login | `666666` (dev bypass) |
| MailHog (OTP inbox) | http://103.172.236.130:8025 |
| API base | http://103.172.236.130:3000/api/v1 |
| Frontend | React + Vite + Ant Design |
| Xác thực | JWT + OTP (cookie session) |
| Tool test | Chrome DevTools MCP |

---

*Bug report generated: 2026-05-08 | QA Automation via Claude Code*
