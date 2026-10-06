# NHSYC_OOS_02 — đo lại trên môi trường nghiệm thu đối tác (05/08/2026)

Tiêu chí lấy nguyên khối ở cột `DEV phản hồi lần 1`, dòng 154 (tab `UAT_TGPL Doanh Nghiệp-tuần 2`).

| Điều kiện | Bug gốc (khối tiêu chí) | Mình test | GAP? |
|---|---|---|---|
| Môi trường | Môi trường nghiệm thu của đối tác | `https://htpldn-uat.ospgroup.vn` — nhãn `HTPLDN · V1.0.7` | Không |
| Vai trò | `cbnv_tw` | `cbnv_tw` · CB_NV_TW · cấp TW · Cục Bổ trợ tư pháp | Không |
| Màn hình | Vụ việc HTPL → [Nhập thủ công] (`/vu-viec/tao-moi`) | Đúng màn đó | Không |
| Ngày thao tác | Ngày hiện tại = 05/08/2026 (đúng ngày phản ánh gốc bị chặn) | 05/08/2026 — trùng đúng ngày của phản ánh gốc | Không |
| Thao tác với ô Ngày tiếp nhận | KHÔNG động vào ô, giữ nguyên giá trị hệ thống điền sẵn | Không mở lịch, không gõ, không xóa — đọc lại ngay trước khi bấm lưu vẫn là `05/08/2026` do hệ thống tự điền | Không |
| Trường bắt buộc còn lại | Chọn doanh nghiệp + điền đủ trường bắt buộc | Doanh nghiệp `DN-AG-001 — Công ty TNHH Bình Minh AG`, Tiêu đề, Nội dung, Lĩnh vực `Thuế`, Loại hình `Tư vấn pháp luật`, Kênh `Trực tiếp` | Không |
| Nút bấm | [Lưu & Tiếp nhận] | Đúng nút đó | Không |
| Bước đọc lại | Mở hồ sơ vừa tạo, đọc ô Ngày tiếp nhận và Thời hạn xử lý | Mở màn chi tiết hồ sơ vừa tạo, đọc đúng hai ô đó | Không |
| Cách đo thứ 2 | Đọc trên giao diện | Đối chiếu thêm giá trị đang lưu ở phía máy chủ của chính hồ sơ đó | Không |

**Kết luận: 0 GAP → PASS.**

## Đối chiếu từng ý của khối tiêu chí

- **Lưu được ngay, không có thông báo chặn**: bấm [Lưu & Tiếp nhận] một lần, hồ sơ tạo thành công
  `VV-BTP-TW-20260805-003`, thông báo thu được là **"Đã tiếp nhận — VV-BTP-TW-20260805-003"**. Bộ bắt thông
  báo cài sẵn **trước** khi bấm không bắt được dòng nào có chữ "Ngày tiếp nhận không được ở tương lai", cũng
  không có dòng lỗi đỏ nào dưới ô nhập. Màn hình chuyển thẳng sang chi tiết hồ sơ. Tình huống của phản ánh
  gốc (chặn lưu, không gửi yêu cầu nào đi, phải lùi ngày về 04/08/2026 mới lưu được) **không còn**.
- **Ngày tiếp nhận lưu đúng bằng ngày thao tác**: màn chi tiết hiện `Ngày tiếp nhận 05/08/2026 00:00` — đúng
  bằng ngày thao tác và đúng bằng giá trị hệ thống điền sẵn, không bị lùi một ngày. Giá trị đang lưu ở máy
  chủ là `2026-08-04T17:00:00.000Z`, tức **00:00 ngày 05/08/2026 giờ Việt Nam** — không còn hiện tượng ngày
  hôm nay bị quy về cuối ngày rồi coi là tương lai như dev nghi ngờ ở phần nguyên nhân.
- **Thời hạn xử lý được tính từ chính ngày đó**: màn chi tiết hiện `Thời hạn xử lý 20/08/2026`, giá trị lưu
  ở máy chủ `deadline = 2026-08-19T17:00:00.000Z` (= 00:00 ngày 20/08/2026 giờ Việt Nam), tức mốc hạn được
  đặt từ chính ngày tiếp nhận 05/08/2026 chứ không phải từ 04/08. Thẻ cảnh báo trên đầu hồ sơ hiện
  `Bình thường · còn 11 ngày LV`, khớp đúng số ngày làm việc còn lại từ 05/08 đến 20/08.
- **Hệ quả nghiệp vụ đã hết**: cán bộ không còn phải ghi lùi ngày tiếp nhận so với thực tế, nên mốc hạn
  không còn bị lệch một ngày do thao tác chữa cháy.

Ảnh: `../image/NHSYC_OOS_02-uat-luu-duoc-ngay-mac-dinh.png`

## Ghi nhận thêm — điểm nằm NGOÀI phiếu này, đề nghị BA/dev xem

- **Mốc hạn đang cộng theo ngày lịch, không phải ngày làm việc.** Hồ sơ trên có ngày tiếp nhận 05/08/2026
  (thứ Tư) → hạn xử lý 20/08/2026, đúng bằng **+15 ngày lịch**. Nếu tính **+15 ngày làm việc** như đặc tả
  (`srs-v3.5/srs-fr-05-vu-viec.md:343` — "Tính deadline SLA: ngày tiếp nhận + 15 ngày làm việc
  (NĐ55/2019 Điều 8 Khoản 1)", và `BR-SLA-01` ở dòng 2338) thì hạn phải là **26/08/2026**. Chênh 6 ngày,
  theo hướng bất lợi cho đơn vị xử lý. Điểm này **không thuộc tiêu chí của phiếu NHSYC_OOS_02** (phiếu chỉ
  yêu cầu hạn được tính *từ chính ngày tiếp nhận*, và điều đó đúng) nên không dùng làm căn cứ trượt; ghi
  lại để bên mình quyết có mở phiếu riêng hay không. Lưu ý đặc tả cũng nói SLA "có thể cấu hình khác tại
  UC108" — cần BA xác nhận môi trường này có đang đặt cấu hình khác hay không trước khi kết luận.
- Dữ liệu phát sinh khi đo (là bước bắt buộc của chính kịch bản): 1 hồ sơ vụ việc
  `VV-BTP-TW-20260805-003` — tiêu đề mở đầu bằng "QA UAT 05-08", trạng thái "Đã tiếp nhận",
  doanh nghiệp `DN-AG-001`. Không sửa, không xóa hồ sơ nào có sẵn.
