## [UAT_TGPL Doanh Nghiệp-tuần 2] row 123 — DKTGMLTVV_05 — S1
Tên chức năng: 
Tác nhân: 
Mô tả: Kiểm tra hiển thị Nhóm 4  Tệp đính kèm
Điều kiện: 1. Đăng nhập tài khoản
Dữ liệu đầu vào: 
Các bước: 1. Chọn menu "Mạng lướt tư vấn viên" -> "Tư vấn viên/Chuyên gia"
2. Chọn tab "Mới đăng ký"
3. Nhấn Thêm mới
KQ mong đợi: - Hệ thống hiển thị các trường thông tin giống với thiết kế
- Dữ liệu hiển thị đúng định dạng và trường thông tin
- Dữ liệu hiển thị không bị tràn/đè lên nhau, đồng nhất ngôn ngữ hiển thị
KQ thực tế (l1): - Nhóm 4 — Hồ sơ đính kèm: Tệp bằng cấp / chứng chỉ, Tệp thẻ hành nghề
Trạng thái 1: Fail | P dev fix1: dev done | Q Verify: Open
KQ thực tế lần 2: 
Trạng thái 2:  | W dev fix2:  | X Verify2: 
--- NOTE (R: DEV phản hồi lần 1) ---
✅ Bug đúng (BA 04/08/2026) — nhưng KHÔNG phải ở điểm đối tác nêu. Về ý đối tác phản ánh (nhóm 4 thiếu ô "Tệp thẻ hành nghề"): BA chốt giữ nguyên như phần mềm đang làm — ô này thuộc nhóm 2 "Thông tin nghề nghiệp", phần đặc tả liệt kê trùng ở nhóm 4 là lỗi tài liệu, BA gỡ. Ý này Dev KHÔNG phải sửa. Phiếu vẫn giữ xử lý vì QA đo thấy 2 lỗi khác nằm trong chính nhóm 4:
(1) Ô "Bằng cấp / Chứng chỉ" không được đánh dấu bắt buộc và hệ thống KHÔNG chặn khi để trống — đã đo bằng vai trò NHT đúng luồng đăng ký ứng viên mới, hồ sơ TVV-BTP-TW-0030 vẫn lưu thành công dù không đính kèm bằng cấp nào. Trái FR-IV-02 §5.1 (dòng 1519) "Bắt buộc khi Người hỗ trợ đăng ký ứng viên mới". Major.
(2) Nút "Xóa" trong danh sách file đã tải gỡ file ngay, không hỏi lại. Trái FR-IV-02 §5.3 (dòng 1521) "Xóa: xác nhận trước khi xóa". Ở chế độ Chỉnh sửa hồ sơ đã lưu thì đây là mất dữ liệu thật. Minor ở màn tạo mới, Major ở màn chỉnh sửa.

Ghi nhận: Dev báo đã sửa cả hai điểm này ngày 03/08/2026 (commit 3299dbf78), verify trên staging. QA CHƯA đo lại trên môi trường bàn giao nên phiếu giữ Open — bản fix sẽ được chấm ở vòng sau theo đúng khối dưới đây.
── CÁCH VERIFY sau Dev fix ──
Precondition: nht_qa_tw (vai trò NHT) + màn Mạng lưới Tư vấn viên → Tư vấn viên / Chuyên gia → tab "Mới đăng ký" → Thêm mới.
1) Điền đủ mọi trường bắt buộc khác, nạp File thẻ hành nghề ở nhóm 2, CỐ Ý để trống ô "Bằng cấp / Chứng chỉ" ở nhóm "File đính kèm" → bấm Lưu.
2) Nạp một tệp PDF vào ô "Bằng cấp / Chứng chỉ" → bấm Xóa ở dòng tệp vừa nạp.
3) Lặp bước 2 ở chế độ Chỉnh sửa một hồ sơ tư vấn viên đã lưu có sẵn tệp đính kèm.
✅ PASS khi: bước 1 bị chặn, hồ sơ KHÔNG được tạo và người dùng đọc được lý do là thiếu bằng cấp/chứng chỉ; bước 2 và 3 đều phải qua một bước xác nhận trước khi tệp bị gỡ, hủy xác nhận thì tệp còn nguyên.
❌ FAIL nếu: bước 1 vẫn tạo được hồ sơ; hoặc thông báo chặn chỉ nhắc thẻ hành nghề mà không nhắc bằng cấp/chứng chỉ; hoặc bước 2 hay bước 3 gỡ tệp ngay không hỏi lại.
⚠️ Nhóm 4 KHÔNG cần có thêm ô "Tệp thẻ hành nghề" — BA đã chốt ô đó ở nhóm 2. Đừng chấm FAIL vì nhóm 4 chỉ có một ô.