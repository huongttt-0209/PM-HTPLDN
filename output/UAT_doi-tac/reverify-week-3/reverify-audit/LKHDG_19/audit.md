# Audit — LKHDG_19 (row 51) · Verdict: BA confirm (mâu thuẫn SRS)

## Cổng 1 — Evidence đối tác
- KQ thực đối tác: "Không hiển thị trường thông tin Cơ quan được đánh giá" (màn Chi tiết đợt, tab Kế hoạch).

## Cổng 2 — Hiểu bug
- Case kiểm tra hiển thị trường trong chi tiết đợt. Đối tác nêu thiếu 1 trường (Cơ quan được đánh giá). Static display — Cổng 3.

## Cổng 3 — Đối chiếu SRS vs web (env 18.143, cbnv_tw, đợt DG-20260720-0002)
| Mục | SRS | Web thực tế | Kết luận |
|---|---|---|---|
| Trường hiển thị ở thẻ Thông tin đợt | SCR-VI-01 #28 (dòng 849): "Mã đợt, Tên đợt, Tần suất, Kỳ đánh giá, Đối tượng (read-only)" — 5 trường, KHÔNG có Cơ quan được đánh giá | Hiển thị: Mã, Tên, Tần suất, Đối tượng, Thời gian BĐ/KT, Số vụ việc, Điểm TB. Thiếu "Cơ quan được đánh giá" | App KHỚP display spec #28 (spec không liệt kê Cơ quan) |
| co_quan_duoc_danh_gia | Data model KE_HOACH_DANH_GIA #16 (dòng 1033): `co_quan_duoc_danh_gia_id | Y | FK→DON_VI | Cơ quan được đánh giá` — BẮT BUỘC (v3.5) | User nhập "Bộ Công an" khi tạo, nhưng không xem lại được ở chi tiết | Field bắt buộc nhưng không có trong display spec |

## Verdict: BA confirm (SRS contradiction)
- Không Open: display spec #28 (dòng 849) KHÔNG yêu cầu hiển thị "Cơ quan được đánh giá" → không có clause bị vi phạm rõ ràng.
- Không Reject: hiện tượng "không hiển thị Cơ quan" CÓ tái hiện.
- Mâu thuẫn SRS: field bắt buộc (data model dòng 1033) nhưng vắng ở display spec chi tiết (dòng 849). BA quyết có bổ sung hiển thị không.
- Evidence: `web-chitiet-thieu-coquan.png`. Note sheet: `note.txt`.
