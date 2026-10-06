# GIAI ĐOẠN B — số đo thô · `QLHSPLDN_06` (tab `bug`, dòng 291 — "Xem")

```
Lô:            F9 — tái xác nhận trên env NGHIỆM THU của đối tác
Flow:          flows/03-reverify-sau-dev-fix.md — NHÁNH 2 "Tái xác nhận trên môi trường khác"
Nguồn chuẩn:   chuan/QLHSPLDN_06.md (Giai đoạn A đã khoá) — làm đúng theo, không tự thêm/bớt vế
Env đo:        https://htpldn-uat.ospgroup.vn  (env nghiệm thu của đối tác)
Người đo:      agent ĐO · 2026-08-07 · phiên 13:08 → 13:22 giờ VN
```

---

## 1. Vân tay bản dựng — ĐẦU và CUỐI phiên

| Hạng mục | ĐẦU phiên — **13:08:14 VN 07/08** | CUỐI phiên — **13:22:07 VN 07/08** |
|---|---|---|
| Bó mã JS | `assets/index-D4NhKEjr.js` | `assets/index-D4NhKEjr.js` |
| Bó mã CSS | `assets/index-DVlgOkLg.css` | `assets/index-DVlgOkLg.css` |
| `GET /` `last-modified` | `Fri, 07 Aug 2026 04:17:55 GMT` (= 11:17 VN) | `Fri, 07 Aug 2026 04:17:55 GMT` |
| `GET /` `etag` | `"6a755c73-428"` | `"6a755c73-428"` |
| Máy chủ web | `nginx` | `nginx` |
| Chuỗi chân sidebar | `HTPLDN · V1.0.10` | `HTPLDN · V1.0.10` |

> ✅ **Hai đầu TRÙNG KHỚP tuyệt đối** ⇒ không có deploy chen giữa phiên ⇒ **mọi quan sát dưới đây đều thuộc cùng
> một bản dựng**, không phải khai chia trước/sau mốc deploy.
>
> ⚠️ Bó mã đo được **khác** bản dựng env nội bộ nơi case từng Pass (`index-DIABnbIr.js`) ⇒ đúng như §0 nguồn chuẩn
> yêu cầu, **mọi vế đã được đo lại từ đầu**, không vế nào miễn.
>
> Trang đã được **tải lại thật, bỏ đệm** (`reload ignoreCache`) trước lô đo — tránh ca tab mở lâu chạy mã cũ.

---

## 2. Tài khoản thực dùng + xác nhận vai trò

| Hạng mục | Giá trị |
|---|---|
| Tài khoản | **`cbnv_tw`** (đúng tài khoản chỉ định, **không** phải fallback) |
| Cách đăng nhập | UI thật: mật khẩu → mã xác thực 6 số lấy ở MailHog của chính env (`/mailhog/api/v2/messages`) |
| Số lượt đăng nhập | **1 lượt duy nhất**, không chạm giới hạn 5 lượt/60s |
| Nguồn xác nhận vai trò | `GET /api/v1/auth/me` → **200** |
| `hoTen` | `Cán bộ NV Trung ương` |
| `vaiTro` | `["CB_NV_TW"]` |
| `capDonVi` | `TW` |
| `donViId` | `00000000-0000-4000-8000-000000000001` (= *Cục Bổ trợ tư pháp - Bộ Tư pháp*) |
| Badge trên màn | `Cán bộ NV Trung ương · Cán bộ Nghiệp vụ Trung ương` · phạm vi `BTP · TW` |

⇒ Khớp đúng vai trò/cấp đọc được trên bằng chứng của đối tác. **Không dùng `admin` ở bất kỳ bước nào.**

---

## 3. Bản ghi đã tạo / đã đổi trên env đối tác

Tất cả trên `https://htpldn-uat.ospgroup.vn`, do `cbnv_tw` tạo, **bằng UI thật** (nút *Thêm hồ sơ* → `Đồng ý`).

**Doanh nghiệp QA đã chọn (KHÔNG tạo mới — dùng DN QA sẵn có, đúng T1):**

| Mã DN | id trên URL | Vì sao chọn |
|---|---|---|
| `DN-HCM-0004` — *QA Doi chung 0311224488* | `ac4a3173-3e2c-4f2a-b63d-cd44dd757fc6` | DN mang dấu QA, trong phạm vi TW, **khác `DN-XX-0005`**, không xuất hiện trong bằng chứng đối tác, thẻ Hồ sơ pháp lý **trống hoàn toàn** trước khi seed ("Chưa có hồ sơ pháp lý") ⇒ nền sạch |

**3 hồ sơ pháp lý QA đã TẠO MỚI:**

| Mã hồ sơ | id | Giờ tạo (VN) | Nội dung | Dạng phủ |
|---|---|---|---|---|
| `HSPL-20260807-0001` | `3d78710b-3639-49a4-b2b8-9eb18ca9c829` | 13:12 | `QA-W5-0807-HS-A co tep` · Giấy phép · Thương mại · 01/08/2026 → 31/12/2026 · CQ cấp `QA-W5-0807 coquan` · Mô tả `QA-W5-0807 mo ta A` · **Hiệu lực** · **1 tệp** `QA-W5-0807-tep-06A.png` | **D1** + D3-Hiệu lực |
| `HSPL-20260807-0002` | `73c15559-007a-447d-9685-4c4b1e2ca2c6` | 13:13 | `QA-W5-0807-HS-B khong tep` · Khác · **Thu hồi** · **0 tệp** · **5 trường tuỳ chọn để TRỐNG** (lĩnh vực, ngày cấp, ngày hết hạn, cơ quan cấp, mô tả) | **D2** + D3-Thu hồi + **D4** |
| `HSPL-20260807-0003` | `728293b4-ff53-45d7-997a-d702979770ef` | 13:15 | `QA-W5-0807-HS-C het han` · Quyết định · 01/03/2026 → 01/07/2026 · **Hết hạn** · **1 tệp** `QA-W5-0807-tep-06C.png` | D1 + D3-Hết hạn |

Tệp seed: `F9-uatdoitac-QLHSPLDN-2026-08-07/seed-files/QA-W5-0807-tep-06A.png` (88 B) · `…-06C.png` (99 B).

**Bản ghi của ĐỐI TÁC — chỉ ĐỌC, không đổi gì:**

| Bản ghi | Thao tác đã làm | Thao tác KHÔNG làm |
|---|---|---|
| `DN-XX-0005` (`1a715c55-…3ce5`) | mở chi tiết, mở thẻ Hồ sơ pháp lý, đếm hàng/nút | ❌ không sửa, không xoá, **không thêm hồ sơ nào vào DN này** |
| `HSPL-20260803-0001` | bấm **Xem** (thao tác đọc) | ❌ không bấm Sửa/Xoá, không bấm lưu |
| `HSPL-20260731-0002` | bấm **Xem** (thao tác đọc) | ❌ không bấm Sửa/Xoá, không bấm lưu |

> Tổng cộng: **3 bản ghi mới**, **0 bản ghi bị sửa/xoá**. Không đụng module khác.

**Đường UI đã đi (đúng 4 bước của phiếu, KHÔNG gõ thẳng URL):**
menu trái *Doanh nghiệp* → nút mở chi tiết trên hàng DN → thẻ *Hồ sơ pháp lý* → nút **Xem** trên hàng hồ sơ.

---

## 4. Số đo thô từng nhóm A → E

### Nhóm A — có điều khiển mở chi tiết trên MỌI hàng không? *(vế a · C1)*

Đếm **thô**, không `unique`, không lọc, không lấy mẫu. Đo trên **cả hai** bảng.

| Bảng | Số hàng **N** | Cách đếm 1 — nút có nghĩa "Xem" **trong ô Hành động của chính từng hàng** | Cách đếm 2 (độc lập) — quét **toàn bộ** `tbody`, bắt phần tử có nhãn/`aria-label`/`title` nghĩa "Xem", đọc bằng `innerText` | Khớp? |
|---|---|---|---|---|
| DN QA `DN-HCM-0004` | **3** | **3** | **3** | ✅ |
| **DN đối tác `DN-XX-0005`** | **4** | **4** | **4** | ✅ |
| **Tổng** | **7** | **7** | **7** | ✅ |

Mỗi hàng đều có **đúng 1** điều khiển mở chi tiết — **không hàng nào thiếu**. Ô Hành động của cả 7/7 hàng đọc ra
`Xem | Sửa | Xoá`.

Kiểm từng điều khiển có **dùng được thật** (7/7 hàng):

| Tiêu chí | Kết quả trên **cả 7/7** nút |
|---|---|
| `disabled` | `false` |
| `aria-disabled="true"` | không có (`null`) |
| `pointer-events` | `auto` |
| `opacity` | `1` |
| `visibility` / `display` | `visible` / `inline-flex` |
| Kích thước khung | **68 × 24 px** (> 0×0) |
| Trong khung nhìn / cuộn tới được | có |
| Phần tử tại tâm nút chính là nó (không bị che) | đúng |

Chi tiết 4 hàng của **bảng đối tác** (chính bảng họ báo lỗi):

| Mã hồ sơ | Trạng thái | Có tệp | Ô Hành động |
|---|---|---|---|
| `HSPL-20260804-0001` | Hết hạn | Có | `Xem \| Sửa \| Xoá` |
| `HSPL-20260803-0002` | Hiệu lực | Không | `Xem \| Sửa \| Xoá` |
| `HSPL-20260803-0001` | Hiệu lực | Có | `Xem \| Sửa \| Xoá` |
| `HSPL-20260731-0002` | Hiệu lực | Có | `Xem \| Sửa \| Xoá` |

⇒ **Nhóm A ①②③ ĐẠT.**

---

### Nhóm B — bấm thật có mở được cửa sổ chi tiết không? *(vế b · C2)*

Bấm bằng **chuột thật qua UI** (công cụ điều khiển chuột, **không** `dispatchEvent`, **không** gọi hàm JS).
**5 lần bấm** trên 5 hồ sơ, phủ đủ D1–D4:

| # | Hồ sơ | Dạng phủ | Cửa sổ mở? | Tiêu đề đọc bằng `innerText` | Ảnh đã chụp **và mở ra đọc bằng mắt** |
|---|---|---|---|---|---|
| 1 | `HSPL-20260807-0001` (QA) | **D1** · Hiệu lực · đủ trường | ✅ | `Chi tiết hồ sơ pháp lý` | ✅ |
| 2 | `HSPL-20260807-0002` (QA) | **D2** · Thu hồi · **D4** 5 trường trống | ✅ | `Chi tiết hồ sơ pháp lý` | ✅ |
| 3 | `HSPL-20260807-0003` (QA) | **D3-Hết hạn** · có tệp | ✅ | `Chi tiết hồ sơ pháp lý` | ✅ |
| 4 | `HSPL-20260803-0001` (**đối tác**) | D1 · Hiệu lực | ✅ | `Chi tiết hồ sơ pháp lý` | ✅ |
| 5 | `HSPL-20260731-0002` (**đối tác**) | D1 · **D4** (ngày hết hạn trống) | ✅ | `Chi tiết hồ sơ pháp lý` | ✅ |

- **5/5 lần** hiện lớp nổi chi tiết ngay trên màn đang đứng — **không** lần nào trắng màn, **không** lần nào điều
  hướng sang màn khác, **không** lần nào văng lỗi bảng điều khiển.
- Lời gọi máy chủ kèm theo: `GET /api/v1/ho-so-phap-ly-dns/{id}` → **200** (đo ở 5/5 lần bấm; đường gọi lấy từ
  **chính request UI phát ra**, không đoán).
- Bộ bắt thông báo (`MutationObserver` trên `document.body`, cài **trước** khi bấm, đọc `innerText`, **không**
  dedupe): **0 thông báo lỗi** trong cả 5 lần.
- Bảng điều khiển: **0 lỗi** (`list_console_messages` type=error → rỗng).
- Đóng cửa sổ được bình thường; bảng phía sau **giữ nguyên dữ liệu**, không mất hàng.

⇒ **Nhóm B ④⑤ ĐẠT.**

---

### Nhóm C — nội dung cửa sổ có khớp bản ghi không? *(vế b · C3)*

**Nguồn độc lập** = đọc lại bản ghi qua phản hồi máy chủ trong cùng phiên, dùng **đúng đường request UI phát ra**
(`GET /api/v1/ho-so-phap-ly-dns/{id}` và `GET /api/v1/ho-so-phap-ly-dns?doanhNghiepId=…&pageSize=100`).
**Không** dùng cách bấm lại cùng nút.

**Hồ sơ 1 — `HSPL-20260807-0001` (D1, đủ trường):**

| Trường | Cửa sổ hiển thị | Máy chủ trả về | Khớp |
|---|---|---|---|
| Mã hồ sơ | `HSPL-20260807-0001` | `maHoSo: "HSPL-20260807-0001"` | ✅ |
| Tên hồ sơ | `QA-W5-0807-HS-A co tep` | `tenHoSo` cùng chuỗi | ✅ |
| Loại hồ sơ | `Giấy phép` | `loaiHoSo: "GIAY_PHEP"` | ✅ (đã dịch nhãn) |
| Lĩnh vực pháp lý | `Thương mại` | `linhVuc.ten: "Thương mại"` | ✅ |
| Nguồn | `Thủ công` | `nguon: "THU_CONG"` | ✅ (đã dịch nhãn) |
| Cơ quan cấp | `QA-W5-0807 coquan` | `coQuanCap` cùng chuỗi | ✅ |
| Ngày cấp | `01/08/2026` | `ngayCap: "2026-08-01"` | ✅ đúng `dd/mm/yyyy` |
| Ngày hết hạn | `31/12/2026` | `ngayHetHan: "2026-12-31"` | ✅ đúng `dd/mm/yyyy` |
| Trạng thái | `Hiệu lực` | `trangThai: "HIEU_LUC"` | ✅ (đã dịch nhãn) |
| Mô tả | `QA-W5-0807 mo ta A` | `ghiChu` cùng chuỗi | ✅ |

**10/10 trường khớp.**

**Hồ sơ 2 — `HSPL-20260807-0002` (D2 + D4, 5 trường trống):**

| Trường | Cửa sổ | Máy chủ | Khớp |
|---|---|---|---|
| Mã / Tên | `HSPL-20260807-0002` / `QA-W5-0807-HS-B khong tep` | cùng chuỗi | ✅ |
| Loại hồ sơ | `Khác` | `loaiHoSo: "KHAC"` | ✅ |
| Lĩnh vực pháp lý | **`—`** | `linhVucId: null` | ✅ |
| Nguồn | `Thủ công` | `THU_CONG` | ✅ |
| Cơ quan cấp | **`—`** | `coQuanCap: null` | ✅ |
| Ngày cấp | **`—`** | `ngayCap: null` | ✅ |
| Ngày hết hạn | **`—`** | `ngayHetHan: null` | ✅ |
| Trạng thái | `Thu hồi` | `trangThai: "THU_HOI"` | ✅ |
| Mô tả | **`—`** | `ghiChu: null` | ✅ |

**5/5 trường bỏ trống hiện ký hiệu rỗng `—` có nhãn đầy đủ**, không ô nào mất nhãn.

**Hồ sơ 3 — `HSPL-20260807-0003` (D3-Hết hạn):** mã/tên/`Quyết định`/`—`/`Thủ công`/`—`/`01/03/2026`/`01/07/2026`/
`Hết hạn`/`—` — **khớp 10/10** với `QUYET_DINH` · `linhVucId:null` · `2026-03-01` · `2026-07-01` · `HET_HAN` · `ghiChu:null`.

**Hồ sơ 4 — `HSPL-20260803-0001` (đối tác):** `Khác`/`Thuế`/`Thủ công`/`TKM`/`03/08/2026`/`03/08/2026`/`Hiệu lực`/
`tkm kiểm thử chức năng` — **khớp 10/10** với `KHAC` · `linhVuc.ten:"Thuế"` · `coQuanCap:"TKM"` · `2026-08-03` ×2 ·
`HIEU_LUC` · `ghiChu` cùng chuỗi.

**Hồ sơ 5 — `HSPL-20260731-0002` (đối tác):** `Giấy chứng nhận`/`Đất đai`/`Thủ công`/`—`/`01/07/2026`/**`—`**/
`Hiệu lực`/`—` — **khớp 10/10** với `GIAY_CN` · `Đất đai` · `coQuanCap:null` · `2026-07-01` · `ngayHetHan:null` ·
`HIEU_LUC` · `ghiChu:null`.

**Quét chuỗi hỏng trên toàn bộ 5 cửa sổ:** `null` = **0** · `undefined` = **0** · `[object Object]` = **0** ·
ô rỗng mất nhãn = **0** · mã enum thô lọt ra màn (`HIEU_LUC`, `GIAY_CN`, `THU_CONG`…) = **0**.

⇒ **Nhóm C ⑥⑦ ĐẠT.**

---

### Nhóm D — danh sách tệp đính kèm *(vế c · C4)*

Đếm tệp bằng `.ant-upload-list-item-container` (đúng bẫy dụng cụ §7), số tệp thực đọc từ `fileDinhKem[]` trong
phản hồi máy chủ.

| Hồ sơ | Dạng | Cửa sổ hiện | Tên tệp đọc được trên cửa sổ | Số tệp **hiển thị** | Số tệp **thực** (máy chủ) | Khớp |
|---|---|---|---|---|---|---|
| `HSPL-20260807-0001` | **D1** | mục *Tệp đính kèm* + dòng tệp + nút *Xem*/*Tải* | `QA-W5-0807-tep-06A.png` **(88 B)** | **1** | **1** — `tenFile` khớp, `dungLuong: 88` | ✅ |
| `HSPL-20260807-0003` | D1 | như trên | `QA-W5-0807-tep-06C.png` **(99 B)** | **1** | **1** — `dungLuong: 99` | ✅ |
| `HSPL-20260803-0001` (đối tác) | D1 | như trên | `2K15 T3 (4.8) & CN (9.8).pdf` **(258.2 KB)** | **1** | **1** — `dungLuong: 264361` B = 258.2 KB | ✅ |
| `HSPL-20260731-0002` (đối tác) | D1 | như trên | `hspl-cu-them-tep-v2.png` **(70 B)** | **1** | **1** — `dungLuong: 70` | ✅ |
| `HSPL-20260807-0002` | **D2** | mục *Tệp đính kèm* + **biểu tượng rỗng + chữ "Chưa có tệp đính kèm"** | — | **0** | **0** — `coFile: false` | ✅ |

**D2 — hồ sơ KHÔNG tệp:** cửa sổ **vẫn mở bình thường**, có **trạng thái rỗng đọc được** (`Chưa có tệp đính kèm`),
**không** trắng, **không** lỗi bảng điều khiển, **không** vỡ bố cục.

⇒ **Nhóm D ⑧⑨ ĐẠT.**

---

### Nhóm E — cửa sổ "Xem" có phải là biểu mẫu Chỉnh sửa không? *(vế d1 · C5)*

Đếm **thô** trong phạm vi cửa sổ: `input` · `textarea` · `select` · `.ant-select` · `.ant-picker` ·
`[contenteditable="true"]`. Liệt kê **toàn bộ** nút.

| Hồ sơ | Số ô nhập | Số nút | Danh sách nút đầy đủ | Có nút lưu/gửi? |
|---|---|---|---|---|
| `HSPL-20260807-0001` (D1) | **0** | 4 | `[×] (aria-label "Close")` · `Xem` · `Tải` · `Đóng` | **KHÔNG** |
| `HSPL-20260807-0002` (D2/D4) | **0** | 2 | `[×] (aria-label "Close")` · `Đóng` | **KHÔNG** |
| `HSPL-20260807-0003` (D3-Hết hạn) | **0** | 4 | `[×]` · `Xem` · `Tải` · `Đóng` | **KHÔNG** |
| `HSPL-20260803-0001` (đối tác) | **0** | 4 | `[×]` · `Xem` · `Tải` · `Đóng` | **KHÔNG** |
| `HSPL-20260731-0002` (đối tác) | **0** | 4 | `[×]` · `Xem` · `Tải` · `Đóng` | **KHÔNG** |

- Nút `Xem` / `Tải` trong cửa sổ là thao tác **đọc tệp**, không phải ghi dữ liệu hồ sơ.
- Đối chiếu trực tiếp: biểu mẫu **Thêm/Sửa** trên chính thẻ này có **9 ô nhập** + nút **`Đồng ý`**; cửa sổ **Xem**
  có **0 ô nhập** + **0 nút `Đồng ý`** ⇒ **hai màn hoàn toàn khác nhau**, không phải cùng một biểu mẫu.
- Cửa sổ Xem cũng có **tiêu đề riêng** `Chi tiết hồ sơ pháp lý` (biểu mẫu thêm là `Thêm hồ sơ pháp lý`).

⇒ **Nhóm E ⑩ ĐẠT** — cửa sổ Xem **không phải** biểu mẫu chỉnh sửa lưu được.

---

### Vế `d2` / C6 — chế độ chỉ đọc *(GAP có điều kiện)*

Dùng **chính số đo của Nhóm E**, **không** mở thêm vòng UI nào.

Số đo: **0 ô nhập** + **0 nút lưu/gửi** trên **cả 5/5** cửa sổ đã mở.

⇒ Rơi đúng vào **hàng 1** của bảng §1.1 nguồn chuẩn: hiện trạng **thoả đúng ô *Kết quả mong đợi*** của đối tác
("ở chế độ chỉ đọc") ⇒ **không tồn tại bất đồng nào để BA chốt** ⇒ `d2` **KHÔNG** kéo case sang Cần BA,
**KHÔNG** kích hoạt câu hỏi BA ở §8.

🔴 **Ghi rõ theo yêu cầu của nguồn chuẩn:** kết luận này **chỉ có hiệu lực với expected gốc của phiếu**.
**SRS v3.5 vẫn IM LẶNG** về chế độ chỉ đọc của cửa sổ Xem trên màn cán bộ (`SCR-V.III-02`) — dòng "Read-only" duy
nhất (`srs-fr-07-doanh-nghiep.md:523`) thuộc `SCR-V.III-04`, màn của **vai trò Doanh nghiệp** (`:508`, `:514`
*"Vai trò khác KHÔNG truy cập trang này"*). **Không được viết như thể SRS quy định read-only.**

**Câu hỏi BA §8 câu 2 cũng KHÔNG phát sinh:** thẻ *Hồ sơ pháp lý* trên env đối tác **CÓ đủ** ô tìm kiếm
(*Tìm theo mã hoặc tên hồ sơ*), 4 bộ lọc (*Loại hồ sơ*, *Trạng thái*, *Từ ngày*, *Đến ngày*) và nút **Xuất Excel**
⇒ không còn điểm lệch giữa `srs-fr-12:589-597` / `:657-665` và `srs-fr-07:468` để hỏi.

---

### Biến thể bắt buộc — M = 4, đã chạy đủ 4/4

| Dạng | Bắt buộc | Đã đo trên | Kết quả |
|---|---|---|---|
| **D1** — có ≥1 tệp | ✅ | `0001`, `0003` (QA) + `20260803-0001`, `20260731-0002` (đối tác) | ĐẠT |
| **D2** — không tệp | ✅ | `0002` (QA) | ĐẠT |
| **D3** — đủ 3 trạng thái | ✅ | Hiệu lực `0001` · Thu hồi `0002` · **Hết hạn** `0003` | ĐẠT 3/3 |
| **D4** — trường tuỳ chọn trống | ✅ | `0002` (5 trường trống) + `20260731-0002` của đối tác (ngày hết hạn trống — đúng ca trên ảnh của họ) | ĐẠT |

**Dạng được MIỄN (khai đúng nguồn chuẩn §5):** hồ sơ `nguon = CONG_PLQG` — phải đến từ API inbound của Cổng PLQG,
QA không tạo được bằng UI. Miễn hợp lệ vì **7/7 hàng đo được trên cả hai bảng đều là `Thủ công`**, đúng như dữ liệu
của đối tác ⇒ không lệch điều kiện đo. **Không** tính thành GAP.

---

## 5. Artifact quyết định verdict

Tất cả nằm ở `F9-uatdoitac-QLHSPLDN-2026-08-07/image/`. Mỗi ảnh **đã được mở ra đọc bằng mắt**, không kết luận
bằng script chạy trong trang.

| Ảnh | Thấy gì trong ảnh |
|---|---|
| `06-A-bang-HSPL-cua-DN-XX-0005-4hang-deu-co-nut-Xem.png` | **Chính bảng đối tác báo lỗi.** Thẻ *Hồ sơ pháp lý DN* của `DN-XX-0005`, 4 hàng `HSPL-20260804-0001` / `-20260803-0002` / `-20260803-0001` / `-20260731-0002`; cột **Hành động** của **cả 4 hàng** đều có cụm **👁 Xem · Sửa · Xoá** — nút *Xem* hiện rõ, không mờ, không khuyết hàng nào. Ảnh cũng cho thấy thẻ có ô tìm kiếm + 4 bộ lọc + nút *Xuất Excel*. |
| `06-B-cuaso-chitiet-D1-HSPL-20260807-0001-co-tep-hieuluc.png` | Cửa sổ **Chi tiết hồ sơ pháp lý** mở đè lên bảng, đọc rõ 10 trường: `HSPL-20260807-0001` · `QA-W5-0807-HS-A co tep` · Giấy phép · Thương mại · Thủ công · `QA-W5-0807 coquan` · `01/08/2026` · `31/12/2026` · nhãn trạng thái xanh **Hiệu lực** · mô tả. Mục **Tệp đính kèm** liệt kê `QA-W5-0807-tep-06A.png (88 B)` kèm nút *Xem*/*Tải*. Chỉ có nút **Đóng** — **không có ô nhập, không có nút lưu**. |
| `06-B-cuaso-chitiet-D2D4-HSPL-20260807-0002-khong-tep-thuhoi-5truong-trong.png` | Cửa sổ mở bình thường cho hồ sơ **không tệp**: 5 trường tuỳ chọn đều hiện ký hiệu **`—`** kèm nhãn đầy đủ; nhãn trạng thái đỏ **Thu hồi**; mục *Tệp đính kèm* hiện **biểu tượng hộp rỗng + chữ "Chưa có tệp đính kèm"**. Cửa sổ không trắng, không vỡ, chỉ có nút **Đóng**. |
| `06-B-cuaso-chitiet-D3-hethan-HSPL-20260807-0003-co-tep.png` | Biến thể trạng thái **Hết hạn** (nhãn cam) mở được đầy đủ; `01/03/2026` → `01/07/2026`; tệp `QA-W5-0807-tep-06C.png (99 B)` liệt kê đúng tên. **0 ô nhập, 0 nút lưu.** |
| `06-B-cuaso-chitiet-banghi-doitac-HSPL-20260803-0001.png` | **Bằng chứng mạnh nhất — đúng bản ghi của đối tác.** Cửa sổ chi tiết `HSPL-20260803-0001` *TKM hồ sơ pháp lý số 1*: Khác · Thuế · Thủ công · `TKM` · `03/08/2026` ×2 · **Hiệu lực** · `tkm kiểm thử chức năng`; tệp `2K15 T3 (4.8) & CN (9.8).pdf (258.2 KB)`. Chỉ **Đóng**, **không** ô nhập, **không** nút lưu. |

---

## 6. Verdict

# 📌 **Pass** — HIỆN TẠI ĐẠT

**Bám luật Flow 03 §Chốt (bảng Verdict logic), dòng "Pass":**

1. **Mọi vế đều `MATCH` và đều đạt.** Bốn vế `MATCH` của nguồn chuẩn — (a) có điều khiển mở chi tiết · (b) bấm mở
   được cửa sổ đủ thông tin · (c) có danh sách tệp · (d1) là thao tác riêng không phải biểu mẫu Sửa — **đều đo
   được và đều đạt**. Không vế nào FAIL.
2. **Đã chạy HẾT phạm vi/biến thể bắt buộc.** Đủ **4/4** dạng D1–D4; đủ **3/3** trạng thái; đo trên **cả hai**
   bảng (DN QA **và** `DN-XX-0005` của đối tác); đếm **thô toàn bộ 7/7 hàng**, không lấy mẫu.
3. **Đủ 5 nhóm điều kiện PASS A→E** của nguồn chuẩn §4 — ①②③④⑤⑥⑦⑧⑨⑩ đều đạt, số đo cụ thể ở §4 trên.
4. **Có đối chứng độc lập cho mọi quan sát quyết định.** Từng trường của **5/5** cửa sổ được đối chiếu với phản
   hồi máy chủ đọc lại qua **đúng đường request UI phát ra**; số tệp đối chiếu với `fileDinhKem[]` thực.
   **Không** dùng cách bấm lại cùng nút làm đối chứng.
5. **Không Pass bằng quan sát tĩnh.** Đã **bấm thật bằng chuột qua UI** 5 lần, mở được cửa sổ, đọc nội dung, đối
   chiếu từng trường; **đã chụp ảnh và mở ảnh đọc bằng mắt** cho từng biến thể.
6. **Vế `d2` không rơi vào ca lửng** (0 ô nhập + 0 nút lưu) ⇒ theo §1.1 hàng 1, không kéo case sang **Cần BA**.

**Giới hạn hiệu lực (bắt buộc ghi):** Pass này **chỉ có hiệu lực trên env `https://htpldn-uat.ospgroup.vn`**, bản
dựng `assets/index-D4NhKEjr.js` · `last-modified Fri, 07 Aug 2026 04:17:55 GMT`, đo lúc **13:08→13:22 giờ VN
07/08/2026**, với vai trò **`CB_NV_TW`**.

**Không viết "fix đã có tác dụng":** phiên này không có bằng chứng trạng thái trước fix trên chính env/bản dựng
này ⇒ chỉ kết luận **hiện trạng ĐẠT so với SRS + expected gốc**, dùng chữ *HIỆN TẠI ĐẠT*.

**Ghi ô Drive theo mapping §7 brief:** `Trạng thái dev fix` = **`UAT done`**.

---

## 7. Bug mới / candidate

Chỉ ghi nhận sai lệch **tự lộ trong chính luồng bắt buộc**, không exploratory, không bấm thử thêm, **không** dùng
thêm lượt xác nhận nào.

### Candidate 1 — nhãn nút thêm là "Thêm hồ sơ" thay vì "Thêm mới"

```
Nhãn nút thêm bản ghi trên thẻ Hồ sơ pháp lý là "Thêm hồ sơ" · xuất hiện tại bước dựng tiền đề T3/T4/T5
(bắt buộc phải bấm nút này để seed) · artifact: ảnh 06-A-bang-HSPL-cua-DN-XX-0005-…png (góc phải hiện nút
"Thêm hồ sơ") + snapshot cây a11y cả 2 bảng · SRS có căn cứ nhưng KHÁC VẾ của case này
```

- **Căn cứ SRS (đã mở file đọc, không quote từ trí nhớ):**
  `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-v3.5.md:6756` —
  *"| **H4** | Nhãn nút thống nhất | Nút thêm mới luôn đặt nhãn **\"Thêm mới\"** (không \"Tạo mới\", \"Tạo\",
  \"Thêm\", \"Mới\"…). … | BẮT BUỘC |"*, phạm vi áp dụng ở `:6749` — *"Áp dụng cho **mọi màn hình** trong hệ
  thống (… DN, …)"*.
- **Vì sao chỉ là candidate, KHÔNG kéo verdict:** nguồn chuẩn §6 xếp đúng mục này vào nhóm *"KHÔNG được chấm Fail
  vì… — ghi nhận / log candidate riêng"*; nó **không** phải vế đối tác nêu (họ nói thiếu hẳn chức năng Xem), và
  **không** làm điều kiện PASS nào của case không đạt.
- **Còn thiếu để xác nhận:** cần chốt phạm vi với BA/đối tác xem H4 có áp cho nút thêm **trong thẻ con** hay chỉ
  cho nút thêm ở màn danh sách chính — QA **không** mở thêm vòng UI để điều tra.

### Ghi nhận không thành candidate

- **Điều khiển mở chi tiết là icon con mắt **kèm** chữ "Xem"** (`button "eye Xem"`, khung 68×24). `srs-v3.5.md:6758`
  (H6) đòi *icon + `aria-label` + tooltip hover*, *"không icon-only"*. Hiện trạng **có icon con mắt đúng quy ước
  "Mắt = Xem"** và **có nhãn chữ** nên không rơi vào ca icon-only. QA **chưa đo** tooltip hover / `aria-label` —
  vì đó **ngoài vế** của case và đo thêm sẽ thành exploratory. Không đủ căn cứ để nêu thành candidate.
- **Trạng thái do người dùng tự chọn có thể lệch với ngày hết hạn** (vd hàng đối tác `HSPL-20260803-0002`
  hết hạn `21/08/2026` nhưng trạng thái *Hiệu lực*; `HSPL-20260804-0001` hết hạn `30/11/2026` nhưng *Hết hạn*).
  `srs-fr-12-tv-chuyen-sau.md:586` khai `trang_thai` nằm trong **bảng Inputs** (`HIEU_LUC / HET_HAN / THU_HOI`) —
  tức là trường **người dùng nhập**, không phải trường suy ra từ ngày ⇒ **đúng đặc tả**, không phải sai lệch.
- **Thông báo "Thêm hồ sơ thành công" bị bộ quan sát ghi 2 lần** ở mỗi lượt seed — đã kiểm lớp CSS: một bản ghi là
  hộp ngoài `.ant-message`, một bản ghi là `.ant-message-notice-wrapper` bên trong ⇒ **một thông báo duy nhất**,
  **không** phải double-toast. Không phải lỗi.

---

## 8. Phần chưa đo được

| Phần | Lý do | Có ảnh hưởng verdict? |
|---|---|---|
| Hồ sơ có `nguon = CONG_PLQG` | Phải đến từ API inbound của Cổng PLQG, QA **không tạo được bằng UI** | **Không** — nguồn chuẩn §5 khai đây là **dạng được MIỄN hợp lệ**; toàn bộ 7/7 hàng trên cả hai bảng đều là *Thủ công*, đúng bằng dữ liệu đối tác đang có |
| Tooltip hover / `aria-label` của nút mở chi tiết | Ngoài vế của case; đo thêm = exploratory, vi phạm §8 brief | **Không** |
| Hành vi của vai trò khác (NHT, vai trò Doanh nghiệp ở `SCR-V.III-04`) | Ngoài vế — case chỉ đo đúng vai trò `CB_NV_TW` của đối tác | **Không** |
| Nội dung tệp đính kèm khi bấm *Xem*/*Tải* trong cửa sổ | Vế (c) chỉ đòi **liệt kê đúng tên + đúng số tệp**, đã đo xong; mở tệp là chức năng khác | **Không** |

---

## 9. Tự kiểm trước khi chốt (cổng Flow 03)

| # | Câu hỏi | Trả lời |
|---|---|---|
| 1 | Chuẩn chấm có bám đúng SRS hiện tại + expected gốc? | Có — dùng nguyên bảng vế/điều kiện đã khoá ở `chuan/QLHSPLDN_06.md`, số dòng SRS đã tự mở file xác minh lại (`:6756`, `:6758`) |
| 2 | Có đo đúng phần còn lỗi, hay chạy lại phần đã đạt / kiểm chức năng kế bên? | Đo đúng 4 vế của phiếu. Bản dựng env đích khác nơi từng Pass ⇒ theo §0 nguồn chuẩn, **bắt buộc** đo lại toàn bộ, không phải chạy thừa |
| 3 | Reopen đã có FAIL hợp lệ chưa? | **Không có FAIL nào** ⇒ luật dừng sớm không kích hoạt; phải chạy hết mọi vế + biến thể để được Pass — đã chạy hết |
| 4 | Pass đã phủ hết vế/biến thể nguồn chuẩn yêu cầu? | Có — 4/4 dạng D1–D4, 3/3 trạng thái, 2/2 bảng, 7/7 hàng đếm thô, 5 lần bấm thật |
| 5 | Artifact có chứa quan sát quyết định và đã mở đọc lại? | Có — 5 ảnh, **từng ảnh đã mở ra đọc bằng mắt**, mô tả ở §5 |
| 6 | Người ngoài phiên đo có phân biệt được phần đạt / cần BA / chưa đo? | Có — §4 số đo, §6 verdict, §7 candidate, §8 phần chưa đo, đều tách bạch |
