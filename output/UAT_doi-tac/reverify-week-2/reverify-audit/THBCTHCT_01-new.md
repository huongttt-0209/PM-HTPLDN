# Audit verify THBCTHCT_01-new

## Cổng 1 — Bằng chứng đối tác

- Đã xem full-res: `partner-evidence/THBCTHCT_01.jpg`.
- Khoảnh khắc lỗi: ảnh tĩnh toàn màn hình, không có timestamp video.
- Mô tả thấy trực tiếp: trang chi tiết đợt báo cáo không có ô tích chọn trong bảng tiến độ theo đơn vị.
- Neo URL/ID: `/ct-htpldn/dot-bao-cao/5adb3002-9de8-4188-bef8-d769d7cee6b7`.
- Neo trạng thái: Sở Tư pháp Hà Nội hiển thị `Đã tổng hợp`; nhiều đơn vị đang `Chưa nộp`.
- Neo dữ liệu tiền đề: vai trò Cán bộ Nghiệp vụ Trung ương, trang chi tiết một đợt báo cáo.

## Cổng 2 — Hiểu bug

- Đối tác phản ánh cụ thể: không có ô tích chọn để chọn các báo cáo cần tổng hợp.
- Dữ liệu/bước tái hiện: đăng nhập CBNV TW, mở Đợt báo cáo có báo cáo đơn vị đã gửi, vào chi tiết đợt và quan sát bảng báo cáo/tiến độ.
- Claim cần kiểm: trong điều kiện có báo cáo BN/ĐP đã gửi, hệ thống phải cho CBNV TW chọn các báo cáo trước khi tổng hợp.

## Cổng 3 — Đối chiếu SRS với web

| SRS yêu cầu | Thực tế web | Đủ/thiếu |
|---|---|---|
| FR-XI-09 (UC170), dòng 984-998: CBNV TW xem danh sách báo cáo BN/ĐP đã gửi, chọn các báo cáo cần tổng hợp; input `bao_cao_ids` lấy từ checkbox. | Record live `DOT-THBC01-UAT` có 2/2 đơn vị ở `Đã nộp`, nhưng bảng chỉ có `Đơn vị / Cấp / Trạng thái nộp / Ngày nộp`, không có cột hoặc control checkbox. Kiểm DOM lần hai: `allCheckboxes=0`, `visibleCheckboxes=0`. | Thiếu |
| FR-XI-09 Processing dòng 1005-1008: hiển thị danh sách BC đã gửi, CBNV TW chọn các BC, sau đó hệ thống mới gợi ý số liệu. | Trang hiển thị ngay số liệu Biểu 21a đã gộp và nút `Tổng hợp`, không có bước chọn báo cáo. | Thiếu |

## Bảng đối chiếu điều kiện

| Điều kiện có thể đổi kết quả | Đối tác | Mình test | GAP? |
|---|---|---|---|
| Vai trò / tài khoản | Cán bộ Nghiệp vụ Trung ương | `cbnv_tw_01` — Cán bộ Nghiệp vụ Trung ương | Không |
| Entity + trạng thái | Chi tiết đợt báo cáo; case yêu cầu có ít nhất một báo cáo BN/ĐP đã gửi lên | `DOT-THBC01-UAT` (`d7a62f6e-a119-4582-8b08-f935d25c534b`), 2/2 đơn vị ở `Đã nộp` | Không |
| Dữ liệu tiền đề | Báo cáo từ nhiều đơn vị trong một đợt | Bộ KH&ĐT và Sở Tư pháp An Giang đều `Đã nộp` | Không |

## Gate real-data

- Artifact quan sát: `../bug-reports/image/BUG-THBCTHCT_01.png`.
- Phương pháp 1: ảnh full-page đã mở đọc, bảng không có ô chọn.
- Phương pháp 2: kiểm DOM/a11y, không có control checkbox (`0` toàn bộ, `0` hiển thị).
- Bất thường ngoài tiêu chí BA: không phát hiện thêm trên ảnh đã đọc.

## Verdict

- `Bug` (tương đương Open): app sai yêu cầu rõ tại FR-XI-09 (UC170), dòng 984-1008.

