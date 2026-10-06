# Bảng đối chiếu điều kiện — PDHSVV_02

Loại bug: **Phê duyệt vụ việc thành công nhưng (1) không gửi thông báo cho Cán bộ Nghiệp vụ phụ trách, (2) trường "Người duyệt" trong nhóm "Phê duyệt" hiển thị mã định danh (UUID) thay vì tên người duyệt.** Cả 2 ý phụ thuộc role (CB PD cùng đơn vị mới phê duyệt được) + state (Chờ phê duyệt) → điền bảng, xác nhận app thực tế đúng điều kiện đối tác trước khi kết luận.

| Điều kiện có thể đổi kết quả | Đối tác (từ cột Điều kiện/Bước/Kết quả) | Mình test | GAP? |
|---|---|---|:-:|
| Vai trò người thao tác (phê duyệt) | **Cán bộ phê duyệt cùng đơn vị với đơn vị tạo hồ sơ** | `cbpd_tw` — CB_PD_TW, đơn vị BTP·TW (cùng đơn vị với đơn vị tạo hồ sơ VV-BTP-TW-...). Cùng loại vai trò Cán bộ Phê duyệt cùng cấp | Không |
| Trạng thái vụ việc khi phê duyệt | Hồ sơ vụ việc ở **"Chờ phê duyệt"** (có nút [Phê duyệt] [Từ chối]) | VV-BTP-TW-20260712-001 ở **CHO_PHE_DUYET** (có nút [Phê duyệt] [Từ chối]) | Không |
| Thao tác thực hiện | Bấm [Phê duyệt] → xác nhận | Bấm [Phê duyệt] → hộp thoại "Phê duyệt vụ việc" → bấm [Phê duyệt] → toast "Đã phê duyệt", VV → DA_DUYET | Không |
| Ý (1) — người nhận thông báo cần kiểm | "Gửi thông báo cho **cán bộ nghiệp vụ phụ trách hồ sơ**" | Kiểm `cbnv_tw` (CB NV phụ trách, CB_NV_TW — trường "Người tiếp nhận" của VV) | Không |
| Ý (2) — nơi hiển thị Người duyệt cần kiểm | "Lỗi hiển thị thông tin **Người duyệt** trong nhóm **Phê duyệt**" | Kiểm nhóm/accordion "Phê duyệt" ở màn chi tiết VV sau khi phê duyệt (trường "Người duyệt") | Không |

**Kết luận: 0 GAP về role/state/data.** Xác nhận app thực tế đúng như đối tác báo:

- **Đổi trạng thái + ghi người/thời điểm duyệt ĐẠT:** bấm [Phê duyệt] → toast "Đã phê duyệt", VV chuyển CHO_PHE_DUYET → DA_DUYET, dữ liệu ghi `nguoiDuyetId` + `ngayDuyet` (06:23:32Z / 13:23). Đúng SRS.
- **Ý (1) — thông báo THIẾU:** sau khi phê duyệt, `cbnv_tw` (CB NV phụ trách) **KHÔNG có thông báo** nào về việc vụ việc được duyệt — in-app: số chưa đọc giữ nguyên 117, thông báo mới nhất vẫn là mục cũ trước thời điểm duyệt, không có mục nào tạo sau 06:23Z; email: chỉ có thư mã OTP đăng nhập, không có thư báo duyệt. Loại trừ nhiễu: `cbnv_tw` VẪN nhận thông báo loại `PHE_DUYET` cho sự kiện khác (đăng ký/khóa học) → cơ chế thông báo phê duyệt còn hoạt động, chỉ thiếu riêng thông báo **phê duyệt vụ việc**.
- **Ý (2) — Người duyệt hiển thị SAI:** nhóm "Phê duyệt" ở màn chi tiết hiển thị `Người duyệt` = **"ID: 4101cf26-cdbd-4f00-ae38-bc3e380366a3"** (mã định danh UUID nội bộ của người duyệt) thay vì **tên** người duyệt ("CB Phê duyệt - Trung ương"). API chi tiết trả về `nguoiDuyetId` (UUID) nhưng không kèm tên đã phân giải (`nguoiDuyet` = null) → giao diện đổ thẳng UUID kèm tiền tố "ID: ".

Chi tiết: xem [`../reverify-audit/PDHSVV_02/audit.md`](../reverify-audit/PDHSVV_02/audit.md).
