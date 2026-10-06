# Tiêu chí chấm — QLHSDNHTCP_10 (dòng 19)

> Round 7 · 2026-07-25. **CẤM tự đặt tiêu chí khác.** Chấm theo đúng 2 khối dưới:
> (A) bar gốc dev đặt ở round trước, (B) các lỗi CÒN LẠI mình đã ghi cho đối tác ở lượt Reopen gần nhất.
> PASS = (A) đủ điều kiện PASS **và** (B) không còn gạch đầu dòng nào tái hiện.

## Case gốc (đối tác)
- **Mô tả:** Nhóm 0 — Thanh thông tin tổng quan hồ sơ
- **Điều kiện:** 1. Đăng nhập tài khoản
- **Các bước:** 1. Chọn menu "Chi trả chi phí"
2. Nhấn vào liên kết tại bản ghi
- **KQ mong đợi:** - Hệ thống hiển thị các trường thông tin giống với thiết kế
- Dữ liệu hiển thị đúng định dạng và trường thông tin
- Dữ liệu hiển thị không bị tràn/đè lên nhau, đồng nhất ngôn ngữ hiển thị
- **KQ thực tế (đối tác báo):** Mức cảnh báo thời hạn không giống với thiết kế

## (A) Bar gốc của DEV — bộ "CÁCH VERIFY" đã chốt

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

## (B) Lỗi CÒN LẠI sau lượt Reopen gần nhất (nội dung đang nằm ở cột R của sheet)

- Hồ sơ chưa quá hạn thì thanh thông tin tổng quan không có trường SLA. Mở CT-SEED-101 (Chờ tiếp nhận), thanh tổng quan chỉ có Mã HS, Quy mô DN và Trạng thái, không có mục cảnh báo thời hạn nào, trong khi ngoài danh sách hồ sơ này vẫn hiện nhãn SLA.
- Hồ sơ đã tiếp nhận thì trường SLA có hiện nhãn kèm số ngày, nhưng mức gắn sai giống lỗi ngoài danh sách: CT-SEED-108 thanh toán xong ngày 24/06 trong khi hạn là 29/06, tức xử lý đúng hạn, mà màn chi tiết vẫn hiện "Quá hạn nghiêm trọng · 21 ngày LV".
- Hai màn còn tính lệch nhau: cùng hồ sơ CT-SEED-107, chú thích tỷ lệ thời hạn đã dùng ngoài danh sách là 350% nhưng vào màn chi tiết lại là 400%, do màn chi tiết đếm từ ngày cán bộ tiếp nhận thay vì ngày doanh nghiệp nộp.
