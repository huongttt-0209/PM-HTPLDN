# Nhật ký đo — `QLHDTVVCG_02` (dòng 308 tab `bug`)

**Ngày:** 2026-08-07 · **Quy trình:** [`flows/04-verify-bug-dev-fix-khong-ho-so.md`](../../../../../flows/04-verify-bug-dev-fix-khong-ho-so.md)
**Chuẩn chấm đã khóa (Giai đoạn A — CẤM sửa):** [`chuan/QLHDTVVCG_02.md`](../chuan/QLHDTVVCG_02.md) — 5 vế: **C1 `MATCH`** · **C2 `GAP`** · **C3 `MATCH`** · **C4 `GAP`** · **C5 `MATCH`** → route **BA**.

---

## 0. Đọc lại dòng phiếu trên bảng trước khi đo (bắt buộc)

Đọc lúc **15:1x ngày 07/08/2026** bằng `tools/sheet_dump_bug_rows_2026-08-07.py --rows 308` (chỉ đọc).

| Ô | Giá trị đọc được |
|---|---|
| `Mã TC` (D) | `QLHDTVVCG_02` |
| `Trạng thái` (N) `N/R` · `Dopai` (O) `N/R` | phiếu **chưa từng chạy** |
| `Kết quả thực tế` (L) · `Ảnh/vieo 1` (M) · `TKM phản hồi lần 1` (Q) | **RỖNG cả ba** |
| `Trạng thái dev fix` (R) | `Fixed` |
| `Kết quả verify` (T) | **RỖNG** |
| `Kết quả mong đợi` (K) | `- Hệ thống hiển thị các trường thông tin giống với thiết kế` / `- Dữ liệu hiển thị đúng định dạng và trường thông tin` / `- Dữ liệu hiển thị không bị tràn/đè lên nhau, đồng nhất ngôn ngữ hiển thị` |
| `DEV phản hồi lần 1` (S) | *"BA chốt 06/08/2026 … quyết định BA ngày 11/05/2026 (bỏ menu riêng cho Hợp đồng tư vấn) vẫn giữ nguyên, phần mềm đang đúng bản gốc; vật cản là bộ test case mô tả một lối vào đã hết hiệu lực — hợp đồng truy cập từ Chi tiết Vụ việc hoặc Lịch sử TVV. … Phần nội dung chức năng Dev đã bổ sung theo SRS: bộ lọc ngữ cảnh cho màn danh sách hợp đồng."* |

Không có phiên khác vừa ghi dòng 308.

## 1. Môi trường + vân tay bản dựng

| Hạng mục | Giá trị |
|---|---|
| Môi trường | `https://18.143.165.120.nip.io` — env **NỘI BỘ** |
| **Vân tay ĐẦU phiên** (14:14:57) | `assets/index-BbPPdate.js` · `assets/index-DVlgOkLg.css` · `last-modified: Fri, 07 Aug 2026 06:47:57 GMT` · `etag "6a757f9d-428"` |
| Tài khoản đo | **`cbnv_tw_03`** / `Test@1234` — vai trò **CB NV TW**, bắt buộc theo `:68` + `:286` (nút thêm chỉ hiện với CB NV). Không gặp `ERR-AUTH-SYS-00-03`, không fallback. |
| Cửa sổ | **1440×900** — ghi rõ vì `srs-fr-05-vu-viec.md:1603` chỉ bảo đảm tối thiểu 1024×768 |
| Thời điểm đo | 15:0x–15:2x ngày 07/08/2026 |

## 2. Bề mặt đã chấm — **MÀN 1**, và vì sao

Theo chỉ đạo điều phối 07/08/2026: bề mặt chấm chính thức của cả đợt A là **MÀN 1** =
**Chi tiết Vụ việc → mục "HĐ tư vấn liên kết"**.

**Lý do chọn Màn 1:**
1. Thanh lọc của nó **khớp `:287` từng ý**: ô tìm toàn văn (*"Tìm theo tên HĐ, mã HĐ, bên B"*) + chọn tư vấn viên (có tìm) + khoảng ngày.
2. Đây là **nơi duy nhất** có nút mở biểu mẫu thêm hợp đồng (`:286`).
3. **Không tồn tại màn danh sách hợp đồng độc lập** — `:266`/`:268` bỏ nó theo quyết định BA 11/05/2026.

**Màn 2** (Chi tiết Tư vấn viên → mục "Hợp đồng tư vấn") **được ghi lại làm dữ kiện cho câu hỏi BA §5.1,
KHÔNG chấm, KHÔNG log bug vì nó thiếu cột** — xem §7.

## 3. Tiền đề đã dựng

| Yêu cầu của chuẩn chấm | Đã có |
|---|---|
| ≥1 hợp đồng trong phạm vi | **2** hợp đồng trên Màn 1 của vụ việc `VV-BTP-TW-20260804-002` |
| ≥1 HĐ đủ chất: giá trị > 0 · có 2 mốc thời hạn · ≥1 vụ việc liên kết · ≥1 giai đoạn **đã thanh toán** | ✅ đủ (xem bảng dưới) |
| ≥1 HĐ **kết thúc ≤ 30 ngày** (để đo vế tô đỏ `:288`) | ✅ `HDTV-20260807-0006` kết thúc **25/08/2026** = **18 ngày** |
| ≥1 HĐ **kết thúc > 30 ngày** (để chứng minh quy tắc có điều kiện, không tô đỏ tất) | ✅ `HDTV-20260807-0007` kết thúc **30/12/2026** = **145 ngày** |
| ≥1 HĐ **tên > 30 ký tự** (cho C4) | ✅ cả hai: **85** và **79** ký tự |

| Mã | Tên (số ký tự) | Bên B | Giá trị | Bắt đầu → Kết thúc | Số VV | Tiến độ TT |
|---|---|---|---|---|---|---|
| `HDTV-20260807-0006` | *Hợp đồng tư vấn xác lập quyền sở hữu trí tuệ và nhãn hiệu cho doanh nghiệp nhỏ và vừa* (85) | Chuyên gia UAT QLNDTVVCG 38 | 250.000.000 | 07/08/2026 → **25/08/2026** | 3 | 0% |
| `HDTV-20260807-0007` | *Hợp đồng tư vấn pháp luật lao động và bảo hiểm xã hội cho doanh nghiệp siêu nhỏ* (79) | QA TVV PheDuyet TW R19 | 200.000.000 | 07/08/2026 → **30/12/2026** | 1 | 25% |

> `HDTV-20260807-0007` do **lượt đo này dựng bằng giao diện** làm tiền đề — khai đầy đủ ở §8.

## 4. Đo từng vế

### C1 — "hiển thị các trường thông tin giống với thiết kế" · `MATCH` · 🔴 **KHÔNG CHẤM ĐƯỢC — chuẩn đo đang tranh chấp**

> 🔴 **CẤM kết "thiếu thành phần ⇒ Reopen".** Đây là bẫy nặng nhất của cụm. Bảng thành phần `:278`–`:289` mô tả
> một **MÀN DANH SÁCH ĐỘC LẬP**. Chính `:266`/`:268` đã **bỏ màn đó** theo quyết định BA 11/05/2026. Một mục
> nằm bên trong màn khác **về kiến trúc không thể có** breadcrumb riêng, tiêu đề trang riêng, phân trang riêng.
> Báo dev sửa theo một bảng thành phần đang tranh chấp là **báo sai việc**.

**Đối chiếu từng vùng — dữ kiện cho BA, KHÔNG phải kết luận đúng/sai:**

| # | Vùng `:278` | Đặc tả khai | Màn 1 thực tế | Nhận định |
|---|---|---|---|---|
| 1 | Breadcrumb (`:285`) | *"Trang chủ > Tư vấn > Hợp đồng tư vấn"* | Đường dẫn của màn là **"Trang chủ / Vụ việc hỗ trợ pháp lý / Chi tiết"** | Thứ **chỉ màn độc lập mới có** |
| 2 | Tiêu đề + 3 nút (`:286`) | *"Quản lý Hợp đồng Tư vấn"* + `[+ Thêm hợp đồng]` `[Xuất Excel]` `[Làm mới]` | Tiêu đề khối **"Hợp đồng tư vấn liên kết"**; có **[+ Tạo hợp đồng]** và **[Xuất Excel]**; **không có [Làm mới]**, thay bằng **[Xóa bộ lọc]** | Tiêu đề **trang** là thứ chỉ màn độc lập mới có; 2/3 nút có |
| 3 | Thanh lọc (`:287`) | Toàn văn: tên HĐ, mã HĐ, bên B · TVV (có tìm) · khoảng ngày | **Khớp từng ý**: ô *"Tìm theo tên HĐ, mã HĐ, bên B"* · ô *"Chọn tư vấn viên"* (gõ để tìm) · *"Từ ngày"* + *"Đến ngày"* · [Tìm kiếm] [Xóa bộ lọc] | **Đủ** |
| 4 | Bảng 10 cột (`:288`) | Mã HĐ · Tên HĐ · Bên A · Bên B · Giá trị · Thời hạn bắt đầu · Thời hạn kết thúc · Số VV · Tiến độ TT · Hành động | **11 cột**: Mã hợp đồng · Tên hợp đồng · Bên A · Bên B · Giá trị (VNĐ) · Ngày bắt đầu · Ngày kết thúc · Vụ việc · Tiến độ TT · **Trạng thái** · Hành động | **Đủ 10 cột + thừa 1 cột "Trạng thái"**. `:288` liệt kê thành phần **bắt buộc có**, không tuyên bố cấm thêm ⇒ thừa **không phải lỗi** |
| 5 | Phân trang (`:289`) | 20 mục/trang | **Có** — *"1-2 / 2 mục"*, chọn *"20 / trang"*, nút trái/phải | **Đủ** (mặc định đúng 20) |

⇒ **3 trong 5 vùng (1, 2 phần tiêu đề trang, và nút [Làm mới]) là hệ quả của quyết định bỏ màn độc lập, KHÔNG
phải lỗi dev.** Hai vùng còn lại (3, 4, 5) **đủ và đúng**.
⇒ **C1 KHÔNG CHẤM ĐƯỢC** cho tới khi BA trả lời: *"bảng thành phần `:278`–`:289` áp cho màn nào?"*

**Nguyên tắc chung suy ra (áp cho cả đợt B và C):** khi vế chấm dựa vào `:278`–`:289` mà thành phần thiếu là
thứ **chỉ màn độc lập mới có** (breadcrumb / tiêu đề trang / phân trang riêng / nút [Làm mới]), thì đó là
**hệ quả của quyết định bỏ màn độc lập**, KHÔNG phải lỗi dev.

### C2 — "giống với **thiết kế**" ở mức bố cục/kiểu control · `GAP` · ❓ **CHỈ GHI HIỆN TRẠNG, CẤM Pass/Reopen**

`:274` trỏ ra bản vẽ `dac-ta-man-hinh-chuc-nang-v2.md -- MH-14.1`; **bản vẽ này không có trong nguồn chuẩn
prompt cấp** ⇒ **không có căn cứ chấm** bố cục, thứ tự, khoảng cách, màu sắc, kiểu control.

**Hiện trạng ghi lại bằng ảnh** (ảnh 03 và 04): thanh lọc xếp 1 hàng 4 ô + hàng nút bên dưới; bảng dùng cuộn
ngang trong khung (`1700px` nội dung / `972px` khung nhìn) chứ không ép cột; phân trang ở góc phải dưới;
nút hành động là biểu tượng.

**CÂU HỎI CHO BA:** đề nghị **cung cấp bản vẽ MH-14.1** hoặc **xác nhận không dùng bản vẽ làm chuẩn nghiệm thu**
cho nhóm màn hợp đồng. Chưa có bản vẽ thì mọi khác biệt về bố cục **không có căn cứ để kết luận**.

### C3 — "Dữ liệu hiển thị đúng định dạng và trường thông tin" · `MATCH` · ✅ **ĐẠT**

**Đường 1 — giao diện, đọc `innerText` + kiểu dựng của từng ô** (2 dòng thật, không phải bảng rỗng):

| Cột `:288` / Outputs `:147`–`:155` | Định dạng đặc tả đòi | `HDTV-…-0007` | `HDTV-…-0006` | Kết luận |
|---|---|---|---|---|
| Mã HĐ | `HDTV-{date}-{seq}` | `HDTV-20260807-0007` | `HDTV-20260807-0006` | ✅ |
| Giá trị | **format tiền VND** | `200.000.000 VNĐ` | `250.000.000 VNĐ` | ✅ dấu chấm nghìn + đơn vị |
| Thời hạn bắt đầu | `dd/mm/yyyy` | `07/08/2026` | `07/08/2026` | ✅ |
| Thời hạn kết thúc | `dd/mm/yyyy` + **đỏ nếu ≤ 30 ngày** | `30/12/2026` — màu thường `rgb(31,31,31)`, **không** bọc thẻ màu | `25/08/2026` — `<span style="color: rgb(255,77,79); font-weight:600">` = **ĐỎ + đậm** | ✅ **có điều kiện đúng**: chỉ dòng ≤30 ngày mới đỏ |
| Số VV liên kết | **badge** | `<span class="ant-badge">` chấm tròn xanh số **1** | badge số **3** | ✅ đúng kiểu badge |
| Tiến độ TT | **progress bar %** | `<div class="ant-progress" role="progressbar">` + chữ **25%**, thanh có phần lấp đầy | cùng kiểu, **0%**, thanh rỗng | ✅ |
| Hành động | CB NV thấy Xem/Sửa/Xóa | 3 nút biểu tượng `aria-label` = *Xem chi tiết* / *Sửa* / *Xóa* | như trên | ✅ (Phụ lục E §H6 cho phép biểu tượng + gợi ý thay vì chữ) |

**Đường 2 — đối chứng độc lập, đọc giá trị thô của chính 2 bản ghi đó từ máy chủ:**

```
GET /api/v1/hop-dong-tu-vans?vuViecId=6bf98a2e-… → 200, total = 2
0007: giaTriHopDong "200000000.00" · ngayBatDau "2026-08-07" · ngayKetThuc "2026-12-30" · soVuViecLienKet 1 · tienDoTt 25
0006: giaTriHopDong "250000000.00" · ngayBatDau "2026-08-07" · ngayKetThuc "2026-08-25" · soVuViecLienKet 3 · tienDoTt 0
```

Số thô khớp từng con số với chuỗi đang hiển thị; kiểu ngày thô `yyyy-mm-dd` được giao diện đổi sang `dd/mm/yyyy`
⇒ **có lớp định dạng thật**, không phải in thẳng dữ liệu.

**Ngưỡng đỏ kiểm bằng số:** 07/08/2026 → 25/08/2026 = **18 ngày (≤30 ⇒ phải đỏ, thực tế đỏ)**;
07/08/2026 → 30/12/2026 = **145 ngày (>30 ⇒ không được đỏ, thực tế không đỏ)**. Hai chiều đều đúng.

**Hai đường khớp nhau ⇒ dừng.**

### C4 — "không bị tràn/đè lên nhau" · `GAP` · ❓ **CHỈ GHI HIỆN TRẠNG, CẤM Pass/Reopen**

Đặc tả **chỉ** quy định **cắt chuỗi dài** (`srs-fr-05-vu-viec.md:1571`–`:1573`) và **độ phân giải tối thiểu**
(`:1603`), **im lặng** về "tràn/đè bố cục" ⇒ không có căn cứ chấm.

**Hiện trạng đo ở 1440×900:**

| Đo | Kết quả |
|---|---|
| Trang có bị cuộn ngang không | **Không** — `document.scrollWidth` = `clientWidth` = **1432px** |
| Bảng | nội dung **1700px** trong khung **972px** ⇒ **cuộn ngang trong khung bảng** (cách xử lý chuẩn), không đẩy vỡ trang |
| Chữ có đè lên nhau không | **Không** — mỗi ô nằm gọn trong ô của nó, dòng cao 65px, không thấy chồng lấn |
| Tên HĐ dài (85 và 79 ký tự) | **có cắt**: nút chứa tên đặt `-webkit-line-clamp: 2` + `overflow: hidden` ⇒ hiện 2 dòng rồi **cắt kèm dấu `…`** (nhìn thấy trên ảnh 03) |

⇒ Về đúng câu chữ của vế (*tràn/đè*): **không thấy hiện tượng tràn hay đè**. Nhưng vế đã khóa `GAP` nên
**không Pass**; ghi hiện trạng + ảnh cho BA.

**CÂU HỎI CHO BA:** đề nghị chốt tiêu chí nghiệm thu "không tràn/đè" — đo ở độ phân giải nào, chấp nhận
**cuộn ngang trong khung bảng** hay không? `srs-fr-05-vu-viec.md:1603` chỉ nói tối thiểu 1024×768.

> **Quan sát độc lập kèm theo (xem §7 mục 1):** cắt chuỗi **có** nhưng **không có gợi ý (tooltip) hiện đủ nội
> dung khi rê chuột** — trong khi §C `:1571` đòi *"cắt + dấu `...` cuối + tooltip hover hiển thị nội dung đầy đủ"*.
> Xử theo gate "bug mới tự lộ", **không** đổi quan hệ `GAP` của C4.

### C5 — "đồng nhất ngôn ngữ hiển thị" · `MATCH` · ✅ **ĐẠT**

**Đường 1 — giao diện, đọc `innerText`** (KHÔNG dùng `textContent` để tránh gom node ẩn):

| Nhóm chữ | Đọc được | Có mã kỹ thuật / tiếng Anh? |
|---|---|---|
| 11 tiêu đề cột | Mã hợp đồng · Tên hợp đồng · Bên A · Bên B · Giá trị (VNĐ) · Ngày bắt đầu · Ngày kết thúc · Vụ việc · Tiến độ TT · Trạng thái · Hành động | **Không** |
| Nhãn thanh lọc | *Tìm theo tên HĐ, mã HĐ, bên B* · *Chọn tư vấn viên* · *Từ ngày* · *Đến ngày* | **Không** |
| Nút | Xuất Excel · Tạo hợp đồng · Tìm kiếm · Xóa bộ lọc · Xem chi tiết · Sửa · Xóa | **Không** (*"Excel"* là tên định dạng tệp, không phải chữ giao diện dịch thiếu) |
| **Ô Trạng thái** (chỗ hay lộ mã nhất) | thẻ **"Đang thực hiện"** | **Không** |
| Phân trang | *1-2 / 2 mục* · *20 / trang* | **Không** |

Quét chủ động 8 mã dữ liệu (`DANG_THUC_HIEN`, `HOAN_THANH`, `HUY`, `TAM_DUNG`, `CHUA_THANH_TOAN`,
`DA_THANH_TOAN`, `CHUA_BAT_DAU`, `HOAT_DONG`) và 14 từ tiếng Anh hay lọt (`Search`, `Filter`, `Status`,
`Action`, `Contract`, `Page`, `Total`, `Reset`, `Submit`, `Cancel`, `Save`, `Delete`, `Edit`, `View`)
trên toàn bộ chữ của khối: **0 kết quả**.

**Đường 2 — đối chứng độc lập:** giá trị thô của chính 2 bản ghi đó từ máy chủ là **`DANG_THUC_HIEN`**
(mã dữ liệu), trong khi màn hiện **"Đang thực hiện"** ⇒ **chứng minh có lớp dịch nhãn**, đúng
`srs-fr-05-vu-viec.md:1492` (*"Mã DB không bao giờ xuất hiện trên giao diện người dùng"*).

**Hai đường khớp nhau ⇒ dừng.**

## 5. Verdict

| Vế | Quan hệ | Kết quả đo |
|---|---|---|
| C1 — đủ thành phần theo bảng `:278`–`:289` | `MATCH` | 🔴 **KHÔNG CHẤM ĐƯỢC** — bảng thành phần mô tả màn độc lập đã bị bỏ; chờ BA |
| C2 — giống bản vẽ thiết kế | `GAP` | ❓ CẦN BA (bản vẽ không có trong nguồn chuẩn) |
| C3 — đúng định dạng + trường thông tin | `MATCH` | ✅ **ĐẠT** (kể cả vế tô đỏ ≤30 ngày, đo cả 2 chiều) |
| C4 — không tràn/đè | `GAP` | ❓ CẦN BA (đặc tả im lặng); hiện trạng: không tràn, không đè |
| C5 — đồng nhất ngôn ngữ | `MATCH` | ✅ **ĐẠT** |

**Không vế `MATCH` nào bị chứng minh là hỏng** (C1 không chấm được ≠ hỏng); **còn 2 vế `GAP` + 1 vế chưa có
chuẩn đo** ⇒ theo bảng Verdict flow 04 + `QĐ-01`: **Verdict = Cần BA** ⇒ ô `Trạng thái dev fix` (R) = **`BA confirm`**.

> Không viết *"fix đã có tác dụng"*: phiếu chưa từng chạy, không có ảnh lỗi cũ ⇒ chỉ kết luận **hiện trạng**.

## 6. Ghi nhận (KHÔNG chấm, không kéo verdict) — gửi dev/BA

- **Thừa 1 cột "Trạng thái"** so với `:288`. `:288` liệt kê thành phần **bắt buộc có**, không cấm thêm ⇒ không tính lỗi.
- **Nhãn nút thêm** thực tế **"+ Tạo hợp đồng"**; `:286` ghi **"+ Thêm hợp đồng"**; Phụ lục E §H4
  (`srs-v3.5.md:6756`) lại bắt nhãn **"Thêm mới"**. **Ba nguồn lệch nhau**; phiếu này không chấm nhãn nút.
- **Không có nút [Làm mới]** (`:286`); thay bằng **[Xóa bộ lọc]**. Thuộc nhóm "thứ chỉ màn độc lập mới có" — chờ BA.
- **Phân trang mặc định đúng 20** — khớp `:289`, và vẫn nằm trong giới hạn `BR-DATA-07` (`:530`, tối đa 100/trang).

## 7. Quan sát ngoài vế — **candidate**, KHÔNG log thành bug

1. `cột Tên hợp đồng cắt chuỗi nhưng KHÔNG có gợi ý hiện đủ nội dung khi rê chuột` · xuất hiện tại **bước bắt
   buộc của C4** (đọc cột text dài ở 1440×900) · artifact: ảnh 03 + đo được nút chứa tên đặt `-webkit-line-clamp: 2`
   (có cắt, có dấu `…`), **không** có thuộc tính `title`, và sau khi phát chuỗi sự kiện rê chuột đầy đủ thì
   **không** có phần tử gợi ý nào xuất hiện trong trang · **còn thiếu**: xác nhận **phạm vi áp dụng của §C**.
   `srs-fr-05-vu-viec.md:1570` mở đầu *"Áp dụng cho **mọi cột text trong bảng**"* nhưng `:1573` lại chốt
   *"Áp dụng nhất quán cho **5 SCR**"* — mà 5 SCR đó là của **nhóm vụ việc**, không phải nhóm hợp đồng.
   **Đặc tả tự mâu thuẫn về phạm vi** ⇒ candidate + câu hỏi BA, **không** log thành lỗi.
2. `quy tắc tô đỏ ngày kết thúc ≤30 ngày KHÔNG áp dụng trên Màn 2` · xuất hiện khi đối chiếu hai bề mặt (§8
   Màn 2) · artifact: ảnh 01 — `HDTV-20260807-0003` kết thúc **25/08/2026** (18 ngày) hiển thị **màu thường**
   trên Màn 2, trong khi cùng ngưỡng đó **được tô đỏ** trên Màn 1 · **còn thiếu**: BA xác nhận `:288` áp cho
   những bề mặt nào ⇒ candidate, **không** đo thêm, **không** log lỗi.

> **Cổng "bug mới tự lộ"** (flow 04, luật 3): case này **không dùng phép xác nhận thêm nào**; cả 2 hiện tượng
> đều dùng lại artifact đã có từ các bước bắt buộc (luật 5).

## 8. Dữ liệu đã thay đổi trên môi trường (bắt buộc khai)

| Đổi gì | Bản ghi | Env | Lúc |
|---|---|---|---|
| **TẠO MỚI 1 hợp đồng tư vấn bằng giao diện — khai rõ là DỰNG TIỀN ĐỀ, không phải phép đo của phiếu nào** | **`HDTV-20260807-0007`** · `id` `7d3d1907-09dc-440d-8217-5b03333eb3eb` · tên *"Hợp đồng tư vấn pháp luật lao động và bảo hiểm xã hội cho doanh nghiệp siêu nhỏ"* (79 ký tự, **cố ý KHÔNG chứa cụm "sở hữu trí tuệ"**) · Bên B **`QA TVV PheDuyet TW R19`** (cố ý **khác** Bên B của HĐ-1) · giá trị 200.000.000 · `07/08/2026`→**`30/12/2026`** (cố ý **>30 ngày**) · 1 giai đoạn thanh toán 50.000.000 **đã thanh toán** ⇒ Tiến độ TT **25%** · 1 vụ việc liên kết · ghi chú mang dấu `QA-F8-TIEN-DE-20260807` | `18.143.165.120.nip.io` (**nội bộ**) | 2026-08-07 15:1x |

**Vì sao phải dựng:** Màn 1 lọc theo vụ việc đang mở, nên **5 hợp đồng nền seed lúc 13:2x KHÔNG hiện ở đây**
(chúng chỉ gắn tư vấn viên). Không có bản ghi thứ hai thì: `_02` C3 không có dòng đối chứng *"không tô đỏ"*,
Tiến độ TT luôn 0%, và `_03` không chứng minh được là **có lọc thật** (một mình HĐ-1 thì mọi từ khóa đều trả về nó).

- **Không** đụng dữ liệu đối tác. **Không** sửa/xóa bản ghi nào.
- Ghi nhận: điều phối đã nạp **1 tệp đính kèm** vào `HDTV-20260807-0006` lúc 14:57 bằng API (sau khi `_15` đo xong).

### Màn 2 — dữ kiện cho câu hỏi BA §5.1 (KHÔNG chấm, KHÔNG log bug)

Chi tiết Tư vấn viên → mục **"Hợp đồng tư vấn"** (ảnh 01):

| Thành phần | Màn 1 (bề mặt chấm) | Màn 2 |
|---|---|---|
| Tiêu đề khối | "Hợp đồng tư vấn liên kết" | "Hợp đồng tư vấn" |
| Nút thêm hợp đồng | **Có** ([+ Tạo hợp đồng]) | **Không có** |
| [Xuất Excel] | Có | Có |
| Ô tìm toàn văn | Có (*tên HĐ, mã HĐ, bên B*) | Có (**cùng câu chữ**) |
| Chọn tư vấn viên | Có | **Không có** (đã ở trong ngữ cảnh một TVV) |
| Khoảng ngày | Có | Có |
| Số cột bảng | **11** | **6** — Mã HĐ · Tên hợp đồng · Trạng thái · Ngày bắt đầu · Ngày kết thúc · Hành động |
| Thiếu so với `:288` | — | **Bên A · Bên B · Giá trị · Số VV (badge) · Tiến độ TT** |
| Tô đỏ ngày kết thúc ≤30 ngày | **Có** | **Không** (xem §7 mục 2) |

⇒ **Hai bề mặt cùng đọc một loại dữ liệu nhưng khác hẳn bộ cột và khác cả quy tắc tô màu.** Đây là dữ kiện
để BA chốt: bảng thành phần `:278`–`:289` **áp cho bề mặt nào**.

## 9. Ảnh bằng chứng (đã mở lại xem từng ảnh trước khi dùng)

| Ảnh | Nội dung | Liên kết xem được |
|---|---|---|
| `QLHDTVVCG_02-01-muc-hop-dong-tu-van-tren-chi-tiet-TVV.png` | **Màn 2** — mục "Hợp đồng tư vấn" trên Chi tiết Tư vấn viên: 6 cột, không nút thêm, ngày 25/08/2026 **không tô đỏ** | https://drive.google.com/file/d/1PsSQDoh5VnVcKSrOcjIXOtHHS8Pkp5lh/view?usp=drivesdk |
| `QLHDTVVCG_02-02-bam-breadcrumb-Hop-dong-tu-van-roi-ve-Tong-quan.png` | **Dữ kiện BA §5.1** — bấm liên kết "Hợp đồng tư vấn" trên đường dẫn phụ đề thì rơi về màn Tổng quan, không mở danh sách hợp đồng nào | https://drive.google.com/file/d/1Pun_QL_0Mr-FTxvgrMWz1bUidGMvnpwD/view?usp=drivesdk |
| `QLHDTVVCG_02-03-bang-2-dong-ngay-ket-thuc-to-do-va-khong-to-do.png` | **C1/C2/C4** — Màn 1 đủ thanh lọc, 2 nút, bảng, phân trang; tên HĐ dài bị cắt kèm dấu `…` | https://drive.google.com/file/d/1eFlzIJEB0YPwUw_iYcsxswCDKdMkoHik/view?usp=drivesdk |
| `QLHDTVVCG_02-04-cot-ngay-ket-thuc-badge-tien-do-trang-thai.png` | **C3** — 25/08/2026 **đỏ**, 30/12/2026 **đen**; badge số vụ việc; thanh tiến độ thanh toán | https://drive.google.com/file/d/18uTE5PffuOdz_3KUpBWuJGIjo0g9X1Xd/view?usp=drivesdk |

## 10. Cổng chốt verdict — trả lời đủ 5 câu (flow 04)

1. **Hành động tranh chấp đã bấm trên giao diện thật chưa?** Phiếu này là phiếu **quan sát màn**, không có thao
   tác tranh chấp; đã mở đúng màn bằng giao diện thật và đọc trực tiếp từ trang.
2. **Mỗi vế có đủ 2 đường đo độc lập không?** C3 và C5 có (giao diện + đọc giá trị thô từ máy chủ). C1/C2/C4
   không chấm nên không cần.
3. **Có Pass bằng quan sát tĩnh không?** Không — bảng có **2 dòng thật**, trong đó 1 dòng do lượt đo này dựng,
   và mọi con số đều đối chiếu với dữ liệu máy chủ.
4. **Có hạ `GAP` xuống `MATCH` không?** Không. C2 và C4 giữ `GAP` dù hiện trạng không thấy vấn đề.
5. **Đã khai dữ liệu thay đổi chưa?** Rồi — §8, kèm mã, định danh và lý do dựng.
