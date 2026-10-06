# QLDMTCTV_OOS_13 — dòng 339 (tab `UAT_TGPL Doanh Nghiệp-tuần 3`)

## Tuần

Tuần 3

## Mã TC

QLDMTCTV_OOS_13

## Mô tả

Biểu mẫu Thêm mới / Chỉnh sửa Tổ chức tư vấn — thứ tự trường và tên gọi Giấy ĐKHĐ chưa thống nhất với đặc tả

## Điều kiện

1. Đăng nhập tài khoản Cán bộ Nghiệp vụ cấp Trung ương (cbnv_tw_04), đơn vị Cục Bổ trợ tư pháp - Bộ Tư pháp.
2. Chọn menu "Mạng lưới Tư vấn viên" -> "Tổ chức tư vấn".

## Dữ liệu đầu vào

Không cần dữ liệu — chỉ đọc thứ tự và nhãn trường trên biểu mẫu.

## Các bước thực hiện

1. Bấm nút "Thêm mới" để mở biểu mẫu Thêm mới Tổ chức tư vấn.
2. Ghi lại thứ tự 15 trường theo đúng trình tự hiển thị.
3. So với bảng thành phần màn hình SCR-IV-NEW-02 (dòng 1676 đến 1695).
4. Đối chiếu tên gọi và tính bắt buộc của trường "Số Giấy ĐKHĐ Sở TP" với các dòng 1052, 1053, 1073, 1681, 1682, 2216 và 2217 của đặc tả.

## Kết quả mong đợi

Đặc tả SCR-IV-NEW-02 xếp "Lĩnh vực pháp luật" và "Số lao động" cùng nhóm 2 (dòng 1684 đến 1685), đứng TRƯỚC nhóm Liên hệ gồm Địa chỉ, Số điện thoại, Email, Website (dòng 1686 đến 1690). Tên gọi và tính bắt buộc của Giấy đăng ký hoạt động cũng phải thống nhất giữa các phần của đặc tả.

## Kết quả thực tế

Thứ tự trên web là: Tên tổ chức, Loại hình, Người đại diện, Chức vụ đại diện, Số Giấy ĐKHĐ Sở TP, Ngày cấp, Số lao động, Địa chỉ, Điện thoại, Email, Website, Lĩnh vực pháp lý, Số quyết định công bố, Ngày quyết định công bố, Ghi chú.
Tức "Số lao động" bị tách khỏi nhóm 2 và chen vào trước "Địa chỉ"; "Lĩnh vực pháp lý" bị đẩy xuống sau "Website".
Về Giấy ĐKHĐ: web ghi nhãn "Số Giấy ĐKHĐ Sở TP" và đặt là bắt buộc. Đối chiếu thì chính đặc tả đang gọi giấy này bằng ba cách khác nhau và ghi tính bắt buộc khác nhau ở các phần khác nhau (nêu rõ ở phần trao đổi).

## Ảnh/vieo 1

QLDMTCTV_OOS_10-nhan-truong-bieu-mau-them-moi.png

## Trạng thái 1

Fail

## Trạng thái dev fix 1

BA confirm

## Verify

BA confirm

## DEV phản hồi lần 1

⚠️ Cần BA xác nhận.
- Đặc tả đang gọi cùng một giấy tờ bằng ba cách khác nhau và ghi tính bắt buộc trái ngược nhau.
- Về tên gọi: dòng 1681 và 1682 gọi là "Số Giấy đăng ký hành nghề" / "Ngày cấp Giấy đăng ký hành nghề"; dòng 1073 gọi là "Giấy đăng ký hoạt động Sở TP"; dòng 2216 và 2217 gọi là "Giấy ĐKHĐ Sở TP", nhãn ghi "Số giấy ĐKHĐ" / "Ngày cấp giấy ĐKHĐ". Lưu ý "đăng ký hoạt động" và "đăng ký hành nghề" là hai loại giấy tờ khác nhau nên không thể coi là cùng một tên rút gọn.
- Về tính bắt buộc: dòng 1052 và 1053 ghi Bắt buộc = "N" (không bắt buộc), nhưng dòng 1073, 1681, 1682, 2216 và 2217 đều ghi bắt buộc.
- Thực tế phần mềm: biểu mẫu Thêm mới đang dùng nhãn "Số Giấy ĐKHĐ Sở TP" và đặt hai trường này là bắt buộc, tức theo dòng 1073 và 2216.
⚠️ Câu hỏi gửi BA: đề nghị chốt một tên gọi chuẩn và một mức bắt buộc duy nhất, rồi sửa đặc tả cho khớp ở cả bốn chỗ nói trên. Nếu chốt là bắt buộc, cần chốt thêm cách xử lý hồ sơ cũ đang thiếu hai thông tin này: cho lưu tiếp và chỉ bắt buộc với hồ sơ tạo mới, hay bắt bổ sung đủ mới lưu được.
- Đây là ý duy nhất trong nhóm này có thể chặn người dùng lưu hồ sơ, đề nghị ưu tiên trả lời trước.
- Rút lại một ý so với lượt trước: ý "thứ tự trường trên biểu mẫu" đã được rà lại và rút, vì bảng thành phần màn hình là bảng liệt kê thành phần chứ không phải bản vẽ bố cục, không đủ căn cứ coi thứ tự là ràng buộc bắt buộc.
- Ghi chú tham chiếu: chức năng "Quản lý Tổ chức tư vấn" (FR-IV-NEW-01) trong đặc tả không được cấp mã UC (dòng 1029 ghi "chưa có trong CSV"), nên chỉ nêu tên chức năng và số dòng.
- Đã đưa vào file gửi BA: ba-confirmation-needed-luong4-to-chuc-tu-van-2026-08-03.md, mục 1.
- Kiểm bằng vai trò Cán bộ Nghiệp vụ Trung ương (cbnv_tw_04), bản dựng HTPLDN V1.0.5.
