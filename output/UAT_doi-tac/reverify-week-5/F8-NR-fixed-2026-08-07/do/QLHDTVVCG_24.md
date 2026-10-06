# QLHDTVVCG_24 — dòng 330 · 07/08/2026 17:37–17:42 · tài khoản **`cbnv_tw_04`** (CB NV TW, Cục Bổ trợ tư pháp - Bộ Tư pháp) · bản dựng `assets/index-BbPPdate.js` (`last-modified` Fri, 07 Aug 2026 06:47:57 GMT · `etag "6a757f9d-428"`)

> Chuẩn chấm khóa: [`chuan/QLHDTVVCG_24.md`](../chuan/QLHDTVVCG_24.md) — **2 vế: C1 `MATCH` · C2 `MATCH`** → route **TEST thuần** (không vế `DIFF`/`GAP`).
> Đọc lại dòng 330 lúc 17:37: `Trạng thái` `N/R` · `Kết quả thực tế` RỖNG · `R` = `Fixed` · `T` RỖNG · `U` RỖNG.
> Ô `DEV phản hồi lần 1` (S) chốt nội dung phải chạy: *"… Dev đã bổ sung theo SRS: **cho nhập Ngày thực tế và Trạng thái ngay trên dòng mốc tiến độ**."*

## Đường vào

Sidebar **Vụ việc HTPL** → `VV-BTP-TW-20260804-002` → [Xem vụ việc] → **"HĐ tư vấn liên kết"** → `HDTV-20260807-0006` → [Xem chi tiết]
→ nút **[Chỉnh sửa]** → mở hộp thoại **"Cập nhật hợp đồng tư vấn"** (`?action=sua`) → mục **"Mốc tiến độ"** (Nhóm 3).
`:292` chỉ khai nút `[+ Thêm mốc]` cho **trang thêm/sửa** ⇒ đo đúng trên **biểu mẫu sửa**, không phải trang xem chi tiết.
Bước J ghi *"Chọn menu Hợp đồng Tư vấn"* ở các phiếu cùng cụm — menu đã bỏ theo `:266`/`:268`, là **tiền đề**, không log lỗi.

**Mốc so ghi TRƯỚC khi bấm:** bảng Mốc tiến độ có **1** dòng — đếm bằng selector dòng cụ thể `input[id^="mocTienDos_"][id$="_tenMoc"]` (**không** đếm thẻ bọc ngoài) → `["mocTienDos_0_tenMoc"]`.

## Kết quả từng vế

| Vế | Quan hệ | Kỳ vọng phiếu | Web thực tế (số liệu quyết định) | Đạt? |
|---|---|---|---|---|
| **C1** | MATCH | *"thêm **một dòng trống** vào bảng mốc tiến độ; NSD **nhập trực tiếp trên dòng**"* (`:292` editable-table / inline-edit) | **Đường 1 (giao diện, bấm thật)** — bấm nút **[+ Thêm mốc tiến độ]** bằng chuột. Kết quả: (a) **KHÔNG mở hộp thoại nhập riêng** — số hộp thoại đang mở vẫn đúng **1** và vẫn là *"Cập nhật hợp đồng tư vấn"*, dòng mới được chèn **ngay trong** mục Mốc tiến độ ⇒ đúng dạng **inline-edit**, đây là bẫy Fail chính của phiếu; (b) số dòng **1 → 2** (`mocTienDos_0_tenMoc` → thêm `mocTienDos_1_tenMoc`), **tăng đúng 1**; (c) dòng mới **RỖNG hoàn toàn**: `tenMoc=""` · `ngayDuKien=""` · `ngayThucTe=""` · `ghiChu=""` · Trạng thái **chưa chọn giá trị nào** (không sao chép dòng trước, không có giá trị mặc định); (d) **gõ được ngay tại chỗ** — gõ bằng bàn phím thật vào ô Tên mốc dòng mới, ô nhận đủ **32 ký tự** `Moc QA H1 kiem tra them moc 1731`, **dòng 0 giữ nguyên** `Ban giao ho so tra cuu nhan hieu`. **Đường 2 (đối chứng độc lập)** — sau khi lưu, đọc lại bản ghi từ máy chủ: `mocTienDos` có **2** phần tử, phần tử mới `id` `aad02477-a3c4-4554-a4c3-c8321bacd85d` mang **đúng** chuỗi vừa gõ ⇒ dòng inline là dòng thật, không phải hiệu ứng giao diện | ✅ |
| **C2** | MATCH | Nhập trên dòng đủ 4 mục: **Tên mốc · Ngày dự kiến · Ngày thực tế (tùy chọn) · Trạng thái mốc** (`:292`; Inputs `:98`–`:102`: `ten_moc` Y · `ngay_du_kien` Y · `ngay_thuc_te` **N** · `trang_thai_moc` Y) | **Đường 1 (giao diện)** — dòng mới có **đúng 4 ô người dùng nhập** mà cột K liệt kê (+ ô `Ghi chú` phụ, + ô `id` ẩn của hệ thống): `Tên mốc tiến độ` · `Ngày dự kiến` · `Ngày thực tế` · Trạng thái (danh sách chọn). Nhập thật từng ô **ngay trên dòng**: Tên mốc gõ bàn phím → nhận; Ngày dự kiến gõ `20/08/2026` + Enter → ô nhận **`20/08/2026`**; Trạng thái mở bằng bàn phím → danh sách hiện **3 nhãn tiếng Việt** `Chưa bắt đầu` / `Đang thực hiện` / `Hoàn thành` (không lộ mã DB), chọn **`Đang thực hiện`** — tức **khác** giá trị mặc định `CHUA_BAT_DAU` ở `:102`, nên đọc lại phân biệt được là do người dùng chọn. **Ngày thực tế CỐ Ý ĐỂ TRỐNG.** **Dấu bắt buộc đọc từ chính biểu mẫu:** `aria-required="true"` ở `tenMoc` · `ngayDuKien` · `trangThaiMoc`; ô **`ngayThucTe` KHÔNG có** dấu bắt buộc ⇒ đúng cột "Bắt buộc = N" của `:101`. **Đường 2 (đối chứng độc lập)** — bấm **[Lưu]**, hệ thống **chấp nhận dòng, KHÔNG báo thiếu**: bộ bắt thông báo (cài **TRƯỚC** khi bấm, **không lọc trùng**, đọc `innerText`) bắt được đúng **1 mốc giờ** `10:42:06.474Z`/`.476Z` (2 nút DOM = vỏ ngoài `ant-message` + vỏ trong `ant-message-notice-wrapper` của **cùng một** thông báo) với nội dung **`Đã lưu hợp đồng`**, **0** thông báo lỗi/thiếu trường; mạng gửi đúng **1** lệnh lưu `PATCH /api/v1/hop-dong-tu-vans/d16487f4-…` → **200** (không double-submit) kèm `POST …/moc-tien-dos` → **201**. Đọc lại bản ghi: mốc mới lưu với `ngayDuKien` `2026-08-20`, **`ngayThucTe` = `null`**, `trangThaiMoc` = **`DANG_THUC_HIEN`** ⇒ bỏ trống Ngày thực tế **được chấp nhận** và ba trường bắt buộc lưu **đúng như gõ trên dòng** | ✅ |

**Chống Pass oan đã làm:** không dừng ở *"bấm nút thấy có thêm dòng"* — đã kiểm **cả 3 điều kiện còn lại** của cột K (không mở hộp thoại riêng · dòng **rỗng** · **gõ được tại chỗ**); đếm dòng bằng **selector ô dữ liệu của dòng**, không đếm thẻ bọc ngoài (tránh số nhân đôi); đọc **`value` từng ô** của dòng mới thay vì nhìn lướt; chọn Trạng thái **khác giá trị mặc định** để đọc lại phân biệt được *"người dùng chọn"* với *"hệ thống gán mặc định"*; đếm thông báo theo **mốc giờ khác nhau** (1) chứ không theo độ dài mảng (2); đếm **số lệnh lưu gửi đi** (1) để loại double-submit; kết luận *"không báo thiếu"* bằng **kết quả lưu thật đọc lại từ máy chủ**, không bằng suy đoán từ việc không thấy chữ đỏ.

**Chống Fail oan đã kiểm:** không Fail vì dòng mới **không có sẵn** giá trị Trạng thái (cột K đòi *"dòng trống"*, `:102` khai mặc định `CHUA_BAT_DAU` — hai điều lệch nhau, cả hai đều không phải lỗi); không Fail vì dòng thiếu trường `hop_dong_id` (`:98` Nguồn = **hệ thống**); không Fail vì bảng mốc không có nút xóa dòng (cột K không nhắc — thực tế **có** biểu tượng gỡ dòng); không Fail vì nhãn nút là *"Thêm mốc tiến độ"* thay vì `[+ Thêm mốc]` (cột K chấm **hành vi**, không chấm nhãn); không Fail vì không có ràng buộc Ngày dự kiến ≤ Ngày thực tế (`:100`, `:101` để trống cột Ràng buộc).

## Ghi nhận (KHÔNG chấm, không kéo verdict)

- Lượt bấm [Lưu] gửi kèm `POST …/thanh-toans` → 201 dù **không** sửa gì ở mục Thanh toán giai đoạn. Đọc lại: danh sách thanh toán vẫn **1** phần tử và **giữ nguyên `id` cũ** `deda5d2d-…` ⇒ **không** sinh bản ghi trùng. Hành vi "gửi lại toàn bộ nhóm con khi lưu" khớp `:122` (*"Tạo hoặc cập nhật bản ghi hợp đồng + mốc tiến độ + thanh toán giai đoạn"*). Đây là dữ kiện thuộc phạm vi phiếu `_21` C3 (thay thế vs cộng dồn) — **không** chấm ở phiếu này.
- Sau lượt lưu, `version` của hợp đồng đi từ **1 → 4** (một `PATCH` + hai lệnh ghi nhóm con). Không phải vế chấm của phiếu, ghi lại để phiếu sau đối chiếu.

## Verdict → ô R

**`Test done`** — **2/2 vế `MATCH` đều đạt**, phiếu không có vế `DIFF`/`GAP`.

> Không viết *"fix đã có tác dụng"*: phiếu chưa từng chạy (`N/R`), không có ảnh lỗi cũ ⇒ chỉ kết luận **hiện trạng đúng so với đặc tả**.

## Dữ liệu đã đổi trên môi trường (BẮT BUỘC khai)

| Đổi gì | Bản ghi | Env | Lúc |
|---|---|---|---|
| **THÊM 1 mốc tiến độ** vào hợp đồng HĐ-1 (bằng **giao diện thật**: `PATCH /api/v1/hop-dong-tu-vans/{id}` 200 + `POST …/moc-tien-dos` 201) | Hợp đồng `HDTV-20260807-0006` (`id` `d16487f4-3ccc-4629-8e07-bb63ea9a12be`) · mốc mới `id` `aad02477-a3c4-4554-a4c3-c8321bacd85d` — `Moc QA H1 kiem tra them moc 1731` · dự kiến `20/08/2026` · thực tế `null` · `DANG_THUC_HIEN` | `https://18.143.165.120.nip.io` (**nội bộ**) | 2026-08-07 17:42:06 |
| ↳ hệ quả | Số mốc tiến độ của HĐ-1: **1 → 2**. `version` **1 → 4**, `ngayCapNhat` `2026-08-07T10:42:06.756Z`. Vụ việc liên kết vẫn **3**, tệp đính kèm vẫn **1**, giai đoạn thanh toán vẫn **1** (giữ nguyên `id` cũ) | " | " |

**Vì sao phải lưu (khai theo `chuan/QLHDTVVCG_24.md` §c):** cột K đòi Ngày thực tế là **tùy chọn**; cách duy nhất chứng minh *"dòng được chấp nhận, không báo thiếu"* mà không suy đoán là **lưu thật** rồi đọc lại bản ghi. Chuẩn chấm cho phép: *"nếu buộc phải lưu để đo được thì khai rõ vào báo cáo"*. Thay đổi này **không phá tiền đề** của phiếu nào còn lại trong phạm vi (`_26`/`_27` dùng mục Thanh toán giai đoạn, `_18` cần HĐ-1 **còn** vụ việc liên kết — vẫn đủ **3**). Không đụng dữ liệu đối tác.

## Ảnh

Không chụp — cả 2 vế `MATCH` đều đạt, không có FAIL cần chứng minh (flow 04 §7). Số liệu quyết định (số dòng trước/sau, giá trị từng ô, mốc giờ thông báo, mã phản hồi, bản ghi đọc lại) đã ghi thẳng trong bảng trên.
