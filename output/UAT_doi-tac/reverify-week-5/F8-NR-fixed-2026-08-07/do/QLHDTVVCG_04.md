# QLHDTVVCG_04 — dòng 310 · 07/08/2026 15:40–15:44 · tài khoản **`cbnv_tw_05`** · bản dựng `index-BbPPdate.js` (`last-modified` 07/08/2026 06:47:57 GMT)

> ⚠️ **Đổi tài khoản giữa chừng — khai theo Rule 7.** Phiên `cbnv_tw_03` bị thu hồi lúc 08:39 GMT
> (`ERR-AUTH-SYS-00-03` — *"Token đã bị thu hồi"*); hộp thư cho thấy **có phiên khác đăng nhập `cbnv_tw_03`
> lúc 08:33 GMT** mà không phải lượt đo này. Theo chỉ đạo brief §3 → chuyển sang **`cbnv_tw_05`**:
> **CÙNG vai trò** (Cán bộ Nghiệp vụ), **CÙNG cấp** (Trung ương), **CÙNG đơn vị** (Cục Bổ trợ tư pháp).
> Không đổi vai trò, không đổi cấp ⇒ phạm vi dữ liệu không đổi.

Phiếu khóa **2 vế, cả hai `MATCH`, route TEST** ⇒ **không cắt phép đo**
([`chuan/QLHDTVVCG_04.md`](../chuan/QLHDTVVCG_04.md)).

## Đường vào

Đăng nhập → **Vụ việc HTPL** → tìm `VV-BTP-TW-20260804-002` → mở chi tiết → bung mục **"HĐ tư vấn liên kết"**
(Màn 1 — bề mặt chấm chính thức của đợt A). Bước J của phiếu ghi *"Chọn menu Hợp đồng Tư vấn"*; menu đó đã bị bỏ
theo `:266`/`:268` ⇒ tiền đề, không phải vế chấm.

**Trạng thái TRƯỚC thao tác** (ảnh 01, bắt buộc để không nhầm "rỗng do lọc" với "rỗng do chưa có dữ liệu"):
ô tìm kiếm **để trống**, bảng có **2 dòng dữ liệu** (`HDTV-20260807-0007`, `HDTV-20260807-0006`), phân trang
**"1-2 / 2 mục"**.

**Thao tác đã làm:** gõ `ZZZKHONGTONTAI` vào ô tìm kiếm → **bấm nút [Tìm kiếm] bằng chuột trên trang**.
Bộ bắt thông báo (`MutationObserver` trên `document.body`, đọc bằng `innerText`, **KHÔNG lọc trùng**, đếm theo
**mốc giờ khác nhau**) được cài **TRƯỚC** khi bấm.

## Kết quả từng vế

| Vế | Quan hệ | Kỳ vọng phiếu | Web thực tế | Đạt? | Ảnh |
|---|---|---|---|---|---|
| **C1** | `MATCH` | *"bảng dữ liệu để trống"* (`:251` + `:228`) | **0 dòng dữ liệu** (trước đó 2 dòng). Còn giữ **11 tiêu đề cột** và khung bảng — đúng, C1 không đòi ẩn cả bảng. Bộ đếm phân trang **ẩn** khi không có kết quả. **Đối chứng:** gọi thẳng dịch vụ tìm kiếm cùng từ khóa → `total = 0`, mảng dữ liệu rỗng, `totalPages = 0` ⇒ khớp bảng | ✅ | 01 · 02 |
| **C2** | `MATCH` | *"hệ thống hiển thị thông báo **"Không tìm thấy hợp đồng phù hợp"**"* (`:251` `INF-HDTV-TK-01`) | Vùng trống của bảng hiện **đúng nguyên văn** `Không tìm thấy hợp đồng phù hợp` — trùng **từng chữ** với cột K và với `:251`. **Đối chứng:** bộ bắt thông báo ghi nhận **1 nút chữ** (`TR.ant-table-placeholder`) tại **1 mốc giờ duy nhất** `08:42:33.016Z`, ứng với **1 yêu cầu gửi đi** (`…&search=ZZZKHONGTONTAI…`) ⇒ **không** có thông báo nổi tự tắt bị trượt, **không** có thông báo lặp | ✅ | 02 |

**Chống Pass oan đã làm đủ:** so **trước/sau** thao tác (2 dòng → 0 dòng) nên chữ trên màn là **phản hồi của
phép tìm**, không phải trạng thái rỗng mặc định; đọc bằng `innerText` chứ không `textContent`; bộ bắt cài trước
khi bấm và **không lọc trùng**; số thông báo đếm theo **mốc giờ**, kèm **số yêu cầu gửi đi**.

**Chống Fail oan đã kiểm:** từ khóa dùng là **chuỗi không dấu** (`ZZZKHONGTONTAI`) — cố ý tránh lớp từ khóa
tiếng Việt có dấu đang lỗi ở `_03`, để lỗi kia **không** làm bẩn phép đo này. Câu chữ khớp từng ký tự nên không
phải viện tới quy tắc "chấm hành vi, không bắt trùng chữ". Đặc tả tự lệch giữa `:251` (*"…phù hợp"*) và `:258`
(*"Không tìm thấy hợp đồng"*) — web đi theo `:251`, tức bản **đúng bằng kỳ vọng đối tác**.

## Verdict → ô R

**`Test done`** — cả **2/2 vế `MATCH` đều đạt**, không còn vế `DIFF`/`GAP` nào (QĐ-01).

## Dữ liệu đã đổi

**KHÔNG có.** Phiếu chỉ đọc (`:244` — *"Read-only, không thay đổi dữ liệu"*). Không tạo, không sửa, không xóa
bản ghi nào; không đụng dữ liệu đối tác. Hai hợp đồng dùng làm nền đã có sẵn từ `_15` và `_02`.

## Ảnh (đã mở lại xem từng ảnh trước khi dùng)

| Ảnh | Nội dung | Liên kết xem được |
|---|---|---|
| 01 `QLHDTVVCG_04-01-truoc-khi-tim-o-tim-kiem-trong-bang-co-2-dong.png` | **Trước** thao tác: ô tìm kiếm trống, 2 dòng dữ liệu, "1-2 / 2 mục" | https://drive.google.com/file/d/1SPLMPZxlVc4FyU_a859y_sUK0WeeqUrv/view?usp=drivesdk |
| 02 `QLHDTVVCG_04-02-sau-khi-tim-bang-trong-va-hien-cau-khong-tim-thay.png` | **Sau** thao tác: ô chứa `ZZZKHONGTONTAI`, 0 dòng dữ liệu, chữ *"Không tìm thấy hợp đồng phù hợp"*, tiêu đề cột vẫn còn | https://drive.google.com/file/d/1zobehZhkOEpmvB3zLT-z67yZjLetCRbO/view?usp=drivesdk |
