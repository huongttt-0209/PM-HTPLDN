# Phép đo — GKQTHCTHTPL_01 (dòng 342) · 2026-08-07 — **Gửi kết quả thực hiện lên Trung ương**

**Verdict: CẦN BA.**
Lỗi đối tác báo (**"Forbidden"**) **đã hết** — thao tác chạy trót lọt và **4/5 vế đo được đều ĐẠT**.
Nhưng vế **C1** (*"Chuyển trạng thái **đợt báo cáo** → Đã gửi Trung ương"*) rơi đúng vào vùng
**đặc tả tự mâu thuẫn** mà chuẩn chấm §7(3) đã cảnh báo trước, và phép đo **đã làm lộ hành vi nhập nhằng**:
cùng một đợt, màn của cán bộ ĐP đọc **"Đã gửi TW"** còn màn của cán bộ TW đọc **"Tạo đợt"**.
Flow 04 (*"Im lặng hoặc tự mâu thuẫn → không Pass/Reopen vế này; kết luận Cần BA"*) ⇒ **không chốt Pass**.

Chuẩn chấm: [`../chuan/GKQTHCTHTPL_01.md`](../chuan/GKQTHCTHTPL_01.md)

---

## 1. Điều kiện đo

| Mục | Giá trị |
|---|---|
| Env / bản dựng | `https://18.143.165.120.nip.io` · **`assets/index-D4Buvu4S.js`** — đã tải lại trang bằng địa chỉ và đọc lại tên bó mã trong tab ở **cả hai** nhịp đo C1 |
| Tài khoản ra verdict | **`cbnv_hn`** — `CB_NV_DP`, `capDonVi = DP`, `donViId = 00000000-0000-4000-8002-000000000001` (Sở Tư pháp Hà Nội), `id = 87bb5785-…` |
| Dựng tiền đề bước [4] | **`cbpd_hn`** — `CB_PD_DP`, **`donViId` trùng đúng** `…8002-000000000001` (đã xác minh `/auth/me`), `id = 82ff67b4-…` ⇒ đúng "CB PD **cùng đơn vị**" (`:852`, `:1552`) |
| Đo C2b + C3 | **`cbnv_tw`** — `CB_NV_TW`, `capDonVi = TW` (đăng nhập riêng qua giao diện, **không** dùng `admin`) |
| Đọc nhật ký (C4) | `admin` — **chỉ đọc log**, khai rõ theo §9.6 |
| Đợt đo | `DOT-SO_BO_NAM-2026-1` — `e9909d96-1391-463b-8072-b1b56c319f8e`, `MAU_21A`, phạm vi **83 đơn vị** |

> **Sai lệch so với chuẩn chấm §3.1 — khai rõ:** chuẩn ghi `cbnv_dp_01`/`cbpd_dp_01`/`cbnv_tw_01`. Lô đo dùng
> `cbnv_hn`/`cbpd_hn`/`cbnv_tw` — **cùng vai trò, cùng cấp**, và `cbnv_hn`/`cbpd_hn` **cùng một đơn vị**
> (đã đối chiếu `donViId`). Đây là cặp đã dùng xuyên suốt 6 phiếu trước nên nối được chuỗi tiền đề. Đúng
> Rule 7 (không đổi ĐP ↔ BN ↔ TW).

**Tiền đề đã dựng (đúng chuỗi §3.3, công thức A — tái sử dụng, không tạo đợt mới):**
bước [1]–[3] xong ở các phiếu trước → bước **[4]** `cbpd_hn` phê duyệt kết quả
(`quyetDinh = DUYET`, ghi chú `QA-F5-20260807-tien-de-case7-duyet-KQ`, nhật ký `APPROVE` lúc `20:08:58`)
→ đợt lên **"Đã duyệt kết quả"**, đọc được **trên màn** trước khi bấm.

---

## 2. 🔴 Bảng kết quả theo chuẩn chấm §4.9

| Mã đợt | Đơn vị | Trạng thái **trước** | Ngay sau bấm | Sau tải lại | Mốc giờ gửi ghi nhận | TW thấy trong DS tổng hợp? | TW nhận TB? | Mục nhật ký? | Nguyên văn thông báo |
|---|---|---|---|---|---|---|---|---|---|
| `DOT-SO_BO_NAM-2026-1` | Sở TP Hà Nội (DP) | **Đã duyệt kết quả** | ✅ **Đã gửi TW** | ✅ **Đã gửi TW** | ✅ `2026-08-06T20:11:24.363Z` | ✅ có | ✅ có | ✅ có | ✅ *"Đã gửi báo cáo lên Trung ương"* |

**Mốc giờ thao tác:** bấm [Gửi lên TW] `20:11:17.462Z` → xác nhận [Đồng ý] `20:11:24.251Z`.

---

## 3. Từng vế

### 3.1 C1 — trạng thái đợt → "Đã gửi Trung ương" · ⚠️ **KHÔNG CHỐT ĐƯỢC**

**Phần ĐẠT (theo đúng đường đo đã khóa — "cho chính đơn vị vừa gửi", 2 nhịp bắt buộc):**

| Nhịp | Cách đọc | Kết quả |
|---|---|---|
| 1 | ngay sau thao tác | `Trạng thái: **Đã gửi TW**`, thanh tiến trình nhảy sang bước **5 "Đã gửi TW"** |
| 2 | **tải lại trang bằng địa chỉ** | `Trạng thái: **Đã gửi TW**`, bước 5 — **giữ nguyên** |

Nút [Gửi lên TW] biến mất sau thao tác — **không** dùng làm bằng chứng (chuẩn chấm §6.2 bẫy 2).
Ảnh: [`trước`](../image/GKQTHCTHTPL_01-truoc-khi-bam-da-duyet-ket-qua.png) ·
[`sau khi tải lại`](../image/GKQTHCTHTPL_01-sau-tai-lai-van-da-gui-tw.png)

**🔴 Phần làm lộ mâu thuẫn — vì sao không chốt Pass được:**

Cùng bản ghi đợt `e9909d96…`, đọc bằng **hai vai trò khác nhau**, ra **hai câu trả lời khác nhau**:

| Đọc bằng | Danh sách đợt | Chi tiết đợt |
|---|---|---|
| `cbnv_hn` (ĐP — người vừa gửi) | — | **"Đã gửi TW"** |
| `cbnv_tw` (**TW — bên nhận**) | **"Tạo đợt"** | **"Tạo đợt"** |

Máy chủ: `DOT_BAO_CAO.trangThai = **TAO_DOT**` · `daGuiTw = **false**` · `ngayGuiTw = **null**` (trên bản ghi đợt),
trong khi `DOT_BAO_CAO_DON_VI_NOP.trangThaiNop = **DA_NOP**` và mốc gửi được ghi ở **bản ghi theo đơn vị**.
Tab lọc **"Đã gửi TW"** ở danh sách đợt của TW **rỗng** — đợt vừa gửi không lọt vào.

`:937` khai nguyên văn: `| 3 | Chuyển trạng thái đợt BC sang DA_GUI_TW, đánh dấu da_gui_tw, ghi thời điểm gửi | SM-DOT-BC |`
— **cả ba việc đều không xảy ra ở cấp ĐỢT**; chúng xảy ra ở **cấp ĐƠN VỊ** đúng như `:938`.
Hai dòng này không thể cùng đúng khi `:1368` chỉ cho đợt **một** giá trị trạng thái mà phạm vi đợt là
**83 đơn vị** (`:621`/`:646`/`:1398`).

⇒ Đúng điều kiện kích hoạt của chuẩn chấm §7(3) — *"chỉ gửi BA nếu phép đo lộ ra hành vi nhập nhằng"* —
và đúng dòng "Đối chiếu đặc tả" của Flow 04: **im lặng hoặc tự mâu thuẫn ⇒ không Pass/Reopen vế này**.

> **Vì sao KHÔNG chấm Reopen:** chuẩn chấm §6.1 bẫy 4 + §7(3) cấm FAIL vì trục trạng thái; và ở đường đo
> đã khóa cho C1 (màn của chính đơn vị vừa gửi, 2 nhịp) thì kết quả **ĐẠT**. Cái thiếu là **câu trả lời của
> BA**, không phải bằng chứng.

### 3.2 C2a — ghi nhận thời điểm gửi · ✅ **ĐẠT**

- Dữ liệu nguồn: `ngayGuiTw = **2026-08-06T20:11:24.363Z**` — lệch **~0,1 giây** so với mốc bấm xác nhận
  `20:11:24.251Z`.
- Trên màn (chi tiết đợt, vai trò TW) — thẻ **"Tiến độ nộp theo đơn vị"** (đúng `:938`: *"Tiến độ nộp hiển
  thị trực tiếp ở chi tiết Đợt BC"*), cột `Đơn vị | Cấp | Trạng thái nộp | Ngày nộp | Số lần nhắc`:

  | Đơn vị | Cấp | Trạng thái nộp | Ngày nộp | Số lần nhắc |
  |---|---|---|---|---|
  | **Sở Tư pháp Hà Nội** | DP | **Đã nộp** | **07/08/2026** | 0 |

  (83 dòng, chỉ đúng 1 dòng "Đã nộp" — chính đơn vị vừa gửi.)
  Ảnh: [`../image/GKQTHCTHTPL_01-tw-tien-do-nop-da-nop-ngay-07-08.png`](../image/GKQTHCTHTPL_01-tw-tien-do-nop-da-nop-ngay-07-08.png)

### 3.3 C2b — báo cáo vào danh sách tổng hợp của TW · ✅ **ĐẠT**

Đọc bằng **chính phiên `cbnv_tw`** (không dùng `admin`), danh sách tổng hợp trả về 3 dòng, trong đó:

```
maDot   = DOT-SO_BO_NAM-2026-1
donVi   = Sở Tư pháp Hà Nội  (00000000-0000-4000-8002-000000000001)
capDonVi= DP
ngayGuiTw = 2026-08-06T20:11:24.363Z
trangThai = DA_GUI_TW
```

Khớp **đủ ba** yếu tố chống nhìn nhầm dòng cũ (chuẩn chấm §6.2 bẫy 4): **mã đợt + tên đơn vị + ngày gửi**.
Tập cột trả về trùng đúng khai báo `:1174` (`Đơn vị / Cấp / Mã đợt / Kỳ / Ngày gửi / Trạng thái`).

> **Chủ động KHÔNG bấm nút [Tổng hợp]** trên màn TW: chuẩn chấm §8 ghi *"KHÔNG mở rộng: bước TW tổng hợp
> (FR-XI-09) là chức năng KHÁC"*, và nút đó gắn với hành động ghi (`POST …/tong-hop`) — bấm sẽ đổi trạng thái
> ngoài phạm vi phiếu.

### 3.4 C3 — thông báo cho CB NV cấp Trung ương · ✅ **ĐẠT**

Đăng nhập `cbnv_tw` (đã xác minh `vaiTro = CB_NV_TW`, `capDonVi = TW`) → hộp thông báo có mục mới:

```
2026-08-06T20:11:24.412Z | PHE_DUYET
Tiêu đề : "Đơn vị đã nộp BC đợt DOT-SO_BO_NAM-2026-1 lên TW"
Nội dung: "Mã: DOT-SO_BO_NAM-2026-1. Vui lòng xem xét và tổng hợp."
```

Trùng mốc giờ (`20:11:24`) và **trỏ đúng mã đợt vừa gửi** — không phải thông báo tồn từ trước.
*(Ghi nhận: thông báo nêu mã đợt nhưng **không nêu tên đơn vị** đã nộp. `:940` chỉ khai "Gửi thông báo
CB NV TW", không đặc tả nội dung ⇒ **không chấm**, chỉ nêu để BA cân nhắc — TW nhận báo cáo từ 83 đơn vị.)*

### 3.5 C4 — lưu vết thao tác · ✅ **ĐẠT**

Nhật ký hệ thống quanh mốc giờ:

```
2026-08-06T20:11:24.393Z | DOT_BAO_CAO | SUBMIT  | e9909d96… | nguoiThucHien = 87bb5785 (cbnv_hn)
2026-08-06T20:11:24.356Z | DOT_BAO_CAO | SUBMIT  | e9909d96… | nguoiThucHien = 87bb5785 (cbnv_hn)
2026-08-06T20:08:58.789Z | DOT_BAO_CAO | APPROVE | e9909d96… | nguoiThucHien = 82ff67b4 (cbpd_hn)
```

Đúng tài khoản, đúng bản ghi, đúng mốc giờ. *(Ghi nhận: 1 thao tác gửi sinh **2** mục nhật ký cùng mốc giờ —
`:941` chỉ đòi "ghi nhật ký thao tác", không đặc tả số mục ⇒ **không chấm**.)*

### 3.6 C5 — thông báo thành công · ✅ phần chấm được ĐẠT, phần câu chữ **trùng khít**

- Phần **MATCH** (`:1173` khai *"Toast success"*): **có** thông báo thành công ⇒ ĐẠT.
- Phần **GAP** (câu chữ — cấm chấm): thực tế hiện **đúng nguyên văn** chuỗi đối tác kỳ vọng:
  **"Đã gửi báo cáo lên Trung ương"**. Ghi nhận, không dùng để chấm.
- Hộp xác nhận trước đó: *"Gửi báo cáo lên TW? Sau khi gửi, báo cáo của đơn vị sẽ chuyển sang trạng thái
  Đã nộp."* — bản thân câu này nói rõ hệ thống đang thao tác trên **trục đơn vị**.

---

## 4. 🔴 Truy được nguồn của chữ "Forbidden" mà phiếu báo

Với tài khoản **cấp TW** (`cbnv_tw`), gọi đúng chức năng gửi TW:

```
POST /api/v1/dot-bao-caos/{id}/gui-tw   →  403
{"success":false,"error":{"code":"ERR-PERM-SYS-00-01","message":"Forbidden", …}}
```

⇒ Chặn tài khoản cấp TW là **ĐÚNG SPEC** — nhánh **(a)** bảng §2 chuẩn chấm
(`:918` Tác nhân *"Cán bộ Nghiệp vụ BN/ĐP"* · `:922` *"User thuộc cấp BN hoặc ĐP"* · `:963` `ERR-XI-08-02`).
**Cấm log thành lỗi.** Nhiều khả năng đây chính là điều đối tác gặp ở vòng trước.

**Nhưng thông điệp là chuỗi tiếng Anh thô** `"Forbidden"` + mã quyền chung `ERR-PERM-SYS-00-01`, **không phải**
hai thông điệp tiếng Việt mà FR-XI-08 đã khai:
`:962` `ERR-XI-08-01` *"Đợt BC chưa được phê duyệt kết quả"* · `:963` `ERR-XI-08-02` *"Chỉ đơn vị BN/ĐP mới gửi BC lên TW"*.
⇒ Ghi thành **mục riêng** đúng chuẩn chấm §7(2) — **không kéo verdict 5 vế**.

---

## 5. Bẫy đã kiểm và loại trừ

| Bẫy (chuẩn chấm) | Đã làm gì |
|---|---|
| §6.1-1 kết luận "Forbidden = bug" khi chưa phân nhánh | Chốt đủ **3** bằng chứng: cấp ĐP ✔ · đơn vị trong phạm vi (83 đơn vị, đã lập–trình–duyệt BC) ✔ · đợt "Đã duyệt kết quả" ✔ ⇒ **không** rơi nhánh (d); và đã truy ra nhánh (a) ở §4 |
| §6.1-2 đo bằng tài khoản cấp TW | Bấm bằng `cbnv_hn` (ĐP). Lượt TW ở §4 là **chẩn đoán**, không phải phép đo verdict |
| §6.1-3 bỏ bước [4] phê duyệt | Đã duyệt bằng `cbpd_hn` **CÙNG ĐƠN VỊ** (nhật ký `APPROVE` bởi `82ff67b4`), **không** dùng CB PD cấp TW |
| §6.1-4 nhầm trục trạng thái | Ghi **tách bạch** cả hai trục (§3.1); không lấy trục đơn vị chấm thay trục đợt, cũng không FAIL vì trục đợt |
| §6.1-5 FAIL vì câu chữ C5 | Không chấm câu chữ (thực tế lại trùng khít) |
| §6.1-6 nhãn "Đã nộp" | C2a chấm theo **mốc thời gian**, không theo nhãn |
| §6.2-1 tin vào thông báo thành công | Đọc lại trạng thái **2 nhịp** + đối chứng độc lập bằng vai trò TW |
| §6.2-2 nút biến mất ⇒ kết luận đạt | Không dùng |
| §6.2-3 đọc danh sách TW bằng `admin` | Đọc bằng **chính phiên `cbnv_tw`**; `admin` chỉ đọc nhật ký + tra định danh tài khoản, đã khai rõ |
| §6.2-4 nhìn nhầm dòng cũ | Khớp đủ **mã đợt + tên đơn vị + ngày gửi** |
| §6.2-5 đếm thông báo không kiểm nội dung | Đã đọc nguyên văn tiêu đề + nội dung + mốc giờ |
| §6.2-6 bản ghi cũ đóng băng | Lượt gửi là **lượt mới** trên bản dựng hiện hành |
| §6.3 thông báo hiện 2 lần | Bộ bắt **không lọc trùng**, đếm kèm số yêu cầu: **1** yêu cầu `POST /gui-tw` → **1** thông báo thành công (2 nút DOM = `ant-message` khung + `ant-message-notice-wrapper` con, lệch 2 ms) + 3 nút DOM của hộp xác nhận ⇒ **không hồi quy** `BUG-BC-TOAST-LOI-HIEN-2-LAN` |
| §8 không mở rộng | **Không bấm [Tổng hợp]** (FR-XI-09) · không đo nhánh CB PD từ chối · chỉ chạy dạng ① (ĐP) |

---

## 6. Dữ liệu QA đã dựng / đã đổi

| Bản ghi | Đã làm gì | Trạng thái để lại |
|---|---|---|
| Đợt `DOT-SO_BO_NAM-2026-1` (`e9909d96…`) | `cbpd_hn` duyệt KQ (tiền đề) → `cbnv_hn` **gửi TW qua giao diện** | đơn vị Sở TP Hà Nội = **Đã nộp**, có mặt trong danh sách tổng hợp TW — dữ liệu QA, xóa/đưa về được |
| Đợt `DOT-TRON_NAM-2026-1` (`a63a3214…`) | chỉ gọi thử `gui-tw` bằng tài khoản TW → 403 | **không đổi** |

---

## 7. Giới hạn hiệu lực

Chỉ có hiệu lực cho `https://18.143.165.120.nip.io` + bó mã **`index-D4Buvu4S.js`**.
Đối tác quay trên `htpldn-uat.ospgroup.vn` — môi trường khác.
Vế **C5 (câu chữ)** không được chấm; **C1** để **CẦN BA** theo §3.1.
Chỉ chạy **dạng ①** (đơn vị cấp ĐP) — dạng ② (BN) là "khuyến nghị", không bắt buộc, và ① đúng cấu hình đối tác mô tả.
