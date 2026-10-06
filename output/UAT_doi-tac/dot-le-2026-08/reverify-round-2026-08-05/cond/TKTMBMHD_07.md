# Bảng đối chiếu điều kiện — TKTMBMHD_07 (re-verify vòng 2, 05/08/2026)

Loại bug: **hành vi của nút "Xóa bộ lọc" trên danh sách thư mục biểu mẫu** → phụ thuộc dữ liệu + trạng thái bộ lọc ⇒ bắt buộc điền bảng, 0 GAP.
Ô note của dòng này (*DEV phản hồi lần 2*) KHÔNG có khối `── CÁCH VERIFY sau Dev fix ──`, nên lấy phần **"Phần còn lỗi"** làm điều kiện phải hết lỗi, phần **"Phần đã được sửa"** làm mốc đã đạt (vẫn kiểm lại để chắc không hồi quy).

| Điều kiện | Bug gốc (note vòng 2) | Mình test | GAP? |
|---|---|---|---|
| Môi trường | Môi trường bàn giao, bản dựng đang chạy | `https://18.143.165.120.nip.io` — bản dựng **HTPLDN · V1.0.6** (đọc ở thanh bên trái) | Không |
| Vai trò | Tài khoản xem được Thư viện biểu mẫu | `cbnv_tw` · CB_NV_TW · Cục Bổ trợ tư pháp - Bộ Tư pháp · cấp TW | Không |
| Màn hình | Thư viện biểu mẫu → Thư mục | Biểu mẫu → **Thư viện biểu mẫu** → màn Thư mục (`/bieu-mau/thu-muc`) | Không |
| Mốc "danh sách mặc định" | Mặc định màn hình có 23 thư mục (số của môi trường đối tác) | Đo mốc mặc định TRƯỚC khi lọc trên môi trường này: **13 thư mục**, thẻ "Tất cả 13", "Hiển thị 1-13 / 13 kết quả" — dùng 13 làm mốc so sánh thay cho 23 | Không |
| Bộ lọc lần 1 | Gõ từ khóa rồi bấm "Xóa bộ lọc" | Gõ từ khóa **"IMPORT"** → Tìm kiếm → còn 3 kết quả, thẻ đổi thành "Tất cả 3"; đồng thời chuyển sang thẻ **Nháp** → bấm **Xóa bộ lọc** | Không |
| Bộ lọc lần 2 (note nói đã thử 2 bộ lọc) | Gõ từ khóa kèm lĩnh vực rồi bấm "Xóa bộ lọc" | Chọn **Lĩnh vực = Thuế** + **Từ ngày = 20/07/2026** → Tìm kiếm → còn 3 kết quả → bấm **Xóa bộ lọc** | Không |
| Kiểm nút "Làm mới" | Bấm "Làm mới" cũng không đưa danh sách về mặc định | Đặt lại từ khóa "IMPORT" → bấm **Làm mới** và đối chiếu ô lọc với danh sách | Không |
| Cách đo | Đếm số bản ghi + số trên thẻ phân loại | Đọc trực tiếp số dòng của bảng, chữ trên thẻ, dòng "Hiển thị ... kết quả", nội dung các ô lọc và địa chỉ trang; kèm ảnh chụp 3 mốc (trước lọc / đang lọc / sau khi xóa lọc) | Không |

**Kết luận: 0 GAP** — đúng bản dựng đang chạy, đúng vai trò, đúng màn hình, đã đo mốc mặc định trước khi lọc, chạy đủ 2 bộ lọc khác nhau đúng như note mô tả và bấm thật nút "Xóa bộ lọc".

## Đo lường trực tiếp (05/08/2026, `18.143.165.120.nip.io`, bản dựng V1.0.6)

### Mốc mặc định trước khi lọc

- 13 thư mục, thẻ **"Tất cả 13"**, "Hiển thị 1-13 / 13 kết quả", các ô lọc đều trống, sắp xếp theo ngày tạo giảm dần (25/07 → 20/07 → 15/07 → 30/06).
  Ảnh: [`../image/TKTMBMHD_07-1-mac-dinh-truoc-khi-loc.png`](../image/TKTMBMHD_07-1-mac-dinh-truoc-khi-loc.png)

### Phần "còn lỗi" của note — kiểm lại từng ý

- ✅ **"Danh sách KHÔNG trở về mặc định"** → nay ĐÃ trở về. Lần 1: từ khóa "IMPORT" + đang đứng ở thẻ Nháp (còn 2 kết quả) → bấm **Xóa bộ lọc** → danh sách quay lại đủ **13 thư mục**, đúng thứ tự và đúng bộ bản ghi như mốc mặc định.
- ✅ **"Số đếm trên thẻ Tất cả cũng đổi theo"** → nay thẻ quay về **"Tất cả 13"** (bằng đúng mốc mặc định), không còn kẹt ở con số của lần lọc trước.
- ✅ **Lặp lại với bộ lọc thứ hai** → Lĩnh vực "Thuế" + Từ ngày 20/07/2026 (còn 3 kết quả) → bấm **Xóa bộ lọc** → ô Lĩnh vực về "Tất cả", ô Từ ngày trắng, danh sách về đủ 13, thẻ về "Tất cả 13". Cả hai bộ lọc đều cho cùng kết quả đúng.
- ✅ **"Bấm thêm nút Làm mới cũng không đưa danh sách về mặc định"** → không còn là vấn đề. Khi còn từ khóa "IMPORT" trong ô tìm kiếm, bấm **Làm mới** thì ô lọc VẪN hiện "IMPORT" và danh sách vẫn là 3 kết quả khớp — tức ô lọc và danh sách khớp nhau, không còn cảnh "ô lọc trông như đã trống nhưng danh sách vẫn đang bị lọc". Đây là cách làm hợp lý của nút tải lại (tải lại theo đúng bộ lọc đang hiển thị), không phải lỗi.
  Ảnh (đang lọc): [`../image/TKTMBMHD_07-2-dang-loc-tu-khoa-va-tab-nhap.png`](../image/TKTMBMHD_07-2-dang-loc-tu-khoa-va-tab-nhap.png)
  Ảnh (sau khi Xóa bộ lọc): [`../image/TKTMBMHD_07-3-sau-khi-xoa-bo-loc-ve-mac-dinh.png`](../image/TKTMBMHD_07-3-sau-khi-xoa-bo-loc-ve-mac-dinh.png)

### Phần "đã được sửa" của note — kiểm lại xem có hồi quy không

- ✅ Thanh thẻ phân loại tự về **"Tất cả"** sau khi bấm Xóa bộ lọc (thử từ thẻ Nháp, vẫn về đúng Tất cả và được chọn).
- ✅ Các ô **Tìm kiếm / Lĩnh vực / Trạng thái / Từ ngày / Đến ngày** đều được xóa trắng.
- ✅ Không có hồi quy ở hai ý này.

### Kết luận

Ý duy nhất còn lỗi ở vòng trước — danh sách và số đếm trên thẻ không trở về mặc định sau khi bấm "Xóa bộ lọc" — nay đã hết, đúng với cả hai bộ lọc khác nhau; phần đã sửa trước đó vẫn giữ nguyên, không hồi quy → **Pass**.

### Ghi nhận thêm (ngoài phạm vi phiếu — không tự thêm dòng mới vào sheet)

- Ô tìm kiếm khớp theo cụm chữ liền: gõ "IMPORT" ra 3 kết quả, nhưng gõ "QA-R7" lại ra "Không tìm thấy thư mục phù hợp" dù trên danh sách có các thư mục tên QA-R7-E-CO-BM / QA-R7-D-RONG / QA-R7-A-CO-BM. Không thuộc phạm vi phiếu này (phiếu chỉ về nút Xóa bộ lọc), chỉ ghi lại để đối tác/BA biết.
