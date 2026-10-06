# Chuẩn chấm đã khóa — QLNDTVVCG_19 (dòng 285)

> **FLOW 04 — GIAI ĐOẠN A.** Bug dev báo đã fix, **KHÔNG có hồ sơ nội bộ** (không có bug entry, không có khối
> `CÁCH VERIFY`). Nguồn chuẩn chấm duy nhất = SRS tại đường dẫn prompt cấp. Chưa mở màn đang tranh chấp.
>
> **Đặc tả — nguồn duy nhất:** `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/`
> — file chính `srs-fr-12-tv-chuyen-sau.md` (1.681 dòng, mtime **06/08/2026 22:52**), phụ trợ `srs-v3.5.md`.
> **Mọi số dòng dưới đây tự mở file đọc lại ngày 2026-08-07**, không lấy từ trí nhớ / phiếu UAT / thư BA.
>
> Chức năng: **FR-X.1-01 (UC147)** màn chi tiết **SCR-X1-02** khối *Đánh giá chất lượng*; dữ liệu nguồn từ
> **FR-X.1-07 (UC153)** — API inbound Cổng PLQG.
>
> ⚠️ **Bằng chứng đối tác:** phiếu KHÔNG khai tệp ảnh/video cho case này, và trong repo cũng không có tệp nào
> tên `QLNDTVVCG_19.*`. ⇒ Không có neo tái hiện từ đối tác; tiền đề phải tự dựng theo §4 và phải khai rõ.

---

## 1. Lỗi gốc — nguyên văn phiếu đối tác

| | Nội dung |
|---|---|
| **Mã TC / dòng** | `QLNDTVVCG_19` — dòng **285** |
| **Mô tả** | "Nhóm 4 — Đánh giá chất lượng" |
| **Điều kiện** | 1. Đăng nhập hệ thống thành công |
| **Các bước** | 1. Chọn menu "Tư vấn" => "Tư vấn chuyên sâu" · 2. Nhấn "Xem chi tiết" tại bản ghi |
| **Kết quả mong đợi (nguyên văn)** | "Bảng liệt kê các đánh giá chất lượng tư vấn do doanh nghiệp gửi sau khi nhận kết quả. Các cột: Mã đánh giá, Điểm (1-5 sao), Nhận xét của doanh nghiệp, Ngày đánh giá. Tổng hợp ở cuối bảng: điểm trung bình và số lượng đánh giá. Toàn bộ dữ liệu chỉ đọc" |
| **Trạng thái** | Fail |
| **Dopai** | N/R |
| **TKM phản hồi lần 1** | "chưa có dữ liệu test" |
| **Trạng thái dev fix** | Fixed |

> 🔴 **Đọc kỹ ô TKM:** *"chưa có dữ liệu test"* — đây là lời **giải thích vì sao không tái hiện được**, KHÔNG
> phải mô tả một lỗi sản phẩm. Nó nói thẳng rằng vế **có dòng dữ liệu** (C2) và vế **dòng tổng hợp** (C4)
> chưa từng được đo. Không được dùng câu này để suy ra "đã fix" hay "không phải lỗi".

---

## 2. Đặc tả đối chiếu — trích dẫn `file:dòng` (tự mở đọc lại 2026-08-07)

### 2.1 Dòng quyết định

| Dòng | Nguyên văn |
|---|---|
| `srs-fr-12-tv-chuyen-sau.md:1150` | `### SCR-X1-02: Thêm mới / Chi tiết Tư vấn pháp luật chuyên sâu` |
| `srs-fr-12-tv-chuyen-sau.md:1152` | `**Loại màn hình:** Form nhập liệu / Chi tiết (tabs: Thông tin, Tư liệu PL, Đánh giá CL + action buttons phân công/phê duyệt)` |
| **`srs-fr-12-tv-chuyen-sau.md:1160`** | `Breadcrumb > Tiêu đề + nhãn trạng thái > Thanh tiến trình SM-TVCS (stepper) > Accordion sections (Thông tin cơ bản / Nội dung TV / Tư liệu PL / Đánh giá CL / Nhật ký) > Thanh hành động cố định` |
| 🔴 **`srs-fr-12-tv-chuyen-sau.md:1172`** | `| 7 | content | Accordion: Đánh giá chất lượng (UC153) | table (read-only) | Bảng: Mã đánh giá / Điểm (1-5 sao) / Nhận xét DN / Ngày. Tổng hợp: Điểm TB + Số lượng. API inbound Cổng PLQG | — | mode chi tiết |` |
| `srs-fr-12-tv-chuyen-sau.md:1006` | `**Màn hình:** Không có màn hình CMS (API inbound từ Cổng PLQG). Dữ liệu hiển thị read-only tại SCR-X1-02 — Accordion "Đánh giá chất lượng"` |
| `srs-fr-12-tv-chuyen-sau.md:153` | `| 4 | Truy vấn đánh giá chất lượng liên quan | — |` *(bước 4 khối Processing "Xem chi tiết" của FR-X.1-01)* |
| `srs-fr-12-tv-chuyen-sau.md:1116` | `| 1 | toolbar | Breadcrumb | breadcrumb | "Trang chủ > Tư vấn > Tư vấn pháp luật chuyên sâu" | navigate | luôn hiển thị |` |
| `srs-fr-12-tv-chuyen-sau.md:1125` | `… Hành động (Xem / Sửa / Phân công CG / Hủy) | click hàng -> xem chi tiết | luôn hiển thị |` |

### 2.2 Dòng nền — nguồn dữ liệu & tính chỉ đọc

| Dòng | Nguyên văn (rút gọn ≤200 ký tự) |
|---|---|
| `srs-fr-12-tv-chuyen-sau.md:1008-1009` | `**Mô tả:** Tiếp nhận đánh giá chất lượng tư vấn từ Cổng PLQG qua API inbound. Hỗ trợ tạo mới, cập nhật, và gửi lại (idempotency). Cập nhật điểm trung bình chuyên gia.` |
| 🔴 `srs-fr-12-tv-chuyen-sau.md:1013` | `- **Path:** /api/v1/inbound/danh-gia-chat-luong-tv — **[CẦN BA CHỐT — BA-22 tuần 4]** … bản đang chạy có **hai** đường dẫn ứng viên và không cái nào khớp hẳn …` |
| `srs-fr-12-tv-chuyen-sau.md:1015` | `- **Authentication:** **mTLS + JWT Bearer RS256** (chuẩn hoá theo BR-INTG-02 …)` |
| `srs-fr-12-tv-chuyen-sau.md:1017` | `**Tác nhân:** Cổng Pháp luật quốc gia (API inbound)` |
| `srs-fr-12-tv-chuyen-sau.md:1479` | `**Mô tả:** Đánh giá chất lượng tư vấn từ doanh nghiệp, tiếp nhận qua API inbound từ Cổng PLQG.` |
| `srs-fr-12-tv-chuyen-sau.md:1487` | `| 3 | ma_danh_gia_cong | text | Y | UNIQUE, mã trên Cổng PLQG | — | Mã đánh giá Cổng |` |
| `srs-fr-12-tv-chuyen-sau.md:1488` | `| 4 | diem_so | number | Y | CHECK BETWEEN 1 AND 5 | — | Điểm đánh giá (1-5) |` |
| `srs-fr-12-tv-chuyen-sau.md:1489` | `| 5 | nhan_xet | text (long) | N | | — | Nhận xét từ DN |` |
| `srs-fr-12-tv-chuyen-sau.md:1491` | `| 7 | ngay_danh_gia | datetime | Y | | — | Ngày DN đánh giá |` |
| `srs-fr-12-tv-chuyen-sau.md:1063` | `| 2 | ma_danh_gia | text | thành công | mã trong PM |` *(Outputs FR-X.1-07 — PM có mã riêng, khác `ma_danh_gia_cong`)* |
| 🔴 `srs-v3.5.md:1368` | `| DANH_GIA_CHAT_LUONG_TV | R | R* | R* | R* | R* | R* | R* | C†R* | — | — | R* |` *(cột: QTHT · CB_NV_TW/BN/DP · CB_PD_TW/BN/DP · DN · NHT · TVV · CG — xem header `srs-v3.5.md:1300`)* |
| `srs-v3.5.md:1380` | `> † DN không truy cập CMS trực tiếp. Quyền Create/Read của DN thực hiện qua API inbound từ Cổng PLQG (SI-04, Nhóm XII). Permission Matrix ghi nhận quyền LOGIC, không phải quyền CMS UI.` |

### 2.3 Dòng nền — thời điểm DN được mời đánh giá (tiền đề vòng đời)

| Dòng | Nguyên văn (rút gọn) |
|---|---|
| `srs-fr-12-tv-chuyen-sau.md:225` | `| 5 | Gửi kết quả tư vấn cho DN (qua Cổng PLQG hoặc email) — **ngoại lệ kênh: KHÔNG áp thêm in-app** … |` *(Processing Phê duyệt, CHO_PHE_DUYET → DA_DUYET)* |
| 🔴 `srs-fr-12-tv-chuyen-sau.md:226` | `| 6 | Gửi thông báo DN mời đánh giá chất lượng — **chỉ thư điện tử** tới DOANH_NGHIEP.email (DN nhóm này chưa có tài khoản nên không có thông báo trong ứng dụng) …|` |
| `srs-fr-12-tv-chuyen-sau.md:1551` | `| CHO_PHE_DUYET | DA_DUYET | CB PD duyệt | Cùng đơn vị | Gửi KQ cho DN …; TB DN mời đánh giá chất lượng (chỉ thư điện tử) | FR-X.1-01 | BR-AUTH-05, BR-NOTIF-01 |` |
| `srs-fr-12-tv-chuyen-sau.md:1539` | `| DA_DUYET | approved | Đã duyệt, gửi kết quả cho DN |` |

⇒ **Trả lời câu hỏi "đánh giá do ai tạo, ở bước nào của vòng đời TVCS":**
Đánh giá **do doanh nghiệp chấm trên Cổng PLQG**, sau khi hồ sơ TVCS đạt **`DA_DUYET`** (CB PD duyệt → hệ thống
gửi kết quả + thư mời đánh giá cho DN — `:225`, `:226`, `:1551`). Bản ghi vào phần mềm **chỉ qua API inbound
UC153** (`:1006`, `:1013`, `:1017`, `:1479`); **không vai trò CMS nào có quyền Create** (`srs-v3.5.md:1368` —
mọi cột đều `R`/`R*`, riêng DN là `C†` nghĩa là tạo **qua API inbound**, không phải qua giao diện, `:1380`).
Khớp đúng chữ của phiếu *"do doanh nghiệp gửi sau khi nhận kết quả"*.

### 2.4 Đã tra gì để dám nói "SRS im lặng"

- Đọc **trọn** §3 Màn hình `srs-fr-12:1098–1231` (SCR-X1-01 + SCR-X1-02 + 5 mục DEPRECATED) — khối *Đánh giá
  chất lượng* chỉ được mô tả tại **một dòng duy nhất** `:1172`.
- Đọc **trọn** FR-X.1-07 `srs-fr-12:1000–1093` và entity `3.4.3.57 DANH_GIA_CHAT_LUONG_TV` `:1477–1500`.
- `grep -n "Chưa có\|empty\|Trạng thái trống\|rỗng"` trên `srs-fr-12` → chỉ ra `:1126` là **trạng thái rỗng của
  MÀN DANH SÁCH** (`"Chưa có nội dung tư vấn. [+ Thêm yêu cầu TV]"`), **không phải** của khối nhóm 4.
- `grep -rn "DANH_GIA_CHAT_LUONG_TV"` toàn thư mục `srs-v3.5/` → 5 vị trí ở `srs-fr-12` + 5 ở `srs-v3.5.md`;
  **không có** file nào khác định nghĩa thêm cột / vị trí / trạng thái rỗng cho khối này.
- Đã loại trừ `srs-fr-08-danh-gia.md`: file này là **Đánh giá hiệu quả công tác HTPL** (FR-VI-01…VI-10,
  UC83–UC91 — `srs-fr-08:84`, `:467`), **không** liên quan đánh giá chất lượng tư vấn; `grep "DANH_GIA_CHAT_LUONG_TV\|UC153"`
  trên file đó ra **rỗng**. Đã loại trừ `srs-fr-04-chuyen-gia-tvv.md` cho vế hiển thị (chỉ liên quan gián tiếp
  qua "điểm trung bình chuyên gia" `srs-fr-12:1009`, không quy định bảng ở SCR-X1-02).

---

## 3. BUG SCOPE LOCK — các dòng `Cn`

> Tách **đúng các vế trong expected của phiếu**, không thêm chức năng kế bên.
> `MATCH` → được chấm · `DIFF` → cấm Pass, BA confirm · `GAP` → cấm Pass, BA confirm.

```
C1 · Màn chi tiết TVCS có khối "Đánh giá chất lượng" (nhóm thứ 4 trong dãy khối)
   · srs-fr-12:1160 + :1172 + :1152 · MATCH · route TEST
   · Mở chi tiết 1 bản ghi TVCS → đọc tên + thứ tự các khối trên màn

C2 · Khối đó là BẢNG LIỆT KÊ các đánh giá chất lượng do doanh nghiệp gửi (mỗi đánh giá 1 dòng)
   · srs-fr-12:1172 + :1006 + :153 + :1479 · MATCH · route TEST
   · Trên bản ghi CÓ ≥2 đánh giá: đếm số dòng bảng = số bản ghi đánh giá của hồ sơ đó

C3 · Bảng có đủ 4 cột: Mã đánh giá · Điểm (thang 1-5) · Nhận xét của doanh nghiệp · Ngày đánh giá
   · srs-fr-12:1172 (đủ 4 cột) + entity :1487 (mã) :1488 (điểm 1-5) :1489 (nhận xét) :1491 (ngày)
   · MATCH · route TEST · Đọc hàng tiêu đề bảng, đối chiếu 4 khái niệm (không đối chiếu từng chữ nhãn)

C4 · Có dòng tổng hợp: điểm trung bình + số lượng đánh giá
   · srs-fr-12:1172 ("Tổng hợp: Điểm TB + Số lượng") · MATCH · route TEST
   · Đọc 2 con số tổng hợp, tự tính lại từ các dòng đang hiển thị và so
   ⚠ SRS IM LẶNG về VỊ TRÍ ("ở cuối bảng" là chữ của phiếu) → không chấm theo vị trí

C5 · Toàn bộ dữ liệu của khối là chỉ đọc (không sửa/xóa/nhập được từ giao diện)
   · srs-fr-12:1172 ("table (read-only)") + srs-v3.5.md:1368 (không vai trò CMS nào có C/U/D)
     + :1380 (DN tạo qua API inbound, không qua CMS) · MATCH · route TEST
   · Đếm phần tử tương tác ghi (nút Sửa/Xóa/ô nhập/upload) bên trong khối = 0
```

**Không có vế `DIFF`. Không có vế `GAP`.** SRS và expected đối tác khớp nhau trên cả 5 vế
⇒ **route toàn case = `TEST`**, sang Giai đoạn B đo.

**Nằm NGOÀI scope — CẤM biến thành tiêu chí chấm** (SRS im lặng hoặc expected không nhắc):
câu chữ trạng thái rỗng của khối · phân trang / sắp xếp / lọc trong bảng đánh giá · liên kết từ dòng đánh giá
sang chuyên gia · việc *"cập nhật điểm trung bình chuyên gia"* (`:1009`, `:1055` — thuộc UC153 phía máy chủ,
đo ở màn Chuyên gia, không phải màn này) · các khối khác của SCR-X1-02 (Tư liệu PL, Nhật ký, Công khai).

---

## 4. Tiền đề tối thiểu

### 4.1 Vai trò / tài khoản

**Vai trò được xem khối này:** theo `srs-v3.5.md:1368` — QTHT · CB_NV (TW/BN/ĐP) · CB_PD (TW/BN/ĐP) · CG đều
có quyền **đọc**, phạm vi theo đơn vị (`R*`, quy tắc scoping `srs-v3.5.md:1374–1378`). NHT và TVV = `—`.

| Vai trò | Tài khoản (env nội bộ `https://18.143.165.120.nip.io`) | Mật khẩu | Ghi chú |
|---|---|---|---|
| **CB NV cấp TW — ra verdict** | `cbnv_tw` (dự phòng `cbnv_tw_01`, `cbnv_tw_02`) | `Test@1234` | Nguồn `output/UAT_doi-tac/input/input.md:19, 38, 46`. Cấp TW thấy dữ liệu **mọi đơn vị** (`srs-v3.5.md:1375`) → dễ tìm bản ghi có đánh giá nhất |
| CB NV cấp ĐP — đối chứng scope (tùy chọn) | `cbnv_dp_01` | `Test@1234` | `input.md:31-33`. Chỉ dùng nếu cần phân biệt lỗi scope; **không bắt buộc** cho 5 vế trên |
| **CẤM ra verdict** | `admin` | — | Quyền rộng che lỗi phạm vi/chỉ-đọc |

Env đối tác `https://htpldn-uat.ospgroup.vn` dùng bộ tài khoản **khác** (`input.md:120–131`): `cbnv_tw` /
`Test@1234` đã kiểm chứng dùng được; mã xác thực lấy ở MailHog của **chính env đó** (`input.md:123`).
**Phải khai rõ đo trên env nào** — TKM phản hồi trên env đối tác.

### 4.2 Dữ liệu

| Cần | Số lượng | Vì sao | Trạng thái |
|---|---|---|---|
| Bản ghi TVCS bất kỳ trong phạm vi đơn vị của tài khoản | ≥1 | Đủ để chấm **C1** (khối tồn tại) | Dựng được: CB NV tạo mới qua `[+ Thêm yêu cầu TV]` (`srs-fr-12:1117`) |
| Bản ghi TVCS ở **`DA_DUYET`** | ≥1 | Đúng thời điểm vòng đời DN được mời đánh giá (`:226`, `:1551`) | Dựng được qua luồng chuẩn (§4.3) |
| **Bản ghi `DANH_GIA_CHAT_LUONG_TV` gắn cùng 1 hồ sơ TVCS** | **≥2** | **C2** (bảng liệt kê nhiều dòng) và **C4** (điểm TB phải khác điểm đơn lẻ mới chứng minh được là trung bình) | 🔴 **Nút thắt — xem §4.4** |

### 4.3 Công thức dựng TVCS lên `DA_DUYET` (từ SM-TVCS `srs-fr-12:1516–1526`)

```
CB NV tạo yêu cầu TV  -> TIEP_NHAN
CB NV [Phân công CG] (CG phải loai_tvv='CG', đang hoạt động, chuyên môn khớp lĩnh vực) -> PHAN_CONG
CG [Chấp nhận]        -> DANG_TU_VAN
CG nhập kết quả + tích "Hoàn thành" (ket_qua không rỗng, :212) -> HOAN_THANH -> [Auto] CHO_PHE_DUYET (:1550)
CB PD cùng đơn vị [Phê duyệt] -> DA_DUYET (:1551)
```
Env nội bộ: CG dùng được là `qa_tvvseed28` / `Test@1234` — đã được QA đổi `loaiTvv` TVV→CG ngày 21/07
(`input.md:114–117`). CB PD cấp TW: `cbpd_tw_01` (`input.md:28`, vì `cbpd_tw` đang fail đăng nhập).

### 4.4 🔴 Nút thắt tiền đề — dữ liệu đánh giá KHÔNG tạo được từ giao diện

SRS nói thẳng: **không có màn hình CMS nào tạo đánh giá** (`:1006`), tác nhân duy nhất là **Cổng PLQG qua API
inbound** (`:1017`), và **không vai trò CMS nào có quyền Create** (`srs-v3.5.md:1368`).
Ba rào chắn khi muốn seed bằng API:

1. **SRS chưa chốt đường dẫn.** `:1013` ghi rõ `[CẦN BA CHỐT — BA-22 tuần 4]`, bản đang chạy có **hai** đường
   dẫn ứng viên và **không cái nào khớp hẳn**. ⇒ **CẤM tự chọn / tự đoán endpoint.** Muốn dùng thì phải tra
   `/api/docs-json` hoặc bắt lời gọi thật của màn danh sách, rồi khai rõ đã dùng đường nào.
2. **Xác thực mTLS + JWT RS256** (`:1015`) — env UAT chưa cấp chứng thư, các đường `/public/*` bị chặn ngay
   ở bắt tay TLS (đã ghi nhận ở các đợt trước).
3. Kể cả gọi được, `ma_noi_dung_cong` (`:1028`) là **mã hồ sơ TV trên Cổng**, không phải mã `TVCS-…` của CMS —
   phải biết ánh xạ trước, không suy đoán.

**Hệ quả bắt buộc cho agent đo:**
- Bước 0 = **đi tìm bản ghi TVCS đã sẵn có đánh giá** (quét danh sách bằng tài khoản cấp TW, mở vài hồ sơ
  `DA_DUYET`; hoặc đọc lời gọi chi tiết TVCS xem trường đánh giá có phần tử không). Có → chấm đủ C1–C5.
- Không tìm được và không seed hợp lệ được → **C2 và C4 = `Chưa chốt`**, nêu đúng dữ kiện còn thiếu.
  **CẤM chấm Fail vì bảng rỗng. CẤM chấm Pass/"không phải lỗi" vì "nhìn thấy khối rồi".**
  C1 · C3 · C5 vẫn chấm được **nếu** giao diện dựng hàng tiêu đề bảng khi rỗng; nếu rỗng thì ẩn luôn cả bảng
  → C3 cũng `Chưa chốt` (SRS im lặng về cách trình bày khi rỗng).

---

## 5. Đường đo ngắn nhất + đối chứng độc lập

**Đường UI (1 đường duy nhất — luật khóa 3):**
1. Đăng nhập `cbnv_tw` / `Test@1234` (mã xác thực ở MailHog của đúng env). **Tải lại trang bằng địa chỉ**,
   ghi bó mã FE + `last-modified` + `etag` + chuỗi phiên bản ở chân sidebar.
2. Menu **Tư vấn → Tư vấn pháp luật chuyên sâu** (breadcrumb chuẩn `:1116`).
3. Mở **chi tiết** một bản ghi — ưu tiên bản ghi đã có đánh giá; nếu chưa xác định thì mở hồ sơ `DA_DUYET`
   (`:1539` — trạng thái sau đó DN mới được mời đánh giá).
4. Cuộn tới khối **"Đánh giá chất lượng"**: chụp 1 ảnh bắt trọn tên khối + hàng tiêu đề + các dòng + dòng
   tổng hợp. Đếm phần tử tương tác ghi trong khối (nút/ô nhập/upload).

**Đối chứng độc lập (đúng 1 đường, khác đường UI):**
- Đọc lại **phản hồi máy chủ của chính lời gọi chi tiết TVCS** mà màn vừa gọi (bắt trong danh sách lời gọi
  mạng khi mở màn — **KHÔNG tự đoán đường dẫn**; cần đường dẫn thì tra `/api/docs-json` hoặc đọc lời gọi
  của màn danh sách trước).
- So **từng trường** của phần đánh giá trong phản hồi với những gì bảng hiển thị: mã · điểm · nhận xét · ngày;
  và tự tính trung bình các điểm trong phản hồi rồi so với con số "điểm trung bình" trên màn (C4).
- Phản hồi trả **mảng rỗng** ⇒ kết luận **thiếu dữ liệu**, KHÔNG phải lỗi hiển thị (C2/C4 → `Chưa chốt`).
  Phản hồi **có dữ liệu** mà bảng vẫn rỗng ⇒ lỗi hiển thị phía giao diện (C2 FAIL).
- **CẤM** thử gọi thao tác ghi để "chứng minh chỉ đọc" — SRS không đặc tả endpoint ghi nào cho thực thể này
  (`:1006`), và đó là thao tác thay đổi môi trường ngoài vế Cn. Chấm C5 bằng **đếm phần tử tương tác ghi = 0**
  cộng ma trận quyền `srs-v3.5.md:1368`.

**Hai đường mâu thuẫn ⇒ CHƯA được chốt** — ghi cả hai, hỏi user.

---

## 6. Bẫy chấm sai

### 6.1 ⚠️ Bẫy **FAIL oan**

1. 🔴 **Bảng rỗng ≠ lỗi.** TKM đã nói *"chưa có dữ liệu test"*. Trạng thái rỗng hợp lệ (`"Chưa có dữ liệu"`,
   `"Không có đánh giá"`, khối trống chuẩn) là **thiếu dữ liệu**, không phải bug. **Chỉ khi** thấy
   *"Chức năng đang phát triển"* / ảnh giữ chỗ mới là **giao diện chưa dựng** → khi đó mới là lỗi.
2. **Chấm theo số thứ tự "Nhóm 4".** `:1160` liệt kê 5 khối, nhưng v3.5 đã **thêm khối 8b "Công khai chuyên
   trang"** (`:1174`) chỉ hiện khi `DA_DUYET` ⇒ số thứ tự trên màn **trôi được**. **Chấm theo TÊN khối**
   ("Đánh giá chất lượng"), không theo con số.
3. **Nhãn cột lệch chữ.** `:1172` ghi `Nhận xét DN` và `Ngày`; phiếu ghi `Nhận xét của doanh nghiệp` và
   `Ngày đánh giá`. **Cùng khái niệm** → không Fail. Chấm 4 **khái niệm**, không chấm từng chữ.
4. **Cách vẽ điểm.** `:1172` ghi *"Điểm (1-5 sao)"* = mô tả **thang điểm 1–5** (`:1488`
   `CHECK BETWEEN 1 AND 5`). Hiện `4`, `4/5`, hay 4 ngôi sao đều đạt — đừng Fail vì biểu tượng.
5. **Vị trí dòng tổng hợp.** SRS chỉ ghi *"Tổng hợp: Điểm TB + Số lượng"*, **im lặng** về "ở cuối bảng".
   Đặt trên đầu khối / cạnh tiêu đề đều đạt.
6. **Cột "Mã đánh giá" hiện mã của phần mềm chứ không phải mã Cổng.** SRS có **cả hai** khái niệm:
   `ma_danh_gia_cong` (`:1487`) và `ma_danh_gia` "mã trong PM" (`:1063`); `:1172` chỉ ghi *"Mã đánh giá"*,
   **không chỉ định** dùng mã nào → không Fail vì chọn mã nào.
7. **Không thấy khối ở chế độ thêm mới.** `:1172` điều kiện hiển thị = **"mode chi tiết"** → đúng đặc tả.
8. **Không có phân trang / sắp xếp / bộ lọc trong bảng đánh giá** — SRS im lặng, ngoài scope.

### 6.2 ⚠️ Bẫy **PASS oan**

1. 🔴 **Thấy tiêu đề khối là Pass.** Expected có **5 vế**. Nhìn thấy chữ "Đánh giá chất lượng" mới xong C1;
   C2 (có dòng dữ liệu) · C3 (đủ 4 cột) · C4 (tổng hợp) · C5 (chỉ đọc) đều chưa đo.
2. 🔴 **Bảng rỗng mà chấm Pass hoặc "không phải lỗi".** Không đo được thì là **`Chưa chốt`** — Flow 04 cấm
   kết luận "không phải lỗi" chỉ vì không tái hiện được.
3. 🔴 **Chấm điểm trung bình bằng mắt.** Phải **tự tính lại** trung bình từ chính các dòng đang hiển thị rồi
   so. Chỉ 1 dòng đánh giá thì trung bình **luôn** bằng điểm đó ⇒ **không chứng minh được gì** — bắt buộc
   **≥2 đánh giá** trên cùng hồ sơ mới chốt được C4.
4. **Nhầm nguồn điểm trung bình.** Thực thể `TU_VAN_CHUYEN_SAU` có trường `diem_danh_gia_dn` thang **0–10**
   (`srs-fr-12:1355`), khác thang **1–5** của `DANH_GIA_CHAT_LUONG_TV.diem_so` (`:1488`). Nếu giao diện lấy
   nhầm nguồn, con số vẫn "hiện ra" nhưng **sai bản chất** → chỉ đối chứng bằng phép tự tính mới bắt được.
5. **Chấm "chỉ đọc" bằng cảm nhận.** "Không thấy nút Sửa" chưa đủ — phải **đếm** phần tử tương tác ghi trong
   khối, gồm cả ô nhập bị vô hiệu hóa nhưng vẫn gửi được, và đọc kèm `srs-v3.5.md:1368`.
6. **Dùng `admin`.** Quyền rộng che cả lỗi phạm vi lẫn lỗi chỉ-đọc → verdict vô hiệu.
7. **Bản dựng cũ trong tab.** Tab mở lâu vẫn chạy bó mã cũ → **tải lại bằng địa chỉ**, ghi vân tay bản dựng.
8. **Nhầm env.** TKM báo trên env đối tác `htpldn-uat.ospgroup.vn`; đo trên env nội bộ `18.143.165.120.nip.io`
   thì verdict chỉ có hiệu lực cho env + bản dựng đã đo — phải ghi câu giới hạn này.

---

## 7. Kết luận sơ bộ — route

| | |
|---|---|
| **Quan hệ SRS ↔ expected** | **5/5 vế `MATCH`** — không vế nào `DIFF`, không vế nào `GAP` |
| **Route** | 🟢 **`TEST`** — sang Giai đoạn B, chốt Pass/Reopen bằng kết quả đo |
| **Câu hỏi BA** | **Không có** ở giai đoạn này |
| **Rủi ro lớn nhất** | **Tiền đề dữ liệu**, không phải đặc tả. Đánh giá chỉ vào qua API inbound (`:1006`, `:1017`), đường dẫn **SRS chưa chốt** (`:1013`), xác thực mTLS (`:1015`) ⇒ nếu env không sẵn bản ghi đánh giá nào thì **C2 + C4 = `Chưa chốt`**, không phải Fail |
| **Chưa có verdict** | Đúng — file này chỉ khóa chuẩn chấm |

**Nhắc lại luật khóa 5:** sau khi mở màn, **cấm** đổi quan hệ `MATCH/DIFF/GAP` để khớp kết quả đo. Đổi chỉ hợp
lệ khi dẫn được **dòng SRS mới đọc được**.

**Nhắc ca biên Flow 04:** không có ảnh "lỗi cũ" của chính mình ⇒ **không suy ra được "fix có tác dụng"**, chỉ
kết luận được **hiện trạng đúng/sai so với đặc tả**. Viết đúng như vậy.

**Ảnh chụp lưu đúng:** `output/UAT_doi-tac/reverify-week-5/F6-flow04-devfix-2026-08-07/image/`.
