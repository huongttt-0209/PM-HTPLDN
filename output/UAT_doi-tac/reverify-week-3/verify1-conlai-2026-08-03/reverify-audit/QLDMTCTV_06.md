# QLDMTCTV_06 — Evidence audit (vòng 1, tuần 3)

**Mã TC:** QLDMTCTV_06 · **Dòng sheet:** 319 · **Tab:** `UAT_TGPL Doanh Nghiệp-tuần 3`
**Ngày verify:** 2026-08-03 · **Người verify:** QA Automation (Chrome DevTools MCP)
**Môi trường verify:** https://18.143.165.120.nip.io — bản dựng đọc ở chân menu: **`HTPLDN · V1.0.5`**
**Verdict chốt:** **`Pass`** (ghi cột Q — `Verify`). Cột P (`Trạng thái dev fix 1`) giữ nguyên `dev done`, KHÔNG đụng.

## Note dev trước khi QA đè

(cột R rỗng tại 2026-08-03 — dev không để lại note)

---

## 1. Bằng chứng đối tác đã xem

| Mục | Nội dung |
|---|---|
| File | `partner-evidence/QLDMTCTV_06.jpg` |
| Cách xem | Mở FULL-RES bằng tool Read, độ phân giải gốc 1904×1031 — đọc trực tiếp chữ trên ảnh, không dùng bản thu nhỏ |
| Loại | Ảnh tĩnh (không phải video) → toàn bộ khung hình chính là khoảnh khắc lỗi |

### Vai trò đọc được trong ảnh

Góc phải trên ảnh ghi rõ: **"Cán bộ NV Trung ương"** kèm mã vai trò **`CB_NV_TW`**, phạm vi **`BTP · TW`**.

> Đã **tự đọc lại từ ảnh của chính case 06**, không suy ra từ kết luận của case QLDMTCTV_05. Kết quả trùng với case 05, nhưng là hai lần đọc độc lập.

Đây đúng là vai trò được đặc tả cấp quyền tạo Tổ chức tư vấn (SRS dòng 1667: *"Quyền truy cập: Cán bộ Nghiệp vụ"*) ⇒ quan sát của đối tác là quan sát **hợp lệ**, không phải xem nhầm vai trò.

### 🔴 Tình trạng nhóm thu gọn trong ảnh đối tác — dữ kiện quyết định của case

Cảnh báo đặt ra trước khi verify: SRS mô tả biểu mẫu **6 nhóm**, nhóm 1 "Mặc định mở" ⇒ hàm ý nhóm khác có thể **mặc định thu gọn** ⇒ nếu đối tác chưa mở nhóm thì kết luận "thiếu trường" của họ sẽ sai. **Đã kiểm và loại trừ khả năng này:**

- Ảnh đối tác chụp từ **đầu biểu mẫu** (thấy breadcrumb "Trang chủ / Mạng lưới Tư vấn viên / Tổ chức tư vấn / **Thêm mới**" và ô đầu tiên "Tên tổ chức") **xuống tới ô cuối cùng "Ghi chú"** — tức gần trọn chiều dài biểu mẫu, không phải chỉ chụp phần trên.
- Trong ảnh **KHÔNG có bất kỳ tiêu đề nhóm nào**, cũng **KHÔNG có nhóm nào ở trạng thái thu gọn** (không thấy mũi tên/dấu cộng để bung nhóm). Biểu mẫu bản đó hiển thị **phẳng**.
- Thứ tự ô đọc được trong ảnh: Tên tổ chức → Loại hình → Người đại diện → Chức vụ đại diện → Số Giấy ĐKHĐ Sở TP → Ngày cấp → Số lao động → Địa chỉ → Điện thoại → Email → Website → Lĩnh vực pháp lý → **Ghi chú**.
- Giữa "Lĩnh vực pháp lý" và "Ghi chú" **không có** vùng "Công bố", **không có** vùng "Tệp đính kèm".

⇒ **Đối tác không bỏ sót do chưa cuộn hay chưa mở nhóm.** Tại bản dựng họ chụp, 3 trường đó thật sự vắng mặt. Phản ánh của đối tác **chính xác** đối với bản dựng đó ⇒ **KHÔNG được dùng `Reject`**.

### 3 dữ kiện neo (viết ra trước khi hình thành giả thuyết)

- (a) URL/bản ghi: `htpldn-uat.ospgroup.vn/chuyen-gia-tvv/to-chuc/tao-moi` — đúng màn Thêm mới; đồng hồ máy đối tác **2026-07-28 09:05**.
- (b) Trạng thái entity: chế độ **nhập liệu mới**, chưa có bản ghi, mọi ô trống ("nhập dữ liệu" / "Vui lòng chọn").
- (c) Dữ liệu tiền đề: vai trò **CB_NV_TW**, phạm vi **BTP · TW**. Case không đòi dữ liệu tiền đề.

---

## 2. Thứ tự thực hiện: ĐO WEB TRƯỚC — ĐỌC SRS SAU

Đã tuân thủ đúng thứ tự bắt buộc. Danh sách nhóm + trường dưới đây được **viết ra trước khi mở file SRS**, đo bằng `label innerText` (**không dùng `textContent`**) cộng ảnh chụp đã mở đọc.

### 2.1 Nhóm/section quan sát được (đo mù)

Rà toàn bộ cây DOM của biểu mẫu bằng bộ chọn rộng (`.ant-collapse`, `.ant-collapse-item`, `.ant-card-head-title`, `fieldset`, `legend`, `.ant-tabs-tab`, `h1`–`h6`, mọi lớp chứa `section` / `group` / `panel` / `accordion`):

- **0 nhóm thu gọn** — không có `.ant-collapse`, không accordion, không fieldset, không thẻ tab.
- **Chỉ 2 tiêu đề phân cách** (đường kẻ có chữ): **"Công bố"** và **"Tệp đính kèm"**.
- 4 nhóm còn lại theo đặc tả (Thông tin cơ bản, Lĩnh vực & Nhân sự, Liên hệ, Ghi chú) **không có tiêu đề nhóm** nào trên web.
- Toàn bộ 16 ô nhập đều `hidden = false` ⇒ **không ô nào bị ẩn**.
- Chiều cao biểu mẫu 1073px, trang cao 1265px so với khung nhìn 900px ⇒ **có cuộn**, và đã cuộn hết tới đáy (thấy 2 nút Hủy/Lưu) trước khi kết luận.

⇒ Vì **không có nhóm thu gọn nào**, cảnh báo "phải mở hết 6 nhóm rồi mới đo" **không áp dụng được** cho bản dựng hiện tại — không có gì để mở. Đo 2 lần (trước và sau khi thử mở nhóm) cho **kết quả y hệt**.

### 2.2 Danh sách nguyên văn 16 trường quan sát được (đo mù, trước khi mở SRS)

| # | Nhãn (nguyên văn) | Loại điều khiển | Bắt buộc |
|:-:|---|---|:-:|
| 1 | Tên tổ chức | ô nhập chữ | có `*` |
| 2 | Loại hình | dropdown | có `*` |
| 3 | Người đại diện | ô nhập chữ | có `*` |
| 4 | Chức vụ đại diện | ô nhập chữ | không |
| 5 | Số Giấy ĐKHĐ Sở TP | ô nhập chữ | có `*` |
| 6 | Ngày cấp | bộ chọn ngày | có `*` |
| 7 | Số lao động | ô số | không |
| 8 | Địa chỉ | ô nhập chữ | có `*` |
| 9 | Điện thoại | ô nhập chữ | không |
| 10 | Email | ô nhập chữ | không |
| 11 | Website | ô nhập chữ | không |
| 12 | Lĩnh vực pháp lý | dropdown chọn nhiều | có `*` |
| — | *(tiêu đề phân cách)* **Công bố** | — | — |
| 13 | **Số quyết định công bố** | ô nhập chữ | không |
| 14 | **Ngày quyết định công bố** | bộ chọn ngày | không |
| — | *(tiêu đề phân cách)* **Tệp đính kèm** | — | — |
| 15 | *(không có nhãn)* vùng kéo-thả tệp | tải tệp | không |
| 16 | Ghi chú | ô văn bản dài | không |

Nút cuối biểu mẫu: **Hủy** · **Lưu**.

### 2.3 Tìm riêng 3 trường tranh chấp bằng ≥2 cách độc lập

| Trường | Cách 1: theo chữ trên nhãn | Cách 2: theo loại điều khiển | Kết luận |
|---|---|---|:-:|
| Số quyết định công bố | ✅ có nhãn đúng chữ | ✅ ô nhập chữ, id `soQdCongBo` | **CÓ** |
| Ngày quyết định công bố | ✅ có nhãn đúng chữ | ✅ đếm `.ant-picker` = 2 (Ngày cấp + Ngày QĐ công bố) | **CÓ** |
| Tệp đính kèm | ✅ có tiêu đề mục đúng chữ | ✅ đếm `input[type=file]` = 1, `.ant-upload-drag` = 1 | **CÓ** |

Hai cách cho **cùng kết quả** ⇒ không có mâu thuẫn giữa 2 phép đo.

Chú thích trên vùng tải tệp (đọc nguyên văn): *"Tối đa 10 tệp. Định dạng: .pdf, .doc, .docx, .xls, .xlsx. Dung lượng tối đa: 20MB/tệp."*

---

## 3. Đối chiếu SRS (đọc SAU khi đã đo web)

**Nguồn:** `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-04-chuyen-gia-tvv.md` — bản chốt duy nhất. Đã **mở file đọc từng dòng**, không lấy số dòng từ trí nhớ. KHÔNG dùng `input/srs-update-2026-5-5/`.

| Dòng | Nội dung SRS | Web |
|---|---|:-:|
| 1662 | `SCR-IV-NEW-02: Thêm mới / Chỉnh sửa Tổ chức tư vấn` | ✅ |
| 1664 | "Loại màn hình: Biểu mẫu nhập liệu (**6 nhóm**)" | ⚠️ web để phẳng, chỉ 2 tiêu đề mục |
| 1666 | Đường dẫn `/chuyen-gia-tvv/to-chuc/tao-moi` | ✅ khớp |
| 1667 | "Quyền truy cập: **Cán bộ Nghiệp vụ**" | ✅ đã test đúng vai trò này |
| 1669 | Tên 6 nhóm: Thông tin cơ bản · Lĩnh vực & Nhân sự · Liên hệ · **Công bố** · **File đính kèm** · Ghi chú | ⚠️ chỉ 2/6 nhóm có tiêu đề |
| 1676–1682 | Nhóm 1: Tên tổ chức* · Loại hình* · Người đại diện* · Chức vụ · Số Giấy ĐKHĐ* · Ngày cấp* | ✅ đủ 6/6 |
| 1678 | Loại hình = 4 lựa chọn "Công ty Luật / Văn phòng Luật sư / Trung tâm Tư vấn Pháp luật / Khác" | ✅ đúng đủ 4 |
| 1683–1685 | Nhóm 2: Lĩnh vực pháp luật* · Số lao động | ✅ đủ 2/2 |
| 1686–1690 | Nhóm 3: Địa chỉ trụ sở* · Số điện thoại · Email · Website | ✅ đủ 4/4 |
| **1691** | Nhóm 4 "**Công bố**" | ✅ có tiêu đề mục |
| **1692** | **Số quyết định công bố** — ô văn bản, *Tùy chọn* | ✅ **CÓ**, không bắt buộc |
| **1693** | **Ngày quyết định công bố** — bộ chọn ngày, *Tùy chọn* | ✅ **CÓ**, không bắt buộc |
| **1694** | Nhóm 5 "**File đính kèm**" — tải nhiều file, PDF/DOC/DOCX/XLS/XLSX, tối đa 20MB/file, quét virus | ✅ **CÓ**, định dạng + 20MB khớp |
| 1695 | Nhóm 6: Ghi chú — ô văn bản dài | ✅ |
| 1696 | 2 nút **Hủy / Lưu** | ✅ đúng 2 nút, đúng tên |

### Nguồn thứ 2 độc lập trong SRS (mục Inputs của FR-IV-NEW-01)

Cả 3 trường tranh chấp được quy định ở **chỗ thứ hai, độc lập** với bảng màn hình:

| Dòng | Field | Bắt buộc | Ràng buộc |
|---|---|:-:|---|
| 1060 | `so_qd_cong_bo` | N | — |
| 1061 | `ngay_qd_cong_bo` | N | — |
| 1063 | `file_dinh_kem` | N | PDF/DOC/DOCX/XLS/XLSX, max 20MB/file |

⇒ Yêu cầu về 3 trường này là **rõ ràng, có ở 2 chỗ độc lập**, không phải suy diễn từ một dòng đơn lẻ.

### Điều kiện ẩn/hiện

Đã đọc kỹ cột **Hành vi** của các dòng 1691–1694 và phần mô tả nhóm (dòng 1669): **SRS KHÔNG đặt bất kỳ điều kiện ẩn/hiện nào** cho 3 trường này. ⇒ SRS đòi chúng **luôn hiện** trên biểu mẫu Thêm mới. Web đang đáp ứng.

### Mã UC

FR gốc `FR-IV-NEW-01: Quản lý Tổ chức tư vấn` ở **dòng 1027**; **dòng 1029** ghi nguyên văn `**UC Reference:** (chưa có trong CSV — gắn [GAP-IV-07])`.

⇒ **FR này KHÔNG có mã UC trong SRS.** Note gửi đối tác **không bịa mã UC**. (Verdict là `Pass` nên note cũng không dùng mã FR/số dòng — chỉ dùng tên chức năng.)

---

## 4. Verify trên web — bằng chứng real-data

### 4.1 Tài khoản & phiên

| Mục | Giá trị |
|---|---|
| Account thực dùng | **`cbnv_tw_04`** (mật khẩu `Test@1234`) — đăng nhập OK ngay lần đầu, **không phải fallback Rule 7** |
| Vai trò hiển thị trên web | "CB Nghiệp vụ - Trung ương #04" · `CB_NV_TW` · phạm vi `BTP · TW` |
| Khớp vai trò đối tác | ✅ trùng khớp tuyệt đối vai trò + cấp + đơn vị |
| Phiên | Cửa sổ trình duyệt cách ly riêng (`q06-cbnv`), kho cookie/bộ nhớ tách hẳn các phiên case khác |
| OTP | Lấy từ MailHog, đăng nhập bình thường |

### 4.2 Đường đi

Đăng nhập → **bấm menu bên trái** *Mạng lưới Tư vấn viên* → *Tổ chức tư vấn* → nút **Thêm mới** (đúng Rule 3: điều hướng bằng menu, không gõ thẳng địa chỉ sau khi đăng nhập). URL kết quả: `/chuyen-gia-tvv/to-chuc/tao-moi` — khớp SRS dòng 1666.

### 4.3 Bản ghi do QA tạo

| Mục | Giá trị |
|---|---|
| Mã tổ chức | **`TC-BTP-TW-0003`** |
| Tên | "Trung tam Tu van QA Kiem Truong Cong Bo 0803" |
| Trạng thái sau khi lưu | **Mới đăng ký** (đúng dòng 1696 + bước 5 Processing) |
| Đơn vị | Cục Bổ trợ tư pháp - Bộ Tư pháp |
| Số QĐ công bố đã nhập | `QD-CB-QA-0803/2026` |
| Ngày QĐ công bố đã chọn | `15/07/2026` |
| Tệp đã đính | `QA-QD-cong-bo-QLDMTCTV06.pdf` (613 B, PDF hợp lệ) |

> Bản ghi này **cố ý chưa trình phê duyệt**, giữ ở "Mới đăng ký". Thẻ "Mới đăng ký" tăng từ **1 → 2** sau khi lưu (bản ghi còn lại là `TC-BTP-TW-0002` của case trước).

### 4.4 3 trường có lưu được dữ liệu thật không (bước D)

| Kiểm tra | Kết quả |
|---|:-:|
| Nhập được vào cả 3 trường | ✅ |
| Bấm Lưu → tạo thành công | ✅ `TC-BTP-TW-0003` |
| Màn **Chi tiết** hiện "Số QĐ công bố" = `QD-CB-QA-0803/2026` | ✅ |
| Màn **Chi tiết** hiện "Ngày QĐ công bố" = `15/07/2026` | ✅ |
| Chế độ **Chỉnh sửa** còn đủ cả 3 (kể cả tệp, có nút "Xem"/"Xóa") | ✅ |
| Sau **tải lại trang bỏ qua bộ nhớ đệm** vẫn còn đủ 3 | ✅ ⇒ dữ liệu nằm ở máy chủ |

⇒ 3 trường **không chỉ hiển thị mà dùng được thật**.

### 4.5 Đo thông báo + số request (theo `tools/toast-capture.js`)

- Cài observer **TRƯỚC** khi bấm Lưu; **không lọc trùng**; đọc bằng `innerText`.
- Tự kiểm trước khi tin số liệu: **`soObserverDangSong = 1`** ⇒ số liệu hợp lệ.
- Kết quả: **SO_REQUEST = 1** (`POST /api/v1/to-chuc-tu-vans`) · **SO_KHUNG_THONG_BAO = 1** ("Tạo Tổ chức tư vấn thành công") · `BI_LAP = false`.
- ⇒ **Không có thông báo lặp, không tạo trùng bản ghi.**

### 4.6 Bảng điều khiển & mạng

- Lỗi/cảnh báo trong bảng điều khiển trình duyệt: **không có**.
- Các lệnh gọi máy chủ: toàn bộ **200/304**, không có 4xx/5xx.
- Bản dựng xác nhận sau khi tải lại trang: **`HTPLDN · V1.0.5`**.

### 4.7 Ảnh chụp (đều đã MỞ RA ĐỌC, không chỉ lưu)

| # | File trong `image/` | Chứng minh gì |
|:-:|---|---|
| 1 | `QLDMTCTV_06-form-them-moi-luc-moi-mo-mac-dinh.png` | Biểu mẫu **lúc vừa mở, chưa thao tác** — đã thấy mục "Công bố" + 2 ô Số QĐ / Ngày QĐ và đầu mục "Tệp đính kèm" |
| 2 | `QLDMTCTV_06-form-them-moi-toan-bo-full-page.png` | Toàn bộ biểu mẫu rỗng từ đầu đến 2 nút Hủy/Lưu — không nhóm nào thu gọn |
| 3 | `QLDMTCTV_06-can-canh-vung-cong-bo-va-tep-dinh-kem.png` | Cận cảnh 2 mục tranh chấp + vùng kéo-thả kèm chú thích định dạng/20MB |
| 4 | `QLDMTCTV_06-da-nhap-3-truong-tranh-chap-truoc-khi-luu.png` | Đã nhập Số QĐ, chọn Ngày QĐ, đính tệp PDF — trước khi bấm Lưu |
| 5 | `QLDMTCTV_06-sau-khi-luu-danh-sach-moi-dang-ky-tang-len-2.png` | Sau khi lưu: về danh sách, thẻ "Mới đăng ký" tăng lên **2** |
| 6 | `QLDMTCTV_06-chi-tiet-ban-ghi-luu-du-so-qd-va-ngay-qd.png` | Màn Chi tiết `TC-BTP-TW-0003` hiện đủ Số QĐ + Ngày QĐ đã lưu |
| 7 | `QLDMTCTV_06-mo-lai-che-do-sua-3-truong-van-con-du-lieu.png` | Mở lại chế độ Chỉnh sửa: cả 3 trường còn nguyên, tệp còn kèm nút Xem/Xóa |

---

## 5. Lập luận chốt verdict

1. Đối tác phản ánh **thiếu 3 trường** trên biểu mẫu Thêm mới. Đã xác minh **phản ánh này là đúng với bản dựng họ chụp** — ảnh cho thấy biểu mẫu phẳng, không nhóm thu gọn, và thật sự không có 3 trường đó.
2. Trên bản dựng hiện tại **`HTPLDN · V1.0.5`**, đo ở **đúng vai trò và đúng đơn vị của đối tác**, cả 3 trường **đã có mặt**, **hiện sẵn ngay khi mở biểu mẫu** (không cần mở nhóm nào), và **khớp đặc tả** cả về loại điều khiển lẫn ràng buộc (tùy chọn / định dạng / 20MB mỗi tệp).
3. Cả 3 **dùng được thật**: nhập → lưu → mở lại vẫn đủ dữ liệu, kể cả sau khi tải lại trang bỏ qua bộ nhớ đệm.
4. Rà **toàn bộ** bảng Thành phần màn hình (dòng 1673–1696), **không thiếu trường nào khác**; 2 nút Hủy/Lưu đúng đặc tả.
5. ⇒ Lỗi dev khai đã sửa (`dev done`) là **có thật đã được sửa** và QA **kiểm chứng được bằng dữ liệu thật** ⇒ **`Pass`**.
6. **Vì sao KHÔNG dùng `Reject`:** `Reject` chỉ dùng khi chứng minh được đối tác **thao tác/hiểu sai**. Ở đây điều ngược lại — đối tác quan sát **đúng**, chỉ là trên bản dựng cũ hơn. **Vì sao KHÔNG dùng `Resolved`:** `Resolved` dành cho bug **không tái hiện** mà nguyên nhân chưa rõ; ở đây dev đã khai fix và QA **xác nhận được đúng phần fix đó** (3 trường mới xuất hiện, đúng chỗ, đúng ràng buộc) ⇒ đúng định nghĩa `Pass`.

---

## 6. Ngoài phạm vi case — quan sát thêm (chưa log, chờ user quyết)

1. **Biểu mẫu không chia 6 nhóm thu gọn như đặc tả** (SRS dòng 1664/1669/1676/1683/1686/1691 ghi "nhóm thu gọn"). Web để phẳng, chỉ có 2 tiêu đề mục "Công bố" + "Tệp đính kèm". **Không cản trở nhập liệu**, nhưng lệch mô tả màn hình.
2. **Thứ tự trường khác SRS:** SRS gom "Lĩnh vực pháp luật + Số lao động" thành nhóm 2 rồi mới tới nhóm Liên hệ; web đặt "Số lao động" cạnh "Địa chỉ" và đẩy "Lĩnh vực pháp lý" xuống sau "Website".
3. **Nhãn rút gọn so với SRS:** "Số Giấy đăng ký hành nghề" → "Số Giấy ĐKHĐ Sở TP"; "Ngày cấp Giấy đăng ký hành nghề" → "Ngày cấp"; "Địa chỉ trụ sở" → "Địa chỉ"; "Lĩnh vực pháp luật" → "Lĩnh vực pháp lý". Nghĩa không đổi.
4. **Mâu thuẫn nội tại của SRS (để BA chốt):** bảng màn hình dòng **1681–1682** đánh dấu "Số Giấy ĐKHĐ" + "Ngày cấp" là **bắt buộc (\*)**, nhưng bảng Inputs dòng **1052–1053** ghi Bắt buộc = **N**. Web làm theo bảng màn hình (bắt buộc), cũng khớp bước 3 phần Processing (dòng 1073).
5. **Màn Chi tiết chưa thấy vùng tệp đính kèm:** bản ghi có tệp nhưng màn Chi tiết chỉ liệt kê thông tin chữ, phải vào Chỉnh sửa mới thấy tệp. Là **màn khác** (SCR-IV-NEW-03) và có thể phụ thuộc trạng thái "Mới đăng ký" ⇒ **chưa kết luận**, chỉ ghi nhận.
6. **Quét virus (SRS dòng 1694)** chưa kiểm trong case này — theo ghi nhận trước đó tính năng quét mã độc chưa bật trên môi trường UAT. Ngoài phạm vi case.

---

## 7. Ghi chú đo lường — chống lặp lại lỗi 16/07

- Bộ bắt thông báo: **chỉ** dùng `tools/toast-capture.js`. Không lọc trùng, đọc bằng `innerText`, tự kiểm `soObserverDangSong = 1` trước khi tin số liệu. Luôn đếm request song song với số thông báo.
- **Chụp ảnh ở mọi thao tác đổi trạng thái, kể cả bước tạo dữ liệu — và đã MỞ RA ĐỌC từng ảnh.**
- **Đổi tên 1 ảnh cho khớp điểm ảnh:** ảnh sau khi lưu ban đầu đặt tên có chữ "thong-bao" nhưng thông báo đã tự tắt trước khi chụp nên điểm ảnh không có thông báo → đổi thành `...-sau-khi-luu-danh-sach-moi-dang-ky-tang-len-2.png` (tên ↔ nội dung ↔ claim phải khớp).
- **Hai lần selector của QA sai — KHÔNG phải lỗi ứng dụng**, đã kiểm lại bằng mã HTML thô nên không log oan:
  1. Đếm tệp đã đính bằng `.ant-upload-list-item` ra **0** trong khi tệp vẫn đính đúng — ứng dụng dựng danh sách tệp bằng cấu trúc riêng. Đọc thô chữ hiển thị của vùng tải tệp mới thấy đúng tên tệp + dung lượng.
  2. Dò chú thích trợ giúp bằng `.anticon-question-circle` trên **toàn trang** thì trúng biểu tượng ở menu bên trái thay vì biểu tượng trong biểu mẫu. Đã thu hẹp phạm vi về trong thẻ `form`.
- 🔴 **Một mâu thuẫn giữa 2 phép đo đã được truy tới cùng trước khi kết luận (đúng quy tắc "bug candidate ≠ bug"):**
  - Hiện tượng: script báo biểu mẫu **đã điền đủ**, nhưng ảnh chụp chế độ **"toàn trang"** ngay sau đó lại ra **biểu mẫu trắng trơn**. Lần khác, ảnh toàn trang **thiếu dòng tệp vừa đính** trong khi cây DOM đo ngay sau đó vẫn có đủ.
  - **Không kết luận vội theo bên nào.** Phép thử phân biệt: **thu phóng khung nhìn thật (1440 → 1100 px) KHÔNG làm mất dữ liệu đang nhập** (kiểm trực tiếp: giá trị vẫn nguyên sau khi đổi kích thước).
  - ⇒ Kết luận: đây là **hiện tượng dựng hình của công cụ chụp ảnh toàn trang**, **không phải hành vi của ứng dụng** ⇒ **KHÔNG log thành bug**. Từ đó chuyển hẳn sang chụp theo khung nhìn + cuộn để lấy bằng chứng, và mọi ảnh dùng làm bằng chứng đều đã đối chiếu lại với phép đo DOM.
