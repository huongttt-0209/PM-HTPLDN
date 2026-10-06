# TLHSBS_01 — Condition table sau Dev fix

| # | Điều kiện cần đo | Kết quả | Bằng chứng |
|---|---|---|---|
| 1 | Đúng actor `cbnv_tw_02` | PASS | Header hiển thị `CB Nghiệp vụ - Trung ương #02`. |
| 2 | Vụ mẫu thuộc tập hoàn thành trong kỳ | PASS | `VV-BTP-TW-20260712-005` ở trạng thái Hoàn thành; timeline ghi Hoàn thành `25/07/2026 02:23`. |
| 3 | Vụ mẫu từng qua bổ sung | PASS | Timeline ghi `Bổ sung hồ sơ` lúc `15/07/2026 12:15`. |
| 4 | Bộ lọc đúng `2026 / Cả năm / Toàn quốc / Tất cả` | PASS | UI và `appliedFilter` của dashboard khớp; khoảng ngày `01/01/2026–14/08/2026`. |
| 5 | Mẫu số là số vụ hoàn thành trong cùng bộ lọc | PASS | Thẻ và danh sách drill-down cùng ghi `23`; danh sách dùng `dateField=ngay_hoan_thanh`. |
| 6 | Khi tử số ≥ 1 và mẫu số = 23, KPI phải > 0% | FAIL | UI và API dashboard đều trả `0%`; chỉ riêng vụ mẫu đã tạo cận dưới `1/23 ≈ 4,35%`. |
| 7 | Không hiện “Chưa có dữ liệu” khi mẫu số > 0 | PASS | Ở bộ lọc cả năm, thẻ hiện `0%` và dấu `—`, không hiện nhãn “Chưa có dữ liệu”. Giá trị vẫn sai theo điều kiện 6. |
| 8 | Một vụ bổ sung nhiều lần chỉ đếm một lần | N/A | Không thể phân biệt nhánh đếm lặp khi kết quả hiện tại đã làm mất cả vụ bổ sung đã xác nhận và trả tử số 0; phải đo lại sau lần sửa tiếp theo. |
| 9 | Mẫu số = 0 thì hiện `—` và không có xu hướng | PASS | Bộ lọc `Tháng 9/2026`: Vụ việc hoàn thành = 0; thẻ Tỷ lệ hồ sơ bổ sung hiện `—`, “Chưa có dữ liệu”, không có mũi tên/% xu hướng. |
| 10 | Không có lỗi console liên quan trong lượt đo | PASS | Chrome console: không có message mức error. |

Kết luận zero-gap: mọi nhánh trong checklist đã được chấm PASS/FAIL/N/A có lý do. Nhánh chính FAIL nên verdict toàn case là `Reopen`.
