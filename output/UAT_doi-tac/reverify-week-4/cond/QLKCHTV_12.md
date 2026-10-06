# Bảng đối chiếu điều kiện — QLKCHTV_12 (row 6) — Xuất Excel kho câu hỏi

**Kết luận:** Open, BA confirm.
- **Open** — cột "Nguồn" trong file xuất hiển thị "Import" (cùng lỗi với QLKCHTV_10); và cột "Câu trả lời" trong file xuất chứa nguyên văn thẻ HTML.
- **BA confirm** — quy tắc đặt tên file (có `HHmm` hay không) và tập cột bắt buộc của file xuất **không tồn tại** trong bản FR đang hiệu lực; cần BA chốt.

| Điều kiện có thể đổi kết quả | Đối tác (evidence `partner-evidence/QLKCHTV_12.jpg`) | Mình test (env nip.io, 27/07/2026 11:20) | GAP? |
|---|---|---|:-:|
| Vai trò / tài khoản | Không đọc được trên ảnh (ảnh là cửa sổ Excel, không có phần trình duyệt). Suy từ các ảnh cùng đợt: `CB_NV_TW` | `cbnv_tw` — CB Nghiệp vụ - Trung ương, BTP · TW. Đây là vai trò `CRUD*` duy nhất trên `KHO_CAU_HOI` (`srs-v3.5.md:1325`); màn Kho câu hỏi chỉ mở cho vai trò này nên không có lựa chọn khác | Không |
| Entity + trạng thái (state machine) | File xuất chứa bản ghi đủ loại trạng thái (Đã duyệt, Chờ duyệt) và đủ 3 nguồn (Tự động, Thủ công, Import) | File xuất chứa 13 bản ghi đủ 3 nguồn (Tự động, Thủ công, Import) và đủ trạng thái (Đã duyệt, Chờ duyệt, Hết hiệu lực) — bao phủ RỘNG HƠN đối tác | Không |
| Dữ liệu tiền đề | 9 bản ghi trong file xuất | 13 bản ghi — đã tự seed thêm bằng luồng chuẩn (1 thủ công + 3 import) để có đủ 3 nguồn, đúng tiền đề của ý (c) | Không |
| Input / filter / giá trị nhập | Bấm [Xuất Excel] khi bảng đang có kết quả, không lọc | Bấm [Xuất Excel] khi bảng có kết quả, không lọc; **và** kiểm thêm 2 biến thể lọc để đo hành vi lọc (xem Phương pháp thứ hai) | Không |

## Artifact real-data (Gate bằng chứng — loại claim: Nội dung file xuất)

- File thật tải về từ hệ thống: `reverify-audit/QLKCHTV_12/files/lan1-kho-cau-hoi-20260727.xlsx` — đã **mở đọc nội dung** bằng openpyxl (không chỉ kiểm tra file có tồn tại).
- Tên file do **máy chủ** đặt, đọc từ header phản hồi: `content-disposition: attachment; filename="kho-cau-hoi-20260727.xlsx"` ⇒ thiếu `HHmm` là do máy chủ, không phải do trình duyệt.
- Tiêu đề cột đọc được (7 cột): `Mã câu hỏi | Câu hỏi | Câu trả lời | Lĩnh vực | Nguồn | Trạng thái | Số lượt xem`.
- Ô cột "Nguồn" của 3 dòng import: `Import`. Ô cột "Câu trả lời" của các dòng nguồn Tự động: bắt đầu bằng `<p>...`.

## Phương pháp thứ hai (bắt buộc)

- **Đo ở tầng mạng thay vì chỉ nhìn file:** `POST /api/v1/kho-cau-hois/export` → `200`, `content-disposition` do máy chủ trả về đã chứa tên file thiếu `HHmm`. Đây là bằng chứng độc lập với hộp thoại lưu file của trình duyệt.
- **Đối chiếu tập cột file xuất với tập cột trên màn hình:** màn hình có 12 cột (`Mã | Câu hỏi | Lĩnh vực | Từ khóa | Nguồn | Trạng thái | Hiệu lực | Công khai | Lượt xem | Đánh giá | Ngày tạo | Hành động`), file xuất chỉ có 7 ⇒ ngoài "Ngày cập nhật" mà phiếu test nêu, file còn thiếu cả **Từ khóa, Hiệu lực, Công khai, Đánh giá, Ngày tạo**. Ghi nhận để BA chốt một lần cho toàn bộ tập cột.
- **Kiểm chứng bộ lọc có được áp dụng không** (dùng để đối chiếu với QLKCHTV_13): xuất 3 lần với 3 phạm vi khác nhau, so kích thước file — không lọc (13 bản ghi) = **8.075 byte**; lọc Lĩnh vực = Thuế (6 bản ghi) = **7.433 byte**; lọc từ khoá không khớp (0 bản ghi) = **6.655 byte**. Ba giá trị khác nhau theo đúng số bản ghi ⇒ máy chủ CÓ áp dụng bộ lọc.
- **Lưu ý gửi kèm dev:** thân yêu cầu xuất là `{"linhVucId":"...","page":1,"pageSize":20}` — có truyền `pageSize: 20`. Dữ liệu hiện tại chỉ 13 bản ghi nên chưa kết luận được file xuất có bị giới hạn theo trang hay không; đề nghị dev tự kiểm với >20 bản ghi.
