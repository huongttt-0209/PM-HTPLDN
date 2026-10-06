# CHUẨN CHẤM — CNHSNLTVV_03 (Lô G3 · khoá TRƯỚC khi đo)

> File này khoá chuẩn chấm **TRƯỚC** khi mở màn trên env nghiệm thu. Sau khi đo, **CẤM** sửa quan hệ
> `MATCH / DIFF / GAP` hoặc đổi ngưỡng Pass/Reopen cho khớp kết quả đo được.

## 1. Bảng đầu

| Mục | Giá trị |
|---|---|
| Bảng / tab / dòng | Sheet `1OKBN2otlmdZ44THkmhtsn-_63M2Boh7zQwearwjYR3s` · tab **`bug`** · **dòng 36** |
| Mã TC | **CNHSNLTVV_03** |
| Mô tả (đối tác) | "Lưu thành công khi nhập dữ liệu hợp lệ" |
| Trạng thái nguồn | `Trạng thái` = **Fail** · `Dopai` = **dev done** · `Trạng thái dev fix` = **Test done** · `Kết quả verify` đã có (đo ở env NỘI BỘ — lô G3 phải đo lại trên env đối tác) |
| Kết quả thực tế (đối tác, nguyên văn) | *"Hệ thống hiển thị thông báo \"Lỗi hệ thống, vui lòng thử lại sau.\""* |
| Env đo | `https://htpldn-uat.ospgroup.vn` (env NGHIỆM THU của đối tác) |
| Bản dựng | **đọc trên UI khi đo** (chân sidebar `HTPLDN · Vx.y.z`) — bắt buộc **tải lại trang** rồi mới ghi |
| Tài khoản dự kiến | `nht_04_ui` / `Test@1234` — vai trò **NHT**, Cục Bổ trợ tư pháp – Bộ Tư pháp, cấp TW (`output/UAT_doi-tac/input/input.md` §"Môi trường NGHIỆM THU của đối tác"). OTP lấy ở `https://htpldn-uat.ospgroup.vn/mailhog/` |
| Vai trò theo đặc tả | **Người hỗ trợ pháp lý (NHT)** — `srs-fr-04-chuyen-gia-tvv.md:375` (*"**Tác nhân:** Người hỗ trợ pháp lý (NHT)"*), `:373` (chủ hồ sơ chỉ đọc), `:377` (TVV **cùng đơn vị** với NHT); điều kiện hiển thị tab: `:1576` |
| Màn | **SCR-IV-03 — Hồ sơ chi tiết Tư vấn viên**, **tab "Năng lực"** → form *Cập nhật năng lực* (FR-IV-04 / UC42) |
| URL dự kiến | `https://htpldn-uat.ospgroup.vn/chuyen-gia-tvv/{id}` — `srs-fr-04-chuyen-gia-tvv.md:1537` (*"**Đường dẫn:** `/chuyen-gia-tvv/:id`"*). Vào theo đúng luồng phiếu: menu **Mạng lưới Tư vấn viên → Tư vấn viên / Chuyên gia** (`/chuyen-gia-tvv/danh-sach`, `:1418`) → mở 1 hồ sơ → tab **Năng lực** |
| SRS đã đọc | `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-04-chuyen-gia-tvv.md` — **2542 dòng** |
| SRS đã đọc | `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-v3.5.md` — **7012 dòng** |

---

## 2. Nguồn đã đọc (tự mở trong lượt này)

**SRS nguồn chuẩn DUY NHẤT — `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/`:**

| File | Đoạn đã đọc trọn | Nội dung |
|---|---|---|
| `srs-fr-04-chuyen-gia-tvv.md` | `:367–435` | **FR-IV-04 Cập nhật năng lực (UC42)** — trọn mục: Tác nhân · Preconditions · 11 Inputs · 8 bước Processing · Outputs · Postconditions · **bảng Error Handling `:423–429` (E1–E5)** · 3 AC `:432–434` |
| `srs-fr-04-chuyen-gia-tvv.md` | `:438–487` | FR-IV-05 Xem chi tiết TVV (UC43) — để phân biệt vế "xem" với vế "lưu" |
| `srs-fr-04-chuyen-gia-tvv.md` | `:1533–1604` | **SCR-IV-03** trọn mục: Quyền truy cập `:1538–1541` · Header + 6 nút `:1547–1558` · 5 Tab `:1562–1583` (**tab "Năng lực" = cell 21, `:1576`**) · Quy tắc tương tác `:1585–1603` |
| `srs-fr-04-chuyen-gia-tvv.md` | `:1414–1425` | SCR-IV-01 — đường dẫn danh sách `/chuyen-gia-tvv/danh-sach` (bước 1 của phiếu) |
| `srs-fr-04-chuyen-gia-tvv.md` | `:2284–2300` | SM-TVV — các trạng thái hồ sơ TVV (để chọn hồ sơ tiền đề hợp lệ) |
| `srs-fr-04-chuyen-gia-tvv.md` | `:12–30`, `:2443–2465` | Lịch sử thay đổi + §6 Tổng quan BR sử dụng |
| `srs-v3.5.md` | `:4623` | REL-02 — *"Mọi lỗi hệ thống hiển thị thông báo thân thiện (không lộ stack trace)"* (🟡 Đề xuất) |
| `srs-fr-16-api.md` | `:168` | `ERR-API-500` — *HTTP 500 "Lỗi hệ thống nội bộ. Vui lòng thử lại sau"* — mã lỗi tầng hạ tầng, không phải kết quả nghiệp vụ hợp lệ của FR-IV-04 |

**Quét từ đồng nghĩa đã chạy trên toàn thư mục `srs-v3.5/`:** `năng lực` · `Năng lực` · `chứng chỉ` ·
`Chứng chỉ` · `chung_chi_moi` · `chung_chi_chi_tiet` · `bằng cấp` · `Lỗi hệ thống` · `lỗi hệ thống` ·
`ERR-NL-` · `Cập nhật năng lực` · `HO_SO_TU_VAN_VIEN` · `FILE_DINH_KEM` · `ClamAV`.

**Ngữ cảnh (CHỈ để biết tra chỗ nào — KHÔNG dùng làm căn cứ verdict, KHÔNG mượn số dòng, KHÔNG kế thừa verdict):**

- `output/UAT_doi-tac/batch-B7-tuvan-mangluoi-2026-08-06/tieuchi/CNHSNLTVV_03.md` + `ketqua-CNHSNLTVV_03.txt`
  — lô đo **env NỘI BỘ** `18.143.165.120.nip.io` bản dựng `V1.0.8` ngày 06/08. Chỉ dùng để biết **chỗ cần
  bấm** và **cảnh cần dựng lại**.
- **Lời DEV (ngữ cảnh, KHÔNG phải căn cứ):** dev khai đã verify E2E pass, tác nhân `nht_qa_tw`, hồ sơ
  `TVV-BTP-TW-0002`, `PATCH …/nang-luc` HTTP 200, *"happy-path được khắc phục nhờ nhóm CNHSNLTVV_02"*.
  ⇒ **Cảnh dev khai là nhánh KHÔNG đính tệp chứng chỉ mới** — không phủ được cảnh trong ảnh của đối tác
  (ảnh có 1 tệp đang đính). Không được dùng lời khai này để bỏ bước đo.

---

## 3. Cổng bằng chứng

**CÓ bằng chứng đối tác — đã MỞ XEM full-res:**
[`output/UAT_doi-tac/batch-B7-tuvan-mangluoi-2026-08-06/partner-evidence/CNHSNLTVV_03.jpg`](../../../batch-B7-tuvan-mangluoi-2026-08-06/partner-evidence/CNHSNLTVV_03.jpg)
(1 ảnh tĩnh, không có video).

| Vị trí trên ảnh | Nội dung đọc được |
|---|---|
| Thanh địa chỉ | `htpldn-uat.ospgroup.vn/chuyen-gia-tvv/b88271a7-34a4-4c43-9133-71342ba73d3e` ⇒ **đúng env nghiệm thu, đúng màn SCR-IV-03** |
| Đường dẫn điều hướng | `Trang chủ / Mạng lưới Tư vấn viên / Chi tiết` |
| Thông báo (khung đỏ, giữa trên) | **"Lỗi hệ thống, vui lòng thử lại sau."** — trùng khít ô *Kết quả thực tế* của phiếu |
| Khối đang mở | `Lĩnh vực pháp luật` — 9 thẻ: Thuế · Lao động · Đất đai · Dân sự · Thương mại · Hành chính · Sở hữu trí tuệ · Doanh nghiệp · Đầu tư |
| Khối kế | `Chứng chỉ hiện có` → **"Chưa có chứng chỉ nào."** |
| Khối kế | `Thêm chứng chỉ mới (PDF, tối đa 10 file)` + vùng kéo thả ghi *"Tối đa 10 tệp. Định dạng: .pdf, .doc, .docx, .xls, .xlsx, .jpg, .png. Dung lượng tối đa: 20MB/tệp."* |
| Hàng tệp đã đính | **`2K15 T3 (4.8) & CN (9.8).pdf` — `(258.2 KB)`** + 2 điều khiển `Xem` / `Xóa` |
| Khối kế | `Ghi chú cập nhật` = **`a`** (bộ đếm `1 / 2000`) |
| Cuối form | 2 nút: `Làm lại` · **`Lưu`** |
| Góc phải trên | `BTP · DP` · chuông 4 · **`hương 3 NHT`** · huy hiệu **`NHT`** |
| Chân sidebar | **`HTPLDN · V1.0.3`** |
| Đồng hồ máy | `03:42 PM · 2026-08-03` |

**Neo lấy được từ bằng chứng (bắt buộc dựng lại khi đo):**

1. Vai trò **NHT** (khớp `srs-fr-04:375`).
2. Màn **SCR-IV-03 / form Cập nhật năng lực**, không phải màn thêm mới TVV (SCR-IV-02).
3. **Có ít nhất 1 tệp chứng chỉ mới đang đính** tại thời điểm bấm `Lưu` — đây là điều kiện quyết định,
   **không được bỏ**.
4. Có nhập `Ghi chú cập nhật` (đối tác nhập `a`).
5. Khối `Chứng chỉ hiện có` đang rỗng ("Chưa có chứng chỉ nào.") trước khi lưu.

**Khác biệt buộc phải khai trong báo cáo (nới điều kiện, không phải GAP):** đối tác đứng ở đơn vị
**`BTP · DP`**; env nghiệm thu chỉ cấp cho QA tài khoản NHT cấp **TW** (`nht_04_ui`). `srs-fr-04:377` +
`:1576` ràng buộc **NHT chỉ thao tác trên TVV cùng đơn vị** ⇒ QA phải chọn hồ sơ TVV thuộc đơn vị của
`nht_04_ui`. Ghi rõ: *"đo ở cùng vai trò NHT, khác cấp đơn vị"*. **CẤM** đăng nhập `admin` để "cho ra
kết quả" — vai trò của vế là NHT.

---

## 4. BUG SCOPE LOCK

Expected đối tác (nguyên văn): **"Thực hiện lưu lại dữ liệu đã cập nhật"**.
⇒ Mệnh đề gồm **2 vế nối tiếp**: (i) thao tác lưu **thực hiện được** (không bị chặn bằng thông báo lỗi hệ
thống) và (ii) dữ liệu **thật sự được lưu lại**. Chỉ đạt (i) mà không đạt (ii) = **chưa thoả**.

| Vế | Quan hệ với SRS | Route |
|---|---|---|
| **C1** — thao tác lưu ở form Cập nhật năng lực, **có đính tệp chứng chỉ mới** (đúng cảnh ảnh), không bị từ chối bằng thông báo lỗi hệ thống | **MATCH** (`:388` cho phép `chung_chi_moi`; `:433` AC nói rõ *"cập nhật thông tin/chứng chỉ + upload file → lưu thành công"*) | **TEST** |
| **C2** — dữ liệu đã nhập **được ghi thật** vào hồ sơ năng lực, còn nguyên sau khi tải lại trang | **MATCH** (`:402`, `:418`) | **TEST** |
| **C3** — tệp chứng chỉ mới đính kèm **được lưu vào hồ sơ** cùng lượt lưu đó | **MATCH** (`:403` — *"Nếu có file mới: tạo bản ghi FILE_DINH_KEM"*) | **TEST** |

### Trích nguyên văn SRS dưới từng vế

**C1 — `Docs-PM-HTPLDN/…/srs-v3.5/srs-fr-04-chuyen-gia-tvv.md:388`** (Inputs, dòng 6):

```
| 6 | chung_chi_moi | binary[] | N | PDF, max 10MB/file, tổng 50MB, max 10 files | — | user upload |
```

**C1 — `srs-fr-04-chuyen-gia-tvv.md:433`** (Acceptance Criteria):

```
- **Given** NHT cập nhật thông tin/chứng chỉ + upload file **When** lưu **Then** validate và lưu thành công
```

**C1 — `srs-fr-04-chuyen-gia-tvv.md:423–429`** (toàn bộ bảng Error Handling của FR-IV-04 — **5 điều kiện
lỗi hợp lệ duy nhất**, không có điều kiện nào là "lỗi hệ thống"):

```
| # | Điều kiện lỗi | Mã lỗi | Phản hồi hệ thống | Severity |
|---|--------------|--------|-------------------|----------|
| E1 | NHT không cùng đơn vị với TVV | ERR-NL-01 | "Bạn không có quyền cập nhật hồ sơ tư vấn viên này (khác đơn vị)" | ERROR |
| E2 | File vượt 10MB/file | ERR-NL-02 | "File tải lên tối đa 10MB/file" | ERROR |
| E3 | File vượt tổng 50MB | ERR-NL-03 | "Tổng dung lượng file tối đa 50MB" | ERROR |
| E4 | Virus scan phát hiện | ERR-NL-04 | "File {ten_file} chứa mã độc, bị từ chối" | ERROR |
| E5 | TVV đã VO_HIEU_HOA | ERR-NL-05 | "Hồ sơ đã bị vô hiệu hóa, không thể chỉnh sửa" | ERROR |
```

→ Dữ liệu **nằm trong ràng buộc Inputs `:383–:393`** + không rơi vào E1–E5 ⇒ **hệ thống phải lưu**.
"Lỗi hệ thống, vui lòng thử lại sau." không thuộc 5 điều kiện trên; `srs-fr-16-api.md:168` xếp thông điệp
này vào **`ERR-API-500` — lỗi server nội bộ**, tức không phải phản hồi nghiệp vụ hợp lệ.

**C2 — `srs-fr-04-chuyen-gia-tvv.md:402` + `:418`:**

```
| 4 | Cập nhật thông tin năng lực trong HO_SO_TU_VAN_VIEN | — |
```
```
- Hồ sơ năng lực được cập nhật
```

**C3 — `srs-fr-04-chuyen-gia-tvv.md:403`:**

```
| 5 | Nếu có file mới: tạo bản ghi FILE_DINH_KEM | — |
```

---

## 5. Tiền đề phải dựng

| # | Tiền đề | Cách thoả (env đối tác **cho phép seed qua API cookie-auth**) |
|---|---|---|
| T1 | Đăng nhập đúng vai trò **NHT** | `nht_04_ui` / `Test@1234` → lấy mã 6 số ở `https://htpldn-uat.ospgroup.vn/mailhog/api/v2/messages?limit=5`. **Giới hạn 5 lượt đăng nhập / 60 giây** — không thử mật khẩu bừa. Lock → Rule 7: fallback **cùng vai trò + cùng cấp**, ghi account thực dùng; hết sibling → BLOCKED, hỏi lead |
| T2 | Xác nhận vai trò + đơn vị thực tế của phiên | Đọc `/api/v1/auth/me` → phải có `vaiTro` chứa `NHT` + ghi lại `donViId`, `capDonVi`. Ghi vào nhật ký đo |
| T3 | **Có ≥1 hồ sơ TVV/CG cùng đơn vị với NHT, trạng thái KHÁC "Vô hiệu hóa"** | Mở `/chuyen-gia-tvv/danh-sach`, lọc theo đơn vị của T2. Xác nhận tab **Năng lực** + nút *"Cập nhật năng lực"* hiện ra (`:1576`). Nếu 0 hồ sơ hợp lệ → **seed**: tra endpoint thật ở `GET /api/docs-json` (mở được không cần auth) tìm nhóm `tu-van-vien`, tạo hồ sơ ứng viên theo FR-IV-03 rồi đưa về trạng thái cho phép sửa. **CẤM đoán đường dẫn endpoint** |
| T4 | **1 tệp PDF hợp lệ để đính** — trong ràng buộc `:388` (PDF, ≤10MB) | Tạo tệp PDF nhỏ (< 1MB). Chạy **2 lượt**: (a) tên tệp **giống ảnh đối tác** `2K15 T3 (4.8) & CN (9.8).pdf` (có dấu cách + ngoặc + `&`); (b) tên tệp **thường** `G3-CNHSNLTVV03-chungchi-A.pdf` — để phân biệt "lỗi do tên tệp" với "lỗi do có tệp" |
| T5 | Ghi chú cập nhật ≤ 2000 ký tự (`:393`) | Nhập chuỗi ngắn có mốc giờ, ví dụ `G3 CNHSNLTVV03 2026-08-07` |
| T6 | **Bộ bắt thông báo đã cài TRƯỚC khi bấm [Lưu]** | `output/UAT_doi-tac/tools/toast-capture.js` — cài lại sau **mỗi** lần tải lại trang / chuyển màn; tự kiểm `soObserverDangSong = 1`; **CẤM lọc trùng**, **CẤM `textContent`**; đếm kèm số lời gọi mạng |
| T7 | Ghi **env + bản dựng** sau khi tải lại trang | Chuỗi `HTPLDN · Vx.y.z` ở chân sidebar + bó mã FE (`assets/index-*.js`) |
| T8 | **Kế hoạch hoàn nguyên** (env NGHIỆM THU của đối tác — dữ liệu không phải của QA) | Trước khi sửa: chụp mốc gốc hồ sơ (đọc lại `GET` chi tiết hồ sơ, lưu JSON vào `do/`). Sau khi đo: trả về đúng mốc gốc + **xoá tệp rác** nếu lượt lưu hỏng vẫn để lại tệp đính kèm. Khai đủ trong báo cáo: **đổi bản ghi nào · đổi gì · env nào**. Ưu tiên seed hồ sơ QA mới thay vì sửa hồ sơ có sẵn |

**Nếu T3 hoặc T4 không dựng được → KHÔNG Pass.** Ghi rõ dữ kiện còn thiếu (BRIEF §4 luật 7).

---

## 6. Bảng chuẩn chấm

| # | Điều kiện BUG GỐC | Đặc tả (`file:dòng` nguyên văn) | Phép đo quyết định | Pass khi | Reopen khi |
|---|---|---|---|---|---|
| **C1** | Ở form *Cập nhật năng lực* (tab Năng lực, SCR-IV-03), NHT nhập dữ liệu hợp lệ **và đang đính 1 tệp chứng chỉ mới** rồi bấm `Lưu` → đối tác nhận **"Lỗi hệ thống, vui lòng thử lại sau."** | `srs-fr-04-chuyen-gia-tvv.md:433` — *"**Given** NHT cập nhật thông tin/chứng chỉ + upload file **When** lưu **Then** validate và lưu thành công"*; `:388` — *"chung_chi_moi \| binary[] \| N \| PDF, max 10MB/file, tổng 50MB, max 10 files"*; `:423–429` — bảng Error Handling **chỉ có E1–E5**, không có điều kiện "lỗi hệ thống" | Cài bộ bắt thông báo → bấm `Lưu` **1 lần** → đọc **nguyên văn** thông báo bắt được (innerText, không lọc trùng) + đếm số lời gọi ghi kèm theo + đọc **mã trạng thái & thân phản hồi** của chính lời gọi ghi đó | Không xuất hiện thông báo lỗi hệ thống; lời gọi ghi trả mã thành công. Lặp đủ **2 lượt T4(a) tên tệp đặc biệt + T4(b) tên tệp thường**, cả 2 đều thành công | Còn ≥1 lượt hiện *"Lỗi hệ thống, vui lòng thử lại sau."* (hoặc thông báo lỗi khác **không** thuộc E1–E5 `:425–429`) / lời gọi ghi trả lỗi 5xx |
| **C2** | KQ mong đợi *"Thực hiện lưu lại dữ liệu đã cập nhật"* — dữ liệu phải còn sau khi lưu | `srs-fr-04-chuyen-gia-tvv.md:402` — *"Cập nhật thông tin năng lực trong HO_SO_TU_VAN_VIEN"*; `:418` — *"Hồ sơ năng lực được cập nhật"* | **Tải lại trang** rồi mở lại tab Năng lực, đọc từng trường vừa nhập. Đối chứng độc lập: đọc lại hồ sơ bằng lời gọi chi tiết (lấy đường dẫn từ `list_network_requests` / `/api/docs-json`, **không đoán**) và so từng chữ | Mọi trường vừa nhập hiện đúng trên màn **và** khớp dữ liệu máy chủ sau khi tải lại | Toast báo thành công nhưng sau khi tải lại dữ liệu **trở về giá trị cũ** / máy chủ không đổi |
| **C3** | Ảnh đối tác cho thấy tệp `2K15 T3 (4.8) & CN (9.8).pdf` đang đính lúc bấm `Lưu`; khối `Chứng chỉ hiện có` đang rỗng | `srs-fr-04-chuyen-gia-tvv.md:403` — *"Nếu có file mới: tạo bản ghi FILE_DINH_KEM"* | Sau khi tải lại: đếm số tệp chứng chỉ trên hồ sơ trước/sau lượt lưu; đối chứng bằng dữ liệu hồ sơ trả về từ máy chủ | Tệp vừa đính **có mặt** trên hồ sơ sau khi tải lại (đúng tên tệp) | Lượt lưu báo thành công nhưng tệp không được gắn vào hồ sơ / tệp bị nhân bản mỗi lần bấm lại |

**Quy tắc gộp:** **fix một phần = Reopen** (BRIEF §4 luật 8). C1 đạt mà C2 hoặc C3 không đạt ⇒ **Reopen**.

---

## 7. Bẫy đã biết

**Chặn PASS oan:**

- **(a) 🔴 Bẫy nguy hiểm nhất — đo nhánh KHÔNG đính tệp.** Lời khai của dev (*"E2E pass, PATCH trả 200"*)
  và lượt đo cũ ở env nội bộ đều cho thấy **nhánh không đính tệp chứng chỉ mới vẫn lưu bình thường**;
  chỉ nhánh **có** tệp chứng chỉ mới mới sinh lỗi. Bấm `Lưu` khi form không có tệp → thành công → **Pass
  oan**. Ảnh của đối tác có tệp đang đính ⇒ **bắt buộc dựng lại đúng cảnh đó**.
- **(b) Toast tự tắt.** Lớp nổi sống < 5s → cài `toast-capture.js` **TRƯỚC** khi bấm; **CẤM lọc trùng**
  (lọc trùng che double-toast → Pass oan); đọc bằng `innerText`, **không** `textContent` (gom node ẩn →
  bug ma). Không bắt được thông báo → dùng **thân phản hồi của chính lời gọi ghi** làm bằng chứng mạnh
  hơn ảnh; **không bấm lại chỉ để chụp lại**.
- **(c) "Lưu được" ≠ "lưu đúng".** CẤM dừng ở toast thành công. Bắt buộc **tải lại trang + đọc lại**
  (C2) và đối chứng bằng dữ liệu máy chủ.
- **(d) Trang cũ / bản dựng cũ.** Tab mở lâu vẫn chạy mã cũ → **tải lại trang** đầu lô đo và **ghi tên
  bản dựng**; ảnh của đối tác là `V1.0.3`, bản trên env hiện tại **khác** ⇒ không suy verdict từ bản cũ.

**Chặn FAIL oan / Reopen oan:**

- **(e) 5 lỗi hợp lệ theo `:425–429` KHÔNG phải bug.** Nếu hệ thống từ chối vì *khác đơn vị*
  (`ERR-NL-01`), *tệp > 10MB* (`ERR-NL-02`), *tổng > 50MB* (`ERR-NL-03`), *nhiễm mã độc* (`ERR-NL-04`),
  *hồ sơ đã vô hiệu hóa* (`ERR-NL-05`) → **đúng đặc tả**, không được chấm Reopen. Vì vậy T3/T4 phải chọn
  hồ sơ **cùng đơn vị, chưa vô hiệu hóa** và tệp **PDF < 10MB**.
- **(f) Định dạng tệp — lệch giữa UI và đặc tả, NGOÀI phạm vi vế này.** Vùng kéo thả trên ảnh ghi
  *".pdf, .doc, .docx, .xls, .xlsx, .jpg, .png · 20MB/tệp"* trong khi `:388` ghi *"PDF, max 10MB/file,
  tổng 50MB"*. Đây là **candidate tài liệu/giao diện riêng**, ghi 1 dòng vào `note/`; **CẤM** dùng làm
  căn cứ Reopen cho CNHSNLTVV_03, và **CẤM** cố tình nạp `.docx`/tệp 15MB rồi gọi là tái hiện.
- **(g) Nhầm màn.** `Sửa hồ sơ` (`:1552` → SCR-IV-02) là màn **khác** với form *Cập nhật năng lực*
  (`:1576`, tab Năng lực). Lưu ở SCR-IV-02 thành công **không** chứng minh gì cho case này.
- **(h) Nhầm vai.** Tab Năng lực + nút *Cập nhật năng lực* chỉ mở cho **Người hỗ trợ** (`:1576`); chủ hồ
  sơ TVV/CG chỉ đọc (`:373`). Không có nút ≠ bug nếu đang đăng nhập sai vai — kiểm `/auth/me` trước.
- **(i) Hồ sơ ở YEU_CAU_BO_SUNG sẽ đổi trạng thái sau khi lưu** (`:405` — chuyển về DANG_THAM_DINH).
  Đây là hành vi **đúng đặc tả**, không phải hiệu ứng phụ sai.

**Bẫy dữ liệu (env NGHIỆM THU của đối tác):**

- **(j) Lượt lưu hỏng có thể vẫn để lại tệp rác trên hồ sơ** (bước nạp tệp và bước lưu là 2 lời gọi tách
  rời). Sau mỗi lượt hỏng phải **đếm lại số tệp** và **dọn tệp rác**; ghi rõ trong nhật ký đo.
- **(k) Không thao tác lan man trên dữ liệu đối tác.** Ưu tiên hồ sơ do QA seed. Mọi thay đổi phải hoàn
  nguyên theo T8 và khai đủ 3 thông tin: bản ghi nào · đổi gì · env nào.
- **(l) Hai phép đo mâu thuẫn = CHƯA chốt.** Ví dụ giao diện báo lỗi nhưng máy chủ trả mã thành công và
  dữ liệu đã đổi → ghi cả hai, hỏi lead, không tự chốt.

---

## 8. Bảng quyết định đã cam kết TRƯỚC khi đo

| Quan sát ở lượt đo | Verdict logic |
|---|---|
| C1 + C2 + C3 đều đạt ở **cả 2 lượt** tệp (tên đặc biệt + tên thường) | **Pass** — ghi rõ env + bản dựng đã đo là phạm vi hiệu lực |
| Còn ≥1 lượt hiện *"Lỗi hệ thống, vui lòng thử lại sau."* khi có tệp chứng chỉ mới | **Reopen** (C1 không đạt) |
| Lưu báo thành công nhưng tải lại thấy dữ liệu **không đổi** | **Reopen** (C2 không đạt) |
| Lưu báo thành công nhưng **tệp chứng chỉ không được gắn** vào hồ sơ | **Reopen** (C3 không đạt) |
| Hệ thống từ chối bằng đúng 1 trong 5 thông báo `:425–429` do QA nhập sai tiền đề | **Chưa chốt** — sửa tiền đề (T3/T4) rồi đo lại; **không** ghi verdict |
| Không dựng được hồ sơ TVV cùng đơn vị (T3) hoặc không đính được tệp (T4) | **Chưa chốt** — nêu rõ dữ kiện còn thiếu, **CẤM Pass** |
| Giao diện và máy chủ mâu thuẫn | **Chưa chốt** — ghi cả hai, hỏi lead |
