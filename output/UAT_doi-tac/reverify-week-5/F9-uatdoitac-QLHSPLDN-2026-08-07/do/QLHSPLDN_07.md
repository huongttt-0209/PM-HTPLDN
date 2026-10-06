# GIAI ĐOẠN B — số đo thô · `QLHSPLDN_07` (tab `bug`, dòng 292 — "Sửa")

```
Lô:            F9 — tái xác nhận trên env NGHIỆM THU của đối tác
Flow:          flows/03-reverify-sau-dev-fix.md — NHÁNH 2 "Tái xác nhận trên môi trường khác"
Nguồn chuẩn:   chuan/QLHSPLDN_07.md (Giai đoạn A đã khoá) — làm đúng theo, sai lệch nào cũng khai ở §9
Env đo:        https://htpldn-uat.ospgroup.vn  (env nghiệm thu của đối tác)
Người đo:      agent ĐO · 2026-08-07 · phiên 13:37 → 13:57 giờ VN
```

---

## 1. Vân tay bản dựng — ĐẦU và CUỐI case

| Hạng mục | ĐẦU case — **13:37:50 VN 07/08** | CUỐI case — **13:57:15 VN 07/08** |
|---|---|---|
| Bó mã JS | `assets/index-D4NhKEjr.js` | `assets/index-D4NhKEjr.js` |
| Bó mã CSS | `assets/index-DVlgOkLg.css` | `assets/index-DVlgOkLg.css` |
| `GET /` `last-modified` | `Fri, 07 Aug 2026 04:17:55 GMT` (= 11:17 VN) | `Fri, 07 Aug 2026 04:17:55 GMT` |
| `GET /` `etag` | `W/"6a755c73-428"` | `W/"6a755c73-428"` |
| Máy chủ web | `nginx` | `nginx` |
| Chuỗi chân sidebar | `HTPLDN · V1.0.10` | `HTPLDN · V1.0.10` |

> ✅ **Hai đầu TRÙNG KHỚP tuyệt đối** ⇒ không có deploy chen giữa case ⇒ mọi quan sát thuộc **cùng một bản dựng**,
> không phải chia trước/sau mốc deploy. Trùng đúng vân tay nguồn chuẩn §Vân tay yêu cầu (`W/` chỉ là tiền tố weak
> validator do đọc bằng `fetch`, giá trị `6a755c73-428` không đổi).
>
> ⚠️ Bó mã này **khác** bản dựng env nội bộ nơi case từng Pass (`index-DIABnbIr.js`) ⇒ theo §0 nguồn chuẩn,
> **mọi vế đã đo lại từ đầu**, không vế nào miễn.

---

## 2. Tài khoản thực dùng + xác nhận vai trò

| Hạng mục | Giá trị |
|---|---|
| Tài khoản ra verdict | **`cbnv_tw`** (đúng tài khoản chỉ định, **không** fallback) |
| Nguồn xác nhận | `GET /api/v1/auth/me` → **200** |
| `hoTen` / `vaiTro` / `capDonVi` | `Cán bộ NV Trung ương` · `["CB_NV_TW"]` · `TW` |
| `donViId` | `00000000-0000-4000-8000-000000000001` (*Cục Bổ trợ tư pháp - Bộ Tư pháp*) |
| `userId` | `dfcf6bbf-45d7-4bc5-95ef-9403e66a0fc9` |
| Badge trên màn | `Cán bộ NV Trung ương · Cán bộ Nghiệp vụ Trung ương` · phạm vi `BTP · TW` |
| Số lượt đăng nhập `cbnv_tw` | 2 (phiên kế thừa 13:08 + đăng nhập lại 13:56 để chụp ảnh danh sách tệp) — không chạm giới hạn 5 lượt/60s |
| Tài khoản phụ | **`admin`** (`QTHT`, `Quản trị viên 1`) — đăng nhập 13:53, **CHỈ** để đọc màn Nhật ký hệ thống ở vế (c) |

⇒ **Toàn bộ 4 lượt bấm `Đồng ý` đều do `cbnv_tw` thực hiện.** `admin` **không** bấm lưu, không tạo/sửa bản ghi
nghiệp vụ nào, chỉ mở màn nhật ký để đọc.

---

## 3. Bản ghi đã tạo / đã đổi trên env đối tác

Tất cả trên `https://htpldn-uat.ospgroup.vn`, do `cbnv_tw` làm **bằng UI thật** (nút *Thêm hồ sơ* / *Sửa* → `Đồng ý`).

**Doanh nghiệp QA đã dùng (KHÔNG tạo mới):** `DN-HCM-0004` — *QA Doi chung 0311224488* ·
id `ac4a3173-3e2c-4f2a-b63d-cd44dd757fc6` (đúng DN QA mà lượt `_06` đã chốt).

**2 hồ sơ pháp lý QA TẠO MỚI cho case này:**

| Vai | Mã hồ sơ | id | Tạo lúc (VN) | Nội dung lúc tạo |
|---|---|---|---|---|
| **R1** — "đã có sẵn tệp trước thao tác" | `HSPL-20260807-0004` | `7e41624a-049e-4e69-bd5c-828b66f872fc` | 13:40:45 | `QA-W5-0807-HS-CU` · Khác · Thuế · 03/08/2026 → 03/08/2026 · `QA-W5-0807 coquan goc` · `QA-W5-0807 mo ta goc` · **Hiệu lực** · **1 tệp** `…-r1a.png` (88 B) |
| **R2** — bản ghi MỚI sau bản vá | `HSPL-20260807-0005` | `23b89366-069d-418e-8f4b-8902a9140aac` | 13:48:04 | `QA-W5-0807-HS-MOI` · Khác · **Hiệu lực** · 5 ô tuỳ chọn để trống · **1 tệp** `…-r2a.png` (73 B) |

**4 lượt bấm `Đồng ý` đã đổi gì** (mốc giờ lấy từ dòng nhật ký hệ thống — nguồn chính xác đến giây):

| Lượt | Giờ VN | Bản ghi | Dạng | Đổi gì |
|---|---|---|---|---|
| **1** | **13:42:48** | R1 | **D1** *(lượt quyết định)* | **CHỈ thêm 1 tệp** `…-r1b.png` (99 B). **Không đụng ô nào khác.** |
| **2** | **13:46:27** | R1 | D2+D3+D4 | 8 ô trong 1 lần: tên→`QA-W5-0807-1344-ten` · cơ quan→`…-1344-coquan` · mô tả→`…-1344-mota` · ngày cấp 03/08→**10/06/2026** · ngày hết hạn 03/08→**25/09/2026** · loại Khác→**Hợp đồng** · lĩnh vực Thuế→**Lao động** · trạng thái Hiệu lực→**Thu hồi** · **+1 tệp** `…-r1c.png` (79 B) |
| **3a** | **13:49:03** | R2 | **D1** | **CHỈ thêm 1 tệp** `…-r2b.png` (74 B). Không đụng ô nào khác. |
| **3b** | **13:51:24** | R2 | D2+D3+D4 | 8 ô trong 1 lần: tên→`QA-W5-0807-1349-ten` · cơ quan→`…-1349-coquan` · mô tả→`…-1349-mota` · ngày cấp (trống)→**12/04/2026** · ngày hết hạn (trống)→**30/11/2026** · loại Khác→**Giấy chứng nhận** · lĩnh vực (trống)→**Đầu tư** · trạng thái Hiệu lực→**Hết hạn** |

Tệp seed: `F9-uatdoitac-QLHSPLDN-2026-08-07/seed-files/QA-W5-0807-tep-07-{r1a,r1b,r1c,r2a,r2b}.png`
— 5 tệp PNG thật, **dung lượng khác nhau** (88 / 99 / 79 / 73 / 74 B) để phân biệt được cả bằng tên lẫn bằng cỡ.

**Bản ghi của ĐỐI TÁC — KHÔNG đụng gì:**

| Bản ghi | Thao tác đã làm | Thao tác KHÔNG làm |
|---|---|---|
| `DN-XX-0005` (`1a715c55-…3ce5`) | chỉ rời khỏi trang mà lượt trước để lại (không bấm gì trên bảng) | ❌ không thêm/sửa/xoá hồ sơ nào |
| `HSPL-20260803-0001` · `HSPL-20260731-0002` | — | ❌ không mở Sửa, không bấm lưu, không xoá |

> Tổng cộng: **2 bản ghi mới**, **0 bản ghi của đối tác bị đụng**, 0 module khác bị đụng.

**Đường UI đã đi:** menu trái *Doanh nghiệp* → hàng `DN-HCM-0004` → thẻ *Hồ sơ pháp lý* → nút **Sửa** trên hàng
hồ sơ → cửa sổ *Sửa hồ sơ pháp lý* → **`Đồng ý`**. (Chỉ 2 lần gõ URL trực tiếp: `/login` khi đổi tài khoản và
quay lại trang DN sau khi đăng nhập lại — không phải bước đo.)

---

## 4. Số đo thô — vế (a): cửa sổ Sửa mở kèm dữ liệu hiện có *(C1 + C2)*

Đọc ô chọn bằng `.ant-select-content`, đếm tệp bằng `.ant-upload-list-item-container` (đúng cảnh báo dụng cụ §7
nguồn chuẩn). Cột "Máy chủ" = đọc lại bản ghi theo id qua **đúng đường request UI phát ra**
(`GET /api/v1/ho-so-phap-ly-dns/{id}`, lấy từ `list_network_requests` reqid=457 khi bấm *Sửa*) — **không đoán**.

### 4.1 Biến thể R1 — bản ghi "đã có sẵn tệp" (mở form lúc 13:41, sau khi đã tải lại trang thật)

| Ô trên form | Form hiện | Máy chủ trả về | Khớp |
|---|---|---|---|
| Tên hồ sơ | `QA-W5-0807-HS-CU` | `tenHoSo` cùng chuỗi | ✅ |
| Loại hồ sơ | `Khác` | `loaiHoSo: "KHAC"` | ✅ |
| Lĩnh vực pháp lý | `Thuế` | `linhVuc.ten: "Thuế"` (`linhVucId: bbbbbbbb-…018`) | ✅ |
| Ngày cấp | `03/08/2026` | `ngayCap: "2026-08-03"` | ✅ |
| Ngày hết hạn | `03/08/2026` | `ngayHetHan: "2026-08-03"` | ✅ |
| Cơ quan cấp | `QA-W5-0807 coquan goc` | `coQuanCap` cùng chuỗi | ✅ |
| Trạng thái | `Hiệu lực` | `trangThai: "HIEU_LUC"` | ✅ |
| Mô tả | `QA-W5-0807 mo ta goc` | `ghiChu` cùng chuỗi | ✅ |
| **Tệp đính kèm** | **1 tệp** — `QA-W5-0807-tep-07-r1a.png (88 B)` | `fileDinhKem[]` **1 phần tử** — `tenFile` khớp, `dungLuong: 88` | ✅ |

**8/8 ô có dữ liệu điền sẵn đúng · 1/1 tệp đúng tên + đúng dung lượng.**

### 4.2 Biến thể R2 — bản ghi mới, có ô để trống (mở form lúc 13:48:5x, sau khi đã tải lại trang thật)

| Ô | Form hiện | Máy chủ | Khớp |
|---|---|---|---|
| Tên hồ sơ | `QA-W5-0807-HS-MOI` | cùng chuỗi | ✅ |
| Loại hồ sơ | `Khác` | `KHAC` | ✅ |
| Trạng thái | `Hiệu lực` | `HIEU_LUC` | ✅ |
| Lĩnh vực / Ngày cấp / Ngày hết hạn / Cơ quan cấp / Mô tả | **trống** (5 ô) | `null` (5 trường) | ✅ — không ô nào tự bịa giá trị |
| **Tệp đính kèm** | **1 tệp** — `QA-W5-0807-tep-07-r2a.png (73 B)` | `fileDinhKem[]` 1 phần tử, `dungLuong: 73` | ✅ |

### 4.3 Thêm 4 mẫu nữa (mở lại form sau MỖI lượt lưu, đều sau khi tải lại trang thật)

| Lần mở | Số ô so | Ô lệch | Số tệp trên form | Số tệp máy chủ | Khớp |
|---|---|---|---|---|---|
| Sau lượt 1 (R1) | 8 | **0** | **2** — r1b (99 B) + r1a (88 B) | 2, tên + dung lượng khớp | ✅ |
| Sau lượt 2 (R1) | 8 | **0** | **3** — r1c (79 B) + r1b (99 B) + r1a (88 B) | 3, khớp | ✅ |
| Sau lượt 3a (R2) | 3 (+5 ô trống) | **0** | **2** — r2b (74 B) + r2a (73 B) | 2, khớp | ✅ |
| Sau lượt 3b (R2) | 8 | **0** | **2** — r2b + r2a | 2, khớp | ✅ |

⇒ **Vế (a) ĐẠT** trên cả 2 biến thể bắt buộc (R1 + R2), tổng **6 lần mở form**, **0 ô lệch**, **0 tệp thiếu/thừa**.

---

## 5. Số đo thô — vế (b): bấm Lưu → bản ghi được cập nhật *(C3)*

**Cách đo mỗi lượt** (đủ cả 5 điều kiện PASS §4 nguồn chuẩn):

1. Bấm **`Đồng ý`** trong cửa sổ Sửa bằng **UI thật**.
2. Bộ bắt thông báo `MutationObserver` cài **TRƯỚC** khi bấm, đọc `innerText`, **không dedupe**, bọc **cả `fetch`
   LẪN `XMLHttpRequest`**. **Tự kiểm `soObserverDangSong = 1` ngay trước MỖI lượt** (observer bị xoá sau mỗi lần
   tải lại trang → đã cài lại + kiểm lại 4/4 lượt).
3. Đường (i): **tải lại trang thật bỏ đệm** (`reload ignoreCache`) → mở lại chính bản ghi → so từng ô.
4. Đường (ii): **đọc lại bản ghi theo id từ máy chủ** bằng **đúng đường UI phát ra khi bấm Lưu** — lấy từ
   `list_network_requests`: UI gửi `PATCH /api/v1/ho-so-phap-ly-dns/{id}`, đọc lại bằng
   `GET /api/v1/ho-so-phap-ly-dns/{id}` (chính request cửa sổ Sửa dùng). **Không đoán đường dẫn.**

### 5.1 Bảng số đo 4 lượt

| Lượt | `soObserverDangSong` | `SO_REQUEST` | Request UI phát ra | `SO_KHUNG_THONG_BAO` | Chữ thông báo |
|---|---|---|---|---|---|
| 1 — D1/R1 | **1** ✅ | **1** | `PATCH /api/v1/ho-so-phap-ly-dns/7e41624a-…f872fc` | **1** | `Cập nhật hồ sơ thành công` |
| 2 — D2+D3+D4/R1 | **1** ✅ | **1** | `PATCH /api/v1/ho-so-phap-ly-dns/7e41624a-…f872fc` | **1** | `Cập nhật hồ sơ thành công` |
| 3a — D1/R2 | **1** ✅ | **1** | `PATCH /api/v1/ho-so-phap-ly-dns/23b89366-…40aac` | **1** | `Cập nhật hồ sơ thành công` |
| 3b — D2+D3+D4/R2 | **1** ✅ | **1** | `PATCH /api/v1/ho-so-phap-ly-dns/23b89366-…40aac` | **1** | `Cập nhật hồ sơ thành công` |

Không lượt nào double-toast (`SO_KHUNG = 1`, `khoangCachMs = null`). `list_console_messages` type=error (giữ qua
3 lần điều hướng) = **rỗng**.

### 5.2 Lượt 1 — **D1 trên R1** *(bản sao chính xác thao tác đối tác: chỉ thêm 1 tệp, không đụng ô nào)*

| Thứ cần lưu | Đường (i) — sau **tải lại trang thật** | Đường (ii) — đọc lại từ máy chủ | Khớp |
|---|---|---|---|
| Tệp vừa thêm `…-r1b.png` | **có**, `(99 B)` | `fileDinhKem[]` có `tenFile: "QA-W5-0807-tep-07-r1b.png"`, `dungLuong: 99` | ✅ |
| Tệp cũ `…-r1a.png` | **còn**, `(88 B)` | còn, `dungLuong: 88` | ✅ |
| **Tổng số tệp** | **2** | **2** | ✅ |
| 8 ô không đụng | y nguyên | y nguyên | ✅ |

⇒ **Dạng D1 — dạng mà cả 2 vòng QA trước KHÔNG đo — LƯU ĐƯỢC.** Hai đường **không mâu thuẫn**.

### 5.3 Lượt 2 — **D2+D3+D4 trên R1**, 1 lần bấm, 8 ô + 1 tệp

| Ô | Giá trị nhập | Đường (i) sau tải lại trang | Đường (ii) máy chủ | Khớp |
|---|---|---|---|---|
| Tên hồ sơ *(D2)* | `QA-W5-0807-1344-ten` | `QA-W5-0807-1344-ten` | `tenHoSo` cùng chuỗi | ✅ |
| Cơ quan cấp *(D2)* | `QA-W5-0807-1344-coquan` | khớp | `coQuanCap` cùng chuỗi | ✅ |
| Mô tả *(D2, text dài)* | `QA-W5-0807-1344-mota` | khớp | `ghiChu` cùng chuỗi | ✅ |
| Ngày cấp *(D3)* | `10/06/2026` | `10/06/2026` | `ngayCap: "2026-06-10"` | ✅ |
| Ngày hết hạn *(D3)* | `25/09/2026` | `25/09/2026` | `ngayHetHan: "2026-09-25"` | ✅ |
| Loại hồ sơ *(D4 enum)* | `Hợp đồng` | `Hợp đồng` | `loaiHoSo: "HOP_DONG"` | ✅ |
| Lĩnh vực pháp lý *(D4 khoá ngoại)* | `Lao động` | `Lao động` | `linhVuc.ten: "Lao động"` | ✅ |
| Trạng thái *(D4 enum)* | `Thu hồi` | `Thu hồi` | `trangThai: "THU_HOI"` | ✅ |
| **Tệp thêm `…-r1c.png`** | — | **có**, `(79 B)`; tổng **3 tệp** | 3 phần tử, `dungLuong: 79` | ✅ |

`version` 1 → **2**, `ngayCapNhat` → `2026-08-07T06:46:27.314Z` (= 13:46:27 VN),
`nguoiCapNhatId = dfcf6bbf-…f0a9` (đúng `cbnv_tw`).

### 5.4 Lượt 3a — **D1 trên R2**

| Thứ cần lưu | Đường (i) | Đường (ii) | Khớp |
|---|---|---|---|
| Tệp vừa thêm `…-r2b.png` | **có**, `(74 B)` | `dungLuong: 74` | ✅ |
| Tệp cũ `…-r2a.png` | **còn**, `(73 B)` | `dungLuong: 73` | ✅ |
| **Tổng số tệp** | **2** | **2** | ✅ |

### 5.5 Lượt 3b — **D2+D3+D4 trên R2**, 1 lần bấm, 8 ô

| Ô | Giá trị nhập | Đường (i) sau tải lại trang | Đường (ii) máy chủ | Khớp |
|---|---|---|---|---|
| Tên hồ sơ | `QA-W5-0807-1349-ten` | khớp | `tenHoSo` cùng chuỗi | ✅ |
| Cơ quan cấp | `QA-W5-0807-1349-coquan` | khớp | cùng chuỗi | ✅ |
| Mô tả | `QA-W5-0807-1349-mota` | khớp | cùng chuỗi | ✅ |
| Ngày cấp | `12/04/2026` (từ **trống**) | `12/04/2026` | `"2026-04-12"` | ✅ |
| Ngày hết hạn | `30/11/2026` (từ **trống**) | `30/11/2026` | `"2026-11-30"` | ✅ |
| Loại hồ sơ | `Giấy chứng nhận` | khớp | `GIAY_CN` | ✅ |
| Lĩnh vực pháp lý | `Đầu tư` (từ **trống**) | khớp | `linhVuc.ten: "Đầu tư"` | ✅ |
| Trạng thái | `Hết hạn` | khớp | `HET_HAN` | ✅ |
| Tệp | không thêm | vẫn **2** | vẫn 2 | ✅ |

`version` 1 → **2**, `ngayCapNhat` → `2026-08-07T06:51:24.344Z` (= 13:51:24 VN), `nguoiCapNhatId` đúng `cbnv_tw`.

### 5.6 Số đo thông báo ↔ request khớp LOẠI

4/4 lượt: **request lưu thành công** (bản ghi thật sự đổi ở cả 2 đường) **và** hiện toast thành công ⇒ đúng
`srs-v3.5.md:576` (*"Toast notification cho thao tác thành công"*). **Không có lượt nào** rơi vào ca cấm của
`srs-v3.5.md:582` (*"KHÔNG nuốt lỗi trong im lặng"*) — tức **không có** ca "báo thành công mà bản ghi không đổi",
đúng chỗ đối tác báo lỗi.

⇒ **Vế (b) ĐẠT** trên đủ **D1–D5**, đo bằng **2 đường độc lập**, hai đường **không mâu thuẫn ở bất kỳ ô nào**.

---

## 6. Số đo thô — vế (c): lưu vết thao tác *(C4 — ĐƯỜNG A)*

**Đường A khả dụng.** `admin` (QTHT) mở được **Quản trị hệ thống → Nhật ký hệ thống**
(`/quan-tri/audit-log`), bảng read-only đủ cột theo `srs-fr-10-quan-tri.md:1984`
(*Thời gian / Người dùng / Đơn vị / Module / Entity / Mã bản ghi / Loại thao tác / Chi tiết thay đổi*),
khoảng thời gian mặc định `31/07/2026 – 07/08/2026` bao trùm cả phiên. Tổng `2990` dòng.

**Dòng nhật ký đọc được cho đúng 4 lượt bấm (+ 2 lượt tạo tiền đề):**

| Thời gian (nhật ký) | Người dùng | Đơn vị | Entity | Mã bản ghi | Loại thao tác | Ứng với |
|---|---|---|---|---|---|---|
| 07/08/2026 **13:51:24** | Cán bộ NV Trung ương | Cục Bổ trợ tư pháp - Bộ Tư pháp | `HO_SO_PHAP_LY_DN` | `23b89366…` | **Cập nhật** | **lượt 3b** |
| 07/08/2026 **13:49:03** | Cán bộ NV Trung ương | Cục Bổ trợ tư pháp - Bộ Tư pháp | `HO_SO_PHAP_LY_DN` | `23b89366…` | **Cập nhật** | **lượt 3a (D1)** |
| 07/08/2026 13:48:04 | Cán bộ NV Trung ương | — | `HO_SO_PHAP_LY_DN` | `23b89366…` | Tạo mới | tạo R2 |
| 07/08/2026 **13:46:27** | Cán bộ NV Trung ương | Cục Bổ trợ tư pháp - Bộ Tư pháp | `HO_SO_PHAP_LY_DN` | `7e41624a…` | **Cập nhật** | **lượt 2** |
| 07/08/2026 **13:42:48** | Cán bộ NV Trung ương | Cục Bổ trợ tư pháp - Bộ Tư pháp | `HO_SO_PHAP_LY_DN` | `7e41624a…` | **Cập nhật** | **lượt 1 (D1)** |
| 07/08/2026 13:40:45 | Cán bộ NV Trung ương | — | `HO_SO_PHAP_LY_DN` | `7e41624a…` | Tạo mới | tạo R1 |

**Mở rộng dòng 13:42:48 (lượt D1 — lượt quyết định)** để xác nhận trỏ đúng bản ghi, không chỉ trùng UUID rút gọn:

```
Dữ liệu cũ:  —
Dữ liệu mới: { "id": "7e41624a-049e-4e69-bd5c-828b66f872fc",
               "maHoSo": "HSPL-20260807-0004",
               "tenHoSo": "QA-W5-0807-HS-CU",
               "doanhNghiepId": "ac4a3173-3e2c-4f2a-b63d-cd44dd757fc6",
               "nguoiCapNhatId": "dfcf6bbf-45d7-4bc5-95ef-9403e66a0fc9", … }
```

Đối chiếu điều kiện PASS C4:

| Điều kiện | Số đo | Đạt |
|---|---|---|
| Có dòng log đúng giây bấm (± sai số hiển thị) | 4/4 lượt có dòng; 2/4 lượt trùng **đúng đến giây** với `ngayCapNhat` máy chủ (13:46:27 / 13:51:24) | ✅ |
| `nguoi_dung` = tài khoản đã bấm | 4/4 dòng ghi `Cán bộ NV Trung ương` + đơn vị `Cục Bổ trợ tư pháp - Bộ Tư pháp`; JSON chi tiết ghi `nguoiCapNhatId = dfcf6bbf-…f0a9` = đúng `userId` của `cbnv_tw` | ✅ |
| Cột Entity / Mã bản ghi trỏ đúng hồ sơ HSPL | `HO_SO_PHAP_LY_DN` + `7e41624a…` / `23b89366…` = đúng id 2 bản ghi QA; JSON chi tiết in cả `maHoSo` | ✅ |
| Đủ dòng cho **mọi** lượt bấm U4/U5/U7/U8 | **4/4** | ✅ |

⇒ Rơi đúng **hàng 1** cây quyết định §2 nguồn chuẩn: **Đường A đạt ⇒ vế (c) PASS**, đóng cả yêu cầu SRS
(`srs-fr-12:627`, `:689`, `:714`; `srs-fr-07:819`/`:821`; `srs-fr-10:2423`) lẫn yêu cầu phiếu.

**Đường B (đối chứng phụ, KHÔNG dùng để chấm vì Đường A đã khả dụng):** 2 lượt sửa ô (`lượt 2`, `lượt 3b`) có
`ngayCapNhat` + `version` đổi đúng người đúng giây. 2 lượt **chỉ thêm tệp** (D1) có `ngayCapNhat`/`version` của
**bản ghi cha** không đổi — xem candidate 1 ở §8; **không** kéo verdict vì Đường A là đường chính và đã đạt.

---

## 7. Artifact quyết định verdict

Tất cả ở `F9-uatdoitac-QLHSPLDN-2026-08-07/image/`. **Từng ảnh đã mở ra đọc bằng mắt**, không kết luận bằng
script chạy trong trang.

| Ảnh | Thấy gì trong ảnh |
|---|---|
| `07-A-form-Sua-R1-HSPL-20260807-0004-9o-dien-san-1tep.png` | Cửa sổ **Sửa hồ sơ pháp lý** của R1 mở kèm **dữ liệu hiện có**: `QA-W5-0807-HS-CU` · Khác · Thuế · 03/08/2026 · 03/08/2026 · `QA-W5-0807 coquan goc` · Hiệu lực · `QA-W5-0807 mo ta goc` — không ô nào trống oan. |
| `07-B-luot1-D1-R1-sau-tai-lai-trang-2tep-r1a-r1b.png` | Sau **lượt 1 (D1)** và **tải lại trang thật**: form mở lại, 8 ô giữ nguyên đúng giá trị cũ (`QA-W5-0807-HS-CU` / Khác / Thuế / 03/08/2026 ×2 / coquan goc / Hiệu lực / mo ta goc) — chứng minh lượt chỉ-thêm-tệp **không xoá trắng** ô nào. |
| `07-C-luot2-D2D3D4-R1-sau-tai-lai-trang-8o-moi-3tep.png` | Sau **lượt 2** và **tải lại trang thật**: cả **8 ô mang giá trị MỚI** đọc rõ trên màn — `QA-W5-0807-1344-ten` · **Hợp đồng** · **Lao động** · **10/06/2026** · **25/09/2026** · `QA-W5-0807-1344-coquan` · **Thu hồi** · `QA-W5-0807-1344-mota`. Bảng phía sau cũng đã đổi sang `10/06/2026`. |
| `07-D-luot3b-D2D3D4-R2-HSPL-20260807-0005-sau-tai-lai-trang.png` | Cùng kết quả trên **bản ghi MỚI R2** sau lượt 3b — `QA-W5-0807-1349-ten` · Giấy chứng nhận · Đầu tư · 12/04/2026 · 30/11/2026 · Hết hạn. |
| **`07-F-R1-danh-sach-3-tep-sau-tai-lai-trang-va-dang-nhap-lai.png`** | **Bằng chứng mạnh nhất cho phần tệp.** Cuộn xuống hết cửa sổ Sửa của R1, chụp **sau khi đăng xuất → đăng nhập lại → tải trang mới**: mục *Tệp đính kèm* liệt kê **đủ 3 tệp** `…-r1c.png (79 B)` · `…-r1b.png (99 B)` · `…-r1a.png (88 B)`, kèm 8 ô đã sửa. Cả tệp thêm ở lượt 1 lẫn lượt 2 đều còn. |
| `07-E-nhatky-he-thong-4-dong-Cap-nhat-HO_SO_PHAP_LY_DN.png` | **Bằng chứng vế (c).** Màn *Nhật ký hệ thống* (đăng nhập QTHT): 4 dòng **Cập nhật** lúc 13:51:24 / 13:49:03 / 13:46:27 / 13:42:48 + 2 dòng **Tạo mới** 13:48:04 / 13:40:45, tất cả `Người dùng = Cán bộ NV Trung ương`, `Đơn vị = Cục Bổ trợ tư pháp - Bộ Tư pháp`, `Entity = HO_SO_PHAP_LY_DN`, `Mã bản ghi = 23b89366…` / `7e41624a…`. Dòng 13:42:48 đang mở rộng, đọc rõ `"id": "7e41624a-049e-4e69-bd5c-828b66f872fc"`, `"maHoSo": "HSPL-20260807-0004"`. |

---

## 8. Verdict

# 📌 **Pass** — HIỆN TẠI ĐẠT

**Bám luật Flow 03 §Chốt (bảng Verdict logic), dòng "Pass":**

1. **Mọi vế đều `MATCH` và đều đạt.** (a1) cửa sổ Sửa mở kèm dữ liệu hiện có · (a2) mục Tệp đính kèm phản ánh
   đúng tệp bản ghi đang có · (b) bấm Lưu → bản ghi được cập nhật · (c) thao tác Sửa để lại lưu vết —
   **cả 4 vế đo được và đều đạt**. Không vế nào FAIL ⇒ luật dừng sớm không kích hoạt.
2. **Đã chạy HẾT biến thể bắt buộc M = 5.** D1 ✅ (2 lượt: R1 + R2 — **dạng cả 2 vòng trước bỏ sót**) ·
   D2 ✅ (3 ô chữ, có ô text dài) · D3 ✅ (2 ô ngày, cả ca "đổi giá trị cũ" lẫn ca "điền từ trống") ·
   D4 ✅ (2 enum + 1 khoá ngoại) · D5 ✅ *một nửa hợp lệ* (chiều "bản ghi mới sau bản vá" = R2; chiều
   "cũ hơn bản vá" được MIỄN theo §3.2 nguồn chuẩn — khai nguyên văn ở §10).
   **4 lượt bấm `Đồng ý`, phủ đủ D1–D5.**
3. **Đủ 5 điều kiện PASS vế (b).** Thao tác bằng UI thật · đo bằng **2 đường độc lập** (tải lại trang thật +
   đọc lại bản ghi theo id qua đúng đường request UI phát ra) · **mọi trường vừa sửa mang giá trị mới ở CẢ HAI
   đường**, đối chiếu bằng dấu nhận dạng duy nhất `QA-W5-0807-<HHmm>-<tên ô>` · thông báo ↔ request **khớp loại**
   4/4 lượt · phủ đủ 5 dạng.
4. **Không Pass bằng quan sát tĩnh.** Không lượt nào kết luận từ "giá trị còn trên form", từ "dòng trong bảng đã
   đổi", hay từ việc bấm lại cùng nút. **6 lần tải lại trang thật bỏ đệm** + **1 lần đăng xuất → đăng nhập lại**
   trước khi đọc kết quả.
5. **Hai đường (i)/(ii) không mâu thuẫn ở bất kỳ ô nào** ⇒ không rơi vào ca "Chưa chốt".
6. **Vế (c) đóng bằng Đường A** (màn Nhật ký hệ thống), không phải bằng `updated_at`/`updated_by` —
   đúng ràng buộc "❌ Đóng vế (c) bằng Đường B trong khi màn Nhật ký MỞ ĐƯỢC" ở §6 nguồn chuẩn.

**Giới hạn hiệu lực (bắt buộc ghi):** Pass này **chỉ có hiệu lực trên env `https://htpldn-uat.ospgroup.vn`**,
bản dựng `assets/index-D4NhKEjr.js` · `last-modified Fri, 07 Aug 2026 04:17:55 GMT`, đo lúc **13:37 → 13:57 giờ
VN 07/08/2026**, với vai trò **`CB_NV_TW`**.

**Không viết "fix đã có tác dụng":** phiên này **không có** bằng chứng trạng thái lỗi trước fix do chính QA chụp
trên env + bản dựng này ⇒ chỉ kết luận **hiện trạng ĐẠT so với SRS + expected gốc**, dùng chữ *HIỆN TẠI ĐẠT*,
**không** dùng *ĐÃ HẾT LỖI*.

**Ghi ô Drive theo mapping §7 brief:** `Trạng thái dev fix` = **`UAT done`**.

---

## 9. Sai lệch so với tiêu chí đã khóa — phải khai

| Điểm | Nguồn chuẩn yêu cầu | Thực tế đã làm | Vì sao |
|---|---|---|---|
| **Bộ lọc `Module = DN` ở U9** | *"lọc `module = DN`, `hanh_dong = Sửa`, `Entity` = mã bản ghi"* | **Không lọc `Module = DN`**; đọc bảng theo khoảng thời gian mặc định rồi đối chiếu theo giây + Entity + Mã bản ghi | Trên bản dựng này, dòng nhật ký của `HO_SO_PHAP_LY_DN` được xếp `Module = **Tư vấn**`, **không phải `DN`**. Lọc đúng chữ trong nguồn chuẩn sẽ trả **0 dòng** ⇒ tạo ra một FAIL giả. Xếp loại "Tư vấn" là **hợp lý**: đặc tả `FR-X.1-04` nằm trong `srs-fr-12-tv-chuyen-sau.md`; `srs-fr-10:1387` liệt kê **cả** `DN` **lẫn** `Tư vấn` trong danh sách giá trị bộ lọc, không nói HSPL thuộc nhóm nào. |
| **Bộ lọc `Loại thao tác = Sửa`** | như trên | Không dùng bộ lọc; đọc trực tiếp cột | Cột `Loại thao tác` trên bản dựng hiển thị **`Cập nhật`** / **`Tạo mới`** (nhãn tiếng Việt của thao tác U/C), trong khi `srs-fr-10:1981` viết `Sua` / `Tao`. Đây là khác biệt **câu chữ nhãn**, không phải thiếu dữ liệu — theo luật *describe-not-prescribe* thì không chấm, nhưng nếu lọc theo đúng chữ `Sửa` có thể trả 0 dòng. |
| **U3 "đóng form, KHÔNG bấm Đồng ý"** | đóng bằng nút | Đóng bằng phím `Esc` | Cùng hiệu ứng đóng không lưu; đã xác nhận `modalVisible = false` và bản ghi không phát request nào. |
| **Ảnh danh sách tệp** | ảnh chụp trong lúc đo | Ảnh `07-F` chụp **sau khi đăng xuất `admin` → đăng nhập lại `cbnv_tw`** | 3 ảnh chụp trong lúc đo bị cắt phần *Tệp đính kèm* dưới màn (cửa sổ dài hơn khung nhìn). Việc chụp lại **chỉ mở form đọc rồi đóng bằng `Esc`, KHÔNG bấm `Đồng ý`**, không tạo/đổi dữ liệu — và vì đọc lại sau một phiên đăng nhập hoàn toàn mới nên bằng chứng **mạnh hơn**, không yếu hơn. |

---

## 10. Bug mới / candidate

Chỉ ghi nhận sai lệch **tự lộ trong chính luồng bắt buộc**; **không** bấm thử thêm, **không** mở chức năng khác,
**không** dùng thêm lượt xác nhận nào (đã dùng 0/1).

### Candidate 1 — lượt Sửa chỉ-thêm-tệp không làm đổi `ngayCapNhat` / `version` của bản ghi cha

```
Bấm Sửa → chỉ thêm 1 tệp → Đồng ý: tệp lưu đủ và nhật ký hệ thống có dòng "Cập nhật", nhưng trường
"ngày cập nhật" của chính bản ghi hồ sơ vẫn giữ nguyên mốc lúc tạo · xuất hiện tại lượt 1 (13:42:48, R1)
và lượt 3a (13:49:03, R2) — đều là bước bắt buộc của dạng D1 · artifact: đọc lại bản ghi từ máy chủ
(ngayCapNhat R1 = 06:40:45.630Z không đổi sau lượt 13:42:48; R2 = 06:48:04.602Z không đổi sau lượt 13:49:03)
+ ảnh 07-E cho thấy nhật ký VẪN ghi dòng Cập nhật đúng giây · còn thiếu: BA/BE xác nhận "ngày cập nhật" của
hồ sơ có phải phản ánh cả thay đổi tệp đính kèm hay chỉ thay đổi trường của chính bảng hồ sơ
```

- **Căn cứ SRS (đã mở file đọc, không quote từ trí nhớ):**
  `srs-fr-12-tv-chuyen-sau.md:1441` — *"| 16 | updated_at | datetime | Y | DEFAULT NOW() | NOW() | Ngày cập nhật |"*;
  `:1443` — *"| 18 | updated_by | identifier | N | FK → TAI_KHOAN(id) | — | Người cập nhật |"*.
  **SRS im lặng** về việc thay đổi *danh sách tệp đính kèm* có phải bump `updated_at` của bảng hồ sơ hay không.
- **Vì sao chỉ là candidate, KHÔNG kéo verdict:**
  ① Cây quyết định §2 nguồn chuẩn đặt **Đường A là đường chính**, Đường B chỉ dùng khi Đường A **không khả dụng** —
  Đường A khả dụng và đã đạt đủ 4/4 lượt. ② §6 nguồn chuẩn xếp `version` vào nhóm *"chỉ làm đối chứng phụ, không
  làm tiêu chí Pass"*. ③ Dữ liệu **không mất**: tệp lưu đủ ở cả 2 đường đo, và thao tác **có** để lại lưu vết.
  ④ SRS im lặng ⇒ candidate, không log như bug đã xác nhận.

### Ghi nhận KHÔNG thành candidate

- **Nhãn nút submit là `Đồng ý` thay vì `Lưu`** (`srs-v3.5.md:6756` quy ước H4) — §6 nguồn chuẩn đã xếp đúng mục
  này vào nhóm "không được chấm Fail", và `_06` đã mở candidate cùng họ (nhãn `Thêm hồ sơ`). Không lặp lại.
- **Chữ thông báo `Cập nhật hồ sơ thành công`** — SRS im lặng về câu chữ cho thao tác Sửa hồ sơ; `srs-v3.5.md:576`
  chỉ đòi **có** toast. Chỉ FAIL khi **sai LOẠI**, mà 4/4 lượt đều đúng loại. Không phải sai lệch.
- **Nút `Sửa` hiện trên dòng hồ sơ của `DN-XX-0005`** — câu hỏi BA §8.1 nguồn chuẩn **không phát sinh**: phiên này
  không bấm `Sửa` trên bản ghi đơn vị khác, không gặp `403 ERR-AUTH-VPD-00-01`, và toàn bộ bản ghi đo được đều
  thuộc đúng đơn vị TW của `cbnv_tw` ⇒ chưa có hiện tượng nào tự lộ để hỏi.
- **Hành vi khi GỠ tệp lúc Sửa** — câu hỏi BA §8.2 **không phát sinh**: không lượt nào gỡ tệp (nguồn chuẩn cấm
  chủ động thử).
- **Nhật ký ghi `Dữ liệu cũ: —`** ở dòng Cập nhật — `srs-fr-10:1405` chỉ đòi `chi_tiet`; `:1984` mô tả cột là
  *"JSON diff: old_value → new_value, expandable"*. Hiện trạng có `chi_tiet` đầy đủ (ảnh chụp toàn bộ bản ghi mới)
  nhưng thiếu vế `old_value`. **Ngoài vế của case này** (case chỉ đòi *có* lưu vết) và đã có nhiều dòng khác trong
  bảng cùng hình dạng ⇒ ghi nhận, không mở candidate mới để tránh exploratory.

---

## 11. Phần chưa đo được

| Phần | Lý do | Có ảnh hưởng verdict? |
|---|---|---|
| **Chiều "bản ghi tồn tại từ TRƯỚC bản vá" của D5** | Khai nguyên văn theo §3.2 nguồn chuẩn: *cách dựng này phủ được chiều "bản ghi đã có sẵn tệp trước thao tác" — chiều quyết định của kịch bản đối tác. Nó **KHÔNG** phủ được chiều "bản ghi tồn tại từ trước bản vá", vì trên môi trường nghiệm thu không có bản ghi QA nào cũ hơn bản dựng đang đo, và hai hồ sơ cũ thật là dữ liệu của đối tác nên không được thao tác lên.* ⇒ Giả thuyết *"dữ liệu tạo trước bản vá bị đóng băng"* **chưa được loại trừ trên env này**. | **Không** — nguồn chuẩn §5 khai đây là dạng **MIỄN hợp lệ một nửa**; chiều quyết định (R1 "đã có sẵn tệp") đã phủ. Không hạ verdict xuống Chưa chốt. |
| Hồ sơ có `nguon = CONG_PLQG` | Phải đến từ API inbound của Cổng PLQG, QA không tạo được bằng UI | **Không** — ngoài vế; 5/5 hồ sơ QA và toàn bộ hồ sơ đối tác đều là *Thủ công* |
| Hành vi gỡ tệp đính kèm khi Sửa | SRS im lặng hoàn toàn; nguồn chuẩn **cấm chủ động thử** | **Không** |
| Hành vi của vai trò khác (NHT, vai trò Doanh nghiệp) | Ngoài vế — case chỉ đo đúng vai trò `CB_NV_TW` của đối tác | **Không** |
| Bộ lọc `Module` / `Loại thao tác` trên màn Nhật ký có trả đúng dòng HSPL không | Đo thêm = exploratory + phải đăng nhập lại QTHT; nguồn chuẩn giới hạn 1 phép xác nhận cho cả case (đã dùng 0/1 nhưng không có hiện tượng đủ nặng để tiêu) | **Không** — vế (c) đã đóng bằng dòng log đọc trực tiếp; xem §9 |

---

## 12. Tự kiểm trước khi chốt (cổng Flow 03)

| # | Câu hỏi | Trả lời |
|---|---|---|
| 1 | Chuẩn chấm có bám đúng SRS hiện tại + expected gốc? | Có — dùng nguyên bảng vế/điều kiện đã khoá ở `chuan/QLHSPLDN_07.md`; **đã tự mở file SRS đọc lại từng dòng** `srs-fr-12:573 587 620 624 625 626 627 687 688 689 708 714 1440-1444`, `srs-fr-10:1365 1371 1373 1387 1388 1405 1981 1982 1984 2423`, `srs-v3.5.md:576 582` — khớp nguyên văn nguồn chuẩn |
| 2 | Có đo đúng phần còn lỗi, hay chạy lại phần đã đạt / kiểm chức năng kế bên? | Đo đúng 3 vế của phiếu (mở form kèm dữ liệu · lưu được · lưu vết). Bản dựng env đích khác nơi từng Pass ⇒ theo §0 nguồn chuẩn **bắt buộc** đo lại toàn bộ |
| 3 | Reopen đã có FAIL hợp lệ chưa? | **Không có FAIL nào** ⇒ luật dừng sớm không kích hoạt; phải chạy hết mọi vế + biến thể để được Pass — đã chạy hết |
| 4 | Pass đã phủ hết vế/biến thể nguồn chuẩn yêu cầu? | Có — 4 lượt bấm Lưu phủ D1–D5, 2 bản ghi (R1 + R2), 6 lần mở form đối chiếu, 6 lần tải lại trang thật, 4/4 lượt có dòng nhật ký |
| 5 | Artifact có chứa quan sát quyết định và đã mở đọc lại? | Có — 6 ảnh, **từng ảnh đã mở ra đọc bằng mắt**, mô tả ở §7. Ảnh quyết định: `07-F` (3 tệp còn đủ sau đăng nhập lại) và `07-E` (4 dòng nhật ký) |
| 6 | Người ngoài phiên đo có phân biệt được phần đạt / cần BA / chưa đo? | Có — §4-§6 số đo, §8 verdict, §9 sai lệch phương pháp, §10 candidate, §11 phần chưa đo, tách bạch |
