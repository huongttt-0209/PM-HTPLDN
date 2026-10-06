# Bảng đối chiếu điều kiện — TKKHCTHTPL_02 (row 33) — Thông báo khi tìm không có kết quả

**Kết luận:** Open (Minor).

Phiếu mong *"Không có kết quả, hệ thống hiển thị \"Không tìm thấy chương trình phù hợp\""*, thực tế *"Hệ thống hiển thị \"Trống\""* → **TÁI HIỆN đúng**, và lần này **đặc tả đứng về phía đối tác**: `srs-fr-15-ct-htpldn.md:381` quy định mã `INF-CT-TK-01` với đúng câu chữ đó, thuộc **FR-XI-02: Tìm kiếm CT HTPL** (`:331`) trên **màn SCR-XI-01** (`:337`) — đúng chức năng, đúng màn. → lỗi `BUG-CT-TIM-KHONG-KET-QUA-TRONG`.

Đo thêm còn thấy hệ thống dùng **cùng một chữ "Trống"** cho hai tình huống khác bản chất: *chưa có dữ liệu nào* và *có dữ liệu nhưng lọc không khớp*.

| Điều kiện có thể đổi kết quả | Đối tác (evidence `partner-evidence/TKKHCTHTPL_02.jpg`) | Mình test (env nip.io, 27/07/2026 14:33–14:40) | GAP? |
|---|---|---|:-:|
| Vai trò / tài khoản | Ảnh cho thấy `CB_NV_TW` ("Cán bộ NV Trung ương"), đơn vị BTP · TW | `cbnv_tw` — CB Nghiệp vụ - Trung ương, BTP · TW. Trùng khít | Không |
| Entity + trạng thái (state machine) | Màn `/ct-htpldn/danh-sach`, thẻ "Tất cả", đang đặt bộ lọc và ra 0 dòng | Màn `/ct-htpldn/danh-sach`, thẻ "Tất cả" (8 chương trình khi chưa lọc), đặt bộ lọc cho ra 0 dòng. Đo thêm thẻ "Dự thảo" (0 bản ghi, **không** đặt bộ lọc) để phân biệt hai loại rỗng | Không |
| Dữ liệu tiền đề | Phiếu yêu cầu "Không tồn tại bản ghi phù hợp với tiêu chí tìm kiếm". Đối tác lọc `keyword=CT-20260720-0001` cộng cờ đã công bố → 0 dòng | Danh sách **có** 8 chương trình rồi mới lọc cho về 0 — đúng tình huống "có dữ liệu nhưng không khớp" mà phiếu mô tả, chứ không phải danh sách rỗng sẵn. Đây là điều kiện bắt buộc để phép đo có ý nghĩa | Không |
| Input / filter / giá trị nhập | Nhập mã `CT-20260720-0001` + chọn "Đã công bố" rồi bấm Tìm kiếm (đọc được từ địa chỉ trang trong ảnh) | Nhập `KHONGTONTAI-XYZ-999` rồi bấm [Tìm kiếm]. **Khác giá trị nhập nhưng cùng loại tình huống** — cả hai đều là bộ lọc không khớp bản ghi nào; mã của đối tác không tồn tại trên môi trường QA nên dùng chuỗi chắc chắn không khớp để tạo đúng tình huống đó | Không |

## Artifact real-data (Gate bằng chứng — loại claim: Thông báo hiển thị)

- `partner-evidence/TKKHCTHTPL_02.jpg` — đã mở đọc: địa chỉ trang ghi rõ `?keyword=CT-20260720-0001&laCongBo=true&page=1`; ô tìm kiếm chứa `CT-20260720-0001`; danh sách chọn hiện *"Đã công bố"*; thân bảng có hình hộp rỗng kèm chữ **"Trống"**; nút [Xuất Excel] bị làm mờ. Trùng khít với môi trường QA.
- `bug-reports/image/BUG-CT-tim-khong-ket-qua-hien-trong.png` — đã mở đọc: cùng màn, từ khóa `KHONGTONTAI-XYZ-999`, thẻ "Tất cả 8" vẫn đếm 8 (chứng tỏ dữ liệu có sẵn), thân bảng 0 dòng với đúng hình hộp rỗng và chữ **"Trống"**, nút [Xuất Excel] cũng bị làm mờ.

## Phương pháp thứ hai (bắt buộc)

- **Đọc chuỗi hiển thị bằng mã lệnh thay vì đọc từ ảnh.** Khối rỗng trả về chữ mô tả đúng bằng `"Trống"`; quét toàn bộ chữ trên màn thì chuỗi `"Không tìm thấy chương trình phù hợp"` **không xuất hiện ở bất kỳ đâu**. Cách này loại khả năng câu thông báo có hiện nhưng bị khuất hoặc bị cuộn ra ngoài khung nhìn.
- **Phép thử phân biệt hai loại rỗng — đây là chỗ lộ thêm vấn đề.** Bấm [Xóa bộ lọc] rồi chuyển sang thẻ **Dự thảo** (0 bản ghi, ô tìm kiếm đã rỗng): thân bảng hiện **y hệt** chữ `"Trống"`. ⇒ Hệ thống không phân biệt *chưa có dữ liệu* với *lọc không khớp*, trong khi hai tình huống này dẫn tới hành động khác nhau của cán bộ.
- **Loại giả thuyết "tìm kiếm hỏng nên mới ra rỗng".** Gọi thẳng dịch vụ dữ liệu của màn: từ khóa không khớp → HTTP 200, tổng 0; từ khóa khớp thật `CT-20260724-0001` → tổng 1; không lọc → tổng 8. ⇒ Chức năng tìm kiếm chạy **đúng**, số liệu khớp màn hình. Đây thuần túy là lỗi câu thông báo, không phải lỗi tìm kiếm — khác hẳn màn Tư vấn nhanh ở Luồng 5.
- **Xác định lớp cần sửa:** phía máy chủ trả về trường thông báo **rỗng** khi không có kết quả, nên câu chữ phải bổ sung ở lớp hiển thị. Ghi rõ để dev không mất công sửa nhầm bên xử lý dữ liệu.
- **Đối chiếu đặc tả — trích nguyên văn + kiểm phạm vi:** `srs-fr-15-ct-htpldn.md:381` — *"| E1 | Không có kết quả | INF-CT-TK-01 | \"Không tìm thấy chương trình phù hợp\" | INFO |"*. Kiểm phạm vi của dòng này: nó nằm trong mục **FR-XI-02: Tìm kiếm CT HTPL (UC161)** bắt đầu ở `:331`, khai báo **Màn hình:** SCR-XI-01 ở `:337`, và mô tả ở `:340` là *"Tìm kiếm và lọc chương trình HTPLDN theo từ khóa, đơn vị, trạng thái, khoảng ngày. Kết quả phân trang, read-only."* ⇒ Đúng chức năng và đúng màn đang đo, nên chuỗi này áp dụng trực tiếp.
- **Bước kiểm phạm vi trên là bắt buộc, không phải thủ tục thừa.** Ở `TKCHTV_02` (Luồng 5) cũng có mã thông báo mang chữ gần giống, nhưng khi tra phạm vi thì nó gắn với chức năng khác chứ không phải màn danh sách, và chuỗi đối tác mong đợi không tồn tại trong SRS v3.5 → phải chuyển BA. Cùng một dạng khiếu nại nhưng hai kết luận ngược nhau; điểm phân biệt là phạm vi của mã thông báo chứ không phải bản thân câu chữ.
- **Ghi nhận một điểm hệ thống làm hợp lý, để không quy kết quá phạm vi:** khi 0 kết quả, nút [Xuất Excel] tự bị làm mờ. `:403` quy định trường hợp không có dữ liệu để xuất phải báo `INF-XI-02-XL-01`; việc chặn trước bằng cách làm mờ nút đạt được cùng mục đích là không cho xuất tệp rỗng, nên QA **không** chấm lỗi điểm này.
