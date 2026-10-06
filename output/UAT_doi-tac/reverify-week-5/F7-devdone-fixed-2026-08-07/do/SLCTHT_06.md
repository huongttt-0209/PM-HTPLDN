# SLCTHT_06 (dòng 267) — BC Số lượng chương trình hỗ trợ · Xuất Excel

**Verdict logic: Pass** → ô "Trạng thái dev fix" = `Test done`.

| | |
|---|---|
| Đo lúc | 2026-08-07 10:25 giờ VN |
| Env | `https://18.143.165.120.nip.io` (nội bộ) |
| Bó mã FE | `assets/index-eWHwDgt2.js` (deploy 09:11 giờ VN 07/08) |
| Nhãn màn | HTPLDN · V1.0.10 |
| Tài khoản | `admin` (QTHT/TW) — vai trò ra verdict · `cbnv_tw_03` (CB NV/TW) — vế chống hồi quy |
| Nguồn canonical | khối `CÁCH VERIFY` / `VERIFY LẠI` trong ô "Kết quả verify" của chính dòng 267 (vòng 06/08) |

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

Đường UI thật: menu [Báo cáo thống kê] → Loại "BC Số lượng chương trình hỗ trợ" → Kỳ "Năm"
(01/01/2026 → 31/12/2026) → Đơn vị "Toàn quốc" → **[Xem báo cáo]** → **[Xuất Excel]**.

| Chỉ tiêu | Trên màn | Trong tệp | Khớp |
|---|---|---|---|
| Tổng chương trình | 7 | `B8 = 7` | ✅ |
| Đang thực hiện | 1 | `B12 = 1` | ✅ |
| Hoàn thành | 1 | `B16 = 1` | ✅ |
| Theo đơn vị — Cục Bổ trợ tư pháp | 7 · 1 · 1 | `B26..D26 = 7 · 1 · 1` | ✅ |
| Theo kỳ — Năm 2026 | 01/01/2026 → 31/12/2026 | `A30..D30 = Năm 2026 · 01/01/2026 · 31/12/2026 · 7` | ✅ |

- `GET /api/v1/bao-cao/so-luong-ct-ho-tro?kyBaoCao=NAM&tuNgay=2026-01-01&denNgay=2026-12-31` → **200**.
- `POST /api/v1/bao-cao/export` → **200**; tệp giao ra `BaoCaoSoLuongCtHoTro_20260807_1025.xlsx`, 6.959 byte.
- **Đã mở tệp ra đọc** (giải nén ngay trong trình duyệt, đọc `workbook.xml` + `sharedStrings.xml` + `sheet1.xml`): tên trang tính `Số lượng chương trình hỗ trợ`, 46 ô có giá trị.
- 4 mục đầu tệp đủ: `A1` tên báo cáo · `A2` *"Kỳ báo cáo: Năm (từ 01/01/2026 đến 31/12/2026)"* ·
  `A3` *"Đơn vị: Toàn quốc"* · `A4` *"Ngày tạo: 07/08/2026"*.
- **3 số quyết định của khối canonical khớp đủ:** Tổng chương trình 7 · Đang thực hiện 1 · Hoàn thành 1.
  Ngoài ra tệp còn có bảng "Theo trạng thái" (Đã phê duyệt 5 · Đang thực hiện 1 · Hoàn thành 1 = 7).
- **Điểm ghi chú [3] của vòng 06/08 nay đã hết hiệu lực.** Ô cũ nêu `srs-fr-11-bao-cao.md:1268`
  (BR-AUTH-08) có ngoại lệ *"QTHT bypass"* cho toàn nhóm FR-IX, tức nghiêng về hướng QTHT **được**
  xuất. Đối chiếu bản chốt hôm nay: ngoại lệ đó đã **bị gỡ khỏi BR-AUTH-08**, và `:79` nay ghi rõ
  *"Vai trò khác (kể cả QTHT) → chặn ngay ở cửa vào, không mở màn hình"*. Nghiệp vụ cũng đã chốt
  06/08/2026 rằng QTHT **không phải tác nhân** của chức năng báo cáo thống kê. ⇒ Nhánh ✅ thứ hai của
  khối canonical là nhánh đúng, và hệ thống đang làm đúng nhánh đó.
- Bẫy số 3 (không chấm hỏng vì tên sheet / thứ tự cột / màu / dòng tổng / không nhúng biểu đồ) đã
  tuân thủ — không dùng các thứ đó để chấm.
- Tên tệp khớp khuôn `{TênBáoCáo}_{YYYYMMDD_HHmm}` đã chốt 04/08.

## Phần KHÔNG đo lại (và vì sao)

Vòng 06/08 đã ghi rõ ở mục [2] rằng vai trò CB Nghiệp vụ xuất tốt, đã thử 4 cấu hình bộ lọc, và FLOW 03
§Chạy bước 1 cấm chạy lại vế đã được kết quả gần nhất ghi là đã đạt. Khối canonical của phiếu này viết
cho vai trò admin (Bước 1–3) và **không nêu đích danh biến thể lọc nào** phải lặp, nên chỉ chạy lại
**1 cấu hình** đúng như Bước 1 mô tả (Kỳ Năm · Toàn quốc · để trống Trạng thái chương trình) — cộng thêm
mở tệp ra đọc vì đó là bẫy số 2 của chính khối đó.

**Không đo lại:** 3 cấu hình lọc còn lại của vòng 06/08 (lọc đơn vị · lọc trạng thái Hoàn thành · một
đơn vị không có dữ liệu); các loại báo cáo khác.

## Việc ghi nhận thêm — sẽ lập phiếu riêng, không chấm vào phiếu này

Trên màn, bảng **"Thống kê theo kỳ"** hiện dòng `Năm 2026` với cả hai ô **Số lượng** và **Tỷ lệ** để
dấu gạch ngang, trong khi:

- máy chủ trả `theoKy: [{kyLabel:"Năm 2026", tuNgayKy:"2026-01-01", denNgayKy:"2026-12-31", soCt: 7}]`;
- tệp xuất in đúng `D30 = 7` ở cột "Số chương trình".

`srs-fr-11-bao-cao.md:914` xếp `theo_ky[] {ky, so_ct}` là output có điều kiện hiển thị **"Luôn"**. Số
liệu đã có sẵn, chỉ riêng chỗ hiển thị trên màn bỏ trống. Việc này **độc lập** với lỗi phân quyền của
phiếu, và 3 số quyết định của phiếu (7 · 1 · 1) vẫn khớp, nên không kéo phiếu này xuống chưa đạt.
Phạm vi thật sự của lỗi sẽ được xác định sau khi đo nốt 3 báo cáo chương trình còn lại trong lô
(`CTTDVQL_04` · `CTTLV_05` · `CTTTG_04`) rồi mới lập phiếu, để phiếu nêu đúng phạm vi thay vì đoán.
