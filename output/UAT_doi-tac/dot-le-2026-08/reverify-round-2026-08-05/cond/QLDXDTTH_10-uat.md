# QLDXDTTH_10 — đo lại trên môi trường nghiệm thu đối tác (05/08/2026)

Tiêu chí lấy nguyên khối ở cột `DEV phản hồi lần 2`, dòng 134 (tab `UAT_TGPL Doanh Nghiệp-tuần 2`).

| Điều kiện | Bug gốc (khối tiêu chí) | Mình test | GAP? |
|---|---|---|---|
| Môi trường | Môi trường nghiệm thu của đối tác, bản mới nhất | `https://htpldn-uat.ospgroup.vn` — nhãn `HTPLDN · V1.0.7` | Không |
| Vai trò | Cán bộ nghiệp vụ cấp Trung ương | `cbnv_tw` · CB_NV_TW · cấp TW · Cục Bổ trợ tư pháp | Không |
| Màn hình | Bảng Đề xuất đào tạo | Đào tạo → Chương trình đào tạo → thẻ "Đề xuất đào tạo" (`/dao-tao/chuong-trinh/danh-sach?type=de-xuat`) | Không |
| Phạm vi rà | Toàn bộ đề xuất đang có, không để bộ lọc che | Thẻ "Tất cả", 17/17 bản ghi trên 1 trang, đối chiếu thêm bằng dữ liệu máy chủ trả về | Không |
| Màn chi tiết | Chi tiết đề xuất cũng hiển thị người đề xuất | Mở chi tiết đề xuất "kiểm thử độc lập test" | Không |
| Thao tác đo | Đọc trên giao diện | Đọc bảng + cây trợ năng của trang (loại trừ cột bị khuất) + đối chiếu dữ liệu máy chủ | Không |

**Kết luận: 0 GAP → KHÔNG PASS (Reopen).** Điều kiện đo khớp bug gốc, nhưng kết quả không đạt tiêu chí.

## Đối chiếu từng ý của khối tiêu chí

- ✅ **Bảng Đề xuất đào tạo nay có cột "Người đề xuất"** — đúng, cột đã có, nằm giữa "SL dự kiến" và
  "Trạng thái". Phần thiếu cột của phản ánh gốc đã được khắc phục.
- ❌ **"cả 7 đề xuất đang có đều hiện đủ họ tên kèm đơn vị … Không còn đề xuất nào hiện dấu gạch ngang"** —
  không đúng ở thời điểm đo. Môi trường đang có **17 đề xuất** (không phải 7), trong đó **10 dòng hiện dấu
  gạch ngang "—" ở cột Người đề xuất**, chỉ hiện tên đơn vị:
  `kiểm thử độc lập test` (25/07) · `TKM gửi đề xuất đào tạo cán bộ nghiệp vụ quý 3/2026` (23/07) ·
  `TKM đề xuất kiểm thử chức năng` (23/07) · `qwiuh ieuhaiena…` (13/07) ·
  `TKM kiểm thử cập nhật trạng thái bản ghi` (06/07) · `TKM kiểm thử đề xuất chỉnh sửa` (06/07) ·
  `Đào tạo nghiệp vụ giải đáp thắc mắc về thuế TNCN` (03/07) · `dawdddahjwdb…` (02/07) ·
  `Doanh nghiệp đề xuất tổ chức khóa đào tạo về pháp luật lao động…` (23/06) · `tgr rhr regdrgdr drgdrgr` (23/06).
  Chỉ 7 dòng còn lại hiện đủ họ tên — đúng bằng con số 7 mà dev báo, nghĩa là lượt kiểm của dev chỉ nhìn thấy
  nhóm có tài khoản.
- ❌ **"nhóm đề xuất gửi từ chuyên trang … hiện không còn bản ghi nào trong môi trường"** — không đúng.
  Đúng 10 bản ghi nói trên chính là nhóm này: dữ liệu máy chủ cho thấy chúng không gắn tài khoản người dùng
  mà gắn mã định danh người gửi từ chuyên trang, người tạo là tài khoản hệ thống. Ngày tạo từ 23/06 đến
  25/07/2026, tức đã có sẵn trước thời điểm dev kiểm tra — không phải dữ liệu mới phát sinh.
- ❌ **"màn hình chi tiết cũng hiển thị đúng thông tin này"** — với nhóm trên thì không. Mở chi tiết
  `kiểm thử độc lập test`: dòng "Người đề xuất" hiện `— · Cục Bổ trợ tư pháp - Bộ Tư pháp`.
- ⇒ **Hệ quả nghiệp vụ của phản ánh gốc vẫn còn**: với 10/17 đề xuất, cán bộ vẫn không biết đề xuất là của
  doanh nghiệp / người nào. Yêu cầu ở phần Kết quả mong đợi ("để cán bộ biết đề xuất là của doanh nghiệp /
  người hỗ trợ nào") mới đạt cho 7/17 bản ghi.

Ảnh: `../image/QLDXDTTH_10-uat-danh-sach-10-dong-gach-ngang.png` ·
`../image/QLDXDTTH_10-uat-chi-tiet-nguoi-de-xuat-gach-ngang.png`

## Ghi nhận thêm — đề nghị làm rõ với BA

Phần còn hụt nằm ở nhóm đề xuất gửi từ chuyên trang: hệ thống chỉ lưu **mã định danh** của người gửi, không
lưu họ tên, nên không có gì để hiển thị. Đây có thể là điểm cần chốt đặc tả chứ không thuần là lỗi dựng:

- Hoặc chuyên trang phải thu và chuyển kèm họ tên / tên doanh nghiệp người gửi;
- Hoặc đặc tả chấp nhận hiển thị nhãn thay thế (ví dụ "Người gửi từ chuyên trang" kèm mã định danh) thay cho
  dấu gạch ngang trống — vì dấu gạch ngang khiến cán bộ hiểu là dữ liệu bị mất.

Đề nghị dev/BA chốt hướng rồi mới đóng phiếu. Không tự nghĩ ra cách hiển thị trong phiếu này.
