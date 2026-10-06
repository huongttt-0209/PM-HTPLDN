# HỒ SƠ ĐO — QLKTLBG_19 (Flow 04 · Giai đoạn B)

> Chuẩn chấm đã khoá: [`chuan/QLKTLBG_19.md`](../chuan/QLKTLBG_19.md). File này chỉ ghi phép đo.
> **Không đổi quan hệ MATCH/DIFF/GAP.** Cả C1 và C2 vào Giai đoạn B với quan hệ `MATCH · route TEST`.

---

## 1. Vân tay bản dựng (ghi đầu phiên)

| Mục | Giá trị thực đo |
|---|---|
| Env | `https://18.143.165.120.nip.io` |
| Giờ đo | **2026-08-07 02:30–02:36 giờ VN** (= 2026-08-06 19:30–19:36 GMT) |
| `last-modified` | `Thu, 06 Aug 2026 19:23:01 GMT` |
| `etag` | `W/"6a74df15-428"` |
| Bó mã FE | `/assets/index-D4Buvu4S.js` |
| Chuỗi phiên bản sidebar | `HTPLDN · V1.0.9` |

🔴 **ĐÃ CÓ DEPLOY GIỮA LÔ ĐO — báo điều phối.** Vân tay tham chiếu của lô 1 (02:08–02:20 giờ VN) là
`last-modified 18:51:25 GMT` · `etag W/"6a74d7ad-428"` · bó mã `index-DsMHK7Dp.js`. Cả 3 chỉ dấu đều đã đổi
⇒ **bản dựng đo case này MỚI HƠN** lô 1. Chuỗi phiên bản trên màn vẫn `V1.0.9` (đúng như cảnh báo: chuỗi này
không đáng tin, đối chiếu bằng `last-modified` + `etag` + bó mã).

Đã **tải lại trang** trước lô đo (chặn bẫy PASS/FAIL-oan (k) — tab cũ chạy JS cũ): `navigate_page` tới
`/dao-tao/bai-giang/danh-sach` → bị đá về `/login` → **đăng nhập lại từ đầu** trên bó mã mới.

---

## 2. Tài khoản thực dùng

| Mục | Giá trị |
|---|---|
| Tài khoản | **`cbnv_tw_02`** / `Test@1234` — đúng tài khoản prompt chỉ định, **không fallback** |
| Mã xác thực | `391703` (MailHog `cbnv_tw_02@htpldn.test`, 2026-08-06T19:31:38Z) |
| Danh tính sau đăng nhập | `CB Nghiệp vụ - Trung ương #02` · `vaiTro: ["CB_NV_TW"]` · `capDonVi: TW` · `donViId: 00000000-0000-4000-8000-000000000001` |
| Vai trò theo đặc tả | **CB NV** — `srs-fr-03-dao-tao.md:751` (đọc lại lượt này: `**Tác nhân:** CB NV / CB PD`) ✅ khớp |

**KHÔNG dùng `admin`** để ra verdict (chặn bẫy (j) — đổi vai trò để "cho ra nút").

---

## 3. Màn + tiền đề

| Mục | Giá trị |
|---|---|
| URL màn | `https://18.143.165.120.nip.io/dao-tao/bai-giang/danh-sach` |
| Điều hướng | **Click sidebar** Đào tạo, tập huấn → Kho tài liệu / Bài giảng (không `navigate_page` sau đăng nhập) |
| Tiêu đề trang (`h1`) | `Kho tài liệu / Bài giảng` |
| **N = tổng bản ghi** | **11** |

### Nguồn của N — 3 chiều số liệu cộng khớp (chống bẫy "phép đo đang nói dối")

| Chiều | Giá trị | Nguồn |
|---|---|---|
| Số thô `meta.total` | **11** | Phản hồi `GET /api/v1/bai-giangs?page=1&pageSize=20` (reqid=278, HTTP 200) |
| Độ dài mảng `data` | **11** | cùng phản hồi trên |
| Chữ trên màn | `Hiển thị 1-11 / 11 kết quả` | `innerText` của `.ant-pagination-total-text` |

→ Ba chiều **cộng khớp** ⇒ N = 11 dùng được. Body phản hồi giữ tại
[`seed-files/QLKTLBG_19-list-response.network-response`](../seed-files/QLKTLBG_19-list-response.network-response).

### Tiền đề "không có điều kiện lọc" (T3) — đo bằng tham số THỰC GỬI, không đoán bằng mắt

Lời gọi danh sách lúc vào màn: `GET /api/v1/bai-giangs?page=1&pageSize=10` (và trước đó `pageSize=20`) —
**không có bất kỳ tham số lọc nào** (không `loaiTaiLieu`, không `linhVucId`, không `congKhai`, không từ khoá).

⚠️ Bẫy (f) đã xử: màn **có hiện chip `Bộ lọc nâng cao (2)`** ngay khi vào. Kiểm bằng tham số thực gửi
⇒ chip này chỉ là **số ô lọc trong panel nâng cao**, KHÔNG phải bộ lọc đang áp. Tiền đề T3 **đạt thật**.

| Tiền đề | Trạng thái |
|---|---|
| T1 vai trò CB NV | ✅ `CB_NV_TW` |
| T2 màn có ≥1 bản ghi | ✅ 11 bản ghi (dữ liệu QA sẵn có, **không seed**) |
| T3 thanh lọc rỗng | ✅ request không mang tham số lọc |
| T4 tổng ≤ 10.000 | ✅ 11 ≪ 10.000 → không chạm trần BR-DATA-06 |
| T5 env + bản dựng | ✅ §1 |

---

## 4. Vế C1 — màn có chức năng Xuất Excel không

**Neo SRS (mở file đọc lại trong lượt này):**
- `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-03-dao-tao.md:1952`
  → `- Nút "Xuất Excel" (phụ): xuất danh sách theo bộ lọc hiện tại, tối đa 10.000 dòng (BR-DATA-06)`
- `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-v3.5.md:5570` (BR-DATA-06)
  → `**Export Excel:** Mọi danh sách có tính năng xuất Excel…` · Áp dụng FR = `Toàn bộ CRUD list` ·
  Ngoại lệ = chỉ `Báo cáo nhóm IX`

### 4.1. Đường UI — liệt kê DOM thanh công cụ (KHÔNG kết luận bằng mắt qua ảnh)

`evaluate_script` liệt kê **mọi** `button` / `a` / `[role=button]` ngoài vùng bảng, trả `innerText` +
`title` + `aria-label` + `className` + `disabled` + `visible`:

| # | innerText | title | aria-label | disabled | visible |
|---|---|---|---|---|---|
| 1 | `Thêm mới` | — | — | false | true |
| 2 | **`Xuất Excel`** | — | — | **false** | **true** |
| 3 | `Làm mới` | — | — | false | true |
| 4 | *(rỗng — icon xoá ô tìm kiếm)* | — | — | false | true |
| 5 | `Bộ lọc nâng cao (2)` | — | — | false | true |
| 6 | `Xóa bộ lọc` | — | — | false | true |
| 7 | `Tìm kiếm` | — | — | false | true |
| 8–10 | *(nút phân trang)* | — | — | — | — |

→ Nút **"Xuất Excel"** tồn tại, **có nhãn chữ rõ ràng**, **hiển thị**, **không bị vô hiệu hoá**.
Không có nút icon-không-nhãn nào bị bỏ sót ⇒ **không cần mở menu phụ** (bước U4 nhánh 5.1 không áp dụng vì
thanh công cụ không có kebab `…` / "Thao tác khác"; đã liệt kê hết và tìm thấy nút).

⚠️ Bẫy (e) đã xử: 4 nút icon trong mỗi hàng bảng (`eye` · `download` · `edit` · `delete`) là **hành động của
từng dòng** — `srs-fr-03-dao-tao.md:1974`: `| Hành động | — | Xem trực tuyến · Tải về (chỉ Slide/PDF) · Sửa ·
Xóa (xóa mềm, có hộp xác nhận) |`. Nút `download` trong hàng là **Tải về tệp bài giảng của một dòng**, KHÔNG
phải Xuất Excel danh sách. Hai thứ đã tách bạch: script lọc `inTable` (43 phần tử trong bảng bị loại khỏi bảng
trên).

### 4.2. Đối chứng độc lập — danh sách endpoint đã công bố

`fetch('/api/docs-json')` → HTTP 200, **549 path**. Lọc theo `bai-giang`:

```
/api/v1/khoa-hocs/{id}/bai-giangs/{baiGiangId}
/api/v1/bai-giangs
/api/v1/bai-giangs/export        ← endpoint xuất của màn này
/api/v1/bai-giangs/{id}
/api/v1/bai-giangs/{id}/preview-url
/api/v1/bai-giangs/{id}/preview-content
/api/v1/bai-giangs/upload-file
/api/v1/bai-giangs/upload-anh
/api/v1/bai-giangs/{id}/anh-url
/api/v1/public/bai-giangs  ·  /api/v1/public/bai-giangs/{id}  ·  /api/v1/public/bai-giangs/{id}/related
```

**Không đoán đường dẫn** — đọc từ danh sách công bố. Endpoint `/api/v1/bai-giangs/export` **có tồn tại**
(nằm trong 35 path `export` toàn hệ thống).

### 4.3. Kết quả C1

> ✅ **C1 ĐẠT.** Hai đường (UI + danh sách endpoint công bố) **khớp nhau** ⇒ dừng, không mở đường thứ ba.

**Triệu chứng TKM ghi trên bảng — "Màn hình không có nút chức năng" — KHÔNG tái hiện được trên bản dựng đo.**

---

## 5. Vế C2 — không đặt bộ lọc thì tệp có chứa toàn bộ danh sách không

**Neo SRS:** `srs-fr-03-dao-tao.md:1952` (*"xuất danh sách **theo bộ lọc hiện tại**"* — theo bộ lọc, **không**
nói theo trang) + `srs-v3.5.md:5570`.

### 5.1. Xử bẫy PASS-oan (i-2) TRƯỚC khi bấm — làm cho phép đo phân biệt được

Mặc định 20 dòng/trang mà N = 11 ⇒ 11 ≤ 20 ⇒ **tệp 11 dòng không phân biệt được** "xuất toàn bộ" với "xuất
đúng trang đang xem". Chuẩn chấm §7 (i-2) cảnh báo đúng ca này.

**Xử lý (không cần seed, không đụng dữ liệu):** hạ **Phân trang xuống `10 / trang`** — đây là tuỳ chọn hợp lệ
của chính màn (`srs-fr-03-dao-tao.md:1976`: *"mặc định 20 dòng/trang; cho phép 10/20/50/100"*), và **không
phải điều kiện lọc** nên tiền đề "không có điều kiện lọc" vẫn nguyên vẹn.

Sau khi hạ:

| Chiều | Giá trị |
|---|---|
| Số dòng trên trang đang xem (`.ant-table-tbody > tr.ant-table-row`) | **10** |
| Chữ trên màn | `Hiển thị 1-10 / 11 kết quả` |
| Số trang | 2 |
| N (tổng) | vẫn **11** |

→ Phép đo giờ **phân biệt được**: tệp 11 dòng ⇒ toàn bộ · tệp 10 dòng ⇒ cắt theo trang.

### 5.2. Đường UI — bấm [Xuất Excel] trên UI thật, 1 lần

Bộ bắt thông báo (`MutationObserver` trên `document.body`, đọc bằng **`innerText`**, **không dedupe**) cài
**TRƯỚC** khi bấm — để không lỡ toast lỗi 4xx/5xx theo bảng quyết định §9.

Kết quả bắt được:

```
19:34:55.564Z  ant-message-notice-wrapper …   "Xuất dữ liệu thành công."
19:34:55.565Z  ant-message-notice-success     "Xuất dữ liệu thành công."
19:34:55.565Z  ant-message-notice-wrapper …   "Xuất dữ liệu thành công."
19:34:55.565Z  ant-message-notice-success     "Xuất dữ liệu thành công."
```

⚠️ **4 bản ghi nhưng CÙNG mốc giờ (19:34:55.564–565)** ⇒ đếm theo **mốc giờ khác nhau**, không theo độ dài
mảng ⇒ đây là **MỘT thông báo** (observer bắt cả thẻ bọc `-wrapper` lẫn thẻ con `-notice`). **Không phải
double-toast, không log bug ma.**

Lời gọi tương ứng: **`POST /api/v1/bai-giangs/export` → HTTP 200** (reqid=291) — đúng endpoint đã công bố ở §4.2.
Console: **sạch** (0 error, 0 warn).

### 5.3. Đối chứng độc lập — MỞ TỆP đọc nội dung bằng `openpyxl`

Tệp **đổ được về `~/Downloads`**: `DanhSachBaiGiang_20260807_0234.xlsx` (7.636 B, 02:34 giờ VN).
Đã giữ bản sao: [`seed-files/QLKTLBG_19-DanhSachBaiGiang_20260807_0234.xlsx`](../seed-files/QLKTLBG_19-DanhSachBaiGiang_20260807_0234.xlsx)
· `md5 = 6cb83f908b5843bc2a3f1c6437d6d6d1`.

```
sheets: ['Bài giảng']
tổng dòng không rỗng = 12
hàng tiêu đề [0]: Tên bài giảng | Loại tài liệu | Lĩnh vực | Dung lượng | Công khai | Người tạo | Ngày tạo | Mô tả
dòng cuối [11]: QA UAT Bài giảng Test QLKTLBG_08 | PDF | Lao động | 547 B | Chưa công khai | … | 10/07/2026 22:52
```

**Số dòng dữ liệu = 12 − 1 (tiêu đề) = 11.**

Đối chiếu **danh tính** (không chỉ đếm số, chống trùng số ngẫu nhiên) — tên 11 bản ghi trong tệp so với
`data[].tenBaiGiang` của phản hồi danh sách:

```
Số dòng dữ liệu trong tệp : 11
Số bản ghi trong API      : 11   (meta.total = 11)
Trùng khớp hoàn toàn      : True
Chỉ có trong tệp          : []
Chỉ có trong API          : []
```

### 5.4. Kết quả C2

| Phép so | Kết quả |
|---|---|
| Số dòng dữ liệu trong tệp **11** vs N = **11** | ✅ **bằng nhau** |
| Danh tính 11 bản ghi tệp vs API | ✅ **trùng khớp hoàn toàn**, không thừa không thiếu |
| Tệp **11** dòng vs trang đang xem **10** dòng | ✅ **tệp KHÔNG cắt theo trang** — bản ghi thứ 11 (`QA UAT Bài giảng Test QLKTLBG_08`) nằm ở **trang 2**, không hiển thị trên trang 1, nhưng **vẫn có trong tệp** |

> ✅ **C2 ĐẠT.** Hai đường (bấm UI thật + mở tệp bằng `openpyxl`) khớp ⇒ dừng.

---

## 6. Bẫy đã chủ động chặn

| Bẫy | Xử lý thực tế |
|---|---|
| (b) nút icon-không-nhãn / menu phụ | Liệt kê DOM đủ `innerText`+`title`+`aria-label`+`className`; không kết luận bằng mắt |
| (c) `textContent` gom node ẩn | Toàn bộ đọc chữ dùng **`innerText`** |
| (d) tải được tệp ≠ nội dung đúng | **Mở tệp bằng `openpyxl`**; toast 200 chỉ ghi làm ngữ cảnh |
| (e) nhầm "Tải về" từng dòng với "Xuất Excel" | Lọc `inTable`; dẫn `:1974` |
| (f) chip "Bộ lọc nâng cao (2)" | Kiểm bằng **tham số thực gửi** — request không mang tham số lọc |
| (g) phạm vi `don_vi_id` | Tài khoản TW thấy rộng là đúng `:1981`; **không log thành lỗi** |
| (h) trần 10.000 dòng | N = 11 ≪ 10.000, không chạm trần; trần là hợp lệ |
| (i) bộ cột tệp xuất | SRS Nhóm III **không** quy định bộ cột cho SCR-III-03 ⇒ **không chấm Fail vì cột**; chỉ ghi lại header |
| (i-2) tệp chỉ chứa trang đang xem | **Hạ 10/trang** để tách bạch — đã chứng minh tệp 11 > trang 10 |
| (j) đổi vai trò cho ra nút | Chỉ dùng `cbnv_tw_02`, **không** đụng `admin` |
| (k) trang cũ / bản dựng cũ | Tải lại + đăng nhập lại trên bó mã mới `index-D4Buvu4S.js`; ghi vân tay |
| (l) hai phép mâu thuẫn | Không xảy ra — 11 = 11 và danh tính trùng khớp |
| đếm gộp thẻ bọc/thẻ con | Dùng `.ant-table-tbody > tr.ant-table-row`; toast đếm theo **mốc giờ** |

---

## 7. Artifact

| Tệp | Chứng minh điều gì | Mốc giờ |
|---|---|---|
| [`image/QLKTLBG_19-01-man-kho-tai-lieu-co-nut-xuat-excel-11-ban-ghi.png`](../image/QLKTLBG_19-01-man-kho-tai-lieu-co-nut-xuat-excel-11-ban-ghi.png) | Màn `/dao-tao/bai-giang/danh-sach` **CÓ nút [Xuất Excel]** ở thanh hành động chính · thanh lọc để trống · tài khoản `CB Nghiệp vụ - Trung ương #02` · bản dựng `HTPLDN · V1.0.9` — **bằng chứng C1** | 2026-08-07 02:33 VN |
| [`image/QLKTLBG_19-02-phan-trang-10-tren-trang-tong-11-luc-bam-xuat.png`](../image/QLKTLBG_19-02-phan-trang-10-tren-trang-tong-11-luc-bam-xuat.png) | `Hiển thị 1-10 / 11 kết quả` · 2 trang · `10 / trang` — trang 1 dừng ở bản ghi thứ 10 (`QA UAT Bài giảng Công khai QLKTLB…`), bản ghi 11 nằm trang 2 — **bằng chứng tiền đề C2 phân biệt được trang-vs-toàn-bộ** | 2026-08-07 02:35 VN |
| [`seed-files/QLKTLBG_19-DanhSachBaiGiang_20260807_0234.xlsx`](../seed-files/QLKTLBG_19-DanhSachBaiGiang_20260807_0234.xlsx) | **Tệp xuất thật** — 11 dòng dữ liệu, trùng khớp hoàn toàn với danh sách · `md5 6cb83f908b5843bc2a3f1c6437d6d6d1` | 2026-08-07 02:34 VN |
| [`seed-files/QLKTLBG_19-list-response.network-response`](../seed-files/QLKTLBG_19-list-response.network-response) | Phản hồi danh sách gốc — `meta.total = 11`, `data.length = 11`, **không tham số lọc** | 2026-08-07 02:32 VN |

Cả 2 ảnh đã **mở lại xác nhận** nội dung khớp mô tả trước khi dẫn.

Toast tự tắt trước khi chụp được — theo Flow 04 bước 7 **không lặp thao tác chỉ để chụp lại output thoáng
qua**; dùng **chữ đã bắt** (§5.2) + **phản hồi máy chủ** `POST /api/v1/bai-giangs/export → 200` thay thế.

---

## 8. Seed / mutate

> **KHÔNG seed. KHÔNG mutate.** Không tạo / sửa / xoá bản ghi nào trên `https://18.143.165.120.nip.io`.
> Dùng nguyên 11 bản ghi QA sẵn có. Không đụng dữ liệu đối tác.
>
> Thay đổi duy nhất là **tuỳ chọn hiển thị `10 / trang`** — thuộc trạng thái giao diện phía trình duyệt,
> không ghi gì xuống dữ liệu.

---

## 9. Bug mới / candidate

- **Bug mới: KHÔNG CÓ.** Console sạch; không hiện tượng nào tự lộ trong bước bắt buộc của C1/C2.
- **Candidate 1 (tài liệu, chuyển tiếp từ Giai đoạn A — không phải lỗi phần mềm, không đổi verdict):**
  bảng §6 `srs-fr-03-dao-tao.md:2243` thiếu FR-III-07 / FR-III-08 ở dòng BR-DATA-06 trong khi
  SCR-III-03 `:1952` dẫn thẳng BR-DATA-06 — đề nghị BA bổ sung cho khớp mục lục.
- **Candidate 2 (mới, MỘT DÒNG — không điều tra trong case này):** bộ quyền của `cbnv_tw_02` có 18 quyền
  `export_*` nhưng **không có `export_bai_giang`**, trong khi thao tác Xuất Excel màn này vẫn chạy 200 —
  cần đổi vai trò/tài khoản mới xác nhận được có phải thiếu kiểm quyền hay không ⇒ **chỉ ghi nhận**.

---

## 10. Cổng chốt verdict

| # | Câu hỏi | Trả lời |
|---|---|---|
| 1 | Mỗi vế neo dòng SRS nào? | C1 + C2 → `srs-fr-03-dao-tao.md:1952` và `srs-v3.5.md:5570`; đã **mở file đọc lại trong lượt này**, số dòng khớp nguyên văn |
| 2 | Mọi thao tác có trả lời một vế Cn? | Có: đăng nhập/vào màn = tiền đề · liệt kê DOM = C1 UI · `/api/docs-json` = C1 đối chứng · đọc `meta.total` = mốc so C2 · hạ 10/trang = tách bạch C2 · bấm Xuất Excel = C2 UI · `openpyxl` = C2 đối chứng. **Không thao tác thừa.** |
| 3 | Vế DIFF/GAP đã chặn Pass + có câu hỏi BA? | **Không có vế DIFF/GAP** (chuẩn chấm khoá C1·C2 đều MATCH) ⇒ không phát sinh câu hỏi BA |
| 4 | Đã đọc đầy đủ expected? | Có — expected nguyên văn *"Hệ thống xuất toàn bộ danh sách hiện có trên bảng danh sách"* + phản hồi TKM *"Màn hình không có nút chức năng"* |
| 5 | Điều kiện đo khớp tiền đề case? | Có — vai trò CB NV ✅ · **không đặt điều kiện lọc** ✅ (verify bằng tham số thực gửi) · danh sách có dữ liệu ✅ |

---

## 11. VERDICT

> # ✅ **Pass**
>
> Giá trị đề nghị cho ô `Trạng thái dev fix`: **`Test done`**

**Neo vào vế Cn:**

| Vế | Quan hệ (đã khoá) | Số đo quyết định | Kết luận |
|---|---|---|---|
| **C1** — màn phải có chức năng Xuất Excel | MATCH · TEST | Nút `Xuất Excel` **hiển thị + không disabled** trên thanh hành động chính; endpoint `/api/v1/bai-giangs/export` **có trong danh sách công bố** | ✅ **ĐẠT** |
| **C2** — không đặt lọc thì tệp chứa toàn bộ danh sách | MATCH · TEST | **Số dòng dữ liệu trong tệp = 11 = N (`meta.total`)**, danh tính trùng khớp 11/11; tệp **11** dòng > trang đang xem **10** dòng ⇒ không cắt theo trang | ✅ **ĐẠT** |

Mọi vế đều `MATCH` và phép đo đều đạt chuẩn rút từ SRS; không còn vế `DIFF`/`GAP` ⇒ theo bảng Verdict của
Flow 04 → **Pass**. Đúng bảng quyết định đã cam kết TRƯỚC khi đo (`chuan/QLKTLBG_19.md` §9, dòng *"Có nút; tệp
mở được; số dòng dữ liệu = tổng bản ghi màn (bộ lọc rỗng) → Pass"*).

### ⚠️ Giới hạn hiệu lực của verdict

1. **Chỉ có hiệu lực cho bản dựng đã đo:** `https://18.143.165.120.nip.io` · `last-modified 2026-08-06
   19:23:01 GMT` · `etag W/"6a74df15-428"` · bó mã `index-D4Buvu4S.js`. Env này deploy liên tục (đã đổi
   ngay giữa lô đo hôm nay).
2. **Không kết luận "fix đã có tác dụng".** Không có ảnh trạng thái trước khi fix của phía QA ⇒ chỉ khẳng
   định được **hiện trạng đúng đặc tả**, không suy ra được thao tác sửa nào đã tạo ra kết quả này
   (Flow 04 §Ca biên).
3. **Chưa kiểm trần 10.000 dòng** (`srs-v3.5.md:5570`) vì N = 11. Trần nằm ngoài expected của case này.
4. **Không chấm bộ cột tệp xuất** — SRS Nhóm III không quy định danh mục cột cho SCR-III-03. Header thực tế
   ghi lại để tham khảo: `Tên bài giảng · Loại tài liệu · Lĩnh vực · Dung lượng · Công khai · Người tạo ·
   Ngày tạo · Mô tả`.
5. **Không đo hộ QLKTLBG_20.** C2 của case 20 (bộ lọc cho ra 0 kết quả) là ca biên mà phép đo này chưa hề
   chạm tới — case đó có agent riêng.
