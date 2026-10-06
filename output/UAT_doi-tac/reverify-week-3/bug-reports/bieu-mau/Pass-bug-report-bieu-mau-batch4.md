# Bug Report — Biểu mẫu (Batch 4 · QLBMHD — Tạo mới + Upload/Validation, rows 97–104)

| Thông tin | Giá trị |
|-----------|---------|
| **Dự án** | PM HTPLDN — Verify bug đối tác (UAT tuần 3) |
| **Môi trường** | https://18.143.165.120.nip.io/ |
| **Người test** | QA Automation (Claude Code) |
| **Ngày** | 2026-07-22 16:20:00 |
| **Loại test** | Functional — re-verify sau dev fix (vòng 2) |
| **Round** | Reverify week-3 — Batch 4 · R2 (2/2 bug PASS → Closed) |
| **Tài liệu tham chiếu** | `srs-v3.5/srs-fr-09-bieu-mau.md` (FR-VII-04 / UC95 / SCR-VII-02) |

---

## Tổng hợp

Verify Batch 4 (QLBMHD tạo mới + upload/validation, rows 97–104). Bug Open có SRS reference cụ thể liệt kê ở Bug Summary Table dưới.

> Các case khác (Reject / BA confirm / ô TRỐNG) không nằm ở đây — xem `../../ba-confirm/bieu-mau/ba-confirmation-needed-week-3-bieu-mau-batch4.md` + audit `reverify-audit/<mã TC>/`.

### Severity breakdown

| Tổng | Critical | Major | Medium | Minor | Trivial | Closed | Open |
|------|----------|-------|--------|-------|---------|--------|------|
| 2    | 0        | 0     | 2      | 0     | 0       | 2      | 0    |

> **QLBMHD_08 (không quét virus file đính kèm — rủi ro bảo mật):** verdict **BA confirm** (chờ Dev/Security xác nhận pipeline AV) → chi tiết ở `../../ba-confirm/bieu-mau/ba-confirmation-needed-week-3-bieu-mau-batch4.md` mục QLBMHD_08, KHÔNG log Open ở đây.

## Bug Summary Table

| Bug ID | Severity | Priority | Type | TC Ref | **SRS Reference** | Title | Status |
|--------|----------|----------|------|--------|-------------------|-------|--------|
| ~~BUG-QLBMHD_03~~ | Medium | P2 | UI/UX | QLBMHD_03 | `SCR-VII-02 #21` (`srs-fr-09:658`) | Form Thêm/Sửa biểu mẫu thiếu trường "Cơ quan ban hành" (read-only auto theo SRS) | Closed |
| ~~BUG-QLBMHD_02~~ | Medium | P2 | UI/UX | QLBMHD_02 | `SCR-VII-02 #20` (`srs-fr-09:657`) | Danh sách biểu mẫu thiếu cột "Cơ quan ban hành" (SRS quy định luôn hiển thị) | Closed |

---

## ~~BUG-QLBMHD_02~~ [CLOSED] — Danh sách biểu mẫu thiếu cột "Cơ quan ban hành"

> **Re-test:** 2026-07-22 R2 (reverify-week-3) — ✅ PASS. Login `cbnv_tw_03` (CB_NV_TW, BTP·TW) → `/bieu-mau/danh-sach`: header nay 12 cột (trước 11), có cột **"Cơ quan ban hành"** ở vị trí #5, hiển thị tên đơn vị ban hành thực cho 8/8 dòng ("Cục Bổ trợ tư pháp - Bộ Tư pháp", "Bộ Kế hoạch và Đầu tư"). Khớp KQ mong đợi (SCR-VII-02 #20). Bằng chứng: `image/BUG-QLBMHD_02-retest-pass.png`.

### Mô tả

Trên màn **Danh sách biểu mẫu** (`/bieu-mau/danh-sach`), bảng danh sách KHÔNG có cột **"Cơ quan ban hành"**. Theo SRS SCR-VII-02 (`srs-fr-09:657`), cột "Cơ quan ban hành" (tên đơn vị ban hành, `don_vi_id → DON_VI`) phải **luôn hiển thị** trong danh sách. Web hiện có 11 cột nhưng thiếu cột này.

### Các bước tái hiện

1. Đăng nhập role **CB Nghiệp vụ - Trung ương** (`cbnv_tw`, quyền "Quản lý biểu mẫu" theo FR-VII-04, đơn vị BTP·TW — vai trò NV phạm vi toàn quốc, rộng nhất trong các role NV).
2. Vào **Biểu mẫu → Danh sách biểu mẫu** (`/bieu-mau/danh-sach`).
3. Quan sát tiêu đề các cột của bảng danh sách (trích DOM `table thead th`).
4. Quan sát: không có cột "Cơ quan ban hành".

### Kết quả mong đợi

- Theo SRS `srs-fr-09-bieu-mau.md:657` (SCR-VII-02 thành phần #20 — "Cột Cơ quan ban hành … luôn hiển thị `[STT12]`"): danh sách biểu mẫu phải có cột "Cơ quan ban hành" hiển thị tên đơn vị ban hành.

### Kết quả thực tế

- Danh sách có 11 cột, KHÔNG có "Cơ quan ban hành": `Mã BM · Tên biểu mẫu · Loại TL · Thư mục · Kích thước · Trạng thái · Đã công khai · Ảnh đại diện · Ngày tạo · Sync Cổng · Hành động`.
- Bộ lọc "Định dạng" (đối tác cũng phản ánh) thực tế **CÓ** trên thanh lọc → không thiếu; "ô chọn biểu mẫu" (checkbox chọn dòng) SRS không quy định cho màn biểu mẫu → tách sang BA confirm.

### Bằng chứng

![BUG-QLBMHD_02 — Danh sách biểu mẫu thiếu cột Cơ quan ban hành; filter Định dạng có mặt](image/BUG-QLBMHD_02-danhsach-cot.png)

```json
// DOM: [...document.querySelectorAll('table thead th')].map(th=>th.innerText.trim())
["Mã BM","Tên biểu mẫu","Loại TL","Thư mục","Kích thước","Trạng thái","Đã công khai","Ảnh đại diện","Ngày tạo","Sync Cổng","Hành động"]
```

---

## ~~BUG-QLBMHD_03~~ [CLOSED] — Form Thêm/Sửa biểu mẫu thiếu trường "Cơ quan ban hành" (read-only)

> **Re-test:** 2026-07-22 R2 (reverify-week-3) — ✅ PASS. Login `cbnv_tw_03` (CB_NV_TW, BTP·TW) → `/bieu-mau/them-moi`: form nay CÓ trường **"Cơ quan ban hành"** (input `disabled` = read-only) auto điền value **"Cục Bổ trợ tư pháp - Bộ Tư pháp"** (đúng đơn vị tài khoản). Trường hiển thị ở CẢ 2 trạng thái switch "Công khai trên Cổng PLQG" (OFF và ON). Giá trị persist được xác nhận qua cột "Cơ quan ban hành" ở danh sách (BUG-QLBMHD_02). Khớp KQ mong đợi (SCR-VII-02 #21 + Inputs #14). Bằng chứng: `image/BUG-QLBMHD_03-retest-pass.png`.

### Mô tả

Trên form **Thêm biểu mẫu** (`/bieu-mau/them-moi`), KHÔNG có trường **"Cơ quan ban hành"** (read-only, auto = đơn vị của tài khoản đăng nhập). Trường thiếu cả khi switch "Công khai trên Cổng PLQG" tắt lẫn bật. Theo SRS SCR-VII-02 #21 (`srs-fr-09:658`) + Inputs #14 (`srs-fr-09:304`), form tạo/sửa biểu mẫu phải hiển thị trường "Cơ quan ban hành" read-only.

### Các bước tái hiện

1. Đăng nhập role **CB Nghiệp vụ - Trung ương** (`cbnv_tw`, quyền "Quản lý biểu mẫu" theo FR-VII-04, đơn vị BTP·TW).
2. Vào **Biểu mẫu → Danh sách biểu mẫu → + Thêm biểu mẫu** (`/bieu-mau/them-moi`).
3. Quan sát các trường của form (label). Bật switch "Công khai trên Cổng PLQG" → quan sát phần "Nội dung công khai".
4. Quan sát: không có trường "Cơ quan ban hành" ở bất kỳ vị trí nào của form.

### Kết quả mong đợi

- Theo SRS `srs-fr-09-bieu-mau.md:658` (SCR-VII-02 #21 — "form / Cơ quan ban hành / text (read-only) / Auto = đơn vị tài khoản / khi tạo/sửa `[STT12]`") + `:304` (Inputs #14 — co_quan_ban_hanh bắt buộc, auto, read-only): form phải hiển thị trường "Cơ quan ban hành" read-only để người dùng thấy đơn vị ban hành sẽ được ghi.

### Kết quả thực tế

- Form có các trường: Thư mục, Tên biểu mẫu, Lĩnh vực, Loại hình, Mô tả, Thứ tự hiển thị, File biểu mẫu; khi bật Công khai thêm: Ảnh đại diện, Mô tả công khai, File đính kèm công khai. **KHÔNG có "Cơ quan ban hành"** (`hasCoQuanBanHanh=false` khi kiểm toàn bộ text form).
- Ghi chú ý phụ (đối tác cũng phản ánh): trường **File đính kèm công khai** hiện chỉ nhận `.pdf,.doc,.docx,.xls,.xlsx` (đúng SRS #19) — lỗi "cho phép .jpg/.png/.gif" đối tác báo KHÔNG tái hiện trên build này (Reject ý phụ).

### Bằng chứng

![BUG-QLBMHD_03 — Form Thêm biểu mẫu (Công khai ON): có Ảnh đại diện/Mô tả công khai/File đính kèm công khai, KHÔNG có trường Cơ quan ban hành](image/BUG-QLBMHD_03-form-congkhai.png)

```json
// DOM form them-moi, switch Công khai ON (evaluate_script)
{"hasCoQuanBanHanh": false,
 "labels": ["Thư mục","Tên biểu mẫu","Lĩnh vực","Loại hình","Mô tả","Thứ tự hiển thị","File biểu mẫu","Nội dung công khai trên Cổng PLQG","Công khai trên Cổng PLQG","Ảnh đại diện","Mô tả công khai","File đính kèm công khai"],
 "fileInputs_accept": [{"File biểu mẫu":".doc,.docx,.xls,.xlsx"},{"Ảnh đại diện":".jpg,.png,.gif"},{"File đính kèm công khai":".pdf,.doc,.docx,.xls,.xlsx"}]}
```

---

## Phụ lục — Môi trường test

| Thành phần | Giá trị |
|------------|---------|
| URL ứng dụng | https://18.143.165.120.nip.io/ |
| OTP login | MailHog (http://18.143.165.120:8025) |
| Tool test | Chrome DevTools MCP |
| Tài khoản | `cbnv_tw` / CB Nghiệp vụ - Trung ương (BTP·TW) |

---

*Bug report generated: 2026-07-20 22:20:00 | QA Automation via Claude Code*
