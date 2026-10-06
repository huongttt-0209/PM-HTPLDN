✅ Vẫn còn lỗi — Reopen (lỗi ở bước cuối: bấm xác nhận nạp).

Đo lại trên môi trường https://18.143.165.120.nip.io, bản dựng V1.0.9 (bó mã index-DsMHK7Dp.js), lúc 02:08–02:20 ngày 07/08/2026. Tài khoản Cán bộ Nghiệp vụ Trung ương cbnv_tw_02 (CB_NV_TW, đơn vị BTP · TW).

Tiền đề: khóa KH-QAW7-HOINGHI (Hội nghị đối thoại DN 2026) ở trạng thái Đang diễn ra — đúng điều kiện SRS srs-fr-03-dao-tao.md:536 (PRE-03: điểm danh chỉ mở khi khóa Đang diễn ra); khóa có 4 buổi học; đo trên Buổi 4 (11/05/2026, 14:00–16:00); 4 học viên đã duyệt thuộc khóa. Tệp nạp là tệp lấy từ chính nút "Tải mẫu điểm danh" của hệ thống, chỉ điền thêm cột trạng thái, gồm 5 dòng: 3 dòng hợp lệ + 2 dòng cố ý sai (1 dòng dùng học viên của khóa khác, 1 dòng ghi trạng thái "XYZ").

ĐÃ ĐẠT — 2 phần:
1) Cơ chế "Tải mẫu → điền → tải lên" đã có đúng đặc tả (srs-fr-03-dao-tao.md:571–583, :651, :1919). Nút "Tải mẫu điểm danh" tắt khi chưa chọn buổi, bật sau khi chọn buổi. Tệp mẫu tải về mở được, đúng 6 cột hoc_vien_id · Họ tên · Email · Đơn vị · Trạng thái điểm danh · Ghi chú; cột hoc_vien_id đã điền sẵn đủ 4 học viên, cột trạng thái để trống; định danh buổi học nằm ở vùng metadata của tệp chứ không phải cột từng dòng. Trạng thái điểm danh nay là 3 giá trị Có mặt / Vắng có phép / Vắng không phép, không còn dạng nhị phân 1/0 như lần ghi nhận trước.
2) Bản xem trước đã có đúng đặc tả (srs-fr-03-dao-tao.md:593). Sau khi bấm "Kiểm tra tệp", hệ thống hiện khối "Kết quả kiểm tra - chưa nhập dữ liệu": Tổng dòng 5 · Hợp lệ 3 · Bỏ qua 0 · Lỗi 2, tách 2 thẻ "Hợp lệ (3)" và "Lỗi/Bỏ qua (2)"; mỗi dòng lỗi ghi rõ số dòng kèm lý do riêng — dòng 5: ERR-KQ-03 (học viên không thuộc khóa), dòng 6: ERR-KQ-04 (giá trị điểm danh không hợp lệ: XYZ). Đối chiếu với dữ liệu máy chủ trả về cho chính lần kiểm tệp: total 5, success 3, errors 2 — khớp hoàn toàn với số trên màn.

CHƯA ĐẠT — bước xác nhận nạp:
Bấm nút "Xác nhận import (3 dòng hợp lệ)" thì hệ thống chỉ báo "Lỗi hệ thống, vui lòng thử lại sau." Máy chủ trả lỗi ở yêu cầu xác nhận nạp (mã ERR-SYS-00-00-01, requestId 6415303f-0248-42b0-b314-defb9492ce64, lúc 02:18:52 ngày 07/08/2026). Kiểm lại bảng điểm danh của đúng Buổi 4 sau đó: cả 4 học viên vẫn chưa có trạng thái điểm danh, không nút chọn nào được tích — tức 0/3 dòng hợp lệ được ghi.

Điều này trái 2 điểm trong đặc tả: srs-fr-03-dao-tao.md:594 quy định khi người dùng xác nhận thì hệ thống merge kết quả, chỉ merge dòng hợp lệ và bỏ qua dòng lỗi (đáng lẽ phải ghi 3 dòng); srs-fr-03-dao-tao.md:595 quy định hệ thống trả về báo cáo import (hiện không có báo cáo nào, chỉ có thông báo lỗi hệ thống chung). Tiêu chí nghiệm thu srs-fr-03-dao-tao.md:652 cũng yêu cầu import tệp mẫu đúng buổi thì phải merge được dòng hợp lệ.

Ghi chú thêm: nhật ký trình duyệt không có lỗi phía giao diện, chỉ có đúng một lỗi 500 từ máy chủ ở yêu cầu xác nhận nạp — lỗi nằm ở phía xử lý của máy chủ, không phải phía màn hình.

Đề nghị BA (không chặn bàn giao): đặc tả hiện chỉ ghi "Trả về báo cáo import" mà chưa quy định câu chữ cụ thể của thông báo kết quả nạp, và bảng xử lý lỗi FR-III-05 chưa có thông báo thành công nào. Sau khi sửa xong lỗi trên, đề nghị bổ sung câu chữ chuẩn để vòng nghiệm thu sau có mốc đối chiếu.

Ảnh bằng chứng: https://drive.google.com/file/d/1nVIr_uTzryAjTA1P7O2XSdXysqbqHq2s/view?usp=drivesdk (một khung chứa đồng thời bản xem trước 5/3/0/2, 2 dòng lỗi ERR-KQ-03 + ERR-KQ-04, nút "Xác nhận import (3 dòng hợp lệ)" và thông báo lỗi hệ thống) · https://drive.google.com/file/d/19h7bVollMCBZ49fzqD1hfVuD8-bg4gfH/view?usp=drivesdk (nút "Tải mẫu điểm danh" đã bật sau khi chọn buổi) · https://drive.google.com/file/d/1yvNtCoGlLHzAMMtWQP4bKX09L35Q4K1d/view?usp=drivesdk (bảng điểm danh sau khi nạp, không dòng nào được ghi).

Kết quả trên chỉ có hiệu lực cho môi trường https://18.143.165.120.nip.io bản dựng V1.0.9 tại thời điểm đo; đợt kiểm trước của bên nghiệm thu thực hiện trên htpldn-uat.ospgroup.vn bản V1.0.

── CÁCH VERIFY sau Dev fix ──
Precondition: tài khoản cbnv_tw_02 (Cán bộ Nghiệp vụ Trung ương) + màn Chi tiết khóa học → tab "Điểm danh".
  Cần có sẵn: 1 khóa học ở trạng thái Đang diễn ra, có ≥1 buổi học, và ≥4 học viên trạng thái Đã duyệt.
  Trên môi trường nội bộ dùng khóa KH-QAW7-HOINGHI (a7480002-0000-4000-8000-000000000002), Buổi 4
  (bd1cdf35-8ab7-41f6-ae85-d21fdec2c8c2) — khóa này đã đủ điều kiện.
  Chưa đủ học viên thì vào tab "Học viên" bấm "Phê duyệt" các đăng ký đang Chờ duyệt cho đủ 4.
1) Tab "Điểm danh" → chọn buổi học ở ô "Chọn buổi học để điểm danh" → bấm "Tải mẫu điểm danh", lưu tệp về máy.
2) Mở tệp mẫu, điền cột "Trạng thái điểm danh" cho 3 dòng đầu (lần lượt Có mặt / Vắng có phép / Vắng không phép),
   rồi thêm 2 dòng sai cố ý: 1 dòng dán hoc_vien_id của học viên thuộc khóa KHÁC, 1 dòng ghi trạng thái "XYZ".
   Lưu lại thành tệp .xlsx (giữ nguyên sheet metadata của tệp mẫu, không tạo tệp mới từ đầu).
3) Bấm "Import Excel" → chọn tệp vừa điền → bấm "Kiểm tra tệp" → đọc khối xem trước.
4) Bấm "Xác nhận import (3 dòng hợp lệ)".
5) Đo bằng đường thứ hai: tải lại tab "Điểm danh", chọn lại đúng buổi đó và đếm số học viên đã có trạng thái điểm danh
   (hoặc đọc lại dữ liệu buổi đó qua yêu cầu danh sách điểm danh mà chính màn này gọi).
✅ PASS khi: bước 4 không còn báo "Lỗi hệ thống"; hệ thống hiển thị báo cáo kết quả nạp có nêu số bản ghi nạp thành công
   và số bản ghi không hợp lệ; và ở bước 5 đếm được ĐÚNG 3 học viên có trạng thái điểm danh mới, đúng 3 giá trị đã điền
   (Có mặt / Vắng có phép / Vắng không phép), còn 2 học viên ở 2 dòng lỗi KHÔNG được ghi.
❌ FAIL nếu: bấm xác nhận vẫn trả lỗi hệ thống; hoặc báo cáo hiện ra nhưng số học viên thực sự được ghi khác 3
   (kể cả ca "đúng một phần": ghi 1–2 dòng, hoặc ghi luôn cả dòng lỗi thành 4–5 dòng); hoặc báo cáo không cho biết
   số nạp thành công và số không hợp lệ.
⚠️ Đừng chấm Fail vì câu chữ của thông báo khác với câu trong phiếu — đặc tả chỉ yêu cầu "trả về báo cáo import",
   chưa quy định câu chữ; chấm theo 2 con số và theo số bản ghi thực ghi.
⚠️ Đừng chấm Fail nếu thao tác bị chặn khi khóa đã ở trạng thái Đã kết thúc — đặc tả (srs-fr-03-dao-tao.md:536 và :640)
   bắt buộc đóng điểm danh khi khóa kết thúc, chặn là đúng. Phải đo trên khóa Đang diễn ra.
⚠️ Đừng chấm Pass chỉ vì thấy màn hiện bản xem trước với đủ số 3/2 — phần đó đã đạt sẵn từ lần đo này; lỗi nằm ở
   bước SAU khi bấm xác nhận. Bắt buộc bấm xác nhận thật rồi đọc lại dữ liệu buổi học mới được kết luận.
⚠️ Tab trình duyệt mở lâu vẫn chạy mã cũ — tải lại trang trước khi đo và ghi lại chuỗi phiên bản ở chân thanh menu,
   vì môi trường này được cập nhật liên tục.
Artifact lỗi lần này: ảnh https://drive.google.com/file/d/1nVIr_uTzryAjTA1P7O2XSdXysqbqHq2s/view?usp=drivesdk; yêu cầu xác nhận nạp trả HTTP 500,
mã ERR-SYS-00-00-01, requestId 6415303f-0248-42b0-b314-defb9492ce64 lúc 02:18:52 ngày 07/08/2026.
