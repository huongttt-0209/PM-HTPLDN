# Bảng đối chiếu điều kiện — TKKHCTHTPL_01 (row 32) — Tiêu chí tìm kiếm CT + phân trang

**Kết luận:** Open (Medium) + BA confirm.

Phiếu ghi *"Thiếu trường thông tin tìm kiếm theo đơn vị quản lý, lĩnh vực"*. Tách 2 vế vì căn cứ khác hẳn nhau:

- **Thiếu lọc Đơn vị** → **TÁI HIỆN + có căn cứ**. `srs-fr-15-ct-htpldn.md:353` liệt kê `don_vi_id` là dữ liệu đầu vào của chức năng tìm kiếm; `:1110` quy định ô chọn Đơn vị trên thanh lọc, điều kiện hiển thị *"luon hien thi"*. → gộp vào lỗi `BUG-CT-LOC-THIEU-DONVI-TRANGTHAI`.
- **Thiếu lọc Lĩnh vực** → **TÁI HIỆN nhưng KHÔNG có căn cứ**. Bảng dữ liệu đầu vào của FR-XI-02 (`:352`–`:356`) chỉ có 5 mục và không có lĩnh vực; thanh lọc `:1109`–`:1112` cũng vậy. → chuyển BA-21.

Phần **kết quả mong đợi** của phiếu — *"hiển thị danh sách với phân trang 20 chương trình mỗi trang"* — thì hệ thống làm **ĐÚNG**, đã đo và xác nhận.

| Điều kiện có thể đổi kết quả | Đối tác (evidence `partner-evidence/TKKHCTHTPL_01.jpg`) | Mình test (env nip.io, 27/07/2026 14:29–14:45) | GAP? |
|---|---|---|:-:|
| Vai trò / tài khoản | Ảnh cho thấy đăng nhập `CB_NV_TW` ("Cán bộ NV Trung ương"), đơn vị BTP · TW | `cbnv_tw` — CB Nghiệp vụ - Trung ương, BTP · TW. Trùng khít. Đặc tả `:342` cho phép cả Cán bộ Nghiệp vụ lẫn Cán bộ Phê duyệt; đã đo thêm bằng `cbpd_tw` ở case cùng màn và thanh lọc không đổi | Không |
| Entity + trạng thái (state machine) | Màn `/ct-htpldn/danh-sach`, thẻ "Tất cả", dữ liệu trải nhiều trạng thái (Đang thực hiện, Tạm dừng, Chờ PD, Đã công bố, Dự thảo, Đã hủy, Hoàn thành) | Màn `/ct-htpldn/danh-sach`, thẻ "Tất cả", 8 chương trình trải 4 trạng thái (Đã duyệt 5, Đã công bố 1, Đang thực hiện 1, Hoàn thành 1) | Không |
| Dữ liệu tiền đề | Phiếu yêu cầu "Tồn tại bản ghi phù hợp với tiêu chí tìm kiếm" | Dựng đủ để phép đo có ý nghĩa theo **cả hai** chiều phiếu nêu: dữ liệu trải trên **2 đơn vị khác nhau** (7/8 thuộc một đơn vị) và trải **3 lĩnh vực khác nhau** (Đất đai, Thuế, Lao động) cộng 1 chương trình không gắn lĩnh vực. Nếu 2 bộ lọc đó tồn tại thì chúng phải có tác dụng thấy được | Không |
| Input / filter / giá trị nhập | Mở màn rồi đọc thanh lọc, không nhập gì | Đọc thanh lọc bằng mã lệnh (liệt kê ô nhập + danh sách chọn) thay vì chỉ nhìn ảnh; đọc phân trang; rồi gọi thẳng dịch vụ dữ liệu với từng tham số để tách lỗi giao diện khỏi lỗi xử lý | Không |

## Artifact real-data (Gate bằng chứng — loại claim: Thành phần giao diện)

- `partner-evidence/TKKHCTHTPL_01.jpg` — đã mở đọc: thanh lọc của đối tác gồm ô "Tìm theo tên hoặc mã CT...", một danh sách chọn nhãn **"Công bố"**, Từ ngày, Đến ngày, [Xóa bộ lọc], [Tìm kiếm]; bên dưới là 7 thẻ phân loại. Không có ô Đơn vị, không có ô Lĩnh vực. Trùng khít với môi trường QA.
- `bug-reports/image/BUG-CT-o-loc-duy-nhat-la-cong-bo.png` — đã mở đọc: danh sách chọn duy nhất đang mở, đúng 2 lựa chọn *"Đã công bố"* / *"Chưa công bố"* ⇒ là bộ lọc cờ công khai, không phải Đơn vị cũng không phải Lĩnh vực.
- `bug-reports/image/BUG-CT-phan-trang-20-moi-trang.png` — đã mở đọc: chân bảng ghi *"Hiển thị 1-8 / 8 kết quả"* và ô chọn *"20 / trang"* ⇒ bằng chứng cho phần phiếu mong đợi mà hệ thống làm đúng.

## Phương pháp thứ hai (bắt buộc)

- **Đọc thành phần bằng mã lệnh thay vì nhìn ảnh** — tránh kết luận "không có" chỉ vì thành phần nằm ngoài khung nhìn. Kết quả: ô nhập = `["Tìm theo tên hoặc mã CT...", "Từ ngày", "Đến ngày"]`; danh sách chọn trong vùng lọc = `["Công bố"]`. Quét chữ vùng lọc không có "Đơn vị" và không có "Lĩnh vực".
- **Phép thử quyết định — tách lỗi giao diện khỏi lỗi xử lý.** Gọi thẳng dịch vụ dữ liệu của màn với từng tham số:

  - không lọc → 8 chương trình
  - lọc theo một đơn vị cụ thể → 7 ⇒ tham số đơn vị **được xử lý thật**
  - lọc theo trạng thái `DA_DUYET` → 5 ⇒ tham số trạng thái **được xử lý thật**
  - lọc theo một lĩnh vực cụ thể → 1 ⇒ tham số lĩnh vực **cũng được xử lý thật**

  ⇒ Cả 3 tiêu chí đều đã chạy được ở phần xử lý phía sau; phần còn thiếu nằm hoàn toàn ở giao diện.
- **Đối chứng âm tính để loại khả năng "tham số nào truyền vào cũng ra kết quả giống nhau":** truyền một tham số bịa không tồn tại → vẫn trả đủ 8 chương trình. ⇒ Kết quả thu hẹp ở 3 phép đo trên là do bộ lọc thật sự có tác dụng, không phải trùng hợp.
- **Đối chiếu đặc tả — trích nguyên văn, và nêu thẳng chỗ KHÔNG có căn cứ:**
  - Có căn cứ cho vế Đơn vị: `:353` — *"| 2 | don_vi_id | identifier | N | Auto phân quyền nếu không truyền | -- | Chọn |"*; `:1110` — *"| 4 | filter-bar | **Don vi** | select | Auto phân quyền theo đơn vị (BR-AUTH-05) | change -> filter | **luon hien thi** |"*.
  - **Không có căn cứ cho vế Lĩnh vực:** bảng dữ liệu đầu vào `:352`–`:356` liệt kê đúng 5 mục `keyword` / `don_vi_id` / `trang_thai` / `tu_ngay` / `den_ngay`; bảng thanh lọc `:1109`–`:1112` cũng đúng 4 ô tương ứng. Không mục nào là lĩnh vực. Vì vậy QA **không** tự chấm lỗi mà chuyển BA-21.
- **Kiểm phần phiếu mong đợi mà hệ thống làm đúng, để không quy kết quá phạm vi:** `:1114` quy định *"| 8 | footer | Phan trang | pagination | **20 muc/trang** | click -> change page | luon hien thi |"*. Đo thực tế: chân bảng hiện *"Hiển thị 1-8 / 8 kết quả"*, ô chọn kích thước trang là *"20 / trang"*. ⇒ Đúng đặc tả. Tìm theo từ khóa cũng chạy đúng (mã `CT-20260724-0001` → 1 kết quả), khác hẳn màn Tư vấn nhanh ở Luồng 5.
- **Liên hệ chéo:** vế Lĩnh vực còn liên quan tới việc bảng **thiếu cột** "Lĩnh vực pháp lý" (`:1113`) — lỗi `BUG-CT-BANG-THIEU-COT-LINHVUC`, dòng `KHTHCTHTPLDN_OOS_05`. Thiếu cả cột lẫn bộ lọc nên hiện không có đường nào tra theo lĩnh vực từ màn này. Đã ghi vào BA-21 để BA xem một lượt.
