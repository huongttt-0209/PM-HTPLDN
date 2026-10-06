# Dòng 234 — `VVTTGCT_05` — BC Vụ việc theo thời gian chi tiết · Xuất Excel

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
| Vai trò | `cbnv_tw_01` — Cán bộ Nghiệp vụ Trung ương (`srs-fr-11-bao-cao.md:51`, `:62`) |
| Giờ đo | 07/08/2026 ~16:38 giờ VN |
| Bộ lọc | Loại báo cáo = **BC Vụ việc theo thời gian chi tiết** · Kỳ = **Năm** · 01/01/2026 → 31/12/2026 · Đơn vị = Toàn quốc |

Trang tải lại từ đầu trước khi đo. Bấm nút thật [Xem báo cáo] → [Xuất Excel].

---

## 3. Thấy gì

### 3.1 Không còn thông báo từ chối

`Đang tạo file...` → chữ trong chính khung đó đổi thành `Tạo file thành công.` (~0,09 s sau).
Không có "Không thể tạo file xuất. Vui lòng thử lại.", không có "Forbidden".

### 3.2 Tệp thật đã về máy

- `POST /api/v1/bao-cao/export` → **200**, `content-disposition: attachment; filename="BaoCaoVuViecTheoTgChiTiet_20260807_1638.xlsx"`.
- Đối tượng tệp **6.636 byte**, kiểu `…spreadsheetml.sheet`; trình duyệt kích hoạt tải xuống đúng tên đó.
- Tên tệp đúng khuôn `{TenBaoCao}_{YYYYMMDD_HHmm}.xlsx` (`srs-fr-11-bao-cao.md:85`).

### 3.3 MỞ TỆP RA ĐỌC

`files/BaoCaoVuViecTheoTgChiTiet_20260807_1638.xlsx`, mở bằng `openpyxl`: chữ ký `PK\x03\x04`,
1 trang tính **"Vụ việc theo thời gian"**, 12 dòng × 6 cột, đủ 4 mục đầu tệp.

| Kỳ | Mới | Tiếp nhận | Đang hỗ trợ | Hoàn thành | Tổng |
|---|---|---|---|---|---|
| Năm 2026 | 2 | 18 | 13 | 21 | 59 |

Khớp từng con số với bảng trên màn; 2+18+13+21 = **59**, khớp ô "Tổng số vụ việc: 59".

---

## 4. Verdict + vì sao

**✅ Test done.** Triệu chứng gốc ở cột L không còn tái hiện với đúng tác nhân của chức năng báo cáo.
Tệp Excel sinh ra là tệp thật, tải về được, mở ra đọc thấy đủ đầu mục và số liệu khớp màn.

---

## 5. Bằng chứng

| Tệp | Nội dung |
|---|---|
| `image/VVTTGCT_05-01-cbnv-tw-man-bao-cao.png` | Màn báo cáo của `cbnv_tw_01` sau khi xuất |
| `files/BaoCaoVuViecTheoTgChiTiet_20260807_1638.xlsx` | Tệp Excel thật (6.636 byte) |
| `files/b64-234-VVTTGCT_05.json` | Bản mã hoá nguyên trạng đối tượng tệp trình duyệt nhận được |
