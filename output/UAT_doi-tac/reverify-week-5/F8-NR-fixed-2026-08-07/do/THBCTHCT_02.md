# Báo cáo đo — THBCTHCT_02 (dòng 344) — "Kiểm tra khi bấm nút «Tổng hợp»"

> **Chuẩn chấm đã khóa:** [`chuan/THBCTHCT_02.md`](../chuan/THBCTHCT_02.md) — 3 vế: **C1 MATCH** ·
> **C2a MATCH** · **C2b GAP**.
> **Đặc tả nguồn:** `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-15-ct-htpldn.md`.
> **Verdict:** ⚠️ **Cần BA** (`BA confirm`) — hai vế MATCH đều ĐẠT, còn vế C2b là GAP nên theo flow 04
> §Ca biên không được chấm Pass.

---

## 0. Đọc lại dòng phiếu trên bảng trước khi đo

- 13:07:35 ngày 07/08/2026 — đọc lại dòng 344 tab `bug` (spreadsheet `1OKBN2otlmdZ44THkmhtsn-_63M2Boh7zQwearwjYR3s`).
- `Mã TC` = `THBCTHCT_02` · `Dopai` = `N/R` · `Trạng thái dev fix` = `Fixed` · `Kết quả verify` = **RỖNG**.
- `Trạng thái` (N) = `N/R`, `Kết quả thực tế` (L) rỗng, không ảnh ⇒ **đối tác chưa từng chạy phiếu này**
  ⇒ chuẩn chấm lấy nguyên văn cột `Kết quả mong đợi` (K) đối chiếu đặc tả (QĐ-03).

## 1. Môi trường · dấu vân tay bản dựng · tài khoản

| Mục | Giá trị |
|---|---|
| Env | `https://18.143.165.120.nip.io` (nội bộ) |
| Bó mã giao diện — **đầu phiên** (12:40) | `assets/index-eWHwDgt2.js`, `GET /` last-modified `Fri, 07 Aug 2026 02:11:03 GMT` |
| Bó mã giao diện — **đo lại lúc 13:15:28** | `assets/index-eWHwDgt2.js`, last-modified `Fri, 07 Aug 2026 02:11:03 GMT` — **TRÙNG** |
| Nhãn phiên bản trên giao diện | `HTPLDN · V1.0.10` |
| Mốc giờ đo | 13:18 → 13:29 ngày 07/08/2026 |

**Tài khoản ra verdict:** `cbnv_tw_05` · `Test@1234`
`GET /api/v1/auth/me` (13:18:14) → `{"vaiTro":["CB_NV_TW"],"capDonVi":"TW","donViId":"00000000-0000-4000-8000-000000000001","hoTen":"CB Nghiệp vụ - Trung ương #05"}`

> 🔴 **Khai rõ việc đổi tài khoản so với chuẩn (`cbnv_tw_03`).** Trong lúc đo, phiên `cbnv_tw_03` bị
> **thu hồi token hai lần liên tiếp** (`ERR-AUTH-SYS-00-03 "Token đã bị thu hồi"` lúc 06:09:54Z và
> ~06:14:40Z UTC). Nguyên nhân đọc được từ MailHog: có **các lượt yêu cầu mã xác thực cho chính
> `cbnv_tw_03` không phải của tôi** (06:12:41, 06:13:04 và 06:14:32 UTC — tôi chỉ đăng nhập 1 lần lúc
> 06:13:31). Tức **một tiến trình khác đang dùng chung tài khoản này**; hệ thống chỉ cho một phiên sống
> nên phiên của tôi bị đá ra giữa phép đo.
> Theo Rule 7 (fallback **cùng vai trò + cùng đơn vị**) tôi chuyển sang `cbnv_tw_05`: **cùng vai trò
> `CB_NV_TW`, cùng cấp TW, cùng `donViId 00000000-0000-4000-8000-000000000001`** (Cục Bổ trợ tư pháp)
> ⇒ phạm vi dữ liệu không đổi, verdict không bị ảnh hưởng. Không dùng `admin`.

**Tài khoản chỉ để đọc đối chứng (không ra verdict):** `cbnv_dp_05` — `CB_NV_DP`, cấp DP,
`donViId 00000000-0000-4000-8002-000000000006` = **Sở Tư pháp An Giang** (đăng nhập bằng API, phiên riêng,
không đụng phiên trình duyệt).

## 2. Tiền đề — xác minh sống trước khi đo

`GET /api/v1/dot-bao-caos/tong-hop?page=1&pageSize=200` bằng chính phiên `cbnv_tw_05`, lúc **13:14:03**:

| # | `baoCaoId` | Đơn vị | Cấp | Đợt | Kỳ · Biểu mẫu | `ngayGuiTw` | Trạng thái |
|---|---|---|---|---|---|---|---|
| 1 | `c4801d2d-dedc-4ffe-b5d2-44e9245fbedc` | Bộ Kế hoạch và Đầu tư | BN | `DOT-THBC01-UAT` | `SO_BO_6_THANG` · `MAU_21A` | 20/07/2026 | `DA_GUI_TW` |
| 2 | `df6498aa-4ae4-4d59-ba3e-7c322e1f9a59` | Sở Tư pháp An Giang | DP | `DOT-THBC01-UAT` | `SO_BO_6_THANG` · `MAU_21A` | 22/07/2026 | `DA_GUI_TW` |
| 3 | `4db99158-5bc4-4069-9d52-cfc756aadc2e` | Sở Tư pháp Hà Nội | DP | `DOT-SO_BO_NAM-2026-1` | `SO_BO_NAM` | 07/08/2026 | `DA_GUI_TW` |

⇒ Cặp #1 + #2 (2 đơn vị khác nhau, cùng đợt / cùng kỳ / cùng biểu mẫu) **còn nguyên** ⇒ **không phải dựng
thêm gì**. Bản #3 khác đợt khác kỳ ⇒ không gộp.

Đợt `DOT-THBC01-UAT` = `d7a62f6e-a119-4582-8b08-f935d25c534b`, phạm vi đúng 2 đơn vị, cả hai `DA_NOP`.

### 2.1 Số liệu gốc của HAI báo cáo nguồn (số hạng để tự cộng tay)

| # | Khóa chỉ tiêu | Nhãn trên giao diện | Bộ KH&ĐT `c4801d2d…` | Sở TP An Giang `df6498aa…` |
|---|---|---|---|---|
| 1 | `soTvvKienToan` | 1. Số TVV kiện toàn | 8 | 4 |
| 2 | `soCuocTapHuan` | 2. Cuộc tập huấn | 3 | 1 |
| 3 | `soHoiNghiDoiThoai` | 3. Hội nghị đối thoại | 2 | 1 |
| 4 | `soVBTraLoiUBND` | 4. VB trả lời UBND | 5 | 2 |
| 5 | `soVBTvMangLuoiTVV` | 5. VB TV mạng lưới TVV | 4 | 3 |
| 6 | `soHsTiepNhan` | 6. HS tiếp nhận | 25 | 12 |
| 7 | `soHsGiaiQuyetTong` | 7. HS giải quyết tổng | 20 | 9 |
| 8 | `hsDoanhNghiepVua` | 8. DN vừa | 5 | 2 |
| 9 | `hsDoanhNghiepNho` | 9. DN nhỏ | 10 | 4 |
| 10 | `hsDoanhNghiepSieuNho` | 10. DN siêu nhỏ | 5 | 3 |
| 11 | `kpHoTroTvpl` | 11. KP hỗ trợ TVPL (NSNN) | 500.000.000 | 180.000.000 |
| 12 | `kpHoatDongKhac` | 12. KP chi HĐ khác | 120.000.000 | 40.000.000 |
| 13 | `kpXaHoiHoa` | 13. KP xã hội hóa | 30.000.000 | 0 |

**Nguồn đọc — hai đường riêng biệt, không đường nào đi qua hộp gợi ý đang cần kiểm:**
- Bộ KH&ĐT: `GET /api/v1/dot-bao-caos/{dotId}` bằng **phiên trình duyệt `cbnv_tw_05`** lúc 13:14:30
  (trường `baoCao.soLieuTongHop`; đây cũng chính là bảng "Biểu mẫu 21a/TP/HTPLDN" hiển thị trên màn chi
  tiết đợt của tài khoản TW).
- Sở TP An Giang: cùng đường dẫn nhưng bằng **phiên API riêng của `cbnv_dp_05`** (13:20 và đọc lại lúc
  13:26) — máy chủ phân giải `baoCao` theo đơn vị của người gọi nên phiên ĐP trả đúng bản của An Giang.

🔴 **Kiểm khả năng phân biệt (chống Pass oan):** 13/13 chỉ tiêu hai đơn vị nhập **khác nhau**, 12/13 chỉ
tiêu **khác 0** ở cả hai bên, và **không tổng nào trùng bất kỳ số hạng nào** (vd 8 + 4 = 12; 25 + 12 = 37).
⇒ phép cộng **phân biệt được**, đủ điều kiện chấm C1.

## 3. Đo từng vế

### 3.0 Ghi nhận đường đi — nút [Tổng hợp] có HAI chỗ, hai nghĩa khác nhau

Trước khi đo tôi phải xác định đúng nút. Trên bản dựng có **hai** nút cùng tên:

| Nơi | Hành vi | Dùng cho phiếu nào |
|---|---|---|
| Màn **chi tiết đợt** (`/ct-htpldn/dot-bao-cao/{id}`) | Mở hộp xác nhận *"Tổng hợp báo cáo? Đợt sẽ chuyển sang Đã tổng hợp."* → **ghi thẳng**, không có bước gợi ý số liệu | **KHÔNG dùng** — sẽ phá tiền đề |
| Màn **Tổng hợp báo cáo toàn quốc** (`/ct-htpldn/tong-hop`) | Bảng báo cáo có **ô chọn**, nút **[Tổng hợp (N)]** → hiện **hộp gợi ý số liệu, sửa được**, rồi mới có [Lưu tổng hợp] | ✅ **Đúng màn của phiếu 344/343/345** |

Để không phá tiền đề khi dò, tôi cài một bộ chặn ghi (chỉ cho đi các yêu cầu đọc) rồi mới bấm thử nút ở
màn chi tiết đợt; hộp xác nhận hiện ra, tôi bấm **Hủy** ngay và đọc lại đợt để xác nhận **không có gì thay
đổi** (`trangThai = TAO_DOT`, `version = 2`, hai đơn vị vẫn `DA_NOP`).

> ⚠️ **Màn `/ct-htpldn/tong-hop` KHÔNG có mục nào trên thanh điều hướng bên trái** — phải biết địa chỉ mới
> vào được. Ghi nhận cho BA/dev (mục 5), không chấm vì phiếu không nhắc.

### 3.1 Vế C1 — "Gợi ý số liệu tổng hợp: tính tổng các chỉ tiêu tương ứng từ các báo cáo đã chọn" → ✅ ĐẠT

**Đường đo 1 — giao diện thật.**
1. Vào màn "Tổng hợp báo cáo toàn quốc", bảng liệt kê 3 báo cáo `Đã gửi TW`, mỗi dòng có ô chọn
   (ảnh 01).
2. Tick **đúng 2 dòng** `Bộ Kế hoạch và Đầu tư` + `Sở Tư pháp An Giang` (cùng đợt `DOT-THBC01-UAT`).
   Nút đổi nhãn thành **[Tổng hợp (2)]**.
3. Bấm **[Tổng hợp (2)]** lúc 13:24. Hộp *"Tổng hợp báo cáo toàn quốc"* hiện ra, phần đầu ghi:
   `Đợt báo cáo: THBCTHCT_01 - Đợt báo cáo sơ bộ 6 tháng 2026 (seed UAT)` · `Kỳ báo cáo: Sơ bộ 6 tháng` ·
   `Biểu mẫu: Biểu mẫu 21a/TP/HTPLDN` · **`Số đơn vị: 2`**, kèm dòng giải thích
   *"Số liệu dưới đây do hệ thống gợi ý — Hệ thống đã cộng các chỉ tiêu tương ứng từ báo cáo của những đơn
   vị được chọn. Cán bộ có thể chỉnh sửa, bổ sung trước khi lưu."* (ảnh 02).

**Bảng đối chiếu từng chỉ tiêu** (cột "Tổng tay" = tự cộng từ §2.1; cột "Hộp gợi ý hiện" = đọc giá trị
thực trong ô nhập):

| # | Chỉ tiêu | Bộ KH&ĐT | An Giang | **Tổng tay** | **Hộp gợi ý hiện** | Khớp |
|---|---|---|---|---|---|---|
| 1 | Số TVV kiện toàn | 8 | 4 | **12** | 12 | ✅ |
| 2 | Cuộc tập huấn | 3 | 1 | **4** | 4 | ✅ |
| 3 | Hội nghị đối thoại | 2 | 1 | **3** | 3 | ✅ |
| 4 | VB trả lời UBND | 5 | 2 | **7** | 7 | ✅ |
| 5 | VB TV mạng lưới TVV | 4 | 3 | **7** | 7 | ✅ |
| 6 | HS tiếp nhận | 25 | 12 | **37** | 37 | ✅ |
| 7 | HS giải quyết tổng | 20 | 9 | **29** | 29 | ✅ |
| 8 | DN vừa | 5 | 2 | **7** | 7 | ✅ |
| 9 | DN nhỏ | 10 | 4 | **14** | 14 | ✅ |
| 10 | DN siêu nhỏ | 5 | 3 | **8** | 8 | ✅ |
| 11 | KP hỗ trợ TVPL (NSNN) | 500.000.000 | 180.000.000 | **680.000.000** | 680000000 | ✅ |
| 12 | KP chi HĐ khác | 120.000.000 | 40.000.000 | **160.000.000** | 160000000 | ✅ |
| 13 | KP xã hội hóa | 30.000.000 | 0 | **30.000.000** | 30000000 | ✅ |

**13/13 khớp.**

**Đường đo 2 — đối chứng độc lập.** Số hạng ở §2.1 được đọc từ **chính hai bản ghi nguồn**, bằng **hai
phiên đăng nhập khác nhau** (`cbnv_tw_05` cho bản Bộ KH&ĐT, `cbnv_dp_05` cho bản An Giang), **không đi qua**
chức năng gợi ý. Phép cộng tay khớp trọn vẹn với hộp gợi ý ⇒ **hai đường đo thống nhất**.

**Phép thử phân biệt bổ sung (cùng một đường đo, chống Pass oan #5).** Bỏ tick Bộ KH&ĐT, chỉ còn An Giang,
bấm lại [Tổng hợp (1)]: hộp đổi thành `Số đơn vị: 1` và **toàn bộ 13 giá trị đổi đúng thành số của riêng
An Giang** (4 · 1 · 1 · 2 · 3 · 12 · 9 · 2 · 4 · 3 · 180000000 · 40000000 · 0). ⇒ hệ thống **thực sự cộng
theo bộ chọn**, không hiển thị con số cố định hay số của lượt trước.

**Đặc tả:** `srs-fr-15-ct-htpldn.md:1002` = `| 4 | Hệ thống gợi ý số liệu: tính tổng các cột tương ứng 21a/21b | — |`;
`:1037` = `- **Given** CB NV TW chọn các BC **When** nhấn "Tổng hợp" **Then** gợi ý số liệu + form tổng hợp theo TT17`.

### 3.2 Vế C2a — "Hiển thị biểu mẫu tổng hợp toàn quốc cho phép CB NV cấp TW chỉnh sửa, bổ sung" → ✅ ĐẠT

**Đường đo 1 — gõ thật vào giao diện.** Trong hộp gợi ý, đưa con trỏ vào ô chỉ tiêu **13. KP xã hội hóa**
(giá trị đang là `30000000`), gõ **`13250807`** (mốc giờ 13:25 ngày 07/08). Đọc lại lúc 13:27:15:
- ô 13 nhận giá trị **`13250807`**;
- **12 ô còn lại giữ nguyên** (`12 · 4 · 3 · 7 · 7 · 37 · 29 · 7 · 14 · 8 · 680000000 · 160000000`);
- ô **"Nhận xét, kiến nghị (tùy chọn)"** cũng gõ được: nhập `QA-F8-344 kiem tra o sua duoc 13:25 07/08/2026`
  và đọc lại đúng nguyên văn ⇒ đáp ứng cả vế **"bổ sung"** (ảnh 03).

**Đường đo 2 — đối chứng độc lập bằng thuộc tính DOM của chính ô đó:** `readOnly = false`, `disabled = false`,
ô là trường nhập số (`ant-input-number`, trạng thái `...-focused` khi đang gõ). Hai đường thống nhất.

Sau khi đo xong tôi bấm **[Hủy]** — **không lưu gì ở phiếu này**; kiểm lại đợt vẫn `TAO_DOT`, hai báo cáo
vẫn `DA_GUI_TW`.

**Đặc tả:** `:1003` = `| 5 | CB NV TW chỉnh sửa/bổ sung trên form tổng hợp | — |`;
`:1175` (trích) = `Chon BC (checkbox) -> [Tong hop] -> tu tinh tong hop mau 21a/21b -> form editable -> [Luu] …`,
điều kiện hiển thị *"user TW"*.

### 3.3 Vế C2b — "hiển thị biểu mẫu tổng hợp Biểu 21a, 21b" → 🔎 GAP, KHÔNG CHẤM (ghi nhận hiện trạng)

Hiện trạng đo được:
- Hộp tổng hợp ghi **`Biểu mẫu: Biểu mẫu 21a/TP/HTPLDN`** — **chỉ một biểu 21a**, không có 21b.
- Bảng chỉ tiêu trong hộp có **đúng 13 dòng**, là 13 chỉ tiêu của biểu 21a.
- **Biểu mẫu của hai báo cáo nguồn:** cả hai đều `MAU_21A`. Biểu mẫu khai ở đợt `DOT-THBC01-UAT` cũng là
  `MAU_21A`. Nhãn hộp lấy theo `bieuMauSuDung` trả về cùng số liệu gợi ý (`"bieuMauSuDung":"MAU_21A"`).
- Bản dựng có sẵn ba nhãn `MAU_21A` / `MAU_21B` / `CA_HAI` ⇒ nếu đợt dùng `CA_HAI` thì nhiều khả năng hiện
  cả hai biểu; **tôi không đo trường hợp đó** vì nằm ngoài phạm vi phiếu và sẽ phải dựng thêm dữ liệu.

Theo chuẩn §1.1, SRS **im lặng** về việc form tổng hợp của TW có buộc hiện cả hai biểu hay không
⇒ **cấm Pass, cấm Reopen vế này**; chuyển câu hỏi cho nghiệp vụ (mục 6).

## 4. Kết luận theo từng vế

| Vế | Quan hệ (đã khóa) | Kết quả đo | Ghi chú |
|---|---|---|---|
| **C1** — gợi ý = tổng các chỉ tiêu từ báo cáo đã chọn | MATCH | ✅ **ĐẠT** | 13/13 chỉ tiêu khớp tổng tay; đổi bộ chọn thì tổng đổi theo |
| **C2a** — form tổng hợp cho TW sửa, bổ sung | MATCH | ✅ **ĐẠT** | Gõ thật vào ô số và ô nhận xét, cả hai nhận giá trị |
| **C2b** — hiển thị **cả** 21a và 21b | **GAP** | 🔎 **Không chấm** | Web hiện **chỉ 21a**, đúng biểu mà cả hai báo cáo nguồn đang dùng |

**Verdict phiếu:** ⚠️ **Cần BA** → ô `Trạng thái dev fix` = **`BA confirm`**.
Căn cứ: flow 04 §Ca biên — *"Không vế nào Reopen mà còn DIFF/GAP → Cần BA"*; QĐ-01 của lô.

## 5. Ghi nhận cho dev (không ảnh hưởng verdict phiếu này)

1. **Màn "Tổng hợp báo cáo toàn quốc" không có lối vào trên thanh điều hướng.** Địa chỉ
   `/ct-htpldn/tong-hop` chạy đúng và đủ quyền cho tài khoản TW, nhưng không xuất hiện ở menu bên trái lẫn
   trong màn "Đợt báo cáo"; cán bộ chỉ vào được nếu biết sẵn địa chỉ. Phiếu 344 không nhắc lối vào nên
   **không chấm**; đề nghị dev/BA xem lại vì đây là chức năng chính của nghiệp vụ tổng hợp.
2. **Trùng tên nút.** Nút [Tổng hợp] ở màn *chi tiết đợt* làm việc khác hẳn nút [Tổng hợp] ở màn *tổng hợp
   toàn quốc*: cái trước chuyển trạng thái đợt ngay sau một hộp xác nhận, không có bước xem trước số liệu.
   Dễ gây nhầm cho người dùng. Ghi nhận, không chấm (phiếu không nhắc nhãn nút).

## 6. Câu hỏi cho nghiệp vụ (vế C2b)

> **CẦN BA CONFIRM:** phiếu kỳ vọng *"hiển thị biểu mẫu tổng hợp **Biểu 21a, 21b** toàn quốc"* (đủ cả hai);
> đặc tả **im lặng** — FR-XI-09 (`srs-fr-15-ct-htpldn.md:971`–`:1038`) chỉ viết gộp *"21a/21b"* (`:1002`)
> và khối màn hình `:1175` chỉ ghi *"tu tinh tong hop mau 21a/21b … form editable"*, **không** khai điều
> kiện hiển thị; điều kiện hiển thị duy nhất cho hai biểu (`:1167`, `:1168`) lại thuộc **form lập báo cáo
> của đơn vị** (*"khi bieu mau ap dung va dot o DANG_LAP_BC"*), trong khi mỗi đơn vị được tự chọn mẫu
> (`:730`, `:1366`).
> **Web hiện tại:** form tổng hợp hiện **chỉ biểu 21a**; cả hai báo cáo nguồn và đợt đều dùng `MAU_21A`.
>
> **Câu hỏi:** form tổng hợp của TW phải hiện **cả hai** biểu 21a và 21b trong mọi trường hợp, hay chỉ hiện
> những biểu mà các báo cáo được chọn thực sự sử dụng? Nếu là vế thứ nhất, xin bổ sung điều kiện hiển thị
> cho khối tổng hợp (`:1175`).

## 7. Dữ liệu đã đụng vào

- **Phiếu này KHÔNG ghi gì xuống máy chủ.** Hai lượt bấm [Tổng hợp] chỉ gọi chức năng *gợi ý số liệu*
  (đọc); giá trị `13250807` và câu nhận xét chỉ nằm trên màn, đã bấm **[Hủy]**.
- Kiểm lại sau khi hủy: đợt `DOT-THBC01-UAT` vẫn `TAO_DOT` (`version 2`), hai báo cáo vẫn `DA_GUI_TW`,
  hai đơn vị vẫn `DA_NOP`.
- Một lượt bấm thăm dò nút [Tổng hợp] ở màn *chi tiết đợt* đã bị chặn ở tầng trình duyệt và bấm **Hủy**;
  đọc lại xác nhận không đổi gì.

## 8. Ảnh bằng chứng

| # | Tệp | Chứng minh | Drive |
|---|---|---|---|
| 01 | `image/THBCTHCT_02-01-man-tong-hop-3-bc-da-gui-tw.png` | Tiền đề + bảng có ô chọn | https://drive.google.com/file/d/1B7QphhLnSCYozM2972ru418LmBCOa7HP/view?usp=drivesdk |
| 02 | `image/THBCTHCT_02-02-hop-goi-y-so-lieu-tong-hop.png` | C1 + C2b — hộp gợi ý, `Số đơn vị: 2`, biểu 21a, các tổng 12/4/3/7/7/37 | https://drive.google.com/file/d/1CBqUaRMCna0pmOnbiwV2QadGIZwPIu4z/view?usp=drivesdk |
| 03 | `image/THBCTHCT_02-03-o-sua-duoc-va-bo-sung-nhan-xet.png` | C2a — ô 13 nhận `13250807`, ô nhận xét nhận chữ, các ô khác giữ nguyên | https://drive.google.com/file/d/1AQVK22gpA0Z7XjIfYLED5rBLQ9fQ9eYP/view?usp=drivesdk |

## 9. Năm câu hỏi cổng verdict (flow 04)

1. **Đã bấm bằng giao diện thật chưa?** Rồi — tick ô chọn và bấm [Tổng hợp (2)] / [Tổng hợp (1)] trên màn.
2. **Có đủ hai đường đo độc lập không?** Có — (a) hộp gợi ý trên giao diện; (b) tự cộng tay từ số liệu hai
   bản ghi nguồn đọc bằng hai phiên đăng nhập khác nhau. Hai đường khớp.
3. **Có Pass bằng quan sát tĩnh không?** Không — mọi kết luận đều từ lượt bấm mới trong phiên này.
4. **Có hạ GAP thành MATCH để ghi Test done không?** Không — C2b giữ nguyên GAP, phiếu chốt `BA confirm`.
5. **Có đổi dữ liệu ngoài phạm vi không?** Không — phiếu này không ghi gì.
