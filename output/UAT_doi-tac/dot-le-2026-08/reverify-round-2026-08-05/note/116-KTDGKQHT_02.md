## [UAT_TGPL Doanh Nghiệp-tuần 2] row 116 — KTDGKQHT_02 — S1
Tên chức năng: 
Tác nhân: 
Mô tả: Kiểm tra dữ liệu hiển thị trong mỗi tab
Điều kiện: 1. Đăng nhập tài khoản
Dữ liệu đầu vào: 
Các bước: 1. Chọn menu "Đào tạo, tập huấn" -> "Khóa học"
2. Nhấn xem chi tiết khóa học
3. Chọn tab "Điểm danh", "Kết quả kiểm tra"
KQ mong đợi: - Dữ liệu hiển thị đúng với trường thông tin và định dạng 
- Dữ liệu không lỗi hiển thị, đồng nhất về mặt ngôn ngữ
- Không bị tràn/đè dữ liệu giữa các cột
- Đồng bộ về căn lề
KQ thực tế (l1): Tab "Kết quả kiểm tra" hiển thị thiếu các trường thông tin: Số buổi có mặt, Số buổi vắng có phép, Số buổi vắng không phép, Tổng số buổi
Trạng thái 1: Fail | P dev fix1: dev done | Q Verify: Open
KQ thực tế lần 2: 
Trạng thái 2:  | W dev fix2:  | X Verify2: 
--- NOTE (R: DEV phản hồi lần 1) ---
✅ Bug đúng (BA 04/08/2026). Dev FE/BE: màn chấm kết quả học tập phải cho người dùng đọc được đủ bốn con số buổi học của mỗi học viên — số buổi có mặt, số buổi vắng có phép, số buổi vắng không phép và tổng số buổi. Hiện chỉ có ô "Chuyên cần" dạng x/y; hai số buổi vắng không hiện ở đâu, nên cán bộ lẫn học viên không kiểm chứng được vì sao ra kết quả Đạt / Không đạt. BA chốt: KHÔNG cần tách thành bốn cột rời — giữ ô gộp nhưng phải đọc được tách bạch ba con số (bản bàn giao mục 4.3.5.2.2 khai đây là thông tin chỉ đọc trên màn hình). Căn cứ: FR-III-05 (UC24) §Outputs (dòng 600-603); công thức chuyên cần (dòng 604) tính cả buổi vắng có phép vào tử số; BR-KQ-02 (dòng 607) dùng tỷ lệ này để xét Đạt/Không đạt. Major.

── CÁCH VERIFY sau Dev fix ──
Precondition: cbnv_tw + một khóa học đã có ≥1 học viên được điểm danh ≥3 buổi, trong đó có ít nhất 1 buổi vắng có phép và 1 buổi vắng không phép + màn Khóa học → tab "Kết quả kiểm tra".
1) Mở tab "Điểm danh" của khóa đó, ghi lại số buổi có mặt / vắng có phép / vắng không phép / tổng buổi thực tế của học viên đó.
2) Sang tab "Kết quả kiểm tra", tìm đúng dòng học viên đó.
3) Đọc phần thông tin chuyên cần của dòng (ô gộp hoặc phần chú giải khi rê chuột — Dev tự chọn cách trình bày).
✅ PASS khi: từ màn hình đọc được đủ CẢ BỐN con số ở bước 1 và cả bốn khớp số liệu điểm danh; tỷ lệ chuyên cần hiển thị đúng bằng (số buổi có mặt + số buổi vắng có phép) chia tổng số buổi.
❌ FAIL nếu: vẫn không đọc được số buổi vắng có phép hoặc số buổi vắng không phép ở bất kỳ đâu trên màn; hoặc con số hiển thị lệch dữ liệu điểm danh; hoặc tỷ lệ chuyên cần bỏ buổi vắng có phép ra khỏi tử số.
⚠️ Không bắt buộc phải là bốn cột rời — gộp trong một ô kèm chú giải vẫn tính PASS, miễn đọc được tách bạch bốn con số.