# Audit — LKHDG_02 (row 43) · Verdict: BA confirm

## Cổng 1 — Evidence đối tác
- File: `partner-evidence/LKHDG_02.jpg` (tải qua fetch_evidence.py, 311725 bytes).
- Nội dung: ảnh danh sách đợt đánh giá trên env đối tác `htpldn-uat.ospgroup.vn/danh-gia/ke-hoach/danh-sach`.
- Neo dữ kiện: (a) màn Danh sách đợt đánh giá; (b) đối tác env cũ — các cột hiển thị: Mã kế hoạch, Đối tượng, Từ ngày, Đến ngày, Số vụ việc, Trạng thái, Người tạo, Ngày tạo, Hành động (KHÔNG có cột Tên đợt/Tần suất); (c) không có dữ liệu tiền đề đặc biệt.

## Cổng 2 — Hiểu bug
- Đối tác phản ánh: "Tên đợt là thông tin quan trọng nhưng cắt bớt quá nhiều dẫn đến khó quan sát".
- Loại bug: Hiển thị (static/layout) → Cổng 3 (SRS vs web), không cần bảng đối chiếu điều kiện.

## Cổng 3 — Đối chiếu SRS vs web (env mình: 18.143.165.120.nip.io, login cbnv_tw CB_NV_TW)
| Mục | SRS (srs-fr-08-danh-gia.md) | Web thực tế | Kết luận |
|---|---|---|---|
| Cột "Tên đợt" tồn tại | SCR-VI-01 Phần A #11 (line 820): "Tên đợt \| text \| Tên đợt đánh giá (cắt bớt + '...')" | CÓ cột "Tên đợt" | ✅ Đủ cột |
| Cắt bớt tên | SRS quy định "(cắt bớt + '...')" = cắt là ĐÚNG thiết kế | Cắt bớt: header cột → "Tên đ...", giá trị "Đợt đánh giá seed 2026" → "Đợt đánh..." | Cắt bớt đúng design nhưng RẤT hẹp (cả header bị cắt) |
| Độ rộng cột / mức cắt | SRS KHÔNG quy định | Cột quá hẹp | SRS silent → BA quyết |

- Evidence web: `web-danhsach.png` (full-res, thấy rõ header "Tên đ..." + cell "Đợt đánh...").

## Verdict: BA confirm
- Lý do: Cột Tên đợt tồn tại, cắt bớt là đúng SRS line 820. Không có clause SRS nào bị vi phạm (không Open). Bug có tái hiện (không Reject). Đối tác quan sát đúng nhưng kỳ vọng "đọc được đầy đủ" là mức độ hiển thị SRS chưa quy định → BA confirm.
- Câu hỏi BA: mở rộng cột Tên đợt hoặc thêm tooltip full-name khi hover, hay giữ cắt bớt như hiện tại?
- Note sheet: `note.txt`.

## Ngoài phạm vi — quan sát thêm
- Env mình danh sách chỉ có 1 record seed (KHDG-SEED-0001). Cột theo SRS đủ (Mã kế hoạch, Tên đợt, Tần suất, Đối tượng, Từ ngày, Đến ngày, Số vụ việc, Trạng thái, Người tạo, Ngày tạo, Hành động).
- Khác biệt nhỏ: SRS #14 gộp "Kỳ đánh giá" thành 1 cột range; web tách "Từ ngày"/"Đến ngày". Chưa đủ mức log bug (minor, chưa thuộc case).
- Không phát hiện thêm lỗi nghiêm trọng khác trên màn này.
