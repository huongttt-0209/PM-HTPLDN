# GIAI ĐOẠN B — số đo thô · `QLHSPLDN_11` (tab `bug`, dòng 293 — "Tìm kiếm hồ sơ pháp lý có kết quả")

```
Lô:            F9 — tái xác nhận trên env NGHIỆM THU của đối tác
Flow:          flows/03-reverify-sau-dev-fix.md — NHÁNH 2 "Tái xác nhận trên môi trường khác"
Nguồn chuẩn:   chuan/QLHSPLDN_11.md (Giai đoạn A đã khoá) — làm đúng theo, không tự thêm/bớt vế
Env đo:        https://htpldn-uat.ospgroup.vn  (env nghiệm thu của đối tác)
Người đo:      agent ĐO · 2026-08-07 · phiên 14:14 → 14:20 giờ VN
```

---

## 1. Vân tay bản dựng — ĐẦU và CUỐI case

| Hạng mục | ĐẦU case — **14:14:55 VN 07/08** | CUỐI case — **14:20:02 VN 07/08** |
|---|---|---|
| Bó mã JS (máy chủ đang phát) | `assets/index-D4NhKEjr.js` | `assets/index-D4NhKEjr.js` |
| Bó mã CSS | `assets/index-DVlgOkLg.css` | `assets/index-DVlgOkLg.css` |
| `GET /` `last-modified` | `Fri, 07 Aug 2026 04:17:55 GMT` (= 11:17 VN) | `Fri, 07 Aug 2026 04:17:55 GMT` |
| `GET /` `etag` | `W/"6a755c73-428"` | `W/"6a755c73-428"` |
| Máy chủ web | `nginx` | `nginx` |
| Chuỗi chân sidebar | `HTPLDN · V1.0.10` | `HTPLDN · V1.0.10` |

> ✅ **Hai đầu TRÙNG KHỚP tuyệt đối** ⇒ **không có deploy chen giữa case** ⇒ không phải khai quan sát nào rơi
> trước/sau mốc deploy. Trùng luôn với vân tay hai case `_06` / `_07` đo trước đó cùng phiên.
>
> ✅ **Đã loại trừ bẫy "tab mở lâu vẫn chạy mã cũ" mà KHÔNG cần tải lại trang:** đọc trực tiếp thẻ script đang
> nạp trong tab — `document.querySelectorAll('script[src]')` trả đúng **`/assets/index-D4NhKEjr.js`**, trùng khít
> bó mã máy chủ đang phát ở cả hai đầu. Tên tệp bó mã có băm nội dung ⇒ **mã đang chạy trong tab CHÍNH LÀ bản
> dựng hiện hành**. (Không tải lại trang để khỏi tiêu thêm lượt đăng nhập/mã xác thực — giới hạn 5 lượt/60s.)
>
> ⚠️ Ghi chú nhỏ: `etag` đọc được có tiền tố yếu `W/`; giá trị `"6a755c73-428"` **y hệt** brief. Khác biệt chỉ do
> cách đọc header, **không** phải đổi bản dựng — `last-modified` và bó mã đều không đổi.

---

## 2. Tài khoản thực dùng + xác nhận vai trò

| Hạng mục | Giá trị |
|---|---|
| Tài khoản | **`cbnv_tw`** (đúng tài khoản chỉ định, **không** phải fallback) |
| Cách vào phiên | **Dùng lại phiên đang sống** của hai case trước cùng lô — kiểm sống bằng `GET /api/v1/auth/me` → **200** |
| Số lượt đăng nhập phát sinh trong case này | **0** — không chạm giới hạn 5 lượt/60s |
| `hoTen` | `Cán bộ NV Trung ương` |
| `vaiTro` | `["CB_NV_TW"]` |
| `capDonVi` | `TW` |
| `donViId` | `00000000-0000-4000-8000-000000000001` (= *Cục Bổ trợ tư pháp - Bộ Tư pháp*) |
| Badge trên màn | `Cán bộ NV Trung ương · Cán bộ Nghiệp vụ Trung ương` · phạm vi `BTP · TW` |

⇒ Khớp đúng vai trò/cấp đọc được trên bằng chứng của đối tác, và đúng tác nhân `srs-fr-12:565`.
**Không dùng `admin` ở bất kỳ bước nào.**

---

## 3. Bản ghi đã đọc / đã tạo / đã đổi

| Hạng mục | Số lượng |
|---|---|
| Bản ghi **TẠO MỚI** | **0** |
| Bản ghi **SỬA / XOÁ** | **0** |
| Bản ghi chỉ **ĐỌC** | 1 DN + 4 hồ sơ pháp lý (liệt kê dưới) |

Case này **chỉ đọc** (tìm kiếm / lọc) ⇒ đúng ưu tiên tuyệt đối của nguồn chuẩn §5: **không seed gì**.

**Doanh nghiệp đo — chọn đúng DN trong bằng chứng của đối tác:**

| Mã DN | id trên URL | Vì sao chọn |
|---|---|---|
| **`DN-XX-0005`** — *Công ty TNHH Mẫu Test* | `1a715c55-bc31-46de-ae07-56dd4f403ce5` | Đúng DN đối tác chụp trong bằng chứng ⇒ đo ngay trên **chính màn họ báo lỗi**. Có **4 hồ sơ** đủ đa dạng loại × trạng thái để bộ lọc cắt được tập con thật. Ưu tiên 1 của nguồn chuẩn §5. |

**4 hồ sơ pháp lý của DN đó — CHỈ ĐỌC, không đụng gì:**

| Mã hồ sơ | Tên hồ sơ | Loại | Trạng thái | Thao tác đã làm | Thao tác KHÔNG làm |
|---|---|---|---|---|---|
| `HSPL-20260804-0001` | QA-HSPL-V2-0408-742199 DA SUA vong 2 | Quyết định | Hết hạn | đọc trên bảng, làm dữ liệu đối chiếu lọc | ❌ không bấm Xem/Sửa/Xoá |
| `HSPL-20260803-0002` | Hồ sơ pháp lý doanh nghiệp XXX | Hợp đồng | Hiệu lực | như trên | ❌ không bấm Xem/Sửa/Xoá |
| `HSPL-20260803-0001` | TKM hồ sơ pháp lý số 1 | Khác | Hiệu lực | như trên | ❌ không bấm Xem/Sửa/Xoá |
| `HSPL-20260731-0002` | Ho so x - SUA CU v2 742199 | Giấy chứng nhận | Hiệu lực | như trên | ❌ không bấm Xem/Sửa/Xoá |

> 🔴 **Tuân thủ kỷ luật dữ liệu §4 brief:** `DN-XX-0005`, `HSPL-20260803-0001`, `HSPL-20260731-0002` và mọi bản ghi
> khác **không bị sửa, không bị xoá, không bị thêm hồ sơ nào**. Toàn bộ case chỉ phát sinh **3 lệnh `GET`**.
> Không đụng DN QA `DN-HCM-0004` (không cần tới — `DN-XX-0005` đã đủ dữ liệu).

**Đường UI đã đi — đúng 4 bước của phiếu, KHÔNG gõ thẳng URL:**
menu trái **Doanh nghiệp** → nút mở chi tiết (👁) trên hàng `DN-XX-0005` ở màn danh sách → thẻ **Hồ sơ pháp lý**
→ nhập từ khóa / chọn bộ lọc → bấm **[Tìm kiếm]**.

---

## 4. Số đo thô

### 4.0 — Nền so sánh (baseline TRƯỚC khi lọc) · 14:16:23 VN

Bắt buộc theo nguồn chuẩn §4 mục 1: không có mốc này thì "bảng đổi" không chứng minh được gì.

| Nguồn | Số hàng | Danh sách mã |
|---|---|---|
| **Bảng trên màn** (đếm `tr.ant-table-row`) | **4** | `HSPL-20260804-0001` · `HSPL-20260803-0002` · `HSPL-20260803-0001` · `HSPL-20260731-0002` |
| **Phản hồi máy chủ** `GET /api/v1/ho-so-phap-ly-dns?doanhNghiepId=1a715c55-…&pageSize=100` → **200** | `meta.total` = **4**, `data[]` = **4** | cùng 4 mã, **cùng thứ tự** |

**Bảng dữ liệu đầy đủ của nền so sánh** (dùng để tính trước kết quả đúng của từng phép lọc):

| # | Mã hồ sơ | Loại (`loaiHoSo`) | Trạng thái (`trangThai`) | Mã có chứa `202608`? |
|---|---|---|---|---|
| 1 | `HSPL-20260804-0001` | Quyết định (`QUYET_DINH`) | Hết hạn (`HET_HAN`) | ✅ có |
| 2 | `HSPL-20260803-0002` | Hợp đồng (`HOP_DONG`) | Hiệu lực (`HIEU_LUC`) | ✅ có |
| 3 | `HSPL-20260803-0001` | Khác (`KHAC`) | Hiệu lực (`HIEU_LUC`) | ✅ có |
| 4 | `HSPL-20260731-0002` | Giấy chứng nhận (`GIAY_CN`) | Hiệu lực (`HIEU_LUC`) | ❌ **không** |

**Từ khóa chọn = `202608`** — lấy đúng theo quy tắc nguồn chuẩn §5 ("đọc bảng TRƯỚC, rồi lấy chuỗi con của mã hồ sơ
đọc được từ chính bảng"): là chuỗi con của **mã hồ sơ** 3 dòng đầu và **không** khớp dòng 4.
Đã kiểm chéo: chuỗi `202608` **không** xuất hiện trong *tên hồ sơ* của bất kỳ dòng nào, cũng không trong tên DN
⇒ tập đúng phải là **đúng 3 dòng**. Căn cứ hợp lệ: `srs-fr-12:593` — keyword "Tìm theo **mã HS**, tên DN, tên HS".

Thẻ hiện đủ **5 ô lọc** đúng `srs-fr-12:589-597`: ô từ khóa · *Loại hồ sơ* · *Trạng thái* · *Từ ngày* · *Đến ngày*
(ô chọn *Doanh nghiệp* bị ràng buộc bởi ngữ cảnh URL — theo nguồn chuẩn §6 **không** được chấm lỗi).
Ba giá trị đọc được của ô *Trạng thái* là `Hiệu lực / Hết hạn / Thu hồi`, khớp đúng enum `srs-fr-12:597`.

---

### 4.1 — BIẾN THỂ (a) · tìm theo TỪ KHÓA · 14:18:07 VN

*(nguồn: `srs-fr-12:710` "Given CB NV tìm kiếm theo từ khóa … Then kết quả matching" + ô phiếu "nhập từ khóa")*

**Thao tác bằng UI thật:** gõ `202608` vào ô *Tìm theo mã hoặc tên hồ sơ* → bấm nút **[Tìm kiếm]**.

Kiểm bẫy dụng cụ trước khi bấm (nguồn chuẩn §4 mục 2 — vòng trước đã gãy vì ô bị **nối chuỗi**):

| Kiểm | Kết quả |
|---|---|
| Giá trị ô sau khi điền | `"202608"` — **độ dài 6**, đúng nguyên chuỗi, **không bị nối** vào giá trị cũ |
| Có lệnh tìm nào tự bắn lúc gõ không? | **Không** — 0 request. Lệnh chỉ phát khi bấm **[Tìm kiếm]** |

**Số đo:**

| Hạng mục | Số đo |
|---|---|
| Số hàng bảng **trước** lọc | **4** |
| Số hàng bảng **sau** lọc | **3** |
| Lệnh máy chủ phát ra bởi CHÍNH cú bấm | `GET /api/v1/ho-so-phap-ly-dns?doanhNghiepId=1a715c55-…&**keyword=202608**&pageSize=100` → **200** |
| Tham số lọc có mặt thật trong lệnh gửi lên? | ✅ **có** — `keyword=202608` |
| `meta.total` máy chủ trả | **3** |
| `data[]` máy chủ trả | `HSPL-20260804-0001` · `HSPL-20260803-0002` · `HSPL-20260803-0001` |
| Danh sách mã **trên bảng** | `HSPL-20260804-0001` · `HSPL-20260803-0002` · `HSPL-20260803-0001` |
| Bảng ↔ phản hồi máy chủ | ✅ **trùng khít** cả **số dòng (3 = 3)** lẫn **danh sách mã** lẫn **thứ tự** |
| Dòng bị loại | `HSPL-20260731-0002` — **đúng** dòng duy nhất có mã không chứa `202608` |
| Thông báo lỗi (`MutationObserver`, `innerText`, không dedupe) | **0** |
| Lỗi bảng điều khiển | **0** |

⇒ **Biến thể (a) ĐẠT.** Bảng cắt thật **4 → 3**, lọc chạy **phía máy chủ** (tham số đi kèm lệnh, `total` do máy chủ
tính), không phải cắt phía trình duyệt.

---

### 4.2 — BIẾN THỂ (b) · KẾT HỢP ≥2 điều kiện, kiểm logic VÀ · 14:19:20 VN

*(nguồn: `srs-fr-12:711` "Given CB NV **kết hợp nhiều điều kiện** … Then kết quả AND logic" + `:643` "Áp dụng tất cả
bộ lọc" + `:644` "**AND logic** cho tất cả điều kiện" + ô phiếu "và/hoặc chọn bộ lọc")*

> 🔴 Đây chính là biến thể vòng F4 (env nội bộ) **đã bỏ sót** khiến case bị chấm Pass non. Lượt này chạy đủ.

**Thao tác bằng UI thật:** **giữ nguyên** từ khóa `202608` → mở ô chọn *Trạng thái* → chọn **`Hiệu lực`** →
bấm **[Tìm kiếm]**.

| Kiểm trước khi bấm | Kết quả |
|---|---|
| Từ khóa còn nguyên? | ✅ `"202608"` |
| Ô chọn hiển thị gì (đọc `.ant-select-content`)? | `Loại hồ sơ` (chưa chọn) · **`Hiệu lực`** (đã chọn) |
| Chỉ chọn ô lọc thôi có tự bắn lệnh tìm không? | **Không** — 0 request |

**Kết quả đúng phải ra là bao nhiêu — tính trước từ bảng nền §4.0:**

| Giả thuyết hệ thống xử lý thế nào | Tập kết quả | Số dòng |
|---|---|---|
| Chỉ áp **từ khóa**, bỏ bộ lọc | {1, 2, 3} | 3 |
| Chỉ áp **bộ lọc**, bỏ từ khóa | {2, 3, 4} | 3 |
| **HOẶC** (OR — sai spec) | {1, 2, 3, 4} | 4 |
| ✅ **VÀ** (AND — đúng `:644`) | **{2, 3}** | **2** |

⇒ Bốn giả thuyết cho **bốn con số khác nhau** (3 · 3 · 4 · **2**) ⇒ chỉ cần đọc số dòng + danh sách mã là **phân
biệt dứt khoát** được, không cần chạy thêm lượt lọc-đơn nào.

**Số đo:**

| Hạng mục | Số đo |
|---|---|
| Số hàng bảng **trước** (kết quả lượt a) | **3** |
| Số hàng bảng **sau** | **2** |
| Lệnh máy chủ phát ra bởi CHÍNH cú bấm | `GET /api/v1/ho-so-phap-ly-dns?doanhNghiepId=1a715c55-…&**keyword=202608**&**trangThai=HIEU_LUC**&pageSize=100` → **200** |
| **CẢ HAI** tham số lọc có mặt thật trong lệnh gửi lên? | ✅ **có** — `keyword=202608` **và** `trangThai=HIEU_LUC` |
| `meta.total` máy chủ trả | **2** |
| `data[]` máy chủ trả | `HSPL-20260803-0002` · `HSPL-20260803-0001` (cả hai `trangThai: "HIEU_LUC"`) |
| Danh sách mã **trên bảng** | `HSPL-20260803-0002` · `HSPL-20260803-0001` |
| Bảng ↔ phản hồi máy chủ | ✅ **trùng khít** số dòng (2 = 2) + danh sách mã + thứ tự |
| Là **tập con** của lượt (a)? | ✅ {2, 3} ⊂ {1, 2, 3} |
| Đúng **giao** của 2 điều kiện? | ✅ **đúng 2 dòng = giao**. Không phải 3 (bỏ 1 điều kiện), không phải 4 (OR) |
| Dòng bị loại thêm so với lượt (a) | `HSPL-20260804-0001` — **đúng** dòng *Hết hạn*, không thoả bộ lọc thứ hai |
| Thông báo lỗi | **0** |
| Lỗi bảng điều khiển | **0** |

⇒ **Biến thể (b) ĐẠT.** Hệ thống áp **đồng thời** cả hai điều kiện theo đúng **logic VÀ** (`:644`, `:711`).

---

### 4.3 — Tổng hợp 3 phép đo (toàn bộ lệnh máy chủ của case)

| # | Điều kiện lọc | Lệnh gửi lên (tham số) | HTTP | `meta.total` | Số hàng bảng | Khớp? |
|---|---|---|---|---|---|---|
| 0 | *(không lọc — nền so sánh)* | `doanhNghiepId` | 200 | **4** | **4** | ✅ |
| a | từ khóa | `doanhNghiepId` + **`keyword`** | 200 | **3** | **3** | ✅ |
| b | từ khóa **VÀ** trạng thái | `doanhNghiepId` + **`keyword`** + **`trangThai`** | 200 | **2** | **2** | ✅ |

Dãy **4 → 3 → 2** thu hẹp đúng theo từng điều kiện cộng thêm. **0 lệnh 4xx/5xx** trong cả case.

---

## 5. Artifact quyết định verdict

Tất cả ở `F9-uatdoitac-QLHSPLDN-2026-08-07/image/`. Mỗi ảnh **đã được mở ra đọc bằng mắt**, không kết luận bằng
script chạy trong trang.

| Ảnh | Thấy gì trong ảnh |
|---|---|
| `11-A-baseline-DN-XX-0005-4hang-truoc-loc.png` | **Nền so sánh trên chính DN của đối tác.** Tiêu đề `Chi tiết DN #DN-XX-0005`, thẻ *Hồ sơ pháp lý* đang mở. Thanh lọc hiện **đủ 5 ô**: ô từ khóa *"Tìm theo mã hoặc tên hồ sơ"* (đang **trống**) · *Loại hồ sơ* · *Trạng thái* · *Từ ngày* · *Đến ngày*, kèm 3 nút *Tìm kiếm* · *Xóa bộ lọc* · *Xuất Excel*. Bảng đếm được **4 hàng**: `HSPL-20260804-0001` · `HSPL-20260803-0002` · `HSPL-20260803-0001` · `HSPL-20260731-0002`. |
| `11-B-luot-a-tukhoa-202608-3hang.png` | **Lượt (a).** Ô từ khóa hiện đúng chuỗi **`202608`** (kèm nút xoá ⊗, không bị nối chuỗi); hai ô chọn vẫn ở trạng thái chưa chọn (*Loại hồ sơ* / *Trạng thái* xám mờ). Bảng còn **3 hàng** — `HSPL-20260804-0001`, `HSPL-20260803-0002`, `HSPL-20260803-0001`; hàng `HSPL-20260731-0002` **đã biến mất**. |
| `11-C-luot-b-tukhoa-202608-VA-trangthai-HieuLuc-2hang.png` | **Lượt (b) — bằng chứng logic VÀ.** Ô từ khóa **vẫn giữ `202608`** *và* ô *Trạng thái* nay hiện **`Hiệu lực`** (chữ đậm, đã chọn) — hai điều kiện cùng lúc trên một màn. Bảng còn **2 hàng**: `HSPL-20260803-0002` (Hợp đồng) và `HSPL-20260803-0001` (Khác), cả hai đều *Hiệu lực*. Hàng `HSPL-20260804-0001` (*Hết hạn*) **đã rụng**, hàng `HSPL-20260731-0002` vẫn không có ⇒ nhìn bằng mắt cũng thấy đúng **giao** của hai điều kiện, không phải hợp. |

---

## 6. Verdict

# 📌 **Pass** — HIỆN TẠI ĐẠT

**Bám luật Flow 03 §Chốt (bảng Verdict logic), dòng "Pass":**

1. **Mọi vế đều `MATCH` và đều đạt.** Ba vế con của nguồn chuẩn — **C1a** thẻ có ô từ khóa + bộ lọc · **C1b** bấm
   tìm ra đúng danh sách kết quả · **C1c** đúng thẻ đang tranh chấp — đều đo được và đều đạt. Không vế nào FAIL.
   Triệu chứng đối tác báo (*"Không có trường thông tin tìm kiếm trên màn hình"*) **không tái hiện**: thẻ hiện đủ
   **5 ô lọc** đúng `srs-fr-12:589-597`.
2. **Đã chạy HẾT biến thể bắt buộc — đủ 2/2.** (a) tìm theo từ khóa (`:710`) **và** (b) kết hợp ≥2 điều kiện cho
   kết quả logic VÀ (`:711` + `:644`). **Đây là điểm vòng trước bỏ sót**; lượt này đã đóng.
3. **Đủ 6 điều kiện PASS của nguồn chuẩn §6:** ① có ô + nút bấm được · ② lượt (a) ra đúng tập con ≥1 dòng ·
   ③ lượt (b) đúng giao 2 điều kiện · ④ cả 2 lượt `total` = số dòng bảng **và** danh sách mã trùng khít ·
   ⑤ tham số lọc có mặt thật trong lệnh gửi lên · ⑥ vân tay bản dựng đầu = cuối.
4. **Có đối chứng độc lập cho mọi quan sát quyết định.** Với **từng** lượt, đọc **phản hồi máy chủ của chính lệnh
   tìm đó** (`meta.total` + `data[].maHoSo`) rồi đối chiếu với bảng đang hiển thị — đúng phương pháp Flow 03
   §Chạy.3 ("hiển thị → đối chiếu dữ liệu nguồn"). **Không** dùng cách bấm lại cùng nút làm đối chứng.
5. **Không Pass bằng quan sát tĩnh.** Không dừng ở việc "thấy ô tìm kiếm đã có": đã **gõ từ khóa thật, bấm nút
   thật**, bảng **đổi thật** (4 → 3 → 2), và mỗi lần đều mở phản hồi máy chủ ra đối chiếu. Đã **chụp ảnh và mở ảnh
   đọc bằng mắt** cho cả ba trạng thái.
6. **Đã loại trừ khả năng "fix UI mà máy chủ vẫn hỏng".** Tham số `keyword` / `trangThai` **thật sự đi kèm lệnh gửi
   lên**, `total` do **máy chủ** tính, và số dòng thu hẹp đúng ⇒ lọc chạy **phía máy chủ**, không phải trình duyệt
   tự cắt bảng.
7. **Logic VÀ được chứng minh dứt khoát, không suy đoán.** Bốn cách xử lý khả dĩ cho bốn con số khác nhau
   (3 · 3 · 4 · **2**); số đo được là **2** ⇒ chỉ khớp **duy nhất** phương án giao (AND).

**Giới hạn hiệu lực (bắt buộc ghi):** Pass này **chỉ có hiệu lực trên env `https://htpldn-uat.ospgroup.vn`**, bản
dựng `assets/index-D4NhKEjr.js` · `last-modified Fri, 07 Aug 2026 04:17:55 GMT`, đo lúc **14:14→14:20 giờ VN
07/08/2026**, với vai trò **`CB_NV_TW`**, trên **`DN-XX-0005`** (chính DN trong bằng chứng của đối tác).

**Không viết "fix đã có tác dụng":** phiên này không có bằng chứng trạng thái trước fix trên chính env/bản dựng
này ⇒ chỉ kết luận **hiện trạng ĐẠT so với SRS + expected gốc**, dùng chữ *HIỆN TẠI ĐẠT*.

**Ghi ô Drive theo mapping §7 brief:** `Trạng thái dev fix` = **`UAT done`**.
*(Chưa ghi — dừng chờ điều phối theo yêu cầu prompt.)*

---

## 7. Bug mới / candidate

**Không có bug mới, không có candidate.**

Cả case chỉ phát sinh **3 lệnh `GET`**, tất cả **200**, **0 thông báo lỗi**, **0 lỗi bảng điều khiển**.
Không dùng tới lượt xác nhận bổ sung nào (hạn mức 1 phép/case vẫn còn nguyên).

### Ghi nhận không thành candidate

- **Khung "Không tìm thấy hồ sơ pháp lý phù hợp" chớp qua giữa hai lần vẽ bảng.** Bộ quan sát bắt được nút này lúc
  `07:18:07.597Z`, rồi các hàng dữ liệu xuất hiện lúc `07:18:07.650Z` — **cách nhau 53 mili-giây**. Đây là khung
  vẽ trung gian của bảng khi tráo dữ liệu, **không phải trạng thái cuối** (trạng thái cuối có đủ 3 hàng, đã chụp
  ảnh xác nhận) và không kịp hiện ra cho người dùng thấy. **Không phải lỗi.**
- **Thẻ không có ô chọn *Doanh nghiệp*** dù `srs-fr-12:595` có liệt kê `doanh_nghiep_id`. Nguồn chuẩn §6 xếp đúng
  mục này vào nhóm **"KHÔNG được chấm Fail vì…"** — thẻ nằm **trong** chi tiết 1 DN nên trường này bị ràng buộc bởi
  ngữ cảnh URL (`:560`, `:1205`), và phiếu đối tác cũng không nhắc ô này. Ghi nhận, **không** chấm lỗi, **không**
  đẩy BA.
- **Nhãn nút thêm là "Thêm hồ sơ"** — đã có candidate riêng ở `do/QLHSPLDN_06.md` §7. Theo Flow 03 §"Bug mới tự
  lộ" mục 2 (tra phiếu trùng trước khi đo thêm): **liên kết vào candidate đã có, không mở phiếu thứ hai.**

---

## 8. Phần chưa đo được

| Phần | Lý do | Có ảnh hưởng verdict? |
|---|---|---|
| Bộ lọc *Loại hồ sơ* · *Từ ngày* · *Đến ngày* (chưa dùng làm điều kiện thứ hai) | Nguồn chuẩn §3 chốt biến thể (b) là **"1 bộ lọc nữa — *Loại hồ sơ* **hoặc** *Trạng thái*"**; đã chọn *Trạng thái* vì bộ dữ liệu cho nó **bốn con số phân biệt** (3/3/4/2) nên chứng minh logic VÀ dứt khoát nhất. Chạy thêm bộ lọc khác là **vượt phạm vi** đã khóa. | **Không** — biến thể bắt buộc đã đủ 2/2 |
| Tìm kiếm không ra kết quả (từ khóa không khớp gì) | Thuộc **`QLHSPLDN_12`** (dòng 294), case khác | **Không** |
| Khoảng ngày không hợp lệ (`tu_ngay > den_ngay`, `:596`) | Thuộc **`QLHSPLDN_13`** (dòng 295), case khác | **Không** |
| Nội dung tệp *Xuất Excel* | Thuộc **`QLHSPLDN_14`** (dòng 296), case khác. Case này **không bấm** nút đó — tránh làm hỏng bằng chứng theo cảnh báo bẫy | **Không** |
| Phân trang kết quả tìm (`:645` BR-DATA-07) | Dữ liệu env đối tác chỉ 4 hồ sơ/DN, FE gọi `pageSize=100` ⇒ **không dựng được** ca nhiều trang mà không seed; case chỉ đọc nên không seed. Vế C1 **không** đòi phân trang | **Không** |
| Hành vi của vai trò khác (NHT, vai trò Doanh nghiệp ở `SCR-V.III-04`) | Ngoài vế — case chỉ đo đúng vai trò `CB_NV_TW` của đối tác | **Không** |

---

## 9. Tự kiểm trước khi chốt (cổng Flow 03)

| # | Câu hỏi | Trả lời |
|---|---|---|
| 1 | Chuẩn chấm có bám đúng SRS hiện tại + expected gốc? | Có — dùng nguyên bảng vế/điều kiện đã khoá ở `chuan/QLHSPLDN_11.md`; agent chuẩn đã tự mở `srs-v3.5` xác minh `:589-597`, `:638-645`, `:710-711` và chốt cả 3 vế là `MATCH` |
| 2 | Có đo đúng phần còn lỗi, hay chạy lại phần đã đạt / kiểm chức năng kế bên? | Đo đúng vế C1. Bản dựng env đích khác nơi từng Pass ⇒ **bắt buộc** đo lại; đặc biệt biến thể (b) là phần vòng trước **chưa hề chạy** |
| 3 | Reopen đã có FAIL hợp lệ chưa? | **Không có FAIL nào** ⇒ luật dừng sớm không kích hoạt; phải chạy hết mọi biến thể để được Pass — đã chạy hết 2/2 |
| 4 | Pass đã phủ hết vế/biến thể nguồn chuẩn yêu cầu? | Có — **2/2** biến thể bắt buộc, cả hai đều có đối chứng phản hồi máy chủ. Không tự nâng lên 3 biến thể (Flow 03 §Khi chưa có FAIL) |
| 5 | Artifact có chứa quan sát quyết định và đã mở đọc lại? | Có — 3 ảnh (nền so sánh · lượt a · lượt b), **từng ảnh đã mở ra đọc bằng mắt**, mô tả ở §5 |
| 6 | Người ngoài phiên đo có phân biệt được phần đạt / cần BA / chưa đo? | Có — §4 số đo, §6 verdict, §7 không có bug mới, §8 phần chưa đo, đều tách bạch |
