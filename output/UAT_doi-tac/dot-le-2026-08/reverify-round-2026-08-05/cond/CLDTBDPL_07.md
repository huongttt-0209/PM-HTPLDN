# Bảng đối chiếu điều kiện — CLDTBDPL_07 (re-verify vòng 2, 05/08/2026)

Loại bug: **thiếu một cột dữ liệu trong bảng của tệp PDF xuất ra** → phụ thuộc dữ liệu thật của báo cáo ⇒ bắt buộc điền bảng đối chiếu, 0 GAP.
Ô note của dòng này (*DEV phản hồi lần 2*) KHÔNG có khối `── CÁCH VERIFY sau Dev fix ──`, nên lấy phần **"Phần còn lỗi"** (tệp PDF thiếu cột "Tỷ lệ đạt" trong bảng "Danh sách khóa học") làm điều kiện phải hết lỗi; phần **"đã chạy được, không còn Forbidden, tạo và tải được tệp"** là mốc đã đạt, vẫn kiểm lại để chắc không hồi quy.

| Điều kiện | Bug gốc (note vòng 2) | Mình test | GAP? |
|---|---|---|---|
| Môi trường | Môi trường bàn giao, bản dựng đang chạy | `https://18.143.165.120.nip.io` — bản dựng **HTPLDN · V1.0.6** (đọc ở thanh bên trái) | Không |
| Vai trò | Tài khoản xem được Báo cáo thống kê | `cbnv_tw` · CB Nghiệp vụ - Trung ương · CB_NV_TW · BTP · TW | Không |
| Màn hình | Báo cáo thống kê | Báo cáo thống kê (`/bao-cao`) | Không |
| Loại báo cáo | BC Chất lượng đào tạo | **BC Chất lượng đào tạo** (chọn đúng tên, không chọn loại gần giống) | Không |
| Kỳ báo cáo | Năm 2026 | **Năm** — Từ 01/01/2026 đến 31/12/2026 | Không |
| Đơn vị | Toàn quốc | **Toàn quốc** | Không |
| Khổ giấy / hướng giấy | A4 dọc (mặc định) | **A4 · Dọc** (giữ mặc định trong hộp thoại *Tùy chọn in báo cáo PDF*) | Không |
| Tiền đề dữ liệu | Có dữ liệu thống kê để bảng "Danh sách khóa học" có dòng | Bấm **Xem báo cáo** ra **7 khóa học** (Thời điểm tạo 05/08/2026 01:53), đủ dòng để đọc cột | Không |
| Thao tác sinh ra lỗi cũ | Bấm Xuất PDF rồi xuất tệp thật | Bấm **Xuất PDF** → hộp thoại → bấm **Xuất file** → tệp được tạo thật (không chấm bằng quan sát tĩnh) | Không |
| Cách đọc nội dung tệp | Đối chiếu bảng trong tệp với bảng trên màn hình | Bắt tệp ngay lúc trình duyệt tạo, giải mã ra tệp PDF rồi **đọc chữ bên trong tệp** + đối chiếu từng dòng với bảng trên màn | Không |
| Số lần xuất | Note nói đã xuất 2 lần cùng điều kiện, đều thiếu cột | Xuất **2 lần** cùng điều kiện lọc (01:54 và 01:56) để loại trừ ngẫu nhiên | Không |

**Kết luận: 0 GAP** — đúng bản dựng đang chạy, đúng vai trò, đúng loại báo cáo, đúng kỳ và đơn vị, đúng khổ giấy mặc định, có dữ liệu thật, đã bấm xuất tệp thật và đọc nội dung bên trong tệp.

## Đo lường trực tiếp (05/08/2026, `18.143.165.120.nip.io`, bản dựng V1.0.6)

### Phần "còn lỗi" của note — bảng "Danh sách khóa học" trong tệp PDF thiếu cột "Tỷ lệ đạt"

- ✅ **Tệp PDF nay CÓ đủ cột "Tỷ lệ đạt (%)"** → bảng "Danh sách khóa học" trong tệp có đúng **6 cột**: Mã khóa học · Tên khóa học · Đơn vị · Số học viên · Điểm TB · **Tỷ lệ đạt (%)**. Không còn cảnh chỉ có 5 cột như lần trước.
- ✅ **Số liệu cột này khớp đúng với màn hình** → đối chiếu cả 7 dòng:
  - KH-20260716-002 — màn hình 0% · tệp 0,0
  - AAA-KH-DP — màn hình 0% · tệp 0,0
  - KH-2026-002 — màn hình 100% · tệp 100,0
  - AAA-KH-BN — màn hình 0% · tệp 0,0
  - KH-2026-001 — màn hình 100% · tệp 100,0
  - KH-SEED-0001 — màn hình 0% · tệp 0,0
  - AAA-KH-TW — màn hình 0% · tệp 0,0
- ✅ **Không phải ăn may một lần** → xuất lại lần thứ hai với đúng điều kiện lọc cũ (Năm 2026 · Toàn quốc · A4 dọc), tệp thứ hai vẫn có đủ cột "Tỷ lệ đạt (%)" và đúng số liệu.
- Ảnh bảng trên màn hình (6 cột, có "Tỷ lệ đạt"): [`../image/CLDTBDPL_07-r2-man-hinh-bang-6-cot.png`](../image/CLDTBDPL_07-r2-man-hinh-bang-6-cot.png)
- Ảnh màn sau khi xuất tệp: [`../image/CLDTBDPL_07-r2-sau-khi-xuat-pdf.png`](../image/CLDTBDPL_07-r2-sau-khi-xuat-pdf.png)
- Tệp đo được: [`../evidence/CLDTBDPL_07-r2.pdf`](../evidence/CLDTBDPL_07-r2.pdf) (lần 1) · [`../evidence/CLDTBDPL_07-r2-lan2.pdf`](../evidence/CLDTBDPL_07-r2-lan2.pdf) (lần 2)

### Phần "đã hết lỗi" của note — kiểm lại xem có hồi quy không

- ✅ Không còn thông báo chặn khi bấm Xuất PDF; hệ thống tạo và tải được tệp bình thường (cả 2 lần).
- ✅ Tên tệp có đủ ngày và giờ-phút: `BaoCaoChatLuongDaoTao_20260805_0154.pdf` (lần 1) và `BaoCaoChatLuongDaoTao_20260805_0156.pdf` (lần 2) — hai lần xuất cùng ngày ra hai tên khác nhau.
- ✅ Tệp đúng khổ A4 (595,28 × 841,89 điểm), 2 trang; đầu trang có quốc hiệu "CỘNG HÒA XÃ HỘI CHỦ NGHĨA VIỆT NAM" + "Độc lập - Tự do - Hạnh phúc" và tên cơ quan "CỤC BỔ TRỢ TƯ PHÁP - BỘ TƯ PHÁP"; có đủ tên báo cáo, "Kỳ báo cáo:", "Đơn vị:", "Ngày tạo:"; cuối tệp có "Ngày 05 tháng 08 năm 2026", "NGƯỜI XUẤT BÁO CÁO", "(Ký, ghi rõ họ tên và đóng dấu)" và tên tài khoản xuất.

### Kết luận

Ý duy nhất còn lỗi ở vòng trước — bảng "Danh sách khóa học" trong tệp PDF thiếu cột "Tỷ lệ đạt" — nay đã hết: tệp có đủ 6 cột, số liệu khớp màn hình, lặp lại 2 lần đều đúng; phần đã chạy được trước đó không hồi quy → **Pass**.

### Ghi nhận thêm (ngoài phạm vi phiếu — không tự thêm dòng mới vào sheet)

- Ô "Điểm trung bình" trên màn hình hiển thị **6**, trong khi tệp PDF ghi **6,35** ở mục "Điểm trung bình chung". Cùng một con số nhưng màn hình làm tròn về số nguyên, tệp giữ 2 chữ số thập phân. Không thuộc phạm vi phiếu này (phiếu chỉ về cột "Tỷ lệ đạt"), chỉ ghi lại để đối tác/BA biết.
- Trang 2 của tệp chỉ chứa phần ký tên ("NGƯỜI XUẤT BÁO CÁO"), phần "Ngày ... tháng ... năm ..." lại nằm cuối trang 1 — phần ký bị tách sang trang mới. Không thuộc phạm vi phiếu, chỉ ghi lại.
