# DGHQHTPL_06 (dòng 214) — BC Đánh giá hiệu quả HTPL · Xuất Excel

**Verdict logic: Pass** → ô "Trạng thái dev fix" = `Test done`.

| | |
|---|---|
| Đo lúc | 2026-08-07 10:01 giờ VN |
| Env | `https://18.143.165.120.nip.io` (nội bộ) |
| Bó mã FE | `assets/index-eWHwDgt2.js` (deploy 09:11 giờ VN 07/08) |
| Nhãn màn | HTPLDN · V1.0.10 |
| Tài khoản | `admin` (QTHT/TW) — vai trò ra verdict · `cbnv_tw_03` (CB NV/TW) — vế chống hồi quy |
| Nguồn canonical | khối `CÁCH VERIFY` / `VERIFY LẠI` trong ô "Kết quả verify" của chính dòng 214 (vòng 06/08) |

## Vế đã đo

| Vế | Nội dung | SRS | Kết quả |
|---|---|---|---|
| **C2** | QTHT không vào được màn báo cáo | `srs-fr-11-bao-cao.md:79` · `srs-v3.5.md:684` (M-05) | ✅ **ĐẠT** |
| **C1** | QTHT không xuất được tệp | `srs-fr-11-bao-cao.md:51` · `:62` | ✅ **ĐẠT** |
| **C3a** | Câu từ chối bằng tiếng Việt, không lộ chuỗi kỹ thuật | `srs-fr-11-bao-cao.md:117` | ✅ **ĐẠT** |
| **C4** | CB Nghiệp vụ TW vẫn xuất được, tệp mở đọc được, số khớp màn | `:124` · `:85` | ✅ **ĐẠT** |

## C2 · C1 · C3a — vai trò Quản trị hệ thống

Bằng chứng dùng chung cho cả 14 phiếu cùng lỗi gốc:
[`image/F7-QTHT-chan-tu-cua-vao-phan-hoi-may-chu.txt`](../image/F7-QTHT-chan-tu-cua-vao-phan-hoi-may-chu.txt) ·
[`image/F7-00-admin-sidebar-khong-con-muc-Bao-cao-thong-ke.png`](../image/F7-00-admin-sidebar-khong-con-muc-Bao-cao-thong-ke.png)

- `GET /api/v1/auth/me` → `vaiTro:["QTHT"]`, `capDonVi:"TW"` ⇒ đúng vai trò trong ảnh nghiệm thu.
- Menu: liệt kê **33 mục** của thanh điều hướng — **không có** "Báo cáo thống kê" (`cbnv_tw_03` liệt kê 29 mục thì **có**, đúng vị trí cũ giữa "Đợt báo cáo" và "Quản trị hệ thống"). ⇒ ẩn theo vai trò, không phải làm mờ, không phải gỡ khỏi phần mềm.
- Gõ thẳng `https://18.143.165.120.nip.io/bao-cao` → bị đẩy về `/dashboard`.
- Máy chủ chặn ở **bước Xem**, không phải bước Xuất: `GET /bao-cao/loai` · `/bao-cao/chi-phi-chi-tra` · `/bao-cao/so-luong-ct-ho-tro` đều **403** với `ERR-RPT-05` — *"Bạn không có quyền xem báo cáo này"*.
- Chuỗi `"Forbidden"` và mã `ERR-PERM-SYS-00-01` **không còn xuất hiện**.

## C4 — chống hồi quy bằng `cbnv_tw_03`

Đường UI thật: menu [Báo cáo thống kê] → Loại "BC Đánh giá hiệu quả HTPL" → Kỳ "Năm"
(01/01/2026 → 31/12/2026) → Đơn vị "Toàn quốc" → **[Xem báo cáo]** → **[Xuất Excel]**.

| Chỉ tiêu | Trên màn | Trong tệp | Khớp |
|---|---|---|---|
| Tổng đợt đánh giá | 4 | `B8 = 4` | ✅ |
| Tổng lượt đánh giá | 8 | `B12 = 8` | ✅ |
| Tổng vụ việc đã đánh giá | 7 | `B16 = 7` | ✅ |
| Bộ Kế hoạch và Đầu tư — Điểm TB/lượt/vụ việc | 80,0 / 1 / 1 | `B24=80 · C24=1 · D24=1` | ✅ |
| Cục Bổ trợ tư pháp | 28,7 / 4 / 4 | `B25=28.65 · C25=4 · D25=4` | ✅ |
| Sở Tư pháp Hà Nội | 25,5 / 3 / 2 | `B26=25.53 · C26=3 · D26=2` | ✅ |

- `GET /api/v1/bao-cao/danh-gia-hieu-qua?kyBaoCao=NAM&tuNgay=2026-01-01&denNgay=2026-12-31` → **200**.
- `POST /api/v1/bao-cao/export` → **200**; tệp giao ra `BaoCaoDanhGiaHieuQua_20260807_1001.xlsx`, 7.615 byte.
- **Đã mở tệp ra đọc** (giải nén ngay trong trình duyệt, đọc `workbook.xml` + `sharedStrings.xml` + `sheet1.xml`): tên trang tính `BC Đánh giá hiệu quả`, 93 ô có giá trị.
- 4 mục đầu tệp đủ: `A1` tên báo cáo · `A2` *"Kỳ báo cáo: Năm (từ 01/01/2026 đến 31/12/2026)"* ·
  `A3` *"Đơn vị: Toàn quốc"* · `A4` *"Ngày tạo: 07/08/2026"*.
- Bảng theo đơn vị cộng dọc đúng: lượt đánh giá 1+4+3 = 8 · vụ việc 1+4+2 = 7 = số tổng.
- Điểm TB theo đơn vị trong tệp là số đầy đủ (28.65 · 25.53), trên màn làm tròn 1 chữ số (28,7 · 25,5) — cùng một giá trị.
- **Ghi nhận lại, không tính vào phiếu này:** thẻ "Điểm trung bình chung" trên màn hiện `33` trong khi tệp là `33.9`. Hiện tượng này đã được ghi ở lượt đo 06/08 và vẫn còn; đặc tả không quy định số chữ số thập phân của thẻ tổng nên để dạng ứng viên, chưa lập phiếu.
- Tên tệp khớp khuôn `{TênBáoCáo}_{YYYYMMDD_HHmm}` đã chốt 04/08.

## Phần KHÔNG đo lại (và vì sao)

Vòng 06/08 đã ghi rõ ở khối "ĐÃ HẾT LỖI" rằng vai trò CB Nghiệp vụ xuất tốt ở 8 lượt xuất với các bộ lọc khác nhau. FLOW 03
§Chạy bước 1 cấm chạy lại vế đã được kết quả gần nhất ghi là đã đạt. Lô này chỉ chạy lại **1 cấu hình
lọc** đúng mục đích bước B4 của khối canonical ("để chắc vai trò này không bị chặn theo") — cộng thêm
mở tệp ra đọc vì đó là bẫy được chính khối đó nêu đích danh. Các cấu hình còn lại **không đo lại**.
