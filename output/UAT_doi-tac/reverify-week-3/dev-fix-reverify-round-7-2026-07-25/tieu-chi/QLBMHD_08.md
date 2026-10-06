# Tiêu chí chấm — QLBMHD_08 (dòng 101)

> Round 7 · 2026-07-25. **CẤM tự đặt tiêu chí khác.** Chấm theo đúng 2 khối dưới:
> (A) bar gốc dev đặt ở round trước, (B) các lỗi CÒN LẠI mình đã ghi cho đối tác ở lượt Reopen gần nhất.
> PASS = (A) đủ điều kiện PASS **và** (B) không còn gạch đầu dòng nào tái hiện.

## Case gốc (đối tác)
- **Mô tả:** Có mã độc
- **Điều kiện:** 1. Đăng nhập tài khoản
- **Các bước:** 1. Chọn menu "Biểu mẫu" -> "Danh sách biểu mẫu"
2. Nhấn "+ Thêm mới"
- **KQ mong đợi:** Hệ thống hiển thị thông điệp "Tệp chứa mã độc, không thể lưu trữ".
- **KQ thực tế (đối tác báo):** Hệ thống hiển thị thông báo không giống với thiết kế

## (A) Bar gốc của DEV — bộ "CÁCH VERIFY" đã chốt

✅ Bug đúng (BA duyệt 24/07/2026) — case này có 2 việc, KHÔNG chỉ là chữ thông báo.
Việc (1) — CHỮ thông báo: khi hệ thống phát hiện tệp chứa mã độc và từ chối, thông báo phải nói rõ lý do là mã độc theo chuỗi đã văn bản hóa, không dùng thông báo chung chung. Mức Minor.
Việc (2) — XÁC NHẬN phạm vi quét: bộ quét mã độc phải chạy TRƯỚC khi lưu tệp và phải quét được nội dung BÊN TRONG tệp nén định dạng Office (.docx/.xlsx). Mức Major — BA đặt ưu tiên cao hơn phần chữ. Nghĩa vụ phòng ngừa, ngăn chặn phần mềm độc hại theo Luật An toàn thông tin mạng 2015 (86/2015/QH13) Điều 11 Khoản 1; không có phương án bỏ qua.
Căn cứ SRS (bản Docs-PM-HTPLDN/.../srs-v3.5/) — 3 chỗ: srs-fr-09-bieu-mau.md:325 (Processing bước 5 "Quét virus file đính kèm"); :394 — "| EC-02 | File chứa macro virus (doc/docx) | Quét antivirus trước lưu trữ → ERR-BM-07 nếu phát hiện mã độc |"; :666 (SCR-VII-02 hàng 15, ô File đính kèm: "Bắt buộc. doc/docx/xls/xlsx. Max 20MB. Quét virus"). Bản input/srs-update-2026-5-5/ tương ứng :314, :382, :652.
⚠️ ĐIỂM CẦN LƯU Ý KHI ĐỌC KẾT LUẬN BA: BA đính chính "phần chặn đã có hiệu lực" dựa trên tệp eicar.docx của đối tác bị từ chối. Nhưng bản đo 20/07/2026 (cbnv_tw) ghi ở ba-confirm/bieu-mau/ba-confirmation-needed-week-3-bieu-mau-tong-hop.md:643 rằng tệp đó bị chặn ở bước kiểm ĐỊNH DẠNG (thông báo "Nội dung file không khớp định dạng…"), CHƯA chạm tới bước quét mã độc; và :644 ghi tệp .docx đúng cấu trúc Office có chèn chuỗi EICAR (valid-eicar.docx) được máy chủ NHẬN (mã 201), tệp báo tải xong, submit tạo biểu mẫu THÀNH CÔNG, không thông báo gì. Vì vậy phép thử quyết định phải dùng tệp Office HỢP LỆ, không dùng tệp rác đổi đuôi.

── CÁCH VERIFY sau Dev fix ──
Precondition: cbnv_tw / Test@1234 tại https://18.143.165.120.nip.io/bieu-mau/them-moi. Cần 2 tệp: (a) eicar.docx = chuỗi thử EICAR thô đổi đuôi .docx; (b) valid-eicar.docx = một tệp .docx mở được bằng Word, chèn chuỗi thử EICAR chuẩn (nguyên văn chuỗi ghi ở reverify-audit/QLBMHD_08/toast-capture.md) vào word/document.xml rồi nén lại đúng cấu trúc Office. EICAR là tệp thử diệt virus chuẩn công nghiệp, vô hại. Cài tools/toast-capture.js trước mỗi lần chọn tệp.
1) Chọn eicar.docx → ghi nguyên văn thông báo.
2) Chọn valid-eicar.docx → ghi nguyên văn thông báo + mã trả về của yêu cầu tải tệp lên.
3) Nếu bước 2 KHÔNG bị chặn: điền Thư mục "Thư mục biểu mẫu seed" + Tên biểu mẫu QA-eicar-row101 rồi bấm Thêm mới.
4) Mở /bieu-mau/danh-sach tìm QA-eicar-row101.
✅ PASS khi đủ 3 điều: (i) bước 2 tệp bị TỪ CHỐI — yêu cầu tải lên không trả mã thành công, tệp không được lưu; (ii) thông báo ở bước 2 nói rõ tệp chứa mã độc, theo chuỗi ERR-BM-07 "Tệp chứa mã độc, không thể lưu trữ" — KHÔNG dùng thông báo chung "Upload file thất bại. Vui lòng thử lại."; (iii) bước 4 KHÔNG tìm thấy biểu mẫu QA-eicar-row101, tức không bản ghi nào được tạo.
❌ FAIL nếu: bước 2 máy chủ nhận tệp (mã 2xx) hoặc dòng tệp báo tải xong; HOẶC bước 3-4 tạo được biểu mẫu; HOẶC bị chặn nhưng thông báo vẫn là chuỗi chung không nêu mã độc.
⚠️ Bẫy 1 (quan trọng nhất) — KHÔNG kết luận PASS chỉ vì bước 1 (eicar.docx) bị chặn: theo bản đo 20/07/2026 tệp đó bị chặn bởi bước kiểm ĐỊNH DẠNG nên không chứng minh được bộ quét mã độc có chạy. Phép thử quyết định là bước 2.
⚠️ Bẫy 2 — hai điểm không quan sát được từ giao diện, phải có xác nhận của Dev/Security bằng văn bản mới đóng case: bộ quét chạy TRƯỚC khi lưu tệp, và bộ quét có giải nén để đọc nội dung bên trong tệp .docx/.xlsx. Chỉ bước 2 bị chặn mà chưa có 2 xác nhận này thì giữ case mở.
Ảnh hiện trạng: reverify-audit/QLBMHD_08/eicar-accepted-list.png (biểu mẫu chứa chuỗi thử mã độc được tạo thành công, đo 20/07/2026, cbnv_tw).

## (B) Lỗi CÒN LẠI sau lượt Reopen gần nhất (nội dung đang nằm ở cột R của sheet)

- Phần chặn và chữ thông báo: ĐÃ ĐẠT trên giao diện.
- Tệp .docx đúng cấu trúc Office có chèn chuỗi thử diệt virus (EICAR) bên trong nội dung: bị TỪ CHỐI, yêu cầu tải lên trả mã 400 với mã lỗi ERR-BM-07, thông báo hiện lên đúng chữ "Tệp chứa mã độc, không thể lưu trữ", dòng tệp chuyển sang trạng thái lỗi và tệp không được đính kèm vào biểu mẫu.
- Tệp rác đổi đuôi .docx cũng bị từ chối với đúng thông báo mã độc nêu trên (trước đây bị chặn ở bước kiểm định dạng).
- Kiểm tra lại danh sách biểu mẫu: không sinh ra bản ghi nào từ các lần thử trên.
- Việc bộ quét đọc được nội dung BÊN TRONG tệp nén Office đã được chứng minh qua kết quả trên.
- Còn 1 việc chưa thể xác nhận từ phía kiểm thử: bộ quét mã độc chạy TRƯỚC khi ghi tệp vào kho lưu trữ (không quan sát được từ giao diện). Theo hướng dẫn kiểm thử của case, cần Dev/An toàn thông tin xác nhận bằng văn bản điểm này rồi mới đóng case. Rất mong đội phát triển bổ sung xác nhận, sau đó chúng tôi sẽ chuyển sang Pass ngay.
- Kiểm tra ngày 25/07/2026, tài khoản CB Nghiệp vụ Trung ương.
