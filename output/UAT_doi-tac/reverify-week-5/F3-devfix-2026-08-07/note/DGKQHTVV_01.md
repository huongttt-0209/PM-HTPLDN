🔁 CÒN LỖI Ở ĐÂU: Doanh nghiệp vẫn không vào được màn chi tiết vụ việc của chính mình để đánh giá — bấm mã vụ việc ngay trong danh sách của mình thì bị đẩy sang trang báo không có quyền truy cập; ngoài danh sách cũng không có chỗ nào để bắt đầu đánh giá.

VÌ SAO LÀ LỖI: srs-fr-05-vu-viec.md:1793 chỉ cho phép chặn khi doanh nghiệp mở vụ việc KHÔNG phải của mình — đây là vụ việc của chính họ. :1809 và :1811 yêu cầu doanh nghiệp nhập được đánh giá ngay trên màn chi tiết khi vụ việc ở "Hoàn thành" / "Đã đánh giá". Màn hình vẫn đòi 2 phần dữ liệu nội bộ (phân công, kết quả kiểm tra) rồi chặn cả trang, trong khi :1805 và :1806 yêu cầu ẩn 2 phần đó với doanh nghiệp.

ĐÃ HẾT LỖI: hệ thống đã cho phép doanh nghiệp đánh giá và phần kết quả xử lý đã đọc được; chặn đánh giá trùng và chặn xem vụ việc của doanh nghiệp khác vẫn đúng.

ĐÃ ĐO: 2 doanh nghiệp, 10 vụ việc, 2 cách mở (bấm trong danh sách và mở thẳng địa chỉ) — hỏng cả 3/3 lần thử.

── CÁCH VERIFY sau Dev fix ──
Precondition: tài khoản doanh nghiệp (tên đăng nhập là mã số thuế) + màn danh sách vụ việc và màn chi tiết vụ việc của chính doanh nghiệp đó.
  Cần >= 2 vụ việc DO CHÍNH doanh nghiệp đó gửi, đang ở "Hoàn thành" và chưa có đánh giá của loại doanh nghiệp, trên >= 2 doanh nghiệp khác nhau.
  Chưa có thì tạo mới bằng luồng chuẩn: doanh nghiệp gửi hồ sơ -> cán bộ nghiệp vụ cùng địa bàn tiếp nhận -> kiểm tra hồ sơ kết luận Đạt -> phân công người xử lý -> cập nhật kết quả -> trình phê duyệt -> cán bộ phê duyệt duyệt -> cập nhật kết quả cuối -> "Hoàn thành".
1) Đăng nhập bằng CHÍNH TÀI KHOẢN DOANH NGHIỆP (không dùng tài khoản cán bộ, không dùng tài khoản quản trị). Mở danh sách vụ việc, bấm mã vụ việc "Hoàn thành" của chính mình để mở chi tiết. Phải xem được nội dung hồ sơ, không bị đẩy sang trang báo không có quyền.
2) Đếm số phần tử tương tác dẫn tới việc đánh giá (nhìn thấy bằng mắt trong khung nhìn, không moi bằng công cụ nhà phát triển). Kích hoạt nó, nhập 9 · 8 · 10 và một chuỗi nhận xét mốc giờ duy nhất dạng QA-DGKQ-<YYYYMMDD-HHMM>, rồi gửi. Cài bộ bắt thông báo TRƯỚC khi bấm, đếm theo mốc giờ khác nhau và đếm số lời gọi song song.
3) Tải lại trang bằng địa chỉ (không dùng lại màn cũ), mở lại phần Đánh giá và đọc nội dung.
4) Đo bằng đường thứ hai: bằng chính phiên đăng nhập của doanh nghiệp, đọc lại bản ghi đánh giá của vụ việc đó từ máy chủ và đối chiếu từng trường với những gì màn hình hiển thị ở bước 3.
5) Lặp bước 1-4 trên vụ việc thứ hai của cùng doanh nghiệp, và trên 1 doanh nghiệp KHÁC với vụ việc của chính doanh nghiệp đó.
6) Kiểm phạm vi (chứng âm): cùng tài khoản doanh nghiệp đó, thử mở và thử đánh giá một vụ việc CỦA DOANH NGHIỆP KHÁC -> phải bị từ chối.
7) Kiểm trùng: doanh nghiệp đánh giá lần thứ hai cùng vụ việc -> phải bị từ chối, đọc lại vẫn đúng 1 bộ điểm của loại doanh nghiệp, nhận xét cũ không bị ghi đè.
✅ PASS khi: doanh nghiệp mở được chi tiết vụ việc của chính mình; đếm được >= 1 phần tử dẫn tới việc đánh giá; gửi xong thì SAU KHI TẢI LẠI TRANG đọc được đúng 3 điểm đã nhập + đúng chuỗi nhận xét + điểm tổng bằng trung bình 3 điểm; đường đo thứ hai trùng khít và ghi loại người đánh giá là doanh nghiệp; đúng trên >= 2 vụ việc và >= 2 doanh nghiệp; chứng âm bước 6 và kiểm trùng bước 7 đều bị từ chối.
❌ FAIL nếu: doanh nghiệp vẫn không mở được chi tiết vụ việc của chính mình; hoặc mở được nhưng không có phần tử nào để bắt đầu đánh giá; hoặc gửi được và báo thành công nhưng sau khi tải lại trang phần đánh giá vẫn rỗng / thiếu >= 1 trong 3 điểm / nhận xét khác chuỗi đã nhập / điểm tổng khác trung bình 3 điểm; hoặc hai đường đo lệch nhau (fix một phần vẫn là FAIL); hoặc doanh nghiệp đánh giá được vụ việc của doanh nghiệp khác.
⚠️ Đừng chấm FAIL vì: nhãn / vị trí / kiểu hiển thị của đường vào đánh giá (nút trên thanh hành động hay điều khiển ngay trong phần đánh giá; hộp thoại hay mở tại chỗ); nguyên văn chữ thông báo thành công; cách làm tròn / định dạng điểm tổng (9 vs 9.0 vs 9,0); không có chức năng sửa/xoá đánh giá đã gửi; thứ tự - màu - bố cục trình bày lại 3 điểm; không ai nhận được thông báo sau khi đánh giá. Doanh nghiệp KHÔNG được thấy phần phân công xử lý và phần kết quả kiểm tra — thiếu 2 phần này là ĐÚNG đặc tả, không phải lỗi.
⚠️ Đừng chấm PASS vì: thấy nhãn trạng thái đã đổi sang "Đã đánh giá", thấy nhật ký đã có mục đánh giá, hay thấy thông báo báo thành công — cả ba dấu hiệu này ĐÃ từng đúng trong khi lỗi còn nguyên. Cũng đừng chấm PASS vì hệ thống đã nhận được lệnh đánh giá gửi thẳng, vì bản ghi đánh giá có sẵn từ bản dựng cũ, hay vì nhánh cán bộ nghiệp vụ chạy được — phải đo lại ĐÚNG nhánh doanh nghiệp, đi từ bước 1.
