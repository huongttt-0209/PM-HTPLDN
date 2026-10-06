# TKTMBMHD_07 — đo lại trên môi trường nghiệm thu đối tác (05/08/2026)

Tiêu chí lấy nguyên khối ở cột `DEV phản hồi lần 2`, dòng 91 (tab `UAT_TGPL Doanh Nghiệp-tuần 3`).

| Điều kiện | Bug gốc (khối tiêu chí) | Mình test | GAP? |
|---|---|---|---|
| Môi trường | Bản mới nhất của môi trường nghiệm thu (dev đo 05/08/2026) | `https://htpldn-uat.ospgroup.vn` — nhãn `HTPLDN · V1.0.7` | Không |
| Vai trò | Cán bộ nghiệp vụ xem Thư viện biểu mẫu | `cbnv_tw` · CB_NV_TW · cấp TW · Cục Bổ trợ tư pháp | Không |
| Màn hình | Thư viện biểu mẫu, mục Thư mục | Biểu mẫu → Thư viện biểu mẫu (`/bieu-mau/thu-muc`) | Không |
| Nút bấm | "Xóa bộ lọc" | Đúng nút đó | Không |
| Bộ lọc thử 1 | Theo từ khóa | Gõ từ khóa `TKM` + bấm Tìm kiếm, rồi chuyển thẻ phân loại sang "Nháp" | Không |
| Bộ lọc thử 2 | Theo lĩnh vực kèm khoảng ngày | Lĩnh vực `Thuế` + khoảng ngày `01/07/2026 – 31/07/2026` + bấm Tìm kiếm, rồi chuyển thẻ sang "Đã ẩn" | Không |
| Điểm phải xem | 4 ô lọc trắng · thẻ về "Tất cả" · số đếm thẻ đúng mặc định · danh sách mặc định sắp theo ngày tạo giảm dần | Đo đủ cả 4 điểm sau mỗi lần bấm, kèm đối chiếu tham số trên thanh địa chỉ | Không |

**Kết luận: 0 GAP → PASS.**

## Đối chiếu từng ý của khối tiêu chí

- **Danh sách trở về đầy đủ bản ghi mặc định, không giữ kết quả của lần lọc trước.** Lần thử 2 (nặng nhất):
  lọc `Thuế` + `01/07–31/07/2026` kéo danh sách xuống còn **3 bản ghi**, rồi chuyển sang thẻ "Đã ẩn" còn
  **1 bản ghi**; bấm [Xóa bộ lọc] → danh sách quay lại **20 dòng trên trang 1 của 23 bản ghi**, đúng mặc
  định. Tham số trên thanh địa chỉ cũng sạch: từ
  `?linhVucId=…&tuNgay=2026-07-01&denNgay=2026-07-31&page=1&tab=AN` về đúng `?page=1`.
- **Số đếm trên thẻ "Tất cả" trở về đúng số mặc định, không kẹt ở số của lần lọc cũ**: trước khi lọc thẻ
  hiện **"Tất cả 23"**; trong lúc lọc thẻ hiện **"Tất cả 3"**; sau khi bấm [Xóa bộ lọc] thẻ trở lại
  **"Tất cả 23"**. Số đếm bám đúng bộ lọc đang áp và về đúng mốc mặc định.
- **Thanh thẻ phân loại tự về "Tất cả"** — đây chính là điểm phản ánh gốc: cả hai lần thử đều đang đứng ở
  thẻ khác ("Nháp" ở lần 1, "Đã ẩn" ở lần 2) và sau khi bấm [Xóa bộ lọc] thẻ **"Tất cả" trở thành thẻ đang
  chọn**, các thẻ còn lại bỏ chọn. Tình trạng "không đưa về tab Tất cả" **không còn**.
- **Bốn ô lọc được xóa trắng**: ô tìm kiếm rỗng, hai ô chọn quay về **"Tất cả"**, hai ô ngày (Từ ngày /
  Đến ngày) rỗng — đo sau cả hai lần thử.
- **Danh sách mặc định sắp theo ngày tạo giảm dần**: đọc cột Ngày tạo của 20 dòng trang 1 và kiểm tra thứ
  tự — giảm dần đúng (`30/07/2026` → `13/07/2026` → … ). Dòng đầu là `Thư mục TKM` (30/07/2026).
- **Hai bộ lọc khác nhau đều cho kết quả đúng** — kết quả của lần thử 1 (từ khóa `TKM` + thẻ "Nháp", đang
  hiện 3 bản ghi) giống hệt lần thử 2 sau khi bấm [Xóa bộ lọc]: về "Tất cả 23", ô lọc trắng, danh sách mặc
  định.

Ảnh: `../image/TKTMBMHD_07-uat-xoa-bo-loc-ve-tat-ca-23.png`

## Ghi nhận thêm

- Không tạo, không sửa, không xóa thư mục nào khi đo phiếu này — chỉ lọc rồi xóa bộ lọc.
