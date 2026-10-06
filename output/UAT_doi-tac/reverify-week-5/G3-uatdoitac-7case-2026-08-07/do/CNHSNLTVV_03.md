# NHẬT KÝ ĐO — CNHSNLTVV_03 (dòng 36) · Lô G3 · env nghiệm thu đối tác

> Phạm vi user chốt (BRIEF §3b): **chỉ verify triệu chứng gốc** — bấm Lưu với dữ liệu hợp lệ
> **có đính tệp chứng chỉ** thì hệ thống còn báo *"Lỗi hệ thống, vui lòng thử lại sau."* không.
> Bỏ: các nhánh phụ · hiển thị tên tệp ở tab khác · tác dụng phụ trạng thái · nhiều hồ sơ / nhiều kiểu tên tệp.

## 1. Bảng đầu

| Mục | Giá trị |
|---|---|
| Env | `https://htpldn-uat.ospgroup.vn` (env NGHIỆM THU của đối tác) |
| **Bản dựng đọc trên UI** | **`HTPLDN · V1.0.10`** (chân sidebar, sau `reload ignoreCache=true`) · bó mã FE `assets/index-Bd1akG3f.js` |
| Ngày giờ đo | 2026-08-07, 18:44–19:00 giờ VN (11:44–12:00 UTC) |
| Tài khoản | `nht_04_ui` / `Test@1234` — `/auth/me` trả `vaiTro=["NHT"]`, `donViId=00000000-0000-4000-8000-000000000001`, `capDonVi=TW`, `hoTen="NHT UI Test 04"` |
| Vai trò theo đặc tả | **Người hỗ trợ pháp lý (NHT)** — `srs-fr-04-chuyen-gia-tvv.md:375` *"**Tác nhân:** Người hỗ trợ pháp lý (NHT)"*; tiền đề cùng đơn vị `:377`; điều kiện hiện tab Năng lực `:1576` |
| Hồ sơ đã đo | **`TVV-BTP-TW-0063`** — "Tester TKM BTP-TW", loại **TVV**, trạng thái **`HOAT_DONG`**, `id=789d5f7e-ecf2-44d1-92e0-e3bfe1805a3a` |
| Màn | `/chuyen-gia-tvv/danh-sach` (`:1418`) → `/chuyen-gia-tvv/789d5f7e-…` (`:1537`) → tab **Năng lực** → **[Cập nhật năng lực]** |
| Số lượt đăng nhập | **1** (`nht_04_ui`). Phiên **KHÔNG** bị thu hồi giữa chừng (cảnh báo N10 không xảy ra trong lượt này) |
| Console | 1 cảnh báo `/ticket=*` (không liên quan) + 1 lỗi tải tài nguyên **422** — chính là 2 lời gọi 422 do tôi chủ động tạo (lượt Lưu #1 và bước thử khôi phục). Không có lỗi nào khác. |

## 2. Mô tả ảnh đối tác (đã mở xem lại full-res)

`batch-B7-tuvan-mangluoi-2026-08-06/partner-evidence/CNHSNLTVV_03.jpg` — 1 ảnh tĩnh:

- Thanh địa chỉ `htpldn-uat.ospgroup.vn/chuyen-gia-tvv/b88271a7-34a4-4c43-9133-71342ba73d3e`; breadcrumb `Trang chủ / Mạng lưới Tư vấn viên / Chi tiết`.
- **Khung đỏ giữa trên: "Lỗi hệ thống, vui lòng thử lại sau."** — trùng khít ô *Kết quả thực tế*.
- Đang mở form *Cập nhật năng lực*: khối `Lĩnh vực pháp luật` 9 thẻ (Thuế · Lao động · Đất đai · Dân sự · Thương mại · Hành chính · Sở hữu trí tuệ · Doanh nghiệp · Đầu tư); `Chứng chỉ hiện có` → **"Chưa có chứng chỉ nào."**; vùng kéo thả *"Thêm chứng chỉ mới (PDF, tối đa 10 file)"*.
- **Hàng tệp đang đính: `2K15 T3 (4.8) & CN (9.8).pdf` — `(258.2 KB)`** + 2 điều khiển `Xem` / `Xóa`.
- `Ghi chú cập nhật` = `a` (`1 / 2000`); cuối form 2 nút `Làm lại` · **`Lưu`**.
- Góc phải trên `BTP · DP` · chuông 4 · **`hương 3 NHT`** · huy hiệu `NHT`. Chân sidebar **`HTPLDN · V1.0.3`**. Đồng hồ máy `03:42 PM · 2026-08-03`.

**Khác biệt đã khai:** đối tác đứng ở đơn vị `BTP · DP`; env chỉ cấp cho QA tài khoản NHT cấp **TW** ⇒ đo **cùng vai trò NHT, khác cấp đơn vị**, và chọn hồ sơ TVV **cùng đơn vị** với `nht_04_ui` theo ràng buộc `:377` / `:1576`.

## 3. Bản sao lưu giá trị gốc (đọc TRƯỚC khi sửa)

`GET /api/v1/tu-van-viens/789d5f7e-…` → HTTP 200. JSON đầy đủ lưu ở
[`seed-files/CNHSNLTVV_03-ban-sao-luu-goc-TVV-BTP-TW-0063.json`](../seed-files/CNHSNLTVV_03-ban-sao-luu-goc-TVV-BTP-TW-0063.json).

| Trường | Giá trị gốc |
|---|---|
| `version` | **14** · `hoSo.version` **3** |
| `trangThai` | `HOAT_DONG` |
| `trinhDo` | `Cử nhân` |
| `soNamKinhNghiem` | `1` |
| `chuyenNganh` | `Luật hành chính` |
| `soTheHanhNghe` | **`null`** |
| `chungChiHanhNghe` · `moTaKinhNghiem` · `ghiChu` | `null` |
| `hoSo.bangCapChiTiet` · `hoSo.chungChiChiTiet` | `[]` · `[]` |
| `linhVucIds` | `…018 (Thuế)` · `…013 (Lao động)` · `…014 (Đất đai)` |
| `fileDinhKems` | **1 tệp** — `2K15 T3 (4.8) & CN (9.8).pdf` (`313ebe1d-…`, 264 361 B) — đồng thời là `fileTheHanhNgheId` |

## 4. Tệp đã chuẩn bị và đính (B1)

`seed-files/QA G3 (4.8) & CN (9.8).pdf` — PDF 1.4 hợp lệ, 1 trang, **672 byte**.
Tên tệp cố ý mang **dấu cách + ngoặc đơn + dấu `&`** giống hệt kiểu tên trong ảnh đối tác.

## 5. Sự cố tiền đề đã xử lý trước khi đo

### 5.1 Cổng bắt buộc nhập số CCCD chặn toàn bộ giao diện (mới, chưa từng ghi nhận)

Ngay sau khi đăng nhập, hộp thoại **"Cập nhật thông tin bắt buộc"** phủ mặt nạ toàn màn:
*"Theo quy định mới, bạn cần cung cấp số Căn cước công dân (CCCD) để tiếp tục sử dụng hệ thống.
Thông tin này chỉ được yêu cầu một lần."* — **không có nút đóng / huỷ, phím `Escape` không tắt**
(rà DOM: `.ant-modal` chỉ có 1 nút `Xác nhận`, không có `.ant-modal-close`). `/auth/me` trả `cccd: null`.

⇒ Không thể tới màn cần đo nếu không hoàn tất bước này. Đã **nhập số tổng hợp rõ ràng là dữ liệu
kiểm thử `000000000004`** qua đúng hộp thoại (`PATCH /api/v1/auth/me/cccd` → **200**), hộp thoại tắt,
`/auth/me` trả `cccd:"000000000004"`. **Đây là thay đổi trên TÀI KHOẢN QA, không phải trên hồ sơ đo.**
Lược đồ `UpdateMeCccdDto` bắt buộc đúng 12 chữ số ⇒ **không có đường trả về `null`**.
Ảnh: `image/CNHSNLTVV_03-00-modal-cccd-bat-buoc.png`.

### 5.2 Ô lọc màn danh sách

Vào `/chuyen-gia-tvv/danh-sach` ô lọc đã sạch (`Tất cả` · `Đơn vị quản lý` trống · `Tổ chức` trống —
kiểm bằng bộ chọn đã cải chính `.ant-select-content-has-value` + `title`). Vẫn bấm **"Xóa bộ lọc"**
theo trình tự → tab mặc định *Đang hoạt động*, chân bảng **`1-11 / 11 mục`**.

### 5.3 Lượt dựng cảnh đầu bị mất trạng thái form (đã dựng lại)

Lần dựng cảnh đầu tiên: đính tệp xong form còn nguyên, nhưng sau thao tác kế thì giao diện **tự nhảy
về tab "Hồ sơ"**, mất toàn bộ form đang nhập (chưa hề bấm Lưu). Đã dựng lại từ đầu và đổi trình tự
(đính tệp trước → lấy uid mới → nhập ghi chú → cài bộ bắt thông báo → bấm Lưu), tránh chụp ảnh
toàn trang trong lúc form đang mở. **Hệ quả dữ liệu:** lượt hỏng đó vẫn để lại 1 tệp trên hồ sơ
(xem §9) — đúng bẫy (j) của chuẩn chấm.

## 6. Cảnh đã dựng lại (B2–B4) — khớp neo bắt buộc của ảnh đối tác

| Neo (chuẩn chấm §3) | Trạng thái khi bấm Lưu |
|---|---|
| 1. Vai trò NHT | ✅ `/auth/me` → `vaiTro=["NHT"]` |
| 2. Form *Cập nhật năng lực* của SCR-IV-03 (không phải màn Sửa hồ sơ) | ✅ tab **Năng lực** → nút **[Cập nhật năng lực]** mở form inline |
| 3. **≥1 tệp chứng chỉ mới đang đính** | ✅ hàng `QA G3 (4.8) & CN (9.8).pdf (672 B)` + `Xem` / `Xóa` |
| 4. Có nhập `Ghi chú cập nhật` | ✅ `G3 CNHSNLTVV03 2026-08-07` (`25 / 2000`) |
| 5. Khối `Chứng chỉ hiện có` đang rỗng | ✅ **"Chưa có chứng chỉ nào."** |

Ảnh: `image/CNHSNLTVV_03-01-truoc-khi-sua.png` · `image/CNHSNLTVV_03-02-da-dinh-tep.png` (**đã mở đọc cả 2**).

**B3 — mở form:** [Cập nhật năng lực] mở được ngay tại chỗ, **không** bị đẩy sang trang báo không có quyền.

## 7. PHÉP ĐO QUYẾT ĐỊNH (B5) — bấm [Lưu]

Bộ bắt thông báo: **dùng nguyên `output/UAT_doi-tac/tools/toast-capture.js`** (không lọc trùng, đọc
bằng `innerText`, đếm kèm số lời gọi ghi). **Tự kiểm trước mỗi lượt: `soObserverDangSong = 1`** (hợp lệ).

### Lượt 1 — dữ liệu đúng như hồ sơ đang có (số thẻ hành nghề để trống)

| Số đo | Giá trị |
|---|---|
| Số lời gọi ghi | **1** — `PATCH /api/v1/tu-van-viens/789d5f7e-…/nang-luc` (1 bấm = 1 request) |
| **Số khung thông báo** | **1** · `BI_LAP=false` |
| **Nguyên văn thông báo** | **"Số thẻ hành nghề là bắt buộc đối với Tư vấn viên"** |
| **Mã phản hồi** | **HTTP 422** |
| **Thân phản hồi** | `{"success":false,"error":{"code":"ERR-VAL-IV-03-10","message":"Số thẻ hành nghề là bắt buộc đối với Tư vấn viên","field":"soTheHanhNghe","requestId":"ddd11f40-…"}}` |
| Thân yêu cầu | `{"trinhDo":"Cử nhân","soNamKinhNghiem":1,"chuyenNganh":"Luật hành chính","bangCapChiTiet":[],"chungChiChiTiet":[],"chungChiMoiIds":["99b9a7e5-…"],"linhVucIds":[…3 mục…],"ghiChuCapNhat":"G3 CNHSNLTVV03 2026-08-07","version":14}` |

⇒ **KHÔNG phải triệu chứng của phiếu.** Đây là lời từ chối nghiệp vụ có căn cứ đặc tả:
`srs-fr-04-chuyen-gia-tvv.md:1507` — *"| 3.5 | nhóm 2 | Số thẻ hành nghề | ô văn bản | **Bắt buộc nếu
Loại = Tư vấn viên** (theo NĐ 77/2008 Đ.20) | — |"*. Hồ sơ đo là loại **TVV** và `soTheHanhNghe` đang
`null` (dữ liệu cũ vi phạm chính quy tắc này) ⇒ **dữ liệu tôi gửi CHƯA hợp lệ**.
Theo chuẩn chấm §8 (*"hệ thống từ chối do QA nhập sai tiền đề → sửa tiền đề rồi đo lại"*) → **sửa dữ liệu, đo lại**.
Ảnh: `image/CNHSNLTVV_03-03-sau-khi-bam-luu.png` (bắt đúng lúc nút Lưu đang xử lý; **thông báo tự tắt
nhanh nên lấy thân phản hồi làm bằng chứng chính** — chuẩn chấm §7b, **không bấm lại chỉ để chụp lại**).

### Lượt 2 — dữ liệu hợp lệ đầy đủ (bổ sung Số thẻ hành nghề), **giữ nguyên tệp đang đính**

| Số đo | Giá trị |
|---|---|
| Số lời gọi ghi | **1** — `PATCH …/nang-luc` (1 bấm = 1 request) |
| **Số khung thông báo** | **1** · `BI_LAP=false` |
| **Nguyên văn thông báo** | **"Cập nhật năng lực thành công"** |
| **🔴 Có câu "Lỗi hệ thống, vui lòng thử lại sau." không?** | **KHÔNG — 0 lần, ở CẢ 2 lượt bấm** |
| **Mã phản hồi** | **HTTP 200** |
| **Thân phản hồi** | `{"success":true,"data":{…,"version":15,"soTheHanhNghe":"QA-G3-20260807","ngayCapNhat":"2026-08-07T11:55:35.778Z","trangThai":"HOAT_DONG",…},"meta":null}` |
| Thân yêu cầu | như lượt 1, thêm `"soTheHanhNghe":"QA-G3-20260807"`, vẫn mang `"chungChiMoiIds":["99b9a7e5-…"]` |

Ảnh: `image/CNHSNLTVV_03-04-sau-khi-bam-luu-hop-le.png` (**đã mở đọc**) — form đã đóng, bảng chỉ đọc
hiện `Chứng chỉ chi tiết = QA G3 (4.8) & CN (9.8).pdf` và `Số thẻ hành nghề = QA-G3-20260807`.

## 8. VERIFY BẢN CHẤT (B6) — tải lại trang rồi đọc lại

`navigate_page type=reload ignoreCache=true` → mở lại tab **Năng lực** → đọc song song màn hình và máy chủ.

| Vế | Trên màn (sau khi tải lại) | Trên máy chủ (`GET /tu-van-viens/{id}`) | Kết |
|---|---|---|---|
| Dữ liệu có được lưu thật | `Trình độ Cử nhân` · `1 năm` · `Chuyên ngành Luật hành chính` · **`Số thẻ hành nghề QA-G3-20260807`** | `version` **14 → 15**, `hoSo.version` **3 → 4**, `ngayCapNhat=2026-08-07T11:55:35.778Z`, `soTheHanhNghe="QA-G3-20260807"` | ✅ **ĐẠT** |
| Tệp vừa đính có được gắn vào hồ sơ | **`Chứng chỉ chi tiết → QA G3 (4.8) & CN (9.8).pdf`** | `hoSo.chungChiChiTiet = [{"fileDinhKemId":"99b9a7e5-…"}]` (gốc là `[]`) | ✅ **ĐẠT** |
| Không có tác dụng phụ trạng thái | badge vẫn *Đang hoạt động* | `trangThai` vẫn `HOAT_DONG` | ✅ |

## 9. Khôi phục dữ liệu (B7)

| Bước | Kết quả |
|---|---|
| Gỡ chứng chỉ vừa gắn (`chungChiXoaIds:["99b9a7e5-…"]`) | `PATCH …/nang-luc` → **200**; đọc lại `hoSo.chungChiChiTiet = []` ✅ về gốc |
| Xoá tệp đã nạp ở lượt đo | `DELETE …/files/99b9a7e5-…` → **204** ✅ |
| Xoá tệp rác của lượt dựng cảnh hỏng (§5.3) | `DELETE …/files/c128cc34-…` → **204** ✅ |
| Trả `soTheHanhNghe` về `null` | `PATCH` với `soTheHanhNghe:null` → **HTTP 422** `ERR-VAL-IV-03-10` *"Số thẻ hành nghề là bắt buộc đối với Tư vấn viên"* ⇒ **KHÔNG khôi phục được bằng chính màn này** |

**Đọc lại lần cuối (sau khi tải lại trang) — đối chiếu với bản sao lưu §3:**

| Trường | Gốc | Sau khi khôi phục | |
|---|---|---|---|
| `trangThai` | `HOAT_DONG` | `HOAT_DONG` | ✅ |
| `trinhDo` · `soNamKinhNghiem` · `chuyenNganh` | `Cử nhân` · `1` · `Luật hành chính` | y hệt | ✅ |
| `linhVucIds` | 3 mục | 3 mục y hệt | ✅ |
| `hoSo.bangCapChiTiet` · `hoSo.chungChiChiTiet` | `[]` · `[]` | `[]` · `[]` | ✅ |
| `fileDinhKems` | 1 tệp `2K15 T3 (4.8) & CN (9.8).pdf` | **đúng 1 tệp đó** | ✅ |
| **`soTheHanhNghe`** | **`null`** | **`QA-G3-20260807`** | ❌ **CÒN SÓT — không gỡ được** |
| `version` · `hoSo.version` | 14 · 3 | 15 · 5 | bộ đếm, không hoàn nguyên được |
| `ghiChuCapNhat` (trường nhật ký, không hiện trên hồ sơ) | — | `Khoi phuc sau do G3 CNHSNLTVV_03` | ghi nhận |

**Khai đủ 3 thông tin theo T8:** bản ghi **`TVV-BTP-TW-0063`** · đổi **`soTheHanhNghe` `null → "QA-G3-20260807"`**
(giá trị mang tiền tố QA để nhận diện, không gỡ được vì máy chủ bắt buộc trường này với loại Tư vấn viên) ·
env **`htpldn-uat.ospgroup.vn`**. Ngoài ra tài khoản `nht_04_ui` bị đặt `cccd = 000000000004` (§5.1).
Mọi thứ còn lại đã về đúng gốc. Ảnh: `image/CNHSNLTVV_03-05-sau-khi-khoi-phuc.png` (**đã mở đọc** —
`Chứng chỉ chi tiết = —`).

## 10. Chốt verdict theo bảng chuẩn chấm §6

| # | Điều kiện | Số đo | Kết |
|---|---|---|---|
| **C1** | Bấm Lưu ở form Cập nhật năng lực **có đính tệp chứng chỉ mới** → không bị chặn bằng thông báo lỗi hệ thống | **0/2 lượt** hiện *"Lỗi hệ thống, vui lòng thử lại sau."*; lượt đủ dữ liệu hợp lệ → **HTTP 200 `success:true`** + 1 thông báo *"Cập nhật năng lực thành công"* | ✅ **ĐẠT** |
| **C2** | Dữ liệu được ghi thật, còn nguyên sau khi tải lại | màn + máy chủ khớp nhau; `version` 14→15, `hoSo.version` 3→4 | ✅ **ĐẠT** |
| **C3** | Tệp chứng chỉ mới được gắn vào hồ sơ | `hoSo.chungChiChiTiet` `[]` → `[{fileDinhKemId:"99b9a7e5-…"}]`, màn hiện đúng tên tệp | ✅ **ĐẠT** |

**Lượt 422 KHÔNG kéo verdict xuống Reopen**, vì đó là lời từ chối nghiệp vụ có căn cứ đặc tả (`:1507`,
NĐ 77/2008 Đ.20) do dữ liệu gửi lên còn thiếu trường bắt buộc — thuộc nhánh *"sửa tiền đề rồi đo lại"*
của chuẩn chấm §8, không phải triệu chứng của phiếu. Sau khi nhập đủ dữ liệu hợp lệ, cả 3 vế đều đạt.

# ⇒ VERDICT: ✅ **Pass** — ghi `Trạng thái dev fix = UAT done` (BRIEF §5)

## 11. Ghi nhận NGOÀI phạm vi (BRIEF §4.12 — không ảnh hưởng verdict, không tự thêm dòng sheet)

- **N12 — Cổng nhập CCCD chặn cứng, không có đường thoát.** Hộp thoại bắt buộc nhập CCCD sau đăng nhập
  không có nút đóng/huỷ và không đóng bằng `Escape`; người dùng chưa có CCCD trong hồ sơ **không thể dùng
  bất kỳ chức năng nào**. Đặc tả `srs-fr-04` không mô tả cổng này. → xem `note/CNHSNLTVV_03-ngoai-pham-vi.md`.
- **N13 — Tệp được ghi vào hồ sơ ngay lúc đính, trước khi bấm Lưu.** Thao tác chọn tệp phát sinh
  `POST …/files` → **201** và tệp xuất hiện ngay trong `fileDinhKems` của hồ sơ. Nếu người dùng bỏ dở form
  (hoặc form tự reset như §5.3) thì **tệp rác vẫn nằm lại trên hồ sơ**. Lượt này đã tự dọn (`DELETE` 204).
- **N14 — Ràng buộc "Số thẻ hành nghề" lệch giữa 3 nơi.** Máy chủ bắt buộc trường này với loại Tư vấn viên
  ở cả màn cập nhật năng lực (`ERR-VAL-IV-03-10`), trong khi **bảng Inputs của FR-IV-04 `:389` ghi
  `so_the_hanh_nghe | text | N` (không bắt buộc)** và **ô nhập trên form không có dấu bắt buộc**.
  Hệ quả thực tế: hồ sơ cũ có trường này rỗng thì **không thể lưu năng lực** cho tới khi điền, và **điền rồi
  thì không xoá lại được**. Cần BA chốt phạm vi áp dụng của quy tắc `:1507` cho FR-IV-04.
