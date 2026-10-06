# QLLKHDTBD_09 — HỒ SƠ ĐO (FLOW 04 · Giai đoạn B)

> Chuẩn chấm đã khoá: [`../chuan/QLLKHDTBD_09.md`](../chuan/QLLKHDTBD_09.md). File này KHÔNG đổi quan hệ MATCH/DIFF/GAP đã khoá.

---

## 1. Vân tay bản dựng + tài khoản

| Mục | Giá trị đo được |
|---|---|
| Env | `https://18.143.165.120.nip.io` |
| `last-modified` | `Thu, 06 Aug 2026 19:23:01 GMT` |
| `etag` | `W/"6a74df15-428"` |
| Bó mã FE | `index-D4Buvu4S.js` (CSS `index-DVlgOkLg.css`) |
| Chuỗi phiên bản chân sidebar | `HTPLDN · V1.0.9` |
| **Đối chiếu lô** | **KHỚP lượt 2+3 của lô** (dòng 13, 14 — `W/"6a74df15-428"` + `index-D4Buvu4S.js`). Không có deploy giữa lượt. |
| Thời điểm đo | 2026-08-07, 03:00 → 03:07 (giờ máy, +07) |
| Tài khoản thực dùng | **`cbnv_tw_02`** — badge màn `CB Nghiệp vụ - Trung ương #02` / `Cán bộ Nghiệp vụ Trung ương`, đơn vị `BTP · TW` |
| Xác minh vai trò | Payload token của chính request danh sách: `vaiTro:["CB_NV_TW"]`, `capDonVi:"TW"`, `hoTen:"CB Nghiệp vụ - Trung ương #02"` |
| Ghi chú phiên | Phiên đăng nhập còn hiệu lực từ case liền trước cùng lô (cùng tài khoản, cùng vai trò) → **không phải đăng nhập lại**, không chạm giới hạn 5 lượt/60s. Đã **tải lại trang** (điều hướng tài liệu mới) trước lô đo ⇒ chạy đúng bó mã hiện hành, không phải mã cũ còn trong tab. |
| Nhật ký trình duyệt | **Sạch** — `list_console_messages` (error + warn) trả 0 thông điệp trong suốt lô đo |

> ⚠️ Đúng cảnh báo của prompt: chuỗi phiên bản trên màn ghi `V1.0.9` — **không dùng làm căn cứ**. Căn cứ là `last-modified` + `etag` + bó mã, cả ba đều khớp lượt 2+3.

---

## 2. Màn + tiền đề

| Mục | Giá trị |
|---|---|
| Màn | `Đào tạo, tập huấn` → `Kế hoạch đào tạo` → `Danh sách` (SCR-III-00 · FR-III-14) |
| URL | `https://18.143.165.120.nip.io/dao-tao/ke-hoach/danh-sach` |
| Endpoint danh sách (đọc từ nhật ký mạng, **không đoán**) | `GET /api/v1/ke-hoach-dao-taos` |
| Endpoint xuất (đọc từ nhật ký mạng) | `POST /api/v1/ke-hoach-dao-taos/export` |
| **`N` = tổng bản ghi KHÔNG lọc** | **14** — lấy từ **số thô** `meta.total` của `GET /api/v1/ke-hoach-dao-taos?page=1&pageSize=20`, KHÔNG đếm bằng mắt |
| Kiểm tra số có nói dối không | `meta.tabCounts` = NHAP 7 + CHO_DUYET 2 + DA_DUYET 4 + DA_CONG_KHAI 1 + TU_CHOI 0 = **14 = `meta.total`** ⇒ các chiều **cộng khớp tổng**, số dùng được |
| Seed / mutate | **KHÔNG tạo, KHÔNG sửa, KHÔNG xoá bản ghi nào.** Chỉ thao tác đọc: đổi tab trạng thái + nhập 2 ô ngày + bấm `Xuất Excel`. Không đụng dữ liệu đối tác. |

Dữ liệu QA sẵn có đủ để lọc phân biệt (14 bản ghi) ⇒ **không cần seed mới**, đúng ưu tiên "dùng lại dữ liệu QA có sẵn".

---

## 3. Vế C1 — tệp xuất theo ĐÚNG bộ lọc hiện tại  ·  quan hệ `MATCH` · route `TEST`

### 3.1 Vì sao đo 2 bộ lọc (không phải mở rộng phạm vi)

Chuẩn chấm §7 khoá sẵn 2 bộ lọc. Căn cứ giữ cả hai:
- **Bộ lọc A `Trạng thái`** là bộ lọc **SRS liệt kê tường minh** (`srs-fr-03-dao-tao.md:1781`) ⇒ neo verdict vào đúng bộ lọc đặc tả công nhận.
- **Bộ lọc B `Từ ngày`/`Đến ngày`** là **đúng bộ lọc mà lỗi gốc đã tái hiện** trong video vòng 1 của đối tác (màn 2 / tệp 12). Luật khoá 4 FLOW 04 cho phép thêm biến thể khi *"bằng chứng của case cho thấy claim phụ thuộc biến thể đó"*. Nếu chỉ đo A mà bỏ B thì có nguy cơ **Pass oan đúng kịch bản đối tác đã báo lỗi**.

Cả hai đều là cùng một vế C1, cùng một màn, cùng một nút.

### 3.2 Phép đo A — lọc `Trạng thái = Đã duyệt`

| Bước | Nội dung |
|---|---|
| Thao tác UI thật | Bấm tab `Đã duyệt` trên màn danh sách |
| **Tên tham số truy vấn THẬT** | **`trangThai=DA_DUYET`** — đọc từ chính request màn gửi: `GET /api/v1/ke-hoach-dao-taos?trangThai=DA_DUYET&page=1&pageSize=20`. **Không đoán tên tham số.** |
| `M` (số thô) | **4** — `meta.total` = 4 của chính request trên |
| Chữ trên màn | `Hiển thị 1-4 / 4 kết quả` (khớp `meta.total`) |
| `M < N`? | **4 < 14** ✅ — tỉ lệ 4/14 ≈ 0,29 ≤ 1/3, đạt mức "lý tưởng" của chuẩn chấm §7 ⇒ phép đo **phân biệt được** "xuất theo lọc" với "xuất toàn bộ" |
| Thao tác đang tranh chấp | Bấm **`Xuất Excel` trên UI thật** (nút `download Xuất Excel` ở hàng hành động chính). **Không gọi API thay thao tác.** |
| Request xuất thực phát sinh | `POST /api/v1/ke-hoach-dao-taos/export?trangThai=DA_DUYET&page=1&pageSize=20` → **bộ lọc CÓ được truyền sang chức năng xuất** |
| Thông báo bắt được | Đúng **1** lần: `Xuất Excel thành công` (bộ bắt `MutationObserver` cài TRƯỚC thao tác, đọc bằng `innerText`, **không lọc trùng**; tự kiểm `soObserverDangSong = 1` ⇒ số liệu hợp lệ) |
| Tệp tải về | `~/Downloads/ke-hoach-dao-tao-1786046602595.xlsx` — epoch trong tên → **2026-08-07 03:03:22**, cách thời điểm bấm 15 giây ⇒ **đúng tệp vừa tạo, không nhặt nhầm tệp cũ** (thư mục có sẵn 6 tệp cùng mẫu tên, cũ nhất từ 03/08) |

**Đối chứng độc lập — MỞ TỆP đọc nội dung bằng `openpyxl`** (không dừng ở "tải được tệp"):

- Trang tính: `Kế hoạch đào tạo` · `max_column` = 7
- **Số dòng dữ liệu = 4** (đã duyệt ngược bỏ dòng trống đuôi, không lấy `max_row` thô)
- Tập `Mã KH` trong tệp: `KH-20260803-0001` · `KHDT-QAW7-01` · `KHDT-2026-001` · `KHDT-SEED-0001`
- Tập `Mã KH` trên màn sau lọc: **giống hệt, đúng 4 mã đó**
- Cột `Trạng thái` của cả 4 dòng đều là `Đã duyệt` ⇒ nội dung nhất quán với bộ lọc

> **A ĐẠT:** số dòng dữ liệu = `M` = 4 (**không** phải `N` = 14), và tập `Mã KH` trùng khít tập trên màn.

### 3.3 Phép đo B — lọc `Từ ngày 01/07/2026` – `Đến ngày 31/07/2026` (tái hiện đúng đối tác)

| Bước | Nội dung |
|---|---|
| Thao tác UI thật | Về tab `Tất cả`, nhập `01/07/2026` vào ô `Từ ngày`, `31/07/2026` vào ô `Đến ngày`, bấm `Tìm kiếm` |
| ⚠️ Sự cố thao tác đã xử lý | Lần điền đầu, ô `Đến ngày` hiện đúng chữ `31/07/2026` nhưng **trạng thái trong ứng dụng chưa nhận** — địa chỉ chỉ có `tuNgay`, thiếu `denNgay`. Đã **không** đo ở trạng thái nhập nhằng này; xử lý bằng cách mở bảng lịch và **bấm đúng ô ngày 31 của tháng 7/2026** rồi `Tìm kiếm` lại, tới khi địa chỉ mang **đủ cả hai** tham số mới đo. |
| **Tên tham số truy vấn THẬT** | **`tuNgay=2026-07-01&denNgay=2026-07-31`** — `GET /api/v1/ke-hoach-dao-taos?tuNgay=2026-07-01&denNgay=2026-07-31&page=1&pageSize=20` |
| Đối chiếu neo đối tác | Trùng khít URL trong video vòng 1: `...danh-sach?tuNgay=2026-07-01&denNgay=2026-07-31&page=1` |
| `M` (số thô) | **1** — `meta.total` = 1 |
| Chữ trên màn | `Hiển thị 1-1 / 1 kết quả` (khớp) |
| `M < N`? | **1 < 14** ✅ |
| Thao tác đang tranh chấp | Bấm **`Xuất Excel` trên UI thật** |
| Request xuất thực phát sinh | `POST /api/v1/ke-hoach-dao-taos/export?tuNgay=2026-07-01&denNgay=2026-07-31&page=1&pageSize=20` → **cả hai mốc ngày CÓ được truyền sang chức năng xuất** |
| Thông báo bắt được | Đúng **1** lần: `Xuất Excel thành công` (bộ bắt cài lại sau khi chuyển màn, tự kiểm `soObserverDangSong = 1`) |
| Tệp tải về | `~/Downloads/ke-hoach-dao-tao-1786046777916.xlsx` — epoch → **2026-08-07 03:06:17**, cách thời điểm bấm ~8 giây ⇒ đúng tệp vừa tạo |

**Đối chứng độc lập — `openpyxl`:**

- Trang tính `Kế hoạch đào tạo` · `max_column` = 7
- **Số dòng dữ liệu = 1**
- `Mã KH` trong tệp: `KH-20260803-0003` — đúng bản ghi duy nhất trên màn (`QA VERIFY QLLKHDTBD_09 - KHDT trong thang 7-2026`, 05/07/2026 → 25/07/2026, nằm trọn trong tháng 7/2026)

> **B ĐẠT:** số dòng dữ liệu = `M` = 1 (**không** phải `N` = 14).
> Đây chính là bộ lọc mà vòng 1 cho **màn 2 / tệp 12**. Vòng này **màn 1 / tệp 1**.

### 3.4 Kết luận C1

**C1 = ĐẠT** trên cả hai bộ lọc. Triệu chứng đối tác ghi trên phiếu — *"Hệ thống xuất toàn bộ danh sách hiện có trên bảng danh sách"* — **không tái hiện** trên bản dựng đo: nếu chức năng xuất bỏ qua bộ lọc thì cả hai tệp đã phải có 14 dòng; thực tế là **4** và **1**, đúng bằng `M` của từng lần.

Neo đặc tả (tự mở lại file trong lượt này, không bê số dòng từ hồ sơ cũ):
- `srs-v3.5.md:5570` — BR-DATA-06: *"**Export Excel:** Mọi danh sách có tính năng xuất Excel. File xuất theo bộ lọc hiện tại, không vượt quá 10,000 rows/file"*, cột Áp dụng `Toàn bộ CRUD list`
- `srs-fr-03-dao-tao.md:2243` — *"| BR-DATA-06 | Export Excel | FR-III-01, FR-III-05, FR-III-06, FR-III-14 |"* (xác nhận áp đúng FR-III-14)
- `srs-fr-03-dao-tao.md:1775` — *"- Nút "Xuất Excel" (phụ): xuất danh sách KH theo bộ lọc, tối đa 10.000 dòng"*
- `srs-fr-03-dao-tao.md:1175` — *"| 2 | Lấy danh sách theo filter, tối đa 10.000 dòng | BR-DATA-06 |"*

### 3.5 🔴 Giới hạn hiệu lực của phép đo C1 (khai báo trung thực, KHÔNG phải bug)

Cả hai lần đo đều có `M` (4 và 1) **nhỏ hơn cỡ trang** (20/trang), và tổng dữ liệu `N` = 14 cũng nhỏ hơn 20. Vì vậy trang đang hiển thị **trùng với toàn bộ tập sau lọc**, nên phép đo này **không phân biệt được** hai hành vi:
- (i) xuất **toàn bộ tập sau lọc** — điều đặc tả yêu cầu; và
- (ii) xuất **đúng những dòng của trang hiện tại**.

Cả hai đều cho cùng kết quả trong điều kiện `M < 20`. Điều này **không ảnh hưởng verdict C1**, vì điều đối tác nêu là *xuất THỪA (toàn bộ 14)* — và điều đó đã bị bác bỏ dứt khoát. Muốn tách bạch (i)/(ii) phải có `M > 20` (cần seed ≥7 bản ghi) hoặc đổi cỡ trang; **cả hai đều nằm ngoài vế đối tác nêu** nên không thực hiện (luật khoá 1 + 4 FLOW 04). Ghi lại thành **candidate một dòng** ở §6.

---

## 4. Vế C2 — tệp xuất có trường Người tạo / Ngày tạo  ·  quan hệ `GAP` · route `BA`

> 🔴 **Chỉ đo hiện trạng để trả lời BA. CẤM Pass, CẤM Reopen vế này.** Dùng lại **chính tệp đã tải ở C1**, không bấm lại nút.

### 4.1 Nguyên văn hàng tiêu đề tệp xuất

Đọc bằng `openpyxl`, in nguyên văn từng ô của hàng 1 — **giống hệt nhau ở CẢ HAI tệp** (A và B):

```
col1 = 'Mã KH'
col2 = 'Tên kế hoạch'
col3 = 'Năm'
col4 = 'Từ ngày'
col5 = 'Đến ngày'
col6 = 'Ngân sách (VNĐ)'
col7 = 'Trạng thái'
```

- Số cột: **7** · Tên trang tính: **`Kế hoạch đào tạo`**

### 4.2 Đối chiếu theo NGHĨA của cột (không so chuỗi cứng)

Đã soát từ đồng nghĩa theo bẫy (c) của chuẩn chấm — `Người lập` · `Ngày lập` · `Thời điểm tạo` · `Cán bộ tạo` · `Ngày khởi tạo` · `Ngày tạo KH`:

| Trường TKM nêu | Có cột nào mang nghĩa đó trong tệp không? |
|---|---|
| **Người tạo** (họ tên cán bộ tạo) | **KHÔNG.** 7 cột đều đã xác định nghĩa rõ; không cột nào chứa họ tên người. Đã đọc giá trị dữ liệu từng dòng để chắc: `Mã KH` chứa mã, `Tên kế hoạch` chứa tên kế hoạch, `Năm`=2026, `Từ ngày`/`Đến ngày` chứa ngày hiệu lực của kế hoạch (vd `01/09/2026`, `31/12/2026`), `Ngân sách (VNĐ)` chứa số tiền, `Trạng thái` chứa nhãn trạng thái. |
| **Ngày tạo** (ngày lập bản ghi) | **KHÔNG.** Hai cột ngày duy nhất là `Từ ngày`/`Đến ngày` — đối chiếu giá trị với màn cho thấy đó là **thời gian hiệu lực của kế hoạch**, không phải ngày tạo bản ghi. Ví dụ quyết định: bản ghi `KH-20260803-0003` có `Từ ngày`=05/07/2026, `Đến ngày`=25/07/2026 trong tệp, trong khi **`Ngày tạo` trên màn là 03/08/2026** — ba giá trị khác nhau ⇒ tệp **không** chứa ngày tạo dưới bất kỳ nhãn nào. |

Ngoài ra tệp cũng **không có** cột `Số chương trình` (cột này có trên bảng màn) — ghi lại phục vụ câu hỏi BA số 2, **không** mở thêm phép đo.

### 4.3 Ánh xạ vào bảng verdict

**C2: tệp KHÔNG có 2 trường.** Vẫn giữ nguyên quan hệ `GAP` đã khoá ở Giai đoạn A — không có dòng SRS mới nào đọc được trong lượt này quy định danh mục cột của tệp xuất, nên **không đủ điều kiện đổi quan hệ** (luật khoá 5).

Neo đặc tả cho phần GAP (tự mở lại, đã xác minh bằng `grep -n` trong lượt này):
- `srs-fr-03-dao-tao.md:1795` — `| Người tạo | Họ tên cán bộ tạo |`
- `srs-fr-03-dao-tao.md:1796` — `| Ngày tạo | dd/mm/yyyy |`
  → **Đây là đặc tả BẢNG TRÊN MÀN** (SCR-III-00 Thành phần 3), không phải của tệp xuất.
- `srs-fr-03-dao-tao.md:1189-1200` — `Outputs — Danh sách` của FR-III-14, 8 trường (`id`, `ten_ke_hoach`, `nam`, `thoi_gian`, `ngan_sach_du_kien`, `so_ctdt`, `trang_thai`, `total_count`) — **không có** `nguoi_tao` / `ngay_tao`
- Tiền lệ chứng minh SRS *biết cách* đặc tả cột tệp xuất khi muốn: `srs-fr-03-dao-tao.md:609-625` — FR-III-05 có hẳn bảng `Outputs` 13 trường cho tệp Xuất Excel kết quả
- `srs-v3.5.md:67` — lịch sử phiên bản 3.5 mục (5): *"**Câu hỏi BA chưa quyết** (defer Sprint sau): cite TT 17/2025/TT-BTP, NĐ55/2019 Đ.8 K.1, **mẫu xuất Excel** UC159."*

---

## 5. Quan sát phụ cùng màn (gate "bug mới") — KHÔNG có bug mới

Chuẩn chấm §6 yêu cầu kiểm: **bảng TRÊN MÀN** có hiển thị `Người tạo` / `Ngày tạo` không? Nếu thiếu thì đó là vi phạm SRS **nói rõ** (`:1795-1796`) và phải log bug mới riêng.

Đã đọc tiêu đề bảng trên màn bằng `innerText` (chữ người dùng nhìn thấy), không dùng `textContent`:

```
["", "Mã kế hoạch", "Tên kế hoạch", "Năm", "Từ ngày", "Đến ngày",
 "Ngân sách (VNĐ)", "Số chương trình", "Trạng thái", "Người tạo", "Ngày tạo", "Hành động"]
```

Và giá trị thực của dòng dữ liệu: `... | "Nháp" | "CB Nghiệp vụ - Trung ương" | "03/08/2026" | ...`

> ✅ **Bảng trên màn CÓ đủ cả `Người tạo` và `Ngày tạo`, có dữ liệu thật.** Đúng `srs-fr-03-dao-tao.md:1795-1796`.
> ⇒ **KHÔNG phát sinh bug mới.** Khoảng trống chỉ nằm ở **tệp xuất**, đúng phạm vi vế C2 (`GAP` → BA).

Bảng có cuộn ngang nên 3 cột cuối bị khuất ở khung nhìn mặc định — đã cuộn bảng sang phải và chụp lại để bằng chứng nhìn thấy được, tránh kết luận nhầm "thiếu cột" do khuất tầm nhìn.

---

## 6. Ánh xạ bảng verdict §1 của prompt

| C1 đo được | C2 đo được | → hàng khớp |
|---|---|---|
| **ĐẠT** (tệp = `M`, cả 2 bộ lọc) | **tệp KHÔNG có 2 trường** | **hàng 2** của bảng §1 |

### 🔴 VERDICT LOGIC: **Cần BA**

### Giá trị đề nghị ô `Trạng thái dev fix`: **`BA confirm`**

**Không có nhánh Pass thuần** cho case này vì vế C2 mang quan hệ `GAP` đã khoá từ Giai đoạn A.

**Bug mới:** KHÔNG có (§5 — bảng trên màn đạt đặc tả).

**Candidate (một dòng, KHÔNG điều tra trong case này):**
- *Chưa tách bạch được "tệp xuất toàn bộ tập sau lọc" với "tệp xuất đúng dòng của trang hiện tại", vì mọi `M` đo được (4 và 1) lẫn tổng `N` (14) đều nhỏ hơn cỡ trang 20; muốn xác nhận phải seed ≥7 bản ghi hoặc đổi cỡ trang — nằm ngoài vế đối tác nêu.*

**Seed / mutate:** KHÔNG có. Không tạo/sửa/xoá bản ghi nào trên env `18.143.165.120.nip.io`.

---

## 7. Artifact

| # | Đường dẫn | Điều nó chứng minh | Mốc giờ |
|---|---|---|---|
| 1 | [`../image/QLLKHDTBD_09-01-loc-trangthai-daduyet-man-4-ketqua.png`](../image/QLLKHDTBD_09-01-loc-trangthai-daduyet-man-4-ketqua.png) | Tiền đề phép đo A: tab `Đã duyệt 4` đang chọn, chân bảng `Hiển thị 1-4 / 4 kết quả`, nút `Xuất Excel` có mặt; tab `Tất cả 14` cho thấy `N`=14 ⇒ `M < N`. Badge tài khoản `CB Nghiệp vụ - Trung ương #02` · `BTP · TW` | 2026-08-07 03:02 |
| 2 | [`../image/QLLKHDTBD_09-02-man-luc-bam-xuat-excel-loc-daduyet-4ketqua.png`](../image/QLLKHDTBD_09-02-man-luc-bam-xuat-excel-loc-daduyet-4ketqua.png) | Trạng thái màn tại thời điểm bấm `Xuất Excel` ở phép đo A (4 kết quả, 4 mã đúng như tệp) | 2026-08-07 03:03 |
| 3 | [`../image/QLLKHDTBD_09-03-loc-ngay-01.07-31.07-man-1-ketqua.png`](../image/QLLKHDTBD_09-03-loc-ngay-01.07-31.07-man-1-ketqua.png) | Tiền đề phép đo B: hai ô lọc mang đúng `01/07/2026` và `31/07/2026` (tái hiện neo đối tác), chân bảng `Hiển thị 1-1 / 1 kết quả` | 2026-08-07 03:05 |
| 4 | [`../image/QLLKHDTBD_09-04-bang-tren-man-CO-cot-nguoitao-ngaytao.png`](../image/QLLKHDTBD_09-04-bang-tren-man-CO-cot-nguoitao-ngaytao.png) | **Bảng trên màn CÓ cột `Người tạo` (`CB Nghiệp vụ - Trung ...`) và `Ngày tạo` (`03/08/2026`)** ⇒ căn cứ kết luận KHÔNG có bug mới ở §5 | 2026-08-07 03:07 |

> Cả 4 ảnh đã **mở lại xem** và xác nhận nội dung khớp mô tả trước khi dẫn.
>
> **Ghi chú về ảnh thông báo:** ảnh #2 chụp trượt lớp thông báo (chụp quá sớm, thông báo chưa kịp dựng). Theo FLOW 04 §7 *"không lặp thao tác chỉ để chụp lại output thoáng qua; dùng chữ đã bắt + phản hồi máy chủ"*, **không bấm lại nút** để chụp bù. Bằng chứng thông báo dùng: chữ do bộ bắt ghi lại (`Xuất Excel thành công`, đúng 1 lần, `soObserverDangSong = 1`) + request `POST .../export` kèm nguyên bộ tham số lọc.

## 8. Tệp đã giữ lại

Verdict phụ thuộc nội dung tệp ⇒ giữ lại chính tệp (không thay bằng ảnh/thông báo):

| Tệp | sha256 | md5 |
|---|---|---|
| [`../seed-files/QLLKHDTBD_09-A-loc-trangthai-DaDuyet-1786046602595.xlsx`](../seed-files/QLLKHDTBD_09-A-loc-trangthai-DaDuyet-1786046602595.xlsx) | `5cf082c473357c8b608bc8e62f3c246a4717fc9210f7494d8eefb1594b58bcae` | `7b8284683491c4997b5f1e39e37aef87` |
| [`../seed-files/QLLKHDTBD_09-B-loc-ngay-0107-3107-1786046777916.xlsx`](../seed-files/QLLKHDTBD_09-B-loc-ngay-0107-3107-1786046777916.xlsx) | `62e1eb2dbb8ee0dceadc874f2e09cce4c8d46b57c00c9894236270850bff8fad` | `59963668ba6f18520aa291f0b2e0aebe` |

Phản hồi thô của máy chủ (số thô `meta.total`, dùng để truy lại `N`/`M`):
- `../seed-files/QLLKHDTBD_09-00-khong-loc.network-response` (`meta.total` = 14)
- `../seed-files/QLLKHDTBD_09-01-loc-trangthai-DA_DUYET.network-response` (`meta.total` = 4)
- `../seed-files/QLLKHDTBD_09-02-loc-ngay-0107-3107.network-response` (`meta.total` = 1)

---

## 9. Cổng chốt verdict — trả lời đủ 5 câu

1. **Mỗi vế neo vào dòng SRS nào?** C1 → `srs-v3.5.md:5570` + `srs-fr-03-dao-tao.md:2243` / `:1775` / `:1175`. C2 → `srs-fr-03-dao-tao.md:1795-1796` (bảng màn) đối lại `:1189-1200` (Outputs) + `srs-v3.5.md:67`. **Toàn bộ tự mở file đọc lại trong lượt này**, xác minh số dòng bằng `grep -n`; không bê từ hồ sơ cũ.
2. **Mọi thao tác có trả lời một vế Cn không?** Có. Đổi tab + nhập 2 ô ngày = dựng tiền đề `M < N` cho C1; bấm `Xuất Excel` = hành động tranh chấp của C1; mở tệp = đối chứng độc lập của C1 và là phép đo hiện trạng của C2; đọc tiêu đề bảng màn = quan sát phụ mà chuẩn chấm §6 yêu cầu. Không thao tác nào ngoài các mục trên.
3. **Vế `GAP` đã bị chặn Pass và có câu hỏi BA chưa?** Có — C2 giữ nguyên `GAP`, không Pass không Reopen; 3 câu hỏi BA ở §5.3 chuẩn chấm được giữ nguyên và điền `WEB HIỆN TẠI` bằng số đo thật.
4. **Đã đọc đầy đủ expected chưa?** Có — cả KQ mong đợi trên phiếu (vế lọc) lẫn ô TKM phản hồi lần 1 (vế Người tạo/Ngày tạo), cùng ảnh v2 và video vòng 1 đã mở ở Giai đoạn A.
5. **Điều kiện đo có khớp tiền đề case không?** Vai trò khớp (CB_NV_TW, đúng vai trò trong video đối tác). Bộ lọc B tái hiện **đúng** neo đối tác. Khác biệt duy nhất là **môi trường** (`18.143.165.120.nip.io` vs `htpldn-uat.ospgroup.vn` của đối tác) ⇒ đã xử lý bằng cách **chỉ so quan hệ `màn ↔ tệp` trong cùng một lần đo**, tuyệt đối không so số bản ghi tuyệt đối giữa hai môi trường.

> **Lưu ý bắt buộc theo §Ca biên:** không có ảnh trạng thái trước khi sửa của chính lượt đo này ⇒ **không kết luận "fix đã có tác dụng"**, chỉ kết luận **hiện trạng đúng/sai so với đặc tả**. Verdict chỉ có hiệu lực cho env + bản dựng + thời điểm đã ghi ở §1.
