# Bảng đối chiếu điều kiện — QLTMBMHD_13 (nút "Xóa" trên thư mục Công khai)

Loại bug: **Hiển thị nút Xóa theo trạng thái + độ rỗng thư mục.** Đối tác kỳ vọng nút Xóa CHỈ hiện khi thư mục Nháp/Ẩn + không chứa biểu mẫu + đúng đơn vị; thực tế nút Xóa hiện cả trên thư mục Công khai (và thư mục còn biểu mẫu). Verdict phụ thuộc: tái hiện đúng role + đúng thư mục Công khai/còn biểu mẫu + đối chiếu điều kiện hiển thị SRS.

| Điều kiện có thể đổi kết quả | Đối tác (từ evidence QLTMBMHD_13.jpg) | Mình test | GAP? |
|---|---|---|:-:|
| Vai trò người xem | **CB Nghiệp vụ - TW** (CB_NV_TW, BTP·TW) | `cbnv_tw` — CB Nghiệp vụ - TW (BTP·TW), cùng vai trò | Không |
| Trạng thái thư mục kiểm | Thư mục **Đã công khai** (tab "Đã công khai", 3 thư mục, đều còn biểu mẫu 2/1/1) | "Thư mục biểu mẫu seed" — **Đã công khai**, 1 biểu mẫu (BTP·TW) | Không |
| Độ rỗng thư mục | Thư mục Công khai còn biểu mẫu bên trong | Test thêm "QA Hidden Folder 715" — **Nháp, còn 1 biểu mẫu** (không rỗng) | Không |
| Đơn vị sở hữu | Thư mục thuộc đơn vị người xem (BTP·TW) | Tất cả thư mục hiển thị đều thuộc BTP·TW | Không |
| Đối tượng so sánh (nút Xóa) | Nút **Xóa** hiển thị trên hàng thư mục Công khai | Nút **Xóa** hiển thị trên "Thư mục biểu mẫu seed" (Công khai) VÀ trên "QA Hidden Folder 715" (Nháp còn biểu mẫu) — evaluate_script + screenshot | Không |

**Kết luận: 0 GAP về role/state/rỗng/đơn vị.** Tái hiện đúng: nút Xóa CÓ hiện trên thư mục Công khai (khớp đối tác) VÀ trên thư mục Nháp còn biểu mẫu. Đối chiếu SRS:

- SRS `srs-fr-09-bieu-mau.md:615` (SCR-VII-01 thành phần #13 — Cột Hành động): **"... / Xóa (khi NHAP/AN, rỗng)"** — điều kiện hiển thị nút Xóa là **trạng thái NHAP hoặc AN VÀ thư mục rỗng (0 biểu mẫu)**.
- Kỳ vọng đối tác (Xóa chỉ khi Nháp/Ẩn + không chứa biểu mẫu) **KHỚP CHÍNH XÁC với SRS**.
- App hiện nút Xóa trên **CONG_KHAI** (vi phạm điều kiện "NHAP/AN") VÀ trên thư mục **còn biểu mẫu** (vi phạm điều kiện "rỗng"). → **Sai điều kiện hiển thị SRS quy định rõ → Open.**
- (Hỗ trợ: SRS `:131` ERR-TM-02 "Thư mục chứa {N} biểu mẫu, không thể xóa" — thư mục còn biểu mẫu không được xóa; nút Xóa hiển thị trên các thư mục này là hành động dẫn tới thao tác không hợp lệ.)

Chi tiết: bug [`../bug-reports/bieu-mau/Pass-bug-report-bieu-mau-batch1.md`](../bug-reports/bieu-mau/Pass-bug-report-bieu-mau-batch1.md) (BUG-QLTMBMHD_13).
