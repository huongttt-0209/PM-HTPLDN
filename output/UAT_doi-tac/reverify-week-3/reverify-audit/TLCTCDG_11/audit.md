# Audit — TLCTCDG_11 (row 58) · Verdict: Reject

## Cổng 1 — Evidence đối tác
- KQ thực đối tác: lưu khi tổng trọng số ≠ 100% báo thành công thay vì cảnh báo.

## Cổng 2 — Hiểu bug
- Kiểm tra hành vi lưu Tab Tiêu chí khi SUM trọng số ≠ 100% — có cho lưu không, có cảnh báo không.

## Cổng 3 — Đối chiếu SRS vs thực tế (env 18.143, cbnv_tw, đợt DG-20260720-0002)
| Mục | SRS | Thực tế | Kết luận |
|---|---|---|---|
| Lưu khi SUM ≠ 100% | Dòng 895: "Tab Tiêu chí... **Cho lưu nếu != 100% nhưng WARNING**"; dòng 201: "cảnh báo nếu khác, **cho phép lưu**" | Bấm "Lưu" (SUM=10%) → toast "Đã lưu tiêu chí đánh giá" | ĐÚNG spec (cho lưu) |
| Cảnh báo khi SUM ≠ 100% | #31 (dòng 852) WRN-TC-01; #30 (dòng 851): nhãn đỏ nếu ≠100% | Hiển thị "Tổng trọng số: 10%(Tổng trọng số phải bằng 100%)" | ĐÚNG spec (có cảnh báo) |
| Bắt buộc = 100% | Dòng 895: chỉ bắt buộc "trước khi thêm/lưu phân công người đánh giá và khi chuyển CHO_DUYET_PC" | — | Không áp cho bước lưu tiêu chí |

- DOM: `weightSummary="Tổng trọng số: 10%(Tổng trọng số phải bằng 100%)"`, `luuDisabled=false`, `toasts=["Đã lưu tiêu chí đánh giá"]`.

## Verdict: Reject
- Hệ thống CHO PHÉP lưu tiêu chí khi SUM ≠ 100% VÀ hiển thị cảnh báo — khớp đúng SRS dòng 895/201/852. Kỳ vọng đối tác (chặn lưu / không cho báo thành công) trái với spec. Không phải lỗi.
- Evidence: `save-weight10-success-with-warning.png`.
