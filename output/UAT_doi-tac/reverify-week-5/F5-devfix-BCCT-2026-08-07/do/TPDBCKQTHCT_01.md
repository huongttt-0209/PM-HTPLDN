# Phép đo — TPDBCKQTHCT_01 (dòng 340) · 2026-08-07 — **Trình phê duyệt báo cáo kết quả**

**Verdict: REOPEN** — nhưng **KHÔNG** theo nhánh triệu chứng đối tác mô tả.
Điểm hỏng đã **dịch chỗ**: thao tác [Trình duyệt KQ] **bị hệ thống từ chối** trong khi biểu mẫu trên màn
**đã hiện giá trị ở đủ 13/13 chỉ tiêu** ⇒ trúng đúng mệnh đề FAIL thứ hai của chuẩn chấm §6:
*"thao tác bị từ chối trong khi báo cáo ĐÃ điền đủ mọi chỉ tiêu của biểu mẫu đang áp dụng"*.

Chuẩn chấm: [`../chuan/TPDBCKQTHCT_01.md`](../chuan/TPDBCKQTHCT_01.md)

---

## 1. Điều kiện đo

| Mục | Giá trị |
|---|---|
| Env / bản dựng | `https://18.143.165.120.nip.io` · **`assets/index-D4Buvu4S.js`** (07/08/2026 02:23 VN) — đã tải lại trang bằng địa chỉ và đọc lại tên bó mã trong tab trước khi đo |
| Tài khoản ra verdict | **`cbnv_hn`** — `CB_NV_DP`, `capDonVi = DP`, `donViId = 00000000-0000-4000-8002-000000000001` (Sở Tư pháp Hà Nội) |
| Tài khoản đo vế C2 | **`cbpd_hn`** — `CB_PD_DP`, `capDonVi = DP`, **`donViId` trùng đúng `…8002-000000000001`** (đã xác minh bằng `/auth/me`, §4.2) |
| Tài khoản chỉ đọc nhật ký | `admin` — **chỉ đọc log cho vế C3**, không dùng ra verdict (chuẩn chấm §9.6) |
| Đợt đo chính | `DOT-SO_BO_NAM-2026-1` — `e9909d96-1391-463b-8072-b1b56c319f8e`, biểu mẫu **`MAU_21A`**, đơn vị ở `DANG_LAP` |
| Đợt đối chứng | `DOT-TRON_NAM-2026-1` — `a63a3214…`, biểu mẫu **`CA_HAI`**, đơn vị ở `DANG_LAP` |

> **Sai lệch so với chuẩn chấm §3.1 — khai rõ:** chuẩn ghi cặp `cbnv_dp_01` / `cbpd_dp_01`. Lô đo này dùng
> `cbnv_hn` / `cbpd_hn` — **cùng vai trò, cùng cấp ĐP, cùng một đơn vị** (đã xác minh `donViId` trùng), và là
> cặp tài khoản đã dùng xuyên suốt 5 phiếu trước của lô nên nối tiếp được tiền đề. Đây là thay thế
> **cùng vai trò + cùng cấp** đúng Rule 7, không đổi ĐP ↔ BN ↔ TW.

---

## 2. 🔴 Kết quả cốt lõi — bảng theo chuẩn chấm §4.8

| Mã đợt | Đơn vị | Chỉ tiêu **hiện giá trị** trên màn | Trạng thái **trước** khi bấm | Ngay sau bấm | Sau khi tải lại | CB PD nhận TB? | Mục nhật ký? |
|---|---|---|---|---|---|---|---|
| `DOT-SO_BO_NAM-2026-1` | Sở TP Hà Nội | **13/13** (1–11 = `0 (HT)`, 12 = `1207`, 13 = `1308`) | "Đang lập báo cáo" | 🔴 **BỊ CHẶN** — không đổi | 🔴 không đổi | 🚫 chưa đo được ở nhịp này | 🚫 chưa đo được ở nhịp này |

**Chuỗi mốc-giờ đã ghi trước khi bấm:** `QA-BCCT-20260807-0209-ghichu-ct1` (ô Ghi chú chỉ tiêu 1) ·
`QA-BCCT-20260807-0209-nhan-xet` (khối Nhận xét).

---

## 3. Vế C1 — 🔴 **FAIL**

### 3.1 Bằng chứng "đã điền đủ" (chuẩn chấm §6.1 bẫy 1 bắt buộc có)

Đọc thẳng từng ô của bảng **`Biểu mẫu 21a/TP/HTPLDN`** trên màn (xác định bảng bằng **tiêu đề thẻ**, không
bằng số dòng), 4 cột `Chỉ tiêu | Số liệu kỳ trước | Kỳ này | Ghi chú`, 13 dòng chỉ tiêu:

| # | Chỉ tiêu | Cột "Kỳ này" hiện gì | Có ô nhập không? |
|---|---|---|---|
| 1 | Số TVV kiện toàn | `0 (HT)` | ❌ **không có ô** |
| 2 | Cuộc tập huấn | `0 (HT)` | ❌ **không có ô** |
| 3 | Hội nghị đối thoại | `0 (HT)` | ❌ **không có ô** |
| 4 | VB trả lời UBND | `0 (HT)` | ❌ **không có ô** |
| 5 | VB TV mạng lưới TVV | `0 (HT)` | ❌ **không có ô** |
| 6 | HS tiếp nhận | `0 (HT)` | ❌ **không có ô** |
| 7 | HS giải quyết tổng | `0 (HT)` | ❌ **không có ô** |
| 8 | DN vừa | `0 (HT)` | ❌ **không có ô** |
| 9 | DN nhỏ | `0 (HT)` | ❌ **không có ô** |
| 10 | DN siêu nhỏ | `0 (HT)` | ❌ **không có ô** |
| 11 | KP hỗ trợ TVPL (NSNN) | `0 (HT)` | ❌ **không có ô** |
| 12 | KP chi HĐ khác | `1207` | ✅ ô nhập |
| 13 | KP xã hội hóa | `1308` | ✅ ô nhập |

⇒ **Không có chỉ tiêu nào bỏ trống trên màn.** 11 chỉ tiêu đầu **không hề có ô để trống** — chúng hiển thị
sẵn giá trị `0` kèm dấu `(HT)`. Theo `srs-fr-15-ct-htpldn.md:802` (BA chốt 2026-08-06):

```
:802  Ô để trống là **chưa điền**; giá trị **0 là đã điền** (đơn vị không phát sinh hoạt động trong kỳ
      vẫn phải nộp). `nhan_xet` **không** tính vào điều kiện này
```

Ảnh: [`../image/TPDBCKQTHCT_01-bi-chan-toast-hoan-chinh-bao-cao.png`](../image/TPDBCKQTHCT_01-bi-chan-toast-hoan-chinh-bao-cao.png)

### 3.2 Thao tác bị từ chối

Bấm **[Trình duyệt KQ]** → hộp xác nhận *"Trình duyệt kết quả?"* → **[Đồng ý]**:

```
POST /api/v1/dot-bao-caos/e9909d96-…/submit-bc      body {"version":1}
→ 422
{"success":false,"error":{"code":"ERR-VAL-XI-07-02",
  "message":"Vui lòng hoàn chỉnh báo cáo trước khi trình",
  "details":{"chiTieuConThieu":[
    "1. Số TVV kiện toàn","2. Cuộc tập huấn","3. Hội nghị đối thoại","4. VB trả lời UBND",
    "5. VB TV mạng lưới TVV","6. HS tiếp nhận","7. HS giải quyết tổng","8. DN vừa",
    "9. DN nhỏ","10. DN siêu nhỏ","11. KP hỗ trợ TVPL (NSNN)"]}}}
```

**Danh sách "còn thiếu" trùng khít 11 chỉ tiêu duy nhất KHÔNG có ô nhập trên màn.**
Lặp lại **3 lần** qua giao diện (19:53:03 · 19:53:27 · 19:53:51 UTC) — kết quả giống hệt.

Trạng thái đọc lại sau khi bị chặn: màn vẫn `Đang lập báo cáo`; máy chủ `DOT_BAO_CAO.trangThai = TAO_DOT`,
`trangThaiNop = DANG_LAP`, `baoCao.trangThai = DU_THAO` — **không đổi**.

### 3.3 Vì sao đây KHÔNG rơi vào bẫy FAIL-oan số 1

Chuẩn chấm §6.1 bẫy 1 loại trừ trường hợp *"bấm khi báo cáo còn **ô trống**"*. Ở đây **không có ô trống**:
với 11 chỉ tiêu đó **không tồn tại ô nào cả**, và giá trị đang hiển thị là `0` — mà `:802` nói thẳng
*"giá trị 0 là đã điền"*. Đúng câu tiếp theo của `:802` còn dự liệu chính tình huống này:
*"đơn vị không phát sinh hoạt động trong kỳ **vẫn phải nộp**"*.

Cán bộ **không có bất kỳ đường nào** trên màn để làm khác đi: không sửa được 11 ô (không có ô), mà giá trị
hệ thống tự đưa ra lại bị chính hệ thống từ chối. ⇒ điều kiện `:829` (*"Given CB NV chọn BC hoàn chỉnh …
Then … đợt BC → CHO_DUYET_KQ"*) **không thể đạt được** qua luồng phiếu mô tả.

Đối chiếu thêm phần dữ liệu đầu vào của chức năng lập BC:
- `:731` — `so_lieu` | Bắt buộc **Y** | Mặc định **"Gợi ý từ HT"** | Nguồn **"Nhập tay / Auto"**
- `:743` — bước 5: *"**Gợi ý số liệu**: tổng hợp từ TẤT CẢ hoạt động HTPL của đơn vị trong kỳ…"*
- `:744` — bước 6: *"CB NV **nhập/chỉnh sửa** số liệu…"*

### 3.4 Tái hiện trên bản ghi thứ hai (loại trừ "lỗi của riêng 1 bản ghi")

Đợt `DOT-TRON_NAM-2026-1` (biểu mẫu **`CA_HAI`**, đơn vị `DANG_LAP`) → `submit-bc` → **422**, cùng mã
`ERR-VAL-XI-07-02`, danh sách thiếu là **cả 13** chỉ tiêu (đợt này chưa nhập 12/13).
⇒ Không phải sự cố cục bộ của một bản ghi.

### 3.5 Đã loại trừ khả năng "chỉ là chưa bấm [Làm mới]"

[Làm mới] mở hộp xác nhận: *"Làm mới sẽ cập nhật các chỉ tiêu 1-11 từ hệ thống. Dữ liệu nhập thủ công
(cột 12, 13) và ghi chú sẽ được giữ nguyên. Tiếp tục?"* → bấm **[Đồng ý]** →
**0 yêu cầu gửi đi**, giá trị trên màn không đổi. Bấm [Lưu nháp] sau đó, phần số liệu gửi lên vẫn là
**5 khóa số**: `soVuViec` · `kpXaHoiHoa` · `tongChiPhi` · `soDnDuocHoTro` · `kpHoatDongKhac` — **không hề có**
11 khóa của chỉ tiêu 1–11. Trình lại → vẫn 422, vẫn đúng 11 chỉ tiêu đó.

> **Tự đính chính (ghi lại để người sau không lặp):** lần thử đầu tôi bấm [Làm mới] rồi bấm [Lưu nháp] sau 3
> giây và tưởng [Làm mới] đã chạy. Đọc lại ảnh mới thấy hộp xác nhận vẫn đang mở — **[Làm mới] chưa từng
> chạy**. Đã làm lại có bấm [Đồng ý]; kết quả nêu trên là của lần làm lại.

### 3.6 Định vị điểm hỏng (chẩn đoán bổ trợ — **không phải vế chấm**)

Đọc chính bó mã giao diện đang chạy (`assets/index-D4Buvu4S.js`) thấy bảng khai 13 chỉ tiêu:

```js
[{key:"soTvvKienToan",     label:"1. Số TVV kiện toàn",      auto:!0},   // …1–11 đều auto:true
 …
 {key:"kpHoTroTvpl",       label:"11. KP hỗ trợ TVPL (NSNN)",auto:!0},
 {key:"kpHoatDongKhac",    label:"12. KP chi HĐ khác",       auto:!1},
 {key:"kpXaHoiHoa",        label:"13. KP xã hội hóa",        auto:!1}]
```

Giao diện chủ đích coi 11 chỉ tiêu đầu là **do hệ thống tự tính** (`auto: true`, hiển thị `(HT)`) — khớp
`:743`. Nhưng phần lưu của giao diện không gửi 11 khóa này, còn phần kiểm tra "BC hoàn chỉnh" ở máy chủ lại
đòi chúng phải có mặt trong dữ liệu đã lưu. Hai bên đang hiểu khác nhau về cùng một điều.

**Kiểm chứng:** ghi thẳng 11 khóa với giá trị `0` qua đường dữ liệu → máy chủ **chấp nhận và lưu đủ 13 khóa**
(`PATCH …/bao-cao` → 200). Nghĩa là chỗ lưu không thiếu gì; thiếu ở chỗ 11 giá trị đó không bao giờ được ghi.

---

## 4. Vế C2, C3 — đo được nhờ ép qua tiền đề, **✅ ĐẠT**

> 🔴 **Khai rõ:** vì luồng giao diện bị chặn (§3), tôi **ép tiền đề bằng đường dữ liệu**: ghi 11 khóa `= 0`
> rồi gọi `submit-bc`. Đây **KHÔNG** phải đường đo của phiếu và **không** dùng để gỡ verdict C1 — chỉ để
> biết C2/C3 còn nguyên hay đã hỏng theo. Thao tác này **đã đổi trạng thái** đợt `e9909d96…` (xem §6).

`POST …/submit-bc {"version":1}` → **200**. Đọc lại ngay sau đó:

| Trục | Trước | Sau |
|---|---|---|
| `BAO_CAO_CT_HTPL.trangThai` (`:1418`) | `DU_THAO` | ✅ **`CHO_PHE_DUYET`** — đúng `:803` vế đầu |
| `DOT_BAO_CAO_DON_VI_NOP.trangThai_nop` (`:1389`) | `DANG_LAP` | `CHO_DUYET` |
| `DOT_BAO_CAO.trangThai` (`:1368`) | `TAO_DOT` | `TAO_DOT` — **không đổi** (xem §5) |
| Nhãn trạng thái **trên màn** sau khi tải lại trang | "Đang lập báo cáo" | ✅ **"Chờ duyệt kết quả"**, thanh tiến trình nhảy sang bước 3 "Chờ duyệt KQ" |

Ảnh: [`../image/TPDBCKQTHCT_01-sau-khi-trinh-thanh-cong-man-hien-cho-duyet-kq.png`](../image/TPDBCKQTHCT_01-sau-khi-trinh-thanh-cong-man-hien-cho-duyet-kq.png)

### 4.1 C2 — ✅ MATCH (`:804` + `:852` + `:1552`)

Đăng nhập **`cbpd_hn`** (phiên riêng, không dùng phiên đang đo) → hộp thông báo có mục mới:

```
2026-08-06T20:01:04.735Z | PHE_DUYET | Báo cáo đợt "QA Reverify CTBC 715 v2 fresh" đã được trình duyệt
```

Trùng đúng mốc giờ lượt trình (`20:01:04`) và **trỏ đúng tên đợt vừa trình** — không phải thông báo tồn từ
đợt cũ (chuẩn chấm §6.2 bẫy 4). `donViId` của `cbpd_hn` trùng `cbnv_hn` ⇒ đúng "cùng đơn vị".

### 4.2 C3 — ✅ MATCH (`:805`)

Nhật ký hệ thống (đọc bằng `admin`, khai rõ theo §9.6) quanh mốc giờ:

```
2026-08-06T20:01:04.751Z | DOT_BAO_CAO       | SUBMIT | e9909d96…
2026-08-06T20:01:04.715Z | BAO_CAO_CT_HTPL   | SUBMIT | 4db99158…
2026-08-06T20:00:57.161Z | BAO_CAO_CT_HTPL   | UPDATE | …
```

Có mục ứng với thao tác trình, đúng bản ghi, đúng mốc giờ. Các lượt bị chặn ở §3 **cũng** được ghi nhật ký
(`19:53:03` · `19:53:27` · `19:53:51`).

---

## 5. 🔴 Triệu chứng đối tác mô tả — **KHÔNG tái hiện**, và phần lệch còn lại **không được chấm**

Phiếu ghi *"Hệ thống không cập nhật trạng thái mặc dù có thông báo trình duyệt thành công"*.
Ở lượt trình **đi lọt** (§4): trạng thái **có** đổi — màn đọc được **"Chờ duyệt kết quả"** và **giữ nguyên
sau khi tải lại trang bằng địa chỉ**, CB PD cùng đơn vị nhìn thấy báo cáo chờ duyệt.
⇒ Nhánh triệu chứng gốc **không còn**.

Phần còn lệch: trường `DOT_BAO_CAO.trang_thai` ở máy chủ vẫn `TAO_DOT` (cả 3 đợt trên môi trường đều
`TAO_DOT`, kể cả đợt đã có đơn vị ở `DANG_LAP`/`CHO_DUYET`). Nhãn người dùng nhìn thấy đang được suy ra từ
**trục ĐƠN VỊ**.

**KHÔNG chấm FAIL điểm này** — chuẩn chấm §7(3) đã khóa trước:
> *"⚠️ **Hệ quả cho phép đo:** KHÔNG chấm FAIL chỉ vì trạng thái nộp của đơn vị vẫn là 'Đang lập' sau khi
> trình — không dòng SRS nào đòi trục đơn vị đổi ở bước này."*

và §6.1 bẫy 3 cấm kết luận từ nhầm trục. Đặc tả **tự mâu thuẫn** ở chỗ này:
- `:1512` (bảng chuyển trạng thái) khai `TAO_DOT → DANG_LAP_BC | CB NV bắt đầu lập BC | FR-XI-06`,
  **nhưng** toàn bộ Processing của FR-XI-06 (`:739`–`:747`) **không có bước nào** đụng `DOT_BAO_CAO.trang_thai`
  — bước 8 (`:746`) chỉ đặt `DOT_BAO_CAO_DON_VI_NOP.trang_thai_nop = DANG_LAP`.
- Một đợt dùng chung cho ~83 đơn vị (`:621`/`:646`/`:1398`) nhưng `:1368` chỉ có **một** giá trị.

⇒ **GAP**, chuyển câu hỏi BA (§7 chuẩn chấm mục 3), không lật verdict.

---

## 6. Dữ liệu QA đã dựng / đã đổi — cần biết để dọn

| Bản ghi | Đã làm gì | Trạng thái để lại |
|---|---|---|
| Đợt `DOT-SO_BO_NAM-2026-1` (`e9909d96…`) | ghi 11 khóa chỉ tiêu `= 0` + gọi `submit-bc` để ép tiền đề đo C2/C3 | đơn vị `CHO_DUYET`, báo cáo `CHO_PHE_DUYET` — **QA đổi, không phải người dùng thật** |
| Đợt `DOT-TRON_NAM-2026-1` (`a63a3214…`) | chỉ gọi `submit-bc` để đối chứng → 422 | **không đổi** |
| Chuỗi mốc-giờ | `QA-BCCT-20260807-0209-*` trong ô Ghi chú + Nhận xét | dữ liệu thử, xóa được |

---

## 7. Bẫy đã kiểm và loại trừ

| Bẫy (chuẩn chấm) | Đã làm gì |
|---|---|
| §6.1-1 FAIL oan vì còn ô trống | Đọc từng ô 13 dòng: **không ô nào trống**; 11 dòng đầu **không có ô** và đang hiện `0` (§3.1) |
| §6.1-2 nhầm `nhan_xet` là bắt buộc | Không dùng; `:802` ghi rõ `nhan_xet` không tính |
| §6.1-3 nhầm trục trạng thái | Ghi đủ **cả 3 trục** riêng biệt (§4); phần lệch trục ĐỢT **không** dùng để chấm (§5) |
| §6.1-4 sai vai trò | Bấm bằng `cbnv_hn` = `CB_NV_DP`, đúng tác nhân `:784`/`:712` |
| §6.1-5 CB PD khác đơn vị | Đã xác minh `donViId` trùng bằng `/auth/me` trước khi đo C2 |
| §6.1-6 FAIL vì câu chữ thông báo | Không chấm C4 |
| §6.2-1 tin vào thông báo thành công | Không dùng thông báo làm bằng chứng; đọc lại trạng thái từ máy chủ **và** tải lại trang |
| §6.2-2 tab mở lâu | Tải lại bằng địa chỉ, đọc lại tên bó mã trong tab |
| §6.2-3 nút biến mất ⇒ kết luận đạt | Không dùng |
| §6.2-5 dùng `admin` ra verdict | `admin` **chỉ** đọc nhật ký (C3); verdict do `cbnv_hn` |
| §6.2-6 bản ghi cũ đóng băng | Lượt trình là **lượt mới** trên bản dựng hiện hành |
| §6.3 thông báo hiện 2 lần | Bộ bắt **không lọc trùng**: mỗi lượt bấm bắt được **2 nút DOM** = `ant-message` (khung) + `ant-message-notice-wrapper` (con) của **CÙNG 1** thông báo, lệch ~1 ms ⇒ **1 thông báo**, **không** hồi quy `BUG-BC-TOAST-LOI-HIEN-2-LAN` |
| §8 không mở rộng | Không đo nhánh từ chối của CB PD (FR-XI-07a) |

---

## 8. Ghi nhận phụ — **không chấm**, chỉ báo để BA/dev biết

1. **Mã lỗi lệch đặc tả.** `:825` khai `ERR-XI-07-01`; hệ thống trả `ERR-VAL-XI-07-02`. Câu chữ thông báo
   khớp đúng đặc tả (*"Vui lòng hoàn chỉnh báo cáo trước khi trình"*). Phiếu không nhắc mã lỗi ⇒ ghi nhận.
2. **3 khóa lưu được nhưng không hiện trên màn.** Dữ liệu đã lưu có `soVuViec = 7`, `soDnDuocHoTro = 0`,
   `tongChiPhi = 0` nhưng không dòng nào trong bảng 13 chỉ tiêu hiển thị các giá trị này.
3. Trường `nguoiGuiDuyetId` / `ngayGuiDuyet` của đợt vẫn `null` sau lượt trình đi lọt.

---

## 9. Giới hạn hiệu lực

Chỉ có hiệu lực cho `https://18.143.165.120.nip.io` + bó mã **`index-D4Buvu4S.js`** (07/08/2026 02:23 VN).
Đối tác quay trên `htpldn-uat.ospgroup.vn` — môi trường khác.
Vế **C4 không được chấm** (SRS im lặng về thông báo thành công của FR-XI-07 — chuẩn chấm §1 + §7(1));
thông báo duy nhất quan sát được ở luồng giao diện là thông báo **lỗi** *"Vui lòng hoàn chỉnh báo cáo trước
khi trình"*, ghi nhận nguyên văn, không dùng để chấm.
