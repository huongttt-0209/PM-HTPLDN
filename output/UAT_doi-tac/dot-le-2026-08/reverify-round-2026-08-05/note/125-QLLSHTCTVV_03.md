## [UAT_TGPL Doanh Nghiệp-tuần 2] row 125 — QLLSHTCTVV_03 — S1
Tên chức năng: 
Tác nhân: 
Mô tả: Kiểm tra hiển thị Cột dữ liệu trong bảng danh sách vụ việc
Điều kiện: 1. Đăng nhập tài khoản
Dữ liệu đầu vào: 
Các bước: 1. Chọn menu "Mạng lướt tư vấn viên" -> "Tư vấn viên/Chuyên gia"
2. Tìm kiếm và Nhấn xem chi tiết ứng viên
3. Chọn tab "Lịch sử hỗ trợ"
KQ mong đợi: - Hệ thống hiển thị các trường thông tin giống với thiết kế
- Dữ liệu hiển thị đúng định dạng và trường thông tin
- Dữ liệu hiển thị không bị tràn/đè lên nhau, đồng nhất ngôn ngữ hiển thị
KQ thực tế (l1): - Cột "Đánh giá" bị tràn màn hình
- Thiếu cột "Trạng thái"
Trạng thái 1: Fail | P dev fix1: dev done | Q Verify: Open
KQ thực tế lần 2: 
Trạng thái 2:  | W dev fix2:  | X Verify2: 
--- NOTE (R: DEV phản hồi lần 1) ---
✅ Bug đúng (BA 04/08/2026) — nhưng KHÔNG phải ở điểm đối tác nêu. Về ý "thiếu cột Trạng thái": BA chốt bảng "Lịch sử hỗ trợ" giữ đúng chín cột như thiết kế, cột trạng thái vụ việc không nằm trong thiết kế của bảng này ở cả bản gốc lẫn bản bàn giao; ô lọc theo trạng thái vẫn giữ. Ý này Dev KHÔNG phải sửa, BA ghi nhận thành yêu cầu cải tiến. Phiếu vẫn giữ xử lý vì hai lỗi hiển thị khác trong cùng bảng đã chứng minh tái hiện:
(1) Cột "Đánh giá" vỡ hai hàng (4 sao trên, 1 sao dưới) ở 6/6 dòng, tại khung nhìn 1440x900 và 1600x900; ở 1920 thì bình thường. Đo được: dãy 5 sao cần 132px, ô rộng 140px trừ đệm còn 124px — thiếu 8px. Đây đúng chỗ đối tác khoanh đỏ, và vi phạm tiêu chí ghi ngay trong phiếu "dữ liệu hiển thị không bị tràn/đè lên nhau". Minor.
(2) Ô "Điểm trung bình" hiện 8.9 trong khi cùng trang, đầu hồ sơ hiện 4.1/5 — dữ liệu đang là thang 10 trong khi FR-IV-10 (dòng 795) quy định thang 1.0-5.0 và SCR-IV-03 (dòng 1578) quy định trình bày {X}/5. Hệ quả: hai vụ việc điểm khác nhau đều hiện 5/5 sao đầy, mất khả năng phân biệt. Major.

Ghi nhận: Dev báo đã sửa cả hai điểm này ngày 03/08/2026 (commit 28e77f8b2 + bc7719a5d). QA CHƯA đo lại trên môi trường bàn giao nên phiếu giữ Open — bản fix sẽ được chấm ở vòng sau theo đúng khối dưới đây.
── CÁCH VERIFY sau Dev fix ──
Precondition: cbnv_tw + hồ sơ TVV-BTP-TW-0002 (có 6 vụ việc, điểm đánh giá khác nhau) → tab "Lịch sử hỗ trợ" + đặt cửa sổ trình duyệt ở bề ngang 1440px.
1) Ở bề ngang 1440px, đọc cột "Đánh giá" của cả 6 dòng.
2) Lặp lại ở bề ngang 1600px.
3) Đọc ô "Điểm trung bình" của tab và đối chiếu với điểm đánh giá hiển thị ở đầu hồ sơ cùng trang.
4) So hai vụ việc có điểm đánh giá khác nhau.
✅ PASS khi: ở cả 1440px và 1600px, dãy sao của mọi dòng nằm trọn trên một hàng, không xuống dòng, không bị cắt; ô "Điểm trung bình" và điểm ở đầu hồ sơ cùng một thang đo và khớp nhau; hai vụ việc điểm khác nhau hiện số sao khác nhau.
❌ FAIL nếu: còn dòng nào vỡ hai hàng ở 1440px hoặc 1600px; hoặc hai chỗ hiển thị điểm vẫn lệch thang; hoặc mọi vụ việc vẫn hiện 5/5 sao đầy.
⚠️ Bảng KHÔNG cần thêm cột "Trạng thái" — BA đã chốt giữ chín cột. Đừng chấm FAIL vì thiếu cột đó.