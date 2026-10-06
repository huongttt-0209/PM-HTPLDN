# Bảng đối chiếu điều kiện — CPCTHTTTG_03 (re-verify vòng 2, 05/08/2026)

Loại bug: **cách hiển thị số liệu trên trục dọc của biểu đồ + bảng tổng hợp của báo cáo** → phụ thuộc dữ liệu thật ⇒ bắt buộc điền bảng đối chiếu, 0 GAP.
Ô note của dòng này (*DEV phản hồi lần 2*) KHÔNG có khối `── CÁCH VERIFY sau Dev fix ──` và cũng KHÔNG có mục "Phần còn lỗi"; note nêu 3 điều đã khắc phục (nhãn trục dọc đọc được · có trục dọc riêng cho "Số hồ sơ" · bảng tổng hợp đủ cột và khớp biểu đồ). Vì vậy lấy đúng 3 điều đó cộng với triệu chứng gốc của phiếu ("số liệu trục tung toàn bộ là 0") làm điều kiện phải đạt.

| Điều kiện | Bug gốc (note vòng 2 + KQ thực tế lần 1) | Mình test | GAP? |
|---|---|---|---|
| Môi trường | Môi trường bàn giao, bản dựng đang chạy | `https://18.143.165.120.nip.io` — bản dựng **HTPLDN · V1.0.6** (đọc ở thanh bên trái) | Không |
| Vai trò | Cán bộ nghiệp vụ Trung ương | `cbnv_tw` · CB Nghiệp vụ - Trung ương · CB_NV_TW · BTP · TW | Không |
| Màn hình | Báo cáo thống kê | Báo cáo thống kê (`/bao-cao`) | Không |
| Loại báo cáo | Chi phí theo thời gian | **BC Chi phí theo thời gian** (chọn đúng tên, không chọn loại gần giống) | Không |
| Kỳ báo cáo | Năm 2026, từ 01/01/2026 đến 31/12/2026 | **Năm** — Từ 01/01/2026 đến 31/12/2026 | Không |
| Đơn vị | Toàn quốc | **Toàn quốc** | Không |
| Tiền đề dữ liệu | Có số liệu chi phí trong kỳ để biểu đồ vẽ được | Có: **Tổng chi phí toàn kỳ 23.000.000 · Tổng hồ sơ toàn kỳ 2**. Số liệu môi trường nay khác con số trong note (226.308.268 / 25) nhưng vẫn khác 0, đủ để đọc trục và đối chiếu | Không |
| Thao tác sinh ra lỗi cũ | Nhập tiêu chí rồi nhấn "Xem báo cáo" | Bấm **Xem báo cáo** thật, chờ biểu đồ và bảng vẽ xong (không chấm bằng quan sát tĩnh) | Không |
| Cách đọc trục dọc | Đọc số liệu trên trục tung | Đọc trực tiếp từng nhãn trên hai trục của biểu đồ + đo vị trí điểm dữ liệu so với vạch chia, kèm ảnh chụp màn | Không |
| Số lần đo | Loại trừ ngẫu nhiên một lần | Vẽ lại báo cáo **2 lần** (lúc 01:58 và 02:00), kết quả đọc được giống hệt nhau | Không |

**Kết luận: 0 GAP** — đúng bản dựng đang chạy, đúng vai trò, đúng loại báo cáo, đúng kỳ và đơn vị, có số liệu thật khác 0, đã bấm "Xem báo cáo" thật và đọc trục bằng cả số đo lẫn ảnh.

## Đo lường trực tiếp (05/08/2026, `18.143.165.120.nip.io`, bản dựng V1.0.6)

### Triệu chứng gốc của phiếu — "số liệu ở trục tung hiển thị toàn bộ giá trị 0"

- ✅ **Không còn**. Trục dọc bên trái (thang tiền) đọc được lần lượt: **0 · 6 triệu · 12 triệu · 18 triệu · 24 triệu** — có nhãn rút gọn "triệu", không phải chuỗi "000.000", cũng không phải toàn số 0.

### Ba điều note nêu là đã khắc phục — kiểm lại từng điều

- ✅ **Nhãn trục dọc đọc được bình thường** → 5 vạch chia trục tiền như trên, chữ không bị cắt, không bị chồng.
- ✅ **Có trục dọc riêng bên phải cho "Số hồ sơ"** → trục bên phải đọc được **0 · 1 · 2 · 3 · 4**, tách hẳn khỏi thang tiền bên trái. Chú giải dưới biểu đồ ghi rõ hai đường: **Số hồ sơ** (xanh dương) và **Tổng chi phí** (xanh lá).
- ✅ **Đường "Số hồ sơ" nằm đúng vị trí giá trị của nó, không bị dồn sát đáy** → đo vị trí điểm dữ liệu:
  - Điểm "Số hồ sơ" nằm đúng mức vạch **2** của trục bên phải (khớp Tổng hồ sơ toàn kỳ = 2), cách đáy rõ ràng.
  - Điểm "Tổng chi phí" nằm giữa vạch 18 triệu và 24 triệu, quy ra khoảng **23 triệu** — khớp Tổng chi phí toàn kỳ 23.000.000.
- ✅ **Bảng tổng hợp đủ cột và khớp biểu đồ** → bảng có đúng 5 cột **Kỳ · Từ ngày · Đến ngày · Số hồ sơ · Tổng chi phí**; dòng dữ liệu: Năm 2026 · 01/01/2026 · 31/12/2026 · **2** · **23.000.000 ₫** — khớp cả hai ô số tổng phía trên và khớp vị trí hai điểm trên biểu đồ.
- Ảnh (hai trục dọc + chú giải + bảng tổng hợp): [`../image/CPCTHTTTG_03-bieu-do-2-truc-doc.png`](../image/CPCTHTTTG_03-bieu-do-2-truc-doc.png)

### Kết luận

Triệu chứng gốc của phiếu không còn; cả ba điều note nêu đều đúng trên bản đang chạy, đo lại 2 lần cho kết quả giống nhau; biểu đồ và bảng tổng hợp khớp nhau và khớp số tổng → **Pass**.

### Ghi nhận thêm (ngoài phạm vi phiếu — không tự thêm dòng mới vào sheet)

- Kỳ báo cáo "Năm" chỉ sinh đúng một mốc thời gian (Năm 2026) nên biểu đồ chỉ có một điểm cho mỗi đường, chưa thấy được nét "xu hướng" nối nhiều kỳ. Đây là hệ quả của việc chọn kỳ Năm chứ không phải lỗi hiển thị; note cũng đo trên đúng kỳ Năm này.
- Thử đổi Kỳ báo cáo sang "Quý" thì hệ thống tự đặt khoảng thời gian về **01/07/2026 → 30/09/2026** (quý hiện tại) và báo "Không có dữ liệu báo cáo cho kỳ và đơn vị đã chọn"; hai nút Xuất Excel / Xuất PDF tự mờ đi. Ô "Thời gian" bị khóa theo kỳ, người dùng không tự chọn được quý khác. Không thuộc phạm vi phiếu này, chỉ ghi lại để đối tác/BA biết.
- Ô "Tổng chi phí toàn kỳ" trên đầu màn hiển thị **23,000,000** (dấu phẩy, không có ký hiệu tiền), trong khi cột "Tổng chi phí" của bảng ghi **23.000.000 ₫** (dấu chấm, có ký hiệu tiền). Chỉ là khác cách định dạng, số liệu vẫn khớp; ghi lại để biết.
