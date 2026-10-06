# Bảng đối chiếu điều kiện — QLDMLHHT_11

Loại bug: **Đóng form Thêm/Sửa danh mục đang nhập/sửa dở KHÔNG hiện hộp thoại xác nhận "Bạn có muốn bỏ các thay đổi chưa lưu?".** Phụ thuộc **state form dirty** → cần bảng. (Cùng bản chất cụm B4 với QLDMLVPL_14 — cùng component drawer, khác tab Loại hình hỗ trợ.)

| Điều kiện có thể đổi kết quả | Đối tác (video full-res) | Mình test | GAP? |
|---|---|---|:-:|
| Vai trò / tài khoản | QTHT (màn Danh mục chỉ QTHT truy cập) | QTHT (`admin`) | Không |
| Entity + **trạng thái form** | Form "Thêm mới danh mục" tab Loại hình hỗ trợ ở state dirty (Mã/Tên="a") | Form Thêm mới tab Loại hình hỗ trợ nhập Mã/Tên/Mô tả="a" (dirty) | Không |
| Dữ liệu tiền đề | Tab có ≥1 record | Tab Loại hình hỗ trợ có 6 record | Không |
| Thao tác đóng | Đóng drawer khi dirty | Bấm nút Đóng (X) khi dirty | Không |

**Kết luận: tái hiện ĐÚNG như đối tác (0 GAP).** Bấm Đóng (X) khi form dirty → drawer đóng thẳng về danh sách (1-6/6 mục), KHÔNG dialog "bỏ thay đổi chưa lưu", 0 toast, 0 request (toast-capture.js, observer tự kiểm=1), record nhập dở bị hủy im lặng.

Đối chiếu SRS v3.5: SCR-VIII-01 dùng chung cho FR-VIII-02 (UC100). §Quy tắc tương tác (dòng 1606–1608) + TPL-DM-CRUD (65–171) không có clause dialog dirty-state (dialog này CÓ ở fr-02:1070, fr-04:1512/1562/1685/1808 nhưng silent cho màn danh mục). → **BA confirm**.

Bằng chứng: `reverify-audit/QLDMLHHT_11/BUG-QLDMLHHT_11-add-close-noconfirm.png`.
