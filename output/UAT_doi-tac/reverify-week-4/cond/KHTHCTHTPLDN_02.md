# Bảng đối chiếu điều kiện — KHTHCTHTPLDN_02 (row 27) — Điều kiện tìm kiếm / bộ lọc màn CT HTPLDN

**Kết luận:** Open (Medium).

Phiếu ghi *"Không có trường thông tin tìm kiếm theo Đơn vị, Trạng thái"* → **TÁI HIỆN đúng**. Thanh lọc chỉ có: ô tìm theo tên/mã, **một** danh sách chọn mang nhãn "Công bố", và cặp Từ ngày / Đến ngày. → lỗi `BUG-CT-LOC-THIEU-DONVI-TRANGTHAI`.

Đã loại trừ khả năng "danh sách chọn đó chính là Trạng thái nhưng đặt nhãn khác": mở ra chỉ có 2 lựa chọn *Đã công bố* / *Chưa công bố*, tức lọc theo cờ công khai. Hàng thẻ phân loại phía dưới có thể coi là cách lọc trạng thái thay thế, nhưng thiếu **Tạm dừng** và **Đã hủy** — 2 trong 8 trạng thái của máy trạng thái.

| Điều kiện có thể đổi kết quả | Đối tác (evidence `partner-evidence/KHTHCTHTPLDN_02.jpg`) | Mình test (env nip.io, 27/07/2026 14:45–15:05) | GAP? |
|---|---|---|:-:|
| Vai trò / tài khoản | Ảnh chụp cho thấy đăng nhập `CB_NV_TW` ("Cán bộ NV Trung ương"), đơn vị BTP · TW | `cbnv_tw` — CB Nghiệp vụ - Trung ương, BTP · TW. Đo lại lần hai bằng `cbpd_tw` (CB Phê duyệt - Trung ương) để chắc không phải khác biệt do quyền — thanh lọc y hệt | Không |
| Entity + trạng thái (state machine) | Ảnh đính kèm là **màn Tư vấn nhanh** `/tv-nhanh/danh-sach`, không phải màn CT HTPLDN. Bố cục màn CT HTPLDN của đối tác đọc được ở ảnh case kế bên `KHTHCTHTPLDN_03.jpg`: thanh lọc có ô tìm, 1 danh sách chọn "Công bố", Từ ngày, Đến ngày | Màn `/ct-htpldn/danh-sach`, 8 chương trình phân bố 4 trạng thái (Đã duyệt 5, Đã công bố 1, Đang thực hiện 1, Hoàn thành 1), thẻ đang chọn "Tất cả" | Không |
| Dữ liệu tiền đề | Phiếu chỉ yêu cầu "Đăng nhập hệ thống thành công" — case này kiểm thành phần giao diện, không phụ thuộc dữ liệu | Vẫn dựng đủ điều kiện để phép đo có ý nghĩa: dữ liệu trải trên **2 đơn vị khác nhau** và 4 trạng thái, nên nếu có bộ lọc Đơn vị / Trạng thái thì chúng phải có tác dụng thấy được | Không |
| Input / filter / giá trị nhập | Mở màn rồi đọc thanh lọc | Đọc thanh lọc bằng mã lệnh (đếm ô nhập, đếm danh sách chọn, lấy nhãn) thay vì chỉ nhìn ảnh, rồi mở danh sách chọn duy nhất để đọc các lựa chọn bên trong | Không |

## Artifact real-data (Gate bằng chứng — loại claim: Thành phần giao diện)

- `partner-evidence/KHTHCTHTPLDN_02.jpg` — đã mở đọc. **Ảnh này gắn nhầm case**: nội dung là màn Tư vấn nhanh (`/tv-nhanh/danh-sach`) với thanh lọc "Tìm theo mã phiên, câu hỏi...", Trạng thái, Từ ngày, Đến ngày, [Xóa bộ lọc], [Tìm kiếm] — không liên quan tới màn Chương trình HTPLDN mà phiếu đang nói. Đã ghi rõ trong hồ sơ lỗi để đối tác đính chính, nhưng **không lấy đó làm lý do bác case** vì nội dung phản ánh vẫn đúng khi kiểm trên đúng màn.
- `partner-evidence/KHTHCTHTPLDN_03.jpg` — đã mở đọc, dùng thay thế: đây mới là màn `/ct-htpldn/danh-sach` của đối tác. Thanh lọc trong ảnh trùng khít với đo được ở môi trường QA — ô tìm, 1 danh sách chọn "Công bố", Từ ngày (13/07/2026), Đến ngày, [Xóa bộ lọc], [Tìm kiếm].
- `bug-reports/image/BUG-CT-o-loc-duy-nhat-la-cong-bo.png` — đã mở đọc: danh sách chọn duy nhất đang mở, đúng 2 lựa chọn *"Đã công bố"* và *"Chưa công bố"*.
- `bug-reports/image/BUG-CT-danh-sach-thieu-loc-donvi-trangthai-va-cot-linhvuc.png` — đã mở đọc: toàn cảnh thanh lọc + hàng thẻ phân loại 7 mục, không có Tạm dừng, không có Đã hủy.

## Phương pháp thứ hai (bắt buộc)

- **Đọc thành phần bằng mã lệnh thay vì nhìn ảnh** — tránh kết luận "không có" chỉ vì thành phần nằm ngoài khung nhìn. Kết quả: ô nhập = `["Tìm theo tên hoặc mã CT...", "Từ ngày", "Đến ngày"]`; danh sách chọn = `["Công bố"]`. Quét chữ toàn màn không có cụm "Đơn vị" ở vùng lọc (chỉ có ở tiêu đề cột bảng).
- **Mở danh sách chọn để loại giả thuyết "Trạng thái bị đặt nhãn sai"** — đây là phép thử phân biệt. Nếu là bộ lọc Trạng thái thì bên trong phải có 8 trạng thái vòng đời. Thực tế chỉ 2 lựa chọn *Đã công bố* / *Chưa công bố* ⇒ đúng là bộ lọc cờ công khai, không thay thế được bộ lọc Trạng thái.
- **Kiểm phía máy chủ để khoanh vùng trách nhiệm** — gọi thẳng dịch vụ dữ liệu của màn: không lọc → 8 chương trình; lọc theo một đơn vị cụ thể → 7; lọc `trangThai=DA_DUYET` → 5; lọc `trangThai=TAM_DUNG` → 0. ⇒ Máy chủ đã nhận và xử lý đúng cả hai tham số. Việc còn thiếu nằm hoàn toàn ở phần giao diện.
- **Đo lại bằng tài khoản khác vai trò** — đăng nhập `cbpd_tw` (CB Phê duyệt - Trung ương) rồi đọc lại thanh lọc: vẫn đúng 1 danh sách chọn "Công bố", không có Đơn vị, không có Trạng thái. ⇒ Không phải khác biệt do phân quyền.
- **Đối chiếu đặc tả — trích nguyên văn:** `srs-fr-15-ct-htpldn.md:1110` — *"| 4 | filter-bar | **Don vi** | select | Auto phân quyền theo đơn vị (BR-AUTH-05) | change -> filter | **luon hien thi** |"*; `:1111` — *"| 5 | filter-bar | **Trang thai** | select | **Tat ca trang thai SM-KH-CTHTPL** | change -> filter | **luon hien thi** |"*.
- **Đối chiếu máy trạng thái để lượng hóa thiệt hại:** `srs-fr-15-ct-htpldn.md:1173-1180` liệt kê 8 trạng thái, gồm `TAM_DUNG` ("Tạm dừng", `:1178`) và `HUY` ("Đã hủy", `:1180`). Hàng thẻ phân loại trên màn chỉ có 6 trạng thái + "Tất cả" ⇒ chương trình đang tạm dừng hoặc đã hủy không có đường nào lọc ra từ giao diện.
- **Kiểm phần đã đúng để không quy kết quá phạm vi:** ô tìm theo tên/mã (`:1109`) và cặp Từ ngày / Đến ngày (`:1112`) đều có và hoạt động; phân trang "20 / trang" khớp `:1114`. Chỉ thiếu đúng 2 thành phần ở `:1110` và `:1111`.
