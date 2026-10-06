# Bảng đối chiếu điều kiện — QLKCHTV_03 (row 3) — Cột dữ liệu bảng Kho câu hỏi

**Kết luận:** Open — 2/3 ý lệch đặc tả (thiếu cột "Câu trả lời"; cột điểm đặt tên "Đánh giá" thay vì "Điểm TB").
Ý còn lại (thiếu ô chọn hàng loạt) **KHÔNG phải lỗi** — đã chứng minh cột đó CÓ, chỉ hiện với vai trò CB Phê duyệt ở thẻ "Chờ duyệt".

| Điều kiện có thể đổi kết quả | Đối tác (evidence full-res `partner-evidence/QLKCHTV_03.jpg`, bổ trợ `QLKCHTV_16(1)-2.jpg` đã cuộn hết sang phải) | Mình test (env nip.io, 27/07/2026 10:56) | GAP? |
|---|---|---|:-:|
| Vai trò / tài khoản | `CB_NV_TW` — "CB Nghiệp vụ - Trung ương", "BTP · TW" | Test **cả 2 vai trò**: `cbnv_tw` (CB Nghiệp vụ - Trung ương, BTP · TW — trùng đối tác) **và** `cbpd_tw` (CB Phê duyệt - Trung ương, BTP · TW — vai trò sở hữu thao tác duyệt hàng loạt, cần để chấm đúng ý "ô chọn hàng loạt") | Không |
| Entity + trạng thái (state machine) | Bảng ở thẻ "Tất cả", các bản ghi Đã duyệt / Công khai | Bảng ở thẻ "Tất cả" (10 bản ghi) **và** thẻ "Chờ duyệt" (1 bản ghi `QA-20260727-0001` do tôi tự tạo để đủ tiền đề) | Không |
| Dữ liệu tiền đề (số bản ghi + trạng thái có mặt) | 36 bản ghi; thẻ "Chờ duyệt" có 5 bản ghi | Ban đầu 9 bản ghi, thẻ "Chờ duyệt" RỖNG → **đã tự seed** 1 câu hỏi qua luồng chuẩn ("Thêm câu hỏi" → Lưu → về trạng thái "Chờ duyệt") để dựng đúng tiền đề của ý "ô chọn hàng loạt"; sau seed: 10 bản ghi, "Chờ duyệt" = 1 | Không |
| Input / filter / giá trị nhập | Không lọc; cuộn ngang bảng để xem hết cột | Không lọc; đọc trực tiếp toàn bộ `.ant-table-thead th` bằng mã lệnh (không phụ thuộc vùng nhìn thấy) + cuộn ngang chụp ảnh 2 nửa bảng | Không |

## Artifact real-data (Gate bằng chứng — loại claim: Hiển thị/render)

- `bug-reports/image/BUG-QLKCHTV_03-cot-bang.png` — nửa trái bảng (vai trò CB_NV_TW), đã mở đọc.
- `bug-reports/image/BUG-QLKCHTV_03-cot-bang-phai.png` — nửa phải sau khi cuộn ngang, đã mở đọc: thấy rõ `Lượt xem | Đánh giá | Ngày tạo | Hành động`.
- `bug-reports/image/BUG-QLKCHTV_03-cbpd-co-checkbox.png` — đã mở đọc: vai trò **CB_PD_TW**, thẻ "Chờ duyệt", bảng **CÓ** ô chọn ở đầu mỗi dòng + ô "chọn tất cả" ở dòng tiêu đề, kèm nút Duyệt (✓) / Từ chối (✕).
- Đọc thẳng DOM tiêu đề bảng (không phụ thuộc vùng nhìn thấy), **cả 2 vai trò cho cùng 12 cột**:
  `Mã | Câu hỏi | Lĩnh vực | Từ khóa | Nguồn | Trạng thái | Hiệu lực | Công khai | Lượt xem | Đánh giá | Ngày tạo | Hành động`
  → không có cột "Câu trả lời"; cột điểm mang nhãn "Đánh giá".

## Phương pháp thứ hai (bắt buộc)

- Ý "ô chọn hàng loạt" được đo **2 lần bằng 2 vai trò khác nhau**: với `cbnv_tw` → `so_checkbox_trong_bang = 0`; với `cbpd_tw` cùng thẻ "Chờ duyệt", cùng bản ghi → xuất hiện `checkbox "Select all"` + checkbox từng dòng. Hai phép đo KHÔNG mâu thuẫn mà giải thích cho nhau: cột này bị chặn theo vai trò + theo thẻ, đúng như `srs-fr-13-tv-nhanh.md:537` mô tả (duyệt hàng loạt gắn với thẻ "Chờ duyệt").
- Ý "thiếu cột Câu trả lời": dữ liệu trả về từ `GET /api/v1/kho-cau-hois` **có** trường `cauTraLoi` cho mọi bản ghi ⇒ thiếu là ở tầng hiển thị, không phải thiếu dữ liệu.
