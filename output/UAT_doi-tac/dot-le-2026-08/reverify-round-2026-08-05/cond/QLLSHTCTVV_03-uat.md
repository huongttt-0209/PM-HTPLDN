# QLLSHTCTVV_03 — đo lại trên môi trường nghiệm thu đối tác (05/08/2026)

Tiêu chí lấy nguyên khối ở cột `DEV phản hồi lần 1`, dòng 125 (tab `UAT_TGPL Doanh Nghiệp-tuần 2`).

| Điều kiện | Bug gốc (khối tiêu chí) | Mình test | GAP? |
|---|---|---|---|
| Môi trường | Môi trường nghiệm thu của đối tác (bản dev báo đã sửa 03/08/2026) | `https://htpldn-uat.ospgroup.vn` — nhãn `HTPLDN · V1.0.7` | Không |
| Vai trò | `cbnv_tw` | `cbnv_tw` · CB_NV_TW · cấp TW · Cục Bổ trợ tư pháp | Không |
| Hồ sơ của phản ánh | `TVV-BTP-TW-0002` — có 6 vụ việc, điểm đánh giá khác nhau | Hồ sơ đó **trên môi trường này chỉ có 0 vụ việc, 0 đánh giá** → thay bằng hồ sơ đúng cùng bản chất: `TVV-BTP-TW-0030` (huongcg) — **đúng 6 vụ việc**, có điểm đánh giá khác nhau | Không |
| Màn hình | Tab "Lịch sử hỗ trợ", cột "Đánh giá" | Đúng tab đó, đúng cột đó | Không |
| Bề ngang 1 | 1440px | Đặt cửa sổ đúng 1440px rồi đo | Không |
| Bề ngang 2 | 1600px | Đặt cửa sổ đúng 1600px rồi đo lại | Không |
| Cách đo "vỡ hàng" | Nhìn dãy sao có xuống dòng không | Đo toạ độ thật của từng ngôi sao — đếm số hàng ngang mà 5 sao chiếm; kèm đo bề rộng dãy sao so với bề rộng ô | Không |
| Đối chiếu thang điểm | Ô "Điểm trung bình" của tab vs điểm ở đầu hồ sơ cùng trang | Đọc cả hai chỗ trên cùng một trang, ở hồ sơ có đủ cả hai giá trị (`TVV-BTP-TW-0032`) | Không |
| So hai vụ việc khác điểm | Ít nhất 2 vụ việc điểm khác nhau | 2 vụ việc trên cùng hồ sơ `TVV-BTP-TW-0030`: `4.5/5` và `3.0/5` | Không |
| Phạm vi loại trừ | Bảng KHÔNG cần thêm cột "Trạng thái" — đừng chấm FAIL vì thiếu cột | Không dùng ý cột làm căn cứ chấm | Không |

**Kết luận: 0 GAP → PASS.**

## Đối chiếu từng ý của khối tiêu chí

- **Ở bề ngang 1440px, dãy sao nằm trọn trên MỘT hàng ở mọi dòng có điểm.** Đo toạ độ thật: cả 5 ngôi sao
  của mỗi dòng đều chung một mốc dòng (1 hàng), không dòng nào tách hai hàng. Kích thước cũng đã có dư:
  **dãy sao rộng 92px trong ô rộng 160px** — dư 68px, trong khi phản ánh gốc đo được 132px sao chen trong
  124px lòng ô (thiếu 8px). Tình trạng "4 sao trên, 1 sao dưới" **không còn**.
- **Lặp lại ở bề ngang 1600px cho kết quả y hệt**: vẫn 1 hàng sao/dòng, dãy sao 92px trong ô 160px, không
  dòng nào bị cắt hay đè.
- **Ô "Điểm trung bình" và điểm ở đầu hồ sơ nay CÙNG một thang đo `/5`**: ở hồ sơ `TVV-BTP-TW-0032`, đầu hồ
  sơ hiện **`4.0/5`** và ô Điểm trung bình của tab hiện **`4.2/5`** — cả hai đều là thang 5 và đều kèm hậu
  tố `/5`. Không còn cảnh một chỗ thang 10 (`8.9`) đứng cạnh một chỗ thang 5 (`4.1/5`) như phản ánh gốc.
  Hai con số không bằng nhau tuyệt đối vì theo đặc tả chúng đếm hai tập khác nhau — ô của tab "Lịch sử hỗ
  trợ" là trung bình điểm **của các vụ việc** (`srs-fr-04-chuyen-gia-tvv.md:1578` dòng 22 mục (c):
  "Điểm trung bình: {X}/5"), còn số ở đầu hồ sơ là điểm trung bình **của các phiếu đánh giá tư vấn viên**
  (cùng file, dòng 23 mục (a)). Điều phiếu này đòi — cùng thang đo — đã đạt.
  Hồ sơ chưa có vụ việc nào được chấm thì ô Điểm trung bình hiện dấu gạch, không hiện `0` (`TVV-BTP-TW-0034`:
  đầu hồ sơ `3.7/5`, ô Điểm trung bình `—`).
- **Hai vụ việc điểm khác nhau nay hiện số sao khác nhau**: trên `TVV-BTP-TW-0030`,
  `VV-BTP-TW-20260803-001` hiện **`4.5/5` — 4 sao đầy + 1 sao nửa**, còn `VV-BTP-TW-20260713-001` hiện
  **`3.0/5` — 3 sao đầy**. Tình trạng "mọi vụ việc đều 5/5 sao đầy, mất khả năng phân biệt" **không còn**.
  Điểm từng dòng cũng đã quy về thang 5 kèm hậu tố `/5`, đúng `srs-fr-04-chuyen-gia-tvv.md:795` (trường
  `diem_danh_gia` trình bày 1.0–5.0, một chữ số thập phân).
- **Ý "thiếu cột Trạng thái" không dùng để chấm**: ghi nhận thêm là bảng hiện nay **đã có** cột "Trạng thái"
  (xem phần Ghi nhận thêm), nên phần BA ghi thành yêu cầu cải tiến coi như đã được làm.

Ảnh: `../image/QLLSHTCTVV_03-uat-1440-sao-mot-hang.png` ·
`../image/QLLSHTCTVV_03-uat-1600-sao-mot-hang.png` ·
`../image/QLLSHTCTVV_03-uat-diem-dau-ho-so-va-tab-cung-thang-5.png`

## Ghi nhận thêm

- **Bảng "Lịch sử hỗ trợ" nay có 14 cột, không phải 9 cột như BA chốt.** Ngoài 9 cột thiết kế (Mã vụ việc ·
  Tên vụ việc · Doanh nghiệp · Lĩnh vực · Vai trò · Ngày phân công · Ngày hoàn thành · Kết quả · Đánh giá),
  bảng có thêm **Mã HĐ · Tên hợp đồng · Trạng thái · Ngày bắt đầu · Ngày kết thúc**. Cột "Trạng thái" chính
  là phần BA ghi nhận thành yêu cầu cải tiến; bốn cột hợp đồng có vẻ để dùng chung cho loại bản ghi hợp
  đồng tư vấn. Đây là phần **thêm**, không nằm trong căn cứ trượt của phiếu, nhưng lệch so với câu
  "giữ đúng chín cột" ở `srs-fr-04-chuyen-gia-tvv.md:1578` dòng 22 mục (b) → nên hỏi BA xem có chốt lại
  thiết kế bảng không.
- **Điểm đang nhập ở thang 0–10, chỉ quy đổi khi hiển thị.** Biểu mẫu chấm điểm vụ việc có 3 ô
  "Điểm chất lượng (0-10)", "Điểm thời gian (0-10)", "Điểm thái độ (0-10)"; giá trị lưu lại vẫn là thang 10
  (ví dụ `9.0`, `6.0`, `8.3`), giao diện chia đôi để hiện `/5`. Cách này đủ để phần hiển thị đạt yêu cầu của
  phiếu, nhưng `srs-fr-04-chuyen-gia-tvv.md:795` mô tả trường `diem_danh_gia` là **1.0–5.0**, tức bản thân
  dữ liệu đáng lẽ ở thang 5. Ghi lại để BA/dev quyết có chuẩn hóa ở tầng dữ liệu hay không — không dùng làm
  căn cứ trượt vì phiếu chỉ nói về chỗ hiển thị.
- Dữ liệu phát sinh khi đo (là bước bắt buộc để có 2 vụ việc điểm khác nhau trên cùng hồ sơ): chấm điểm vụ
  việc `VV-BTP-TW-20260803-001` (bản ghi kiểm thử "tkm kiểm thử chức năng 1" của TKM Company, đang
  "Hoàn thành") với 9/9/9 kèm nhận xét mở đầu "QA UAT 05-08" → vụ việc chuyển "Đã đánh giá", điểm trung bình
  của hồ sơ `TVV-BTP-TW-0030` đổi từ `3.0/5` thành `3.8/5`. Không sửa, không xóa bản ghi nào khác.
- Hồ sơ `TVV-BTP-TW-0002` mà phản ánh gốc dùng hiện không còn vụ việc nào trên môi trường này
  (tab "Lịch sử hỗ trợ (0)", "Chưa có đánh giá") nên không đo được trên chính hồ sơ đó.
