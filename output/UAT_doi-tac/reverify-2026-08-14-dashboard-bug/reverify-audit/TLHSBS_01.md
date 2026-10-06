# TLHSBS_01 — audit verify vòng đầu

## Ba cổng

- Evidence đã xem: `partner-evidence/TLHSBS_01.jpg`, ảnh tĩnh full-res; lỗi nhìn thấy tại thẻ “Tỷ lệ hồ sơ bổ sung”: `0%`, “Chưa có dữ liệu”.
- Đối tác phản ánh cụ thể: tỷ lệ hiển thị 0 dù tồn tại hồ sơ cần bổ sung.
- Data + bước tái hiện: đăng nhập `cbnv_tw_02` → Dashboard → năm 2026 / Cả năm / Toàn quốc / Tất cả; đối chiếu một vụ hoàn thành có lịch sử bổ sung hồ sơ.

## Dữ kiện neo

- URL/ID: `/dashboard`; vụ đối chiếu `/vu-viec/cf90a65c-5fe0-4687-bbed-50538b0341c0`, mã `VV-BTP-TW-20260712-005`.
- Trạng thái: vụ `Hoàn thành` ngày 25/07/2026; dòng thời gian có `Bổ sung hồ sơ` ngày 15/07/2026.
- Tiền đề: cùng phạm vi Toàn quốc, năm 2026; Dashboard có 23 vụ hoàn thành.

## Đối chiếu SRS với web

| SRS yêu cầu | Thực tế web | Đủ/thiếu |
|---|---|---|
| KPI-S-01, dòng 567-580: tử số là số vụ trong mẫu số đã từng đi qua trạng thái “Yêu cầu bổ sung” ít nhất một lần; giá trị = tử số / mẫu số × 100 | Có ít nhất 1 vụ hoàn thành từng có bước “Bổ sung hồ sơ”, nhưng thẻ trả 0% | Thiếu |
| Dòng 589-591: có vụ hoàn thành từng qua bổ sung thì tỷ lệ phải phản ánh tử số; chỉ khi không có vụ hoàn thành mới hiển thị trống | Dashboard có 23 vụ hoàn thành nhưng hiển thị thêm “Chưa có dữ liệu” | Thiếu |

## Artifact quan sát

- `image/TLHSBS_01-dashboard-live.png`: Dashboard cùng filter, 23 vụ hoàn thành và tỷ lệ 0%.
- `image/TLHSBS_01-record-history.png`: vụ hoàn thành và dòng thời gian có bước “Bổ sung hồ sơ”.

## Lỗi phát hiện thêm ngoài phạm vi

- Không phát hiện thêm bất thường độc lập ngoài lỗi tỷ lệ và hai case click đã được giao riêng.
