# DGKQHTVV_04 — row 68 (tab `bug`)

## [2] Tuần

Tuần 3

## [3] Mã TC

DGKQHTVV_04

## [6] Mô tả

Tự động tính điểm tổng bằng trung bình cộng 3 điểm

## [7] Điều kiện

1. Đăng nhập tài khoản
2. Hồ sơ vụ việc ở trạng thái "Hoàn thành" hoặc "Đã đánh giá".

## [9] Các bước thực hiện

1. Chọn menu "Vụ việc HTPL"
2. Tìm kiếm và nhấn Xem chi tiết
3. Mở Nhóm 8 – Đánh giá
4. Bấm nút "Đánh giá" và nhấn "Lưu đánh giá"

## [10] Kết quả mong đợi

Tự động tính điểm tổng bằng trung bình cộng 3 điểm

## [13] Trạng thái

Fail

## [14] Dopai

Open

## [15] Loại vấn đề

đối tác xóa và đánh lệch ID, chuyển lại ID 4 và 5 cho map với đối tác

## [17] Trạng thái dev fix

Test done

## [19] Kết quả verify

✅ ĐÃ HẾT LỖI — điểm tổng được tính đúng bằng trung bình cộng 3 điểm và do hệ thống tự sinh.

ĐÃ ĐO
Env nội bộ 18.143.165.120.nip.io, bó mã index-DsMHK7Dp.js, tài khoản cbnv_tw_04 (Cán bộ Nghiệp vụ Trung ương), vụ việc VV-QAW7-DG01 đang "Hoàn thành" và chưa từng có đánh giá của cán bộ, cùng đơn vị tài khoản đo. Đo lúc 07/08/2026 02:17-02:22 bằng thao tác thật trên giao diện.

ĐÃ HẾT LỖI
1) Cửa sổ "Đánh giá chất lượng" chỉ có 3 ô điểm bắt buộc (Điểm chất lượng, Điểm thời gian, Điểm thái độ) và ô Nhận xét. KHÔNG có ô nào để người dùng tự nhập điểm tổng, đúng yêu cầu "tự động tính" (srs-fr-05-vu-viec.md:1208, :1734, :2120).
2) Nhập 4 - 8 - 9 rồi xác nhận, tải lại trang: điểm tổng hiện 7/10. Đọc lại bản ghi từ máy chủ cũng được điểm tổng 7 cùng ba điểm thành phần 4 - 8 - 9 và đúng chuỗi nhận xét đã nhập. Hai đường đo khớp nhau.
3) Bộ điểm 4 - 8 - 9 được chọn để loại trừ mọi cách tính sai: trung bình cộng ra 7, còn trung vị ra 8, nhỏ nhất ra 4, lớn nhất ra 9, tổng ra 21, trung bình hai điểm đầu ra 6. Chỉ công thức trung bình cộng ba điểm mới cho ra đúng số đo được. Lượt gửi chỉ chạy đúng một lần, không nhân đôi.

PHẠM VI CHẤM
Phiếu chỉ yêu cầu "tự động tính điểm tổng bằng trung bình cộng 3 điểm", không nhắc tới làm tròn hay số chữ số thập phân, nên phần đó không đưa vào tiêu chí chấm của dòng này. Ghi nhận để đặc tả bổ sung sau: đặc tả hiện im lặng về quy tắc làm tròn cho đánh giá vụ việc (:2462 chỉ áp cho thang tư vấn viên 1-5 và loại trừ rõ trường hợp này), và lượt đo dùng bộ điểm chia hết cho 3 nên chưa lộ quy tắc làm tròn. Muốn chốt quy tắc thì cần một phép đo riêng bằng bộ điểm không chia hết cho 3.
Nhãn nút trong cửa sổ là "Xác nhận" chứ không phải "Lưu đánh giá" như phiếu ghi - không tính là lỗi vì đặc tả không quy định nhãn nút này.

DỮ LIỆU ĐÃ THAY ĐỔI TRÊN MÔI TRƯỜNG
Đã tạo một bản ghi đánh giá của cán bộ trên vụ việc VV-QAW7-DG01 (4 - 8 - 9, nhận xét QA-DGKQ-20260807-0220), khiến vụ việc chuyển từ "Hoàn thành" sang "Đã đánh giá". Bản ghi này không dùng lại được cho lượt đo sau vì hệ thống chặn đánh giá lần hai cùng loại người; nếu cần đo lại thì dùng VV-QAW7-TRALOI-UBND, VV-QAW7-TV-MANGLUOI hoặc VV-QA-001 đến VV-QA-007. Không đụng dữ liệu của đối tác.

BẰNG CHỨNG
Cửa sổ đánh giá khi chưa nhập, không có ô điểm tổng: https://drive.google.com/file/d/1X_BEnrpmrcg86cx9-EJCvdK47ELryHFl/view?usp=drivesdk
Sau khi tải lại trang, điểm tổng hiện 7/10: https://drive.google.com/file/d/1INRY9n_US_ET8W6F-mrZPUOSaAAk409p/view?usp=drivesdk

GIỚI HẠN
Kết luận chỉ có hiệu lực cho env nội bộ và bó mã index-DsMHK7Dp.js đã đo; đối tác đo trên môi trường nghiệm thu khác. Không có ảnh lỗi cũ do chính bên kiểm thử chụp, nên đây là kết luận về hiện trạng đúng so với đặc tả, không phải kết luận về việc bản sửa có tác dụng hay không.

GHI NHẬN THÊM (không thuộc dòng này)
Trên cùng màn, ô giá trị ở cột đầu tiên của bảng nhóm Đánh giá bị bẻ dòng: "4/1" xuống dòng "0" và "7/1" xuống dòng "0". Hiện tượng này thuộc dòng 65 và đã được ghi ở ô Kết quả verify của dòng đó.
