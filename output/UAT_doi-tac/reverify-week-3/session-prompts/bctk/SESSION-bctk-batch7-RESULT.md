# Kết quả — BCTK Batch 7 (EXPORT: Xuất Excel/PDF — họ Vụ việc nhóm 1, 8 case)

| Thông tin | Giá trị |
|---|---|
| Ngày verify | 2026-07-21 |
| Env verify | https://18.143.165.120.nip.io (env đối tác log: `htpldn-uat.ospgroup.vn`) |
| Tài khoản verdict | `cbnv_tw_04` (CB Nghiệp vụ TW — phạm vi Toàn quốc) |
| Tool | Chrome DevTools MCP + tools/toast-capture.js (self-check soObserver=1) |
| SRS | `srs-v3.5/srs-fr-11-bao-cao.md` — SCR-IX-01 item 8/9 (dòng 1048–1049), AC dòng 123–124, E6 ERR-RPT-04 (dòng 116), toast item 14 (dòng 1054) |

## Verdict tổng (SAU khi kiểm tra NỘI DUNG file): 4 Reject (Excel) + 4 Open (PDF)

> **Cập nhật 2026-07-21 16:10** — verdict ban đầu 8/8 Reject chỉ dựa trên "file được tạo (200 + binary)". Sau khi **mở & đọc nội dung thực** 8 file (openpyxl + PyMuPDF + render ảnh): bản **Excel đúng chuẩn**, bản **PDF thiếu 3/4 trường header bắt buộc** → 4 case PDF chuyển **Open**. Lỗi ERR-RPT-04 đối tác báo ("không tạo được file") vẫn KHÔNG tái hiện.

| Row | Mã TC | Báo cáo (FR/UC) | Thao tác | Nội dung file thực tế | Verdict |
|---|---|---|---|---|---|
| 191 | SLHDVM_06 | Số lượng hỏi đáp (FR-IX-01/UC124) | Xuất Excel | **200** → xlsx. Header TT17 **ĐỦ 4/4** + data khớp (TM 6/Thuế 4/LĐ 1 = 11) | **Reject** |
| 192 | SLHDVM_07 | Số lượng hỏi đáp (FR-IX-01/UC124) | Xuất PDF | **200** → pdf. Data đúng NHƯNG **thiếu 3/4 header** (kỳ/đơn vị/ngày tạo) | **Open** |
| 196 | VVDTN_06 | VV đã tiếp nhận (FR-IX-02/UC125) | Xuất Excel | **200** → xlsx. Header **ĐỦ** + data khớp (Trực tiếp 14) | **Reject** |
| 197 | VVDTN_07 | VV đã tiếp nhận (FR-IX-02/UC125) | Xuất PDF | **200** → pdf. Data đúng NHƯNG **thiếu 3/4 header** | **Open** |
| 203 | VVDHT_06 | VV đang hỗ trợ (FR-IX-03/UC126) | Xuất Excel | **200** → xlsx. Header **ĐỦ** + data khớp (SLA 7/0/0/0). *Minor: SLA in enum thô* | **Reject** |
| 204 | VVDHT_07 | VV đang hỗ trợ (FR-IX-03/UC126) | Xuất PDF | **200** → pdf. Data đúng NHƯNG **thiếu 3/4 header** + enum SLA thô | **Open** |
| 209 | VVDHTHT_06 | VV đã hoàn thành (FR-IX-04/UC127) | Xuất Excel | **200** → xlsx. Header **ĐỦ** + data khớp (Thương mại 5) | **Reject** |
| 210 | VVDHTHT_07 | VV đã hoàn thành (FR-IX-04/UC127) | Xuất PDF | **200** → pdf. Data đúng NHƯNG **thiếu 3/4 header** | **Open** |

## Kiểm tra nội dung file xuất (2026-07-21 16:10 — bổ sung theo yêu cầu "file xuất ra phải đúng")

**Cách làm:** dump response body 8 request `POST /bao-cao/export` ra đĩa (`reverify-audit/_export-check/`), đọc XLSX bằng openpyxl, đọc PDF bằng PyMuPDF (text-extract) + render ảnh 2x xác nhận trực quan.

**Đối chiếu SRS `srs-fr-11-bao-cao.md:1088`:** *"Export XLSX/PDF chèn tiêu đề BC + thông tin kỳ + đơn vị + ngày tạo vào header file"* (áp dụng CẢ XLSX lẫn PDF).

| Định dạng | Tiêu đề | Kỳ báo cáo | Đơn vị | Ngày tạo | Data body | Kết luận |
|---|:-:|:-:|:-:|:-:|:-:|---|
| **Excel (4 file _06)** | ✅ | ✅ | ✅ | ✅ | ✅ khớp màn hình | ĐÚNG chuẩn |
| **PDF (4 file _07)** | ✅ | ❌ | ❌ | ❌ | ✅ khớp màn hình | **SAI — thiếu 3/4 header** |

- **Excel:** ví dụ SLHDVM có `Kỳ báo cáo: Năm (từ 01/01/2026 đến 31/12/2026)` · `Đơn vị: Toàn quốc` · `Ngày tạo: 21/07/2026`. Tiếng Việt render đúng dấu.
- **PDF:** chỉ có tiêu đề rồi vào bảng ngay. Lặp đồng nhất 4/4 báo cáo → template PDF dùng chung bỏ khối header.
- **Enum SLA (chỉ VVDHT):** file in `BINH_THUONG/SAP_HET/QUA_HAN/QUA_HAN_NGHIEM_TRONG` thay vì nhãn tiếng Việt (web hiển thị "Bình thường") → Minor.

→ **2 bug đã log:** [`bug-reports/bctk/Pass-bug-report-bctk-batch7-export.md`](../../bug-reports/bctk/Pass-bug-report-bctk-batch7-export.md) — BUG-EXPORT-PDF-HEADER (Major) + BUG-EXPORT-SLA-ENUM (Minor).

## Phân tích cụm gốc chung (ERR-RPT-04)
- Giả thuyết "1 bug BE gốc chung endpoint xuất cho mọi báo cáo" (session prompt): endpoint `POST /api/v1/bao-cao/export` **KHÔNG fail tạo file** (không có ERR-RPT-04) trên env `18.143.165.120.nip.io` cho cả 4 báo cáo × 2 định dạng — mỗi lần trả **200** + `content-disposition: attachment` + body file thật + toast "Đang tạo file..." (SRS item 14).
- **NHƯNG** có "gốc chung" thật ở nhánh dựng PDF: mọi báo cáo xuất PDF đều thiếu header bắt buộc (BUG-EXPORT-PDF-HEADER) → 4 case PDF Open. Bản Excel không dính.
- Điều kiện tiên quyết (§SCR item 8/9): đã "Xem báo cáo" ra data trước khi Xuất cho MỌI case (Tổng: SLHDVM 11 · VVDTN 14 · VVDHT 7 · VVDHTHT 5). Không bấm Xuất trên báo cáo rỗng.
- Đối tác test trên env `htpldn-uat.ospgroup.vn` (login admin QTHT) — env khác env được giao. Lỗi có thể thuộc env đối tác tại thời điểm 15/07 (thiếu thư viện tạo file / quyền ghi ổ đĩa / template hỏng ERR-RPT-07) hoặc đã được fix. → Đối tác kiểm tra lại trên bản mới nhất.

## Bug đã log (batch 7)
- [`bug-reports/bctk/Pass-bug-report-bctk-batch7-export.md`](../../bug-reports/bctk/Pass-bug-report-bctk-batch7-export.md): BUG-EXPORT-PDF-HEADER (Major, 4 PDF case) + BUG-EXPORT-SLA-ENUM (Minor, VVDHT).
- File gốc đã dump để đọc nội dung: `reverify-audit/_export-check/*.xlsx` + `*.pdf` (8 file).
- Evidence audit từng case: `reverify-audit/<mã TC>/`. Bảng đối chiếu điều kiện: `cond/<mã TC>.md` (0 GAP về điều kiện tái hiện lỗi đối tác báo).

## Quan sát ngoài tiêu chí BA (không phải bug)
- **Xuất PDF mở hộp thoại "Tùy chọn in báo cáo PDF"** (khổ giấy A4/A3/Letter + hướng Dọc/Ngang) trước khi tải — SRS SCR-IX-01 item 9 (dòng 1049) chỉ ghi "click → auto-download", không mô tả hộp thoại này. Đây là **cải tiến UX** (mặc định A4 + Dọc khớp TT17), kết quả cuối vẫn ra file PDF đúng → KHÔNG phải lỗi, KHÔNG chặn luồng. Ghi nhận để BA biết app thêm bước chọn khổ giấy so với đặc tả.
- Evidence đối tác cho cặp _06 (Excel) và _07 (PDF) của cùng 1 báo cáo là **cùng 1 ảnh** (VVDTN/VVDHT/VVDHTHT: 2 file jpg trùng dung lượng byte) — đối tác dùng chung 1 screenshot lỗi xuất cho cả 2 định dạng.
