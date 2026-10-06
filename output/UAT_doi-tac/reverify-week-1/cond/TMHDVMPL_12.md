# Bảng đối chiếu điều kiện — TMHDVMPL_12 (row 277) — Upload JPG vào File đính kèm hỏi đáp

**Kết luận:** Open (Major). Tái hiện 1/1 bằng thao tác thật, cộng bằng chứng lưu được xuống máy chủ.

Phiếu ghi kỳ vọng *"Báo lỗi"*, thực tế *"Hệ thống upload file thành công"* → **TÁI HIỆN ĐÚNG**.

Trên màn **Quản lý hỏi đáp, vướng mắc pháp lý → [Thêm mới] → File đính kèm**, tôi tải lên một tệp `.jpg`. Hệ thống **nhận tệp** (đưa vào danh sách kèm nút *Xem / Xóa*), **không** báo lỗi, **không** có thông báo nào. Bấm **[Lưu]** thì bản ghi được tạo (`HD-20260730-001`) và tệp `.jpg` **được lưu xuống máy chủ** — đọc lại bản ghi thấy `fileDinhKem = [{ ten: "QA-TMHDVMPL_12-test.jpg", loai: "image/jpeg" }]`.

| Điều kiện có thể đổi kết quả | Đối tác (evidence `partner-evidence/TMHDVMPL_12.jpg`, full-res) | Mình test (env nip.io, 30/07/2026 10:54–10:56) | GAP? |
|---|---|---|:-:|
| Màn hình / chức năng | Ảnh: URL `htpldn-uat.ospgroup.vn/hoi-dap`, tiêu đề *"Quản lý hỏi đáp, vướng mắc pháp lý"*, panel phải *"Thêm mới hỏi đáp"* (nút *Hủy* / *Lưu*), mục **File đính kèm** | Đúng màn đó: `18.143.165.120.nip.io/hoi-dap`, tiêu đề *"Quản lý hỏi đáp, vướng mắc pháp lý"*, panel **Thêm mới hỏi đáp** (*Hủy* / *Lưu*), mục **File đính kèm** — bố cục trùng khít | Không |
| Vai trò / tài khoản | Ảnh bị panel che góc phải nên **không đọc được tên tài khoản**. Đọc được: đây là màn CMS nội bộ, thanh điều hướng bên trái trùng khít danh sách của tài khoản Cán bộ nghiệp vụ (Tổng quan · Hỏi đáp pháp lý · Đào tạo, tập huấn với 6 mục con · Mạng lưới Tư vấn viên với 3 mục con …) | `cbnv_tw` — **CB Nghiệp vụ - Trung ương (CB_NV_TW)**, BTP · TW. Đây là đúng lớp tác nhân mà đặc tả quy định cho chức năng này (`srs-fr-02-hoi-dap.md:89` — *"**Tác nhân:** Cán bộ Nghiệp vụ (TW/BN/ĐP)"*), và ràng buộc định dạng tệp được đặc tả khai ở **cấp trường dữ liệu** (`:108`) nên áp cho cả 3 cấp TW/BN/ĐP | Không |
| Input / giá trị nhập — **phần tranh chấp** | Tệp `TMHDVMPL_11.jpg` (259,4 KB) nằm trong danh sách *File đính kèm* cùng 3 tệp hợp lệ (`.pdf`, `.docx`, `.xlsx`), có nút *Xem* / *Xóa*, **không có dòng lỗi nào** | Tệp `QA-TMHDVMPL_12-test.jpg` (2,5 KB — JPEG thật, `file(1)` xác nhận *JPEG image data … 400x300*) được nhận vào danh sách, có nút *Xem* / *Xóa*, không dòng lỗi. **Dung lượng không phải điều kiện tranh chấp** (cả 2 đều ≪ 20MB/tệp); điều kiện tranh chấp là **phần mở rộng `.jpg`** | Không |
| Số tệp trong lần tải | 4 tệp (3 hợp lệ + 1 jpg) | Tôi tải **đúng 1 tệp `.jpg`** để cô lập biến — nếu chỉ 1 tệp jpg mà vẫn được nhận thì càng không thể do "lẫn trong lô nhiều tệp" | Không |

## Artifact real-data (Gate bằng chứng — loại claim: Validation → input sai → rule → message)

- `partner-evidence/TMHDVMPL_12.jpg` — đã mở đọc full-res. Dòng gợi ý của ô tải tệp ghi: *"Tối đa 10 tệp. Định dạng: .pdf, .doc, .docx, .xls, .xlsx, .jpg, .png. Dung lượng tối đa: 20MB/tệp."* Danh sách đã tải: `2K15 T5 (23.7) & T7 (25.7).pdf` (256,4 KB) · `Báo cáo mẫu.docx` (19,3 KB) · `Plan kiem thu.xlsx` (52,2 KB) · **`TMHDVMPL_11.jpg` (259,4 KB)** — tệp ảnh nằm yên trong danh sách, không có thông báo từ chối. Đồng hồ máy 09:14 27/07/2026.
- `reverify-audit/TMHDVMPL_12/01-man-quan-ly-hoi-dap-cbnv_tw.png` — đã mở đọc: màn `Quản lý hỏi đáp, vướng mắc pháp lý` của `cbnv_tw`, thanh điều hướng + tiêu đề + nhóm nút (*Làm mới · Xuất Excel · Thêm mới*) trùng khít ảnh đối tác.
- `reverify-audit/TMHDVMPL_12/02-drawer-them-moi-hoi-dap-goi-y-dinh-dang.png` — đã mở đọc: panel **Thêm mới hỏi đáp** mở ra, các mục Nội dung câu hỏi / Phân loại / Thông tin người gửi.
- `reverify-audit/TMHDVMPL_12/03-BUG-jpg-duoc-nhan-khong-bao-loi.png` — đã mở đọc = **khoảnh khắc lỗi**: mục **File đính kèm** hiển thị dòng gợi ý *"Định dạng: .pdf, .doc, .docx, .xls, .xlsx, .jpg, .png"* và tệp `QA-TMHDVMPL_12-test.jpg (2.5 KB)` với nút *Xem / Xóa*, **không có dòng lỗi**. Trùng khít bố cục ảnh đối tác.
- `reverify-audit/TMHDVMPL_12/04-BUG-jpg-luu-thanh-cong-tren-ban-ghi.png` — đã mở đọc: bản ghi `HD-20260730-001` (bước **1 Mới**) hiển thị **File đính kèm: QA-TMHDVMPL_12-test.jpg (2.5 KB)** với nút *Xem / Tải* ⇒ tệp ảnh đã vào hồ sơ thật, không chỉ nằm tạm ở giao diện.
- **Chứng minh "không có chốt kiểm nào chạy"**: lúc chọn tệp — **0 request**, **0 khung thông báo**, `.ant-form-item-explain-error` **rỗng**. Lúc [Lưu] — **2 request** `POST /api/v1/hoi-daps` (**201**) + `POST /api/v1/hoi-daps/{id}/files` (**201**), **1 khung thông báo** *"Tạo hỏi đáp thành công. Mã: HD-20260730-001"*; **không có phản hồi 4xx nào**. Bộ bắt thông báo `tools/toast-capture.js`, tự kiểm `soObserverDangSong = 1`.

## Phương pháp thứ hai (bắt buộc)

- **Đọc lại bản ghi trên máy chủ** (không chỉ nhìn giao diện): `GET /api/v1/hoi-daps/d3031a32-…` trả `fileDinhKem = [{ ten: "QA-TMHDVMPL_12-test.jpg", loai: "image/jpeg" }]` ⇒ máy chủ **đã nhận và lưu** tệp ảnh, không phải giao diện hiển thị nhầm rồi bị chặn khi lưu.
- **Đọc thuộc tính lọc tệp của chính ô tải lên** (bằng chứng độc lập với hành vi): thuộc tính `accept` của ô chọn tệp là `.pdf,.doc,.docx,.xls,.xlsx,.jpg,.png` — nghĩa là **`.jpg` và `.png` được đưa vào danh sách cho phép có chủ đích**, không phải lọt do lỗi ngẫu nhiên. Dòng gợi ý hiển thị cho người dùng cũng ghi y như vậy.
- **Cô lập biến số tệp**: đối tác tải 1 lô 4 tệp, tôi tải **duy nhất 1 tệp `.jpg`** — vẫn được nhận ⇒ loại giả thuyết "chốt kiểm chỉ chạy khi tải 1 tệp/lần" hoặc "lẫn trong lô nên bị bỏ qua".
- **Xác nhận tệp là JPEG thật**, không phải tệp đổi tên: `file(1)` trả *"JPEG image data, JFIF standard 1.01 … baseline, precision 8, 400x300, components 3"*; máy chủ cũng nhận diện `image/jpeg`. ⇒ Không phải trường hợp "hệ thống đọc nội dung thấy không phải ảnh nên tha".
- **Đối chiếu đặc tả — trích nguyên văn** (`Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-02-hoi-dap.md`):
  - `:79` — *"### FR-II-01: Quản lý thông tin hỏi đáp, vướng mắc pháp luật (UC10)"* · `:81` — *"**UC Reference:** UC 10"* · `:85` — *"**Màn hình:** SCR-II-01"*
  - `:108` (Inputs, trường 9 `file_dinh_kem`) — *"File đính kèm. Tối đa 10 file/upload, tổng max 100MB, mỗi file max 20MB. **Định dạng: doc/docx/xls/xlsx/pdf.** …"*
  - `:1070` (SCR-II-01, thành phần 45 *File đính kèm*) — *"Ref F-36: Tối đa 10 file/lần, tổng tối đa 100MB, mỗi file tối đa 20MB. **Định dạng: doc/docx/xls/xlsx/pdf.** …"*
  - `:1125` (SCR-II-01, thành phần 23 *File đính kèm phản hồi*) — *"Ref F-36 (đồng bộ với SCR-II-01 dòng 45) … **doc/docx/xls/xlsx/pdf.**"*
  ⇒ Cả 3 chỗ đặc tả nêu **cùng một** danh sách 5 định dạng, **không có** `jpg`/`png`. Kỳ vọng *"Báo lỗi"* của đối tác trùng khớp đặc tả ⇒ `Open`, không phải `BA confirm`.
- **Đối chiếu chỗ đặc tả CÓ cho phép ảnh, để không quy kết quá phạm vi**: đặc tả cho `jpg/png/gif` ở **ô ảnh đại diện khi công khai** (`:656`, `:1355` — *"Upload 1 file, jpg/png/gif, max 5MB"*) và vẫn giữ `PDF/DOC/DOCX/XLS/XLSX` cho **file đính kèm công khai** (`:658`, `:1358`). ⇒ Đặc tả phân biệt rõ *ảnh đại diện* (được phép ảnh) với *file đính kèm* (chỉ tài liệu). Ô đang test là **File đính kèm** của form thêm mới, không phải ảnh đại diện.
- **Đo lại trên bản triển khai MỚI (V1.0.3)** — bắt buộc vì hệ thống được deploy giữa phiên (thanh bên đổi `HTPLDN · V1.0.2` → `V1.0.3`): thuộc tính `accept` của ô chọn tệp **vẫn** là `.pdf,.doc,.docx,.xls,.xlsx,.jpg,.png`, dòng gợi ý **vẫn** ghi `.jpg, .png`, tải tệp `.jpg` **vẫn** được nhận (`toast: []`, `err: []`) và lưu được xuống hồ sơ `HD-20260730-003` với `loai: "image/jpeg"`. ⇒ **Lỗi còn nguyên trên bản đang chạy**.
- **Kiểm phần đã đúng**: 3 định dạng tài liệu tải kèm bình thường; giới hạn 10 tệp và 20MB/tệp được nêu đúng trong gợi ý; lưu bản ghi chạy đúng (1 thông báo, sinh mã `HD-YYYYMMDD-SEQ` theo `:117`). Lỗi khoanh đúng vào **danh sách định dạng cho phép của ô File đính kèm**.

## Pass đối kháng (tự bác trước khi ghi sheet)

1. *"Giao diện ghi rõ cho phép .jpg nên hệ thống chạy đúng thiết kế, không phải lỗi."* — Bác: chính **dòng gợi ý cũng sai** so với đặc tả. `:1070` quy định thành phần *File đính kèm* của SCR-II-01 phải nêu *"Định dạng: doc/docx/xls/xlsx/pdf"*. Giao diện tự thêm `.jpg, .png` ⇒ lệch ở **cả** hành vi lẫn phần chữ hiển thị, không phải "đặc tả im lặng nên app tự chọn".
2. *"Có thể đối tác/BA đã đồng ý mở thêm ảnh sau này."* — Đã tra: `CHANGELOG-v3-to-v3.5.md` ghi yêu cầu thay đổi của chính đối tác là *"Trong tất cả các chức năng quản lý có phần Thêm mới, cho phép tải lên file pdf, word…"* và các vị trí đã sửa đều là `PDF/DOC/DOCX/XLS/XLSX` — **không** có chỗ nào mở `jpg/png` cho *file đính kèm*. Cũng không có entry nào trong `tasks/srs-contradictions.md` về chủ đề này.
3. *"Có thể tệp bị chặn ở bước lưu, chỉ giao diện hiển thị tạm."* — Bác bằng số đo: `POST …/files` trả **201**, và đọc lại hồ sơ thấy tệp `image/jpeg` nằm trong `fileDinhKem`, giao diện chi tiết hồ sơ có nút *Xem / Tải*.
4. *"Ràng buộc `:108` có thể chỉ áp cho luồng nhận từ Cổng PLQG, không áp cho cán bộ nhập tay."* — Bác: `:108` nằm trong **bảng Inputs của FR-II-01**, mà FR-II-01 mô tả (`:87`) là *"Quản lý toàn bộ danh sách hỏi đáp pháp luật: xem, **thêm mới**, sửa, xóa…"* với tác nhân là Cán bộ Nghiệp vụ (`:89`) — tức đúng luồng tôi vừa test. Thêm nữa `:1070` là **thành phần màn hình** của chính form Thêm mới, không liên quan luồng liên thông.

## Ngoài tiêu chí phiếu — có thấy gì bất thường không?

- **Liên quan trực tiếp tới phiếu tiếp theo (`TMHDVMPL_16`, row 278):** dòng gợi ý của ô tải tệp **thiếu hẳn giới hạn tổng dung lượng** — chỉ ghi *"Tối đa 10 tệp … Dung lượng tối đa: 20MB/tệp."*, trong khi `:108` và `:1070` quy định *"tổng max 100MB"* và `:1070` còn yêu cầu hiển thị *"Tổng dung lượng {total} / 100MB"*. Ghi nhận ở đây làm dữ kiện, **verdict và bug sẽ ra ở đúng phiếu row 278** để không chấm trùng.
- **Đã soi và LOẠI, không log:** bảng điều khiển trình duyệt có 2 mục *issue* về trợ năng (*"No label associated with a form field"* ×4, *"A form field element should have an id or name attribute"* ×1) — đây là cảnh báo trợ năng của trình duyệt, **không phải lỗi JavaScript**, và đặc tả không quy định thuộc tính trợ năng cho các trường này ⇒ chưa đủ căn cứ log.
- Ngoài ra không phát hiện thêm: thao tác lưu = 2 request ↔ 1 thông báo (đúng: 1 request tạo hồ sơ + 1 request tải tệp, chỉ 1 thông báo kết quả), không lặp thông báo.
