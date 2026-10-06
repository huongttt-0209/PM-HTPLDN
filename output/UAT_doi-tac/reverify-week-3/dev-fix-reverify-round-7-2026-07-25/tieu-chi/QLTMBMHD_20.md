# Tiêu chí chấm — QLTMBMHD_20 (dòng 86)

> Round 7 · 2026-07-25. **CẤM tự đặt tiêu chí khác.** Chấm theo đúng 2 khối dưới:
> (A) bar gốc dev đặt ở round trước, (B) các lỗi CÒN LẠI mình đã ghi cho đối tác ở lượt Reopen gần nhất.
> PASS = (A) đủ điều kiện PASS **và** (B) không còn gạch đầu dòng nào tái hiện.

## Case gốc (đối tác)
- **Mô tả:** Xóa hàng loạt một phần thành công
- **Điều kiện:** 1. Đăng nhập tài khoản 
2. Thư mục còn biểu mẫu
- **Các bước:** 1. Chọn menu "Biểu mẫu" -> "Thư mục biểu mẫu"
2. Chọn ít nhất một thư mục bằng ô chọn ở đầu dòng
3. Nhấn Xóa hàng loạt và Xác nhận
- **KQ mong đợi:** Hệ thống hiển thị thông điệp "Đã xóa {X} thư mục. {Y} thư mục không đủ điều kiện xóa (còn biểu mẫu bên trong)".
- **KQ thực tế (đối tác báo):** - Thông báo không giống với thiết kế
- Sau khi xóa thành công hệ thống vẫn hiển thị dòng thông báo đã tích chọn và các nút chức năng

## (A) Bar gốc của DEV — bộ "CÁCH VERIFY" đã chốt

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

## (B) Lỗi CÒN LẠI sau lượt Reopen gần nhất (nội dung đang nằm ở cột R của sheet)

- Thao tác XÓA hàng loạt (1 thư mục rỗng + 1 thư mục còn biểu mẫu): đã đạt. Hộp xác nhận ghi "Xóa 1 thư mục? Hành động này không thể hoàn tác. Bạn có chắc không? (1 thư mục không đủ điều kiện (còn biểu mẫu) sẽ được bỏ qua)"; thông báo kết quả ghi "Đã xóa 1/2 thư mục. 1 thư mục không đủ điều kiện (còn biểu mẫu)." — nêu đủ số xử lý được, số bị bỏ qua và lý do.
- Thao tác CÔNG KHAI hàng loạt (1 thư mục có biểu mẫu + 1 thư mục rỗng): thông báo kết quả đã đạt ("Đã công khai 1/2 thư mục. 1 thư mục không đủ điều kiện (rỗng, chưa có biểu mẫu).") NHƯNG hộp xác nhận trước khi chạy chỉ hiện "Công khai 2 thư mục?" kèm câu chung "Đặt cờ công khai cho các thư mục đủ điều kiện (có biểu mẫu). Cổng PLQG sẽ tự cập nhật ở lượt kéo dữ liệu tiếp theo." — không cho người dùng biết sẽ bỏ qua mấy thư mục và vì sao.
- Hộp xác nhận của thao tác ẨN hàng loạt cũng vậy: "Ẩn 2 thư mục? Gỡ cờ công khai cho các thư mục đủ điều kiện." — thiếu số bị bỏ qua và lý do.
- Đề nghị đưa hộp xác nhận của Công khai và Ẩn về cùng cách viết như hộp xác nhận của Xóa (đã đúng).
- Không còn chữ "thất bại" ở bất kỳ thông báo nào — phần này đạt. Thư mục còn biểu mẫu không bị xóa nhầm — đúng.
- Kiểm tra ngày 25/07/2026, tài khoản CB Nghiệp vụ Trung ương.
