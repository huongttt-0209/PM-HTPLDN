## [UAT_TGPL Doanh Nghiệp-tuần 3] row 331 — QLDMTCTV_OOS_05 — S1
Tên chức năng: 
Tác nhân: 
Mô tả: Danh sách Tổ chức tư vấn — bảng có thêm cột "Đơn vị quản lý" không nằm trong danh sách cột của đặc tả
Điều kiện: 1. Đăng nhập tài khoản Cán bộ Nghiệp vụ cấp Trung ương (cbnv_tw_04), đơn vị Cục Bổ trợ tư pháp - Bộ Tư pháp.
2. Chọn menu "Mạng lưới Tư vấn viên" -> "Tổ chức tư vấn".
Dữ liệu đầu vào: 3 tổ chức ở thẻ "Đang hoạt động".
Các bước: 1. Đọc lần lượt toàn bộ tiêu đề cột của bảng, từ trái sang phải.
2. Đối chiếu với danh sách cột trong đặc tả màn hình.
KQ mong đợi: Màn hình SCR-IV-NEW-01 liệt kê đúng 10 cột cho bảng danh sách, từ dòng 1637 đến dòng 1646: Ô chọn, Số thứ tự, Mã tổ chức, Tên tổ chức, Loại hình, Người đại diện, Lĩnh vực, Trạng thái, Công khai, Hành động. "Đơn vị quản lý" chỉ được nêu ở dòng 1634 với vai trò là một bộ lọc, không phải cột của bảng.
KQ thực tế (l1): Bảng đang có 11 cột: thêm cột "Đơn vị quản lý" đặt giữa "Lĩnh vực" và "Người đại diện".
Không thiếu thông tin, nhưng lệch danh sách cột đã duyệt và làm bảng rộng thêm, phải cuộn ngang mới thấy được 3 cột cuối (Trạng thái, Công khai, Hành động).
Trạng thái 1: Fail | P dev fix1: dev done | Q Verify: Open
KQ thực tế lần 2: 
Trạng thái 2:  | W dev fix2:  | X Verify2: 
--- NOTE (R: DEV phản hồi lần 1) ---
✅ Bug đúng (BA 04/08/2026). Dev FE: bảng danh sách Tổ chức tư vấn đang có 11 cột, thừa cột "Đơn vị quản lý" đặt giữa "Lĩnh vực" và "Người đại diện" — gỡ để bảng về đúng 10 cột theo thiết kế: Ô chọn, Số thứ tự, Mã tổ chức, Tên tổ chức, Loại hình, Người đại diện, Lĩnh vực, Trạng thái, Công khai, Hành động (SCR-IV-NEW-01, srs-fr-04-chuyen-gia-tvv.md dòng 1637-1646). "Đơn vị quản lý" chỉ được nêu ở dòng 1634 với vai trò BỘ LỌC, không phải cột của bảng — nhu cầu xem đơn vị quản lý đã có bộ lọc đó phục vụ. Hệ quả đang thấy: cột thừa đẩy ba cột cuối ra ngoài khung nhìn, trong đó có "Hành động" là chỗ thao tác nhiều nhất. QA đã kiểm lại ngày 04/08/2026 trên bản dựng V1.0.5: cột này VẪN CÒN. Minor.

── CÁCH VERIFY sau Dev fix ──
Precondition: cbnv_tw + màn Mạng lưới Tư vấn viên → Tổ chức tư vấn, thẻ "Đang hoạt động" có ≥1 bản ghi + đặt cửa sổ trình duyệt ở bề ngang 1440px.
1) Đọc lần lượt tiêu đề tất cả các cột của bảng danh sách, từ trái sang phải.
2) Không cuộn ngang, kiểm xem ba cột Trạng thái, Công khai, Hành động có nằm trong khung nhìn không.
3) Mở bộ lọc phía trên bảng, kiểm bộ lọc theo đơn vị quản lý còn dùng được không.
✅ PASS khi: bảng có đúng 10 cột theo danh sách trên, không còn cột "Đơn vị quản lý"; ở bề ngang 1440px nhìn thấy được cả ba cột cuối mà không phải cuộn ngang; bộ lọc theo đơn vị quản lý vẫn còn và vẫn lọc đúng.
❌ FAIL nếu: cột "Đơn vị quản lý" vẫn còn trong bảng; hoặc gỡ cột nhưng đồng thời gỡ mất bộ lọc theo đơn vị quản lý.