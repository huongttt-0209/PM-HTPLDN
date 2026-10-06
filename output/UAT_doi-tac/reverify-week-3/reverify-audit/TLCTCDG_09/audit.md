# Audit — TLCTCDG_09 (row 57) · Verdict: Reject

## Cổng 1 — Evidence đối tác
- KQ thực đối tác: lưu tiêu chí khi thiếu trường bắt buộc vẫn báo thành công.

## Cổng 2 — Hiểu bug
- Kiểm tra validate trường bắt buộc ở modal "Thêm tiêu chí" — hành vi tĩnh, deterministic.

## Cổng 3 — Đối chiếu SRS vs thực tế (env 18.143, cbnv_tw)
| Mục | SRS | Thực tế | Kết luận |
|---|---|---|---|
| Trường bắt buộc modal | SCR-VI-01 #29: Tên (bắt buộc), Trọng số (1-100), Điểm tối đa (>0) | Modal có 4 trường bắt buộc: Tên, Nhóm, Trọng số, Điểm tối đa | — |
| Submit thiếu bắt buộc | Validate chặn, không lưu | Bấm "Thêm mới" khi trống → modal KHÔNG đóng, lỗi "Vui lòng nhập tên tiêu chí" / "Vui lòng chọn nhóm tiêu chí" | Validate ĐÚNG |

- DOM: `requiredFields=["Tên tiêu chí","Nhóm tiêu chí","Trọng số (%)","Điểm tối đa"]`; submit trống → `modalStillOpen=true`, `validationErrors=["Vui lòng nhập tên tiêu chí","Vui lòng chọn nhóm tiêu chí"]`.

## Verdict: Reject
- Thiếu trường bắt buộc bị chặn với thông báo rõ ràng, không lưu thành công → lỗi đối tác báo KHÔNG tái hiện.
- Evidence: `modal-required-validation.png`.
