# CLDTBDPL_07 — đo lại trên môi trường nghiệm thu đối tác (05/08/2026)

Tiêu chí lấy nguyên khối ở cột `DEV phản hồi lần 2`, dòng 238 (tab `UAT_TGPL Doanh Nghiệp-tuần 3`).

| Điều kiện | Bug gốc (khối tiêu chí) | Mình test | GAP? |
|---|---|---|---|
| Môi trường | Bản mới nhất của môi trường nghiệm thu | `https://htpldn-uat.ospgroup.vn` — nhãn `HTPLDN · V1.0.7` | Không |
| Vai trò | `cbnv_tw` | `cbnv_tw` · CB_NV_TW · cấp TW · Cục Bổ trợ tư pháp | Không |
| Loại báo cáo | Báo cáo chất lượng đào tạo | `BC Chất lượng đào tạo`, kỳ `Năm` (01/01/2026 – 31/12/2026), đơn vị `Toàn quốc` | Không |
| Bảng phải kiểm | "Danh sách khóa học" trong tệp PDF — đủ 6 cột, có cột "Tỷ lệ đạt (%)" | Đọc nội dung thật của tệp: bảng có đúng 6 cột, cột thứ 6 là "Tỷ lệ đạt (%)" | Không |
| Đối chiếu số liệu | Khớp màn hình ở mọi khóa học trong kỳ | Đối chiếu từng dòng tệp với từng dòng bảng trên màn — khớp **5/5 khóa** (kỳ này có 5 khóa, dev đo lúc có 7) | Không |
| Lặp lần 2 | Xuất lại lần 2 với đúng điều kiện lọc cũ, tệp vẫn đủ cột và đúng số liệu | Xuất lại lần nữa, giữ nguyên điều kiện lọc, **so nội dung hai tệp bằng cách đọc chữ trong tệp** — giống hệt nhau | Không |
| Xuất tệp | Không còn thông báo chặn | Cả 3 lần xuất đều ra tệp, không có thông báo lỗi | Không |
| Tên tệp | Có đủ ngày và giờ-phút, không đè nhau | `BaoCaoChatLuongDaoTao_20260805_1640.pdf` · `…_1641.pdf` · `…_1642.pdf` — ba tên khác nhau | Không |

**Kết luận: 0 GAP → PASS.**

## Đối chiếu từng ý của khối tiêu chí

- **Tệp xuất được, không còn báo lỗi**: bấm [Xuất PDF] → [Xuất file] ra tệp **37 615 byte, 2 trang**.
  Thông báo "Không thể tạo file xuất. Vui lòng thử lại." của phản ánh gốc **không còn**.
- **Bảng "Danh sách khóa học" có đủ 6 cột, đã có cột "Tỷ lệ đạt (%)"**: dòng tiêu đề trong tệp đọc được là
  `Mã khóa học · Tên khóa học · Đơn vị · Số học viên · Điểm TB · Tỷ lệ đạt (%)`.
- **Số liệu cột "Tỷ lệ đạt" khớp màn hình ở mọi khóa trong kỳ** — đối chiếu từng dòng:

  | Mã khóa học | Trên màn (Số HV · Điểm TB · Tỷ lệ đạt) | Trong tệp PDF | Khớp? |
  |---|---|---|---|
  | `KH-20260703-005` | 2 · 7,5 · 50% | 2 · 7,5 · 50,0 | Khớp |
  | `KH-20260703-007` | 1 · 10,0 · 0% | 1 · 10,0 · 0,0 | Khớp |
  | `KH-20260509-001` | 1 · 8,5 · 100% | 1 · 8,5 · 100,0 | Khớp |
  | `KH-HDSD-AG-003` | 5 · 7,2 · 80% | 5 · 7,2 · 80,0 | Khớp |
  | `KH-20260509-005` | 5 · 6,5 · 60% | 5 · 6,5 · 60,0 | Khớp |

  Bốn ô tổng hợp cũng khớp: Tổng số khóa học 5 · Tổng số học viên 14 · Điểm trung bình chung 7,94 ·
  Tỷ lệ đạt tổng 58,0%.
- **Không phải ngẫu nhiên một lần**: xuất lại lần nữa với đúng điều kiện lọc cũ → tệp thứ hai
  **giống hệt tệp thứ nhất về nội dung chữ** (so nguyên văn sau khi chuẩn hóa khoảng trắng) và cùng kích
  thước 37 615 byte; vẫn đủ 6 cột, vẫn đúng số liệu.
- **Tên tệp có đủ ngày và giờ-phút, hai lần xuất trong ngày không đè nhau**: ba lần xuất ra
  `BaoCaoChatLuongDaoTao_20260805_1640.pdf`, `…_1641.pdf`, `…_1642.pdf`.
- **Phần khuôn mẫu vẫn giữ**: khổ `595,28 × 841,89` điểm (A4 dọc), phông `Tinos-*` (cùng số đo Times New
  Roman), đầu trang có `CỤC BỔ TRỢ TƯ PHÁP - BỘ TƯ PHÁP` + quốc hiệu + tiêu ngữ, cuối trang có
  `Ngày 05 tháng 08 năm 2026` · `NGƯỜI XUẤT BÁO CÁO` · `(Ký, ghi rõ họ tên và đóng dấu)` ·
  `Cán bộ NV Trung ương`; đủ bốn mục tên báo cáo / kỳ báo cáo / đơn vị / ngày tạo.

Tệp đo: `../evidence/CLDTBDPL_07-uat.pdf` (lần 1) · `../evidence/CLDTBDPL_07-uat-lan3.pdf` (lần đối chứng)

## Ghi nhận thêm

- Dev đo lúc kỳ báo cáo có **7 khóa học**, hiện tại kỳ này có **5 khóa** — chênh do dữ liệu thay đổi giữa
  hai lượt đo, không ảnh hưởng kết luận vì đã đối chiếu **toàn bộ** khóa đang có, không lấy mẫu.
- Cỡ chữ trong bảng số liệu là 11 (tiêu đề và dòng hành chính cỡ 13–14) — giống mọi báo cáo khác của nhóm
  này; đã ghi chi tiết ở `cond/SLHDVM_07-uat.md`, không dùng làm căn cứ trượt.
- Không tạo, không sửa dữ liệu nghiệp vụ nào khi đo phiếu này — chỉ xem và xuất báo cáo (3 lần).
