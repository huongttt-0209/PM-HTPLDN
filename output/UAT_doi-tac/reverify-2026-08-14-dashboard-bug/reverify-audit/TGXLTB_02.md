# TGXLTB_02 — audit verify vòng đầu

## Ba cổng

- Evidence đã xem: `partner-evidence/TGXLTB_01.jpg`, ảnh tĩnh full-res; thẻ “Thời gian xử lý trung bình” ở Dashboard, phản ánh bấm không mở danh sách.
- Đối tác phản ánh cụ thể: bấm thẻ thời gian trung bình phải mở danh sách nhưng web không điều hướng.
- Data + bước tái hiện: đăng nhập `cbnv_tw_02` → Dashboard → năm 2026 / Cả năm / Toàn quốc / Tất cả → bấm thẻ “Thời gian xử lý trung bình”.

## Dữ kiện neo

- URL trước và sau thao tác: `https://18.143.165.120.nip.io/dashboard`; history length không đổi.
- Thẻ là nội dung tĩnh trong cây accessibility, không được công bố là button.
- Phạm vi: Toàn quốc, năm 2026, Cả năm, Tất cả đơn vị.

## Đối chiếu SRS với web

| SRS yêu cầu | Thực tế web | Đủ/thiếu |
|---|---|---|
| KPI-S-02, dòng 596-615: hiển thị thời gian xử lý trung bình; `Drill-down: không có` | Bấm thẻ không mở danh sách, URL và history length giữ nguyên | Đủ theo SRS |
| Expected của đối tác: bấm thẻ mở danh sách thời gian xử lý trung bình | SRS hiện hành không quy định màn danh sách/drill-down | Cần BA xác nhận thay đổi đặc tả |

## Artifact quan sát

- `image/TGXLTB_02-before-click.png`: trạng thái trước thao tác.
- `image/TGXLTB_02-after-click.png`: trạng thái ổn định sau thao tác, vẫn ở Dashboard.
- `reverify-audit/TGXLTB_02-a11y.txt`: cây accessibility xác nhận nhãn KPI là `StaticText`, trong khi các KPI có drill-down là `button`.
- `reverify-audit/TGXLTB_02-click-measure.json`: đo URL và history length trước-sau khi click đúng thẻ; cả hai không đổi.
- Network sau thao tác chỉ có request Dashboard/thông báo/session hiện hữu, không có request mở danh sách.

## Kết luận

- `BA confirm`, không ghi bug report: hành vi web khớp SRS nhưng khác expected của đối tác.

## Lỗi phát hiện thêm ngoài phạm vi

- Không phát hiện thêm bất thường độc lập.
