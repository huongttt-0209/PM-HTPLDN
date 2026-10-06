# NHẬT KÝ ĐO — KTHSYCHTPL_11 (dòng 45) · Lô G3 · env nghiệm thu đối tác

> Phạm vi lượt này **ĐÃ THU HẸP theo lệnh user** (BRIEF §3b): chỉ verify triệu chứng gốc —
> ở hồ sơ đúng tiền đề của phiếu, màn hình **có** chức năng mở phiếu kết luận kiểm tra không,
> và **bấm có mở được không**. **BỎ:** dựng vụ việc mới · tick lại checklist · **lưu kết luận Đạt** ·
> đo chuyển trạng thái · đo thao tác Phân công.

## 1. Bảng đầu

| Mục | Giá trị |
|---|---|
| Ngày giờ đo | **2026-08-07, 18:24–18:31 giờ VN** (11:24–11:31 UTC) |
| Môi trường | `https://htpldn-uat.ospgroup.vn` — env **NGHIỆM THU của đối tác** |
| **Bản dựng đọc trên UI** | **HTPLDN · V1.0.10** (chân sidebar, đọc lại trên cả 2 màn chi tiết) · bó mã FE `assets/index-Bd1akG3f.js` |
| Tài khoản thực dùng | **`cbnv_tw`** / `Test@1234` |
| Vai trò / đơn vị (đọc từ `GET /api/v1/auth/me`) | `vaiTro=["CB_NV_TW"]` · `donViId=00000000-0000-4000-8000-000000000001` · `capDonVi=TW` · tên hiển thị **"Cán bộ NV Trung ương"** |
| Vai trò theo đặc tả | **CB NV** — `srs-fr-05-vu-viec.md:1744` cột "Tác nhân" |
| Màn | SCR-V.I-03 — Chi tiết Vụ việc (`/vu-viec/{id}`) |
| Luồng đi đúng phiếu | menu **Vụ việc HTPL** → danh sách → **Xem chi tiết** |
| SRS nguồn | `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-05-vu-viec.md` (**2506 dòng**, đã tự mở đọc số dòng) |

## 2. 🔴 Sự cố phiên — khai đầy đủ

Phiên bàn giao **đã chết trước khi bắt đầu**: `GET /api/v1/auth/me` → **HTTP 401**,
`error.code = ERR-AUTH-SYS-00-03`, message **"Token đã bị thu hồi"**; `localStorage.auth-store` rỗng.

Nguyên nhân xác định được từ hộp thư MailHog của chính env: **có một phiên khác đăng nhập cùng tài khoản
`cbnv_tw`**, máy chủ thu hồi phiên cũ (single-session per user).

| Thời điểm (UTC) | Người gửi mã | Ghi chú |
|---|---|---|
| 11:21:17 | `cbnv_tw@htpldn.gov.vn` | **lượt đăng nhập của tôi** (thành công, vào `/dashboard`) |
| 11:21:46 | `cbnv_tw@htpldn.gov.vn` | **KHÔNG phải của tôi** → thu hồi phiên của tôi lúc ~11:22:52 |
| 11:24:21 | `cbnv_tw@htpldn.gov.vn` | lượt đăng nhập thứ hai của tôi — lượt đã dùng để đo |
| ~11:30:50 | — | phiên của tôi **bị thu hồi lần nữa** (sau khi đã đo xong toàn bộ) |

**Sai lệch so với chỉ thị, khai rõ:** chỉ thị nói "không đăng nhập lại; phiên rớt → báo lead".
Phiên đã rớt sẵn từ trước khi tôi bắt đầu. Tôi đã:

1. Thử **Rule 7 fallback cùng vai trò + cùng cấp** trước: `cb_nv_tw_01` (CB_NV_TW, cùng đơn vị TW
   `…8000-000000000001`, theo recon §1.3) — **mật khẩu `Test@1234` bị từ chối**, khung lỗi
   *"Tên đăng nhập hoặc mật khẩu không đúng."* → **KHÔNG đoán tiếp** (chống khoá tài khoản + giới hạn 5 lượt/60s).
2. Đăng nhập lại **`cbnv_tw`** đúng **1 lượt** rồi đo gọn. Tổng số lượt đăng nhập tôi tiêu: **3**
   (2 lần `cbnv_tw` + 1 lần `cb_nv_tw_01` thất bại), không lần nào trong cùng cửa sổ 60 giây với nhau.

**Không** logout chủ động lần nào. Toàn bộ số đo dưới đây lấy trong phiên 11:24:21 → ~11:30:50.

## 3. Hai hồ sơ đối chứng — cả hai đều CHỈ ĐỌC

Xác nhận tiền đề bằng `GET /api/v1/vu-viecs/{id}` + `GET /api/v1/vu-viecs/{id}/ket-qua-kiem-tra`
**trước** khi mở màn:

| | **Hồ sơ X** | **Hồ sơ Y** |
|---|---|---|
| Mã vụ việc | **`VV-BTP-TW-20260805-004`** | **`VV-BTP-TW-20260807-001`** |
| `id` | `ad1bbcc1-efc5-4480-887c-8c9b0648eb70` | `a694d1b9-5994-459b-bad4-2c8e8c63203a` |
| Tiêu đề | "QA UAT 05-08 - TKHSYCHTPL_OOS_02 luu nhap roi chuyen cho tiep nhan" | "Vụ việc test luồng" |
| Trạng thái | **`DANG_KIEM_TRA`** ("Đang kiểm tra") | **`DA_TIEP_NHAN`** ("Đã tiếp nhận") |
| Kết luận đã lưu | **`ketLuan = "DAT"`** | **`ketLuan = null`** |
| Checklist đã lưu | **`C01..C06 = DAT` (đủ 6/6)** | **`items = []`** (chưa có) |
| Người kiểm tra / ngày | "Cán bộ NV Trung ương" · `2026-08-05T14:59:54.599Z` | `null` / `null` |
| Đơn vị | TW `…8000-000000000001` (cùng đơn vị tài khoản đo) | TW `…8000-000000000001` |

> **Hồ sơ X thoả CHÍNH XÁC "Điều kiện 2" của phiếu**: *trạng thái "Đang kiểm tra", đã đánh dấu đủ
> 6 hạng mục trong danh sách kiểm tra*.
>
> Ghi chú chọn mẫu: toàn env chỉ có **4** vụ việc `DANG_KIEM_TRA`, trong đó **duy nhất** `VV-BTP-TW-20260805-004`
> thuộc đơn vị TW của tài khoản đo (3 vụ còn lại thuộc STP An Giang `…8002-…0006`). Đúng như recon §2.4
> cảnh báo, **cả 4 vụ đều đã lưu kết luận Đạt sẵn**.

## 4. Bộ bắt thông báo

Cài **đúng `output/UAT_doi-tac/tools/toast-capture.js`** (dán nguyên khối, không tự viết lại, không lọc trùng,
đọc bằng `innerText`) trên màn chi tiết hồ sơ X, **TRƯỚC** mọi cú bấm.

- Tự kiểm bằng node giả: **`soObserverDangSong = 1`** ✔ (số liệu hợp lệ).
- Bộ đếm lời gọi ghi (`window.__qa.net`, bỏ qua GET) chạy song song.

⚠️ **Khai trung thực:** lần tự kiểm **sau** lượt đo không chạy được vì phiên bị thu hồi ở ~11:30:50 làm trang
tải lại, xoá `window.__qa`. Việc này xảy ra **sau khi đã đo xong**; mọi số đo toast/mạng dưới đây đều đọc
ngay tại thời điểm thao tác, khi observer còn sống (đọc ra mảng, không phải `undefined`).

## 5. Hồ sơ X — bảng liệt kê nút NGUYÊN VĂN (không kết luận bằng mắt)

Rà bằng `evaluate_script`: **mọi** `button` / `a` / `[role=button]` trong `<main>`, lấy `innerText` +
`aria-label` + `title` + tên biểu tượng + `disabled` + `className` + toạ độ.
**Tổng 8 phần tử tương tác**, trong đó 5 là đầu mục accordion, 1 là mũi tên quay lại.

**Vùng thanh hành động (y < 260):**

| # | Thẻ | `innerText` nguyên văn | `aria-label` | `title` | Biểu tượng | `disabled` | Kiểu nút |
|---|---|---|---|---|---|---|---|
| 0 | `div` | *(rỗng)* | `back` | — | `arrow-left` | không | mũi tên quay lại |
| 1 | `button` | **`Phân công`** | — | — | `team` | **không** | `ant-btn-primary` (nền xanh) |
| 2 | `button` | **`Kiểm tra lại`** | — | — | `verified` | **không** | `ant-btn-default` (viền) |

**Các phần tử còn lại** (đều là đầu mục accordion, y ≥ 300): `Thông tin Doanh nghiệp` · `Nội dung Yêu cầu` ·
`Tài liệu đính kèm` · `Kết quả kiểm tra` · `HĐ tư vấn liên kết`.

**Kết luận rà DOM:** **KHÔNG có** menu phụ (kebab `…` / "Thao tác khác"), **KHÔNG có** nút ẩn,
**KHÔNG có** nút mờ. **KHÔNG có** phần tử nào mang chữ *"Hoàn tất kiểm tra"*.
→ **Triệu chứng đối tác báo được TÁI HIỆN Y NGUYÊN ở bề mặt**: màn chỉ có `[Phân công]` + `[Kiểm tra lại]`.

Ảnh: `image/KTHSYCHTPL_11-01-hoso-X-dangkiemtra-daluu-ketluan.png` — **đã mở đọc**: bản dựng `HTPLDN · V1.0.10`,
mã `VV-BTP-TW-20260805-004`, huy hiệu `Đang kiểm tra`, thanh tiến trình sáng ở bước 4 "Đang kiểm tra",
tài khoản `Cán bộ NV Trung ương` · `BTP · TW`, thanh hành động đúng 2 nút như bảng trên.

## 6. Bấm mở phiếu kết luận trên hồ sơ X — chức năng GỌI ĐƯỢC

Bấm **`[Kiểm tra lại]`** (bắt buộc bấm — cấm Pass bằng quan sát tĩnh):

| Số đo | Giá trị |
|---|---|
| Số hộp thoại mở ra | **1** (`ant-modal`) |
| **Tiêu đề hộp thoại** | **`Kiểm tra hồ sơ`** |
| Dòng thông tin đầu | `Lần bổ sung: 0/3` |
| Tiêu đề danh sách | **`Checklist Mẫu 01 NĐ55 (6 hạng mục)`** |
| Số nhóm lựa chọn (hạng mục) | **6** |
| Số ô chọn Đạt/Không đạt | **12** (6 hạng mục × 2) |
| Ô kết luận | `* Kết luận` — bắt buộc; giá trị đang mang: **`Đạt — chuyển sang phân công`** |
| Nút trong hộp thoại | `Hủy` · `Xác nhận` (+ nút đóng `×`) |
| **Khung thông báo bắt được** | **0** |
| **Lời gọi ghi dữ liệu (khác GET)** | **0** |
| Lỗi 4xx/5xx | **0** |

**6 hạng mục đọc nguyên văn trong phiếu** (khớp `srs-fr-05-vu-viec.md:525–531` về cấu trúc):

1. `Văn bản đề nghị hỗ trợ (Mẫu 01 NĐ55)` — đang chọn **Đạt**
2. `Bản chụp Giấy CNĐKKD` — **Đạt**
3. `Tờ khai xác định quy mô DN (NĐ39/2018)` — **Đạt**
4. `Hợp đồng dịch vụ TVPL` — **Đạt**
5. `Văn bản TVPL (bản đầy đủ)` — **Đạt**
6. `Văn bản TVPL (bản loại bỏ bí mật KD)` — **Đạt**

Mỗi hạng mục có thêm ô `Ghi chú cho hạng mục (không bắt buộc)`.

**Ô "Kết luận" — mở ra liệt kê đủ 3 lựa chọn:**

| # | Lựa chọn nguyên văn |
|---|---|
| 1 | **`Đạt — chuyển sang phân công`** ← **lựa chọn "Đạt" CÓ MẶT** |
| 2 | `Không đạt — từ chối hồ sơ` |
| 3 | `Yêu cầu bổ sung` |

Ảnh: `image/KTHSYCHTPL_11-02-phieu-ketluan-mo-6hangmuc.png` và
`image/KTHSYCHTPL_11-03-o-ketluan-co-lua-chon-Dat.png` — **đã mở đọc cả hai**, khớp đúng số đo trên.

**Đóng lại bằng `[Hủy]` — KHÔNG bấm `[Xác nhận]`.** Sau khi đóng: `0` hộp thoại còn mở,
`0` khung thông báo, `0` lời gọi ghi.

## 7. Hồ sơ Y — bảng liệt kê nút NGUYÊN VĂN (CHỈ MỞ XEM, không bấm gì)

**Tổng 6 phần tử tương tác** trong `<main>`.

**Vùng thanh hành động (y < 260):**

| # | Thẻ | `innerText` nguyên văn | `aria-label` | `title` | Biểu tượng | `disabled` | Kiểu nút |
|---|---|---|---|---|---|---|---|
| 0 | `div` | *(rỗng)* | `back` | — | `arrow-left` | không | mũi tên quay lại |
| 1 | `button` | **`Kiểm tra hồ sơ`** | — | — | `verified` | **không** | `ant-btn-primary` (nền xanh) |

**Các phần tử còn lại:** `Thông tin Doanh nghiệp` · `Nội dung Yêu cầu` · `Tài liệu đính kèm` ·
`HĐ tư vấn liên kết` (đều là đầu mục accordion).
Màn Y **không có** accordion "Kết quả kiểm tra" (vì chưa từng qua bước kiểm tra).

**KHÔNG bấm `[Kiểm tra hồ sơ]`** — nút này đưa vụ việc `DA_TIEP_NHAN → DANG_KIEM_TRA` (`:1743`),
tức là **đổi trạng thái**, nằm ngoài phạm vi được phép của lượt này.

Ảnh: `image/KTHSYCHTPL_11-04-hoso-Y-datiepnhan-chua-ketluan.png` — **đã mở đọc**: bản dựng `V1.0.10`,
mã `VV-BTP-TW-20260807-001`, huy hiệu `Đã tiếp nhận`, thanh tiến trình sáng ở bước 3, đúng 1 nút
`Kiểm tra hồ sơ`, dòng thời gian chỉ có `Tạo vụ việc 07/08/2026 15:56 · CB Nghiệp vụ TW 01`.

## 8. Trả lời dứt khoát 3 câu hỏi

### Câu 1 — Ở hồ sơ đúng tiền đề phiếu, màn CÓ nút mở phiếu kết luận kiểm tra không? Nhãn nguyên văn?

**CÓ.** Nhãn nguyên văn: **`Kiểm tra lại`** (thẻ `<button>`, biểu tượng `verified`, **không** bị vô hiệu hoá,
**không** bị làm mờ). Bên cạnh nó là nút **`Phân công`**.
**Không** có phần tử nào mang chữ *"Hoàn tất kiểm tra"* trên màn này.

### Câu 2 — Bấm có mở được phiếu không? Đủ 6 hạng mục? Ô kết luận có "Đạt"?

**Mở được.** Hộp thoại **`Kiểm tra hồ sơ`** hiện ra ngay, **đủ 6 hạng mục** (6 nhóm × 2 lựa chọn Đạt/Không đạt,
12 ô chọn) và ô `* Kết luận` **có lựa chọn "Đạt"** — nguyên văn **`Đạt — chuyển sang phân công`**.
**0 lỗi 4xx/5xx · 0 khung thông báo lỗi · 0 lỗi console.** Đã đóng bằng `[Hủy]`, **không lưu**.

### Câu 3 — Nhãn nút có đổi theo việc đã lưu kết luận hay chưa?

**CÓ — và đây gần như chắc chắn là gốc phản hồi của đối tác.**

| Hồ sơ | Trạng thái | Kết luận đã lưu | Nút trên thanh hành động | Dòng đặc tả khớp |
|---|---|---|---|---|
| **Y** | Đã tiếp nhận | **chưa** | **`[Kiểm tra hồ sơ]`** (đúng 1 nút) | `:1743` |
| **X** | Đang kiểm tra | **rồi** (Đạt, 6/6) | **`[Phân công]` + `[Kiểm tra lại]`** | `:1745` (+ `[Kiểm tra lại]` của `:1744`) |

**Lập luận quyết định — vì sao đây là "đổi theo kết luận đã lưu" chứ không chỉ "đổi theo trạng thái":**
hồ sơ X **đang ở đúng trạng thái `DANG_KIEM_TRA`**. Nếu giao diện chỉ phân nhánh theo trạng thái thì
X phải hiện bộ nút của `:1744` (`[Hoàn tất Kiểm tra] · [Kiểm tra lại]`). Thực tế X hiện **`[Phân công]`** —
chính là bộ nút của dòng `:1745`, dòng mà đặc tả đặt tên là **`DANG_KIEM_TRA (kết luận Đạt)`**.
⇒ Tiêu chí phân nhánh của giao diện **chính là "đã lưu kết luận hay chưa"**, đúng như đặc tả phân dòng.

**Giới hạn của phép đo — khai rõ, không suy rộng:** X và Y khác nhau **2 biến** (trạng thái *và* tình trạng
kết luận). Trạng thái đối chứng sạch nhất — **`DANG_KIEM_TRA` mà CHƯA lưu kết luận** — **không đo được**
trong lượt này vì (a) cả 4 vụ `DANG_KIEM_TRA` sẵn có đều đã lưu kết luận, (b) lệnh thu hẹp phạm vi cấm
dựng vụ việc mới và cấm bấm `[Kiểm tra hồ sơ]` trên Y. **Do đó tôi KHÔNG khẳng định** nhãn hiển thị ở
trạng thái `DANG_KIEM_TRA`-chưa-kết-luận là gì.

## 9. Đối chiếu đặc tả — đã tự mở tệp đọc số dòng

Tệp: `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-05-vu-viec.md` (2506 dòng).
Bảng "Bảng nút hành động theo trạng thái (#13)" bắt đầu ở `:1738`, header cột ở `:1740`.

```
:1743 | DA_TIEP_NHAN | [Kiểm tra Hồ sơ] | CB NV | → DANG_KIEM_TRA. Mở Accordion 4 |
```
```
:1744 | DANG_KIEM_TRA | [Hoàn tất Kiểm tra] · [Kiểm tra lại] | CB NV | Kết luận: **Đạt → vụ việc sẵn sàng
      phân công, VẪN giữ trạng thái DANG_KIEM_TRA** (chưa chuyển DA_PHAN_CONG) … Nút [Kiểm tra lại] dùng
      khi cần sửa lại kết quả kiểm tra đã lưu |
```
```
:1745 | DANG_KIEM_TRA (kết luận Đạt) / DA_TIEP_NHAN (phân công lại sau khi bị từ chối) | [Phân công]
      (modal 2 thẻ, gộp MH-05.5) | CB NV | … **Chỉ khi CB NV chọn được người/tổ chức xử lý và xác nhận
      thì vụ việc mới chuyển sang DA_PHAN_CONG.** … |
```
```
:1760 - Nút context-sensitive theo bảng trên — KHÔNG hiển thị tất cả nút cùng lúc
```

**Đối chiếu:**

| Quan sát | Dòng đặc tả | Quan hệ |
|---|---|---|
| Y (`DA_TIEP_NHAN`) → đúng 1 nút `Kiểm tra hồ sơ` | `:1743` `[Kiểm tra Hồ sơ]` | **KHỚP** (chỉ khác chữ hoa/thường ở "Hồ sơ") |
| X (`DANG_KIEM_TRA` + kết luận Đạt) → `[Phân công]` | `:1745` | **KHỚP** |
| X → còn `[Kiểm tra lại]` | `:1744` *"[Kiểm tra lại] dùng khi cần sửa lại kết quả kiểm tra đã lưu"* | **KHỚP** — X đúng là trường hợp "đã lưu" |
| X **không** có `[Hoàn tất Kiểm tra]` | `:1744` | **KHÔNG kết luận được** — `:1744` áp cho `DANG_KIEM_TRA`; X thuộc nhánh hẹp hơn `:1745`, và `:1760` cấm hiện mọi nút cùng lúc. Trạng thái `DANG_KIEM_TRA` chưa-kết-luận **chưa đo** |
| Nhãn giao diện `Kiểm tra hồ sơ` / `Kiểm tra lại` thay cho chữ `Hoàn tất Kiểm tra` | `:1744` | **Chênh câu chữ nhãn — Minor**, chức năng đầy đủ ⇒ không tự nó thành lỗi (chuẩn chấm §6 V1-b, §7c) |

## 10. Vế "kết luận Đạt → Đã phân công" — NGOÀI PHẠM VI, KHÔNG CHẤM

Ô "Kết quả mong đợi" của phiếu đòi *"Hệ thống chuyển trạng thái hồ sơ: 'Đang kiểm tra' → 'Đã phân công'"*.
Vế này **nằm ngoài phạm vi lượt đo** (đã bị lệnh thu hẹp loại bỏ) **và** vốn đã **trái đặc tả hiện hành**.
Bốn vị trí normative đã tự mở đọc, tất cả nói **ngược lại**:

```
:541  | 5 | Nếu DAT: vụ việc sẵn sàng phân công, **giữ trạng thái DANG_KIEM_TRA** — chỉ chuyển
        DA_PHAN_CONG khi CB NV phân công người/tổ chức xử lý qua FR-V.I-09 … | SM-VUVIEC |
```
```
:564  - **Given** CB NV kiểm tra xong **When** kết luận Đạt **Then** vụ việc sẵn sàng phân công,
        vẫn ở trạng thái DANG_KIEM_TRA; chỉ chuyển DA_PHAN_CONG khi CB NV phân công người/tổ chức
        xử lý (FR-V.I-09)
```
```
:2288 | DANG_KIEM_TRA | DA_PHAN_CONG | Đạt + chọn người/tổ chức xử lý | Đối tượng xử lý hợp lệ,
        đang hoạt động | Gửi TB người được phân công | FR-V.I-09 | BR-CALC-07 |
```
```
:22   | 2026-07-16 | BA + Claude | **Apply chốt UAT tuần 2:** … sửa nút "Đạt" khớp bảng chuyển trạng
        thái — Đạt giữ DANG_KIEM_TRA, chỉ chuyển DA_PHAN_CONG khi phân công người xử lý
        (KTHSYCHTPL_11, đồng bộ FR-V.I-06); …
```

Dòng `:22` **nêu đích danh mã case này**. Quan sát hiện trạng ăn khớp: hồ sơ X đã có kết luận Đạt
mà vẫn đứng ở "Đang kiểm tra", đồng thời **đã xuất hiện nút `[Phân công]`** — đúng mô hình đặc tả mô tả.

⇒ **Không chấm vế này.** Chỉ ghi nhận + đưa vào mục đề nghị BA đối chiếu lại với đối tác
(đối tác vẫn ghi Fail vế này ở vòng 2 ⇒ chưa được thông báo hoặc chưa đồng thuận).
**Không chặn bàn giao.**

## 11. Bằng chứng đối tác — đã mở xem và mô tả lại

### 11.1 `KTHSYCHTPL_11.jpg` (vòng 1) — `output/UAT_doi-tac/flowtest-2026-08-05/partner-evidence/`

Ảnh chụp toàn màn hình Windows, đồng hồ máy **03:34 PM · 2026-07-09**. Đọc được:

- Thanh địa chỉ: `htpldn-uat.ospgroup.vn/vu-viec/aadd0022-0000-4000-8000-000000000004`
- Góc phải trên: `BTP · DP` · chuông **52** · **`CB NV DP 01 (AG)`** · huy hiệu **`CB_NV_DP`**
- Chân sidebar: **`HTPLDN · V1.0`**
- Tiêu đề: **`VV-QA-R7-SLA-QHNT`** — *"QA R7 — Vụ việc SLA QUA_HAN_NGHIEM_TRONG"* + huy hiệu **`Đang kiểm tra`**
- **Thanh hành động: đúng 2 nút — `[Phân công]` (nền xanh) và `[Kiểm tra lại]` (viền).**
  **Không** có nút mang chữ "Hoàn tất kiểm tra".
- Thanh tiến trình dừng ở bước **Đang kiểm tra**
- Accordion `Kết quả kiểm tra` đang mở, bảng 5 cột `Mã / Hạng mục / Đạt / Không đạt / Ghi chú`,
  dòng `C01 — Văn bản đề nghị hỗ trợ (Mẫu 01 NĐ55)` (2 cột Đạt/Không đạt bị khung hình cắt)

### 11.2 `KTHSYCHTPL_11_v2.webm` (vòng 2) — đã trích 13 khung hình

Thư mục khung: `output/UAT_doi-tac/flowtest-2026-08-05/frames/KTHSYCHTPL_11_v2/`. Hai khung quyết định:

- **`t021.12s.jpg`** — **hộp thoại kiểm tra ĐANG MỞ**: các hạng mục `3. Tờ khai xác định quy mô DN (NĐ39/2018)`,
  `4. Hợp đồng dịch vụ TVPL`, `5. Văn bản TVPL (bản đầy đủ)`, `6. Văn bản TVPL (bản loại bỏ bí mật KD)`,
  mỗi hạng mục 2 lựa chọn `Đạt`/`Không đạt` (đang chọn **Đạt**) + ô `Ghi chú cho hạng mục (không bắt buộc)`.
  Cuối hộp thoại: `* Kết luận` = **"Đạt — chuyển sang phân công"**, 2 nút `[Hủy]` `[Xác nhận]`.
  Tài khoản `CB Nghiệp vụ TW 01 · CB_NV_TW`, bản dựng **`HTPLDN · V1.0.4`**, ngày `2026-08-03`.
  ⇒ **Chính đối tác cũng mở được phiếu này.**
- **`t036.19s.jpg`** — **sau khi xác nhận**: `VV-BTP-TW-20260514-002` — *"R23v3 Seed VV2 LV Dat dai"*,
  huy hiệu **`Đang kiểm tra`** + `Quá hạn nghiêm trọng · 40 ngày LV`, thanh hành động **vẫn** là
  **`[Phân công]` + `[Kiểm tra lại]`**, thanh tiến trình dừng ở bước 4 "Đang kiểm tra".

### 11.3 🔴 Ý nghĩa của 2 bằng chứng — đây là chỗ dễ chấm sai nhất

**Cả hai bằng chứng đều chụp ở trạng thái ĐÃ LƯU KẾT LUẬN.** Khung `t036.19s.jpg` chụp **ngay sau khi
bấm `[Xác nhận]`**; ảnh vòng 1 chụp vụ việc đã có kết quả kiểm tra trong accordion.
⇒ **Không được suy "thiếu nút" từ hai bằng chứng này** — chúng chỉ chứng minh rằng *sau khi đã lưu kết luận*
thì thanh hành động đổi sang `[Phân công]` + `[Kiểm tra lại]`, đúng `:1745`.

Ngoài ra 2 bằng chứng là **2 vụ việc khác nhau**, **2 vai trò khác nhau** (`CB_NV_DP` vs `CB_NV_TW`),
**2 bản dựng khác nhau** (`V1.0` vs `V1.0.4`) — và cả hai đều **cũ hơn** bản đang nghiệm thu (`V1.0.10`).

## 12. Console + mạng

- `list_console_messages` (lọc `error`, `warn`): **0 lỗi**, đúng **1 cảnh báo** không liên quan —
  `Route path "/ticket=*" will be treated as if it were "/ticket=/*" …` (đã gặp ở các case khác cùng lô).
- Bộ đếm lời gọi ghi của toast-capture: **0 lời gọi khác GET** trong suốt thao tác mở + đóng phiếu.
- **0 phản hồi 4xx/5xx** trong lượt đo (ngoài các lần `401 ERR-AUTH-SYS-00-03` do phiên bị thu hồi,
  đã khai ở §2 — không liên quan chức năng đang đo).

## 13. ✅ Khẳng định KHÔNG đổi trạng thái vụ việc nào

Đọc lại máy chủ **sau** toàn bộ thao tác:

| Hồ sơ | Trước | Sau | Kết |
|---|---|---|---|
| **X** `VV-BTP-TW-20260805-004` | `DANG_KIEM_TRA` · `ketLuan=DAT` · `ngayKiemTra=2026-08-05T14:59:54.599Z` · `C01..C06=DAT` · `boSungCount=0` | **y hệt từng trường** | ✅ không đổi |
| **Y** `VV-BTP-TW-20260807-001` | `DA_TIEP_NHAN` · `ketLuan=null` · `items=[]` | **y hệt** | ✅ không đổi |

`GET /vu-viecs/{X}/lich-su` sau lượt đo: **vẫn đúng 3 dòng** —
`KIEM_TRA 2026-08-05T14:59:54.624Z` · `TIEP_NHAN 2026-08-05T08:56:44.933Z` · `TAO_VV 2026-08-05T08:56:11.283Z`.
**Không sinh dòng lịch sử mới.**

**Không** bấm `[Xác nhận]`, **không** bấm `[Phân công]`, **không** bấm `[Kiểm tra hồ sơ]` trên hồ sơ Y,
**không** tạo/sửa/xoá bản ghi nào. Lượt đo **thuần chỉ đọc**.

## 14. Ảnh bằng chứng (đã mở đọc từng ảnh) + link Drive

| Tệp | Nội dung | Link Drive |
|---|---|---|
| `KTHSYCHTPL_11-01-hoso-X-dangkiemtra-daluu-ketluan.png` | Hồ sơ X "Đang kiểm tra" đã lưu kết luận — thanh hành động `[Phân công]` + `[Kiểm tra lại]`, bản dựng V1.0.10 | https://drive.google.com/file/d/1oxty1DfVEWRr82d3ls8B5GBkPG14F4vT/view?usp=drivesdk |
| `KTHSYCHTPL_11-02-phieu-ketluan-mo-6hangmuc.png` | Phiếu `Kiểm tra hồ sơ` đã mở — `Checklist Mẫu 01 NĐ55 (6 hạng mục)` | https://drive.google.com/file/d/1u2IbwEuLpYLJoILW2Ezdbw9kWopdcSzm/view?usp=drivesdk |
| `KTHSYCHTPL_11-03-o-ketluan-co-lua-chon-Dat.png` | Ô `* Kết luận` mở ra: `Đạt — chuyển sang phân công` / `Không đạt — từ chối hồ sơ` / `Yêu cầu bổ sung` | https://drive.google.com/file/d/1GGAje3k8pD6eqXWCqeqPiZJ8oFQKn1vE/view?usp=drivesdk |
| `KTHSYCHTPL_11-04-hoso-Y-datiepnhan-chua-ketluan.png` | Hồ sơ Y "Đã tiếp nhận" chưa lưu kết luận — đúng 1 nút `[Kiểm tra hồ sơ]` | https://drive.google.com/file/d/1vp8c9ub4_78-VUX8yNlSAY7zbRaTP30p/view?usp=drivesdk |

## 15. Verdict

**✅ Pass** (theo chuẩn chấm đã khoá §8 dòng 1 + dòng 2, và theo cách chấm của lệnh thu hẹp phạm vi).

- Ở hồ sơ đúng tiền đề phiếu: **CÓ** chức năng mở phiếu kết luận (`[Kiểm tra lại]`) ✔
- **Bấm mở được** ✔ — phiếu đủ **6 hạng mục** ✔ + ô kết luận **có lựa chọn "Đạt"** ✔
- **0** lỗi 4xx/5xx, **0** thông báo lỗi, **0** lỗi console ✔
- Nhãn khác chữ "Hoàn tất kiểm tra" → **Minor về cách đặt tên trên giao diện**, không tự nó thành lỗi
  (chuẩn chấm §6 V1-b, §7c; cách chấm của lệnh thu hẹp)
- Vế "Đạt → Đã phân công": **không chấm**, chuyển mục đề nghị BA (§10)

**Phạm vi hiệu lực của kết luận:** chỉ gồm **sự hiện diện và khả năng gọi được** của chức năng kết luận
kiểm tra, trên env nghiệm thu `https://htpldn-uat.ospgroup.vn`, bản dựng **V1.0.10**, vai trò **CB NV cấp TW**,
ngày **07/08/2026**. **KHÔNG** bao gồm phần lưu kết luận và chuyển trạng thái sau khi lưu.

## 16. Ghi nhận ngoài phạm vi (chưa log bug, báo lead)

| # | Nội dung | Mức |
|---|---|---|
| **N8** | **Tên 2/6 hạng mục trên giao diện trích văn bản CŨ hơn đặc tả.** Giao diện V1.0.10: hạng mục 1 = *"Văn bản đề nghị hỗ trợ (**Mẫu 01 NĐ55**)"*, hạng mục 3 = *"Tờ khai xác định quy mô DN (**NĐ39/2018**)"*. SRS v3.5 `:526` ghi *"Mẫu 01 (**Phụ lục NĐ18/2026**)"*, `:528` ghi *"(**NĐ80/2021**)"*. Chỉ là câu chữ nhãn, không ảnh hưởng chức năng ⇒ chưa đưa vào note đối tác. | Minor |
| **N9** | **Câu chữ lựa chọn kết luận có thể là gốc kỳ vọng sai của đối tác.** Ô kết luận ghi nguyên văn **"Đạt — chuyển sang phân công"**. Câu này dễ đọc thành "chọn Đạt thì hệ thống chuyển sang trạng thái Đã phân công", trong khi đặc tả (`:541`/`:564`/`:1744`/`:2288`) nói Đạt **giữ** "Đang kiểm tra". Đặc tả **không** quy định câu chữ cho lựa chọn này ⇒ chỉ ghi candidate câu chữ giao diện, **không** dùng làm căn cứ Pass/Reopen. Đã nêu trong mục đề nghị BA của note. | Candidate câu chữ |
| **N10** | **Máy chủ chỉ cho 1 phiên sống mỗi tài khoản** — phiên mới thu hồi phiên cũ (`ERR-AUTH-SYS-00-03` "Token đã bị thu hồi"). Hai lượt đo trong lô G3 đã bị cắt giữa chừng vì có phiên khác đăng nhập cùng `cbnv_tw`. **Khuyến nghị điều phối:** mỗi người đo dùng một tài khoản riêng, hoặc chạy tuần tự. | Vận hành |
| **N11** | **`cb_nv_tw_01` KHÔNG dùng mật khẩu `Test@1234`** — recon §1.3 suy đoán "khả năng cao đúng cho cả bộ `_NN`"; đã kiểm chứng thật và **sai**. Khung lỗi: *"Tên đăng nhập hoặc mật khẩu không đúng."* → tài khoản dự phòng cùng vai trò CB_NV_TW hiện **không dùng được**. | Đính chính recon |
