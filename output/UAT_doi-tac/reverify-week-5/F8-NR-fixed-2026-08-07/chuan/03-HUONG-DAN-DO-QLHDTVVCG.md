# Hướng dẫn đo cụm 18 phiếu `QLHDTVVCG` — Giai đoạn B

Đọc **cùng với** [`00-BRIEF-CHUNG.md`](../00-BRIEF-CHUNG.md) (luật chung của lô) ·
[`QUYET-DINH-DIEU-PHOI.md`](../QUYET-DINH-DIEU-PHOI.md) (QĐ-01/02/03) ·
[`00-TONG-HOP-QLHDTVVCG.md`](00-TONG-HOP-QLHDTVVCG.md) (khóa chuẩn chấm — **CẤM sửa**) ·
[`02-SEED-HDTV.md`](02-SEED-HDTV.md) (dữ liệu nền đã dựng).

File này chỉ ghi thứ **riêng của cụm này**. Không lặp lại luật chung.

---

## 1. 🔴 Đường vào màn — đọc TRƯỚC KHI mở trình duyệt

**Sự thật đã đo bằng API lúc 13:1x ngày 07/08/2026** (phiên `cbnv_tw_03`, xem [`02-SEED-HDTV.md`](02-SEED-HDTV.md) §0):

```
GET /api/v1/hop-dong-tu-vans           (KHÔNG kèm ngữ cảnh) → 403 ERR-PERM-SYS-00-01
   "Hợp đồng tư vấn chỉ truy cập trong ngữ cảnh vụ việc/tư vấn viên/tổ chức."
GET /api/v1/hop-dong-tu-vans?tuVanVienId=<id>                → 200, n=3
GET /api/v1/hop-dong-tu-vans?vuViecId=<id>                   → 200
```

⇒ **403 là chốt chặn dev dựng CỐ Ý** theo `srs-fr-14-hop-dong-tv.md:266`/`:268`, **không phải lỗi phân quyền**
(cùng phiên, cùng tài khoản, thêm ngữ cảnh thì 200).

### Bắt buộc

1. **CẤM log 403 này thành bug phân quyền.** Ai định log phải đọc lại `:266`, `:268` trước.
2. Bước 1 của **cả 18 phiếu** ghi *"Chọn menu Hợp đồng Tư vấn"*. Menu này **không tồn tại theo thiết kế**.
   Đây là **tiền đề/đường đi**, **KHÔNG phải vế chấm** (không cột `Kết quả mong đợi` nào nhắc menu)
   ⇒ **không tách thành vế, không tự log bug, không FAIL phiếu vì không tìm thấy menu.**
3. **Ghi vào `do/<MÃ>.md` §Đường vào** đúng đường thực tế đã đi, kèm ảnh. Đây là dữ kiện cho câu hỏi BA
   §5.1 của file khóa — càng cụ thể càng tốt.

### Đường vào — đã dò sẵn bằng cách đọc bó mã giao diện (13:40 ngày 07/08/2026)

Đã tải khép kín **283 chunk** của bó `index-eWHwDgt2.js` và đọc bảng định tuyến. Kết quả:

**Bảng định tuyến module hợp đồng** (`index-DXkJqXjo.js`):

```js
<Route path="danh-sach" element={<Navigate to="/dashboard" replace/>} />   ← ĐÁ VỀ DASHBOARD
<Route path="tao-moi"   element={<Guard create HopDongTuVan><HopDongFormPage/></Guard>} />
<Route path=":id"       element={<Guard read   HopDongTuVan><TrangChiTiet/></Guard>} />
<Route path="*"         element={<Navigate to="/dashboard" replace/>} />
```

⇒ **`/hop-dong-tv/danh-sach` KHÔNG dựng màn nào** — chuyển hướng thẳng về `/dashboard`.
Đường 3 (gõ địa chỉ) **vô ích**, đừng mất thời gian.

**Hai đường vào của `:266` thì ĐỀU đã dựng thật:**

| # | Đường | Chunk | Chuỗi tìm được trong bó mã |
|---|---|---|---|
| **1** | Chi tiết **Vụ việc** → mục **"HĐ tư vấn liên kết"** | `index-B1e4Szfq.js` (55 KB) | `"HĐ tư vấn liên kết"` · `"Hợp đồng tư vấn liên kết"` · `"Vụ việc này chưa có hợp đồng tư vấn liên kết."` · `"Tạo hợp đồng"` · `"Xóa hợp đồng?"` · `"Không tìm thấy hợp đồng phù hợp"` |
| **2** | Chi tiết **Tư vấn viên** → mục **"Hợp đồng tư vấn"** | `index-BASfDqiz.js` (49 KB) | `"Hợp đồng tư vấn"` · `"Tư vấn viên chưa có hợp đồng tư vấn nào"` · `"Mã HĐ"` · `"Tên hợp đồng"` · **`"Trạng thái"` · `"Từ ngày"` · `"Đến ngày"`** · **`"Xuất Excel"`** · `"Xóa hợp đồng?"` |

**Cột bảng hợp đồng** (`columns-BLDPeyaL.js`) — khớp gần trọn `:288`:
`Mã hợp đồng · Tên hợp đồng · Bên A · Bên B · Giá trị (VNĐ) · Ngày bắt đầu · Ngày kết thúc · Vụ việc ·
Tiến độ TT · Hành động (Xem chi tiết / Sửa / Xóa)`; nhãn trạng thái `Nháp · Đang thực hiện · Tạm dừng ·
Hoàn thành · Hết hạn · Hủy`.

> 🔴 **Đây là TRINH SÁT, KHÔNG phải phép đo.** Đọc chuỗi trong bó mã **không** chứng minh màn chạy đúng —
> flow 04 cấm Pass bằng quan sát tĩnh. Dùng nó để **biết đi đâu**, rồi **đo thật trên giao diện**.
> Cũng chưa chắc `"Từ ngày"/"Đến ngày"/"Trạng thái"` thuộc đúng mục hợp đồng (chunk chi tiết TVV có nhiều
> mục khác) — **phải nhìn tận mắt**.

### 🔴 ĐÃ ĐO THẬT 14:20–14:26 ngày 07/08/2026 — **có HAI màn hợp đồng khác nhau, không phải một**

Đợt A đã xác nhận bằng mắt: thanh bên **không** có mục "Hợp đồng Tư vấn" (đã liệt kê trọn 14 mục).

| | **MÀN 1** — Chi tiết **Vụ việc** → "HĐ tư vấn liên kết" | **MÀN 2** — Chi tiết **TVV** → tab "Lịch sử hỗ trợ" → "Hợp đồng tư vấn" |
|---|---|---|
| API | `GET /hop-dong-tu-vans?vuViecId=…` | `GET /hop-dong-tu-vans?tuVanVienId=…` |
| Thanh lọc | **3 nhóm** — từ khóa (*"Tìm theo tên HĐ, mã HĐ, bên B"*) + **chọn tư vấn viên** + Từ ngày/Đến ngày + [Tìm kiếm] [Xóa bộ lọc] | **2 nhóm** — từ khóa + Từ ngày/Đến ngày (không có ô chọn TVV — hợp lý vì đã ở trong ngữ cảnh TVV) |
| Nút | [Xuất Excel] (mờ khi bảng rỗng) · **[+ Tạo hợp đồng]** | **chỉ** [Xuất Excel] — **không có nút tạo** |
| Bảng | **11 cột** (10 cột của `:288` + thêm **Trạng thái**) | **6 cột** — thiếu Bên A · Bên B · Giá trị · Số VV · Tiến độ TT |
| Hành động | Xem chi tiết / Sửa / Xóa | Xem chi tiết / Sửa / Xóa |
| Phân trang | chưa rõ (bảng rỗng lúc đo) | có (`1-3 / 3 mục`) |

**⇒ BỀ MẶT CHẤM CHÍNH THỨC = MÀN 1**, vì bộ lọc khớp **chính xác** `:287` (*"Full-text: tên HĐ, mã HĐ,
bên B. TVV (searchable). Khoảng ngày"*) và đây là nơi **duy nhất** tạo được hợp đồng.
Mỗi `do/<MÃ>.md` phải ghi **đã chấm trên màn nào và vì sao**.
Màn 2 **không bỏ qua**: ghi lại thành phần quan sát được làm dữ kiện cho câu hỏi BA §5.1 —
**không chấm, không log bug vì nó thiếu cột**.

### 🔴 LUẬT CHUNG — thiếu thành phần "chỉ màn độc lập mới có" **KHÔNG phải lỗi dev**

Áp cho **mọi vế** dựa vào bảng thành phần `:278`–`:289` (nặng nhất là `_02` C1, còn đụng `_08` · `_09` · `_16`).

Năm vùng mà `:278` khai: `:285` breadcrumb *"Trang chủ > Tư vấn > Hợp đồng tư vấn"* · `:286` tiêu đề trang
*"Quản lý Hợp đồng Tư vấn"* + `[+ Thêm hợp đồng] [Xuất Excel] [Làm mới]` · `:287` thanh lọc 3 nhóm ·
`:288` bảng 10 cột · `:289` phân trang 20 mục/trang.

**Ba trong năm vùng** (`:285` breadcrumb, `:286` tiêu đề trang, `:289` phân trang riêng) là thành phần của
một **màn độc lập** — thứ mà `:266`/`:268` đã **quyết bỏ**. Một mục accordion nằm trong màn khác **không thể
có chúng theo bản chất kiến trúc**.

⇒ Khi thành phần thiếu thuộc nhóm này:
- **CẤM** viết *"thiếu nút Làm mới ⇒ lỗi"* / *"sai số cột ⇒ lỗi"* / kết `Reopen`.
- Ghi vế đó **"không chấm được — chuẩn đo đang tranh chấp"**, nêu rõ lý do, ghi **đầy đủ hiện trạng đối chiếu
  từng vùng** (có gì / thiếu gì / khác gì) làm dữ kiện cho BA.
- Báo dev sửa theo một bảng thành phần đang tranh chấp là **báo sai việc**.

### Ngữ cảnh vào màn

- **Màn 1:** vào từ vụ việc **đã có hợp đồng liên kết** — sau `_15` thì HĐ-1 sẽ nằm ở các vụ việc đã chọn.
- **Màn 2:** TVV `Chuyên gia UAT QLNDTVVCG 38` (3 hợp đồng seed) hoặc `QA TVV PheDuyet TW R19` (2 hợp đồng).

> ⚠️ **Hụt tiền đề dễ gặp:** `HDTV-20260807-0003` (kết thúc 25/08/2026, rơi đúng ngưỡng ≤30 ngày của `:288`)
> chỉ gắn **tư vấn viên**, **không** gắn vụ việc ⇒ **không hiện trên màn 1**. Vì vậy **HĐ-1 tạo ở `_15`
> BẮT BUỘC đặt ngày kết thúc trong vòng 30 ngày**, nếu không sẽ không có dòng nào để đo vế tô đỏ trên màn 1.

### Nếu KHÔNG đường nào vào được

Ghi phiếu đó **Chưa chốt** (ô `R` giữ nguyên `Fixed`, **không ghi** `Test done`/`Reopen`/`BA confirm`),
nêu rõ đã thử những đường nào + ảnh từng đường, rồi **chạy tiếp phiếu sau** — không dừng cả cụm.

---

## 2. Việc ĐẦU TIÊN sau khi vào được màn — chụp và ghi rõ thành phần

Chốt bằng mắt (bó mã chỉ là gợi ý), rồi báo lại ngay cho điều phối:

- [ ] thanh lọc: từ khóa · trạng thái · khoảng ngày → `_02` · `_03` · `_04` · `_05`
- [ ] nút `[Xuất Excel]` → `_16`
- [ ] nút thêm mới (bó mã ghi **"Tạo hợp đồng"**, phiếu ghi `[+ Thêm hợp đồng]`) → `_13` · `_15`
- [ ] cột `Hành động` có Xem chi tiết / Sửa / Xóa → `_08` · `_19` · `_17` · `_18`
- [ ] phân trang

Thiếu thành phần nào ⇒ phiếu tương ứng ghi **Chưa chốt** kèm ảnh, **không** đoán, **không** FAIL vống.

> ⚠️ **Nhãn nút lệch không phải lý do FAIL.** Bó mã dùng *"Tạo hợp đồng"*, đặc tả `:286` ghi
> *`[+ Thêm hợp đồng]`*. Cột `Kết quả mong đợi` của `_13`/`_15` **không chấm nhãn nút** ⇒ đừng FAIL vì chữ.

---

## 3. Dữ liệu đã có sẵn (đừng dựng lại)

5 hợp đồng nền — chi tiết ở [`02-SEED-HDTV.md`](02-SEED-HDTV.md) §3:

| Mã | Nhãn | Dùng cho | Lưu ý |
|---|---|---|---|
| `HDTV-20260807-0001` | HĐ-2 | **`_17`** xóa mềm | **CỐ Ý 0 vụ việc** — đừng gắn vụ việc vào nó |
| `HDTV-20260807-0002` | HĐ-3 | **`_22` C5** | gắn chéo cùng 1 vụ việc với HĐ-1 |
| `HDTV-20260807-0003` | HĐ-4 | `_02` C3 | kết thúc **2026-08-25** (≤30 ngày → `:288` tô đỏ) |
| `HDTV-20260807-0004` | HĐ-5 | lọc trạng thái | `HOAN_THANH` |
| `HDTV-20260807-0005` | HĐ-6 | `_03` | cùng từ khóa *"sở hữu trí tuệ"* với HĐ-3 |

**Ngữ cảnh vào được:** TVV `Chuyên gia UAT QLNDTVVCG 38` (`38383838-0000-4000-8000-000000000038`) → 3 hợp đồng ·
TVV `QA TVV PheDuyet TW R19` (`aaaa1707-0000-4000-8000-000000000d01`) → 2 hợp đồng.

**Vụ việc tên DN > 40 ký tự** (cho `_09` C4): `VV-BTP-TW-20260804-002` / `-003` / `-004`.

**Tệp đính kèm thật** (D8) — `files/fixture-hdtv/`: `phu-luc-hop-dong.pdf` · `bien-ban-thoa-thuan.docx` ·
`bang-tien-do.xlsx` · `so-do-quy-trinh.png`. Đã kiểm bằng `file` (chữ ký nhị phân) + mở đọc lại bằng
thư viện tương ứng. **Dùng đúng bộ này, đừng tạo tệp đổi đuôi.**

**Từ khóa cho `_03`:** `sở hữu trí tuệ` → khớp **2** (HĐ-3, HĐ-6), loại 3. Cho `_04`: chuỗi vô nghĩa (vd `zzqq`).
⚠️ Ô tìm kiếm quét trường nào là thứ `_03` phải **đo**, không được giả định.

---

## 4. HĐ-1 **phải tạo bằng giao diện thật** ở phiếu `_15`

Đã cố ý **không** seed HĐ-1 bằng API: *tạo hợp đồng chính là hành động đang tranh chấp* của `_15`.
Nhìn một bản ghi seed sẵn rồi chấm `_15` = **Pass bằng quan sát tĩnh** — đúng thứ yêu cầu cấm.

Khi chạy `_15`, nhập **đủ 4 nhóm con trong một lượt** để dựng luôn D2+D3+D4:

- Tên **> 30 ký tự** · Giá trị > 0 (ghi lại con số) · Nội dung · Ghi chú
- Thời hạn: **1 mốc kết thúc ≤ 30 ngày** (để đo `:288`)
- **≥1 tệp đính kèm** từ `files/fixture-hdtv/`
- **≥2 vụ việc liên kết**, trong đó ≥1 dùng `VV-BTP-TW-20260804-002/003/004`

---

## 5. Ba đợt chạy (giữ nguyên ràng buộc thứ tự đã khóa)

Ràng buộc cứng: `_15` → (`_22` → `_09`) · `_22` → `_23` · `_18` **trước** `_23` · `_26` → `_27` ·
`_21` sau khi HĐ-1 đủ 4 nhóm con · `_17` **cuối cùng** (xóa mềm thật).

| Đợt | Phiếu (đúng thứ tự) | Mục tiêu |
|---|---|---|
| **A** | `_13` → `_15` → `_02` → `_03` → `_04` → `_05` | xác lập đường vào + tạo HĐ-1 + cụm đọc/lọc |
| **B** | `_16` → `_08` → `_19` → `_22` → `_09` → `_24` | xuất Excel + chi tiết + liên kết vụ việc |
| **C** | `_26` → `_27` → `_21` → `_18` → `_23` → `_17` | nhóm con thanh toán + sửa + phá tiền đề |

Đợt A **bắt buộc** báo lại kết quả mục §2 (hình thái màn) trước khi đợt B chạy — nó quyết định
`_16` và các phiếu chi tiết có đo được không.

---

## 5b. 🔴 Rủi ro dây chuyền — phép đo `_22` C5 có thể **cướp mất tiền đề của `_18`**

Điều phối đã tự mở file đọc lại và xác nhận mâu thuẫn:

| Dòng | Nói gì | Nghĩa |
|---|---|---|
| `:90` | `vu_viec_ids · identifier[] · FK[] -> VU_VIEC (many-to-many)` | một vụ việc **được** thuộc nhiều hợp đồng |
| `:291` | *"Nút [+ Liên kết VV] -> modal multi-select. **N:N**"* | như trên |
| `:373` | `VU_VIEC }o--o| HOP_DONG_TU_VAN : "hop_dong_tv_id"` | **nhiều vụ việc → MỘT hợp đồng** |
| `:352`, `:424` | khoá ngoại `hop_dong_tv_id` **đặt trên `VU_VIEC`** (một cột, một giá trị) | một vụ việc chỉ giữ được **một** hợp đồng |

**Hệ quả cần đề phòng:** nếu bản dựng theo `:373`/`:424` (một khoá ngoại), thì thao tác `_22` C5 —
gắn **cùng một vụ việc** sang HĐ-3 — nhiều khả năng **gỡ vụ việc đó khỏi HĐ-1** thay vì tạo liên kết thứ hai.
Mà HĐ-1 **phải còn ≥1 vụ việc liên kết** thì `_18` (đợt C) mới đo được vế *"xóa hợp đồng đang có vụ việc
liên kết phải bị chặn"*. `_22` chạy ở **đợt B**, `_18` ở **đợt C** ⇒ hỏng thì phát hiện rất muộn.

**Bắt buộc khi chạy `_22` C5:**

1. **Trước** khi gắn chéo: đọc và **ghi lại** danh sách vụ việc liên kết của HĐ-1 (số lượng + mã từng vụ việc).
2. Gắn chéo **đúng MỘT** vụ việc, chọn cái mà **HĐ-1 còn dư ra** (vì `_15` đã gắn ≥2).
3. **Sau** khi gắn: đọc lại HĐ-1, ghi rõ **còn mấy vụ việc**. Kết quả này chính là bằng chứng của C5 —
   *"vụ việc bị chuyển đi"* hay *"vụ việc thuộc cả hai"* là hai kết luận trái ngược, và đây là phép đo
   duy nhất phân biệt được.
4. Nếu HĐ-1 **còn 0 vụ việc** ⇒ **gắn bù ngay một vụ việc khác** bằng chính chức năng liên kết, khai rõ là
   dựng lại tiền đề, để `_18` còn đo được.

---

## 5c. Manh mối cho `_21` C3 (đợt C) — cách lưu nhóm con trong dữ liệu

Điều phối đã tự mở file đọc lại bảng thực thể:

| Dòng | Khai gì |
|---|---|
| `:394` | `moc_tien_do · **text (long)** · N · … · "Mốc tiến độ (**JSON array**)"` |

⇒ Cả danh sách mốc nằm trong **một cột duy nhất** dưới dạng mảng JSON. Với kiểu lưu này, lưu bản sửa
thường **ghi đè nguyên mảng** (thay thế) chứ không trộn từng phần tử — đúng thứ `_21` C3 đang hỏi
(`:122` chỉ nói *"cập nhật"*, `:123` nói *"tạo"*, không nói rõ thay thế hay cộng dồn).

**Đây là manh mối để biết đo gì, KHÔNG phải kết luận** — và theo luật khóa 5 nó **không** đổi được
`GAP` → `MATCH`. Cách đo đúng ở `_21`: ghi lại số phần tử **từng nhóm con trước khi sửa**, sửa **bớt đi
một phần tử** của một nhóm, lưu, rồi đọc lại **cả 4 nhóm** — phần tử bị bỏ có biến mất không, và các nhóm
**không đụng tới** có bị xóa lây không. Hai câu trả lời đó phân biệt "thay thế" với "cộng dồn".

---

## 6. Bẫy riêng của cụm này

| Bẫy | Vì sao | Cách tránh |
|---|---|---|
| FAIL vì **không thấy menu** | menu bị bỏ theo thiết kế | §1 — tiền đề, không phải vế |
| Log **403** thành bug quyền | là chốt chặn cố ý | §1 — cùng phiên + ngữ cảnh trả 200 |
| Hạ `DIFF`/`GAP` → `MATCH` vì *"web làm đúng kỳ vọng rồi"* | 12/18 phiếu có `DIFF`/`GAP` ⇒ **CẤM Pass** | luật khóa 5 — chỉ **dòng SRS mới đọc được** mới đổi được quan hệ |
| FAIL `_15`/`_21` vì **không quay về danh sách** | `:175` + `:187` nói *"quay về ngữ cảnh đã mở nó"*, và ghi rõ đây là **biến thể hợp lệ** của quy ước H7 | đây là vế `DIFF` — route BA, **không** FAIL |
| FAIL `_26` vì **thanh tiến trình không tự cộng** | `:301` + `:112` — chỉ dòng **đã thanh toán** mới tính, dòng mới mặc định `CHUA_THANH_TOAN` | vế `DIFF` — route BA |
| Chấm `_16` đạt vì **tệp tải về được** | khuôn tên tệp `srs-v3.5.md:6760` bỏ **mọi** dấu gạch nối, PascalCase | **mở tệp bằng `openpyxl`** đọc nội dung; ghi **nguyên văn tên tệp** nhận được |
| Xóa HĐ-2 sớm | mất bản ghi của phiếu khác | `_17` chạy **cuối cùng** |
| Ghi đè ô người khác vừa sửa | **có phiên khác đang ghi cùng bảng** (đã thấy lượt ghi dòng 291 lúc 13:32 của Flow 03) | **luôn** truyền `--expect-file`; lệch ⇒ đọc lại dòng rồi mới quyết |

---

## 7. Nhắc về ô `Trạng thái dev fix`

Chỉ ba giá trị: **`Test done`** (Pass) · **`Reopen`** · **`BA confirm`** (cần BA).
Giá trị `UAT done` thấy ở dòng 291 là của **quy trình khác** (Flow 03, env nghiệm thu) — **không dùng cho lô này**.

Phiếu **Chưa chốt** ⇒ **không ghi ô `R`**, chỉ ghi ô `T` nêu rõ vì sao chưa đo được và cần gì.

---

## 8. 🔴 Chế độ rút gọn — áp dụng từ **15:40 ngày 07/08/2026**, đợt B và C

Người chủ trì yêu cầu bỏ công sức đổ vào chỗ **không đổi được kết quả ghi bảng**. Mục này thay thế
cách làm cũ. **Không làm lại các phiếu đã đóng** (`_13` `_15` `_02` và đợt A).

### 8.1 Vế `DIFF` / `GAP` — KHÔNG đo, viết thẳng câu hỏi BA

Quan hệ đã khóa ở [`00-TONG-HOP-QLHDTVVCG.md`](00-TONG-HOP-QLHDTVVCG.md). Với vế đã khóa `DIFF`/`GAP`,
ô `R` là `BA confirm` **bất kể phần mềm làm gì** ⇒ đo để chấm là công vô ích.

| Bỏ | Giữ |
|---|---|
| ✂ Đường đo thứ hai / đối chứng độc lập | ✅ Viết câu hỏi BA theo mẫu §5.2–5.4 của file khóa |
| ✂ Dựng thêm dữ liệu, đổi trạng thái, tạo bản ghi **chỉ để** nhìn thấy vế đó | ✅ Nếu vế đó **nhìn thấy ngay trên màn đang đứng** (đã mở để đo vế `MATCH`): liếc + **1 ảnh** |
| ✂ Phân tích dài trong `do/` | ✅ Ghi 1 dòng bảng: thao tác · web hiện ra gì · ảnh |

**Vì sao vẫn giữ một cái liếc:** mẫu câu hỏi BA đã chốt có **ba vế** — *đối tác mong X · đặc tả quy định Y
(`file:dòng`) · **web hiện tại làm Z***. Vế Z quyết định BA trả lời ra sao: web làm **giống đối tác** ⇒ việc
cần làm là **bổ sung đặc tả** (rẻ); web làm **giống đặc tả** ⇒ mới là chuyện **đổi mã** (đắt). Thiếu Z, BA
nhận câu hỏi không quyết được. Mà phiếu **đằng nào cũng đã mở màn đó** để đo vế `MATCH` ⇒ chi phí ≈ 0.

**Khi phải dựng thêm mới thấy được vế đó ⇒ BỎ.** Viết câu hỏi BA **thiếu vế Z**, ghi rõ trong ô `T`:
*"chưa đo hiện trạng phần này"*. Cấm đoán Z.

### 8.2 Vế `MATCH` — KHÔNG CẮT GÌ

**Cả 18 phiếu đều có ≥1 vế `MATCH`** (thấp nhất `_23`, `_27` = 1 vế) ⇒ **không phiếu nào bỏ được lượt mở màn.**
Còn lại **32 vế `MATCH`** phải chạy **trọn luồng**, đủ 2 đường đo, đủ bằng chứng. Đây là những vế duy nhất
quyết định `Test done` hay `Reopen`. Yêu cầu gốc của người chủ trì vẫn nguyên hiệu lực:

> 🔴 CẤM Pass bằng quan sát tĩnh. Phải chạy hết luồng — sửa thêm giao diện mà xử lý bên trong vẫn hỏng là chuyện thường.

### 8.3 Bỏ phần tài liệu làm quá

| Bỏ / dừng | Giữ nguyên chất lượng |
|---|---|
| ✂ Không viết thêm tệp `BAN-GIAO-*.md` | ✅ `note/<MÃ>.txt` — **đây là sản phẩm giao**, nghiệp vụ và dev đọc, không phải chỗ tiết kiệm |
| ✂ Không thêm mục `QĐ-*` trừ khi có quyết định **thật sự đổi cách làm** | ✅ [`00-TONG-HOP-QLHDTVVCG.md`](00-TONG-HOP-QLHDTVVCG.md) — chuẩn chấm đã khóa, **CẤM sửa** |
| ✂ `do/<MÃ>.md` rút từ ~20 KB xuống **một bảng** + ảnh (mẫu §8.4) | ✅ `audit/` — bản chụp ô cũ trước khi ghi đè (đã xong, không đụng) |
| ✂ Không mở rộng file hướng dẫn này nữa | ✅ `--expect-file` mỗi lần ghi bảng (QĐ-02) |

### 8.4 Khuôn `do/<MÃ>.md` mới

```markdown
# <MÃ> — dòng <N>   ·   <ngày giờ> · tài khoản <username> · bản dựng <index-*.js>

## Đường vào
<1–2 dòng> + ảnh

## Kết quả từng vế
| Vế | Quan hệ | Kỳ vọng phiếu | Web thực tế | Đạt? | Ảnh |
|---|---|---|---|---|---|
| C1 | MATCH | … | … | ✅/❌ | … |
| G1 | GAP   | … | … | — (không chấm) | … |

## Verdict → ô R
<Test done | Reopen | BA confirm> — theo QĐ-01

## Dữ liệu đã đổi
<bản ghi nào bị tạo/sửa/xóa — cho phiếu sau biết>
```

**Không cắt:** vẫn **đóng từng phiếu một** (đo → `do/` → `note/` → ghi bảng → **đọc lại xác nhận**) rồi mới
sang phiếu kế. Gom nhiều phiếu ghi một lượt đã từng làm mất trắng công — cấm lặp lại.
