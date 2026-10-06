# CPCTHTTTG_06 (dòng 264) — BC Chi phí theo thời gian · Xuất PDF

**Verdict logic: Pass** → ô "Trạng thái dev fix" = `Test done`.

| | |
|---|---|
| Đo lúc | 2026-08-07 10:12 giờ VN |
| Env | `https://18.143.165.120.nip.io` (nội bộ) |
| Bó mã FE | `assets/index-eWHwDgt2.js` (deploy 09:11 giờ VN 07/08) |
| Nhãn màn | HTPLDN · V1.0.10 |
| Tài khoản | `admin` (QTHT/TW) — vai trò ra verdict · `cbnv_tw_03` (CB NV/TW) — vế chống hồi quy |
| Nguồn canonical | khối `CÁCH VERIFY` / `VERIFY LẠI` trong ô "Kết quả verify" của chính dòng 264 (vòng 06/08) |

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

Đường UI thật: menu [Báo cáo thống kê] → Loại "BC Chi phí theo thời gian" → Kỳ "Năm"
(01/01/2026 → 31/12/2026) → Đơn vị "Toàn quốc" → **[Xem báo cáo]** → **[Xuất PDF] → hộp thoại để mặc định A4 + Dọc → [Xuất file]**.

| Chỉ tiêu | Trên màn | Trong tệp | Khớp |
|---|---|---|---|
| Tổng chi phí toàn kỳ | 23.000.000 ₫ | `23.000.000` | ✅ |
| Tổng hồ sơ toàn kỳ | 2 | `2` | ✅ |
| Bảng Theo kỳ — dòng Năm 2026 | 01/01/2026 · 31/12/2026 · 2 · 23.000.000 ₫ | `Năm 2026 · 01/01/2026 · 31/12/2026 · 2 · 23.000.000` | ✅ |

- `GET /api/v1/bao-cao/chi-phi-theo-thoi-gian?kyBaoCao=NAM&tuNgay=2026-01-01&denNgay=2026-12-31` → **200**.
- `POST /api/v1/bao-cao/export` → **200**; tệp giao ra `BaoCaoChiPhiTheoThoiGian_20260807_1012.pdf`, 32.088 byte.
- **Đã mở tệp ra đọc** (giải nén luồng nội dung ngay trong trình duyệt rồi tra bảng `ToUnicode` của từng phông): 1 trang, `%PDF-1.3`, bộ sinh `pdfmake`, phông `Tinos` (bản tương thích số đo của Times New Roman — bẫy số 4, không chấm Fail).
- 4 mục nhận dạng giữa trang đủ: tên báo cáo *"BC CHI PHÍ THEO THỜI GIAN"* · *"Kỳ báo cáo: Năm (từ
  01/01/2026 đến 31/12/2026)"* · *"Đơn vị: Toàn quốc"* · *"Ngày tạo: 07/08/2026"*.
- **Khổ giấy khi để mặc định:** `/MediaBox 595.28 × 841.89 pt` = 210 × 297 mm = **A4 Dọc**, `/Count 1`
  = 1 trang. Hộp thoại mở ra đã chọn sẵn **A4** + **Dọc** (ảnh
  [`image/F7-264-hop-thoai-xuat-PDF-macdinh-A4-Doc.png`](../image/F7-264-hop-thoai-xuat-PDF-macdinh-A4-Doc.png)).
- **Đủ khung văn bản hành chính** — đầu trang: tên cơ quan *"CỤC BỔ TRỢ TƯ PHÁP - BỘ TƯ PHÁP"* ·
  quốc hiệu *"CỘNG HÒA XÃ HỘI CHỦ NGHĨA VIỆT NAM"* · tiêu ngữ *"Độc lập - Tự do - Hạnh phúc"*.
  Cuối trang: *"Ngày 07 tháng 08 năm 2026"* · *"NGƯỜI XUẤT BÁO CÁO"* · *"(Ký, ghi rõ họ tên và đóng
  dấu)"* · họ tên người xuất *"CB Nghiệp vụ - Trung ương #03"*.
- **Không** có dòng chức danh người ký — đúng quyết định nghiệp vụ 04/08/2026, bẫy số 4 dặn không
  chấm Fail vì việc này.
- Đúng **bẫy số 1**: nút [Xuất PDF] chỉ mở hộp thoại; lượt xuất thật là nút [Xuất file] bên trong —
  đã bấm đúng nút đó nên thấy lời gọi `POST /api/v1/bao-cao/export`.
- Khung thông báo theo dõi theo thời gian (không đếm khung mới, đúng bẫy số 5): *"Đang tạo file..."*
  → *"Tạo file thành công."*, không có chuỗi tiếng Anh nào.
- Chữ đọc được đầy đủ:
  [`image/F7-264-noi-dung-doc-duoc-trong-tep-PDF.txt`](../image/F7-264-noi-dung-doc-duoc-trong-tep-PDF.txt).
- Tên tệp khớp khuôn `{TênBáoCáo}_{YYYYMMDD_HHmm}` đã chốt 04/08.

## Phần KHÔNG đo lại (và vì sao)

Vòng 06/08 đã ghi rõ ở khối "ĐÃ HẾT LỖI" rằng vai trò CB Nghiệp vụ xuất PDF tốt ở cấu hình Kỳ Năm 2026
và thêm một cấu hình Khoảng tùy chọn tháng 6, và FLOW 03 §Chạy bước 1 cấm chạy lại vế đã được kết quả
gần nhất ghi là đã đạt. Bước B4 của khối canonical ở phiếu này **không nêu đích danh biến thể nào**
("Lặp B1–B3 bằng `cbnv_tw_03` để chắc vai trò này không bị chặn theo"), nên chỉ chạy lại **1 cấu hình**
đúng như B1 mô tả — cộng thêm mở tệp ra đọc vì đó là bẫy số 3 của chính khối đó.

**Không đo lại:** cấu hình Kỳ "Khoảng tùy chọn" tháng 6 (vòng 06/08 đã ghi đạt); các loại báo cáo khác;
tuỳ chọn khổ giấy A3 / Letter và hướng Ngang (khối canonical chỉ đòi kiểm khổ **mặc định**).

**Không chấm trong phiếu này** (đã tách phiếu riêng, đúng như khối canonical dặn): `BCTK_QA07` (dòng
370) — nút Xuất bị khoá sau lần xem thứ 2; `BCTK_QA09` (dòng 372) — tệp PDF in mã kỹ thuật "KHOANG" ở
dòng Kỳ báo cáo khi chọn Khoảng tùy chọn. Lượt đo này dùng Kỳ "Năm" nên dòng Kỳ báo cáo in đúng tiếng
Việt, việc đó **không** dùng để đóng `BCTK_QA09`.
