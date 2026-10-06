# QLDMTCTV_OOS_12 — dòng 338 (tab `UAT_TGPL Doanh Nghiệp-tuần 3`)

## Tuần

Tuần 3

## Mã TC

QLDMTCTV_OOS_12

## Mô tả

Danh sách Tổ chức tư vấn — ô tìm kiếm không tìm được theo Người đại diện

## Điều kiện

1. Đăng nhập tài khoản Cán bộ Nghiệp vụ cấp Trung ương (cbnv_tw_04), đơn vị Cục Bổ trợ tư pháp - Bộ Tư pháp.
2. Chọn menu "Mạng lưới Tư vấn viên" -> "Tổ chức tư vấn".

## Dữ liệu đầu vào

Tổ chức TC-STP-AG-0001 "Trung tam Tu van Phap luat QA Dia phuong", Người đại diện là "Nguyen Van QA" (đang hiển thị trên bảng ở cột Người đại diện).

## Các bước thực hiện

1. Ở thẻ "Đang hoạt động", nhập "Trung tam Tu van" vào ô tìm kiếm rồi bấm "Tìm kiếm" — đây là phép đối chứng theo TÊN.
2. Xóa ô tìm kiếm, nhập "TC-STP-AG-0001" rồi bấm "Tìm kiếm" — đối chứng theo MÃ.
3. Xóa ô tìm kiếm, nhập "Nguyen Van QA" rồi bấm "Tìm kiếm" — tìm theo NGƯỜI ĐẠI DIỆN.
4. So ba kết quả.

## Kết quả mong đợi

Màn hình SCR-IV-NEW-01 dòng 1631 quy định ô tìm kiếm có nội dung gợi ý là "Tìm theo mã tổ chức, tên tổ chức hoặc người đại diện", và hành vi là "Tìm theo mã / tên / người đại diện". Vậy nhập đúng tên người đại diện của một tổ chức thì phải tìm ra tổ chức đó, giống như khi tìm theo tên hoặc theo mã.

## Kết quả thực tế

Tìm theo TÊN trả về 2 tổ chức, tìm theo MÃ trả về 1 tổ chức — ô tìm kiếm hoạt động bình thường. Nhưng tìm theo NGƯỜI ĐẠI DIỆN "Nguyen Van QA" trả về 0 kết quả, bảng hiện màn hình rỗng, dù người này đang hiện đúng ở cột "Người đại diện" của tổ chức TC-STP-AG-0001.
Nội dung gợi ý trong ô tìm kiếm cũng chỉ ghi "Tìm theo tên hoặc mã tổ chức", thiếu hẳn phần "người đại diện" so với đặc tả.
Hệ quả: cán bộ không tra được tổ chức khi trong tay chỉ có tên người đại diện.

## Ảnh/vieo 1

QLDMTCTV_OOS_12-tim-theo-nguoi-dai-dien-khong-ra-ket-qua.png

## Trạng thái 1

Fail

## Trạng thái dev fix 1

dev done

## Verify

Pass

## DEV phản hồi lần 1

✅ Bug ĐÚNG - chuyển dev.
- Ô tìm kiếm của danh sách Tổ chức tư vấn không tìm được theo Người đại diện: nhập "Nguyen Van QA" trả về 0 kết quả, trong khi người này đang hiện ở cột "Người đại diện" của tổ chức TC-STP-AG-0001.
- Đã đối chứng ngay trong cùng phiên: tìm theo tên trả 2 kết quả, tìm theo mã trả 1 kết quả. Vậy ô tìm kiếm vẫn chạy, chỉ thiếu tiêu chí người đại diện.
- Đặc tả (dòng 1631) yêu cầu tìm theo cả ba: mã tổ chức, tên tổ chức, người đại diện; nội dung gợi ý trong ô cũng phải là "Tìm theo mã tổ chức, tên tổ chức hoặc người đại diện". Web đang ghi "Tìm theo tên hoặc mã tổ chức".
- Hệ quả: cán bộ không tra được tổ chức khi trong tay chỉ có tên người đại diện.
- Ghi chú tham chiếu: chức năng "Quản lý Tổ chức tư vấn" (FR-IV-NEW-01) trong đặc tả KHÔNG được cấp mã UC (dòng 1029 ghi "chưa có trong CSV"), nên chỉ nêu tên chức năng và số dòng, không có mã UC để dẫn.
- Lỗi do QA phát hiện thêm khi kiểm 4 phiếu QLDMTCTV_02 / _05 / _06 / _09 ngày 03/08/2026, không nằm trong phạm vi 4 phiếu đó nên mở dòng riêng để chuyển dev.
- Môi trường kiểm: bản dựng HTPLDN V1.0.5.
