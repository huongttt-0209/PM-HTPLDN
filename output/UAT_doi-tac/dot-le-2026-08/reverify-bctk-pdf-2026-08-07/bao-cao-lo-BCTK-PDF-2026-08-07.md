# Báo cáo lô BCTK-PDF — re-verify 21 phiếu "Xuất PDF · Báo cáo thống kê"

**Ngày:** 2026-08-07 · **Env:** `https://18.143.165.120.nip.io` (nội bộ) · **Bó mã FE:** `assets/index-BbPPdate.js`
**Tab ghi:** `bug` (gid `1714340219`) của `1OKBN2otlmdZ44THkmhtsn-_63M2Boh7zQwearwjYR3s`

## 1. Kết quả — 21/21 dòng đã đo và đã ghi sheet

| Dòng | Mã TC | Loại báo cáo | Verdict | Ô "Trạng thái dev fix" đã ghi |
|---:|---|---|---|---|
| 175 | SLHDVM_07 | BC Số lượng hỏi đáp/vướng mắc pháp luật | **Pass** | `Test done` |
| 180 | VVDTN_07 | BC Vụ việc đã tiếp nhận | **Pass** | `Test done` |
| 186 | VVDHT_07 | BC Vụ việc đang hỗ trợ | **Pass** | `Test done` |
| 190 | VVDHTHT_07 | BC Vụ việc đã hoàn thành | **Pass** | `Test done` |
| 196 | VVTTG_06 | BC Vụ việc theo thời gian | **Pass** | `Test done` |
| 201 | CLDTBDDDR_07 | BC Lớp đào tạo đang diễn ra | **Pass** | `Test done` |
| 206 | LDTBDDDR_07 | BC Lớp đào tạo đã diễn ra | **Pass** | `Test done` |
| 211 | CGTVPL_07 | BC Số lượng CG/TVV | **Pass** | `Test done` |
| 215 | DGHQHTPL_07 | BC Đánh giá hiệu quả HTPL | **Pass** | `Test done` |
| 219 | CLDTBDPL_07 | BC Chất lượng đào tạo | **Pass** | `Test done` |
| 223 | VVTDVQL_07 | BC Vụ việc theo đơn vị quản lý | **Pass** | `Test done` |
| 227 | VVTLV_06 | BC Vụ việc theo lĩnh vực | **Pass** | `Test done` |
| 231 | VVTLHDN_06 | BC Vụ việc theo loại hình DN | **Pass** | `Test done` |
| 235 | VVTTGCT_06 | BC Vụ việc theo thời gian chi tiết | **Pass** | `Test done` |
| 239 | CPHTCT_07 | BC Chi phí chi trả hỗ trợ | **Pass** | `Test done` |
| 244 | CPCTHTTDVQL_07 | BC Chi phí theo đơn vị | **Pass** | `Test done` |
| 259 | CPCTHTTLHDN_07 | BC Chi phí theo loại hình DN | **Pass** | `Test done` |
| 268 | SLCTHT_07 | BC Số lượng chương trình hỗ trợ | **Pass** | `Test done` |
| 273 | CTTDVQL_05 | BC Chương trình theo đơn vị | **Pass** | `Test done` |
| 278 | CTTLV_06 | BC Chương trình theo lĩnh vực | **Pass** | `Test done` |
| 282 | CTTTG_05 | BC Chương trình theo thời gian | **Pass** | `Test done` |

**21 Pass · 0 Reopen · 0 blocker.** Mọi lượt ghi đều qua `tools/sheet_bug_verify_write.py` (đối chiếu gid +
`Mã TC` + giá trị cũ trước khi ghi, đọc lại sau khi ghi). Cột `Kết quả verify` **để trống toàn bộ** — đúng
quy ước "Pass thì không ghi diễn giải". Các ô chỉ-đọc `Trạng thái` · `Kết quả thực tế` · `TKM phản hồi lần 1` ·
`DEV phản hồi lần 1` còn nguyên, đã kiểm bằng lượt đọc lại cuối lô.

> ℹ️ **Lưu ý chuyển trạng thái:** cả 21 ô trước lô này mang giá trị `UAT done` (do bên khác đặt — không lượt
> ghi nào của công cụ QA từng chạm 21 dòng này). Lô ghi đè thành `Test done` theo đúng ánh xạ verdict được
> cấp. Bản sao lưu nguyên trạng ở [files/backup-truoc-ghi.json](files/backup-truoc-ghi.json) nếu cần hoàn tác.

## 2. Vì sao Pass — hai vế đều phải đạt

21 phiếu **cùng một lỗi gốc, cùng một màn** `/bao-cao`, chỉ khác loại báo cáo. Ô *Kết quả thực tế* của đối tác
ghi câu `"Không thể tạo file xuất. Vui lòng thử lại."` (16/07); ô *TKM phản hồi lần 1* ghi `Forbidden` (31/07).
Chuẩn chấm khóa trước khi đo ở [chuan/chuan-21-case-pdf.md](chuan/chuan-21-case-pdf.md).

### Vế A — xuất PDF bằng vai trò Cán bộ Nghiệp vụ (`cbnv_tw_05`)

Chạy **đúng 4 bước bug gốc** cho từng loại báo cáo: Báo cáo thống kê → chọn loại + Kỳ **Năm** (01/01/2026 →
31/12/2026) + Đơn vị **Toàn quốc** → [Xem báo cáo] → [Xuất PDF] → hộp thoại *Tùy chọn in báo cáo PDF* để
**mặc định A4 · Dọc** → [Xuất file]. Mỗi tệp đều được **mở ra đọc nội dung**, không chỉ kiểm tệp có tạo được.

**15/15 mục đạt ở cả 21 loại:**

| Mục | Kết quả chung |
|---|---|
| Tên tệp đúng khuôn `{TenBaoCao}_{YYYYMMDD_HHmm}.pdf` | ✅ 21/21 — đủ ngày **và** giờ-phút |
| Hai lần xuất khác phút ra hai tên khác nhau | ✅ `BaoCaoHoiDap_20260807_1834.pdf` vs `..._1837.pdf` |
| Đầu trang: quốc hiệu `CỘNG HÒA XÃ HỘI CHỦ NGHĨA VIỆT NAM` | ✅ 21/21 |
| Đầu trang: tiêu ngữ `Độc lập - Tự do - Hạnh phúc` | ✅ 21/21 |
| Đầu trang: tên cơ quan ban hành | ✅ 21/21 — `CỤC BỔ TRỢ TƯ PHÁP - BỘ TƯ PHÁP` |
| Cuối trang: ngày ký | ✅ 21/21 — `Ngày 07 tháng 08 năm 2026` |
| Cuối trang: `NGƯỜI XUẤT BÁO CÁO` | ✅ 21/21 |
| Cuối trang: chỗ trống con dấu `(Ký, ghi rõ họ tên và đóng dấu)` | ✅ 21/21 |
| Cuối trang: họ tên cán bộ xuất báo cáo | ✅ 21/21 — `CB Nghiệp vụ - Trung ương #05` |
| Khổ A4 dọc | ✅ 21/21 — `595,28 × 841,89 pt` |
| Phông tương thích Times New Roman | ✅ 21/21 — `Tinos-Regular` / `Tinos-Bold` / `Tinos-Italic` |
| Đầu tệp có tên báo cáo | ✅ 21/21 |
| Đầu tệp có `Kỳ báo cáo:` kèm khoảng thời gian | ✅ 21/21 |
| Đầu tệp có `Đơn vị:` | ✅ 21/21 |
| Đầu tệp có `Ngày tạo:` | ✅ 21/21 |
| Không tái hiện câu `"Không thể tạo file xuất. Vui lòng thử lại."` | ✅ 21/21 — không tệp nào, không thông báo nào |

**Số liệu trong tệp khớp số trên màn** của chính lần đo đó — ví dụ `SLHDVM_07`: màn hiện Tổng hỏi đáp 22 ·
Đã trả lời 11 · Chờ trả lời 11 · Tỷ lệ 50,0% · Thương mại 13 · Thuế 8 · Lao động 1 · Cục Bổ trợ tư pháp 21 ·
Sở Tư pháp Hà Nội 1; tệp in lại đúng từng con số đó.

### Vế B — vai trò Quản trị hệ thống (`admin`), đo một lần áp chung 21 phiếu

Chi tiết ở [do/VE-B-quan-tri-he-thong.md](do/VE-B-quan-tri-he-thong.md). Tóm tắt:

| Điều phải chứng minh | Kết quả |
|---|---|
| Mục menu "Báo cáo thống kê" bị **ẩn hẳn** (không làm mờ) | ✅ đếm đủ 32 mục, không có mục này |
| Vào thẳng `/bao-cao` **không mở được màn** | ✅ bị đưa về màn Tổng quan, không ô chọn loại BC, không nút xuất |
| Bước **xem** ở tầng máy chủ từ chối bằng tiếng Việt | ✅ 403 · `ERR-RPT-05` · "Bạn không có quyền xem báo cáo này" |
| Bước **xuất tệp** ở tầng máy chủ từ chối bằng tiếng Việt | ✅ 403 · `ERR-RPT-08` · "Bạn không có quyền thực hiện thao tác này" |
| Máy chủ **không sinh tệp** cho vai trò này | ✅ |
| Ẩn theo vai trò, không phải gỡ chức năng | ✅ cùng bó mã, tài khoản CB Nghiệp vụ **vẫn thấy** mục đó |

**Chuỗi `Forbidden` mà đối tác báo ngày 31/07 KHÔNG còn tái hiện** ở bất kỳ bước nào.

**Điểm mấu chốt:** kỳ vọng gốc của 21 phiếu ở vế này (quản trị hệ thống **xuất được** tệp) đã **không còn là
nhánh Pass** — nghiệp vụ chốt ngày 06/08/2026 rằng Quản trị hệ thống không phải tác nhân của chức năng báo
cáo thống kê. Nhánh Pass đúng là chặn ở cửa vào + ẩn mục menu + báo bằng tiếng Việt, và phần mềm đang làm
đúng như vậy.

## 3. Bằng chứng — 21 tệp PDF đã tải về và mở ra đọc

| Mã TC | Loại báo cáo | Tệp nhận được | Kích cỡ |
|---|---|---|---|
| SLHDVM_07 | BC Số lượng hỏi đáp/vướng mắc pháp luật | `BaoCaoHoiDap_20260807_1837.pdf` | 34.720 byte · 1 trang |
| VVDTN_07 | BC Vụ việc đã tiếp nhận | `BaoCaoVuViecTiepNhan_20260807_1836.pdf` | 34.806 byte · 1 trang |
| VVDHT_07 | BC Vụ việc đang hỗ trợ | `BaoCaoVuViecDangHoTro_20260807_1839.pdf` | 35.314 byte · 1 trang |
| VVDHTHT_07 | BC Vụ việc đã hoàn thành | `BaoCaoVuViecHoanThanh_20260807_1840.pdf` | 36.152 byte · 2 trang |
| VVTTG_06 | BC Vụ việc theo thời gian | `BaoCaoVuViecTheoThoiGian_20260807_1840.pdf` | 33.694 byte · 1 trang |
| CLDTBDDDR_07 | BC Lớp đào tạo đang diễn ra | `BaoCaoLopDaoTaoDangDienRa_20260807_1841.pdf` | 37.268 byte · 2 trang |
| LDTBDDDR_07 | BC Lớp đào tạo đã diễn ra | `BaoCaoLopDaoTaoDaDienRa_20260807_1842.pdf` | 35.894 byte · 2 trang |
| CGTVPL_07 | BC Số lượng CG/TVV | `BaoCaoSoLuongCgTvv_20260807_1842.pdf` | 34.540 byte · 1 trang |
| DGHQHTPL_07 | BC Đánh giá hiệu quả HTPL | `BaoCaoDanhGiaHieuQua_20260807_1843.pdf` | 39.505 byte · 2 trang |
| CLDTBDPL_07 | BC Chất lượng đào tạo | `BaoCaoChatLuongDaoTao_20260807_1844.pdf` | 40.264 byte · 2 trang |
| VVTDVQL_07 | BC Vụ việc theo đơn vị quản lý | `BaoCaoVuViecTheoDonVi_20260807_1844.pdf` | 33.827 byte · 1 trang |
| VVTLV_06 | BC Vụ việc theo lĩnh vực | `BaoCaoVuViecTheoLinhVuc_20260807_1845.pdf` | 32.326 byte · 1 trang |
| VVTLHDN_06 | BC Vụ việc theo loại hình DN | `BaoCaoVuViecTheoLoaiDn_20260807_1846.pdf` | 32.791 byte · 1 trang |
| VVTTGCT_06 | BC Vụ việc theo thời gian chi tiết | `BaoCaoVuViecTheoTgChiTiet_20260807_1846.pdf` | 31.191 byte · 1 trang |
| CPHTCT_07 | BC Chi phí chi trả hỗ trợ | `BaoCaoChiPhiChiTra_20260807_1847.pdf` | 35.682 byte · 1 trang |
| CPCTHTTDVQL_07 | BC Chi phí theo đơn vị | `BaoCaoChiPhiTheoDonVi_20260807_1848.pdf` | 32.632 byte · 1 trang |
| CPCTHTTLHDN_07 | BC Chi phí theo loại hình DN | `BaoCaoChiPhiTheoLoaiDn_20260807_1848.pdf` | 33.783 byte · 1 trang |
| SLCTHT_07 | BC Số lượng chương trình hỗ trợ | `BaoCaoSoLuongCtHoTro_20260807_1849.pdf` | 34.075 byte · 1 trang |
| CTTDVQL_05 | BC Chương trình theo đơn vị | `BaoCaoCtTheoDonVi_20260807_1850.pdf` | 32.565 byte · 1 trang |
| CTTLV_06 | BC Chương trình theo lĩnh vực | `BaoCaoCtTheoLinhVuc_20260807_1850.pdf` | 31.330 byte · 1 trang |
| CTTTG_05 | BC Chương trình theo thời gian | `BaoCaoCtTheoThoiGian_20260807_1851.pdf` | 32.243 byte · 1 trang |

Tệp gốc + bản bắt được ở [evidence/](evidence/). Ảnh vế Quản trị hệ thống ở
[image/VE-B-01-QTHT-menu-khong-co-Bao-cao-thong-ke.png](image/VE-B-01-QTHT-menu-khong-co-Bao-cao-thong-ke.png).

## 4. Những thứ cố ý KHÔNG chấm FAIL (đều là tiền lệ đã chốt, không phải suy đoán)

- **Không có chữ ký số** — cờ chữ ký của cả 21 tệp trả `-1`, tệp không có trường ký điện tử. Đúng chủ trương
  đã chốt cho nhóm báo cáo thống kê; chuỗi "ký số" không xuất hiện ở bất kỳ dòng nào của đặc tả nhóm này.
- **Không có dòng chức danh người ký** — đúng quyết định chốt 04/08, khối ký chỉ in ngày + họ tên + chỗ dấu.
- **Phông tên là `Tinos-*` chứ không phải chuỗi "Times New Roman"** — bản tương thích số đo, đã được chấp
  nhận từ các lượt đo trước.
- **Nút [Xuất PDF] chỉ mở hộp thoại**, lượt xuất thật ở nút [Xuất file] — không phải "bấm không có phản hồi".
- **Dev dùng `ERR-RPT-05` cho bước xem** thay vì mã mới — thuộc phiếu riêng, không lật verdict lô này.
- **5 phiếu đã tách riêng** (`BCTK_QA05` · `BCTK_QA07` · `BCTK_QA09` · `BCTK_QA13` · `BCTK_QA14`) — không
  chấm lại trong lô này, kể cả 2 phiếu chạm đúng `SLCTHT_07` và `CTTTG_05`.

## 5. Giới hạn hiệu lực

Mọi verdict trong lô chỉ có hiệu lực trên **env nội bộ** `18.143.165.120.nip.io` và **đúng bó mã FE
`assets/index-BbPPdate.js`** (`last-modified` 07/08/2026 06:47:57 GMT). Env nghiệm thu của đối tác
(`htpldn-uat.ospgroup.vn`) là môi trường khác, chưa đo trong lô này.

Lượt đo lô F7 sáng cùng ngày chạy trên bó mã cũ hơn (`index-eWHwDgt2.js`) nên **không kế thừa**; toàn bộ
21 phiếu + vế Quản trị hệ thống của lô này đều đo lại từ đầu.

## 6. Tệp trong lô

| Tệp | Nội dung |
|---|---|
| [BAN-DUNG.md](BAN-DUNG.md) | Vân tay bản dựng đầu/cuối phiên + tài khoản dùng đo |
| [chuan/chuan-21-case-pdf.md](chuan/chuan-21-case-pdf.md) | Chuẩn chấm khóa trước khi đo — tiêu chí PASS/FAIL + căn cứ đặc tả + 17 bẫy |
| [do/VE-B-quan-tri-he-thong.md](do/VE-B-quan-tri-he-thong.md) | Kết quả 4 phép đo vế Quản trị hệ thống |
| [files/kiem-tep-pdf.py](files/kiem-tep-pdf.py) | Bộ chấm tự động 15 mục cho tệp PDF xuất ra |
| [files/ghi.sh](files/ghi.sh) | Vỏ bọc ghi verdict 1 dòng vào tab `bug` |
| [files/CACH-GHI-SHEET.md](files/CACH-GHI-SHEET.md) | Lệnh ghi sẵn 21 dòng × 2 kịch bản |
| [files/dropdown-cot-R.md](files/dropdown-cot-R.md) | Từ vựng dropdown thật của ô verdict trên 21 dòng |
| [files/backup-truoc-ghi.json](files/backup-truoc-ghi.json) | Sao lưu nguyên trạng 21 dòng trước khi ghi |
| [evidence/](evidence/) | 21 tệp PDF + bản bắt được từ trình duyệt |
| [image/](image/) | Ảnh màn hình vế Quản trị hệ thống |
