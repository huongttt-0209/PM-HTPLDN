# Bảng đối chiếu điều kiện — re-verify TDHSTVV_14 lần 2 (row 68, mode reverify2, 30/07/2026 23:26)

Lượt trước (30/07 22:29-22:36) FAIL ở tiêu chí (1) và (5): thông báo trên màn sau "Gửi KQ" chỉ hiện
"Đã lưu kết quả thẩm định" cho cả hai kết luận. Dev báo đã fix → đo lại ĐỦ 5 tiêu chí, kể cả 3 tiêu
chí đã đạt, vì sửa câu chữ có thể động vào chính luồng phát thông báo và thư.

| Điều kiện | Bug gốc / CÁCH VERIFY yêu cầu | Mình test | GAP? |
|---|---|---|---|
| Tài khoản Người hỗ trợ | `nht_qa_tw` / Test@1234, Cục Bổ trợ tư pháp | Đúng `nht_qa_tw` — tạo + nộp 2 hồ sơ, đọc màn Thông báo | Không |
| Tài khoản thẩm định | `cbnv_tw` / Test@1234, cùng đơn vị | Đúng `cbnv_tw` — bấm "Bắt đầu thẩm định" và "Gửi KQ" bằng tay trên giao diện cả 2 nhánh | Không |
| Hồ sơ phải do CHÍNH Người hỗ trợ đó nộp (bẫy a) | Hồ sơ do nht_qa_tw nộp | 2 hồ sơ mới `TVV-BTP-TW-0028` và `TVV-BTP-TW-0029`, tạo trong chính phiên đăng nhập `nht_qa_tw`; người tạo trên hồ sơ trùng đúng tài khoản đó; thông báo và thư đều về đúng `nht_qa_tw` | Không |
| Phải dùng hồ sơ MỚI, không dùng lại bản ghi lượt trước | Fix về câu chữ sinh tại thời điểm thao tác | 3 hồ sơ lượt trước (0025/0026/0027) đều ở trạng thái cuối, không thẩm định lại được → seed 2 hồ sơ mới đi trọn luồng. Không đụng bất kỳ hồ sơ cũ nào | Không |
| Trạng thái hồ sơ khi thẩm định | Đang thẩm định / Chờ phê duyệt | Cả 2 đi đúng đường Mới đăng ký → "Bắt đầu thẩm định" → Đang thẩm định → "Gửi KQ" | Không |
| KHÔNG dùng hồ sơ ở "Yêu cầu bổ sung" sẵn có (bẫy e) | Tránh lỗi khác đã ghi ở vòng 1 | Mỗi hồ sơ chỉ thẩm định đúng 1 lần từ Đang thẩm định; sau khi gửi kết quả thẻ Thẩm định tự biến mất, không thao tác lại | Không |
| Phải kiểm CẢ HAI nhánh kết luận (bẫy d) | "Không đạt" và "Yêu cầu bổ sung" | Nhánh "Không đạt" trên 0028, nhánh "Yêu cầu bổ sung" trên 0029; mỗi nhánh đo đủ 4 điều | Không |
| Lý do nhập vào | "Thiếu bản sao thẻ hành nghề" / "Bổ sung bằng tốt nghiệp" | Đúng 2 chuỗi đó | Không |
| Mốc đối chiếu số thông báo (bước 1) | Ghi số thông báo trước khi thẩm định | Đọc lại mốc mới ngay đầu lượt: 4 bản ghi → sau nhánh Không đạt 5 → sau nhánh Yêu cầu bổ sung 6, tăng đúng +1 mỗi lần | Không |
| Kênh thư điện tử | MailHog http://18.143.165.120:8025 | Đọc trực tiếp; thư tới `nht.qa.tw@htpldn.test` và tới email khai trên hồ sơ ứng viên, cả 2 nhánh | Không |
| Cách đo thông báo tự tắt | Không được kết luận hụt do thông báo biến mất | Cài bộ theo dõi thay đổi trang TRƯỚC khi bấm, KHÔNG lọc trùng; hẹn giờ bấm rồi mới chụp (mốc 4,29 giây) — bắt được đúng khung cả 2 lần | Không |
| Không lẫn dữ liệu người khác | — | Trong lúc chạy có tài khoản `nht_tw` (khác `nht_qa_tw`) cũng phát sinh thông báo/thư trên cùng môi trường; đã lọc theo đúng hộp thư `nht.qa.tw` và đúng tên hồ sơ "QA R5" | Không |
| Cách kết luận câu chữ (bẫy c) | Không so chuỗi cứng, phải nói rõ bị TỪ CHỐI | Đo nội dung thực tế: "Đã từ chối hồ sơ" phản ánh đúng kết quả; xác nhận KHÔNG còn chuỗi "Đã lưu kết quả thẩm định" | Không |
