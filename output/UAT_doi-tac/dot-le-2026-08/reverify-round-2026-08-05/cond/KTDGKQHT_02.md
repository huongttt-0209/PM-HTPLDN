# Bảng đối chiếu điều kiện — KTDGKQHT_02 (re-verify vòng 1, 05/08/2026)

Loại bug: **thiếu thông tin buổi học trên màn chấm kết quả học tập** → phụ thuộc dữ liệu điểm danh thật của từng học viên ⇒ bắt buộc điền bảng đối chiếu, 0 GAP.
Ô note của dòng này (*DEV phản hồi lần 1*) CÓ khối `── CÁCH VERIFY sau Dev fix ──`, nên lấy nguyên khối đó làm tiêu chí (Precondition / ✅ PASS khi / ❌ FAIL nếu / dòng ⚠️).

| Điều kiện | Bug gốc (khối CÁCH VERIFY) | Mình test | GAP? |
|---|---|---|---|
| Môi trường | Môi trường bàn giao, bản dựng đang chạy | `https://18.143.165.120.nip.io` — bản dựng **HTPLDN · V1.0.6** (đọc ở thanh bên trái) | Không |
| Vai trò | `cbnv_tw` | `cbnv_tw` · CB Nghiệp vụ - Trung ương · CB_NV_TW · đơn vị Cục Bổ trợ tư pháp - Bộ Tư pháp · cấp TW | Không |
| Màn hình | Khóa học → tab "Kết quả kiểm tra" | Đào tạo, tập huấn → Khóa học → chi tiết khóa → tab **Kết quả** (đi bằng menu bên trái và các thẻ tab, không gõ địa chỉ) | Không |
| Tiền đề — khóa học | Một khóa học có học viên trong danh sách kết quả | Khóa **KH-QAW7-HOINGHI** "QAW7 — Hội nghị đối thoại DN 2026", trạng thái **Đang diễn ra**, có **2 học viên** | Không |
| Tiền đề — đã điểm danh ≥3 buổi | Học viên được điểm danh ít nhất 3 buổi | Khóa có sẵn **3 buổi** trong tab Lịch học; đã tự chấm điểm danh và lưu **cả 3 buổi** cho cả 2 học viên | Không |
| Tiền đề — có đủ loại vắng | Trong đó có ít nhất 1 buổi vắng có phép và 1 buổi vắng không phép | Học viên **QA R3 Mailto Ba**: buổi 1 **Có mặt**, buổi 2 **Vắng có phép**, buổi 3 **Vắng không phép** (mỗi buổi bấm Lưu điểm danh, hệ thống báo "Đã lưu điểm danh") | Không |
| Bước 1 | Mở tab "Điểm danh", ghi lại số buổi có mặt / vắng có phép / vắng không phép / tổng buổi thực tế | Ghi lại từ chính màn Điểm danh: Ba = 1 có mặt · 1 vắng có phép · 1 vắng không phép · tổng 3 buổi; Hai = 3 có mặt · 0 · 0 · tổng 3 buổi | Không |
| Bước 2 | Sang tab "Kết quả kiểm tra", tìm đúng dòng học viên đó | Mở tab **Kết quả**, tìm đúng dòng "QA R3 Mailto Ba" (và đối chiếu thêm dòng "QA R3 Mailto Hai") | Không |
| Bước 3 | Đọc phần thông tin chuyên cần của dòng — ô gộp hoặc phần chú giải khi rê chuột | Đọc ô **Chuyên cần** và **rê chuột vào ô đó** để đọc phần chú giải hiện ra | Không |
| Cách đo | Đối chiếu bốn con số trên màn với số liệu điểm danh, và kiểm công thức tỷ lệ | Đối chiếu từng con số với dữ liệu điểm danh vừa chấm + tự tính lại tỷ lệ theo công thức (có mặt + vắng có phép) / tổng số buổi + ảnh chụp màn có phần chú giải | Không |

**Kết luận: 0 GAP** — đúng bản dựng đang chạy, đúng vai trò và đường đi của phiếu, tiền đề điểm danh còn thiếu đã tự tạo bằng luồng người dùng, chạy trọn tới bước sinh ra lỗi cũ (không chấm bằng quan sát tĩnh).

## Đo lường trực tiếp (05/08/2026, `18.143.165.120.nip.io`, bản dựng V1.0.6, tài khoản `cbnv_tw`)

### Bước 1 — số liệu gốc ở tab "Điểm danh"

- ✅ Chấm và lưu điểm danh đủ 3 buổi, mỗi lần đều nhận thông báo **"Đã lưu điểm danh"**.
- ✅ Số liệu thực tế của học viên **QA R3 Mailto Ba**: có mặt **1** · vắng có phép **1** · vắng không phép **1** · tổng số buổi **3**.
  Ảnh: [`../image/KTDGKQHT_02-r1-diem-danh-buoi-3.png`](../image/KTDGKQHT_02-r1-diem-danh-buoi-3.png)

### Bước 2 + 3 — đọc thông tin chuyên cần ở tab "Kết quả"

- ✅ **Đọc được đủ cả bốn con số** — ô Chuyên cần hiện **"2/3 (66.67%)"** (mẫu số 3 chính là tổng số buổi), rê chuột vào ô hiện chú giải **"Số buổi có mặt: 1 · Số buổi vắng có phép: 1 · Số buổi vắng không phép: 1"**. Không còn cảnh hai con số buổi vắng không hiện ở đâu.
- ✅ **Bốn con số khớp đúng số liệu điểm danh** ở bước 1 (1 · 1 · 1 · 3).
- ✅ **Tỷ lệ chuyên cần tính đúng công thức**: (1 có mặt + 1 vắng có phép) / 3 buổi = **66,67%** — buổi vắng có phép vẫn được tính vào tử số, không bị bỏ ra.
- ✅ Đối chiếu chéo học viên thứ hai **QA R3 Mailto Hai**: ô hiện **"3/3 (100.00%)"**, chú giải **"Số buổi có mặt: 3 · Số buổi vắng có phép: 0 · Số buổi vắng không phép: 0"** — cũng đủ bốn con số và khớp điểm danh.
  Ảnh: [`../image/KTDGKQHT_02-r1-ket-qua-chu-giai-4-con-so.png`](../image/KTDGKQHT_02-r1-ket-qua-chu-giai-4-con-so.png)

### Ý note dặn KHÔNG chấm FAIL — tôn trọng

- ⚠️ Note ghi rõ **không bắt buộc tách thành bốn cột rời**, gộp trong một ô kèm chú giải vẫn tính đạt. Bản đang chạy đúng theo hướng gộp: một ô "x/y (z%)" kèm chú giải khi rê chuột. Không dùng ý này để chấm phiếu.

### Kết luận

Cả ba bước của khối hướng dẫn nghiệm thu đều đạt: đọc được đủ bốn con số buổi học ngay trên màn chấm kết quả, bốn con số khớp dữ liệu điểm danh, tỷ lệ chuyên cần đúng công thức có tính buổi vắng có phép → **Pass**.

### Ghi nhận thêm (ngoài phạm vi phiếu — không tự thêm dòng mới vào sheet)

- Tab "Thông tin" của chính khóa này hiển thị **"Số buổi: 1"** trong khi tab "Lịch học" có 3 buổi (và 4 buổi sau khi thêm). Ô "Số buổi" ở phần thông tin chung không bám theo lịch học thực tế. Không thuộc phạm vi phiếu này, chỉ ghi lại để đối tác/BA biết.
- Dữ liệu do kiểm thử tạo: đã chấm điểm danh 3 buổi cho 2 học viên của khóa **KH-QAW7-HOINGHI** để có đủ trường hợp có mặt / vắng có phép / vắng không phép.
