# QLHDTVVCG_18 — dòng 324 · 07/08/2026 18:04–18:07 · tài khoản **`cbnv_tw_04`** (CB NV TW, Cục Bổ trợ tư pháp - Bộ Tư pháp) · bản dựng `assets/index-BbPPdate.js` (`last-modified` Fri, 07 Aug 2026 06:47:57 GMT · `etag "6a757f9d-428"`)

> Chuẩn chấm khóa: [`chuan/QLHDTVVCG_18.md`](../chuan/QLHDTVVCG_18.md) — **2 vế: C1 `MATCH` · C2 `MATCH`** (không có vế `DIFF`/`GAP`).
> Đọc lại dòng 324 lúc 18:03: `Trạng thái` `N/R` · `Kết quả thực tế` RỖNG · `R` = `Fixed` · `T` RỖNG · `U` RỖNG.
> Ô `DEV phản hồi lần 1` (S): *"…Dev đã bổ sung theo SRS: **chuẩn hóa thông báo chặn xóa hợp đồng khi còn vụ việc liên kết**."* ⇒ đúng nội dung 2 vế phải đo.
> Cột K nguyên văn: *"Hệ thống **chặn thao tác** và hiển thị thông báo **"Không thể xóa hợp đồng đang có vụ việc liên kết"**"*.

## Đường vào

`/hop-dong-tv/d16487f4-3ccc-4629-8e07-bb63ea9a12be` (HĐ-1 `HDTV-20260807-0006`) → nút **[Xóa]** ở cuối trang chi tiết → hộp xác nhận → **[Xóa]**.
Bước J ghi *"Chọn menu Hợp đồng Tư vấn"* — menu đã bỏ theo `:266`/`:268`, là **tiền đề**, không phải vế chấm.

## Tiền đề đã xác nhận TRƯỚC khi bấm (bắt buộc — dùng nhầm hợp đồng sạch liên kết sẽ cho kết quả ngược)

| Đường | Số liệu |
|---|---|
| **Giao diện** — thẻ "Vụ việc liên kết" trên trang chi tiết | **3** dòng: `VV-BTP-TW-20260804-002` · `-003` · `-004` |
| **Máy chủ** — `GET /api/v1/hop-dong-tu-vans/d16487f4-…` | `vuViecLienKets` có **đúng 3** phần tử, **cùng 3 mã** như trên; `version` = **10**; **không** có trường nào mang nghĩa đã xóa (quét toàn bộ khóa khớp `delet|xoa` = **rỗng**) |

Nút **[Xóa]** ở trạng thái **bấm được** (không mờ, không ẩn) ⇒ đo được cả C1 lẫn C2 (chuẩn chấm §d: nếu nút bị vô hiệu thì không có thông báo, phải ghi *Chưa chốt* thay vì Pass).

## Kết quả từng vế

| Vế | Quan hệ | Kỳ vọng phiếu | Web thực tế (số liệu quyết định) | Đạt? |
|---|---|---|---|---|
| **C1** | MATCH | *"Hệ thống **chặn thao tác**"* — `:124` (*"Xóa: chỉ khi KHÔNG có vụ việc liên kết"*), `:183` (AC: *"từ chối + thông báo"*), `:299`, `:171` mức `ERROR` | **Đường 1 (giao diện)** — bấm [Xóa] → hiện hộp xác nhận *"Xóa hợp đồng? / Hợp đồng sẽ được gỡ khỏi danh sách và lưu vết trong nhật ký."* → bấm **[Xóa]** xác nhận → hộp đóng nhưng **trang chi tiết vẫn ở nguyên** (`location.href` không đổi), bản ghi **vẫn hiển thị đầy đủ**. **Đường 2 (máy chủ — độc lập)** — đọc lại bản ghi ngay sau đó: `GET` → **200**, `maHopDong` vẫn `HDTV-20260807-0006`, `version` **vẫn 10** (không nhích), `trangThai` vẫn `DANG_THUC_HIEN`, **không** sinh trường cờ xóa nào, **3** vụ việc liên kết còn nguyên; và trong **danh sách** hợp đồng của vụ việc (`GET /api/v1/hop-dong-tu-vans?vuViecId=6bf98a2e-…` → 200) vẫn đủ **2** hợp đồng `HDTV-20260807-0007` + **`HDTV-20260807-0006`** ⇒ **máy chủ chặn thật**, không phải giao diện giả vờ | ✅ |
| **C2** | MATCH | *"…và hiển thị thông báo **"Không thể xóa hợp đồng đang có vụ việc liên kết"**"* — `:171` (`ERR-HDTV-04`, trùng **từng chữ**) | **Đường 1 (bắt thông báo)** — `MutationObserver` cài trên `document.body` **TRƯỚC** khi bấm xác nhận, **không lọc trùng**, đọc `innerText`: bắt được chuỗi **`Không thể xóa hợp đồng đang có vụ việc liên kết`** — **trùng từng chữ** với cột K và với `:171`. Thông báo **tự tắt**: đọc DOM sau đó `.ant-message-notice-wrapper` đã **rỗng** ⇒ nếu dò DOM kiểu poll thì đã kết luận sai *"im lặng"*. Bộ bắt ghi **2 nút DOM cùng một thời điểm** = vỏ `.ant-message` + con `.ant-message-notice-wrapper` ⇒ **1** thông báo, **không** phải hiện 2 lần. **Đường 2 (mã phản hồi của chính lời gọi xóa — độc lập)** — móc `XMLHttpRequest` ghi lại: **đúng 1** lời gọi `DELETE /api/v1/hop-dong-tu-vans/d16487f4-…` → **HTTP 403**, thân phản hồi `{"success":false,"error":{"code":"ERR-HDTV-04","message":"Không thể xóa hợp đồng đang có vụ việc liên kết","requestId":"034297e3-…"}}` lúc `2026-08-07T11:05:24.794Z` (18:05:24 giờ VN) ⇒ chữ trên màn **đúng là do máy chủ từ chối sinh ra**, đúng mã `ERR-HDTV-04`; **chỉ 1** lời gọi ⇒ không có gửi trùng | ✅ |

**Chống Pass oan đã làm:** **không** chấm "đã chặn" vì nút bị mờ — nút [Xóa] **bấm được** và đã bấm **tới bước xác nhận cuối**; **không** dừng ở giao diện — đã đối chứng bằng **bản ghi máy chủ** (`version` không nhích, không cờ xóa) và bằng **danh sách** vẫn còn hợp đồng; **xác nhận tiền đề ≥1 vụ việc liên kết bằng 2 đường** trước khi bấm (nếu hợp đồng sạch liên kết thì xóa thành công mới là đúng đặc tả, chấm sẽ ngược); bắt thông báo bằng `MutationObserver` cài **trước** thao tác (thông báo đã tự tắt, poll sẽ trượt), đọc `innerText` chứ không `textContent`; **đếm số lời gọi** `DELETE` = 1 để loại ca gửi trùng.

**Chống Fail oan đã kiểm:** **không** Fail vì có hộp xác nhận trung gian (bước J vốn ghi *"Nhấn Xóa **và xác nhận**"*); **không** Fail vì thông báo là chữ nổi tự tắt thay vì hộp thoại (đặc tả chỉ khai mức + nội dung, không khai hình thức); **không** Fail vì màn không tự làm mới sau khi bị chặn (cột K phiếu này **không** nhắc làm mới); **không** Fail vì trên màn không hiện mã `ERR-HDTV-04` (mã là định danh nội bộ; mã có mặt trong thân phản hồi máy chủ).

## Ghi nhận thêm (KHÔNG chấm — đã kiểm để khỏi log nhầm thành lỗi)

Gọi danh sách hợp đồng **không kèm ngữ cảnh** (`GET /api/v1/hop-dong-tu-vans`, kể cả kèm `page`/`limit`) trả **403** `ERR-PERM-SYS-00-01` — *"Hợp đồng tư vấn chỉ truy cập trong ngữ cảnh vụ việc/tư vấn viên/tổ chức."* Cùng endpoint kèm `?vuViecId=…` trả **200**. Đây **đúng** hệ quả của quyết định nghiệp vụ bỏ menu riêng (`:266`/`:268`), **không** phải lỗi ⇒ **không** log. Ghi lại để lượt sau khỏi tưởng là lỗi phân quyền.

## Verdict → ô R

**`Test done`** — **2/2 vế `MATCH` đều đạt**: thao tác xóa bị chặn ở **cả giao diện lẫn máy chủ** (`DELETE` → **403 `ERR-HDTV-04`**, bản ghi giữ nguyên `version` 10 và 3 vụ việc liên kết), và thông báo hiện đúng **nguyên văn** chuỗi mà cột K + `:171` yêu cầu. Phiếu không có vế `DIFF`/`GAP`.

> Không viết *"fix đã có tác dụng"*: phiếu chưa từng chạy (`N/R`), không có ảnh lỗi cũ ⇒ chỉ kết luận **hiện trạng**.

## Dữ liệu đã đổi trên môi trường

**KHÔNG có.** Thao tác xóa **bị từ chối** nên không có gì bị ghi: `HDTV-20260807-0006` giữ nguyên `version` **10**, `trangThai` `DANG_THUC_HIEN`, **3** vụ việc liên kết, 2 mốc tiến độ, 1 giai đoạn thanh toán. Không đụng hợp đồng khác, không đụng dữ liệu đối tác.

## Ảnh

Không chụp — cả 2 vế `MATCH` đều **đạt**, không có FAIL cần chứng minh (flow 04 §7). Số liệu quyết định (403 · `ERR-HDTV-04` · nguyên văn thông báo · `version` 10) đã ghi thẳng trong bảng trên.
