# Đối chiếu điều kiện / Cổng 3 — QLBMHD_02 (Hiển thị cột danh sách biểu mẫu)

Loại bug: **Hiển thị (display) — cột danh sách cố định.** Theo protocol, bug tĩnh (cột hiển thị cố định) không phụ thuộc role/state/data → không cần bảng GAP role/state; chỉ cần **Cổng 3 (SRS yêu cầu vs thực tế web)**. Vẫn verify bằng đúng vai trò đối tác (**CB Nghiệp vụ**) để loại trừ khả năng cột ẩn theo quyền.

**Vai trò đã dùng:** `cbnv_tw` — CB Nghiệp vụ, Trung ương (BTP·TW) — trùng vai trò đối tác (CB Nghiệp vụ). Đây là vai trò NV phạm vi toàn quốc; nếu cột "Cơ quan ban hành" có điều kiện hiển thị theo quyền thì TW là role rộng nhất vẫn phải thấy.

## Bảng đối chiếu Cổng 3 — SRS SCR-VII-02 vs web

| Thành phần đối tác phản ánh thiếu | SRS yêu cầu (dẫn dòng) | Thực tế web (DOM `thead th`, 20/07/2026) | Kết luận |
|---|---|---|:--|
| Cột **Cơ quan ban hành** | SCR-VII-02 #20 `srs-fr-09:657` — "Cột Cơ quan ban hành … **luôn hiển thị** `[STT12]`" | **KHÔNG có.** 11 cột: Mã BM · Tên biểu mẫu · Loại TL · Thư mục · Kích thước · Trạng thái · Đã công khai · Ảnh đại diện · Ngày tạo · Sync Cổng · Hành động | **Thiếu → Open** |
| Bộ lọc/cột **Định dạng** | SCR-VII-02 #3 filter `srs-fr-09:640` — "Lọc lĩnh vực / loại hình / thư mục / **định dạng**". Không có **cột** "Định dạng" (cột #6 là "Loại TL/Loại tài liệu") | **Bộ lọc "Định dạng" CÓ** trên thanh lọc (Thư mục · Lĩnh vực · Loại hình · Định dạng). Không có cột "Định dạng" (đúng SRS — cột format là "Loại TL") | **Không thiếu / không sai SRS** |
| **Ô chọn biểu mẫu** (checkbox chọn dòng) | SCR-VII-02 (dòng 634–658) **KHÔNG** quy định checkbox chọn hàng loạt cho biểu mẫu; thao tác hàng loạt chỉ có ở màn **Thư mục** (SCR-VII-01) và wizard **Nhập hàng loạt** | Không có checkbox chọn dòng (`thead` không có `.ant-checkbox`) | **SRS im lặng → BA confirm** (không phải bug theo SRS) |

## Verdict từng ý

- **Cơ quan ban hành** → `Open` (BUG-QLBMHD_02): SRS quy định rõ cột luôn hiển thị, web thiếu.
- **Định dạng** → không phải bug: bộ lọc đã có; SRS không có cột "Định dạng" riêng (Loại TL đã thể hiện định dạng qua icon doc/xls).
- **Ô chọn biểu mẫu** → `BA confirm`: SRS không quy định chọn hàng loạt cho biểu mẫu → cần BA quyết có bổ sung không.

**Verdict tổng (theo protocol "≥1 ý Open → Open"): `Open`.**

Evidence: [`../bug-reports/bieu-mau/image/BUG-QLBMHD_02-danhsach-cot.png`](../bug-reports/bieu-mau/image/BUG-QLBMHD_02-danhsach-cot.png) + DOM header list (11 cột, không có "Cơ quan ban hành") trích qua `evaluate_script`.
