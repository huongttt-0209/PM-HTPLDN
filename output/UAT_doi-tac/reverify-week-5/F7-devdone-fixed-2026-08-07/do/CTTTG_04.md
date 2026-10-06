# CTTTG_04 (dòng 281) — BC Chương trình theo thời gian · Xuất Excel

**Verdict logic: Pass** → ô "Trạng thái dev fix" = `Test done`.

| | |
|---|---|
| Đo lúc | 2026-08-07 10:32 giờ VN |
| Env | `https://18.143.165.120.nip.io` (nội bộ) |
| Bó mã FE | `assets/index-eWHwDgt2.js` (deploy 09:11 giờ VN 07/08) |
| Nhãn màn | HTPLDN · V1.0.10 |
| Tài khoản | `admin` (QTHT/TW) — vai trò ra verdict · `cbnv_tw_03` (CB NV/TW) — vế chống hồi quy |
| Nguồn canonical | khối `CÁCH VERIFY` / `VERIFY LẠI` trong ô "Kết quả verify" của chính dòng 281 (vòng 06/08) |

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

Đường UI thật: menu [Báo cáo thống kê] → Loại "BC Chương trình theo thời gian" → Kỳ "Năm"
(01/01/2026 → 31/12/2026) → Đơn vị "Toàn quốc" → **[Xem báo cáo]** → **[Xuất Excel]**.

| Chỉ tiêu | Trên màn | Trong tệp | Khớp |
|---|---|---|---|
| Tổng chương trình toàn kỳ | 6 | `B8 = 6` | ✅ |
| Tổng ngân sách toàn kỳ | 250.000.000 ₫ | `B16 = 250000000` | ✅ |
| Theo kỳ — Năm 2026 · từ ngày · đến ngày | 01/01/2026 · 31/12/2026 | `A20..C20 = Năm 2026 · 01/01/2026 · 31/12/2026` | ✅ |
| Theo kỳ — Năm 2026 · số chương trình | 6 | `D20 = 6` | ✅ |
| Theo kỳ — Năm 2026 · tổng ngân sách | 250.000.000 ₫ | `F20 = 250000000` | ✅ |

- `GET /api/v1/bao-cao/ct-theo-thoi-gian?kyBaoCao=NAM&tuNgay=2026-01-01&denNgay=2026-12-31` → **200**.
- `POST /api/v1/bao-cao/export` → **200**; tệp giao ra `BaoCaoCtTheoThoiGian_20260807_1032.xlsx`, 6.758 byte.
- **Đã mở tệp ra đọc** (giải nén ngay trong trình duyệt, đọc `workbook.xml` + `sharedStrings.xml` + `sheet1.xml`): tên trang tính `Chương trình theo thời gian`, 32 ô có giá trị.
- 4 mục đầu tệp đủ: `A1` tên báo cáo · `A2` *"Kỳ báo cáo: Năm (từ 01/01/2026 đến 31/12/2026)"* ·
  `A3` *"Đơn vị: Toàn quốc"* · `A4` *"Ngày tạo: 07/08/2026"*.
- **Đối chiếu TỪNG HÀNG kỳ** đúng như Bước 3 của khối canonical đòi — bảng "Theo kỳ" có đúng 1 hàng
  (`Năm 2026`), khớp cả nhãn kỳ, từ ngày, đến ngày và số chương trình.
- **Cộng dọc cột số chương trình bằng đúng số tổng:** 6 = ô `B8`.
- **Cùng một bó mã cho cả hai vai trò** — đúng bẫy số 3 của phiếu này: vế Quản trị hệ thống đo lúc
  09:48 và vế Cán bộ Nghiệp vụ đo lúc 10:32 đều trên `assets/index-eWHwDgt2.js`, không có deploy xen
  giữa (xem [`../BAN-DUNG.md`](../BAN-DUNG.md)).
- Mục [4] của vòng 06/08 (tên tệp `BaoCaoCtTheoThoiGian_…`) đã kết luận **không phải lỗi** — giữ nguyên.
- Tên tệp khớp khuôn `{TênBáoCáo}_{YYYYMMDD_HHmm}` đã chốt 04/08.

## Phần KHÔNG đo lại (và vì sao)

Vòng 06/08 đã ghi rõ ở mục [2] rằng vai trò CB Nghiệp vụ xuất tốt, đã thử 4 cấu hình bộ lọc, và FLOW 03
§Chạy bước 1 cấm chạy lại vế đã được kết quả gần nhất ghi là đã đạt. Khối canonical của phiếu này chỉ có
Bước 1–3 và **không nêu đích danh biến thể lọc nào** phải lặp, nên chạy lại **1 cấu hình** đúng như
Bước 1 mô tả (Kỳ Năm · Toàn quốc) — cộng thêm mở tệp ra đọc và đối chiếu **từng hàng** kỳ vì Bước 3 đòi
đích danh việc đó.

**Không đo lại:** 3 cấu hình lọc còn lại của vòng 06/08 (kỳ Năm + lọc đơn vị Cục Bổ trợ tư pháp · kỳ
Tháng phủ 12 tháng · đơn vị Bộ Công an không có dữ liệu); các loại báo cáo khác.

**Không chấm lại:** tên tệp — mục [4] của vòng 06/08 đã kết luận không phải lỗi.

## Việc ghi nhận thêm — sẽ lập phiếu riêng, không chấm vào phiếu này

Báo cáo này vẫn còn chỉ tiêu **số doanh nghiệp** ở cả ba chỗ: thẻ *"Tổng DN toàn kỳ"* trên màn (đang
hiện `0`), chú giải biểu đồ *"Số DN"*, cột *"Số DN"* trong bảng Theo kỳ; và trong tệp xuất là `A12`
*"Tổng số DN toàn kỳ"* = `B12` `0` cùng cột `E19` *"Số DN"* → `E20` `0`.

`srs-fr-11-bao-cao.md:1021` (FR-IX-23, output `trend_data[]`) ghi dấu quyết định:
*"`[CTTLV_04 chốt 2026-07-24: bỏ so_dn — CSV UC146 chỉ "thống kê chương trình theo thời gian", không có
số DN; không có mô hình CT↔DN. Cùng lý do FR-IX-22.]`"* — tức chỉ tiêu này đã được nghiệp vụ quyết bỏ.
Báo cáo anh em `BC Chương trình theo lĩnh vực` (FR-IX-22, `:964`, cùng quyết định) **đã** bỏ đúng: bảng
chỉ còn `Lĩnh vực PL · Số chương trình`. Riêng báo cáo này còn sót.

Việc này **không** kéo phiếu xuống chưa đạt: điều kiện chấm của phiếu là *"mỗi hàng một kỳ thời gian kèm
nhãn kỳ và số chương trình, khớp đúng bảng trên màn"* — đã khớp; và bẫy của phiếu dặn không chấm hỏng vì
thứ tự / cách viết cột.
