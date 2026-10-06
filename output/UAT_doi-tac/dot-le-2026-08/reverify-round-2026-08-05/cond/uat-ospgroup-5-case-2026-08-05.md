# Bảng đối chiếu điều kiện — 5 case đo lại trên môi trường UAT đối tác (05/08/2026, 12:05–13:00)

Tiêu chí lấy nguyên từ khối `── CÁCH VERIFY sau Dev fix ──` (cột R hoặc Y) của chính từng dòng trên sheet,
không tự đặt thêm.

| Điều kiện | Bug gốc | Mình test | GAP? |
|---|---|---|---|
| Môi trường | Môi trường nghiệm thu của đối tác | `https://htpldn-uat.ospgroup.vn` — bundle `assets/index-Dn5IWt_M.js`, nhãn `HTPLDN · V1.0.7` | Không |
| Vai trò (4 case nghiệp vụ) | Cán bộ nghiệp vụ TW | `cbnv_tw` · CB_NV_TW · `donViId 00000000-0000-4000-8000-000000000001` · cấp TW | Không |
| Vai trò (QLTKND_03) | Quản trị hệ thống | `admin` · QTHT · vào được màn Tài khoản & phân quyền | Không |
| Đăng nhập | — | Có bước mã xác thực; mã lấy ở MailHog của chính môi trường đó | Không |
| Dữ liệu không bị bộ đệm cũ | — | Báo cáo ghi "Thời điểm tạo: 05/08/2026 12:41", sinh mới trong phiên đo | Không |
| Thao tác đo | Bấm thật trên giao diện | Toàn bộ đo qua trình duyệt; số liệu đọc từ DOM và từ phần hồi đáp của máy chủ | Không |

**Kết luận: 0 GAP.**

## VVTLV_06 (tuần 3, dòng 244) — 3 ý → PASS

- Ý 1 · đầu trang: `CỤC BỔ TRỢ TƯ PHÁP - BỘ TƯ PHÁP` · `CỘNG HÒA XÃ HỘI CHỦ NGHĨA VIỆT NAM` · `Độc lập - Tự do - Hạnh phúc`
- Ý 2 · cuối trang: `Ngày 05 tháng 08 năm 2026` · `NGƯỜI XUẤT BÁO CÁO` · `(Ký, ghi rõ họ tên và đóng dấu)` · `Cán bộ NV Trung ương`; **không có dòng chức danh**
- Ý 3 · tên tệp: lần 1 `BaoCaoVuViecTheoLinhVuc_20260805_1242.pdf` (giờ máy chủ 05:42:08 GMT), lần 2 `..._20260805_1243.pdf` (05:43:32 GMT) — cùng ngày, hai tên khác nhau
- Kiểm lại: khổ trang 595.3 × 841.9 pt = A4 dọc · phông `Tinos` (bộ tương thích số đo Times New Roman trên máy chủ Linux), khối quốc hiệu và khối ký cỡ 13 · đủ tên báo cáo / kỳ / đơn vị / ngày tạo · số liệu trong tệp trùng khít bảng trên màn hình, tổng 59
- Ảnh: `../image/VVTLV_06-uat-pdf-dau-trang-va-khoi-ky.png` · tệp gốc: `../evidence/VVTLV_06-uat-lan1.pdf`, `../evidence/VVTLV_06-uat-lan2.pdf`

## TLCTCDG_11 (tuần 3, dòng 58) — 4 ý → PASS

- Ý 1: dải cảnh báo `Tổng trọng số hiện tại: 90%. Cần đảm bảo = 100% trước khi trình phê duyệt` — đúng nguyên văn Kết quả mong đợi của phiếu
- Ý 2: bấm Lưu → hai thông báo bật cùng một mốc thời gian (bắt bằng bộ theo dõi DOM, không lọc trùng): `Đã lưu tiêu chí đánh giá` và thông điệp trọng số nói trên
- Ý 3: dải thang điểm `Tổng điểm tối đa có trọng số hiện tại: 90. Cần đảm bảo = 100 trước khi trình phê duyệt`
- Ý 4: nhãn `(Tổng trọng số phải bằng 100%)` là chữ đỏ `rgb(245,34,45)`, và thao tác lưu không bị chặn
- Bền sau khi tải lại trang: tiêu chí còn nguyên, tổng vẫn 90%, đợt vẫn "Lập kế hoạch", hai dải cảnh báo vẫn hiện
- Dữ liệu đã tạo khi đo: thêm 1 tiêu chí `QA doi chung UAT 05-08 trong so 90` (trọng số 90) vào đợt `DG-20260803-0001` — đợt do QA tạo ngày 03/08 đúng cho phép thử này
- Ảnh: `../image/TLCTCDG_11-uat-canh-bao-trong-so-90.png`

## QLTKND_03 (tuần 3, dòng 166) — 5 ý → PASS

- Bốn màu ở cột Trạng thái: Hoạt động `rgb(82,196,26)` xanh lá · Chờ kích hoạt `rgb(250,173,20)` vàng · Tạm khóa `rgb(245,34,45)` đỏ · Vô hiệu hóa `rgb(0,0,0)` đen
- Số trên từng thẻ khớp đúng danh sách lọc ra, đọc từ dòng "Hiển thị … / N kết quả": Tất cả 218 · Hoạt động 148 · Chờ kích hoạt 28 · Tạm khóa 2
- Thanh thẻ còn đúng 4 thẻ, không còn thẻ "Chờ phân quyền"
- Ảnh: `../image/QLTKND_03-uat-mau-vo-hieu-hoa-den.png`
- Ghi nhận ngoài phạm vi phiếu, KHÔNG chấm là lỗi ở đây: còn 2 bản ghi mang trạng thái `CHO_PHAN_QUYEN` (trạng thái BA đã bỏ 07/05/2026) — không thẻ nào lọc ra được nhưng vẫn đếm vào "Tất cả", nên 148+28+2+38 = 216 ≠ 218

## QLLSHTCTVV_04 (tuần 2, dòng 126) — PASS phần quyết định

- Ô lọc "Trạng thái vụ việc" đúng 3 lựa chọn: Đang xử lý / Hoàn thành / Từ chối — **không còn "Đã hủy"**, tức điều kiện FAIL của phiếu không xảy ra
- Chọn cả 3 lựa chọn → ra đúng tổng khi không lọc, không vụ việc nào nằm ngoài mọi lựa chọn
- Đúng ở cả hai màn: tab "Lịch sử hỗ trợ" của tư vấn viên và tab "Vụ việc đã hỗ trợ" của người hỗ trợ pháp lý
- Điểm yếu đã ghi nhận: hồ sơ đo được chỉ có 1 vụ việc nên phép cộng tổng là phép thử yếu
- Ảnh: `../image/QLLSHTCTVV_04-uat-oloc-3-lua-chon-khong-con-da-huy.png`

## KTDGKQHT_02 (tuần 2, dòng 116) — PASS phần quyết định

- Cột "Chuyên cần" hiện `2/2 (100.00%)` và `1/2 (50.00%)`; rê chuột ra chú giải đủ bốn con số
- Học viên 1: có mặt 2 · vắng có phép 0 · vắng không phép 0 → 2/2 = 100%
- Học viên 2: có mặt 1 · vắng có phép 0 · vắng không phép 1 → (1+0)/2 = 50%
- Điều kiện FAIL của phiếu là "không đọc được số buổi vắng có phép hoặc vắng không phép ở bất kỳ đâu" — không xảy ra
- Điểm yếu đã ghi nhận: cả hai học viên có vắng có phép = 0, nên vế "vắng có phép nằm trong tử số" chưa bị thử với giá trị khác 0
- Ảnh: `../image/KTDGKQHT_02-uat-chu-giai-du-4-con-so-chuyen-can.png`

## Không nằm trong 5 case ghi sheet

`QLLSHTCTVV_03` (tuần 2, dòng 125): **không đủ điều kiện đo**. Hồ sơ tiền đề TVV-BTP-TW-0002 trên môi trường
này có 0 vụ việc; hồ sơ thay thế TVV-BTP-TW-0035 có 1 vụ việc với cột Đánh giá bỏ trống, nên không có dãy sao
nào để đo vỡ hàng ở 1440px/1600px. Giữ nguyên trạng, không ghi kết luận.
