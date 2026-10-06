# CPCTHTTLHDN_06 (dòng 258) — BC Chi phí theo loại hình DN · Xuất Excel

**Verdict logic: Pass** → ô "Trạng thái dev fix" = `Test done`.

| | |
|---|---|
| Đo lúc | 2026-08-07 10:09–10:10 giờ VN |
| Env | `https://18.143.165.120.nip.io` (nội bộ) |
| Bó mã FE | `assets/index-eWHwDgt2.js` (deploy 09:11 giờ VN 07/08) |
| Nhãn màn | HTPLDN · V1.0.10 |
| Tài khoản | `admin` (QTHT/TW) — vai trò ra verdict · `cbnv_tw_03` (CB NV/TW) — vế chống hồi quy |
| Nguồn canonical | khối `CÁCH VERIFY` / `VERIFY LẠI` trong ô "Kết quả verify" của chính dòng 258 (vòng 06/08) |

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

Đường UI thật: menu [Báo cáo thống kê] → Loại "BC Chi phí theo loại hình DN" → Kỳ "Năm"
(01/01/2026 → 31/12/2026) → Đơn vị "Toàn quốc" → **[Xem báo cáo]** → **[Xuất Excel]**.

| Chỉ tiêu | Trên màn | Trong tệp | Khớp |
|---|---|---|---|
| Tổng hồ sơ | 2 | `B8 = 2` | ✅ |
| Tổng chi phí | 23.000.000 ₫ | `B12 = 23000000` | ✅ |
| Nhỏ — 6 ô nghiệp vụ | 1 · 15.000.000 ₫ · 30,0 · 30.000.000 ₫ · 30.000.000 ₫ · −15.000.000 ₫ | `B16..G16 = 1 · 15000000 · 30 · 30000000 · 30000000 · -15000000` | ✅ |
| Siêu nhỏ — 6 ô nghiệp vụ | 1 · 8.000.000 ₫ · 100,0 · 30.000.000 ₫ · 30.000.000 ₫ · −22.000.000 ₫ | `B17..G17 = 1 · 8000000 · 100 · 30000000 · 30000000 · -22000000` | ✅ |

- `GET /api/v1/bao-cao/chi-phi-theo-loai-dn?kyBaoCao=NAM&tuNgay=2026-01-01&denNgay=2026-12-31` → **200**.
- `POST /api/v1/bao-cao/export` → **200**; tệp giao ra `BaoCaoChiPhiTheoLoaiDn_20260807_1009.xlsx`, 6.822 byte.
- **Đã mở tệp ra đọc** (giải nén ngay trong trình duyệt, đọc `workbook.xml` + `sharedStrings.xml` + `sheet1.xml`): tên trang tính `Chi phí theo loại DN`, 36 ô có giá trị.
- 4 mục đầu tệp đủ: `A1` tên báo cáo · `A2` *"Kỳ báo cáo: Năm (từ 01/01/2026 đến 31/12/2026)"* ·
  `A3` *"Đơn vị: Toàn quốc"* · `A4` *"Ngày tạo: 07/08/2026"*.
- **Đủ cả 7 cột nghiệp vụ** mà khối canonical đòi (thiếu bất kỳ cột nào là FAIL): `A15` Quy mô DN ·
  `B15` Số hồ sơ · `C15` Tổng chi phí (₫) · `D15` Mức hỗ trợ (%) · `E15` Trần / hồ sơ (₫) ·
  `F15` Trần chi phí (₫) · `G15` Chênh lệch (₫). Đếm được 7/7.
- Cột **Chênh lệch âm** (−15.000.000 và −22.000.000): đúng bẫy số 3 của khối canonical (chi phí chưa
  chạm trần theo Nghị định 55) — **không chấm Fail**.
- **Biến thể B4 nêu đích danh — chọn Loại DN = quy mô CÓ dữ liệu:** chọn "Nhỏ" →
  `GET …&loaiDn=NHO` → **200**; màn còn đúng 1 dòng (Tổng hồ sơ **1** · Tổng chi phí **15.000.000 ₫**),
  tệp thứ hai `BaoCaoChiPhiTheoLoaiDn_20260807_1010.xlsx` 6.767 byte / 29 ô có `B8 = 1`, `B12 = 15000000`,
  chỉ còn dòng `A16 = Nhỏ` ⇒ **tệp khớp màn sau khi lọc**, bộ lọc có tác dụng thật cả trên màn lẫn trong tệp.
- Tên tệp khớp khuôn `{TênBáoCáo}_{YYYYMMDD_HHmm}` đã chốt 04/08.

## Phần KHÔNG đo lại (và vì sao)

Vòng 06/08 đã ghi rõ ở khối "ĐÃ HẾT LỖI" rằng vai trò CB Nghiệp vụ xuất tốt ở 3 cấu hình Loại DN, và
FLOW 03 §Chạy bước 1 cấm chạy lại vế đã được kết quả gần nhất ghi là đã đạt. Lô này chạy lại **2/3 cấu
hình**: cấu hình gốc B1 (để trống ô Loại DN) + biến thể mà bước B4 **nêu đích danh** ("chọn Loại DN =
quy mô CÓ dữ liệu") — biến thể được nguồn canonical gọi tên thì không được bỏ. Cộng thêm mở tệp ra đọc
vì đó là bẫy số 2 của chính khối đó.

**Không đo lại:** cấu hình Loại DN = "Siêu nhỏ" (vòng 06/08 đã ghi đạt, và biến thể B4 chỉ đòi **một**
quy mô có dữ liệu — đã dùng "Nhỏ"); các loại báo cáo khác (mỗi loại là một phiếu riêng); các kỳ báo cáo
ngoài Kỳ Năm 2026.

**Không chấm trong phiếu này:** việc xếp quy mô doanh nghiệp — đã tách phiếu `BCTK_QA05` (dòng 368),
đúng như bẫy số 3 của khối canonical dặn.
