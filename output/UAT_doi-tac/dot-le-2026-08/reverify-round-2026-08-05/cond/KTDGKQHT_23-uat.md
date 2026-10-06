# KTDGKQHT_23 — đo lại trên môi trường nghiệm thu đối tác (05/08/2026)

Tiêu chí lấy nguyên khối ở cột `DEV phản hồi lần 1`, dòng 149 (tab `UAT_TGPL Doanh Nghiệp-tuần 2`).

| Điều kiện | Bug gốc (khối tiêu chí) | Mình test | GAP? |
|---|---|---|---|
| Môi trường | Môi trường nghiệm thu của đối tác (bug đo trên bản V1.0.5) | `https://htpldn-uat.ospgroup.vn` — nhãn `HTPLDN · V1.0.7` | Không |
| Vai trò | `cbnv_tw` | `cbnv_tw` · CB_NV_TW · cấp TW · Cục Bổ trợ tư pháp | Không |
| Khóa học của phản ánh | `KH-20260509-006` — Đang diễn ra, 6 học viên, lịch học 4 buổi | Đúng khóa đó, đúng trạng thái, 6 học viên, 4 buổi lúc bắt đầu đo | Không |
| Kịch bản gốc | Điểm danh xong rồi mới thêm buổi học | Chạy đúng thứ tự đó ở **2 khóa**: khóa mới `KH-20260525-001` (lưu điểm danh xong mới thêm buổi) và chính khóa `KH-20260509-006` (thêm buổi thứ 5) | Không |
| Màn hình đọc kết quả | Tab "Kết quả" của khóa | Đúng tab đó | Không |
| Cách đo thứ 2 | Mở nội dung tệp DOCX xuất từ nút [Xuất DOCX], đọc cột "Tổng số buổi" | Bấm đúng nút đó, giải nén tệp và đọc nội dung thật | Không |
| Ngưỡng chuyên cần | 80% | Khóa đang để 80% | Không |

**Kết luận: 0 GAP → PASS.**

## Đối chiếu từng ý của khối tiêu chí

- **Phép thử quyết định trên dữ liệu mới hoàn toàn** (khóa `KH-20260525-001`, 3 buổi, 1 học viên):
  lưu điểm danh trước (học viên "Vắng có phép" 1 buổi) → tab Kết quả hiện `1/3 (33.33%)`, đúng mẫu số 3.
  Sau đó **thêm buổi thứ 4** → tab Kết quả tự đổi thành **`1/4 (25.00%)`** — đúng bằng con số mà phần
  Kết quả mong đợi của phiếu nêu ("học viên Vắng có phép 1 buổi cũng 25.00%"). Mẫu số đã bám theo tổng số
  buổi hiện có của khóa.
- **Chạy lại trên chính khóa của phản ánh** (`KH-20260509-006`): thêm buổi thứ 5 → **cả 6/6 học viên** chuyển
  sang mẫu số **5**, kể cả 5 học viên trước đó đang kẹt ở mẫu số 3:
  `2/5 (40.00%)` · `1/5 (20.00%)` · `0/5 (0.00%)` · `1/5 (20.00%)` · `1/5 (20.00%)` · `0/5 (0.00%)`.
  Tình trạng "cùng một bảng hiện hai mẫu số khác nhau" **không còn**.
- **Công thức đúng BR-KQ-02** — (số buổi Có mặt + số buổi Vắng có phép) / tổng số buổi × 100:
  tester 1 có 1 buổi Có mặt + 1 buổi Vắng có phép → (1+1)/5 = 40.00% ✔;
  tester 5 có 0 Có mặt + 1 Vắng có phép → 1/5 = 20.00% ✔; tester 3 và 6 đều 0 → 0.00% ✔.
- **Cách đo thứ 2 — nội dung tệp DOCX xuất ra**: bấm nút [Xuất DOCX] trên tab Kết quả, giải nén tệp và đọc
  nội dung thật. Cột **"Tổng số buổi" ghi 5 cho cả 6 học viên**, cột "Tỉ lệ chuyên cần (%)" ghi
  `40.00 · 20.00 · 0.00 · 20.00 · 20.00 · 0.00` — khớp đúng với màn hình. Ở phản ánh gốc, chính cột này ghi
  4 cho học viên 1 và 3 cho 5 học viên còn lại; nay đồng nhất.
- **Tác động nghiệp vụ đã hết**: mẫu số không còn nhỏ hơn thực tế nên tỷ lệ chuyên cần không bị đẩy cao oan
  so với ngưỡng 80%.

Ảnh: `../image/KTDGKQHT_23-uat-mau-so-bam-theo-so-buoi-moi.png` (khóa dữ liệu mới) ·
`../image/KTDGKQHT_23-uat-ca-6-hoc-vien-cung-mau-so.png` (khóa của phản ánh)

## Ghi nhận thêm — điểm cần dev/BA biết

- **Bản ghi kết quả tạo TRƯỚC bản vá không tự sửa khi chỉ mở xem.** Lúc bắt đầu đo, `KH-20260509-006` có 4
  buổi trong Lịch học nhưng tab Kết quả vẫn hiện `2/4` cho học viên 1 và `x/3` cho 5 học viên còn lại — đúng
  y như phản ánh gốc. Chỉ khi lịch học của khóa **thay đổi lần kế tiếp** (thêm buổi thứ 5) thì cả 6 dòng mới
  được tính lại. Nghĩa là bản vá đã đúng, nhưng dữ liệu cũ còn kẹt số sai cho tới lần đổi lịch tiếp theo.
  Đề nghị dev chạy một lượt tính lại cho các khóa đã điểm danh trước bản vá, kẻo cán bộ vẫn đọc phải số cũ.
- Dữ liệu phát sinh khi đo (là bước bắt buộc của chính kịch bản): thêm 1 buổi vào `KH-20260525-001`
  (26/07/2026) và 1 buổi vào `KH-20260509-006` (16/02/2026 13:00–15:00); lưu lại điểm danh buổi 15/07/2026
  của `KH-20260525-001` **giữ nguyên** lựa chọn cũ ("Vắng có phép"), không đổi kết quả điểm danh của ai.
- Ghi nhận thêm khi thao tác: màn Thêm buổi học chặn đúng hai trường hợp sai — ngày ngoài khoảng của khóa
  ("Ngày học phải nằm trong khoảng 15/02/2026 – 17/02/2026 của khóa học") và trùng giờ với buổi đã có.
