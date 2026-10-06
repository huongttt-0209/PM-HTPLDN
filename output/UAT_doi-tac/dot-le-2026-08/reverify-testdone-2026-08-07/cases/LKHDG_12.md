# LKHDG_12 — row 126 (tab `bug`)

## [1] STT

11/07/2026

## [2] Tuần

Tuần 3

## [3] Mã TC

LKHDG_12

## [6] Mô tả

Xuất Excel

## [7] Điều kiện

1. Đăng nhập tài khoản 
2. Tồn tại tiêu chí tìm kiếm

## [9] Các bước thực hiện

1. Chọn menu "Đánh giá hiệu quả"
2. Nhập tiêu chí có kết quả
3. Bấm nút Xuất Excel

## [10] Kết quả mong đợi

Hệ thống xuất danh sách đợt đánh giá hiện tại (sau khi áp dụng bộ lọc và phân quyền) ra tệp định dạng XLSX để người dùng tải xuống.

## [11] Kết quả thực tế

- Hệ thống xuất danh sách không đúng với tiêu chí lọc
- File excel xuất ra thiếu cột thông tin "Số vụ việc", "Người tạo", "Ngày tạo"
- Thông tin các cột: Tần suất, Đối tượng, Trạng thái hiển thị không dấu

## [12] Ảnh/vieo 1

LKHDG_12.webm

## [13] Trạng thái

Fail

## [14] Dopai

dev done

## [16] TKM phản hồi lần 1

TKM retest 30/7: Hệ thống xuất danh sách không đúng với tiêu chí lọc

## [17] Trạng thái dev fix

Test done

## [19] Kết quả verify

✅ ĐÃ HẾT LỖI — Xuất Excel nay đúng theo bộ lọc đang bật.

Đã kiểm lại ngày 07/08/2026 trên danh sách Đợt đánh giá (Đánh giá hiệu quả → Kế hoạch đánh giá → Danh sách), tài khoản Cán bộ nghiệp vụ Trung ương.

Yêu cầu nghiệp vụ được kiểm: tệp Excel tải về phải chứa đúng những đợt đang hiển thị sau khi lọc — không thừa, không thiếu.

Đã đo trên 20 đợt, với 2 bộ lọc ở 2 cột khác nhau:
• Lọc Tần suất = "Tròn năm": màn hình còn 19 đợt → tệp tải về có đúng 19 dòng, đối chiếu từng mã đợt thì trùng khít 19/19.
• Lọc Trạng thái = "Hoàn thành": màn hình còn 4 đợt → tệp tải về có đúng 4 dòng, trùng khít 4/4 mã.
Hai lần xuất cho ra hai tệp có dung lượng khác nhau, không còn hiện tượng tệp giống hệt nhau bất kể lọc gì như lần trước.

Đã kiểm chứng thêm bằng một đường độc lập (đối chiếu trực tiếp với dữ liệu hệ thống trả về): lọc lấy 4 / 19 / 20 đợt thì tệp xuất tương ứng cũng thay đổi theo cả 3 trường hợp. Trước đây cả 3 trường hợp đều cho tệp y hệt nhau.

Hai điểm còn lại đối tác từng nêu vẫn tốt, không tái phát: tệp có đủ các cột Số vụ việc, Người tạo, Ngày tạo; các cột Tần suất / Đối tượng / Trạng thái ghi bằng tiếng Việt có dấu.

Ghi nhận thêm (không thuộc phạm vi phiếu này, không ảnh hưởng kết luận): danh sách chọn "Trạng thái" trên màn lọc đang dùng một số tên gọi khác với bộ trạng thái mô tả trong đặc tả, và thiếu mục "Hủy" trong danh sách chọn dù bảng vẫn hiển thị đợt đã hủy. Sẽ theo dõi riêng.

Phạm vi hiệu lực: đo trên môi trường nội bộ, khoảng 02:05-02:20 ngày 07/08/2026, trên bản dựng đang chạy tại thời điểm đó (màn hình hiển thị V1.0.9, khác bản đã đo ngày 06/08). Lưu ý: môi trường nội bộ này được cập nhật nhiều lần trong cùng một ngày — riêng đêm 06 rạng 07/08 đã thay 4 lần, lần gần nhất lúc 02:23 tức ngay sau lượt đo này. Vì vậy kết luận "đã hết lỗi" gắn với bản dựng nêu trên; khi chuyển sang môi trường nghiệm thu của đối tác cần xác nhận lại trên bản dựng thực tế ở đó.

## [25] 

phân loại R1-FIX-THIEU.

Phiếu gốc có 3 vế:
1. File Excel thiếu 3 cột "Số vụ việc", "Người tạo", "Ngày tạo" → ✅ đã fix vòng 1
2. Cột Tần suất/Đối tượng/Trạng thái ghi mã enum thô (TRON_NAM, LAP_KE_HOACH) thay vì nhãn tiếng Việt → ✅ đã fix vòng 1
3. "Hệ thống xuất danh sách không đúng với tiêu chí lọc" → ❌ chưa fix

Vòng 1 (commit 6b5e15e9d, 21/07) tự ghi trong DEV phản hồi: "chưa tái hiện được lỗi lọc (phiên đăng nhập hết hạn khi thử áp bộ lọc). Hai lỗi trên đã đủ căn cứ." — tức là biết còn một vế chưa test nhưng vẫn đóng phiếu thay vì đánh dấu BLOCKED/NOT RUN và giữ mở. TKM retest 30/07 gặp đúng vế đó → Reopen.

Root cause kỹ thuật của vế còn lại (lệch cách truyền tham số giữa FE và BE):

- FE ke-hoach-danh-gia.api.ts:91 gửi bộ lọc qua query string, body để rỗng:
