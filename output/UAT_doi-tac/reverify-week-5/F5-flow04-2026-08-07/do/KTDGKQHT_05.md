# HỒ SƠ ĐO — KTDGKQHT_05 · "Tải lên tệp Excel điểm danh"

> **FLOW 04 · GIAI ĐOẠN B.** Chuẩn chấm khoá tại [`chuan/KTDGKQHT_05.md`](../chuan/KTDGKQHT_05.md) — quan hệ `MATCH/DIFF/GAP` **không đổi** trong lượt đo này.

---

## 1. Vân tay bản dựng thực đo 🔴 KHÁC KỲ VỌNG

| Hạng mục | Kỳ vọng (TIEN-DO.md) | **Thực đo 2026-08-07 ~02:08–02:20 giờ VN** | Khớp? |
|---|---|---|---|
| `GET /` last-modified | `Thu, 06 Aug 2026 17:39:54 GMT` | **`Thu, 06 Aug 2026 18:51:25 GMT`** | ❌ mới hơn ~1h12 |
| `GET /` etag | `W/"6a74c6ea-428"` | **`W/"6a74d7ad-428"`** | ❌ |
| Bó mã FE | `assets/index-B2W2Krcs.js` | **`assets/index-DsMHK7Dp.js`** | ❌ |
| Chuỗi phiên bản chân sidebar | `V1.0.10` | **`HTPLDN · V1.0.9`** | ❌ |
| Máy chủ | `nginx/1.27.5` sau `Caddy` | `nginx/1.27.5` sau `Caddy` | ✅ |

⇒ **Đã có deploy khác sau bản V1.0.10 mà lô này lấy làm mốc; chuỗi phiên bản công bố lại là V1.0.9.**
Đã báo điều phối. Verdict dưới đây **chỉ có hiệu lực cho bản dựng `index-DsMHK7Dp.js` / `V1.0.9` đo lúc 2026-08-07 02:08–02:20 giờ VN**.

**Env:** `https://18.143.165.120.nip.io` (env nội bộ) · API `https://18.143.165.120.nip.io/api/v1`

---

## 2. Tài khoản thực dùng

| Hạng mục | Giá trị |
|---|---|
| **Tài khoản** | **`cbnv_tw_02`** / `Test@1234` — đăng nhập lần đầu thành công, **không phải fallback** |
| Vai trò hệ thống trả về | `CB_NV_TW` — "CB Nghiệp vụ - Trung ương #02" · đơn vị `BTP · TW` (`donViId 00000000-0000-4000-8000-000000000001`, `capDonVi TW`) |
| Mã xác thực | MailHog `cbnv_tw_02@htpldn.test` · `279055` (19:08:42 UTC) |
| Tài khoản quản trị | **KHÔNG dùng** — không dùng `admin` cho bất kỳ bước nào (kể cả chuẩn bị dữ liệu) |

Khớp vai trò trong bằng chứng đối tác (`CB_NV_TW`, `BTP · TW`).

---

## 3. Tiền đề đã chuẩn bị

| # | Tiền đề | Trạng thái | Bằng chứng |
|---|---|---|---|
| **T1** | Khóa học ở `DANG_DIEN_RA` | ✅ | Khóa **`KH-QAW7-HOINGHI`** — `khoa_hoc_id = a7480002-0000-4000-8000-000000000002` — "QAW7 — Hội nghị đối thoại DN 2026". Thanh bước: bước 4 "Đang diễn ra" mang lớp `ant-steps-item-process ant-steps-item-active` |
| **T2** | Khóa có ≥1 buổi học + đã chọn buổi | ✅ | Tab Lịch học đọc được **4 buổi**. Buổi đo: **Buổi 4 — 11/05/2026 · 14:00:00–16:00:00 — "Buổi 4 - QA seed KTDGKQHT_23"** · `lich_hoc_id = bd1cdf35-8ab7-41f6-ae85-d21fdec2c8c2` |
| **T3** | ≥4 học viên **thuộc** khóa | ✅ *(sau seed — xem §7)* | 4 học viên trạng thái `Đã duyệt`: `dbf62f06…b660` QA R3 Mailto Ba · `cd17f1b7…3458b` QA R3 Mailto Hai · `6feead91…27f53` QA R3 Mailto Mot · `56640d49…01162` Nguyễn Văn A |
| **T4** | 1 `hoc_vien_id` của khóa **KHÁC** | ✅ | `cccccccc-0000-4000-8000-000000000001` — "Nguyễn Văn Học Viên", thuộc khóa `DDD-KH-011` (`dddddddd-…-011`), trạng thái `DA_DUYET`. Đọc qua endpoint danh sách **đã lộ trên màn** `GET /api/v1/khoa-hocs/{id}/dang-ky-dao-taos` (không đoán đường dẫn) |
| **T5** | Quyền + phạm vi đơn vị | ✅ | Khóa nằm trong phạm vi `cbnv_tw_02`; mọi endpoint trả 200, không gặp 403 |
| **T6** | Vân tay bản dựng | ⚠️ lệch | §1 |

**Mốc gốc trước khi nạp (baseline):** `GET /api/v1/khoa-hocs/a7480002…0002/diem-danhs?lichHocId=bd1cdf35…c2c8c2` → 4 học viên, **cả 4 đều `trangThai = null`, `id = ""`** ⇒ buổi 4 **chưa có bản ghi điểm danh nào**.

### Tệp fixture

| Tệp | Vai trò |
|---|---|
| [`seed-files/mau-goc-KTDGKQHT_05.xlsx`](../seed-files/mau-goc-KTDGKQHT_05.xlsx) | **Tệp mẫu do chính hệ thống sinh** (bản sao nguyên trạng của tệp tải về từ nút "Tải mẫu điểm danh") |
| [`seed-files/fixture-KTDGKQHT_05-3hople-2loi.xlsx`](../seed-files/fixture-KTDGKQHT_05-3hople-2loi.xlsx) | Fixture nạp — **dựng bằng `openpyxl` TỪ chính tệp mẫu trên**, giữ nguyên sheet metadata, chỉ điền cột "Trạng thái điểm danh" + thêm 2 dòng lỗi. Không phải chuỗi chữ đổi đuôi (`file` xác nhận: *Microsoft Excel 2007+*) |

**Nội dung fixture — 5 dòng dữ liệu (3 hợp lệ / 2 lỗi):**

| Dòng Excel | `hoc_vien_id` | Họ tên | Trạng thái điểm danh | Kỳ vọng |
|---:|---|---|---|---|
| 2 | `dbf62f06…b660` | QA R3 Mailto Ba | `Có mặt` | hợp lệ |
| 3 | `cd17f1b7…3458b` | QA R3 Mailto Hai | `Vắng có phép` | hợp lệ |
| 4 | `6feead91…27f53` | QA R3 Mailto Mot | `Vắng không phép` | hợp lệ |
| 5 | `cccccccc…0001` | Nguyễn Văn Học Viên *(khóa khác)* | `Có mặt` | **lỗi — ERR-KQ-03** (`:592`, `:637`) |
| 6 | `56640d49…01162` | Nguyễn Văn A | `XYZ` | **lỗi — ERR-KQ-04** (`:638`) |

Sheet `_HTPLDN_META` giữ nguyên: `template_type=DIEM_DANH` · `khoa_hoc_id=a7480002…0002` · `lich_hoc_id=bd1cdf35…c2c8c2`.

---

## 4. Vế C3 — cơ chế tệp mẫu *(đo trước, vì tệp mẫu là đầu vào của C1/C2)*

**Quan hệ đã khoá:** `MATCH` · route `TEST` · SRS `srs-fr-03-dao-tao.md:571–583`, `:590`, `:651`, `:1919`

### Thao tác (UI thật)

Đăng nhập → sidebar "Khóa học" → mở `KH-QAW7-HOINGHI` → tab **Điểm danh** → chọn **Buổi 4** → bấm nút **"Tải mẫu điểm danh"** (bấm bằng `click` trên phần tử thật, `uid=5_28`).

### Số đo

| # | Chuẩn chấm (§4 chuan) | Số đo thực | Đạt |
|---|---|---|---|
| (a) | Nút có mặt + bật đúng điều kiện `:577` | Nút **"Tải mẫu điểm danh"** có trên Tab Điểm danh. **Chưa chọn buổi → `disabled: true`**; **đã chọn buổi (khóa `DANG_DIEN_RA`, khóa có 4 buổi, có quyền) → `disabled: false`** | ✅ |
| (b) | Bộ cột khớp 6 cột `:581` | Hàng tiêu đề đọc bằng `openpyxl`: `hoc_vien_id · Họ tên · Email · Đơn vị · Trạng thái điểm danh · Ghi chú` — **đúng 6 cột, đúng thứ tự** | ✅ |
| (c) | Số ô `hoc_vien_id` điền sẵn = số học viên của khóa | **4/4** dòng có UUID điền sẵn, khớp đúng 4 học viên `Đã duyệt` của khóa | ✅ |
| (d) | Cột "Trạng thái điểm danh" rỗng 100% | **4/4 ô rỗng** (`''`) | ✅ |
| (e) | Định danh buổi nằm ở metadata/tiêu đề, không phải cột từng dòng (`:583`) | Sheet riêng **`_HTPLDN_META`**: `lich_hoc_id = bd1cdf35-8ab7-41f6-ae85-d21fdec2c8c2` (khớp buổi đang chọn) + `khoa_hoc_id` + `template_type=DIEM_DANH`. **Không** có cột buổi trong sheet dữ liệu | ✅ |

### Đối chứng độc lập

**Mở nội dung tệp thật bằng `openpyxl`** (không phải quan sát màn hình): tệp về máy tại `~/Downloads/mau-diem-danh-a7480002-0000-4000-8000-000000000002.xlsx`, 8 191 byte, `file` → *Microsoft Excel 2007+*, 2 sheet `_HTPLDN_META` + `Mẫu điểm danh`.

### Quan sát bắt buộc — enum điểm danh

Ảnh đối tác 24/07 cho thấy hệ thống lúc đó đòi cột `Ma hoc vien, Co mat (1/0)` (nhị phân). **Bản đo hiện tại KHÔNG còn nhị phân**: cột là "Trạng thái điểm danh" với **3 giá trị** Có mặt / Vắng có phép / Vắng không phép — khớp `:549`, `:581`, `:1919`. Trên màn, ô trạng thái là 3 nút chọn đúng 3 nhãn này.

### ⇒ **C3 ĐẠT** (5/5 số đo)

**Artifact:**
- [`image/KTDGKQHT_05-01-tab-diemdanh-chua-chon-buoi.png`](../image/KTDGKQHT_05-01-tab-diemdanh-chua-chon-buoi.png) — chứng minh: chưa chọn buổi thì 4 nút (kể cả "Tải mẫu điểm danh") **tắt**, và màn hiện dòng "Vui lòng chọn buổi học để bắt đầu điểm danh". Mốc: 2026-08-07 ~02:12 VN · khóa `a7480002…0002`.
- [`image/KTDGKQHT_05-02-da-chon-buoi-nut-taimau-bat.png`](../image/KTDGKQHT_05-02-da-chon-buoi-nut-taimau-bat.png) — **đã mở lại xác minh**: thanh bước "4 Đang diễn ra" đang sáng, buổi 4 đã chọn, nút "Tải mẫu điểm danh" **bật**, ô trạng thái là 3 nút chọn Có mặt/Vắng có phép/Vắng không phép, chân sidebar `HTPLDN · V1.0.9`.
- Tệp tải về: [`seed-files/mau-goc-KTDGKQHT_05.xlsx`](../seed-files/mau-goc-KTDGKQHT_05.xlsx) (giữ nguyên bản để truy lại nội dung).

---

## 5. Vế C1 — bản xem trước

**Quan hệ đã khoá:** `MATCH` · route `TEST` · SRS `srs-fr-03-dao-tao.md:593` (+ `:594`, `:650`)

### Thao tác (UI thật)

Cùng phiên, cùng buổi 4 → bấm **"Import Excel"** → hộp thoại **"Import điểm danh từ Excel"** → **`upload_file`** fixture qua vùng thả tệp thật (`uid=7_13`) → bấm **"Kiểm tra tệp"** → **dừng lại trước khi xác nhận nạp** → đọc khối xem trước bằng `innerText` (không dùng `textContent`).

**Chú thích hộp thoại đã đổi hẳn so với ảnh đối tác 24/07:**

| | Nội dung |
|---|---|
| Đối tác 24/07 (env nghiệm thu) | "File .xlsx, tối đa 5MB. **Cột bắt buộc: `Ma hoc vien,Co mat` (1/0)**." · một nút **"Bắt đầu Import"** |
| Bản đo 2026-08-07 | "File .xlsx, tối đa 5MB. **Chỉ dùng tệp từ nút Tải mẫu điểm danh. Hệ thống chỉ ghi dữ liệu sau khi bạn xem trước và xác nhận.**" · nút **"Kiểm tra tệp"** |

### Số đo

| # | Chuẩn chấm | Số đo thực | Đạt |
|---|---|---|---|
| 1 | Khối xem trước hiện ra **TRƯỚC** khi ghi dữ liệu (`:594`) | Khối tiêu đề **"Kết quả kiểm tra - chưa nhập dữ liệu"** hiện ra; nút hành động là **"Xác nhận import (3 dòng hợp lệ)"** ⇒ xem trước là **cổng xác nhận**, chưa ghi. Máy chủ trả `sessionId` để xác nhận ở bước sau | ✅ |
| 2 | Phân tách rõ dòng hợp lệ vs dòng lỗi | Dải số: **Tổng dòng 5 · Hợp lệ 3 · Bỏ qua 0 · Lỗi 2**. Hai thẻ: **"Hợp lệ (3)"** / **"Lỗi/Bỏ qua (2)"** | ✅ |
| 3 | Mỗi dòng lỗi có lý do/mã lỗi + số dòng; 2 lỗi khác lý do ra **2 lý do khác nhau** | Dòng **5** → `ERR-KQ-03: Không tìm thấy học viên ở dòng 5 (định danh không hợp lệ hoặc không thuộc khóa học này)` · Dòng **6** → `ERR-KQ-04: Giá trị điểm danh không hợp lệ: XYZ`. **2 lý do khác nhau, gắn đúng số dòng** | ✅ |

**Bộ ba số đo quyết định: (hợp lệ, lỗi, tập lý do) = (3, 2, {ERR-KQ-03@dòng 5, ERR-KQ-04@dòng 6})**
**Cộng khớp:** 3 + 0 + 2 = **5** = tổng dòng dữ liệu fixture ✅

Câu chữ 2 mã lỗi khớp nguyên văn SRS `:637` và `:638`.

### Đối chứng độc lập — **response body của chính request xem trước**

`POST /api/v1/khoa-hocs/a7480002…0002/diem-danhs/import/preview` → **200**
(multipart: `file=fixture-KTDGKQHT_05-3hople-2loi.xlsx` + `lichHocId=bd1cdf35…c2c8c2`)

```json
{"success":true,"data":{"total":5,"success":3,"skipped":0,"errors":2,"details":[
 {"row":2,"status":"success","hocVienId":"dbf62f06-…-b660","hoTen":"QA R3 Mailto Ba","trangThai":"CO_MAT"},
 {"row":3,"status":"success","hocVienId":"cd17f1b7-…-3458b","hoTen":"QA R3 Mailto Hai","trangThai":"VANG_PHEP"},
 {"row":4,"status":"success","hocVienId":"6feead91-…-27f53","hoTen":"QA R3 Mailto Mot","trangThai":"VANG_KHONG_PHEP"},
 {"row":5,"status":"error","reason":"ERR-KQ-03: Không tìm thấy học viên ở dòng 5 (…)"},
 {"row":6,"status":"error","reason":"ERR-KQ-04: Giá trị điểm danh không hợp lệ: XYZ"}],
 "sessionId":"cbdeadfc-d9a8-4c2c-9db7-8c8971c3d0d5"}}
```

**Hai đường KHỚP tuyệt đối** (màn 3/2/5 ↔ payload `success:3, errors:2, total:5`; enum lưu đúng `CO_MAT` / `VANG_PHEP` / `VANG_KHONG_PHEP` theo `:549`) ⇒ **dừng, không mở đường thứ ba**.

### ⇒ **C1 ĐẠT** (3/3 chuẩn)

**Artifact:**
- [`image/KTDGKQHT_05-03-hopthoai-import-truoc-khi-chon-tep.png`](../image/KTDGKQHT_05-03-hopthoai-import-truoc-khi-chon-tep.png) — hộp thoại lúc chưa chọn tệp, chú thích mới + nút "Kiểm tra tệp" (tắt). Mốc ~02:16 VN.
- [`image/KTDGKQHT_05-04-xemtruoc-tab-loi-2dong.png`](../image/KTDGKQHT_05-04-xemtruoc-tab-loi-2dong.png) — thẻ "Lỗi/Bỏ qua (2)" với 2 dòng lỗi.
- [`image/KTDGKQHT_05-05-thongbao-sau-khi-xacnhan-nap.png`](../image/KTDGKQHT_05-05-thongbao-sau-khi-xacnhan-nap.png) — **artifact mạnh nhất, đã mở lại xác minh**: một khung chứa đồng thời khối xem trước đầy đủ (Tổng 5 / Hợp lệ 3 / Bỏ qua 0 / Lỗi 2), 2 dòng lỗi ERR-KQ-03 + ERR-KQ-04, nút "Xác nhận import (3 dòng hợp lệ)", **và** thông báo lỗi hệ thống của bước C2. Mốc: 2026-08-07 02:18:52 VN.
- Response body reqid=173 (đã trích ở trên).

---

## 6. Vế C2 — báo cáo sau khi nạp 🔴 **KHÔNG ĐẠT**

**Quan hệ đã khoá:** `MATCH` · route `TEST` · SRS `srs-fr-03-dao-tao.md:595` (+ `:594`, `:650`)

### Thao tác (UI thật)

Cài `MutationObserver` trên `document.body` **TRƯỚC** khi bấm (không lọc trùng, đọc bằng `innerText`, đếm kèm số request) → hẹn giờ bấm **"Xác nhận import (3 dòng hợp lệ)"** sau 2 500 ms rồi mới chụp màn (để bắt thông báo tự tắt).

### Số đo

| # | Chuẩn chấm | Số đo thực | Đạt |
|---|---|---|---|
| 1 | Hệ thống **trả về/hiển thị báo cáo kết quả import**, không im lặng | Không có báo cáo import. Thông báo duy nhất người dùng thấy: **"Lỗi hệ thống, vui lòng thử lại sau."** | ❌ |
| 2 | Báo cáo cho biết **số nạp thành công** + **số không hợp lệ** | **Không có con số nào** trong thông báo | ❌ |
| 3 | Hai con số **đúng** so với tệp và **cộng khớp** = 5 | Không áp dụng (không có số) | ❌ |
| *(đối chứng)* | Số học viên thực đổi trạng thái = **3**; 2 dòng lỗi **không** được ghi (`:594`) | **0/3 dòng hợp lệ được ghi** | ❌ |

**Thông báo bắt được (observer, không lọc trùng):** 2 nút DOM cùng **một mốc giờ** (`dt = +111 ms` cả hai) — là thẻ bọc `.ant-message` và thẻ con `.ant-message-notice-wrapper` của **CÙNG một thông báo**, đếm theo mốc giờ ⇒ **1 thông báo**, nội dung `Lỗi hệ thống, vui lòng thử lại sau.`
**Số request phát sinh kèm thông báo:** 2 (`…/diem-danhs/import/confirm` + `thong-baos/unread-count`) ⇒ đúng 1 lần bấm, không double-submit.

### Phản hồi máy chủ — bằng chứng quyết định

`POST /api/v1/khoa-hocs/a7480002-0000-4000-8000-000000000002/diem-danhs/import/confirm` → **HTTP 500**

Request body:
```json
{"lichHocId":"bd1cdf35-8ab7-41f6-ae85-d21fdec2c8c2","sessionId":"cbdeadfc-d9a8-4c2c-9db7-8c8971c3d0d5"}
```
Response body:
```json
{"success":false,"error":{"code":"ERR-SYS-00-00-01","message":"Lỗi hệ thống, vui lòng thử lại sau",
 "timestamp":"2026-08-06T19:18:52.365Z","requestId":"6415303f-0248-42b0-b314-defb9492ce64"}}
```

### Đối chứng độc lập — đọc lại bảng điểm danh của **đúng buổi vừa nạp**

`GET /api/v1/khoa-hocs/a7480002…0002/diem-danhs?lichHocId=bd1cdf35…c2c8c2` (sau khi xác nhận):

| Học viên | `trangThai` | `id` bản ghi |
|---|---|---|
| Nguyễn Văn A | `null` | `""` |
| QA R3 Mailto Ba | `null` | `""` |
| QA R3 Mailto Hai | `null` | `""` |
| QA R3 Mailto Mot | `null` | `""` |

**Số đã ghi = 0** — **y hệt mốc gốc trước khi nạp**. Xác nhận thêm trên UI: bảng điểm danh buổi 4 có **12 nút chọn trạng thái, 0 nút được tick**.

**Hai đường KHỚP** (thông báo lỗi + HTTP 500 ↔ 0 bản ghi được ghi) — không mâu thuẫn ⇒ đủ điều kiện chốt.

### Phân loại lỗi (Rule 9)

Nhật ký trình duyệt chỉ có **đúng 1 lỗi**: `Failed to load resource: the server responded with a status of 500` — **không có lỗi phía giao diện**. ⇒ **Lỗi phía máy chủ**: dừng, không thử lại mù, chuyển dev BE.

### ⇒ **C2 KHÔNG ĐẠT**

Vi phạm hai dòng SRS đã khoá:
- `:594` — *"Nếu xác nhận: merge kết quả — **chỉ merge dòng hợp lệ**, dòng lỗi bỏ qua"* ⇒ phải ghi **3** dòng, thực tế ghi **0**.
- `:595` — *"Trả về báo cáo import"* ⇒ phải có báo cáo, thực tế chỉ có thông báo lỗi hệ thống chung.

Đồng thời trái Acceptance Criteria `:652` — *"**When** import **Then** đối chiếu học viên theo định danh sẵn trong tệp, **merge dòng hợp lệ**"*.

---

## 7. Dữ liệu đã seed / mutate (khai báo bắt buộc)

| Env | Bản ghi bị đổi | Đổi gì | Vì sao |
|---|---|---|---|
| `18.143.165.120.nip.io` (nội bộ) | Đăng ký học viên `2c87b577-0ad0-440d-b9da-ebb7a7a9311e` — **"QA R3 Mailto Mot"** (`qa.r3.mailto1@gmail.com`), khóa `KH-QAW7-HOINGHI` `a7480002-0000-4000-8000-000000000002` | Trạng thái đăng ký **`Chờ duyệt` → `Đã duyệt`** (qua nút "Phê duyệt" trên UI, `POST /api/v1/dang-ky-dao-taos/{id}/approve` → 201) | Khóa chỉ có 2 học viên đã duyệt; thiết kế fixture đã khoá cần **4 học viên thuộc khóa** (3 hợp lệ + 1 dòng lỗi enum) |
| `18.143.165.120.nip.io` (nội bộ) | Đăng ký học viên `b7745c2c-d440-4abc-9010-550db3441858` — **"Nguyễn Văn A"** (`nguyenvana@gmail.com`), cùng khóa | Trạng thái đăng ký **`Chờ duyệt` → `Đã duyệt`** | như trên |

- **Không** tạo khóa học mới, **không** tạo buổi học mới, **không** đụng dữ liệu của đối tác (khóa `0aad5545…5862` trong ảnh đối tác nằm trên env khác, không tồn tại ở đây).
- **Không** ghi được bản ghi điểm danh nào (do chính lỗi C2) ⇒ trạng thái điểm danh buổi 4 **giữ nguyên như trước khi đo**.
- 2 học viên còn lại ("Nguyễn Văn Ngọc", "QA Probe Email") **vẫn ở `Chờ duyệt`** — không đụng.

---

## 8. Bug mới / candidate

| Loại | Nội dung |
|---|---|
| **Bug mới** | **Không có.** Lỗi 500 ở bước xác nhận nạp là **của chính vế C2**, không phải bug ngoài phạm vi |
| **Candidate** | **Không có.** Bẫy §7-20 của chuẩn chấm (bảng điểm danh render đầu cột với thân rỗng khi chưa chọn buổi — vế của KTDGKQHT_03) **KHÔNG tái xuất hiện**: màn hiện đúng dòng *"Vui lòng chọn buổi học để bắt đầu điểm danh"* theo `:1921` |

**Ghi chú mềm (không chặn bàn giao, không phải câu hỏi BA):** SRS `:595` chỉ ghi *"Trả về báo cáo import"* và bảng Error Handling `:633–643` không định nghĩa thông báo **thành công** nào. Sau khi dev sửa lỗi 500, đề nghị BA bổ sung câu chữ chuẩn cho báo cáo import vào Error Handling FR-III-05 để vòng nghiệm thu sau có mốc chấm câu chữ.

---

## 9. VERDICT LOGIC

| Vế | Quan hệ (đã khoá) | Kết quả đo | Neo SRS |
|---|---|---|---|
| **C3** — cơ chế tệp mẫu | `MATCH` | ✅ **ĐẠT** (5/5 số đo) | `:571–583`, `:590`, `:651`, `:1919` |
| **C1** — bản xem trước | `MATCH` | ✅ **ĐẠT** (3/3 chuẩn; (3,2,5) khớp cả 2 đường) | `:593`, `:594`, `:650` |
| **C2** — báo cáo sau khi nạp | `MATCH` | ❌ **KHÔNG ĐẠT** — HTTP 500 `ERR-SYS-00-00-01`, **0/3** dòng hợp lệ được ghi | `:594`, `:595`, `:652` |
| **D1** — đề xuất cột "Mã học viên" của TKM | `DIFF` nhưng **BA đã trả lời trong chính SRS hiện hành** | **Không đo** — không mở câu hỏi BA mới | `:1919`, `:14`, `srs-v3.5.md:75`, `:3550–3562` |

### ⇒ **VERDICT = `Reopen`**

**Lý do neo vào vế Cn:** Flow 04 §Ca biên — *"còn ≥1 vế `MATCH` vẫn lỗi → Reopen"*. Vế **C2** là `MATCH` (SRS `:594`/`:595` và kỳ vọng đối tác cùng đòi hệ thống nạp được dòng hợp lệ rồi báo cáo kết quả) nhưng web **không đạt**: bấm xác nhận nạp trả lỗi hệ thống và **không dòng nào được ghi**.

**Không có vế `DIFF/GAP` nào cần chặn Pass** ⇒ **không** phát sinh câu `CẦN BA CONFIRM`.

**Phần đã đạt (ghi nhận cho dev, tránh sửa hỏng):** C3 và C1 đã đạt đầy đủ — cơ chế "Tải mẫu → điền → tải lên" và bản xem trước 2 bước đã đúng đặc tả. **Chỉ còn bước xác nhận nạp bị lỗi.**

**Ô `Trạng thái dev fix` đề nghị ghi:** `Reopen`

**Giới hạn hiệu lực:** verdict chỉ áp cho env `https://18.143.165.120.nip.io`, bản dựng `assets/index-DsMHK7Dp.js` / chuỗi phiên bản `V1.0.9`, đo 2026-08-07 02:08–02:20 giờ VN. Đối tác đo trên `htpldn-uat.ospgroup.vn` bản `V1.0` ngày 24/07/2026.

---

## 10. Cổng chốt verdict — tự kiểm

| # | Câu hỏi (Flow 04) | Trả lời |
|---|---|---|
| 1 | Mỗi vế chấm neo vào dòng nào của đúng SRS prompt cấp? | C1 → `:593`(+`:594`,`:650`) · C2 → `:595`(+`:594`,`:652`) · C3 → `:571–583`,`:590`,`:651`,`:1919`. Đã **tự mở lại** `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-03-dao-tao.md` trong lượt này; tổng **2 296 dòng**, md5 `63f378eab606497c51f0c38c74420c89` — **khớp** bản Giai đoạn A ⇒ số dòng còn hiệu lực |
| 2 | Mọi thao tác đã chạy có trả lời một vế Cn hoặc là đối chứng của vế đó? | Có. Duyệt 2 học viên = dựng tiền đề T3 (khai ở §7); đọc khóa `DDD-KH-011` = tiền đề T4. Không mở thêm màn/vai trò/bộ lọc nào |
| 3 | Mọi vế `DIFF/GAP` đã bị chặn Pass và có câu hỏi BA đúng phần thiếu? | Không có vế `DIFF/GAP` trong chuẩn chấm. D1 đã được BA trả lời trong SRS hiện hành ⇒ không mở câu hỏi mới |
| 4 | Đã đọc đầy đủ expected, không dựa bản cắt ngắn? | Có — chuẩn chấm Giai đoạn A đã đọc trọn ô "Kết quả mong đợi", "Điều kiện", "Các bước thực hiện", "Loại vấn đề", "TKM phản hồi lần 1"; `DEV phản hồi lần 1` trống |
| 5 | Điều kiện đo có khớp tiền đề của case; khác thì đã xử lý? | Hai chênh lệch đã khai: **(a)** env + bản dựng khác (§1, §9 giới hạn hiệu lực); **(b)** phiếu ghi điều kiện *"Đang diễn ra **hoặc Đã kết thúc**"* nhưng SRS `:536` PRE-03 chỉ cho `DANG_DIEN_RA` ⇒ **đã đo trên `DANG_DIEN_RA`** đúng SRS. Không chấm Fail nào liên quan `DA_KET_THUC` |

### Bẫy chặn FAIL oan — đã tuân thủ

- ❌ **Không** chấm Fail vì Tab Điểm danh thiếu cột "Mã học viên" (`:1919`, `srs-v3.5.md:75`).
- ❌ **Không** chấm Fail vì câu chữ thông báo khác chuỗi đối tác viết — C2 fail vì **không có báo cáo và 0 dòng được ghi**, không vì câu chữ.
- ❌ **Không** chấm Fail vì khối xem trước thiếu con số tổng — thực tế có đủ số.
- ❌ **Không** đo trên khóa `DA_KET_THUC`.
- ❌ **Không** chấm Fail vì tên tệp mẫu / vì `hoc_vien_id` là UUID khó đọc (`:581` quy định đúng là ID nội bộ opaque).

*Đo xong 2026-08-07 ~02:20 giờ VN · tài khoản `cbnv_tw_02` · 1 phiên đăng nhập duy nhất.*
