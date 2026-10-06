# Audit — LKHDG_04 (row 45) · Verdict: Open (BUG-LKHDG_04)

## Cổng 1 — Evidence đối tác
- File: `partner-evidence/LKHDG_04.webm` (video). Frames: `frames/t000..t010`.
- Frame t002/t006: chi tiết đợt DG-20260526-0003, Tên đợt "Đợt đánh giá hiệu quả" (đợt tồn tại, đối tác bôi đen copy tên).
- Frame t008: về danh sách, ô search focus.
- Frame t010 (KHOẢNH KHẮC LỖI): URL `?keyword=Đợt+đánh+giá+hiệu+quả` → bảng "Không có kế hoạch đánh giá nào phù hợp".

## Cổng 2 — Hiểu bug
- Đối tác báo: search trả "Không tìm thấy" dù tồn tại dữ liệu phù hợp (search full tên "Đợt đánh giá hiệu quả").
- Loại: Filter/Search (phụ thuộc input + data) → cần bảng đối chiếu điều kiện: `cond/LKHDG_04.md` (0 GAP).

## Cổng 3 — Đối chiếu SRS vs web
| Mục | SRS | Web thực tế (env 18.143, cbnv_tw) | Kết luận |
|---|---|---|---|
| Ô tìm kiếm lọc tên/mã đợt | SCR-VI-01 #3 (line 812): "Ô tìm kiếm \| Từ khóa (tên đợt, mã đợt) \| change → filter" | Baseline 2 record. "Đợt đánh giá seed 2026"→0; "Đợt"→0; "seed"→1 | Search fail với dấu tiếng Việt → SAI |
| AC danh sách | FR-VI-01 AC (line 156) danh sách KH thuộc đơn vị | Search theo tên đợt (có dấu) không trả record | Vi phạm |

## Verdict: Open — BUG-LKHDG_04 (Major/P1)
- Search theo tên đợt (luôn có dấu tiếng Việt) trả 0 kết quả → tính năng tìm theo tên hỏng. Workaround = từ khóa ASCII/mã → Major.
- Root-cause khả dĩ (không prescribe): so khớp từ khóa không chuẩn hóa dấu — dev tự chọn cách fix (normalize keyword ↔ dữ liệu).
- Bug-report: `bug-reports/Pass-bug-report-DGHQ-batchA.md`. Evidence: `bug-reports/image/BUG-LKHDG_04-search-dau-tv-0ketqua.png`.
- Note sheet: `note.txt`.

## Ngoài phạm vi — quan sát thêm
- Đã thấy đợt "DGHQ-B1-20260720 Batch B downstream" (Session 2 seed) — parallel session hoạt động, không đụng.
- Không phát hiện lỗi khác khi test search.
