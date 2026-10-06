# TLHSBS_01 — Re-verify sau Dev fix

- Ngày verify: 14/08/2026
- Môi trường: DEV, build `HTPLDN · v1.0.14`
- Account: `cbnv_tw_02`; OTP lấy qua MailHog
- Phương thức kết luận: thao tác và quan sát trên UI
- Verdict: **PASS**

## Nguyên nhân kết luận Reopen cũ bị sai

Hồ sơ cũ `VV-BTP-TW-20260712-005` có mốc thao tác `Bổ sung hồ sơ`, nhưng không có trạng thái `Yêu cầu bổ sung`. Đây là thao tác thêm tài liệu, không phải một lần hồ sơ đi qua nhánh yêu cầu bổ sung. Vì vậy, dùng hồ sơ này làm tử số đã tạo false-positive.

## Dữ liệu và kết quả UI

Hồ sơ fresh `VV-BTP-TW-20260814-002` được thực hiện đủ luồng trên UI. Lịch sử hiển thị `Yêu cầu bổ sung` lúc 17:14 và `Hoàn thành` lúc 17:16 ngày 14/08/2026.

Với cùng bộ lọc `2026 / Cả năm / Toàn quốc / Tất cả`, dashboard hiển thị:

- `Vụ việc hoàn thành = 24`
- `Tỷ lệ hồ sơ bổ sung = 4,2%`
- Phép đối chiếu: `1 / 24 × 100 = 4,166…%`, làm tròn thành `4,2%`

Click thẻ `Vụ việc hoàn thành` cho danh sách 24 kết quả, trong đó có `VV-BTP-TW-20260814-002`.

## Bằng chứng

- `image/05-dashboard-after-apply-pass.png`: bộ lọc và hai giá trị dashboard
- `image/02-fresh-case-completed.png`: hồ sơ fresh ở trạng thái Hoàn thành
- `image/04-fresh-case-full-history.png`: lịch sử Yêu cầu bổ sung → Hoàn thành
- `image/07-completed-list-fresh-row.png`: dòng hồ sơ fresh trong danh sách hoàn thành
- `image/08-completed-list-total-24.png`: tổng số 24 kết quả

