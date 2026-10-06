# QLDMTCTV_09 — Bảng đối chiếu điều kiện + Cổng 3 (SRS vs web)

**Mã TC:** QLDMTCTV_09 · **Dòng sheet:** 320 · **Tab:** `UAT_TGPL Doanh Nghiệp-tuần 3`
**Ngày verify:** 2026-08-03 · **Môi trường:** https://18.143.165.120.nip.io (bản dựng đọc ở chân menu: `HTPLDN · V1.0.5`)
**Cột P (`Trạng thái dev fix 1`):** `dev done` — dev tự điền, là CLAIM chứ không phải bằng chứng · **Cột R:** rỗng tại thời điểm QA verify
**Phản ánh đối tác:** "Kiểm tra các trường thông tin trên màn hình/popup **sửa**" — màn *Mạng lưới Tư vấn viên → Tổ chức tư vấn → nhấn Sửa*. Kết quả thực tế đối tác ghi: **"Thiếu trường thông tin Số QĐ công bố, Ngày QĐ công bố, Tệp đính kèm"**.

> Bảng dưới đây là **bảng đối chiếu điều kiện duy nhất** trong file (script `sheet_write.py` đọc mọi bảng markdown trong file này).
> Phần Cổng 3 trình bày dạng gạch đầu dòng; bảng so 3 lần đo và lập luận đầy đủ đặt ở `reverify-audit/QLDMTCTV_09.md`.

---

## Cổng 1 — Bằng chứng đối tác (đã mở FULL-RES)

- File: `partner-evidence/QLDMTCTV_09.jpg` — đã mở đọc bằng tool Read ở độ phân giải gốc, đọc trực tiếp chữ trên ảnh, không kết luận từ ảnh thu nhỏ. Ảnh tĩnh ⇒ toàn bộ khung hình chính là khoảnh khắc lỗi.
- **3 dữ kiện neo (viết ra TRƯỚC khi hình thành giả thuyết):**
  - (a) **Vai trò đăng nhập:** góc phải trên ảnh ghi rõ **"Cán bộ NV Trung ương"** kèm mã **`CB_NV_TW`**, phạm vi **`BTP · TW`**. Đây đúng là vai trò được đặc tả cấp quyền sửa Tổ chức tư vấn ⇒ quan sát của đối tác là quan sát **hợp lệ**.
  - (b) **Bản ghi + trạng thái đang sửa:** URL `htpldn-uat.ospgroup.vn/chuyen-gia-tvv/to-chuc/d6434545-b76b-47ae-8be7-8bceea2d01a7/chinh-sua` — đúng chế độ **Chỉnh sửa**. Breadcrumb: "Trang chủ / Mạng lưới Tư vấn viên / Tổ chức tư vấn / **Chi tiết** / **Chỉnh sửa**" — **breadcrumb KHÔNG kèm tên tổ chức**, và **màn Sửa KHÔNG hiển thị mã tổ chức lẫn badge trạng thái**, nên không đọc được trạng thái bản ghi từ ảnh. Dữ liệu đọc được: Tên tổ chức "Test thêm mới tổ chức địa phương", Loại hình "Khác", Người đại diện "TKM", Số Giấy ĐKHĐ Sở TP "3344", Ngày cấp 08/07/2026, Địa chỉ "Hà Nội", 8 lĩnh vực pháp lý. Đồng hồ máy đối tác **2026-07-28 09:11**.
  - (c) **Nhóm thu gọn / ảnh cắt tới đâu:** biểu mẫu trong ảnh hiển thị **phẳng**, **KHÔNG có tiêu đề nhóm nào**, **KHÔNG có nhóm nào đang thu gọn** (không thấy mũi tên/dấu cộng để bung nhóm). Ảnh chụp từ ô đầu tiên "Tên tổ chức" **xuống tới ô cuối "Ghi chú"** và còn thấy mép trên của 2 nút cuối biểu mẫu ⇒ đã bao trọn chiều dài biểu mẫu.
- **🔴 Dữ kiện quyết định:** thứ tự ô đọc được trong ảnh là Tên tổ chức → Loại hình → Người đại diện → Chức vụ đại diện → Số Giấy ĐKHĐ Sở TP → Ngày cấp → Số lao động → Địa chỉ → Điện thoại → Email → Website → Lĩnh vực pháp lý → **Ghi chú**. Giữa "Lĩnh vực pháp lý" và "Ghi chú" **không có** mục "Công bố", **không có** mục "Tệp đính kèm".
- ⇒ Kết luận Cổng 1: đối tác **không bỏ sót do chưa cuộn hay chưa mở nhóm**. Tại bản dựng họ chụp, 3 trường đó **thật sự vắng mặt ở cả chế độ Sửa**. Phản ánh của đối tác **chính xác** đối với bản dựng đó ⇒ **KHÔNG được dùng `Reject`**.
- **Lưu ý bản ghi đối tác dùng:** tên "Test thêm mới tổ chức địa phương" cho thấy đây là bản ghi họ vừa tạo từ màn Thêm mới (ảnh case QLDMTCTV_06 chụp lúc 09:05, ảnh case này 09:11 — cách nhau 6 phút). Vì màn Thêm mới của bản dựng đó cũng thiếu 3 trường, nên **bản ghi này chắc chắn KHÔNG có dữ liệu ở 3 trường tranh chấp** — đây chính là điều kiện phải tái hiện.

## Cổng 2 — Hiểu bug

- Đối tác phản ánh CỤ THỂ 3 thành phần bị thiếu **trên biểu mẫu ở chế độ Sửa**: (1) ô nhập **Số quyết định công bố**, (2) bộ chọn ngày **Ngày quyết định công bố**, (3) vùng **Tệp đính kèm**. Ngoài ra Kết quả mong đợi của đối tác còn đòi biểu mẫu phải **điền sẵn thông tin hiện có**, đúng định dạng, không tràn/đè, đồng nhất ngôn ngữ.
- Dữ liệu + bước tái hiện: đăng nhập vai trò Cán bộ Nghiệp vụ → menu *Mạng lưới Tư vấn viên* → *Tổ chức tư vấn* → bấm biểu tượng **Sửa** (bút chì) trên một dòng → đọc toàn bộ biểu mẫu.
- **Điểm sắc bén của case:** nếu ứng dụng chỉ vẽ 3 trường đó **khi bản ghi đã có sẵn dữ liệu**, thì bản ghi cũ (tạo lúc chưa có 3 trường) mở ra vẫn thiếu — đúng y hệt cái đối tác báo. Vì vậy tiền đề bắt buộc là phải mở chế độ Sửa trên **cả bản ghi KHÔNG có dữ liệu 3 trường lẫn bản ghi CÓ dữ liệu**, ở **nhiều trạng thái khác nhau**.

---

## 🔴 Bảng đối chiếu điều kiện (0 GAP mới được chốt verdict)

| Điều kiện có thể đổi kết quả | Đối tác (từ evidence, full-res) | Mình test | GAP? |
|---|---|---|---|
| Vai trò / tài khoản | Cán bộ Nghiệp vụ Trung ương — vai trò `CB_NV_TW`, phạm vi `BTP · TW` (đọc được ở góc phải trên ảnh) | `cbnv_tw_04` (CB Nghiệp vụ - Trung ương, `CB_NV_TW`, phạm vi `BTP · TW`, đơn vị Cục Bổ trợ tư pháp - Bộ Tư pháp) — **trùng khớp tuyệt đối vai trò + cấp + đơn vị của đối tác**; đăng nhập OK ngay lần đầu, không phải dùng tài khoản thay thế. Chạy trong phiên trình duyệt cách ly riêng nên không dính phiên cũ | Không |
| Entity + trạng thái (state machine) | `TO_CHUC_TU_VAN` — chế độ **Chỉnh sửa** (`/chuyen-gia-tvv/to-chuc/:id/chinh-sua`). Ảnh **không hiển thị badge trạng thái** nên không đọc được trạng thái bản ghi ⇒ phải phủ nhiều trạng thái để loại trừ | Mở chế độ **Chỉnh sửa** trên **4 bản ghi thuộc 3 trạng thái khác nhau**: `TCTV-SEED-0001` (Đang hoạt động) · `TC-BTP-TW-0002` (Mới đăng ký) · `TC-BTP-TW-0003` (Mới đăng ký) · `TC-BTP-TW-0001` (Chờ phê duyệt). Cả 4 lần đo cho **kết quả giống hệt nhau** ⇒ biểu mẫu Sửa **không đổi theo trạng thái** | Không |
| Dữ liệu tiền đề (bản ghi CÓ vs KHÔNG có dữ liệu ở 3 trường tranh chấp) | Bản ghi "Test thêm mới tổ chức địa phương" — vừa tạo từ màn Thêm mới của bản dựng thiếu 3 trường ⇒ **KHÔNG có dữ liệu** ở Số QĐ / Ngày QĐ / tệp đính kèm | Đo trên **cả hai loại**: (1) bản ghi **KHÔNG có dữ liệu 3 trường** — `TCTV-SEED-0001` (dữ liệu seed cũ nhất, không do QA tạo), `TC-BTP-TW-0002`, `TC-BTP-TW-0001`; (2) bản ghi **CÓ dữ liệu 3 trường** — `TC-BTP-TW-0003`. Đây là phép thử quyết định của case, đã chạy đủ cả 2 nhánh | Không |
| Input / filter / giá trị nhập | Không nhập gì — ảnh chụp biểu mẫu Sửa lúc vừa mở, chỉ đọc | Đo **lúc vừa mở, chưa thao tác gì** (đúng điều kiện ảnh đối tác) trên cả 4 bản ghi; có **cuộn hết chiều dài biểu mẫu** và **rà mọi dấu hiệu nhóm thu gọn** trước khi kết luận. Sau đó nhập thêm để kiểm 3 trường **dùng được thật** trên bản ghi vốn đang trống, rồi **tải lại trang bỏ qua bộ nhớ đệm** đo lại để chắc không đọc phải mã cũ còn giữ trong tab | Không |

**Kết luận điều kiện: 0 GAP → đủ điều kiện chốt verdict.**

---

## Cổng 3 — SRS yêu cầu (dẫn dòng) vs thực tế web

**Nguồn SRS:** `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-04-chuyen-gia-tvv.md` — bản chốt duy nhất, đã **mở file đọc từng dòng**, không lấy số dòng từ trí nhớ. KHÔNG dùng `input/srs-update-2026-5-5/`.

### Thứ tự đo (đo web TRƯỚC, đọc SRS SAU)

- Danh sách nhóm + trường quan sát được đã viết ra **TRƯỚC** khi mở SRS, bằng cách đọc thô cây DOM (`label innerText`, **không dùng `textContent`**) + ảnh chụp đã mở đọc.

### 🔴 SRS dùng CHUNG một màn cho Thêm mới VÀ Sửa — nên yêu cầu về trường của màn Sửa = y hệt màn Thêm mới

- **Dòng 1662**: tiêu đề `SCR-IV-NEW-02: **Thêm mới / Chỉnh sửa** Tổ chức tư vấn`.
- **Dòng 1666**: hai đường dẫn `/chuyen-gia-tvv/to-chuc/tao-moi` **và** `/chuyen-gia-tvv/to-chuc/:id/chinh-sua` cùng trỏ về **1 màn duy nhất** này.
- **Dòng 1675**: breadcrumb có hai nhánh — nhánh "Thêm mới" và nhánh "**Chỉnh sửa [Tên TC]**" — xác nhận màn này phục vụ cả chế độ Sửa.
- **Dòng 1696**: nút Lưu xử lý **cả 2 chế độ** ("tạo mới **hoặc cập nhật**").
- **Dòng 1334**: cây menu ghi `SCR-IV-NEW-02: **Thêm/Sửa** Tổ chức tư vấn` — cùng một mã màn cho cả 2 chế độ.
- Phần **Processing** của FR chỉ có các khối "Thêm mới" / "Xóa (xóa mềm)" / "Công khai" / "Xuất DS" — **KHÔNG có khối riêng cho Sửa**; Postconditions **dòng 1114** gộp "tạo/cập nhật/xóa mềm".
- ⇒ **SRS KHÔNG có danh sách trường riêng cho màn Sửa và KHÔNG quy định trường chỉ-đọc nào.** Yêu cầu về trường ở chế độ Sửa **bằng đúng** chế độ Thêm mới.
- **Dòng 1667**: "Quyền truy cập: **Cán bộ Nghiệp vụ** (tạo/sửa Tổ chức tư vấn thuộc đơn vị mình). **Chỉ cho phép sửa khi trạng thái khác 'Vô hiệu hóa'**" — đã test đúng vai trò này; 3 trạng thái đã phủ đều khác "Vô hiệu hóa" nên đều được phép sửa.
- **Dòng 1646**: nút Sửa (bút chì) → SCR-IV-NEW-02, "**ẩn nếu trạng thái Vô hiệu hóa**" — xem mục ghi nhận bên dưới.

### 3 trường đối tác báo thiếu — kết quả đo trên web hiện tại (chế độ **Sửa**)

- **Số quyết định công bố** (SRS **dòng 1692**, nhóm 4 "Công bố", ô văn bản, *Tùy chọn*): ✅ **CÓ trên cả 4 bản ghi**, hiện sẵn ngay khi vừa mở biểu mẫu Sửa.
- **Ngày quyết định công bố** (SRS **dòng 1693**, nhóm 4 "Công bố", bộ chọn ngày, *Tùy chọn*): ✅ **CÓ trên cả 4 bản ghi**, là bộ chọn ngày thật (có biểu tượng lịch).
- **Tệp đính kèm** (SRS **dòng 1694**, nhóm 5 "File đính kèm", tải nhiều file, PDF/DOC/DOCX/XLS/XLSX, tối đa 20MB/file, quét virus): ✅ **CÓ trên cả 4 bản ghi**. Chú thích trên web: *"Tối đa 10 tệp. Định dạng: .pdf, .doc, .docx, .xls, .xlsx. Dung lượng tối đa: 20MB/tệp."* — định dạng và giới hạn 20MB **khớp đúng** SRS.
- Tìm bằng **≥2 cách độc lập**: (1) theo chữ trên nhãn (`label[for="soQdCongBo"]`, `label[for="ngayQdCongBo"]`), (2) theo **loại điều khiển** — đếm được `input[type=file]` = 1, `.ant-upload-drag` = 1, `.ant-picker` = 2 (Ngày cấp + Ngày QĐ công bố), và 2 tiêu đề phân cách "Công bố" + "Tệp đính kèm". Hai cách cho **cùng kết quả** trên cả 4 lần đo.
- **Nguồn thứ 2 độc lập trong SRS** (mục Inputs của FR-IV-NEW-01) xác nhận cùng 3 trường: `so_qd_cong_bo` **dòng 1060** · `ngay_qd_cong_bo` **dòng 1061** · `file_dinh_kem` **dòng 1063** (PDF/DOC/DOCX/XLS/XLSX, max 20MB/file). Cả 3 được quy định ở **2 chỗ độc lập** → yêu cầu rõ ràng, không phải suy diễn từ một dòng đơn lẻ.
- **Điều kiện ẩn/hiện:** đã đọc kỹ cột "Hành vi" các dòng 1691–1694 và mô tả nhóm dòng 1669 — **SRS KHÔNG đặt bất kỳ điều kiện ẩn/hiện nào** cho 3 trường này (không theo trạng thái, không theo việc bản ghi đã có dữ liệu hay chưa). ⇒ SRS đòi chúng **luôn hiện**. Web đang đáp ứng.

### 🔴 Phép thử quyết định — giả thuyết "chỉ hiện khi bản ghi đã có dữ liệu" đã bị BÁC BỎ

- 3 trong 4 bản ghi đo được (`TCTV-SEED-0001`, `TC-BTP-TW-0002`, `TC-BTP-TW-0001`) **đều rỗng cả 3 trường** ở phía máy chủ, **vẫn hiển thị đủ 3 trường** ở chế độ Sửa (ô rỗng kèm gợi ý "nhập dữ liệu" / "Vui lòng chọn" / vùng kéo-thả trống).
- Riêng `TCTV-SEED-0001` là **dữ liệu seed cũ nhất, không do QA tạo** — đúng tinh thần "bug về trường lưu trong CSDL phải thử trên cả dữ liệu cũ lẫn dữ liệu mới".
- ⇒ Không tồn tại hiện tượng "bản ghi cũ mở ra thì thiếu trường". Cả bản ghi cũ lẫn mới, cả có dữ liệu lẫn không, đều hiện đủ.

### Đối chiếu ĐỦ/THIẾU **TỪNG** trường theo bảng Thành phần màn hình (dòng 1673–1696)

- Nhóm 1 — **dòng 1676–1682**: Tên tổ chức * ✅ · Loại hình * ✅ · Người đại diện * ✅ · Chức vụ người đại diện ✅ · Số Giấy ĐKHĐ * ✅ · Ngày cấp * ✅.
- Nhóm 2 — **dòng 1683–1685**: Lĩnh vực pháp luật * ✅ (chọn nhiều) · Số lao động ✅ (ô số).
- Nhóm 3 — **dòng 1686–1690**: Địa chỉ trụ sở * ✅ · Số điện thoại ✅ · Email ✅ · Website ✅.
- Nhóm 4 — **dòng 1691–1693**: Số quyết định công bố ✅ · Ngày quyết định công bố ✅.
- Nhóm 5 — **dòng 1694**: File đính kèm ✅.
- Nhóm 6 — **dòng 1695**: Ghi chú ✅ (ô văn bản dài).
- **Dòng 1696**: 2 nút **Hủy / Lưu** ✅ — đúng 2 nút, đúng tên.
- ⇒ **Không thiếu trường nào** ở chế độ Sửa. Tổng 16 ô nhập trên biểu mẫu, khớp đủ danh sách SRS (15 trường + 1 vùng tải tệp).

### "Điền sẵn thông tin hiện có" — phần còn lại trong Kết quả mong đợi của đối tác

- Đối chiếu **từng trường** giữa dữ liệu thật của bản ghi và giá trị hiện trên biểu mẫu Sửa, trên **cả 4 bản ghi**: mọi trường có dữ liệu đều được **điền sẵn đúng**; các ô để trống đều tương ứng với trường **thật sự chưa có dữ liệu** ở bản ghi đó.
- Định dạng hiển thị đúng: ngày hiện dạng ngày/tháng/năm (ví dụ `01/06/2026`, `15/07/2026`), dropdown một lựa chọn hiện đúng nhãn tiếng Việt ("Trung tâm Tư vấn Pháp luật", "Công ty Luật"), dropdown nhiều lựa chọn hiện đúng các thẻ lĩnh vực, tệp đính kèm hiện **đúng tên tệp + dung lượng** kèm nút "Xem"/"Xóa".
- Không tràn/đè, bố cục đều, **toàn bộ chữ hiển thị là tiếng Việt** — kiểm bằng ảnh chụp đã mở đọc.
- ⇒ Phần "điền sẵn thông tin hiện có" của case **đạt**.

### 3 trường có dùng được thật không (không chỉ hiển thị)

- Chọn **bản ghi vốn đang trống cả 3 trường** — `TC-BTP-TW-0002` (Mới đăng ký) — nhập **Số QĐ công bố** = `QD-CB-QA-0903/2026`, chọn **Ngày QĐ công bố** = `20/07/2026`, đính **1 tệp PDF hợp lệ** (`QA-QD-cong-bo-QLDMTCTV09.pdf`, 398 B) rồi bấm **Lưu**.
- Kết quả: lưu thành công, chuyển về màn Chi tiết hiển thị "Số QĐ công bố: QD-CB-QA-0903/2026" và "Ngày QĐ công bố: 20/07/2026"; trạng thái bản ghi giữ nguyên "Mới đăng ký".
- **Dữ liệu được lưu thật:** sau **tải lại trang bỏ qua bộ nhớ đệm** rồi mở lại chế độ Sửa, cả 3 vẫn còn đủ — kể cả tệp đính kèm (tên tệp + dung lượng + nút "Xem"/"Xóa"), và tệp đã được quét ở trạng thái sạch ⇒ dữ liệu nằm ở máy chủ, không phải chỉ trên màn hình.
- Đo kèm số request: **1 request** cập nhật / **1 khung thông báo** "Cập nhật thành công" → không có thông báo lặp, không ghi trùng.

### Ghi nhận thêm về nút Sửa khi trạng thái "Vô hiệu hóa" (SRS dòng 1646/1667)

- Không kiểm được: cả 3 tab "Đã từ chối", "Tạm dừng", "Vô hiệu hóa" đều **rỗng** (không có bản ghi nào), nên không có dòng nào ở trạng thái Vô hiệu hóa để xem nút Sửa có bị ẩn không.
- **Không ảnh hưởng verdict**: đây không phải tiêu chí của case (case chỉ kiểm các trường trên biểu mẫu Sửa), và 3 trạng thái đã phủ đều là trạng thái **được phép sửa** theo dòng 1667.

---

## Kết luận

- Phản ánh của đối tác **KHÔNG còn tái hiện** trên bản dựng hiện tại `HTPLDN · V1.0.5`, kiểm ở đúng vai trò `CB_NV_TW` + đúng đơn vị `BTP · TW` như ảnh đối tác:
  - **Số quyết định công bố → đã có** ở chế độ Sửa, trên mọi bản ghi đã thử.
  - **Ngày quyết định công bố → đã có**, là bộ chọn ngày thật.
  - **Tệp đính kèm → đã có**, kèm đúng ràng buộc định dạng và 20MB/tệp như đặc tả.
- **Phép thử quyết định đã chạy đủ 2 nhánh:** bản ghi **không có** dữ liệu 3 trường (kể cả dữ liệu seed cũ nhất) và bản ghi **có** dữ liệu — **cả hai đều hiện đủ 3 trường** ⇒ bác bỏ khả năng "chỉ vẽ trường khi đã có dữ liệu".
- Đã phủ **3 trạng thái** (Đang hoạt động · Mới đăng ký · Chờ phê duyệt) — biểu mẫu Sửa **không đổi theo trạng thái**.
- Cả 3 **không chỉ hiển thị mà lưu được dữ liệu thật** trên chính bản ghi vốn đang trống, còn nguyên sau khi tải lại trang bỏ qua bộ nhớ đệm.
- Phần "**điền sẵn thông tin hiện có**" trong Kết quả mong đợi của đối tác cũng **đạt**: mọi trường có dữ liệu đều được điền đúng, đúng định dạng, không tràn/đè, đồng nhất tiếng Việt.
- Xác nhận thêm: đối tác **không thao tác sai** — ảnh của họ cho thấy biểu mẫu Sửa bản cũ thật sự thiếu 3 trường và **không có nhóm thu gọn nào để mà bỏ sót**. Vì vậy **KHÔNG dùng `Reject`**.
- Mỗi kết luận dựa trên 2 phương pháp độc lập cho kết quả trùng nhau: đọc thô cây DOM và ảnh chụp **đã mở ra đọc**.
- Không có lỗi/cảnh báo trong bảng điều khiển trình duyệt; các lệnh gọi máy chủ đều 200/304.
- **⇒ Verdict: `Pass`** (cột Q — Verify). Cột P giữ nguyên `dev done`, KHÔNG đụng tới.

## Ngoài phạm vi case (chưa log — chờ user quyết)

1. **Biểu mẫu Sửa không chia 6 nhóm thu gọn như đặc tả.** SRS dòng 1664 / 1669 / 1676 / 1683 / 1686 / 1691 mô tả 6 nhóm dạng "nhóm thu gọn"; web để phẳng, chỉ có 2 tiêu đề phân cách "Công bố" và "Tệp đính kèm". Giống hệt quan sát ở màn Thêm mới (case QLDMTCTV_06). Không cản trở nhập liệu.
2. **Thứ tự trường và một số nhãn rút gọn so với SRS** — giống màn Thêm mới, nghĩa không đổi.
3. **Mâu thuẫn nội tại của SRS (để BA chốt, KHÔNG dùng chấm case này).** Bảng màn hình dòng 1681–1682 đánh dấu "Số Giấy ĐKHĐ" và "Ngày cấp" là **bắt buộc (\*)**, nhưng bảng Inputs của FR dòng 1052–1053 lại ghi Bắt buộc = **N**. Web làm theo bảng màn hình (bắt buộc) — cũng khớp bước 3 phần Processing (dòng 1073). Hệ quả quan sát được ở chế độ Sửa: bản ghi seed cũ `TCTV-SEED-0001` đang **trống 2 trường bắt buộc này**, nên nếu muốn lưu bản ghi đó thì buộc phải bổ sung dữ liệu mới lưu được.
4. **Màn Chi tiết chưa hiển thị vùng tệp đính kèm.** Bản ghi có tệp nhưng màn Chi tiết chỉ liệt kê thông tin chữ, phải vào Chỉnh sửa mới thấy tệp. Là **màn khác** (SCR-IV-NEW-03) ⇒ chỉ ghi nhận, chưa kết luận.

## Ghi chú đo lường (chống lặp lại lỗi 16/07)

- Bộ bắt thông báo: dùng đúng `tools/toast-capture.js`, **không lọc trùng**, đọc bằng `innerText`; đã tự kiểm **`soObserverDangSong = 1`** *trước* khi tin số liệu.
- Thao tác đổi trạng thái (lưu bản ghi) đo kèm số request: **1 request / 1 khung thông báo** → không lặp, không ghi trùng.
- Mọi ảnh đều **đã được mở ra đọc**, không chỉ lưu; **2 ảnh đã đổi tên cho khớp điểm ảnh** (xem `reverify-audit/QLDMTCTV_09.md`).
- **Hai lần selector của QA sai — KHÔNG phải lỗi ứng dụng**, đã truy tới cùng bằng mã HTML thô trước khi kết luận nên không log oan: (1) đọc giá trị dropdown bằng `.ant-select-selector` ra rỗng trong khi dropdown vẫn hiện đúng giá trị — bản Ant Design của ứng dụng dùng `.ant-select-content-value`; (2) đọc vùng tệp bằng `.ant-upload` nên không thấy tên tệp đã đính — danh sách tệp nằm cạnh vùng kéo-thả chứ không nằm trong nó. Cả 2 lần đều là **phép đo sai, không phải ứng dụng thiếu dữ liệu**.
- Theo cảnh báo từ case trước, **không dùng ảnh chụp chế độ "toàn trang"**; toàn bộ bằng chứng chụp theo **khung nhìn + cuộn** và đối chiếu lại với phép đo cây DOM trước khi kết luận.
