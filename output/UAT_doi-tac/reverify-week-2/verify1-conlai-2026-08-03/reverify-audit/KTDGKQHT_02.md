# KTDGKQHT_02 — Audit verify vòng 1 (2026-08-03)

> Sheet `1OKBN2otlmdZ44THkmhtsn-_63M2Boh7zQwearwjYR3s` · tab `UAT_TGPL Doanh Nghiệp-tuần 2` · row **116**
> Cột P (dev) = `Reject` — **giữ nguyên**. Cột Q (QA Verify) = **`BA confirm`**.
> Tài khoản ra verdict: **`cbnv_tw`** (vai trò `CB_NV_TW`, đơn vị `Bộ Tư Pháp · Cục Bổ trợ tư pháp`, `BTP · TW`). Không dùng `admin`.
> Bản dựng đã test: **HTPLDN · V1.0.5** (đọc từ chân sidebar) — env `https://18.143.165.120.nip.io`.

## Note dev trước khi QA đè (2026-08-03)

Nguyên văn cột R (`DEV phản hồi lần 1`) trước khi ghi đè:

```
KHÔNG phải bug: Tab "Kết quả kiểm tra" (SCR-III-02) không có 4 cột số buổi — các cột đó thuộc Tab "Điểm danh". Code đúng spec (còn thêm cột Chuyên cần). Kỳ vọng của TC lệch SRS v3.5.
```

**Lập luận này SAI ở dữ kiện.** Tab "Điểm danh" trên bản V1.0.5 chỉ có **7 cột**: `STT · Họ tên · Email · Số điện thoại · Đơn vị · Trạng thái · Ghi chú` (đo bằng DOM, `scrollWidth 1141` vs `clientWidth 1136` → không có cột nào bị khuất). Đặc tả `srs-fr-03-dao-tao.md:1896` (Tab 4 — Điểm danh) **cũng không** liệt kê 4 cột đó. Không có dòng SRS nào chống lưng cho câu *"các cột đó thuộc Tab Điểm danh"*.

Phần dev nói đúng: danh sách cột của Tab 5 tại `:1901` **không** chứa 4 cột, và app **có thêm** cột `Chuyên cần`. Nhưng đó **không đủ** để kết luận `Reject` — xem §Vì sao BA confirm.

## Cổng 1 — 3 dữ kiện neo (tự mở full-res, không đọc lại của phiên trước)

| # | Dữ kiện | Giá trị |
|---|---|---|
| (a) | URL / ID bản ghi | `htpldn-uat.ospgroup.vn/dao-tao/khoa-hoc/0362c6e3-1968-4644-9001-d24b267e6b21?tab=ket-qua-kiem-tra` (ảnh `-2`) và `?tab=lich-hoc-diem-danh` (ảnh `-1`) — cùng 1 khoá học |
| (b) | Trạng thái entity | Stepper: `✓ Dự thảo — ✓ Chờ duyệt — ✓ Đã duyệt — **(4) Đang diễn ra** — 5 Đã kết thúc — 6 Chờ duyệt KQ — 7 Hoàn thành`; băng vàng *"Kết quả tạm tính"* |
| (c) | Dữ liệu tiền đề | 1 học viên `Hoàng Minh Đức` · `0105545484`; ô `Chuyên cần = 0/3 (33.33%)` ⇒ khoá có 3 buổi; tab Điểm danh: buổi `15/07/2026 · 14:00:00-15:00:00`, HV chấm **Vắng có phép** |

Vai trò đối tác đọc từ header phải cả 2 ảnh: `Cán bộ NV Trung ương` · **`CB_NV_TW`** · `BTP · TW`.

## Cổng 2 — 3 dòng

1. **Evidence + frame chứa LỖI:** `partner-evidence/KTDGKQHT_02_v2-2.jpg` (ảnh tĩnh full-res, đồng hồ máy `05:02 PM 2026-07-24`). Trong khung hình, bảng tab "Kết quả" chỉ có 9 cột nhìn thấy `STT · Họ tên · Email · Số điện thoại · Đơn vị · Chuyên cần · Điểm kiểm tra · Kết quả · Xếp loại`; không có cột nào mang tên 4 trường đối tác nêu. Ảnh `-1.jpg` (`05:01 PM`) là tab "Điểm danh" cùng khoá, 7 cột, cũng không có.
2. **Đối tác phản ánh CỤ THỂ:** tab "Kết quả kiểm tra" **thiếu 4 trường hiển thị** `Số buổi có mặt` / `Số buổi vắng có phép` / `Số buổi vắng không phép` / `Tổng số buổi`. Không phàn nàn sai số liệu, không phàn nàn tràn cột.
3. **Data + bước tái hiện:** đăng nhập CB_NV_TW → `Đào tạo, tập huấn` → `Khóa học` → mở chi tiết khoá **Đang diễn ra** có ≥1 học viên + ≥3 buổi + đã điểm danh ≥1 buổi → tab `Kết quả` → cuộn hết thanh ngang → đọc danh sách cột.

## Cổng 3 — SRS yêu cầu vs thực tế web

Nguồn SRS: `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-03-dao-tao.md` (bản chốt 2026-07-25). Đã tự mở file xác nhận từng số dòng.

| SRS yêu cầu (file:line) | Thực tế web (V1.0.5) | Đủ/Thiếu |
|---|---|---|
| Tab 5 có cột **STT · Họ tên · Email · Số điện thoại · Đơn vị** (`:1901`) | Có đủ 5 | ✅ |
| Tab 5 có cột **Đề kiểm tra** (`:1901`) | **KHÔNG có** | ❌ *(ngoài phạm vi case — xem §Phát hiện thêm)* |
| Tab 5 có cột **Điểm** (`:1901`) | Có — nhãn `Điểm kiểm tra` | ✅ |
| Tab 5 có cột **Xếp loại** auto BR-KQ-01 (`:1901`) | Có | ✅ |
| Tab 5 có cột **Kết quả** Đạt/Không đạt auto BR-KQ-02 (`:1901`) | Có | ✅ |
| Tab 5 có cột **Ghi chú** (`:1901`) | Có (khuất 187px, hiện ra sau khi cuộn ngang) | ✅ |
| Tab 5 hiển thị **nhãn "Kết quả tạm tính"** khi khoá chưa `DA_KET_THUC` (`:1903`) | Có, nguyên văn khớp `:1903` | ✅ |
| Tab 4 có **bộ chọn buổi học** dạng Ngày · Khung giờ · Nội dung, KHÔNG date-picker (`:1897`) | Có — dropdown `10/05/2026 · 08:00:00-10:00:00 · Buổi 1 …` | ✅ |
| Tab 4 trạng thái rỗng *"Vui lòng chọn buổi học để bắt đầu điểm danh"* (`:1898`) | Có, đúng nguyên văn | ✅ |
| Tab 4 có cột **Trạng thái điểm danh** 3 giá trị (`:1896`) | Có — `Có mặt` / `Vắng có phép` / `Vắng không phép` | ✅ |
| **[đối tác đòi]** Hiển thị **Số buổi có mặt** — SRS đặt ở **Outputs UC24 `:600`**, KHÔNG đặt ở cột Tab 5 `:1901` cũng KHÔNG ở cột Tab 4 `:1896` | Không có cột riêng ở cả 2 tab. **Có** trong file DOCX xuất (cột `Số buổi có mặt`) và trong API `/ket-quas` (`soBuoiCoMat`) | ⚠️ đáp ứng **cách khác** |
| **[đối tác đòi]** **Số buổi vắng có phép** — Outputs UC24 `:601` | **Không có ở đâu**: không ở Tab 4/Tab 5, không ở DOCX xuất, không có field tương ứng trong API `/ket-quas` | ❌ |
| **[đối tác đòi]** **Số buổi vắng không phép** — Outputs UC24 `:602` | **Không có ở đâu** (như trên) | ❌ |
| **[đối tác đòi]** **Tổng số buổi** — Outputs UC24 `:603` | Không có cột riêng ở 2 tab. **Có** trong DOCX (cột `Tổng số buổi`) + API (`tongBuoi`); trên UI gộp vào mẫu số ô `Chuyên cần` | ⚠️ đáp ứng **cách khác** |
| **[liên quan]** **% chuyên cần** `ty_le_chuyen_can` — Outputs UC24 `:604`, đầu vào BR-KQ-02 `:2251` | Có — hiện trong ngoặc ô `Chuyên cần`, DOCX có cột `Tỉ lệ chuyên cần (%)`, API `tyLeChuyenCan` | ✅ |

### Trích nguyên văn SRS đã xác minh

- `srs-fr-03-dao-tao.md:517` — `### FR-III-05: Quản lý kiểm tra, đánh giá kết quả (UC24)`
- `srs-fr-03-dao-tao.md:519` — `**UC Reference:** UC 24 | **Priority:** Essential | **Stability:** High`
- `srs-fr-03-dao-tao.md:520` — `**Màn hình:** SCR-III-02 (chi tiet Khoa hoc — Tab 3 "Lich hoc & Diem danh" + Tab 4 "Ket qua kiem tra")`
  ⚠️ Dòng này đánh số tab **cũ/lệch** (Tab 3/Tab 4). SCR-III-02 hiện hành dùng Tab 4 = Điểm danh, Tab 5 = Kết quả kiểm tra. Khi log/quote phải dùng `:1896` / `:1901`.
- `srs-fr-03-dao-tao.md:600`–`:603` — bảng **Outputs** của FR-III-05:
  `| 6 | so_buoi_co_mat | number | Số buổi có mặt (CO_MAT) |`
  `| 7 | so_buoi_vang_phep | number | Số buổi vắng có phép (VANG_PHEP) |`
  `| 8 | so_buoi_vang_khong_phep | number | Số buổi vắng không phép (VANG_KHONG_PHEP) |`
  `| 9 | tong_buoi | number | Tổng số buổi |`
- `srs-fr-03-dao-tao.md:1896` — Tab 4 Điểm danh: `Cột STT · Họ tên · Email · Số điện thoại · Đơn vị · Buổi học (FK lich_hoc_id) · Trạng thái điểm danh (Có mặt / Vắng có phép / Vắng không phép — enum 3 trạng thái) · Ghi chú.`
- `srs-fr-03-dao-tao.md:1901` — Tab 5 Kết quả kiểm tra: `Cột STT · Họ tên · Email · Số điện thoại · Đơn vị · Đề kiểm tra · Điểm · Xếp loại (Giỏi/Khá/Trung bình/Không đạt — auto BR-KQ-01) · Kết quả (Đạt/Không đạt — auto BR-KQ-02) · Ghi chú.`
- `srs-fr-03-dao-tao.md:2251` — `ty_le_chuyen_can` = (số buổi Có mặt + số buổi Vắng có phép) / tổng số buổi × 100
- `srs-fr-03-dao-tao.md:628`–`:637` — Acceptance Criteria FR-III-05: **không có** AC nào bắt Tab 5 hiển thị 4 trường chuyên cần.

## Đo trên web — số liệu thô

Bộ cột đọc từ `.ant-tabs-tabpane-active` (không lấy toàn trang, vì AntD giữ mount cả tabpanel ẩn):

| Tab | Số cột | Danh sách |
|---|:-:|---|
| Kết quả (`?tab=ket-qua-kiem-tra`) | **10** | STT · Họ tên · Email · Số điện thoại · Đơn vị · **Chuyên cần** · Điểm kiểm tra · Kết quả · Xếp loại · Ghi chú |
| Điểm danh (`?tab=lich-hoc-diem-danh`) | **7** | STT · Họ tên · Email · Số điện thoại · Đơn vị · Trạng thái · Ghi chú |

- Tab Kết quả: `scrollWidth 1315` / `clientWidth 1128` → khuất 187px; đã cuộn hết phải, cột khuất duy nhất = `Ghi chú`.
- Tab Điểm danh: `scrollWidth 1141` / `clientWidth 1136` → khuất 5px, không có cột ẩn.
- Bất biến theo trạng thái: đo thêm `KH-SEED-0001` (Đã kết thúc) và `AAA-KH-TW` (Hoàn thành) — **cùng đúng 10 cột đó**.

Nội dung file DOCX xuất từ tab Kết quả (`POST /api/v1/khoa-hocs/{id}/ket-quas/export-docx` → 200; giải nén `word/document.xml` đọc text, **không** chỉ dựa vào HTTP 200):

```
STT | Họ và tên | Email | Số điện thoại | Đơn vị | Số buổi có mặt | Tổng số buổi |
Tỉ lệ chuyên cần (%) | Điểm kiểm tra | Kết quả | Xếp loại | Ghi chú
```

→ File xuất **có** `Số buổi có mặt` + `Tổng số buổi`, **không có** `Số buổi vắng có phép` / `Số buổi vắng không phép`.

API `GET /api/v1/khoa-hocs/{id}/ket-quas` trả mỗi học viên: `soBuoiCoMat`, `tongBuoi`, `tyLeChuyenCan`, `diemKiemTra`, `ketQua`, `xepLoai`, `ghiChu` — **không có** field vắng có phép / vắng không phép.

## Vì sao `BA confirm` (không phải `Reject`, không phải `Open`)

1. **Không `Open`:** không có dòng SRS nào quy định Tab 5 (hoặc Tab 4) phải có 4 cột đó. Đặc tả cột của cả 2 tab (`:1896`, `:1901`) là danh sách liệt kê đầy đủ và **không** chứa chúng; `:628`–`:637` cũng không có AC nào đòi. Chấm theo đặc tả màn hình thì app **không sai**.
2. **Không `Reject`:** kỳ vọng của đối tác **có điểm tựa hợp lệ trong chính SRS** — bảng **Outputs của UC24** (`:600`–`:603`) liệt kê đủ 4 trường, mà `:520` gắn UC24 cho đúng 2 tab này. Đây là **bất đồng về ĐẶC TẢ**, không phải đối tác thao tác/hiểu sai. Protocol §Verdict ghi rõ: *"KHÔNG dùng `Reject` cho bất đồng kỳ vọng vs SRS (dù web đúng SRS)"*.
3. **SRS tự mâu thuẫn:** 4 trường vừa là Outputs bắt buộc của UC24, vừa không xuất hiện trong đặc tả cột của bất kỳ tab nào thuộc UC đó. Riêng `so_buoi_vang_phep` / `so_buoi_vang_khong_phep` hiện **không tồn tại ở bất kỳ bề mặt nào** (UI, file xuất, API) — tức Output `:601`/`:602` chưa được đáp ứng theo bất kỳ cách nào. Cần BA chốt.

## Câu hỏi cho BA

1. Bốn trường `so_buoi_co_mat` / `so_buoi_vang_phep` / `so_buoi_vang_khong_phep` / `tong_buoi` (Outputs UC24, `srs-fr-03-dao-tao.md:600`–`:603`) **có bắt buộc hiển thị thành cột trên Tab 5 "Kết quả kiểm tra"** không? (có/không)
2. Nếu **không** — danh sách cột tại `:1901` có phải danh sách **đóng** (app hiện đủ là đạt) không? (có/không)
3. Việc app gộp `so_buoi_co_mat` + `tong_buoi` + `ty_le_chuyen_can` vào **một ô `Chuyên cần` dạng `x/y (z%)`** có được chấp nhận thay cho 3 cột riêng không? (có/không)
4. Hai trường `so_buoi_vang_phep` (`:601`) và `so_buoi_vang_khong_phep` (`:602`) hiện **không có ở bất kỳ đâu** (không ở 2 tab, không ở file DOCX xuất, không ở API kết quả). BA xác nhận **cần bổ sung** hay **gỡ khỏi Outputs UC24**? (bổ sung / gỡ)
5. Dòng `:520` đang đánh số tab lệch (Tab 3 / Tab 4) so với SCR-III-02 (Tab 4 / Tab 5) — BA xác nhận `:520` là dòng cũ cần sửa? (có/không)

## Phát hiện thêm ngoài phạm vi case (dựa trên đo thực, không suy đoán)

### 1. `Tổng số buổi` đếm sai ⇒ tỷ lệ chuyên cần sai ⇒ ảnh hưởng kết quả Đạt/Không đạt — **ĐÃ LOG**

Khoá `KH-QAW7-HOINGHI` có **3 buổi** trong tab Lịch học (API `/lich-hocs` trả 3), mới điểm danh **1 buổi**. Cả 3 bề mặt đo đều trả `tongBuoi = 1`:

| Bề mặt đo | Học viên "Vắng có phép" | Học viên "Có mặt" |
|---|---|---|
| UI tab Kết quả, ô `Chuyên cần` | `0/1 (100.00%)` | `1/1 (100.00%)` |
| File DOCX xuất (cột Tổng số buổi / Tỉ lệ) | `0` · `1` · `100.00` | `1` · `1` · `100.00` |
| API `GET /ket-quas` | `soBuoiCoMat:0, tongBuoi:1, tyLeChuyenCan:"100.00"` | `soBuoiCoMat:1, tongBuoi:1, tyLeChuyenCan:"100.00"` |

Theo `srs-fr-03-dao-tao.md:2251`, mẫu số phải là **tổng số buổi của khoá (3)**, nên đúng ra cả 2 học viên đều `33.33%`. Mẫu số đang là *số buổi đã có bản ghi điểm danh*. Hệ quả: học viên mới dự 1/3 buổi đã đạt 100% chuyên cần → vượt ngưỡng `ty_le_chuyen_can_toi_thieu` (mặc định 80%, `:2252`) → BR-KQ-02 kết luận **Đạt** sai.

Đã đo bằng **3 phương pháp độc lập** (UI render · file DOCX do server sinh · API thô) → không phải lỗi phép đo. Ảnh đối tác chụp bản cũ cho `0/3 (33.33%)` — đúng công thức — nên đây là **hồi quy của bản V1.0.5**.

→ Đã mở dòng TC mới trên sheet để tới được dev (xem §Log ra sheet).

### 2. Tab "Kết quả" thiếu cột `Đề kiểm tra` — **CHƯA LOG, cần đo lần 2**

`:1901` liệt kê cột **Đề kiểm tra**; bản V1.0.5 không có cột này ở cả 3 khoá đã mở. Nhưng cả 3 khoá đó **đều chưa gán đề kiểm tra** nào, nên chưa loại trừ được khả năng cột chỉ render khi khoá có đề. Theo quy tắc *"bug candidate ≠ bug — đo lại bằng phương pháp thứ hai"*, chưa log; cần gán 1 đề vào khoá rồi đo lại.

### 3. `Xếp loại` có giá trị khi `Điểm kiểm tra` trống — **KHÔNG log**

Trên `AAA-KH-TW` (Hoàn thành) và `KH-SEED-0001` (Đã kết thúc), nhiều dòng có `Điểm kiểm tra` trống nhưng `Xếp loại` = `Giỏi`/`Khá` và `Kết quả` = `Không đạt`. Trên dữ liệu **mới tạo** ở `KH-QAW7-HOINGHI` thì hành vi đúng (`diemKiemTra:null` → `xepLoai:null`, `ketQua:null`). Nhiều khả năng là giá trị có sẵn của dữ liệu seed cũ trong DB, không phải lỗi luồng tính. Không đủ căn cứ log.

## Log ra sheet

| Việc | Kết quả |
|---|---|
| Verdict case | `UAT_TGPL Doanh Nghiệp-tuần 2` **row 116** — cột Q (`Verify`) `'' → 'BA confirm'`, cột R ghi note QA (2218 ký tự). Cột P giữ nguyên `Reject` của dev. Ghi lúc `2026-08-03T15:43:43` bằng `sheet_write.py --mode qaverdict` (đã đọc lại xác nhận). |
| Bug phát hiện thêm (mục 1) | Đã mở dòng TC mới **row 130**, mã **`KTDGKQHT_20`**, `Trạng thái 1 = Fail`, bằng `tools/sheet_add_bug_row.py` (11 ô, đã đọc lại xác nhận). |

## ⚠️ Dữ liệu đã thay đổi trong phiên này (để phiên sau biết)

Khoá **`KH-QAW7-HOINGHI`** (`a7480002-0000-4000-8000-000000000002`, Đang diễn ra, Cục Bổ trợ tư pháp) trước phiên này **có 0 buổi học** và **chưa điểm danh**. Đã seed:

- Thêm **3 buổi** vào tab Lịch học: `10/05/2026 08:00–10:00`, `10/05/2026 14:00–16:00`, `11/05/2026 08:00–10:00` (nội dung `Buổi N - QA seed KTDGKQHT_02`, địa điểm `Phòng họp A - QA seed`).
- Điểm danh **buổi 1**: `QA R3 Mailto Ba` = **Vắng có phép**, `QA R3 Mailto Hai` = **Có mặt**.

Không xoá/đổi dữ liệu nào khác. Khoá `DDD-KH-011` (Đang diễn ra, 1 học viên) **không dùng được** cho vai trò `CB_NV_TW`: thuộc đơn vị khác (`donViId …8001-…`), bấm tab Lịch học → điều hướng sang `/403`, API `/lich-hocs` trả 403.

## File bằng chứng

| Loại | Đường dẫn |
|---|---|
| Ảnh đối tác — tab Kết quả (ảnh lỗi) | `partner-evidence/KTDGKQHT_02_v2-2.jpg` |
| Ảnh đối tác — tab Điểm danh | `partner-evidence/KTDGKQHT_02_v2-1.jpg` |
| Crop bảng tab Kết quả (zoom) | `frames/KTDGKQHT_02/crop-ketqua-table.png` · `crop-ketqua-right.png` |
| **Web — tab Kết quả, khoá Đang diễn ra** | `image/KTDGKQHT_02-web-tab-ketqua-dangdienra.png` |
| **Web — tab Kết quả, đã cuộn hết phải (lộ cột Ghi chú)** | `image/KTDGKQHT_02-web-tab-ketqua-cuonhet-phai.png` |
| Web — seed buổi học (1 request / 1 thông báo) | `image/KTDGKQHT_02-seed-buoi1-toast.png` |
| Web — tab Điểm danh sau khi lưu điểm danh | `image/KTDGKQHT_02-seed-luu-diemdanh.png` |
| Trích SRS | `srs/KTDGKQHT_02-srs.md` |
| Bảng đối chiếu điều kiện | `cond/KTDGKQHT_02.md` |
