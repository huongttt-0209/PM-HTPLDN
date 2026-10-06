# Tiêu chí verify — QLBMHD_02

```
Mã case: QLBMHD_02 (tab `bug`, dòng 138 — Tuần 3, ngày 13/07/2026)
Mô tả case: "Kiểm tra hiển thị các trường thông tin" — màn Biểu mẫu → Danh sách biểu mẫu (SCR-VII-02)
Thời điểm viết tiêu chí: 2026-08-06 (GIAI ĐOẠN A — CHƯA mở màn, chưa đo)
Môi trường sẽ verify: https://18.143.165.120.nip.io  (env NỘI BỘ — đối tác đo trên htpldn-uat.ospgroup.vn)
Bản dựng: xem §7 — PHẢI đo lại ngay trước khi chạy case, không dùng lại số cũ
Trạng thái trên bảng: Trạng thái = Fail · Dopai = dev done · Trạng thái dev fix = Fixed · Kết quả verify = (trống)
```

> **Khai báo hồ sơ đã đọc trước khi viết §3–§6** (bắt buộc theo flow 04 §GIAI ĐOẠN A):
> - `flows/04-verify-bug-dev-fix-khong-ho-so.md` — §GIAI ĐOẠN A, §Cổng bằng chứng, §Đối chiếu đặc tả, §Ca biên.
> - `output/UAT_doi-tac/reverify-week-3/NGU-CANH-reverify-24-case-reopent.md` §"## 13. QLBMHD_02"
>   (dòng 618–665) — nguyên văn 3 vế đối tác + phản hồi dev vòng 1.
> - `output/UAT_doi-tac/reverify-week-3/cond/QLBMHD_02.md` — bảng đối chiếu Cổng 3 ngày 20/07:
>   web khi đó **11 cột, KHÔNG có "Cơ quan ban hành"** → Open.
> - `output/UAT_doi-tac/reverify-week-3/cond/QLBMHD_02-reverify.md` — re-test 22/07 bằng `cbnv_tw_03`:
>   **12 cột, có "Cơ quan ban hành" ở vị trí thứ 5**, 8/8 dòng có dữ liệu → PASS.
> - `output/UAT_doi-tac/reverify-week-3/bug-reports/bieu-mau/verify-2-moi-truong-QLBMHD_02-2026-07-28.md` —
>   đo SONG SONG 2 env ngày 28/07: dev **CÓ** cột / UAT **KHÔNG** có; trên UAT trường `coQuanBanHanh`
>   **không tồn tại** ở endpoint danh sách quản lý, cũng không có trong 43 bó mã FE.
> - `output/UAT_doi-tac/reverify-week-3/dev-fix-reverify-round-10-2026-07-30/KET-QUA-reverify-24-case-reopent.md`
>   dòng 24 (hàng #13 của bảng) — QA nội bộ chấm **✅ PASS 30/07** với **12 cột**.
> - `output/UAT_doi-tac/reverify-week-3/ba-confirm/phan-hoi/phan-hoi-ba/phan-hoi-ba-confirmation-needed-week-3-bieu-mau-tong-hop.md`
>   dòng 74–79 — **BA đã chốt điểm "ô tích chọn" ngày 2026-07-24** (chi tiết ở §3 vế (c)).
>
> **§3–§6 suy TỪ ĐẶC TẢ + bằng chứng đối tác. Số cột / vị trí cột của các vòng cũ (11 · 12 · index 4/5)
> chỉ có giá trị bối cảnh, KHÔNG được dùng làm ngưỡng chấm lần này** — phải đếm lại thô từ đầu.

---

## 🔴 Mâu thuẫn phải giải quyết trong lượt đo này

| Ngày | Ai đo | Env | Kết quả về cột "Cơ quan ban hành" |
|---|---|---|---|
| 20/07 | QA nội bộ | nội bộ `18.143.165.120.nip.io` | **KHÔNG có** (11 cột) → Open |
| 22/07 | QA nội bộ | nội bộ | **CÓ** (12 cột) → Pass |
| 27/07 | TKM (đối tác) | nghiệm thu `htpldn-uat.ospgroup.vn` | **Vẫn thiếu** → Reopen |
| 28/07 | QA nội bộ, đo 2 env cùng lúc | nội bộ **và** nghiệm thu | nội bộ **CÓ** · nghiệm thu **KHÔNG** |
| 30/07 | QA nội bộ | nội bộ | **CÓ** (12 cột) → Pass |

**Hai bên KHÔNG mâu thuẫn về sự thật — họ đo hai môi trường chạy hai bản dựng khác nhau.** Phép đo
28/07 đã chứng minh: bản trên env nghiệm thu chưa có phần fix này ở **cả BE lẫn FE**.

**Hệ quả bắt buộc cho lượt này:**

1. Lượt này đo trên env **NỘI BỘ** ⇒ dù đạt hết cũng chỉ là **Pass tạm**, hiệu lực **chỉ cho env + bản
   dựng ghi ở §7**. Cấm viết verdict theo kiểu để người đọc hiểu là đối tác mở lên sẽ hết lỗi.
2. Chuẩn chấm ở §4 phải **phân định được FE tự chế chữ** với **BE thật sự trả dữ liệu** — vì đúng điểm
   này là chỗ 2 env lệch nhau (env nghiệm thu vẫn có `coQuanBanHanh` ở nhóm endpoint chuyên trang công
   khai nhưng KHÔNG có ở endpoint danh sách quản lý). Chỉ nhìn chữ trên màn là không đủ.
3. §7 bắt buộc ghi **dấu vân tay bản dựng** (tên bó mã + last-modified + etag), không chỉ chuỗi phiên bản
   — env này đã có tiền lệ deploy lại mà giữ nguyên chuỗi `V1.0.8`.

---

## 1. Đối tác phản ánh

**Kết quả mong đợi (nguyên văn ô trên bảng):**

> - Hệ thống hiển thị các trường thông tin giống với thiết kế
> - Dữ liệu hiển thị đúng định dạng và trường thông tin
> - Dữ liệu hiển thị không bị tràn/đè lên nhau, đồng nhất ngôn ngữ hiển thị

**Kết quả thực tế (nguyên văn ô trên bảng):**

> - Thiếu Ô chọn biểu mẫu
> - Thiếu các cột thông tin: Cơ quan ban hành, Định dạng

**TKM phản hồi lần 1 (nguyên văn):**

> - TKM retest 27/7: Thiếu cột "Cơ quan ban hành"
> - Cần chị anhduong16.work@gmail.com xác nhận về "Ô tích chọn"

Case này **gộp 3 vế**. Tách rõ để chấm từng vế (flow 04 §Ca biên: mọi vế hết lỗi mới Pass · còn ≥1 vế
lỗi → Reopen · không vế nào lỗi mà còn vế cần-BA → cần BA):

| Vế | Nội dung đối tác nêu | Còn treo sau retest 27/7? | Trạng thái đặc tả | Nhánh |
|---|---|---|---|---|
| **(a)** | Thiếu **cột "Cơ quan ban hành"** | **CÓ** — TKM nhắc lại đích danh | Nói rõ (`srs-fr-09-bieu-mau.md:671` "luôn hiển thị") — **khớp** kỳ vọng đối tác | Chấm PASS/FAIL |
| **(b)** | Thiếu **cột "Định dạng"** | TKM không nhắc lại; dev vẫn nhận là lỗi phải sửa | Đặc tả có **bộ lọc** Định dạng (`:654`) + **cột "Loại tài liệu"** (`:657`), **KHÔNG** có cột tên "Định dạng" | b1 (bộ lọc + cột thể hiện định dạng) chấm PASS/FAIL · b2 (đòi cột tên "Định dạng") → **cần BA** |
| **(c)** | Thiếu **ô chọn (tích chọn) biểu mẫu** từng dòng | **CÓ** — TKM xin người có thẩm quyền xác nhận | SCR-VII-02 (`:650`–`:673`) liệt kê **đóng** 22 thành phần, **không có** ô tích chọn; màn Thư mục SCR-VII-01 thì **có** (`:624`, `:630`) | **KHÔNG chấm bằng phép đo** — áp quyết định BA 2026-07-24 (§3(c)) |

**Phản hồi dev lần 1 (tóm tắt, để đối chiếu — KHÔNG dùng làm chuẩn chấm):** dev khẳng định màn Danh
sách biểu mẫu **không thiết kế ô tích chọn từng dòng** (thao tác hàng loạt đặt ở cấp thư mục) và đề nghị
đưa vào yêu cầu cải tiến; đồng thời **thừa nhận thiếu cột Cơ quan ban hành / Định dạng là lỗi Dev phải sửa**.
Theo flow 04 §Ca biên *"Dev mô tả fix ở chỗ khác với triệu chứng → vẫn chạy đủ luồng, đừng tin mô tả"* —
lời nhận này không thay được phép đo, và cũng không tự động biến "cột Định dạng" thành yêu cầu của đặc tả.

---

## 2. Neo bằng chứng đối tác

**Tệp:** `reverify-week-5/partner-evidence/QLBMHD_02.jpg` — ảnh tĩnh **1896×1031 px**, **279.435 byte**,
md5 `1ee38a82b6a7e249260c47c3f3dcc3e7`. **Đã mở full-res + phóng to 3 vùng** (hàng tiêu đề bảng · thanh
lọc · mép dưới bảng) để đọc chữ.

**Kiểm bằng chứng có đúng case không:** ✅ đúng màn (`/bieu-mau/danh-sach`), đúng breadcrumb
*Trang chủ / Thư viện biểu mẫu / Danh sách*, đúng vai trò, đúng mã case. Chỉ có **1 ảnh tĩnh, không có video**.

**3 dữ kiện neo lấy được:**

1. **URL / màn:** `htpldn-uat.ospgroup.vn/bieu-mau/danh-sach` — **env nghiệm thu của đối tác**, không phải env mình sẽ đo.
2. **Vai trò + đơn vị:** góc phải ghi `BTP · TW` · avatar `CU` · **"Cán bộ NV Trung ương  CB_NV_TW"** · chuông `99+`.
3. **Bản dựng + thời điểm:** chân sidebar ghi **`HTPLDN · V1.0`**; đồng hồ máy **09:54 AM ngày 2026-07-13**.

### Đọc được gì trên ảnh

| Vùng trên ảnh | Đọc được nguyên văn | Ý nghĩa cho vế nào |
|---|---|---|
| Hàng tiêu đề bảng (đọc từ trái sang) | `Mã BM` · `Tên biểu mẫu` · `Loại TL` · `Thư mục` · `Kích thước` · `Trạng thái` · `Đã công khai` · `Hành động` | (a) (b) (c) — **8 nhãn đọc được**, KHÔNG có `Cơ quan ban hành`, KHÔNG có `Định dạng`, KHÔNG có ô tích chọn trước `Mã BM` |
| Mép dưới bảng | Có **thanh cuộn ngang**; nhãn `Đã công khai` bị **cắt sát** vào cột `Hành động` (cột dính bên phải); ô dữ liệu hiện `Chưa công…` | ⚠️ Bảng **rộng hơn khung chứa** ⇒ **có thể còn cột bị khuất bên phải** mà ảnh không cho thấy |
| Thanh lọc | Ô `Nhập từ khóa tìm kiếm...` + 4 danh sách chọn: `Thư mục` · `Lĩnh vực` · `Loại hình` · **`Định dạng`** + nút `Xóa bộ lọc` · `Tìm kiếm` | (b) — **bộ lọc "Định dạng" ĐÃ CÓ** ngay trên ảnh của chính đối tác |
| Thanh công cụ | `Biểu mẫu` + `+ Thêm biểu mẫu` · `Nhập hàng loạt` · `Làm mới` | (c) — có `Nhập hàng loạt` (import), **không có** nhóm nút thao tác hàng loạt kiểu công khai/ẩn/xóa |
| 6 hàng dữ liệu đọc được | `BM-20260713-… TKM test` (icon Excel, `52.2 KB`, `Đã ẩn`, `Chưa công…`) · `BM-20260703-… 77777` ×2 (icon Word, `30.0 KB`, `Nháp`) · `BM-20260630-… Test Download` (`945 B`, `Đã công khai`, `Công khai`) · `BM-20260525-… Hợp đồng lao động` (`2.2 KB`, `Đã công khai`, `Công khai`) · `BM-20260513-… TC-BM-401 Pilot Upload Test 2026-…` (`943 B`, `Nháp`) | (a) (b) — có **cả nhóm Excel và nhóm Word**; có đủ 3 trạng thái vòng đời `Đã ẩn` / `Nháp` / `Đã công khai` |
| Ô Hành động mỗi hàng | `Tải về` · `Sửa` · `Xóa` (nhãn chữ) | Ngoài phạm vi 3 vế — xem §4 "KHÔNG được chấm Fail vì" |

🔴 **Hệ quả về phương pháp đo:** bảng của đối tác **đang cuộn ngang và có cột dính bên phải** ⇒ **đếm cột
bằng mắt trên ảnh là phép đo KHÔNG hợp lệ** (flow 04 §Dấu hiệu phép đo đang nói dối: *"Kết luận 100% từ
script chạy trong trang, không có ảnh"* và ngược lại — nhìn ảnh mà kết luận danh sách đầy đủ cũng sai).
Lần này **bắt buộc đọc `innerText` của hàng tiêu đề, đếm thô**, xem §4.

---

## 3. Đặc tả nói gì — cho TỪNG vế

**Nguồn DUY NHẤT:** `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/` (bản chốt của đợt này).
Đã **mở file đọc từng dòng**, không dẫn theo trí nhớ.

> ⚠️ **Cảnh báo số dòng — hồ sơ QA cũ dẫn theo BẢN KHÁC.** Các file tuần 3 (`cond/QLBMHD_02.md`, note
> DRIVE, phản hồi BA) dẫn `SCR-VII-02 dòng 657`, `dòng 640`, `dòng 634`, `dòng 662` — đó là số dòng của
> **`input/srs-update-2026-5-5/srs-fr-09-bieu-mau.md`**. Mình đã mở CẢ HAI bản để đối chiếu:
>
> | Nội dung | Bản cũ `input/srs-update-2026-5-5/` | Bản chuẩn `Docs-PM-HTPLDN/…/srs-v3.5/` | Nội dung có khác không? |
> |---|---|---|---|
> | Cột Cơ quan ban hành (#20) | `:657` | **`:671`** (lệch **+14**) | **Giống hệt từng chữ** |
> | Bộ lọc lĩnh vực/loại hình/thư mục/định dạng (#3) | `:640` | **`:654`** (lệch **+14**) | **KHÁC** — bản cũ chỉ ghi cụt *"Các bộ lọc"*; bản chuẩn ghi rõ *"Lĩnh vực PL / Loại hình / Thư mục / Định dạng (doc / docx / xls / xlsx). Mỗi bộ lọc mặc định 'Tất cả (không lọc)'"* |
> | Cột Loại tài liệu (#6) | `:643` | **`:657`** (lệch **+14**) | Giống hệt |
> | Bảng thành phần SCR-VII-02 | 21 dòng (#1–#21) | **22 dòng** (#1–#22) | Bản chuẩn **thêm #22** *"Tệp đang đính kèm"* (`:673`) |
>
> ⇒ Số `657` của hồ sơ cũ, đọc trên bản chuẩn, lại rơi đúng vào **"Cột Loại tài liệu"** — trích nhầm bản
> là đổi hẳn nội dung. **Mọi trích dẫn dưới đây dùng số dòng bản chuẩn.**

### Vế (a) — cột "Cơ quan ban hành": đặc tả NÓI RÕ, khớp kỳ vọng đối tác

- `srs-fr-09-bieu-mau.md:671` (SCR-VII-02 #20) → nguyên văn:

```
| 20 | content | Cột Cơ quan ban hành | table-column | Tên đơn vị ban hành (`don_vi_id` → DON_VI) | — | luôn hiển thị `[STT12]` |
```

- `srs-fr-09-bieu-mau.md:315` (FR-VII-04 §Inputs #14) → *"co_quan_ban_hanh | identifier | **Y** | Auto = đơn vị
  của tài khoản đăng nhập (`BIEU_MAU.don_vi_id`); hiển thị **read-only**, không cho sửa; là Cơ quan ban hành
  hiển thị trên chuyên trang | đơn vị tài khoản | hệ thống `[STT12]`"*
- `srs-fr-09-bieu-mau.md:796` (Entity BIEU_MAU #16) → *"don_vi_id | identifier | Y | FK → DON_VI(id) | — |
  Đơn vị sở hữu theo đơn vị; **đồng thời là Cơ quan ban hành** hiển thị trên chuyên trang (auto = đơn vị tài
  khoản tạo, read-only) `[STT12]`"*

⇒ Cột **bắt buộc luôn hiển thị**, và giá trị phải **lấy theo `don_vi_id` của TỪNG bản ghi**, không phải
đơn vị của người đang đăng nhập. Đây là điểm phân biệt then chốt ở §4.

### Vế (b) — "Định dạng": đặc tả có BỘ LỌC, KHÔNG có CỘT cùng tên

- `srs-fr-09-bieu-mau.md:654` (SCR-VII-02 #3) → nguyên văn:
  `| 3 | filter-bar | Lọc lĩnh vực / loại hình / thư mục / định dạng | select | Lĩnh vực PL / Loại hình / Thư mục / Định dạng (doc / docx / xls / xlsx). Mỗi bộ lọc mặc định "Tất cả (không lọc)" | change → filter | luôn hiển thị |`
- `srs-fr-09-bieu-mau.md:415` (FR-VII-05 §Inputs #5) → *"dinh_dang | text | N | **CHECK IN ('doc','docx','xls','xlsx')**
  | Tất cả (không lọc) | user input"*
- `srs-fr-09-bieu-mau.md:437` (FR-VII-05 §Outputs #6) → *"dinh_dang | text | — | Định dạng file"*
- `srs-fr-09-bieu-mau.md:657` (SCR-VII-02 #6) → nguyên văn:
  `| 6 | content | Cột Loại tài liệu | table-column | Icon doc/xls | — | luôn hiển thị |`

**Danh sách cột bắt buộc của bảng — trích đủ, đây là liệt kê ĐÓNG** (`:650` là hàng tiêu đề bảng đặc tả,
`:651` hàng ngăn, `:652`–`:673` là 22 thành phần; kết thúc ở `:674` trống + `:675` dấu `---`).
Các thành phần thuộc vùng `content` và ghi **"luôn hiển thị"**:

| # SRS | Dòng | Nguyên văn tên cột | Nội dung đặc tả ghi |
|---|---|---|---|
| 4 | `:655` | Cột Mã BM | Mã auto |
| 5 | `:656` | Cột Tên BM | Tên (<=500 ký tự) |
| 6 | `:657` | **Cột Loại tài liệu** | **Icon doc/xls** |
| 7 | `:658` | Cột Thư mục | Tên thư mục (link) |
| 8 | `:659` | Cột Kích thước | Format: "1.5 MB" |
| 9 | `:660` | Cột Trạng thái lifecycle | NHAP / CONG_KHAI / AN (SM-BIEUMAU) |
| 10 | `:661` | Cột Đã công khai | badge xanh khi `cong_khai`=1, xám khi =0; tooltip kèm `thoi_gian_dang_tai` |
| 11 | `:662` | Cột Ảnh đại diện | thumbnail ảnh đại diện công khai |
| 12 | `:663` | Cột Hành động | Xem trước (mặc định) / Tải về / Sửa / Xóa |
| 20 | `:671` | **Cột Cơ quan ban hành** | Tên đơn vị ban hành (`don_vi_id` → DON_VI) |

⇒ **10 cột bắt buộc. Trong đó KHÔNG có cột nào tên "Định dạng".** Thông tin định dạng tệp được đặc tả
giao cho **cột "Loại tài liệu"** (`:657`, icon doc/xls) và cho **bộ lọc "Định dạng"** (`:654`).
Vì vậy kỳ vọng *"thiếu cột Định dạng"* của đối tác là **nói ngược đặc tả**, không phải đặc tả im lặng
→ theo flow 04 §Đối chiếu đặc tả hàng *"Nói rõ nhưng ngược kỳ vọng đối tác"* ⇒ **cần BA, QA không tự bác đối tác**.

🔴 **Mâu thuẫn nội bộ phải nêu ra, không được giấu:** phản hồi BA ngày 23–24/07 có câu mở ngoặc
*"thiếu cột Cơ quan ban hành **+ Định dạng** là bug hiển thị cột BUG-QLBMHD_02, xử lý riêng"*
(`reverify-week-3/ba-confirm/phan-hoi/phan-hoi-ba/phan-hoi-ba-confirmation-needed-week-3-bieu-mau-tong-hop.md:75`),
và dev cũng nhận cột Định dạng là lỗi phải sửa — trong khi văn bản SCR-VII-02 (`:650`–`:673`) **không có
cột nào tên "Định dạng"**. Câu ngoặc đó không phải kết luận của phiếu (phiếu chỉ xử điểm "ô tích chọn"),
nên **chưa đủ tư cách quyết định**. Đây chính là lý do b2 đi nhánh cần BA.

### Vế (c) — ô tích chọn từng dòng: đặc tả IM LẶNG ở SCR-VII-02, nhưng **BA ĐÃ CHỐT**

Đặc tả trước:

- SCR-VII-02 (`:650`–`:673`) — liệt kê **đóng 22 thành phần**, **không có** thành phần "Checkbox / Chọn hàng loạt",
  và **không có** vùng `action-bar` nào.
- `srs-fr-09-bieu-mau.md:652` (SCR-VII-02 #1) → nguyên văn:
  `| 1 | toolbar | Tiêu đề + Nút | label + button | "Quản lý Biểu mẫu" + [+ Thêm biểu mẫu] [Nhập hàng loạt] | click → hành động | luôn hiển thị |`
  ⇒ nút hàng loạt duy nhất của màn này là **Nhập hàng loạt** (import), không phải công khai/ẩn/xóa hàng loạt.
- Đối chiếu màn anh em **SCR-VII-01 (Thư mục)** thì **CÓ**, ghi rõ:
  - `:624` → `| 9 | content | Checkbox | checkbox | Chọn hàng loạt | — | luôn hiển thị |`
  - `:630` → `| 15 | action-bar | Hành động hàng loạt | button | [Công khai hàng loạt] [Ẩn hàng loạt] [Xóa hàng loạt] | click → batch; … | khi chọn nhiều |`

⇒ Cùng một tài liệu, cùng một nhóm chức năng: màn Thư mục được khai checkbox tường minh, màn Biểu mẫu
thì không. Đó là **im lặng có chủ ý hay bỏ sót — QA không có thẩm quyền quyết**.

**BA đã chốt đúng điểm này, có nguồn + ngày:**

> **Nguồn:** `output/UAT_doi-tac/reverify-week-3/ba-confirm/phan-hoi/phan-hoi-ba/phan-hoi-ba-confirmation-needed-week-3-bieu-mau-tong-hop.md`
> dòng 74–79, mục *"### QLBMHD_02 (điểm phụ) — Thiếu 'ô chọn biểu mẫu' (checkbox chọn dòng) trên màn Danh sách biểu mẫu"*.
> **Ngày duyệt: 2026-07-24** (đầu file ghi *"Các kết luận dưới đây đã được BA duyệt (2026-07-24)"*).
> **Kết luận nguyên văn:** *"→ Kết luận: **Loại 3 — Không sửa, đề nghị đối tác đưa vào danh sách yêu cầu
> cải tiến:** công khai/ẩn theo thư mục là thiết kế chủ đích; thêm bulk cấp biểu mẫu = FR mới vượt phạm vi,
> defer để CĐT cân nhắc. **✅ BA duyệt 2026-07-24.**"*

Theo flow 04 §Đối chiếu đặc tả — *"BA đã chốt trước đúng điểm này và có nguồn + ngày → áp quyết định đó"* —
vế (c) **áp quyết định BA**, không đi hỏi lại. Cách xử lý đo đạc + điều kiện chặn ở §4.

---

## 4. Tiêu chí chấm

### 4.0 Tiền đề tối thiểu để đo được

- **Tài khoản:** `cbnv_tw` / `Test@1234` — vai trò **CB_NV_TW** (Cán bộ Nghiệp vụ Trung ương), cấp **TW**,
  đơn vị *Cục Bổ trợ tư pháp - Bộ Tư pháp*. Đúng vai trò + cấp đọc được trên ảnh đối tác
  (`Cán bộ NV Trung ương  CB_NV_TW`, `BTP · TW`). Tài khoản này đã đăng nhập được trên chính env này ngày
  06/08 (ghi trong `reverify-week-5/BAN-DUNG.md`).
  **Dự phòng theo Rule 7 (chỉ đổi hậu tố, GIỮ NGUYÊN vai trò + cấp):** `cbnv_tw_01` → `cbnv_tw_02` → `cbnv_tw_03`.
  Đã có tiền lệ `cbnv_tw` bị `ERR-AUTH-LOCKED-01` ngày 28/07. **Phải ghi rõ tài khoản thực dùng vào verdict.**
  **Không dùng `admin` để ra verdict** (quyền rộng che lỗi phân quyền).
- **Màn:** `/bieu-mau/danh-sach` (menu **Biểu mẫu → Danh sách biểu mẫu**), vào bằng **click menu**, không gõ URL.
- **Tải lại trang** trước khi đo (tab mở lâu vẫn chạy bó mã cũ — đã có tiền lệ báo Reopen oan).
- **Dữ liệu tiền đề tối thiểu:** xem §5. Thiếu dạng nào mà **tạo được** thì **phải seed** rồi mới ra verdict.

### ✅ PASS vế (a) — cột "Cơ quan ban hành" — khi ĐỦ cả 4

1. **Đếm thô hàng tiêu đề.** Lấy `innerText` của **toàn bộ** ô tiêu đề bảng (kể cả ô nằm ngoài khung nhìn
   và ô thuộc cột dính), **KHÔNG lọc, KHÔNG `unique`, KHÔNG bỏ ô rỗng** → in ra **danh sách theo thứ tự +
   tổng số**. Trong danh sách đó có **đúng 1** nhãn `Cơ quan ban hành`.
   *(Bảng cuộn ngang + có cột dính ⇒ nhìn ảnh không đủ; nhưng vẫn phải kèm ảnh — xem điều kiện 5 dưới.)*
2. **Mọi hàng đều có dữ liệu.** Đếm thô số hàng dữ liệu của trang 1 trước, rồi đọc ô "Cơ quan ban hành"
   của **từng hàng** (không lấy mẫu 2–3 hàng đầu): **100% hàng** có giá trị **khác rỗng** và khác chuỗi
   giữ chỗ (`-`, `—`, `null`, `undefined`, `N/A`, `Không xác định`).
3. **Giá trị bám theo `don_vi_id` của từng bản ghi, không phải đơn vị người đăng nhập** (`:671`, `:796`):
   trong trang 1 có **≥1 bản ghi thuộc đơn vị KHÁC** đơn vị của tài khoản đang đăng nhập, và ô của nó
   hiện **đúng tên đơn vị khác đó**. Nếu cả trang đều cùng một đơn vị ⇒ **chưa chứng minh được**, phải
   seed dạng D2 ở §5 rồi đo lại; **không được suy luận thay cho phép đo**.
4. **Đối chứng bằng đường thứ hai (bắt buộc, đây là chỗ 2 env từng lệch nhau):** bắt **lời gọi danh sách
   mà chính màn này phát ra** (đọc từ nhật ký mạng của phiên đo — **cấm tự đoán, tự gõ đường dẫn API**),
   mở phần trả về và kiểm: có trường mang **tên đơn vị ban hành**, và **giá trị khớp từng dòng** với chữ
   đang hiện trên màn. Hai phép lệch nhau ⇒ **CHƯA được chốt**, ghi cả hai, hỏi user.
5. **Có ảnh chụp** hàng tiêu đề + vài hàng dữ liệu, kèm 1 dòng chú thích *tên tệp + thấy gì trong ảnh*.
   Kết luận 100% từ script chạy trong trang mà không có ảnh = **không hợp lệ**.

### ❌ FAIL vế (a) nếu

- Danh sách tiêu đề (đếm thô) **không có** nhãn `Cơ quan ban hành`; **hoặc**
- Có nhãn nhưng **≥1 hàng** trống / hiện chuỗi giữ chỗ; **hoặc**
- Chữ trên màn có nhưng **phần trả về của lời gọi danh sách không có trường tương ứng** (⇒ chỉ FE dựng
  chữ — đúng kiểu "đúng một phần", vẫn là **Reopen**); **hoặc**
- Ô hiện **đơn vị của người đăng nhập cho mọi hàng** trong khi dữ liệu có bản ghi thuộc đơn vị khác
  (sai bản chất `:671` + `:796`).

### ✅ PASS vế (b1) — bộ lọc "Định dạng" + cột thể hiện định dạng — khi ĐỦ cả 3

1. **Bộ lọc tồn tại + đúng tập giá trị** (`:654`, `:415`): trên thanh lọc có điều khiển **"Định dạng"**;
   mở ra đọc thô toàn bộ lựa chọn → phủ đủ **doc · docx · xls · xlsx**; trạng thái ban đầu là
   **"Tất cả (không lọc)"** (không tự đổi tay trước khi đọc).
2. **Bộ lọc có tác dụng thật**: chọn 1 định dạng **đang có dữ liệu** → số hàng trả về (**đếm thô**) bằng
   số bản ghi đúng định dạng đó, và **mọi hàng còn lại đều đúng định dạng đã chọn** (đọc hết, không lấy mẫu);
   đối chứng bằng phần trả về của lời gọi tương ứng. Rồi bấm **Xóa bộ lọc** → danh sách trở về đủ như ban đầu.
3. **Cột thể hiện định dạng tồn tại và phân biệt được** (`:657`): trong danh sách tiêu đề (đếm thô ở bước
   a.1) có cột thể hiện loại/định dạng tài liệu; **≥1 bản ghi nhóm Word** và **≥1 bản ghi nhóm Excel** cho
   ra **biểu hiện khác nhau** (icon khác nhau hoặc chữ khác nhau) — đọc được bằng mắt trên ảnh chụp.

### ❌ FAIL vế (b1) nếu

Thiếu hẳn điều khiển lọc "Định dạng"; **hoặc** thiếu ≥1 trong 4 giá trị doc/docx/xls/xlsx; **hoặc** chọn
định dạng mà danh sách **không đổi** / trả về **lẫn định dạng khác**; **hoặc** không có cột nào thể hiện
định dạng; **hoặc** có cột nhưng bản ghi Word và bản ghi Excel hiện **y hệt nhau** (không phân biệt được).

### → **cần BA — vế (b2): đối tác đòi một cột tên "Định dạng"**

**Vì sao:** đặc tả **nói rõ nhưng ngược kỳ vọng đối tác**. `:650`–`:673` là liệt kê **đóng** 22 thành phần;
trong đó thông tin định dạng được giao cho **cột "Loại tài liệu"** (`:657` — *"Icon doc/xls"*) và cho
**bộ lọc "Định dạng"** (`:654`); **không có** cột nào tên "Định dạng". QA **không tự bác đối tác**, cũng
**không tự bênh dev** — vẫn **đo và ghi nhận hiện trạng**: tên nhãn cột thực tế là gì, ô hiện icon hay chữ,
có tooltip/nhãn trợ năng nào cho biết định dạng không.

*Ngoại lệ — hết bất đồng thì bỏ khỏi danh sách hỏi BA:* nếu bản dựng đã có một cột cho **đọc được định dạng
bằng chữ** (dù nhãn là "Loại TL", "Loại tài liệu" hay "Định dạng"), thì kỳ vọng đối tác coi như đã được đáp
ứng trên thực tế ⇒ chỉ ghi nhận, không mở câu hỏi BA.

*Nếu vẫn còn bất đồng, câu hỏi gửi BA phải nêu đúng 2 việc:* ① SCR-VII-02 có bổ sung cột riêng tên
"Định dạng" không, hay giữ nguyên "Loại tài liệu" + bộ lọc như `:654`/`:657`? ② Câu mở ngoặc trong phản hồi
BA 23–24/07 coi *"thiếu cột … + Định dạng là bug hiển thị cột"* có phải là quyết định chính thức không —
vì nó ngược với văn bản SCR đang hiệu lực.

### → **KHÔNG chấm bằng phép đo — vế (c): ô tích chọn từng dòng**

**Căn cứ:** BA đã chốt **2026-07-24**, nguồn ghi đầy đủ ở §3(c): *Loại 3 — không sửa, đề nghị đối tác đưa
vào danh sách yêu cầu cải tiến*. Theo flow 04, có quyết định BA kèm nguồn + ngày thì **áp quyết định đó**,
không hỏi lại và cũng **không chấm Fail**.

**Vẫn phải đo và ghi nhận hiện trạng** (để hồ sơ đầy đủ, không kết luận): hàng tiêu đề và các hàng dữ liệu
**có / không có** ô tích chọn (kiểm bằng `innerText` hàng tiêu đề ở bước a.1 + soi phần tử tích chọn trong
bảng), và thanh công cụ có / không có nhóm nút thao tác hàng loạt cấp biểu mẫu.

**Điều kiện chặn — phải hỏi user trước khi ghi verdict cho vế này:** TKM ghi *"Cần chị
anhduong16.work@gmail.com xác nhận về 'Ô tích chọn'"*, tức phía đối tác vẫn đang chờ xác nhận. Trong hồ sơ
có sẵn **câu trả lời soạn cho đối tác** (dòng 79 của file phản hồi BA) nhưng **không có bằng chứng câu đó
đã được gửi / đã được người đối tác nêu đích danh xác nhận**. Vì vậy:

- Nếu người ra verdict xác nhận quyết định BA 24/07 đã là căn cứ hợp lệ với đối tác → vế (c) = **không phải
  lỗi**, verdict phải **dẫn nguồn + ngày** (được phép ghi *"BA đã chốt ngày 2026-07-24"* — đó là căn cứ,
  không phải diễn biến trao đổi).
- Nếu chưa xác nhận được đã gửi → vế (c) giữ nhánh **cần BA**, câu hỏi đúng 1 ý: *quyết định 24/07 đã được
  thông báo tới đối tác chưa, và ai là người xác nhận thay cho đề nghị của TKM?*

**Cấm** tự kết luận "không phải lỗi" chỉ vì dev nói đó là thiết kế có chủ đích.

### Verdict tổng của case (flow 04 §Ca biên)

| Tình huống sau khi đo | Verdict case |
|---|---|
| (a) đạt · (b1) đạt · (b2) hết bất đồng · (c) áp được quyết định BA | **Pass** — và là **Pass tạm** (chỉ cho env + bản dựng §7) |
| ≥1 trong (a) / (b1) **không đạt** | **Reopen** (kể cả khi chỉ đúng một phần, vd có nhãn cột nhưng dữ liệu rỗng) |
| (a) và (b1) đều đạt, nhưng còn (b2) hoặc (c) treo | **Cần BA** |
| Không dựng được tiền đề bắt buộc ở §5 (vd không có bản ghi thuộc đơn vị khác và **không seed được**) | **ô trống** + ghi rõ thiếu gì |

### KHÔNG được chấm Fail vì

- **Cột thừa so với đặc tả.** Env nội bộ từng có thêm `Ngày tạo` và `Sync Cổng` — không nằm trong 10 cột
  `:655`–`:663`/`:671`, nhưng đối tác **không nêu** và đặc tả không cấm cột phụ. Ghi nhận, không kéo verdict.
- **Cột `Ảnh đại diện` (`:662`) nếu thiếu.** Đặc tả có yêu cầu, nhưng **không thuộc 3 vế đối tác nêu**.
  Gặp thiếu ⇒ xử theo flow §"Bug mới trực tiếp trong luồng": tra phiếu trùng, log riêng — **không** kéo verdict case.
- **Ô Hành động là nhãn chữ (`Tải về` / `Sửa` / `Xóa`) thay vì icon.** Đây là quy ước chung
  `srs-v3.5.md:6714` (Phụ lục E §H6) — **không thuộc vế đối tác nêu ở case này**. Gặp thì log riêng.
- **Nhãn cột bị cắt hoặc chữ trong ô bị cắt** (ảnh đối tác cho thấy `Đã công khai` sát cột dính, ô hiện
  `Chưa công…`). Đặc tả cho phép cắt + tooltip (`srs-fr-05-vu-viec.md:1568`, `:1571`); và ô *Kết quả thực tế*
  của đối tác **không nêu** tràn/đè. Chỉ log riêng nếu thấy chữ **đè chồng lên ô khác** (khác với cắt gọn).
- **Bề rộng cửa sổ < 1024 px.** `srs-fr-05-vu-viec.md:1603` (§F) chỉ cam kết tối thiểu **1024×768** cho màn phía cán bộ.
- **Số bản ghi ít hơn ảnh đối tác** / thứ tự hàng khác / thư mục khác tên — không thuộc vế nào.
- **Số cột đúng bằng 11 hay 12 như vòng cũ.** Con số cũ **không phải ngưỡng**; chỉ nhãn `Cơ quan ban hành`
  có mặt + có dữ liệu mới là điều kiện.

---

## 5. Dạng dữ liệu phải phủ — **M = 5**

Đây là bug về **cột hiển thị dữ liệu dẫn xuất từ quan hệ** (`don_vi_id` → DON_VI), nên M bắt buộc ≥ 2.

| # | Dạng | Vì sao là một dạng riêng (căn cứ) | Vế nào cần |
|---|---|---|---|
| **D1** | Biểu mẫu thuộc **đúng đơn vị của tài khoản đăng nhập** (TW — Cục Bổ trợ tư pháp) | `:315` — giá trị auto = đơn vị tài khoản khi tạo; đây là ca phổ biến nhất | (a) |
| **D2** | Biểu mẫu thuộc **đơn vị KHÁC** đơn vị người đăng nhập | `:671` + `:796` — cột phải đọc `don_vi_id` của **bản ghi**, không phải của người xem. Không có D2 thì **không phân biệt được** cột đúng với cột hard-code. Bằng chứng có thật: hồ sơ 22/07 và 28/07 ghi nhận cả *"Cục Bổ trợ tư pháp - Bộ Tư pháp"* lẫn *"Bộ Kế hoạch và Đầu tư"* | (a) |
| **D3** | Biểu mẫu **nhóm Word** (`doc` / `docx`) | `:654` + `:415` khai 4 định dạng; `:657` cột hiển thị *"Icon doc/xls"* ⇒ phải có ≥1 ca mỗi nhóm mới đo được "phân biệt được". Ảnh đối tác có sẵn nhóm này (icon Word) | (b1) |
| **D4** | Biểu mẫu **nhóm Excel** (`xls` / `xlsx`) | như trên; ảnh đối tác có `TKM test 52.2 KB` icon Excel | (b1) |
| **D5** | Biểu mẫu **tạo TRƯỚC bản dựng đang đo** (bản ghi cũ) **và** ≥1 bản ghi **tạo mới trong lượt đo** | Bản ghi đối tác nhìn thấy đều là bản ghi cũ. Nếu cột chỉ có dữ liệu với bản ghi sinh sau khi fix thì fix **không cứu** dữ liệu đối tác đang xem ⇒ vẫn là lỗi. Ngược lại, chỉ đo bản ghi cũ thì không loại được rủi ro luồng tạo mới hỏng | (a) |

**Nguồn xác định M:** ① đặc tả — `:671` (nguồn giá trị cột) · `:796` (`don_vi_id` là Cơ quan ban hành) ·
`:315` (auto theo đơn vị tài khoản) · `:415` (tập 4 định dạng); ② chính ảnh đối tác — có sẵn cả nhóm Word
và nhóm Excel, có 3 trạng thái vòng đời khác nhau.

**Thiếu dạng nào mà tạo được → BẮT BUỘC seed rồi mới ra verdict** (flow 04 cấm ra verdict khi tiền đề tạo
được mà không chuẩn bị). Cách tạo D2 không cần đụng DB: đăng nhập **cùng vai trò CB_NV nhưng khác đơn vị**
(vd `cbnv_bn` / `cbnv_dp_01`) để **tạo** 1 biểu mẫu, rồi quay lại đăng nhập `cbnv_tw` để **đo** — vì `:315`
gán `don_vi_id` theo đơn vị người tạo. **Khai vào báo cáo: tạo bản ghi nào · bằng tài khoản nào · trên env nào.**
Không đụng dữ liệu do đối tác tạo.

**Không mở rộng ngoài danh sách trên** — cụ thể không đo mọi vai trò, mọi cấp, mọi thư mục, mọi trạng thái
vòng đời, vì đặc tả `:671` ghi cột **"luôn hiển thị"** không kèm điều kiện theo trạng thái hay theo quyền.

---

## 6. Bảng điều kiện

| Điều kiện có thể đổi kết quả | Đối tác | Mình test lần này | GAP? |
|---|---|---|:-:|
| **Vai trò** / tài khoản | `CB_NV_TW` — badge trên ảnh: "Cán bộ NV Trung ương  CB_NV_TW", `BTP · TW` | `cbnv_tw` / `Test@1234` — CB Nghiệp vụ Trung ương, cấp TW, đơn vị Cục Bổ trợ tư pháp. Dự phòng cùng vai trò + cùng cấp: `cbnv_tw_01`/`_02`/`_03`. Không dùng `admin` ra verdict | **Không** — đúng vai trò, đúng cấp, đúng đơn vị. Nếu buộc phải đổi sang vai trò/cấp khác thì DỪNG, hỏi user |
| **Entity** + trạng thái | `BIEU_MAU` trên `/bieu-mau/danh-sach`; 6 hàng đọc được phủ 3 trạng thái vòng đời: `Đã ẩn` (1) · `Nháp` (3) · `Đã công khai` (2); cột Đã công khai có cả `Công khai` và `Chưa công…` | `BIEU_MAU` trên `/bieu-mau/danh-sach`, **không lọc trạng thái**, đọc **toàn bộ hàng trang 1** — không lấy mẫu | **Không** — `:671` ghi cột "luôn hiển thị", không ràng buộc trạng thái ⇒ không cần tách phép đo theo trạng thái; chỉ cần không lọc bỏ trạng thái nào |
| Dữ liệu **tiền đề** | 6 hàng đọc được đều thuộc dữ liệu env nghiệm thu; ảnh **không cho biết** đơn vị ban hành của bản ghi nào (cột đó không tồn tại lúc chụp) | Trang 1 phải có đồng thời **D1 + D2** (≥1 bản ghi đơn vị khác) và **D3 + D4** (≥1 Word, ≥1 Excel) và **D5** (≥1 bản ghi cũ + ≥1 bản ghi tạo mới trong lượt đo) — xem §5 | **Có rủi ro GAP ở D2** — env nội bộ có thể chỉ có bản ghi cùng một đơn vị. Nếu thiếu ⇒ **phải seed** theo §5 (tạo bằng tài khoản khác đơn vị) rồi mới verdict; không seed được ⇒ **ô trống**, ghi rõ thiếu gì |
| Input / **filter** / giá trị nhập | Không lọc gì (4 danh sách chọn `Thư mục` · `Lĩnh vực` · `Loại hình` · `Định dạng` đều ở trạng thái giữ chỗ, chưa chọn); ô từ khóa trống; **bảng đang cuộn ngang** | Lượt đo chính: **không lọc, không gõ từ khóa**, mở màn xong đọc ngay. Lượt đo b1: chọn **1 định dạng có dữ liệu** rồi bấm **Xóa bộ lọc** để về trạng thái ban đầu. **Phải cuộn hết chiều ngang** + đọc cả ô tiêu đề thuộc cột dính | **Không** — trạng thái lọc lượt đo chính giống hệt đối tác. Riêng thao tác lọc ở b1 là **thêm**, không phải lệch: nó phục vụ `:654` mà ảnh đối tác chưa chứng minh được |
| **Độ phủ** biến thể | N = 6 hàng đọc được trên ảnh (còn hàng bị cắt ở mép dưới) · 1 bề rộng cửa sổ (~1896 px) · M = 2 dạng định dạng (Word / Excel) · **0 dạng đơn vị ban hành** (cột chưa tồn tại) | N = **toàn bộ hàng trang 1, đếm thô, đọc hết từng hàng** · M = **5 dạng** (D1 D2 D3 D4 D5) · 1 bề rộng chuẩn dự án **1440×900** | **Không** — độ phủ rộng hơn đối tác ở mọi chiều. Chỉ 1 bề rộng là **đủ**: 3 vế của case là *có/không có cột* và *bộ lọc*, không phải vế bố cục; `srs-fr-05-vu-viec.md:1603` chỉ cam kết tối thiểu 1024×768 |

**Ghi chú giới hạn (KHÔNG phải GAP):**

- **Lệch môi trường + lệch bản dựng.** Đối tác đo trên env nghiệm thu `htpldn-uat.ospgroup.vn` bản
  `HTPLDN · V1.0` lúc 09:54 ngày 13/07; mình đo trên env nội bộ `18.143.165.120.nip.io` bản ghi ở §7.
  Theo flow 04, đây là **giới hạn hiệu lực của verdict**, phải ghi rõ nhưng **không tự động chặn kết luận**.
  Với case này giới hạn đó đặc biệt nặng vì phép đo 28/07 đã chứng minh hai env chạy hai nhánh khác nhau
  đúng ở phần cột này ⇒ Pass ở đây là **Pass tạm**, chưa đóng được Reopen phía đối tác.
- **Không tái hiện được đúng bản ghi trên ảnh đối tác.** Ảnh chụp dữ liệu env nghiệm thu; mình dùng dữ liệu
  QA tương đương trên env nội bộ, **không đụng dữ liệu đối tác** — đúng flow 04 §Chuẩn bị bước 3.

---

## 7. Bản dựng — ghi tại thời điểm đo

🔴 **Bắt buộc đo lại ngay trước khi chạy case, không chép lại số của lô khác.** Ghi **dấu vân tay** chứ
không chỉ chuỗi phiên bản — env này đã có tiền lệ deploy lại mà **giữ nguyên** chuỗi `V1.0.8`.

| Hạng mục | Giá trị đo được lúc chạy case |
|---|---|
| Thời điểm đo (giờ VN) | **06/08/2026 19:33 → 19:41** (đăng nhập 19:32:33, đo lại vân tay lúc 19:41 — không đổi) |
| Môi trường | `https://18.143.165.120.nip.io` — env **NỘI BỘ** |
| Chuỗi phiên bản trên màn (chân sidebar) | `HTPLDN · V1.0.8` |
| Bó mã FE (`assets/index-*.js` + `*.css`) | `assets/index-DIABnbIr.js` · `assets/index-DVlgOkLg.css` |
| `GET /` → `last-modified` | `Thu, 06 Aug 2026 07:13:15 GMT` |
| `GET /` → `etag` | `W/"6a74340b-428"` |
| Tài khoản thực dùng để ra verdict | **`cbnv_tw` / `Test@1234`** — vai trò `CB_NV_TW`, cấp TW, đơn vị `00000000-0000-4000-8000-000000000001` *Cục Bổ trợ tư pháp - Bộ Tư pháp* (đọc từ `access_token`: `vaiTro: ["CB_NV_TW"]`, `capDonVi: "TW"`). **Không phải dự phòng** — đăng nhập được ngay lần đầu, không gặp `ERR-AUTH-LOCKED-01` |
| Có phải bản dựng đã đổi so với lần đo gần nhất? | **KHÔNG** — trùng khít `BAN-DUNG.md` (18:44) và trùng cả lượt đo case `QLHSPLDN_07` (19:24): cùng bó mã, cùng `last-modified`, cùng `etag` ⇒ FE không deploy lại trong suốt đợt |

### Dữ liệu đã seed trong lượt đo (khai theo flow 04 §Chuẩn bị 4)

| Việc | Chi tiết |
|---|---|
| Tạo mới **1 biểu mẫu** (dạng **D5** + bổ sung **D4**) | `BM-20260806-001` — *"QA-W5-1936 BM moi trong luot do"*, thư mục `QA-R7-A-CO-BM`, tệp `QA-W5-QLBMHD02-bieu-mau-moi.xlsx` (4.869 B, XLSX thật), tạo bằng **UI thật** (nút *Thêm biểu mẫu*) bằng `cbnv_tw` trên env nội bộ. Cơ quan ban hành auto = *Cục Bổ trợ tư pháp - Bộ Tư pháp* |
| **KHÔNG** seed dạng D2 | Env đã sẵn **8/27 bản ghi thuộc đơn vị khác** (`00000000-0000-4000-8001-000000000001` — *Bộ Kế hoạch và Đầu tư*) ⇒ không cần tạo thêm, không cần đăng nhập tài khoản khác đơn vị |
| Không đụng dữ liệu đối tác | Mọi bản ghi thao tác đều nằm trên env nội bộ; không sửa/xoá bản ghi có sẵn |

**Số đo tham chiếu gần nhất trên env này** (`output/UAT_doi-tac/reverify-week-5/BAN-DUNG.md`, đo
**2026-08-06 18:44** giờ VN): chuỗi phiên bản `HTPLDN · V1.0.8` · bó mã `assets/index-DIABnbIr.js` +
`assets/index-DVlgOkLg.css` + `assets/index-DNsk8fKL.css` · `last-modified: Thu, 06 Aug 2026 07:13:15 GMT` ·
`etag W/"6a74340b-428"`. **Dùng để SO SÁNH xem bản dựng có đổi không — KHÔNG dùng thay cho phép đo mới.**

**Câu ghi hiệu lực bắt buộc kèm mọi verdict Pass của case này:**
*"Kết quả chỉ có hiệu lực cho env nội bộ + bản dựng ghi ở bảng trên; đây là Pass tạm cho tới khi bản dựng
này lên môi trường nghiệm thu."*

---

## 9. Kết quả chốt (điền sau khi đo — 2026-08-06)

**Verdict: ✅ PASS** — chạm đúng ô Pass của bảng §Verdict tổng ở trên, **không nới tiêu chí**.

| Điều kiện Pass đã kẻ sẵn ở §Verdict tổng | Thoả bằng gì |
|---|---|
| **(a) đạt** | Cột *Cơ quan ban hành* có, **27/27 bản ghi** có giá trị, **2 đơn vị** (19 + 8) ⇒ bám `don_vi_id` của **bản ghi**; đối chứng máy chủ **0/20 dòng lệch** |
| **(b1) đạt** | Bộ lọc đủ `DOC/DOCX/XLS/XLSX`, mặc định `Tất cả`, **không còn "PDF"**; lọc `XLSX` ra **3/3** (`total = 3`); cột `Loại TL` phân biệt Word ↔ Excel |
| **(b2) hết bất đồng** | **BA đã cập nhật đặc tả cho chính phiếu này**, dấu `[STT12]` ở **5 chỗ** (`srs-fr-09-bieu-mau.md:315` · `:482` · `:671` · `:672` · `:796`) — **cả 5 đều là *Cơ quan ban hành***; grep toàn file **không có** thành phần nào tên *"Cột Định dạng"*. BA có đủ cơ hội thêm cột đó khi sửa đặc tả và **chỉ thêm 1 cột** ⇒ bản sửa đặc tả là **ý chí sau cùng**, thay cho câu chêm 24/07 ⇒ **không còn bất đồng để hỏi** |
| **(c) áp được quyết định BA** | BA chốt **2026-07-24 Loại 3 — không sửa**; câu trả lời cho đối tác **đã nằm sẵn** trong ô *DEV phản hồi lần 1* của dòng 138 ⇒ đúng nhánh *"người ra verdict xác nhận quyết định BA 24/07 đã là căn cứ hợp lệ với đối tác"* ⇒ vế (c) = **không phải lỗi**, verdict dẫn nguồn + ngày |

**Hai lần chấm sai trước đó của chính đợt này, ghi lại để không lặp:**

1. **Chấm cần BA (19:47)** — treo vế (c) vì tưởng quyết định BA 24/07 chưa tới tay đối tác. **Sai**: câu trả
   lời nằm ngay trong ô *DEV phản hồi lần 1* của dòng 138, tức đối tác đã được thông báo trên chính bảng họ đọc.
2. **Suýt chấm Pass bằng lý do sai (20:0x)** — dựa vào việc TKM ngày 27/07 chỉ còn nhắc *Cơ quan ban hành*.
   Chứng cứ đó **yếu**, và bị một sự thật cứng hơn phản bác: cột `Loại TL` **đã có sẵn trên bản dựng đối tác
   chụp** (`V1.0`, hàng tiêu đề 8 nhãn có `Loại TL`) — đối tác nhìn thấy rồi vẫn log thiếu ⇒ ở vế đó dev
   **không đổi gì**, không thể lấy làm căn cứ Pass.

⇒ **Bài học:** trước khi treo BA, **kiểm xem BA đã trả lời bằng cách sửa đặc tả chưa**. Dấu thay đổi trong
văn bản đặc tả (`[STT12]`) là căn cứ mạnh hơn mọi câu chữ trong thư trả lời — kể cả câu chêm của chính BA.
