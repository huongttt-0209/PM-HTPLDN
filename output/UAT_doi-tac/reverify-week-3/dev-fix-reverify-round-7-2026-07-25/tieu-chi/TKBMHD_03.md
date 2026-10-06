# Tiêu chí chấm — TKBMHD_03 (dòng 113)

> Round 7 · 2026-07-25. **CẤM tự đặt tiêu chí khác.** Chấm theo đúng 2 khối dưới:
> (A) bar gốc dev đặt ở round trước, (B) các lỗi CÒN LẠI mình đã ghi cho đối tác ở lượt Reopen gần nhất.
> PASS = (A) đủ điều kiện PASS **và** (B) không còn gạch đầu dòng nào tái hiện.

## Case gốc (đối tác)
- **Mô tả:** Kiểm tra Điều kiện tìm kiếm / bộ lọc
- **Điều kiện:** 1. Đăng nhập tài khoản
- **Các bước:** 1. Chọn menu "Biểu mẫu" -> "Danh sách biểu mẫu"
- **KQ mong đợi:** - Hệ thống hiển thị các trường thông tin giống với thiết kế
- Dữ liệu hiển thị đúng định dạng và trường thông tin
- Dữ liệu hiển thị không bị tràn/đè lên nhau, đồng nhất ngôn ngữ hiển thị
- **KQ thực tế (đối tác báo):** - Các trường thông tin có kiểu dữ liệu Danh sách chọn giá trị mặc định không phải là Tất cả
- Trường thông tin Định dạng thừa giá trị "PDF"

## (A) Bar gốc của DEV — bộ "CÁCH VERIFY" đã chốt

✅ Bug đúng (BA duyệt 24/07/2026) — case này có 2 ý, cả 2 đều phải sửa, verdict Open.

Ý (a) — bộ lọc màn Danh sách biểu mẫu phải mặc định "Tất cả" (Loại 2, SRS đã chốt sửa): bốn ô lọc dạng danh sách chọn (Thư mục, Lĩnh vực, Loại hình, Định dạng) phải có sẵn mục "Tất cả" và mục đó được chọn sẵn khi mở màn, thay vì để ô trắng chỉ có chữ gợi ý mờ. Căn cứ SRS: srs-v3.5/srs-fr-09-bieu-mau.md:654 (SCR-VII-02 #3 — "Lĩnh vực PL / Loại hình / Thư mục / Định dạng (doc / docx / xls / xlsx). Mỗi bộ lọc mặc định "Tất cả (không lọc)"") và §Inputs FR-VII-05 đã được sửa cho khớp: :412 linh_vuc_id, :413 loai_hinh, :414 thu_muc_id, :415 dinh_dang — cả 4 dòng cột Mặc định = "Tất cả (không lọc)". (BA trích :400 và :640 theo bản SRS trước khi cập nhật.) Đồng bộ với TKTMBMHD_04 của màn Thư mục. Mức Minor.

Ý (b) — bỏ giá trị "PDF" khỏi ô lọc Định dạng (Loại 1, phần mềm sai): ô lọc này lọc theo định dạng của tệp biểu mẫu chính, mà tệp biểu mẫu chính chỉ được nhận doc/docx/xls/xlsx nên không biểu mẫu nào có định dạng PDF — để mục PDF trong danh sách là một lựa chọn chết, chọn vào luôn ra rỗng và làm người dùng tưởng hệ thống mất dữ liệu. Căn cứ SRS: :415 (§Inputs FR-VII-05, dinh_dang — ràng buộc "CHECK IN ('doc','docx','xls','xlsx')"), :654 (SCR-VII-02 #3 ghi rõ danh sách định dạng của bộ lọc = doc / docx / xls / xlsx), :50 (phạm vi Nhóm VII — "File chấp nhận doc/docx/xls/xlsx (max 20MB)"), :666 (SCR-VII-02 #15 form File đính kèm — "Bắt buộc. doc/docx/xls/xlsx. Max 20MB. Quét virus"). PDF chỉ hợp lệ ở ô khác là File đính kèm công khai — :670 (SCR-VII-02 #19 — "Nhiều file PDF/DOC/DOCX/XLS/XLSX, max 20MB/file"). Mức Minor.

── CÁCH VERIFY sau Dev fix ──
Precondition: cbnv_tw / Test@1234 (CB Nghiệp vụ Trung ương) · https://18.143.165.120.nip.io/bieu-mau/danh-sach · mở URL sạch, không kèm tham số lọc; cần ≥1 biểu mẫu .docx và ≥1 biểu mẫu .xlsx đang tồn tại trong phạm vi đơn vị để bước 4 so sánh được số lượng.
1) Mở URL trên, chưa bấm gì, đọc chữ đang hiển thị trong cả 4 ô lọc: Thư mục, Lĩnh vực, Loại hình, Định dạng. Ghi lại tổng số biểu mẫu đang hiển thị.
2) Mở dropdown ô "Định dạng", liệt kê ĐẦY ĐỦ mọi mục trong đó.
3) Chọn Định dạng = DOCX → đọc số biểu mẫu; rồi chọn lại Định dạng = "Tất cả".
4) So số biểu mẫu sau khi chọn lại "Tất cả" với tổng đã ghi ở bước 1.
✅ PASS khi ĐỦ 4 điều: (i) bước 1 cả 4 ô hiển thị chữ "Tất cả" ở dạng giá trị đã chọn, không phải chữ mờ gợi ý; (ii) bước 2 dropdown Định dạng có đúng 5 mục — Tất cả, DOC, DOCX, XLS, XLSX — và KHÔNG có mục PDF; (iii) bước 3 chọn DOCX ra đúng nhóm biểu mẫu .docx; (iv) bước 4 chọn lại "Tất cả" thì số biểu mẫu trở về đúng tổng của bước 1.
❌ FAIL nếu: dropdown Định dạng còn mục PDF (kể cả khi chọn vào ra 0 kết quả); HOẶC bất kỳ ô nào trong 4 ô khi mới mở màn chỉ hiện chữ mờ gợi ý, không có mục "Tất cả" được chọn sẵn.
⚠️ Chỉ gỡ PDF khỏi ô LỌC Định dạng của màn danh sách biểu mẫu. Ô "File đính kèm công khai" trong form biểu mẫu VẪN phải nhận tệp PDF theo :670 — gỡ PDF ở đó là làm phát sinh lỗi mới.
⚠️ Đừng chấm PASS chỉ vì "chọn PDF ra 0 kết quả". Yêu cầu là mục PDF không còn xuất hiện trong danh sách chọn.
⚠️ Hai ý (a) và (b) phải cùng đạt mới PASS. Bỏ được PDF mà 4 ô lọc vẫn để trắng thì case này vẫn FAIL.

## (B) Lỗi CÒN LẠI sau lượt Reopen gần nhất (nội dung đang nằm ở cột R của sheet)

- Ý (b) — bỏ PDF khỏi ô lọc Định dạng: ĐÃ ĐẠT. Danh sách chọn của ô Định dạng chỉ còn đúng 5 mục: Tất cả, DOC, DOCX, XLS, XLSX — không còn mục PDF.
- Lọc chạy đúng: chọn DOCX ra 9 biểu mẫu, chọn XLSX ra 2 biểu mẫu, chọn lại Tất cả trở về đúng 11 biểu mẫu như lúc mới mở màn.
- Ý (a) — 4 ô lọc mặc định Tất cả: CHƯA ĐẠT. Khi mới mở màn Danh sách biểu mẫu (chưa bấm gì), cả 4 ô Thư mục, Lĩnh vực, Loại hình, Định dạng đều chỉ hiện chữ Tất cả dưới dạng chữ mờ gợi ý (màu xám nhạt), không phải giá trị đang được chọn: ô còn rỗng, và khi mở danh sách chọn thì mục Tất cả không được đánh dấu là đang chọn.
- Đối chiếu cho thấy đây không phải hạn chế hiển thị: sau khi người dùng tự tay chọn mục Tất cả thì chữ Tất cả chuyển sang màu đậm như một giá trị đã chọn, và mục Tất cả trong danh sách được đánh dấu. Nghĩa là trạng thái lúc mới mở màn vẫn là ô trống.
- Theo tiêu chí, hai ý (a) và (b) phải cùng đạt mới tính đạt, nên case này còn mở vì ý (a).
- Kiểm tra ngày 25/07/2026, tài khoản CB Nghiệp vụ Trung ương.
