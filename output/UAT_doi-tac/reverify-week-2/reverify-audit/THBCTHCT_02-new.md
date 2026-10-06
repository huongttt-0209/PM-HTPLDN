# Audit verify THBCTHCT_02-new

## Cổng 1 — Bằng chứng đối tác

- Đã xem full-res: `partner-evidence/THBCTHCT_02.jpg`.
- Khoảnh khắc lỗi: ảnh tĩnh sau khi bấm `Tổng hợp`.
- Mô tả thấy trực tiếp: hộp thoại chỉ hỏi `Tổng hợp báo cáo?` và báo `Đợt sẽ chuyển sang Đã tổng hợp.`, không có form chỉnh sửa/bổ sung.
- Neo URL/ID: `/ct-htpldn/dot-bao-cao/5adb3002-9de8-4188-bef8-d769d7cee6b7`.
- Neo trạng thái: đang ở chi tiết đợt, sau thao tác bấm `Tổng hợp`, chưa xác nhận `Đồng ý`.
- Neo dữ liệu tiền đề: vai trò CBNV TW, biểu 21a có số liệu và có chương trình liên quan.

## Cổng 2 — Hiểu bug

- Đối tác phản ánh cụ thể: bấm `Tổng hợp` chỉ hiện popup xác nhận, không cho CBNV TW chỉnh sửa/bổ sung số liệu tổng hợp.
- Dữ liệu/bước tái hiện: CBNV TW mở chi tiết đợt có báo cáo đã gửi, bấm `Tổng hợp`.
- Claim cần kiểm: thao tác phải mở form tổng hợp editable trước khi lưu/xác nhận trạng thái.

## Cổng 3 — Đối chiếu SRS với web

| SRS yêu cầu | Thực tế web | Đủ/thiếu |
|---|---|---|
| FR-XI-09 (UC170), dòng 984-1008: sau khi chọn báo cáo, hệ thống gợi ý số liệu và CBNV TW chỉnh sửa/bổ sung trên form tổng hợp. | Bấm `Tổng hợp` trên `DOT-THBC01-UAT` chỉ mở modal xác nhận chuyển sang `Đã tổng hợp`; không có control editable. | Thiếu |
| Acceptance Criteria dòng 1042-1043: nhấn `Tổng hợp` → gợi ý số liệu + form TT17; CBNV chỉnh sửa/bổ sung rồi mới lưu. | Form không xuất hiện; UI chỉ có `Hủy`/`Đồng ý`. Kiểm DOM lần hai: `visibleEditableControls=[]`. | Thiếu |

## Bảng đối chiếu điều kiện

| Điều kiện có thể đổi kết quả | Đối tác | Mình test | GAP? |
|---|---|---|---|
| Vai trò / tài khoản | Cán bộ Nghiệp vụ Trung ương | `cbnv_tw_01` — Cán bộ Nghiệp vụ Trung ương | Không |
| Entity + trạng thái | Chi tiết đợt có dữ liệu tổng hợp, vừa bấm `Tổng hợp`, chưa xác nhận | `DOT-THBC01-UAT`, 2/2 đơn vị `Đã nộp`, vừa bấm `Tổng hợp`, chưa xác nhận | Không |
| Dữ liệu tiền đề | Biểu 21a có số liệu từ báo cáo đơn vị | Biểu 21a có đủ 13 dòng số liệu đã gợi ý từ hai đơn vị | Không |

## Gate real-data

- Artifact quan sát: `../bug-reports/image/BUG-THBCTHCT_02.png`.
- Phương pháp 1: ảnh modal đã mở đọc, chỉ có xác nhận chuyển trạng thái.
- Phương pháp 2: snapshot a11y + DOM cho `visibleEditableControls=[]`, nút chỉ gồm `Tổng hợp/Hủy/Đồng ý`.
- Đã bấm `Hủy` để giữ nguyên seed; ảnh sau hủy: `THBCTHCT_02-after-cancel.png`.
- Bất thường ngoài tiêu chí BA: không phát hiện thêm trên các ảnh đã đọc.

## Verdict

- `Bug` (tương đương Open): app sai flow rõ tại FR-XI-09 (UC170), dòng 984-1008 và AC 1042-1043.

