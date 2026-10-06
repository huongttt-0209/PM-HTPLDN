# Bảng đối chiếu điều kiện — QLDMTTVV_11

Loại bug: **Đóng form Thêm/Sửa danh mục đang nhập/sửa dở KHÔNG hiện hộp thoại xác nhận "Bạn có muốn bỏ các thay đổi chưa lưu?".** Phụ thuộc **state form dirty** → cần bảng. (Cùng cụm B4, tab Tình trạng vụ việc, cùng component drawer.)

| Điều kiện có thể đổi kết quả | Đối tác (video full-res t009, form dirty rồi bấm Hủy) | Mình test | GAP? |
|---|---|---|:-:|
| Vai trò / tài khoản | QTHT | QTHT (`admin`) | Không |
| Entity + **trạng thái form** | Form Thêm mới tab Tình trạng vụ việc dirty (Tên="a") | Form Thêm mới nhập Mã/Tên/Mô tả="a" (dirty) | Không |
| Dữ liệu tiền đề | Tab có ≥1 record | Tab Tình trạng vụ việc có 12 record | Không |
| Thao tác đóng | Đóng/Hủy form khi dirty | Bấm nút Đóng (X) khi dirty | Không |

**Kết luận: tái hiện ĐÚNG như đối tác (0 GAP).** Bấm Đóng (X) khi form dirty → drawer đóng thẳng về danh sách (1-12/12 mục), KHÔNG dialog "bỏ thay đổi chưa lưu", 0 toast, 0 request (toast-capture.js, observer tự kiểm=1), record nhập dở bị hủy im lặng.

Đối chiếu SRS v3.5: SCR-VIII-01 (FR-VIII-04, UC102). §Quy tắc tương tác (1606–1608) + TPL-DM-CRUD (65–171) không có clause dialog dirty-state (dialog CÓ ở fr-02:1070, fr-04:1512/1562/1685/1808, silent cho màn danh mục). → **BA confirm**.

Bằng chứng: `reverify-audit/QLDMTTVV_11/BUG-QLDMTTVV_11-add-close-noconfirm.png`.
