# Bảng đối chiếu điều kiện — re-verify TKDGHQHTPL_02 (row 47 tuần 1, mode reverify2, 30/07/2026)

Bug gốc (vòng 2): thang điểm đánh giá hiệu quả không nhất quán — điểm tối đa mặc định 10 trong khi
Dashboard hiển thị thang /100. BA chốt 30/07/2026: thêm BR-CALC-08 (tổng của điểm tối đa × trọng số
÷ 100 phải = 100), đổi mặc định điểm tối đa 10 → 100, Dashboard GIỮ NGUYÊN, không quy đổi dữ liệu cũ.

| Điều kiện | Bug gốc / CÁCH VERIFY yêu cầu | Mình test | GAP? |
|---|---|---|---|
| Vai trò/tài khoản đo | `cbnv_tw` / Test@1234 | Đúng `cbnv_tw` cho toàn bộ phần đo trên giao diện | Không |
| Tài khoản phụ (chỉ dựng dữ liệu) | Không nêu; bước duyệt phân công cần vai trò phê duyệt | `cbpd_tw_01` / Test@1234 chỉ dùng để duyệt phân công (`cbpd_tw` hỏng mật khẩu); không dùng để đo tiêu chí nào | Không |
| Màn A | Đánh giá hiệu quả → Kế hoạch đánh giá → cấu hình tiêu chí | Đúng màn đó | Không |
| Màn B + bộ lọc | Tổng quan hệ thống, Cấp đơn vị "Trung ương" + Đơn vị "Cục Bổ trợ tư pháp - Bộ Tư pháp", Năm 2026, Tháng "Tất cả" | Đúng bộ lọc đó (Tháng hiển thị là "Cả năm") | Không |
| Phải dùng kế hoạch MỚI (bẫy b) | Không được kiểm bằng kế hoạch cũ vì BA chốt không quy đổi dữ liệu cũ | Tạo kế hoạch hoàn toàn mới `DG-20260730-0003` ngay trong lượt kiểm; không mở, không sửa `DG-20260730-0001`, `DG-20260730-0002` hay bất kỳ kế hoạch có sẵn nào trong 18 kế hoạch của env | Không |
| Cấu hình bước 2 | 50% + 50%, điểm tối đa 10 và 10 | Đúng cấu hình đó → bị chặn lưu | Không |
| Cấu hình bước 3 | 50% + 50%, điểm tối đa 100 và 100 | Đúng cấu hình đó → lưu thành công | Không |
| Cấu hình bước 4 | 50% + 50%, điểm tối đa 200 và 200 | Đúng cấu hình đó. Giao diện chặn trần 100 nên không nhập nổi 200; đã gửi thẳng cấu hình 200+200 cho máy chủ để đọc câu từ chối. Hai đường đo thống nhất: không cách nào lưu được | Không |
| Cấu hình bước 5 (bẫy a) | 30% + 70%, điểm tối đa 100 và 100 — PHẢI lưu được | Đúng cấu hình đó → lưu thành công, bảng hiện 30/100 và 70/100, tổng trọng số 100%. Không lấy việc này làm căn cứ trượt | Không |
| Đối tượng chấm ở bước 6 | 1 đối tượng, chấm đạt điểm tối đa cả 2 tiêu chí | Vụ việc `VV-QA-005`, phân công `cbnv_tw` làm Trưởng nhóm, duyệt phân công, chấm 100 + 100 | Không |
| Bước 7 chỉ xét nhãn/trục/không vượt 100 (bẫy c) | Số trung bình thấp do trộn trần cũ 10 và trần mới 100 KHÔNG phải lỗi | Chỉ đối chiếu 3 thứ bước 7 yêu cầu; con số 21.2/100 không tính là lỗi | Không |
| Không báo lỗi thẻ đào tạo thang /10 (bẫy d) | Thẻ "Chất lượng đào tạo, bồi dưỡng pháp lý" /10 là cố ý đúng | Thẻ đó đang hiện 7.3/10 trên cùng màn — bỏ qua có chủ ý, không đưa vào căn cứ | Không |
