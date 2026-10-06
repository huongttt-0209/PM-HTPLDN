# Chuẩn đối chiếu — Cụm A (9 case xuất Excel báo cáo thống kê)

> **File này KHÔNG chứa verdict.** Chỉ là chuẩn để agent đo đối chiếu. Verdict do agent đo ra sau khi đo thật.
>
> **Nguồn đặc tả duy nhất của lô:** `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/`
> — file chính `srs-fr-11-bao-cao.md` (**1.295 dòng**, mtime 06/08/2026 22:52), phụ trợ `srs-v3.5.md` (7.012 dòng).
> **Mọi số dòng dưới đây do chính lượt này mở file đọc lại ngày 2026-08-07** (Read/grep -n), không lấy từ trí nhớ,
> không lấy từ phiếu UAT, không lấy từ thư BA.

---

## 🔴 CẢNH BÁO SỐ 1 — SỐ DÒNG TRONG BRIEF/PHIẾU BA ĐÃ LỆCH, ĐỪNG QUOTE LẠI

`srs-fr-11-bao-cao.md` đã được **sửa ngày 06/08/2026** để áp kết luận BA (thêm bước kiểm vai trò, thêm mã lỗi
`ERR-RPT-08`, thêm 2 tiêu chí chấp nhận, thêm ghi chú điều kiện vào màn). Việc chèn dòng làm **trôi số dòng**
của phần §3 Màn hình. Bảng đối chiếu — **cột phải là số ĐANG ĐÚNG hôm nay**:

| Nội dung | Brief / phiếu BA ghi | **Số dòng THẬT (đọc 2026-08-07)** | Lệch |
|---|---|---|---|
| Nút **Xem báo cáo** | `:1051` | **`:1056`** | +5 |
| Nút **Xuất Excel** | `:1052` | **`:1057`** | +5 |
| Nút **Xuất PDF** | `:1053` | **`:1058`** | +5 |
| UC124 `Donut + Trend` | `:1064` | **`:1069`** | +5 |
| UC125 `Bar + Trend` | `:1065` | **`:1070`** | +5 |
| UC127 `Bar + Donut` | `:1067` | **`:1072`** | +5 |
| `theo_linh_vuc[]` "Luôn" của UC125 | `:215` | **`:218`** | +3 |
| Quy tắc tương tác — header tệp xuất | `:1092` | **`:1097`** | +5 |
| Dòng "QTHT bypass" của BR-AUTH-08 | `:1268` | **`:1273`** (và **nội dung đã ĐẢO**, xem cảnh báo 2) | +5 |
| Ma trận quyền — dòng `BAO_CAO` | `srs-v3.5.md:1335` | **`srs-v3.5.md:1339`** | +4 |

**Các số dòng brief nêu mà VẪN đúng nguyên (đã kiểm từng dòng):** `:51`, `:62`, `:79`, `:85`, `:117`,
`srs-v3.5.md:684`.

---

## 🔴 CẢNH BÁO SỐ 2 — DÒNG "QTHT BYPASS" ĐÃ ĐƯỢC GỠ, KHÔNG CÒN MÂU THUẪN NỘI TẠI

Brief hỏi: dòng `:1268` "QTHT bypass" còn hay đã gỡ. **Trả lời: ĐÃ GỠ và viết ngược lại.** Nguyên văn dòng
hiện hành:

> `srs-v3.5/srs-fr-11-bao-cao.md:1273` — *"| BR-AUTH-08 | chính sách phân quyền áp dụng cho MỌI bảng có cột
> `don_vi_id`. TW thấy toàn quốc, BN thấy BN, ĐP thấy ĐP | Architecture AD-07 | Toàn bộ FR-IX | — (QTHT **không
> phải tác nhân của nhóm IX** nên không có ca bypass ở đây; ngoại lệ QTHT của BR-AUTH-08 chỉ áp cho các nhóm mà
> QTHT là tác nhân) `[BA chốt 2026-08-06]` | Verify phân quyền |"*

⇒ **Đặc tả hiện KHÔNG còn tự mâu thuẫn.** Toàn bộ 7 việc trong "Phương án xử lý" mục 5 của phiếu BA đã được
áp vào file (kiểm từng chỗ, xem §3 dưới). Agent đo **không được** dùng lập luận "SRS có ngoại lệ QTHT bypass"
để nới quyền — lập luận đó lấy từ bản SRS trước 06/08 và nay đã sai.

---

## 0. Điều kiện phải dựng lại

| Hạng mục | Yêu cầu | Căn cứ / ghi chú |
|---|---|---|
| **Vai trò vế (a) — xuất được** | `cbnv_tw_04` (`CB_NV_TW`) hoặc `cbpd_tw_04` (`CB_PD_TW`), mật khẩu `Test@1234` | Tác nhân đích danh `srs-fr-11-bao-cao.md:51` + `:62`. Bộ **04** theo brief. Cấp TW để thấy Toàn quốc (`:45`) → dễ có dữ liệu |
| **Vai trò vế (b) — phải bị chặn** | `admin` / `Secret@123` (QTHT, **không có biến thể `_04`**) | Đúng vai trò trong 10/10 ảnh đối tác. Không có tài khoản QTHT nào khác để fallback |
| **State entity** | KHÔNG cần dựng state — báo cáo là read-only (`:105` — *"Không thay đổi dữ liệu nghiệp vụ (read-only)"*) | Không tạo/sửa/xoá bản ghi nào trong lượt đo |
| **Dữ liệu tiền đề** | Mỗi loại BC phải có **≥1 dòng dữ liệu** trong kỳ đã chọn, nếu không nút Xuất tự tắt và phép đo vô nghĩa | `:1057` điều kiện *"Sau khi đã Xem báo cáo"*; `:113` INF-RPT-01 *"Không có dữ liệu báo cáo cho kỳ và đơn vị đã chọn"*. Lượt 06/08 dựng được đủ 9/9 loại với **Kỳ = Năm 01/01–31/12/2026, Đơn vị = Toàn quốc** |
| **Chỉ đọc, chỉ tính bản ghi đã duyệt** | Số liệu chỉ gồm bản ghi đã duyệt / hoàn thành / đã thanh toán | `:82` — *"Truy vấn dữ liệu: CHỈ bản ghi đã duyệt (trạng thái đã duyệt / hoàn thành / đã thanh toán)"* (BR-RPT-01) |
| **Bản dựng** | Ghi nhãn bản dựng ở chân giao diện **trước** mỗi case; **tải lại trang bằng địa chỉ** trước khi verify bản fix | Luật chung lô §3. Lượt 06/08 đo trên **V1.0.8** |
| **Môi trường** | `https://18.143.165.120.nip.io` (nội bộ), MailHog `http://18.143.165.120:8025` | Brief §Tham số đợt. **Không** phải env đối tác `ospgroup.vn` → verdict phải ghi câu giới hạn hiệu lực |

**Bẫy tiền đề đã ghi nhận (lượt 06/08, ngoài phạm vi 9 case này nhưng làm hỏng phép đo):**
bấm **[Xem báo cáo] từ 2 lần trở lên** thì hai nút Xuất bị khoá cả phiên (đã tách phiếu riêng `BCTK_QA07`,
dòng 370). ⇒ Mỗi lượt đo: **tải lại trang → chọn bộ lọc → bấm [Xem báo cáo] đúng 1 lần → bấm Xuất**.

---

## 1. VIỆC 1 — Bảng ánh xạ Mã TC → màn báo cáo

Tất cả 9 case dùng **cùng một màn** `SCR-IX-01` (`srs-fr-11-bao-cao.md:1034`) — *"Một trang báo cáo thống nhất
cho tất cả 23 loại BC"* (`:1042`). Khác nhau ở **giá trị chọn trong dropdown loại BC** (`:1052`).

Cột "Tên báo cáo trên giao diện" lấy **đúng chữ** từ cột *Tên hiển thị* của bảng "Mapping 23 loại BC trong
Dropdown" (`:1067–1091`) — đây là chữ mà đặc tả quy định cho chính ô dropdown đó.

| Mã TC | Dòng sheet | Tên báo cáo trên giao diện (đúng chữ SRS) | Mã FR / UC | Dòng SRS |
|---|---|---|---|---|
| `VVDTN_06` | 179 | **BC Vụ việc đã tiếp nhận** | FR-IX-02 / UC125 | tên dropdown `:1070` · mục FR `:184` · Tác nhân `:195` |
| `VVDHT_06` | 185 | **BC Vụ việc đang hỗ trợ** | FR-IX-03 / UC126 | tên dropdown `:1071` · mục FR `:228` · Tác nhân `:239` |
| `VVDHTHT_06` | 189 | **BC Vụ việc đã hoàn thành** | FR-IX-04 / UC127 | tên dropdown `:1072` · mục FR `:273` · Tác nhân `:284` |
| `VVTTG_05` | 195 | **BC Vụ việc theo thời gian** | FR-IX-05 / UC128 | tên dropdown `:1073` · mục FR `:317` · Tác nhân `:328` |
| `VVTDVQL_06` | 222 | **BC Vụ việc theo đơn vị quản lý** | FR-IX-11 / UC134 | tên dropdown `:1079` · mục FR `:559` · Tác nhân `:570` |
| `VVTLV_05` | 226 | **BC Vụ việc theo lĩnh vực** | FR-IX-12 / UC135 | tên dropdown `:1080` · mục FR `:596` · Tác nhân `:607` |
| `VVTLHDN_05` | 230 | **BC Vụ việc theo loại hình DN** | FR-IX-13 / UC136 | tên dropdown `:1081` · mục FR `:629` · Tác nhân `:640` |
| `VVTTGCT_05` | 234 | **BC Vụ việc theo thời gian chi tiết** | FR-IX-14 / UC137 | tên dropdown `:1082` · mục FR `:668` · Tác nhân `:679` |
| `CPCTHTTTG_05` | 263 | **BC Chi phí theo thời gian** | FR-IX-19 / UC142 | tên dropdown `:1087` · mục FR `:849` · Tác nhân `:860` |

**Suy luận tiền tố → tên, và bằng chứng xác nhận:**

- `VVTTGCT` — brief đặt dấu hỏi *"theo tổ chức/thời gian chi tiết?"*. **Đúng là "theo thời gian chi tiết"**,
  không có chữ "tổ chức". Hai bằng chứng độc lập: (1) SRS chỉ có đúng một BC vụ việc mang chữ "chi tiết" —
  `:1082` UC137 *"BC Vụ việc theo thời gian chi tiết"*; (2) lượt đo 06/08 xuất ra tệp
  `BaoCaoVuViecTheoTgChiTiet_20260806_1307.xlsx` (ô Kết quả verify dòng 234).
- `CPCTHTTTG` = "Chi phí Chi Trả Hỗ Trợ Theo Thời Gian". Nhóm Chi phí có **5** loại (UC138–UC142). Chốt là
  **UC142** vì: (1) ô Kết quả verify dòng 263 ghi thẳng *"BC Chi phí theo thời gian · Kỳ Năm 2026"*;
  (2) tệp lượt đó là `BaoCaoChiPhiTheoThoiGian_…`. ⚠️ **Điểm agent đo tự xác nhận trên màn:** dropdown còn có
  **UC138 "BC Chi phí chi trả hỗ trợ"** (`:1083`) — tên này cũng khớp một phần tiền tố. Mở dropdown, **đọc đủ
  cả 5 tên nhóm Chi phí**, chọn đúng *"BC Chi phí theo thời gian"*, và **ghi lại tên đã chọn** vào note.

**Tên nhóm (optgroup) để tìm nhanh trong dropdown** (`:1069–1091`): 4 case đầu nằm ở optgroup **"Vụ việc"**;
4 case giữa nằm ở optgroup **"VV theo chiều phân tích"**; case cuối nằm ở optgroup **"Chi phí"**.

⚠️ **CHƯA XÁC MINH ĐƯỢC — agent đo phải tự xác nhận trên màn:** SRS quy định mỗi option hiển thị dạng
*"[Mã UC] Tên BC"* (`:1052`). Không có bằng chứng nào trong repo cho biết giao diện thật có in mã UC hay
không, cũng không biết giao diện có dùng **đúng từng chữ** tên trên hay dùng biến thể. **Chấm theo khái niệm
báo cáo, KHÔNG chấm theo từng chữ nhãn** — nhãn lệch chữ không phải nội dung 9 phiếu này.

---

## 2. VIỆC 2 — Chuẩn nội dung tệp xuất

### 2.1 Điều kiện hiển thị / bấm được của 3 nút

| Nút | Dòng | Nguyên văn cột "Điều kiện hiển thị" |
|---|---|---|
| **Xem báo cáo** | `srs-v3.5/srs-fr-11-bao-cao.md:1056` | *"**Chỉ với vai trò CB Nghiệp vụ / CB Phê duyệt** — vai trò khác không vào được màn này (M-05 ẩn mục menu) `[BA chốt 2026-08-06]`"* |
| **Xuất Excel** | `srs-v3.5/srs-fr-11-bao-cao.md:1057` | *"Sau khi đã \"Xem báo cáo\" **và người dùng có vai trò CB Nghiệp vụ hoặc CB Phê duyệt** `[BA chốt 2026-08-06]`"* |
| **Xuất PDF** | `srs-v3.5/srs-fr-11-bao-cao.md:1058` | *"Sau khi đã \"Xem báo cáo\" **và người dùng có vai trò CB Nghiệp vụ hoặc CB Phê duyệt** `[BA chốt 2026-08-06]`"* |

Và ghi chú phủ toàn bảng, đặt ngay trên bảng thành phần:

> `srs-v3.5/srs-fr-11-bao-cao.md:1046` — *"**Điều kiện vào màn — áp cho TOÀN BỘ bảng dưới đây** `[BA chốt
> 2026-08-06]`: người dùng phải có vai trò **Cán bộ Nghiệp vụ** hoặc **Cán bộ Phê duyệt** (TW/BN/ĐP). Vai trò
> khác — kể cả **Quản trị hệ thống** — **không vào được màn này**; mục menu \"Báo cáo thống kê\" bị **ẩn** theo
> quy ước M-05 (ẩn, không làm mờ). Cột \"Điều kiện hiển thị\" của từng dòng chỉ mô tả điều kiện **bổ sung**
> bên trong màn, luôn hiểu là đã thoả điều kiện vai trò này."*

⇒ Hệ quả cho phép đo: với `admin`/QTHT thì **không được có bước "bấm Xuất"** — nếu tới được nút Xuất thì
vế (b) đã hỏng từ trước đó rồi.

### 2.2 Khuôn tên tệp — SRS quy định gì, sheet ghi gì, lệch ở đâu

**SRS — 2 chỗ, thống nhất với nhau:**

> `srs-v3.5/srs-fr-11-bao-cao.md:85` — *"| 7 | Nếu xuất Excel: tạo file .xlsx (khổ A4, Times New Roman cỡ 13).
> Tên tệp `{TenBaoCao}_{YYYYMMDD_HHmm}.xlsx` theo **Phụ lục E §H8**; `{TenBaoCao}` là tên loại báo cáo
> `[BA chốt 2026-08-04, nâng thành quy ước chung 2026-08-06]` | — |"*

> `srs-v3.5/srs-fr-11-bao-cao.md:1097` — *"Export XLSX/PDF chèn tiêu đề BC + thông tin kỳ + đơn vị + ngày tạo
> vào header file. … Tên tệp cả hai định dạng theo **Phụ lục E §H8** — `{TenBaoCao}_{YYYYMMDD_HHmm}.{ext}`
> `[BA chốt 2026-08-04]`"*

**Quy ước gốc §H8** (`srs-v3.5/srs-v3.5.md:6760`), trích phần chịu lực:

> *"| **H8** | Tên tệp xuất thống nhất | Áp cho **tệp kết xuất dữ liệu** phần mềm sinh ra theo yêu cầu người
> dùng (xuất danh sách, xuất báo cáo), ở **mọi nhóm chức năng**. … **Khuôn:** `{TenTep}[_{DinhDanh}]_{YYYYMMDD_HHmm}.{đuôi}`.
> `{TenTep}` viết liền kiểu PascalCase, bỏ dấu tiếng Việt và bỏ mọi ký tự không phải chữ hoặc số (kể cả dấu
> gạch nối, dấu cách, dấu câu); dấu gạch dưới chỉ dùng để ngăn các đoạn. … Phần giờ-phút bắt buộc để xuất hai
> lần trong cùng ngày không đè tệp. Tổng độ dài tối đa **255 ký tự** … Trùng tên (hai lần xuất trong cùng phút)
> thì tự thêm hậu tố `_1`, `_2` … | BẮT BUỘC |"*

**4 điều kiện chấm được, rút từ hai trích trên:**

1. Có phần thời gian **đủ tới phút** (`YYYYMMDD_HHmm`) → xuất 2 lần trong cùng ngày **không đè tệp**.
2. Phần tên viết **liền, không dấu, chỉ chữ và số**; gạch dưới chỉ để ngăn đoạn.
3. Phần tên **phân biệt được loại báo cáo** — vì `:85` nói `{TenBaoCao}` *"là tên loại báo cáo"*.
4. Đuôi `.xlsx`.

🔴 **LỆCH — ghi rõ để đừng chấm Fail oan:** cột *Kết quả mong đợi* của sheet ở **dòng 222 · 226 · 230 · 234**
ghi `BaoCaoVuViec_{YYYYMMDD_HHmm}.xlsx` (một chuỗi **giống nhau cho 4 loại báo cáo khác nhau**), dòng **263**
ghi `BaoCaoChiPhi_{YYYYMMDD_HHmm}.xlsx`. Theo `:85` thì `{TenBaoCao}` phải là **tên loại báo cáo**, nên 4 loại
khác nhau bắt buộc ra 4 tên khác nhau — làm đúng chữ của sheet thì 4 tệp trùng tên, trái ngay điều kiện 3.
⇒ **Chuẩn chấm là SRS, không phải chuỗi trong sheet.** Không được Fail vì tên tệp dài hơn / cụ thể hơn chuỗi
sheet ghi.

🔴 **SRS KHÔNG chốt chuỗi cụ thể cho từng báo cáo.** Đã đọc trọn `:85`, `:86`, `:124`, `:125`, `:1097` và
§H8 — không chỗ nào liệt kê chuỗi thành phẩm cho 23 loại BC. Vậy **cấm chấm Fail vì chọn cách viết tắt nào**
(`BaoCaoVuViecTiepNhan` hay `BCVuViecDaTiepNhan` đều thoả H8). Tên các tệp phần mềm đã giao lượt 06/08 —
dùng làm **mốc đối chiếu hồi quy**, KHÔNG dùng làm tiêu chí chấm:

| Mã TC | Tệp phần mềm giao 06/08 (V1.0.8) |
|---|---|
| `VVDTN_06` | `BaoCaoVuViecTiepNhan_20260806_1254.xlsx` |
| `VVDHT_06` | `BaoCaoVuViecDangHoTro_20260806_1417.xlsx` |
| `VVDHTHT_06` | `BaoCaoVuViecHoanThanh_20260806_1301.xlsx` (6.990 byte) |
| `VVTTG_05` | `BaoCaoVuViecTheoThoiGian_20260806_1432.xlsx` |
| `VVTDVQL_06` | `BaoCaoVuViecTheoDonVi_20260806_1305.xlsx` (6.834 byte) |
| `VVTLV_05` | `BaoCaoVuViecTheoLinhVuc_20260806_1306.xlsx` (6.826 byte) |
| `VVTLHDN_05` | `BaoCaoVuViecTheoLoaiDn_20260806_1306.xlsx` (6.801 byte) |
| `VVTTGCT_05` | `BaoCaoVuViecTheoTgChiTiet_20260806_1307.xlsx` (6.638 byte) |
| `CPCTHTTTG_05` | `BaoCaoChiPhiTheoThoiGian_…xlsx` |

> ℹ️ Bối cảnh: tracker `tasks/srs-contradictions.md` (mục SRS-C-010, dòng 462) còn ghi phần mềm đặt tên
> `bao-cao-<slug>-YYYY-MM-DD.xlsx` — đó là hiện trạng **trước** bản V1.0.8, nay đã đổi. Đừng lấy dòng đó làm
> chuẩn. Phần **PDF theo khung TT 17/2025** của SRS-C-010 **vẫn Open** nhưng **ngoài phạm vi 9 case này** —
> 9 phiếu chỉ nói về **Xuất Excel**.

### 2.3 Header bắt buộc trong tệp

**Quy định trực tiếp cho tệp xuất** (`srs-v3.5/srs-fr-11-bao-cao.md:1097`):
*"Export XLSX/PDF chèn **tiêu đề BC + thông tin kỳ + đơn vị + ngày tạo** vào header file."*

⇒ **4 mục BẮT BUỘC phải đọc thấy trong tệp:**

| # | Mục | Đối chiếu với Output chung |
|---|---|---|
| 1 | **Tên/tiêu đề báo cáo** | `:94` — *"| 1 | ten_bao_cao | text | Luôn | Tên báo cáo |"* |
| 2 | **Kỳ báo cáo + khoảng thời gian** | `:95` — *"| 2 | ky_bao_cao | text | Luôn | Kỳ đã chọn |"* · `:96` — *"| 3 | tu_ngay / den_ngay | datetime | Luôn | Khoảng thời gian |"* |
| 3 | **Đơn vị** | `:97` — *"| 4 | don_vi_ten | text | Luôn | Tên đơn vị hoặc \"Toàn quốc\" |"* |
| 4 | **Ngày tạo báo cáo** | `:98` — *"| 5 | ngay_tao_bc | datetime | Luôn | Thời điểm tạo |"* |

⚠️ **KHÔNG được Fail vì tệp thiếu "Người tạo" / "Tổng số bản ghi" trong phần header.** Hai mục này có ở
**Output của chức năng** (`:99` `nguoi_tao`, `:100` `tong_ban_ghi`) nhưng `:1097` — dòng duy nhất nói về
**header tệp** — chỉ liệt kê 4 mục. SRS im lặng về việc in chúng vào tệp Excel. (`nguoi_tao` chỉ được đặc tả
bắt buộc **in ra** ở tệp **PDF**, `:86` — ngoài phạm vi cụm A.)

⚠️ **KHÔNG được Fail vì tệp Excel thiếu quốc hiệu / tiêu ngữ / khối ký.** Khung văn bản hành chính TT 17/2025
chỉ áp cho **PDF** (`:86`, `:125`), không áp cho XLSX.

**Tiêu chí chấp nhận đúng chữ cho vế (a)** — `srs-v3.5/srs-fr-11-bao-cao.md:124`:
> *"**Given** CB nhấn \"Xuất Excel\" **When** click **Then** tải file .xlsx khổ A4 Times New Roman 13, tên tệp
> đúng khuôn `{TenBaoCao}_{YYYYMMDD_HHmm}.xlsx` (Phụ lục E §H8)"*

### 2.4 Tập cột / chiều số liệu bắt buộc — theo từng loại báo cáo

Đây là **chiều dữ liệu SRS đòi "Luôn" phải có**. Agent đo dùng bảng này để biết **đối chiếu tệp với màn ở
đâu**: mỗi ô trong cột "Chiều số liệu" phải xuất hiện **cả trên màn lẫn trong tệp**, và **từng con số phải khớp**.

| Mã TC | UC | Chiều số liệu bắt buộc (điều kiện "Luôn") | Dòng SRS |
|---|---|---|---|
| `VVDTN_06` | UC125 | Tổng VV tiếp nhận · **theo kênh tiếp nhận** · **theo lĩnh vực PL** · theo đơn vị · theo kỳ | `:216`–`:220` (Dimensions `:208`) |
| `VVDHT_06` | UC126 | Tổng VV đang xử lý · SLA bình thường · SLA sắp hết hạn · SLA quá hạn · **theo người hỗ trợ (NHT)** · theo đơn vị | `:260`–`:265` (Dimensions `:252`) |
| `VVDHTHT_06` | UC127 | Tổng VV hoàn thành · thành công · không thành công · **tỷ lệ thành công (%)** · theo lĩnh vực · theo đơn vị · theo kỳ | `:303`–`:309` (Dimensions `:297`) |
| `VVTTG_05` | UC128 | Dãy **theo kỳ** `{nhãn kỳ, tiếp nhận, hoàn thành}` · theo đơn vị · dạng biểu đồ `LINE` | `:340`–`:342` (Dimensions `:334`) |
| `VVTDVQL_06` | UC134 | Cross-tab **hàng = đơn vị**: mã đơn vị · tên đơn vị · cấp (TW/BN/ĐP) · tổng · **mới** · **tiếp nhận** · **đang hỗ trợ** · **hoàn thành** | `:582`–`:589` (Công thức `:574`) |
| `VVTLV_05` | UC135 | Cross-tab **hàng = lĩnh vực**: mã lĩnh vực · tên lĩnh vực · tổng · **theo đơn vị[]** | `:619`–`:622` (Công thức `:611`) |
| `VVTLHDN_05` | UC136 | Cross-tab **hàng = loại DN**: mã loại · tên loại (Siêu nhỏ / Nhỏ / Vừa) · tổng · **theo đơn vị[]** | `:658`–`:661` (Công thức `:650`) |
| `VVTTGCT_05` | UC137 | Dãy **theo kỳ × trạng thái** `{nhãn kỳ, mới, tiếp nhận, đang hỗ trợ, hoàn thành}` · dạng `STACKED_BAR` · tổng theo trạng thái | `:691`–`:693` (Công thức `:683`) |
| `CPCTHTTTG_05` | UC142 | Dãy **theo kỳ** `{nhãn kỳ, tổng chi phí, số hồ sơ}` · dạng `LINE` · **tổng chi phí toàn kỳ** | `:872`–`:874` (Dimensions `:866`) |

**Cách chấm "nội dung khớp" — 3 phép, làm đủ cả 3:**

1. **Khớp chiều:** mọi ô ở cột trên có mặt trong tệp. Thiếu một chiều "Luôn" → đó là thiếu nội dung, ghi rõ
   chiều nào.
2. **Khớp từng con số:** đọc số trên màn trước, rồi mở tệp đọc lại, so **từng con số** (không so "đại khái
   giống"). Cộng các dòng chi tiết phải ra đúng dòng tổng.
3. **Tệp bám bộ lọc hiện tại:** đổi **1 bộ lọc** (vd Kỳ Năm → Tháng, hoặc bộ lọc đặc thù của chính loại BC đó)
   rồi xuất **lượt thứ hai** — số trong tệp phải đổi theo. Căn cứ: `srs-v3.5/srs-fr-11-bao-cao.md:1285`
   (BR-DATA-06) — *"File xuất theo bộ lọc hiện tại, không vượt quá 10,000 rows/file"*. Đây là phép duy nhất
   phân biệt "xuất đúng" với "xuất cứng bảng mẫu".

**Bộ lọc đặc thù dùng cho phép 3 của từng case** (`:1067–1091` cột *Bộ lọc đặc thù*): UC125 Kênh tiếp nhận /
Lĩnh vực PL · UC126 NHT phụ trách / Mức SLA · UC127 Lĩnh vực PL / Kết quả · UC128 — (không có, đổi Kỳ) ·
UC134 — (đổi Kỳ) · UC135 — (đổi Kỳ) · UC136 Loại DN · UC137 — (đổi Kỳ) · UC142 — (đổi Kỳ).

⚠️ **KHÔNG được Fail vì:** biểu đồ (chart) không có trong tệp Excel — `:1097` chỉ đòi header + dữ liệu; ·
số liệu khác ảnh nghiệm thu của đối tác (khác env, khác bản dựng, khác dữ liệu) — điều phải đúng là **TỆP KHỚP
MÀN**; · bảng chỉ có một dòng kỳ khi chọn kỳ Năm.

⚠️ **CHƯA XÁC MINH ĐƯỢC:** SRS **không** quy định nhãn cột tiếng Việt cụ thể trong tệp Excel, cũng không quy
định thứ tự sheet/cột. ⇒ Chấm theo **khái niệm** chiều dữ liệu, không chấm theo từng chữ nhãn. Nếu tệp in
**mã kỹ thuật** thay chữ tiếng Việt (vd `KHOANG`, `TIEP_NHAN`) thì đó là lỗi hiển thị đã có phiếu riêng
`BCTK_QA09` (dòng 372) — ghi nhận, **không kéo verdict 9 phiếu này**.

---

## 3. VIỆC 3 — Chuẩn quyền vai trò (căn cứ chấm vế (b))

### 3.1 Bốn dòng brief yêu cầu — nguyên văn, số dòng đọc lại 2026-08-07

| Dòng | Nguyên văn |
|---|---|
| `srs-v3.5/srs-fr-11-bao-cao.md:51` | *"**Tác nhân chính:** Cán bộ Nghiệp vụ (TW/BN/ĐP), Cán bộ Phê duyệt (TW/BN/ĐP)"* |
| `srs-v3.5/srs-fr-11-bao-cao.md:62` | *"- User đã đăng nhập, có role CB Nghiệp vụ hoặc CB Phê duyệt (TW/BN/ĐP)"* |
| 🔴 `srs-v3.5/srs-fr-11-bao-cao.md:79` | *"| 1 | **Kiểm tra vai trò trước:** chỉ CB Nghiệp vụ hoặc CB Phê duyệt (TW/BN/ĐP) được truy cập chức năng báo cáo. Vai trò khác (kể cả QTHT) → **chặn ngay ở cửa vào, không mở màn hình**. Sau đó kiểm phạm vi theo đơn vị `[BA chốt 2026-08-06]` | BR-AUTH-01 |"* |
| `srs-v3.5/srs-fr-11-bao-cao.md:117` | *"| E7 | Không có quyền | ERR-RPT-05 | \"Bạn không có quyền xem báo cáo này\" | ERROR |"* |
| `srs-v3.5/srs-v3.5.md:684` | *"| M-05 | **Hiển thị theo quyền** — menu item chỉ hiện nếu vai trò có quyền truy cập ≥ 1 chức năng trong đó. Ẩn (không disable) nếu không có quyền | NF-Security |"* |
| ~~`srs-fr-11-bao-cao.md:1268`~~ | **Đã gỡ.** Xem cảnh báo 2 đầu file — dòng tương ứng nay là `:1273` và ghi ngược lại |

### 3.2 Ba dòng mới do lượt sửa 06/08 — brief chưa nêu, nhưng là căn cứ chấm mạnh nhất

| Dòng | Nguyên văn |
|---|---|
| 🔴 `srs-v3.5/srs-fr-11-bao-cao.md:127` | *"- **Given** người dùng vai trò Quản trị hệ thống **When** đăng nhập **Then** **không thấy** mục menu \"Báo cáo thống kê\" (ẩn theo M-05, không làm mờ) `[BA chốt 2026-08-06]`"* |
| 🔴 `srs-v3.5/srs-fr-11-bao-cao.md:128` | *"- **Given** vai trò ngoài CB Nghiệp vụ / CB Phê duyệt **When** gọi thẳng dịch vụ xuất tệp ở tầng máy chủ (không có đường bấm từ giao diện vì màn đã ẩn) **Then** từ chối với `ERR-RPT-08` — \"Bạn không có quyền thực hiện thao tác này\" `[BA chốt 2026-08-06]`"* |
| `srs-v3.5/srs-fr-11-bao-cao.md:120` | *"| E10 | Không có quyền **thực hiện thao tác xuất tệp** (vai trò ngoài CB NV / CB PD) | ERR-RPT-08 | \"Bạn không có quyền thực hiện thao tác này\" (câu chuẩn `srs-fr-05-vu-viec.md` §3.E — Thông báo người dùng) `[BA chốt 2026-08-06]` | ERROR |"* |

Câu chuẩn được viện dẫn nằm ở `srs-v3.5/srs-fr-05-vu-viec.md:1594` — *"| Không có quyền truy cập | Toast error |
\"Bạn không có quyền thực hiện thao tác này\" |"*.

### 3.3 Ô `R` của QTHT trong ma trận quyền — đã được làm rõ, đừng dùng để nới quyền

| Dòng | Nguyên văn (rút gọn) |
|---|---|
| `srs-v3.5/srs-v3.5.md:1339` | *"| BAO_CAO | R | CRU* | CRU* | CRU* | RU* | RU* | RU* | — | — | — | — |"* (cột 1 = QTHT; header cột ở `:1300`) |
| 🔴 `srs-v3.5/srs-v3.5.md:1296` | *"**Bảng này là quyền ở MỨC DỮ LIỆU, không phải quyền chạy chức năng** `[làm rõ 2026-08-06]`. Một ô có `R` chỉ nói vai trò đó **được đọc dữ liệu** … nó **không** đồng nghĩa vai trò đó là **tác nhân** của các chức năng thao tác trên thực thể ấy."* |
| 🔴 `srs-v3.5/srs-v3.5.md:1298` | *"Ví dụ đã gây tranh chấp ở UAT tuần 5: `BAO_CAO` cột QTHT = `R`, nhưng cả 23 mục FR-IX lẫn 23 giao dịch UC124–146 đều ghi tác nhân là **CB Nghiệp vụ / CB Phê duyệt** — QTHT **không** vào màn báo cáo thống kê và **không** xuất tệp báo cáo."* |

### 3.4 Vế (b) — chuẩn chấm, 2 phép bắt buộc

Brief cấm kết luận vế (b) bằng cách chỉ nhìn menu. Đặc tả cho **hai** mốc chấm riêng biệt:

| Phép | Đo gì | Căn cứ | Đạt khi |
|---|---|---|---|
| **b1 — Menu** | Đăng nhập `admin`, quét toàn bộ menu điều hướng | `:127` + `srs-v3.5.md:684` (M-05) | **Không thấy** mục "Báo cáo thống kê". **Thấy nhưng bị làm mờ / disable = KHÔNG đạt** — M-05 nói *"Ẩn (không disable)"* |
| **b2 — Vào thẳng bằng địa chỉ** | Cùng phiên `admin`, gõ thẳng địa chỉ màn báo cáo (`/bao-cao…`) | `:79` — *"chặn ngay ở cửa vào, **không mở màn hình**"* + `:1046` | Bị chặn / điều hướng đi. **Vào xem được số liệu = KHÔNG đạt**, kể cả khi nút Xuất đã ẩn |

**Ghi rõ trong note:** phép b2 phải chạy **cùng một phiên đăng nhập** với b1 và **kiểm phiên còn sống** ngay
sau đó (lượt 06/08 đã phải làm việc này để loại trừ giả thuyết "hết phiên").

⚠️ **CẤM tự mở rộng phép đo sang tầng máy chủ.** `:128` đặt yêu cầu cho trường hợp *"gọi thẳng dịch vụ xuất tệp
ở tầng máy chủ"* — nhưng đó là ca **không có đường bấm từ giao diện**. Nếu màn đã ẩn đúng thì đây không phải
bước bắt buộc của 9 phiếu. Có gọi thì ghi thành **ghi nhận thêm**, không kéo verdict.

### 3.5 Câu từ chối "Forbidden" — TÁCH KHỎI verdict 9 phiếu

Phiếu BA mục 5 việc số 6 chốt: câu đúng cho tình huống **chặn xuất** là `ERR-RPT-08` *"Bạn không có quyền thực
hiện thao tác này"* (`:120`), **không** phải câu `:117` *"Bạn không có quyền xem báo cáo này"* (`ERR-RPT-05`,
dành cho tình huống **xem**). Phiếu QA `BUG-BCTK-QA01` đang yêu cầu dev hiện câu `:117` → **phiếu đó phải QA
tự chỉnh**, và brief đã nói rõ: *"đây là việc của QA, không kéo verdict 9 dòng này"*.

⇒ Agent đo: nếu còn gặp chuỗi `"Forbidden"`, **ghi nhận vào note**, nhưng verdict 9 phiếu chấm theo bảng
b1/b2 + vế (a), không chấm theo câu chữ thông báo.

---

## 4. Bẫy chấm sai — cụm A

### 4.1 Bẫy **PASS oan**

1. 🔴 **Chấm vế (a) bằng "tệp về máy".** `200 + binary` chỉ chứng minh CREATE. Phải **mở tệp đọc nội dung**:
   4 mục header (§2.3) + đủ chiều số liệu (§2.4) + **từng con số khớp màn** + **lượt xuất thứ hai đổi bộ lọc**.
2. 🔴 **Suy từ loại báo cáo này sang loại khác.** 9 phiếu = 9 loại báo cáo khác nhau, mỗi loại một truy vấn và
   một bộ cột riêng. **Xuất riêng từng loại**, không suy.
3. 🔴 **Chỉ nhìn menu rồi kết luận vế (b).** Bắt buộc đủ b1 **và** b2 (§3.4).
4. **Menu bị làm mờ / disable coi là đã ẩn.** M-05 nói *"Ẩn (không disable)"* — làm mờ là KHÔNG đạt.
5. **Dùng vai trò CB Nghiệp vụ để chứng minh đã fix.** Vai trò đó vốn đã xuất tốt từ 06/08. Phép đo quyết định
   của vế (b) là chạy bằng chính `admin`.
6. **Bản dựng cũ trong tab.** Tab MCP mở lâu vẫn chạy bó mã cũ → tải lại trang bằng địa chỉ, ghi nhãn bản dựng
   trước mỗi case.

### 4.2 Bẫy **FAIL oan**

1. **Fail vì tên tệp không đúng chuỗi trong sheet** (`BaoCaoVuViec_…` / `BaoCaoChiPhi_…`) — chuỗi đó lệch SRS,
   xem §2.2.
2. **Fail vì số liệu khác ảnh nghiệm thu của đối tác** — khác env, khác bản dựng, khác dữ liệu. Điều phải đúng
   là **tệp khớp màn**.
3. **Fail vì tệp Excel thiếu quốc hiệu / khối ký / biểu đồ** — chỉ PDF mới đòi khung TT 17/2025 (`:86`).
4. **Fail vì tệp thiếu "Người tạo" / "Tổng số bản ghi"** — `:1097` chỉ đòi 4 mục header.
5. **Fail vì nút Xuất bị mờ trong khi màn đang có số liệu** — nhiều khả năng do đã bấm [Xem báo cáo] ≥2 lần
   (phiếu riêng `BCTK_QA07`). Tải lại trang, chọn lại bộ lọc, bấm đúng 1 lần.
6. **Fail vì báo cáo rỗng và nút Xuất tự tắt** — đó là hành vi đúng (`:113` INF-RPT-01 + `:1057` điều kiện
   *"Sau khi đã Xem báo cáo"*). Đổi kỳ sang kỳ có dữ liệu rồi đo lại.
7. **Fail vì nhãn cột / nhãn dropdown lệch chữ so với SRS** — chấm theo khái niệm, không theo từng chữ.
8. **Fail vì còn chữ "Forbidden"** — tách phiếu, xem §3.5.

---

## 5. Danh sách CHƯA XÁC MINH ĐƯỢC — agent đo phải tự xác nhận trên màn

| # | Điểm | Vì sao chưa xác minh được từ file | Phải làm gì trên màn |
|---|---|---|---|
| A-1 | Chuỗi hiển thị thật của 9 option trong dropdown loại BC | SRS chỉ quy định khuôn *"[Mã UC] Tên BC"* (`:1052`) + tên ở `:1069–1091`; không có bằng chứng nào trong repo về chữ thật trên giao diện | Mở dropdown, chụp toàn bộ danh sách, **ghi lại chính xác tên đã chọn** cho từng case |
| A-2 | `CPCTHTTTG_05` là UC142 hay UC138 | Tiền tố TC khớp một phần cả hai tên; chốt UC142 dựa trên **lượt đo 06/08**, không phải trên SRS | Đọc đủ 5 tên nhóm "Chi phí" trong dropdown, xác nhận chọn *"BC Chi phí theo thời gian"* |
| A-3 | Nhãn cột tiếng Việt trong tệp Excel của từng loại BC | SRS không quy định nhãn cột cho tệp xuất, chỉ quy định **chiều dữ liệu** | Chấm theo khái niệm §2.4; nếu tệp in mã kỹ thuật thì ghi nhận (phiếu `BCTK_QA09`), không kéo verdict |
| A-4 | Địa chỉ màn báo cáo để chạy phép b2 | Lượt 06/08 dùng `/bao-cao?loai=…`; SRS không đặc tả đường dẫn | Ghi lại địa chỉ thật khi vào màn bằng vai trò CB NV, rồi dùng chính địa chỉ đó cho phiên `admin` |
| A-5 | Mục menu chứa "Báo cáo thống kê" nằm ở nhánh nào | SRS chỉ có breadcrumb *"Trang chủ > Báo cáo thống kê"* (`:1050`) | Quét **toàn bộ** menu bằng phiên `admin` (kể cả submenu phải bấm mới bung), không kết luận từ màn đầu tiên |
| A-6 | Kỳ / đơn vị nào hiện có dữ liệu cho đủ 9 loại | Không có ảnh chụp state hiện tại trong repo | Bắt đầu bằng **Kỳ Năm 01/01–31/12/2026 · Toàn quốc** (bộ lọc lượt 06/08 dựng đủ 9/9); rỗng thì đổi kỳ trước khi kết luận |
