# Bảng đối chiếu điều kiện — nhóm 21 phiếu Xuất PDF (tab tuần 3, vòng 2)

Case: Kiểm tra chức năng Xuất PDF của Báo cáo thống kê — khung văn bản hành chính TT 17/2025,
quy ước tên tệp, ký số điện tử. Đại diện đo: `SLHDVM_07` (dòng 192, BC Số lượng hỏi đáp/vướng mắc pháp luật).

| Điều kiện có thể đổi kết quả | Bug gốc (vòng 2) | Mình test | GAP? |
|---|---|---|:-:|
| Môi trường | Đối tác và Dev cùng làm việc trên môi trường bàn giao `htpldn-uat.ospgroup.vn` | `https://htpldn-uat.ospgroup.vn` — đúng môi trường bàn giao, không dùng môi trường nội bộ | Không |
| Bản dựng | Phép đo trước của tổ QA là ngày 03/08 trên bản dựng **V1.0.4**; Dev đánh dấu "dev done" sau đó | Đo lại 04/08/2026 trên bản dựng **HTPLDN · V1.0.5** đang chạy — đọc trực tiếp từ thanh bên trái, không lấy từ trí nhớ. Đây là lý do phải đo lại thay vì dùng lại kết quả 03/08 | Không |
| Vai trò / tài khoản | Phiếu do đối tác lập trên vai trò cán bộ nghiệp vụ | `cbnv_tw` — vai trò `CB_NV_TW`, đơn vị Cục Bổ trợ tư pháp - Bộ Tư pháp, cấp TW. Cùng vai trò, có quyền xem và xuất báo cáo | Không |
| Loại báo cáo | 22 phiếu Xuất PDF trải trên nhiều loại báo cáo của nhóm IX, phiếu đại diện là BC Số lượng hỏi đáp/vướng mắc pháp luật | Đo đúng loại "BC Số lượng hỏi đáp/vướng mắc pháp luật" của phiếu `SLHDVM_07`. Ba điểm đang tranh chấp (khung văn bản, tên tệp, ký số) đều do **cùng một bộ sinh tệp** của nhóm IX tạo ra, không phụ thuộc loại báo cáo — nên một phép đo phủ được cả nhóm | Không |
| Tham số kỳ / thời gian / đơn vị | Phiếu không ràng buộc kỳ hay đơn vị cụ thể | Kỳ **Năm**, 01/01/2026–31/12/2026, đơn vị **Toàn quốc** — tham số hợp lệ, báo cáo trả về có số liệu thật (64 hỏi đáp, 2 trang), không rơi vào trường hợp báo cáo rỗng làm mất khối đầu/cuối trang | Không |
| Dữ liệu tiền đề | Vòng 1 đã ghi Pass: tệp tải về được, số liệu khớp màn hình; lỗi "Không thể tạo file xuất" của vòng trước đã hết | Xuất thành công, phản hồi HTTP 200, `content-type: application/pdf`, tệp 28.741 byte mở được bằng trình đọc PDF — đúng tình trạng của vòng 1, không lẫn với lỗi cũ | Không |
| Cách đọc nội dung tệp | Phép đo 03/08 là mở tệp thật đọc bằng mắt | Đọc bằng trình phân tích PDF: khổ giấy 595×842 pt, phông nhúng `Tinos-Regular`/`Tinos-Bold`, toàn bộ chữ trong tệp, và cờ chữ ký số của tệp. Tra từ khóa trên **toàn văn** nên kết luận "không có quốc hiệu / không có khối ký" là đo trên cả 2 trang, không phải nhìn lướt 1 trang | Không |
| Tên tệp lấy từ đâu | Phiếu yêu cầu tên tệp theo khuôn có giờ-phút | Lấy từ phần đầu phản hồi của máy chủ (`content-disposition`), là nguồn quyết định tên tệp khi tải về — không suy từ tên hiển thị trên trình duyệt | Không |

**Kết luận bảng:** 0 GAP — đo đúng môi trường bàn giao, đúng bản dựng đang chạy, đúng vai trò, đúng loại
báo cáo của phiếu đại diện, tham số cho ra báo cáo có số liệu thật, và đọc nội dung tệp bằng phương pháp
đọc được toàn văn. Đủ điều kiện chốt verdict cho cả nhóm.
