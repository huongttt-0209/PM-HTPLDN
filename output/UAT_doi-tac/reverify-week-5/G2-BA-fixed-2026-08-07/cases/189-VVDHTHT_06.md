# Dòng 189 — `VVDHTHT_06` — BC Vụ việc đã hoàn thành · Xuất Excel

**Verdict: ✅ Test done** (bug gốc hết)

---

## 1. Bug gốc là gì

| Nguồn | Nội dung |
|---|---|
| Kết quả mong đợi (cột K) | "Hệ thống xuất toàn bộ và tự động tải tệp về máy người dùng." |
| Kết quả thực tế (cột L) | "Hệ thống hiển thị thông báo **"Không thể tạo file xuất. Vui lòng thử lại."**" (lượt 31/7 là chữ `Forbidden`) |

**Đạt khi (bảng "Bug gốc — chốt trước khi đo" của BRIEF):** xuất ra được tệp thật, tải về máy,
không còn 2 thông báo đó.

**Ngoài phạm vi — BRIEF §PHẠM VI liệt kê đích danh, KHÔNG dùng để giữ phiếu ở trạng thái còn lỗi:**
"tệp xuất thiếu bảng theo kỳ". Vẫn mở tệp ra đọc để chứng minh tệp **thật**, nhưng **không audit
tệp thiếu bảng nào**.

---

## 2. Đo thế nào

| Hạng mục | Giá trị |
|---|---|
| Môi trường | `https://18.143.165.120.nip.io` |
| Bó mã FE | `assets/index-BbPPdate.js` · `GET /` last-modified `Fri, 07 Aug 2026 06:47:57 GMT` (nhãn sidebar `HTPLDN · V1.0.10`) |
| Vai trò | `cbnv_tw_01` — Cán bộ Nghiệp vụ Trung ương (`srs-fr-11-bao-cao.md:51`, `:62`) |
| Giờ đo | 07/08/2026 ~16:43 giờ VN |
| Bộ lọc | Loại báo cáo = **BC Vụ việc đã hoàn thành** · Kỳ = **Năm** · 01/01/2026 → 31/12/2026 · Đơn vị = Toàn quốc |

Trang tải lại từ đầu trước khi đo. Bấm nút thật [Xem báo cáo] → [Xuất Excel].

> Bó mã hiện tại **trùng khít** với bó mã của lượt Reopen 07/08 lúc 15:26–16:09, tức chưa có bản dựng
> mới nào kể từ lượt đó. Vì vậy chạy **lượt xác nhận rút gọn** theo BRIEF (xuất 1 tệp, mở đọc), không
> diễn lại sweep 2 vai trò.

---

## 3. Thấy gì

### 3.1 Không còn thông báo từ chối

`Đang tạo file...` → chữ trong chính khung đó đổi thành `Tạo file thành công.` (~0,07 s sau).
**Không có** "Không thể tạo file xuất. Vui lòng thử lại." và **không có** "Forbidden".

### 3.2 Tệp thật đã về máy

- `POST /api/v1/bao-cao/export` → **200**, `content-disposition: attachment; filename="BaoCaoVuViecHoanThanh_20260807_1643.xlsx"`.
- Đối tượng tệp **7.133 byte**, kiểu `…spreadsheetml.sheet`; trình duyệt kích hoạt tải xuống đúng tên đó.

### 3.3 MỞ TỆP RA ĐỌC — chứng minh tệp thật, không rỗng/hỏng

`files/BaoCaoVuViecHoanThanh_20260807_1643.xlsx`, mở bằng `openpyxl`: chữ ký `PK\x03\x04`,
1 trang tính **"BC Vụ việc đã hoàn thành"**, 38 dòng × 2 cột, đủ 4 mục đầu tệp
(tên báo cáo / kỳ + khoảng thời gian / đơn vị / ngày tạo).

Số liệu trong tệp khớp màn: Tổng vụ việc hoàn thành **21** · Thành công **6** · Không thành công **0** ·
Tỷ lệ thành công **28,6%** · Theo lĩnh vực (Dân sự 11, Thương mại 8, Thuế 2) · Theo kết quả
(Chưa xác định 15, Thành công 6) · Theo đơn vị (Cục BTTP 17, Bộ KH&ĐT 2, Sở TP Hà Nội 1, Sở TP An Giang 1).

---

## 4. Verdict + vì sao

**✅ Test done.** Triệu chứng gốc ghi ở cột L — thông báo "Không thể tạo file xuất. Vui lòng thử lại."
(và chữ "Forbidden" ở lượt 31/7) — **không còn tái hiện**. Thao tác xuất ra tệp Excel thật, tải về máy,
mở ra đọc được và không rỗng/hỏng. Đúng điều kiện "Đạt khi" mà BRIEF chốt cho dòng này.

Điểm "tệp thiếu bảng theo kỳ" đã nêu ở lượt trước nay nằm **ngoài phạm vi lô** (BRIEF §PHẠM VI liệt kê
đích danh), nên không dùng để giữ phiếu ở trạng thái còn lỗi. Đã ghi 1 dòng vào
`99-quan-sat-ngoai-pham-vi.md` để không mất dấu.

---

## 5. Bằng chứng

| Tệp | Nội dung |
|---|---|
| `image/VVDHTHT_06-01-cbnv-tw-man-bao-cao.png` | Màn báo cáo của `cbnv_tw_01` sau khi xuất |
| `files/BaoCaoVuViecHoanThanh_20260807_1643.xlsx` | Tệp Excel thật (7.133 byte) |
| `files/b64-189-VVDHTHT_06.json` | Bản mã hoá nguyên trạng đối tượng tệp trình duyệt nhận được |
