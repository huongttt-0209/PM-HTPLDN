# Bảng đối chiếu điều kiện — TKCHTV_01 (row 24) — Tìm kiếm câu hỏi / tư vấn có kết quả

**Kết luận:** Open (Major) — phần Tư vấn nhanh. Phần Kho câu hỏi không còn tái hiện.

Phiếu nêu 2 vế tách bạch, đo riêng từng vế:

- **Bước 2 — Kho câu hỏi** *"Nhập từ khóa có kết quả nhưng hệ thống hiển thị toàn bộ bản ghi hiện có"* → **KHÔNG tái hiện**. Gõ `lao động` trên kho 14 câu hỏi → còn đúng **1 bản ghi** (`QA-20260727-0003`), phân trang đổi thành "Hiển thị 1-1 / 1 kết quả", số đếm trên thẻ đổi thành "Tất cả 1 / Đã duyệt 1 / Chờ duyệt 0". Đúng kết quả mong đợi của phiếu, kể cả phần phân trang 20 bản ghi mỗi trang.
- **Bước 4 — Tư vấn nhanh** *"Nhập từ khóa có kết quả nhưng hệ thống hiển thị 'Không có phiên tư vấn nhanh nào.'"* → **TÁI HIỆN**. → lỗi `BUG-TK-TVN-TIM-KIEM`.

Chấm **Open** vì vế thứ hai tái hiện đúng, mức Major: ô tìm kiếm là đường chính để cán bộ tra phiên, hiện gần như không dùng được theo cách gõ tự nhiên.

| Điều kiện có thể đổi kết quả | Đối tác (evidence `partner-evidence/TKCHTV_01.webm`) | Mình test (env nip.io, 27/07/2026 14:05–14:30) | GAP? |
|---|---|---|:-:|
| Vai trò / tài khoản | Cán bộ nghiệp vụ TW/BN/ĐP theo cột Tác nhân của phiếu; video thao tác trên màn quản trị Kho câu hỏi và Tư vấn nhanh | `cbnv_tw` — CB Nghiệp vụ - Trung ương, BTP · TW. Nằm trong tập tác nhân phiếu ghi | Không |
| Entity + trạng thái (state machine) | Kho câu hỏi: khung video `t012.04s` cho thấy phân trang "Hiển thị 1-20 / 44 kết quả" ⇒ 44 bản ghi, không lọc. Tư vấn nhanh: danh sách phiên ở mọi trạng thái | Kho câu hỏi 14 bản ghi (Tất cả 14 / Đã duyệt 13 / Chờ duyệt 1). Tư vấn nhanh 4 phiên (CB trả lời 3, Hoàn thành 1). Cả hai màn đều ở thẻ "Tất cả", không đặt bộ lọc phụ | Không |
| Dữ liệu tiền đề | Phiếu yêu cầu "Tồn tại bản ghi phù hợp với tiêu chí tìm kiếm". Video gõ `khoi kien` ở Kho câu hỏi, và gõ dở `tkm kiể` ở Tư vấn nhanh (video kết thúc trước khi hiện kết quả) | **Chủ động dựng đúng điều kiện đó thay vì đoán:** chọn từ khóa lấy nguyên văn từ bản ghi đang hiển thị trên màn — `lao động` khớp `QA-20260727-0003` và 2 phiên TVN; `Thủ tục` khớp mở đầu câu hỏi `TVN-20260727-0003`; `TVN-20260727-0001` là mã phiên đang hiện. Nghĩa là bản ghi phù hợp chắc chắn tồn tại | Không |
| Input / filter / giá trị nhập | Gõ từ khóa vào ô tìm kiếm rồi kích hoạt tìm | Gõ vào đúng ô tìm kiếm của từng màn rồi bấm nút tìm của màn đó (Kho câu hỏi: biểu tượng kính lúp; Tư vấn nhanh: nút [Tìm kiếm]). Đo thêm cùng từ khóa ở dạng bỏ dấu và tách chữ để khoanh vùng | Không |

## Artifact real-data (Gate bằng chứng — loại claim: Tìm kiếm / lọc dữ liệu)

- `partner-evidence/TKCHTV_01.webm` (9.381.437 byte) — đã tải và tách 7 khung hình. Khung `t012.04s.jpg` đọc được địa chỉ `?page=1&search=khoi+kien` cùng phân trang "Hiển thị 1-20 / 44 kết quả" ⇒ đúng là kho 44 bản ghi mà từ khóa không lọc. Khung `t030`/`t036` chuyển sang màn Tư vấn nhanh, video dừng giữa lúc đang gõ nên không quay được kết quả của bước 4.
- `bug-reports/image/BUG-TK-kho-cau-hoi-loc-dung-1-ket-qua.png` — đã mở đọc: Kho câu hỏi, ô tìm kiếm `lao động`, bảng còn 1 dòng `QA-20260727-0003`, "Hiển thị 1-1 / 1 kết quả", "20 / trang", thẻ đếm "Tất cả 1 · Đã duyệt 1 · Chờ duyệt (trống)". Đây là bằng chứng vế Kho câu hỏi đã chạy đúng.
- `bug-reports/image/BUG-TK-tv-nhanh-tim-dung-ma-phien-ra-0.png` — đã mở đọc: Tư vấn nhanh, ô tìm kiếm `TVN-20260727-0001`, vùng bảng chỉ có dòng chữ "Không có phiên tư vấn nhanh nào.".
- `bug-reports/image/BUG-TK-tv-nhanh-tu-khoa-co-dau-ra-0.png` — đã mở đọc: cùng màn, ô tìm kiếm `Thủ tục`, vẫn "Không có phiên tư vấn nhanh nào." — trong khi `TVN-20260727-0003` mở đầu bằng đúng cụm đó.

## Phương pháp thứ hai (bắt buộc)

- **Đo lại bằng đường khác giao diện.** Sau khi bấm nút trên màn, gọi thẳng dịch vụ dữ liệu của từng màn với cùng bộ từ khóa để loại khả năng lỗi chỉ nằm ở phần vẽ bảng. Kết quả trùng khít với giao diện: Tư vấn nhanh trả `TVN-20260727-0001` → 0, `Thủ tục` → 0, `lao động` → 0, `động` → 0, nhưng `dong` → 2, `lao` → 2, `Tranh` → 1. Kho câu hỏi trả `lao động` → 1, `động` → 1, `thử việc` → 1, `hợp đồng` → 1. ⇒ Không phải lỗi hiển thị, mà là phần lọc dữ liệu.
- **Đối chứng dương tính trong cùng phiên đăng nhập.** Hai màn dùng chung tài khoản, chung phiên, chung thời điểm. Một màn xử lý đúng cả từ khóa có dấu lẫn cụm nhiều chữ, màn kia không. Loại trừ được các cách giải thích chung như "hệ thống không hỗ trợ tiếng Việt có dấu" hay "môi trường lỗi".
- **Khoanh vùng bằng biến thiên có kiểm soát.** Đổi lần lượt từng yếu tố của từ khóa để biết chính xác cái gì làm hỏng: `Tranh` (1 chữ, không dấu, đầu từ) → khớp; `tranh`/`TRANH` → vẫn khớp (không phân biệt hoa thường); `ranh` (giữa từ) → 0; `động` (có dấu) → 0 còn `dong` → 2; `lao động` (có dấu cách) → 0 còn `lao` → 2. ⇒ Ba yếu tố phá kết quả là **dấu tiếng Việt**, **dấu cách**, và **khớp giữa từ**. Mã phiên thì hoàn toàn ngoài phạm vi tìm (`TVN` → 0, `20260727` → 0, `0001` → 0) dù chữ mời nhập trên ô ghi "Tìm theo mã phiên, câu hỏi...".
- **Đối chiếu đặc tả — trích nguyên văn:** `srs-fr-13-tv-nhanh.md:568` (§3 SCR-X2-03, dòng 4 "Thanh loc"): *"**Tu khoa**. Trang thai SM-TVNHANH. Khoang ngay"* ⇒ màn Tư vấn nhanh bắt buộc lọc được theo từ khóa. `srs-fr-13-tv-nhanh.md:866` (BR-DATA-08, ô "Ngoại lệ"): *"Các entity khác: search by LIKE/index"* ⇒ với `TU_VAN_NHANH`, từ khóa khớp theo chuỗi; `lao động` là chuỗi con nguyên vẹn của *"Tranh chấp lao động giải quyết tại đâu?"* nên phải ra kết quả.
- **Kiểm phần đã đúng để không quy kết quá phạm vi:** phân trang cả hai màn đều "20 / trang", khớp `srs-fr-13-tv-nhanh.md:539` và `:570`. Thẻ phân loại và số đếm của Kho câu hỏi cập nhật theo từ khóa. Vế Kho câu hỏi của phiếu đã đạt đúng kết quả mong đợi, ghi rõ để dev không sửa nhầm sang màn đó.
