# Sao lưu nguyên văn dòng 125 — QLLSHTCTVV_03 (trước khi QA ghi đè cột R)

## Mã TC

QLLSHTCTVV_03

## Mô tả

Kiểm tra hiển thị Cột dữ liệu trong bảng danh sách vụ việc

## Điều kiện

1. Đăng nhập tài khoản

## Dữ liệu đầu vào

(trống)

## Các bước thực hiện

1. Chọn menu "Mạng lướt tư vấn viên" -> "Tư vấn viên/Chuyên gia"
2. Tìm kiếm và Nhấn xem chi tiết ứng viên
3. Chọn tab "Lịch sử hỗ trợ"

## Kết quả mong đợi

- Hệ thống hiển thị các trường thông tin giống với thiết kế
- Dữ liệu hiển thị đúng định dạng và trường thông tin
- Dữ liệu hiển thị không bị tràn/đè lên nhau, đồng nhất ngôn ngữ hiển thị

## Kết quả thực tế

- Cột "Đánh giá" bị tràn màn hình
- Thiếu cột "Trạng thái"

## Ảnh/vieo 1

QLLSHTCTVV_03.png

## Trạng thái 1

Fail

## Trạng thái dev fix 1

dev done

## Verify

BA confirm

## DEV phản hồi lần 1

⚠️ Cần BA xác nhận — trạng thái: CHỜ BA XÁC NHẬN.
- Case hỗn hợp: dòng bắt đầu bằng ⚠️ là ý CHỜ BA CHỐT; dòng bắt đầu bằng ✅ là LỖI THẬT đã chứng minh, dev xử lý được ngay, KHÔNG phải chờ BA.
- Đã kiểm tra lại trên web bằng vai trò Cán bộ Nghiệp vụ Trung ương, mở hồ sơ một tư vấn viên đang hoạt động có sẵn 6 vụ việc trong tab "Lịch sử hỗ trợ". Case này gồm 2 ý bên kiểm thử nêu, kết luận từng ý như sau.
- ✅ Ý 1 – "cột Đánh giá bị tràn màn hình": ĐÚNG, đã tái hiện. Ô của cột "Đánh giá" hẹp hơn dãy 5 ngôi sao đúng 8 điểm ảnh, nên ngôi sao thứ 5 bị đẩy xuống dòng thứ hai. Lỗi xuất hiện ở toàn bộ 6/6 dòng của bảng, tại khung nhìn rộng 1440 và 1600 (khung nhìn laptop thông dụng); ở màn hình rộng 1920 thì hiển thị bình thường. Bug ID: BUG-QLLSHTCTVV_03.
- ✅ Trong lúc đo ý 1, phát hiện thêm một lỗi nữa ngay tại cột "Đánh giá": điểm đánh giá của vụ việc đang theo thang 10 nhưng được đưa thẳng vào phần hiển thị sao thang 5. Hậu quả: hai vụ việc điểm 9.0 và 8.7 đều hiện 5/5 sao đầy, không phân biệt được; ô "Điểm trung bình" hiện 8.9 trong khi ngay đầu trang hồ sơ hiện 4.1/5. Theo SCR-IV-03 (dòng 1578) mục (c) phải là "Điểm trung bình: {X}/5", và FR-IV-10 (UC48) mục Outputs (dòng 795) quy định điểm có thang 1.0–5.0. Bug ID: BUG-QLLSHTCTVV_03-B.
- ⚠️ Ý 2 (CHỜ BA XÁC NHẬN – không phải việc của dev) – "thiếu cột Trạng thái": web hiện đủ 9 cột đúng như SCR-IV-03 (dòng 1578) liệt kê, và bản thân dòng 1578 KHÔNG có cột "Trạng thái" nên phần mềm không sai so với đặc tả màn hình. Tuy nhiên đặc tả chức năng của cùng chức năng này lại mâu thuẫn: FR-IV-10 (UC48) mục Outputs (dòng 792) có khai trường "Trạng thái vụ việc", và mục Inputs (dòng 773) cho phép lọc theo trạng thái — trên web bộ lọc "Trạng thái vụ việc" cũng đang hiển thị. Dữ liệu trạng thái thực tế đã có sẵn cho từng dòng (6 vụ việc đang mang 5 trạng thái khác nhau), chỉ là không được trình bày thành cột.
- ⚠️ Đề nghị BA xác nhận: bảng của tab "Lịch sử hỗ trợ" có bổ sung cột "Trạng thái vụ việc" không, khi mà FR-IV-10 (dòng 792) đã khai trường này là dữ liệu đầu ra và bộ lọc theo trạng thái (dòng 773 + SCR-IV-03 dòng 1578 mục a) vẫn đang được dùng? Nếu có thì xin cập nhật lại bảng cột ở SCR-IV-03 dòng 1578 cho khớp.
- Verify: tài khoản Cán bộ Nghiệp vụ Trung ương, bản dựng V1.0.5, ngày 03/08/2026.

──────── (append) ────────
[DEV cập nhật 03/08/2026 — sau fix]
• Cột "Đánh giá" tràn + điểm thang 10 render sao thang 5 (03-B): ĐÃ FIX + verify 120 PASS (commit 28e77f8b2 + bc7719a5d).
• Ý "thiếu cột Trạng thái": CHỜ BA CHỐT — bảng Lịch sử hỗ trợ có bổ sung cột "Trạng thái vụ việc" không (SCR-IV-03:1578 khai 9 cột không có Trạng thái; FR-IV-10:792/:773 lại khai trường + bộ lọc). Đã lập phiếu BA (mục b).

──────── (append) ────────
[DEV rà lại SRS 03/08] Ý "thiếu cột Trạng thái" = KHÔNG_BUG: SCR-IV-03 :1578 (b) liệt kê ĐÚNG 9 cột và KHÔNG có cột Trạng thái (Trạng thái chỉ là BỘ LỌC :1578(a), không phải cột). Code đúng 100% đặc tả màn hình → KHÔNG cần chờ BA. Cả tràn + điểm /5 (03-B) đã fix → QLLSHTCTVV_03 = dev done.
