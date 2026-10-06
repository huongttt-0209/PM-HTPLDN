# VVTLHDN_06 — đo lại trên môi trường nghiệm thu đối tác (05/08/2026)

Tiêu chí lấy nguyên khối ở cột `DEV phản hồi lần 2`, dòng 247 (tab `UAT_TGPL Doanh Nghiệp-tuần 3`).

| Điều kiện | Bug gốc (khối CÁCH VERIFY) | Mình test | GAP? |
|---|---|---|---|
| Môi trường | Bản mới nhất của môi trường nghiệm thu | `https://htpldn-uat.ospgroup.vn` — nhãn `HTPLDN · V1.0.7` | Không |
| Vai trò | `cbnv_tw` | `cbnv_tw` · CB_NV_TW · cấp TW · Cục Bổ trợ tư pháp | Không |
| Màn hình | Báo cáo thống kê | Sidebar → Báo cáo thống kê (`/bao-cao`) | Không |
| Loại báo cáo | Đúng loại của phiếu này | `BC Vụ việc theo loại hình DN` | Không |
| Kỳ báo cáo | Năm 2026 | Kỳ `Năm` → tự điền 01/01/2026 – 31/12/2026 | Không |
| Đơn vị | Toàn quốc | `Toàn quốc` | Không |
| Thao tác | Xem báo cáo → Xuất PDF → lưu tệp | Bấm [Xem báo cáo] → [Xuất PDF] → hộp thoại "Tùy chọn in báo cáo PDF" (A4 · Dọc) → [Xuất file] | Không |
| Lặp lần 2 cùng ngày | Xuất lại lần nữa trong cùng ngày, so tên | Xuất lần 2 lúc 16:46 cùng ngày, so tên với lần 1 lúc 16:44 | Không |
| Cách đọc tệp | Mở tệp, đọc đầu trang đầu + cuối trang cuối | Đọc nội dung thật của tệp PDF (không chỉ xem tệp tải được) — cả trang đầu và trang cuối, kèm khổ giấy, phông chữ, cỡ chữ | Không |

**Kết luận: 0 GAP → PASS.**

## Đối chiếu từng ý của khối tiêu chí

- **Tệp xuất được, không còn báo lỗi**: bấm [Xuất file] ra tệp PDF **33 604 byte, 1 trang**. Thông báo
  "Không thể tạo file xuất. Vui lòng thử lại." của phản ánh gốc **không còn**.
- **Tên tệp có đủ ngày lẫn giờ-phút**: lần 1 ra `BaoCaoVuViecTheoLoaiDn_20260805_1644.pdf` — đúng dạng `{TênBáoCáo}_{YYYYMMDD_HHmm}.pdf`.
- **Hai lần xuất trong cùng ngày ra hai tên khác nhau**: lần 2 ra `BaoCaoVuViecTheoLoaiDn_20260805_1646.pdf` — khác lần 1, nên xuất nhiều lần
  trong ngày không còn đè lên nhau.
- **Đầu trang có quốc hiệu, tiêu ngữ và tên cơ quan ban hành**: trang 1 mở đầu bằng
  `CỤC BỔ TRỢ TƯ PHÁP - BỘ TƯ PHÁP` · `CỘNG HÒA XÃ HỘI CHỦ NGHĨA VIỆT NAM` · `Độc lập - Tự do - Hạnh phúc`.
- **Cuối trang cuối có ngày ký, họ tên người xuất báo cáo và chỗ trống cho con dấu**: trang cuối kết thúc
  bằng `Ngày 05 tháng 08 năm 2026` · `NGƯỜI XUẤT BÁO CÁO` · `(Ký, ghi rõ họ tên và đóng dấu)` · `Cán bộ NV Trung ương` (đúng tên tài
  khoản đang đăng nhập).
- **Khổ A4**: kích thước trang đo được `595,28 × 841,89` điểm — đúng A4 dọc.
- **Phông Times New Roman**: tệp nhúng phông `Tinos-Bold` / `Tinos-Regular` / `Tinos-Italic` — bộ phông cùng số đo với Times New Roman. Khối tiêu đề
  và các dòng hành chính ở **cỡ 13–14**.
- **Đủ bốn mục**: `BC VỤ VIỆC THEO LOẠI HÌNH DN` (tên báo cáo) · `Kỳ báo cáo: Năm (từ 01/01/2026 đến 31/12/2026)` · `Đơn vị: Toàn quốc` · `Ngày tạo: 05/08/2026`.
- **Hai điều phiếu dặn KHÔNG chấm FAIL đã tôn trọng**: tệp không có chữ ký số (cờ chữ ký = không có) và
  không có dòng chức danh người ký — đúng kết luận đã thống nhất cho nhóm báo cáo thống kê.

Tệp đo: `../evidence/VVTLHDN_06.pdf` (bản bắt trực tiếp từ thao tác [Xuất file]) ·
bản bắt gốc `../evidence/VVTLHDN_06-pdf-capture.json`

## Ghi nhận thêm

- **Cỡ chữ trong bảng số liệu là 11, không phải 13.** Phần tiêu đề và các dòng hành chính (quốc hiệu, tiêu
  ngữ, tên báo cáo, bốn mục) ở cỡ 13–14, còn nội dung bảng ở cỡ 11–12. Đối chiếu với tệp đo ngày 04/08/2026
  (`reverify-week-4/reverify-round-2026-08-04/evidence/bao-cao-hoi-dap-2026-08-04.pdf`) thì phân bố cỡ chữ
  giống hệt — nghĩa là không phải thay đổi do bản vá lần này gây ra, mà là cách trình bày sẵn có đã được
  chấp nhận ở vòng trước. Ghi lại để BA quyết có yêu cầu đưa toàn bộ về cỡ 13 theo Thông tư 17/2025/TT-BTP
  hay không; không dùng làm căn cứ trượt phiếu.
- Không tạo, không sửa dữ liệu nghiệp vụ nào khi đo phiếu này — chỉ xem và xuất báo cáo (2 lần).
