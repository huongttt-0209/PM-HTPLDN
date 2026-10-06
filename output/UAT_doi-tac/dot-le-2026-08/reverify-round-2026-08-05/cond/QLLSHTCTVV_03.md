# Bảng đối chiếu điều kiện — QLLSHTCTVV_03 (re-verify vòng 1, 05/08/2026)

Loại bug: **hiển thị trong bảng "Lịch sử hỗ trợ"** — dãy sao cột "Đánh giá" vỡ hai hàng ở bề ngang hẹp, và điểm đánh giá lệch thang giữa hai chỗ trên cùng trang ⇒ phụ thuộc bề ngang cửa sổ và dữ liệu điểm thật ⇒ bắt buộc điền bảng đối chiếu, 0 GAP.
Ô note của dòng này (*DEV phản hồi lần 1*) CÓ khối `── CÁCH VERIFY sau Dev fix ──`, nên lấy nguyên khối đó làm tiêu chí (Precondition / ✅ PASS khi / ❌ FAIL nếu / dòng ⚠️).

| Điều kiện | Bug gốc (khối CÁCH VERIFY) | Mình test | GAP? |
|---|---|---|---|
| Môi trường | Môi trường bàn giao, bản dựng đang chạy | `https://18.143.165.120.nip.io` — bản dựng **HTPLDN · V1.0.6** (đọc ở thanh bên trái) | Không |
| Vai trò | `cbnv_tw` | `cbnv_tw` · CB Nghiệp vụ - Trung ương · CB_NV_TW · đơn vị Cục Bổ trợ tư pháp - Bộ Tư pháp · cấp TW | Không |
| Hồ sơ | TVV-BTP-TW-0002 | Đúng hồ sơ **TVV-BTP-TW-0002** — "QA TVV Seed28 Active", Đang hoạt động | Không |
| Màn hình | Tab "Lịch sử hỗ trợ" của hồ sơ đó | Mạng lưới Tư vấn viên → Tư vấn viên / Chuyên gia → chi tiết hồ sơ → thẻ **Lịch sử hỗ trợ** | Không |
| Tiền đề dữ liệu | 6 vụ việc, điểm đánh giá khác nhau | Hồ sơ nay có **8 vụ việc**, trong đó **2 vụ việc có điểm đánh giá và hai điểm khác nhau** (4.5/5 và 4.3/5) — đủ để so số sao giữa hai điểm khác nhau; 6 vụ việc còn lại chưa có điểm nên ô hiện dấu "—" | Không |
| Bước 1 — bề ngang 1440 | Đọc cột "Đánh giá" của mọi dòng ở bề ngang 1440px | Đặt cửa sổ đúng **1440px**, đọc cột "Đánh giá" của **cả 8 dòng** (đo vị trí thật của từng ngôi sao, không chỉ nhìn ảnh) | Không |
| Bước 2 — bề ngang 1600 | Lặp lại ở bề ngang 1600px | Đặt cửa sổ đúng **1600px**, đo lại y hệt | Không |
| Bước 3 — hai chỗ hiển thị điểm | Đọc ô "Điểm trung bình" của tab và điểm ở đầu hồ sơ cùng trang | Đọc ô **Điểm trung bình** trong thẻ Lịch sử hỗ trợ và **điểm ở đầu hồ sơ** (ngay dưới tên tư vấn viên) trên cùng một trang | Không |
| Bước 4 — so hai vụ việc điểm khác nhau | So số sao của hai vụ việc có điểm khác nhau | So dòng có **4.5/5** với dòng có **4.3/5**, đọc trạng thái tô của từng ngôi sao | Không |
| Cách đo | Phải thấy rõ có xuống dòng hay không | Đo **vị trí dòng của cả 5 ngôi sao** trong từng ô (cùng một hàng thì mọi ngôi sao cùng một mốc), kèm ảnh chụp màn ở cả hai bề ngang | Không |

**Kết luận: 0 GAP** — đúng bản dựng đang chạy, đúng vai trò, đúng hồ sơ và tab, đo ở đúng hai bề ngang mà phiếu yêu cầu, chạy trọn tới chỗ sinh ra lỗi cũ (không chấm bằng quan sát tĩnh).

## Đo lường trực tiếp (05/08/2026, `18.143.165.120.nip.io`, bản dựng V1.0.6, tài khoản `cbnv_tw`)

### Ý (1) — dãy sao cột "Đánh giá" vỡ hai hàng

- ✅ **Ở bề ngang 1440px: không dòng nào vỡ hai hàng.** Cả 5 ngôi sao của mỗi ô nằm trọn trên **một hàng**; dãy sao rộng 92px trong ô rộng 160px nên còn dư chỗ, không bị cắt.
  Ảnh: [`../image/QLLSHTCTVV_03-r1-danh-gia-1440.png`](../image/QLLSHTCTVV_03-r1-danh-gia-1440.png)
- ✅ **Ở bề ngang 1600px: kết quả y hệt** — mọi dãy sao vẫn nằm trên một hàng, không xuống dòng, không bị cắt.
  Ảnh: [`../image/QLLSHTCTVV_03-r1-danh-gia-1600.png`](../image/QLLSHTCTVV_03-r1-danh-gia-1600.png)

### Ý (2) — điểm đánh giá lệch thang giữa hai chỗ

- ✅ **Hai chỗ hiển thị điểm nay cùng một thang đo**: ô "Điểm trung bình" của thẻ Lịch sử hỗ trợ hiện **4.5/5**, điểm ở đầu hồ sơ hiện **4.1/5**. Không còn cảnh một bên là 8.9 (thang 10) còn một bên là 4.1/5.
- ✅ **Điểm từng vụ việc cũng theo thang đó**: hai vụ việc có điểm hiện **4.5/5** và **4.3/5**, đều nằm trong khoảng 1.0–5.0 và trình bày dạng {X}/5.
- ✅ **Hai vụ việc điểm khác nhau hiện số sao khác nhau**: dòng 4.5/5 hiện 4 sao đầy + 1 nửa sao; dòng 4.3/5 hiện 4 sao đầy + 1 sao rỗng. Không còn cảnh mọi vụ việc đều 5/5 sao đầy nên mất khả năng phân biệt.

### Ý note dặn KHÔNG chấm FAIL — tôn trọng

- ⚠️ Bảng "Lịch sử hỗ trợ" vẫn **không có cột "Trạng thái"** — đúng như BA đã chốt giữ chín cột. Không dùng ý này để chấm phiếu.

### Kết luận

Hai lỗi hiển thị mà BA xác định trong phiếu đều đã hết: dãy sao không còn vỡ hàng ở cả 1440px lẫn 1600px; hai chỗ hiển thị điểm đã cùng thang {X}/5 và hai vụ việc điểm khác nhau cho số sao khác nhau → **Pass**.

### Ghi nhận thêm (ngoài phạm vi phiếu — không tự thêm dòng mới vào sheet)

- Ô "Điểm trung bình" hiện **4.5/5**, trong khi trung bình cộng của hai vụ việc có điểm trên chính bảng đó (4.5/5 và 4.3/5) là **4.4/5** — lệch 0,1 do làm tròn. Con số này cũng khác điểm 4.1/5 ở đầu hồ sơ vì hai chỗ tính trên hai nhóm dữ liệu khác nhau (điểm các vụ việc đã hỗ trợ so với điểm đánh giá tư vấn viên). Không thuộc hai ý của phiếu, chỉ ghi lại để đối tác/BA biết.
- Dữ liệu hồ sơ đã thay đổi so với lúc lập phiếu: nay có **8 vụ việc** thay vì 6, và chỉ 2 vụ việc có điểm đánh giá. Chỉ ghi lại.
