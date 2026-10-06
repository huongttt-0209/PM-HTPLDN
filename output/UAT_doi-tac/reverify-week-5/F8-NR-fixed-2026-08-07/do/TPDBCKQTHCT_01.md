# TPDBCKQTHCT_01 — dòng 340 · 07/08/2026 18:17–18:28 · tài khoản ra verdict **`cbnv_dp_04`** (CB Nghiệp vụ Địa phương — **Sở Tư pháp An Giang**) · bản dựng `assets/index-BbPPdate.js`

> Chuẩn chấm khóa: [`chuan/TPDBCKQTHCT_01.md`](../chuan/TPDBCKQTHCT_01.md) — **5 vế: C1a `MATCH` · C1b `GAP` · C2 `MATCH` · C3 `MATCH` · C4 `GAP`**.
> Tiền đề đã xác minh: [`chuan/TPDBCKQTHCT_01-TIEN-DE-DA-XAC-MINH.md`](../chuan/TPDBCKQTHCT_01-TIEN-DE-DA-XAC-MINH.md).
> Đọc lại dòng 340 lúc 18:17: `Trạng thái` = `Fail` · `Dopai` = `Open` · `Ảnh/vieo 1` = `TPDBCKQTHCT_01.webm` · **`Trạng thái dev fix` (R) = `Fixed`** (đúng trạng thái yêu cầu ⇒ chạy) · `Kết quả verify` (T) đang chứa nội dung lượt 03:07 — **đã đọc, KHÔNG dùng làm chuẩn chấm, KHÔNG ghi đè**.

## Vân tay bản dựng — đầu và cuối phiên

| Mốc | Giờ đo | Bó mã | `last-modified` | `etag` |
|---|---|---|---|---|
| **Đầu phiên** | 07/08/2026 18:17:21 | `assets/index-BbPPdate.js` | Fri, 07 Aug 2026 06:47:57 GMT | `"6a757f9d-428"` |
| **Cuối phiên** | 07/08/2026 18:28:30 | `assets/index-BbPPdate.js` | Fri, 07 Aug 2026 06:47:57 GMT | `"6a757f9d-428"` |

**Không đổi giữa hai mốc** ⇒ mọi quan sát dưới đây đều rơi trên cùng một bản dựng, khớp tham chiếu prompt cấp.
Lượt đo cũ (03:07) chạy trên `index-D4Buvu4S.js` ⇒ **đây là bản dựng khác**, phép đo cũ không dùng lại được.

## Tài khoản thực dùng

| Vai trò trong phiếu | Tài khoản | Đơn vị | Dùng để |
|---|---|---|---|
| **Ra verdict** | **`cbnv_dp_04`** — *CB Nghiệp vụ - Địa phương #04*, vai trò hiển thị "Cán bộ Nghiệp vụ Địa phương", cấp `DP` | `00000000-0000-4000-8002-000000000006` — **Sở Tư pháp An Giang** (tên đọc được trên màn Nhật ký hệ thống) | Bấm [Trình duyệt KQ] **bằng giao diện thật** |
| Nhận thông báo (`C2`) | **`cbpd_dp_04`** — *CB Phê duyệt - Địa phương #04*, cấp `DP` | **cùng** `00000000-0000-4000-8002-000000000006` | **CHỈ ĐỌC** thông báo. 🔴 **KHÔNG bấm [Phê duyệt]/[Từ chối]** |
| Đọc nhật ký (`C3`) | `admin` — *Quản trị hệ thống* | Bộ Tư pháp | **CHỈ đọc nhật ký.** Không dùng để chấm vế khác |

Cặp CB Nghiệp vụ ↔ CB Phê duyệt **trùng đơn vị** ⇒ đo được `C2` đúng nghĩa "cùng đơn vị". **Không dùng Rule 7, không lệch prompt.**

## Đợt và bản ghi đã dùng

**`DOT-SO_BO_NAM-2026-1`** (`e9909d96-1391-463b-8072-b1b56c319f8e`) — biểu mẫu **21a**, ưu tiên 1 theo chuẩn chấm §4.5.
Báo cáo của Sở Tư pháp An Giang trong đợt: `c1b1045d-007c-4104-a169-e267010557a0`.
**Đợt ưu tiên 2 (`DOT-SO_BO_6_THANG-2026-1`) KHÔNG dùng** — lượt ① đã chốt được, sàn biến thể N = 1 (§10).

**Đọc lại ngay trước khi đo (18:18–18:20), TRƯỚC KHI ĐỘNG VÀO:**

| Trục | Giá trị trước |
|---|---|
| Trạng thái bản ghi **ĐỢT** | `TAO_DOT` (version 1) |
| **Trạng thái nộp của đơn vị mình** | `DANG_LAP` |
| Trạng thái **BÁO CÁO** | `DU_THAO` |
| Số liệu đã lưu | **đúng 3 khóa** (`soVuViec` 3 · `tongChiPhi` 0 · `soDnDuocHoTro` 0) — **không khóa nào thuộc bộ 13 chỉ tiêu Biểu 21a** |
| Nhận xét, kiến nghị | rỗng |

**Màn hình trước khi động vào** (đọc từng ô, không nhìn lướt): chỉ tiêu **1 → 11** hiển thị giá trị kèm dấu `(HT)` trong một ô chữ **không nhập được** (chỉ tiêu 1 = `1`, chỉ tiêu 2→11 = `0`), mỗi dòng chỉ có thêm một ô *Ghi chú*; chỉ tiêu **12 và 13** có ô nhập số và đang **để trống**. — Đây **đúng** `srs-v3.5.md:6678`–`:6688` (cột −1→−11 do hệ thống tính) và `:6689`/`:6690` (chỉ −12, −13 là *"Nhập thủ công"*), **không phải lỗi**.

## Cổng TĐ-UI — dựng báo cáo hoàn chỉnh **chỉ bằng giao diện** (§5.1)

🔴 **Không dùng bất kỳ đường dữ liệu nào để bơm số liệu.** Không gọi lệnh ghi số liệu trực tiếp, không kèm số liệu vào bước bắt đầu lập báo cáo. Mọi giá trị dưới đây do **gõ trên màn** và **bấm nút trên màn** sinh ra. (Bước [Lập báo cáo] **không phát sinh** — đơn vị đã sẵn ở "Đang lập".)

| Bước | Thao tác trên màn | Kết quả đo được |
|---|---|---|
| 1 | Gõ **1207** vào chỉ tiêu 12 (KP chi HĐ khác) và **1308** vào chỉ tiêu 13 (KP xã hội hóa) | Hai ô nhận đúng giá trị |
| 2 | Bấm **[Lưu nháp]** của khối biểu mẫu | Gửi đi **1** lệnh ghi (không nhân đôi) · **1** khung thông báo, **1** mốc giờ: **"Đã lưu nháp thành công"** |
| 3 | **Tải lại trang bằng địa chỉ** | Chỉ tiêu 12 = `1207`, chỉ tiêu 13 = `1308` **giữ nguyên** |
| 4 | Đọc lại bản ghi từ máy chủ | 🔴 **Số liệu đã lưu nay có đủ 13 chỉ tiêu Biểu 21a** (16 khóa = 13 chỉ tiêu + 3 khóa cũ). 11 chỉ tiêu hệ thống tính **đã được lưu cùng lúc** với 2 ô nhập tay: `soTvvKienToan` 1, mười chỉ tiêu còn lại 0, `kpHoatDongKhac` 1207, `kpXaHoiHoa` 1308 |
| 5 | Ghi dấu nhận dạng **`QA-F8-340-20260807-1820`** vào ô *Nhận xét, kiến nghị*, bấm **[Lưu nháp] của chính khối Nhận xét** | Lưu được — đọc lại bản ghi thấy đúng chuỗi trên |

**⇒ Cổng TĐ-UI ĐẠT theo nhánh 1 của bảng §5.1**: 13/13 chỉ tiêu có giá trị **trong dữ liệu đã lưu**, dựng **hoàn toàn bằng giao diện**.

> 🔴 **Đây chính là chỗ đã đổi so với lượt 03:07.** Lúc đó dữ liệu đã lưu chỉ có 3 khóa lạ, không có chỉ tiêu nào của Biểu 21a ⇒ máy chủ báo còn thiếu 11 chỉ tiêu. Trên bản dựng hiện tại, thao tác lưu nháp trên màn ghi luôn cả 11 chỉ tiêu hệ thống tính, nên báo cáo trở thành "hoàn chỉnh" đúng nghĩa `srs-fr-15-ct-htpldn.md:802` (*"giá trị 0 là đã điền"*).

**Không bấm [Làm mới]:** cổng đã đạt ở bước 4, mục tiêu của bước đó (xem 11 chỉ tiêu hệ thống có được nạp/lưu không) đã có câu trả lời ⇒ không thêm thao tác đổi dữ liệu ngoài phần cần cho vế đang đo.

## Kết quả từng vế

| Vế | Quan hệ | Kỳ vọng phiếu | Web thực tế (số liệu quyết định) | Đạt? |
|---|---|---|---|---|
| **C1a** | MATCH | *"Chuyển trạng thái … Đang lập báo cáo → Chờ duyệt kết quả"* — phần chấm được: thao tác **đi lọt** và trạng thái **người dùng thấy** + bản ghi **BÁO CÁO** chuyển đúng (`:803` · `:829` · `:802` · `:1389` · `:1418`) | **Đường 1 (giao diện, bấm thật)** — 18:23:22 bấm **[Trình duyệt KQ]** → hộp thoại xác nhận *"Trình duyệt kết quả?"* → bấm **[Đồng ý]**. Thao tác **KHÔNG bị chặn**, **không** có thông báo "còn thiếu" nào. Nhãn *Trạng thái* trên màn chuyển sang **"Chờ duyệt kết quả"**; thanh tiến trình: *Tạo đợt* ✓ · *Đang lập BC* ✓ · ***Chờ duyệt KQ* = bước hiện tại**. **Tải lại trang bằng địa chỉ** → vẫn **"Chờ duyệt kết quả"**, biểu mẫu chuyển sang chế độ chỉ đọc (không còn ô nhập, không còn nút [Lưu nháp]/[Trình duyệt KQ]), 13/13 dòng chỉ tiêu hiển thị giá trị, ô Nhận xét hiện đúng `QA-F8-340-20260807-1820`. **Đường 2 (đối chứng độc lập — đọc lại bản ghi từ máy chủ)** — **BÁO CÁO** `c1b1045d-…`: `DU_THAO` → **`CHO_PHE_DUYET`** (`:1418`); **trạng thái nộp của Sở Tư pháp An Giang**: `DANG_LAP` → **`CHO_DUYET`** (`:1389`). Hai đường khớp nhau ⇒ dừng | ✅ |
| **C1b** | **GAP** — *không chấm* | cùng câu trên, hiểu theo nghĩa đen: trường trạng thái của bản ghi **ĐỢT** phải đi `DANG_LAP_BC → CHO_DUYET_KQ` | **Ghi nhận hiện trạng:** trạng thái bản ghi **ĐỢT** trước thao tác = `TAO_DOT`, sau thao tác = **`TAO_DOT`** (version 1 → 1, **không đổi**). Nhãn người dùng nhìn thấy suy từ trục *trạng thái nộp của từng đơn vị*, không từ trục đợt. **Không ép trường này bằng bất kỳ đường nào.** Đặc tả tự mâu thuẫn (`:789` đòi đợt đã ở `DANG_LAP_BC`; `:1512` giao bước đó cho FR-XI-06 nhưng phần xử lý `:739`–`:747` không có bước nào đụng trạng thái đợt; `:1368` cho đợt **một** giá trị trong khi phạm vi đợt là 83 đơn vị theo `:1367`) ⇒ **route BA**, 🔴 **CẤM lấy làm lý do FAIL** | — *(GAP)* |
| **C2** | MATCH | *"Gửi thông báo cho cán bộ phê duyệt cùng đơn vị"* (`:804` · `:819` · `:1552`) | **Đường 1 (giao diện, tài khoản `cbpd_dp_04`)** — mở chuông **Thông báo**: có mục **"Báo cáo đợt "QA Reverify CTBC 715 v2 fresh" đã được trình duyệt"** · nội dung *"Mã: DOT-SO_BO_NAM-2026-1. Vui lòng xem xét và phê duyệt."* · nhãn thời gian **"3 phút trước"** (đo lúc ~18:26, khớp mốc bấm 18:23). **Đường 2 (đối chứng độc lập — danh sách thông báo cá nhân của CHÍNH tài khoản đó)** — bản ghi `68b7f28f-c687-40a6-955a-0482d2e1a467`, loại `PHE_DUYET`, gắn với **đúng đợt** `e9909d96-…`, **người nhận** `6fa7307f-…` = chính `cbpd_dp_04` (khác `85bdef3b-…` là người trình), **giờ tạo `2026-08-07T11:23:25.464Z`** — nằm **giữa** hai dòng nhật ký của chính lượt bấm (`.431Z` và `.496Z`) ⇒ nối khít với thao tác. Không bấm [Phê duyệt]/[Từ chối] | ✅ |
| **C3** | MATCH | *"Lưu vết thao tác theo quy định"* (`:805` · `:1568`) | ⚠️ Tài khoản CB Nghiệp vụ **không có quyền đọc nhật ký** (bị từ chối quyền) ⇒ đọc bằng tài khoản **Quản trị hệ thống**, khai rõ, **không dùng để chấm vế khác**. **Đường 1 (giao diện — màn Nhật ký hệ thống)** — **2 dòng lúc `07/08/2026 18:23:25`**, người dùng *"CB Nghiệp vụ - Địa phương #04"*, đơn vị **"Sở Tư pháp An Giang"**, module *"CT HTPLDN"*, loại thao tác **"Gửi"**: một dòng cho `DOT_BAO_CAO` mã `e9909d96`, một dòng cho `BAO_CAO_CT_HTPL` mã `c1b1045d`. Kèm 2 dòng **"Cập nhật"** lúc `18:20:56` và `18:21:59` ứng đúng 2 lần lưu nháp. **Đường 2 (đối chứng độc lập — đọc danh sách nhật ký)** — bản ghi `ec3e4a02-…` (`DOT_BAO_CAO` / `e9909d96-…` / `SUBMIT` / `2026-08-07T11:23:25.496Z` / kết quả 200) và `fcdc5129-…` (`BAO_CAO_CT_HTPL` / `c1b1045d-…` / `SUBMIT` / `11:23:25.431Z`), cùng một phiên làm việc `2f8ab5b0-…` với 2 lần lưu nháp ⇒ **nối được** mã bản ghi + mốc giờ + người thực hiện với lượt bấm trên màn | ⏸ *(xem đính chính bên dưới)* |
| **C4** | **GAP** — *không chấm* | *"Trình thành công, hệ thống hiển thị «Đã trình phê duyệt báo cáo»"* — SRS **IM LẶNG** (Outputs `:810`–`:814`, Postconditions `:816`–`:819`, Error Handling `:821`–`:825` chỉ có một dòng lỗi; `:1170` không ghi thông báo thành công) | **WEB HIỆN TẠI: đúng kỳ vọng đối tác.** Bộ bắt thông báo cài **TRƯỚC** khi bấm, **không lọc trùng**, đọc chữ người dùng nhìn thấy; tự kiểm cho **1** bộ đo đang sống ⇒ số liệu hợp lệ. Kết quả: **1** khung thông báo, **1** mốc giờ duy nhất, nội dung **"Đã trình phê duyệt báo cáo"** — **trùng khít nguyên văn** chuỗi đối tác chờ. Kèm **1** lệnh gửi đi (không nhân đôi, không bấm lặp). 🔴 Vẫn **không chấm đạt/lỗi** vì SRS im lặng ⇒ route BA (mục đích: **bổ sung vào đặc tả**, không chặn bàn giao) | — *(GAP)* |

**Triệu chứng gốc của đối tác — trả lời thẳng:** mô tả *"Hệ thống không cập nhật trạng thái mặc dù có thông báo trình duyệt thành công"* **KHÔNG còn tái hiện**. Lần này có thông báo thành công **và** trạng thái đổi thật: nhãn trên màn sang "Chờ duyệt kết quả" và **giữ nguyên sau khi tải lại trang bằng địa chỉ**, đọc lại bản ghi từ máy chủ thấy báo cáo sang "Chờ phê duyệt" và trạng thái nộp của đơn vị sang "Chờ duyệt".

**Chống Pass oan đã làm:** tiền đề dựng **UI-ONLY** — không bơm 13 chỉ tiêu bằng đường dữ liệu (đây là bẫy đã làm hỏng lượt 03:07); **đọc lại bản ghi từ máy chủ sau thao tác** trên cả 3 trục trạng thái thay vì tin thông báo (đúng vế của bug gốc); tải lại trang **bằng địa chỉ** rồi đọc lại nhãn, không chấm bằng màn đang mở; đếm thông báo theo **mốc giờ khác nhau** (1) chứ không theo độ dài mảng, kèm **tự kiểm số bộ đo = 1**; đếm **số lệnh gửi đi** (1) để loại double-submit; đọc chữ bằng nội dung **nhìn thấy được**, không gom node ẩn; đọc thông báo `C2` bằng **chính tài khoản CB Phê duyệt** (đọc bằng tài khoản khác sẽ không thấy) và đã **xác minh trùng đơn vị** trước; đo bản ghi **mới của đơn vị `_04`**, không dùng lại bản ghi mà lượt trước đã tác động (Sở Tư pháp Hà Nội); **đo vân tay bản dựng đầu và cuối phiên**.

**Chống Fail oan đã kiểm:** **không** Fail vì 11 chỉ tiêu không có ô nhập — `srs-v3.5.md:6678`–`:6688` giao các chỉ tiêu đó cho hệ thống tính, chỉ `:6689`/`:6690` là *"Nhập thủ công"*, màn đang làm **đúng**; **không** Fail vì bản ghi ĐỢT vẫn đứng `TAO_DOT` — đó là vế `C1b` GAP; **không** Fail vì nhãn nút là *"Trình duyệt KQ"* thay vì *"Trình phê duyệt"* như phiếu viết (`:1170` khai đúng chữ giao diện, phiếu không chấm nhãn); **không** Fail vì nhãn trạng thái đọc là "Đang lập BC"/"Chờ duyệt KQ" trên thanh tiến trình (`:1195`/`:1196`); **không** Fail vì ô Nhận xét bỏ trống hay vì các chỉ tiêu bằng 0 (`:802` ghi rõ cả hai đều không phải "chưa đầy đủ"); **không** coi việc tài khoản CB Nghiệp vụ không đọc được nhật ký là lỗi của phiếu — đó là blocker vận hành.

### 🔴 Đính chính vế `C3` (điều phối rà lại sau khi phiếu đóng — KHÔNG đổi ô R)

Bảng trên **ban đầu chấm `C3` = ✅**, nay **hạ về `⏸ chưa chốt`** cho đúng chuẩn chấm đã khóa:

- Chuẩn chấm dòng `:57` quy định **Đường 1 của `C3`** là `GET /api/v1/audit-logs` **bằng chính phiên
  `cbnv_dp_04`**; màn Nhật ký hệ thống của QTHT chỉ là **đối chứng**. Thực tế **Đường 1 bị từ chối quyền**
  ⇒ cả hai đường bằng chứng đều đọc bằng tài khoản **Quản trị hệ thống**, tức chỉ còn **một nguồn**.
- Chuẩn chấm dòng `:340` đã dự liệu đúng ca này: *"Nếu tài khoản thiếu quyền đọc log → **blocker vận hành,
  không phải bug**: ghi ⏸ cho riêng C3"*; dòng `:196` còn ghi tài khoản `admin` **"CẤM dùng ra verdict"**.

**Không đổi ô R.** Dòng 340 **CÓ bug gốc thật** (`Trạng thái` = `Fail`, `Kết quả thực tế` = *"Hệ thống không
cập nhật trạng thái mặc dù có thông báo trình duyệt thành công"*) và ô `DEV phản hồi lần 1` **RỖNG** (không có
nội dung BA chốt) ⇒ theo tiêu chí user chốt cuối (*bug gốc + nội dung BA chốt*), chuẩn chấm rút về **đúng bug
gốc**, mà bug gốc nằm trọn ở `C1a` — đã đạt bằng **hai đường độc lập thật**. `C3` ⏸ vì thiếu quyền đọc nhật ký
của vai trò nghiệp vụ, **không** phải vì phần mềm sai.

## Verdict → ô R

**`Test done`** — **bug gốc đã hết lỗi**: trình được bằng giao diện, vế `C1a` (chính là bug gốc) và `C2` đều
đạt bằng hai đường độc lập, trên một lượt bấm thật với tiền đề dựng hoàn toàn bằng màn hình. `C3` ⏸ (blocker
vận hành, xem đính chính ngay trên).
Hai vế `GAP` (`C1b` · `C4`) **ghi đầy đủ ở trên nhưng không chặn `Test done`** theo luật lô H1 §2 — và ở `C4` thì **web đang đúng y kỳ vọng đối tác**.
Ô `Kết quả verify` (T) và ô `Ảnh/video verify` (U): **không đụng** (verdict Pass).

> Không viết *"fix đã có tác dụng"*: không có ảnh lỗi cũ của chính QA trên bản dựng cũ cho **đúng bản ghi mới này** ⇒ chỉ kết luận **hiện trạng đúng so với đặc tả**.
> **Giới hạn hiệu lực:** đo trên môi trường nội bộ `https://18.143.165.120.nip.io`, bản dựng `index-BbPPdate.js`; đối tác nghiệm thu trên môi trường khác.

## Câu hỏi BA còn treo (không chặn bàn giao)

- **Q-A (`C1b`)** — vòng đời trạng thái của đợt báo cáo gắn vào **bản ghi ĐỢT** hay **bản ghi nộp của từng đơn vị**? 🔗 **CÙNG GỐC với câu Q1 đã mở** (phiếu 343 · C2) ⇒ **liên kết, không mở câu trùng**; phần bổ sung là nhánh FR-XI-07 và mâu thuẫn `:789` ↔ `:1512`/`:746`.
- **Q-B (`C4`)** — khi trình phê duyệt thành công, hệ thống có phải hiển thị thông báo cho người trình không, và câu chữ chốt là gì? Đề nghị **bổ sung một dòng thông báo thành công vào bảng thông báo của FR-XI-07**. Hiện web đã hiển thị đúng chuỗi đối tác chờ.

## 🔴 Dữ liệu đã thay đổi trên môi trường (BẮT BUỘC khai)

| Đổi gì | Bản ghi | Env | Lúc |
|---|---|---|---|
| **Điền + lưu số liệu Biểu 21a** bằng **giao diện thật** (2 lần bấm [Lưu nháp]) | Báo cáo `c1b1045d-007c-4104-a169-e267010557a0` của **Sở Tư pháp An Giang** trong đợt `DOT-SO_BO_NAM-2026-1` (`e9909d96-1391-463b-8072-b1b56c319f8e`). Số liệu đã lưu: 3 khóa → **16 khóa** (đủ 13 chỉ tiêu Biểu 21a); chỉ tiêu 12 = `1207`, chỉ tiêu 13 = `1308`, 11 chỉ tiêu còn lại do hệ thống tính (`1` và mười số `0`) | `https://18.143.165.120.nip.io` (**nội bộ**) | 2026-08-07 18:20:56 và 18:21:59 |
| **Ghi dấu nhận dạng** vào ô *Nhận xét, kiến nghị* | cùng báo cáo trên — nội dung **`QA-F8-340-20260807-1820`**. `:802` ghi rõ ô này **không** tính vào điều kiện hoàn chỉnh | " | 2026-08-07 18:21:59 |
| 🔴 **TRÌNH PHÊ DUYỆT — thao tác không hoàn tác được bằng vai trò CB Nghiệp vụ** | Báo cáo `c1b1045d-…`: `DU_THAO` → **`CHO_PHE_DUYET`**. Trạng thái nộp của **Sở Tư pháp An Giang** trong đợt: `DANG_LAP` → **`CHO_DUYET`** | " | 2026-08-07 18:23:25 |
| ↳ hệ quả | Bản ghi **ĐỢT** **không đổi** (`TAO_DOT`, version 1). Đợt `DOT-SO_BO_6_THANG-2026-1` **không đụng tới** — vẫn `DANG_LAP`, còn nguyên cho lượt đo sau. Sinh 1 thông báo cho `cbpd_dp_04` + 2 dòng nhật ký "Gửi" | " | " |

**Không hoàn tác:** [Trình duyệt KQ] đi lọt ⇒ báo cáo sang "Chờ phê duyệt" và **CB Nghiệp vụ không tự đưa lại được**. Theo chuẩn chấm §3, **KHÔNG** nhờ `cbpd_dp_04` bấm [Từ chối] để hoàn tác — việc đó nằm ngoài vế của phiếu và sẽ tiêu hủy đúng trạng thái vừa đo. Bản ghi được để nguyên ở "Chờ phê duyệt". Không đụng dữ liệu đối tác.

## Ghi nhận (KHÔNG chấm, không kéo verdict)

1. **Ba khóa cũ trong số liệu đã lưu** (`soVuViec` = 3 · `tongChiPhi` = 0 · `soDnDuocHoTro` = 0) không thuộc bộ 13 chỉ tiêu Biểu 21a và không dòng nào trên bảng hiển thị chúng — vẫn còn nguyên sau lượt lưu. Trùng ghi nhận §9 mục 3 của chuẩn chấm, **không điều tra**.
2. **Tài khoản CB Nghiệp vụ không có quyền đọc nhật ký hệ thống** ⇒ phải mượn tài khoản quản trị để lấy đối chứng `C3`. Là **blocker vận hành**, không phải lỗi của phiếu; nêu để cân nhắc cấp quyền đọc nhật ký cho vai trò nghiệp vụ nếu quy trình cần.
3. **Mã lỗi lệch đặc tả** (`:825` khai một mã, hệ thống trả mã khác) — **lượt này không tái hiện** vì thao tác không còn bị chặn. Đã có ở bàn giao lô F5, **liên kết, không mở mục trùng**.

## Bug candidate (chưa đủ căn cứ xác nhận — đặc tả im lặng)

**`CAND-BC-NHANXET-01` · Bấm [Lưu nháp] ở khối biểu mẫu báo thành công nhưng chữ vừa gõ trong ô *Nhận xét, kiến nghị* bị mất.**

- **Xuất hiện tại:** bước dựng tiền đề bắt buộc (ghi dấu nhận dạng vào ô Nhận xét theo chuẩn chấm §4.3).
- **Hiện tượng đo được:** gõ `QA-F8-340-20260807-1820` vào ô *Nhận xét, kiến nghị* rồi bấm **[Lưu nháp] của khối biểu mẫu** → hiện thông báo **"Đã lưu nháp thành công"**; tải lại trang bằng địa chỉ thì ô Nhận xét **rỗng** (bộ đếm ký tự về `0 / 5000`) và đọc lại bản ghi thấy trường nhận xét **chưa có giá trị**. Gõ lại rồi bấm **[Lưu nháp] của chính khối Nhận xét** thì lưu được.
- **Vì sao chỉ là candidate:** màn có **hai** nút [Lưu nháp] thuộc hai khối khác nhau; đặc tả **không nói** mỗi nút phải lưu tới đâu, cũng không cấm phạm vi hẹp. Cần đặc tả hoặc BA chốt mới kết luận được là lỗi hay là thiết kế.
- **Còn thiếu để xác nhận:** một dòng đặc tả về phạm vi lưu của nút [Lưu nháp] trên màn Chi tiết đợt báo cáo.
- **Không kéo verdict phiếu 340:** ô Nhận xét **không** tính vào điều kiện báo cáo hoàn chỉnh (`:802`) và phiếu 340 không nhắc tới ô này.

## Ảnh

Một ảnh chụp trạng thái **trước khi bấm** [Trình duyệt KQ] (bảng 13 chỉ tiêu + nhãn "Đang lập báo cáo" + dấu nhận dạng): [`image/TPDBCKQTHCT_01-truoc-khi-trinh-1820.png`](../image/TPDBCKQTHCT_01-truoc-khi-trinh-1820.png). Chụp theo yêu cầu §5.1[7] của chuẩn chấm vì trạng thái này **không dựng lại được** sau khi trình.
**Không phải bằng chứng lỗi** — verdict là Pass ⇒ **không gắn vào bảng**, ô `Ảnh/video verify` giữ nguyên rỗng. Mọi số liệu quyết định đã ghi thẳng trong các bảng trên.
