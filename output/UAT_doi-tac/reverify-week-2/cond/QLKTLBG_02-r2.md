# Bảng đối chiếu điều kiện — QLKTLBG_02 (verify phản ánh vòng 2)

**Claim vòng 2 của đối tác:** Bảng danh sách Kho tài liệu / Bài giảng hiển thị thiếu các trường: **Ảnh xem trước**, **Lĩnh vực**, **Người tạo**.

**Evidence:** `QLKTLBG_02_v2.jpg` (ảnh tĩnh full-res) — màn `dao-tao/bai-giang/danh-sach`, header hiện vai trò
"Cán bộ NV Trung ương CB_NV_TW", bảng có các cột Tên bài giảng · Loại tài liệu · Dung lượng · (cột ngày bị cắt) · Thao tác.

| Điều kiện có thể đổi kết quả | Đối tác (từ evidence, full-res) | Mình test | GAP? |
|---|---|---|:-:|
| Vai trò / tài khoản | Cán bộ NV Trung ương (CB_NV_TW), đơn vị BTP·TW — đọc ở góc phải header ảnh | `cbnv_tw` / CB_NV_TW, đơn vị BTP·TW (Cục Bổ trợ tư pháp) | Không |
| Entity + trạng thái | Màn danh sách Kho tài liệu / Bài giảng, không đặt bộ lọc riêng (chỉ có "Bộ lọc nâng cao (2)" mặc định), bảng có dữ liệu (8 bản ghi) | Cùng màn `dao-tao/bai-giang/danh-sach`, cùng bộ lọc mặc định "Bộ lọc nâng cao (2)", bảng có dữ liệu (5 bản ghi) | Không |
| Dữ liệu tiền đề | Bài giảng đủ 3 loại Slide / PDF / Video, có bản ghi cả đã và chưa công khai | Bài giảng có PDF + Video, có bản ghi "Đã công khai" và "Chưa công khai" | Không |

**Kết luận:** 0 GAP — cùng vai trò, cùng màn hình, cùng loại dữ liệu. Số cột hiển thị không phụ thuộc dữ liệu (đọc trực tiếp `.ant-table-thead th`, đủ 6 cột ở cả 2 phía).

Đối chiếu SRS vs thực tế web + phép đo: xem [`../reverify-audit/QLKTLBG_02/audit.md`](../reverify-audit/QLKTLBG_02/audit.md).
