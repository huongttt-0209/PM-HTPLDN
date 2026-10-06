# Phép đo — LBCKQTHCT_04 (dòng 337) · 2026-08-07 — Biểu mẫu **21b**

**Verdict logic: PASS** — 2/2 vế `MATCH` đều ĐẠT, ở cả chế độ chỉ đọc lẫn chế độ nhập.
Lỗi đối tác báo (*"thiếu cột Số liệu kỳ trước, Ghi chú"*) **không tái hiện trên bảng 21b**.

Chuẩn chấm: [`../chuan/LBCKQTHCT_04.md`](../chuan/LBCKQTHCT_04.md)

---

## 1. Gỡ 2 chặn tiền đề trước khi đo

Chuẩn chấm xếp đây là **case bị chặn nặng nhất**. Trạng thái thực tế của 2 chặn:

| Chặn | Nội dung | Cách gỡ |
|---|---|---|
| **1 — không đợt nào dùng 21b** | Cả 3 đợt đang có đều `bieuMauSuDung = MAU_21A` ⇒ theo `:1168` (*"khi bieu mau ap dung"*), 21b **không phải** hiện ⇒ đo bằng dữ liệu cũ rồi chấm FAIL là **Reopen oan** (bẫy 12) | ✅ **ĐÃ GỠ — seed đợt mới** (§2) |
| **2 — không đợt nào ở `DANG_LAP_BC`** | Cả 3 đợt `TAO_DOT` | ⚠️ **KHÔNG gỡ được** — xử như **tiền đề** theo luật khóa 1, xem §5 |

### Vế hợp lệ (sau khi áp luật khóa 1 của Flow 04)

Chuẩn chấm khóa 4 vế; **chỉ C1 + C2 là vế hợp lệ**. **C3** (đợt phải áp dụng 21b) và **C4** (hiển thị ngoài
`DANG_LAP_BC`) là **điều kiện SRS đặt ra để vế có hiệu lực** ⇒ luật khóa 1 buộc dùng làm **tiền đề**,
không tách thành vế/bug riêng. Xử lý này giống hệt case LBCKQTHCT_03 và **quyết trước khi biết kết quả đo**.

| Vế | Expected đối tác | SRS | Quan hệ | Route |
|---|---|---|---|---|
| **C1** | Bảng **21b** cho cán bộ thấy **số liệu kỳ trước** theo từng chỉ tiêu | `:1168` *"Tuong tu 21a"* → `:1167` | MATCH | TEST |
| **C2** | Bảng **21b** có **chỗ ghi chú** | `:1168` → `:1167`; củng cố bởi master `srs-v3.5.md:6699` `\| -14 \| Ghi chú \| Nhập thủ công \|` | MATCH | TEST |

---

## 2. Seed — khai đầy đủ vì làm thay đổi môi trường chung

Không có đợt nào áp dụng 21b ⇒ bắt buộc tạo mới (`:625` — chỉ CB NV cấp TW được tạo đợt).

| Mục | Giá trị |
|---|---|
| Người tạo | **`cbnv_tw`** — *CB Nghiệp vụ - Trung ương*, `CB_NV_TW`, cấp `TW` |
| Endpoint | `POST /api/v1/dot-bao-caos` — schema đọc từ `/api/docs-json`, **không đoán tên trường** (`required: tenDot, phamViDonViNopIds, kyBaoCao, hanNop, tuNgay, denNgay, bieuMauSuDung`) |
| Đợt tạo ra | **`DOT-TRON_NAM-2026-1`** · id `a63a3214-d1d3-421b-8c0c-cec5db419413` |
| Tên đợt | `QA F5 reverify 21b - CA_HAI (LBCKQTHCT_04)` |
| **`bieuMauSuDung`** | **`CA_HAI`** — cố ý chọn để màn hiện **cả 2 bảng**, buộc phải phân biệt đúng 21a/21b bằng nhãn (chống bẫy 3) |
| Kỳ / phạm vi | `TRON_NAM` (chưa đợt nào dùng, tránh đụng dữ liệu sẵn có) · 2 đơn vị: Sở Tư pháp Hà Nội + đơn vị của `cbnv_dp_01` |
| Ghi chú lưu trong bản ghi | `Seed QA de do bieu mau 21b - phieu LBCKQTHCT_04 (reverify tuan 5, 07/08/2026)` |

⚠️ **Đợt seed này còn nằm lại trên môi trường** — cần thì xoá sau khi đối tác đọc xong kết quả.
`cbnv_tw` **chỉ dùng để tạo tiền đề**, **KHÔNG** dùng ra verdict (`:712` — TW không tự lập BC).

---

## 3. Điều kiện đo

| Mục | Giá trị |
|---|---|
| Env / bản dựng | `18.143.165.120.nip.io` · **`assets/index-D4Buvu4S.js`** (07/08/2026 02:23 VN) — đã đọc lại tên bó mã ngay trong tab |
| Tài khoản ra verdict | **`cbnv_hn`** — `CB_NV_DP`, cấp ĐP, Sở Tư pháp Hà Nội. Đúng tác nhân `:712` |
| Đợt đo | `DOT-TRON_NAM-2026-1` — `bieuMauSuDung = CA_HAI` ✅ (tiền đề #3 THỎA) |
| Trục ĐỢT `trangThai` | `TAO_DOT` (tiền đề #4 **không thỏa** — xem §5) |
| Trục ĐƠN VỊ `trangThaiNop` | `CHUA_NOP` → sau [Lập báo cáo] thành `DANG_LAP`, `baoCaoId = 1b3085b8-b00f-448f-bda7-f00cc52de895` |

---

## 4. Kết quả

### 4.1 Nhận diện bảng — bằng NHÃN, không bằng số dòng (bẫy 3)

Màn có **2 thẻ biểu mẫu**, nhãn đọc từ `.ant-card-head-title` và xác nhận lại độc lập qua cây trợ năng:

| Thẻ | Nhãn nguyên văn | Là bảng nào |
|---|---|---|
| #2 | **`Biểu mẫu 21a/TP/HTPLDN`** | 21a — thuộc case LBCKQTHCT_03 |
| #3 | **`Biểu mẫu 21b/TP/HTPLDN`** | **21b — bảng của case này** |

> ⚠️ Hai bảng **giống hệt nhau từng dòng**. Nếu nhận diện bằng số dòng hoặc bằng nội dung thì
> **chắc chắn đo nhầm**. Chỉ nhãn thẻ mới phân biệt được.

### 4.2 Bảng 21b — cả 2 chế độ

| Chế độ | `trangThaiNop` | Số cột | **Tiêu đề cột đọc được** | Số chỉ tiêu | Ô nhập |
|---|---|---|---|---|---|
| Chỉ đọc | `CHUA_NOP` | **4** | `Chỉ tiêu` · **`Số liệu kỳ trước`** · `Kỳ này` · **`Ghi chú`** | 13 | 0 |
| Nhập | `DANG_LAP` | **4** | `Chỉ tiêu` · **`Số liệu kỳ trước`** · `Kỳ này` · **`Ghi chú`** | 13 | **15** |

- **C1 ĐẠT** — cột *Số liệu kỳ trước* hiện ở cả 2 chế độ, giá trị `—` vì `soLieuKyTruoc = null`.
  🟢 **Bẫy 10 bị vô hiệu bằng số:** dữ liệu nguồn rỗng mà cột **vẫn hiện** ⇒ không phải "ẩn cột khi rỗng".
- **C2 ĐẠT** — ở chế độ nhập, **mỗi chỉ tiêu có 1 ô Ghi chú riêng**, `placeholder = "Ghi chú"`
  (13 ô Ghi chú + 2 ô số liệu chỉ tiêu 12/13 = 15). Không phải cột trang trí.
- Cuộn ngang: `scrollWidth 1009` vs `clientWidth 1005` — lệch 4px, **không cột nào bị giấu** (bẫy 4).
- Ảnh: [`../image/LBCKQTHCT_04-21b-du-4-cot-chidoc.png`](../image/LBCKQTHCT_04-21b-du-4-cot-chidoc.png) ·
  [`../image/LBCKQTHCT_04-21b-che-do-nhap-o-ghichu.png`](../image/LBCKQTHCT_04-21b-che-do-nhap-o-ghichu.png)

---

## 5. Tiền đề #4 không thỏa — khai rõ, không đổi verdict

`:1168` ràng buộc hiển thị *"khi bieu mau ap dung va **dot o DANG_LAP_BC**"*. Đợt seed vẫn `TAO_DOT`
sau khi bấm [Lập báo cáo] — **giống hệt hành vi đã đo ở case LBCKQTHCT_01**: phần mềm gác hiển thị theo
trục **ĐƠN VỊ**, không theo trục **ĐỢT**. Đây là **tiền đề**, không phải vế (luật khóa 1), và xử lý đối xứng:
thiếu cột trong tình huống này cũng **không được chấm FAIL**. Vấn đề trục ĐỢT được xử đúng chỗ ở phiếu
**TPDBCKQTHCT_01**.

---

## 6. Quan sát ngoài vế — ghi nhận, KHÔNG chấm, KHÔNG mở thêm phép đo

| # | Quan sát | Vì sao không chấm |
|---|---|---|
| 1 | 🟡 **Bảng 21b render y hệt 21a** — cùng 13 dòng chỉ tiêu, **không có** 2 cột định danh `STT` + `Sở/ban ngành`. Theo master `srs-v3.5.md` D.1.3 (`:6614–6622`) + D.2.2 (`:6698–6699`), mẫu 21b là **bảng tổng hợp cấp tỉnh, mỗi dòng 1 đơn vị**, khác hẳn 21a | `srs-fr-15:1168` — **nguồn prompt chỉ định** — nói đúng chữ *"Tuong tu 21a"*, dev đang làm **khớp** chữ đó. Hai tầng đặc tả lệch nhau (form nhập trên màn vs mẫu văn bản xuất). Expected của đối tác **chỉ nhắc 2 cột**, không nhắc cấu trúc dòng ⇒ luật khóa 1 cấm biến thành tiêu chí chấm. **Đề nghị BA làm rõ** (câu hỏi §9 chuẩn chấm), nhưng **không kéo verdict phiếu này** và **không đủ căn cứ mở dòng bug mới** vì chưa biết bên nào đúng |
| 2 | Thẻ **"Nhận xét, kiến nghị"** chỉ xuất hiện **sau khi vào chế độ nhập** | Thuộc phiếu **LBCKQTHCT_05** — cấm suy chéo (bẫy 7), case đó phải tự đo |
| 3 | Đợt `CA_HAI` bắt đơn vị nhập **cả 2 biểu mẫu** cùng lúc, không thấy chỗ chọn mẫu | `:742` nói *"đơn vị chọn mẫu phù hợp"*. Ngoài vế, ghi candidate |

Không thấy tràn/đè hay lẫn tiếng Anh trong bảng 21b.

---

## 7. Giới hạn hiệu lực

Chỉ có hiệu lực cho `18.143.165.120.nip.io` + bó mã `index-D4Buvu4S.js` (07/08/2026 02:23 VN).
Bằng chứng đối tác là **ảnh tĩnh** `LBCKQTHCT_04.jpg`, **tiêu đề thẻ bị cắt** nên không đọc được ảnh chụp
21a hay 21b, cũng không đọc được biểu mẫu áp dụng và trạng thái đợt — tức **chưa đủ chứng minh vi phạm
`:1168`**. Vì vậy QA tự dựng tiền đề và đo lại, **không** vì ảnh thiếu dữ kiện mà chấm "không phải lỗi".
