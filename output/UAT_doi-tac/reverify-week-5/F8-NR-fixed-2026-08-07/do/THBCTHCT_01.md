# Báo cáo đo — THBCTHCT_01 (dòng 343) — "Tổng hợp báo cáo từ nhiều đơn vị → Lưu tổng hợp"

> **Chuẩn chấm đã khóa:** [`chuan/THBCTHCT_01.md`](../chuan/THBCTHCT_01.md) — 4 vế: **C1 MATCH** ·
> **C2 GAP** · **C3 MATCH** · **C4 MATCH**.
> **Đặc tả nguồn:** `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-15-ct-htpldn.md`.
> **Verdict:** ⚠️ **Cần BA** (`BA confirm`) — cả ba vế MATCH đều ĐẠT, còn vế C2 là GAP (đặc tả tự mâu
> thuẫn) nên theo flow 04 §Ca biên không được chấm Pass.

---

## 0. Đọc lại dòng phiếu trên bảng trước khi đo

- 13:07:35 ngày 07/08/2026 — đọc lại dòng 343 tab `bug`.
- `Mã TC` = `THBCTHCT_01` · `Dopai` = `N/R` · `Trạng thái dev fix` = `Fixed` · `Kết quả verify` = **RỖNG**.
- `Trạng thái` (N) = `N/R`, `Kết quả thực tế` (L) rỗng ⇒ **đối tác chưa từng chạy phiếu này**; ô
  `TKM phản hồi lần 1` ghi *"Chưa thực hiện được do uc GKQTHCTHTPL_01 lỗi"* — tức bên nghiệm thu bị chặn ở
  luồng thượng nguồn ⇒ chuẩn chấm lấy nguyên văn cột `Kết quả mong đợi` (K) đối chiếu đặc tả (QĐ-03).

## 1. Môi trường · dấu vân tay bản dựng · tài khoản

| Mục | Giá trị |
|---|---|
| Env | `https://18.143.165.120.nip.io` (nội bộ) |
| Bó mã giao diện — đầu phiên (12:40) và đo lại (13:15:28) | `assets/index-eWHwDgt2.js`, last-modified `Fri, 07 Aug 2026 02:11:03 GMT` — **TRÙNG hai đầu** |
| Nhãn phiên bản trên giao diện | `HTPLDN · V1.0.10` |
| Mốc giờ đo | 13:30 → 13:45 ngày 07/08/2026 |

**Tài khoản ra verdict:** `cbnv_tw_05` (`CB_NV_TW`, cấp TW, `donViId 00000000-0000-4000-8000-000000000001`).
Lý do dùng số 05 thay số 03 (tranh chấp phiên với một tiến trình khác) đã khai đầy đủ ở
[`do/THBCTHCT_02.md` §1](THBCTHCT_02.md) — cùng vai trò, cùng cấp, cùng đơn vị nên phạm vi dữ liệu không đổi.

**Tài khoản chỉ để ĐỌC (không ra verdict):**
- `cbnv_dp_05` (Sở Tư pháp An Giang) — đọc lại trạng thái đợt bằng phiên độc lập.
- 🔴 `admin` (QTHT) — **CHỈ dùng để đọc Nhật ký hệ thống ở vế C3**, đúng như chuẩn §3.1 cho phép, vì tài
  khoản nghiệp vụ không có quyền: `cbnv_tw_05` gọi `GET /api/v1/audit-logs` trả **403 `ERR-PERM-SYS-00-01`
  "Bạn không có quyền thực hiện thao tác này"** (đúng phân quyền, không phải lỗi). **Không dùng `admin` cho
  bất kỳ thao tác nào khác.**

## 2. Tiền đề — xác minh sống trước khi bấm

Kiểm lúc 13:14:03 bằng chính phiên `cbnv_tw_05` (`GET /api/v1/dot-bao-caos/tong-hop`): cặp báo cáo
**2 đơn vị khác nhau, cùng đợt `DOT-THBC01-UAT`, cùng kỳ `SO_BO_6_THANG`, cùng biểu `MAU_21A`**, cả hai
`DA_GUI_TW`:

| `baoCaoId` | Đơn vị | Cấp | `ngayGuiTw` |
|---|---|---|---|
| `c4801d2d-dedc-4ffe-b5d2-44e9245fbedc` | Bộ Kế hoạch và Đầu tư | BN | 20/07/2026 |
| `df6498aa-4ae4-4d59-ba3e-7c322e1f9a59` | Sở Tư pháp An Giang | DP | 22/07/2026 |

Đợt `DOT-THBC01-UAT` = `d7a62f6e-a119-4582-8b08-f935d25c534b`. **Không phải dựng thêm gì** — chuỗi
[1]→[6] của chuẩn §3.3 và phương án dự phòng §3.4 **không phải chạy**.

### 2.1 Trạng thái BA TRỤC **trước** thao tác (13:14 — 13:29)

| Trục | Trường | Giá trị trước |
|---|---|---|
| **ĐỢT** | `DOT_BAO_CAO.trangThai` | **`TAO_DOT`** (`version = 2`) · `daGuiTw = false` · `ngayGuiTw = null` |
| **ĐƠN VỊ** | `tienDo[].trangThaiNop` | Bộ KH&ĐT = `DA_NOP` · Sở TP An Giang = `DA_NOP` |
| **BÁO CÁO** | `trangThai` trong danh sách tổng hợp của TW | cả hai = **`DA_GUI_TW`** |

> Ghi nhận: đợt **chưa bao giờ** đi qua `DA_GUI_TW` ở trục ĐỢT — nó đứng nguyên `TAO_DOT` trong khi hai
> báo cáo con đã `DA_GUI_TW`. Đây đúng là hiện tượng "trục ĐỢT đứng yên" mà chuẩn §6 R1 cảnh báo. Tuy vậy
> thao tác tổng hợp **không bị chặn** (bản dựng lọc theo trục BÁO CÁO, không theo trạng thái đợt) ⇒ rủi ro
> R1 **không xảy ra**.

## 3. Đo từng vế

### 3.0 Thao tác đã thực hiện (một lượt duy nhất, bằng giao diện thật)

Trên màn **"Tổng hợp báo cáo toàn quốc"** (`/ct-htpldn/tong-hop`):
1. Tick đúng 2 dòng Bộ KH&ĐT + Sở TP An Giang → bấm **[Tổng hợp (2)]** → hộp gợi ý hiện 13 chỉ tiêu đã
   cộng (chi tiết đo ở phiếu 344).
2. Nhập vào ô "Nhận xét, kiến nghị" chuỗi mốc-giờ:
   `QA-F8-343-20260807-1330 tong hop toan quoc tu 2 don vi (Bo KH&DT + So Tu phap An Giang)`
   *(chống nhìn nhầm bản ghi cũ — bẫy Pass oan #3)*.
3. Bấm **[Lưu tổng hợp]** lúc **13:30:50**.

Bộ bắt thông báo được cài **TRƯỚC** khi bấm, **không lọc trùng**, đọc bằng `innerText`.

### 3.1 Vế C1 — "Lưu bản ghi báo cáo tổng hợp toàn quốc" → ✅ ĐẠT

**Đường đo 1 — giao diện thật.** Lượt bấm [Lưu tổng hợp] đi lọt; máy chủ trả **201** và **tạo mới một
bản ghi**:

| Trường | Giá trị |
|---|---|
| `id` | `57d4ce85-03b6-4d62-8f76-bb7546bec5c5` |
| `maBaoCao` | `TH-TW-1786084251126` |
| `tieuDe` | `Báo cáo tổng hợp TW - THBCTHCT_01 - Đợt báo cáo sơ bộ 6 tháng 2026 (seed UAT)` |
| **`loai`** | **`TONG_HOP_TW`** |
| `dotBaoCaoId` | `d7a62f6e-a119-4582-8b08-f935d25c534b` |
| `donViId` / `donViNopId` | `00000000-0000-4000-8000-000000000001` (Cục Bổ trợ tư pháp — cấp TW) |
| `trangThai` | `DA_DUYET` · `version = 1` · `ngayTao = 2026-08-07T06:30:51.115Z` |
| `soLieuTongHop` | 12 · 4 · 3 · 7 · 7 · 37 · 29 · 7 · 14 · 8 · 680000000 · 160000000 · 30000000 |
| `nhanXet` | đúng chuỗi mốc-giờ đã nhập |

⇒ Số liệu lưu xuống **trùng khít** số liệu trên form lúc bấm (tôi không sửa ô số nào ở lượt này).
Bản ghi mang đúng loại `TONG_HOP_TW` mà `:1004` / `:1016` yêu cầu.

**Đường đo 2 — đọc lại từ máy chủ SAU KHI TẢI LẠI TRANG BẰNG ĐỊA CHỈ.** Tải lại
`/ct-htpldn/dot-bao-cao/d7a62f6e-…` (nạp lại toàn bộ trang, phiên vẫn sống), rồi đọc lại bằng chính phiên
`cbnv_tw_05`:
- đợt đọc lại được ở **`DA_TONG_HOP`**, `version = 3` (trước là `TAO_DOT`, `version = 2`);
- màn hiện thanh tiến trình dừng ở **bước 6 "Đã tổng hợp"**, ô Trạng thái = **"Đã tổng hợp"** (ảnh 02);
- danh sách tổng hợp của TW: hai báo cáo nguồn đọc lại được ở **`DA_TONG_HOP`** (ảnh 01);
- đọc lại bằng **một phiên đăng nhập khác hẳn** (`cbnv_dp_05`, phiên API riêng, không dùng `admin`) lúc
  13:31: cũng ra `DA_TONG_HOP`, `version = 3`;
- **tệp Excel do chính máy chủ sinh sau khi lưu** (bấm [Xuất Excel] lúc 13:32) chứa **đúng 13 con số đã
  lưu**: 12 · 4 · 3 · 7 · 7 · 37 · 29 · 7 · 14 · 8 · 680.000.000 · 160.000.000 · 30.000.000.

⇒ Dữ liệu **nằm ở máy chủ**, không phải chỉ trong phiên. Hai đường đo thống nhất.

> ⚠️ **Giới hạn phải khai thẳng:** bản dựng **không có chức năng đọc lại bản ghi tổng hợp theo mã** — tra
> `/api/docs-json` chỉ có `PATCH …/chinh-sua-tong-hop` và `POST …/hoan-thanh-tong-hop` (đều là ghi), không
> có đường đọc. Vì vậy phép đọc lại được thực hiện gián tiếp qua **bốn nguồn máy chủ độc lập** kể trên
> (trạng thái đợt · trạng thái hai báo cáo nguồn · phiên đăng nhập khác · nội dung tệp xuất). Không có
> nguồn nào mâu thuẫn.
>
> **Bổ sung sau khi đo phiếu 345 (13:56):** thân yêu cầu xuất tệp chỉ gửi `baoCaoIds` + `format`, nên
> **không phân biệt được** máy chủ *đọc bản ghi đã lưu* hay *cộng lại từ danh sách báo cáo được chọn*.
> ⇒ nguồn thứ tư (nội dung tệp xuất) chỉ chứng minh **số liệu khớp**, tự nó **không** chứng minh bản ghi
> tồn tại. Căn cứ chính của C1 là phản hồi 201 + ba nguồn còn lại. Nêu rõ để người đọc không suy rộng.

**Đặc tả:** `:1004` = `| 6 | Lưu bản ghi BC tổng hợp toàn quốc (loại TONG_HOP_TW) | — |`.

### 3.2 Vế C3 — "Lưu vết thao tác theo quy định" → ✅ ĐẠT

Đọc Nhật ký hệ thống (`GET /api/v1/audit-logs?tuNgay=2026-08-07&denNgay=2026-08-07`) bằng tài khoản QTHT
`admin` — **chỉ để đọc**. Có đúng một mục ứng với thao tác:

```
id                    03f23f21-b7e7-4891-b49a-8a4946a0f70b
module                DOT_BAO_CAO
entityType            BAO_CAO_CT_HTPL
hanhDong              TONG_HOP
entityId              57d4ce85-03b6-4d62-8f76-bb7546bec5c5   ← đúng bản ghi vừa lưu
thoiGian              2026-08-07T06:30:51.115Z               ← đúng mốc giờ bấm (13:30:51 giờ VN)
nguoiThucHienUsername cbnv_tw_05                             ← đúng tài khoản đã bấm
nguoiThucHienHoTen    CB Nghiệp vụ - Trung ương #05
nguoiThucHienVaiTro   Cán bộ Nghiệp vụ TW
donViTen              Cục Bổ trợ tư pháp - Bộ Tư pháp
```

**Đường đo 2 — đối chứng độc lập:** `entityId` và `thoiGian` của mục nhật ký trùng khít `id` và `ngayTao`
trong phản hồi 201 của chính lượt bấm; `nguoiThucHienId` `4f0f08e7-f832-4775-a331-d17dbc9f9965` trùng
`nguoiTaoId` của bản ghi. Hai đường thống nhất.

Ghi nhận (không chấm): ba trường `ipAddress`, `endpoint`, `responseCode` của mục nhật ký đều `null`.
Phiếu chỉ yêu cầu *"lưu vết thao tác theo quy định"* và `:1007` chỉ ghi `| 9 | Ghi nhật ký thao tác | BR-DATA-05 |`
⇒ không đủ căn cứ chấm sai, chuyển thành ghi nhận cho dev (mục 5).

**Đặc tả:** `:1007` = `| 9 | Ghi nhật ký thao tác | BR-DATA-05 |`.

### 3.3 Vế C4 — thông báo **"Đã tổng hợp báo cáo toàn quốc"** → ✅ ĐẠT, đúng nguyên văn

**Đường đo 1 — bộ bắt thông báo cài trước thao tác, không lọc trùng, đọc `innerText`:**

| # | Mốc giờ | Lớp nút DOM | Nội dung đọc được |
|---|---|---|---|
| 1 | `2026-08-07T06:30:51.061Z` | `ant-message ant-message-top …` | **`Đã tổng hợp báo cáo toàn quốc`** |
| 2 | `2026-08-07T06:30:51.064Z` | `ant-message-notice-wrapper …` | **`Đã tổng hợp báo cáo toàn quốc`** |

Hai nút DOM lệch nhau **3 mili-giây** là khung ngoài và phần thân của **cùng một** thông báo (đúng pattern
AntD đã ghi nhận ở lô F5) ⇒ **đúng 1 thông báo**. Đếm kèm số yêu cầu gửi đi: **đúng 1** yêu cầu
`POST /api/v1/dot-bao-caos/tong-hop` ⇒ không có hiện tượng hiện hai lần.

**Đường đo 2 — đối chứng độc lập:** phản hồi máy chủ của chính lượt bấm là **201** kèm bản ghi mới; thông
báo hiển thị đúng lúc đó. Chuỗi hiển thị **trùng khít từng chữ** với chuỗi đặc tả khai.

**Đặc tả:** `:1032` = `| I1 | Tổng hợp thành công | INF-XI-09-01 | "Đã tổng hợp báo cáo toàn quốc" | INFO |`.

### 3.4 Vế C2 — "chuyển trạng thái các đợt báo cáo đã chọn: Đã gửi Trung ương → Đã tổng hợp" → 🔎 GAP, KHÔNG CHẤM

**Ghi nhận hiện trạng đầy đủ trên cả hai trục, trước và sau:**

| Trục | Trường | **Trước** (13:14) | **Sau** (13:31, đọc lại sau khi tải lại trang) |
|---|---|---|---|
| **ĐỢT** | `DOT_BAO_CAO.trangThai` | `TAO_DOT` (`version 2`) | **`DA_TONG_HOP`** (`version 3`) |
| **ĐỢT** | `daGuiTw` / `ngayGuiTw` | `false` / `null` | `false` / `null` — **không đổi** |
| **ĐƠN VỊ** | `tienDo[].trangThaiNop` | `DA_NOP` / `DA_NOP` | `DA_NOP` / `DA_NOP` — **không đổi** |
| **BÁO CÁO** | `trangThai` (danh sách tổng hợp TW) | `DA_GUI_TW` / `DA_GUI_TW` | **`DA_TONG_HOP` / `DA_TONG_HOP`** |

**Nhãn người dùng nhìn thấy:**
- Tài khoản **TW** ở màn chi tiết đợt: thanh tiến trình dừng ở **bước 6 "Đã tổng hợp"**, ô Trạng thái ghi
  **"Đã tổng hợp"** (ảnh 02).
- Tài khoản **TW** ở màn tổng hợp: hai dòng đổi nhãn từ *"Đã gửi TW"* sang **"Đã tổng hợp"** (ảnh 01);
  báo cáo của đợt khác (Sở TP Hà Nội) **giữ nguyên "Đã gửi TW"** — tức chỉ các báo cáo **được chọn** bị đổi.
- Bảng "Tiến độ nộp theo đơn vị" của **chính đợt đó** vẫn hiển thị **"Đã nộp"** cho cả hai đơn vị.

**Vì sao vẫn không chấm:** đặc tả yêu cầu bước chuyển ở **trục ĐỢT** (`:1005`, `:1022`, `:1517`) nhưng tự
mâu thuẫn (đầu vào là **danh sách báo cáo theo đơn vị** `:993`; một đợt chỉ có một trạng thái `:1368`
trong khi phạm vi đợt tới ~70–83 đơn vị `:1367`, `:1398`; trục đơn vị `:1389` **không có** giá trị
`DA_TONG_HOP`). Chuẩn đã khóa **GAP** ⇒ luật khóa 5: kết quả đo trên web **không** biến GAP thành MATCH.

> Cần nói rõ để người ngoài không đọc nhầm thành lỗi: **web hiện tại làm ĐÚNG kỳ vọng của đối tác** ở phần
> quan sát được — đợt của các báo cáo đã chọn chuyển sang "Đã tổng hợp", đợt khác không bị đụng. Điểm chưa
> khớp đặc tả là **đợt đi thẳng `TAO_DOT → DA_TONG_HOP`, không đi qua `DA_GUI_TW`** như `:1517` mô tả, và
> `daGuiTw` vẫn `false`. Câu hỏi BA nhằm **đính chính/bổ sung đặc tả**, không chặn bàn giao.

**Về "bước chốt" (chuẩn §4.1 bẫy #10):** không cần — đợt đã sang `DA_TONG_HOP` **ngay sau** [Lưu tổng hợp];
tôi **không** gọi `POST /api/v1/bao-cao-ct-htpl/{id}/hoan-thanh-tong-hop` và trên màn cũng **không có**
nút "Hoàn thành/Chốt tổng hợp" nào.

## 4. Kết luận theo từng vế

| Vế | Quan hệ (đã khóa) | Kết quả đo |
|---|---|---|
| **C1** — lưu bản ghi tổng hợp toàn quốc | MATCH | ✅ **ĐẠT** — bản ghi `TH-TW-1786084251126`, loại `TONG_HOP_TW`, đọc lại được sau khi tải lại trang |
| **C2** — chuyển trạng thái đợt `DA_GUI_TW → DA_TONG_HOP` | **GAP** | 🔎 **Không chấm** — đã ghi nhận đủ ba trục trước/sau |
| **C3** — lưu vết thao tác | MATCH | ✅ **ĐẠT** — mục `TONG_HOP` đúng bản ghi, đúng mốc giờ, đúng tài khoản |
| **C4** — thông báo "Đã tổng hợp báo cáo toàn quốc" | MATCH | ✅ **ĐẠT** — đúng nguyên văn, 1 thông báo / 1 yêu cầu |

**Verdict phiếu:** ⚠️ **Cần BA** → ô `Trạng thái dev fix` = **`BA confirm`**
(flow 04 §Ca biên: *"Không vế nào Reopen mà còn DIFF/GAP → Cần BA"*; QĐ-01 của lô).

## 5. Ghi nhận cho dev (không ảnh hưởng verdict)

1. **Mục nhật ký thiếu ba trường bối cảnh.** `ipAddress`, `endpoint`, `responseCode` đều `null`. Phiếu và
   `:1007` không đòi các trường này nên không chấm; nêu để dev cân nhắc bổ sung cho việc truy vết.
2. **Không có đường đọc lại bản ghi tổng hợp.** Sau khi lưu, không có chức năng nào cho phép mở lại bản
   tổng hợp toàn quốc để xem/kiểm — kể cả màn chi tiết đợt cũng **vẫn hiển thị số liệu của một đơn vị**
   (Bộ KH&ĐT: 8 · 3 · 2 · …) chứ không phải số tổng đã lưu (12 · 4 · 3 · …). Cán bộ chỉ thấy được số tổng
   qua tệp xuất. Phiếu 343 không nhắc việc xem lại nên **không chấm**; đề nghị dev/BA xem lại.
3. **Màn "Tổng hợp báo cáo toàn quốc" không có lối vào trên menu** — đã nêu ở [`do/THBCTHCT_02.md` §5](THBCTHCT_02.md).

## 6. Câu hỏi cho nghiệp vụ (vế C2)

> **CẦN BA CONFIRM:** phiếu kỳ vọng *"chuyển trạng thái **các đợt báo cáo đã chọn**: Đã gửi Trung ương →
> Đã tổng hợp"*. Đặc tả quy định điều đó ở **trục ĐỢT** (`srs-fr-15-ct-htpldn.md:1005`, `:1022`, `:1517`)
> nhưng **tự mâu thuẫn**: đầu vào của chính chức năng là **danh sách BÁO CÁO theo đơn vị** (`:993`); một
> đợt chỉ có **một** giá trị trạng thái (`:1368`) trong khi phạm vi đợt là **~70–83 đơn vị** (`:1367`,
> `:1398`); còn trục đơn vị (`:1389`) **không có** giá trị `DA_TONG_HOP`; đồng thời `:937` và `:938` khai
> cùng một hành vi ở hai bậc khác nhau.
>
> **Web/dev hiện tại đo được:** trục ĐỢT chuyển **`TAO_DOT` → `DA_TONG_HOP`** (không đi qua `DA_GUI_TW`,
> cờ `daGuiTw` vẫn `false`); trục ĐƠN VỊ giữ nguyên `DA_NOP`; trục BÁO CÁO chuyển `DA_GUI_TW` →
> `DA_TONG_HOP` đúng cho **hai báo cáo được chọn**, báo cáo của đợt khác không bị đụng. Cán bộ TW nhìn thấy
> nhãn "Đã tổng hợp" ở cả màn chi tiết đợt lẫn màn tổng hợp; bảng tiến độ theo đơn vị vẫn ghi "Đã nộp".
>
> **Câu hỏi:** sau khi TW lưu tổng hợp, **cái gì** phải chuyển sang "Đã tổng hợp" — (a) **cả đợt**, kể cả
> khi mới tổng hợp một phần số đơn vị; (b) **từng bản ghi nộp của đơn vị đã được chọn** (khi đó xin bổ sung
> giá trị `DA_TONG_HOP` vào `:1389`); hay (c) **bản ghi báo cáo tổng hợp TW** là nơi duy nhất mang trạng
> thái này? Và trạng thái cán bộ nhìn thấy ở chi tiết đợt là của **đơn vị mình** hay của **đợt**? Ngoài ra
> xin xác nhận đợt có bắt buộc đi qua `DA_GUI_TW` trước khi sang `DA_TONG_HOP` không, vì `:1517` khai bước
> chuyển từ `DA_GUI_TW` nhưng thực tế đợt chưa từng đạt trạng thái đó.
>
> *(Cùng gốc với câu hỏi đã gửi ở bàn giao lô F5 §3 Nhóm 2 — **liên kết, không mở câu hỏi trùng**.)*

## 7. 🔴 Dữ liệu đã thay đổi trên môi trường nội bộ

| Đối tượng | Trước | Sau | Do thao tác |
|---|---|---|---|
| Đợt `DOT-THBC01-UAT` (`d7a62f6e-a119-4582-8b08-f935d25c534b`) | `TAO_DOT`, `version 2` | **`DA_TONG_HOP`**, `version 3` | [Lưu tổng hợp] 13:30:50 |
| Báo cáo `c4801d2d…` (Bộ KH&ĐT) | `DA_GUI_TW` | **`DA_TONG_HOP`** | như trên |
| Báo cáo `df6498aa…` (Sở TP An Giang) | `DA_GUI_TW` | **`DA_TONG_HOP`** | như trên |
| **Bản ghi mới** `57d4ce85-03b6-4d62-8f76-bb7546bec5c5` | không tồn tại | **được tạo** — `TH-TW-1786084251126`, loại `TONG_HOP_TW`, nhận xét mang chuỗi `QA-F8-343-20260807-1330` | như trên |

**Hệ quả cho lô sau:** cặp báo cáo `DA_GUI_TW` của đợt `DOT-THBC01-UAT` **đã dùng hết**, không tổng hợp lại
được (nút [Tổng hợp] bị vô hiệu kèm chú thích *"Trong danh sách chọn có báo cáo thuộc đợt đã tổng hợp —
không tổng hợp lại được"*). Muốn có tiền đề lượt hai: Bộ KH&ĐT còn 2 báo cáo `CHO_PHE_DUYET`
(`c19b1bc2…` ở `DOT-SO_BO_NAM-2026-1`, `a63bf70c…` ở `DOT-SO_BO_6_THANG-2026-1`) — `cbpd_bn_03` duyệt rồi
`cbnv_bn_03` gửi TW. Ngoài ra còn báo cáo `4db99158…` (Sở TP Hà Nội, đợt `DOT-SO_BO_NAM-2026-1`) vẫn
`DA_GUI_TW`, chưa bị đụng.

**Không đụng dữ liệu của đối tác. Không ghi thẳng DB. Không ép trạng thái đợt bằng đường dữ liệu.**

## 8. Ảnh bằng chứng

| # | Tệp | Chứng minh | Drive |
|---|---|---|---|
| 01 | `image/THBCTHCT_01-01-sau-luu-2-bc-da-tong-hop.png` | Ngay sau [Lưu tổng hợp]: hai báo cáo được chọn đổi nhãn sang "Đã tổng hợp", báo cáo đợt khác giữ "Đã gửi TW" | https://drive.google.com/file/d/1S1_DK0Kw4HkBGgXgX3v1ILxc-9EUP57W/view?usp=drivesdk |
| 02 | `image/THBCTHCT_01-02-tai-lai-trang-dot-da-tong-hop.png` | Sau khi **tải lại trang bằng địa chỉ**: đợt ở bước 6 "Đã tổng hợp", hai đơn vị vẫn "Đã nộp" | https://drive.google.com/file/d/1M7omE-bcvFN3JpXqlVzrLHx_-AjELdxy/view?usp=drivesdk |

Tệp Excel do máy chủ sinh sau khi lưu (dùng làm một nguồn đọc lại số liệu ở §3.1) lưu tại
`files/BaoCaoTongHopCTHTPL_20260807_1332.xlsx`.

## 9. Năm câu hỏi cổng verdict (flow 04)

1. **Đã bấm bằng giao diện thật chưa?** Rồi — tick ô chọn, [Tổng hợp (2)], nhập nhận xét, [Lưu tổng hợp].
2. **Có đủ hai đường đo độc lập không?** Có, cho từng vế: C1 (phản hồi tạo bản ghi ↔ đọc lại từ máy chủ sau
   khi tải lại trang, thêm phiên đăng nhập khác và nội dung tệp xuất); C3 (mục nhật ký ↔ phản hồi 201 của
   chính lượt bấm); C4 (bộ bắt thông báo ↔ phản hồi máy chủ). Không đường nào mâu thuẫn.
3. **Có Pass bằng quan sát tĩnh không?** Không — mọi kết luận từ lượt bấm mới lúc 13:30:50.
4. **Có hạ GAP thành MATCH để ghi Test done không?** Không — C2 giữ GAP, phiếu chốt `BA confirm`.
5. **Có khai đủ dữ liệu đã đổi không?** Có — §7, kèm hệ quả cho lô sau.
