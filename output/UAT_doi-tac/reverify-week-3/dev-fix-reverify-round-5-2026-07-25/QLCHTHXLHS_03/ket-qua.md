# Row 153 — QLCHTHXLHS_03 — re-verify 2026-07-25 R5

Kết quả: **PASS** (đủ 5 điều kiện a–e). Tài khoản `admin` (QTHT), `/quan-tri/cau-hinh` → thẻ "Thời hạn xử lý (SLA)".

## Đối chiếu từng điều kiện

| | Điều kiện | Kết quả | Bằng chứng |
|---|---|---|---|
| (a) | "Số ngày bổ sung tối đa" có ở cả bảng và cửa sổ Sửa; dòng VU_VIEC hiện 5 | ✅ | Cột bảng: `Loại yêu cầu · Tên loại · Thời hạn (ngày LV) · **Số ngày BS tối đa** · Vùng cảnh báo · Email · Thông báo app · Hành động`. Dòng VU_VIEC = 5. Cửa sổ Sửa VU_VIEC có trường "Số ngày bổ sung tối đa" = 5. Ảnh 05 |
| (b) | Không còn "Hệ số quá hạn" ở bảng lẫn cửa sổ Sửa | ✅ | Không có trong danh sách cột; không có trong cửa sổ Sửa của cả VU_VIEC lẫn HOI_DAP |
| (c) | Xóa trắng rồi lưu bị từ chối + thông báo yêu cầu số nguyên dương + giá trị cũ giữ nguyên | ✅ | Thông báo "Số ngày bổ sung tối đa phải là số nguyên dương"; cửa sổ Sửa không đóng; dòng VU_VIEC trên bảng vẫn là 5. Ảnh 06 |
| (d) | Dòng HOI_DAP để trống hoặc không cho nhập ô này | ✅ | Bảng hiện "—"; cửa sổ Sửa HOI_DAP chỉ có 5 trường (Thời hạn / Ngưỡng 1 / Ngưỡng 2 / Email / In-app), **không có** ô Số ngày bổ sung tối đa. Ảnh 07 |
| (e) | Có khung giải thích 4 mức cảnh báo và cảnh báo ảnh hưởng khi lưu | ✅ | Đầu thẻ có "Giải thích các mức cảnh báo SLA (BR-SLA-02)" đủ 4 mức (Bình thường / Sắp hết hạn / Quá hạn / Quá hạn nghiêm trọng) **và** "Ảnh hưởng khi thay đổi cấu hình SLA". Ảnh 05 |

## So với lượt kiểm trước (sáng 25/07)

Hai điểm trước đó còn thiếu nay đã có: cột "Số ngày BS tối đa" đã được đưa ra bảng, và khối "Ảnh hưởng khi thay đổi cấu hình SLA" đã hiển thị ngay trên thẻ (trước chỉ nằm trong cửa sổ Sửa).

## Ghi nhận thêm (không ảnh hưởng kết luận)

- Nhãn cột trên bảng viết tắt là "Số ngày BS tối đa"; trong cửa sổ Sửa ghi đầy đủ "Số ngày bổ sung tối đa". Tiêu chí yêu cầu đưa thông tin ra bảng để xem nhanh — đã đạt; khác biệt chỉ là cách viết tắt.
- Bảng ở chế độ chỉ đọc + sửa qua cửa sổ, và 6 dòng loại yêu cầu — đúng đặc tả mới, không tính lỗi.

## Ảnh hưởng dữ liệu

Không đổi cấu hình nào. Bước xóa trắng bị hệ thống từ chối nên không ghi được; cửa sổ Sửa của cả VU_VIEC và HOI_DAP đều đóng bằng [Hủy]. Dòng VU_VIEC sau khi test vẫn `15 / 5`.
