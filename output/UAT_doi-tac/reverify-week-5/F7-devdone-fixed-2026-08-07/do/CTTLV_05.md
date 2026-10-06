# CTTLV_05 (dòng 277) — BC Chương trình theo lĩnh vực · Xuất Excel

**Verdict logic: Pass** → ô "Trạng thái dev fix" = `Test done`.

| | |
|---|---|
| Đo lúc | 2026-08-07 10:31 giờ VN |
| Env | `https://18.143.165.120.nip.io` (nội bộ) |
| Bó mã FE | `assets/index-eWHwDgt2.js` (deploy 09:11 giờ VN 07/08) |
| Nhãn màn | HTPLDN · V1.0.10 |
| Tài khoản | `admin` (QTHT/TW) — vai trò ra verdict · `cbnv_tw_03` (CB NV/TW) — vế chống hồi quy |
| Nguồn canonical | khối `CÁCH VERIFY` / `VERIFY LẠI` trong ô "Kết quả verify" của chính dòng 277 (vòng 06/08) |

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

Đường UI thật: menu [Báo cáo thống kê] → Loại "BC Chương trình theo lĩnh vực" → Kỳ "Năm"
(01/01/2026 → 31/12/2026) → Đơn vị "Toàn quốc" → **[Xem báo cáo]** → **[Xuất Excel]**.

| Chỉ tiêu | Trên màn | Trong tệp | Khớp |
|---|---|---|---|
| Tổng chương trình | 7 | `B8 = 7` | ✅ |
| Chưa phân loại | 3 | `B12 = 3` | ✅ |
| Lao động | 1 | `B13 = 1` | ✅ |
| Đất đai | 1 | `B14 = 1` | ✅ |
| Thuế | 1 | `B15 = 1` | ✅ |
| Thương mại | 1 | `B16 = 1` | ✅ |

- `GET /api/v1/bao-cao/ct-theo-linh-vuc?kyBaoCao=NAM&tuNgay=2026-01-01&denNgay=2026-12-31` → **200**.
- `POST /api/v1/bao-cao/export` → **200**; tệp giao ra `BaoCaoCtTheoLinhVuc_20260807_1031.xlsx`, 6.673 byte.
- **Đã mở tệp ra đọc** (giải nén ngay trong trình duyệt, đọc `workbook.xml` + `sharedStrings.xml` + `sheet1.xml`): tên trang tính `Chương trình theo lĩnh vực`, 22 ô có giá trị.
- 4 mục đầu tệp đủ: `A1` tên báo cáo · `A2` *"Kỳ báo cáo: Năm (từ 01/01/2026 đến 31/12/2026)"* ·
  `A3` *"Đơn vị: Toàn quốc"* · `A4` *"Ngày tạo: 07/08/2026"*.
- **Đối chiếu TỪNG HÀNG lĩnh vực** đúng như Bước 3 của khối canonical đòi — 5/5 hàng khớp, không
  hàng nào thừa hay thiếu, thứ tự cũng như trên màn.
- **Cộng dọc bằng đúng số tổng:** 3 + 1 + 1 + 1 + 1 = **7** = ô `B8`.
- Mục [4] của vòng 06/08 (tên tệp `BaoCaoCtTheoLinhVuc_…` không phải chuỗi `BaoCaoChuongTrinh`) đã
  kết luận **không phải lỗi** — giữ nguyên, không chấm lại.
- Bẫy số 3 (nút xuất xám vì đã xuất một lần trong lượt vào trang) **không xảy ra** ở lượt đo này:
  nút [Xuất Excel] còn bật, `POST /api/v1/bao-cao/export` trả **200** và tệp về máy bình thường.
- Tên tệp khớp khuôn `{TênBáoCáo}_{YYYYMMDD_HHmm}` đã chốt 04/08.

## Phần KHÔNG đo lại (và vì sao)

Vòng 06/08 đã ghi rõ ở mục [2] rằng vai trò CB Nghiệp vụ xuất tốt, đã thử 5 cấu hình bộ lọc, và FLOW 03
§Chạy bước 1 cấm chạy lại vế đã được kết quả gần nhất ghi là đã đạt. Khối canonical của phiếu này chỉ có
Bước 1–3 và **không nêu đích danh biến thể lọc nào** phải lặp, nên chạy lại **1 cấu hình** đúng như
Bước 1 mô tả (Kỳ Năm · Toàn quốc · để trống Lĩnh vực) — cộng thêm mở tệp ra đọc vì đó là bẫy số 2, và
đối chiếu **từng hàng** lĩnh vực vì Bước 3 đòi đích danh việc đó.

**Không đo lại:** 4 cấu hình lọc còn lại của vòng 06/08 (lọc đơn vị Cục Bổ trợ tư pháp · lọc lĩnh vực ·
một đơn vị không có dữ liệu · một lĩnh vực khác); các loại báo cáo khác.

**Không chấm lại:** tên tệp — mục [4] của vòng 06/08 đã kết luận không phải lỗi.

**Không thuộc phiếu này:** mục [7] — nút xuất bị khoá sau lượt xuất đầu tiên, đã có dòng theo dõi riêng
(`BCTK_QA02` dòng 365, và `BCTK_QA07` dòng 370 cùng triệu chứng). Lượt đo hôm nay nút Xuất vẫn bật và
xuất được, nhưng **không** dùng quan sát đó để đóng hai phiếu kia vì kịch bản của chúng là *xuất một lần
rồi bấm [Xem báo cáo] lần nữa mà không đổi bộ lọc* — lượt này không chạy kịch bản đó.
