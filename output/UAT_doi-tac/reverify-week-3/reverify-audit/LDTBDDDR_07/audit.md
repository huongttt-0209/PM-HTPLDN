# Audit — LDTBDDDR_07 (row 228) — Xuất PDF BC Lớp đào tạo đã diễn ra — Verdict: Open (BUG-EXPORT-PDF-HEADER)

> **Cập nhật 21/07/2026:** verdict đổi từ Reject → **Open** sau khi kiểm tra NỘI DUNG file PDF tải về. Lỗi ERR-RPT-04 vẫn KHÔNG tái hiện, nhưng file PDF thiếu header bắt buộc → tái hiện BUG-EXPORT-PDF-HEADER. Xem mục "Kiểm tra nội dung file xuất".

## Cổng 1 — Bằng chứng đối tác
- File cột "Ảnh/vieo 1" row 228 = `CLDTBDDDR_07.jpg` (đối tác gán NHẦM ảnh báo cáo "Lớp đào tạo ĐANG diễn ra" cho case "ĐÃ diễn ra"). KQ thực tế đối tác ghi trong sheet: "Không thể tạo file xuất. Vui lòng thử lại." (ERR-RPT-04). Vai trò: Quản trị viên (QTHT).
- Tiền đề case: đăng nhập thành công + có dữ liệu thống kê. Thao tác: Xem báo cáo → Xuất PDF.

## Cổng 2 — Hiểu bug
- Đối tác phản ánh: bấm Xuất PDF báo cáo Lớp đào tạo đã diễn ra → báo lỗi tạo file, không tải được tệp PDF.

## Cổng 3 — Đối chiếu SRS vs web
- SRS `srs-v3.5/srs-fr-11-bao-cao.md:1049` (SCR-IX-01 item 9) + AC `:124`: Xuất PDF → auto-download .pdf (TT17). FR-IX-07 `:389`. E6 `:116` ERR-RPT-04.
- Web QA: Xuất PDF → dialog khổ giấy/hướng → Xuất file → tải file .pdf thành công, không có ERR-RPT-04.

## Verify — 2 phương pháp (env QA, account `cbnv_tw_05`)
1. UI: BC Lớp đào tạo đã diễn ra, Năm 2026, Toàn quốc → Xem báo cáo ra data (Tổng khóa học=5, Tổng học viên=11). Xuất PDF → dialog A4/Dọc → Xuất file → toast "Đang tạo file..."; không toast lỗi. Ảnh `LDTBDDDR_07-web-export-pdf.png`.
2. Network: `POST /api/v1/bao-cao/export` reqid=141 (loaiBaoCao=BC_LOP_DAO_TAO_DA_DIEN_RA, PDF, A4, portrait) → **200**, content-type application/pdf, content-disposition attachment `bao-cao-lop-dao-tao-da-dien-ra-2026-07-21.pdf`, body binary.

## Kiểm tra nội dung file xuất (bổ sung 21/07/2026)
- Tải file PDF thật về qua fetch (`POST /api/v1/bao-cao/export`, formatXuat=PDF, A4/portrait) rồi mở đọc bằng PyMuPDF.
- **Khổ giấy:** A4 (210×297mm) ✅. **Font:** Tinos (Times New Roman-tương thích), tiêu đề cỡ 14, body cỡ 13 ✅. **Số liệu:** đúng — 3 đơn vị: Cục Bổ trợ tư pháp 2 khóa/5 HV, Bộ KH&ĐT 1/3, Sở Tư pháp Hà Nội 2/3 (Σ = 5 khóa / 11 học viên, khớp màn hình).
- **Header file:** ❌ PDF chỉ có tiêu đề "BC LỚP ĐÀO TẠO ĐÃ DIỄN RA" rồi vào thẳng bảng — THIẾU 3/4 trường: **Kỳ báo cáo / Đơn vị / Ngày tạo** (bản Excel cùng báo cáo có đủ 4 trường; xem ảnh so sánh).
- SRS `srs-v3.5/srs-fr-11-bao-cao.md:1088`: *"Export XLSX/PDF chèn tiêu đề BC + thông tin kỳ + đơn vị + ngày tạo vào header file"* → PDF vi phạm. Bug: **BUG-EXPORT-PDF-HEADER** (Major, Open).
- Evidence: `bug-reports/bctk/image/BUG-EXPORT-PDF-HEADER-LDTBDDDR-pdf-no-header.png` + so sánh `BUG-EXPORT-PDF-HEADER-compare-LDTBDDDR.png`.

## Kết luận
- Lỗi ERR-RPT-04 ("Không thể tạo file xuất") **KHÔNG tái hiện** — file PDF vẫn tạo/tải được.
- Nhưng **nội dung file PDF sai chuẩn**: thiếu header bắt buộc (Kỳ/Đơn vị/Ngày tạo) theo SRS `:1088` → defect khác lỗi đối tác báo. → **Open** (BUG-EXPORT-PDF-HEADER). Bảng điều kiện 0 GAP: `cond/LDTBDDDR_07.md`.
