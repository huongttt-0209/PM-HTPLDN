# Sao lưu nguyên văn dòng 123 — DKTGMLTVV_05 (trước khi QA ghi đè cột R)

## Mã TC

DKTGMLTVV_05

## Mô tả

Kiểm tra hiển thị Nhóm 4  Tệp đính kèm

## Điều kiện

1. Đăng nhập tài khoản

## Dữ liệu đầu vào

(trống)

## Các bước thực hiện

1. Chọn menu "Mạng lướt tư vấn viên" -> "Tư vấn viên/Chuyên gia"
2. Chọn tab "Mới đăng ký"
3. Nhấn Thêm mới

## Kết quả mong đợi

- Hệ thống hiển thị các trường thông tin giống với thiết kế
- Dữ liệu hiển thị đúng định dạng và trường thông tin
- Dữ liệu hiển thị không bị tràn/đè lên nhau, đồng nhất ngôn ngữ hiển thị

## Kết quả thực tế

- Nhóm 4 — Hồ sơ đính kèm: Tệp bằng cấp / chứng chỉ, Tệp thẻ hành nghề

## Ảnh/vieo 1

DKTGMLTVV_05_v2.jpg

## Trạng thái 1

Fail

## Trạng thái dev fix 1

BA confirm

## Verify

BA confirm

## DEV phản hồi lần 1

⚠️ Cần BA xác nhận — trạng thái: CHỜ BA XÁC NHẬN.
- Case hỗn hợp: dòng bắt đầu bằng ⚠️ là ý CHỜ BA CHỐT; dòng bắt đầu bằng ✅ là LỖI THẬT đã chứng minh, dev xử lý được ngay, KHÔNG phải chờ BA.
- Đã kiểm tra lại trên web (vai trò Người hỗ trợ pháp lý, màn Thêm mới Tư vấn viên). Case này gồm 3 ý, kết luận từng ý như sau.
- ⚠️ Ý 1 (CHỜ BA XÁC NHẬN – không phải việc của dev) – phản ánh "Nhóm 4 thiếu Tệp thẻ hành nghề": quan sát của bên kiểm thử là ĐÚNG, nhóm "File đính kèm" trên web chỉ có duy nhất mục "File đính kèm (Bằng cấp / Chứng chỉ)". Tuy nhiên chức năng tải tệp thẻ hành nghề vẫn có, nằm ở nhóm "Nghề nghiệp". Vướng ở chỗ SRS v3.5 liệt kê CÙNG một trường này ở CẢ HAI nơi: SCR-IV-02 dòng 1508 (nhóm 2, mục 3.6) và dòng 1520 (nhóm 4, mục 5.2), không có câu nào nói nó xuất hiện ở cả hai. Đây là mâu thuẫn của đặc tả, không phải lỗi phần mềm ⇒ đề nghị BA chốt: trường "File thẻ hành nghề" thuộc nhóm 2 hay nhóm 4, hay giữ ở cả hai? Chốt xong xin sửa lại SRS cho khớp để không lệch tiếp.
- ✅ Ý 2 – LỖI THẬT, chuyển dev (BUG-DKTGMLTVV_05): mục "File đính kèm (Bằng cấp / Chứng chỉ)" không được đánh dấu bắt buộc và hệ thống KHÔNG chặn khi bỏ trống. Đã đăng ký ứng viên mới bằng vai trò Người hỗ trợ, cố ý không đính kèm bằng cấp / chứng chỉ nào, hệ thống vẫn báo "Tạo hồ sơ TVV thành công" và tạo ra hồ sơ TVV-BTP-TW-0030. Theo FR-IV-03 (UC41), màn SCR-IV-02 dòng 1519, trường này bắt buộc khi Người hỗ trợ đăng ký ứng viên mới ⇒ hệ thống phải từ chối lưu và báo rõ còn thiếu gì. Đối chiếu: cùng biểu mẫu đó, khi thiếu File thẻ hành nghề thì hệ thống CÓ chặn ("File thẻ hành nghề là bắt buộc đối với Tư vấn viên"), tức cơ chế chặn đã có sẵn, chỉ chưa áp cho mục này.
- ✅ Ý 3 – LỖI THẬT, chuyển dev (BUG-DKTGMLTVV_05-B): trong danh sách file đã tải của nhóm 4, bấm nút "Xóa" thì tệp bị gỡ ngay, không có bước xác nhận nào. Theo SCR-IV-02 dòng 1521, hành vi quy định là "Xóa: xác nhận trước khi xóa". Mới đo ở chế độ Thêm mới; đề nghị dev rà cả chế độ Chỉnh sửa vì ở đó tệp đã lưu, xóa nhầm là mất dữ liệu thật.
- Ghi nhận thêm cho dev: mục "Danh sách file đã tải" (SCR-IV-02 dòng 1521) đã hiển thị đủ tên tệp, dung lượng, nút Xem và nút Xóa; nút Xem mở được tệp PDF. Phần này đạt.
- Verify: tài khoản Người hỗ trợ pháp lý cấp Trung ương, bản dựng V1.0.5, ngày 03/08/2026.

──────── (append) ────────
[DEV cập nhật 03/08/2026 — sau fix]
• ý2 (File Bằng cấp/Chứng chỉ bắt buộc khi Người hỗ trợ đăng ký mới) + ý3 (xác nhận trước khi xóa tệp): ĐÃ FIX + verify staging 120 PASS (commit 3299dbf78).
• ý1: CHỜ BA CHỐT — File "Thẻ hành nghề" thuộc Nhóm 2 hay Nhóm 4 (SRS mâu thuẫn: srs-fr-04:1508 Nhóm 2 vs :1520 Nhóm 4). Đã lập phiếu BA (mục a). Chưa code phần này cho tới khi BA chốt.
