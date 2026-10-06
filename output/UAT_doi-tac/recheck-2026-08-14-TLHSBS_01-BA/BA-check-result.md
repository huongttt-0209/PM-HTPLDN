# TLHSBS_01 — Kết quả đo lại theo yêu cầu BA

## Phạm vi đo

- Môi trường: `https://18.143.165.120.nip.io`
- Tài khoản: `cbnv_tw_02` — Cán bộ Nghiệp vụ Trung ương #02
- Bộ lọc: Năm `2026` · Tháng `Cả năm` · Cấp đơn vị `Toàn quốc` · Đơn vị `Tất cả`
- Thời điểm quan sát: 14/08/2026, khoảng 15:29–15:31 (GMT+7)

## Hiện trạng

1. Dashboard hiển thị `Vụ việc hoàn thành: 23`.
2. Cùng lúc, thẻ `Tỷ lệ hồ sơ bổ sung` hiển thị `0%` và dòng `Chưa có dữ liệu`.
3. Bấm thẻ `Vụ việc hoàn thành` mở danh sách với bộ lọc:
   - Trạng thái: `HOAN_THANH, DA_DANH_GIA`
   - Trường ngày: `ngay_hoan_thanh`
   - Khoảng ngày: `01/01/2026–14/08/2026`
   - Tổng cộng: `23` kết quả.
4. Trong chính tập 23 vụ này có vụ `VV-BTP-TW-20260712-005`:
   - Trạng thái hiện tại: `Hoàn thành`.
   - Dòng thời gian có sự kiện `Bổ sung hồ sơ` lúc `15/07/2026 12:15`.
   - Dòng thời gian có sự kiện `Hoàn thành` lúc `25/07/2026 02:23`.

## Đối chiếu cách đọc của BA

| Nhánh BA nêu | Hiện trạng | Kết quả |
|---|---|---|
| Có ≥1 vụ hoàn thành và không vụ nào từng qua yêu cầu bổ sung | Có 23 vụ hoàn thành, nhưng đã tìm thấy ít nhất 1 vụ có lịch sử bổ sung | Không thỏa |
| Không có vụ hoàn thành mà thẻ vẫn hiện 0 | Có 23 vụ hoàn thành | Không thỏa |
| Có ≥1 vụ hoàn thành và có ≥1 vụ từng qua bổ sung | Đây là hiện trạng thực tế: ít nhất `1/23` | Thẻ phải lớn hơn 0%; hiển thị 0% là sai |

Theo KPI-S-01, dòng 567–580 của SRS: tử số là số vụ trong mẫu số từng qua trạng thái yêu cầu bổ sung ít nhất một lần; giá trị bằng tử số chia mẫu số nhân 100. Chỉ với một vụ đã chứng minh được, tỷ lệ tối thiểu đã là `1/23 × 100 ≈ 4,35%`, nên không thể bằng `0%`.

## Kết luận

`TLHSBS_01` vẫn là bug thật. Dữ liệu hiện tại không đủ điều kiện để khép `Reject`: mẫu số là 23 và đã có ít nhất một vụ hoàn thành từng qua bước bổ sung. Đồng thời đây cũng không phải nhánh mẫu số bằng 0 để đổi sang dấu `—`.

## Ảnh bằng chứng

- `image/01-dashboard-card-and-completed-count.png`: cùng bộ lọc, 23 vụ hoàn thành nhưng tỷ lệ hồ sơ bổ sung = 0%.
- `image/02-completed-list-23-records.png`: danh sách theo ngày hoàn thành trong kỳ, tab Hoàn thành có 23 kết quả.
- `image/03-completed-record-with-supplement.png`: vụ `VV-BTP-TW-20260712-005` đang ở trạng thái Hoàn thành.
- `image/04-record-timeline-supplement.png`: dòng thời gian của vụ trên có sự kiện Bổ sung hồ sơ ngày 15/07/2026.

## Lỗi phát hiện thêm ngoài phạm vi

- Không phát hiện thêm bất thường độc lập; dòng `Chưa có dữ liệu` trên thẻ là cùng biểu hiện của lỗi KPI-S-01.
