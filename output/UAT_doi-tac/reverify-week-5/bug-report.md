# Bug Report — Hồ sơ pháp lý DN / Biểu mẫu (tuần 5 · verify bug dev đã fix)

| Thông tin | Giá trị |
|-----------|---------|
| **Dự án** | Phần mềm Hỗ trợ pháp lý doanh nghiệp (PM HTPLDN) |
| **Môi trường** | https://18.143.165.120.nip.io — **env nội bộ**, KHÔNG phải env nghiệm thu của đối tác (`htpldn-uat.ospgroup.vn`) |
| **Bản dựng** | `HTPLDN · V1.0.8` · bó mã FE `assets/index-DIABnbIr.js` (+ `assets/index-DVlgOkLg.css`, `assets/index-DNsk8fKL.css`) · `GET /` `last-modified: Thu, 06 Aug 2026 07:13:15 GMT` (14:13:15 giờ VN) · `etag W/"6a74340b-428"`. Đọc lại sau khi tải lại trang bỏ qua bộ nhớ đệm lúc 18:54 — **trùng khít vân tay lô B7 cùng ngày** ⇒ FE chưa deploy lại kể từ 14:13 |
| **Người test** | QA (Chrome DevTools MCP) |
| **Ngày** | 2026-08-06 19:41:00 |
| **Loại test** | Verify bug dev đã fix (flow `flows/04-verify-bug-dev-fix-khong-ho-so.md`) |
| **Round** | Tuần 5 — vòng verify 2026-08-06 |
| **Tài liệu tham chiếu** | [bao-cao-dot-2026-08-06.md](bao-cao-dot-2026-08-06.md) (báo cáo cuối đợt 4 mục) · [BAN-DUNG.md](BAN-DUNG.md) · [tieuchi/QLHSPLDN_06.md](tieuchi/QLHSPLDN_06.md) · [tieuchi/QLHSPLDN_07.md](tieuchi/QLHSPLDN_07.md) · [tieuchi/QLBMHD_02.md](tieuchi/QLBMHD_02.md) · [ba-confirm/cau-hoi-ba-tuan-5.md](ba-confirm/cau-hoi-ba-tuan-5.md) · SRS `srs-v3.5/srs-fr-12-tv-chuyen-sau.md` · `srs-v3.5/srs-fr-07-doanh-nghiep.md` · `srs-v3.5/srs-fr-10-quan-tri.md` · `srs-v3.5/srs-fr-09-bieu-mau.md` · `srs-v3.5.md` Phụ lục E §H6 |

---

## Tổng hợp

Phạm vi đợt: lọc tab `bug` theo `Dopai = dev done` **và** `Trạng thái dev fix = fixed` → **7 dòng**. Không
module nào đủ 3 case (nhiều nhất là `QLHSPLDN` với 2) ⇒ chạy **2 module / 3 case**: `QLHSPLDN_06` (dòng 291) ·
`QLHSPLDN_07` (dòng 292) · `QLBMHD_02` (dòng 138).

- **QLHSPLDN_06** (dòng 291 — *"Xem"*, case **gộp 4 vế**): **Pass**. N = **7/7 hàng đo hết, đếm thô** ×
  **M = 4/4 dạng** (có tệp · không tệp · đủ 3 trạng thái · trường tuỳ chọn trống) = 3 lượt bấm mở thật +
  3 lượt đối chứng đọc lại bản ghi qua máy chủ. Cả 4 vế đều hết lỗi: có chức năng mở chi tiết ở **mọi** hàng ·
  bấm mở được thật · nội dung khớp **10/10 trường** với bản ghi gốc · liệt kê đúng tệp đính kèm · cửa sổ
  **0 ô nhập, không nút lưu** ⇒ vế "chỉ đọc" hết bất đồng, không phải hỏi BA.

- **QLHSPLDN_07** (dòng 292 — *"Sửa"*, case **gộp 3 vế**): **Pass**. N = **2 bản ghi** (1 cũ có sẵn tệp +
  1 mới tạo trong phiên sau bản vá) × **4 lượt bấm lưu**, phủ **M = 5/5 dạng** (D1 chỉ-thêm-tệp · D2 chữ +
  chữ dài · D3 ngày · D4 ô chọn/enum/FK · D5 bản ghi mới vs cũ). Mỗi lượt đo **2 đường độc lập và cả 2 khớp**
  (tải lại trang bỏ đệm rồi mở lại · đọc lại bản ghi từ máy chủ theo đúng đường dẫn giao diện phát ra).
  **Triệu chứng đối tác không tái hiện**: lượt lặp y hệt video (chỉ thêm 1 tệp, không đụng ô nào) cho ra
  **đủ 2 tệp** ở cả 2 đường. Vế (c) đóng bằng **Nhật ký hệ thống** (`SCR-VIII-10`): đủ **5 dòng** ứng đúng
  5 thao tác, đúng giây bấm, đúng người dùng + đơn vị + mã bản ghi.

- **QLBMHD_02** (dòng 138 — *"Kiểm tra hiển thị các trường thông tin"*, case **gộp 3 vế**): **Pass**.
  Đo theo **bản đặc tả BA đã cập nhật cho chính phiếu này** (dấu `[STT12]`): cột *Cơ quan ban hành* (`:671`)
  đã có, **27/27 bản ghi** có giá trị, **2 đơn vị khác nhau** (19 + 8) ⇒ bám `don_vi_id` của **bản ghi** chứ
  không phải của người đăng nhập, đối chứng phản hồi máy chủ **0/20 dòng lệch**; bộ lọc *Định dạng* (`:654`)
  đúng `doc/docx/xls/xlsx`, mặc định *"Tất cả"*, **đã bỏ "PDF"**, lọc `XLSX` ra **3/3**; cột *Loại tài liệu*
  (`:657`) đúng dạng **Icon doc/xls**; **0** ô tích chọn — khớp danh sách **đóng 22 thành phần** và khớp
  quyết định BA **24/07 Loại 3 — không sửa**. Bản dựng đối tác chụp (`V1.0`) khi đó **không có**
  `Cơ quan ban hành` ⇒ đúng thứ họ log, và nay đã hết.

> **Kết quả chỉ có hiệu lực cho env nội bộ + bản dựng ghi ở đầu file.** Đối tác đo trên env nghiệm thu
> `htpldn-uat.ospgroup.vn` bản `HTPLDN · V1.0.3` ⇒ Pass ở đây là **Pass tạm**, phải xác nhận lại khi bản dựng
> này lên env nghiệm thu.

### Severity breakdown

| Tổng | Critical | Major | Medium | Minor | Trivial | Closed | Open |
|------|----------|-------|--------|-------|---------|--------|------|
| 3    | 0        | 1     | 1      | 1     | 0       | 3      | 0    |

## Bug Summary Table

| Bug ID | Severity | Priority | Type | TC Ref | **SRS Reference** | Title | Status |
|--------|----------|----------|------|--------|-------------------|-------|--------|
| ~~BUG-HSPLDN-QLHSPLDN-06~~ | Minor | P3 | UI/UX | QLHSPLDN_06 (tab `bug` dòng 291) | `FR-X.1-04 §Mô tả` (`srs-fr-12-tv-chuyen-sau.md:550`) · `§Processing — Xem chi tiết` (:634, :640-:642) · `§AC` (:693) · `SCR-V.III-02 tab Hồ sơ PL` (`srs-fr-07-doanh-nghiep.md:459`, :468) · Phụ lục E §H6 (`srs-v3.5.md:6714`) | Bảng Hồ sơ pháp lý DN trong chi tiết doanh nghiệp không có chức năng mở chi tiết hồ sơ (cột Hành động chỉ có Sửa / Xoá) | **Closed** |
| ~~BUG-HSPLDN-QLHSPLDN-07~~ | Major | P2 | Chức năng | QLHSPLDN_07 (tab `bug` dòng 292) | `FR-X.1-04 §Processing — Chỉnh sửa` (`srs-fr-12-tv-chuyen-sau.md:607`, :613, :614) · `§Postconditions` (:674, :676) · `§AC` (:695, :701) · `§Inputs Thêm mới/Chỉnh sửa` (:560-574) · `SCR-V.III-02 tab Hồ sơ PL` (`srs-fr-07-doanh-nghiep.md:459`, :468) · `BR-DATA-05` (`srs-fr-07:819-821`) · `SCR-VIII-10 Nhật ký hệ thống` (`srs-fr-10-quan-tri.md:1365`, :1371, :1373) · `UI-04`/`UI-10` (`srs-v3.5.md:576`, :582) | Cửa sổ Sửa hồ sơ pháp lý DN báo "Cập nhật hồ sơ thành công" nhưng bản ghi không được cập nhật (tệp vừa thêm biến mất khi mở lại) | **Closed** |
| ~~BUG-BM-QLBMHD-02~~ | Medium | P3 | UI/UX | QLBMHD_02 (tab `bug` dòng 138) | `SCR-VII-02 §Thành phần màn hình` (`srs-fr-09-bieu-mau.md:650-673`) — #20 Cột Cơ quan ban hành (:671 `[STT12]`) · #3 bộ lọc Định dạng (:654) · #6 Cột Loại tài liệu (:657) · `FR-VII-04 §Inputs #14` (:315 `[STT12]`) · `Entity BIEU_MAU #16` (:796 `[STT12]`) · `SCR-VII-01 checkbox` (:624, :630) | Màn Danh sách biểu mẫu thiếu cột Cơ quan ban hành + thông tin định dạng (kèm điểm phụ ô tích chọn từng dòng) | **Closed** |

---

## ~~BUG-HSPLDN-QLHSPLDN-06~~ [CLOSED] — Bảng Hồ sơ pháp lý DN trong chi tiết doanh nghiệp không có chức năng mở chi tiết hồ sơ (cột Hành động chỉ có Sửa / Xoá)

> **Re-test:** 2026-08-07 13:22 — ✅ PASS trên env nghiệm thu `htpldn-uat.ospgroup.vn` (bó mã
> `assets/index-D4NhKEjr.js`, `last-modified Fri, 07 Aug 2026 04:17:55 GMT`, vân tay 2 đầu phiên trùng khớp),
> tài khoản `cbnv_tw`, đo 13:08→13:22 giờ VN. Cột Hành động có nút "Xem" ở **7/7 hàng** trên cả bảng DN QA lẫn
> chính bảng `DN-XX-0005` của đối tác; 5 lượt bấm thật phủ đủ D1–D4 mở được cửa sổ chi tiết, khớp **10/10 trường**
> với bản ghi đọc lại qua máy chủ, tệp liệt kê đúng tên + số lượng, cửa sổ **0 ô nhập / 0 nút lưu** ⇒ câu
> "Pass tạm cho tới khi bản dựng lên môi trường nghiệm thu" của vòng trước đã đóng.

### Mô tả

Trên màn *Chi tiết doanh nghiệp* (`SCR-V.III-02`, `srs-fr-07-doanh-nghiep.md:455`), thẻ **Hồ sơ pháp lý**
(`/doanh-nghiep/{id}?tab=ho-so-pl`) là nơi **duy nhất** còn thực thi `FR-X.1-04` — màn cũ `SCR-X1-03` đã bị
gỡ (`srs-fr-12-tv-chuyen-sau.md:547`, :1176). Đặc tả yêu cầu chức năng này gồm cả **"xem chi tiết"**
(`srs-fr-12:550`) với khối xử lý riêng *Xem chi tiết* (`:634`) phải **trả full record** (`:640`) và **danh
sách tệp đính kèm kèm tên / loại / dung lượng / URL xem trước** (`:641`, `:642`); tiêu chí chấp nhận `:693`
ghi rõ *"Given CB NV xem chi tiết hồ sơ When chọn bản ghi Then hiển thị đầy đủ thông tin + file đính kèm"*.

Đối tác báo trên bản dựng `HTPLDN · V1.0.3` (env nghiệm thu) cột **Hành động** của bảng chỉ có **2 nút
`Sửa` và `Xoá`** — không có bất kỳ điều khiển nào để mở chi tiết hồ sơ, nên thao tác *"Nhấn Xem"* ở bước 4
của phiếu không thực hiện được.

### Các bước tái hiện

1. Đăng nhập vai trò **Cán bộ Nghiệp vụ Trung ương** (`CB_NV_TW`) — ô *Tác nhân* của đặc tả là *"Cán bộ
   Nghiệp vụ (TW/BN/ĐP), Người hỗ trợ"* (`srs-fr-12:552`).
2. Menu trái → **Doanh nghiệp**.
3. Trên một doanh nghiệp bất kỳ trong phạm vi đơn vị, bấm nút mở chi tiết.
4. Chọn thẻ **Hồ sơ pháp lý**.
5. Nhìn cột **Hành động** của các hàng trong bảng *Hồ sơ pháp lý DN*.

### Kết quả mong đợi

Mỗi hàng hồ sơ có điều khiển mở chi tiết; bấm vào mở cửa sổ hiển thị **toàn bộ thông tin hồ sơ** cùng
**danh sách tệp đính kèm (nếu có)** ở **chế độ chỉ đọc** — theo `srs-fr-12:550`, `:640`, `:641`, `:642`,
`:693` và ô *Kết quả mong đợi* của phiếu.

### Kết quả thực tế

**Trên bản dựng đối tác chụp (`V1.0.3`, env nghiệm thu, 03/08/2026 10:03):** cột Hành động của **cả 2 hàng**
chỉ có `Sửa` và `Xoá`. Cột nằm sát mép phải và hiện đủ 2 nút ⇒ không phải do chưa cuộn ngang.

**Trên bản dựng đo lại (`V1.0.8`, env nội bộ, 06/08/2026 18:54→18:59): đã hết lỗi.**

| Nhóm đo | Số đo |
|---|---|
| Số hàng của bảng (đếm thô `.ant-table-tbody tr.ant-table-row`) | **7** |
| Số nút mở chi tiết trong ô Hành động (đếm thô) | **7** — mỗi hàng đúng 1 nút `Xem`; ô Hành động nay có 3 nút `Xem` · `Sửa` · `Xoá` |
| Cách đếm độc lập thứ hai (quét biểu tượng con mắt trong thân bảng) | **7** — khớp |
| Trạng thái từng nút | `disabled = false` · không `aria-disabled` · `pointer-events: auto` · `opacity: 1` · kích thước thật **68 × 24 px** · nằm trong khung nhìn |
| Bấm thật qua giao diện | 3 lượt (3 dạng dữ liệu) → cả 3 mở lớp nổi **"Chi tiết hồ sơ pháp lý"** |
| Đối chiếu từng trường với bản ghi đọc lại từ máy chủ | **10/10 trường khớp** ở cả 3 hồ sơ (mã · tên · loại · lĩnh vực · nguồn · cơ quan cấp · ngày cấp · ngày hết hạn · trạng thái · mô tả) |
| Tệp đính kèm | Hồ sơ có tệp: cửa sổ liệt kê **1 tệp** `QA-EDIT-A-tep-moi.png (191 B)` — máy chủ trả đúng 1 tệp cùng tên, dung lượng 191 byte ⇒ khớp cả **số tệp + tên + dung lượng** |
| Hồ sơ không tệp | Cửa sổ vẫn mở, hiện trạng thái rỗng **"Chưa có tệp đính kèm"**, không trắng, không lỗi |
| Chế độ chỉ đọc | Đếm thô ô nhập trong cửa sổ (`input`/`textarea`/`select`/`.ant-select`/`.ant-picker`/`[contenteditable]`) = **0** ở cả 3 lượt; nút của cửa sổ chỉ có `Xem`/`Tải` (thao tác trên tệp) và `Đóng` — **không nút lưu** |
| Bảng điều khiển trình duyệt | **0** thông điệp lỗi / cảnh báo trong suốt luồng |

Nhãn hiển thị đã dịch đúng tiếng Việt, **không** lọt mã enum thô (`GIAY_PHEP` → *Giấy phép*, `HIEU_LUC` →
*Hiệu lực*, `THU_CONG` → *Thủ công*); ngày theo `dd/mm/yyyy` đúng `srs-fr-12:663`, `:664`.

### Bằng chứng

| Tệp | Thấy gì trong ảnh |
|---|---|
| [`image/QLHSPLDN_06-D1-chitiet-HSPL-20260803-0001-co-tep.png`](image/QLHSPLDN_06-D1-chitiet-HSPL-20260803-0001-co-tep.png) | Lớp nổi *Chi tiết hồ sơ pháp lý* của `HSPL-20260803-0001`: đọc được 10 trường (Mã hồ sơ · Tên hồ sơ · Loại hồ sơ *Giấy phép* · Lĩnh vực *Thuế* · Nguồn *Thủ công* · Cơ quan cấp · Ngày cấp `01/08/2026` · Ngày hết hạn `31/12/2026` · Trạng thái *Hiệu lực* · Mô tả) và mục **Tệp đính kèm** liệt kê `QA-EDIT-A-tep-moi.png (191 B)` kèm 2 nút *Xem* / *Tải*; chân cửa sổ chỉ có nút **Đóng** |
| [`image/QLHSPLDN_06-D2D4-chitiet-HSPL-20260803-0002-khong-tep-truong-trong.png`](image/QLHSPLDN_06-D2D4-chitiet-HSPL-20260803-0002-khong-tep-truong-trong.png) | Cùng lớp nổi cho `HSPL-20260803-0002` (trạng thái *Thu hồi*, không tệp): 5 trường trống hiển thị `—` chứ không phải `null`/`undefined`, mục tệp hiện chữ **"Chưa có tệp đính kèm"**, cửa sổ không vỡ |
| [`image/QLHSPLDN_06-D3-chitiet-HSPL-20260721-0001-het-han.png`](image/QLHSPLDN_06-D3-chitiet-HSPL-20260721-0001-het-han.png) | Hồ sơ `HSPL-20260721-0001` trạng thái **Hết hạn** vẫn mở được cửa sổ chi tiết, có tệp `QA-EDIT-A-tep-moi.png (191 B)` ⇒ nút không biến mất theo trạng thái |
| [`tieuchi/QLHSPLDN_06.md`](tieuchi/QLHSPLDN_06.md) §7 | Bảng số đo đầy đủ theo 5 nhóm tiêu chí A–E + vân tay bản dựng + khai tài khoản thực dùng |
| [`partner-evidence/QLHSPLDN_06.jpg`](partner-evidence/QLHSPLDN_06.jpg) | Ảnh đối tác (1915×1041): env `htpldn-uat.ospgroup.vn`, DN `#DN-XX-0005`, thẻ *Hồ sơ pháp lý*, cột Hành động của cả 2 hàng **chỉ có `Sửa` và `Xoá`**, bản dựng `HTPLDN · V1.0.3` |

---

## ~~BUG-HSPLDN-QLHSPLDN-07~~ [CLOSED] — Cửa sổ Sửa hồ sơ pháp lý DN báo "Cập nhật hồ sơ thành công" nhưng bản ghi không được cập nhật (tệp vừa thêm biến mất khi mở lại)

> **Re-test:** 2026-08-07 13:57 — ✅ PASS trên env nghiệm thu `htpldn-uat.ospgroup.vn` (bó mã `assets/index-D4NhKEjr.js`, vân tay đầu/cuối phiên 13:37→13:57 trùng khớp), tài khoản `cbnv_tw`: 4 lượt bấm `Đồng ý` trên 2 hồ sơ QA tự tạo (`HSPL-20260807-0004` có sẵn tệp trước thao tác + `HSPL-20260807-0005` mới tạo), phủ đủ D1–D5 gồm dạng chỉ-thêm-1-tệp mà 2 vòng trước bỏ sót; mỗi lượt khớp ở **cả 2 đường độc lập** (tải lại trang thật bỏ đệm + đọc lại bản ghi từ máy chủ theo đúng đường UI phát ra), thông báo ↔ request khớp loại 4/4, vế (c) đóng bằng Đường A với 4 dòng `Cập nhật` đúng giây bấm trên màn Nhật ký hệ thống. Ghi chú "Pass tạm" của vòng env nội bộ nay đã đóng; chưa loại trừ được chiều "bản ghi tạo trước bản vá" vì env nghiệm thu không có bản ghi QA cũ hơn bản dựng.

### Mô tả

Case gộp **3 vế**: (a) cửa sổ chỉnh sửa mở kèm dữ liệu hiện có · (b) bấm lưu thì hệ thống **cập nhật bản
ghi** · (c) bấm lưu thì **lưu vết thao tác**. Đối tác báo vế (b) hỏng: *"Hệ thống hiển thị thông báo cập nhật
thành công nhưng dữ liệu chưa được cập nhật vào bản ghi"*.

Đặc tả yêu cầu rõ: khối `Processing — Chỉnh sửa` (`srs-fr-12-tv-chuyen-sau.md:607`) gồm bước **cập nhật bản
ghi hồ sơ** (`:613`) và bước **ghi nhật ký thao tác** (`:614`, `BR-DATA-05`); Postconditions `:674` *"Hồ sơ
được tạo/cập nhật/xóa mềm trong CSDL"* + `:676` *"AUDIT_LOG ghi nhận mọi thao tác CUD"*; tiêu chí chấp nhận
`:695` và `:701` (*"upload file + nhấn Lưu → validate, cập nhật, AUDIT_LOG ghi `nguoi_thuc_hien_id`"*). Ô
`file_dinh_kem` nằm trong bảng Inputs áp cho **"Thêm mới / Chỉnh sửa"** (`:560`, `:574`). Về thông báo,
`srs-v3.5.md:576` cho phép toast thành công cho thao tác thành công, còn `:582` (UI-10) cấm **"nuốt lỗi trong
im lặng"** ⇒ báo thành công trong khi không lưu được là sai **loại** thông báo, không phải sai chữ.

### Các bước tái hiện

1. Đăng nhập vai trò **Cán bộ Nghiệp vụ Trung ương** (`CB_NV_TW`, cấp TW).
2. Menu trái → **Doanh nghiệp** → mở chi tiết một doanh nghiệp trong phạm vi đơn vị → thẻ **Hồ sơ pháp lý**.
3. Chọn một hồ sơ **thuộc đơn vị mình** và **đã có sẵn ≥ 1 tệp đính kèm** → bấm **Sửa**.
4. Ở mục *Tệp đính kèm*, thêm **đúng 1 tệp**; **không** sửa ô nào khác.
5. Bấm **Đồng ý** → hệ thống hiện thông báo *"Cập nhật hồ sơ thành công"*.
6. Mở lại cửa sổ **Sửa** của **chính** hồ sơ đó, cuộn xuống mục *Tệp đính kèm*.

### Kết quả mong đợi

Bản ghi được cập nhật thật: tệp vừa thêm còn nguyên khi đọc lại (mở lại sau khi **tải lại trang** và khi
**đọc lại bản ghi từ máy chủ**), các ô khác giữ đúng giá trị đang có; thao tác để lại **dấu vết trong nhật ký**
(`srs-fr-12:613`, `:614`, `:674`, `:676`, `:695`, `:701`). Thông báo hiển thị phải **cùng loại với kết quả
thật** (`srs-v3.5.md:576`, `:582`).

### Kết quả thực tế

**Trên bản dựng đối tác quay (`V1.0.3`, env nghiệm thu, 03/08/2026 10:06):** sau khi thêm tệp
`QLHSPLDN_07.jpg` (213.3 KB) và bấm `Đồng ý`, hệ thống hiện *"Cập nhật hồ sơ thành công"*; mở lại cửa sổ Sửa
của chính hồ sơ thì mục Tệp đính kèm **chỉ còn 1 tệp** cũ — tệp vừa thêm biến mất (khung `t013.33s.jpg`).

**Trên bản dựng đo lại (`V1.0.8`, env nội bộ, 06/08/2026 19:05→19:24): cả 3 vế đều đạt, triệu chứng không
tái hiện.**

| Vế / lượt đo | Số đo |
|---|---|
| **(a)** mở cửa sổ Sửa | Cả 2 bản ghi: **9/9 ô** trên form khớp từng giá trị đọc lại từ máy chủ; danh sách tệp khớp **đúng số tệp + tên + dung lượng** |
| **Lượt 1 — D1 trên bản ghi CŨ** (thao tác y hệt đối tác: thêm đúng 1 tệp, không đụng ô nào) | `SO_REQUEST = 1` (`PATCH …/5bd8169a-…`) ↔ `SO_KHUNG = 1` (*"Cập nhật hồ sơ thành công"*) · đường (i) tải lại trang → **2 tệp** · đường (ii) đọc lại bản ghi → **2 tệp** gồm tệp vừa thêm ⇒ **hai đường khớp, không mất dữ liệu** |
| **Lượt 2 — D2+D3+D4 trên bản ghi CŨ** (8 ô + 1 tệp, 1 lần bấm) | 1 request ↔ 1 thông báo · **8/8 ô mang giá trị mới** + **3 tệp** ở cả (i) và (ii) |
| **Lượt 3a — D1 trên bản ghi MỚI** `HSPL-20260806-0001` (tạo 19:12:03 bằng UI thật) | 1 request ↔ 1 thông báo · (i) **2 tệp** · (ii) **2 tệp** ⇒ bản ghi tạo **sau bản vá** cũng lưu đúng |
| **Lượt 3b — D2+D3+D4 trên bản ghi MỚI** | 1 request ↔ 1 thông báo · **8/8 ô mang giá trị mới** (`QA-W5-1926 …` · *Quyết định* · *Lao động* · `07/03/2026` · `05/08/2026` · *Hết hạn*) + **3 tệp** ở cả (i) và (ii) |
| **(c)** nhật ký thao tác — **Đường A** (`SCR-VIII-10`, đọc bằng `admin`) | Đủ **5 dòng** khớp 5 thao tác: `19:05:18` *Cập nhật* `5bd8169a…` · `19:09:45` *Cập nhật* `5bd8169a…` · `19:12:03` *Tạo mới* `11a5f733…` · `19:16:57` *Cập nhật* `11a5f733…` · `19:22:13` *Cập nhật* `11a5f733…`; mọi dòng `Người dùng = CB Nghiệp vụ - Trung ương`, `Đơn vị = Cục Bổ trợ tư pháp - Bộ Tư pháp`, `Entity = HO_SO_PHAP_LY_DN` |
| **(c)** đối chứng phụ — Đường B | `nguoiCapNhatId` = đúng tài khoản vừa bấm ở cả 2 bản ghi; `ngayCapNhat` = đúng giây bấm ở các lượt có sửa ô (xem *Quan sát ghi nhận thêm* mục 3 cho lượt chỉ-thêm-tệp) |

Bộ bắt thông báo dùng `tools/toast-capture.js` (không lọc trùng, đọc bằng `innerText`, đếm cả `fetch` lẫn
`XMLHttpRequest`), cài **trước** mỗi lần bấm và tự kiểm `soObserverDangSong = 1`; **không lượt nào** có
thông báo lặp hay request kép.

### Bằng chứng

| Tệp | Thấy gì trong ảnh |
|---|---|
| [`image/QLHSPLDN_07-D1-sau-tai-lai-trang-2-tep.png`](image/QLHSPLDN_07-D1-sau-tai-lai-trang-2-tep.png) | Lượt 1 (D1, bản ghi cũ) — **sau khi tải lại trang** và mở lại cửa sổ Sửa: mục Tệp đính kèm hiện **2 tệp**, gồm tệp vừa thêm ⇒ đúng chỗ đối tác thấy mất |
| [`image/QLHSPLDN_07-D2D3D4-sau-tai-lai-trang-8-o-doi-3-tep.png`](image/QLHSPLDN_07-D2D3D4-sau-tai-lai-trang-8-o-doi-3-tep.png) | Lượt 2 — sau khi tải lại trang: 8 ô mang giá trị mới `QA-W5-1911 …` + **3 tệp** |
| [`image/QLHSPLDN_07-D5-luot3-sau-tai-lai-trang-2-tep.png`](image/QLHSPLDN_07-D5-luot3-sau-tai-lai-trang-2-tep.png) | Lượt 3a (D1 trên **bản ghi mới tạo sau bản vá**) — sau khi tải lại trang: **2 tệp** `QA-W5-1907-tep-luot4.png (73 B)` + `…luot3.png (79 B)`; chân sidebar `HTPLDN · V1.0.8` |
| [`image/QLHSPLDN_07-D5-luot3b-sau-tai-lai-trang-8-o-doi-3-tep.png`](image/QLHSPLDN_07-D5-luot3b-sau-tai-lai-trang-8-o-doi-3-tep.png) | Lượt 3b — sau khi tải lại trang: *Lao động* · `07/03/2026` · `05/08/2026` · `QA-W5-1926 coquan` · *Hết hạn* · `QA-W5-1926 mota` + **3 tệp** |
| [`image/QLHSPLDN_07-veC-nhat-ky-he-thong-5-dong-thao-tac.png`](image/QLHSPLDN_07-veC-nhat-ky-he-thong-5-dong-thao-tac.png) | Màn **Nhật ký hệ thống** đọc bằng `admin`: 5 dòng `19:05:18` / `19:09:45` / `19:12:03` / `19:16:57` / `19:22:13` với `Entity HO_SO_PHAP_LY_DN`, mã bản ghi `5bd8169a…` và `11a5f733…` |
| [`tieuchi/QLHSPLDN_07.md`](tieuchi/QLHSPLDN_07.md) §7 | Vân tay bản dựng · tài khoản thực dùng + lý do lệch so với tài khoản gợi ý · danh sách bản ghi đã dùng / đã seed |
| [`partner-evidence/QLHSPLDN_07-2.webm`](partner-evidence/QLHSPLDN_07-2.webm) | Video 17,2 s của đối tác — mốc 00:03 thấy 2 tệp trước khi lưu, mốc 00:13 mở lại chỉ còn 1 tệp (khung đã trích ở `frames/QLHSPLDN_07/`) |

---

## ~~BUG-BM-QLBMHD-02~~ [CLOSED] — Màn Danh sách biểu mẫu thiếu cột Cơ quan ban hành + thông tin định dạng (kèm điểm phụ ô tích chọn từng dòng)

> **Re-test:** 2026-08-06 19:33→19:41 — ✅ **PASS** (Closed-verified) · env nội bộ
> `18.143.165.120.nip.io` · bản dựng `HTPLDN · V1.0.8`, bó mã `assets/index-DIABnbIr.js`,
> `last-modified Thu, 06 Aug 2026 07:13:15 GMT`, `etag W/"6a74340b-428"` (trùng khít lô 18:44 và lượt
> `QLHSPLDN_07` 19:24 ⇒ FE không deploy lại giữa đợt) · tài khoản `cbnv_tw` (`CB_NV_TW`, cấp TW, đơn vị
> `00000000-0000-4000-8000-000000000001`), **không** phải tài khoản dự phòng · dữ liệu: **27 biểu mẫu**
> (19 *Cục Bổ trợ tư pháp - Bộ Tư pháp* + 8 *Bộ Kế hoạch và Đầu tư*; 24 DOCX + 3 XLSX) · biến thể đã phủ
> **D1** bản ghi cùng đơn vị · **D2** bản ghi **khác** đơn vị · **D3** nhóm Word · **D4** nhóm Excel ·
> **D5** bản ghi cũ (15/07→25/07) + **1 bản ghi tạo mới trong lượt đo**.
> **Đo theo bản đặc tả BA ĐÃ CẬP NHẬT cho chính phiếu này (dấu `[STT12]`), cả 3 vế đều đạt:** cột
> *Cơ quan ban hành* (:671) đã có và đúng đơn vị **từng bản ghi** — 27/27, đối chứng máy chủ 0/20 dòng lệch ·
> bộ lọc *Định dạng* (:654) đúng `doc/docx/xls/xlsx`, mặc định *"Tất cả"*, **đã bỏ "PDF"** · cột *Loại tài liệu*
> (:657) đúng dạng **Icon doc/xls** · **không** ô tích chọn — khớp danh sách đóng 22 thành phần, và khớp
> quyết định BA **2026-07-24 Loại 3 — không sửa** (câu trả lời cho đối tác đã nằm sẵn ở ô *DEV phản hồi lần 1*
> của dòng 138).
> **Đã seed:** tạo `BM-20260806-001` *"QA-W5-1936 BM moi trong luot do"* (thư mục `QA-R7-A-CO-BM`, tệp
> `QA-W5-QLBMHD02-bieu-mau-moi.xlsx` 4.869 B) bằng **UI thật**, trên env nội bộ; không đụng dữ liệu đối tác.
> **Hiệu lực:** chỉ cho env nội bộ + bản dựng trên; đối tác chụp trên env nghiệm thu bản `HTPLDN · V1.0`.

### Mô tả

Case gộp **3 vế** theo ô *Kết quả thực tế* của phiếu: (a) thiếu cột **Cơ quan ban hành** · (b) thiếu cột
**Định dạng** · (c) thiếu **ô tích chọn** biểu mẫu từng dòng. Màn tranh chấp là *Biểu mẫu → Danh sách biểu
mẫu* (`SCR-VII-02`, `/bieu-mau/danh-sach`).

Đặc tả `srs-fr-09-bieu-mau.md:650-673` liệt kê **đóng 22 thành phần** của màn: `:671` bắt buộc **Cột Cơ quan
ban hành** *"luôn hiển thị"*, giá trị lấy theo `don_vi_id` của **bản ghi** (`:796`, `:315`); `:657` là **Cột
Loại tài liệu** thể hiện bằng *"Icon doc/xls"*; `:654` là **bộ lọc Định dạng** (doc/docx/xls/xlsx). Trong
danh sách đóng đó **không có** thành phần nào tên *"Cột Định dạng"*, cũng **không có** ô tích chọn — trong
khi màn anh em `SCR-VII-01` (Thư mục) lại khai rõ checkbox (`:624`) + thanh hành động hàng loạt (`:630`).

### Các bước tái hiện

1. Đăng nhập vai trò **Cán bộ Nghiệp vụ Trung ương** (`CB_NV_TW`, cấp TW).
2. Menu trái → **Biểu mẫu → Danh sách biểu mẫu** (`/bieu-mau/danh-sach`), tải lại trang.
3. Đọc **toàn bộ** nhãn hàng tiêu đề của bảng (kể cả cột dính bên phải và phần phải cuộn ngang mới thấy).
4. Đọc ô *Cơ quan ban hành* của **từng hàng**, không lấy mẫu.
5. Mở điều khiển lọc **Định dạng** trên thanh lọc, đọc toàn bộ lựa chọn; chọn `XLSX` rồi bấm **Tìm kiếm**;
   sau đó bấm **Xóa bộ lọc**.
6. Đếm ô tích chọn trong bảng và xem thanh công cụ có nhóm nút thao tác hàng loạt cấp biểu mẫu không.

### Kết quả mong đợi

Cột **Cơ quan ban hành** luôn hiển thị và mang **tên đơn vị của từng bản ghi** (`:671`, `:796`); thông tin
định dạng có mặt qua **cột Loại tài liệu** (`:657`) và **bộ lọc Định dạng** đủ 4 giá trị (`:654`, `:415`);
màn **không** bắt buộc có ô tích chọn (`:650-673`).

### Kết quả thực tế

**Trên bản dựng đối tác chụp (`V1.0`, env nghiệm thu, 13/07/2026 09:54):** hàng tiêu đề đọc được 8 nhãn
`Mã BM` · `Tên biểu mẫu` · `Loại TL` · `Thư mục` · `Kích thước` · `Trạng thái` · `Đã công khai` ·
`Hành động` — **không có** `Cơ quan ban hành`, **không có** ô tích chọn.

**Trên bản dựng đo lại (`V1.0.8`, env nội bộ, 06/08/2026 19:33→19:41):**

| Vế / phép đo | Số đo |
|---|---|
| **(a)** đếm thô hàng tiêu đề (`innerText`, không lọc, không `unique`) | **12 ô**: `Mã BM` · `Tên biểu mẫu` · `Loại TL` · `Thư mục` · **`Cơ quan ban hành`** · `Kích thước` · `Trạng thái` · `Đã công khai` · `Ảnh đại diện` · `Ngày tạo` · `Sync Cổng` · `Hành động` — đúng **1** nhãn `Cơ quan ban hành` |
| **(a)** dữ liệu từng hàng | Trang 1 **20/20 hàng** có giá trị, **0** ô trống / `-` / `—` / `null` / `undefined`; đọc thêm trang 2 (7 hàng) cũng đủ ⇒ **27/27 bản ghi** |
| **(a)** giá trị bám bản ghi hay bám người xem | **2 đơn vị khác nhau** trên cùng danh sách: *Cục Bổ trợ tư pháp - Bộ Tư pháp* (19) và *Bộ Kế hoạch và Đầu tư* (8). Người đăng nhập thuộc đơn vị `…8000-000000000001`; 8 bản ghi kia mang `donViId …8001-000000000001` ⇒ cột đọc `don_vi_id` của **bản ghi**, không hard-code theo người xem |
| **(a)** đường đối chứng thứ hai | Lời gọi **do chính màn phát ra** (`list_network_requests`): `GET /api/v1/bieu-maus?page=1&pageSize=20&sortBy=ngayTao&sortOrder=DESC`. Phản hồi **có** trường `coQuanBanHanh` cho **27/27** bản ghi; so từng dòng với chữ trên màn: **0/20 dòng lệch** ⇒ không phải FE tự dựng chữ |
| **(b1)** bộ lọc định dạng | Ô lọc thứ 4 mở ra đúng **`Tất cả` · `DOC` · `DOCX` · `XLS` · `XLSX`**, trạng thái ban đầu `Tất cả` ⇒ phủ đủ 4 định dạng của `:654`/`:415` |
| **(b1)** bộ lọc có tác dụng | Chọn `XLSX` + bấm *Tìm kiếm* → **3/3 kết quả**, cả 3 hàng đều biểu tượng Excel; phản hồi `GET …?dinhDang=XLSX…` trả `total = 3`, cả 3 `dinhDang = XLSX`. Bấm *Xóa bộ lọc* → về lại **27 kết quả** |
| **(b1)** cột phân biệt định dạng | `Loại TL` hiện biểu tượng khác nhau: `file-excel` (màu xanh lá) cho XLSX ↔ `file-word` (xanh dương) cho DOCX ⇒ **phân biệt được** |
| **(b2)** cột định dạng thể hiện bằng gì | Ô cột `Loại TL` rỗng chữ (`innerText = ""`), **không** `title`, **không** tooltip; thuộc tính trợ năng là tên biểu tượng tiếng Anh `aria-label = "file-excel"` / `"file-word"` ⇒ **thuần biểu tượng — đúng y nguyên `:657`** (*"Cột Loại tài liệu · table-column · **Icon doc/xls** · luôn hiển thị"*). Đặc tả **chỉ định biểu tượng**, không chỉ định chữ ⇒ đòi thêm cột chữ là **kê yêu cầu ngoài đặc tả** |
| **(c)** ô tích chọn | Đếm thô `input[type="checkbox"]` trong bảng = **0**; thanh công cụ chỉ có `+ Thêm biểu mẫu` · `Nhập hàng loạt` · `Làm mới`, **không** có nhóm nút công khai/ẩn/xoá hàng loạt ⇒ **khớp** `:650-673` và `:652`, và khớp quyết định BA **24/07 Loại 3 — không sửa** |

### Đối chiếu với bản đặc tả BA đã cập nhật

BA **đã sửa đặc tả cho đúng phiếu này**, đánh dấu `[STT12]`. Dấu đó xuất hiện **5 chỗ** trong
`srs-fr-09-bieu-mau.md` — `:315` · `:482` · `:671` · `:672` · `:796` — và **cả 5 đều là *Cơ quan ban hành***.
Grep toàn file: **không có thành phần nào tên *"Cột Định dạng"***. ⇒ BA có đủ cơ hội thêm cột đó khi sửa đặc
tả cho chính phiếu này và **chỉ thêm 1 cột**; bản sửa đặc tả là ý chí sau cùng, thay cho câu chêm 24/07.

| Yêu cầu trong đặc tả **đã cập nhật** | Đo được trên bản dựng V1.0.8 | Đạt? |
|---|---|:-:|
| `:671` #20 — **Cột Cơ quan ban hành**, *"Tên đơn vị ban hành (`don_vi_id` → DON_VI)"*, luôn hiển thị `[STT12]` | Có đúng **1** nhãn; **27/27 bản ghi** có giá trị; **2 đơn vị khác nhau** (19 + 8) ⇒ bám `don_vi_id` của **bản ghi**; đối chứng phản hồi máy chủ **0/20 dòng lệch** | ✅ |
| `:654` #3 — bộ lọc *"Định dạng (doc / docx / xls / xlsx)"*, *"mỗi bộ lọc mặc định Tất cả (không lọc)"* | Mở ra đúng `Tất cả · DOC · DOCX · XLS · XLSX`, mặc định `Tất cả`, **không còn "PDF"** (đúng quyết định BA 24/07 mục `TKBMHD_03`); lọc `XLSX` ra **3/3**, máy chủ `total = 3` | ✅ |
| `:657` #6 — **Cột Loại tài liệu**, *"**Icon** doc/xls"* | Có, biểu tượng `file-excel` (xanh lá) ↔ `file-word` (xanh dương) — phân biệt được. Đặc tả chỉ định **biểu tượng**, app làm đúng biểu tượng | ✅ |
| `:650-673` — danh sách **đóng 22 thành phần**, **không** khai ô tích chọn (màn Thư mục `SCR-VII-01` mới có, `:624`, `:630`) | Đếm thô `input[type="checkbox"]` = **0**; thanh công cụ không có nhóm nút hàng loạt cấp biểu mẫu | ✅ |

**Điểm phụ *ô tích chọn* — không phải lỗi, đã đóng ở tầng BA:** chốt **2026-07-24 Loại 3 — không sửa**
(*"màn Danh sách biểu mẫu không được thiết kế ô tích chọn từng dòng; công khai/ẩn/xoá hàng loạt đặt ở cấp thư
mục theo đúng cách Cổng PLQG lấy dữ liệu — thiết kế có chủ đích"*). Câu trả lời cho đối tác **đã nằm sẵn**
trong ô *DEV phản hồi lần 1* của chính dòng 138 ⇒ đối tác đã được thông báo, không còn gì phải hỏi.

**Đối chiếu bản dựng đối tác chụp (`V1.0`, 13/07):** hàng tiêu đề khi đó chỉ 8 nhãn, **không có**
`Cơ quan ban hành` — đúng điều đối tác log, và cũng đúng điểm duy nhất phía TKM còn nêu ở lần retest **27/07**.
Nay cột đó đã có ⇒ **lỗi đối tác log đã hết**, đồng thời dev làm **đúng và đủ** phần đặc tả BA cập nhật.

### Bằng chứng

| Tệp | Thấy gì trong ảnh |
|---|---|
| [`image/QLBMHD_02-veA-cot-co-quan-ban-hanh-2-don-vi.png`](image/QLBMHD_02-veA-cot-co-quan-ban-hanh-2-don-vi.png) | Hàng tiêu đề có **`Cơ quan ban hành`**; các hàng hiện *Cục Bổ trợ tư pháp - Bộ …* và *Bộ Kế hoạch và Đầu tư*; cột `Loại TL` hiện biểu tượng Excel (xanh lá, hàng `BM-20260806-001`) lẫn Word (xanh dương) |
| [`image/QLBMHD_02-veB1-bo-loc-dinh-dang-4-gia-tri.png`](image/QLBMHD_02-veB1-bo-loc-dinh-dang-4-gia-tri.png) | Ô lọc thứ 4 đang mở, đọc được `Tất cả` · `DOC` · `DOCX` · `XLS` · `XLSX` |
| [`image/QLBMHD_02-veB1-loc-XLSX-3-ket-qua.png`](image/QLBMHD_02-veB1-loc-XLSX-3-ket-qua.png) | Sau khi lọc `XLSX`: *"Hiển thị 1-3 / 3 kết quả"*, cả 3 hàng biểu tượng Excel |
| [`image/QLBMHD_02-thanh-loc-4-o-khong-nhan.png`](image/QLBMHD_02-thanh-loc-4-o-khong-nhan.png) | Thanh lọc: 4 ô chọn **đều chỉ hiện `Tất cả`, không có nhãn chữ** phân biệt (ghi nhận ở mục 3.1 của phiếu BA) |
| [`tieuchi/QLBMHD_02.md`](tieuchi/QLBMHD_02.md) §7 | Vân tay bản dựng + tài khoản thực dùng + khai dữ liệu đã seed |
| [`partner-evidence/QLBMHD_02.jpg`](partner-evidence/QLBMHD_02.jpg) | Ảnh đối tác (1896×1031): env `htpldn-uat.ospgroup.vn`, bản `HTPLDN · V1.0`, hàng tiêu đề 8 nhãn, không có `Cơ quan ban hành` |

---

## Quan sát ghi nhận thêm — KHÔNG log thành bug, KHÔNG kéo verdict

**1) Nút thao tác dùng biểu tượng + nhãn chữ, không có `aria-label` / tooltip.** Đo được: nút `Xem` có biểu
tượng con mắt kèm chữ "Xem", `aria-label = null`, `title = null`. Phụ lục E §H6 (`srs-v3.5.md:6714`) yêu cầu
cột Hành động *"dùng icon … **thay cho nhãn text**"* và *"mỗi icon **BẮT BUỘC** có `aria-label` và tooltip
hover"*, nhưng cùng dòng đó lại nêu mục đích *"Đáp ứng WCAG 4.1.2 — **không icon-only**"*. Bản dựng đang làm
icon **kèm** chữ — thoả mục đích (tên khả truy cập lấy từ chính chữ trên nút) nhưng **trái chữ nghĩa**
("thay cho nhãn text"). Đây là **đặc tả tự mâu thuẫn** ⇒ theo flow 04 §Bug mới trực tiếp trong luồng bước 1,
**không được log bug**, chuyển thành **candidate cho BA**. Không thuộc vế đối tác nêu, không kéo verdict case.

**2) Cột `Module` của Nhật ký hệ thống gắn nhãn *"Tư vấn"* cho `HO_SO_PHAP_LY_DN`.** Bộ lọc `module` của
`SCR-VIII-10` được đặc tả có giá trị **`DN`** (`srs-fr-10-quan-tri.md:1387`), còn thao tác trên tab Hồ sơ pháp
lý của màn Chi tiết doanh nghiệp lại được xếp vào nhóm *Tư vấn* (do `FR-X.1-04` nằm ở module Tư vấn chuyên
sâu). Kiểm chuyện này phải mở thêm màn + đặt bộ lọc khác ⇒ theo flow 04 §Bug mới bước 5, chỉ ghi **1 dòng
candidate**, không mở phiếu, không kéo verdict.

**3) Lượt sửa *chỉ thêm tệp* không làm đổi `ngayCapNhat` / `version` của bản ghi hồ sơ.** Đo được ở lượt 3a:
`PATCH` thành công, tệp được gắn thật (bản ghi tệp có `ngayCapNhat` đúng giây bấm) và **nhật ký hệ thống vẫn
ghi dòng *Cập nhật*** — nhưng cột `updated_at` của chính bản ghi HSPL giữ nguyên. Đặc tả chỉ khai
`updated_at | Ngày cập nhật` (`srs-fr-12-tv-chuyen-sau.md:1414`) mà **im lặng** về ca "chỉ đổi tệp đính kèm"
(tệp là entity `FILE_DINH_KEM` riêng) ⇒ theo flow 04 §Bug mới bước 1, **không log bug**, chuyển **candidate
cho BA**. Vế (c) đã đóng bằng Đường A nên không ảnh hưởng verdict.

**4) Dòng *Cập nhật* trong nhật ký hiển thị `Dữ liệu cũ: —`** (chỉ có `Dữ liệu mới`). Outputs của
`SCR-VIII-10` đặc tả 6 trường `thoi_gian, nguoi_dung, module, hanh_dong, chi_tiet, ip_address`
(`srs-fr-10-quan-tri.md:1405`) — **không** đòi ảnh trước/sau ⇒ candidate cho BA, không phải sai lệch.

**5) Ghi nhận tích cực (không phải lỗi):** tải lên tệp có phần mở rộng `.png` nhưng **nội dung không phải
PNG** bị máy chủ từ chối kèm thông báo *"Nội dung file không khớp định dạng. Vui lòng tải lên file gốc đúng
loại đã chọn."* ⇒ kiểm tra định dạng theo nội dung thật, không chỉ theo phần mở rộng.

**6) Màn Danh sách biểu mẫu — 4 ô lọc không có nhãn chữ; chọn giá trị không tự lọc.** Đo được: cả 4 ô lọc
chỉ hiện `Tất cả`, phải mở từng ô mới biết ô nào là Thư mục / Lĩnh vực / Loại hình / Định dạng; và chọn
`XLSX` **không** đổi danh sách (giữ 27 kết quả, không phát lời gọi nào) cho tới khi bấm **Tìm kiếm**.
`srs-fr-09-bieu-mau.md:653`, `:654` ghi hành vi **`change → filter`** và bảng thành phần **không** khai nút
`Tìm kiếm` / `Xóa bộ lọc` mà bản dựng đang có; nhãn của từng ô lọc thì đặc tả **im lặng**. ⇒ theo flow 04
§Bug mới bước 1, **không log bug**, chuyển **candidate cho BA** — đã ghi ở
[`ba-confirm/cau-hoi-ba-tuan-5.md`](ba-confirm/cau-hoi-ba-tuan-5.md) mục 3.1 và 3.2. Không thuộc 3 vế đối
tác nêu, không kéo verdict.

**7) `ERR-BM-05` khi tạo biểu mẫu vào thư mục đơn vị khác — CÓ hiện thông báo, không nuốt lỗi.** Ô chọn
*Thư mục* của form *Thêm biểu mẫu* liệt kê cả thư mục thuộc đơn vị khác; chọn `QA-IMPORT-R7` rồi bấm
*Thêm mới* thì máy chủ trả **422 `ERR-BM-05`** *"Thư mục biểu mẫu không tồn tại hoặc không thuộc đơn vị"* —
chặn **đúng** `BR-AUTH-08`. Lần đọc đầu tiên (dò DOM sau khi bấm) **không thấy thông báo**, nhưng đo lại
đúng cách (cài bộ bắt thông báo **trước** khi bấm, tự kiểm `soObserverDangSong = 1`) thì ra
**`SO_REQUEST = 1` ↔ `SO_KHUNG = 1`**, chữ đúng câu lỗi trên ⇒ **không phải lỗi nuốt thông báo**; số đo đầu
là **phép đo nói dối** do dò DOM sau khi toast đã tắt. Việc ô chọn mời cả thư mục đơn vị khác đã được ghi
nhận từ 25/07 và tester khi đó quyết không mở phiếu ⇒ **không mở phiếu mới**, chỉ nhắc lại ở mục 3.3 của
phiếu BA.
