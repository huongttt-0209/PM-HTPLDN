# Audit — PCNTHDG_06 (row 60) · Verdict: BA confirm

## Cổng 1 — Evidence đối tác
- KQ mong đợi đối tác: bấm "Hủy" → hiển thị cửa sổ xác nhận hủy bỏ thay đổi chưa lưu, sau đó hoàn tác.
- KQ thực đối tác: không hiển thị cửa sổ xác nhận. Video `PCNTHDG_06.webm` (env htpldn-uat.ospgroup.vn): mở modal "Thêm người đánh giá", chọn Người ĐG + Vai trò (Trưởng nhóm), bấm [Hủy] → modal đóng, không xác nhận.

## Cổng 2 — Hiểu bug
- "Hủy" = nút [Hủy] trên modal "Thêm người đánh giá" (xác định qua video đối tác). Test hành vi hủy khi đã nhập input chưa lưu.

## Cổng 3 — Đối chiếu SRS vs thực tế (env 18.143, cbnv_tw, đợt DG-20260720-0002)
| Mục | SRS | Thực tế | Kết luận |
|---|---|---|---|
| Xác nhận khi Hủy modal Thêm người ĐG | SRS SCR-VI-01 KHÔNG quy định modal này phải xác nhận trước khi hủy input chưa lưu (khác Xóa tiêu chí #29 gán C12 confirm) | Bấm [Hủy] (đã chọn Người ĐG + Trưởng nhóm) → modal đóng ngay, `confirmPopup=false`, Tổng: 0 người | SRS SILENT |

- DOM: chọn "Cán bộ Nghiệp vụ Demo" + "Trưởng nhóm" → [Hủy] → `confirmPopup=false`, `addModalStillOpen=false`, `anyModalCount=0`, Tổng 0 người.

## Verdict: BA confirm
- Hành vi (đóng im lặng, không xác nhận) tái hiện đúng như đối tác báo → KHÔNG phải Reject.
- Không có SRS quy định modal cancel phải xác nhận; đóng im lặng khi hủy input chưa commit là chuẩn UX → KHÔNG phải Open.
- SRS silent + kỳ vọng đối tác khác hành vi → BA chốt có cần cửa sổ xác nhận "hủy bỏ thay đổi chưa lưu?" hay không.
- Evidence: `modal-them-nguoi-danh-gia.png`, `dom-evidence.txt`.
