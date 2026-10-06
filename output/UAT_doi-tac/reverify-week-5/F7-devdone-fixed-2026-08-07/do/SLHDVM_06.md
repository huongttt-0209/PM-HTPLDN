# SLHDVM_06 (dòng 174) — BC Số lượng hỏi đáp/vướng mắc PL · Xuất Excel

**Verdict logic: Pass** → ô "Trạng thái dev fix" = `Test done`.

| | |
|---|---|
| Đo lúc | 2026-08-07 09:48–09:54 giờ VN |
| Env | `https://18.143.165.120.nip.io` (nội bộ) |
| Bó mã FE | `assets/index-eWHwDgt2.js` (deploy 09:11 giờ VN 07/08) |
| Nhãn màn | HTPLDN · V1.0.10 |
| Tài khoản | `admin` (QTHT/TW) — vai trò ra verdict · `cbnv_tw_03` (CB NV/TW) — vế chống hồi quy |
| Nguồn canonical | khối `VERIFY LẠI` trong ô "Kết quả verify" của chính dòng 174 (vòng 06/08) |

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

Đường UI thật: menu [Báo cáo thống kê] → Loại "BC Số lượng hỏi đáp/vướng mắc pháp luật" → Kỳ "Năm"
(01/01/2026 → 31/12/2026) → Đơn vị "Toàn quốc" → **[Xem báo cáo]** → **[Xuất Excel]**.

| Chỉ tiêu | Trên màn | Trong tệp | Khớp |
|---|---|---|---|
| Tổng hỏi đáp | 22 | `B8 = 22` | ✅ |
| Đã trả lời | 11 | `B12 = 11` | ✅ |
| Chờ trả lời | 11 | `B16 = 11` | ✅ |
| Tỷ lệ trả lời | 50.0% | `B20 = 50` | ✅ |
| Thương mại | 13 | `B24 = 13` | ✅ |
| Thuế | 8 | `B25 = 8` | ✅ |
| Lao động | 1 | `B26 = 1` | ✅ |

- `GET /api/v1/bao-cao/hoi-dap?kyBaoCao=NAM&tuNgay=2026-01-01&denNgay=2026-12-31` → **200**.
- `POST /api/v1/bao-cao/export` → **200**; tệp giao ra `BaoCaoHoiDap_20260807_0954.xlsx`, 6.967 byte,
  kiểu `application/vnd.openxmlformats-officedocument.spreadsheetml.sheet`.
- **Đã mở tệp ra đọc** (giải nén ngay trong trình duyệt, đọc `workbook.xml` + `sharedStrings.xml` +
  `sheet1.xml`): tên trang tính `BC Số lượng hỏi đáp`, 40 ô có giá trị.
- 4 mục đầu tệp đủ: `A1` tên báo cáo · `A2` *"Kỳ báo cáo: Năm (từ 01/01/2026 đến 31/12/2026)"* ·
  `A3` *"Đơn vị: Toàn quốc"* · `A4` *"Ngày tạo: 07/08/2026"*.
- Bảng theo đơn vị cộng dọc đúng: Cục Bổ trợ tư pháp 21 + Sở Tư pháp Hà Nội 1 = 22 = số tổng.
- Tên tệp khớp khuôn `{TênBáoCáo}_{YYYYMMDD_HHmm}.xlsx` đã chốt 04/08.

## Phần KHÔNG đo lại (và vì sao)

Vòng 06/08 đã ghi rõ ở khối "ĐÃ HẾT LỖI" rằng vai trò CB Nghiệp vụ xuất tốt cả **3 bộ lọc**. FLOW 03
§Chạy bước 1 cấm chạy lại vế đã được kết quả gần nhất ghi là đã đạt. Lô này chỉ chạy lại **1 cấu hình
lọc** làm phép chống hồi quy đúng mục đích bước B4 của khối `VERIFY LẠI` ("để chắc vai trò này không bị
chặn theo") — cộng thêm mở tệp ra đọc vì đó là bẫy số 2 của chính khối đó. Hai bộ lọc còn lại **không
đo lại**.
