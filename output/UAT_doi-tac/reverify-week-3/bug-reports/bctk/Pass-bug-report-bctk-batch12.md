# Bug Report — Báo cáo Thống kê (BCTK Batch 12 — EXPORT họ Chương trình HTPLDN)

| Thông tin | Giá trị |
|-----------|---------|
| **Dự án** | PM Hỗ trợ pháp lý doanh nghiệp (HTPLDN) |
| **Môi trường** | https://18.143.165.120.nip.io |
| **Người test** | QA (Chrome DevTools MCP + đọc nội dung file: openpyxl / PyMuPDF) |
| **Ngày** | 2026-07-23 09:55:00 |
| **Loại test** | UAT reverify tuần 3 (R1) — Functional / Export content |
| **Round** | Reverify tuần 3 — batch BCTK-12 (EXPORT họ Chương trình) |
| **Tài liệu tham chiếu** | `srs-v3.5/srs-fr-11-bao-cao.md` (§Quy tắc tương tác dòng 1088; SCR-IX-01 item 8/9 dòng 1048–1049; AC dòng 124) |
| **Tài khoản verdict** | `cbnv_tw_03` (CB Nghiệp vụ - Trung ương, phạm vi Toàn quốc) |

---

## Tổng hợp

> **R1 reverify tuần 3 (2026-07-23 09:55) — ✅ PASS / CLOSED.** Dev đã bổ sung khối header vào template PDF dùng chung. Chạy lại đủ luồng **Xuất PDF** cho cả **3 loại báo cáo** họ Chương trình batch 12 (`cbnv_tw_05`, kỳ Năm 2026, Toàn quốc): CTTDVQL_05 / CTTLV_06 / CTTTG_05. Mọi file PDF nay có đủ 4 trường header (tiêu đề + Kỳ báo cáo + Đơn vị + Ngày tạo) như bản Excel. 3/3 `POST /bao-cao/export` trả **200**, không ERR-RPT-04. Đọc nội dung file thực (PyMuPDF text-extract + render ảnh), không kết luận tĩnh.

Bối cảnh gốc (vòng 1, 2026-07-21, `cbnv_tw_03`): lỗi đối tác báo ERR-RPT-04 *"Không thể tạo file xuất. Vui lòng thử lại."* KHÔNG tái hiện; bản Excel đủ 4/4 header (tiêu đề + Kỳ báo cáo + Đơn vị + Ngày tạo) → Reject; bản PDF thiếu 3/4 trường header (Kỳ báo cáo / Đơn vị / Ngày tạo) → log BUG-EXPORT-PDF-HEADER (Major). Cùng template PDF dùng chung với batch 7/8 (7 loại BC khác) → lỗi hệ thống module Báo cáo thống kê (SCR-IX-01), không phải lỗi cục bộ 1 báo cáo. Nay đã fix.

### Severity breakdown

| Tổng | Critical | Major | Medium | Minor | Trivial | Closed | Open |
|------|----------|-------|--------|-------|---------|--------|------|
| 1    | 0        | 1     | 0      | 0     | 0       | 1      | 0    |

## Bug Summary Table

| Bug ID | Severity | Priority | Type | TC Ref | **SRS Reference** | Title | Status |
|--------|----------|----------|------|--------|-------------------|-------|--------|
| BUG-EXPORT-PDF-HEADER | Major | P1 | UI/UX | **Batch12:** CTTDVQL_05 (row 269), CTTLV_06 (row 274), CTTTG_05 (row 276) — họ Chương trình. Cùng bug batch 7/8 (7 loại BC khác) | `srs-fr-11-bao-cao.md:1088` (§Quy tắc tương tác) | File PDF xuất ra thiếu header bắt buộc (Kỳ báo cáo / Đơn vị / Ngày tạo) — bản Excel có đủ | Closed |

---

## ~~BUG-EXPORT-PDF-HEADER~~ [CLOSED] — File PDF xuất ra thiếu header bắt buộc (Kỳ báo cáo / Đơn vị / Ngày tạo)

> **Re-test:** 2026-07-23 09:55:00 R1 — ✅ PASS (Closed-verified). Chạy lại đủ luồng Xuất PDF cho cả 3 loại BC họ Chương trình (CTTDVQL_05 / CTTLV_06 / CTTTG_05) bằng `cbnv_tw_05`, kỳ Năm 2026, Toàn quốc. Đọc nội dung file thực (PyMuPDF): mọi PDF nay đủ 4 trường header — tiêu đề + `Kỳ báo cáo: Năm (từ 01/01/2026 đến 31/12/2026)` + `Đơn vị: Toàn quốc` + `Ngày tạo: 23/07/2026` (dòng header phạm vi tách biệt với cột "Đơn vị"/"Kỳ" của bảng số liệu). 3/3 `POST /bao-cao/export` trả 200, không ERR-RPT-04. Bằng chứng: [CTTDVQL](image/BUG-EXPORT-PDF-HEADER-CTTDVQL-reverify-pass.png) · [CTTLV](image/BUG-EXPORT-PDF-HEADER-CTTLV-reverify-pass.png) · [CTTTG](image/BUG-EXPORT-PDF-HEADER-CTTTG-reverify-pass.png).

### Mô tả

Khi xuất báo cáo họ **Chương trình HTPLDN** ra **PDF**, file tạo ra chỉ có **tiêu đề báo cáo** rồi nhảy thẳng vào bảng số liệu. Thiếu **3/4 trường header bắt buộc** mà SRS yêu cầu: **thông tin kỳ báo cáo, đơn vị, ngày tạo**. Cùng dữ liệu đó, bản **Excel (XLSX) xuất ra ĐỦ cả 4 trường** — chứng minh back-end có sẵn dữ liệu header và đây là lỗi riêng của luồng dựng file PDF (template PDF bỏ khối header). Lỗi này lặp lại đồng nhất với BUG-EXPORT-PDF-HEADER đã phát hiện ở batch 7/8 trên 7 loại báo cáo khác → lỗi hệ thống của template PDF dùng chung cho toàn module Báo cáo thống kê (SCR-IX-01).

### Các bước tái hiện

1. Đăng nhập role **CB Nghiệp vụ - Trung ương** (`cbnv_tw_03` / `Test@1234`) — quyền xem báo cáo thống kê phạm vi Toàn quốc theo SCR-IX-01.
2. (Tiền đề) Đã có ≥1 chương trình HTPLDN đã duyệt trong kỳ (báo cáo CT chỉ đếm CT ≥ Đã duyệt).
3. Vào **Báo cáo thống kê** → chọn loại **BC Chương trình theo đơn vị** → Kỳ **Năm** (01/01/2026 – 31/12/2026) → Đơn vị **Toàn quốc** → **Xem báo cáo** (báo cáo có data: Tổng CT 4, ngân sách 300.000.000).
4. Bấm **Xuất PDF** → hộp thoại "Tùy chọn in báo cáo PDF" (A4, Dọc) → **Xuất file** → `POST /api/v1/bao-cao/export` trả **200**, tải về `bao-cao-ct-theo-don-vi-2026-07-21.pdf`.
5. Mở file PDF: chỉ có tiêu đề "BC CHƯƠNG TRÌNH THEO ĐƠN VỊ" + bảng số liệu. **Không có** dòng Kỳ báo cáo / Đơn vị / Ngày tạo.
6. So sánh: xuất cùng báo cáo ra **Excel** → file XLSX có đủ 4 dòng header (tiêu đề + `Kỳ báo cáo: Năm (từ 01/01/2026 đến 31/12/2026)` + `Đơn vị: Toàn quốc` + `Ngày tạo: 21/07/2026`).

### Kết quả mong đợi

- Theo SRS v3.5 `srs-fr-11-bao-cao.md:1088` (§Quy tắc tương tác): *"Export XLSX/PDF chèn tiêu đề BC + thông tin kỳ + đơn vị + ngày tạo vào header file"* — quy tắc áp dụng cho **cả XLSX lẫn PDF**.
- File PDF xuất ra phải có ở phần đầu: tiêu đề báo cáo + kỳ báo cáo + đơn vị + ngày tạo (như bản Excel).

### Kết quả thực tế

- File PDF chỉ có tiêu đề báo cáo + bảng số liệu; **thiếu 3 trường**: Kỳ báo cáo, Đơn vị, Ngày tạo.
- Trích text thực từ file PDF (`bao-cao-ct-theo-don-vi-2026-07-21.pdf`, PyMuPDF): `BC CHƯƠNG TRÌNH THEO ĐƠN VỊ` → `Đơn vị` → `Cấp đơn vị` → `Số chương trình` → `Tổng ngân sách (₫)` → `Cục Bổ trợ tư pháp - Bộ Tư pháp` → `TW` → `4` → `300.000.000`. Không có chuỗi "Kỳ báo cáo" / "Đơn vị:" / "Ngày tạo".
- PDF trang A4 dọc (595.28×841.89pt), font Tinos-Bold/Regular (Times New Roman-tương thích) — 2 yêu cầu định dạng SRS đạt; chỉ thiếu khối header.
- Bản Excel cùng báo cáo (đối chứng) có đủ: `BC Chương trình theo đơn vị` · `Kỳ báo cáo: Năm (từ 01/01/2026 đến 31/12/2026)` · `Đơn vị: Toàn quốc` · `Ngày tạo: 21/07/2026`.

### Bằng chứng

![BUG-EXPORT-PDF-HEADER — PDF BC Chương trình theo đơn vị: chỉ có tiêu đề rồi vào thẳng bảng (Đơn vị/Cấp đơn vị/Số CT/Tổng ngân sách), thiếu Kỳ báo cáo/Đơn vị/Ngày tạo — verify cbnv_tw_03, Năm 2026, Toàn quốc](image/BUG-EXPORT-PDF-HEADER-CTTDVQL-pdf-no-header.png)

![BUG-EXPORT-PDF-HEADER — tái hiện trên PDF BC Chương trình theo lĩnh vực (CTTLV_06): chỉ có tiêu đề "BC CHƯƠNG TRÌNH THEO LĨNH VỰC" rồi vào thẳng bảng (Lĩnh vực PL/Số CT/Số DN tham gia), thiếu Kỳ báo cáo/Đơn vị/Ngày tạo — verify cbnv_tw_03, Năm 2026, Toàn quốc](image/BUG-EXPORT-PDF-HEADER-CTTLV-pdf-no-header.png)

![BUG-EXPORT-PDF-HEADER — tái hiện trên PDF BC Chương trình theo thời gian (CTTTG_05): chỉ có tiêu đề "BC CHƯƠNG TRÌNH THEO THỜI GIAN" rồi vào thẳng bảng (Kỳ/Từ ngày/Đến ngày/Số CT/Số DN/Tổng ngân sách), thiếu Kỳ báo cáo/Đơn vị/Ngày tạo — verify cbnv_tw_03, Năm 2026, Toàn quốc](image/BUG-EXPORT-PDF-HEADER-CTTTG-pdf-no-header.png)

**Request/response** (giống nhau cho mọi loại báo cáo, chỉ khác `loaiBaoCao`):

```json
// Request (BC_CT_THEO_DON_VI)
{"loaiBaoCao":"BC_CT_THEO_DON_VI","kyBaoCao":"NAM","tuNgay":"2026-01-01","denNgay":"2026-12-31","formatXuat":"PDF","khoGiay":"A4","huongGiay":"portrait"}
// Response: 200, content-type: application/pdf, content-disposition: attachment; filename="bao-cao-ct-theo-don-vi-2026-07-21.pdf"
// → file PDF tạo được nhưng nội dung thiếu khối header (Kỳ/Đơn vị/Ngày tạo)
```

---

## Phụ lục — Môi trường test

| Thành phần | Giá trị |
|------------|---------|
| URL ứng dụng | https://18.143.165.120.nip.io |
| OTP login | MailHog `http://18.143.165.120:8025` |
| API base | https://18.143.165.120.nip.io/api/v1 |
| Frontend | React + Ant Design |
| Tool test | Chrome DevTools MCP; đọc file: openpyxl 3.1.5 / PyMuPDF 1.26.5 (render + text-extract) |
| Tài khoản verdict | `cbnv_tw_03` (CB Nghiệp vụ - Trung ương, phạm vi Toàn quốc) |
| File gốc đã dump | `reverify-audit/_export-check-bctk12/*.xlsx` · `*.pdf` (từ response body của `POST /bao-cao/export`) |

---

*Bug report generated: 2026-07-21 17:20:00 | QA via Claude Code*
