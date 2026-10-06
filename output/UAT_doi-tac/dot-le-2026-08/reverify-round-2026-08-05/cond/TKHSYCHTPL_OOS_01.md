# Bảng đối chiếu điều kiện — TKHSYCHTPL_OOS_01 (re-verify vòng 1, 05/08/2026)

Loại bug: **cột "Cảnh báo thời hạn" ở màn danh sách vụ việc hiện nhãn không có trong đặc tả** → phụ thuộc dữ liệu hồ sơ đã đóng có mức cảnh báo đang lưu ⇒ bắt buộc điền bảng đối chiếu, 0 GAP.
Ô note của dòng này (*DEV phản hồi lần 1*) CÓ khối `── CÁCH VERIFY sau Dev fix ──`, nên lấy nguyên khối đó làm tiêu chí (Precondition / ✅ PASS khi / ❌ FAIL nếu / dòng ⚠️).

| Điều kiện | Bug gốc (khối CÁCH VERIFY) | Mình test | GAP? |
|---|---|---|---|
| Môi trường | Môi trường bàn giao, bản dựng đang chạy | `https://18.143.165.120.nip.io` — bản dựng **HTPLDN · V1.0.6** (đọc ở thanh bên trái) | Không |
| Vai trò | `cbnv_tw` — Cán bộ nghiệp vụ Trung ương, đơn vị Bộ Tư pháp | `cbnv_tw` · CB Nghiệp vụ - Trung ương · CB_NV_TW · đơn vị Cục Bổ trợ tư pháp - Bộ Tư pháp · cấp TW | Không |
| Màn hình | Vụ việc HTPL → danh sách | Vụ việc HTPL → **Danh sách** (đi bằng menu bên trái) | Không |
| Tiền đề dữ liệu | Hai hồ sơ đã đóng VV-BTP-TW-20260712-006 (Từ chối) và VV-BTP-TW-20260712-005 (Hoàn thành) đang lưu mức cảnh báo "Sắp hết hạn" | Cả hai hồ sơ **vẫn còn** trong kho, đúng trạng thái Từ chối / Hoàn thành, ngày tiếp nhận 12/07/2026, thời hạn xử lý 31/07/2026 | Không |
| Bước 1 | Đặt bộ lọc "Mức SLA" = "Sắp hết hạn" | Mở ô **Mức SLA**, chọn **Sắp hết hạn**, bấm **Tìm kiếm** (các ô lọc khác để trống, thẻ "Tất cả") | Không |
| Bước 2 | Đọc cột "Cảnh báo thời hạn" của từng dòng kết quả | Đọc cột **Cảnh báo thời hạn** (cột đứng sau "Thời hạn xử lý") của từng dòng, ở bề ngang **1920px** để thấy trọn cả mã vụ việc lẫn cột này trong một khung hình | Không |
| Bước 3 | Bỏ lọc, duyệt danh sách và đọc cột này ở cả hồ sơ đang xử lý lẫn hồ sơ đã đóng | Bấm **Xóa bộ lọc**, đặt **100 dòng/trang** để xem trọn **41 hồ sơ** trong một lượt, đọc cột này ở mọi dòng | Không |
| Cách đo | Đối chiếu nhãn hiển thị với bốn mức đã định nghĩa | Liệt kê **toàn bộ giá trị khác nhau** đang xuất hiện ở cột đó trên cả 41 hồ sơ rồi đối chiếu với bốn mức Bình thường / Sắp hết hạn / Quá hạn / Quá hạn nghiêm trọng | Không |
| Cách đo thứ hai | Note đo 2 chiều: ảnh chụp màn + dữ liệu danh sách trả về | Đo **2 cách**: đọc thẳng ô trên bảng + đối chiếu với mức cảnh báo đang lưu của từng hồ sơ | Không |

**Kết luận: 0 GAP** — đúng bản dựng đang chạy, đúng vai trò và màn hình, hai hồ sơ tiền đề còn nguyên, chạy trọn cả ba bước tới chỗ sinh ra lỗi cũ (không chấm bằng quan sát tĩnh), đo bằng 2 cách.

## Đo lường trực tiếp (05/08/2026, `18.143.165.120.nip.io`, bản dựng V1.0.6, tài khoản `cbnv_tw`)

### Bước 1 + 2 — lọc "Mức SLA" = "Sắp hết hạn"

- ✅ Bộ lọc trả về đúng **2 hồ sơ** như phiếu mô tả: VV-BTP-TW-20260712-006 (Từ chối) và VV-BTP-TW-20260712-005 (Hoàn thành).
- ✅ **Cột "Cảnh báo thời hạn" của cả 2 dòng nay hiện "Sắp hết hạn"** — **không còn nhãn "Đã hoàn thành"**. Bộ lọc và cột hiển thị nay nói cùng một điều, không còn cảnh dễ hiểu nhầm bộ lọc trả về sai bản ghi.
- ✅ Cột "Trạng thái" vẫn hiện đúng "Từ chối" / "Hoàn thành" — hai cột không bị lẫn vào nhau.
  Ảnh: [`../image/TKHSYCHTPL_OOS_01-r1-loc-sap-het-han.png`](../image/TKHSYCHTPL_OOS_01-r1-loc-sap-het-han.png)

### Bước 3 — bỏ lọc, duyệt toàn bộ danh sách

- ✅ Xem trọn **41 hồ sơ** trong một trang. Toàn bộ nhãn xuất hiện ở cột "Cảnh báo thời hạn" chỉ gồm: **"Bình thường"** (có dòng kèm thêm phần đếm ngược "còn N ngày LV"), **"Sắp hết hạn"**, **"Quá hạn"** (kèm "3 ngày LV"). **Không còn nhãn "Đã hoàn thành"** và không có nhãn nào khác ngoài các mức đã định nghĩa.
- ✅ Hồ sơ **đang xử lý** và hồ sơ **đã đóng** đều hiển thị mức cảnh báo bình thường: ví dụ VV-BTP-TW-20260730-001 (Đã đánh giá, thời hạn 20/08/2026) hiện **"Bình thường"**; hai hồ sơ đã đóng ở bước 1 hiện **"Sắp hết hạn"**.
- ✅ **Cách đo thứ hai cho cùng kết quả**: đối chiếu với mức cảnh báo đang lưu của từng hồ sơ — mọi hồ sơ đều đang lưu một trong ba mức Bình thường / Sắp hết hạn / Quá hạn, và nhãn trên màn khớp đúng mức đang lưu ở mọi dòng có hiển thị nhãn.

### Ý note dặn KHÔNG chấm FAIL — tôn trọng

- ⚠️ Hồ sơ trạng thái **Hoàn thành hiện "Sắp hết hạn"** ở cột này — note dặn rõ đây là kết quả ĐÚNG theo đặc tả hiện hành (mức cảnh báo giữ nguyên tại thời điểm hồ sơ đóng), không chấm FAIL và không mở bug mới vì điều đó. Đã tôn trọng.
- ⚠️ Hai ý còn lại BA đã chốt là đúng (giữ nguyên mức cảnh báo của hồ sơ đã đóng; bộ lọc trả về hồ sơ đã đóng) — không dùng để chấm phiếu.

### Kết luận

Nhãn "Đã hoàn thành" — giá trị không tồn tại trong hệ thống — đã bị gỡ khỏi cột "Cảnh báo thời hạn"; hai hồ sơ đã đóng ở bước 1 hiện đúng "Sắp hết hạn", khớp với chính bộ lọc đã chọn; duyệt hết 41 hồ sơ không còn nhãn nào ngoài các mức đã định nghĩa → **Pass**.

### Ghi nhận thêm (ngoài phạm vi phiếu — không tự thêm dòng mới vào sheet)

- **19/41 hồ sơ đang để trống (dấu "—") ở cột "Cảnh báo thời hạn"**, trong đó có 11 hồ sơ đã đóng (Hoàn thành / Đã đánh giá). Đây **không phải hệ quả của việc hồ sơ đã đóng**: đúng 19 hồ sơ đó cũng đang để trống cột "Thời hạn xử lý" và cột "Tên doanh nghiệp" (nhóm dữ liệu cũ, thiếu thông tin nền), và tình trạng này gặp ở cả hồ sơ chưa đóng (Mới tạo, Đã duyệt). Mọi hồ sơ đã đóng **có thời hạn xử lý** đều hiển thị mức cảnh báo bình thường. Ghi lại để đối tác/BA cân nhắc mở phiếu riêng cho nhóm hồ sơ thiếu dữ liệu nền.
- Nhãn ở cột này có kèm phần đếm ngược ("Bình thường · còn 14 ngày LV", "Quá hạn · 3 ngày LV") ngoài tên mức. Không thuộc phạm vi phiếu, chỉ ghi lại.
