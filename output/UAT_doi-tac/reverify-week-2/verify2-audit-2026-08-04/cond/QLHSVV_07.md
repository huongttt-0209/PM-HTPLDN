# QLHSVV_07 — Bảng đối chiếu điều kiện (VÒNG SOÁT LẠI 2, 2026-08-04)

> Sheet `UAT_TGPL Doanh Nghiệp-tuần 2` row 128 · Verdict Verify 2: `Reopen`
> **Bug gốc:** ở nhóm "Tài liệu đính kèm" của Chi tiết vụ việc, bấm **biểu tượng "Tải xuống"** thì hệ thống **mở màn
> hình xem chi tiết** thay vì tải tệp. **Kết quả mong đợi:** *"Hệ thống tải tệp về máy người dùng."*
> **Loại bug:** kết quả phụ thuộc **tệp đính kèm được đưa vào bằng đường nào** + **trạng thái tệp trong kho lưu trữ**
> ⇒ KHÔNG phải bug tĩnh (không thể kết luận bằng việc "nhìn thấy 2 nút") ⇒ bắt buộc điền bảng này.

**Môi trường soát lại 2:** `https://htpldn-uat.ospgroup.vn` · `HTPLDN · V1.0.5` · gói giao diện **`index-DpIXRGaI.js`**
(môi trường dev vừa dựng bản vá).

| Điều kiện có thể đổi kết quả | Điều kiện bug gốc | Mình test (soát lại 2, 04/08/2026) | GAP? |
|---|---|---|:-:|
| Vai trò / tài khoản | Cán bộ Nghiệp vụ Trung ương (`CB_NV_TW`), đơn vị BTP · TW | **`cbnv_tw`** — `CB_NV_TW`, cấp TW, thanh trên hiện `BTP · TW`, tên hiển thị "Cán bộ NV Trung ương" ⇒ **trùng đúng** vai trò + cấp + đơn vị của bug gốc | Không |
| Màn hình + trạng thái entity | Chi tiết vụ việc → nhóm "Tài liệu đính kèm", cột "Thao tác"; vụ việc **đã tiếp nhận** | Đúng màn Chi tiết vụ việc → nhóm "Tài liệu đính kèm"; đo trên **2 vụ việc mới tạo hôm nay**, cả hai đều ở trạng thái **Đã tiếp nhận**: `VV-BTP-TW-20260804-003` và `VV-BTP-TW-20260804-005` | Không |
| Dữ liệu tiền đề — **tệp đính kèm** | "Tồn tại bản ghi chứa tệp đính kèm"; dev vòng 1 kiểm bằng **1 tệp ảnh JPG đã quét sạch** | Phủ **cả 2 đường đưa tệp vào hồ sơ**, tổng **13 tệp trên 6 vụ việc**: (a) **đính kèm ngay lúc tạo hồ sơ** — 4 tệp (loại "Yêu cầu"); (b) **bấm "Thêm tài liệu" ở màn chi tiết** — 9 tệp (loại "Bổ sung", gồm JPG/PDF/DOCX/XLSX). Tệp tự dựng: `QLHSVV_07-v2-anh-dinh-kem.jpg` (13 419 B), `QLHSVV_07-v2-tai-lieu-chinh.pdf`, `QLHSVV_07-v2-tep-dinh-kem-luc-tao-ho-so.pdf` (633 B) | Không |
| Thao tác được đo | Bấm **"Tải"**; và phải phân biệt với nút **"Xem"** (2 nút làm 2 việc khác nhau) | Bấm **cả 2 nút** trên cùng một hàng tệp, không chỉ nhìn biểu tượng: **"Xem"** → mở khung xem trước ngay trong trang; **"Tải"** → phải có tệp về máy. Đo trên **cả 2 nhóm tệp (a) và (b)** ở trên | Không |
| Phép đo "tệp có thực sự về máy không" | Dev vòng 1: "tệp nhận được có kích thước và nội dung y hệt tệp đã đính kèm"; lặp 3 lần, 2 lần sau khi tải lại trang | Với mỗi lượt bấm "Tải": ghi lại **thẻ tải xuống mà trang tạo ra** (đường dẫn + tên tệp), kiểm **tệp trong thư mục Tải xuống**, so **mã băm MD5** với tệp gốc, và đọc **mã trả về của lượt lấy tệp từ kho lưu trữ**. Bộ bắt thông báo dùng chung `tools/toast-capture.js`, tự kiểm `soObserverDangSong = 1` | Không |

## Kết quả đo

**Nhóm (b) — tệp thêm bằng nút "Thêm tài liệu" ở màn chi tiết: 9/9 tệp ĐẠT.**

- Hai nút là **hai nút riêng biệt** trong DOM: "Xem" (68×24, biểu tượng con mắt) và "Tải" (60×24, biểu tượng mũi tên
  tải xuống), nằm cách nhau trên cùng một hàng (ảnh `…-v2-01`).
- Bấm **"Xem"** trên tệp `QLHSVV_07-v2-anh-dinh-kem.jpg` → mở **khung xem trước ngay trong trang** (có phóng to, xoay),
  đọc được đúng chữ in trong ảnh; **không** tạo thẻ tải xuống nào, **không** đổi địa chỉ trang (ảnh `…-v2-02`).
- Bấm **"Tải"** trên đúng tệp đó → tạo thẻ tải xuống với tên `QLHSVV_07-v2-anh-dinh-kem.jpg`; **không** mở khung xem,
  **không** đổi địa chỉ trang. Tệp về máy **13 419 B**, **MD5 `d9b94c28a8b817abb6685709165d4a25` trùng khít tệp gốc**,
  so từng byte `giống nhau: True`.
- Lấy tệp từ kho lưu trữ cho **9/9** tệp nhóm này đều trả **mã 200** (trên 3 vụ việc khác nhau, gồm cả hồ sơ cũ ngày
  03/08 và 30/06) ⇒ triệu chứng cũ ("bấm Tải lại mở màn xem") **đã hết** ở nhóm này.

**Nhóm (a) — tệp đính kèm ngay lúc tạo hồ sơ: 4/4 tệp KHÔNG ĐẠT.**

- Tạo hồ sơ mới qua đúng luồng chuẩn (Vụ việc HTPL → Nhập thủ công → chọn doanh nghiệp → điền đủ trường bắt buộc →
  đính kèm 1 tệp PDF → [Lưu & Tiếp nhận]) ⇒ sinh `VV-BTP-TW-20260804-005`. Trên biểu mẫu, tệp hiện **đúng tên**
  `QLHSVV_07-v2-tep-dinh-kem-luc-tao-ho-so.pdf` **(633 B)**.
- Nhưng sau khi lưu, hàng tệp trong bảng "Tài liệu đính kèm" hiện **`File đính kèm 8e7566a5`** — tên tệp thật đã mất,
  cột **Định dạng bỏ trống**, cột **Kích thước hiện "—"** (ảnh `…-v2-03`).
- Bấm **"Tải"** trên hàng đó → **không có tệp nào về máy**, không tạo thẻ tải xuống nào, thay vào đó hiện thông báo
  **"Không kết nối được máy chủ."** (ảnh `…-v2-04` — bắt đúng khoảnh khắc thông báo còn trên màn). Bấm **"Xem"** cũng
  vậy.
- Lượt lấy tệp từ kho lưu trữ trả về **mã 404 — `NoSuchKey` "The specified key does not exist."** ⇒ **tệp chưa từng
  được lưu vào kho**, nên không nút nào lấy được.
- **Tái hiện 4/4**, trên 4 hồ sơ khác nhau — `…-20260804-001`, `…-002`, `…-003`, `…-005` — trong đó **001 và 002 không
  phải do tôi tạo**. Cùng lúc đó 9/9 tệp nhóm (b) vẫn lấy được bình thường ⇒ không phải lỗi mạng, không phải lỗi kho
  lưu trữ, mà đúng đường "đính kèm lúc tạo hồ sơ".

**Kết luận đo:** yêu cầu của phiếu — *"Hệ thống tải tệp về máy người dùng"* — **chỉ đúng với tệp thêm sau ở màn chi
tiết**, còn tệp người dùng đính kèm ngay lúc tạo hồ sơ thì **không bao giờ tải về được**. Đây đúng là tiền đề mà phiếu
mô tả ("tồn tại bản ghi chứa tệp đính kèm") ⇒ **fix mới đạt một phần → Reopen**.

## Đã cố BÁC BỎ / cố XÁC NHẬN kết luận `Pass` bằng những cách nào

1. **Cố Pass theo cách nhanh nhất — "nhìn thấy 2 nút Xem và Tải là xong"** → **KHÔNG chấp nhận**: bấm cả 2 nút, đo
   riêng từng nút, và kiểm tệp thật về máy.
2. **Nghi "Tải chỉ đổi biểu tượng chứ vẫn mở màn xem"** → **BÁC**: bấm Tải không mở khung xem nào (`khungXem = 0`),
   địa chỉ trang không đổi, và có thẻ tải xuống mang đúng tên tệp.
3. **Nghi "tải về nhưng tệp rỗng / sai nội dung"** → **BÁC**: MD5 tệp về máy trùng khít tệp gốc, so từng byte giống
   nhau, cùng kích thước và cùng loại ảnh.
4. **Nghi "chỉ đúng với ảnh, sai với tệp không xem trước được"** → đã phủ thêm PDF/DOCX/XLSX ⇒ đều lấy được (mã 200).
5. **Nghi "bản ghi cũ hỏng là bình thường, phải thử bản ghi mới"** (đúng luật: bug về trường lưu trong kho dữ liệu) →
   **đã tạo 2 hồ sơ MỚI hôm nay** qua luồng chuẩn. Chính **hồ sơ mới** mới là chỗ lộ ra phần chưa đạt.
6. **Nghi "lỗi 404 là do cách tôi nạp tệp bằng công cụ kiểm thử, không phải lỗi phần mềm"** → **BÁC**: 2 hồ sơ
   `…-001` và `…-002` **không phải do tôi tạo** cũng hỏng y hệt; và cùng công cụ đó nạp 9 tệp qua nút "Thêm tài liệu"
   thì lưu đúng 100%.
7. **Nghi "máy chủ/kho lưu trữ đang trục trặc lúc đo"** → **BÁC**: đo xen kẽ trong cùng vài phút — 9 tệp nhóm (b) trả
   200, 4 tệp nhóm (a) trả 404 `NoSuchKey`; thông báo "Không kết nối được máy chủ." là **chữ hiển thị sai bản chất**,
   máy chủ vẫn trả lời bình thường.
8. **Nghi "đây là bug khác, không thuộc phiếu này"** → cân nhắc và **giữ trong phiếu này**: yêu cầu của phiếu là bấm
   "Tải" thì tệp về máy; với tệp đính kèm lúc tạo hồ sơ thì bấm "Tải" **không** cho tệp về máy ⇒ đúng phạm vi phiếu.

**Kết luận: 0 GAP** — đúng vai trò/đơn vị, đúng màn hình, đúng trạng thái hồ sơ, phủ **cả hai** đường đưa tệp vào hồ
sơ và **cả hai** nút; phép đo dùng tệp thật + đối chiếu mã băm.
