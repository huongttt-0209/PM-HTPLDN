# Tiêu chí verify — QLHSPLDN_07

```
Mã case: QLHSPLDN_07 (tab `bug`, dòng 292 — Tuần 3)     Thời điểm viết: 2026-08-06 (GIAI ĐOẠN A)
Môi trường verify: https://18.143.165.120.nip.io  (env NỘI BỘ — đối tác đo trên env nghiệm thu khác)
Bản dựng: CHƯA ĐO LẠI CHO CASE NÀY — bắt buộc đo và điền ở §7 ngay trước khi bấm nút đầu tiên.
          Số gần nhất của đợt (lô B7 cùng ngày): `HTPLDN · V1.0.8` · gói mã `/assets/index-DIABnbIr.js`
          · `GET /` last-modified `Thu, 06 Aug 2026 07:13:15 GMT` · etag `W/"6a74340b-428"`
          (nguồn: reverify-week-5/BAN-DUNG.md — chuỗi V1.0.x KHÔNG đủ làm vân tay, phải neo bó mã + last-modified)
Trạng thái phiếu: Trạng thái = Fail · Dopai = dev done · Trạng thái dev fix = Fixed · Kết quả verify = (trống)
```

> **Khai báo hồ sơ QA nội bộ đã đọc trước khi viết §4 và §5** (bắt buộc theo flow 04 §GIAI ĐOẠN A):
> - `reverify-week-3/verify1-conlai-2026-08-03/reverify-audit/QLHSPLDN_07.md` — **vòng 1** (03/08, bản
>   `V1.0.5`, tài khoản `cbnv_tw_04`): 3 kịch bản A / A2 / B × 9 trường = 27 ô đo, kết luận Pass.
>   Có ghi nhận 3 lần *phép đo nói dối* (sai class đếm tệp `.ant-upload-list-item-container`, sai class
>   đọc ô chọn `.ant-select-content`, `fill_form` nối chuỗi thay vì thay thế) — **giữ lại làm cảnh báo dụng cụ**.
> - `reverify-week-3/verify1-conlai-2026-08-03/cond/QLHSPLDN_07.md` — bảng đối chiếu điều kiện vòng 1, 0 GAP.
> - `reverify-week-3/uat-luong3-2026-08-04/cases/QLHSPLDN_07.md` — nội dung phiếu + giải trình dev lần 1.
> - `reverify-week-3/uat-luong3-2026-08-04/cond/QLHSPLDN_07.md` — bản sao phiếu dạng mục.
> - `reverify-week-3/uat-luong3-2026-08-04/reverify-audit/QLHSPLDN_07-vong2.md` — **vòng 2** (04/08, bản
>   `V1.0.5`, tài khoản `cb_nv_tw_01`): tạo mới `HSPL-20260804-0001` rồi sửa 8 ô + thêm tệp, kết luận Pass;
>   tự khai bộ đếm request hỏng ở lượt sửa bản ghi cũ (`SO_REQUEST = 0` do quên bọc `XMLHttpRequest`).
>
> **§4 và §5 dưới đây suy TỪ ĐẶC TẢ + bằng chứng đối tác, KHÔNG lấy số đo cũ làm chuẩn chấm.**
> Hai vòng trước đo trên bản `V1.0.5`; lần này bản dựng khác (§7) ⇒ **27/27 ô cũ không chứng minh gì cho lượt
> này**, phải đo lại từ đầu. Đặc biệt: cả 2 vòng cũ đều **sửa nhiều ô cùng lúc rồi mới thêm tệp**, trong khi
> đối tác **chỉ thêm tệp và không đụng ô nào khác** — đây là chênh lệch kịch bản đã bị bỏ sót 2 vòng liền
> (xem D1 ở §5).

---

## 1. Đối tác phản ánh

Mô tả case: **"Sửa"** — màn *Doanh nghiệp → Xem chi tiết → thẻ "Hồ sơ pháp lý doanh nghiệp" → nút "Sửa"*.

**Kết quả mong đợi (nguyên văn ô của đối tác):** *"- Hệ thống mở cửa sổ chỉnh sửa với dữ liệu hiện có.
- NSD cập nhật và bấm "Lưu", hệ thống cập nhật bản ghi và lưu vết thao tác."*
**Kết quả thực tế (nguyên văn):** *"Hệ thống hiển thị thông báo cập nhật thành công nhưng dữ liệu chưa được
cập nhật vào bản ghi"*

Case này **gộp 3 vế**, phải tách để chấm (flow 04 §Ca biên — *mọi vế hết lỗi mới Pass*):

| Vế | Nội dung đối tác nêu | Nguồn ô | Trạng thái đặc tả |
|---|---|---|---|
| **(a)** | Cửa sổ chỉnh sửa **mở kèm dữ liệu hiện có** | Kết quả mong đợi, câu 1 | đặc tả **nói rõ** (`srs-fr-12:560-574` Inputs Thêm mới/**Chỉnh sửa**; `srs-fr-12:693`) — khớp kỳ vọng |
| **(b)** | Bấm Lưu → **hệ thống cập nhật bản ghi** (đối tác đo thấy: báo thành công nhưng KHÔNG lưu) | Kết quả mong đợi câu 2 + Kết quả thực tế | đặc tả **nói rõ** (`srs-fr-12:613`, `:674`, `:695`, `:701`) — khớp kỳ vọng |
| **(c)** | Bấm Lưu → **lưu vết thao tác** | Kết quả mong đợi, câu 2 | đặc tả **nói rõ yêu cầu** (`srs-fr-12:614`, `:676`, `:701`; `srs-fr-07:160`, `:819-821`) nhưng **im lặng về bề mặt để đọc lại log của 1 bản ghi HSPL** ⇒ xem nhánh ở §4 |

### Bằng chứng đã xem — đọc được gì, ở mốc giây nào

**① `partner-evidence/QLHSPLDN_07-1.webm`** — 218.405 byte. **Không phải video**: là **1 khung MJPEG
1907×1031** bọc trong vỏ `.webm` (giải mã ra đúng 1 frame, `pts = 0.00s`). Băm MD5 `bc8860c5…d4d7` **trùng
byte-for-byte** với `reverify-week-3/verify1-conlai-2026-08-03/partner-evidence/QLHSPLDN_07-1.jpg` ⇒ **cùng
một tấm ảnh, chỉ đổi phần mở rộng**. Đã mở full-res (`frames/QLHSPLDN_07/v1/t000.00s.jpg`). Đọc được:

- Thanh địa chỉ: `htpldn-uat.ospgroup.vn/doanh-nghiep/1a715c55-bc31-46de-ae07-56dd4f403ce5?tab=ho-so-pl`.
- Khung thông báo xanh: **"Cập nhật hồ sơ thành công"**. Tiêu đề: **"Chi tiết DN #DN-XX-0005"**, thẻ đang mở **"Hồ sơ pháp lý"**.
- Bảng 2 dòng: `HSPL-20260803-0001` — *TKM hồ sơ pháp lý …* · Khác · Thuế · Thủ công · 03/08/2026 · 03/08/2026 · `Hiệu lự…`;
  `HSPL-20260731-0002` — *Hồ sơ x* · Giấy chứng nhận · Đất đai · Thủ công · 01/07/2026 · `–` · `Hiệu lự…`. Cột **Hành động: `Sửa` / `Xoá`**.
- Góc phải: `BTP · TW` · chuông `99+` · avatar `CU` · **"Cán bộ NV Trung ương  CB_NV_TW"**.
- Chân sidebar: **`HTPLDN · V1.0.3`**. Đồng hồ máy: **10:04 AM 2026-08-03**.

**② `partner-evidence/QLHSPLDN_07-2.webm`** — video VP9 **1920×1080, 17,2 giây**, 4.907.482 byte. MD5
`01a0aa6e…1895` **trùng** file cùng tên của tuần 3 ⇒ **cùng một video, không phải bằng chứng mới**.
Đã trích **17 khung mỗi 1 giây** vào `reverify-week-5/frames/QLHSPLDN_07/` và **mở đọc từng khung quyết định**:

| Mốc | Khung | Đọc được gì trên màn |
|---|---|---|
| **00:00** | `t000.00s.jpg` | Cửa sổ **"Sửa hồ sơ pháp lý"** đang mở, đã cuộn tới cuối. Các ô có sẵn dữ liệu: ngày `03/08/2026`, **Cơ quan cấp `TKM`**, **Trạng thái `Hiệu lực`**, **Mô tả `tkm kiểm thử chức năng`**. Mục **Tệp đính kèm**: vùng kéo-thả *"Tối đa 10 tệp. Định dạng: .pdf, .jpg, .png. Dung lượng tối đa: 20MB/tệp."* + **đúng 1 tệp** `2K15 T3 (4.8) & CN (9.8).pdf` **(258.2 KB)**. Đồng hồ **10:06 AM 2026-08-03** |
| **00:03** | `t003.07s.jpg` | Mục Tệp đính kèm nay có **2 tệp**: `2K15 T3 (4.8) & CN (9.8).pdf` (258.2 KB) + **`QLHSPLDN_07.jpg` (213.3 KB)** vừa thêm. **Các ô Cơ quan cấp / Trạng thái / Mô tả GIỮ NGUYÊN** giá trị cũ |
| **00:09** | `t009.22s.jpg` | Vẫn 2 tệp. Nút **`Đồng ý`** (không phải nhãn "Lưu") đang **quay vòng chờ** ⇒ đây là lúc bấm lưu |
| **00:11** | `t011.28s.jpg` | Cửa sổ đóng, quay về bảng. Khung thông báo xanh **"Cập nhật hồ sơ thành công"** |
| **00:12** | `t012.31s.jpg` | Mở lại **"Sửa hồ sơ pháp lý"** của **chính** `HSPL-20260803-0001` — đầu form: Tên `TKM hồ sơ pháp lý số 1`, Loại `Khác`, LVPL `Thuế`, Ngày cấp `03/08/2026`, Ngày hết hạn `03/08/2026`, Cơ quan cấp `TKM` ⇒ **vế (a) đạt trên chính bản dựng của đối tác** |
| **00:13** | `t013.33s.jpg` | **KHOẢNH KHẮC LỖI (sớm nhất).** Cuộn xuống mục Tệp đính kèm: **chỉ còn 1 tệp** `2K15 T3 (4.8) & CN (9.8).pdf` (258.2 KB). **`QLHSPLDN_07.jpg` đã biến mất.** Khung thông báo thành công vẫn đang mờ dần ở góc |
| **00:14 / 00:16** | `t014.36s.jpg` · `t016.42s.jpg` | Vẫn **1 tệp duy nhất**; nút `Hủy` / `Đồng ý` ở cuối form. Cơ quan cấp `TKM`, Trạng thái `Hiệu lực`, Mô tả `tkm kiểm thử chức năng` **không đổi so với 00:00** |

**Kết luận cổng bằng chứng:** ✅ ĐÓNG — đã thấy đúng khung chứa lỗi (`t013.33s.jpg`), đúng màn, đúng vai trò,
đúng mã case. **2 điều bắt buộc ghi lại:**

1. **Thay đổi duy nhất đối tác thực hiện là THÊM 1 TỆP.** Không có ô chữ / ngày / ô chọn nào bị sửa giữa
   00:00 và 00:13. ⇒ video **chỉ chứng minh** vế (b) hỏng ở **trường tệp đính kèm**, **không** chứng minh
   các kiểu trường khác hỏng, và cũng **không** loại trừ chúng.
2. **Cách đối tác kết luận "không lưu"** là **mở lại cửa sổ Sửa** của chính bản ghi vừa lưu — **không** tải
   lại trang, **không** đọc lại bản ghi từ máy chủ. Đây là đường đo yếu (có thể trúng bộ nhớ đệm phía trình
   duyệt), nên lượt đo của mình **phải mạnh hơn**, không được bắt chước đúng bằng ấy (§4).

---

## 2. Neo bằng chứng (tối đa 3, viết ra TRƯỚC khi hình thành giả thuyết)

| # | Neo | Giá trị đọc được từ bằng chứng đối tác |
|---|---|---|
| **N1** | URL / bản ghi | `htpldn-uat.ospgroup.vn/doanh-nghiep/1a715c55-bc31-46de-ae07-56dd4f403ce5?tab=ho-so-pl` — màn **Chi tiết DN #DN-XX-0005**, thẻ **Hồ sơ pháp lý**; bản ghi bị lỗi: **`HSPL-20260803-0001`** (*TKM hồ sơ pháp lý số 1*) |
| **N2** | Trạng thái entity + tiền đề | Loại **Khác** (`KHAC`) · LVPL **Thuế** · Nguồn **Thủ công** · Ngày cấp **03/08/2026** · Ngày hết hạn **03/08/2026** · Trạng thái **Hiệu lực** (`HIEU_LUC`). **Hồ sơ ĐÃ CÓ SẴN 1 tệp** trước thao tác. DN có 2 hồ sơ, cả hai `Hiệu lực` |
| **N3** | Vai trò + env/bản dựng | **`Cán bộ NV Trung ương  CB_NV_TW`**, phạm vi **`BTP · TW`**; env **`htpldn-uat.ospgroup.vn`**; bản dựng ghi trên màn **`HTPLDN · V1.0.3`**; đồng hồ máy **2026-08-03 10:04 → 10:06** |

---

## 3. Đặc tả nói gì

Nguồn: `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/` — **bản chốt duy nhất**. Mọi dòng dưới đây
đã **mở file đọc trực tiếp**, không dẫn theo trí nhớ.

### a) Màn đang tranh chấp — `srs-fr-07-doanh-nghiep.md`

- `:459` → *"**Mô tả:** Xem/chỉnh sửa chi tiết doanh nghiệp với 4 tab — Thông tin cơ bản (28 trường + auto-suggest quy mô NĐ80/2021), **Hồ sơ pháp lý DN (CRUD entity HO_SO_PHAP_LY_DN, 5 loại × 3 trạng thái)**, Lịch sử Hỗ trợ …"* — đây là `SCR-V.III-02`, đúng màn trong bằng chứng.
- `:461` → *"**Quyền truy cập:** Cán bộ nghiệp vụ (TW / Bộ ngành / Địa phương) có quyền CRUD doanh nghiệp. Phạm vi dữ liệu theo BR-AUTH-08 …"*
- `:468` → `| 2 | tab | Tab Hồ sơ PL doanh nghiệp (MỚI v2.1) | tab | CRUD hồ sơ pháp lý DN: GIAY_PHEP / HOP_DONG / GIAY_CN / QUYET_DINH / KHAC. Trạng thái: HIEU_LUC / HET_HAN / THU_HOI. Gộp từ MH-12.3 (Tư vấn CS) | — | Chỉ khi xem chi tiết |`
- `:160` → *"- **BR-DATA-05**: Ghi nhật ký thao tác"* (BR áp cho nhóm V.III).
- `:819-821` → *"### BR-DATA-05: Audit trail — **Mọi thao tác CUD + phê duyệt đều ghi vào AUDIT_LOG. Log là immutable.**"*

> **Cảnh báo dẫn nhầm màn:** `srs-fr-07-doanh-nghiep.md:523` ghi *"| 4 | tab | Tab 2 — Hồ sơ pháp lý DN | tab |
> **Read-only** danh sách HO_SO_PHAP_LY_DN | Luôn |"* — nhưng dòng đó thuộc **`SCR-V.III-04` "Hồ sơ doanh
> nghiệp của tôi"** (`:508`, `:514` — *"Quyền truy cập: Doanh nghiệp (Tier 2 VNeID) … Vai trò khác KHÔNG truy
> cập trang này"*). **CẤM dùng dòng :523 để chấm case này.**

### b) Chức năng Sửa/Cập nhật — `srs-fr-12-tv-chuyen-sau.md` (FR-X.1-04, nơi đặc tả xử lý thật sự)

`srs-fr-07` chỉ khai **màn**; phần **Processing / AC / audit** của chính tab này nằm ở FR-X.1-04
(`srs-fr-12-tv-chuyen-sau.md:547` ghi màn cũ `SCR-X1-03` **DEPRECATED v2.1 — chuyển sang tab trong MH-07.2
chi tiết DN**, tức tab ở `srs-fr-07:468`). Vì vậy phải dẫn cả hai file.

- `:541` → `### FR-X.1-04: Quản lý hồ sơ pháp lý doanh nghiệp (UC150)`
- `:550` → *"CRUD hồ sơ pháp lý doanh nghiệp: xem danh sách, xem chi tiết, thêm mới, **chỉnh sửa**, xóa mềm, tìm kiếm."*
- `:560` → `**Inputs (Dữ liệu đầu vào) -- Thêm mới / Chỉnh sửa:**` — 11 trường, trong đó:
  - `:566` `| 3 | ten_ho_so | text | Y | Tối đa 500 ký tự | — | người dùng nhập |`
  - `:567` `| 4 | loai_ho_so | text | Y | GIAY_PHEP / HOP_DONG / GIAY_CN / QUYET_DINH / KHAC | — | người dùng chọn |`
  - `:568` `| 5 | linh_vuc_id | identifier | N | FK -> DANH_MUC | — | người dùng chọn |`
  - `:569` / `:570` `ngay_cap` / `ngay_het_han | date | N`
  - `:571` `co_quan_cap | text | N` · `:572` `mo_ta | text (long) | N`
  - `:573` `| 10 | trang_thai | text | Y | HIEU_LUC / HET_HAN / THU_HOI | HIEU_LUC | người dùng chọn |`
  - `:574` → `| 11 | file_dinh_kem | file | N | PDF/image, max 20MB | — | người dùng upload |`
- `:607-614` → `**Chỉnh sửa:**` — bảng 4 bước:
  - `:611` `| 1 | Kiểm tra quyền và phạm vi đơn vị | BR-AUTH-01, BR-AUTH-08 |`
  - `:612` `| 2 | Xác nhận dữ liệu cập nhật | — |`
  - `:613` → `| 3 | **Cập nhật bản ghi hồ sơ** | — |`
  - `:614` → `| 4 | **Ghi nhật ký thao tác** | BR-DATA-05 |`
- `:674` → *"- Hồ sơ được tạo/**cập nhật**/xóa mềm trong CSDL"* (Postconditions)
- `:676` → *"- **AUDIT_LOG ghi nhận mọi thao tác CUD**"*
- `:695` → *"- **Given** CB NV chỉnh sửa hồ sơ **When** sửa thông tin + nhấn Lưu **Then** cập nhật bản ghi"*
- `:701` → *"- **Given** NHT cập nhật/đính kèm tài liệu hồ sơ **When** sửa nội dung + **upload file** + nhấn Lưu **Then** validate, **cập nhật**, **AUDIT_LOG ghi `nguoi_thuc_hien_id = user.id`** (NHT) …"* — dòng duy nhất nối thẳng *upload tệp khi Sửa* với *cập nhật* và *ghi audit*.
- `:693` → *"- **Given** CB NV xem chi tiết hồ sơ **When** chọn bản ghi **Then** hiển thị đầy đủ thông tin + **file đính kèm**"*; `:641-642` Processing Xem chi tiết: *"Truy vấn danh sách file đính kèm (FILE_DINH_KEM)"* → *"Trả kết quả bao gồm file đính kèm (tên, loại, dung lượng, URL preview)"*.
- `:1391-1419` → Entity `3.4.3.55 HO_SO_PHAP_LY_DN`, trong đó `:1413` `created_at`, **`:1414` `| 16 | updated_at | datetime | Y | DEFAULT NOW() | NOW() | Ngày cập nhật |`**, **`:1416` `| 18 | updated_by | identifier | N | FK → TAI_KHOAN(id) | — | Người cập nhật |`**, `:1417` `is_deleted`.
- `:682-688` Error Handling — 7 mã lỗi (`ERR-HSPL-01…06`, `INF-HSPL-01`), **KHÔNG có mã nào cho ca "lưu thất bại"**.

**Kiểm nhãn `[GAP-…]`:** trong FR-X.1-04 chỉ có 2 khối mang nhãn — `Processing — Xem chi tiết [GAP-X.1-05]`
(`:634`) và `Processing — Xuất Excel [GAP-X.1-05]` (`:644`). Khối **"Chỉnh sửa" (`:607`) và AC `:695` / `:701`
KHÔNG mang nhãn GAP** ⇒ yêu cầu của case này là **đã chốt**, không thuộc vùng đặc tả còn treo.

### c) Thông báo — `srs-v3.5.md`

- `:576` → `| UI-04 | Error display | Kiểm tra thời gian thực + viền đỏ + thông báo lỗi dưới ô nhập. Popup xác nhận trước xóa. **Toast notification cho thao tác thành công** | UX-Spec Section 4.2 |`
- `:582` → `| UI-10 | Báo lỗi mất kết nối | Khi thao tác lưu/gửi thất bại …: dừng trạng thái chờ (spinner), hiển thị thông báo "Lưu thất bại. Vui lòng kiểm tra kết nối và thử lại." kèm nút Thử lại; **KHÔNG nuốt lỗi trong im lặng**. Áp cho mọi module | UAT tuần 2 (TDHSTVV_09) |`

⇒ Đặc tả buộc **toast thành công phải gắn với thao tác thành công**; ca "lưu hỏng" phải hiện **lỗi**, không
được hiện thành công. Đây chính là loại sai **"đúng chữ sai loại"** mà flow 04 §Chạy bước 6 liệt kê.

### d) Bề mặt đọc nhật ký — `srs-fr-10-quan-tri.md`

- `:1365` → `### FR-VIII-28: Nhật ký hệ thống (MH-10.10) [GAP-VIII-02]`; `:1371` màn `SCR-VIII-10`.
- `:1373` → *"Tra cứu, lọc và xuất nhật ký thao tác toàn hệ thống (audit log). **Chỉ QTHT truy cập.** Dữ liệu read-only, không sửa/xóa."*
- `:1387` bộ lọc `module` có giá trị **`DN`**; `:1388` bộ lọc `hanh_dong` có giá trị **`Sửa`**.
- `:1405` Outputs: `thoi_gian, nguoi_dung, module, hanh_dong, chi_tiet, ip_address`.
- `:2423` → `| BR-DATA-05 | Mọi thao tác CUD + phê duyệt + đăng nhập/xuất đều ghi vào AUDIT_LOG. Immutable | NFR-06 | … |`

### IM LẶNG / cần lưu ý về đặc tả

1. **Nội dung chữ của thông báo thành công cho thao tác Sửa hồ sơ** — đặc tả **im lặng**. `srs-v3.5.md:576`
   chỉ đòi *có* toast; bảng chữ mẫu ở Phụ lục E.I.1 (`srs-v3.5.md:6728-6730`) chỉ phủ 4 tình huống công
   khai/hủy công khai/sai phạm vi/khóa lạc quan. ⇒ **KHÔNG chấm Fail vì chữ toast là "Cập nhật hồ sơ thành công"**.
2. **Bước upload/thay tệp trong Processing "Chỉnh sửa"** — bảng `:607-614` **không** có bước tương ứng với
   `:604` của "Thêm mới" (*"Upload file nếu có (max 20MB, quét virus) | EC-FILE-01"*). Nhưng Inputs `:560`
   ghi rõ áp cho **"Thêm mới / Chỉnh sửa"** và có `file_dinh_kem` (`:574`), còn AC `:701` nói thẳng
   *"upload file + nhấn Lưu → validate, cập nhật"*. ⇒ **KHÔNG im lặng ở mức yêu cầu**; đủ căn cứ chấm vế (b) cho tệp.
3. **Hành vi GỠ tệp khi Sửa** — đặc tả **im lặng hoàn toàn** (không dòng nào nói gỡ tệp lúc chỉnh sửa).
   ⇒ nếu đo thấy lệch ở chiều gỡ tệp: **ghi nhận + candidate cho BA**, **KHÔNG** kéo verdict case.
4. **Không có bề mặt nào (ngoài `SCR-VIII-10` của QTHT) để đọc lại AUDIT_LOG của 1 bản ghi HSPL.** Entity
   HO_SO_PHAP_LY_DN chỉ có `updated_at` / `updated_by` (`srs-fr-12:1414`, `:1416`) — đó là *dấu vết trên bản
   ghi*, **không phải** AUDIT_LOG mà `:676` đòi. Xử lý theo nhánh ở §4 vế (c).
5. **Không có cột `version`** trong entity HO_SO_PHAP_LY_DN ở cả 2 bản (`srs-fr-12:1391-1419` và bản rút gọn
   `srs-v3.5.md:3592-3614`, dòng `:3597` ghi *"Chi tiết xem: srs-fr-12-tv-chuyen-sau.md"*). Khóa lạc quan
   `version` chỉ được đặc tả cho HOI_DAP (`srs-fr-02:370`, `:379`). ⇒ `version 1→2` mà 2 vòng QA trước dùng
   làm bằng chứng là **chi tiết cài đặt**, dùng làm *đối chứng phụ* thì được, **không** được dùng làm tiêu chí Pass.
6. **Mâu thuẫn phạm vi đọc** giữa `srs-fr-12:675` (*"chỉ xem hồ sơ đơn vị mình"*) và `srs-fr-10:2381`
   (BR-AUTH-08: *"TW thấy toàn quốc"*) — đã ghi nhận ở vòng 1, **ngoài phạm vi case**, không kéo verdict.

---

## 4. Tiêu chí chấm

### Precondition bắt buộc trước khi được chấm

- **Tài khoản ra verdict:** `cbnv_tw_04` / `Test@1234` — vai trò **CB_NV_TW**, cấp **TW**, đơn vị *Cục Bổ trợ
  tư pháp – Bộ Tư pháp*, **trùng vai trò + cấp** đọc được trên bằng chứng (`Cán bộ NV Trung ương CB_NV_TW`,
  `BTP · TW`). Fallback theo Rule 7 **cùng vai trò + cùng cấp**: `cbnv_tw_05` → `cbnv_tw_02` → `cbnv_tw_01`;
  **cấm** đổi sang cấp BN/ĐP. **KHÔNG dùng `admin` để ra verdict** (chỉ dùng cho việc đọc `SCR-VIII-10` ở vế (c)
  và cho chuẩn bị dữ liệu — flow 04 §Chuẩn bị 1).
- **Bản ghi phải thuộc đơn vị TW.** Vòng 1 đã dính bẫy: `cbnv_tw_04` sửa hồ sơ của **Sở Tư pháp Hà Nội** →
  bị chặn **403 `ERR-AUTH-VPD-00-01`** *"Không có quyền truy cập dữ liệu đơn vị khác"*. Đây là **chặn theo đơn
  vị (`BR-AUTH-08`)**, KHÔNG phải lỗi lưu dữ liệu ⇒ nếu gặp lại thì **đổi bản ghi**, tuyệt đối **không** chấm Fail.
- **Bộ bắt thông báo:** bắt buộc dùng `tools/toast-capture.js`, cài **TRƯỚC** khi bấm, và tự kiểm
  **`soObserverDangSong = 1`** trước mỗi lượt đo; observer bị xoá sau mỗi lần tải lại trang → **cài lại + kiểm lại**.
  Đếm thông báo theo **mốc giờ khác nhau**, không theo số phần tử.
- **Cảnh báo dụng cụ (đã gãy 2 vòng trước, đọc lại trước khi đo):** đếm tệp phải dùng
  `.ant-upload-list-item-container` (KHÔNG phải `.ant-upload-list-item`); đọc ô chọn phải dùng
  `.ant-select-content` (KHÔNG phải `.ant-select-selection-item`); điền ô phải **đặt giá trị qua setter gốc +
  phát `input`/`change`** (`fill_form` / `Control+A` **nối chuỗi** thay vì thay thế); bộ đếm request phải bọc
  **cả `fetch` lẫn `XMLHttpRequest`** (vòng 2 báo `SO_REQUEST = 0` vì thiếu XHR).

---

**✅ PASS vế (a) — cửa sổ Sửa mở kèm dữ liệu hiện có — khi ĐỦ cả 2:**

1. Bấm `Sửa` trên 1 dòng hồ sơ → cửa sổ mở, **mọi ô đặc tả liệt kê ở `srs-fr-12:566-574` có dữ liệu trong bản
   ghi đều được điền sẵn đúng giá trị hiện có** — so từng ô với giá trị đọc lại từ máy chủ của chính bản ghi đó,
   **không** so với trí nhớ hay với dòng trong bảng.
2. Mục **Tệp đính kèm** liệt kê **đúng số tệp và đúng tên + dung lượng** mà bản ghi đang có (`srs-fr-12:693`,
   `:641-642`).

**❌ FAIL vế (a) nếu:** ≥1 ô có dữ liệu trong bản ghi nhưng ô trên form trống/khác giá trị, **hoặc** danh sách
tệp thiếu/thừa so với bản ghi.

---

**✅ PASS vế (b) — bấm Lưu thì bản ghi ĐƯỢC cập nhật — khi ĐỦ cả 5:**

1. **Thao tác bằng UI thật** (bấm nút `Đồng ý` trong cửa sổ Sửa). API/DB chỉ dùng để đối chứng, **không** thay
   thao tác. Cấm Pass bằng quan sát tĩnh kiểu *"thấy giá trị vẫn còn trên form"*.
2. **Đo bằng ĐƯỜNG THỨ HAI sau khi bấm Lưu** — bắt buộc **cả 2 đường độc lập, và cả 2 phải khớp**:
   - **(i) Tải lại trang thật** (bỏ bộ nhớ đệm) → mở lại chính bản ghi → so **từng trường vừa sửa**.
   - **(ii) Đọc lại bản ghi theo id từ máy chủ** → so **từng trường vừa sửa**, gồm **danh sách tệp đính kèm
     (tên + dung lượng)**. Đường gọi máy chủ **lấy từ chính request mà UI phát ra khi bấm Lưu**
     (`list_network_requests`), **CẤM tự đoán đường dẫn API**.
3. **Từng trường vừa sửa phải mang GIÁ TRỊ MỚI ở cả (i) và (ii)** — đối chiếu theo dấu nhận dạng duy nhất
   (vd `QA-W5-<HHmm>-<ten_o>`), không dùng giá trị dễ trùng.
4. **Số đo thông báo ↔ request khớp:** thao tác lưu phát ra request lưu và hiện **thông báo cùng loại với kết
   quả thật**. Cụ thể: request lưu **thành công** ⇒ được phép hiện toast thành công (`srs-v3.5.md:576`);
   request lưu **thất bại / bản ghi không đổi** mà vẫn hiện toast **thành công** ⇒ **FAIL** (`srs-v3.5.md:582`
   — *"KHÔNG nuốt lỗi trong im lặng"*).
5. **Phủ đủ M = 5 dạng ở §5**, mỗi dạng đều qua đủ bước 1-4.

**❌ FAIL vế (b) nếu:** ≥1 trường vừa sửa (kể cả **tệp vừa thêm**) **không** mang giá trị mới ở (i) **hoặc** (ii);
**hoặc** hệ thống hiện thông báo thành công trong khi bản ghi không đổi; **hoặc** (i) và (ii) **mâu thuẫn nhau**
(⇒ **CHƯA được chốt**: ghi cả hai số đo, hỏi user — flow 04 §Chạy bước 8).
**Đúng một phần cũng là FAIL:** chỉ cần 1 trong 5 dạng ở §5 mất dữ liệu ⇒ vế (b) FAIL, dù 4 dạng kia lưu đủ.

---

**✅ PASS vế (c) — lưu vết thao tác — theo cây quyết định (đo theo thứ tự, KHÔNG bỏ bước):**

- **Đường A (đóng vế của ĐẶC TẢ `srs-fr-12:614` + `:676`):** đăng nhập **QTHT (`admin`)** → mở
  `SCR-VIII-10` **Nhật ký hệ thống** (`srs-fr-10:1365`, `:1371`, `:1373`) → lọc `module = DN` (`:1387`),
  `hanh_dong = Sửa` (`:1388`), khoảng thời gian bao trùm giây bấm → **có dòng log ứng đúng thao tác vừa làm**
  (`thoi_gian` = giây bấm ± sai số hiển thị, `nguoi_dung` = tài khoản đã bấm, `chi_tiet` trỏ đúng bản ghi HSPL).
  **Việc đọc log bằng QTHT là ĐỐI CHỨNG, không phải hành động đang tranh chấp** — thao tác Sửa vẫn phải do
  `cbnv_tw_04` thực hiện.
- **Đường B (đóng vế của PHIẾU — chỉ dùng khi Đường A không khả dụng):** đọc lại bản ghi từ máy chủ thấy
  **`updated_at` = đúng giây bấm** và **`updated_by` = đúng tài khoản đã bấm** (`srs-fr-12:1414`, `:1416`).
- **Chấm:**
  - Đường A đạt ⇒ **vế (c) PASS** (đóng cả yêu cầu đặc tả lẫn yêu cầu phiếu).
  - Đường A **không khả dụng** (màn `SCR-VIII-10` chưa có / không mở được bằng QTHT / không có mục `module = DN`)
    **nhưng Đường B đạt** ⇒ **vế (c) PASS theo phạm vi phiếu**, đồng thời **mở 1 dòng candidate riêng** về
    `FR-VIII-28` / `srs-fr-12:676` và **ghi rõ trong verdict là chưa chứng minh được AUDIT_LOG**.
    **KHÔNG** kéo verdict case (flow 04 §Bug mới, mục 6).
  - Đường A có màn nhưng **không có dòng log** cho thao tác vừa làm, dù Đường B đạt ⇒ **KHÔNG Pass vế (c)**;
    đây là sai lệch trực tiếp với `:614` + `:676` ⇒ báo là **vế còn lỗi**.
  - **Cả A lẫn B đều không lấy được số đo** ⇒ vế (c) **CHƯA ĐO ĐƯỢC** ⇒ **không Pass**, ghi rõ thiếu gì.

**❌ FAIL vế (c) nếu:** bản ghi được cập nhật nhưng `updated_by` **không phải** người vừa thao tác, **hoặc**
`updated_at` không đổi, **hoặc** có màn nhật ký mà thao tác Sửa không để lại dòng log nào.

---

**Chốt verdict cả case** (flow 04 §Ca biên — case gộp nhiều vế):
**Pass** khi (a) + (b) + (c) đều đạt · **Reopen** khi còn ≥1 vế lỗi · **cần BA** khi không vế nào lỗi nhưng
còn vế phải chờ BA · **ô trống** khi điều kiện quyết định chưa đo được.
🔴 **Không có ảnh "lỗi cũ" do chính mình chụp trên bản dựng trước** ⇒ chỉ được kết luận **hiện trạng đúng/sai so
với đặc tả**, **CẤM viết** *"fix đã có tác dụng"* (flow 04 §Ca biên).
🔴 **Pass ở env nội bộ chỉ là Pass tạm** cho tới khi bản dựng này lên env đối tác — phải nói rõ trong verdict.

### KHÔNG được chấm Fail vì

- **Nhãn nút là `Đồng ý` thay vì `Lưu`** (đặc tả `srs-fr-07:496` ghi nút *"Lưu"*). Đây là quy ước UI toàn hệ
  thống của bản dựng, **không** thuộc vế đối tác nêu; nếu muốn thì log candidate riêng.
- **Chữ của thông báo thành công** (*"Cập nhật hồ sơ thành công"*) — đặc tả im lặng về nội dung (§3 mục IM LẶNG 1).
  Chỉ FAIL khi **sai LOẠI** (báo thành công lúc không lưu được), không FAIL vì chọn chữ nào.
- **`version` không tăng / không có trường `version`** — entity không đặc tả cột này (§3 mục IM LẶNG 5).
- **403 `ERR-AUTH-VPD-00-01` khi sửa hồ sơ của đơn vị khác** — đúng `BR-AUTH-08`; đổi bản ghi rồi đo lại.
- **Nút `Sửa` vẫn hiện trên dòng hồ sơ của đơn vị khác** — quan sát ngoài phạm vi đã ghi từ vòng 1, đang vướng
  mâu thuẫn `srs-fr-12:675` vs `srs-fr-10:2381` (§3 mục IM LẶNG 6). Candidate cho BA, **không** kéo verdict.
- **Hành vi khi GỠ tệp lúc Sửa** — đặc tả im lặng (§3 mục IM LẶNG 3).
- **Số hồ sơ / dữ liệu trên env nội bộ khác env đối tác** — lệch env là **giới hạn hiệu lực**, không phải lỗi.

### KHÔNG được chấm Pass vì (chống Pass oan — case này là bug "báo thành công nhưng KHÔNG lưu")

- ❌ Thấy **thông báo "Cập nhật hồ sơ thành công"** → đây chính là thứ đã nói dối trong video đối tác.
- ❌ Thấy **giá trị vẫn còn trên form ngay sau khi lưu** (form chưa đóng, hoặc mở lại form mà **không** tải lại
   trang) → đúng đường đo yếu của đối tác, có thể trúng trạng thái trong bộ nhớ trình duyệt.
- ❌ Thấy **dòng trong bảng danh sách đổi** mà chưa tải lại trang → cùng nguồn dữ liệu trong bộ nhớ.
- ❌ Chỉ đo **một** trong hai đường (i)/(ii) ở vế (b) — **bấm lại cùng một nút không tính là đường thứ hai**.
- ❌ Kết luận 100% từ script chạy trong trang mà **không có ảnh mở ra đọc** (flow 04 §Dấu hiệu phép đo nói dối).
- ❌ Suy từ số đo của vòng 1 / vòng 2 (bản `V1.0.5`) sang bản dựng lần này.

---

## 5. Dạng dữ liệu phải phủ — **M = 5**

Bug này là bug về **ghi dữ liệu xuống bản ghi**, mỗi *kiểu ô* là một đường ghi khác nhau nên M bắt buộc ≥ 2.
Nguồn xác định M: bảng **Inputs "Thêm mới / Chỉnh sửa"** `srs-fr-12:560-574` (11 trường, 6 kiểu logic) +
tiền đề đọc được trên bằng chứng (N2).

| # | Dạng | Vì sao là một dạng riêng | Vế nào cần |
|---|---|---|---|
| **D1** | **CHỈ thêm 1 tệp** vào hồ sơ **đã có sẵn ≥1 tệp**, **không đụng ô nào khác**, rồi bấm `Đồng ý` | **Bản sao chính xác thao tác đối tác** (00:00 → 00:13). Đường lưu tệp khi *không có ô nào bẩn* có thể khác đường lưu khi *có ô bẩn* — **cả 2 vòng QA trước đều KHÔNG đo dạng này** (luôn sửa 8-9 ô rồi mới thêm tệp) | (b) (c) |
| **D2** | Ô **chữ** + **chữ dài**: `ten_ho_so` (`:566`), `co_quan_cap` (`:571`), `mo_ta` (`:572`) | 3 trường text, trong đó `mo_ta` là `text (long)` — kiểu lưu khác | (b) |
| **D3** | Ô **ngày**: `ngay_cap` (`:569`), `ngay_het_han` (`:570`) | Kiểu `date` — hay hỏng riêng do định dạng/múi giờ; đối tác **không** đụng nên video không loại trừ được | (b) |
| **D4** | Ô **chọn**: `loai_ho_so` 5 giá trị (`:567`), `linh_vuc_id` FK → DANH_MUC (`:568`), `trang_thai` 3 giá trị (`:573`) | Enum + khóa ngoại — đường ghi khác text; `:468` khai đủ 5 loại × 3 trạng thái | (b) |
| **D5** | **Bản ghi MỚI tạo qua luồng chuẩn sau bản vá** vs **bản ghi CŨ có sẵn từ trước** (ưu tiên bản ghi cũ **đã có sẵn tệp**, đúng tiền đề N2) | Flow 04 §Ca biên: *bug về trường lưu trong CSDL phải đo trên bản ghi mới sau fix*; đồng thời phải giữ 1 bản ghi cũ để loại giả thuyết "dữ liệu cũ đóng băng" | (b) (c) |

**Cách ghép cho tiết kiệm mà không mất độ phủ:** mỗi lượt đo là **1 lần bấm `Đồng ý`**.
- **Lượt 1 = D1 trên bản ghi CŨ có sẵn tệp** (thao tác y hệt đối tác). ← **lượt quyết định**
- **Lượt 2 = D2+D3+D4 + thêm 1 tệp, cùng 1 lần bấm, trên bản ghi CŨ**.
- **Lượt 3 = tạo bản ghi MỚI (D5) → lặp lại D1 → rồi lặp lại lượt 2** trên chính bản ghi mới.

**Nếu env thiếu tiền đề "hồ sơ thuộc đơn vị TW **và** đã có sẵn ≥1 tệp" → được SEED**, nhưng phải khai vào báo
cáo: **đổi/tạo bản ghi nào · đổi gì · trên env nào** (flow 04 §Chuẩn bị 4). Seed phải làm bằng **UI thật**;
nếu buộc phải gọi máy chủ thì đường gọi **lấy từ request UI phát ra**, **cấm đoán đường dẫn, cấm ghi thẳng CSDL**.
**Tuyệt đối không đụng dữ liệu của đối tác** (`DN-XX-0005`, `HSPL-20260803-0001` nằm trên env nghiệm thu — env
nội bộ có thể có bản ghi trùng tên, phải kiểm id trước khi sửa).

---

## 6. Bảng điều kiện

| Điều kiện có thể đổi kết quả | Đối tác | Mình test lần này | GAP? |
|---|---|---|:-:|
| **Vai trò** / tài khoản | Badge góc phải: **"Cán bộ NV Trung ương  CB_NV_TW"**, phạm vi **`BTP · TW`** (đọc được trên cả ảnh tĩnh và mọi khung video) | **`cbnv_tw_04`** — vai trò `CB_NV_TW`, cấp TW, đơn vị *Cục Bổ trợ tư pháp – Bộ Tư pháp*. Fallback Rule 7 **cùng vai trò + cùng cấp**: `cbnv_tw_05` → `cbnv_tw_02` → `cbnv_tw_01`. `admin` (QTHT) **chỉ** để đọc `SCR-VIII-10` ở vế (c), không ra verdict | **Không** — GAP nếu buộc phải đổi sang cấp BN/ĐP hoặc ra verdict bằng `admin` |
| **Entity** + trạng thái | `HO_SO_PHAP_LY_DN` — `HSPL-20260803-0001`, loại **Khác** (`KHAC`), LVPL **Thuế**, nguồn **Thủ công**, trạng thái **Hiệu lực** (`HIEU_LUC`); DN có 2 hồ sơ, cả hai `Hiệu lực` | Cùng entity, trên màn `/doanh-nghiep/:id?tab=ho-so-pl` (`SCR-V.III-02`). Bắt đầu từ bản ghi **`HIEU_LUC` + loại `KHAC`** cho khớp đối tác, sau đó D4 phủ thêm các giá trị `loai_ho_so` / `trang_thai` khác theo `srs-fr-07:468` | **Không** — GAP nếu env không có bản ghi `HIEU_LUC` thuộc đơn vị TW (khi đó phải seed và khai rõ) |
| Dữ liệu **tiền đề** | Hồ sơ **ĐÃ CÓ SẴN đúng 1 tệp** `2K15 T3 (4.8) & CN (9.8).pdf` (258.2 KB) trước thao tác; bản ghi tạo cùng ngày quay, thuộc đúng đơn vị người thao tác | Bắt buộc có **≥1 hồ sơ thuộc đơn vị TW đã có sẵn ≥1 tệp** (khớp tiền đề) **và** **1 hồ sơ mới tạo sau bản vá** (D5). Thiếu → **seed bằng UI thật + khai đổi gì/ở đâu** | **Không** — GAP nếu chỉ đo được hồ sơ **chưa có tệp nào** (khác tiền đề đối tác) hoặc chỉ đo được bản ghi cũ, không dựng được bản ghi mới |
| Input / **filter** / giá trị nhập | **Chỉ thay đổi 1 thứ duy nhất: thêm tệp `QLHSPLDN_07.jpg` (213.3 KB)**. Không lọc, không tìm kiếm; bảng hồ sơ 2 dòng, phân trang trang `1` | **Lượt 1 lặp đúng như vậy (D1)**; lượt 2-3 phủ thêm D2+D3+D4 trong **cùng 1 lần bấm**. Không đặt bộ lọc nào trên tab Hồ sơ pháp lý (giữ nguyên như đối tác). Giá trị nhập mang dấu nhận dạng `QA-W5-<HHmm>-<ten_o>` để không nhầm với dữ liệu cũ | **Không** — GAP nếu bỏ lượt D1 (chỉ đo kịch bản "sửa nhiều ô + thêm tệp" như 2 vòng trước) |
| **Độ phủ** biến thể (N bản ghi, M dạng) | N = **1 bản ghi**, **1 lần bấm Lưu**, M = **1 dạng** (chỉ trường tệp đính kèm); 1 vai trò; đo bằng **1 đường duy nhất** (mở lại form, không tải lại trang) | N ≥ **2 bản ghi** (1 cũ có sẵn tệp + 1 mới tạo sau bản vá) × **3 lượt bấm Lưu**/bản ghi; M = **5 dạng** (D1 tệp-đơn-lẻ · D2 chữ + chữ dài · D3 ngày · D4 ô chọn/enum/FK · D5 bản ghi mới vs cũ); mỗi lượt đo bằng **2 đường độc lập** (tải lại trang + đọc lại bản ghi từ máy chủ) + ảnh mở ra đọc | **Không** — GAP nếu bỏ bớt bất kỳ dạng nào trong D1-D5, **hoặc** chỉ đo 1 đường thay vì 2 |

**Ghi chú giới hạn (KHÔNG phải GAP):** đối tác đo trên env nghiệm thu `htpldn-uat.ospgroup.vn` bản
**`HTPLDN · V1.0.3`** (đọc ở chân sidebar cả ảnh lẫn video, 03/08/2026); mình đo trên env **nội bộ**
`18.143.165.120.nip.io` bản ghi ở §7. **Lệch env + lệch bản dựng ⇒ giới hạn hiệu lực của verdict**, phải ghi
rõ, nhưng **không tự động chặn kết luận** (flow 04 §Kiểm chênh điều kiện).

**Ghi chú về bằng chứng (KHÔNG phải GAP):** cả 2 tệp bằng chứng tuần 5 **trùng băm MD5** với bằng chứng tuần 3
(`QLHSPLDN_07-1.webm` ≡ `QLHSPLDN_07-1.jpg`, `QLHSPLDN_07-2.webm` ≡ file cùng tên tuần 3) ⇒ **đối tác chưa gửi
bằng chứng mới sau lần dev báo Fixed**. Vẫn phải tự đo lại đầy đủ; **không** được lấy việc "bằng chứng cũ" làm
lý do rút gọn phép đo, cũng **không** được coi đó là dấu hiệu đối tác đã hết lỗi.

---

## 7. Bản dựng đã đo (điền NGAY TRƯỚC khi bấm nút đầu tiên, sau khi tải lại trang thật)

> Tab mở lâu vẫn chạy bản dựng cũ — đã có tiền lệ Reopen oan. **Bắt buộc tải lại trang rồi mới đo.**
> Ghi **dấu vân tay**, không chỉ chuỗi phiên bản: dự án đã có lần deploy lại mà **giữ nguyên** số `V1.0.x`.

| Hạng mục | Giá trị đo được |
|---|---|
| Thời điểm đo (giờ VN) | **06/08/2026 19:05 → 19:24** (5 lần bấm lưu/tạo: 19:05:18 · 19:09:45 · 19:12:03 · 19:16:57 · 19:22:13) |
| Môi trường | `https://18.143.165.120.nip.io` — env **NỘI BỘ** |
| Chuỗi phiên bản trên màn (chân sidebar) | `HTPLDN · V1.0.8` |
| Bó mã FE (`/assets/index-*.js` + `*.css`) | `assets/index-DIABnbIr.js` · `assets/index-DVlgOkLg.css` |
| `GET /` → `last-modified` | `Thu, 06 Aug 2026 07:13:15 GMT` |
| `GET /` → `etag` | `W/"6a74340b-428"` (đo lại lúc 19:24 sau lượt cuối — **không đổi giữa đợt**) |
| Tài khoản đã dùng ra verdict | **`cbnv_tw` / `Test@1234`** — KHÔNG phải `cbnv_tw_04` như §4 gợi ý. Lý do: phiên đang mở của lô này đăng nhập bằng `cbnv_tw`; đã kiểm `/api/v1/auth/me` + đối chiếu dòng nhật ký (`Người dùng` = *CB Nghiệp vụ - Trung ương*, `Đơn vị` = *Cục Bổ trợ tư pháp - Bộ Tư pháp*) ⇒ **trùng vai trò `CB_NV_TW` + trùng cấp TW + trùng đơn vị** với tài khoản gợi ý ⇒ không tạo GAP ở bảng §6 dòng "Vai trò". Không dùng `admin` để ra verdict |
| Tài khoản phụ (chỉ đọc nhật ký vế (c)) | **`admin` (QTHT)** — chỉ mở `SCR-VIII-10` để đọc, không thao tác dữ liệu |
| Bản ghi đã dùng / đã seed | **(1) CŨ** `HSPL-20260803-0001` id `5bd8169a-0997-493b-8503-ddfcc7d5830a` — DN `DN-HNI-0001` (`829abcac-…014c`), đơn vị TW `00000000-0000-4000-8000-000000000001`, **có sẵn từ trước** + đã có sẵn tệp ⇒ lượt 1 (D1) + lượt 2 (D2+D3+D4). **(2) MỚI** `HSPL-20260806-0001` id `11a5f733-58ce-4ed2-b898-6580a259b612` — **tạo trong phiên** lúc 19:12:03 bằng UI thật (nút *Thêm hồ sơ*), cùng DN + cùng đơn vị TW ⇒ lượt 3a (D1 trên bản ghi mới) + lượt 3b (D2+D3+D4). Tệp seed: `QA-W5-1907-tep-luot1…luot5.png` (PNG thật, 73–99 B, thư mục `reverify-week-5/seed-files/`) |
| Đối chiếu với bản dựng B7 cùng ngày | **TRÙNG** — cùng `index-DIABnbIr.js`, cùng `last-modified Thu, 06 Aug 2026 07:13:15 GMT`, cùng `etag W/"6a74340b-428"` ⇒ FE **không** deploy lại giữa lô B7 và lượt đo này |

**Nếu bản dựng đổi giữa đợt đo** → ghi rõ trong verdict và **đo lại từ lượt 1** (flow 04 §Dấu hiệu phép đo nói dối).
