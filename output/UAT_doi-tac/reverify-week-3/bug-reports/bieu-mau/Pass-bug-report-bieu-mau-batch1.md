# Bug Report — Biểu mẫu (Batch 1 · QLTMBMHD — Quản lý thư mục biểu mẫu)

| Thông tin | Giá trị |
|-----------|---------|
| **Dự án** | PM HTPLDN — Verify bug đối tác (UAT tuần 3) |
| **Môi trường** | https://18.143.165.120.nip.io/ |
| **Người test** | QA Automation (Claude Code) |
| **Ngày** | 2026-07-22 23:38:26 |
| **Loại test** | Functional (verify bug đối tác vòng 1) |
| **Round** | Reverify week-3 — Batch 1 |
| **Tài liệu tham chiếu** | `srs-v3.5/srs-fr-09-bieu-mau.md` (FR-VII-01 / SCR-VII-01) |

---

## Tổng hợp

Phát hiện **4** lỗi có SRS reference cụ thể trong quá trình verify Batch 1 (QLTMBMHD, rows 80–87): 3 lỗi trong phạm vi 8 case đối tác (BUG-QLTMBMHD_13 / _19 / _23) + **1 lỗi** thuộc case `QLTMBMHD_OOS_01` (sheet row 302, phát hiện khi verify QLTMBMHD_07) — `BUG-QLTMBMHD_OOS_01`.

> **R2 reverify 2026-07-22 (snapshot LATEST):** Dev báo fix xong 4/4 bug (dev done batch) → re-verify qua Chrome DevTools MCP với `cbnv_tw` (BTP·TW): **4/4 PASS → tất cả Closed, Open còn 0**. _13 (nút Xóa đúng điều kiện Nháp/Ẩn+rỗng) · _19 (thanh chọn + nút bulk reset sau xóa hàng loạt) · _23 (Excel có cột tên "Lĩnh vực" đọc được, bỏ UUID) · _OOS_01 (toast trùng tên chèn tên thư mục cụ thể theo ERR-TM-01).

> Các case khác: QLTMBMHD_07 → Reject (thông báo trùng tên không nhân đôi); QLTMBMHD_08 / _10 / _17 → BA confirm (`../../ba-confirm/bieu-mau/ba-confirmation-needed-week-3-bieu-mau-batch1.md`). QLTMBMHD_20 → Open (bug bên dưới) **kèm** BA confirm (wording thông báo xóa một phần).

### Severity breakdown

| Tổng | Critical | Major | Medium | Minor | Trivial | Closed | Open |
|------|----------|-------|--------|-------|---------|--------|------|
| 4    | 0        | 0     | 3      | 1     | 0       | 4      | 0    |

## Bug Summary Table

| Bug ID | Severity | Priority | Type | TC Ref | **SRS Reference** | Title | Status |
|--------|----------|----------|------|--------|-------------------|-------|--------|
| ~~BUG-QLTMBMHD_13~~ | Medium | P2 | UI/UX | QLTMBMHD_13 | `SCR-VII-01 #13` (`srs-fr-09:615`) | Nút "Xóa" hiển thị sai điều kiện — hiện trên thư mục Công khai và thư mục còn biểu mẫu | **Closed** ✅ |
| ~~BUG-QLTMBMHD_19~~ | Medium | P2 | UI/UX | QLTMBMHD_19, QLTMBMHD_20 | `SCR-VII-01 #14` (`srs-fr-09:616`) | Sau khi xóa hàng loạt thành công, thanh "Đã chọn N thư mục" + nút hành động hàng loạt không tự xóa (count cũ) | **Closed** ✅ |
| ~~BUG-QLTMBMHD_23~~ | Medium | P2 | Data | QLTMBMHD_23 | `SCR-VII-01 Outputs #3 ten_linh_vuc` (`srs-fr-09:120`) | File Excel xuất ra không có cột tên Lĩnh vực — chỉ có "Lĩnh vực ID" (UUID) | **Closed** ✅ |
| ~~BUG-QLTMBMHD_OOS_01~~ | Minor | P3 | UI/Content | QLTMBMHD_OOS_01 | `ERR-TM-01` (`srs-fr-09:130`) | Thông báo lỗi trùng tên không chèn tên thư mục cụ thể `{tên}` theo mẫu ERR-TM-01 | **Closed** ✅ |

---

## ~~BUG-QLTMBMHD_13~~ [CLOSED] — Nút "Xóa" hiển thị trên thư mục Công khai và thư mục còn biểu mẫu (sai điều kiện SCR-VII-01)

> **Re-test:** 2026-07-22 23:28:16 R2 — ✅ PASS (Closed-verified). Soi DOM 4 thư mục: nút Xóa CHỈ hiện trên "BM-B3-0720-Rong-1" (Nháp + 0 biểu mẫu). Hai thư mục vi phạm gốc đều đã ẩn Xóa: "Thư mục biểu mẫu seed" (Đã công khai, 3 BM) + "QA Hidden Folder 715" (Đã ẩn, còn 1 BM). Khớp SCR-VII-01: Xóa chỉ khi trạng thái Nháp/Ẩn VÀ rỗng.

### Mô tả

Trên màn Quản lý thư mục biểu mẫu, nút hành động **Xóa** hiển thị trên MỌI hàng thư mục bất kể trạng thái và độ rỗng. Theo SRS SCR-VII-01, nút Xóa chỉ được hiển thị khi thư mục ở trạng thái Nháp/Ẩn VÀ rỗng (0 biểu mẫu). Thực tế nút Xóa xuất hiện cả trên thư mục **Đã công khai** và thư mục **còn biểu mẫu bên trong**.

### Các bước tái hiện

1. Đăng nhập role **CB Nghiệp vụ - Trung ương** (`cbnv_tw`, quyền quản lý thư mục biểu mẫu theo SCR-VII-01, đơn vị BTP·TW).
2. Vào **Biểu mẫu → Thư viện biểu mẫu** (`/bieu-mau/thu-muc`), tab **Tất cả**.
3. Quan sát cột **Hành động** trên hàng "Thư mục biểu mẫu seed" (Đã công khai, 1 biểu mẫu) và "QA Hidden Folder 715" (Nháp, 1 biểu mẫu).
4. Quan sát: nút **Xóa** hiển thị trên cả hai hàng.

### Kết quả mong đợi

- Theo SRS `srs-fr-09-bieu-mau.md:615` (SCR-VII-01 #13 — "... / Xóa (khi NHAP/AN, rỗng)"): nút Xóa chỉ hiển thị khi thư mục ở trạng thái Nháp hoặc Ẩn VÀ rỗng (0 biểu mẫu).
- Trên thư mục Đã công khai, hoặc thư mục còn biểu mẫu → nút Xóa không được hiển thị.

### Kết quả thực tế

- Nút **Xóa** hiển thị trên hàng "Thư mục biểu mẫu seed" (Đã công khai) — vi phạm điều kiện trạng thái.
- Nút **Xóa** hiển thị trên hàng "QA Hidden Folder 715" (Nháp, còn 1 biểu mẫu) — vi phạm điều kiện rỗng.

### Bằng chứng

![BUG-QLTMBMHD_13 — nút Xóa trên thư mục Đã công khai và thư mục Nháp còn biểu mẫu](image/BUG-QLTMBMHD_13-xoa-tren-congkhai.png)

```json
[{"Tên":"Thư mục biểu mẫu seed","Trạng thái":"Đã công khai","Số biểu mẫu":"1","actions":["Ẩn","Sửa","Xóa"]},
 {"Tên":"QA Hidden Folder 715","Trạng thái":"Nháp","Số biểu mẫu":"1","actions":["Công khai","Sửa","Xóa"]}]
```

---

## ~~BUG-QLTMBMHD_19~~ [CLOSED] — Sau khi xóa hàng loạt thành công, thanh "Đã chọn N thư mục" + nút hành động hàng loạt không tự xóa

> **Re-test:** 2026-07-22 23:33:51 R2 — ✅ PASS (Closed-verified). Tạo 2 thư mục Nháp rỗng → tích chọn 2 → Xóa hàng loạt → xác nhận. Sau khi toast "Đã xóa 2 thư mục." (2 DELETE 204): soi DOM thanh "Đã chọn N thư mục" biến mất hẳn, 0 nút bulk, 0 checkbox tích, Select all reset, còn 4 thư mục. Phần "xóa một phần" (QLTMBMHD_20) vẫn thuộc BA confirm (sheet row 86, ngoài batch dev-done này).

### Mô tả

Sau khi xóa hàng loạt thành công, hệ thống KHÔNG reset trạng thái chọn: thanh "Đã chọn N thư mục" vẫn hiển thị với **số đếm CŨ** (số thư mục đã chọn trước khi xóa, nay đã bị xóa), kèm các nút [Công khai hàng loạt] [Ẩn hàng loạt] [Xóa hàng loạt] [Bỏ chọn]. Xảy ra cả khi xóa toàn bộ (QLTMBMHD_19) lẫn xóa một phần (QLTMBMHD_20).

### Các bước tái hiện

1. Đăng nhập role **CB Nghiệp vụ - Trung ương** (`cbnv_tw`, BTP·TW).
2. Vào **Biểu mẫu → Thư viện biểu mẫu**, tab Tất cả.
3. Tích chọn 2 thư mục Nháp rỗng ("BM-B1-0720 DelA", "BM-B1-0720 Trung") → bấm **Xóa hàng loạt** → xác nhận **Xóa**.
4. Sau khi thông báo "Đã xóa 2 thư mục." hiện + danh sách còn lại cập nhật (2 thư mục kia biến mất).
5. Quan sát thanh chọn phía trên bảng.

### Kết quả mong đợi

- Theo SRS `srs-fr-09-bieu-mau.md:616` (SCR-VII-01 #14 — Hành động hàng loạt: điều kiện hiển thị **"khi chọn nhiều"**): sau khi xóa xong, không còn thư mục nào được chọn → thanh "Đã chọn N thư mục" và các nút hành động hàng loạt phải tự ẩn / reset về 0.

### Kết quả thực tế

- Thanh **"Đã chọn 2 thư mục"** vẫn hiển thị sau khi xóa xong, với số đếm **2 (cũ, đã stale)** — trong khi thực tế 0 dòng còn được tích (`checkboxesStillChecked=0`).
- Các nút [Công khai hàng loạt] [Ẩn hàng loạt] [Xóa hàng loạt] [Bỏ chọn] vẫn hiển thị.
- Ở luồng xóa một phần (QLTMBMHD_20): thanh vẫn hiện "Đã chọn 2 thư mục" và thư mục bị bỏ qua ("QA Hidden Folder 715") vẫn ở trạng thái tích chọn (`checkboxesStillChecked=1`).

### Bằng chứng

![BUG-QLTMBMHD_19 — "Tất cả 2" (đã xóa 2 thư mục) nhưng thanh "Đã chọn 2 thư mục" + nút vẫn hiện, các dòng còn lại KHÔNG tích](image/BUG-QLTMBMHD_19-selection-not-cleared.png)

```
Xóa hàng loạt 2 thư mục Nháp rỗng:
  toast: "Đã xóa 2 thư mục." (1 khung, không nhân đôi, 2 DELETE request = 2 thư mục)
  post-state: selectionBar="Đã chọn 2 thư mục" (STALE), bulkButtons=hiện, checkboxesChecked=0, remainingRows=2
```

---

## ~~BUG-QLTMBMHD_23~~ [CLOSED] — File Excel xuất ra không có cột tên Lĩnh vực (chỉ có "Lĩnh vực ID" chứa UUID)

> **Re-test:** 2026-07-22 23:35:44 R2 — ✅ PASS (Closed-verified). Bấm "Xuất Excel" trên UI → mở file bằng openpyxl: header cột D nay là **"Lĩnh vực"** (bỏ "ID"), dữ liệu đọc được **Thuế / Lao động / Thương mại / Thương mại** — không còn UUID. Khớp cột Lĩnh vực trên UI + SCR-VII-01 Outputs #3 `ten_linh_vuc`. File: `reverify-audit/QLTMBMHD_23/export-thu-muc-reverify-R2.xlsx`.

### Mô tả

Chức năng "Xuất Excel" trên màn Quản lý thư mục biểu mẫu xuất file XLSX có cột **"Lĩnh vực ID"** chứa mã định danh UUID (vd `bbbbbbbb-0000-4000-8000-00000000001c`), KHÔNG có cột tên lĩnh vực đọc được (vd "Thương mại"). Trên UI danh sách, cột "Lĩnh vực" hiển thị tên ("Thương mại"), nhưng file xuất ra thay tên bằng UUID → người dùng không đọc được lĩnh vực.

### Các bước tái hiện

1. Đăng nhập role **CB Nghiệp vụ - Trung ương** (`cbnv_tw`, BTP·TW).
2. Vào **Biểu mẫu → Thư viện biểu mẫu**.
3. Bấm nút **Xuất Excel** (POST `/api/v1/thu-muc-bieu-maus/export`) → tải file `thu-muc-bieu-mau-*.xlsx`.
4. Mở file, xem hàng tiêu đề + dữ liệu cột lĩnh vực.

### Kết quả mong đợi

- Theo SRS `srs-fr-09-bieu-mau.md:120` (SCR-VII-01 Outputs #3 — `ten_linh_vuc | text`): danh sách thư mục có trường **tên lĩnh vực** (hiển thị "Thương mại" trên UI).
- File Excel xuất ra phải có cột **tên Lĩnh vực đọc được** (như cột hiển thị trên UI).

### Kết quả thực tế

- Hàng tiêu đề file: `STT | Tên thư mục | Mô tả | Lĩnh vực ID | Thứ tự | Trạng thái | Ngày tạo | Ngày cập nhật`.
- Cột "Lĩnh vực ID" chứa **UUID** (`bbbbbbbb-0000-4000-8000-00000000001c`), KHÔNG có cột tên lĩnh vực ("Thương mại").

### Bằng chứng

![BUG-QLTMBMHD_23 — hàng tiêu đề Excel: cột "Lĩnh vực ID" chứa UUID, không có cột tên Lĩnh vực](image/BUG-QLTMBMHD_23-excel-thieu-linhvuc.png)

*(File gốc: `reverify-audit/QLTMBMHD_23/export-thu-muc.xlsx`)*

```
Header: ('STT','Tên thư mục','Mô tả','Lĩnh vực ID','Thứ tự','Trạng thái','Ngày tạo','Ngày cập nhật')
Row1  : (1,'QA Hidden Folder 715','QA seed...','bbbbbbbb-0000-4000-8000-00000000001c',0,'Nháp',...)
```

---

## ~~BUG-QLTMBMHD_OOS_01~~ [CLOSED] — Thông báo lỗi trùng tên không chèn tên thư mục cụ thể theo mẫu ERR-TM-01

> **Re-test:** 2026-07-22 23:38:26 R2 — ✅ PASS (Closed-verified). Thêm thư mục tên trùng "BM-B3-0720-Rong-1" (đã tồn tại, BTP·TW) → toast nay là **"Thư mục 'BM-B3-0720-Rong-1' đã tồn tại trong đơn vị"** — đã chèn tên thư mục cụ thể trong dấu nháy, khớp mẫu ERR-TM-01. Trước đây là "Tên thư mục đã tồn tại trong đơn vị" (không có tên). Bằng chứng: `image/BUG-QLTMBMHD_OOS_01-reverify-pass.png`.

> **Ghi chú phạm vi:** phát hiện tình cờ khi verify QLTMBMHD_07 (case thông báo trùng tên nhân đôi), sau đó được tách thành case riêng `QLTMBMHD_OOS_01` (sheet row 302). Log theo quy tắc "bug ngoài phạm vi cũng log".

### Mô tả

Khi tạo thư mục với tên trùng thư mục đã có trong đơn vị, hệ thống hiển thị thông báo lỗi **"Tên thư mục đã tồn tại trong đơn vị"** — thông báo chung, KHÔNG chèn tên thư mục cụ thể bị trùng. Theo SRS ERR-TM-01, thông báo phải nêu đúng tên thư mục bị trùng (`{tên}`), giúp người dùng biết chính xác tên nào xung đột.

### Các bước tái hiện

1. Đăng nhập role **CB Nghiệp vụ - Trung ương** (`cbnv_tw`, BTP·TW).
2. Vào **Biểu mẫu → Thư viện biểu mẫu** → **+ Thêm thư mục**.
3. Nhập tên trùng một thư mục đã tồn tại (vd "BM-B1-0720 Trung") → **Lưu**.
4. Quan sát thông báo lỗi.

### Kết quả mong đợi

- Theo SRS `srs-fr-09-bieu-mau.md:130` (ERR-TM-01): thông báo báo đúng tên thư mục bị trùng — **"Thư mục '{tên}' đã tồn tại trong đơn vị"** (chèn tên cụ thể).

### Kết quả thực tế

- App hiển thị **"Tên thư mục đã tồn tại trong đơn vị"** — không chèn tên thư mục cụ thể, đổi mẫu "Thư mục '{tên}'" → "Tên thư mục".
- Đo bằng `tools/toast-capture.js` 2 lần độc lập: mỗi lần 1 khung thông báo / 1 request, `BI_LAP=false`, `innerText` nhất quán → nội dung wording ổn định (không phải lỗi render ngẫu nhiên).

### Bằng chứng

![BUG-QLTMBMHD_OOS_01 — app hiển thị "Tên thư mục đã tồn tại trong đơn vị" vs SRS ERR-TM-01 "Thư mục '{tên}' đã tồn tại trong đơn vị"](image/BUG-QLTMBMHD_OOS_01-trungten-thieu-ten.png)

*(Đo chi tiết: `reverify-audit/QLTMBMHD_07/toast-measurement.md` — mục "Ghi chú phụ (ngoài tiêu chí case — wording)")*

---

## Phụ lục — Môi trường test

| Thành phần | Giá trị |
|------------|---------|
| URL ứng dụng | https://18.143.165.120.nip.io/ |
| OTP login | MailHog `http://18.143.165.120:8025/` |
| Tài khoản | `cbnv_tw` / Test@1234 (CB Nghiệp vụ - TW, BTP·TW) |
| Frontend | React + Ant Design v5 |
| Tool test | Chrome DevTools MCP |

---

*Bug report generated: 2026-07-20 20:45:00 | QA Automation via Claude Code*
