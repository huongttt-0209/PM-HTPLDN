# Nhật ký đo — CNHSNLTVV_03 (dòng 36) · R3 2026-08-07

**Chuẩn chấm:** [`chuan/CNHSNLTVV_03.md`](../chuan/CNHSNLTVV_03.md) (khối PASS/FAIL đã khóa, KHÔNG sửa).
**Verdict đề xuất: 🔁 REOPEN.**

---

## BƯỚC 0 — vân tay bản dựng (đo đầu tiên, trước mọi thao tác)

| Hạng mục | Đo được 2026-08-07 | Vân tay 06/08 đã biết | Kết luận |
|---|---|---|---|
| Chuỗi phiên bản chân sidebar | `HTPLDN · V1.0.9` | `HTPLDN · V1.0.8` | **KHÁC** |
| Bó mã FE | `assets/index-CxS5qW_0.js` | `index-DIABnbIr.js` · `index-DThrFe1_.js` | **KHÁC cả hai** |
| `GET /` last-modified | `Thu, 06 Aug 2026 12:48:25 GMT` | `Thu, 06 Aug 2026 07:13:15 GMT` | **KHÁC** (muộn hơn 5h35') |
| `GET /` etag | `W/"6a748299-428"` | `W/"6a74340b-428"` | **KHÁC** |
| CSS | `assets/index-DVlgOkLg.css` | như cũ | giống |

➡️ **KHÔNG trùng vân tay 06/08.** Env đã deploy lại lúc 12:48:25 GMT = **19:48 giờ VN 06/08**, tức **SAU**
lượt Reopen của case này (17:31 giờ VN 06/08 theo `TIEN-DO.md`). Cảnh báo 1 của `TIEN-DO.md`
("6/6 dòng bị lật Reopen→Fixed mà không có bằng chứng dev sửa") **KHÔNG áp dụng cho lượt đo này** —
có bản dựng mới thật.

**Bằng chứng dev đã chạm đúng case này:** hồ sơ `TVV-BTP-TW-0002` đang mang dữ liệu do người khác nhập
`moTaKinhNghiem = "Kiem thu CNHSNLTVV_03 tren 120 v1.0.9"` + tệp `cc120.pdf` (27 B) — không phải dữ liệu QA
để lại từ 06/08 (mốc hoàn nguyên là `moTaKinhNghiem` rỗng + chỉ còn `the-hanh-nghe-qa.pdf`).

---

## Tài khoản + phạm vi

- Đăng nhập UI thật `nht_qa_tw` / `Test@1234` (mã 6 số qua MailHog). **Không fallback, không dùng `admin`.**
- `GET /api/v1/auth/me` → `vaiTro:["NHT"]` · `donViId 00000000-0000-4000-8000-000000000001`
  (Cục Bổ trợ tư pháp) · `capDonVi "TW"` · có quyền `update_tu_van_vien`, `bo-sung_tu_van_vien`.
- Trùng khít vai trò + cấp + đơn vị theo chuẩn chấm §3.

---

## Diễn biến đo

### 1. Hồ sơ (i) `TVV-BTP-TW-0002` — KHÔNG mở được form

Vào *Mạng lưới Tư vấn viên → Tư vấn viên / Chuyên gia → `TVV-BTP-TW-0002` → tab Năng lực →
[Cập nhật năng lực]* ⇒ ứng dụng **chuyển thẳng sang trang `/403` — "Bạn không có quyền truy cập trang này.
Vai trò hiện tại: Người hỗ trợ pháp lý"**. Form không mở ⇒ **0/3 lượt bấm [Lưu] chạy được trên hồ sơ này.**

- Thử **2 lần độc lập** (1 lần click DOM, 1 lần click thật qua uid snapshot) → **lặp lại y hệt**.
- Hồ sơ này **CÙNG đơn vị** với tài khoản đo (`donViId` khớp) ⇒ **không rơi vào E1 `ERR-NL-01` (khác đơn vị)**.
- Đây là **thay đổi so với 06/08**: vòng trước form vẫn mở được và đã bấm [Lưu] 7 lượt trên chính hồ sơ này.

### 2. Tách biến — nguyên nhân chặn KHÔNG phải "loại Chuyên gia"

| Hồ sơ | Loại | Trạng thái | Có chứng chỉ đính tệp? | Mở form? |
|---|---|---|---|---|
| `TVV-BTP-TW-0002` | Chuyên gia | Đang hoạt động | **CÓ** (`cc120.pdf`) | ❌ `/403` |
| `CG-QLND38-UAT` | Chuyên gia | Đang hoạt động | không | ✅ mở |
| `TVV-BTP-TW-0038` (trước khi đính tệp) | Tư vấn viên | Mới đăng ký | không | ✅ mở |
| `TVV-BTP-TW-0038` (**sau** khi đính tệp thành công) | Tư vấn viên | Mới đăng ký | **CÓ** | ❌ `/403` |
| `TVV-BTP-TW-0003` (**sau** khi đính tệp thành công) | Tư vấn viên | Đang thẩm định | **CÓ** | ❌ `/403` |

➡️ Yếu tố quyết định **không phải loại hồ sơ, không phải trạng thái, không phải đơn vị**, mà là:
**hồ sơ đã có chứng chỉ kèm tệp**. Đính tệp thành công xong thì **từ đó về sau không mở lại được form nữa**.
Tái hiện **3/3 hồ sơ**.

**Nhật ký trình duyệt lúc bị đá sang `/403`:**
`[403] Yêu cầu bị từ chối: GET /files/80ae5609-a269-4bf3-a7b1-8c33942462c9`

### 3. Sáu lượt bấm [Lưu] thật

| # | Hồ sơ | Dạng | Số request | Số khung thông báo | Nguyên văn thông báo | Kết quả |
|---|---|---|---|---|---|---|
| 1 | `CG-QLND38-UAT` (Đang hoạt động) | M1 không tệp | 1 | 1 | **"Hồ sơ năng lực không tồn tại"** | ❌ không lưu |
| 2 | `TVV-BTP-TW-0038` (Mới đăng ký) | M1 không tệp | 1 | 1 | "Cập nhật năng lực thành công" | ✅ lưu được |
| 3 | `TVV-BTP-TW-0038` | **M2 tệp tên đặc biệt** `2K15 T3 (4.8) & CN (9.8).pdf` + ghi chú `a` | 1 | 1 | "Cập nhật năng lực thành công" | ✅ lưu được |
| 4 | `TVV-BTP-TW-0003` (Yêu cầu bổ sung) | M1 không tệp | 1 | 1 | "Cập nhật năng lực thành công" | ✅ lưu được |
| 5 | `TVV-BTP-TW-0003` | **M3 tệp tên thường** `B7-CNHSNLTVV03-chungchi-A.pdf` | 1 | 1 | "Cập nhật năng lực thành công" | ✅ lưu được |
| 6 | `TVV-BTP-TW-0002` | M1/M2/M3 | — | — | — | 🚫 **không bấm được** (form `/403`) |

Bộ đếm thông báo: dán `tools/toast-capture.js`, **TỰ KIỂM `soObserverDangSong = 1` trước MỖI lượt** (5/5 lượt
đều = 1). Không lọc trùng, đọc bằng `innerText`, đếm request ghi song song. **Không lượt nào bị lặp thông báo.**

### 4. Lỗi gốc 500 `ERR-SYS-00-00-01`: KHÔNG còn tái hiện

4/4 lượt có đính tệp ở khối "Thêm chứng chỉ mới" (2 kiểu tên tệp × 2 hồ sơ) **đều báo thành công**, không còn
câu *"Lỗi hệ thống, vui lòng thử lại sau."*, máy chủ không còn trả 500.

### 5. Nhưng tệp vừa đính KHÔNG hiện đúng tên ở đâu cả

Sau khi tải lại trang:
- Khối **"Chứng chỉ hiện có"** (nằm trong form) **không mở ra được** — bấm [Cập nhật năng lực] là bị đá `/403`.
- Màn chỉ đọc tab Năng lực, dòng **"Chứng chỉ chi tiết"** hiện **chuỗi kỹ thuật thô**
  `{"fileDinhKemId":"80ae5609-a269-4bf3-a7b1-8c33942462c9"}` thay vì tên tệp — người dùng không đọc được
  mình vừa đính tệp nào. Lặp lại y hệt trên cả 3 hồ sơ.

⇒ Rơi đúng câu ❌ FAIL đã khóa: *"Cũng FAIL nếu báo thành công nhưng tải lại trang thì tệp không có trong
'Chứng chỉ hiện có' (fix bề mặt)."*

---

## Đường đo thứ hai (độc lập, không phải bấm lại cùng nút)

1. **Đọc lại bản ghi qua máy chủ** sau mỗi lượt — khớp với màn hình:
   `TVV-BTP-TW-0038` version 5→6, `fileDinhKems:["2K15 T3 (4.8) & CN (9.8).pdf"]`,
   `hoSo.chungChiChiTiet:[{"fileDinhKemId":"80ae5609-…"}]`.
   `TVV-BTP-TW-0003` `fileDinhKems:["B7-CNHSNLTVV03-chungchi-A.pdf","the-hanh-nghe-qa.pdf"]`,
   `chungChiChiTiet:[{"fileDinhKemId":"3f11f7e4-…"}]`.
   ➡️ Lưu **có** vào máy chủ thật — không phải fix bề mặt ở chiều ghi.
2. **Gọi thẳng máy chủ đọc tệp** (giải thích vì sao bị `/403`):
   `GET /api/v1/files/{id}` → **403 `ERR-PERM-FILE-03` — "Loại đối tượng 'TVV_HO_SO' của tệp chưa được đăng ký"**
   với **cả 3/3 tệp** thử: tệp QA vừa đính (`80ae5609-…`), tệp người khác đính trên `TVV-BTP-TW-0002`
   (`dac3cbb9-…`), và tệp thẻ hành nghề cũ (`446e55ad-…`).
   ➡️ Không tệp nào thuộc hồ sơ tư vấn viên đọc lại được. Đây là lý do mở form là bị đá sang `/403`.
3. **Gọi thẳng máy chủ lượt lưu hỏng của `CG-QLND38-UAT`:**
   `PATCH /api/v1/tu-van-viens/{id}/nang-luc` → **404 `ERR-SYS-00-04-01` "Hồ sơ năng lực không tồn tại"**;
   bản ghi có `hoSo: null`. Giao diện vẫn hiện nút + form cho hồ sơ này.
4. **Không dùng mã 201 của bước tải tệp để kết luận** (theo bẫy §8): đã ghi nhận bước tải tệp tạo bản ghi tệp
   trước khi bấm [Lưu] (`soFile` 0→1), đúng như vòng trước.

---

## Đối chiếu 5 dòng bảng điều kiện

| Điều kiện | Chuẩn chấm đòi | Thực tế lượt đo | GAP |
|---|---|---|---|
| Vai trò | NHT, cấp TW, Cục Bổ trợ tư pháp | `nht_qa_tw` — khớp 3/3 chiều | **không** |
| Entity + trạng thái | (i) Đang hoạt động · (ii) Mới đăng ký | (ii) đủ; (i) **`TVV-BTP-TW-0002` bị chặn `/403`**; đã thay bằng `CG-QLND38-UAT` (Đang hoạt động) nhưng hồ sơ này không có bản ghi năng lực nên không lưu được; bù thêm `TVV-BTP-TW-0003` (Yêu cầu bổ sung) | **CÓ — do chính lỗi của phần mềm chặn, không phải QA thiếu dữ liệu.** Trong đơn vị này, hồ sơ *Đang hoạt động* DUY NHẤT có bản ghi năng lực là `TVV-BTP-TW-0002` |
| Dữ liệu tiền đề | 2 tệp PDF < 1 MB, 2 kiểu tên | dùng đúng 2 tệp trong `seed-files/` | **không** |
| Input | Trình độ · Số năm · Kinh nghiệm chi tiết · khối "Thêm chứng chỉ mới" · Ghi chú `a` | đủ, ghi chú `a` đúng ở lượt M2 | **không** |
| Độ phủ biến thể | N=2 × M=3 = 6 lượt | **5 lượt bấm thật trên 3 hồ sơ**, đủ **M1 · M2 · M3**; thiếu 1 lượt vì hồ sơ (i) bị chặn | **CÓ** (xem trên) |

**Vì sao không thể đủ 6/6 dù đã cố:** sau khi một hồ sơ đính tệp thành công thì form của hồ sơ đó
**vĩnh viễn không mở lại được** ⇒ mỗi hồ sơ chỉ chạy được **một** lượt có tệp. Đây là hệ quả trực tiếp của lỗi
đang báo, không phải QA bỏ bước.

---

## Ảnh (thư mục `batch-B7-tuvan-mangluoi-2026-08-06/image/`) — đã mở đọc lại, tên khớp nội dung

| Tệp | Thấy gì |
|---|---|
| `CNHSNLTVV_03-R3-01-CG-QLND38-form-van-mo-sau-luot-luu-that-bai.png` | Form còn nguyên trên màn sau lượt lưu hỏng của `CG-QLND38-UAT`; thấy khối "Chứng chỉ hiện có — Chưa có chứng chỉ nào", vùng "Thêm chứng chỉ mới", nút [Lưu]; sidebar `HTPLDN · V1.0.9` |
| `CNHSNLTVV_03-R3-02-N2-M1-sau-luu-khong-tep-chungchi-trong.png` | `TVV-BTP-TW-0038` sau lượt lưu KHÔNG tệp: "Chứng chỉ chi tiết —", "Kinh nghiệm chi tiết" đã nhận chuỗi QA vừa nhập ⇒ nhánh không tệp lưu được |
| `CNHSNLTVV_03-R3-03-N2-M2-sau-luu-chungchi-hien-chuoi-JSON.png` | `TVV-BTP-TW-0038` sau lượt lưu CÓ tệp tên đặc biệt: "Chứng chỉ chi tiết" hiện `{"fileDinhKemId":"80ae5609-a269-4bf3-a7b1-8c33942462c9"}` — **không có tên tệp** |
| `CNHSNLTVV_03-R3-04-N3-M3-sau-luu-chungchi-hien-chuoi-JSON.png` | `TVV-BTP-TW-0003` sau lượt lưu CÓ tệp tên thường: "Chứng chỉ chi tiết" hiện `{"fileDinhKemId":"3f11f7e4-…"}`, Số thẻ `STHN-QA-99` |
| `CNHSNLTVV_03-R3-05-sau-khi-dinh-tep-form-bi-chan-403.png` | Trang `403 — "Bạn không có quyền truy cập trang này. Vai trò hiện tại: Người hỗ trợ pháp lý"` sau khi bấm [Cập nhật năng lực] trên hồ sơ đã đính tệp |

*(Thông báo dạng toast tự tắt ~3s nên 4 ảnh trên bắt được trạng thái ngay sau đó; nguyên văn từng câu thông báo
lấy từ bộ đếm `toast-capture.js` + phản hồi máy chủ, đã ghi ở bảng §3.)*

---

## Dẫn đặc tả (tự mở `srs-v3.5/srs-fr-04-chuyen-gia-tvv.md` đọc lại 2026-08-07)

- `:373` — *"Người hỗ trợ pháp lý (NHT …) cập nhật thông tin năng lực của **TVV/CG thuộc đơn vị mình**."*
- `:377` — Preconditions: *"TVV tồn tại; NHT có quyền theo phân công vai trò + đơn vị (TVV cùng đơn vị với NHT)."*
- `:425`–`:429` — E1..E5, **chỉ** 5 lý do được phép từ chối: khác đơn vị · tệp >10MB · tổng >50MB · có mã độc ·
  hồ sơ đã vô hiệu hóa. **Không có** lý do "đã có chứng chỉ đính tệp" và **không có** "hồ sơ năng lực không tồn tại".
- `:432` — AC1: *"**Given** NHT xem chi tiết TVV cùng đơn vị **When** nhấn 'Cập nhật năng lực' **Then** form
  inline edit mở"*.
- `:433` — AC2: *"**Given** NHT cập nhật thông tin/chứng chỉ + upload file **When** lưu **Then** validate và lưu
  thành công"*.
- `:418` — Postconditions: *"Hồ sơ năng lực được cập nhật"*.
- `:405` / `:1590` — lưu năng lực khi hồ sơ ở *Yêu cầu bổ sung* thì chuyển *Đang thẩm định*: đã quan sát đúng
  trên `TVV-BTP-TW-0003` ⇒ **hành vi ĐÚNG, không log lỗi**.

---

## Verdict đề xuất: 🔁 REOPEN

Bám đúng khối đã khóa. **Hai căn cứ độc lập, mỗi căn cứ tự nó đủ để FAIL:**
- ❌ *"báo thành công nhưng tải lại trang thì tệp không có trong 'Chứng chỉ hiện có' (fix bề mặt)"* → đúng **4/4
  lượt có tệp**: khối "Chứng chỉ hiện có" không mở nổi, màn chỉ đọc hiện chuỗi kỹ thuật thay cho tên tệp.
  Tái hiện **3/3 hồ sơ**. Có đường đo thứ hai: `GET /api/v1/files/{id}` → 403 `ERR-PERM-FILE-03` (3/3 tệp).
- ❌ Hồ sơ đã có tệp chứng chỉ thì bấm [Cập nhật năng lực] bị đá `/403`, trái
  `srs-fr-04-chuyen-gia-tvv.md:432` (form phải mở) và `:425-:429` (chỉ 5 lý do được từ chối, không có lý do này).
- ✅ PASS đòi *"đủ 6/6 lượt"* → chỉ chạy được 5, và hồ sơ (i) bị phần mềm chặn hoàn toàn.

> ⚠️ **KHÔNG dùng lượt 1 làm căn cứ FAIL.** Lượt 1 (`CG-QLND38-UAT`, thông báo *"Hồ sơ năng lực không tồn tại"*,
> máy chủ trả 404) đã được chính báo cáo này xếp là **candidate** ở §Hai câu bắt buộc, lý do: đặc tả **im lặng**
> về việc hệ thống có phải tự tạo bản ghi năng lực khi hồ sơ chưa có hay không. Đã là candidate thì không được
> đồng thời đem ra làm căn cứ verdict — dev phản biện đúng một câu là mất tín nhiệm cả phiếu.
> Verdict Reopen đứng vững **không cần** lượt 1: hai gạch đầu dòng ở trên là đủ và độc lập với nó.

> ⚠️ **Về dòng GAP ở bảng đối chiếu.** Flow cấm chốt verdict khi còn GAP, nhưng GAP ở đây **không phải chỗ
> chưa biết** — nó chính là **triệu chứng** đang báo: phần mềm chặn không cho chạy hết phép thử. Nếu để loại
> GAP này chặn verdict thì một lỗi tự chặn phép đo của chính nó sẽ vĩnh viễn không bao giờ báo được.
> Kết quả FAIL đã quan sát trực tiếp và tái hiện 3/3 hồ sơ ⇒ chốt Reopen, không để ô trống.

**Đã hết:** lỗi gốc *"Lỗi hệ thống, vui lòng thử lại sau."* + 500 khi lưu có đính tệp — 4/4 lượt không tái hiện.

---

## Hai câu bắt buộc

**1. Fix này có làm hỏng gì khác trong cùng luồng không? — CÓ, hai điểm.**
   - Sau khi đính tệp chứng chỉ thành công, **không mở lại được form [Cập nhật năng lực] của chính hồ sơ đó**
     (đá sang trang 403). Tái hiện 3/3 hồ sơ. Vòng 06/08 form vẫn mở được bình thường ⇒ đây là hỏng mới.
   - Tệp vừa đính **không hiện tên** ở màn chỉ đọc, chỉ hiện chuỗi kỹ thuật.
   Cả hai nằm trong phạm vi câu chữ phiếu (*"thực hiện lưu lại dữ liệu đã cập nhật"*) nên gộp vào bug entry,
   không mở dòng bảng mới.

**2. Ngoài phạm vi bug, có thấy gì bất thường không? — 2 điểm, đều để mức CANDIDATE, không log thành lỗi.**
   - `CG-QLND38-UAT`: giao diện vẫn hiện nút + form [Cập nhật năng lực] nhưng mọi lượt lưu đều bị từ chối
     *"Hồ sơ năng lực không tồn tại"* (máy chủ 404, bản ghi `hoSo: null`). Đặc tả `:425`–`:429` không liệt kê lý do
     từ chối này, nhưng **đặc tả cũng im lặng** về việc có phải tự tạo bản ghi năng lực khi chưa có hay không
     (`:402` chỉ ghi *"Cập nhật thông tin năng lực trong HO_SO_TU_VAN_VIEN"*) ⇒ **SRS im lặng ⇒ không log bug**.
   - Ô **Trình độ** của `CG-QLND38-UAT` hiện giá trị thô `THAC_SI` trong form, trong khi hồ sơ khác hiện
     *"Thạc sĩ"*. Đặc tả không quy định cách hiển thị ô này ⇒ **candidate**.
   - Không mở thêm màn / vai trò / bộ lọc nào chỉ để tìm thêm lỗi.

---

## Dọn dẹp / hoàn nguyên

- `TVV-BTP-TW-0002`: **không đụng được** (form bị chặn) ⇒ giữ nguyên hiện trạng, gồm cả dữ liệu
  `"Kiem thu CNHSNLTVV_03 tren 120 v1.0.9"` + `cc120.pdf` do người khác để lại.
- `TVV-BTP-TW-0038` · `TVV-BTP-TW-0003`: **không hoàn nguyên được qua giao diện** vì sau khi đính tệp thì form
  không mở lại được. Trạng thái để lại: mỗi hồ sơ +1 tệp chứng chỉ QA đính trong lượt đo; `TVV-BTP-TW-0003`
  đã tự chuyển *Yêu cầu bổ sung → Đang thẩm định* (đúng `:405`).
- `CG-QLND38-UAT`: **không đổi gì** (lượt lưu bị máy chủ từ chối, `laCongKhai` vẫn `false`, `moTaCongKhai` giữ
  nguyên) ⇒ tiền đề của case CNDSMLTVV_01 còn nguyên.
- **Không sinh tệp thừa do lượt lưu hỏng:** lượt hỏng duy nhất (`CG-QLND38-UAT`) không đính tệp nên
  `soFile` giữ 0.
