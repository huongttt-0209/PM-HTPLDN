# Sao lưu nguyên văn dòng 321 — QLDKTK_01 (trước khi QA ghi đè cột R)

## Mã TC

QLDKTK_01

## Mô tả

Quản lý đăng ký tài khoản trên hệ thống

## Điều kiện

1. Truy cập hệ thống

## Dữ liệu đầu vào

(trống)

## Các bước thực hiện

1. Chọn "Đăng ký tài khoản doanh nghiệp"
2. Nhập thông tin hợp lệ và nhấn Đăng ký

## Kết quả mong đợi

Dữ liệu hợp lệ, hệ thống hiển thị trang xác nhận "Đăng ký thành công. Vui lòng kiểm tra thư điện tử và nhấn liên kết kích hoạt để đặt mật khẩu".

## Kết quả thực tế

Một số trường thông tin không giống với tài liệu

## Ảnh/vieo 1

QLDKTK_02.webm

## Trạng thái 1

Fail

## Trạng thái dev fix 1

Reject

## Verify

(trống)

## DEV phản hồi lần 1

KHÔNG phải bug: Chặn "MST đã tồn tại" khi MST đã có trong DOANH_NGHIEP là ĐÚNG SRS (srs-fr-10:1078). Triệu chứng do dữ liệu test (lượt trước đã tạo DN cùng MST) — dùng MST mới hoặc chức năng Quên mật khẩu để verify.
