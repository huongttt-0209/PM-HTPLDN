# QLLKHDTBD_50 — đo lại trên môi trường nghiệm thu đối tác (05/08/2026)

Tiêu chí lấy nguyên khối ở cột `DEV phản hồi lần 2`, dòng 144 (tab `UAT_TGPL Doanh Nghiệp-tuần 2`).

| Điều kiện | Bug gốc (khối tiêu chí) | Mình test | GAP? |
|---|---|---|---|
| Môi trường | Môi trường nghiệm thu của đối tác, bản mới nhất | `https://htpldn-uat.ospgroup.vn` — nhãn `HTPLDN · V1.0.7` | Không |
| Vai trò | Cán bộ nghiệp vụ (màn Kế hoạch đào tạo) | `cbnv_tw` · CB_NV_TW · cấp TW · Cục Bổ trợ tư pháp | Không |
| Màn hình | Bảng danh sách Kế hoạch đào tạo | Đào tạo → Kế hoạch đào tạo (`/dao-tao/ke-hoach/danh-sach`) | Không |
| Phạm vi rà | Toàn bộ dòng đang hiển thị (dev đo 14 dòng) | 15/15 dòng trên 1 trang — nhiều hơn 1 dòng so với lúc dev đo | Không |
| Cách đọc cột | Đọc tiêu đề bảng trong mã trang, không để cột bị khuất | Đọc danh sách tiêu đề `th` trong mã trang + cây trợ năng | Không |
| Đối chứng số đếm | Số chương trình phải khớp dữ liệu thực | Đếm độc lập bằng dữ liệu máy chủ: mở từng chương trình (16 bản ghi) lấy kế hoạch gắn kèm rồi cộng theo kế hoạch | Không |
| Phép thử dữ liệu mới | Tạo thêm 1 chương trình gắn vào 1 kế hoạch, xem số có tăng | Tạo `QA doi chung UAT 05-08 - CTDT do dem so chuong trinh` gắn `KH-20260723-0001` | Không |

**Kết luận: 0 GAP → PASS.**

## Đối chiếu từng ý của khối tiêu chí

- **Ô tích chọn dòng + tích ở dòng tiêu đề chọn theo toàn bộ**: bảng đã có cột ô tích. Bấm ô tích ở dòng
  tiêu đề → **15/15 dòng đang hiển thị được chọn**; bấm lại → bỏ chọn hết (0/15). Phản ánh gốc
  "toàn trang không có ô tích nào" đã hết.
- **Đủ cột theo thiết kế**: danh sách tiêu đề đọc trong mã trang là
  `[ô tích] · Mã kế hoạch · Tên kế hoạch · Năm · Từ ngày · Đến ngày · Ngân sách (VNĐ) · Số chương trình ·
  Trạng thái · Người tạo · Ngày tạo · Hành động` — có đủ 4 thành phần trước đây thiếu (ô tích,
  Số chương trình, Người tạo, Ngày tạo).
- **Cột "Người tạo" hiện đúng người lập kế hoạch**: 15/15 dòng có tên người, không dòng nào trống —
  ví dụ `CB Nghiệp vụ TW 01`, `Cán bộ NV Trung ương`, `Cán bộ NV Địa phương`, `CB NV BN 01 (BKH)`,
  `CB NV DP 02 (BG)`, `CB NV BN 02 (BTC)`, `CB Nghiệp vụ TW 02`, `Quản trị viên 1`.
- **Cột "Ngày tạo" đúng dạng ngày/tháng/năm**: 15/15 dòng dạng `dd/mm/yyyy` (03/08/2026 … 08/05/2026).
- **Ngân sách đúng định dạng dấu chấm kèm đơn vị, chưa nhập thì hiện "—", không còn số thô**: 15/15 dòng
  đúng — `100.000.000 đ`, `2.943.499.581 đ`, `1.000.000.000 đ`, `2.500.000.000 đ`, `50.000.000 đ` …
  Hai kế hoạch chưa nhập ngân sách (`KH-20260725-0003`, `KHDT-HDSD-AG-001`) hiện **"—"**; kế hoạch nhập
  số 0 (`KH-20260725-0002`) hiện **"0 đ"** — phân biệt đúng giữa *chưa nhập* và *nhập bằng 0*.
  Không dòng nào ra số thô kiểu `100000000.00`.
- **Cột "Số chương trình" đếm khớp dữ liệu thực tế**: đếm độc lập từ phía dữ liệu — mở từng chương trình
  trong 16 chương trình đang có để lấy kế hoạch mà nó gắn vào, rồi cộng theo kế hoạch. Kết quả **khớp
  15/15 dòng** (1, 0, 0, 1, 1, 4, 0, 1, 0, 0, 3, 0, 0, 3, 2 — tổng 16 đúng bằng tổng số chương trình).
- **Đúng cả với dữ liệu mới phát sinh**: `KH-20260723-0001` đang là **1**; tạo mới chương trình
  `QA doi chung UAT 05-08 - CTDT do dem so chuong trinh` gắn vào chính kế hoạch đó → thông báo
  "Tạo chương trình đào tạo thành công"; tải lại danh sách kế hoạch thì dòng này thành **2**.

Ảnh: `../image/QLLKHDTBD_50-uat-bang-du-cot-tich-chon-toan-bo.png` ·
`../image/QLLKHDTBD_50-uat-so-chuong-trinh-tang-theo.png`

## Ghi nhận thêm

- Dữ liệu phát sinh khi đo (là bước bắt buộc của chính khối tiêu chí): 1 chương trình đào tạo trạng thái
  nháp `QA doi chung UAT 05-08 - CTDT do dem so chuong trinh` gắn kế hoạch kiểm thử `KH-20260723-0001`.
- Môi trường hiện có 15 kế hoạch (dev đo lúc 14) — chênh 1 do dữ liệu phát sinh giữa hai lượt đo, không ảnh
  hưởng kết luận vì mọi tiêu chí đều rà trên toàn bộ dòng đang hiển thị.
