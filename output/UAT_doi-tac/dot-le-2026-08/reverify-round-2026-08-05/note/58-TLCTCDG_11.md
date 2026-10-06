## [UAT_TGPL Doanh Nghiệp-tuần 3] row 58 — TLCTCDG_11 — S2
Tên chức năng: 
Tác nhân: 
Mô tả: Kiểm tra lưu thành công, tổng trọng số khác 100%
Điều kiện: 1. Đăng nhập tài khoản 
2. Đợt đánh giá đang ở trạng thái "Lập kế hoạch".
Dữ liệu đầu vào: 
Các bước: 1. Chọn menu "Đánh giá hiệu quả"
2. Mở Chi tiết đợt đánh giá (tab Tiêu chí)
3. Nhập thông tin hợp lệ và nhấn "Lưu"
KQ mong đợi: - Hệ thống hiển thị thông điệp "Tổng trọng số hiện tại: {X}%. Cần đảm bảo = 100% trước khi trình phê duyệt".
KQ thực tế (l1): Hệ thống hiển thị thông báo thành công
Trạng thái 1: Fail | P dev fix1: dev done | Q Verify: Pass
KQ thực tế lần 2: 
Trạng thái 2:  | W dev fix2: dev done | X Verify2: 
--- NOTE (Y: DEV phản hồi lần 2) ---
✅ Bug ĐÚNG (BA chốt 31/07/2026) — Loại 1, phần mềm sai đặc tả. Phản hồi lần 1 của dev đúng về quy tắc (cho lưu, chỉ chặn ở bước sau) nhưng lệch trọng tâm: điều đối tác nêu là thông điệp không đúng nội dung quy định, không phải chuyện có chặn lưu hay không.

Đính chính hiện trạng: phần mềm ĐÃ có cảnh báo trọng số — nhãn tổng đỏ kèm chú thích "(Tổng trọng số phải bằng 100%)", thấy rõ trong ảnh TLCTCDG_11.jpg. Cái thiếu là thông điệp nêu rõ tổng hiện tại và mốc phải đạt. Đừng hiểu thành "chưa có gì" rồi dựng lại từ đầu.

Việc Dev (2 phần):
(1) Bổ sung dải cảnh báo trọng số ở Tab Tiêu chí, hiện khi tổng trọng số khác 100%, nội dung nêu tổng trọng số hiện tại và mốc 100% cần đạt trước khi trình phê duyệt. GIỮ NGUYÊN nhãn tổng xanh/đỏ và việc cho phép lưu — không chặn lưu.
(2) Bổ sung dải cảnh báo chuẩn thang điểm, hiện khi tổng của (điểm tối đa × trọng số ÷ 100) khác 100, nội dung nêu tổng hiện tại. Ràng buộc chuẩn thang điểm (BR-CALC-08) cũng KHÔNG áp vào thao tác Lưu ở Tab Tiêu chí — kiểm tại cổng thêm/lưu người đánh giá và trình phê duyệt phân công, cùng cổng với ràng buộc tổng trọng số 100% đang làm.

Căn cứ (SRS bản chốt, đã mở file kiểm số dòng ngày 03/08):
- srs-fr-08-danh-gia.md:202 — "Kiểm tra tổng trọng số = 100% cho toàn đợt (cảnh báo nếu khác, cho phép lưu)".
- srs-fr-08-danh-gia.md:862 — SCR-VI-01 Tab 1 thành phần 31: Alert banner, mã WRN-DG-TC-01, "Tổng trọng số hiện tại: {X}%. Cần đảm bảo = 100% trước khi trình phê duyệt", điều kiện hiện: khi SUM != 100%.
- srs-fr-08-danh-gia.md:863 — thành phần 31b: Alert banner, mã WRN-DG-TC-02, "Tổng điểm tối đa có trọng số hiện tại: {X}. Cần đảm bảo = 100 trước khi trình phê duyệt".
- srs-fr-08-danh-gia.md:860 — thành phần 30 (nhãn "Tổng trọng số: {X}%" xanh/đỏ) phần mềm ĐÃ làm đúng; thiếu là thành phần 31 và 31b.
Bản .docx v2.0 mục 4.8.2.2.3 STT 6 "Lưu" trường hợp 2 cùng chiều — không có chênh lệch tài liệu. SRS đã cập nhật ngày 31/07 (CHANGELOG Phase 13); Kết quả mong đợi của test case giữ nguyên, đối tác không phải sửa.