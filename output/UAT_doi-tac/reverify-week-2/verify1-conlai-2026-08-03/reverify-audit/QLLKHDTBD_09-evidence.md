# QLLKHDTBD_09 — Cổng 1 + Cổng 2 (AGENT-EVIDENCE, 2026-08-03)

> Sheet: `UAT_TGPL Doanh Nghiệp-tuần 2` row **119** · `fetch_evidence.py` **exit 0** (1 link Drive, tải được `QLLKHDTBD_09.webm`, 4.450.495 bytes).
> Ô "Ảnh/video 2" (cột T) **trống**. Video dài **~14,5 giây**, đã trích 5 frame/3s + 15 frame/1s.

## Cổng 1 — 3 dữ kiện neo

**(a) URL / mã bản ghi đối tác đang đứng**
- **`htpldn-uat.ospgroup.vn/dao-tao/ke-hoach/danh-sach?tuNgay=2026-07-01&denNgay=2026-07-31&page=1`**
- Màn: `Đào tạo, tập huấn → Kế hoạch đào tạo → Danh sách` (CMS).
- **Bộ lọc nằm ngay trên URL**: `tuNgay=2026-07-01`, `denNgay=2026-07-31`, `page=1` — đây là bằng chứng neo mạnh nhất của case.
- File Excel tải về: **`ke-hoach-dao-tao-1784950244818.xlsx`**, sheet trong file tên **`Kế hoạch đào tạo`**.

**(b) Trạng thái entity**
- Tab lọc trạng thái đang chọn: **`Tất cả` (2)**. Các tab còn lại: `Nháp` (0), `Chờ duyệt` (**1**), `Đã duyệt` (**1**), `Từ chối` (0), `Đã công khai` (0).
- 2 bản ghi hiện trên bảng:
  | Mã kế hoạch | Năm | Từ ngày | Đến ngày | Ngân sách (VNĐ) | Trạng thái |
  |---|---|---|---|---|---|
  | `KH-20260725-0001` | 2026 | 01/07/2026 | 31/07/2026 | 2.943.499.581,00 | **Chờ duyệt** |
  | `KH-20260723-0001` | 2026 | 01/07/2026 | 28/07/2026 | 1.000.000.000,00 | **Đã duyệt** |
- Chân bảng ghi rõ: **`Hiển thị 1-2 / 2 kết quả`**, phân trang `20 / trang`, chỉ 1 trang.

**(c) Dữ liệu tiền đề**
- Bộ lọc trên UI: ô `Tìm theo tên hoặc mã kế hoạch` **trống**, ô `Năm kế hoạch` **trống**, **`Từ ngày = 01/07/2026`**, **`Đến ngày = 31/07/2026`**. Nút `Xóa bộ lọc`, `Tìm kiếm`.
- DB thực tế (đọc ngược từ file Excel) có **12 kế hoạch** trải nhiều đơn vị (TW/BTP, BN/BTC, DP/STP Bắc Giang, An Giang) và đủ 5 trạng thái.

## Cổng 2 — 3 dòng

**(1) Evidence đã xem + frame chứa LỖI**
`partner-evidence/QLLKHDTBD_09.webm`. Chuỗi frame:
- `t000.00s` (10:30 AM 2026-07-25) — baseline: URL có `tuNgay/denNgay`, bảng **2 dòng**, chân bảng **"Hiển thị 1-2 / 2 kết quả"**.
- `t008.20s` — bấm `Xuất Excel`: toast xanh **"✅ Xuất Excel thành công"** + hộp thoại Save As `ke-hoach-dao-tao-1784950244818.xlsx`; **bộ lọc trên màn vẫn nguyên `01/07/2026`–`31/07/2026` và vẫn "Hiển thị 1-2 / 2 kết quả"**.
- **`t011.28s` / `t014.51s` = FRAME LỖI:** file mở bằng Excel (Protected View), sheet `Kế hoạch đào tạo`, header `Mã KH · Tên kế hoạch · Năm · Từ ngày · Đến ngày · Ngân sách (VNĐ) · Trạng thái`, dữ liệu chạy **từ dòng 2 đến dòng 13 = 12 bản ghi**:

| # | Mã KH | Tên kế hoạch | Từ ngày | Đến ngày | Trạng thái |
|---|---|---|---|---|---|
| 1 | KH-20260725-0001 | Kế hoạch kiểm thử TKM lần 2-retest | 1/7/2026 | 31/7/2026 | Chờ duyệt |
| 2 | KH-20260723-0001 | Kế hoạch kiểm thử HTPLDN 2026 | 1/7/2026 | 28/7/2026 | Đã duyệt |
| 3 | KH-20260525-0001 | Kế hoạch đào tạo luật doanh nghiệp năm quý 3 n… | 1/7/2026 | 30/9/2026 | Đã duyệt |
| 4 | KH-20260515-0001 | Kế hoạch đào tạo bồi dưỡng nghiệp vụ Hỗ trợ ph… | 15/5/2026 | 30/6/2026 | Chờ duyệt |
| 5 | KHDT-HDSD-AG-001 | Kế hoạch đào tạo HTPLDN An Giang 2026 | 1/1/2026 | 31/12/2026 | Đã duyệt |
| 6 | KH-20260509-0003 | KH ĐT năm 2026 - Cấp DP (STP Bắc Giang) - R9 | 1/1/2026 | 31/12/2026 | Nháp |
| 7 | KH-20260509-0002 | KH ĐT năm 2026 - Cấp BN (BTC) - R9 | 1/1/2026 | 31/12/2026 | Từ chối |
| 8 | KH-20260509-0001 | KH ĐT năm 2026 - Cấp TW (BTP) - R9 | 1/1/2026 | 31/12/2026 | Đã duyệt |
| 9 | KH-20260508-0006 | KH ĐT năm 2026 - Cấp DP (STP Bắc Giang) - R8 | 31/12/2025 | 30/12/2026 | Đã công khai |
| 10 | KH-20260508-0005 | KH ĐT năm 2026 - Cấp BN (BTC) - R8 | 31/12/2025 | 30/12/2026 | Đã công khai |
| 11 | KH-20260508-0004 | KH ĐT năm 2026 - Cấp TW (BTP) - R8 | 31/12/2025 | 30/12/2026 | Đã duyệt |
| 12 | KH-20260508-0001 | KH ĐT năm 2026 - Cấp TW (BTP) | 31/12/2025 | 30/12/2026 | Đã công khai |

- 1 câu tả lỗi: *màn danh sách đang lọc `01/07/2026 → 31/07/2026` và chỉ có **2** kết quả, nhưng file Excel xuất ra chứa **12** kế hoạch, gồm cả những kế hoạch nằm hoàn toàn ngoài khoảng lọc (vd `15/5/2026–30/6/2026`, `31/12/2025–30/12/2026`).*

**(2) Đối tác phản ánh CỤ THỂ gì**
Không phải sai cột, không phải lỗi file hỏng — mà là **file Excel không áp bộ lọc đang có trên màn**: xuất **toàn bộ 12 bản ghi** thay vì đúng **2 bản ghi** khớp `tuNgay/denNgay`. Kết quả mong đợi ở sheet: *"Hệ thống xuất danh sách … theo điều kiện lọc hiện tại ra tệp Excel."*

**(3) Data + bước tái hiện chính xác**
1. Đăng nhập **Cán bộ nghiệp vụ Trung ương** (`CB_NV_TW`, `BTP · TW`).
2. Menu `Đào tạo, tập huấn` → `Kế hoạch đào tạo`.
3. Đặt bộ lọc **`Từ ngày = 01/07/2026`**, **`Đến ngày = 31/07/2026`**, tab **`Tất cả`**, các ô còn lại để trống → bấm `Tìm kiếm`. URL phải thành `?tuNgay=2026-07-01&denNgay=2026-07-31&page=1`.
4. **Ghi lại số kết quả trên chân bảng** (đối tác: `Hiển thị 1-2 / 2 kết quả`).
5. Bấm **`Xuất Excel`** → mở file → **đếm số dòng dữ liệu** và đối chiếu với số ở bước 4.

## Vai trò / tài khoản đối tác dùng

`Cán bộ NV Trung ương` — mã **`CB_NV_TW`**, đơn vị **`BTP · TW`** (header phải, frame `t000.00s`). Nhóm tài khoản sheet: `cbnv_tw`. Thời điểm quay: **10:30 AM 2026-07-25**.

## Ghi chú cho người verify

- **Đây là case đếm số (filter/count) — theo protocol Cổng 3 phải có baseline + query phân biệt + số bản ghi thực.** Bằng chứng đối tác đã đủ 3 mảnh: 12 bản ghi tổng, filter còn 2, file xuất 12.
- **Tiền đề bắt buộc dựng lại:** DB phải có **≥1 kế hoạch NẰM NGOÀI** khoảng `01/07–31/07/2026` thì mới phân biệt được. Nếu môi trường hiện tại chỉ còn đúng các kế hoạch trong khoảng lọc → **số 2 = số xuất ra là ngẫu nhiên trùng, KHÔNG kết luận được**. Cần seed thêm bản ghi ngoài khoảng trước khi test.
- **Bước 2 trong "Các bước thực hiện" của sheet ghi nhầm**: *"Bấm nút Gửi phê duyệt"* — trong video đối tác **không** bấm nút đó, chỉ đặt bộ lọc rồi `Xuất Excel`. Bám video, đừng bám câu chữ sheet.
- **Kiểm nội dung file, không chỉ kiểm file tạo được**: mở `.xlsx` bằng `openpyxl` và **đếm dòng + so từng `Từ ngày/Đến ngày`** với khoảng lọc. HTTP 200 + có binary chỉ chứng minh CREATE, không chứng minh CORRECT.
- Phản hồi dev ở sheet (cột P=`Reject`, cột R): *"Xuất Excel dùng chung query builder với danh sách + cap 10.000 dòng (BR-DATA-06) → đã áp đủ điều kiện lọc. 'Xuất toàn bộ' không tái hiện (do build cũ / chưa đặt bộ lọc)."* — video đã chứng minh đối tác **CÓ đặt bộ lọc** (URL mang `tuNgay/denNgay` + chân bảng ghi 1-2/2). Người verify cần **tải lại trang + ghi tên bản dựng** rồi mới kết luận là fix hay chưa.

## File evidence + frame đã dùng

| Loại | Đường dẫn tuyệt đối |
|---|---|
| Video gốc | `/Users/huongttt/Downloads/antigravity/PM HTPLDN/skilkk/output/UAT_doi-tac/reverify-week-2/verify1-conlai-2026-08-03/partner-evidence/QLLKHDTBD_09.webm` |
| Frame baseline (filter + "1-2 / 2 kết quả") | `…/frames/QLLKHDTBD_09/dense/t000.00s.jpg` (và `t005.12s.jpg`) |
| Frame toast "Xuất Excel thành công" + Save As | `…/frames/QLLKHDTBD_09/dense/t008.20s.jpg` |
| **Frame LỖI — Excel 12 dòng** | `…/frames/QLLKHDTBD_09/dense/t011.28s.jpg` và `…/dense/t014.51s.jpg` |

*(Thư mục gốc frame: `/Users/huongttt/Downloads/antigravity/PM HTPLDN/skilkk/output/UAT_doi-tac/reverify-week-2/verify1-conlai-2026-08-03/frames/QLLKHDTBD_09/`)*

## Ngoài lỗi đối tác nêu, trong frame còn thấy gì bất thường? (dựa trên ảnh ĐÃ ĐỌC)

1. **File Excel chứa kế hoạch của đơn vị KHÁC** — `KH ĐT năm 2026 - Cấp DP (STP Bắc Giang)`, `Cấp BN (BTC)`, `KHDT-HDSD-AG-001 (An Giang)` — trong khi người xuất là `CB_NV_TW` đơn vị `BTP · TW`. Có thể đúng theo phạm vi dữ liệu của cấp TW, nhưng nếu SRS giới hạn scope thì đây là **rò rỉ phạm vi dữ liệu qua đường xuất file**, đáng soi riêng.
2. **Excel xuất cả bản ghi trạng thái `Nháp`** (`KH-20260509-0003`) và `Từ chối` (`KH-20260509-0002`) — bản nháp của đơn vị khác lọt vào file xuất.
3. **Cột `Ngân sách (VNĐ)` trống ở dòng 6** (`KHDT-HDSD-AG-001`) trong khi 11 dòng còn lại đều có số.
4. **Ngày trong Excel không thống nhất định dạng với UI**: UI hiện `01/07/2026`, Excel hiện `1/7/2026`; và có bản ghi `Từ ngày = 31/12/2025` nhưng `Năm = 2026`.
5. **Bảng trên UI có cột thứ 2 (ngay sau `Mã kế hoạch`) rỗng hoàn toàn ở cả 2 dòng** — nhìn header thì cột `Tên kế hoạch` bị mất nhãn/mất dữ liệu trên màn danh sách, dù trong Excel tên kế hoạch có đủ. Có thể do cuộn ngang, nhưng ở frame `t000.00s` khoảng trắng nằm giữa `Mã kế hoạch` và `Năm` rất rõ.

*(Tất cả đọc trực tiếp từ pixel frame, không suy đoán. Chưa log bug — thuộc quyền người verify.)*
