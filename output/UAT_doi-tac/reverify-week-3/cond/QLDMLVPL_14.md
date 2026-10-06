# Bảng đối chiếu điều kiện — QLDMLVPL_14

Loại bug: **Đóng form Thêm/Sửa danh mục đang nhập/sửa dở KHÔNG hiện hộp thoại xác nhận "Bạn có muốn bỏ các thay đổi chưa lưu?".** Verdict phụ thuộc: khi form ở trạng thái dirty (đã đổi field) mà bấm đóng, hệ thống có cảnh báo trước khi hủy thay đổi không. Bug phụ thuộc **state của form** (dirty) → cần bảng.

| Điều kiện có thể đổi kết quả | Đối tác (từ video full-res) | Mình test | GAP? |
|---|---|---|:-:|
| Vai trò / tài khoản | QTHT (màn Danh mục chỉ QTHT truy cập) | QTHT (`admin`) — đúng vai trò của bug | Không |
| Entity + **trạng thái form** | Form "Thêm mới danh mục" tab Lĩnh vực pháp lý ở state **dirty** (Mã/Tên/Mô tả = "a") | Test 2 state: (1) form **Sửa** THUE đổi Tên→"Thuế EDIT-B4"; (2) form **Thêm mới** nhập Mã/Tên/Mô tả="a" — cả 2 đều dirty | Không |
| Dữ liệu tiền đề | Tab có ≥1 record để mở form | Tab Lĩnh vực pháp lý có 10 record | Không |
| Thao tác đóng | Đóng drawer khi đang dirty (video: drawer biến mất, không lưu record "a") | Bấm nút **Đóng (X)** góc drawer khi dirty | Không |

**Kết luận: tái hiện ĐÚNG như đối tác báo (0 GAP).** Trên bản kiểm thử hiện tại, bấm Đóng (X) khi form đang dirty → drawer đóng thẳng về danh sách, **KHÔNG** hiện dialog "bỏ thay đổi chưa lưu", KHÔNG toast, 0 request (đo bằng `tools/toast-capture.js`, observer tự kiểm = 1), không có chữ "chưa lưu"/"bỏ thay đổi" nào trên màn; record nhập dở bị hủy im lặng (danh sách vẫn 1-10/10 mục). Áp dụng cho cả form Sửa lẫn Thêm mới (cùng component drawer).

Đối chiếu SRS v3.5 (SCR-VIII-01): §Quy tắc tương tác (dòng 1606–1608) chỉ quy định phân trang + sắp xếp; TPL-DM-CRUD Inputs/Processing/Outputs/Error (dòng 65–171) + thành phần modal (dòng 1582: "Nút Hủy/Lưu → đóng/lưu") **KHÔNG** có clause dialog xác nhận dirty-state. Dialog này CÓ được quy định ở module khác (`srs-fr-02-hoi-dap.md:1070`, `srs-fr-04-chuyen-gia-tvv.md:1512/1562/1685/1808`) nhưng **silent** cho màn Danh mục dùng chung. → Actual đúng như đối tác quan sát nhưng kỳ vọng (cảnh báo dirty-state) là thứ SRS **không quy định** cho màn này → **BA confirm** (bất đồng về đặc tả, để BA quyết có bổ sung cho nhất quán UX không). KHÔNG phải `Open` (không vi phạm clause SRS nào của SCR-VIII-01), KHÔNG phải `Reject` (lỗi/hành vi đối tác báo tái hiện đúng).

Bằng chứng: `reverify-audit/QLDMLVPL_14/BUG-QLDMLVPL_14-edit-close-noconfirm.png`, `BUG-QLDMLVPL_14-add-close-noconfirm.png`.
