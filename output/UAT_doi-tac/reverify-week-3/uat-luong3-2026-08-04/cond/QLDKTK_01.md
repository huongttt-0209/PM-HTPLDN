# Bảng đối chiếu điều kiện — QLDKTK_01 (dòng 321) — Doanh nghiệp tự đăng ký tài khoản

**Kết luận:** **Reopen** — đối tác báo đúng: nhập dữ liệu hoàn toàn mới vẫn bị chặn bằng câu "Mã số thuế đã tồn tại trong hệ thống"; đã tái hiện trên bản dựng mới và khoanh được nguyên nhân là ô "Tỉnh/Thành phố" chọn Hà Nội.

**Bản dựng đo:** `assets/index-DpIXRGaI.js` · nhãn `HTPLDN · V1.0.5` · 04/08/2026 15:10–15:30 (giờ VN)
**Tài khoản:** khách vãng lai (màn hình đăng ký không cần đăng nhập) · đối chiếu dữ liệu bằng `admin` và `cbnv_tw`

## Bảng đối chiếu

| Điều kiện có thể đổi kết quả | Đối tác phản ánh (vòng 2) | Mình đo lại (04/08/2026) | GAP? |
|---|---|---|:-:|
| Vai trò / tài khoản | Khách vãng lai, chưa đăng nhập, vào màn hình "Đăng ký tài khoản doanh nghiệp" | Giống hệt — mở `/register/doanh-nghiep` trong ngữ cảnh trình duyệt sạch, không đăng nhập | Không |
| Màn hình / thực thể + trạng thái | Màn hình đăng ký (SCR-VIII-08); chưa có bản ghi nào của doanh nghiệp này | Giống hệt — kiểm bằng `admin`: mã số thuế thử nghiệm không có trong danh sách doanh nghiệp lẫn danh sách tài khoản (0/0) | Không |
| Dữ liệu tiền đề | Mã số thuế `0155488787` chưa tồn tại — đối tác đã chụp màn hình tra cứu ra "Không tìm thấy doanh nghiệp phù hợp" | Dùng **6 mã số thuế khác nhau, tất cả đều mới tinh** (0155488787 · 0177342219 · 0388776611 · 0912345678 · 0765432198 · 0301998271) — cả 6 đều bị chặn | Không |
| Thao tác / dữ liệu nhập | Điền đủ trường bắt buộc rồi bấm **Đăng ký**; Tỉnh/Thành phố = **Hà Nội** | Giống hệt — điền đủ, Tỉnh/Thành phố = **Hà Nội**, bấm Đăng ký. Bắt được thân yêu cầu gửi đi đúng mã số thuế mới | Không |
| Bản dựng | Đối tác quay trên nhãn `HTPLDN · V1.0.2` ngày 31/07 | Đo trên nhãn `HTPLDN · V1.0.5` ngày 04/08 (mới hơn) — **vẫn nguyên lỗi** | Không |

## Kiểm từng ý của phiếu

- **Ý 1 — các trường trên biểu mẫu khớp tài liệu** (lỗi gốc vòng 1): ✅ **Đạt.** Biểu mẫu có **28 trường** đúng bằng danh sách thành phần màn hình `SCR-VIII-08` (24 trường thông tin doanh nghiệp + 4 trường tài khoản) và 2 nút Hủy / Đăng ký. "Tên đăng nhập" chỉ đọc, tự điền theo Mã số thuế. Chênh duy nhất: đặc tả ghi "Doanh nghiệp do nữ làm chủ" kiểu ô tích, ứng dụng làm công tắc và rút nhãn còn "Nữ làm chủ" — dev đã ghi nhận ở vòng 1.
- **Ý 2 — nhập thông tin hợp lệ rồi bấm Đăng ký thì đăng ký được**: ❌ **Lỗi.** Không đạt khi chọn Tỉnh/Thành phố = Hà Nội — hệ thống chặn, hiện "Mã số thuế đã tồn tại trong hệ thống". Đổi sang TP.HCM hoặc An Giang, giữ nguyên mọi thứ khác thì đăng ký chạy trọn.
- **Ý 3 — sau khi đăng ký hiện thông báo thành công + gửi thư kích hoạt**: ✅ **Đạt** (trên tỉnh chạy được). Hiện khung xanh "Đăng ký thành công, vui lòng kiểm tra email kích hoạt", tạo tài khoản trạng thái Chờ kích hoạt với tên đăng nhập = mã số thuế, và thư "Kích hoạt tài khoản doanh nghiệp" về đúng hộp thư.
- **Ý 4 — khi mã số thuế trùng thật thì báo đúng cách**: ✅ **Đạt.** Thử mã số thuế `5566778899` (đã có sẵn, thuộc TP.HCM): hiện đúng câu "Mã số thuế này đã có trong hệ thống. Vui lòng dùng chức năng *Quên mật khẩu*…" kèm nút "Quên mật khẩu".

⇒ Còn ý 2 lỗi nên toàn phiếu **Reopen**.

## Nguyên nhân đã khoanh được

Giữ nguyên toàn bộ dữ liệu nhập, **chỉ đổi mỗi ô Tỉnh/Thành phố**:

- TP. Hồ Chí Minh → đăng ký **thành công**, cấp mã `DN-HCM-0003`.
- **Hà Nội** → **bị chặn**, "Mã số thuế đã tồn tại trong hệ thống".
- An Giang → đăng ký **thành công**, cấp mã `DN-AGG-0004`.

Thứ bị trùng là **mã doanh nghiệp hệ thống tự cấp**, không phải mã số thuế người dùng nhập — luồng cán bộ nghiệp vụ
tạo hồ sơ doanh nghiệp ở Hà Nội nói thẳng điều đó: "**Mã doanh nghiệp** vừa bị trùng do thao tác đồng thời"
(thử 3 lần liên tiếp, 3 mã số thuế khác nhau, đều y hệt nên không phải do đồng thời), còn ở TP.HCM thì tạo được.
Luồng tự đăng ký gộp lỗi này vào `ERR-DN-02` nên câu báo ra màn hình sai bản chất.

Mã doanh nghiệp có dạng `DN-<mã tỉnh>-<số thứ tự>`; số thứ tự cấp cho Hà Nội đang đâm vào một mã đã tồn tại.

> **Đính chính 04/08/2026 16:00 — bản trước của file này ghi công thức "số bản ghi của tỉnh + 1". Công thức đó SAI.**
> Phép can thiệp trên môi trường dev đã bác bỏ: tự tạo lỗ hổng ở An Giang (`[1,2,4,5]`, đếm+1 = 5 đã có) thì đăng ký
> **vẫn chạy** và cấp `DN-AGG-0006`. Cũng không phải "số lớn nhất + 1" (Hà Nội còn số trống phía trên mà vẫn bị chặn).
> Công thức thật chưa xác định được từ ngoài; chi tiết + giả thuyết còn lại ở
> [`../reverify-audit/QLDKTK_01-moi-truong-dev.md`](../reverify-audit/QLDKTK_01-moi-truong-dev.md) §4–5.

**Kiểm chứng độc lập trên môi trường dev (`18.143.165.120.nip.io`):** cùng triệu chứng, xác định và lặp lại được —
Hà Nội chặn 2/2 lần, TP.HCM / Hải Phòng / Đà Nẵng / An Giang chạy 4/4 lần; luồng cán bộ ở Hà Nội cũng trả đúng
`ERR-STATE-SYS-00-01` "Mã doanh nghiệp vừa bị trùng". ⇒ lỗi mã nguồn, không phải sự cố dữ liệu riêng của UAT.

## Bằng chứng

- `image/QLDKTK_01-v2-01-tai-hien-bao-MST-da-ton-tai.png` — tái hiện đúng triệu chứng đối tác báo, trên bản dựng mới.
- `image/QLDKTK_01-v2-02-du-lieu-hoan-toan-moi-van-bi-chan.png` — biểu mẫu mã số thuế `0301998271` (mới tinh), Tỉnh/Thành phố = Hà Nội → khung đỏ "Mã số thuế đã tồn tại trong hệ thống", **không có** nút "Quên mật khẩu".
- `image/QLDKTK_01-v2-03-cung-bieu-mau-doi-tinh-TPHCM-dang-ky-thanh-cong.png` — cùng biểu mẫu, đổi tỉnh sang TP. Hồ Chí Minh → khung xanh "Đăng ký thành công, vui lòng kiểm tra email kích hoạt".
- `image/QLDKTK_01-v2-04-bieu-mau-dang-ky-28-truong-doi-chieu-dac-ta.png` — toàn bộ biểu mẫu 28 trường, dùng đối chiếu ý 1.
- `image/QLDKTK_01-v2-05-mst-trung-that-bao-dung-kem-nut-quen-mat-khau.png` — mã số thuế trùng THẬT → câu báo khác hẳn, kèm nút "Quên mật khẩu" ⇒ hai đường lỗi khác nhau.
- `../reverify-audit/QLDKTK_01/phep-thu-tach-bien-tinh.md` — bản ghi thô: thân yêu cầu + phản hồi 3 tỉnh, 2 luồng, và bảng mã doanh nghiệp theo tỉnh.
- `../reverify-audit/QLDKTK_01/frames/` — 7 khung hình cắt từ video đối tác; khung 04 giây cho thấy Tỉnh/Thành phố = Hà Nội, khung 16 giây cho thấy tra cứu mã số thuế ra "Không tìm thấy doanh nghiệp phù hợp".
- Mạng: `POST /api/v1/auth/register-doanh-nghiep` → **HTTP 409** `ERR-DN-02` (Hà Nội) · **HTTP 201** (TP.HCM, An Giang).
- Đối chiếu dữ liệu bằng `admin`: 6 mã số thuế thử nghiệm → 0 doanh nghiệp, 0 tài khoản; sau các lần bị chặn **không** sinh bản ghi dở dang nào.
- Hộp thư MailHog: nhận đủ thư "Kích hoạt tài khoản doanh nghiệp" cho 4 lần đăng ký thành công.

## Đặc tả đã tra

`Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-10-quan-tri.md`:

- dòng 1038 — điều kiện tiên quyết: "Mã số thuế và email đăng ký chưa tồn tại trong hệ thống".
- dòng 1078 — xử lý bước 1: chỉ được từ chối khi mã số thuế **đã có trong DOANH_NGHIEP**.
- dòng 1096 — lỗi E2 `ERR-REG-MST-EXIST`, kèm nút "Quên mật khẩu".
- dòng 1104–1108 — hậu điều kiện: tạo tài khoản Chờ kích hoạt + tạo doanh nghiệp + gửi thư kích hoạt.
- dòng 1115 — tiêu chí chấp nhận: điền đủ + tích cam kết → phải tạo được tài khoản và doanh nghiệp.
- dòng 1895–1939 — màn hình `SCR-VIII-08`: 24 thành phần thông tin doanh nghiệp + 4 thành phần tài khoản + 2 nút; **không** yêu cầu trang xác nhận riêng.
