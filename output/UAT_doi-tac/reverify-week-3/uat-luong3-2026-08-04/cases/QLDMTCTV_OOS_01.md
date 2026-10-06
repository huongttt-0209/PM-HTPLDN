# QLDMTCTV_OOS_01 — dòng 327 (tab `UAT_TGPL Doanh Nghiệp-tuần 3`)

## Tuần

Tuần 3

## Mã TC

QLDMTCTV_OOS_01

## Mô tả

Danh sách Tổ chức tư vấn — thẻ "Chờ phê duyệt" không chuyển dấu đỏ khi đang có hồ sơ chờ xử lý

## Điều kiện

1. Đăng nhập tài khoản Cán bộ Phê duyệt cấp Trung ương (cbpd_tw_04), đơn vị Cục Bổ trợ tư pháp - Bộ Tư pháp.
2. Chọn menu "Mạng lưới Tư vấn viên" -> "Tổ chức tư vấn".

## Dữ liệu đầu vào

Tổ chức TC-BTP-TW-0001 đang ở trạng thái "Chờ phê duyệt" (1 hồ sơ).

## Các bước thực hiện

1. Quan sát thanh thẻ trạng thái phía trên bảng.
2. Đọc màu huy hiệu của thẻ "Chờ phê duyệt".
3. So sánh với huy hiệu của thẻ "Mới đăng ký" (cũng đang có hồ sơ).

## Kết quả mong đợi

Màn hình SCR-IV-NEW-01 dòng 1628 quy định thẻ "Chờ phê duyệt" thuộc loại "tab + số đếm + chấm đỏ nếu >0" — đúng y như thẻ "Mới đăng ký" ở dòng 1627. Vậy khi thẻ đang có từ 1 hồ sơ trở lên, hệ thống phải hiện dấu đỏ để Cán bộ Phê duyệt nhận ra có việc cần xử lý.

## Kết quả thực tế

Thẻ "Chờ phê duyệt" đang có 1 hồ sơ nhưng huy hiệu vẫn nền XANH. Cùng lúc đó thẻ "Mới đăng ký" cũng có hồ sơ thì huy hiệu nền ĐỎ. Hai thẻ được đặc tả bằng cùng một mệnh đề nhưng hiển thị khác nhau.
Hệ quả: Cán bộ Phê duyệt mất tín hiệu cảnh báo trên đúng thẻ chứa việc của mình.

## Ảnh/vieo 1

QLDMTCTV_05-cbpd-tw-04-thanh-the-co-cho-phe-duyet.png

## Trạng thái 1

Fail

## Trạng thái dev fix 1

dev done

## Verify

Pass

## DEV phản hồi lần 1

✅ Bug ĐÚNG - chuyển dev.
- Thẻ "Chờ phê duyệt" đang có hồ sơ nhưng không chuyển dấu đỏ, trong khi thẻ "Mới đăng ký" cùng tình huống thì có dấu đỏ.
- Theo màn hình SCR-IV-NEW-01 (dòng 1628), thẻ "Chờ phê duyệt" phải là "tab + số đếm + chấm đỏ nếu >0", giống hệt quy định cho thẻ "Mới đăng ký" (dòng 1627).
- Đây là thẻ chứa việc cần xử lý của Cán bộ Phê duyệt nên thiếu dấu đỏ là mất tín hiệu quan trọng nhất.
- Kiểm bằng tài khoản Cán bộ Phê duyệt Trung ương, đơn vị Cục Bổ trợ tư pháp.
- Ghi chú tham chiếu: chức năng "Quản lý Tổ chức tư vấn" (FR-IV-NEW-01) trong đặc tả KHÔNG được cấp mã UC (dòng 1029 ghi "chưa có trong CSV"), nên chỉ nêu tên chức năng và số dòng, không có mã UC để dẫn.
- Lỗi do QA phát hiện thêm khi kiểm 4 phiếu QLDMTCTV_02 / _05 / _06 / _09 ngày 03/08/2026, không nằm trong phạm vi 4 phiếu đó nên mở dòng riêng để chuyển dev.
- Môi trường kiểm: bản dựng HTPLDN V1.0.5.
