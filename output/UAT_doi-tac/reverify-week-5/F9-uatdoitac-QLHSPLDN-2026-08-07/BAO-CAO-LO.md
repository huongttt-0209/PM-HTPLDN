# Báo cáo cuối lô F9 — tái xác nhận 6 case QLHSPLDN trên env nghiệm thu của đối tác

**Ngày:** 2026-08-07 · **Flow:** [`flows/03-reverify-sau-dev-fix.md`](../../../../flows/03-reverify-sau-dev-fix.md) — nhánh 2
*"Tái xác nhận trên môi trường khác"* · **Env:** `https://htpldn-uat.ospgroup.vn` (env NGHIỆM THU của đối tác)
**Tài khoản ra verdict:** `cbnv_tw` (`CB_NV_TW`, cấp TW) · `admin` chỉ dùng đọc màn Nhật ký ở `_07`.

---

## 1. Kết quả — 6/6 Pass

| Dòng | Mã TC | Verdict | Ô `Trạng thái dev fix` | Quan sát quyết định | Bản dựng khi đo |
|---|---|---|---|---|---|
| 291 | `QLHSPLDN_06` | **Pass** | `UAT done` | 7/7 hàng có nút Xem (2 cách đếm độc lập), bấm chuột thật 5 lượt phủ 4 dạng, mỗi cửa sổ khớp **10/10 trường** với bản ghi đọc lại từ máy chủ; 0 ô nhập + 0 nút lưu | `index-D4NhKEjr.js` |
| 292 | `QLHSPLDN_07` | **Pass** | `UAT done` | 4 lượt bấm lưu × **2 đường độc lập đều khớp** (tải lại trang thật · đọc lại bản ghi từ máy chủ); phủ được dạng *chỉ thêm tệp* mà 2 vòng trước bỏ sót; nhật ký hệ thống đủ 4 dòng đúng giây bấm | `index-D4NhKEjr.js` |
| 293 | `QLHSPLDN_11` | **Pass** | `UAT done` | Bảng **4 → 3 → 2** hàng; `total` máy chủ + danh sách mã khớp từng lượt. Chạy **đủ 2 biến thể** (chỉ từ khóa · kết hợp thêm bộ lọc) — con số 2 loại trừ được cả 3 phương án khác ⇒ chứng minh lọc chồng nhau | `index-D4NhKEjr.js` |
| 294 | `QLHSPLDN_12` | **Pass** | `UAT done` | Chữ trên màn khớp **0 ký tự lệch** (36/36 điểm mã) với `:701`; máy chủ trả rỗng `total=0`; đã loại ca *câu chữ cứng* (từ khóa khác vẫn ra 3–4 hàng) và ca *khung chớp* | `index-D4NhKEjr.js` |
| 295 | `QLHSPLDN_13` | **Pass** | `UAT done` | Thông báo khớp **0 ký tự lệch** (37/37) với `:700`; **đúng 1 thông báo** — bộ quan sát ghi 2 lượt thêm node nhưng kiểm định danh cho thấy **cùng một node**; bấm lặp cho kết quả y hệt | `index-D4NhKEjr.js` |
| 296 | `QLHSPLDN_14` | **Pass** | `UAT done` | **Mở nội dung tệp `.xlsx` ra đọc**: tiêu đề đủ **8 trường đúng thứ tự**; xuất **2 lượt** — không lọc → 4 dòng, có lọc → 2 dòng đúng tập con, loại được cả 2 bản ghi "khớp một nửa" | `index-Bd1akG3f.js` |

**Dòng 297 `QLHSPLDN_15`** không thuộc phạm vi (đang `BA confirm`) — không đụng.

**Hiệu lực:** cả 6 ô `Kết quả verify` đã được ghi đè bằng kết quả đo trên chính env nghiệm thu. Câu *"Pass tạm cho
tới khi bản dựng lên môi trường nghiệm thu"* của vòng env nội bộ **đã được đóng**.

---

## 2. Bản dựng — env deploy 2 lần trong lô

| Bó mã | `last-modified` | Giờ VN | Case đo trên bản này |
|---|---|---|---|
| `assets/index-D4NhKEjr.js` · etag `W/"6a755c73-428"` | Fri, 07 Aug 2026 04:17:55 GMT | **11:17** | 291 · 292 · 293 · 294 · 295 |
| `assets/index-Bd1akG3f.js` · etag `W/"6a759424-428"` | Fri, 07 Aug 2026 08:15:32 GMT | **15:15** | 296 |

Mọi case đều đo vân tay ở **cả đầu và cuối phiên**, và đều trùng khớp 2 đầu ⇒ không có case nào bị deploy chen
giữa. Cú deploy 15:15 rơi vào **sau khi 5 case đầu đã đo xong**. Sidebar ghi `V1.0.10` ở **cả hai** bản dựng ⇒
xác nhận lại kết luận cũ: **chuỗi `V1.0.x` không dùng làm định danh bản dựng được**, chỉ bó mã + `last-modified`
mới là vân tay thật.

⚠️ **Giới hạn hiệu lực:** 5 verdict đầu gắn với bản dựng `index-D4NhKEjr.js`, mà bản đó **không còn chạy trên
env**. Chúng vẫn hợp lệ cho đúng bản đã đo, nhưng nếu cần khẳng định trên bản `index-Bd1akG3f.js` thì phải đo lại.

---

## 3. Bug mới đã log

**`QLHSPLDN_QA01`** — dòng **379** tab `bug` · `Trạng thái = Fail` · `Dopai = bug` · có link ảnh xem được.

Bản dựng 15:15 bật hộp thoại **"Cập nhật thông tin bắt buộc" đòi số CCCD**: không nút đóng, Escape không tắt,
bấm ra ngoài không tắt, và **che nút chức năng phía sau** (tại thẻ Hồ sơ pháp lý chỉ còn ló nút *Tìm kiếm*; *Xóa
bộ lọc* và *Xuất Excel* bị che hoàn toàn, cú bấm rơi vào lớp phủ). Tái hiện 2/2 lần tải lại. Chặn cứng tài khoản
cán bộ nội bộ cho tới khi nhập.

Trái đặc tả ở 4 chỗ (đã mở file xác minh): `srs-v3.5.md:5543` (BR-AUTH-13 — cán bộ nội bộ *"không cần định danh
công dân"*) · `srs-v3.5.md:5642` (BR-INTG-06 — *"không cần CCCD vì user là cán bộ nội bộ"*) ·
`srs-fr-10-quan-tri.md:1734` (trường CCCD *"Không bắt buộc"*) · `:2110` (cccd nullable, nguồn từ VNeID chứ không
phải người dùng tự khai).

Đây là **lỗi chặn toàn hệ thống**, không riêng màn hồ sơ pháp lý.

---

## 4. Dữ liệu đã tạo / thay đổi trên env đối tác

| Bản ghi | Thay đổi | Case | Ghi chú |
|---|---|---|---|
| `HSPL-20260807-0001` · `-0002` · `-0003` | **Tạo mới** trên DN QA `DN-HCM-0004` (`ac4a3173-…fc6`) | 291 | Phủ 4 dạng dữ liệu bắt buộc |
| `HSPL-20260807-0004` · `-0005` | **Tạo mới** cùng DN QA | 292 | 4 lượt bấm lưu chạy trên 2 bản ghi này |
| Tài khoản `cbnv_tw` — trường `cccd` | `null` → `000000000001` lúc **15:34:32 VN** qua `PATCH /api/v1/auth/me/cccd` | 296 | **Chủ việc phê duyệt trước khi làm.** Bắt buộc để qua hộp thoại chặn |

🔴 **Không thêm / sửa / xoá bất kỳ bản ghi nào của đối tác.** `DN-XX-0005` (`1a715c55-…3ce5`),
`HSPL-20260803-0001`, `HSPL-20260731-0002` chỉ được ĐỌC — các case tìm kiếm / lọc / xuất chạy trên chính DN đó vì
đó là thao tác đọc.

⚠️ **Chưa hoàn nguyên được:** `cccd` của `cbnv_tw` nay còn `000000000001`. Giao diện không có đường xoá; muốn trả
lại `null` phải làm ở tầng quản trị hệ thống hoặc cơ sở dữ liệu.

---

## 5. Chỗ vòng trước làm chưa tới, lô này sửa

1. **`_11` từng Pass khi mới chạy 1/2 biến thể bắt buộc.** Tiêu chí chấp nhận `:711` và chính ô phiếu
   (*"nhập từ khóa **và/hoặc** chọn bộ lọc"*) nêu đích danh biến thể kết hợp ≥2 điều kiện; vòng env nội bộ chỉ
   chạy tìm theo từ khóa. Theo Flow 03 đó là **Chưa chốt**, không phải Pass. Lô này chạy đủ 2 biến thể.
2. **Số dòng SRS đã dịch.** `srs-fr-12`, `srs-fr-10`, `srs-v3.5.md` được sửa lúc **06/08 22:52** — sau khi
   `tieuchi/QLHSPLDN_06.md` và `_07.md` được viết (18:48) và sau vòng đo env nội bộ. Nội dung không đổi, số dòng
   dịch **+13** ở phần FR và **+27** ở phần Entity/SCR. ⇒ ô `Kết quả verify` cũ của dòng 291–292 quote số dòng
   lỗi thời; lô này ghi đè bằng số dòng bản hiện tại.
3. **`_07` vế lưu vết thao tác** từng bị xếp là *"đặc tả im lặng về bề mặt đọc log"*. Đọc lại
   `srs-fr-10-quan-tri.md:1981`, `:1982`, `:1984` cho thấy có đủ bề mặt ⇒ đường đọc màn Nhật ký là **đường
   chính**, không phải phương án dự phòng. Lô này đóng vế đó bằng chính đường chính.

---

## 6. Phần chưa đo được

| Điểm | Vì sao | Cần gì để đóng |
|---|---|---|
| Ngưỡng **10.000 dòng** của xuất Excel (`srs-fr-12:663`) | Env chỉ có 4 hồ sơ trên DN đang đo | Seed khối lượng lớn, hoặc kiểm ở tầng truy vấn |
| Chiều **"bản ghi có từ trước bản vá"** của `_07` | Env đối tác không có bản ghi QA nào cũ hơn bản dựng 11:17 hôm nay; 2 hồ sơ cũ thật là dữ liệu đối tác nên không được đụng | Một hồ sơ tạo trước bản vá mà QA được phép sửa, hoặc đối tác tự thử lại trên hồ sơ cũ của họ rồi báo kết quả |
| Hiệu lực của 5 verdict đầu trên bản dựng `index-Bd1akG3f.js` | 5 case đo xong trước cú deploy 15:15 | 1 lượt đo lại nếu cần khẳng định trên bản đang chạy |
| Nhánh *không ra kết quả do chọn bộ lọc* (thay vì gõ từ khóa) ở `_12` | Lô cố ý chốt 1 cách dựng tình huống, không tự mở rộng | Dựng được ngay mà vẫn chỉ đọc: DN đang xem không có hồ sơ loại *Giấy phép* và không có trạng thái *Thu hồi* |

---

## 7. Việc còn tồn của hồ sơ nội bộ (không ảnh hưởng verdict)

1. **Bug Summary Table** của `BUG-HSPLDN-QLHSPLDN-06` và `-07` trong [`../bug-report.md`](../bug-report.md) còn
   quote **số dòng SRS bản cũ** (`:550`, `:634`, `:640-642`, `:693`, `srs-v3.5.md:6714`, `:607`, `:613`, `:674`).
   Số hiện tại: `:563`, `:647`, `:653-655`, `:706`, `:6758`, `:626`, `:627`, `:687`. Sửa cần **edit nguyên tử**
   theo quy tắc severity-sync của repo.
2. **Header `**Ngày**`** của [`../bug-report.md`](../bug-report.md) và
   [`../F4-pilot-QLHSPLDN-2026-08-07/bug-report.md`](../F4-pilot-QLHSPLDN-2026-08-07/bug-report.md) đang stale so
   với timestamp mới nhất trong body (các dòng Re-test 07/08 14:20–15:00). Bump sẽ mâu thuẫn với 2 dòng header
   `Môi trường` / `Bản dựng` đang mô tả vòng 06/08 ⇒ cần quyết cách xử, không tự bump.
3. **Trình duyệt** còn mở, phiên `cbnv_tw` trên env đối tác còn sống — đóng được khi không còn lô nào chạy.

---

## 8. Ghi chú phối hợp

Lô này chạy **hoàn toàn trên env đối tác**, không đụng env nội bộ `18.143.165.120.nip.io`.

🔴 **Thông tin dưới đây CHƯA đến được phiên G1** (phiên đang verify 11 bug `Dopai=BA` trên env nội bộ).
G1 nhắn sang hỏi về mã OTP `cbnv_tw_03` lúc 15:33 trên MailHog env nội bộ; câu trả lời của tôi **gửi nhầm
sang một phiên khác** (phiên đó đã báo lại là họ không phải G1). `ListAgents` từ phiên này chỉ thấy đúng
một peer và **không phải G1**, nên không có đường gửi lại. Cần người điều phối chuyển tay 4 ý sau:

1. Mã OTP `cbnv_tw_03` lúc 15:33 trên MailHog env nội bộ **không phải của lô này** — lô này chỉ đăng nhập
   `cbnv_tw` trên env đối tác, không sinh OTP nào trên env nội bộ.
2. Phạm vi lô này là **dòng 291–296**, không phải 291–294 như G1 đang ghi.
3. Đã thêm **dòng 379 `QLHSPLDN_QA01`** vào sheet bug — G1 tránh cấp trùng số `_QA01`.
4. Cảnh báo trước: bản dựng `index-Bd1akG3f.js` có **hộp thoại CCCD chặn cứng** (không nút đóng, Escape và
   nền đều không tắt) — nếu bản đó lên env nội bộ thì mọi lô đang chạy sẽ tắc ở đó.
