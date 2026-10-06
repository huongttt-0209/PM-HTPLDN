# Chuẩn chấm đã khóa — LKHDG_12 (dòng 126)

**Case:** Xuất Excel danh sách đợt đánh giá — không áp bộ lọc đang bật
**Nguồn khối CÁCH VERIFY được khóa:** `output/UAT_doi-tac/flowtest-kiemdinh/bug-report.md:107-128` (file prompt chỉ định)
**Nguồn đặc tả:** `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/` — đã TỰ MỞ ĐẾM LẠI ngày 2026-08-07
**Người viết chuẩn:** agent đọc (không chạm trình duyệt) · viết 2026-08-07

---

## 1. Lỗi gốc (Expected/Actual của phiếu) — phiếu gốc gộp 3 vế

Phiếu đối tác dòng 126 gộp **3 vế**. Vòng trước (2026-08-06, V1.0.8 env dev) đã tách và đo từng vế:

| Vế | Đối tác ghi | Hiện trạng sau vòng 06/08 | Có dùng để chấm verdict không? |
|---|---|---|---|
| **(a)** | "Hệ thống xuất danh sách **không đúng với tiêu chí lọc**" | ❌ **VẪN TÁI HIỆN nguyên vẹn** trên 2 bộ lọc khác cột nhau (màn 19 → tệp 20 dòng; màn 4 → tệp 20 dòng; 2 tệp cùng 8520 byte) | ✅ **CÓ — vế DUY NHẤT quyết định verdict** |
| **(b)** | "File Excel xuất ra **thiếu cột** *Số vụ việc*, *Người tạo*, *Ngày tạo*" | ✅ **ĐÃ HẾT LỖI** — tệp có đủ 10 cột: Mã KH · Tên đợt · Tần suất · Đối tượng · **Số vụ việc** · Từ ngày · Đến ngày · Trạng thái · **Người tạo** · **Ngày tạo** | ❌ **KHÔNG** — đặc tả im lặng về tập cột của tệp xuất |
| **(c)** | "Cột *Tần suất* / *Đối tượng* / *Trạng thái* hiển thị **không dấu**" (thực chất là **mã enum thô** `TRON_NAM`, `VU_VIEC`, `LAP_KE_HOACH`) | ✅ **ĐÃ HẾT LỖI** — tệp ghi nhãn tiếng Việt có dấu ("Sơ bộ 6 tháng", "Tròn năm", "Lập kế hoạch", "Vụ việc"…) | ❌ **KHÔNG** — đặc tả im lặng về định dạng nhãn trong tệp |

**Kết luận vế:** verdict của cả phiếu chỉ do **vế (a)** quyết định. Vế (b) + (c) đã hết lỗi vòng trước và **đặc tả im lặng** ⇒ vòng này **chỉ ghi nhận, tuyệt đối không dùng để Pass hay Fail**. Nếu vòng này thấy (b)/(c) tái phát (mất cột, quay lại mã enum thô) thì **ghi nhận riêng, không đổi verdict** — vì không có căn cứ đặc tả.

**Expected (rút gọn):** tệp Excel xuất ra chứa **đúng tập bản ghi đang hiển thị sau khi lọc** — không thừa, không thiếu.
**Actual vòng 06/08:** tệp luôn chứa **toàn bộ 20 bản ghi** bất kể bộ lọc; đường dẫn yêu cầu xuất **có mang** tham số lọc nhưng phần sinh tệp bỏ qua ⇒ lỗi nằm phía máy chủ.

---

## 2. Dẫn đặc tả (đã tự mở đếm lại)

> 🔴 **Đã tự mở file đọc từng dòng ngày 2026-08-07.** Cả 2 trích dẫn cũ đều **LỆCH**, trong đó `srs-v3.5.md:5525` lệch **+45 dòng** (không phải +2 như cảnh báo lệch dòng của `srs-fr-08`) — hồ sơ cũ **KHÔNG** được bê nguyên.

| Trích dẫn cũ (trong hồ sơ) | Trích dẫn ĐÚNG hiện tại | Nguyên văn dòng (≤200 ký tự) |
|---|---|---|
| `srs-v3.5.md:5525` — BR-DATA-06 | 🔴 **`srs-v3.5.md:5570`** (lệch **+45**) | `\| BR-DATA-06 \| **Export Excel:** Mọi danh sách có tính năng xuất Excel. File xuất theo bộ lọc hiện tại, không vượt quá 10,000 rows/file \| Pattern IP-01 \| Toàn bộ CRUD list \| Báo cáo nhóm IX có xuất PDF theo khung TT 17/2025 \|` |
| `srs-fr-08-danh-gia.md:821` — nút [Xuất Excel] | 🔴 **`srs-fr-08-danh-gia.md:823`** (lệch **+2**, đúng như điều phối xác nhận) | `\| 2 \| toolbar \| Tiêu đề trang \| C02 \| "Theo dõi Đánh giá Hiệu quả HTPL" + [+ Tạo đợt đánh giá] [Xuất Excel] [Làm mới] \| click → tương ứng \| Luôn. [+ Tạo đợt] khi có quyền "Quản lý đánh giá" \|` |
| `srs-fr-11-bao-cao.md:1276-1280` — bản nhắc lại BR-DATA-06 trong nhóm IX | 🔴 **`srs-fr-11-bao-cao.md:1281-1285`** (lệch **+5**) | `### BR-DATA-06: Export Excel` (`:1281`) · `\| BR-DATA-06 \| Mọi danh sách có tính năng xuất Excel. File xuất theo bộ lọc hiện tại… \| Toàn bộ FR-IX \| Báo cáo nhóm IX có xuất PDF \|` (`:1285`) |
| `srs-fr-08-danh-gia.md:829-837` — vùng bảng/filter (dùng trong tiêu chí cũ) | 🔴 **`:824-829`** = filter-bar · **`:831-839`** = cột bảng (xem §7) | xem §7 bên dưới |
| *(liên quan case 127, ghi để chống lây lỗi)* `srs-fr-08-danh-gia.md:837` — Hành động Sửa | 🔴 **`srs-fr-08-danh-gia.md:839`** (lệch **+2**) | `\| 18 \| table \| Hành động \| icon-group \| Xem / Sửa (chỉ LAP_KE_HOACH/PHAN_CONG) / Xóa (chỉ LAP_KE_HOACH) \| click → tương ứng \| Luôn \|` |

**Vì sao lệch:** commit `2699898` (2026-08-06 22:43 — *"Áp 7 quyết định BA từ phiếu UAT tuần 5 vào SRS"*) chèn **+2 dòng** vào `srs-fr-08-danh-gia.md` (2 ô nhập mới `:852` Cơ quan được đánh giá `[CR-10]` và `:854` Tài liệu đính kèm `[CR-07]`, cộng 2 dòng ở vùng §Inputs `:113`) và **+44 dòng ròng** vào `srs-v3.5.md`. Đã đối chiếu bản trước commit: `srs-v3.5.md` BR-DATA-06 ở `:5526` trước commit, `:5525` ở bản 04/08 (tức trích dẫn cũ **đúng lúc viết**, nay đã hỏng).

### A. BR-DATA-06 CÓ áp cho màn này không? — **CÓ**

Đọc nguyên bảng B.2 (`srs-v3.5.md:5561-5574`), 3 cột quyết định của dòng `:5570`:

| Cột | Giá trị nguyên văn | Diễn giải |
|---|---|---|
| **Phát biểu** | *"Mọi danh sách có tính năng xuất Excel. **File xuất theo bộ lọc hiện tại**, không vượt quá 10,000 rows/file"* | Ràng buộc đúng vế (a) |
| **Áp dụng FR** | **"Toàn bộ CRUD list"** | Màn SCR-VI-01 Phần A là danh sách CRUD ⇒ nằm trong phạm vi |
| **Ngoại lệ** | **"Báo cáo nhóm IX có xuất PDF theo khung TT 17/2025"** | Chỉ miễn **nhóm IX** và chỉ cho **xuất PDF**. **KHÔNG** miễn nhóm VI, **KHÔNG** miễn xuất Excel |

⚠️ **Điểm phải nói thẳng (không được giấu):** §6 *Tổng quan BR sử dụng* của chính nhóm VI (`srs-fr-08-danh-gia.md:1211-1222`) **KHÔNG liệt kê BR-DATA-06** — chỉ có BR-DATA-03 (`:1215`), BR-DATA-04 (`:1216`), BR-DATA-05 (`:1217`). Đây là **thiếu sót của bảng tổng quan chương**, **không phải một ngoại lệ**: cột "Ngoại lệ" của `:5570` là chỗ duy nhất đặc tả cho phép miễn trừ, và nó không nêu nhóm VI. Theo quy tắc dự án (*"BR có 'Áp dụng: Toàn bộ…' = default áp dụng; ngoại lệ phải QUOTE line SRS, không tự suy luận"*) ⇒ **BR-DATA-06 áp cho màn này**.
Bản nhắc lại ở `srs-fr-11-bao-cao.md:1285` ghi "Áp dụng: Toàn bộ FR-IX" — đó là **bản sao cục bộ trong chương IX**, không thu hẹp phạm vi của bản gốc ở Phụ lục B.

### Đặc tả IM LẶNG về (giữ nguyên kết luận tiêu chí gốc, đã kiểm lại)

- **Tập cột của TỆP xuất** — cả nhóm VI (FR-VI-01…10, `srs-fr-08-danh-gia.md:84-805`) không có FR nào đặc tả luồng xuất Excel danh sách. `grep "Xuất Excel" srs-fr-08-danh-gia.md` chỉ ra 2 chỗ: `:823` (nút trên toolbar) và `:915` (tab Báo cáo, xuất theo template TT17/2025 — **màn khác**).
- **Định dạng nhãn trong TỆP xuất** — bảng `:831-839` là đặc tả **màn hình**, không phải tệp.

---

## 3. Precondition + dữ liệu

| Hạng mục | Giá trị |
|---|---|
| **Tài khoản** | **`cbnv_tw` / `Test@1234`** — CB Nghiệp vụ Trung ương (CB_NV_TW, `BTP · TW`). Nguồn: `output/UAT_doi-tac/input/input.md:19`. Đăng nhập qua UI thật, mã 6 số lấy ở MailHog `http://18.143.165.120:8025` |
| **KHÔNG dùng** | `admin` / QTHT để ra verdict (quyền rộng che lỗi phân quyền). Vai trò này **trùng khít vai trò đối tác dùng trong video** (CB_NV_TW, BTP·TW) ⇒ không được đổi |
| **Môi trường** | `https://18.143.165.120.nip.io` — env **NỘI BỘ**, KHÔNG phải env nghiệm thu đối tác (`htpldn-uat.ospgroup.vn`) |
| **URL màn** | `https://18.143.165.120.nip.io/danh-gia/ke-hoach/danh-sach` (Đánh giá hiệu quả → Kế hoạch đánh giá → Danh sách) |
| **Yêu cầu tối thiểu về dữ liệu** | Danh sách phải có **≥2 giá trị khác nhau ở cột định lọc**, và `n_lọc` **<** `n_tổng`. Nếu mọi đợt cùng Tần suất thì lọc không cắt được gì ⇒ **phép đo vô nghĩa** ⇒ phải tạo thêm 1 đợt khác Tần suất trước khi đo |
| **Dữ liệu vòng trước** | `n_tổng = 20` đợt, phủ 7 trạng thái + 2 giá trị Tần suất. Vòng 06/08 đã **seed 1 đợt** `DG-20260806-0001` (Tần suất *Sơ bộ 6 tháng*) vì 19 đợt sẵn có đều `TRON_NAM`. **Kiểm lại đợt seed này còn tồn tại không** — mất nó là mất luôn điều kiện đo lượt 1 |

---

## 4. Các bước đo (thao tác UI thật)

> Chép từ khối CÁCH VERIFY được khóa (`flowtest-kiemdinh/bug-report.md:112-115`), diễn giải thao tác cho rõ.

**Bước 0 (bắt buộc, ngoài khối — yêu cầu của lô F3):** ghi lại **chuỗi phiên bản chân sidebar** + **tên bó mã FE** (`assets/index-*.js`) ngay sau khi tải lại trang. So với 2 vân tay đã biết: `assets/index-DThrFe1_.js` (đo 06/08 lúc 00:32 & 08:50) và `assets/index-DIABnbIr.js` (đo 06/08 lúc 18:44). **Trùng khít một trong hai ⇒ báo điều phối TRƯỚC khi chốt verdict** (không có bằng chứng dev deploy lại).

1. Mở màn danh sách, **CHƯA lọc**. Ghi lại **tổng số kết quả** đọc ở chân bảng (`"Hiển thị 1-N / N kết quả"`) = `n_tổng`.
2. Chọn **Tần suất = "Tròn năm"** → bấm **[Tìm kiếm]**. Ghi lại số kết quả sau lọc = `n_lọc` (**phải < `n_tổng`**). Ghi lại **danh sách mã đợt đang hiện trên màn** (cuộn hết mọi trang nếu `n_lọc` > 20).
3. Bấm **[Xuất Excel]** → **mở tệp**, đếm **số dòng dữ liệu** (không kể dòng tiêu đề) và **liệt kê cột "Mã KH"**. Ghi lại **kích thước byte** của tệp.
4. Lặp lại bước 2-3 với **cột lọc KHÁC**: **Tần suất = "Tất cả"**, **Trạng thái = "Hoàn thành"** → **[Tìm kiếm]** → **[Xuất Excel]** → đếm lại.

**Ghi chú thao tác (không phải điều kiện chấm):** hồ sơ thứ hai + ô sheet ghi bước 4 là *"bấm **[Xóa bộ lọc]** rồi Trạng thái = Hoàn thành"*. Hai cách tương đương — đều đưa về trạng thái **chỉ còn bộ lọc Trạng thái đang bật**; SRS `:829` xác nhận màn có cả nút *Tìm kiếm / Xóa bộ lọc*. Chọn cách nào cũng được, miễn **xác nhận bằng URL** rằng bộ lọc Tần suất đã tắt (`?trangThai=HOAN_THANH&page=1`, không còn `tanSuat=`).

**Cách MỞ TỆP để đếm (kinh nghiệm đã có, chọn 1):**
- **Ưu tiên** — giải nén `.xlsx` **ngay trong trang**: bắt response của yêu cầu xuất → parse EOCD + `DecompressionStream` → đọc `xl/worksheets/sheet1.xml` + `xl/sharedStrings.xml`, chỉ trả về số dòng + tập mã (đừng dump base64). Vòng trước đã dùng đúng cách này.
- Nếu tệp có về `~/Downloads` thì đọc bằng `openpyxl`.
- 🔴 **Cấm** kết luận từ mã HTTP 200 hoặc số byte đơn thuần — 200 + binary chỉ chứng minh **tạo được tệp**, không chứng minh **tệp đúng**.

---

## 5. Đường đo thứ hai (đối chứng độc lập)

Gọi thẳng máy chủ **cùng một chuỗi truy vấn**, so 2 đường dẫn (JWT `access_token` là cookie ⇒ `fetch(..., {credentials:'include'})` chèn trong trang là xác thực được):

| Chuỗi truy vấn | `GET /api/v1/ke-hoach-danh-gias` | `POST /api/v1/ke-hoach-danh-gias/export` |
|---|---|---|
| `?trangThai=HOAN_THANH&page=1&pageSize=20` | số bản ghi trả về = ? | số byte tệp = ? |
| `?tanSuat=TRON_NAM&page=1&pageSize=20` | số bản ghi trả về = ? | số byte tệp = ? |
| `?page=1&pageSize=20` (KHÔNG lọc) | số bản ghi trả về = ? | số byte tệp = ? |

**Đọc kết quả:** nếu cột `GET` biến thiên theo bộ lọc mà cột `POST …/export` **giữ nguyên số byte ở cả 3 dòng** ⇒ lỗi vẫn còn, nằm **phía máy chủ** (giá trị lọc hợp lệ và được hiểu đúng ở đường danh sách nhưng bị bỏ qua ở đường xuất tệp). Đó đúng là kết quả vòng 06/08: `4 / 19 / 20` bản ghi ↔ `8519 / 8519 / 8519` byte.
**Mâu thuẫn UI vs API** (một bên đúng, một bên sai) ⇒ ghi CẢ HAI vào bug entry, không tự chọn bên nào.

---

## 6. ✅ PASS khi / ❌ FAIL nếu — **CHÉP NGUYÊN VĂN** từ khối CÁCH VERIFY

> Nguồn: `output/UAT_doi-tac/flowtest-kiemdinh/bug-report.md:116-123`. **Cấm sửa, cấm nới, cấm thêm điều kiện.**

```
✅ PASS khi: cả 2 lượt, số dòng dữ liệu trong tệp = đúng n_lọc của lượt đó, VÀ tập "Mã KH"
   trong tệp trùng khít tập mã đang hiện trên màn (so từng mã, không chỉ so số lượng).
❌ FAIL nếu: tệp chứa ≥1 mã không thuộc tập sau lọc, hoặc số dòng ≠ n_lọc, hoặc 2 lượt lọc
   khác nhau lại cho 2 tệp cùng kích thước byte.
⚠️ Đừng chấm Fail vì tệp thiếu cột hay vì định dạng nhãn — đặc tả không quy định tập cột của
   tệp xuất; chỉ chấm đúng phần "theo bộ lọc hiện tại" của BR-DATA-06.
⚠️ Đừng kết luận "đã fix" khi chỉ thấy đường dẫn yêu cầu xuất CÓ mang tham số lọc — giao diện
   gửi đúng tham số ngay cả khi đang lỗi; phải mở tệp đếm dòng.
```

---

## 7. Độ phủ biến thể bắt buộc

### 7.1 Kiểm kê đầy đủ cột lọc của màn (đọc `srs-fr-08-danh-gia.md:824-829`, vùng `filter-bar`)

| # SRS | Dòng | Thành phần | Loại | Giá trị / enum | Số giá trị enum |
|---|---|---|---|---|---|
| 3 | `:824` | Ô tìm kiếm | C09 | Từ khóa (tên đợt, mã đợt) | — (văn bản tự do) |
| 4 | `:825` | **Lọc tần suất** | C10 dropdown | `Tất cả / SO_BO_6_THANG / TRON_NAM` | **2** (+ "Tất cả") |
| 5 | `:826` | **Lọc đối tượng** | C10 dropdown | `Tất cả / VU_VIEC / DAO_TAO / TONG_HOP` | **3** (+ "Tất cả") |
| 6 | `:827` | **Lọc trạng thái** | C10 dropdown | `Tất cả / LAP_KE_HOACH / PHAN_CONG / CHO_DUYET_PC / THUC_HIEN / BAO_CAO / CHO_PHE_DUYET / HOAN_THANH / HUY` | **8** (+ "Tất cả") |
| 7 | `:828` | Khoảng ngày | C11 range | Từ ngày – Đến ngày (dd/mm/yyyy) | — (khoảng) |
| 8 | `:829` | Nút Tìm kiếm / Xóa bộ lọc | C08 | — | — |

⇒ **5 ô lọc** (3 dropdown enum + 1 ô từ khóa + 1 khoảng ngày) · **13 giá trị enum** tổng cộng (2 + 3 + 8).

### 7.2 Tối thiểu phải đo mấy lượt — **2 lượt** (đúng bằng khối đã khóa, KHÔNG nới, KHÔNG siết)

| Lượt | Cột lọc | Giá trị | Bắt buộc? |
|---|---|---|---|
| 1 | **Tần suất** (`:825`) | `Tròn năm` (`TRON_NAM`) | ✅ **BẮT BUỘC** |
| 2 | **Trạng thái** (`:827`) | `Hoàn thành` (`HOAN_THANH`), Tần suất về "Tất cả" | ✅ **BẮT BUỘC** |
| — | Đối tượng (`:826`) · từ khóa (`:824`) · khoảng ngày (`:828`) | — | ❌ **KHÔNG bắt buộc** — khối khóa chỉ đòi 2 cột. Đo thêm thì ghi nhận, **không** dùng để Fail |

**Lý do khối khóa đòi 2 cột khác nhau:** để loại giả thuyết "chỉ hỏng riêng 1 tham số". Đo 1 lượt là **không đủ** để Pass.

### 7.3 Dạng dữ liệu phải phủ — M = 5 (giữ nguyên từ tiêu chí gốc `flowtest-kiemdinh/tieuchi/LKHDG_12.md:93-103`)

1. Đợt Tần suất = **Sơ bộ 6 tháng** (`SO_BO_6_THANG`) · 2. Đợt Tần suất = **Tròn năm** (`TRON_NAM`) · 3. Đợt Đối tượng = **Vụ việc** (`VU_VIEC`) · 4. Đợt Đối tượng = **Đào tạo hoặc Tổng hợp** · 5. **≥2 giá trị Trạng thái khác nhau**.
Vòng 06/08 đạt **M = 5/5** với N = 20 dòng. Nếu dữ liệu env đã bị reset thì **seed lại cho đủ M trước khi đo**, và khai rõ đã seed gì trong báo cáo.

---

## 8. ⚠️ Bẫy / rule chống kết luận oan

1. **🔴 Bẫy số 1 — URL có tham số lọc ≠ đã fix.** Giao diện gửi đúng `?tanSuat=…` / `?trangThai=…` **ngay cả khi đang lỗi**. Vòng 06/08 URL có `?trangThai=HOAN_THANH` mà tệp vẫn 20 dòng. **Phải mở tệp đếm dòng.**
2. **🔴 Bẫy số 2 — 200 OK / có byte ≠ đúng.** Bằng chứng phải là **nội dung tệp** (số dòng + tập mã), không phải mã HTTP.
3. **KHÔNG chấm Fail vì tệp thiếu cột / nhãn sai định dạng.** Đặc tả im lặng (§2). Vế (b)(c) đã hết lỗi vòng trước — nếu tái phát thì **ghi nhận riêng**, không đổi verdict.
4. **"Mã KH" là nhãn quan sát được trong tệp, KHÔNG phải tên do đặc tả quy định.** SRS `:831` gọi cột trên **màn** là *"Mã đợt"* (format `DG-{YYYYMMDD}-{SEQ}`). Nếu dev đổi tiêu đề cột trong tệp thành "Mã đợt" ⇒ **không được chấm Fail vì chuyện đó**; tìm cột theo **nội dung** (chuỗi `DG-…` / `KHDG-…`), không theo tiêu đề.
5. **So TỪNG MÃ, không chỉ so số lượng.** 2 tập cùng số lượng vẫn có thể khác phần tử — điều kiện PASS đòi "trùng khít".
6. **`n_lọc` phải < `n_tổng`.** Nếu bộ lọc không cắt bớt gì thì tệp đúng-hay-sai đều ra cùng kết quả ⇒ **phép đo vô nghĩa**, không được Pass trên nền đó.
7. **Nếu `n_lọc` > 20 (1 trang):** phải cuộn/lật hết trang để lấy đủ tập mã trên màn trước khi so — `:841` quy định 20 mục/trang.
8. **Nhãn trạng thái trong tệp vòng trước** có *"Đang đánh giá"* và *"Đã đánh giá"* — hai chuỗi này **không nằm** trong enum `:827` (`PHAN_CONG` / `BAO_CAO` …). Đây là **phát hiện tình cờ, ghi candidate riêng**, **KHÔNG dùng để chấm LKHDG_12** (đặc tả im lặng về nhãn trong tệp).
9. **Bản dựng.** Tải lại trang rồi mới đo; ghi bó mã FE. Tab MCP mở lâu vẫn chạy JS cũ ⇒ đã có tiền lệ báo Reopen oan.
10. **Hiệu lực verdict.** Đo trên env **nội bộ** `18.143.165.120.nip.io`; đối tác nghiệm thu trên `htpldn-uat.ospgroup.vn` bản V1.0 ⇒ Pass (nếu có) là **Pass tạm**, phải ghi rõ giới hạn hiệu lực trong ô sheet.
11. **Ảnh chụp mới đặt ở đâu:** xem §10.

---

## 9. Đối chiếu 3 chiều khối CÁCH VERIFY

**Kết luận: GIỐNG NHAU ở TOÀN BỘ phần quyết định chấm điểm. Chỉ lệch chữ nghĩa + đường dẫn ảnh ⇒ dùng bản của file (1) theo chỉ định prompt.**

| Yếu tố quyết định chấm | (1) `flowtest-kiemdinh/bug-report.md:107-128` | (2) `reverify-bug-devfix-2026-08-06/…/bug-report-LKHDG.md:207-227` | (3) Ô sheet (`audit/LKHDG_12-ketqua-verify-CU.md:23-43`) | Kết |
|---|---|---|---|:-:|
| Precondition (tài khoản, URL, yêu cầu ≥2 giá trị khác nhau) | `cbnv_tw`/`Test@1234` + `/danh-gia/ke-hoach/danh-sach` | y hệt từng chữ | y hệt từng chữ | **GIỐNG** |
| Số lượt đo | **2** | **2** | **2** | **GIỐNG** |
| Cột lọc dùng | Tần suất + Trạng thái | Tần suất + Trạng thái | Tần suất + Trạng thái | **GIỐNG** |
| Giá trị lọc | "Tròn năm" · "Hoàn thành" | "Tròn năm" · "Hoàn thành" | "Tròn năm" · "Hoàn thành" | **GIỐNG** |
| Bước 1-3 | y hệt | y hệt | y hệt | **GIỐNG** |
| **✅ PASS khi** | 2 câu, "= đúng n_lọc" + "trùng khít tập Mã KH, so từng mã" | **y hệt từng chữ** | **y hệt từng chữ** | **GIỐNG** |
| **❌ FAIL nếu** | 3 vế: ≥1 mã lạ · số dòng ≠ n_lọc · 2 tệp cùng byte | **y hệt từng chữ** | **y hệt từng chữ** | **GIỐNG** |
| ⚠️ Bẫy #1 (thiếu cột / nhãn) | y hệt | y hệt | y hệt | **GIỐNG** |
| ⚠️ Bẫy #2 (URL có tham số) | không có phần trong ngoặc | thêm `(lượt này URL có ?trangThai=HOAN_THANH mà tệp vẫn 20 dòng)` | y hệt (2) | **LỆCH — chỉ là ví dụ minh họa, không đổi điều kiện** |

**Điểm lệch duy nhất về THAO TÁC (không phải điều kiện chấm) — bước 4:**

| | Nguyên văn bước 4 |
|---|---|
| (1) **file prompt chỉ định — DÙNG BẢN NÀY** | *"Lặp lại bước 2-3 với cột lọc KHÁC: **Tần suất = "Tất cả", Trạng thái = "Hoàn thành"**."* |
| (2) + (3) | *"Lặp lại bước 2-3 với cột lọc KHÁC: **[Xóa bộ lọc] rồi Trạng thái = "Hoàn thành"**."* |

⇒ Hai cách **tương đương về trạng thái cuối** (chỉ còn lọc Trạng thái đang bật) và SRS `:829` xác nhận màn có cả 2 lối. **Không phải lệch quyết định chấm điểm.** Theo chỉ định prompt: **dùng bản (1)**; xác nhận bằng URL `?trangThai=HOAN_THANH&page=1` không còn `tanSuat=`.

**Điểm lệch về đường dẫn bằng chứng (kiểm tra thực tế trên đĩa — mục D):**

| Đường dẫn ghi trong khối | Có thật trên đĩa? | Vị trí thực |
|---|:-:|---|
| (1) `frames/LKHDG_12/t009.06s.jpg` · `t018.13s.jpg` (ảnh lỗi gốc đối tác) | ✅ **CÓ** | `output/UAT_doi-tac/flowtest-kiemdinh/frames/LKHDG_12/` (8 frame: `t000.00s` → `t021.25s`) |
| (1) `image/LKHDG_12-man-loc-HoanThanh-4ketqua-V108-2026-08-06.png` + `…-file-xuat-…xlsx` | ✅ **CÓ** | `output/UAT_doi-tac/flowtest-kiemdinh/image/` |
| (2)+(3) `image/LKHDG_12-luot1-man-loc-TronNam-19ketqua-V108.png` · `…-luot2-man-loc-HoanThanh-4ketqua-V108.png` | ✅ **CÓ** | `output/UAT_doi-tac/reverify-bug-devfix-2026-08-06/bug-reports/image/` |
| Video gốc đối tác `partner-evidence/LKHDG_12.webm` | ✅ **CÓ** (2 bản) | `flowtest-kiemdinh/partner-evidence/` và `reverify-bug-devfix-2026-08-06/partner-evidence/` |

⇒ **Không có ảnh nào 404.** Hai hồ sơ chỉ trỏ vào thư mục `image/` của riêng mình.

---

## 10. Cảnh báo cho agent đo

1. **🔴 Verdict case này phải cập nhật vào CẢ HAI file bug-report** (không được sửa 1 file rồi thôi):

   | # | File | Chỗ phải sửa |
   |---|---|---|
   | (1) | `output/UAT_doi-tac/flowtest-kiemdinh/bug-report.md` | entry **`BUG-LKHDG_12-EXPORT-FILTER`** — dòng Bảng tổng hợp (`:20`, cột *Verdict đợt này* / *Chủ việc* / *Trạng thái*) **+** dòng blockquote `> **Re-test:**` (`:29-31`) — **OVERWRITE 1 dòng latest, KHÔNG append lịch sử** **+** trích dẫn `srs-v3.5.md:5525` ở `:54` phải sửa thành **`:5570`** |
   | (2) | `output/UAT_doi-tac/reverify-bug-devfix-2026-08-06/bug-reports/bug-report-LKHDG.md` | entry **`BUG-LKHDG-EXPORT-FILTER`** — §Tổng hợp (`:21-29`, snapshot LATEST ≤5 dòng), Severity breakdown (`:33-35`), Bug Summary Table (`:41`, cột Status + cột **SRS Reference** đang ghi `srs-v3.5.md:5525` + `srs-fr-08-danh-gia.md:821` ⇒ sửa thành **`:5570`** và **`:823`**), blockquote `> **Re-test:**` (`:48-50`), header **`Ngày`** (`:8`) phải sync với timestamp mới |

2. **KHÔNG đổi tên file thành `Pass-…` dù case này Pass.** Cả 2 file còn bug khác chưa đóng: (1) còn `BUG-QLHSDNHTCP_03-SLA` = **Chờ BA**; (2) còn `BUG-LKHDG-SUA-PHANCONG` (LKHDG_16) = **Open**. Rename khi chưa 100% Closed là sai quy tắc.

3. **Ảnh/tệp bằng chứng vòng này lưu ở đâu:** đặt vào thư mục `image/` của **file bug-report mình đang cập nhật** — `flowtest-kiemdinh/image/` cho hồ sơ (1), `reverify-bug-devfix-2026-08-06/bug-reports/image/` cho hồ sơ (2). **Cấm** tạo subfolder mới (`evidence-*`, `screenshots/`, `img/`) và **cấm** để ảnh rời cùng cấp với file `.md`.

4. **Nếu bug này Reopen lần nữa** ⇒ bug entry **BẮT BUỘC** có mục thứ 7 *"Cách verify sau khi fix"*, ghi **giống hệt từng chữ** với ô note trên bảng.

5. **Ghi bảng:** dòng **126**, tab `bug` (spreadsheet `1OKBN2otlmdZ44THkmhtsn-_63M2Boh7zQwearwjYR3s`, gid 1714340219). Ánh xạ theo `TIEN-DO.md`: note → cột **`Kết quả verify`** (được phép đè, bản cũ đã lưu ở `audit/LKHDG_12-ketqua-verify-CU.md`); verdict → cột **`Trạng thái dev fix`** (tab này chỉ có MỘT cột trạng thái; Pass ⇒ ghi `Test done`). Cập nhật cả bảng **Kết quả** trong `TIEN-DO.md`.

6. **🔴 Cảnh báo bản dựng (từ BƯỚC 0 của lô):** không có bằng chứng dev sửa gì — cả 6 dòng bị QA ghi `Reopen` ngày 06/08 nay lại về `Fixed` với ô `DEV phản hồi lần 1` trống. Nếu bó mã FE đo được **trùng khít** `assets/index-DIABnbIr.js` (đo 06/08 18:44) hoặc `assets/index-DThrFe1_.js` (đo 06/08 00:32) ⇒ **báo điều phối TRƯỚC khi chốt verdict**. Lưu ý lỗi này nằm **phía máy chủ** ⇒ bó mã FE không đổi **cũng chưa chứng minh BE không đổi** — vẫn phải đo thật, và phải chốt bằng **đường đo thứ hai** (§5).

7. **Không nới điều kiện.** Khối ở §6 là bản đã khóa. Nếu thấy đặc tả hiện hành khiến một điều kiện trở nên vô nghĩa hoặc mâu thuẫn ⇒ **báo điều phối**, không tự sửa tiêu chí giữa chừng.
