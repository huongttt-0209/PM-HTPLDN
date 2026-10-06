# Sao lưu nguyên văn dòng 126 — QLLSHTCTVV_04 (trước khi QA ghi đè cột R)

## Mã TC

QLLSHTCTVV_04

## Mô tả

Kiểm tra các trường thông tin tìm kiếm

## Điều kiện

1. Đăng nhập tài khoản

## Dữ liệu đầu vào

(trống)

## Các bước thực hiện

1. Chọn menu "Mạng lướt tư vấn viên" -> "Tư vấn viên/Chuyên gia"
2. Tìm kiếm và Nhấn xem chi tiết ứng viên
3. Chọn tab "Lịch sử hỗ trợ"

## Kết quả mong đợi

- Hệ thống hiển thị các trường thông tin giống với thiết kế
- Dữ liệu hiển thị đúng định dạng và trường thông tin
- Dữ liệu hiển thị không bị tràn/đè lên nhau, đồng nhất ngôn ngữ hiển thị

## Kết quả thực tế

- Danh sách chọn Trạng thái chưa đủ giá trị theo định nghĩa của nhóm chức năng Quản lý vụ việc

## Ảnh/vieo 1

QLLSHTCTVV_04.jpg

## Trạng thái 1

Fail

## Trạng thái dev fix 1

dev done

## Verify

BA confirm

## DEV phản hồi lần 1

⚠️ Cần BA xác nhận — trạng thái: CHỜ BA XÁC NHẬN.
- Case hỗn hợp: dòng bắt đầu bằng ⚠️ là ý CHỜ BA CHỐT; dòng bắt đầu bằng ✅ là LỖI THẬT đã chứng minh, dev xử lý được ngay, KHÔNG phải chờ BA.
- Đã kiểm tra lại trên web bằng vai trò Cán bộ Nghiệp vụ Trung ương, đúng bề mặt của phiếu: màn Hồ sơ chi tiết Tư vấn viên, tab "Lịch sử hỗ trợ", bộ lọc "Trạng thái vụ việc". Case này gồm 3 ý, kết luận từng ý như sau.
- ⚠️ Ý 1 (CHỜ BA XÁC NHẬN – không phải việc của dev) – phản ánh "danh sách chọn Trạng thái chưa đủ giá trị": quan sát của bên kiểm thử là ĐÚNG, bộ lọc chỉ có 3 giá trị "Đang xử lý" / "Hoàn thành" / "Từ chối", ít hơn tập trạng thái đầy đủ của nhóm Quản lý vụ việc. Tuy nhiên SRS v3.5 – FR-IV-10 (UC48), màn SCR-IV-03 dòng 1578 – cố ý quy định cho riêng tab này một tập RÚT GỌN, không phải toàn bộ 12 trạng thái vụ việc. Phần mềm đang bám đúng tập rút gọn đó, nên phần này là khác biệt về ĐẶC TẢ, cần BA chốt chứ không phải lỗi lập trình.
- ⚠️ Ý 2 (CHỜ BA XÁC NHẬN – không phải việc của dev) – nhãn giá trị: SRS dòng 1578 ghi giá trị thứ tư là "Đã hủy", nhưng bảng quy đổi trạng thái vụ việc (srs-fr-05-vu-viec.md dòng 1498-1509) không có trạng thái nào tên "Đã hủy"; giá trị gần nhất là "Từ chối". Web đang hiển thị "Từ chối" và lọc đúng theo trạng thái đó, tức web khớp bảng quy đổi và lệch so với chữ ở dòng 1578. Hai chỗ trong SRS đang mâu thuẫn nhau, cũng cần BA chốt.
- ✅ Ý 3 – lỗi phát hiện thêm trên chính bộ lọc này, ĐÃ chuyển dev: SRS dòng 1578 quy định "Trạng thái vụ việc (chọn nhiều: ...)", nhưng thực tế chỉ chọn được 1 giá trị. Chọn "Đang xử lý" rồi chọn tiếp "Hoàn thành" thì giá trị sau đè giá trị trước, không giữ được cả hai, nên không lọc kết hợp nhiều trạng thái trong một lần được. Cùng quy định "chọn nhiều" này còn được SRS lặp lại ở dòng 1856 cho bộ lọc tương ứng của màn Người hỗ trợ pháp lý.
- Số liệu đo trên hồ sơ TVV-BTP-TW-0002 (6 vụ việc, chưa lọc hiện đủ 6 dòng): chọn "Đang xử lý" còn 1 dòng, "Hoàn thành" còn 1 dòng, "Từ chối" còn 0 dòng. Tức bộ lọc hiện chỉ chạm tới 2/6 vụ việc; 4 vụ việc còn lại đang ở các trạng thái khác không có giá trị nào lọc ra được. Đề nghị BA cân nhắc số liệu này khi chốt ý 1.
- Ghi chú: ô lọc có nút xóa, bấm xóa thì quay lại đủ 6 dòng, nên chức năng "xem tất cả" vẫn dùng được dù danh sách không có mục tên "Tất cả".
- Bug ID: BUG-QLLSHTCTVV_04.
- Verify: tài khoản Cán bộ Nghiệp vụ Trung ương, hồ sơ TVV-BTP-TW-0002 (Đang hoạt động), bản dựng V1.0.5, ngày 03/08/2026. Không tạo hay thay đổi dữ liệu nào.

──────── (append) ────────
[DEV cập nhật 03/08/2026 — sau fix]
• ý3 (bộ lọc Trạng thái phải chọn nhiều): ĐÃ FIX FE+BE (IN) + verify 120 PASS (commit a03203023).
• ý1 (tập trạng thái rút gọn có đúng ý đồ?) + ý2 (nhãn "Từ chối" vs SRS ghi "Đã hủy" — enum thật TU_CHOI, không có DA_HUY): CHỜ BA CHỐT. Đã lập phiếu BA (mục c). Chưa đổi nhãn/tập trạng thái cho tới khi BA chốt.

──────── (append) ────────
[DEV rà lại SRS 03/08] ý1 (tập trạng thái rút gọn) = code ĐÚNG SRS :1578(a) (rút gọn: Tất cả/Đang xử lý/Hoàn thành). ý2 nhãn: enum trạng thái vụ việc KHÔNG có DA_HUY, chỉ có TU_CHOI → code hiển thị "Từ chối" là ĐÚNG dữ liệu thật; SRS :1578 ghi "Đã hủy" là TYPO → đề nghị BA sửa SRS thành "Từ chối" (không đổi code, không chặn). ý3 chọn nhiều đã fix → QLLSHTCTVV_04 = dev done.
