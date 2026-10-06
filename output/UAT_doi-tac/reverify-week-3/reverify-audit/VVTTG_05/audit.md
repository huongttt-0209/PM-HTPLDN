# Audit — VVTTG_05 (row 216) — Xuất Excel BC Vụ việc theo thời gian — Verdict: Reject

## Cổng 1 — Bằng chứng đối tác (đã mở full-res)
- File: `partner-evidence/VVTTG_05.jpg` (233 KB).
- 3 dữ kiện neo:
  - (a) URL/ID: `htpldn-uat.ospgroup.vn/bao-cao?loai=...&kyBaoCao=NAM&tuNgay=2026-01-01&denNgay=2026-12-31&donViId=00000000-0000-4000-8000-0000000...` (env đối tác).
  - (b) Trạng thái: báo cáo ĐÃ Xem ra data (KPI "Tổng vụ việc toàn kỳ = 1"); toast đỏ **"Không thể tạo file xuất. Vui lòng thử lại."** hiển thị góc trên. Vai trò đăng nhập = Quản trị viên (QTHT).
  - (c) Tiền đề: Loại BC = BC Vụ việc theo thời gian; Kỳ = Năm 2026; Đơn vị = Cục Bổ trợ tư pháp - Bộ Tư pháp (BTP-TW).

## Cổng 2 — Hiểu bug
- Evidence đã xem: VVTTG_05.jpg, frame chứa lỗi = toast "Không thể tạo file xuất. Vui lòng thử lại." ngay sau khi bấm Xuất Excel trên báo cáo đã có data (1 VV).
- Đối tác phản ánh cụ thể: bấm **Xuất Excel** → hệ thống báo lỗi tạo file (ERR-RPT-04), tệp KHÔNG được tải về.
- Data + bước tái hiện: Login → Báo cáo thống kê → BC Vụ việc theo thời gian → Kỳ Năm 2026 → Xem báo cáo (ra data) → Xuất Excel.

## Cổng 3 — Đối chiếu SRS vs thực tế web
- SRS `srs-v3.5/srs-fr-11-bao-cao.md:1048` (SCR-IX-01 item 8): Nút "Xuất Excel (.xlsx)" — điều kiện "Sau khi đã Xem báo cáo" — hành vi "click → auto-download".
- AC `:123`: "Given CB nhấn Xuất Excel When click Then tải file .xlsx theo format TT17/2025".
- E6 `:116` ERR-RPT-04 "Không thể tạo file xuất. Vui lòng thử lại" = message đối tác báo (đúng mã lỗi xuất file).
- Thực tế web QA: nút Xuất Excel bật đúng sau khi Xem báo cáo; bấm → tải file .xlsx thành công, KHÔNG có ERR-RPT-04 → web đáp ứng đúng SCR item 8 + AC dòng 123.

## Verify — 2 phương pháp (env `18.143.165.120.nip.io`, account `cbnv_tw_05`)
1. **UI:** đã Xem báo cáo (BC Vụ việc theo thời gian, Năm 2026). Bấm Xuất Excel → toast "Đang tạo file..." (loading); KHÔNG xuất hiện toast lỗi "Không thể tạo file xuất". Ảnh: `VVTTG_05-web-export-excel.png` (data = 6 VV Toàn quốc, không toast lỗi).
2. **Network:** `POST /api/v1/bao-cao/export`:
   - reqid=97 (Toàn quốc): body `{...,"formatXuat":"XLSX"}` → **200**, `content-type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet`, `content-disposition: attachment; filename="bao-cao-vu-viec-theo-thoi-gian-2026-07-21.xlsx"`, body = binary.
   - reqid=108 (đúng đơn vị BTP-TW, donViId ...0001): body `{...,"donViId":"00000000-0000-4000-8000-000000000001","formatXuat":"XLSX"}` → **200** + xlsx binary (khớp điều kiện đối tác).

## Kết luận
- Lỗi đối tác báo (ERR-RPT-04 khi Xuất Excel) **KHÔNG tái hiện** trên env QA — hệ thống tạo và tải file .xlsx thành công ở cả 2 phạm vi. → **Reject** + "→ Đối tác kiểm tra lại".
- **Kiểm tra nội dung file (bổ sung 21/07):** tải file .xlsx thật về, mở bằng openpyxl → có đủ 4 trường header (tiêu đề "BC Vụ việc theo thời gian" · "Kỳ báo cáo: Năm..." · "Đơn vị: Toàn quốc" · "Ngày tạo: 21/07/2026") + số liệu đúng (Số vụ việc = 6). Bản Excel đạt chuẩn header SRS `:1088` → giữ **Reject**. (Bản PDF cùng báo cáo — VVTTG_06 — thiếu header, xử lý riêng ở BUG-EXPORT-PDF-HEADER.)
- Bảng đối chiếu điều kiện 0 GAP: `cond/VVTTG_05.md`.
