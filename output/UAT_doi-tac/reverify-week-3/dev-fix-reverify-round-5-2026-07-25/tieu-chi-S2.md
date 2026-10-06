# S2 — Biểu mẫu · Thư mục biểu mẫu · Nhập hàng loạt · SLA hồ sơ chi phí

- **Tài khoản của session:** cbnv_tw_01 / Test@1234 (chính) · cbnv_bn / Test@1234 (riêng row 119)
- **Số case:** 8 — rows [86, 89, 101, 106, 113, 119, 16, 19]
- **Mức seed:** NẶNG — cần 2 thư mục biểu mẫu, 2 tệp EICAR, 1 biểu mẫu có tệp đính kèm, 4 tệp import, hồ sơ chi phí phủ 4 mức SLA.

> **Nguồn tiêu chí:** khối `── CÁCH VERIFY ──` gốc do BA/dev viết, khôi phục từ giá trị `old=` trong `output/UAT_doi-tac/tools/sheet_verify_write.log`. Ô R trên sheet đã bị chế độ `--reopen` ghi đè sáng 25/07 nên KHÔNG còn tiêu chí. **Chấm PASS/FAIL đúng theo khối này, không tự nghĩ tiêu chí.**

> Bản snapshot nguyên văn P/Q/R trước round 5: `snapshot-P-Q-R-truoc-round5.md` cùng thư mục.


---

# Row 86 — QLTMBMHD_20

## TIÊU CHÍ GỐC — bắt buộc chấm theo

✅ Bug đúng (BA duyệt 24/07/2026) — thuộc nhóm Loại 2: BA cập nhật SRS trước, Dev làm theo SRS mới. Yêu cầu nghiệp vụ: với thao tác hàng loạt xong MỘT PHẦN, hệ thống phải cho người dùng biết bao nhiêu thư mục đã xử lý được / bao nhiêu bị bỏ qua kèm lý do, ở CẢ hộp xác nhận LẪN thông báo kết quả; đếm đúng số thành công; và không gọi thư mục không đủ điều kiện nghiệp vụ là "thất bại".
Căn cứ SRS (bản Docs-PM-HTPLDN/.../srs-v3.5/ ĐÃ cập nhật theo chốt BA): srs-fr-09-bieu-mau.md:135-138 (§Error Handling FR-VII-01) và :258-261 (§Error Handling FR-VII-03), nguyên văn: "Dùng cụm 'không đủ điều kiện', KHÔNG dùng 'thất bại'; đếm đúng số thư mục thành công (X/Y)" · "Xong một phần: 'Đã {hành động} {X}/{Y} thư mục. {Z} thư mục không đủ điều kiện ({lý do})'" · biến {lý do}: xóa → "còn biểu mẫu"; công khai → "rỗng, chưa có biểu mẫu"; ẩn → "chưa công khai". Chuỗi đơn lẻ giữ nguyên: :131 ERR-TM-02 "Thư mục chứa {N} biểu mẫu, không thể xóa"; :255-256 ERR-CK-01 / WRN-CK-01. (Bản input/srs-update-2026-5-5/ CHƯA có khối mẫu thông báo này — ở bản đó chỉ có ERR-TM-02 :131 và ERR-CK-01/WRN-CK-01 :250-251.) Mức Minor.

── CÁCH VERIFY sau Dev fix ──
Precondition: cbnv_tw / Test@1234 tại https://18.143.165.120.nip.io/bieu-mau/thu-muc. Cần sẵn 2 thư mục cùng đơn vị BTP·TW: A = trạng thái Nháp và RỖNG (cột Số biểu mẫu = 0) — nếu chưa có thì bấm [+ Thêm thư mục], đặt tên "QA-bulk-A-rong", Lĩnh vực Thuế; B = thư mục còn ≥ 1 biểu mẫu (dùng "Thư mục biểu mẫu seed", cột Số biểu mẫu ≥ 1). Cài bộ bắt thông báo tools/toast-capture.js (CẤM lọc trùng) TRƯỚC bước 1 vì thông báo nổi chỉ sống 3-5 giây.
1) Tích chọn cả A và B rồi bấm [Xóa hàng loạt].
2) Ghi nguyên văn câu trong hộp xác nhận, rồi bấm đồng ý.
3) Ghi nguyên văn thông báo kết quả sau khi xóa + số khung thông báo hiện lên.
4) Lặp bước 1-3 với [Công khai hàng loạt], chọn 1 thư mục có biểu mẫu + 1 thư mục rỗng.
✅ PASS khi đủ 3 điều: (i) CẢ hộp xác nhận LẪN thông báo kết quả đều nêu số đã xử lý được và số bị bỏ qua kèm lý do, theo mẫu SRS :135-138; (ii) không còn chữ "thất bại" gán cho thư mục bị bỏ qua vì lý do nghiệp vụ — dùng "không đủ điều kiện"; (iii) số đếm đúng: bước 3 xóa được 1 trong 2 → "1/2" kèm lý do "còn biểu mẫu" (KHÔNG phải "0/2"), bước 4 công khai được 1 trong 2 → "1/2" kèm lý do "rỗng, chưa có biểu mẫu".
❌ FAIL nếu: thông báo kết quả chỉ ghi số đã làm và bỏ hẳn phần bị bỏ qua (hiện trạng đo 20/07/2026: 1 khung, "Đã xóa 1 thư mục."); HOẶC còn chữ "thất bại" cho thư mục không đủ điều kiện; HOẶC đếm sai kiểu "0/2" trong khi thực tế đã xử lý được 1 thư mục.
⚠️ Bẫy 1 — phần "sau khi xóa vẫn còn dòng đã tích + thanh hành động hàng loạt" là bug RIÊNG (BUG-QLTMBMHD_19; SRS đã bổ sung postcondition ở :274). Đừng gộp vào PASS/FAIL của case này.
⚠️ Bẫy 2 — nếu thư mục B (còn biểu mẫu) bị xóa mất thì đó là lỗi nặng hơn hẳn phần chữ: log riêng, không tính PASS wording.
Ảnh hiện trạng: reverify-audit/QLTMBMHD_20/post-partial-delete-selection-not-cleared.png. Nguồn quan sát: ba-confirm/bieu-mau/ba-confirmation-needed-week-3-bieu-mau-tong-hop.md:169-171 (20/07/2026, cbnv_tw).

## Triệu chứng QA ghi nhận lượt trước (sáng 25/07) — CHỈ tham khảo, không phải tiêu chí

- Thao tác XÓA hàng loạt (1 thư mục rỗng + 1 thư mục còn biểu mẫu): đã đạt. Hộp xác nhận ghi "Xóa 1 thư mục? Hành động này không thể hoàn tác. Bạn có chắc không? (1 thư mục không đủ điều kiện (còn biểu mẫu) sẽ được bỏ qua)"; thông báo kết quả ghi "Đã xóa 1/2 thư mục. 1 thư mục không đủ điều kiện (còn biểu mẫu)." — nêu đủ số xử lý được, số bị bỏ qua và lý do.
- Thao tác CÔNG KHAI hàng loạt (1 thư mục có biểu mẫu + 1 thư mục rỗng): thông báo kết quả đã đạt ("Đã công khai 1/2 thư mục. 1 thư mục không đủ điều kiện (rỗng, chưa có biểu mẫu).") NHƯNG hộp xác nhận trước khi chạy chỉ hiện "Công khai 2 thư mục?" kèm câu chung "Đặt cờ công khai cho các thư mục đủ điều kiện (có biểu mẫu). Cổng PLQG sẽ tự cập nhật ở lượt kéo dữ liệu tiếp theo." — không cho người dùng biết sẽ bỏ qua mấy thư mục và vì sao.
- Hộp xác nhận của thao tác ẨN hàng loạt cũng vậy: "Ẩn 2 thư mục? Gỡ cờ công khai cho các thư mục đủ điều kiện." — thiếu số bị bỏ qua và lý do.
- Đề nghị đưa hộp xác nhận của Công khai và Ẩn về cùng cách viết như hộp xác nhận của Xóa (đã đúng).
- Không còn chữ "thất bại" ở bất kỳ thông báo nào — phần này đạt. Thư mục còn biểu mẫu không bị xóa nhầm — đúng.
- Kiểm tra ngày 25/07/2026, tài khoản CB Nghiệp vụ Trung ương.


---

# Row 89 — TKTMBMHD_04

## TIÊU CHÍ GỐC — bắt buộc chấm theo

✅ Bug đúng (BA duyệt 24/07/2026). Loại 2 — SRS đã được chốt sửa, Dev FE làm theo bản mới.
Yêu cầu nghiệp vụ: hai ô lọc dạng danh sách chọn trên màn Thư viện biểu mẫu > Thư mục (Lĩnh vực và Trạng thái) phải có sẵn một mục "Tất cả", và mục đó được chọn sẵn làm giá trị mặc định khi mở màn — thay vì để ô trắng chỉ có chữ gợi ý mờ. Người dùng phải đọc được trên ô rằng hiện đang không lọc, và xóa nhanh lựa chọn lẻ bằng cách chọn lại "Tất cả".
Căn cứ SRS: srs-v3.5/srs-fr-09-bieu-mau.md:619 (SCR-VII-01 #4 Lọc lĩnh vực — "Lĩnh vực PL (từ UC99). Mặc định: "Tất cả""), :620 (#5 Lọc trạng thái — "Tất cả / NHAP / CONG_KHAI / AN"), và §Inputs FR-VII-02 đã được sửa cho khớp: :168 (linh_vuc_id, cột Mặc định = "Tất cả (không lọc)"), :171 (trang_thai, Mặc định = "Tất cả (không lọc)"). Quy ước dùng chung srs-v3.5/srs-v3.5.md:580 (UI-11) cũng yêu cầu ô lọc chọn có một mục "Tất cả". (BA trích :163/:166 theo bản SRS trước khi cập nhật; số dòng hiện hành là :168/:171.) Mức Minor.

── CÁCH VERIFY sau Dev fix ──
Precondition: cbnv_tw / Test@1234 (CB Nghiệp vụ Trung ương) · https://18.143.165.120.nip.io/bieu-mau/thu-muc · mở URL sạch, KHÔNG kèm tham số tab / keyword / bộ lọc trên URL.
1) Mở URL trên, chưa bấm gì cả, đọc chữ đang hiển thị trong ô lọc "Lĩnh vực" và ô lọc "Trạng thái".
2) Mở dropdown ô "Trạng thái", đếm số mục và đọc mục đầu tiên.
3) Mở dropdown ô "Lĩnh vực", đọc mục đầu tiên (trước nhóm các lĩnh vực Thuế / Lao động / Đất đai...).
4) Ở ô "Trạng thái" chọn "Nháp" (danh sách co lại), rồi chọn lại "Tất cả".
✅ PASS khi ĐỦ 4 điều: (i) bước 1 cả hai ô hiển thị chữ "Tất cả" ở dạng giá trị đã chọn (chữ đậm như khi có lựa chọn), không phải chữ mờ gợi ý "Lĩnh vực" / "Trạng thái"; (ii) bước 2 dropdown Trạng thái có đúng 4 mục — Tất cả, Nháp, Đã công khai, Đã ẩn — và "Tất cả" đứng đầu; (iii) bước 3 dropdown Lĩnh vực có mục "Tất cả" đứng trước toàn bộ lĩnh vực; (iv) bước 4 chọn lại "Tất cả" thì danh sách trở về đủ số thư mục như lúc mới mở màn.
❌ FAIL nếu: ô lọc chỉ hiện chữ mờ gợi ý khi mới mở màn; HOẶC dropdown không có mục "Tất cả"; HOẶC có mục "Tất cả" nhưng khi mở màn nó không được chọn sẵn.
⚠️ Đừng lấy "danh sách vẫn ra đủ thư mục" làm bằng chứng PASS — để ô trắng cũng ra đủ thư mục. Case này chấm giá trị hiển thị trên ô lọc và sự tồn tại của mục "Tất cả" trong dropdown.
⚠️ Không nhầm hai ô lọc này với dãy tab phân loại phía trên bảng (Tất cả / Đã công khai / Nháp / Đã ẩn, srs-v3.5/srs-fr-09-bieu-mau.md:623). Tab là control khác và thuộc case TKTMBMHD_07.

## Triệu chứng QA ghi nhận lượt trước (sáng 25/07) — CHỈ tham khảo, không phải tiêu chí

- Mở màn Thư viện biểu mẫu > Thư mục lần đầu: hai ô lọc "Lĩnh vực" và "Trạng thái" đã đổi chữ hiển thị thành "Tất cả", nhưng vẫn là chữ gợi ý mờ (xám nhạt) chứ chưa phải giá trị đang được chọn. Khi người dùng thực sự chọn một mục thì chữ mới đậm lên — nên nhìn vào ô lọc lúc mới mở màn vẫn không biết đang để "Tất cả" hay đang bỏ trống.
- Mở danh sách chọn của ô "Lĩnh vực": chỉ có 10 lĩnh vực (Thuế, Lao động, Đất đai, Dân sự, Thương mại, Hình sự, Hành chính, Sở hữu trí tuệ, Doanh nghiệp, Đầu tư), KHÔNG có mục "Tất cả".
- Ô "Trạng thái" đã có đủ 4 mục (Tất cả / Nháp / Đã công khai / Đã ẩn) và "Tất cả" đứng đầu — phần này đạt; nhưng lúc mới mở màn mục "Tất cả" không được đánh dấu là đang chọn.
- Chọn Trạng thái = Nháp rồi chọn lại "Tất cả" thì danh sách trở về đủ 4 thư mục — phần này đạt.
- Kiểm tra ngày 25/07/2026, tài khoản CB Nghiệp vụ Trung ương.


---

# Row 101 — QLBMHD_08

## TIÊU CHÍ GỐC — bắt buộc chấm theo

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

## Triệu chứng QA ghi nhận lượt trước (sáng 25/07) — CHỈ tham khảo, không phải tiêu chí

- Phần chặn và chữ thông báo: ĐÃ ĐẠT trên giao diện.
- Tệp .docx đúng cấu trúc Office có chèn chuỗi thử diệt virus (EICAR) bên trong nội dung: bị TỪ CHỐI, yêu cầu tải lên trả mã 400 với mã lỗi ERR-BM-07, thông báo hiện lên đúng chữ "Tệp chứa mã độc, không thể lưu trữ", dòng tệp chuyển sang trạng thái lỗi và tệp không được đính kèm vào biểu mẫu.
- Tệp rác đổi đuôi .docx cũng bị từ chối với đúng thông báo mã độc nêu trên (trước đây bị chặn ở bước kiểm định dạng).
- Kiểm tra lại danh sách biểu mẫu: không sinh ra bản ghi nào từ các lần thử trên.
- Việc bộ quét đọc được nội dung BÊN TRONG tệp nén Office đã được chứng minh qua kết quả trên.
- Còn 1 việc chưa thể xác nhận từ phía kiểm thử: bộ quét mã độc chạy TRƯỚC khi ghi tệp vào kho lưu trữ (không quan sát được từ giao diện). Theo hướng dẫn kiểm thử của case, cần Dev/An toàn thông tin xác nhận bằng văn bản điểm này rồi mới đóng case. Rất mong đội phát triển bổ sung xác nhận, sau đó chúng tôi sẽ chuyển sang Pass ngay.
- Kiểm tra ngày 25/07/2026, tài khoản CB Nghiệp vụ Trung ương.


---

# Row 106 — QLBMHD_13

## TIÊU CHÍ GỐC — bắt buộc chấm theo

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

## Triệu chứng QA ghi nhận lượt trước (sáng 25/07) — CHỈ tham khảo, không phải tiêu chí

- Đã kiểm tra trên một biểu mẫu MỚI tạo qua luồng chuẩn (mã BM-20260724-005, tệp đính kèm qa-edit-src.docx, 931 B).
- Phần đã đạt: form Chỉnh sửa nay CÓ hiện tên tệp đang đính kèm (qa-edit-src.docx).
- Phần đã đạt: sửa Tên biểu mẫu rồi bấm Lưu mà KHÔNG chọn lại tệp thì lưu thành công, ô File biểu mẫu không báo lỗi bắt buộc; sau khi lưu, tệp đính kèm vẫn nguyên tệp cũ (đúng tên, kích thước vẫn 931 B).
- Còn thiếu 1: không tải được tệp đang đính kèm ngay trên form Chỉnh sửa. Tên tệp chỉ là dòng chữ, không bấm vào được; nút duy nhất cạnh tên tệp là "Gỡ bỏ tập tin", không có nút hay liên kết tải tệp về.
- Còn thiếu 2: form chưa nói rõ để trống ô tải tệp nghĩa là giữ nguyên tệp hiện tại. Toàn bộ chữ ở vùng File biểu mẫu chỉ có "Kéo thả hoặc click để chọn file" và "Chỉ chấp nhận: .doc, .docx, .xls, .xlsx — Tối đa 20MB". Người dùng vẫn dễ hiểu nhầm là phải tải đè tệp mới.
- Kiểm tra ngày 25/07/2026, tài khoản CB Nghiệp vụ Trung ương.


---

# Row 113 — TKBMHD_03

## TIÊU CHÍ GỐC — bắt buộc chấm theo

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

## Triệu chứng QA ghi nhận lượt trước (sáng 25/07) — CHỈ tham khảo, không phải tiêu chí

- Ý (b) — bỏ PDF khỏi ô lọc Định dạng: ĐÃ ĐẠT. Danh sách chọn của ô Định dạng chỉ còn đúng 5 mục: Tất cả, DOC, DOCX, XLS, XLSX — không còn mục PDF.
- Lọc chạy đúng: chọn DOCX ra 9 biểu mẫu, chọn XLSX ra 2 biểu mẫu, chọn lại Tất cả trở về đúng 11 biểu mẫu như lúc mới mở màn.
- Ý (a) — 4 ô lọc mặc định Tất cả: CHƯA ĐẠT. Khi mới mở màn Danh sách biểu mẫu (chưa bấm gì), cả 4 ô Thư mục, Lĩnh vực, Loại hình, Định dạng đều chỉ hiện chữ Tất cả dưới dạng chữ mờ gợi ý (màu xám nhạt), không phải giá trị đang được chọn: ô còn rỗng, và khi mở danh sách chọn thì mục Tất cả không được đánh dấu là đang chọn.
- Đối chiếu cho thấy đây không phải hạn chế hiển thị: sau khi người dùng tự tay chọn mục Tất cả thì chữ Tất cả chuyển sang màu đậm như một giá trị đã chọn, và mục Tất cả trong danh sách được đánh dấu. Nghĩa là trạng thái lúc mới mở màn vẫn là ô trống.
- Theo tiêu chí, hai ý (a) và (b) phải cùng đạt mới tính đạt, nên case này còn mở vì ý (a).
- Kiểm tra ngày 25/07/2026, tài khoản CB Nghiệp vụ Trung ương.


---

# Row 119 — IBMHD_07

## TIÊU CHÍ GỐC — bắt buộc chấm theo

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

## Triệu chứng QA ghi nhận lượt trước (sáng 25/07) — CHỈ tham khảo, không phải tiêu chí

- Kịch bản: thư mục đích QA-IMPORT-KQ mới tạo (trống). Chọn 4 tệp trong 1 lượt: 2 tệp .docx hợp lệ, 1 tệp qa-loi.txt sai định dạng, 1 tệp qa-hong.docx đúng đuôi nhưng nội dung hỏng.
- Phần đã đạt: 2 tệp hợp lệ vẫn được nhập bình thường, không bị chặn cả lô — mở danh sách lọc theo thư mục QA-IMPORT-KQ đếm đúng 2 biểu mẫu.
- Còn lỗi 1: màn kết quả cuối ghi "Nhập biểu mẫu hoàn tất: 2 thành công / 0 lỗi" — báo 0 lỗi trong khi thực tế có 2 tệp bị loại: qa-loi.txt bị loại ngay lúc chọn tệp, qa-hong.docx bị loại lúc tải lên (có thông báo "Tệp không hợp lệ hoặc bị hỏng" và dòng đếm ở bước chọn tệp ghi "Đã tải lên thành công: 2/3 · Có file lỗi"). Người dùng nhìn màn kết quả vẫn không biết mình mất 2 tệp nào.
- Còn lỗi 2: màn kết quả không có lối xem chi tiết tệp lỗi. Toàn màn chỉ có dòng kết quả và 2 nút "Quay lại danh sách" / "Nhập tiếp"; không có bảng liệt kê tên tệp lỗi kèm lý do.
- Ghi nhận thêm: ở bước Kiểm tra, bảng kiểm tra có liệt kê qa-loi.txt kèm lý do, nhưng qa-hong.docx không có dòng nào trong bảng đó.
- Kiểm tra ngày 25/07/2026, tài khoản CB Nghiệp vụ Bộ ngành.


---

# Row 16 — QLHSDNHTCP_03

## TIÊU CHÍ GỐC — bắt buộc chấm theo

✅ Bug đúng (BA 24/07/2026) — Loại 2: BA chốt chuẩn hóa cảnh báo thời hạn và ĐÃ cập nhật đặc tả, Dev sửa hiển thị theo đặc tả mới. Cột SLA của danh sách hồ sơ chi trả phải hiển thị 4 mức cảnh báo theo BR-SLA-02 — Bình thường (còn > 50% thời lượng) / Sắp hết hạn (còn < 50%) / Quá hạn (> 100%) / Quá hạn nghiêm trọng (> 200%) — kèm số ngày còn lại; app hiện chỉ đếm ngày + tô màu, không thuộc bộ nhãn nào. Toàn hệ thống dùng chung một mô hình BR-SLA-02, bỏ mô hình 70/85 riêng của Chi trả. Căn cứ: srs-fr-06-chi-tra.md:1058 (cột #16 SLA = 4 mức theo BR-SLA-02), :1311 (trường mức cảnh báo với 4 giá trị + ngưỡng 50/100/200, BA điều chỉnh 24/07/2026), :1514-1523 (bảng ngưỡng + quy tắc ưu tiên mức). Tên cột "SLA" của app đã khớp đặc tả, không đổi. Mức Minor.

── CÁCH VERIFY sau Dev fix ──
Precondition: cbnv_tw / Test@1234, mở danh sách "Hồ sơ Đề nghị Hỗ trợ Chi phí". Cần dữ liệu phủ đủ mức: ít nhất 1 hồ sơ còn > 50% thời lượng, 1 hồ sơ còn < 50%, 1 hồ sơ đã quá hạn, 1 hồ sơ trễ vượt 200% (căn theo ngày nộp của hồ sơ).
1) Đọc cột SLA của từng dòng trong danh sách.
2) Với mỗi dòng, lấy ngày nộp + thời hạn cấu hình (mặc định 10 ngày làm việc) tính ra hạn, đối chiếu mức đang hiển thị.
3) Lọc/duyệt qua các tab trạng thái để chắc chắn cả 4 mức đều xuất hiện ít nhất 1 lần.
✅ PASS khi: cột SLA hiện đúng 1 trong 4 nhãn "Bình thường / Sắp hết hạn / Quá hạn / Quá hạn nghiêm trọng" cùng số ngày còn lại hoặc quá hạn, và nhãn của từng dòng khớp ngưỡng 50% / 100% / 200% tính từ dữ liệu thực.
❌ FAIL nếu: cột chỉ còn đếm ngày và màu, không có nhãn mức; hoặc dùng bộ nhãn cũ (warning / urgent / critical / overdue, ngưỡng 70% - 85%); hoặc nhãn sai ngưỡng (ví dụ còn 60% thời lượng mà báo Sắp hết hạn).
⚠️ Giữ số ngày bên cạnh nhãn là ĐÚNG yêu cầu — đừng FAIL vì vẫn thấy chuỗi "Quá hạn 58 ngày LV", miễn có kèm nhãn mức. Thời hạn đếm từ NGÀY NỘP chứ không phải ngày cán bộ tiếp nhận (srs-fr-06-chi-tra.md:119) — đối chiếu sai mốc sẽ ra kết luận sai.
Ảnh lỗi cũ: QLHSDNHTCP_03.jpg (ảnh UAT đối tác — cột SLA chỉ hiện "Quá hạn N ngày LV" + tô màu, không có nhãn mức).

## Triệu chứng QA ghi nhận lượt trước (sáng 25/07) — CHỈ tham khảo, không phải tiêu chí

- Cột SLA đã có nhãn mức kèm số ngày, nhưng mức gắn cho nhiều hồ sơ vẫn sai.
- Hồ sơ còn hạn bị báo quá hạn: CT-SEED-101 nộp 15/07, hạn xử lý 10 ngày làm việc là 29/07 nên vẫn còn hạn, đúng ra phải là "Sắp hết hạn", nhưng danh sách hiện "Quá hạn · 0 ngày LV".
- Hồ sơ mới trễ ít đã bị đẩy lên mức nặng nhất: CT-SEED-105 (nộp 03/07, hạn 17/07) trễ 5 ngày làm việc và CT-SEED-106 (nộp 01/07, hạn 15/07) trễ 7 ngày làm việc, nhưng cả hai đều hiện "Quá hạn nghiêm trọng"; mức này chỉ dùng khi trễ vượt quá 2 lần thời hạn.
- Hồ sơ đã kết thúc vẫn tiếp tục bị đếm quá hạn: CT-SEED-108 thanh toán xong ngày 24/06 trong khi hạn là 29/06, tức xử lý đúng hạn, vẫn hiện "Quá hạn nghiêm trọng · 21 ngày LV"; CT-SEED-109 từ chối ngày 27/06 (hạn 03/07) và CT-SEED-110 đã hủy cũng bị gắn "Quá hạn nghiêm trọng".
- Nguyên nhân chung: hạn xử lý đang tính 10 ngày liên tục kể từ ngày nộp, không trừ thứ Bảy, Chủ nhật và ngày lễ, nên tỷ lệ thời hạn đã dùng bị đội lên và nhảy mức sớm (ví dụ CT-SEED-103 chú thích 188% trong khi tính đúng chỉ 150%).
- Duyệt hết 10 hồ sơ của cả 5 thẻ trạng thái chỉ thấy 2 mức "Quá hạn" và "Quá hạn nghiêm trọng"; không hồ sơ nào hiện "Bình thường" hoặc "Sắp hết hạn".


---

# Row 19 — QLHSDNHTCP_10

## TIÊU CHÍ GỐC — bắt buộc chấm theo

✅ Bug đúng (BA 24/07/2026) — Loại 2, cùng gốc với QLHSDNHTCP_03 nhưng ở MÀN CHI TIẾT. BA chốt chuẩn hóa và đã cập nhật đặc tả: trường SLA trên thanh thông tin tổng quan của màn Chi tiết hồ sơ chi trả phải hiển thị 4 mức cảnh báo BR-SLA-02 — Bình thường (còn > 50%) / Sắp hết hạn (còn < 50%) / Quá hạn (> 100%) / Quá hạn nghiêm trọng (> 200%) — kèm số ngày còn lại, thống nhất với màn danh sách để một hồ sơ không hiện hai kiểu cảnh báo ở hai màn. Căn cứ: srs-fr-06-chi-tra.md:1102 (khối thông tin đầu trang, trường SLA = 4 mức theo BR-SLA-02), :1311 (4 giá trị mức cảnh báo + ngưỡng 50/100/200, BA điều chỉnh 24/07/2026), :1514-1523 (bảng ngưỡng). Mức Minor.

── CÁCH VERIFY sau Dev fix ──
Precondition: cbnv_tw / Test@1234. Chọn sẵn 2 hồ sơ chi trả ở 2 mức khác nhau (1 hồ sơ chưa quá hạn, 1 hồ sơ đã quá hạn), ghi lại mã của cả hai.
1) Mở màn Chi tiết hồ sơ chưa quá hạn, đọc trường SLA trên thanh thông tin tổng quan đầu màn.
2) Mở màn Chi tiết hồ sơ đã quá hạn, đọc lại trường SLA.
3) Quay ra danh sách, tìm đúng 2 hồ sơ đó và so nhãn SLA ở danh sách với nhãn vừa đọc ở màn chi tiết.
✅ PASS khi: trường SLA ở thanh tổng quan hiện nhãn mức BR-SLA-02 kèm số ngày; nhãn khớp ngưỡng tính từ dữ liệu thực của từng hồ sơ; và cùng một hồ sơ cho CÙNG một nhãn ở cả màn danh sách lẫn màn chi tiết.
❌ FAIL nếu: màn chi tiết vẫn chỉ đếm ngày + tô màu không có nhãn mức; hoặc cùng một hồ sơ ra hai nhãn khác nhau ở hai màn; hoặc dùng bộ nhãn cũ 70% - 85%.
⚠️ Nhãn của ô đang là "SLA" — đúng đặc tả, KHÔNG yêu cầu đổi thành "Hạn xử lý", đừng FAIL vì tên nhãn. Trường hợp này chấm chính THANH TỔNG QUAN màn Chi tiết (QLHSDNHTCP_03 mới là màn danh sách) — chụp lại màn danh sách không đủ để kết luận.
Ảnh lỗi cũ: QLHSDNHTCP_10.jpg (ảnh UAT đối tác — thanh tổng quan màn Chi tiết, nhãn SLA = "Quá hạn 58 ngày LV" không có mức).

## Triệu chứng QA ghi nhận lượt trước (sáng 25/07) — CHỈ tham khảo, không phải tiêu chí

- Hồ sơ chưa quá hạn thì thanh thông tin tổng quan không có trường SLA. Mở CT-SEED-101 (Chờ tiếp nhận), thanh tổng quan chỉ có Mã HS, Quy mô DN và Trạng thái, không có mục cảnh báo thời hạn nào, trong khi ngoài danh sách hồ sơ này vẫn hiện nhãn SLA.
- Hồ sơ đã tiếp nhận thì trường SLA có hiện nhãn kèm số ngày, nhưng mức gắn sai giống lỗi ngoài danh sách: CT-SEED-108 thanh toán xong ngày 24/06 trong khi hạn là 29/06, tức xử lý đúng hạn, mà màn chi tiết vẫn hiện "Quá hạn nghiêm trọng · 21 ngày LV".
- Hai màn còn tính lệch nhau: cùng hồ sơ CT-SEED-107, chú thích tỷ lệ thời hạn đã dùng ngoài danh sách là 350% nhưng vào màn chi tiết lại là 400%, do màn chi tiết đếm từ ngày cán bộ tiếp nhận thay vì ngày doanh nghiệp nộp.
