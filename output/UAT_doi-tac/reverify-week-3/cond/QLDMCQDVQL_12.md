# Bảng đối chiếu điều kiện — QLDMCQDVQL_12

Loại bug: **Đóng/hủy form đang nhập dở KHÔNG hiện hộp thoại xác nhận "Bạn có muốn bỏ các thay đổi chưa lưu?".** Phụ thuộc **state form dirty** → cần bảng. (Cùng cụm B4 nhưng tab **Cơ quan đơn vị = Tree View**, form là panel chi tiết bên phải + nút Hủy, KHÁC cấu trúc drawer của các tab phẳng — verify riêng.)

| Điều kiện có thể đổi kết quả | Đối tác (video full-res t004→t012) | Mình test | GAP? |
|---|---|---|:-:|
| Vai trò / tài khoản | QTHT | QTHT (`admin`) | Không |
| Entity + **trạng thái form** | Form "Thêm đơn vị mới" (panel phải) dirty: Mã đơn vị="tkm", Tên="tkm", Cấp="Trung ương" → panel reset về empty detail (t012), form bị hủy | Form "Thêm đơn vị mới" nhập Mã="TKM-B4", Tên="TKM test bỏ thay đổi" (dirty) | Không |
| Dữ liệu tiền đề | Cây đơn vị có ≥1 node (Cục Bổ trợ tư pháp) | Cây có node TW "Cục Bổ trợ tư pháp - Bộ Tư pháp" | Không |
| Thao tác đóng | Hủy/rời form khi dirty (panel reset không cảnh báo) | Bấm nút **Hủy** khi form dirty | Không |

**Kết luận: tái hiện ĐÚNG như đối tác (0 GAP).** Bấm Hủy khi form "Thêm đơn vị mới" đang dirty → panel reset về "Chi tiết đơn vị" empty ("Chọn một đơn vị từ cây bên trái..."), **KHÔNG** dialog "bỏ thay đổi chưa lưu", 0 toast, 0 request (toast-capture.js, observer tự kiểm=1), dữ liệu nhập dở bị hủy im lặng — khớp frame t012 của đối tác. Kể cả form Tree-View (panel, không phải drawer) vẫn cùng hành vi → củng cố 1 bug gốc chung toàn cụm.

Đối chiếu SRS v3.5: SCR-VIII-01 (FR-VIII-05, UC103, Tree View dòng 1584–1591). §Quy tắc tương tác (1606–1608) + TPL-DM-CRUD (65–171) + thành phần Tree View (1584–1591) KHÔNG có clause dialog dirty-state (dialog này CÓ ở fr-02:1070, fr-04:1512/1562/1685/1808, silent cho màn danh mục). → **BA confirm**.

Bằng chứng: `reverify-audit/QLDMCQDVQL_12/BUG-QLDMCQDVQL_12-cancel-dirty-noconfirm.png`.
