# Bảng đối chiếu điều kiện — QLBMHD_15 (màn Chi tiết biểu mẫu "không có nút chức năng")

Loại bug: **Thiếu nút chức năng trên màn Chi tiết biểu mẫu.** Đối tác kỳ vọng màn Chi tiết (khi bấm "Xem") có các nút chức năng; thực tế (theo đối tác) "màn hình không có nút chức năng". Verdict phụ thuộc: đúng vai trò + mở đúng màn Chi tiết biểu mẫu + biểu mẫu tồn tại (có file).

| Điều kiện có thể đổi kết quả | Đối tác (từ evidence QLBMHD_15.jpg + Excel row 108) | Mình test | GAP? |
|---|---|---|:-:|
| Vai trò | **CB Nghiệp vụ - TW** (CB_NV_TW, BTP·TW) | `cbnv_tw` — CB Nghiệp vụ - Trung ương (BTP·TW), cùng vai trò | Không |
| Màn kiểm | Màn **Chi tiết biểu mẫu** (mục tiêu của thao tác "Xem chi tiết") | Màn Chi tiết biểu mẫu `/bieu-mau/28104008-7b0d-4783-9825-a188ad11a289` (heading "Chi tiết biểu mẫu") | Không |
| Biểu mẫu | Biểu mẫu đã có file (evidence là màn Danh sách các biểu mẫu có file) | BM-20260715-001 — DOCX, có file 943 B, Công khai | Không |

**Kết luận: 0 GAP. Tái hiện: KHÔNG.**

Trên build hiện tại (`18.143.165.120.nip.io`, 2026-07-20), màn **Chi tiết biểu mẫu** hiển thị **đầy đủ 4 nút chức năng** ở góc trên phải, đều **hiện rõ + có style** (không phải node ẩn):

- `eye Xem trước` (uid 26_38)
- `download Tải về` (uid 26_39)
- `edit Sửa` (uid 26_40)
- `delete Xóa` (uid 26_41)

Xác minh qua `take_snapshot` (a11y tree liệt kê 4 button focusable) + screenshot `reverify-audit/QLBMHD_15/QLBMHD_15-detail-has-buttons.png` (4 nút hiện trực quan trên header "Chi tiết biểu mẫu").

Ghi chú evidence đối tác: ảnh `QLBMHD_15.jpg` đối tác đính kèm là **màn Danh sách biểu mẫu** (không phải màn Chi tiết) — và ngay trên màn Danh sách đó, cột "Hành động" cũng ĐÃ có nút chức năng (Tải về / Sửa / Xóa). Cả màn Danh sách lẫn màn Chi tiết đều không rơi vào tình trạng "không có nút chức năng".

Đối chiếu SRS:
- SRS `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-09-bieu-mau.md:649` (SCR-VII-02 — cột Hành động / nút màn chi tiết: "Xem trước (mặc định) / Tải về / Sửa / Xóa"). Hành vi build hiện tại **khớp** SRS (đủ 4 nút).

→ **`Reject`** (không tái hiện): màn Chi tiết biểu mẫu có đầy đủ nút chức năng theo SRS; lỗi "màn hình không có nút chức năng" không còn xảy ra trên build hiện tại. Nếu đối tác vẫn gặp trên bản mới → gửi lại video thao tác cụ thể (đường dẫn màn hình + biểu mẫu) để re-verify.

Chi tiết: bug KHÔNG log (Reject); không tạo bug-report entry.
