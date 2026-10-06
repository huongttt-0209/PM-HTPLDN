# Bảng đối chiếu điều kiện — QLGVTG_07 (verify phản ánh vòng 2)

**Claim vòng 2 của đối tác:** Tab "Thông tin" vẫn cho phép chỉnh sửa ngay tại màn Xem chi tiết giảng viên.

**Evidence:** `QLGVTG_07_v2.jpg` (ảnh tĩnh full-res) — URL `htpldn-uat.ospgroup.vn/dao-tao/giang-vien/bc2ea722-eb29-4b46-b2a6-7afa55fcbf85`
(KHÔNG có hậu tố `/chinh-sua`), breadcrumb `Trang chủ / Đào tạo, tập huấn / Giảng viên / Trợ giảng / **Chi tiết**`,
tab "Thông tin" đang mở, các ô Họ và tên · Chuyên ngành · Trình độ · Tổ chức · Email · Điện thoại đều là ô nhập viền đầy đủ.

| Điều kiện có thể đổi kết quả | Đối tác (từ evidence, full-res) | Mình test | GAP? |
|---|---|---|:-:|
| Vai trò / tài khoản | Cán bộ NV Trung ương (CB_NV_TW), đơn vị BTP·TW — đọc ở góc phải header ảnh | `cbnv_tw` / CB_NV_TW, đơn vị BTP·TW (Cục Bổ trợ tư pháp) | Không |
| Màn hình + chế độ mở | Màn chi tiết giảng viên ở chế độ **Xem**: URL dạng `/dao-tao/giang-vien/{id}` không có `/chinh-sua`, breadcrumb dừng ở "Chi tiết", tab "Thông tin" | Bấm nút 👁 ở cột Hành động màn danh sách → URL `/dao-tao/giang-vien/{id}`, breadcrumb dừng ở "Chi tiết", tab "Thông tin" — trùng khít | Không |
| Bản ghi giảng viên | "Hoàng Minh Đức" (`bc2ea722-eb29-4b46-b2a6-7afa55fcbf85`); ô Trạng thái nằm ngoài khung ảnh nên không đọc được | Kiểm trên **2 bản ghi khác nhau** để loại trừ yếu tố bản ghi: `TS. Lê Hoàng Thái` (`f0fafafa-…-000000000001`) và `QA GV QLGVTG09` (`fb261852-2362-4f0a-a540-215596fd521f`) — cả hai "Đang hoạt động", hành vi giống hệt nhau | Không |
| Dữ liệu tiền đề | Bản ghi có đủ dữ liệu các trường bắt buộc (Họ tên, Chuyên ngành, Trình độ) | Cả 2 bản ghi đều có đủ Họ tên, Chuyên ngành, Trình độ, Email, Điện thoại | Không |

**Kết luận:** 0 GAP — cùng vai trò, cùng màn hình, cùng chế độ mở (Xem), và đã kiểm lặp trên 2 bản ghi khác nhau.

Đối chiếu SRS vs thực tế web + toàn bộ phép đo: xem [`../reverify-audit/QLGVTG_07/audit.md`](../reverify-audit/QLGVTG_07/audit.md).
