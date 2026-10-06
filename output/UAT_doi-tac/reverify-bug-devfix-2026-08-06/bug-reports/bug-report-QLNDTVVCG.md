# Bug Report — QLNDTVVCG (Tư vấn chuyên sâu · Quản lý nội dung TV với TVV/CG)

| Thông tin | Giá trị |
|-----------|---------|
| **Dự án** | PM HTPLDN |
| **Môi trường** | https://18.143.165.120.nip.io — bản dựng **HTPLDN · V1.0.8** |
| **Người test** | QA Automation (Chrome DevTools MCP) |
| **Ngày** | 2026-08-06 09:45:00 |
| **Loại test** | Re-verify sau dev fix (FLOW 04) — **lỗi phát hiện NGOÀI phạm vi phiếu** |
| **Round** | Đợt verify bug `Dopai=dev done` + `Trạng thái dev fix=Fixed` |
| **Tài liệu tham chiếu** | `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/` · tiêu chí `../tieuchi/QLNDTVVCG_24.md` + `../tieuchi/QLNDTVVCG_26.md` · bảng `1OKBN2otlmdZ44…` tab `bug` dòng 286 + 287 |

> 🔴 **Hiệu lực:** đo trên **env dev**, không phải env nghiệm thu của đối tác (`htpldn-uat.ospgroup.vn`, bản
> dựng V1.0.3 trong bằng chứng).

---

## Tổng hợp

Hai case của module này trên bảng `bug` — `QLNDTVVCG_24` (dòng 286) và `QLNDTVVCG_26` (dòng 287) — **đều Pass**,
không có bug nào thuộc phạm vi đối tác phản ánh. Toàn bộ **3** bug dưới đây là **lỗi tình cờ phát hiện trong lúc
dựng tiền đề và đo**, nằm ngoài nội dung đối tác nêu, nên **không** kéo verdict của hai case đó và **không** được
ghi vào bảng của đối tác. Cả 3 đã được mở phiếu riêng ở cuối tab `bug`: `QLNDTVVCG_OOS_02` (dòng 360),
`QLNDTVVCG_OOS_03` (dòng 361), `QLNDTVVCG_OOS_04` (dòng 362) — `Trạng thái = Fail`, `Dopai = bug`.

- **Quyền:** tài khoản chỉ có vai trò *Tư vấn viên / Chuyên gia* vẫn phân công được nội dung tư vấn — cả giao
  diện lẫn máy chủ đều cho qua, trong khi đặc tả ghi tác nhân của chức năng này là **Cán bộ Nghiệp vụ**.
- **Thông báo:** bước phân công không sinh thư điện tử, dù đây là bước **duy nhất** trong nhóm có ghi rõ kênh
  *"(in-app + email)"*.
- **Nhật ký:** thao tác chuyên gia từ chối không lưu lý do vào nhật ký, dù đặc tả đòi ghi kèm.

### Severity breakdown

| Tổng | Critical | Major | Medium | Minor | Trivial | Closed | Open |
|------|----------|-------|--------|-------|---------|--------|------|
| 5    | 0        | 1     | 1      | 1     | 2       | 2      | 3    |

## Bug Summary Table

| Bug ID | Severity | Priority | Type | TC Ref | **SRS Reference** | Title | Status |
|--------|----------|----------|------|--------|-------------------|-------|--------|
| BUG-TVCS-PHANCONG-QUYEN | Major | P1 | Permission | `QLNDTVVCG_OOS_02` (dòng 360) — *ngoài phạm vi, phát hiện khi dựng tiền đề `QLNDTVVCG_26`* | `srs-fr-12-tv-chuyen-sau.md:34` · `:97` · `:170` | Tài khoản vai trò Tư vấn viên / Chuyên gia phân công được nội dung tư vấn chuyên sâu | Open |
| BUG-TVCS-PHANCONG-EMAIL | Medium | P3 | Function | `QLNDTVVCG_OOS_03` (dòng 361) — *ngoài phạm vi, phát hiện khi dựng tiền đề `QLNDTVVCG_26`* | `srs-fr-12-tv-chuyen-sau.md:174` | Bước phân công chuyên gia không gửi thư điện tử dù đặc tả ghi rõ kênh in-app + email | Open |
| BUG-TVCS-NHATKY-LYDO | Minor | P3 | Data | `QLNDTVVCG_OOS_04` (dòng 362) — *ngoài phạm vi, phát hiện khi đo `QLNDTVVCG_26`* | `srs-fr-12-tv-chuyen-sau.md:198` | Nhật ký thao tác không lưu lý do khi chuyên gia từ chối phân công | Open |
| ~~BUG-TVCS-XACNHAN-THONGBAO~~ | Minor | P3 | Function | QLNDTVVCG_24 (dòng 286) | `srs-fr-12-tv-chuyen-sau.md:186` · `:184` · `:185` | Doanh nghiệp và cán bộ nghiệp vụ không nhận được thông báo khi chuyên gia xác nhận | Closed |
| ~~BUG-TVCS-TUCHOI-THONGBAO~~ | Minor | P3 | Function | QLNDTVVCG_26 (dòng 287) | `srs-fr-12-tv-chuyen-sau.md:197` · `:195` · `:196` | Cán bộ nghiệp vụ phụ trách không nhận được thông báo kèm lý do khi chuyên gia từ chối | Closed |

---

## BUG-TVCS-PHANCONG-QUYEN — Tài khoản vai trò Tư vấn viên / Chuyên gia phân công được nội dung tư vấn chuyên sâu

> **Re-test:** 2026-08-06 09:41 V1.0.8 (env dev `18.143.165.120.nip.io`) — ❗ **Mới log**, chưa từng được báo.
> Đo 2 đường độc lập: giao diện hiện nút, và máy chủ chấp nhận yêu cầu (HTTP 200, bản ghi đổi trạng thái thật).

### Mô tả

Trên màn **Tư vấn chuyên sâu → Chi tiết**, tài khoản chỉ mang vai trò **Tư vấn viên + Chuyên gia tư vấn**
(`vaiTro = ["TVV","CG"]`, không có vai trò Cán bộ Nghiệp vụ) vẫn **nhìn thấy và dùng được** thao tác **[Phân
công]** trên bản ghi ở trạng thái *Tiếp nhận*. Máy chủ **không** chặn: yêu cầu phân công gửi từ chính tài khoản
này trả về thành công và bản ghi chuyển sang *Phân công* thật, có gán chuyên gia.

Theo đặc tả, chức năng quản lý nội dung tư vấn chuyên sâu (UC147 / FR-X.1-01) chỉ có một tác nhân là **Cán bộ
Nghiệp vụ (TW/BN/ĐP)**, và bước đầu tiên của luồng phân công là *kiểm tra quyền Cán bộ Nghiệp vụ*. Nghĩa là
người dùng vai trò Tư vấn viên / Chuyên gia đang tự phân công được việc cho mình hoặc cho người khác, vượt quyền.

### Các bước tái hiện

1. Đăng nhập bằng tài khoản chỉ có vai trò **Tư vấn viên + Chuyên gia tư vấn** (đợt này dùng `qa_tvvseed28`,
   `BTP · TW`). Xác nhận vai trò qua thông tin phiên: `vaiTro = ["TVV","CG"]`.
2. Mở một bản ghi tư vấn chuyên sâu đang ở trạng thái **Tiếp nhận** thuộc đơn vị của tài khoản
   (đợt này: `TVCS-20260806-0002`).
3. Nhìn thanh hành động cuối màn chi tiết → **[Phân công]** hiện ra.
4. Thực hiện thao tác phân công một chuyên gia cho bản ghi đó.
5. Đọc lại bản ghi để đối chiếu trạng thái và người được phân công.

### Kết quả mong đợi

Theo `srs-fr-12-tv-chuyen-sau.md:34` (*"Tác nhân chính: Cán bộ Nghiệp vụ (TW/BN/ĐP) — UC147/148/150/152"*),
`:97` (*"Tác nhân: Cán bộ Nghiệp vụ (TW/BN/ĐP)"* của FR-X.1-01) và `:170` (bước 1 của luồng phân công:
*"Kiểm tra quyền CB NV và phạm vi đơn vị | BR-AUTH-01, BR-AUTH-08"*): người dùng không mang vai trò Cán bộ
Nghiệp vụ phải bị hệ thống từ chối thao tác phân công, và giao diện không nên mời họ thao tác.

### Kết quả thực tế

- Giao diện **hiện nút [Phân công]** cho tài khoản vai trò Tư vấn viên / Chuyên gia.
- Máy chủ **chấp nhận** yêu cầu phân công gửi từ tài khoản này: trả về **HTTP 200**, bản ghi
  `TVCS-20260806-0002` chuyển từ *Tiếp nhận* sang **Phân công** và được gán chuyên gia thật.
- Không có bất kỳ thông báo từ chối nào ở cả hai tầng.
- Sau phép thử đã **hoàn nguyên** bản ghi về *Tiếp nhận* + gỡ chuyên gia.

### Bằng chứng

- `image/QLNDTVVCG_26-B-sau-tu-choi-ve-Tiepnhan-go-chuyengia-V108.png` — thanh hành động có **[Phân công]** trong
  khi góc phải màn ghi rõ người đang đăng nhập là *"QA TVV Seed28 Active · Tư vấn viên · Chuyên gia tư vấn"*.
- Đường đo thứ hai (máy chủ): yêu cầu phân công gửi bằng chính phiên của tài khoản đó → **200**, đọc lại bản ghi
  thấy `trangThai = PHAN_CONG` + `chuyenGiaId` đã gán. Vai trò phiên đọc từ hệ thống: `vaiTro = ["TVV","CG"]`.

---

## BUG-TVCS-PHANCONG-EMAIL — Bước phân công chuyên gia không gửi thư điện tử dù đặc tả ghi rõ kênh in-app + email

> **Re-test:** 2026-08-06 09:35 V1.0.8 (env dev `18.143.165.120.nip.io`) — ❗ **Mới log**, chưa từng được báo.
> Đo bằng hộp thư giả lập của env, đối chiếu tổng số thư trước/sau và mốc giờ từng thư.

### Mô tả

Khi Cán bộ Nghiệp vụ phân công một nội dung tư vấn chuyên sâu cho chuyên gia, hệ thống có sinh thông báo
**trong ứng dụng** cho chuyên gia, nhưng **không** sinh thư điện tử. Đây là bước **duy nhất** trong nhóm xử lý
của module có ghi rõ kênh *"(in-app + email)"* ngay trong bảng bước xử lý — khác với bước *chuyên gia xác nhận*
(`:186`) và *chuyên gia từ chối* (`:197`) vốn để trống kênh. Vì vậy điểm này **không** thuộc nhóm "đặc tả im
lặng về kênh" đang chờ BA chốt, mà là yêu cầu đã ghi rõ nhưng chưa được đáp ứng.

Hệ quả nghiệp vụ: chuyên gia chỉ biết mình được giao việc khi chủ động mở phần mềm, trong khi chính bước này
gắn với hạn xác nhận **2 ngày làm việc**; quá hạn thì bản ghi tự trả về *Tiếp nhận*.

### Các bước tái hiện

1. Ghi lại **tổng số thư** trong hộp thư giả lập của env (`http://18.143.165.120:8025`).
2. Đăng nhập tài khoản Cán bộ Nghiệp vụ, phân công một chuyên gia cho bản ghi tư vấn chuyên sâu ở trạng thái
   *Tiếp nhận* (đợt này: 2 bản ghi, `TVCS-20260806-0002` và `TVCS-20260803-0003`).
3. Đăng nhập tài khoản chuyên gia được phân công → mở hộp thông báo, xác nhận **có** thông báo trong ứng dụng.
4. Mở lại hộp thư giả lập, đối chiếu tổng số thư và mốc giờ từng thư với mốc giờ phân công.

### Kết quả mong đợi

Theo `srs-fr-12-tv-chuyen-sau.md:174` — bước 5 của *"Processing — Phân công CG"*: *"Gửi thông báo CG/TVV
**(in-app + email)**: nội dung yêu cầu + SLA 2 ngày LV xác nhận | BR-NOTIF-01"* — chuyên gia phải nhận được
thông báo qua **cả hai** kênh.

### Kết quả thực tế

- **Trong ứng dụng: có.** Chuyên gia nhận đúng 2 thông báo *"Bạn được phân công tư vấn: TVCS-20260806-0002"* và
  *"…: TVCS-20260803-0003"*, sinh lúc **02:28:56.544Z** và **02:28:56.641Z** — khớp mốc phân công 02:28:56.
- **Thư điện tử: không.** Tổng số thư trong hộp thư giả lập **không tăng** vì thao tác phân công; thư kế tiếp
  sinh lúc **02:29:28** là **mã đăng nhập** của chính tài khoản chuyên gia, không phải thông báo phân công.
  Toàn đợt đo, mọi thư tăng thêm đều là mã đăng nhập.

### Bằng chứng

- Hộp thư giả lập của env: tổng **1510** trước thao tác; thư mới nhất trước đó lúc **02:16:49** (mã đăng nhập);
  sau 2 lần phân công lúc **02:28:56**, thư kế tiếp là **02:29:28** — mã đăng nhập.
- Thông báo trong ứng dụng của chuyên gia: 2 mục *"Bạn được phân công tư vấn: …"* đúng mốc giây phân công.

---

## BUG-TVCS-NHATKY-LYDO — Nhật ký thao tác không lưu lý do khi chuyên gia từ chối phân công

> **Re-test:** 2026-08-06 09:36 V1.0.8 (env dev `18.143.165.120.nip.io`) — ❗ **Mới log**, chưa từng được báo.
> Đo 2 đường: bảng *Nhật ký thao tác* trên màn chi tiết, và bản ghi nhật ký đọc trực tiếp từ hệ thống.

### Mô tả

Khi chuyên gia từ chối phân công, hệ thống **có** ghi một dòng nhật ký cho thao tác đó, nhưng dòng nhật ký
**không chứa lý do từ chối**: bảng trên màn chỉ hiển thị hành động chung chung *"Cập nhật"* kèm người thực hiện,
còn bản ghi nhật ký đọc trực tiếp từ hệ thống **không có trường nào** mang lý do.

Lý do vẫn còn lưu ở chỗ khác (trường ghi chú của bản ghi và nội dung thông báo gửi Cán bộ Nghiệp vụ), nên chưa
mất dấu hoàn toàn — nhưng nhật ký là nơi đặc tả chỉ định để tra cứu về sau, và hai chỗ kia đều có thể bị ghi đè
bởi lượt phân công / từ chối kế tiếp.

### Các bước tái hiện

1. Cho một bản ghi tư vấn chuyên sâu ở trạng thái **Phân công**.
2. Đăng nhập bằng chuyên gia được phân công, bấm **[Từ chối nhiệm vụ]**, nhập lý do (đợt này: chuỗi 61 ký tự có
   dấu nhận dạng riêng) rồi xác nhận.
3. Mở lại màn chi tiết → mở khối **Nhật ký thao tác** → đọc dòng mới nhất.
4. Đối chiếu bằng đường thứ hai: đọc bản ghi nhật ký của chính bản ghi đó từ hệ thống, liệt kê các trường.

### Kết quả mong đợi

Theo `srs-fr-12-tv-chuyen-sau.md:198` — bước 6 của *"Processing — CG từ chối"*: *"Ghi nhật ký thao tác **(kèm lý
do từ chối)** | BR-DATA-05"* — dòng nhật ký của thao tác từ chối phải mang theo lý do người dùng đã nhập.

### Kết quả thực tế

- Bảng **Nhật ký thao tác** trên màn chi tiết hiển thị: *"06/08/2026 09:31 · **Cập nhật** · QA TVV Seed28 Active
  (qa_tvvseed28) · Chuyên gia tư vấn, Tư vấn viên"* — hành động ghi là *"Cập nhật"*, **không** có cột hay dòng nào
  chứa lý do; bảng cũng không phân biệt được thao tác này với thao tác *chấp nhận*.
- Bản ghi nhật ký đọc trực tiếp từ hệ thống có **18 trường** (loại thực thể, mã thực thể, hành động, người thực
  hiện, thời gian, địa chỉ IP, điểm gọi, mã phản hồi, phiên, phân hệ, họ tên, vai trò, đơn vị…) — **không có**
  trường nào mang lý do / nội dung thay đổi. Giá trị hành động là `UPDATE`.

### Bằng chứng

- Bảng *Nhật ký thao tác* của bản ghi `TVCS-20260803-0003`, dòng mới nhất **06/08/2026 09:31 · Cập nhật**.
- Bản ghi nhật ký tương ứng (`thoiGian = 2026-08-06T02:31:47.124Z`, `hanhDong = "UPDATE"`,
  `nguoiThucHienUsername = "qa_tvvseed28"`, `responseCode = 200`) — danh sách trường không có mục nào cho lý do.
- Đối chứng cho thấy lý do **có** được lưu ở nơi khác: nội dung thông báo gửi Cán bộ Nghiệp vụ có đoạn
  *"Lý do: QA FLOW04 QLNDTVVCG_26 - ly do tu choi ban ghi B luc 20260806"* — xem
  `image/QLNDTVVCG_26-F-CBNV-tao-banghi-khac-nguoi-phancong-van-nhan-thongbao-V108.png`.

---

## ~~BUG-TVCS-XACNHAN-THONGBAO~~ [CLOSED] — Doanh nghiệp và cán bộ nghiệp vụ không nhận được thông báo khi chuyên gia xác nhận

> **Re-test:** 2026-08-06 09:18 V1.0.8 (env dev `18.143.165.120.nip.io`) — ✅ **Pass** (Closed-verified).
> Thông báo trong ứng dụng đã có cho **cả hai** đối tượng, sinh đúng mốc giây bấm chấp nhận và trỏ đúng mã bản
> ghi; bản ghi sang *Đang tư vấn* có ngày bắt đầu và có tạo phiên tư vấn mới.
> N = 2 bản ghi · M = 1/2 dạng (dạng "người được phân công là tư vấn viên" **không tồn tại được** — hệ thống chỉ
> nhận loại chuyên gia) · seed: 1 bản ghi mới `TVCS-20260806-0001` + phân công/chấp nhận trên `TVCS-20260725-0005`.

### Mô tả

Sau khi chuyên gia được phân công bấm **[Chấp nhận]** trên màn *Tư vấn chuyên sâu → Chi tiết*, đối tác phản ánh
doanh nghiệp và cán bộ nghiệp vụ phụ trách **không nhận được thông báo** nào về việc này. Triệu chứng **không còn
tái hiện** trên bản dựng V1.0.8.

### Các bước tái hiện

Xem khối **CÁCH VERIFY** ở cuối entry — giống từng chữ với ô note của dòng 286.

### Kết quả mong đợi

Theo `srs-fr-12-tv-chuyen-sau.md:186` — bước 6 của *"Processing — CG xác nhận"*: *"Gửi thông báo DN + CB NV: CG
đã xác nhận | BR-NOTIF-01"*; kèm `:184` (*đổi trạng thái → DANG_TU_VAN, ghi `ngay_bat_dau` = NOW()*) và `:185`
(*tạo PHIEN_TU_VAN mới liên kết với bản ghi TVCS*).

### Kết quả thực tế

- Doanh nghiệp `0109998887` nhận *"Chuyên gia đã xác nhận tư vấn: TVCS-20260725-0005"* — sinh **02:11:23.083Z**,
  sau mốc bấm **02:11:23.0Z**.
- Cán bộ nghiệp vụ `cbnv_tw` nhận *"Chuyên gia đã xác nhận tư vấn: TVCS-20260806-0001"* — sinh **02:16:32.537Z**,
  sau mốc bấm **02:16:32.4Z**.
- Cả 2 bản ghi sang *Đang tư vấn* có ghi ngày bắt đầu; phiên tư vấn mới được tạo cùng mốc giây.
- Còn tồn (**không** kéo verdict, đã tách sang phiếu hỏi BA): chỉ có thông báo trong ứng dụng, **không** có thư
  điện tử — đặc tả không chốt kênh cho sự kiện này.

### Bằng chứng

- `image/QLNDTVVCG_24-A-CG-vua-chap-nhan-TVCS0005-dangtuvan-V108.png`
- `image/QLNDTVVCG_24-B-DN-nhan-thong-bao-CG-da-xac-nhan-V108.png`
- `image/QLNDTVVCG_24-C-CBNV-nhan-thong-bao-CG-da-xac-nhan-V108.png`
- Tiêu chí + bảng điều kiện đã điền: `../tieuchi/QLNDTVVCG_24.md`

```
── CÁCH VERIFY sau Dev fix ──
Precondition: chuyên gia `qa_tvvseed28` (Test@1234) + màn Tư vấn chuyên sâu → Chi tiết
  https://18.143.165.120.nip.io/tv-chuyen-sau/{id}.
  Cần MỘT bản ghi ở trạng thái "Phân công", người được phân công là chính tài khoản này, và bản ghi
  phải DO CHÍNH cán bộ nghiệp vụ mà mình sẽ đi kiểm thông báo TẠO RA.
  Chưa có thì tự dựng (tiền đề TẠO ĐƯỢC, không phải blocker):
    a) đăng nhập `cbnv_tw` (Test@1234) → Tư vấn chuyên sâu → tạo nội dung tư vấn mới, chọn
       doanh nghiệp `0109998887` (tài khoản DN này dùng để kiểm vế "DN có nhận thông báo không");
    b) vẫn tài khoản đó → [Phân công] → chọn `qa_tvvseed28` → lưu.
1) Ghi lại mã bản ghi + mốc giờ, rồi bấm [Chấp nhận] → xác nhận trong hộp thoại.
2) Đọc lại bản ghi: trạng thái, ngày bắt đầu, và phiên tư vấn mới có được tạo không.
3) Đăng nhập tài khoản doanh nghiệp của bản ghi → mở chuông thông báo → đối chiếu mã + mốc giờ.
4) Đăng nhập cán bộ nghiệp vụ ĐÃ TẠO bản ghi → mở chuông → đối chiếu mã + mốc giờ.
✅ PASS khi: bản ghi sang "Đang tư vấn" có ghi ngày bắt đầu, VÀ cả doanh nghiệp lẫn cán bộ nghiệp vụ
   đều có thông báo mới sinh SAU mốc bấm và trỏ ĐÚNG mã bản ghi đó.
❌ FAIL nếu: một trong hai bên không có thông báo tương ứng, hoặc thông báo trỏ sai mã, hoặc sinh
   trước mốc bấm, hoặc bản ghi không đổi trạng thái.
⚠️ Đừng chấm Fail khi cán bộ nghiệp vụ không thấy gì mà chưa kiểm AI LÀ NGƯỜI TẠO bản ghi — thông báo
   đi tới người tạo, không đi tới người phân công. Đo trên bản ghi do người khác tạo sẽ cho kết quả sai.
⚠️ Đừng chấm Fail vì không có thư điện tử — đặc tả không chốt kênh cho sự kiện này, đang chờ BA.
⚠️ Đừng dựng dạng "người được phân công là tư vấn viên" — hệ thống chỉ nhận người loại chuyên gia.
```

---

## ~~BUG-TVCS-TUCHOI-THONGBAO~~ [CLOSED] — Cán bộ nghiệp vụ phụ trách không nhận được thông báo kèm lý do khi chuyên gia từ chối

> **Re-test:** 2026-08-06 09:36 V1.0.8 (env dev `18.143.165.120.nip.io`) — ✅ **Pass** (Closed-verified).
> Cán bộ nghiệp vụ phụ trách nhận thông báo trong ứng dụng trong vòng **38 ms / 30 ms** sau thao tác, trỏ đúng mã
> bản ghi và **có kèm lý do từ chối**; bản ghi về *Tiếp nhận* + gỡ liên kết chuyên gia; bỏ trống lý do bị chặn.
> N = 2 bản ghi · M = 2/2 dạng (người tạo = người phân công; người tạo ≠ người phân công) · seed: phân công +
> từ chối trên `TVCS-20260806-0002` và `TVCS-20260803-0003`.

### Mô tả

Sau khi chuyên gia được phân công nhập lý do và bấm **[Từ chối nhiệm vụ]**, đối tác phản ánh hệ thống **không gửi
thông báo tới cán bộ nghiệp vụ phụ trách kèm lý do từ chối**. Triệu chứng **không còn tái hiện** trên bản dựng
V1.0.8.

### Các bước tái hiện

Xem khối **CÁCH VERIFY** ở cuối entry — giống từng chữ với ô note của dòng 287.

### Kết quả mong đợi

Theo `srs-fr-12-tv-chuyen-sau.md:197` — bước 5 của *"Processing — CG từ chối"*: *"Gửi thông báo CB NV: CG từ
chối, cần phân công lại | BR-NOTIF-01"*; kèm `:195` (*yêu cầu lý do từ chối — bắt buộc*) và `:196` (*xóa liên kết
`chuyen_gia_id`, trạng thái → TIEP_NHAN*).

### Kết quả thực tế

- Bản ghi A `TVCS-20260806-0002` (người tạo = người phân công = `cbnv_tw`): thông báo *"Chuyên gia từ chối phân
  công: TVCS-20260806-0002"* sinh **02:30:46.157Z**, sau mốc bấm **02:30:46.119Z**.
- Bản ghi B `TVCS-20260803-0003` (người tạo `cbnv_tw_04` ≠ người phân công `cbnv_tw`): thông báo sinh
  **02:31:47.138Z**, sau mốc bấm **02:31:47.108Z**, **vào hộp của người tạo**.
- Nội dung thông báo **có kèm lý do**: *"Mã: … Chuyên gia đã từ chối, cần phân công lại. **Lý do:** …"*.
- Cả 2 bản ghi về `TIEP_NHAN` với `chuyenGiaId = null`; giao diện hiện *Tiếp nhận* / *Chưa phân công*.
- Bỏ trống lý do → bị chặn (*"Vui lòng nhập lý do từ chối"* + *"Lý do phải có ít nhất 10 ký tự"*), bản ghi giữ nguyên.
- Còn tồn (**không** kéo verdict, đã tách sang phiếu hỏi BA): sau khi từ chối màn hình ở nguyên trang *Chi tiết*,
  không tự quay về danh sách; và chỉ có thông báo trong ứng dụng, không có thư điện tử.

### Bằng chứng

- `image/QLNDTVVCG_26-A-tu-choi-bo-trong-ly-do-bi-chan-V108.png`
- `image/QLNDTVVCG_26-B-sau-tu-choi-ve-Tiepnhan-go-chuyengia-V108.png`
- `image/QLNDTVVCG_26-D-CBNV-nguoi-tao-nhan-thong-bao-CG-tu-choi-V108.png`
- `image/QLNDTVVCG_26-E-noi-dung-thong-bao-co-kem-ly-do-tu-choi-V108.png`
- `image/QLNDTVVCG_26-F-CBNV-tao-banghi-khac-nguoi-phancong-van-nhan-thongbao-V108.png`
- Tiêu chí + bảng điều kiện đã điền (GAP = 0): `../tieuchi/QLNDTVVCG_26.md`

```
── CÁCH VERIFY sau Dev fix ──
Precondition: chuyên gia `qa_tvvseed28` (Test@1234) + màn Tư vấn chuyên sâu → Chi tiết
  https://18.143.165.120.nip.io/tv-chuyen-sau/{id}.
  Cần MỘT bản ghi ở trạng thái "Phân công", người được phân công là chính tài khoản này, và bản ghi
  phải DO CHÍNH cán bộ nghiệp vụ mà mình sẽ đi kiểm thông báo TẠO RA.
  Chưa có thì tự dựng (tiền đề TẠO ĐƯỢC, không phải blocker):
    a) đăng nhập `cbnv_tw` (Test@1234) → Tư vấn chuyên sâu → tạo nội dung tư vấn mới;
    b) vẫn tài khoản đó → [Phân công] → chọn `qa_tvvseed28` → lưu.
1) Bấm [Từ chối nhiệm vụ], BỎ TRỐNG lý do rồi bấm [Từ chối]: ghi lại có bị chặn không, và đọc lại
   bản ghi xem trạng thái có đổi không.
2) Nhập lý do ≥10 ký tự có chuỗi nhận dạng riêng, ghi lại mốc giờ, rồi bấm [Từ chối].
3) Đọc lại bản ghi: trạng thái + ô Chuyên gia.
4) Đăng nhập cán bộ nghiệp vụ ĐÃ TẠO bản ghi → mở chuông → mở màn Thông báo đọc nội dung đầy đủ →
   đối chiếu mã bản ghi, mốc giờ, và chuỗi lý do đã nhập ở bước 2.
✅ PASS khi: bỏ trống lý do thì bị chặn và bản ghi giữ nguyên; nhập lý do thì bản ghi về "Tiếp nhận"
   với ô Chuyên gia thành "Chưa phân công"; VÀ cán bộ nghiệp vụ có thông báo mới sinh SAU mốc bấm,
   trỏ ĐÚNG mã bản ghi.
❌ FAIL nếu: bỏ trống lý do vẫn đi qua · bản ghi không về "Tiếp nhận" · chuyên gia vẫn còn gắn ·
   cán bộ nghiệp vụ không có thông báo tương ứng · thông báo trỏ sai mã hoặc sinh trước mốc bấm.
⚠️ Đừng chấm Fail khi cán bộ nghiệp vụ không thấy gì mà chưa kiểm AI LÀ NGƯỜI TẠO bản ghi — thông báo
   đi tới người tạo, không đi tới người phân công.
⚠️ Đừng chấm Fail vì thông báo trên màn không đúng một câu chữ cụ thể, hoặc vì màn hình không tự quay
   về danh sách — đặc tả im lặng cả hai điểm, đang chờ BA. Nhưng nếu thông báo báo SAI BẢN CHẤT hành
   động (bấm Từ chối mà báo "Đã xác nhận") thì phải log riêng.
⚠️ Đừng chấm Fail vì không có thư điện tử — đặc tả không chốt kênh cho sự kiện này, đang chờ BA.
```
