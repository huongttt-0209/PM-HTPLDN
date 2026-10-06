# Re-verify bug DKTGMLTVV_OOS_03 — dòng 349

- Môi trường: `https://18.143.165.120.nip.io` — HTPLDN v1.0.10
- Thời điểm: 07/08/2026 22:03–22:05 (Asia/Ho_Chi_Minh)
- Tài khoản: `nht_qa_tw` — NHT Trung ương, Cục Bổ trợ tư pháp
- Verdict: **PASS**

## Phạm vi bug

Kiểm ràng buộc phía máy chủ khi tạo hồ sơ `Loại = TVV` nhưng không gửi `soTheHanhNghe`. Yêu cầu được gửi trực tiếp tới API, không qua validation của biểu mẫu.

## Luồng đã chạy

1. Đăng nhập đúng tài khoản NHT Trung ương có quyền `register_tu_van_vien`.
2. Tại route `/chuyen-gia-tvv/tao-moi`, chuẩn bị bộ dữ liệu hợp lệ theo bug: TVV, ngày sinh, giới tính, CCCD, email, điện thoại, địa chỉ, trình độ, chuyên ngành, 5 năm kinh nghiệm và lĩnh vực Thương mại.
3. Gửi đúng một `POST /api/v1/tu-van-viens` trực tiếp, cố ý không có thuộc tính `soTheHanhNghe`.
4. Đọc phản hồi máy chủ; sau đó đọc toàn bộ 44 hồ sơ hiện có và tìm lại bằng tên/email/điện thoại thử nghiệm.

## Kết quả

- Máy chủ trả **HTTP 422**, không còn chấp nhận/tạo hồ sơ `201` như lỗi cũ.
- Lỗi trả đúng field `soTheHanhNghe`, nội dung: `Số thẻ hành nghề là bắt buộc đối với Tư vấn viên`.
- Đối chiếu kho dữ liệu: `0` bản ghi khớp tên, email hoặc điện thoại thử nghiệm; không sinh hồ sơ mới.
- Kết quả khớp SCR-IV-02 dòng 1507 và nội dung bug/BA đã chốt.

## Bằng chứng

- `349-direct-create-without-so-the.request.json`: payload trực tiếp, không có `soTheHanhNghe`.
- `349-direct-create-without-so-the.response.json`: response `422` và lỗi đúng field/nội dung.
- `349-direct-create-without-so-the.network.txt`: metadata network của request duy nhất.
- `349-storage-readback.json`: đọc lại kho dữ liệu, không có bản ghi thử nghiệm.
- `image/349-direct-api-rejected-422.png`: màn hình form cùng panel bằng chứng QA; file PDF thẻ hợp lệ đã được chọn ở giao diện để đối chứng điều kiện liền kề, nhưng direct API bị chặn ngay vì thiếu số thẻ.

## Cập nhật Sheet

- Dòng: 349
- `Trạng thái dev fix`: `Test done`
- Không ghi `Kết quả verify` vì verdict Pass.
