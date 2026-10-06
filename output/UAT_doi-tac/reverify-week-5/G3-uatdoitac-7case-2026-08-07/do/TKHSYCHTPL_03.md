# NHẬT KÝ ĐO — TKHSYCHTPL_03 (dòng 50) · Lô G3 · env nghiệm thu đối tác

> Chuẩn chấm đã khoá trước khi đo: [`chuan/TKHSYCHTPL_03.md`](../chuan/TKHSYCHTPL_03.md).
> **Không sửa chuẩn chấm trong/sau lượt đo này.**

## 0. Bảng đầu

| Mục | Giá trị |
|---|---|
| Env | `https://htpldn-uat.ospgroup.vn` (env NGHIỆM THU của đối tác) |
| **Bản dựng đọc trên UI** | **`HTPLDN · V1.0.10`** — đọc ở chân sidebar **sau khi `reload ignoreCache`** |
| Bó mã FE | `https://htpldn-uat.ospgroup.vn/assets/index-Bd1akG3f.js` |
| Tài khoản | **`cbnv_tw`** — phiên có sẵn, **không đăng nhập lại** (env giới hạn 5 lượt/60s) |
| Vai trò / đơn vị đo được trên màn | `Cán bộ NV Trung ương` · `Cán bộ Nghiệp vụ Trung ương` · `BTP · TW` |
| Vai trò theo đặc tả | `srs-fr-05-vu-viec.md:94` — *"**Tác nhân:** CB NV (TW/BN/ĐP)"*; phạm vi TW xem toàn quốc `:2450` |
| Màn | SCR-V.I-01 — Danh sách Hồ sơ Vụ việc |
| URL thật | `https://htpldn-uat.ospgroup.vn/vu-viec/danh-sach` (vào bằng **click sidebar "Vụ việc HTPL"**) |
| **Tab đứng khi đo** | **Tất cả** (xem §2 — bẫy số 1) |
| Thời gian đo | 2026-08-07, **17:41 – 17:50 giờ VN** |
| Verdict | ✅ **Pass** |

---

## 1. B0 — Tải lại trang, đọc bản dựng

`navigate_page type=reload ignoreCache=true` → đọc lại trên UI:

```
banDungUI  : ["HTPLDN · V1.0.10"]
boMaFE     : ["https://htpldn-uat.ospgroup.vn/assets/index-Bd1akG3f.js"]
```

Bản dựng của bằng chứng đối tác là **V1.0.2**, lượt đo cũ ở env nội bộ là **V1.0.5** — cả hai đều **khác** bản
đang chạy ⇒ mọi kết luận dưới đây chỉ có hiệu lực cho **V1.0.10 trên env nghiệm thu**.

---

## 2. Bẫy 2 — Đếm lại tiền đề NGAY trước khi đo (việc đầu tiên)

Gọi trong trang bằng `fetch(..., {credentials:'include'})` (không dùng curl ngoài), lúc **`2026-08-07T10:41:17.726Z` = 17:41 giờ VN**:

| Phép đếm | HTTP | `meta.total` | `meta.tabCounts` |
|---|---|---|---|
| `GET /api/v1/vu-viecs?mucSla=SAP_HET&page=1&pageSize=5` | **200** | **1** | `{TAT_CA:1, CHO_TIEP_NHAN:0, DANG_XU_LY:0, CHO_PHE_DUYET:0, HOAN_THANH:1, TU_CHOI:0}` |
| `GET /api/v1/vu-viecs?page=1&pageSize=1` (không lọc) | **200** | **74** | `{TAT_CA:74, CHO_TIEP_NHAN:5, DANG_XU_LY:44, CHO_PHE_DUYET:3, HOAN_THANH:16, TU_CHOI:6}` |

Bản ghi duy nhất mức "Sắp hết hạn" (đọc nguyên văn từ phản hồi):

```json
{"maVuViec":"VV-BTP-TW-20260713-001","tieuDe":"TKM test","trangThai":"DA_DANH_GIA",
 "mucDoCanhBao":"SAP_HET","deadline":"2026-08-03T09:47:32.881Z","ngayTiepNhan":"2026-07-13T09:47:32.881Z",
 "donViId":"00000000-0000-4000-8000-000000000001","tenLinhVuc":"Thuế","tenNguoiHoTro":"huongcg"}
```

⇒ **Tiền đề CÒN** (≥1 bản ghi). Không rơi vào nhánh "mất tiền đề → dừng báo lead".
`tabCounts` xác nhận bản ghi nằm ở tab **Hoàn thành**, **0** ở tab "Đang xử lý" ⇒ đúng cảnh báo của recon R1:
**đo ở tab mặc định sẽ ra 0 dòng**. Trên bản dựng V1.0.10 tab mặc định khi vào màn là **Tất cả (74)** —
vẫn ghi rõ để không ai suy ngược.

---

## 3. B1 — Vào màn bằng sidebar, xoá bộ lọc, chốt mốc chưa lọc

1. Click sidebar **"Vụ việc HTPL"** → URL thật `https://htpldn-uat.ospgroup.vn/vu-viec/danh-sach`.
2. Trạng thái ô lọc **khi vừa vào** (đo bằng bộ chọn đã cải chính `.ant-select-content-has-value` + `title`,
   **không** dùng `.ant-select-selection-item`): 5 ô lọc (Lĩnh vực PL · Đơn vị · Kênh tiếp nhận · Mức SLA · Trạng thái)
   **đều rỗng**; ô từ khoá rỗng; chỉ ô kích thước trang có giá trị `20 / trang`.
   ⇒ Không có bộ lọc sót từ màn trước (bẫy 3 không xảy ra), nhưng **vẫn bấm "Xóa bộ lọc"** theo trình tự bắt buộc.
3. Bấm **"Xóa bộ lọc"** → xác nhận lại:

| Mốc chưa lọc | Giá trị |
|---|---|
| Chân bảng nguyên văn | **`Hiển thị 1-20 / 74 kết quả`** |
| `meta.total` (máy chủ) | **74** |
| Đếm tay số dòng trên bảng | **20** (trang 1 của 4 trang) |
| Tab đang chọn | **Tất cả 74** |
| `tabCounts` trên UI | Tất cả 74 · Chờ tiếp nhận 5 · Đang xử lý 44 · Chờ phê duyệt 3 · Hoàn thành 16 · Từ chối 6 |

→ **3 nguồn khớp** (chân bảng · tổng máy chủ · đếm tay).

### T6 — Chip "Bộ lọc nâng cao (3)"

Mở chip ra đọc: chứa **3 tiêu chí** — 1 ô chọn **Trạng thái** (hiện `Tất cả` / `+ 0 ...` = **không chọn giá trị nào**)
và 2 ô ngày **`Từ ngày`** / **`Đến ngày`** (**cả hai trống**). Tổng vẫn **74** khi mở chip ⇒ chip `(3)` là **số ô có sẵn**,
**không phải** 3 điều kiện đang áp. Đã thu gọn chip lại cho giống trạng thái trong bằng chứng đối tác.

---

## 4. B2 — Đo vế chính: Mức SLA = "Sắp hết hạn"

### 4.1 Bộ bắt thông báo

Cài **đúng `output/UAT_doi-tac/tools/toast-capture.js`** (nguyên văn, không lọc trùng, đọc bằng `innerText`)
**TRƯỚC** khi bấm. Tự kiểm bằng node giả `NODE_TU_KIEM`:

```
lần đo 1: { soObserverDangSong: 1, hopLe: true }
lần đo 2: { soObserverDangSong: 1, hopLe: true }
```

⇒ Số liệu hợp lệ (nếu ≠ 1 thì toàn bộ số đếm vô hiệu).

### 4.2 Danh sách lựa chọn thật của ô "Mức SLA"

Mở ô lọc, đọc DOM dropdown → **đúng 4 lựa chọn**:

```
["Bình thường", "Sắp hết hạn", "Quá hạn", "Quá hạn nghiêm trọng"]
```

Khớp `srs-fr-05-vu-viec.md:1644` (4 giá trị hợp lệ của ô lọc Mức SLA).

### 4.3 Lần đo 1 — vào màn bằng bấm menu

Thao tác: chọn **"Sắp hết hạn"** trên ô lọc **Mức SLA** (thao tác trên giao diện, **không gõ tay địa chỉ**) →
xác nhận ô lọc hiển thị `Sắp hết hạn` → bấm **[Tìm kiếm]**.

| # | Số đo | Giá trị |
|---|---|---|
| 1 | **Số khung thông báo bắt được** | **0** — `SO_KHUNG_THONG_BAO = 0`, `chu = []`, `BI_LAP = false` |
| 2a | **HTTP của lời gọi danh sách** | **200** (`reqid=547`) |
| 2b | **Query thật màn gửi lên** | **`GET /api/v1/vu-viecs?mucSla=SAP_HET&page=1&pageSize=20`** |
| 2c | **Giá trị mức SLA màn gửi đi** | **`SAP_HET`** (giá trị hợp lệ). URL trình duyệt: `/vu-viec/danh-sach?mucSla=SAP_HET&page=1` |
| 3 | **Khung lỗi trên DOM** (rà `.ant-message-*`, `.ant-notification-*`, `.ant-alert-error`, `[role=alert]`, `.ant-form-item-explain-error`) | **[]** — không phần tử nào |
| 4a | Đếm tay số dòng trên bảng | **1** |
| 4b | Chân bảng nguyên văn | **`Hiển thị 1-1 / 1 kết quả`** |
| 4c | `meta.total` | **1** |
| 5 | Mã VV + nhãn cột *Cảnh báo thời hạn* | **`VV-BTP-TW-20260713-001`** · trạng thái `Đã đánh giá` · **`Sắp hết hạn`** ✔ đúng mức đã lọc |
| — | Tab đang đứng | **Tất cả 1** (tabs: Tất cả 1 · Chờ tiếp nhận – · Đang xử lý – · Chờ phê duyệt – · **Hoàn thành 1** · Từ chối –) |

> `SO_REQUEST` của bộ đo = 0 là **đúng thiết kế**: bộ đo cố ý bỏ qua GET; lời gọi danh sách là GET nên
> được đọc từ `list_network_requests` (mục 2a/2b), không phải từ bộ đếm ghi dữ liệu.

**Ảnh:** [`image/TKHSYCHTPL_03-01-loc-sap-het-han.png`](../image/TKHSYCHTPL_03-01-loc-sap-het-han.png) — **đã mở đọc**:
sidebar `HTPLDN · V1.0.10`; ô Mức SLA hiển thị `Sắp hết hạn`; tab `Tất cả 1` đang chọn, `Hoàn thành 1`;
1 dòng `VV-BTP-TW-20260713-001` / "TKM test tự động cập nhật địa chỉ" / Thuế / Trực tiếp / Đã đánh giá / huongcg;
chân bảng `Hiển thị 1-1 / 1 kết quả` + `20 / trang`; **không có khung thông báo lỗi nào trên màn**.

### 4.4 Lần đo 2 — sau `reload ignoreCache` (loại trừ tab chạy mã cũ)

`navigate_page type=reload ignoreCache=true` trên `?mucSla=SAP_HET&page=1`:
bản dựng vẫn `V1.0.10`; ô Mức SLA tự phục hồi `Sắp hết hạn`; **1 dòng**; `Hiển thị 1-1 / 1 kết quả`;
`khungLoi = []`. Rồi **cài lại bộ đo** (tự kiểm = 1) → bấm **"Xóa bộ lọc"** (về **74**, khớp mốc) →
**chọn lại "Sắp hết hạn" trên ô lọc** → bấm **[Tìm kiếm]**:

| Số đo | Lần 1 | Lần 2 |
|---|---|---|
| Số khung thông báo | **0** | **0** |
| Khung lỗi trên DOM | **[]** | **[]** |
| HTTP lời gọi danh sách | **200** (`reqid=547`) | **304 Not Modified** (`reqid=632`) — phản hồi thành công, không phải 4xx/5xx |
| Query thật | `mucSla=SAP_HET&page=1&pageSize=20` | `mucSla=SAP_HET&page=1&pageSize=20` |
| Đếm tay / chân bảng | 1 · `Hiển thị 1-1 / 1 kết quả` | 1 · `Hiển thị 1-1 / 1 kết quả` |
| Mã VV · nhãn cảnh báo | `VV-BTP-TW-20260713-001` · `Sắp hết hạn` | `VV-BTP-TW-20260713-001` · `Sắp hết hạn` |

⇒ **2 lần đo trong 2 lần tải trang khác nhau cho kết quả trùng khít** — loại trừ ngẫu nhiên.

---

## 5. B3 — Đo nốt 3 mức còn lại + phép thử tổng

Mỗi mức là một phép đo riêng, cùng cách: chọn giá trị trên ô lọc **Mức SLA** → bấm **[Tìm kiếm]**.
Cột "sai mức" = số dòng trên bảng có nhãn cột *Cảnh báo thời hạn* **không** thuộc mức đã lọc.

| Mức chọn trên giao diện | Query thật màn gửi lên | HTTP | Tổng bản ghi (chân bảng) | Dòng trang 1 | Dòng sai mức |
|---|---|---|---|---|---|
| Bình thường | `?mucSla=BINH_THUONG&page=1&pageSize=20` | **200** (`reqid=634`) | **29** — `Hiển thị 1-20 / 29 kết quả` | 20 | **0** |
| **Sắp hết hạn** | `?mucSla=SAP_HET&page=1&pageSize=20` | **200** / 304 | **1** — `Hiển thị 1-1 / 1 kết quả` | 1 | **0** |
| Quá hạn | `?mucSla=QUA_HAN&page=1&pageSize=20` | **200** (`reqid=636`) | **5** — `Hiển thị 1-5 / 5 kết quả` | 5 | **0** |
| Quá hạn nghiêm trọng | `?mucSla=QUA_HAN_NGHIEM_TRONG&page=1&pageSize=20` | **200** (`reqid=638`) | **39** — `Hiển thị 1-20 / 39 kết quả` | 20 | **0** |

**Số khung thông báo bắt được ở cả 4 mức: 0. Khung lỗi trên DOM ở cả 4 mức: [].**

### Phép thử tổng (bộ lọc phân hoạch đủ, không sót)

```
29 (Bình thường) + 1 (Sắp hết hạn) + 5 (Quá hạn) + 39 (Quá hạn nghiêm trọng) = 74
mốc chưa lọc                                                                 = 74   ✔ KHỚP
```

Đối chứng nhãn từng dòng (mẫu thật đọc từ bảng):
- Bình thường → `Bình thường · còn 11 ngày LV`, `… còn 9 ngày LV`, `Bình thường`, … (20/20 đúng mức)
- Quá hạn → `Quá hạn · 5 ngày LV`, `· 6 ngày LV`, `· 7 ngày LV`, `· 13 ngày LV` (5/5 đúng mức, **không lẫn**
  dòng "Quá hạn nghiêm trọng")
- Quá hạn nghiêm trọng → `Quá hạn nghiêm trọng · 38 / 39 / 18 / 52 ngày LV`, … (20/20 đúng mức)

---

## 6. B4 — Vế phân trang 20 bản ghi/trang

Đo trên **tập chưa lọc (74 bản ghi > 20)** sau khi bấm "Xóa bộ lọc".

| Số đo | Trang 1 | Trang 2 |
|---|---|---|
| Đếm tay số dòng | **20** | **20** |
| Chân bảng nguyên văn | **`Hiển thị 1-20 / 74 kết quả`** | **`Hiển thị 21-40 / 74 kết quả`** |
| Ô kích thước trang | **`20 / trang`** | `20 / trang` |
| Nút trang hiện có | `1` `2` `3` `4` | `1` `2` `3` `4`, đang chọn **`2`** |
| Tham số kích thước trang màn gửi lên | `pageSize=20` | URL `?page=2&pageSize=20` |
| **Số mã vụ việc trùng với trang 1** | — | **0** |

Mã trang 1 (20): `VV-BTP-TW-20260807-001` … `VV-BTP-TW-20260711-002`.
Mã trang 2 (20): `VV-BTP-TW-20260711-001` … `VV-QA-R9-DN-002`. **Giao nhau = ∅.**

**Ảnh:** [`image/TKHSYCHTPL_03-02-phan-trang.png`](../image/TKHSYCHTPL_03-02-phan-trang.png) — **đã mở đọc**:
chân bảng `Hiển thị 21-40 / 74 kết quả`, nút trang `1 [2] 3 4` với **2 đang được chọn**, ô `20 / trang`,
bảng hiện các mã `VV-HDSD-003`, `VV-HDSD-TVV-001`, `VV-HDSD-002`, `VV-BTP-TW-20260512-001`, `VV-QA-R9-*`
— **không mã nào trùng trang 1**.

---

## 7. B5 — Bảng điều khiển trình duyệt

`list_console_messages` (error + warn, gồm cả bản ghi được giữ lại):

```
1 cảnh báo: Route path "/ticket=*" will be treated as if it were "/ticket=/*" … [5 times]
0 lỗi
```

⇒ **0 lỗi**; cảnh báo duy nhất là về khai báo tuyến đường của khung React, **không liên quan** case.

---

## 8. Mô tả bằng chứng video của đối tác (đã mở xem)

Tệp: `output/UAT_doi-tac/reverify-week-2/verify1-conlai-2026-08-03/partner-evidence/TKHSYCHTPL_03.webm`
(21 khung đã trích sẵn tại `frames/TKHSYCHTPL_03/`, bước ~0,5 s; công cụ `tools/extract_frames.py`).
Đồng hồ máy trong video: **09:08 AM · 2026-07-30**. Chân sidebar: **`HTPLDN · V1.0.2`**.
Góc phải: `BTP · TW` · `Cán bộ NV Trung ương` · huy hiệu `CB_NV_TW` — **trùng khít vai trò QA dùng để đo lại**.

| Khung | Nội dung đọc được |
|---|---|
| `t002.07s.jpg` | Địa chỉ còn là `/vu-viec/danh-sach` (chưa lọc). Ô **Mức SLA đã chọn "Sắp hết hạn"**, con trỏ đang trên nút **[Tìm kiếm]**. Tab **Tất cả 56** đang chọn (Chờ tiếp nhận – · Đang xử lý 35 · Chờ phê duyệt 2 · Hoàn thành 14 · Từ chối 5). Bảng **đang có dữ liệu**, trong đó nhìn thấy `VV-BTP-TW-20260713-001` (Hoàn thành, huongcg, 13/07→03/08) và 2 dòng gắn nhãn **`Sắp hết hạn · còn 1 ngày LV`** ⇒ **thời điểm đó dữ liệu mức "Sắp hết hạn" CÓ tồn tại**. |
| `t004.63s.jpg` → `t008.07s.jpg` | Sau khi bấm Tìm kiếm: địa chỉ đổi thành **`/vu-viec/danh-sach?mucSla=SAP_HET_HAN&page=1`**; xuất hiện **khung thông báo lỗi nền trắng viền đỏ, dấu ✖ đỏ**, nguyên văn: **`mucSla must be one of the following values: BINH_THUONG, SAP_HET, QUA_HAN, QUA_HAN_NGHIEM_TRONG`**; vùng dữ liệu về **rỗng** kèm icon trống + dòng **"Không tìm thấy hồ sơ phù hợp"**; các đếm số trên 6 tab **biến mất hết**. Khung lỗi còn nguyên đến hết video (~8,1 s). |

**Nguyên nhân cũ đọc được từ video:** màn hình gửi lên máy chủ **một giá trị mức SLA không nằm trong tập
hợp lệ** (`SAP_HET_HAN`), máy chủ từ chối và màn hiện thông báo lỗi. Bảng rỗng chỉ là **hệ quả**, không phải
triệu chứng chính.

**Đối chiếu với lượt đo hôm nay:** trên `V1.0.10`, cùng thao tác đó, màn gửi lên **`SAP_HET`** — đúng giá trị
nằm trong tập hợp lệ mà chính thông báo lỗi cũ liệt kê ⇒ nguyên nhân gốc đã hết. (Ghi theo **hành vi quan sát
được**, không kê đơn cách hiện thực.)

---

## 9. Đối chiếu đặc tả — đã **mở file đọc số dòng thật**

Nguồn chuẩn: `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/`.

| Vế | `file:dòng` | Nguyên văn |
|---|---|---|
| S1 | `srs-fr-05-vu-viec.md:1644` | `\| 9 \| filter-bar \| Mức SLA \| C10 dropdown \| BINH_THUONG / SAP_HET / QUA_HAN / QUA_HAN_NGHIEM_TRONG \| change → filter \| Luôn \|` |
| S1 | `srs-fr-05-vu-viec.md:1516` | `` \| `SAP_HET` \| Sắp hết hạn \| Vàng \| `` |
| S1 | `srs-fr-05-vu-viec.md:692` | `\| E1 \| Không có kết quả \| INF-VV-TK-01 \| "Không tìm thấy hồ sơ phù hợp" \| INFO \|` |
| S1 | `srs-fr-05-vu-viec.md:693` | `\| E2 \| tu_ngay > den_ngay \| ERR-VV-TK-01 \| "Ngày bắt đầu phải trước ngày kết thúc" \| ERROR \|` |
| S2 | `srs-fr-05-vu-viec.md:697` | `- **Given** CB NV lọc theo lĩnh vực/trạng thái/thời gian **When** áp dụng **Then** kết quả lọc` |
| S2 | `srs-fr-05-vu-viec.md:2031` | `\| muc_do_canh_bao \| text \| N \| CHECK IN ('BINH_THUONG','SAP_HET','QUA_HAN','QUA_HAN_NGHIEM_TRONG') \| 'BINH_THUONG' \| Mức cảnh báo SLA \|` |
| S3 | `srs-fr-05-vu-viec.md:668` | `\| 4 \| Phân trang (20/trang) \| BR-DATA-07 \|` |
| S3 | `srs-fr-05-vu-viec.md:1659` | `\| 24 \| pagination \| Phân trang \| C05 \| "Hiển thị 1-20 / N kết quả". Mặc định 20/trang \| click → chuyển trang \| Luôn \|` |
| S3 | `srs-v3.5.md:5571` | `\| BR-DATA-07 \| **Pagination:** Mọi danh sách sử dụng phân trang. Default: 20 rows/page, max: 100 rows/page \| …` |
| Vai trò | `srs-fr-05-vu-viec.md:94` | `**Tác nhân:** CB NV (TW/BN/ĐP)` |
| Phạm vi | `srs-fr-05-vu-viec.md:2450` | `Cán bộ TW xem được toàn bộ dữ liệu. Cán bộ BN/ĐP chỉ xem dữ liệu thuộc đơn vị mình…` |

**Bảng lỗi của FR-V.I-08 (`:690–693`) chỉ có đúng 2 dòng** — không có điều kiện lỗi nào cho việc chọn một
giá trị hợp lệ ở ô Mức SLA. Lượt đo hôm nay: **0 khung thông báo lỗi** ⇒ hết mâu thuẫn với đặc tả.

---

## 10. Chốt theo bảng chuẩn chấm §6 / §8

| Vế | Tiêu chí Pass đã cam kết trước khi đo | Số đo thật | Kết |
|---|---|---|---|
| **S1** | 0 khung thông báo lỗi khi chọn "Sắp hết hạn"; lời gọi danh sách trả mã thành công | **0 khung** (2 lần đo, 2 lần tải trang) · HTTP **200 / 304** · **[]** khung lỗi trên DOM | ✅ **ĐẠT** |
| **S2** | Bảng hiện ≥1 bản ghi, khớp tổng máy chủ, **mọi** bản ghi đúng mức "Sắp hết hạn"; tổng 4 nhóm = mốc chưa lọc | 1 dòng = `meta.total` 1; nhãn `Sắp hết hạn`; **29+1+5+39 = 74 = 74** | ✅ **ĐẠT** |
| **S3** | Kích thước trang mặc định = 20 ở cả điều khiển phân trang lẫn lời gọi danh sách; >20 bản ghi thì trang 1 đúng 20 dòng và chuyển trang được | `20 / trang` · `pageSize=20` · trang 1 = 20 dòng · trang 2 = 20 dòng, `Hiển thị 21-40 / 74`, **0 mã trùng** | ✅ **ĐẠT** |

**Bẫy đã chủ động loại trừ:** (a) không nhầm danh sách rỗng với báo lỗi — màn có dữ liệu thật · (b) tiền đề
được đếm lại ngay trước khi đo, không Pass trên tập rỗng · (c) **không** gõ tay địa chỉ cũ `?mucSla=SAP_HET_HAN`;
toàn bộ đo bằng thao tác chọn trên ô lọc · (d) chip "Bộ lọc nâng cao (3)" đã mở ra khai · (e) S3 đo bằng
kích thước trang mặc định trên tập 74, không đo trên tập 1 bản ghi · (h) chạy đủ **baseline + 4 giá trị** và
kiểm phép cộng · (i) đối chứng nhãn cảnh báo **từng dòng** · (j) bộ đo cài trước khi bấm, tự kiểm = 1 ·
(k) lặp lại sau `reload ignoreCache` · (l) giao diện và dữ liệu trả về **không** mâu thuẫn.

⇒ **VERDICT: ✅ Pass** (S1 + S2 + S3 đều đạt; không có "fix một phần").

---

## 11. Ghi nhận cho BA (không chặn bàn giao, không ảnh hưởng verdict)

**Đặc tả tự lệch tên mức cảnh báo giữa các mục** — bẫy (f) của chuẩn chấm, đã xác minh bằng cách mở file:

| `file:dòng` | Dùng mã | Dùng nhãn |
|---|---|---|
| `srs-fr-05-vu-viec.md:1516` · `:1644` · `:1656` · `:2031` | **`SAP_HET`** | "Sắp hết hạn" · "Bình thường" |
| `srs-fr-05-vu-viec.md:1449` | **`SAP_HET_HAN`** | — |
| `srs-v3.5.md:5626` (BR-SLA-02) | **`SAP_HET_HAN`** | đổi nhãn `BINH_THUONG` → **"Trong hạn"** (chốt 2026-05-04) |

Hai điểm lệch: (1) **tên mã** của mức "Sắp hết hạn" khác nhau giữa các mục; (2) **nhãn hiển thị** của mức thấp
nhất — quy tắc nghiệp vụ nói "Trong hạn", bảng ánh xạ màn hình nói "Bình thường"; giao diện hiện đang hiển thị
"Bình thường". Đề nghị BA thống nhất lại một bản. **Không ảnh hưởng kết quả case này** — chuẩn chấm của vế S1
là **hành vi nghiệp vụ** ("chọn 'Sắp hết hạn' phải ra danh sách, không báo lỗi"), không phải giá trị mã mà
giao diện gửi lên.

**Quan sát phụ (chỉ ghi, không đề nghị):** bảng *Inputs* của FR-V.I-08 (`srs-fr-05-vu-viec.md:651–659`) liệt
kê 7 tiêu chí tìm kiếm và **không có** tiêu chí mức SLA, trong khi ô lọc này được quy định ở phần màn hình
`:1644`. Đây là khác biệt giữa 2 mục của cùng bộ đặc tả, không phải lỗi phần mềm.

---

## 12. Tác động lên dữ liệu

Toàn bộ lượt đo **chỉ đọc** (lọc + phân trang). **Không tạo / sửa / xoá** bản ghi nghiệp vụ nào.
Không đăng nhập thêm lượt nào (dùng phiên `cbnv_tw` có sẵn).

---

## 13. Ảnh bằng chứng

| Tệp | Nội dung | Đã mở đọc |
|---|---|---|
| `image/TKHSYCHTPL_03-01-loc-sap-het-han.png` | Màn sau khi lọc Mức SLA = "Sắp hết hạn": bản dựng V1.0.10, tab Tất cả 1, 1 dòng đúng mức, `Hiển thị 1-1 / 1 kết quả`, **không có khung lỗi** | ✅ |
| `image/TKHSYCHTPL_03-02-phan-trang.png` | Trang 2 của tập chưa lọc: `Hiển thị 21-40 / 74 kết quả`, nút trang `1 [2] 3 4`, `20 / trang` | ✅ |
