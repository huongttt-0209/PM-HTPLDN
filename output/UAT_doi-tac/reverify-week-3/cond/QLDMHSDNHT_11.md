# Bảng đối chiếu điều kiện — QLDMHSDNHT_11

Loại bug: **Đóng form Thêm/Sửa danh mục đang nhập/sửa dở KHÔNG hiện hộp thoại xác nhận "Bạn có muốn bỏ các thay đổi chưa lưu?".** Phụ thuộc **state form dirty** → cần bảng. (Cùng cụm B4, tab Hồ sơ đề nghị hỗ trợ, cùng component drawer.)

| Điều kiện có thể đổi kết quả | Đối tác (video full-res, ending=list) | Mình test | GAP? |
|---|---|---|:-:|
| Vai trò / tài khoản | QTHT | QTHT (`admin`) | Không |
| Entity + **trạng thái form** | Form Thêm mới tab Hồ sơ đề nghị hỗ trợ ở state dirty | Form Thêm mới nhập Mã/Tên/Mô tả="a" (dirty) | Không |
| Dữ liệu tiền đề | Tab có ≥1 record | Tab Hồ sơ đề nghị hỗ trợ có 4 record | Không |
| Thao tác đóng | Đóng form khi dirty | Bấm nút Đóng (X) khi dirty | Không |

**Kết luận: tái hiện ĐÚNG như đối tác (0 GAP).** Bấm Đóng (X) khi form dirty → drawer đóng thẳng về danh sách (1-4/4 mục), KHÔNG dialog "bỏ thay đổi chưa lưu", 0 toast, 0 request (toast-capture.js, observer tự kiểm=1), record nhập dở bị hủy im lặng.

Đối chiếu SRS v3.5: SCR-VIII-01 (FR-VIII-08, UC106). §Quy tắc tương tác (1606–1608) + TPL-DM-CRUD (65–171) không có clause dialog dirty-state (dialog CÓ ở fr-02:1070, fr-04:1512/1562/1685/1808, silent cho màn danh mục). → **BA confirm**.

Bằng chứng: `reverify-audit/QLDMHSDNHT_11/BUG-QLDMHSDNHT_11-add-close-noconfirm.png`.
