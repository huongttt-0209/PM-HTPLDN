# QLHSPLDN_12 — Tìm kiếm hồ sơ pháp lý không có kết quả · GIAI ĐOẠN A (khóa phép thử)

**Dòng bảng:** 294 (tab `bug`) · **Flow:** [`flows/03-reverify-sau-dev-fix.md`](../../../../../flows/03-reverify-sau-dev-fix.md) nhánh 2
**Env đo:** `https://htpldn-uat.ospgroup.vn` (env nghiệm thu của đối tác) · **Tài khoản ra verdict:** `cbnv_tw` / `Test@1234` (`CB_NV_TW`)
**Màn:** menu **Doanh nghiệp** → *Xem chi tiết* 1 DN → thẻ **Hồ sơ pháp lý doanh nghiệp** (`/doanh-nghiep/{id}?tab=ho-so-pl`)
**Nguồn canonical cách đo:** entry `BUG-HSPLDN-QLHSPLDN-12` trong [`F4-pilot/bug-report.md`](../../F4-pilot-QLHSPLDN-2026-08-07/bug-report.md) + vế C2 trong [`F4-pilot/bao-cao-lo`](../../F4-pilot-QLHSPLDN-2026-08-07/bao-cao-lo-2026-08-07.md)

> ⚠️ Mọi dòng SRS dưới đây đã **mở file đọc lại** trong lô này, không bê từ báo cáo cũ.

---

## 1. Ô phiếu đối tác (expected gốc — nguyên văn)

| Ô | Nội dung |
|---|---|
| **Mô tả** | Tìm kiếm hồ sơ pháp lý không có kết quả |
| **Bước 4** | *NSD nhập từ khóa và/hoặc chọn bộ lọc* (không khớp bản ghi nào) |
| **Kết quả mong đợi** | *"Không có kết quả, hệ thống hiển thị thông báo \"Không tìm thấy hồ sơ pháp lý phù hợp\"."* |
| **TKM phản hồi lần 1 (KQ thực tế phía đối tác)** | *"Không có trường thông tin tìm kiếm trên màn hình"* |

---

## 2. Bảng vế × quan hệ SRS

| Vế | Đối tác đòi gì | SRS `file:dòng` — quote nguyên văn | Quan hệ | Route |
|---|---|---|---|---|
| **C2a** — chạy được thao tác tìm (tiền đề) | Bước 4 phải thực hiện được | `srs-fr-12-tv-chuyen-sau.md:589` — "**Inputs -- Tìm kiếm:**"; `:593` — "\| 1 \| keyword \| text \| N \| Tìm theo mã HS, tên DN, tên HS \|"; `:638` — "**Tìm kiếm:**"; `:643` — "Áp dụng tất cả bộ lọc: từ khóa, loại hồ sơ, DN, khoảng ngày, trạng thái" | **MATCH** | TEST (tiền đề, đã khóa riêng ở `QLHSPLDN_11`) |
| **C2b** — hiện đúng câu báo khi không ra kết quả | *"hệ thống hiển thị thông báo \"Không tìm thấy hồ sơ pháp lý phù hợp\""* | `srs-fr-12:701` — "\| E7 \| Không có kết quả tìm kiếm \| **INF-HSPL-01** \| \"**Không tìm thấy hồ sơ pháp lý phù hợp**\" \| INFO \|" (bảng **Error Handling** mở ở `:691`, tiêu đề cột ở `:693`) | **MATCH** — khớp **từng ký tự** với câu trong ô phiếu | TEST |
| **C2c** — chức năng thuộc đúng thẻ đang tranh chấp | Phiếu chỉ đích danh thẻ *Hồ sơ pháp lý* trong chi tiết DN | `srs-fr-12:560` — "**Màn hình:** ~~SCR-X1-03~~ (DEPRECATED v2.1 — chuyển sang tab trong MH-07.2 chi tiết DN)"; `:1205` — "> **Chuyển sang:** Tab \"Hồ sơ PL\" trong MH-07.2 chi tiết Doanh nghiệp (srs-fr-07-doanh-nghiep.md)."; `srs-fr-07-doanh-nghiep.md:455`, `:461` | **MATCH** | TEST |

**Vai trò được phép:** `srs-fr-12:565` — "**Tác nhân:** Cán bộ Nghiệp vụ (TW/BN/ĐP), Người hỗ trợ".

### 2.1 Giải quyết điểm "hai nơi không khớp" — `srs-fr-12` ↔ `srs-fr-07:468` ("CRUD")

- `srs-fr-07:468` — "| 2 | tab | Tab Hồ sơ PL doanh nghiệp (MỚI v2.1) | tab | **CRUD hồ sơ pháp lý DN**: GIAY_PHEP / … Trạng thái: … Gộp từ MH-12.3 (Tư vấn CS) | — | Chỉ khi xem chi tiết |"
- `srs-fr-12:563` — "CRUD hồ sơ pháp lý doanh nghiệp: xem danh sách, xem chi tiết, thêm mới, chỉnh sửa, xóa mềm, **tìm kiếm**."

⇒ "CRUD" ở `:468` là **nhãn gọi tắt của FR-X.1-04**, mà FR-X.1-04 tự khai phạm vi CRUD của nó **bao gồm tìm kiếm**. Bảng thành phần `SCR-V.III-02` **không enumerate** nội dung bên trong thẻ 2/3/4 (`:467`–`:470` là 4 dòng thẻ; `:471`–`:494` là trường của thẻ *Thông tin cơ bản*; `:495`–`:496` là thanh hành động), nên đây là **im lặng ở mức liệt kê**, **không phải phủ định**. Câu báo `INF-HSPL-01` lại được `:701` quy định **tường minh và có mã lỗi riêng**.

**Kết luận C2: `MATCH`** — được đo, được Pass nếu đạt. **Không có câu hỏi BA.**

### 2.2 Bẫy đã có tiền lệ — đã kiểm lại, xác nhận không áp

`srs-fr-07:523` ("Tab 2 — Hồ sơ pháp lý DN | **Read-only** danh sách HO_SO_PHAP_LY_DN") thuộc **`SCR-V.III-04`** (`:508`), màn `/doanh-nghiep/ho-so-cua-toi` của **vai trò Doanh nghiệp**; `:514` — "**Quyền truy cập:** Doanh nghiệp (Tier 2 VNeID) … **Vai trò khác KHÔNG truy cập trang này.**" ⇒ **cấm dùng cho màn đang đo** (`SCR-V.III-02`).

---

## 3. Dòng khóa phép đo

```
C2 · không có ô tìm kiếm nên không kiểm được câu báo khi tìm không ra hồ sơ nào
   · srs-fr-12-tv-chuyen-sau.md:701 (E7 · INF-HSPL-01 · INFO) + :589-597 + :638-645 (neo màn :560, :1205)
   · MATCH
   · thao tác: trên thẻ Hồ sơ pháp lý của 1 DN — clear ô từ khóa, gõ chuỗi chắc chắn không khớp bản ghi nào
              (vd `zzqqxx-khongtontai`) rồi bấm [Tìm kiếm]
   · PASS khi: bảng còn 0 dòng · trên màn hiện đúng NGUYÊN VĂN TỪNG KÝ TỰ "Không tìm thấy hồ sơ pháp lý phù hợp"
              (đọc bằng innerText) · phản hồi máy chủ của CHÍNH lệnh tìm đó trả danh sách rỗng (total = 0)
   · FAIL khi: bảng vẫn còn dòng · hoặc không hiện câu nào · hoặc câu lệch dù 1 ký tự · hoặc máy chủ trả > 0
              bản ghi mà màn báo rỗng (và ngược lại) · hoặc lệnh tìm trả 4xx/5xx
   · biến thể bắt buộc: 1 — nhánh rỗng do từ khóa (đúng phạm vi Bước 4 của phiếu)
```

---

## 4. Đối chứng độc lập bắt buộc

🔴 **CẤM Pass bằng quan sát tĩnh.** Nhìn thấy màn "trống" **không phải** bằng chứng — phải chứng minh cả **câu chữ** lẫn **dữ liệu nguồn rỗng**.

| # | Việc phải làm | Vì sao tính là độc lập |
|---|---|---|
| 1 | **Clear sạch ô từ khóa** rồi mới gõ `zzqqxx-khongtontai`. Kiểm lại giá trị ô sau khi điền | Công cụ điền **nối chuỗi** vào giá trị cũ — vòng trước đã đo hụt 1 lần vì `QA-W5zzqqxx-khongtontai` |
| 2 | Bấm [Tìm kiếm] thật bằng UI | Hành động tranh chấp phải chạy bằng UI |
| 3 | **Đọc chữ trên màn bằng `innerText`** (CẤM `textContent` — bắt cả node ẩn của AntD → sinh bug ma), rồi **so từng ký tự** với chuỗi `Không tìm thấy hồ sơ pháp lý phù hợp` ở `:701`. Ghi lại `exactMatch` + danh sách vị trí ký tự lệch (nếu có) | So bằng mắt không phát hiện được lệch dấu / khoảng trắng kép / chữ hoa-thường |
| 4 | **Đọc phản hồi máy chủ của chính lệnh tìm đó**: phải là danh sách **rỗng**, `total = 0`, và tham số `keyword` gửi lên đúng chuỗi đã gõ | Đối chứng độc lập theo Flow 03 §Chạy.3. **Bấm lại cùng nút KHÔNG tính.** Đây là chỗ bắt ca "FE tự ẩn dòng nhưng BE vẫn trả dữ liệu" và ca "FE hiện câu rỗng cứng bất kể máy chủ trả gì" |
| 5 | Ghi rõ **câu hiện ở đâu**: thông báo nổi hay dòng chữ trong vùng bảng rỗng | Không dùng để chấm (xem §6), nhưng dev cần biết |

**Ghi lại tối thiểu:** ảnh màn có ô từ khóa + bảng rỗng + câu báo · kết quả so ký tự · thân phản hồi máy chủ · vân tay bản dựng ở **đầu và cuối** case.

---

## 5. Tiền đề dữ liệu trên env đối tác

**KHÔNG seed gì.** Case này chỉ đọc, và nhánh cần đo là nhánh **rỗng** — không đòi hỏi bản ghi nào.

| Hạng mục | Nội dung |
|---|---|
| DN dùng để đo | **`DN-XX-0005`** (`1a715c55-bc31-46de-ae07-56dd4f403ce5`) — dùng chung phiên với `QLHSPLDN_11` |
| Tiền đề duy nhất | Thẻ mở được và có ô từ khóa (đã là kết quả đo của `QLHSPLDN_11`) |
| Từ khóa an toàn | **`zzqqxx-khongtontai`** — chuỗi vô nghĩa, **không phụ thuộc dữ liệu đối tác**, chắc chắn không khớp mã/tên nào. Có thể thay bằng chuỗi ngẫu nhiên tương đương; **cấm** dùng chuỗi có thể tình cờ khớp (vd `a`, `2026`, `hồ sơ`) |
| 🔴 Cấm | **KHÔNG sửa, KHÔNG xoá** `DN-XX-0005`, `HSPL-20260803-0001`, `HSPL-20260731-0002` và mọi bản ghi QA không tự tạo |

**Nếu DN đang xem không có hồ sơ nào (bảng vốn đã rỗng):** vẫn đo được nhưng **yếu** — không phân biệt được "rỗng do lọc" với "rỗng do chưa có dữ liệu". ⇒ Phải chạy trên DN **có ≥1 hồ sơ**, chụp baseline ≥1 dòng trước, rồi mới gõ từ khóa rác. Không có DN nào có hồ sơ → theo §5 của [`QLHSPLDN_11.md`](QLHSPLDN_11.md) (đổi DN → nếu vẫn không có thì tạo bằng UI **[Thêm hồ sơ]** với dấu `QA-W5-…`, khai đủ vào báo cáo).

---

## 6. Chuẩn chấm

### ✅ PASS khi (phải đủ **tất cả**)
1. Trước khi lọc, bảng có ≥1 dòng (baseline chụp được).
2. Gõ từ khóa rác + bấm [Tìm kiếm] → bảng còn **0 dòng**.
3. Trên màn hiện chữ **`Không tìm thấy hồ sơ pháp lý phù hợp`**, so bằng `innerText`, **khớp tuyệt đối 0 ký tự lệch** với `:701`.
4. Phản hồi máy chủ của chính lệnh đó: danh sách rỗng, `total = 0`, `keyword` gửi lên đúng chuỗi đã gõ.
5. Vân tay bản dựng đầu case = cuối case.

### ❌ FAIL khi (chỉ cần **một**)
- Thẻ không có ô tìm kiếm ⇒ đúng triệu chứng đối tác báo, Reopen ngay.
- Bảng rỗng nhưng **không hiện câu nào**, hoặc chỉ hiện chữ chung chung khác (vd *"Không có dữ liệu"*, *"No data"*).
- Câu hiện ra **lệch dù 1 ký tự** so với `:701`.
- Máy chủ trả > 0 bản ghi mà màn báo rỗng, hoặc máy chủ trả rỗng mà bảng vẫn còn dòng.
- Lệnh tìm trả 4xx/5xx.

### 🚫 KHÔNG được chấm **Fail** vì
- **Câu hiện dưới dạng dòng chữ trong vùng bảng rỗng thay vì thông báo nổi.** `:701` chỉ quy định **nội dung phản hồi + mức INFO**, **không** quy định kênh hiển thị. Ghi lại kênh, không chấm lỗi.
- Không thấy mã `INF-HSPL-01` hiện trên giao diện — mã là định danh nội bộ của đặc tả, không phải chuỗi bắt buộc hiển thị.
- Kèm theo câu đúng còn có thêm hình minh họa / icon trạng thái rỗng.
- Lần điền đầu bị **nối chuỗi** vào ô (lỗi công cụ) → clear ô, đo lại; không tính là lỗi sản phẩm.
- Bảng trên màn có 10 cột — thuộc phạm vi ghi nhận của `QLHSPLDN_14`, không liên quan C2.

### 🚫 KHÔNG được chấm **Pass** vì
- **Chỉ nhìn thấy ô tìm kiếm đã hiện trên màn** (quan sát tĩnh) — cấm tuyệt đối.
- Đọc chữ bằng `textContent` (bắt node ẩn) hoặc so bằng mắt thay vì so từng ký tự.
- Không đọc phản hồi máy chủ ⇒ không loại được ca "FE hiện câu rỗng cứng" hoặc "BE vẫn trả dữ liệu".
- Bảng vốn đã rỗng từ đầu, không có baseline ≥1 dòng ⇒ **Chưa chốt**, không phải Pass.
- Lấy kết quả Pass ở env nội bộ (bản dựng `V1.0.9`) làm căn cứ.
- Bấm lại cùng nút lần hai và coi đó là đối chứng độc lập.

---

## 7. Câu hỏi BA

**Không có.** Cả 3 vế con đều `MATCH` (xem §2.1); câu chữ ở `:701` trùng khít **từng ký tự** với ô phiếu đối tác. Case này đi thẳng **TEST**.
