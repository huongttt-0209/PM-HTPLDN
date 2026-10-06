# Bảng đối chiếu điều kiện — KTDGKQHT_23 (re-verify vòng 1, 05/08/2026)

Loại bug: **mẫu số của tỷ lệ chuyên cần bị chốt cứng tại thời điểm lưu điểm danh, không tính lại khi lịch học thêm buổi** → phụ thuộc dữ liệu điểm danh và lịch học thật ⇒ bắt buộc điền bảng đối chiếu, 0 GAP.
Ô note của dòng này (*DEV phản hồi lần 1*) KHÔNG có khối `── CÁCH VERIFY sau Dev fix ──`, nên lấy phần **"Web đang sai"** (khóa có 4 buổi ở tab "Lịch học" nhưng tab "Kết quả" vẫn tính chuyên cần trên 3 buổi, cùng một bảng hiện hai mẫu số khác nhau) làm điều kiện phải hết lỗi; phần **dòng KTDGKQHT_20 đã hết lỗi** là mốc đã đạt, vẫn kiểm lại để chắc không hồi quy.

| Điều kiện | Bug gốc (note vòng 1) | Mình test | GAP? |
|---|---|---|---|
| Môi trường | Bản dựng V1.0.5 khi phát hiện lỗi | `https://18.143.165.120.nip.io` — bản dựng đang chạy **HTPLDN · V1.0.6** (đọc ở thanh bên trái) | Không |
| Vai trò | `cbnv_tw` — cán bộ nghiệp vụ đúng đơn vị của khóa học | `cbnv_tw` · CB Nghiệp vụ - Trung ương · CB_NV_TW · đơn vị Cục Bổ trợ tư pháp - Bộ Tư pháp · cấp TW | Không |
| Trạng thái khóa học | Khóa "Đang diễn ra", có học viên trong danh sách kết quả | Khóa **KH-QAW7-HOINGHI** "QAW7 — Hội nghị đối thoại DN 2026" — **Đang diễn ra**, 2 học viên trong danh sách kết quả | Không |
| Dữ liệu gốc của phiếu | Khóa KH-20260509-006 "Luật đất đai cập nhật 2024 - R9" | Khóa đó **không còn trong kho dữ liệu hiện tại** → dựng lại đúng tình huống trên khóa KH-QAW7-HOINGHI bằng luồng người dùng | Không |
| Lịch học ban đầu | 3 buổi | Khóa có sẵn **3 buổi** trong tab Lịch học | Không |
| Điểm danh trước khi thêm buổi | Đã lưu điểm danh, có đủ Có mặt / Vắng có phép / Vắng không phép | Chấm và lưu điểm danh **cả 3 buổi**: học viên Ba = Có mặt / Vắng có phép / Vắng không phép; học viên Hai = Có mặt cả 3 buổi | Không |
| Mốc đối chứng trước khi thêm buổi | Ghi nhận mẫu số đang là 3 | Đọc tab Kết quả trước khi thêm buổi: Ba **2/3 (66.67%)**, Hai **3/3 (100.00%)** — mẫu số 3 | Không |
| Thao tác sinh ra lỗi cũ | Thêm buổi thứ 4 vào tab "Lịch học" **sau khi** đã lưu điểm danh | Thêm buổi 4 (11/05/2026 · 14:00–16:00 · Trực tiếp · "Buổi 4 - QA seed KTDGKQHT_23") qua nút **Thêm buổi học**, không chấm lại điểm danh cho ai | Không |
| Cách đọc lại kết quả | Tải lại trang (bỏ bộ nhớ đệm) rồi mở lại tab "Kết quả" | **Tải lại toàn bộ trang** rồi mới mở lại tab Kết quả và đọc ô Chuyên cần | Không |
| Số cách đo | Note đo 2 cách độc lập: giao diện + nội dung tệp xuất ra | Đo **2 cách**: (1) đọc ô Chuyên cần + phần chú giải trên màn; (2) đọc dữ liệu kết quả mà chính màn hình đó lấy về, so từng con số | Không |
| Phạm vi so sánh | Cùng một bảng đang hiện hai mẫu số khác nhau (1/4 và 1/3) | So **cả hai dòng học viên trong cùng bảng**, trong đó có 1 học viên **không** được chấm lại sau khi thêm buổi | Không |

**Kết luận: 0 GAP** — đúng bản dựng đang chạy, đúng vai trò, đúng trạng thái khóa học, dựng lại đúng trình tự sinh ra lỗi (điểm danh trước, thêm buổi sau, không chấm lại), tải lại trang trước khi đọc và đo bằng 2 cách độc lập.

## Đo lường trực tiếp (05/08/2026, `18.143.165.120.nip.io`, bản dựng V1.0.6, tài khoản `cbnv_tw`)

### Phần "còn lỗi" của note — mẫu số chuyên cần không bám theo tổng số buổi hiện có

- ✅ **Mốc trước khi thêm buổi**: lịch học 3 buổi → tab Kết quả hiện Ba **2/3 (66.67%)**, Hai **3/3 (100.00%)**.
- ✅ **Thêm buổi thứ 4 thành công**, tab "Lịch học" hiển thị đủ **4 buổi**; **không chấm lại điểm danh** cho học viên nào.
  Ảnh: [`../image/KTDGKQHT_23-r1-lich-hoc-4-buoi.png`](../image/KTDGKQHT_23-r1-lich-hoc-4-buoi.png)
- ✅ **Sau khi tải lại trang, mẫu số đã tự cập nhật theo tổng số buổi hiện có**: Ba **2/4 (50.00%)**, Hai **3/4 (75.00%)**. Không còn cảnh mẫu số đứng yên ở 3.
- ✅ **Cùng một bảng chỉ còn MỘT mẫu số** — cả hai học viên đều là mẫu số 4, dù không ai được lưu điểm danh thêm lần nữa sau khi thêm buổi. Không còn cảnh 1/4 nằm cạnh 1/3.
- ✅ **Tỷ lệ đúng công thức**: Ba = (1 có mặt + 1 vắng có phép) / 4 buổi = **50,00%**; Hai = 3 / 4 = **75,00%**.
  Ảnh: [`../image/KTDGKQHT_23-r1-ket-qua-mau-so-4.png`](../image/KTDGKQHT_23-r1-ket-qua-mau-so-4.png)
- ✅ **Cách đo thứ hai cho cùng kết quả** — dữ liệu kết quả của chính khóa đó ghi: học viên Ba có mặt 1 · vắng có phép 1 · vắng không phép 1 · **tổng số buổi 4** · chuyên cần 50,00; học viên Hai có mặt 3 · **tổng số buổi 4** · chuyên cần 75,00. Trùng khớp với những gì đọc trên màn.

### Phần "đã hết lỗi" của note — kiểm lại xem có hồi quy không

- ✅ Ý của dòng KTDGKQHT_20 (mẫu số lấy theo số buổi đã điểm danh) vẫn không tái diễn: học viên Hai được điểm danh 3 buổi nhưng mẫu số vẫn là 4 — đúng tổng số buổi của khóa, không phải số buổi đã điểm danh.
- ✅ Phần chú giải chuyên cần vẫn đọc được đủ số buổi có mặt / vắng có phép / vắng không phép sau khi thêm buổi.

### Kết luận

Ý còn lỗi của phiếu — mẫu số chuyên cần chốt cứng tại thời điểm lưu điểm danh — nay đã hết: thêm buổi vào lịch học rồi tải lại trang thì mẫu số của **mọi** học viên đều nhảy theo tổng số buổi hiện có, tỷ lệ tính đúng công thức, trong cùng bảng không còn hai mẫu số khác nhau → **Pass**.

### Ghi nhận thêm (ngoài phạm vi phiếu — không tự thêm dòng mới vào sheet)

- Khóa học **KH-20260509-006 "Luật đất đai cập nhật 2024 - R9"** mà phiếu dùng làm dữ liệu kiểm tra **không còn tồn tại** trong kho dữ liệu của môi trường nghiệm thu ở thời điểm kiểm tra lại. Đã dựng lại đúng tình huống trên một khóa khác. Chỉ ghi lại để đối tác biết.
- Tab "Thông tin" của khóa hiển thị **"Số buổi: 1"** trong khi tab "Lịch học" đang có 4 buổi — ô này không bám theo lịch học thực tế. Không thuộc phạm vi phiếu, chỉ ghi lại.
- Dữ liệu do kiểm thử tạo: thêm **buổi 4 (11/05/2026, 14:00–16:00)** vào lịch học khóa KH-QAW7-HOINGHI và chấm điểm danh 3 buổi trước đó.
