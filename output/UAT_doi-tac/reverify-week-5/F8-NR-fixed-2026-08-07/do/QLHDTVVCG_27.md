# QLHDTVVCG_27 — dòng 333 · 07/08/2026 17:59–18:02 · tài khoản **`cbnv_tw_04`** (CB NV TW, Cục Bổ trợ tư pháp - Bộ Tư pháp) · bản dựng `assets/index-BbPPdate.js` (`last-modified` Fri, 07 Aug 2026 06:47:57 GMT · `etag "6a757f9d-428"` — **đo lại lúc 18:02, y hệt đầu phiên, không có deploy giữa lượt**)

> Chuẩn chấm khóa: [`chuan/QLHDTVVCG_27.md`](../chuan/QLHDTVVCG_27.md) — **2 vế: C1 `GAP` · C2 `MATCH`**.
> Luật ghi lô H1 §2: vế `GAP` **không chặn** `Test done`; ô R chỉ nhận `Test done`/`Reopen`.
> Đọc lại dòng 333 lúc 17:58: `Trạng thái` `N/R` · `Kết quả thực tế` RỖNG · `R` = `Fixed` · `T` RỖNG · `U` RỖNG.
> Ô `DEV phản hồi lần 1` (S) giống hệt phiếu `_26`: dev khai đã bổ sung **thanh tiến độ thanh toán** — đúng thứ vế `MATCH` C2 cần đo.
> Cột K nguyên văn: *"Hệ thống **bỏ dòng khỏi bảng** và **cập nhật lại thanh tiến trình tổng**"*.

## Đường vào

`/hop-dong-tv/d16487f4-3ccc-4629-8e07-bb63ea9a12be` (HĐ-1 `HDTV-20260807-0006`) → **[Chỉnh sửa]** → hộp thoại **"Cập nhật hợp đồng tư vấn"** → nhóm **"Thanh toán giai đoạn"**.
Bước J ghi *"Bấm nút **Xóa giai đoạn thanh toán**"* — trên web không có nút mang chữ đó; trên mỗi dòng có **biểu tượng dấu trừ tròn** (`anticon-minus-circle`), xem C1.

## Tiền đề đã dựng (bắt buộc, vì thiếu là C2 không đo được gì)

Chuẩn chấm §c đòi **≥2 giai đoạn, trong đó ≥1 dòng "đã thanh toán"**, và cảnh báo: xoá dòng *chưa* thanh toán thì % **đương nhiên** không đổi ⇒ phép đo vô nghĩa.
Thêm một bậc nữa để **không rơi vào ca suy biến 0%**: nếu chỉ có 1 dòng đã thanh toán thì xoá xong % về **0** — mà một giao diện hỏng kiểu "reset về 0" cũng cho ra **0**, không phân biệt được.

⇒ Trước khi đo đã bật **cả 2 dòng** sang **Đã TT** ngay trên biểu mẫu, tạo mốc **60%** (= `150.000.000 / 250.000.000`), để sau khi xoá dòng 50.000.000 con số phải rơi xuống **40%** — một giá trị **không tầm thường**, chỉ đúng nếu hệ thống thực sự tính lại theo công thức.

**Mốc so ghi trước khi bấm xoá** (đọc thẳng từ biểu mẫu):

| # | Giai đoạn | Số tiền | Ngày TT | Trạng thái |
|---|---|---|---|---|
| 1 | `Dot 1 - tam ung khi ky hop dong` | 100.000.000 | 15/08/2026 | **Đã TT** |
| 2 | `Dot 2 - QA H1 kiem thu them giai doan` | 50.000.000 | 22/08/2026 | **Đã TT** |

Giá trị hợp đồng **250.000.000 VNĐ** · khối tổng đọc nguyên văn **`60% · Đã thanh toán: 150.000.000 VNĐ · Tổng 2 giai đoạn: 150.000.000 VNĐ · Giá trị hợp đồng: 250.000.000 VNĐ`** · `aria-valuenow` = **60** · bản ghi máy chủ lúc đó: `version` **7**, `tienDoTt` **20**, 2 giai đoạn.

## Kết quả từng vế

| Vế | Quan hệ | Kỳ vọng phiếu | Web thực tế (số liệu quyết định) | Đạt? |
|---|---|---|---|---|
| **C1** | **GAP** | *"Hệ thống **bỏ dòng khỏi bảng**"* — `srs-fr-14-hop-dong-tv.md:293` **im lặng**: khai bảng Nhóm 4 là `editable-table` nhưng **không khai nút xoá nào**, trong khi `:291` có khai `[Bỏ liên kết]` và `:292` có khai `[+ Thêm mốc]`; Processing `:118`–`:125` chỉ có bước 7 xoá **hợp đồng** | **Không chấm** (quan hệ đã khóa `GAP`; kết quả đo không đổi được quan hệ). **Hiện trạng — web hiện tại LÀM ĐÚNG kỳ vọng đối tác:** mỗi dòng thanh toán **có** một điều khiển xoá là **biểu tượng dấu trừ tròn** (`span.anticon.anticon-minus-circle`, `aria-label="minus-circle"`), đặt ở cuối dòng; bấm bằng chuột → dòng **biến khỏi bảng ngay**, số dòng **2 → 1**, dòng còn lại đúng là `Dot 1 - tam ung khi ky hop dong`. **Không** có hộp xác nhận (`.ant-popconfirm`/`.ant-modal-confirm` đếm = **0**) và **không** mở thêm hộp thoại nào (`.ant-modal-wrap` hiện vẫn = **1**). Ghi thêm 2 chi tiết cho BA: (a) điều khiển là **biểu tượng không có chữ, cũng không có `title`/tooltip**; (b) bước J của phiếu gọi nó là *"nút Xóa giai đoạn thanh toán"* — trên web **không tồn tại nhãn chữ đó** | — (không chấm) |
| **C2** | MATCH | *"…và **cập nhật lại thanh tiến trình tổng**"* — `:301` `Progress bar thanh toán = SUM(đã thanh toán) / giá trị HĐ * 100%`, `:155` `tien_do_tt` | **Đường 1 (giao diện, ngay khi xoá)** — xoá **dòng đã thanh toán 50.000.000**: khối tổng đổi từ **`60% · Đã thanh toán: 150.000.000 VNĐ · Tổng 2 giai đoạn`** → **`40% · Đã thanh toán: 100.000.000 VNĐ · Tổng 1 giai đoạn: 100.000.000 VNĐ`**, `aria-valuenow` **60 → 40**. **Đối chứng độc lập 1 — tự tính lại, không đọc bằng mắt:** phần còn lại `SUM(đã thanh toán)` = **100.000.000**, chia giá trị hợp đồng **250.000.000** = **40%** ⇒ **khớp**; mức tụt đúng bằng **20 điểm** = `50.000.000 / 250.000.000`, tức đúng phần của dòng vừa xoá, không phải "reset". **Đối chứng độc lập 2 — máy chủ:** bấm [Lưu] → `GET` lại bản ghi: còn **1** giai đoạn (`id deda5d2d-…`; giai đoạn `ded3bba0-…` **đã biến mất**), **`tienDoTt` = 40** — trùng khít số hiển thị, chứng minh không phải giao diện tự vẽ | ✅ |

### Câu hỏi BA cho vế `GAP` C1

> **CẦN BA CONFIRM:** cột `Kết quả mong đợi` đòi *"Hệ thống bỏ dòng khỏi bảng"* và bước J gọi là *"nút Xóa giai đoạn thanh toán"*, nhưng `srs-fr-14-hop-dong-tv.md:293` — dòng **duy nhất** đặc tả bảng Nhóm 4 — **không khai bất kỳ nút nào** cho nhóm này (trong khi `:291` khai `[Bỏ liên kết]`, `:292` khai `[+ Thêm mốc]`), và bảng Processing `:118`–`:125` cũng không có bước xoá một giai đoạn thanh toán. Web hiện tại **đã có** điều khiển xoá dạng biểu tượng dấu trừ, xoá được dòng và cập nhật lại thanh tiến trình đúng công thức `:301`. Đề nghị BA chốt **bổ sung điều khiển xoá dòng vào đặc tả `:293`** (kèm quy ước: biểu tượng hay chữ, có cần tooltip và hộp xác nhận không) — đây là **điểm bổ sung đặc tả, không phải lỗi chặn bàn giao**.

## Ghi nhận thêm (KHÔNG chấm)

1. **Xoá chỉ có hiệu lực trong bộ nhớ biểu mẫu cho tới khi bấm [Lưu].** Đọc bản ghi máy chủ **ngay sau khi dòng biến mất mà chưa lưu**: vẫn **2** giai đoạn, `tienDoTt` vẫn **20**, `version` vẫn **7**. Sau khi [Lưu] mới còn 1 giai đoạn, `tienDoTt` = 40. Đây **không** bị chấm Fail — `:122` khai giai đoạn thanh toán được lưu **cùng** bản ghi hợp đồng, và đặc tả không khai thời điểm ghi xuống.
2. **`version` lại tăng 3 đơn vị cho MỘT lần lưu** (7 → 10), lần thứ ba liên tiếp cùng bước nhảy (`_24`: 1 → 4; `_26`: 4 → 7) ⇒ quy ước máy chủ, **không** phải gửi trùng. Toast **"Đã lưu hợp đồng"** chỉ có **1** thông báo — bộ bắt (cài trước, **không lọc trùng**, đọc `innerText`) ghi **2 nút DOM cùng thời điểm** = vỏ `.ant-message-notice-wrapper` + con, đúng bẫy đếm gộp mà flow 04 cảnh báo.
3. **Các nhóm con khác không bị đụng:** sau khi lưu, mốc tiến độ vẫn **2**, vụ việc liên kết vẫn **3** (`VV-BTP-TW-20260804-002/-003/-004`) ⇒ **tiền đề của `_18` (HĐ-1 đang có vụ việc liên kết) còn nguyên**.

## Chống Pass oan / Chống Fail oan

**Chống Pass oan:** **không** xoá dòng "chưa thanh toán" rồi kết luận C2 đạt (theo `:301` thì % **đương nhiên** không đổi — phép đo đó vô nghĩa); **không** để phép đo rơi vào ca suy biến **về 0%** (đã dựng mốc 60% để số đích **40%** phải đúng mới qua được); **không** đọc % bằng mắt — đã **tự tính lại** `SUM(đã thanh toán) / giá trị HĐ` từ các dòng còn lại; **không** dừng ở giao diện — đã đọc lại **bản ghi máy chủ** (`tienDoTt` = 40) để loại ca "giao diện tự vẽ số"; đếm dòng bằng **ô `input` của từng dòng**, không đếm gộp thẻ bọc.

**Chống Fail oan:** **không** Fail C1 vì trên dòng không có nút mang chữ *"Xóa giai đoạn thanh toán"* (`:293` **không khai** nút nào cho Nhóm 4 ⇒ thiếu/khác đều có thể là đúng đặc tả — đó chính là lý do vế khóa `GAP`); **không** Fail vì phải bấm [Lưu] mới có hiệu lực (`:122`); **không** Fail vì % **không** về 0 sau khi xoá (công thức `:301` chỉ trừ phần của dòng bị xoá); **không** Fail vì điều khiển xoá là **biểu tượng** chứ không phải chữ; **không** Fail vì **không có hộp xác nhận** (cột K của phiếu này **không nhắc** hộp xác nhận — khác `_23`).

## Verdict → ô R

**`Test done`** — vế `MATCH` **duy nhất (C2) đạt**, có 3 phép độc lập trùng khít (giao diện 60% → 40% · tự tính 100.000.000/250.000.000 = 40% · máy chủ `tienDoTt` = 40). Vế `GAP` C1 chỉ ghi hiện trạng + câu hỏi BA, theo luật lô H1 **không chặn** `Test done`.

> Không viết *"fix đã có tác dụng"*: phiếu chưa từng chạy (`N/R`), không có ảnh lỗi cũ ⇒ chỉ kết luận **hiện trạng**.

## Dữ liệu đã đổi trên môi trường

Môi trường **`https://18.143.165.120.nip.io`** (nội bộ), bản ghi **`HDTV-20260807-0006`** (`id d16487f4-3ccc-4629-8e07-bb63ea9a12be`), lúc **18:00–18:01 ngày 07/08/2026**.

| Đổi gì | Trước | Sau |
|---|---|---|
| **Xoá** giai đoạn `ded3bba0-d1e5-4f96-ba1d-1e8124da6139` (`Dot 2 - QA H1 kiem thu them giai doan`, 50.000.000, do chính phiếu `_26` tạo) | 2 giai đoạn | **1** giai đoạn |
| Trạng thái giai đoạn `deda5d2d-…` (`Dot 1`) | `CHUA_THANH_TOAN` | **`DA_THANH_TOAN`** — bật để dựng mốc 60%, **cố ý giữ**, xem ghi chú dưới |
| `tienDoTt` | 20 | **40** |
| `version` | 7 | **10** |

**Không hoàn tác** trạng thái `Dot 1`: hoàn tác là thêm một lần ghi nữa vào môi trường chung mà không phiếu nào cần, và không có phiếu còn lại nào phụ thuộc trạng thái thanh toán của HĐ-1. **Không** đụng mốc tiến độ (vẫn 2), **không** đụng vụ việc liên kết (vẫn 3), **không** đụng hợp đồng khác, **không** đụng dữ liệu đối tác.

## Ảnh

Không chụp — vế `MATCH` duy nhất **đạt**, không có FAIL cần chứng minh (flow 04 §7). Số liệu quyết định (60 → 40, `tienDoTt` = 40) đã ghi thẳng trong bảng trên.
