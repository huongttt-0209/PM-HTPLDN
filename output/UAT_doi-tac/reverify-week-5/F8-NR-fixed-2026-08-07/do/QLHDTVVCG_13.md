# Nhật ký đo — `QLHDTVVCG_13` (dòng 319 tab `bug`)

**Ngày:** 2026-08-07 · **Quy trình:** [`flows/04-verify-bug-dev-fix-khong-ho-so.md`](../../../../../flows/04-verify-bug-dev-fix-khong-ho-so.md)
**Chuẩn chấm đã khóa (Giai đoạn A — CẤM sửa):** [`chuan/QLHDTVVCG_13.md`](../chuan/QLHDTVVCG_13.md) — 3 vế: **C1 `MATCH`** · **C2 `GAP`** · **C3 `MATCH`** → route **BA**.

---

## 0. Đọc lại dòng phiếu trên bảng trước khi đo (bắt buộc)

Đọc lúc **14:16 ngày 07/08/2026** bằng `tools/sheet_dump_bug_rows_2026-08-07.py --rows 319` (chỉ đọc).

| Ô | Giá trị đọc được |
|---|---|
| `Mã TC` (D) | `QLHDTVVCG_13` |
| `Trạng thái` (N) `N/R` · `Dopai` (O) `N/R` | phiếu **chưa từng chạy** |
| `Kết quả thực tế` (L) · `Ảnh/vieo 1` (M) · `TKM phản hồi lần 1` (Q) | **RỖNG cả ba** |
| `Trạng thái dev fix` (R) | `Fixed` |
| `Kết quả verify` (T) | **RỖNG** ⇒ không có nội dung cũ để giữ |
| `Kết quả mong đợi` (K) | `- Hệ thống mở màn hình biểu mẫu ở chế độ "Thêm mới" với các trường trống; các trường "Mã hợp đồng" và "Bên A" được hệ thống tự điền.` |
| `DEV phản hồi lần 1` (S) | *"BA chốt 06/08/2026 — cụm Hợp đồng tư vấn (27 phiếu), Loại 4 hướng A: giữ quyết định BA 11/05/2026 bỏ menu riêng; phần mềm đúng bản gốc, test case mô tả lối vào đã hết hiệu lực (vào từ Chi tiết Vụ việc / Lịch sử TVV). Không sửa phần mềm theo lối vào cũ."* |

Không có thay đổi so với bản chụp 11:3x.

## 1. Môi trường + vân tay bản dựng

| Hạng mục | Giá trị |
|---|---|
| Môi trường | `https://18.143.165.120.nip.io` — env **NỘI BỘ** (đối tác nghiệm thu trên `htpldn-uat.ospgroup.vn`) |
| **Vân tay ĐẦU phiên** (14:14:57) | `GET /` → `assets/index-BbPPdate.js` · `assets/index-DVlgOkLg.css` · `last-modified: Fri, 07 Aug 2026 06:47:57 GMT` · `etag "6a757f9d-428"` |
| Bó mã trình duyệt thực nạp | `evaluate_script` đọc `<script src>` → **`/assets/index-BbPPdate.js`** (khớp) |
| Nhãn thanh bên | `HTPLDN · V1.0.10` — **không** dùng làm định danh |
| Tài khoản đo | **`cbnv_tw_03`** / `Test@1234` — đăng nhập bằng **giao diện thật** + mã 6 số ở MailHog lúc 14:16. Không gặp `ERR-AUTH-SYS-00-03`, **không** phải fallback sang `_05`. |
| Danh tính đọc được sau khi đăng nhập | `hoTen` = `CB Nghiệp vụ - Trung ương #03` · `vaiTro` = `CB_NV_TW` · `capDonVi` = `TW` · `donViId` = `00000000-0000-4000-8000-000000000001` |
| **Tên đơn vị của tài khoản** (cần cho C3) | `GET /api/v1/don-vi/00000000-0000-4000-8000-000000000001` → `tenDonVi` = **`Cục Bổ trợ tư pháp - Bộ Tư pháp`**, `maDonVi` = `BTP-TW` |
| Cửa sổ | 1440×900 (cấu hình MCP của lô) |

## 2. §Đường vào — bước J nói một đằng, phần mềm làm một nẻo (tiền đề, KHÔNG phải vế chấm)

Bước J ghi *"Chọn menu Hợp đồng Tư vấn"*. **Xác nhận bằng mắt:** thanh bên có đúng 14 mục
(Tổng quan · Hỏi đáp pháp lý · Đào tạo tập huấn · Mạng lưới Tư vấn viên · Vụ việc HTPL · Chi trả chi phí ·
Doanh nghiệp · Đánh giá hiệu quả · Biểu mẫu · Tư vấn · Chương trình HTPLDN · Đợt báo cáo · Báo cáo thống kê ·
Quản trị hệ thống) — **KHÔNG có mục "Hợp đồng Tư vấn"**. Đúng `srs-fr-14-hop-dong-tv.md:266`, `:268`.
Đây là **tiền đề/đường đi**, **không tách thành vế, không log bug, không FAIL phiếu vì lý do này**.

**Đường thực tế đã đi (bề mặt chấm chính thức của cả đợt A — MÀN 1):**

```
Thanh bên "Vụ việc HTPL" → ô tìm "VV-BTP-TW-20260804-002" → [Tìm kiếm] → nút Xem vụ việc
→ trang Chi tiết vụ việc → mở accordion "HĐ tư vấn liên kết" → nút [+ Tạo hợp đồng]
```

Chọn màn này vì: (a) thanh lọc của nó khớp **chính xác** `:287` (từ khóa tên/mã/bên B + chọn tư vấn viên +
khoảng ngày); (b) đây là nơi **duy nhất** có nút mở biểu mẫu thêm mới.

**Màn thứ hai đã quan sát (ghi làm dữ kiện cho câu hỏi BA §5.1, KHÔNG chấm):**
Chi tiết Tư vấn viên → tab *"Lịch sử hỗ trợ"* → mục *"Hợp đồng tư vấn"*. Màn này **không có** nút tạo hợp đồng,
thanh lọc chỉ 2 nhóm, bảng chỉ 6 cột. Xem [`do/QLHDTVVCG_02.md`](QLHDTVVCG_02.md) §hình thái để so hai màn.

Yêu cầu gửi đi chứng minh hai màn là hai ngữ cảnh khác nhau (đọc từ tab Mạng):
`GET /api/v1/hop-dong-tu-vans?vuViecId=6bf98a2e-…` (màn 1) ↔ `GET /api/v1/hop-dong-tu-vans?tuVanVienId=38383838-…` (màn 2).

## 3. Tiền đề

**Không cần seed** (chuẩn chấm §c). Chỉ cần một vụ việc để mở biểu mẫu từ đó.
Dùng **`VV-BTP-TW-20260804-002`** (`6bf98a2e-77ee-4c03-8e1f-a51561406a3b`), đang có **0 hợp đồng liên kết**.

**Kỷ luật thao tác đã giữ:** trong cả phiên **chưa mở bản ghi hợp đồng nào** trước đó; biểu mẫu được mở bằng
**đúng một lần bấm** nút [+ Tạo hợp đồng] — loại trừ khả năng biểu mẫu còn giữ giá trị của lần mở trước.

## 4. Đo từng vế

### C1 — Biểu mẫu mở ở chế độ Thêm mới, các trường trống · `MATCH` · ✅ **ĐẠT**

Yêu cầu: `srs-fr-14-hop-dong-tv.md:279`, `:290` + cột **Mặc định** của bảng Inputs `:82`, `:84`–`:92` (đều `—`).

**Đường 1 — giao diện thật.** Bấm **[+ Tạo hợp đồng]** lúc **14:22:46** → mở hộp thoại tiêu đề
**"Tạo hợp đồng tư vấn"**. Đọc `value` từng ô nhập của người dùng (đọc thuộc tính `value`, **không** đọc
`placeholder`):

| Ô người dùng nhập (theo `:82`, `:84`–`:92`) | `value` đọc được | `placeholder` |
|---|---|---|
| Tên hợp đồng | **`""` (rỗng)** | `Nhập tên hợp đồng` |
| Số hợp đồng | **`""`** | `Nhập số hợp đồng` |
| Bên B | **`""`** | `Tên bên B` |
| Tư vấn viên / Chuyên gia | **`""`** | *(gợi ý "Gõ mã hoặc họ tên…")* |
| Giá trị hợp đồng (VNĐ) | **`""`** | `Nhập giá trị hợp đồng` |
| Thời gian thực hiện (ngày bắt đầu / kết thúc) | **`""`** | `Ngày bắt đầu` |
| Ngày ký | **`""`** | `Chọn thời điểm` |
| Nội dung hợp đồng | **`""`** (bộ đếm `0 / 10000`) | `Nhập nội dung hợp đồng` |
| Ghi chú | **`""`** (bộ đếm `0 / 2000`) | `Nhập ghi chú` |

Ba nhóm con cũng ở trạng thái khởi tạo: **Mốc tiến độ** chỉ có nút `[+ Thêm mốc tiến độ]` (0 dòng) ·
**Thanh toán giai đoạn** `Đã thanh toán: 0 VNĐ · Tổng 0 giai đoạn: 0 VNĐ · 0%` · **Tài liệu đính kèm** trống.

**Đường 2 — đối chứng độc lập, đọc danh sách yêu cầu gửi đi của chính lượt bấm đó.** Sau khi bấm, phần mềm
gửi đúng 4 yêu cầu: `GET /api/v1/auth/me` · `GET /api/v1/hop-dong-tu-vans/ma-preview` ·
`GET /api/v1/tu-van-viens?trangThai=HOAT_DONG&pageSize=50` · `GET /api/v1/to-chuc-tu-vans?trangThai=HOAT_DONG&pageSize=50`.
**KHÔNG có** yêu cầu đọc bản ghi hợp đồng nào (`/hop-dong-tu-vans/{id}`) ⇒ chứng minh đây là **chế độ tạo mới
thật**, không phải mở nhầm một bản ghi cũ ở chế độ sửa.

**Hai đường khớp nhau ⇒ DỪNG.**

> **Quan sát kèm theo, KHÔNG dùng để Fail:** ô **"Vụ việc liên kết"** hiện sẵn `VV-BTP-TW-20260804-002` và
> ô **"Trạng thái"** hiện sẵn `Đang thực hiện`. Cả hai **nằm ngoài** danh sách ô mà chuẩn chấm C1 liệt kê.
> Trạng thái là **giá trị mặc định của thực thể** (`:396` `'DANG_THUC_HIEN'`); vụ việc liên kết là **hệ quả
> trực tiếp của đường vào** (mở biểu mẫu từ trong chính vụ việc đó). Ghi lại làm dữ kiện cho BA.

### C2 — Thời điểm hiện "Mã hợp đồng" · `GAP` · ⏸ **CHỈ GHI HIỆN TRẠNG, KHÔNG CHẤM**

Điểm mâu thuẫn đã khóa ở Giai đoạn A: `:290` khai "Mã (auto)" **như một trường trên biểu mẫu**, còn `:119`
xếp việc sinh mã vào **bước xử lý khi lưu**; đặc tả **không phát biểu** mã phải hiện ngay lúc mở biểu mẫu.

**Hiện trạng đo được:** ngay khi biểu mẫu vừa mở, ô **Mã hợp đồng** đã có sẵn giá trị
**`HDTV-20260807-0006`** (ô hiển thị dạng chỉ-đọc, nền xám). Đối chứng: phần mềm gọi
`GET /api/v1/hop-dong-tu-vans/ma-preview` → phản hồi `200`:

```json
{"success":true,"data":{"maHopDong":"HDTV-20260807-0006"},"meta":null}
```

Chuỗi máy chủ trả về **trùng khít** chuỗi hiển thị. ⇒ **Web hiện tại ĐÚNG y kỳ vọng đối tác** (mã tự điền
ngay khi mở biểu mẫu), và dev đã dựng hẳn một điểm cuối riêng cho việc xem trước mã.

🔴 Theo luật khóa 5 (flow 04) và QĐ-01: **kết quả đo không biến `GAP` thành `MATCH`** — **không Pass, không
Reopen** vế này. Câu hỏi BA: **mã hợp đồng hiện ngay khi mở biểu mẫu hay chỉ sau khi lưu?** Mục đích là
**bổ sung điều này vào đặc tả**, KHÔNG phải chặn bàn giao.

### C3 — "Bên A" được hệ thống tự điền · `MATCH` · ✅ **ĐẠT**

Yêu cầu: `srs-fr-14-hop-dong-tv.md:83` (Mặc định `auto đơn vị`, Nguồn `hệ thống`) + `:290` ("Bên A (auto đơn vị)").

**Đường 1 — giao diện thật.** Ô **Bên A** có `value` = **`Cục Bổ trợ tư pháp - Bộ Tư pháp`**, trong khi
`placeholder` của chính ô đó là `Tên bên A`. ⇒ đây là **giá trị thật**, không phải chữ mờ gợi ý (đúng bẫy
Pass oan §d mục 1). Ảnh chụp cho thấy chữ đen đậm, khác hẳn chữ mờ của các ô còn trống.

**Đường 2 — đối chứng độc lập, hồ sơ tài khoản đọc từ máy chủ.** `GET /api/v1/auth/me` → `donViId` =
`00000000-0000-4000-8000-000000000001`; `GET /api/v1/don-vi/00000000-0000-4000-8000-000000000001` →
`tenDonVi` = **`Cục Bổ trợ tư pháp - Bộ Tư pháp`**.

Chuỗi trên biểu mẫu **trùng khít từng chữ** với tên đơn vị của **chính tài khoản đang đăng nhập** ⇒ loại được
bẫy "tự điền nhưng sai đơn vị". **Hai đường khớp ⇒ DỪNG.**

## 5. Verdict

**Cần BA** → ô `Trạng thái dev fix` (R) = **`BA confirm`**.

- C1 `MATCH` ✅ đạt · C3 `MATCH` ✅ đạt ⇒ **không vế `MATCH` nào còn lỗi** ⇒ không Reopen.
- C2 vẫn là `GAP` (đặc tả tự mâu thuẫn về **thời điểm** sinh mã) ⇒ theo QĐ-01 hàng 3: **`BA confirm`**,
  KHÔNG phải `Test done`.
- ⚠️ Flow 04 §Ca biên: đội **không có ảnh "lỗi cũ"** (đối tác chưa từng chạy phiếu) ⇒ chỉ kết luận
  **hiện trạng đúng yêu cầu**, **không** viết "bản sửa đã có tác dụng".
- **KHÔNG bấm Lưu** — đóng biểu mẫu bằng nút **[Hủy]** lúc 14:24. Hành vi lưu thuộc phiếu `_15`.

## 6. Ghi nhận (KHÔNG chấm, không kéo verdict) — gửi dev/BA

1. Biểu mẫu **có** hai trường `Số hợp đồng` và `Ngày ký` — hai trường này có ở phần thực thể (`:385`, `:390`)
   nhưng **không** được liệt kê ở bảng thành phần `:290`. Thừa thành phần ⇒ ghi nhận cho BA, **không** Fail.
2. Nhãn nút thực tế là **[+ Tạo hợp đồng]**, phiếu ghi `[+ Thêm hợp đồng]`, `:286` cũng ghi
   `[+ Thêm hợp đồng]`, còn Phụ lục E §H4 (`srs-v3.5.md:6756`) bắt nhãn **"Thêm mới"** — ba nguồn lệch nhau.
   Cột `Kết quả mong đợi` của phiếu **không chấm nhãn nút** ⇒ **không** Fail; gộp vào câu hỏi BA §5.5.
3. Biểu mẫu là **hộp thoại** (modal), không phải trang mới — `:272` khai "Form (trang mới/modal/drawer)",
   cả ba hình thức đều hợp lệ ⇒ **không** Fail.
4. Nút xác nhận của biểu mẫu ghi **[Thêm mới]** (không phải [Lưu]); nút hủy ghi **[Hủy]**.

## 7. Quan sát ngoài vế — **candidate**, KHÔNG log thành bug

| # | Hiện tượng | Xuất hiện tại | Vì sao chỉ là candidate |
|---|---|---|---|
| 1 | Mục **"Tài liệu đính kèm"** trên biểu mẫu **Thêm mới** không cho chọn tệp, chỉ hiện dòng chữ *"Vui lòng lưu hợp đồng trước khi đính kèm tài liệu."* Trong khi `:92` khai `file_dinh_kem` là **đầu vào của FR-X.3-01** và `:290` liệt kê **"File đính kèm"** là trường của **trang thêm/sửa** | ngay khi mở biểu mẫu Thêm mới, ảnh `…-03-…` | Đây thuộc vế **C2 của phiếu `_15`** ("tạo bản ghi cùng … tệp đính kèm đã nhập"), không thuộc vế nào của `_13`. Chuyển sang `_15` đo và kết luận; `_13` chỉ ghi nhận |

## 8. Dữ liệu đã thay đổi trên môi trường (bắt buộc khai)

| Đổi gì | Bản ghi nào | Env | Lúc |
|---|---|---|---|
| **KHÔNG có thay đổi nào** | — | `18.143.165.120.nip.io` (nội bộ) | — |

Phiếu này chỉ **mở** biểu mẫu rồi bấm **[Hủy]**; không lưu, không tạo bản ghi, không sửa bản ghi nào.
Mã `HDTV-20260807-0006` chỉ là **xem trước** (`ma-preview`), **chưa** được cấp cho bản ghi nào.

## 9. Ảnh bằng chứng (đã mở lại xem từng ảnh trước khi dùng)

| Ảnh | Chứng minh điều gì | Link Drive |
|---|---|---|
| `QLHDTVVCG_13-01-muc-HD-tu-van-lien-ket-tren-chi-tiet-vu-viec.png` | Đường vào thực tế: mục "HĐ tư vấn liên kết" trong Chi tiết vụ việc, có nút [+ Tạo hợp đồng] và thanh lọc 3 nhóm | https://drive.google.com/file/d/1s5eRH0ReJ5XY3-KsC1Bf-8Qy3UYs3N8Q/view?usp=drivesdk |
| `QLHDTVVCG_13-02-bieu-mau-them-moi-ma-va-ben-A-tu-dien.png` | C1+C2+C3: biểu mẫu "Tạo hợp đồng tư vấn" vừa mở — Mã đã tự điền `HDTV-20260807-0006`, Bên A đã tự điền `Cục Bổ trợ tư pháp - Bộ Tư pháp` (chữ đen), Tên HĐ / Số HĐ / Bên B còn trống (chữ mờ gợi ý) | https://drive.google.com/file/d/1qymUuEc2jEqkB9seNAVYlHwy7zygY5Mj/view?usp=drivesdk |
| `QLHDTVVCG_13-03-bieu-mau-them-moi-cac-nhom-con-deu-trong.png` | C1: phần dưới biểu mẫu — Nội dung/Ghi chú trống, Mốc tiến độ 0 dòng, Thanh toán giai đoạn 0%, và dòng chữ "Vui lòng lưu hợp đồng trước khi đính kèm tài liệu" (candidate §7) | https://drive.google.com/file/d/1fj-A_6RwPm4ZkxoVjqxouGS5MFPPSK5v/view?usp=drivesdk |

## 10. Cổng chốt verdict — trả lời đủ 5 câu (flow 04)

1. **Neo đặc tả:** C1 → `srs-fr-14-hop-dong-tv.md:279`, `:290`, `:82`, `:84`–`:92`; C2 → `:81`, `:119`, `:290`
   (mâu thuẫn); C3 → `:83`, `:290`. Số dòng lấy từ khóa chuẩn chấm Giai đoạn A đã tự mở file đếm lại hôm nay.
2. **Mọi thao tác ánh xạ về vế:** tìm vụ việc + mở chi tiết + mở accordion (tiền đề/đường vào) · một lần bấm
   [+ Tạo hợp đồng] (C1) · đọc `value` từng ô (C1, C2, C3) · đọc danh sách yêu cầu gửi đi (đối chứng C1) ·
   đọc phản hồi `ma-preview` (đối chứng C2) · đọc hồ sơ tài khoản + đơn vị (đối chứng C3). Không thao tác thừa.
3. **Vế `GAP` đã bị chặn Pass:** C2 — có câu hỏi BA đúng phần mâu thuẫn (thời điểm sinh mã), nêu rõ web hiện
   tại đúng kỳ vọng đối tác và mục đích là bổ sung vào đặc tả.
4. **Đã đọc đầy đủ phiếu:** đọc lại trọn dòng 319 lúc 14:16, gồm cả ô `DEV phản hồi lần 1`.
5. **Điều kiện đo khớp phiếu:** vai trò **Cán bộ Nghiệp vụ** (`:68`, `:286`, `:290` — nút thêm và trang biểu
   mẫu **chỉ** dành cho CB NV) · điều kiện (H) chỉ đòi đăng nhập thành công · bước J thao tác "nhấn nút thêm
   hợp đồng" đã thực hiện bằng giao diện thật. Lệch duy nhất là **đường vào** (menu không tồn tại theo thiết kế)
   — đã xử theo §2, không đổi kết quả.
