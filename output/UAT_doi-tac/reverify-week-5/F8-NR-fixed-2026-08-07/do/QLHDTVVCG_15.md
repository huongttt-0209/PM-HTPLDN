# Nhật ký đo — `QLHDTVVCG_15` (dòng 321 tab `bug`)

**Ngày:** 2026-08-07 · **Quy trình:** [`flows/04-verify-bug-dev-fix-khong-ho-so.md`](../../../../../flows/04-verify-bug-dev-fix-khong-ho-so.md)
**Chuẩn chấm đã khóa (Giai đoạn A — CẤM sửa):** [`chuan/QLHDTVVCG_15.md`](../chuan/QLHDTVVCG_15.md) — 5 vế: **C1 `MATCH`** · **C2 `MATCH`** · **C3 `MATCH`** · **C4 `MATCH`** · **C5 `DIFF`** → route **BA**.

---

## 0. Đọc lại dòng phiếu trên bảng trước khi đo (bắt buộc)

Đọc lúc **14:47 ngày 07/08/2026** bằng `tools/sheet_dump_bug_rows_2026-08-07.py --rows 321` (chỉ đọc).

| Ô | Giá trị đọc được |
|---|---|
| `Mã TC` (D) | `QLHDTVVCG_15` |
| `Trạng thái` (N) `N/R` · `Dopai` (O) `N/R` | phiếu **chưa từng chạy** |
| `Kết quả thực tế` (L) · `Ảnh/vieo 1` (M) · `TKM phản hồi lần 1` (Q) | **RỖNG cả ba** |
| `Trạng thái dev fix` (R) | `Fixed` |
| `Kết quả verify` (T) | **RỖNG** ⇒ không có nội dung cũ để giữ |
| `Kết quả mong đợi` (K) | `- Sinh mã hợp đồng HDTV-{YYYYMMDD}-{số thứ tự}, tạo bản ghi hợp đồng cùng toàn bộ mốc tiến độ, thanh toán giai đoạn, liên kết vụ việc, tệp đính kèm đã nhập; gán trạng thái "Đang thực hiện".` / `- Hệ thống hiển thị thông báo "Đã lưu hợp đồng" và quay về danh sách.` |
| `DEV phản hồi lần 1` (S) | *"BA chốt 06/08/2026 — Loại 4 hướng B (bản gốc bị sót câu thông báo): lấy câu theo bản bàn giao .docx là "Đã lưu hợp đồng"; Kết quả mong đợi của đơn vị kiểm thử viết ĐÚNG, không phải sửa. Dev action: Có. Dev đã dùng chung câu INF-HDTV-01 "Đã lưu hợp đồng" cho mọi đường lưu hợp đồng (tạo mới và cập nhật)."* |

Không có thay đổi so với bản chụp `audit/gia-tri-o-truoc-khi-ghi.md`. Không có phiên khác vừa ghi dòng 321.

## 1. Môi trường + vân tay bản dựng

| Hạng mục | Giá trị |
|---|---|
| Môi trường | `https://18.143.165.120.nip.io` — env **NỘI BỘ** (đối tác nghiệm thu trên `htpldn-uat.ospgroup.vn`) |
| **Vân tay ĐẦU phiên** (14:14:57) | `GET /` → `assets/index-BbPPdate.js` · `assets/index-DVlgOkLg.css` · `last-modified: Fri, 07 Aug 2026 06:47:57 GMT` · `etag "6a757f9d-428"` |
| Bó mã trình duyệt thực nạp | `/assets/index-BbPPdate.js` (khớp) — **cùng phiên, cùng tab với `_13`, không tải lại trang giữa hai phiếu** |
| Tài khoản đo | **`cbnv_tw_03`** / `Test@1234` — đăng nhập bằng giao diện thật lúc 14:16. Không gặp `ERR-AUTH-SYS-00-03`, **không** fallback sang `_05`. |
| Danh tính đọc được | `hoTen` = `CB Nghiệp vụ - Trung ương #03` · `vaiTro` = `CB_NV_TW` · `capDonVi` = `TW` · `donViId` = `00000000-0000-4000-8000-000000000001` (`Cục Bổ trợ tư pháp - Bộ Tư pháp`) |
| Cửa sổ | 1440×900 |

## 2. Bề mặt đã chấm — **MÀN 1** (Chi tiết Vụ việc → mục "HĐ tư vấn liên kết")

Theo chỉ đạo điều phối 07/08/2026: bề mặt chấm chính thức của cả đợt A là **Màn 1**.
Lý do chọn: đây là **nơi duy nhất** có nút mở biểu mẫu thêm hợp đồng, và bộ lọc của nó khớp `:287`.

Đường vào thực tế (bước J của phiếu ghi *"Chọn menu Hợp đồng Tư vấn"* — mục menu đó **không tồn tại theo
thiết kế**, `:266` + `:268`; đây là **tiền đề**, không phải vế chấm, không log lỗi):

```
Vụ việc HTPL → ô tìm kiếm nhập VV-BTP-TW-20260804-002 → [Tìm kiếm] → [Xem vụ việc]
→ mở mục "HĐ tư vấn liên kết" → [+ Tạo hợp đồng]
```

## 3. Tiền đề đã dựng trước khi bấm Lưu

| Nhóm | Đã nhập | Nguồn yêu cầu |
|---|---|---|
| Thông tin chung | Tên HĐ 84 ký tự (>30) · Bên B `Chuyên gia UAT QLNDTVVCG 38` · TVV `CG-QLND38-UAT` · Giá trị `250.000.000` · Thời gian `07/08/2026`→`25/08/2026` (**18 ngày ≤ 30**, để `_02` C3 có dòng đo vế tô đỏ `:288`) · Nội dung 85 ký tự · Ghi chú mang dấu `QA-F8-321-20260807` | `:290` |
| **Mốc tiến độ** | **1** dòng — `Ban giao ho so tra cuu nhan hieu` · dự kiến `18/08/2026` · `Chưa bắt đầu` | `:122` |
| **Thanh toán giai đoạn** | **1** dòng — `Dot 1 - tam ung khi ky hop dong` · `100.000.000` · `15/08/2026` · `Chưa TT`; tổng 100tr **≤** giá trị HĐ 250tr (qua kiểm tra `:121`) | `:122`, `:121` |
| **Vụ việc liên kết** | **3** — `VV-BTP-TW-20260804-002` / `-003` / `-004` (đều có tên DN 41 ký tự > 40) | `:123` |
| **Tệp đính kèm** | Bộ tệp thật (pdf/docx/xlsx/png) **đã chuẩn bị đủ** ở `files/fixture-hdtv/` ⇒ **tiền đề phía người đo ĐẠT**. Không nạp được là do **hành vi của phần mềm**: ở chế độ Thêm mới mục "Tài liệu đính kèm" **không có ô chọn tệp** (`input[type=file]` đếm được = **0**) và hiện dòng chữ *"Vui lòng lưu hợp đồng trước khi đính kèm tài liệu."* → xem §4-C2 | `:92`, `:290` |

> ⚠️ **Ghi chú kỹ thuật khi nhập:** ô "Nội dung hợp đồng" đặt giá trị bằng `fill_form` thì DOM có chữ nhưng
> bộ đếm ký tự của giao diện vẫn `0 / 10000` ⇒ React **chưa nhận**, gửi đi sẽ mất trường. Phải bấm vào ô rồi
> gõ phím thật (`type_text`); sau đó bộ đếm lên `85 / 10000`. Đã kiểm lại bằng thân yêu cầu gửi đi (§4-C2).

## 4. Đo từng vế

### C1 — Sinh mã `HDTV-{YYYYMMDD}-{SEQ}` · `MATCH` · ✅ **ĐẠT**

| | |
|---|---|
| **Đường 1 — giao diện** | Sau khi lưu, mã hiển thị ở 3 chỗ trên chi tiết hợp đồng: dưới tiêu đề, ô "Mã hợp đồng", và cột "Mã hợp đồng" của bảng trên Màn 1 — cả 3 đều là **`HDTV-20260807-0006`** |
| **Đường 2 — đối chứng độc lập** | Đọc lại bản ghi từ máy chủ: `GET /api/v1/hop-dong-tu-vans/d16487f4-3ccc-4629-8e07-bb63ea9a12be` → `maHopDong` = **`HDTV-20260807-0006`** — trùng khít chuỗi hiển thị |
| **Kiểm phần ngày** (bẫy đã nêu ở chuẩn chấm) | `20260807` = **ngày tạo bản ghi** (`ngayTao` = `2026-08-07T07:43:54.778Z`), **không** phải ngày bắt đầu hợp đồng (cũng 07/08 nhưng trùng ngẫu nhiên) và **không** phải ngày kết thúc (25/08/2026). Khuôn `HDTV-` + `YYYYMMDD` + số thứ tự `0006` khớp `:81`, `:119`, `:514` |

**Hai đường khớp nhau ⇒ dừng.**

### C2 — Lưu bản ghi **cùng toàn bộ** nhóm con · `MATCH` · ⚠️ **ĐẠT 3/4 NHÓM · riêng phần tệp đính kèm là `GAP` → CẦN BA**

> 🔴 **Không viết "không đo được" cho phần tệp.** Dòng 106 của chuẩn chấm (*"Thiếu nhóm nào thì phần đó của C2
> không đo được"*) nằm trong ô **"Dữ liệu đầu vào (bắt buộc để C2 đo được)"** — đó là luật cho ca **người đo
> không chuẩn bị đủ dữ liệu**. Lượt này người đo **đã chuẩn bị đủ tệp thật**; thứ chặn là **hành vi của phần
> mềm**. Hành vi đó **đo được và đã đo**, nên phải ghi là **kết quả đo**, không phải thiếu điều kiện đo.

**Đường 1 — giao diện, mở lại chi tiết sau khi lưu** (KHÔNG đếm trên biểu mẫu chưa tải lại — bẫy đã nêu):
bấm biểu tượng "Xem chi tiết" trên dòng vừa tạo → màn `/hop-dong-tv/d16487f4-…` tải lại từ máy chủ.

| Nhóm | Đã nhập | Đếm trên chi tiết sau khi lưu | Kết luận |
|---|---|---|---|
| Mốc tiến độ | 1 | **1** dòng — `Ban giao ho so tra cuu nhan hieu` · `18/08/2026` · `Chưa bắt đầu` | ✅ khớp |
| Thanh toán giai đoạn | 1 | **1** dòng — `Dot 1 - tam ung khi ky hop dong` · `100.000.000 VNĐ` · `15/08/2026` · `Chưa thanh toán` | ✅ khớp |
| Vụ việc liên kết | 3 | **3** dòng — `-002`, `-003`, `-004`, đủ cột Doanh nghiệp / Lĩnh vực / Trạng thái | ✅ khớp |
| Tệp đính kèm | phần mềm **không cho nhập** ở chế độ Thêm mới | *"Chưa có tài liệu đính kèm"* | ❓ **`GAP` → CẦN BA** |

**Đường 2 — đối chứng độc lập, đọc bản ghi từ máy chủ:**

```
GET /api/v1/hop-dong-tu-vans/d16487f4-3ccc-4629-8e07-bb63ea9a12be  → 200
mocTienDos = 1 · thanhToans = 1 · vuViecLienKets = 3 · fileDinhKem = 0 · version = 1
```

Thân yêu cầu gửi đi lúc lưu cũng chứa đủ `mocTienDos[1]`, `thanhToans[1]`, `vuViecIds[3]`, `noiDung`, `ghiChu`
⇒ loại được ca *"giao diện nhận dữ liệu con nhưng máy chủ chỉ lưu Thông tin chung"*.

**Hai đường khớp nhau ở 3 nhóm ⇒ 3 nhóm ĐẠT.**

Phụ chứng cho `:162` (*AUDIT_LOG ghi nhận*): chi tiết hợp đồng có mục **"Nhật ký hoạt động"** đã ghi
`07/08/2026 14:43 · Tạo mới · CB Nghiệp vụ - Trung ương #03 (cbnv_tw_03) · POST /api/v1/hop-dong-tu-vans · 201`.

**Phần tệp đính kèm — `GAP`, chỉ ghi hiện trạng + câu hỏi BA (CẤM Pass, CẤM kết "lỗi dev"):**

**1) HÀNH VI ĐO ĐƯỢC — năng lực đính kèm CÓ, nhưng bị tách làm 2 bước:**

| Chế độ | Ô chọn tệp | Bằng chứng |
|---|---|---|
| **Thêm mới** | **KHÔNG có** — `input[type=file]` đếm được **0**; thay vào đó là dòng chữ *"Vui lòng lưu hợp đồng trước khi đính kèm tài liệu."* | ảnh 01 |
| **Sửa** (mở sau khi đã lưu) | **CÓ** — vùng *"Kéo thả hoặc nhấp để chọn tệp đính kèm"*, `input[type=file]` đếm được **1**; ràng buộc ghi ngay trên màn: tối đa 10 tệp · `.pdf .doc .docx .xls .xlsx .jpg .png` · 20MB/tệp | ảnh 04 |

⇒ Phần mềm **yêu cầu lưu hợp đồng trước rồi mới đính kèm**, không phải "không đính kèm được".

> ⚠️ Chỉ **NHÌN THẤY** ô chọn tệp rồi bấm **[Hủy]** — **KHÔNG bấm tải tệp lên**. Thao tác sửa hợp đồng là hành
> động của phiếu **`_21` (đợt C)**, làm bây giờ sẽ làm bẩn phép đo đó. Đã xác minh không đổi dữ liệu: `version = 1`.

**2) Đối chứng độc lập:** `/api/docs-json` — điểm cuối nạp tệp là `POST /api/v1/hop-dong-tu-vans/{id}/files`,
**buộc phải có `id` hợp đồng trước** ⇒ phía máy chủ cũng thiết kế theo hai bước. Là **hành vi nhất quán**,
không phải trục trặc ngẫu nhiên.

**3) Đặc tả đứng ở đâu** (tự mở tệp đọc lại 4 chỗ lượt này):

| Dòng | Bảng | Có nhắc tệp đính kèm? |
|---|---|---|
| `:92` | **Inputs** | **CÓ** — `file_dinh_kem` · `file[]` · `N` (không bắt buộc) · *"Upload nhiều file"* · nguồn *"người dùng upload"* |
| `:290` | **Thành phần màn hình** | **CÓ** — *"File đính kèm"* là trường của *"trang thêm/sửa"* |
| `:122`, `:123` | **Bước xử lý KHI LƯU** | **KHÔNG** — chỉ nhắc *"mốc tiến độ + thanh toán giai đoạn"* và *"liên kết vụ việc"* |
| `:159`–`:162` | **Outputs / Postconditions** | **KHÔNG** — chỉ có HĐ tạo/cập nhật/xóa mềm · mốc tiến độ và thanh toán · liên kết vụ việc · AUDIT_LOG |

⇒ Đặc tả **CÓ khai trường tệp trên biểu mẫu**, nhưng **KHÔNG phát biểu ở đâu rằng tệp phải được lưu CÙNG LÚC
tạo bản ghi**. Trong khi cột `Kết quả mong đợi` của phiếu nói rõ *"cùng toàn bộ … tệp đính kèm đã nhập"*.
⇒ **đặc tả IM LẶNG** ⇒ quan hệ cho **riêng phần tệp** là **`GAP`** ⇒ **CẤM Pass, CẤM kết "lỗi dev"**, đưa vào câu hỏi BA.

**4) Câu hỏi BA (soạn theo mẫu vế `GAP`):**

> Đối tác kỳ vọng tạo hợp đồng và nạp tệp đính kèm trong **cùng một lượt lưu**. Đặc tả **có** khai trường tệp
> trên biểu mẫu thêm/sửa (`:92`, `:290`) nhưng **bước xử lý khi lưu** (`:122`, `:123`) và **Outputs**
> (`:159`–`:162`) **không nhắc** tệp đính kèm, nên **không có căn cứ đòi lưu cùng lúc**. **Web hiện tại** yêu cầu
> lưu hợp đồng trước rồi mới đính kèm ở chế độ Sửa. Đề nghị nghiệp vụ chốt: nạp tệp lúc tạo có **bắt buộc**
> không, hay **tách hai bước** là chấp nhận được — và **bổ sung điều này vào đặc tả**.

### C3 — Gán trạng thái "Đang thực hiện" · `MATCH` · ✅ **ĐẠT**

| | |
|---|---|
| **Đường 1 — giao diện** | Chi tiết hợp đồng hiện nhãn **"Đang thực hiện"** ở 2 chỗ (thẻ dưới tiêu đề + ô "Trạng thái"); cột "Trạng thái" của bảng Màn 1 cũng **"Đang thực hiện"**. Là **nhãn tiếng Việt**, **không** lộ mã `DANG_THUC_HIEN` ⇒ không vướng `srs-fr-05-vu-viec.md:1492` |
| **Đường 2 — đối chứng độc lập** | Đọc lại bản ghi từ máy chủ → `trangThai` = **`DANG_THUC_HIEN`** ⇒ đúng giá trị mặc định `:396`, loại được ca *"giao diện hiển thị mặc định cứng"* |
| Ghi thêm | `:464` xác nhận trạng thái HĐ chỉ là trường trạng thái đơn giản, không có vòng đời phê duyệt ⇒ lưu xong là xong, không phải chờ duyệt |

**Hai đường khớp nhau ⇒ dừng.**

### C4 — Thông báo "Đã lưu hợp đồng" · `MATCH` · ✅ **ĐẠT**

**Đường 1 — giao diện, bắt thông báo thoáng qua đúng cách:** cài `MutationObserver` trên `document.body`
lúc **07:39:57 GMT (14:39:57)**, **TRƯỚC** khi bấm Lưu, **CẤM lọc trùng**, đọc bằng `innerText`.

| Đo | Kết quả |
|---|---|
| Số nút thông báo bắt được (thô, không lọc trùng) | **2** (`div.ant-message` + `div.ant-message-notice-wrapper` — vỏ ngoài + vỏ trong của **một** thông báo) |
| **Số mốc giờ khác nhau** | **1** — `2026-08-07T07:43:54.827Z` |
| Chữ đọc được | **`Đã lưu hợp đồng`** — trùng **từng chữ** `INF-HDTV-01` ở `:173` và `:187` |
| **Số yêu cầu lưu gửi đi** | **1** — `POST /api/v1/hop-dong-tu-vans` |

**Đường 2 — đối chứng độc lập:** chính yêu cầu lưu đó trả **HTTP 201**, tiêu đề `date: Fri, 07 Aug 2026
07:43:54 GMT` — **cùng mốc giây** với thông báo (07:43:54.827). ⇒ 1 yêu cầu ↔ 1 thông báo, **không** có
thông báo kép, **không** có "im lặng".

**Hai đường khớp nhau ⇒ dừng.**

### C5 — "quay về danh sách" · `DIFF` · ❓ **CHỈ GHI HIỆN TRẠNG — CẤM Pass, CẤM Fail**

**Hiện trạng đo được** (đọc đường dẫn + tiêu đề màn ngay sau khi thông báo hiện):

| Đo | Kết quả |
|---|---|
| Đường dẫn sau khi lưu | **`https://18.143.165.120.nip.io/vu-viec/6bf98a2e-77ee-4c03-8e1f-a51561406a3b`** — **không đổi** so với trước khi bấm |
| Trạng thái hộp thoại | cả 2 hộp thoại (`Tạo hợp đồng tư vấn`, `Liên kết vụ việc`) chuyển `display: none` ⇒ **biểu mẫu đóng** |
| Màn dừng ở đâu | **Chi tiết vụ việc `VV-BTP-TW-20260804-002`** — đúng ngữ cảnh đã mở biểu mẫu |
| Bảng trong màn đó | mục "HĐ tư vấn liên kết" **tự nạp lại** (`GET /api/v1/hop-dong-tu-vans?vuViecId=6bf98a2e-…`) và **đã hiện bản ghi mới**, phân trang `1-1 / 1 mục` |

⇒ **Dev đang theo phía SRS** (`:175` + `:187`): đóng biểu mẫu, trả người dùng về **ngữ cảnh đã mở nó**,
**không** chuyển sang một màn danh sách hợp đồng độc lập.

**Câu bắt buộc cho vế `DIFF` (đã điền hiện trạng):**

> **CẦN BA CONFIRM:** đối tác kỳ vọng sau khi lưu hợp đồng mới thì hệ thống **quay về màn danh sách hợp đồng**;
> SRS quy định nhóm X.3 **không có màn danh sách độc lập**, sau khi lưu hệ thống **đóng biểu mẫu và trả người
> dùng về ngữ cảnh đã mở nó** (Chi tiết Vụ việc hoặc Chi tiết Tư vấn viên) — `srs-fr-14-hop-dong-tv.md:175`,
> ghi chú `[BA chốt 2026-08-06]`, và `:187`; **web/dev hiện tại: đóng biểu mẫu, ở lại Chi tiết vụ việc
> `VV-BTP-TW-20260804-002` và nạp lại bảng "HĐ tư vấn liên kết" ngay trong màn đó — tức làm theo phía SRS.**

## 5. Verdict

| Vế | Quan hệ | Kết quả đo |
|---|---|---|
| C1 — sinh mã `HDTV-{YYYYMMDD}-{SEQ}` | `MATCH` | ✅ ĐẠT |
| C2 — lưu kèm nhóm con | `MATCH` | ✅ ĐẠT 3/4 nhóm (mốc · thanh toán · vụ việc) · ❓ riêng phần **tệp đính kèm**: đặc tả im lặng ⇒ `GAP` ⇒ CẦN BA |
| C3 — trạng thái "Đang thực hiện" | `MATCH` | ✅ ĐẠT |
| C4 — thông báo "Đã lưu hợp đồng" | `MATCH` | ✅ ĐẠT |
| C5 — quay về danh sách | `DIFF` | ❓ CẦN BA (chỉ ghi hiện trạng) |

**Không vế `MATCH` nào bị chứng minh là hỏng; còn 1 vế `DIFF` (C5) + 1 phần `GAP` (tệp đính kèm trong C2)**
⇒ theo bảng Verdict flow 04 + `QĐ-01`: **Verdict = Cần BA** ⇒ ô `Trạng thái dev fix` (R) = **`BA confirm`**.
Phần tệp đính kèm **không** làm đổi verdict (phiếu vốn đã route BA vì C5 `DIFF`); chỉnh cách viết chỉ để phần
diễn giải **nói đúng sự thật** và **không đổ lỗi nhầm sang phía người đo**.

> Không viết *"fix đã có tác dụng"*: phiếu chưa từng chạy, không có ảnh lỗi cũ ⇒ chỉ kết luận **hiện trạng**.

## 6. Ghi nhận (KHÔNG chấm, không kéo verdict) — gửi dev/BA

- **Nhãn nút gửi biểu mẫu đổi theo chế độ:** chế độ Thêm mới là **[Thêm mới]**, chế độ Sửa là **[Lưu]**.
  Bước J của phiếu và Phụ lục E quy ước nhãn **[Lưu]**. Phiếu này chấm theo hành vi, không chấm nhãn nút.
- **Có màn chi tiết hợp đồng ĐỘC LẬP** `/hop-dong-tv/{id}`, đường dẫn phụ đề có liên kết tới **`/hop-dong-tv`**
  (màn danh sách độc lập). Đây là dữ kiện quan trọng cho câu hỏi BA §5.1 (`:266`/`:268` nói nhóm X.3
  *"không còn là mục menu riêng"*) — **ghi lại, không chấm ở phiếu này**.
- Màn chi tiết hợp đồng có mục **"Nhật ký hoạt động"** với cột Endpoint + HTTP — vượt trên mức `:162` yêu cầu.

## 7. Quan sát ngoài vế — **candidate**, KHÔNG log thành bug

1. `nhật ký hoạt động hiện 2 dòng "Tạo mới" cho 1 lần lưu` · xuất hiện tại **bước mở lại chi tiết để đếm nhóm
   con (C2)** · artifact: ảnh 03 — dòng 1 `POST /api/v1/hop-dong-tu-vans · 201`, dòng 2 cùng mốc `14:43` nhưng
   Endpoint và HTTP đều `—`; mạng chỉ ghi nhận **1** yêu cầu lưu · **còn thiếu**: đặc tả `:162` chỉ ghi
   *"AUDIT_LOG ghi nhận"*, **im lặng** về số bản ghi nhật ký cho một giao dịch ⇒ candidate, **không** đo thêm.

> **Cổng "bug mới tự lộ"** (flow 04, luật 3): cả case **chỉ dùng 1 phép xác nhận** — mở biểu mẫu chế độ **Sửa**
> để **nhìn** xem có ô chọn tệp hay không, rồi bấm **[Hủy]**, **không lưu, không tải tệp lên**. Đã kiểm chứng
> không đổi dữ liệu: `version = 1`, `ngayCapNhat` = `ngayTao` = `2026-08-07T07:43:54.778Z`. Phép xác nhận này
> phục vụ **phần tệp của C2** (§4-C2), không phải ứng viên nào; ứng viên 1 dùng lại artifact sẵn có,
> **không** cộng thêm lượt xác nhận (luật 5).
>
> Phần tệp đính kèm **không** xếp vào mục ứng viên: nó **thuộc chính vế C2** của phiếu (đối tác nêu rõ *"tệp
> đính kèm đã nhập"*), nên xử theo vế `GAP` ở §4-C2, không xử theo gate bug mới.

## 8. Dữ liệu đã thay đổi trên môi trường (bắt buộc khai)

| Đổi gì | Bản ghi | Env | Lúc |
|---|---|---|---|
| **TẠO MỚI 1 hợp đồng tư vấn** bằng **giao diện thật** (`POST /api/v1/hop-dong-tu-vans` → 201) | **`HDTV-20260807-0006`** · `id` = `d16487f4-3ccc-4629-8e07-bb63ea9a12be` · tên *"Hợp đồng tư vấn xác lập quyền sở hữu trí tuệ và nhãn hiệu cho doanh nghiệp nhỏ và vừa"* · Bên B `Chuyên gia UAT QLNDTVVCG 38` · giá trị 250.000.000 · `07/08/2026`→`25/08/2026` · trạng thái `DANG_THUC_HIEN` · ghi chú mang dấu `QA-F8-321-20260807` | `18.143.165.120.nip.io` (**nội bộ**) | 2026-08-07 14:43:54 |
| ↳ **1 mốc tiến độ con** | `id` `c1683473-61ea-4ccc-a8f0-e0a2d6f3d75b` — `Ban giao ho so tra cuu nhan hieu` · `18/08/2026` · `CHUA_BAT_DAU` | " | " |
| ↳ **1 giai đoạn thanh toán con** | `id` `deda5d2d-6edb-4514-ab74-6b32f139b9cc` — `Dot 1 - tam ung khi ky hop dong` · `100.000.000` · `15/08/2026` · `CHUA_THANH_TOAN` | " | " |
| ↳ **3 liên kết vụ việc** (nhiều-nhiều) | `VV-BTP-TW-20260804-002` · `-003` · `-004` — **chỉ tạo liên kết**, KHÔNG sửa bản thân vụ việc | " | " |

- Đây chính là **HĐ-1** mà `chuan/02-SEED-HDTV.md` §5 giao cho phiếu `_15` dựng (D2 + D3).
- **Người đo KHÔNG nạp tệp bằng chức năng Sửa.** Lý do đầy đủ: nạp tệp **không** phải hành động tranh chấp của
  phiếu nào, nhưng phiếu **`_21` (đợt C)** tranh chấp ở chính **thao tác lưu bản sửa**, và vế C3 của `_21` đo
  *"lưu bản sửa có thay thế toàn bộ 4 danh sách con không"* — tệp phải **có sẵn TRƯỚC** thì C3 mới đo được.
  Dùng Sửa để đính kèm bây giờ vừa **tiêu thụ trước** hành động của `_21`, vừa **làm mờ** phép đo đó.
- **Điều phối đã dựng nốt D2 bằng API lúc 14:57** (SAU khi lượt đo này kết thúc lúc 14:47), phiên `cbnv_tw_05`
  để tránh tranh phiên: `POST /api/v1/hop-dong-tu-vans/d16487f4-…/files` (multipart, tên trường **`file`**) → 201,
  `tenFile` `phu-luc-hop-dong.pdf` · 1248 byte · `application/pdf` · `trangThaiQuet` `SACH`; đọc lại bản ghi thì
  `fileDinhKem` có **1** phần tử. ⚠️ **Việc seed này KHÔNG che phát hiện của phiếu `_15`** — phần "không đính
  kèm được lúc tạo" đã đo và ghi xong **trước** khi seed chạy (§4-C2, ảnh 01 và 04, mốc 14:43–14:47).
  Ghi chú kỹ thuật cho người sau: `/api/docs-json` **không** khai `requestBody` cho điểm nạp này; tên trường
  đúng là **`file`**. Chi tiết ở `chuan/02-SEED-HDTV.md` §6 và §7.
- **Không** đụng dữ liệu đối tác. **Không** sửa/xóa bản ghi nào. Biểu mẫu Sửa chỉ **mở rồi Hủy**, đã xác minh
  bản ghi giữ `version = 1`.
- Hệ quả cho các phiếu sau trong đợt A: Màn 1 của vụ việc `-002` hiện có **đúng 1** hợp đồng; tên hợp đồng
  **chứa cụm "sở hữu trí tuệ"** ⇒ `_03` cần **thêm 1 hợp đồng nữa không chứa cụm đó** trong cùng vụ việc để
  chứng minh có lọc thật (sẽ khai là dựng tiền đề).

## 9. Ảnh bằng chứng (đã mở lại xem từng ảnh trước khi dùng)

| Ảnh | Nội dung | Liên kết xem được |
|---|---|---|
| `QLHDTVVCG_15-01-du-lieu-nhap-4-nhom-con-truoc-khi-luu.png` | dữ liệu đã nhập trước khi bấm lưu: Nội dung, Ghi chú, 1 mốc tiến độ, 1 giai đoạn thanh toán (0%) | https://drive.google.com/file/d/1-Ut6CKSa2OoHCX1L1he5edygARQTPfOi/view?usp=drivesdk |
| `QLHDTVVCG_15-02-sau-khi-luu-man-dung-o-chi-tiet-vu-viec.png` | **C5** — sau khi lưu: biểu mẫu đóng, màn dừng ở Chi tiết vụ việc, bảng "HĐ tư vấn liên kết" đã có bản ghi mới | https://drive.google.com/file/d/1ce65-8s3aoiS__GLD7HyVOiz8WqBHHmk/view?usp=drivesdk |
| `QLHDTVVCG_15-03-mo-lai-chi-tiet-dem-tung-nhom-con.png` | **C2** — mở lại chi tiết: 3 vụ việc · 1 mốc tiến độ · 1 giai đoạn thanh toán · *"Chưa có tài liệu đính kèm"* · Nhật ký hoạt động | https://drive.google.com/file/d/1tbbdgTvP1J4ix0V-HTnJY80x1fB8xIH0/view?usp=drivesdk |
| `QLHDTVVCG_15-04-o-che-do-sua-moi-co-o-chon-tep-dinh-kem.png` | **C2 — phần tệp** — chế độ Sửa có vùng *"Kéo thả hoặc nhấp để chọn tệp đính kèm"* kèm ràng buộc định dạng/dung lượng, chế độ Thêm mới thì không | https://drive.google.com/file/d/1VMsiUnGvgaPLqAvEXnm_cYQBR0JB7OuH/view?usp=drivesdk |

## 10. Cổng chốt verdict — trả lời đủ 5 câu (flow 04)

1. **Hành động tranh chấp đã bấm trên giao diện thật chưa?** Rồi — nút gửi biểu mẫu ở chế độ Thêm mới, bấm
   bằng công cụ điều khiển trình duyệt thật, sinh đúng **1** `POST /api/v1/hop-dong-tu-vans` → 201.
   API **chỉ** dùng để đối chứng (đọc lại bản ghi, đọc `/api/docs-json`), **không** dùng để tạo hợp đồng.
2. **Mỗi vế có đủ 2 đường đo độc lập không?** Có — giao diện + đọc lại bản ghi từ máy chủ cho C1/C2/C3;
   quan sát thông báo + mã phản hồi cùng mốc giây cho C4. Không vế nào hai đường mâu thuẫn.
3. **Có Pass bằng quan sát tĩnh không?** Không — bản ghi do chính lượt đo này tạo ra bằng giao diện.
4. **Có hạ `DIFF`/`GAP` xuống `MATCH` không?** Không. C5 giữ `DIFF` dù web làm theo đúng SRS.
5. **Đã khai dữ liệu thay đổi chưa?** Rồi — §8, kèm mã và định danh đầy đủ để người sau truy được.
