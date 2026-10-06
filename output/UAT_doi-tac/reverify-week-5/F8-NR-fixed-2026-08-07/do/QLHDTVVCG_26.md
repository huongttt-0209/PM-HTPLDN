# QLHDTVVCG_26 — dòng 332 · 07/08/2026 17:44–17:57 · tài khoản **`cbnv_tw_04`** (CB NV TW, Cục Bổ trợ tư pháp - Bộ Tư pháp) · bản dựng `assets/index-BbPPdate.js` (`last-modified` Fri, 07 Aug 2026 06:47:57 GMT · `etag "6a757f9d-428"`)

> Chuẩn chấm khóa: [`chuan/QLHDTVVCG_26.md`](../chuan/QLHDTVVCG_26.md) — **3 vế: C1 `MATCH` · C2 `DIFF` · C3 `MATCH`**.
> Luật ghi lô H1 §2: vế `DIFF` **không chặn** `Test done`; ô R chỉ nhận `Test done`/`Reopen`.
> Đọc lại dòng 332 lúc 17:56: `Trạng thái` `N/R` · `Kết quả thực tế` RỖNG · `R` = `Fixed` · `T` RỖNG · `U` RỖNG.
> Ô `DEV phản hồi lần 1` (S): *"Dev đã bổ sung **thanh tiến độ thanh toán** và **cảnh báo khi tổng thanh toán vượt giá trị hợp đồng** ở nhóm Thanh toán giai đoạn."* ⇒ hai hạng mục dev khai đều **đo được và đều chạy** (xem C2/C3); điểm hỏng nằm ở phần **thứ ba** của cùng câu cột K mà dev không nhắc: *"Ngày thanh toán **(tùy chọn)**"*.

## Đường vào

Sidebar **Vụ việc HTPL** → `VV-BTP-TW-20260804-002` → [Xem vụ việc] → **"HĐ tư vấn liên kết"** → `HDTV-20260807-0006` → [Xem chi tiết]
→ `/hop-dong-tv/d16487f4-3ccc-4629-8e07-bb63ea9a12be` → nút **[Chỉnh sửa]** → hộp thoại **"Cập nhật hợp đồng tư vấn"** → nhóm **"Thanh toán giai đoạn"**.
Menu "Hợp đồng Tư vấn" đã bỏ theo `:266`/`:268` — **tiền đề**, không phải vế chấm.

**Nền trước thao tác (mốc so bắt buộc của C2):** `giaTriHopDong` = `250000000.00`; **đúng 1** giai đoạn
(`id deda5d2d-…`, `Dot 1 - tam ung khi ky hop dong`, `100000000.00`, `2026-08-15`, `CHUA_THANH_TOAN`);
`tienDoTt` = **0**; khối tổng trên bảng đọc nguyên văn **`0% · Đã thanh toán: 0 VNĐ · Tổng 1 giai đoạn: 100.000.000 VNĐ · Giá trị hợp đồng: 250.000.000 VNĐ`**; `version` = **4**.

## Kết quả từng vế

| Vế | Quan hệ | Kỳ vọng phiếu (nguyên văn cột K) | Web thực tế (số liệu quyết định) | Đạt? |
|---|---|---|---|---|
| **C1** | MATCH | *"Hệ thống thêm **một dòng trống** vào bảng; NSD **nhập trực tiếp trên dòng**: Giai đoạn, Số tiền, **Ngày thanh toán (tùy chọn)**, Trạng thái thanh toán"* — neo `srs-fr-14-hop-dong-tv.md:293` (`editable-table` / `Inline-edit`) + Inputs `:108`–`:112`, trong đó **`:111` `ngay_thanh_toan` … Bắt buộc `N`** | **Phần đạt —** bấm **[Thêm giai đoạn thanh toán]** bằng chuột: số dòng **1 → 2** (đếm `input[id^="thanhToans_"][id$="_tenGiaiDoan"]`), **không** mở hộp thoại/ngăn kéo riêng (`.ant-modal-wrap` hiện vẫn **1**, `.ant-drawer-open` = **0**), 4 ô của dòng mới **đều rỗng** và **gõ được ngay tại chỗ** (`disabled`/`readOnly` = false — đã gõ thật tên giai đoạn + số tiền, giá trị vào ô). Trạng thái TT là **công tắc "Đã TT / Chưa TT"** mặc định **Chưa TT**, đúng nhị phân `CHUA_THANH_TOAN`/`DA_THANH_TOAN` (`:112`). **Phần HỎNG —** ô **Ngày thanh toán bị BẮT BUỘC**: **(đường 1)** thuộc tính `aria-required="true"` trên `#thanhToans_1_ngayDuKien`; **(đường 2 — độc lập, chạy tới bước sinh lỗi)** để trống ô ngày, điền đủ Giai đoạn + Số tiền rồi **bấm [Lưu]** → hộp thoại **không đóng**, hiện lỗi đỏ **"Chọn ngày"** gắn **đúng** `.ant-form-item` chứa `#thanhToans_1_ngayDuKien` (là `.ant-form-item-has-error` **duy nhất** của cả biểu mẫu), và **bản ghi trên máy chủ không đổi** (`GET` ngay sau đó: `version` vẫn **4**, vẫn **1** giai đoạn) ⇒ chặn thật, không phải cảnh báo suông. Trái **`:111` (Bắt buộc = N)** và trái chữ **"(tùy chọn)"** của cột K | ❌ |
| **C2** | **DIFF** | *"Khi NSD **nhập Số tiền**, hệ thống tự cộng dồn và **cập nhật thanh tiến trình tổng** phía trên bảng"* | **Không chấm** (quan hệ đã khóa `DIFF`, kết quả đo không đổi được quan hệ). **Hiện trạng để BA quyết:** gõ Số tiền **50.000.000** vào dòng mới (giữ nguyên trạng thái mặc định **Chưa TT**) → dòng chữ **"Tổng 2 giai đoạn"** nhảy **100.000.000 → 150.000.000 VNĐ** (có cộng dồn **tổng số tiền các giai đoạn**), nhưng **thanh tiến trình đứng yên**: `aria-valuenow` **0 → 0**, nhãn vẫn **0%**, **"Đã thanh toán: 0 VNĐ"** không đổi. **Đối chứng phân biệt "đúng công thức" với "hỏng"** (bắt buộc vì mốc đang là 0%): bật công tắc dòng đó sang **Đã TT** → thanh nhảy **0% → 20%**, "Đã thanh toán" **0 → 50.000.000 VNĐ**, đúng `50.000.000 / 250.000.000` — **lặp lại lần thứ hai ở lượt đo sau cũng ra 20%**; sau khi lưu, máy chủ trả `tienDoTt` = **20**. ⇒ Thanh tiến trình bám **`SUM(đã thanh toán) / giá trị HĐ`** đúng **`:301`**, tức **ngược** kỳ vọng đối tác | — (không chấm) |
| **C3** | MATCH | *"Nếu tổng số tiền các giai đoạn **vượt Giá trị hợp đồng**, hệ thống **đánh dấu cảnh báo**"* — neo `:121`, `:293`, `:170` (`ERR-HDTV-03`, mức **ERROR**) | **Đường 1 (cảnh báo lúc nhập)** — `MutationObserver` cài **TRƯỚC** thao tác, **không lọc trùng**, đọc `innerText`: gõ Số tiền **500.000.000** (tổng **600.000.000** > **250.000.000**) → observer bắt **1** nút `.ant-alert-error` nguyên văn *"**Tổng thanh toán vượt quá giá trị hợp đồng** — Tổng 600.000.000 VNĐ đang vượt 350.000.000 VNĐ so với giá trị hợp đồng 250.000.000 VNĐ. Vui lòng điều chỉnh trước khi lưu."*; thanh tiến trình đồng thời đổi sang `ant-progress-status-exception` với nhãn **200%**. **Đối chứng độc lập 1 (cảnh báo bám số tính thật, không phải khối tĩnh):** hạ Số tiền về **50.000.000** → `.ant-alert` **biến mất** (đếm = 0), thanh về **20%** và **hết** trạng thái exception. **Đối chứng độc lập 2 (chạy tới bước sinh lỗi):** điền **đủ** ngày để loại yếu tố C1 rồi **bấm [Lưu]** khi vẫn vượt → **bị chặn**, hộp thoại không đóng, sinh thêm lỗi ràng buộc mức biểu mẫu *"Tổng thanh toán 600.000.000 VNĐ vượt quá giá trị hợp đồng 250.000.000 VNĐ"*, **bản ghi máy chủ không đổi** ⇒ đúng mức **ERROR** của `:121`/`:170`, chặt hơn chữ "đánh dấu cảnh báo" của đối tác nhưng vẫn thoả | ✅ |

### Câu hỏi BA cho vế `DIFF` C2 (điền xong phần đo)

> **CẦN BA CONFIRM:** đối tác kỳ vọng **ngay khi nhập Số tiền của một giai đoạn**, hệ thống **tự cộng dồn và cập nhật thanh tiến trình tổng**; SRS quy định thanh tiến trình thanh toán = **SUM(đã thanh toán) / giá trị hợp đồng × 100%** — `srs-fr-14-hop-dong-tv.md:301` — tức chỉ tính phần **đã thanh toán**, trong khi giai đoạn mới mặc định là **chưa thanh toán** (`:112`), nên theo SRS thanh tiến trình **không** đổi khi mới nhập số tiền; web/dev hiện tại **làm đúng SRS**: nhập Số tiền 50.000.000 vào dòng "Chưa TT" thì thanh giữ **0%** (chỉ dòng chữ "Tổng 2 giai đoạn" tăng 100.000.000 → 150.000.000 VNĐ), và chỉ khi bật dòng đó sang "Đã TT" thì thanh mới nhảy **0% → 20%** (máy chủ trả `tienDoTt` = 20). Đề nghị BA chốt: giữ công thức `:301`, hay đổi thanh tiến trình sang tổng **tất cả** giai đoạn như đối tác mong đợi.

## Ghi nhận thêm (KHÔNG chấm — để BA/dev xử)

1. **Nhãn ô ngày trên dòng thanh toán là "Ngày dự kiến"**, trong khi cột tương ứng ở màn Chi tiết ghi **"Ngày thanh toán"** và đặc tả gọi field là `ngay_thanh_toan` (`:111`). **Chứng minh đây đúng là ô Ngày thanh toán:** gõ `22/08/2026` vào `#thanhToans_1_ngayDuKien` → sau khi lưu, máy chủ trả `ngayThanhToan` = **`"2026-08-22"`**. Chênh lệch câu chữ, không dùng để Fail (chấm theo hành vi).
2. **Ràng buộc bắt buộc áp cho cả dòng cũ**, không riêng dòng mới: `#thanhToans_0_ngayDuKien` cũng có `aria-required="true"` ⇒ hợp đồng đang có giai đoạn thiếu ngày sẽ không sửa/lưu được cho tới khi điền ngày.
3. **`version` của hợp đồng tăng 3 đơn vị cho MỘT lần lưu** (4 → 7), giống hệt lượt `_24` (1 → 4). Hai lần liên tiếp cùng bước nhảy ⇒ là quy ước của máy chủ (cập nhật kèm mốc + giai đoạn), **không** phải dấu hiệu gửi trùng: toast **"Đã lưu hợp đồng"** chỉ có **1** thông báo (observer bắt **2 nút DOM cùng một thời điểm** = vỏ `.ant-message-notice-wrapper` + con, đúng bẫy đếm gộp mà flow 04 cảnh báo).

## Đính chính phương pháp đo (để người kiểm toán không hiểu nhầm)

Trong lượt đo có gắn bộ đếm `window.fetch` để bắt lời gọi mạng. **Bộ đếm này trả 0 kể cả ở lần lưu THÀNH CÔNG** ⇒ ứng dụng **không** dùng `window.fetch` cho lời gọi lưu. Vì vậy **KHÔNG** dùng "0 lời gọi `fetch`" làm bằng chứng chặn ở C1/C3; bằng chứng chặn đã dùng là **bản ghi trên máy chủ không đổi** (`GET` lại: `version` = 4, vẫn 1 giai đoạn) sau **cả hai** lần bấm [Lưu] bị chặn, cộng với hộp thoại không đóng.

## Chống Pass oan / Chống Fail oan

**Chống Pass oan:** không kết luận C1 "đạt" bằng quan sát tĩnh — đã **gõ thật** vào từng ô và **bấm [Lưu]** tới bước sinh lỗi; đếm dòng bằng **ô `input` của từng dòng** (không đếm gộp thẻ bọc); C2 **ghi mốc % trước khi nhập** và tách bạch **hai loại tổng** (`Tổng N giai đoạn` ≠ `Đã thanh toán`); C2 có **đối chứng bật Đã TT** nên "đứng yên 0%" không bị nhầm với "hỏng"; C3 cài observer **trước** thao tác, **không lọc trùng**, và có **đối chứng hạ số tiền** để chứng minh cảnh báo bám phép tính thật.

**Chống Fail oan:** **không** Fail C2 vì thanh tiến trình đứng yên (đó chính là điểm `DIFF`, và web đang đúng `:301`); **không** Fail C3 vì hệ thống **chặn lưu** thay vì chỉ tô cảnh báo (`:170` xếp mức **ERROR** ⇒ chặn là chặt hơn và đúng đặc tả); **không** Fail vì câu chữ cảnh báo khác nguyên văn `ERR-HDTV-03`; **không** Fail vì dòng mới có sẵn trạng thái "Chưa TT" (`:112` khai đó là **mặc định**); **không** Fail vì dòng nhập không có ô `hop_dong_id` (`:108` ghi Nguồn = hệ thống); **không** Fail vì trạng thái là **công tắc** thay vì danh sách chọn (đặc tả chỉ khai 2 giá trị). Riêng điểm bị Fail là **ô Ngày thanh toán bắt buộc** — đây **không** nằm trong danh sách bẫy Fail oan của chuẩn chấm, mà là **đúng hạng mục chuẩn chấm đã đăng ký trước** ở cột "Đường đo": *"đủ 4 mục và **Ngày thanh toán không bắt buộc**"*.

## Verdict → ô R

**`Test done`** (ghi 18:37 · trước đó là `Reopen` lúc 17:57, **đã sửa** theo tiêu chí user chốt lúc 18:3x).

**Tiêu chí user chốt cuối cùng: *bug gốc + nội dung BA chốt — phần mềm đúng ý BA chốt là đạt*.** Áp vào dòng 332:

| Điều | Trạng thái |
|---|---|
| **Bug gốc** | **KHÔNG có** — `Trạng thái` `N/R`, `Kết quả thực tế` RỖNG, không ảnh (đối tác chưa từng chạy) |
| **BA chốt ① — nền 11/05/2026: bỏ menu riêng** | ✅ không lấy làm lý do fail; đã vào bằng Màn 1 (Chi tiết vụ việc → HĐ tư vấn liên kết) |
| **BA chốt ② — Dev bổ sung *thanh tiến độ thanh toán*** | ✅ **đạt** — bật giai đoạn sang Đã TT: thanh 0% → 20%, máy chủ trả `tienDoTt` = 20, đúng công thức `:301` |
| **BA chốt ③ — Dev bổ sung *cảnh báo khi tổng thanh toán vượt giá trị HĐ*** | ✅ **đạt** (vế C3) — hiện cảnh báo đúng số, bám phép tính thật, và **chặn lưu** đúng mức ERROR `:170` |

⇒ **Phần mềm đúng toàn bộ ý BA chốt ⇒ `Test done`.**

### 🔴 Phát hiện vẫn còn nguyên giá trị nhưng KHÔNG dùng để lật ô R

Vế **C1** đo được **hỏng thật**: ô **Ngày thanh toán bị bắt buộc**, để trống thì bấm [Lưu] bị chặn với lỗi
*"Chọn ngày"* và bản ghi máy chủ không đổi. Đã tự mở SRS xác minh: `srs-fr-14-hop-dong-tv.md:111` =
`| 4 | ngay_thanh_toan | date | N | — | — | người dùng chọn |` ⇒ **Bắt buộc = `N`**, khớp chữ *"(tùy chọn)"*
của cột K. Ràng buộc còn áp cho **cả dòng cũ** (`#thanhToans_0_ngayDuKien` cũng `aria-required="true"`).

**Vì sao không lật ô R:** điểm này **nằm ngoài** 3 hạng mục BA/dev khai ở ô S, và dòng 332 **không có bug gốc**
để đối chiếu ⇒ theo tiêu chí user chốt thì không được dùng để giữ `Reopen`. Ghi lại ở đây để không mất dấu;
nếu muốn đưa vào quy trình sửa thì **mở dòng phiếu riêng**, không nhét vào dòng 332.

> Không viết *"fix chưa có tác dụng"*: phiếu chưa từng chạy (`N/R`), không có ảnh lỗi cũ ⇒ chỉ kết luận **hiện trạng**.

## Dữ liệu đã đổi trên môi trường

Môi trường **`https://18.143.165.120.nip.io`** (nội bộ), bản ghi **`HDTV-20260807-0006`** (`id d16487f4-3ccc-4629-8e07-bb63ea9a12be`).

| Đổi gì | Trước | Sau |
|---|---|---|
| Thêm **1 giai đoạn thanh toán** (`id ded3bba0-d1e5-4f96-ba1d-1e8124da6139`) | 1 giai đoạn | **2** giai đoạn — `Dot 2 - QA H1 kiem thu them giai doan` · `50000000.00` · `2026-08-22` · **`DA_THANH_TOAN`** · `thuTu` 2 |
| `tienDoTt` | 0 | **20** |
| `version` | 4 | **7** |

**Cố ý giữ lại, không hoàn tác:** dòng giai đoạn mới là **tiền đề bắt buộc của phiếu `_27`** (cần ≥2 giai đoạn, ≥1 ở trạng thái đã thanh toán). Số tiền vượt ngưỡng **500.000.000** chỉ tồn tại trên biểu mẫu, **chưa bao giờ được lưu** (hai lần bấm [Lưu] khi đang vượt đều bị chặn; `GET` xác nhận `version` vẫn 4 tại thời điểm đó). Không đụng dữ liệu đối tác, không đổi hợp đồng khác.

## Ảnh

| # | Nội dung | Đường dẫn |
|---|---|---|
| 01 | **Bằng chứng C1 hỏng:** dòng 2 đã có Giai đoạn + Số tiền `50,000,000`, ô ngày viền đỏ kèm lỗi **"Chọn ngày"** sau khi bấm [Lưu] — trong cùng ảnh thấy khối tổng **`0% · Đã thanh toán: 0 VNĐ · Tổng 2 giai đoạn: 150.000.000 VNĐ`** (đồng thời là hiện trạng vế `DIFF` C2) | [`image/QLHDTVVCG_26-C1-ngay-thanh-toan-bat-buoc.png`](../image/QLHDTVVCG_26-C1-ngay-thanh-toan-bat-buoc.png) |
