# Nhật ký đo — `KTDGKQHT_05` (dòng 10 tab `bug`)

**Ngày:** 2026-08-07 · **Quy trình:** flow 04 BƯỚC 0 mục 2 — phiếu đã có khối `CÁCH VERIFY` sẵn ⇒ **chạy lại đúng khối đó**, không chạy flow 04 từ đầu.

## 0. Minh bạch về cách lượt đo này được hoàn tất

Phần thao tác trên giao diện do một thành viên trong đội thực hiện lúc **12:04–12:06 ngày 07/08/2026**.
Phiên của thành viên đó **bị ngắt giữa chừng** (chạm giới hạn API theo tuần) **sau khi đã đo xong và đã tải
ảnh lên Drive**, nhưng **trước khi kịp viết nhật ký và ghi bảng**. Nhật ký này do điều phối dựng lại
**từ hiện vật để lại**, và **mọi kết luận đều được xác minh lại độc lập** trước khi chốt:

| Hiện vật / phép xác minh | Ai tạo | Đã kiểm lại thế nào |
|---|---|---|
| `files/mau-goc-KTDGKQHT_05-20260807-1204.xlsx` — tệp mẫu hệ thống sinh | thành viên đo | **mở bằng `openpyxl`**: sheet ẩn `_HTPLDN_META` có `khoa_hoc_id=a7480002…0002`, `lich_hoc_id=bd1cdf35…c8c2` ⇒ đúng khóa + đúng Buổi 4 |
| `files/fixture-KTDGKQHT_05-3hople-2loi-20260807-1205.xlsx` — tệp đã điền | thành viên đo | **mở bằng `openpyxl`**: đúng 5 dòng — 3 hợp lệ (Có mặt / Vắng có phép / Vắng không phép) + 1 dòng học viên khóa khác + 1 dòng trạng thái `XYZ` |
| 3 ảnh màn hình quyết định | thành viên đo | **điều phối tự mở xem lại từng ảnh**, không trích ảnh chưa xem |
| **Đọc lại bản ghi qua API** (đường đo thứ hai) | **điều phối, lúc 12:35** | `GET /khoa-hocs/{id}/diem-danhs?lichHocId=…&ngayDiemDanh=2026-05-11` |
| **Vân tay bản dựng** | **điều phối, lúc 12:40** | `GET /` ×2 |

⇒ Hai đường đo (giao diện + đọc lại bản ghi) **khớp nhau**, nên theo flow 04 §Giai đoạn B mục 8 **không thêm đường thứ ba**.

## 1. Môi trường + bản dựng

| Hạng mục | Giá trị |
|---|---|
| Môi trường | `https://18.143.165.120.nip.io` — env **NỘI BỘ** (đối tác đo trên `htpldn-uat.ospgroup.vn`) |
| Bó mã giao diện | **`assets/index-eWHwDgt2.js`** · `assets/index-DVlgOkLg.css` |
| `GET /` last-modified | `Fri, 07 Aug 2026 02:11:03 GMT` = **09:11 giờ VN 07/08** · etag `W/"6a753eb7-428"` |
| Vân tay đầu lượt | 11:49 (đồng đội trinh sát) — cùng bó mã, cùng etag |
| Vân tay cuối lượt | **12:40 (điều phối), `GET /` ×2 — y nguyên** ⇒ **không có bản mới xen giữa lượt đo** |
| Nhãn ở thanh bên | `HTPLDN · V1.0.10` (đọc được trên ảnh) — **không dùng làm định danh** (đã có ca lùi nhãn, xem `BAN-DUNG.md`) |
| Tài khoản đo | **`cbnv_tw_03`** — Cán bộ Nghiệp vụ Trung ương, hiện trên màn là "CB Nghiệp vụ - Trung ương #03" |

> Lượt đo trước (02:20 cùng ngày) chạy trên bó mã `index-DsMHK7Dp.js` ⇒ **đã qua 2 lần deploy**.

## 2. Tiền đề

- Khóa **`KH-QAW7-HOINGHI`** (`a7480002-0000-4000-8000-000000000002`), trạng thái `DANG_DIEN_RA`, 4 buổi, 4 học viên `DA_DUYET`.
- **Buổi 4** (`bd1cdf35-8ab7-41f6-ae85-d21fdec2c8c2`) — **11/05/2026, 14:00–16:00**, nhãn trên màn "Buổi 4 - QA seed KTDGKQHT_23".
  Trinh sát lúc ~11:49 xác nhận đây là **buổi SẠCH duy nhất** (buổi 1/2/3 đã có dữ liệu từ các lượt trước) ⇒ **chỉ có đúng một lượt đo sạch**.
- **Không seed thêm gì.** Thay đổi duy nhất lên môi trường là **3 bản ghi điểm danh của Buổi 4** do chính thao tác đang verify sinh ra (khai ở §5).

## 3. Đo từng vế

### C1 — Bản xem trước (số dòng hợp lệ, số dòng lỗi, lý do từng dòng) · `MATCH` · **ĐẠT**

Đặc tả `srs-fr-03-dao-tao.md:593`: *"Hiển thị bản review (thành công / lỗi) — dòng lỗi ghi rõ mã lỗi + số dòng"*.

Đo được (ảnh 03): hộp thoại "Import điểm danh từ Excel" → khối **"Kết quả kiểm tra - chưa nhập dữ liệu"**:
**Tổng dòng 5 · Hợp lệ 3 · Bỏ qua 0 · Lỗi 2**; hai thẻ "Hợp lệ (3)" / "Lỗi/Bỏ qua (2)"; bảng lỗi ghi
**đúng số dòng và lý do riêng cho từng dòng**:
- dòng 5 → `ERR-KQ-03: Không tìm thấy học viên ở dòng 5…`
- dòng 6 → `ERR-KQ-04: Giá trị điểm danh không hợp lệ…`

Đối chiếu câu chữ với bảng xử lý lỗi: `:637` `ERR-KQ-03` = *"Không tìm thấy học viên ở dòng {N} (định danh không hợp lệ hoặc không thuộc khóa học này)"* · `:638` `ERR-KQ-04` = *"Giá trị điểm danh không hợp lệ"* ⇒ **khớp**.
Nút hành động ghi rõ **"Xác nhận import (3 dòng hợp lệ)"**.

### C2 — Nạp thành công, chỉ merge dòng hợp lệ · `MATCH` · **ĐẠT** (đây là chỗ hỏng của lượt trước)

Đặc tả: `:594` *"Nếu xác nhận: merge kết quả — **chỉ merge dòng hợp lệ**, dòng lỗi bỏ qua"* ·
`:595` *"Trả về báo cáo import"* · AC `:652` *"…merge dòng hợp lệ"* · AC `:654` *"…dòng đó báo ERR-KQ-03 và bị bỏ qua"*.

**Đường 1 — giao diện** (ảnh 04, chụp ngay sau khi bấm "Xác nhận import"):
hệ thống hiện **"Import hoàn tất" — Đã nhập 3 · Bỏ qua 0 · Lỗi 2**, kèm bảng chi tiết 5 dòng
(dòng 2/3/4 "Hợp lệ" với đúng 3 giá trị đã điền; dòng 5/6 "Lỗi" với 2 mã lỗi khác nhau).
🔴 **Không còn thông báo "Lỗi hệ thống, vui lòng thử lại sau"** như lượt 02:20 cùng ngày.

**Đường 2 — đọc lại bản ghi qua API** (điều phối chạy lúc 12:35, `GET /khoa-hocs/{id}/diem-danhs?lichHocId=bd1cdf35…&ngayDiemDanh=2026-05-11`), trả về **4 học viên**:

| hocVienId | Họ tên | `trangThai` | `coMat` | Kỳ vọng |
|---|---|---|---|---|
| `dbf62f06…b660` | QA R3 Mailto Ba | `CO_MAT` | true | ✅ đúng dòng 2 của tệp ("Có mặt") |
| `cd17f1b7…458b` | QA R3 Mailto Hai | `VANG_PHEP` | false | ✅ đúng dòng 3 ("Vắng có phép") |
| `6feead91…7f53` | QA R3 Mailto Mot | `VANG_KHONG_PHEP` | false | ✅ đúng dòng 4 ("Vắng không phép") |
| `56640d49…1162` | Nguyễn Văn A | **`None`** | false | ✅ đúng — đây là dòng 6 ghi `XYZ`, **phải bị bỏ qua** |

Học viên ở dòng 5 (`cccccccc-…`, thuộc khóa khác) **không xuất hiện** trong danh sách ⇒ đúng `ERR-KQ-03`.
**Đếm: đúng 3/3 dòng hợp lệ được ghi, đúng giá trị; 0/2 dòng lỗi được ghi.**

**Đường 1 đối chiếu trên giao diện** (ảnh 06): tab Điểm danh Buổi 4 sau khi nạp — 4 dòng, **3 dòng có nút trạng thái được tô đậm đúng giá trị**, dòng Nguyễn Văn A **không nút nào được chọn**. Khớp hoàn toàn với đường 2.

### C3 — Cơ chế "Tải mẫu → điền → tải lên" (khiếu nại GỐC của đối tác) · `MATCH` · **ĐẠT**

Khiếu nại gốc ở ô `TKM phản hồi lần 1`: *"Màn hình danh sách không hiển thị mã học viên nhưng khi nhập file excel điểm danh hệ thống bắt buộc có mã học viên"*, kèm ô `Loại vấn đề`: *"nếu thêm cột MHV có đc ko"*.

🔴 **Nghiệp vụ đã chốt việc này rồi, và đã thi hành vào đặc tả.** `srs-fr-03-dao-tao.md:14` là dấu sửa đổi ghi
đích danh phiếu này: *"**Sửa đổi 2026-08-04 — chuẩn hoá nghiệp vụ nhập kết quả qua Excel bằng cơ chế "Tải mẫu →
điền → tải lên" (KTDGKQHT_05)**… hệ thống điền sẵn danh sách học viên + định danh, cán bộ chỉ điền cột
điểm/điểm danh… **Giữ `hoc_vien_id` làm khoá đối chiếu, KHÔNG thêm trường vào entity HOC_VIEN.**"*
`:573`: *"cán bộ **không tự gõ định danh học viên**"* · `:581`: cột `hoc_vien_id` *"(điền sẵn, khoá/ẩn — ID nội bộ opaque, cán bộ không sửa)"*.

Đo được: tệp mẫu tải từ nút "Tải mẫu điểm danh" **đã điền sẵn `hoc_vien_id` cho cả 4 học viên**, cột A **ẩn và khóa**, đúng 6 cột theo `:581`; định danh buổi học nằm ở **vùng metadata** (`_HTPLDN_META`) chứ không phải cột từng dòng, đúng `:583`.
⇒ Cán bộ **không cần biết mã học viên**. Khiếu nại gốc **đã được giải quyết đúng hướng nghiệp vụ đã chốt**.

### G1 — Câu chữ thông báo kết quả nạp · **`GAP` (đặc tả im lặng)** · route **BA** — **CẤM Pass**

Phiếu đòi đúng chuỗi: *"Đã nạp {số thành công} bản ghi thành công, {số lỗi} bản ghi không hợp lệ"*.

Đặc tả **im lặng về câu chữ**: `:595` chỉ ghi *"Trả về báo cáo import"*; **bảng Error Handling `:633`–`:643`
không có dòng thông báo thành công nào** (9 dòng đều là `ERROR`); AC `:650` chỉ ghi *"validate + import + báo cáo lỗi"*.
Đã đọc trọn mục xử lý (`:586`–`:596`), bảng lỗi (`:631`–`:645`) và trọn khối AC (`:647`–`:660`) — không có chỗ nào quy định câu chữ báo thành công.

Web hiện tại: **"Import hoàn tất — Đã nhập 3 · Bỏ qua 0 · Lỗi 2"**. Tức **có đủ hai con số** mà phiếu đòi
(3 thành công, 2 không hợp lệ), nhưng **khác câu chữ**, và có thêm một chỉ số thứ ba ("Bỏ qua").

🔴 Theo flow 04 luật khóa 5, **không được hạ `GAP` xuống `MATCH`** để chấm Pass chỉ vì "web đã làm đủ ý".
Quan hệ này đã khóa trước khi mở màn, và khi đo xong **không tìm thấy dòng đặc tả mới** nào quy định câu chữ ⇒ giữ nguyên `GAP`.

## 4. Verdict

**Cần BA** → ô `Trạng thái dev fix` = **`BA confirm`** (theo `QUYET-DINH-DIEU-PHOI.md` QĐ-01: không còn vế `MATCH` nào lỗi, nhưng còn vế `GAP` ⇒ Cần BA, không phải `Test done`).

- 3/3 vế `MATCH` (C1, C2, C3) **đều đạt** — trong đó **C2 là lỗi cũ, nay đã hết**.
- 1 vế `GAP` (G1) chặn Pass sạch. **Không chặn bàn giao** — chỉ cần nghiệp vụ chốt câu chữ.
- ⚠️ Theo flow 04 §Ca biên: **không có ảnh "lỗi cũ" do chính đội chụp trước khi dev sửa** ở vế C3 ⇒ chỉ kết luận được **hiện trạng đúng đặc tả**, không kết luận "bản sửa đã có tác dụng". Riêng C2 thì có mốc so sánh thật (lượt 02:20 cùng ngày, cùng đội đo).

## 5. Dữ liệu đã thay đổi trên môi trường (bắt buộc khai)

| Đổi gì | Bản ghi nào | Env |
|---|---|---|
| Ghi **3 bản ghi điểm danh** (`CO_MAT`, `VANG_PHEP`, `VANG_KHONG_PHEP`) | Buổi 4 (`bd1cdf35…c8c2`) của khóa `KH-QAW7-HOINGHI` | `18.143.165.120.nip.io` (nội bộ) |

Đây là **hệ quả trực tiếp của chính thao tác đang verify**, không phải seed thêm.
🔴 **Hệ quả:** khóa `KH-QAW7-HOINGHI` nay **không còn buổi nào sạch** (4/4 buổi đã có dữ liệu điểm danh).
Lượt verify sau muốn đo lại phiếu này **phải tạo buổi học mới** hoặc dùng khóa khác ở `DANG_DIEN_RA`.

## 6. Quan sát ngoài vế — ghi candidate, KHÔNG log thành bug

| # | Hiện tượng | Xuất hiện tại | Vì sao chỉ là candidate |
|---|---|---|---|
| 1 | Danh sách điểm danh **không có cột mã học viên** (cột hiển thị: STT · Họ tên · Email · SĐT · Đơn vị · Trạng thái · Ghi chú; phản hồi máy chủ có `hocVienId` dạng UUID nhưng không có mã dạng người đọc) | tab Điểm danh, ảnh 06 | Đây **đúng ý nghiệp vụ đã chốt** ở `:14` (*"KHÔNG thêm trường vào entity HOC_VIEN"*) ⇒ **không phải lỗi**. Ghi lại vì đó là khiếu nại gốc của đối tác, để người đọc không tưởng bị bỏ qua |
| 2 | Giao diện dùng từ tiếng Anh "Import" trong nhãn tiếng Việt ("Import điểm danh từ Excel", "Import hoàn tất", nút "Import Excel") | hộp thoại nạp tệp, ảnh 03/04 | Đặc tả cũng dùng từ "import" trong mô tả nghiệp vụ; phiếu này **không có vế nào về tính đồng nhất ngôn ngữ** ⇒ không thuộc phạm vi chấm. Không thêm phép đo |

Cả hai **không đổi verdict** vì không chặn điều kiện đạt của vế nào.
