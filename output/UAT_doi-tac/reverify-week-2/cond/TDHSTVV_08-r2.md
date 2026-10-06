# Bảng đối chiếu điều kiện — TDHSTVV_08 (verify phản ánh vòng 2)

**Claim vòng 2 của đối tác:** "Hệ thống không lưu nháp mà thực hiện cập nhật trạng thái của bản ghi là **Đang thẩm định**".

**Evidence:** `TDHSTVV_08_v2.webm` — video 57 giây (trích khung bằng `tools/extract_frames.py`, thêm dải 0,5 s/khung cho đoạn 20–30 s).
Diễn biến đọc được:
- t≈0 s — danh sách tab "Mới đăng ký" **27 bản ghi**; `TVV-BTP-TW-0058 — Tư vấn viên 1` đang ở trạng thái **Mới đăng ký**.
- t≈6 s — màn chi tiết `/chuyen-gia-tvv/39f6910f-…`, tab **Thẩm định** đang mở, đang điền 4 nhóm tiêu chí.
- t≈21,0 s và t≈21,7 s — **con trỏ nằm đúng trên nút "Lưu nháp"**, nút hiện viền tiêu điểm (đã bấm). Không có khung hình nào cho thấy con trỏ chạm nút "Gửi KQ" hay "Trình duyệt".
- t≈22,7 s — hộp thông báo xanh **"Đã lưu kết quả thẩm định"**.
- t≈36 s — quay lại danh sách, tab "Mới đăng ký" còn **26 bản ghi**.
- t≈48 s — mở lại chi tiết: `TVV-BTP-TW-0058` hiển thị trạng thái **"Đang thẩm định"**.
- t≈54 s — mở lại tab Thẩm định: nội dung đã nhập (Nhóm 1 tick đủ, Kết luận Pháp lý "Đạt", Điểm nhóm 2 = 3, Nhận xét "tốt") **vẫn còn**.

Header trong video: **"BTP · TW · Cán bộ NV Trung ương · CB_NV_TW"**, thời điểm 25/07/2026 16:58–16:59.

| Điều kiện có thể đổi kết quả | Đối tác (từ evidence, full-res) | Mình test | GAP? |
|---|---|---|:-:|
| Vai trò / cấp | Cán bộ Nghiệp vụ **Trung ương** (`CB_NV_TW`), badge "BTP · TW" | `cbnv_tw` — vai trò **CB_NV_TW**, badge "BTP · TW" (trùng khít) | Không |
| Màn hình + thẻ | Màn chi tiết tư vấn viên `/chuyen-gia-tvv/{id}`, thẻ **Thẩm định** | Cùng đường dẫn, cùng thẻ Thẩm định | Không |
| Trạng thái bản ghi trước thao tác | **Mới đăng ký** (`TVV-BTP-TW-0058`) | **Mới đăng ký** — bản ghi QA tự tạo `TVV-BTP-TW-0019` và `TVV-BTP-TW-0020`, đọc trạng thái bằng lời gọi dữ liệu ngay trước khi bấm (`MOI_DANG_KY`, phiên bản 1) | Không |
| Quan hệ đơn vị người xem ↔ tư vấn viên | Tư vấn viên mã `TVV-BTP-TW-…` ⇒ cùng Cục Bổ trợ tư pháp – Bộ Tư pháp với người xem | Cùng đơn vị — cả 2 bản ghi thuộc "Cục Bổ trợ tư pháp – Bộ Tư pháp", trùng đơn vị tài khoản `cbnv_tw` | Không |
| Nút được bấm | **"Lưu nháp"** (2 khung hình liên tiếp cho thấy con trỏ trên nút + nút có viền tiêu điểm) | **"Lưu nháp"** — chọn phần tử theo đúng nhãn "Lưu nháp" rồi mới bấm | Không |
| Dữ liệu đã nhập trước khi bấm | Nhóm 1 tick đủ 4 mục + Kết luận Pháp lý "Đạt"; Nhóm 2 điểm 3 + nhận xét "tốt"; Nhóm 3 nhận xét "tốt"; Nhóm 4 tích "Có tham gia mạng lưới"; Kết luận thẩm định "ĐẠT" | Lần 2 (`TVV-BTP-TW-0020`) nhập **y hệt**: Nhóm 1 đủ + Pháp lý "Đạt", Nhóm 2 điểm 3 + "tốt", Nhóm 3 "tốt", Nhóm 4 tích, Kết luận "ĐẠT" — đã đọc lại toàn bộ giá trị biểu mẫu ngay trước khi bấm để xác nhận trùng | Không |
| Trình duyệt / kích thước cửa sổ | Cốc Cốc trên Windows, cửa sổ tối đa | Chrome 1440×900 — thao tác đo ở tầng dữ liệu (trạng thái + phiên bản bản ghi trước/sau) nên không phụ thuộc kích thước cửa sổ | Không |

**Kết luận:** 0 GAP — cùng vai trò, cùng màn/thẻ, cùng trạng thái đầu vào, cùng nút bấm, cùng bộ dữ liệu nhập; đo 2 bản ghi độc lập.

**Kết quả tái hiện:** ở cả 2 lần đo, sau khi bấm "Lưu nháp" trạng thái **giữ nguyên "Mới đăng ký"** (phiên bản bản ghi 1 → 2), thông báo hiện ra là **"Đã lưu nháp kết quả thẩm định"**.
Cách xử lý tình huống "không tái hiện nhưng đối tác có bằng chứng rõ" + các sai lệch khác QA phát hiện trên cùng màn:
xem [`../reverify-audit/TDHSTVV_08/audit.md`](../reverify-audit/TDHSTVV_08/audit.md).
