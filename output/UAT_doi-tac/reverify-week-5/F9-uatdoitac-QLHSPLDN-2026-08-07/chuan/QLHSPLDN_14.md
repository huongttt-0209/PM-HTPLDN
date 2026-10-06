# QLHSPLDN_14 — Xuất Excel thành công · GIAI ĐOẠN A (khóa phép thử)

**Dòng bảng:** 296 (tab `bug`) · **Flow:** [`flows/03-reverify-sau-dev-fix.md`](../../../../../flows/03-reverify-sau-dev-fix.md) nhánh 2
**Env đo:** `https://htpldn-uat.ospgroup.vn` (env nghiệm thu của đối tác) · **Tài khoản ra verdict:** `cbnv_tw` / `Test@1234` (`CB_NV_TW`)
**Màn:** menu **Doanh nghiệp** → *Xem chi tiết* 1 DN → thẻ **Hồ sơ pháp lý doanh nghiệp** (`/doanh-nghiep/{id}?tab=ho-so-pl`)
**Nguồn canonical cách đo:** entry `BUG-HSPLDN-QLHSPLDN-14` trong [`F4-pilot/bug-report.md`](../../F4-pilot-QLHSPLDN-2026-08-07/bug-report.md) + vế C4 trong [`F4-pilot/bao-cao-lo`](../../F4-pilot-QLHSPLDN-2026-08-07/bao-cao-lo-2026-08-07.md)

> ⚠️ Mọi dòng SRS dưới đây đã **mở file đọc lại** trong lô này, không bê từ báo cáo cũ.

---

## 1. Ô phiếu đối tác (expected gốc — nguyên văn)

| Ô | Nội dung |
|---|---|
| **Mô tả** | Xuất Excel thành công |
| **Bước 4** | *Bấm nút "Xuất Excel" trên thẻ* |
| **Kết quả mong đợi** | *"Hệ thống xuất danh sách hồ sơ pháp lý theo bộ lọc hiện tại ra tệp Excel (tối đa 10.000 dòng), gồm các cột: Mã hồ sơ, Tên hồ sơ, Doanh nghiệp, Loại hồ sơ, Ngày cấp, Ngày hết hạn, Trạng thái, Cơ quan cấp."* |
| **TKM phản hồi lần 1 (KQ thực tế phía đối tác)** | *"Màn hình không có nút chức năng"* |

---

## 2. Bảng vế × quan hệ SRS

| Vế | Đối tác đòi gì | SRS `file:dòng` — quote nguyên văn | Quan hệ | Route |
|---|---|---|---|---|
| **C4a** — xuất được tệp `.xlsx` từ thẻ | Bước 4: *"Bấm nút \"Xuất Excel\" trên thẻ"* | `srs-fr-12-tv-chuyen-sau.md:657` — "**Processing — Xuất Excel** \`[GAP-X.1-05]\`"; `:661` — "\| 1 \| Kiểm tra quyền và phạm vi đơn vị \| BR-AUTH-01, BR-AUTH-08 \|"; `:665` — "\| 5 \| **Trả file .xlsx cho người dùng download** \| — \|" | **MATCH** | TEST |
| **C4b** — xuất **theo bộ lọc hiện tại** | *"xuất danh sách hồ sơ pháp lý **theo bộ lọc hiện tại**"* | `srs-fr-12:662` — "\| 2 \| **Áp dụng bộ lọc hiện tại (keyword, loại, DN, khoảng ngày, trạng thái)** \| — \|" | **MATCH** | TEST |
| **C4c** — tệp gồm **đúng 8 cột, đúng thứ tự** | *"gồm các cột: Mã hồ sơ, Tên hồ sơ, Doanh nghiệp, Loại hồ sơ, Ngày cấp, Ngày hết hạn, Trạng thái, Cơ quan cấp"* | `srs-fr-12:664` — "\| 4 \| Tạo file .xlsx: **columns = mã hồ sơ, tên, DN, loại, ngày cấp, hết hạn, trạng thái, cơ quan cấp** \| — \|" | **MATCH** — cùng **8 trường, cùng thứ tự** (SRS viết tắt, phiếu viết đủ nhãn) | TEST |
| **C4d** — ngưỡng *"tối đa 10.000 dòng"* | *"(tối đa 10.000 dòng)"* | `srs-fr-12:663` — "\| 3 \| Truy vấn tất cả bản ghi matching, **giới hạn tối đa 10.000 dòng** \| — \|" | **MATCH** về yêu cầu, nhưng **không đo tới được trên env** — xem §6.1 | TEST phần đo được + khai `⏸ CHƯA KIỂM TRA` phần còn lại |
| **C4e** — chức năng thuộc đúng thẻ đang tranh chấp | Phiếu chỉ đích danh nút trên **thẻ Hồ sơ pháp lý** | `srs-fr-12:560` — "**Màn hình:** ~~SCR-X1-03~~ (DEPRECATED v2.1 — chuyển sang tab trong MH-07.2 chi tiết DN)"; `:1205` — "> **Chuyển sang:** Tab \"Hồ sơ PL\" trong MH-07.2 chi tiết Doanh nghiệp (srs-fr-07-doanh-nghiep.md)."; `srs-fr-07-doanh-nghiep.md:455`, `:461` | **MATCH** | TEST |

**Vai trò được phép:** `srs-fr-12:565` — "**Tác nhân:** Cán bộ Nghiệp vụ (TW/BN/ĐP), Người hỗ trợ".

### 2.1 Giải quyết điểm "hai nơi không khớp" — `srs-fr-12` (khối Xuất Excel) ↔ `srs-fr-07:468` ("CRUD")

Đây là vế mà điểm không khớp **thật sự có sức nặng**, vì "Xuất Excel" **không** phải một thao tác CRUD. Đã đọc trọn cả hai đoạn và tra tiếp lịch sử sửa đổi:

**Phía nghi ngờ (SRS im lặng ở 3 chỗ):**
- `srs-fr-07:468` — "| 2 | tab | Tab Hồ sơ PL doanh nghiệp (MỚI v2.1) | tab | **CRUD hồ sơ pháp lý DN**: GIAY_PHEP / … | — | Chỉ khi xem chi tiết |" — không nhắc Xuất Excel. Cùng ý ở `:459`, `:502`.
- `srs-fr-12:563` (**Mô tả** của FR-X.1-04) — "CRUD hồ sơ pháp lý doanh nghiệp: xem danh sách, xem chi tiết, thêm mới, chỉnh sửa, xóa mềm, tìm kiếm." — **không** liệt kê Xuất Excel.
- **Tiêu chí chấp nhận** của FR-X.1-04 (`:703`–`:714`) — **không** có tiêu chí nào cho Xuất Excel.

**Phía khẳng định (SRS nói tường minh):**
- `srs-fr-12:657`–`:665` — nguyên một **khối Xử lý riêng** "Processing — Xuất Excel", 5 bước, có quy định bộ lọc (`:662`), ngưỡng (`:663`), danh sách cột (`:664`), trả tệp (`:665`). Đây là **phát biểu yêu cầu**, không phải ghi chú.
- `CHANGELOG-v3-to-v3.5.md:1577` — "…với hồ sơ pháp lý thì thiếu \"Xem chi tiết\" và \"**Xuất Excel**\" **mặc dù màn hình SCR-X1-03 đã có nút và Tiêu chí chấp nhận đã yêu cầu**…"
- `CHANGELOG:1578` — "…v4 bổ sung 6 khối Xử lý còn thiếu (2 khối cho FR-X.1-04…) → B1." ⇒ khối `:657-665` là **thay đổi có chủ đích đã được duyệt và apply**.
- `CHANGELOG:1651` — "### Gap ngoài delta phát hiện ở deep review (xử lý ở lượt review tiếp / Pha 3)"; `:1658` — "4. **FR-X.1-04 phần Tiêu chí chấp nhận** chưa thêm tiêu chí cho \"Xem chi tiết\" và \"Xuất Excel\" (Thay đổi 8.1, 8.2)."; `:1659` — "5. **Phần Mô tả của FR-X.1-01 / FR-X.1-04 / FR-X.1-06** chưa cập nhật để nhắc tới các luồng nghiệp vụ mới được bổ sung."; `:1661` — "5 gap này thuộc category \"**đầy đủ nội dung tài liệu**\" chứ không phải \"đúng nội dung delta\"…"

**Kết luận:** ba chỗ im lặng ở trên **đã được chính SRS tự khai là thiếu sót biên tập chưa dọn**, **không** phải quyết định bỏ chức năng. Không có bất kỳ câu nào trong SRS nói thẻ này **không** có Xuất Excel. Bảng thành phần `SCR-V.III-02` cũng **không enumerate** nội dung bên trong thẻ 2/3/4 (`:467`–`:470` là 4 dòng thẻ; `:471`–`:494` là trường của thẻ *Thông tin cơ bản*; `:495`–`:496` là thanh hành động) — im lặng ở mức liệt kê, không phải phủ định.

⇒ **C4 = `MATCH`**, không phải `DIFF`, không phải `GAP`. **Được đo và được Pass nếu đo đạt. Không có câu hỏi BA cho case này.**

**Hệ quả cho phép đo:** SRS **không** quy định **vị trí, nhãn hay hình dạng** của nút xuất trên thẻ. Điều bắt buộc là: **từ chính thẻ Hồ sơ pháp lý, người dùng xuất được tệp .xlsx đúng nội dung `:662`–`:665`**.

### 2.2 Ba bẫy phải tránh khi đo C4

| Bẫy | Sự thật đã kiểm | Hệ quả |
|---|---|---|
| **Nhầm nút Xuất Excel của màn khác** | `srs-fr-07:425` — "\| 5 \| toolbar \| Nút Xuất Excel \| button \| \"Xuất Excel\" \| click → export danh sách \| Luôn hiển thị \|" thuộc **`SCR-V.III-01` — màn DANH SÁCH doanh nghiệp**, xuất **danh sách DN**, khác thực thể | Chỉ bấm nút nằm **trong đúng vùng thẻ Hồ sơ pháp lý**. Nếu tệp xuất ra là danh sách DN ⇒ **không** phải bằng chứng cho C4 |
| **Lấy nhầm dòng "bỏ Xuất Excel"** | `srs-fr-07:17` — "…Quyết định CĐT/BA — **BỎ chức năng Xuất Excel khỏi FR-V.III-01** (Thay đổi 5 cũ trong delta — đã OUT, không apply vào v3.5)." Đây là **FR-V.III-01 (doanh nghiệp)**, **không** phải FR-X.1-04 (hồ sơ pháp lý) | **Cấm** dùng dòng này để kết luận thẻ Hồ sơ pháp lý không cần xuất Excel |
| **Chấm nhầm theo bảng trên màn** | Vòng trước ghi nhận: **bảng trên màn có 10 cột** (thêm *Lĩnh vực pháp lý* · *Nguồn* · *Có tệp đính kèm*; **thiếu** *Doanh nghiệp* · *Cơ quan cấp*), trong khi `:664` quy định **8 cột cho TỆP** | Vế C4 nói về **tệp xuất** ⇒ **chấm theo tệp**, tuyệt đối không chấm theo bảng. Bảng 10 cột **không** phải lỗi của C4 |

### 2.3 Bẫy đã có tiền lệ — đã kiểm lại, xác nhận không áp

`srs-fr-07:523` ("Tab 2 — Hồ sơ pháp lý DN | **Read-only** danh sách HO_SO_PHAP_LY_DN") thuộc **`SCR-V.III-04`** (`:508`, URL `/doanh-nghiep/ho-so-cua-toi`), mà `:514` ghi "**Vai trò khác KHÔNG truy cập trang này.**" ⇒ **cấm dùng cho màn đang đo** (`SCR-V.III-02`).

---

## 3. Dòng khóa phép đo

```
C4 · thẻ Hồ sơ pháp lý DN không có nút Xuất Excel nên không xuất được danh sách
   · srs-fr-12-tv-chuyen-sau.md:657-665 (bộ lọc :662 · ngưỡng :663 · 8 cột :664 · trả tệp :665)
     (neo màn :560, :1205; srs-fr-07:455, :461, :468 — đã giải ở §2.1)
   · MATCH
   · thao tác: trên thẻ Hồ sơ pháp lý của 1 DN — (a) [Xóa bộ lọc] để về tập ĐẦY ĐỦ, ghi số dòng + danh sách mã,
              bấm [Xuất Excel], MỞ NỘI DUNG tệp .xlsx; (b) đặt bộ lọc cắt ra TẬP CON thực sự nhỏ hơn, ghi lại
              tập con, bấm [Xuất Excel] lần nữa, MỞ NỘI DUNG tệp thứ hai
   · PASS khi: cả 2 tệp mở được · hàng tiêu đề đủ 8 trường ĐÚNG THỨ TỰ :664 · thân tệp (a) khớp đúng số dòng
              và đúng danh sách mã của tập đầy đủ · thân tệp (b) chỉ chứa TẬP CON (đúng số dòng + đúng mã),
              không lẫn bản ghi ngoài bộ lọc
   · FAIL khi: không xuất được từ thẻ · tệp hỏng/không mở được/không phải .xlsx · thiếu cột · thừa cột ·
              sai thứ tự cột · thân tệp (b) chứa cả bản ghi ngoài bộ lọc (tức bỏ qua :662) ·
              số dòng hoặc danh sách mã trong tệp lệch tập đang hiển thị
   · biến thể bắt buộc: 2 — (a) xuất KHÔNG lọc · (b) xuất CÓ lọc ra tập con thực sự nhỏ hơn (:662 + expected
              "theo bộ lọc hiện tại")
   · ngưỡng 10.000 dòng (:663): KHÔNG đo tới được trên env ⇒ khai ⏸ CHƯA KIỂM TRA, KHÔNG chặn Pass (xem §6.1)
```

---

## 4. Đối chứng độc lập bắt buộc

🔴 **CẤM Pass bằng quan sát tĩnh.** Thấy nút *Xuất Excel* hiện trên thẻ **không phải** bằng chứng. **Thấy tệp tải về cũng CHƯA ĐỦ** — phải **mở nội dung tệp**.

| # | Việc phải làm | Vì sao tính là độc lập |
|---|---|---|
| 1 | **Ghi baseline trước mỗi lần xuất:** số dòng bảng + **danh sách mã hồ sơ** đang hiển thị (cả 2 lượt (a) và (b)) | Không có tập đối chiếu thì "tệp đúng bộ lọc" không chứng minh được |
| 2 | **Bấm nút [Xuất Excel] thật bằng UI**, nút nằm **trong đúng vùng thẻ Hồ sơ pháp lý** (xem bẫy §2.2) | Hành động tranh chấp phải chạy bằng UI |
| 3 | 🔴 **MỞ NỘI DUNG tệp `.xlsx`.** MCP isolated Chrome **không** đổ tệp về `~/Downloads` ⇒ **parse ngay trong trang**: lấy `ArrayBuffer` của tệp → tìm **EOCD** (chữ ký `PK\x05\x06`) đọc central directory → định vị entry `xl/sharedStrings.xml` + `xl/worksheets/sheet1.xml` → giải nén bằng **`DecompressionStream('deflate-raw')`** → đọc XML. **Chỉ `return` đúng thứ cần đo** (mảng nhãn hàng 1 · số hàng thân · mảng giá trị cột 1) — **không** dump base64, không trả cả tệp | Đây là đối chứng độc lập theo Flow 03 §Chạy.3 ("tệp xuất → **mở chính tệp**"). Nút bấm được + tệp về ≠ tệp đúng |
| 4 | **Đọc hàng tiêu đề**: đếm số cột, ghi **nguyên văn từng nhãn theo đúng thứ tự trái→phải**, đối chiếu 1-1 với 8 trường ở `:664` | Bắt ca thiếu cột / thừa cột / đảo thứ tự |
| 5 | **Đếm số hàng thân tệp** và **đọc cột mã hồ sơ của toàn bộ thân**, so với danh sách mã ở bước 1 — so **theo tập**, không chỉ so số lượng | Số lượng bằng nhau vẫn có thể là **tập khác** |
| 6 | **Lượt (b) là phép chứng minh "theo bộ lọc hiện tại"**: tập trong tệp (b) phải **⊊** tập trong tệp (a) và **bằng đúng** tập đang hiển thị sau khi lọc | Đây là điều duy nhất phân biệt "xuất theo bộ lọc" với "xuất tất cả". **Bấm lại cùng nút KHÔNG tính** |
| 7 | Ghi lại đường gọi máy chủ sinh tệp (từ `list_network_requests`) + kích thước tệp + kiểu MIME | Phân biệt tệp do máy chủ sinh với tệp ghép ở trình duyệt; dữ kiện cho dev |
| 8 | Ghi lại thông báo sau khi bấm (nếu có) bằng `MutationObserver` cài **trước** khi bấm, **không lọc trùng**, đọc `innerText` | Bắt ca "báo thành công nhưng tệp rỗng/hỏng" |

**Ghi lại tối thiểu:** ảnh thẻ có nút + bảng ở trạng thái (a) và (b) · mảng nhãn hàng tiêu đề của cả 2 tệp · số hàng thân + danh sách mã của cả 2 tệp · vân tay bản dựng ở **đầu và cuối** case.

---

## 5. Tiền đề dữ liệu trên env đối tác

**Ưu tiên: KHÔNG seed gì.** Xuất Excel là thao tác **đọc** — nó tạo tệp tải về, **không** ghi vào hệ thống.

| Hạng mục | Nội dung |
|---|---|
| DN dùng để đo | **`DN-XX-0005`** (`1a715c55-bc31-46de-ae07-56dd4f403ce5`), URL `/doanh-nghiep/1a715c55-bc31-46de-ae07-56dd4f403ce5?tab=ho-so-pl` |
| Hồ sơ đã biết trên DN đó (đọc từ bằng chứng đối tác vòng trước) | `HSPL-20260803-0001` *TKM hồ sơ pháp lý số 1* — **Khác** · Thuế · Thủ công · 03/08/2026 · 03/08/2026 · Hiệu lực<br>`HSPL-20260731-0002` *Hồ sơ x* — **Giấy chứng nhận** · Đất đai · Thủ công · 01/07/2026 · – · Hiệu lực |
| 🔴 **Điều kiện tối thiểu** | **≥2 bản ghi** trên cùng thẻ **và** tồn tại **≥1 bộ lọc cắt ra tập con thực sự nhỏ hơn** (≥1 dòng nhưng < tổng). Không có điều này thì **không chứng minh được `:662`** ⇒ **Chưa chốt**, không được Pass |
| 🔴 Cấm | **KHÔNG sửa, KHÔNG xoá** `DN-XX-0005`, `HSPL-20260803-0001`, `HSPL-20260731-0002` và mọi bản ghi QA không tự tạo |

### Bộ lọc an toàn để cắt tập con (không phụ thuộc dữ liệu đối tác)

**Quy tắc: đọc bảng TRƯỚC, rồi chọn bộ lọc từ chính giá trị đọc được.** Không đoán.

1. **Ưu tiên *Loại hồ sơ*** — 2 bản ghi đã biết khác loại (`Khác` vs `Giấy chứng nhận`) ⇒ chọn 1 loại là cắt 2 → 1.
2. Nếu mọi dòng cùng loại: dùng **từ khóa** = chuỗi con của `mã hồ sơ` một dòng cụ thể (vd `20260731`), căn cứ `srs-fr-12:593` — keyword "Tìm theo **mã HS**, tên DN, tên HS".
3. Nếu vẫn không cắt được: dùng **Trạng thái**, hoặc **khoảng ngày hợp lệ** bao đúng một phần các dòng.
4. Ghi rõ vào báo cáo **đã lọc bằng gì, tập trước là gì, tập sau là gì**.

### Nếu thẻ không đủ 2 bản ghi

Theo thứ tự — **dừng ở bước nào đủ thì thôi**:
1. **Đổi sang DN khác đã có ≥2 hồ sơ** (mở màn danh sách DN, chọn DN có nhiều hồ sơ). **Vẫn là đọc, không ghi ⇒ ưu tiên tuyệt đối.**
2. Chỉ khi không DN nào đủ: dựng bằng **UI thật** — nút **[Thêm hồ sơ]** trên chính thẻ, tạo **1 bản ghi** với `Tên hồ sơ` mang dấu **`QA-W5-…`** (vd `QA-W5-HSPL-EXPORT`) và **`Loại hồ sơ` khác** với các dòng sẵn có (để chính nó là bộ lọc cắt tập con), các trường bắt buộc theo `srs-fr-12:577-587`. **Khai đủ vào báo cáo:** tạo bản ghi nào, trên DN nào, giá trị gì, env nào.
3. **Cấm** sửa bản ghi có sẵn của đối tác để tạo ra sự khác biệt cần thiết.

---

## 6. Chuẩn chấm

### 6.1 Ngưỡng "tối đa 10.000 dòng" — xử lý thế nào

`:663` yêu cầu "giới hạn tối đa 10.000 dòng". Env nghiệm thu **không thể** có > 10.000 hồ sơ pháp lý trên một DN, và seed tới ngưỡng đó là hành vi bị cấm trên env đối tác.

**Cách xử — bắt buộc làm đủ 3 ý:**
1. **Chấm theo phần đo được:** điều kiện quyết định của phiếu *"Xuất Excel thành công"* là **xuất được đúng cột + đúng bộ lọc**. Đo đủ phần này thì được Pass.
2. **Khai thẳng phần chưa đo** vào mục `⏸ CHƯA KIỂM TRA` của nội dung kết quả: *ngưỡng tối đa 10.000 dòng chưa kiểm được vì số hồ sơ trên môi trường thấp hơn ngưỡng rất nhiều; muốn kiểm phải dựng khối lượng dữ liệu lớn, không làm trên môi trường nghiệm thu.*
3. **Không** vì ngưỡng này mà chặn Pass, và **không** im lặng bỏ qua. Bỏ mục `⏸` = hồ sơ sai.

### ✅ PASS khi (phải đủ **tất cả**)
1. Từ chính thẻ Hồ sơ pháp lý, xuất được tệp `.xlsx` (`:665`).
2. **Lượt (a) không lọc:** tệp mở được; hàng tiêu đề **8 cột, đúng thứ tự** `:664`; thân tệp có **đúng số dòng** và **đúng danh sách mã** của tập đầy đủ đang hiển thị.
3. **Lượt (b) có lọc:** tệp mở được; hàng tiêu đề vẫn **8 cột đúng thứ tự**; thân tệp chứa **đúng tập con** sau khi lọc, **⊊** tập lượt (a), **không** lẫn bản ghi ngoài bộ lọc (`:662`).
4. Cả 2 lượt đều đối chiếu **theo tập mã**, không chỉ theo số lượng.
5. Đã khai `⏸ CHƯA KIỂM TRA` cho ngưỡng 10.000 dòng theo §6.1.
6. Vân tay bản dựng đầu case = cuối case.

### ❌ FAIL khi (chỉ cần **một**)
- Thẻ **không có** cách nào xuất Excel ⇒ đúng triệu chứng đối tác báo, Reopen ngay.
- Bấm mà **không** ra tệp, hoặc tệp hỏng / mở không được / không phải `.xlsx`.
- Hàng tiêu đề **thiếu cột**, **thừa cột**, hoặc **sai thứ tự** so với 8 trường `:664` — đặc biệt **thiếu *Doanh nghiệp*** hoặc **thiếu *Cơ quan cấp*** (2 cột có trong tệp theo `:664` nhưng vắng trên bảng màn hình).
- Thân tệp **lệch** tập đang hiển thị (sai số dòng **hoặc** sai danh sách mã).
- **Lượt (b): tệp chứa cả bản ghi ngoài bộ lọc** ⇒ vi phạm `:662` ⇒ Reopen.
- Tệp chứa hồ sơ của **DN khác** (vi phạm phạm vi `:661`).
- Lệnh xuất trả 4xx/5xx.

### 🚫 KHÔNG được chấm **Fail** vì
- **Nhãn cột trong tệp viết đầy đủ hơn `:664`.** `:664` viết tắt ("tên", "DN", "loại", "hết hạn"); phiếu đối tác viết đủ ("Tên hồ sơ", "Doanh nghiệp", "Loại hồ sơ", "Ngày hết hạn"). Chấm theo **đúng 8 trường + đúng thứ tự**, **KHÔNG** bắt khớp từng ký tự nhãn. SRS không quy định câu chữ tiêu đề cột.
- **Bảng trên màn có 10 cột** (thêm *Lĩnh vực pháp lý* · *Nguồn* · *Có tệp đính kèm*; thiếu *Doanh nghiệp* · *Cơ quan cấp*). C4 chấm **tệp**, không chấm bảng.
- **Vị trí / nhãn / hình dạng nút xuất** khác mong đợi — SRS không quy định (xem §2.1).
- Tên tệp, thứ tự dòng trong tệp, định dạng ngày trong ô — SRS không quy định ở `:657-665`.
- **Chưa chạm ngưỡng 10.000 dòng** — xem §6.1.
- Tệp có thêm sheet phụ / dòng tiêu đề trang trí phía trên, **miễn là** xác định được hàng tiêu đề 8 cột và thân tệp đúng tập.

### 🚫 KHÔNG được chấm **Pass** vì
- **Chỉ nhìn thấy nút *Xuất Excel* hiện trên thẻ** (quan sát tĩnh) — cấm tuyệt đối.
- **Chỉ thấy tệp tải về / chỉ thấy thông báo "Xuất Excel thành công"** mà **không mở nội dung tệp** — cấm tuyệt đối. Fix nút mà máy chủ sinh tệp sai là ca thường gặp.
- Chỉ chạy lượt (a) không lọc ⇒ **chưa chứng minh `:662`** ⇒ thiếu biến thể bắt buộc ⇒ **Chưa chốt**, không phải Pass.
- Lượt (b) lọc ra tập **bằng đúng** tập đầy đủ (bộ lọc không cắt gì) ⇒ không chứng minh được gì ⇒ **Chưa chốt**.
- Chỉ so **số dòng** mà không so **danh sách mã**.
- Bấm nút Xuất Excel của **màn danh sách DN** (`srs-fr-07:425`) và lấy tệp đó làm bằng chứng.
- Lấy kết quả Pass ở env nội bộ (bản dựng `V1.0.9`) làm căn cứ — khác env, khác bản dựng.
- Bấm lại cùng nút lần hai và coi đó là đối chứng độc lập.

---

## 7. Câu hỏi BA

**Không có.** Cả 5 vế con đều `MATCH`. Điểm nghi ngờ nặng nhất — *"`srs-fr-07:468` chỉ ghi CRUD, mà Xuất Excel không phải CRUD"* — đã được giải ở **§2.1**: khối `srs-fr-12:657-665` là thay đổi có chủ đích đã duyệt (`CHANGELOG:1577-1578`), còn ba chỗ im lặng (`srs-fr-07:468` · `srs-fr-12:563` Mô tả · `:703-714` Tiêu chí chấp nhận) đã được **chính SRS tự khai là thiếu sót biên tập chưa dọn** (`CHANGELOG:1651`, `:1658`, `:1659`, `:1661`), **không** phải quyết định bỏ chức năng. SRS **không im lặng** và **không tự mâu thuẫn** về nghĩa vụ xuất Excel ⇒ không đủ căn cứ để đẩy BA.

> Đề xuất cho BA/BA-editor (**không** chặn case này, **không** cần trả lời để chốt verdict): dọn nốt 2 gap `CHANGELOG:1658` và `:1659` — thêm "xuất Excel" vào phần **Mô tả** `srs-fr-12:563`, thêm tiêu chí chấp nhận cho "Xem chi tiết" và "Xuất Excel" vào `:703-714`, và bổ sung nội dung thẻ 2 ở `srs-fr-07:468` để lần sau không phải tra lại CHANGELOG mới kết luận được.
