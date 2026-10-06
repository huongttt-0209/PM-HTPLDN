# Audit — LKHDG_03 (row 44) · Verdict: BA confirm

## Cổng 1 — Evidence đối tác
- File: `partner-evidence/LKHDG_03.jpg`. Màn danh sách đợt đánh giá env đối tác. Không mở dropdown → không thấy giá trị filter.

## Cổng 2 — Hiểu bug (3 ý con về bộ lọc)
1. Giá trị tần suất là "Tròn năm", không phải "Trọn năm".
2. Không đặt giá trị mặc định của các danh sách chọn là "Tất cả".
3. Thiếu trường tìm kiếm theo Trạng thái.
- Loại: hiển thị/UI filter (static) → Cổng 3.

## Cổng 3 — Đối chiếu SRS vs web (env mình 18.143, login cbnv_tw)
| Ý | SRS | Web thực tế | Kết luận |
|---|---|---|---|
| #1 chính tả tần suất | SCR-VI-01 #12 (line 821): "TRON_NAM → 'Tròn năm'" | Dropdown + cột hiển thị "**Trọn năm**" | Web ĐÚNG chính tả; lỗi đối tác báo KHÔNG tái hiện. (SRS có thể typo "Tròn năm") |
| #2 default "Tất cả" | SCR-VI-01 #4/#5 (line 813-814): dropdown gồm "Tất cả / ..." | Dropdown Tần suất = ["Sơ bộ 6 tháng","Trọn năm"] — KHÔNG có "Tất cả"; hiện placeholder, không default | App dùng placeholder "không chọn = tất cả" thay mục "Tất cả" → khác SRS |
| #3 lọc trạng thái | SCR-VI-01 #6 (line 815): "Lọc trạng thái \| C10 dropdown" trong thanh lọc | Không có dropdown trạng thái trong thanh lọc; CÓ lọc trạng thái dạng TABS (Tất cả/Lập kế hoạch/.../Hủy) | App đáp ứng bằng tabs, khác dạng dropdown SRS |
- Evidence web: `web-tansuat-dropdown.png` (dropdown Tần suất mở + filter bar + tabs).

## Verdict: BA confirm
- Tổng hợp (protocol §1-case-nhiều-ý): #1 không tái hiện (web đúng); #2 + #3 = app đáp ứng cách khác SRS → có ≥1 ý BA confirm, 0 Open → verdict tổng BA confirm.
- Câu hỏi BA: (a) placeholder có thay được mục "Tất cả" mặc định không? (b) bộ tab trạng thái có thay được dropdown lọc trạng thái không?
- Note sheet: `note.txt`.

## Ngoài phạm vi — quan sát thêm
- Env mình có 2 record: DG-20260720-0001 ("DGHQ-B1-...", do Session 2/Batch B seed hôm nay) + KHDG-SEED-0001. Không phát hiện lỗi khác trên filter.
- Tabs có "Đang đánh giá" + "Đã đánh giá" ngoài 8 state SM-DANHGIA — chưa rõ ánh xạ; chưa đủ mức log, ghi nhận để ý các case sau.
