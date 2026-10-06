# CPCTHTTTG_03 — đo lại trên môi trường nghiệm thu đối tác (05/08/2026)

Tiêu chí lấy nguyên khối ở cột `DEV phản hồi lần 2`, dòng 259 (tab `UAT_TGPL Doanh Nghiệp-tuần 3`).

| Điều kiện | Bug gốc (khối tiêu chí) | Mình test | GAP? |
|---|---|---|---|
| Môi trường | Bản mới nhất của môi trường nghiệm thu | `https://htpldn-uat.ospgroup.vn` — nhãn `HTPLDN · V1.0.7` | Không |
| Vai trò | `cbnv_tw` | `cbnv_tw` · CB_NV_TW · cấp TW · Cục Bổ trợ tư pháp | Không |
| Loại báo cáo | Chi phí theo thời gian | `BC Chi phí theo thời gian`, kỳ `Năm` (01/01/2026 – 31/12/2026), đơn vị `Toàn quốc` | Không |
| Điểm 1 | Nhãn trục dọc đọc được, không còn toàn giá trị 0 | Đọc nguyên văn nhãn trên biểu đồ, không đoán bằng mắt | Không |
| Điểm 2 | Có trục dọc riêng bên phải cho "Số hồ sơ" | Đọc cả hai dãy nhãn trục dọc và đối chiếu thang giá trị với dữ liệu thực | Không |
| Điểm 3 | Bảng tổng hợp đủ cột Kỳ, Từ ngày, Đến ngày, Số hồ sơ, Tổng chi phí và khớp biểu đồ | Đọc tiêu đề và từng ô của bảng, đối chiếu với hai ô tổng hợp phía trên biểu đồ | Không |
| Điểm 4 | Đã đo lại hai lần, kết quả giống nhau | Bấm [Xem báo cáo] hai lần, so nguyên văn nhãn biểu đồ + bảng + ô tổng hợp | Không |

**Kết luận: 0 GAP → PASS.**

## Đối chiếu từng ý của khối tiêu chí

- **Nhãn trục dọc đọc được bình thường, không còn toàn giá trị 0**: trục dọc bên trái (Tổng chi phí) hiện
  `0 · 60 triệu · 120 triệu · 180 triệu · 240 triệu`. Tình trạng "toàn bộ giá trị 0" ở phản ánh gốc
  **không còn**.
- **Có trục dọc riêng bên phải cho "Số hồ sơ"**: trục bên phải hiện `0 · 7 · 14 · 21 · 28`, thang riêng
  cho số hồ sơ. Giá trị thực của kỳ là **25 hồ sơ**, nằm gần đỉnh thang 28 — tức đường "Số hồ sơ" đứng đúng
  vị trí giá trị của nó chứ không bị dồn sát đáy như khi dùng chung thang tiền (226 triệu). Chú giải biểu
  đồ cũng ghi rõ hai chuỗi `Số hồ sơ` và `Tổng chi phí`.
- **Bảng tổng hợp đủ cột và khớp số liệu biểu đồ**: tiêu đề bảng là
  `Kỳ · Từ ngày · Đến ngày · Số hồ sơ · Tổng chi phí`; dòng dữ liệu là
  `Năm 2026 · 01/01/2026 · 31/12/2026 · 25 · 226.308.268 ₫`. Hai ô tổng hợp phía trên biểu đồ ghi
  `Tổng chi phí toàn kỳ 226,308,268` và `Tổng hồ sơ toàn kỳ 25` — khớp đúng với bảng và với thang của hai
  trục dọc.
- **Đo lại hai lần cho kết quả giống nhau**: bấm [Xem báo cáo] lần thứ hai với cùng điều kiện — nhãn hai
  trục, dòng bảng và hai ô tổng hợp giống hệt lần thứ nhất (so nguyên văn, không so bằng mắt).

Ảnh: `../image/CPCTHTTTG_03-uat-hai-truc-doc-co-so-lieu.png`

## Ghi nhận thêm

- **Biểu đồ chỉ có một điểm dữ liệu** vì báo cáo này gom cả khoảng thời gian đã chọn thành **một kỳ duy
  nhất** — thử cả ba kiểu kỳ (`Năm`, `Tháng`, `Khoảng tùy chọn` 01/01–31/12/2026) đều ra đúng một dòng
  `Kỳ / Từ ngày / Đến ngày`. Nghĩa là "đường xu hướng" thực chất không có nhiều mốc để nối. Đây là cách
  báo cáo đang được thiết kế, không nằm trong phạm vi phiếu (phiếu chỉ nói về nhãn trục dọc bằng 0) nên
  không dùng làm căn cứ trượt; ghi lại để BA quyết có yêu cầu tách nhỏ kỳ (theo tháng/quý trong khoảng
  chọn) hay không.
- Kỳ `Tháng` mặc định là tháng hiện tại (08/2026) và **không có dữ liệu** — màn hiện đúng câu
  "Không có dữ liệu báo cáo cho kỳ và đơn vị đã chọn", không phải lỗi.
- Không tạo, không sửa dữ liệu nghiệp vụ nào khi đo phiếu này — chỉ xem báo cáo.
