# QLHDTVVCG_09 — dòng 315 · 07/08/2026 17:33–17:35 · tài khoản **`cbnv_tw_04`** (CB NV TW, Cục Bổ trợ tư pháp - Bộ Tư pháp) · bản dựng `assets/index-BbPPdate.js` (`last-modified` Fri, 07 Aug 2026 06:47:57 GMT · `etag "6a757f9d-428"`)

> Chuẩn chấm khóa: [`chuan/QLHDTVVCG_09.md`](../chuan/QLHDTVVCG_09.md) — **5 vế: C1 `MATCH` · C2 `GAP` · C3 `MATCH` · C4 `GAP` · C5 `MATCH`**.
> Luật ghi lô H1 §2: vế `GAP` **không chặn** `Test done`.
> Đọc lại dòng 315 lúc 17:32: `Trạng thái` `N/R` · `Kết quả thực tế` RỖNG · `R` = `Fixed` · `T` RỖNG · `U` RỖNG.
> Ô `DEV phản hồi lần 1` (S): *"… Phần nội dung chức năng Dev đã bổ sung theo SRS: **màn Chi tiết hợp đồng dựng đủ các nhóm thông tin**."* ⇒ bề mặt chấm = **màn Chi tiết hợp đồng** (`/hop-dong-tv/{id}`), đúng bước J *"Nhấn Xem chi tiết"*.

## Đường vào

Sidebar **Vụ việc HTPL** → tìm `VV-BTP-TW-20260804-002` → [Xem vụ việc] → bung **"HĐ tư vấn liên kết"** →
dòng `HDTV-20260807-0006` → **[Xem chi tiết]** → `/hop-dong-tv/d16487f4-3ccc-4629-8e07-bb63ea9a12be` → thẻ **"Vụ việc liên kết"** (Nhóm 2).
Bước J ghi *"Chọn menu Hợp đồng Tư vấn"* — menu đã bỏ theo `:266`/`:268`, là **tiền đề**, không phải vế chấm.

**Tiền đề đắt nhất của phiếu đã có sẵn — không phải seed:** HĐ-1 `HDTV-20260807-0006` đang có **3 vụ việc liên kết**
(`VV-BTP-TW-20260804-002/-003/-004`, do phiếu `_15` tạo), trong đó **Tên DN 41 ký tự (>40)** — đủ chất để đo C3/C5 và ghi hiện trạng C4.
⇒ **Không phụ thuộc phiếu `_22`** (phiếu `_22` đã bị bỏ qua vì ô `R` = `UAT done`, xem bàn giao); ràng buộc thứ tự `_22` → `_09` chỉ nhằm bảo đảm có liên kết, điều kiện đó đã thoả sẵn.

## Kết quả từng vế

| Vế | Quan hệ | Kỳ vọng phiếu | Web thực tế (số liệu quyết định) | Đạt? |
|---|---|---|---|---|
| **C1** | MATCH | Đủ các cột đặc tả khai cho Nhóm 2 — `:291`: Mã VV / Tên DN / Lĩnh vực / Trạng thái / `[Bỏ liên kết]`, kèm nút `[+ Liên kết VV]` | **Đường 1 (giao diện, `innerText`)** — bảng "Vụ việc liên kết" có **5 tiêu đề cột**: `Mã vụ việc` · `Tiêu đề` · `Doanh nghiệp` · `Lĩnh vực` · `Trạng thái`, **3 dòng dữ liệu**. ⇒ **đủ 4/4 cột dữ liệu** mà `:291` khai (Tên DN ↔ cột `Doanh nghiệp`), **thừa 1 cột** `Tiêu đề`. **Đường 2 (đối chứng độc lập)** — `GET /api/v1/hop-dong-tu-vans/d16487f4-…` → `vuViecLienKets` có **đúng 3** phần tử, mã lần lượt `VV-BTP-TW-20260804-002` · `-003` · `-004`, **trùng khít** 3 dòng đang hiện ⇒ bảng render đúng tập liên kết thật của bản ghi, không phải dữ liệu tĩnh | ✅ |
| **C2** | GAP | *"giống với **thiết kế**"* ở mức bố cục/thứ tự/kiểu control | **Không chấm** (chuẩn đo `MH-14.1` không tồn tại trong nguồn chuẩn). **Hiện trạng để BA quyết (vế Z):** Nhóm 2 dựng thành **thẻ riêng "Vụ việc liên kết"** xếp ngay dưới thẻ "Thông tin hợp đồng", dạng bảng 5 cột không phân trang, thứ tự cột như trên | — (không chấm) |
| **C3** | MATCH | Dữ liệu đúng định dạng: Mã VV đúng khuôn, **Trạng thái là nhãn tiếng Việt** đúng bảng §B, **Lĩnh vực là TÊN** (không phải mã) | **Đường 1** — dòng 1: `VV-BTP-TW-20260804-002` · `Cong ty QA R3 kiem trang thai sau dang ky` · `Thuế` · **`Đã tiếp nhận`**; cả 3 dòng cùng khuôn `VV-{đơn vị}-{YYYYMMDD}-{SEQ}` với phần ngày `20260804` + số thứ tự `002/003/004` (`srs-fr-05-vu-viec.md:1648`), hiển thị **nguyên vẹn** đúng mã do module Vụ việc sinh (đối chiếu chính chuỗi này trên màn danh sách Vụ việc lúc 17:29). **Đường 2 (đối chứng độc lập)** — đọc thẳng bản ghi vụ việc `GET /api/v1/vu-viecs/6bf98a2e-…` → 200: giá trị **thô** là `trangThai` = **`DA_TIEP_NHAN`** và `linhVucPhapLyId` = **`bbbbbbbb-0000-4000-8000-000000000018`** (UUID). Màn hiện `Đã tiếp nhận` và `Thuế` ⇒ **có lớp dịch mã DB → nhãn** (đúng `srs-fr-05-vu-viec.md:1498`) và **có tra Danh mục lấy TÊN lĩnh vực** (đúng `:1650`), không đổ mã/UUID ra màn | ✅ |
| **C4** | GAP | *"không bị tràn/đè lên nhau"* | **Không chấm** (đặc tả im lặng về tràn/đè bố cục). **Hiện trạng để BA quyết (vế Z):** ở **1440×900**, bảng **không** có thanh cuộn ngang, trang **không** tràn ngang. Hai cột dài (`Tiêu đề` 36–40 ký tự · `Doanh nghiệp` **41 ký tự**) bị **cắt bằng dấu `…`** (`scrollWidth` 303–329 > `clientWidth` 293) **và đều có tooltip** — thuộc tính `title` đọc được là **nguyên văn đầy đủ** `Cong ty QA R3 kiem trang thai sau dang ky` ⇒ **đúng** quy ước cắt + tooltip `srs-fr-05-vu-viec.md:1571`, **không** phát sinh "bug mới tự lộ" | — (không chấm) |
| **C5** | MATCH | Đồng nhất ngôn ngữ hiển thị — không mã DB, không lẫn tiếng Anh | **Đường 1** — quét `innerText` toàn thẻ Nhóm 2: **0** nhãn/giá trị hệ thống ở dạng mã DB; chuỗi duy nhất khớp mẫu `SNAKE_CASE` là **`QLHSVV_07`** nằm trong **tiêu đề vụ việc do QA tự đặt** (`QLHSVV_07 120 baseline …`), không phải nhãn hệ thống; **0** chuỗi tiếng Anh / `null` / `undefined`. Tiêu đề cột và giá trị Trạng thái đều tiếng Việt. **Đường 2 (đối chứng)** — máy chủ trả `trangThai` thô `DA_TIEP_NHAN` cho cả 3 dòng, màn hiện `Đã tiếp nhận` ⇒ chứng minh lớp dịch nhãn tồn tại thật | ✅ |

**Chống Pass oan đã làm:** **không** chấm bằng bảng rỗng — bảng có **3 dòng dữ liệu thật** nên C3/C4/C5 đo được trên dữ liệu; so **mã từng dòng** với danh sách liên kết đọc lại từ máy chủ (không chỉ so số lượng); C3/C5 chứng minh bằng **chênh lệch giữa giá trị thô của máy chủ và chuỗi hiển thị** (`DA_TIEP_NHAN` → `Đã tiếp nhận`, UUID lĩnh vực → `Thuế`) — nếu màn chỉ in thẳng dữ liệu thô thì phép so này sẽ lộ ngay; đọc bằng `innerText`, không `textContent`; ghi rõ **đã đo mã trạng thái nào** (`DA_TIEP_NHAN`) và **không** mở rộng thành ma trận 12 trạng thái (luật khóa 4).

**Chống Fail oan đã kiểm:** **không** Fail C1 vì màn xem chi tiết thiếu cột hành động `[Bỏ liên kết]` và thiếu nút `[+ Liên kết VV]` — `:291` khai hai thứ đó cho **trang thêm/sửa** (*"trang thêm/sửa — chỉ CB NV"*), còn **trang xem chi tiết thì đặc tả không khai bảng thành phần nào** (chỉ nhắc ở `:294`–`:295`) ⇒ đưa vào câu hỏi BA gộp §5.4, không Fail; **không** Fail vì bảng có **thêm** cột `Tiêu đề` (đặc tả liệt kê cột bắt buộc có, không cấm thêm); **không** Fail vì Tên DN bị cắt cụt (cắt + tooltip là **đúng** `:1571`, chỉ sai khi cắt mà không có tooltip — đã kiểm là **có** tooltip đầy đủ); **không** chấm theo bản vẽ Figma/ảnh đối tác (lý do C2 khóa `GAP`).

## Verdict → ô R

**`Test done`** — **3/3 vế `MATCH` (C1, C3, C5) đều đạt**; 2 vế `GAP` (C2, C4) chỉ ghi hiện trạng, theo luật lô H1 **không chặn** `Test done`.

> Không viết *"fix đã có tác dụng"*: phiếu chưa từng chạy (`N/R`), không có ảnh lỗi cũ ⇒ chỉ kết luận **hiện trạng**.

## Dữ liệu đã đổi

**KHÔNG có.** Phiếu chỉ đọc. `version` của `HDTV-20260807-0006` giữ nguyên **1**; 3 liên kết vụ việc giữ nguyên. Không đụng dữ liệu đối tác.

## Ảnh

Không chụp — mọi vế `MATCH` đều đạt, không có FAIL cần chứng minh (flow 04 §7).
