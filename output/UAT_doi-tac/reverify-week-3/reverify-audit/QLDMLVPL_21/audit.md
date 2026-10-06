# Audit — QLDMLVPL_21 (row 127) — Reject

**Verdict:** Reject (lỗi đối tác báo không tái hiện). Verify 21/07/2026, Chrome DevTools MCP, account `admin`/QTHT, env `18.143.165.120.nip.io`.

## Evidence đối tác đã xem
- File: `partner-evidence/QLDMLVPL_21.webm` (video ~10s, env `htpldn-uat.ospgroup.vn`, clock 13/07/2026).
- Frame chứa hành vi tranh chấp: `frames-QLDMLVPL_21/t010.12s.jpg` — URL `...LINH_VUC_PL?sortBy=ten&sortOrder=DESC&page=1`, tooltip "Nhấp để hủy sắp xếp", nhưng danh sách VẪN theo thứ tự thu_tu (Thuế 1, Lao động 2, Đất đai 3...), KHÔNG sort theo tên → build cũ của đối tác: URL đổi param nhưng data không re-sort.
- Frame t004 `frames-QLDMLVPL_21/t004.04s.jpg`: chuột trên cột THỨ TỰ, tooltip "Nhấp để sắp xếp giảm dần" → build đối tác còn cho THỨ TỰ sortable (trái SRS STT69).

## Đối tác phản ánh
Nhấn tên cột KHÔNG sắp xếp. Kỳ vọng: luân phiên tăng/giảm; mặc định Thứ tự↑ rồi Tên↑.

## Kết quả verify web hiện tại (real-data)
- 10 record tên khác nhau (đủ ≥3 để quan sát sort).
- Baseline: thu_tu ASC — Thuế(1)...Đầu tư(10). `baseline-thutu-order.png`.
- Click header **Tên** → ASC: Dân sự, Doanh nghiệp, Đất đai, Đầu tư, Hành chính, Hình sự, Lao động, Sở hữu trí tuệ, Thuế, Thương mại (aria-sort=ascending, cột Thứ tự lộn xộn → sort thực theo ten). `ten-asc.png`.
- Click **Tên** lần 2 → DESC: đảo ngược (aria-sort=descending), tooltip "Nhấp để hủy sắp xếp". `ten-desc.png`.
- Chỉ cột Tên có mũi tên sort; Mã/Mô tả/Thứ tự không sortable → khớp SRS STT69.

## SRS line
- `input/srs-update-2026-5-5/srs-fr-10-quan-tri.md:1572` — cột Tên: sort (click tiêu đề → `ten` ASC↔DESC); Mã/Mô tả/Thứ tự KHÔNG sortable [STT69 UAT 2026-06-02].
- `input/srs-update-2026-5-5/srs-fr-10-quan-tri.md:1608` — mặc định thu_tu ASC, ten ASC; click Tên re-sort ten ASC↔DESC, không sắp Tên thì về mặc định.

## Kết luận
Web hiện tại sort theo cột Tên hoạt động đúng SRS, luân phiên ASC↔DESC↔mặc định. Lỗi đối tác báo (click tên cột không sort) KHÔNG tái hiện — nghi build cũ của đối tác chưa fix. → Reject, đối tác kiểm tra lại.
