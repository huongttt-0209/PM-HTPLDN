# Nhật ký đo — QLDKTK_01 (dòng 321) — vòng 2 — 04/08/2026

**Môi trường:** `https://htpldn-uat.ospgroup.vn`
**Bản dựng:** `assets/index-DpIXRGaI.js` · nhãn sidebar `HTPLDN · V1.0.5`
**Tài khoản dùng:** khách vãng lai (màn hình đăng ký công khai) · `admin` (`Secret@123`) và `cbnv_tw` (`Test@1234`) để đối chiếu dữ liệu
**Bộ bắt thông báo:** `tools/toast-capture.js` — tự kiểm `soObserverDangSong = 1` trước mỗi lần đo

---

## 0. Cổng bằng chứng — đọc phần đối tác bổ sung vòng 2

Cột "Kết quả thực tế lần 2" (S): *"Hệ thống hiển thị thông báo 'Mã số thuế đã tồn tại trong hệ thống' mặc dù MST chưa tồn tại trong hệ thống"*.
Cột "Ảnh/video 2" (T): `QLDKTK_01_v2.webm` — đã tải về `partner-evidence/QLDKTK_01_v2.webm` (4.845.347 byte), cắt 7 khung hình vào `QLDKTK_01/frames/`.

Đọc khung hình:

| Khung | Thấy gì |
|---|---|
| `t004.02s.jpg` | Màn hình `/register/doanh-nghiep`, khung đỏ "Mã số thuế đã tồn tại trong hệ thống"; biểu mẫu điền Công ty TNHH TKM VN, mã số thuế `0155488787`, **Tỉnh/Thành phố = Hà Nội**; nhãn bản dựng `HTPLDN · V1.0.2`, ngày máy 31/07/2026 |
| `t016.05s.jpg` | Cùng người đó đăng nhập quản trị viên, vào Danh sách doanh nghiệp, tìm `0155488787` → "**Không tìm thấy doanh nghiệp phù hợp**" |

⇒ Đối tác đã tự chứng minh mã số thuế không tồn tại mà vẫn bị chặn. Bằng chứng đủ để mở phép đo, không phải thao tác sai.

---

## 1. 15:05 — Tái hiện trên bản dựng mới

Mở `/register/doanh-nghiep` trong ngữ cảnh trình duyệt sạch. Điền đủ trường bắt buộc, Tỉnh/Thành phố = **Hà Nội**, bấm Đăng ký.

```json
{"thoiDiemBam":"2026-08-04T08:10:23.016Z","SO_REQUEST":1,
 "request":["POST /api/v1/auth/register-doanh-nghiep"],
 "SO_KHUNG":1,"chu":["Mã số thuế đã tồn tại trong hệ thống"],
 "phanHoi":[{"status":409,"body":"{\"success\":false,\"error\":{\"code\":\"ERR-DN-02\",\"field\":\"maSoThue\",\"message\":\"Mã số thuế đã tồn tại trong hệ thống\"}}"}]}
```

Ảnh: `image/QLDKTK_01-v2-01-tai-hien-bao-MST-da-ton-tai.png` — khung đỏ ngay đầu biểu mẫu, đúng câu đối tác báo.

**⇒ Tái hiện được trên bản mới hơn bản đối tác quay.**

## 2. 15:08 — Loại giả thuyết "mã số thuế đó trùng thật"

Thử lần lượt **6 mã số thuế khác nhau**, mỗi lần tải lại trang sạch và nhập lại từ đầu:
`0155488787` · `0177342219` · `0388776611` · `0912345678` · `0765432198` · `0301998271` → **cả 6 đều HTTP 409 `ERR-DN-02`**.

Bắt được thân yêu cầu thật sự gửi đi ở lần cuối (bọc `XMLHttpRequest.prototype.send` vì ứng dụng dùng XHR chứ không dùng fetch):

```json
{"m":"POST","u":"/api/v1/auth/register-doanh-nghiep",
 "body":"{...\"captchaToken\":\"mock-captcha\",\"tenDoanhNghiep\":\"Cong ty QA Sach V2 991827\",\"maSoThue\":\"0301998271\",\"email\":\"qa.sach.991827@example.com\",\"nganhNghe\":\"THUONG_MAI\",\"quyMo\":\"NHO\"}",
 "status":409,
 "resp":"{\"success\":false,\"error\":{\"code\":\"ERR-DN-02\",\"field\":\"maSoThue\",\"message\":\"Mã số thuế đã tồn tại trong hệ thống\"}}"}
```

Ảnh: `image/QLDKTK_01-v2-02-du-lieu-hoan-toan-moi-van-bi-chan.png`.

Đối chiếu bằng `admin`: cả 6 mã số thuế → **0 doanh nghiệp, 0 tài khoản**. Tổng số tài khoản trước/sau đều 212 ⇒ các lần bị chặn **không** để lại bản ghi dở dang.

## 3. 15:15 — Đối chiếu biểu mẫu với đặc tả màn hình (ý 1 — lỗi gốc vòng 1)

Đọc `SCR-VIII-08` (`srs-fr-10-quan-tri.md` dòng 1895–1939): 24 thành phần nhóm "Thông tin doanh nghiệp" + 4 thành phần nhóm "Tài khoản đăng nhập" + 2 nút.

Đếm trên màn hình thực: **28 trường**, khớp đủ; 2 nút Hủy / Đăng ký. "Tên đăng nhập" chỉ đọc, tự điền theo Mã số thuế.
Chênh duy nhất: dòng 24 đặc tả ghi "Doanh nghiệp do nữ làm chủ" kiểu **ô tích**, ứng dụng làm thành **công tắc** và rút nhãn còn "Nữ làm chủ" — dev đã ghi nhận ở vòng 1, không đổi kết quả nghiệp vụ.

Ảnh: `image/QLDKTK_01-v2-04-bieu-mau-dang-ky-28-truong-doi-chieu-dac-ta.png`. **⇒ ý 1 đạt.**

## 4. 15:20 — Phép thử tách biến: chỉ đổi ô Tỉnh/Thành phố

Gọi thẳng `POST /api/v1/auth/register-doanh-nghiep`, giữ nguyên toàn bộ thân yêu cầu, chỉ đổi `tinhThanhId`:

| Tỉnh/Thành phố | Mã số thuế | Kết quả |
|---|---|---|
| TP. Hồ Chí Minh | 0311224455 | **HTTP 201** — tạo tài khoản Chờ kích hoạt, cấp mã `DN-HCM-0003` |
| Hà Nội | 0311224466 | **HTTP 409** `ERR-DN-02` |
| An Giang | 0311224477 | **HTTP 201** — cấp mã `DN-AGG-0004` |

Lặp lại ở luồng cán bộ nghiệp vụ (`POST /api/v1/doanh-nghieps`, tài khoản `cbnv_tw`):

| Tỉnh/Thành phố | Kết quả |
|---|---|
| TP. Hồ Chí Minh | **HTTP 201** — cấp mã `DN-HCM-0004` |
| Hà Nội | **HTTP 409** `ERR-STATE-SYS-00-01` "**Mã doanh nghiệp** vừa bị trùng do thao tác đồng thời. Vui lòng thử lại." |

Hà Nội đã thử 3 lần liên tiếp cách nhau 1 giây với 3 mã số thuế khác nhau — cả 3 lần y hệt, nên **không phải** do thao tác đồng thời.

Bản ghi thô: `QLDKTK_01/phep-thu-tach-bien-tinh.md`.

## 5. 15:24 — Đọc quy luật cấp mã doanh nghiệp

Đọc toàn bộ 47 doanh nghiệp (`GET /api/v1/doanh-nghieps`, 3 trang), nhóm theo tiền tố tỉnh:

```
tỉnh   số bản ghi  số thứ tự đang có                             (số bản ghi + 1)
HNI            13  [1,2,3,4,5,6, 11,12,13,14,15,16,17]                       14  *** TRÙNG DN-HNI-0014
HCM             2  [1,2]                                                      3  trống
AGG             3  [1,2,3]                                                    4  trống
… 10 tỉnh còn lại đều liền mạch, đều trống
```

Quan sát mã được cấp: TP.HCM đang 2 bản ghi → bản mới được cấp `DN-HCM-0003`; rồi 3 bản ghi → cấp `DN-HCM-0004`; An Giang 3 bản ghi → cấp `DN-AGG-0004`.

> **⚠️ ĐÍNH CHÍNH 04/08/2026 16:00 — mục này ban đầu kết luận "mã cấp theo số bản ghi + 1". KẾT LUẬN ĐÓ SAI.**
> Phép can thiệp trên môi trường dev đã bác: tự tạo lỗ hổng ở An Giang (`[1,2,4,5]`, đếm+1 = 5 đã có) thì đăng ký
> **vẫn chạy** và cấp `DN-AGG-0006`. "Số lớn nhất + 1" cũng bị bác (Hà Nội còn số trống phía trên mà vẫn bị chặn).
> Trên UAT công thức "đếm+1" khớp chỉ vì số bản ghi tình cờ bằng giá trị bộ đếm.
> Điều CHẮC CHẮN vẫn đứng: thứ bị trùng là **mã doanh nghiệp hệ thống tự cấp** (luồng cán bộ nói thẳng), lỗi
> phụ thuộc ô Tỉnh/Thành phố, chỉ Hà Nội dính. Chi tiết: [`QLDKTK_01-moi-truong-dev.md`](QLDKTK_01-moi-truong-dev.md).

## 6. 15:27 — Chạy trọn luồng ở tỉnh không bị chặn (ý 3)

Điền cùng biểu mẫu trên giao diện, Tỉnh/Thành phố = TP. Hồ Chí Minh, mã số thuế `0311663388`:

```json
{"thoiDiemBam":"2026-08-04T08:25:39.267Z","SO_REQUEST":1,
 "request":["POST /api/v1/auth/register-doanh-nghiep"],
 "SO_KHUNG":1,"chu":["Đăng ký thành công, vui lòng kiểm tra email kích hoạt"],
 "duongDanHienTai":"/login"}
```

Ảnh: `image/QLDKTK_01-v2-03-cung-bieu-mau-doi-tinh-TPHCM-dang-ky-thanh-cong.png` (chụp theo cách hẹn giờ bấm 2500 ms rồi mới chụp, nên bắt được khung xanh trước lúc nó tự tắt).

Hậu điều kiện kiểm bằng `admin`:
- Tài khoản `0311663388` — trạng thái `CHO_KICH_HOAT`, thư điện tử `qa.tinhkhac.663388@example.com`, **tên đăng nhập = mã số thuế** ✅
- MailHog nhận thư "Kích hoạt tài khoản doanh nghiệp" lúc `08:26:41` ✅ (cả 4 lần đăng ký thành công đều có thư)

Đặc tả `SCR-VIII-08` **không** yêu cầu trang xác nhận riêng, nút Đăng ký chỉ cần submit; câu thông báo của ứng dụng khác chữ với ô "Kết quả mong đợi" của phiếu nhưng cùng nghĩa ⇒ không tính là lỗi.

## 7. 15:29 — Kiểm nhánh mã số thuế trùng THẬT (ý 4)

Đăng ký với mã số thuế `5566778899` (đã có sẵn, thuộc TP.HCM), Tỉnh/Thành phố = TP.HCM:

> "Mã số thuế này đã có trong hệ thống. Vui lòng dùng chức năng "Quên mật khẩu" với chính mã số thuế của bạn để khôi phục hoặc nhận lại quyền truy cập tài khoản." **+ nút "Quên mật khẩu"**

Ảnh: `image/QLDKTK_01-v2-05-mst-trung-that-bao-dung-kem-nut-quen-mat-khau.png`.

Khớp đúng dòng 1096 đặc tả (`ERR-REG-MST-EXIST`). **⇒ Nhánh trùng thật đã làm đúng.**
Điều này cũng chứng minh trường hợp Hà Nội đi **đường lỗi khác** — chữ khác, không có nút — nên không thể coi là "hệ thống phát hiện trùng".

---

## Kết luận

**Reopen.** Ý 1, 3, 4 đạt; **ý 2 vẫn lỗi**: doanh nghiệp có địa chỉ ở Hà Nội không đăng ký được tài khoản, hệ thống trả về câu báo lệch hẳn bản chất ("mã số thuế đã tồn tại") nên người dùng không có cách nào tự xử lý.

**Nguyên nhân đã khoanh:** mã doanh nghiệp hệ thống tự cấp cho Hà Nội bị trùng với một mã đã tồn tại; đụng ràng buộc duy nhất rồi bị quy nhầm sang lỗi mã số thuế. Công thức sinh số thứ tự **chưa xác định được từ ngoài** (xem đính chính §5).

**Đã kiểm chứng độc lập trên môi trường dev** — cùng triệu chứng, xác định, chỉ Hà Nội ⇒ lỗi mã nguồn chứ không phải sự cố dữ liệu riêng của UAT. Nhật ký: [`QLDKTK_01-moi-truong-dev.md`](QLDKTK_01-moi-truong-dev.md).

## Dữ liệu QA tạo trên môi trường (để dev/BA biết mà bỏ qua)

| Mã doanh nghiệp | Mã số thuế | Tỉnh | Tạo bằng |
|---|---|---|---|
| DN-HCM-0003 | 0311224455 | TP.HCM | tự đăng ký qua API |
| DN-AGG-0004 | 0311224477 | An Giang | tự đăng ký qua API |
| DN-HCM-0004 | 0311224488 | TP.HCM | `cbnv_tw` tạo qua API |
| (cấp tiếp theo) | 0311552277 | TP.HCM | tự đăng ký qua giao diện |
| (cấp tiếp theo) | 0311663388 | TP.HCM | tự đăng ký qua giao diện |

Kèm 5 tài khoản trạng thái Chờ kích hoạt tương ứng (tên đăng nhập = mã số thuế) và 4 thư kích hoạt trong MailHog.

> **Đừng xóa các bản ghi này bằng tay.** Xóa sẽ tạo lỗ hổng trong dãy số của TP.HCM / An Giang và làm 2 tỉnh đó dính đúng lỗi của Hà Nội.
