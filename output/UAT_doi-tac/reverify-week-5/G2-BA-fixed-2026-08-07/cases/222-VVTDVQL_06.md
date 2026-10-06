# Dòng 222 — `VVTDVQL_06` — BC Vụ việc theo đơn vị quản lý · Xuất Excel

**Verdict: ✅ Test done** (bug gốc hết)

---

## 1. Bug gốc là gì

| Nguồn | Nội dung |
|---|---|
| Kết quả mong đợi (cột K) | "Hệ thống xuất toàn bộ và tự động tải tệp về máy người dùng. Tên tệp xuất: `BaoCaoVuViec_{YYYYMMDD_HHmm}.xlsx`" |
| Kết quả thực tế (cột L) | "Hệ thống hiển thị thông báo **"Không thể tạo file xuất. Vui lòng thử lại."**" |

**Đạt khi:** xuất ra được tệp thật, tải về máy, không còn thông báo đó.

**Ngoài phạm vi — BRIEF §PHẠM VI liệt kê đích danh:** "tệp xuất thiếu cột cấp đơn vị". Vẫn mở tệp đọc
để chứng minh tệp **thật**, nhưng **không audit tệp thiếu bảng/cột nào**.

---

## 2. Đo thế nào

| Hạng mục | Giá trị |
|---|---|
| Môi trường | `https://18.143.165.120.nip.io` |
| Bó mã FE | `assets/index-BbPPdate.js` · `GET /` last-modified `Fri, 07 Aug 2026 06:47:57 GMT` (nhãn sidebar `HTPLDN · V1.0.10`) |
| Vai trò | `cbnv_tw_01` — Cán bộ Nghiệp vụ Trung ương (`srs-fr-11-bao-cao.md:51`, `:62`) |
| Giờ đo | 07/08/2026 ~16:46 giờ VN |
| Bộ lọc | Loại báo cáo = **BC Vụ việc theo đơn vị quản lý** · Kỳ = **Năm** · 01/01/2026 → 31/12/2026 · Đơn vị = Toàn quốc |

Trang tải lại từ đầu trước khi đo. Bấm nút thật [Xem báo cáo] → [Xuất Excel].

> Bó mã hiện tại **trùng khít** với bó mã của lượt Reopen 07/08 lúc 15:26–16:09 ⇒ chạy **lượt xác nhận
> rút gọn** theo BRIEF (xuất 1 tệp, mở đọc), không diễn lại sweep 2 vai trò.

---

## 3. Thấy gì

### 3.1 Không còn thông báo từ chối

`Đang tạo file...` → chữ trong chính khung đó đổi thành `Tạo file thành công.` (~0,08 s sau).
Không có "Không thể tạo file xuất. Vui lòng thử lại.", không có "Forbidden".

### 3.2 Tệp thật đã về máy

- `POST /api/v1/bao-cao/export` → **200**, `content-disposition: attachment; filename="BaoCaoVuViecTheoDonVi_20260807_1646.xlsx"`.
- Đối tượng tệp **6.834 byte**, kiểu `…spreadsheetml.sheet`; trình duyệt kích hoạt tải xuống đúng tên đó.
- Tên tệp đúng khuôn `{TenBaoCao}_{YYYYMMDD_HHmm}.xlsx` (`srs-fr-11-bao-cao.md:85`).

### 3.3 MỞ TỆP RA ĐỌC — chứng minh tệp thật

`files/BaoCaoVuViecTheoDonVi_20260807_1646.xlsx`, mở bằng `openpyxl`: chữ ký `PK\x03\x04`,
1 trang tính **"Vụ việc theo đơn vị"**, 15 dòng × 6 cột, đủ 4 mục đầu tệp.

| Đơn vị | Mới | Tiếp nhận | Đang hỗ trợ | Hoàn thành | Tổng |
|---|---|---|---|---|---|
| Bộ Kế hoạch và Đầu tư | 0 | 0 | 2 | 2 | 4 |
| Cục Bổ trợ tư pháp - Bộ Tư pháp | 2 | 13 | 4 | 17 | 40 |
| Sở Tư pháp An Giang | 0 | 2 | 4 | 1 | 8 |
| Sở Tư pháp Hà Nội | 0 | 3 | 3 | 1 | 7 |

Khớp từng con số với bảng trên màn; 4+40+8+7 = **59**, khớp ô "Tổng số vụ việc: 59".

---

## 4. Verdict + vì sao

**✅ Test done.** Triệu chứng gốc ghi ở cột L không còn tái hiện. Thao tác xuất ra tệp Excel thật,
tải về máy, mở ra đọc được và số liệu khớp màn — đúng điều kiện "Đạt khi" mà BRIEF chốt cho dòng này.

Điểm "tệp thiếu cột cấp đơn vị" nêu ở lượt trước nay nằm **ngoài phạm vi lô** (BRIEF §PHẠM VI liệt kê
đích danh) nên không dùng để giữ phiếu ở trạng thái còn lỗi.

---

## 5. Bằng chứng

| Tệp | Nội dung |
|---|---|
| `image/VVTDVQL_06-01-cbnv-tw-man-bao-cao.png` | Màn báo cáo của `cbnv_tw_01` sau khi xuất |
| `files/BaoCaoVuViecTheoDonVi_20260807_1646.xlsx` | Tệp Excel thật (6.834 byte) |
| `files/b64-222-VVTDVQL_06.json` | Bản mã hoá nguyên trạng đối tượng tệp trình duyệt nhận được |
