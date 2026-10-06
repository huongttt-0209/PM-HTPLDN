# Dòng 263 — `CPCTHTTTG_05` — BC Chi phí theo thời gian · Xuất Excel

**Verdict: ✅ Test done** (bug gốc hết)

---

## 1. Bug gốc là gì

| Nguồn | Nội dung |
|---|---|
| Kết quả mong đợi (cột K) | "Hệ thống xuất toàn bộ và tự động tải tệp về máy người dùng. Tên tệp xuất: `BaoCaoChiPhi_{YYYYMMDD_HHmm}.xlsx`" |
| Kết quả thực tế (cột L) | "Hệ thống hiển thị thông báo **"Không thể tạo file xuất. Vui lòng thử lại."**" |

**Đạt khi:** bấm [Xuất Excel] ra được tệp thật, tải về máy, không còn thông báo từ chối đó.

**Ngoài phạm vi (BRIEF §PHẠM VI, không dùng để chặn Pass):** QTHT xem được báo cáo rồi mới bị chặn ở
bước Xuất · chữ tiếng Anh "Forbidden" · thiếu mã lỗi tiếng Việt.

---

## 2. Đo thế nào

| Hạng mục | Giá trị |
|---|---|
| Môi trường | `https://18.143.165.120.nip.io` |
| Bó mã FE | `assets/index-BbPPdate.js` · `GET /` last-modified `Fri, 07 Aug 2026 06:47:57 GMT` (nhãn sidebar `HTPLDN · V1.0.10`) |
| Vai trò | `cbnv_tw_01` — Cán bộ Nghiệp vụ Trung ương (`srs-fr-11-bao-cao.md:51`, `:62`) |
| Giờ đo | 07/08/2026 ~16:40 giờ VN |
| Bộ lọc | Loại báo cáo = **BC Chi phí theo thời gian** · Kỳ = **Năm** · 01/01/2026 → 31/12/2026 · Đơn vị = Toàn quốc |

Trang tải lại từ đầu trước khi đo. Bấm nút thật [Xem báo cáo] → [Xuất Excel].

---

## 3. Thấy gì

### 3.1 Không còn thông báo từ chối

`Đang tạo file...` → chữ trong chính khung đó đổi thành `Tạo file thành công.` (~0,07 s sau).
Không có "Không thể tạo file xuất. Vui lòng thử lại.", không có "Forbidden".

### 3.2 Tệp thật đã về máy

- `POST /api/v1/bao-cao/export` → **200**, `content-disposition: attachment; filename="BaoCaoChiPhiTheoThoiGian_20260807_1640.xlsx"`.
- Đối tượng tệp **6.660 byte**, kiểu `…spreadsheetml.sheet`; trình duyệt kích hoạt tải xuống đúng tên đó.
- Tên tệp đúng khuôn `{TenBaoCao}_{YYYYMMDD_HHmm}.xlsx` (`srs-fr-11-bao-cao.md:85`).

### 3.3 MỞ TỆP RA ĐỌC

`files/BaoCaoChiPhiTheoThoiGian_20260807_1640.xlsx`, mở bằng `openpyxl`: chữ ký `PK\x03\x04`,
1 trang tính **"Chi phí theo thời gian"**, 16 dòng × 5 cột, đủ 4 mục đầu tệp.

| Mục | Giá trị trong tệp | Giá trị trên màn |
|---|---|---|
| Tổng chi phí toàn kỳ | 23000000 | 23,000,000 |
| Tổng hồ sơ toàn kỳ | 2 | 2 |
| Theo kỳ — Năm 2026 | 01/01/2026 · 31/12/2026 · 2 hồ sơ · 23000000 | 01/01/2026 · 31/12/2026 · 2 · 23.000.000 ₫ |

Khớp từng con số với màn hình.

---

## 4. Verdict + vì sao

**✅ Test done.** Triệu chứng gốc ở cột L không còn tái hiện với đúng tác nhân của chức năng báo cáo.
Tệp Excel sinh ra là tệp thật, tải về được, mở ra đọc thấy đủ đầu mục và số liệu khớp màn — thoả
"xuất toàn bộ và tự động tải tệp về máy" của Kết quả mong đợi.

Hai điểm từng nêu ở lượt verify trước (QTHT xem được rồi mới bị chặn ở bước Xuất; chữ "Forbidden")
đều **không phải triệu chứng ghi ở cột L** nên theo phạm vi lô này không dùng để giữ phiếu ở trạng
thái còn lỗi. BA cũng đã chốt 06/08 rằng việc máy chủ chặn vai trò Quản trị hệ thống là đúng —
`srs-fr-11-bao-cao.md:79` nay đã ghi rõ "Vai trò khác (kể cả QTHT) → chặn ngay ở cửa vào".

---

## 5. Bằng chứng

| Tệp | Nội dung |
|---|---|
| `image/CPCTHTTTG_05-01-cbnv-tw-man-bao-cao.png` | Màn báo cáo của `cbnv_tw_01` sau khi xuất |
| `files/BaoCaoChiPhiTheoThoiGian_20260807_1640.xlsx` | Tệp Excel thật (6.660 byte) |
| `files/b64-263-CPCTHTTTG_05.json` | Bản mã hoá nguyên trạng đối tượng tệp trình duyệt nhận được |
