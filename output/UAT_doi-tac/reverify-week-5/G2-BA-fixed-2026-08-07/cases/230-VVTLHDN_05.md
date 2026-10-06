# Dòng 230 — `VVTLHDN_05` — BC Vụ việc theo loại hình DN · Xuất Excel

**Verdict: ✅ Test done** (bug gốc hết)

---

## 1. Bug gốc là gì

| Nguồn | Nội dung |
|---|---|
| Kết quả mong đợi (cột K) | "Hệ thống xuất toàn bộ và tự động tải tệp về máy người dùng. Tên tệp xuất: `BaoCaoVuViec_{YYYYMMDD_HHmm}.xlsx`" |
| Kết quả thực tế (cột L) | "Hệ thống hiển thị thông báo **"Không thể tạo file xuất. Vui lòng thử lại."**" |

**Đạt khi:** bấm [Xuất Excel] ra được tệp thật, tải về máy, không còn thông báo từ chối đó.

---

## 2. Đo thế nào

| Hạng mục | Giá trị |
|---|---|
| Môi trường | `https://18.143.165.120.nip.io` |
| Bó mã FE | `assets/index-BbPPdate.js` · `GET /` last-modified `Fri, 07 Aug 2026 06:47:57 GMT` (nhãn sidebar `HTPLDN · V1.0.10`) |
| Vai trò | `cbnv_tw_01` — Cán bộ Nghiệp vụ Trung ương (tác nhân của chức năng báo cáo theo `srs-fr-11-bao-cao.md:51` + `:62`) |
| Giờ đo | 07/08/2026 ~16:35 giờ VN |
| Bộ lọc | Loại báo cáo = **BC Vụ việc theo loại hình DN** · Kỳ = **Năm** · 01/01/2026 → 31/12/2026 · Đơn vị = Toàn quốc |

Trang được tải lại từ đầu trước khi đo (không dùng lại tab cũ). Bấm **nút thật** [Xem báo cáo] → [Xuất Excel].

---

## 3. Thấy gì

### 3.1 Không còn thông báo từ chối

| Mốc | Nội dung khung thông báo |
|---|---|
| ngay sau khi bấm | `Đang tạo file...` |
| ~0,07 s sau | chữ trong **chính khung đó** đổi thành `Tạo file thành công.` |

Không xuất hiện "Không thể tạo file xuất. Vui lòng thử lại." và không có chữ "Forbidden".

### 3.2 Tệp thật đã về máy

- `POST /api/v1/bao-cao/export` → **200**, `content-disposition: attachment; filename="BaoCaoVuViecTheoLoaiDn_20260807_1635.xlsx"`.
- Đối tượng tệp **6.801 byte**, kiểu `…spreadsheetml.sheet`; trình duyệt đã kích hoạt tải xuống với đúng tên đó.
- Tên tệp đúng khuôn `{TenBaoCao}_{YYYYMMDD_HHmm}.xlsx` (`srs-fr-11-bao-cao.md:85`).

### 3.3 MỞ TỆP RA ĐỌC

Lưu tại `files/BaoCaoVuViecTheoLoaiDn_20260807_1635.xlsx`, mở bằng `openpyxl`:
chữ ký `PK\x03\x04`, 1 trang tính **"Vụ việc theo loại hình DN"**, 14 dòng × 6 cột, đủ 4 mục đầu tệp
(tên báo cáo / kỳ + khoảng thời gian / đơn vị / ngày tạo).

| Quy mô DN | Cục BTTP - BTP | Sở TP Hà Nội | Sở TP An Giang | Bộ KH&ĐT | Tổng |
|---|---|---|---|---|---|
| Nhỏ | 14 | 5 | 8 | 0 | 27 |
| Siêu nhỏ | 12 | 2 | 0 | 4 | 18 |
| (Không phân loại) | 1 | 0 | 0 | 0 | 1 |

Khớp **từng con số** với bảng trên màn; cộng 27+18+1 = **46**, khớp ô "Tổng số vụ việc: 46" trong tệp.

---

## 4. Verdict + vì sao

**✅ Test done.** Triệu chứng gốc ở cột L không còn tái hiện với đúng tác nhân của chức năng báo cáo.
Tệp Excel sinh ra là tệp thật, tải về được, mở ra đọc thấy đủ đầu mục và số liệu khớp màn — thoả
"xuất toàn bộ và tự động tải tệp về máy" của Kết quả mong đợi.

---

## 5. Bằng chứng

| Tệp | Nội dung |
|---|---|
| `image/VVTLHDN_05-01-cbnv-tw-man-bao-cao.png` | Màn báo cáo của `cbnv_tw_01` sau khi xuất, bộ lọc + số liệu hiện rõ |
| `files/BaoCaoVuViecTheoLoaiDn_20260807_1635.xlsx` | Tệp Excel thật do nút [Xuất Excel] sinh ra (6.801 byte) |
| `files/b64-230-VVTLHDN_05.json` | Bản mã hoá nguyên trạng đối tượng tệp trình duyệt nhận được |
