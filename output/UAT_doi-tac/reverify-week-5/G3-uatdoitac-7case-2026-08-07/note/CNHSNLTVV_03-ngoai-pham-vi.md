# Ghi nhận NGOÀI phạm vi — phát sinh khi đo CNHSNLTVV_03 (dòng 36)

> BRIEF §4.12: thấy vấn đề ngoài phạm vi case thì **ghi nhận + báo lead**, **không tự thêm dòng sheet mới**.
> Cả 3 mục dưới đây **không ảnh hưởng verdict Pass** của dòng 36.

## N12 — Cổng bắt buộc nhập số CCCD chặn cứng toàn bộ giao diện, không có đường thoát

- **Quan sát:** ngay sau khi đăng nhập `nht_04_ui` (vai trò NHT), hộp thoại **"Cập nhật thông tin bắt buộc"**
  phủ mặt nạ toàn màn: *"Theo quy định mới, bạn cần cung cấp số Căn cước công dân (CCCD) để tiếp tục sử dụng
  hệ thống. Thông tin này chỉ được yêu cầu một lần."*
- Hộp thoại **không có nút đóng / huỷ**, **phím `Escape` không tắt** được (rà DOM: chỉ có duy nhất nút
  `Xác nhận`). Người dùng chưa khai CCCD **không dùng được bất kỳ chức năng nào**.
- Ràng buộc đầu vào bắt buộc **đúng 12 chữ số** ⇒ **không có đường đưa trường này về trống**.
- **Đặc tả `srs-fr-04-chuyen-gia-tvv.md` không mô tả cổng này.** Chưa rõ đây là yêu cầu mới đã được chốt
  ở tài liệu khác hay là hành vi tự phát sinh → **đề nghị BA xác nhận** phạm vi áp dụng và cách xử lý cho
  người dùng chưa có CCCD.
- Ảnh: `image/CNHSNLTVV_03-00-modal-cccd-bat-buoc.png`.
- **Ảnh hưởng dữ liệu env:** tài khoản `nht_04_ui` đã bị đặt `cccd = 000000000004` (giá trị tổng hợp rõ ràng
  là dữ liệu kiểm thử) vì không thể tới màn cần đo nếu bỏ qua bước này.

## N13 — Tệp được ghi vào hồ sơ ngay lúc đính, trước khi bấm Lưu → dễ để lại tệp rác

- Thao tác chọn tệp ở khối *"Thêm chứng chỉ mới"* phát sinh ngay `POST /api/v1/tu-van-viens/{id}/files`
  → **HTTP 201**, và tệp **xuất hiện luôn trong danh sách tệp đính kèm của hồ sơ** dù người dùng **chưa
  bấm Lưu**.
- Trong lượt đo, form đang mở **tự nhảy về tab "Hồ sơ"** một lần, mất toàn bộ nội dung đang nhập; tệp đã
  đính thì **vẫn nằm lại trên hồ sơ**. Đã phải xoá thủ công (`DELETE …/files/{fileId}` → 204).
- ⇒ Người dùng bỏ dở biểu mẫu sẽ vô tình để lại tệp trên hồ sơ mà không có dấu hiệu nào báo.
- Đây là **quan sát về hành vi lưu tệp**, ngoài mệnh đề của dòng 36 → chỉ ghi nhận, chờ lead quyết.

## N14 — Ràng buộc "Số thẻ hành nghề" lệch giữa 3 nơi

| Nơi | Nội dung |
|---|---|
| Máy chủ (thực tế đo) | Từ chối lưu năng lực của hồ sơ loại **Tư vấn viên** khi trường này rỗng — `ERR-VAL-IV-03-10`, *"Số thẻ hành nghề là bắt buộc đối với Tư vấn viên"* |
| `srs-fr-04-chuyen-gia-tvv.md:1507` (màn Thêm/Sửa hồ sơ) | *"Số thẻ hành nghề \| ô văn bản \| **Bắt buộc nếu Loại = Tư vấn viên** (theo NĐ 77/2008 Đ.20)"* — **ủng hộ máy chủ** |
| `srs-fr-04-chuyen-gia-tvv.md:389` (bảng Inputs của FR-IV-04 — chính chức năng cập nhật năng lực) | `so_the_hanh_nghe \| text \| **N** (không bắt buộc)` — **mâu thuẫn** |
| Giao diện form *Cập nhật năng lực* | Ô nhập **không có dấu bắt buộc**, không có lời nhắc trước khi bấm Lưu |

**Hệ quả thực tế quan sát được:** hồ sơ Tư vấn viên cũ đang để trống trường này thì **không lưu được năng lực**
cho tới khi điền; và **điền rồi thì không xoá lại được** (thử đặt lại rỗng → bị từ chối cùng mã lỗi).

→ **Đề nghị BA chốt:** quy tắc `:1507` có áp cho FR-IV-04 không; nếu có thì bảng Inputs `:389` và dấu bắt buộc
trên form cần thống nhất theo. Không chặn bàn giao dòng 36.
