# Tiêu chí chấm — QLBMHD_13 (dòng 106)

> Round 7 · 2026-07-25. **CẤM tự đặt tiêu chí khác.** Chấm theo đúng 2 khối dưới:
> (A) bar gốc dev đặt ở round trước, (B) các lỗi CÒN LẠI mình đã ghi cho đối tác ở lượt Reopen gần nhất.
> PASS = (A) đủ điều kiện PASS **và** (B) không còn gạch đầu dòng nào tái hiện.

## Case gốc (đối tác)
- **Mô tả:** Kiểm tra nút chức năng "Sửa
- **Điều kiện:** 1. Đăng nhập tài khoản
- **Các bước:** 1. Chọn menu "Biểu mẫu" -> "Danh sách biểu mẫu"
2. Nhấn "Sửa"
- **KQ mong đợi:** Hệ thống mở biểu mẫu chỉnh sửa với dữ liệu hiện tại, cho phép thay tệp đính kèm.
- **KQ thực tế (đối tác báo):** Hệ thống không hiển thị file đính kèm mặc dù tồn tại file

## (A) Bar gốc của DEV — bộ "CÁCH VERIFY" đã chốt

✅ Bug đúng (BA duyệt 24/07/2026) — thuộc nhóm Loại 2: BA cập nhật SRS trước, Dev làm theo SRS mới. Yêu cầu nghiệp vụ: form Chỉnh sửa biểu mẫu phải cho người dùng thấy tệp ĐANG đính kèm (tên tệp + cách tải tệp đó về) và nêu rõ để trống ô tải tệp nghĩa là giữ nguyên tệp hiện tại — vì ô tệp là bắt buộc mà lại trống trơn nên người dùng dễ hiểu nhầm là chưa có tệp, tải đè thừa hoặc tưởng mất dữ liệu.
Căn cứ SRS (bản Docs-PM-HTPLDN/.../srs-v3.5/ ĐÃ cập nhật theo chốt BA): srs-fr-09-bieu-mau.md:384 — "**Given** CB NV mở form Sửa **When** form hiển thị **Then** hiển thị tệp đang đính kèm hiện có; để trống ô tải tệp = giữ nguyên tệp hiện tại". Ô File đính kèm vẫn Bắt buộc và hiện "khi tạo/sửa" (:666, SCR-VII-02 hàng 15) — riêng dòng SCR này BA còn phải bổ sung câu hiển thị tệp hiện có. (Bản input/srs-update-2026-5-5/ CHƯA có điều kiện mới này; ở bản đó chỉ có :372 phần chỉnh sửa và :652 ô File đính kèm.) Mức Minor — nâng Major nếu lưu mà không tải lại làm MẤT tệp.

── CÁCH VERIFY sau Dev fix ──
Precondition: cbnv_tw / Test@1234 tại https://18.143.165.120.nip.io/bieu-mau/danh-sach. Cần 1 biểu mẫu ĐÃ có tệp đính kèm — dùng BM-20260715-001; nếu không còn thì tạo mới ở /bieu-mau/them-moi với 1 tệp .docx hợp lệ và ghi lại tên + kích thước tệp đó.
1) Ở dòng biểu mẫu đó bấm "Sửa" để mở form Chỉnh sửa.
2) Xem vùng "File biểu mẫu": có hiện tên tệp đang đính kèm và cách tải tệp đó về không; có câu nói rõ ý nghĩa của việc để trống ô tải không.
3) KHÔNG chọn tệp mới — chỉ sửa Tên biểu mẫu (thêm hậu tố " - r1") rồi bấm lưu.
4) Mở lại chi tiết biểu mẫu, tải tệp đính kèm về và so tên + kích thước với tệp ban đầu.
✅ PASS khi đủ 3 điều: (i) bước 2 form Sửa hiện tên tệp đang đính kèm VÀ cho tải tệp đó về ngay trên form; (ii) form nêu rõ để trống ô tải = giữ tệp hiện tại, và ô File đính kèm không báo lỗi bắt buộc khi người dùng không tải lại; (iii) bước 3 lưu được, bước 4 tệp đính kèm vẫn đúng tệp cũ — tên và kích thước không đổi.
❌ FAIL nếu: form Sửa vẫn chỉ có ô tải trống "Kéo thả hoặc click để chọn file" (hiện trạng đo 20/07/2026: 0 phần tử tệp, không có liên kết tải); HOẶC bấm lưu bị chặn vì ô File đính kèm báo bắt buộc dù biểu mẫu đã có tệp; HOẶC sau khi lưu tệp đính kèm bị mất/rỗng — trường hợp này nâng thành lỗi chức năng và log riêng, không chỉ ghi Minor.
⚠️ Bẫy 1 — bước 3-4 là phần BẮT BUỘC phải chạy: hành vi "lưu mà không tải lại tệp" CHƯA từng kiểm được (ba-confirm/bieu-mau/ba-confirmation-needed-week-3-bieu-mau-tong-hop.md:772 ghi chưa test được do phiên hết hạn), nên chưa biết tệp cũ được giữ hay bị mất.
⚠️ Bẫy 2 — nếu bản ghi cũ có dấu hiệu dữ liệu tệp bị đóng băng từ trước khi dev sửa, hãy tạo 1 biểu mẫu MỚI qua luồng chuẩn rồi chạy lại bước 1-4 trên bản ghi mới để tránh kết luận sai.
Ảnh hiện trạng: reverify-audit/QLBMHD_13/QLBMHD_13-edit-form-no-file.png (form Sửa BM-20260715-001, vùng File biểu mẫu chỉ có ô tải trống). Nguồn quan sát: cùng phiếu, dòng :768-772 (20/07/2026, cbnv_tw).

## (B) Lỗi CÒN LẠI sau lượt Reopen gần nhất (nội dung đang nằm ở cột R của sheet)

- Đã kiểm tra trên một biểu mẫu MỚI tạo qua luồng chuẩn (mã BM-20260724-005, tệp đính kèm qa-edit-src.docx, 931 B).
- Phần đã đạt: form Chỉnh sửa nay CÓ hiện tên tệp đang đính kèm (qa-edit-src.docx).
- Phần đã đạt: sửa Tên biểu mẫu rồi bấm Lưu mà KHÔNG chọn lại tệp thì lưu thành công, ô File biểu mẫu không báo lỗi bắt buộc; sau khi lưu, tệp đính kèm vẫn nguyên tệp cũ (đúng tên, kích thước vẫn 931 B).
- Còn thiếu 1: không tải được tệp đang đính kèm ngay trên form Chỉnh sửa. Tên tệp chỉ là dòng chữ, không bấm vào được; nút duy nhất cạnh tên tệp là "Gỡ bỏ tập tin", không có nút hay liên kết tải tệp về.
- Còn thiếu 2: form chưa nói rõ để trống ô tải tệp nghĩa là giữ nguyên tệp hiện tại. Toàn bộ chữ ở vùng File biểu mẫu chỉ có "Kéo thả hoặc click để chọn file" và "Chỉ chấp nhận: .doc, .docx, .xls, .xlsx — Tối đa 20MB". Người dùng vẫn dễ hiểu nhầm là phải tải đè tệp mới.
- Kiểm tra ngày 25/07/2026, tài khoản CB Nghiệp vụ Trung ương.
