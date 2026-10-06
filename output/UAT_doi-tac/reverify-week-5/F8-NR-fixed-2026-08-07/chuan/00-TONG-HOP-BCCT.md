# 00 — Tổng hợp chuẩn chấm nhóm **Báo cáo thực hiện Chương trình HTPL** (lô F8, 4 phiếu)

**Ngày khóa chuẩn:** 2026-08-07 · **Giai đoạn A của** [`flows/04-verify-bug-dev-fix-khong-ho-so.md`](../../../../../flows/04-verify-bug-dev-fix-khong-ho-so.md)
**Đặc tả — nguồn DUY NHẤT:** `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-15-ct-htpldn.md`
(1.610 dòng); riêng phiếu 345 dùng thêm **hai cross-ref do chính `:1017` khai** trong cùng thư mục nguồn
chuẩn: `srs-v3.5.md` §D.2.4 (`:6709`–`:6724`) và Phụ lục E §H8 (`:6760`).
**Mọi số dòng trong 4 file chuẩn đều do agent này tự mở file đếm lại trong lượt hôm nay.**

**Đặc điểm cả 4 phiếu:** đối tác **CHƯA TỪNG CHẠY** (`Trạng thái` = `N/R`, `Kết quả thực tế` RỖNG, không ảnh)
⇒ `expected đối tác` = **nguyên văn cột `Kết quả mong đợi` (K)**; không có triệu chứng cũ để đối chiếu.
Cổng bằng chứng flow 04 rơi nhánh *"thiếu bằng chứng nhưng tự tái hiện được"* ⇒ **cấm kết luận "không phải
lỗi" chỉ vì không có bằng chứng**.

---

## 1. Bảng tổng hợp 4 phiếu × số vế × quan hệ × route

| Dòng | Mã TC | Vế | Quan hệ | Route | Verdict logic **sớm nhất có thể** (khi mọi vế MATCH đều đạt) | File chuẩn |
|---|---|---|---|---|---|---|
| **341** | `TPDBCKQTHCT_02` | **2** | 2 MATCH · 0 DIFF · 0 GAP | TEST ×2 | **Pass** (phiếu duy nhất có thể Pass thẳng) | [`TPDBCKQTHCT_02.md`](TPDBCKQTHCT_02.md) |
| **343** | `THBCTHCT_01` | **4** | 3 MATCH · 0 DIFF · **1 GAP** (C2 trạng thái đợt) | TEST ×3 + **BA** ×1 | **Cần BA** | [`THBCTHCT_01.md`](THBCTHCT_01.md) |
| **344** | `THBCTHCT_02` | **3** | 2 MATCH · 0 DIFF · **1 GAP** (C2b đủ 2 biểu) | TEST ×2 + **BA** ×1 | **Cần BA** | [`THBCTHCT_02.md`](THBCTHCT_02.md) |
| **345** | `THBCTHCT_05` | **8** | 6 MATCH · **2 DIFF** (C6 chức danh · C7 tên tệp) · 0 GAP | TEST ×6 + **BA** ×2 | **Cần BA** | [`THBCTHCT_05.md`](THBCTHCT_05.md) |

**Tổng: 17 vế — 13 MATCH · 2 DIFF · 2 GAP.**

### 1.1 Bốn vế không được Pass — tóm tắt lý do

| Phiếu · vế | Loại | Một câu lý do | Dòng đặc tả then chốt |
|---|---|---|---|
| 343 · **C2** — "đợt đã chọn: Đã gửi TW → Đã tổng hợp" | **GAP** | Đặc tả **tự mâu thuẫn**: đầu vào là **danh sách báo cáo theo đơn vị** nhưng lại bắt đổi trạng thái của **ĐỢT**; một đợt chỉ có **một** giá trị trạng thái trong khi phạm vi đợt là ~70–83 đơn vị; trục đơn vị **không có** giá trị `DA_TONG_HOP` | `:1005` · `:993` · `:1368` · `:1389` · `:1367` · `:1398` · `:937`/`:938` · `:1517` |
| 344 · **C2b** — "hiển thị biểu 21a **và** 21b" | **GAP** | SRS **im lặng** về việc form tổng hợp của TW phải hiện cả hai biểu hay chỉ hiện biểu mà báo cáo nguồn dùng; điều kiện hiển thị duy nhất (`:1167`/`:1168`) là của **form lập BC cấp đơn vị** | `:1002` · `:1175` · `:1167` · `:1168` · `:730` · `:1366` |
| 345 · **C6** — "cuối trang có **chức danh người ký**" | **DIFF** | SRS nói **ngược**: *"**không in sẵn dòng chức danh"*, có 2 căn cứ nghiệp vụ (`TAI_KHOAN` không lưu chức vụ; biểu mẫu gốc để trống cho người ký tự ghi) | `:1017` · `srs-v3.5.md:6723` · `:6722` |
| 345 · **C7** — tên tệp `BaoCaoTongHop_CTHTPL_…` | **DIFF** | SRS chốt `BaoCaoTongHopCTHTPL_…` (viết liền, không có dấu gạch dưới giữa "TongHop" và "CTHTPL"); §H8 quy định `{DinhDanh}` phải là **trường đã khai trong entity**, mà `CTHTPL` không phải | `:1017` · `srs-v3.5.md:6760` |

🔴 **Luật khóa 5 (flow 04):** kết quả đo trên web **không** biến `DIFF/GAP` thành `MATCH`. Kể cả khi web làm
đúng y nguyên kỳ vọng đối tác ⇒ **vẫn không Pass** vế đó; nhưng tóm tắt phải ghi rõ *"web hiện tại đúng kỳ
vọng đối tác"* và câu hỏi BA nêu đúng mục đích **bổ sung/đính chính đặc tả**, không phải chặn bàn giao.

### 1.2 Hai vế MATCH có ràng buộc **câu chữ** — hiếm, phải chấm đúng chuỗi

| Phiếu · vế | Chuỗi đặc tả khai nguyên văn | Dòng |
|---|---|---|
| 341 · C2 | `"Vui lòng hoàn chỉnh báo cáo trước khi trình"` (mã `ERR-XI-07-01`) | `:825` |
| 343 · C4 | `"Đã tổng hợp báo cáo toàn quốc"` (mã `INF-XI-09-01`) | `:1032` |

*(Đối chiếu: FR-XI-07 **thông báo thành công** và FR-XI-08 **câu chữ toast** đều **im lặng** ⇒ lô F5 phải để
GAP. Đây là lý do phải mở đúng mục Error Handling của từng FR trước khi kết luận "SRS không quy định câu chữ".)*

---

## 2. Chuẩn tài khoản dùng chung

| Vai trò | Tài khoản (bộ `_03` theo brief §3) | Dùng cho phiếu | Ghi chú bắt buộc |
|---|---|---|---|
| CB NV cấp **TW** — ra verdict 343/344/345 | **`cbnv_tw_03`** | 343 · 344 · 345 | `:982` Tác nhân *"Cán bộ Nghiệp vụ TW"* · `:986` · `:1175` điều kiện hiển thị *"user TW"* |
| CB NV đơn vị nộp — ra verdict 341 | **`cbnv_dp_03`** (hoặc `cbnv_bn_03`) | 341 | `:784` *"Cán bộ Nghiệp vụ"* · `:712` khâu lập BC là **CB NV cấp ĐP/BN** |
| CB PD **cùng đơn vị** — chỉ dựng tiền đề | `cbpd_dp_03` / `cbpd_bn_03` | 343 · 344 · 345 | 🔴 **Phải xác minh cùng `donViId`** với CB NV tương ứng (`:852` · `:1552` BR-AUTH-05). Khác đơn vị ⇒ **không duyệt được** ⇒ đổi cặp `_04`/`_05` **cùng vai trò + cùng cấp** |
| CB NV cấp TW — chỉ dựng đợt | `cbnv_tw_03` | mọi phiếu | `:625` chỉ CB NV cấp TW được tạo đợt |
| Đọc nhật ký | QTHT (hoặc `admin` **chỉ đọc log**) | 343 | Khai rõ; không dùng ra verdict |
| **CẤM ra verdict** | `admin` | — | Quyền rộng che đúng loại lỗi phạm vi/vai trò |

Mật khẩu `Test@1234`. Login fail → **Rule 7**: fallback **cùng vai trò + cùng cấp** (`_04`, `_05`), **khai
account thực dùng**; CẤM đổi ĐP ↔ BN ↔ TW để "cho chạy được".

---

## 3. 🔴 CÔNG THỨC DỰNG TIỀN ĐỀ DÙNG CHUNG (3 phiếu THBCTHCT)

**Mục tiêu:** có **≥2 báo cáo của 2 ĐƠN VỊ KHÁC NHAU** ở trạng thái **"Đã gửi Trung ương"**, ưu tiên **cùng
một đợt**, và có **≥1 chỉ tiêu mà hai đơn vị nhập số khác nhau, khác 0**.

### Bước 0 — KIỂM KÊ TRƯỚC (bắt buộc, đừng dựng thừa)

> 🟢 **TIN TỐT — kiểm kê đã có, tiền đề ĐANG SẴN SÀNG.** Lượt trinh sát chỉ-đọc lúc **11:33–11:50 ngày
> 2026-08-07** ([`01-KIEM-KE-TIEN-DE.md`](01-KIEM-KE-TIEN-DE.md) §4.2) đọc được **3 báo cáo ở `DA_GUI_TW`**:
>
> | # | `baoCaoId` | Đợt | Kỳ | Biểu mẫu | Đơn vị | `ngayGuiTw` |
> |---|---|---|---|---|---|---|
> | 1 | `c4801d2d-dedc-4ffe-b5d2-44e9245fbedc` | `DOT-THBC01-UAT` | `SO_BO_6_THANG` | `MAU_21A` | Bộ Kế hoạch và Đầu tư (BN) | 2026-07-20 02:00 |
> | 2 | `df6498aa-4ae4-4d59-ba3e-7c322e1f9a59` | `DOT-THBC01-UAT` | `SO_BO_6_THANG` | `MAU_21A` | Sở Tư pháp An Giang (DP) | 2026-07-22 07:30 |
> | 3 | `4db99158-5bc4-4069-9d52-cfc756aadc2e` | `DOT-SO_BO_NAM-2026-1` | `SO_BO_NAM` | `MAU_21A` | Sở Tư pháp Hà Nội (DP) | 2026-08-06 20:11 |
>
> ⇒ **Cặp sạch nhất để tổng hợp = {#1, #2}** — cùng đợt `DOT-THBC01-UAT`
> (`d7a62f6e-a119-4582-8b08-f935d25c534b`, phạm vi **đúng 2 đơn vị**, cả hai đã nộp), **cùng kỳ, cùng biểu
> mẫu**, và đúng cấu hình `1 BN + 1 ĐP` mà `:1604` (BR-FLOW-08) mô tả. **KHÔNG cần chạy chuỗi [1]→[6] bên
> dưới** — chuỗi đó chỉ dùng khi cần đơn vị thứ ba hoặc khi dữ liệu đã đổi.
>
> ⚠️ **Đây là MANH MỐI, không phải chuẩn chấm** — và dữ liệu môi trường chung **có thể đổi** giữa lúc kiểm
> kê và lúc đo (tác nhân khác cùng chạy). **Bắt buộc đọc lại danh sách ngay trước khi đo.**

**Cách đọc lại (bắt buộc, ngay trước khi đo):** đăng nhập **`cbnv_tw_03`** bằng giao diện → menu
**"Đợt báo cáo"** → mở chi tiết đợt → khối *"Bảng BC từ BN/ĐP"* (`:1174`, `Filter: da_gui_tw = 1`, cột
`Checkbox / Don vi / Cap / Ma dot / Ky / Ngay gui / Trang thai / Hanh dong (Xem)`). Lập bảng:
`mã đợt | đơn vị | cấp | ngày gửi | trạng thái`. Chỉ dựng **phần còn thiếu**.

**Danh tính tài khoản `_03` (đã đọc được, 6/6 đăng nhập được):** `cbnv_bn_03` = **Bộ Kế hoạch và Đầu tư**
(BN) · `cbnv_dp_03` = **Sở Tư pháp An Giang** (ĐP). `cbnv_bn_03`/`cbnv_dp_03` gọi danh sách tổng hợp đều bị
**403 `ERR-PERM-XI-09-02`** (*"Chỉ cấp TW mới có quyền tổng hợp báo cáo"*) ⇒ đúng `:1030`, **cấm log**.

> 🔴 **Vẫn phải xác minh `donViId` của cặp CB NV ↔ CB PD trước khi dùng chuỗi [1]→[6]** (`:852`, `:1552`).

### Bước 1→6 — dựng cho MỖI đơn vị còn thiếu

| Bước | Việc | Tài khoản | **API hay UI?** | Dòng đặc tả |
|---|---|---|---|---|
| **[1]** | Đợt BC tồn tại + đơn vị nằm trong phạm vi nộp. Chưa có → tạo đợt mới (kỳ chưa dùng trong năm; trùng kỳ+năm bị chặn là **đúng spec**) | `cbnv_tw_03` | **API hoặc UI** — tiền đề | `:717` · `:646` · `:657` · `:625` · `:656` · `:688` |
| **[2]** | Mở chi tiết đợt → **[Lập báo cáo]** → đơn vị sang "Đang lập" | `cbnv_<đv>_03` | **API hoặc UI** — tiền đề | `:746` |
| **[3]** | Nhập số liệu + **[Lưu nháp]**. 🔴 **Mỗi đơn vị nhập GIÁ TRỊ KHÁC NHAU, KHÁC 0** ở các chỉ tiêu **có ô nhập** | `cbnv_<đv>_03` | **API hoặc UI** — tiền đề | `:731` · `:743` · `:744` |
| **[4]** | **[Trình duyệt KQ]** → "Chờ duyệt kết quả" | `cbnv_<đv>_03` | **UI** (nếu chạy được) — **xem §3.1 khi hỏng** | `:802` · `:803` · `:1170` |
| **[5]** | **[Phê duyệt]** → "Đã duyệt kết quả" | `cbpd_<đv>_03` **CÙNG ĐƠN VỊ** | **UI hoặc API** — tiền đề | `:869` · `:1171` · `:852` · `:1552` |
| **[6]** | **[Gửi lên TW]** → Xác nhận → đơn vị "Đã nộp", lọt vào bảng BC của TW | `cbnv_<đv>_03` | **UI hoặc API** — tiền đề | `:937` · `:938` · `:939` · `:1173` · `:1174` |

**Giá trị đề nghị cho bước [3]** *(để phép cộng của phiếu 344 phân biệt được)*:

| Đơn vị | Chỉ tiêu có ô nhập #1 | Chỉ tiêu có ô nhập #2 |
|---|---|---|
| #1 — ĐP *(tái dùng Sở TP Hà Nội của lô F5 nếu còn)* | `1207` | `1308` |
| #2 — BN | `2100` | `3400` |
| **Tổng kỳ vọng** | **`3307`** | **`4708`** |

**Ghi bắt buộc cho mỗi đơn vị:** `username thực dùng` · `capDonVi` · `donViId` · `mã đợt` · `biểu mẫu` ·
`giá trị từng chỉ tiêu` · `mốc giờ gửi TW`.

### 3.1 🔴 Phương án dự phòng khi bước [4] vẫn hỏng

**Điểm đứt đã biết (lô F5, dòng 340 — Reopen):** 11/13 chỉ tiêu biểu 21a hiển thị sẵn `0 (HT)` và **không có
ô nhập**; giao diện **không gửi** 11 khóa đó khi lưu, máy chủ lại đòi chúng ⇒ [Trình duyệt KQ] trả **422**
kèm đúng danh sách 11 chỉ tiêu ấy. Cán bộ không có đường nào hoàn tất bằng giao diện.

```
(a) Đọc đúng TÊN KHÓA của 13 chỉ tiêu — CẤM ĐOÁN. Nguồn hợp lệ:
      · bảng khai 13 chỉ tiêu trong bó mã giao diện đang chạy (mỗi phần tử có `key` + cờ `auto`)
      · hoặc lược đồ ở /api/docs-json  (đọc được, không cần đăng nhập)
(b) Ghi bổ sung các khóa còn thiếu với giá trị 0 vào chính bản báo cáo đang lập  (lô F5: PATCH …/bao-cao → 200)
(c) Gọi đúng chức năng trình duyệt của bản ghi đó, kèm `version` HIỆN TẠI
      (GET trước mỗi bước — sai `version` là lỗi xung đột, KHÔNG phải bug nghiệp vụ)
(d) Mở UI kiểm trạng thái cuối: đơn vị phải đọc được "Chờ duyệt kết quả"
```

**Ràng buộc cứng:**
1. Hợp lệ vì đây là **tiền đề** của 3 phiếu THBCTHCT (hành vi tranh chấp của chúng là [Tổng hợp]/[Lưu]/[Xuất]).
2. 🔴 **TUYỆT ĐỐI KHÔNG dùng cho phiếu 341** — ở đó [Trình phê duyệt] **chính là** hành vi tranh chấp.
3. 🔴 **KHÔNG ép trạng thái ĐỢT** (`DOT_BAO_CAO.trang_thai`) bằng bất kỳ đường nào — nó **chính là vế C2 GAP**
   của phiếu 343, và không có chức năng hợp lệ nào sinh ra nó.
4. **Khai vào báo cáo:** đổi bản ghi nào · đổi khóa nào · giá trị gì · trên env nào · lúc mấy giờ.
5. **CẤM ghi thẳng DB · CẤM đoán endpoint · CẤM đụng dữ liệu đối tác.**
6. Nếu bước [4] **đã tự chạy được** bằng giao diện ⇒ **không dùng dự phòng**, và ghi nhận cho người đo dòng 340.

### 3.2 Ranh giới API / UI — bảng chốt cho cả 4 phiếu

| Hành động | Phiếu | Đường bắt buộc |
|---|---|---|
| Tạo đợt · lập BC · nhập/lưu số liệu · phê duyệt · gửi TW · đọc lại bản ghi đối chứng | mọi phiếu | **API hoặc UI** (tiền đề) |
| **[Trình phê duyệt] / [Trình duyệt KQ]** | **341** | 🔴 **UI THẬT** (hành vi tranh chấp) |
| **[Trình duyệt KQ]** | 343/344/345 | UI ưu tiên; được ép qua bằng đường dữ liệu theo §3.1 (tiền đề) |
| **Tick chọn báo cáo + [Tổng hợp]** | **344** | 🔴 **UI THẬT** |
| **[Lưu] / [Lưu tổng hợp]** | **343** | 🔴 **UI THẬT** |
| **[Xuất Excel] / [Xuất Word]** | **345** | 🔴 **UI THẬT**; nội dung tệp bắt buộc **mở bằng thư viện đọc tệp**, cấm chấm bằng ảnh |

---

## 4. Thứ tự chạy đề xuất

| # | Phiếu | Vì sao đặt ở đây | Có làm hỏng tiền đề của phiếu sau không? |
|---|---|---|---|
| **1** | **341 `TPDBCKQTHCT_02`** | Tiền đề rẻ nhất, độc lập, không cần cấp TW, và **thao tác bị chặn nên không tiêu hủy tiền đề** ⇒ đo lại được nhiều lượt. Chạy trước để có kết quả chắc chắn sớm | Không — dùng 2 báo cáo `DU_THAO` của Sở TP An Giang (`c1b1045d…`, `f445b699…`), **khác hẳn** cặp `DA_GUI_TW` của nhóm THBCTHCT |
| **2** | *(kiểm kê lại tiền đề chung §3 Bước 0)* | Xác minh cặp `c4801d2d…` + `df6498aa…` còn ở "Đã nộp". Chỉ chạy chuỗi §3 khi cặp này đã mất | — |
| **3** | **344 `THBCTHCT_02`** | Bấm [Tổng hợp] = **gợi ý số liệu, CHỈ ĐỌC** ⇒ chưa đổi trạng thái gì. **Phải đọc số liệu 2 báo cáo nguồn TRƯỚC bước này** | Không |
| **4** | **343 `THBCTHCT_01`** | Bấm [Lưu] — **ghi dữ liệu + đưa các báo cáo đã chọn rời `DA_GUI_TW`** | 🔴 **Có, và không hoàn tác được** — sau bước này cặp nguồn **hết dùng lại được**. Bắt buộc chạy sau 344 |
| **5** | **345 `THBCTHCT_05`** | Điều kiện H345 mục 2 đòi **"Đã hoàn thành tổng hợp"** ⇒ **bắt buộc sau 343, và ngay sau, trong cùng phiên** | — |

> ⚠️ **Đổi thứ tự 3 ↔ 4 là hỏng phép đo:** nếu bấm [Lưu] trước rồi mới đo 344, form tổng hợp còn sót trên
> màn **không** được dùng để Pass (flow 04: *"CẤM Pass bằng quan sát tĩnh"*) — vẫn phải bấm lại [Tổng hợp].
> Mà bấm lại thì **cặp nguồn đã bị tiêu thụ** ⇒ 344 mất tiền đề luôn.
>
> 🔴 **CHỈ CÓ MỘT LƯỢT ĐO SẠCH cho 3→4→5.** Muốn có lượt hai, **không phải** dựng lại từ đầu: Bộ KH&ĐT còn
> **2 báo cáo đang `CHO_PHE_DUYET`** — `c19b1bc2…` (`DOT-SO_BO_NAM-2026-1`) và `a63bf70c…`
> (`DOT-SO_BO_6_THANG-2026-1`); chỉ cần `cbpd_bn_03` phê duyệt rồi `cbnv_bn_03` gửi TW là có thêm 2 nguồn.
> Xa hơn nữa mới phải chạy chuỗi §3 đầy đủ.

---

## 5. Rủi ro chặn — cảnh báo trước cho điều phối

| Mức | Phiếu | Rủi ro | Hệ quả nếu xảy ra |
|---|---|---|---|
| 🔴 **Cao** | **343 · 344 · 345** | **Máy chủ chặn [Tổng hợp]/[Lưu] vì đợt chưa ở `DA_GUI_TW`.** `:1517` đặt tiền trạng thái đó ở **trục ĐỢT**, nhưng lô F5 đo được trục đợt **đứng yên `TAO_DOT`** sau khi gửi TW (`daGuiTw = false`, `ngayGuiTw = null`), tab lọc "Đã gửi TW" của TW **rỗng** | Cả 3 phiếu rơi **Cần BA + Chưa chốt**. Ghi nguyên văn mã lỗi + thông điệp làm bằng chứng cho GAP 343 §2. **CẤM ép trạng thái đợt để "cho chạy được"** |
| 🔴 **Cao** | **345** | **Không thu được tệp để mở nội dung** (trình duyệt cách ly có thể không đổ tệp ra đĩa) | Thử đủ 3 cách (`THBCTHCT_05.md` §3); vẫn không được ⇒ **Chưa chốt**, cần bật đường tải tệp hoặc dev cấp tệp do hệ thống xuất |
| 🟡 **Trung bình** | **343 · 344** | **Không dựng nổi đơn vị thứ hai** (cặp `cbnv_bn_03`/`cbpd_bn_03` khác `donViId`, hoặc bước [4] hỏng mà không đọc được tên khóa chỉ tiêu) | 344 **Chưa chốt vế C1** (không kiểm được phép cộng); 343 vẫn đo được nhưng phải khai giới hạn "chỉ 1 đơn vị" |
| 🟡 **Trung bình** | **344** | **Mọi chỉ tiêu đều `0`** ⇒ tổng không phân biệt được với "không cộng" | Bắt buộc dựng số khác nhau, khác 0 (§3). Không làm được ⇒ **Chưa chốt vế C1** |
| 🟢 **Thấp** | **341** | Giao diện tự điền `0` nên không tạo được ô trống | Dùng tiền đề dự phòng TĐ-B + khai rõ giới hạn kết luận |
| 🟢 **Thấp** | **343 · 344 · 345** | Không thấy khối [Tổng hợp] trên màn của `cbnv_tw_03` | Xác minh `capDonVi = TW`; đúng TW mà không có khối ⇒ **Reopen** (không có đường nào tổng hợp), kèm khối `CÁCH VERIFY` |

---

## 6. Kỷ luật đo dùng chung (rút từ flow 04 + brief lô F8)

1. **Khóa chuẩn TRƯỚC khi mở màn** — đã xong ở 4 file chuẩn. Sau khi mở màn **cấm đổi quan hệ MATCH/DIFF/GAP**
   để khớp kết quả; chỉ đổi được khi dẫn được **dòng SRS mới đọc được**.
2. Mỗi thao tác/ảnh/phép đo phải trả lời được **"đang kiểm Cn nào?"**. Không ánh xạ được ⇒ **CẤM chạy**.
3. Mỗi vế: **một đường UI ngắn nhất + một đối chứng độc lập**. Bấm lại cùng nút **không** tính là đường thứ
   hai. Hai đường khớp thì **DỪNG**. **Hai phép mâu thuẫn = chưa được chốt.**
4. **Bắt thông báo:** cài bộ bắt **TRƯỚC** thao tác, **CẤM lọc trùng**, đếm kèm **số yêu cầu gửi đi**, đọc
   chữ bằng `innerText`. Đếm theo **mốc giờ khác nhau**, không theo độ dài mảng.
   *(Lô F5: 1 thông báo sinh 2 nút DOM `ant-message` + `ant-message-notice-wrapper` lệch ~1–2 ms ⇒ vẫn là 1.)*
5. **Vân tay bản dựng:** ghi bó mã `assets/index-*.js` + `last-modified` của trang gốc ở **đầu VÀ cuối** phiên;
   nhãn `V1.0.x` ở chân thanh bên **không** phải định danh. Hai đầu lệch ⇒ nói rõ quan sát nào rơi trước/sau
   mốc triển khai.
6. **Giới hạn hiệu lực:** đo trên env **nội bộ** `https://18.143.165.120.nip.io`; đối tác nghiệm thu trên
   `htpldn-uat.ospgroup.vn` ⇒ mọi kết luận phải kèm câu giới hạn.
7. **Seed = mutate môi trường chung** ⇒ khai: **đổi bản ghi nào · đổi gì · trên env nào**. Cấm ghi thẳng DB,
   cấm đoán endpoint (đọc `/api/docs-json` trước), cấm đụng dữ liệu đối tác.
8. **Bug mới tự lộ:** chỉ ghi nhận sai lệch **trong chính màn/phản hồi/tệp đang quan sát**; **tối đa 1 phép
   xác nhận** cho mỗi phiếu; không đủ căn cứ ⇒ ghi **candidate**, dừng điều tra.

---

## 7. Câu hỏi BA phát sinh từ lô này (4 câu — gom gửi 1 lần)

| # | Phiếu · vế | Nội dung | Trạng thái |
|---|---|---|---|
| **Q1** | 343 · C2 | Sau khi TW lưu tổng hợp, **cái gì** chuyển sang "Đã tổng hợp": cả đợt / từng bản ghi nộp của đơn vị đã chọn / bản ghi báo cáo tổng hợp TW? Trạng thái cán bộ nhìn thấy ở chi tiết đợt là của **đơn vị mình** hay của **đợt**? | **Cùng gốc** với bàn giao lô F5 §3 Nhóm 2 ⇒ **liên kết, không mở câu trùng**; phần mới là bước `DA_GUI_TW → DA_TONG_HOP` và mâu thuẫn "chọn báo cáo nhưng đổi trạng thái đợt" |
| **Q2** | 344 · C2b | Form tổng hợp của TW phải hiện **cả hai** biểu 21a và 21b trong mọi trường hợp, hay chỉ hiện biểu mà các báo cáo được chọn thực sự dùng? | Mới |
| **Q3** | 345 · C6 | Tệp xuất nhóm XI có **in sẵn** dòng chức danh người ký không, hay giữ ngoại lệ §D.2.4 (chỉ chừa chỗ trống)? Phiếu UAT viết trước hay sau chốt 2026-08-06? | Mới |
| **Q4** | 345 · C7 | Tên tệp đúng là `BaoCaoTongHopCTHTPL_…` (viết liền, theo §H8) hay `BaoCaoTongHop_CTHTPL_…` (như phiếu UAT)? | Mới |

**Ghi nhận gửi dev/BA (không mở dòng bug mới, không kéo verdict):** mã lỗi khi chặn trình duyệt là
`ERR-VAL-XI-07-02` trong khi `:825` khai `ERR-XI-07-01` (đã có ở bàn giao F5 §4 mục 2) · `:1016`/`:1021` khai
`loai = TONG_HOP_TW` nhưng entity `BAO_CAO_CT_HTPL` (`:1400`–`:1418`) **không có** trường `loai`, còn
`don_vi_nop_id` (`:1410`) lại bắt buộc và chỉ dành cho ĐP/BN · cờ `da_gui_tw` dùng ở `:937`/`:993`/`:1174`
nhưng **không entity nào khai** · `:1005` viết *"các đợt BC đã chọn"* trong khi đầu vào `:993` là `bao_cao_ids`.
