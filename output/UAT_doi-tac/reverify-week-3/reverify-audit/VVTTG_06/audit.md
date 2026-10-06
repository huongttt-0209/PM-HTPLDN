# Audit — VVTTG_06 (row 217) — Xuất PDF BC Vụ việc theo thời gian — Verdict: Open (BUG-EXPORT-PDF-HEADER)

> **Cập nhật 21/07/2026:** verdict đổi từ Reject → **Open** sau khi kiểm tra NỘI DUNG file PDF tải về (không chỉ xác nhận file được tạo). Lỗi ERR-RPT-04 đối tác báo vẫn KHÔNG tái hiện, nhưng file PDF thiếu header bắt buộc → tái hiện BUG-EXPORT-PDF-HEADER (đã log ở `bug-reports/bctk/Pass-bug-report-bctk-batch7-export.md`). Xem mục "Kiểm tra nội dung file xuất".

## Cổng 1 — Bằng chứng đối tác (đã mở full-res)
- File: `partner-evidence/VVTTG_06.jpg` (233 KB).
- 3 dữ kiện neo:
  - (a) URL/ID: `htpldn-uat.ospgroup.vn/bao-cao?loai=...&kyBaoCao=NAM&tuNgay=2026-01-01&denNgay=2026-12-31&donViId=00000000-0000-4000-8000-0000000...` (env đối tác).
  - (b) Trạng thái: báo cáo ĐÃ Xem ra data (KPI "Tổng vụ việc toàn kỳ = 1"); toast đỏ **"Không thể tạo file xuất. Vui lòng thử lại."**. Vai trò = Quản trị viên (QTHT).
  - (c) Tiền đề: BC Vụ việc theo thời gian; Kỳ = Năm 2026; Đơn vị = Cục Bổ trợ tư pháp - Bộ Tư pháp (BTP-TW).

## Cổng 2 — Hiểu bug
- Evidence đã xem: VVTTG_06.jpg, frame chứa lỗi = toast "Không thể tạo file xuất. Vui lòng thử lại." sau khi bấm Xuất PDF trên báo cáo đã có data.
- Đối tác phản ánh cụ thể: bấm **Xuất PDF** → hệ thống báo lỗi tạo file (ERR-RPT-04), tệp PDF KHÔNG được tải về.
- Data + bước tái hiện: Login → Báo cáo thống kê → BC Vụ việc theo thời gian → Kỳ Năm 2026 → Xem báo cáo (ra data) → Xuất PDF.

## Cổng 3 — Đối chiếu SRS vs thực tế web
- SRS `srs-v3.5/srs-fr-11-bao-cao.md:1049` (SCR-IX-01 item 9): Nút "Xuất PDF (.pdf)" — điều kiện "Sau khi đã Xem báo cáo" — hành vi "click → auto-download".
- AC `:124`: "Given CB nhấn Xuất PDF When click Then tải file .pdf theo format TT17/2025".
- E6 `:116` ERR-RPT-04 = message đối tác báo.
- Thực tế web QA: nút Xuất PDF bật đúng sau Xem báo cáo; bấm → dialog chọn khổ giấy/hướng → Xuất file → tải file .pdf thành công, KHÔNG có ERR-RPT-04 → đúng SCR item 9 + AC dòng 124.

## Verify — 2 phương pháp (env `18.143.165.120.nip.io`, account `cbnv_tw_05`)
1. **UI:** đã Xem báo cáo (BC Vụ việc theo thời gian, Năm 2026, đơn vị BTP-TW, data = 3). Bấm Xuất PDF → mở dialog "Tùy chọn in báo cáo PDF" (khổ A4/A3/Letter, hướng Dọc/Ngang) → chọn A4/Dọc → "Xuất file" → toast "Đang tạo file..."; KHÔNG có toast lỗi. Ảnh: `VVTTG_06-web-export-pdf.png`.
2. **Network:** `POST /api/v1/bao-cao/export` reqid=112: body `{...,"donViId":"00000000-0000-4000-8000-000000000001","formatXuat":"PDF","khoGiay":"A4","huongGiay":"portrait"}` → **200**, `content-type: application/pdf`, `content-disposition: attachment; filename="bao-cao-vu-viec-theo-thoi-gian-2026-07-21.pdf"`, body = binary.

## Kiểm tra nội dung file xuất (bổ sung 21/07/2026)
- Tải file PDF thật về qua fetch (`POST /api/v1/bao-cao/export`, formatXuat=PDF, A4/portrait) rồi mở đọc bằng PyMuPDF (text + toạ độ + page size + font).
- **Khổ giấy:** A4 (210×297mm) ✅. **Font:** Tinos-Regular/Bold — bản metric-tương thích Times New Roman, body cỡ 13 ✅.
- **Số liệu:** đúng (khớp bảng trên màn hình).
- **Header file:** ❌ file PDF **chỉ có tiêu đề "BC VỤ VIỆC THEO THỜI GIAN" rồi vào thẳng bảng** — THIẾU 3/4 trường header bắt buộc: **Kỳ báo cáo / Đơn vị / Ngày tạo**. Bản Excel cùng báo cáo có đủ 4 trường (đối chứng).
- SRS `srs-v3.5/srs-fr-11-bao-cao.md:1088` (§Quy tắc tương tác): *"Export XLSX/PDF chèn tiêu đề BC + thông tin kỳ + đơn vị + ngày tạo vào header file"* — áp dụng cho **cả PDF**. → PDF vi phạm.
- Đây là lỗi template PDF dùng chung toàn module BC (đã tái hiện ở batch7 trên 4 loại BC khác; batch-8 xác nhận thêm trên VVTTG). Bug: **BUG-EXPORT-PDF-HEADER** (Major, Open).
- Evidence nội dung file: `bug-reports/bctk/image/BUG-EXPORT-PDF-HEADER-VVTTG-pdf-no-header.png`.

## Kết luận
- Lỗi đối tác báo (ERR-RPT-04 "Không thể tạo file xuất") **KHÔNG tái hiện** — file PDF vẫn tạo và tải về được.
- Tuy nhiên **nội dung file PDF sai chuẩn**: thiếu header bắt buộc (Kỳ/Đơn vị/Ngày tạo) theo SRS `:1088`. Đây là defect khác lỗi đối tác báo. → **Open** (BUG-EXPORT-PDF-HEADER).
- Ghi nhận thêm: Xuất PDF có bước dialog chọn khổ giấy/hướng giấy (A4/A3/Letter · Dọc/Ngang) trước khi tạo file — hợp lý, không phải lỗi.
- Bảng đối chiếu điều kiện 0 GAP: `cond/VVTTG_06.md`.
