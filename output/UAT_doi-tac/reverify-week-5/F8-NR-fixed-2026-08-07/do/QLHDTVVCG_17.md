# QLHDTVVCG_17 — dòng 323 · 07/08/2026 18:08–18:12 · tài khoản **`cbnv_tw_04`** (CB NV TW, Cục Bổ trợ tư pháp - Bộ Tư pháp) · bản dựng `assets/index-BbPPdate.js` (`last-modified` Fri, 07 Aug 2026 06:47:57 GMT · `etag "6a757f9d-428"`)

> Chuẩn chấm khóa: [`chuan/QLHDTVVCG_17.md`](../chuan/QLHDTVVCG_17.md) — **4 vế: C1 `MATCH` · C2 `MATCH` · C3 `GAP` · C4 `GAP`**.
> Luật ghi lô H1 §2: vế `GAP` **không chặn** `Test done`; ô R chỉ nhận `Test done`/`Reopen`.
> Đọc lại dòng 323 lúc 18:07: `Trạng thái` `N/R` · `Kết quả thực tế` RỖNG · `R` = `Fixed` · `T` RỖNG · `U` RỖNG.
> Cột K nguyên văn: *"Hệ thống thực hiện **xóa mềm** (đánh dấu đã xóa, **không xóa vật lý**), **lưu vết thao tác** theo quy định, hiển thị thông báo **"Đã xóa hợp đồng"** và **làm mới danh sách**."*
> **Phiếu chạy CUỐI CÙNG của lượt** vì đây là thao tác xóa thật.

## Đường vào

Không có màn danh sách hợp đồng độc lập (`:175`, `:266`, `:268`) và HĐ-2 **không gắn vụ việc nào** nên không vào được qua "HĐ tư vấn liên kết" của vụ việc. Đã thử **Mạng lưới Tư vấn viên → Tư vấn viên / Chuyên gia → `CG-QLND38-UAT` → chi tiết**: màn chỉ có 4 thẻ *Hồ sơ · Năng lực · Lịch sử hỗ trợ (0) · Đánh giá (0)*, **không có mục hợp đồng** ⇒ đường "Lịch sử TVV" mà ô `DEV phản hồi lần 1` nhắc **hiện chưa dẫn tới hợp đồng**.
⇒ Vào thẳng trang chi tiết `/hop-dong-tv/fbcb5a7a-27a0-4d49-9712-123ce1ac4eef` bằng điều hướng nội bộ của ứng dụng (không tải lại trang, phiên đăng nhập giữ nguyên). Đây là **tiền đề**, không phải vế chấm — không log lỗi. (Ghi nhận cho BA ở mục cuối.)

## Tiền đề đã xác nhận TRƯỚC khi bấm

| Đường | Số liệu |
|---|---|
| **Giao diện** trang chi tiết | Mã **`HDTV-20260807-0001`** · trường "Vụ việc liên kết" = **0** · thẻ "Vụ việc liên kết" hiện **"Chưa có vụ việc liên kết"** · Ghi chú *"QA-F8-SEED-20260807 · CỐ Ý không gắn vụ việc (phục vụ phiếu _17)"* |
| **Máy chủ** `GET /api/v1/hop-dong-tu-vans/fbcb5a7a-…` | 200 · `vuViecLienKets` **0** phần tử · `version` **1** · `trangThai` `DANG_THUC_HIEN` |
| **Danh sách theo ngữ cảnh** `?tuVanVienId=38383838-…` | **4** hợp đồng, có `HDTV-20260807-0001` |
| **Nhật ký trước khi xóa** `GET /{id}/audit-logs` | **200**, **2** dòng, cả hai `CREATE` lúc `2026-08-07T06:14:42Z` do `cbnv_tw_03` — chứng minh **trước khi xóa** vẫn đọc được nhật ký của bản ghi này |

**Định danh ghi lại trước khi xóa (bắt buộc):** `id` **`fbcb5a7a-27a0-4d49-9712-123ce1ac4eef`** · mã **`HDTV-20260807-0001`** · số HĐ `QAF8/2026/HD-02`.

## Thao tác đã chạy

Bấm **[Xóa]** → hộp xác nhận *"Xóa hợp đồng? / Hợp đồng sẽ được gỡ khỏi danh sách và **lưu vết trong nhật ký**."* → bấm **[Xóa]** xác nhận.
Móc `XMLHttpRequest` + `MutationObserver` (cài **trước** thao tác, **không lọc trùng**, đọc `innerText`) ghi được **toàn bộ** chuỗi sự kiện lúc `2026-08-07T11:10:36Z` (18:10:36 giờ VN):

| # | Sự kiện | Kết quả |
|---|---|---|
| 1 | `DELETE /api/v1/hop-dong-tu-vans/fbcb5a7a-…` | **204** (đúng **1** lời gọi ⇒ không gửi trùng) |
| 2 | Thông báo nổi | **`Đã xóa hợp đồng`** (2 nút DOM cùng thời điểm = vỏ `.ant-message` + con ⇒ **1** thông báo) |
| 3 | `GET /api/v1/hop-dong-tu-vans/fbcb5a7a-…` (ứng dụng tự gọi lại) | **404** `ERR-VAL-X3-159-02` *"Hợp đồng tư vấn không tồn tại"* |
| 4 | `GET /api/v1/hop-dong-tu-vans/fbcb5a7a-…/audit-logs` (ứng dụng tự gọi lại) | **404** cùng mã lỗi |
| 5 | Thông báo nổi **thứ hai** | **`Hợp đồng tư vấn không tồn tại`** |
| 6 | Màn hình | rời trang chi tiết, dừng ở **`/dashboard`** |

## Kết quả từng vế

| Vế | Quan hệ | Kỳ vọng phiếu | Web thực tế (số liệu quyết định) | Đạt? |
|---|---|---|---|---|
| **C1** | MATCH | *"**xóa mềm** (đánh dấu đã xóa, **không xóa vật lý**)"* — `:124`, `:299`, `:182`, BR-DATA-01 `:505` (*"set `is_deleted = 1`. Không xóa vật lý"*) | **Phần đo được:** thao tác được chấp nhận (`DELETE` → **204**) và bản ghi **biến khỏi danh sách** — danh sách theo ngữ cảnh `?tuVanVienId=38383838-…` từ **4** hợp đồng còn **3** (`0006`/`0005`/`0003`), **không** còn `HDTV-20260807-0001`. **Phần KHÔNG đo được — đúng thứ mà cột K đòi:** tra lại **đúng định danh** `fbcb5a7a-…` trả **404** `ERR-VAL-X3-159-02` *"Hợp đồng tư vấn không tồn tại"* (đo lại lần 2 lúc 18:12 vẫn 404) ⇒ **không có bề mặt nào cho thấy bản ghi còn tồn tại kèm cờ đã xóa**. Đã tìm hết đường hợp lệ: lược đồ `/api/docs-json` (549 đường dẫn) **không có** đường tra bản ghi đã xóa / thùng rác / khôi phục, và **không có** tham số kiểu "gồm cả bản ghi đã xóa" trên đường dẫn hợp đồng; nhật ký toàn hệ thống trả **403** với vai trò CB NV (chuẩn chấm cấm dùng `admin` để ra kết luận). **CHƯA CHỐT** — 404 là hành vi **bình thường của cả xóa mềm lẫn xóa vật lý**, nên **không** được suy ra "đã xóa vật lý" để Fail, mà cũng **không** được Pass bằng "biến khỏi danh sách" (chuẩn chấm §d cấm đúng bẫy này) | 🟡 chưa chốt |
| **C2** | MATCH | *"**lưu vết thao tác** theo quy định"* — `:125`, `:162`, BR-DATA-05 `:522`; phải là dòng **của chính thao tác vừa làm** | **Trước khi xóa:** nhật ký của bản ghi đọc được bình thường (**200**, 2 dòng `CREATE`). **Sau khi xóa:** cùng đường dẫn trả **404** cùng mã `ERR-VAL-X3-159-02` (kiểm tra tồn tại chặn trước khi trả nhật ký) ⇒ **không đọc được dòng nhật ký của thao tác xóa**. Mục "Nhật ký hoạt động" trên trang chi tiết cũng mất theo trang. Nhật ký toàn hệ thống `GET /api/v1/audit-logs?entityId=…` trả **403** với vai trò CB NV bắt buộc của phiếu ⇒ **CHƯA CHỐT**: không có bằng chứng nào cho thấy thao tác xóa **có** được lưu vết, và cũng **không** có bằng chứng cho thấy **không** lưu vết. (Hộp xác nhận có hứa *"lưu vết trong nhật ký"* — lời hứa của giao diện, **không** phải bằng chứng.) | 🟡 chưa chốt |
| **C3** | **GAP** | *"hiển thị thông báo **"Đã xóa hợp đồng"**"* — đặc tả **im lặng**: bảng Error Handling `:166`–`:173` có mã cho **xóa thất bại** (`E4`) và **lưu thành công** (`I1`) nhưng **không có** mã cho **xóa thành công**; bảng thông báo chung `srs-fr-05-vu-viec.md:1588`–`:1597` cũng không có | **Không chấm** (quan hệ khóa `GAP`). **Hiện trạng — web ĐÚNG kỳ vọng đối tác:** bắt được nguyên văn **`Đã xóa hợp đồng`**, **trùng từng chữ** với cột K. Thông báo **tự tắt** (đọc DOM sau đó `.ant-message-notice-wrapper` **rỗng**) ⇒ nếu dò DOM kiểu poll thì đã kết luận sai *"im lặng"* | — (không chấm) |
| **C4** | **GAP** | *"và **làm mới danh sách**"* — đặc tả **im lặng**; `:175` còn khẳng định nhóm X.3 **không có màn danh sách độc lập** nên "danh sách" chưa xác định là màn nào | **Không chấm** (quan hệ khóa `GAP`). **Hiện trạng:** sau khi xác nhận, ứng dụng **rời trang chi tiết** và dừng ở **`/dashboard`** — **không** phải "làm mới một danh sách". Bản ghi không còn hiển thị ở bất kỳ danh sách nào (danh sách theo ngữ cảnh TVV còn 3 dòng) | — (không chấm) |

## 🔴 Lỗi tự lộ trong bước bắt buộc (ghi nhận, đã đủ bằng chứng)

Ngay **sau khi xóa thành công**, ứng dụng **tự gọi lại** bản ghi vừa xóa — `GET /{id}` và `GET /{id}/audit-logs` — cả hai trả **404 `ERR-VAL-X3-159-02`**, và **hiện thêm một thông báo lỗi** *"**Hợp đồng tư vấn không tồn tại**"* **ngay sau** thông báo thành công *"Đã xóa hợp đồng"*. Người dùng làm đúng một thao tác hợp lệ nhưng nhận **cùng lúc 1 thông báo thành công + 1 thông báo lỗi**.
Lỗi này **tự lộ trong bước bắt buộc** của chính vế đang verify (bấm xác nhận xóa), không phải do đổi màn/vai trò/bộ lọc ⇒ ghi nhận theo quy định. **Yêu cầu nghiệp vụ:** sau khi xóa thành công, hệ thống **không được** báo lỗi cho người dùng về chính bản ghi vừa xóa.

**Không chụp ảnh:** cả hai thông báo **tự tắt sau vài giây**; bằng chứng đang dùng **mạnh hơn ảnh** — nhật ký lời gọi mạng (mã 204/404 + mã lỗi + `requestId` + mốc thời gian) và nguyên văn chuỗi do bộ bắt cài **trước** thao tác ghi lại. Dựng lại cảnh để chụp sẽ phải **xóa thêm một hợp đồng thật nữa** — vi phạm phạm vi và làm bẩn môi trường chung.

## Chống Pass oan / Chống Fail oan

**Chống Pass oan:** **không** kết luận "đã xóa mềm" chỉ vì bản ghi biến khỏi danh sách (xóa vật lý cũng cho đúng hiện tượng đó — đây là bẫy số 1 của chuẩn chấm); **đã ghi định danh trước khi xóa** nên tra ngược được (không rơi vào bẫy "không tra được"); **không** nhận "nhật ký có dòng nào đó" là đạt C2 — dòng cần là **của chính thao tác xóa**, và dòng đó hiện **không đọc được**; **không** Pass C3/C4 dù web làm đúng ý đối tác (hai vế đã khóa `GAP`); bắt thông báo bằng `MutationObserver` cài **trước** thao tác (cả hai thông báo đều tự tắt), đọc `innerText`, **không lọc trùng**, và **đếm số lời gọi** `DELETE` = 1 để loại gửi trùng.

**Chống Fail oan:** **không** Fail C3 vì đặc tả không quy định thông báo xóa thành công (đó là `GAP`); **không** Fail C4 vì màn không "làm mới danh sách" (đặc tả im lặng + `:175`); **không** Fail vì câu chữ hộp xác nhận khác (đặc tả không khai câu xác nhận xóa cho hợp đồng); **không** Fail vì nút Xóa là biểu tượng; **không** Fail C1 chỉ vì tra lại được **404** — 404 là hành vi bình thường của xóa mềm, nên đây là **chưa chốt**, không phải "đã xóa vật lý".

## Verdict → ô R

**`Test done`** (ghi 18:4x · trước đó là `Reopen` lúc 18:12, **đã sửa** theo tiêu chí user chốt lúc 18:3x).

**Tiêu chí user chốt cuối cùng: *bug gốc + nội dung BA chốt — phần mềm đúng ý BA chốt là đạt*.** Áp vào dòng 323:

| Điều | Trạng thái |
|---|---|
| **Bug gốc** | **KHÔNG có** — `Trạng thái` `N/R`, `Kết quả thực tế` RỖNG, không ảnh (đối tác chưa từng chạy) |
| **BA chốt ① — 06/08/2026, Loại 4 hướng A: giữ QĐ 11/05 bỏ menu riêng, *"phần mềm đúng bản gốc, test case mô tả lối vào đã hết hiệu lực"*** | ✅ không lấy lối vào làm lý do fail (đã ghi rõ là tiền đề) |
| **BA chốt ② — Dev bổ sung *cột Hành động*** | ✅ **đạt** — nút [Xóa] có trên màn, bấm được, có hộp xác nhận trước khi xóa |
| **BA chốt ③ — Dev bổ sung *luồng thao tác theo ngữ cảnh vụ việc*** | ✅ **đạt** — thao tác xóa đi lọt (`DELETE` **204**, đúng **1** lời gọi), toast **"Đã xóa hợp đồng"** trùng khít cột K, bản ghi rời danh sách (4 → 3 hợp đồng) |

⇒ **Phần mềm đúng toàn bộ ý BA chốt ⇒ `Test done`.**

### 🔴 Hai phát hiện vẫn còn nguyên giá trị nhưng KHÔNG dùng để lật ô R

1. **Lỗi người dùng nhìn thấy:** ngay sau khi xóa thành công, ứng dụng **tự gọi lại** bản ghi vừa xóa
   (`GET /{id}` và `GET /{id}/audit-logs`) → **2 lần 404** `ERR-VAL-X3-159-02`, và hiện **thêm** thông báo
   **"Hợp đồng tư vấn không tồn tại"** ngay sau thông báo thành công. Người dùng làm một thao tác hợp lệ mà
   nhận cùng lúc 1 thông báo thành công + 1 thông báo lỗi.
2. **Hai vế `MATCH` (C1 xóa mềm · C2 lưu vết) CHƯA CHỐT:** sau khi xóa không có bề mặt hợp lệ nào cho vai
   **Cán bộ Nghiệp vụ** thấy bản ghi còn tồn tại kèm cờ đã xóa, cũng không đọc được dòng nhật ký của chính
   thao tác xóa (nhật ký hợp đồng trả 404; nhật ký toàn hệ thống trả 403 với vai trò này).

**Vì sao không lật ô R:** cả hai đều **nằm ngoài** 3 hạng mục BA chốt ở ô S, và dòng 323 **không có bug gốc**
để đối chiếu. Riêng điểm 2 còn **không phải "dev còn lỗi"** mà là **không đo được** — thiếu quyền đọc nhật ký
của vai trò nghiệp vụ, đúng dạng **blocker vận hành**. Ghi lại để không mất dấu; muốn đưa vào quy trình sửa
thì **mở dòng phiếu riêng**.

### ⚠️ Giới hạn phương pháp phải khai (ảnh hưởng độ chắc của điểm 1)

Lối vào mà BA chốt (*"vào từ Chi tiết Vụ việc / Lịch sử TVV"*) **không dùng được cho chính phiếu này**:
Điều kiện của phiếu là *"Không có vụ việc liên kết"*, mà hợp đồng không gắn vụ việc thì **không** vào được từ
Chi tiết Vụ việc; còn màn chi tiết Tư vấn viên/Chuyên gia **không có mục hợp đồng**. Đã phải vào thẳng trang
chi tiết bằng điều hướng nội bộ. ⇒ **Chưa chứng minh được** điểm 1 có tái hiện y hệt khi vào bằng lối BA chốt
hay không. Đây là **mâu thuẫn giữa Điều kiện của phiếu và lối vào BA chốt**, nên đề nghị BA chốt lối vào cho
nhóm hợp đồng "chưa gắn vụ việc" (xem mục *Ghi nhận thêm cho BA* cuối file).

> Không viết *"fix chưa có tác dụng"*: phiếu chưa từng chạy (`N/R`), không có ảnh lỗi cũ ⇒ chỉ kết luận **hiện trạng**.

## Dữ liệu đã đổi trên môi trường

Môi trường **`https://18.143.165.120.nip.io`** (nội bộ), lúc **18:10:36 ngày 07/08/2026**, tài khoản `cbnv_tw_04`.

| Đổi gì | Trước | Sau |
|---|---|---|
| **Xóa hợp đồng HĐ-2** `HDTV-20260807-0001` (`id fbcb5a7a-27a0-4d49-9712-123ce1ac4eef`, số HĐ `QAF8/2026/HD-02`) | tồn tại, `version` 1, 0 vụ việc liên kết | **không còn tra được** (`GET` → 404); danh sách theo ngữ cảnh TVV `38383838-…` từ **4** còn **3** hợp đồng |

**Đây là thao tác xóa CÓ CHỦ ĐÍCH của phiếu** — HĐ-2 do QA seed lúc 13:14 cùng ngày, ghi chú *"CỐ Ý không gắn vụ việc (phục vụ phiếu _17)"*, **không** phải dữ liệu đối tác. **Không khôi phục được bằng giao diện** (không có chức năng khôi phục trong lược đồ). Nếu lượt sau cần lại một hợp đồng "sạch vụ việc" thì phải seed mới.
Không đụng hợp đồng khác: `HDTV-20260807-0006` (HĐ-1) giữ nguyên 3 vụ việc liên kết, 2 mốc tiến độ, 1 giai đoạn thanh toán.

## Ghi nhận thêm cho BA (KHÔNG chấm)

Ô `DEV phản hồi lần 1` nói lối vào hợp đồng là *"vào từ **Chi tiết Vụ việc** / **Lịch sử TVV**"*. Đo được: lối "Chi tiết Vụ việc" **có thật** (mục "HĐ tư vấn liên kết"), nhưng màn chi tiết Tư vấn viên/Chuyên gia hiện **chỉ có** 4 thẻ *Hồ sơ · Năng lực · Lịch sử hỗ trợ · Đánh giá*, **không có** mục hợp đồng. Hệ quả: **hợp đồng không gắn vụ việc nào thì người dùng không có lối vào nào** để xem/sửa/xóa nó. Đề nghị BA chốt lối vào cho nhóm hợp đồng "chưa gắn vụ việc". Không log thành lỗi vì lối vào là **tiền đề** theo quyết định BA 11/05/2026, ngoài phạm vi vế chấm của phiếu.
