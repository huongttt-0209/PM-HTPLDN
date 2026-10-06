⚠️ Cần BA xác nhận — khối truy vết "Chương trình HTPL liên quan trong kỳ" ĐÃ CÓ và dùng được, nhưng chỉ hiện sau khi cán bộ bấm [Lập báo cáo]; đặc tả không có dòng nào quy định khối này nên chưa đủ căn cứ chấm hết lỗi.

Đo ngày 07/08/2026 trên môi trường nội bộ 18.143.165.120.nip.io, bó mã giao diện index-D4Buvu4S.js (07/08/2026 02:23) — đã tải lại trang bằng địa chỉ và đọc lại tên bó mã ngay trong tab trước khi đo.
Tài khoản: cbnv_hn (Cán bộ Nghiệp vụ Địa phương — Sở Tư pháp Hà Nội), đúng vai trò và đúng cấp theo đặc tả.

PHẦN ĐÃ ĐẠT — khối tồn tại và hoạt động đúng:
- Trên màn Chi tiết đợt báo cáo, trong thẻ "Nhận xét, kiến nghị" có khối nhãn "Chương trình HTPL liên quan trong kỳ", kèm dòng mô tả "Tùy chọn — dùng để truy vết các chương trình đơn vị đã triển khai trong kỳ báo cáo" — gần như nguyên văn yêu cầu tại srs-fr-15-ct-htpldn.md:732.
- Điều khiển đúng kiểu chọn nhiều giá trị có tìm kiếm, khớp mô tả "Multi-select" và cột Nguồn nhập ghi "Chọn" tại :732.
- Chọn được chương trình, bấm Lưu nháp, rồi TẢI LẠI TRANG: lựa chọn vẫn còn trên giao diện và dữ liệu nguồn lưu đúng mã chương trình đã chọn. Hai đường đo khớp nhau, nên không phải trường hợp "khối chỉ có vỏ".

Một chi tiết cần nói rõ để không hiểu nhầm: lượt quét đầu tiên, ô chọn mở ra nhưng hiện "Trống". Đã kiểm và xác định đây KHÔNG phải lỗi: giao diện gọi đúng địa chỉ lấy danh sách chương trình và nhận phản hồi thành công với 0 bản ghi, vì toàn bộ 14 chương trình đang có trên môi trường đều thuộc đơn vị Cục Bổ trợ tư pháp (Trung ương), còn đơn vị đang đo (Sở Tư pháp Hà Nội) chưa sở hữu chương trình nào. Đúng theo :732 thì khối này chỉ liệt kê chương trình của chính đơn vị, nên danh sách rỗng là phân quyền dữ liệu đúng. Để kiểm được trọn vẹn, QA đã tạo một chương trình thử cho Sở Tư pháp Hà Nội (mã CT-20260807-0001) — đây là dữ liệu QA dựng để kiểm thử, có thể xóa sau khi đối tác đọc xong kết quả. Sau khi có dữ liệu, khối hoạt động đầy đủ như mô tả ở trên.

PHẦN CẦN BA QUYẾT — vì sao chưa chấm hết lỗi được:
Làm đúng 2 bước ghi trong phiếu (mở menu "Đợt báo cáo" rồi mở Chi tiết đợt báo cáo) trên đợt mà đơn vị chưa bắt đầu lập báo cáo, thì màn chỉ có thẻ Biểu mẫu 21a; thẻ "Nhận xét, kiến nghị" không hiện, mà khối truy vết lại nằm bên trong thẻ đó nên cũng không hiện. Nghĩa là quan sát của đối tác không sai — chỉ là đo ở thời điểm trước khi bắt đầu lập.
Nhưng cũng chưa đủ căn cứ kết luận là lỗi: bảng thành phần màn hình của màn Chi tiết đợt báo cáo (:1163–1175, gồm 11 dòng) KHÔNG có dòng nào khai khối truy vết chương trình liên quan, nên đặc tả cũng không quy định nó phải là khối riêng, đặt ở đâu, hay hiện ở trạng thái nào. Yêu cầu về khối này hiện chỉ nằm ở phần dữ liệu đầu vào của chức năng Lập báo cáo (:732, :744, :745, :1417).

⚠️ CẦN BA CONFIRM (chung với phiếu LBCKQTHCT_05, chỉ cần trả lời một lần):
(1) Khi đơn vị chưa vào pha lập báo cáo, màn Chi tiết đợt báo cáo có phải hiển thị phần lập báo cáo — gồm khối "Nhận xét, kiến nghị" và khối "Chương trình HTPL liên quan" — ở dạng chỉ đọc không, hay đúng là chỉ hiện khi bắt đầu lập?
(2) Đề nghị bổ sung một dòng cho khối truy vết chương trình liên quan vào bảng thành phần màn hình Chi tiết đợt báo cáo (hiện dừng ở dòng #45), ghi rõ kiểu điều khiển, vị trí và điều kiện hiển thị, để các vòng sau có căn cứ chấm thay vì phải suy từ phần dữ liệu đầu vào.
(3) Khối này đang đặt lồng trong thẻ "Nhận xét, kiến nghị" — có đúng ý đồ thiết kế không, hay cần tách thành khối riêng?
Mục đích là bổ sung, làm rõ đặc tả màn hình, KHÔNG chặn bàn giao — chức năng truy vết đã dùng được bình thường.

Ghi nhận thêm, không thuộc phạm vi phiếu: danh sách đổ vào ô chọn hiện không lọc theo trạng thái chương trình (chương trình còn ở Dự thảo vẫn xuất hiện) và không lọc theo kỳ báo cáo. Đặc tả không quy định các bộ lọc này nên chỉ ghi nhận, có thể gộp vào câu hỏi (2) nếu BA muốn siết lại.

Về bằng chứng gốc: file LBCKQTHCT_06.jpg và LBCKQTHCT_05.jpg là cùng một file ảnh (trùng mã băm), tức một ảnh đang dùng cho hai khiếu nại về hai khối khác nhau; ảnh lại chỉ bắt phần dưới trang. Vì vậy QA không dựa vào ảnh mà tự tái hiện đúng các bước phiếu mô tả để đo.
