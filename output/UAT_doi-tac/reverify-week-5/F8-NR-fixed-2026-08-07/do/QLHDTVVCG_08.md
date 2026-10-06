# QLHDTVVCG_08 — dòng 314 · 07/08/2026 17:29–17:31 · tài khoản **`cbnv_tw_04`** (CB NV TW, Cục Bổ trợ tư pháp - Bộ Tư pháp) · bản dựng `assets/index-BbPPdate.js` (`last-modified` Fri, 07 Aug 2026 06:47:57 GMT · `etag "6a757f9d-428"`)

> Chuẩn chấm khóa: [`chuan/QLHDTVVCG_08.md`](../chuan/QLHDTVVCG_08.md) — **5 vế: C1 `MATCH` · C2 `GAP` · C3 `MATCH` · C4 `GAP` · C5 `MATCH`**.
> Luật ghi lô H1 ([`H1-LUAT-GHI-2026-08-07.md`](../H1-LUAT-GHI-2026-08-07.md) §2): vế `DIFF`/`GAP` **không chặn** `Test done`; ô R chỉ nhận `Test done`/`Reopen`.
> Đọc lại dòng 314 lúc 17:28: `Trạng thái` `N/R` · `Kết quả thực tế` RỖNG · `R` = `Fixed` · `T` RỖNG · `U` RỖNG — không có phiên khác vừa ghi.
> Ô `DEV phản hồi lần 1` (S) chốt hướng đo: *"BA chốt 06/08/2026 … Loại 4 hướng A: giữ quyết định BA 11/05/2026 bỏ menu riêng … Phần nội dung chức năng Dev đã bổ sung theo SRS: **màn Chi tiết hợp đồng dựng đủ các nhóm thông tin**."* ⇒ bề mặt chấm = **màn Chi tiết hợp đồng** (`/hop-dong-tv/{id}`), đúng bước J *"Nhấn Xem chi tiết"*.

## Đường vào

Sidebar **Vụ việc HTPL** → ô tìm kiếm nhập `VV-BTP-TW-20260804-002` → [Tìm kiếm] (1/1 kết quả) → [Xem vụ việc]
→ bung mục **"HĐ tư vấn liên kết"** (Màn 1, bảng *1-2 / 2 mục*) → dòng `HDTV-20260807-0006` → nút **[Xem chi tiết]**
→ `https://18.143.165.120.nip.io/hop-dong-tv/d16487f4-3ccc-4629-8e07-bb63ea9a12be`.

Bước J ghi *"Chọn menu Hợp đồng Tư vấn"* — menu đã bỏ theo `srs-fr-14-hop-dong-tv.md:266`/`:268`; đây là **tiền đề**, không phải vế chấm, không log lỗi.

**Màn đã chấm:** **trang xem chi tiết hợp đồng**, KHÔNG phải trang thêm/sửa. Nhóm 1 trên màn này là thẻ **"Thông tin hợp đồng"**.
Bản ghi đo: `HDTV-20260807-0006` (`id` `d16487f4-3ccc-4629-8e07-bb63ea9a12be`) — hợp đồng "đầy đủ trường" do phiếu `_15` tạo, có cả 3 trường **không bắt buộc** (Nội dung · Ghi chú · tệp đính kèm) nên đo được đủ C1/C3.

## Kết quả từng vế

| Vế | Quan hệ | Kỳ vọng phiếu | Web thực tế (số liệu quyết định) | Đạt? |
|---|---|---|---|---|
| **C1** | MATCH | Đủ các trường đặc tả khai cho Nhóm 1 — 10 mục ở `:290` (Mã / Tên / Bên A / Bên B / Giá trị / Thời hạn bắt đầu / Thời hạn kết thúc / Nội dung / Ghi chú / File đính kèm) | **Đường 1 (giao diện, `innerText`)** — thẻ "Thông tin hợp đồng" có **13 nhãn**: `Mã hợp đồng` · `Số hợp đồng` · `Tên hợp đồng` · `Bên A` · `Bên B` · `Giá trị hợp đồng` · `Ngày ký` · `Ngày bắt đầu` · `Ngày kết thúc` · `Vụ việc liên kết` · `Trạng thái` · `Nội dung` · `Ghi chú`. **9/10 mục của `:290` nằm trong thẻ này**; mục thứ 10 (**File đính kèm**) có mặt trên **cùng màn** ở thẻ riêng **"Tài liệu đính kèm"** — hiện `phu-luc-hop-dong.pdf (1.2 KB)` + nút `Xem` ⇒ **đủ 10/10**. **Đường 2 (đối chứng độc lập)** — `GET /api/v1/hop-dong-tu-vans/d16487f4-…` → 200, từng giá trị khớp chuỗi đang hiện: `maHopDong` `HDTV-20260807-0006` · `benA` `Cục Bổ trợ tư pháp - Bộ Tư pháp` · `benB` `Chuyên gia UAT QLNDTVVCG 38` · `noiDung`/`ghiChu` trùng từng chữ · `fileDinhKem[0].tenFile` `phu-luc-hop-dong.pdf`, `dungLuong` 1248 byte ⇒ biểu mẫu nạp **đúng bản ghi vừa bấm**, không phải dữ liệu sót của màn trước | ✅ |
| **C2** | GAP | *"giống với **thiết kế**"* ở mức bố cục/thứ tự/kiểu control | **Không chấm** (chuẩn đo `MH-14.1` không tồn tại trong nguồn chuẩn). **Hiện trạng để BA quyết (vế Z):** trang chi tiết dựng theo dạng `ant-descriptions` 2 cột, thứ tự Mã · Số HĐ · Tên (trải hết chiều ngang) · Bên A · Bên B · Giá trị · Ngày ký · Ngày bắt đầu · Ngày kết thúc · Vụ việc liên kết · Trạng thái · Nội dung · Ghi chú; các nhóm con là các thẻ rời xếp dọc bên dưới (Vụ việc liên kết · Tài liệu đính kèm · Mốc tiến độ · Thanh toán giai đoạn · Nhật ký hoạt động) | — (không chấm) |
| **C3** | MATCH | Dữ liệu đúng định dạng: tiền VND (`:151`), ngày `dd/mm/yyyy` (`:152`, `:153`), không lộ mã DB | **Đường 1** — `Giá trị hợp đồng` = **`250.000.000 VNĐ`** (dấu chấm nhóm 3 chữ số + đơn vị); `Ngày bắt đầu` = **`07/08/2026`**, `Ngày kết thúc` = **`25/08/2026`** (đủ `dd/mm/yyyy`); hai trường rỗng (`Số hợp đồng`, `Ngày ký`) hiện **`—`**, không hiện `null`. **Đường 2 (đối chứng)** — giá trị thô từ máy chủ là `giaTriHopDong` = **`"250000000.00"`**, `ngayBatDau` = **`"2026-08-07"`**, `ngayKetThuc` = **`"2026-08-25"`**, `soHopDong` = `null`, `ngayKy` = `null` ⇒ chuỗi hiển thị **không phải** giá trị thô, tức có lớp định dạng thật; hai đường khớp | ✅ |
| **C4** | GAP | *"không bị tràn/đè lên nhau"* | **Không chấm** (đặc tả im lặng về tràn/đè bố cục). **Hiện trạng để BA quyết (vế Z):** ở cửa sổ **1440×900**, đếm bằng máy: **0/13** ô nội dung có `scrollWidth > clientWidth` (không ô nào bị cắt), `document.scrollWidth == clientWidth` ⇒ **không có thanh cuộn ngang**, không quan sát thấy chồng lấn | — (không chấm) |
| **C5** | MATCH | Đồng nhất ngôn ngữ hiển thị — không mã DB, không lẫn tiếng Anh | **Đường 1** — quét `innerText` toàn thẻ Nhóm 1: **0** chuỗi mã DB kiểu `SNAKE_CASE` (chuỗi duy nhất khớp mẫu là `QLHDTVVCG_15` nằm **trong nội dung ghi chú do QA tự nhập**, không phải nhãn hệ thống); **0** chuỗi tiếng Anh / `null` / `undefined`; nhãn trạng thái hiện **`Đang thực hiện`**. **Đường 2 (đối chứng)** — máy chủ trả `trangThai` = **`DANG_THUC_HIEN`** ⇒ chứng minh có **lớp dịch mã DB → nhãn tiếng Việt** đúng `srs-fr-05-vu-viec.md:1492`, không phải giao diện gán cứng chữ tiếng Việt | ✅ |

**Chống Pass oan đã làm:** không chấm bằng danh sách nhãn suông — mỗi trường đều so **giá trị** với bản ghi đọc lại từ máy chủ (loại ca "có nhãn nhưng ô rỗng" và ca "biểu mẫu nạp nhầm bản ghi"); chọn bản ghi **có đủ 3 trường không bắt buộc** (Nội dung/Ghi chú/tệp) nên C3 không chỉ đo phần bắt buộc; đọc bằng `innerText` (không `textContent`) để loại node ẩn AntD; C5 chứng minh bằng **chênh lệch** giữa mã thô của máy chủ và nhãn hiển thị, không phải bằng cảm nhận "trông tiếng Việt".

**Chống Fail oan đã kiểm:** không Fail vì màn có **thêm** `Số hợp đồng` · `Ngày ký` · `Vụ việc liên kết` · `Trạng thái` ngoài `:290` (chính đặc tả khai `so_hop_dong` `:385` và `ngay_ky` `:390` ở phần thực thể ⇒ thừa trường là ghi nhận cho BA); không Fail vì **File đính kèm** nằm ở thẻ riêng thay vì trong khối Thông tin chung (đặc tả **không** khai bảng thành phần cho trang xem chi tiết, chỉ khai cho trang thêm/sửa `:290`); không Fail vì hai trường rỗng hiện `—`; không Fail theo bản vẽ Figma/ảnh đối tác (chính là lý do C2 khóa `GAP`).

## Verdict → ô R

**`Test done`** — **3/3 vế `MATCH` (C1, C3, C5) đều đạt**; 2 vế `GAP` (C2, C4) chỉ ghi hiện trạng, theo luật lô H1 **không chặn** `Test done`.

> Không viết *"fix đã có tác dụng"*: phiếu chưa từng chạy (`Trạng thái` = `N/R`), không có ảnh lỗi cũ ⇒ chỉ kết luận **hiện trạng đúng so với đặc tả**.

## Dữ liệu đã đổi

**KHÔNG có.** Phiếu chỉ đọc. Không tạo/sửa/xóa bản ghi nào; `version` của `HDTV-20260807-0006` giữ nguyên **1** trước và sau lượt đo. Không đụng dữ liệu đối tác.

## Ảnh

Không chụp — mọi vế `MATCH` đều đạt, không có FAIL cần chứng minh (flow 04 §7: chỉ chụp khi quan sát cho thấy FAIL). Số liệu quyết định đã ghi thẳng trong bảng trên.
