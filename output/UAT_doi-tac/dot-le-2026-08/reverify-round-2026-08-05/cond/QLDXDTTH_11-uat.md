# QLDXDTTH_11 — đo lại trên môi trường nghiệm thu đối tác (05/08/2026)

Tiêu chí lấy nguyên khối `── CÁCH VERIFY sau Dev fix ──` ở cột `DEV phản hồi lần 1`, dòng 135
(tab `UAT_TGPL Doanh Nghiệp-tuần 2`).

| Điều kiện | Bug gốc (khối CÁCH VERIFY) | Mình test | GAP? |
|---|---|---|---|
| Môi trường | Môi trường nghiệm thu của đối tác | `https://htpldn-uat.ospgroup.vn` — nhãn `HTPLDN · V1.0.7` | Không |
| Vai trò | `cbnv_tw` — CB_NV_TW, Cục Bổ trợ tư pháp - Bộ Tư pháp | `cbnv_tw` · CB_NV_TW · Cục Bổ trợ tư pháp - Bộ Tư pháp · cấp TW | Không |
| Màn hình | Chương trình đào tạo → thẻ "Đề xuất đào tạo" | Đúng thẻ đó (`/dao-tao/chuong-trinh/danh-sach?type=de-xuat`) | Không |
| Điều kiện dữ liệu | ≥1 đề xuất "Mới gửi" thuộc cùng đơn vị | 6 đề xuất "Mới gửi" thuộc Cục Bổ trợ tư pháp - Bộ Tư pháp trước khi đo | Không |
| Bước 1 | Đọc cột "Hành động" ở dòng đề xuất cùng đơn vị, trạng thái "Mới gửi" | Đọc cả 17 dòng của thẻ "Tất cả" | Không |
| Bước 2 | Mở màn chi tiết chính đề xuất đó, đọc vùng thao tác | Mở chi tiết `TKM đề xuất kiểm thử chức năng` | Không |
| Bước 3 | Thực hiện tiếp nhận rồi mở lại danh sách | Tiếp nhận 2 đề xuất (`kiểm thử độc lập test` ở danh sách, `TKM đề xuất kiểm thử chức năng` ở màn chi tiết) rồi tải lại trang | Không |
| Ý phụ tách riêng | Không chấm FAIL vì nút "Gửi đề xuất mới" còn hiện với vai trò cán bộ | Không tính vào kết luận; ghi lại ở phần Ghi nhận thêm | Không |

**Kết luận: 0 GAP → PASS.**

## Đối chiếu từng ý của khối tiêu chí

- Bước 1 · **cột "Hành động" không còn trống**: mọi dòng "Mới gửi" đều có nút **Tiếp nhận** (9/9 dòng),
  mọi dòng "Đã tiếp nhận" đều có nút **Đánh dấu thực hiện** (4/4 dòng). Chỉ các dòng đã đi hết luồng
  ("Đã xử lý", "Đang xử lý", "Đã thực hiện") mới để dấu gạch ngang — đúng bản chất, không còn nút để bấm.
  Vế FAIL "cột Hành động vẫn trống ở dòng đề xuất cùng đơn vị đang ở Mới gửi" **không xảy ra**.
- Bước 2 · **màn chi tiết có vùng thao tác**: mở `TKM đề xuất kiểm thử chức năng` (Mới gửi, cùng đơn vị) →
  ngoài "Quay lại danh sách" còn có nút **Tiếp nhận**. Vế FAIL "màn chi tiết vẫn chỉ có nút quay lại"
  **không xảy ra**.
- Bước 3 · **tiếp nhận được và trạng thái đổi thật**: bấm Tiếp nhận → hộp xác nhận
  "Tiếp nhận đề xuất? — Đề xuất sẽ chuyển sang trạng thái "Đã tiếp nhận"" → xác nhận → thông báo
  "Đã tiếp nhận đề xuất", trạng thái chuyển **Mới gửi → Đã tiếp nhận**. Làm ở cả hai đường:
  nút trên danh sách (`kiểm thử độc lập test`) và nút trong màn chi tiết (`TKM đề xuất kiểm thử chức năng`).
- Bước 3 · **thay đổi còn nguyên sau khi tải lại trang**: tải lại toàn trang danh sách (không phải chuyển
  thẻ) → `kiểm thử độc lập test` = "Đã tiếp nhận", `TKM đề xuất kiểm thử chức năng` = "Đã thực hiện".
- **Đề xuất đi tiếp trong quy trình, không đứng ở "Mới gửi"**: chạy thêm một nấc — bấm
  **Đánh dấu thực hiện** trên đề xuất vừa tiếp nhận → hộp xác nhận "Đánh dấu đề xuất đã thực hiện?" →
  thông báo "Đã đánh dấu thực hiện", trạng thái **Đã tiếp nhận → Đã thực hiện**, còn nguyên sau khi tải lại.

Ảnh: `../image/QLDXDTTH_11-uat-danh-sach-co-nut-hanh-dong.png` ·
`../image/QLDXDTTH_11-uat-chi-tiet-co-nut-tiep-nhan.png`

## Ghi nhận thêm

- Ý phụ mà khối tiêu chí dặn **không chấm FAIL**: trên môi trường này, vai trò cán bộ **không còn** nút
  "Gửi đề xuất mới" ở thẻ Đề xuất đào tạo (thanh công cụ chỉ có Làm mới / lọc lĩnh vực / Xóa bộ lọc /
  Tìm kiếm). Ghi lại để BA biết hiện trạng khi trả lời câu hỏi "cán bộ có được gửi đề xuất không".
- Dữ liệu môi trường thay đổi khi đo (là bước bắt buộc của chính khối tiêu chí, không có đường hoàn tác trên
  giao diện): `kiểm thử độc lập test` Mới gửi → **Đã tiếp nhận**; `TKM đề xuất kiểm thử chức năng`
  Mới gửi → **Đã thực hiện**. Cả hai đều là bản ghi kiểm thử, không phải hồ sơ nghiệp vụ của đối tác.
- Cột "Người đề xuất" của hai bản ghi này hiện dấu gạch ngang — đó là nội dung của phiếu `QLDXDTTH_10`
  (đã chấm Reopen), không thuộc phiếu này.
