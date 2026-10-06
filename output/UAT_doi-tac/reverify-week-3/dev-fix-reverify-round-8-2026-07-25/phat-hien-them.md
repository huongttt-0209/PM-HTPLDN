# Phát hiện thêm — round 8 (2026-07-25)

Các quan sát nằm NGOÀI tiêu chí chấm của QLHSDNHTCP_03 / QLHSDNHTCP_10. **Không tính vào verdict** (cả 2 case đều Pass). Ghi lại để BA/dev cân nhắc, không mở dòng TC mới.

---

## 1. Ba hồ sơ `CT-QAW7-*` có khoảng hạn 15 ngày làm việc, khác 10 ngày của `CT-SEED-*`

| Mã HS | Ngày nộp | Hạn | Số ngày làm việc giữa 2 mốc |
|---|---|---|---|
| CT-QAW7-NORMAL | 24/07/2026 | 14/08/2026 | **15** |
| CT-QAW7-OVERDUE | 04/05/2026 | 25/05/2026 | **15** |
| CT-QAW7-CLOSED | 01/06/2026 | 22/06/2026 | **15** |
| CT-SEED-101 … 110 | 06–07/2026 | — | **10** (đồng nhất cả 10 hồ sơ) |

- Đặc tả `srs-v3.5/srs-fr-06-chi-tra.md:1310`: hạn = ngày nộp + N ngày làm việc, N lấy từ cấu hình SLA, **seed mặc định 10 ngày làm việc** theo NĐ 18/2026/NĐ-CP, quản trị hệ thống sửa được.
- Nhiều khả năng đây là dữ liệu dựng tay của dev để có đủ 4 mức, không phải lỗi tính toán: mức cảnh báo của cả 3 hồ sơ này đều đúng khi tính theo chính khoảng hạn của nó (0% → Bình thường, 393% → Quá hạn nghiêm trọng).
- **Rủi ro:** trong cùng một danh sách đang tồn tại 2 khoảng hạn khác nhau cho cùng loại hồ sơ. Nếu đây không phải chủ ý thì con số "còn 15 ngày LV" của CT-QAW7-NORMAL đang rộng hơn thực tế 5 ngày làm việc.
- **Đề xuất:** BA xác nhận giá trị N đang cấu hình cho hồ sơ chi trả, và dev cho biết 3 hồ sơ `CT-QAW7-*` có phải fixture cắm tay hay không.
- Đã thử tra cấu hình qua các đường `cau-hinh-sla` / `cau-hinh-slas` / `cau-hinh-he-thong?nhom=SLA` — đều không tồn tại, nên chưa tự kiểm chứng được N hiện hành.

## 2. Hồ sơ đã kết thúc hiển thị nhãn thứ 5 — "Đã hoàn thành"

- 4 hồ sơ ở trạng thái kết thúc (CT-SEED-108 Đã thanh toán, CT-SEED-109 Từ chối, CT-SEED-110 Hủy, CT-QAW7-CLOSED Đã thanh toán) hiển thị ô SLA = **"Đã hoàn thành"** ở cả màn danh sách lẫn thanh tổng quan màn chi tiết.
- Đây chính là cách dev xử lý gạch lỗi "hồ sơ đã kết thúc vẫn bị đếm quá hạn" — hợp lý về nghiệp vụ và đã giải quyết đúng vấn đề QA nêu, nên **không tính là lỗi**.
- Tuy nhiên "Đã hoàn thành" không nằm trong bộ 4 nhãn BR-SLA-02 của đặc tả (`:1514-1523`), và máy chủ vẫn trả mức `BINH_THUONG` cho các hồ sơ này → giao diện và trường dữ liệu đang nói hai chuyện khác nhau.
- Thêm nữa, chữ "Đã hoàn thành" chưa sát với hồ sơ **Từ chối** (CT-SEED-109) và **Hủy** (CT-SEED-110) — hai hồ sơ này kết thúc chứ không "hoàn thành".
- **Đề xuất:** BA chốt nhãn hiển thị cho hồ sơ ở trạng thái kết thúc (giữ "Đã hoàn thành", đổi thành "Đã kết thúc", hay để trống), và bổ sung vào đặc tả để lần sau không lệch.

## 3. CT-SEED-102: chú thích 101% trong khi tính theo ngày làm việc tròn là 100%

- Hạn 24/07/2026, hôm nay 25/07/2026 → đã trôi đúng 10/10 ngày làm việc, chú thích app ghi **"101% thời hạn đã dùng"**, nhãn "Quá hạn · 0 ngày LV".
- Nhãn **đúng** (đã qua hạn thì phải là Quá hạn), số ngày quá hạn **đúng** (chưa sang ngày làm việc nào sau hạn). Chênh 1% là do app tính theo mốc giờ chứ không làm tròn theo ngày.
- Không phải lỗi, chỉ nêu để nếu sau này có ai đối chiếu con số thì không hiểu nhầm.

## 4. Bảng danh sách bị cắt ngang ở độ rộng màn hình 1440

- Ở khung nhìn 1440×900, cột SLA bị cắt mất phần đuôi ("Bình thường · cò…", "Quá hạn · 5 ngà…") do bảng rộng hơn vùng hiển thị, phải kéo ngang mới đọc hết nhãn. Ở 1920 thì đọc trọn.
- Nhãn mới dài hơn nhãn cũ khá nhiều nên vấn đề này chỉ mới lộ ra sau bản sửa. Không thuộc tiêu chí đang chấm (KQ mong đợi của case gốc có nhắc "không bị tràn/đè lên nhau", nhưng chữ ở đây bị **cắt** chứ không tràn hay đè).
- **Đề xuất:** dev cân nhắc nới bề rộng cột SLA hoặc rút gọn nhãn để máy 1366–1440 đọc được mà không phải kéo ngang.
