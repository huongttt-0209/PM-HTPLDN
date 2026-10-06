# Tiêu chí verify — QLHSPLDN_06

```
Mã case: QLHSPLDN_06 (tab `bug`, dòng 291 — Tuần 3)     Thời điểm viết: 2026-08-06 18:48 (giờ VN)
Môi trường verify: https://18.143.165.120.nip.io  (env NỘI BỘ — đối tác đo trên env nghiệm thu
                   https://htpldn-uat.ospgroup.vn, KHÁC env này)
Bản dựng khi ĐO: ______________________  ← người đo điền ở §7 (KHÔNG copy sẵn từ file khác)
Đo lúc: ______ → ______                  ← người đo điền
Trạng thái dòng: Trạng thái = Fail · Dopai = dev done · Trạng thái dev fix = Fixed · Kết quả verify = (trống)
```

> **Khai hồ sơ QA nội bộ đã đọc trước khi viết §4 và §5** (bắt buộc theo flow 04 §GIAI ĐOẠN A):
> - `output/UAT_doi-tac/reverify-week-3/verify1-conlai-2026-08-03/reverify-audit/QLHSPLDN_06.md` — vòng
>   verify 03/08 trên bản `V1.0.5`: đo 6/6 hàng có nút Xem, 6 khả năng gây kết luận sai đã loại trừ, có
>   seed 2 hồ sơ để phủ trạng thái *Hết hạn* / *Thu hồi*, verdict ghi `Pass`.
> - `output/UAT_doi-tac/reverify-week-3/verify1-conlai-2026-08-03/cond/QLHSPLDN_06.md` — bảng điều kiện
>   vòng đó (4 hàng, 0 GAP), tài khoản `cbnv_tw_04`, DN `DN-HNI-0001`.
> - `output/UAT_doi-tac/reverify-week-3/uat-luong3-2026-08-04/cases/QLHSPLDN_06.md` — nội dung dòng sheet
>   + chữ đã ghi cho đối tác ở cột `DEV phản hồi lần 1` (04/08).
> - `output/UAT_doi-tac/reverify-week-3/uat-luong3-2026-08-04/cond/QLHSPLDN_06.md` — bảng điều kiện đo lại
>   04/08 (bản dựng `index-DpIXRGaI.js · V1.0.5`), tài khoản `cb_nv_tw_01`, DN `DN-NEW-NH2`.
>
> 🔴 **Các số đo cũ ở 4 file trên KHÔNG phải chuẩn chấm của lượt này.** Chúng đo trên bản dựng `V1.0.5`
> (03–04/08), lượt này đo trên bản dựng khác (xem §7). Số cũ chỉ dùng làm **bối cảnh** (biết chỗ nào dễ sập,
> biết đã seed gì) — mọi tiêu chí ở §4 suy **TỪ ĐẶC TẢ + Kết quả mong đợi của đối tác**, phải đo lại từ đầu.
> Đặc biệt **không được** lấy kết luận `Pass` cũ làm lý do rút gọn phép đo lần này.

---

## 1. Đối tác phản ánh

| Ô trên bảng | Nội dung nguyên văn |
|---|---|
| Mô tả | "Xem" |
| Điều kiện | "1. Đăng nhập hệ thống thành công" |
| Các bước thực hiện | 1. Chọn menu "Doanh nghiệp" · 2. Nhấn "Xem chi tiết" · 3. Chọn thẻ "Hồ sơ pháp lý doanh nghiệp" · 4. Nhấn "Xem" |
| Kết quả mong đợi | "Hệ thống mở cửa sổ chi tiết hiển thị toàn bộ thông tin của hồ sơ và danh sách tệp đính kèm (nếu có) ở chế độ chỉ đọc." |
| Kết quả thực tế | "Màn hình không có nút chức năng xem chi tiết" |

**Case này gộp 4 vế** (tách từ chính ô *Kết quả mong đợi* + ô *Kết quả thực tế*):

| Vế | Nội dung đối tác đòi | Nguồn ô | Trạng thái đặc tả |
|---|---|---|---|
| **(a)** | Trên bảng hồ sơ pháp lý phải có chức năng **mở chi tiết từng hồ sơ** (thứ đối tác nói là "không có") | Kết quả thực tế + bước 4 | đặc tả **nói rõ** (`srs-fr-12:550`, `:634`, `:693`; `srs-v3.5.md:6714`) — khớp kỳ vọng |
| **(b)** | Bấm vào đó **mở được cửa sổ chi tiết**, hiển thị **toàn bộ thông tin của hồ sơ** | Kết quả mong đợi | đặc tả **nói rõ** (`srs-fr-12:640`, `:693`) — khớp kỳ vọng |
| **(c)** | Cửa sổ có **danh sách tệp đính kèm (nếu có)** | Kết quả mong đợi | đặc tả **nói rõ** (`srs-fr-12:641`, `:642`, `:693`) — khớp kỳ vọng |
| **(d)** | Cửa sổ ở **chế độ chỉ đọc** | Kết quả mong đợi | đặc tả **im lặng** cho màn cán bộ (chỗ duy nhất ghi "Read-only" là `srs-fr-07:523`, thuộc màn của **vai trò Doanh nghiệp**) ⇒ xử theo nhánh phân đôi ở §4 |

### Đọc được gì trên ảnh đối tác

**Tệp:** `reverify-week-5/partner-evidence/QLHSPLDN_06.jpg` — ảnh tĩnh, **1915 × 1041** điểm ảnh, 222.176 byte,
md5 `f4d7dacb9389bbe8db3174f2cb9c1d1a` (**trùng md5** với bản ở `reverify-week-3/.../partner-evidence/` ⇒
cùng một tấm ảnh, không phải bằng chứng mới của tuần 5). **Đã mở full-res bằng tool Read**, đọc chữ trực tiếp.

| # | Vùng trên ảnh | Đọc được cụ thể |
|---|---|---|
| 1 | Thanh địa chỉ | `htpldn-uat.ospgroup.vn/doanh-nghiep/1a715c55-bc31-46de-ae07-56dd4f403ce5?tab=ho-so-pl` — **env nghiệm thu của đối tác**, tham số thẻ `ho-so-pl` |
| 2 | Đường dẫn phân cấp | "Trang chủ / Doanh nghiệp được hỗ trợ / **Chi tiết**" |
| 3 | Tiêu đề màn | "**Chi tiết DN #DN-XX-0005**" kèm mũi tên quay lại |
| 4 | Thanh thẻ | **Thông tin · Hồ sơ pháp lý (đang mở, gạch chân xanh) · Lịch sử hỗ trợ · Hồ sơ chi trả** — đúng 4 thẻ |
| 5 | Góc phải trên | `BTP · TW` · chuông `99+` · avatar `CU` · "**Cán bộ NV Trung ương**  `CB_NV_TW`" |
| 6 | Chân menu trái | "BỘ TƯ PHÁP — Hỗ trợ pháp lý doanh nghiệp — **HTPLDN · V1.0.3**"; đáy trang "Bộ Tư Pháp · Cục Bổ trợ tư pháp" |
| 7 | Menu trái | Tư vấn viên / Chuyê… · Tổ chức tư vấn · Người hỗ trợ pháp lý · Vụ việc HTPL · Chi trả chi phí · **Doanh nghiệp (đang chọn, nền xanh)** · Đánh giá hiệu quả · Biểu mẫu (Thư viện biểu mẫu / Danh sách biểu mẫu) · Tư vấn (Tư vấn chuyên sâu / Kho câu hỏi) |
| 8 | Khối bảng | Tiêu đề "**Hồ sơ pháp lý DN**" + nút xanh "**Thêm hồ sơ**" góc phải |
| 9 | Đầu cột | Mã hồ sơ · Tên hồ sơ · Loại · Lĩnh vực pháp lý · Nguồn · Ngày cấp · Ngày hết hạn · **Trạng**(bị cắt) · **Hành động** — **9 cột**, KHÔNG có cột "Có tệp đính kèm" |
| 10 | Hàng 1 | `HSPL-20260803-0001` · "TKM hồ sơ pháp lý …" (bị cắt) · Khác · Thuế · Thủ công · 03/08/2026 · 03/08/2026 · nhãn xanh "Hiệu lự…" · **[Sửa] [Xoá]** |
| 11 | Hàng 2 | `HSPL-20260731-0002` · "Hồ sơ x" · Giấy chứng nhận · Đất đai · Thủ công · 01/07/2026 · **"-"** (không có ngày hết hạn) · nhãn xanh "Hiệu lự…" · **[Sửa] [Xoá]** |
| 12 | **Khoảnh khắc lỗi** | Cột **Hành động** của **cả 2 hàng** chỉ có **đúng 2 nút chữ: `Sửa` (xanh) và `Xoá` (đỏ)**. Không có nút thứ ba, không có biểu tượng con mắt, không có nút "…" gom nhóm |
| 13 | Dưới bảng | **Thanh cuộn ngang** (bảng rộng hơn khung) + phân trang chỉ có trang **`1`** |
| 14 | Đồng hồ máy | **10:03 AM · 2026-08-03**, thanh tác vụ Windows (Zalo, Word, Chrome) |

**Kiểm bằng chứng có đúng case không:** ✅ đúng màn (thẻ *Hồ sơ pháp lý* trong Chi tiết DN), đúng vai trò
(`CB_NV_TW` cấp TW), đúng triệu chứng của ô *Kết quả thực tế*. Cột Hành động nằm sát mép phải và hiện đủ 2 nút
⇒ **không phải** đối tác bỏ sót do chưa cuộn ngang. ⇒ Phản ánh của đối tác **đúng với bản dựng họ chụp
(`V1.0.3`)**; tuyệt đối **không** được dùng verdict "không phải lỗi" kiểu "đối tác thao tác sai".

⚠️ Ảnh **không cho biết** hồ sơ nào có tệp đính kèm (bảng của họ không có cột đó) ⇒ vế (c) phải tự dựng tiền đề.

## 2. Neo bằng chứng (tối đa 3, lấy từ chính ảnh)

| # | Neo | Giá trị |
|---|---|---|
| 1 | URL / bản ghi | `…/doanh-nghiep/1a715c55-bc31-46de-ae07-56dd4f403ce5?tab=ho-so-pl` — DN **#DN-XX-0005**, thẻ *Hồ sơ pháp lý*, 2 hồ sơ `HSPL-20260803-0001` + `HSPL-20260731-0002`, phân trang 1 trang |
| 2 | Trạng thái | Cả 2 hồ sơ nhãn **"Hiệu lực"**, nguồn **Thủ công**; 1 hồ sơ có ngày hết hạn, 1 hồ sơ để trống (`-`) |
| 3 | Vai trò + env/bản dựng | **`CB_NV_TW`** — "Cán bộ NV Trung ương", phạm vi `BTP · TW`; env `htpldn-uat.ospgroup.vn`; bản dựng ghi trên màn **`HTPLDN · V1.0.3`**; chụp 10:03 ngày 03/08/2026 |

## 3. Đặc tả nói gì

Nguồn DUY NHẤT: `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/`. Mọi dòng dưới đây **đã mở file đọc
trực tiếp**, không trích theo trí nhớ.

**a) FR-X.1-04 — Quản lý hồ sơ pháp lý doanh nghiệp (UC150)**, `srs-fr-12-tv-chuyen-sau.md`:

- `:541` → `### FR-X.1-04: Quản lý hồ sơ pháp lý doanh nghiệp (UC150)`
- `:547` → `**Màn hình:** ~~SCR-X1-03~~ (DEPRECATED v2.1 — chuyển sang tab trong MH-07.2 chi tiết DN)`
  ⇒ **màn duy nhất còn thực thi FR này là đúng cái thẻ đối tác đang đứng** (xác nhận lại ở `:1176`:
  `### ~~SCR-X1-03: Hồ sơ Pháp lý DN~~ (DEPRECATED v2.1)` và `:1178` "Chuyển sang: Tab 'Hồ sơ PL' trong
  MH-07.2 chi tiết Doanh nghiệp").
- `:550` → *"CRUD hồ sơ pháp lý doanh nghiệp: xem danh sách, **xem chi tiết**, thêm mới, chỉnh sửa, xóa mềm,
  tìm kiếm."*
- `:552` → `**Tác nhân:** Cán bộ Nghiệp vụ (TW/BN/ĐP), Người hỗ trợ`
- `:573` → `| 10 | trang_thai | text | Y | HIEU_LUC / HET_HAN / THU_HOI | HIEU_LUC | người dùng chọn |`
- `:574` → `| 11 | file_dinh_kem | file | N | PDF/image, max 20MB | — | người dùng upload |` (tệp là **không bắt
  buộc** ⇒ ca "không có tệp" là hợp lệ, đúng chữ "(nếu có)" của đối tác)
- **Khối `**Processing — Xem chi tiết** [GAP-X.1-05]`** — `:634`:
  - `:640` → `| 3 | Trả full record: thông tin hồ sơ + thông tin DN liên kết | — |`
  - `:641` → `| 4 | Truy vấn danh sách file đính kèm (FILE_DINH_KEM) | — |`
  - `:642` → `| 5 | Trả kết quả bao gồm file đính kèm (tên, loại, dung lượng, URL preview) | — |`
- **Outputs** — `:663` `| 6 | ngay_cap | date | luôn | dd/mm/yyyy |` · `:664` `| 7 | ngay_het_han | date | luôn |
  dd/mm/yyyy |` · `:665` `| 8 | trang_thai | text | luôn | HIEU_LUC / HET_HAN / THU_HOI |`
- **Acceptance Criteria** — `:693` → *"**Given** CB NV xem chi tiết hồ sơ **When** chọn bản ghi **Then** hiển
  thị đầy đủ thông tin + file đính kèm"* · `:692` → *"…**Then** danh sách hồ sơ thuộc đơn vị, phân trang"*
- `:700` (AC vai trò NHT) → *"**Given** NHT xem chi tiết hồ sơ **When** chọn bản ghi thuộc DN của vụ việc được
  phân công **Then** hiển thị đầy đủ thông tin + file đính kèm; ngoài phạm vi → 403"*

**b) Màn hình chứa thẻ** — `srs-fr-07-doanh-nghiep.md`:

- `:455` → `### SCR-V.III-02: Chi tiết / Chỉnh sửa Doanh nghiệp` — chính màn đối tác đứng
- `:459` → *"Xem/chỉnh sửa chi tiết doanh nghiệp với 4 tab — Thông tin cơ bản …, **Hồ sơ pháp lý DN (CRUD
  entity HO_SO_PHAP_LY_DN, 5 loại × 3 trạng thái)**, Lịch sử Hỗ trợ …, Hồ sơ Chi trả …"*
- `:468` → `| 2 | tab | Tab Hồ sơ PL doanh nghiệp (MỚI v2.1) | tab | CRUD hồ sơ pháp lý DN: GIAY_PHEP /
  HOP_DONG / GIAY_CN / QUYET_DINH / KHAC. Trạng thái: HIEU_LUC / HET_HAN / THU_HOI. Gộp từ MH-12.3 (Tư vấn CS)
  | — | Chỉ khi xem chi tiết |`
- `:461` → *"**Quyền truy cập:** Cán bộ nghiệp vụ (TW / Bộ ngành / Địa phương) có quyền CRUD doanh nghiệp…"*

**c) Quy ước UI chung — cột Hành động** — `srs-v3.5.md`:

- `:6714` (**Phụ lục E §H, H6**) → *"Cột Hành động dạng icon + tooltip BẮT BUỘC | Cột Hành động trong mọi bảng
  dùng icon (**Mắt = Xem**, Bút = Sửa, Thùng rác = Xóa, …) thay cho nhãn text. **Mỗi icon BẮT BUỘC có
  `aria-label` và tooltip hover** mô tả hành động (vd. "Xem chi tiết", "Chỉnh sửa", "Xóa mềm"). Đáp ứng WCAG
  4.1.2 — không icon-only. | BẮT BUỘC"*
- `:6705` → *"Áp dụng cho **mọi màn hình** trong hệ thống (… DN …)"* ⇒ H6 áp cho đúng bảng này.
  ⇒ Ghép `:6714` với `:550` : **chức năng "Xem" là một thành phần bắt buộc của cột Hành động**, không phải tuỳ chọn thiết kế.

**d) Nhãn hiển thị** — `srs-fr-05-vu-viec.md:1490-1492` (§B, Phụ lục E §A–G áp toàn hệ thống theo
`srs-v3.5.md:6699-6701`) → *"Khi render UI, dev **phải dịch** mã DB (snake_case enum) sang nhãn tiếng Việt…
Mã DB **không bao giờ** xuất hiện trên giao diện người dùng."*

### ĐẶC TẢ IM LẶNG / MƠ HỒ về

- **"Chế độ chỉ đọc" của cửa sổ chi tiết trên màn CÁN BỘ** — vế (d). Cụm "Read-only" chỉ xuất hiện ở
  `srs-fr-07-doanh-nghiep.md:523` → `| 4 | tab | Tab 2 — Hồ sơ pháp lý DN | tab | Read-only danh sách
  HO_SO_PHAP_LY_DN | Luôn |`, nhưng dòng này thuộc **SCR-V.III-04 "Hồ sơ doanh nghiệp của tôi"**
  (`:508`, `:514` "Quyền truy cập: Doanh nghiệp (Tier 2 VNeID)… Vai trò khác KHÔNG truy cập trang này")
  ⇒ **không** áp cho màn cán bộ. Với màn cán bộ, đặc tả chỉ tách **Processing Xem chi tiết** (`:634`) khỏi
  **Processing Chỉnh sửa** (`:607`) mà không nói cửa sổ Xem có được sửa hay không ⇒ xử theo nhánh phân đôi ở §4.
- **Hình dạng cụ thể của "cửa sổ chi tiết"** (lớp nổi hay trang riêng, danh sách trường nào phải hiện, thứ tự
  trường) — đặc tả không liệt kê thành phần màn cho khối này (SCR-X1-03 đã DEPRECATED ở `:547`/`:1176` mà
  bản thay thế `srs-fr-07:468` chỉ ghi vỏn vẹn "CRUD"). ⇒ Chỉ chấm được **nội dung** (`:640`, `:693`), **không
  chấm** bố cục/kiểu cửa sổ.
- **Ô tìm kiếm / bộ lọc / Xuất Excel trên thẻ này** — `srs-fr-12:576-584` khai 5 bộ lọc và `:644-652` khai hẳn
  khối *Processing — Xuất Excel*, nhưng mô tả thẻ ở `srs-fr-07:468` **chỉ ghi "CRUD"**. Hai chỗ **không khớp
  nhau** ⇒ nhánh **cần BA**, và **ngoài vế** của case này (xem §4 "KHÔNG được chấm Fail vì").

---

## 4. Tiêu chí chấm

### Precondition (điều kiện đo — chuẩn bị TRƯỚC khi mở màn tranh chấp)

- **Tài khoản ra verdict: `cbnv_tw_04` / `Test@1234`** — vai trò **CB_NV_TW** (Cán bộ Nghiệp vụ Trung ương),
  cấp **TW**, đơn vị Cục Bổ trợ tư pháp - Bộ Tư pháp.
  **Vì sao chọn:** ① ô *Tác nhân* của đặc tả (`srs-fr-12:552`) là "Cán bộ Nghiệp vụ (TW/BN/ĐP)"; ② ảnh đối tác
  đọc được đúng chuỗi "Cán bộ NV Trung ương `CB_NV_TW`" + phạm vi `BTP · TW` ⇒ **trùng vai trò + trùng cấp
  + trùng đơn vị**, không nới chiều nào; ③ `srs-fr-07:461` yêu cầu vai trò cán bộ nghiệp vụ mới vào được
  SCR-V.III-02. **KHÔNG dùng `admin`/QTHT để ra verdict** (quyền rộng che lỗi phân quyền — flow 04 §Giai đoạn B
  bước 1); admin chỉ được dùng để chuẩn bị dữ liệu nếu bắt buộc.
  Login fail → fallback **cùng vai trò + cùng cấp** (`cbnv_tw_02` → `_03` → `_05` → `cbnv_tw`), ghi rõ account
  thực dùng; hết siblings → BLOCKED, **cấm** đổi sang cấp/vai trò khác.
- **Màn:** menu **Doanh nghiệp** → mở chi tiết 1 DN → thẻ **Hồ sơ pháp lý** (`/doanh-nghiep/{id}?tab=ho-so-pl`).
  Đi đúng 4 bước của phiếu bằng **UI thật** (bấm menu, bấm nút xem chi tiết trên hàng DN), không nhảy thẳng URL.
- **Tiền đề dữ liệu:** 1 DN trong phạm vi đơn vị, có **≥1 hồ sơ pháp lý**, và phủ đủ 4 dạng ở §5. Thiếu dạng
  nào → **seed bằng chính UI [Thêm hồ sơ]** của tài khoản trên (đặc tả `srs-fr-12:596-605`), rồi khai vào báo
  cáo: **đổi/bổ sung bản ghi nào · đổi gì · trên env nào**. Tiền đề tạo được mà không tạo ⇒ **CẤM ra verdict**.
- **Tải lại trang** trước khi đo (tab mở lâu vẫn chạy bó mã cũ) và ghi vân tay bản dựng vào §7.
- **Cài bộ bắt thông báo TRƯỚC** mọi thao tác ghi (bước seed): dùng `tools/toast-capture.js` — không lọc trùng,
  đọc `innerText`, đếm request song song, tự kiểm observer còn sống.

### ✅ PASS — chỉ khi ĐỦ CẢ 5 nhóm A→E

**A. Có chức năng mở chi tiết trên MỌI hàng** *(vế a)*

1. Đếm **thô** số hàng dữ liệu của bảng Hồ sơ pháp lý DN trên trang đang xem (`.ant-table-tbody
   tr.ant-table-row`) = **N**; đếm **thô** số điều khiển mở chi tiết trong ô Hành động của chính các hàng đó = **N**
   (mỗi hàng ≥1). **Cấm** `unique`/lọc/gộp trước khi đếm; **cấm** lấy mẫu 2-3 hàng rồi suy ra cả bảng.
2. Đếm lại bằng **≥2 cách độc lập** cho ra cùng N (vd: đếm điều khiển trong ô cuối mỗi hàng · đếm phần tử có
   nhãn/`aria-label`/tooltip mang nghĩa "Xem"/"Xem chi tiết", đọc bằng **`innerText`** — không `textContent`).
3. Điều khiển **dùng được thật**, đo trên **từng hàng**: `disabled = false` · không `aria-disabled="true"` ·
   `pointer-events ≠ none` · `opacity = 1` · hình chữ nhật thật **> 0×0** · toạ độ nằm trong khung nhìn (hoặc
   truy cập được sau khi cuộn).

**B. Bấm thật thì MỞ ĐƯỢC cửa sổ chi tiết** *(vế b — chống Pass bằng quan sát tĩnh)*

4. Bấm bằng **chuột thật qua UI** (không `dispatchEvent`, không gọi thẳng hàm JS) trên **≥1 hồ sơ của MỖI dạng
   D1–D4 ở §5**. Sau mỗi lần bấm: xuất hiện cửa sổ/lớp nổi chi tiết, **đọc được tiêu đề + nội dung bằng
   `innerText`** và **chụp ảnh, mở ảnh ra đọc bằng mắt** (cấm kết luận 100% bằng script chạy trong trang).
5. Selector dò cửa sổ trả 0 **không** được kết luận "không mở" — phải đo lại bằng đường khác (quét lớp bao
   ngoài, đọc `innerText` toàn trang, chụp ảnh) rồi mới chốt. Nếu có lời gọi lấy chi tiết thì mã trả về phải
   **2xx**; nếu FE lấy dữ liệu từ danh sách đã tải (0 lời gọi) thì **không** vì thế mà chấm Fail.

**C. Nội dung cửa sổ KHỚP hồ sơ gốc** *(vế b — chống Pass oan "có cửa sổ là đủ")*

6. Với **mỗi** hồ sơ đã bấm, đối chiếu **từng trường** trên cửa sổ với **nguồn độc lập** (đọc lại bản ghi qua
   lời gọi máy chủ trong cùng phiên, và/hoặc so với chính hàng trên bảng cho các trường có mặt ở bảng):
   **mã hồ sơ · tên hồ sơ · loại hồ sơ · lĩnh vực pháp lý · nguồn · cơ quan cấp · ngày cấp · ngày hết hạn ·
   trạng thái · mô tả**. Mọi trường đọc được phải **khớp nguyên văn**; ngày theo `dd/mm/yyyy` (`:663`, `:664`).
   Bấm lại cùng nút **không** tính là phương pháp thứ hai.
7. Không trường nào hiện `null` / `undefined` / `[object Object]` / ô rỗng mất cả nhãn trường. Trường bỏ trống
   (ngày hết hạn, cơ quan cấp, lĩnh vực, mô tả) phải hiện ký hiệu rỗng — đúng như hàng 2 trong ảnh đối tác (`-`).

**D. Danh sách tệp đính kèm** *(vế c)*

8. Hồ sơ **CÓ tệp** (dạng D1): cửa sổ hiển thị mục tệp đính kèm, **nhận diện được từng tệp bằng tên tệp**, và
   **số tệp hiển thị = số tệp thực có của bản ghi** (đối chiếu bằng đường thứ hai: đọc lại bản ghi qua máy chủ
   hoặc mở biểu mẫu Sửa của chính hồ sơ đó). Căn cứ `:641`, `:642`, `:693`.
9. Hồ sơ **KHÔNG có tệp** (dạng D2): cửa sổ **vẫn mở bình thường**, có trạng thái rỗng đọc được (hoặc không có
   mục tệp) — **không** trắng cửa sổ, **không** lỗi trên bảng điều khiển. Chữ "(nếu có)" trong Kết quả mong đợi
   + `:574` (file **không bắt buộc**) ⇒ ca này **không phải lỗi**.

**E. Chế độ chỉ đọc** *(vế d — đặc tả IM LẶNG, chấm theo 3 nhánh, không tự bịa chuẩn)*

10. Đếm **thô** trong phạm vi cửa sổ: `input`, `textarea`, `select`, `.ant-select`, `.ant-picker`,
    `[contenteditable="true"]`, và nút lưu/gửi.
    - **= 0 ô nhập và không có nút lưu** ⇒ đúng kỳ vọng đối tác ⇒ **hết bất đồng**, vế (d) đạt, **không cần hỏi BA**.
    - **Bấm "Xem" mở ra đúng biểu mẫu chỉnh sửa** (có ô nhập + nút lưu, sửa và lưu được) ⇒ **FAIL** — vì như vậy
      không tồn tại thao tác "xem chi tiết" tách khỏi "chỉnh sửa" như `:634` vs `:607`, và trái Kết quả mong đợi.
    - **Ca lửng** (có vài ô nhập nhưng không lưu được / chỉ là ô tìm kiếm trong cửa sổ) ⇒ **ghi nhận hiện trạng,
      KHÔNG chấm Pass/Fail vế này**, chuyển **cần BA** kèm câu hỏi: *màn cán bộ, cửa sổ xem chi tiết hồ sơ pháp lý
      có được phép chỉnh sửa tại chỗ không, hay chỉ đọc như SCR-V.III-04:523 quy định cho màn của DN?*

> **Verdict tổng của case (case gộp nhiều vế — flow 04 §Ca biên):** mọi vế (a)(b)(c) đạt **và** vế (d) rơi vào
> nhánh 1 ⇒ **Pass**. Còn ≥1 vế lỗi ⇒ **Reopen**. Không vế nào lỗi nhưng vế (d) rơi vào nhánh 3 ⇒ **cần BA**.

### ❌ FAIL (Reopen) nếu ≥1 trong các điều sau

- **≥1 hàng bất kỳ** (ở bất kỳ dạng D1–D4 nào) **không có** điều khiển mở chi tiết — kể cả khi các hàng khác có.
  Ca "chỉ hàng *Hiệu lực* có nút, hàng *Hết hạn*/*Thu hồi* không có" = **fix một phần** ⇒ vẫn FAIL.
- Có điều khiển nhưng **bấm bằng UI thật không mở được gì** (không cửa sổ, lỗi trên bảng điều khiển, hoặc điều
  hướng sang màn khác thay vì mở chi tiết), hoặc điều khiển bị vô hiệu hoá / kích thước 0×0 / bị che không bấm được.
- Cửa sổ mở nhưng **≥1 trường lệch** so với nguồn độc lập, hoặc hiện `null`/`undefined`/`[object Object]`.
- Hồ sơ **có tệp** mà cửa sổ **không liệt kê tệp**, hoặc **số tệp lệch** so với bản ghi thực.
- Hồ sơ **không có tệp** mà cửa sổ **vỡ** (trắng / văng lỗi / không mở được).
- Bấm "Xem" mở ra **biểu mẫu chỉnh sửa lưu được** (E10 nhánh 2).
- Fix **đẻ ra lỗi mới ngay trong luồng này** (vd bấm Xem xong bảng mất dữ liệu, hoặc mở cửa sổ thì không đóng được).

### ⚠️ KHÔNG được chấm Fail vì (chống FAIL oan — ghi nhận / log riêng, KHÔNG kéo verdict case)

- **Điều khiển là nhãn chữ "Xem" thay vì icon con mắt, hoặc thiếu `aria-label`/tooltip.** `srs-v3.5.md:6714`
  (H6) có quy định thật, nhưng đó **không phải vế đối tác nêu** (họ nói *thiếu hẳn chức năng*). Phát hiện lệch
  H6 ⇒ log riêng theo flow §"Bug mới trực tiếp trong luồng", giữ nguyên verdict case.
- **Thẻ này không có ô tìm kiếm / bộ lọc / nút Xuất Excel.** Hai chỗ trong đặc tả không khớp nhau
  (`srs-fr-12:576-584` + `:644-652` **có** ↔ `srs-fr-07:468` chỉ ghi "CRUD") ⇒ **cần BA**, không tự chấm là lỗi.
- **Không bấm được vào hàng để mở chi tiết** (chỉ mở bằng nút). Đặc tả **không** quy định click-hàng cho bảng này.
- **Cửa sổ chi tiết không hiển thị thông tin DN liên kết.** `:640` là bước xử lý **phía máy chủ** ("trả full
  record"), còn cửa sổ đang mở **bên trong** màn chi tiết của chính DN đó ⇒ ghi nhận, đưa candidate cho BA nếu
  cần, **không** kéo verdict.
- **Bố cục / thứ tự trường / kiểu cửa sổ (lớp nổi hay trang riêng) / màu nhãn trạng thái / bảng phải cuộn ngang
  mới thấy cột Trạng thái** — đặc tả không quy định (SCR-X1-03 DEPRECATED, bản thay thế chỉ ghi "CRUD").
- **Ký hiệu ô trống không nhất quán** (`—` ở cột này, `-` ở cột kia) — thuần mỹ thuật.
- **Vai trò khác** (NHT theo `:700`-`:701`, hoặc vai trò Doanh nghiệp ở SCR-V.III-04) — **ngoài vế của case**;
  flow cấm tự mở rộng sang mọi vai trò. Chỉ đo đúng vai trò của đối tác.
- **Mã enum thô hiện trên màn** (`HIEU_LUC`, `GIAY_CN`, `THU_CONG`) — có căn cứ ở `srs-fr-05:1492` nhưng **khác
  vế**; log riêng, không kéo verdict (trừ khi vì thế mà trường trở nên sai/không đọc được ⇒ rơi vào C6).

---

## 5. Dạng dữ liệu phải phủ — **M = 4**

Case là "thiếu điều khiển trên hàng của bảng" ⇒ phải chứng minh điều khiển có ở **mọi dạng hàng**, không chỉ
dạng may mắn có sẵn trong môi trường.

| # | Dạng | Vì sao là một dạng riêng (căn cứ) | Vế nào cần |
|---|---|---|---|
| **D1** | Hồ sơ **CÓ ≥1 tệp đính kèm** | `:641`, `:642` quy định riêng việc truy vấn + trả danh sách tệp; đây là dạng **duy nhất** chứng minh được vế (c) | (a)(b)(c) |
| **D2** | Hồ sơ **KHÔNG có tệp** | `:574` khai `file_dinh_kem` **không bắt buộc**; đối tác ghi rõ "(nếu có)" ⇒ phải chứng minh cửa sổ không vỡ ở ca rỗng | (a)(b)(c) |
| **D3** | Hồ sơ ở **cả 3 trạng thái**: Hiệu lực · Hết hạn · Thu hồi | `:573` + `srs-fr-07:468` khai đúng 3 trạng thái; đây là biến thể kinh điển làm nút biến mất theo điều kiện hiển thị | (a)(b) |
| **D4** | Hồ sơ có **trường tuỳ chọn để trống** (không ngày hết hạn / không cơ quan cấp / không lĩnh vực / không mô tả) | `:568-:572` khai 5 trường **không bắt buộc**; **chính ảnh đối tác** có hàng ngày hết hạn `-` ⇒ ca này có thật trên dữ liệu đối tác | (b) |

**Nguồn xác định M:** ① bảng Inputs `:562-:574` (trường nào bắt buộc / tuỳ chọn, enum trạng thái); ② khối
Processing Xem chi tiết `:634-:642` (tệp đính kèm là một vế riêng); ③ chính bằng chứng đối tác (hàng có ngày
hết hạn `-`).

**Thiếu dạng nào trong env → SEED bằng UI [Thêm hồ sơ]** của đúng tài khoản ra verdict, rồi khai vào báo cáo:
đổi/tạo bản ghi nào · đổi gì · env nào. **Không** ghi thẳng cơ sở dữ liệu, **không** đoán đường dẫn máy chủ.
Dạng **không dựng được** (vd hồ sơ `nguon = CONG_PLQG` phải đến từ API inbound của Cổng PLQG) ⇒ **không** coi
là dạng bắt buộc: đối tác cũng chỉ có hồ sơ `Thủ công` (đọc được trên ảnh) nên không lệch điều kiện với họ.

**Độ phủ hàng:** đo **toàn bộ hàng của trang đang xem, đếm thô, không lấy mẫu**. Bấm mở chi tiết ít nhất
**1 hồ sơ cho mỗi dạng D1–D4** (một hồ sơ có thể phủ nhiều dạng cùng lúc — ghi rõ hồ sơ nào phủ dạng nào).

---

## 6. Bảng điều kiện

| Điều kiện có thể đổi kết quả | Đối tác | Mình test lần này | GAP? |
|---|---|---|:-:|
| **Vai trò** / tài khoản | `CB_NV_TW` — badge "Cán bộ NV Trung ương  `CB_NV_TW`", phạm vi `BTP · TW` (đọc trên ảnh) | `cbnv_tw_04` / `Test@1234` — vai trò `CB_NV_TW`, cấp TW, đơn vị Cục Bổ trợ tư pháp - Bộ Tư pháp. **Trùng vai trò + trùng cấp + trùng đơn vị, không nới chiều nào.** Không dùng `admin` ra verdict | **Không** |
| **Entity** + trạng thái | `HO_SO_PHAP_LY_DN` — 2 bản ghi, **cả 2 đều "Hiệu lực"**, nguồn "Thủ công", 1 trang | `HO_SO_PHAP_LY_DN` trên cùng loại màn — đo **đủ 3 trạng thái** `Hiệu lực` / `Hết hạn` / `Thu hồi` (`:573`), nguồn Thủ công. Bao trùm chặt hơn đối tác | **Không** |
| Dữ liệu **tiền đề** | DN `#DN-XX-0005` (env đối tác) có sẵn 2 hồ sơ; ảnh **không cho biết** hồ sơ nào có tệp | DN QA trong phạm vi đơn vị, có ≥1 hồ sơ; phủ đủ D1–D4 ở §5 — thiếu dạng nào thì **seed bằng UI [Thêm hồ sơ]** (`:596-605`) và khai rõ bản ghi/đổi gì/env nào. Không đụng dữ liệu của đối tác | **Không** |
| Input / **filter** / thao tác | Không nhập, không lọc gì — ảnh chụp ngay khi vừa mở thẻ; bảng đang cuộn ngang; phân trang 1 trang | Không nhập, không lọc, đo ngay khi vừa mở thẻ (đúng 4 bước của phiếu, bằng UI thật); có tải lại trang trước khi đo; đo cả khi bảng đang cuộn ngang để chắc điều khiển không bị che | **Không** |
| **Độ phủ** biến thể | N = 2 hàng (1 trang) · 1 trạng thái (Hiệu lực) · 1 dạng ngày hết hạn trống · 0 thông tin về tệp đính kèm | N = **toàn bộ hàng trang đang xem, đếm thô** · **M = 4 dạng** (D1 có tệp · D2 không tệp · D3 đủ 3 trạng thái · D4 trường tuỳ chọn trống) · bấm mở thật ≥1 hồ sơ mỗi dạng | **Không** |
| Env + bản dựng | `htpldn-uat.ospgroup.vn`, chuỗi trên màn **`HTPLDN · V1.0.3`**, chụp 03/08/2026 10:03 | `18.143.165.120.nip.io` (env **NỘI BỘ**), bản dựng ghi ở §7 | **Không** — lệch env/bản dựng là **giới hạn hiệu lực** của verdict (Pass = **Pass tạm** cho tới khi bản dựng lên env đối tác), không phải chênh điều kiện đo |

**Nếu khi đo phát sinh chênh lệch mới** (vd không dựng nổi dạng D1 vì tải tệp lên bị chặn) ⇒ **sửa ngay ô GAP
thành `CÓ — <thiếu gì>`**, và theo flow: chênh lệch quyết định kết quả mà chưa đo được ⇒ **để verdict trống**,
ghi rõ cần bổ sung gì. Cấm để trống ô GAP, cấm ghi `...`.

---

## 7. Bản dựng thực tế khi đo — **người đo điền, không copy sẵn**

> Tham chiếu vân tay đã đo đầu đợt: `reverify-week-5/BAN-DUNG.md` (18:44 ngày 06/08 — `HTPLDN · V1.0.8`,
> bó mã `assets/index-DIABnbIr.js`, `last-modified: Thu, 06 Aug 2026 07:13:15 GMT`, `etag W/"6a74340b-428"`).
> **Vẫn phải đo lại tại thời điểm chạy case này** — dự án hay deploy lại mà **không đổi chuỗi phiên bản**, nên
> chỉ ghi "V1.0.8" là sau này không biết đã đo bản nào.

| Hạng mục | Giá trị đo được khi chạy case này |
|---|---|
| Thời điểm đo (bắt đầu → kết thúc) | **2026-08-06 18:54 → 18:59 (giờ VN)** |
| Môi trường | `https://18.143.165.120.nip.io` — env **NỘI BỘ** |
| Chuỗi phiên bản trên màn (chân sidebar) | `HTPLDN · V1.0.8` |
| Bó mã FE (`assets/index-*.js` / `*.css`) | `assets/index-DIABnbIr.js` · `assets/index-DVlgOkLg.css` · `assets/index-DNsk8fKL.css` — **đọc lại sau khi tải lại trang bỏ qua bộ nhớ đệm lúc 18:54**, không đổi so với đầu đợt |
| `GET /` — `last-modified` + `etag` | `Thu, 06 Aug 2026 07:13:15 GMT` · `W/"6a74340b-428"` |
| Tài khoản thực dùng ra verdict (kèm ghi chú nếu phải fallback) | **`cbnv_tw` / `Test@1234`** — KHÔNG phải `cbnv_tw_04` như §4 đề xuất. **Lý do khai rõ:** `cbnv_tw` nằm trong chính chuỗi dự phòng §4 khai sẵn, và `GET /api/v1/auth/me` xác nhận **trùng cả 3 chiều**: vai trò `["CB_NV_TW"]` · cấp `TW` · `donViId 00000000-0000-4000-8000-000000000001` (Cục Bổ trợ tư pháp — đọc được ở chân menu trái). Đây cũng là đúng tên đăng nhập đối tác ghi ở ô *Tác nhân* của bảng. **Không nới chiều nào**; không dùng `admin` |
| DN + danh sách mã hồ sơ đã đo (kèm dạng D1–D4 mỗi hồ sơ phủ) | DN **`DN-HNI-0001`** *Cong ty TNHH QA UAT Kiem Thu* (`829abcac-…`), thẻ `?tab=ho-so-pl`, **7/7 hàng đo hết, đếm thô, không lấy mẫu**. Bấm mở thật 3 hồ sơ: `HSPL-20260803-0001` (**D1** có 1 tệp + trạng thái *Hiệu lực*) · `HSPL-20260803-0002` (**D2** không tệp + **D4** 5 trường trống + trạng thái *Thu hồi*) · `HSPL-20260721-0001` (**D3** trạng thái *Hết hạn* + có tệp). ⇒ phủ đủ D1·D2·D3 (cả 3 trạng thái)·D4 |
| Bản ghi đã seed (mã · đổi gì · env) | **KHÔNG seed gì.** Dữ liệu sẵn có của DN-HNI-0001 đã phủ đủ 4 dạng ⇒ không mutate môi trường |
| Ảnh bằng chứng (đường dẫn + 1 dòng "thấy gì trong ảnh") | `image/QLHSPLDN_06-D1-chitiet-HSPL-20260803-0001-co-tep.png` — lớp nổi *Chi tiết hồ sơ pháp lý* của `HSPL-20260803-0001`, đọc được 10 trường + mục **Tệp đính kèm** liệt kê `QA-EDIT-A-tep-moi.png (191 B)` kèm 2 nút Xem/Tải, chân cửa sổ chỉ có nút **Đóng** (không nút lưu) · `image/QLHSPLDN_06-D2D4-chitiet-HSPL-20260803-0002-khong-tep-truong-trong.png` — cùng lớp nổi cho hồ sơ không tệp: 5 trường trống hiện `—` (không `null`), mục tệp hiện chữ **"Chưa có tệp đính kèm"**, cửa sổ không vỡ · `image/QLHSPLDN_06-D3-chitiet-HSPL-20260721-0001-het-han.png` — hồ sơ trạng thái **Hết hạn** vẫn mở được cửa sổ, có tệp `QA-EDIT-A-tep-moi.png (191 B)` |

### Kết quả đo theo 5 nhóm tiêu chí

| Nhóm | Số đo | Đạt? |
|---|---|:-:|
| **A** — mọi hàng có điều khiển mở chi tiết | Đếm thô `.ant-table-tbody tr.ant-table-row` = **7 hàng**; đếm thô nút trong ô Hành động = **7 nút "Xem"** (mỗi hàng đúng 1, ô Hành động có 3 nút: `Xem`·`Sửa`·`Xoá`). Cách đếm độc lập thứ hai (quét `.anticon-eye` trong thân bảng) = **7** → khớp. Từng nút: `disabled=false` · không `aria-disabled` · `pointer-events:auto` · `opacity:1` · kích thước thật **68×24 px** · toạ độ x=1164 trong khung nhìn | ✅ |
| **B** — bấm thật mở được cửa sổ | Bấm bằng chuột thật qua giao diện 3 lần (3 dạng) → cả 3 lần đều mở lớp nổi tiêu đề **"Chi tiết hồ sơ pháp lý"**; đã chụp ảnh và mở ảnh đọc lại | ✅ |
| **C** — nội dung khớp hồ sơ gốc | Đối chiếu **từng trường** với bản ghi đọc lại từ máy chủ trong cùng phiên (`GET /api/v1/ho-so-phap-ly-dns/{id}`): `HSPL-20260803-0001` khớp **10/10** trường (`GIAY_PHEP`→*Giấy phép*, `THU_CONG`→*Thủ công*, `HIEU_LUC`→*Hiệu lực*, `2026-08-01`→`01/08/2026`, `2026-12-31`→`31/12/2026`, cơ quan cấp + mô tả khớp nguyên văn); `HSPL-20260721-0001` khớp 10/10 (`HET_HAN`→*Hết hạn*, `2026-08-10`→`10/08/2026`, `2026-11-30`→`30/11/2026`); `HSPL-20260803-0002` khớp 10/10 (mọi trường `null` → hiện `—`). **Không** trường nào hiện `null`/`undefined`/`[object Object]`; **không** mã enum thô lọt ra giao diện | ✅ |
| **D** — danh sách tệp đính kèm | Hồ sơ **có tệp**: cửa sổ liệt kê **1 tệp** `QA-EDIT-A-tep-moi.png (191 B)` — máy chủ trả **đúng 1 tệp** `QA-EDIT-A-tep-moi.png` dung lượng `191` byte ⇒ **số tệp khớp + tên tệp khớp + dung lượng khớp**. Hồ sơ **không tệp**: cửa sổ vẫn mở, hiện trạng thái rỗng đọc được **"Chưa có tệp đính kèm"**, không trắng, không lỗi bảng điều khiển | ✅ |
| **E** — chế độ chỉ đọc | Đếm thô trong phạm vi cửa sổ: `input`+`textarea`+`select`+`.ant-select`+`.ant-picker`+`[contenteditable]` = **0** ở cả 3 lần mở; danh sách nút của cửa sổ chỉ gồm `Xem`/`Tải` (thao tác trên tệp) và `Đóng` — **không có nút lưu/gửi** ⇒ rơi vào **nhánh 1** của E10: đúng kỳ vọng đối tác, **hết bất đồng, không cần hỏi BA** | ✅ |

**Bảng điều khiển trình duyệt:** `list_console_messages` lọc `error`+`warn` → **không có thông điệp nào** trong suốt luồng ⇒ không phát hiện lỗi mới do bản vá gây ra trong chính luồng này.

**Ô GAP §6 giữ nguyên `Không` cho cả 6 hàng** — không phát sinh chênh lệch mới khi đo (không phải seed, phủ được đủ 4 dạng, đúng vai trò/cấp/đơn vị).

> **Ghi nhớ khi chốt:** Pass chỉ có hiệu lực cho **đúng env + đúng bản dựng ghi ở bảng trên**. Đo trên env nội
> bộ ⇒ ghi rõ là **Pass tạm** cho tới khi bản dựng này lên env nghiệm thu của đối tác. Nếu bản dựng đổi giữa
> chừng (bó mã / `last-modified` khác) ⇒ **đo lại**, không gộp số đo của 2 bản dựng vào một verdict.
