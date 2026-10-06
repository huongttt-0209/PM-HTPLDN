# Bảng đối chiếu điều kiện — QLDKTK_04

Loại bug: **Nhập Mã số thuế ĐÃ TỒN TẠI rồi Đăng ký → thông báo lỗi thiếu nội dung hướng dẫn [Quên mật khẩu] + thiếu nút "Quên mật khẩu".** Verdict phụ thuộc dữ liệu: MST nhập vào phải là MST đã có hồ sơ trong hệ thống.

| Điều kiện có thể đổi kết quả | Đối tác | Mình test | GAP? |
|---|---|---|:-:|
| Vai trò | Khách chưa đăng nhập (form đăng ký công khai) | Khách chưa đăng nhập (form đăng ký công khai `/register/doanh-nghiep`) | Không |
| Màn hình / thao tác | Màn "Đăng ký tài khoản doanh nghiệp" → nhập MST đã tồn tại → bấm Đăng ký | Cùng màn → điền đủ trường bắt buộc + MST đã tồn tại → bấm Đăng ký | Không |
| Dữ liệu tiền đề (MST) | MST `0265484878` (đã có hồ sơ DN trong hệ thống) | MST `0109998887` (DN-HNI-0001, đã có hồ sơ DN trong hệ thống) — cùng điều kiện "MST đã tồn tại" | Không |
| Input các trường còn lại | Hợp lệ | Hợp lệ (email mới, mật khẩu đủ mạnh, đã tích cam kết) | Không |

**Kết luận: TÁI HIỆN.** Trên bản kiểm thử hiện tại (2026-07-21), submit đăng ký với MST đã tồn tại → API `POST /auth/register-doanh-nghiep` trả 409 `ERR-REG-MST-EXIST`, message backend "Mã số thuế này đã có hồ sơ doanh nghiệp. Vui lòng dùng chức năng \"Quên mật khẩu\" để kích hoạt tài khoản." NHƯNG UI chỉ hiển thị banner ngắn **"Mã số thuế này đã có hồ sơ doanh nghiệp trong hệ thống."** — thiếu phần hướng dẫn dùng [Quên mật khẩu] và **KHÔNG render nút "Quên mật khẩu"** (quét toàn trang: 0 button/link chứa "Quên mật khẩu"). Sai so với SRS FR-VIII-22 §Error Handling E2 `ERR-REG-MST-EXIST` (dòng 1082) + AC (dòng 1103): phải hiện thông báo đầy đủ kèm nút "Quên mật khẩu" dẫn sang FR-VIII-26. → **Open**. Bằng chứng: `BUG-QLDKTK_04-mst-exists-message.png` + network 409 body.
