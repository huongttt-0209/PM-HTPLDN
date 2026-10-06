# CTTDVQL_04 (dòng 272) — BC Chương trình theo đơn vị · Xuất Excel

**Verdict logic: Pass** → ô "Trạng thái dev fix" = `Test done`.

| | |
|---|---|
| Đo lúc | 2026-08-07 10:29 giờ VN |
| Env | `https://18.143.165.120.nip.io` (nội bộ) |
| Bó mã FE | `assets/index-eWHwDgt2.js` (deploy 09:11 giờ VN 07/08) |
| Nhãn màn | HTPLDN · V1.0.10 |
| Tài khoản | `admin` (QTHT/TW) — vai trò ra verdict · `cbnv_tw_03` (CB NV/TW) — vế chống hồi quy |
| Nguồn canonical | khối `CÁCH VERIFY` / `VERIFY LẠI` trong ô "Kết quả verify" của chính dòng 272 (vòng 06/08) |

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

Đường UI thật: menu [Báo cáo thống kê] → Loại "BC Chương trình theo đơn vị" → Kỳ "Năm"
(01/01/2026 → 31/12/2026) → Đơn vị "Toàn quốc" → **[Xem báo cáo]** → **[Xuất Excel]**.

| Chỉ tiêu | Trên màn | Trong tệp | Khớp |
|---|---|---|---|
| Tổng chương trình | 7 | `B8 = 7` | ✅ |
| Tổng ngân sách | 350.000.000 ₫ | `B12 = 350000000` | ✅ |
| Cục Bổ trợ tư pháp — cấp đơn vị | TW | `B16 = TW` | ✅ |
| Cục Bổ trợ tư pháp — số chương trình | 7 | `C16 = 7` | ✅ |
| Cục Bổ trợ tư pháp — tổng ngân sách | 350.000.000 ₫ | `D16 = 350000000` | ✅ |

- `GET /api/v1/bao-cao/ct-theo-don-vi?kyBaoCao=NAM&tuNgay=2026-01-01&denNgay=2026-12-31` → **200**.
- `POST /api/v1/bao-cao/export` → **200**; tệp giao ra `BaoCaoCtTheoDonVi_20260807_1029.xlsx`, 6.693 byte.
- **Đã mở tệp ra đọc** (giải nén ngay trong trình duyệt, đọc `workbook.xml` + `sharedStrings.xml` + `sheet1.xml`): tên trang tính `Chương trình theo đơn vị`, 23 ô có giá trị.
- 4 mục đầu tệp đủ: `A1` tên báo cáo · `A2` *"Kỳ báo cáo: Năm (từ 01/01/2026 đến 31/12/2026)"* ·
  `A3` *"Đơn vị: Toàn quốc"* · `A4` *"Ngày tạo: 07/08/2026"*.
- **Giữ đủ chiều đơn vị cùng hai cột bắt buộc** — điều kiện "không hỏng phần cũ" của khối canonical:
  bảng chéo có `A15` Đơn vị · `B15` Cấp đơn vị · `C15` Số chương trình · `D15` Tổng ngân sách (₫).
- Cộng dọc bằng đúng hai thẻ tổng: 7 = 7 và 350.000.000 = 350.000.000 (env thử chỉ có một đơn vị
  phát sinh chương trình).
- **Tài khoản dùng cho vế chống hồi quy:** khối canonical (Bước 4) nêu `cbnv_tw_04`; lượt này dùng
  `cbnv_tw_03` — **cùng vai trò CB Nghiệp vụ, cùng cấp TW, cùng đơn vị**, đúng phạm vi thay thế mà
  quy tắc dự phòng tài khoản cho phép. Ghi rõ ở đây để đối tác biết tài khoản thực dùng.
- Mục [4] của vòng 06/08 (tên tệp `BaoCaoCtTheoDonVi_…` không phải chuỗi `BaoCaoChuongTrinh`) đã kết
  luận **không phải lỗi** — lượt này giữ nguyên kết luận đó, không chấm lại.
- Báo cáo này **không có** bảng "Thống kê theo kỳ", nên việc ghi nhận ở phiếu `SLCTHT_06` không liên
  quan tới phiếu này.
- Tên tệp khớp khuôn `{TênBáoCáo}_{YYYYMMDD_HHmm}` đã chốt 04/08.

## Phần KHÔNG đo lại (và vì sao)

Vòng 06/08 đã ghi rõ ở mục [2] rằng vai trò CB Nghiệp vụ xuất tốt, đã thử 4 cấu hình bộ lọc, và FLOW 03
§Chạy bước 1 cấm chạy lại vế đã được kết quả gần nhất ghi là đã đạt. Bước 4 của khối canonical chỉ đòi
"làm lại bước 1–3" mà **không nêu đích danh biến thể lọc nào**, nên chỉ chạy lại **1 cấu hình** đúng như
Bước 1 mô tả (Kỳ Năm 01/01–31/12/2026 · Toàn quốc) — cộng thêm mở tệp ra đọc vì đó là bẫy số 2.

**Không đo lại:** 3 cấu hình lọc còn lại của vòng 06/08 (Năm + lọc một đơn vị · Khoảng 01.02–31.12.2026
+ Toàn quốc · một đơn vị không có dữ liệu); các loại báo cáo khác.

**Không chấm lại:** tên tệp — mục [4] của vòng 06/08 đã kết luận không phải lỗi (đặc tả `:85` chỉ quy
định khuôn `{TênTệp}_{YYYYMMDD_HHmm}`, không ấn định chuỗi `BaoCaoChuongTrinh`).

**Vẫn để ngỏ, không thuộc phiếu này:** mục [7] của vòng 06/08 — kỳ "Khoảng tùy chọn" in mã nội bộ
`KHOANG` trong tệp Excel. Lượt đo hôm nay dùng kỳ "Năm" nên không chạm tới việc đó; nó trùng nội dung
với phiếu `BCTK_QA09` (dòng 372) và vẫn đang chờ nghiệp vụ chốt.
