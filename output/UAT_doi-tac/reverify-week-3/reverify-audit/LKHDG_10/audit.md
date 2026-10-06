# Audit — LKHDG_10 (row 48) · Verdict: BA confirm

## Cổng 1 — Evidence đối tác
- KQ thực đối tác: "Không giữ/chuyển đến màn hình chi tiết đợt" sau khi Lưu nháp.
- KQ mong đợi đối tác: hiện thông điệp "Đã lưu đợt đánh giá" + giữ user ở màn chi tiết đợt; tự sinh mã DG-{ngày}-{seq}; lưu trạng thái "Lập kế hoạch".

## Cổng 2 — Hiểu bug
- Đối tác test nút "Lưu nháp" trên form Tạo kế hoạch. Vấn đề nêu: sau lưu không điều hướng sang màn chi tiết. Deterministic — không phụ thuộc data/state combinatorial.

## Cổng 3 — Đối chiếu SRS vs web (env 18.143, cbnv_tw)
| Mục | SRS FR-VI-01 (UC83) | Web thực tế | Kết luận |
|---|---|---|---|
| Toast thành công | Outputs #3 (dòng 139): "Thông báo thành công \| Toast" | "Tạo kế hoạch đánh giá thành công" | ĐẠT |
| Mã tự sinh | Outputs #2 (dòng 138) + Processing #3 (dòng 120): DG-{YYYYMMDD}-{SEQ} | DG-20260720-0002 | ĐẠT |
| Trạng thái | Postconditions (dòng 143): tạo record LAP_KE_HOACH | Đợt ở "Lập kế hoạch" | ĐẠT |
| Điều hướng sau lưu | **SRS KHÔNG quy định** (không có ở Outputs/Postconditions) | Ở lại danh sách, không sang chi tiết | SRS SILENT |

## Verdict: BA confirm
- Hệ thống đáp ứng đủ 3 yêu cầu SRS-mandated (toast + mã + trạng thái LAP_KE_HOACH). Không có clause SRS nào bị vi phạm → không Open.
- Hiện tượng "không sang chi tiết" CÓ tái hiện (app ở lại danh sách) → không Reject.
- Kỳ vọng "chuyển màn chi tiết" của đối tác nằm ngoài SRS (SRS silent về navigation sau lưu) → BA quyết chuẩn hoá.
- Evidence: `web-luunhap-stay-list.png` (đợt DG-20260720-0002 ở "Lập kế hoạch" trong danh sách sau lưu). Note sheet: `note.txt`.

## Ghi chú phụ (đã tạo data phục vụ test downstream)
- Đợt DG-20260720-0002 (LAP_KE_HOACH) do lần test này tạo — dùng làm precondition cho LKHDG_16/19/20/21/22 (màn Sửa cần đợt Lập kế hoạch/Phân công).
