# Bảng đối chiếu điều kiện — QLDMTCTV_OOS_12 (dòng 338) — Ô tìm kiếm không tìm được theo Người đại diện

**Kết luận:** Pass — tìm theo tên người đại diện nay ra đúng tổ chức (thử 4 người khác nhau, 4/4 đúng), và nội dung gợi ý trong ô đã ghi đủ "Tìm theo mã tổ chức, tên tổ chức hoặc người đại diện".

| Điều kiện có thể đổi kết quả | Bug gốc (vòng 1) | Mình đo lại (cbnv_tw, 04/08/2026) | GAP? |
|---|---|---|:-:|
| Vai trò / tài khoản | Cán bộ Nghiệp vụ cấp Trung ương (`cbnv_tw_04`), Cục Bổ trợ tư pháp – Bộ Tư pháp | `cbnv_tw` — `CB_NV_TW`, đơn vị "Bộ Tư Pháp · Cục Bổ trợ tư pháp" (cùng vai trò + cùng cấp + cùng đơn vị) | Không |
| Màn hình / entity + trạng thái | Danh sách Tổ chức tư vấn, thẻ "Đang hoạt động" | Đúng màn `/chuyen-gia-tvv/to-chuc`, thẻ "Đang hoạt động" (8 dòng) | Không |
| Dữ liệu tiền đề | Tổ chức TC-STP-AG-0001, người đại diện "Nguyen Van QA" | Tổ chức đó **không nằm trong thẻ Đang hoạt động** trên môi trường mới (TC-STP-AG-0001 đang ở "Chờ phê duyệt", người đại diện là "Nguyen Van AG"). Vì vậy **lấy tên người đại diện có thật ngay trên bảng đang hiển thị** làm từ khóa: Nguyễn Văn A · Le Van Kappa · Phạm Thị D · Tran Thi Iota | Không |
| Thao tác / input | 3 phép: tìm theo TÊN (đối chứng) → theo MÃ (đối chứng) → theo NGƯỜI ĐẠI DIỆN | Làm đủ 3 kiểu bằng ô tìm kiếm + nút "Tìm kiếm" trên giao diện (xóa sạch ô trước mỗi lần gõ để không dính từ khóa cũ) | Không |

**Kết quả 3 kiểu tìm (thẻ "Đang hoạt động"):**

- Theo TÊN (đối chứng) — từ khóa `Trung tâm TVPL` → **2 kết quả**: TC-BTP-TW-0008 · TC-BTP-TW-0003.
- Theo MÃ (đối chứng) — từ khóa `TC-BTP-TW-0001` → **1 kết quả**: TC-BTP-TW-0001.
- **Theo NGƯỜI ĐẠI DIỆN — từ khóa `Nguyễn Văn A` → 1 kết quả: TC-BTP-TW-0001** (người đại diện = Nguyễn Văn A).
- Theo NGƯỜI ĐẠI DIỆN — từ khóa `Le Van Kappa` → 1 kết quả: TC-BTP-TW-0008 (người đại diện = Le Van Kappa).
- Theo NGƯỜI ĐẠI DIỆN — từ khóa `Phạm Thị D` → 1 kết quả: TC-BTP-TW-0004 (người đại diện = Phạm Thị D).
- Theo NGƯỜI ĐẠI DIỆN — từ khóa `Tran Thi Iota` → 1 kết quả: TC-BTP-TW-0007 (người đại diện = Tran Thi Iota).

Cả 4 từ khóa người đại diện đều KHÔNG trùng với tên tổ chức tương ứng ⇒ kết quả chỉ có thể đến từ tiêu chí người đại diện, không phải ăn theo tiêu chí tên.

**Nội dung gợi ý trong ô tìm kiếm:** đọc thuộc tính `placeholder` = **"Tìm theo mã tổ chức, tên tổ chức hoặc người đại diện"** — khớp nguyên văn đặc tả (bug gốc ghi web chỉ có "Tìm theo tên hoặc mã tổ chức").

**Bằng chứng:** `image/QLDMTCTV_OOS_12-v2-01-tim-theo-nguoi-dai-dien-Nguyen-Van-A-ra-1-ket-qua.png` (đã mở đọc: ô tìm kiếm chứa "Nguyễn Văn A", bảng trả 1 dòng TC-BTP-TW-0001 "Công ty Luật TNHH Alpha Hà Nội", chân bảng ghi "Hiển thị 1-1 / 1 kết quả") · `image/QLDMTCTV_02-v2-03-tich-chon-dong-hien-thanh-thao-tac-hang-loat.png` (thấy rõ toàn bộ nội dung gợi ý trong ô tìm kiếm) · network `GET /api/v1/to-chuc-tu-vans?trangThai=HOAT_DONG&tuKhoa=Nguyễn+Văn+A` [200] · đặc tả `srs-v3.5/srs-fr-04-chuyen-gia-tvv.md` dòng 1631.
