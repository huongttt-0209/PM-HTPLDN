# Tiêu chí chấm — IBMHD_07 (dòng 119)

> Round 7 · 2026-07-25. **CẤM tự đặt tiêu chí khác.** Chấm theo đúng 2 khối dưới:
> (A) bar gốc dev đặt ở round trước, (B) các lỗi CÒN LẠI mình đã ghi cho đối tác ở lượt Reopen gần nhất.
> PASS = (A) đủ điều kiện PASS **và** (B) không còn gạch đầu dòng nào tái hiện.

## Case gốc (đối tác)
- **Mô tả:** Một số lỗi
- **Điều kiện:** 1. Đăng nhập tài khoản
- **Các bước:** 1. Chọn menu "Biểu mẫu" -> "Danh sách biểu mẫu"
2. Kéo thả hoặc chọn tệp trên ô tải tệp
3. Bấm nút "Xác nhận nhập {X} tệp hợp lệ"
- **KQ mong đợi:** Hệ thống hiển thị thông điệp "Nhập thành công {X} tệp. {Y} tệp lỗi: xem chi tiết" kèm bảng chi tiết lý do từng tệp lỗi.
- **KQ thực tế (đối tác báo):** Hệ thống không hiển thị "{Y} tệp lỗi: xem chi tiết" kèm bảng chi tiết lý do từng tệp lỗi.

## (A) Bar gốc của DEV — bộ "CÁCH VERIFY" đã chốt

✅ Bug đúng (BA duyệt 24/07/2026). Loại 1 — SRS quy định rõ nhánh này, phần mềm thiếu.
Yêu cầu nghiệp vụ: màn kết quả sau khi nhập hàng loạt phải LUÔN cho người dùng thấy tổng hợp hai con số — bao nhiêu tệp đã thành biểu mẫu và bao nhiêu tệp bị lỗi — kèm lối xem chi tiết từng tệp lỗi với tên tệp và lý do; phần lỗi phải gộp cả tệp bị loại từ bước chọn tệp lẫn tệp phát sinh lỗi khi đang ghi. Hiện app chỉ báo số nhập thành công nên người dùng không biết mình mất tệp nào.
Căn cứ SRS: srs-v3.5/srs-fr-09-bieu-mau.md:483 (FR-VII-06 Processing bước 4 — "Với mỗi file lỗi: ghi vào báo cáo lỗi (tên tệp + lý do)"), :484 (bước 5 — "Trả về tổng hợp: N thành công, M lỗi"), :492 (§Error Handling E2, WRN-IMP-01 — "Import thành công {N} file. {M} file lỗi: xem chi tiết"), :502 (§Outputs chi_tiet_loi — "[{file_ten, ly_do}] | Khi có lỗi"), :511-512 (§Acceptance Criteria — "Given 1+ file lỗi When import Then báo cáo lỗi chi tiết, import các file hợp lệ còn lại" và "Then hiển thị tổng hợp: N file thành công, M file lỗi"), :506 (§Postconditions — "File lỗi được ghi vào báo cáo chi tiết"). (BA trích :469/:479/:489/:498-499 theo bản SRS trước khi cập nhật.) Mức Minor.

── CÁCH VERIFY sau Dev fix ──
Precondition: cbnv_bn / Test@1234 (CB Nghiệp vụ — vai trò case chỉ định) · https://18.143.165.120.nip.io/bieu-mau/nhap-hang-loat · cần 1 thư mục đích trống mới tạo (đặt tên QA-IMPORT-KQ, để bước 5 đếm được) và 4 tệp: 2 tệp .docx hợp lệ dưới 20MB; 1 tệp sai định dạng qa-loi.txt; 1 tệp qa-hong.docx đúng đuôi nhưng NỘI DUNG HỎNG — tạo bằng cách đổi tên một tệp .txt hoặc một ảnh thành .docx, hoặc cắt bỏ vài nghìn byte đầu của một tệp .docx thật. Tệp qa-hong.docx dùng để dựng nhánh lỗi phát sinh lúc ghi mà bước chọn tệp không lọc được — đây chính là phần BA yêu cầu QA seed thêm để xác minh.
1) Chọn Thư mục đích = QA-IMPORT-KQ.
2) Chọn cả 4 tệp trong cùng một lượt, đi tiếp tới bước xác nhận.
3) Bấm nút xác nhận nhập.
4) Đọc nguyên văn thông báo / màn kết quả, rồi bấm vào lối "xem chi tiết" và đọc bảng chi tiết.
5) Mở https://18.143.165.120.nip.io/bieu-mau/danh-sach, lọc theo thư mục QA-IMPORT-KQ, đếm số biểu mẫu.
✅ PASS khi ĐỦ 3 điều: (i) màn kết quả nêu CẢ HAI con số — số tệp nhập thành công VÀ số tệp lỗi — chứ không chỉ một câu kiểu đã nhập thành công N biểu mẫu; (ii) có lối mở chi tiết và bảng chi tiết liệt kê từng tệp lỗi kèm tên tệp và lý do, trong đó có tên qa-loi.txt; (iii) bước 5 đếm được đúng 2 biểu mẫu trong QA-IMPORT-KQ — tức các tệp hợp lệ vẫn được nhập, không bị chặn cả lô.
❌ FAIL nếu: màn kết quả chỉ có số thành công, không có số tệp lỗi; HOẶC có số lỗi nhưng không mở được chi tiết tên tệp + lý do; HOẶC cả lô bị chặn nên QA-IMPORT-KQ trống.
⚠️ Nếu qa-hong.docx được app nhận và tạo thành biểu mẫu bình thường thì chưa đủ dữ liệu để chấm riêng nhánh lỗi-lúc-ghi. Khi đó vẫn chấm PASS/FAIL bằng qa-loi.txt: tệp bị loại ở bước chọn VẪN phải được đếm vào số tệp lỗi ở màn kết quả, vì SRS bắt gộp cả tệp bị loại sớm. Đừng vì không dựng được lỗi-lúc-ghi mà kết luận không test được.
⚠️ Tệp trùng tên với biểu mẫu đã có KHÔNG phải tệp lỗi — bảng đối chiếu điều kiện QA ngày 20/07/2026 (reverify-week-3/cond/IBMHD_07.md) ghi nhận app chấp nhận tệp trùng tên. Đừng dùng trùng tên để dựng nhánh lỗi.
Ảnh lỗi cũ: image/BUG-IBMHD_07-step3-ket-qua-import.png

## (B) Lỗi CÒN LẠI sau lượt Reopen gần nhất (nội dung đang nằm ở cột R của sheet)

- Kịch bản: thư mục đích QA-IMPORT-KQ mới tạo (trống). Chọn 4 tệp trong 1 lượt: 2 tệp .docx hợp lệ, 1 tệp qa-loi.txt sai định dạng, 1 tệp qa-hong.docx đúng đuôi nhưng nội dung hỏng.
- Phần đã đạt: 2 tệp hợp lệ vẫn được nhập bình thường, không bị chặn cả lô — mở danh sách lọc theo thư mục QA-IMPORT-KQ đếm đúng 2 biểu mẫu.
- Còn lỗi 1: màn kết quả cuối ghi "Nhập biểu mẫu hoàn tất: 2 thành công / 0 lỗi" — báo 0 lỗi trong khi thực tế có 2 tệp bị loại: qa-loi.txt bị loại ngay lúc chọn tệp, qa-hong.docx bị loại lúc tải lên (có thông báo "Tệp không hợp lệ hoặc bị hỏng" và dòng đếm ở bước chọn tệp ghi "Đã tải lên thành công: 2/3 · Có file lỗi"). Người dùng nhìn màn kết quả vẫn không biết mình mất 2 tệp nào.
- Còn lỗi 2: màn kết quả không có lối xem chi tiết tệp lỗi. Toàn màn chỉ có dòng kết quả và 2 nút "Quay lại danh sách" / "Nhập tiếp"; không có bảng liệt kê tên tệp lỗi kèm lý do.
- Ghi nhận thêm: ở bước Kiểm tra, bảng kiểm tra có liệt kê qa-loi.txt kèm lý do, nhưng qa-hong.docx không có dòng nào trong bảng đó.
- Kiểm tra ngày 25/07/2026, tài khoản CB Nghiệp vụ Bộ ngành.
