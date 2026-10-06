# Bug report — đợt verify dev fix (FLOW 04) — flowtest-kiemdinh

**Ngày:** 2026-08-07 02:12:30
**Môi trường verify:** https://18.143.165.120.nip.io — R3 (07/08) đo trên bản dựng **HTPLDN · V1.0.9**, gói mã `assets/index-DsMHK7Dp.js` (`GET /` last-modified `Thu, 06 Aug 2026 18:51:25 GMT`, etag `W/"6a74d7ad-428"`). Vòng 06/08 đo trên **V1.0.8**, gói mã `assets/index-DThrFe1_.js`.
**Tài khoản đã dùng:** `cbnv_tw` (CB_NV_TW) · `cbpd_tw_01` (CB_PD, cấp TW) · `cbpd_bn` (CB_PD_BN — 0 dữ liệu)
**Khung nhìn:** 1440×741
**Nguồn case:** bảng làm việc `1OKBN2otlmdZ44…` tab `bug`, dòng 126 + dòng 72 (`Dopai` = *dev done*, `Trạng thái dev fix` = *Fixed*)

> 🔴 **Hiệu lực của kết quả:** đo trên **env dev**, không phải env nghiệm thu của đối tác
> (`htpldn-uat.ospgroup.vn`, bản dựng V1.0/V1.0.2 trong bằng chứng). Vế nào ghi "đã hết lỗi" thì mới chỉ hết
> **trên bản dựng V1.0.8 của env dev** — chưa có hiệu lực cho tới khi bản dựng này lên env đối tác.
> **Đợt này KHÔNG ghi gì lên bảng** (theo yêu cầu đầu đợt): ô kết quả QA + ô note để trống, ô trạng thái dev chỉ đọc.

---

## Bảng tổng hợp

| Mã lỗi | Mã TC | Dòng bảng | Mức độ | Verdict đợt này | Chủ việc tiếp theo | Trạng thái |
|---|---|---|---|---|---|---|
| ~~BUG-LKHDG_12-EXPORT-FILTER~~ | `LKHDG_12` | 126 | Major | **Pass** | — (đã đóng) | **Closed** |
| BUG-QLHSDNHTCP_03-SLA | `QLHSDNHTCP_03` | 72 | — | **Cần BA** | **BA** | Chờ BA |

**Mức độ:** 1 Major (**đã đóng 2026-08-07 R3**) · 0 Minor · 1 chưa xếp mức (chờ BA quyết có phải lỗi không).
**Trạng thái:** Closed **1** · Open **0** · Chờ BA **1**.

---

## ~~BUG-LKHDG_12-EXPORT-FILTER~~ [CLOSED] — Xuất Excel danh sách đợt đánh giá không áp bộ lọc đang bật

> **Re-test:** 2026-08-07 02:12:30 R3 — ✅ PASS (Closed-verified) trên bản dựng `assets/index-DsMHK7Dp.js` (deploy 07/08 01:51 giờ VN; sidebar hiển thị V1.0.9 nhưng **nhãn này không dùng làm định danh được** — bó mã này MỚI HƠN bó mã của bản gắn nhãn V1.0.10) (env dev `18.143.165.120.nip.io`). Vế "xuất sai tiêu chí lọc" đã hết lỗi: lọc Tần suất *Tròn năm* → màn 19, tệp **19 dòng** trùng khít 19/19 mã; lọc Trạng thái *Hoàn thành* → màn 4, tệp **4 dòng** trùng khít 4/4 mã; 2 tệp khác kích thước (8440 ≠ 7195 byte). Đường đo thứ hai: `GET` 4/19/20 bản ghi ↔ `POST …/export` 7195/8439/8559 byte (vòng trước đứng yên 8519). N = 20 · M = 5/5 dạng · bảng GAP trống · không seed thêm. Chi tiết: `../reverify-week-5/F3-devfix-2026-08-07/do/LKHDG_12.md`.

**Mức độ:** Major — người dùng lọc để lấy đúng tập cần báo cáo, tệp lại trả toàn bộ danh sách; sai lệch **âm
thầm**, không có cảnh báo nào, nên rất dễ dùng nhầm số liệu.

### Mô tả

Trên màn **Đánh giá hiệu quả → Kế hoạch đánh giá → Danh sách**, sau khi áp bộ lọc, nút **[Xuất Excel]** tạo tệp
chứa **toàn bộ** danh sách thay vì tập đã lọc. Giao diện gửi tham số lọc đi đúng (`?tanSuat=…` / `?trangThai=…`
có trong đường dẫn của yêu cầu xuất), nhưng tệp trả về không phản ánh tham số đó.

### Bước tái hiện

Điều kiện: đăng nhập `cbnv_tw` (CB Nghiệp vụ Trung ương), danh sách có ≥2 giá trị khác nhau ở cột định lọc.

1. Vào **Đánh giá hiệu quả** → danh sách hiện **20 kết quả**.
2. Chọn **Tần suất = "Tròn năm"** → bấm **[Tìm kiếm]**. Chân bảng báo **"Hiển thị 1-19 / 19 kết quả"**.
3. Bấm **[Xuất Excel]** → mở tệp tải về, đếm số dòng dữ liệu.
4. Làm lại với cột lọc khác: **Tần suất = "Tất cả"**, **Trạng thái = "Hoàn thành"** → **[Tìm kiếm]**.
   Chân bảng báo **"Hiển thị 1-4 / 4 kết quả"**. Bấm **[Xuất Excel]**, đếm lại.

### Kết quả mong đợi

Theo **BR-DATA-06** (`srs-v3.5.md:5570` — *"Export Excel: Mọi danh sách có tính năng xuất Excel. **File xuất
theo bộ lọc hiện tại**, không vượt quá 10,000 rows/file"*; cột Áp dụng = **"Toàn bộ CRUD list"**, cột Ngoại lệ
chỉ miễn cho báo cáo nhóm IX xuất PDF — không miễn nhóm VI): tệp xuất ra chứa **đúng tập bản ghi đang hiển thị
sau khi lọc** — bước 3 phải là **19 dòng**, bước 4 phải là **4 dòng**.

### Kết quả thực tế

| Lượt | Bộ lọc | Trên màn | Trong tệp | Kết luận |
|---|---|---|---|---|
| 1 | `Tần suất = Tròn năm` | **19** bản ghi | **20 dòng** | ❌ dư `DG-20260806-0001` — đợt **Sơ bộ 6 tháng**, không thuộc tập lọc |
| 2 | `Trạng thái = Hoàn thành` | **4** bản ghi | **20 dòng** | ❌ tệp chứa **7 trạng thái**: Lập kế hoạch 2 · Đang đánh giá 4 · Thực hiện 5 · Hủy 2 · Đã đánh giá 1 · Chờ phê duyệt 2 · Hoàn thành 4 |

Hai lượt cho **tệp giống hệt nhau, cùng 8.521 byte** ⇒ bộ lọc không tác động gì tới nội dung tệp.

**Bằng chứng vòng R3 (2026-08-07, V1.0.9) — đã hết lỗi:**

![LKHDG_12 R3 lượt 1 — màn đã lọc Tần suất "Tròn năm", chân bảng "Hiển thị 1-19 / 19 kết quả", URL ?tanSuat=TRON_NAM&page=1, chân sidebar HTPLDN · V1.0.9](image/LKHDG_12-R3-01-luot1-loc-TronNam-19ketqua-V109.png)

![LKHDG_12 R3 lượt 2 — màn đã lọc Trạng thái "Hoàn thành", chân bảng "Hiển thị 1-4 / 4 kết quả", URL ?trangThai=HOAN_THANH&page=1](image/LKHDG_12-R3-02-luot2-loc-HoanThanh-4ketqua-V109.png)

**Đối chứng bằng phương pháp thứ hai** (cùng một chuỗi truy vấn `trangThai=HOAN_THANH&page=1&pageSize=20`):

- Đầu ra danh sách trả **4 bản ghi** — `DG-20260723-0002`, `DG-20260722-0001`, `DG-20260720-0001`, `KHDG-SEED-0001`.
- Đầu ra xuất tệp trả **8.521 byte** = đúng tệp 20 dòng ở trên.

⇒ Giá trị lọc **hợp lệ và được hiểu đúng** ở đường dẫn danh sách, nhưng **bị bỏ qua** ở đường dẫn xuất tệp.
Lỗi nằm phía máy chủ, không phải phía giao diện.

### Bằng chứng

- `image/LKHDG_12-man-loc-HoanThanh-4ketqua-V108-2026-08-06.png` — màn danh sách sau khi lọc *Trạng thái =
  Hoàn thành*: ô lọc hiện "Hoàn thành", chân bảng "Hiển thị 1-4 / 4 kết quả", 4 dòng
  `DG-20260723-0002` / `DG-20260722-0001` / `DG-20260720-0001` / `KHDG-SEED-0001`, thanh bên ghi `HTPLDN · V1.0.8`.
- `image/LKHDG_12-file-xuat-loc-HoanThanh-V108-2026-08-06.xlsx` — chính tệp do lượt xuất đó tạo ra
  (8.521 byte). Mở bằng openpyxl: sheet *"Kế hoạch đánh giá"*, **21 hàng × 10 cột** = 1 hàng tiêu đề + **20 dòng
  dữ liệu**, hàng 2 là `DG-20260806-0001` (Sơ bộ 6 tháng / Lập kế hoạch) — không thuộc bộ lọc *Hoàn thành*.
- Bằng chứng gốc của đối tác: `partner-evidence/LKHDG_12.webm` → khung `frames/LKHDG_12/t009.06s.jpg`
  (màn đã lọc `?tanSuat=TRON_NAM`, "Hiển thị 1-4 / 4 kết quả") và `frames/LKHDG_12/t018.13s.jpg`
  (tệp `ke-hoach-danh-gia-1783739630247.xlsx` mở trong Excel, 14 dòng dữ liệu).

### 2 vế còn lại của case — ĐÃ HẾT LỖI trên V1.0.8

| Vế đối tác | Hiện trạng đo được | Kết luận |
|---|---|---|
| "File thiếu cột *Số vụ việc*, *Người tạo*, *Ngày tạo*" | Tệp có **10 cột**: Mã KH · Tên đợt · Tần suất · Đối tượng · **Số vụ việc** · Từ ngày · Đến ngày · Trạng thái · **Người tạo** · **Ngày tạo** | ✅ đủ cả 3 cột |
| "Tần suất / Đối tượng / Trạng thái hiển thị không dấu" | Giá trị trong tệp là nhãn tiếng Việt: "Sơ bộ 6 tháng", "Tròn năm", "Đào tạo", "Vụ việc", "Tổng hợp", "Lập kế hoạch", "Đang đánh giá", "Hoàn thành"… — **không còn mã enum thô** | ✅ hết lỗi |

Hai vế này đặc tả vốn **im lặng** (nhóm VI không có yêu cầu chức năng nào đặc tả tệp xuất), nên lúc viết tiêu chí
đã xếp là "phải hỏi BA". Nhưng bản dựng hiện tại **đã làm đúng như đối tác mong đợi** ⇒ **không còn bất đồng để
hỏi BA**, bỏ khỏi danh sách câu hỏi.

### Kiểm tra kèm — thông báo sau khi bấm [Xuất Excel]

1 yêu cầu mạng ↔ **1 thông báo** *"Xuất Excel thành công"* (đo bằng bộ đếm chạy **trước** lúc bấm: số thẻ thông
báo cùng tồn tại tối đa = 1, số yêu cầu tới đường dẫn xuất = 1). Bộ theo dõi thay đổi DOM bắt được **4 sự kiện**
nhưng đó là cặp *thẻ bọc + thẻ trong* bị dựng lại 2 lần trong cùng 1 mili-giây — **không phải thông báo đúp**,
không log lỗi.

```
── CÁCH VERIFY sau Dev fix ──
Precondition: tài khoản `cbnv_tw` (CB Nghiệp vụ Trung ương, Test@1234) + màn
  https://18.143.165.120.nip.io/danh-gia/ke-hoach/danh-sach.
  Danh sách phải có ≥2 giá trị khác nhau ở cột định lọc (nếu mọi đợt cùng Tần suất thì phải
  tạo thêm 1 đợt khác Tần suất, nếu không thì phép đo vô nghĩa).
1) Ghi lại tổng số kết quả khi CHƯA lọc (đọc ở chân bảng "Hiển thị 1-N / N kết quả").
2) Chọn Tần suất = "Tròn năm" → bấm [Tìm kiếm]. Ghi lại số kết quả sau lọc = n_lọc (phải < tổng).
3) Bấm [Xuất Excel] → mở tệp, đếm số dòng dữ liệu (không kể dòng tiêu đề) và liệt kê cột "Mã KH".
4) Lặp lại bước 2-3 với cột lọc KHÁC: Tần suất = "Tất cả", Trạng thái = "Hoàn thành".
✅ PASS khi: cả 2 lượt, số dòng dữ liệu trong tệp = đúng n_lọc của lượt đó, VÀ tập "Mã KH"
   trong tệp trùng khít tập mã đang hiện trên màn (so từng mã, không chỉ so số lượng).
❌ FAIL nếu: tệp chứa ≥1 mã không thuộc tập sau lọc, hoặc số dòng ≠ n_lọc, hoặc 2 lượt lọc
   khác nhau lại cho 2 tệp cùng kích thước byte.
⚠️ Đừng chấm Fail vì tệp thiếu cột hay vì định dạng nhãn — đặc tả không quy định tập cột của
   tệp xuất; chỉ chấm đúng phần "theo bộ lọc hiện tại" của BR-DATA-06.
⚠️ Đừng kết luận "đã fix" khi chỉ thấy đường dẫn yêu cầu xuất CÓ mang tham số lọc — giao diện
   gửi đúng tham số ngay cả khi đang lỗi; phải mở tệp đếm dòng.
Ảnh lỗi cũ: frames/LKHDG_12/t009.06s.jpg (màn đã lọc, 4 kết quả)
            frames/LKHDG_12/t018.13s.jpg (tệp xuất ra 14 dòng)
Bằng chứng lượt này: image/LKHDG_12-man-loc-HoanThanh-4ketqua-V108-2026-08-06.png
            image/LKHDG_12-file-xuat-loc-HoanThanh-V108-2026-08-06.xlsx
```

**Chủ việc + việc tiếp theo:** **Dev BE** — áp bộ lọc đang nhận được vào truy vấn của đường dẫn xuất tệp
(hiện đường dẫn nhận tham số nhưng truy vấn không dùng), để tệp khớp đúng tập bản ghi mà đường dẫn danh sách
trả về với cùng chuỗi truy vấn.

---

## BUG-QLHSDNHTCP_03-SLA — Cột cảnh báo thời hạn danh sách Hồ sơ Chi trả

> **Re-test:** 2026-08-06 00:40 V1.0.8 (env dev `18.143.165.120.nip.io`) — ⚠️ **Cần BA**. **Cả 2 vế đối tác
> phản ánh đều đã hết lỗi** (0 px tràn trên 28 lượt đo dòng × 2 vai trò; đã hiện 4 nhãn mức rời theo BR-SLA-02).
> Phát sinh 1 điểm đặc tả chưa quy định → chuyển BA, QA không tự chấm. N = 14 hồ sơ × 2 vai trò · M = 4/4 mức.

**Mức độ:** chưa xếp — phụ thuộc BA quyết điểm hỏi ở `cau-hoi-BA.md` §1.

### Mô tả

Case kiểm tra các cột dữ liệu của bảng **Chi trả chi phí → Danh sách** (`/chi-tra/danh-sach`), tập trung ở cột
cảnh báo thời hạn. Đối tác phản ánh 2 vòng: vòng 1 *"cột không giống thiết kế"*, vòng 2 *"dữ liệu cột tràn sang
cột Ngày nộp"*.

### Bước tái hiện

Điều kiện: cần có hồ sơ ở mức cảnh báo **"Quá hạn nghiêm trọng"** (chuỗi nhãn dài nhất, dễ tràn nhất).

1. Đăng nhập `cbnv_tw` → **Chi trả chi phí** → tab **"Tất cả"** (`?tab=TAT_CA&page=1`).
2. Cuộn bảng sang phải cho tới khi cột cảnh báo và cột **Ngày nộp** cùng nằm trong tầm nhìn.
3. Với từng dòng: đọc nhãn ở ô cảnh báo; đo hộp bao của nội dung ô so với hộp bao ô; kiểm giá trị Ngày nộp có
   đọc được đủ 10 ký tự không.
4. Đăng xuất, lặp lại bước 1-3 bằng tài khoản vai trò **CB Phê duyệt**.

### Kết quả mong đợi

- **BA chốt 2026-07-24** (`../../reverify-week-3/ba-confirm/phan-hoi/phan-hoi-ba/phan-hoi-ba-confirmation-needed-week-3.md:56-63`):
  cột hiển thị **4 nhãn mức rời** theo **BR-SLA-02** — *"Bình thường / Sắp hết hạn / Quá hạn / Quá hạn nghiêm
  trọng"* — **kèm số ngày còn lại**, áp cho cả màn danh sách lẫn màn chi tiết. Cùng quyết định đó ghi rõ
  **tên cột "SLA" của phần mềm là khớp đặc tả**.
- **SCR-V.II-01** (`srs-fr-06-chi-tra.md:1058-1059`): thành phần #16 *SLA* và #17 *Ngày nộp* là **hai cột riêng**,
  #17 có điều kiện hiển thị **"Luôn"** ⇒ giá trị Ngày nộp phải đọc được đầy đủ ở mọi dòng.
- Theo "Kết quả mong đợi" ghi trên dòng bảng: **dữ liệu không bị tràn / đè lên nhau**.

### Kết quả thực tế

**Vế (a) — tên cột + 4 nhãn mức: đã hết lỗi.**

| | Bằng chứng đối tác | V1.0.8 env dev |
|---|---|---|
| Tiêu đề cột | "SLA" | "SLA" — **đúng như BA chốt 2026-07-24** |
| Giá trị | Vòng 1: đếm ngày trần *"Quá hạn 58 ngày LV"* (chưa có nhãn mức) | **Nhãn mức rời + số ngày**: "Bình thường · còn 10 ngày LV" · "Sắp hết hạn · còn 6 ngày LV" · "Quá hạn · 6 ngày LV" · "Quá hạn nghiêm trọng · 53 ngày LV" |
| Phủ mức | — | **4/4 mức BR-SLA-02**: Bình thường 1 · Sắp hết hạn 1 · Quá hạn 2 · Quá hạn nghiêm trọng 6 |

**Vế (b) — tràn sang cột Ngày nộp: đã hết lỗi.** Đo hộp bao trên **14 dòng × 2 vai trò = 28 lượt**:

| Phép đo | `cbnv_tw` (CB NV) | `cbpd_tw_01` (CB PD) |
|---|---|---|
| Chồng lấn ngang lớn nhất giữa nội dung ô cảnh báo và ô Ngày nộp | **0 px** / 14 dòng | **0 px** / 14 dòng |
| Mép phải nội dung so với mép phải ô (số âm = nằm trong ô) | **−8 px** (xấu nhất) | **−8 px** (xấu nhất) |
| Nội dung có bị cắt ngầm không (`scrollWidth` vs `clientWidth`) | bằng nhau ở mọi dòng ⇒ không cắt | — |
| Ngày nộp đọc đủ 10 ký tự, không bị phần tử nào phủ | **14/14 dòng** | **14/14 dòng** |

Ô cảnh báo nay **xuống dòng trong ô** ("Quá hạn nghiêm/trọng · 53 ngày LV" thành 2 dòng) thay vì kéo dài đè
sang cột bên cạnh như trong ảnh vòng 2 của đối tác. Đo ở khung nhìn **1440 px** — **hẹp hơn** khung của đối tác,
tức phép đo lần này **ngặt hơn**, không dễ dãi hơn.

**Điểm phát sinh — đặc tả chưa quy định, chuyển BA:** 4 dòng ở trạng thái **đã kết thúc**
(`CT-QAW7-CLOSED`, `CT-SEED-108` — Đã thanh toán; `CT-SEED-109` — Từ chối; `CT-SEED-110` — Hủy) hiện
**nhãn thứ 5 "Đã hoàn thành"**, không nằm trong 4 mức BR-SLA-02, trong khi dữ liệu của đúng 4 bản ghi đó trả
`mucDoCanhBao = "BINH_THUONG"`. Chi tiết + câu hỏi: `cau-hoi-BA.md` §1.

### Bằng chứng

- `image/QLHSDNHTCP_03-danhsach-SLA-NgayNop-V108-2026-08-06.png` — vai trò **CB Nghiệp vụ TW**: cột "SLA" hiện
  thẻ "Bình thường · còn 10 ngày LV" (nền xanh), "Sắp hết hạn · còn 6 ngày LV" (nền cam), "Quá hạn nghiêm trọng
  · 53 ngày LV" (nền đen, chữ **xuống 2 dòng nằm trong ô**); cột "Ngày nộp" bên phải đọc rõ 03/08/2026,
  24/07/2026, 01/06/2026, 04/05/2026, 05/07/2026 — **không bị thẻ nào che**.
- `image/QLHSDNHTCP_03-vaitro-CBPD-SLA-NgayNop-V108-2026-08-06.png` — vai trò **CB Phê duyệt**: 9 dòng cuối,
  các thẻ "Quá hạn nghiêm trọng · 20 / 16 / 14 ngày LV" đều xuống 2 dòng trong ô, "Quá hạn · 6 / 9 ngày LV"
  (nền đỏ) và "Đã hoàn thành" (nền xám) nằm gọn; cột Ngày nộp đọc đủ ở cả 9 dòng; chân bảng "Hiển thị 1-14 / 14 kết quả".
- Bằng chứng gốc của đối tác: `partner-evidence/QLHSDNHTCP_03.jpg` (vòng 1, V1.0, CB_NV_TW — cột "SLA" hiện
  đếm ngày trần) · `partner-evidence/QLHSDNHTCP_03_v2.png` (vòng 2, V1.0.2, CB_PD_BN — khung đỏ khoanh 2 dòng
  `HSCT000051`/`HSCT000052`, thẻ đen "Quá hạn nghiêm trọng · 52 / 54 ngày LV" **đè lên cột Ngày nộp**, chỉ còn
  đọc được 3 ký tự cuối `026`).

```
── CÁCH VERIFY sau Dev fix ──
Precondition: tài khoản `cbnv_tw` (CB Nghiệp vụ Trung ương, Test@1234) + màn
  https://18.143.165.120.nip.io/chi-tra/danh-sach, tab "Tất cả".
  Bắt buộc có ≥1 hồ sơ ở mức "Quá hạn nghiêm trọng" — đây là chuỗi nhãn dài nhất nên là dạng
  dễ tràn nhất; thiếu nó thì phép đo không kết luận được.
1) Cuộn bảng sang phải tới khi cột cảnh báo thời hạn VÀ cột "Ngày nộp" cùng nằm trong tầm nhìn.
2) Với TỪNG dòng: đọc nhãn ở ô cảnh báo (phải là nhãn mức + số ngày, không phải đếm ngày trần).
3) Với TỪNG dòng: kiểm nội dung ô cảnh báo có nằm trọn trong ô của nó không, và giá trị Ngày nộp
   có đọc được đủ dd/mm/yyyy không.
4) Lặp lại bước 1-3 bằng một tài khoản vai trò CB Phê duyệt (bộ cột khác: có thêm ô chọn dòng
   và nút thao tác khác → độ rộng cột khác).
✅ PASS khi: mọi dòng của hồ sơ CÒN ĐANG XỬ LÝ mang đúng 1 trong 4 nhãn "Bình thường" /
   "Sắp hết hạn" / "Quá hạn" / "Quá hạn nghiêm trọng" kèm số ngày; VÀ mọi dòng có phần chồng
   lấn giữa ô cảnh báo và ô Ngày nộp = 0 px; VÀ mọi dòng đọc được đủ 10 ký tự Ngày nộp.
❌ FAIL nếu: ≥1 dòng có ô cảnh báo đè sang ô Ngày nộp, hoặc Ngày nộp bị che một phần, hoặc
   ≥1 dòng hồ sơ đang xử lý vẫn hiện đếm ngày trần không kèm nhãn mức.
⚠️ Đừng chấm Fail vì tiêu đề cột là "SLA" thay vì "Mức cảnh báo thời hạn" — BA đã chốt ngày
   2026-07-24 rằng tên "SLA" khớp đặc tả.
⚠️ Đừng chấm Fail khi chưa cuộn ngang: ở vị trí cuộn mặc định, cột "Hành động" dán cố định che
   mất phần bên phải, dễ tưởng nhầm là cột cảnh báo đè lên Ngày nộp.
⚠️ 4 dòng hồ sơ đã kết thúc hiện nhãn "Đã hoàn thành" — đang chờ BA, KHÔNG dùng để chấm.
Ảnh lỗi cũ: partner-evidence/QLHSDNHTCP_03_v2.png (thẻ đen đè lên cột Ngày nộp)
Bằng chứng lượt này: image/QLHSDNHTCP_03-danhsach-SLA-NgayNop-V108-2026-08-06.png
            image/QLHSDNHTCP_03-vaitro-CBPD-SLA-NgayNop-V108-2026-08-06.png
```

**Chủ việc + việc tiếp theo:** **BA** — trả lời câu hỏi ở `cau-hoi-BA.md` §1. Chưa có câu trả lời thì **chưa
chuyển cho dev**: hai vế đối tác phản ánh đều đã hết lỗi, không có việc gì cho dev làm ở thời điểm này.
