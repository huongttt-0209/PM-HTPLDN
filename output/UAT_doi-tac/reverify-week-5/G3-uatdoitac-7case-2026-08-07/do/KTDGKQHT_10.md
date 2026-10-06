# NHẬT KÝ ĐO — KTDGKQHT_10 (dòng 11) · Lô G3 · env nghiệm thu đối tác

> 🔴 **Phạm vi đã được user THU HẸP giữa lượt đo** (thông báo lead lúc ~18:10): chỉ verify **đúng triệu chứng
> bug gốc** — *"Màn hình không có nút chức năng"*. Bỏ phần nạp tệp thật / đo bản xem trước làm căn cứ verdict /
> đọc lại điểm đã lưu. Các số đo đã kịp thu được **trước** lúc thu hẹp vẫn ghi đầy đủ ở §7 (thừa còn hơn thiếu),
> nhưng **verdict chỉ chấm trên triệu chứng gốc**.
>
> ✅ **KHÔNG có bất kỳ thay đổi dữ liệu nào xảy ra** — dừng trước nút "Xác nhận import". Xem §8.

## 1. Bảng đầu

| Mục | Giá trị |
|---|---|
| Mã TC · dòng | **KTDGKQHT_10** · dòng **11** · tab `bug` |
| Mô tả phiếu | "Tải lên tệp Excel Kết quả kiểm tra" |
| TKM phản hồi lần 1 | **"Màn hình không có nút chức năng"** |
| Ảnh/video đối tác · Kết quả thực tế | **đều TRỐNG** — không có bằng chứng đối tác; toàn bộ tiền đề do QA tự dựng |
| Env | `https://htpldn-uat.ospgroup.vn` (env nghiệm thu đối tác) |
| **Bản dựng đọc trên UI** | **V1.0.10** (sidebar "HTPLDN · V1.0.10") · bó mã `assets/index-Bd1akG3f.js` |
| Tài khoản | `cbnv_tw` — vai trò **`CB_NV_TW`**, cấp **TW**, đơn vị `00000000-0000-4000-8000-000000000001`, họ tên hiển thị "Cán bộ NV Trung ương" (đọc từ `GET /api/v1/auth/me`) |
| Ngày giờ đo | **2026-08-07**, 18:00–18:15 giờ VN (11:00–11:08 UTC theo header `date` của máy chủ) |
| Phiên | Dùng lại phiên đang mở, **không đăng nhập lại** (env giới hạn 5 lượt/60s). Đã `reload ignoreCache=true` trước khi đo |

## 2. Tiền đề đã xác nhận trên màn (B0–B2)

| Tiền đề | Giá trị đo được | Nguồn |
|---|---|---|
| Khóa học đo | **`KH-20260509-006`** — "Luật đất đai cập nhật 2024 - R9", `id=dd1adee1-715e-47f9-986d-52f9dcc60373` | UI + `GET /khoa-hocs/{id}` |
| **Trạng thái khóa** | **"Đang diễn ra"** — bước 4 của thanh tiến trình đang `ant-steps-item-process ant-steps-item-active`; API trả `trangThai=DANG_DIEN_RA`, `version=20` | ảnh `-00-`, `-02-` |
| ⇒ Điều kiện 2 của phiếu | **THỎA** ("Khóa học ở trạng thái *Đang diễn ra* hoặc *Đã kết thúc*") | SRS `:537` PRE-04 |
| Đề kiểm tra đã gán | **1 đề** — "Đề kiểm tra cuối khóa luật đất đai quý 3 năm 2026", `deKiemTraId=bc334727-7065-4b63-8d58-f814fc31c95d`, `trangThai=KICH_HOAT` | `GET /khoa-hocs/{id}/de-kiem-tras` |
| Học viên trong khóa | **6** (tester 1…6), sĩ số hiển thị `6/100` | `GET /khoa-hocs/{id}/ket-quas` |
| Khóa **chưa** ở `CHO_DUYET_KQ` | Đúng — bước 6 "Chờ duyệt KQ" còn `ant-steps-item-wait` ⇒ bảng **không** ở chế độ chỉ đọc (`:1929`) | ảnh `-00-` |

**Đường dẫn thật:**
- Danh sách: `https://htpldn-uat.ospgroup.vn/dao-tao/khoa-hoc/danh-sach` — vào màn ô lọc **đã sạch** (kiểm bằng bộ chọn đã cải chính `.ant-select-content-has-value` + `title`: chỉ có ô `20 / trang`; ô ngày rỗng; ô từ khoá rỗng; chân bảng "Hiển thị 1-20 / 22 kết quả" = tổng 22) ⇒ **không cần bấm "Xóa bộ lọc"**.
- Chi tiết: `.../dao-tao/khoa-hoc/dd1adee1-715e-47f9-986d-52f9dcc60373`
- Tab kết quả: `.../dd1adee1-715e-47f9-986d-52f9dcc60373?tab=ket-qua-kiem-tra`

## 3. Điểm gốc 6 học viên — BẢN SAO LƯU trước khi thao tác (Kỷ luật §1)

Đọc bằng `GET /api/v1/khoa-hocs/{id}/ket-quas` (fetch `credentials:'include'`) lúc 18:00:

| # | Học viên | `dangKyId` | **Điểm kiểm tra** | `ketQua` | `xepLoai` | Chuyên cần |
|---|---|---|---|---|---|---|
| 1 | tester 1 | `a61ab8f0-5cf9-4c77-80f6-89af0c6419d2` | **9.0** | KHONG_DAT | GIOI | 2/5 (40.00%) |
| 2 | tester 2 | `fff9490c-0e6d-4205-95f7-962fe6993f3c` | **4.0** | KHONG_DAT | KHONG_DAT | 1/5 (20.00%) |
| 3 | tester 3 | `2a2e3495-1834-4e40-9fd6-8d3e878ca11d` | **null** | null | null | 0/5 (0.00%) |
| 4 | tester 4 | `19186ac6-eca1-4062-a0a7-84a09e8edea6` | **null** | null | null | 1/5 (20.00%) |
| 5 | tester 5 | `446b3a02-bb8e-437a-b46a-3fdba367f56a` | **null** | null | null | 1/5 (20.00%) |
| 6 | tester 6 | `20ab2a8e-7334-42a0-a717-289eb9fc7f81` | **null** | null | null | 0/5 (0.00%) |

> ⚠️ Đính chính recon §2.1: recon ghi "6 học viên **đã có điểm sẵn**". Thực tế **chỉ 2/6** có điểm
> (tester 1 = 9.0 · tester 2 = 4.0); 4 học viên còn lại điểm **null**.

## 4. 🔴 B4 — Rà chức năng 2 lượt (PHẦN QUYẾT ĐỊNH VERDICT)

### 4.1 Nhãn tab thật

Phiếu ghi tab **"Kết quả kiểm tra"**. Nhãn hiển thị thật trên V1.0.10 là **"Kết quả"**
(khóa nội bộ `data-node-key="ket-qua-kiem-tra"`, đúng Tab 5 của SCR-III-02). Đây là **khác biệt câu chữ nhãn**,
không phải khác chức năng. 8 tab thật: *Thông tin · Học viên · Lịch học · Điểm danh · **Kết quả** · Công bố kết quả ·
Bài giảng đã gán · Đề kiểm tra*.

### 4.2 Lượt A — CHƯA chọn đề kiểm tra

Khóa `KH-20260509-006` **chỉ có 1 đề** và giao diện **tự chọn sẵn** đề đó; ô chọn **không có nút xóa**
(`allowClear=false`) ⇒ trên chính khóa này **không dựng được** trạng thái "chưa chọn đề".

→ Dựng lượt A bằng **khóa đối chứng cùng điều kiện**, chỉ khác duy nhất ở chỗ **chưa có đề**:
**`KH-2026-001`** "Bồi dưỡng kiến thức pháp luật kinh doanh năm 2026"
(`id=99f4d1e2-5a21-4b11-8e31-abc123456789`, **`DANG_DIEN_RA`** — cùng trạng thái hợp lệ, **1 học viên**, **0 đề gán**).
Lượt này **chỉ xem, không bấm bất kỳ nút hành động nào**.

Liệt kê `button` / `a` / `[role=button]` / `input[type=file]` trong vùng tab (lấy cả `innerText`, `title`,
`aria-label`, tên icon, thuộc tính vô hiệu hoá):

| Phần tử | Icon | Trạng thái |
|---|---|---|
| Ô chọn đề — placeholder **"Chọn đề kiểm tra"** | — | **rỗng, chưa chọn** |
| **"Lưu kết quả"** | `save` | 🚫 **vô hiệu hoá** |
| **"Tải mẫu điểm kiểm tra"** | `download` | 🚫 **vô hiệu hoá** |
| **"Import Excel"** | `import` | 🚫 **vô hiệu hoá** |
| "Xuất DOCX" | `file-word` | ✅ bật |

`input[type=file]` toàn trang: **0**.

📸 `image/KTDGKQHT_10-01-chua-chon-de.png` — **đã Read ra đọc:** ô "Chọn đề kiểm tra" trống; 3 nút
*Lưu kết quả · Tải mẫu điểm kiểm tra · Import Excel* hiển thị **xám mờ**; chỉ "Xuất DOCX" đậm.

### 4.3 Lượt B — ĐÃ chọn đề kiểm tra

Quay lại `KH-20260509-006`, tab "Kết quả". Ô chọn đề mang giá trị
**"Đề kiểm tra cuối khóa luật đất đai quý 3 năm 2026"**. Rà lại y hệt:

| Phần tử | Icon | Trạng thái |
|---|---|---|
| Ô chọn đề | — | **có giá trị** = "Đề kiểm tra cuối khóa luật đất đai quý 3 năm 2026" |
| "Lưu kết quả" | `save` | 🚫 vô hiệu (chưa sửa ô điểm nào — hợp lý) |
| **"Tải mẫu điểm kiểm tra"** | `download` | ✅ **BẬT** |
| **"Import Excel"** | `import` | ✅ **BẬT** |
| "Xuất DOCX" | `file-word` | ✅ bật |

📸 `image/KTDGKQHT_10-02-da-chon-de.png` — **đã Read ra đọc:** ô đề mang tên đề; "Tải mẫu điểm kiểm tra"
và "Import Excel" hiển thị **đậm, viền rõ**; bảng dưới hiện tester 1 = `9.0`, tester 2 = `4.0`.

### 4.4 So sánh A ↔ B

| Nút | Lượt A (chưa chọn đề) | Lượt B (đã chọn đề) | Kết |
|---|---|---|---|
| Tải mẫu điểm kiểm tra | 🚫 vô hiệu | ✅ bật | **đổi trạng thái theo đúng điều kiện** |
| Import Excel | 🚫 vô hiệu | ✅ bật | **đổi trạng thái theo đúng điều kiện** |

⇒ Nút **có mặt trên màn ở cả hai lượt**, chỉ **bật lên sau khi có đề kiểm tra**. Khớp đúng đặc tả
`srs-fr-03-dao-tao.md:578` (đã mở file xác minh):

```
| Mẫu điểm kiểm tra | "Tải mẫu điểm kiểm tra" (Tab 5) | Đề kiểm tra đang chọn (`de_kiem_tra_id`) | Đã chọn đề thuộc khóa + khóa `DANG_DIEN_RA`/`DA_KET_THUC` + có quyền |
```

và `:1924` — *"Hỗ trợ Import Excel qua tệp mẫu — nút **"Tải mẫu điểm kiểm tra"** (bật sau khi chọn đề kiểm tra
thuộc khóa, khóa `DANG_DIEN_RA`/`DA_KET_THUC`, có quyền…)"*.

🔴 **Đây gần như chắc chắn là gốc của phản hồi "Màn hình không có nút chức năng":** nếu mở tab "Kết quả" của một
khóa **chưa gán đề kiểm tra**, các nút này nằm đó nhưng **mờ và không bấm được** — nhìn đúng như "không có nút".
Trạng thái đó **đúng đặc tả, không phải lỗi**.

## 5. Chứng minh chức năng GỌI ĐƯỢC (không dừng ở quan sát tĩnh)

Không dừng ở "thấy nút". Đã bấm thật:

| # | Thao tác | Kết quả đo được |
|---|---|---|
| 1 | Bấm **"Tải mẫu điểm kiểm tra"** | `GET /api/v1/khoa-hocs/{id}/ket-quas/template?deKiemTraId=bc334727-…` → **HTTP 200**, `content-length: 8278`, `content-type: …spreadsheetml.sheet`, `content-disposition: attachment; filename="mau-diem-kiem-tra-KH-20260509-006.xlsx"`. **Tệp về máy thật** (`~/Downloads`, 8278 byte) |
| 2 | Bấm **"Import Excel"** | Mở hộp thoại **"Import điểm kiểm tra từ Excel"** — có vùng **"Kéo thả hoặc click để chọn file"**, `input[type=file]` `accept=".xlsx"`, nút "Kiểm tra tệp", cùng câu dẫn *"Chỉ dùng tệp từ nút Tải mẫu điểm kiểm tra. Hệ thống chỉ ghi dữ liệu sau khi bạn xem trước và xác nhận."* |
| 3 | Chọn tệp + bấm **"Kiểm tra tệp"** | `POST /api/v1/khoa-hocs/{id}/ket-quas/import/preview` (multipart, `file` + `deKiemTraId`) → **HTTP 200**, `success:true` |

**Tệp mẫu do hệ thống sinh — đã mở đọc bằng `openpyxl`:**
- Sheet ẩn `_HTPLDN_META` (`sheet_state=veryHidden`): `template_version=1` · `template_type=DIEM_KIEM_TRA` ·
  `khoa_hoc_id=dd1adee1-715e-47f9-986d-52f9dcc60373` · `de_kiem_tra_id=bc334727-7065-4b63-8d58-f814fc31c95d`.
- Sheet `Mẫu điểm kiểm tra`: cột `hoc_vien_id · Họ tên · Email · Đơn vị · Điểm kiểm tra · Ghi chú`,
  **6 dòng học viên điền sẵn**, cột Điểm để trống. Khớp bộ cột SRS `:582`.

⇒ Chức năng **hiện diện, bấm được, máy chủ nhận và xử lý được tệp**. **Không có 4xx/5xx nào.**

📸 `image/KTDGKQHT_10-03-ban-xem-truoc.png` — **đã Read ra đọc:** hộp thoại "Import điểm kiểm tra từ Excel" mở,
hệ thống đã xử lý xong tệp và hiện khối kết quả kiểm tệp.

## 6. Thông báo + console

- Bộ bắt thông báo: dùng **đúng** `output/UAT_doi-tac/tools/toast-capture.js`, cài **TRƯỚC** mọi thao tác,
  **không lọc trùng**, đọc bằng `innerText`.
- **Tự kiểm observer:** `soObserverDangSong = 1` → **số liệu hợp lệ**.
- Kết quả: **0 khung thông báo**, `BI_LAP=false`. Lời gọi ghi dữ liệu bắt được: **đúng 1** —
  `POST …/ket-quas/import/preview` (endpoint **xem trước, không ghi**). Không có lời gọi ghi nào khác.
- `list_console_messages` (error + warn): **0 lỗi**; đúng 1 cảnh báo `Route path "/ticket=*"` — cảnh báo
  thư viện định tuyến, không liên quan case (đã gặp ở cả 4 case trước của lô).

## 7. Số đo thu được TRƯỚC lúc thu hẹp phạm vi (ghi nhận, KHÔNG dùng làm căn cứ verdict)

Trước khi có thông báo thu hẹp, đã kịp chạy tới bước **xem trước** (bước không ghi dữ liệu). Ghi lại nguyên vẹn:

**Tệp nạp** `seed-files/KTDGKQHT_10-nap.xlsx` (dựng từ tệp mẫu hệ thống sinh; **không sửa** `hoc_vien_id`,
**không xóa** sheet ẩn `_HTPLDN_META`):

| Dòng Excel | Học viên | Điểm điền | Chủ ý |
|---|---|---|---|
| 2 | tester 1 | `7.5` | hợp lệ (số lẻ) |
| 3 | tester 4 | `0` | hợp lệ (biên dưới) |
| 4 | tester 3 | `10` | hợp lệ (biên trên) |
| 5 | tester 2 | `6` | hợp lệ |
| 6 | tester 5 | `15` | **cố ý lỗi** — ngoài thang 0–10 |
| 7 | tester 6 | `abc` | **cố ý lỗi** — sai kiểu |

**Bản xem trước hiện ra trên màn** — `Tổng dòng 6 · Hợp lệ 4 · Lỗi 2`, hai tab `Hợp lệ (4)` / `Lỗi (2)`,
bảng cột `Dòng · Trạng thái · Học viên · Điểm · Ghi chú · Lý do lỗi`:

| Dòng | Trạng thái | Học viên | Điểm | Lý do lỗi (nguyên văn) |
|---|---|---|---|---|
| 2 | Hợp lệ | tester 1 | 7.5 | – |
| 3 | Hợp lệ | tester 4 | 0 | – |
| 4 | Hợp lệ | tester 3 | 10 | – |
| 5 | Hợp lệ | tester 2 | 6 | – |
| 6 | **Lỗi** | tester 5 | – | `ERR-KQ-01: Điểm kiểm tra không hợp lệ (0-10): 15` |
| 7 | **Lỗi** | tester 6 | – | `ERR-KQ-01: Điểm kiểm tra không hợp lệ (0-10): abc` |

Nút xác nhận mang nhãn **"Xác nhận import (4 dòng hợp lệ)"**.

**Thân phản hồi `POST …/import/preview` (HTTP 200), nguyên văn rút gọn:**
```json
{"success":true,"data":{"sessionId":"fa1cb199-8e00-4d64-93e0-46e258526854","total":6,"valid":4,"invalid":2,
 "rows":[{"row":2,"hoTen":"tester 1","diemKiemTra":7.5,"status":"HOP_LE"},
         {"row":3,"hoTen":"tester 4","diemKiemTra":0,"status":"HOP_LE"},
         {"row":4,"hoTen":"tester 3","diemKiemTra":10,"status":"HOP_LE"},
         {"row":5,"hoTen":"tester 2","diemKiemTra":6,"status":"HOP_LE"},
         {"row":6,"hoTen":"tester 5","diemKiemTra":null,"status":"LOI","reason":"ERR-KQ-01: Điểm kiểm tra không hợp lệ (0-10): 15"},
         {"row":7,"hoTen":"tester 6","diemKiemTra":null,"status":"LOI","reason":"ERR-KQ-01: Điểm kiểm tra không hợp lệ (0-10): abc"}]}}
```

> Số đo này khớp cả 3 chiều mà vế A2 của chuẩn chấm đòi (phân nhóm hợp lệ/lỗi · số dòng · lý do kèm mã lỗi),
> nhưng **vẫn không đưa vào verdict** vì phạm vi đã thu hẹp — và vì **chưa chạy vế nạp thật + đọc lại dữ liệu**,
> nên **không kết luận gì** về phần xử lý phía sau (ghi dữ liệu, báo cáo sau nạp, chống kéo điểm về biên).

## 8. Kỷ luật dữ liệu — KHÔNG có thay đổi nào

- **Dừng trước nút "Xác nhận import (4 dòng hợp lệ)"** — đóng hộp thoại bằng nút **Close**.
- Endpoint đã gọi duy nhất là `import/preview` — chính hộp thoại khai *"Hệ thống chỉ ghi dữ liệu sau khi bạn xem
  trước và xác nhận"*, và tài liệu API mô tả `import/preview` là **"Xem trước, chưa ghi dữ liệu"**.
- **Đối chứng bằng số:** đọc lại `GET /khoa-hocs/{id}/ket-quas` sau khi đóng hộp thoại →
  `tester 1 = 9.0 · tester 2 = 4.0 · tester 3/4/5/6 = null` — **khớp 6/6 với bản sao lưu §3, số dòng lệch = 0**.
- ⇒ **Không cần khôi phục.** Không tạo học viên, không xóa bản ghi, **không bấm "Trình duyệt kết quả"**,
  không bấm "Kết thúc" / "Gỡ công khai".
- Tệp `seed-files/KTDGKQHT_10-khoi-phuc.xlsx` đã dựng sẵn (tester 1 = 9.0 · tester 2 = 4.0 · còn lại trống)
  nhưng **không dùng đến** vì không có gì để khôi phục. Giữ lại để lượt sau dùng nếu cần.

## 9. Đối chiếu đặc tả (đã mở file xác minh từng dòng)

Nguồn: `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-03-dao-tao.md`

| Dòng | Nguyên văn (rút gọn) | Dùng cho |
|---|---|---|
| `:522` | *"SCR-III-02 (chi tiết Khóa học — Tab 4 "Điểm danh" + **Tab 5 "Kết quả kiểm tra"**)"* | màn/tab |
| `:524` | *"Hỗ trợ nhập thủ công + **import Excel**"* | có chức năng |
| `:526` | *"**Tác nhân:** CB NV / CB PD"* | vai trò đo |
| `:534` | PRE-01 — *"có quyền "Quản lý kết quả ĐT""* | quyền |
| `:537` | PRE-04 — *"**Nhập điểm kiểm tra:** khóa học ở `DANG_DIEN_RA` **hoặc** `DA_KET_THUC`"* | Điều kiện 2 phiếu |
| **`:578`** | *"Đã chọn đề thuộc khóa + khóa `DANG_DIEN_RA`/`DA_KET_THUC` + có quyền"* (điều kiện **bật nút**) | **giải thích A↔B** |
| `:589` | Processing Import Excel bước 1 — *"Upload file Excel (.xlsx)"* | có đường tải lên |
| `:1924` | *"Hỗ trợ Import Excel qua tệp mẫu — nút "Tải mẫu điểm kiểm tra" (**bật sau khi chọn đề kiểm tra** thuộc khóa…)"* | **giải thích A↔B** |
| `:1929` | *"**Chỉ đọc từ `CHO_DUYET_KQ`**"* | loại trừ — khóa đo chưa tới bước đó |

## 10. Bẫy đã né

| Bẫy (chuẩn chấm §7) | Xử lý thật |
|---|---|
| (a) Nút mờ đúng đặc tả khi chưa chọn đề | **Đã dựng khóa đối chứng 0 đề** để đo lượt A thật, không suy đoán |
| (b) Nút chỉ có biểu tượng / nằm trong menu phụ / `input[type=file]` ẩn | Liệt kê DOM đủ `innerText` + `title` + `aria-label` + tên icon + cờ vô hiệu, **không** kết luận bằng mắt qua ảnh |
| (c) Nhầm "Tải mẫu" ↔ "Tải lên" ↔ "Xuất Excel" | Ghi tách bạch 4 nút; nút xuất trên tab này là **"Xuất DOCX"**, không nhầm với đường nhập |
| (d) Đo nhầm Tab 4 "Điểm danh" | Đo đúng tab khoá nội bộ `ket-qua-kiem-tra` |
| (e) Tệp tự chế bị từ chối | Dùng **đúng tệp hệ thống sinh**; máy chủ nhận, không có ERR-KQ-02/09 |
| (g) Khóa đã trình duyệt KQ → bảng chỉ đọc | Đã kiểm: bước "Chờ duyệt KQ" còn `wait` |
| (h) Đổi vai trò để "cho ra nút" | **Không đổi** — đo bằng đúng `cbnv_tw` (CB NV) |
| (i) `innerText` không `textContent` | Toàn bộ đọc chữ bằng `innerText` |
| (n) Tab chạy mã cũ | `reload ignoreCache=true` trước lượt đo + ghi bản dựng V1.0.10 |

## 11. VERDICT (theo phạm vi đã thu hẹp)

> **✅ Pass — `UAT done`.**

| Vế trong phạm vi | Số đo quyết định | Kết |
|---|---|---|
| Sau khi chọn đề, màn **có** chức năng nạp tệp Excel kết quả | Lượt B: "Tải mẫu điểm kiểm tra" + "Import Excel" đều **bật**; lượt A cùng 2 nút **vô hiệu** ⇒ khác biệt do đúng điều kiện `:578`, không phải thiếu chức năng | ✅ ĐẠT |
| Chức năng **bấm được / gọi được**, không lỗi | Tải mẫu → **HTTP 200**, tệp 8278 byte về máy, mở đọc được. Import Excel → hộp thoại mở, chọn tệp được. Kiểm tệp → `POST …/import/preview` **HTTP 200**. **0 lỗi 4xx/5xx · 0 lỗi console** | ✅ ĐẠT |

**Triệu chứng gốc "Màn hình không có nút chức năng" KHÔNG tái hiện** trên V1.0.10 khi khóa ở "Đang diễn ra"
và đã có đề kiểm tra.

**Phạm vi hiệu lực:** kết luận này chỉ nói về **sự hiện diện và gọi được** của chức năng nạp tệp Excel kết quả
kiểm tra. **Không khẳng định gì** về phần xử lý tệp phía sau (ghi dữ liệu vào bảng, báo cáo sau khi nạp,
ràng buộc thang điểm khi ghi) — phần đó **không nằm trong phạm vi lượt này**.

## 12. Ghi nhận ngoài phạm vi (chưa log bug, chờ lead quyết)

| # | Nội dung |
|---|---|
| **N6** | **Tên tệp mẫu tải về không dùng tên máy chủ khai.** Máy chủ trả `content-disposition: attachment; filename="mau-diem-kiem-tra-KH-20260509-006.xlsx"` (theo **mã khóa học**), nhưng tệp lưu xuống máy là `mau-diem-kiem-tra-dd1adee1-715e-47f9-986d-52f9dcc60373.xlsx` (theo **mã nội bộ**) ⇒ giao diện tự đặt tên đè lên tên máy chủ khai. Người dùng thấy tên tệp là chuỗi mã máy, khó nhận ra thuộc khóa nào. **Không ảnh hưởng verdict** case này. |
| **N7** | **Nhãn tab lệch đặc tả:** đặc tả `:522`/`:1924` gọi Tab 5 là **"Kết quả kiểm tra"**, giao diện V1.0.10 hiển thị **"Kết quả"** (khóa nội bộ vẫn `ket-qua-kiem-tra`). Chỉ là câu chữ nhãn. |
| **N8** | **Đính chính recon §2.1** (dữ liệu, không phải lỗi phần mềm): recon ghi 6 học viên "đã có điểm sẵn"; thực tế **chỉ 2/6** có điểm. |

## 13. Sản phẩm

| Loại | Đường dẫn |
|---|---|
| Ảnh | `image/KTDGKQHT_10-00-khoa-dang-dien-ra.png` · `-01-chua-chon-de.png` · `-02-da-chon-de.png` · `-03-ban-xem-truoc.png` (đều đã Read ra đọc) |
| Tệp | `seed-files/KTDGKQHT_10-mau-goc-he-thong-sinh.xlsx` · `-nap.xlsx` · `-khoi-phuc.xlsx` (không dùng đến) |
| Note đối tác | `note/KTDGKQHT_10-ketqua-verify.txt` |
