# CPCTHTTDVQL_06 (dòng 243) — BC Chi phí theo đơn vị · Xuất Excel

**Verdict logic: Pass** → ô "Trạng thái dev fix" = `Test done`.

| | |
|---|---|
| Đo lúc | 2026-08-07 10:03–10:05 giờ VN |
| Env | `https://18.143.165.120.nip.io` (nội bộ) |
| Bó mã FE | `assets/index-eWHwDgt2.js` (deploy 09:11 giờ VN 07/08) |
| Nhãn màn | HTPLDN · V1.0.10 |
| Tài khoản | `admin` (QTHT/TW) — vai trò ra verdict · `cbnv_tw_03` (CB NV/TW) — vế chống hồi quy |
| Nguồn canonical | khối `CÁCH VERIFY` / `VERIFY LẠI` trong ô "Kết quả verify" của chính dòng 243 (vòng 06/08) |

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

Đường UI thật: menu [Báo cáo thống kê] → Loại "BC Chi phí theo đơn vị" → Kỳ "Năm"
(01/01/2026 → 31/12/2026) → Đơn vị "Toàn quốc" → **[Xem báo cáo]** → **[Xuất Excel]**.

| Chỉ tiêu | Trên màn | Trong tệp | Khớp |
|---|---|---|---|
| Tổng hồ sơ | 2 | `B8 = 2` | ✅ |
| Tổng chi phí | 23.000.000 ₫ | `B12 = 23000000` | ✅ |
| Cục Bổ trợ tư pháp — số hồ sơ | 2 | `B16 = 2` | ✅ |
| Cục Bổ trợ tư pháp — tổng chi phí | 23.000.000 ₫ | `C16 = 23000000` | ✅ |
| Cục Bổ trợ tư pháp — trung bình chi phí | 11.500.000 ₫ | `D16 = 11500000` | ✅ |

- `GET /api/v1/bao-cao/chi-phi-theo-don-vi?kyBaoCao=NAM&tuNgay=2026-01-01&denNgay=2026-12-31` → **200**.
- `POST /api/v1/bao-cao/export` → **200**; tệp giao ra `BaoCaoChiPhiTheoDonVi_20260807_1003.xlsx`, 6.677 byte.
- **Đã mở tệp ra đọc** (giải nén ngay trong trình duyệt, đọc `workbook.xml` + `sharedStrings.xml` + `sheet1.xml`): tên trang tính `Chi phí theo đơn vị`, 23 ô có giá trị.
- 4 mục đầu tệp đủ: `A1` tên báo cáo · `A2` *"Kỳ báo cáo: Năm (từ 01/01/2026 đến 31/12/2026)"* ·
  `A3` *"Đơn vị: Toàn quốc"* · `A4` *"Ngày tạo: 07/08/2026"*.
- Bảng chéo đủ **4 cột** mà khối canonical đòi: `A15` Đơn vị · `B15` Số hồ sơ · `C15` Tổng chi phí (₫) ·
  `D15` Trung bình chi phí (₫). Số dòng đơn vị trong tệp = số dòng trên màn (1 dòng — env thử chỉ
  phát sinh chi phí ở một đơn vị, đúng bẫy số 3 của khối canonical, không chấm Fail vì việc này).
- **Biến thể B4 nêu đích danh — đổi Đơn vị sang một đơn vị cụ thể:** chọn "Cục Bổ trợ tư pháp - Bộ Tư
  pháp (BTP-TW)" → `GET …&donViId=00000000-0000-4000-8000-000000000001` → **200**; tệp thứ hai
  `BaoCaoChiPhiTheoDonVi_20260807_1004.xlsx`, 6.670 byte (khác tệp đầu 6.677 byte). Dòng `A3` trong
  tệp **đổi theo** từ *"Đơn vị: Toàn quốc"* → *"Đơn vị: Cục Bổ trợ tư pháp - Bộ Tư pháp"* ⇒ tệp bám
  bộ lọc, không xuất cứng.
- Tên tệp khớp khuôn `{TênBáoCáo}_{YYYYMMDD_HHmm}` đã chốt 04/08.

## Phần KHÔNG đo lại (và vì sao)

Vòng 06/08 đã ghi rõ ở khối "ĐÃ HẾT LỖI" rằng vai trò CB Nghiệp vụ xuất tốt ở cả 2 cấu hình bộ lọc, và
FLOW 03 §Chạy bước 1 cấm chạy lại vế đã được kết quả gần nhất ghi là đã đạt. **Riêng phiếu này vẫn chạy
lại đủ cả 2 cấu hình** vì bước B4 của khối canonical nêu đích danh biến thể "đổi Đơn vị sang một đơn vị
cụ thể" như một phép đo bắt buộc — biến thể được nguồn canonical gọi tên thì không được bỏ. Cộng thêm mở
tệp ra đọc vì đó là bẫy số 2 của chính khối đó. **Không có cấu hình nào của phiếu này bị bỏ đo.**

Phần **không** đo lại: các loại báo cáo khác (mỗi loại là một phiếu riêng trong lô) và các kỳ báo cáo
ngoài Kỳ Năm 2026 — vòng 06/08 không nêu chúng ở phiếu này.
