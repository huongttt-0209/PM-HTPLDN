# CHUẨN CHẤM — TKHSYCHTPL_03 (Lô G3 · khoá TRƯỚC khi đo)

> File này khoá chuẩn chấm **TRƯỚC** khi mở màn trên env nghiệm thu. Sau khi đo, **CẤM** sửa quan hệ
> `MATCH / DIFF / GAP` hoặc đổi ngưỡng Pass/Reopen cho khớp kết quả đo được.

## 1. Bảng đầu

| Mục | Giá trị |
|---|---|
| Bảng / tab / dòng | Sheet `1OKBN2otlmdZ44THkmhtsn-_63M2Boh7zQwearwjYR3s` · tab **`bug`** · **dòng 50** |
| Mã TC | **TKHSYCHTPL_03** |
| Mô tả (đối tác) | "Tìm kiếm bộ lọc có kết quả" |
| Trạng thái nguồn | `Trạng thái` = **Fail** · `Trạng thái dev fix` = **Test done** · `Kết quả verify` đã có (đo ở env NỘI BỘ — lô G3 phải đo lại trên env đối tác) |
| Kết quả thực tế (đối tác, nguyên văn) | *"Khi chọn Mức SLA là \"Sắp hết hạn\" hệ thống hiển thị thông báo lỗi"* |
| Env đo | `https://htpldn-uat.ospgroup.vn` (env NGHIỆM THU của đối tác) |
| Bản dựng | **đọc trên UI khi đo** (chân sidebar `HTPLDN · Vx.y.z`) — bắt buộc **tải lại trang** rồi mới ghi |
| Tài khoản dự kiến | `cbnv_tw` / `Test@1234` — vai trò **CB_NV_TW**, `donViId …8000-000000000001`, cấp TW (`output/UAT_doi-tac/input/input.md` §"Môi trường NGHIỆM THU của đối tác"). **Trùng khít vai trò + cấp của đối tác trong bằng chứng.** OTP ở `https://htpldn-uat.ospgroup.vn/mailhog/` |
| Vai trò theo đặc tả | **CB NV (TW/BN/ĐP)** — `srs-fr-05-vu-viec.md:94` (*"**Tác nhân:** CB NV (TW/BN/ĐP)"* của FR-V.I-01); FR-V.I-08 PRE-01 `:647`; phạm vi dữ liệu `:2450` (BR-AUTH-03/04 — TW xem toàn quốc) |
| Màn | **SCR-V.I-01 — Danh sách Hồ sơ Vụ việc** (thanh lọc + bảng + phân trang) |
| URL dự kiến | `https://htpldn-uat.ospgroup.vn/vu-viec/danh-sach` — vào theo đúng luồng phiếu: menu **Vụ việc HTPL** → chọn giá trị ở ô lọc **Mức SLA** |
| SRS đã đọc | `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-05-vu-viec.md` — **2506 dòng** |
| SRS đã đọc | `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-v3.5.md` — **7012 dòng** |

---

## 2. Nguồn đã đọc (tự mở trong lượt này)

**SRS nguồn chuẩn DUY NHẤT — `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/`:**

| File | Đoạn đã đọc trọn | Nội dung |
|---|---|---|
| `srs-fr-05-vu-viec.md` | `:636–700` | **FR-V.I-08 Tìm kiếm hồ sơ (UC58)** — trọn mục: PRE `:645–647` · **Inputs 7 tiêu chí `:651–659`** · Processing `:663–668` (**bước 4 = phân trang 20/trang**) · **Outputs `:672–684` (dòng 9 `muc_sla`, dòng 11 `total_count`)** · **Error Handling `:690–693`** · **AC `:695–698`** |
| `srs-fr-05-vu-viec.md` | `:87–157` | FR-V.I-01 Quản lý hồ sơ yêu cầu HTPL (UC51) — Tác nhân `:94`, Inputs `muc_sla` `:114`, Processing `:124–125`, Error `:149` |
| `srs-fr-05-vu-viec.md` | `:1626–1667` | **SCR-V.I-01** trọn mục: 24 thành phần `:1634–1659` (**ô lọc Mức SLA = `:1644`**, cột Cảnh báo thời hạn = `:1656`, **phân trang = `:1659`**) + Quy tắc tương tác `:1661–1667` (`:1664` — ngưỡng 4 mức) |
| `srs-fr-05-vu-viec.md` | `:1490–1567` | §B Bảng ánh xạ mã DB → nhãn tiếng Việt — **bảng "Mức cảnh báo thời hạn" `:1511–1518` (dòng `SAP_HET` = `:1516`)** |
| `srs-fr-05-vu-viec.md` | `:1575–1599` | §D Trạng thái dữ liệu chung (`:1580` rỗng, `:1583` lỗi tải) + §E Thông báo chung — dùng để **phân biệt "danh sách rỗng" với "báo lỗi"** |
| `srs-fr-05-vu-viec.md` | `:1423–1467` | FR-V.I-CROSS-01 Cấu hình SLA — job 30 phút `:1435`, **bảng 4 mức `:1444–1451`** |
| `srs-fr-05-vu-viec.md` | `:2004–2047`, `:2392–2396`, `:2436–2446` | Entity VU_VIEC (**ràng buộc `muc_do_canh_bao` = `:2031`**) · BR-DATA-07 · BR-SLA-01/02/03 |
| `srs-v3.5.md` | `:5571` | Phụ lục B — **BR-DATA-07 Pagination** (nguyên văn ở §4) |
| `srs-v3.5.md` | `:5626` | Phụ lục B — BR-SLA-02 (dùng để đối chiếu mã enum, xem §7 bẫy (f)) |

**Quét từ đồng nghĩa đã chạy trên toàn thư mục `srs-v3.5/`:** `Mức SLA` · `muc_sla` · `Sắp hết hạn` ·
`SAP_HET` · `SAP_HET_HAN` · `muc_do_canh_bao` · `cảnh báo thời hạn` · `Cảnh báo SLA` · `phân trang` ·
`Pagination` · `20 bản ghi` · `20/trang` · `total_count` · `Không tìm thấy` · `Chưa có dữ liệu`.

**Ngữ cảnh (CHỈ để biết tra chỗ nào — KHÔNG dùng làm căn cứ verdict, KHÔNG mượn số dòng, KHÔNG kế thừa
verdict):** `output/UAT_doi-tac/reverify-week-2/verify1-conlai-2026-08-03/cond/TKHSYCHTPL_03.md` ·
`.../reverify-audit/TKHSYCHTPL_03.md` · `.../notes/TKHSYCHTPL_03.txt` — lượt đo cũ, **bản dựng `V1.0.5`**,
không phải bản đang chạy trên env nghiệm thu.

---

## 3. Cổng bằng chứng

**CÓ bằng chứng đối tác (video) — đã trích và đọc khung hình:**
`output/UAT_doi-tac/reverify-week-2/verify1-conlai-2026-08-03/partner-evidence/TKHSYCHTPL_03.webm`
→ khung hình đã trích sẵn tại
[`.../frames/TKHSYCHTPL_03/`](../../../reverify-week-2/verify1-conlai-2026-08-03/frames/TKHSYCHTPL_03/)
(21 khung, bước ~0,5s). Công cụ trích: `output/UAT_doi-tac/tools/extract_frames.py`.

**Khung `t008.07s.jpg` (khung quyết định) đọc được:**

| Vị trí trên khung hình | Nội dung đọc được |
|---|---|
| Thanh địa chỉ | `htpldn-uat.ospgroup.vn/vu-viec/danh-sach?**mucSla=SAP_HET_HAN**&page=1` |
| **Thông báo (khung đỏ, giữa trên)** | **`mucSla must be one of the following values: BINH_THUONG, SAP_HET, QUA_HAN, QUA_HAN_NGHIEM_TRONG`** |
| Góc phải trên | `BTP · TW` · chuông `99+` · **`Cán bộ NV Trung ương`** · huy hiệu **`CB_NV_TW`** |
| Chân sidebar | **`HTPLDN · V1.0.2`** |
| Tiêu đề màn | `Vụ việc HTPL` + `[+ Nhập thủ công]` `[Xuất Excel]` (mờ) `[Làm mới]` |
| Thanh lọc | ô từ khoá `Tìm theo mã VV hoặc tên DN...` **trống** · `Lĩnh vực PL` **trống** · `Đơn vị` **trống** · `Kênh tiếp nhận` **trống** · **`Sắp hết hạn`** (ô Mức SLA) · chip `Bộ lọc nâng cao (3)` đang thu gọn · `[Xóa bộ lọc]` `[Tìm kiếm]` |
| Tab | 6 tab `Tất cả` (đang chọn) / `Chờ tiếp nhận` / `Đang xử lý` / `Chờ phê duyệt` / `Hoàn thành` / `Từ chối` |
| Bảng | cột `Mã vụ việc` · `Kênh tiếp nhận` · `Trạng thái` · `Người xử lý / Tổ chức` · `Ngày tiếp nhận` · `Thời hạn xử lý` · `Cảnh báo thời hạn` · `Hành động`; vùng dữ liệu hiện icon rỗng + **"Không tìm thấy hồ sơ phù hợp"** |
| Đồng hồ máy | `09:08 AM · 2026-07-30` |

**Neo lấy được từ bằng chứng (bắt buộc dựng lại khi đo):**

1. Vai trò **CB_NV_TW**, đơn vị **BTP · TW** — QA dùng `cbnv_tw`, **trùng khít**, không có khoảng lệch.
2. Màn **Vụ việc HTPL / Danh sách**, tab **Tất cả**.
3. **Chỉ đặt 1 ô lọc: Mức SLA = "Sắp hết hạn"**; mọi ô lọc khác để trống.
4. Triệu chứng là **khung thông báo lỗi**, **không phải** danh sách rỗng (bảng rỗng chỉ là hệ quả).
5. Bản dựng của đối tác là **`V1.0.2`** — bản trên env hiện tại **khác** ⇒ phải tự đọc lại bản dựng.

---

## 4. BUG SCOPE LOCK — tách 3 vế

Expected đối tác (nguyên văn): **"Có kết quả, hệ thống hiển thị danh sách kết quả tìm kiếm, phân trang 20
bản ghi mỗi trang."** ⇒ **3 vế nối tiếp**, kèm điều kiện đầu vào của chính phiếu: *"2. Tồn tại bản ghi phù
hợp với tiêu chí tìm kiếm"*.

| Vế | Nội dung | Quan hệ với SRS | Route |
|---|---|---|---|
| **S1** | Chọn Mức SLA = "Sắp hết hạn" **không bị hệ thống từ chối bằng thông báo lỗi** | **MATCH** — `:1644` liệt kê giá trị này là 1 trong 4 lựa chọn hợp lệ của ô lọc; `:690–693` chỉ cho phép 2 phản hồi lỗi (`INF-VV-TK-01` khi không có kết quả, `ERR-VV-TK-01` khi ngày sai) | **TEST** |
| **S2** | Hệ thống **hiển thị danh sách kết quả** đúng tiêu chí lọc | **MATCH** — `:696–697` (AC) + `:672–684` (Outputs, có `muc_sla` và `total_count`) | **TEST** |
| **S3** | **Phân trang 20 bản ghi mỗi trang** | **MATCH** — `:668` + `:1659` + `:2394` + `srs-v3.5.md:5571` | **TEST** |

### Trích nguyên văn SRS dưới từng vế

**S1 — `Docs-PM-HTPLDN/…/srs-v3.5/srs-fr-05-vu-viec.md:1644`** (SCR-V.I-01 §Thành phần màn hình, dòng 9;
header cột `:1634` = `| # | Vùng | Thành phần | Loại | Dữ liệu / Nội dung | Hành vi | Điều kiện hiển thị |`):

```
| 9 | filter-bar | Mức SLA | C10 dropdown | BINH_THUONG / SAP_HET / QUA_HAN / QUA_HAN_NGHIEM_TRONG | change → filter | Luôn |
```

**S1 — `srs-fr-05-vu-viec.md:1516`** (§B Bảng ánh xạ mã DB → nhãn hiển thị tiếng Việt, bảng "Mức cảnh báo
thời hạn (`VU_VIEC.muc_do_canh_bao`)"; header `:1513` = `| Mã DB | Nhãn UI | Màu |`):

```
| `SAP_HET` | Sắp hết hạn | Vàng |
```

**S1 — `srs-fr-05-vu-viec.md:690–693`** (toàn bộ bảng Error Handling của FR-V.I-08 — **chỉ 2 dòng**):

```
| # | Điều kiện lỗi | Mã lỗi | Phản hồi hệ thống | Severity |
|---|--------------|--------|-------------------|----------|
| E1 | Không có kết quả | INF-VV-TK-01 | "Không tìm thấy hồ sơ phù hợp" | INFO |
| E2 | tu_ngay > den_ngay | ERR-VV-TK-01 | "Ngày bắt đầu phải trước ngày kết thúc" | ERROR |
```

→ **Không có điều kiện lỗi nào cho việc chọn một giá trị hợp lệ ở ô Mức SLA.** Bộ lọc không ra kết quả
thì phản hồi đúng là **INFO "Không tìm thấy hồ sơ phù hợp"**, không phải khung báo lỗi.

**S2 — `srs-fr-05-vu-viec.md:696–698`** (FR-V.I-08 §Acceptance Criteria):

```
- **Given** CB NV nhập từ khóa (mã HS/tên DN) **When** tìm kiếm **Then** hiển thị kết quả, phân trang
- **Given** CB NV lọc theo lĩnh vực/trạng thái/thời gian **When** áp dụng **Then** kết quả lọc
- **Given** CB NV kết hợp nhiều điều kiện **When** tìm kiếm **Then** áp dụng AND
```

**S2 — `srs-fr-05-vu-viec.md:2031`** (Entity VU_VIEC — ràng buộc giá trị lưu trữ, dùng để đối chứng bản
ghi lọt bộ lọc):

```
| muc_do_canh_bao | text | N | CHECK IN ('BINH_THUONG','SAP_HET','QUA_HAN','QUA_HAN_NGHIEM_TRONG') | 'BINH_THUONG' | Mức cảnh báo SLA |
```

**S3 — `srs-fr-05-vu-viec.md:668`** (FR-V.I-08 §Processing, bước 4):

```
| 4 | Phân trang (20/trang) | BR-DATA-07 |
```

**S3 — `srs-fr-05-vu-viec.md:1659`** (SCR-V.I-01 §Thành phần, dòng 24):

```
| 24 | pagination | Phân trang | C05 | "Hiển thị 1-20 / N kết quả". Mặc định 20/trang | click → chuyển trang | Luôn |
```

**S3 — `srs-v3.5.md:5571`** (Phụ lục B.2; header cột `:5563` =
`| ID | Phát biểu quy tắc | Nguồn | Áp dụng FR | Ngoại lệ | Kiểm chứng |`):

```
| BR-DATA-07 | **Pagination:** Mọi danh sách sử dụng phân trang. Default: 20 rows/page, max: 100 rows/page | UX-Spec | Toàn bộ list | Dashboard (nhóm I): không phân trang | Verify API response |
```

---

## 5. Tiền đề phải dựng

🔴 **Điều kiện #2 của chính phiếu — *"Tồn tại bản ghi phù hợp với tiêu chí tìm kiếm"* — là tiền đề BẮT
BUỘC.** Không có bản ghi mức "Sắp hết hạn" trong phạm vi tài khoản đo thì phép đo **không nói được gì về
case này** (danh sách rỗng là hành vi đúng theo `:692`), và **CẤM Pass**.

| # | Tiền đề | Cách thoả (env đối tác **cho phép seed qua API cookie-auth**) |
|---|---|---|
| T1 | Đăng nhập đúng vai trò **CB_NV_TW** | `cbnv_tw` / `Test@1234` → mã 6 số ở `https://htpldn-uat.ospgroup.vn/mailhog/api/v2/messages?limit=5`. **5 lượt / 60 giây**. Lock → Rule 7 fallback **cùng vai trò + cùng cấp**, ghi account thực dùng |
| T2 | Xác nhận vai trò + đơn vị của phiên | `/api/v1/auth/me` → `vaiTro` chứa `CB_NV_TW`, `capDonVi = TW` (TW xem toàn quốc — `:2450`) |
| T3 | **Đếm baseline trước khi lọc** | Mở `/vu-viec/danh-sach`, tab **Tất cả**, không đặt ô lọc nào → ghi tổng số bản ghi (chân bảng *"Hiển thị 1-N / M kết quả"* + `total_count` trong phản hồi danh sách qua `list_network_requests`) |
| T4 | **≥1 vụ việc mang mức cảnh báo "Sắp hết hạn" trong phạm vi tài khoản đo** | **Bước 1 — kiểm tra trước:** lọc thử và đọc `total_count`; hoặc đọc thẳng dịch vụ danh sách với tham số mức SLA (lấy đường dẫn + tên tham số từ `list_network_requests` của chính lượt lọc, hoặc `GET /api/docs-json` — **CẤM đoán**). **Bước 2 — nếu 0 bản ghi thì SEED:** tạo vụ việc mới theo luồng *Nhập thủ công* với **`ngay_tiep_nhan` lùi lại** sao cho đã dùng **quá 50% nhưng chưa quá 100%** thời hạn (SLA mặc định 15 ngày làm việc — `:2432` BR-SLA-01; ngưỡng mức — `:1664` và `:1444–1451`) ⇒ bản ghi rơi vào nhóm "Sắp hết hạn". **Bước 3 — xác nhận 2 chiều:** bản ghi hiện ở cột *Cảnh báo thời hạn* = "Sắp hết hạn" **và** dữ liệu trả về mang mức tương ứng |
| T5 | Biết mức cảnh báo được tính lúc nào | `:124` (*"Tính mức SLA thời gian thực"*) và `:1664` (*"SLA cảnh báo tính realtime"*) nói tính realtime, trong khi `:1435` nói job chạy **mỗi 30 phút**. ⇒ Sau khi seed mà chưa thấy đổi mức, **chờ 1 chu kỳ 30 phút rồi đo lại** trước khi kết luận; ghi rõ đã chờ bao lâu |
| T6 | Ghi lại **trạng thái chip "Bộ lọc nâng cao (N)"** | Mở rộng chip, chụp và ghi giá trị từng ô bên trong (đối tác để mặc định, chip hiện `(3)`). Nếu có bộ lọc ẩn đang bật thì phải khai — nó đổi tập kết quả |
| T7 | **Bộ bắt thông báo cài TRƯỚC mỗi lần bấm [Tìm kiếm]** | `output/UAT_doi-tac/tools/toast-capture.js`; cài lại sau mỗi lần tải lại trang; tự kiểm `soObserverDangSong = 1`; **CẤM lọc trùng**, **CẤM `textContent`**; đếm kèm số lời gọi mạng |
| T8 | Ghi **env + bản dựng** sau khi tải lại trang | `HTPLDN · Vx.y.z` ở chân sidebar + bó mã FE |
| T9 | Kế hoạch hoàn nguyên | Vụ việc do QA seed → **giữ lại**, ghi mã VV vào nhật ký đo. **Không** sửa vụ việc của đối tác. Nếu buộc phải đụng: khai đủ **bản ghi nào · đổi gì · env nào** |

---

## 6. Bảng chuẩn chấm

| # | Điều kiện BUG GỐC | Đặc tả (`file:dòng` nguyên văn) | Phép đo quyết định | Pass khi | Reopen khi |
|---|---|---|---|---|---|
| **S1** | Ở màn *Vụ việc HTPL / Danh sách*, tab **Tất cả**, mọi ô lọc khác **trống**, chọn ô **Mức SLA = "Sắp hết hạn"** rồi chạy tìm kiếm → đối tác nhận **khung thông báo lỗi** (`mucSla must be one of the following values: …`) | `srs-fr-05-vu-viec.md:1644` — ô lọc Mức SLA có đúng 4 lựa chọn `BINH_THUONG / SAP_HET / QUA_HAN / QUA_HAN_NGHIEM_TRONG`; `:1516` — `SAP_HET` → nhãn **"Sắp hết hạn"**; `:690–693` — bảng lỗi FR-V.I-08 **chỉ có** `INF-VV-TK-01` (không có kết quả) và `ERR-VV-TK-01` (ngày sai) | Cài bộ bắt thông báo → chọn "Sắp hết hạn" qua **giao diện** (không gõ tay địa chỉ) → chạy tìm kiếm → đếm **số khung thông báo lỗi** (không lọc trùng, `innerText`) + đọc **mã trạng thái** của chính lời gọi danh sách. **Chạy đủ 4 giá trị + 1 baseline** để tách "chỉ hỏng ở Sắp hết hạn" khỏi "hỏng cả bộ lọc" | **0 khung thông báo lỗi** khi chọn "Sắp hết hạn"; lời gọi danh sách trả mã thành công | Còn ≥1 khung thông báo lỗi khi chọn "Sắp hết hạn" / lời gọi danh sách bị từ chối (4xx/5xx) |
| **S2** | *KQ mong đợi*: *"Có kết quả, hệ thống hiển thị danh sách kết quả tìm kiếm"*; điều kiện #2 của phiếu: *"Tồn tại bản ghi phù hợp"* | `srs-fr-05-vu-viec.md:696–697` (AC); `:672–684` Outputs có `muc_sla` + `total_count`; `:2031` ràng buộc giá trị lưu trữ | Với tiền đề T4 đã thoả: đọc **số dòng hiện trên bảng** + chuỗi chân bảng *"Hiển thị 1-N / M kết quả"*. Đối chứng độc lập: `total_count` trong phản hồi của **chính lời gọi danh sách** đó, và mức cảnh báo của từng bản ghi trả về phải là mức "Sắp hết hạn" | Bảng hiện đúng số bản ghi ≥1, khớp `total_count`, **mọi** bản ghi trả về đều mang mức "Sắp hết hạn" (bộ lọc lọc đúng, không lọt bản ghi mức khác) | Bộ lọc trả về bản ghi **mức khác** / số dòng trên bảng ≠ `total_count` / có bản ghi mức "Sắp hết hạn" trong phạm vi nhưng bộ lọc **bỏ sót** |
| **S3** | *KQ mong đợi*: *"phân trang 20 bản ghi mỗi trang"* | `srs-fr-05-vu-viec.md:668` — *"Phân trang (20/trang) \| BR-DATA-07"*; `:1659` — *"\"Hiển thị 1-20 / N kết quả\". Mặc định 20/trang"*; `srs-v3.5.md:5571` — *"Default: 20 rows/page, max: 100 rows/page"* | Đọc **điều khiển phân trang** (chuỗi *"Hiển thị 1-N / M kết quả"* + ô chọn số dòng/trang nếu có) **và** tham số kích thước trang trong lời gọi danh sách. Nếu tập lọc **> 20 bản ghi** thì đo thêm: trang 1 đúng 20 dòng + chuyển sang trang 2 | Kích thước trang mặc định = **20** (đọc được ở cả điều khiển phân trang và lời gọi danh sách); nếu >20 bản ghi thì trang 1 đúng 20 dòng và chuyển trang được | Kích thước trang mặc định ≠ 20 / điều khiển phân trang không xuất hiện / tập >20 bản ghi mà không chuyển được trang |

**Quy tắc gộp:** **fix một phần = Reopen** (BRIEF §4 luật 8). S1 đạt mà S2 hoặc S3 không đạt ⇒ **Reopen**.

---

## 7. Bẫy đã biết

**Chặn FAIL oan / Reopen oan:**

- **(a) 🔴 Danh sách rỗng ≠ báo lỗi.** `:692` quy định **INFO** *"Không tìm thấy hồ sơ phù hợp"* khi không
  có kết quả; `:1580` quy định trạng thái rỗng cho danh sách. Bảng rỗng + dòng chữ này là **hành vi
  đúng**, **CẤM** chấm Reopen. Chỉ **khung thông báo lỗi** mới là triệu chứng của case.
- **(b) 🔴 Rỗng vì thiếu dữ liệu ≠ Pass.** Nếu 0 bản ghi mức "Sắp hết hạn" thì tiền đề #2 của phiếu
  **chưa thoả** → phải **seed** (T4) rồi đo lại. Ghi *"đã Pass"* trên tập rỗng là **Pass oan**.
- **(c) Gõ tay địa chỉ cũ của đối tác.** Mở thẳng `/vu-viec/danh-sach?mucSla=SAP_HET_HAN&page=1` là **địa
  chỉ của bản dựng cũ**, không phải thao tác người dùng trên giao diện hiện tại. Nếu địa chỉ đó vẫn bị từ
  chối thì **không tính** là lỗi của case — chỉ ghi 1 dòng candidate. **Luồng chính bắt buộc: chọn giá
  trị trong ô lọc trên giao diện** (BRIEF §4 luật 1).
- **(d) Chip "Bộ lọc nâng cao (N)" mang bộ lọc mặc định.** Nếu không mở ra ghi lại, tập kết quả có thể
  khác đối tác mà không biết ⇒ T6 bắt buộc.
- **(e) Tập lọc < 20 bản ghi.** Không được vì thế mà chấm S3 hỏng. Phép đo quyết định của S3 là **kích
  thước trang mặc định = 20**, không phải "phải có đủ 20 dòng".
- **(f) Đặc tả tự lệch mã enum — KHÔNG dùng làm căn cứ verdict.** Cùng bộ SRS v3.5 dùng **`SAP_HET`** ở
  `srs-fr-05-vu-viec.md:1516`, `:1644`, `:2031` nhưng dùng **`SAP_HET_HAN`** ở `srs-fr-05-vu-viec.md:1449`
  và `srs-v3.5.md:5626`. ⇒ **Ghi 1 dòng candidate tài liệu** trong `note/`. Chuẩn chấm của vế S1 là **hành
  vi nghiệp vụ** (*"chọn 'Sắp hết hạn' phải ra danh sách, không báo lỗi"*), **KHÔNG** kê đơn giá trị mã mà
  giao diện phải gửi lên — dev có quyền chọn cách hiện thực.
- **(g) Phạm vi đơn vị.** Tài khoản đo là cấp TW (xem toàn quốc — `:2450`); nếu phải fallback sang tài
  khoản cấp BN/ĐP thì phạm vi dữ liệu **hẹp hơn** ⇒ số đếm khác, phải khai rõ và **không** so với baseline
  của cấp TW.

**Chặn PASS oan:**

- **(h) Chỉ bấm 1 giá trị rồi kết luận.** Phải chạy **baseline (không lọc) + đủ 4 giá trị** Mức SLA trong
  **cùng một phiên**, và kiểm phép cộng: tổng 4 nhóm = tổng baseline. Lệch ⇒ bộ lọc chia nhóm sai (S2
  không đạt), dù giá trị "Sắp hết hạn" không báo lỗi.
- **(i) Không đối chứng dữ liệu trả về.** Bảng có dòng ≠ lọc đúng. Bắt buộc đọc mức cảnh báo của **từng**
  bản ghi trong phản hồi danh sách (S2).
- **(j) Thông báo tự tắt.** Khung thông báo sống < 5s → cài `toast-capture.js` **TRƯỚC** khi bấm, **CẤM
  lọc trùng**, đọc bằng `innerText`. Không bắt được → dùng **mã trạng thái + thân phản hồi** của lời gọi
  danh sách làm bằng chứng mạnh hơn ảnh; **không bấm lại chỉ để chụp lại**.
- **(k) Trang cũ / bản dựng cũ.** Bằng chứng là `V1.0.2`, lượt đo cũ là `V1.0.5` (env nội bộ) — bản trên
  env nghiệm thu hiện tại **khác cả hai** ⇒ **tải lại trang** (bỏ bộ nhớ đệm) + **ghi tên bản dựng** trước
  khi đo, và lặp lại thao tác "Sắp hết hạn" **một lần nữa sau khi tải lại** để loại khả năng tab còn chạy
  mã cũ.
- **(l) Hai phép đo mâu thuẫn = CHƯA chốt.** Ví dụ giao diện hiện danh sách nhưng lời gọi danh sách trả
  lỗi (hoặc ngược lại) → ghi cả hai, hỏi lead.

---

## 8. Bảng quyết định đã cam kết TRƯỚC khi đo

| Quan sát ở lượt đo | Verdict logic |
|---|---|
| Tiền đề T4 thoả · chọn "Sắp hết hạn" **0 khung lỗi** · danh sách trả đúng bản ghi mức đó · kích thước trang mặc định 20 · tổng 4 nhóm = baseline | **Pass** — ghi rõ env + bản dựng đã đo là phạm vi hiệu lực |
| Còn khung thông báo lỗi khi chọn "Sắp hết hạn" qua giao diện | **Reopen** (S1 không đạt) |
| Không lỗi nhưng bộ lọc trả bản ghi **mức khác**, hoặc **bỏ sót** bản ghi mức "Sắp hết hạn" | **Reopen** (S2 không đạt) |
| Không lỗi, lọc đúng, nhưng kích thước trang mặc định ≠ 20 / không chuyển được trang khi >20 bản ghi | **Reopen** (S3 không đạt) |
| Tổng 4 nhóm ≠ baseline | **Reopen** (S2 không đạt — bộ lọc chia nhóm sai) |
| 0 bản ghi mức "Sắp hết hạn" **và không seed được** (T4 không thoả) | **Chưa chốt** — nêu rõ dữ kiện còn thiếu, **CẤM Pass** |
| Địa chỉ cũ `?mucSla=SAP_HET_HAN` bị từ chối nhưng thao tác trên giao diện chạy đúng | **Không tính vào verdict** — ghi 1 dòng candidate trong `note/` |
| Giao diện và dữ liệu trả về mâu thuẫn | **Chưa chốt** — ghi cả hai, hỏi lead |
