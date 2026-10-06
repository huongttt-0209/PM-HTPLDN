# Bảng đối chiếu điều kiện — QLKCHTV_35 (row 17) — Thiếu chức năng "Đẩy sang Nhóm II"

**Kết luận:** Open (Major).
- Tái hiện đúng: màn trả lời **không có nút "Đẩy sang Nhóm II"** — chỉ có [Gửi trả lời].
- Đặc tả v3.5 yêu cầu rất rõ ở **4 chỗ độc lập**: `:204` (bước xử lý 9), `:211` + `:216` + `:218` (đầu ra & trạng thái sau), `:227` (mã lỗi `ERR-TVN-03` dành riêng cho thao tác này), `:236` (tiêu chí nghiệm thu), `:572` (nút trên màn SCR-X2-03).
- Đã kiểm cả tầng máy chủ: chức năng **cũng chưa có ở phía sau**, không phải chỉ thiếu nút (chi tiết ở Phương pháp thứ hai) — thông tin này để dev ước lượng đúng khối lượng.

| Điều kiện có thể đổi kết quả | Đối tác (evidence `partner-evidence/QLKCHTV_35.jpg`) | Mình test (env nip.io, 27/07/2026 11:56) | GAP? |
|---|---|---|:-:|
| Vai trò / tài khoản | `CB_NV_TW` — "Cán bộ NV Trung ương", BTP · TW | `cbnv_tw` — CB Nghiệp vụ - Trung ương, BTP · TW — TRÙNG KHỚP. Đặc tả giao thao tác này cho *"CB NV/TVV"* (`:204`) | Không |
| Entity + trạng thái (state machine) | Phiên `2f144009-…` ở màn trả lời, **chưa** ở trạng thái "Hoàn thành" (đúng điều kiện hiển thị mà phiếu test nêu) | Phiên `TVN-20260727-0001` trạng thái **"CB trả lời"** — chưa Hoàn thành, đúng điều kiện. **Bổ sung** kiểm thêm phiên `TVN-20260727-0004` mới tạo để chắc chắn nút không phụ thuộc lịch sử thao tác | Không |
| Dữ liệu tiền đề | Phiên đang ở chế độ nhập liệu | Phiên đang ở chế độ nhập liệu (ô soạn nhập được, nút [Gửi trả lời] bật) | Không |
| Input / filter / giá trị nhập | Cuộn xuống cuối cột phải, tìm nút bên cạnh [Gửi trả lời] | Liệt kê **toàn bộ** nút trong vùng nội dung bằng mã lệnh (không phụ thuộc việc cuộn tới đâu) | Không |

## Artifact real-data (Gate bằng chứng — loại claim: Hiển thị/render + Hành vi)

- `bug-reports/image/BUG-TVN-man-tra-loi-cot-trai.png` và `bug-reports/image/BUG-TVN-chon-tu-kho-vuot-gioi-han-5000.png` — đã mở đọc: cuối cột phải chỉ có **một** nút xanh **[Gửi trả lời]**, không có nút cảnh báo nào bên cạnh.
- Liệt kê toàn bộ nút trong vùng nội dung màn trả lời (đọc bằng mã lệnh, không phụ thuộc vùng nhìn thấy):
  `["Quay lại danh sách", "Tìm kiếm", "Gửi trả lời"]` — **không có** "Đẩy sang Nhóm II" / "Escalate".
- Quét chữ toàn màn: không có cụm "Nhóm II" ở bất kỳ đâu.

## Phương pháp thứ hai (bắt buộc)

- **Kiểm tầng máy chủ để xác định thiếu ở đâu (phép thử quyết định).** Đọc danh mục giao diện lập trình của hệ thống (`/api/docs-json`), nhóm tư vấn nhanh có 10 đường dẫn; đường gần nghĩa nhất là `POST /api/v1/tu-van-nhanhs/{id}/chuyen-kenh`. Đã **gọi thử** trên phiên tạo riêng `TVN-20260727-0004`:

  Đối chiếu điều đặc tả yêu cầu (`:204`, `:216`, `:218`) với kết quả thực tế của `chuyen-kenh`:
  - Tạo bản ghi Hỏi đáp Nhóm II với kênh tiếp nhận "Từ Tư vấn nhanh" → ❌ `hoiDapId` vẫn `null`, **không tạo bản ghi nào**
  - Giữ liên kết về phiên tư vấn nhanh gốc → ❌ không có
  - Chuyển phiên sang trạng thái "Hoàn thành" → ❌ vẫn ở **"CB trả lời"**
  - Ghi chú "Đã đẩy sang Nhóm II hỏi đáp «{mã}»" → ❌ không có
  - *Thực tế `chuyen-kenh` chỉ làm một việc*: đổi **Kênh** từ "TV Nhanh" → "Thủ công"

  ⇒ `chuyen-kenh` là một thao tác **khác**, không phải chức năng đẩy sang Nhóm II. Kết luận: chức năng chưa có ở **cả giao diện lẫn máy chủ**.
- **Đối chiếu đặc tả — trích nguyên văn 4 chỗ:**
  - `srs-fr-13-tv-nhanh.md:204` (FR-X.2-02, bước xử lý 9): *"**Đẩy sang Nhóm II giữa chừng (do CB/TVV chủ động):** Nếu CB NV/TVV phát hiện câu hỏi cần xử lý chính thức … → click nút "Đẩy sang Nhóm II" → mở modal xác nhận → tạo bản ghi HOI_DAP với `kenh_tiep_nhan = TVN_BRIDGE` + `tu_van_nhanh_goc_id = TU_VAN_NHANH.id` …; cập nhật trạng thái phiên TV nhanh sang HOAN_THANH với ghi chú "Đã đẩy sang Nhóm II hỏi đáp #{ma_hoi_dap}"; gửi thông báo cho cán bộ Nhóm II tiếp nhận."*
  - `:227` (bảng xử lý lỗi, E4): *"Đẩy sang Nhóm II khi phiên đã HOAN_THANH | ERR-TVN-03 | "Phiên tư vấn đã kết thúc, không thể đẩy sang Nhóm II" | ERROR"* — đặc tả đã cấp **mã lỗi riêng**, tức thao tác này là bắt buộc phải có.
  - `:236` (tiêu chí nghiệm thu): *"**Given** CB NV/TVV đang trả lời phát hiện câu hỏi cần xử lý chính thức **When** click "Đẩy sang Nhóm II" + xác nhận **Then** tạo HOI_DAP với kênh = TVN_BRIDGE + liên kết phiên TV nhanh gốc; phiên TV nhanh đóng với ghi chú đã đẩy sang Nhóm II"*
  - `:572` (§3 SCR-X2-03, cột phải): *"**Them nut phu "Day sang Nhom II"** (button warning, ben canh nut Gui tra loi) … click -> mo modal xac nhan"*
- **Kiểm tra phía nhận để chắc đây không phải chức năng đã dời sang module khác:** đặc tả `:573` mô tả luồng *"TV Thu cong -> UC12 (Nhóm II Hỏi đáp) với kênh tiếp nhận = TVN_BRIDGE + liên kết phiên Tư vấn nhanh gốc"* ⇒ đầu nhận ở nhóm Hỏi đáp có tồn tại trong đặc tả; chỉ đầu gửi ở Tư vấn nhanh là chưa được dựng.
