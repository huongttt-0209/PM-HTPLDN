# Bảng đối chiếu điều kiện — QLKCHTV_18 (row 10) — Hộp thoại xác nhận Bật/tắt hiệu lực

**Kết luận:** BA confirm — hộp thoại thực tế tái hiện đúng như đối tác mô tả, nhưng **câu chữ mà phiếu test kỳ vọng KHÔNG có trong SRS v3.5**. Ngược lại, đặc tả mô tả đây là thao tác gạt trực tiếp, **không** yêu cầu hộp thoại xác nhận nào. Cần BA chốt trước khi chuyển dev.

| Điều kiện có thể đổi kết quả | Đối tác (evidence `partner-evidence/QLKCHTV_18.jpg`) | Mình test (env nip.io, 27/07/2026 11:16) | GAP? |
|---|---|---|:-:|
| Vai trò / tài khoản | Không đọc được trên ảnh (hộp thoại + panel che vùng avatar). Suy từ các ảnh cùng đợt: `CB_NV_TW` | `cbnv_tw` — CB Nghiệp vụ - Trung ương, BTP · TW. Đặc tả giao thao tác này cho Cán bộ Nghiệp vụ: `srs-fr-13-tv-nhanh.md:118` *"CB NV đánh dấu 'Hết hiệu lực'"* | Không |
| Entity + trạng thái (state machine) | Bản ghi `QA-20260702-0003` — Nguồn "Tự động", Trạng thái **"Đã duyệt"**, Hiệu lực **"Có"** (tức đang bật, sắp tắt) | Bản ghi `QA-20260708-0001` — Nguồn "Tự động", Trạng thái **"Đã duyệt"**, Hiệu lực **"Có"** — TRÙNG KHỚP. **Bổ sung**: đo tiếp chiều ngược lại (Hiệu lực "Không" → bật lại) mà ảnh đối tác không có | Không |
| Dữ liệu tiền đề | Bản ghi đã duyệt, đang có hiệu lực | Bản ghi đã duyệt, đang có hiệu lực. Sau khi đo xong đã **khôi phục nguyên trạng** (bật lại hiệu lực, bản ghi trở về "Đã duyệt" / Hiệu lực "Có") | Không |
| Input / filter / giá trị nhập | Mở chi tiết → bấm nút bật/tắt hiệu lực → đọc hộp thoại | Mở chi tiết → bấm **[Hết hiệu lực]** → đọc hộp thoại; rồi bấm **[Kích hoạt hiệu lực]** → đọc hộp thoại chiều ngược lại. Đọc tiêu đề/nội dung bằng mã lệnh để lấy nguyên văn | Không |

## Artifact real-data (Gate bằng chứng — loại claim: Hiển thị/render)

- `bug-reports/image/BUG-QLKCHTV_18-dialog-het-hieu-luc.png` — đã mở đọc: hộp thoại tiêu đề **"Đánh dấu hết hiệu lực"**, nội dung **"Câu hỏi sẽ ngừng hiển thị nhưng vẫn lưu trong hệ thống. Tiếp tục?"**, nút **[Hủy]** / **[Đồng ý]** (đỏ).
- Đọc nguyên văn 2 chiều:
  - Tắt: tiêu đề `"Đánh dấu hết hiệu lực"` · nội dung `"Câu hỏi sẽ ngừng hiển thị nhưng vẫn lưu trong hệ thống. Tiếp tục?"`
  - Bật lại: tiêu đề `"Kích hoạt hiệu lực"` · nội dung `"Câu hỏi sẽ được kích hoạt lại và hiển thị cho người dùng. Tiếp tục?"`
- Cả 2 hộp thoại **không chứa mã câu hỏi**.

## Phương pháp thứ hai (bắt buộc)

- **Đo bằng hành vi thật, không chỉ đọc chữ:** bấm [Đồng ý] → đo bằng bộ bắt thông báo dùng chung (1 observer, đã tự kiểm): `SO_REQUEST = 1` (`POST /api/v1/kho-cau-hois/{id}/het-hieu-luc`), `SO_KHUNG_THONG_BAO = 1` (*"Đã đánh dấu hết hiệu lực"*), không lặp. Bản ghi chuyển sang Trạng thái **"Hết hiệu lực"**, Hiệu lực **"Không"**. Bấm [Kích hoạt hiệu lực] → khôi phục về "Đã duyệt" / Hiệu lực "Có". ⇒ **chức năng chạy đúng**, sai lệch (nếu có) chỉ nằm ở câu chữ hộp thoại.
- **Tìm nguyên văn câu kỳ vọng trong đặc tả:** đã tìm toàn bộ `srs-v3.5/` (gồm `srs-v3.5.md` và `CHANGELOG-v3-to-v3.5.md`) với các biến thể *"Bạn có chắc"* / *"Ban co chac"* → **0 kết quả**. Câu mà phiếu test nêu (*"Bạn có chắc chắn muốn đánh dấu câu hỏi «{mã}» là «{hết hiệu lực/có hiệu lực}»?"*) **không tồn tại trong SRS v3.5** ⇒ nhiều khả năng đến từ tài liệu thiết kế khác của bên đối tác.
- **Đặc tả nói ngược lại:** `srs-fr-13-tv-nhanh.md:533` mô tả *"Toggle hieu luc | toggle | Tat -> hieu_luc = 0, an khoi Cong. Bat -> hieu_luc = 1 | **toggle -> cap nhat** | luon hien thi"* — tức gạt là cập nhật ngay, **không nhắc tới hộp thoại xác nhận**. `:118` và `:160` cũng chỉ mô tả kết quả, không mô tả hộp thoại.
- **Đối chứng nội bộ cùng màn hình (chứng minh đây là chủ đích, không phải sót):** cùng SCR-X2-01, hành động **Công khai / Hủy công khai** (`srs-fr-13-tv-nhanh.md:538`) **CÓ** ghi rõ *"modal xac nhan"* — 2 lần. Việc đặc tả ghi modal cho hành động này mà không ghi cho Bật/tắt hiệu lực là một khác biệt có chủ ý, không phải thiếu sót ngẫu nhiên.
- **Kết luận đo được:** ứng dụng đang **cẩn thận hơn** đặc tả (thêm hộp thoại xác nhận mà đặc tả không đòi). Vì vậy không chấm là lỗi; chuyển BA chốt: (a) có bắt buộc hộp thoại không, (b) nếu có thì câu chữ chuẩn là gì và có phải nhắc mã câu hỏi không.
- **Phát hiện thêm (ngoài phạm vi phiếu):** phía sau hộp thoại, phần "Câu trả lời" của bản ghi hiện nguyên văn thẻ HTML — trùng với phát hiện ở QLKCHTV_14, đã tách bug riêng `BUG-KCH-HTML-THO`.
