# Audit — LDTBDDDR_06 (row 227) — Xuất Excel BC Lớp đào tạo đã diễn ra — Verdict: Reject

## Cổng 1 — Bằng chứng đối tác
- File cột "Ảnh/vieo 1" row 227 = `CLDTBDDDR_06.jpg` (đối tác gán NHẦM ảnh báo cáo "Lớp đào tạo ĐANG diễn ra" cho case "ĐÃ diễn ra"). KQ thực tế đối tác ghi trong sheet: "Không thể tạo file xuất. Vui lòng thử lại." (ERR-RPT-04). Vai trò: Quản trị viên (QTHT).
- Tiền đề case (cột Điều kiện): đăng nhập thành công + có dữ liệu thống kê. Thao tác (cột Các bước): Xem báo cáo → Xuất Excel.

## Cổng 2 — Hiểu bug
- Đối tác phản ánh: bấm Xuất Excel báo cáo Lớp đào tạo đã diễn ra → báo lỗi tạo file, không tải được tệp.

## Cổng 3 — Đối chiếu SRS vs web
- SRS `srs-v3.5/srs-fr-11-bao-cao.md:1048` (SCR-IX-01 item 8) + AC `:123`: Xuất Excel → auto-download .xlsx. FR-IX-07 `:389` (BC Lớp đào tạo đã diễn ra). E6 `:116` ERR-RPT-04.
- Web QA: Xuất Excel → tải file .xlsx thành công, không có ERR-RPT-04.

## Verify — 2 phương pháp (env QA, account `cbnv_tw_05`)
1. UI: BC Lớp đào tạo đã diễn ra, Năm 2026, Toàn quốc → Xem báo cáo ra data (Tổng khóa học=5, Tổng học viên=11). Bấm Xuất Excel → toast "Đang tạo file..."; không toast lỗi. Ảnh `LDTBDDDR_06-web-export-excel.png`.
2. Network: `POST /api/v1/bao-cao/export` reqid=139 (loaiBaoCao=BC_LOP_DAO_TAO_DA_DIEN_RA, XLSX) → **200**, content-type xlsx, content-disposition attachment `bao-cao-lop-dao-tao-da-dien-ra-2026-07-21.xlsx`, body binary.

## Kết luận
- Lỗi ERR-RPT-04 KHÔNG tái hiện → **Reject** + "→ Đối tác kiểm tra lại". Bảng điều kiện 0 GAP: `cond/LDTBDDDR_06.md`.
- **Kiểm tra nội dung file (bổ sung 21/07):** tải file .xlsx thật về, mở bằng openpyxl → có đủ 4 trường header (tiêu đề "BC Lớp đào tạo đã diễn ra" · "Kỳ báo cáo: Năm..." · "Đơn vị: Toàn quốc" · "Ngày tạo: 21/07/2026") + số liệu đúng (Σ = 5 khóa / 11 học viên: Cục Bổ trợ 2/5, Bộ KH&ĐT 1/3, Sở Tư pháp Hà Nội 2/3). Bản Excel đạt chuẩn header SRS `:1088` → giữ **Reject**. (Bản PDF cùng báo cáo — LDTBDDDR_07 — thiếu header, xử lý riêng ở BUG-EXPORT-PDF-HEADER.)
