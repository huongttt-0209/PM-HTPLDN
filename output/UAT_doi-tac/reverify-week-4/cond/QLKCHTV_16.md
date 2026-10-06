# Bảng đối chiếu điều kiện — QLKCHTV_16 (row 9) — Nút trong cửa sổ "Sửa câu hỏi"

**Kết luận:** Open — cửa sổ Sửa chỉ có [Hủy] [Lưu]; không có đường nào giữ hoặc đưa bản ghi về trạng thái "Nháp", trong khi đặc tả bắt buộc trạng thái này phải tồn tại và dùng được. Cùng gốc với BUG-QLKCHTV_04 và BUG-QLKCHTV_02.

| Điều kiện có thể đổi kết quả | Đối tác (evidence `partner-evidence/QLKCHTV_16(1)-1.jpg`, `-2.jpg`) | Mình test (env nip.io, 27/07/2026 11:19) | GAP? |
|---|---|---|:-:|
| Vai trò / tài khoản | Ảnh -2 (sau khi lưu, cửa sổ đã đóng) đọc rõ: "Cán bộ NV Trung ương", mã `CB_NV_TW`, badge "BTP · TW" | `cbnv_tw` — CB Nghiệp vụ - Trung ương, BTP · TW — TRÙNG KHỚP. Cũng là vai trò duy nhất có quyền Sửa (`srs-v3.5.md:1325`: CB_NV = `CRUD*`, CB_PD chỉ `RU*`) | Không |
| Entity + trạng thái (state machine) | Bản ghi `QA-20260720-0003` — Nguồn **"Import"**, Trạng thái **"Chờ duyệt"**, đang ở thẻ "Chờ duyệt" | Bản ghi `QA-20260727-0002` — Nguồn **"Import"**, Trạng thái **"Chờ duyệt"** — TRÙNG KHỚP cả nguồn lẫn trạng thái | Không |
| Dữ liệu tiền đề | Bản ghi có sẵn từ luồng nhập Excel, có từ khóa (`thue`, `ho tro`, `doanh nghiep nho`) | **Đã tự dựng đúng tiền đề**: nhập Excel để sinh bản ghi cùng loại, có từ khóa (`thue`, `mien giam`, `dnnvv`) | Không |
| Input / filter / giá trị nhập | Bấm nút Sửa trên dòng bảng, cuộn tới đáy cửa sổ, quan sát vùng nút | Bấm nút Sửa trên dòng bảng; đọc **toàn bộ** nút trong cửa sổ bằng mã lệnh (không phụ thuộc vùng nhìn thấy) để loại trừ khả năng nút bị khuất do cuộn | Không |

## Artifact real-data (Gate bằng chứng — loại claim: Hiển thị/render)

- `bug-reports/image/BUG-QLKCHTV_16-drawer-sua-nut.png` — đã mở đọc: cửa sổ **"Sửa câu hỏi QA-20260727-0002"**, vùng nút cố định đáy chỉ có **[Hủy]** và **[Lưu]**.
- Đọc toàn bộ nút trong cửa sổ Sửa: `["Dùng ảnh hệ thống mặc định", "Hủy", "Lưu"]` ⇒ không có [Lưu nháp], không có [Gửi duyệt] ở bất kỳ vị trí nào — không phải bị khuất do cuộn.
- Các trường trong cửa sổ Sửa: Câu hỏi, Câu trả lời, Lĩnh vực, Từ khóa, Ảnh đại diện công khai, Mô tả công khai, Tệp đính kèm công khai — nạp đúng nội dung hiện tại của bản ghi.

## Phương pháp thứ hai (bắt buộc)

- **Đối chứng với cửa sổ Thêm (QLKCHTV_04):** cửa sổ Thêm cũng chỉ có `["Dùng ảnh hệ thống mặc định", "Hủy", "Lưu"]`. Hai cửa sổ giống hệt nhau về vùng nút ⇒ đây là thiếu sót hệ thống ở cả 2 đường vào, không phải sai sót riêng màn Sửa.
- **Đo bằng hành vi thật chứ không chỉ đọc nhãn (đã đo ở QLKCHTV_04):** bấm [Lưu] ở cửa sổ Thêm với dữ liệu hợp lệ → bản ghi ra thẳng **"Chờ duyệt"** (1 request `POST /api/v1/kho-cau-hois`, 1 thông báo *"Tạo câu hỏi thành công, đang chờ duyệt"*). Nghĩa là [Lưu] đang gánh vai trò [Gửi duyệt].
- **Chứng minh trạng thái "Nháp" là bắt buộc theo đặc tả** (nên việc không có đường tới nó là lỗi, không phải lựa chọn thiết kế):
  - `srs-fr-13-tv-nhanh.md:103` — Inputs khai `trang_thai` gồm *"NHAP / CHO_DUYET / DA_DUYET / CONG_KHAI / HET_HIEU_LUC"*.
  - `srs-fr-13-tv-nhanh.md:530` — thanh lọc phải có *"NHAP/CHO_DUYET/DA_DUYET/CONG_KHAI/HET_HIEU_LUC"*.
  - `srs-fr-13-tv-nhanh.md:534` — cửa sổ nhập Q&A phải có *"[Huy] [Luu nhap] [Gui duyet]"*.
  - `srs-fr-13-tv-nhanh.md:536` — hành động từ chối: *"[Tu choi] modal ly do bat buoc + **SET NHAP** + TB CB NV"* ⇒ bản ghi bị từ chối **phải quay về Nháp**, và cán bộ nghiệp vụ phải sửa rồi gửi duyệt lại. Với vùng nút hiện tại, sau khi sửa chỉ có [Lưu] — không có đường nghiệp vụ rõ ràng để giữ nháp hay gửi duyệt lại.
  - Chính giao diện cũng đang truy vấn `NHAP`: `GET /api/v1/kho-cau-hois?trangThai=CHO_DUYET,NHAP&page=1&pageSize=1` ⇒ trạng thái này có thật trong hệ thống.
- **Ghi nhận trung thực khoảng trống đặc tả:** SRS v3.5 mô tả cửa sổ **Thêm** (dòng 534) nhưng **không mô tả riêng cửa sổ Sửa**; dòng 531 chỉ liệt kê nút "Sua" trong cột Hành động. Vì vậy bug này mô tả **yêu cầu nghiệp vụ** (phải có đường giữ/đưa bản ghi về Nháp), không quy định dev phải đặt đúng 2 nút tên gì.
