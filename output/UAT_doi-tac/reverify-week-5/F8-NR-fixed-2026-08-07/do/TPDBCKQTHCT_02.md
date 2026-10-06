# Nhật ký đo — `TPDBCKQTHCT_02` (dòng 341 tab `bug`)

**Ngày:** 2026-08-07 · **Quy trình:** [`flows/04-verify-bug-dev-fix-khong-ho-so.md`](../../../../../flows/04-verify-bug-dev-fix-khong-ho-so.md)
**Chuẩn chấm đã khóa:** [`chuan/TPDBCKQTHCT_02.md`](../chuan/TPDBCKQTHCT_02.md) — 2 vế, **cả hai `MATCH`**, route `TEST` ×2.

---

## 0. Đọc lại dòng phiếu trên bảng trước khi đo (bắt buộc)

Đọc lúc **12:56 ngày 07/08/2026** bằng `tools/sheet_dump_bug_rows_2026-08-07.py --rows 341` (chỉ đọc).
Không có thay đổi so với bản chụp 11:3x:

| Ô | Giá trị đọc được |
|---|---|
| `Mã TC` (D) | `TPDBCKQTHCT_02` |
| `Trạng thái` (N) | `N/R` · `Dopai` (O) `N/R` |
| `Kết quả thực tế` (L) · `Ảnh/vieo 1` (M) · `TKM phản hồi lần 1` (Q) | **RỖNG cả ba** ⇒ đối tác **chưa từng chạy** phiếu |
| `Trạng thái dev fix` (R) | `Fixed` |
| `Kết quả verify` (T) | **RỖNG** ⇒ không có nội dung cũ để giữ |
| `Kết quả mong đợi` (K) | `Hệ thống hiển thị "Vui lòng hoàn chỉnh báo cáo trước khi trình".` |
| `DEV phản hồi lần 1` (S) | *"BA chốt 06/08/2026 — Loại 2 … 'báo cáo hoàn chỉnh' = có mặt đủ các chỉ tiêu của biểu mẫu mà đơn vị đã chọn. … Dev đã siết cổng 'báo cáo hoàn chỉnh' khi trình phê duyệt theo đúng định nghĩa này, áp cho cả 3 giá trị biểu mẫu."* |

## 1. Môi trường + vân tay bản dựng

| Hạng mục | Giá trị |
|---|---|
| Môi trường | `https://18.143.165.120.nip.io` — env **NỘI BỘ** (đối tác nghiệm thu trên `htpldn-uat.ospgroup.vn`) |
| **Vân tay ĐẦU phiên** (12:54:37) | `GET /` → `assets/index-eWHwDgt2.js` · `assets/index-DVlgOkLg.css` · `last-modified: Fri, 07 Aug 2026 02:11:03 GMT` · `etag W/"6a753eb7-428"` |
| Bó mã trình duyệt thực nạp | `evaluate_script` đọc `<script src>` của trang `/login` → **`/assets/index-eWHwDgt2.js`** (khớp) |
| **Vân tay CUỐI phiên** | ghi ở [`BAN-GIAO-BCCT.md`](../BAN-GIAO-BCCT.md) §vân tay |
| Nhãn thanh bên | `HTPLDN · V1.0.10` — **không** dùng làm định danh (đã có ca lùi nhãn) |
| Tài khoản đo | **`cbnv_dp_03`** (`CB_NV_DP`, cấp `DP`, `donViId 00000000-0000-4000-8002-000000000006` = Sở Tư pháp An Giang), mật khẩu `Test@1234`, đăng nhập bằng **giao diện thật** + mã 6 số ở MailHog. **Không** dùng `admin`, **không** dùng cấp TW (đúng `:784` + `:712`) |

## 2. Tiền đề — dựng theo **TĐ-A** (hình thái sạch nhất)

**Bản ghi dùng:** đợt **`DOT-SO_BO_6_THANG-2026-1`** (`a61e07f1-e205-4948-ad7d-a3ccac49830a`), biểu mẫu
`MAU_21A`, báo cáo của Sở Tư pháp An Giang **`f445b699-04bd-4c94-ab77-9ca118c78dd0`**.

**Trạng thái TRƯỚC khi dựng** (đọc bằng API, phiên `cbnv_dp_03`, 12:55):
`DOT.trangThai = TAO_DOT` (version 1) · `DON_VI.trangThaiNop = DANG_LAP` · `BAO_CAO.trangThai = DU_THAO` ·
`soLieuTongHop` = 3 khóa (`soVuViec:3`, `tongChiPhi:0`, `soDnDuocHoTro:0`).

**🔴 Quan sát quyết định về hình thái ô nhập** (đọc DOM từng ô, **không** đoán):

| Nhóm | Số chỉ tiêu | Cột "Kỳ này" |
|---|---|---|
| Chỉ tiêu 1–11 | 11 | **KHÔNG có ô nhập** — hiển thị chữ `N (HT)` (hệ thống tự tính) |
| Chỉ tiêu 12 (KP chi HĐ khác) · 13 (KP xã hội hóa) | 2 | **CÓ ô nhập số** (`ant-input-number-input`), đang trống |

⇒ Áp đúng TĐ-A: **điền ô 12, CỐ Ý để trống ô 13.**

**Thao tác dựng (bằng giao diện):** điền `12. KP chi HĐ khác = 40000000` + ô Ghi chú của chính dòng đó =
`QA-F8-341-20260807-1300`; **để trống `13. KP xã hội hóa`** → bấm **[Lưu nháp]**.

Yêu cầu giao diện gửi đi (đọc từ tab Mạng, `PATCH /api/v1/dot-bao-caos/{id}/bao-cao` → **200**):
```
soLieuTongHop = { soTvvKienToan:1, soCuocTapHuan:0, soHoiNghiDoiThoai:0, soVBTraLoiUBND:0,
                  soVBTvMangLuoiTVV:0, soHsTiepNhan:0, soHsGiaiQuyetTong:0, hsDoanhNghiepVua:0,
                  hsDoanhNghiepNho:0, hsDoanhNghiepSieuNho:0, kpHoTroTvpl:0,
                  soVuViec:3, tongChiPhi:0, soDnDuocHoTro:0,
                  kpHoatDongKhac:40000000, ghiChu:{kpHoatDongKhac:"QA-F8-341-20260807-1300"} }
```
⇒ giao diện **có gửi đủ 11 khóa tự tính**; **thiếu đúng một khóa `kpXaHoiHoa`** — chính là ô người dùng
cố ý bỏ trống. *(Điểm đứt lô F5 mô tả cho dòng 340 — "giao diện không gửi 11 khóa" — **không còn**.)*

**Xác minh tiền đề sau khi TẢI LẠI TRANG BẰNG ĐỊA CHỈ:** ô 12 = `40000000` + ghi chú mốc-giờ; **ô 13 vẫn TRỐNG**.
Ảnh: `image/TPDBCKQTHCT_02-01-tien-de-chi-tieu-13-de-trong.png`.

⇒ Báo cáo **thực sự "chưa đầy đủ"** theo đúng định nghĩa `:802` (*"Ô để trống là chưa điền; giá trị 0 là đã
điền"*) — **không** phải "chưa đầy đủ do hệ thống tự coi là thiếu". Tránh được bẫy PASS oan §4.2 mục 1.

## 3. Đo từng vế

### C1 — Chặn thao tác khi báo cáo chưa đầy đủ · `MATCH` · ✅ **ĐẠT**

Đặc tả `srs-fr-15-ct-htpldn.md:830` = *"**Given** báo cáo còn chỉ tiêu bỏ trống **When** CB NV nhấn "Trình phê
duyệt" **Then** chặn + báo `ERR-XI-07-01`"*.

**Đường 1 — giao diện thật.** Bấm nút **[Trình duyệt KQ]** (bấm bằng chuột thật qua công cụ điều khiển trình
duyệt, uid `11_186`) → hiện hộp xác nhận **"Trình duyệt kết quả?"** với [Hủy] [Đồng ý] → bấm **[Đồng ý]**
lúc **13:00:18**.
Đúng **MỘT** yêu cầu gửi đi: `POST /api/v1/dot-bao-caos/a61e07f1…/submit-bc` body `{"version":1}` → **HTTP 422**.
Thao tác **không đi lọt**: thanh tiến trình vẫn ở bước **2 "Đang lập BC"**, ô Trạng thái vẫn **"Đang lập báo cáo"**
(ảnh `…-02-…` và `…-03-…`).

**Đường 2 — đối chứng độc lập, đọc lại bản ghi ở máy chủ** (13:02:07, bằng **chính phiên `cbnv_dp_03`**,
cookie-auth, **không** dùng `admin`):

| Trục | Trước khi bấm | Sau khi bấm | Kết luận |
|---|---|---|---|
| ĐỢT `DOT_BAO_CAO.trangThai` | `TAO_DOT` (version 1) | `TAO_DOT` (version 1) | **không đổi** |
| ĐƠN VỊ `trangThaiNop` | `DANG_LAP` | `DANG_LAP` | **không đổi** (KHÔNG sang `CHO_DUYET`) |
| BÁO CÁO `trangThai` | `DU_THAO` | `DU_THAO` | **không đổi** |
| `ngayGuiDuyet` / `nguoiGuiDuyetId` | `null` / `null` | `null` / `null` | **không có dấu vết trình duyệt** |
| `daGuiTw` / `ngayGuiTw` | `false` / `null` | `false` / `null` | không đổi |

**Hai đường khớp nhau ⇒ DỪNG, không thêm đường thứ ba** (flow 04 §Giai đoạn B mục 8).

### C2 — Câu chữ hiển thị cho người dùng · `MATCH` (kể cả chuỗi) · ✅ **ĐẠT**

Đặc tả `srs-fr-15-ct-htpldn.md:825` =
`| E1 | BC chưa hoàn chỉnh | ERR-XI-07-01 | "Vui lòng hoàn chỉnh báo cáo trước khi trình" | ERROR |`

**Đường 1 — chữ người dùng nhìn thấy.** Bộ bắt (`MutationObserver` trên `document.body`) cài **TRƯỚC** khi bấm,
đọc bằng `innerText`, **KHÔNG lọc trùng**. Bắt được sau khi bấm [Đồng ý]:

| Mốc giờ | Thẻ | Lớp | Chữ đọc được |
|---|---|---|---|
| `06:00:18.647Z` | `DIV` | `ant-message ant-message-top …` | **"Vui lòng hoàn chỉnh báo cáo trước khi trình"** |
| `06:00:18.647Z` | `DIV` | `ant-message-notice-wrapper …` | **"Vui lòng hoàn chỉnh báo cáo trước khi trình"** |

🔴 **Đếm theo mốc giờ khác nhau, không theo độ dài mảng:** hai nút DOM trên có **cùng một mốc giờ**
(`…18.647Z`) và là khung ngoài + nút con của **cùng một** thông báo ⇒ **1 thông báo**, kèm đúng **1 yêu cầu
gửi đi** (`submit-bc`). Không có hiện tượng thông báo hiện hai lần.

**Đường 2 — đối chứng độc lập, phản hồi máy chủ của chính lượt bấm đó** (`reqid=524`, 422):
```json
{"success":false,"error":{"code":"ERR-XI-07-01",
 "message":"Vui lòng hoàn chỉnh báo cáo trước khi trình",
 "details":{"chiTieuConThieu":["13. KP xã hội hóa"]},
 "timestamp":"2026-08-07T06:00:18.749Z"}}
```
Chuỗi hiển thị **trùng khít từng chữ** với `message` của máy chủ và với `:825`.

## 4. Verdict

**Pass** → ô `Trạng thái dev fix` (R) = **`Test done`**.

- 2/2 vế `MATCH` (C1, C2) **đều đạt**, trên **một lượt bấm mới** bằng giao diện thật sau bản dựng đang đo.
- **Không còn** vế `DIFF`/`GAP` nào ⇒ theo bảng Verdict flow 04 và QĐ-01, đây là **Pass**, ghi `Test done`.
- ⚠️ Theo flow 04 §Ca biên: đội **không có ảnh "lỗi cũ"** của chính mình (đối tác chưa từng chạy phiếu, ô
  `Kết quả thực tế` rỗng) ⇒ chỉ kết luận được **hiện trạng đúng đặc tả**, **không** viết "bản sửa đã có tác dụng".

## 5. Ghi nhận (KHÔNG chấm, không kéo verdict) — gửi dev/BA

1. 🟢 **Mã lỗi nay ĐÚNG đặc tả.** `:825` khai `ERR-XI-07-01`; máy chủ trả đúng `ERR-XI-07-01`.
   *(Lô F5 đo được `ERR-VAL-XI-07-02` và đã ghi nhận ở bàn giao F5 §4 mục 2 — **mục đó nay có thể đóng**.)*
   Mã lỗi **không** phải vế chấm của phiếu 341 (§1.2 file chuẩn), nên đây chỉ là ghi nhận tích cực.
2. 🟢 **Danh sách chỉ tiêu còn thiếu nay chỉ liệt kê đúng ô người dùng bỏ trống** — `details.chiTieuConThieu`
   = `["13. KP xã hội hóa"]`, **không** còn kéo theo 11 chỉ tiêu tự tính. Cùng với việc giao diện **đã gửi**
   đủ 11 khóa tự tính khi [Lưu nháp], điểm đứt mà lô F5 mô tả cho **dòng 340 (`TPDBCKQTHCT_01`, đang Reopen)**
   **không còn tái hiện**. ⇒ **Chuyển thông tin này cho người đo dòng 340**; phiếu 341 không kết luận thay.
3. **11/13 chỉ tiêu vẫn không có ô nhập** ở cột "Kỳ này" (hiển thị `N (HT)`) — đây là thiết kế "hệ thống tự
   tính", không phải lỗi của phiếu 341. Ghi lại vì nó quyết định cách dựng tiền đề.

## 6. Quan sát ngoài vế — **candidate**, KHÔNG log thành bug

| # | Hiện tượng | Xuất hiện tại | Vì sao chỉ là candidate |
|---|---|---|---|
| 1 | **Hộp xác nhận "Trình duyệt kết quả?" không tự đóng** sau khi máy chủ từ chối (422). Người dùng thấy thông báo lỗi nhưng hộp thoại vẫn còn, phải tự bấm [Hủy] | ngay sau [Đồng ý], ảnh `…-02-…` | Đặc tả **im lặng** về hành vi đóng/mở hộp xác nhận khi thao tác bị từ chối — FR-XI-07 `:773`–`:831` không có dòng nào quy định. Không đủ căn cứ ⇒ ghi candidate, **không** thêm phép đo, **không** mở dòng bug mới |

Không đổi verdict vì không chặn điều kiện đạt của vế nào.

## 7. Dữ liệu đã thay đổi trên môi trường (bắt buộc khai)

| Đổi gì | Bản ghi nào | Env | Lúc |
|---|---|---|---|
| Ghi số liệu vào báo cáo đang lập: thêm 11 khóa tự tính + `kpHoatDongKhac = 40000000` + ghi chú `QA-F8-341-20260807-1300`; **cố ý không ghi `kpXaHoiHoa`** | Báo cáo `f445b699-04bd-4c94-ab77-9ca118c78dd0` của **Sở Tư pháp An Giang** trong đợt `DOT-SO_BO_6_THANG-2026-1` (`a61e07f1…`) | `18.143.165.120.nip.io` (nội bộ) | 12:58 |

- Đây là **dựng tiền đề bằng giao diện** (nút [Lưu nháp]), **không** ghi thẳng CSDL, **không** đoán đường dẫn.
- **Không** đụng dữ liệu đối tác. **Không** đụng đợt `DOT-THBC01-UAT` (tiền đề của 3 phiếu `THBCTHCT_*`).
- Báo cáo vẫn ở `DU_THAO` / đơn vị vẫn `DANG_LAP` ⇒ **tiền đề không bị tiêu hủy**, phiếu này đo lại được.

## 8. Ảnh bằng chứng (đã mở lại xem từng ảnh trước khi dùng)

| Ảnh | Chứng minh điều gì | Link Drive |
|---|---|---|
| `TPDBCKQTHCT_02-01-tien-de-chi-tieu-13-de-trong.png` | Tiền đề C1: chỉ tiêu 13 để TRỐNG trong dữ liệu **đã lưu** (chụp sau khi tải lại trang), chỉ tiêu 12 = 40000000 + ghi chú mốc-giờ | https://drive.google.com/file/d/1OPCSjZpBVBKNrI_93PQTeu6Zioq8togv/view?usp=drivesdk |
| `TPDBCKQTHCT_02-02-sau-khi-bi-chan-van-dang-lap.png` | C1: ngay sau khi bấm [Đồng ý] thao tác bị chặn; thanh tiến trình vẫn ở bước 2 "Đang lập BC"; hộp xác nhận còn mở (candidate §6) | https://drive.google.com/file/d/1lpmUNNvzda78DvYl8IC9nDYmyp3TtMYi/view?usp=drivesdk |
| `TPDBCKQTHCT_02-03-trang-thai-giu-nguyen-dang-lap-bc.png` | C1: sau khi đóng hộp xác nhận, thanh tiến trình bước 2 "Đang lập BC", ô Trạng thái "Đang lập báo cáo" — **không đổi** | https://drive.google.com/file/d/1MpBJjfrdpSE0iYHzgechpHHj5lZEkgPz/view?usp=drivesdk |

> Không lặp lại thao tác để chụp lại thông báo thoáng qua (flow 04 §Chạy mục 7). Bằng chứng cho câu chữ là
> **chữ đã bắt bằng `innerText`** + **phản hồi máy chủ** của chính lượt bấm đó, ghi nguyên văn ở §3 C2.

## 9. Cổng chốt verdict — trả lời đủ 5 câu (flow 04)

1. **Neo đặc tả:** C1 → `srs-fr-15-ct-htpldn.md:830` (+ `:825`, `:802`); C2 → `:825`. Đã tự mở file đếm lại hôm nay.
2. **Mọi thao tác ánh xạ về vế:** dựng TĐ-A (tiền đề C1) · bấm [Trình duyệt KQ]+[Đồng ý] (C1) · bộ bắt thông báo (C2) · đọc lại bản ghi (đối chứng C1) · phản hồi máy chủ (đối chứng C2). Không thao tác nào ngoài phạm vi.
3. **Vế `DIFF/GAP`:** phiếu này **không có** vế nào — nên không phải chặn Pass.
4. **Đã đọc đầy đủ phiếu:** đọc lại trọn dòng 341 trên bảng lúc 12:56 (§0), gồm cả ô `DEV phản hồi lần 1`.
5. **Điều kiện đo khớp phiếu:** vai trò CB Nghiệp vụ đơn vị nộp (ĐP) · trạng thái "Báo cáo chưa đầy đủ" đúng nghĩa `:802` · thao tác đúng bước 3 của phiếu. Phiếu ghi nhãn nút *"Trình phê duyệt"*, giao diện là **[Trình duyệt KQ]** — phiếu **không nhắc nhãn nút** ⇒ không FAIL vì nhãn (bẫy §4.1 mục 1).
