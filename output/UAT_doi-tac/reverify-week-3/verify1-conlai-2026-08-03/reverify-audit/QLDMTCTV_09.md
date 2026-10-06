# QLDMTCTV_09 — Evidence audit (vòng 1, tuần 3)

**Mã TC:** QLDMTCTV_09 · **Dòng sheet:** 320 · **Tab:** `UAT_TGPL Doanh Nghiệp-tuần 3`
**Ngày verify:** 2026-08-03 · **Người verify:** QA Automation (Chrome DevTools MCP)
**Môi trường verify:** https://18.143.165.120.nip.io — bản dựng đọc ở chân menu: **`HTPLDN · V1.0.5`**
**Verdict chốt:** **`Pass`** (ghi cột Q — `Verify`). Cột P (`Trạng thái dev fix 1`) giữ nguyên `dev done`, KHÔNG đụng.

## Note dev trước khi QA đè

(cột R rỗng tại 2026-08-03 — dev không để lại note)

---

## 1. Bằng chứng đối tác đã xem

| Mục | Nội dung |
|---|---|
| File | `partner-evidence/QLDMTCTV_09.jpg` |
| Cách xem | Mở FULL-RES bằng tool Read, đọc trực tiếp chữ trên ảnh — không dùng bản thu nhỏ |
| Loại | Ảnh tĩnh (không phải video) → toàn bộ khung hình chính là khoảnh khắc lỗi |

### (a) Vai trò đọc được trong ảnh

Góc phải trên ảnh ghi rõ: **"Cán bộ NV Trung ương"** kèm mã vai trò **`CB_NV_TW`**, phạm vi **`BTP · TW`**.

Đây đúng là vai trò được đặc tả cấp quyền sửa Tổ chức tư vấn (SRS dòng 1667: *"Quyền truy cập: Cán bộ Nghiệp vụ (tạo/sửa Tổ chức tư vấn thuộc đơn vị mình)"*) ⇒ quan sát của đối tác là quan sát **hợp lệ**.

### (b) Bản ghi nào + trạng thái nào đối tác đang sửa

- **URL:** `htpldn-uat.ospgroup.vn/chuyen-gia-tvv/to-chuc/d6434545-b76b-47ae-8be7-8bceea2d01a7/chinh-sua` — đúng chế độ **Chỉnh sửa**, đúng dạng đường dẫn đặc tả ở dòng 1666.
- **Breadcrumb:** "Trang chủ / Mạng lưới Tư vấn viên / Tổ chức tư vấn / **Chi tiết** / **Chỉnh sửa**".
  - 🔴 **Breadcrumb KHÔNG kèm tên tổ chức** (SRS dòng 1675 đòi nhánh "Chỉnh sửa [Tên TC]"). Ghi nhận, không dùng để chấm case này.
- **Mã tổ chức:** không đọc được — **màn Sửa không hiển thị mã tổ chức**.
- **Badge trạng thái:** không đọc được — **màn Sửa không hiển thị badge trạng thái**. ⇒ Vì không chốt được trạng thái bản ghi của đối tác, QA **phải phủ nhiều trạng thái** để loại trừ khả năng biểu mẫu đổi theo state (đã làm, xem §4).
- **Dữ liệu bản ghi đọc được trên ảnh:** Tên tổ chức "Test thêm mới tổ chức địa phương" · Loại hình "Khác" · Người đại diện "TKM" · Chức vụ đại diện trống · Số Giấy ĐKHĐ Sở TP "3344" · Ngày cấp 08/07/2026 · Số lao động trống · Địa chỉ "Hà Nội" · Điện thoại/Email/Website trống · Lĩnh vực pháp lý 8 thẻ (Thuế, Lao động, Đất đai, Dân sự, Thương mại, Hình sự, Hành chính, Sở hữu trí tuệ) · Ghi chú trống.
- **Đồng hồ máy đối tác:** 2026-07-28 09:11.
- 🔴 **Suy ra tình trạng 3 trường của bản ghi đối tác:** tên bản ghi ("Test thêm mới tổ chức địa phương") cho thấy đây là bản ghi họ vừa tạo từ màn Thêm mới; ảnh case QLDMTCTV_06 chụp màn Thêm mới lúc **09:05**, ảnh case này lúc **09:11** — cách nhau 6 phút. Vì màn Thêm mới của bản dựng đó **cũng thiếu đúng 3 trường này**, bản ghi được tạo ra **chắc chắn không có dữ liệu ở cả 3 trường**. ⇒ Điều kiện phải tái hiện là **bản ghi RỖNG 3 trường**.

### (c) Form có nhóm thu gọn nào không / ảnh cắt tới đâu

- Biểu mẫu trong ảnh hiển thị **phẳng**: **KHÔNG có tiêu đề nhóm nào**, **KHÔNG có nhóm nào đang thu gọn** (không thấy mũi tên/dấu cộng để bung nhóm).
- **Ảnh cắt tới đâu:** phía trên thấy trọn breadcrumb và ô đầu tiên "Tên tổ chức" (nhãn bị xén nhẹ ~15px do đã cuộn một chút); phía dưới thấy trọn ô cuối "Ghi chú" và **mép trên của 2 nút cuối biểu mẫu** ⇒ đã bao **trọn chiều dài biểu mẫu**, không cắt mất phần nào ở giữa.
- **Thứ tự ô đọc được:** Tên tổ chức → Loại hình → Người đại diện → Chức vụ đại diện → Số Giấy ĐKHĐ Sở TP → Ngày cấp → Số lao động → Địa chỉ → Điện thoại → Email → Website → Lĩnh vực pháp lý → **Ghi chú**.
- 🔴 Giữa "Lĩnh vực pháp lý" và "Ghi chú" **không có** mục "Công bố", **không có** mục "Tệp đính kèm".

⇒ **Đối tác không bỏ sót do chưa cuộn hay chưa mở nhóm.** Tại bản dựng họ chụp, 3 trường đó thật sự vắng mặt **ở cả chế độ Sửa**. Phản ánh của đối tác **chính xác** với bản dựng đó ⇒ **KHÔNG được dùng `Reject`**.

---

## 2. Thứ tự thực hiện: ĐO WEB TRƯỚC — ĐỌC SRS SAU

Đã tuân thủ đúng thứ tự bắt buộc. Toàn bộ danh sách nhóm + trường ở §4 được **đo và viết ra trước khi mở file SRS**, bằng `label innerText` (**không dùng `textContent`**) cộng ảnh chụp đã mở đọc.

---

## 3. Đối chiếu SRS (đọc SAU khi đã đo web)

**Nguồn:** `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-04-chuyen-gia-tvv.md` — bản chốt duy nhất. Đã **mở file đọc từng dòng**, không lấy số dòng từ trí nhớ. KHÔNG dùng `input/srs-update-2026-5-5/`.

### 3.1 🔴 SRS dùng CHUNG 1 màn cho Thêm mới VÀ Sửa (điểm quyết định của case)

| Dòng | Nội dung SRS (đã tự mở file xác minh) | Ý nghĩa |
|---|---|---|
| 1662 | `SCR-IV-NEW-02: **Thêm mới / Chỉnh sửa** Tổ chức tư vấn` | 1 màn cho 2 chế độ |
| 1666 | `/chuyen-gia-tvv/to-chuc/tao-moi` **hoặc** `/chuyen-gia-tvv/to-chuc/:id/chinh-sua` | 2 đường dẫn cùng trỏ 1 SCR |
| 1675 | breadcrumb nhánh "Thêm mới" **hoặc** nhánh "Chỉnh sửa [Tên TC]" | xác nhận màn phục vụ cả chế độ Sửa |
| 1696 | nút Lưu: "tạo mới **hoặc cập nhật**" | 1 nút xử lý cả 2 chế độ |
| 1334 | cây menu: `SCR-IV-NEW-02: **Thêm/Sửa** Tổ chức tư vấn` | cùng mã màn cho cả 2 chế độ |
| 1065–1100 | Processing chỉ có khối "Thêm mới" / "Xóa (xóa mềm)" / "Công khai" / "Xuất DS" — **không có khối riêng cho Sửa**; Postconditions dòng 1114 gộp "tạo/cập nhật/xóa mềm" | không có xử lý riêng cho Sửa |

⇒ **SRS KHÔNG có danh sách trường riêng cho màn Sửa, KHÔNG quy định trường chỉ-đọc nào.** Yêu cầu về trường ở chế độ Sửa **bằng đúng** chế độ Thêm mới.
⚠️ Lưu ý phương pháp: điều này **chỉ dùng để xác định TIÊU CHÍ chấm**, **KHÔNG** dùng thay cho phép đo. Việc "3 trường có mặt ở chế độ Sửa hay không" đã được **test thật** trên 4 bản ghi (§4), tuyệt đối không suy luận kiểu "màn dùng chung nên chắc giống nhau".

### 3.2 Quyền + điều kiện trạng thái

| Dòng | Nội dung SRS | Web |
|---|---|:-:|
| 1667 | "Quyền truy cập: **Cán bộ Nghiệp vụ** (tạo/sửa TCTV thuộc đơn vị mình). **Chỉ cho phép sửa khi trạng thái khác 'Vô hiệu hóa'**" | ✅ đã test đúng vai trò; 3 trạng thái đã phủ đều khác "Vô hiệu hóa" |
| 1646 | nút Sửa (bút chì) → SCR-IV-NEW-02, "**ẩn nếu trạng thái Vô hiệu hóa**" | ⏭ không kiểm được — 0 bản ghi ở trạng thái Vô hiệu hóa (xem §6) |

### 3.3 Bảng Thành phần màn hình — đối chiếu ĐỦ/THIẾU TỪNG trường (dòng 1673–1696)

| Dòng | Trường theo SRS | Web (chế độ Sửa) |
|---|---|:-:|
| 1664 | "Biểu mẫu nhập liệu (**6 nhóm**)" | ⚠️ web để phẳng, chỉ 2 tiêu đề mục |
| 1669 | 6 nhóm: Thông tin cơ bản · Lĩnh vực & Nhân sự · Liên hệ · **Công bố** · **File đính kèm** · Ghi chú | ⚠️ chỉ 2/6 nhóm có tiêu đề |
| 1677–1682 | Tên tổ chức* · Loại hình* · Người đại diện* · Chức vụ đại diện · Số Giấy ĐKHĐ* · Ngày cấp* | ✅ đủ 6/6 |
| 1684–1685 | Lĩnh vực pháp luật* · Số lao động | ✅ đủ 2/2 |
| 1687–1690 | Địa chỉ trụ sở* · Số điện thoại · Email · Website | ✅ đủ 4/4 |
| **1691** | Nhóm 4 "**Công bố**" | ✅ có tiêu đề mục |
| **1692** | **Số quyết định công bố** — ô văn bản, *Tùy chọn* | ✅ **CÓ**, không bắt buộc |
| **1693** | **Ngày quyết định công bố** — bộ chọn ngày, *Tùy chọn* | ✅ **CÓ**, không bắt buộc |
| **1694** | Nhóm 5 "**File đính kèm**" — tải nhiều file, PDF/DOC/DOCX/XLS/XLSX, ≤20MB/file, quét virus | ✅ **CÓ**, định dạng + 20MB khớp |
| 1695 | Nhóm 6: Ghi chú — ô văn bản dài | ✅ |
| 1696 | 2 nút **Hủy / Lưu** | ✅ đúng 2 nút, đúng tên |

⇒ **Không thiếu trường nào** ở chế độ Sửa. 16 ô nhập trên web khớp đủ danh sách SRS (15 trường + 1 vùng tải tệp).

### 3.4 Nguồn thứ 2 độc lập trong SRS (mục Inputs của FR-IV-NEW-01)

| Dòng | Field | Bắt buộc | Ràng buộc |
|---|---|:-:|---|
| 1060 | `so_qd_cong_bo` | N | — |
| 1061 | `ngay_qd_cong_bo` | N | — |
| 1063 | `file_dinh_kem` | N | PDF/DOC/DOCX/XLS/XLSX, max 20MB/file |

⇒ Yêu cầu về 3 trường này **có ở 2 chỗ độc lập**, không phải suy diễn từ một dòng đơn lẻ.

### 3.5 Điều kiện ẩn/hiện

Đã đọc kỹ cột **Hành vi** các dòng 1691–1694 và mô tả nhóm dòng 1669: **SRS KHÔNG đặt bất kỳ điều kiện ẩn/hiện nào** cho 3 trường này — không theo trạng thái, không theo việc bản ghi đã có dữ liệu hay chưa. ⇒ SRS đòi chúng **luôn hiện**. Web đang đáp ứng.

### 3.6 Mã UC

FR gốc `FR-IV-NEW-01: Quản lý Tổ chức tư vấn` ở **dòng 1027**; **dòng 1029** ghi nguyên văn `**UC Reference:** (chưa có trong CSV — gắn [GAP-IV-07])`.

⇒ **FR này KHÔNG có mã UC trong SRS.** Note gửi đối tác **không bịa mã UC**. (Verdict `Pass` nên note cũng không dùng mã FR/số dòng — chỉ dùng tên chức năng, đúng quy tắc tham chiếu theo verdict.)

---

## 4. Verify trên web — bằng chứng real-data

### 4.1 Tài khoản & phiên

| Mục | Giá trị |
|---|---|
| Account thực dùng | **`cbnv_tw_04`** (mật khẩu `Test@1234`) — đăng nhập OK ngay lần đầu, **không phải fallback Rule 7** |
| Vai trò hiển thị trên web | "CB Nghiệp vụ - Trung ương #04" · `CB_NV_TW` · phạm vi `BTP · TW` |
| Khớp vai trò đối tác | ✅ trùng khớp tuyệt đối vai trò + cấp + đơn vị |
| Phiên | Cửa sổ trình duyệt cách ly riêng (`q09-cbnv`), kho cookie/bộ nhớ tách hẳn các phiên case khác |
| OTP | Lấy từ MailHog, đăng nhập bình thường |

### 4.2 Đường đi

Đăng nhập → **bấm menu bên trái** *Mạng lưới Tư vấn viên* → *Tổ chức tư vấn* → bấm biểu tượng **Sửa (bút chì)** trên từng dòng (đúng Rule 3: điều hướng bằng menu/thao tác trong ứng dụng). URL kết quả có dạng `/chuyen-gia-tvv/to-chuc/{id}/chinh-sua` — khớp SRS dòng 1666.

> Riêng bản ghi ở trạng thái **Chờ phê duyệt** phải mở bằng đường dẫn trực tiếp vì danh sách **không có tab "Chờ phê duyệt"** cho vai trò này (đã đối chiếu SRS — đúng đặc tả, xem §6). Phiên **không bị đăng xuất** khi mở thẳng đường dẫn (xác thực nằm ở cookie), vẫn đúng vai trò `cbnv_tw_04`.

### 4.3 🔴 BẢNG SO 4 LẦN ĐO TRÊN 4 BẢN GHI KHÁC NHAU (phép thử quyết định của case)

| # | Bản ghi | Trạng thái | Nguồn gốc | Có sẵn dữ liệu 3 trường? | Số QĐ công bố | Ngày QĐ công bố | Tệp đính kèm | Tổng số trường | Nhóm thu gọn |
|:-:|---|---|---|:-:|:-:|:-:|:-:|:-:|:-:|
| 1 | `TCTV-SEED-0001` | Đang hoạt động | **Seed cũ nhất, KHÔNG do QA tạo** | **KHÔNG** (cả 3 rỗng) | ✅ **CÓ** (rỗng) | ✅ **CÓ** (rỗng) | ✅ **CÓ** (vùng kéo-thả trống) | 16 | 0 |
| 2 | `TC-BTP-TW-0002` | Mới đăng ký | QA tạo | **KHÔNG** (cả 3 rỗng) | ✅ **CÓ** (rỗng) | ✅ **CÓ** (rỗng) | ✅ **CÓ** (vùng kéo-thả trống) | 16 | 0 |
| 3 | `TC-BTP-TW-0001` | Chờ phê duyệt | QA tạo | **KHÔNG** (cả 3 rỗng) | ✅ **CÓ** (rỗng) | ✅ **CÓ** (rỗng) | ✅ **CÓ** (vùng kéo-thả trống) | 16 | 0 |
| 4 | `TC-BTP-TW-0003` | Mới đăng ký | QA tạo | **CÓ** đủ 3 | ✅ **CÓ** = `QD-CB-QA-0803/2026` | ✅ **CÓ** = `15/07/2026` | ✅ **CÓ** = `QA-QD-cong-bo-QLDMTCTV06.pdf` (613 B) + nút Xem/Xóa | 16 | 0 |

**Đọc kết quả:**
- Nếu ứng dụng chỉ vẽ 3 trường khi bản ghi đã có dữ liệu thì các dòng 1–3 phải THIẾU. Thực tế **cả 3 đều ĐỦ** ⇒ **giả thuyết bị BÁC BỎ**.
- Dòng 1 là **dữ liệu cũ nhất, không do QA tạo** ⇒ thoả yêu cầu "bug về trường lưu trong CSDL phải thử trên dữ liệu cũ VÀ mới".
- 3 trạng thái khác nhau cho **kết quả giống hệt** ⇒ biểu mẫu Sửa **không đổi theo trạng thái**.
- Cả 4 lần đo đều: **16 trường**, **0 nhóm thu gọn**, đúng **2 tiêu đề mục** "Công bố" + "Tệp đính kèm".

### 4.4 Tìm 3 trường bằng ≥2 cách độc lập (mọi lần đo đều trùng kết quả)

| Trường | Cách 1: theo chữ trên nhãn | Cách 2: theo loại điều khiển | Kết luận |
|---|---|---|:-:|
| Số quyết định công bố | ✅ có nhãn đúng chữ (`label[for="soQdCongBo"]`) | ✅ ô nhập chữ trong mục "Công bố" | **CÓ** |
| Ngày quyết định công bố | ✅ có nhãn đúng chữ (`label[for="ngayQdCongBo"]`) | ✅ đếm bộ chọn ngày = 2 (Ngày cấp + Ngày QĐ công bố) | **CÓ** |
| Tệp đính kèm | ✅ có tiêu đề mục đúng chữ | ✅ đếm `input[type=file]` = 1, vùng kéo-thả = 1 | **CÓ** |

Chú thích trên vùng tải tệp (đọc nguyên văn): *"Tối đa 10 tệp. Định dạng: .pdf, .doc, .docx, .xls, .xlsx. Dung lượng tối đa: 20MB/tệp."*

### 4.5 "Điền sẵn thông tin hiện có" — đối chiếu từng trường (một phần của case, không bỏ)

Đối chiếu giá trị trên biểu mẫu Sửa với dữ liệu thật của bản ghi, trên **cả 4 bản ghi**:

- **Mọi trường có dữ liệu đều được điền sẵn ĐÚNG.** Ví dụ `TC-BTP-TW-0002`: Tên tổ chức, Loại hình "Trung tâm Tư vấn Pháp luật", Người đại diện "Le Thi Kiem Tra", Số Giấy ĐKHĐ "QA-DKHD-0803-05", Ngày cấp "01/06/2026", Địa chỉ "So 1 Pho Kiem Thu, Ha Noi", Lĩnh vực "Thương mại" — khớp 1:1.
- **Mọi ô để trống đều tương ứng trường thật sự chưa có dữ liệu** ở bản ghi đó (không có trường hợp có dữ liệu mà biểu mẫu bỏ trống).
- **Định dạng đúng:** ngày hiện dạng ngày/tháng/năm; dropdown 1 lựa chọn hiện đúng nhãn tiếng Việt; dropdown nhiều lựa chọn hiện đúng các thẻ lĩnh vực; tệp đính kèm hiện **đúng tên tệp + dung lượng** kèm nút "Xem"/"Xóa".
- **Không tràn/đè, đồng nhất ngôn ngữ:** bố cục 2–3 cột đều, không chữ chồng chữ, **toàn bộ chữ hiển thị là tiếng Việt** — kiểm bằng ảnh chụp đã mở đọc.

⇒ Phần "điền sẵn thông tin hiện có" trong Kết quả mong đợi của đối tác **ĐẠT**.

### 4.6 Bước D — 3 trường có dùng được thật không (nhập mới trên bản ghi vốn đang trống)

Chọn `TC-BTP-TW-0002` (Mới đăng ký) vì đây đúng loại "bản ghi chưa từng có dữ liệu ở 3 trường".

| Kiểm tra | Kết quả |
|---|:-:|
| Nhập được Số QĐ công bố = `QD-CB-QA-0903/2026` | ✅ |
| Chọn được Ngày QĐ công bố = `20/07/2026` | ✅ |
| Đính được tệp PDF hợp lệ `QA-QD-cong-bo-QLDMTCTV09.pdf` (398 B) | ✅ hiện tên + dung lượng + nút Xem/Xóa |
| Bấm **Lưu** → lưu thành công | ✅ chuyển về màn Chi tiết |
| Màn **Chi tiết** hiện "Số QĐ công bố" = `QD-CB-QA-0903/2026` | ✅ |
| Màn **Chi tiết** hiện "Ngày QĐ công bố" = `20/07/2026` | ✅ |
| Trạng thái bản ghi sau khi lưu | ✅ giữ nguyên "Mới đăng ký" |
| **Tải lại trang bỏ qua bộ nhớ đệm** rồi mở lại chế độ Sửa → còn đủ 3 | ✅ kể cả tệp (tên + dung lượng + Xem/Xóa) |
| Tệp được quét ở trạng thái sạch | ✅ |

⇒ 3 trường **không chỉ hiển thị mà dùng được thật**, và dữ liệu nằm ở **máy chủ** chứ không phải chỉ trên màn hình.

### 4.7 Đo thông báo + số request (theo `tools/toast-capture.js`)

- Cài observer **TRƯỚC** khi bấm Lưu; **không lọc trùng**; đọc bằng `innerText`.
- Tự kiểm trước khi tin số liệu: **`soObserverDangSong = 1`** ⇒ số liệu hợp lệ.
- Kết quả: **SO_REQUEST = 1** (1 lệnh cập nhật bản ghi) · **SO_KHUNG_THONG_BAO = 1** ("Cập nhật thành công") · `BI_LAP = false`.
- ⇒ **Không có thông báo lặp, không ghi trùng bản ghi.**

### 4.8 Bảng điều khiển & mạng

- Lỗi/cảnh báo trong bảng điều khiển trình duyệt: **không có**.
- Các lệnh gọi máy chủ: toàn bộ **200/304**, không có 4xx/5xx.
- Bản dựng xác nhận sau khi tải lại trang: **`HTPLDN · V1.0.5`**.

### 4.9 Ảnh chụp (đều đã MỞ RA ĐỌC, không chỉ lưu)

| # | File trong `image/` | Chứng minh gì |
|:-:|---|---|
| 1 | `QLDMTCTV_09-danh-sach-tab-dang-hoat-dong-3-ban-ghi.png` | Danh sách Tổ chức tư vấn, các tab + số đếm, cột Hành động có icon Sửa |
| 2 | `QLDMTCTV_09-01-TCTV-SEED-0001-form-sua-tu-dau-den-muc-cong-bo.png` | **Ảnh mạnh nhất**: biểu mẫu Sửa của bản ghi cũ/rỗng 3 trường, thấy trong **một khung nhìn** từ "Tên tổ chức" xuống "Lĩnh vực pháp lý" → mục **"Công bố"** (2 ô) → đầu mục **"Tệp đính kèm"** |
| 3 | `QLDMTCTV_09-02-TCTV-SEED-0001-can-canh-cong-bo-va-tep-dinh-kem.png` | Cận cảnh 2 mục tranh chấp trên bản ghi **Đang hoạt động, rỗng 3 trường** + vùng kéo-thả kèm chú thích định dạng/20MB |
| 4 | `QLDMTCTV_09-03-TC-BTP-TW-0002-moi-dang-ky-cong-bo-va-tep-dinh-kem.png` | Bản ghi **Mới đăng ký, rỗng 3 trường** — vẫn đủ 2 mục |
| 5 | `QLDMTCTV_09-04-TC-BTP-TW-0003-co-du-lieu-3-truong-dien-san.png` | Bản ghi **CÓ dữ liệu** — 3 trường điền sẵn đúng, có tệp kèm nút Xem/Xóa |
| 6 | `QLDMTCTV_09-05-TC-BTP-TW-0001-cho-phe-duyet-cong-bo-va-tep-dinh-kem.png` | Bản ghi **Chờ phê duyệt, rỗng 3 trường** — vẫn đủ 2 mục |
| 7 | `QLDMTCTV_09-06-TC-BTP-TW-0002-da-nhap-3-truong-truoc-khi-luu.png` | Đã nhập Số QĐ, chọn Ngày QĐ, đính tệp PDF — **trước khi** bấm Lưu |
| 8 | `QLDMTCTV_09-07-TC-BTP-TW-0002-sau-khi-luu-man-chi-tiet-hien-so-qd-va-ngay-qd.png` | Sau khi lưu: màn Chi tiết hiện đủ Số QĐ + Ngày QĐ, trạng thái vẫn "Mới đăng ký" |
| 9 | `QLDMTCTV_09-08-TC-BTP-TW-0002-sau-tai-lai-trang-3-truong-con-du-lieu.png` | **Sau tải lại trang bỏ qua bộ nhớ đệm**: mở lại Sửa, cả 3 còn nguyên (kể cả tệp) |

---

## 5. Lập luận chốt verdict

1. Đối tác phản ánh **thiếu 3 trường trên biểu mẫu ở chế độ Sửa**. Đã xác minh **phản ánh này đúng với bản dựng họ chụp** — ảnh cho thấy biểu mẫu phẳng, không nhóm thu gọn, ảnh bao trọn chiều dài biểu mẫu, và thật sự không có 3 trường đó.
2. Trên bản dựng hiện tại **`HTPLDN · V1.0.5`**, đo ở **đúng vai trò và đúng đơn vị của đối tác**, cả 3 trường **đã có mặt ở chế độ Sửa**, hiện sẵn ngay khi mở (không cần mở nhóm nào), khớp đặc tả cả loại điều khiển lẫn ràng buộc.
3. 🔴 **Phép thử quyết định đã chạy đủ 2 nhánh và bác bỏ được kịch bản nguy hiểm nhất của case:** 3 bản ghi **chưa từng có dữ liệu** ở 3 trường (trong đó có **dữ liệu seed cũ nhất, không do QA tạo**) vẫn hiện **đủ** 3 trường; bản ghi **có dữ liệu** cũng hiện đủ và điền sẵn đúng. ⇒ Không tồn tại hiện tượng "bản ghi cũ mở ra thì thiếu trường".
4. Đã phủ **3 trạng thái** (Đang hoạt động · Mới đăng ký · Chờ phê duyệt) — biểu mẫu Sửa **không đổi theo trạng thái**, loại trừ khả năng form đổi theo state.
5. Cả 3 **dùng được thật** trên chính bản ghi vốn đang trống: nhập → lưu → **tải lại trang bỏ qua bộ nhớ đệm** → vẫn đủ dữ liệu.
6. Phần "**điền sẵn thông tin hiện có**" trong Kết quả mong đợi của đối tác cũng **đạt**; không tràn/đè, đồng nhất tiếng Việt.
7. Rà **toàn bộ** bảng Thành phần màn hình (dòng 1673–1696), **không thiếu trường nào khác**; 2 nút Hủy/Lưu đúng đặc tả.
8. ⇒ Lỗi dev khai đã sửa (`dev done`) là **có thật đã được sửa** và QA **kiểm chứng được bằng dữ liệu thật** ⇒ **`Pass`**.
9. **Vì sao KHÔNG dùng `Reject`:** `Reject` chỉ dùng khi chứng minh được đối tác **thao tác/hiểu sai**. Ở đây điều ngược lại — đối tác quan sát **đúng**, chỉ là trên bản dựng cũ hơn.
10. **Vì sao KHÔNG dùng `Resolved`:** `Resolved` dành cho bug **không tái hiện** mà nguyên nhân chưa rõ; ở đây dev đã khai fix và QA **xác nhận được đúng phần fix đó** ⇒ đúng định nghĩa `Pass`.
11. **Vì sao KHÔNG dùng `BA confirm`:** kỳ vọng của đối tác (biểu mẫu Sửa phải có 3 trường + điền sẵn dữ liệu) **trùng** với SRS, không có tranh chấp đặc tả cho case này.

---

## 6. Ngoài phạm vi case — quan sát thêm

1. **Biểu mẫu Sửa không chia 6 nhóm thu gọn như đặc tả** (SRS dòng 1664/1669/1676/1683/1686/1691). Web để phẳng, chỉ có 2 tiêu đề mục "Công bố" + "Tệp đính kèm". Trùng quan sát ở màn Thêm mới (case QLDMTCTV_06). **Không cản trở nhập liệu.**
2. **Breadcrumb ở chế độ Sửa không kèm tên tổ chức.** SRS dòng 1675 đòi nhánh "Chỉnh sửa **[Tên TC]**"; web chỉ hiện "… / Chi tiết / Chỉnh sửa". Quan sát này thấy **trên cả ảnh đối tác lẫn bản dựng hiện tại** ⇒ chưa được sửa. Nhỏ, chỉ ghi nhận.
3. **Thứ tự trường và một số nhãn rút gọn so với SRS** — giống màn Thêm mới, nghĩa không đổi.
4. **Mâu thuẫn nội tại của SRS (để BA chốt, KHÔNG dùng chấm case này):** bảng màn hình dòng **1681–1682** đánh dấu "Số Giấy ĐKHĐ" + "Ngày cấp" là **bắt buộc (\*)**, nhưng bảng Inputs dòng **1052–1053** ghi Bắt buộc = **N**. Web làm theo bảng màn hình (bắt buộc), cũng khớp bước 3 phần Processing (dòng 1073). **Hệ quả quan sát được ở chế độ Sửa:** bản ghi seed cũ `TCTV-SEED-0001` đang **trống cả 2 trường bắt buộc này**, nên muốn lưu bản ghi đó thì buộc phải bổ sung dữ liệu — dữ liệu cũ không thoả ràng buộc hiện hành.
5. **Màn Chi tiết chưa hiển thị vùng tệp đính kèm.** Bản ghi có tệp nhưng màn Chi tiết chỉ liệt kê thông tin chữ, phải vào Chỉnh sửa mới thấy tệp. Là **màn khác** (SCR-IV-NEW-03) ⇒ chỉ ghi nhận, chưa kết luận.
6. **Không kiểm được rule "ẩn nút Sửa khi Vô hiệu hóa"** (SRS dòng 1646): cả 3 tab "Đã từ chối", "Tạm dừng", "Vô hiệu hóa" đều **rỗng**. Không thuộc tiêu chí case.
7. **🔴 Một nghi vấn đã được truy tới cùng và KẾT LUẬN KHÔNG PHẢI LỖI** (đúng quy tắc "bug candidate ≠ bug"): danh sách **không có tab "Chờ phê duyệt"**, trong khi có bản ghi `TC-BTP-TW-0001` đang ở trạng thái đó ⇒ thoạt nhìn giống bản ghi bị "mất tích" khỏi giao diện. **Đã mở SRS kiểm:** dòng **1628** quy định tab "Chờ phê duyệt" **"Hiển thị khi vai trò là Cán bộ Phê duyệt"**. QA đang đăng nhập vai trò **Cán bộ Nghiệp vụ** ⇒ tab bị ẩn là **ĐÚNG đặc tả**. **Không log.**

---

## 7. Ghi chú đo lường — chống lặp lại lỗi 16/07

- Bộ bắt thông báo: **chỉ** dùng `tools/toast-capture.js`. Không lọc trùng, đọc bằng `innerText`, tự kiểm `soObserverDangSong = 1` trước khi tin số liệu. Luôn đếm request song song với số thông báo.
- **Chụp ảnh ở mọi thao tác đổi trạng thái — và đã MỞ RA ĐỌC từng ảnh.**
- **Đổi tên 2 ảnh cho khớp điểm ảnh** (tên ↔ nội dung ↔ claim phải khớp):
  1. `...-01-...-sua-phan-tren.png` → `...-01-TCTV-SEED-0001-form-sua-tu-dau-den-muc-cong-bo.png` (ảnh thực tế bao tới tận mục "Công bố" + đầu mục "Tệp đính kèm", tên cũ nói "phần trên" là mô tả thiếu).
  2. `...-07-...-ngay-sau-khi-bam-luu.png` → `...-07-TC-BTP-TW-0002-sau-khi-luu-man-chi-tiet-hien-so-qd-va-ngay-qd.png` (thông báo đã tự tắt trước khi chụp nên điểm ảnh **không có** thông báo; tên mới mô tả đúng thứ ảnh thật sự chứng minh).
- 🔴 **Hai lần selector của QA sai — KHÔNG phải lỗi ứng dụng**, đã truy tới cùng bằng mã HTML thô trước khi kết luận nên **không log oan**:
  1. Đọc giá trị dropdown bằng `.ant-select-selector` ra **rỗng** trong khi cây trợ năng và ảnh chụp đều cho thấy dropdown **có giá trị**. Hai phép đo mâu thuẫn ⇒ **không kết luận vội**, đọc thẳng HTML thô của ô đó thì thấy bản Ant Design của ứng dụng dựng giá trị ở `.ant-select-content-value` (chọn 1) và `.ant-select-selection-item` (chọn nhiều), **không có** `.ant-select-selector`. ⇒ Sửa phép đo, kết quả trùng với ảnh. **Nếu tin phép đo đầu sẽ báo oan "biểu mẫu Sửa không điền sẵn Loại hình / Lĩnh vực".**
  2. Đọc vùng tệp bằng `.ant-upload` nên **không thấy tên tệp đã đính** trên bản ghi `TC-BTP-TW-0003`. Đọc lại nguyên khối vùng tệp thì thấy đủ "QA-QD-cong-bo-QLDMTCTV06.pdf (613 B) Xem Xóa" — danh sách tệp nằm **cạnh** vùng kéo-thả chứ không nằm **trong** nó. ⇒ Phép đo sai, không phải ứng dụng mất dữ liệu.
- Theo cảnh báo từ case QLDMTCTV_06, **không dùng ảnh chụp chế độ "toàn trang"**; toàn bộ bằng chứng chụp theo **khung nhìn + cuộn**, và mọi ảnh dùng làm bằng chứng đều **đối chiếu lại với phép đo cây DOM** trước khi kết luận.
- Tệp dùng để kiểm tải lên đặt tại `output/UAT_doi-tac/scratchpad_notes/upload-fixture/QA-QD-cong-bo-QLDMTCTV09.pdf` (PDF hợp lệ 398 B).
