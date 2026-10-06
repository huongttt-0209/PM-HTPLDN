# QLHSPLDN_06 — Audit verify vòng 1 (2026-08-03)

**Dòng sheet:** 324 · **Tab:** `UAT_TGPL Doanh Nghiệp-tuần 3` · **Verdict QA:** `Pass` (cột Q — Verify)
**Môi trường:** https://18.143.165.120.nip.io — bản dựng đọc ở chân menu trái: **`HTPLDN · V1.0.5`**
**Tài khoản dùng ra verdict:** `cbnv_tw_04` (CB Nghiệp vụ - Trung ương, `CB_NV_TW`, phạm vi `BTP · TW`) — **trùng vai trò + cấp của đối tác**. Tài khoản đối chiếu vai trò thứ hai: `0109998887` (Doanh nghiệp). **KHÔNG dùng `admin` để ra verdict.**

---

## Note dev trước khi QA đè (2026-08-03 20:53:50)

**Cột R (`DEV phản hồi lần 1`) TRỐNG — không có note dev để lưu.**
Cột P (`Trạng thái dev fix 1`) = `dev done` (giữ nguyên, QA KHÔNG đụng). Dev không viết giải trình kèm theo, nên không có nội dung nào bị mất khi QA ghi note vào cột R.

Các cột khác của dòng 324 tại thời điểm verify (chỉ để đối chiếu, QA không sửa):
- `G` Mô tả: `Xem`
- `H` Điều kiện: `1. Đăng nhập hệ thống thành công`
- `J` Các bước thực hiện: `1. Chọn menu "Doanh nghiệp" → 2. Nhấn "Xem chi tiết" → 3. Chọn thẻ "Hồ sơ pháp lý doanh nghiệp" → 4. Nhấn "Xem"`
- `K` Kết quả mong đợi: `Hệ thống mở cửa sổ chi tiết hiển thị toàn bộ thông tin của hồ sơ và danh sách tệp đính kèm (nếu có) ở chế độ chỉ đọc.`
- `L` Kết quả thực tế: `Màn hình không có nút chức năng xem chi tiết`
- `M` Ảnh: `QLHSPLDN_06.jpg` · `N` Trạng thái 1: `Fail`

---

## Cổng 1 — Bằng chứng đối tác (đã mở FULL-RES bằng tool Read)

**File:** `partner-evidence/QLHSPLDN_06.jpg` — ảnh tĩnh, độ phân giải gốc **1904×1031**, mở đọc trực tiếp chữ trên ảnh. Không có video cho case này nên không cần trích frame.

### 3 dữ kiện neo (viết ra TRƯỚC khi hình thành giả thuyết)

| # | Dữ kiện | Giá trị đọc được từ ảnh |
|---|---|---|
| a | URL / bản ghi | `htpldn-uat.ospgroup.vn/doanh-nghiep/1a715c55-bc31-46de-ae07-56dd4f403ce5?tab=ho-so-pl` · tiêu đề **"Chi tiết DN #DN-XX-0005"** · thẻ đang mở: **Hồ sơ pháp lý** (thanh thẻ: Thông tin / Hồ sơ pháp lý / Lịch sử hỗ trợ / Hồ sơ chi trả) |
| b | Trạng thái entity | 2 bản ghi `HO_SO_PHAP_LY_DN`, **cả hai nhãn xanh "Hiệu lực"**. `HSPL-20260803-0001` (Khác · Thuế · Thủ công · cấp 03/08/2026 · hết hạn 03/08/2026) · `HSPL-20260731-0002` (Giấy chứng nhận · Đất đai · Thủ công · cấp 01/07/2026 · hết hạn "–") |
| c | Dữ liệu tiền đề | Góc phải trên: **"Cán bộ NV Trung ương · CB_NV_TW"**, phạm vi **BTP · TW**. Đồng hồ máy đối tác **2026-08-03 10:03**. Cả 2 hồ sơ nguồn **Thủ công**. Có nút **[Thêm hồ sơ]** góc phải bảng |

### Khoảnh khắc lỗi trong ảnh

Chính khung hình này. Cột **Hành động** của **cả 2 hàng** chỉ chứa đúng **2 nút: `[Sửa]` `[Xoá]`**. Không có nút thứ ba, không có biểu tượng con mắt, không có nhóm lệnh "…". Bảng của đối tác có **9 cột** (Mã hồ sơ / Tên hồ sơ / Loại / Lĩnh vực pháp lý / Nguồn / Ngày cấp / Ngày hết hạn / Trạng thái / Hành động) — **không có** cột "Có tệp đính kèm".

⇒ Phản ánh của đối tác **chính xác đối với bản dựng họ chụp**. Không có dấu hiệu họ bỏ sót do chưa cuộn (cột Hành động là cột ghim phải, hiện đủ trong ảnh) hay do chọn nhầm màn.

## Cổng 2 — Hiểu bug (3 dòng)

1. **Evidence đã xem:** `partner-evidence/QLHSPLDN_06.jpg`, ảnh tĩnh (không có mốc thời gian video) — khung hình cho thấy cột Hành động của bảng "Hồ sơ pháp lý DN" chỉ có `[Sửa] [Xoá]`, thiếu hẳn nút mở chi tiết.
2. **Đối tác phản ánh CỤ THỂ:** thiếu **nút mở chi tiết hồ sơ** trên từng hàng của bảng Hồ sơ pháp lý DN ⇒ không thực hiện được bước 4 của kịch bản ("Nhấn Xem") ⇒ không xem được toàn bộ thông tin hồ sơ + danh sách tệp đính kèm ở chế độ chỉ đọc.
3. **Data + bước tái hiện:** cần 1 DN có ≥1 hồ sơ pháp lý. Đăng nhập vai trò Cán bộ Nghiệp vụ → menu **Doanh nghiệp** → **Xem chi tiết** một DN → thẻ **Hồ sơ pháp lý** → tìm nút mở chi tiết trên từng hàng.

---

## Thứ tự đo — CHỐNG THIÊN KIẾN

**ĐO WEB TRƯỚC, ĐỌC SRS SAU.** Toàn bộ số đo mục dưới được ghi lại trước khi mở bất kỳ file SRS nào. Chỉ sau khi có số đo mới grep SRS để đối chiếu.

---

## Số đo thực tế trên web (bản `HTPLDN · V1.0.5`)

### Bối cảnh đo

- DN dùng để đo: **`DN-HNI-0001` — `Cong ty TNHH QA UAT Kiem Thu`** (MST 0109998887), id `829abcac-b0af-4cde-9af9-ec51bc79014c`, đường dẫn `?tab=ho-so-pl` — **cùng dạng màn, cùng thẻ** với ảnh đối tác.
- Bảng của web hiện tại có **10 cột** — 9 cột như đối tác **+ thêm cột "Có tệp đính kèm"**.

### Đo 1 — số nút trên cột Hành động (3 cách độc lập, cùng kết quả)

| Cách đếm | Kết quả |
|---|---|
| Đếm nút trong ô cuối của mỗi hàng (`td:last-child button`) | **18** nút / 6 hàng = 3 nút/hàng |
| Đếm nút có chữ đúng bằng "Xem" (đọc bằng `innerText`) | **6** |
| Đếm biểu tượng con mắt (`.anticon-eye`) trong thân bảng | **6** |

Cột Hành động mỗi hàng = **`[👁 Xem]` `[Sửa]` `[Xoá]`**.

### Đo 2 — nút Xem có thật sự dùng được không (không chỉ tồn tại trong DOM)

Đo trên **cả 6 hàng**, mọi hàng cho cùng kết quả:

| Thuộc tính | Giá trị đo được | Nghĩa |
|---|---|---|
| `disabled` | `false` | không bị vô hiệu hoá |
| `aria-disabled` | `null` | không bị đánh dấu vô hiệu cho trợ năng |
| `pointer-events` | `auto` | nhận được sự kiện chuột |
| `opacity` | `1` | không bị làm mờ |
| Kích thước thật | `68 × 24` điểm ảnh | không phải phần tử 0×0 ẩn |
| Toạ độ | `x = 1164 … 1232` (khung nhìn rộng 1440) | nằm trọn trong tầm nhìn |

### Đo 3 — bấm Xem thì có gì xảy ra

- Bấm `[Xem]` hàng `HSPL-20260727-0001` → mở cửa sổ **"Chi tiết hồ sơ pháp lý"**.
- Nội dung đọc được: `Mã hồ sơ HSPL-20260727-0001` · `Tên hồ sơ R27 HS kiem thu day du tieu chi` · `Loại hồ sơ Hợp đồng` · `Lĩnh vực pháp lý Lao động` · `Nguồn Thủ công` · `Cơ quan cấp —` · `Ngày cấp —` · `Ngày hết hạn —` · `Trạng thái Hiệu lực` · `Mô tả Noi dung kiem thu mo ta R27` · mục **Tệp đính kèm**: `R27-HSPL-RETEST.pdf (627 B)` kèm 2 nút `Xem` / `Tải` · nút `Đóng`.
- **Chế độ chỉ đọc:** đếm được **0 ô nhập liệu** trong cửa sổ (0 `input`, 0 `textarea`, 0 ô chọn) ⇒ đúng yêu cầu "chế độ chỉ đọc" ở cột K của phiếu.
- Số request / số thông báo khi bấm Xem: **0 request ghi dữ liệu · 0 khung thông báo** — hợp lý, dữ liệu lấy từ danh sách đã tải.

### Đo 4 — seed để phủ trạng thái còn thiếu (tự tạo, KHÔNG coi là blocker)

Môi trường ban đầu chỉ có hồ sơ trạng thái **Hiệu lực** (4 bản ghi) — thiếu 2 trạng thái còn lại. Đội kiểm thử **tự tạo** qua chính giao diện, bằng đúng tài khoản `cbnv_tw_04`:

| Bản ghi tạo | Loại | Trạng thái | Request / Thông báo | Kết quả |
|---|---|---|---|---|
| `HSPL-20260803-0001` — "QA0803 HSPL trang thai HET HAN" | Quyết định | **Hết hạn** | **1 request** `POST /api/v1/ho-so-phap-ly-dns` / **1 thông báo** "Thêm hồ sơ thành công" | Tạo OK, không lặp thông báo, không tạo trùng |
| `HSPL-20260803-0002` — "QA0803 HSPL trang thai THU HOI" | Giấy chứng nhận | **Thu hồi** | **1 request** `POST /api/v1/ho-so-phap-ly-dns` / **1 thông báo** "Thêm hồ sơ thành công" | Tạo OK, không lặp thông báo, không tạo trùng |

Bộ bắt thông báo dùng **đúng `tools/toast-capture.js`** (không lọc trùng, đọc bằng `innerText`), đã **tự kiểm `soObserverDangSong = 1`** trước mỗi lần tin số liệu.

### Đo 5 — nút Xem theo từng trạng thái (sau khi seed)

| Mã hồ sơ | Trạng thái | Cột Hành động | Số nút |
|---|---|---|:-:|
| `HSPL-20260803-0002` | **Thu hồi** | Xem \| Sửa \| Xoá | 3 |
| `HSPL-20260803-0001` | **Hết hạn** | Xem \| Sửa \| Xoá | 3 |
| `HSPL-20260727-0001` | Hiệu lực | Xem \| Sửa \| Xoá | 3 |
| `HSPL-20260725-0002` | Hiệu lực | Xem \| Sửa \| Xoá | 3 |
| `HSPL-20260725-0001` | Hiệu lực | Xem \| Sửa \| Xoá | 3 |
| `HSPL-20260721-0001` | Hiệu lực | Xem \| Sửa \| Xoá | 3 |

**6/6 hàng · 3/3 trạng thái đều có nút Xem.**

---

## 🔴 Danh sách các khả năng đã LOẠI TRỪ

Đây là loại case "thiếu nút" — dễ kết luận sai nhất. Từng khả năng dưới đây được đóng bằng **đo thật**, không bằng lập luận:

| # | Khả năng | Cách loại trừ | Kết quả |
|:-:|---|---|---|
| 1 | **Nút chỉ hiện với vai trò khác** | Đo ở **2 vai trò** trong **2 phiên trình duyệt cách ly riêng**: (a) `cbnv_tw_04` — trùng khớp vai trò `CB_NV_TW` + cấp `BTP · TW` của đối tác; (b) `0109998887` — vai trò **Doanh nghiệp** | (a) có đủ nút Xem trên 6/6 hàng. (b) vai trò DN **không có màn này**: đăng nhập DN → menu "Doanh nghiệp" dẫn tới `/doanh-nghiep/me/sua` là màn "Hồ sơ doanh nghiệp" **không có thẻ nào** (đếm được 0 thẻ); ép mở đường dẫn màn chi tiết DN thì bộ định tuyến đá về `/vu-viec/danh-sach`. ⇒ Nút **không phải** thứ chỉ dành cho vai trò khác |
| 2 | **Nút chỉ hiện ở trạng thái bản ghi khác** | Môi trường chỉ có trạng thái **Hiệu lực** → **tự seed** thêm 2 hồ sơ để phủ **Hết hạn** và **Thu hồi** (xem Đo 4). Hệ thống chỉ có đúng 3 trạng thái cho hồ sơ pháp lý | **3/3 trạng thái** đều có nút Xem (Đo 5). Không có trạng thái nào làm nút biến mất |
| 3 | **Nút bị cuộn ngang khuất** | Đo bằng toạ độ thật thay vì nhìn ảnh: bảng **CÓ** cuộn ngang (bề rộng nội dung 1425 > bề rộng khung 1048), nhưng ô Hành động mang lớp `ant-table-cell-fix-end` = **cột ghim bên phải**, toạ độ `x = 1148 → 1368` trong khung nhìn rộng 1440, `scrollLeft = 0` | Cột Hành động **luôn hiện**, không thể bị cuộn khuất. Ảnh đối tác cũng cho thấy cột này hiện đủ ⇒ họ không bỏ sót vì cuộn |
| 4 | **Nút nằm trong nhóm lệnh "…" / menu thả xuống** | Quét toàn bộ ô Hành động: mỗi ô có đúng **3 phần tử điều khiển**, đều là thẻ `BUTTON` có chữ hiển thị ("Xem" / "Sửa" / "Xoá"), **không có** phần tử nào là nút "…" hay menu thả xuống | Không có menu ẩn. Cả bản của đối tác lẫn bản hiện tại đều dùng nút rời, không gom nhóm |
| 5 | **Nút tồn tại nhưng bị vô hiệu hoá** (khác hẳn "không có nút") | Đo 6 thuộc tính cho từng nút Xem trên cả 6 hàng (xem Đo 2) | Không nút nào bị vô hiệu hoá. Và bấm thật thì mở được cửa sổ chi tiết ⇒ dùng được, không phải "có mà bấm không ăn" |
| 6 | **Bấm cả hàng / thẻ để mở chi tiết thay cho nút** | Bấm vào ô dữ liệu "Tên hồ sơ" của hàng (không phải nút) rồi đợi 1,2 giây; đồng thời đo con trỏ chuột của hàng | Bấm hàng **KHÔNG** mở chi tiết; con trỏ hàng là `auto` (không phải `pointer`). ⇒ Cơ chế mở chi tiết **duy nhất** là nút Xem — và nút đó đã có. Ghi nhận: nếu bản cũ của đối tác cũng không cho bấm hàng thì họ thật sự không còn cách nào mở chi tiết, càng củng cố phản ánh của họ là đúng với bản đó |

**Cảnh giác với chính phép đo (bài học postmortem 16/07):** trong phiên này có **1 lần selector của QA sai** — dùng `.ant-modal-wrap:not([style*="display: none"]) .ant-modal-content` để dò cửa sổ chi tiết thì trả về `coModal = false`, trong khi tiêu đề cửa sổ vẫn đọc được là "Chi tiết hồ sơ pháp lý". **Không kết luận "cửa sổ không mở"** mà đo lại bằng cách khác (quét thẳng `.ant-modal-wrap` + đọc `innerText` + chụp ảnh mở ra đọc) → xác nhận cửa sổ **có mở thật**. Đây đúng là tình huống "selector trả 0 không có nghĩa là thiếu phần tử".

---

## Phép thử thứ hai (đo lại bằng phương pháp khác)

Giao diện cho kết quả "đã có nút Xem và mở được chi tiết" → kiểm chứng lại bằng **gọi thẳng dịch vụ máy chủ** trong chính phiên của vai trò `cbnv_tw_04`:

| Phép gọi | Kết quả |
|---|---|
| Lấy danh sách hồ sơ pháp lý của DN | HTTP **200**, trả **6 bản ghi** — khớp đúng 6 hàng đang hiện trên giao diện, trạng thái trả về `THU_HOI` / `HET_HAN` / `HIEU_LUC` ×4, nguồn `THU_CONG` cho cả 6 |
| Lấy **chi tiết** 1 hồ sơ theo mã định danh | HTTP **200**, trả full bản ghi gồm `maHoSo, tenHoSo, doanhNghiepId, loaiHoSo, linhVucId, soKyHieu, ngayCap, ngayHetHan, coQuanCap, trangThai, nguon, ghiChu, doanhNghiep, linhVuc, donVi, **fileDinhKem**` |

⇒ **Hai phương pháp không mâu thuẫn:** giao diện có nút và mở được chi tiết; máy chủ cũng có sẵn dịch vụ trả chi tiết kèm tệp đính kèm. Không rơi vào ca "2 phương pháp mâu thuẫn → chưa được ghi verdict".

---

## Cổng 3 — SRS vs web

**Đã grep TOÀN BỘ 18 file trong `srs-v3.5/`** cho khái niệm "Hồ sơ pháp lý" trước khi chốt (kết quả: xuất hiện ở `srs-fr-07-doanh-nghiep.md`, `srs-fr-12-tv-chuyen-sau.md`, `srs-fr-16-api.md`, `srs-v3.5.md`, `CHANGELOG-v3-to-v3.5.md`), **không** đọc một dòng rồi kết luận. Mọi số dòng dưới đây đều mở file đọc trực tiếp, không lấy từ trí nhớ.

| SRS yêu cầu (dẫn dòng) | Thực tế web | Đủ/Thiếu |
|---|---|:-:|
| `srs-fr-12-tv-chuyen-sau.md:550` — FR-X.1-04 mô tả: *"CRUD hồ sơ pháp lý doanh nghiệp: xem danh sách, **xem chi tiết**, thêm mới, chỉnh sửa, xóa mềm, tìm kiếm."* | Có nút Xem trên 6/6 hàng, bấm mở được cửa sổ chi tiết | ✅ Đủ |
| `srs-fr-12-tv-chuyen-sau.md:634` — khối *Processing — Xem chi tiết*, bước 3 *"Trả full record: thông tin hồ sơ + thông tin DN liên kết"* | Cửa sổ hiển thị 11 mục thông tin hồ sơ | ✅ Đủ |
| `srs-fr-12-tv-chuyen-sau.md:634` bước 4–5 — *"Truy vấn danh sách file đính kèm… trả kèm tên, loại, dung lượng, URL preview"* | Mục "Tệp đính kèm": `R27-HSPL-RETEST.pdf (627 B)` + 2 nút Xem / Tải | ✅ Đủ |
| `srs-fr-12-tv-chuyen-sau.md:693` — AC: *"**Given** CB NV xem chi tiết hồ sơ **When** chọn bản ghi **Then** hiển thị đầy đủ thông tin + file đính kèm"* | Đúng như vậy, ở đúng vai trò CB NV | ✅ Đủ |
| `srs-fr-07-doanh-nghiep.md:468` — SCR-V.III-02 thành phần 2: *"Tab Hồ sơ PL doanh nghiệp… **CRUD hồ sơ pháp lý DN**: 5 loại × 3 trạng thái"* | Đúng màn đối tác đứng; đủ cả C-R-U-D: Thêm hồ sơ / Xem / Sửa / Xoá | ✅ Đủ |
| Cột K của chính phiếu: *"mở cửa sổ chi tiết hiển thị toàn bộ thông tin + danh sách tệp đính kèm ở chế độ chỉ đọc"* | Cửa sổ chi tiết có 0 ô nhập liệu ⇒ chỉ đọc | ✅ Đủ |

**Kiểm mâu thuẫn nội tại của SRS (bắt buộc trước khi chốt):** chỗ **duy nhất** trong toàn bộ SRS gọi danh sách hồ sơ pháp lý là *"Read-only"* là `srs-fr-07-doanh-nghiep.md:523`. Nhưng dòng đó nằm trong **SCR-V.III-04 "Hồ sơ doanh nghiệp của tôi"** (`srs-fr-07-doanh-nghiep.md:508`) — **chuyên trang của vai trò Doanh nghiệp**, không phải màn của cán bộ mà đối tác đang đứng. ⇒ **Không có mâu thuẫn** giữa các nguồn cho màn đang xét, nên **không** rơi vào ca `BA confirm`.

**Ghi chú tránh trích dẫn nhầm:** `srs-fr-07-doanh-nghiep.md:451` có câu *"Xem luôn hiển thị; Sửa/Xóa chỉ hiển thị khi user có quyền…"* — nhưng dòng này thuộc **SCR-V.III-01 Danh sách Doanh nghiệp** (`srs-fr-07-doanh-nghiep.md:410`), nói về nút trên **bảng danh sách DN**, KHÔNG phải bảng hồ sơ pháp lý. **Không dùng dòng này làm căn cứ cho case.**

**Mã UC dùng cho note:** `srs-fr-12-tv-chuyen-sau.md:543` ghi `**UC Reference:** UC 150`. Vì verdict là `Pass`, note gửi đối tác **chỉ dùng tên chức năng bằng lời**, không đưa mã FR / số dòng SRS / mã màn (theo `QA_VERIFY_PROTOCOL.md` §Viết note sheet cho đối tác).

---

## GATE bằng chứng real-data

Loại claim của case = **Hiển thị/render** (thiếu nút) + **Thao tác/state** (bấm nút phải mở được chi tiết). Artifact QUAN SÁT, chạy trên dữ liệu thật đã seed, đều **đã mở ảnh ra đọc pixel**, tên file khớp nội dung:

| Ảnh | Nội dung đã đọc |
|---|---|
| `image/QLHSPLDN_06-cbnv-tab-hsplDN-co-nut-xem.png` | Bảng "Hồ sơ pháp lý DN" của `DN-HNI-0001`, 4 hàng, mỗi hàng đủ `[👁 Xem] [Sửa] [Xoá]`; góc phải trên "CB Nghiệp vụ - Trung ương #04 · CB_NV_TW", chân menu "HTPLDN · V1.0.5" |
| `image/QLHSPLDN_06-cbnv-modal-chi-tiet-ho-so.png` | Cửa sổ "Chi tiết hồ sơ pháp lý" mở trên `HSPL-20260727-0001`, đủ 11 mục thông tin + mục Tệp đính kèm `R27-HSPL-RETEST.pdf (627 B)` + nút Xem/Tải + nút Đóng |
| `image/QLHSPLDN_06-seed-form-them-ho-so-het-han.png` | Biểu mẫu "Thêm hồ sơ pháp lý" đã điền: Tên "QA0803 HSPL trang thai HET HAN", Loại "Quyết định", Trạng thái "Hết hạn" — ảnh của **bước seed**, chụp và đọc theo yêu cầu postmortem |
| `image/QLHSPLDN_06-cbnv-3-trang-thai-deu-co-nut-xem.png` | Bảng sau seed: **6 hàng**, gồm 1 hàng Thu hồi + 1 hàng Hết hạn + 4 hàng Hiệu lực, **mọi hàng đều có `[👁 Xem] [Sửa] [Xoá]`** |
| `image/QLHSPLDN_06-vaitro-DN-khong-co-man-tab-ho-so-phap-ly.png` | Phiên vai trò **Doanh nghiệp** (`QA UAT Kiem Thu DN · DN`, phạm vi BTP · DP): màn "Hồ sơ doanh nghiệp — Cong ty TNHH QA UAT Kiem Thu, MST 0109998887", **không có thanh thẻ nào**, không có thẻ Hồ sơ pháp lý |

---

## Kết luận

- Lỗi đối tác báo (thiếu nút mở chi tiết) **KHÔNG còn tái hiện** trên bản dựng `HTPLDN · V1.0.5`, kiểm ở **đúng vai trò và đúng cấp** của đối tác.
- Đủ 6 khả năng gây kết luận sai đã được loại trừ bằng đo thật, trong đó 2 khả năng phải **tự seed dữ liệu** mới đóng được.
- Web đáp ứng đúng cả đặc tả (FR-X.1-04) lẫn kết quả mong đợi ghi trong chính phiếu của đối tác.
- **KHÔNG dùng `Reject`**: đối tác có bằng chứng thật và không hề thao tác/hiểu sai — bản dựng họ chụp đúng là thiếu nút.
- **⇒ Verdict `Pass`** (cột Q). Cột P giữ nguyên `dev done`.

---

## Ngoài phạm vi case (CHƯA log — mô tả để user quyết)

1. **Thẻ Hồ sơ pháp lý không có ô tìm kiếm, không có bộ lọc, không có nút Xuất Excel.** Đo được: 0 ô tìm kiếm, 0 ô chọn lọc, 0 nút xuất trong vùng bảng; vùng bảng chỉ có nút "Thêm hồ sơ" + bảng + phân trang. Trong khi `srs-fr-12-tv-chuyen-sau.md` mục *Inputs — Tìm kiếm* của FR-X.1-04 định nghĩa **5 điều kiện lọc** (từ khoá, loại hồ sơ, DN, khoảng ngày, trạng thái) và **dòng 644** có hẳn khối *Processing — Xuất Excel*. **Nhưng** màn hình gốc `SCR-X1-03` đã bị đánh dấu **DEPRECATED** (`srs-fr-12-tv-chuyen-sau.md:547`) và bản thay thế là tab, mà mô tả tab ở `srs-fr-07-doanh-nghiep.md:468` **chỉ ghi "CRUD"** — không nhắc tìm kiếm/xuất Excel. ⇒ Thật sự **mơ hồ giữa hai chỗ trong SRS**, nên **không tự chấm là bug**; nếu user muốn đưa tới dev/BA thì nên mở dòng TC mới và hỏi BA phạm vi tab sau khi gộp màn.
2. **Không bấm được vào hàng để mở chi tiết.** Con trỏ hàng là `auto`, bấm ô dữ liệu không mở gì. Bảng anh em cùng nhóm (bảng nội dung Tư vấn chuyên sâu) được đặc tả rõ *"click hàng → xem chi tiết"* ở `srs-fr-12-tv-chuyen-sau.md:1112`, còn bảng hồ sơ pháp lý thì SRS **không quy định**. Hiện đã có nút Xem nên người dùng không bị chặn — chỉ là khác biệt trải nghiệm giữa 2 bảng.
3. **Ký hiệu ô trống không nhất quán trong cùng một bảng.** Cột "Lĩnh vực pháp lý" dùng gạch dài `—`, cột "Ngày cấp" / "Ngày hết hạn" dùng gạch ngắn `-`. Thuần mỹ thuật, không ảnh hưởng nghiệp vụ.
4. **Ở khung nhìn 1440 điểm ảnh, các cột "Trạng thái" và "Có tệp đính kèm" nằm ngoài vùng nhìn, phải cuộn ngang mới thấy.** Cột Hành động được ghim nên vẫn hiện. Ảnh của đối tác cũng bị cắt cột Trạng thái y hệt. SRS không quy định bề rộng cột nên **không chấm là sai đặc tả**, chỉ nêu vì nó khiến trạng thái hồ sơ — thông tin quan trọng — không thấy ngay.

## Ghi chú đo lường (chống lặp lại lỗi 16/07)

- Bộ bắt thông báo: dùng **nguyên văn** `tools/toast-capture.js` — **không lọc trùng**, đọc bằng `innerText`, đếm request song song. Đã **tự kiểm `soObserverDangSong = 1`** trước mỗi lần tin số liệu.
- Cả **2 thao tác ghi dữ liệu** (seed 2 hồ sơ) đều đo được **1 request / 1 khung thông báo** → không có thông báo lặp, không tạo trùng bản ghi.
- **Mọi ảnh đều đã được mở ra đọc bằng tool Read**, không chỉ lưu; kể cả ảnh của **bước seed**.
- Đã tính tới bẫy "tab mở lâu vẫn chạy mã cũ": phiên này là phiên **đăng nhập mới hoàn toàn** trong ngữ cảnh trình duyệt cách ly riêng (`hspl06-cbnv`), tải trang từ đầu, bản dựng đọc trực tiếp trên giao diện là `HTPLDN · V1.0.5`.
