# Row 186 — QLDKTK_03 — re-verify 2026-07-25 R5

Kết quả: **PASS** (đủ 4 điều kiện). Biểu mẫu công khai `/register/doanh-nghiep`, render bản chưa đăng nhập (browser context tách riêng, `localStorage` rỗng).

## Đối chiếu từng điều kiện

| Điều kiện | Kết quả | Bằng chứng |
|---|---|---|
| (i) Mục Tài khoản không còn "Họ và tên người đăng ký" + "Số điện thoại" người đăng ký | ✅ | a11y tree không có; truy vấn DOM `hoTen\|soDienThoaiTaiKhoan\|nguoiDangKy` trả về `[]` (kể cả input ẩn) |
| (ii) Mục Tài khoản đúng 4 mục: Tên đăng nhập chỉ đọc + Mật khẩu + Xác nhận mật khẩu + ô cam kết | ✅ | ô `Tự động theo Mã số thuế` có `disabled=true`; ảnh 01 |
| (iii) Tên đăng nhập bám Mã số thuế, đổi động không cần tải lại | ✅ | 3 lần đo: MST `0101234567` → tên đăng nhập `0101234567`; đổi `0107654321` → đổi theo; đổi `0198877665` → đổi theo |
| (iv) Đăng ký được chấp nhận, không lỗi bắt buộc trỏ vào 2 ô đã gỡ | ✅ | `POST /api/v1/auth/register-doanh-nghiep` → **201**, `trangThai: CHO_KICH_HOAT`, chuyển về `/login`; ảnh 02 |

## Chống điều kiện FAIL "ẩn khỏi giao diện nhưng vẫn gửi lên"

Payload thực tế gửi đi (bắt qua hook XHR trong trang) — **không có** `hoTen`, **không có** `soDienThoaiTaiKhoan`:

```json
{"password":"…","passwordConfirm":"…","dongYDieuKhoan":true,"captchaToken":"mock-captcha",
 "tenDoanhNghiep":"Công ty TNHH QA Reverify R5","maSoThue":"0198877665",
 "loaiDnId":"07a9d620-647d-4858-9b8d-5db754e914cc","diaChi":"Số 1 phố Kiểm Thử, quận Ba Đình",
 "tinhThanhId":"deac39eb-fdfd-4544-9f39-1c9cd77eb528","dienThoai":"0243888999",
 "email":"qa.reverify.r5.186b@example.com","nganhNghe":"NONG_LAM",
 "nguoiDaiDien":"Nguyễn Văn Kiểm Thử","quyMo":"SIEU_NHO"}
```

Response: `{"success":true,"data":{"id":"ed26b23c-6a09-4b5f-8fcb-4ce26c8a953a","trangThai":"CHO_KICH_HOAT",…}}`

## Đối chiếu 3 bẫy trong tiêu chí

- **Bẫy 1** — "Điện thoại doanh nghiệp" vẫn còn và vẫn bắt buộc (`* Điện thoại doanh nghiệp`), gửi lên dưới khoá `dienThoai`. Không tái phát QLDKTK_08.
- **Bẫy 2** — "Người đại diện" vẫn còn, bắt buộc, gửi lên dưới khoá `nguoiDaiDien`.
- **Bẫy 3** — lần submit đầu bị chặn vì MST `0107654321` đã tồn tại; đổi sang `0198877665` + email mới thì đăng ký được. Theo tiêu chí, không tính FAIL.

## Dữ liệu phát sinh

Tài khoản DN mới tạo trong lúc test: MST/tên đăng nhập `0198877665`, email `qa.reverify.r5.186b@example.com`, mật khẩu `Test@1234`, trạng thái `CHO_KICH_HOAT` (chưa kích hoạt qua email).
