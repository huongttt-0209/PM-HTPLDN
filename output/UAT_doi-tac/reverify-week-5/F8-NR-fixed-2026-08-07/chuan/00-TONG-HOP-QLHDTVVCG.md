# Tổng hợp khóa chuẩn chấm — 18 phiếu `QLHDTVVCG` (lô F8, Giai đoạn A flow 04)

**Ngày khóa:** 2026-08-07 · **Quy trình:** [`flows/04-verify-bug-dev-fix-khong-ho-so.md`](../../../../../flows/04-verify-bug-dev-fix-khong-ho-so.md)
**Nguồn chuẩn duy nhất:** `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-14-hop-dong-tv.md` (536 dòng, **đã đọc trọn** lượt này)
**Kiểm chéo đã đọc:** `srs-v3.5.md` Phụ lục E §H (`:6747`–`:6762`) + ma trận quyền (`:1295`–`:1378`) + thực thể `HOP_DONG_TU_VAN` (`:2293`–`:2321`) · `srs-fr-05-vu-viec.md` §3.A–G (`:1477`–`:1623`) + SCR-V.I-01 (`:1626`–`:1658`) + SCR-V.I-03 (`:1715`–`:1786`) · `srs-fr-04-chuyen-gia-tvv.md` SCR-IV-03 (`:1560`–`:1585`) · `srs-fr-11-bao-cao.md:85` · `srs-fr-12-tv-chuyen-sau.md:1359`, `:1367`

**Đặc điểm lô:** cả 18 phiếu đều `Trạng thái` = `N/R`, `Kết quả thực tế` RỖNG, không ảnh ⇒ **`expected đối tác` = nguyên văn cột `Kết quả mong đợi` (K)**, không có triệu chứng cũ. Cột `Tác nhân` (F) của **cả 18 phiếu đều RỖNG** ⇒ vai trò suy từ đặc tả (xem §4).

---

## 1. Bảng 18 phiếu × số vế × phân bố quan hệ × route

| # | Dòng | Mã phiếu | Nội dung | Vế | MATCH | DIFF | GAP | Route |
|---|---|---|---|---|---|---|---|---|
| 1 | 308 | [`_02`](QLHDTVVCG_02.md) | Điều kiện tìm kiếm / bộ lọc (màn danh sách) | 5 | 3 | 0 | 2 | **BA** |
| 2 | 309 | [`_03`](QLHDTVVCG_03.md) | Tìm kiếm có kết quả | 1 | 1 | 0 | 0 | TEST |
| 3 | 310 | [`_04`](QLHDTVVCG_04.md) | Tìm kiếm không có kết quả | 2 | 2 | 0 | 0 | TEST |
| 4 | 311 | [`_05`](QLHDTVVCG_05.md) | Khoảng ngày nghịch | 2 | 2 | 0 | 0 | TEST |
| 5 | 314 | [`_08`](QLHDTVVCG_08.md) | Chi tiết — Nhóm 1 Thông tin chung | 5 | 3 | 0 | 2 | **BA** |
| 6 | 315 | [`_09`](QLHDTVVCG_09.md) | Chi tiết — Nhóm 2 Vụ việc liên kết | 5 | 3 | 0 | 2 | **BA** |
| 7 | 319 | [`_13`](QLHDTVVCG_13.md) | Nhấn "+ Thêm hợp đồng" | 3 | 2 | 0 | 1 | **BA** |
| 8 | 321 | [`_15`](QLHDTVVCG_15.md) | Thêm hợp đồng thành công | 5 | 4 | **1** | 0 | **BA** |
| 9 | 322 | [`_16`](QLHDTVVCG_16.md) | Xuất Excel | 4 | 2 | **1** | 1 | **BA** |
| 10 | 323 | [`_17`](QLHDTVVCG_17.md) | Xóa — không có vụ việc liên kết | 4 | 2 | 0 | 2 | **BA** |
| 11 | 324 | [`_18`](QLHDTVVCG_18.md) | Xóa — có vụ việc liên kết | 2 | 2 | 0 | 0 | TEST |
| 12 | 325 | [`_19`](QLHDTVVCG_19.md) | Nhấn "Sửa" | 3 | 3 | 0 | 0 | TEST |
| 13 | 327 | [`_21`](QLHDTVVCG_21.md) | Sửa thành công | 5 | 3 | **1** | 1 | **BA** |
| 14 | 328 | [`_22`](QLHDTVVCG_22.md) | Liên kết vụ việc | 5 | 3 | 0 | 2 | **BA** |
| 15 | 329 | [`_23`](QLHDTVVCG_23.md) | Bỏ liên kết | 2 | 1 | 0 | 1 | **BA** |
| 16 | 330 | [`_24`](QLHDTVVCG_24.md) | Thêm mốc tiến độ | 2 | 2 | 0 | 0 | TEST |
| 17 | 332 | [`_26`](QLHDTVVCG_26.md) | Thêm giai đoạn thanh toán | 3 | 2 | **1** | 0 | **BA** |
| 18 | 333 | [`_27`](QLHDTVVCG_27.md) | Xóa giai đoạn thanh toán | 2 | 1 | 0 | 1 | **BA** |
| | | **TỔNG** | | **60** | **41** | **4** | **15** | **12 BA / 6 TEST** |

- **6 phiếu route TEST thuần** (mọi vế `MATCH`, được chấm Pass/Reopen bằng kết quả đo): `_03` · `_04` · `_05` · `_18` · `_19` · `_24`.
- **12 phiếu chắc chắn route BA** (có ≥1 vế `DIFF`/`GAP` ⇒ **CẤM Pass toàn phiếu**): `_02` · `_08` · `_09` · `_13` · `_15` · `_16` · `_17` · `_21` · `_22` · `_23` · `_26` · `_27`.
- 41 vế `MATCH` vẫn phải đo đầy đủ — trong 12 phiếu route BA, nếu một vế `MATCH` sai thì kết quả logic là **Reopen + cần BA** (flow 04 §Ca biên).

### 4 vế `DIFF` — đặc tả nói **ngược** kỳ vọng phiếu

| Phiếu · vế | Đối tác kỳ vọng | SRS quy định | Neo |
|---|---|---|---|
| `_15` C5 | Sau khi lưu → **quay về danh sách** | Nhóm X.3 **không có màn danh sách độc lập**; đóng biểu mẫu, trả về **ngữ cảnh đã mở nó** | `srs-fr-14-hop-dong-tv.md:175` `[BA chốt 2026-08-06]`, `:187` |
| `_21` C5 | Sau khi lưu bản sửa → **quay về danh sách** | như trên | `:175`, `:187` |
| `_16` C4 | Tên tệp `HDTV-danh-sach-{YYYYMMDD-HHmm}.xlsx` | Khuôn **BẮT BUỘC** `{TenTep}[_{DinhDanh}]_{YYYYMMDD_HHmm}.{đuôi}`, PascalCase, **bỏ mọi ký tự không phải chữ/số kể cả dấu gạch nối** | `srs-v3.5.md:6760` (Phụ lục E §H8) |
| `_26` C2 | Nhập Số tiền → **tự cộng dồn** vào thanh tiến trình | Thanh tiến trình = **SUM(đã thanh toán)** / giá trị HĐ × 100%; dòng mới mặc định **chưa thanh toán** | `srs-fr-14-hop-dong-tv.md:301`, `:112` |

### 15 vế `GAP` — đặc tả im lặng hoặc tự mâu thuẫn

| Phiếu · vế | Điểm thiếu / mâu thuẫn | Neo (dòng gần nhất đã đọc) |
|---|---|---|
| `_02` C2 · `_08` C2 · `_09` C2 | "giống với **thiết kế**": SRS trỏ ra `dac-ta-man-hinh-chuc-nang-v2.md — MH-14.1`, **tệp này không tồn tại trong nguồn chuẩn** (đã `find` toàn repo) | `srs-fr-14-hop-dong-tv.md:274` |
| `_02` C4 · `_08` C4 · `_09` C4 | "không bị tràn/đè": SRS chỉ có quy ước **cắt chuỗi dài + tooltip** và **độ phân giải tối thiểu**, im lặng về tràn/đè bố cục | `srs-fr-05-vu-viec.md:1571`–`:1573`, `:1603`; `srs-v3.5.md:6755` |
| `_13` C2 | **Thời điểm** sinh mã hợp đồng: `:290` khai "Mã (auto)" như trường trên biểu mẫu, `:119` xếp sinh mã vào **bước xử lý khi lưu** | `:81`, `:119`, `:290` |
| `_16` C2 | Cấu trúc cột tệp Excel: chính SRS ghi *"**cần CĐT xác nhận template**"*, cả khối mang cờ `[GAP-X.3-02]` | `:127`, `:134` |
| `_17` C3 | Câu thông báo **sau khi xóa thành công**: bảng lỗi FR-X.3-01 có mã cho *xóa thất bại* và *lưu thành công*, **không có** mã cho xóa thành công | `:166`–`:173`; `srs-fr-05-vu-viec.md:1588`–`:1597` |
| `_17` C4 | "làm mới danh sách" sau khi xóa: im lặng, lại vướng `:175` "không có màn danh sách độc lập" | `:124`, `:175`, `:299` |
| `_21` C3 | Ngữ nghĩa **thay thế toàn bộ** 4 danh sách con khi lưu bản sửa: `:122` chỉ nói "cập nhật", `:123` nói "tạo"; tệp đính kèm không xuất hiện trong bảng Processing | `:118`–`:125`, `:159`–`:162` |
| `_22` C2 | Tiêu chí tìm kiếm **bên trong cửa sổ chọn vụ việc**: `:291` chỉ khai "modal multi-select" + cột của **bảng kết quả** | `:291`, `:90` |
| `_22` C5 | **MÂU THUẪN** quan hệ HĐ ↔ VV: 4 chỗ khai `many-to-many` (`:90`, `:123`, `:161`, `:291`) ↔ 4 chỗ khai **một-nhiều** (`:352`, `:373`, `:424`, `srs-v3.5.md:4406`) | như bên |
| `_23` C1 | Hộp xác nhận + câu chữ khi **bỏ liên kết**: không khai ở đâu; mẫu ở `srs-fr-05-vu-viec.md:1595` là câu **xóa vụ việc**, không được mượn | `:291`; `srs-fr-05-vu-viec.md:1588`–`:1597` |
| `_27` C1 | **Nút xóa dòng** ở bảng Thanh toán giai đoạn: `:291` có khai `[Bỏ liên kết]`, `:292` có khai `[+ Thêm mốc]`, riêng `:293` **không khai nút nào**; Processing cũng không có bước xóa giai đoạn | `:293`, `:118`–`:125` |

---

## 2. Danh sách tiền đề gộp — dựng **một lần** cho cả 18 phiếu

### 2.1 Tài khoản

| Vai trò | Tài khoản | Dùng cho | Căn cứ |
|---|---|---|---|
| **Cán bộ Nghiệp vụ TW** | `cbnv_tw_03` / `Test@1234` | **Cả 18 phiếu** | `srs-fr-14-hop-dong-tv.md:27`, `:68`, `:203` |

- Cấp **TW** để phạm vi dữ liệu rộng nhất (`srs-v3.5.md:1375` — "TW: Nhìn thấy dữ liệu TẤT CẢ đơn vị"), tránh bảng rỗng vì phân quyền chứ không vì chức năng.
- **Ghi lại tên đơn vị của tài khoản** ngay sau khi đăng nhập — cần đối chứng trường "Bên A" ở `_13` C3 và `_19` C3.
- Tài khoản khóa → fallback **cùng vai trò + cùng cấp** (`_04`, `_05`), ghi rõ tài khoản thực dùng. **CẤM đổi vai trò/cấp.**
- **`admin` chỉ dùng dựng dữ liệu/điều tra, KHÔNG dùng ra verdict** (brief §3).

### 2.2 Dữ liệu cần có (7 mục — dựng một lần, dùng chung)

| Mã | Dữ liệu | Phục vụ phiếu | Ghi chú dựng |
|---|---|---|---|
| **D1** | **≥4 hợp đồng** trong phạm vi, trong đó một từ khóa cụ thể chỉ khớp **≈2** (còn lại bị loại) | `_02`, `_03`, `_04`, `_16` | Cần cả bản ghi **bị loại** mới chứng minh được lọc. `_04` không cần seed thêm (dùng từ khóa vô nghĩa) |
| **D2** | **HĐ-1 "đầy đủ"**: Tên **> 30 ký tự** · Giá trị > 0 (ghi lại con số) · đủ 2 mốc thời hạn, **1 mốc kết thúc ≤ 30 ngày** · Nội dung · Ghi chú · **≥1 tệp đính kèm** | `_02` C3/C4, `_08`, `_19`, `_21` | Cột "Thời hạn kết thúc đỏ khi ≤30 ngày" (`:288`) chỉ đo được nếu có bản ghi rơi vào ngưỡng |
| **D3** | **HĐ-1 có ≥2 vụ việc liên kết**, trong đó ≥1 vụ việc có **Tên DN > 40 ký tự** | `_09`, `_18`, `_22`, `_23` | Dựng bằng chính chức năng ở `_22` |
| **D4** | **HĐ-1 có ≥2 mốc tiến độ** và **≥2 giai đoạn thanh toán**, trong đó **≥1 giai đoạn ở trạng thái "đã thanh toán"** | `_21`, `_24`, `_26`, `_27` | Dòng "đã thanh toán" là **bắt buộc** — theo `:301` chỉ dòng đã thanh toán mới ảnh hưởng thanh tiến trình |
| **D5** | **HĐ-2 "sạch liên kết"** (Số VV liên kết = 0) — sẽ bị **xóa mềm thật** | `_17` | Dùng hợp đồng QA tự dựng, **không đụng dữ liệu đối tác**. Ghi định danh **trước khi** xóa |
| **D6** | **HĐ-3** (hợp đồng thứ hai còn sống) để thử gắn **cùng một vụ việc** vào hai hợp đồng | `_22` C5 | Phép đo duy nhất phân biệt nhiều-nhiều với một-nhiều |
| **D7** | **≥3 vụ việc** trong phạm vi, **chưa** liên kết với HĐ-1 | `_15`, `_22` | Nếu môi trường chưa có → seed vụ việc **trước**, khai vào báo cáo |
| **D8** | **Bộ tệp fixture thật** (pdf / docx / xlsx / png đúng định dạng) | `_15`, `_08` (D2) | **CẤM** tạo tệp văn bản rồi đổi đuôi (brief §4.6) |

> **HĐ-1 = hợp đồng tạo ra ở `_15`.** Chạy `_15` sớm và nhập đủ 4 nhóm con là dựng xong D2+D3+D4 trong một lượt.

### 2.3 Công cụ / môi trường

- Cửa sổ **1440×900** (cấu hình MCP của lô) — ghi vào báo cáo; `srs-fr-05-vu-viec.md:1603` chỉ bảo đảm ≥1024×768.
- **`MutationObserver` cài TRƯỚC thao tác, CẤM lọc trùng** — bắt buộc cho: `_04` C2, `_05` C2, `_15` C4, `_17` C3, `_18` C2, `_21` C4, `_26` C3.
- **`openpyxl`** để mở tệp xuất — bắt buộc cho `_16`. Ảnh chụp không thay được việc mở tệp.
- Đọc chữ người dùng thấy bằng **`innerText`** (không `textContent` — gom node ẩn AntD → bug ma).
- Đọc `/api/docs-json` **trước** khi gọi API đối chứng — **cấm đoán đường dẫn/khóa JSON**.
- Đo **vân tay bản dựng đầu VÀ cuối phiên** (bó mã `assets/index-*.js` + `last-modified` của `GET /`).

### 2.4 Thao tác **mutate môi trường chung** phải khai vào báo cáo

`_15` (tạo HĐ-1) · `_21` (sửa HĐ-1) · `_22` (gắn vụ việc) · `_23` (gỡ liên kết) · `_24`/`_26` (thêm dòng, nếu có lưu) · `_27` (xóa giai đoạn) · `_17` (**xóa mềm HĐ-2**) · seed vụ việc D7 nếu phải làm.
Mỗi mục khai: **đổi bản ghi nào · đổi gì · trên env nào** (env nội bộ `https://18.143.165.120.nip.io`).

---

## 3. Thứ tự chạy đề xuất

Ràng buộc cứng: `_15` → (`_22` → `_09`) · `_22` → `_23` · `_18` **trước** `_23` · `_26` → `_27` · `_21` sau khi HĐ-1 đã đủ 4 nhóm con · `_17` chạy muộn (xóa mềm thật).

| Bước | Phiếu | Vì sao đặt ở đây |
|---|---|---|
| **Giai đoạn 0 — dựng nền** | | |
| 0a | *(chuẩn bị, không phải phiếu)* | Đăng nhập `cbnv_tw_03`, ghi tên đơn vị + vân tay bản dựng. Kiểm D7 (≥3 vụ việc); thiếu thì seed. Chuẩn bị D8 (tệp fixture) |
| 1 | **`_13`** | Không phụ thuộc dữ liệu; đồng thời xác nhận vào được biểu mẫu Thêm mới. **KHÔNG bấm Lưu** |
| 2 | **`_15`** | **Tạo HĐ-1 với đủ 4 nhóm con** → dựng xong D2+D3+D4 trong một lượt. Là tiền đề của 11 phiếu sau |
| 3 | *(dựng thêm)* | Lặp luồng `_15` để có **HĐ-2** (sạch liên kết, cho `_17`) và **HĐ-3** (cho `_22` C5). Đủ HĐ-1..3 + bản ghi sẵn có ⇒ thoả D1 |
| **Giai đoạn 1 — đọc / hiển thị (không đổi dữ liệu)** | | |
| 4 | **`_02`** | Cần HĐ-1 đầy đủ (D2) đã có |
| 5 | **`_03`** | Cần D1 |
| 6 | **`_04`** | Không cần seed; chạy liền sau `_03` trên cùng thanh lọc |
| 7 | **`_05`** | Cùng thanh lọc, không cần dữ liệu |
| 8 | **`_16`** | Cần D1 + bộ lọc ra tập con; chạy sau khi đã quen bộ lọc ở `_03` |
| 9 | **`_08`** | Chi tiết HĐ-1, Nhóm 1 |
| 10 | **`_19`** | Mở biểu mẫu Sửa. **KHÔNG bấm Lưu** (bấm Hủy sau khi gõ thử) |
| **Giai đoạn 2 — nhóm con trên biểu mẫu** | | |
| 11 | **`_22`** | Gắn thêm vụ việc cho HĐ-1 + thử gắn chéo sang HĐ-3 (C5). Phải chạy **trước** `_09` và `_23` |
| 12 | **`_09`** | Chi tiết Nhóm 2 — chắc chắn đã có liên kết sau bước 11 |
| 13 | **`_24`** | Thêm mốc trên HĐ-1 |
| 14 | **`_26`** | Thêm giai đoạn thanh toán; đặt ≥1 dòng sang "đã thanh toán" để phục vụ bước 15 |
| 15 | **`_27`** | Xóa giai đoạn — **bắt buộc sau `_26`** |
| 16 | **`_21`** | Sửa thành công — cần HĐ-1 **đã có đủ** 4 nhóm con (sau bước 11–15) để đo được vế C3 "thay thế" |
| **Giai đoạn 3 — thao tác phá tiền đề (chạy CUỐI)** | | |
| 17 | **`_18`** | Xóa HĐ-1 khi **đang có** vụ việc liên kết (phải bị chặn). **Bắt buộc trước `_23`** |
| 18 | **`_23`** | Bỏ liên kết — làm giảm tiền đề của `_18`/`_09`, nên đặt sau cả hai |
| 19 | **`_17`** | **Xóa mềm HĐ-2 thật** — chạy cuối cùng để không mất bản ghi phục vụ phiếu khác |

> **Không dừng chờ nếu không có blocker.** Gặp blocker thật: ghi **Chưa chốt**, nêu đúng dữ kiện còn thiếu, **bỏ qua phiếu đó và chạy tiếp phiếu sau**, báo lại ở bàn giao cuối.

---

## 4. Vai trò / tác nhân — suy từ đặc tả (cột `Tác nhân` của cả 18 phiếu đều RỖNG)

| Kết luận | Dòng đặc tả |
|---|---|
| Tác nhân chính nhóm X.3 = **Cán bộ Nghiệp vụ (TW/BN/ĐP)** | `srs-fr-14-hop-dong-tv.md:27` — "**Tác nhân chính:** Cán bộ Nghiệp vụ (TW/BN/ĐP)" |
| CB NV có **quyền CRUD đầy đủ**; TVV/CG chỉ **xem** | `:68`, `:69` |
| TVV/CG bị **chặn mọi thao tác Create/Update/Delete** | `:118` |
| Tìm kiếm (FR-X.3-02) thêm **Cán bộ Phê duyệt** | `:203` |
| Nút `[+ Thêm hợp đồng]` **chỉ hiện với CB NV** | `:286` |
| **Chỉ CB NV** truy cập trang biểu mẫu; TVV/CG chỉ thấy `[Đóng]` ở trang xem chi tiết | `:290`, `:295` |
| Ma trận quyền dữ liệu: `HOP_DONG_TU_VAN` → CB_NV_* = `CRUD*`, CB_PD_* = `R*`, TVV/CG = `R*`, DN/NHT = `—` | `srs-v3.5.md:1345` |
| ⚠️ Ma trận quyền là **quyền dữ liệu, KHÔNG phải tác nhân chức năng** — tác nhân do dòng "Tác nhân" của FR quyết định | `srs-v3.5.md:1295` `[làm rõ 2026-08-06]` |

---

## 5. Câu hỏi BA — gom theo chủ đề (soạn sẵn cho Giai đoạn A)

### 5.1 🔴 Cảnh báo sớm — **đường vào chức năng không tồn tại trong đặc tả** (ảnh hưởng CẢ 18 PHIẾU)

Bước J của **cả 18 phiếu** bắt đầu bằng *"Chọn menu **Hợp đồng Tư vấn**"*. Đặc tả nói ngược, **và** đường thay thế mà nó chỉ ra thì **không có ở đâu**:

- `srs-fr-14-hop-dong-tv.md:266` — *"HD Tu van (UC159) **khong con la muc menu rieng**. Truy cap tu: (1) Chi tiet Vu viec MH-05.3 -> tab/section **"HD tu van lien ket"**, (2) Chi tiet TVV MH-04.3 -> tab **"Lich su"** -> HD."*
- `srs-fr-14-hop-dong-tv.md:268` — *"Route standalone `/hop-dong-tv/danh-sach` **KHÔNG phải menu/màn hình nghiệp vụ public** … **không được QA coi là luồng chính**."* `[Round 7 BA decision 2026-05-11]`
- `srs-v3.5.md:454` và `:680` khẳng định lại: **KHÔNG có menu**, truy cập qua chi tiết vụ việc và chi tiết tư vấn viên.
- **NHƯNG:** bảng thành phần **SCR-V.I-03 Chi tiết Vụ việc** (`srs-fr-05-vu-viec.md:1722`–`:1737`, đã đọc trọn — 8 accordion) **KHÔNG có** tab/section nào tên "HĐ tư vấn liên kết".
- **VÀ:** **SCR-IV-03 Chi tiết TVV** (`srs-fr-04-chuyen-gia-tvv.md:1560`–`:1585`, đã đọc trọn — **5 tab**: Hồ sơ / Thẩm định / Năng lực / Lịch sử hỗ trợ / Đánh giá) **KHÔNG có** mục hợp đồng; tab "Lịch sử hỗ trợ" (`:1577`) liệt kê **vụ việc**, không phải hợp đồng.
- **Đồng thời** `srs-fr-14-hop-dong-tv.md:278`–`:289` đặc tả **đầy đủ một màn danh sách độc lập** (breadcrumb "Trang chủ > Tư vấn > Hợp đồng tư vấn", 3 nút, thanh lọc, bảng 10 cột, phân trang 20 mục), và `:179` ghi AC *"CB NV truy cập "HĐ tư vấn" **When** hiển thị **Then** danh sách HĐ, phân trang"*.

> **CẦN BA CONFIRM:** Đặc tả vừa nói nhóm X.3 **không có menu và không có màn danh sách độc lập** (`srs-fr-14-hop-dong-tv.md:266`, `:268`, `:175`), vừa đặc tả **đầy đủ một màn danh sách** kèm AC truy cập (`:179`, `:278`–`:289`); trong khi hai màn chủ mà nó chỉ sang (**SCR-V.I-03** và **SCR-IV-03**) **đều không khai** mục Hợp đồng tư vấn nào. Vậy **đường vào chính thức của chức năng Hợp đồng tư vấn là gì**, và bảng thành phần ở `:278`–`:289` áp cho màn nào?

**Cách xử lý trong lúc chờ BA:** đây là **tiền đề/đường đi**, **không** phải vế chấm của phiếu nào (không cột K nào nhắc tới menu) ⇒ **không tách thành vế, không tự log bug**. Mỗi phiếu **ghi rõ đường thực tế đã đi vào** trong `do/<MÃ>.md`.

### 5.2 Bốn điểm `DIFF` — bắt buộc có câu "CẦN BA CONFIRM" trong ô kết quả

Câu đầy đủ đã soạn sẵn trong từng tệp: [`_15`](QLHDTVVCG_15.md) · [`_21`](QLHDTVVCG_21.md) · [`_16`](QLHDTVVCG_16.md) · [`_26`](QLHDTVVCG_26.md). Tóm tắt ở §1.

### 5.3 Điểm `GAP` do đặc tả **tự mâu thuẫn** (nặng nhất — cần chốt để dev có chuẩn)

1. **Quan hệ Hợp đồng ↔ Vụ việc** (`_22` C5): 4 chỗ khai `many-to-many` (`:90`, `:123`, `:161`, `:291`) ↔ 4 chỗ khai cấu trúc **một-nhiều** với khoá ngoại đặt trên `VU_VIEC` (`:352`, `:373`, `:424`, `srs-v3.5.md:4406`). **Một vụ việc có được thuộc nhiều hợp đồng không?**
2. **Thời điểm sinh mã hợp đồng** (`_13` C2): `:290` khai "Mã (auto)" như trường biểu mẫu ↔ `:119` xếp sinh mã vào **bước xử lý khi lưu**. **Mã hiện ngay khi mở biểu mẫu hay chỉ sau khi lưu?**

### 5.4 Điểm `GAP` do đặc tả **im lặng** — đề nghị **bổ sung vào đặc tả**, không chặn bàn giao

| Chủ đề | Phiếu · vế | Câu hỏi cho BA |
|---|---|---|
| Câu thông báo sau khi **xóa hợp đồng thành công** | `_17` C3 | Có yêu cầu thông báo không, câu chữ là gì? (bảng lỗi hiện chỉ có "xóa thất bại" và "lưu thành công") |
| Hành vi màn hình **sau khi xóa** | `_17` C4 | "Làm mới danh sách" nghĩa là màn nào, khi nhóm X.3 được tuyên bố không có danh sách độc lập? |
| **Hộp xác nhận bỏ liên kết** vụ việc | `_23` C1 | Có bắt buộc hộp xác nhận không, câu chữ có chèn mã vụ việc không? |
| **Nút xóa dòng** ở bảng Thanh toán giai đoạn | `_27` C1 | Bảng Nhóm 4 có được phép xóa dòng không? (`:293` không khai nút nào, trong khi `:291`/`:292` đều có) |
| **Tiêu chí tìm kiếm** trong cửa sổ chọn vụ việc | `_22` C2 | Cửa sổ chọn có ô tìm kiếm không, tìm theo mã VV / tên DN / lĩnh vực? |
| Ngữ nghĩa **thay thế vs cộng dồn** khi lưu bản sửa | `_21` C3 | Lưu bản sửa có xoá các mốc/giai đoạn/liên kết/tệp không còn trong dữ liệu mới không? |
| **Cấu trúc cột tệp Excel** | `_16` C2 | Template cột đã được CĐT xác nhận chưa? (`:134` tự khai "cần CĐT xác nhận template") |
| **Bản vẽ thiết kế** MH-14.1 | `_02`/`_08`/`_09` C2 | Tệp `dac-ta-man-hinh-chuc-nang-v2.md` không có trong bộ tài liệu chuẩn — lấy gì làm chuẩn chấm "giống với thiết kế"? |
| **Quy ước tràn/đè** giao diện | `_02`/`_08`/`_09` C4 | Có tiêu chí đo được nào cho "không tràn/đè" ngoài quy ước cắt chuỗi dài không? |
| **Bảng thành phần trang xem chi tiết** hợp đồng | `_08`, `_09` | Đặc tả chỉ có bảng thành phần cho **trang thêm/sửa** (`:290`–`:295`); trang "Xem chi tiết" (bước J của hai phiếu) hiển thị những gì? |
| **Nhãn tiếng Việt cho `HOP_DONG_TU_VAN.trang_thai`** | `_15` C3 | Bảng ánh xạ mã→nhãn ở `srs-fr-05-vu-viec.md:1490`–`:1566` **không có** hợp đồng; nhãn hiển thị của `DANG_THUC_HIEN` là gì? |

### 5.5 Lệch nội bộ nhỏ — ghi nhận, **không dùng để Fail**

| Điểm lệch | Hai phía |
|---|---|
| Nhãn nút thêm mới | `:286` ghi `[+ Thêm hợp đồng]` ↔ Phụ lục E §H4 (`srs-v3.5.md:6756`) bắt **"Thêm mới"** |
| Câu chữ "không tìm thấy" | `:251` "Không tìm thấy hợp đồng **phù hợp**" ↔ `:258` "Không tìm thấy hợp đồng" |
| Bộ lọc áp cho Xuất Excel | `:132` liệt kê "TVV, **trạng thái**, thời gian" ↔ Inputs FR-X.3-02 `:216`–`:219` có **keyword**, **không có** bộ lọc trạng thái |
| Cột bảng kết quả | Bảng tìm kiếm `:240` **có** cột Trạng thái ↔ bảng danh sách `:288` **không có** |
| Trường thực thể | `srs-fr-14:382`–`:396` **không có** `to_chuc_tu_van_id` ↔ `srs-v3.5.md:2306` **có**; biểu mẫu `:290` thiếu `so_hop_dong` (`:385`) và `ngay_ky` (`:390`) |
| Phân trang | `:289` ghi 20 mục/trang ↔ BR-DATA-07 `:530` cho phép tới 100 |

---

## 6. Nhắc lại luật khóa (flow 04 §BUG SCOPE LOCK)

1. **Sau khi mở màn, CẤM đổi quan hệ `MATCH`/`DIFF`/`GAP` để khớp kết quả đo.** Chỉ đổi được khi dẫn ra **dòng SRS mới đọc được**; lý do kiểu *"web đã làm đúng expected"* hoặc *"coi như đã đáp ứng bằng cách khác"* **không** thay được quan hệ đã khóa.
2. **`DIFF`/`GAP` → CẤM Pass**, kể cả khi web làm đúng y kỳ vọng đối tác. Với `GAP` mà web đang đúng kỳ vọng: tóm tắt phải ghi rõ *"web hiện tại đúng kỳ vọng đối tác"* và câu hỏi BA nêu đúng mục đích là **bổ sung vào đặc tả**, không phải chặn bàn giao.
3. **Mỗi thao tác/ảnh/phép đo phải trả lời được "đang kiểm Cn nào?"** Không ánh xạ được về vế → **CẤM chạy**.
4. **Mỗi vế: một đường UI ngắn nhất + một đối chứng độc lập.** Bấm lại cùng một nút **không** tính là đường thứ hai. Hai đường khớp thì **dừng**. **Hai phép mâu thuẫn = chưa được chốt.**
5. **Hành động đang tranh chấp phải bấm bằng UI thật**; API chỉ để dựng tiền đề + đối chứng. **CẤM Pass bằng quan sát tĩnh** khi vế là hành động.
6. **Không mở rộng** thành regression / ma trận CRUD / mọi vai trò / mọi bộ lọc / mọi trạng thái.
7. **Case gộp nhiều vế:** còn ≥1 vế `MATCH` sai **và** có vế `DIFF`/`GAP` → kết quả logic **Reopen + cần BA**; không vế nào Reopen mà còn `DIFF`/`GAP` → **Cần BA**.
