# B1 — dòng 308 · `QLHDTVVCG_02` — Điều kiện tìm kiếm / bộ lọc (màn danh sách Hợp đồng tư vấn)

> Lô G4 · nhóm B · 2026-08-07. Luật chung ở [`00-BRIEF-CHUNG.md`](../00-BRIEF-CHUNG.md) — không lặp lại ở đây.

## 0. Tham số lượt đo

| Mục | Giá trị |
|---|---|
| Bản dựng TRƯỚC lượt đo | `index-BbPPdate.js` (đo 2026-08-07 21:57:17 +07) |
| Bản dựng SAU lượt đo | `index-BbPPdate.js`, `last-modified Fri, 07 Aug 2026 06:47:57 GMT` = **13:47:57 VN** (đo 2026-08-07 22:21:09 +07) ⇒ **KHÔNG đổi** trong suốt lượt đo, và **cùng bản dựng với lượt cũ ở ô T** |
| Khung giờ đo | 2026-08-07, 21:57 → 22:21 (giờ VN) |
| Môi trường | `https://18.143.165.120.nip.io` (nội bộ) |
| Tài khoản | `cbnv_tw_03` — CB Nghiệp vụ - Trung ương (BTP · TW). Không dùng `admin` ra verdict. |
| Cửa sổ | 1440×900 (+ đo phụ 1024×768) |
| Đường vào | Vụ việc HTPL → Chi tiết vụ việc `VV-BTP-TW-20260804-002` → mục "HĐ tư vấn liên kết" |
| SRS nguồn | `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-14-hop-dong-tv.md` |

## 1. Phạm vi đo (user chốt — CẤM mở rộng)

Chỉ 2 nguồn:

1. **Bước của phiếu** `[J]`: `1. Chọn menu "Hợp đồng Tư vấn"` — điều kiện `[H]`: đã đăng nhập.
   Chấm theo `[K] Kết quả mong đợi`, nguyên văn 3 ý:
   - Hệ thống hiển thị các trường thông tin giống với thiết kế
   - Dữ liệu hiển thị đúng định dạng và trường thông tin
   - Dữ liệu hiển thị không bị tràn/đè lên nhau, đồng nhất ngôn ngữ hiển thị
2. **BA chốt ô `[S]` 06/08/2026** (hướng A): giữ quyết định 11/05/2026 bỏ menu riêng; phần mềm đúng bản gốc;
   lối vào = Chi tiết Vụ việc / Lịch sử TVV; **Dev đã bổ sung theo SRS: bộ lọc ngữ cảnh cho màn danh sách hợp đồng**.

⇒ Thanh bên không có mục "Hợp đồng Tư vấn" là ĐÚNG, không tính lỗi.

## 2. Quote SRS — đã MỞ FILE xác minh số dòng (2026-08-07)

| Dòng | Nội dung thực đọc được |
|---|---|
| `srs-fr-14-hop-dong-tv.md:266` | "**Thay doi v2.1:** HD Tu van (UC159) khong con la muc menu rieng. Truy cap tu: (1) Chi tiet Vu viec MH-05.3 -> tab/section "HD tu van lien ket", (2) Chi tiet TVV MH-04.3 -> tab "Lich su" -> HD. **Noi dung MH-14.1 ben duoi giu lai de tham chieu element-level** -- implement dang modal/drawer khi truy cap tu VV/TVV." |
| `:268` | "**Round 7 BA decision (2026-05-11):** Route standalone `/hop-dong-tv/danh-sach` KHÔNG phải menu/màn hình nghiệp vụ public… route này phải là route ẩn… không xuất hiện trong sidebar/menu, và không được QA coi là luồng chính." |
| `:274` | "**UX-Spec ref:** dac-ta-man-hinh-chuc-nang-v2.md -- MH-14.1" |
| `:278` | "**Danh sách:** Breadcrumb > Tiêu đề + nút hành động > Thanh lọc (tìm kiếm UC159e) > Bảng hợp đồng > Phân trang." |
| `:285` | vùng 1 toolbar — Breadcrumb "Trang chủ > Tư vấn > Hợp đồng tư vấn" |
| `:286` | vùng 2 toolbar — Tiêu đề "Quản lý Hợp đồng Tư vấn" + [+ Thêm hợp đồng] [Xuất Excel] [Làm mới]; **nút [+ Thêm hợp đồng] CHỈ hiển thị với CB NV — ẩn với TVV/CG** |
| `:287` | vùng 3 filter-bar — "Thanh lọc (UC159e) \| form \| **Full-text: tên HĐ, mã HĐ, bên B. TVV (searchable). Khoảng ngày** \| change -> filter \| luôn hiển thị" |
| `:288` | vùng 4 content — Bảng hợp đồng 10 cột: Mã HĐ (HDTV-{YYYYMMDD}-{SEQ}) / Tên HĐ / Bên A / Bên B / Giá trị (format tiền) / Thời hạn bắt đầu / Thời hạn kết thúc (**đỏ nếu <= 30 ngày**) / Số VV liên kết (badge) / Tiến độ TT (progress bar %) / Hành động |
| `:289` | vùng 5 footer — Phân trang, 20 mục/trang |
| `:216`–`:219` | Inputs FR-X.3-02 (UC159e): `keyword` (tên HĐ, mã HĐ, bên B) · `tvv_id` · `tu_ngay` · `den_ngay` (`>= tu_ngay`) |
| `:226`–`:227` | Xử lý: "Tìm kiếm toàn văn trên tên HĐ, mã HĐ, bên B" + "Áp dụng bộ lọc **AND logic**" |
| `:250`–`:251` | E1 `ERR-HDTV-TK-01` "Ngày bắt đầu phải trước ngày kết thúc"; E2 `INF-HDTV-TK-01` "Không tìm thấy hợp đồng phù hợp" |
| `:255`–`:258` | AC: từ khóa → DS matching + phân trang · lọc TVV → chỉ HĐ của TVV đó · lọc khoảng ngày → lọc theo thời gian · không kết quả → "Không tìm thấy hợp đồng" |
| `:175` | "**Câu thông báo sau khi lưu + điều hướng** `[BA chốt 2026-08-06]`: … Nhóm X.3 **không có màn danh sách độc lập** (xem §3 — quyết định BA 11/05/2026), nên sau khi lưu hệ thống đóng biểu mẫu và trả người dùng về **ngữ cảnh đã mở nó** (Chi tiết Vụ việc hoặc Chi tiết Tư vấn viên)…" |
| `srs-fr-05-vu-viec.md:1492` | "Khi render UI, dev **phải dịch** mã DB (snake_case enum) sang nhãn tiếng Việt… Mã DB **không bao giờ** xuất hiện trên giao diện người dùng." |
| `srs-fr-05-vu-viec.md:1603` | "**Phía cán bộ (CMS)…:** tối thiểu hỗ trợ máy tính bảng 1024×768. Không bắt buộc mobile." |

**Đã kiểm chứng thêm:** tài liệu bản vẽ `dac-ta-man-hinh-chuc-nang-v2.md` (đích của `:274`) **KHÔNG tồn tại** trong repo — `find . -iname "*dac-ta-man-hinh*"` trả 0 kết quả. Chuỗi `MH-14.1` chỉ xuất hiện trong chính 3 bản srs-fr-14 (v3 / v3.5 / v4), không có file bản vẽ nào.

## 3. 🔴 Ba điểm treo của lượt cũ (ô T) → NAY THẾ NÀO

### Điểm 1 — "Bảng thành phần màn hình áp cho màn nào?" → **HẾT TREO, BA đã trả lời**

Lượt cũ hỏi: đặc tả mô tả một **màn danh sách hợp đồng độc lập** gồm 5 vùng (`:285` breadcrumb riêng ·
`:286` tiêu đề trang + 3 nút · `:287` thanh lọc · `:288` bảng 10 cột · `:289` phân trang), nhưng chính
đặc tả `:266`/`:268` đã bỏ màn độc lập đó ⇒ bảng thành phần áp cho bề mặt nào?

**BA ô S 06/08/2026 trả lời trực tiếp:** quyết định 11/05/2026 (bỏ menu riêng) **vẫn giữ nguyên**,
**"phần mềm đang đúng bản gốc"**, vật cản là bộ test case mô tả lối vào đã hết hiệu lực, hợp đồng truy
cập từ Chi tiết Vụ việc hoặc Lịch sử TVV, **"Không sửa phần mềm theo lối vào cũ"**.

Cộng thêm câu chốt đã có sẵn trong đặc tả `:266` — "**Noi dung MH-14.1 ben duoi giu lai de tham chieu
element-level** -- implement dang modal/drawer khi truy cap tu VV/TVV" — thì bảng `:283`–`:295` là chuẩn
ở mức **THÀNH PHẦN**, không phải chuẩn "phải có đủ 5 vùng của một màn độc lập".

⇒ Ba vùng chỉ-màn-độc-lập-mới-có (đường dẫn phụ đề riêng · tiêu đề trang riêng · phân trang riêng của
   màn) **không còn là điểm treo** và không phải thiếu sót của Dev.
⇒ Chấm ở mức thành phần (kết quả đo §4): thanh lọc khớp **4/4** trường `:287` · bảng đủ **10/10** cột
   `:288` (dư cột "Trạng thái" — `:288` liệt kê thành phần bắt buộc CÓ, không cấm thêm) · phân trang
   **20 mục/trang** đúng `:289` · nút `[+ Tạo hợp đồng]` + `[Xuất Excel]` có (`:286`).
   Lệch nhỏ: `:286` liệt kê thêm nút `[Làm mới]` — màn này không có, thay bằng `[Xóa bộ lọc]` trong
   thanh lọc; và nhãn thực tế là `+ Tạo hợp đồng` (đặc tả ghi `+ Thêm hợp đồng`).
   **Hai lệch này thuộc vùng toolbar của màn độc lập đã bị bỏ, và phiếu B1 chấm "trường THÔNG TIN",
   không chấm nhãn nút ⇒ không tính lỗi cho phiếu này.** (đã ghi vào mục "Báo lead" §6)

### Điểm 2 — "Không có bản vẽ thiết kế để đối chiếu" → **BA chưa cấp bản vẽ, NHƯNG không còn quyết định đạt/không đạt**

- Đã kiểm lại: tài liệu `dac-ta-man-hinh-chuc-nang-v2.md` (đích của `:274`) **KHÔNG tồn tại** trong bộ
  nguồn chuẩn (`find . -iname "*dac-ta-man-hinh*"` → 0 kết quả; chuỗi `MH-14.1` chỉ có trong chính 3 bản
  `srs-fr-14-*`). Điều này KHÔNG đổi so với lượt cũ.
- **Nhưng vai trò của nó đã đổi.** Bản vẽ chỉ cần thiết khi đo ra **một khác biệt về bố cục/thứ tự/màu
  sắc mà văn bản đặc tả im lặng**. Lượt này đo hết mọi yêu cầu văn bản đặc tả có ghi (trường lọc, cột
  bảng, định dạng tiền/ngày, quy tắc tô đỏ, phân trang, ngôn ngữ hiển thị) và **không tìm thấy khác
  biệt nào cần bản vẽ để phân xử**. Cộng với việc BA ô S đã khẳng định "phần mềm đang đúng bản gốc" cho
  đúng cụm này.
- ⇒ Theo bảng chốt verdict của lô (`00-BRIEF-CHUNG.md`): điểm treo chỉ giữ `BA confirm` khi nó
  **quyết định đạt/không đạt**. Ở đây nó không quyết định gì nữa ⇒ **không giữ `BA confirm` vì điểm này**.
  Vẫn nêu lại đề nghị cấp bản vẽ (hoặc xác nhận không dùng bản vẽ làm chuẩn nghiệm thu) trong ô sheet
  dưới dạng ghi chú phạm vi chấm, không phải blocker.

### Điểm 3 — "Tiêu chí không tràn / không đè chưa được định nghĩa" → **HẾT TREO, đo được ở mọi cách hiểu hợp lý**

Lượt cũ chỉ đo ở 1440×900 rồi hỏi BA "đo ở độ phân giải nào, có chấp nhận cuộn ngang trong khung bảng
không". Lượt này đo **thêm ở đúng độ phân giải tối thiểu mà đặc tả có ghi** — `srs-fr-05-vu-viec.md:1603`
"Phía cán bộ (CMS)… tối thiểu hỗ trợ máy tính bảng **1024×768**" — và kết quả ĐẠT ở cả hai (chi tiết §4.3):

| Phép đo | 1440 rộng | 1024 rộng |
|---|---|---|
| Trang có cuộn ngang không (`scrollWidth` vs `clientWidth`) | **KHÔNG** (1432 = 1432) | **KHÔNG** (1016 = 1016) |
| Số cặp ô **chữ đè chữ** (loại trừ cột ghim) | **0** | **0** |
| Số ô có chữ tràn khỏi khung ô | **0** | **0** |
| Thanh lọc | 1 hàng, gọn | tự xuống 2 hàng, gọn |

⇒ Dù BA chốt tiêu chí theo cách nào (đo ở 1024 hay 1440; chấp nhận hay không chấp nhận cuộn ngang trong
khung bảng), màn này **vẫn không tràn, không đè**. Điểm treo không còn quyết định đạt/không đạt.

**Ghi chú kỹ thuật quan trọng — chống kết luận sai:** ở cả hai độ phân giải, phép dò hình học có báo
4–8 cặp ô "giao nhau". **Toàn bộ đều là cặp giữa một ô thường và cột ghim** (`position: sticky;
right: 0; z-index: 3; background: rgb(255,255,255)` — nền TRẮNG ĐỤC + đổ bóng mép). Đây là cơ chế ghim
cột chuẩn: nội dung trượt XUỐNG DƯỚI cột ghim chứ không phải chữ chồng lên chữ. Đã chứng minh bằng cách
cuộn ngang khung bảng tới cuối (`scrollLeft` 0 → 728 = hết mức): toàn bộ 11 cột hiện đủ và đọc được,
không mất chữ (ảnh `-12-`). **Số cặp giao nhau giữa HAI ô thường = 0.**

### Kết luận về ba điểm treo

| Điểm treo lượt cũ | Nay | Vì sao |
|---|---|---|
| 1 — bảng thành phần áp cho bề mặt nào | ✅ **hết treo** | BA ô S 06/08 chốt hướng A + `:266` nói rõ bảng dùng ở mức thành phần |
| 2 — không có bản vẽ thiết kế | ⚠️ vẫn thiếu bản vẽ nhưng **không còn là blocker** | không đo ra khác biệt nào cần bản vẽ phân xử; BA khẳng định phần mềm đúng bản gốc |
| 3 — chưa định nghĩa "tràn/đè" | ✅ **hết treo** | đo ở cả 1440 và 1024 (mức tối thiểu đặc tả ghi) đều không tràn, không đè |

## 4. Nhật ký đo

### 4.0 Đăng nhập + đường vào (21:59–22:03)

- `cbnv_tw_03` / `Test@1234`, mã xác thực lấy ở MailHog. Vai trò hiển thị trên thanh trên cùng:
  "CB Nghiệp vụ - Trung ương #03 · Cán bộ Nghiệp vụ Trung ương", phạm vi "BTP · TW".
- **Phiên bị rớt 1 lần lúc ~22:01** (đang mở Chi tiết vụ việc thì bị đẩy về màn đăng nhập, `auth-store`
  trong `localStorage` bị xóa). MailHog cho thấy có mã xác thực phát cho `cbnv_tw_03` lúc 15:01:29 UTC
  **không phải do tôi bấm** ⇒ nhiều khả năng tiến trình khác đăng nhập cùng tài khoản. Đăng nhập lại
  `cbnv_tw_03` (không đổi vai trò/cấp), phần còn lại chạy liên tục không rớt nữa.
- **Thanh bên KHÔNG có mục "Hợp đồng Tư vấn"** — liệt kê đủ 24 mục: Tổng quan · Hỏi đáp pháp lý ·
  Kế hoạch đào tạo · Chương trình đào tạo · Khóa học · Kho tài liệu / Bài giảng · Ngân hàng câu hỏi &
  Đề kiểm tra · Giảng viên / Trợ giảng · Tư vấn viên / Chuyên gia · Tổ chức tư vấn · Người hỗ trợ pháp
  lý · Vụ việc HTPL · Chi trả chi phí · Doanh nghiệp · Đánh giá hiệu quả · Thư viện biểu mẫu · Danh sách
  biểu mẫu · Tư vấn chuyên sâu · Kho câu hỏi · Tư vấn nhanh · Chương trình HTPLDN · Đợt báo cáo · Báo cáo
  thống kê · Cấu hình hệ thống. ⇒ Đúng SRS `:266` + `:268` + BA ô S. **Không tính lỗi.** (ảnh `-01-`)
- Đường vào đã dùng: Vụ việc HTPL → gõ `VV-BTP-TW-20260804-002` + Enter → 1 kết quả → mở Chi tiết →
  mục **"HĐ tư vấn liên kết"** (accordion). (ảnh `-02-`)

### 4.1 Baseline mục "HĐ tư vấn liên kết" — 2 hợp đồng

Bảng có **11 cột**: `Mã hợp đồng · Tên hợp đồng · Bên A · Bên B · Giá trị (VNĐ) · Ngày bắt đầu ·
Ngày kết thúc · Vụ việc · Tiến độ TT · Trạng thái · Hành động`
⇒ đủ **10/10 cột** SRS `:288` đòi, dư thêm cột "Trạng thái" (SRS liệt kê thành phần **bắt buộc có**, không cấm thêm).

| Mã HĐ | Tên | Bên A | Bên B | Giá trị | Bắt đầu | Kết thúc | VV | Tiến độ TT | Trạng thái |
|---|---|---|---|---|---|---|---|---|---|
| HDTV-20260807-0007 | Hợp đồng tư vấn pháp luật lao động và bảo hiểm xã hội cho doanh nghiệp siêu nhỏ | Cục Bổ trợ tư pháp - Bộ Tư pháp | QA TVV PheDuyet TW R19 | 200.000.000 VNĐ | 07/08/2026 | 30/12/2026 | 1 | 25% | Đang thực hiện |
| HDTV-20260807-0006 | Hợp đồng tư vấn xác lập quyền sở hữu trí tuệ và nhãn hiệu cho doanh nghiệp nhỏ và vừa | Cục Bổ trợ tư pháp - Bộ Tư pháp | Chuyên gia UAT QLNDTVVCG 38 | 250.000.000 VNĐ | 07/08/2026 | 25/08/2026 | 3 | 40% | Đang thực hiện |

Màu chữ đọc bằng `getComputedStyle` (không đoán qua ảnh):
- Ngày kết thúc `30/12/2026` (còn 145 ngày) → `rgb(31,31,31)`, `font-weight 400` = **thường**.
- Ngày kết thúc `25/08/2026` (còn 18 ngày ≤ 30) → `rgb(255,77,79)`, `font-weight 600` = **đỏ + đậm**.
⇒ Quy tắc `:288` "Thời hạn kết thúc (đỏ nếu <= 30 ngày)" chạy **CÓ ĐIỀU KIỆN**, đo được cả hai chiều.

### 4.2 Bộ lọc ngữ cảnh — Dev khai đã bổ sung (ô S). ĐO THẬT, có baseline + phép lọc phân biệt

**Bộ lọc CÓ THẬT, đủ 4 trường đúng `:287` / `:216`–`:219`:**

| Trường trên màn | SRS đòi | Khớp |
|---|---|---|
| Ô chữ `Tìm theo tên HĐ, mã HĐ, bên B` | `:287` "Full-text: tên HĐ, mã HĐ, bên B" · `:216` `keyword` | ✅ |
| Ô chọn `Chọn tư vấn viên` (gõ tìm được) | `:287` "TVV (searchable)" · `:217` `tvv_id` | ✅ |
| Ô `Từ ngày` | `:287` "Khoảng ngày" · `:218` `tu_ngay` | ✅ |
| Ô `Đến ngày` | `:219` `den_ngay` | ✅ |
| + nút `Tìm kiếm`, `Xóa bộ lọc` | — (không bắt buộc, không cấm) | có |

**"Ngữ cảnh" là có thật, không phải danh sách toàn hệ thống:** mọi lượt lọc đều kèm định danh vụ việc
đang mở (`vuViecId=6bf98a2e-…`) — kể cả lượt không nhập điều kiện nào. ⇒ danh sách luôn bị giới hạn
trong vụ việc đang xem.

**Bảng phép đo (baseline 2 → sau lọc bao nhiêu, bản ghi nào):**

| # | Điều kiện lọc | Số bản ghi | Bản ghi trả về | Đúng? |
|---|---|---:|---|---|
| L0 | (không lọc) | **2** | 0007 + 0006 | baseline |
| L1 | từ khóa `HDTV-20260807-0006` (mã HĐ) | **1** | 0006 | ✅ (ảnh `-03-`) |
| L2 | từ khóa `sở hữu trí tuệ` (giữa tên HĐ) | **1** | 0006 | ✅ |
| L3 | từ khóa `lao động` (giữa tên HĐ) | **1** | 0007 | ✅ |
| L4 | từ khóa `PheDuyet` (giữa tên Bên B) | **1** | 0007 | ✅ |
| L5 | từ khóa `ZZZKHONGCO` | **0** | — + câu "Không tìm thấy hợp đồng phù hợp" | ✅ khớp `:251` `INF-HDTV-TK-01` |
| L6 | Tư vấn viên = `TVV-BTP-TW-0016 — QA TVV PheDuyet TW R19` | **1** | 0007 (Bên B đúng người đã chọn) | ✅ khớp AC `:256` (ảnh `-06-`) |
| L7 | Tư vấn viên = `CG-QLND38-UAT — Chuyên gia UAT QLNDTVVCG 38` | **1** | 0006 | ✅ đổi người → đổi kết quả, không phải số cố định |
| L8 | Từ ngày `01/09/2026` | **0** | — (cả 2 HĐ đều bắt đầu 07/08/2026) | ✅ đúng, lọc theo **ngày bắt đầu** |
| L9 | Đến ngày `31/08/2026` | **1** | 0006 (kết thúc 25/08 ≤ 31/08); loại 0007 (kết thúc 30/12) | ✅ lọc theo **ngày kết thúc** (ảnh `-07-`) |
| L10 | `lao động` **+** Đến ngày `31/08/2026` | **0** | — (L3 ra 0007, L9 ra 0006 ⇒ giao = rỗng) | ✅ đúng **AND** `:227` (ảnh `-08-`) |
| L11 | `sở hữu trí tuệ` **+** Đến ngày `31/08/2026` | **1** | 0006 (nằm trong cả hai vế) | ✅ đúng AND |
| L12 | bấm `Xóa bộ lọc` | **2** | 0007 + 0006 | ✅ trả lại baseline |

Ô `Chọn tư vấn viên` **gõ tìm được thật**: gõ `PheDuyet` → danh sách 7 lựa chọn thu còn **1**
(`TVV-BTP-TW-0016 — QA TVV PheDuyet TW R19`) (ảnh `-05-`). Danh sách lựa chọn chỉ hiện
`mã TVV — họ tên (tổ chức)`, **không lộ mã kỹ thuật** — 2 nút chứa chuỗi định danh nội bộ trong cây DOM
có `width = 0px` (nút đo ẩn của thư viện giao diện), đã kiểm bằng `getBoundingClientRect` + xem ảnh
`-04-`: trên màn không nhìn thấy chuỗi nào như vậy.

### 4.2b Tiền đề tự dựng để phép lọc khoảng ngày có tính phân biệt

Cả 2 hợp đồng sẵn có đều bắt đầu **07/08/2026** ⇒ ô `Từ ngày` không thể chứng minh "chọn đúng tập con",
chỉ chứng minh được "loại hết". Theo luật 5 của lô (thiếu dữ liệu thì tự tạo), đã **tạo mới 1 hợp đồng**
bằng chính giao diện, từ nút `Tạo hợp đồng` của mục này:

- Mã sinh tự động **`HDTV-20260807-0008`** (đúng khuôn `HDTV-{YYYYMMDD}-{SEQ}` của `:288`/`:147`)
- Tên `Hop dong QA-G4-B1 kiem tra bo loc khoang ngay 20260807` · Bên B `QA TVV Seed28 Active`
  (`TVV-BTP-TW-0002`) · Giá trị `150.000.000` · Thời gian **01/06/2026 → 20/06/2026** (khác hẳn 2 HĐ cũ)
- Ghi chú mang dấu `QA-G4-B1-TIEN-DE-20260807` để phân biệt với dữ liệu đối tác
- Vụ việc liên kết được điền sẵn `VV-BTP-TW-20260804-002` ngay khi mở biểu mẫu từ ngữ cảnh này
- Bộ bắt thông báo (tự kiểm `soObserverDangSong = 1`): **1 request ghi** `POST /api/v1/hop-dong-tu-vans`
  + **1 khung thông báo** "Đã lưu hợp đồng" ⇒ không gửi trùng, không hiện thông báo lặp.
  *(Câu thông báo này thuộc phạm vi phiếu B3 dòng 321, ghi ở đây chỉ để lưu vết.)*

Baseline sau khi tạo = **3 hợp đồng**. Phép lọc khoảng ngày trên baseline 3 (ảnh `-09-` → `-11-`):

| # | Điều kiện | Số bản ghi | Bản ghi | Đúng? |
|---|---|---:|---|---|
| L13 | (không lọc) | **3** | 0008 (01/06→20/06) · 0007 (07/08→30/12) · 0006 (07/08→25/08) | baseline |
| L14 | Từ ngày `01/07/2026` | **2** | 0007 + 0006 — **loại đúng 0008** (bắt đầu 01/06 < 01/07) | ✅ (ảnh `-10-`) |
| L15 | Đến ngày `30/06/2026` | **1** | **chỉ 0008** (kết thúc 20/06 ≤ 30/06) — loại 0007 và 0006 | ✅ (ảnh `-11-`) |

⇒ Ô `Từ ngày` so với **ngày bắt đầu**, ô `Đến ngày` so với **ngày kết thúc**; cả hai chọn đúng tập con,
không phải "ra hết" hay "ra rỗng".

### 4.3 Ba ý của cột `[K]` — chấm từng ý

**Ý 1 — "Hệ thống hiển thị các trường thông tin giống với thiết kế" → ✅ ĐẠT**
Chấm ở mức thành phần theo `:266` + BA ô S (xem §3 Điểm 1): 4/4 trường lọc `:287` · 10/10 cột `:288`
· phân trang 20 mục/trang `:289` · nút `[+ Tạo hợp đồng]` `[Xuất Excel]` `:286`. Không đo ra khác biệt
nào cần bản vẽ để phân xử.

**Ý 2 — "Dữ liệu hiển thị đúng định dạng và trường thông tin" → ✅ ĐẠT (kiểm bằng 2 đường)**

Đường 1 — đọc từng ô trên màn (§4.1). Đường 2 — đọc giá trị thô của **chính 3 bản ghi đó** từ máy chủ:

| Trường | Giá trị thô lưu | Trên màn | Đặc tả |
|---|---|---|---|
| `trangThai` | `DANG_THUC_HIEN` | "Đang thực hiện" | `srs-fr-05-vu-viec.md:1492` — mã dữ liệu KHÔNG bao giờ xuất hiện trên giao diện ⇒ **có lớp dịch nhãn thật** |
| `giaTriHopDong` | `150000000.00` / `200000000.00` / `250000000.00` | `150.000.000 VNĐ` / `200.000.000 VNĐ` / `250.000.000 VNĐ` | `:288` "Giá trị (format tiền)" · `:151` "format tiền VND" ⇒ **có lớp định dạng thật** |
| `thoiHanBatDau` | `2026-06-01` / `2026-08-07` | `01/06/2026` / `07/08/2026` | `:152` `dd/mm/yyyy` |
| `thoiHanKetThuc` | `2026-06-20` / `2026-12-30` / `2026-08-25` | `20/06/2026` / `30/12/2026` / `25/08/2026` | `:153` `dd/mm/yyyy` |
| `soVuViecLienKet` | `1` / `1` / `3` | huy hiệu tròn 1 / 1 / 3 | `:154` "badge" |
| tiến độ thanh toán | — | thanh tiến trình `0%` / `25%` / `40%` | `:155` "progress bar %" |

Quy tắc `:288` "Ngày kết thúc đỏ nếu ≤ 30 ngày" — đo **cả hai chiều** bằng `getComputedStyle`:
`25/08/2026` (còn 18 ngày) → `rgb(255,77,79)` + `font-weight 600`; `30/12/2026` (còn 145 ngày) →
`rgb(31,31,31)` + `400`. Chạy **có điều kiện**, không tô đỏ tất cả.

**Ý 3 — "Không tràn/đè lên nhau, đồng nhất ngôn ngữ hiển thị" → ✅ ĐẠT**

*Không tràn / không đè:* bảng §3 Điểm 3 — 1440 và 1024 đều: trang không cuộn ngang · **0 cặp chữ đè chữ**
· 0 ô tràn. Bảng dùng cuộn ngang **bên trong khung bảng** (`overflow-x: auto`, `scrollWidth 1700` >
`clientWidth 972`/`748`) chứ không đẩy vỡ trang; cuộn tới cuối thì đủ 11 cột đọc được (ảnh `-12-`, `-13-`).

Tên hợp đồng dài (54 · 79 · 85 ký tự) được **cắt gọn 2 dòng kèm dấu ba chấm** (`-webkit-line-clamp: 2`)
và **CÓ gợi ý hiện đủ nội dung khi rê chuột** — thuộc tính `title` của ô mang **nguyên văn** tên hợp đồng,
đã đọc lại đúng từng chữ cho cả 3 dòng.
🔴 **Đây là điểm SỬA LẠI so với ô T lượt cũ**, chỗ đó ghi "KHÔNG có gợi ý hiện đủ nội dung khi rê chuột".
Đo lại trên đúng bản dựng đó thì **CÓ**. Lượt cũ nhận định sai điểm này.

*Đồng nhất ngôn ngữ:* quét toàn bộ **54 cụm chữ NHÌN THẤY ĐƯỢC** trong mục (đi theo cây DOM, bỏ node
`display:none`/`visibility:hidden`, cộng cả chữ mờ trong ô nhập): 11 tiêu đề cột · nhãn 4 ô lọc · nhãn 4
nút · nội dung 3 dòng dữ liệu · ô Trạng thái · dòng phân trang. Chủ động dò 10 mã dữ liệu hay lộ
(`DANG_THUC_HIEN`, `HOAN_THANH`, `null`, `undefined`, `NaN`…) và 22 từ tiếng Anh hay lọt (`Search`,
`Filter`, `Export`, `Status`, `Actions`, `No data`…): **0 kết quả cho cả hai**. Không có mục nào tiếng Anh,
không có mục nào lộ mã kỹ thuật.

Bảng điều khiển trình duyệt trong suốt lượt đo: **0 lỗi, 0 cảnh báo**.

## 5. Verdict

| Mục chấm | Kết quả |
|---|---|
| Ý 1 `[K]` — trường thông tin giống thiết kế | ✅ ĐẠT |
| Ý 2 `[K]` — đúng định dạng và trường thông tin | ✅ ĐẠT |
| Ý 3 `[K]` — không tràn/đè + đồng nhất ngôn ngữ | ✅ ĐẠT |
| BA ô S — thanh bên không có mục "Hợp đồng Tư vấn" | ❌ không phải lỗi (đúng quyết định nghiệp vụ) |
| BA ô S — Dev khai đã bổ sung **bộ lọc ngữ cảnh** | ✅ CÓ THẬT + CHẠY ĐÚNG (15 phép đo L0–L15, đều có baseline + số bản ghi thực) |

**⇒ `Test done`.** Không có ý nào Reopen. Không còn điểm treo nào quyết định đạt/không đạt.

## 6. Báo lead — ghi nhận ngoài phạm vi phiếu (KHÔNG đưa vào ô sheet đối tác)

1. **Từ khóa là mảnh rời của mã hợp đồng thì không tìm ra.** `0006` → 0 kết quả · `20260807` → 0 ·
   `807-0006` → 0 · `HDTV-20260807-000` → 0. Nhưng `HDTV-20260807-0006` → 1 · `HDTV-20260807` → 2 ·
   `HDTV` → 2 · `-0006` → 1. Trong khi mảnh GIỮA của **tên HĐ** (`sở hữu trí tuệ`, `nhãn hiệu`,
   `lao động`) và của **bên B** (`PheDuyet`) đều tìm được bình thường. ⇒ riêng mã hợp đồng khớp theo
   đầu chuỗi/từ, không khớp mảnh giữa. Đặc tả `:226` chỉ ghi "Tìm kiếm toàn văn trên tên HĐ, mã HĐ,
   bên B", không quy định mức mảnh ⇒ **chưa đủ căn cứ kết là lỗi**, nhưng người dùng quen gõ 4 số cuối
   sẽ thấy rỗng. Đề nghị lead cân nhắc mở dòng riêng nếu muốn Dev nới.
2. **Hợp đồng đã hết hạn trong quá khứ không được tô đỏ.** `HDTV-20260807-0008` kết thúc 20/06/2026
   (trước ngày đo 07/08/2026) hiển thị màu thường. Đặc tả `:288` chỉ ghi "đỏ nếu <= 30 ngày", **im lặng**
   về hợp đồng đã quá hạn. Chưa kết luận đúng/sai.
3. **Nút `[Làm mới]` mà `:286` liệt kê không có** trên mục này (thay bằng `[Xóa bộ lọc]` trong thanh lọc);
   nhãn nút thêm là `+ Tạo hợp đồng` trong khi `:286` ghi `+ Thêm hợp đồng`. Cả hai thuộc vùng toolbar
   của màn độc lập đã bị bỏ ⇒ không tính lỗi cho phiếu B1; liên quan phiếu B2 (dòng 319) hơn.
4. **Sửa lại nhận định của lượt trước:** ô T cũ ghi cột Tên hợp đồng "KHÔNG có gợi ý hiện đủ nội dung khi
   rê chuột" — đo lại trên **đúng bản dựng đó** thì **CÓ** (thuộc tính `title` mang nguyên văn tên, cả 3
   dòng). Nếu lead đã chuyển ý này cho Dev thì nên rút.
5. **Tranh chấp tài khoản:** phiên `cbnv_tw_03` bị rớt 1 lần lúc ~22:01; MailHog có mã xác thực phát cho
   `cbnv_tw_03` lúc 15:01:29 UTC không phải do tôi bấm ⇒ có tiến trình khác dùng cùng tài khoản. Đã đăng
   nhập lại cùng tài khoản, cùng vai trò, cùng cấp; phần còn lại chạy liên tục.
6. **Dữ liệu đã thay đổi trên môi trường nội bộ:** tạo mới **1** hợp đồng `HDTV-20260807-0008` trong vụ
   việc `VV-BTP-TW-20260804-002` (ghi chú mang dấu `QA-G4-B1-TIEN-DE-20260807`). Không sửa, không xóa bản
   ghi nào khác. Các phép lọc là thao tác chỉ-đọc, không ghi gì.

## 7. Danh sách ảnh — ảnh nào chứng minh gì

| Tệp trong `image/` | Chứng minh |
|---|---|
| `QLHDTVVCG_02-01-thanh-ben-khong-co-muc-hop-dong.png` | Thanh bên đủ 24 mục, **không có** "Hợp đồng Tư vấn" — bước 1 của phiếu là lối vào đã hết hiệu lực, không phải lỗi |
| `QLHDTVVCG_02-02-muc-HD-tu-van-lien-ket-baseline-2HD.png` | Bề mặt đã chấm: mục "HĐ tư vấn liên kết" trong Chi tiết vụ việc — thanh lọc 4 ô, 2 nút, bảng, phân trang "1-2 / 2 mục" |
| `QLHDTVVCG_02-03-loc-tu-khoa-ma-HD-con-1.png` | Lọc từ khóa theo mã hợp đồng: baseline 2 → còn **1** đúng bản ghi (L1) |
| `QLHDTVVCG_02-04-dropdown-chon-tu-van-vien.png` | Danh sách chọn tư vấn viên chỉ hiện `mã — họ tên (tổ chức)`, không lộ mã kỹ thuật |
| `QLHDTVVCG_02-05-o-tu-van-vien-go-tim-duoc.png` | Ô tư vấn viên **gõ tìm được**: gõ `PheDuyet` → 7 lựa chọn thu còn 1 |
| `QLHDTVVCG_02-06-loc-theo-tu-van-vien-con-1.png` | Lọc theo tư vấn viên: 2 → **1**, đúng hợp đồng có Bên B là người đã chọn (L6) |
| `QLHDTVVCG_02-07-loc-den-ngay-3108-con-1.png` | Lọc `Đến ngày 31/08/2026`: 2 → **1**, giữ HĐ kết thúc 25/08, loại HĐ kết thúc 30/12 (L9) |
| `QLHDTVVCG_02-08-ket-hop-2-dieu-kien-khong-tim-thay.png` | Kết hợp 2 điều kiện giao nhau rỗng → **0 kết quả** + câu "Không tìm thấy hợp đồng phù hợp" ⇒ đúng AND, đúng câu báo không có kết quả (L10) |
| `QLHDTVVCG_02-09-baseline-3-hop-dong.png` | Baseline mới **3 hợp đồng** sau khi dựng tiền đề `HDTV-20260807-0008` |
| `QLHDTVVCG_02-10-loc-tu-ngay-0107-con-2.png` | Lọc `Từ ngày 01/07/2026`: 3 → **2**, loại đúng HĐ bắt đầu 01/06 (L14) |
| `QLHDTVVCG_02-11-loc-den-ngay-3006-con-1.png` | Lọc `Đến ngày 30/06/2026`: 3 → **1**, chỉ còn HĐ kết thúc 20/06 (L15) |
| `QLHDTVVCG_02-12-cuon-ngang-trong-bang-du-11-cot.png` | Cuộn ngang **bên trong khung bảng** tới cuối: đủ 11 cột đọc được, không mất chữ; `25/08/2026` tô đỏ còn `20/06/2026` và `30/12/2026` màu thường |
| `QLHDTVVCG_02-13-do-o-man-hinh-1024-khong-tran.png` | Đo ở bề rộng **1024** (mức tối thiểu đặc tả ghi): trang không cuộn ngang, thanh lọc tự xuống 2 hàng gọn, không chữ đè chữ |
