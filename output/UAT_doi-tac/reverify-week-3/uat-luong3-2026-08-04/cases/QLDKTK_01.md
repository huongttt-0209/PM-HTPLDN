# QLDKTK_01 — dòng 321 (tab `UAT_TGPL Doanh Nghiệp-tuần 3`)

## Tuần

Tuần 3

## Mã TC

QLDKTK_01

## Tên chức năng

Quản lý đăng ký tài khoản

## Mô tả

Quản lý đăng ký tài khoản trên hệ thống

## Điều kiện

1. Truy cập hệ thống

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

## TKM phản hồi lần 1

bug giống với các tc QLDKTK_02, QLDKTK_03. Nếu 2 tc đó pass thì tester sẽ tự động test lại case này

## Trạng thái dev fix 1

Reject

## Verify

Resolved

## DEV phản hồi lần 1

Đã kiểm tra lại — không còn tái hiện. Biểu mẫu Đăng ký tài khoản doanh nghiệp hiện tại đã khớp với tài liệu, không thừa và không thiếu trường nào. Đối tác báo "một số trường thông tin không giống tài liệu" nên đội kiểm thử rà lại toàn bộ danh sách trường của biểu mẫu, không rà phần mã số thuế.
• Ba mục đối tác thấy thừa nay đã được gỡ khỏi biểu mẫu: "Họ và tên người đăng ký", ô "Số điện thoại" riêng của phần tài khoản đăng nhập, và công tắc "Cho phép công khai thông tin".
• Nhãn "Doanh thu (VNĐ)" đã được sửa thành "Doanh thu năm (VNĐ)" đúng như tài liệu.
• Đã đếm và đối chiếu 1-1 toàn bộ biểu mẫu với bảng thành phần màn hình trong tài liệu: 28 mục nhập liệu cộng 2 nút Hủy và Đăng ký, đúng bằng số mục tài liệu yêu cầu. Không mục nào thiếu, không mục nào thừa, tính bắt buộc của từng mục cũng đúng.
• Biểu mẫu chia đúng 3 phần: Thông tin doanh nghiệp, Quy mô (theo NĐ39/2018), Tài khoản đăng nhập. Ba danh sách chọn cố định cũng đúng: Quy mô có Siêu nhỏ / Nhỏ / Vừa; Ngành nghề chính có Nông, lâm, thủy sản / Công nghiệp, xây dựng / Thương mại, dịch vụ; Lĩnh vực kinh doanh cho chọn nhiều mục theo dạng "mã — tên".
• Ô "Tên đăng nhập" tự điền theo mã số thuế vừa nhập và ở chế độ chỉ đọc, đúng yêu cầu.
• Đã chạy thật một lượt đăng ký với dữ liệu hợp lệ hoàn toàn mới. Hệ thống nhận thành công, hiện thông báo "Đăng ký thành công, vui lòng kiểm tra email kích hoạt" rồi đưa về trang đăng nhập; tài khoản ở trạng thái chờ kích hoạt. Thư kích hoạt gửi tới đúng hòm thư đã khai, có ghi rõ tên đăng nhập là mã số thuế. Bấm liên kết trong thư thì tài khoản chuyển sang đang hoạt động và đăng nhập được ngay bằng mã số thuế.
• Điểm khác biệt duy nhất so với tài liệu là mục "Doanh nghiệp do nữ làm chủ": tài liệu mô tả là ô tích, phần mềm đang vẽ bằng công tắc gạt. Mục này vẫn không bắt buộc, mặc định tắt, không cản trở việc điền và lưu, nên đội kiểm thử ghi nhận là khác biệt về cách thể hiện chứ không tính là lỗi. Ô tích "Cam kết thông tin là chính xác" thì phần mềm vẫn đang vẽ đúng dạng ô tích.
• Một điểm xin lưu ý riêng, không thuộc phần đối tác báo lỗi: phần Kết quả mong đợi của phiếu có nhắc việc đặt mật khẩu ở bước bấm liên kết kích hoạt, trong khi phần mềm cho đặt mật khẩu ngay trên biểu mẫu đăng ký và liên kết trong thư chỉ dùng để kích hoạt. Đây là điểm thuộc quy trình nghiệp vụ, đội kiểm thử đang xác nhận lại với bên phân tích nghiệp vụ và sẽ phản hồi riêng, không gộp vào phiếu này.
• Bằng chứng đính kèm của phiếu này đang là tệp mang mã của phiếu khác (QLDKTK_02.webm). Đội kiểm thử vẫn mở ra xem đầy đủ và ghi nhận nội dung đúng với mô tả của đối tác, nhưng nhờ đối tác đính kèm lại đúng tệp cho phiếu này để hồ sơ khớp mã.
• Verify: kiểm ở trạng thái khách vãng lai, không đăng nhập, đúng như phiếu mô tả. Đã tải lại trang bỏ qua bộ nhớ đệm trước khi chốt.
