# GIAI ĐOẠN A — khóa phép thử · `QLHSPLDN_07` (tab `bug`, dòng 292 — "Sửa")

```
Lô:            F9 — tái xác nhận trên env NGHIỆM THU của đối tác
Flow:          flows/03-reverify-sau-dev-fix.md — NHÁNH 2 "Tái xác nhận trên môi trường khác"
Env đích:      https://htpldn-uat.ospgroup.vn  (bó mã đo 12:43 VN 07/08: assets/index-D4NhKEjr.js
               · GET / last-modified Fri, 07 Aug 2026 04:17:55 GMT = 11:17 VN 07/08)
Tài khoản ra verdict: cbnv_tw / Test@1234 (CB_NV_TW, cấp TW) — env này CÓ bước mã xác thực, lấy ở
               https://htpldn-uat.ospgroup.vn/mailhog/. KHÔNG có sibling _01.._05 ⇒ khóa thì DỪNG, mark BLOCKED.
Tài khoản phụ: admin / Secret@123 (QTHT) — CHỈ để đọc màn Nhật ký hệ thống ở vế (c). CẤM ra verdict bằng admin.
Nguồn canonical: tieuchi/QLHSPLDN_07.md §4 §5 §6 + entry BUG-HSPLDN-QLHSPLDN-07 trong bug-report.md
Nguồn SRS:     Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/  — đã MỞ FILE ĐỌC LẠI 07/08
Người viết:    agent CHUẨN-1 · 2026-08-07 · KHÔNG mở trình duyệt
```

> 🔴 **Bản dựng env đích khác hoàn toàn nơi đã Pass** (env nội bộ, bó mã `index-DIABnbIr.js`).
> ⇒ **MỌI vế `MATCH` phải đo lại từ đầu.** 27 ô đo vòng 1, các lượt đo vòng 2 và vòng 06/08 **không chứng
> minh gì** cho lô này.

---

## 0. 🔴 SỐ DÒNG SRS ĐÃ ĐỔI — tieuchi cũ quote SAI, phải dùng cột "Thực tế 07/08"

`srs-fr-12-tv-chuyen-sau.md`, `srs-fr-10-quan-tri.md`, `srs-v3.5.md` được sửa lúc **2026-08-06 22:52:29**,
tức **sau** khi `tieuchi/QLHSPLDN_07.md` được viết và sau vòng đo env nội bộ (06/08 19:05→19:24).
**Nội dung các dòng được trích vẫn nguyên văn — chỉ số dòng dịch** (`srs-fr-12` dịch +13 ở phần FR, +27 ở
phần Entity; `srs-v3.5.md` dịch +40..+44 ở Phụ lục E). Mọi trích dẫn dưới đây là số dòng tôi tự mở file đọc.

| Nội dung | tieuchi ghi | **Thực tế 07/08** |
|---|---|---|
| `### FR-X.1-04: Quản lý hồ sơ pháp lý doanh nghiệp (UC150)` | `srs-fr-12:541` | **`:554`** |
| Mô tả `CRUD … chỉnh sửa …` | `:550` | **`:563`** |
| `**Inputs (Dữ liệu đầu vào) -- Thêm mới / Chỉnh sửa:**` | `:560` | **`:573`** |
| `ten_ho_so` / `loai_ho_so` / `linh_vuc_id` / `ngay_cap` / `ngay_het_han` / `co_quan_cap` / `mo_ta` | `:566`–`:572` | **`:579`–`:585`** |
| `trang_thai … HIEU_LUC / HET_HAN / THU_HOI` | `:573` | **`:586`** |
| `file_dinh_kem … N … PDF/image, max 20MB` | `:574` | **`:587`** |
| Khối `**Chỉnh sửa:**` (bảng 4 bước) | `:607-614` | **`:620-627`** |
| `\| 1 \| Kiểm tra quyền và phạm vi đơn vị \| BR-AUTH-01, BR-AUTH-08 \|` | `:611` | **`:624`** |
| `\| 2 \| Xác nhận dữ liệu cập nhật \| — \|` | `:612` | **`:625`** |
| `\| 3 \| **Cập nhật bản ghi hồ sơ** \| — \|` | `:613` | **`:626`** |
| `\| 4 \| **Ghi nhật ký thao tác** \| BR-DATA-05 \|` | `:614` | **`:627`** |
| Processing **Thêm mới** — bước `Upload file nếu có (max 20MB, quét virus)` | `:604` | **`:617`** |
| Postcondition `Hồ sơ được tạo/cập nhật/xóa mềm trong CSDL` | `:674` | **`:687`** |
| Postcondition `phân quyền dữ liệu theo đơn vị (chỉ xem hồ sơ đơn vị mình)` | `:675` | **`:688`** |
| Postcondition `AUDIT_LOG ghi nhận mọi thao tác CUD` | `:676` | **`:689`** |
| Error Handling 7 mã (`ERR-HSPL-01…06`, `INF-HSPL-01`) | `:682-688` | **`:695-701`** |
| AC `CB NV xem chi tiết hồ sơ … + file đính kèm` | `:693` | **`:706`** |
| AC `CB NV chỉnh sửa hồ sơ … Then cập nhật bản ghi` | `:695` | **`:708`** |
| AC `NHT cập nhật/đính kèm tài liệu … upload file + nhấn Lưu … AUDIT_LOG ghi nguoi_thuc_hien_id` | `:701` | **`:714`** |
| Entity `3.4.3.55 HO_SO_PHAP_LY_DN` (19 trường) | `:1391-1419` | **`:1418-1445`** |
| `created_at` / `updated_at` / `updated_by` / `is_deleted` | `:1413` `:1414` `:1416` `:1417` | **`:1440` `:1441` `:1443` `:1444`** |
| `srs-v3.5.md` — entity rút gọn HO_SO_PHAP_LY_DN + dòng `**Chi tiết xem:**` | `:3592-3614` / `:3597` | **`:3635-3658` / `:3640`** |
| `srs-v3.5.md` — Phụ lục E.I.1 bảng mẫu thông báo | `:6728-6730` | **`:6768-6775`** |

**KHÔNG lệch (đã kiểm từng dòng):** `srs-v3.5.md` `:576` (UI-04) · `:582` (UI-10) ·
`srs-fr-07-doanh-nghiep.md` `:160` `:459` `:461` `:468` `:496` `:508` `:514` `:523` `:819-821` ·
`srs-fr-10-quan-tri.md` `:1365` `:1371` `:1373` `:1387` `:1388` `:1405` `:2381` `:2423`.

> ⚠️ `srs-fr-10:1388` (bộ lọc `hanh_dong`) đã được **bổ sung nội dung** ngày 06/08 — nay có 11 giá trị,
> gắn dấu `` `[đồng bộ 2026-08-06 — đủ 11 giá trị của AUDIT_LOG]` ``. Giá trị **`Sửa`** vẫn còn ⇒ đường đo
> vế (c) không đổi.

---

## 1. Bảng vế × quan hệ SRS

| Vế | Nội dung đối tác đòi (ô phiếu) | SRS hiện tại — `file:dòng` + nguyên văn | Quan hệ | Route |
|---|---|---|---|---|
| **a1** | Cửa sổ chỉnh sửa mở kèm **dữ liệu hiện có** ở các ô | `srs-fr-12-tv-chuyen-sau.md:573` — *"**Inputs (Dữ liệu đầu vào) -- Thêm mới / Chỉnh sửa:**"* (bảng 11 trường `:575-587` áp cho CẢ thao tác Chỉnh sửa) · `:625` — *"\| 2 \| Xác nhận dữ liệu cập nhật \| — \|"* · `:626` — *"\| 3 \| Cập nhật bản ghi hồ sơ \| — \|"* · `:687` — *"- Hồ sơ được tạo/**cập nhật**/xóa mềm trong CSDL"* (thao tác là **cập nhật** trên dữ liệu đang có, không phải tạo lại — form mở trống rồi Lưu sẽ xoá trắng các trường `N`, trái chính `:626`/`:687`) | **MATCH** | TEST |
| **a2** | Mục **Tệp đính kèm** trên cửa sổ Sửa phản ánh đúng tệp bản ghi đang có | `srs-fr-12:587` — *"\| 11 \| file_dinh_kem \| file \| N \| PDF/image, max 20MB \| — \| người dùng upload \|"* nằm trong chính bảng Inputs **"Thêm mới / Chỉnh sửa"** (`:573`) · `:714` — *"**Given** NHT cập nhật/đính kèm tài liệu hồ sơ **When** sửa nội dung + **upload file** + nhấn Lưu **Then** validate, **cập nhật**, **AUDIT_LOG ghi `nguoi_thuc_hien_id = user.id`**…"* (tệp là một phần bề mặt Sửa) · `:654`, `:655` (bề mặt đọc chi tiết phải trả đủ tên/loại/dung lượng tệp) | **MATCH** | TEST |
| **b** | Bấm Lưu → **hệ thống cập nhật bản ghi** *(đối tác đo thấy: báo thành công nhưng KHÔNG lưu)* | `srs-fr-12:626` — *"\| 3 \| **Cập nhật bản ghi hồ sơ** \| — \|"* · `:687` — *"- Hồ sơ được tạo/cập nhật/xóa mềm trong CSDL"* · `:708` — *"- **Given** CB NV chỉnh sửa hồ sơ **When** sửa thông tin + nhấn Lưu **Then** cập nhật bản ghi"* · `:714` (upload file + nhấn Lưu → **cập nhật**) · Về loại thông báo: `srs-v3.5.md:576` — *"\| UI-04 \| Error display \| … **Toast notification cho thao tác thành công** \| UX-Spec Section 4.2 \|"* và `:582` — *"\| UI-10 \| Báo lỗi mất kết nối \| Khi thao tác lưu/gửi thất bại…: dừng trạng thái chờ (spinner), hiển thị thông báo \"Lưu thất bại. Vui lòng kiểm tra kết nối và thử lại.\" kèm nút Thử lại; **KHÔNG nuốt lỗi trong im lặng**. Áp cho mọi module \|"* | **MATCH** | TEST |
| **c** | Bấm Lưu → **lưu vết thao tác** | `srs-fr-12:627` — *"\| 4 \| **Ghi nhật ký thao tác** \| BR-DATA-05 \|"* · `:689` — *"- **AUDIT_LOG ghi nhận mọi thao tác CUD**"* · `:714` (AUDIT_LOG ghi `nguoi_thuc_hien_id`) · `srs-fr-07-doanh-nghiep.md:160` — *"- **BR-DATA-05**: Ghi nhật ký thao tác"*, `:819`/`:821` — *"### BR-DATA-05: Audit trail"* / *"Mọi thao tác CUD + phê duyệt đều ghi vào AUDIT_LOG. Log là immutable."* · Bề mặt đọc: `srs-fr-10-quan-tri.md:1365` — *"### FR-VIII-28: Nhật ký hệ thống (MH-10.10) `[GAP-VIII-02]`"*, `:1371` màn `SCR-VIII-10`, `:1373` — *"Tra cứu, lọc và xuất nhật ký thao tác toàn hệ thống (audit log). **Chỉ QTHT truy cập.** Dữ liệu read-only, không sửa/xóa."*, `:1387` bộ lọc `module` có **`DN`**, `:1388` bộ lọc `hanh_dong` có **`Sửa`**, `:1405` Outputs `thoi_gian, nguoi_dung, module, hanh_dong, chi_tiet, ip_address`, `:2423` BR-DATA-05 | **MATCH** | TEST |

### 1.1 Điều chỉnh so với tieuchi — vế (c) không còn "im lặng về bề mặt đọc"

tieuchi §1 xếp vế (c) là *"đặc tả nói rõ yêu cầu nhưng **im lặng về bề mặt để đọc lại log của 1 bản ghi
HSPL**"*. **Đọc lại SRS 07/08 thì bề mặt đó CÓ**, đủ chi tiết để đo:

- `srs-fr-10-quan-tri.md:1982` — *"| 7 | filter-bar | Entity | text-input | **Ten bang hoac ma ban ghi** |
  change → filter | luon hien thi |"*
- `:1984` — *"| 9 | content | Bang nhat ky | table (read-only) | Cot: Thoi gian (dd/mm/yyyy HH:mm:ss,
  sortable DESC) / Nguoi dung (ho_ten) / Don vi / Module / Entity / **Ma ban ghi** / Loai thao tac…"*
- `:1981` — *"| 6 | filter-bar | Loai thao tac | select | Tao / **Sua** / Xoa / Phe duyet / Tu choi /
  Dang nhap / Dang xuat |"*

⇒ **Đường A là đường chính** của vế (c). Đường B (`updated_at`/`updated_by`) chỉ là đối chứng phụ /
đường dự phòng.

### 1.2 Không có vế `DIFF` / `GAP` nào

Cả 4 vế đều `MATCH`. ⇒ **Không có câu hỏi BA bắt buộc cho case này** — xem §8 cho các điểm chỉ trở thành
candidate nếu tự lộ trong lúc chạy.

---

## 2. Dòng khóa phép đo

```
C1 · Cửa sổ Sửa mở KHÔNG kèm dữ liệu hiện có ở các ô · srs-fr-12:573 (Inputs áp cho Chỉnh sửa) + :625 + :626
   + :687 · MATCH · bấm `Sửa` trên 1 dòng hồ sơ QA · PASS khi: MỌI ô trong bảng Inputs :579-:586 mà bản ghi
   ĐANG CÓ dữ liệu đều được điền sẵn ĐÚNG giá trị hiện có — so từng ô với giá trị đọc lại TỪ MÁY CHỦ của
   chính bản ghi đó (cấm so với trí nhớ, cấm so với dòng trong bảng) · FAIL khi: ≥1 ô có dữ liệu trong bản
   ghi nhưng ô trên form trống hoặc khác giá trị · biến thể bắt buộc: R1 (bản ghi đóng vai "đã có sẵn tệp")
   và R2 (bản ghi mới tạo trong phiên)

C2 · Mục Tệp đính kèm trên form Sửa thiếu/thừa tệp · srs-fr-12:587 + :573 + :714 (+ :654 :655) · MATCH ·
   trong cùng lần mở form ở C1, đếm tệp bằng .ant-upload-list-item-container · PASS khi: ĐÚNG số tệp và
   ĐÚNG tên + dung lượng mà bản ghi đang có · FAIL khi: thiếu tệp / thừa tệp / sai tên · biến thể: R1, R2

C3 · Báo "Cập nhật hồ sơ thành công" nhưng bản ghi KHÔNG được cập nhật · srs-fr-12:626 + :687 + :708 + :714
   + srs-v3.5.md:576 :582 · MATCH · thao tác bằng UI THẬT (bấm nút `Đồng ý` trong cửa sổ Sửa; API/DB chỉ
   đối chứng, KHÔNG thay thao tác) · PASS khi: TỪNG trường vừa sửa (kể cả TỆP VỪA THÊM) mang GIÁ TRỊ MỚI ở
   CẢ HAI đường độc lập — (i) TẢI LẠI TRANG THẬT bỏ đệm rồi mở lại chính bản ghi, (ii) ĐỌC LẠI BẢN GHI THEO
   ID TỪ MÁY CHỦ theo đúng đường request UI phát ra khi bấm Lưu (list_network_requests, CẤM đoán đường dẫn)
   — đối chiếu theo dấu nhận dạng duy nhất QA-W5-0807-<HHmm>-<ten_o>; VÀ số đo thông báo ↔ request khớp
   LOẠI (request lưu thành công ⇒ được phép toast thành công; request thất bại / bản ghi không đổi mà vẫn
   toast thành công ⇒ FAIL theo :582) · FAIL khi: ≥1 trường vừa sửa không mang giá trị mới ở (i) HOẶC (ii);
   hoặc toast thành công trong khi bản ghi không đổi; (i) và (ii) MÂU THUẪN nhau ⇒ CHƯA CHỐT, ghi cả 2 số
   đo, báo điều phối · biến thể bắt buộc: D1 D2 D3 D4 D5 — ĐÚNG MỘT PHẦN CŨNG LÀ FAIL (chỉ cần 1/5 dạng mất
   dữ liệu ⇒ vế FAIL, dù 4 dạng kia lưu đủ)

C4 · Thao tác Sửa không để lại dấu vết nhật ký · srs-fr-12:627 + :689 + :714 + srs-fr-07:819 :821 +
   srs-fr-10:1365 :1371 :1373 :1387 :1388 :1405 :1981 :1982 :1984 :2423 · MATCH · ĐƯỜNG A: đăng nhập QTHT
   (`admin`) → màn Nhật ký hệ thống → lọc `module = DN`, `hanh_dong = Sửa`, khoảng thời gian bao trùm giây
   bấm, `Entity` = mã bản ghi → tìm dòng ứng đúng thao tác vừa làm. Thao tác Sửa VẪN phải do `cbnv_tw` thực
   hiện; đọc log bằng QTHT là ĐỐI CHỨNG, không phải hành động đang tranh chấp · PASS khi: có dòng log đúng
   giây bấm (± sai số hiển thị), `nguoi_dung` = tài khoản đã bấm, cột Entity/Mã bản ghi trỏ đúng hồ sơ HSPL
   · FAIL khi: có màn nhật ký mà thao tác Sửa KHÔNG để lại dòng nào; hoặc `updated_by` không phải người vừa
   thao tác; hoặc `updated_at` không đổi · biến thể bắt buộc: ít nhất 1 lượt trên R1 và 1 lượt trên R2

C4-dự-phòng · ĐƯỜNG B (chỉ dùng khi Đường A KHÔNG khả dụng) · srs-fr-12:1441 (updated_at) + :1443
   (updated_by) · MATCH · đọc lại bản ghi từ máy chủ · PASS-theo-phạm-vi-phiếu khi: `updated_at` = đúng giây
   bấm VÀ `updated_by` = đúng tài khoản đã bấm ⇒ đồng thời MỞ 1 DÒNG CANDIDATE riêng về FR-VIII-28 /
   srs-fr-12:689 và ghi rõ trong verdict là CHƯA CHỨNG MINH ĐƯỢC AUDIT_LOG; KHÔNG kéo verdict case
```

**Cây quyết định vế (c):**

| Tình huống | Chấm |
|---|---|
| Đường A đạt | **vế (c) PASS** — đóng cả yêu cầu SRS lẫn yêu cầu phiếu |
| Đường A **không khả dụng** (`admin` không đăng nhập được / không có menu Nhật ký hệ thống / không có giá trị `module = DN`) **nhưng Đường B đạt** | **PASS theo phạm vi phiếu** + candidate riêng + ghi rõ chưa chứng minh AUDIT_LOG. KHÔNG kéo verdict case |
| Đường A **có màn nhưng không có dòng log** cho thao tác vừa làm, dù Đường B đạt | **KHÔNG Pass vế (c)** — sai lệch trực tiếp với `:627` + `:689` ⇒ **vế còn lỗi** |
| Cả A lẫn B đều không lấy được số đo | vế (c) **CHƯA ĐO ĐƯỢC** ⇒ **không Pass**, ghi rõ thiếu gì |

---

## 3. Tiền đề phải dựng trên env ĐỐI TÁC

### 3.1 Ranh giới cứng — vì sao case này KHÔNG được đo trên bản ghi đối tác

Vế (b) yêu cầu **bấm Lưu** — đây là thao tác **ghi**. ⇒ **Toàn bộ phép đo phải chạy trên bản ghi QA tự tạo.**

- ❌ **CẤM sửa/xoá** `DN-XX-0005` (`1a715c55-bc31-46de-ae07-56dd4f403ce5`), `HSPL-20260803-0001`,
  `HSPL-20260731-0002` — kể cả "chỉ thêm 1 tệp rồi gỡ ra".
- ❌ **CẤM thêm hồ sơ mới vào `DN-XX-0005`.**
- ✅ Bản ghi QA mang dấu nhận dạng `QA-W5-0807-…`.
- ✅ **Bản ghi phải thuộc đơn vị TW của `cbnv_tw`.** Nếu sửa hồ sơ đơn vị khác gặp **403
  `ERR-AUTH-VPD-00-01`** thì đó là chặn theo `BR-AUTH-08` (`srs-fr-12:624`, `srs-fr-10:2381`),
  **KHÔNG phải lỗi lưu dữ liệu** ⇒ đổi bản ghi, tuyệt đối không chấm Fail.

### 3.2 🔴 D5 — "bản ghi CŨ" dựng thế nào trên env đối tác, và giới hạn của cách dựng

tieuchi §5 định nghĩa D5 = *"bản ghi MỚI tạo qua luồng chuẩn sau bản vá **vs** bản ghi CŨ có sẵn từ trước
(ưu tiên bản ghi cũ **đã có sẵn tệp**)"*, mục đích: ① đo trên bản ghi mới sau fix, ② giữ 1 bản ghi cũ để
loại giả thuyết "dữ liệu cũ đóng băng".

Trên env đối tác:

- Bản ghi **thật sự cũ hơn bản vá** chỉ có 2 hồ sơ của đối tác (`HSPL-20260803-0001` tạo 03/08,
  `HSPL-20260731-0002` tạo 31/07) — **cấm đụng**.
- Env này **không có bản ghi QA nào từ trước** (QA chưa làm module này trên env đối tác), và bản dựng đang
  đo mới deploy **11:17 hôm nay** ⇒ **mọi bản ghi QA tạo được đều là "sau bản vá"**.

**Cách dựng hợp lệ (bắt buộc dùng):**

> QA **tự tạo** hồ sơ `R1` kèm **đúng 1 tệp ngay lúc tạo**, bấm `Đồng ý`, **tải lại trang thật**, mở lại và
> xác nhận hồ sơ có đúng 1 tệp. **Từ mốc đó trở đi, `R1` được coi là "bản ghi đã có sẵn tệp TRƯỚC thao tác"**
> — đúng tiền đề N2 của đối tác (*"Hồ sơ ĐÃ CÓ SẴN 1 tệp trước thao tác"*), vì lượt thêm tệp thứ hai là một
> giao dịch Lưu **tách rời** khỏi giao dịch tạo.

**Giới hạn phải khai nguyên văn vào báo cáo + ô `Kết quả verify`:**

> Cách này phủ được chiều *"bản ghi đã có sẵn tệp trước thao tác"* — **chiều quyết định** của kịch bản đối
> tác. Nó **KHÔNG** phủ được chiều *"bản ghi tồn tại từ trước bản vá"*, vì trên môi trường nghiệm thu không
> có bản ghi QA nào cũ hơn bản dựng đang đo, và hai hồ sơ cũ thật là dữ liệu của đối tác nên không được
> thao tác lên. ⇒ Giả thuyết *"dữ liệu tạo trước bản vá bị đóng băng"* **chưa được loại trừ trên env này**.
> Ghi vào mục `⏸ CHƯA KIỂM TRA`, **không** vì thế mà hạ verdict xuống Chưa chốt (chiều quyết định đã phủ).

### 3.3 Danh sách tiền đề + thứ tự dựng

> **Chạy sau khi đã hoàn tất `QLHSPLDN_06`.** Dùng lại **DN QA** đã chốt ở `chuan/QLHSPLDN_06.md` §3.2 (T1/T1b).
> **Tạo hồ sơ RIÊNG cho case này** — không tái dùng `QA-W5-0807-HS-A/B/C` (lượt 2 sẽ ghi đè 8 ô, phá tiền đề
> D1/D4 của `_06`).

| # | Việc | Cách làm bằng UI | Kết quả cần có |
|---|---|---|---|
| **U0** | Ghi vân tay bản dựng (đầu case) + đăng nhập `cbnv_tw` | Tải lại trang bỏ đệm → đọc `assets/index-*.js` + `GET /` `last-modified` + `etag` | Vân tay đầu |
| **U1** | Chuẩn bị **5 tệp** seed | Đặt vào `F9-uatdoitac-QLHSPLDN-2026-08-07/seed-files/`: `QA-W5-0807-tep-07-r1a.png` · `-r1b.png` · `-r1c.png` · `-r2a.png` · `-r2b.png` (PNG thật, vài chục byte). Có thể sao chép từ `reverify-week-5/seed-files/QA-W5-1907-tep-luot*.png` rồi đổi tên | 5 tệp phân biệt được bằng tên |
| **U2** | Tạo **R1** — bản ghi đóng vai *"đã có sẵn tệp trước thao tác"* | DN QA → thẻ **Hồ sơ pháp lý** → **[Thêm hồ sơ]** → Tên `QA-W5-0807-HS-CU` · Loại **`Khác`** · Lĩnh vực **`Thuế`** · Ngày cấp `03/08/2026` · Ngày hết hạn `03/08/2026` · Cơ quan cấp `QA-W5-0807 coquan goc` · Mô tả `QA-W5-0807 mo ta goc` · Trạng thái **`Hiệu lực`** *(khớp tiền đề N2 của đối tác: `KHAC` + `Thuế` + `HIEU_LUC`)* → đính kèm **đúng 1 tệp** `…-r1a.png` → **`Đồng ý`** | 1 hồ sơ, **1 tệp** |
| **U3** | **Chốt tiền đề R1** | **Tải lại trang thật** → mở lại form Sửa của `QA-W5-0807-HS-CU` → xác nhận **đúng 1 tệp** + 9 ô đúng giá trị vừa nhập → **đóng form, KHÔNG bấm Đồng ý** | R1 đứng vững; ghi mã + id |
| **U4** | **Lượt 1 = D1 trên R1** ← **lượt quyết định** | Mở form Sửa R1 → **CHỈ thêm đúng 1 tệp** `…-r1b.png`, **không đụng ô nào khác** → `Đồng ý`. *(Bản sao chính xác thao tác đối tác ở mốc 00:00→00:13 của video.)* | Đo theo C3 |
| **U5** | **Lượt 2 = D2+D3+D4 trên R1**, **1 lần bấm** | Mở form Sửa R1 → đổi **8 ô** trong cùng một lần: Tên `QA-W5-0807-<HHmm>-ten` · Cơ quan cấp `QA-W5-0807-<HHmm>-coquan` · Mô tả `QA-W5-0807-<HHmm>-mota` *(D2)* · Ngày cấp + Ngày hết hạn sang giá trị khác *(D3)* · Loại hồ sơ + Lĩnh vực + Trạng thái sang giá trị khác *(D4)* → thêm 1 tệp `…-r1c.png` → `Đồng ý` | Đo theo C3 |
| **U6** | Tạo **R2** — bản ghi MỚI *(D5)* | [Thêm hồ sơ] → Tên `QA-W5-0807-HS-MOI` · Loại `Khác` · Trạng thái `Hiệu lực` → đính kèm đúng 1 tệp `…-r2a.png` → `Đồng ý` → **tải lại trang**, xác nhận 1 tệp | R2 có 1 tệp |
| **U7** | **Lượt 3a = D1 trên R2** | Mở form Sửa R2 → chỉ thêm 1 tệp `…-r2b.png`, không đụng ô nào → `Đồng ý` | Đo theo C3 |
| **U8** | **Lượt 3b = D2+D3+D4 trên R2** | Như U5, giá trị mang dấu `QA-W5-0807-<HHmm>-…` | Đo theo C3 |
| **U9** | **Vế (c) — Đường A** | Đăng xuất → đăng nhập `admin` / `Secret@123` → **Quản trị hệ thống → Nhật ký hệ thống** → lọc `Từ ngày–Đến ngày` bao trùm phiên · `Module = DN` · `Loại thao tác = Sửa` · `Entity` = mã/ID bản ghi → đọc bảng | Đủ dòng cho **mọi** lượt bấm ở U4/U5/U7/U8 |
| **U10** | Ghi vân tay bản dựng (cuối case) | Đọc lại `assets/index-*.js` + `last-modified` + `etag` | Hai đầu khác nhau ⇒ khai rõ + đo lại từ lượt 1 |
| **U11** | Khai vào báo cáo | DN QA · `QA-W5-0807-HS-CU` + `QA-W5-0807-HS-MOI` (mã + id) · từng lượt đổi gì · giờ bấm từng lượt · env `htpldn-uat.ospgroup.vn` | **Bản ghi không khai = coi như chưa đo** |

> ⏱ **Ghi mốc giờ (đến giây) của TỪNG lần bấm `Đồng ý`** — đây là khoá đối chiếu duy nhất cho vế (c) ở U9.
> 🔑 **Phiên đăng nhập:** token idle 30 phút; U9 phải đổi tài khoản ⇒ làm U9 **sau cùng**, sau khi đã thu đủ
> số đo của U4–U8 bằng `cbnv_tw`.

---

## 4. Điều kiện PASS bắt buộc / FAIL

### ✅ PASS vế (a) — khi ĐỦ cả 2 *(C1 + C2)*

1. Mọi ô SRS liệt kê ở `srs-fr-12:579-586` **có dữ liệu trong bản ghi** đều được điền sẵn **đúng giá trị
   hiện có** — so **từng ô** với giá trị đọc lại **từ máy chủ** của chính bản ghi đó. Không so với trí nhớ,
   không so với dòng trong bảng danh sách.
2. Mục **Tệp đính kèm** liệt kê **đúng số tệp + đúng tên + đúng dung lượng** bản ghi đang có.

**❌ FAIL vế (a):** ≥1 ô có dữ liệu trong bản ghi nhưng ô trên form trống/khác giá trị, **hoặc** danh sách
tệp thiếu/thừa so với bản ghi.

### ✅ PASS vế (b) — khi ĐỦ cả 5 *(C3)*

1. **Thao tác bằng UI thật** (bấm `Đồng ý` trong cửa sổ Sửa). API/DB chỉ đối chứng, **không** thay thao tác.
   Cấm Pass bằng quan sát tĩnh kiểu *"thấy giá trị vẫn còn trên form"*.
2. **Đo bằng đường thứ hai sau khi bấm Lưu — bắt buộc CẢ 2 đường độc lập và CẢ 2 phải khớp:**
   (i) **tải lại trang thật** (bỏ đệm) → mở lại chính bản ghi → so **từng trường vừa sửa**;
   (ii) **đọc lại bản ghi theo id từ máy chủ** → so **từng trường vừa sửa**, gồm **danh sách tệp (tên +
   dung lượng)**. Đường gọi máy chủ **lấy từ chính request UI phát ra khi bấm Lưu** (`list_network_requests`)
   — **CẤM tự đoán đường dẫn API**.
3. **Từng trường vừa sửa mang GIÁ TRỊ MỚI ở cả (i) và (ii)**, đối chiếu theo dấu nhận dạng duy nhất
   `QA-W5-0807-<HHmm>-<ten_o>` — không dùng giá trị dễ trùng.
4. **Số đo thông báo ↔ request khớp LOẠI:** request lưu **thành công** ⇒ được phép toast thành công
   (`srs-v3.5.md:576`); request lưu **thất bại / bản ghi không đổi** mà vẫn toast **thành công** ⇒ **FAIL**
   (`:582` — *"KHÔNG nuốt lỗi trong im lặng"*).
5. **Phủ đủ M = 5 dạng** ở §5, mỗi dạng qua đủ bước 1–4.

**❌ FAIL vế (b):** ≥1 trường vừa sửa (kể cả **tệp vừa thêm**) **không** mang giá trị mới ở (i) **hoặc** (ii);
**hoặc** toast thành công trong khi bản ghi không đổi. **(i) và (ii) mâu thuẫn nhau ⇒ CHƯA CHỐT** — ghi cả
hai số đo, báo điều phối, **không tự chọn bên nào đúng**.
🔴 **Đúng một phần cũng là FAIL:** chỉ cần **1 trong 5 dạng** mất dữ liệu ⇒ vế (b) FAIL, dù 4 dạng kia lưu đủ.

### ✅ PASS vế (c) — theo cây quyết định ở §2

**❌ FAIL vế (c):** bản ghi được cập nhật nhưng `updated_by` **không phải** người vừa thao tác, **hoặc**
`updated_at` không đổi, **hoặc** có màn nhật ký mà thao tác Sửa không để lại dòng log nào.

### Chốt verdict cả case

**Pass** khi (a) + (b) + (c) đều đạt **và** đã chạy hết D1–D5 · **Reopen** khi ≥1 vế `MATCH` FAIL đủ 4 điều
kiện Flow 03 (dừng ngay, không chạy nốt biến thể) · **Chưa chốt** khi hai đường (i)/(ii) mâu thuẫn, hoặc
thiếu biến thể quyết định.
🔴 **Không có ảnh "lỗi cũ" do chính mình chụp trên env này trước bản vá** ⇒ chỉ được kết luận **hiện trạng
đúng/sai so với đặc tả**; **CẤM viết** *"fix đã có tác dụng"* — dùng `✅ HIỆN TẠI ĐẠT`, không dùng
`✅ ĐÃ HẾT LỖI`, trừ khi có bằng chứng trạng thái lỗi trước đó **trên chính env + bản dựng này**.

---

## 5. Biến thể bắt buộc — **M = 5**

| # | Dạng | Căn cứ (SRS 07/08) | Vế cần | Bắt buộc? |
|---|---|---|---|---|
| **D1** | **CHỈ thêm 1 tệp** vào hồ sơ **đã có sẵn ≥1 tệp**, **không đụng ô nào khác**, rồi bấm `Đồng ý` | **Bản sao chính xác thao tác đối tác** (video 00:00 → 00:13). Đường lưu tệp khi *không có ô nào bẩn* có thể khác đường lưu khi *có ô bẩn* — **cả 2 vòng QA trước đều KHÔNG đo dạng này** | b · c | ✅ **BẮT BUỘC** — U4 (R1) **và** U7 (R2) |
| **D2** | Ô **chữ** + **chữ dài**: `ten_ho_so` (`:579`), `co_quan_cap` (`:584`), `mo_ta` (`:585`) | 3 trường text, `mo_ta` là `text (long)` — kiểu lưu khác | b | ✅ **BẮT BUỘC** — U5, U8 |
| **D3** | Ô **ngày**: `ngay_cap` (`:582`), `ngay_het_han` (`:583`) | Kiểu `date` — hay hỏng riêng do định dạng/múi giờ; đối tác **không** đụng nên video không loại trừ được | b | ✅ **BẮT BUỘC** — U5, U8 |
| **D4** | Ô **chọn**: `loai_ho_so` 5 giá trị (`:580`), `linh_vuc_id` FK → DANH_MUC (`:581`), `trang_thai` 3 giá trị (`:586`) | Enum + khóa ngoại — đường ghi khác text; `srs-fr-07:468` khai đủ 5 loại × 3 trạng thái | b | ✅ **BẮT BUỘC** — U5, U8 |
| **D5** | Bản ghi **MỚI tạo qua luồng chuẩn** (R2) **vs** bản ghi **đã có sẵn tệp trước thao tác** (R1) | Flow 03 §Chuẩn bị 5: *bug về trường lưu trong CSDL phải đo trên bản ghi mới sau fix*; đồng thời giữ 1 bản ghi "có sẵn tệp" để khớp tiền đề N2 | b · c | ⚠️ **BẮT BUỘC MỘT NỬA** — chiều *"mới sau bản vá"* ✅ dựng được (R2); chiều *"cũ hơn bản vá"* ❌ **MIỄN** vì trên env nghiệm thu không có bản ghi QA cũ hơn bản dựng, và bản ghi cũ thật là dữ liệu đối tác. **Khai nguyên văn giới hạn ở §3.2 vào báo cáo.** |

**Ghép lượt (mỗi lượt = 1 lần bấm `Đồng ý`):** U4 = D1/R1 *(quyết định)* · U5 = D2+D3+D4/R1 ·
U7 = D1/R2 · U8 = D2+D3+D4/R2. ⇒ **4 lượt bấm Lưu**, phủ đủ D1–D5.

**Thiếu bất kỳ dạng D1–D4 nào, hoặc chỉ đo 1 đường thay vì 2 ⇒ Chưa chốt**, không Pass.

---

## 6. Chống chấm oan

### ⚠️ KHÔNG được chấm **Fail** vì *(candidate riêng, KHÔNG kéo verdict case)*

- **Nhãn nút là `Đồng ý` thay vì `Lưu`.** ⚠️ **Căn cứ đã mạnh hơn so với tieuchi:** ngoài `srs-fr-07:496`
  (*"| 30 | action-bar | Lưu | button | … |"*), nay có quy ước hệ thống `srs-v3.5.md:6756` — *"**H4** | Nhãn
  nút thống nhất | … Nút lưu luôn **'Lưu'** (không 'Lưu lại', 'Cập nhật', 'Hoàn tất'…) | BẮT BUỘC"*. Vẫn
  **không phải vế đối tác nêu** ⇒ **candidate riêng**, không kéo verdict.
- **Chữ của thông báo thành công** (*"Cập nhật hồ sơ thành công"*) — SRS im lặng về nội dung chữ cho thao tác
  Sửa hồ sơ. `srs-v3.5.md:576` chỉ đòi **có** toast; bảng mẫu Phụ lục E.I.1 (`:6768-6775`) chỉ phủ 4 tình
  huống công khai / hủy công khai / sai phạm vi đơn vị / khóa lạc quan. **Chỉ FAIL khi sai LOẠI** (báo thành
  công lúc không lưu được), **không** FAIL vì chọn chữ nào.
- **`version` không tăng / không có trường `version`.** Entity `HO_SO_PHAP_LY_DN` **không có cột này** ở cả
  hai bản (`srs-fr-12:1418-1445` — 19 trường, `srs-v3.5.md:3635-3658`). Khóa lạc quan `version` chỉ đặc tả
  cho HOI_DAP. ⇒ `version 1→2` mà các vòng trước dùng là **chi tiết cài đặt**, chỉ làm đối chứng phụ,
  **không** làm tiêu chí Pass.
- **Tên tệp đính kèm không theo khuôn `{TenTep}_{YYYYMMDD_HHmm}`.** `srs-v3.5.md:6760` (H8) ghi rõ
  *"**Không áp** cho tệp mẫu nhập liệu tải sẵn…, **tệp người dùng tải lên và tệp đính kèm** — các loại này
  giữ tên gốc"* ⇒ **cấm Fail** ở chiều này.
- **403 `ERR-AUTH-VPD-00-01` khi sửa hồ sơ của đơn vị khác** — đúng `BR-AUTH-08` (`srs-fr-12:624`,
  `srs-fr-10:2381`); đổi bản ghi rồi đo lại.
- **Nút `Sửa` vẫn hiện trên dòng hồ sơ của đơn vị khác** — vướng mâu thuẫn `srs-fr-12:688` (*"phân quyền dữ
  liệu theo đơn vị (chỉ xem hồ sơ đơn vị mình)"*) vs `srs-fr-10:2381` (BR-AUTH-08 áp mọi bảng có `don_vi_id`;
  TW thấy toàn quốc). **Candidate cho BA**, không kéo verdict.
- **Hành vi khi GỠ tệp lúc Sửa** — SRS **im lặng hoàn toàn** (không dòng nào nói gỡ tệp lúc chỉnh sửa).
  Ghi nhận + candidate, **không** kéo verdict. **Và không được chủ động thử gỡ tệp** — ngoài phạm vi đo.
- **Số hồ sơ / dữ liệu trên env đối tác khác env nội bộ** — lệch env là bối cảnh, không phải lỗi.
- **Khối `Processing — Chỉnh sửa` (`:620-627`) không có bước "Upload file"** như khối Thêm mới (`:617`).
  Đây **không** phải im lặng ở mức yêu cầu: bảng Inputs `:573` áp cho **"Thêm mới / Chỉnh sửa"** và có
  `file_dinh_kem` (`:587`), còn AC `:714` nói thẳng *"upload file + nhấn Lưu → validate, cập nhật"* ⇒ **đủ
  căn cứ chấm vế (b) cho tệp**; không được lấy việc thiếu bước đó làm lý do miễn vế (b).

### 🚫 KHÔNG được chấm **Pass** vì *(case này là bug "báo thành công nhưng KHÔNG lưu")*

- ❌ Thấy **thông báo "Cập nhật hồ sơ thành công"** → đây chính là thứ đã nói dối trong video đối tác.
- ❌ Thấy **giá trị vẫn còn trên form ngay sau khi lưu** (form chưa đóng, hoặc mở lại form mà **không** tải
  lại trang) → đúng đường đo yếu của đối tác, có thể trúng trạng thái trong bộ nhớ trình duyệt.
- ❌ Thấy **dòng trong bảng danh sách đổi** mà chưa tải lại trang → cùng nguồn dữ liệu trong bộ nhớ.
- ❌ Chỉ đo **một** trong hai đường (i)/(ii) — **bấm lại cùng một nút không tính là đường thứ hai**.
- ❌ Kết luận 100% từ script chạy trong trang mà **không có ảnh mở ra đọc**.
- ❌ **Bỏ lượt D1** (chỉ đo kịch bản "sửa nhiều ô + thêm tệp" như 2 vòng trước) — đây chính là chênh lệch
  kịch bản đã bị bỏ sót 2 vòng liền; D1 là **lượt quyết định**.
- ❌ Chỉ đo trên **1 bản ghi** (bỏ R2, hoặc bỏ R1).
- ❌ Suy từ số đo env nội bộ 06/08 (bó mã `index-DIABnbIr.js`) sang bản dựng `index-D4NhKEjr.js`.
- ❌ Đóng vế (c) bằng `updated_at`/`updated_by` **trong khi màn Nhật ký hệ thống MỞ ĐƯỢC** — Đường B chỉ dùng
  khi Đường A **không khả dụng**.

---

## 7. Cảnh báo dụng cụ — đọc TRƯỚC khi bấm

*(chép từ `tieuchi/QLHSPLDN_07.md` §4 Precondition — 3 lần "phép đo nói dối" đã ghi nhận ở vòng trước)*

1. **Đếm tệp** phải dùng `.ant-upload-list-item-container` — **KHÔNG** `.ant-upload-list-item`.
   *(Sai class này đã làm hỏng số đo vòng 1.)*
2. **Đọc ô chọn** phải dùng `.ant-select-content` — **KHÔNG** `.ant-select-selection-item`.
   *(Sai class này đã làm hỏng số đo vòng 1.)*
3. **Điền ô** phải **đặt giá trị qua setter gốc + phát `input`/`change`**. `fill_form` / `Control+A`
   **NỐI CHUỖI** thay vì thay thế ⇒ **bắt buộc clear field trước**. *(Sai ở vòng 1 — giá trị đo được là
   chuỗi cũ + chuỗi mới dính nhau.)*
4. **Bộ đếm request** phải bọc **cả `fetch` LẪN `XMLHttpRequest`** — vòng 2 báo `SO_REQUEST = 0` ở lượt sửa
   bản ghi cũ **chỉ vì quên bọc XHR**. Không có số này thì điều kiện PASS b4 không đo được.
5. **Bộ bắt thông báo:** dùng `tools/toast-capture.js`, cài **TRƯỚC** khi bấm, tự kiểm
   **`soObserverDangSong = 1`** trước **mỗi** lượt; observer bị xoá sau mỗi lần tải lại trang → **cài lại +
   kiểm lại**. **CẤM dedupe** (che double-toast → Pass oan). Đọc `innerText`, **CẤM `textContent`**.
   Đếm thông báo theo **mốc giờ khác nhau**, không theo số phần tử.
6. Đường gọi máy chủ để đối chứng **lấy từ chính request UI phát ra** (`list_network_requests`) —
   **CẤM đoán đường dẫn API, CẤM ghi thẳng CSDL**.
7. Nút submit form là **`Đồng ý`**. Row action `Sửa`/`Xoá` là thẻ `<a>`.
8. **Tải lại trang** trước lô đo và sau mỗi lượt cần đường (i) — tab mở lâu vẫn chạy bó mã cũ (đã có tiền lệ
   Reopen oan). Sau mỗi lần tải lại phải **cài lại observer**.
9. Ảnh lưu vào `F9-uatdoitac-QLHSPLDN-2026-08-07/image/`.

---

## 8. Câu hỏi BA

**Không có vế `DIFF`/`GAP` ⇒ case này KHÔNG có câu hỏi BA bắt buộc.**

Chỉ mở candidate + câu hỏi nếu hiện tượng tương ứng **tự lộ** trong luồng bắt buộc (Flow 03 §Bug mới tự lộ —
tối đa **1 phép xác nhận** cho cả case, giữ nguyên role/dữ liệu/bộ lọc, **không** replay thao tác ghi):

1. **Nếu thấy nút `Sửa` hiện trên dòng hồ sơ thuộc đơn vị khác:**
   > `srs-fr-12-tv-chuyen-sau.md:688` ghi *"phân quyền dữ liệu theo đơn vị (chỉ xem hồ sơ đơn vị mình)"*,
   > còn `srs-fr-10-quan-tri.md:2381` (BR-AUTH-08) áp cho **mọi bảng có cột `don_vi_id`** và cấp TW thấy
   > toàn quốc. Với hồ sơ pháp lý DN, cán bộ nghiệp vụ **cấp TW** được **xem** hồ sơ của mọi đơn vị hay chỉ
   > đơn vị mình? Và nếu chỉ được xem, nút **Sửa** có phải ẩn đi trên dòng của đơn vị khác không, hay cứ để
   > hiện rồi chặn bằng lỗi 403 khi bấm?

2. **Nếu thấy hành vi lạ khi gỡ tệp trong lúc Sửa** *(chỉ khi tự lộ — cấm chủ động thử)*:
   > SRS v3.5 không có dòng nào quy định hành vi **gỡ tệp đính kèm** khi chỉnh sửa hồ sơ pháp lý DN
   > (khối `Processing — Chỉnh sửa` `srs-fr-12:620-627` không có bước tương ứng với bước upload `:617` của
   > Thêm mới). Khi người dùng gỡ một tệp khỏi hồ sơ rồi bấm Lưu, hệ thống phải xử lý thế nào — xoá hẳn,
   > xoá mềm, hay không cho gỡ?
