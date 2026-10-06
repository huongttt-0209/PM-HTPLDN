# Bảng đối chiếu điều kiện — verify QLTVV_28 (row 48)

Đối tác phản ánh: xóa Tư vấn viên đang có vụ việc chưa hoàn thành → hệ thống báo CHUNG CHUNG
"Không thể xóa tư vấn viên. Vui lòng thử lại." thay vì nêu lý do nghiệp vụ. Evidence: video
KTDGKQHT... nhầm — video QLTVV_28.webm, frame t≈27s: role CB_NV_TW, danh sách TVV "Đang hoạt động",
bấm Xóa TVV "TVV R11 Verify Mail Fix" → hộp "Xác nhận xóa" → bấm Xóa → toast đỏ
"Không thể xóa tư vấn viên. Vui lòng thử lại."

Verify 2026-07-16: login `cbnv_tw` (CB_NV_TW) → Mạng lưới Tư vấn viên → Tư vấn viên/Chuyên gia →
tab "Đang hoạt động" → bấm Xóa TVV "QA TVV Seed28 Active" (đang có vụ việc đang xử lý — hệ thống
xác nhận bằng chính hành vi chặn xóa) → hộp "Xác nhận xóa" → bấm Xóa → quan sát toast.

| Điều kiện | Đối tác (vòng 1, từ evidence full-res) | Mình test | GAP? |
|---|---|---|---|
| Vai trò/tài khoản thực hiện xóa | CB Nghiệp vụ Trung ương (CB_NV_TW) | CB Nghiệp vụ Trung ương `cbnv_tw` (CB_NV_TW) — cùng vai trò/cấp | Không |
| Trạng thái TVV bị xóa | TVV "Đang hoạt động" | TVV "QA TVV Seed28 Active" (TVV-BTP-TW-0002) "Đang hoạt động" | Không |
| Dữ liệu tiền đề: TVV có vụ việc chưa hoàn thành | TVV đang có vụ việc chưa hoàn thành (theo mô tả đối tác) | TVV có vụ việc đang xử lý — được xác nhận bởi chính việc hệ thống CHẶN xóa với lý do "TVV còn vụ việc đang xử lý" | Không |
| Thao tác | Bấm Xóa trên dòng → hộp xác nhận → bấm Xóa | Bấm Xóa trên dòng → hộp "Xác nhận xóa" → bấm Xóa (giống hệt) | Không |
