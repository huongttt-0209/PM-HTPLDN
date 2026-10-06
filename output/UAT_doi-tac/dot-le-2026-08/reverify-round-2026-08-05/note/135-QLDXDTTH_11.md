## [UAT_TGPL Doanh Nghiệp-tuần 2] row 135 — QLDXDTTH_11 — S1
Tên chức năng: 
Tác nhân: 
Mô tả: Quyền của Cán bộ nghiệp vụ trên tab "Đề xuất đào tạo": thiếu thao tác Tiếp nhận / Đánh dấu thực hiện, nhưng lại có nút Gửi đề xuất mới.
Điều kiện: 1. Đăng nhập tài khoản Cán bộ nghiệp vụ
2. Đơn vị của cán bộ có ít nhất 1 đề xuất đào tạo ở trạng thái "Mới gửi"
Dữ liệu đầu vào: Đề xuất QA-VERIFY-0803 (trạng thái "Mới gửi") thuộc đúng đơn vị của tài khoản cán bộ đang đăng nhập.
Các bước: 1. Vào Đào tạo, tập huấn -> Chương trình đào tạo -> tab "Đề xuất đào tạo"
2. Nhìn cột "Hành động" của dòng đề xuất đang ở trạng thái "Mới gửi"
3. Bấm vào nội dung đề xuất để mở màn chi tiết, nhìn các nút thao tác
4. Nhìn khu vực nút phía trên bên phải của tab
KQ mong đợi: Cán bộ nghiệp vụ của đơn vị tiếp nhận thực hiện được việc tiếp nhận và đánh dấu thực hiện đề xuất, để đề xuất đi tiếp trong quy trình thay vì đứng mãi ở trạng thái "Mới gửi".
Ngược lại, cán bộ không phải là người gửi đề xuất nên không cần chức năng gửi đề xuất mới.
Căn cứ: FR-III-13 (UC32) §Mô tả (dòng 1045) "CB NV tiếp nhận"; §Tác nhân (dòng 1047) "DN / NHT"; §Đặc tả màn hình SCR-III-01 - Thành phần 8 (dòng 1875) "Hành động (Xem, Tiếp nhận, Đánh dấu thực hiện)".
KQ thực tế (l1): Ngược lại hoàn toàn:
- Cột "Hành động" của MỌI dòng đều là dấu gạch ngang, không có nút nào. Màn chi tiết cũng chỉ có nút "Quay lại danh sách". Cán bộ không tiếp nhận được đề xuất, quy trình bị đứng.
- Nhưng nút "Gửi đề xuất mới" lại hiện với vai trò cán bộ, dù đặc tả chỉ cho Doanh nghiệp / Người hỗ trợ là người gửi. (Chưa bấm thử để tránh tạo dữ liệu rác.)
Đã kiểm bằng tài khoản Cán bộ nghiệp vụ thuộc đúng đơn vị tiếp nhận của đề xuất.
Trạng thái 1: Fail | P dev fix1: dev done | Q Verify: Open
KQ thực tế lần 2: 
Trạng thái 2:  | W dev fix2:  | X Verify2: 
--- NOTE (R: DEV phản hồi lần 1) ---
✅ Bug đúng (QA đo lại 04/08/2026 theo yêu cầu của BA, trên đúng môi trường bàn giao, bản dựng V1.0.5, tài khoản cbnv_tw thuộc Cục Bổ trợ tư pháp). Dev FE: cán bộ nghiệp vụ mở danh sách Đề xuất đào tạo thì cột "Hành động" trống ở 16/16 dòng — kể cả 4 đề xuất trạng thái "Mới gửi" thuộc CHÍNH đơn vị của cán bộ đó; mở màn chi tiết cũng chỉ có nút quay lại danh sách. Không có đường nào để tiếp nhận hay đánh dấu thực hiện, nên đề xuất đứng vĩnh viễn ở "Mới gửi".
Phần hỏng nằm ở giao diện, không phải ở phân quyền: máy chủ đã có sẵn chức năng tiếp nhận, đã cấp quyền tiếp nhận và sửa cho vai trò CB_NV_TW, và phép thử quyền bằng một mã bản ghi không tồn tại trả về "không tìm thấy bản ghi" chứ không phải "không có quyền" — tức yêu cầu đã qua được lớp kiểm tra quyền.
Mâu thuẫn đặc tả mà QA nêu trước đây đã tự khép: FR-III-13 (UC32) §Mô tả (dòng 1045) và SCR-III-01 Thành phần 8 (dòng 1875) đều giao việc tiếp nhận cho cán bộ nghiệp vụ, bản bàn giao mục 4.3.13.1 và 4.3.13.2.3 STT 4/5 cũng vậy. Chỉ dòng Ma trận phân quyền (srs-v3.5.md dòng 1309) còn ghi cán bộ chỉ có quyền đọc — đó là việc dọn tài liệu của BA, không chặn Dev. Major.

── CÁCH VERIFY sau Dev fix ──
Precondition: cbnv_tw (vai trò CB_NV_TW, Cục Bổ trợ tư pháp - Bộ Tư pháp) + màn Chương trình đào tạo → tab "Đề xuất đào tạo", có ít nhất 1 đề xuất trạng thái "Mới gửi" thuộc cùng đơn vị.
1) Mở tab "Đề xuất đào tạo", tìm dòng đề xuất "Mới gửi" cùng đơn vị, đọc cột "Hành động".
2) Mở màn chi tiết của chính đề xuất đó, đọc vùng thao tác.
3) Thực hiện tiếp nhận đề xuất, rồi mở lại danh sách.
✅ PASS khi: cán bộ có đường tiếp nhận đề xuất ngay trên danh sách hoặc trong màn chi tiết; sau khi tiếp nhận, trạng thái đề xuất chuyển khỏi "Mới gửi" và thay đổi này còn nguyên sau khi tải lại trang.
❌ FAIL nếu: cột "Hành động" vẫn trống ở dòng đề xuất cùng đơn vị đang ở "Mới gửi"; hoặc màn chi tiết vẫn chỉ có nút quay lại; hoặc bấm tiếp nhận mà trạng thái không đổi.
⚠️ Còn MỘT ý phụ chưa được BA trả lời, tách riêng, KHÔNG chặn phiếu này: vai trò cán bộ có được phép GỬI đề xuất đào tạo không? Máy chủ đang cấp quyền tạo và trên môi trường có 4 đề xuất do "CB Nghiệp vụ TW 01" gửi, nhưng §Tác nhân của FR-III-13 (dòng 1047) và bản bàn giao mục 4.3.13.2.3 STT 1 chỉ ghi doanh nghiệp và người hỗ trợ pháp lý. Đừng chấm FAIL vì nút "Gửi đề xuất mới" còn hiện với vai trò cán bộ.
Bằng chứng đo: do-lai-QLDXDTTH_11-2026-08-04.md + image/BUG-QLDXDTTH_11-doban-giao-danhsach-hanhdong-gachngang.png