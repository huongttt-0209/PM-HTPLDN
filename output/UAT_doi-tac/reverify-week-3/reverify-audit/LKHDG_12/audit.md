# Audit — LKHDG_12 (row 49) · Verdict: Open (BUG-LKHDG_12)

## Cổng 1 — Evidence đối tác
- KQ thực đối tác: (a) "xuất danh sách không đúng với tiêu chí lọc"; (b) "File excel thiếu cột Số vụ việc, Người tạo, Ngày tạo"; (c) "Tần suất, Đối tượng, Trạng thái hiển thị không dấu".

## Cổng 2 — Hiểu bug
- Xuất Excel client-side (endpoint /export trả 404 → không phải server-side). Đọc trực tiếp nội dung file blob sinh ra để kiểm.

## Cổng 3 — Đối chiếu SRS vs file export thực (env 18.143, cbnv_tw) — chi tiết `export-content-doc-duoc.md`
| Mục | SRS / UI | File export thực | Kết luận |
|---|---|---|---|
| Số cột | Danh sách UI có Số vụ việc, Người tạo, Ngày tạo | Export 7 cột: Mã KH, Tên đợt, Tần suất, Đối tượng, Từ ngày, Đến ngày, Trạng thái | THIẾU 3 cột (b) — SAI |
| Tần suất | SCR-VI-01 #12 (dòng 821): "TRON_NAM → 'Tròn năm'" (nhãn tiếng Việt) | Ghi `TRON_NAM` | SAI (c) |
| Trạng thái | SCR-VI-01 #15 (dòng 824): nhãn theo SM-DANHGIA ("Lập kế hoạch"...) | Ghi `LAP_KE_HOACH`/`CHO_PHE_DUYET`/`HOAN_THANH` | SAI (c) |
| Đối tượng | UI hiển thị "Vụ việc" | Ghi `VU_VIEC` | SAI (c) |
| Lọc (a) | Export phải theo bộ lọc | Export không lọc trả đúng 3 đợt (chưa test với filter — session hết hạn) | Chưa tái hiện |

## Verdict: Open — BUG-LKHDG_12 (Medium/P2)
- (b) thiếu cột + (c) ghi mã enum thô thay nhãn tiếng Việt → 2 lỗi thật, tái hiện trên file export. ≥1 Open → case Open.
- (a) chưa tái hiện; ghi rõ trong note để dev/BA lưu ý.
- Evidence: `export-content-doc-duoc.md` (nội dung đọc từ blob) + `export-danhsach-dot.xlsx` (file gốc, sheet1.xml xác nhận 7 cột A1:G4).
