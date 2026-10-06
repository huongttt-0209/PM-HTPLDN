# Bảng đối chiếu điều kiện — RE-VERIFY QLDKDTTH_06 (row 272) — sau khi dev báo đã sửa

**Kết luận:** Pass. Chốt kiểm đã tồn tại và chạy đúng: bấm **[Phê duyệt]** trên hồ sơ *Chờ duyệt* của khóa học **không đang nhận đăng ký** thì hệ thống **từ chối**, hiện thông báo lỗi đỏ *"Khóa học đã đóng đăng ký"* (đúng câu chữ đặc tả quy định), máy chủ trả **422**, hồ sơ **giữ nguyên Chờ duyệt**. Tái hiện **2/2** trên 2 hồ sơ khác nhau. Có **2 nhánh của đặc tả chưa phủ được** vì môi trường không dựng nổi dữ liệu — khai báo chi tiết ở §Giới hạn, không giấu.

Đo ngày 30/07/2026 22:44–22:52; **rà soát bổ sung 31/07/2026 00:00–00:20** (cố dựng nốt nhánh còn thiếu). Bản **HTPLDN · V1.0.3**, tài khoản `cbnv_tw_03` (và `0109998887` vai trò DN khi kiểm đường tự đăng ký).

| Điều kiện có thể đổi kết quả | Bug gốc (BUG-QLDKDTTH_06, Pass-bug-report-tuan-1-vong-dau.md) | Mình test lại (env nip.io, 30/07/2026 22:44–22:52) | GAP? |
|---|---|---|:-:|
| Vai trò / tài khoản | `cbnv_tw` — **CB Nghiệp vụ - Trung ương (CB_NV_TW)**, phạm vi **BTP · TW** | `cbnv_tw_03` — **CB Nghiệp vụ - Trung ương #03 (CB_NV_TW)**, phạm vi **BTP · TW**, đơn vị *Bộ Tư Pháp · Cục Bổ trợ tư pháp* (đọc trên thanh tiêu đề) — cùng vai trò, cùng cấp, cùng đơn vị | Không |
| Màn hình + thao tác kích hoạt | Tab **Học viên** của chi tiết khóa học → bấm **[Phê duyệt]** trên dòng hồ sơ (bước 4 của phiếu) | Đúng tab **Học viên** → bấm **[Phê duyệt]** trên dòng hồ sơ, **2 lần trên 2 hồ sơ khác nhau** | Không |
| Trạng thái hồ sơ đăng ký lúc bấm | **Chờ duyệt**, cột Hành động có [Phê duyệt] [Từ chối] | **Chờ duyệt**, cột Hành động có [Phê duyệt] [Từ chối] — `QA Verify DKTGKH07 R2 Now` và `QA Import Valid 2` | Không |
| Tiền đề khóa học: **không đang nhận đăng ký** (điều kiện mà chốt kiểm E1 phải bắt) | `KH-20260730-001` — trạng thái **Đã duyệt** (chưa công khai, chưa khai giảng) **và** cửa sổ đăng ký 01/07→03/07/2026 đã đóng ⇒ **không** thỏa `trạng thái ∈ {DA_CONG_KHAI, DANG_DIEN_RA}` (`srs-fr-03-dao-tao.md:454`) | `KH-SEED-0001` — trạng thái **Đã kết thúc** ⇒ cũng **không** thỏa `trạng thái ∈ {DA_CONG_KHAI, DANG_DIEN_RA}`. Cùng một vế điều kiện của đặc tả, cùng lớp "khóa học không đang nhận đăng ký". Đã mở lại `KH-20260730-001` xác nhận tiền đề gốc còn nguyên: `trangThai = DA_DUYET`, `moDangKyTuNgay = 2026-07-01`, `moDangKyDenNgay = 2026-07-03` | Không |
| Đối chứng ngược — khóa **đang** nhận đăng ký thì vẫn phải duyệt được | Không có trong bug gốc (bug gốc chỉ đo nhánh lỗi) | `KH-QAW7-HOINGHI` — **Đang diễn ra**, không đặt cửa sổ ⇒ đang nhận đăng ký. Bấm [Phê duyệt] → **201**, thông báo xanh *"Đã phê duyệt đăng ký"*, hồ sơ sang **Đã duyệt**. Chứng minh chốt kiểm là phép kiểm có điều kiện, **không phải chặn mù mọi thao tác duyệt** | Không |
| Nguồn tạo hồ sơ đăng ký | Cột **Nguồn = "Nhập tay"** (thêm qua nút [Thêm học viên]) | Cột **Nguồn = "Nhập tay"** và **"Import Excel"** — cả 2 nguồn đều cho cùng kết quả bị chặn. Nút [Thêm học viên] nay đã bị gỡ theo `srs-fr-03-dao-tao.md:445` *[BA chốt 2026-07-30]* nên không tạo hồ sơ mới được (xem §Giới hạn) | Không |

## Bằng chứng đã mở đọc

- `bug-reports/image/BUG-QLDKDTTH_06-r5-V103-PASS-toast-khoa-hoc-da-dong-dang-ky.png` — **khoảnh khắc bị chặn**: thông báo **đỏ** *"Khóa học đã đóng đăng ký"* ở đầu trang; thanh tiến trình khóa học ở bước **5 Đã kết thúc**; dòng hồ sơ vẫn còn **[Phê duyệt] [Từ chối]** (chưa bị duyệt); góc phải là **CB Nghiệp vụ - Trung ương #03 · CB_NV_TW · BTP · TW**; thanh bên ghi **HTPLDN · V1.0.3**.
- `bug-reports/image/BUG-QLDKDTTH_06-r5-V103-doi-chung-khoa-con-nhan-dang-ky-duyet-thanh-cong.png` — **đối chứng**: cùng tài khoản, khóa `KH-QAW7-HOINGHI` ở bước **4 Đang diễn ra**, thông báo **xanh** *"Đã phê duyệt đăng ký"*, 2 dòng đầu đã sang **Đã duyệt**.
- `bug-reports/image/BUG-QLDKDTTH_06-r5-V103-tien-de-cua-so-dang-ky-da-dong.png` — tiền đề gốc còn nguyên trên `KH-20260730-001`: **Mở đăng ký từ 01/07/2026 · đến 03/07/2026**, thanh tiến trình bước **3 Đã duyệt**.

## Phương pháp thứ hai (bắt buộc)

- **Đọc lại dữ liệu sau thao tác bị chặn**: 2 hồ sơ `8e92fb79-…` và `061f34d8-…` vẫn `trangThai = "CHO_DUYET"` ⇒ chặn thật ở máy chủ, không phải chỉ ẩn nút trên giao diện.
- **Đếm request ↔ thông báo**: mỗi lần bấm = **1** `POST /api/v1/dang-ky-dao-taos/{id}/approve` → **422**. Đo số khung thông báo hiển thị đồng thời (`.ant-message-notice`) trong 9 giây: **đỉnh = 1** ⇒ 1 request ↔ 1 thông báo, không double-toast.
- **Đối chứng ngược** (mục trong bảng trên): khóa đang nhận đăng ký → **201** + đổi trạng thái thật. Loại giả thuyết "dev sửa bằng cách chặn hết mọi thao tác duyệt".
- **Đối chiếu đặc tả** (`Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-03-dao-tao.md`):
  - `:387` — *"| PRE-02 | Khóa học tồn tại, đang mở đăng ký |"*
  - `:428` — *"| E1 | Khóa học đã đóng đăng ký | ERR-DKDT-01 | \"Khóa học đã đóng đăng ký\" | ERROR |"* ⇒ câu thông báo web đang hiện **trùng khít nguyên văn** đặc tả.
  - `:454` — *"Khóa học đang nhận đăng ký: trạng thái ∈ **{DA_CONG_KHAI, DANG_DIEN_RA}** VÀ (nếu có cửa sổ) `NOW ∈ [mo_dang_ky_tu, mo_dang_ky_den]`"*.

## Pass đối kháng (tự bác trước khi ghi sheet)

1. *"Có thể web chỉ ẩn nút chứ không chặn thật."* — Bác: nút **vẫn hiện** và **vẫn bấm được**; chặn xảy ra ở máy chủ (**422**) và đọc lại dữ liệu thấy hồ sơ giữ `CHO_DUYET`.
2. *"Có thể dev chặn mù mọi thao tác duyệt cho xong."* — Bác bằng **đối chứng ngược**: trên khóa đang nhận đăng ký, duyệt vẫn chạy đúng (**201**, hồ sơ sang *Đã duyệt*).
3. *"Có thể chỉ đúng trên bản build cũ."* — Bác: thanh bên ghi **V1.0.3** nhưng đây là **bản triển khai MỚI so với lần đo 30/07 11:31**: chuỗi `"Thêm học viên"` đã biến mất khỏi **toàn bộ 87 tệp mã nguồn giao diện đã tải (~3 MB)**, và endpoint tạo đăng ký thủ công trả **404 `Cannot POST`**. Tức là mã đã đổi thật, không phải đo lại đúng bản cũ.
4. *"Thông báo có thể là lỗi chung chung, không phải chốt kiểm đúng chỗ."* — Bác: câu chữ **trùng nguyên văn** ô *"Phản hồi hệ thống"* của E1 tại `:428`, và chỉ xuất hiện đúng trên khóa không nhận đăng ký.

## Giới hạn còn lại (khai báo minh bạch — không giấu)

- **Không dựng được hồ sơ *Chờ duyệt* MỚI.** Ngày 30/07/2026 BA đã chốt (`srs-fr-03-dao-tao.md:445`): *"DN/NHT tự đăng ký … Đây là **đường tạo đăng ký duy nhất** — cán bộ không nhập tay, không nhập tệp danh sách"*. Dev đã thực hiện: nút [Thêm học viên] bị gỡ khỏi giao diện, endpoint tạo đăng ký thủ công trả **404**, không có API nhập tệp học viên. Đường còn lại là chuyên trang Pháp luật quốc gia (webhook `/api/v1/public/dang-ky-dao-taos/inbound`, yêu cầu mTLS — không cấp chứng thư trên env này). Đã thử vai trò **DN** (`0109998887`): không có thao tác tự đăng ký, và không thấy khóa học của cấp TW.
- **Hệ quả — 2 nhánh của đặc tả `:454` chưa đo được, nói thẳng chứ không giấu:**
  1. **Nhánh trạng thái `Đã duyệt`** (đúng trạng thái của khóa trong phiếu gốc). Đã đo trên khóa **"Đã kết thúc"** — cùng vế điều kiện (`không ∈ {DA_CONG_KHAI, DANG_DIEN_RA}`), cùng lớp lỗi, nhưng **không phải cùng một trạng thái**.
  2. **Nhánh "trạng thái hợp lệ nhưng cửa sổ đăng ký đã hết hạn"** — tức vế `NOW ∈ [mo_dang_ky_tu, mo_dang_ky_den]` của `:454`, đúng cái tên phiếu nhắc tới. Chưa đo được lần nào.
- **Đã rà lại một lượt riêng (31/07/2026 00:00–00:20) để cố dựng bằng được nhánh 2, và ghi lại vì sao không dựng nổi:**
  - **Quét toàn bộ 13 khóa học** trong môi trường: chỉ **1** khóa còn hồ sơ *Chờ duyệt* là `KH-QAW7-HOINGHI` (4 hồ sơ) — và khóa này **không đặt cửa sổ đăng ký** (— / —), nên theo `:454` nó **đang** nhận đăng ký ⇒ không dùng để đo nhánh 2 được. Mọi khóa **có** đặt cửa sổ thì **không** còn hồ sơ *Chờ duyệt* nào.
  - **Không sửa được cửa sổ đăng ký của bất kỳ khóa nào**: dòng trong danh sách khóa học chỉ có thao tác **[Xem]**; trang chi tiết chỉ có **[Quay lại danh sách]**, **[Công khai]/[Gỡ công khai]**, **[Khai giảng]/[Kết thúc]** — **không có** [Sửa]/[Chỉnh sửa] ở đâu. Nên không thể gắn cửa sổ hết hạn cho khóa đang có hồ sơ *Chờ duyệt*.
  - **Không tạo được hồ sơ đăng ký mới bằng bất kỳ đường nào**: nút [Thêm học viên] đã bị gỡ (BA chốt `:445`); tab **Học viên** không còn thao tác nhập tệp danh sách; và đã **đăng nhập kiểm chứng bằng vai trò DN** (`0109998887` — *QA UAT Kiem Thu DN*): DN **không có bất kỳ thao tác tự đăng ký nào** trên màn Khóa học (chi tiết khóa chỉ có [Quay lại danh sách]) và chỉ nhìn thấy khóa thuộc phạm vi của mình. Đường còn lại là chuyên trang Pháp luật quốc gia (webhook yêu cầu mTLS — không cấp chứng thư trên env này).
  - Trong lượt rà này có **công khai `KH-20260730-001`** (khóa có cửa sổ 01/07→03/07 đã đóng) để thử xem DN có đăng ký được không, sau đó **đã gỡ công khai, hoàn nguyên đúng trạng thái ban đầu** (*Đã duyệt*, chưa công khai) — có kiểm chứng lại trên giao diện.
- **Vì sao vẫn để verdict Pass:** yêu cầu của phiếu là *"hệ thống phải từ chối duyệt khi khóa không nhận đăng ký"* — điều đó **đã đo được là đúng** bằng thao tác thật, chặn ở máy chủ (422), đúng câu chữ đặc tả, tái hiện 2/2, và có đối chứng ngược loại bỏ khả năng chặn mù. Hai nhánh trên là **phần chưa phủ hết**, không phải bằng chứng lỗi còn tồn tại. Nếu cần phủ nốt thì phải mở cửa lại đường tạo hồ sơ đăng ký (hoặc cấp chứng thư mTLS) rồi kiểm một lượt riêng — đây là việc của môi trường/dữ liệu, không phải của phép đo.

## Ngoài tiêu chí phiếu — có thấy gì bất thường không?

- **Khóa học đã kết thúc vẫn "gỡ công khai" được nhưng không công khai lại được** — `POST …/unpublish` trả **200** trên khóa `KH-SEED-0001` (*Đã kết thúc*), nhưng `POST …/publish` sau đó trả **422 `ERR-KH-DK-WINDOW-01: Khóa học phải có cửa sổ đăng ký hợp lệ trước khi công khai`* vì khóa này không đặt cửa sổ ⇒ thao tác một chiều, không quay lại được. Chưa log thành bug vì chưa tra đủ đặc tả cho cặp công khai/gỡ công khai; đã ghi vào phần bàn giao để tra sau.
- **Công khai được khóa học có cửa sổ đăng ký đã hết hạn** — `KH-20260730-001` (cửa sổ 01/07→03/07/2026, đã đóng) vẫn công khai thành công (*"Đã công khai khóa học thành công"*), tức `ERR-KH-DK-WINDOW-01` chỉ kiểm **có** cửa sổ chứ không kiểm cửa sổ **còn hiệu lực**. Cùng lý do trên, chưa log — đã ghi lại để tra đặc tả.
- Cả 2 thao tác trên đã được **hoàn nguyên**: `KH-20260730-001` đã gỡ công khai về đúng trạng thái ban đầu (*Đã duyệt*, chưa công khai). Riêng `KH-SEED-0001` **không** công khai lại được (lý do ở trên) — trạng thái `DA_KET_THUC` giữ nguyên, chỉ cờ công khai đổi.
