# Nhật ký đo — CNDSMLTVV_01 (dòng 37) · R3 2026-08-07

## ✅ TRẠNG THÁI: **ĐÃ ĐO XONG** — verdict đề xuất: 🔁 **Reopen** (triệu chứng ĐÃ ĐỔI)

**Đo lúc:** 2026-08-07 00:46 → 01:03 giờ VN (06/08 17:46 → 18:03 GMT).
**Tài khoản thực dùng:** `cbnv_tw_02` / `Test@1234` — CB_NV_TW, cấp TW, đơn vị *Cục Bổ trợ tư pháp - Bộ Tư pháp*
(xác nhận qua `/api/v1/auth/me`: `vaiTro:["CB_NV_TW"]`, `donViId 00000000-0000-4000-8000-000000000001`,
`capDonVi:"TW"`, có quyền `publish_tu_van_vien`). **Không dùng `admin`, không đổi vai trò/cấp/đơn vị.**

---

## 1. BƯỚC 0 — vân tay bản dựng: **KHÁC vân tay agent trước → env ĐÃ DEPLOY TIẾP**

| Hạng mục | Đo được 2026-08-07 00:45 VN (lượt này) | Agent trước đo 00:1x 07/08 | 06/08 (lượt Reopen) |
|---|---|---|---|
| Phiên bản chân sidebar | **`HTPLDN · V1.0.10`** | `V1.0.9` | `V1.0.8` |
| Bó mã FE | **`assets/index-B2W2Krcs.js`** | `index-CxS5qW_0.js` | `index-DIABnbIr.js` |
| `GET /` `last-modified` | **`Thu, 06 Aug 2026 17:39:54 GMT`** (00:39:54 VN 07/08) | `12:48:25 GMT` | `07:13:15 GMT` |
| `GET /` `etag` | **`W/"6a74c6ea-428"`** | `W/"6a748299-428"` | `W/"6a74340b-428"` |

➡️ **Env vừa deploy tiếp lần nữa** (V1.0.9 → V1.0.10, lên lúc 00:39 VN 07/08, tức chỉ ~20 phút trước lượt đo này).
Mọi số liệu dưới đây **chỉ có hiệu lực cho `V1.0.10` / `index-B2W2Krcs.js`**.

---

## 2. Tiền đề — 3 biến thể (đọc lại qua máy chủ đầu phiên, KHÁC bàn giao cũ)

Endpoint thật là **`/api/v1/tu-van-viens`** (số nhiều). *(`/api/v1/tu-van-vien` số ít là route tích hợp,
trả 401 `ERR-AUTH-MTLS-01` — không liên quan case này.)*

Tab **Đang hoạt động** đầu phiên có **6 dòng**; toàn bộ 43 hồ sơ TVV đã quét để tìm tiền đề.

| Biến thể | Bản ghi | Loại | Số thẻ hành nghề | Cờ công khai đầu phiên | Đơn vị | Xử lý |
|---|---|---|---|---|---|---|
| **V1** Chuyên gia | `CG-QLND38-UAT` (`38383838-…-038`) | CG | — | false | Cục Bổ trợ tư pháp | ✅ dùng ngay |
| **V2** TVV **có** số thẻ | 🔴 **`TVV-BTP-TW-0016`** (`aaaa1707-…-0d01`) | TVV | `THN-TW-2026-016` | false | Cục Bổ trợ tư pháp | 🔧 **QA tự dựng** (xem §3) |
| **V3** TVV **không** số thẻ | `TVV-SEED-0001` (`5eed0003-…-001`) | TVV | **null** | false | Cục Bổ trợ tư pháp | ✅ dùng ngay — **biến thể quyết định** |

**Không đụng:** `TVV-BTP-TW-0002` · `DDD-TVV-021` (đang công khai, bản ghi người khác giữ) ·
`DDD-TVV-022` (không cần dùng).

### 2.1 Câu hỏi khác đơn vị — `TVV-STP-AG-0001` (đã kiểm thực nghiệm, KHÔNG log bug)

`cbnv_tw_02` **NHÌN THẤY và TÍCH CHỌN ĐƯỢC** `TVV-STP-AG-0001` (đơn vị *Sở Tư pháp An Giang*,
`00000000-0000-4000-8002-000000000006`): bản ghi nằm ngay trong tab Đang hoạt động, ô chọn **có mặt và
`disabled = false`** (kiểm bằng DOM trên cả 6/6 dòng). ⇒ **KHÔNG bị chặn vì khác đơn vị.**

Đây **không phải lỗi và không log**: tài khoản đo ở **cấp TW**, phạm vi dữ liệu đọc được trên màn Tổng quan
là *"Phạm vi: Toàn quốc"*; `srs-fr-04-chuyen-gia-tvv.md:1420` (*"Cán bộ Nghiệp vụ: thêm/sửa/xóa, xuất Excel,
công khai (TVV thuộc đơn vị)"*) không nói rõ cấp TW bao phủ tới đâu ⇒ **đặc tả im lặng, không đủ căn cứ.**

**Vẫn KHÔNG dùng `TVV-STP-AG-0001` làm V2** vì đầu phiên nó đang ở trạng thái **Công khai**
(`moTaCongKhai = "Kiem thu v1.0.9 tren 120"`, `thoiGianDangTai = 2026-08-06T13:04:32.751Z` — dữ liệu dev để lại),
không thoả yêu cầu *"Chưa công khai"* của V2, và gỡ nó ra sẽ ghi đè dấu vết của dev.

---

## 3. Tiền đề V2 — QA tự dựng, đường đi và mức hoàn nguyên

**Trong đơn vị Cục Bổ trợ tư pháp KHÔNG có sẵn hồ sơ nào loại *Tư vấn viên* + Đang hoạt động + Chưa công khai**
(quét 43/43 hồ sơ: nhóm Đang hoạt động của đơn vị chỉ có `CG-QLND38-UAT` và `TVV-BTP-TW-0002`, đều loại Chuyên gia).

**Đã dựng:** `TVV-BTP-TW-0016` — hồ sơ QA cũ, loại *Tư vấn viên*, **sẵn có** số thẻ `THN-TW-2026-016`,
đang ở *Chờ kích hoạt tài khoản* → đẩy lên *Đang hoạt động* bằng `POST /tu-van-viens/{id}/cap-nhat-trang-thai`.

- Đường trực tiếp `CHO_KICH_HOAT → HOAT_DONG` **bị máy trạng thái chặn** (422 `ERR-STATE-IV-TT-01`).
- Đi vòng **`CHO_KICH_HOAT → TAM_DUNG → HOAT_DONG`** (2 bước, đều 200).
- **KHÔNG sửa gì khác** trên hồ sơ: không đổi loại, không đổi số thẻ, không đụng V1/V3.

**Hoàn nguyên (§8):** cờ công khai đã trả về `false`, thời gian đăng tải đã rỗng. **Trạng thái KHÔNG trả về
`CHO_KICH_HOAT` được** — máy trạng thái một chiều, cả `HOAT_DONG → CHO_KICH_HOAT` lẫn `TAM_DUNG → CHO_KICH_HOAT`
đều 422. Đã để lại ở **`HOAT_DONG`** (hữu ích làm tiền đề V2 cho các vòng sau). **Khai rõ để điều phối biết.**

---

## 4. Các lượt đo — số liệu thô

Bộ bắt thông báo dùng `output/UAT_doi-tac/tools/toast-capture.js`. **Mỗi lượt đều tự kiểm trước khi bấm:
`soObserverDangSong = 1`** (4/4 lượt hợp lệ). Không lọc trùng, đọc bằng `innerText`, đếm request song song.

| Lượt | Tập chọn | Câu xác nhận trong cửa sổ | SO_REQUEST | SO_KHUNG_THONG_BAO | Nguyên văn thông báo | Thực tế sau **tải lại trang** |
|---|---|---|---|---|---|---|
| **L1** | riêng **V3** (1 dòng) | *"Công khai **1** tư vấn viên đã chọn lên Cổng pháp luật quốc gia?"* | 1 | 1 | *"Đã công khai tư vấn viên thành công"* | 🔴 **0/1** công khai |
| **L2** | **V2 + V3** (2 dòng) | *"Công khai **2** tư vấn viên đã chọn…"* | 1 | 1 | *"Đã công khai tư vấn viên thành công"* | 🔴 **1/2** công khai |
| **L3** | riêng **V1** (1 dòng) | *"Công khai **1** tư vấn viên đã chọn…"* | 1 | 1 | *"Đã công khai tư vấn viên thành công"* | ✅ **1/1** công khai |
| **L4** | riêng **V2** (1 dòng) | *"Công khai **1** tư vấn viên đã chọn…"* | 1 | 1 | *"Đã công khai tư vấn viên thành công"* | ✅ **1/1** công khai |
| (phụ) | riêng **V2** — [Hủy công khai] | *"1 tư vấn viên đã chọn sẽ bị gỡ khỏi Cổng…"* | 1 | 1 | *"Đã hủy công khai tư vấn viên thành công"* | ✅ gỡ đúng |

**Không lượt nào bị lặp thông báo** (`BI_LAP = false`, `SO_KHUNG = 1` mọi lượt) — 1 request ↔ 1 thông báo.

**Độ phủ: N = 3 bản ghi × M = 3 dạng** (Chuyên gia · TVV **có** số thẻ · TVV **không** số thẻ)
**× 2 cỡ lô** (1 dòng và 2 dòng) = **4 lượt bấm công khai thật** + 1 lượt hủy công khai. **Không còn GAP biến thể.**

---

## 5. Đường đo thứ hai — đọc TỪNG phần tử `data.results[]` của chính lượt bấm

Cả 4 lượt vỏ ngoài đều `HTTP 200` + `success: true`. Bên trong:

**L1** — `POST /api/v1/tu-van-viens/batch-cong-khai`, `ids:["5eed0003-…-001"]`:
```json
{"success":true,"data":{"results":[
  {"id":"5eed0003-0000-4000-8000-000000000001","success":false,
   "error":"Tư vấn viên chưa có Số thẻ hành nghề nên chưa thể công khai. Vui lòng bổ sung Số thẻ hành nghề trước."}
]},"meta":null}
```
⇒ **1/1 phần tử `success:false`. Giao diện vẫn báo "Đã công khai … thành công".**

**L2** — `ids:["aaaa1707-…-0d01","5eed0003-…-001"]`:
```json
{"success":true,"data":{"results":[
  {"id":"aaaa1707-0000-4000-8000-000000000d01","success":true,"laCongKhai":true},
  {"id":"5eed0003-0000-4000-8000-000000000001","success":false,
   "error":"Tư vấn viên chưa có Số thẻ hành nghề nên chưa thể công khai. Vui lòng bổ sung Số thẻ hành nghề trước."}
]},"meta":null}
```
⇒ **1 true + 1 false. Giao diện vẫn báo một câu thành công duy nhất, không nhắc hồ sơ thất bại.**

**L3** — `ids:["38383838-…-038"]` → `[{"success":true,"laCongKhai":true}]` ⇒ khớp thực tế.

**Đọc lại bản ghi qua máy chủ sau khi tải lại trang** (`GET /api/v1/tu-van-viens/{id}`):

| Bản ghi | `laCongKhai` | `moTaCongKhai` | `thoiGianDangTai` | `version` |
|---|---|---|---|---|
| V2 sau L2 | `true` | `"R3-07-08 L2 lo 2 ho so V2 TVV-BTP-TW-0016 co so the + V3 TVV-SEED-0001 khong so the"` (đúng nguyên văn vừa nhập) | `2026-08-06T17:55:13.196Z` = **00:55:13 VN 07/08**, bám đúng thời điểm bấm | 5 → 6 |
| V3 sau L1 **và** sau L2 | `false` | **giữ nguyên chuỗi cũ** `"QA re-verify OOS02/OOS01 - 04/08/2026 …"` | `null` | **22 (không đổi)** |
| V1 sau L3 | `true` | `"R3-07-08 L3 rieng V1 CG-QLND38-UAT loai Chuyen gia doi chung"` | `2026-08-06T17:57:27.106Z` | 8 → 9 |

**Đối chứng mô tả (mỗi lượt một chuỗi riêng có mốc giờ):** V2 sau L4 mang chuỗi **L4**, không phải chuỗi L2
⇒ dữ liệu là của lượt bấm mới, **không phải bản cũ chưa cập nhật**.

**⚠️ Kiểm thêm theo yêu cầu khối chuẩn — lượt bấm hỏng KHÔNG ghi đè mô tả công khai cũ:** ✅ đạt.
V3 qua 2 lượt hỏng vẫn giữ nguyên `moTaCongKhai` cũ và `version` **không nhích** (22 → 22).

**Màn chi tiết V2 (tab "Hồ sơ", nhóm "Thông tin công khai" — `:1564`):** hiện đủ
*Mô tả công khai* = đúng chuỗi vừa nhập · *File đính kèm công khai* = — · *Thời gian đăng tải* = **07/08/2026**.
**Không bị văng `/403`** — cảnh báo chéo từ case 36 không chạm case này (hồ sơ V2 không có tệp đính kèm).

---

## 6. Bảng đối chiếu 5 dòng điều kiện của khối đã khóa

| # | Điều kiện (nguyên văn khối `✅ PASS khi` / `❌ FAIL nếu`) | Đo được | Kết luận | GAP |
|---|---|---|---|---|
| (a) | *"với hồ sơ không đủ điều kiện, hệ thống báo TỪ CHỐI rõ hồ sơ nào không đạt và vì sao (KHÔNG được báo thành công)"* | L1: 0/1 công khai nhưng thông báo là *"Đã công khai tư vấn viên thành công"*. L2: 1/2 nhưng cũng chỉ một câu thành công, **không nêu hồ sơ nào trượt, không nêu lý do**. Máy chủ **có** trả lý do rõ trong `results[]` nhưng giao diện bỏ qua | 🔴 **KHÔNG ĐẠT** | không |
| (b) | *"với lô có lẫn hồ sơ hỏng, những hồ sơ hợp lệ còn lại vẫn phải được công khai đủ (hoặc chặn cả lô nhưng NÓI RÕ)"* | L2: V2 (hợp lệ) **vẫn được công khai đủ** dù V3 cùng lô bị từ chối. Nhánh 1 của điều kiện thoả | ✅ **ĐẠT — đã fix so với 06/08** | không |
| (c) | *"mọi hồ sơ báo thành công đều đủ 4 kết cục sau khi tải lại: mô tả đúng nguyên văn · cờ công khai bật · nhóm Thông tin công khai hiện ra · thời gian đăng tải bám đúng thời điểm bấm"* | Với hồ sơ máy chủ báo `success:true` (V1, V2): đủ **4/4 kết cục**, đã đọc cả trên màn chi tiết lẫn qua máy chủ | ✅ **ĐẠT** | không |
| (d) | *"số hồ sơ chuyển sang Công khai sau khi tải lại đúng bằng số hồ sơ mà thông báo nói là đã công khai"* | Thông báo **không nêu con số nào**, chỉ khẳng định trống *"Đã công khai tư vấn viên thành công"* trong khi L1 = 0 hồ sơ đổi, L2 = 1/2 | 🔴 **KHÔNG ĐẠT** | không |
| ❌ | *"báo thành công mà tải lại trang hồ sơ vẫn Chưa công khai — kể cả khi chỉ sai 1 hồ sơ trên 2; … hoặc người dùng không biết hồ sơ nào không đạt và vì sao"* | **Trúng 2 vế**: L1 (0/1) và L2 (1/2) đều báo thành công; người dùng không được cho biết hồ sơ nào trượt và vì sao | 🔴 **KÍCH HOẠT FAIL** | không |

**⇒ Verdict đề xuất: 🔁 Reopen.** (a) và (d) không đạt, vế ❌ FAIL bị kích hoạt.

### 6.1 Triệu chứng ĐÃ ĐỔI so với vòng 06/08 — dev có sửa thật, nhưng chưa hết

| Vế | 06/08 (V1.0.8) | 07/08 (V1.0.10) |
|---|---|---|
| Cửa sổ nhập mô tả | ✅ đã đúng từ 06/08 | ✅ vẫn đúng |
| **Nguyên tử của lô** — 1 hồ sơ hỏng kéo đổ cả lô | 🔴 0/2 công khai | ✅ **ĐÃ FIX** — 1/2, hồ sơ hợp lệ đi qua |
| **Nội dung lỗi máy chủ trả về** | 🔴 lộ nguyên văn ràng buộc CSDL `CHK_tu_van_vien_tvv_so_the_hanh_nghe` | ✅ **ĐÃ FIX** — câu nghiệp vụ đọc được: *"Tư vấn viên chưa có Số thẻ hành nghề nên chưa thể công khai…"* |
| **Giao diện báo kết quả** | 🔴 báo thành công sai | 🔴 **CÒN NGUYÊN** — vẫn báo thành công dù `results[]` có hồ sơ trượt |

⇒ Phần còn lại **nằm ở lớp giao diện**: máy chủ đã nói đủ, giao diện không đọc `results[]`.

### 6.2 Điều KHÔNG được log ngược (đã kiểm, ghi để dev không sửa nhầm chỗ)

Máy chủ **từ chối công khai V3 là ĐÚNG ĐẶC TẢ** — `srs-fr-04-chuyen-gia-tvv.md:1507`
(*"Số thẻ hành nghề | ô văn bản | **Bắt buộc nếu Loại = Tư vấn viên** (theo NĐ 77/2008 Đ.20)"*).
**Không được đòi hệ thống công khai được hồ sơ Tư vấn viên thiếu số thẻ.** Lỗi nằm ở chỗ **báo thành công
sai sự thật** và **không cho người dùng biết hồ sơ nào không đạt / vì sao**.

Các nhánh ngược đã đo để **không chấm oan**: cửa sổ nhập mở đúng 4/4 lượt · câu xác nhận phản ánh đúng tập
dòng đã chọn (1 và 2) · các tab khác *Đang hoạt động* không có nút công khai hàng loạt — đúng `:1464`.

---

## 7. Ảnh — tên ↔ nội dung đã mở đọc lại, khớp

Thư mục `output/UAT_doi-tac/batch-B7-tuvan-mangluoi-2026-08-06/image/`.

| Tệp | Mở ra thấy gì |
|---|---|
| `CNDSMLTVV_01-R3-03-luot2-lo-2-ho-so-thong-bao.png` | 🔴 **Ảnh quyết định.** Thông báo xanh *"Đã công khai tư vấn viên thành công"* ngay sau lượt L2 (lô 2 hồ sơ) — lượt mà thực tế chỉ 1/2 hồ sơ được công khai. Chân sidebar ghi `HTPLDN · V1.0.10` |
| `CNDSMLTVV_01-R3-08-ma-tvv-va-cot-cong-khai-day-du.png` | 🔴 **Ảnh quyết định.** Bảng đủ cả cột **Mã TVV** lẫn cột **Công khai**: `CG-QLND38-UAT` Công khai · `TVV-BTP-TW-0016` Công khai · **`TVV-SEED-0001` Chưa công khai** (dù đã bị bấm công khai 2 lượt) |
| `CNDSMLTVV_01-R3-05-V2-chi-tiet-nhom-thong-tin-cong-khai.png` | Màn chi tiết `TVV-BTP-TW-0016`: *Loại = Tư vấn viên*, *Đơn vị quản lý = Cục Bổ trợ tư pháp - Bộ Tư pháp*, *Số thẻ hành nghề = THN-TW-2026-016*; nhóm **Thông tin công khai** đủ mô tả đúng nguyên văn + *Thời gian đăng tải 07/08/2026* ⇒ chứng minh điều kiện (c) |
| `CNDSMLTVV_01-R3-01-luot1-rieng-V3-ngay-sau-bam-modal-da-dong.png` | Danh sách ngay sau lượt L1, cửa sổ đã đóng (**không bắt kịp thông báo** — tên tệp đã sửa lại cho khớp nội dung) |

> 4 ảnh chụp giữa chừng không thể hiện được điều mà tên tệp khẳng định (thiếu cột *Công khai* trong khung nhìn)
> đã **xoá bỏ** thay vì để tên sai lệch.

---

## 8. Đã seed gì · đã hoàn nguyên gì

| Bản ghi | Trước lượt đo | Đã làm | Sau khi hoàn nguyên | Còn lệch? |
|---|---|---|---|---|
| `CG-QLND38-UAT` (V1) | HOAT_DONG · ck=false | công khai (L3) → [Hủy công khai] | HOAT_DONG · **ck=false** · `thoiGianDangTai=null` | mô tả công khai còn lưu chuỗi L3 — **đúng `:1406`, không phải lỗi** |
| `TVV-BTP-TW-0016` (V2) | **CHO_KICH_HOAT** · ck=false | đẩy lên HOAT_DONG (qua TAM_DUNG) · công khai L2 & L4 · [Hủy công khai] ×2 | **HOAT_DONG** · **ck=false** · `thoiGianDangTai=null` | 🔴 **trạng thái KHÔNG về lại `CHO_KICH_HOAT` được** (máy trạng thái một chiều, 422 cả 2 đường) |
| `TVV-SEED-0001` (V3) | HOAT_DONG · ck=false | bị bấm công khai 2 lượt, **máy chủ từ chối cả 2** | HOAT_DONG · ck=false · `version` **22 không đổi** | **không lệch gì** |
| `TVV-STP-AG-0001` · `TVV-BTP-TW-0002` · `DDD-TVV-021` · `DDD-TVV-022` | — | **không đụng tới** | nguyên trạng | không |

---

## 9. Hai câu bắt buộc

**1. Fix này có làm hỏng gì khác trong cùng luồng không?** → **Không.**
Cùng luồng đã đo lại: cửa sổ nhập mô tả vẫn mở đúng (4/4) · câu xác nhận vẫn phản ánh đúng số dòng đã chọn
(1 và 2) · nút **[Hủy công khai]** vẫn chạy đúng (gỡ cờ, xoá thời gian đăng tải, giữ lại mô tả theo `:1406`) ·
hồ sơ hợp lệ vẫn ra đủ 4 kết cục · lượt bấm hỏng **không** ghi đè mô tả công khai cũ, **không** nhích `version`.
Không thấy lặp thông báo, không thấy gửi trùng request (1 request ↔ 1 thông báo ở cả 5 lượt).

**2. Ngoài phạm vi bug, có thấy gì bất thường không?** → **Không có bug mới nào qua được cổng.** 2 ghi nhận:

- **(candidate, KHÔNG dùng làm căn cứ verdict)** Câu thông báo thành công *"Đã công khai tư vấn viên thành công"*
  thiếu mã/tên đối tượng so với mẫu chuẩn `srs-v3.5.md:6772` (*"Đã công khai {ten_doi_tuong} '{ma_hoac_ten}'
  lên Cổng Pháp luật Quốc gia."*). Đối tác **không nêu** vế này; giữ nguyên mức candidate như các vòng trước.
- **(không log)** `cbnv_tw_02` cấp TW tích chọn được hồ sơ của *Sở Tư pháp An Giang* — đặc tả `:1420` **im lặng**
  về phạm vi của cấp TW, màn Tổng quan lại ghi *"Phạm vi: Toàn quốc"* ⇒ **không đủ căn cứ, không log** (§2.1).

---

## 10. Cảnh báo cho điều phối

1. 🔴 **Bản dựng đã nhảy tiếp sang `V1.0.10`** (`index-B2W2Krcs.js`, 00:39 VN 07/08) — khác cả vân tay agent
   trước ghi lúc 00:1x. Nếu có vòng đo tiếp thì **phải đo lại vân tay đầu phiên**, env đang deploy liên tục.
2. 🔴 Số dòng `srs-v3.5.md` trong hồ sơ cũ của case này **lệch +44**: dùng `5729` (BR-PUBLIC-01) · `5741`
   (BR-PUBLIC-03) · `6766` (mô hình KÉO) · `6772` (mẫu thông báo công khai) · `6773` (mẫu hủy công khai).
   Số dòng `srs-fr-04-chuyen-gia-tvv.md` **không lệch** — đã tự mở đếm lại 13/13 dòng trích trong lượt này.
3. Tiền đề **V2 giờ đã tồn tại sẵn** cho các vòng sau: `TVV-BTP-TW-0016` — TVV, có số thẻ `THN-TW-2026-016`,
   Đang hoạt động, Chưa công khai, cùng đơn vị Cục Bổ trợ tư pháp. **Không cần dựng lại.**
4. Trạng thái `TVV-BTP-TW-0016` **không hoàn nguyên được về `CHO_KICH_HOAT`** — nếu vòng nào cần hồ sơ ở
   *Chờ kích hoạt tài khoản* thì phải dùng bản ghi khác (còn 6 hồ sơ khác trong tab đó).
