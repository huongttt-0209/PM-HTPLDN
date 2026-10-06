# Phép đo — LBCKQTHCT_01 (dòng 335) · 2026-08-07

**Verdict logic: CẦN BA** — 3/3 vế `MATCH` đều ĐẠT (gồm đúng vế đối tác báo hỏng ở vòng 2);
1 vế `GAP` (thông báo nhanh) bị luật khóa chặn Pass.

Chuẩn chấm: [`../chuan/LBCKQTHCT_01.md`](../chuan/LBCKQTHCT_01.md) · Chuẩn bị chung: [`../chuan/00-CHUAN-BI-CHUNG.md`](../chuan/00-CHUAN-BI-CHUNG.md)

---

## 1. Điều kiện đo

| Mục | Giá trị |
|---|---|
| Môi trường | `https://18.143.165.120.nip.io` |
| Bản dựng | Sidebar **HTPLDN · V1.0.9** · bó mã `assets/index-DsMHK7Dp.js` · ETag `"6a74d7ad-1127fb"` · Last-Modified `07/08/2026 01:51 VN` |
| Kiểm bản dựng trong tab | ✅ đọc lại `script[src]` ngay trong tab đo → đúng `index-DsMHK7Dp.js`, **không phải tab chạy mã cũ** |
| Tài khoản thực dùng | **`cbnv_hn`** — *QA CB Nghiep vu Ha Noi*, vai trò **`CB_NV_DP`**, cấp **ĐP**, đơn vị **Sở Tư pháp Hà Nội** (`donViId 00000000-0000-4000-8002-000000000001`), userId `87bb5785` |
| Vì sao không dùng `cbnv_dp_01` | Đơn vị của `cbnv_dp_01` đã ở `DANG_LAP`/`DA_NOP` trên cả 3 đợt ⇒ **không quan sát được phép chuyển `CHUA_NOP → DANG_LAP`**. `cbnv_bn_01` cũng đã `DA_NOP`/`CHO_DUYET`. `cbnv_hn` là **cùng vai trò `CB_NV_DP` + cùng cấp ĐP** (đúng vai trò trong thông báo 403 của đối tác), chỉ khác đơn vị — đúng công thức C §3.3 chuẩn chấm, SRS `:712` cho phép cả ĐP lẫn BN |
| Bản ghi đo | Đợt `DOT-SO_BO_NAM-2026-1` — `e9909d96-1391-463b-8072-b1b56c319f8e`, kỳ *Sơ bộ năm*, biểu mẫu **21a**, hạn nộp 31/12/2026 |
| Tiền đề `:717` | ✅ đơn vị **nằm trong** `phamViDonViNopIds` (83 đơn vị) — đã kiểm bằng số trước khi bấm |
| Tiền đề `:718` | ✅ `trangThaiNop = CHUA_NOP`, `baoCaoId = null` **trước** khi bấm |
| Đã seed gì | **Không tạo đợt mới, không đổi bản ghi của ai.** Chỉ thao tác đúng luồng nghiệp vụ trên đợt sẵn có bằng đơn vị chưa từng nộp |
| Mutation để lại | Đợt `DOT-SO_BO_NAM-2026-1` × đơn vị *Sở Tư pháp Hà Nội*: `CHUA_NOP → DANG_LAP`, sinh báo cáo `4db99158-5bc4-4069-9d52-cfc756aadc2e` |

---

## 2. Kết quả từng vế

| Vế | Quan hệ | Kết quả | Số đo quyết định |
|---|---|---|---|
| **C1** — trạng thái nộp đơn vị → "Đang lập" (`:746`) | MATCH | ✅ **ĐẠT** | `trangThaiNop`: `CHUA_NOP` → **`DANG_LAP`**; `baoCaoId`: `null` → **`4db99158…`**; giữ nguyên sau khi **tải lại trang bằng địa chỉ** |
| **C2** — lưu nội dung báo cáo chi tiết (`:745`) | MATCH | ✅ **ĐẠT** | Nhận xét + ghi chú + 2 chỉ tiêu nhập tay đọc lại **khớp từng chữ** sau tải lại trang, trên **cả 2 đường đo** |
| **C3** — lưu vết thao tác (`:747`) | MATCH | ✅ **ĐẠT** | Nhật ký có `CREATE·DOT_BAO_CAO` + 2× `UPDATE·BAO_CAO_CT_HTPL`, đúng tài khoản/vai trò/đơn vị/mốc giờ |
| **C4** — thông báo nhanh "Đã lưu nháp" | **GAP** | ⚠️ **KHÔNG CHẤM** | Web hiện *"Đã lưu nháp thành công"*. SRS im lặng ⇒ luật khóa 5 cấm Pass/Reopen vế này |

### 2.1 C1 — chi tiết (vế quyết định vòng này)

Chuỗi thao tác **bằng giao diện thật**: [Lập báo cáo] → hộp thoại *"Bắt đầu lập báo cáo? Hệ thống sẽ tạo báo
cáo nháp để bạn nhập số liệu."* → [Đồng ý].

| Thời điểm | Trục ĐƠN VỊ `trangThaiNop` | Trục ĐỢT `trangThai` | `baoCaoId` |
|---|---|---|---|
| Trước khi bấm | `CHUA_NOP` | `TAO_DOT` | `null` |
| Ngay sau [Đồng ý] | — | — | — |
| **Sau khi tải lại trang bằng địa chỉ** | **`DANG_LAP`** ✅ | `TAO_DOT` | **`4db99158-5bc4-4069-9d52-cfc756aadc2e`** ✅ |

- Giao diện: ô **Trạng thái** đổi `Tạo đợt` → **`Đang lập báo cáo`**, nút [Lập báo cáo] biến mất, hiện
  [Làm mới] [Lưu nháp] [Trình duyệt KQ]; bước 1 trên thanh tiến trình chuyển sang dấu tích.
- Mạng: đúng **1** yêu cầu `POST /api/v1/dot-bao-caos/{id}/start` → **200**. Không double-submit.
- Ảnh: [`../image/LBCKQTHCT_01-C1-truoc-khi-bam-taodot-chuanop.png`](../image/LBCKQTHCT_01-C1-truoc-khi-bam-taodot-chuanop.png) ·
  [`../image/LBCKQTHCT_01-C1-sau-tai-lai-dang-lap-bao-cao.png`](../image/LBCKQTHCT_01-C1-sau-tai-lai-dang-lap-bao-cao.png)

> 🔴 **Đây chính là điểm đối tác báo hỏng ở vòng 2** (*"Hệ thống không chuyển trạng thái thành «Đang lập»"*).
> **Không tái hiện** trên bản V1.0.9.

### 2.2 C2 — chi tiết

Chuỗi mốc-giờ duy nhất **ghi lại trước khi bấm**: `QA-BCCT-20260807-0209-nhan-xet` ·
`QA-BCCT-20260807-0209-ghichu-ct1` · chỉ tiêu 12 = `1207` · chỉ tiêu 13 = `1308`.

| Trường | Nhập vào | Đường 1 — giao diện sau tải lại | Đường 2 — máy chủ sau tải lại | Khớp? |
|---|---|---|---|---|
| Nhận xét, kiến nghị | `QA-BCCT-20260807-0209-nhan-xet` | y hệt | `nhanXet` y hệt | ✅ từng chữ |
| Ghi chú chỉ tiêu 1 | `QA-BCCT-20260807-0209-ghichu-ct1` | y hệt | `soLieuTongHop.ghiChu.soTvvKienToan` y hệt | ✅ từng chữ |
| 12. KP chi HĐ khác | `1207` | `1207` | `kpHoatDongKhac = 1207` | ✅ |
| 13. KP xã hội hóa | `1308` | `1308` | `kpXaHoiHoa = 1308` | ✅ |

- Mạng: đúng **1** yêu cầu `PATCH /api/v1/dot-bao-caos/{id}/bao-cao` → **200**, thân yêu cầu mang **cả**
  `soLieuTongHop` lẫn `nhanXet`.
- Ảnh: [`../image/LBCKQTHCT_01-C2-sau-tai-lai-du-lieu-doc-lai-duoc.png`](../image/LBCKQTHCT_01-C2-sau-tai-lai-du-lieu-doc-lai-duoc.png)
- Ghi nhận cấu trúc màn (không phải tiêu chí chấm): chỉ tiêu **1–11 do hệ thống tự tính**, hiện dạng
  `0 (HT)` và **không phải ô nhập**; chỉ **12–13** nhập tay. Mỗi dòng có ô **Ghi chú** riêng.
  Thẻ *Biểu mẫu* và thẻ *Nhận xét, kiến nghị* có **2 nút [Lưu nháp] độc lập** — nút thẻ biểu mẫu
  **không** lưu nhận xét.

### 2.3 C3 — chi tiết

Đọc `GET /api/v1/audit-logs` bằng **phiên API riêng của tài khoản quản trị** (vai trò `CB_NV_DP` bị chặn
`403 ERR-PERM-SYS-00-01` — đúng phân quyền). **Quản trị chỉ dùng để ĐỌC nhật ký, không dùng ra verdict**;
mọi vế khác đo bằng chính `cbnv_hn`.

| Mốc giờ (UTC) | Hành động | Thực thể | Đường dẫn | HTTP | Người thực hiện |
|---|---|---|---|---|---|
| `19:05:49.800` | `CREATE` | `DOT_BAO_CAO` | `POST …/dot-bao-caos/e9909d96…/start` | 200 | `cbnv_hn` · CB NV ĐP · Sở Tư pháp Hà Nội |
| `19:09:34.129` | `UPDATE` | `BAO_CAO_CT_HTPL` | `PATCH …/dot-bao-caos/e9909d96…/bao-cao` | 200 | nt |
| `19:10:50.192` | `UPDATE` | `BAO_CAO_CT_HTPL` | `PATCH …/dot-bao-caos/e9909d96…/bao-cao` | 200 | nt |

---

## 3. CẦN BA CONFIRM (vế C4)

> **CẦN BA CONFIRM:** đối tác kỳ vọng *khi lưu nháp thành công, hệ thống hiển thị thông báo nhanh
> **"Đã lưu nháp"***; SRS **IM LẶNG** — `srs-fr-15-ct-htpldn.md` FR-XI-06 (`:701`–`:770`) có Outputs chỉ
> *"Báo cáo CT"*, Postconditions chỉ *record created + AUDIT_LOG*, Error Handling chỉ `ERR-XI-06-01`,
> 2 dòng Acceptance Criteria **không** nhắc thông báo; dòng màn hình `:1170` liệt kê `[Huy] [Luu nhap]
> [Trinh duyet KQ]` mà **không** đặc tả thông báo — trong khi `:1173` (Gửi TW) **có** ghi *"Toast success"*
> và cả file chỉ có 3 mã `INF-` (`:381`, `:403`, `:1032`), **không mã nào** thuộc FR-XI-06;
> **web/dev hiện tại ĐÚNG kỳ vọng đối tác** — bấm [Lưu nháp] hiện đúng **1** thông báo nhanh
> *"Đã lưu nháp thành công"*, và bấm [Lập báo cáo] hiện *"Đã bắt đầu lập báo cáo"*.
>
> **Câu hỏi BA:** (a) Thao tác Lưu nháp ở FR-XI-06 **có bắt buộc** phản hồi thành công cho người dùng không?
> (b) Nếu có, câu chữ có bị ràng buộc đúng chuỗi *"Đã lưu nháp"*, hay chỉ cần một thông báo thành công bất kỳ
> (hiện là *"Đã lưu nháp thành công"*)? (c) Nếu BA chốt bắt buộc, xin **bổ sung mã `INF-XI-06-*`** vào bảng
> Error/Info Handling của FR-XI-06 để lần sau chấm được.
>
> ⚠️ Mục đích câu hỏi là **bổ sung vào đặc tả** — **KHÔNG chặn bàn giao**. Không có lỗi nào chưa xử lý ở vế này.

---

## 4. Quan sát ngoài vế — chỉ ghi nhận, KHÔNG đổi verdict

| # | Quan sát | Xử lý |
|---|---|---|
| 1 | Mỗi thao tác sinh **2 dòng nhật ký** cùng mốc giờ ±30ms: một dòng có `endpoint`+`responseCode` mang `entityId` = id ĐỢT, một dòng `endpoint = null` mang `entityId` = id BÁO CÁO. | **Không phải lỗi đã xác nhận** — đọc hợp lý là 2 tầng ghi (nghiệp vụ + HTTP). SRS im lặng về độ mịn dòng nhật ký ⇒ chỉ ghi nhận |
| 2 | Dòng nhật ký có `entityType = BAO_CAO_CT_HTPL` nhưng `entityId` lại là id của ĐỢT | **Candidate 1 dòng** — SRS im lặng, không điều tra trong case này |
| 3 | Thẻ *Biểu mẫu* và thẻ *Nhận xét* có 2 nút [Lưu nháp] riêng; SRS `:1170` khai **một** nhóm nút `[Huy] [Luu nhap] [Trinh duyet KQ]` | **Candidate 1 dòng** — không thuộc vế nào của phiếu; muốn xác nhận phải mở thêm nhánh ⇒ không điều tra |
| 4 | Không thấy **[Hủy]** trong nhóm nút dù `:1170` có khai | **Candidate 1 dòng** — cùng lý do trên |

**Không** hồi quy `BUG-BC-TOAST-LOI-HIEN-2-LAN` (tuần 4): mỗi thao tác chỉ sinh **1** thông báo.
Bộ bắt ghi 2 node nhưng là cặp `ant-message` (thẻ bọc) + `ant-message-notice-wrapper` (thẻ con) —
đã phân giải đúng, không phải 2 thông báo.

---

## 5. Ghi chú về độ tin cậy của phép đo

- ⚠️ **Một lượt đo đã bị hỏng dụng cụ và đã đo lại.** Sau khi tải lại trang bằng địa chỉ, bộ bắt thông báo và
  bản vá đếm yêu cầu bị xoá theo ngữ cảnh trang; lượt bấm [Lưu nháp] đầu tiên vì thế cho ra *"0 thông báo,
  0 yêu cầu"* — **đó là dụng cụ chưa cài lại, KHÔNG phải hệ thống im lặng**. Đã xác minh bằng cách đọc lại
  bản ghi máy chủ (dữ liệu **đã** lưu), rồi cài lại dụng cụ và đo lại lượt sau. Số liệu ở §2 lấy từ lượt đo
  có đủ dụng cụ.
- Bằng chứng đối tác cho **claim vòng 2 không tồn tại** (file `LBCKQTHCT_01.webm` là của vòng 1, quay trên
  bản **V1.0 ngày 20/07/2026**). Kết luận ở đây dựa trên việc **tự tái hiện đúng luồng phiếu mô tả**.
- Verdict chỉ có hiệu lực cho môi trường và bản dựng ghi ở §1.
