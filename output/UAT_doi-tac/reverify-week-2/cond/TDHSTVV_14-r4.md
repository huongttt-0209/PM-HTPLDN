# Bảng đối chiếu điều kiện — re-verify TDHSTVV_14 (row 68, mode reverify2, 30/07/2026)

Bug gốc (vòng 2): thẩm định hồ sơ TVV kết luận "Không đạt" / "Yêu cầu bổ sung" nhưng Người hỗ trợ đã
nộp hồ sơ không nhận được thông báo; thân thư mang tiêu đề sai ("Phê duyệt" + tích xanh trên thư từ chối).
BA chốt 30/07/2026: bổ sung Người hỗ trợ vào danh sách nhận cho CẢ HAI kết luận, cả 2 kênh; thông báo
phải phản ánh đúng việc hồ sơ bị từ chối.

| Điều kiện | Bug gốc / CÁCH VERIFY yêu cầu | Mình test | GAP? |
|---|---|---|---|
| Tài khoản Người hỗ trợ | `nht_qa_tw` / Test@1234, Cục Bổ trợ tư pháp | Đúng `nht_qa_tw` | Không |
| Tài khoản thẩm định | `cbnv_tw` / Test@1234, cùng đơn vị | Đúng `cbnv_tw`, cùng Cục Bổ trợ tư pháp | Không |
| Hồ sơ phải do CHÍNH Người hỗ trợ đó nộp (bẫy a) | Hồ sơ do nht_qa_tw nộp | 3 hồ sơ tự tạo trong phiên bằng chính `nht_qa_tw`: TVV-BTP-TW-0025 / 0026 / 0027; đã đối chiếu người tạo của hồ sơ trùng đúng tài khoản `nht_qa_tw`. Cố tình KHÔNG dùng TVV-BTP-TW-0019/0020 vì do `cbnv_tw` tạo | Không |
| Trạng thái hồ sơ phải cho phép thẩm định | Đang thẩm định / Chờ phê duyệt | Cả 3 đi đúng đường Mới đăng ký → "Bắt đầu thẩm định" → Đang thẩm định → "Gửi KQ"; cả 3 lần Gửi KQ đều thành công, không phát sinh lỗi kỹ thuật | Không |
| KHÔNG dùng hồ sơ ở "Yêu cầu bổ sung" sẵn có (bẫy e) | Tránh lỗi khác đã ghi ở vòng 1 | Không đụng TVV-BTP-TW-0022 và TVV-BTP-TW-0003 (đang ở Yêu cầu bổ sung) | Không |
| Phải kiểm CẢ HAI nhánh kết luận (bẫy d) | "Không đạt" và "Yêu cầu bổ sung" | Chạy nhánh "Không đạt" 2 lần (0025, 0027) + nhánh "Yêu cầu bổ sung" 1 lần (0026); mỗi nhánh đều đi đủ bước Thông báo trong phần mềm + MailHog | Không |
| Lý do nhập vào | "Thiếu bản sao thẻ hành nghề" / "Bổ sung bằng tốt nghiệp" | Đúng 2 chuỗi đó | Không |
| Mốc đối chiếu số thông báo (bước 1) | Ghi số thông báo trước khi thẩm định | Mốc = 1 bản ghi ("Kích hoạt tài khoản hệ thống PM-HTPLDN" 12/07/2026); sau mỗi lần Gửi KQ tăng đúng +1, đi 1 → 4 trong phiên | Không |
| Kênh thư điện tử | MailHog http://18.143.165.120:8025 | Đọc trực tiếp MailHog, xác nhận thư gửi `nht.qa.tw@htpldn.test` và thư gửi email khai trên hồ sơ ứng viên | Không |
| Cách đo thông báo tự tắt | Không được kết luận hụt do thông báo biến mất | Cài bộ theo dõi thay đổi trên trang TRƯỚC khi bấm, KHÔNG lọc trùng; hẹn giờ bấm nút rồi mới chụp màn hình nên bắt được đúng lúc thông báo còn hiển thị (ảnh 02 và 06) | Không |
| Cách kết luận câu chữ (bẫy c) | Không so chuỗi cứng, nhưng phải nói rõ bị TỪ CHỐI | Đo nội dung thực tế; chuỗi thu được là "Đã lưu kết quả thẩm định", hoàn toàn không nhắc kết quả từ chối → tính KHÔNG ĐẠT đúng theo bẫy | Không |
