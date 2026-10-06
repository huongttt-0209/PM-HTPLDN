# Audit — CLDTBDDDR_07 (row 223) — Xuất PDF BC Lớp đào tạo đang diễn ra — Verdict: Open (BUG-EXPORT-PDF-HEADER)

> **Cập nhật 21/07/2026:** verdict đổi từ Reject → **Open** sau khi kiểm tra NỘI DUNG file PDF tải về. Lỗi ERR-RPT-04 vẫn KHÔNG tái hiện, nhưng file PDF thiếu header bắt buộc → tái hiện BUG-EXPORT-PDF-HEADER. Xem mục "Kiểm tra nội dung file xuất".

## Cổng 1 — Bằng chứng đối tác (đã mở full-res)
- File: `partner-evidence/CLDTBDDDR_07.jpg` (giống hệt CLDTBDDDR_06.jpg — đối tác tái dùng 1 ảnh cho cả Excel và PDF). 3 dữ kiện neo:
  - (a) URL: `htpldn-uat.ospgroup.vn/bao-cao?loai=lop-dao-tao-dang-dien-ra&kyBaoCao=NAM...` (env đối tác).
  - (b) Trạng thái: báo cáo đã Xem ra data (Tổng số = 3); toast đỏ "Không thể tạo file xuất. Vui lòng thử lại."; vai trò Quản trị viên (QTHT).
  - (c) Tiền đề: BC Lớp đào tạo đang diễn ra, Kỳ Năm 2026, Đơn vị Toàn quốc.

## Cổng 2 — Hiểu bug
- Frame chứa lỗi: toast ERR-RPT-04 khi Xuất PDF trên báo cáo có data.
- Đối tác phản ánh: bấm Xuất PDF → báo lỗi tạo file, không tải được tệp PDF.

## Cổng 3 — Đối chiếu SRS vs web
- SRS `srs-v3.5/srs-fr-11-bao-cao.md:1049` (SCR-IX-01 item 9) + AC `:124`: Xuất PDF → click → auto-download file .pdf (TT17). E6 `:116` ERR-RPT-04 = message đối tác báo.
- Web QA: Xuất PDF → dialog chọn khổ giấy/hướng → Xuất file → tải file .pdf thành công, không có ERR-RPT-04 → đúng SCR item 9 + AC 124.

## Verify — 2 phương pháp (env QA, account `cbnv_tw_05`)
1. UI: báo cáo có data (Tổng số=1, Toàn quốc); Xuất PDF → dialog "Tùy chọn in báo cáo PDF" (A4/A3/Letter · Dọc/Ngang) → A4/Dọc → Xuất file → toast "Đang tạo file..."; không toast lỗi. Ảnh `CLDTBDDDR_07-web-export-pdf.png`.
2. Network: `POST /api/v1/bao-cao/export` reqid=133 → **200**, content-type application/pdf, content-disposition attachment `bao-cao-lop-dao-tao-dang-dien-ra-2026-07-21.pdf`, body binary.

## Kiểm tra nội dung file xuất (bổ sung 21/07/2026)
- Tải file PDF thật về qua fetch (`POST /api/v1/bao-cao/export`, formatXuat=PDF, A4/portrait) rồi mở đọc bằng PyMuPDF.
- **Khổ giấy:** A4 (210×297mm) ✅. **Font:** Tinos (Times New Roman-tương thích), body cỡ 13 ✅. **Số liệu:** đúng (Bộ Kế hoạch và Đầu tư, trực tuyến 1, Tổng 1).
- **Header file:** ❌ PDF chỉ có tiêu đề "BC LỚP ĐÀO TẠO ĐANG DIỄN RA" rồi vào thẳng bảng — THIẾU 3/4 trường: **Kỳ báo cáo / Đơn vị / Ngày tạo** (bản Excel cùng báo cáo có đủ 4 trường).
- SRS `srs-v3.5/srs-fr-11-bao-cao.md:1088`: *"Export XLSX/PDF chèn tiêu đề BC + thông tin kỳ + đơn vị + ngày tạo vào header file"* → PDF vi phạm. Bug: **BUG-EXPORT-PDF-HEADER** (Major, Open).
- Evidence: `bug-reports/bctk/image/BUG-EXPORT-PDF-HEADER-CLDTBDDDR-pdf-no-header.png`.

## Kết luận
- Lỗi ERR-RPT-04 ("Không thể tạo file xuất") **KHÔNG tái hiện** — file PDF vẫn tạo/tải được.
- Nhưng **nội dung file PDF sai chuẩn**: thiếu header bắt buộc (Kỳ/Đơn vị/Ngày tạo) theo SRS `:1088` → defect khác lỗi đối tác báo. → **Open** (BUG-EXPORT-PDF-HEADER). Bảng điều kiện 0 GAP: `cond/CLDTBDDDR_07.md`.
