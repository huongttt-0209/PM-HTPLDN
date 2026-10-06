# Tiêu chí chấm — QLHSDNHTCP_03 (dòng 16)

> Round 7 · 2026-07-25. **CẤM tự đặt tiêu chí khác.** Chấm theo đúng 2 khối dưới:
> (A) bar gốc dev đặt ở round trước, (B) các lỗi CÒN LẠI mình đã ghi cho đối tác ở lượt Reopen gần nhất.
> PASS = (A) đủ điều kiện PASS **và** (B) không còn gạch đầu dòng nào tái hiện.

## Case gốc (đối tác)
- **Mô tả:** Kiểm tra Cột dữ liệu trong bảng kết quả
- **Điều kiện:** 1. Đăng nhập tài khoản
- **Các bước:** 1. Chọn menu "Chi trả chi phí"
- **KQ mong đợi:** - Hệ thống hiển thị các trường thông tin giống với thiết kế
- Dữ liệu hiển thị đúng định dạng và trường thông tin
- Dữ liệu hiển thị không bị tràn/đè lên nhau, đồng nhất ngôn ngữ hiển thị
- Mặc định: hệ thống sắp xếp theo ngày cập nhật mới nhất trước, 20 bản ghi mỗi trang.
- **KQ thực tế (đối tác báo):** Cột thông tin Mức cảnh báo thời hạn không giống với thiết kế

## (A) Bar gốc của DEV — bộ "CÁCH VERIFY" đã chốt

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

## (B) Lỗi CÒN LẠI sau lượt Reopen gần nhất (nội dung đang nằm ở cột R của sheet)

- Cột SLA đã có nhãn mức kèm số ngày, nhưng mức gắn cho nhiều hồ sơ vẫn sai.
- Hồ sơ còn hạn bị báo quá hạn: CT-SEED-101 nộp 15/07, hạn xử lý 10 ngày làm việc là 29/07 nên vẫn còn hạn, đúng ra phải là "Sắp hết hạn", nhưng danh sách hiện "Quá hạn · 0 ngày LV".
- Hồ sơ mới trễ ít đã bị đẩy lên mức nặng nhất: CT-SEED-105 (nộp 03/07, hạn 17/07) trễ 5 ngày làm việc và CT-SEED-106 (nộp 01/07, hạn 15/07) trễ 7 ngày làm việc, nhưng cả hai đều hiện "Quá hạn nghiêm trọng"; mức này chỉ dùng khi trễ vượt quá 2 lần thời hạn.
- Hồ sơ đã kết thúc vẫn tiếp tục bị đếm quá hạn: CT-SEED-108 thanh toán xong ngày 24/06 trong khi hạn là 29/06, tức xử lý đúng hạn, vẫn hiện "Quá hạn nghiêm trọng · 21 ngày LV"; CT-SEED-109 từ chối ngày 27/06 (hạn 03/07) và CT-SEED-110 đã hủy cũng bị gắn "Quá hạn nghiêm trọng".
- Nguyên nhân chung: hạn xử lý đang tính 10 ngày liên tục kể từ ngày nộp, không trừ thứ Bảy, Chủ nhật và ngày lễ, nên tỷ lệ thời hạn đã dùng bị đội lên và nhảy mức sớm (ví dụ CT-SEED-103 chú thích 188% trong khi tính đúng chỉ 150%).
- Duyệt hết 10 hồ sơ của cả 5 thẻ trạng thái chỉ thấy 2 mức "Quá hạn" và "Quá hạn nghiêm trọng"; không hồ sơ nào hiện "Bình thường" hoặc "Sắp hết hạn".
