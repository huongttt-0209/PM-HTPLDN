# QLHDTVVCG_16 — dòng 322 · 07/08/2026 16:00–16:10 · tài khoản **`cbnv_tw_05`** (CB NV TW, Cục Bổ trợ tư pháp) · bản dựng `assets/index-BbPPdate.js` (`last-modified` 07/08/2026 06:47:57 GMT)

> Chuẩn chấm khóa: [`chuan/QLHDTVVCG_16.md`](../chuan/QLHDTVVCG_16.md) — **4 vế: C1 `MATCH` · C2 `GAP` · C3 `MATCH` · C4 `DIFF`**.
> Chế độ rút gọn §8: C1/C3 chạy trọn luồng + 2 đường đo; C2/C4 chỉ liếc hiện trạng (thấy ngay trên chính tệp vừa xuất, chi phí ≈ 0).
> Đọc lại dòng 322 lúc 15:58: `Trạng thái` `N/R` · `Kết quả thực tế` RỖNG · `R` = `Fixed` · `T` RỖNG — không có phiên khác vừa ghi.

## Đường vào

**Màn 1** (bề mặt chấm chính thức): Vụ việc HTPL → tìm `VV-BTP-TW-20260804-002` → mở chi tiết → bung mục **"HĐ tư vấn liên kết"**
(`/vu-viec/6bf98a2e-77ee-4c03-8e1f-a51561406a3b`). Bước J ghi *"Chọn menu Hợp đồng Tư vấn"* — menu đã bỏ theo `:266`/`:268`,
là **tiền đề**, không phải vế chấm. Ảnh 01.

**Nền trước thao tác:** mọi ô lọc trống, bảng **2 dòng** (`HDTV-20260807-0007`, `HDTV-20260807-0006`), phân trang *"1-2 / 2 mục"*.
Từ khóa dùng là **chuỗi không dấu** `UAT QLNDTVVCG` — cố ý tránh lớp từ khóa tiếng Việt có dấu đang hỏng ở `_03`, để lỗi kia
không làm bẩn phép đo này.

## Kết quả từng vế

| Vế | Quan hệ | Kỳ vọng phiếu | Web thực tế | Đạt? | Ảnh |
|---|---|---|---|---|---|
| **C1** | MATCH | Xuất theo **toàn bộ bộ lọc đang hiển thị** + phân quyền dữ liệu theo đơn vị (`:132`, `:133`, `:184`) | Lọc `UAT QLNDTVVCG` → bảng còn **1 dòng** `HDTV-20260807-0006` (*"1-1 / 1 mục"*) → bấm **[Xuất Excel] bằng chuột**. **Mở tệp bằng `openpyxl`: đúng 1 dòng tiêu đề + 1 dòng dữ liệu, mã `HDTV-20260807-0006`** — khớp danh tính, không phải chỉ khớp số lượng. **Đối chứng độc lập:** xóa bộ lọc (bảng về 2 dòng) rồi xuất lần nữa → tệp thứ hai có **2 dòng dữ liệu** `0007` + `0006`. Hai tệp khác nhau đúng bằng phần bộ lọc cắt đi ⇒ bộ lọc được áp thật. Cả hai tệp đều **không** chứa 5 hợp đồng còn lại của hệ thống ⇒ giữ đúng phạm vi ngữ cảnh vụ việc; cột Bên A của mọi dòng đều là `Cục Bổ trợ tư pháp - Bộ Tư pháp` = đơn vị của tài khoản | ✅ | 01 · 02 · tệp 1606 · tệp 1607 |
| **C2** | GAP | *"gồm các cột đang hiển thị trên màn hình danh sách"* | **12 cột** trong tệp: Mã hợp đồng · Tên hợp đồng · **Số hợp đồng** · Bên A · Bên B · Giá trị · **Ngày ký** · Ngày bắt đầu · Ngày kết thúc · Số vụ việc liên kết · Tiến độ thanh toán (%) · Trạng thái. Màn hình có **11 cột** (10 cột dữ liệu + *Hành động*). Tệp **thừa** 2 cột (`Số hợp đồng`, `Ngày ký` — cả hai đang rỗng), **thiếu** cột *Hành động* (vốn là nút bấm, không phải dữ liệu). Tên trang tính: *"Hợp đồng tư vấn"* | — (không chấm) | tệp 1606 |
| **C3** | MATCH | ≤ **10.000 dòng**, không bị cắt (`:134`) | Tệp lọc: **1** dòng dữ liệu / tập hiển thị 1 ⇒ không cắt. Tệp không lọc: **2** / 2 ⇒ không cắt. Cả hai ≪ 10.000. **Giới hạn hiệu lực đã ghi rõ:** môi trường chỉ ~1.000 bản ghi/năm (`:398`) nên **không dựng được ca chạm ngưỡng**; ngoài ra lời gọi xuất có kèm `pageSize: 20` nên **chưa chứng minh được** hành vi khi tập lọc > 20 dòng — cấm seed 10.000 bản ghi để thử | ✅ (trong giới hạn đã nêu) | tệp 1606 · 1607 |
| **C4** | DIFF | Tên tệp `HDTV-danh-sach-{YYYYMMDD-HHmm}.xlsx` | Tên tệp **máy chủ trả về** (đọc từ tiêu đề `content-disposition` của chính lời gọi tải, không phải tên tự đặt): **`HdtvDanhSach_20260807_1606.xlsx`** (lần hai: `HdtvDanhSach_20260807_1607.xlsx`) — viết liền PascalCase, ngăn bằng dấu gạch dưới, **không** có dấu gạch nối. Tức **đúng khuôn §H8 của SRS**, **ngược** khuôn đối tác kỳ vọng | — (không chấm) | tệp 1606 · 1607 |

**Chống Pass oan đã làm đủ:** mở tệp bằng `openpyxl` đọc nội dung thật (không chấm bằng "tệp tải về được"); đếm **riêng** dòng tiêu đề
và dòng dữ liệu; so **mã hợp đồng từng dòng** chứ không chỉ số lượng; có ca **đối chứng không lọc** nên số dòng khớp không phải trùng hợp.

**Chống Fail oan đã kiểm:** không Fail C4 vì tên tệp lệch kỳ vọng đối tác (đó chính là điểm `DIFF`); không Fail C2 vì thừa/thiếu cột
(chính SRS ghi *"cần CĐT xác nhận template"*); không Fail vì thiếu cột *Hành động* (là nút, `:147`–`:155` không có); không đòi khổ A4 /
Times New Roman 13 (yêu cầu đó của nhóm báo cáo, không khai cho nhóm X.3).

## Verdict → ô R

**`BA confirm`** — **2/2 vế `MATCH` (C1, C3) đều đạt**, nhưng còn **1 `DIFF` (C4) + 1 `GAP` (C2)** ⇒ theo QĐ-01 hàng 3.

## Dữ liệu đã đổi

**KHÔNG có.** Phiếu chỉ đọc + tải tệp; không tạo/sửa/xóa bản ghi nào, không đụng dữ liệu đối tác.
Hai tệp xuất được giữ lại ở `files/xuat-hdtv/` và đã tải lên Drive.

## Ảnh / tệp bằng chứng (đã mở lại xem trước khi dùng)

| # | Nội dung | Liên kết xem được |
|---|---|---|
| 01 | Nền trước khi lọc: mục "HĐ tư vấn liên kết" của `VV-BTP-TW-20260804-002` có **2** hợp đồng, *"1-2 / 2 mục"* | https://drive.google.com/file/d/1UvOvWq44uUtBS75cokcKfjYkQxXYR6OZ/view?usp=drivesdk |
| 02 | Sau khi lọc `UAT QLNDTVVCG`: còn **1** dòng `HDTV-20260807-0006`, *"1-1 / 1 mục"* — chụp **ngay trước** khi bấm Xuất Excel | https://drive.google.com/file/d/1g4-4O2pkg93Itqlff3xcCiTnif3d1bV3/view?usp=drivesdk |
| tệp 1606 | **Tệp thật** hệ thống trả khi đang lọc: `HdtvDanhSach_20260807_1606.xlsx` — 1 dòng dữ liệu `HDTV-20260807-0006`, 12 cột | https://docs.google.com/spreadsheets/d/1ktFZMeHroP7bIveTKGrsUuRbtCqSM4la/edit?usp=drivesdk&rtpof=true&sd=true |
| tệp 1607 | Tệp đối chứng khi **đã xóa bộ lọc**: 2 dòng dữ liệu `0007` + `0006` | https://docs.google.com/spreadsheets/d/1rergJSTZRSIuqgG9xngGj7Tu87U8Jr7T/edit?usp=drivesdk&rtpof=true&sd=true |
