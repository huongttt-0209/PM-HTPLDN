# CPHTCT_06 · CPHTCT_07 (sheet `bug` dòng 238 · 239) — Nội dung tệp xuất so với màn hình thống kê

- Môi trường: https://htpldn-uat.ospgroup.vn — bản dựng **HTPLDN · V1.0.11**
- Tài khoản: **`cbnv_tw`** (Cán bộ Nghiệp vụ Trung ương). Phạm vi Sở Tư pháp Hà Nội của tài khoản địa phương `cbnv_dp` **không có dữ liệu chi trả** nên không dựng được báo cáo để so — đây là phương án dự phòng đã được đồng ý.
- Thời điểm: 2026-08-11 ~10:28 – 10:33
- Báo cáo: **BC Chi phí chi trả hỗ trợ** · Kỳ = **Năm** (01/01/2026 → 31/12/2026) · Đơn vị = Toàn quốc · Thời điểm tạo 11/08/2026 10:29

## Ô "Kết quả verify" không có tiêu chí sẵn — verify theo đúng nội dung lỗi ghi trong ô

Nguyên văn ô (giống nhau ở cả 2 dòng): *"File được xuất hiển thị số liệu thống kê theo quy mô doanh nghiệp nhưng màn hình thống kê không hiển thị"*

⇒ Phép đo: dựng báo cáo trên màn, **đọc nội dung thật của tệp xuất ra** (không chỉ chứng minh tệp tạo được), rồi so từng mục màn hình ↔ tệp. Còn lỗi nếu tệp có mục "theo quy mô doanh nghiệp" mà màn hình không có.

Lưu ý về cách xuất PDF: nút **[Xuất PDF]** không tải tệp ngay, nó mở hộp thoại "Tùy chọn in báo cáo PDF" (khổ giấy A4/A3/Letter, hướng Dọc/Ngang) — phải bấm **[Xuất file]** trong hộp thoại mới sinh tệp. [Xuất Excel] thì tải ngay.

## Đối chiếu 3 nơi: màn hình ↔ Excel (dòng 238) ↔ PDF (dòng 239)

| Mục | Màn hình | Excel | PDF |
|---|---|---|---|
| Tiêu đề | BC Chi phí chi trả hỗ trợ | BC Chi phí chi trả hỗ trợ | BC CHI PHÍ CHI TRẢ HỖ TRỢ |
| Kỳ / khoảng thời gian / đơn vị | Kỳ: Năm • 01/01/2026 → 31/12/2026 • Toàn quốc | Kỳ báo cáo: Năm (từ 01/01/2026 đến 31/12/2026) · Đơn vị: Toàn quốc | y hệt |
| **1. Tổng số hồ sơ** | 25 | 25 | 25 |
| **2. Tổng chi phí** | 226,308,268 | 226308268 | 226.308.268 |
| **3. Trung bình / hồ sơ** | 9,052,331 | 9052331 | 9.052.331 |
| **4. Theo đơn vị** (7 dòng) | Bắc Giang 6 / 103.417.226 / 17.236.204 · An Giang 9 / 36.269.068 / 4.029.896 · Bộ KH&ĐT 2 / 34.666.619 / 17.333.310 · Cục BTTP 3 / 15.802.407 / 5.267.469 · Bắc Ninh 3 / 15.283.887 / 5.094.629 · Bộ Tài chính 1 / 12.622.206 · Bộ Công Thương 1 / 8.246.855 | trùng khít 7 dòng, cùng thứ tự, cùng số | trùng khít 7 dòng, cùng thứ tự, cùng số |
| **5. Theo kỳ** | Năm 2026 · 226.308.268 · 25 | Năm 2026 · 226308268 · 25 | Năm 2026 · 226.308.268 · 25 |
| **Mục "theo quy mô doanh nghiệp"** | **không có** | **không có** | **không có** |

Quét chuỗi "quy mô" trên cả ba nơi: **0 kết quả**.

Cách đọc nội dung tệp (không dùng công cụ ngoài trình duyệt để lấy tệp): giữ tệp ngay lúc phần mềm sinh ra, giải nén tệp Excel đọc trực tiếp `xl/worksheets/sheet1.xml` (25 dòng có dữ liệu, liệt kê ở bảng trên); tệp PDF ghi ra đĩa rồi đọc chữ trong trang.

## Kết quả

| Dòng | Định dạng | Điểm chấm | Kết |
|---|---|---|---|
| 238 | Excel | Tệp không còn mục thống kê mà màn hình không có; mọi mục và mọi con số trùng màn hình | ✅ |
| 239 | PDF | Tệp không còn mục thống kê mà màn hình không có; mọi mục và mọi con số trùng màn hình | ✅ |

## Ghi nhận thêm (không đổi kết quả)

- PDF ra đúng khổ **A4** (595,3 × 841,9 pt), 1 trang; có quốc hiệu/tiêu ngữ + tên cơ quan "CỤC BỔ TRỢ TƯ PHÁP - BỘ TƯ PHÁP" ở đầu, cuối trang có "Ngày 11 tháng 08 năm 2026 / NGƯỜI XUẤT BÁO CÁO / (Ký, ghi rõ họ tên và đóng dấu) / Cán bộ NV Trung ương".
- Tên trang tính trong tệp Excel: "BC Chi phí chi trả".

## Bằng chứng

- [image/CPHTCT_06-07-r238-239-uat-man-hinh-bao-cao-chi-phi.png](image/CPHTCT_06-07-r238-239-uat-man-hinh-bao-cao-chi-phi.png) — màn hình thống kê: 3 chỉ số + biểu đồ + bảng Theo đơn vị + bảng Theo kỳ
- [image/CPHTCT_07-r239-uat-pdf-trang-1.png](image/CPHTCT_07-r239-uat-pdf-trang-1.png) — ảnh trang PDF xuất ra
- [CPHTCT_07-r239-uat-BaoCaoChiPhiChiTra.pdf](CPHTCT_07-r239-uat-BaoCaoChiPhiChiTra.pdf) — chính tệp PDF phần mềm sinh ra
