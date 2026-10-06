# Audit — CLDTBDDDR_06 (row 222) — Xuất Excel BC Lớp đào tạo đang diễn ra — Verdict: Reject

## Cổng 1 — Bằng chứng đối tác (đã mở full-res)
- File: `partner-evidence/CLDTBDDDR_06.jpg`. 3 dữ kiện neo:
  - (a) URL: `htpldn-uat.ospgroup.vn/bao-cao?loai=lop-dao-tao-dang-dien-ra&kyBaoCao=NAM&tuNgay=2026-01-01&denNgay=2026-12-31` (env đối tác).
  - (b) Trạng thái: báo cáo đã Xem ra data (Tổng số = 3); toast đỏ "Không thể tạo file xuất. Vui lòng thử lại."; vai trò Quản trị viên (QTHT).
  - (c) Tiền đề: BC Lớp đào tạo đang diễn ra, Kỳ Năm 2026, Đơn vị Toàn quốc.

## Cổng 2 — Hiểu bug
- Frame chứa lỗi: toast ERR-RPT-04 sau khi bấm Xuất Excel trên báo cáo có data.
- Đối tác phản ánh: bấm Xuất Excel → báo lỗi tạo file, không tải được tệp.

## Cổng 3 — Đối chiếu SRS vs web
- SRS `srs-v3.5/srs-fr-11-bao-cao.md:1048` (SCR-IX-01 item 8) + AC `:123`: Xuất Excel → click → auto-download file .xlsx (TT17). E6 `:116` ERR-RPT-04 = message đối tác báo.
- Web QA: Xuất Excel → tải file .xlsx thành công, không có ERR-RPT-04 → đúng SCR item 8 + AC 123.

## Verify — 2 phương pháp (env QA, account `cbnv_tw_05`)
1. UI: báo cáo có data (Tổng số=1, Toàn quốc); bấm Xuất Excel → toast "Đang tạo file..."; không toast lỗi. Ảnh `CLDTBDDDR_06-web-export-excel.png`.
2. Network: `POST /api/v1/bao-cao/export` reqid=130 → **200**, content-type xlsx, content-disposition attachment `bao-cao-lop-dao-tao-dang-dien-ra-2026-07-21.xlsx`, body binary.

## Kết luận
- Lỗi ERR-RPT-04 KHÔNG tái hiện → **Reject** + "→ Đối tác kiểm tra lại". Bảng điều kiện 0 GAP: `cond/CLDTBDDDR_06.md`.
- **Kiểm tra nội dung file (bổ sung 21/07):** tải file .xlsx thật về, mở bằng openpyxl → có đủ 4 trường header (tiêu đề "BC Lớp đào tạo đang diễn ra" · "Kỳ báo cáo: Năm..." · "Đơn vị: Toàn quốc" · "Ngày tạo: 21/07/2026") + số liệu đúng (Bộ Kế hoạch và Đầu tư, trực tuyến 1, Tổng 1). Bản Excel đạt chuẩn header SRS `:1088` → giữ **Reject**. (Bản PDF cùng báo cáo — CLDTBDDDR_07 — thiếu header, xử lý riêng ở BUG-EXPORT-PDF-HEADER.)
