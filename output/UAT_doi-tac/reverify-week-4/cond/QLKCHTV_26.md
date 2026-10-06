# Bảng đối chiếu điều kiện — QLKCHTV_26 (row 14) — Cột trái màn trả lời: thanh tiến trình, Thông tin DN, Lịch sử trao đổi

**Kết luận:** Open, BA confirm. Cả 3 ý của đối tác đều **tái hiện đúng**, nhưng căn cứ đặc tả khác nhau:

- **(1) Thanh tiến trình hiển thị lỗi** — tái hiện ✅. Căn cứ: `srs-fr-13-tv-nhanh.md:571` yêu cầu cột trái có thanh tiến trình (C17); chữ bị vỡ dòng từng ký tự là lỗi trình bày. → **Open**
- **(2) Thiếu MST** — tái hiện ✅. Căn cứ: `:571` yêu cầu *"Thong tin DN"*; giao diện có **nhãn "MST" nhưng bỏ trống** dù doanh nghiệp có mã số thuế trong hồ sơ. → **Open**
- **(2b) Thiếu thư điện tử liên hệ + người gửi câu hỏi** — tái hiện ✅. Căn cứ: `:571` chỉ ghi chung *"Thong tin DN"*, không liệt kê trường. → **BA confirm** (BA-14)
- **(3) Thiếu Lịch sử trao đổi** — tái hiện ✅. Căn cứ: `:571` ghi rõ *"**Lich su trao doi (chat bubbles)**"*. → **Open**

| Điều kiện có thể đổi kết quả | Đối tác (evidence `partner-evidence/QLKCHTV_26.jpg`) | Mình test (env nip.io, 27/07/2026 11:56) | GAP? |
|---|---|---|:-:|
| Vai trò / tài khoản | `CB_NV_TW` — "Cán bộ NV Trung ương", BTP · TW (đọc rõ góc phải ảnh) | `cbnv_tw` — CB Nghiệp vụ - Trung ương, BTP · TW — TRÙNG KHỚP | Không |
| Entity + trạng thái (state machine) | Phiên `TVN-QA-20260423-0024`, trạng thái **"Đã gợi ý"**, đang ở màn trả lời 2 cột | Phiên `TVN-20260727-0001`, trạng thái **"CB trả lời"**, cùng màn trả lời 2 cột. **Khác trạng thái nhưng cùng chế độ hiển thị** — cột trái là thành phần tĩnh của chế độ trả lời (`:571` điều kiện hiển thị = *"mode tra loi"*), không phụ thuộc trạng thái. Đã kiểm chứng: cả 2 trạng thái đều cho ra cùng bố cục cột trái | Không |
| Dữ liệu tiền đề | Phiên gắn doanh nghiệp **"Công ty Cổ phần An Khang BNI"** — ảnh cho thấy dòng "MST:" bỏ trống | Phiên gắn doanh nghiệp **"Công ty TNHH QA Reverify R5"** — hồ sơ doanh nghiệp này **CÓ mã số thuế `0198877665`** và **CÓ thư điện tử** (đọc từ `GET /api/v1/doanh-nghieps`). Chọn có chủ đích DN có đủ dữ liệu để loại trừ khả năng "trống vì doanh nghiệp không khai" | Không |
| Input / filter / giá trị nhập | Mở màn trả lời của phiên, đọc cột trái | Mở màn trả lời của phiên, đọc cột trái bằng mã lệnh (đo cả kích thước từng nhãn thanh tiến trình) | Không |

## Artifact real-data (Gate bằng chứng — loại claim: Hiển thị/render + Nội dung dữ liệu)

- `bug-reports/image/BUG-TVN-man-tra-loi-cot-trai.png` — đã mở đọc, thấy rõ cả 3 hiện tượng:
  - Thanh tiến trình: chữ **"Mới" bị bẻ thành 3 dòng "M / ở / i"**, **"Đã gợi ý" thành "Đã / gợi / ý"**, **"CB trả lời" thành "CB / trả / lời"**.
  - Khối "Thông tin Doanh nghiệp": chỉ 2 dòng — `Tên DN: Công ty TNHH QA Reverify R5` và `MST:` **bỏ trống**.
  - Không có mục "Lịch sử trao đổi" nào trên màn.
- Đo kích thước nhãn thanh tiến trình bằng mã lệnh (bằng chứng định lượng, không phụ thuộc cảm nhận):

  Kích thước nhãn (rộng × cao):
  - Mới → **11,9 × 66 px** (vỡ)
  - Đang tìm kiếm → 58,5 × 44 px (bình thường)
  - Đã gợi ý → **28,8 × 66 px** (vỡ)
  - CB trả lời → **33,8 × 66 px** (vỡ)
  - Hoàn thành → 46,8 × 44 px (bình thường)

  Nhãn 3 ký tự "Mới" rộng 11,9 px và cao 66 px ⇒ mỗi ký tự nằm một dòng.
- Quét chữ toàn màn: `coLichSuTraoDoi = false` (không có cụm "Lịch sử trao đổi").

## Phương pháp thứ hai (bắt buộc)

- **Truy tầng dữ liệu để chỉ đúng nơi hỏng (MST):** `GET /api/v1/tu-van-nhanhs/{id}` trả về khối doanh nghiệp **rút gọn chỉ 2 trường**: `"doanhNghiep": {"id": "...", "tenDoanhNghiep": "Công ty TNHH QA Reverify R5"}` — **không có** `maSoThue`, không có `email`, không có người gửi. Trong khi `GET /api/v1/doanh-nghieps` cho cùng doanh nghiệp trả đủ `maSoThue: "0198877665"`, `email: "qa.reverify.r5.186b@example.com"`. ⇒ Giao diện dựng đúng nhãn nhưng **máy chủ không trả dữ liệu**; đề nghị dev bổ sung ở tầng trả dữ liệu chứ không phải sửa giao diện.
- **Đối chứng bố cục để tách nguyên nhân vỡ chữ:** mở phiên `TVN-20260727-0002` ở trạng thái "Hoàn thành" — màn dùng bố cục **1 cột toàn chiều rộng**, thanh tiến trình **hiển thị bình thường trên một dòng** (xem `bug-reports/image/BUG-TVN-danh-gia-thieu-xuat-excel.png`). ⇒ Chữ chỉ vỡ khi thanh tiến trình bị nhồi vào **cột trái hẹp (40%)** của chế độ trả lời, không phải lỗi phông chữ hay lỗi dữ liệu. Đây là thông tin định vị lỗi cho dev.
- **Đối chiếu đặc tả từng thành phần** — `srs-fr-13-tv-nhanh.md:571`, §3 SCR-X2-03 dòng 7: *"| 7 | content (tra loi) | Cot trai (40%) | layout | Ma phien + Trang thai (C06/C17). **Thong tin DN**. Cau hoi DN (card nen nhat). **Lich su trao doi (chat bubbles)** | -- | mode tra loi |"*

  Đối chiếu từng thành phần `:571` với hệ thống thực tế:
  - Mã phiên + Trạng thái (C06/C17) → ✅ có, nhưng thanh tiến trình (C17) vỡ chữ
  - Thông tin DN → ⚠️ có khối, thiếu dữ liệu (MST trống)
  - Câu hỏi DN (thẻ nền nhạt) → ✅ có
  - **Lịch sử trao đổi (bong bóng hội thoại) → ❌ KHÔNG CÓ**
- **Kiểm tra entity xem dữ liệu lịch sử có tồn tại không:** bảng thuộc tính `TU_VAN_NHANH` (`srs-fr-13-tv-nhanh.md:709-718`) chỉ có 1 câu hỏi + 1 nội dung trả lời, **không có bảng lượt trao đổi**. Vậy để dựng được "Lịch sử trao đổi" cần bổ sung cả mô hình dữ liệu ⇒ QA ghi nhận đây là hạng mục cần dev ước lượng, không phải chỉnh giao diện đơn thuần.
