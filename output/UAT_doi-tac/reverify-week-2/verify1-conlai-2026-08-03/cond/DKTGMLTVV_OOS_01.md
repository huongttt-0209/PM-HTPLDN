# Bảng đối chiếu điều kiện — DKTGMLTVV_OOS_01 (row 138, tab `UAT_TGPL Doanh Nghiệp-tuần 2`)

**Chức năng:** Đăng ký tham gia mạng lưới TVV — FR-IV-03 (UC41), màn SCR-IV-02 "Thêm mới / Chỉnh sửa Tư vấn viên"
**Nội dung TC:** ô "Số thẻ hành nghề" không bị áp ràng buộc bắt buộc khi Loại = Tư vấn viên — hồ sơ vẫn lưu được dù ô này để trống (SRS `:1507`).
**Loại bug:** ràng buộc **có điều kiện theo giá trị nhập** (chỉ phát sinh khi Loại = Tư vấn viên) và chỉ kết luận được sau khi bấm Lưu → KHÔNG phải bug tĩnh, BẮT BUỘC có bảng này (QA_VERIFY_PROTOCOL §Quy tắc VÀNG).
**Ngày verify:** 2026-08-03 · **Tài khoản QA dùng:** `nht_qa_tw` (NHT, đơn vị Cục Bổ trợ tư pháp - Bộ Tư pháp, cấp TW)

> **Nguồn gốc dòng TC:** lỗi do QA tự phát hiện khi verify DKTGMLTVV_05 (row 123), nằm ngoài tiêu chí của phiếu nên mở dòng mới. **Không có evidence đối tác cho riêng lỗi này** — cột "Đối tác" ghi rõ "Không áp dụng" thay vì suy diễn điều kiện đối tác.

| Điều kiện có thể đổi kết quả | Đối tác | Mình test | GAP? |
|---|---|---|:-:|
| Vai trò / tài khoản | Không áp dụng — lỗi do QA phát hiện, không có báo cáo đối tác | `nht_qa_tw` — "QA NHT Trung uong", vai trò `NHT`, đơn vị `Cục Bổ trợ tư pháp - Bộ Tư pháp`, cấp `BTP · TW`. Đây là vai duy nhất được submit hồ sơ ứng viên TVV theo `SCR-IV-02` §Quyền truy cập (dòng 1476) | Không |
| Màn hình + trạng thái entity | Không áp dụng — lỗi do QA phát hiện, không có báo cáo đối tác | Màn "Thêm mới Tư vấn viên" (`/chuyen-gia-tvv/tao-moi`). TU_VAN_VIEN **chưa tồn tại** khi bắt đầu; sau khi bấm Lưu sinh ra `TVV-BTP-TW-0031` ở trạng thái `MOI_DANG_KY` | Không |
| Giá trị kích hoạt ràng buộc | Không áp dụng — lỗi do QA phát hiện, không có báo cáo đối tác | **Loại = "Tư vấn viên (TVV)"** — đúng điều kiện mà `:1507` quy định ("Bắt buộc nếu Loại = Tư vấn viên"). Đã đọc lại giá trị đang chọn trên biểu mẫu trước khi bấm Lưu, và `loaiTvv = TVV` trong hồ sơ đã tạo | Không |
| Dữ liệu tiền đề (12 trường bắt buộc + tệp) | Không áp dụng — lỗi do QA phát hiện, không có báo cáo đối tác | Đã điền **đủ 12/12** trường bắt buộc (Loại, Họ tên, Ngày sinh, Giới tính, Số CMND/CCCD, Email, Số điện thoại, Địa chỉ, Trình độ học vấn, Chuyên ngành, Số năm kinh nghiệm, Lĩnh vực pháp luật) — đã đo `batBuocConTrong = []` trước khi bấm. **Đã tải lên "File thẻ hành nghề (PDF)"** (tệp PDF hợp lệ 605 B) để cô lập biến số. Chỉ riêng ô "Số thẻ hành nghề" để trống | Không |
| Thao tác / nút bấm | Không áp dụng — lỗi do QA phát hiện, không có báo cáo đối tác | Bấm **[Lưu]** đúng 1 lần | Không |

## Ghi chú đóng GAP

- **Không có ô GAP nào vì không có điều kiện đối tác để lệch:** dòng TC do QA mở, toàn bộ điều kiện do QA tự dựng và đã ghi đủ ở cột "Mình test". Cột "Đối tác" ghi "Không áp dụng" là khẳng định có ý thức, không phải ô bỏ trống.
- **Biến số gây nhiễu đã được cô lập bằng thực nghiệm, không bằng lập luận:** lần bấm Lưu **thứ nhất** (chưa tải File thẻ hành nghề) bị chặn — gửi **0 lệnh**, hiện thông báo *"File thẻ hành nghề là bắt buộc đối với Tư vấn viên"*. Sau khi tải tệp lên, biểu mẫu chỉ còn đúng ô "Số thẻ hành nghề" trống và lần bấm **thứ hai** lưu được. Vậy kết quả "lưu được" quy về đúng một biến là ô "Số thẻ hành nghề", không phải do biểu mẫu thiếu cơ chế kiểm tra.
- **Đo được cả hai chiều của cơ chế chặn:** chặn (0 lệnh, có thông báo cản) và không chặn (3 lệnh: tạo hồ sơ → nạp tệp → cập nhật; 1 thông báo "Tạo hồ sơ TVV thành công"). Bộ đếm lệnh + bộ bắt thông báo đã tự kiểm `soObserverDangSong = 1` trước khi tin số liệu.
- **Kiểm chéo bằng phương pháp khác:** đọc lại hồ sơ vừa tạo qua màn hình chi tiết (ô "Số thẻ hành nghề" hiện `—`) và qua dữ liệu hệ thống trả về (`soTheHanhNghe = null`, `loaiTvv = "TVV"`) — hai nguồn khớp nhau.

**Kết luận: 0 GAP** — mọi điều kiện quan sát lỗi đã được dựng và test thật.
