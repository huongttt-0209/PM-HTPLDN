# QLDMTCTV_OOS_10 — dòng 336 (tab `UAT_TGPL Doanh Nghiệp-tuần 3`)

## Tuần

Tuần 3

## Mã TC

QLDMTCTV_OOS_10

## Mô tả

Biểu mẫu Thêm mới / Chỉnh sửa Tổ chức tư vấn — 5 nhãn trường hiển thị khác nhãn trong đặc tả

## Điều kiện

1. Đăng nhập tài khoản Cán bộ Nghiệp vụ cấp Trung ương (cbnv_tw_04), đơn vị Cục Bổ trợ tư pháp - Bộ Tư pháp.
2. Chọn menu "Mạng lưới Tư vấn viên" -> "Tổ chức tư vấn".

## Dữ liệu đầu vào

Không cần dữ liệu — chỉ đọc nhãn hiển thị trên biểu mẫu.

## Các bước thực hiện

1. Bấm nút "Thêm mới" để mở biểu mẫu Thêm mới Tổ chức tư vấn.
2. Đọc lần lượt nhãn của từng trường trên biểu mẫu.
3. So từng nhãn với bảng thành phần màn hình SCR-IV-NEW-02 (dòng 1676 đến 1695).
4. Mở tiếp một tổ chức bất kỳ ở chế độ Chỉnh sửa để đối chiếu — hai chế độ dùng chung biểu mẫu.

## Kết quả mong đợi

Màn hình SCR-IV-NEW-02 quy định nhãn của các trường như sau: "Chức vụ người đại diện" (dòng 1679), "Ngày cấp Giấy đăng ký hành nghề" (dòng 1682), "Lĩnh vực pháp luật" (dòng 1685), "Địa chỉ trụ sở" (dòng 1687), "Số điện thoại" (dòng 1688). Biểu mẫu phải hiển thị đúng các nhãn này.

## Kết quả thực tế

Năm nhãn hiển thị khác đặc tả:
- "Chức vụ đại diện" (đặc tả: "Chức vụ người đại diện")
- "Ngày cấp" (đặc tả: "Ngày cấp Giấy đăng ký hành nghề")
- "Lĩnh vực pháp lý" (đặc tả: "Lĩnh vực pháp luật")
- "Địa chỉ" (đặc tả: "Địa chỉ trụ sở")
- "Điện thoại" (đặc tả: "Số điện thoại")
Giống nhau ở cả chế độ Thêm mới và Chỉnh sửa. Nghĩa của trường không đổi, vẫn nhập liệu bình thường — mức ảnh hưởng nhẹ.

## Ảnh/vieo 1

QLDMTCTV_OOS_10-nhan-truong-bieu-mau-them-moi.png

## Trạng thái 1

Fail

## Trạng thái dev fix 1

dev done

## Verify

Pass

## DEV phản hồi lần 1

✅ Bug ĐÚNG - chuyển dev. Mức nhẹ.
- Năm nhãn trên biểu mẫu khác nhãn trong đặc tả: "Chức vụ đại diện" (đặc tả dòng 1679 ghi "Chức vụ người đại diện"), "Ngày cấp" (dòng 1682 ghi "Ngày cấp Giấy đăng ký hành nghề"), "Lĩnh vực pháp lý" (dòng 1685 ghi "Lĩnh vực pháp luật"), "Địa chỉ" (dòng 1687 ghi "Địa chỉ trụ sở"), "Điện thoại" (dòng 1688 ghi "Số điện thoại").
- Nghĩa của trường không đổi và vẫn nhập liệu bình thường, nên đây là lỗi nhẹ về câu chữ.
- Đã tách riêng: phần thứ tự trường và phần tên gọi Giấy ĐKHĐ chuyển sang dòng QLDMTCTV_OOS_13 vì hai phần đó cần BA chốt trước, không phải việc dev sửa ngay.
- Ghi chú: nhãn "Số Giấy ĐKHĐ Sở TP" trên web KHÔNG tính là lỗi ở dòng này — đặc tả dòng 1073 và dòng 2216 cũng gọi giấy này là "Giấy ĐKHĐ Sở TP", tức web theo đúng hai chỗ đó. Xem dòng QLDMTCTV_OOS_13.
- Ghi chú tham chiếu: chức năng "Quản lý Tổ chức tư vấn" (FR-IV-NEW-01) trong đặc tả KHÔNG được cấp mã UC (dòng 1029 ghi "chưa có trong CSV"), nên chỉ nêu tên chức năng và số dòng, không có mã UC để dẫn.
- Lỗi do QA phát hiện thêm khi kiểm 4 phiếu QLDMTCTV_02 / _05 / _06 / _09 ngày 03/08/2026, không nằm trong phạm vi 4 phiếu đó nên mở dòng riêng để chuyển dev.
- Môi trường kiểm: bản dựng HTPLDN V1.0.5.
