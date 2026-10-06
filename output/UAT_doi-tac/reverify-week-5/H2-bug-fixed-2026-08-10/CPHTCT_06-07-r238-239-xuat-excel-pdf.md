# CPHTCT_06 / CPHTCT_07 (sheet `bug` dòng 238 · 239) — Xuất Excel · Xuất PDF

- Môi trường: https://18.143.165.120.nip.io — bản dựng **HTPLDN · V1.0.11**
- Tài khoản: `cbnv_tw_03` (CB Nghiệp vụ Trung ương, Cục Bổ trợ tư pháp - Bộ Tư pháp)
- Thời điểm: 2026-08-10 21:30 (Excel) · 21:35 (PDF)
- Báo cáo đo: **BC Chi phí chi trả hỗ trợ** (đúng cụm CPHTCT — FR-IX-15 / UC138), Kỳ = Năm, 01/01/2026 → 31/12/2026, Đơn vị = Toàn quốc
- Đường đi: thanh bên → Báo cáo thống kê → chọn loại + kỳ → **Xem báo cáo** → **Xuất Excel** / **Xuất PDF**

## Tiêu chí đang verify (nguyên văn ô "Kết quả verify" của cả 2 dòng)

> - File được xuất hiển thị số liệu thống kê theo quy mô doanh nghiệp nhưng màn hình thống kê không hiển thị

⇒ Phép đo quyết định: **so từng mục giữa màn hình và tệp xuất**, xem tệp có còn mục "theo quy mô doanh nghiệp" mà màn hình không có hay không.

## Kết quả đo — màn hình vs tệp xuất

| Mục | Màn hình | Excel | PDF |
|---|---|---|---|
| Tổng chi phí | 23.000.000 ₫ | 23000000 | 23.000.000 |
| Tổng hồ sơ | 2 | 2 | 2 |
| Trung bình / hồ sơ | 11.500.000 ₫ | 11500000 | 11.500.000 |
| Bảng **Theo đơn vị** | Cục Bổ trợ tư pháp - Bộ Tư pháp · 2 · 23.000.000 ₫ · 11.500.000 ₫ | y hệt | y hệt |
| Bảng **Theo kỳ** | Năm 2026 · 23.000.000 ₫ · 2 | y hệt | y hệt |
| Mục **theo quy mô doanh nghiệp** | KHÔNG có | **KHÔNG có** | **KHÔNG có** |

→ Ba nơi trùng khớp đúng 5 mục, **không còn mục "theo quy mô doanh nghiệp"** trong tệp. Lỗi đang treo hết tái hiện.
Kiểm chứng bằng máy: đọc thẳng ruột tệp `.xlsx` (giải nén `xl/worksheets/sheet1.xml`) và `.pdf` (PyMuPDF) — tìm chuỗi "quy mô" trên toàn bộ nội dung → **0 lần xuất hiện**.

## CPHTCT_06 — Xuất Excel

- Tệp về máy thật: `~/Downloads/BaoCaoChiPhiChiTra_20260810_2130.xlsx` — **6.808 byte**, MIME `application/vnd.openxmlformats-officedocument.spreadsheetml.sheet`
- Không còn thông báo "Không thể tạo file xuất. Vui lòng thử lại." và không còn "Forbidden" (vai trò CB Nghiệp vụ được phép xuất). `POST /api/v1/bao-cao/export` → **200**.
- Ruột tệp (1 sheet "BC Chi phí chi trả", 19 dòng có dữ liệu):
  tiêu đề BC → Kỳ báo cáo: **Năm** (chữ tiếng Việt, không in mã `NAM`) → Đơn vị → Ngày tạo → Tổng số hồ sơ → Tổng chi phí → Trung bình / hồ sơ → Theo đơn vị → Theo kỳ.

## CPHTCT_07 — Xuất PDF

Luồng đã đổi: bấm **Xuất PDF** mở hộp thoại **"Tùy chọn in báo cáo PDF"** (Khổ giấy A4/A3/Letter, Hướng Dọc/Ngang; mặc định **A4 + Dọc**) → bấm **Xuất file** mới sinh tệp. Giữ mặc định A4 + Dọc.

- Tệp về máy thật: `~/Downloads/BaoCaoChiPhiChiTra_20260810_2135.pdf` — **33.892 byte**, `%PDF-1.3`, 1 trang
- Khổ giấy đo được: **595,3 × 841,9 pt = 210 × 297 mm → đúng A4**
- Đầu trang: `CỤC BỔ TRỢ TƯ PHÁP - BỘ TƯ PHÁP` · `CỘNG HÒA XÃ HỘI CHỦ NGHĨA VIỆT NAM` · `Độc lập - Tự do - Hạnh phúc` → đủ quốc hiệu + tiêu ngữ + tên cơ quan
- Cuối trang: `Ngày 10 tháng 08 năm 2026` · `NGƯỜI XUẤT BÁO CÁO` · `(Ký, ghi rõ họ tên và đóng dấu)` · `CB Nghiệp vụ - Trung ương #03` → đủ ngày ký + họ tên cán bộ xuất + chỗ trống con dấu, **không in dòng chức danh** (đúng ngoại lệ srs-fr-11-bao-cao.md:86)
- Nội dung 5 mục trùng khớp màn hình (bảng trên)

## Ghi nhận thêm — KHÔNG thuộc tiêu chí lần verify này, không đổi verdict

1. **Tên tệp** ra `BaoCaoChiPhiChiTra_{YYYYMMDD_HHmm}` thay vì `BaoCaoChiPhi_{YYYYMMDD_HHmm}` như phiếu ghi. Phiếu viết trước khi BA chốt quy ước chung (srs-fr-11-bao-cao.md:85-86, Phụ lục E §H8 — BA chốt 2026-08-04, nâng thành quy ước chung 2026-08-06): tên tệp lấy theo **tên loại báo cáo**. Tên hiện tại suy từ đúng loại báo cáo đang xuất nên coi là đạt.
2. **Cỡ chữ trong tệp:** PDF dùng bộ Tinos (bản tương thích số đo với Times New Roman) — tiêu đề 14, quốc hiệu/tên cơ quan 13, dòng kỳ/đơn vị 12, ruột bảng **11**; Excel dùng **Calibri 11** và không đặt khổ giấy A4 trong page-setup. Đặc tả chung của trang báo cáo (srs-fr-11-bao-cao.md:85-86) ghi "khổ A4, Times New Roman cỡ 13". Đây là chi tiết trình bày, KHÔNG phải nội dung lỗi của 2 phiếu này (phiếu CPHTCT_06 không đặt yêu cầu phông/khổ cho Excel), và phiếu cùng bộ sinh tệp `CPCTHTTDVQL_07` (dòng 244) đã được nghiệm thu **UAT done** → không mở rộng case, chỉ ghi lại để đơn vị chủ quản quyết.

## Bằng chứng

- Màn hình báo cáo: [image/CPHTCT_06-r238-man-hinh-bao-cao-chi-phi-chi-tra.png](image/CPHTCT_06-r238-man-hinh-bao-cao-chi-phi-chi-tra.png)
- Hộp thoại tùy chọn in PDF (A4 + Dọc): [image/CPHTCT_07-r239-modal-tuy-chon-in-pdf-A4-doc.png](image/CPHTCT_07-r239-modal-tuy-chon-in-pdf-A4-doc.png)
- Nội dung PDF trang 1: [image/CPHTCT_07-r239-noi-dung-pdf-A4-trang1.png](image/CPHTCT_07-r239-noi-dung-pdf-A4-trang1.png)
- Tệp gốc kèm theo: `CPHTCT_06-r238-BaoCaoChiPhiChiTra.xlsx` · `CPHTCT_07-r239-BaoCaoChiPhiChiTra.pdf`
