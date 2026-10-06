# QLHDTVVCG_05 — dòng 311 · 07/08/2026 15:45–15:49 · tài khoản **`cbnv_tw_05`** · bản dựng `index-BbPPdate.js` (`last-modified` 07/08/2026 06:47:57 GMT)

> ⚠️ **Tài khoản thực dùng `cbnv_tw_05`** (không phải `cbnv_tw_03` như brief §3) — lý do đầy đủ ghi ở
> [`do/QLHDTVVCG_04.md`](QLHDTVVCG_04.md): phiên `_03` bị thu hồi (`ERR-AUTH-SYS-00-03`) do có phiên khác
> đăng nhập cùng tài khoản. Fallback **cùng vai trò · cùng cấp · cùng đơn vị** theo Rule 7 ⇒ phạm vi dữ liệu không đổi.

Phiếu khóa **2 vế, cả hai `MATCH`, route TEST** ⇒ **không cắt phép đo**
([`chuan/QLHDTVVCG_05.md`](../chuan/QLHDTVVCG_05.md)).

## Đường vào

Màn 1 — Chi tiết vụ việc `VV-BTP-TW-20260804-002` → mục **"HĐ tư vấn liên kết"** → **thanh lọc**.

🔴 **Vị trí đo đúng:** cặp ô **Từ ngày / Đến ngày trên THANH LỌC** (`:287`) — neo `:250` `ERR-HDTV-TK-01`.
**KHÔNG** đo cặp Thời hạn bắt đầu/kết thúc trong biểu mẫu thêm/sửa (`:290`, `:169` `ERR-HDTV-02`); hai chỗ có
**câu chữ giống hệt nhau** nên đo nhầm là hỏng phiếu. Biểu mẫu thêm/sửa **không được mở** trong lượt đo này.

**Nền trước thao tác:** đã bấm [Xóa bộ lọc] → mọi ô lọc trống, bảng **2 dòng dữ liệu**, phân trang "1-2 / 2 mục".
Bộ bắt thông báo (`MutationObserver` trên `document.body`, `innerText`, **KHÔNG lọc trùng**, đếm theo **mốc giờ**)
+ bộ đếm yêu cầu gửi đi được cài **TRƯỚC** thao tác.

**Thao tác:** gõ tay `20/08/2026` vào ô **Từ ngày**, `10/08/2026` vào ô **Đến ngày** (lệch **10 ngày**, không dùng
hai ngày bằng nhau vì `:219` cho phép bằng nhau) → **bấm nút [Tìm kiếm] bằng chuột trên trang**.

> Bẫy "ô chọn ngày tự chặn nên không nhập nổi ca lỗi" **không xảy ra**: đã kiểm các ô ngày 8–12/08 trong lịch của
> **Đến ngày** sau khi Từ ngày = 20/08 — **không ô nào bị khoá** (`ant-picker-cell-disabled` = false). Ca nghịch
> nhập được thật, không phải "coi như đã chặn".

## Kết quả từng vế

| Vế | Quan hệ | Kỳ vọng phiếu | Web thực tế | Đạt? | Ảnh |
|---|---|---|---|---|---|
| **C1** | `MATCH` | *"Hệ thống **chặn thao tác**"* (`:250` severity `ERROR` + `:219`) | **Không có yêu cầu tìm kiếm nào rời trình duyệt**: bộ đếm ghi **0** yêu cầu `hop-dong-tu-vans` qua **cả 3 lần bấm** [Tìm kiếm] với khoảng ngày nghịch. Bảng **giữ nguyên kết quả cũ** (2 dòng, "1-2 / 2 mục"), **không** bị thay bằng danh sách mới hay bảng rỗng. **Đối chứng:** nhật ký mạng của trang không có bản ghi nào chứa cặp `tuNgay=2026-08-20&denNgay=2026-08-10` | ✅ | 01 · 02 |
| **C2** | `MATCH` | *"hiển thị thông báo **"Ngày bắt đầu phải trước ngày kết thúc"**"* (`:250` `ERR-HDTV-TK-01`) | Báo lỗi **đúng nguyên văn**, hiện **hai kênh cùng lúc**: (a) **thông báo nổi** `ant-message` tại `08:47:43.255Z`; (b) **chữ đỏ cố định dưới CẢ HAI ô ngày** `ant-form-item-explain-error` tại `08:47:43.259Z`, kèm viền đỏ ô nhập. Chữ trùng **từng ký tự** với cột K và với `:250`. **Đối chứng:** bộ bắt cài trước thao tác ghi nhận **1 thông báo nổi / 1 lần bấm** (lần 1 và lần 2 mỗi lần đúng **1 mốc giờ**) ⇒ **không** thông báo lặp, **không** thông báo nào bị trượt | ✅ | 02 |

**Chống Pass oan đã làm đủ:** ca nghịch **nhập được thật** (đã chứng minh lịch không khoá); chứng minh có chặn
bằng **số yêu cầu gửi đi = 0** chứ không suy từ việc bảng không đổi; bộ bắt thông báo cài **trước** khi bấm nên
thông báo nổi tự tắt không bị trượt; đọc bằng `innerText`.

**Chống Fail oan đã kiểm:** câu chữ trùng từng ký tự nên không phải viện quy tắc "chấm hành vi"; đặc tả không đòi
hiện mã lỗi `ERR-HDTV-TK-01` cho người dùng nên không bắt lỗi chuyện đó; hệ thống **không** báo lỗi sớm lúc đổi
ngày mà chỉ báo khi bấm [Tìm kiếm] — `:287` khai `change -> filter`, báo lúc bấm là **lỏng hơn** chứ không sai vế
"chặn thao tác", vì thao tác vẫn bị chặn.

**Không mở rộng case:** ca **Từ ngày = Đến ngày** (`:219` cho phép, đáng lẽ phải tìm được) **KHÔNG đo** — nó là
case khác, không tự lộ trong bước bắt buộc của vế đang verify (BUG SCOPE LOCK). Ghi lại để đợt sau biết là chưa có
số liệu, **không** suy đoán.

## Verdict → ô R

**`Test done`** — cả **2/2 vế `MATCH` đều đạt**, không còn vế `DIFF`/`GAP` nào (QĐ-01).

## Dữ liệu đã đổi

**KHÔNG có.** Chỉ nhập giá trị vào thanh lọc rồi bấm tìm; thao tác bị chặn nên **không** có truy vấn nào chạy.
Không tạo, không sửa, không xóa bản ghi nào; **không** mở biểu mẫu thêm/sửa hợp đồng (giữ sạch phép đo của `_21`).

## Ảnh (đã mở lại xem từng ảnh trước khi dùng)

| Ảnh | Nội dung | Liên kết xem được |
|---|---|---|
| 01 `QLHDTVVCG_05-01-da-nhap-khoang-ngay-nghich-tren-thanh-loc-truoc-khi-bam-tim.png` | Thanh lọc đã nhận **Từ ngày 20/08/2026** và **Đến ngày 10/08/2026**, **chưa bấm** [Tìm kiếm] nên chưa có báo lỗi; bảng 2 dòng | https://drive.google.com/file/d/1oBcxO_V3yPumDvUPrTVtJH79zl9YBZQu/view?usp=drivesdk |
| 02 `QLHDTVVCG_05-02-sau-khi-bam-tim-bao-loi-duoi-ca-hai-o-ngay.png` | **Sau** khi bấm [Tìm kiếm]: hai ô ngày viền đỏ, dưới mỗi ô hiện *"Ngày bắt đầu phải trước ngày kết thúc"*; bảng **giữ nguyên** 2 dòng cũ | https://drive.google.com/file/d/1PoMR_VyQt75x6JTnbWH-v3LssdS_zAba/view?usp=drivesdk |

> **Thông báo nổi không vào được ảnh** (tự tắt ~3 giây, ba lần hẹn giờ chụp đều trượt). Bằng chứng của nó là bản
> ghi của bộ bắt thông báo: phần tử `DIV.ant-message ant-message-top`, nội dung *"Ngày bắt đầu phải trước ngày kết
> thúc"*, mốc giờ `08:47:43.255Z` (lần bấm 1) và `08:48:22.868Z` (lần bấm 2) — mỗi lần bấm đúng **1** thông báo.
> Ảnh 02 đã bắt được kênh hiển thị **cố định** (chữ đỏ dưới hai ô ngày), tự nó đã đủ cho vế C2.
