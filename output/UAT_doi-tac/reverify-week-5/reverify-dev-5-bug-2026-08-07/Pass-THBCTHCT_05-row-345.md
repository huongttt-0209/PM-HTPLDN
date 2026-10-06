# Reverify THBCTHCT_05 - dòng 345

- Thời gian chạy: 08/08/2026, khoảng 00:26-00:31 giờ Việt Nam
- Môi trường: `https://18.143.165.120.nip.io`
- Giao diện: `HTPLDN · V1.0.10`
- Công cụ thao tác: Chrome DevTools trên cửa sổ Chrome hiển thị; không dùng Playwright, không gọi backend trực tiếp
- Tài khoản xuất báo cáo: **CB Nghiệp vụ - Trung ương #05**, đơn vị **BTP · TW**
- BA/DEV chốt ngày 06/08 dùng để chấm: tên tệp theo quy ước chung `BaoCaoTongHopCTHTPL_{YYYYMMDD_HHmm}`; vùng ký không in sẵn dòng chức danh
- Verdict: **PASS / Test done**

## Luồng UI đã thực hiện

1. Từ menu **Đợt báo cáo**, mở đợt `DOT-TRON_NAM-2026-1`, trạng thái **Đã tổng hợp**.
2. Mở màn **Tổng hợp báo cáo toàn quốc** bằng giao diện web.
3. Chọn đúng duy nhất dòng **Sở Tư pháp An Giang / DOT-TRON_NAM-2026-1 / Tròn năm / Đã tổng hợp**. Đây là báo cáo nguồn `b63fe4e2-0af5-4945-aeab-825814107209` đã được dùng duy nhất để tạo bản tổng hợp TW `04ae77a6-3c28-479c-98ce-a42154264828` ở lượt row343. Nút `Tổng hợp (1)` bị khóa đúng vì báo cáo đã tổng hợp; hai nút xuất được bật.
4. Bấm **Xuất Excel** bằng UI; trình duyệt tải thật tệp Excel vào Downloads.
5. Giữ nguyên tập chọn, bấm **Xuất Word** bằng UI; trình duyệt tải thật tệp Word vào Downloads.
6. Mở trực tiếp hai tệp vừa tải bằng `openpyxl` và `python-docx`, đồng thời kiểm tra cấu trúc OOXML, khổ giấy, phông/cỡ chữ, nội dung, vùng ký và số liệu.

## Kết quả theo từng tiêu chí quyết định

| Tiêu chí | Bằng chứng thực tế | Kết quả |
|---|---|---|
| Tải đủ hai định dạng qua UI | Hai lượt bấm UI tạo hai `POST /api/v1/dot-bao-caos/tong-hop/export`, đều HTTP 200. Chrome tải hoàn tất hai tệp thật, không còn `.crdownload`; `file` nhận dạng đúng Microsoft Excel 2007+ và Microsoft Word 2007+. | PASS |
| Tên tệp exact theo BA | Excel: `BaoCaoTongHopCTHTPL_20260808_0028.xlsx`; Word: `BaoCaoTongHopCTHTPL_20260808_0029.docx`. Đúng `YYYYMMDD_HHmm`, không có dạng sai `TongHop_CT`. | PASS |
| Nội dung theo TT17 | Cả hai tệp có tiêu đề báo cáo tổng hợp, dòng `Biểu mẫu 21a/TP/HTPLDN (Theo Thông tư số 17/2025/TT-BTP)` và bảng đủ 13 chỉ tiêu. Excel có một sheet `Biểu mẫu 21a TP HTPLDN`, vùng dùng `A1:C29`; Word có bảng quốc hiệu/cơ quan và bảng chỉ tiêu 14 dòng gồm tiêu đề + 13 chỉ tiêu. | PASS |
| Khổ A4 | Excel `paperSize = 9`, portrait, fit 1 trang ngang/dọc. Word có khổ `209,99 × 296,99 mm`, portrait. | PASS |
| Times New Roman cỡ 13 | Excel: **42/42** ô của bảng `A8:C21` là Times New Roman 13. Word: `docDefaults` là Times New Roman, `w:sz = 26` = 13 pt; toàn bộ nội dung bảng kế thừa mặc định này. Tiêu đề/chú thích dùng cỡ nhấn theo mẫu, không làm thay đổi cỡ chữ thân bảng. | PASS |
| Quốc hiệu và tên cơ quan | Cả hai tệp có `CỘNG HÒA XÃ HỘI CHỦ NGHĨA VIỆT NAM`, `Độc lập - Tự do - Hạnh phúc` và `BỘ TƯ PHÁP`. | PASS |
| Ngày, người xuất, vùng ký/dấu | Cả hai có `Ngày 08 tháng 08 năm 2026`, `NGƯỜI XUẤT BÁO CÁO`, `(Ký, ghi rõ họ tên và đóng dấu)` và họ tên đầy đủ `CB Nghiệp vụ - Trung ương #05`. Excel để trống ba dòng giữa hướng dẫn ký và họ tên; Word tạo khoảng trống ký 50 pt. | PASS |
| Không in sẵn chức danh | Quét toàn bộ text/XML của cả hai tệp không có `Chức vụ`, `Cục trưởng`, `Phó Cục trưởng`, `Trưởng phòng`, `Thủ trưởng`, `Giám đốc` hoặc một dòng chức danh tương tự. Vùng dành cho chức danh/ký/dấu để trống đúng BA chốt. | PASS |
| Số liệu khớp bản đã chọn | Excel và Word cùng trả đúng dãy 13 số: `5, 2, 1, 3, 6, 14, 10, 4, 5, 1, 235.000.000, 60.000.000, 18.000.000`. Dãy này khớp 13/13 với báo cáo An Giang `b63fe4e2…` đã chọn; row343 chứng minh bản tổng hợp `04ae77a6…` được tạo từ duy nhất nguồn này. Không có số liệu Hà Nội bị kéo vào. | PASS |

## Network, console và bằng chứng hiển thị

- Network do chính thao tác UI tạo: request Excel và Word đều đến endpoint export tổng hợp, đều HTTP 200.
- Response Excel có `Content-Type` đúng OpenXML spreadsheet và `Content-Disposition` đúng tên `BaoCaoTongHopCTHTPL_20260808_0028.xlsx`; tệp Word đã được Chrome lưu hoàn chỉnh với tên `_0029.docx` và mở được bằng thư viện Word.
- Console sau hai lượt xuất: không có `error` hoặc `warning`.
- Chrome DevTools đã chụp các trạng thái hiển thị: trước khi chọn; sau khi chọn đúng một dòng An Giang với hai nút xuất bật; sau lượt bấm Excel; sau lượt bấm Word. Tập chọn không thay đổi giữa hai lần xuất.

## Tệp kiểm tra thực tế

- `/Users/huongttt/Downloads/BaoCaoTongHopCTHTPL_20260808_0028.xlsx` — 7,8 KB
- `/Users/huongttt/Downloads/BaoCaoTongHopCTHTPL_20260808_0029.docx` — 9,7 KB

Hai tệp là kết quả trực tiếp của các lượt click UI lúc 00:28 và 00:29; không lấy lại tệp cũ và không gọi endpoint lần hai ngoài giao diện.

## Kết luận để cập nhật Sheet

`Trạng thái dev fix = Test done`.

`Kết quả verify`: **PASS - Xuất thành công đủ Excel và Word từ bản tổng hợp hoàn tất. Tên tệp đúng quy ước BaoCaoTongHopCTHTPL_YYYYMMDD_HHmm, nội dung theo TT17, A4, thân bảng Times New Roman 13, đủ quốc hiệu/cơ quan/ngày/người xuất, vùng ký-dấu để trống và không in sẵn chức danh; 13/13 số liệu ở hai định dạng khớp bản báo cáo đã chọn.**
