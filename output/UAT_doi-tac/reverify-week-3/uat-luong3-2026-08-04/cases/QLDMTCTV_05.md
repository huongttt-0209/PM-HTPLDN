# QLDMTCTV_05 — dòng 318 (tab `UAT_TGPL Doanh Nghiệp-tuần 3`)

## Tuần

Tuần 3

## Mã TC

QLDMTCTV_05

## Mô tả

Chọn thẻ trạng thái

## Điều kiện

1. Đăng nhập tài khoản

## Các bước thực hiện

1. Chọn menu "Mạng lưới tư vấn viên" => "Tổ chức tư vấn"
2. Chọn 1 trong 6 thẻ: "Đang hoạt động" / "Chờ phê duyệt" / "Mới đăng ký" / "Đã từ chối" / "Tạm dừng" / "Vô hiệu hóa"

## Kết quả mong đợi

- Hệ thống lọc danh sách theo trạng thái tương ứng; mỗi thẻ hiển thị số đếm bản ghi.
- Thẻ "Mới đăng ký" có nhãn đỏ nếu có tổ chức chưa trình phê duyệt; thẻ "Chờ phê duyệt" chỉ hiển thị với người dùng có vai trò Cán bộ phê duyệt.

## Kết quả thực tế

- Mỗi thẻ không hiển thị số đếm
- Thẻ "Mới đăng ký" không có nhãn đỏ mặc dù tồn tại tổ chức chưa trình duyệt
- Thẻ "Chờ phê duyệt" hiển thị đối với CBNV

## Ảnh/vieo 1

QLDMTCTV_05.jpg

## Trạng thái 1

Fail

## Trạng thái dev fix 1

dev done

## Verify

Pass

## DEV phản hồi lần 1

Đã kiểm tra lại — lỗi đã được khắc phục, chức năng chọn thẻ trạng thái ở màn Tổ chức tư vấn chạy đúng. Kiểm ở đúng vai trò Cán bộ Nghiệp vụ Trung ương và đúng đơn vị Bộ Tư pháp - Trung ương như trong ảnh đối tác gửi. Cả 3 ý đối tác nêu đều không còn tái hiện:
• Ý 1 — "Mỗi thẻ không hiển thị số đếm": ĐÃ CÓ. Nay mỗi thẻ hiện số bản ghi ngay cạnh tên thẻ, và số này khớp đúng số dòng trong bảng: "Đang hoạt động" là 3 (bảng 3 dòng), "Mới đăng ký" là 1 (bảng 1 dòng), "Chờ phê duyệt" là 1 (bảng 1 dòng). Đội kiểm thử đã thử thêm một tổ chức mới rồi tải lại trang, số đếm tự tăng theo đúng dữ liệu thật chứ không phải số cố định. Lưu ý nhỏ: thẻ nào chưa có bản ghi nào thì để trống, không hiện số 0.
• Ý 2 — "Thẻ Mới đăng ký không có nhãn đỏ mặc dù tồn tại tổ chức chưa trình duyệt": ĐÃ CÓ. Khi thẻ "Mới đăng ký" đang rỗng thì không có dấu hiệu gì; khi có tổ chức chưa trình phê duyệt thì thẻ này hiện huy hiệu NỀN ĐỎ mang số lượng, trong khi thẻ "Đang hoạt động" cùng lúc vẫn là nền xanh. Tức dấu hiệu đỏ chỉ bật đúng lúc còn hồ sơ chưa trình. Vì đầu phiên kiểm thử thẻ này đang rỗng nên đội kiểm thử đã tự tạo một tổ chức mới và cố ý KHÔNG trình phê duyệt để dựng đúng tình huống đối tác mô tả, rồi mới đo.
• Ý 3 — "Thẻ Chờ phê duyệt hiển thị đối với CBNV": ĐÃ ĐƯỢC ẨN. Đăng nhập vai trò Cán bộ Nghiệp vụ chỉ thấy 5 thẻ, không còn thẻ "Chờ phê duyệt". Đăng nhập vai trò Cán bộ Phê duyệt cùng đơn vị mới thấy đủ 6 thẻ, trong đó có "Chờ phê duyệt". Đây đúng là cách phân quyền mong muốn.
• Kiểm tra thêm phần lọc: bấm lần lượt cả 6 thẻ thì danh sách đều lọc đúng theo trạng thái tương ứng, không có dòng nào lọt sai thẻ.
• Verify: tài khoản Cán bộ Nghiệp vụ Trung ương (cbnv_tw_04) là vai trò trùng với ảnh đối tác, đối chiếu thêm bằng tài khoản Cán bộ Phê duyệt Trung ương cùng đơn vị (cbpd_tw_04); mỗi vai trò chạy trong một phiên đăng nhập tách riêng để chắc chắn không dính phiên cũ. Dữ liệu kiểm thử gồm 3 tổ chức đang hoạt động có sẵn, 1 tổ chức chờ phê duyệt và 1 tổ chức mới đăng ký do đội kiểm thử tự tạo.
