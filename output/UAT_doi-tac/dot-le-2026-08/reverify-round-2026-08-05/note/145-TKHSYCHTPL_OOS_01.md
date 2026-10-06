## [UAT_TGPL Doanh Nghiệp-tuần 2] row 145 — TKHSYCHTPL_OOS_01 — S1
Tên chức năng: 
Tác nhân: 
Mô tả: Hồ sơ đã kết thúc vẫn lọt bộ lọc "Mức SLA = Sắp hết hạn", nhưng cột "Cảnh báo thời hạn" của chính các hồ sơ đó lại hiển thị "Đã hoàn thành"
Điều kiện: 1. Đăng nhập tài khoản Cán bộ nghiệp vụ Trung ương (đơn vị Bộ Tư pháp - Trung ương)
2. Có hồ sơ vụ việc đã kết thúc (Hoàn thành hoặc Từ chối) mà mốc thời hạn xử lý đã trôi qua so với ngày kiểm tra
Dữ liệu đầu vào: Vụ việc VV-BTP-TW-20260712-006 (trạng thái Từ chối) và VV-BTP-TW-20260712-005 (trạng thái Hoàn thành); cả 2 tiếp nhận ngày 12/07/2026, thời hạn xử lý 31/07/2026 - đã qua so với ngày kiểm 03/08/2026. Lần cập nhật cuối lần lượt 29/07/2026 và 24/07/2026.
Các bước: 1. Chọn menu "Vụ việc HTPL"
2. Ở thanh lọc, mở ô "Mức SLA" và chọn "Sắp hết hạn" (các ô lọc khác để trống, tab "Tất cả")
3. Bấm [Tìm kiếm]
4. Đọc cột "Cảnh báo thời hạn" của các dòng kết quả (cột nằm sau cột "Thời hạn xử lý", cần đủ bề rộng màn hình mới thấy)
KQ mong đợi: Giữa bộ lọc và cột hiển thị phải nhất quán: hồ sơ do bộ lọc "Sắp hết hạn" trả về thì cột "Cảnh báo thời hạn" phải cho biết đúng mức cảnh báo tương ứng, hoặc hồ sơ đã kết thúc phải được loại khỏi kết quả lọc mức cảnh báo. Cột "Cảnh báo thời hạn" chỉ dùng các mức đã được đặc tả định nghĩa.
KQ thực tế (l1): Lọc "Mức SLA" = "Sắp hết hạn" trả về đúng 2 hồ sơ VV-BTP-TW-20260712-006 và VV-BTP-TW-20260712-005 ("Hiển thị 1-2 / 2 kết quả"), nhưng cột "Cảnh báo thời hạn" của CẢ 2 dòng lại hiển thị "Đã hoàn thành". Nhìn trên màn hình, bộ lọc và cột hiển thị nói hai điều khác nhau, dễ hiểu nhầm là bộ lọc trả về sai bản ghi.

Nguyên nhân quan sát được: mức cảnh báo thời hạn của 2 hồ sơ vẫn giữ nguyên ở mức "Sắp hết hạn" từ lúc hồ sơ được đóng và không đổi nữa, dù mốc thời hạn 31/07/2026 đã trôi qua. Điều này phù hợp với phạm vi công việc tự động đã mô tả trong đặc tả (chỉ rà hồ sơ đang hoạt động), nhưng đặc tả không nói phải xử lý ra sao với giá trị còn sót của hồ sơ đã đóng.

Lưu ý cần phân biệt 2 cột: cột "Trạng thái" hiện "Từ chối" / "Hoàn thành"; cột "Cảnh báo thời hạn" là cột khác, đứng sau "Thời hạn xử lý", và hiện "Đã hoàn thành".

Đo 2 chiều đều khớp: ảnh chụp màn hình ở bề rộng 1920px (lấy trọn cả cột "Mã vụ việc" lẫn cột "Cảnh báo thời hạn" trong một khung hình) và dữ liệu danh sách trả về đều cho cùng kết quả.

(Lỗi do tổ kiểm thử phát hiện thêm khi verify case TKHSYCHTPL_03 ngày 03/08/2026 - phiếu TKHSYCHTPL_03 chỉ nói về việc bộ lọc báo lỗi, không có dòng nào cho phần hiển thị cột "Cảnh báo thời hạn" nên mở dòng mới.)
Trạng thái 1: Fail | P dev fix1: dev done | Q Verify: Open
KQ thực tế lần 2: 
Trạng thái 2:  | W dev fix2:  | X Verify2: 
--- NOTE (R: DEV phản hồi lần 1) ---
✅ Bug đúng (BA 04/08/2026). Dev FE/BE: cột "Cảnh báo thời hạn" ở màn danh sách vụ việc đang hiện nhãn "Đã hoàn thành" — một giá trị không tồn tại trong hệ thống. Cột này chỉ được phép hiện đúng bốn mức đã định nghĩa: Bình thường, Sắp hết hạn, Quá hạn, Quá hạn nghiêm trọng (FR-V.I §cột danh sách, srs-fr-05-vu-viec.md dòng 1656, điều kiện hiển thị "Luôn"; thực thể dòng 2031 cũng chỉ nhận đúng bốn mã này). Với hồ sơ đã đóng thì cột hiển thị đúng mức đang lưu — với hai hồ sơ QA quan sát là "Sắp hết hạn".
BA chốt rõ hai phần CÒN LẠI của phiếu là ĐÚNG, Dev không đụng: (a) giữ nguyên mức cảnh báo của hồ sơ đã đóng là đúng, vì công việc tự động chỉ quét vụ việc đang hoạt động (dòng 1436); (b) bộ lọc trả về hồ sơ đã đóng cũng đúng, vì nó lọc theo giá trị đã lưu. Việc loại hồ sơ đã đóng khỏi bộ lọc là yêu cầu cải tiến, mở phiếu riêng nếu BA muốn. Minor. Không sửa đặc tả.

── CÁCH VERIFY sau Dev fix ──
Precondition: cbnv_tw + màn danh sách vụ việc, có sẵn hai hồ sơ đã đóng VV-BTP-TW-20260712-006 và VV-BTP-TW-20260712-005 (một Từ chối, một Hoàn thành) đang lưu mức cảnh báo "Sắp hết hạn".
1) Đặt bộ lọc "Mức SLA" = "Sắp hết hạn".
2) Đọc cột "Cảnh báo thời hạn" của từng dòng kết quả.
3) Bỏ lọc, duyệt danh sách và đọc cột này ở các hồ sơ đang xử lý lẫn hồ sơ đã đóng.
✅ PASS khi: mọi giá trị xuất hiện ở cột "Cảnh báo thời hạn" đều nằm trong đúng bốn mức đã định nghĩa; hai hồ sơ đã đóng ở bước 1 hiện "Sắp hết hạn" — khớp với chính bộ lọc đã chọn.
❌ FAIL nếu: cột còn hiện "Đã hoàn thành" hay bất kỳ nhãn nào ngoài bốn mức; hoặc cột để trống ở hồ sơ đã đóng.
⚠️ Sau khi sửa, hồ sơ trạng thái Hoàn thành SẼ hiện "Sắp hết hạn" ở cột này. Đó là kết quả ĐÚNG theo đặc tả hiện hành — mức cảnh báo được giữ nguyên tại thời điểm hồ sơ đóng. Đừng chấm FAIL và đừng mở bug mới vì điều đó.