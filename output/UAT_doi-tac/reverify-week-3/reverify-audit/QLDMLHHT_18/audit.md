# Audit — QLDMLHHT_18 (row 132) — Reject

**Verdict:** Reject. Verify 21/07/2026, Chrome DevTools MCP, `admin`/QTHT, env `18.143.165.120.nip.io`. Cùng cụm gốc với QLDMLVPL_21 (B6 sort).

## Evidence đối tác đã xem
- File: `partner-evidence/QLDMLHHT_18.webm` (env `htpldn-uat.ospgroup.vn`, clock 13/07/2026).
- Frame lỗi: `frames-QLDMLHHT_18/t012.09s.jpg` — URL `...LOAI_HINH_HO_TRO?...sortBy=ten&sortOrder=DESC`, nhưng danh sách VẪN thứ tự thu_tu (LHHT_TKM 0, Tư vấn pháp luật 1, Tham gia tố tụng 2...), không sort theo tên → build cũ: URL đổi param nhưng data không re-sort.
- Frame t006: chuột trên THỨ TỰ, tooltip "Nhấp để hủy sắp xếp" → build đối tác còn cho THỨ TỰ sortable (trái STT69).

## Đối tác phản ánh
Nhấn tên cột KHÔNG sắp xếp.

## Kết quả verify web hiện tại (real-data)
- 6 record tên khác nhau (đủ ≥3).
- Baseline thu_tu ASC. `baseline-thutu-order.png`.
- Click Tên → ASC (Đại diện ngoài tố tụng, Đào tạo/bồi dưỡng, Hòa giải, Tham gia tố tụng, Trợ giúp khác, Tư vấn pháp luật), aria-sort=ascending, cột Thứ tự lộn xộn. `ten-asc.png`.
- Click Tên lần 2 → DESC (đảo ngược), aria-sort=descending, tooltip "Nhấp để hủy sắp xếp". `ten-desc.png`.
- Chỉ cột Tên sortable → khớp STT69.

## SRS line
- `input/srs-update-2026-5-5/srs-fr-10-quan-tri.md:1572` — cột Tên sort ten ASC↔DESC; Mã/Mô tả/Thứ tự KHÔNG sortable [STT69].
- `input/srs-update-2026-5-5/srs-fr-10-quan-tri.md:1608` — click Tên re-sort ten ASC↔DESC.

## Kết luận
Web hiện tại sort theo cột Tên đúng SRS. Lỗi đối tác báo KHÔNG tái hiện — nghi build cũ. → Reject, đối tác kiểm tra lại.
