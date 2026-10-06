# Audit — PCNTHDG_10 (row 61) · Verdict: Reject

## Cổng 1 — Evidence đối tác
- KQ mong đợi đối tác: thông điệp "Người đánh giá đã được phân công" (chặn trùng).
- KQ thực đối tác: hệ thống hiển thị thông báo thành công (cho phép trùng).

## Cổng 2 — Hiểu bug
- Test: thêm cùng 1 người 2 lần vào phân công → hệ thống có chặn trùng không.

## Cổng 3 — Đối chiếu SRS vs thực tế (env 18.143, cbnv_tw, đợt DG-20260720-0002)
| Mục | SRS | Thực tế | Kết luận |
|---|---|---|---|
| Chặn người ĐG trùng | SRS SCR-VI-01 #38 (dòng 864): "Backend chỉ cho trình khi ... **không trùng lặp** ..." | Thêm "Cán bộ Nghiệp vụ Demo" lần 1 (Trưởng nhóm) → OK (Tổng 1). Thêm lại đúng người đó → toast "Người đánh giá đã được phân công trong kế hoạch này", modal không đóng, Tổng vẫn 1 | Chặn ĐÚNG |

- DOM: `dupAddToasts=["Người đánh giá đã được phân công trong kế hoạch này"]`, `modalStillOpenAfterDup=true`, `totalAfter="Tổng: 1 người — 1 Trưởng nhóm"`.

## Verdict: Reject
- App chặn người đánh giá trùng ngay tại bước thêm với thông báo rõ ràng — khớp SRS #38 dòng 864 và khớp chính KQ mong đợi của đối tác. Lỗi đối tác báo (cho phép trùng / báo thành công) KHÔNG tái hiện.
- Evidence: `dom-evidence.txt`.
