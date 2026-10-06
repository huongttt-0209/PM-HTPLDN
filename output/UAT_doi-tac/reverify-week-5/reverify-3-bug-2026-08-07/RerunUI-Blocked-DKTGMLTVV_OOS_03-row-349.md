# Rerun UI-only bug DKTGMLTVV_OOS_03 — dòng 349

- Môi trường: `https://18.143.165.120.nip.io` — HTPLDN v1.0.10
- Ngày chạy: 07/08/2026 (Asia/Ho_Chi_Minh)
- Tài khoản: `nht_qa_tw` — Người hỗ trợ pháp lý, cấp TW
- Công cụ: Chrome DevTools kết nối cửa sổ Chrome hiển thị
- Verdict lượt chạy UI-only: **BLOCKED / INCONCLUSIVE đối với bug gốc phía máy chủ**
- Ghi Sheet: **không thực hiện** theo phạm vi được giao cho lượt chạy này

## Phạm vi bug gốc

Bug `DKTGMLTVV_OOS_03` kiểm ràng buộc phía máy chủ khi tạo hồ sơ `Loại = Tư vấn viên (TVV)` nhưng request cố ý thiếu `soTheHanhNghe`. Điều kiện quyết định là máy chủ phải từ chối request đã vượt qua hoặc bỏ qua validation giao diện.

## Luồng UI đã chạy

1. Mở trang đăng nhập bằng Chrome hiển thị, đăng nhập `nht_qa_tw` và lấy OTP qua giao diện MailHog hiển thị.
2. Đi theo sidebar: **Mạng lưới Tư vấn viên → Tư vấn viên / Chuyên gia → Thêm mới**.
3. Giữ `Loại = Tư vấn viên (TVV)`.
4. Nhập hợp lệ toàn bộ trường bắt buộc khác: họ tên, ngày sinh, giới tính, CCCD, email, số điện thoại, địa chỉ, trình độ, chuyên ngành, số năm kinh nghiệm và lĩnh vực pháp luật. Trường **Số thẻ hành nghề** được cố ý để trống.
5. Nhấn **Lưu** hai lần để kiểm tra tính lặp lại.
6. Sau mỗi lần bấm, đọc UI và danh sách Network trong Chrome DevTools, không replay/edit request, không phát request API trực tiếp.

## Kết quả quan sát

- Giao diện chặn tại đúng trường và hiển thị: **“Số thẻ hành nghề là bắt buộc đối với Tư vấn viên”**.
- Trang vẫn ở `/chuyen-gia-tvv/tao-moi`, không chuyển sang danh sách và không báo tạo thành công.
- Network trước lần bấm đầu có 25 request XHR/fetch. Sau hai lần bấm chỉ tăng các request định kỳ `GET /api/v1/thong-baos/unread-count`; **không có `POST /api/v1/tu-van-viens`**.
- Hai lần bấm cho cùng kết quả, chứng minh validation phía giao diện hoạt động ổn định.

## Kết luận

Không thể chấm **Pass** hay **Reopen** cho bug gốc bằng UI-only. Form đã chặn trước khi phát request nên lượt chạy này không đi tới lớp máy chủ, trong khi bug gốc yêu cầu kiểm chính tình huống bypass giao diện. Đây là giới hạn đo, không phải lỗi mới.

- Kết luận được phép từ bằng chứng UI: **frontend đã chặn đúng và không tạo request**.
- Kết luận chưa thể đưa ra dưới giới hạn UI-only: backend có còn chấp nhận request TVV thiếu `soTheHanhNghe` hay không.
- Để xác nhận backend phải có một phép đo có chủ đích ở lớp request, ví dụ kiểm thử tích hợp/negative API; cách đó bị loại trừ trong lượt rerun này.

## Bằng chứng

- Ảnh Chrome hiển thị trước thao tác: form **Thêm mới Tư vấn viên**, Loại = TVV, dữ liệu thử nghiệm đã nhập.
- Ảnh Chrome hiển thị sau thao tác: trường **Số thẻ hành nghề** viền đỏ và thông báo bắt buộc nêu trên.
- Chrome DevTools Network: không phát sinh `POST /api/v1/tu-van-viens` sau cả hai lần nhấn **Lưu**.
- Không lưu ảnh ra tệp cục bộ vì Chrome DevTools MCP không được cấp quyền ghi vào workspace; ảnh đã được hiển thị trực tiếp trong phiên kiểm thử.

## Lưu ý về tệp PDF

Các vùng upload PDF trên form không có dấu bắt buộc. Đã thử dùng tệp PDF hợp lệ trong workspace, nhưng Chrome DevTools MCP từ chối đọc đường dẫn do giới hạn workspace root của công cụ. Không dùng cách lách hay API; việc này không làm thay đổi kết luận vì validation quyết định xảy ra tại trường bắt buộc `Số thẻ hành nghề` trước khi có request tạo mới.
