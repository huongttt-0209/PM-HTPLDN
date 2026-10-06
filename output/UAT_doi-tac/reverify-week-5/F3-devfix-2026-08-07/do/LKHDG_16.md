# Nhật ký đo — LKHDG_16 (dòng 127) · lô F3-devfix-2026-08-07

**Đo lúc:** 2026-08-07 02:13 → 02:21 giờ VN · **Agent:** agent ĐO (Chrome DevTools MCP)
**Chuẩn chấm áp dụng:** `output/UAT_doi-tac/reverify-week-5/F3-devfix-2026-08-07/chuan/LKHDG_16.md` (khối PASS/FAIL §7, đã khóa — không sửa)
**Bug entry:** `BUG-LKHDG-SUA-PHANCONG` trong `output/UAT_doi-tac/reverify-bug-devfix-2026-08-06/bug-reports/bug-report-LKHDG.md`

---

## 1. Vân tay bản dựng (đo đầu phiên, dùng chung với case 126)

| Hạng mục | Giá trị đo được | Bản đã biết | Kết |
|---|---|---|---|
| Chuỗi phiên bản chân sidebar | **`HTPLDN · V1.0.9`** | `V1.0.8` | 🔼 ĐỔI |
| Bó mã FE | **`assets/index-DsMHK7Dp.js`** | `index-DThrFe1_.js` (bug-report + tiêu chí + phiếu BA) · `index-DIABnbIr.js` (TIEN-DO.md) | 🔼 **KHÔNG trùng bản nào trong hai** |
| CSS | `assets/index-DVlgOkLg.css` | y hệt | giữ nguyên |
| `GET /` last-modified | **`Thu, 06 Aug 2026 18:51:25 GMT`** | `Thu, 06 Aug 2026 07:13:15 GMT` | 🔼 ĐỔI (+~11,5 giờ) |
| `GET /` etag | **`W/"6a74d7ad-428"`** | `W/"6a74340b-428"` | 🔼 ĐỔI |

⇒ Cảnh báo §11.1 của chuẩn (*"trùng một trong hai ⇒ báo điều phối TRƯỚC khi chốt verdict"*) **KHÔNG kích hoạt** — có bản dựng mới thật.
⚠️ Sidebar đọc **V1.0.9** (không phải V1.0.10 như tin nền của lô). Ghi đúng cái đo được.

**Tài khoản:** `cbnv_tw` / `Test@1234`, đăng nhập UI thật + mã 6 số MailHog. `GET /api/v1/auth/me` xác nhận `vaiTro=["CB_NV_TW"]`, `donViId=00000000-0000-4000-8000-000000000001`, `capDonVi=TW`. Không dùng `admin`. Không cần fallback Rule 7.

---

## 2. Đặc tả (tự mở đếm lại ngày 07/08, KHÔNG bê số cũ)

| Dòng | Nguyên văn (`Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-08-danh-gia.md`) |
|---|---|
| **`:839`** | `\| 18 \| table \| Hành động \| icon-group \| Xem / Sửa (chỉ LAP_KE_HOACH/PHAN_CONG) / Xóa (chỉ LAP_KE_HOACH) \| click → tương ứng \| Luôn \|` |
| **`:161`** | `- **Given** CB NV chỉnh sửa KH chưa duyệt **When** thay đổi **Then** validate + lưu` |
| **`:852`** | `\| 25a \| form \| Cơ quan được đánh giá \| C10 dropdown searchable \| **Bắt buộc.** Danh sách chọn từ danh mục Đơn vị, chọn 1 đơn vị (1:1)… \`[CR-10][BA chốt 2026-08-06]\` \| change → validate \| Khi mở form \|` |
| **`:854`** | `\| 26a \| form \| Tài liệu đính kèm \| C15 File Upload \| Không bắt buộc… **Hiện danh sách tệp đã có kèm thao tác [Xem] [Xóa]** \`[CR-07][BA chốt 2026-08-06]\` \| upload → validate \| Khi mở form \|` |
| **`:1191`** | `\| LAP_KE_HOACH \| PHAN_CONG \| CB NV phân công \| Có KH \| Gán CB/CG \| FR-VI-03 \| — \|` |

Kiểm chứng phụ (tự chạy hôm nay): `grep -rn "ERR-BIZ-XI" srs-v3.5/` → **0 kết quả** (mã lỗi máy chủ trả vòng trước không tồn tại trong đặc tả). File `srs-fr-08-danh-gia.md` hiện **1280 dòng**.

🔴 Dẫn cũ trong hồ sơ 06/08 **đều lệch** và đã được sửa trong bug entry: `:837` → **`:839`** · `:159` → **`:161`** · `:1188` → **`:1193`** · `:1185-1194` → **`:1190-1199`**.

---

## 3. Tiền đề đã dựng

**Không phải dựng gì thêm** — tiền đề bắt buộc đã có sẵn:

| Dạng (chuẩn §4) | Yêu cầu | Bản ghi thực dùng | Đạt |
|---|---|---|:-:|
| **3 — dạng QUYẾT ĐỊNH VERDICT** | Trạng thái **Phân công** + ≥1 tệp đính kèm, thuộc đơn vị tài khoản | **`DG-20260806-0001`** — `id=a7d1b311-0a3e-4cd9-bb6b-fb92437df902`, `trangThai=PHAN_CONG`, `donViId=…8000-000000000001` (đúng đơn vị `cbnv_tw`), **1 tệp** `QA-LKHDG16-ke-hoach.pdf` | ✅ |
| 2 | Lập kế hoạch + ≥2 tệp **khác định dạng** | **`DG-20260730-0002`** — 2 tệp `QA-LKHDG16-baocao-mau.docx` (1.3 KB) + `QA-LKHDG16-ke-hoach.pdf` (398 B) | ✅ |
| 1 | Lập kế hoạch + **đúng 1** tệp | **KHÔNG dựng** — xem §7 | ❌ |

Không phải chạy công thức a) tiêu chí → b) thêm người đánh giá: `DG-20260806-0001` vẫn còn nguyên ở `PHAN_CONG` từ vòng 06/08. Guard `BR-CALC-08` không phải chạm tới.
⚠️ **Dữ liệu env đã bị đổi trước phiên đo:** tên `DG-20260806-0001` hiện kết thúc bằng `"- sua v1.0.9"` và `version` đã ở **5** khi tôi bắt đầu — tức đã có người/quy trình khác sửa bản ghi này trên bản dựng V1.0.9 trước tôi. Không ảnh hưởng phép đo (bug là **luật chặn theo trạng thái phía máy chủ**, không phải trường đã đóng băng trong CSDL — chuẩn §9.9 cho phép đo lại trên bản ghi cũ), nhưng ghi lại để điều phối biết.

---

## 4. Các bước đo + quan sát thô

### Bước 1 — đợt đang *Lập kế hoạch*: cột Hành động có mấy thao tác
`DG-20260730-0002` (Lập kế hoạch) → **3 thao tác**: `Xem chi tiết` · **`Sửa kế hoạch`** · `Xóa kế hoạch`.

### Bước 2 — đợt đang *Phân công*: cột Hành động có mấy thao tác. So với bước 1
`DG-20260806-0001` (Phân công) → **2 thao tác**: `Xem chi tiết` · **`Sửa kế hoạch`** — **không** có `Xóa`.

⇒ Khớp **đúng từng chữ** với `:839`: *Sửa* mở cho cả `LAP_KE_HOACH` và `PHAN_CONG`, *Xóa* chỉ mở cho `LAP_KE_HOACH`.
Đếm bằng **DOM** (`aria-label` của phần tử trong ô Hành động) **và** ảnh chụp cùng một bảng có cả 2 hàng — không chỉ đếm thẻ `button`.
Đối chiếu toàn bảng 20 hàng: mọi hàng ở 6 trạng thái còn lại (`Đang đánh giá`, `Thực hiện`, `Hủy`, `Đã đánh giá`, `Chờ phê duyệt`, `Hoàn thành`) đều **chỉ 1 thao tác** (Xem) — đúng `:839`, không bị nới quyền sửa ra trạng thái khác.
📷 `image/LKHDG_16-R3-01-hang-PhanCong-da-co-nut-Sua-V109.png`

### Bước 3 — mở [Sửa] đợt *Phân công*, đổi 1 trường, lưu, MỞ LẠI đối chiếu
Khung nhập mở ra: **`Sửa kế hoạch đánh giá`** (kiểu Drawer bên phải, lớp `.ant-drawer-section` — đúng cảnh báo dụng cụ đo ở chuẩn §9), **9 mục**, giá trị cũ nạp sẵn đủ, **không rời màn Danh sách** (đường dẫn giữ *"Trang chủ / Đánh giá hiệu quả / Kế hoạch đánh giá / Danh sách"*, URL không đổi).

| Thời điểm | Trường Ghi chú |
|---|---|
| Trước khi sửa | `QA-LKHDG16-V1-1TEP-20260806` |
| Nhập mới | **`QA-LKHDG16-PC-20260807-0215`** |
| Sau khi bấm **[Lưu nháp]** | bộ đo thông báo: `SO_KHUNG_THONG_BAO = 1` · chữ `"Cập nhật thành công"` · `khoangCachMs = null` ⇒ **không** có dấu hiệu bất thường (`SO_KHUNG > 1` kèm `khoangCachMs < 1ms`) |
| **Đóng khung, MỞ LẠI [Sửa] chính đợt đó** | **`QA-LKHDG16-PC-20260807-0215`** ⇒ **giá trị mới đã lưu thật**, không chốt bằng toast |
| Trạng thái hàng sau khi lưu | vẫn **`Phân công`** (không bị đẩy sang trạng thái khác) |
| Tệp đính kèm sau khi lưu | vẫn **1 tệp** `QA-LKHDG16-ke-hoach.pdf (398 B)` — lưu form không đụng vùng đính kèm thì không mất tệp |

*Bộ đo thông báo cài **TRƯỚC** khi bấm, tự kiểm `soObserverDangSong = 1` (hợp lệ) ở cả 2 lần lưu; **không** lọc trùng; đọc bằng `innerText`.*
📷 `image/LKHDG_16-R3-02-drawer-sua-dot-PhanCong-co-CoQuanDG-va-tep-dinh-kem-V109.png` · `image/LKHDG_16-R3-03-mo-lai-drawer-ghichu-da-luu-dot-PhanCong-V109.png`

### Bước 5 — thành phần form Sửa (yêu cầu có căn cứ đặc tả sau khi BA chốt 06/08)

Bảng 9 mục đọc được trên khung Sửa của **đợt Phân công**, đối chiếu `:847-855`:

| # SRS | Thành phần | Có mặt? | Giá trị đọc được |
|---|---|:-:|---|
| 21 | Tên đợt đánh giá | ✅ | `QA FLOW04 LKHDG_12 seed So bo 6 thang 20260806 - sua v1.0.9` |
| 22 | Mục tiêu | ✅ | có, 111/2000 ký tự |
| 23 | Tần suất | ✅ | `Sơ bộ 6 tháng` |
| 24 | Thời gian bắt đầu / kết thúc | ✅ | `01/01/2026` – `30/06/2026` |
| 25 | Đối tượng | ✅ | `Đào tạo` |
| **25a** (`:852`) | **Cơ quan được đánh giá** | ✅ **CÓ**, đánh dấu bắt buộc `*` | `Bộ Công an` |
| 26 | Ghi chú | ✅ | trường vừa đo ở bước 3 |
| **26a** (`:854`) | **Tài liệu đính kèm** | ✅ **CÓ**, **liệt kê tệp đã có** kèm **[Xem]** và thao tác **gỡ bỏ** | `QA-LKHDG16-ke-hoach.pdf (398 B) · Xem · Xóa` |
| 27 | Thanh hành động | ✅ | `Hủy` · `Lưu nháp` · `Lưu & Chuyển tiêu chí` |

⇒ **Không** có hồi quy gỡ mất 2 mục BA chèn ngày 06/08 ⇒ không phải log bug mới theo chuẩn §11.8.

### Bước 6 — chống hồi quy vế (a)(b)(c) ở trạng thái *Lập kế hoạch* — `DG-20260730-0002` (dạng 2)

| Điểm kiểm | Kết quả |
|---|---|
| (a) trường nhập/đổi được, nạp sẵn giá trị cũ | ✅ 9 mục, các ô văn bản/ngày/danh sách chọn đều thao tác được và đã nạp sẵn (`Cơ quan được đánh giá = Bộ Kế hoạch và Đầu tư`) |
| (a) lưu thật | ✅ đổi Ghi chú → **`QA-LKHDG16-LKH-20260807-0222`**, bấm [Lưu nháp] (1 khung `"Cập nhật thành công"`, `khoangCachMs = null`), **mở lại thấy đúng giá trị mới** |
| (b) không rời ngữ cảnh Sửa | ✅ đường dẫn giữ *"Trang chủ / Đánh giá hiệu quả / Kế hoạch đánh giá / Danh sách"*, URL không đổi, tiêu đề khung ghi rõ *"Sửa kế hoạch đánh giá"* |
| (c) danh sách tệp đính kèm | ✅ liệt kê **2 tệp khác định dạng** `QA-LKHDG16-baocao-mau.docx (1.3 KB)` + `QA-LKHDG16-ke-hoach.pdf (398 B)`, mỗi tệp có **[Xem] [Xóa]** |
| (c) lưu form không đụng vùng đính kèm | ✅ sau lưu mở lại vẫn **đủ 2 tệp**, không mất |

📷 `image/LKHDG_16-R3-04-drawer-sua-dot-LapKeHoach-2tep-khac-dinh-dang-V109.png`

> **Ghi chú trung thực về thao tác của tôi (không phải lỗi ứng dụng):** giữa bước 3 và bước 6 tôi bấm [Sửa] hàng khác trong khi khung Sửa cũ **chưa đóng hẳn** (2 hộp *"Hủy bỏ thay đổi?"* đang chồng lên nhau chặn thao tác), nên có một lượt đọc ra dữ liệu của bản ghi cũ. Đã đóng dứt điểm rồi mở lại và đọc đúng bản ghi — **không** ghi đây thành lỗi ứng dụng.

---

## 5. Đường đo thứ hai (gọi thẳng máy chủ, cùng phiên đăng nhập `cbnv_tw`)

`fetch(url, {credentials:'include'})` chèn trong trang.

| Bước | Kết quả |
|---|---|
| 1. `GET /api/v1/ke-hoach-danh-gias?trangThai=PHAN_CONG&page=1&pageSize=20` | 200 · **1** bản ghi → `DG-20260806-0001`, `id = a7d1b311-0a3e-4cd9-bb6b-fb92437df902` |
| 2. `GET /api/v1/ke-hoach-danh-gias/{id}` | `trangThai = PHAN_CONG` · `ghiChu = QA-LKHDG16-PC-20260807-0215` · **`version = 5`** · `coQuanDuocDanhGiaId = …8001-000000000016` · 1 tệp đính kèm |
| 3. **`PATCH /api/v1/ke-hoach-danh-gias/{id}`** body `{ghiChu:"QA-LKHDG16-PC-API-20260807-0218", version:5}` | 🔼 **HTTP 200** · `success: true` · trả về bản ghi `version: 6`, `trangThai: "PHAN_CONG"` — **KHÔNG có `error.code`, KHÔNG bị từ chối vì lý do trạng thái** |
| 4. `GET` lại | `ghiChu = QA-LKHDG16-PC-API-20260807-0218` · **`version = 6`** (tăng) · `trangThai = PHAN_CONG` (không đổi) |

**So với vòng 06/08:** cùng thao tác trả **409** · `ERR-BIZ-XI-01-02` · *"Không thể cập nhật kế hoạch ở trạng thái 'PHAN_CONG'"*. Nay **200**.

**Đọc kết quả theo quy tắc 2 đường (chuẩn §6):** giao diện **cho vào sửa** và máy chủ **cho lưu** — **cả hai đều thông** ⇒ đủ điều kiện xét PASS. Không rơi vào nhánh "fix nửa vời ở lớp FE" (UI hiện nút mà API vẫn 409) hay "nửa vời ở lớp BE" (API thông mà UI giấu nút). **Không có mâu thuẫn UI vs API.**

---

## 6. Bảng GAP (điều kiện PASS/FAIL không đo được)

| # | Điều kiện trong khối đã khóa | Đo được? | Ghi chú |
|---|---|:-:|---|
| 1 | Đợt "Phân công" vào được chế độ sửa | ✅ | nút Sửa có mặt + khung nhập mở ra thật |
| 2 | Đổi rồi lưu thì mở lại thấy giá trị mới | ✅ | mở lại đối chiếu, không chốt bằng toast |
| 3 | Yêu cầu cập nhật ở bước 4 không bị từ chối vì lý do trạng thái | ✅ | `PATCH` → 200, version 5→6 |

⇒ **BẢNG GAP TRỐNG — 0 mục.** Không rơi vào luật "có GAP ⇒ verdict ô trống".

---

## 7. Độ phủ biến thể

**Trạng thái bắt buộc phải đo (chuẩn §8): `LAP_KE_HOACH` VÀ `PHAN_CONG` — đã đo CẢ HAI.** ✅
Ngoài ra đã đối chiếu cột Hành động của **toàn bộ 20 hàng** phủ 8 giá trị trạng thái hiển thị trên bảng.

**M (dạng dữ liệu) = 2/3 theo định nghĩa chặt:**

| Dạng | Yêu cầu | Kết |
|---|---|:-:|
| 1 | Lập kế hoạch · **đúng 1** tệp | ❌ **không đo** — env chỉ còn **1** đợt ở `Lập kế hoạch` (`DG-20260730-0002`) và nó có **2** tệp. Dựng dạng này đòi tạo mới 1 đợt + tải tệp lên; đã cắt để ưu tiên hoàn tất hồ sơ 2 case trong ngân sách phiên |
| 2 | Lập kế hoạch · ≥2 tệp khác định dạng | ✅ `DG-20260730-0002` |
| 3 | **Phân công · ≥1 tệp** — dạng QUYẾT ĐỊNH | ✅ `DG-20260806-0001` — vòng 06/08 **không đo được chính vì lỗi này**, nay đo được |

🔴 **Thiếu dạng 1 KHÔNG tạo GAP** cho verdict: cả 3 điều kiện của khối PASS/FAIL đã khóa đều đo được đầy đủ (§6), và biến thể *"đúng 1 tệp"* mà dạng 1 nhắm tới **vẫn được phủ** — `DG-20260806-0001` có đúng 1 tệp và vùng đính kèm hiển thị đúng (chỉ khác ở chỗ nó đang ở trạng thái *Phân công* thay vì *Lập kế hoạch*). Vòng 06/08 đạt M = 2/3 nhưng **thiếu đúng dạng 3**; lô này đạt M = 2/3 và **có dạng 3**.

---

## 8. Đối chiếu TỪNG gạch đầu dòng của khối PASS/FAIL đã khóa

> Khối nguồn: `chuan/LKHDG_16.md` §7 (chép từ `bug-report-LKHDG.md:251-254`). Không sửa, không nới.

| Gạch đầu dòng của khối khóa | Số đo | Kết |
|---|---|:-:|
| ✅ *"đợt 'Phân công' vào được chế độ sửa"* | hàng `DG-20260806-0001` có thao tác **Sửa**; bấm vào mở khung `"Sửa kế hoạch đánh giá"` 9 mục | **THOẢ** |
| ✅ *"đổi rồi lưu thì mở lại thấy giá trị mới"* | Ghi chú `QA-LKHDG16-V1-1TEP-20260806` → `QA-LKHDG16-PC-20260807-0215`; **mở lại** đọc đúng giá trị mới | **THOẢ** |
| ✅ *"yêu cầu cập nhật ở bước 4 không bị từ chối vì lý do trạng thái"* | `PATCH` → **200**, `version` 5→6, không có `error.code` | **THOẢ** |
| ❌ *"đợt 'Phân công' không có lối vào sửa"* | có lối vào | **KHÔNG dính** |
| ❌ *"lưu xong mở lại vẫn giá trị cũ"* | mở lại ra giá trị mới | **KHÔNG dính** |
| ❌ *"bước 4 trả 409 kèm thông điệp từ chối theo trạng thái"* | 200, không thông điệp từ chối | **KHÔNG dính** |
| ⚠️ *"Đừng chấm Fail vì CHUỖI breadcrumb khác một mẫu cụ thể"* | tuân thủ — chỉ chấm *"có rời khỏi ngữ cảnh Sửa hay không"*: **không rời** | tuân thủ |
| ⚠️ *"Đừng kết luận 'đã fix' khi chỉ thấy nút [Sửa] xuất hiện trở lại"* | tuân thủ — **đã bấm vào, đổi, lưu, mở lại đối chiếu**, và **đã đo trên CẢ HAI** trạng thái | tuân thủ |
| ⚠️ *"Cảnh báo dụng cụ đo: lớp CSS riêng `.ant-drawer-section`, danh sách tệp KHÔNG dùng `.ant-upload-list-item`"* | tuân thủ — đọc DOM qua `.ant-drawer-section` + `.ant-form-item`, chốt bằng **ảnh chụp** và **đọc lại bản ghi qua máy chủ** | tuân thủ |

**Bẫy chuẩn §9 đã né:** #4 không bê số dòng SRS cũ (tự đếm lại toàn bộ) · #5 không đòi đúng mã lỗi — chấm theo **hành vi** (*có bị từ chối vì lý do trạng thái hay không*) · #6 không kê đơn cách làm · #7 đợt đo **thuộc đúng đơn vị** `…8000-000000000001` của `cbnv_tw` nên việc hiện [Sửa] không thể nhầm với vấn đề quyền · #8 không chạm guard `BR-CALC-08` · #9 được phép đo trên bản ghi cũ vì bản chất là luật chặn theo trạng thái · #10 dùng thân phản hồi làm bằng chứng mạnh hơn ảnh · #11 đã tải lại trang, ghi bó mã FE.

---

## 9. VERDICT

# ✅ **Pass**

**Căn cứ chính (tự mở đếm lại hôm nay):**
- `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-08-danh-gia.md:839` — *"Xem / **Sửa (chỉ LAP_KE_HOACH/PHAN_CONG)** / Xóa (chỉ LAP_KE_HOACH)"*: đợt ở *Phân công* **phải** có lối vào chỉnh sửa. Nay **có**, và *Xóa* vẫn đúng bị bó vào *Lập kế hoạch*.
- `:161` — *"**Given** CB NV chỉnh sửa KH chưa duyệt **When** thay đổi **Then** validate + lưu"*: thay đổi ở đợt chưa duyệt phải lưu được. Nay **lưu được** (giao diện lẫn máy chủ).
- `:852` / `:854` (2 mục BA chốt 06/08): form Sửa **vẫn có đủ** *Cơ quan được đánh giá* (bắt buộc) và *Tài liệu đính kèm* **có liệt kê tệp đã có kèm [Xem] [Xóa]** ⇒ không hồi quy.
- Ba vế đối tác nêu (a) trường không sửa được · (b) rơi sang màn Chi tiết · (c) không hiện danh sách tệp đính kèm: **đều không tái phát** ở cả *Lập kế hoạch* lẫn *Phân công*.

**Verdict hợp lệ theo ràng buộc của lô:** case này **không dùng `reopenba`** — điểm chờ BA đã được BA chốt ngày 06/08 bằng chính 2 dòng `:852` + `:854` (chuẩn §3), và vòng này 2 mục đó **có mặt đầy đủ** nên cũng không phát sinh lỗi mới có căn cứ đặc tả.

**Giới hạn hiệu lực:** đo trên **env dev nội bộ** `18.143.165.120.nip.io` bản **V1.0.9 / `index-DsMHK7Dp.js`**. Đối tác quay bằng chứng trên env nghiệm thu `htpldn-uat.ospgroup.vn` bản V1.0 / V1.0.2 ⇒ **Pass tạm**, chỉ có hiệu lực trên bản dựng env dev cho tới khi bản này lên env đối tác.

---

## 10. Lỗi phát hiện thêm ngoài phạm vi (candidate — KHÔNG dùng làm căn cứ verdict)

1. **Nhãn trạng thái trên danh sách chọn lệch enum `:827`** — danh sách chọn "Trạng thái" có *Đang đánh giá · Đã đánh giá · Lập báo cáo* (không có trong enum đặc tả) và **thiếu mục *Hủy*** dù bảng vẫn hiển thị đợt *Hủy*. Đặc tả im lặng về nhãn ⇒ ghi riêng.
2. **Nút "Bộ lọc nâng cao (2)"** trên thanh lọc không có trong bảng `filter-bar` `:824-829`. Ngoài phạm vi case.
3. **Nhãn nút lưu là *"Lưu nháp"*** trên khung Sửa của đợt **đã ở trạng thái *Phân công*** (không còn là bản nháp). `:855` chỉ đặc tả *"Thanh hành động"* chung, không quy định câu chữ ⇒ **đặc tả im lặng**, ghi candidate, không chấm.
4. **Bản ghi `DG-20260806-0001` đã bị sửa trước phiên đo** (tên kết thúc `"- sua v1.0.9"`, `version` đã là 5). Không ảnh hưởng phép đo nhưng dữ liệu env không còn nguyên trạng so với vòng 06/08.

---

## 11. Ảnh bằng chứng

Tất cả nằm ở `output/UAT_doi-tac/reverify-bug-devfix-2026-08-06/bug-reports/image/` (ngang cấp với `bug-report-LKHDG.md`, link tương đối `image/…` là đúng):

| Ảnh | Tên tệp |
|---|---|
| Cùng một bảng: hàng *Phân công* `DG-20260806-0001` nay **có** thao tác Sửa (2 thao tác, không Xóa) bên cạnh hàng *Lập kế hoạch* `DG-20260730-0002` (3 thao tác) | `LKHDG_16-R3-01-hang-PhanCong-da-co-nut-Sua-V109.png` |
| Khung Sửa của đợt *Phân công*: có *Cơ quan được đánh giá* = Bộ Công an và *Tài liệu đính kèm* liệt kê `QA-LKHDG16-ke-hoach.pdf (398 B)` kèm [Xem] [Xóa] | `LKHDG_16-R3-02-drawer-sua-dot-PhanCong-co-CoQuanDG-va-tep-dinh-kem-V109.png` |
| Mở lại khung Sửa đợt *Phân công* sau khi lưu: Ghi chú = `QA-LKHDG16-PC-20260807-0215` | `LKHDG_16-R3-03-mo-lai-drawer-ghichu-da-luu-dot-PhanCong-V109.png` |
| Khung Sửa đợt *Lập kế hoạch* `DG-20260730-0002`: 2 tệp khác định dạng, mỗi tệp có [Xem] [Xóa] | `LKHDG_16-R3-04-drawer-sua-dot-LapKeHoach-2tep-khac-dinh-dang-V109.png` |
