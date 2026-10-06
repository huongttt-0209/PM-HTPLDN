# Bảng đối chiếu điều kiện — QLBMHD_12 (nút "Sửa" trên biểu mẫu Công khai)

Loại bug: **Hiển thị nút Sửa theo trạng thái biểu mẫu.** Đối tác kỳ vọng nút Sửa CHỈ hiện khi biểu mẫu Nháp/Ẩn + đúng đơn vị; thực tế nút Sửa hiện cả trên biểu mẫu "Đã công khai" (CONG_KHAI). Verdict phụ thuộc: tái hiện đúng role + đúng biểu mẫu Công khai + đối chiếu điều kiện hiển thị SRS.

| Điều kiện có thể đổi kết quả | Đối tác (từ evidence QLBMHD_12.jpg, full-res) | Mình test | GAP? |
|---|---|---|:-:|
| Vai trò người xem | **CB Nghiệp vụ - TW** (CB_NV_TW, BTP·TW) | `cbnv_tw` — CB Nghiệp vụ - Trung ương (BTP·TW), cùng vai trò | Không |
| Trạng thái biểu mẫu kiểm | Biểu mẫu **Đã công khai** (dòng "Test Download", "Hợp đồng lao động" — Công khai) có nút Sửa | "Biểu mẫu hợp đồng tư vấn seed" (BM-SEED-0001) — **Đã công khai / Công khai** — có nút Sửa | Không |
| Đơn vị sở hữu | Biểu mẫu thuộc đơn vị người xem (BTP·TW) | Cả 2 biểu mẫu hiển thị đều thuộc phạm vi BTP·TW | Không |
| Đối tượng so sánh (nút Sửa) | Nút **Sửa** hiển thị trên hàng biểu mẫu Công khai | Nút **Sửa** hiển thị trên BM-SEED-0001 (Công khai) VÀ BM-20260715-001 (Nháp) — evaluate_script + screenshot | Không |

**Kết luận: 0 GAP về role/state/đơn vị.** Tái hiện đúng: nút Sửa CÓ hiện trên biểu mẫu Công khai (khớp đối tác). Đối chiếu SRS:

- SRS `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-09-bieu-mau.md:649` (SCR-VII-02 thành phần #12 — Cột Hành động): **"Xem trước (mặc định) / Tải về / Sửa / Xóa"** — **KHÔNG** kèm điều kiện trạng thái cho nút Sửa (khác SCR-VII-01:615 dành cho *thư mục*, nơi điều kiện "(khi NHAP/AN, rỗng)" chỉ gắn với nút **Xóa**, cũng không gắn với Sửa).
- SRS `:372` (FR-VII-04 AC): "Given CB NV chỉnh sửa When cập nhật + upload lại file (nếu cần) Then validate và lưu" — **không** ràng buộc trạng thái.
- SM-BIEUMAU (`:826`–`:856`): NHAP→CONG_KHAI↔AN — chỉnh sửa nội dung không phải chuyển trạng thái; không có quy tắc nào cấm sửa khi CONG_KHAI.

→ App hiện nút Sửa trên biểu mẫu Công khai **PHÙ HỢP với SRS hiện hành** (SRS không cấm). Kỳ vọng đối tác (Sửa chỉ Nháp/Ẩn) là ràng buộc **SRS chưa quy định** → bất đồng về **đặc tả** → **`BA confirm`** (KHÔNG Reject vì hành vi tái hiện đúng; KHÔNG Open vì không vi phạm clause SRS nào).

Chi tiết: [`../ba-confirm/bieu-mau/ba-confirmation-needed-week-3-bieu-mau-batch5.md`](../ba-confirm/bieu-mau/ba-confirmation-needed-week-3-bieu-mau-batch5.md) (QLBMHD_12).
